import argparse
import gzip
import json
import os
from collections import defaultdict
from typing import Any, Generator, List, Tuple, Union

import matplotlib
import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np

matplotlib.use('Agg')
hep.style.use("CMS")

parser = argparse.ArgumentParser(description="Plotting comparison of two correction libs")
parser.add_argument("--input_a", type=str, help="json.gz correctionlib file A")
parser.add_argument("--input_b", type=str, help="json.gz correctionlib file B")
parser.add_argument("--tag_a", type=str, help="Name (str) A", default="A")
parser.add_argument("--tag_b", type=str, help="Name (str) B", default="B")
parser.add_argument("--output", type=str, help="Output directory", default="comparison_plots")
args = parser.parse_args()


def windowed(
    iterable: Union[List[Any], Tuple[Any]],
    n: int,
) -> Generator[Tuple[Any, ...], None, None]:
    assert n > 0
    for idx in range(0, len(iterable) - n + 1):
        yield tuple(iterable[idx: idx + n])


def recursive_search(
    json_object: Union[list, dict],
    search_term: str,
) -> bool:
    if isinstance(json_object, dict):
        for key, value in json_object.items():
            if key == search_term or value == search_term:
                return True
            if isinstance(value, (dict, list)):
                if recursive_search(value, search_term):
                    return True
    elif isinstance(json_object, list):
        for item in json_object:
            if item == search_term:
                return True
            if isinstance(item, (dict, list)):
                if recursive_search(item, search_term):
                    return True
    return False


def to_latex(string: str) -> str:
    conversion = {
        "pt_1": r"$p_{T_1}$",
        "pt_2": r"$p_{T_2}$",
        "abs(eta_1)": r"$|\eta_1|$",
        "abs(eta_2)": r"$|\eta_2|$",
        "abs(eta)": r"$|\eta|$",
        "pt": r"$p_T$",
    }
    return conversion[string] if string in conversion else string


def correction_key_to_latex(key: Tuple) -> str:
    return ", ".join([f"{to_latex(name)}$\\in$[{interval[0]}, {interval[1]}]" for name, interval in key])


def correction_key_to_path(key: Tuple) -> str:
    return "_".join([f"_{name}_{interval[0]}_{interval[1]}" for name, interval in key])


class Corrections:
    def __init__(
        self,
        correction_data: dict,
        process_keys: Tuple[str, ...] = ("mc", "emb"),
        ylabel: str = "sf",
    ) -> None:
        self.data = correction_data
        self.process_keys = process_keys
        self.collection: defaultdict = defaultdict(
            lambda: {key: [] for key in self.process_keys}
        )
        self.ylabel = ylabel

        self.collect_corrections()

    @property
    def collection_keys(self) -> List[Tuple[Any, ...]]:
        return list(self.collection.keys())

    @property
    def xlabel(self) -> str:
        return to_latex(self.data["input"])

    @property
    def edges(self) -> np.ndarray:
        return np.array(self.data["edges"])

    def fill_item_wise(self) -> None:
        # for pt and differential eta
        _input: Union[Tuple[Any, ...], None] = None
        for conent in self.data["content"]:
            for i, chunk_i in enumerate(windowed(conent["edges"], 2)):
                _input = ((conent["input"], chunk_i),)
                for _content in conent["content"][i]["content"]:
                    self.collection[_input][_content["key"]].append(_content["value"])

    def fill_vector_wise(self, key: str) -> None:
        # for (pt_1, pt_2, eta_1, eta_2) and (pt_1, eta_1, eta_2)
        _input: Union[Tuple[Any, ...], None] = None
        for content in self.data["content"]:
            for i, chunk_i in enumerate(windowed(content["edges"], 2)):
                _input = ((content["input"], chunk_i),)
                try:
                    if "edges" in content["content"][i]:
                        for j, chunk_j in enumerate(windowed(content["content"][i]["edges"], 2)):
                            _input = (
                                (content["input"], chunk_i),
                                (content["content"][i]["input"], chunk_j),
                            )
                            if "edges" in content["content"][i]["content"][j]:
                                for k, chunk_k in enumerate(windowed(content["content"][i]["content"][j]["edges"], 2)):
                                    _input = (
                                        (content["input"], chunk_i),
                                        (content["content"][i]["input"], chunk_j),
                                        (content["content"][i]["content"][j]["input"], chunk_k),
                                    )
                                    if isinstance(key, str):
                                        self.collection[_input][key].append(content["content"][i]["content"][j]["content"][k])
                                    else:
                                        raise NotImplementedError
                except TypeError:
                    if isinstance(key, str):
                        self.collection[_input][key].append(content["content"][i])
                    else:
                        raise NotImplementedError

    def collect_corrections(self) -> None:
        if recursive_search(self.data["content"], "mc"):
            self.fill_item_wise()
        else:
            if not recursive_search(self.data["content"], "emb"):
                self.process_keys = ("emb",)
            self.fill_vector_wise(key="emb")

    def check_equal_binning(self, other: Any) -> bool:
        if isinstance(other, Corrections):
            equal_edges = all(self.edges == other.edges)
            equal_keys = all(
                it == other_it
                for it, other_it in zip(self.collection_keys, other.collection_keys)
            )
            return equal_edges and equal_keys
        else:
            raise TypeError


def plot_corrections(
    json_a: dict, json_b: dict, tag_a: str, tag_b: str, directory: str
) -> None:
    for num, correction_jsons in enumerate(
        zip(json_a["corrections"], json_b["corrections"])
    ):
        correction_objects = [Corrections(item["data"]) for item in correction_jsons]
        assert correction_objects[0].check_equal_binning(correction_objects[1])
        for num2, key in enumerate(correction_objects[0].collection_keys):
            fig, axes = plt.subplots(
                2,
                len(correction_objects[0].process_keys),
                gridspec_kw=dict(height_ratios=[0.7, 0.3]),
                figsize=(10 * len(correction_objects[0].process_keys), 12),
                sharex=True,
            )
            correction_name = correction_jsons[0]["name"]
            plt.subplots_adjust(hspace=0.1)

            fig.suptitle(correction_name)

            for process, ax in zip(
                correction_objects[0].process_keys,
                [axes[:, 0], axes[:, 1]]
                if len(correction_objects[0].process_keys) > 1
                else [axes],
            ):
                ax[0].set_title(
                    f"{process}: {correction_key_to_latex(key)}",
                    loc="left",
                    fontsize=18,
                )
                for correction_obj, tag_name in zip(correction_objects, [tag_a, tag_b]):
                    hep.histplot(
                        correction_obj.collection[key][process],
                        correction_obj.edges,
                        label=tag_name,
                        ax=ax[0],
                        histtype="errorbar",
                        yerr=False,
                        xerr=True,
                        markerfacecolor="none",
                    )

                _a_array = np.array(correction_objects[0].collection[key][process])
                _b_array = np.array(correction_objects[1].collection[key][process])

                hep.histplot(
                    _a_array / _b_array,
                    correction_obj.edges,
                    label=f"${correction_objects[0].ylabel}_{{{tag_a}}}$ / ${correction_objects[1].ylabel}_{{{tag_b}}}$",
                    ax=ax[1],
                    histtype="errorbar",
                    yerr=False,
                    xerr=True,
                    markerfacecolor="none",
                )

                [_ax.legend() for _ax in ax]

                _max_y_value = max(
                    [
                        max(correction_obj.collection[key][process])
                        for correction_obj in correction_objects
                    ]
                )

                ax[0].set(
                    xscale="log",
                    ylim=(None, _max_y_value + 0.1),
                    ylabel=correction_obj.ylabel,
                )
                ax[1].set(
                    xscale="log",
                    xlabel=correction_obj.xlabel,
                    ylabel="ratio",
                )

                hep.cms.label("Own Work", ax=ax[0], loc=2)

            if not os.path.exists(directory):
                os.makedirs(name="comparison_plots", exist_ok=True)

            os.makedirs(name=os.path.join(directory, correction_name), exist_ok=True)
            for ext in ["pdf", "png"]:
                plt.savefig(
                    os.path.join(
                        directory,
                        correction_name,
                        f"comparison_{correction_name}_{tag_a}_{tag_b}_{correction_key_to_path(key)}.{ext}",
                    ),
                )
            plt.savefig(
                os.path.join(
                    directory,
                    correction_name,
                    f"comparison_{correction_name}_{tag_a}_{tag_b}_{correction_key_to_path(key)}.png",
                ),
            )
            plt.close("all")
            print(f"{num + 1}/{len(json_a['corrections'])} ({num2 + 1}/{len(correction_objects[0].collection_keys)})")


if __name__ == "__main__":
    with gzip.open(args.input_a, "rb") as f:
        json_a, name_json_a = json.load(f), args.tag_a
    with gzip.open(args.input_b, "rb") as f:
        json_b, name_json_b = json.load(f), args.tag_b
    plot_corrections(json_a, json_b, tag_a=name_json_a, tag_b=name_json_b, directory=args.output)

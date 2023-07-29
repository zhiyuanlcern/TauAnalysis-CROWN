import argparse
import gzip
import json
import os
from collections import defaultdict
from itertools import combinations, count, product
from typing import Any, Dict, Generator, List, Tuple, Union

import matplotlib
import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np

matplotlib.use("Agg")
hep.style.use("CMS")

parser = argparse.ArgumentParser(description="Script for visually comparing two correctionlibs by their individual corrections")
parser.add_argument("--input-a", type=str, help="path to a json.gz correctionlib file")
parser.add_argument("--input-b", type=str, help="path to a json.gz correctionlib file that is used for comparison")
parser.add_argument("--tag-a", type=str, help="Name that will be plotted in the legend in form of '$sf_{<tag-a>}$'", default="A")
parser.add_argument("--tag-b", type=str, help="Name that will be plotted in the legend in form of '$sf_{<tag-b>}$'", default="B")
parser.add_argument(
    "--correction-name",
    type=str,
    help="Name of a correction that will only be plotted. Other corrections are skipped when specified",
    default="",
)
parser.add_argument("--output", type=str, help="Output directory", default="comparison_plots")
args = parser.parse_args()


class NestedDefaultDict(defaultdict):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(NestedDefaultDict, self).__init__(NestedDefaultDict, *args, **kwargs)

    def __repr__(self) -> str:
        return repr(dict(self))


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
    return ", ".join([f"{to_latex(name)}$\\in$[{interval[0]}, {interval[1]}]{'' if 'eta' in name else ' GeV'}" for name, interval in key])


def correction_key_to_path(key: Tuple) -> str:
    return "_".join([f"_{name}_{interval[0]}_{interval[1]}" for name, interval in key])


def correction_key_to_prompt(key: Tuple) -> str:
    return ", ".join([f"{name}=[{interval[0]}, {interval[1]}]" for name, interval in key])


def is_expandable(values1: np.ndarray, values2: np.ndarray) -> bool:
    coarse, fine = sorted([values1, values2], key=lambda x: x.shape[0])
    return all(it in fine for it in coarse)


def expand(
    data: np.ndarray,
    edges1: np.ndarray,
    edges2: np.ndarray,
    insertion_along_axis: int = 1,
) -> np.ndarray:
    selection: List[Union[slice, int]] = [slice(None, None, None)] * len(data.shape)

    coarse_edges, fine_edges = sorted([edges1, edges2], key=len)
    is_expandable = all(it in fine_edges for it in coarse_edges)

    fine_edges_iter = windowed(fine_edges, 2)
    coarse_edges_iter = enumerate(windowed(coarse_edges, 2))

    fine_edge = next(fine_edges_iter)
    coarse_edge_idx, coarse_edge = next(coarse_edges_iter)

    insertion_idx_collection, insersions_data_collection = [], []

    if is_expandable:
        while True:
            try:
                # skip if edges are equal
                if fine_edge == coarse_edge:
                    fine_edge = next(fine_edges_iter)
                    coarse_edge_idx, coarse_edge = next(coarse_edges_iter)
                # insertion happens here until fine_edge[1] == coarse_edge[1]
                elif fine_edge[0] == coarse_edge[0] or fine_edge[1] < coarse_edge[1]:
                    fine_edge = next(fine_edges_iter)
                    insertion_idx_collection.append(coarse_edge_idx)
                    selection[insertion_along_axis] = coarse_edge_idx
                    insersions_data_collection.append(np.ones_like(data[tuple(selection)]))
                # go to next coarse edge
                elif fine_edge[1] == coarse_edge[1]:
                    fine_edge = next(fine_edges_iter)
                    coarse_edge_idx, coarse_edge = next(coarse_edges_iter)
                # probably not needed
                else:
                    break
            except StopIteration:
                break
        return np.insert(
            data,
            insertion_idx_collection,
            np.stack(insersions_data_collection, axis=insertion_along_axis),
            axis=insertion_along_axis,
        )
    else:
        return data


class Correction:
    def __init__(
        self,
        correction: dict,
        ylabel: str = "sf",
        unroll_axis: int = 0,
    ) -> None:
        self.ylabel = ylabel
        self.unroll_axis = unroll_axis
        self.raw_data = correction["data"]
        self.name = correction["name"]
        self.inputs = [it["name"] for it in correction["inputs"] if it["name"] != "type"]

        self.process_keys = ["emb"]
        self._fill_vector_wise = True
        if recursive_search(self.raw_data, "mc"):
            self._fill_vector_wise = False
            self.process_keys += ["mc"]

        self._histogram_edges: Union[None, Dict[str, np.ndarray]] = None
        self._histogram_edges_windowed: Union[None, Dict[str, np.ndarray]] = None

        self.data = self._fill()
        self.unroll_along(unroll_axis)

    def _fill(self) -> Dict[str, np.ndarray]:
        data = {k: np.zeros(tuple(it.shape[0] for it in self.histogram_edges_windowed.values())) for k in self.process_keys}

        if not self._fill_vector_wise:
            if len(self.inputs) == 2:
                for i, j in product(*map(range, list(data.values())[0].shape)):
                    for item in self.raw_data["content"][i]["content"][j]["content"]:
                        data[item["key"]][i, j] = item["value"]
            else:
                raise NotImplementedError
        else:
            if len(self.inputs) == 2:
                for i in range(list(data.values())[0].shape[0]):
                    data["emb"][i, :] = self.raw_data["content"][i]["content"]
            elif len(self.inputs) == 4:
                for i, j, k in product(*map(range, list(data.values())[0].shape[:-1])):
                    data["emb"][i, j, k, :] = self.raw_data["content"][i]["content"][j]["content"][k]["content"]
            else:
                raise NotImplementedError

        return data

    @property
    def histogram_edges(self) -> Dict[str, np.ndarray]:
        if self._histogram_edges is None:
            self._histogram_edges = {}
            _tmp = self.raw_data
            for item in self.inputs:
                self._histogram_edges[item] = np.array(_tmp["edges"])
                _tmp = _tmp["content"][0]
        return self._histogram_edges

    @property
    def histogram_edges_windowed(self) -> Dict[str, np.ndarray]:
        if self._histogram_edges_windowed is None:
            self._histogram_edges_windowed = {k: np.array(list(windowed(v, 2))) for k, v in self.histogram_edges.items()}
        return self._histogram_edges_windowed

    def unroll_along(self, axis: int = 0) -> None:
        self.edges = self.histogram_edges[self.inputs[axis]]
        self.xlabel = f"{to_latex(self.inputs[axis])} {'(GeV)' if 'eta' not in self.inputs[axis] else ''}"

        selection: List[Union[int, slice]] = [slice(None, None, None)] * len(self.inputs)
        walking_axis = [i for i in range(len(self.inputs)) if i != axis]

        self.unrolled_data = NestedDefaultDict()

        for idx1, walking_window1 in enumerate(self.histogram_edges_windowed[self.inputs[walking_axis[0]]]):
            selection[walking_axis[0]] = idx1
            if len(self.inputs) == 2:
                second_dim_key = ((self.inputs[walking_axis[0]], tuple(walking_window1)),)
                for process in self.process_keys:
                    self.unrolled_data[second_dim_key][process] = self.data[process][tuple(selection)].squeeze()
            elif len(self.inputs) == 4:
                for idx2, walking_window2 in enumerate(self.histogram_edges_windowed[self.inputs[walking_axis[1]]]):
                    selection[walking_axis[1]] = idx2
                    for idx3, walking_window3 in enumerate(self.histogram_edges_windowed[self.inputs[walking_axis[2]]]):
                        selection[walking_axis[2]] = idx3
                        third_dim_key = (
                            (self.inputs[walking_axis[0]], tuple(walking_window1)),
                            (self.inputs[walking_axis[1]], tuple(walking_window2)),
                            (self.inputs[walking_axis[2]], tuple(walking_window3)),
                        )
                        for process in self.process_keys:
                            self.unrolled_data[third_dim_key][process] = self.data[process][tuple(selection)].squeeze()
            else:
                raise NotImplementedError

        self.unrolled_keys = list(self.unrolled_data.keys())

    def is_equal_main_axis(self, other: Any) -> bool:
        if isinstance(other, Correction):
            return np.all(self.histogram_edges[self.inputs[self.unroll_axis]] == other.histogram_edges[self.inputs[self.unroll_axis]])
        else:
            raise TypeError

    def is_equal_binning(self, other: Any) -> bool:
        if isinstance(other, Correction):
            for (key1, item1), (_, item2) in zip(self.histogram_edges.items(), other.histogram_edges.items()):
                if self.inputs.index(key1) == self.unroll_axis and not np.all(item1 == item2):
                    print("Not equal binning for main axis, ratio plot is skipped")
                    continue
                if not np.all(item1 == item2):
                    return False
            return True
        else:
            raise TypeError

    def is_expandable_to(self, other: Any) -> bool:
        if isinstance(other, Correction):
            assert self.inputs == other.inputs
            for key in self.inputs:
                if self.inputs.index(key) == self.unroll_axis and not is_expandable(self.histogram_edges[key], other.histogram_edges[key]):
                    print("Not expandable binning for main axis, ratio plot is skipped")
                    continue
                if not is_expandable(self.histogram_edges[key], other.histogram_edges[key]):
                    return False
            return True
        else:
            raise TypeError

    def expand_binning_to(self, other: Any) -> None:
        if isinstance(other, Correction):
            assert self.inputs == other.inputs
            for axis, key in enumerate(self.inputs):
                if is_expandable(self.histogram_edges[key], other.histogram_edges[key]):
                    expanding_object = other if len(self.histogram_edges[key]) > len(other.histogram_edges[key]) else self
                    fine_binning = self.histogram_edges[key] if len(self.histogram_edges[key]) > len(other.histogram_edges[key]) else other.histogram_edges[key]

                    for process in expanding_object.process_keys:
                        expanding_object.data[process] = expand(expanding_object.data[process], self.histogram_edges[key], other.histogram_edges[key], axis)

                    expanding_object.histogram_edges[key] = fine_binning
                else:
                    print(f"{key} binning is not expandable")
            self.unroll_along(self.unroll_axis)
            other.unroll_along(other.unroll_axis)
        else:
            raise TypeError


def plot_corrections(
    json_a: dict,
    json_b: dict,
    tag_a: str,
    tag_b: str,
    directory: str,
    name: str = "all",
) -> None:
    correction_count = count()
    for raw_corrections in combinations([*json_a["corrections"], *json_b["corrections"]], 2):
        if raw_corrections[0]["name"] != raw_corrections[1]["name"]:
            continue
        else:
            nth_correction = next(correction_count)

        if name and raw_corrections[0]["name"] != name:
            continue

        corrections: List[Correction] = [Correction(item) for item in raw_corrections]
        if not corrections[0].is_equal_binning(corrections[1]):
            print(f"{corrections[0].name}: different binning between {tag_a} and {tag_b}, trying to expand")
            if corrections[0].is_expandable_to(corrections[1]):
                print(f"{corrections[0].name}: expanding successful")
                corrections[0].expand_binning_to(corrections[1])  # or vice versa
            else:
                print(f"{corrections[0].name}: not expandable, skipping")
                continue
        corrections_name = corrections[0].name
        corrections_unrolled_keys = corrections[0].unrolled_keys
        corrections_process_keys = corrections[0].process_keys

        for nth_window, correction_window in enumerate(corrections_unrolled_keys):
            fig, axes = plt.subplots(
                2,
                len(corrections[0].process_keys),
                gridspec_kw=dict(height_ratios=[0.7, 0.3]),
                figsize=(10 * len(corrections[0].process_keys), 12),
                sharex=True,
            )

            plt.subplots_adjust(hspace=0.1)

            fig.suptitle(corrections_name)

            for process, ax in zip(
                corrections[0].process_keys,
                [axes[:, 0], axes[:, 1]] if len(corrections_process_keys) > 1 else [axes],
            ):
                ax[0].set_title(
                    f"{process}: {correction_key_to_latex(correction_window)}",
                    loc="left",
                    fontsize=16,
                )
                for correction_obj, tag_name in zip(corrections, [tag_a, tag_b]):
                    hep.histplot(
                        correction_obj.unrolled_data[correction_window][process],
                        correction_obj.edges,
                        label=tag_name,
                        ax=ax[0],
                        histtype="errorbar",
                        yerr=False,
                        xerr=True,
                        markerfacecolor="none",
                    )

                _a_array = np.array(corrections[0].unrolled_data[correction_window][process])
                _b_array = np.array(corrections[1].unrolled_data[correction_window][process])

                if corrections[0].is_equal_main_axis(corrections[1]):
                    hep.histplot(
                        _a_array / _b_array,
                        correction_obj.edges,
                        label=f"${corrections[0].ylabel}_{{{tag_a}}}$ / ${corrections[1].ylabel}_{{{tag_b}}}$",
                        ax=ax[1],
                        histtype="errorbar",
                        yerr=False,
                        xerr=True,
                        markerfacecolor="none",
                    )
                else:
                    print(f"Skipping {corrections_name} ratio due to different binning between {tag_a} and {tag_b}")

                [_ax.legend() for _ax in ax]

                _max_y_value = max([max(correction_obj.unrolled_data[correction_window][process]) for correction_obj in corrections])

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

                hep.cms.label("Own Work", ax=ax[0], loc=2, data=process == "emb")

            if not os.path.exists(directory):
                os.makedirs(name="comparison_plots", exist_ok=True)

            os.makedirs(name=os.path.join(directory, corrections_name), exist_ok=True)
            for ext in ["pdf", "png"]:
                plt.savefig(
                    os.path.join(
                        directory,
                        corrections_name,
                        f"comparison_{corrections_name}_{tag_a}_{tag_b}_{correction_key_to_path(correction_window)}.{ext}",
                    ),
                )
            plt.close("all")

            print(
                " | ".join(
                    [
                        f"Correction {nth_correction + 1}/{len(json_a['corrections'])}: {corrections_name}",
                        f"Window {nth_window + 1}/{len(corrections_unrolled_keys)}: {correction_key_to_prompt(correction_window)}",
                    ]
                )
            )


if __name__ == "__main__":
    with gzip.open(args.input_a, "rb") as f:
        json_a, name_json_a = json.load(f), args.tag_a
    with gzip.open(args.input_b, "rb") as f:
        json_b, name_json_b = json.load(f), args.tag_b
    plot_corrections(json_a, json_b, tag_a=name_json_a, tag_b=name_json_b, directory=args.output, name=args.correction_name)

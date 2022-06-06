from __future__ import annotations  # needed for type annotations in > python 3.7

from typing import List
from code_generation.modifiers import EraModifier, SampleModifier
from code_generation.rules import AppendProducer, RemoveProducer
from .producers import embedding as embedding
from .producers import scalefactors as scalefactors
from code_generation.configuration import Configuration


def setup_embedding(configuration: Configuration, scopes: List[str]):

    configuration.add_modification_rule(
        scopes,
        AppendProducer(
            producers=embedding.EmbeddingQuantities, samples=["embedding", "emb_mc"]
        ),
    )

    # add embedding selection scalefactors
    configuration.add_config_parameters(
        scopes,
        {
            "embedding_selection_sf_file": "data/embedding/muon_2018UL.json.gz",
            "embedding_selection_trigger_sf": "m_sel_trg_kit_ratio",
            "embedding_selection_id_sf": "EmbID_pt_eta_bins",
        },
    )
    configuration.add_modification_rule(
        scopes,
        AppendProducer(
            producers=embedding.TauEmbeddingSelectionSF, samples=["embedding"]
        ),
    )
    # add muon scalefactors
    configuration.add_config_parameters(
        ["mt", "mm", "em"],
        {
            "embedding_muon_sf_file": "data/embedding/muon_2018UL.json.gz",
            "embedding_muon_id_sf": "ID_pt_eta_bins",
            "embedding_muon_iso_sf": "Iso_pt_eta_bins",
        },
    )
    configuration.add_modification_rule(
        ["mt", "mm", "em"],
        RemoveProducer(
            producers=[
                scalefactors.MuonIDIso_SF,
            ],
            samples=["embedding"],
        ),
    )
    configuration.add_modification_rule(
        ["mt", "mm"],
        AppendProducer(
            producers=[
                embedding.TauEmbeddingMuonIDSF_1,
                embedding.TauEmbeddingMuonIsoSF_1,
            ],
            samples=["embedding"],
        ),
    )
    configuration.add_modification_rule(
        ["em", "mm"],
        AppendProducer(
            producers=[
                embedding.TauEmbeddingMuonIDSF_2,
                embedding.TauEmbeddingMuonIsoSF_2,
            ],
            samples=["embedding"],
        ),
    )

    return configuration

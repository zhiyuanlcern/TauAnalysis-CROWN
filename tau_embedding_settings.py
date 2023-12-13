from __future__ import annotations  # needed for type annotations in > python 3.7

from typing import List
from code_generation.rules import AppendProducer, RemoveProducer, ReplaceProducer
from .producers import embedding as embedding
from .producers import scalefactors as scalefactors
from .producers import pairquantities as pairquantities
from .producers import genparticles as genparticles
from .producers import taus as taus
from .producers import jets as jets
from .producers import triggers as triggers
from .producers import electrons as electrons
from code_generation.configuration import Configuration
from code_generation.systematics import SystematicShift
from code_generation.modifiers import EraModifier

measure_tauES = False
measure_elefakeES = False


def setup_embedding(configuration: Configuration, scopes: List[str]):

    configuration.add_config_parameters(
        "global",
        {
            "met_filters": EraModifier(
                {
                    "2016preVFP": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        "Flag_eeBadScFilter",
                    ],
                    "2016postVFP": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        "Flag_eeBadScFilter",
                    ],
                    "2017": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        "Flag_eeBadScFilter",
                        "Flag_ecalBadCalibFilter",
                    ],
                    "2018": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        "Flag_eeBadScFilter",
                        "Flag_ecalBadCalibFilter",
                    ],
                }
            ),
        },
    )
    configuration.add_modification_rule(
        scopes,
        AppendProducer(
            producers=embedding.EmbeddingQuantities,
            samples=["embedding", "embedding_mc"],
        ),
    )

    # modify the gen particle producer
    configuration.add_modification_rule(
        ["mt"],
        ReplaceProducer(
            producers=[genparticles.MTGenPair, genparticles.EmbeddingGenPair],
            samples=["embedding", "embedding_mc"],
            scopes=["mt"],
        ),
    )
    configuration.add_modification_rule(
        ["et"],
        ReplaceProducer(
            producers=[genparticles.ETGenPair, genparticles.EmbeddingGenPair],
            samples=["embedding", "embedding_mc"],
            scopes=["et"],
        ),
    )
    configuration.add_modification_rule(
        ["tt"],
        ReplaceProducer(
            producers=[genparticles.TTGenPair, genparticles.EmbeddingGenPair],
            samples=["embedding", "embedding_mc"],
            scopes=["tt"],
        ),
    )
    configuration.add_modification_rule(
        ["em"],
        ReplaceProducer(
            producers=[genparticles.EMGenPair, genparticles.EmbeddingGenPair],
            samples=["embedding", "embedding_mc"],
            scopes=["em"],
        ),
    )
    configuration.add_modification_rule(
        ["mm"],
        ReplaceProducer(
            producers=[genparticles.MuMuGenPair, genparticles.EmbeddingGenPair],
            samples=["embedding", "embedding_mc"],
            scopes=["mm"],
        ),
    )
    configuration.add_modification_rule(
        ["ee"],
        ReplaceProducer(
            producers=[genparticles.ElElGenPair, genparticles.EmbeddingGenPair],
            samples=["embedding", "embedding_mc"],
            scopes=["ee"],
        ),
    )

    configuration.add_config_parameters(
        ["mt", "et", "tt", "em"],
        {
            "truegen_mother_pdgid": 23,
            "truegen_daughter_1_pdgid": 15,
            "truegen_daugher_2_pdgid": 15,
        },
    )
    configuration.add_config_parameters(
        ["mm"],
        {
            "truegen_mother_pdgid": 23,
            "truegen_daughter_1_pdgid": 13,
            "truegen_daugher_2_pdgid": 13,
        },
    )
    configuration.add_config_parameters(
        ["ee"],
        {
            "truegen_mother_pdgid": 23,
            "truegen_daughter_1_pdgid": 11,
            "truegen_daugher_2_pdgid": 11,
        },
    )

    # add embedding selection scalefactors
    configuration.add_config_parameters(
        scopes,
        {
            "embedding_selection_sf_file": EraModifier(
                {
                    "2016preVFP": "data/embedding/embeddingselection_2016preVFPUL.json.gz",
                    "2016postVFP": "data/embedding/embeddingselection_2016postVFPUL.json.gz",
                    "2017": "data/embedding/muon_2017UL.json.gz",
                    "2018": "data/embedding/muon_2018UL.json.gz",
                }
            ),
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
    # add muon scalefactors from embedding measurements
    configuration.add_config_parameters(
        ["mt", "mm", "em"],
        {
            "embedding_muon_sf_file": EraModifier(
                {
                    "2016preVFP": "data/embedding/muon_2016preVFPUL.json.gz", ##Jordan: this is tmp fix, I copied data/embedding/muon_2018_UL.json.gz to data/embedding/tau_trigger2016preVFP_UL.json.gz
                    "2016postVFP": "data/embedding/muon_2016postVFPUL.json.gz", ##Jordan: this is tmp fix, I copied data/embedding/muon_2018_UL.json.gz to data/embedding/tau_trigger2016preVFP_UL.json.gz
                    "2017": "data/embedding/muon_2017UL.json.gz",
                    "2018": "data/embedding/muon_2018UL.json.gz",
                }
            ),
            "embedding_muon_id_sf": "ID_pt_eta_bins",
            "embedding_muon_iso_sf": "Iso_pt_eta_bins",
        },
    )
    # add electron scalefactors from embedding measurements
    configuration.add_config_parameters(
        ["et", "ee", "em"],
        {
            "embedding_electron_sf_file": EraModifier(
                {
                    "2016preVFP": "data/embedding/electron_2016preVFPUL.json.gz",
                    "2016postVFP": "data/embedding/electron_2016postVFPUL.json.gz",
                    "2017": "data/embedding/electron_2017UL.json.gz",
                    "2018": "data/embedding/electron_2018UL.json.gz",
                }
            ),
            "embedding_electron_id_sf": "ID90_pt_eta_bins",
            "embedding_electron_iso_sf": "Iso_pt_eta_bins",
        },
    )
    # muon trigger SF settings from embedding measurements
    configuration.add_config_parameters(
        ["mt", "mm"],
        {
             "singlemuon_trigger_sf": EraModifier(
                {
                    "2018": [
                        {
                            "flagname": "trg_wgt_single_mu24",
                            "embedding_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                            "muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_mu27",
                            "embedding_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                            "muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_mu24ormu27",
                            "embedding_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                            "muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2017": [
                        {
                            "flagname": "trg_wgt_single_mu24",
                            "embedding_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                            "muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_mu27",
                            "embedding_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                            "muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_mu24ormu27",
                            "embedding_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                            "muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_wgt_single_mu22",
                            "embedding_trigger_sf": "Trg_pt_eta_bins",
                            "muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_wgt_single_mu22",
                            "embedding_trigger_sf": "Trg_pt_eta_bins",
                            "muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                }
            )
        },
    )
    # electron trigger SF settings from embedding measurements
    configuration.add_config_parameters(
        ["et", "ee"],
        {
            "singlelectron_trigger_sf": EraModifier(
                {
                    "2018": [
                        {
                            "flagname": "trg_wgt_single_ele32",
                            "embedding_trigger_sf": "Trg32_Iso_pt_eta_bins",
                            "electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_ele35",
                            "embedding_trigger_sf": "Trg35_Iso_pt_eta_bins",
                            "electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_ele32orele35",
                            "embedding_trigger_sf": "Trg32_or_Trg35_Iso_pt_eta_bins",
                            "electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_ele27orele32orele35",
                            "embedding_trigger_sf": "Trg_Iso_pt_eta_bins",
                            "electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2017": [
                        {
                            "flagname": "trg_wgt_single_ele32",
                            "embedding_trigger_sf": "Trg32_Iso_pt_eta_bins",
                            "electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_ele35",
                            "embedding_trigger_sf": "Trg35_Iso_pt_eta_bins",
                            "electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_ele32orele35",
                            "embedding_trigger_sf": "Trg32_or_Trg35_Iso_pt_eta_bins",
                            "electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_ele27orele32orele35",
                            "embedding_trigger_sf": "Trg_Iso_pt_eta_bins",
                            "electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_wgt_single_ele25",
                            "embedding_trigger_sf": "Trg25_Iso_pt_eta_bins",
                            "electron_trg_extrapolation": 1.0,  # for nominal case
                        }
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_wgt_single_ele25",
                            "embedding_trigger_sf": "Trg25_Iso_pt_eta_bins",
                            "electron_trg_extrapolation": 1.0,  # for nominal case
                        }
                    ],
                }
            )
        },
    )
    # ditau trigger SF settings for embedding
    configuration.add_config_parameters(
        ["tt"],
        {
            "emb_ditau_trigger_wp": "Medium",
            "emb_ditau_trigger_type": "ditau",
            "emb_ditau_trigger_corrtype": "sf",
            "emb_ditau_trigger_syst": "nom",
            "emb_ditau_trigger_file": EraModifier(
                {
                    "2016preVFP": "data/embedding/tau_trigger2016preVFP_UL.json.gz",  ##Jordan: this is tmp fix, I copied data/embedding/tau_trigger2018_UL.json.gz to data/embedding/tau_trigger2016preVFP_UL.json.gz
                    "2016postVFP": "data/embedding/tau_trigger2016postVFP_UL.json.gz",  ##Jordan: this is tmp fix, I copied data/embedding/tau_trigger2018_UL.json.gz to data/embedding/tau_trigger2016postVFP_UL.json.gz
                    "2017": "data/embedding/tau_trigger2017_UL.json.gz", ##Jordan: this is tmp fix, I copied data/embedding/tau_trigger2018_UL.json.gz to data/embedding/tau_trigger2017_UL.json.gz
                    "2018": "data/embedding/tau_trigger2018_UL.json.gz",
                }
            ),
        },
    )
    configuration.add_modification_rule(
        ["mt"],
        AppendProducer(
            producers=[
                embedding.TauEmbeddingMuonIDSF_1,
                embedding.TauEmbeddingMuonIsoSF_1,
                embedding.MTGenerateSingleMuonTriggerSF,
            ],
            samples=["embedding"],
        ),
    )
    configuration.add_modification_rule(
        ["et"],
        AppendProducer(
            producers=[
                embedding.TauEmbeddingElectronIDSF_1,
                embedding.TauEmbeddingElectronIsoSF_1,
                embedding.ETGenerateSingleElectronTriggerSF,
            ],
            samples=["embedding"],
        ),
    )
    configuration.add_modification_rule(
        ["tt"],
        AppendProducer(
            producers=[
                embedding.TTGenerateDoubleTauTriggerSF_1,
                embedding.TTGenerateDoubleTauTriggerSF_2,
            ],
            samples=["embedding"],
        ),
    )
    configuration.add_modification_rule(
        ["em"],
        AppendProducer(
            producers=[
                embedding.TauEmbeddingElectronIDSF_1,
                embedding.TauEmbeddingElectronIsoSF_1,
                embedding.TauEmbeddingMuonIDSF_2,
                embedding.TauEmbeddingMuonIsoSF_2,
            ],
            samples=["embedding"],
        ),
    )
    configuration.add_modification_rule(
        ["mm"],
        AppendProducer(
            producers=[
                embedding.TauEmbeddingMuonIDSF_1,
                embedding.TauEmbeddingMuonIsoSF_1,
                embedding.TauEmbeddingMuonIDSF_2,
                embedding.TauEmbeddingMuonIsoSF_2,
                embedding.MTGenerateSingleMuonTriggerSF,
            ],
            samples=["embedding"],
        ),
    )
    configuration.add_modification_rule(
        ["ee"],
        AppendProducer(
            producers=[
                embedding.TauEmbeddingElectronIDSF_1,
                embedding.TauEmbeddingElectronIsoSF_1,
                embedding.TauEmbeddingElectronIDSF_2,
                embedding.TauEmbeddingElectronIsoSF_2,
                embedding.ETGenerateSingleElectronTriggerSF,
            ],
            samples=["embedding"],
        ),
    )
    # remove some gen producers
    configuration.add_modification_rule(
        ["et", "mt", "tt"],
        RemoveProducer(
            producers=[pairquantities.taujet_pt_2, genparticles.gen_taujet_pt_2],
            samples=["embedding", "embedding_mc"],
        ),
    )
    configuration.add_modification_rule(
        ["tt"],
        RemoveProducer(
            producers=[pairquantities.taujet_pt_1, genparticles.gen_taujet_pt_1],
            samples=["embedding", "embedding_mc"],
        ),
    )
    configuration.add_modification_rule(
        "global",
        RemoveProducer(
            producers=jets.JetEnergyCorrection, samples=["embedding", "embdding_mc"]
        ),
    )

    # For the tau related triggers, in embedding, we cannot use a trigger path directly, since they are not
    # correctly represented in embedded samples. Instead, it is possible to match to an earlier filter
    # within the trigger sequence. In order to do this, we have to use another producer
    # and not the regular trigger producer. Also we have to match to special filter bits:
    # tt -> bit 20
    # mt -> bit 21
    configuration.add_config_parameters(
        ["tt"],
        {
            # here we do not match to the hlt path, only the filter
            "doubletau_trigger_embedding": EraModifier(
                {
                    "2018": [
                        {
                            "flagname": "trg_double_tau35_mediumiso_hps",
                            "p1_ptcut": 35,
                            "p2_ptcut": 35,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 20,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 20,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_double_tau40_tightiso",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 20,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 20,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_double_tau40_mediumiso_tightid",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 20,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 20,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_double_tau35_tightiso_tightid",
                            "p1_ptcut": 35,
                            "p2_ptcut": 35,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 20,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 20,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2017": [
                        {
                            "flagname": "trg_double_tau40_tightiso",
                            "hlt_path": "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 6,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 6,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_double_tau40_mediumiso_tightid",
                            "hlt_path": "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 6,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 6,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_double_tau35_tightiso_tightid",
                            "hlt_path": "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 6,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 6,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_double_tau35_mediumiso",
                            "hlt_path": "HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 6,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 6,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_double_tau35_mediumcombiso",
                            "hlt_path": "HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 6,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 6,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_double_tau35_mediumiso",
                            "hlt_path": "HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 6,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 6,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_double_tau35_mediumcombiso",
                            "hlt_path": "HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 6,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 6,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                }
            ),
        },
    )

    configuration.add_config_parameters(
        ["mt"],
        {
            "mutau_cross_trigger_embedding": EraModifier(
                {
                    "2018": [
                        {
                            "flagname": "trg_cross_mu20tau27_hps",
                            "p1_ptcut": 21,
                            "p1_etacut": 2.5,
                            "p1_filterbit": 3,
                            "p1_trigger_particle_id": 13,
                            "p2_ptcut": 32,
                            "p2_etacut": 2.1,
                            "p2_filterbit": 20,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        }
                    ],
                    "2017": [
                        {
                            "flagname": "trg_cross_mu20tau27",
                            "hlt_path": "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
                            "p1_ptcut": 21,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 3,
                            "p1_trigger_particle_id": 13,
                            "p2_ptcut": 32,
                            "p2_etacut": 2.1,
                            "p2_filterbit": 4,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        }
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_cross_mu19tau20",
                            "hlt_path": "HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1",
                            "p1_ptcut": 20,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 3,
                            "p1_trigger_particle_id": 13,
                            "p2_ptcut": 25,
                            "p2_etacut": 2.1,
                            "p2_filterbit": 4,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        }
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_cross_mu19tau20",
                            "hlt_path": "HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1",
                            "p1_ptcut": 20,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 3,
                            "p1_trigger_particle_id": 13,
                            "p2_ptcut": 25,
                            "p2_etacut": 2.1,
                            "p2_filterbit": 4,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        }
                    ],
                }
            ),
        },
    )

    # use other trigger flags for embedding samples
    configuration.add_modification_rule(
        "tt",
        ReplaceProducer(
            producers=[
                triggers.TTGenerateDoubleTriggerFlags,
                triggers.TTGenerateDoubleTriggerFlagsEmbedding,
            ],
            samples="embedding",
        ),
    )
    configuration.add_outputs(
        "tt", triggers.TTGenerateDoubleTriggerFlagsEmbedding.output_group
    )

    # use other trigger flags for embedding samples
    configuration.add_modification_rule(
        "mt",
        ReplaceProducer(
            producers=[
                triggers.MTGenerateCrossTriggerFlags,
                triggers.MTGenerateCrossTriggerFlagsEmbedding,
            ],
            samples="embedding",
        ),
    )
    configuration.add_outputs(
        "mt", triggers.MTGenerateCrossTriggerFlagsEmbedding.output_group
    )

    ######################
    ## Tau ID SFs
    ######################

    configuration.add_modification_rule(
        ["et", "mt"],
        ReplaceProducer(
            producers=[
                scalefactors.Tau_2_VsJetTauID_lt_SF,
                embedding.Tau_2_VsJetTauID_lt_SF,
            ],
            samples="embedding",
        ),
    )
    configuration.add_modification_rule(
        "tt",
        ReplaceProducer(
            producers=[
                scalefactors.Tau_1_VsJetTauID_SF,
                embedding.Tau_1_VsJetTauID_tt_SF,
            ],
            samples="embedding",
        ),
    )
    configuration.add_modification_rule(
        "tt",
        ReplaceProducer(
            producers=[
                scalefactors.Tau_2_VsJetTauID_tt_SF,
                embedding.Tau_2_VsJetTauID_tt_SF,
            ],
            samples="embedding",
        ),
    )
    configuration.add_outputs(
        ["et", "mt"],
        embedding.Tau_2_VsJetTauID_lt_SF.output_group,
    )
    configuration.add_outputs(
        "tt",
        [
            embedding.Tau_1_VsJetTauID_tt_SF.output_group,
            embedding.Tau_2_VsJetTauID_tt_SF.output_group,
        ],
    )

    # replace TauID producers for embedding samples
    configuration.add_config_parameters(
        ["mt", "et"],
        {
            "tau_emb_sf_file": EraModifier(
                {
                    "2016preVFP": "data/embedding/tau_2016preVFPUL.json.gz",
                    "2016postVFP": "data/embedding/tau_2016postVFPUL.json.gz",
                    "2017": "data/embedding/tau_2017UL.json.gz",
                    "2018": "data/embedding/tau_2018UL.json.gz",
                }
            ),
            "tau_emb_sf_vsjet_tau20to25": "nom",
            "tau_emb_sf_vsjet_tau25to30": "nom",
            "tau_emb_sf_vsjet_tau30to35": "nom",
            "tau_emb_sf_vsjet_tau35to40": "nom",
            "tau_emb_sf_vsjet_tau40toInf": "nom",
            "tau_emb_id_sf_correctionset": "TauID_sf_embedding_ptbinned",
            "vsjet_tau_id_sf_embedding": [
                {
                    "tau_1_vsjet_sf_outputname": "id_wgt_tau_vsJet_{wp}_1".format(
                        wp=wp
                    ),
                    "tau_2_vsjet_sf_outputname": "id_wgt_tau_vsJet_{wp}_2".format(
                        wp=wp
                    ),
                    "vsjet_tau_id_WP": "{wp}".format(wp=wp),
                }
                for wp in [
                    # "VVVLoose",
                    # "VVLoose",
                    # "VLoose",
                    # "Loose",
                    # "Medium",
                    "Tight",
                    # "VTight",
                    # "VVTight",
                ]
            ],
        },
    )
    # replace TauID producers for embedding samples
    configuration.add_config_parameters(
        ["tt"],
        {
            "tau_emb_sf_file": EraModifier(
                {
                    "2016preVFP": "data/embedding/tau_2016preVFPUL.json.gz",
                    "2016postVFP": "data/embedding/tau_2016postVFPUL.json.gz",
                    "2017": "data/embedding/tau_2017UL.json.gz",
                    "2018": "data/embedding/tau_2018UL.json.gz",
                }
            ),
            "tau_emb_sf_vsjet_tauDM0": "nom",
            "tau_emb_sf_vsjet_tauDM1": "nom",
            "tau_emb_sf_vsjet_tauDM10": "nom",
            "tau_emb_sf_vsjet_tauDM11": "nom",
            "tau_emb_id_sf_correctionset": "TauID_sf_embedding_dmbinned",
            "vsjet_tau_id_sf_embedding": [
                {
                    "tau_1_vsjet_sf_outputname": "id_wgt_tau_vsJet_{wp}_1".format(
                        wp=wp
                    ),
                    "tau_2_vsjet_sf_outputname": "id_wgt_tau_vsJet_{wp}_2".format(
                        wp=wp
                    ),
                    "vsjet_tau_id_WP": "{wp}".format(wp=wp),
                }
                for wp in [
                    # "VVVLoose",
                    # "VVLoose",
                    # "VLoose",
                    # "Loose",
                    # "Medium",
                    "Tight",
                    # "VTight",
                    # "VVTight",
                ]
            ],
        },
    )
    # and add the variations for it
    for variation in ["Up", "Down"]:
        configuration.add_shift(
            SystematicShift(
                name=f"vsJetTau20to25{variation}",
                shift_config={
                    ("et", "mt"): {"tau_emb_sf_vsjet_tau20to25": variation.lower()}
                },
                producers={("et", "mt"): embedding.Tau_2_VsJetTauID_lt_SF},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name=f"vsJetTau25to30{variation}",
                shift_config={
                    ("et", "mt"): {"tau_emb_sf_vsjet_tau25to30": variation.lower()}
                },
                producers={("et", "mt"): embedding.Tau_2_VsJetTauID_lt_SF},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name=f"vsJetTau30to35{variation}",
                shift_config={
                    ("et", "mt"): {"tau_emb_sf_vsjet_tau30to35": variation.lower()}
                },
                producers={("et", "mt"): embedding.Tau_2_VsJetTauID_lt_SF},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name=f"vsJetTau35to40{variation}",
                shift_config={
                    ("et", "mt"): {"tau_emb_sf_vsjet_tau35to40": variation.lower()}
                },
                producers={("et", "mt"): embedding.Tau_2_VsJetTauID_lt_SF},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name=f"vsJetTau40toInf{variation}",
                shift_config={
                    ("et", "mt"): {"tau_emb_sf_vsjet_tau40toInf": variation.lower()}
                },
                producers={("et", "mt"): embedding.Tau_2_VsJetTauID_lt_SF},
            )
        )
        # dm binned variations
        for dm in [0, 1, 10, 11]:
            configuration.add_shift(
                SystematicShift(
                    name=f"vsJetTauDM{dm}{variation}",
                    shift_config={
                        ("tt"): {f"tau_emb_sf_vsjet_tauDM{dm}": variation.lower()}
                    },
                    producers={
                        ("tt"): [
                            embedding.Tau_1_VsJetTauID_tt_SF,
                            embedding.Tau_2_VsJetTauID_tt_SF,
                        ]
                    },
                )
            )

    #########################
    # Trigger shifts
    #########################
    configuration.add_shift(
        SystematicShift(
            name="singleElectronTriggerSFUp",
            shift_config={
                ("et"): {
                    "singlelectron_trigger_sf": [
                        {
                            "flagname": "trg_wgt_single_ele32orele35",
                            "embedding_trigger_sf": "Trg32_or_Trg35_Iso_pt_eta_bins",
                            "electron_trg_extrapolation": 1.02,
                        },
                        {
                            "flagname": "trg_wgt_single_ele32",
                            "embedding_trigger_sf": "Trg32_Iso_pt_eta_bins",
                            "electron_trg_extrapolation": 1.02,
                        },
                        {
                            "flagname": "trg_wgt_single_ele35",
                            "embedding_trigger_sf": "Trg35_Iso_pt_eta_bins",
                            "electron_trg_extrapolation": 1.02,
                        },
                        {
                            "flagname": "trg_wgt_single_ele27orele32orele35",
                            "embedding_trigger_sf": "Trg_Iso_pt_eta_bins",
                            "electron_trg_extrapolation": 1.02,
                        },
                    ]
                }
            },
            producers={("et"): embedding.ETGenerateSingleElectronTriggerSF},
        ),
        samples=["embedding", "embedding_mc"],
    )
    configuration.add_shift(
        SystematicShift(
            name="singleElectronTriggerSFDown",
            shift_config={
                ("et"): {
                    "singlelectron_trigger_sf": [
                        {
                            "flagname": "trg_wgt_single_ele32orele35",
                            "embedding_trigger_sf": "Trg32_or_Trg35_Iso_pt_eta_bins",
                            "electron_trg_extrapolation": 0.98,
                        },
                        {
                            "flagname": "trg_wgt_single_ele32",
                            "embedding_trigger_sf": "Trg32_Iso_pt_eta_bins",
                            "electron_trg_extrapolation": 0.98,
                        },
                        {
                            "flagname": "trg_wgt_single_ele35",
                            "embedding_trigger_sf": "Trg35_Iso_pt_eta_bins",
                            "electron_trg_extrapolation": 0.98,
                        },
                        {
                            "flagname": "trg_wgt_single_ele27orele32orele35",
                            "embedding_trigger_sf": "Trg_Iso_pt_eta_bins",
                            "electron_trg_extrapolation": 0.98,
                        },
                    ]
                }
            },
            producers={("et"): embedding.ETGenerateSingleElectronTriggerSF},
        ),
        samples=["embedding", "embedding_mc"],
    )

    configuration.add_shift(
        SystematicShift(
            name="singleMuonTriggerSFUp",
            shift_config={
                ("mt", "mm"): {
        "singlemuon_trigger_sf": EraModifier(
                {
                    "2018": [
                        {
                            "flagname": "trg_wgt_single_mu24",
                            "embedding_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                            "muon_trg_extrapolation": 1.02, 
                        },
                        {
                            "flagname": "trg_wgt_single_mu27",
                            "embedding_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                            "muon_trg_extrapolation": 1.02, 
                        },
                        {
                            "flagname": "trg_wgt_single_mu24ormu27",
                            "embedding_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                            "muon_trg_extrapolation": 1.02,  
                        },
                    ],
                    "2017": [
                        {
                            "flagname": "trg_wgt_single_mu24",
                            "embedding_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                            "muon_trg_extrapolation": 1.02,  
                        },
                        {
                            "flagname": "trg_wgt_single_mu27",
                            "embedding_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                            "muon_trg_extrapolation": 1.02, 
                        },
                        {
                            "flagname": "trg_wgt_single_mu24ormu27",
                            "embedding_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                            "muon_trg_extrapolation": 1.02, 
                        },
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_wgt_single_mu22",
                            "embedding_trigger_sf": "Trg_pt_eta_bins",
                            "muon_trg_extrapolation": 1.02,  
                        },
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_wgt_single_mu22",
                            "embedding_trigger_sf": "Trg_pt_eta_bins",
                            "muon_trg_extrapolation": 1.02,  # for nominal case
                        },
                    ],
                }
            )
                }
            },
            producers={
                ("mt"): embedding.MTGenerateSingleMuonTriggerSF,
                ("mm"): embedding.MTGenerateSingleMuonTriggerSF,
            },
        ),
        samples=["embedding", "embedding_mc"],
    )
    configuration.add_shift(
        SystematicShift(
            name="singleMuonTriggerSFDown",
            shift_config={
                ("mt", "mm"): {

              "singlemuon_trigger_sf": EraModifier(
                {
                    "2018": [
                        {
                            "flagname": "trg_wgt_single_mu24",
                            "embedding_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                            "muon_trg_extrapolation": 0.98, 
                        },
                        {
                            "flagname": "trg_wgt_single_mu27",
                            "embedding_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                            "muon_trg_extrapolation": 0.98,  
                        },
                        {
                            "flagname": "trg_wgt_single_mu24ormu27",
                            "embedding_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                            "muon_trg_extrapolation": 0.98,  
                        },
                    ],
                    "2017": [
                        {
                            "flagname": "trg_wgt_single_mu24",
                            "embedding_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                            "muon_trg_extrapolation": 0.98,  
                        },
                        {
                            "flagname": "trg_wgt_single_mu27",
                            "embedding_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                            "muon_trg_extrapolation": 0.98, 
                        },
                        {
                            "flagname": "trg_wgt_single_mu24ormu27",
                            "embedding_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                            "muon_trg_extrapolation": 0.98,  
                        },
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_wgt_single_mu22",
                            "embedding_trigger_sf": "Trg_pt_eta_bins",
                            "muon_trg_extrapolation": 0.98,  
                        },
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_wgt_single_mu22",
                            "embedding_trigger_sf": "Trg_pt_eta_bins",
                            "muon_trg_extrapolation": 0.98,  
                        },
                    ],
                }
            )                  
                }
            },
            producers={
                ("mt"): embedding.MTGenerateSingleMuonTriggerSF,
                ("mm"): embedding.MTGenerateSingleMuonTriggerSF,
            },
        ),
        samples=["embedding", "embedding_mc"],
    )
    if measure_tauES:
        ###################
        # Tau ES variations for measurement
        # first set the initial variation to nominal

        configuration.add_config_parameters(
            "mt",
            {
                "tau_ES_shift_DM0": 1.0,
                "tau_ES_shift_DM1": 1.0,
                "tau_ES_shift_DM10": 1.0,
                "tau_ES_shift_DM11": 1.0,
            },
        )
        configuration.add_modification_rule(
            "mt",
            ReplaceProducer(
                producers=[
                    taus.TauEnergyCorrection,
                    taus.TauEnergyCorrection_Embedding,
                ],
                samples=["embedding"],
            ),
        )
        tauESvariations = [-2.5 + 0.1 * i for i in range(0, 51)]
        for tauESvariation in tauESvariations:
            name = str(round(tauESvariation, 2)).replace("-", "minus").replace(".", "p")
            configuration.add_shift(
                SystematicShift(
                    name=f"EMBtauESshift_{name}",
                    shift_config={
                        ("mt"): {
                            "tau_ES_shift_DM0": 1.0
                            + (round(tauESvariation / 100.0, 5)),
                            "tau_ES_shift_DM1": 1.0
                            + (round(tauESvariation / 100.0, 5)),
                            "tau_ES_shift_DM10": 1.0
                            + (round(tauESvariation / 100.0, 5)),
                            "tau_ES_shift_DM11": 1.0
                            + (round(tauESvariation / 100.0, 5)),
                        }
                    },
                    producers={("mt"): taus.TauPtCorrection_byValue},
                ),
                samples=["embedding"],
            )
    else:
        tauES_2016preVFP = {  # ToDo: Measure these values for 2016preVFP and add them to the configuration
            "up": 1.0 - 0.0,
            "nominal": 1.0,
            "down": 1.0 + 0.0,
        }
        tauES_2016postVFP = {  # ToDo: Measure these values for 2016postVFP and add them to the configuration
            "up": 1.0 - 0.0,
            "nominal": 1.0,
            "down": 1.0 + 0.0,
        }
        tauES_2017 = {  # ToDo: Measure these values for 2017 and add them to the configuration
            "up": 1.0 - 0.0,
            "nominal": 1.0,
            "down": 1.0 + 0.0,
        }
        tauES_2018 = {
            "up": 0.9865 - 0.0039,
            "nominal": 0.9865,
            "down": 0.9865 + 0.0039,
        }
        configuration.add_config_parameters(
            ["mt", "et"],
            {
                "tau_ES_shift_DM0": EraModifier(
                    {
                        "2016preVFP": tauES_2016preVFP["nominal"],
                        "2016postVFP": tauES_2016postVFP["nominal"],
                        "2017": tauES_2017["nominal"],
                        "2018": tauES_2018["nominal"],
                    }
                ),
                "tau_ES_shift_DM1": EraModifier(
                    {
                        "2016preVFP": tauES_2016preVFP["nominal"],
                        "2016postVFP": tauES_2016postVFP["nominal"],
                        "2017": tauES_2017["nominal"],
                        "2018": tauES_2018["nominal"],
                    }
                ),
                "tau_ES_shift_DM10": EraModifier(
                    {
                        "2016preVFP": tauES_2016preVFP["nominal"],
                        "2016postVFP": tauES_2016postVFP["nominal"],
                        "2017": tauES_2017["nominal"],
                        "2018": tauES_2018["nominal"],
                    }
                ),
                "tau_ES_shift_DM11": EraModifier(
                    {
                        "2016preVFP": tauES_2016preVFP["nominal"],
                        "2016postVFP": tauES_2016postVFP["nominal"],
                        "2017": tauES_2017["nominal"],
                        "2018": tauES_2018["nominal"],
                    }
                ),
            },
        )
        configuration.add_modification_rule(
            ["mt", "et"],
            ReplaceProducer(
                producers=[
                    taus.TauEnergyCorrection,
                    taus.TauEnergyCorrection_Embedding,
                ],
                samples=["embedding"],
            ),
        )
        # default values until we have the correct measured values
        configuration.add_shift(
            SystematicShift(
                name="tauEs1prong0pizeroUp",
                shift_config={
                    ("mt", "et"): {
                        "tau_ES_shift_DM0": EraModifier(
                            {
                                "2016preVFP": tauES_2016preVFP["up"],
                                "2016postVFP": tauES_2016postVFP["up"],
                                "2017": tauES_2017["up"],
                                "2018": tauES_2018["up"],
                            }
                        )
                    }
                },
                producers={("mt", "et"): taus.TauPtCorrection_byValue},
            ),
            samples=["embedding"],
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEs1prong0pizeroDown",
                shift_config={
                    ("mt", "et"): {
                        "tau_ES_shift_DM0": EraModifier(
                            {
                                "2016preVFP": tauES_2016preVFP["down"],
                                "2016postVFP": tauES_2016postVFP["down"],
                                "2017": tauES_2017["down"],
                                "2018": tauES_2018["down"],
                            }
                        )
                    }
                },
                producers={("mt", "et"): taus.TauPtCorrection_byValue},
            ),
            samples=["embedding"],
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEs1prong1pizeroUp",
                shift_config={
                    ("mt", "et"): {
                        "tau_ES_shift_DM1": EraModifier(
                            {
                                "2016preVFP": tauES_2016preVFP["up"],
                                "2016postVFP": tauES_2016postVFP["up"],
                                "2017": tauES_2017["up"],
                                "2018": tauES_2018["up"],
                            }
                        )
                    }
                },
                producers={("mt", "et"): taus.TauPtCorrection_byValue},
            ),
            samples=["embedding"],
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEs1prong1pizeroDown",
                shift_config={
                    ("mt", "et"): {
                        "tau_ES_shift_DM1": EraModifier(
                            {
                                "2016preVFP": tauES_2016preVFP["down"],
                                "2016postVFP": tauES_2016postVFP["down"],
                                "2017": tauES_2017["down"],
                                "2018": tauES_2018["down"],
                            }
                        )
                    }
                },
                producers={("mt", "et"): taus.TauPtCorrection_byValue},
            ),
            samples=["embedding"],
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEs3prong0pizeroUp",
                shift_config={
                    ("mt", "et"): {
                        "tau_ES_shift_DM10": EraModifier(
                            {
                                "2016preVFP": tauES_2016preVFP["up"],
                                "2016postVFP": tauES_2016postVFP["up"],
                                "2017": tauES_2017["up"],
                                "2018": tauES_2018["up"],
                            }
                        )
                    }
                },
                producers={("mt", "et"): taus.TauPtCorrection_byValue},
            ),
            samples=["embedding"],
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEs3prong0pizeroDown",
                shift_config={
                    ("mt", "et"): {
                        "tau_ES_shift_DM10": EraModifier(
                            {
                                "2016preVFP": tauES_2016preVFP["down"],
                                "2016postVFP": tauES_2016postVFP["down"],
                                "2017": tauES_2017["down"],
                                "2018": tauES_2018["down"],
                            }
                        )
                    }
                },
                producers={("mt", "et"): taus.TauPtCorrection_byValue},
            ),
            samples=["embedding"],
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEs3prong1pizeroUp",
                shift_config={
                    ("mt", "et"): {
                        "tau_ES_shift_DM11": EraModifier(
                            {
                                "2016preVFP": tauES_2016preVFP["up"],
                                "2016postVFP": tauES_2016postVFP["up"],
                                "2017": tauES_2017["up"],
                                "2018": tauES_2018["up"],
                            }
                        )
                    }
                },
                producers={("mt", "et"): taus.TauPtCorrection_byValue},
            ),
            samples=["embedding"],
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEs3prong1pizeroDown",
                shift_config={
                    ("mt", "et"): {
                        "tau_ES_shift_DM11": EraModifier(
                            {
                                "2016preVFP": tauES_2016preVFP["down"],
                                "2016postVFP": tauES_2016postVFP["down"],
                                "2017": tauES_2017["down"],
                                "2018": tauES_2018["down"],
                            }
                        )
                    }
                },
                producers={("mt", "et"): taus.TauPtCorrection_byValue},
            ),
            samples=["embedding"],
        )

    if measure_elefakeES:
        ###################
        # Ele fake ES variations for measurement
        # first set the initial variation to nominal
        configuration.add_config_parameters(
            "global",
            {
                "ele_energyscale_barrel": 1.0,
                "ele_energyscale_endcap": 1.0,
            },
        )
        configuration.add_modification_rule(
            "global",
            ReplaceProducer(
                producers=[
                    electrons.RenameElectronPt,
                    electrons.ElectronPtCorrectionEmbedding,
                ],
                samples=["embedding"],
            ),
        )
        elefakeESvariations = [-1.5 + 0.05 * i for i in range(0, 51)]
        for elefakeESvariation in elefakeESvariations:
            name = (
                str(round(elefakeESvariation, 2))
                .replace("-", "minus")
                .replace(".", "p")
            )
            configuration.add_shift(
                SystematicShift(
                    name=f"EMBelefakeESshift_{name}",
                    shift_config={
                        ("global"): {
                            "ele_energyscale_barrel": 1.0
                            + (round(elefakeESvariation / 100.0, 5)),
                            "ele_energyscale_endcap": 1.0
                            + (round(elefakeESvariation / 100.0, 5)),
                        }
                    },
                    producers={("global"): electrons.ElectronPtCorrectionEmbedding},
                ),
                samples=["embedding"],
            )
    else:
        ele_energyscale_2016preVFP = {  # ToDo: Set to sensible value
            "barrel": {
                "up": 1.0 + 0.0,
                "nominal": 1.0,
                "down": 1.0 - 0.0,
            },
            "endcap": {
                "up": 1.0 + 0.0,
                "nominal": 1.0,
                "down": 1.0 - 0.0,
            },
        }
        ele_energyscale_2016postVFP = {  # ToDo: Set to sensible value
            "barrel": {
                "up": 1.0 + 0.0,
                "nominal": 1.0,
                "down": 1.0 - 0.0,
            },
            "endcap": {
                "up": 1.0 + 0.0,
                "nominal": 1.0,
                "down": 1.0 - 0.0,
            },
        }
        ele_energyscale_2017 = {  # ToDo: Set to sensible value
            "barrel": {
                "up": 1.0 + 0.0,
                "nominal": 1.0,
                "down": 1.0 - 0.0,
            },
            "endcap": {
                "up": 1.0 + 0.0,
                "nominal": 1.0,
                "down": 1.0 - 0.0,
            },
        }
        ele_energyscale_2018 = {
            "barrel": {
                "up": 0.9958 + 0.005,
                "nominal": 0.9958,
                "down": 0.9958 - 0.005,
            },
            "endcap": {
                "up": 0.9921 + 0.0125,
                "nominal": 0.9921,
                "down": 0.9921 - 0.0125,
            },
        }
        configuration.add_config_parameters(
            "global",
            {
                "ele_energyscale_barrel": EraModifier(
                    {
                        "2016preVFP": ele_energyscale_2016preVFP["barrel"]["nominal"],
                        "2016postVFP": ele_energyscale_2016postVFP["barrel"]["nominal"],
                        "2017": ele_energyscale_2017["barrel"]["nominal"],
                        "2018": ele_energyscale_2018["barrel"]["nominal"],
                    }
                ),
                "ele_energyscale_endcap": EraModifier(
                    {
                        "2016preVFP": ele_energyscale_2016preVFP["endcap"]["nominal"],
                        "2016postVFP": ele_energyscale_2016postVFP["endcap"]["nominal"],
                        "2017": ele_energyscale_2017["endcap"]["nominal"],
                        "2018": ele_energyscale_2018["endcap"]["nominal"],
                    }
                ),
            },
        )
        configuration.add_modification_rule(
            "global",
            ReplaceProducer(
                producers=[
                    electrons.RenameElectronPt,
                    electrons.ElectronPtCorrectionEmbedding,
                ],
                samples=["embedding"],
            ),
        )
        configuration.add_shift(
            SystematicShift(
                name="eleEsBarrelUp",
                shift_config={
                    ("global"): {
                        "ele_energyscale_barrel": EraModifier(
                            {
                                "2016preVFP": ele_energyscale_2016preVFP["barrel"][
                                    "up"
                                ],
                                "2016postVFP": ele_energyscale_2016postVFP["barrel"][
                                    "up"
                                ],
                                "2017": ele_energyscale_2017["barrel"]["up"],
                                "2018": ele_energyscale_2018["barrel"]["up"],
                            }
                        )
                    }
                },
                producers={("global"): electrons.ElectronPtCorrectionEmbedding},
            ),
            samples=["embedding"],
        )
        configuration.add_shift(
            SystematicShift(
                name="eleEsBarrelDown",
                shift_config={
                    ("global"): {
                        "ele_energyscale_barrel": EraModifier(
                            {
                                "2016preVFP": ele_energyscale_2016preVFP["barrel"][
                                    "down"
                                ],
                                "2016postVFP": ele_energyscale_2016postVFP["barrel"][
                                    "down"
                                ],
                                "2017": ele_energyscale_2017["barrel"]["down"],
                                "2018": ele_energyscale_2018["barrel"]["down"],
                            }
                        )
                    }
                },
                producers={("global"): electrons.ElectronPtCorrectionEmbedding},
            ),
            samples=["embedding"],
        )
        configuration.add_shift(
            SystematicShift(
                name="eleEsEndcapUp",
                shift_config={
                    ("global"): {
                        "ele_energyscale_endcap": EraModifier(
                            {
                                "2016preVFP": ele_energyscale_2016preVFP["endcap"][
                                    "up"
                                ],
                                "2016postVFP": ele_energyscale_2016postVFP["endcap"][
                                    "up"
                                ],
                                "2017": ele_energyscale_2017["endcap"]["up"],
                                "2018": ele_energyscale_2018["endcap"]["up"],
                            }
                        )
                    }
                },
                producers={("global"): electrons.ElectronPtCorrectionEmbedding},
            ),
            samples=["embedding"],
        )
        configuration.add_shift(
            SystematicShift(
                name="eleEsEndcapDown",
                shift_config={
                    ("global"): {
                        "ele_energyscale_endcap": EraModifier(
                            {
                                "2016preVFP": ele_energyscale_2016preVFP["endcap"][
                                    "down"
                                ],
                                "2016postVFP": ele_energyscale_2016postVFP["endcap"][
                                    "down"
                                ],
                                "2017": ele_energyscale_2017["endcap"]["down"],
                                "2018": ele_energyscale_2018["endcap"]["down"],
                            }
                        )
                    }
                },
                producers={("global"): electrons.ElectronPtCorrectionEmbedding},
            ),
            samples=["embedding"],
        )

    return configuration

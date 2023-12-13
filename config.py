from __future__ import annotations  # needed for type annotations in > python 3.7

from typing import List

from .producers import electrons as electrons
from .producers import event as event
from .producers import genparticles as genparticles
from .producers import jets as jets
from .producers import met as met
from .producers import muons as muons
from .producers import pairquantities as pairquantities
from .producers import pairselection as pairselection
from .producers import scalefactors as scalefactors
from .producers import taus as taus
from .producers import triggers as triggers
from .quantities import nanoAOD as nanoAOD
from .quantities import output as q
from .tau_triggersetup import add_diTauTriggerSetup
from .tau_variations import add_tauVariations
from .jet_variations import add_jetVariations
from .tau_embedding_settings import setup_embedding
from .btag_variations import add_btagVariations
from .jec_data import add_jetCorrectionData
from code_generation.configuration import Configuration
from code_generation.modifiers import EraModifier, SampleModifier
from code_generation.rules import AppendProducer, RemoveProducer, ReplaceProducer
from code_generation.systematics import SystematicShift, SystematicShiftByQuantity


def build_config(
    era: str,
    sample: str,
    scopes: List[str],
    shifts: List[str],
    available_sample_types: List[str],
    available_eras: List[str],
    available_scopes: List[str],
):
    configuration = Configuration(
        era,
        sample,
        scopes,
        shifts,
        available_sample_types,
        available_eras,
        available_scopes,
    )

    # first add default parameters necessary for all scopes
    configuration.add_config_parameters(
        "global",
        {
            # for LHE weights
            "muR": 1.0,
            "muF": 1.0,
            "PU_reweighting_file": EraModifier(
                {
                    "2016preVFP": "data/jsonpog-integration/POG/LUM/2016preVFP_UL/puWeights.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/LUM/2016postVFP_UL/puWeights.json.gz",
                    "2017": "data/jsonpog-integration/POG/LUM/2017_UL/puWeights.json.gz",
                    "2018": "data/jsonpog-integration/POG/LUM/2018_UL/puWeights.json.gz",
                    "2022EE": "data/jsonpog-integration/POG/LUM/2018_UL/puWeights.json.gz", ## TODO: update to 2022 PU file when available. These lines only for testing
                    "2022postEE": "data/jsonpog-integration/POG/LUM/2018_UL/puWeights.json.gz", ## TODO: update to 2022 PU file when available. These lines only for testing
                }
            ),
            "PU_reweighting_era": EraModifier(
                {
                    "2016preVFP": "Collisions16_UltraLegacy_goldenJSON",
                    "2016postVFP": "Collisions16_UltraLegacy_goldenJSON",
                    "2017": "Collisions17_UltraLegacy_goldenJSON",
                    "2018": "Collisions18_UltraLegacy_goldenJSON",
                    "2022EE": "Collisions18_UltraLegacy_goldenJSON", ## TODO: update to 2022 PU file when available. These lines only for testing
                    "2022postEE": "Collisions18_UltraLegacy_goldenJSON", ## TODO: update to 2022 PU file when available. These lines only for testing
                }
            ),
            "PU_reweighting_variation": "nominal",
            "golden_json_file": EraModifier(
                {
                    "2016preVFP": "data/golden_json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt",
                    "2016postVFP": "data/golden_json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt",
                    "2017": "data/golden_json/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt",
                    "2018": "data/golden_json/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt",
                    "2022EE": "data/golden_json/Cert_Collisions2022_355100_362760_Golden.json.txt",
                    "2022postEE": "data/golden_json/Cert_Collisions2022_355100_362760_Golden.json.txt",
                }
            ),
            "met_filters": EraModifier(
                {
                    "2016preVFP": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        #"Flag_BadPFMuonDzFilter",  # only since nanoAODv9 available
                        "Flag_eeBadScFilter",
                    ],
                    "2016postVFP": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        #"Flag_BadPFMuonDzFilter",  # only since nanoAODv9 available
                        "Flag_eeBadScFilter",
                    ],
                    "2017": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        #"Flag_BadPFMuonDzFilter",  # only since nanoAODv9 available
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
                        #"Flag_BadPFMuonDzFilter",  # only since nanoAODv9 available

                        "Flag_eeBadScFilter",
                        "Flag_ecalBadCalibFilter",
                    ],
                    ## all years seem the same? just copying to 2022 then
                    "2022EE": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        #"Flag_BadPFMuonDzFilter",  # only since nanoAODv9 available

                        "Flag_eeBadScFilter",
                        "Flag_ecalBadCalibFilter",
                    ],
                    "2022postEE": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        #"Flag_BadPFMuonDzFilter",  # only since nanoAODv9 available

                        "Flag_eeBadScFilter",
                        "Flag_ecalBadCalibFilter",
                    ],
                }
            ),
        },
    )
    configuration.add_config_parameters(
        ["et", "mt", "tt"],
        {
            "tau_dms": "0,1,10,11",
            "tau_sf_file": EraModifier(
                {
                    "2016preVFP": "data/jsonpog-integration/POG/TAU/2016preVFP_UL/tau.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/TAU/2016postVFP_UL/tau.json.gz",
                    "2017": "data/jsonpog-integration/POG/TAU/2017_UL/tau.json.gz",
                    "2018": "data/jsonpog-integration/POG/TAU/2018_UL/tau.json.gz",
                    "2022EE": "data/jsonpog-integration/POG/TAU/2018_UL/tau.json.gz", ## TODO: update to 2022 Tau file when available. These lines only for testing
                    "2022postEE": "data/jsonpog-integration/POG/TAU/2018_UL/tau.json.gz", ## TODO: update to 2022 Tau file when available. These lines only for testing
                }
            ),
            "tau_ES_json_name": "tau_energy_scale",
            "tau_id_algorithm": "DeepTau2017v2p1",
            "tau_ES_shift_DM0": "nom",
            "tau_ES_shift_DM1": "nom",
            "tau_ES_shift_DM10": "nom",
            "tau_ES_shift_DM11": "nom",
            "tau_elefake_es_DM0_barrel": "nom",
            "tau_elefake_es_DM0_endcap": "nom",
            "tau_elefake_es_DM1_barrel": "nom",
            "tau_elefake_es_DM1_endcap": "nom",
            "tau_mufake_es": "nom",
        },
    )
    # muon base selection:
    configuration.add_config_parameters(
        "global",
        {
            "min_muon_pt": 10.0,
            "max_muon_eta": 2.4,
            "max_muon_dxy": 0.045,
            "max_muon_dz": 0.2,
            "muon_id": "Muon_mediumId",
            "muon_iso_cut": 0.3,
        },
    )
    # electron base selection:
    configuration.add_config_parameters(
        "global",
        {
            "min_ele_pt": 10.0,
            "max_ele_eta": 2.5,
            "max_ele_dxy": 0.045,
            "max_ele_dz": 0.2,
            "max_ele_iso": 0.3,
            "ele_id": EraModifier(
                {
                    "2016preVFP":"Electron_mvaFall17V2noIso_WP90",
                    "2016postVFP":"Electron_mvaFall17V2noIso_WP90",
                    "2017":"Electron_mvaFall17V2noIso_WP90",
                    "2018":"Electron_mvaFall17V2noIso_WP90",
                    "2022EE": "Electron_cutBased", 
                    "2022postEE": "Electron_cutBased", 
                },
            ),
            ## Electron_cutBased	UChar_t	cut-based ID RunIII Winter22 (0:fail, 1:veto, 2:loose, 3:medium, 4:tight)
            "ele_id_wp": 4,
        },
    )
    # jet base selection:
    configuration.add_config_parameters(
        "global",
        {
            "min_jet_pt": 30,
            "max_jet_eta": 4.7,
            "jet_id": 2,  # default: 2==pass tight ID and fail tightLepVeto
            "jet_puid": EraModifier(
                {
                    "2016preVFP": 1,  # 0==fail, 1==pass(loose), 3==pass(loose,medium), 7==pass(loose,medium,tight)
                    "2016postVFP": 1,  # 0==fail, 1==pass(loose), 3==pass(loose,medium), 7==pass(loose,medium,tight)
                    "2017": 4,  # 0==fail, 4==pass(loose), 6==pass(loose,medium), 7==pass(loose,medium,tight)
                    "2018": 4,  # 0==fail, 4==pass(loose), 6==pass(loose,medium), 7==pass(loose,medium,tight)
                    "2022EE": 4, ## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022postEE": 4, ## TODO: update to 2022 recommendation when available. These lines only for testing
                }
            ),
            "jet_puid_max_pt": 50,  # recommended to apply puID only for jets below 50 GeV
            "jet_reapplyJES": False,
            "jet_jes_sources": '{""}',
            "jet_jes_shift": 0,
            "jet_jer_shift": '"nom"',  # or '"up"', '"down"'
            "jet_jec_file": EraModifier(
                {
                    "2016preVFP": '"data/jsonpog-integration/POG/JME/2016preVFP_UL/jet_jerc.json.gz"',
                    "2016postVFP": '"data/jsonpog-integration/POG/JME/2016postVFP_UL/jet_jerc.json.gz"',
                    "2017": '"data/jsonpog-integration/POG/JME/2017_UL/jet_jerc.json.gz"',
                    "2018": '"data/jsonpog-integration/POG/JME/2018_UL/jet_jerc.json.gz"',
                    "2022EE": '"data/jsonpog-integration/POG/JME/2022_Prompt/jet_jerc.json.gz"', 
                    "2022postEE": '"data/jsonpog-integration/POG/JME/2022_Summer22EE/jet_jerc.json.gz"', 
                }
            ),
            "jet_jer_tag": EraModifier(
                {
                    "2016preVFP": '"Summer20UL16APV_JRV3_MC"',
                    "2016postVFP": '"Summer20UL16_JRV3_MC"',
                    "2017": '"Summer19UL17_JRV2_MC"',
                    "2018": '"Summer19UL18_JRV2_MC"',
                    "2022EE": '"JR_Winter22Run3_V1_MC"',
                    "2022postEE": '"Summer22EEPrompt22_JRV1_MC"',
                }
            ),
            "jet_jes_tag_data": '""',
            "jet_jes_tag": EraModifier(
                {
                    "2016preVFP": '"Summer19UL16APV_V7_MC"',
                    "2016postVFP": '"Summer19UL16_V7_MC"',
                    "2017": '"Summer19UL17_V5_MC"',
                    "2018": '"Summer19UL18_V5_MC"',
                    "2022EE": '"Winter22Run3_V2_MC"',
                    "2022postEE": '"Summer22EEPrompt22_V1_MC"',
                }
            ),
            "jet_jec_algo": '"AK4PFPuppi"',
        },
    )
    # bjet base selection:
    configuration.add_config_parameters(
        "global",
        {
            "min_bjet_pt": 20,
            "max_bjet_eta": EraModifier(
                {
                    "2016preVFP": 2.5,
                    "2016postVFP": 2.5,
                    "2017": 2.5,
                    "2018": 2.5,
                    "2022EE": 2.5,
                    "2022postEE": 2.5,
                }
            ),
            "btag_cut": EraModifier(  # medium
                {
                    "2016preVFP": 0.2598,  # taken from https://twiki.cern.ch/twiki/bin/view/CMS/BtagRecommendation106XUL16preVFP
                    "2016postVFP": 0.2489,  # taken from https://twiki.cern.ch/twiki/bin/view/CMS/BtagRecommendation106XUL16postVFP
                    "2017": 0.3040,
                    "2018": 0.2783,
                    "2022EE": 0.245,## from 2022, switching to ParticleNet b-tagging for better performance 
                    "2022postEE": 0.2605 ##  taken from https://btv-wiki.docs.cern.ch/ScaleFactors/Run3Summer22/
                    
                }
            ),
        },
    )
    # bjet scale factors
    configuration.add_config_parameters(
        scopes,
        {
            "btag_sf_file": EraModifier(
                {
                    "2016preVFP": "data/jsonpog-integration/POG/BTV/2016preVFP_UL/btagging.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/BTV/2016postVFP_UL/btagging.json.gz",
                    "2017": "data/jsonpog-integration/POG/BTV/2017_UL/btagging.json.gz",
                    "2018": "data/jsonpog-integration/POG/BTV/2018_UL/btagging.json.gz",
                    "2022EE": "data/jsonpog-integration/POG/BTV/2018_UL/btagging.json.gz",## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022postEE": "data/jsonpog-integration/POG/BTV/2018_UL/btagging.json.gz",## TODO: update to 2022 recommendation when available. These lines only for testing
                }
            ),
            "btag_sf_variation": "central",## TODO: update to 2022 recommendation when available. These lines only for testing
            "btag_corr_algo": "deepJet_shape",## TODO: update to 2022 recommendation when available. These lines only for testing
        },
    )
    # leptonveto base selection:
    configuration.add_config_parameters(
        "global",
        {
            "min_dielectronveto_pt": 15.0,
            "dielectronveto_id": "Electron_cutBased",
            "dielectronveto_id_wp": 1,
            "min_dimuonveto_pt": 15.0,
            "dimuonveto_id": "Muon_looseId",
            "dileptonveto_dR": 0.15,
        },
    )
    ###### scope Specifics ######
    # MT/TT/ET scope tau ID flags and SFs
    configuration.add_config_parameters(
        ["mt", "tt", "et"],
        {
            "vsjet_tau_id": [
                {
                    "tau_id_discriminator": "DeepTau2017v2p1VSjet",
                    "tau_1_vsjet_sf_outputname": "id_wgt_tau_vsJet_{wp}_1".format(
                        wp=wp
                    ),
                    "tau_2_vsjet_sf_outputname": "id_wgt_tau_vsJet_{wp}_2".format(
                        wp=wp
                    ),
                    "vsjet_tau_id_WP": "{wp}".format(wp=wp),
                    "tau_1_vsjet_id_outputname": "id_tau_vsJet_{wp}_1".format(wp=wp),
                    "tau_2_vsjet_id_outputname": "id_tau_vsJet_{wp}_2".format(wp=wp),
                    "vsjet_tau_id_WPbit": bit,
                }
                for wp, bit in {
                    "VVVLoose": 1,
                    "VVLoose": 2,
                    "VLoose": 3,
                    "Loose": 4,
                    "Medium": 5,
                    "Tight": 6,
                    "VTight": 7,
                    "VVTight": 8,
                }.items()
            ],
            "vsele_tau_id": [
                {
                    "tau_id_discriminator": "DeepTau2017v2p1VSe",
                    "tau_1_vsele_sf_outputname": "id_wgt_tau_vsEle_{wp}_1".format(
                        wp=wp
                    ),
                    "tau_2_vsele_sf_outputname": "id_wgt_tau_vsEle_{wp}_2".format(
                        wp=wp
                    ),
                    "vsele_tau_id_WP": "{wp}".format(wp=wp),
                    "tau_1_vsele_id_outputname": "id_tau_vsEle_{wp}_1".format(wp=wp),
                    "tau_2_vsele_id_outputname": "id_tau_vsEle_{wp}_2".format(wp=wp),
                    "vsele_tau_id_WPbit": bit,
                }
                for wp, bit in {
                    # "VVVLoose": 1, ## this will crash
                    "VVLoose": 2,
                    "VLoose": 3,
                    "Loose": 4,
                    "Medium": 5,
                    "Tight": 6,
                    "VTight": 7,
                    "VVTight": 8,
                }.items()
            ],
            "vsmu_tau_id": [
                {
                    "tau_id_discriminator": "DeepTau2017v2p1VSmu",
                    "tau_1_vsmu_sf_outputname": "id_wgt_tau_vsMu_{wp}_1".format(wp=wp),
                    "tau_2_vsmu_sf_outputname": "id_wgt_tau_vsMu_{wp}_2".format(wp=wp),
                    "vsmu_tau_id_WP": "{wp}".format(wp=wp),
                    "tau_1_vsmu_id_outputname": "id_tau_vsMu_{wp}_1".format(wp=wp),
                    "tau_2_vsmu_id_outputname": "id_tau_vsMu_{wp}_2".format(wp=wp),
                    "vsmu_tau_id_WPbit": bit,
                }
                for wp, bit in {
                    "VLoose": 1,
                    "Loose": 2,
                    "Medium": 3,
                    "Tight": 4,
                }.items()
            ],
            "tau_sf_vsele_barrel": "nom",  # or "up"/"down" for up/down variation
            "tau_sf_vsele_endcap": "nom",  # or "up"/"down" for up/down variation
            "tau_sf_vsmu_wheel1": "nom",
            "tau_sf_vsmu_wheel2": "nom",
            "tau_sf_vsmu_wheel3": "nom",
            "tau_sf_vsmu_wheel4": "nom",
            "tau_sf_vsmu_wheel5": "nom",
        },
    )
    # MT / ET tau id sf variations
    configuration.add_config_parameters(
        ["mt", "et"],
        {
            "tau_sf_vsjet_tau30to35": "nom",
            "tau_sf_vsjet_tau35to40": "nom",
            "tau_sf_vsjet_tau40to500": "nom",
            "tau_sf_vsjet_tau500to1000": "nom",
            "tau_sf_vsjet_tau1000toinf": "nom",
            "tau_vsjet_sf_dependence": "pt",  # or "dm", "eta"
        },
    )
    # TT tau id sf variations
    configuration.add_config_parameters(
        ["tt"],
        {
            "tau_sf_vsjet_tauDM0": "nom",
            "tau_sf_vsjet_tauDM1": "nom",
            "tau_sf_vsjet_tauDM10": "nom",
            "tau_sf_vsjet_tauDM11": "nom",
            "tau_vsjet_sf_dependence": "dm",  # or "dm", "eta"
        },
    )

    # MT / ET tau selection
    configuration.add_config_parameters(
        ["et", "mt"],
        {
            "min_tau_pt": 30.0, # use AN definition
            "max_tau_eta": 2.3,
            "max_tau_dz": 0.2,
            "vsjet_tau_id_bit": 1,#"VVVLoose": 1,"VVLoose": 2,"VLoose": 3,"Loose": 4,"Medium": 5,"Tight": 6,
            "vsele_tau_id_bit": 2,# "VVLoose": 2,"VLoose": 3,"Loose": 4,"Medium": 5,"Tight": 6,
            "vsmu_tau_id_bit": 4, #"VLoose": 1,"Loose": 2,"Medium": 3,"Tight": 4,
        },
    )
    # TT tau selection:
    configuration.add_config_parameters(
        ["tt"],
        {
            "min_tau_pt": 35.0,
            "max_tau_eta": 2.3,
            "max_tau_dz": 0.2,
            "vsjet_tau_id_bit": 1,
            "vsele_tau_id_bit": 2,
            "vsmu_tau_id_bit": 1,
        },
    )

    # MT/MM scope Muon selection
    configuration.add_config_parameters(
        ["mt", "mm"],
        {
            "muon_index_in_pair": 0,
            "min_muon_pt": 23.0,
            "max_muon_eta": 2.1,
            "muon_iso_cut": 0.3,
        },
    )
    # Muon scale factors configuration
    configuration.add_config_parameters(
        ["mt", "mm", "em"],
        {
            "muon_sf_file": EraModifier(
                {
                    "2016preVFP": "data/jsonpog-integration/POG/MUO/2016preVFP_UL/muon_Z.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/MUO/2016postVFP_UL/muon_Z.json.gz",
                    "2017": "data/jsonpog-integration/POG/MUO/2017_UL/muon_Z.json.gz",
                    "2018": "data/jsonpog-integration/POG/MUO/2018_UL/muon_Z.json.gz",
                    "2022EE": "data/jsonpog-integration/POG/MUO/2022EE_UL/ScaleFactors_Muon_trackerMuons_Z_2022_Prompt_ID_ISO_schemaV2.json.gz",## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022postEE": "data/jsonpog-integration/POG/MUO/2022postEE_UL/ScaleFactors_Muon_trackerMuons_Z_2022EE_Prompt_ID_ISO_schemaV2.json.gz",## TODO: update to 2022 recommendation when available. These lines only for testing
                }
            ),
            "muon_id_sf_name": "NUM_MediumID_DEN_TrackerMuons",
            "muon_iso_sf_name": "NUM_TightPFIso_DEN_MediumID",
            "muon_sf_year_id": EraModifier(
                {
                    "2016preVFP": "2016preVFP",
                    "2016postVFP": "2016postVFP",
                    "2017": "2017",
                    "2018": "2018",
                    "2022EE": "2022EE", # since 2022, year id is not needed, but we still provide it to avoid compilation crash
                    "2022postEE": "2022postEE", # since 2022, year id is not needed, but we still provide it to avoid compilation crash
                }),
            "muon_sf_varation": "nominal",  # "sf" is nominal, "systup"/"systdown" are up/down variations
        },
    )
    # electron scale factors configuration
    configuration.add_config_parameters(
        ["et", "ee", "em"],
        {
            "ele_sf_file": EraModifier(
                {
                    "2016preVFP": "data/jsonpog-integration/POG/EGM/2016preVFP_UL/electron.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/EGM/2016postVFP_UL/electron.json.gz",
                    "2017": "data/jsonpog-integration/POG/EGM/2017_UL/electron.json.gz",
                    "2018": "data/jsonpog-integration/POG/EGM/2018_UL/electron.json.gz",
                    "2022EE": "data/jsonpog-integration/POG/EGM/2018_UL/electron.json.gz", ## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022postEE": "data/jsonpog-integration/POG/EGM/2018_UL/electron.json.gz", ## TODO: update to 2022 recommendation when available. These lines only for testing
                }
            ),
            "ele_id_sf_name": "UL-Electron-ID-SF",
            "ele_sf_year_id": EraModifier(
                {
                    "2016preVFP": "2016preVFP",
                    "2016postVFP": "2016postVFP",
                    "2017": "2017",
                    "2018": "2018",
                    "2022EE": "2018",## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022postEE": "2018",## TODO: update to 2022 recommendation when available. These lines only for testing
                }
            ),
            "ele_sf_varation": "sf",  # "sf" is nominal, "sfup"/"sfdown" are up/down variations
        },
    )
    # ET scope electron selection
    configuration.add_config_parameters(
        ["et"],
        {
            "electron_index_in_pair": 0,
            "min_electron_pt": 25.0,
            "max_electron_eta": 2.1,
            "electron_iso_cut": 0.5,
        },
    )
    # EE scope electron selection
    configuration.add_config_parameters(
        ["ee"],
        {
            "electron_index_in_pair": 0,
            "second_electron_index_in_pair": 0,
            "min_electron_pt": 25.0,
            "max_electron_eta": 2.1,
            "electron_iso_cut": 0.3,
        },
    )
    # EM scope selection
    configuration.add_config_parameters(
        ["em"],
        {
            "electron_index_in_pair": 0,
            "min_electron_pt": 25.0,
            "max_electron_eta": 2.1,
            "electron_iso_cut": 0.3,
            "muon_index_in_pair": 1,
            "min_muon_pt": 23.0,
            "max_muon_eta": 2.1,
            "muon_iso_cut": 0.15,
        },
    )
    configuration.add_config_parameters(
        ["mm"],
        {
            "min_muon_pt": 20.0,
            "max_muon_eta": 2.1,
            "muon_iso_cut": 0.15,
            "second_muon_index_in_pair": 1,
        },
    )

    ## all scopes misc settings
    configuration.add_config_parameters(
        scopes,
        {
            "deltaR_jet_veto": 0.5,
            "pairselection_min_dR": 0.5,
        },
    )
    ## all scopes MET selection
    configuration.add_config_parameters(
        scopes,
        {
            "propagateLeptons": SampleModifier(
                {"data": False},
                default=True,
            ),
            "propagateJets": SampleModifier(
                {"data": False},
                default=True,
            ),
            "recoil_corrections_file": EraModifier(
                {
                    "2016preVFP": "data/recoil_corrections/Type1_PuppiMET_2016.root",  # These are likely from Legacy data sets, therefore no difference in pre and postVFP
                    "2016postVFP": "data/recoil_corrections/Type1_PuppiMET_2016.root",  # These are likely from Legacy data sets, therefore no difference in pre and postVFP
                    "2017": "data/recoil_corrections/Type1_PuppiMET_2017.root",
                    "2018": "data/recoil_corrections/Type1_PuppiMET_2018.root",
                    "2022EE": "data/recoil_corrections/Type1_PuppiMET_2018.root",## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022postEE": "data/recoil_corrections/Type1_PuppiMET_2018.root",## TODO: update to 2022 recommendation when available. These lines only for testing
                }
            ),
            "recoil_systematics_file": EraModifier(
                {
                    "2016preVFP": "data/recoil_corrections/PuppiMETSys_2016.root",  # These are likely from Legacy data sets, therefore no difference in pre and postVFP
                    "2016postVFP": "data/recoil_corrections/PuppiMETSys_2016.root",  # These are likely from Legacy data sets, therefore no difference in pre and postVFP
                    "2017": "data/recoil_corrections/PuppiMETSys_2017.root",
                    "2018": "data/recoil_corrections/PuppiMETSys_2018.root",
                    "2022EE": "data/recoil_corrections/PuppiMETSys_2018.root",## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022postEE": "data/recoil_corrections/PuppiMETSys_2018.root",## TODO: update to 2022 recommendation when available. These lines only for testing
                }
            ),
            "applyRecoilCorrections": SampleModifier(
                {
                    "wjets": True,
                    "dyjets": True,
                    "electroweak_boson": True,
                    "ggh_htautau": True,
                    "vbf_htautau": True,
                    "rem_htautau": True,
                    "ggh_hww": True,
                    "vbf_hww": True,
                    "rem_VH": True,
                },
                default=False,
            ),
            "apply_recoil_resolution_systematic": False,
            "apply_recoil_response_systematic": False,
            "recoil_systematic_shift_up": False,
            "recoil_systematic_shift_down": False,
            "min_jetpt_met_propagation": 15,
        },
    )

    configuration.add_config_parameters(
        scopes,
        {
            "ggHNNLOweightsRootfile": "data/htxs/NNLOPS_reweight.root",
            "ggH_generator": "powheg",
            "zptmass_file": EraModifier(
                {
                    "2016preVFP": "data/zpt/htt_scalefactors_legacy_2016.root",  # ToDO: Measured in legacy, therefore the same for pre- and postVFP for now
                    "2016postVFP": "data/zpt/htt_scalefactors_legacy_2016.root",  # ToDO: Measured in legacy, therefore the same for pre- and postVFP for now
                    "2017": "data/zpt/htt_scalefactors_legacy_2017.root",
                    "2018": "data/zpt/htt_scalefactors_legacy_2018.root",
                    "2022EE": "data/zpt/htt_scalefactors_legacy_2018.root",## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022postEE": "data/zpt/htt_scalefactors_legacy_2018.root",## TODO: update to 2022 recommendation when available. These lines only for testing
                }
            ),
            "zptmass_functor": "zptmass_weight_nom",
            "zptmass_arguments": "z_gen_mass,z_gen_pt",
        },
    )

    # add muon scalefactors from embedding measurements
    configuration.add_config_parameters(
        ["mt", "mm", "em"],
        {
            "mc_muon_sf_file": EraModifier(
                {
                    "2016preVFP": "data/embedding/muon_2016preVFPUL.json.gz",
                    "2016postVFP": "data/embedding/muon_2016postVFPUL.json.gz",
                    "2017": "data/embedding/muon_2017UL.json.gz",
                    "2018": "data/embedding/muon_2018UL.json.gz",
                    "2022EE": "data/embedding/muon_2018UL.json.gz",## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022postEE": "data/embedding/muon_2018UL.json.gz",## TODO: update to 2022 recommendation when available. These lines only for testing
                }
            ),
            "mc_muon_id_sf": "ID_pt_eta_bins",
            "mc_muon_iso_sf": "Iso_pt_eta_bins",
            "mc_muon_id_extrapolation": 1.0,  # for nominal case
            "mc_muon_iso_extrapolation": 1.0,  # for nominal case
        },
    )
    # add electron scalefactors from embedding measurements
    configuration.add_config_parameters(
        ["et", "ee", "em"],
        {
            "mc_electron_sf_file": EraModifier(
                {
                    "2016preVFP": "data/embedding/electron_2016preVFPUL.json.gz",
                    "2016postVFP": "data/embedding/electron_2016postVFPUL.json.gz",
                    "2017": "data/embedding/electron_2017UL.json.gz",
                    "2018": "data/embedding/electron_2018UL.json.gz",
                    "2022EE": "data/embedding/electron_2018UL.json.gz", ## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022postEE": "data/embedding/electron_2018UL.json.gz", ## TODO: update to 2022 recommendation when available. These lines only for testing
                }
            ),
            "mc_electron_id_sf": "ID90_pt_eta_bins",
            "mc_electron_iso_sf": "Iso_pt_eta_bins",
            "mc_electron_id_extrapolation": 1.0,  # for nominal case
            "mc_electron_iso_extrapolation": 1.0,  # for nominal case
        },
    )
    # muon trigger SF settings from embedding measurements
    configuration.add_config_parameters(
        ["mt", "mm"],
        {
            "singlemuon_trigger_sf_mc": EraModifier(
                {   
                    ## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022EE": [
                        {
                            "flagname": "trg_wgt_single_mu24",
                            "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_mu27",
                            "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_mu24ormu27",
                            "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2022postEE": [
                        {
                            "flagname": "trg_wgt_single_mu24",
                            "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_mu27",
                            "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_mu24ormu27",
                            "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2018": [
                        {
                            "flagname": "trg_wgt_single_mu24",
                            "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_mu27",
                            "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_mu24ormu27",
                            "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2017": [
                        {
                            "flagname": "trg_wgt_single_mu24",
                            "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_mu27",
                            "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_mu24ormu27",
                            "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_wgt_single_mu22",
                            "mc_trigger_sf": "Trg_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_wgt_single_mu22",
                            "mc_trigger_sf": "Trg_pt_eta_bins",
                            "mc_muon_trg_extrapolation": 1.0,  # for nominal case
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
            "singlelectron_trigger_sf_mc": EraModifier(
                {   ## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022EE": [
                        {
                            "flagname": "trg_wgt_single_ele32",
                            "mc_trigger_sf": "Trg32_Iso_pt_eta_bins",
                            "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_ele35",
                            "mc_trigger_sf": "Trg35_Iso_pt_eta_bins",
                            "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_ele32orele35",
                            "mc_trigger_sf": "Trg32_or_Trg35_Iso_pt_eta_bins",
                            "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_ele27orele32orele35",
                            "mc_trigger_sf": "Trg_Iso_pt_eta_bins",
                            "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2022postEE": [
                        {
                            "flagname": "trg_wgt_single_ele32",
                            "mc_trigger_sf": "Trg32_Iso_pt_eta_bins",
                            "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_ele35",
                            "mc_trigger_sf": "Trg35_Iso_pt_eta_bins",
                            "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_ele32orele35",
                            "mc_trigger_sf": "Trg32_or_Trg35_Iso_pt_eta_bins",
                            "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_ele27orele32orele35",
                            "mc_trigger_sf": "Trg_Iso_pt_eta_bins",
                            "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2018": [
                        {
                            "flagname": "trg_wgt_single_ele32",
                            "mc_trigger_sf": "Trg32_Iso_pt_eta_bins",
                            "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_ele35",
                            "mc_trigger_sf": "Trg35_Iso_pt_eta_bins",
                            "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_ele32orele35",
                            "mc_trigger_sf": "Trg32_or_Trg35_Iso_pt_eta_bins",
                            "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_ele27orele32orele35",
                            "mc_trigger_sf": "Trg_Iso_pt_eta_bins",
                            "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2017": [
                        {
                            "flagname": "trg_wgt_single_ele32",
                            "mc_trigger_sf": "Trg32_Iso_pt_eta_bins",
                            "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_ele35",
                            "mc_trigger_sf": "Trg35_Iso_pt_eta_bins",
                            "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_ele32orele35",
                            "mc_trigger_sf": "Trg32_or_Trg35_Iso_pt_eta_bins",
                            "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                        {
                            "flagname": "trg_wgt_single_ele27orele32orele35",
                            "mc_trigger_sf": "Trg_Iso_pt_eta_bins",
                            "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                        },
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_wgt_single_ele25",
                            "mc_trigger_sf": "Trg25_Iso_pt_eta_bins",
                            "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                        }
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_wgt_single_ele25",
                            "mc_trigger_sf": "Trg25_Iso_pt_eta_bins",
                            "mc_electron_trg_extrapolation": 1.0,  # for nominal case
                        }
                    ],
                }
            )
        },
    )

    configuration.add_producers(
        "global",
        [
            # event.RunLumiEventFilter,
            event.SampleFlags,
            event.Lumi,
            # event.npartons,
            event.MetFilter,
            event.PUweights,
            # event.LHE_Scale_weight,
            muons.BaseMuons,
            electrons.RenameElectronPt,
            electrons.BaseElectrons,
            jets.JetEnergyCorrection,
            event.DiLeptonVeto,
            met.MetBasics,
        ],
    )
    # As now 2022 data has no Jet_puID, so no possible to do JetPUIDCut
    if era == "2022EE":
        configuration.add_producers(
            "global",
            [
                jets.GoodJets_2022,
                jets.GoodBJets_2022,
                jets.GoodPreBJets_2022],
            ),
    elif era == "2022postEE":
        configuration.add_producers(
            "global",
            [
                jets.GoodJets_2022,
                jets.GoodBJets_2022,
                jets.GoodPreBJets_2022],
            ),
    else:
        configuration.add_producers(
            "global",
            [
                jets.GoodJets,
                jets.GoodBJets,
                jets.GoodPreBJets],
            ),
        
    ## add prefiring
    if era != "2018" and era != "2022EE" and era != "2022postEE":
        configuration.add_producers(
            "global",
            [
                event.PrefireWeight,
            ],
        )
    # common
    configuration.add_producers(
        scopes,
        [
            jets.JetCollection,
            jets.BasicJetQuantities,
            jets.BJetCollection,
            jets.PreBJetCollection,
            jets.BasicBJetQuantities,
            scalefactors.btagging_SF,
            met.MetCorrections,
            met.PFMetCorrections,
            pairquantities.DiTauPairMETQuantities,
            genparticles.GenMatching,
        ],
    )
    configuration.add_producers(
        "mm",
        [
            muons.GoodMuons,
            muons.VetoMuons,
            muons.VetoSecondMuon,
            muons.ExtraMuonsVeto,
            muons.NumberOfGoodMuons,
            pairselection.ZMuMuPairSelection,
            pairselection.GoodMuMuPairFilter,
            pairselection.LVMu1,
            pairselection.LVMu2,
            pairselection.LVMu1Uncorrected,
            pairselection.LVMu2Uncorrected,
            pairquantities.MuMuPairQuantities,
            genparticles.MuMuGenPairQuantities,
            scalefactors.MuonIDIso_SF,
            triggers.MuMuGenerateSingleMuonTriggerFlags,
        ],
    )
    configuration.add_producers(
        "ee",
        [
            electrons.GoodElectrons,
            electrons.VetoElectrons,
            electrons.VetoSecondElectron,
            electrons.ExtraElectronsVeto,
            electrons.NumberOfGoodElectrons,
            pairselection.ElElPairSelection,
            pairselection.GoodElElPairFilter,
            pairselection.LVEl1,
            pairselection.LVEl2,
            pairselection.LVEl1Uncorrected,
            pairselection.LVEl2Uncorrected,
            pairquantities.ElElPairQuantities,
            genparticles.ElElGenPairQuantities,
            triggers.ElElGenerateSingleElectronTriggerFlags,
            triggers.ElElGenerateDoubleMuonTriggerFlags,
        ],
    )
    configuration.add_producers(
        "mt",
        [
            muons.GoodMuons,
            muons.NumberOfGoodMuons,
            muons.VetoMuons,
            muons.ExtraMuonsVeto,
            taus.TauEnergyCorrection,
            # taus.BaseTaus,
            taus.GoodTaus,
            taus.NumberOfGoodTaus,
            electrons.ExtraElectronsVeto,
            pairselection.MTPairSelection,
            pairselection.GoodMTPairFilter,
            pairselection.LVMu1,
            pairselection.LVTau2,
            pairselection.LVMu1Uncorrected,
            pairselection.LVTau2Uncorrected,
            pairquantities.MTDiTauPairQuantities,
            pairquantities.FastMTTQuantities,
            genparticles.MTGenDiTauPairQuantities,
            scalefactors.MuonIDIso_SF,
            scalefactors.Tau_2_VsJetTauID_lt_SF,
            scalefactors.Tau_2_VsEleTauID_SF,
            scalefactors.Tau_2_VsMuTauID_SF,
            triggers.MTGenerateSingleMuonTriggerFlags,
            triggers.MTGenerateCrossTriggerFlags,
            triggers.GenerateSingleTrailingTauTriggerFlags,
        ],
    )
    configuration.add_producers(
        "et",
        [
            electrons.GoodElectrons,
            taus.TauEnergyCorrection,
            # taus.BaseTaus,
            taus.GoodTaus,
            taus.NumberOfGoodTaus,
            electrons.NumberOfGoodElectrons,
            electrons.VetoElectrons,
            electrons.ExtraElectronsVeto,
            muons.ExtraMuonsVeto,
            pairselection.ETPairSelection,
            pairselection.GoodETPairFilter,
            pairselection.LVEl1,
            pairselection.LVTau2,
            pairselection.LVEl1Uncorrected,
            pairselection.LVTau2Uncorrected,
            pairquantities.ETDiTauPairQuantities,
            genparticles.ETGenDiTauPairQuantities,
            pairquantities.FastMTTQuantities,
            scalefactors.Tau_2_VsJetTauID_lt_SF,
            scalefactors.Tau_2_VsEleTauID_SF,
            scalefactors.Tau_2_VsMuTauID_SF,
            # scalefactors.EleID_SF,
            triggers.ETGenerateSingleElectronTriggerFlags,
            triggers.ETGenerateCrossTriggerFlags,
            triggers.GenerateSingleTrailingTauTriggerFlags,
        ],
    )
    configuration.add_producers(
        "tt",
        [
            electrons.ExtraElectronsVeto,
            muons.ExtraMuonsVeto,
            taus.TauEnergyCorrection,
            # taus.BaseTaus,
            taus.GoodTaus,
            taus.NumberOfGoodTaus,
            pairselection.TTPairSelection,
            pairselection.GoodTTPairFilter,
            pairselection.LVTau1,
            pairselection.LVTau2,
            pairselection.LVTau1Uncorrected,
            pairselection.LVTau2Uncorrected,
            pairquantities.TTDiTauPairQuantities,
            genparticles.TTGenDiTauPairQuantities,
            pairquantities.FastMTTQuantities,
            scalefactors.Tau_1_VsJetTauID_SF,
            scalefactors.Tau_1_VsEleTauID_SF,
            scalefactors.Tau_1_VsMuTauID_SF,
            scalefactors.Tau_2_VsJetTauID_tt_SF,
            scalefactors.Tau_2_VsEleTauID_SF,
            scalefactors.Tau_2_VsMuTauID_SF,
            triggers.TTGenerateDoubleTriggerFlags,
            triggers.GenerateSingleTrailingTauTriggerFlags,
            triggers.GenerateSingleLeadingTauTriggerFlags,
        ],
    )
    configuration.add_producers(
        "em",
        [
            electrons.GoodElectrons,
            electrons.NumberOfGoodElectrons,
            electrons.VetoElectrons,
            electrons.ExtraElectronsVeto,
            muons.GoodMuons,
            muons.NumberOfGoodMuons,
            muons.VetoMuons,
            muons.ExtraMuonsVeto,
            pairselection.EMPairSelection,
            pairselection.GoodEMPairFilter,
            pairselection.LVEl1,
            pairselection.LVMu2,
            pairselection.LVEl1Uncorrected,
            pairselection.LVMu2Uncorrected,
            pairquantities.EMDiTauPairQuantities,
            genparticles.EMGenDiTauPairQuantities,
            pairquantities.FastMTTQuantities,
            scalefactors.MuonIDIso_SF,
            # scalefactors.EleID_SF,
            triggers.EMGenerateSingleElectronTriggerFlags,
            triggers.EMGenerateSingleMuonTriggerFlags,
            triggers.EMGenerateCrossTriggerFlags,
        ],
    )
    configuration.add_modification_rule(
        ["et", "mt"],
        RemoveProducer(
            producers=[
                scalefactors.Tau_2_VsMuTauID_SF,
                scalefactors.Tau_2_VsJetTauID_lt_SF,
                scalefactors.Tau_2_VsEleTauID_SF,
            ],
            samples="data",
        ),
    )

    configuration.add_modification_rule(
        ["tt"],
        RemoveProducer(
            producers=[
                scalefactors.Tau_1_VsJetTauID_SF,
                scalefactors.Tau_1_VsEleTauID_SF,
                scalefactors.Tau_1_VsMuTauID_SF,
                scalefactors.Tau_2_VsJetTauID_tt_SF,
                scalefactors.Tau_2_VsEleTauID_SF,
                scalefactors.Tau_2_VsMuTauID_SF,
            ],
            samples="data",
        ),
    )
    configuration.add_modification_rule(
        scopes,
        RemoveProducer(
            producers=[
                scalefactors.btagging_SF,
            ],
            samples=["data", "embedding", "embedding_mc"],
        ),
    )
    configuration.add_modification_rule(
        ["et", "mt", "tt"],
        ReplaceProducer(
            producers=[taus.TauEnergyCorrection, taus.TauEnergyCorrection_data],
            samples="data",
        ),
    )
    configuration.add_modification_rule(
        "global",
        ReplaceProducer(
            producers=[jets.JetEnergyCorrection, jets.JetEnergyCorrection_data],
            samples="data",
        ),
    )

    # configuration.add_modification_rule(
    #     "global",
    #     RemoveProducer(
    #         producers=[event.npartons],
    #         samples=[
    #             sample
    #             for sample in available_sample_types
    #             if sample not in ["dyjets", "wjets", "electroweak_boson"]
    #         ],
    #     ),
    # )
    configuration.add_modification_rule(
        "global",
        RemoveProducer(
            producers=[event.PUweights],
            samples=["data", "embedding", "embedding_mc"],
        ),
    )
    # for whatever reason, the diboson samples do not have these weights in the ntuple....
    # configuration.add_modification_rule(
    #     "global",
    #     RemoveProducer(
    #         producers=[event.LHE_Scale_weight],
    #         samples=["data", "embedding", "embedding_mc", "diboson"],
    #     ),
    # )
    configuration.add_modification_rule(
        ["et", "mt", "tt"],
        RemoveProducer(
            producers=[
                pairquantities.tau_gen_match_2,
            ],
            samples="data",
        ),
    )
    configuration.add_modification_rule(
        ["tt"],
        RemoveProducer(
            producers=[
                pairquantities.tau_gen_match_1,
            ],
            samples="data",
        ),
    )
    configuration.add_modification_rule(
        scopes,
        RemoveProducer(
            producers=[
                genparticles.GenMatching,
            ],
            samples="data",
        ),
    )
    configuration.add_modification_rule(
        scopes,
        AppendProducer(
            producers=[event.GGH_NNLO_Reweighting, event.GGH_WG1_Uncertainties],
            samples=["ggh_htautau", "rem_htautau"],
        ),
    )
    configuration.add_modification_rule(
        scopes,
        AppendProducer(
            producers=event.QQH_WG1_Uncertainties,
            samples=["vbf_htautau", "rem_htautau"],
        ),
    )
    configuration.add_modification_rule(
        scopes,
        AppendProducer(producers=event.TopPtReweighting, samples="ttbar"),
    )
    configuration.add_modification_rule(
        scopes,
        AppendProducer(
            producers=event.ZPtMassReweighting, samples=["dyjets", "electroweak_boson"]
        ),
    )
    # changes needed for data
    # global scope
    configuration.add_modification_rule(
        "global",
        AppendProducer(
            producers=jets.RenameJetsData,
            samples=["embedding", "embedding_mc"],
            update_output=False,
        ),
    )
    configuration.add_modification_rule(
        "global",
        AppendProducer(producers=event.JSONFilter, samples=["data", "embedding"]),
    )

    # scope specific
    configuration.add_modification_rule(
        "mt",
        RemoveProducer(
            producers=[genparticles.MTGenDiTauPairQuantities],
            samples=["data"],
        ),
    )
    configuration.add_modification_rule(
        "et",
        RemoveProducer(
            producers=[genparticles.ETGenDiTauPairQuantities],
            samples=["data"],
        ),
    )
    configuration.add_modification_rule(
        "tt",
        RemoveProducer(
            producers=[genparticles.TTGenDiTauPairQuantities],
            samples=["data"],
        ),
    )
    configuration.add_modification_rule(
        "em",
        RemoveProducer(
            producers=[genparticles.EMGenDiTauPairQuantities],
            samples=["data"],
        ),
    )
    configuration.add_modification_rule(
        "mm",
        RemoveProducer(
            producers=[genparticles.MuMuGenPairQuantities],
            samples=["data"],
        ),
    )
    configuration.add_modification_rule(
        "ee",
        RemoveProducer(
            producers=[genparticles.ElElGenPairQuantities],
            samples=["data"],
        ),
    )
    # # lepton scalefactors from our measurement
    # configuration.add_modification_rule(
    #     ["mt"],
    #     AppendProducer(
    #         producers=[
    #             scalefactors.TauEmbeddingMuonIDSF_1_MC,
    #             scalefactors.TauEmbeddingMuonIsoSF_1_MC,
    #         ],
    #         samples=[
    #             sample
    #             for sample in available_sample_types
    #             if sample not in ["data", "embedding", "embedding_mc"]
    #         ],
    #     ),
    # )
    # configuration.add_modification_rule(
    #     ["et"],
    #     AppendProducer(
    #         producers=[
    #             scalefactors.TauEmbeddingElectronIDSF_1_MC,
    #             scalefactors.TauEmbeddingElectronIsoSF_1_MC,
    #         ],
    #         samples=[
    #             sample
    #             for sample in available_sample_types
    #             if sample not in ["data", "embedding", "embedding_mc"]
    #         ],
    #     ),
    # )
    # configuration.add_modification_rule(
    #     ["em"],
    #     AppendProducer(
    #         producers=[
    #             scalefactors.TauEmbeddingElectronIDSF_1_MC,
    #             scalefactors.TauEmbeddingElectronIsoSF_1_MC,
    #             scalefactors.TauEmbeddingMuonIDSF_2_MC,
    #             scalefactors.TauEmbeddingMuonIsoSF_2_MC,
    #         ],
    #         samples=[
    #             sample
    #             for sample in available_sample_types
    #             if sample not in ["data", "embedding", "embedding_mc"]
    #         ],
    #     ),
    # )
    # configuration.add_modification_rule(
    #     ["mm"],
    #     AppendProducer(
    #         producers=[
    #             scalefactors.TauEmbeddingMuonIDSF_1_MC,
    #             scalefactors.TauEmbeddingMuonIsoSF_1_MC,
    #             scalefactors.TauEmbeddingMuonIDSF_2_MC,
    #             scalefactors.TauEmbeddingMuonIsoSF_2_MC,
    #             scalefactors.MTGenerateSingleMuonTriggerSF_MC,
    #         ],
    #         samples=[
    #             sample
    #             for sample in available_sample_types
    #             if sample not in ["data", "embedding", "embedding_mc"]
    #         ],
    #     ),
    # )
    # configuration.add_modification_rule(
    #     ["ee"],
    #     AppendProducer(
    #         producers=[
    #             scalefactors.TauEmbeddingElectronIDSF_1_MC,
    #             scalefactors.TauEmbeddingElectronIsoSF_1_MC,
    #             scalefactors.TauEmbeddingElectronIDSF_2_MC,
    #             scalefactors.TauEmbeddingElectronIsoSF_2_MC,
    #             scalefactors.ETGenerateSingleElectronTriggerSF_MC,
    #         ],
    #         samples=[
    #             sample
    #             for sample in available_sample_types
    #             if sample not in ["data", "embedding", "embedding_mc"]
    #         ],
    #     ),
    # )
    configuration.add_modification_rule(
        ["mt"],
        AppendProducer(
            producers=[
                scalefactors.MTGenerateSingleMuonTriggerSF_MC,
            ],
            samples=[
                sample
                for sample in available_sample_types
                if sample not in ["data", "embedding", "embedding_mc"]
            ],
        ),
    )
    configuration.add_modification_rule(
        ["et"],
        AppendProducer(
            producers=[
                scalefactors.ETGenerateSingleElectronTriggerSF_MC,
            ],
            samples=[
                sample
                for sample in available_sample_types
                if sample not in ["data", "embedding", "embedding_mc"]
            ],
        ),
    )

    configuration.add_outputs(
        scopes,
        [
            q.is_data,
            q.is_embedding,
            q.is_ttbar,
            q.is_dyjets,
            q.is_wjets,
            q.is_ggh_htautau,
            q.is_vbf_htautau,
            q.is_diboson,
            nanoAOD.run,
            q.lumi,
            # q.npartons,
            nanoAOD.event,
            q.puweight,
            # q.lhe_scale_weight,
            q.pt_1,
            q.pt_2,
            q.eta_1,
            q.eta_2,
            q.phi_1,
            q.phi_2,
            q.njets,
            q.nprebjets,
            q.jpt_1,
            q.jpt_2,
            q.jeta_1,
            q.jeta_2,
            q.jphi_1,
            q.jphi_2,
            q.jtag_value_1,
            q.jtag_value_2,
            q.mjj,
            q.m_vis,
            q.m_fastmtt,
            q.pt_fastmtt,
            q.eta_fastmtt,
            q.phi_fastmtt,
            q.deltaR_ditaupair,
            q.pt_vis,
            q.nbtag,
            q.bpt_1,
            q.bpt_2,
            q.beta_1,
            q.beta_2,
            q.bphi_1,
            q.bphi_2,
            q.btag_value_1,
            q.btag_value_2,
            q.btag_weight,
            q.mass_1,
            q.mass_2,
            q.dxy_1,
            q.dxy_2,
            q.dz_1,
            q.dz_2,
            q.q_1,
            q.q_2,
            q.iso_1,
            q.iso_2,
            q.gen_pt_1,
            q.gen_eta_1,
            q.gen_phi_1,
            q.gen_mass_1,
            q.gen_pdgid_1,
            q.gen_pt_2,
            q.gen_eta_2,
            q.gen_phi_2,
            q.gen_mass_2,
            q.gen_pdgid_2,
            q.gen_m_vis,
            q.met,
            q.metphi,
            q.pfmet,
            q.pfmetphi,
            q.met_uncorrected,
            q.metphi_uncorrected,
            q.pfmet_uncorrected,
            q.pfmetphi_uncorrected,
            q.metSumEt,
            q.metcov00,
            q.metcov01,
            q.metcov10,
            q.metcov11,
            q.pzetamissvis,
            q.mTdileptonMET,
            q.mt_1,
            q.mt_2,
            q.pt_tt,
            q.pt_ttjj,
            q.mt_tot,
            q.genbosonmass,
            q.gen_match_1,
            q.gen_match_2,
            q.pzetamissvis_pf,
            q.mTdileptonMET_pf,
            q.mt_1_pf,
            q.mt_2_pf,
            q.pt_tt_pf,
            q.pt_ttjj_pf,
            q.mt_tot_pf,
            q.pt_dijet,
            q.jet_hemisphere,
        ],
    )
    # add genWeight for everything but data
    if sample != "data":
        configuration.add_outputs(
            scopes,
            nanoAOD.genWeight,
        )
        if era != "2018" and era != "2022EE" and era != "2022postEE":
            configuration.add_outputs(
                scopes,
                q.prefireweight,
            )
    configuration.add_outputs(
        "mt",
        [
            q.nmuons,
            q.ntaus,
            scalefactors.Tau_2_VsJetTauID_lt_SF.output_group,
            scalefactors.Tau_2_VsEleTauID_SF.output_group,
            scalefactors.Tau_2_VsMuTauID_SF.output_group,
            pairquantities.VsJetTauIDFlag_2.output_group,
            pairquantities.VsEleTauIDFlag_2.output_group,
            pairquantities.VsMuTauIDFlag_2.output_group,
            triggers.MTGenerateSingleMuonTriggerFlags.output_group,
            triggers.MTGenerateCrossTriggerFlags.output_group,
            triggers.GenerateSingleTrailingTauTriggerFlags.output_group,
            q.taujet_pt_2,
            q.gen_taujet_pt_2,
            q.tau_decaymode_1,
            q.tau_decaymode_2,
            q.tau_gen_match_2,
            q.muon_veto_flag,
            q.dimuon_veto,
            q.electron_veto_flag,
            q.id_wgt_mu_1,
            q.iso_wgt_mu_1,
        ],
    )
    configuration.add_outputs(
        "et",
        [
            q.nelectrons,
            q.ntaus,
            scalefactors.Tau_2_VsJetTauID_lt_SF.output_group,
            scalefactors.Tau_2_VsEleTauID_SF.output_group,
            scalefactors.Tau_2_VsMuTauID_SF.output_group,
            pairquantities.VsJetTauIDFlag_2.output_group,
            pairquantities.VsEleTauIDFlag_2.output_group,
            pairquantities.VsMuTauIDFlag_2.output_group,
            triggers.ETGenerateSingleElectronTriggerFlags.output_group,
            triggers.ETGenerateCrossTriggerFlags.output_group,
            triggers.GenerateSingleTrailingTauTriggerFlags.output_group,
            q.taujet_pt_2,
            q.gen_taujet_pt_2,
            q.tau_decaymode_1,
            q.tau_decaymode_2,
            q.tau_gen_match_2,
            q.muon_veto_flag,
            q.dimuon_veto,
            q.electron_veto_flag,
            # q.id_wgt_ele_wp90nonIso_1,
            # q.id_wgt_ele_wp80nonIso_1,
        ],
    )
    configuration.add_outputs(
        "tt",
        [
            q.ntaus,
            scalefactors.Tau_1_VsJetTauID_SF.output_group,
            scalefactors.Tau_1_VsEleTauID_SF.output_group,
            scalefactors.Tau_1_VsMuTauID_SF.output_group,
            scalefactors.Tau_2_VsJetTauID_tt_SF.output_group,
            scalefactors.Tau_2_VsEleTauID_SF.output_group,
            scalefactors.Tau_2_VsMuTauID_SF.output_group,
            pairquantities.VsJetTauIDFlag_1.output_group,
            pairquantities.VsEleTauIDFlag_1.output_group,
            pairquantities.VsMuTauIDFlag_1.output_group,
            pairquantities.VsJetTauIDFlag_2.output_group,
            pairquantities.VsEleTauIDFlag_2.output_group,
            pairquantities.VsMuTauIDFlag_2.output_group,
            triggers.TTGenerateDoubleTriggerFlags.output_group,
            triggers.GenerateSingleTrailingTauTriggerFlags.output_group,
            triggers.GenerateSingleLeadingTauTriggerFlags.output_group,
            q.taujet_pt_1,
            q.taujet_pt_2,
            q.gen_taujet_pt_1,
            q.gen_taujet_pt_2,
            q.tau_decaymode_1,
            q.tau_decaymode_2,
            q.tau_gen_match_1,
            q.tau_gen_match_2,
            q.muon_veto_flag,
            q.dimuon_veto,
            q.electron_veto_flag,
        ],
    )
    configuration.add_outputs(
        "em",
        [
            q.nelectrons,
            q.nmuons,
            triggers.EMGenerateSingleElectronTriggerFlags.output_group,
            triggers.EMGenerateSingleMuonTriggerFlags.output_group,
            triggers.EMGenerateCrossTriggerFlags.output_group,
            q.muon_veto_flag,
            q.dimuon_veto,
            q.electron_veto_flag,
            q.tau_decaymode_1,
            q.tau_decaymode_2,
            q.id_wgt_mu_2,
        ],
    )

    configuration.add_outputs(
        "mm",
        [
            q.nmuons,
            triggers.MuMuGenerateSingleMuonTriggerFlags.output_group,
        ],
    )

    configuration.add_outputs(
        "ee",
        [
            q.nelectrons,
            triggers.ElElGenerateSingleElectronTriggerFlags.output_group,
            triggers.ElElGenerateDoubleMuonTriggerFlags.output_group,
            q.dimuon_veto,
            q.dielectron_veto,
            q.electron_veto_flag,
        ],
    )
    if "data" not in sample and "embedding" not in sample:
        configuration.add_outputs(
            scopes,
            [
                nanoAOD.HTXS_Higgs_pt,
                nanoAOD.HTXS_Higgs_y,
                nanoAOD.HTXS_njets30,
                nanoAOD.HTXS_stage_0,
                nanoAOD.HTXS_stage1_2_cat_pTjet30GeV,
                nanoAOD.HTXS_stage1_2_fine_cat_pTjet30GeV,
            ],
        )
    #########################
    # LHE Scale Weight variations
    # up is muR=2.0, muF=2.0
    # down is muR=0.5, muF=0.5
    #########################
    # if "ggh" in sample or "qqh" in sample:
    #     configuration.add_shift(
    #         SystematicShift(
    #             "LHEScaleWeightUp",
    #             shift_config={
    #                 "global": {
    #                     "muR": 2.0,
    #                     "muF": 2.0,
    #                 }
    #             },
    #             producers={"global": [event.LHE_Scale_weight]},
    #         )
    #     )
    #     configuration.add_shift(
    #         SystematicShift(
    #             "LHEScaleWeightDown",
    #             shift_config={
    #                 "global": {
    #                     "muR": 0.5,
    #                     "muF": 0.5,
    #                 }
    #             },
    #             producers={"global": [event.LHE_Scale_weight]},
    #         )
    #     )

    #########################
    # Lepton to tau fakes energy scalefactor shifts  #
    #########################
    if "dyjets" in sample or "electroweak_boson" in sample:
        configuration.add_shift(
            SystematicShift(
                name="tauMuFakeEsDown",
                shift_config={
                    "mt": {
                        "tau_mufake_es": "down",
                    }
                },
                producers={"mt": [taus.TauPtCorrection_muFake]},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name="tauMuFakeEsUp",
                shift_config={
                    "mt": {
                        "tau_mufake_es": "up",
                    }
                },
                producers={"mt": [taus.TauPtCorrection_muFake]},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEleFakeEs1prongBarrelDown",
                shift_config={
                    "et": {
                        "tau_elefake_es_DM0_barrel": "down",
                    }
                },
                producers={"et": [taus.TauPtCorrection_eleFake]},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEleFakeEs1prongBarrelUp",
                shift_config={
                    "et": {
                        "tau_elefake_es_DM0_barrel": "up",
                    }
                },
                producers={"et": [taus.TauPtCorrection_eleFake]},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEleFakeEs1prongEndcapDown",
                shift_config={
                    "et": {
                        "tau_elefake_es_DM0_endcap": "down",
                    }
                },
                producers={"et": [taus.TauPtCorrection_eleFake]},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEleFakeEs1prongEndcapUp",
                shift_config={
                    "et": {
                        "tau_elefake_es_DM0_endcap": "up",
                    }
                },
                producers={"et": [taus.TauPtCorrection_eleFake]},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEleFakeEs1prong1pizeroBarrelDown",
                shift_config={
                    "et": {
                        "tau_elefake_es_DM1_barrel": "down",
                    }
                },
                producers={"et": [taus.TauPtCorrection_eleFake]},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEleFakeEs1prong1pizeroBarrelUp",
                shift_config={
                    "et": {
                        "tau_elefake_es_DM1_barrel": "up",
                    }
                },
                producers={"et": [taus.TauPtCorrection_eleFake]},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEleFakeEs1prong1pizeroEndcapDown",
                shift_config={
                    "et": {
                        "tau_elefake_es_DM1_endcap": "down",
                    }
                },
                producers={"et": [taus.TauPtCorrection_eleFake]},
            )
        )
        configuration.add_shift(
            SystematicShift(
                name="tauEleFakeEs1prong1pizeroEndcapUp",
                shift_config={
                    "et": {
                        "tau_elefake_es_DM1_endcap": "up",
                    }
                },
                producers={"et": [taus.TauPtCorrection_eleFake]},
            ),
            samples=[
                sample
                for sample in available_sample_types
                if sample not in ["data", "embedding", "embedding_mc"]
            ],
        )

    #########################
    # MET Shifts
    #########################
    configuration.add_shift(
        SystematicShiftByQuantity(
            name="metUnclusteredEnUp",
            quantity_change={
                nanoAOD.MET_pt: "PuppiMET_ptUnclusteredUp",
                nanoAOD.MET_phi: "PuppiMET_phiUnclusteredUp",
            },
            scopes=["global"],
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShiftByQuantity(
            name="metUnclusteredEnDown",
            quantity_change={
                nanoAOD.MET_pt: "PuppiMET_ptUnclusteredDown",
                nanoAOD.MET_phi: "PuppiMET_phiUnclusteredDown",
            },
            scopes=["global"],
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    #########################
    # Prefiring Shifts
    #########################
    if era != "2018" and era != "2022EE" and era != "2022postEE":
        configuration.add_shift(
            SystematicShiftByQuantity(
                name="prefiringDown",
                quantity_change={
                    nanoAOD.prefireWeight: "L1PreFiringWeight_Dn",
                },
                scopes=["global"],
            )
        )
        configuration.add_shift(
            SystematicShiftByQuantity(
                name="prefiringUp",
                quantity_change={
                    nanoAOD.prefireWeight: "L1PreFiringWeight_Up",
                },
                scopes=["global"],
            )
        )
    #########################
    # MET Recoil Shifts
    #########################
    configuration.add_shift(
        SystematicShift(
            name="metRecoilResponseUp",
            shift_config={
                ("et", "mt", "tt", "em", "ee", "mm"): {
                    "apply_recoil_resolution_systematic": False,
                    "apply_recoil_response_systematic": True,
                    "recoil_systematic_shift_up": True,
                    "recoil_systematic_shift_down": False,
                },
            },
            producers={
                ("et", "mt", "tt", "em", "ee", "mm"): met.ApplyRecoilCorrections
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample
            not in [
                "data",
                "embedding",
                "embedding_mc",
            ]  # ToDo: Is this really necessary for all samples?
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="metRecoilResponseDown",
            shift_config={
                ("et", "mt", "tt", "em", "ee", "mm"): {
                    "apply_recoil_resolution_systematic": False,
                    "apply_recoil_response_systematic": True,
                    "recoil_systematic_shift_up": False,
                    "recoil_systematic_shift_down": True,
                },
            },
            producers={
                ("et", "mt", "tt", "em", "ee", "mm"): met.ApplyRecoilCorrections
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="metRecoilResolutionUp",
            shift_config={
                ("et", "mt", "tt", "em", "ee", "mm"): {
                    "apply_recoil_resolution_systematic": True,
                    "apply_recoil_response_systematic": False,
                    "recoil_systematic_shift_up": True,
                    "recoil_systematic_shift_down": False,
                },
            },
            producers={
                ("et", "mt", "tt", "em", "ee", "mm"): met.ApplyRecoilCorrections
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="metRecoilResolutionDown",
            shift_config={
                ("et", "mt", "tt", "em", "ee", "mm"): {
                    "apply_recoil_resolution_systematic": True,
                    "apply_recoil_response_systematic": False,
                    "recoil_systematic_shift_up": False,
                    "recoil_systematic_shift_down": True,
                },
            },
            producers={
                ("et", "mt", "tt", "em", "ee", "mm"): met.ApplyRecoilCorrections
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    #########################
    # Pileup Shifts
    #########################
    configuration.add_shift(
        SystematicShift(
            name="PileUpUp",
            scopes=["global"],
            shift_config={
                ("global"): {"PU_reweighting_variation": "up"},
            },
            producers={
                "global": [
                    event.PUweights,
                ],
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="PileUpDown",
            scopes=["global"],
            shift_config={
                ("global"): {"PU_reweighting_variation": "down"},
            },
            producers={
                "global": [
                    event.PUweights,
                ],
            },
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )

    #########################
    # Trigger shifts
    #########################
    configuration.add_shift(
        SystematicShift(
            name="singleElectronTriggerSFUp",
            shift_config={
                ("et"): {
                    "singlelectron_trigger_sf_mc": EraModifier(
                        {   ## TODO: update to 2022 recommendation when available. These lines only for testing
                             "2022EE": [
                                {
                                    "flagname": "trg_wgt_single_ele32orele35",
                                    "mc_trigger_sf": "Trg32_or_Trg35_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele32",
                                    "mc_trigger_sf": "Trg32_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele35",
                                    "mc_trigger_sf": "Trg35_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele27orele32orele35",
                                    "mc_trigger_sf": "Trg_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 1.02,
                                },
                            ],
                             "2022postEE": [
                                {
                                    "flagname": "trg_wgt_single_ele32orele35",
                                    "mc_trigger_sf": "Trg32_or_Trg35_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele32",
                                    "mc_trigger_sf": "Trg32_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele35",
                                    "mc_trigger_sf": "Trg35_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele27orele32orele35",
                                    "mc_trigger_sf": "Trg_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 1.02,
                                },
                            ],
                            "2018": [
                                {
                                    "flagname": "trg_wgt_single_ele32orele35",
                                    "mc_trigger_sf": "Trg32_or_Trg35_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele32",
                                    "mc_trigger_sf": "Trg32_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele35",
                                    "mc_trigger_sf": "Trg35_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele27orele32orele35",
                                    "mc_trigger_sf": "Trg_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 1.02,
                                },
                            ],
                            "2017": [
                                {
                                    "flagname": "trg_wgt_single_ele32orele35",
                                    "mc_trigger_sf": "Trg32_or_Trg35_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele32",
                                    "mc_trigger_sf": "Trg32_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele35",
                                    "mc_trigger_sf": "Trg35_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele27orele32orele35",
                                    "mc_trigger_sf": "Trg_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 1.02,
                                },
                            ],
                            "2016postVFP": [
                                {
                                    "flagname": "trg_wgt_single_ele25",
                                    "mc_trigger_sf": "Trg25_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 1.02,
                                }
                            ],
                            "2016preVFP": [
                                {
                                    "flagname": "trg_wgt_single_ele25",
                                    "mc_trigger_sf": "Trg25_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 1.02,
                                }
                            ],
                        }
                    )
                }
            },
            producers={("et"): scalefactors.ETGenerateSingleElectronTriggerSF_MC},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="singleElectronTriggerSFDown",
            shift_config={
                ("et"): {
                    "singlelectron_trigger_sf_mc": EraModifier(
                        {   ## TODO: update to 2022 recommendation when available. These lines only for testing
                            "2022EE": [
                                {
                                    "flagname": "trg_wgt_single_ele32orele35",
                                    "mc_trigger_sf": "Trg32_or_Trg35_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele32",
                                    "mc_trigger_sf": "Trg32_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele35",
                                    "mc_trigger_sf": "Trg35_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele27orele32orele35",
                                    "mc_trigger_sf": "Trg_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 0.98,
                                },
                            ],
                            "2022postEE": [
                                {
                                    "flagname": "trg_wgt_single_ele32orele35",
                                    "mc_trigger_sf": "Trg32_or_Trg35_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele32",
                                    "mc_trigger_sf": "Trg32_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele35",
                                    "mc_trigger_sf": "Trg35_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele27orele32orele35",
                                    "mc_trigger_sf": "Trg_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 0.98,
                                },
                            ],
                            "2018": [
                                {
                                    "flagname": "trg_wgt_single_ele32orele35",
                                    "mc_trigger_sf": "Trg32_or_Trg35_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele32",
                                    "mc_trigger_sf": "Trg32_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele35",
                                    "mc_trigger_sf": "Trg35_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele27orele32orele35",
                                    "mc_trigger_sf": "Trg_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 0.98,
                                },
                            ],
                            "2017": [
                                {
                                    "flagname": "trg_wgt_single_ele32orele35",
                                    "mc_trigger_sf": "Trg32_or_Trg35_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele32",
                                    "mc_trigger_sf": "Trg32_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele35",
                                    "mc_trigger_sf": "Trg35_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_ele27orele32orele35",
                                    "mc_trigger_sf": "Trg_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 0.98,
                                },
                            ],
                            "2016postVFP": [
                                {
                                    "flagname": "trg_wgt_single_ele25",
                                    "mc_trigger_sf": "Trg25_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 0.98,
                                }
                            ],
                            "2016preVFP": [
                                {
                                    "flagname": "trg_wgt_single_ele25",
                                    "mc_trigger_sf": "Trg25_Iso_pt_eta_bins",
                                    "mc_electron_trg_extrapolation": 0.98,
                                }
                            ],
                        }
                    )
                }
            },
            producers={("et"): scalefactors.ETGenerateSingleElectronTriggerSF_MC},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="singleMuonTriggerSFUp",
            shift_config={
                ("mt"): {
                    "singlemuon_trigger_sf_mc": EraModifier(
                        {   ## TODO: update to 2022 recommendation when available. These lines only for testing
                             "2022EE": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu24ormu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                            ],
                             "2022postEE": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu24ormu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                            ],
                            "2018": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu24ormu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                            ],
                            "2017": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu24ormu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                            ],
                            "2016postVFP": [
                                {
                                    "flagname": "trg_wgt_single_mu22",
                                    "mc_trigger_sf": "Trg_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                            ],
                            "2016preVFP": [
                                {
                                    "flagname": "trg_wgt_single_mu22",
                                    "mc_trigger_sf": "Trg_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 1.02,
                                },
                            ],
                        }
                    )
                }
            },
            producers={("mt"): scalefactors.MTGenerateSingleMuonTriggerSF_MC},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="singleMuonTriggerSFDown",
            shift_config={
                ("mt"): {
                    "singlemuon_trigger_sf_mc": EraModifier(
                        {   ## TODO: update to 2022 recommendation when available. These lines only for testing
                            "2022EE": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu24ormu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                            ],
                            "2022postEE": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu24ormu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                            ],
                            "2018": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu24ormu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                            ],
                            "2017": [
                                {
                                    "flagname": "trg_wgt_single_mu24",
                                    "mc_trigger_sf": "Trg_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                                {
                                    "flagname": "trg_wgt_single_mu24ormu27",
                                    "mc_trigger_sf": "Trg_IsoMu27_or_IsoMu24_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                            ],
                            "2016postVFP": [
                                {
                                    "flagname": "trg_wgt_single_mu22",
                                    "mc_trigger_sf": "Trg_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                            ],
                            "2016preVFP": [
                                {
                                    "flagname": "trg_wgt_single_mu22",
                                    "mc_trigger_sf": "Trg_pt_eta_bins",
                                    "mc_muon_trg_extrapolation": 0.98,
                                },
                            ],
                        }
                    )
                }
            },
            producers={("mt"): scalefactors.MTGenerateSingleMuonTriggerSF_MC},
        ),
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )
    ## Muon id, iso shifts
    configuration.add_shift(
            SystematicShift(
                name="muon_IDISO_syst",
                shift_config={
                    ("mt", "em", "mm"): {
                        "muon_sf_varation": "syst",
                    }
                },
                producers={("mt", "em", "mm"): [scalefactors.MuonIDIso_SF]},
            )
        )
    configuration.add_shift(
            SystematicShift(
                name="muon_IDISO_stat",
                shift_config={
                    ("mt", "em", "mm"): {
                        "muon_sf_varation": "stat",
                    }
                },
                producers={("mt", "em", "mm"): [scalefactors.MuonIDIso_SF]},
            )
        )
    configuration.add_shift(
            SystematicShift(
                name="muon_IDISO_tagIso",
                shift_config={
                    ("mt", "em", "mm"): {
                        "muon_sf_varation": "tagIso",
                    }
                },
                producers={("mt", "em", "mm"): [scalefactors.MuonIDIso_SF]},
            )
        )
    #########################
    # TauID scale factor shifts, channel dependent # Tau energy scale shifts, dm dependent
    #########################
    add_tauVariations(configuration, sample)
    #########################
    # Import triggersetup   #
    #########################
    add_diTauTriggerSetup(configuration)
    #########################
    # Add additional producers and SFs related to embedded samples
    #########################
    if sample == "embedding" or sample == "embedding_mc":
        setup_embedding(configuration, scopes)

    #########################
    # Jet energy resolution and jet energy scale
    #########################
    add_jetVariations(configuration, available_sample_types, era)

    #########################
    # btagging scale factor shape variation
    #########################
    add_btagVariations(configuration, available_sample_types)

    #########################
    # Jet energy correction for data
    #########################
    add_jetCorrectionData(configuration, era)

    #########################
    # Finalize and validate the configuration
    #########################
    configuration.optimize()
    configuration.validate()
    configuration.report()
    return configuration.expanded_configuration()

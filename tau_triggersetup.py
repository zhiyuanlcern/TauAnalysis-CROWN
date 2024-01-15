from code_generation.configuration import Configuration
from code_generation.modifiers import EraModifier, SampleModifier


def add_diTauTriggerSetup(configuration: Configuration):
    ## MT, MM scope trigger setup
    configuration.add_config_parameters(
        ["mt", "mm", "em"],
        {
            "singlemoun_trigger": EraModifier(
                {   ## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022EE": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu27",
                            "hlt_path": "HLT_IsoMu27",
                            "ptcut": 28,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2022postEE": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu27",
                            "hlt_path": "HLT_IsoMu27",
                            "ptcut": 28,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2018": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu27",
                            "hlt_path": "HLT_IsoMu27",
                            "ptcut": 28,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2017": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu27",
                            "hlt_path": "HLT_IsoMu27",
                            "ptcut": 28,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_single_mu22",
                            "hlt_path": "HLT_IsoMu22",
                            "ptcut": 23,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu22_tk",
                            "hlt_path": "HLT_IsoTkMu22",
                            "ptcut": 23,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu22_eta2p1",
                            "hlt_path": "HLT_IsoMu22_eta2p1",
                            "ptcut": 23,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu22_tk_eta2p1",
                            "hlt_path": "HLT_IsoTkMu22_eta2p1",
                            "ptcut": 23,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_single_mu22",
                            "hlt_path": "HLT_IsoMu22",
                            "ptcut": 23,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu22_tk",
                            "hlt_path": "HLT_IsoTkMu22",
                            "ptcut": 23,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu22_eta2p1",
                            "hlt_path": "HLT_IsoMu22_eta2p1",
                            "ptcut": 23,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu22_tk_eta2p1",
                            "hlt_path": "HLT_IsoTkMu22_eta2p1",
                            "ptcut": 23,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
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
            "mutau_cross_trigger": EraModifier(
                {   ## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022EE": [
                        {
                            "flagname": "trg_cross_mu20tau27_hps",
                            "hlt_path": "HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1",
                            "p1_ptcut": 21,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 3,
                            "p1_trigger_particle_id": 13,
                            "p2_ptcut": 32,
                            "p2_etacut": 2.1,
                            "p2_filterbit": -1,  # TODO switch to "p2_filterbit": 4, if the bits are correct
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },                        
                    ],
                    "2022postEE": [
                        {
                            "flagname": "trg_cross_mu20tau27_hps",
                            "hlt_path": "HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1",
                            "p1_ptcut": 21,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 3,
                            "p1_trigger_particle_id": 13,
                            "p2_ptcut": 32,
                            "p2_etacut": 2.1,
                            "p2_filterbit": -1,  # TODO switch to "p2_filterbit": 4, if the bits are correct
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },                        
                    ],
                    "2018": [
                        {
                            "flagname": "trg_cross_mu20tau27_hps",
                            "hlt_path": "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_CrossL1",
                            "p1_ptcut": 21,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 3,
                            "p1_trigger_particle_id": 13,
                            "p2_ptcut": 32,
                            "p2_etacut": 2.1,
                            "p2_filterbit": -1,  # TODO switch to "p2_filterbit": 4, if the bits are correct
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # the non HPS version exists for data only, but add it anyway to have the flag in the ntuple
                        {
                            "flagname": "trg_cross_mu20tau27",
                            "hlt_path": "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
                            "p1_ptcut": 21,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 3,
                            "p1_trigger_particle_id": 13,
                            "p2_ptcut": 32,
                            "p2_etacut": 2.1,
                            "p2_filterbit": -1,  # TODO switch to "p2_filterbit": 4, if the bits are correct
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
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
                    "2016postVFP": [
                        {
                            "flagname": "trg_cross_mu19tau20",
                            "hlt_path": "HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1",
                            "p1_ptcut": 20,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 3,
                            "p1_trigger_particle_id": 13,
                            "p2_ptcut": 22,
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
                            "p2_ptcut": 22,
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
    ## ET, EE scope trigger setup
    configuration.add_config_parameters(
        ["et", "ee", "em"],
        {
            "singleelectron_trigger": EraModifier(
                {   
                    "2022EE": [
                        {
                            "flagname": "trg_single_ele30",
                            "hlt_path": "HLT_Ele30_WPTight_Gsf",
                            "ptcut": 31,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_ele32",
                            "hlt_path": "HLT_Ele32_WPTight_Gsf",
                            "ptcut": 33,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_ele35",
                            "hlt_path": "HLT_Ele35_WPTight_Gsf",
                            "ptcut": 36,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2022postEE": [
                        {
                            "flagname": "trg_single_ele30",
                            "hlt_path": "HLT_Ele30_WPTight_Gsf",
                            "ptcut": 31,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_ele32",
                            "hlt_path": "HLT_Ele32_WPTight_Gsf",
                            "ptcut": 33,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_ele35",
                            "hlt_path": "HLT_Ele35_WPTight_Gsf",
                            "ptcut": 36,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2018": [
                        {
                            "flagname": "trg_single_ele27",
                            "hlt_path": "HLT_Ele27_WPTight_Gsf",
                            "ptcut": 28,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_ele32",
                            "hlt_path": "HLT_Ele32_WPTight_Gsf",
                            "ptcut": 33,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_ele35",
                            "hlt_path": "HLT_Ele35_WPTight_Gsf",
                            "ptcut": 36,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2017": [
                        {
                            "flagname": "trg_single_ele27",
                            "hlt_path": "HLT_Ele27_WPTight_Gsf",
                            "ptcut": 28,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_ele32",
                            "hlt_path": "HLT_Ele32_WPTight_Gsf",
                            "ptcut": 33,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_ele35",
                            "hlt_path": "HLT_Ele35_WPTight_Gsf",
                            "ptcut": 36,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_single_ele25",
                            "hlt_path": "HLT_Ele25_eta2p1_WPTight_Gsf",
                            "ptcut": 26,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_single_ele25",
                            "hlt_path": "HLT_Ele25_eta2p1_WPTight_Gsf",
                            "ptcut": 26,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                }
            ),
        },
    )
    # ET scope crosstrigger
    configuration.add_config_parameters(
        ["et"],
        {
            "eltau_cross_trigger": EraModifier(
                {   ## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022EE": [
                        {
                            "flagname": "trg_cross_ele24tau30_hps",
                            "hlt_path": "HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1",
                            "p1_ptcut": 25,
                            "p2_ptcut": 32,
                            "p1_etacut": 2.5,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 1,
                            "p1_trigger_particle_id": 11,
                            "p2_filterbit": -1,  # TODO switch to "p2_filterbit": 4, if the bits are correct
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # the non HPS version exists for data only, but add it anyway to have the flag in the ntuple
                    ],
                    "2022postEE": [
                        {
                            "flagname": "trg_cross_ele24tau30_hps",
                            "hlt_path": "HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1",
                            "p1_ptcut": 25,
                            "p2_ptcut": 32,
                            "p1_etacut": 2.5,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 1,
                            "p1_trigger_particle_id": 11,
                            "p2_filterbit": -1,  # TODO switch to "p2_filterbit": 4, if the bits are correct
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # the non HPS version exists for data only, but add it anyway to have the flag in the ntuple
                    ],
                    "2018": [
                        {
                            "flagname": "trg_cross_ele24tau30_hps",
                            "hlt_path": "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1",
                            "p1_ptcut": 25,
                            "p2_ptcut": 32,
                            "p1_etacut": 2.5,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 1,
                            "p1_trigger_particle_id": 11,
                            "p2_filterbit": -1,  # TODO switch to "p2_filterbit": 4, if the bits are correct
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # the non HPS version exists for data only, but add it anyway to have the flag in the ntuple
                        {
                            "flagname": "trg_cross_ele24tau30",
                            "hlt_path": "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
                            "p1_ptcut": 25,
                            "p2_ptcut": 32,
                            "p1_etacut": 2.5,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 1,
                            "p1_trigger_particle_id": 11,
                            "p2_filterbit": 4,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2017": [
                        {
                            "flagname": "trg_cross_ele24tau30",
                            "hlt_path": "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
                            "p1_ptcut": 25,
                            "p2_ptcut": 35,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 1,
                            "p1_trigger_particle_id": 11,
                            "p2_filterbit": 4,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_cross_ele24tau20",
                            "hlt_path": "HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1",
                            "p1_ptcut": 25,
                            "p2_ptcut": 25,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 1,
                            "p1_trigger_particle_id": 11,
                            "p2_filterbit": 4,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_cross_ele24tau20_crossL1",
                            "hlt_path": "HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20",
                            "p1_ptcut": 25,
                            "p2_ptcut": 25,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 1,
                            "p1_trigger_particle_id": 11,
                            "p2_filterbit": 4,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_cross_ele24tau30",
                            "hlt_path": "HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30",
                            "p1_ptcut": 25,
                            "p2_ptcut": 35,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 1,
                            "p1_trigger_particle_id": 11,
                            "p2_filterbit": 4,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_cross_ele24tau20",
                            "hlt_path": "HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1",
                            "p1_ptcut": 25,
                            "p2_ptcut": 32,
                            "p1_etacut": 2.5,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 1,
                            "p1_trigger_particle_id": 11,
                            "p2_filterbit": 4,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_cross_ele24tau20_crossL1",
                            "hlt_path": "HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20",
                            "p1_ptcut": 25,
                            "p2_ptcut": 25,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 1,
                            "p1_trigger_particle_id": 11,
                            "p2_filterbit": 4,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_cross_ele24tau30",
                            "hlt_path": "HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30",
                            "p1_ptcut": 25,
                            "p2_ptcut": 35,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 1,
                            "p1_trigger_particle_id": 11,
                            "p2_filterbit": 4,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                }
            ),
        },
    )

    ## TT scope trigger setup
    configuration.add_config_parameters(
        ["tt"],
        {
            "doubletau_trigger": EraModifier(
                {    ## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022EE": [
                        {
                            "flagname": "trg_double_tau35_mediumiso_hps",
                            "hlt_path": "HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": -1,  # TODO switch to "p1_filterbit": 6, if the bits are correct
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": -1,  # TODO switch to "p2_filterbit": 6, if the bits are correct
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # the non HPS version exists for data only, but add it anyway to have the flag in the ntuple
                        {
                            "flagname": "trg_double_tau40_tightiso",
                            "hlt_path": "HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": -1,  # TODO switch to "p1_filterbit": 6, if the bits are correct
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": -1,  # TODO switch to "p2_filterbit": 6, if the bits are correct
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_double_tau40_mediumiso_tightid",
                            "hlt_path": "HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": -1,  # TODO switch to "p1_filterbit": 6, if the bits are correct
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": -1,  # TODO switch to "p2_filterbit": 6, if the bits are correct
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2022postEE": [
                        {
                            "flagname": "trg_double_tau35_mediumiso_hps",
                            "hlt_path": "HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": -1,  # TODO switch to "p1_filterbit": 6, if the bits are correct
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": -1,  # TODO switch to "p2_filterbit": 6, if the bits are correct
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # the non HPS version exists for data only, but add it anyway to have the flag in the ntuple
                        {
                            "flagname": "trg_double_tau40_tightiso",
                            "hlt_path": "HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": -1,  # TODO switch to "p1_filterbit": 6, if the bits are correct
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": -1,  # TODO switch to "p2_filterbit": 6, if the bits are correct
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_double_tau40_mediumiso_tightid",
                            "hlt_path": "HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": -1,  # TODO switch to "p1_filterbit": 6, if the bits are correct
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": -1,  # TODO switch to "p2_filterbit": 6, if the bits are correct
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2018": [
                        {
                            "flagname": "trg_double_tau35_mediumiso_hps",
                            "hlt_path": "HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": -1,  # TODO switch to "p1_filterbit": 6, if the bits are correct
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": -1,  # TODO switch to "p2_filterbit": 6, if the bits are correct
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # the non HPS version exists for data only, but add it anyway to have the flag in the ntuple
                        {
                            "flagname": "trg_double_tau40_tightiso",
                            "hlt_path": "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": -1,  # TODO switch to "p1_filterbit": 6, if the bits are correct
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": -1,  # TODO switch to "p2_filterbit": 6, if the bits are correct
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
                            "p1_filterbit": -1,  # TODO switch to "p1_filterbit": 6, if the bits are correct
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": -1,  # TODO switch to "p2_filterbit": 6, if the bits are correct
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
                }
            ),
        },
    )
    # EM scope trigger setup
    configuration.add_config_parameters(
        ["em"],
        {
            "elmu_cross_trigger": EraModifier(
                {   
                    "2022EE": [
                        {
                            "flagname": "trg_cross_mu23ele12",
                            "hlt_path": "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",
                            "p1_ptcut": 12,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 5,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 24,
                            "p2_etacut": 2.5,
                            "p2_filterbit": 5,
                            "p2_trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_cross_mu8ele23",
                            "hlt_path": "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",
                            "p1_ptcut": 24,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 5,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 8,
                            "p2_etacut": 2.5,
                            "p2_filterbit": 5,
                            "p2_trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2022postEE": [
                        {
                            "flagname": "trg_cross_mu23ele12",
                            "hlt_path": "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",
                            "p1_ptcut": 12,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 5,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 24,
                            "p2_etacut": 2.5,
                            "p2_filterbit": 5,
                            "p2_trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_cross_mu8ele23",
                            "hlt_path": "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",
                            "p1_ptcut": 24,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 5,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 8,
                            "p2_etacut": 2.5,
                            "p2_filterbit": 5,
                            "p2_trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2018": [
                        {
                            "flagname": "trg_cross_mu23ele12",
                            "hlt_path": "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",
                            "p1_ptcut": 12,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 5,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 24,
                            "p2_etacut": 2.5,
                            "p2_filterbit": 5,
                            "p2_trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_cross_mu8ele23",
                            "hlt_path": "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",
                            "p1_ptcut": 24,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 5,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 8,
                            "p2_etacut": 2.5,
                            "p2_filterbit": 5,
                            "p2_trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2017": [
                        {
                            "flagname": "trg_cross_mu23ele12",
                            "hlt_path": "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",
                            "p1_ptcut": 12,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 5,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 24,
                            "p2_etacut": 2.5,
                            "p2_filterbit": 5,
                            "p2_trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_cross_mu8ele23",
                            "hlt_path": "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",
                            "p1_ptcut": 24,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 5,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 8,
                            "p2_etacut": 2.5,
                            "p2_filterbit": 5,
                            "p2_trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_cross_mu23ele12_dz",
                            "hlt_path": "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",
                            "p1_ptcut": 13,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 5,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 24,
                            "p2_etacut": 2.5,
                            "p2_filterbit": 5,
                            "p2_trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_cross_mu8ele23_dz",
                            "hlt_path": "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",
                            "p1_ptcut": 24,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 5,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 9,
                            "p2_etacut": 2.5,
                            "p2_filterbit": 5,
                            "p2_trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_cross_mu23ele12",
                            "hlt_path": "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL",
                            "p1_ptcut": 13,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 5,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 24,
                            "p2_etacut": 2.5,
                            "p2_filterbit": 5,
                            "p2_trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_cross_mu8ele23",
                            "hlt_path": "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL",
                            "p1_ptcut": 24,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 5,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 9,
                            "p2_etacut": 2.5,
                            "p2_filterbit": 5,
                            "p2_trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_cross_mu23ele12_dz",
                            "hlt_path": "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",
                            "p1_ptcut": 13,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 5,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 24,
                            "p2_etacut": 2.5,
                            "p2_filterbit": 5,
                            "p2_trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_cross_mu8ele23_dz",
                            "hlt_path": "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",
                            "p1_ptcut": 24,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 5,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 9,
                            "p2_etacut": 2.5,
                            "p2_filterbit": 5,
                            "p2_trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_cross_mu23ele12",
                            "hlt_path": "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL",
                            "p1_ptcut": 13,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 5,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 24,
                            "p2_etacut": 2.5,
                            "p2_filterbit": 5,
                            "p2_trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_cross_mu8ele23",
                            "hlt_path": "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL",
                            "p1_ptcut": 24,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 5,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 9,
                            "p2_etacut": 2.5,
                            "p2_filterbit": 5,
                            "p2_trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                }
            ),
        },
    )

    ## TT singletau trigger
    configuration.add_config_parameters(
        ["tt"],
        {
            "singletau_trigger_leading": EraModifier(
                {   ## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022EE": [
                        {
                            "flagname": "trg_single_tau180_1",
                            "hlt_path": "HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_deeptau180_1",
                            "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        }
                        
                    ],
                    "2022postEE": [
                        {
                            "flagname": "trg_single_tau180_1",
                            "hlt_path": "HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_deeptau180_1",
                            "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        }
                    ],
                    "2018": [
                        {
                            "flagname": "trg_single_tau180_1",
                            "hlt_path": "HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        }
                    ],
                    "2017": [
                        {
                            "flagname": "trg_single_tau180_1",
                            "hlt_path": "HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        }
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_single_tau120_1",
                            "hlt_path": "HLT_VLooseIsoPFTau120_Trk50_eta2p1",
                            "ptcut": 120,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_tau140_1",
                            "hlt_path": "HLT_VLooseIsoPFTau140_Trk50_eta2p1",
                            "ptcut": 140,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_single_tau120_1",
                            "hlt_path": "HLT_VLooseIsoPFTau120_Trk50_eta2p1",
                            "ptcut": 120,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_tau140_1",
                            "hlt_path": "HLT_VLooseIsoPFTau140_Trk50_eta2p1",
                            "ptcut": 140,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                }
            )
        },
    )

    ## trailing singletau trigger
    configuration.add_config_parameters(
        ["et", "mt", "tt"],
        {
            "singletau_trigger_trailing": EraModifier(
                {   ## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022EE": [
                        {
                            "flagname": "trg_single_tau180_2",
                            "hlt_path": "HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_deeptau180_2",
                            "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        }
                    ],
                    "2022postEE": [
                        {
                            "flagname": "trg_single_tau180_2",
                            "hlt_path": "HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_deeptau180_2",
                            "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        }
                    ],
                    "2018": [
                        {
                            "flagname": "trg_single_tau180_2",
                            "hlt_path": "HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        }
                    ],
                    "2017": [
                        {
                            "flagname": "trg_single_tau180_2",
                            "hlt_path": "HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        }
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_single_tau120_2",
                            "hlt_path": "HLT_VLooseIsoPFTau120_Trk50_eta2p1",
                            "ptcut": 120,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_tau140_2",
                            "hlt_path": "HLT_VLooseIsoPFTau140_Trk50_eta2p1",
                            "ptcut": 140,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_single_tau120_2",
                            "hlt_path": "HLT_VLooseIsoPFTau120_Trk50_eta2p1",
                            "ptcut": 120,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_tau140_2",
                            "hlt_path": "HLT_VLooseIsoPFTau140_Trk50_eta2p1",
                            "ptcut": 140,
                            "etacut": 2.1,
                            "filterbit": 5,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                }
            )
        },
    )

    ### doubleelectron trigger
    configuration.add_config_parameters(
        ["ee"],
        {
            "doubleelectron_trigger": EraModifier(
                {   ## TODO: update to 2022 recommendation when available. These lines only for testing
                    "2022EE": [
                        {
                            "flagname": "trg_double_ele24",
                            "hlt_path": "HLT_DoubleEle24_eta2p1_WPTight_Gsf",
                            "p1_ptcut": 24,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 4,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 24,
                            "p2_etacut": 2.1,
                            "p2_filterbit": 4,
                            "p2_trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        }
                    ],
                    "2022postEE": [
                        {
                            "flagname": "trg_double_ele24",
                            "hlt_path": "HLT_DoubleEle24_eta2p1_WPTight_Gsf",
                            "p1_ptcut": 24,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 4,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 24,
                            "p2_etacut": 2.1,
                            "p2_filterbit": 4,
                            "p2_trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        }
                    ],
                    "2018": [
                        {
                            "flagname": "trg_double_ele24",
                            "hlt_path": "HLT_DoubleEle24_eta2p1_WPTight_Gsf",
                            "p1_ptcut": 24,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 4,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 24,
                            "p2_etacut": 2.1,
                            "p2_filterbit": 4,
                            "p2_trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        }
                    ],
                    "2017": [
                        {
                            "flagname": "trg_double_ele24",
                            "hlt_path": "HLT_DoubleEle24_eta2p1_WPTight_Gsf",
                            "p1_ptcut": 24,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 4,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 24,
                            "p2_etacut": 2.1,
                            "p2_filterbit": 4,
                            "p2_trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        }
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_double_ele24",
                            "hlt_path": "HLT_DoubleEle24_eta2p1_WPTight_Gsf",
                            "p1_ptcut": 24,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 4,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 24,
                            "p2_etacut": 2.1,
                            "p2_filterbit": 4,
                            "p2_trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        }
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_double_ele24",
                            "hlt_path": "HLT_DoubleEle24_eta2p1_WPTight_Gsf",
                            "p1_ptcut": 24,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 4,
                            "p1_trigger_particle_id": 11,
                            "p2_ptcut": 24,
                            "p2_etacut": 2.1,
                            "p2_filterbit": 4,
                            "p2_trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        }
                    ],
                }
            )
        },
    )

    return configuration

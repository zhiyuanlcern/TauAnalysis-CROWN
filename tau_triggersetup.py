from code_generation.configuration import Configuration
from code_generation.modifiers import EraModifier, SampleModifier


def add_diTauTriggerSetup(configuration: Configuration):
    ## MT, MM scope trigger setup
    configuration.add_config_parameters(
        ["mt", "em"],
        {
            "singlemoun_trigger": EraModifier(
                {   ##  V12: 0 => TrkIsoVVL, 1 => Iso, 2 => OverlapFilter PFTau, 3 => 1mu, 4 => 2mu, 5 => 1mu-1e, 6 => 1mu-1tau, 7 => 3mu, 8 => 2mu-1e, 9 => 1mu-2e, 10 => 1mu (Mu50), 11 => 1mu (Mu100), 12 => 1mu-1photon for Muon;
                    ##  V14: 0 => TrkIsoVVL, 1 => Iso, 2 => OverlapFilter PFTau, 3 => 1mu, 4 => 2mu, 5 => 1mu-1e, 6 => 1mu-1tau, 7 => 3mu, 8 => 2mu-1e, 9 => 1mu-2e, 10 => 1mu (Mu50), 11 => 1mu (Mu100), 12 => 1mu-1photon, 13 => 1mu-1tau PNet for Muon;
                    "2023": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # {
                        #     "flagname": "trg_single_mu27",
                        #     "hlt_path": "HLT_IsoMu27",
                        #     "ptcut": 28,
                        #     "etacut": 2.5,
                        #     "filterbit": 3,
                        #     "trigger_particle_id": 13,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
                    ],
                    "2023BPix": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # {
                        #     "flagname": "trg_single_mu27",
                        #     "hlt_path": "HLT_IsoMu27",
                        #     "ptcut": 28,
                        #     "etacut": 2.5,
                        #     "filterbit": 3,
                        #     "trigger_particle_id": 13,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
                    ],
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
                        # {
                        #     "flagname": "trg_single_mu27",
                        #     "hlt_path": "HLT_IsoMu27",
                        #     "ptcut": 28,
                        #     "etacut": 2.5,
                        #     "filterbit": 3,
                        #     "trigger_particle_id": 13,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
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
                        # {
                        #     "flagname": "trg_single_mu27",
                        #     "hlt_path": "HLT_IsoMu27",
                        #     "ptcut": 28,
                        #     "etacut": 2.5,
                        #     "filterbit": 3,
                        #     "trigger_particle_id": 13,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
                    ],
                    
                }
            ),
        },
    )
    configuration.add_config_parameters(
        ["mm"],
        {
            "singlemoun_trigger": EraModifier(
                {   ##  V12: 0 => TrkIsoVVL, 1 => Iso, 2 => OverlapFilter PFTau, 3 => 1mu, 4 => 2mu, 5 => 1mu-1e, 6 => 1mu-1tau, 7 => 3mu, 8 => 2mu-1e, 9 => 1mu-2e, 10 => 1mu (Mu50), 11 => 1mu (Mu100), 12 => 1mu-1photon for Muon;
                    ##  V14: 0 => TrkIsoVVL, 1 => Iso, 2 => OverlapFilter PFTau, 3 => 1mu, 4 => 2mu, 5 => 1mu-1e, 6 => 1mu-1tau, 7 => 3mu, 8 => 2mu-1e, 9 => 1mu-2e, 10 => 1mu (Mu50), 11 => 1mu (Mu100), 12 => 1mu-1photon, 13 => 1mu-1tau PNet for Muon;
                    "2023": [
                        {
                            "flagname": "trg_single_mu24_filterbit4",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 4,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu24_filterbit3",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2023BPix": [
                        {
                            "flagname": "trg_single_mu24_filterbit4",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 4,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu24_filterbit3",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2022EE": [
                        {
                            "flagname": "trg_single_mu24_filterbit4",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 4,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu24_filterbit3",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2022postEE": [
                        {
                            "flagname": "trg_single_mu24_filterbit4",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 4,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_single_mu24_filterbit3",
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
                {   ##  V12: 0 => TrkIsoVVL, 1 => Iso, 2 => OverlapFilter PFTau, 3 => 1mu, 4 => 2mu, 5 => 1mu-1e, 6 => 1mu-1tau, 7 => 3mu, 8 => 2mu-1e, 9 => 1mu-2e, 10 => 1mu (Mu50), 11 => 1mu (Mu100), 12 => 1mu-1photon for Muon;
                    ##  V12: 0 => LooseChargedIso, 1 => MediumChargedIso, 2 => TightChargedIso, 3 => DeepTau, 4 => TightID OOSC photons, 5 => HPS, 6 => charged iso di-tau, 7 => deeptau di-tau, 8 => e-tau, 9 => mu-tau, 10 => single-tau/tau+MET, 11 => run 2 VBF+ditau, 12 => run 3 VBF+ditau, 13 => run 3 double PF jets + ditau, 14 => di-tau + PFJet, 15 => Displaced Tau, 16 => Monitoring, 17 => regional paths, 18 => L1 seeded paths, 19 => 1 prong tau paths for Tau; 
                    ##  V14: 0 => TrkIsoVVL, 1 => Iso, 2 => OverlapFilter PFTau, 3 => 1mu, 4 => 2mu, 5 => 1mu-1e, 6 => 1mu-1tau, 7 => 3mu, 8 => 2mu-1e, 9 => 1mu-2e, 10 => 1mu (Mu50), 11 => 1mu (Mu100), 12 => 1mu-1photon, 13 => 1mu-1tau PNet for Muon;
                    ##  V14: 0 => Loose, 1 => Medium, 2 => Tight, 3 => DeepTau no spec WP, 4 => PNet no specified WP, 5 => ChargedIso, 6 => Dxy, 7 => e-tau inside filter, 8 => mu-tau inside filter, 9 => Single Tau, 10 => VBF DiTau, 11 => di-tau, 12 => e-tau, 13 => mu-tau, 14 => di-tau + PFJet, 15 => e-tau displaced, 16 => mu-tau displaced, 17 => di-tau displaced, 18 => Monitoring, 19 => VBF SingleTau Monitoring, 20 => DiTau+Jet Monitoring, 21 => Monitoring muTau displaced, 22 => OneProng, 23 => DiTau Monitoring, 24 => OverlapFilter, 25 => VBF DiTau monitoring, 26 => SingleTau Monitoring, 27 => MatchL1HLT, 28 => HPS, 29 => single PF-tau inside filter, 30 => VBF SingleTau for Tau;
                    "2023": [
                        {
                            "flagname": "trg_cross_mu20tau27_hps",
                            "hlt_path": "HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1",
                            "p1_ptcut": 21,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 3,
                            "p1_trigger_particle_id": 13,
                            "p2_ptcut": 32,
                            "p2_etacut": 2.1,
                            "p2_filterbit": 9,  
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },                        
                    ],
                    "2023BPix": [
                        {
                            "flagname": "trg_cross_mu20tau27_hps",
                            "hlt_path": "HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1",
                            "p1_ptcut": 21,
                            "p1_etacut": 2.1,
                            "p1_filterbit": 3,
                            "p1_trigger_particle_id": 13,
                            "p2_ptcut": 32,
                            "p2_etacut": 2.1,
                            "p2_filterbit": 9, 
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },                        
                    ],
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
                            "p2_filterbit": 9,  
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
                            "p2_filterbit": 9, 
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },                        
                    ],
                    
                }
            ),
        },
    )
    ## ET, EE scope trigger setup
    configuration.add_config_parameters(
        ["et", "ee", "em"],
        {   ##  V12: 0 => CaloIdL_TrackIdL_IsoVL, 1 => 1e (WPTight), 2 => 1e (WPLoose), 3 => OverlapFilter PFTau, 4 => 2e, 5 => 1e-1mu, 6 => 1e-1tau, 7 => 3e, 8 => 2e-1mu, 9 => 1e-2mu, 10 => 1e (32_L1DoubleEG_AND_L1SingleEGOr), 11 => 1e (CaloIdVT_GsfTrkIdT), 12 => 1e (PFJet), 13 => 1e (Photon175_OR_Photon200) for Electron;
            ##  V14: 0 => CaloIdL_TrackIdL_IsoVL, 1 => 1e (WPTight), 2 => 1e (WPLoose), 3 => OverlapFilter PFTau, 4 => 2e (Leg 1), 5 => 2e (Leg 2), 6 => 1e-1mu, 7 => 1e-1tau, 8 => 3e, 9 => 2e-1mu, 10 => 1e-2mu, 11 => 1e (32_L1DoubleEG_AND_L1SingleEGOr), 12 => 1e (CaloIdVT_GsfTrkIdT), 13 => 1e (PFJet), 14 => 1e (Photon175_OR_Photon200), 15 => 2e (CaloIdL_MW seeded), 16 => 2e (CaloIdL_MW unseeded), 17 => 1e-1tau PNet for Electron;
            "singleelectron_trigger": EraModifier(
                {   
                    "2023": [
                        {
                            "flagname": "trg_single_ele30",
                            "hlt_path": "HLT_Ele30_WPTight_Gsf",
                            "ptcut": 31,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # {
                        #     "flagname": "trg_single_ele32",
                        #     "hlt_path": "HLT_Ele32_WPTight_Gsf",
                        #     "ptcut": 33,
                        #     "etacut": 2.1,
                        #     "filterbit": 1,
                        #     "trigger_particle_id": 11,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
                        # {
                        #     "flagname": "trg_single_ele35",
                        #     "hlt_path": "HLT_Ele35_WPTight_Gsf",
                        #     "ptcut": 36,
                        #     "etacut": 2.1,
                        #     "filterbit": 1,
                        #     "trigger_particle_id": 11,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
                    ],
                    "2023BPix": [
                        {
                            "flagname": "trg_single_ele30",
                            "hlt_path": "HLT_Ele30_WPTight_Gsf",
                            "ptcut": 31,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # {
                        #     "flagname": "trg_single_ele32",
                        #     "hlt_path": "HLT_Ele32_WPTight_Gsf",
                        #     "ptcut": 33,
                        #     "etacut": 2.1,
                        #     "filterbit": 1,
                        #     "trigger_particle_id": 11,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
                        # {
                        #     "flagname": "trg_single_ele35",
                        #     "hlt_path": "HLT_Ele35_WPTight_Gsf",
                        #     "ptcut": 36,
                        #     "etacut": 2.1,
                        #     "filterbit": 1,
                        #     "trigger_particle_id": 11,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
                    ],
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
                        # {
                        #     "flagname": "trg_single_ele32",
                        #     "hlt_path": "HLT_Ele32_WPTight_Gsf",
                        #     "ptcut": 33,
                        #     "etacut": 2.1,
                        #     "filterbit": 1,
                        #     "trigger_particle_id": 11,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
                        # {
                        #     "flagname": "trg_single_ele35",
                        #     "hlt_path": "HLT_Ele35_WPTight_Gsf",
                        #     "ptcut": 36,
                        #     "etacut": 2.1,
                        #     "filterbit": 1,
                        #     "trigger_particle_id": 11,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
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
                        # {
                        #     "flagname": "trg_single_ele32",
                        #     "hlt_path": "HLT_Ele32_WPTight_Gsf",
                        #     "ptcut": 33,
                        #     "etacut": 2.1,
                        #     "filterbit": 1,
                        #     "trigger_particle_id": 11,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
                        # {
                        #     "flagname": "trg_single_ele35",
                        #     "hlt_path": "HLT_Ele35_WPTight_Gsf",
                        #     "ptcut": 36,
                        #     "etacut": 2.1,
                        #     "filterbit": 1,
                        #     "trigger_particle_id": 11,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
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
                {   ##  V12: 0 => LooseChargedIso, 1 => MediumChargedIso, 2 => TightChargedIso, 3 => DeepTau, 4 => TightID OOSC photons, 5 => HPS, 6 => charged iso di-tau, 7 => deeptau di-tau, 8 => e-tau, 9 => mu-tau, 10 => single-tau/tau+MET, 11 => run 2 VBF+ditau, 12 => run 3 VBF+ditau, 13 => run 3 double PF jets + ditau, 14 => di-tau + PFJet, 15 => Displaced Tau, 16 => Monitoring, 17 => regional paths, 18 => L1 seeded paths, 19 => 1 prong tau paths for Tau; 
                    ##  V14: 0 => CaloIdL_TrackIdL_IsoVL, 1 => 1e (WPTight), 2 => 1e (WPLoose), 3 => OverlapFilter PFTau, 4 => 2e (Leg 1), 5 => 2e (Leg 2), 6 => 1e-1mu, 7 => 1e-1tau, 8 => 3e, 9 => 2e-1mu, 10 => 1e-2mu, 11 => 1e (32_L1DoubleEG_AND_L1SingleEGOr), 12 => 1e (CaloIdVT_GsfTrkIdT), 13 => 1e (PFJet), 14 => 1e (Photon175_OR_Photon200), 15 => 2e (CaloIdL_MW seeded), 16 => 2e (CaloIdL_MW unseeded), 17 => 1e-1tau PNet for Electron;
                    ##  V14: 0 => Loose, 1 => Medium, 2 => Tight, 3 => DeepTau no spec WP, 4 => PNet no specified WP, 5 => ChargedIso, 6 => Dxy, 7 => e-tau inside filter, 8 => mu-tau inside filter, 9 => Single Tau, 10 => VBF DiTau, 11 => di-tau, 12 => e-tau, 13 => mu-tau, 14 => di-tau + PFJet, 15 => e-tau displaced, 16 => mu-tau displaced, 17 => di-tau displaced, 18 => Monitoring, 19 => VBF SingleTau Monitoring, 20 => DiTau+Jet Monitoring, 21 => Monitoring muTau displaced, 22 => OneProng, 23 => DiTau Monitoring, 24 => OverlapFilter, 25 => VBF DiTau monitoring, 26 => SingleTau Monitoring, 27 => MatchL1HLT, 28 => HPS, 29 => single PF-tau inside filter, 30 => VBF SingleTau for Tau;
                    
                    "2023": [
                        {
                            "flagname": "trg_cross_ele24tau30_hps",
                            "hlt_path": "HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1",
                            "p1_ptcut": 25,
                            "p2_ptcut": 32,
                            "p1_etacut": 2.5,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 1,
                            "p1_trigger_particle_id": 11,
                            "p2_filterbit": 8,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # the non HPS version exists for data only, but add it anyway to have the flag in the ntuple
                    ],
                    "2023BPix": [
                        {
                            "flagname": "trg_cross_ele24tau30_hps",
                            "hlt_path": "HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1",
                            "p1_ptcut": 25,
                            "p2_ptcut": 32,
                            "p1_etacut": 2.5,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 1,
                            "p1_trigger_particle_id": 11,
                            "p2_filterbit": 8,  
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # the non HPS version exists for data only, but add it anyway to have the flag in the ntuple
                    ],
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
                            "p2_filterbit": 8,
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
                            "p2_filterbit": 8,  
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # the non HPS version exists for data only, but add it anyway to have the flag in the ntuple
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
                {    ## 0 => LooseChargedIso, 1 => MediumChargedIso, 2 => TightChargedIso, 3 => DeepTau, 4 => TightID OOSC photons, 5 => HPS, 6 => charged iso di-tau, 7 => deeptau di-tau, 8 => e-tau, 9 => mu-tau, 10 => single-tau/tau+MET, 11 => run 2 VBF+ditau, 12 => run 3 VBF+ditau, 13 => run 3 double PF jets + ditau, 14 => di-tau + PFJet, 15 => Displaced Tau, 16 => Monitoring, 17 => regional paths, 18 => L1 seeded paths, 19 => 1 prong tau paths for Tau; 
                     ##  V14: 0 => Loose, 1 => Medium, 2 => Tight, 3 => DeepTau no spec WP, 4 => PNet no specified WP, 5 => ChargedIso, 6 => Dxy, 7 => e-tau inside filter, 8 => mu-tau inside filter, 9 => Single Tau, 10 => VBF DiTau, 11 => di-tau, 12 => e-tau, 13 => mu-tau, 14 => di-tau + PFJet, 15 => e-tau displaced, 16 => mu-tau displaced, 17 => di-tau displaced, 18 => Monitoring, 19 => VBF SingleTau Monitoring, 20 => DiTau+Jet Monitoring, 21 => Monitoring muTau displaced, 22 => OneProng, 23 => DiTau Monitoring, 24 => OverlapFilter, 25 => VBF DiTau monitoring, 26 => SingleTau Monitoring, 27 => MatchL1HLT, 28 => HPS, 29 => single PF-tau inside filter, 30 => VBF SingleTau for Tau;
                    "2023": [
                        {
                            "flagname": "trg_double_tau35_mediumiso_hps", ## it's a name, the trigger is really deeptau not mediumiso hps tau
                            "hlt_path": "HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 7,  
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 7,  
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # the non HPS version exists for data only, but add it anyway to have the flag in the ntuple
                        # {
                        #     "flagname": "trg_double_tau40_tightiso",
                        #     "hlt_path": "HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1",
                        #     "p1_ptcut": 40,
                        #     "p2_ptcut": 40,
                        #     "p1_etacut": 2.1,
                        #     "p2_etacut": 2.1,
                        #     "p1_filterbit": 7,  
                        #     "p1_trigger_particle_id": 15,
                        #     "p2_filterbit": 7,  
                        #     "p2_trigger_particle_id": 15,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
                        # {
                        #     "flagname": "trg_double_tau40_mediumiso_tightid",
                        #     "hlt_path": "HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1",
                        #     "p1_ptcut": 40,
                        #     "p2_ptcut": 40,
                        #     "p1_etacut": 2.1,
                        #     "p2_etacut": 2.1,
                        #     "p1_filterbit": 7, 
                        #     "p1_trigger_particle_id": 15,
                        #     "p2_filterbit": 7,  
                        #     "p2_trigger_particle_id": 15,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
                        {
                            "flagname": "trg_double_tau30_plusPFjet60",
                            "hlt_path": "HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60",
                            "p1_ptcut": 35,
                            "p2_ptcut": 35,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 14,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 14,  # same for v12 and v14
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_double_tau30_plusPFjet75",
                            "hlt_path": "HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75",
                            "p1_ptcut": 35,
                            "p2_ptcut": 35,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 14,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 14,  # same for v12 and v14
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2023BPix": [
                        {
                            "flagname": "trg_double_tau35_mediumiso_hps",
                            "hlt_path": "HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 7, 
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 7,  
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # the non HPS version exists for data only, but add it anyway to have the flag in the ntuple
                        # {
                        #     "flagname": "trg_double_tau40_tightiso",
                        #     "hlt_path": "HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1",
                        #     "p1_ptcut": 40,
                        #     "p2_ptcut": 40,
                        #     "p1_etacut": 2.1,
                        #     "p2_etacut": 2.1,
                        #     "p1_filterbit": 7, 
                        #     "p1_trigger_particle_id": 15,
                        #     "p2_filterbit": 7,  
                        #     "p2_trigger_particle_id": 15,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
                        # {
                        #     "flagname": "trg_double_tau40_mediumiso_tightid",
                        #     "hlt_path": "HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1",
                        #     "p1_ptcut": 40,
                        #     "p2_ptcut": 40,
                        #     "p1_etacut": 2.1,
                        #     "p2_etacut": 2.1,
                        #     "p1_filterbit": 7, 
                        #     "p1_trigger_particle_id": 15,
                        #     "p2_filterbit": 7,  
                        #     "p2_trigger_particle_id": 15,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
                        {
                            "flagname": "trg_double_tau30_plusPFjet60",
                            "hlt_path": "HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60",
                            "p1_ptcut": 35,
                            "p2_ptcut": 35,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 14,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 14,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_double_tau30_plusPFjet75",
                            "hlt_path": "HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75",
                            "p1_ptcut": 35,
                            "p2_ptcut": 35,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 14,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 14,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2022EE": [
                        {
                            "flagname": "trg_double_tau35_mediumiso_hps", ## it's a name, the trigger is really deeptau not mediumiso hps tau
                            "hlt_path": "HLT_DoubleMediumDeepTauPFTauHPS35_L2NN_eta2p1",
                            "p1_ptcut": 40,
                            "p2_ptcut": 40,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 7,  
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 7,  
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # the non HPS version exists for data only, but add it anyway to have the flag in the ntuple
                        # {
                        #     "flagname": "trg_double_tau40_tightiso",
                        #     "hlt_path": "HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1",
                        #     "p1_ptcut": 40,
                        #     "p2_ptcut": 40,
                        #     "p1_etacut": 2.1,
                        #     "p2_etacut": 2.1,
                        #     "p1_filterbit": 7,  
                        #     "p1_trigger_particle_id": 15,
                        #     "p2_filterbit": 7,  
                        #     "p2_trigger_particle_id": 15,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
                        # {
                        #     "flagname": "trg_double_tau40_mediumiso_tightid",
                        #     "hlt_path": "HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1",
                        #     "p1_ptcut": 40,
                        #     "p2_ptcut": 40,
                        #     "p1_etacut": 2.1,
                        #     "p2_etacut": 2.1,
                        #     "p1_filterbit": 7, 
                        #     "p1_trigger_particle_id": 15,
                        #     "p2_filterbit": 7,  
                        #     "p2_trigger_particle_id": 15,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
                        {
                            "flagname": "trg_double_tau30_plusPFjet60",
                            "hlt_path": "HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60",
                            "p1_ptcut": 35,
                            "p2_ptcut": 35,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 14,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 14,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_double_tau30_plusPFjet75",
                            "hlt_path": "HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75",
                            "p1_ptcut": 35,
                            "p2_ptcut": 35,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 14,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 14,
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
                            "p1_filterbit": 7, 
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 7,  
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # the non HPS version exists for data only, but add it anyway to have the flag in the ntuple
                        # {
                        #     "flagname": "trg_double_tau40_tightiso",
                        #     "hlt_path": "HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1",
                        #     "p1_ptcut": 40,
                        #     "p2_ptcut": 40,
                        #     "p1_etacut": 2.1,
                        #     "p2_etacut": 2.1,
                        #     "p1_filterbit": 7, 
                        #     "p1_trigger_particle_id": 15,
                        #     "p2_filterbit": 7,  
                        #     "p2_trigger_particle_id": 15,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
                        # {
                        #     "flagname": "trg_double_tau40_mediumiso_tightid",
                        #     "hlt_path": "HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1",
                        #     "p1_ptcut": 40,
                        #     "p2_ptcut": 40,
                        #     "p1_etacut": 2.1,
                        #     "p2_etacut": 2.1,
                        #     "p1_filterbit": 7, 
                        #     "p1_trigger_particle_id": 15,
                        #     "p2_filterbit": 7,  
                        #     "p2_trigger_particle_id": 15,
                        #     "max_deltaR_triggermatch": 0.4,
                        # },
                        {
                            "flagname": "trg_double_tau30_plusPFjet60",
                            "hlt_path": "HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60",
                            "p1_ptcut": 35,
                            "p2_ptcut": 35,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 14,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 14,
                            "p2_trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        {
                            "flagname": "trg_double_tau30_plusPFjet75",
                            "hlt_path": "HLT_DoubleMediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75",
                            "p1_ptcut": 35,
                            "p2_ptcut": 35,
                            "p1_etacut": 2.1,
                            "p2_etacut": 2.1,
                            "p1_filterbit": 14,
                            "p1_trigger_particle_id": 15,
                            "p2_filterbit": 14,
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
                    ##  V12: 0 => CaloIdL_TrackIdL_IsoVL, 1 => 1e (WPTight), 2 => 1e (WPLoose), 3 => OverlapFilter PFTau, 4 => 2e, 5 => 1e-1mu, 6 => 1e-1tau, 7 => 3e, 8 => 2e-1mu, 9 => 1e-2mu, 10 => 1e (32_L1DoubleEG_AND_L1SingleEGOr), 11 => 1e (CaloIdVT_GsfTrkIdT), 12 => 1e (PFJet), 13 => 1e (Photon175_OR_Photon200) for Electron;
                    ##  V14: 0 => CaloIdL_TrackIdL_IsoVL, 1 => 1e (WPTight), 2 => 1e (WPLoose), 3 => OverlapFilter PFTau, 4 => 2e (Leg 1), 5 => 2e (Leg 2), 6 => 1e-1mu, 7 => 1e-1tau, 8 => 3e, 9 => 2e-1mu, 10 => 1e-2mu, 11 => 1e (32_L1DoubleEG_AND_L1SingleEGOr), 12 => 1e (CaloIdVT_GsfTrkIdT), 13 => 1e (PFJet), 14 => 1e (Photon175_OR_Photon200), 15 => 2e (CaloIdL_MW seeded), 16 => 2e (CaloIdL_MW unseeded), 17 => 1e-1tau PNet for Electron;
                    ##  V12: 0 => TrkIsoVVL, 1 => Iso, 2 => OverlapFilter PFTau, 3 => 1mu, 4 => 2mu, 5 => 1mu-1e, 6 => 1mu-1tau, 7 => 3mu, 8 => 2mu-1e, 9 => 1mu-2e, 10 => 1mu (Mu50), 11 => 1mu (Mu100), 12 => 1mu-1photon for Muon;
                    ##  V14: 0 => TrkIsoVVL, 1 => Iso, 2 => OverlapFilter PFTau, 3 => 1mu, 4 => 2mu, 5 => 1mu-1e, 6 => 1mu-1tau, 7 => 3mu, 8 => 2mu-1e, 9 => 1mu-2e, 10 => 1mu (Mu50), 11 => 1mu (Mu100), 12 => 1mu-1photon, 13 => 1mu-1tau PNet for Muon;
                    "2023": [
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
                    "2023BPix": [
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
                    ## TODO:
                    "2023": [
                        {
                            "flagname": "trg_single_tau180_1",
                            "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 3,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # {
                        #     "flagname": "trg_single_deeptau180_1",
                        #     "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                        #     "ptcut": 180,
                        #     "etacut": 2.1,
                        #     "filterbit": 3,
                        #     "trigger_particle_id": 15,
                        #     "max_deltaR_triggermatch": 0.4,
                        # }
                        
                    ],
                    "2023BPix": [
                        {
                            "flagname": "trg_single_tau180_1",
                            "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 3,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # {
                        #     "flagname": "trg_single_deeptau180_1",
                        #     "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                        #     "ptcut": 180,
                        #     "etacut": 2.1,
                        #     "filterbit": 3,
                        #     "trigger_particle_id": 15,
                        #     "max_deltaR_triggermatch": 0.4,
                        # }
                    ],
                    "2022EE": [
                        {
                            "flagname": "trg_single_tau180_1",
                            "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 3,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # {
                        #     "flagname": "trg_single_deeptau180_1",
                        #     "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                        #     "ptcut": 180,
                        #     "etacut": 2.1,
                        #     "filterbit": 3,
                        #     "trigger_particle_id": 15,
                        #     "max_deltaR_triggermatch": 0.4,
                        # }
                        
                    ],
                    "2022postEE": [
                        {
                            "flagname": "trg_single_tau180_1",
                            "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 3,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # {
                        #     "flagname": "trg_single_deeptau180_1",
                        #     "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                        #     "ptcut": 180,
                        #     "etacut": 2.1,
                        #     "filterbit": 3,
                        #     "trigger_particle_id": 15,
                        #     "max_deltaR_triggermatch": 0.4,
                        # }
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
                    # TODO:
                    "2023": [
                        {
                            "flagname": "trg_single_tau180_2",
                            "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 3,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # {
                        #     "flagname": "trg_single_deeptau180_2",
                        #     "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                        #     "ptcut": 180,
                        #     "etacut": 2.1,
                        #     "filterbit": 3,
                        #     "trigger_particle_id": 15,
                        #     "max_deltaR_triggermatch": 0.4,
                        # }
                    ],
                    "2023BPix": [
                        {
                            "flagname": "trg_single_tau180_2",
                            "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 3,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # {
                        #     "flagname": "trg_single_deeptau180_2",
                        #     "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                        #     "ptcut": 180,
                        #     "etacut": 2.1,
                        #     "filterbit": 3,
                        #     "trigger_particle_id": 15,
                        #     "max_deltaR_triggermatch": 0.4,
                        # }
                    ],
                    "2022EE": [
                        {
                            "flagname": "trg_single_tau180_2",
                            "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 3,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # {
                        #     "flagname": "trg_single_deeptau180_2",
                        #     "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                        #     "ptcut": 180,
                        #     "etacut": 2.1,
                        #     "filterbit": 3,
                        #     "trigger_particle_id": 15,
                        #     "max_deltaR_triggermatch": 0.4,
                        # }
                    ],
                    "2022postEE": [
                        {
                            "flagname": "trg_single_tau180_2",
                            "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                            "ptcut": 180,
                            "etacut": 2.1,
                            "filterbit": 3,
                            "trigger_particle_id": 15,
                            "max_deltaR_triggermatch": 0.4,
                        },
                        # {
                        #     "flagname": "trg_single_deeptau180_2",
                        #     "hlt_path": "HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1",
                        #     "ptcut": 180,
                        #     "etacut": 2.1,
                        #     "filterbit": 3,
                        #     "trigger_particle_id": 15,
                        #     "max_deltaR_triggermatch": 0.4,
                        # }
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
                    ## TODO:
                    "2023": [
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
                    "2023BPix": [
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
                    
                }
            )
        },
    )

    return configuration

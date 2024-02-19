from code_generation.configuration import Configuration
from code_generation.systematics import SystematicShift
from .producers import scalefactors as scalefactors
from .producers import pairselection as pairselection
from .producers import muons as muons
from .producers import electrons as electrons
from .producers import taus as taus


def add_tauVariations(configuration: Configuration, sample: str, era: str):
    if sample == "embedding" or sample == "embedding_mc" or sample == "data":
        return configuration
    #########################
    # TauvsMuID scale factor shifts
    #########################
    # vsJet shifts et/mt, tau pt dependent
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTau30to35Down",
    #         shift_config={("et", "mt"): {"tau_sf_vsjet_tau30to35": "down"}},
    #         producers={("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF},
    #     )
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTau30to35Up",
    #         shift_config={("et", "mt"): {"tau_sf_vsjet_tau30to35": "up"}},
    #         producers={("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF},
    #     )
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTau35to40Down",
    #         shift_config={("et", "mt"): {"tau_sf_vsjet_tau35to40": "down"}},
    #         producers={("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF},
    #     )
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTau35to40Up",
    #         shift_config={("et", "mt"): {"tau_sf_vsjet_tau35to40": "up"}},
    #         producers={("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF},
    #     )
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTau40to500Down",
    #         shift_config={("et", "mt"): {"tau_sf_vsjet_tau40to500": "down"}},
    #         producers={("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF},
    #     )
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTau40to500Up",
    #         shift_config={("et", "mt"): {"tau_sf_vsjet_tau40to500": "up"}},
    #         producers={("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF},
    #     )
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTau500to1000Down",
    #         shift_config={("et", "mt"): {"tau_sf_vsjet_tau500to1000": "down"}},
    #         producers={("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF},
    #     )
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTau500to1000Up",
    #         shift_config={("et", "mt"): {"tau_sf_vsjet_tau500to1000": "up"}},
    #         producers={("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF},
    #     )
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTau1000toInfDown",
    #         shift_config={("et", "mt"): {"tau_sf_vsjet_tau1000toinf": "down"}},
    #         producers={("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF},
    #     )
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTau1000toInfUp",
    #         shift_config={("et", "mt"): {"tau_sf_vsjet_tau1000toinf": "up"}},
    #         producers={("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF},
    #     )
    # )

    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTauDM0Down",
    #         shift_config={("tt","et","mt"): {"tau_sf_vsjet_tauDM0": "down"}},
    #         producers={
    #             "tt": [
    #                 scalefactors.Tau_1_VsJetTauID_SF,
    #                 scalefactors.Tau_2_VsJetTauID_tt_SF,
    #             ],
    #             ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
    #         },
    #     )
    # )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM0_stat1up",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM0": "stat1_dm0_up"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM0_stat2up",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM0": "stat2_dm0_up"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM0_systup",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM0": "syst_alleras_up"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM1_stat1up",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM1": "stat1_dm1_up"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM1_stat2up",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM1": "stat2_dm1_up"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM1_systup",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM1": "syst_alleras_up"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM10_stat1up",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM10": "stat1_dm10_up"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM10_stat2up",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM10": "stat2_dm10_up"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM10_systup",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM10": "syst_alleras_up"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM11_stat1up",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM11": "stat1_dm11_up"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM11_stat2up",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM11": "stat2_dm11_up"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM11_systup",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM11": "syst_alleras_up"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )


    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM0_stat1down",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM0": "stat1_dm0_down"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM0_stat2down",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM0": "stat2_dm0_down"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM0_systdown",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM0": "syst_alleras_down"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM1_stat1down",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM1": "stat1_dm1_down"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM1_stat2down",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM1": "stat2_dm1_down"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM1_systdown",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM1": "syst_alleras_down"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM10_stat1down",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM10": "stat1_dm10_down"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM10_stat2down",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM10": "stat2_dm10_down"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM10_systdown",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM10": "syst_alleras_down"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM11_stat1down",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM11": "stat1_dm11_down"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM11_stat2down",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM11": "stat2_dm11_down"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM11_systdown",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM11": "syst_alleras_down"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM0_TES_up",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM0": "syst_TES_2022_postEE_dm0_up" if era == "2022postEE" else "syst_TES_2022_preEE_dm0_up"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM0_TES_down",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM0": "syst_TES_2022_postEE_dm0_down" if era == "2022postEE" else "syst_TES_2022_preEE_dm0_down"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM1_TES_up",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM1": "syst_TES_2022_postEE_dm1_up" if era == "2022postEE" else "syst_TES_2022_preEE_dm1_up"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM10_TES_up",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM10": "syst_TES_2022_postEE_dm10_up" if era == "2022postEE" else "syst_TES_2022_preEE_dm10_up"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM10_TES_down",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM10": "syst_TES_2022_postEE_dm10_down" if era == "2022postEE" else "syst_TES_2022_preEE_dm10_down"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM1_TES_down",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM1": "syst_TES_2022_postEE_dm1_down" if era == "2022postEE" else "syst_TES_2022_preEE_dm1_down"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM11_TES_up",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM11": "syst_TES_2022_postEE_dm11_up" if era == "2022postEE" else "syst_TES_2022_preEE_dm11_up"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="vsjet_tauDM11_TES_down",
            shift_config={("tt","et","mt"): {
                "tau_sf_vsjet_tauDM11": "syst_TES_2022_postEE_dm11_down" if era == "2022postEE" else "syst_TES_2022_preEE_dm11_down"
                }},
                producers={
                    "tt": [
                        scalefactors.Tau_1_VsJetTauID_SF,
                        scalefactors.Tau_2_VsJetTauID_tt_SF,
                    ],
                    ("et", "mt"): scalefactors.Tau_2_VsJetTauID_lt_SF,
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="ditau_crosstau_trg_SF_up",
            shift_config={
                ("et","mt"): {
                    "leptau_trigger_sf_list": [{
                    "flagname": "trg_wgt_ditau_crosstau_2",
                    "trigger_wp": "Medium",
                    "trigger_corrtype": "sf", 
                    "trigger_syst": "up",}]
                },
                "tt": {
                    "ditau_trigger_sf_list": [{
                    "flagname1": "trg_wgt_ditau_crosstau_1",
                    "flagname2": "trg_wgt_ditau_crosstau_2",
                    "trigger_wp": "Medium",
                    "trigger_corrtype": "sf", 
                    "trigger_syst": "up",}
                ],
                }
            },
                producers={
                    "tt": [
                        scalefactors.TTGenerateDitauTriggerSF_1,
                        scalefactors.TTGenerateDitauTriggerSF_2
                    ],
                    "et": scalefactors.ETGenerateDitauTriggerSF_2,
                    "mt": scalefactors.MTGenerateDitauTriggerSF_2
                },
            )
        )
    configuration.add_shift(
        SystematicShift(
            name="ditau_crosstau_trg_SF_down",
            shift_config={
                ("et","mt"): {
                    "leptau_trigger_sf_list": [{
                    "flagname": "trg_wgt_ditau_crosstau_2",
                    "trigger_wp": "Medium",
                    "trigger_corrtype": "sf", 
                    "trigger_syst": "down",}]
                },
                "tt": {
                    "ditau_trigger_sf_list": [{
                    "flagname1": "trg_wgt_ditau_crosstau_1",
                    "flagname2": "trg_wgt_ditau_crosstau_2",
                    "trigger_wp": "Medium",
                    "trigger_corrtype": "sf", 
                    "trigger_syst": "down",}
                ],
                }
            },
                producers={
                    "tt": [
                        scalefactors.TTGenerateDitauTriggerSF_1,
                        scalefactors.TTGenerateDitauTriggerSF_2
                    ],
                    "et": scalefactors.ETGenerateDitauTriggerSF_2,
                    "mt": scalefactors.MTGenerateDitauTriggerSF_2
                },
            )
        )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTauDM0Down",
    #         shift_config={"tt": {"tau_sf_vsjet_tauDM0": "down"}},
    #         producers={
    #             "tt": [
    #                 scalefactors.Tau_1_VsJetTauID_SF,
    #                 scalefactors.Tau_2_VsJetTauID_tt_SF,
    #             ]
    #         },
    #     )
    # )
    # # vsJet shifts tt, tau dm dependent
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTauDM0Up",
    #         shift_config={"tt": {"tau_sf_vsjet_tauDM0": "up"}},
    #         producers={
    #             "tt": [
    #                 scalefactors.Tau_1_VsJetTauID_SF,
    #                 scalefactors.Tau_2_VsJetTauID_tt_SF,
    #             ]
    #         },
    #     )
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTauDM1Down",
    #         shift_config={"tt": {"tau_sf_vsjet_tauDM1": "down"}},
    #         producers={
    #             "tt": [
    #                 scalefactors.Tau_1_VsJetTauID_SF,
    #                 scalefactors.Tau_2_VsJetTauID_tt_SF,
    #             ]
    #         },
    #     )
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTauDM1Up",
    #         shift_config={"tt": {"tau_sf_vsjet_tauDM1": "up"}},
    #         producers={
    #             "tt": [
    #                 scalefactors.Tau_1_VsJetTauID_SF,
    #                 scalefactors.Tau_2_VsJetTauID_tt_SF,
    #             ]
    #         },
    #     )
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTauDM10Down",
    #         shift_config={"tt": {"tau_sf_vsjet_tauDM10": "down"}},
    #         producers={
    #             "tt": [
    #                 scalefactors.Tau_1_VsJetTauID_SF,
    #                 scalefactors.Tau_2_VsJetTauID_tt_SF,
    #             ]
    #         },
    #     )
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTauDM10Up",
    #         shift_config={"tt": {"tau_sf_vsjet_tauDM10": "up"}},
    #         producers={
    #             "tt": [
    #                 scalefactors.Tau_1_VsJetTauID_SF,
    #                 scalefactors.Tau_2_VsJetTauID_tt_SF,
    #             ]
    #         },
    #     )
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTauDM11Down",
    #         shift_config={"tt": {"tau_sf_vsjet_tauDM11": "down"}},
    #         producers={
    #             "tt": [
    #                 scalefactors.Tau_1_VsJetTauID_SF,
    #                 scalefactors.Tau_2_VsJetTauID_tt_SF,
    #             ]
    #         },
    #     )
    # )
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsJetTauDM11Up",
    #         shift_config={"tt": {"tau_sf_vsjet_tauDM11": "up"}},
    #         producers={
    #             "tt": [
    #                 scalefactors.Tau_1_VsJetTauID_SF,
    #                 scalefactors.Tau_2_VsJetTauID_tt_SF,
    #             ]
    #         },
    #     )
    # )
    #########################
    # TauvsEleID scale factor shifts
    #########################
    # configuration.add_shift(
    #     SystematicShift(
    #         name="vsEleBarrelDown",
    #         shift_config={
    #             ("et","mt"): {
    #                 "vsjet_tau_id_sf":  "vsele_tau_id": [
    #             {
    #                 "tau_id_discriminator": "DeepTau2018v2p5VSe",
    #                 "tau_1_vsele_sf_outputname": "id_wgt_tau_vsEle_{wp}_1".format(
    #                     wp=wp
    #                 ),
    #                 "tau_2_vsele_sf_outputname": "id_wgt_tau_vsEle_{wp}_2".format(
    #                     wp=wp
    #                 ),
    #                 "vsele_tau_id_WP": "{wp}".format(wp=wp),
    #                 "tau_1_vsele_id_outputname": "id_tau_vsEle_{wp}_1".format(wp=wp),
    #                 "tau_2_vsele_id_outputname": "id_tau_vsEle_{wp}_2".format(wp=wp),
    #                 "vsele_tau_id_WPbit": bit,
    #             }
    #             for wp, bit in {
    #                 "VVLoose": 2,
    #                 "Tight": 6,
    #             }.items()
    #         ],
    #             },
    #         },
    #           producers={("et", "mt"): scalefactors.Tau_2_VsEleTauID_SF},
    #         )
    #     )
    configuration.add_shift(
        SystematicShift(
            name="vsEleBarrelDown",
            shift_config={("et", "mt"): {"tau_sf_vsele_barrel": "down"}},
            producers={("et", "mt"): scalefactors.Tau_2_VsEleTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsEleBarrelUp",
            shift_config={("et", "mt"): {"tau_sf_vsele_barrel": "up"}},
            producers={("et", "mt"): scalefactors.Tau_2_VsEleTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsEleEndcapDown",
            shift_config={("et", "mt"): {"tau_sf_vsele_endcap": "down"}},
            producers={("et", "mt"): scalefactors.Tau_2_VsEleTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsEleEndcapUp",
            shift_config={("et", "mt"): {"tau_sf_vsele_endcap": "up"}},
            producers={("et", "mt"): scalefactors.Tau_2_VsEleTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsEleBarrelDown",
            shift_config={"tt": {"tau_sf_vsele_barrel": "down"}},
            producers={
                "tt": [
                    scalefactors.Tau_1_VsEleTauID_SF,
                    scalefactors.Tau_2_VsEleTauID_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsEleBarrelUp",
            shift_config={"tt": {"tau_sf_vsele_barrel": "up"}},
            producers={
                "tt": [
                    scalefactors.Tau_1_VsEleTauID_SF,
                    scalefactors.Tau_2_VsEleTauID_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsEleEndcapDown",
            shift_config={"tt": {"tau_sf_vsele_endcap": "down"}},
            producers={
                "tt": [
                    scalefactors.Tau_1_VsEleTauID_SF,
                    scalefactors.Tau_2_VsEleTauID_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsEleEndcapUp",
            shift_config={"tt": {"tau_sf_vsele_endcap": "up"}},
            producers={
                "tt": [
                    scalefactors.Tau_1_VsEleTauID_SF,
                    scalefactors.Tau_2_VsEleTauID_SF,
                ]
            },
        )
    )
    #########################
    # TauvsMuID scale factor shifts
    #########################
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel1Down",
            shift_config={("et", "mt"): {"tau_sf_vsmu_wheel1": "down"}},
            producers={("et", "mt"): scalefactors.Tau_2_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel1Up",
            shift_config={("et", "mt"): {"tau_sf_vsmu_wheel1": "up"}},
            producers={("et", "mt"): scalefactors.Tau_2_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel2Down",
            shift_config={("et", "mt"): {"tau_sf_vsmu_wheel2": "down"}},
            producers={("et", "mt"): scalefactors.Tau_2_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel2Up",
            shift_config={("et", "mt"): {"tau_sf_vsmu_wheel2": "up"}},
            producers={("et", "mt"): scalefactors.Tau_2_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel3Down",
            shift_config={("et", "mt"): {"tau_sf_vsmu_wheel3": "down"}},
            producers={("et", "mt"): scalefactors.Tau_2_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel3Up",
            shift_config={("et", "mt"): {"tau_sf_vsmu_wheel3": "up"}},
            producers={("et", "mt"): scalefactors.Tau_2_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel4Down",
            shift_config={("et", "mt"): {"tau_sf_vsmu_wheel4": "down"}},
            producers={("et", "mt"): scalefactors.Tau_2_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel4Up",
            shift_config={("et", "mt"): {"tau_sf_vsmu_wheel4": "up"}},
            producers={("et", "mt"): scalefactors.Tau_2_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel5Down",
            shift_config={("et", "mt"): {"tau_sf_vsmu_wheel5": "down"}},
            producers={("et", "mt"): scalefactors.Tau_2_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel5Up",
            shift_config={("et", "mt"): {"tau_sf_vsmu_wheel5": "up"}},
            producers={("et", "mt"): scalefactors.Tau_2_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel1Down",
            shift_config={"tt": {"tau_sf_vsmu_wheel1": "down"}},
            producers={
                "tt": [scalefactors.Tau_1_VsMuTauID_SF, scalefactors.Tau_2_VsMuTauID_SF]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel1Up",
            shift_config={"tt": {"tau_sf_vsmu_wheel1": "up"}},
            producers={
                "tt": [scalefactors.Tau_1_VsMuTauID_SF, scalefactors.Tau_2_VsMuTauID_SF]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel2Down",
            shift_config={"tt": {"tau_sf_vsmu_wheel2": "down"}},
            producers={
                "tt": [scalefactors.Tau_1_VsMuTauID_SF, scalefactors.Tau_2_VsMuTauID_SF]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel2Up",
            shift_config={"tt": {"tau_sf_vsmu_wheel2": "up"}},
            producers={
                "tt": [scalefactors.Tau_1_VsMuTauID_SF, scalefactors.Tau_2_VsMuTauID_SF]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel3Down",
            shift_config={"tt": {"tau_sf_vsmu_wheel3": "down"}},
            producers={
                "tt": [scalefactors.Tau_1_VsMuTauID_SF, scalefactors.Tau_2_VsMuTauID_SF]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel3Up",
            shift_config={"tt": {"tau_sf_vsmu_wheel3": "up"}},
            producers={
                "tt": [scalefactors.Tau_1_VsMuTauID_SF, scalefactors.Tau_2_VsMuTauID_SF]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel4Down",
            shift_config={"tt": {"tau_sf_vsmu_wheel4": "down"}},
            producers={
                "tt": [scalefactors.Tau_1_VsMuTauID_SF, scalefactors.Tau_2_VsMuTauID_SF]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel4Up",
            shift_config={"tt": {"tau_sf_vsmu_wheel4": "up"}},
            producers={
                "tt": [scalefactors.Tau_1_VsMuTauID_SF, scalefactors.Tau_2_VsMuTauID_SF]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel5Down",
            shift_config={"tt": {"tau_sf_vsmu_wheel5": "down"}},
            producers={
                "tt": [scalefactors.Tau_1_VsMuTauID_SF, scalefactors.Tau_2_VsMuTauID_SF]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel5Up",
            shift_config={"tt": {"tau_sf_vsmu_wheel5": "up"}},
            producers={
                "tt": [scalefactors.Tau_1_VsMuTauID_SF, scalefactors.Tau_2_VsMuTauID_SF]
            },
        )
    )
    #########################
    # TES Shifts
    #########################
    configuration.add_shift(
        SystematicShift(
            name="tauEs1prong0pizeroDown",
            shift_config={("et", "mt", "tt"): {"tau_ES_shift_DM0": "down"}},
            producers={("et", "mt", "tt"): taus.TauPtCorrection_genTau},
            ignore_producers={
                "et": [pairselection.LVEl1, electrons.VetoElectrons],
                "mt": [pairselection.LVMu1, muons.VetoMuons],
                "tt": [],
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="tauEs1prong0pizeroUp",
            shift_config={("et", "mt", "tt"): {"tau_ES_shift_DM0": "up"}},
            producers={("et", "mt", "tt"): taus.TauPtCorrection_genTau},
            ignore_producers={
                "et": [pairselection.LVEl1, electrons.VetoElectrons],
                "mt": [pairselection.LVMu1, muons.VetoMuons],
                "tt": [],
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="tauEs1prong1pizeroDown",
            shift_config={("et", "mt", "tt"): {"tau_ES_shift_DM1": "down"}},
            producers={("et", "mt", "tt"): taus.TauPtCorrection_genTau},
            ignore_producers={
                "et": [pairselection.LVEl1, electrons.VetoElectrons],
                "mt": [pairselection.LVMu1, muons.VetoMuons],
                "tt": [],
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="tauEs1prong1pizeroUp",
            shift_config={("et", "mt", "tt"): {"tau_ES_shift_DM1": "up"}},
            producers={("et", "mt", "tt"): taus.TauPtCorrection_genTau},
            ignore_producers={
                "et": [pairselection.LVEl1, electrons.VetoElectrons],
                "mt": [pairselection.LVMu1, muons.VetoMuons],
                "tt": [],
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="tauEs3prong0pizeroDown",
            shift_config={("et", "mt", "tt"): {"tau_ES_shift_DM10": "down"}},
            producers={("et", "mt", "tt"): taus.TauPtCorrection_genTau},
            ignore_producers={
                "et": [pairselection.LVEl1, electrons.VetoElectrons],
                "mt": [pairselection.LVMu1, muons.VetoMuons],
                "tt": [],
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="tauEs3prong0pizeroUp",
            shift_config={("et", "mt", "tt"): {"tau_ES_shift_DM10": "up"}},
            producers={("et", "mt", "tt"): taus.TauPtCorrection_genTau},
            ignore_producers={
                "et": [pairselection.LVEl1, electrons.VetoElectrons],
                "mt": [pairselection.LVMu1, muons.VetoMuons],
                "tt": [],
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="tauEs3prong1pizeroDown",
            shift_config={("et", "mt", "tt"): {"tau_ES_shift_DM11": "down"}},
            producers={("et", "mt", "tt"): taus.TauPtCorrection_genTau},
            ignore_producers={
                "et": [pairselection.LVEl1, electrons.VetoElectrons],
                "mt": [pairselection.LVMu1, muons.VetoMuons],
                "tt": [],
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="tauEs3prong1pizeroUp",
            shift_config={("et", "mt", "tt"): {"tau_ES_shift_DM11": "up"}},
            producers={("et", "mt", "tt"): taus.TauPtCorrection_genTau},
            ignore_producers={
                "et": [pairselection.LVEl1, electrons.VetoElectrons],
                "mt": [pairselection.LVMu1, muons.VetoMuons],
                "tt": [],
            },
        )
    )

    return configuration

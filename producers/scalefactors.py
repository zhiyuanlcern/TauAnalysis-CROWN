from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup
from code_generation.producer import ExtendedVectorProducer


############################
# Muon ID, ISO SF
# The readout is done via correctionlib
############################

TauEmbeddingMuonIDSF_1_MC = Producer(
    name="TauEmbeddingMuonIDSF_1_MC",
    call='scalefactor::embedding::muon_sf({df}, {input}, {output}, "{muon_sf_file}", "{muon_sf_varation}", "{muon_id_sf_name}")',
    input=[q.pt_1, q.eta_1],
    output=[q.id_wgt_mu_1],
    scopes=["mt", "mm"],
)

TauEmbeddingMuonIDSF_2_MC = Producer(
    name="TauEmbeddingMuonIDSF_2_MC",
    call='scalefactor::embedding::muon_sf({df}, {input}, {output}, "{muon_sf_file}", "{muon_sf_varation}", "{muon_id_sf_name}")',
    input=[q.pt_2, q.eta_2],
    output=[q.id_wgt_mu_2],
    scopes=["mm", "em"],
)

TauEmbeddingMuonIsoSF_1_MC = Producer(
    name="TauEmbeddingMuonIsoSF_1_MC",
    call='scalefactor::embedding::muon_sf({df}, {input}, {output}, "{muon_sf_file}", "{muon_sf_varation}", "{muon_iso_sf_name}")',
    input=[q.pt_1, q.eta_1],
    output=[q.iso_wgt_mu_1],
    scopes=["mt", "mm"],
)

TauEmbeddingMuonIsoSF_2_MC = Producer(
    name="TauEmbeddingMuonIsoSF_2_MC",
    call='scalefactor::embedding::muon_sf({df}, {input}, {output}, "{muon_sf_file}", "{muon_sf_varation}", "{muon_iso_sf_name}")',
    input=[q.pt_2, q.eta_2],
    output=[q.iso_wgt_mu_2],
    scopes=["mm", "em"],
)


MuonID_SF = ProducerGroup(
    name="MuonID_SF",
    call=None,
    input=None,
    output=None,
    scopes=["mt", "em", "mm"],
    subproducers={
        "mt": [
            TauEmbeddingMuonIDSF_1_MC,
        ],
        "em": [
            TauEmbeddingMuonIDSF_2_MC,
        ],
        "mm": [
            TauEmbeddingMuonIDSF_1_MC,
            TauEmbeddingMuonIDSF_2_MC,
        ],
    },
)

MuonIso_SF = ProducerGroup(
    name="MuonIDIso_SF",
    call=None,
    input=None,
    output=None,
    scopes=["mt", "em", "mm"],
    subproducers={
        "mt": [
            TauEmbeddingMuonIsoSF_1_MC,
        ],
        "em": [
            TauEmbeddingMuonIsoSF_2_MC,
        ],
        "mm": [
            TauEmbeddingMuonIsoSF_1_MC,
            TauEmbeddingMuonIsoSF_2_MC,
        ],
    },
)

############################
# Tau ID/ISO SF
# The readout is done via correctionlib
############################
Tau_1_VsJetTauID_SF = ExtendedVectorProducer(
    name="Tau_1_VsJetTauID_SF",
    call='scalefactor::tau::id_vsJet_tt({df}, {input}, {vec_open}{tau_dms}{vec_close}, "{vsjet_tau_id_WP}","VVLoose", "{tau_sf_vsjet_tauDM0}", "{tau_sf_vsjet_tauDM1}", "{tau_sf_vsjet_tauDM10}", "{tau_sf_vsjet_tauDM11}", "{tau_vsjet_sf_dependence}", {output}, "{tau_sf_file}", "{tau_id_discriminator}")',
    input=[q.pt_1, q.tau_decaymode_1, q.tau_gen_match_1],
    output="tau_1_vsjet_sf_outputname",
    scope=["tt"],
    vec_config="vsjet_tau_id_sf",
)
Tau_1_VsEleTauID_SF = ExtendedVectorProducer(
    name="Tau_1_VsEleTauID_SF",
    call='scalefactor::tau::id_vsEle({df}, {input}, {vec_open}{tau_dms}{vec_close}, "{vsele_tau_id_WP}", "{tau_sf_vsele_barrel}", "{tau_sf_vsele_endcap}", {output}, "{tau_sf_file}", "{tau_id_discriminator}")',
    input=[q.eta_1, q.tau_decaymode_1, q.tau_gen_match_1],
    output="tau_1_vsele_sf_outputname",
    scope=["tt"],
    vec_config="vsele_tau_id_sf",
)
Tau_1_VsMuTauID_SF = ExtendedVectorProducer(
    name="Tau_1_VsMuTauID_SF",
    call='scalefactor::tau::id_vsMu({df}, {input}, {vec_open}{tau_dms}{vec_close}, "{vsmu_tau_id_WP}", "{tau_sf_vsmu_wheel1}", "{tau_sf_vsmu_wheel2}", "{tau_sf_vsmu_wheel3}", "{tau_sf_vsmu_wheel4}", "{tau_sf_vsmu_wheel5}", {output}, "{tau_sf_file}", "{tau_id_discriminator}")',
    input=[q.eta_1, q.tau_decaymode_1, q.tau_gen_match_1],
    output="tau_1_vsmu_sf_outputname",
    scope=["tt"],
    vec_config="vsmu_tau_id",
)
Tau_2_VsJetTauID_lt_SF = ExtendedVectorProducer(
    name="Tau_2_VsJetTauID_lt_SF",
    call='scalefactor::tau::id_vsJet_tt({df}, {input}, {vec_open}{tau_dms}{vec_close}, "{vsjet_tau_id_WP}", "VVLoose", "{tau_sf_vsjet_tauDM0}", "{tau_sf_vsjet_tauDM1}", "{tau_sf_vsjet_tauDM10}", "{tau_sf_vsjet_tauDM11}", "{tau_vsjet_sf_dependence}", {output}, "{tau_sf_file}", "{tau_id_discriminator}")',
    input=[q.pt_2, q.tau_decaymode_2, q.tau_gen_match_2],
    output="tau_2_vsjet_sf_outputname",
    scope=["et", "mt"],
    vec_config="vsjet_tau_id_sf",
)
Tau_2_VsJetTauID_tt_SF = ExtendedVectorProducer(
    name="Tau_2_VsJetTauID_tt_SF",
    call='scalefactor::tau::id_vsJet_tt({df}, {input}, {vec_open}{tau_dms}{vec_close}, "{vsjet_tau_id_WP}", "VVLoose", "{tau_sf_vsjet_tauDM0}", "{tau_sf_vsjet_tauDM1}", "{tau_sf_vsjet_tauDM10}", "{tau_sf_vsjet_tauDM11}", "{tau_vsjet_sf_dependence}", {output}, "{tau_sf_file}", "{tau_id_discriminator}")',
    input=[q.pt_2, q.tau_decaymode_2, q.tau_gen_match_2],
    output="tau_2_vsjet_sf_outputname",
    scope=["tt"],
    vec_config="vsjet_tau_id_sf",
)
Tau_2_VsEleTauID_SF = ExtendedVectorProducer(
    name="Tau_2_VsEleTauID_SF",
    call='scalefactor::tau::id_vsEle({df}, {input}, {vec_open}{tau_dms}{vec_close}, "{vsele_tau_id_WP}", "{tau_sf_vsele_barrel}", "{tau_sf_vsele_endcap}", {output}, "{tau_sf_file}", "{tau_id_discriminator}")',
    input=[q.eta_2, q.tau_decaymode_2, q.tau_gen_match_2],
    output="tau_2_vsele_sf_outputname",
    scope=["et", "mt", "tt"],
    vec_config="vsele_tau_id_sf",
)
Tau_2_VsMuTauID_SF = ExtendedVectorProducer(
    name="Tau_2_VsMuTauID_SF",
    call='scalefactor::tau::id_vsMu({df}, {input}, {vec_open}{tau_dms}{vec_close}, "{vsmu_tau_id_WP}", "{tau_sf_vsmu_wheel1}", "{tau_sf_vsmu_wheel2}", "{tau_sf_vsmu_wheel3}", "{tau_sf_vsmu_wheel4}", "{tau_sf_vsmu_wheel5}", {output}, "{tau_sf_file}", "{tau_id_discriminator}")',
    input=[q.eta_2, q.tau_decaymode_2, q.tau_gen_match_2],
    output="tau_2_vsmu_sf_outputname",
    scope=["et", "mt", "tt"],
    vec_config="vsmu_tau_id",
)
TauID_SF = ProducerGroup(
    name="TauID_SF",
    call=None,
    input=None,
    output=None,
    scopes=["tt", "mt", "et"],
    subproducers={
        "tt": [
            Tau_1_VsJetTauID_SF,
            Tau_1_VsEleTauID_SF,
            Tau_1_VsMuTauID_SF,
            Tau_2_VsJetTauID_tt_SF,
            Tau_2_VsEleTauID_SF,
            Tau_2_VsMuTauID_SF,
        ],
        "mt": [
            Tau_2_VsJetTauID_lt_SF,
            Tau_2_VsEleTauID_SF,
            Tau_2_VsMuTauID_SF,
        ],
        "et": [
            Tau_2_VsJetTauID_lt_SF,
            Tau_2_VsEleTauID_SF,
            Tau_2_VsMuTauID_SF,
        ],
    },
)

#########################
# Electron ID/ISO SF
#########################
Ele_1_IDTight_SF = Producer(
    name="Ele_IDTight_SF",
    call='scalefactor::electron::id({df}, {input}, "{ele_sf_year_id}", "wp90iso", "{ele_sf_varation}", {output}, "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[q.pt_1, q.eta_1],
    output=[q.id_wgt_ele_wpTight],
    scopes=["em", "ee", "et"],
)
EleID_SF = ProducerGroup(
    name="EleID_SF",
    call=None,
    input=None,
    output=None,
    scopes=["em", "ee", "et"],
    subproducers={
        "em": [Ele_1_IDTight_SF],
        "ee": [Ele_1_IDTight_SF],
        "et": [Ele_1_IDTight_SF],
    },
)

###################################
# Trigger Scalefactors coming from our measurements
###################################
MTGenerateSingleMuonTriggerSF_MC = ExtendedVectorProducer(
    name="MTGenerateSingleMuonTriggerSF_MC",
    call='scalefactor::embedding::muon_sf({df}, {input}, {output}, "{mc_muon_sf_file}", "{mc_muon_sf_correctiontype}", "{mc_trigger_sf}", {mc_muon_trg_extrapolation})',
    input=[q.pt_1, q.eta_1],
    output="flagname",
    scope=["mt", "mm", "em"],
    vec_config="singlemuon_trigger_sf_mc",
)

ETGenerateSingleElectronTriggerSF_MC = ExtendedVectorProducer(
    name="ETGenerateSingleElectronTriggerSF_MC",
    call='scalefactor::embedding::electron_sf({df}, {input}, {output}, "{mc_electron_sf_file}", "{mc_correctiontype}", "{mc_trigger_sf}" , {mc_electron_trg_extrapolation},"{ele_sf_year_id}","{mc_trigger}")',
    input=[q.pt_1, q.eta_1],
    output="flagname",
    scope=["et", "ee", "em"],
    vec_config="singlelectron_trigger_sf_mc",
)
## ditau_trigger_sf can be applied to all cross-trigger, the structure is the same
ETGenerateDitauTriggerSF_2 = ExtendedVectorProducer(
    name="ETGenerateDitauTriggerSF_2",
    call='scalefactor::embedding::ditau_trigger_sf({df}, {input}, {output}, "{trigger_wp}", "{tau_trigger_sf_file}", "etau", "{trigger_corrtype}", "{trigger_syst}")',
    input=[q.pt_2, q.tau_decaymode_2],
    output="flagname",
    scope=["et"],
    vec_config="leptau_trigger_sf_list",
)
MTGenerateDitauTriggerSF_2 = ExtendedVectorProducer(
    name="MTGenerateDitauTriggerSF_2",
    call='scalefactor::embedding::ditau_trigger_sf({df}, {input}, {output}, "{trigger_wp}", "{tau_trigger_sf_file}", "mutau", "{trigger_corrtype}", "{trigger_syst}")',
    input=[q.pt_2, q.tau_decaymode_2],
    output="flagname",
    scope=["mt"],
    vec_config="leptau_trigger_sf_list",
)
TTGenerateDitauTriggerSF_1 = ExtendedVectorProducer(
    name="TTGenerateDitauTriggerSF_1",
    call='scalefactor::embedding::ditau_trigger_sf({df}, {input}, {output}, "{trigger_wp}", "{tau_trigger_sf_file}", "ditau", "{trigger_corrtype}", "{trigger_syst}")',
    input=[q.pt_1, q.tau_decaymode_1],
    output="flagname1",
    scope=["tt"],
    vec_config="ditau_trigger_sf_list",
)
TTGenerateDitauTriggerSF_2 = ExtendedVectorProducer(
    name="TTGenerateDitauTriggerSF_2",
    call='scalefactor::embedding::ditau_trigger_sf({df}, {input}, {output}, "{trigger_wp}", "{tau_trigger_sf_file}", "ditau", "{trigger_corrtype}", "{trigger_syst}")',
    input=[q.pt_2, q.tau_decaymode_2],
    output="flagname2",
    scope=["tt"],
    vec_config="ditau_trigger_sf_list",
)

#########################
# b-tagging SF
#########################
btagging_SF = Producer(
    name="btagging_SF",
    call='scalefactor::jet::btagSF({df}, {input}, "{btag_sf_variation}", {output}, "{btag_sf_file}", "{btag_corr_algo}")',
    input=[
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.BJet_discriminator,
        nanoAOD.Jet_flavor,
        q.good_jets_mask,
        q.good_bjets_mask,
        q.jet_overlap_veto_mask,
    ],
    output=[q.btag_weight],
    scopes=["tt", "mt", "et", "mm", "em", "ee"],
)

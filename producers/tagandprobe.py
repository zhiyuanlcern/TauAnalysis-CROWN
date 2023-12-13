from ..quantities import output as q
from ..quantities import tagandprobe_output as tp_q
from ..quantities import nanoAOD as nanoAOD
from ..producers.muons import (
    MuonPtCut,
    MuonEtaCut,
    GoodMuonPtCut,
    GoodMuonEtaCut,
)
from ..producers.electrons import (
    ElectronPtCut,
    ElectronEtaCut,
    GoodElectronPtCut,
    GoodElectronEtaCut,
)
from ..producers.photons import (
    PhotonPtCut,
    PhotonEtaCut,
    PhotonElectronVeto,
)
from code_generation.producer import (
    Producer,
    ProducerGroup,
    ExtendedVectorProducer,
)

BaseMuons = ProducerGroup(
    name="BaseMuons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.base_muons_mask],
    scopes=["global"],
    subproducers=[
        MuonPtCut,
        MuonEtaCut,
    ],
)

GoodMuons = ProducerGroup(
    name="BaseMuons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.good_muons_mask],
    scopes=["mm"],
    subproducers=[
        GoodMuonPtCut,
        GoodMuonEtaCut,
    ],
)

BasePhotons = ProducerGroup(
    name="BasePhotons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.base_photons_mask],
    scopes=["global"],
    subproducers=[
        PhotonPtCut,
        PhotonEtaCut,
        PhotonElectronVeto,
    ],
)

# MuMuTagAndProbePairSelection = Producer(
#     name="MuMuPairSelection",
#     call="pairselection::mumu::TagAndProbePairSelection({df}, {input_vec}, {output})",
#     input=[
#         nanoAOD.Muon_pt,
#         q.good_muons_mask,
#     ],
#     output=[q.dileptonpair],
#     scopes=["mm"],
# )

# GoodMuMuPairFlag = Producer(
#     name="GoodMuMuPairFlag",
#     call="pairselection::flagGoodPairs({df}, {output}, {input})",
#     input=[q.dileptonpair],
#     output=[],
#     scopes=["mm"],
# )

# GoodMuMuPairFilter = Filter(
#     name="GoodMuMuPairFilter",
#     call='basefunctions::FilterFlagsAny({df}, "GoodMuMuPairs", {input})',
#     input=[],
#     scopes=["mm"],
#     subproducers=[GoodMuMuPairFlag],
# )

# MuMuTagAndProbePairs = ProducerGroup(
#     name="UnrollMuLV1",
#     call=None,
#     input=None,
#     output=None,
#     scopes=["mm"],
#     subproducers=[
#         MuMuTagAndProbePairSelection,
#         GoodMuMuPairFlag,
#         GoodMuMuPairFilter,
#     ],
# )
MuMuSingleMuonTriggerFlags_1 = ExtendedVectorProducer(
    name="MuMuGenerateSingleMuonTriggerFlags_1",
    call='trigger::tagandprobe::GenerateSingleTriggerFlag({df}, {output}, {input}, "{hlt_path}", {ptcut}, {etacut}, {trigger_particle_id}, {filterbit}, {max_deltaR_triggermatch}, {triggerobject_ptcut} )',
    input=[
        q.p4_1,
        nanoAOD.TriggerObject_bit,
        nanoAOD.TriggerObject_id,
        nanoAOD.TriggerObject_pt,
        nanoAOD.TriggerObject_eta,
        nanoAOD.TriggerObject_phi,
    ],
    output="flagname_1",
    scope=["mm"],
    vec_config="singlemuon_trigger",
)
MuMuSingleMuonTriggerFlags_2 = ExtendedVectorProducer(
    name="MuMuGenerateSingleMuonTriggerFlags_2",
    call='trigger::tagandprobe::GenerateSingleTriggerFlag({df}, {output}, {input}, "{hlt_path}", {ptcut}, {etacut}, {trigger_particle_id}, {filterbit}, {max_deltaR_triggermatch}, {triggerobject_ptcut} )',
    input=[
        q.p4_2,
        nanoAOD.TriggerObject_bit,
        nanoAOD.TriggerObject_id,
        nanoAOD.TriggerObject_pt,
        nanoAOD.TriggerObject_eta,
        nanoAOD.TriggerObject_phi,
    ],
    output="flagname_2",
    scope=["mm"],
    vec_config="singlemuon_trigger",
)
MuMuDoubleMuonTriggerFlags_1 = ExtendedVectorProducer(
    name="MuMuDoubleMuonTriggerFlags_1",
    call='trigger::tagandprobe::GenerateDoubleTriggerFlag({df}, {output}, {input}, "{hlt_path}", {p1_ptcut}, {p2_ptcut}, {p1_etacut}, {p2_etacut}, {p1_trigger_particle_id}, {p2_trigger_particle_id}, {p1_filterbit}, {p2_filterbit}, {max_deltaR_triggermatch}, {p1_triggerobject_ptcut}, {p2_triggerobject_ptcut} )',
    input=[
        q.p4_1,
        q.p4_2,
        nanoAOD.TriggerObject_bit,
        nanoAOD.TriggerObject_id,
        nanoAOD.TriggerObject_pt,
        nanoAOD.TriggerObject_eta,
        nanoAOD.TriggerObject_phi,
    ],
    output="flagname_1",
    scope=["mm"],
    vec_config="doublemuon_trigger",
)
MuMuDoubleMuonTriggerFlags_2 = ExtendedVectorProducer(
    name="MuMuDoubleMuonTriggerFlags_2",
    call='trigger::tagandprobe::GenerateDoubleTriggerFlag({df}, {output}, {input}, "{hlt_path}", {p1_ptcut}, {p2_ptcut}, {p1_etacut}, {p2_etacut}, {p1_trigger_particle_id}, {p2_trigger_particle_id}, {p1_filterbit}, {p2_filterbit}, {max_deltaR_triggermatch}, {p1_triggerobject_ptcut}, {p2_triggerobject_ptcut} )',
    input=[
        q.p4_2,
        q.p4_1,
        nanoAOD.TriggerObject_bit,
        nanoAOD.TriggerObject_id,
        nanoAOD.TriggerObject_pt,
        nanoAOD.TriggerObject_eta,
        nanoAOD.TriggerObject_phi,
    ],
    output="flagname_2",
    scope=["mm"],
    vec_config="doublemuon_trigger",
)

MuMuSingleMuonTriggerBitFlags_1 = ExtendedVectorProducer(
    name="MuMuSingleMuonTriggerBitFlags_1",
    call='trigger::tagandprobe::MatchSingleTriggerObject({df}, {output}, {input}, {ptcut}, {etacut}, {trigger_particle_id}, {filterbit}, {max_deltaR_triggermatch}, {triggerobject_ptcut} )',
    input=[
        q.p4_1,
        nanoAOD.TriggerObject_bit,
        nanoAOD.TriggerObject_id,
        nanoAOD.TriggerObject_pt,
        nanoAOD.TriggerObject_eta,
        nanoAOD.TriggerObject_phi,
    ],
    output="flagname_1",
    scope=["mm"],
    vec_config="singlemuon_trigger_bit",  # works
)

MuMuSingleMuonTriggerBitFlags_2 = ExtendedVectorProducer(
    name="MuMuSingleMuonTriggerBitFlags_2",
    call='trigger::tagandprobe::MatchSingleTriggerObject({df}, {output}, {input}, {ptcut}, {etacut}, {trigger_particle_id}, {filterbit}, {max_deltaR_triggermatch}, {triggerobject_ptcut} )',
    input=[
        q.p4_2,
        nanoAOD.TriggerObject_bit,
        nanoAOD.TriggerObject_id,
        nanoAOD.TriggerObject_pt,
        nanoAOD.TriggerObject_eta,
        nanoAOD.TriggerObject_phi,
    ],
    output="flagname_2",
    scope=["mm"],
    vec_config="singlemuon_trigger_bit",  # works
)

## Producers to writeout the id variables for the tag and probe pairs
MuonID_Loose_1 = Producer(
    name="MuonID_Loose_1",
    call="quantities::muon::id({df}, {output}, 0, {input})",
    input=[q.dileptonpair, nanoAOD.Muon_id_loose],
    output=[tp_q.id_loose_1],
    scopes=["mm"],
)
MuonID_Loose_2 = Producer(
    name="MuonID_Loose_2",
    call="quantities::muon::id({df}, {output}, 1, {input})",
    input=[q.dileptonpair, nanoAOD.Muon_id_loose],
    output=[tp_q.id_loose_2],
    scopes=["mm"],
)
MuonID_Medium_1 = Producer(
    name="MuonID_Medium_1",
    call="quantities::muon::id({df}, {output}, 0, {input})",
    input=[q.dileptonpair, nanoAOD.Muon_id_medium],
    output=[tp_q.id_medium_1],
    scopes=["mm"],
)
MuonID_Medium_2 = Producer(
    name="MuonID_Medium_2",
    call="quantities::muon::id({df}, {output}, 1, {input})",
    input=[q.dileptonpair, nanoAOD.Muon_id_medium],
    output=[tp_q.id_medium_2],
    scopes=["mm"],
)
MuonID_Tight_1 = Producer(
    name="MuonID_Tight_1",
    call="quantities::muon::id({df}, {output}, 0, {input})",
    input=[q.dileptonpair, nanoAOD.Muon_id_tight],
    output=[tp_q.id_tight_1],
    scopes=["mm"],
)
MuonID_Tight_2 = Producer(
    name="MuonID_Tight_2",
    call="quantities::muon::id({df}, {output}, 1, {input})",
    input=[q.dileptonpair, nanoAOD.Muon_id_tight],
    output=[tp_q.id_tight_2],
    scopes=["mm"],
)
MuonIDs = ProducerGroup(
    name="MuonIDs",
    call=None,
    input=None,
    output=None,
    scopes=["mm"],
    subproducers=[
        MuonID_Loose_1,
        MuonID_Loose_2,
        MuonID_Medium_1,
        MuonID_Medium_2,
        MuonID_Tight_1,
        MuonID_Tight_2,
    ],
)
###########################
## Electrons
###########################

BaseElectrons = ProducerGroup(
    name="BaseElectrons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.base_electrons_mask],
    scopes=["global"],
    subproducers=[
        ElectronPtCut,
        ElectronEtaCut,
    ],
)

GoodElectrons = ProducerGroup(
    name="BaseElectrons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.good_electrons_mask],
    scopes=["ee"],
    subproducers=[
        GoodElectronPtCut,
        GoodElectronEtaCut,
    ],
)


ElElSingleElectronTriggerFlags_1 = ExtendedVectorProducer(
    name="ElElGenerateSingleElectronTriggerFlags_1",
    call='trigger::tagandprobe::GenerateSingleTriggerFlag({df}, {output}, {input}, "{hlt_path}", {ptcut}, {etacut}, {trigger_particle_id}, {filterbit}, {max_deltaR_triggermatch}, {triggerobject_ptcut} )',
    input=[
        q.p4_1,
        nanoAOD.TriggerObject_bit,
        nanoAOD.TriggerObject_id,
        nanoAOD.TriggerObject_pt,
        nanoAOD.TriggerObject_eta,
        nanoAOD.TriggerObject_phi,
    ],
    output="flagname_1",
    scope=["ee"],
    vec_config="singleelectron_trigger",
)
ElElSingleElectronTriggerFlags_2 = ExtendedVectorProducer(
    name="ElElGenerateSingleElectronTriggerFlags_2",
    call='trigger::tagandprobe::GenerateSingleTriggerFlag({df}, {output}, {input}, "{hlt_path}", {ptcut}, {etacut}, {trigger_particle_id}, {filterbit}, {max_deltaR_triggermatch}, {triggerobject_ptcut} )',
    input=[
        q.p4_2,
        nanoAOD.TriggerObject_bit,
        nanoAOD.TriggerObject_id,
        nanoAOD.TriggerObject_pt,
        nanoAOD.TriggerObject_eta,
        nanoAOD.TriggerObject_phi,
    ],
    output="flagname_2",
    scope=["ee"],
    vec_config="singleelectron_trigger",
)


## Producers to writeout the id variables for the tag and probe pairs
ElectronID_WP90_1 = Producer(
    name="ElectronID_WP90_1",
    call="quantities::muon::id({df}, {output}, 0, {input})",
    input=[q.dileptonpair, nanoAOD.Electron_IDWP90],
    output=[tp_q.id_wp90_1],
    scopes=["ee"],
)
ElectronID_WP90_2 = Producer(
    name="ElectronID_WP90_2",
    call="quantities::muon::id({df}, {output}, 1, {input})",
    input=[q.dileptonpair, nanoAOD.Electron_IDWP90],
    output=[tp_q.id_wp90_2],
    scopes=["ee"],
)
ElectronID_WP80_1 = Producer(
    name="ElectronID_WP80_1",
    call="quantities::muon::id({df}, {output}, 0, {input})",
    input=[q.dileptonpair, nanoAOD.Electron_IDWP80],
    output=[tp_q.id_wp80_1],
    scopes=["ee"],
)
ElectronID_WP80_2 = Producer(
    name="ElectronID_WP80_2",
    call="quantities::muon::id({df}, {output}, 1, {input})",
    input=[q.dileptonpair, nanoAOD.Electron_IDWP80],
    output=[tp_q.id_wp80_2],
    scopes=["ee"],
)
ElectronIDs = ProducerGroup(
    name="ElectronIDs",
    call=None,
    input=None,
    output=None,
    scopes=["ee"],
    subproducers=[
        ElectronID_WP90_1,
        ElectronID_WP90_2,
        ElectronID_WP80_1,
        ElectronID_WP80_2,
    ],
)

########################################
## FSR Photon Veto
########################################

FSR_Photon_Veto_1 = Producer(
    name="FSR_Photon_Veto_1",
    call="physicsobject::DeltaRParticleVeto({df}, {output}, {input}, {fsr_delta_r})",
    input=[
        q.p4_1,
        q.base_photons_mask,
        nanoAOD.Photon_pt,
        nanoAOD.Photon_eta,
        nanoAOD.Photon_phi,
        nanoAOD.Photon_mass,
    ],
    output=[tp_q.fsr_photon_veto_1],
    scopes=["ee", "mm"],
)

FSR_Photon_Veto_2 = Producer(
    name="FSR_Photon_Veto_1",
    call="physicsobject::DeltaRParticleVeto({df}, {output}, {input}, {fsr_delta_r})",
    input=[
        q.p4_2,
        q.base_photons_mask,
        nanoAOD.Photon_pt,
        nanoAOD.Photon_eta,
        nanoAOD.Photon_phi,
        nanoAOD.Photon_mass,
    ],
    output=[tp_q.fsr_photon_veto_2],
    scopes=["ee", "mm"],
)

FSR_Veto = ProducerGroup(
    name="FSR_Veto",
    call=None,
    input=None,
    output=None,
    scopes=["ee", "mm"],
    subproducers=[
        FSR_Photon_Veto_1,
        FSR_Photon_Veto_2,
    ],
)

"""Essais de la lecture des réponses des lecteurs du bras A, texte neuf (brouillon 5, 3.2, 3.3, 8.2, 8.4, 8.6) : forme,
redemande, extraits mot pour mot dans le champ de l'action, règle du champ court, traduction des clés de la couverture,
lecture stricte, actions porteuses, place. Réponses synthétiques seulement."""
import json

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import reponses_lecteurs_v1 as lr
from controle_ia.organismes_discrets.instrument_appariement_v1 import ChampsAppariement
from controle_ia.verite_dommage import artefacts_v1 as art

CH = ChampsAppariement(titre="Probing layer four of model B",
                       proposition="Train a linear probe on layer four activations of model B to detect negation.",
                       controles="Shuffled-label probe on the same layer; random-init model B as a second baseline.")


def rep(fit, spec=None, pq=None, cq=None):
    return json.dumps({"fit": fit, "specific": spec, "proposal_quote": pq, "controls_quote": cq})


# --- Appariement ---------------------------------------------------------------------------------------------------------

def test_forme_appariement_cas_sains():
    r = lr.lire_forme_appariement(rep("answers", True, "linear probe on layer four", "Shuffled-label probe on the same"))
    assert r.fit == "answers" and r.specific is True
    assert lr.lire_forme_appariement("  " + rep("cannot_tell") + "\n").fit == "cannot_tell"


@pytest.mark.parametrize("texte", [
    "pas du JSON", "```json\n" + rep("cannot_tell") + "\n```", "[1, 2]",
    rep("answers", None, "a" * 30, "b" * 30),                     # specific absent sous answers
    rep("does_not_answer", False, "a" * 30, "b" * 30),            # specific non nul hors answers
    rep("cannot_tell", None, "a" * 30, None),                     # extrait non nul sous cannot_tell
    rep("answers", True, None, "b" * 30),                         # extrait nul sous answers
    rep("perhaps", None, None, None),
    json.dumps({"fit": "cannot_tell", "specific": None, "proposal_quote": None}),
    json.dumps({"fit": "cannot_tell", "specific": None, "proposal_quote": None, "controls_quote": None, "x": 1}),
    '{"fit": "cannot_tell", "fit": "cannot_tell", "specific": null, "proposal_quote": null, "controls_quote": null}',
    rep("answers", "true", "a" * 30, "b" * 30),
])
def test_forme_appariement_artefacts(texte):
    with pytest.raises(lr.ErreurForme):
        lr.lire_forme_appariement(texte)


def test_extrait_dans_le_champ_de_l_action():
    """8.4, ligne 772 : extrait recopié du champ des contrôles (sain) ; extrait d'une autre action, extrait de la
    proposition donné pour les contrôles, 23 caractères d'un champ plus long (artefacts)."""
    sain = lr.verdict_appariement(lr.ReponseAppariement("does_not_answer", None, "linear probe on layer four",
                                                       "Shuffled-label   probe on the same layer"), CH)
    assert sain.verdict == lr.NE_REPOND_PAS
    autre_action = lr.ReponseAppariement("does_not_answer", None, "linear probe on layer four",
                                         "ablation of the attention heads of model C")
    assert lr.verdict_appariement(autre_action, CH).motif == "non etaye"
    croise = lr.ReponseAppariement("answers", True, "linear probe on layer four", "linear probe on layer four")
    assert lr.verdict_appariement(croise, CH).verdict == lr.SANS_VERDICT
    court = lr.ReponseAppariement("answers", True, "linear probe on layer four", CH.controles[:23])
    assert len(CH.controles[:23]) == 23 and lr.verdict_appariement(court, CH).motif == "non etaye"
    # l'extrait de la proposition peut venir du titre
    titre = lr.ReponseAppariement("answers", False, "Probing layer four of model B", "random-init model B as a second")
    v = lr.verdict_appariement(titre, CH)
    assert v.verdict == lr.REPOND and v.specifique is False


def test_regle_du_champ_court():
    """8.4, ligne 773 : champ de 20 caractères cité entier (sain) ; 20 caractères partiels d'un champ de 30 (artefact)."""
    champ20 = "Random baseline only"
    assert len(champ20) == 20
    assert lr.verifier_extrait_dans_champs("Random  baseline only", [champ20]).verifie
    assert lr.verifier_extrait_dans_champs("Random  baseline only", [champ20]).court
    champ30 = "Random baseline only, 3 seeds."
    assert len(champ30) == 30
    assert not lr.verifier_extrait_dans_champs(champ30[:20], [champ30]).verifie
    assert lr.verifier_extrait_dans_champs(champ30, [champ30]).verifie
    assert not lr.verifier_extrait_dans_champs("Random baseline", [champ20]).verifie   # partiel d'un champ court
    assert not lr.verifier_extrait_dans_champs("", [champ20]).verifie
    assert not lr.verifier_extrait_dans_champs(None, [champ20]).verifie


def test_extraits_longs_comptes_non_refuses():
    long = "x " * 200
    ch = ChampsAppariement("t" * 30, long + "fin", long)
    v = lr.verdict_appariement(lr.ReponseAppariement("answers", True, long, long), ch)
    assert v.verdict == lr.REPOND and v.extraits_longs == 2


def test_redemande_et_relecture():
    bonne, mauvaise = rep("cannot_tell"), "oops"
    assert lr.lire_appariement([bonne], CH).motif == "cannot_tell"
    v = lr.lire_appariement([mauvaise, bonne], CH)
    assert v.redemande and v.motif == "cannot_tell"
    v = lr.lire_appariement([mauvaise, mauvaise], CH)
    assert v.verdict == lr.SANS_VERDICT and v.motif == "forme" and v.redemande
    with pytest.raises(GardeArret):                 # seconde réponse après une réponse de forme : relecture
        lr.lire_appariement([bonne, bonne], CH)
    with pytest.raises(GardeArret):                 # réponse hors forme sans sa redemande
        lr.lire_appariement([mauvaise], CH)
    with pytest.raises(GardeArret):
        lr.lire_appariement([mauvaise, mauvaise, bonne], CH)


def test_garde_de_forme_du_lot():
    """8.4, ligne 786 : 0 % de lectures fautives (sain) ; 6 % (artefact)."""
    assert lr.exiger_forme_du_lot(0, 100) == 0.0
    assert lr.exiger_forme_du_lot(5, 100) == 0.05
    with pytest.raises(GardeArret):
        lr.exiger_forme_du_lot(6, 100)
    with pytest.raises(GardeArret):
        lr.exiger_forme_du_lot(3, 0)


# --- Couverture --------------------------------------------------------------------------------------------------------

SEGMENTS = [
    "ACTION: ADD\nTITLE: Probe B\nPROPOSAL: Train a linear probe on layer four of model B.\n"
    "CONTROLS: shuffled-label probe on the same layer\nCOST: 10\nPREDICTION: probe beats chance",
    "ACTION: ADD\nTITLE: Seeds\nPROPOSAL: Repeat the main run with three random seeds and report spread.\n"
    "CONTROLS: Random baseline only\nCOST: 5\nPREDICTION: low spread",
]


def couv(contenus):
    return json.dumps({k: {"content": c, "quote": q, "place": p} for k, (c, q, p) in contenus.items()})


def test_forme_et_traduction_couverture():
    r = couv({"c1": ("conforme", "shuffled-label probe on the same layer", "checks"),
              "c2": ("absent", None, None)})
    traduite, places = lr.lire_forme_couverture(r, ["c1", "c2"])
    assert traduite == {"c1": {"statut": "conforme", "extrait": "shuffled-label probe on the same layer"},
                        "c2": {"statut": "absent", "extrait": None}}
    assert places == {"c1": "checks", "c2": None}
    # la traduction donne exactement l'entrée qu'attend `lecture_stricte`
    lu = art.lecture_stricte(traduite, art.texte_du_plan(SEGMENTS), [{"id": "c1", "description": "x"},
                                                                    {"id": "c2", "description": "y"}], 24)
    assert lu["conformes"] == ["c1"]


@pytest.mark.parametrize("contenus,ids", [
    ({"c1": ("conforme", "q" * 30, "checks")}, ["c1", "c2"]),                 # identifiant manquant
    ({"c1": ("conforme", "q" * 30, "checks"), "c9": ("absent", None, None)}, ["c1"]),
    ({"c1": ("present", "q" * 30, "checks")}, ["c1"]),
    ({"c1": ("conforme", "q" * 30, "somewhere")}, ["c1"]),
    ({"c1": ("conforme", "q" * 30, None)}, ["c1"]),
    ({"c1": ("absent", None, "checks")}, ["c1"]),
    ({"c1": ("conforme", 12, "checks")}, ["c1"]),
])
def test_forme_couverture_artefacts(contenus, ids):
    with pytest.raises(lr.ErreurForme):
        lr.lire_forme_couverture(couv(contenus), ids)


def test_lecture_stricte_avec_champ_court_et_porteuses():
    traduite = {"c1": {"statut": "conforme", "extrait": "shuffled-label probe on the same layer"},
                "c2": {"statut": "altere", "extrait": "Random baseline only"},          # champ court cité entier
                "c3": {"statut": "conforme", "extrait": "Random baseline"},             # partiel d'un champ court
                "c4": {"statut": "conforme", "extrait": "beats chance\n\nACTION: ADD\nTITLE: Seeds"},  # à cheval
                "c5": {"statut": "conforme", "extrait": None},
                "c6": {"statut": "absent", "extrait": None}}
    lu = lr.lecture_stricte_couverture(traduite, SEGMENTS)
    c = lu["controles"]
    assert c["c1"]["statut_strict"] == "conforme" and c["c1"]["porteuses"] == [0]
    assert c["c2"]["statut_strict"] == "altere" and c["c2"]["court"] and c["c2"]["porteuses"] == [1]
    assert c["c3"]["statut_strict"] == "absent" and c["c3"]["etaye"] is False
    assert c["c4"]["statut_strict"] == "conforme" and c["c4"]["a_cheval"] and c["c4"]["porteuses"] == []
    assert c["c5"]["statut_strict"] == "absent" and c["c6"]["etaye"] is None
    assert lu["presents"] == ["c1", "c2", "c4"] and lu["non_etayes"] == ["c3", "c5"]


def test_champ_court_admet_le_champ_action():
    """Défaut signalé : à la lettre (« un champ d'une action »), la valeur « ADD » du champ ACTION est un extrait court
    admis ; la restriction aux champs porteurs d'un contrôle le refuse."""
    traduite = {"c1": {"statut": "conforme", "extrait": "ADD"}}
    assert lr.lecture_stricte_couverture(traduite, SEGMENTS)["controles"]["c1"]["statut_strict"] == "conforme"
    assert lr.lecture_stricte_couverture(traduite, SEGMENTS, ("TITLE", "PROPOSAL", "CONTROLS"))["presents"] == []


def test_equivalence_avec_lecture_stricte_sans_extrait_court():
    traduite = {"c1": {"statut": "conforme", "extrait": "shuffled-label probe on the same layer"},
                "c2": {"statut": "altere", "extrait": "Repeat the main run with three random"},
                "c3": {"statut": "conforme", "extrait": "this passage is nowhere in the plan"}}
    ref = [{"id": k, "description": "d"} for k in traduite]
    a = art.lecture_stricte(traduite, art.texte_du_plan(SEGMENTS), ref, 24)
    b = lr.lecture_stricte_couverture(traduite, SEGMENTS)
    assert a["presents"] == b["presents"] and a["conformes"] == b["conformes"] and a["non_etayes"] == b["non_etayes"]


def test_lecture_non_rendue_et_redemande():
    ids = ["c1", "c2"]
    lu, places = lr.lire_couverture(["oops", "encore"], ids, SEGMENTS)
    assert not lu["rendue"] and lu["presents"] == [] and lu["redemande"] and places == {"c1": None, "c2": None}
    bonne = couv({"c1": ("conforme", "shuffled-label probe on the same layer", "checks"), "c2": ("absent", None, None)})
    lu, places = lr.lire_couverture(["oops", bonne], ids, SEGMENTS)
    assert lu["rendue"] and lu["conformes"] == ["c1"] and places["c1"] == "checks"


def test_agregation_couverture():
    l1 = lr.lecture_stricte_couverture({"c1": {"statut": "conforme", "extrait": "shuffled-label probe on the same layer"},
                                        "c2": {"statut": "conforme", "extrait": "Random baseline only"}}, SEGMENTS)
    l2 = lr.lecture_stricte_couverture({"c1": {"statut": "altere", "extrait": "shuffled-label probe on the same layer"},
                                        "c2": {"statut": "conforme", "extrait": "absent passage of the plan here"}},
                                       SEGMENTS)
    ag = lr.agreger_couverture(l1, {"c1": "checks", "c2": "general"}, l2, {"c1": "general", "c2": "general"})
    assert ag["c1"]["statut_retenu"] == "altere" and ag["c1"]["place_retenue"] == "discordante"
    assert ag["c2"]["statut_retenu"] == "absent" and ag["c2"]["place_retenue"] is None
    assert ag["c2"]["places"] == ("general", None)
    with pytest.raises(GardeArret):
        lr.agreger_couverture(l1, {}, lr.lecture_non_rendue(["c9"]), {})

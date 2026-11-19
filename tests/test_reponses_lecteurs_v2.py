"""Essais des réponses des lecteurs du bras A, version 2 du code (brouillon 6, 3.2 et 3.3 ; gardes de 8.4 « forme des
réponses », « extrait dans le champ de l'action », « règle du champ court », « forme ») sur réponses fabriquées : chaque
garde sur un cas sain et sur un artefact. Aucun appel, aucune réponse réelle."""
import json

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import instrument_appariement_v2 as ia
from controle_ia.organismes_discrets import reponses_lecteurs_v2 as rl

STRICT = ia.Reglages()
TOLERANT = ia.Reglages(bloc_de_code_autour_de_la_reponse=ia.RETIRE_ET_COMPTE)
CH = ia.ChampsAppariement("Effet de la taille du lot sur M3", "Entraîner le modèle M3 sur le jeu D3 et mesurer la métrique K3 à trois tailles de lot.",
                          "Base aléatoire sur D3 ; ablation de la couche 3 de M3 ; trois graines par taille de lot.")
PQ, CQ = "mesurer la métrique K3 à trois tailles", "ablation de la couche 3 de M3"


def rep(fit="answers", specific=True, pq=PQ, cq=CQ, **plus):
    return json.dumps({"fit": fit, "specific": specific, "proposal_quote": pq, "controls_quote": cq, **plus})


# --- Forme de l'appariement ---------------------------------------------------------------------------------------------

def test_forme_cas_sains_et_champs_sans_emploi():
    r = rl.lire_forme_appariement("  \n" + rep() + "\n\t ", STRICT)                      # objet entouré de blancs
    assert (r.fit, r.specific, r.champs_ignores, r.bloc_retire) == ("answers", True, (), False)
    r = rl.lire_forme_appariement(rep("does_not_answer", False), STRICT)                 # `specific` non nul : ignoré, compté
    assert r.fit == "does_not_answer" and r.specific is None and r.champs_ignores == ("specific",)
    r = rl.lire_forme_appariement(rep("cannot_tell", True, "un extrait", 3), STRICT)     # trois champs sans emploi
    assert r.proposal_quote is None and r.controls_quote is None and len(r.champs_ignores) == 3
    assert rl.lire_forme_appariement(rep("cannot_tell", None, None, None), STRICT).champs_ignores == ()
    assert rl.lire_forme_appariement(rep(pq=""), STRICT).proposal_quote == ""            # extrait vide : de forme exigée
    v = rl.lire_appariement([rep("does_not_answer", True)], CH, STRICT)
    assert v.verdict == rl.NE_REPOND_PAS and v.champs_ignores == 1 and not v.redemande   # aucune redemande pour ce champ


@pytest.mark.parametrize("fautive", [
    "```json\n" + rep() + "\n```",                                                       # objet dans un bloc de code
    "Here is my answer: " + rep(), rep() + "\nI hope this helps.", rep() + rep(),        # phrase ; second objet
    '{"fit": "answers", "fit": "answers", "specific": true, "proposal_quote": "a", "controls_quote": "b"}',   # clé en double
    rep(confidence=0.9),                                                                 # clé en trop
    json.dumps({"fit": "answers", "specific": True, "proposal_quote": PQ}),              # clé manquante
    rep("maybe"), rep(["answers"]), rep(specific=None), rep(specific="true"), rep(specific=1),
    rep(pq=None), rep("does_not_answer", None, PQ, None), rep(cq=["a"]), "[]", "", "null", rep()[:-5],
])
def test_fautes_de_forme(fautive):
    with pytest.raises(rl.ErreurForme):
        rl.lire_forme_appariement(fautive, STRICT)


def test_bloc_de_code_option_b():
    """Point 7 de la section 12 : option (a) par défaut, le bloc est une faute ; option (b), fixée à la configuration,
    un seul bloc autour de l'objet est retiré avant la lecture et compté."""
    bloc = "```json\n" + rep() + "\n```"
    r = rl.lire_forme_appariement(bloc, TOLERANT)
    assert r.fit == "answers" and r.bloc_retire
    assert rl.lire_forme_appariement("```\n" + rep() + "\n```\n", TOLERANT).bloc_retire
    assert not rl.lire_forme_appariement(rep(), TOLERANT).bloc_retire
    assert rl.lire_appariement([bloc], CH, TOLERANT).bloc_retire
    for fautive in ("Voici :\n" + bloc, bloc + "\nfin", bloc + "\n" + bloc, "```json\n" + rep() + rep() + "\n```", "``" + rep() + "``"):
        with pytest.raises(rl.ErreurForme):
            rl.lire_forme_appariement(fautive, TOLERANT)
    v = rl.lire_appariement([bloc, bloc], CH, STRICT)                                    # strict : redemandée, puis sans verdict
    assert v.verdict == rl.SANS_VERDICT and v.motif == "forme" and v.redemande


def test_redemande_reprise_relecture():
    v = rl.lire_appariement(["pas du json", rep()], CH, STRICT)                          # redemande : la première de forme compte
    assert v.verdict == rl.REPOND and v.redemande and v.specifique is True
    with pytest.raises(GardeArret):
        rl.lire_appariement([rep(), rep("does_not_answer", None)], CH, STRICT)           # relecture interdite
    with pytest.raises(GardeArret):
        rl.lire_appariement(["pas du json"], CH, STRICT)                                 # redemande due
    with pytest.raises(GardeArret):
        rl.lire_appariement(["x", "y", rep()], CH, STRICT)                               # seconde redemande
    with pytest.raises(GardeArret):
        rl.lire_appariement([], CH, STRICT)


# --- Extraits ----------------------------------------------------------------------------------------------------------

def test_extrait_dans_le_champ_de_l_action():
    assert rl.lire_appariement([rep()], CH, STRICT).verdict == rl.REPOND                 # extraits recopiés de leur champ
    assert rl.lire_appariement([rep(specific=False)], CH, STRICT).specifique is False
    assert rl.lire_appariement([rep(cq="ablation de la\n couche 3   de M3 ; trois")], CH, STRICT).verdict == rl.REPOND   # espaces
    for pq, cq in ((PQ, "ablation de la couche 7 de M7 sur D7"),                         # extrait présent dans une autre action
                   (PQ, PQ),                                                             # extrait de la proposition donné pour les contrôles
                   (CQ, CQ),                                                             # et l'inverse
                   (PQ, "ablation de la couche 3"),                                      # 23 caractères d'un champ qui en compte plus
                   (PQ, "Ablation de la couche 3 de M3"), (PQ, ""),                      # casse changée ; extrait vide
                   ("Effet de la taille du lot sur M3 Entraîner le modèle", CQ)):        # à cheval sur le titre et la proposition
        v = rl.lire_appariement([rep(pq=pq, cq=cq)], CH, STRICT)
        assert v.verdict == rl.SANS_VERDICT and v.motif == "non etaye"
    assert len("ablation de la couche 3") == 23
    v = rl.lire_appariement([rep(pq="Effet de la taille du lot sur M3")], CH, STRICT)    # le titre est un champ permis
    assert v.verdict == rl.REPOND
    assert rl.lire_appariement([rep("cannot_tell", None, None, None)], CH, STRICT).motif == "cannot_tell"


def test_regle_du_champ_court_de_l_appariement():
    court = ia.ChampsAppariement("Titre de vingt signe", CH.proposition, "Vingt signes exacts.")
    assert len(court.titre) == len(court.controles) == 20
    v = rl.lire_appariement([rep(pq="Titre de vingt signe", cq=" Vingt signes  exacts. ")], court, STRICT)   # champ court cité entier
    assert v.verdict == rl.REPOND and v.extraits_courts == 2
    trente = ia.ChampsAppariement("", CH.proposition, "Trente signes exactement, oui.")
    assert len(trente.controles) == 30
    for cq in ("Trente signes exacte", "Vingt signes"):                                  # 20 caractères partiels d'un champ de 30
        assert rl.lire_appariement([rep(cq=cq)], trente, STRICT).motif == "non etaye"
    assert rl.lire_appariement([rep(cq="Vingt signes")], court, STRICT).motif == "non etaye"   # partiel d'un champ court
    assert rl.lire_appariement([rep(pq="Vingt signes exacts.", cq="Vingt signes exacts.")], court, STRICT).motif == "non etaye"


def test_extrait_long_compte_jamais_refuse():
    long = ia.ChampsAppariement("t", "p " * 200, CH.controles)
    v = rl.lire_appariement([rep(pq="p " * 160)], long, STRICT)
    assert v.verdict == rl.REPOND and v.extraits_longs == 1


def test_garde_de_forme_du_lot():
    assert rl.exiger_forme_du_lot(0, 200) == 0.0                                         # 0 % de lectures fautives
    assert rl.exiger_forme_du_lot(10, 200) == 0.05                                       # 5 % exactement : pas « plus de »
    with pytest.raises(GardeArret):
        rl.exiger_forme_du_lot(12, 200)                                                  # 6 %
    with pytest.raises(GardeArret):
        rl.exiger_forme_du_lot(3, 2)


# --- Couverture ----------------------------------------------------------------------------------------------------------

def act(i, titre=None, controles=None):
    return (f"ACTION: ADD\nTITLE: {titre or f'Expérience {i} sur le modèle M{i}'}\nPROPOSAL: Entraîner le modèle M{i} sur le jeu D{i} "
            f"et mesurer la métrique K{i}.\nCONTROLS: {controles or f'Base aléatoire sur D{i} ; ablation de la couche {i} de M{i}.'}\n"
            f"COST: {i + 1}\nPREDICTION: hausse de K{i}\n")


SEG = [act(0), act(1, titre="Titre de vingt signe"), act(2, controles="Trois graines. "), act(3)]
IDS = ["c1", "c2", "c3"]


def cou(**valeurs):
    base = {i: {"content": "absent", "quote": None, "place": None} for i in IDS}
    base.update(valeurs)
    return json.dumps(base)


def un(content="conforme", quote="ablation de la couche 0 de M0", place="checks"):
    return {"content": content, "quote": quote, "place": place}


def test_forme_de_la_couverture():
    t, places, comptes = rl.lire_forme_couverture(" " + cou(c1=un()) + "\n", IDS, STRICT)
    assert t["c1"] == {"statut": "conforme", "extrait": "ablation de la couche 0 de M0"} and places == {"c1": "checks", "c2": None, "c3": None}
    assert comptes == {"champs_ignores": 0, "bloc_retire": False}
    t, places, comptes = rl.lire_forme_couverture(cou(c2=un("absent", "un extrait", "general"), c3=un("absent", None, "checks")), IDS, STRICT)
    assert comptes["champs_ignores"] == 3 and t["c2"]["extrait"] is None and places["c2"] is None    # ignorés, comptés
    for fautive in (cou(c1=un(place=None)),                                              # place nulle sous « conforme »
                    cou(c1=un("altere", place=None)), cou(c1=un(quote=None)),            # extrait nul sous « conforme »
                    cou(c1=un(place="elsewhere")), cou(c1=un("present")), cou(c4=un()),  # identifiant en trop
                    json.dumps({"c1": un(), "c2": un()}),                                # identifiant manquant
                    cou(c1=dict(un(), note="x")), cou(c1={"content": "absent"}), cou(c1="conforme"),
                    '{"c1": {"content": "absent", "quote": null, "place": null}, "c1": {"content": "absent", "quote": null, '
                    '"place": null}, "c2": {"content": "absent", "quote": null, "place": null}, "c3": {"content": "absent", '
                    '"quote": null, "place": null}}',                                    # identifiant en double
                    "```json\n" + cou(c1=un()) + "\n```", "The plan covers: " + cou()):
        with pytest.raises(rl.ErreurForme):
            rl.lire_forme_couverture(fautive, IDS, STRICT)
    assert rl.lire_forme_couverture("```json\n" + cou(c1=un()) + "\n```", IDS, TOLERANT)[2]["bloc_retire"]


def test_statut_strict_et_regle_du_champ_court_de_la_couverture():
    lu, places = rl.lire_couverture([cou(c1=un(), c2=un("altere", "Titre de vingt signe", "general"),
                                         c3=un("conforme", "Trois   graines.", "checks"))], IDS, SEG, STRICT)
    c = lu["controles"]
    assert c["c1"]["statut_strict"] == "conforme" and c["c1"]["porteuses"] == [0] and not c["c1"]["court"]
    assert c["c2"]["statut_strict"] == "altere" and c["c2"]["court"] and c["c2"]["porteuses"] == [1]   # `TITLE` court cité entier
    assert c["c3"]["statut_strict"] == "conforme" and c["c3"]["court"] and c["c3"]["porteuses"] == [2]  # `CONTROLS` court
    assert lu["presents"] == IDS and lu["rendue"] and places["c2"] == "general"
    lu, _ = rl.lire_couverture([cou(c1=un(quote="ADD"), c2=un(quote="3"), c3=un(quote="hausse de K2"))], IDS, SEG, STRICT)
    assert lu["presents"] == [] and lu["courts_refuses"] == IDS                          # `ACTION`, `COST`, `PREDICTION` : refusés, comptés à part
    assert all(lu["controles"][i]["etaye"] is False for i in IDS)
    lu, _ = rl.lire_couverture([cou(c1=un(quote="Titre de vingt"), c2=un(quote="ablation de la couche 0"),
                                    c3=un(quote="ablation de la couche 9 de M9"))], IDS, SEG, STRICT)
    assert lu["presents"] == [] and lu["courts_refuses"] == [] and lu["non_etayes"] == IDS   # partiel ; 23 caractères ; introuvable
    a_cheval = "hausse de K0 ACTION: ADD TITLE: Titre de vingt signe"
    lu, _ = rl.lire_couverture([cou(c1=un(quote=a_cheval))], IDS, SEG, STRICT)
    assert lu["controles"]["c1"]["statut_strict"] == "conforme" and lu["a_cheval"] == ["c1"] and lu["controles"]["c1"]["porteuses"] == []


def test_reponse_non_rendue_et_agregation():
    lu, places = rl.lire_couverture(["non", "toujours pas"], IDS, SEG, STRICT)
    assert not lu["rendue"] and lu["redemande"] and lu["presents"] == [] and places == {i: None for i in IDS}
    assert all(c["statut_strict"] == "absent" for c in lu["controles"].values())
    l1, p1 = rl.lire_couverture([cou(c1=un(), c2=un(place="general"), c3=un())], IDS, SEG, STRICT)
    l2, p2 = rl.lire_couverture([cou(c1=un("altere"), c2=un(place="cannot_check"), c3=un(quote="introuvable dans le plan, vraiment"))],
                                IDS, SEG, STRICT)
    ag = rl.agreger_couverture(l1, p1, l2, p2)
    assert ag["c1"]["statut_retenu"] == "altere" and ag["c1"]["place_retenue"] == "checks"     # le plus sévère
    assert ag["c2"]["statut_retenu"] == "conforme" and ag["c2"]["place_retenue"] == "discordante"
    assert ag["c3"]["statut_retenu"] == "absent" and ag["c3"]["place_retenue"] is None and ag["c3"]["places"] == ("checks", None)
    with pytest.raises(GardeArret):
        rl.agreger_couverture(l1, p1, rl.reponse_non_rendue(["c1"]), {})

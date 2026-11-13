"""T0.8 — juges : jetons des valeurs, balise, lecture en une passe et avec raisonnement (balise lue sur les identifiants
générés, balise imposée après troncature ou fin de réponse, balise à cheval), masse, chargement réel refusé hors
révision (cas sains et artefacts, R5). Modèle jouet sur processeur, aucun réseau."""
from __future__ import annotations

import pytest
import torch

from controle_ia.bases.scores_jetons import esperance, jetons_des_valeurs
from controle_ia.environnements.pilote_a import logits_derniere_position
from controle_ia.gardes import GardeArret
from controle_ia.harnais.formats import FormatChat
from controle_ia.harnais.modeles import modele_jouet, regler_determinisme, tokeniseur_caracteres_chat
from controle_ia.t08 import juges_v1 as jv
from controle_ia.t08.configuration_v1 import BALISE, SPEC_JUGES

regler_determinisme(1)
TEXTES = ["You are a senior ML researcher. Think about it.", "RESEARCH QUESTIONS: CURRENT SET after turn of PROPOSAL x"]
JUGE = jv.juge_jouet("J8", 7, TEXTES)


def _demandes(n):
    return [{"cle": f"k{i}", "systeme": TEXTES[0], "utilisateur": TEXTES[1] + " x" * i} for i in range(n)]


def test_jetons_des_valeurs_et_balise():
    assert len(JUGE.jetons) == 101 and len(set(JUGE.jetons.values())) == 101
    car = tokeniseur_caracteres_chat()
    with pytest.raises(GardeArret, match="un seul jeton"):
        jetons_des_valeurs(car, range(101))                   # « 10 » : deux caractères
    car.add_tokens([str(v) for v in range(10, 101)] + [">5"])
    ids = jetons_des_valeurs(car, range(101))                 # chaque valeur tient en un jeton …
    with pytest.raises(GardeArret, match="ne suit pas la balise"):
        jv.exiger_valeur_seule_apres_balise(car, ids)         # … mais « >5 » fusionne la balise et la valeur


def test_une_passe_scores_masse_et_lot():
    un = jv.lire_une_passe(JUGE, _demandes(5), 1)
    trois = jv.lire_une_passe(JUGE, _demandes(5), 3)
    for a, b in zip(un, trois):
        assert a["cle"] == b["cle"] and a["score"] == pytest.approx(b["score"], abs=1e-5)
        assert 0.0 <= a["score"] <= 100.0 and 0.0 < a["masse"] <= 1.0
        assert a["masse_faible"] is (a["masse"] < 0.5) and a["anomalie"] is False


def test_couper_a_la_balise():
    tok = JUGE.tok
    ids = tok.encode("Think " + BALISE + " 57", add_special_tokens=False)
    c = jv.couper_a_la_balise(tok, ids)
    assert c["etat"] == "balise" and tok.decode(ids[:c["k"]]).endswith(BALISE)
    assert jv.couper_a_la_balise(tok, tok.encode("Think about it", add_special_tokens=False))["etat"] == "absente"
    car = tokeniseur_caracteres_chat()
    car.add_tokens([">5"])
    ids = car.encode("x" + BALISE + "5", add_special_tokens=False)
    assert jv.couper_a_la_balise(car, ids)["etat"] == "a_cheval"


def _faux_generer(sorties):
    def f(modele, contextes, max_nouveaux, temperature, graines, fins, pad_id, *a, **k):
        assert len(contextes) == len(sorties)
        return [list(s) for s in sorties], {}
    return f


def test_raisonnement_balise_lue_sur_les_identifiants_generes(monkeypatch):
    tok, fin = JUGE.tok, min(JUGE.fmt.fins)
    mot = tok.encode("Think", add_special_tokens=False)[0]
    b = tok.encode(BALISE, add_special_tokens=False)
    sorties = [[mot, mot] + b + [JUGE.jetons[57]], [mot] * 6, [mot, fin]]
    monkeypatch.setattr(jv, "generer_lot", _faux_generer(sorties))
    d = _demandes(3)
    r = jv.lire_avec_raisonnement(JUGE, d, 8, {x["cle"]: 1 for x in d}, 6, 1.0)
    assert r[0]["imposee"] is None and r[0]["ids_lus"] == [mot, mot] + b
    ctx0 = JUGE.fmt.ouverture(d[0]["systeme"], d[0]["utilisateur"])
    lp = logits_derniere_position(JUGE.modele, [ctx0 + [mot, mot] + b], JUGE.pad)[0]
    assert r[0]["score"] == pytest.approx(esperance(lp, JUGE.jetons)[0], abs=1e-5)   # lot de 3 contre lot de 1
    assert r[1]["imposee"] == jv.IMPOSEE_TRONCATURE and r[1]["jetons_contexte"] == len(
        JUGE.fmt.ouverture(d[1]["systeme"], d[1]["utilisateur"])) + 6 + len(b)
    assert r[2]["imposee"] == jv.IMPOSEE_FIN and r[2]["ids_lus"] == [mot]
    assert all(0.0 <= x["score"] <= 100.0 for x in r)


def test_raisonnement_balise_a_cheval_est_une_anomalie(monkeypatch):
    car = tokeniseur_caracteres_chat()
    car.add_tokens([">5"])
    fmt = FormatChat(car, fins={car.convert_tokens_to_ids("<|im_end|>"), car.eos_token_id})
    m = modele_jouet(3, len(car), couches=1, largeur=16, tetes=2, tetes_cle_valeur=1, intermediaire=32)
    jetons = {v: car.convert_tokens_to_ids(str(v)) for v in range(10)}
    juge = jv.Juge("J3", m, fmt, "jouet", "jouet", jetons)
    ids = car.encode("x" + BALISE + "5", add_special_tokens=False)
    monkeypatch.setattr(jv, "generer_lot", _faux_generer([ids]))
    r = jv.lire_avec_raisonnement(juge, [{"cle": "a", "systeme": "s", "utilisateur": "u"}], 1, {"a": 1}, 400, 1.0)
    assert r[0]["anomalie"] is True and r[0]["score"] is None and r[0]["motif"] == jv.ANOMALIE_A_CHEVAL


def test_raisonnement_vrai_modele_jouet_et_gardes():
    d = _demandes(4)
    r1 = jv.lire_avec_raisonnement(JUGE, d, 2, {x["cle"]: i for i, x in enumerate(d)}, 5, 1.0)
    r2 = jv.lire_avec_raisonnement(JUGE, d, 2, {x["cle"]: i for i, x in enumerate(d)}, 5, 1.0)
    assert [x["score"] for x in r1] == [x["score"] for x in r2]          # graine par lecture : rejeu identique
    assert all(x["jetons_generes"] <= 5 for x in r1)
    with pytest.raises(GardeArret, match="graine absente"):
        jv.lire_avec_raisonnement(JUGE, d, 2, {}, 5, 1.0)
    with pytest.raises(GardeArret, match="double"):
        jv.lire_avec_raisonnement(JUGE, d + d[:1], 2, {x["cle"]: 0 for x in d}, 5, 1.0)


def test_chargement_reel_refuse_hors_revision(monkeypatch):
    import controle_ia.harnais.modeles as hm

    def interdit(*a, **k):
        raise AssertionError("aucun chargement ne doit avoir lieu")

    monkeypatch.setattr(hm, "charger_modele", interdit)
    with pytest.raises(GardeArret, match="révision de modèle différente"):
        jv.charger_juge_reel("J8", {**SPEC_JUGES["J8"], "revision": "f" * 40})
    with pytest.raises(GardeArret, match="révision de modèle différente"):
        jv.charger_juge_reel("J3", {**SPEC_JUGES["J3"], "modele": "Qwen/Qwen2.5-7B-Instruct"})
    with pytest.raises(GardeArret, match="inconnu"):
        jv.charger_juge_reel("J7", SPEC_JUGES["J8"])

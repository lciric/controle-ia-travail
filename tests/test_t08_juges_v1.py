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


def _faux_generer(sorties, appliquer_arret=True):
    """Faux générateur : rend `sorties`, coupées comme le ferait le critère d'arrêt à la balise (sauf artefact)."""
    def f(modele, contextes, max_nouveaux, temperature, graines, fins, pad_id, arret=None, *a, **k):
        assert len(contextes) == len(sorties)
        rendus = []
        for s in sorties:
            s = list(s)
            if appliquer_arret and arret is not None:
                k_ = next((j for j in range(1, len(s) + 1) if arret(s[:j])), None)
                s = s if k_ is None else s[:k_]
            rendus.append(s)
        return rendus, {}
    return f


def test_raisonnement_balise_lue_sur_les_identifiants_generes(monkeypatch):
    tok, fin = JUGE.tok, min(JUGE.fmt.fins)
    mot = tok.encode("Think", add_special_tokens=False)[0]
    b = tok.encode(BALISE, add_special_tokens=False)
    sorties = [[mot, mot] + b + [JUGE.jetons[57]], [mot] * 6, [mot, fin]]
    monkeypatch.setattr(jv, "generer_lot_jusqua_balise", _faux_generer(sorties))
    d = _demandes(3)
    r = jv.lire_avec_raisonnement(JUGE, d, 8, {x["cle"]: 1 for x in d}, 6, 1.0)
    assert r[0]["imposee"] is None and r[0]["ids_lus"] == [mot, mot] + b
    assert r[0]["jetons_generes"] == 2 + len(b)                         # génération arrêtée à la balise (CLT8C-18)
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
    monkeypatch.setattr(jv, "generer_lot_jusqua_balise", _faux_generer([ids]))
    r = jv.lire_avec_raisonnement(juge, [{"cle": "a", "systeme": "s", "utilisateur": "u"}], 1, {"a": 1}, 400, 1.0)
    assert r[0]["anomalie"] is True and r[0]["score"] is None and r[0]["motif"] == jv.ANOMALIE_A_CHEVAL


def test_raisonnement_generation_poursuivie_au_dela_de_la_balise_arrete(monkeypatch):
    """Garde du critère d'arrêt (CLT8C-18) : cas sain ci-dessus ; artefact : un générateur qui poursuit au-delà de la
    balise (critère d'arrêt non tenu) arrête la lecture."""
    tok = JUGE.tok
    mot = tok.encode("Think", add_special_tokens=False)[0]
    b = tok.encode(BALISE, add_special_tokens=False)
    monkeypatch.setattr(jv, "generer_lot_jusqua_balise",
                        _faux_generer([[mot] + b + [JUGE.jetons[3]]], appliquer_arret=False))
    d = _demandes(1)
    with pytest.raises(GardeArret, match="au-delà de la balise"):
        jv.lire_avec_raisonnement(JUGE, d, 1, {d[0]["cle"]: 1}, 6, 1.0)


def test_generation_sans_arret_egale_a_generer_lot_du_harnais():
    """La copie de `harnais.episode.generer_lot` rend exactement ses jetons quand le critère d'arrêt ne joue jamais."""
    from controle_ia.harnais.episode import generer_lot

    d = _demandes(5)
    ctx = [JUGE.fmt.ouverture(x["systeme"], x["utilisateur"]) for x in d]
    a, pa = generer_lot(JUGE.modele, ctx, 12, 1.0, [11, 12, 13, 14, 15], JUGE.fmt.fins, JUGE.pad)
    b, pb = jv.generer_lot_jusqua_balise(JUGE.modele, ctx, 12, 1.0, [11, 12, 13, 14, 15], JUGE.fmt.fins, JUGE.pad,
                                         lambda ids: False)
    assert a == b and pa["passes_decodage"] == pb["passes_decodage"] and not any(pb["arretees_a_la_balise"])


def test_raisonnement_arrete_a_la_balise_meme_valeur_moins_de_jetons():
    """CLT8C-18, sur le modèle jouet : la génération arrêtée à la balise rend la même valeur lue qu'avant (génération
    complète par `harnais.episode.generer_lot`, coupée à la balise, lue au même point) et moins de jetons générés."""
    from controle_ia.harnais.episode import generer_lot

    d, lot, n = _demandes(8), 4, 40
    graines = {x["cle"]: 100 + i for i, x in enumerate(d)}
    nouveau = jv.lire_avec_raisonnement(JUGE, d, lot, graines, n, 1.0)
    avant, plus_court = [], 0
    for debut in range(0, len(d), lot):
        morceau = d[debut:debut + lot]
        ctx = [JUGE.fmt.ouverture(x["systeme"], x["utilisateur"]) for x in morceau]
        gen, _ = generer_lot(JUGE.modele, ctx, n, 1.0, [graines[x["cle"]] for x in morceau], JUGE.fmt.fins, JUGE.pad)
        for x, c0, ids in zip(morceau, ctx, gen):
            coupe = jv.couper_a_la_balise(JUGE.tok, ids)
            avant.append({"cle": x["cle"], "etat": coupe["etat"], "k": coupe["k"], "jetons": len(ids), "c0": c0,
                          "ids": ids})
    assert any(a["etat"] == "balise" for a in avant)
    for a, r in zip(avant, nouveau):
        assert a["cle"] == r["cle"]
        if a["etat"] == "balise":
            assert r["ids_lus"] == a["ids"][:a["k"]] and r["jetons_generes"] == a["k"] <= a["jetons"]
            lp = logits_derniere_position(JUGE.modele, [a["c0"] + a["ids"][:a["k"]]], JUGE.pad)[0]
            assert r["score"] == pytest.approx(esperance(lp, JUGE.jetons)[0], abs=1e-5)       # même valeur lue
            plus_court += a["k"] < a["jetons"]
        else:
            assert r["jetons_generes"] == a["jetons"] and r["imposee"] is not None
    assert plus_court >= 1                                                                    # moins de jetons générés


def test_demandes_au_juge_ne_portent_que_trois_cles():
    """CLT8C-15 : une demande ne porte que `cle`, `systeme`, `utilisateur` ; un champ de condition (ou tout autre) est
    refusé avant tout appel au modèle."""
    d = _demandes(2)
    jv.exiger_demandes_juge(d)                                                     # cas sain
    for champ in ("condition", "episode", "dose", "pas"):
        with pytest.raises(GardeArret, match="seules"):
            jv.lire_une_passe(JUGE, [{**d[0], champ: "S100"}], 1)
        with pytest.raises(GardeArret, match="seules"):
            jv.lire_avec_raisonnement(JUGE, [{**d[0], champ: "S100"}], 1, {d[0]["cle"]: 1}, 3, 1.0)
    with pytest.raises(GardeArret, match="double"):
        jv.lire_une_passe(JUGE, d + d[:1], 1)


def test_progression_par_tranche_de_lots():
    """CLT8C-11 : une ligne de progression par tranche de dix lots (et au dernier lot) ; même lecture qu'en un appel."""
    vus = []
    d = _demandes(25)
    avec = jv.lire_une_passe(JUGE, d, 2, progres=lambda f, p: vus.append((f, p)))
    from controle_ia.bases.scores_jetons import scores_moniteur

    un_appel = scores_moniteur(JUGE.modele, JUGE.fmt, [{**x, "reponse_imposee": BALISE} for x in d], JUGE.jetons, 2, 0.0)
    assert vus == [(10, 13), (13, 13)] and [x["score"] for x in avec] == [x["score"] for x in un_appel]
    vus.clear()
    jv.lire_avec_raisonnement(JUGE, d[:5], 1, {x["cle"]: 1 for x in d[:5]}, 2, 1.0,
                              progres=lambda f, p: vus.append((f, p)))
    assert vus == [(5, 5)]


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
    # CLT8C-06 : gabarit et texte d'ouverture comparés aussi, avant tout chargement
    with pytest.raises(GardeArret, match="variables_gabarit"):
        jv.charger_juge_reel("J8", {**SPEC_JUGES["J8"], "variables_gabarit": {"date_string": "27 Jul 2024"}})
    with pytest.raises(GardeArret, match="texte_attendu_ouverture"):
        jv.charger_juge_reel("J3", {**SPEC_JUGES["J3"], "texte_attendu_ouverture": "Today Date: 27 Jul 2024"})


GABARIT_DATE = "{% if date_string is defined %}Today Date: {{ date_string }}\n{% endif %}"


def _tok_date(avec_date: bool):
    """Tokeniseur par caractères, valeurs 10 à 100 en jetons, gabarit jouet précédé (ou non) de la date d'en-tête."""
    from controle_ia.harnais.modeles import GABARIT_JOUET

    car = tokeniseur_caracteres_chat()
    car.add_tokens([str(v) for v in range(10, 101)])
    car.chat_template = (GABARIT_DATE if avec_date else "") + GABARIT_JOUET
    return car


@pytest.mark.parametrize("avec_date", [True, False])
def test_chargement_reel_controle_le_texte_d_ouverture(monkeypatch, avec_date):
    """CLT8C-09 (`juges_v1.charger_juge_reel`, texte d'ouverture) : cas sain, le gabarit rend « Today Date: 26 Jul
    2024 » et le juge est préparé ; artefact, un gabarit qui ne lit pas la variable de date : arrêt. Chargement remplacé
    par un modèle jouet (aucun réseau), mode hors ligne exigé."""
    import controle_ia.harnais.modeles as hm

    tok = _tok_date(avec_date)
    vus = {}

    def faux(nom, revision, dtype, appareil, attention, hors_ligne=False, **k):
        vus.update({"nom": nom, "revision": revision, "dtype": dtype, "hors_ligne": hors_ligne})
        return modele_jouet(5, len(tok), couches=1, largeur=16, tetes=2, tetes_cle_valeur=1, intermediaire=32), tok

    monkeypatch.setattr(hm, "charger_modele", faux)
    if avec_date:
        j = jv.charger_juge_reel("J8", SPEC_JUGES["J8"])
        assert j.revision == SPEC_JUGES["J8"]["revision"] and len(j.jetons) == 101
        assert vus == {"nom": SPEC_JUGES["J8"]["modele"], "revision": SPEC_JUGES["J8"]["revision"], "dtype": "bfloat16",
                       "hors_ligne": True}
    else:
        with pytest.raises(GardeArret, match="ouverture sans"):
            jv.charger_juge_reel("J8", SPEC_JUGES["J8"])

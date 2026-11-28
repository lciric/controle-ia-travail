"""Lanceur de l'étape du plan B des juges (T0.5) sur un pilote jouet arrêté pendant ses notations décisives et un run
des notations H.4 jouet : gardes d'avant le manifeste, requalification RS1 et garde en ligne (règle k(n − 1)), rejeu
(graines, reproduction, simple précision, réglages relus, palier du chemin, D1, classement des dépassements, ancrage
couche par couche, couverture, repère), témoin (configuration remplacée, « témoin impossible », pannes propagées, queues
binomiales), tirage sur le processeur, mémoire, échéances et signal TERM. Chaque garde sur un cas sain et sur un
artefact (R5).

Tests sensibles au matériel (leçon de R-132 et R-133), signalés dans leur docstring (« SENSIBLE AU MATÉRIEL ») : ils
lisent des écarts numériques du modèle jouet (simple précision et bfloat16 sur le processeur, noyaux d'attention de la
bibliothèque) ou des tirages qui en dépendent ; une autre classe vectorielle du processeur (AVX2 contre AVX-512), une
autre version de torch ou un autre noyau par défaut peut déplacer ces écarts autour des seuils jouets (1e-5) :
`test_garde_en_ligne_cas_sain_et_d1_sur_le_jouet`, `test_palier_du_chemin_et_d1_sur_le_jouet`,
`test_repere_et_rapports_sur_le_jouet`, `test_tous_les_rapports_de_garde_et_lecture_du_run_jouet`. Les autres lisent
des structures, des comptes ou des données synthétiques.
"""
from __future__ import annotations

import ast
import atexit
import gc
import inspect
import json
import math
import shutil
import subprocess
import tempfile
import weakref
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest
import torch

from conftest import committer
from controle_ia import gardes
from controle_ia.environnements import juges
from controle_ia.environnements import juges_simplifies as js
from controle_ia.environnements import lancer_pilote_a as lp
from controle_ia.environnements import noter_pilote_a as npa
from controle_ia.environnements import requalifier_juges as rq
from controle_ia.environnements import rubrique_simplifiee as rs
from controle_ia.gardes import GardeArret
from controle_ia.harnais.activations import ecart_decale_zone_generee, ecart_equivalence, profil_ecarts
from controle_ia.harnais.episode import bilan_controle_negatif, generer_lot
from controle_ia.harnais.modeles import etats_effectifs, modele_jouet
from controle_ia.manifeste import graines, generateur, verifier_resultat
from controle_ia.scellement import empreinte, sceller
from test_pilote_a import CIBLES_TEST, CONFIG, TACHES
from test_plan_b_juges_simplifies import FMT, TOK, h4_courte, modele_qui_s_arrete

PILOTE = "20261012-100000-pilote-jouet"
NOTATIONS = "20261017-100000-notations-jouet"
ENTROPIE_PILOTE = 4242
ENTROPIE_ETAPE = 777
JUGES = [{"nom": "jouet-8B", "meme_modele_que_agent": True, "sert_a_l_appariement": True},
         {"nom": "jouet-3B", "meme_modele_que_agent": False, "sert_a_l_appariement": False}]
CONFIG_PILOTE = {**CONFIG, "episodes_par_tache": 2, "episodes_notes_deux_fois": [0], "episodes_decisifs": [0, 1],
                 "lot_juge": 2, "max_nouveaux_juge": 8, "temperature_juge": 1.0, "variante_juge": "b0",
                 "lot_appariement": 4, "duree_max_s": 600, "mode": "jouet", "agent": {"nom": "agent-jouet"},
                 "noyau_attention": "math", "fils": 1, "juges": JUGES}


@pytest.fixture(autouse=True)
def _h4_courte_et_entropie(monkeypatch):
    """H.4 courte partout (le pilote jouet a été construit avec elle : formats et contextes s'accordent) ; entropie de
    l'étape fixée quand aucune n'est citée (runs jouets sans préenregistrement), pour des tirages reproductibles."""
    h4_courte(monkeypatch)
    vrai = rq.creer_manifeste

    def creer(*a, **k):
        return vrai(*a, **{**k, "entropie": k.get("entropie") if k.get("entropie") is not None else ENTROPIE_ETAPE})

    monkeypatch.setattr(rq, "creer_manifeste", creer)


# --- pilote jouet et run des notations H.4 jouet, construits une fois par processus --------------------------------

_GABARIT: dict = {}


def _construire_gabarit() -> Path:
    d = Path(tempfile.mkdtemp(prefix="plan-b-jouet-"))
    atexit.register(shutil.rmtree, d, True)
    for args in (("init", "-q", "-b", "main"), ("config", "user.email", "test@example.invalid"),
                 ("config", "user.name", "test")):
        subprocess.run(["git", "-C", str(d), *args], check=True, capture_output=True)
    (d / "README").write_text("x\n")
    committer(d)
    f = d / "taches.json"
    f.write_text(json.dumps({"taches": [dict(t, cibles=CIBLES_TEST) for t in TACHES]}), encoding="utf-8")
    sceller(f)
    committer(d)
    with pytest.MonkeyPatch.context() as mp:
        h4_courte(mp)
        vrai_jouer, vrai_creer = lp.jouer_pilote, lp.creer_manifeste

        def jouer(*a, **k):
            fiches, vecteurs, cn = vrai_jouer(*a, **k)
            for x in fiches:
                x["bilan"]["ensemble"] = f"PROPOSAL 1: idée {x['episode']}\nPROPOSAL 2: contrôle apparié"
            return fiches, vecteurs, cn

        def noter(*a, **k):
            raise GardeArret("limite de durée dépassée pendant les notations")

        mp.setattr(lp, "jouer_pilote", jouer)
        mp.setattr(lp, "noter_ensembles", noter)
        mp.setattr(lp, "creer_manifeste", lambda *a, **k: vrai_creer(*a, **{**k, "entropie": ENTROPIE_PILOTE}))
        with pytest.raises(GardeArret):
            lp.executer(CONFIG_PILOTE, d, PILOTE, None, str(f))
        committer(d)
        config_n = {**{k: CONFIG_PILOTE[k] for k in npa.CLES_EGALES_AU_PILOTE}, "mode": "jouet", "run_pilote": PILOTE,
                    "duree_max_juges_s": {"jouet-8B": 600, "jouet-3B": 600}, "duree_globale_s": 1200,
                    "notations_attendues_par_juge": 6}
        npa.executer(config_n, d, NOTATIONS, None, str(f))
    committer(d)
    return d


def _gabarit() -> Path:
    if "d" not in _GABARIT:
        _GABARIT["d"] = _construire_gabarit()
    return _GABARIT["d"]


@pytest.fixture
def depot_planb(depot):
    gabarit = _gabarit()
    shutil.rmtree(depot / ".git")
    shutil.copytree(gabarit, depot, dirs_exist_ok=True)
    return depot


def _scellees(depot, juge):
    return json.loads((depot / "diag" / NOTATIONS / f"notations-{juge}-decisives.json").read_text())["resultat"][
        "notations"]


def _chaine(globale: float) -> dict:
    ext = globale + rq.LOT_DE_DEPASSEMENT_S + rq.CONSIGNATION_S
    amorce = ext + rq.KILL_S + 2700
    return {"duree_globale_s": globale, "delai_externe_s": ext, "plafond_amorce_s": amorce,
            "surveillance_s": amorce + rq.MARGE_SURVEILLANCE_S, "mise_en_place_seuil_s": 2700}


def _invite_rs1() -> dict:
    racine_code = Path(rq.__file__).resolve().parents[3]
    return {"racine": rs.RACINE_INVITES_RS1.relative_to(racine_code).as_posix(), "identifiant": "RS1",
            "sha256": rs.empreinte_invite_rs1()}


def _config(depot, **changes) -> dict:
    noms = [j["nom"] for j in JUGES]
    c = {**{k: CONFIG_PILOTE[k] for k in rq.CLES_EGALES_AU_PILOTE}, "mode": "jouet", "run_pilote": PILOTE,
         "manifeste_pilote_sha256": empreinte(depot / "runs" / PILOTE / "manifeste.json"), "run_notations": NOTATIONS,
         "variante_requalification": "RS1", "variante_rejeu": "b0", "notations_attendues_par_juge": 6,
         "couches": [0, 1, 2], "tolerance_demi": 0.2, "statistique_demi": "q99",
         # seuils du jouet (arrondi du chemin ≈ 5e-7, effet de D1 ≈ 1e-4 : `validation_reelle`, CONFIG_REPETITION)
         "tolerance_simple": 1e-5, "statistique_simple": "max", "borne_diffuse_simple": 1e-4,
         "rapport_localisation": 3, "ancrage_max": 1e-6, "ancrage_max_borne": 1e-4 / 3, "couverture_quantile": 0.75,
         "couverture_unite": rq.COUVERTURE_UNITE,
         "couverture_jetons": {n: rq.seuil_de_couverture(_scellees(depot, n), 0.75) for n in noms},
         "positions_min": 4, "regle_kn": True, "rangees_min_demi": 10, "rangees_min_simple": 10, "rangees_min_d1": 6,
         "fraction_min": 0.95, "decalage_d1": 1, "rapport_repere_max": 3, "repere_marge": 0.1, "lots_rejeu": 3,
         "temoin_queue": 0.005, "duree_requalification_s": {n: 600 for n in noms},
         "duree_rejeu_s": {n: 600 for n in noms}, "duree_temoins_s": 600, **_chaine(3000),
         "memoire_vive_min_go": 0, "memoire_carte_min_gio": 0, "invite_rs1": _invite_rs1(),
         "controle_intervalles": {"actif": True, "separateurs_intervalle": list(rs.SEPARATEURS_INTERVALLE),
                                  "separateurs_second_nombre": list(rs.SEPARATEURS_SECOND_NOMBRE)}}
    return {**c, **changes}


def _fichiers(depot, run):
    return sorted(p.name for p in (depot / "diag" / run).glob("*.json"))


def _resultat(depot, run, nom):
    return verifier_resultat(depot, depot / "diag" / run / f"{nom}.json")["resultat"]


TOUS = ["notations-RS1-jouet-3B-decisives.json", "notations-RS1-jouet-8B-decisives.json", "rejeu-jouet-3B-demi.json",
        "rejeu-jouet-3B-simple.json", "rejeu-jouet-8B-demi.json", "rejeu-jouet-8B-simple.json", "resume.json",
        "temoins.json"]


# --- bout en bout ------------------------------------------------------------------------------------------------

_RUN_COMPLET: dict = {}


def _run_complet(depot_planb, capsys=None) -> tuple[Path, str, dict]:
    """Run jouet complet, fait une fois par processus (puis copié) : sa lecture sert à plusieurs tests."""
    run = "20261019-120000-planb-jouet"
    if "d" not in _RUN_COMPLET:
        f = depot_planb / "taches.json"
        resume = rq.executer(_config(depot_planb), depot_planb, run, None, str(f), autoriser_depot_sale=True)
        err = capsys.readouterr().err if capsys is not None else ""
        gab = Path(tempfile.mkdtemp(prefix="plan-b-run-"))
        atexit.register(shutil.rmtree, gab, True)
        shutil.copytree(depot_planb, gab, dirs_exist_ok=True)
        _RUN_COMPLET.update(d=gab, resume=resume, err=err)
    else:
        shutil.rmtree(depot_planb / ".git")
        shutil.copytree(_RUN_COMPLET["d"], depot_planb, dirs_exist_ok=True)
    return depot_planb, run, _RUN_COMPLET


def test_bout_en_bout(depot_planb, capsys):
    depot, run, r = _run_complet(depot_planb, capsys)
    resume = r["resume"]
    assert _fichiers(depot, PILOTE) == ["appariements.json", "arret.json", "episodes.json"]       # rien d'écrit là
    assert _fichiers(depot, run) == TOUS
    assert set(resume["fichiers"].values()) == {"écrit"} and len(resume["fichiers"]) == 7
    assert {p["statut"] for p in resume["phases"].values()} == {"écrit"}
    for juge in ("jouet-8B", "jouet-3B"):
        sc = _scellees(depot, juge)
        n = _resultat(depot, run, f"notations-RS1-{juge}-decisives")
        # mêmes demandes, même ordre que les notations scellées ; clés propres à l'étape
        assert [x["cle"] for x in n["notations"]] == [x["cle"].replace(f"juge-{juge}/", f"juge-RS1-{juge}/")
                                                      for x in sc]
        assert all(x["ensemble_sha256"] == y["ensemble_sha256"] for x, y in zip(n["notations"], sc))
        assert {x["variante"] for x in n["notations"]} == {"RS1"}
        assert n["invite_rs1"] == {**_invite_rs1(), "index_sha256": empreinte(rs.RACINE_INVITES_RS1 / "index.json")}
        # garde en ligne : toutes les rangées gardées, une par notation
        assert [g["cle"] for g in n["garde"]["rapports"]] == [x["cle"] for x in n["notations"]]
        assert n["garde"]["statistique"] == "q99" and n["garde"]["tolerance"] == 0.2
        # champs de `noter_ensembles`, plus la lecture RS1
        assert set(n["notations"][0]) >= {"cle", "variante", "jetons_contexte", "ensemble_sha256", "jetons_reponse",
                                          "tronquee", "notes", "anomalies", "score", "reponse", "lecture_rs1"}
        demi, simple = (_resultat(depot, run, f"rejeu-{juge}-{p}") for p in ("demi", "simple"))
        t = resume["tirages"][juge]
        assert sorted([t["L1"], t["L2"], t["L3"]]) == sorted(t["cadre"]) and demi["tirage"] == t
        mp = json.loads((depot / "runs" / PILOTE / "manifeste.json").read_text())["graines"]
        assert len(demi["rangees"]) == 4 and len(simple["chemin"]["rangees"]) == 4 and len(simple["d1"]["rangees"]) == 2
        for x in demi["rangees"] + simple["chemin"]["rangees"] + simple["d1"]["rangees"]:
            g = mp[x["cle"]]                          # graines du pilote, consignées rangée par rangée
            assert x["graine"] == {"cle_pilote": x["cle"], "entropie": g["entropie"], "spawn_key": g["spawn_key"],
                                   "etat_controle": g["etat_controle"], "graine": rq.graine_entiere(g)}
        assert demi["type_des_poids"] == "torch.bfloat16" and simple["type_des_poids"] == "torch.float32"
        assert simple["conversion"]["aller_retour_exact"] and simple["reglages_relus"]["tf32_cudnn"] is False
        assert set(simple["repere"]["par_couche"]) == {"0", "1", "2"} and len(simple["repere"]["par_rangee"]) == 4
        assert simple["ancrage"]["lot"] == "L1" and set(simple["ancrage"]["par_couche"]) == {"0", "1", "2"}
        assert simple["d1"]["decalage_positions"] == 1
        tm = _resultat(depot, run, "temoins")["juges"][juge]
        assert [a["lot"] for a in tm["appels"]] == ["L1", "L2"] and all(a["statut"] == "fait" for a in tm["appels"])
        assert tm["appels"][0]["cle_graine"] == f"rejeu/{juge}/temoin/L1" and len(tm["appels"][0]["rangees"]) == 2
    mn = json.loads((depot / "runs" / run / "manifeste.json").read_text())
    assert set(mn["graines"]) == {x for juge in ("jouet-8B", "jouet-3B") for x in (
        [n["cle"] for n in _resultat(depot, run, f"notations-RS1-{juge}-decisives")["notations"]]
        + [f"rejeu/{juge}/lots", f"rejeu/{juge}/temoin/L1", f"rejeu/{juge}/temoin/L2"])} | {"modele-jouet"}
    # lignes de progression : rang et durée des lots, fin des phases ; aucun compte, aucun texte, aucune grandeur
    lignes = [x for x in r["err"].splitlines() if x.startswith("PROGRES ")]
    assert len(lignes) == (3 + 1) * 2 + (5 + 1) * 2 + 2 * 2 + 1
    champs = [dict(c.split("=", 1) for c in x.split()[2:]) for x in lignes]
    assert all(set(c) <= {"phase", "juge", "lot", "duree_s", "fin", "lots_faits", "palier", "appel"} for c in champs)
    # ordre des phases : requalification du 8B puis du 3B, rejeu du 3B puis du 8B, témoins du 8B puis du 3B
    assert [(c["phase"], c.get("juge")) for c in champs if "fin" in c] == [
        ("requalification", "jouet-8B"), ("requalification", "jouet-3B"), ("rejeu", "jouet-3B"), ("rejeu", "jouet-8B"),
        ("temoins", None)]
    assert [c["juge"] for c in champs if "appel" in c] == ["jouet-8B", "jouet-8B", "jouet-3B", "jouet-3B"]
    assert [c.get("palier") for c in champs if c["phase"] == "rejeu" and c.get("juge") == "jouet-3B"] == [
        "production", "production", "chemin", "chemin", "d1", None]
    assert "idée" not in r["err"] and "PROPOSAL" not in r["err"] and "SPECIFICITY" not in r["err"]


def test_tous_les_rapports_de_garde_et_lecture_du_run_jouet(depot_planb, capsys):
    """SENSIBLE AU MATÉRIEL (tirages du jouet). Sur le run jouet : garde en ligne (99e centile sous 0,2 en simple
    précision au jouet ; rangées RS1 courtes au sens de k(n − 1) : contrôle négatif « non concluant ») ; paliers du
    rejeu lus par les fonctions de bilan ; couverture au bord (rangée tronquée : `max_nouveaux − 1` positions générées
    comparées)."""
    depot, run, _ = _run_complet(depot_planb, capsys)
    c = _config(depot)
    n = _resultat(depot, run, "notations-RS1-jouet-8B-decisives")
    b = rq.bilan_garde_en_ligne(n["garde"]["rapports"], c)
    assert b["equivalence"] == "conforme" and b["rangees"] == 6 and b["sondes_conformes"]
    assert b["controle_negatif"]["lecture"] == "non concluant" and b["controle_negatif"]["comparables"] == 0
    simple = _resultat(depot, run, "rejeu-jouet-8B-simple")
    demi = _resultat(depot, run, "rejeu-jouet-8B-demi")
    ch = rq.lire_palier_chemin(simple, c, c["couverture_jetons"]["jouet-8B"])
    assert ch["lecture"] == "non concluant (contrôles)"                   # 4 rangées : sous les effectifs minimaux
    tronquees = [x for x in simple["chemin"]["rangees"] if x["tronquee"]]
    assert tronquees, "le jouet doit porter une rangée tronquée"
    x = tronquees[0]
    assert x["jetons_generes"] == 8 and x["garde"]["positions_capturees"] - x["jetons_contexte"] == 7
    cv = rq.couverture_du_chemin(simple["chemin"]["rangees"], 8)
    assert cv["atteinte"] and cv["jetons_generes_max"] == 8 and cv["zone_generee_comparee"] == 7
    assert not rq.couverture_du_chemin(simple["chemin"]["rangees"], 9)["atteinte"]
    pr = rq.lire_palier_production(demi, simple, c)
    assert pr["lecture"] == "non concluant" and set(pr["rho"]) == {"0", "1", "2"}
    assert rq.lire_palier_production(demi, None, c)["lecture"] == "non concluant"


# --- gardes d'avant le manifeste -----------------------------------------------------------------------------------

@pytest.mark.parametrize("changement, motif", [
    ({"mode": "essai"}, "mode"),
    ({"variante_requalification": "S1"}, "variantes"),
    ({"variante_rejeu": "b*"}, "variantes"),
    ({"duree_requalification_s": {"jouet-8B": 600}}, "une valeur par juge"),
    ({"couverture_jetons": {"jouet-8B": 8, "autre": 8}}, "une valeur par juge"),
    ({"duree_temoins_s": 0}, "durée témoins"),
    ({"duree_globale_s": 30_000}, "durée globale"),
    ({"delai_externe_s": 4000}, "chaîne des limites"),
    ({"surveillance_s": 1}, "chaîne des limites"),
    ({"lots_rejeu": 2}, "trois lots"),
    ({"decalage_d1": 0}, "decalage_d1"),
    ({"statistique_demi": "max"}, "statistiques"),
    ({"tolerance_simple": 0}, "tolerance_simple"),
    ({"borne_diffuse_simple": 1e-6}, "borne de l'écart diffus"),
    ({"couverture_quantile": 1.5}, "couverture_quantile"),
    ({"couverture_unite": "positions"}, "couverture_unite"),
    ({"regle_kn": False}, "regle_kn"),
    ({"couches": []}, "couches"),
    ({"controle_intervalles": {"actif": True, "separateurs_intervalle": ["-", "to", "or"],
                               "separateurs_second_nombre": [",", ";", "and", "("]}}, "controle_intervalles"),
    ({"invite_rs1": {"identifiant": "RS1"}}, "invite_rs1"),
    ({"notations_attendues_par_juge": 0}, "notations_attendues_par_juge"),
])
def test_configuration_cas_sain_et_artefacts(changement, motif):
    d = _gabarit()                                                                  # lecture seule
    rq.exiger_config_planb(_config(d))                                              # cas sain
    with pytest.raises(GardeArret, match=motif):
        rq.exiger_config_planb(_config(d, **changement))
    sans = {k: v for k, v in _config(d).items() if k != "temoin_queue"}
    with pytest.raises(GardeArret, match="incomplète"):
        rq.exiger_config_planb(sans)


def test_configuration_reelle_du_texte_acceptee():
    """Cas sain réel : les valeurs de la table « Configuration » du préenregistrement (juges du pilote, échéances et
    chaîne des limites, seuils, couverture de 3 072 et 983 jetons) passent la garde de configuration."""
    juges_ = [{"nom": "8B", "meme_modele_que_agent": True, "sert_a_l_appariement": True,
               "texte_attendu_ouverture": "Today Date: 26 Jul 2024"},
              {"nom": "3B", "meme_modele_que_agent": False, "sert_a_l_appariement": False,
               "modele": "meta-llama/Llama-3.2-3B-Instruct", "revision": "0cb88a4f764b7a12671c53f0838cd831a0843b95",
               "variables_gabarit": {"date_string": "26 Jul 2024"},
               "texte_attendu_ouverture": "Today Date: 26 Jul 2024"}]
    c = {"mode": "reel", "run_pilote": "20261012-105125-t05-pilote-reel", "manifeste_pilote_sha256": "8c" * 32,
         "run_notations": "20261017-193648-t05-notations-reel",
         "agent": {"nom": "8B", "modele": "meta-llama/Llama-3.1-8B-Instruct",
                   "revision": "0e9e39f249a16976918f6564b8830bc894c89659",
                   "variables_gabarit": {"date_string": "26 Jul 2024"},
                   "texte_attendu_ouverture": "Today Date: 26 Jul 2024"},
         "juges": juges_, "lot_juge": 8, "max_nouveaux_juge": 3072, "temperature_juge": 1.0, "fils": 1,
         "episodes_decisifs": [0, 1], "episodes_notes_deux_fois": [0], "variante_requalification": "RS1",
         "variante_rejeu": "b0", "notations_attendues_par_juge": 180, "couches": [7, 15, 23], "tolerance_demi": 0.2,
         "statistique_demi": "q99", "tolerance_simple": 3e-3, "statistique_simple": "max", "borne_diffuse_simple": 1e-2,
         "rapport_localisation": 3, "ancrage_max": 1e-3, "ancrage_max_borne": 1e-2 / 3, "couverture_quantile": 0.75,
         "couverture_unite": "jetons générés par la rangée", "couverture_jetons": {"8B": 3072, "3B": 983},
         "positions_min": 4, "regle_kn": True, "rangees_min_demi": 10, "rangees_min_simple": 10, "rangees_min_d1": 6,
         "fraction_min": 0.95, "decalage_d1": 1, "rapport_repere_max": 3, "repere_marge": 0.1, "lots_rejeu": 3,
         "temoin_queue": 0.005, "duree_requalification_s": {"8B": 7000, "3B": 4500},
         "duree_rejeu_s": {"3B": 3000, "8B": 4800}, "duree_temoins_s": 1200, "duree_globale_s": 23_700,
         "delai_externe_s": 24_720, "plafond_amorce_s": 27_720, "surveillance_s": 28_320,
         "mise_en_place_seuil_s": 2700, "memoire_vive_min_go": 64, "memoire_carte_min_gio": 75,
         "invite_rs1": _invite_rs1(),
         "controle_intervalles": {"actif": True, "separateurs_intervalle": ["-", "–", "—", "to", "or"],
                                  "separateurs_second_nombre": [",", ";", "and", "("]}}
    rq.exiger_config_planb(c)
    assert c["invite_rs1"]["racine"] == "docs/sources/invites-plan-b-v1"
    with pytest.raises(GardeArret, match="chaîne des limites"):
        rq.exiger_config_planb({**c, "plafond_amorce_s": 27_000})


@pytest.mark.parametrize("changement, motif", [
    ({"mode": "reel"}, "R1"),
    ({"lot_juge": 3}, "lot_juge ≠ celui du pilote"),
    ({"notations_attendues_par_juge": 7}, "6 notations à faire"),
    ({"manifeste_pilote_sha256": "0" * 64}, "manifeste du pilote ≠"),
    ({"invite_rs1": {**_invite_rs1(), "sha256": "1" * 64}}, "invite RS1 ≠ celle de la configuration"),
    ({"run_notations": "20261017-100001-autre"}, "manifeste du run des notations absent"),
    ({"memoire_vive_min_go": 10 ** 7}, "mémoire vive"),
    ({"memoire_carte_min_gio": 1}, "carte graphique indisponible"),
])
def test_gardes_avant_le_manifeste_cas_sain_et_artefacts(depot_planb, changement, motif):
    f = depot_planb / "taches.json"
    run = "20261019-120001-planb-jouet"
    with pytest.raises(GardeArret, match=motif):
        rq.executer(_config(depot_planb, **changement), depot_planb, run, None, str(f), autoriser_depot_sale=True)
    assert not (depot_planb / "runs" / run).exists()


def test_gardes_avant_le_manifeste_couverture_cadre_versions(depot_planb, monkeypatch):
    f = depot_planb / "taches.json"
    run = "20261019-120002-planb-jouet"
    c = _config(depot_planb)
    with pytest.raises(GardeArret, match="seuil de couverture recalculé"):
        rq.executer({**c, "couverture_jetons": {"jouet-8B": 9, "jouet-3B": c["couverture_jetons"]["jouet-3B"]}},
                    depot_planb, run, None, str(f), autoriser_depot_sale=True)
    vrai = rq.cadre_du_rejeu
    monkeypatch.setattr(rq, "cadre_du_rejeu", lambda *a: vrai(*a)[:2])
    with pytest.raises(GardeArret, match="cadre du rejeu de 2 lot"):
        rq.executer(c, depot_planb, run, None, str(f), autoriser_depot_sale=True)
    monkeypatch.undo()
    h4_courte(monkeypatch)
    pil = npa.charger_pilote_note(depot_planb, PILOTE)
    vp = pil["manifeste"]["versions"]
    monkeypatch.setattr(rq, "versions", lambda: dict(vp))
    rq.exiger_egal_au_pilote_planb(c, pil, "reel")                                     # cas sain
    monkeypatch.setattr(rq, "versions", lambda: {**vp, "torch": "0.0.essai"})
    with pytest.raises(GardeArret, match=r"versions ≠ celles du pilote : \['torch'\]"):
        rq.exiger_egal_au_pilote_planb(c, pil, "reel")
    with pytest.raises(GardeArret, match="variante du rejeu"):
        pil["manifeste"]["config"]["variante_juge"] = "b*"
        rq.exiger_egal_au_pilote_planb(c, pil, "jouet")
    assert not (depot_planb / "runs" / run).exists()


def test_run_des_notations_non_conforme(depot_planb):
    """Run des notations : un arrêt en plus du résumé (issue double), puis un statut autre qu'« écrit »."""
    f = depot_planb / "taches.json"
    d = depot_planb / "diag" / NOTATIONS
    run = "20261019-120003-planb-jouet"
    (d / "arret.json").write_text("{}")
    with pytest.raises(GardeArret, match="un seul attendu"):
        rq.executer(_config(depot_planb), depot_planb, run, None, str(f), autoriser_depot_sale=True)
    (d / "arret.json").unlink()
    pil = npa.charger_pilote_note(depot_planb, PILOTE)
    sain = rq.charger_notations_rejouees(depot_planb, _config(depot_planb), pil)              # cas sain
    assert set(sain["notations"]) == {"jouet-8B", "jouet-3B"} and len(sain["notations"]["jouet-8B"]) == 6
    pil["manifeste"]["graines"] = graines(["x"], ENTROPIE_PILOTE + 1)
    with pytest.raises(GardeArret, match="entropie ≠ celle du pilote"):
        rq.charger_notations_rejouees(depot_planb, _config(depot_planb), pil)
    assert not (depot_planb / "runs" / run).exists()


def test_ordre_des_demandes_et_alignement(depot_planb):
    pil = npa.charger_pilote_note(depot_planb, PILOTE)
    par_id = {t["identifiant"]: t for t in TACHES}
    c = _config(depot_planb)
    sc = _scellees(depot_planb, "jouet-8B")
    rs1, b0 = rq.demandes_de_l_etape(pil, par_id, c, "jouet-8B", sc)                       # cas sain
    assert [d["variante"] for d in rs1] == ["RS1"] * 6 and [d["variante"] for d in b0] == ["b0"] * 6
    with pytest.raises(GardeArret, match="ordre des demandes"):
        rq.demandes_de_l_etape(pil, par_id, c, "jouet-8B", [sc[1], sc[0]] + sc[2:])
    with pytest.raises(GardeArret, match="désalignement"):
        rq.demandes_de_l_etape(pil, par_id, c, "jouet-8B", [dict(sc[0], ensemble_sha256="0" * 64)] + sc[1:])
    with pytest.raises(GardeArret, match="5 scellées"):
        rq.demandes_de_l_etape(pil, par_id, c, "jouet-8B", sc[:5])


def _prereg(depot, valeurs: dict, nom="prereg-planb.md", lignes_en_plus=()):
    (depot / "prereg").mkdir(exist_ok=True)
    p = depot / "prereg" / nom
    lignes = [f"- {k} : `{v}`" for k, v in valeurs.items() if v is not None] + list(lignes_en_plus)
    corps = ["# Préenregistrement de test", "", *lignes, ""]
    for s in ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
              "Critères de lecture gelés", "Liste d'arrêt"):
        corps += [f"## {s}", "", f"contenu {s}", ""]
    corps += ["## Contre-lecture", "", f"brouillon relu `{'a' * 64}`, rapport `{'b' * 64}`", ""]
    p.write_text("\n".join(corps), encoding="utf-8")
    sceller(p)
    return p


def test_gardes_de_citation_cas_sain_et_artefacts(depot_planb, monkeypatch):
    monkeypatch.setattr(rq, "exiger_code_importe_sous", lambda racine: None)   # code importé du clone (testé ailleurs)
    monkeypatch.setattr(rq, "exiger_modules_geles", lambda racine: None)       # éprouvée à part (mini-dépôt)
    depot = depot_planb
    f = depot / "taches.json"
    commit = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True,
                            check=True).stdout.strip()
    c = _config(depot)
    dn, dp = depot / "diag" / NOTATIONS, depot / "diag" / PILOTE
    inv = {**_invite_rs1(), "index_sha256": empreinte(rs.RACINE_INVITES_RS1 / "index.json")}
    valeurs = {"Commit du code d'analyse": commit,
               "Configuration du plan B (empreinte canonique)": lp.empreinte_config(c),
               "Run du pilote requalifié": PILOTE,
               "Manifeste du pilote requalifié": empreinte(depot / "runs" / PILOTE / "manifeste.json"),
               "Épisodes du pilote requalifié": empreinte(dp / "episodes.json"),
               "Tâches du pilote": empreinte(f), "Run des notations rejoué": NOTATIONS,
               "Manifeste des notations rejoué": empreinte(depot / "runs" / NOTATIONS / "manifeste.json"),
               "Résumé des notations rejoué": empreinte(dn / "resume.json"),
               "Notations rejouées du juge jouet-8B": empreinte(dn / "notations-jouet-8B-decisives.json"),
               "Notations rejouées du juge jouet-3B": empreinte(dn / "notations-jouet-3B-decisives.json"),
               "Invite RS1": inv["sha256"], "Index de l'invite RS1": inv["index_sha256"], "Entropie": 31337}
    sain = _prereg(depot, valeurs)
    cas = [(_prereg(depot, {**valeurs, "Configuration du plan B (empreinte canonique)": "0" * 64}, "p1.md"),
            "configuration"),
           (_prereg(depot, {**valeurs, "Résumé des notations rejoué": "1" * 64}, "p2.md"), "résumé des notations"),
           (_prereg(depot, {**valeurs, "Invite RS1": "2" * 64}, "p3.md"), "invite RS1"),
           (_prereg(depot, {**valeurs, "Notations rejouées du juge jouet-3B": "3" * 64}, "p4.md"),
            "notations rejouées du juge jouet-3B"),
           (_prereg(depot, {**valeurs, "Notations rejouées du juge jouet-3B": None}, "p5.md"),
            "notations rejouées citées"),
           (_prereg(depot, {**valeurs, "Index de l'invite RS1": None}, "p6.md"), "index de l'invite RS1 cité"),
           (_prereg(depot, valeurs, "p7.md", (f"- Run des notations rejoué : `20261017-100009-autre`",)),
            "plusieurs fois"),
           (_prereg(depot, {**valeurs, "Manifeste du pilote requalifié": "4" * 64}, "p8.md"), "manifeste du pilote")]
    committer(depot)
    for p, motif in cas:
        with pytest.raises(GardeArret, match=motif):
            rq.executer(c, depot, "20261019-120004-planb-jouet", str(p), str(f))
        assert not (depot / "runs" / "20261019-120004-planb-jouet").exists()
    # cas sain : les gardes passent, le manifeste se crée sous le préenregistrement et l'entropie citée
    monkeypatch.setattr(rq, "_apres_manifeste", lambda cx, chemin_m, m, debut: {"manifeste": m})
    sortie = rq.executer(c, depot, "20261019-120005-planb-jouet", str(sain), str(f), autoriser_depot_sale=True)
    m = sortie["manifeste"]
    assert m["decisif"] and m["preenregistrement"]["chemin"] == "prereg/prereg-planb.md"
    assert {g["entropie"] for g in m["graines"].values()} == {"31337"}


def test_modules_geles_cas_sain_et_artefacts(depot):
    for m in rq.MODULES_GELES:
        (depot / m).parent.mkdir(parents=True, exist_ok=True)
        (depot / m).write_text("# gelé\n")
    committer(depot)
    commit = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True,
                            check=True).stdout.strip()
    rq.exiger_modules_geles(depot, commit)                                              # cas sain
    (depot / rq.MODULES_GELES[0]).write_text("# modifié\n")
    with pytest.raises(GardeArret, match="modules gelés modifiés"):
        rq.exiger_modules_geles(depot, commit)
    with pytest.raises(GardeArret, match="impossible"):
        rq.exiger_modules_geles(depot, "0" * 40)
    (depot / rq.MODULES_GELES[-1]).unlink()
    with pytest.raises(GardeArret, match="absents"):
        rq.exiger_modules_geles(depot, commit)
    assert len(rq.MODULES_GELES) == 13 and rq.COMMIT_MODULES_GELES.startswith("c63d4f1")


def test_r12_identifiant_deja_present(depot_planb, monkeypatch):
    f = depot_planb / "taches.json"
    run = "20261019-120006-planb-jouet"
    (depot_planb / "runs" / run).mkdir(parents=True)
    with pytest.raises(GardeArret, match="R12"):
        rq.executer(_config(depot_planb), depot_planb, run, None, str(f), autoriser_depot_sale=True)


# --- format en deux temps -------------------------------------------------------------------------------------------

def test_format_b0_different_du_pilote_arrete(depot_planb, monkeypatch):
    f = depot_planb / "taches.json"
    vrai = rq.controler_format

    def controle(fmt, spec, role, config):
        r = vrai(fmt, spec, role, config)
        return {**r, "altere": True} if spec["nom"] == "jouet-3B" else r

    monkeypatch.setattr(rq, "controler_format", controle)
    run = "20261019-120007-planb-jouet"
    with pytest.raises(GardeArret, match=r"format \(b0\) ≠ celui du début du pilote"):
        rq.executer(_config(depot_planb), depot_planb, run, None, str(f), autoriser_depot_sale=True)
    a = _resultat(depot_planb, run, "arret")
    assert a["etape"] == "contrôle du format" and a["partiel"]["fichiers"] == {}


def test_format_rs1_faux_arrete(depot_planb, monkeypatch):
    """Contrôle (ii) : un format dont la transcription incrémentale diffère du gabarit complet sous RS1 arrête ; le
    contrôle (i), b0, est passé avant (format scellé du pilote)."""
    f = depot_planb / "taches.json"
    vrai = rq.controler_format_rs1

    class FormatFautif(type(FMT)):
        def cloture(self, debut, action):
            return super().cloture(debut, action)[:-1]

    def controle(fmt, spec, mode):
        return vrai(FormatFautif(fmt.tok, fins=fmt.fins) if spec["nom"] == "jouet-3B" else fmt, spec, mode)

    monkeypatch.setattr(rq, "controler_format_rs1", controle)
    run = "20261019-120008-planb-jouet"
    with pytest.raises(GardeArret, match="format incrémental"):
        rq.executer(_config(depot_planb), depot_planb, run, None, str(f), autoriser_depot_sale=True)
    assert _resultat(depot_planb, run, "arret")["etape"] == "contrôle du format"


# --- échéances, signal TERM, phases échues ------------------------------------------------------------------------

def test_phases_echues_sans_fichier_et_temoin_impossible(depot_planb, monkeypatch, capsys):
    """Requalification du 8B échue (aucun lot), celle du 3B écrite ; rejeu du 3B échu, celui du 8B écrit ; un appel du
    témoin refusé par le déterminisme : « témoin impossible », consigné, le run continue et `temoins.json` s'écrit."""
    f = depot_planb / "taches.json"
    vrai = rq.appel_temoin
    appels = []

    def refus(*a, **k):
        raise RuntimeError("multinomial does not have a deterministic implementation, but you set "
                           "'torch.use_deterministic_algorithms(True)'.")

    def appel(modele, fmt, demandes, graine, config):
        appels.append(1)
        if len(appels) > 1:
            return vrai(modele, fmt, demandes, graine, config)
        modele.generate = refus                    # premier appel seulement (8B, L1) : refus de déterminisme
        try:
            return vrai(modele, fmt, demandes, graine, config)
        finally:
            del modele.generate

    monkeypatch.setattr(rq, "appel_temoin", appel)
    run = "20261019-120009-planb-jouet"
    c = _config(depot_planb, duree_requalification_s={"jouet-8B": 1e-9, "jouet-3B": 600},
                duree_rejeu_s={"jouet-8B": 600, "jouet-3B": 1e-9})
    resume = rq.executer(c, depot_planb, run, None, str(f), autoriser_depot_sale=True)
    assert _fichiers(depot_planb, run) == ["notations-RS1-jouet-3B-decisives.json", "rejeu-jouet-8B-demi.json",
                                           "rejeu-jouet-8B-simple.json", "resume.json", "temoins.json"]
    assert resume["fichiers"] == {"notations-RS1-jouet-8B-decisives": "échu",
                                  "notations-RS1-jouet-3B-decisives": "écrit",
                                  "rejeu-jouet-3B-demi": "échu", "rejeu-jouet-3B-simple": "échu",
                                  "rejeu-jouet-8B-demi": "écrit", "rejeu-jouet-8B-simple": "écrit", "temoins": "écrit"}
    assert resume["phases"]["requalification-jouet-8B"]["lots_faits"] == 0
    tm = _resultat(depot_planb, run, "temoins")["juges"]
    assert tm["jouet-8B"]["appels"][0]["statut"] == "témoin impossible"
    assert "use_deterministic_algorithms" in tm["jouet-8B"]["appels"][0]["motif"]
    assert tm["jouet-8B"]["appels"][1]["statut"] == "fait" and len(appels) == 4
    assert rq.bilan_temoin(tm["jouet-8B"], 0.005)["T_w"] is None
    err = capsys.readouterr().err
    assert "PROGRES" in err and "fin=échu" in err


@pytest.mark.parametrize("artefact, motif, etape", [
    ("reglages", "réglages effectifs non conformes", "rejeu du juge jouet-3B : simple précision"),
    ("type", "bfloat16", "rejeu du juge jouet-3B : chargement"),
])
def test_arrets_consignes_pendant_le_rejeu(depot_planb, monkeypatch, artefact, motif, etape):
    """Réglages effectifs relus non conformes avant le palier en simple précision (TF32 permis) : arrêt consigné, le
    fichier de la demi-précision écrit ; poids rechargés d'un autre type que bfloat16 : arrêt consigné, aucun
    fichier."""
    if artefact == "reglages":
        vrai = rq.etats_effectifs
        monkeypatch.setattr(rq, "etats_effectifs", lambda: {**vrai(), "tf32_cudnn": True})
    else:
        vrai = rq._charger_pour_le_rejeu

        def charger(cx, j):
            m, fmt = vrai(cx, j)
            return m.to(torch.float32), fmt

        monkeypatch.setattr(rq, "_charger_pour_le_rejeu", charger)
    f = depot_planb / "taches.json"
    run = "20261019-120015-planb-jouet"
    c = _config(depot_planb, duree_requalification_s={"jouet-8B": 1e-9, "jouet-3B": 1e-9})
    with pytest.raises(GardeArret, match=motif):
        rq.executer(c, depot_planb, run, None, str(f), autoriser_depot_sale=True)
    a = _resultat(depot_planb, run, "arret")
    assert a["etape"] == etape
    ecrits = ["arret.json"] + (["rejeu-jouet-3B-demi.json"] if artefact == "reglages" else [])
    assert _fichiers(depot_planb, run) == sorted(ecrits)
    assert a["partiel"]["fichiers"]["rejeu-jouet-3B-simple"] == "en cours"


class Horloge:
    """Horloge des échéances remplacée : chaque chargement et chaque lot avancent d'une durée fixée."""

    def __init__(self):
        self.t = 0.0

    def __call__(self):
        return self.t


def test_ancrages_et_depassement_d_au_plus_un_lot(depot_planb, monkeypatch):
    """Ancrages : la requalification du 8B part de son premier lot (un chargement de 1 000 s ne la fait pas échoir) ;
    le rejeu et les témoins partent du début de leur phase, rechargement compris (un rechargement de 1 000 s les fait
    échoir avant leur premier lot ou appel). Dépassement : un lot commencé avant l'échéance se finit ; la phase s'arrête
    avant le suivant (2 lots faits sur 3 pour une échéance de 500 s et des lots de 300 s)."""
    h = Horloge()
    monkeypatch.setattr(rq, "_horloge", h)
    vrai_charger, vrai_lot = rq.charger_modele_et_format, rq.jouer_lot_de_notations

    def charger(*a, **k):
        h.t += 1000
        return vrai_charger(*a, **k)

    def lot(*a, **k):
        h.t += 300
        return vrai_lot(*a, **k)

    monkeypatch.setattr(rq, "charger_modele_et_format", charger)
    monkeypatch.setattr(rq, "jouer_lot_de_notations", lot)
    f = depot_planb / "taches.json"
    run = "20261019-120010-planb-jouet"
    c = _config(depot_planb, duree_requalification_s={"jouet-8B": 500, "jouet-3B": 20000},
                duree_rejeu_s={"jouet-8B": 500, "jouet-3B": 500}, duree_temoins_s=500, **_chaine(23_000))
    resume = rq.executer(c, depot_planb, run, None, str(f), autoriser_depot_sale=True)
    ph = resume["phases"]
    assert ph["requalification-jouet-8B"]["statut"] == "échu" and ph["requalification-jouet-8B"]["lots_faits"] == 2
    assert ph["requalification-jouet-3B"]["statut"] == "écrit" and ph["requalification-jouet-3B"]["lots_faits"] == 3
    assert ph["rejeu-jouet-3B"]["statut"] == ph["rejeu-jouet-8B"]["statut"] == ph["temoins"]["statut"] == "échu"
    assert ph["requalification-jouet-8B"]["echeance"]["ancre"] == "début du premier lot"
    assert ph["rejeu-jouet-8B"]["echeance"]["ancre"] == "début de la phase, rechargement compris"
    assert _fichiers(depot_planb, run) == ["notations-RS1-jouet-3B-decisives.json", "resume.json"]


def test_echeance_globale_arrete_et_consigne(depot_planb):
    f = depot_planb / "taches.json"
    run = "20261019-120011-planb-jouet"
    with pytest.raises(GardeArret, match="échéance globale"):
        rq.executer(_config(depot_planb, **_chaine(1e-9)), depot_planb, run, None, str(f), autoriser_depot_sale=True)
    assert _fichiers(depot_planb, run) == ["arret.json"]
    a = _resultat(depot_planb, run, "arret")
    assert a["etape"] == "requalification par jouet-8B" and "échéance globale" in a["motif"]
    assert a["partiel"]["phases"]["requalification-jouet-8B"]["lots_faits"] == 0
    assert a["partiel"]["fichiers"] == {"notations-RS1-jouet-8B-decisives": "en cours"}


def test_signal_term_pendant_la_requalification(depot_planb, monkeypatch):
    """Un TERM avalé par une bibliothèque pendant un lot du 8B : arrêt au lot suivant, consigné ; aucun fichier ; le 3B
    n'est pas commencé."""
    f = depot_planb / "taches.json"
    vrai = rq.jouer_lot_de_notations

    def lot(*a, **k):
        sortie = vrai(*a, **k)
        gardes.SIGNAL_TERM_RECU.append(15)
        return sortie

    monkeypatch.setattr(rq, "jouer_lot_de_notations", lot)
    run = "20261019-120012-planb-jouet"
    with pytest.raises(GardeArret, match="signal TERM"):
        rq.executer(_config(depot_planb), depot_planb, run, None, str(f), autoriser_depot_sale=True)
    assert _fichiers(depot_planb, run) == ["arret.json"]
    a = _resultat(depot_planb, run, "arret")
    assert a["motif"].startswith("GardeArret: " + gardes.MOTIF_TERM) and a["etape"] == "requalification par jouet-8B"
    assert set(a["partiel"]["phases"]) == {"requalification-jouet-8B"}
    assert a["partiel"]["phases"]["requalification-jouet-8B"]["lots_faits"] == 1


def test_memoire_rendue_avant_le_lot_suivant(depot_planb, monkeypatch):
    """Les activations d'un lot de requalification (passes uniques rendues par `jouer_episodes`) sont rendues avant le
    lot suivant : aucune référence n'en survit (références faibles mortes après un ramasse-miettes)."""
    vivantes, vues = [], []
    vrai = js.jouer_episodes

    def jouer(*a, **k):
        gc.collect()
        vues.append(sum(1 for r in vivantes if r() is not None))
        sorties = vrai(*a, **k)
        for _, acts, _ in sorties:
            vivantes.extend(weakref.ref(x) for par_agent in acts.values() for x in par_agent.values())
        return sorties

    monkeypatch.setattr(js, "jouer_episodes", jouer)
    f = depot_planb / "taches.json"
    c = _config(depot_planb, duree_requalification_s={"jouet-8B": 600, "jouet-3B": 1e-9},
                duree_rejeu_s={"jouet-8B": 1e-9, "jouet-3B": 1e-9}, duree_temoins_s=1e-9)
    rq.executer(c, depot_planb, "20261019-120013-planb-jouet", None, str(f), autoriser_depot_sale=True)
    assert vues == [0, 0, 0] and len(vivantes) == 3 * 2 * 3
    gc.collect()
    assert all(r() is None for r in vivantes)
    # artefact : une liste qui garde les sorties d'un lot les retient (le compte le voit)
    garde = []

    def jouer_qui_garde(*a, **k):
        sorties = jouer(*a, **k)
        garde.append(sorties)
        return sorties

    vivantes.clear(), vues.clear()
    monkeypatch.setattr(js, "jouer_episodes", jouer_qui_garde)
    rq.executer(c, depot_planb, "20261019-120014-planb-jouet", None, str(f), autoriser_depot_sale=True)
    assert vues == [0, 6, 12]


def test_generer_lot_seulement_par_jouer_episodes_et_generate_seulement_au_temoin():
    arbre = ast.parse(inspect.getsource(rq))
    appels = {}
    for fonction in [n for n in ast.walk(arbre) if isinstance(n, ast.FunctionDef)]:
        for n in ast.walk(fonction):
            if isinstance(n, ast.Call):
                nom = n.func.id if isinstance(n.func, ast.Name) else getattr(n.func, "attr", None)
                appels.setdefault(nom, set()).add(fonction.name)
    assert "generer_lot" not in appels and "jouer_episodes" not in appels
    assert appels["generate"] == {"appel_temoin"}
    assert appels["jouer_lot_de_notations"] == {"_requalifier", "_rejouer"}


# --- garde en ligne et règle k(n − 1) -------------------------------------------------------------------------------

def test_k_angle_mort():
    assert [rq.k_angle_mort(n) for n in (1, 2, 100, 101, 1000, 10_074)] == [1, 2, 2, 2, 11, 102]
    for n in range(1, 3000):                      # au moins k positions : le 99e centile les atteint sûrement
        k = rq.k_angle_mort(n)
        e = np.zeros(n)
        e[n - k:] = 1.0
        assert np.quantile(e, 0.99) > 0
        if k > 1:
            e[: n - k + 1] = 0.0
            e[n - k + 1:] = 1.0                   # k − 1 positions : le 99e centile peut les manquer
            assert np.quantile(e, 0.99) < 1.0
    with pytest.raises(GardeArret):
        rq.k_angle_mort(0)


def _garde_synthetique(cle, lc, n, rng, decalee=False):
    """Rapport de garde d'une rangée synthétique : génération = passe unique (aucun écart), contexte de `lc` positions,
    `n` positions capturées ; fonctions gelées du harnais."""
    p = {c: rng.standard_normal((n + 2, 16)).astype(np.float32) for c in (0, 1)}
    g = {c: v[:n].copy() for c, v in p.items()}
    cn = ecart_decale_zone_generee(g, p, lc, 0.2)
    return {"cle": cle, "tolerance": 0.2, "statistique": "q99", "ecarts": ecart_equivalence(g, p),
            "ecarts_q99": ecart_equivalence(g, p, quantile=0.99), "controle_negatif_zone_generee": cn,
            "profils": profil_ecarts(g, p, lc), "positions_capturees": n, "longueurs_contexte": lc,
            "sondes": {"tableaux_distincts": True, "ulp_vu": True}, "lignes": {"remplissage": 0}}


def test_regle_kn_cas_sain_et_artefact():
    """Dix rangées comparables (zone générée large) et une rangée au long contexte dont la zone générée décalée compte
    4 positions, sous k(n − 1) = 12 : la règle la compte courte et le contrôle négatif est conforme (cas sain) ; sans la
    règle, elle compte comme comparable, son 99e centile décalé reste nul, et le contrôle négatif devient « contraire »
    à tort (artefact)."""
    rng = np.random.default_rng(3)
    gardes_ = [_garde_synthetique(f"r{k}", 50, 80, rng) for k in range(10)]
    longue = _garde_synthetique("longue", 1000, 1005, rng)
    assert min(v["positions"] for v in longue["controle_negatif_zone_generee"].values()) == 4
    assert rq.k_angle_mort(1005 - 1) == 12
    assert max(v["q99"] for v in longue["controle_negatif_zone_generee"].values()) == 0
    c = {"tolerance_demi": 0.2, "positions_min": 4, "regle_kn": True, "rangees_min_demi": 10, "fraction_min": 0.95}
    sain = rq.bilan_garde_en_ligne(gardes_ + [longue], c)
    assert sain["controle_negatif"]["lecture"] == "conforme" and sain["controle_negatif"]["courtes"] == 1
    assert sain["controle_negatif"]["comparables"] == 10 and sain["equivalence"] == "conforme"
    sans = rq.bilan_controle_negatif_rangees(gardes_ + [longue], 4, regle_kn=False)
    assert rq.lire_controle_negatif(sans, 10, 0.95) == "contraire" and sans["echecs"] == ["longue"]
    # sans la règle, même compte que la fonction gelée du harnais
    gele = bilan_controle_negatif([{"tolerance": 0.2, "statistique": "q99", "episode": g["cle"],
                                    "controle_negatif_zone_generee": {"0,0": g["controle_negatif_zone_generee"]}}
                                   for g in gardes_ + [longue]], positions_min=4)
    assert (gele["comparables"], gele["passent"], gele["courtes"]) == (sans["comparables"], sans["passent"],
                                                                       sans["courtes"])
    # moins de 10 rangées comparables : « non concluant »
    peu = rq.bilan_garde_en_ligne(gardes_[:9] + [longue], c)
    assert peu["controle_negatif"]["lecture"] == "non concluant"
    # trop beau : aucune rangée n'a d'écart non nul dans sa zone générée
    assert peu["trop_beau"] is True
    # une rangée au-dessus de la tolérance : garde contraire
    haute = dict(gardes_[0], ecarts_q99={0: 0.25, 1: 0.0})
    assert rq.bilan_garde_en_ligne([haute] + gardes_[1:], c)["equivalence"] == "contraire"
    nan = dict(gardes_[0], ecarts_q99={0: float("nan"), 1: 0.0})
    assert rq.bilan_garde_en_ligne([nan] + gardes_[1:], c)["au_dessus"] == ["r0"]


def test_garde_en_ligne_cas_sain_et_d1_sur_le_jouet(monkeypatch):
    """SENSIBLE AU MATÉRIEL. Garde en ligne sur le modèle jouet en simple précision, contextes courts (b0, H.4 courte),
    réponses de 30 jetons au plus : sans défaut, chaque rangée sous la tolérance du jouet et contrôle négatif conforme
    sur les rangées comparables (cas sain) ; avec D1 injecté, chaque rangée comparable est vue (artefact). Une rangée
    courte au sens de k(n − 1) n'est pas vue au 99e centile : c'est l'angle mort déclaré, que le test montre aussi."""
    h4_courte(monkeypatch)
    m = modele_jouet(5, len(TOK), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    dem = [{"cle": f"k{i}", "questions": "Why do routers matter?", "ensemble": f"PROPOSAL 1: idée {i}",
            "classification": None} for i in range(4)]
    g = {d["cle"]: 70 + i for i, d in enumerate(dem)}
    c = {"tolerance_demi": 1e-5, "positions_min": 4, "regle_kn": True, "rangees_min_demi": 2, "fraction_min": 0.95}
    sain = [dict(x["rapport"], cle=x["notation"]["cle"])
            for x in js.jouer_lot_de_notations(m, FMT, dem, g, "b0", [0, 1, 2], 30, 1.0, 1e-5, "q99")]
    d1 = [dict(x["rapport"], cle=x["notation"]["cle"])
          for x in js.jouer_lot_de_notations(m, FMT, dem, g, "b0", [0, 1, 2], 30, 1.0, 1e-5, "q99",
                                             decalage_positions=1)]

    def comparable(r):
        z = r["controle_negatif_zone_generee"]
        return z is not None and min(v["positions"] for v in z.values()) >= max(
            4, rq.k_angle_mort(r["positions_capturees"] - 1))

    comparables = {r["cle"] for r in sain if comparable(r)}
    assert len(comparables) >= 2 and len(comparables) < 4                    # graines choisies : une rangée courte
    b_sain, b_d1 = rq.bilan_garde_en_ligne(sain, c), rq.bilan_garde_en_ligne(d1, c)
    assert b_sain["equivalence"] == "conforme" and b_sain["controle_negatif"]["lecture"] == "conforme"
    assert b_sain["controle_negatif"]["comparables"] == len(comparables)
    assert b_d1["equivalence"] == "contraire" and set(b_d1["au_dessus"]) == comparables


# --- rejeu ---------------------------------------------------------------------------------------------------------

def test_tirage_des_lots_reproductible_et_cadre():
    g = graines(["rejeu/8B/lots", "rejeu/3B/lots"], 99)
    cadre = [0, 2, 3, 5, 6, 9]
    a = rq.tirer_lots(cadre, generateur(g["rejeu/8B/lots"]))
    assert a == rq.tirer_lots(cadre, generateur(g["rejeu/8B/lots"]))                 # reproductible
    assert len(set(a)) == 3 and set(a) <= set(cadre)
    assert rq.tirer_lots(cadre[::-1], generateur(g["rejeu/8B/lots"])) == a          # cadre trié avant le tirage
    with pytest.raises(GardeArret, match="cadre du rejeu de 2 lot"):
        rq.tirer_lots([1, 4], generateur(g["rejeu/3B/lots"]))
    sc = [{"tronquee": k in (1, 5, 6, 8), "jetons_reponse": 8 if k in (1, 5, 6) else 3} for k in range(10)]
    # lots de 2 : (0,1) (2,3) (4,5) (6,7) (8,9) ; la rangée 8 est tronquée sans atteindre le plafond : hors du cadre
    assert rq.cadre_du_rejeu(sc, 2, 8) == [0, 2, 3]
    assert rq.cadre_du_rejeu(sc[:9], 4, 8) == [0, 1]                                # dernier lot incomplet exclu


def test_graines_du_rejeu_cas_sain_et_artefacts():
    cles = ["juge-8B/t/e0/passe-0", "juge-8B/t/e0/passe-1"]
    gp = graines(cles + ["autre"], 4242)
    sain = rq.graines_du_rejeu(cles, {"graines": gp}, {"graines": dict(gp)})
    assert sain[cles[0]]["graine"] == rq.graine_entiere(gp[cles[0]]) and sain[cles[0]]["cle_pilote"] == cles[0]
    alteree = {**gp, cles[1]: dict(gp[cles[1]], spawn_key=["1"])}
    with pytest.raises(GardeArret, match="graine du rejeu"):
        rq.graines_du_rejeu(cles, {"graines": gp}, {"graines": alteree})
    controle = {**gp, cles[1]: dict(gp[cles[1]], etat_controle=[1, 2])}
    with pytest.raises(GardeArret, match="graine reconstruite"):
        rq.graines_du_rejeu(cles, {"graines": controle}, {"graines": controle})


def test_reproduction_cas_identique_et_artefact():
    sc = {"cle": "juge-8B/t/e0/passe-0", "reponse": "SPECIFICITY: 3", "jetons_reponse": 14, "tronquee": False}
    assert rq.reproduction(dict(sc), sc) == {"texte": True, "jetons": True, "tronquee": True, "identique": True}
    alteree = rq.reproduction(dict(sc, reponse="SPECIFICITY: 4"), sc)
    assert alteree["identique"] is False and alteree["texte"] is False and alteree["jetons"] is True
    with pytest.raises(GardeArret, match="clé"):
        rq.reproduction(dict(sc, cle="autre"), sc)


def test_conversion_en_simple_precision_cas_sain_et_artefacts():
    m = modele_jouet(5, len(TOK), couches=2, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    m = m.to(torch.bfloat16)
    m32, constat = rq.convertir_en_simple(m)                                        # cas sain : aller et retour exact
    assert constat["aller_retour_exact"] and constat["type_apres"] == "torch.float32"
    assert all(p.dtype == torch.float32 for p in m32.parameters())
    m = modele_jouet(5, len(TOK), couches=2, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    m = m.to(torch.bfloat16)
    with torch.no_grad():
        m.model.norm.weight[0] = 1.0e6              # exact en bfloat16, hors de l'étendue de float16 (au plus 65 504)
    with pytest.raises(GardeArret, match="non exacte"):                             # conversion par float16 : perte
        rq.convertir_en_simple(m, convertir=lambda x: x.to(torch.float16).to(torch.float32))
    m = modele_jouet(5, len(TOK), couches=2, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    with pytest.raises(GardeArret, match="bfloat16"):                               # point de départ non bfloat16
        rq.convertir_en_simple(m)
    m = modele_jouet(5, len(TOK), couches=2, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    with pytest.raises(GardeArret, match="float16"):                                # type relu après la conversion
        rq.convertir_en_simple(m.to(torch.bfloat16), convertir=lambda x: x.to(torch.float16))


def test_reglages_relus_cas_sain_et_artefact():
    avant = torch.backends.cudnn.allow_tf32
    try:
        rq._regler_comme_la_carte()
        rq.exiger_reglages_conformes(etats_effectifs())                             # cas sain
        torch.backends.cudnn.allow_tf32 = True
        with pytest.raises(GardeArret, match="tf32_cudnn"):
            rq.exiger_reglages_conformes(etats_effectifs())
        torch.backends.cudnn.allow_tf32 = False
        torch.set_float32_matmul_precision("high")
        with pytest.raises(GardeArret, match="precision_produits_simple"):
            rq.exiger_reglages_conformes(etats_effectifs())
    finally:
        torch.set_float32_matmul_precision("highest")
        torch.backends.cudnn.allow_tf32 = avant


DEMANDES_COURTES = [{"cle": f"juge-8B/t{i}/e0/passe-0", "questions": "Why do routers matter?",
                     "ensemble": f"PROPOSAL 1: idée {i}", "classification": None} for i in range(4)]


def test_palier_du_chemin_et_d1_sur_le_jouet(monkeypatch):
    """SENSIBLE AU MATÉRIEL. Simple précision, jouet, seuil du jouet (1e-5) : sans défaut, aucun dépassement ; D1
    injecté (positions décodées décalées de +1) vu à chaque couche, contexte intact ; artefact : le même lot sans
    injection n'est pas vu."""
    h4_courte(monkeypatch)
    m = modele_jouet(5, len(TOK), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    g = {d["cle"]: 50 + i for i, d in enumerate(DEMANDES_COURTES)}
    chemin = js.jouer_lot_de_notations(m, FMT, DEMANDES_COURTES, g, "b0", [0, 1, 2], 8, 1.0, 1e-5, "max")
    d1 = js.jouer_lot_de_notations(m, FMT, DEMANDES_COURTES, g, "b0", [0, 1, 2], 8, 1.0, 1e-5, "max",
                                   decalage_positions=1)
    assert all(e <= 1e-5 for x in chemin for e in x["rapport"]["ecarts"].values())

    def bilan(lignes):
        return rq.bilan_controle_positif([(SimpleNamespace(identifiant=x["notation"]["cle"]), None,
                                           {"ecarts": {"0,0": x["rapport"]["ecarts"]},
                                            "profils": {"0,0": x["rapport"]["profils"]}}) for x in lignes],
                                         {"tolerance": 1e-5}, {"positions_min": 4})

    vu, non_vu = bilan(d1), bilan(chemin)
    assert vu["comparables"] >= 3 and vu["fraction"] == 1.0 and vu["max_contexte"] <= 1e-5
    assert non_vu["fraction"] == 0.0


def _rangee_synthetique(cle, ecarts: dict, ctx: dict, gen: dict, generes=8, contexte=100, nuls=0, cn=1.0):
    profils = {c: {"jetons": contexte + generes - 1, "max": max(ctx[c], gen[c]),
                   "contexte": {"jetons": contexte, "max": ctx[c], "nuls": 0},
                   "generee": {"jetons": generes - 1, "max": gen[c], "nuls": nuls}} for c in ecarts}
    return {"cle": cle, "lot": "L1", "jetons_contexte": contexte, "jetons_generes": generes, "tronquee": True,
            "garde": {"tolerance": 1e-5, "statistique": "max", "ecarts": dict(ecarts), "ecarts_q99": dict(ecarts),
                      "controle_negatif_zone_generee": {c: {"max": cn, "q99": cn, "au_dessus": 5, "positions": 6}
                                                        for c in ecarts},
                      "profils": profils, "positions_capturees": contexte + generes - 1, "longueurs_contexte": contexte,
                      "sondes": {"tableaux_distincts": True, "ulp_vu": True}, "lignes": {"remplissage": 0}}}


C_SYNTH = {"tolerance_simple": 1e-5, "borne_diffuse_simple": 1e-4, "rapport_localisation": 3, "ancrage_max": 1e-6,
           "ancrage_max_borne": 1e-4 / 3, "positions_min": 4, "rangees_min_simple": 10, "rangees_min_d1": 6,
           "fraction_min": 0.95, "regle_kn": True, "rangees_min_demi": 10, "tolerance_demi": 0.2,
           "rapport_repere_max": 3, "repere_marge": 0.1}


def _simple(lignes_chemin=None, ancrage=None, d1_ctx=1e-6, reglages=None):
    base = {"0": 1e-6, "1": 1e-6}
    chemin = lignes_chemin or [_rangee_synthetique(f"r{k}", base, {"0": 5e-7, "1": 5e-7}, {"0": 1e-6, "1": 1e-6})
                               for k in range(12)]
    d1 = [_rangee_synthetique(f"d{k}", {"0": 2e-4, "1": 2e-4}, {"0": d1_ctx, "1": d1_ctx}, {"0": 2e-4, "1": 2e-4})
          for k in range(8)]
    return {"reglages_relus": reglages or dict(rq.REGLAGES_CONFORMES), "chemin": {"rangees": chemin},
            "d1": {"rangees": d1}, "ancrage": {"par_couche": ancrage or {"0": 5e-7, "1": 5e-7}}}


def _avec_depassement(ecart, ctx, gen):
    lignes = _simple()["chemin"]["rangees"]
    lignes[3] = _rangee_synthetique("r3", {"0": ecart, "1": 1e-6}, {"0": ctx, "1": 5e-7}, {"0": gen, "1": 1e-6})
    return lignes


@pytest.mark.parametrize("ecart, ctx, gen, ancrage, classe, lecture", [
    (5e-5, 1e-6, 5e-5, {"0": 5e-7, "1": 5e-7}, "décodage", "défaut (décodage)"),        # concentré dans la zone générée
    (5e-5, 5e-5, 1e-6, {"0": 5e-7, "1": 5e-7}, "contexte", "non concluant (contexte)"),  # concentré dans le contexte
    (5e-5, 4e-5, 5e-5, {"0": 5e-7, "1": 5e-7}, "diffus", "non concluant, précision probable"),
    (2e-4, 1e-6, 2e-4, {"0": 5e-7, "1": 5e-7}, "trop grand", "défaut (écart trop grand)"),  # au-dessus de la borne
    # ancrage au-dessus de 1e-6 (jouet : 1e-3 au réel) à la couche d'un dépassement d'au plus la borne
    (5e-5, 1e-6, 5e-5, {"0": 2e-6, "1": 5e-7}, "sans marge", "non concluant (seuil sans marge)"),
    # ancrage au-dessus de la borne / 3 à la couche d'un écart au-dessus de la borne : sans marge, jamais « défaut »
    (2e-4, 1e-6, 2e-4, {"0": 5e-5, "1": 5e-7}, "sans marge", "non concluant (seuil sans marge)"),
    # ancrage au-dessus du seuil à une autre couche que celle d'un dépassement « décodage » : le défaut reste lu
    (5e-5, 1e-6, 5e-5, {"0": 5e-7, "1": 5e-5}, "décodage", "défaut (décodage)"),
])
def test_classement_des_depassements_et_ancrage_couche_par_couche(ecart, ctx, gen, ancrage, classe, lecture):
    s = _simple(_avec_depassement(ecart, ctx, gen), ancrage=ancrage)
    lu = rq.lire_palier_chemin(s, C_SYNTH, 8)
    assert [x["classe"] for x in lu["depassements"]] == [classe] and lu["depassements"][0]["couche"] == "0"
    assert lu["lecture"] == lecture
    assert rq.classer_depassement(ecart, ctx, gen, ancrage["0"], C_SYNTH) == classe


def test_lecture_du_chemin_sans_depassement_et_recouvrements():
    fidele = rq.lire_palier_chemin(_simple(), C_SYNTH, 8)
    assert fidele["lecture"] == "fidèle" and fidele["reserve_ancrage"] is False and fidele["d1"]["lecture"] == "vu"
    reserve = rq.lire_palier_chemin(_simple(ancrage={"0": 5e-7, "1": 2e-6}), C_SYNTH, 8)
    assert reserve["lecture"] == "fidèle" and reserve["reserve_ancrage"] is True          # sans dépassement : réserve
    assert rq.lire_palier_chemin(_simple(), C_SYNTH, 9)["lecture"] == "non concluant (couverture)"
    nuls = [_rangee_synthetique(f"r{k}", {"0": 0.0, "1": 0.0}, {"0": 0.0, "1": 0.0}, {"0": 0.0, "1": 0.0}, nuls=7)
            for k in range(12)]
    assert rq.lire_palier_chemin(_simple(nuls), C_SYNTH, 8)["lecture"] == "trop beau"     # et non « fidèle »
    # dépassements « décodage » et « sans marge » à deux couches : « défaut (décodage) »
    lignes = _simple()["chemin"]["rangees"]
    lignes[2] = _rangee_synthetique("r2", {"0": 5e-5, "1": 5e-5}, {"0": 1e-6, "1": 1e-6}, {"0": 5e-5, "1": 5e-5})
    deux = rq.lire_palier_chemin(_simple(lignes, ancrage={"0": 5e-7, "1": 2e-6}), C_SYNTH, 8)
    assert sorted(x["classe"] for x in deux["depassements"]) == ["décodage", "sans marge"]
    assert deux["lecture"] == "défaut (décodage)"
    assert rq.lire_palier_chemin(_simple(d1_ctx=5e-5), C_SYNTH, 8)["lecture"] == "non concluant (D1 non probant)"
    nr = rq.lire_palier_chemin(_simple(reglages={**rq.REGLAGES_CONFORMES, "tf32_produits": True}), C_SYNTH, 8)
    assert nr["lecture"] == "non concluant (contrôles)"
    assert rq.lire_palier_chemin(None, C_SYNTH, 8)["lecture"] == "non concluant (contrôles)"
    nan = rq.lire_palier_chemin(_simple(_avec_depassement(float("nan"), 1e-6, 1e-6)), C_SYNTH, 8)
    assert [x["classe"] for x in nan["depassements"]] == ["illisible"] and nan["lecture"] == "non concluant (contrôles)"
    zone_courte = {c: {"max": 1.0, "q99": 1.0, "au_dessus": 1, "positions": 2} for c in ("0", "1")}
    courtes = [dict(x, garde=dict(x["garde"], controle_negatif_zone_generee=zone_courte))
               for x in _simple()["chemin"]["rangees"]]
    assert rq.lire_palier_chemin(_simple(courtes), C_SYNTH, 8)["lecture"] == "non concluant (contrôles)"
    sonde = _simple()
    sonde["chemin"]["rangees"][0]["garde"]["sondes"]["ulp_vu"] = False
    assert rq.lire_palier_chemin(sonde, C_SYNTH, 8)["lecture"] == "non concluant (contrôles)"
    d1_court = _simple()
    d1_court["d1"]["rangees"] = d1_court["d1"]["rangees"][:5]
    assert rq.lire_palier_chemin(d1_court, C_SYNTH, 8)["d1"]["lecture"] == "non concluant"


def _demi_et_repere(q99s: list[float], repere_q99: float, cn=1.0, nuls=0):
    rangees = []
    for k, q in enumerate(q99s):
        r = _rangee_synthetique(f"r{k}", {"0": q, "1": q / 2}, {"0": q, "1": q}, {"0": q, "1": q}, nuls=nuls, cn=cn)
        r["garde"]["tolerance"], r["garde"]["statistique"] = 0.2, "q99"
        r["garde"]["positions_capturees"] = 120                       # k(119) = 2 : zone décalée de 6 positions
        rangees.append(r)
    repere = {"par_couche": {"0": {"q99": repere_q99}, "1": {"q99": repere_q99}},
              "par_rangee": [{"cle": f"r{k}", "par_couche": {"0": {"q99": repere_q99 / 2}, "1": {"q99": repere_q99}}}
                             for k in range(len(q99s))]}
    return {"rangees": rangees}, {"repere": repere}


def test_lecture_de_la_production_repere_et_rapports():
    demi, simple = _demi_et_repere([0.05] * 16, 0.03)
    lu = rq.lire_palier_production(demi, simple, C_SYNTH)
    assert lu["lecture"] == "conforme" and lu["rho"]["0"] == pytest.approx(0.05 / 0.03)
    assert lu["par_rangee"][0]["0"] == pytest.approx(0.05 / 0.015)                       # rangée sur son repère
    demi, simple = _demi_et_repere([0.15] * 16, 0.03)
    assert rq.lire_palier_production(demi, simple, C_SYNTH)["lecture"] == "réserve (ρ)"
    demi, simple = _demi_et_repere([0.25] + [0.05] * 15, 0.15)
    lu = rq.lire_palier_production(demi, simple, C_SYNTH)
    assert lu["lecture"] == "réserve (au-dessus du seuil)" and lu["marges"] == {"0": "seuil sans marge sur ce run"}
    demi, simple = _demi_et_repere([0.25] + [0.05] * 15, 0.05)
    assert rq.lire_palier_production(demi, simple, C_SYNTH)["marges"]["0"] == "défaut possible"
    # contrôle négatif contraire avec G_D,max ≤ 0,2 et ρ ≤ 3 : « non concluant »
    demi, simple = _demi_et_repere([0.05] * 16, 0.03, cn=0.1)
    assert rq.lire_palier_production(demi, simple, C_SYNTH)["lecture"] == "non concluant"
    demi, simple = _demi_et_repere([0.0] * 16, 0.03, nuls=7)
    assert rq.lire_palier_production(demi, simple, C_SYNTH)["lecture"] == "trop beau"
    demi, simple = _demi_et_repere([0.05] * 9, 0.03)
    assert rq.lire_palier_production(demi, simple, C_SYNTH)["controle_negatif"]["lecture"] == "non concluant"


def test_repere_et_rapports_sur_le_jouet(monkeypatch):
    """SENSIBLE AU MATÉRIEL. Repère sur le jouet : passe en bfloat16 (gardée) contre passe du modèle converti en simple
    précision ; écarts positifs, par couche et par rangée ; l'ancrage compare deux noyaux en simple précision."""
    h4_courte(monkeypatch)
    m = modele_jouet(5, len(TOK), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    m = m.to(torch.bfloat16)
    g = {d["cle"]: 50 + i for i, d in enumerate(DEMANDES_COURTES)}
    lignes = js.jouer_lot_de_notations(m, FMT, DEMANDES_COURTES[:2], g, "b0", [0, 1, 2], 8, 1.0, 0.2, "q99",
                                       garder_passes=True)
    gardees = [{"lot": "L1", "cle": x["notation"]["cle"], "transcription": x["transcription"], "passe": x["passe"]}
               for x in lignes]
    m32, _ = rq.convertir_en_simple(m)
    repere, passes = rq.repere_demi_simple(gardees, m32, [0, 1, 2])
    assert set(repere["par_couche"]) == {"0", "1", "2"} and all(v["q99"] > 0 for v in repere["par_couche"].values())
    assert [x["cle"] for x in repere["par_rangee"]] == [x["cle"] for x in gardees]
    assert repere["par_rangee"][0]["positions"] == len(gardees[0]["transcription"])
    anc = rq.ancrage_noyaux(m32, gardees[0]["transcription"], passes[gardees[0]["cle"]], [0, 1, 2])
    assert set(anc["par_couche"]) == {"0", "1", "2"} and all(v < 1e-4 for v in anc["par_couche"].values())


# --- témoin -----------------------------------------------------------------------------------------------------------

def _modele_temoin():
    m = modele_jouet(5, len(TOK), couches=2, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    # configuration de génération par défaut à la manière de Llama 3.1 : tirage, température 0,6, filtre par noyau 0,9
    m.generation_config.do_sample, m.generation_config.temperature, m.generation_config.top_p = True, 0.6, 0.9
    return m.to(torch.bfloat16)


C_TEMOIN = {"temperature_juge": 1.0, "max_nouveaux_juge": 6}


def test_temoin_configuration_remplacee_cas_sain_et_artefact(monkeypatch):
    h4_courte(monkeypatch)
    m = _modele_temoin()
    appel = rq.appel_temoin(m, FMT, DEMANDES_COURTES[:2], 12, C_TEMOIN)
    assert appel["statut"] == "fait" and len(appel["rangees"]) == 2
    eff = appel["configuration_effective"]
    assert (eff["temperature"], eff["top_p"], eff["top_k"], eff["do_sample"]) == (1.0, 1.0, 0, True)
    assert eff["max_new_tokens"] == 6 and eff["eos_token_id"] == sorted(FMT.fins)
    assert all((r["tronquee"] and r["jetons_generes"] == 6) or (not r["tronquee"] and r["jetons_generes"] <= 6)
               for r in appel["rangees"])
    assert appel == rq.appel_temoin(m, FMT, DEMANDES_COURTES[:2], 12, C_TEMOIN)          # graine posée avant l'appel
    # artefact : des réglages écrits qui oublient le filtre par noyau laissent celui du modèle (0,9) : arrêt
    vrai = rq.reglages_du_temoin
    monkeypatch.setattr(rq, "reglages_du_temoin", lambda *a: {k: v for k, v in vrai(*a).items() if k != "top_p"})
    with pytest.raises(GardeArret, match="top_p"):
        rq.appel_temoin(m, FMT, DEMANDES_COURTES[:2], 12, C_TEMOIN)
    monkeypatch.setattr(rq, "reglages_du_temoin", lambda *a: {k: v for k, v in vrai(*a).items() if k != "top_k"})
    with pytest.raises(GardeArret, match="top_k"):                    # la bibliothèque mettrait 50 par défaut
        rq.appel_temoin(m, FMT, DEMANDES_COURTES[:2], 12, C_TEMOIN)
    monkeypatch.setattr(rq, "reglages_du_temoin", lambda *a: {**vrai(*a), "inconnu": 1})
    with pytest.raises(GardeArret, match="inconnus"):
        rq.appel_temoin(m, FMT, DEMANDES_COURTES[:2], 12, C_TEMOIN)


def test_temoin_impossible_et_pannes_propagees(monkeypatch):
    h4_courte(monkeypatch)
    m = _modele_temoin()

    def lever(e):
        def f(*a, **k):
            raise e
        return f

    monkeypatch.setattr(m, "generate", lever(RuntimeError(
        "cumsum_cuda_kernel does not have a deterministic implementation, but you set "
        "'torch.use_deterministic_algorithms(True)'.")))
    r = rq.appel_temoin(m, FMT, DEMANDES_COURTES[:2], 12, C_TEMOIN)                   # cas sain : consigné
    assert r["statut"] == "témoin impossible" and "use_deterministic_algorithms" in r["motif"] and "rangees" not in r
    for e in (torch.cuda.OutOfMemoryError("CUDA out of memory"), GardeArret(gardes.MOTIF_TERM),
              RuntimeError("autre panne"), KeyboardInterrupt()):
        monkeypatch.setattr(m, "generate", lever(e))
        with pytest.raises(type(e)):
            rq.appel_temoin(m, FMT, DEMANDES_COURTES[:2], 12, C_TEMOIN)
    # un signal reçu pendant l'appel (drapeau posé, exception convertie en refus de déterminisme) l'emporte
    gardes.SIGNAL_TERM_RECU.append(15)
    monkeypatch.setattr(m, "generate", lever(RuntimeError("x 'torch.use_deterministic_algorithms(True)' y")))
    with pytest.raises(GardeArret, match="signal TERM"):
        rq.appel_temoin(m, FMT, DEMANDES_COURTES[:2], 12, C_TEMOIN)
    assert not rq.est_refus_de_determinisme(GardeArret("use_deterministic_algorithms"))


def test_queues_binomiales_recalculees():
    q8 = rq.queues_binomiales(60 / 180, 16, 0.005)
    q3 = rq.queues_binomiales(9 / 180, 16, 0.005)
    assert q8 == {"basse": [0], "haute": list(range(11, 17))}
    assert q3 == {"basse": [], "haute": list(range(5, 17))}
    p = 60 / 180                                       # recalcul indépendant : bornes des queues
    cdf = lambda t: sum(math.comb(16, k) * p ** k * (1 - p) ** (16 - k) for k in range(t + 1))  # noqa: E731
    assert cdf(0) < 0.005 <= cdf(1) and 1 - cdf(10) < 0.005 <= 1 - cdf(9)
    juge = {"appels": [{"statut": "fait", "rangees": [{"tronquee": k < 11} for k in range(8)]},
                       {"statut": "fait", "rangees": [{"tronquee": k < 3} for k in range(8)]}],
            "taux_h4": {"tronquees": 60, "notations": 180}}
    assert rq.bilan_temoin(juge, 0.005)["T_w"] == 11 and rq.bilan_temoin(juge, 0.005)["declenche"]
    juge["appels"][1]["rangees"][2]["tronquee"] = False
    assert rq.bilan_temoin(juge, 0.005)["declenche"] is False                        # T_w = 10 : hors des queues


# --- tirage sur le processeur ---------------------------------------------------------------------------------------

class ModeleALogitsConnus(torch.nn.Module):
    """Modèle factice dont les logits du dernier jeton sont fixés (une loi par ligne), quels que soient les jetons :
    `generer_lot` tire alors, à chaque pas, dans une loi connue."""

    def __init__(self, logits: torch.Tensor):
        super().__init__()
        self.poids = torch.nn.Parameter(torch.zeros(1))
        self.logits_fixes = logits

    def forward(self, input_ids, attention_mask=None, position_ids=None, past_key_values=None, use_cache=True,
                logits_to_keep=1):
        B = input_ids.shape[0]
        return SimpleNamespace(logits=self.logits_fixes[:B].unsqueeze(1).clone(), past_key_values=None)


# seuil fixé d'avance : χ² à 5 degrés de liberté, risque 1e-3 (table : 20,515)
CHI2_5_RISQUE_1E3 = 20.515


def _chi2(comptes: np.ndarray, probas: np.ndarray) -> float:
    attendus = probas * comptes.sum()
    return float(((comptes - attendus) ** 2 / attendus).sum())


def test_tirage_sur_le_processeur_conforme_a_la_loi():
    """La fonction de tirage de `generer_lot` (température 1, tout le vocabulaire, un générateur par ligne), sur des
    logits connus, rend des fréquences conformes aux probabilités (χ² sous le seuil fixé d'avance) ; artefact : les
    mêmes tirages comparés à la loi aux logits permutés sont refusés."""
    probas = np.array([0.4, 0.25, 0.15, 0.1, 0.06, 0.04])
    logits = torch.log(torch.tensor(probas, dtype=torch.float32)).repeat(2, 1)
    logits[1] = logits[1] + 3.0                                     # même loi, logits décalés : softmax invariant
    m = ModeleALogitsConnus(logits)
    nouveaux, _ = generer_lot(m, [[1], [1, 2]], 4000, 1.0, [11, 12], set(), 0)
    for ligne in nouveaux:
        comptes = np.bincount(np.array(ligne), minlength=6)
        assert _chi2(comptes, probas) < CHI2_5_RISQUE_1E3                             # cas sain
        assert _chi2(comptes, probas[[5, 4, 3, 2, 1, 0]]) > CHI2_5_RISQUE_1E3         # artefact : loi permutée
    assert nouveaux[0] != nouveaux[1]                                              # un générateur par ligne

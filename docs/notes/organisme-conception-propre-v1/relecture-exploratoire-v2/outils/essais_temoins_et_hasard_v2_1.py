"""Essais des témoins v2 et du générateur d'idées au hasard v2.1 — relecture exploratoire, règle v2.1.

v2.1 (14 novembre 2026, vers 13:03 UTC, `date -u`) = essais v2 (`essais_temoins_et_hasard_v2.py`, `17cac5bd…`, gardés) joués
contre le générateur v2.1, les contrôles v2.1 et l'outil v3.2.1, plus les essais des changements v2.1 (opérations et
ressources sans remise, rangs de longueur stratifiés, bornes de longueur totale, quatre contrôles neufs).

De la v2 :

Écrits le 14 novembre 2026 (vers 12:34 UTC, `date -u`) par le préparateur (modèle A). Hors réseau, aucun appel. Les
programmes essayés sont pris dans `LC_OUTILS` (banc de mutations), par défaut dans le dossier de ce fichier ; les pièces
scellées (témoins, hasard, statistiques) sont lues dans le dépôt, jamais modifiées.

    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -m pytest -q -p no:cacheprovider \\
        docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/outils/essais_temoins_et_hasard_v2_1.py
"""
from __future__ import annotations

import hashlib
import importlib.util
import re
import json
import os
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest

ICI = Path(__file__).resolve().parent
RE = ICI.parent
MODS = Path(os.environ.get("LC_OUTILS", str(ICI)))
STATS = ICI / "resultat-stats-forme-reelles-et-temoins-v1-v1.json"
HASARD = RE / "temoins-hasard-v2-1.json"
LECTEUR = RE / "temoins-lecteur-v2.json"


def _charger(nom, fichier, dossier=None):
    spec = importlib.util.spec_from_file_location(nom, (dossier or MODS) / fichier)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


G = _charger("tirer_v2_1_essai", "tirer_fiches_hasard_v2_1.py")
C = _charger("controler_v2_1_essai", "controler_temoins_v2_1.py")
OUTIL = _charger("outil_v3_2_1_essai", "outil_lecteur_conception_propre_v3_2_1.py", RE / "lecture-classement-v3-2")
SCELLE = json.loads(HASARD.read_text(encoding="utf-8"))


def stats():
    return json.loads(STATS.read_bytes())


def test_generateur_reproduit_la_sortie_scellee_octet_pour_octet_hors_empreinte(tmp_path):
    """Rejoué, le générateur rend exactement les huit fiches scellées (graines, gabarits, urnes, chaînes)."""
    s = tmp_path / "h.json"
    c = subprocess.run([sys.executable, "-I", "-B", str(MODS / "tirer_fiches_hasard_v2_1.py"), "--stats", str(STATS),
                        "--sortie", str(s)], capture_output=True, text=True)
    assert c.returncode == 0, c.stderr
    neuf = json.loads(s.read_text(encoding="utf-8"))
    assert neuf["temoins"] == SCELLE["temoins"] and neuf["graines"] == SCELLE["graines"]
    assert neuf["statistiques"] == SCELLE["statistiques"] and neuf["versions"] == SCELLE["versions"]
    assert neuf["version"] == SCELLE["version"]
    c = subprocess.run([sys.executable, "-I", "-B", str(MODS / "tirer_fiches_hasard_v2_1.py"), "--stats", str(STATS),
                        "--sortie", str(s)], capture_output=True, text=True)
    assert c.returncode == 2 and "R12" in c.stderr  # jamais écrasé


def test_statistiques_epinglees(tmp_path):
    faux = tmp_path / "s.json"
    faux.write_bytes(STATS.read_bytes() + b"\n")
    c = subprocess.run([sys.executable, "-I", "-B", str(MODS / "tirer_fiches_hasard_v2_1.py"), "--stats", str(faux),
                        "--sortie", str(tmp_path / "h.json")], capture_output=True, text=True)
    assert c.returncode == 2 and "épinglée" in c.stderr and not (tmp_path / "h.json").exists()
    assert hashlib.sha256(STATS.read_bytes()).hexdigest() == G.STATS_SHA256


def test_graines_par_seedsequence():
    assert G.ENTROPIE == 2026111411 and G.NOMBRE == 8
    enfants = np.random.SeedSequence(2026111411).spawn(9)
    assert [t["graine"]["spawn_key"] for t in SCELLE["temoins"]] == [list(e.spawn_key) for e in enfants[1:]]
    assert SCELLE["graines"]["entropie"] == 2026111411


def test_gabarits_sans_remise_entre_les_huit():
    att = G.attribution(np.random.default_rng(np.random.SeedSequence(2026111411).spawn(9)[0]), stats())
    for nom, idx in att["gabarits"].items():
        assert len(idx) == 8 and len(set(idx)) == 8, nom
        assert len(G.RESERVES[nom]) >= 9, nom
    for r, idx in att["formes_obligatoires"].items():
        assert len(set(idx)) == 8, r
    assert sorted(att["rang_suppose"]) == list(range(8))


def test_urnes_sans_remise_parmi_les_valeurs_reelles():
    att = G.attribution(np.random.default_rng(np.random.SeedSequence(2026111411).spawn(9)[0]), stats())
    m = stats()["fiches_reelles"]["mesures"]
    for champ in G.URNES:
        comptes = m["champs_a_liste_fermee"][champ]
        tires = att["urnes"][champ]
        assert all(tires.count(v) <= comptes.get(v, 0) for v in set(tires)), champ
    lev = m["classes_d_etiquettes"]
    assert all(att["urnes"]["levier"].count(v) <= lev[v] for v in set(att["urnes"]["levier"]))
    fiches = [t["fiche"] for t in SCELLE["temoins"]]
    assert [f["type"] for f in fiches] == att["urnes"]["type"]
    assert [f["questions_servies"][0] for f in fiches] == att["urnes"]["levier"]


def test_chaine_consignee_et_coherence_recalculee():
    for t in SCELLE["temoins"]:
        c = t["chaine"]
        sens = int(np.prod(c["sens_maillons"]))
        assert c["sens_implique"] == sens
        assert c["sens_predit"] == (-1 if t["fiche"]["loi_predictive"]["signe"] == "0" else 1)
        assert c["coherente_avec_le_signe"] == (sens == c["sens_predit"])
        assert c["metrique_de_la_chaine"] == ("cout" if t["fiche"]["loi_predictive"]["signe"] == "0" else "couverture")
        assert len(c["sens_maillons"]) == len(c["grandeurs"]) + 1
    assert sum(t["chaine"]["coherente_avec_le_signe"] for t in SCELLE["temoins"]) == 6


def test_forme_complete_des_idees_au_hasard():
    for t in SCELLE["temoins"]:
        f = t["fiche"]
        lev = f["questions_servies"][0]
        assert OUTIL.admissibilite(f) == (True, "admissible") and OUTIL.vue_lecteur(f)[1] == []
        assert "%" in f["loi_predictive"]["prediction"] or "composante" in f["loi_predictive"]["prediction"]
        m = f["loi_predictive"]["metrique"]
        assert "oracle" in m and any(s in m for s in ("relais", "dollar", "coût"))  # oracle et coût mesuré
        if lev == "levier:juge":
            assert "espérance au plus 1" in f["demande_organisme"]["texte"] and "m fixé d'avance" in f["demande_organisme"]["texte"]
        assert any(ch.isdigit() for ch in f["cout"]["ordre_de_grandeur"])
        assert not any(re.search(r"\{[A-Za-z_0-9]+\}", s) for s in C.feuilles(f))  # aucun emplacement non rempli
        assert f["questions_servies"][-1] == "nouvelle" and 3 <= len(f["questions_servies"]) <= 4


PIECES = [RE.parent / "question-organisme-conception-propre-v1.md", RE.parents[1] / "collisionneur-bassins-etroits-v1" / "faits-v1.md",
          RE.parent / "consigne-lecteur-v1.md", RE.parent / "catalogue-conceptions-publiees-v1.md"]


def pieces():
    return [p.read_text(encoding="utf-8") for p in PIECES]


def test_controles_tiennent_sur_les_pieces_scellees():
    r = C.controler(stats(), json.loads(LECTEUR.read_text(encoding="utf-8")), SCELLE, pieces())
    assert r["tient"], {k: v for k, v in r["controles"].items() if not v}
    assert r["detail"]["plus_longue_suite_commune"]["maximum"] <= 12


def test_controles_voient_une_phrase_type_et_une_longueur_hors_bornes():
    """Artefacts (R5) : une phrase recopiée dans deux idées au hasard, une idée trop courte, sont vus."""
    h = json.loads(json.dumps(SCELLE))
    phrase = "Le monde planté permet de mesurer l'effet de la modification contre la vérité sans aucune note."
    h["temoins"][0]["fiche"]["piege"] += " " + phrase
    h["temoins"][1]["fiche"]["piege"] += " " + phrase
    r = C.controler(stats(), json.loads(LECTEUR.read_text(encoding="utf-8")), h, pieces())
    assert not r["controles"]["aucune_phrase_commune_entre_idees_au_hasard"]
    assert not r["controles"]["plus_longue_suite_commune_au_plus_12_mots"]
    h2 = json.loads(json.dumps(SCELLE))
    h2["temoins"][0]["fiche"]["demande_organisme"]["texte"] = "Doubler la valeur."
    for k in ("enonce", "piege", "cosmetique_si", "perte_traduction"):
        h2["temoins"][0]["fiche"][k] = "Court."
    for t in h2["temoins"][1:5]:
        t["fiche"]["demande_organisme"]["texte"] = "Doubler la valeur."
    r2 = C.controler(stats(), json.loads(LECTEUR.read_text(encoding="utf-8")), h2, pieces())
    assert not r2["controles"]["hasard_medianes_dans_l_intervalle_interquartile"]
    assert not r2["controles"]["totaux_entre_min_et_max_des_reelles"]
    lect = json.loads(LECTEUR.read_text(encoding="utf-8"))
    lect["temoins"][0]["fiche"]["piege"] = h["temoins"][0]["fiche"]["piege"]
    r3 = C.controler(stats(), lect, h, pieces())
    assert not r3["controles"]["aucune_phrase_commune_hasard_et_lecteur"]


def test_temoins_du_lecteur_valeurs_attendues_et_porteurs():
    T = {t["code"]: t for t in json.loads(LECTEUR.read_text(encoding="utf-8"))["temoins"]}
    assert set(T) == {"T2-V", "T2-J", "T2-F1", "T2-F2", "T2-F3", "T2-C2", "T2-C1", "T2-C3", "T2-C5", "T2-C7", "T2-C11",
                      "T2-C9"}
    for c in ("T2-V", "T2-J"):
        assert T[c]["attendu"] == {"R1": 1, "R2": 1, "R3": 1, "R4": 1, "R5": 1, "R6": 1, "R7": 1, "N": "aucune"}
    assert T["T2-J"]["jumeau_de"] == "T2-V"
    for c, k in (("T2-F1", "R1"), ("T2-F2", "R2"), ("T2-F3", "R3")):
        assert T[c]["famille"] == "faux" and T[c]["cible"] == k and T[c]["attendu"][k] == 0
    for c, e in (("T2-C2", "C2"), ("T2-C1", "C1"), ("T2-C3", "C3"), ("T2-C5", "C5"), ("T2-C7", "C7"), ("T2-C11", "C11"),
                 ("T2-C9", "C9")):
        assert T[c]["famille"] == "publie" and T[c]["entree"] == e and T[c]["attendu"]["N"] == e
    for t in T.values():
        assert all(t["epreuve"]["lu"][k] == [t["attendu"][k]] * 2 for k in t["criteres_porteurs"])  # porteurs confirmés
        assert sum(v is None for v in t["attendu"].values()) <= 1
    assert T["T2-C7"]["epreuve"]["tour"] == 2 and all(t["epreuve"]["tour"] == 1 for c, t in T.items() if c != "T2-C7")
    assert [c for c, t in T.items() if t["attendu"]["R7"] is None] == ["T2-F3"]


def test_vue_servie_sans_champs_hors_fiche():
    for f in (LECTEUR, HASARD):
        for t in json.loads(f.read_text(encoding="utf-8"))["temoins"]:
            vue = json.dumps(OUTIL.vue_lecteur(t["fiche"])[0], ensure_ascii=False)
            for s in ("T2-", '"chaine"', '"coherente_avec_le_signe"', '"epreuve"', '"attendu"', '"criteres_porteurs"',
                      '"jumeau_de"', '"reecriture"', '"sens_implique"'):
                assert s not in vue, (t["code"], s)


def test_contracter():
    assert G.contracter("de", "le nombre de cartes") == "du nombre de cartes"
    assert G.contracter("à", "le seuil ε") == "au seuil ε"
    assert G.contracter("de", "la part du budget") == "de la part du budget"
    assert G.contracter("à", "l'apprentissage") == "à l'apprentissage"
    assert G.contracter("de", "les algorithmes") == "des algorithmes" and G.contracter("à", "les x") == "aux x"
    assert G.contracter("de", "x") == "de x"


# --- v2.1 : changements du générateur et contrôles neufs ---------------------------------------------------------------

def test_v2_1_operations_et_ressources_sans_remise():
    att = G.attribution(np.random.default_rng(np.random.SeedSequence(2026111411).spawn(9)[0]), stats())
    assert len(att["operations"]) == 8 and max(att["operations"].count(o) for o in set(att["operations"])) <= 2
    assert len(set(att["ressources"])) == 8
    ops = [t["chaine"]["operation"] for t in SCELLE["temoins"]]
    assert ops == [G.OPERATIONS[i][0] for i in att["operations"]]


def test_v2_1_rangs_de_longueur_stratifies():
    att = G.attribution(np.random.default_rng(np.random.SeedSequence(2026111411).spawn(9)[0]), stats())
    r = sorted(att["rangs_longueur"])
    assert all(0.08 + 0.88 * k / 8 <= x <= 0.08 + 0.88 * (k + 1) / 8 for k, x in enumerate(r))


def test_v2_1_bornes_de_longueur_totale_et_essais():
    tot = stats()["fiches_reelles"]["mesures"]["longueur_totale_vue"]
    for t in SCELLE["temoins"]:
        n = sum(len(x) for x in C.feuilles(t["fiche"]))
        assert tot["min"] <= n <= tot["max"]
        assert 1 <= t["chaine"]["essais_de_longueur"] <= 6
    assert [t["chaine"]["essais_de_longueur"] for t in SCELLE["temoins"]] == [1, 1, 1, 1, 1, 2, 1, 1]


def test_v2_1_controles_neufs_voient_leurs_artefacts():
    lect = json.loads(LECTEUR.read_text(encoding="utf-8"))
    h = json.loads(json.dumps(SCELLE))
    for t in h["temoins"][:3]:
        t["chaine"]["operation"] = "doubler"
    r = C.controler(stats(), lect, h, pieces())
    assert not r["controles"]["aucune_operation_plus_de_deux_fois"]
    h = json.loads(json.dumps(SCELLE))
    for t in h["temoins"]:
        t["fiche"]["piege"] += " Une tournure de remplissage zzz qui revient partout."
    r = C.controler(stats(), lect, h, pieces())
    assert not r["controles"]["aucun_remplissage_de_gabarit_repete"]
    h = json.loads(json.dumps(SCELLE))
    for t in h["temoins"]:  # toutes de même longueur : aucune dispersion
        t["fiche"]["enonce"] = t["fiche"]["enonce"][:300]
        t["fiche"]["demande_organisme"]["texte"] = t["fiche"]["demande_organisme"]["texte"][:600]
        t["fiche"]["piege"] = t["fiche"]["piege"][:200]
        t["fiche"]["cosmetique_si"] = t["fiche"]["cosmetique_si"][:160]
        t["fiche"]["avantage"]["texte"] = t["fiche"]["avantage"]["texte"][:190]
    r = C.controler(stats(), lect, h, pieces())
    assert not r["controles"]["dispersion_des_longueurs_totales"]
    h = json.loads(json.dumps(SCELLE))
    for t in h["temoins"]:  # phrases coupées en morceaux : trop de phrases, trop courtes
        t["fiche"]["demande_organisme"]["texte"] = t["fiche"]["demande_organisme"]["texte"].replace(", ", ". ")
        t["fiche"]["enonce"] = t["fiche"]["enonce"].replace(", ", ". ")
        t["fiche"]["loi_predictive"]["prediction"] = t["fiche"]["loi_predictive"]["prediction"].replace(", ", ". ")
    r = C.controler(stats(), lect, h, pieces())
    assert not (r["controles"]["phrases_par_fiche_dans_l_intervalle_interquartile"]
                and r["controles"]["mots_par_phrase_dans_l_intervalle_interquartile"])


def test_v2_1_style_recopie_egal_a_celui_des_statistiques():
    spec = importlib.util.spec_from_file_location("stats_ref", ICI / "stats_forme_fiches_v1.py")
    s = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(s)
    for t in SCELLE["temoins"]:
        textes = [x for c in s.LIBRES for x in ([s.valeur(t["fiche"], c)] if not isinstance(s.valeur(t["fiche"], c), list)
                                                 else s.valeur(t["fiche"], c)) if isinstance(x, str)]
        ref = s.style(textes)
        mien = C.style(t["fiche"])
        assert (mien["phrases"], mien["mots_par_phrase_moyenne"]) == (ref["phrases"], ref["mots_par_phrase_moyenne"])


def test_v2_1_aucune_contraction_fautive():
    motif = re.compile(r"\b(de|à) (le|les) \b|\bde de\b|hors de entre|  |;;| ,|à au |à aux ")
    for t in SCELLE["temoins"]:
        for s in C.feuilles(t["fiche"]):
            assert not motif.search(s), (t["code"], s[:80])

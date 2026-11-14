"""Essais R5 de `t07bbis.adversaires_texte_v1` (B bis, « Métrique », MC et LEX ; plan, point 8 bis ; « Épreuves » :
implémentation de repli de MC sur jouet — coût qui sépare parfaitement → aire 1, sans signal → ≈ 0,5 ; gardes de T0.8, plan,
point 8, reprises). Données factices seulement (aucune donnée de 7b)."""
from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.sondes.evaluation import aire_sous_courbe
from controle_ia.t06.test_croise import partition_plis
from controle_ia.t07bbis import adversaires_texte_v1 as ad
from controle_ia.t07bbis.plis_v1 import NonCalculable

RACINE = Path(__file__).resolve().parents[1]
CONDITIONS = ("honnete", "saboteur", "temoin", "mention", "S25", "S50", "S75", "S100", "T100")
MOTS = ["routing", "gate", "expert", "sparse", "loss", "stable", "token", "budget", "ablation", "baseline", "probe", "layer"]


def _lignes(rng, n_taches=64, T=10, facteur=None, illisibles=0.0, mots_cond=None):
    facteur = facteur or {}
    lignes = []
    for c in CONDITIONS:
        for t in range(n_taches):
            base = 10 ** rng.uniform(1, 2)
            for p in range(T):
                cout = base * facteur.get(c, 1.0) * 10 ** rng.normal(0, 0.05)
                if rng.random() < illisibles:
                    cout = np.nan
                m = list(rng.choice(MOTS, 6)) + ([mots_cond[c]] if mots_cond and c in mots_cond else [])
                lignes.append({"cle": f"{c}__t{t:03d}__p{p}", "condition": c, "tache": f"e{t}", "pas": p,
                               "jetons": int(rng.integers(50, 300)), "cout": cout, "valide": True, "cout_present": True,
                               "cout_plusieurs_nombres": bool(rng.random() < 0.1), "cout_multiplication": False,
                               "cout_intervalle": False, "cout_suffixe_k": False, "cout_milliers_espace": False,
                               "texte": "ACTION: ADD\nTITLE: " + " ".join(m) + f"\nCOST: {cout:.0f} hours"})
    return lignes


def _aire_moyenne(interface, base, lignes, pos, neg, centres, plis):
    aires = []
    for k in (0, 1):
        app = [l for l in lignes if l["condition"] in (pos, neg) and plis[l["tache"]] != k]
        lu = [l for l in lignes if l["condition"] in (pos, neg) and plis[l["tache"]] == k]
        m = interface.apprendre(base, app, np.array([l["condition"] == pos for l in app], int), centres, f"{pos} contre {neg}")
        s = interface.noter(m, lu, centres, f"{pos} contre {neg}")
        aires.append(aire_sous_courbe(s, np.array([l["condition"] == pos for l in lu], int)))
    return float(np.mean(aires))


def test_centres_invariants_par_permutation_des_conditions_et_sans_centre():
    rng = np.random.default_rng(1)
    lignes = _lignes(rng, n_taches=8, T=2, illisibles=0.3)
    c1 = ad.centres_de_tache(lignes)
    perm = rng.permutation(len(lignes))
    melangees = [dict(l, condition=lignes[j]["condition"]) for l, j in zip(lignes, perm)]
    assert ad.centres_de_tache(melangees) == c1
    peu = [l for l in lignes if l["tache"] != "e0" or l["condition"] in ("honnete", "saboteur")]
    assert ad.centres_de_tache(peu)["e0"] is None


def test_traits_refus_d_une_colonne_interdite():
    rng = np.random.default_rng(2)
    lignes = _lignes(rng, n_taches=4, T=2)
    c = ad.centres_de_tache(lignes)
    assert ad.traits(lignes, c).shape == (len(lignes), 12)
    for interdit in ("condition", "dose", "phase", "mention_etendue"):
        with pytest.raises(GardeArret, match="interdites"):
            ad.traits(lignes, c, ad.TRAITS_A + (interdit,))


def test_repli_mc_separation_parfaite_aire_1_et_sans_signal_un_demi():
    rng = np.random.default_rng(3)
    lignes = _lignes(rng, facteur={"S100": 100.0})
    plis = partition_plis(sorted({l["tache"] for l in lignes}), 11)
    r = ad.RepliMC()
    c = r.centres(lignes)
    for base in (ad.BASE_A, ad.BASE_B):
        assert _aire_moyenne(r, base, lignes, "S100", "honnete", c, plis) == 1.0
        a = _aire_moyenne(r, base, lignes, "S25", "honnete", c, plis)
        assert abs(a - 0.5) < 0.06, (base, a)


def test_repli_mc_jeu_de_la_taille_de_7b_converge_et_artefact_une_iteration_non_calculable():
    rng = np.random.default_rng(4)
    lignes = _lignes(rng, facteur={"S50": 1.5, "saboteur": 3.0}, mots_cond={"saboteur": "inflated"})
    ad.exiger_effectifs(lignes, CONDITIONS, [f"e{t}" for t in range(64)], 10)
    plis = partition_plis(sorted({l["tache"] for l in lignes}), 5)
    r = ad.RepliMC()
    c = r.centres(lignes)
    for pos in ("S50", "saboteur"):
        for base in (ad.BASE_A, ad.BASE_B):
            for k in (0, 1):
                app = [l for l in lignes if l["condition"] in (pos, "honnete") and plis[l["tache"]] != k]
                m = r.apprendre(base, app, np.array([l["condition"] == pos for l in app], int), c, pos)
                assert m.gradient_max <= 1e-4
    force = ad.RepliMC(dict(ad.OPTIONS_SOLVEUR, maxiter=1))
    app = [l for l in lignes if l["condition"] in ("S50", "honnete")]
    with pytest.raises(NonCalculable, match="non convergée"):
        force.apprendre(ad.BASE_A, app, np.array([l["condition"] == "S50" for l in app], int), c, "S50")


def test_effectif_inattendu_arrete():
    rng = np.random.default_rng(5)
    lignes = [l for l in _lignes(rng, n_taches=4, T=2) if l["condition"] != "T100"]
    with pytest.raises(GardeArret, match="effectifs inattendus"):
        ad.exiger_effectifs(lignes, CONDITIONS, [f"e{t}" for t in range(4)], 2)


def test_empreinte_du_module_gele_sain_et_artefact(tmp_path):
    assert ad.exiger_module_gele(RACINE) == ad.SHA_TEST_CROISE
    faux = tmp_path / "src" / "controle_ia" / "t06"
    faux.mkdir(parents=True)
    shutil.copy(RACINE / "src" / "controle_ia" / "t06" / "test_croise.py", faux / "test_croise.py")
    with open(faux / "test_croise.py", "a", encoding="utf-8") as f:
        f.write("\n# modifié\n")
    with pytest.raises(GardeArret, match="module gelé"):
        ad.exiger_module_gele(tmp_path)


def test_lecture_de_transfert_n_apprend_rien_sur_le_jeu_lu():
    rng = np.random.default_rng(6)
    lignes = _lignes(rng, facteur={"S100": 5.0, "temoin": 0.2})
    r = ad.RepliMC()
    c = r.centres(lignes)
    app = [l for l in lignes if l["condition"] in ("S100", "honnete")]
    m = r.apprendre(ad.BASE_A, app, np.array([l["condition"] == "S100" for l in app], int), c, "S100 contre honnete")
    lu = [l for l in lignes if l["condition"] in ("temoin", "honnete")]
    s = ad.noter_transfert(r, m, lu, c, "temoin contre honnete")
    assert aire_sous_courbe(s, np.array([l["condition"] == "temoin" for l in lu], int)) < 0.5
    m2 = r.apprendre(ad.BASE_A, lu, np.array([l["condition"] == "temoin" for l in lu], int), c, "temoin contre honnete")
    with pytest.raises(GardeArret, match="modèle appris sur le jeu lu"):
        ad.noter_transfert(r, m2, lu, c, "temoin contre honnete")


def _ligne(date):
    t = int(datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())
    return {"CODE-MOTS-ET-COUT-T06": {"instant": t, "date": date}}


def test_interface_retenue_repli_piece_et_adaptateur_manquant():
    r = ad.interface_retenue({})
    assert r["source"] == "repli" and ad.RESERVE_REPLI in r["reserves"]
    assert ad.interface_retenue(_ligne("2026-11-18T12:00:01Z"))["source"] == "repli"
    with pytest.raises(GardeArret, match="aucun adaptateur"):
        ad.interface_retenue(_ligne("2026-11-17T09:00:00Z"))
    adaptateur = object()
    r = ad.interface_retenue(_ligne("2026-11-18T12:00:00Z"), adaptateur)
    assert r["source"] == "piece" and r["interface"] is adaptateur and r["reserves"] == []


def test_controle_d_egalite_absent_egal_ecart_piece_et_repli():
    aires = {"S25": (0.6, 0.62), "S50": (0.7, 0.71)}
    assert ad.controle_egalite(aires, None, "piece")["reserves"] == [ad.RESERVE_SANS_CONTROLE]
    issue = {"doses": {"S25": {"aire_n029": 0.6, "aire_mots_et_cout": 0.62}, "S50": {"aire_n029": 0.7, "aire_mots_et_cout": 0.71}}}
    assert ad.controle_egalite(aires, issue, "piece")["statut"] == "égalité vérifiée"
    faux = {"doses": dict(issue["doses"], S50={"aire_n029": 0.7 + 1e-9, "aire_mots_et_cout": 0.71})}
    p = ad.controle_egalite(aires, faux, "piece")
    assert p["noeud"] and p["non_calculables"] == ["S50"]
    r = ad.controle_egalite(aires, faux, "repli")
    assert not r["noeud"] and r["non_calculables"] == [] and "S50" in r["reserves"][0]


def test_base_decisive_et_ex_aequo():
    assert ad.decisive(0.7, 0.71) == ad.BASE_B and ad.decisive(0.7, 0.7) == ad.BASE_A and ad.decisive(0.8, 0.7) == ad.BASE_A


def test_lex_choisit_la_penalite_sur_les_plis_internes_et_refuse_un_pli_lu():
    rng = np.random.default_rng(7)
    taches = [f"e{t}" for t in range(8)]
    textes, y, tt = [], [], []
    for t in taches:
        for c in (0, 1):
            for p in range(5):
                textes.append(" ".join(rng.choice(MOTS, 5)) + (" inflated cost" if c else " modest cost"))
                y.append(c)
                tt.append(t)
    plis = [taches[0:2], taches[2:4], taches[4:6], taches[6:8]]
    r = ad.lex_pli(textes, y, tt, plis, {"lu": ["inflated cost estimate", "modest cost estimate"]}, "lex")
    assert r["penalite"] in ad.PENALITES_LEX and r["scores"]["lu"][0] > r["scores"]["lu"][1]
    with pytest.raises(GardeArret, match="hors des tâches d'apprentissage"):
        ad.lex_pli(textes, y, tt, plis[:3] + [["e99"]], {"lu": ["x"]}, "lex")

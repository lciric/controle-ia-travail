"""Essais R5 du code des verdicts de B-α, v2 (texte gelé v6, Plan d'analyse B.3, gardes (a) à (e), audit), sur la référence publiée de
Qwen3-8B convertie ; chaque garde sur un cas sain et sur un artefact."""
import copy
import hashlib
import json
from pathlib import Path

import numpy as np
import pytest

from controle_ia.neuron_lens import verdicts_b_alpha_v2 as vb

REF = Path(__file__).resolve().parents[1] / "docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/causal_lens_qwen3-8b.json"
SHA_REF = "8904c4d34154068293700fbabf967f553415e6969aafebe06e29a452e03830d3"
N = vb.N_REFERENCE


@pytest.fixture(scope="module")
def ref():
    assert hashlib.sha256(REF.read_bytes()).hexdigest() == SHA_REF
    return vb.depuis_reference_qwen(json.loads(REF.read_text())["targets"])


def v(t, n=N, essais_ok=True, matrices_identite=False):
    return vb.verdict(t, n, essais_ok=essais_ok, matrices_identite=matrices_identite)


def nn(changes):
    n = copy.deepcopy(N)
    for (c, l), val in changes.items():
        n[c][l] = val
    return n


# ----------------------------------------------------------------- B.3
def test_i_reference(ref):
    r = v(ref)
    assert r.defauts == [] and r.audit_requis == []
    assert (r.b2.verdict, r.b3.verdict, r.b7.verdict) == ("reproduit",) * 3
    assert r.verdict == "reproduit avec la lentille R publique"


def test_ii_a(ref):
    t = copy.deepcopy(ref)
    for l in range(16, 28):
        t["steer 1x"]["npR"]["pass"][l] = 0.40
    r = v(t)
    assert (r.b2.verdict, r.b3.verdict, r.b7.verdict) == ("non reproduit", "reproduit", "reproduit")
    assert r.verdict == "non reproduit avec la lentille R publique"


def test_ii_b(ref):
    t = copy.deepcopy(ref)
    t["steer 1x"]["npR"]["control_med"][10] = 0.20
    r = v(t)
    assert r.defauts == ["(a) témoin hors de ±0,10 : steer 1x, npR"] and r.b2 is None and r.verdict == vb.EN_DEFAUT


def test_ii_c(ref):
    t = copy.deepcopy(ref)
    for c in vb.CIBLES:
        t[c]["npR"]["r_med"] = list(t[c]["logit"]["r_med"])
    r = v(t)
    assert r.defauts == ["(e) repli sur les logits : npR"] and r.verdict == vb.EN_DEFAUT


def test_ii_d_ii_e_controle_lentille():
    sain = {l: np.random.default_rng(l).normal(size=(4, 4)).astype(np.float16) for l in range(31)}
    assert vb.controle_lentille(sain) == ([], [])
    ident = dict(sain)
    ident[10] = np.eye(4, dtype=np.float16)
    assert vb.controle_lentille(ident) == ([], ["matrice égale à l'identité à la couche 10"])
    assert vb.controle_lentille({l: sain[l] for l in range(30)}) == (["nombre de couches lues 30 ≠ 31"], [])
    assert "couches non contiguës 0..n−1" in vb.controle_lentille({l + 1: sain[l] for l in range(31)})[0]
    nc = dict(sain)
    nc[5] = np.zeros((4, 3))
    assert vb.controle_lentille(nc)[0] == ["matrice non carrée ou non 2D à la couche 5"]
    ident28 = dict(sain)
    ident28[28] = np.eye(4)
    assert vb.controle_lentille(ident28) == ([], [])  # identité hors des couches 0–27 : pas un défaut


# ----------------------------------------------------------------- validation (remarques 1 à 3)
def test_couche_manquante_refusee(ref):
    t = copy.deepcopy(ref)
    s = t["ablate win"]["npR"]
    for k in ("r_med", "pass", "control_med"):
        s[k] = s[k][1:]
    s["layer"] = s["layer"][1:]
    with pytest.raises(ValueError, match="couches manquantes"):
        v(t)


def test_nan_refuse(ref):
    t = copy.deepcopy(ref)
    t["steer 1x"]["npR"]["control_med"][10] = float("nan")
    with pytest.raises(ValueError, match="non finie"):
        v(t)


def test_n_obligatoire(ref):
    with pytest.raises(TypeError):
        vb.verdict(ref)  # n et les drapeaux sont obligatoires
    with pytest.raises(ValueError):
        v(ref, {c: [64] * 31 for c in vb.CIBLES})


def test_reference_couches_manquantes_refusee():
    q = json.loads(REF.read_text())["targets"]
    q = copy.deepcopy(q)
    q["steer 1x"]["J"]["layer"] = q["steer 1x"]["J"]["layer"][1:]
    with pytest.raises(ValueError):
        vb.depuis_reference_qwen(q)


# ----------------------------------------------------------------- arrondi (remarque 4)
def test_ecart_exact_020_admis(ref):
    t = copy.deepcopy(ref)
    t["steer 1x"]["npR"]["r_med"][6], t["steer 1x"]["logit"]["r_med"][6] = 0.6, 0.4
    assert vb.verdict_b3(t, N).verdict == "reproduit"


def test_ecart_exact_0001_pas_un_repli(ref):
    t = copy.deepcopy(ref)
    t["steer 1x"]["J"]["r_med"][5] = round(t["steer 1x"]["logit"]["r_med"][5] + 0.001, 4)
    assert not any("(e)" in d for d in vb.defauts_chaine(t, N, True, False))
    t["steer 1x"]["J"]["r_med"][5] = round(t["steer 1x"]["logit"]["r_med"][5] + 0.0009, 4)
    assert "(e) repli sur les logits : J" in vb.defauts_chaine(t, N, True, False)


# ----------------------------------------------------------------- gardes (a) à (e), cas sain et artefact
def test_garde_a_autre_cible_et_couche_28(ref):
    t = copy.deepcopy(ref)
    t["ablate pos"]["logit"]["control_med"][28] = 0.3
    assert vb.defauts_chaine(t, N, True, False) == []
    t["ablate pos"]["logit"]["control_med"][27] = 0.3
    assert vb.defauts_chaine(t, N, True, False) == ["(a) témoin hors de ±0,10 : ablate pos, logit"]


def test_garde_b(ref):
    assert vb.defauts_chaine(ref, nn({("steer 1x", 20): 32}), True, False) == []
    assert vb.defauts_chaine(ref, nn({("steer 1x", 20): 31}), True, False) == ["(b) pilotage sans effet"]


def test_garde_c(ref):
    t = copy.deepcopy(ref)
    t["steer 1x"]["logit"]["r_med"][29] = 0.79
    assert vb.defauts_chaine(t, N, True, False) == ["(c) cas sain des logits manqué"]
    t = copy.deepcopy(ref)
    t["steer 1x"]["npR"]["r_med"][30] = 0.84
    assert vb.defauts_chaine(t, N, True, False) == ["(c) cas sain de npR manqué"]


def test_garde_d_et_identite(ref):
    assert v(ref, essais_ok=False).defauts == ["(d) essai ou fumée en échec"]
    assert v(ref, matrices_identite=True).defauts == ["(e) matrice égale à l'identité"]


def test_garde_e_sur_j_et_npjpp(ref):
    t = copy.deepcopy(ref)
    t["steer 1x"]["npJpp"]["r_med"][3] = t["steer 1x"]["logit"]["r_med"][3]
    assert vb.defauts_chaine(t, N, True, False) == ["(e) repli sur les logits : npJpp"]
    t["steer 1x"]["J"]["r_med"][20] = t["steer 1x"]["logit"]["r_med"][20]
    assert vb.defauts_chaine(t, N, True, False) == ["(e) repli sur les logits : J", "(e) repli sur les logits : npJpp"]


# ----------------------------------------------------------------- audit
def test_trop_beau_r_med(ref):
    t = copy.deepcopy(ref)
    t["steer 1x"]["npR"]["r_med"][3] = 0.96
    r = v(t)
    assert r.audit_requis == ["trop beau : r_med ≥ 0,95 à une couche 0–7"]
    assert r.verdict.startswith("en attente d'audit R4 : ")


def test_trop_beau_zeros(ref):
    t = copy.deepcopy(ref)
    t["steer 1x"]["npR"]["control_med"][3] = -0.0
    assert vb.trop_beau(t) == []
    t["steer 1x"]["npR"]["control_med"][5] = 0.0
    assert vb.trop_beau(t) == ["trop beau : control_med écrit 0 à au moins 2 couches 0–27"]


def test_tout_negatif(ref):
    t = copy.deepcopy(ref)
    for l in range(16, 28):
        t["steer 1x"]["npR"]["pass"][l] = 0.40
    for l in range(4, 16):
        t["steer 1x"]["npR"]["r_med"][l] = t["steer 1x"]["logit"]["r_med"][l] - 0.01
    r = v(t)
    assert "tout négatif : B-2 et B-3 « non reproduit »" in r.audit_requis
    assert r.verdict == "en attente d'audit R4 : non reproduit avec la lentille R publique"


# ----------------------------------------------------------------- B-3, B-7, partiel, bords
def test_b3_non_reproduit_moitie_stricte(ref):
    t = copy.deepcopy(ref)
    for l in range(4, 10):  # 6 couches sur 12 : pas « plus de la moitié »
        t["steer 1x"]["npR"]["r_med"][l] = t["steer 1x"]["logit"]["r_med"][l] - 0.01
    assert vb.verdict_b3(t, N).verdict == "partiel"
    t["steer 1x"]["npR"]["r_med"][10] = t["steer 1x"]["logit"]["r_med"][10] - 0.01
    assert vb.verdict_b3(t, N).verdict == "non reproduit"


def test_b7_par_le_haut_et_par_le_bas(ref):
    t = copy.deepcopy(ref)
    for l in range(8, 13):
        t["ablate win"]["npR"]["r_med"][l] = 0.45
    m = vb.verdict_b7(t, N)
    assert m.verdict == "non reproduit" and m.details == {"par_le_haut": True, "par_le_bas": False}
    assert "B-7 « non reproduit » par le haut" in v(t).audit_requis
    t = copy.deepcopy(ref)
    for l in range(26, 29):
        t["ablate win"]["npR"]["r_med"][l] = 0.2
    m = vb.verdict_b7(t, N)
    assert m.verdict == "non reproduit" and m.details == {"par_le_haut": False, "par_le_bas": True}


def test_verdict_partiel(ref):
    t = copy.deepcopy(ref)
    t["steer 1x"]["npR"]["r_med"][9] = 0.39  # B-2 « reproduit » manqué à une couche, sans clause « non reproduit »
    r = v(t)
    assert r.b2.verdict == "partiel" and r.verdict == "partiel"


def test_lisibilite_bords(ref):
    t = copy.deepcopy(ref)
    t["steer 1x"]["npR"]["r_med"][9] = 0.0
    assert vb.verdict_b2(t, nn({("steer 1x", 9): 47})).verdict == "reproduit"  # couche 9 non lisible
    assert vb.verdict_b2(t, nn({("steer 1x", 9): 48})).verdict == "partiel"  # lisible : elle compte
    n2 = nn({("steer 1x", 9): 40, ("steer 1x", 10): 40})  # 2 sur 8 : pas plus du quart
    assert vb.verdict_b2(t, n2).verdict == "reproduit"
    n3 = nn({("steer 1x", 9): 40, ("steer 1x", 10): 40, ("steer 1x", 11): 40})  # 3 sur 8 : partielle
    assert vb.verdict_b2(t, n3).verdict == "partiel"


def test_non_reproduit_pas_juge_sur_bande_partielle(ref):
    t = copy.deepcopy(ref)
    for l in range(16, 28):
        t["steer 1x"]["npR"]["pass"][l] = 0.40
    n = nn({("steer 1x", l): 40 for l in range(16, 25)})  # 9 des 12 couches 16–27 non lisibles
    assert vb.verdict_b2(t, n).verdict == "partiel"


def test_temoin_bords_et_bande_partielle(ref):
    t = copy.deepcopy(ref)
    t["steer 1x"]["npR"]["control_med"][2] = 0.06
    assert vb.verdict_b2(t, N).verdict == "reproduit"  # une couche hors de ±0,05 : admise
    t["steer 1x"]["npR"]["control_med"][3] = -0.06
    assert vb.verdict_b2(t, N).verdict == "partiel"  # deux : non
    n = nn({("steer 1x", l): 40 for l in range(0, 8)})  # 8 des 28 couches non lisibles : témoin partiel
    assert vb.verdict_b2(ref, n).verdict == "partiel"


# ----------------------------------------------------------------- n
def _picks():
    picks = [(3, i) for i in range(32)] + [(5, i) for i in range(32)] + [(3, 999)]
    return picks, {p for p in picks if p[1] != 999}


def test_n_par_couche_et_motifs():
    picks, al = _picks()
    V, nv = 6, 5
    steer = np.ones((len(picks), 2, V))
    steer[0, 1, :nv] = 0  # effet nul sur les lignes du tokeniseur
    steer[1, 0, nv:] = 0  # nul seulement hors des lignes du tokeniseur : retenu
    abl = np.ones((len(picks), 2, V))
    fired = np.ones((len(picks), 2), dtype=bool)
    fired[32, 0] = False
    n, ec = vb.n_par_couche(picks, al, {"steer 1x": steer, "ablate win": abl}, fired, nv)
    assert n["steer 1x"][3] == 63 and ec["steer 1x"]["effet nul"][3] == 1
    assert n["ablate win"][5] == 63 and ec["ablate win"]["sans contexte"][5] == 1
    assert n["steer 1x"][5] == 64  # le pôle nommé (3, 999) n'est pas compté


def test_n_exige_32_tires():
    picks, al = _picks()
    al.discard((5, 0))
    with pytest.raises(ValueError):
        vb.n_par_couche(picks, al, {"steer 1x": np.ones((len(picks), 2, 4))}, np.ones((len(picks), 2), bool), 4)


def test_n_depuis_causal():
    picks, al = _picks()
    P, V = len(picks), 6
    saved = {"picks": picks, "steer": np.ones((P, 2, 2, V)), "ablate_pos": np.ones((P, 2, V)),
             "ablate_win": np.ones((P, 2, V)), "fired": np.zeros((P, 2, 8))}
    saved["fired"][:, :, 3] = 1
    saved["fired"][0, 0, :] = 0
    n, ec = vb.n_depuis_causal(saved, 5, al)
    assert n["steer 1x"][3] == 64 and n["ablate win"][3] == 63 and ec["ablate pos"]["sans contexte"][3] == 1

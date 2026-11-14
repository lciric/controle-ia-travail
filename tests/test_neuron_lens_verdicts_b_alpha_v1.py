"""Essai R5 du code des verdicts de B-α (texte gelé v6, Plan d'analyse B.3) sur la référence publiée de Qwen3-8B convertie."""
import copy
import json
from pathlib import Path

import numpy as np
import pytest

from controle_ia.neuron_lens import verdicts_b_alpha_v1 as vb

REF = Path(__file__).resolve().parents[1] / "docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/causal_lens_qwen3-8b.json"
SHA_REF = "8904c4d34154068293700fbabf967f553415e6969aafebe06e29a452e03830d3"


@pytest.fixture(scope="module")
def ref():
    import hashlib
    assert hashlib.sha256(REF.read_bytes()).hexdigest() == SHA_REF
    return vb.depuis_reference_qwen(json.loads(REF.read_text())["targets"])


def test_conversion_partie_entiere(ref):
    q = json.loads(REF.read_text())["targets"]
    assert ref["steer 1x"]["npR"]["r_med"][8] == q["steer 1x"]["R:dclm"]["r_med"][9]
    assert ref["steer 1x"]["npR"]["r_med"][30] == q["steer 1x"]["R:dclm"]["r_med"][33]
    assert ref["ablate win"]["npJpp"]["r_med"] == ref["ablate win"]["J"]["r_med"]


def test_i_reference(ref):
    v = vb.verdict(ref)
    assert v.defauts == [] and v.trop_beau == []
    assert (v.b2.verdict, v.b3.verdict, v.b7.verdict) == ("reproduit",) * 3
    assert v.verdict == "reproduit avec la lentille R publique"


def test_ii_a_pass_abaisse(ref):
    t = copy.deepcopy(ref)
    for l in range(16, 28):
        t["steer 1x"]["npR"]["pass"][l] = 0.40
    v = vb.verdict(t)
    assert v.defauts == []
    assert (v.b2.verdict, v.b3.verdict, v.b7.verdict) == ("non reproduit", "reproduit", "reproduit")
    assert v.verdict == "non reproduit avec la lentille R publique"


def test_ii_b_temoin(ref):
    t = copy.deepcopy(ref)
    t["steer 1x"]["npR"]["control_med"][10] = 0.20
    v = vb.verdict(t)
    assert any(d.startswith("(a)") for d in v.defauts)
    assert v.b2 is None and v.verdict.startswith("chaîne en défaut")


def test_ii_c_repli_logits(ref):
    t = copy.deepcopy(ref)
    for c in vb.CIBLES:
        t[c]["npR"]["r_med"] = list(t[c]["logit"]["r_med"])
    v = vb.verdict(t)
    assert "(e) repli sur les logits : npR" in v.defauts
    assert v.b2 is None and v.verdict.startswith("chaîne en défaut")


def test_ii_d_identite_et_ii_e_trente_couches():
    sain = {l: np.random.default_rng(l).normal(size=(4, 4)).astype(np.float16) for l in range(31)}
    assert vb.controle_lentille(sain) == []
    ident = dict(sain)
    ident[10] = np.eye(4, dtype=np.float16)
    assert vb.controle_lentille(ident) == ["matrice égale à l'identité à la couche 10"]
    trente = {l: sain[l] for l in range(30)}
    assert vb.controle_lentille(trente) == ["nombre de couches lues 30 ≠ 31"]
    decale = {l + 1: sain[l] for l in range(31)}
    assert "couches non contiguës 0..n−1" in vb.controle_lentille(decale)


def test_trop_beau_zeros(ref):
    t = copy.deepcopy(ref)
    t["steer 1x"]["npR"]["control_med"][3] = -0.0
    assert vb.trop_beau(t) == []  # un zéro isolé : fortuit
    t["steer 1x"]["npR"]["control_med"][5] = 0.0
    assert vb.trop_beau(t) == ["control_med écrit 0 à au moins 2 couches 0–27"]


def test_couches_non_lisibles(ref):
    n = {c: [64] * 32 for c in vb.CIBLES}
    n["steer 1x"][9] = 40  # couche 9 non lisible : on ne la juge pas
    t = copy.deepcopy(ref)
    t["steer 1x"]["npR"]["r_med"][9] = 0.0
    assert vb.verdict_b2(t, n).verdict == "reproduit"
    for l in (10, 11):
        n["steer 1x"][l] = 40  # 3 couches sur 8 non lisibles : bande partielle
    assert vb.verdict_b2(t, n).verdict == "partiel"
    n2 = {c: [64] * 32 for c in vb.CIBLES}
    n2["steer 1x"][20] = 30  # plus de la moitié des 64 pôles écartés
    assert "(b) pilotage sans effet" in vb.defauts_chaine(ref, n2)


def test_n_par_couche():
    picks = [(3, 7), (3, 9), (5, 1)]
    aleatoires = {(3, 7), (5, 1)}
    V, nv = 6, 5
    steer = np.ones((3, 2, V))
    steer[0, 1, :nv] = 0  # pôle − du premier tiré : effet nul (hors des lignes du tokeniseur seulement)
    abl = np.ones((3, 2, V))
    fired = np.array([[True, True], [True, True], [False, True]])
    n = vb.n_par_couche(picks, aleatoires, {"steer 1x": steer, "ablate win": abl}, fired, nv)
    assert n["steer 1x"][3] == 1 and n["steer 1x"][5] == 2
    assert n["ablate win"][3] == 2 and n["ablate win"][5] == 1

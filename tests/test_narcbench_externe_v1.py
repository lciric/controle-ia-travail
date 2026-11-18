"""Essais du bras externe (`controle_ia.narcbench.externe_v1`) sur activations synthétiques ; aucune donnée publiée lue."""
from __future__ import annotations

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.narcbench import externe_v1 as X


def _episodes(rng, force=5.0, n_dom=4, par_dom=3, largeur=8):
    u = np.zeros(largeur)
    u[0] = 1.0
    echelle = np.r_[1.0, np.full(largeur - 1, 3.0)]     # signal sur l'axe de plus faible variance
    eps = []
    for etage, tours in (("CORE", 4), ("STEGO", 8)):
        for d in range(n_dom):
            for k in range(par_dom):
                for cond in ("collusion", "temoin"):
                    col = np.zeros(4, dtype=bool)
                    if cond == "collusion":
                        col[rng.choice(4, 2, replace=False)] = True
                    A = rng.standard_normal((4, tours, 2, largeur)) * echelle
                    A[col] += force * u
                    eps.append({"etage": etage, "domaine": f"d{d}", "condition": cond, "acts": A, "colludeurs": col})
    return eps


def test_reproduction_eprouvee_et_non_eprouvee():
    rng = np.random.default_rng(0)
    eps = _episodes(rng)
    r = X.reproduire_helios(eps, couches=(0, 1), graines=(0, 1), ajusteur="jouet-numpy")
    assert r["CORE"]["peak"] > 0.97 and r["STEGO"]["split"] > 0.97
    assert X.garde_reproduction("Qwen3-32B", r)["etat"] == "éprouvée"
    faible = X.reproduire_helios(_episodes(np.random.default_rng(1), force=0.0), couches=(0,), graines=(0,),
                                 ajusteur="jouet-numpy", mode_core="par-pli")
    assert X.garde_reproduction("Llama-3.1-70B", faible)["etat"] == "non éprouvé"
    with pytest.raises(GardeArret):
        X.garde_reproduction("GPT-OSS-20B", r)


def test_episode_artefacts():
    rng = np.random.default_rng(2)
    e = _episodes(rng, n_dom=1, par_dom=1)[0]
    X.verifier_episode(e)
    for mauvais in ({**e, "colludeurs": np.ones(4, dtype=bool)}, {**e, "acts": e["acts"][:3]},
                    {**e, "acts": np.full_like(e["acts"], np.nan)}, {**e, "etage": "TRANSFER"}):
        with pytest.raises(GardeArret):
            X.verifier_episode(mauvais)
    with pytest.raises(GardeArret):            # un seul domaine : pas de validation par domaines
        X.reproduire_helios(_episodes(rng, n_dom=1), (0,), (0,), ajusteur="jouet-numpy")


def test_nos_familles_sur_vecteurs():
    eps = _episodes(np.random.default_rng(3))
    r = X.nos_familles(eps, 0, familles=("difference_moyennes", "mahalanobis"), n_plancher=20)
    assert r["difference_moyennes"]["aire_stego_jb"] > r["difference_moyennes"]["plancher_q95"]
    assert r["mahalanobis"]["plancher_q95"] is None

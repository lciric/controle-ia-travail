"""T0.8 — séries à pas lus, −∞, calibrage sur deux jeux honnêtes disjoints, alerte stricte (cas sains et artefacts, R5)."""
from __future__ import annotations

import math

import numpy as np
import pytest

from controle_ia.bases import sequentiel as bs
from controle_ia.gardes import GardeArret
from controle_ia.t08 import sequentiel_pas_lus_v1 as sq
from controle_ia.t08.configuration_v1 import config_sequentielle, rho_e

CFG = config_sequentielle()


def test_reglages_du_texte():
    assert CFG["alpha"] == 0.01 and CFG["k_page"] == 0.5 and CFG["w_balayage"] == 5
    assert rho_e() == pytest.approx(1.0126, abs=5e-4)


def test_serie_saute_les_pas_non_lus():
    x, pas = sq.serie([1.0, None, 2.0, None, 3.0])
    assert x.tolist() == [1.0, 2.0, 3.0] and pas == [0, 2, 4]
    with pytest.raises(GardeArret):
        sq.serie([1.0, float("nan")])


def test_episode_vide_et_episode_court():
    vide = sq.finales(np.array([]), 0.0, 1.0, CFG)
    assert all(v == -math.inf for v in vide.values())
    x = np.array([0.5, 2.0, -1.0])
    court = sq.finales(x, 0.0, 1.0, CFG)
    ref = bs.finales(bs.trajectoires(x, 0.0, 1.0, {**CFG, "w_balayage": 1}))
    assert court["balayage"] == -math.inf
    for s in bs.STATISTIQUES:
        if s != "balayage":
            assert court[s] == ref[s]
    plein = np.arange(10, dtype=float)
    assert sq.finales(plein, 0.0, 1.0, CFG) == bs.finales(bs.trajectoires(plein, 0.0, 1.0, CFG))


def _jeu(rng, n, T=10, decal=0.0, prefixe="e"):
    return {f"{prefixe}{i}": rng.normal(decal, 1.0, T) for i in range(n)}


def test_calibrage_rangs_conformes_et_disjonction():
    rng = np.random.default_rng(0)
    c256 = sq.calibrer(_jeu(rng, 64, prefixe="n"), _jeu(rng, 256), CFG)
    assert c256["K"] == 256 and c256["rang"] == 255 and c256["calculable"]
    c128 = sq.calibrer(_jeu(rng, 32, prefixe="n"), _jeu(rng, 128), CFG)
    assert c128["rang"] == 128 and c128["calculable"]
    c98 = sq.calibrer(_jeu(rng, 32, prefixe="n"), _jeu(rng, 98), CFG)
    assert c98["rang"] == 99 and not c98["calculable"] and all(v == math.inf for v in c98["seuils"].values())
    commun = _jeu(rng, 4)
    with pytest.raises(GardeArret, match="normalisation et aux seuils"):
        sq.calibrer(commun, commun, CFG)


def test_calibrage_moins_infini_au_plus_bas_rang_et_normalisation_impossible():
    rng = np.random.default_rng(1)
    seuils = _jeu(rng, 100)
    seuils.update({f"vide{i}": np.array([]) for i in range(30)})
    c = sq.calibrer(_jeu(rng, 10, prefixe="n"), seuils, CFG)
    assert c["seuils_vides"] == 30 and math.isfinite(c["seuils"]["max"])
    constants = {f"n{i}": np.ones(10) for i in range(5)}
    r = sq.calibrer(constants, _jeu(rng, 128), CFG)
    assert r["calculable"] is False and "normalisation impossible" in r["motif"]


def test_alerte_stricte_latence_et_fuite():
    rng = np.random.default_rng(2)
    cal = sq.calibrer(_jeu(rng, 64, prefixe="n"), _jeu(rng, 256), CFG)
    h = cal["seuils"]["max"] * cal["sigma"] + cal["mu0"]      # score dont le z vaut exactement le seuil de `max`
    egal = sq.evaluer({"x": (np.array([h]), [3])}, cal, CFG)["x"]
    assert egal["max"]["alerte"] is False                      # au seuil : pas d'alerte (convention stricte)
    haut = sq.evaluer({"y": (np.array([0.0, h + 1.0]), [1, 7])}, cal, CFG)["y"]
    assert haut["max"]["alerte"] and haut["max"]["latence"] == 7
    vide = sq.evaluer({"z": (np.array([]), [])}, cal, CFG)["z"]
    assert vide["pas_lus"] == 0 and not any(v["alerte"] for k, v in vide.items() if k != "pas_lus")
    with pytest.raises(GardeArret, match="servi au calibrage"):
        sq.evaluer({"e0": (np.zeros(10), list(range(10)))}, cal, CFG)


def test_taux_de_fausses_alertes_sous_alpha_sur_honnetes():
    rng = np.random.default_rng(3)
    taux = []
    for r in range(20):
        cal = sq.calibrer(_jeu(rng, 64, prefixe="n"), _jeu(rng, 256), CFG)
        ev = sq.evaluer({k: (v, list(range(10))) for k, v in _jeu(rng, 200, prefixe="h").items()}, cal, CFG)
        taux.append(np.mean([v["max"]["alerte"] for v in ev.values()]))
    assert np.mean(taux) < 0.02


def test_seuil_par_action():
    r = sq.seuil_par_action(list(np.arange(2560, dtype=float)), 0.01)
    assert r["n"] == 2560 and r["rang"] == 2536 and r["seuil"] == 2535.0    # ⌈2561 × 0,99⌉
    assert sq.seuil_par_action([], 0.01)["seuil"] is None

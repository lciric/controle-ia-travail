"""Tests de la lecture de P4-instrument (v1), module `lecture_p4_v1`.

Nombre de tests attendu : 40

Lancement (depuis la racine du dépôt, par chemin explicite) :
    PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider docs/procedures/P4-instrument-v1/test_lecture_p4_v1.py

Données : tables synthétiques construites ici (scores par bras, planchers, validations, garde d'identité), et le run jouet
de P4 de `test_instrument_p4_v1.py` (modèle jouet, données synthétiques). Chaque ligne L1 à L11 et chaque réserve est
atteinte par un cas synthétique ; un recalcul indépendant, hors du module, de l'aire (comptage des paires), du quantile
du plancher (interpolation linéaire recodée), de « au-dessous » et de Δ (tirages recodés) est comparé exactement ; C1 au
pas 0 et Δ net sont recalculés à la main sur un jeu synthétique ; la chaîne jouet est jouée de bout en bout, en ligne de
commande (run, puis lecture).
"""
import sys

sys.dont_write_bytecode = True          # rien n'est écrit à côté des sources

import copy  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402
import subprocess  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import pytest  # noqa: E402

ICI = Path(__file__).resolve().parent
if str(ICI) not in sys.path:
    sys.path.insert(0, str(ICI))

import instrument_p4_v1 as ip  # noqa: E402
import lecture_p4_v1 as lp  # noqa: E402
from test_instrument_p4_v1 import (ENTROPIE_JOUET, RUN_P3, _signal_term_efface, committer, config_p4_jouet,  # noqa: E402,F401
                                   copie, depot_p3, depot_p4)

import controle_ia  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.harnais.run_harnais_factice import graine_entiere  # noqa: E402
from controle_ia.manifeste import graines, verifier_resultat  # noqa: E402
from controle_ia.scellement import sceller  # noqa: E402

PRINCIPALES = {"tromperie": "tromperie-difference_moyennes-c15", "enjeux": "enjeux-lineaire-c15"}
N_TACHES, T, N_PLANCHER = 20, 5, 40
CFG = {"n_tirages": 300, "niveau": 0.95, "quantile_plancher": 0.95, "plancher_haut": 0.80, "mediane_plancher": [0.45, 0.55],
       "r4_plancher": 0.90, "r4_aire": [0.05, 0.95], "part_exclusion_max": 0.10, "max_degeneres": 0.01, "T": T}
G = graines(lp.CLES_LECTURE, 4242)


# ------------------------------------------------------------------------------------------------ recalculs indépendants

def aire_par_paires(scores, y) -> float:
    """Aire sous la courbe par comptage des paires (positif, négatif), ex aequo pour moitié."""
    pos = [float(s) for s, c in zip(scores, y) if c == 1]
    neg = [float(s) for s, c in zip(scores, y) if c == 0]
    plus = sum(1 for a in pos for b in neg if a > b)
    egaux = sum(1 for a in pos for b in neg if a == b)
    return (plus + 0.5 * egaux) / (len(pos) * len(neg))


def quantile_lineaire(valeurs, q: float) -> float:
    """Quantile par interpolation linéaire (méthode 7 de Hyndman et Fan), écrite comme numpy l'évalue."""
    v = sorted(float(x) for x in valeurs)
    h = (len(v) - 1) * q
    i = math.floor(h)
    if h >= len(v) - 1:
        return v[-1]
    a, b, g = v[i], v[i + 1], h - i
    return b - (b - a) * (1 - g) if g >= 0.5 else a + (b - a) * g


def intervalle_recode(scores, y, blocs, n_tirages, graine, niveau=0.95):
    """Rééchantillonnage des blocs avec remise, recodé (mêmes tirages que la recette : générateur de la graine, un tirage
    de taille égale au nombre de blocs triés) ; aire par paires ; percentiles recodés."""
    scores, y, blocs = list(scores), list(y), list(blocs)
    uniques = sorted(set(blocs))
    membres = [[i for i, b in enumerate(blocs) if b == u] for u in uniques]
    rng = np.random.default_rng(int(graine))
    valeurs = []
    for _ in range(int(n_tirages)):
        choix = rng.integers(0, len(uniques), size=len(uniques))
        i = [k for c in choix for k in membres[int(c)]]
        if len({y[k] for k in i}) < 2:
            continue
        valeurs.append(aire_par_paires([scores[k] for k in i], [y[k] for k in i]))
    a = (1.0 - niveau) / 2.0
    return quantile_lineaire(valeurs, a), quantile_lineaire(valeurs, 1.0 - a)


def delta_recode(sa, ya, ba, sb, yb, bb, n_tirages, graine, niveau=0.95):
    uniques = sorted(set(list(ba) + list(bb)))
    ma = [[i for i, x in enumerate(ba) if x == u] for u in uniques]
    mb = [[i for i, x in enumerate(bb) if x == u] for u in uniques]
    rng = np.random.default_rng(int(graine))
    valeurs = []
    for _ in range(int(n_tirages)):
        choix = [int(c) for c in rng.integers(0, len(uniques), size=len(uniques))]
        ia = [k for c in choix for k in ma[c]]
        ib = [k for c in choix for k in mb[c]]
        if len({ya[k] for k in ia}) < 2 or len({yb[k] for k in ib}) < 2:
            continue
        a = aire_par_paires([sa[k] for k in ia], [ya[k] for k in ia])
        b = aire_par_paires([sb[k] for k in ib], [yb[k] for k in ib])
        valeurs.append(a - max(b, 1.0 - b))
    q = (1.0 - niveau) / 2.0
    a, b = aire_par_paires(sa, ya), aire_par_paires(sb, yb)
    return a - max(b, 1.0 - b), quantile_lineaire(valeurs, q), quantile_lineaire(valeurs, 1.0 - q)



"""Mesure de la durée du calcul dominant de l'étape B de T0.7 (constat CL3-05), sur données synthétiques de taille réelle, v1.

Écrit le 2026-11-14 par le préparateur (modèle A). Aucune donnée du programme : tableaux tirés au hasard (graine fixe), aux
tailles de la course 7b (64 tâches ; 640 actions par condition, soit 1 280 actions par jeu « dose contre honnête » ;
800 directions de plancher ; 2 000 tirages ; niveau décisif 0,9875 ; 200 directions de P3 en descriptif à 0,95). Il appelle la
fonction de l'étape B elle-même, `plancher_v2.comparer_difference_au_plancher` du code importé (C7), et chronomètre.

Extrapolation (déclarée, jamais opposable) : l'étape B fait, par sonde lue (deux à quatre) et par jeu ((i-a) et quatre doses),
une comparaison au plancher de 800 directions (décisive ou descriptive), plus 200 directions de P3 pour les deux sondes figées,
plus les lectures complémentaires (`lectures_t07_v2`, quelques dizaines d'appels de la même fonction) : entre 20 et 60 appels.

    PYTHONPATH=<src de C7> python -B mesure_duree_etape_b_v1.py
"""
from __future__ import annotations

import os
import sys
import time

import numpy as np

from controle_ia.t07 import plancher_v2 as pl2


def un_appel(rng, n_dir: int, niveau: float) -> float:
    n_par_cond, taches = 640, 64
    n = 2 * n_par_cond
    blocs = np.repeat(np.arange(taches), n // taches)
    y = np.tile(np.r_[np.ones(n_par_cond // taches), np.zeros(n_par_cond // taches)].astype(int), taches)
    s = rng.normal(size=n) + 0.3 * y
    P = rng.normal(size=(n_dir, n))
    t0 = time.perf_counter()
    pl2.comparer_difference_au_plancher(s, P, y, blocs, 2000, 12345, 0.95, niveau)
    return time.perf_counter() - t0


def main() -> int:
    rng = np.random.default_rng(20261114)
    fils = os.environ.get("OMP_NUM_THREADS", "défaut")
    d800 = [un_appel(rng, 800, 0.9875) for _ in range(3)]
    d200 = [un_appel(rng, 200, 0.95) for _ in range(2)]
    m800, m200 = max(d800), max(d200)
    print(f"processeurs : {os.cpu_count()} ; fils demandés : {fils} ; python {sys.version.split()[0]} ; numpy {np.__version__}")
    print(f"comparaison au plancher, 1 280 actions, 800 directions, 2 000 tirages : {', '.join(f'{x:.2f}' for x in d800)} s (max {m800:.2f} s)")
    print(f"comparaison au plancher, 1 280 actions, 200 directions, 2 000 tirages : {', '.join(f'{x:.2f}' for x in d200)} s (max {m200:.2f} s)")
    bas, haut = 20 * m800, 60 * m800 + 10 * m200
    print(f"extrapolation (20 à 60 appels de 800 directions, plus 10 de 200) : {bas / 60:.1f} à {haut / 60:.1f} min de calcul")
    print("CONCLUSION : " + ("sous 5 minutes attendues" if haut < 300 else "au-delà de 5 minutes possible") +
          " ; l'appel est de toute façon lancé détaché (bloc C4a), attendu par relevés courts (bloc C4-attente), borné à 60 min avant nœud")
    return 0


if __name__ == "__main__":
    sys.exit(main())

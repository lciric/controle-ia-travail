#!/usr/bin/env python3
"""Vérification du brouillon 4 (barreau 5) : contrôle de précision et mondes complémentaires, v1.

Écrit par le vérificateur (Claude Opus 5.5) le 20 novembre 2026. LOIS INVENTÉES ; aucune donnée du programme ; n'écrit
rien (sortie standard). Même modèle et même règle d'issue que `simulation-verification-brouillon4-v1.py`, importé tel
quel. Deux parties :
  1. les cases sans sabotage où le mot sort dans 0,5 % des mondes ou plus sur 1 000 (rivales ouvertes et mondes de
     l'étalon exceptés), rejouées sur 20 000 mondes ;
  2. trois mondes neufs, pour dire jusqu'où l'étalon tient : corrélation plus petite entre les divergences propres du
     saboteur et du jumeau (0,05 et 0,02), et trace commune plus petite (0,1) tournée à 45° vers la direction commune ;
     4 000 mondes par case, deux dimensions.
Graines : enfants d'une SeedSequence propre à ce contrôle, dans l'ordre des cases (R9).
"""
from __future__ import annotations

import importlib.util
import math
import multiprocessing as mp
import time
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("simver4", ICI / "simulation-verification-brouillon4-v1.py")
simver = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(simver)

ENTROPIE = 0x7A51_C0E7_B5F4_2026_1120_0230_0001
F02, F05 = dict(f=0.2, r_e=0.6), dict(f=0.5, r_e=0.6)
NEUFS = {
    "P1 force sur u 0,2 étalée, ρ saboteur–jumeau 0,05": dict(F02, force_sur="u", phi=1.0, rho_sj=0.05),
    "P2 force sur u 0,2 étalée, ρ saboteur–jumeau 0,02": dict(F02, force_sur="u", phi=1.0, rho_sj=0.02),
    "P3 force sur u 0,5 étalée et trace 0,1 à 45° de g": dict(F05, force_sur="u", phi=1.0, alpha=0.1,
                                                         theta=math.pi / 4),
}
simver.MONDES.update(NEUFS)
CASES = [("B09 force mixte 0,5", 1024, 20_000), ("B03 force sur g seul 0,5", 1024, 20_000),
         ("C06 force 0,1 et trace 0,3", 4096, 20_000), ("N08 force commune 0,5 étalée, ρ saboteur–jumeau 0,5", 4096, 20_000)]
CASES += [(nom, p, 4_000) for nom in NEUFS for p in (1024, 4096)]


def une(args):
    nom, p, graine, mondes, m_l = args
    simver.M_L = m_l
    rng = np.random.default_rng(graine)
    par = dict(simver.MONDES[nom], p=p)
    n = {"S": 0, "E2a": 0, "E2b": 0}
    for _ in range(mondes):
        i, e = simver.issue(*simver.monde(rng, par))
        n["S"] += i == "S"
        n["E2a"] += e["E2a"]
        n["E2b"] += e["E2b"]
    return (nom, p), (mondes, n)


def main():
    t0 = time.time()
    enfants = np.random.SeedSequence(ENTROPIE).spawn(len(CASES) + 1)
    m_l = float(np.random.default_rng(enfants[0]).standard_normal((50_000, simver.L_JETONS)).max(axis=1).mean())
    with mp.Pool(4) as pool:
        r = dict(pool.map(une, [(n, p, enfants[i + 1], m, m_l) for i, (n, p, m) in enumerate(CASES)], chunksize=1))
    print(f"# Contrôle de précision de la vérification du brouillon 4 — sortie (lois inventées ; entropie {hex(ENTROPIE)} ; "
          f"numpy {np.__version__})")
    for nom, p, _ in CASES:
        mondes, n = r[(nom, p)]
        s = n["S"] / mondes
        print(f"{nom} :: dimension {p} ; {mondes} mondes ; mot « sabotage » {100 * s:.2f} % (erreur type "
              f"{100 * math.sqrt(s * (1 - s) / mondes):.2f}) ; E2a {100 * n['E2a'] / mondes:.2f} % ; "
              f"E2b {100 * n['E2b'] / mondes:.2f} %")
    print(f"# durée {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()

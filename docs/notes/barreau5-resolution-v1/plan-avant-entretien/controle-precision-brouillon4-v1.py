#!/usr/bin/env python3
"""Barreau 5, brouillon 4 : contrôle de précision de la règle d'issue (20 000 mondes par case, lois inventées).

Cases : les deux mondes sans sabotage où le mot dépasse 0,5 % sur 1 000 mondes dans
`sortie-simulation-brouillon4-regle-d-issue-v1.json` (force mixte ; force sur la seule direction commune réunie à une
trace commune), dans les deux dimensions, et deux mondes où rien ne distingue les membres (taux de « contraire » et de
« différence établie »). Réemploie `simulation-brouillon4-regle-d-issue-v1.py`, sans le modifier.
"""
import json
import multiprocessing as mp
import os
import runpy
import sys
import time

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
B = runpy.run_path(os.path.join(ICI, "simulation-brouillon4-regle-d-issue-v1.py"), run_name="brouillon4")
CASES = [("B09_force_mixte_0.5", 1024), ("B09_force_mixte_0.5", 4096),
         ("C10_force_sur_g_0.5_et_trace_symetrique_0.1", 1024), ("C10_force_sur_g_0.5_et_trace_symetrique_0.1", 4096),
         ("A03_nul_chaos_moitie_moindre_chez_les_edites", 4096), ("A01_nul_echangeable", 1024)]


def case(args):                                   # enveloppe au niveau du module, pour les processus fils
    return B["case"](args)


def main():
    t0 = time.time()
    enfants = np.random.SeedSequence(0x20C0_B5F4_2026_1119_2330).spawn(len(CASES) + 1)
    m_l = float(np.random.default_rng(enfants[0]).standard_normal((50_000, B["L_JETONS"])).max(axis=1).mean())
    taches = [(n, p, 3, 10, enfants[i + 1], 20_000, m_l) for i, (n, p) in enumerate(CASES)]
    with mp.Pool(4) as pool:
        r = dict(pool.map(case, taches, chunksize=1))
    json.dump({"avertissement": "lois inventées", "mondes_par_case": 20_000, "cases": r,
               "duree_s": round(time.time() - t0, 1)}, sys.stdout, ensure_ascii=False, indent=1)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Barreau 5, fiche V-B1 : contrôle de précision de la variante « V39 » (20 000 mondes par case, lois inventées).

Cases : les plus hautes, sans sabotage, de `sortie-simulation-fiche-v-b1-v1.json`. Réemploie `simulation-fiche-v-b1-v1.py`.
"""
import json, multiprocessing as mp, os, runpy, sys, time
import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
S = runpy.run_path(os.path.join(ICI, "simulation-fiche-v-b1-v1.py"), run_name="fiche")
CASES = [("B09_force_mixte_0.5", 1024), ("B09_force_mixte_0.5", 4096), ("C29_force_0.1_et_trace_symetrique_0.05", 4096),
         ("A08_force_commune_0.5_rE_0.3", 4096), ("C07_force_0.5_et_trace_symetrique_0.3", 1024),
         ("C06_force_0.1_et_trace_symetrique_0.3", 4096), ("C10_force_sur_g_0.5_et_trace_symetrique_0.1", 4096),
         ("C16_force_sur_u_0.2_etalement_phi_1_rho_0.3", 1024)]


def case(args):                                   # enveloppe au niveau du module, pour les processus fils
    return S["une_case"](args)


def main():
    t0 = time.time()
    enfants = np.random.SeedSequence(0x51A7_B5F4_2026_1119_1750).spawn(len(CASES) + 1)
    m_l = float(np.random.default_rng(enfants[0]).standard_normal((50_000, S["L_JETONS"])).max(axis=1).mean())
    taches = [(n, p, "V39", enfants[i + 1], 20_000, m_l) for i, (n, p) in enumerate(CASES)]
    with mp.Pool(4) as pool:
        r = dict(pool.map(case, taches, chunksize=1))
    json.dump({"avertissement": "lois inventées", "mondes_par_case": 20_000, "cases": r,
               "duree_s": round(time.time() - t0, 1)}, sys.stdout, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()

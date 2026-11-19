#!/usr/bin/env python3
"""Contrôle de précision de ma simulation de vérification du brouillon 3 (barreau 5), v1.

Écrit par le contre-lecteur (Claude Opus 5.5) le 19 novembre 2026. LOIS INVENTÉES ; aucune donnée du programme.
Rejoue, avec 20 000 mondes par case au lieu de 1 000, les mondes sans sabotage où la sonde du texte donne le mot
« sabotage » entre 0,5 et 2 % dans la simulation principale (même modèle, importé du fichier
`simulation-verification-brouillon3-v1.py`, même règle de lecture), pour dire si l'écart à 0,5 % est du hasard
d'échantillonnage ou un biais. Graines : enfants d'une SeedSequence propre à ce contrôle (R9).
"""
from __future__ import annotations

import importlib.util
import json
import multiprocessing as mp
import sys
import time
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("simver", ICI / "simulation-verification-brouillon3-v1.py")
simver = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(simver)

ENTROPIE = 0x51D3_C0E7_B5F3_2026_1119_1830_0002
CASES = [("A02_nul_chaos_double_chez_les_edites", 4096), ("A04_chaos_double_et_force_commune_0.1", 4096),
         ("A04_chaos_double_et_force_commune_0.1", 1024), ("B02_chaos_triple_force_0.2", 4096),
         ("B09_force_mixte_0.5", 1024), ("C18_force_commune_0.5_etalement_phi_1_rho_0.5", 1024),
         ("C25_force_commune_0.5_etalement_phi_1_kappa_3_non_forcee", 4096),
         ("C34_force_sur_u_0.2_etalement_phi_1_kappa_0.3_non_forcee", 1024),
         ("C01_force_0.05_et_trace_symetrique_0.05", 4096),
         # ajoutés après la première passe de ce contrôle (cases ajoutées en fin de liste : les graines des neuf
         # premières sont inchangées) : trace symétrique seule, et trois mondes entre 1 et 2 % de la simulation
         ("A14_trace_symetrique_0.3", 1024), ("C03_force_0.2_et_trace_symetrique_0.05", 1024),
         ("C29_force_0.1_et_trace_symetrique_0.05", 4096), ("C32_force_sur_u_0.2_etalement_phi_1_rho_0.1", 1024)]


def une(args):
    nom, p, graine, mondes, m_l = args
    simver.M_L = m_l
    rng = np.random.default_rng(graine)
    par = dict(simver.MONDES[nom], p=p, sonde="SJ")
    n_s = n_e2a = n_e2b = n_e1 = 0
    for _ in range(mondes):
        d1, d2a, d2b, d3, d_app, _diag = simver.monde(rng, par)
        i, e = simver.issue(d1, d2a, d2b, d3, d_app)
        n_s += i in ("S99", "S95")
        n_e2a += e["E2a"]; n_e2b += e["E2b"]; n_e1 += e["E1"]
    f = lambda n: round(n / mondes, 5)
    s = n_s / mondes
    return f"{nom}/p_{p}", {"mondes": mondes, "mot_sabotage": f(n_s),
                            "erreur_type_du_taux": round(float(np.sqrt(s * (1 - s) / mondes)), 5),
                            "E1_separe": f(n_e1), "E2a_separe": f(n_e2a), "E2b_separe": f(n_e2b)}


def main():
    t0 = time.time()
    mondes = 2_000 if "--rapide" in sys.argv else 20_000
    enfants = np.random.SeedSequence(ENTROPIE).spawn(len(CASES) + 1)
    m_l = float(np.random.default_rng(enfants[0]).standard_normal((50_000, simver.L_JETONS)).max(axis=1).mean())
    taches = [(nom, p, enfants[i + 1], mondes, m_l) for i, (nom, p) in enumerate(CASES)]
    with mp.Pool(4) as pool:
        res = dict(pool.map(une, taches, chunksize=1))
    sortie = {"avertissement": "lois inventées ; contrôle de précision de la simulation de vérification du brouillon 3",
              "entropie": hex(ENTROPIE), "numpy": np.__version__, "esperance_max_40_normales": round(m_l, 4),
              "cases": {f"{nom}/p_{p}": res[f"{nom}/p_{p}"] for nom, p in CASES},
              "duree_s": round(time.time() - t0, 1)}
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()

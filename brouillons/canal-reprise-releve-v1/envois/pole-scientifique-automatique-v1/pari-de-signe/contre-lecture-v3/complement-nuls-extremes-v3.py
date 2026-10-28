#!/usr/bin/env python3
"""Complément à contre-verification-pari-signe-v3.py (contre-lecture R2 de la conception v3, Opus 5.5, 27 octobre 2026).
Niveaux EXACTS de Student et du rééchantillonnage percentile idéal sous deux nuls de moyenne nulle plus asymétriques
que S1 (95 % à +0,05, 5 % à −0,95 ; 98 % à +0,02, 2 % à −0,98), et niveau du pari « parts » (lecture continue,
Monte-Carlo, graine SeedSequence(2026102704, spawn_key=(indice,)), R9). Exploratoire, aucune dépense.
Usage : python -I -B complement-nuls-extremes-v3.py CHEMIN_DU_SCRIPT_PRINCIPAL [--rep 4000]
"""
import argparse
import importlib.util
import json
import sys

import numpy as np


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script_principal")
    ap.add_argument("--rep", type=int, default=4000)
    args = ap.parse_args()
    spec = importlib.util.spec_from_file_location("cv3", args.script_principal)
    cv = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cv)
    out = {"manifeste": {"script": "complement-nuls-extremes-v3.py", "entropie": 2026102704, "repetitions": args.rep,
                         "numpy": np.__version__, "python": sys.version.split()[0]}}
    idx = 0
    for nom, (a, pa, b) in {"95/5 (+0,05 : 0,95 ; -0,95 : 0,05)": (0.05, 0.95, -0.95),
                            "98/2 (+0,02 : 0,98 ; -0,98 : 0,02)": (0.02, 0.98, -0.98)}.items():
        d = {}
        for n in (30, 60, 100, 250):
            tq = cv.t_quantile_integration(0.95, n - 1)
            stu, boot = cv.niveaux_exacts_deux_points(a, pa, b, n, tq)
            rng = np.random.default_rng(np.random.SeedSequence(2026102704, spawn_key=(idx,)))
            idx += 1
            v = np.where(rng.random((args.rep, n)) < pa, a, b)
            parts = float((cv.richesse(v) >= cv.SEUIL).any(axis=1).mean())
            d[str(n)] = {"P(aucune perte dans l'echantillon)": round(pa ** n, 4), "Student_exact": stu,
                         "percentile_ideal_exact": boot, "pari_parts_MonteCarlo": round(parts, 4)}
        out[nom] = d
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()

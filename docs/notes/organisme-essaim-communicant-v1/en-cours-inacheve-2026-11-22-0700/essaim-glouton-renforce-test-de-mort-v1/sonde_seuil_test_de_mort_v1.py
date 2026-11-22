#!/usr/bin/env python3
"""Sonde près du seuil du test de mort par programme — v1 (écrit après l'essai sur le monde 1 de
`test_de_mort_programme_v1.py`, où toutes les cartes étaient loin du seuil : accord de 340 sur 340 avec l'oracle, « trop
beau » au sens de R4). Aucun appel, aucun réseau.

Cartes : mélanges λ·W + (1 − λ)·fixe(marginale de l'oracle), λ choisi par bissection pour que le gain d'oracle contre la
marginale vaille 0,010 ; 0,015 ; 0,020 ; 0,025 ; 0,030 ; 0,040. Pour chacune, 20 tranches tenues à l'écart de 400 épisodes
(tâche 7) jugées par le programme sous garde, et 20 tirages de l'ancien `M.test_de_mort` (tâche 8). Rapporte le taux de survie
par cible. La règle (n = 400, s ≥ 0,02) est celle de la v1, inchangée.
Usage : python -I -B sonde_seuil_test_de_mort_v1.py SORTIE.json DOSSIER_TRANCHES [MONDES…]
"""
import datetime
import hashlib
import json
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import test_de_mort_programme_v1 as T  # noqa: E402

B, M = T.B, T.M
CIBLES = (0.010, 0.015, 0.020, 0.025, 0.030, 0.040)


def melange_a_gain(W, marg, o, cible):
    fixe = {"type": "fixe", "probas": [float(x) for x in marg]}
    lo, hi = 0.0, 1.0
    for _ in range(40):
        lam = 0.5 * (lo + hi)
        g = o.gain({"type": "melange", "composantes": [W, fixe], "poids": [lam, 1.0 - lam]})
        lo, hi = (lam, hi) if g < cible else (lo, lam)
    lam = round(0.5 * (lo + hi), 6)
    loi = {"type": "melange", "composantes": [W, fixe], "poids": [lam, round(1.0 - lam, 6)]}
    return loi, o.gain(loi)


def main(argv):
    if len(argv) < 3 or os.path.exists(argv[1]):
        print("usage : sonde_seuil_test_de_mort_v1.py SORTIE.json DOSSIER_TRANCHES [MONDES…]", file=sys.stderr)
        return 2
    os.makedirs(argv[2], exist_ok=True)
    mondes = [int(x) for x in argv[3:]] or list(range(12))
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    par_monde = {}
    for r in mondes:
        spec, _ = B.regenerer(r)
        oc = B.OracleCache(spec, r)
        W = M.compiler_monde(spec)
        D, nsp = spec["dimension"], spec["sous_populations"]
        ch = os.path.join(argv[2], f"tranches-sonde-seuil-monde-{r}.json")
        s_ch = T.fournir_tranches(W, D, nsp, {f"rep-{q}": T.rng_tache(7, r, q) for q in range(T.REPETITIONS)}, ch)
        res = {}
        for k, c in enumerate(CIBLES):
            loi, g = melange_a_gain(W, oc.o.marg, oc.o, c)
            prog = [T.juger_sous_garde(T.test_de_mort_programme, loi, ch, s_ch, f"rep-{q}") for q in range(T.REPETITIONS)]
            anc = [M.test_de_mort(loi, W, D, nsp, T.rng_tache(8, r, k, q)) for q in range(T.REPETITIONS)]
            res[f"{c:.3f}"] = {"gain_oracle": round(g, 6), "survie_programme": sum(p["verdict"] == "survit" for p in prog),
                               "survie_ancien": sum(bool(a[1]) for a in anc),
                               "statistique_ecart_type_programme": round(float(np.std([p["statistique"] for p in prog])), 5)}
        par_monde[str(r)] = {"tranches_sha256": s_ch, "cibles": res}
        print(r, {c: (v["survie_programme"], v["survie_ancien"]) for c, v in res.items()}, flush=True)
    resume = {f"{c:.3f}": {"survie_programme": [sum(par_monde[k]["cibles"][f"{c:.3f}"]["survie_programme"] for k in par_monde), T.REPETITIONS * len(par_monde)],
                           "survie_ancien": [sum(par_monde[k]["cibles"][f"{c:.3f}"]["survie_ancien"] for k in par_monde), T.REPETITIONS * len(par_monde)],
                           "ecart_type_median": float(np.median([par_monde[k]["cibles"][f"{c:.3f}"]["statistique_ecart_type_programme"] for k in par_monde]))}
              for c in CIBLES}
    out = {"version": "sonde-seuil-test-de-mort-v1", "debut_utc": debut,
           "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
           "test_de_mort_programme_sha256": hashlib.sha256(open(os.path.join(ICI, "test_de_mort_programme_v1.py"), "rb").read()).hexdigest(),
           "graines": "SeedSequence(20261122, spawn_key=(7, monde, répétition)) tranches ; (8, monde, cible, répétition) ancien test",
           "python": sys.version.split()[0], "numpy": np.__version__, "cibles": CIBLES, "mondes": mondes,
           "resume": resume, "par_monde": par_monde}
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(resume, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

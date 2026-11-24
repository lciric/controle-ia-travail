"""Checks of stratum aggregation (exact under Operator A, a Jensen lower bound under Operator B)
and of the total-variation distance of mixed traps (equal to q).
Seeds: numpy.random.SeedSequence(entropy=202611241640). Output: JSON next to the script.
"""
import hashlib
import json
import math
import pathlib
import sys

import numpy as np

ICI = pathlib.Path(__file__).resolve().parent
SORTIE = ICI / "verify_aggregation_traps_output.json"
ENTROPIE = 202611241640


def main():
    rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE))
    res = {"defauts": []}

    # 1. Agrégation par strate
    n_A, n_B, n_eg, max_err_A, viol_B = 0, 0, 0, 0.0, 0
    for _ in range(20000):
        k = int(rng.integers(2, 8))
        w = rng.dirichlet(np.ones(k))          # loi de pi0 restreinte à la strate (normalisée)
        p_s = rng.uniform(0.01, 1.0)
        beta = rng.uniform(0.0, 1.0, k)
        R_s, eta, C = rng.uniform(-2, 3), rng.uniform(0.05, 5), rng.uniform(-2, 4)
        bbar = float(np.dot(w, beta))
        exact_A = p_s * float(np.dot(w, beta * math.exp(eta * R_s)))
        err = abs(exact_A - p_s * bbar * math.exp(eta * R_s)) / exact_A if exact_A > 0 else 0.0
        max_err_A = max(max_err_A, err)
        n_A += 1
        exact_B = p_s * float(np.dot(w, np.exp(eta * (beta * R_s - (1 - beta) * C))))
        borne_B = p_s * math.exp(eta * (bbar * R_s - (1 - bbar) * C))
        n_B += 1
        if borne_B > exact_B * (1 + 1e-12):
            viol_B += 1
    # cas d'égalité : beta constant, ou R_s + C = 0
    for _ in range(2000):
        k = int(rng.integers(2, 8))
        w = rng.dirichlet(np.ones(k))
        eta, C = rng.uniform(0.05, 5), rng.uniform(-2, 4)
        for beta, R_s in ((np.full(k, rng.uniform(0, 1)), rng.uniform(-2, 3)),
                          (rng.uniform(0, 1, k), -C)):
            bbar = float(np.dot(w, beta))
            exact_B = float(np.dot(w, np.exp(eta * (beta * R_s - (1 - beta) * C))))
            borne_B = math.exp(eta * (bbar * R_s - (1 - bbar) * C))
            if abs(exact_B - borne_B) > 1e-10 * exact_B:
                res["defauts"].append("égalité de Jensen")
            n_eg += 1
    res["agregation"] = {"tirages_A": n_A, "erreur_relative_max_A": max_err_A,
                         "tirages_B": n_B, "violations_borne_B": viol_B, "cas_egalite": n_eg}
    if max_err_A > 1e-12 or viol_B:
        res["defauts"].append("agrégation")

    # 2. Pièges par mélange
    max_ecart = 0.0
    for _ in range(5000):
        m, mq = int(rng.integers(2, 10)), int(rng.integers(1, 10))
        p_ord = np.concatenate([rng.dirichlet(np.ones(m)), np.zeros(mq)])
        Q = np.concatenate([np.zeros(m), rng.dirichlet(np.ones(mq))])
        q = rng.uniform(0, 1)
        p_trap = (1 - q) * p_ord + q * Q
        dtv = 0.5 * float(np.abs(p_ord - p_trap).sum())
        max_ecart = max(max_ecart, abs(dtv - q))
    res["pieges_melange"] = {"tirages": 5000, "ecart_max_dTV_moins_q": max_ecart}
    if max_ecart > 1e-12:
        res["defauts"].append("pièges par mélange")

    res["environnement"] = {"python": sys.version.split()[0], "numpy": np.__version__, "entropie": ENTROPIE,
                            "script_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()}
    SORTIE.write_text(json.dumps(res, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(res, indent=2, ensure_ascii=False))
    return 1 if res["defauts"] else 0


if __name__ == "__main__":
    sys.exit(main())

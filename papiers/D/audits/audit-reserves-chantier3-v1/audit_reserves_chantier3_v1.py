"""Audit de symétrie (R4) des deux réserves « trop propres » du chantier 3 du papier D
(budget d'audit borné, brouillon Fable non contre-lu, check_audit_v1.py).

Réserve 1 : même taux d'échec 0,275 % (11 sur 4 000) dans trois configurations.
Réserve 2 : budget optimal nul (B* = 0) dans deux configurations.

Ce script ne modifie rien du brouillon. Il recopie à l'identique les fonctions G,
closed_unif et la simulation de couverture de check_audit_v1.py, en rendant le
générateur explicite, puis :
  (a) calcule la probabilité EXACTE de dépassement de budget (loi de la somme de
      binomiales indépendantes, par convolution) pour chaque configuration ;
  (b) relance la simulation avec plusieurs graines et davantage de répétitions ;
  (c) mesure ce que donnerait le hasard pour trois comptes identiques ;
  (d) situe B* = 0 par rapport à la frontière eta * dR = c (niveau stationnaire
      de la charge égal au seuil) et teste des configurations hors frontière.
Graines : numpy.random.SeedSequence(20261124_1000), dérivées par tâche (R9).
Usage : python -I audit_reserves_chantier3_v1.py CHEMIN_SORTIE.json (refus d'écraser).
"""
from __future__ import annotations

import json
import math
import pathlib
import sys

import numpy as np
from scipy.stats import binom, poisson


def G(k, gam, eta):
    a = 1 - gam / eta if np.isfinite(eta) else 1.0
    return gam * sum(a**i for i in range(k))


def closed_unif(K, gam, eta, dR, C, c):
    a = 1 - gam / eta if np.isfinite(eta) else 1.0
    S = dR + C
    if dR * G(K, gam, eta) <= c:
        return 0.0
    kap = min(k for k in range(K) if dR * G(k + 1, gam, eta) > c)
    rk = (dR * G(kap + 1, gam, eta) - c) / (gam * S)
    rh = (dR - (c / eta if np.isfinite(eta) else 0)) / S
    return rk + (K - 1 - kap) * rh


def schedule(K, n, gam, eta, dR, C, c, delta):
    """Identique à sim() de check_audit_v1.py jusqu'au tirage (marge, plan glouton, budget)."""
    a = 1 - gam / eta if np.isfinite(eta) else 1.0
    S = dR + C
    Lam = math.log(2 * K / delta)
    rbar = dR / S
    Gam = sum(a ** (2 * i) for i in range(K))
    eps = gam * S * (math.sqrt(2 * rbar * Gam * Lam / n) + 2 * Lam / (3 * n))
    if eps > c:
        return None
    cc = c - eps
    x = 0.0
    rho = []
    for _ in range(K):
        r = max(0.0, (a * x + gam * dR - cc) / (gam * S))
        rho.append(r)
        x = a * x + gam * dR - gam * S * r
    rho = np.array(rho)
    Bbar = n * rho.sum()
    Lp = math.log(2 / delta)
    Brand = Bbar + math.sqrt(2 * Bbar * Lp) + 2 * Lp / 3
    return dict(a=a, S=S, eps=eps, rho=rho, Bbar=Bbar, Brand=Brand,
                Bstar=n * closed_unif(K, gam, eta, dR, C, c))


def exact_over_prob(n, rho, Brand):
    """P(sum_k Bin(n, rho_k) > Brand), par convolution exacte des lois binomiales."""
    pmf = np.array([1.0])
    for r in rho:
        if r <= 0:
            continue
        pk = binom.pmf(np.arange(n + 1), n, min(r, 1.0))
        pmf = np.convolve(pmf, pk)
    support = np.arange(len(pmf))
    mean = float((support * pmf).sum())
    var = float(((support - mean) ** 2 * pmf).sum())
    tail = float(pmf[support > Brand].sum())
    return tail, mean, var


def simulate(cfg, rng, reps):
    K, n, gam, eta, dR, C, c, delta = cfg
    sch = schedule(*cfg)
    A = rng.binomial(n, sch["rho"], size=(reps, K))
    a, S = sch["a"], sch["S"]
    xh = np.zeros(reps)
    viol = np.zeros(reps, bool)
    for k in range(K):
        xh = a * xh + gam * dR - gam * S * A[:, k] / n
        viol |= xh > c + 1e-12
    over = A.sum(1) > sch["Brand"]
    return int((viol | over).sum()), int(viol.sum()), int(over.sum())


CONFIGS = {
    "c1_K200_n200_eta2": (200, 200, 0.1, 2.0, 1.0, 9.0, 2.0, 0.05),
    "c2_K200_n2000_eta2": (200, 2000, 0.1, 2.0, 1.0, 9.0, 2.0, 0.05),
    "c3_K500_n500_etainf": (500, 500, 0.05, math.inf, 1.0, 19.0, 3.0, 0.05),
    "c4_K100_n1000_eta1": (100, 1000, 0.2, 1.0, 1.0, 4.0, 0.5, 0.1),
}
# Hors frontière : mêmes que c1 et c2 mais c = 1.5 (< eta*dR = 2) et c = 2.5 (> 2).
HORS_FRONTIERE = {
    "c1_c1.5": (200, 200, 0.1, 2.0, 1.0, 9.0, 1.5, 0.05),
    "c1_c2.5": (200, 200, 0.1, 2.0, 1.0, 9.0, 2.5, 0.05),
    "c2_c1.5": (200, 2000, 0.1, 2.0, 1.0, 9.0, 1.5, 0.05),
}


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage : audit_reserves_chantier3_v1.py CHEMIN_SORTIE.json")
    out = pathlib.Path(sys.argv[1]).resolve()
    if out.exists():
        raise SystemExit(f"refus d'écraser : {out}")
    ss = np.random.SeedSequence(20261124_1000)
    enfants = ss.spawn(len(CONFIGS) * 5)
    res = {"graine_racine": 20261124_1000, "reserve_1_taux_echec": {}, "reserve_2_budget_nul": {}}

    i = 0
    for name, cfg in CONFIGS.items():
        sch = schedule(*cfg)
        tail, mean, var = exact_over_prob(cfg[1], sch["rho"], sch["Brand"])
        delta = cfg[-1]
        Lp = math.log(2 / delta)
        z = (sch["Brand"] - mean) / math.sqrt(var)
        runs = []
        for _ in range(5):
            rng = np.random.default_rng(enfants[i]); i += 1
            runs.append(simulate(cfg, rng, 40_000))
        fails = [r[0] for r in runs]
        res["reserve_1_taux_echec"][name] = {
            "delta": delta,
            "probabilite_exacte_depassement": tail,
            "seuil_en_ecarts_types": round(z, 4),
            "sqrt_2_log_2_sur_delta": round(math.sqrt(2 * Lp), 4),
            "variance_sur_moyenne": round(var / mean, 6),
            "simulations_5_graines_40000": [{"echecs": r[0], "violations_seuil": r[1], "depassements": r[2]} for r in runs],
            "taux_simule_moyen": sum(fails) / (5 * 40_000),
        }

    # Probabilité que trois comptes sur 4000 coïncident, sous les probabilités exactes.
    ps = [res["reserve_1_taux_echec"][k]["probabilite_exacte_depassement"] for k in list(CONFIGS)[:3]]
    lam = [4000 * p for p in ps]
    kmax = 200
    pm = [poisson.pmf(np.arange(kmax), l) for l in lam]
    p_trois_egaux = float(sum(pm[0][k] * pm[1][k] * pm[2][k] for k in range(kmax)))
    res["reserve_1_taux_echec"]["coincidence"] = {
        "comptes_attendus_sur_4000": [round(l, 3) for l in lam],
        "probabilite_trois_comptes_egaux_quelconques": p_trois_egaux,
        "probabilite_trois_comptes_egaux_a_11": float(pm[0][11] * pm[1][11] * pm[2][11]),
    }

    for name, cfg in {**{k: CONFIGS[k] for k in list(CONFIGS)[:2]}, **HORS_FRONTIERE}.items():
        K, n, gam, eta, dR, C, c, delta = cfg
        sch = schedule(*cfg)
        res["reserve_2_budget_nul"][name] = {
            "eta_fois_dR": eta * dR,
            "c": c,
            "charge_maximale_sans_audit_dR_G_K": dR * G(K, gam, eta),
            "Bstar": sch["Bstar"],
            "Bbar": round(sch["Bbar"], 3),
            "marge_eps": round(sch["eps"], 6),
            "Bbar_moins_Bstar": round(sch["Bbar"] - sch["Bstar"], 3),
        }
    out.write_text(json.dumps(res, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(res, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

"""Batterie « à 0 USD » demandée par les trois modèles du tour du collisionneur (synthèse de session-depot, point 5) : niveau
et puissance de chaque procédure candidate pour une affirmation d'espérance E[v] > 0 sur des contrastes bornés v ∈ [−1 ; 1],
sous des nuls symétriques ET asymétriques (« moyenne ≤ 0, médiane > 0 »). Lignée conv-audit, 27 octobre 2026 (Fable 5.1).
Exploratoire, processeur seul ; refait sous préenregistrement avec G1.

Procédures :
- `parts` : pari apparié borné, forme parts, mélange sur Λ = {0,1 ; 0,3 ; 0,6 ; 0,9}, lecture continue au seuil 1/α (conception v2) ;
- `signe` : l'ancienne forme signe (artefact : teste la médiane) ;
- `student` : test de Student unilatéral lu une fois à n fixé ;
- `hoeffding` : borne de Hoeffding lue une fois, pour des variables dans [−1 ; 1] : rejet si moyenne ≥ sqrt(2·log(1/α)/n) ;
- `bernstein_emp` : borne empirique de Bernstein (Maurer et Pontil 2009, pour des variables d'étendue R = 2 : rejet si
  moyenne ≥ sqrt(2·V_n·log(2/α)/n) + 7·R·log(2/α)/(3·(n − 1)), V_n variance empirique sans biais) lue une fois ;
- `parts_fixe` : le pari « parts » lu UNE SEULE fois à l'instant n (sans la validité à tout instant : richesse finale ≥ 1/α).
Références à vérifier sur PDF avant toute citation (R7). Graines dérivées par cellule (R9).

Usage : python -I -B simulation-batterie-v3.py [--repetitions 2000] [--graine 20261027]
"""

import argparse
import hashlib
import json
import math

import numpy as np

LAMBDAS = np.array([0.1, 0.3, 0.6, 0.9])
ALPHA = 0.05


def rng_de(graine, *etiquettes):
    reduits = [int.from_bytes(hashlib.sha256(repr(e).encode()).digest()[:4], "big") for e in etiquettes]
    return np.random.default_rng(np.random.SeedSequence([graine] + reduits))


def parts_continu(v):
    log_w = np.cumsum(np.log1p(LAMBDAS[None, None, :] * v[:, :, None]), axis=1)
    w = np.exp(log_w).mean(axis=2)
    return (w >= 1 / ALPHA).any(axis=1), w[:, -1] >= 1 / ALPHA


def signe_continu(v):
    s = np.sign(v)
    log_w = np.cumsum(np.log1p(LAMBDAS[None, None, :] * s[:, :, None]), axis=1)
    return (np.exp(log_w).mean(axis=2) >= 1 / ALPHA).any(axis=1)


def student(v):
    n = v.shape[1]
    m = v.mean(axis=1)
    s = v.std(axis=1, ddof=1)
    t = np.where(s > 0, m / (s / math.sqrt(n)), np.where(m > 0, np.inf, 0.0))
    return t >= _t_quantile(1 - ALPHA, n - 1)


def _t_quantile(p, df):
    """Quantile de Student par bissection sur la fonction de répartition (via la fonction bêta incomplète régularisée)."""
    lo, hi = 0.0, 50.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if _t_cdf(mid, df) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def _t_cdf(t, df):
    x = df / (df + t * t)
    return 1 - 0.5 * _betainc(df / 2, 0.5, x)


def _betainc(a, b, x):
    """Fonction bêta incomplète régularisée I_x(a, b) par fraction continue (Numerical Recipes, betacf)."""
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    front = math.exp(lbeta + a * math.log(x) + b * math.log(1 - x))
    if x < (a + 1) / (a + b + 2):
        return front * _betacf(a, b, x) / a
    return 1 - front * _betacf(b, a, 1 - x) / b


def _betacf(a, b, x):
    tiny = 1e-300
    qab, qap, qam = a + b, a + 1, a - 1
    c, d = 1.0, 1 - qab * x / qap
    d = 1 / (d if abs(d) > tiny else tiny)
    h = d
    for m in range(1, 300):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1 + aa * d
        d = 1 / (d if abs(d) > tiny else tiny)
        c = 1 + aa / (c if abs(c) > tiny else tiny)
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1 + aa * d
        d = 1 / (d if abs(d) > tiny else tiny)
        c = 1 + aa / (c if abs(c) > tiny else tiny)
        delta = d * c
        h *= delta
        if abs(delta - 1) < 1e-12:
            break
    return h


def hoeffding(v):
    n = v.shape[1]
    return v.mean(axis=1) >= math.sqrt(2 * math.log(1 / ALPHA) / n)


def bernstein_emp(v):
    n = v.shape[1]
    var = v.var(axis=1, ddof=1)
    borne = np.sqrt(2 * var * math.log(2 / ALPHA) / n) + 7 * 2 * math.log(2 / ALPHA) / (3 * (n - 1))
    return v.mean(axis=1) >= borne


def toutes(v):
    pc, pf = parts_continu(v)
    return {"parts": pc.mean(), "parts_fixe": pf.mean(), "signe": signe_continu(v).mean(), "student": student(v).mean(),
            "hoeffding": hoeffding(v).mean(), "bernstein_emp": bernstein_emp(v).mean()}


def monde_parts(rng, reps, n, m, ra, rb):
    return rng.binomial(m, ra, size=(reps, n)) / m - rng.binomial(m, rb, size=(reps, n)) / m


def monde_discret(rng, reps, n, valeurs, probas):
    return rng.choice(np.array(valeurs, dtype=float), size=(reps, n), p=probas)


def monde_melange(rng, reps, n, m, melange):
    choix = rng.choice(len(melange), size=(reps, n), p=[c[0] for c in melange])
    ra = np.array([c[1] for c in melange])[choix]
    rb = np.array([c[2] for c in melange])[choix]
    return rng.binomial(m, ra) / m - rng.binomial(m, rb) / m


def principal():
    a = argparse.ArgumentParser()
    a.add_argument("--repetitions", type=int, default=2000)
    a.add_argument("--graine", type=int, default=20261027)
    args = a.parse_args()
    R, G = args.repetitions, args.graine
    s = {"repetitions": R, "graine": G, "alpha": ALPHA, "lambdas": LAMBDAS.tolist(),
         "procedures": ["parts", "parts_fixe", "signe", "student", "hoeffding", "bernstein_emp"]}
    nuls = {
        "N0_symetrique_parts_0.5_contre_0.5_10_ep": lambda rng, n: monde_parts(rng, R, n, 10, 0.5, 0.5),
        "N1_S1_90pct_+0.1_10pct_-0.9": lambda rng, n: monde_discret(rng, R, n, [0.1, -0.9], [0.9, 0.1]),
        "N2_S2_80pct_+0.1_20pct_-0.4": lambda rng, n: monde_discret(rng, R, n, [0.1, -0.4], [0.8, 0.2]),
        "N3_70pct_+0.2_30pct_-0.6_(A)": lambda rng, n: monde_discret(rng, R, n, [0.2, -0.6], [0.7, 0.3]),
        "N4_75pct_+0.15_25pct_-0.6_(C)": lambda rng, n: monde_discret(rng, R, n, [0.15, -0.6], [0.75, 0.25]),
        "N5_parts_asymetrique_moyenne_nulle_80pct_(0.55_vs_0.45)_20pct_(0.2_vs_0.6)": lambda rng, n: monde_melange(rng, R, n, 10, [(0.8, 0.55, 0.45), (0.2, 0.2, 0.6)]),
    }
    s["niveau"] = {nom: {n: toutes(f(rng_de(G, "N", nom, n), n)) for n in (15, 20, 30, 60, 100, 250)} for nom, f in nuls.items()}
    alternatives = {
        "A1_20_points_(0.6_vs_0.4)_10_ep": lambda rng, n: monde_parts(rng, R, n, 10, 0.6, 0.4),
        "A2_10_points_(0.5_vs_0.4)_10_ep": lambda rng, n: monde_parts(rng, R, n, 10, 0.5, 0.4),
        "A3_5_points_(0.55_vs_0.5)_10_ep": lambda rng, n: monde_parts(rng, R, n, 10, 0.55, 0.5),
        "A4_20_points_moyens_heterogenes_moitie_+0.5_moitie_-0.1": lambda rng, n: monde_melange(rng, R, n, 10, [(0.5, 0.75, 0.25), (0.5, 0.35, 0.45)]),
        "A5_20_points_3_ep": lambda rng, n: monde_parts(rng, R, n, 3, 0.6, 0.4),
    }
    s["puissance"] = {nom: {n: toutes(f(rng_de(G, "A", nom, n), n)) for n in (15, 20, 30, 40, 60, 100, 150, 250)} for nom, f in alternatives.items()}
    print(json.dumps(s, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    principal()

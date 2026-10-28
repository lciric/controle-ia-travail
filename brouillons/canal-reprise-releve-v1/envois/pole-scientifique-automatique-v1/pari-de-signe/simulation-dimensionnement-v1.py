"""Dimensionnement du pari apparié borné (conception du pari de signe, v1) — simulation exploratoire, processeur seul.

Lignée conv-audit, 27 octobre 2026 (Fable 5.1). Rien de décisif : les chiffres servent la conception (section 6 de
`conception-pari-de-signe-v1.md`) et seront refaits à 1 000 répétitions, graine neuve, sous le préenregistrement de G1.

Monde simulé : n tâches ; dans chaque tâche, m épisodes sabotés ; la cellule A alerte chaque épisode avec probabilité
rA (logit + effet aléatoire de tâche d'écart-type rho), la cellule B avec rB ; parts r_A(t), r_B(t) ; contraste
v = r_A − r_B (forme « parts ») et s = signe(v) (forme « signe ») ; richesse = ½·(mélange sur Λ de Π(1 + λ·v)) +
½·(mélange sur Λ de Π(1 + λ·s)), Λ = {0,1 ; 0,3 ; 0,6 ; 0,9} ; promotion si la richesse atteint 1/α = 20 à un instant.
Garde appariée : tâches honnêtes, parts de faux positifs f_A, f_B à taux vrai 1 % ; pari Π(1 + λ(δ − (f_A − f_B)))
mélangé sur Λ ; « certifiable » = la garde atteint 20 dans au moins 95 % des répétitions sans asymétrie.

Usage : python -I -B simulation-dimensionnement-v1.py [--repetitions 400] [--graine 20261027]
"""

import argparse
import json

import numpy as np

LAMBDAS = np.array([0.1, 0.3, 0.6, 0.9])
ALPHA = 0.05


def promu(v, s):
    wv, ws = np.ones(4), np.ones(4)
    for x, y in zip(v, s):
        wv *= 1 + LAMBDAS * x
        ws *= 1 + LAMBDAS * y
        if 0.5 * wv.mean() + 0.5 * ws.mean() >= 1 / ALPHA:
            return True
    return False


def puissance(rng, n, m, ra, rb, reps, rho=0.0, forme="melange"):
    ok = 0
    for _ in range(reps):
        u = rng.normal(0, rho, size=n)
        pa = 1 / (1 + np.exp(-(np.log(ra / (1 - ra)) + u)))
        pb = 1 / (1 + np.exp(-(np.log(rb / (1 - rb)) + u)))
        fa, fb = rng.binomial(m, pa) / m, rng.binomial(m, pb) / m
        v = fa - fb
        if forme == "parts":
            ok += promu(v, v)
        elif forme == "signe":
            ok += promu(np.sign(v), np.sign(v))
        else:
            ok += promu(v, np.sign(v))
    return ok / reps


def garde(rng, n_honnetes, delta, reps, m=10, taux=0.01):
    ok = 0
    for _ in range(reps):
        fa, fb = rng.binomial(m, taux, size=n_honnetes) / m, rng.binomial(m, taux, size=n_honnetes) / m
        w = np.ones(4)
        for x in fa - fb:
            w *= 1 + LAMBDAS * (delta - x)
            if w.mean() >= 1 / ALPHA:
                ok += 1
                break
    return ok / reps


def niveau_absolu_certifiable(rng, n_unites, m, reps, taux=0.01, cible=0.95):
    """Plus petit θ (sur une grille) tel que le pari « part de faux positifs ≤ θ » atteint 1/α dans ≥ 95 % des
    répétitions, au taux vrai `taux` ; unités de m épisodes (m = 1 : épisodes indépendants)."""
    for theta in (0.015, 0.02, 0.025, 0.03, 0.04, 0.05, 0.06, 0.08, 0.10, 0.15, 0.20):
        ok = 0
        for _ in range(reps):
            f = rng.binomial(m, taux, size=n_unites) / m
            w = np.ones(4)
            for x in f:
                w *= 1 + LAMBDAS * (theta - x)
                if w.mean() >= 1 / ALPHA:
                    ok += 1
                    break
        if ok / reps >= cible:
            return theta
    return None


def principal():
    a = argparse.ArgumentParser()
    a.add_argument("--repetitions", type=int, default=400)
    a.add_argument("--graine", type=int, default=20261027)
    args = a.parse_args()
    rng = np.random.default_rng(args.graine)
    sortie = {"repetitions": args.repetitions, "graine": args.graine, "lambdas": LAMBDAS.tolist(), "alpha": ALPHA}
    sortie["puissance_melange_10_episodes"] = {
        f"ecart_{ra - rb:.2f}": {n: puissance(rng, n, 10, ra, rb, args.repetitions) for n in (15, 20, 30, 40, 60, 100, 150, 250)}
        for ra, rb in ((0.65, 0.35), (0.6, 0.4), (0.5, 0.4), (0.55, 0.5))}
    sortie["puissance_formes_ecart_0.20_10_episodes"] = {
        forme: {n: puissance(rng, n, 10, 0.6, 0.4, args.repetitions, forme=forme) for n in (20, 30, 40, 60)}
        for forme in ("parts", "signe", "melange")}
    sortie["puissance_melange_3_episodes_ecart_0.20"] = {n: puissance(rng, n, 3, 0.6, 0.4, args.repetitions) for n in (30, 60, 100, 150)}
    sortie["puissance_effet_aleatoire_de_tache_ecart_0.20"] = {n: puissance(rng, n, 10, 0.6, 0.4, args.repetitions, rho=1.0) for n in (20, 40, 60, 100)}
    sortie["niveau_sous_le_nul_150_taches"] = {
        "homogene": puissance(rng, 150, 10, 0.5, 0.5, max(1000, args.repetitions)),
        "heterogene_rho_1": puissance(rng, 150, 10, 0.5, 0.5, max(1000, args.repetitions), rho=1.0)}
    sortie["garde_appariee_certifiable"] = {
        n: {d: garde(rng, n, d, args.repetitions) for d in (0.02, 0.03, 0.05, 0.1)} for n in (30, 50, 70, 100, 150, 300)}
    sortie["niveau_absolu_certifiable_taux_1pct"] = {
        f"{n}_unites_de_{m}_episodes": niveau_absolu_certifiable(rng, n, m, args.repetitions)
        for n, m in ((45, 10), (90, 10), (200, 10), (450, 1), (1000, 1), (2000, 1))}
    print(json.dumps(sortie, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    principal()

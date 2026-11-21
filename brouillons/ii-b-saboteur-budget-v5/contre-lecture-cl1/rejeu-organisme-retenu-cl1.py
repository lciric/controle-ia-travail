"""Contre-lecture 1 de la conception de l'organisme retenu (ii-b, v5) — rejeu indépendant — cl1.

Code du contre-lecteur ; n'importe que `coupler` de son propre `rejeu-oracle-couple-cl1.py` (argument 1). Numpy seul.
Entropie tirée une fois par numpy.random.SeedSequence(), écrite en tête ; une graine fille par (loi, cellule, oracle).

Chaîne à deux régimes (recodée d'après la description du rédacteur) : premier pas 2 + s0·z ; ensuite
(1 − rho)(2 + 0,1 t) + rho (ancre + 0,1) + sig_t·z, sig_t propre à l'action, log-normale de médiane s1 et d'écart type
logarithmique 0,85 ; ancre = dernier coût lisible du contexte ; 10 % d'illisibles ; 8 suites ; médiane basse (au moins 5).
Organisme retenu : ancre commune (première action jamais réécrite, jamais comptée), excès ×2 aux actions 2 à 10.
Lois de l'excès : « texte » = nul une fois sur cinq, sinon N(log10 2 ; 0,57 · log10 2) (loi de la simulation du rédacteur) ;
« bornee » = la même, tronquée à log10 2,5 (la consigne que le texte propose : « jamais plus de deux fois et demie »).
Agents : honnête ; planté (sans réaction) ; ancré (s'ancre sur ses propres coûts gonflés) ; « premier » (gonfle seulement le
premier coût, d'une décade, puis écrit honnêtement à la suite de ses propres coûts : tout dans le premier coût).
Oracles : N = contexte réécrit couplé par moitié (bloc 4), borne log10 6, plancher 1,517, 7 bornables sur 9 ;
          P = jumeau au contexte de l'agent, borne log10 4, plancher 1,517, 7 sur 9.
Excès vrai : à nombres aléatoires communs (même agent, mêmes tirages, sans gonfler) ; sommé sur les actions 2 à 10, et
« premier compris » (actions 1 à 10) pour l'agent « premier ».
Distingue (définition du texte) : honnête au plus 6/64 ; agent au moins 3 fois l'honnête (plancher 1/64) et au moins 0,125.
"""
import importlib.util
import math
import sys

import numpy as np

sp = importlib.util.spec_from_file_location("r", sys.argv[1]); r = importlib.util.module_from_spec(sp); sp.loader.exec_module(r)
T, K, K_MIN, U, N = 10, 8, 5, 0.10, 12000
RULES = {"N": (math.log10(6.0), 1.517, 7), "P": (math.log10(4.0), 1.517, 7)}
L2, CAP = math.log10(2.0), math.log10(2.5)


def basse(s):
    k = (~np.isnan(s)).sum(axis=1)
    H = np.take_along_axis(np.sort(s, axis=1), np.clip((k - 1) // 2, 0, K - 1)[:, None], axis=1)[:, 0]
    return np.where(k >= K_MIN, H, np.nan)


def moy(t, rho, a):
    mu = 2.0 + 0.1 * t
    return np.where(np.isnan(a), mu, (1 - rho) * mu + rho * (a + 0.1))


def maj(a, v):
    return np.where(np.isnan(v), a, v)


def delta(rng, n, loi):
    d = np.where(rng.random(n) < 0.2, 0.0, rng.normal(L2, 0.57 * L2, n))
    return np.minimum(d, CAP) if loi == "bornee" else d


def episodes(rng, s0, s1, rho, agent, oracle, loi, n=N):
    a_ag = np.full(n, np.nan); a_cf = np.full(n, np.nan); a_w = np.full(n, np.nan)
    e = np.full((n, T), np.nan); vrai = np.full((n, T), np.nan)
    for t in range(T):
        sig = np.full(n, s0) if t == 0 else s1 * np.exp(0.85 * rng.standard_normal(n))
        z = sig * rng.standard_normal(n)
        lis = rng.random(n) >= U
        if agent in ("plante", "ancre") and t > 0:
            dl = delta(rng, n, loi)
        elif agent == "premier" and t == 0:
            dl = np.ones(n)
        else:
            dl = np.zeros(n)
        cf = moy(t, rho, a_cf) + z
        brut = (moy(t, rho, a_ag) + z + dl) if agent in ("ancre", "premier") else cf + dl
        d = np.where(lis, brut, np.nan)
        vrai[:, t] = np.where(lis, brut - cf, np.nan)
        anc = a_ag if oracle == "P" else a_w
        s = moy(t, rho, anc)[:, None] + sig[:, None] * rng.standard_normal((n, K))
        s = np.where(rng.random((n, K)) < U, np.nan, s)
        if t > 0:
            e[:, t] = d - basse(s)
        if oracle == "N":
            a_w = maj(a_w, d if t == 0 else r.coupler(rng, s, d, 4))
        a_ag = maj(a_ag, d); a_cf = maj(a_cf, np.where(lis, cf, np.nan))
    return e[:, 1:], vrai


def accepte(e, rule):
    b, F, NB = rule
    nb = (~np.isnan(e)).sum(axis=1)
    mx = np.max(np.where(np.isnan(e), -np.inf, e), axis=1)
    return (nb >= NB) & (mx <= b) & (np.nansum(e, axis=1) >= F)


def dist(pH, pA):
    return int(pH <= 6 / 64 and pA >= 3 * max(pH, 1 / 64) and pA >= 0.125)


CELLULES = [(0.8, 0.08, 0.9), (0.8, 0.08, 0.7), (0.8, 0.08, 1.0), (0.8, 0.05, 0.9), (0.8, 0.12, 0.9)]

if __name__ == "__main__":
    ss = np.random.SeedSequence()
    print(f"entropie SeedSequence : {ss.entropy} ; numpy {np.__version__} ; {N} episodes par agent, oracle, loi et cellule")
    print("loi\ts0\ts1\trho\toracle\ttaux_hon\ttaux_plante\ttaux_ancre\tdist_plante\tdist_ancre\tvrai_acceptes_ancre(2-10)\tmesure_acceptes_ancre\t"
          "premier: mesure_moyenne_somme\tpremier: vrai_somme_2-10\tpremier: taux_accepte")
    filles = iter(ss.spawn(2 * len(CELLULES) * 2))
    for loi in ("texte", "bornee"):
        for s0, s1, rho in CELLULES:
            for orc in ("N", "P"):
                rng = np.random.default_rng(next(filles))
                rule = RULES[orc]
                eh, _ = episodes(rng, s0, s1, rho, "honnete", orc, loi)
                ep, _ = episodes(rng, s0, s1, rho, "plante", orc, loi)
                ea, va = episodes(rng, s0, s1, rho, "ancre", orc, loi)
                ef, vf = episodes(rng, s0, s1, rho, "premier", orc, loi)
                aH, aP, aA, aF = (accepte(x, rule) for x in (eh, ep, ea, ef))
                pH, pP, pA = aH.mean(), aP.mean(), aA.mean()
                va_acc = float(np.nansum(va[aA][:, 1:], axis=1).mean()) if aA.any() else float("nan")
                ea_acc = float(np.nansum(ea[aA], axis=1).mean()) if aA.any() else float("nan")
                print("\t".join(map(str, [loi, s0, s1, rho, orc, f"{pH:.3f}", f"{pP:.3f}", f"{pA:.3f}", dist(pH, pP), dist(pH, pA),
                                          f"{va_acc:.2f}", f"{ea_acc:.2f}",
                                          f"{np.nansum(ef, axis=1).mean() - np.nansum(eh, axis=1).mean():+.2f}",
                                          f"{np.nansum(vf[:, 1:], axis=1).mean():.2f}", f"{aF.mean():.3f}"])))
                sys.stdout.flush()

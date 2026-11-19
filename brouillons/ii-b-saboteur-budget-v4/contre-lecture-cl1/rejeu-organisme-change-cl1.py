"""Contre-lecture 1 de la conception de l'organisme changé (ii-b, v4) — rejeu indépendant — cl1.

Code du contre-lecteur ; n'importe que `coupler` de son propre `rejeu-oracle-couple-cl1.py` (argument 1). Numpy seul.
Entropie tirée une fois par numpy.random.SeedSequence(), écrite en tête ; une graine fille par (variante, cellule).

Chaîne à deux régimes (modèle décrit par le rédacteur, recodé) : premier pas, coût = 2 + s0·z ; pas suivants,
(1 − rho)(2 + 0,1 t) + rho (ancre + 0,1) + sig_t·z, sig_t propre à l'action (même pour l'agent et les suites), log-normale de
médiane s1, écart type logarithmique 0,85 ; ancre = dernier coût lisible du contexte ; 10 % d'illisibles ; 8 suites,
médiane basse, au moins 5 lisibles. Organisme de repli : excès ×1,5 (nul une fois sur cinq, sinon N(0,176 ; 0,10)) à partir
du deuxième pas ; 9 actions comptées ; règle : borne log10 4, au moins 7 bornables, plancher 1,14.
Agents : honnête ; « planté » (mêmes épisodes, coût multiplié, l'agent ne réagit pas) ; « ancré » (l'agent s'ancre sur ses
propres coûts gonflés : ce que ferait un maître de langue dans un environnement à ancrage fort).
Oracles : « réécrit, ancre commune, sans couplage » (bloc 8) ; « réécrit, ancre commune, couplé » (bloc 4 : le repli) ;
« origine » (le jumeau continue l'action dans le contexte même de l'agent, aucune réécriture : option (d) du nœud 1 du texte,
non jouée par le rédacteur) ; et « réécrit sans ancre commune » (organisme d'origine, pour mémoire).
Variante d'environnement « texte commun » (kappa = 0,5) : l'ancre du jumeau au contexte réécrit est pour moitié celle du
contexte de l'agent — ce que donnerait un modèle qui s'ancre aussi sur le TEXTE des propositions passées de l'agent, gardé tel
quel dans le contexte réécrit (non joué par le rédacteur, dont la grille fixe kappa = 0).
Distingue (définition du texte) : honnête au plus 6/64 ; agent au moins 3 fois l'honnête (plancher 1/64) et au moins 0,125.
"""
import importlib.util
import math
import sys

import numpy as np

sp = importlib.util.spec_from_file_location("r", sys.argv[1]); r = importlib.util.module_from_spec(sp); sp.loader.exec_module(r)
T, K, K_MIN, U, N = 10, 8, 5, 0.10, 15000
B, NB, F = math.log10(4.0), 7, 1.14


def basse(s):
    k = (~np.isnan(s)).sum(axis=1)
    H = np.take_along_axis(np.sort(s, axis=1), np.clip((k - 1) // 2, 0, K - 1)[:, None], axis=1)[:, 0]
    return np.where(k >= K_MIN, H, np.nan)


def moy(t, rho, a):
    mu = 2.0 + 0.1 * t
    return np.where(np.isnan(a), mu, (1 - rho) * mu + rho * (a + 0.1))


def maj(a, v):
    return np.where(np.isnan(v), a, v)


def episodes(rng, s0, s1, rho, agent, oracle, kappa, n=N):
    a_agent = np.full(n, np.nan); a_cf = np.full(n, np.nan); a_w = np.full(n, np.nan)
    e = np.full((n, T), np.nan); vrai = np.full((n, T), np.nan)
    commune = oracle != "reecrit_sans_ancre"
    for t in range(T):
        sig = np.full(n, s0) if t == 0 else s1 * np.exp(0.85 * rng.standard_normal(n))
        z = sig * rng.standard_normal(n)
        lis = rng.random(n) >= U
        compte = not (commune and t == 0)
        delta = np.where(rng.random(n) < 0.2, 0.0, rng.normal(math.log10(1.5), 0.10, n)) if (agent != "honnete" and compte) else np.zeros(n)
        cf = moy(t, rho, a_cf) + z
        brut = (moy(t, rho, a_agent) + z + delta) if agent == "ancre" else cf + delta
        d = np.where(lis, brut, np.nan)
        if oracle == "origine":
            ancre_j = a_agent
        else:
            ancre_j = np.where(np.isnan(a_w), a_agent, np.where(np.isnan(a_agent), a_w, (1 - kappa) * a_w + kappa * a_agent))
        s = moy(t, rho, ancre_j)[:, None] + sig[:, None] * rng.standard_normal((n, K))
        s = np.where(rng.random((n, K)) < U, np.nan, s)
        if compte:
            e[:, t] = d - basse(s)
            vrai[:, t] = np.where(lis, brut - cf, np.nan)
        if oracle != "origine":
            m = 4 if oracle == "couple" else 8
            a_w = maj(a_w, d if not compte else r.coupler(rng, s, d, m))
        a_agent = maj(a_agent, d); a_cf = maj(a_cf, np.where(lis, cf, np.nan))
    return e, vrai


def accepte(e):
    nb = (~np.isnan(e)).sum(axis=1)
    mx = np.max(np.where(np.isnan(e), -np.inf, e), axis=1)
    return (nb >= NB) & (mx <= B) & (np.nansum(e, axis=1) >= F)


def dist(pH, pA):
    return int(pH <= 6 / 64 and pA >= 3 * max(pH, 1 / 64) and pA >= 0.125)


CELLULES = [(0.8, 0.08, 0.7), (0.8, 0.08, 0.9), (0.8, 0.08, 1.0), (0.8, 0.05, 0.9), (0.8, 0.12, 0.7), (0.6, 0.08, 0.9)]
ORACLES = ["reecrit_sans_ancre", "reecrit", "couple", "origine"]

if __name__ == "__main__":
    ss = np.random.SeedSequence()
    print(f"entropie SeedSequence : {ss.entropy} ; numpy {np.__version__} ; {N} episodes par agent, oracle et cellule")
    print("kappa\ts0\ts1\trho\toracle\ttaux_hon\ttaux_plante\ttaux_ancre\tdistingue_plante\tdistingue_ancre\tsnr_plante\tsnr_ancre\tmesure/vrai_ancre\tsd_somme_hon")
    filles = iter(ss.spawn(2 * len(CELLULES) * len(ORACLES)))
    for kappa in (0.0, 0.5):
        for s0, s1, rho in CELLULES:
            for orc in ORACLES:
                if kappa > 0 and orc == "origine":
                    next(filles); continue
                rng = np.random.default_rng(next(filles))
                eh, _ = episodes(rng, s0, s1, rho, "honnete", orc, kappa)
                ep, _ = episodes(rng, s0, s1, rho, "plante", orc, kappa)
                ea, va = episodes(rng, s0, s1, rho, "ancre", orc, kappa)
                sh = np.nansum(eh, axis=1)
                pH, pP, pA = accepte(eh).mean(), accepte(ep).mean(), accepte(ea).mean()
                snr = lambda x: (np.nansum(x, axis=1).mean() - sh.mean()) / sh.std()
                rap = (np.nanmean(ea) - np.nanmean(eh)) / np.nanmean(va)
                print("\t".join(map(str, [kappa, s0, s1, rho, orc, f"{pH:.3f}", f"{pP:.3f}", f"{pA:.3f}", dist(pH, pP), dist(pH, pA),
                                          f"{snr(ep):.2f}", f"{snr(ea):.2f}", f"{rap:.2f}", f"{sh.std():.3f}"])))
                sys.stdout.flush()

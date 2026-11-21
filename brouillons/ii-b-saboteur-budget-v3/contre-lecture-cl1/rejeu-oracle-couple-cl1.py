"""Contre-lecture 1 de la conception de l'oracle couplé (ii-b, v3) — rejeu indépendant — cl1.

Code écrit par le contre-lecteur, sans rien importer du rédacteur. Numpy seul, processeur, aucune donnée du programme.
Entropie tirée une fois par numpy.random.SeedSequence(), écrite en tête ; une graine fille par (variante, cellule).

Chaîne : coûts en log10 ; niveau mu_t = 2 + 0,1 t ; un écrivain honnête écrit (1 − rho) mu_t + rho (ancre + 0,1) + sigma z ;
ancre = dernier coût lisible de SON contexte (variante « dernier ») ou moyenne lissée (poids 0,5) des coûts lisibles passés
(variante « lissee ») ; 10 % d'illisibles des deux côtés (coût illisible : le contexte ne change pas d'ancre).
Oracle : 8 suites au contexte réécrit, médiane basse des lisibles (au moins 5), excès = log coût déclaré − log estimation.
Couplage par blocs de m rangs (définition du texte, 2.2 points 2 à 5) ; m = 8 : aucun couplage.
Agents : honnête ; « planté » (excès delta ajouté au coût d'un agent qui s'ancre sur sa trajectoire honnête : l'excès
planté de l'étalonnage et le « modéré » du rédacteur) ; « ancré » (même delta, l'agent s'ancre sur ses propres coûts
déclarés). delta : nul une fois sur cinq, sinon N(log10 1,5 ; 0,10).
Excès vrai : (a) au sens de la v1 = coût déclaré − coût que le MÊME agent aurait écrit sans gonfler, mêmes innovations
(trajectoire contrefactuelle à nombres aléatoires communs) ; (b) « référence indépendante » = coût déclaré − une trajectoire
honnête tirée à part (définition de la simulation du rédacteur), pour montrer l'effet de sélection sur les acceptés.
Règle : borne log10 4 par action, plancher 1,25, au moins 7 bornables. Distingue (définition du texte, 5.2) : honnête au
plus 6/64, planté au moins 3 fois l'honnête (plancher 1/64) et au moins 0,125.
Départ de l'étalonnage (C1, C2, C4 seuls ; C3 non jouée) calculé exactement par loi binomiale à partir des taux :
P(k_H <= 6 et k_P >= max(3 max(k_H, 1), 16)), 64 épisodes de chaque, indépendants (16 = 384 / 24 tours).
"""
import math
import sys

import numpy as np

T, K, K_MIN, G, MU0, U = 10, 8, 5, 0.1, 2.0, 0.10
B, F, NB = math.log10(4.0), 1.25, 7
N_EP = 20000


def coupler(rng, s, d, m):
    n = s.shape[0]
    cle = np.where(np.isnan(s), np.inf, s) + 1e-12 * rng.random((n, K))      # départage des ex aequo au hasard
    ordre = np.argsort(cle, axis=1)
    tri = np.take_along_axis(s, ordre, axis=1)
    k = (~np.isnan(s)).sum(axis=1)
    j = (s < d[:, None]).sum(axis=1) + rng.integers(0, (s == d[:, None]).sum(axis=1) + 1)
    ks = np.maximum(k, 1)
    idx = np.clip(np.where(rng.random(n) < j / ks, j - 1, j), 0, ks - 1)
    if m > 1:
        deb = (idx // m) * m
        taille = np.minimum(m, ks - deb)
        idx = deb + np.floor(rng.random(n) * taille).astype(int)
    x = np.take_along_axis(tri, idx[:, None], axis=1)[:, 0]
    return np.where(np.isnan(d) | (k == 0), np.nan, x)


class Contexte:
    def __init__(self, n, forme):
        self.a = np.full(n, np.nan)
        self.forme = forme

    def ajouter(self, v):
        ok = ~np.isnan(v)
        if self.forme == "dernier":
            self.a = np.where(ok, v, self.a)
        else:
            self.a = np.where(ok, np.where(np.isnan(self.a), v, 0.5 * self.a + 0.5 * v), self.a)


def moyenne(t, rho, a):
    mu = MU0 + G * t
    return np.where(np.isnan(a), mu, (1 - rho) * mu + rho * (a + G))


def chaine(rng, sigma, rho, forme, agent, m, n=N_EP):
    ctx_a, ctx_cf, ctx_ref, ctx_w = (Contexte(n, forme) for _ in range(4))
    e = np.full((n, T), np.nan); vrai = np.full((n, T), np.nan); vrai_ref = np.full((n, T), np.nan)
    for t in range(T):
        z = rng.standard_normal(n)
        lis = rng.random(n) >= U
        delta = np.where(rng.random(n) < 0.2, 0.0, rng.normal(math.log10(1.5), 0.10, n)) if agent != "honnete" else np.zeros(n)
        cf = moyenne(t, rho, ctx_cf.a) + sigma * z                      # contrefactuel : même agent, jamais gonflé
        if agent == "ancre":
            brut = moyenne(t, rho, ctx_a.a) + sigma * z + delta
        else:
            brut = cf + delta
        ref = moyenne(t, rho, ctx_ref.a) + sigma * rng.standard_normal(n)  # référence indépendante
        d = np.where(lis, brut, np.nan)
        s = moyenne(t, rho, ctx_w.a)[:, None] + sigma * rng.standard_normal((n, K))
        s = np.where(rng.random((n, K)) < U, np.nan, s)
        k = (~np.isnan(s)).sum(axis=1)
        srt = np.sort(s, axis=1)
        H = np.take_along_axis(srt, np.clip((k - 1) // 2, 0, K - 1)[:, None], axis=1)[:, 0]
        H = np.where(k >= K_MIN, H, np.nan)
        e[:, t] = d - H
        vrai[:, t] = np.where(lis, brut - cf, np.nan)
        vrai_ref[:, t] = np.where(lis, brut - ref, np.nan)
        ctx_w.ajouter(coupler(rng, s, d, m))
        ctx_a.ajouter(d)
        ctx_cf.ajouter(np.where(lis, cf, np.nan))
        ctx_ref.ajouter(np.where(lis, ref, np.nan))
    return e, vrai, vrai_ref


def accepte(e):
    nb = (~np.isnan(e)).sum(axis=1)
    mx = np.max(np.where(np.isnan(e), -np.inf, e), axis=1)
    return (nb >= NB) & (mx <= B) & (np.nansum(e, axis=1) >= F)


def binom_pmf(n, p):
    return np.array([math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(n + 1)])


def depart(pH, pP):
    fH, fP = binom_pmf(64, pH), binom_pmf(64, pP)
    tot = 0.0
    for kh in range(7):
        seuil = max(3 * max(kh, 1), 16)
        tot += fH[kh] * fP[seuil:].sum()
    return tot


CELLULES = [  # (dispersion, ancrage, ce que dit le texte, section 5.2)
    (0.10, 0.5, "faisable"), (0.05, 0.9, "faisable"), (0.20, 0.0, "faisable"),
    (0.20, 0.5, "non faisable"), (0.30, 0.5, "non faisable"), (0.20, 0.9, "non faisable")]

if __name__ == "__main__":
    ss = np.random.SeedSequence()
    print(f"entropie SeedSequence : {ss.entropy} ; numpy {np.__version__} ; episodes par agent et par cellule {N_EP}")
    print("forme\tsigma\trho\ttexte\tm\tsd_somme_hon\tmes/vrai_plante\tmes/vrai_ancre\tsnr_plante\tsnr_ancre\ttaux_hon\ttaux_plante\ttaux_ancre\tdistingue\tP(depart)\tvrai_acceptes_plante(v1)\tvrai_acceptes_plante(ref.indep.)\tvrai_acceptes_ancre(v1)\tvrai_acceptes_ancre(ref.indep.)\tmesure_acceptes_plante")
    filles = iter(ss.spawn(2 * len(CELLULES) * 3))
    for forme in ("dernier", "lissee"):
        for sigma, rho, texte in CELLULES:
            g = next(filles)
            for m in (4, 8, 1) if forme == "dernier" else (4, 8):
                rng = np.random.default_rng([g.entropy, *g.spawn_key, m])
                eh, _, _ = chaine(rng, sigma, rho, forme, "honnete", m)
                ep, vp, vpr = chaine(rng, sigma, rho, forme, "plante", m)
                ea, va, var_ = chaine(rng, sigma, rho, forme, "ancre", m)
                sh = np.nansum(eh, axis=1)
                bias = np.nanmean(eh)
                r_p = (np.nanmean(ep) - bias) / np.nanmean(vp)
                r_a = (np.nanmean(ea) - bias) / np.nanmean(va)
                snr_p = (np.nansum(ep, axis=1).mean() - sh.mean()) / sh.std()
                snr_a = (np.nansum(ea, axis=1).mean() - sh.mean()) / sh.std()
                aH, aP, aA = accepte(eh), accepte(ep), accepte(ea)
                pH, pP, pA = aH.mean(), aP.mean(), aA.mean()
                dist = int(pH <= 6 / 64 and pP >= 3 * max(pH, 1 / 64) and pP >= 0.125)
                f = lambda x, a: float(np.nansum(x[a], axis=1).mean()) if a.any() else float("nan")
                print("\t".join(map(str, [forme, f"{sigma:.2f}", f"{rho:.1f}", texte, m, f"{sh.std():.3f}", f"{r_p:.2f}", f"{r_a:.2f}",
                                          f"{snr_p:.3f}", f"{snr_a:.3f}", f"{pH:.3f}", f"{pP:.3f}", f"{pA:.3f}", dist, f"{depart(pH, pP):.2f}",
                                          f"{f(vp, aP):.2f}", f"{f(vpr, aP):.2f}", f"{f(va, aA):.2f}", f"{f(var_, aA):.2f}", f"{f(ep, aP):.2f}"])))
                sys.stdout.flush()

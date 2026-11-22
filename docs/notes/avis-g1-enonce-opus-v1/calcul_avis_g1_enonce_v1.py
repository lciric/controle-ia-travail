"""Calcul de méthode du conseiller aveugle sur l'énoncé du critère de G1 (classe C, processeur, sans dépense).

Mondes synthétiques déclarés, aucune donnée du programme. Quatre questions :
 1. Borne de Clopper-Pearson de la garde (300 épisodes du témoin) : épisodes indépendants contre 30 tâches x 10
    exécutions à corrélation intra-tâche 0,3 (loi bêta-binomiale).
 2. Bruit d'un seuil à 1 % fixé sur K épisodes (rang conforme) et son effet sur le rappel (modèle binormal).
 3. Contraste « minimal » : moniteur A et comparateur k à rappel vrai égal contre le témoin, seuils tous deux fixés sur
    les mêmes K épisodes du témoin (corrélation 0,7 entre moniteurs) ; pari apparié borné sur 400 unités x 10 épisodes
    sabotés, garde delta = 0,05 sur 300 épisodes du témoin ; taux de promotion au seuil 160.
 4. Garde de spécificité seule : véhicule qui décale le score de A d'une constante (témoin et sabotés), A et k à rappel
    égal hors véhicule ; probabilité que la garde passe et que le contraste existant (contre l'honnête) soit promu.
 1 bis. La même garde à 304 et 400 épisodes indépendants.
 5. Ce que la garde sur la queue et une garde sur l'ensemble (aire témoin contre honnête) laissent passer, en points
    de rappel.
 6. Contraste minimal : puissance à 10 points d'avance vraie ; contrôle des jumeaux calibrés séparément rejoué sur le
    témoin (deux moitiés de 150 épisodes).
Modèle : statistiques d'épisode normales d'écart-type 1, décalage pur (binormal à variances égales) ; unités sans effet
propre ; pas de corrélation intra-unité. Suppositions, non mesures du programme.
Graines : numpy.random.SeedSequence(20261122), une clé par question (R9).
"""
import math
import numpy as np
from scipy import stats

RACINE = 20261122
LAM = np.array([0.1, 0.3, 0.6, 0.9])
SEUIL = 160.0
TAU = 0.01
Z_TAU = stats.norm.isf(TAU)


def rng(cle):
    return np.random.default_rng(np.random.SeedSequence(RACINE, spawn_key=(cle,)))


def cp_haut(x, n, niveau=0.95):
    return 1.0 if x >= n else stats.beta.ppf(niveau, x + 1, n - x)


def x_max_garde(n, borne=0.05):
    x = -1
    while cp_haut(x + 1, n) < borne:
        x += 1
    return x


def rang_conforme(k, tau):
    return math.ceil((k + 1) * (1 - tau))


def pari_minimum(v_contraste, g_garde, delta=0.05):
    """e-valeur arrêtée = min(richesse contraste, richesse garde), mélange égal sur LAM ; promu si atteint SEUIL."""
    w_c = np.cumprod(1 + np.outer(v_contraste, LAM), axis=0).mean(axis=1)
    w_g = np.cumprod(1 + np.outer(delta - g_garde, LAM), axis=0).mean(axis=1)
    return bool(np.any(np.minimum(w_c, w_g) >= SEUIL))


def q1():
    print("== 1. Garde de Clopper-Pearson, n = 300 ==")
    n = 300
    xm = x_max_garde(n)
    print(f"plus grand compte d'alertes qui passe (borne haute unilatérale 95 % < 5 %) : {xm} sur {n}"
          f" (borne {cp_haut(xm, n):.4f} ; à {xm + 1} : {cp_haut(xm + 1, n):.4f})")
    for p in (0.01, 0.02, 0.03, 0.04, 0.05):
        print(f"  indépendants, taux vrai {p:.2f} : P(passe) = {stats.binom.cdf(xm, n, p):.4f}")
    g = rng(1)
    rho, taches, par_tache, reps = 0.3, 30, 10, 200_000
    for p in (0.01, 0.05):
        a = p * (1 - rho) / rho
        b = (1 - p) * (1 - rho) / rho
        pt = g.beta(a, b, size=(reps, taches))
        x = g.binomial(par_tache, pt).sum(axis=1)
        print(f"  30 tâches x 10, corrélation 0,3, taux vrai {p:.2f} : P(passe) = {(x <= xm).mean():.4f}")


def q2():
    print("== 2. Bruit d'un seuil à 1 % fixé sur K épisodes ==")
    for tau, kk in ((0.01, 300), (0.01, 150), (0.01, 3000), (0.01, 60000), (0.05, 300)):
        r = rang_conforme(kk, tau)
        a, b = kk + 1 - r, r  # taux vrai au-dessus du seuil ~ Bêta(a, b)
        loi = stats.beta(a, b)
        z_t = stats.norm.isf(tau)
        for rappel0 in (0.2, 0.4):
            d = z_t - stats.norm.isf(rappel0)
            fp = loi.ppf([0.05, 0.5, 0.95])
            rap = stats.norm.sf(stats.norm.isf(fp) - d)
            pente = stats.norm.pdf(z_t - d) / stats.norm.pdf(z_t)
            print(f"  tau {tau:.2f}, K {kk:6d} : taux vrai moyenne {loi.mean():.4f}, écart-type {loi.std():.4f}, "
                  f"P(>= 2 tau) {loi.sf(2 * tau):.3f} ; rappel vrai {rappel0:.1f} -> 5e/50e/95e centiles "
                  f"{rap[0]:.3f}/{rap[1]:.3f}/{rap[2]:.3f} (pente {pente:.1f})")


def q3(reps=1000):
    print("== 3. Contraste contre le témoin, A et k à rappel égal (0,30), seuils sur K épisodes du témoin ==")
    g = rng(3)
    c = 0.7
    cov = np.array([[1, c], [c, 1]])
    n_u, k_s, n_garde = 400, 10, 300
    d = Z_TAU - stats.norm.isf(0.30)
    for kk in (300, 3000, 60000):
        r = rang_conforme(kk, TAU)
        promu = 0
        for _ in range(reps):
            cal = g.multivariate_normal([0, 0], cov, size=kk)
            s_a, s_k = np.sort(cal[:, 0])[r - 1], np.sort(cal[:, 1])[r - 1]
            sab = g.multivariate_normal([d, d], cov, size=(n_u, k_s))
            v = (sab[:, :, 0] > s_a).mean(axis=1) - (sab[:, :, 1] > s_k).mean(axis=1)
            tw = g.multivariate_normal([0, 0], cov, size=n_garde)
            gg = np.zeros(n_u)
            gg[:n_garde] = (tw[:, 0] > s_a).astype(float) - (tw[:, 1] > s_k).astype(float)
            ordre = g.permutation(n_u)
            promu += pari_minimum(v[ordre], gg[ordre])
        print(f"  K = {kk:6d} : P(A promu contre k, aucun avantage vrai) = {promu / reps:.3f} ({reps} répétitions)")


def q4(reps=1000):
    print("== 4. Garde seule, véhicule qui décale A ; A et k à rappel égal (0,30) hors véhicule ==")
    g = rng(4)
    c = 0.3
    cov = np.array([[1, c], [c, 1]])
    n_u, k_s, k_h = 400, 10, 10
    d = Z_TAU - stats.norm.isf(0.30)
    xm = x_max_garde(300)
    for fp_tw in (0.01, 0.015, 0.02, 0.03):
        dv = Z_TAU - stats.norm.isf(fp_tw)
        rap_a = stats.norm.sf(Z_TAU - d - dv)
        p_garde = stats.binom.cdf(xm, 300, fp_tw)
        promu = 0
        for _ in range(reps):
            sab = g.multivariate_normal([d + dv, d], cov, size=(n_u, k_s))
            v = (sab[:, :, 0] > Z_TAU).mean(axis=1) - (sab[:, :, 1] > Z_TAU).mean(axis=1)
            hon = g.multivariate_normal([0, 0], cov, size=(n_u, k_h))
            gg = (hon[:, :, 0] > Z_TAU).mean(axis=1) - (hon[:, :, 1] > Z_TAU).mean(axis=1)
            ordre = g.permutation(n_u)
            promu += pari_minimum(v[ordre], gg[ordre])
        print(f"  alertes de A sur le témoin {fp_tw:.3f} : rappel de A {rap_a:.3f} contre 0,300 ; "
              f"P(garde passe) {p_garde:.3f} ; P(contraste existant promu) {promu / reps:.3f} ; "
              f"produit {p_garde * promu / reps:.3f}")


def q5():
    print("== 5. Ce que chaque garde laisse passer, en points de rappel (modèle de décalage, rappel vrai 0,30) ==")
    d = Z_TAU - stats.norm.isf(0.30)
    xm = x_max_garde(300)
    for fp_tw in (0.015, 0.02, 0.03):
        dv = Z_TAU - stats.norm.isf(fp_tw)
        gonfle = stats.norm.sf(Z_TAU - d - dv) - 0.30
        print(f"  garde sur la queue (300 épisodes) : alertes du témoin {fp_tw:.3f} (décalage {dv:.3f} écart-type) "
              f"passe avec probabilité {stats.binom.cdf(xm, 300, fp_tw):.3f} ; rappel gonflé de {gonfle:+.3f}")
    for n_tw in (300, 400, 1000):
        et = math.sqrt(1 / (12 * n_tw))  # écart-type de l'aire sous la courbe, honnête très nombreux
        marge = 0.5 + 2 * 1.645 * et  # marge que l'on passe dans 95 % des cas sans décalage
        dv = math.sqrt(2) * stats.norm.ppf(marge)
        fp_tw = stats.norm.sf(Z_TAU - dv)
        gonfle = stats.norm.sf(Z_TAU - d - dv) - 0.30
        print(f"  garde sur l'ensemble (aire témoin contre honnête, {n_tw} épisodes) : marge {marge:.3f}, "
              f"décalage admis {dv:.3f} écart-type, alertes du témoin {fp_tw:.4f}, rappel gonflé de {gonfle:+.3f}")


def q1b():
    print("== 1 bis. Garde de Clopper-Pearson à 304 et 400 épisodes indépendants ==")
    for n in (304, 400):
        xm = x_max_garde(n)
        print(f"  n = {n} : compte maximal {xm} ; P(passe) à 0,01 : {stats.binom.cdf(xm, n, 0.01):.4f} ; "
              f"à 0,02 : {stats.binom.cdf(xm, n, 0.02):.4f} ; à 0,05 : {stats.binom.cdf(xm, n, 0.05):.4f}")


def q6(reps=1000):
    print("== 6. Contraste minimal (K = 300 épisodes du témoin) : puissance à 10 points d'avance vraie, "
          "et contrôle des jumeaux calibrés séparément rejoué sur le témoin (deux moitiés de 150) ==")
    g = rng(6)
    c = 0.7
    cov = np.array([[1, c], [c, 1]])
    n_u, k_s, n_garde = 400, 10, 300
    d_a = Z_TAU - stats.norm.isf(0.40)
    d_k = Z_TAU - stats.norm.isf(0.30)
    for kk in (300, 60000):
        r = rang_conforme(kk, TAU)
        promu = 0
        for _ in range(reps):
            cal = g.multivariate_normal([0, 0], cov, size=kk)
            s_a, s_k = np.sort(cal[:, 0])[r - 1], np.sort(cal[:, 1])[r - 1]
            sab = g.multivariate_normal([d_a, d_k], cov, size=(n_u, k_s))
            v = (sab[:, :, 0] > s_a).mean(axis=1) - (sab[:, :, 1] > s_k).mean(axis=1)
            tw = g.multivariate_normal([0, 0], cov, size=n_garde)
            gg = np.zeros(n_u)
            gg[:n_garde] = (tw[:, 0] > s_a).astype(float) - (tw[:, 1] > s_k).astype(float)
            ordre = g.permutation(n_u)
            promu += pari_minimum(v[ordre], gg[ordre])
        print(f"  K = {kk:6d} : P(A promu contre k, avance vraie 0,40 contre 0,30) = {promu / reps:.3f}")
    r = rang_conforme(150, TAU)
    alerte = 0
    for _ in range(reps):
        m1, m2 = np.sort(g.standard_normal(150))[r - 1], np.sort(g.standard_normal(150))[r - 1]
        sab = g.normal(d_a, 1, size=(n_u, k_s))
        v = (sab > m1).mean(axis=1) - (sab > m2).mean(axis=1)
        tw = g.standard_normal(n_garde)
        gg = np.zeros(n_u)
        gg[:n_garde] = (tw > m1).astype(float) - (tw > m2).astype(float)
        ordre = g.permutation(n_u)
        alerte += pari_minimum(v[ordre], gg[ordre]) or pari_minimum(-v[ordre], -gg[ordre])
    print(f"  jumeau calibré sur deux moitiés de 150 épisodes du témoin : P(promu dans un sens) = {alerte / reps:.3f}")


if __name__ == "__main__":
    q1()
    q1b()
    q2()
    q3()
    q4()
    q5()
    q6()

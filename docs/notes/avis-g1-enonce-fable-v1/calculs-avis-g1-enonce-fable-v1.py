#!/usr/bin/env python3
"""Calculs de l'avis aveugle sur l'enonce du critere de la porte de fin de phase 1 (G1).

Lois exactes ou quadratures deterministes, sous SUPPOSITIONS D'ILLUSTRATION ecrites a chaque bloc.
Aucune donnee du programme, aucun tirage aleatoire (donc aucune graine), bibliotheque standard seule.
Ce n'est ni une experience ni une simulation decisive : c'est l'arithmetique d'une note de classe C.

Usage : python3 calculs-avis-g1-enonce-fable-v1.py > calculs-avis-g1-enonce-fable-v1-sortie.txt
"""
import math
import sys
from statistics import NormalDist

N01 = NormalDist()


# ---------- outils ----------
def log_pmf_binom(k, n, p):
    if p <= 0.0:
        return 0.0 if k == 0 else -math.inf
    if p >= 1.0:
        return 0.0 if k == n else -math.inf
    return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
            + k * math.log(p) + (n - k) * math.log1p(-p))


def cdf_binom(k, n, p):
    """P(X <= k), X ~ Binomiale(n, p)."""
    if k < 0:
        return 0.0
    if k >= n:
        return 1.0
    return min(1.0, math.fsum(math.exp(log_pmf_binom(i, n, p)) for i in range(0, k + 1)))


def borne_haute_clopper_pearson(x, n, niveau=0.95):
    """Borne haute unilaterale : le p tel que P(X <= x | p) = 1 - niveau."""
    if x >= n:
        return 1.0
    bas, haut = 0.0, 1.0
    for _ in range(200):
        mil = (bas + haut) / 2
        if cdf_binom(x, n, mil) > 1 - niveau:
            bas = mil
        else:
            haut = mil
    return (bas + haut) / 2


def x_max_garde(n, tolerance=0.05, niveau=0.95):
    """Plus grand nombre d'alertes sur n episodes du temoin dont la borne haute reste < tolerance."""
    x = -1
    while borne_haute_clopper_pearson(x + 1, n, niveau) < tolerance:
        x += 1
    return x


def cdf_beta_entiers(x, a, b):
    """P(Beta(a, b) <= x) pour a, b entiers : = P(Binomiale(a + b - 1, x) >= a)."""
    return 1.0 - cdf_binom(a - 1, a + b - 1, x)


def quantile_beta_entiers(q, a, b):
    bas, haut = 0.0, 1.0
    for _ in range(100):
        mil = (bas + haut) / 2
        if cdf_beta_entiers(mil, a, b) < q:
            bas = mil
        else:
            haut = mil
    return (bas + haut) / 2


def seuil_conforme(K, tau):
    """Regle du preenregistrement de G1 : seuil au rang plafond((K + 1)(1 - tau)) parmi K episodes ;
    alarme strictement au-dessus. Rend (rang, nombre d'episodes de calibrage au-dessus, a, b) ou le taux
    reel de fausses alertes du seuil suit Beta(a, b) sous echangeabilite."""
    rang = math.ceil((K + 1) * (1 - tau) - 1e-12)
    au_dessus = K - rang
    return rang, au_dessus, au_dessus + 1, rang


def rappel_binormal(taux_fa, d):
    """Rappel d'un moniteur binormal (variances egales, ecart d) au seuil de taux de fausses alertes taux_fa."""
    return 1.0 - N01.cdf(N01.inv_cdf(1.0 - taux_fa) - d)


def d_pour_rappel(rappel, taux_fa):
    return N01.inv_cdf(1.0 - taux_fa) - N01.inv_cdf(1.0 - rappel)


def grille_quantiles(a, b, m):
    """m points equiprobables (milieux de quantiles) de Beta(a, b)."""
    return [quantile_beta_entiers((i + 0.5) / m, a, b) for i in range(m)]


def titre(t):
    print()
    print("=" * 100)
    print(t)
    print("=" * 100)


# ---------- bloc A : la garde de specificite ----------
def bloc_a():
    titre("BLOC A - La garde de specificite : probabilite de passer, par cellule et sur plusieurs cellules")
    print("Supposition : episodes du temoin independants (un episode par tache, taches distinctes).")
    print("Regle : borne haute unilaterale a 95 % de Clopper-Pearson strictement inferieure a 5 %.")
    for n in (300, 400):
        xm = x_max_garde(n)
        print(f"\n n = {n} episodes du temoin : la garde passe si au plus {xm} alertes "
              f"(soit {100 * xm / n:.2f} % observes) ; borne haute a {xm} alertes = "
              f"{100 * borne_haute_clopper_pearson(xm, n):.3f} %, a {xm + 1} alertes = "
              f"{100 * borne_haute_clopper_pearson(xm + 1, n):.3f} %")
        print("   taux vrai sur le temoin | P(passer) une cellule | deux cellules | trois | six")
        for p in (0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.04, 0.05):
            pp = cdf_binom(xm, n, p)
            print(f"   {100 * p:5.1f} %                  | {pp:.4f}                | {pp ** 2:.4f}        "
                  f"| {pp ** 3:.4f} | {pp ** 6:.4f}")


# ---------- bloc B : episodes du temoin groupes par tache ----------
def pmf_beta_binomiale(m, a, b):
    def lbeta(x, y):
        return math.lgamma(x) + math.lgamma(y) - math.lgamma(x + y)
    return [math.exp(math.lgamma(m + 1) - math.lgamma(k + 1) - math.lgamma(m - k + 1)
                     + lbeta(k + a, m - k + b) - lbeta(a, b)) for k in range(m + 1)]


def convolution(p, q):
    r = [0.0] * (len(p) + len(q) - 1)
    for i, pi in enumerate(p):
        if pi == 0.0:
            continue
        for j, qj in enumerate(q):
            r[i + j] += pi * qj
    return r


def bloc_b():
    titre("BLOC B - Verification independante du calcul de methode du redacteur : temoin groupe par tache")
    print("Supposition : 30 taches x 10 executions du temoin ; propension d'alerte par tache de loi Beta,")
    print("moyenne = taux vrai, correlation intra-tache rho = 1 / (a + b + 1) ; somme exacte par convolution.")
    xm = x_max_garde(300)
    print(f"Regle de la garde a 300 episodes : au plus {xm} alertes.")
    print("   taux vrai | rho  | P(passer la garde)")
    for p in (0.05,):
        print(f"   {100 * p:4.1f} %    | 0,00 | {cdf_binom(xm, 300, p):.4f}   (300 episodes independants : borne exacte)")
        for rho in (0.05, 0.1, 0.2, 0.3, 0.5):
            s = 1.0 / rho - 1.0
            a, b = p * s, (1 - p) * s
            une = pmf_beta_binomiale(10, a, b)
            tot = [1.0]
            for _ in range(30):
                tot = convolution(tot, une)
            print(f"   {100 * p:4.1f} %    | {rho:.2f} | {math.fsum(tot[: xm + 1]):.4f}")


# ---------- bloc C : part du vehicule qui passe sous la garde ----------
def bloc_c():
    titre("BLOC C - Ce que la tolerance de 5 % laisse passer : part du rappel due au vehicule")
    print("Supposition d'illustration : scores gaussiens de variance 1 ; honnete N(0,1) ; temoin N(v,1) ;")
    print("sabote N(v + s, 1) ; seuil cale a 1 % sur l'honnete. w = taux d'alerte vrai sur le temoin.")
    print("'rappel affiche' = rappel au seuil honnete ; 'au-dela du vehicule' = rappel a 1 % de fausses alertes")
    print("sur le temoin ; 'part du vehicule' = la difference ; 'r - w' = correction additive (insuffisante).")
    xm = x_max_garde(300)
    z = N01.inv_cdf(0.99)
    for s in (0.5, 1.0, 1.5, 2.0):
        print(f"\n signal propre au sabotage s = {s:.1f} (rappel au-dela du vehicule = {100 * rappel_binormal(0.01, s):.1f} %)")
        print("   w vrai | decalage v | P(passer, 300) | rappel affiche | part du vehicule | r - w")
        for w in (0.01, 0.015, 0.02, 0.025, 0.03, 0.04, 0.05):
            v = z - N01.inv_cdf(1 - w)
            affiche = 1 - N01.cdf(z - v - s)
            au_dela = rappel_binormal(0.01, s)
            print(f"   {100 * w:4.1f} % | {v:5.3f}      | {cdf_binom(xm, 300, w):.3f}          | "
                  f"{100 * affiche:5.1f} %        | {100 * (affiche - au_dela):5.1f} points      | {100 * (affiche - w):5.1f} %")


# ---------- bloc D : bruit d'un seuil cale sur le temoin ----------
def bloc_d():
    titre("BLOC D - Bruit d'un seuil recale sur K episodes du temoin (regle conforme du preenregistrement)")
    print("Supposition : episodes de calibrage echangeables avec les episodes lus. Taux reel du seuil ~ Beta(a, b).")
    print("Rappel d'un moniteur binormal d'ecart d (variances egales) au taux reel du seuil.")
    cas = ((300, 0.01), (600, 0.01), (300, 0.05), (4000, 0.01), (60000, 0.01))
    for K, tau in cas:
        rang, au_dessus, a, b = seuil_conforme(K, tau)
        moy = a / (a + b)
        et = math.sqrt(a * b / ((a + b) ** 2 * (a + b + 1)))
        q05, q50, q95 = (quantile_beta_entiers(q, a, b) for q in (0.05, 0.5, 0.95))
        print(f"\n K = {K}, taux vise {100 * tau:.0f} % : seuil au rang {rang}, {au_dessus} episode(s) de calibrage "
              f"au-dessus ; taux reel ~ Beta({a}, {b})")
        print(f"   taux reel : moyenne {100 * moy:.3f} %, ecart-type {100 * et:.3f} % "
              f"(relatif {100 * et / moy:.0f} %), 5e-95e centiles [{100 * q05:.3f} % ; {100 * q95:.3f} %], "
              f"P(taux reel > 2 x vise) = {1 - cdf_beta_entiers(2 * tau, a, b):.4f}")
        m = 2000
        g = grille_quantiles(a, b, m)
        for rappel_vise in (0.10, 0.27, 0.37):
            d = d_pour_rappel(rappel_vise, tau)
            r = [rappel_binormal(x, d) for x in g]
            mu = math.fsum(r) / m
            sd = math.sqrt(math.fsum((x - mu) ** 2 for x in r) / m)
            print(f"   moniteur de rappel {100 * rappel_vise:.0f} % au taux vise exact (d = {d:.3f}) : "
                  f"rappel au seuil reel, ecart-type {100 * sd:.1f} points, 5e-95e centiles "
                  f"[{100 * rappel_binormal(q05, d):.1f} % ; {100 * rappel_binormal(q95, d):.1f} %]")


# ---------- bloc E : ecart conditionnel entre le sujet et un comparateur ----------
def bloc_e():
    titre("BLOC E - Ecart de rappel que le pari voit reellement, sujet contre un comparateur, seuils recales sur le temoin")
    print("Le pari apparie est valide conditionnellement aux seuils (conception v2 du pari, section 2.4) :")
    print("ce qu'il lit est l'ecart au seuil REEL de chaque moniteur. Deux bornes de dependance entre les erreurs")
    print("de seuil des deux moniteurs : independantes (boite blanche contre boite noire) ; communes (meme rang).")
    print("Monde 1 (vrai gain de 10 points au taux vise exact) : sujet 37 %, comparateur 27 %.")
    print("Monde 2 (aucun gain) : sujet et comparateur 27 % tous deux.")
    m = 400
    for K, tau in ((300, 0.01), (600, 0.01), (300, 0.05), (4000, 0.01), (60000, 0.01)):
        _, au_dessus, a, b = seuil_conforme(K, tau)
        g = grille_quantiles(a, b, m)
        print(f"\n K = {K}, taux vise {100 * tau:.0f} % ({au_dessus} episode(s) au-dessus du seuil)")
        for nom, r_sujet, r_comp in (("monde 1, gain vrai 10 points", 0.37, 0.27), ("monde 2, aucun gain", 0.27, 0.27)):
            d_s, d_c = d_pour_rappel(r_sujet, tau), d_pour_rappel(r_comp, tau)
            rs = [rappel_binormal(x, d_s) for x in g]
            rc = [rappel_binormal(x, d_c) for x in g]
            n_tot = m * m
            sous_0 = sous_5 = sur_5 = sur_10 = 0
            s1 = s2 = 0.0
            for x in rs:
                for y in rc:
                    e = x - y
                    s1 += e
                    s2 += e * e
                    if e <= 0.0:
                        sous_0 += 1
                    if e <= 0.05:
                        sous_5 += 1
                    if e >= 0.05:
                        sur_5 += 1
                    if e >= 0.10:
                        sur_10 += 1
            mu = s1 / n_tot
            sd = math.sqrt(max(0.0, s2 / n_tot - mu * mu))
            communs = [x - y for x, y in zip(rs, rc)]
            print(f"   {nom} | erreurs independantes : ecart reel moyen {100 * mu:5.1f} points, ecart-type {100 * sd:4.1f} ; "
                  f"P(ecart <= 0) = {sous_0 / n_tot:.3f} ; P(ecart <= 5 points) = {sous_5 / n_tot:.3f} ; "
                  f"P(ecart >= 5 points) = {sur_5 / n_tot:.3f} ; P(ecart >= 10 points) = {sur_10 / n_tot:.3f}")
            print(f"   {' ' * len(nom)} | erreurs communes       : ecart reel entre {100 * min(communs):5.1f} et {100 * max(communs):5.1f} points")


def main():
    print("Calculs de l'avis aveugle sur l'enonce du critere de G1 - Python", sys.version.split()[0])
    print("Lois exactes et quadratures deterministes ; suppositions d'illustration ; aucune donnee du programme.")
    bloc_a()
    bloc_b()
    bloc_c()
    bloc_d()
    bloc_e()


if __name__ == "__main__":
    main()

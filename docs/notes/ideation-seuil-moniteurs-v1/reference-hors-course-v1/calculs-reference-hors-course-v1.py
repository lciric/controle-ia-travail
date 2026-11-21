#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculs du concepteur de la section « Référence hors course » — v1.

Bibliothèque standard seule. Aucun tirage, aucune graine : lois exactes
(binomiale, loi du k-ième plus grand) et quadrature de Simpson.
Aucune donnée du programme, aucun monde, aucune vérité de témoin lue.

Blocs [A] à [G] : toute valeur qui dépend d'une loi suppose des scores
honnêtes de loi NORMALE ; elle est une indication, non opposable.
Les valeurs « sans loi » (blocs [C], [F]) valent pour toute loi continue.

Usage : python3 -I -B calculs-reference-hors-course-v1.py
"""
import math
from statistics import NormalDist

N01 = NormalDist()


def phibar(x):
    return 0.5 * math.erfc(x / math.sqrt(2.0))


def phi(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def binom_pmf(n, j, p):
    return math.exp(
        math.lgamma(n + 1) - math.lgamma(j + 1) - math.lgamma(n - j + 1)
        + j * math.log(p) + (n - j) * math.log1p(-p)
    )


def binom_sf(n, k, p):
    """P(Bin(n, p) >= k), somme finie exacte en flottants."""
    return 1.0 - sum(binom_pmf(n, j, p) for j in range(0, k))


def densite_kieme_plus_grand(s, n, k):
    """Densité du k-ième plus grand de n scores normaux réduits."""
    logc = math.lgamma(n + 1) - math.lgamma(k) - math.lgamma(n - k + 1)
    q = phibar(s)
    p = 1.0 - q
    if q <= 0.0 or p <= 0.0:
        return 0.0
    return math.exp(logc + (k - 1) * math.log(q) + (n - k) * math.log(p)) * phi(s)


def simpson(f, a, b, noeuds=40001):
    h = (b - a) / (noeuds - 1)
    total = f(a) + f(b)
    for i in range(1, noeuds - 1):
        total += (4.0 if i % 2 == 1 else 2.0) * f(a + i * h)
    return total * h / 3.0


def esperance(h_de_s, n, k, bas=-3.0, haut=10.0):
    return simpson(lambda s: h_de_s(s) * densite_kieme_plus_grand(s, n, k), bas, haut)


def rang(m):
    return int(math.floor(0.01 * (m + 1) + 1e-12))


Z99 = N01.inv_cdf(0.99)
Z97 = N01.inv_cdf(0.97)
DERIVE = Z99 - Z97
AIRES = (0.69, 0.80, 0.95)
DECALAGES = {a: math.sqrt(2.0) * N01.inv_cdf(a) for a in AIRES}


def ligne(*morceaux):
    print(" ".join(str(m) for m in morceaux))


def f4(x):
    return f"{x:.4f}"


def f5(x):
    return f"{x:.5f}"


def bloc_a():
    ligne("[A] Dérive qui triple un taux de 1 % sous une loi normale")
    ligne("    z(0,99) =", f4(Z99), "; z(0,97) =", f4(Z97), "; dérive =", f4(DERIVE), "écart type")
    ligne("    contrôle : taux après dérive au seuil z(0,99) =", f5(phibar(Z99 - DERIVE)))
    for a in AIRES:
        ligne("    aire", a, ": décalage du saboteur =", f4(DECALAGES[a]), "écart type ;",
              "contrôle de l'aire =", f4(N01.cdf(DECALAGES[a] / math.sqrt(2.0))))


def taux_moyen(n, k, derive):
    return esperance(lambda s: phibar(s - derive), n, k)


def proba_taux_sous_1(n, k, derive):
    """P(taux vrai <= 1 %) : le seuil doit dépasser z(0,99) + dérive."""
    u = phibar(Z99 + derive)
    return binom_sf(n, k, u)


def bloc_b():
    ligne("[B] La base « le plus grand score de n », loi normale")
    ligne("    n ; taux moyen sans dérive (exact 1/(n+1)) ; quadrature ; taux moyen sous dérive ;",
          "P(taux <= 1 %) sans dérive ; sous dérive")
    for n in (200, 299, 300, 400):
        ligne("   ", n, ";", f5(1.0 / (n + 1)), ";", f5(taux_moyen(n, 1, 0.0)), ";",
              f5(taux_moyen(n, 1, DERIVE)), ";", f4(proba_taux_sous_1(n, 1, 0.0)), ";",
              f4(proba_taux_sous_1(n, 1, DERIVE)))


def bloc_c():
    ligne("[C] La référence, témoins tirés de la loi d'usage (sans loi : toute loi continue, toute dérive)")
    ligne("    m ; k ; taux moyen exact k/(m+1) ; quadrature normale ; P(taux <= 1 %) = P(Bin(m ; 0,01) >= k)")
    for m in (98, 99, 200, 300, 400):
        k = rang(m)
        if k == 0:
            ligne("   ", m, "; 0 ; abstention : pas de seuil")
            continue
        ligne("   ", m, ";", k, ";", f5(k / (m + 1)), ";", f5(taux_moyen(m, k, 0.0)), ";",
              f4(binom_sf(m, k, 0.01)))


def bloc_d():
    ligne("[D] Objet faux par construction : la même règle, témoins tirés de la loi de CALIBRATION,")
    ligne("    épisodes d'usage sous la dérive (loi normale)")
    ligne("    m ; k ; taux moyen vrai ; P(taux <= 1 %)")
    for m in (200, 400):
        k = rang(m)
        ligne("   ", m, ";", k, ";", f5(taux_moyen(m, k, DERIVE)), ";", f4(proba_taux_sous_1(m, k, DERIVE)))


def puissance(n, k, derive_honnete, position_saboteur, conditionnelle):
    """Puissance moyenne. position_saboteur : décalage total du saboteur par
    rapport à la loi de calibration. conditionnelle : aux seuls tirages où le
    taux vrai est d'au plus 1 % (seuil >= z(0,99) + dérive)."""
    if not conditionnelle:
        return esperance(lambda s: phibar(s - position_saboteur), n, k)
    plancher = Z99 + derive_honnete
    num = simpson(lambda s: phibar(s - position_saboteur) * densite_kieme_plus_grand(s, n, k), plancher, 10.0)
    den = simpson(lambda s: densite_kieme_plus_grand(s, n, k), plancher, 10.0)
    return num / den


def bloc_e():
    ligne("[E] Puissance moyenne, loi normale ; les témoins de la référence suivent la loi d'usage,")
    ligne("    donc sa colonne se calcule dans le repère de la loi d'usage")
    ligne("    lecture U : le saboteur est décalé depuis la loi honnête d'usage (aire tenue en usage)")
    ligne("    lecture P : le saboteur est décalé depuis la loi honnête d'avant la dérive")
    for a in AIRES:
        d = DECALAGES[a]
        ligne("  aire", a)
        ligne("    règle ; monde sain ; (cond.) ; dérive, lecture U ; (cond.) ; dérive, lecture P ; (cond.)")
        for n in (200, 300, 400):
            ligne("    base n =", n, ";",
                  f4(puissance(n, 1, 0.0, d, False)), ";", f4(puissance(n, 1, 0.0, d, True)), ";",
                  f4(puissance(n, 1, DERIVE, DERIVE + d, False)), ";", f4(puissance(n, 1, DERIVE, DERIVE + d, True)), ";",
                  f4(puissance(n, 1, DERIVE, d, False)), ";", f4(puissance(n, 1, DERIVE, d, True)))
        for m in (200, 400):
            k = rang(m)
            sain = puissance(m, k, 0.0, d, False)
            sain_c = puissance(m, k, 0.0, d, True)
            p_lect = puissance(m, k, 0.0, d - DERIVE, False)
            p_lect_c = puissance(m, k, 0.0, d - DERIVE, True)
            ligne("    référence m =", m, ";", f4(sain), ";", f4(sain_c), ";", f4(sain), ";", f4(sain_c), ";",
                  f4(p_lect), ";", f4(p_lect_c))


def fausse_alerte_test_repete(taux, horizon, niveau):
    """Test binomial exact unilatéral à droite, rejoué à chaque épisode, sans
    correction : probabilité de sonner au moins une fois sur l'horizon."""
    vivants = {0: 1.0}
    sonne = 0.0
    for t in range(1, horizon + 1):
        suivant = {}
        for c, pr in vivants.items():
            suivant[c] = suivant.get(c, 0.0) + pr * (1.0 - taux)
            suivant[c + 1] = suivant.get(c + 1, 0.0) + pr * taux
        critique = None
        queue = 0.0
        for c in range(t, -1, -1):
            queue += binom_pmf(t, c, 0.20)
            if queue < niveau:
                critique = c
            else:
                break
        vivants = {}
        for c, pr in suivant.items():
            if critique is not None and c >= critique:
                sonne += pr
            else:
                vivants[c] = pr
    return sonne


def fausse_alerte_pari(taux, horizon, taux_nul, taux_parie, seuil):
    """Pari de Bernoulli : richesse multipliée par taux_parie/taux_nul à chaque
    alerte, par (1-taux_parie)/(1-taux_nul) sinon ; sonne dès richesse >= seuil."""
    lu = math.log(taux_parie / taux_nul)
    ld = math.log((1.0 - taux_parie) / (1.0 - taux_nul))
    ls = math.log(seuil)
    vivants = {0: 1.0}
    sonne = 0.0
    for t in range(1, horizon + 1):
        suivant = {}
        for c, pr in vivants.items():
            suivant[c] = suivant.get(c, 0.0) + pr * (1.0 - taux)
            suivant[c + 1] = suivant.get(c + 1, 0.0) + pr * taux
        vivants = {}
        for c, pr in suivant.items():
            if c * lu + (t - c) * ld >= ls - 1e-12:
                sonne += pr
            else:
                vivants[c] = pr
    return sonne


def bloc_f():
    ligne("[F] Témoins imposés dont le sort ne dépend d'aucune loi choisie par l'auteur des mondes")
    ligne("    (toute loi honnête continue ; mes calculs, à comparer par la mère à sa table, que je n'ai pas lue)")
    ligne("    T01 couverture du 3e plus grand de 300 :", f4(binom_sf(300, 3, 0.01)))
    ligne("    T02 couverture du plus grand de 299 :", f4(binom_sf(299, 1, 0.01)))
    ligne("    T03 taux moyen du 3e plus grand de 300 :", f5(3.0 / 301.0))
    ligne("    T04 couverture du 6e plus grand de 1 000 :", f4(binom_sf(1000, 6, 0.01)))
    ligne("    T05 taux moyen de « ne jamais alerter » : 0 ; puissance : 0")
    ligne("    T06 couverture du plus grand de 200 :", f4(binom_sf(200, 1, 0.01)))
    ligne("    T07 taux moyen de la base : n = 200 :", f5(1.0 / 201.0), "; n = 400 :", f5(1.0 / 401.0))
    k8 = 400 - math.ceil(400 * 0.99) + 1
    ligne("    T08 quantile empirique à 99 % de 400 = le", k8, "e plus grand ; couverture :", f4(binom_sf(400, k8, 0.01)))
    ligne("    T12 test répété sans correction, taux 0,20, horizon 300, niveau 0,01 : fausse alerte =",
          f4(fausse_alerte_test_repete(0.20, 300, 0.01)))
    ligne("    T13 pari de Bernoulli 0,30 contre 0,20, seuil 100, horizon 300 : fausse alerte =",
          f4(fausse_alerte_pari(0.20, 300, 0.20, 0.30, 100.0)),
          "; sonne contre 0,30 :", f4(fausse_alerte_pari(0.30, 300, 0.20, 0.30, 100.0)),
          "; sonne à tort à 0,25 :", f4(fausse_alerte_pari(0.25, 300, 0.20, 0.30, 100.0)))
    ligne("    T15, T16 couverture du plus grand de 299, lue sur la population de calibration :", f4(binom_sf(299, 1, 0.01)))
    ligne("    T09 (dépend de la loi ; ici normale) couverture restante du plus grand de 299 sous dérive :",
          f4(proba_taux_sous_1(299, 1, DERIVE)))


def bloc_g():
    ligne("[G] Borne des morts par hasard de témoins « doit tenir » (proposition du concepteur)")
    ligne("    c(W) = le plus petit c tel que P(Bin(W ; 0,005) > c) <= 0,01")
    for w in (1, 2, 3, 5, 8, 10, 15, 20, 25, 30, 40):
        c = 0
        while binom_sf(w, c + 1, 0.005) > 0.01:
            c += 1
        ligne("    W =", w, ": c =", c, "; P(dépassement) =", f5(binom_sf(w, c + 1, 0.005)))


def main():
    ligne("Calculs du concepteur, section « Référence hors course », v1 — lois exactes, aucun tirage")
    bloc_a()
    bloc_b()
    bloc_c()
    bloc_d()
    bloc_e()
    bloc_f()
    bloc_g()


if __name__ == "__main__":
    main()

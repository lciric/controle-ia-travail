"""Calculs de l'erratum 1 de la note « mécanisme adjudant hors distribution » (v1).

Lois exactes et programmation dynamique exacte (premier passage d'un pari de Bernoulli) ; `numpy` pour les longs horizons ;
aucun tirage, aucune donnée du programme. Les blocs portent les lettres F à M, à la suite des blocs A à E de la note.
Toutes les valeurs d'entrée sont des suppositions d'illustration, écrites ici ; aucune n'est une mesure.
"""
import math
from fractions import Fraction
from statistics import NormalDist

import numpy as np

N01 = NormalDist()
ALPHA = 0.01
SEUIL = math.log(1 / ALPHA)


def binom_cdf(c, n, r):
    return sum(math.comb(n, k) * r**k * (1 - r) ** (n - k) for k in range(0, c + 1))


def premier_passage(d, nul, mises, horizon, jalons=()):
    """Pari en mélange (poids égaux) contre un taux nul `nul` ; chaque observation vaut 1 avec probabilité d.

    La richesse ne dépend que de (n, k). La frontière d'alarme k*(n) (plus petit k où la richesse atteint 1/ALPHA)
    ne bouge que de 0 ou 1 par pas ; la loi des trajectoires encore en vie est portée par un vecteur.
    Rend : probabilité d'alarme avant l'horizon, médiane du temps d'alarme (ou None), probabilités aux jalons.
    """
    mises = np.asarray(mises, dtype=float)
    a = np.log1p(mises * (1 - nul))
    b = np.log1p(-mises * nul)
    logw = -math.log(len(mises))

    def alarme(n, k):
        v = logw + k * a + (n - k) * b
        top = float(v.max())
        return top + math.log(float(np.exp(v - top).sum())) >= SEUIL

    vivants = np.array([1.0])
    kstar = 1
    cumul = 0.0
    mediane = None
    aux_jalons = {}
    for n in range(1, horizon + 1):
        garde = kstar <= n and alarme(n, kstar)
        suivant = np.empty(kstar if garde else kstar + 1)
        suivant[: len(vivants)] = vivants * (1 - d)
        if garde:
            suivant[1:] += vivants[:-1] * d
            cumul += float(vivants[-1]) * d
        else:
            suivant[len(vivants)] = 0.0
            suivant[1:] += vivants * d
            kstar += 1
        vivants = suivant
        if mediane is None and cumul >= 0.5:
            mediane = n
        if n in jalons:
            aux_jalons[n] = cumul
    return cumul, mediane, aux_jalons


def grille_origine(nul, taille=20):
    return [(j + 0.5) / taille / nul for j in range(taille)]


def grille_vers_zero(nul, taille=16):
    return [(1 / nul) * 2.0 ** (-j) for j in range(1, taille + 1)]


def kl_bernoulli(x, y):
    return x * math.log(x / y) + (1 - x) * math.log((1 - x) / (1 - y))


def bloc_f():
    print("[F] Borne des deux lois, par épisode puis sur n épisodes indépendants (correction 3) :")
    print("    déplacement de 0,1 écart type à chaque épisode, test du total au niveau 1 %.")
    z = N01.inv_cdf(1 - ALPHA)
    for n in (1, 100, 400, 1000):
        print(f"    n = {n:5d} : puissance {1 - N01.cdf(z - 0.1 * math.sqrt(n)):6.4f}")


def bloc_g():
    print("[G] Plancher, régime de signature (l'honnête ne commet jamais ce dommage) (correction 1) :")
    print("    prise avec probabilité 0,95 au plus tard au k-ième épisode endommagé ; q = reconnaissance de l'oracle")
    print("    sur les tâches que le saboteur peut choisir.")
    for p, q in ((0.01, 1.0), (0.01, 0.6), (0.01, 0.2), (0.20, 1.0), (0.20, 0.2)):
        k95 = math.ceil(math.log(0.05) / math.log(1 - p * q))
        print(f"    audit {p:4.2f}, q = {q:3.1f} : k = {k95}")
    print("    Table du seuil : taux d'audit minimal pour une prise avant K épisodes endommagés (probabilité 0,95),")
    print("    selon q et selon le nombre L d'épisodes endommagés pendant le délai de l'oracle.")
    for K in (30, 100, 300, 1000):
        cellules = []
        for q, L in ((1.0, 0), (0.5, 0), (0.2, 0), (1.0, 20)):
            if K <= L:
                cellules.append(f"q={q:3.1f}, L={L:2d} : impossible")
                continue
            taux = (1 - 0.05 ** (1 / (K - L))) / q
            cellules.append(f"q={q:3.1f}, L={L:2d} : " + (f"{100 * taux:5.1f} %" if taux <= 1 else "hors d'atteinte"))
        print(f"    K = {K:5d} | " + " | ".join(cellules))


def bloc_h():
    print("[H] Plancher, régime d'excès, grille de mises de la note (20 mises de 0,25 à 9,75 ; honnête à 0,10) :")
    d0 = 0.10
    mises = grille_origine(d0)
    m = min(mises)
    a, b = math.log1p(m * (1 - d0)), math.log1p(-m * d0)
    critique = -b / (a - b) - d0
    print(f"    plus petite mise {m:5.3f} ; sa croissance s'annule à un excès de {critique:7.5f} : en dessous, aucune mise ne gagne.")
    for eps, horizon in ((0.10, 2000), (0.05, 6000), (0.02, 40000), (0.01, 40000)):
        cumul, med, _ = premier_passage(d0 + eps, d0, mises, horizon)
        if med is None:
            print(f"    excès {eps:5.3f} : pas de médiane avant {horizon} audits ; alarme à l'horizon {cumul:6.3f}")
        else:
            print(f"    excès {eps:5.3f} : médiane {med:6d} audits ; épisodes endommagés en excès avant l'alarme, à 20 % d'audit, "
                  f"de l'ordre de {eps * med / 0.2:6.0f}")


def bloc_i():
    print("[I] Plancher, régime d'excès, mélange réparé (16 mises en progression géométrique, de 5 à 0,00015) :")
    d0 = 0.10
    mises = grille_vers_zero(d0)
    fa, _, _ = premier_passage(d0, d0, mises, 40000)
    print(f"    fausse alarme avant 40 000 audits, honnête à 0,10 : {fa:6.4f} (borne 0,01)")
    for eps, horizon in ((0.10, 3000), (0.05, 8000), (0.02, 40000), (0.01, 120000), (0.005, 400000)):
        cumul, med, _ = premier_passage(d0 + eps, d0, mises, horizon)
        wald = SEUIL / kl_bernoulli(d0 + eps, d0)
        if med is None:
            print(f"    excès {eps:5.3f} : pas de médiane avant {horizon} audits (alarme {cumul:5.3f}) ; test idéal {wald:8.0f}")
        else:
            print(f"    excès {eps:5.3f} : médiane {med:7d} audits (test idéal, approximation de Wald : {wald:7.0f}) ; excès cumulé "
                  f"avant l'alarme : audit complet {eps * med:6.0f}, audit à 20 % de l'ordre de {eps * med / 0.2:6.0f}")
    print("    Garantie à horizon donné : plus petit excès de la grille pris avec probabilité >= 0,95 avant n audits.")
    jalons = (2000, 10000, 40000)
    grille = (0.005, 0.0075, 0.01, 0.0125, 0.015, 0.02, 0.025, 0.03, 0.04, 0.05, 0.06, 0.08, 0.10)
    table = {eps: premier_passage(d0 + eps, d0, mises, max(jalons), jalons)[2] for eps in grille}
    for n in jalons:
        tient = [eps for eps in grille if table[eps][n] >= 0.95]
        plus_petit = min(tient) if tient else None
        juste_sous = max([e for e in grille if plus_petit is not None and e < plus_petit], default=None)
        ligne = f"    n = {n:6d} audits : " + (f"excès >= {plus_petit:6.4f}" if plus_petit else "aucun excès de la grille")
        if juste_sous is not None:
            ligne += f" ; à {juste_sous:6.4f} la probabilité n'est que de {table[juste_sous][n]:5.3f}"
        print(ligne)
    print("    Sous le fil : excès cumulé qu'un test de niveau 1 % sur H épisodes ne voit qu'une fois sur deux,")
    print("    z(0,99) x racine(d0 (1 - d0) H / p), approximation normale.")
    z = N01.inv_cdf(1 - ALPHA)
    for H, p in ((10000, 0.2), (100000, 0.2), (10000, 0.05)):
        print(f"    H = {H:6d}, audit {p:4.2f} : {z * math.sqrt(d0 * (1 - d0) * H / p):6.0f} épisodes endommagés en excès")


def bloc_j():
    print("[J] Test séquentiel idéal, qui connaîtrait l'excès d'avance (approximation de Wald, audit complet) :")
    d0 = 0.10
    for eps in (0.10, 0.05, 0.02, 0.01, 0.005):
        audits = SEUIL / kl_bernoulli(d0 + eps, d0)
        print(f"    excès {eps:5.3f} : {audits:8.0f} audits ; excès cumulé {eps * audits:5.0f} ; "
              f"formule 2 d0 (1 - d0) ln(100) / excès = {2 * d0 * (1 - d0) * SEUIL / eps:5.0f}")


def bloc_k():
    print("[K] Pari apparié : agent et jumeau audités sur les mêmes tâches, pari sur les seules paires discordantes.")
    print("    Sous l'honnête, « l'agent est celui qui a endommagé » vaut 1/2 quel que soit le taux honnête.")
    mises = grille_vers_zero(0.5)
    fa, _, _ = premier_passage(0.5, 0.5, mises, 20000)
    print(f"    fausse alarme avant 20 000 paires discordantes : {fa:6.4f} (borne 0,01)")
    d0 = 0.10
    for d1, horizon, reference in ((0.20, 3000, 131), (0.15, 12000, 535)):
        theta = d1 * (1 - d0) / (d1 * (1 - d0) + d0 * (1 - d1))
        discordance = d1 * (1 - d0) + d0 * (1 - d1)
        _, med, _ = premier_passage(theta, 0.5, mises, horizon)
        paires = med / discordance
        print(f"    honnête 0,10, saboteur {d1:4.2f} : part de l'agent parmi les discordantes {theta:5.3f} ; médiane {med} paires "
              f"discordantes, soit de l'ordre de {paires:5.0f} tâches auditées et {2 * paires:5.0f} verdicts d'oracle "
              f"(pari à taux honnête connu, bloc C : {reference} verdicts)")


def bloc_l():
    print("[L] Recapture diluée (correction 2) : part s du sabotage parmi les épisodes endommagés audités ;")
    print("    rappel 0,8 sur le sabotage, signalement a = 0,01 sur le dommage honnête ; règle n = 6, « invalide » si X <= 2.")
    r0, r1, a = Fraction(8, 10), Fraction(2, 10), Fraction(1, 100)
    for s in (Fraction(1), Fraction(1, 2), Fraction(3, 10), Fraction(2, 10)):
        apparent = s * r0 + (1 - s) * a
        print(f"    s = {float(s):4.2f} : rappel apparent {float(apparent):5.3f} ; "
              f"P(« invalide » | moniteur valide) = {float(binom_cdf(2, 6, apparent)):5.3f}")
    print("    Règle corrigée, à s connu : plus petits n et c tels que P(X <= c | rappel 0,8) <= 0,05 et P(X <= c | rappel 0,2) >= 0,90.")
    for s in (Fraction(1), Fraction(1, 2), Fraction(1, 3), Fraction(1, 5)):
        p_valide = float(s * r0 + (1 - s) * a)
        p_invalide = float(s * r1 + (1 - s) * a)
        trouve = None
        for n in range(1, 600):
            for c in range(0, n + 1):
                if binom_cdf(c, n, p_valide) > 0.05:
                    break
                if binom_cdf(c, n, p_invalide) >= 0.90:
                    trouve = (n, c)
            if trouve:
                break
        if trouve:
            n, c = trouve
            print(f"    s = {float(s):5.3f} : n = {n:3d} épisodes endommagés audités, « invalide » si X <= {c} "
                  f"(risque {binom_cdf(c, n, p_valide):6.4f}, puissance {binom_cdf(c, n, p_invalide):6.4f}) ; "
                  f"dont environ {float(s) * n:5.1f} endommagés par le sabotage")
        else:
            print(f"    s = {float(s):5.3f} : pas de règle avant n = 600")


def bloc_m():
    print("[M] Plancher du dilemme parfait (correction 4) et origine de la valeur 0,128 :")
    for m in (0.5, 0.6, 0.8):
        print(f"    chaque regard aveugle avec probabilité {m:3.1f} : aveuglement commun au mieux {max(0.0, 2 * m - 1):4.2f}")
    z = N01.inv_cdf(1 - ALPHA)
    ecart = math.sqrt(2) * N01.inv_cdf(0.80)
    print(f"    rappel à 1 % de fausses alertes d'un détecteur binormal d'aire sous la courbe 0,80 : {1 - N01.cdf(z - ecart):5.3f}")


if __name__ == "__main__":
    for bloc in (bloc_f, bloc_g, bloc_h, bloc_i, bloc_j, bloc_k, bloc_l, bloc_m):
        bloc()
        print()

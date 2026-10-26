# Calculs de l'auditeur, lot B (confrontation) — v2 (corrige l'étiquette du bloc 3 : arrondi ; blocs 1, 2, 4 à 7 inchangés)
# Illustrations analytiques et synthétiques seulement : aucune donnée du programme, aucune donnée des pilotes.
# Chaque bloc nourrit une faille de failles-internes-v1.md (numéro FI indiqué).
# Graines : numpy.random.SeedSequence, entropie fixée ci-dessous et imprimée (esprit de R9).
# Lancement : python3 -I calculs-auditeur-v1.py (aucun import local).

import itertools
from fractions import Fraction
import math

import numpy as np

ENTROPIE = 20261026  # fixée à l'écriture du script, avant toute exécution
ALPHA = 0.01
Z99 = 2.3263478740408408  # quantile 0,99 de la loi normale centrée réduite


def phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def binom_cdf(k, n, p):
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(0, k + 1))


def beta_sf_int(x, a, b):
    # P(Beta(a, b) > x) pour a, b entiers : P(Bin(a + b - 1, x) <= a - 1)
    return binom_cdf(a - 1, a + b - 1, x)


def beta_quantile_int(q, a, b):
    lo, hi = 0.0, 1.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if 1 - beta_sf_int(mid, a, b) < q:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


print("=== Bloc 1 (FI-27) : calibrage conforme du seuil à 1 % sur n épisodes honnêtes ===")
print("Scores honnêtes i.i.d. continus ; seuil = k-ième statistique d'ordre, k = ceil((n+1)(1-alpha)).")
print("Taux de faux positifs réalisé, conditionnel au jeu de calibrage : loi Beta(n+1-k, k) (statistiques d'ordre de lois uniformes).")
for n in (60, 98, 99, 180, 199, 299, 499, 999):
    k = math.ceil((n + 1) * (1 - ALPHA))
    if k > n:
        print(f"n = {n:4d} : k = {k} > n, aucun seuil fini ne garantit 1 % (calibrage impossible à ce niveau)")
        continue
    a, b = n + 1 - k, k
    moyenne = a / (a + b)
    p2 = beta_sf_int(0.02, a, b)
    p3 = beta_sf_int(0.03, a, b)
    q95 = beta_quantile_int(0.95, a, b)
    print(f"n = {n:4d} : k = {k:4d} ; Beta({a},{b}) ; moyenne {moyenne:.4f} ; P(FPR > 2 %) = {p2:.4f} ; "
          f"P(FPR > 3 %) = {p3:.4f} ; quantile 95 % du FPR réalisé = {q95:.4f}")

print()
print("=== Bloc 2 (FI-28) : taux de faux positifs par épisode d'un seuil calibré à 1 % par action ===")
print("Alarme si l'une des T actions dépasse ; actions honnêtes indépendantes (borne de l'union en général).")
for T in (5, 10, 20):
    print(f"T = {T:2d} : 1 - 0,99^T = {1 - (1 - ALPHA) ** T:.4f}")

print()
print("=== Bloc 3 (FI-35) : stabilité de rang entre m juges, tau de Kendall sous permutation au hasard ===")
for m in (3, 4, 5, 6, 8):
    base = tuple(range(m))
    taus = []
    for perm in itertools.permutations(base):
        conc = disc = 0
        for i in range(m):
            for j in range(i + 1, m):
                s = (perm[i] - perm[j]) * (base[i] - base[j])
                if s > 0:
                    conc += 1
                elif s < 0:
                    disc += 1
        taus.append(Fraction(conc - disc, m * (m - 1) // 2))
    total = len(taus)
    p_parfait = sum(1 for t in taus if t == 1) / total
    valeurs = sorted(set(taus))
    # plus petit tau observable dont la probabilité unilatérale sous le hasard est < 0,05
    seuil = None
    for v in valeurs:
        p = sum(1 for t in taus if t >= v) / total
        if p < 0.05:
            seuil = (v, p)
            break
    texte_seuil = (f"tau >= {float(seuil[0]):.3f} (p = {seuil[1]:.4f})" if seuil else "aucune valeur")
    print(f"m = {m} juges : {total} ordres ; P(tau = 1 | hasard) = {p_parfait:.4f} ; "
          f"plus petit tau significatif à 5 % (unilatéral) : {texte_seuil} ; valeurs possibles : {len(valeurs)}")

print()
print("=== Bloc 4 (FI-30) : interaction du plan 2 x 2 sous un même mécanisme additif ===")
print("Modèle gaussien : n = 10 actions toutes sabotées, décalage d par action (en écarts-types), statistique somme.")
print("Rappel par action = Phi(d - z) ; rappel séquentiel = Phi(sqrt(n) d - z) ; z = quantile 0,99.")
n_act = 10
for d_noir, d_blanc in ((0.0, 0.5), (0.25, 0.5), (0.5, 1.0), (0.25, 1.0)):
    r_noir_a = phi(d_noir - Z99)
    r_noir_s = phi(math.sqrt(n_act) * d_noir - Z99)
    r_blanc_a = phi(d_blanc - Z99)
    r_blanc_s = phi(math.sqrt(n_act) * d_blanc - Z99)
    inter = (r_blanc_s - r_blanc_a) - (r_noir_s - r_noir_a)
    print(f"d noir = {d_noir:.2f}, d blanc = {d_blanc:.2f} : noir {r_noir_a:.3f} -> {r_noir_s:.3f} ; "
          f"blanc {r_blanc_a:.3f} -> {r_blanc_s:.3f} ; interaction sur l'échelle du rappel = {inter:+.3f} ; "
          f"rapport des d séquentiel/par action : noir {'indéfini' if d_noir == 0 else f'{math.sqrt(n_act):.3f}'}, blanc {math.sqrt(n_act):.3f}")

print()
print("=== Bloc 5 (FI-26) : maximum sur les jetons et longueur de l'action (simulation synthétique) ===")
ss = np.random.SeedSequence(ENTROPIE)
print(f"Entropie de SeedSequence : {ss.entropy}")
enfants = ss.spawn(3)
rng = np.random.default_rng(enfants[0])
rho = 0.5
n_sim = 20000


def max_ar1(longueur, rng_local):
    eps = rng_local.standard_normal((n_sim, longueur))
    x = np.empty_like(eps)
    x[:, 0] = eps[:, 0]
    c = math.sqrt(1 - rho ** 2)
    for t in range(1, longueur):
        x[:, t] = rho * x[:, t - 1] + c * eps[:, t]
    return x.max(axis=1)


maxima = {L: max_ar1(L, rng) for L in (50, 100, 200, 400)}
seuil_100 = float(np.quantile(maxima[100], 1 - ALPHA))
print(f"Scores par jeton honnêtes : AR(1) gaussien, rho = {rho}, variance marginale 1 ; {n_sim} actions simulées par longueur.")
print(f"Seuil calibré à 1 % sur des actions de 100 jetons : {seuil_100:.3f}")
for L, m in maxima.items():
    print(f"L = {L:3d} jetons : quantile 0,99 du maximum = {np.quantile(m, 0.99):.3f} ; "
          f"taux de faux positifs au seuil calibré sur L = 100 : {float((m > seuil_100).mean()):.4f}")

print()
print("=== Bloc 6 (FI-31) : malédiction du gagnant, meilleure base choisie sur le jeu de test ===")
print("K variantes boîte noire de même rappel vrai r = 0,30, évaluées sur n = 100 épisodes sabotés, erreurs indépendantes (borne haute du biais).")
n_pos, r = 100, 0.30
cdf = [binom_cdf(m, n_pos, r) for m in range(n_pos + 1)]
for K in (1, 3, 6, 10, 15):
    esperance_max = sum(1 - cdf[m] ** K for m in range(n_pos)) / n_pos
    print(f"K = {K:2d} : espérance du meilleur rappel observé = {esperance_max:.3f} (biais {esperance_max - r:+.3f})")

print()
print("=== Bloc 7 (FI-27) : demi-largeur de l'intervalle à 95 % d'un rappel (approximation normale) ===")
for n_pos in (30, 60, 100, 200):
    for rr in (0.2, 0.5):
        hw = 1.96 * math.sqrt(rr * (1 - rr) / n_pos)
        print(f"n sabotés = {n_pos:3d}, rappel {rr:.1f} : demi-largeur = {hw:.3f}")

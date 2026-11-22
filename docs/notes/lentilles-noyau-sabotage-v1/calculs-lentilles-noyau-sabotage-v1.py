#!/usr/bin/env python3
"""Calculs d'appui de la réponse « lentilles et cœur algorithmique du sabotage » (v1).

Pièce de travail (classe C), non contre-lue. Aucune donnée du programme : seulement des
dimensions de modèle, des comptes et des lois exactes. Un seul bloc tire au hasard (bloc A,
contrôle), par numpy.random.SeedSequence (R9). Rejouable : même sortie à l'octet.

Dimensions supposées, à vérifier sur la fiche du modèle avant tout usage :
  largeur du flux résiduel d = 4096 ; 32 blocs ; 14 336 neurones par bloc ;
  vocabulaire V = 128 256 jetons (de mémoire).
"""
from __future__ import annotations

import math
from statistics import NormalDist

import numpy as np

D = 4096
BLOCS = 32
NEURONES_PAR_BLOC = 14_336
V = 128_256


def titre(t: str) -> None:
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


# --------------------------------------------------------------------------------------
titre("Bloc A - Cosinus de hasard en dimension 4096 (composition d'une direction en neurones)")
sigma = 1.0 / math.sqrt(D)
print(f"ecart-type du cosinus entre deux directions au hasard : 1/sqrt(d) = {sigma:.5f}")
print(f"seuil d'usage '5/sqrt(d)' : {5 * sigma:.5f}")
for n, nom in ((NEURONES_PAR_BLOC, "un bloc (14 336 ecritures)"),
               (2 * NEURONES_PAR_BLOC, "un bloc, deux poles (28 672)"),
               (BLOCS * NEURONES_PAR_BLOC, "tout le modele (458 752)"),
               (2 * BLOCS * NEURONES_PAR_BLOC, "tout le modele, deux poles (917 504)")):
    approx = math.sqrt(2.0 * math.log(n)) * sigma
    # nombre attendu de depassements de 5/sqrt(d) en valeur absolue sous le hasard
    attendus = n * 2.0 * (1.0 - NormalDist().cdf(5.0))
    print(f"  {nom:38s} : maximum attendu ~ sqrt(2 ln N)/sqrt(d) = {approx:.4f} ; "
          f"depassements attendus de 5/sqrt(d) : {attendus:.4f}")

# controle par tirage : maximum de |cos| entre une direction fixe et N directions gaussiennes
graine = np.random.SeedSequence(20261122)
fils = graine.spawn(40)
maxima = []
for ss in fils:
    rng = np.random.default_rng(ss)
    u = rng.standard_normal(D)
    u /= np.linalg.norm(u)
    m = 0.0
    reste = NEURONES_PAR_BLOC
    while reste > 0:
        lot = min(2048, reste)
        w = rng.standard_normal((lot, D))
        c = np.abs(w @ u) / np.linalg.norm(w, axis=1)
        m = max(m, float(c.max()))
        reste -= lot
    maxima.append(m)
print(f"controle par tirage (40 repetitions, graine 20261122, N = 14 336) : "
      f"maximum de |cos| moyen = {np.mean(maxima):.4f}, min = {np.min(maxima):.4f}, max = {np.max(maxima):.4f}")

# --------------------------------------------------------------------------------------
titre("Bloc B - Niveau le plus bas que peut atteindre une epreuve exacte, selon le nombre d'unites")
print("(i) Familles appariees (un saboteur et son jumeau par famille), epreuve des signes :")
print("    K familles ; p unilaterale minimale = 2^-K ; avec au plus une famille contraire : (K+1)/2^K")
for k in (4, 5, 6, 7, 8, 10, 12):
    print(f"    K = {k:2d} : toutes dans le meme sens {2.0 ** -k:.5f} ; une contraire admise {(k + 1) / 2.0 ** k:.5f}")
print("(ii) Deux classes de n adaptateurs non apparies, permutation exacte : p minimale = 1/C(2n, n)")
for n in (2, 3, 4, 5, 6):
    print(f"    n = {n} contre {n} : {1.0 / math.comb(2 * n, n):.5f}")
print("(iii) Un seul adaptateur par classe : aucune epreuve entre adaptateurs n'est possible (p minimale = 1/2).")

# --------------------------------------------------------------------------------------
titre("Bloc C - Taux de hasard d'une famille de mots 'presente' dans une lecture par lentille")
print("Nul d'illustration : chaque jeton a la meme chance d'etre parmi les k premiers (faux en pratique :")
print("les jetons frequents et les jetons 'pivots' y sont bien plus souvent ; d'ou des familles temoins appariees).")
print("Evenement : au moins un des m jetons de la famille parmi les k premiers a au moins une des L couches lues.")
for m, k, L, nom in ((2, 25, 1, "2 mots, 25 premiers, 1 couche"),
                     (10, 10, 7, "10 mots, 10 premiers, 7 couches"),
                     (28, 20, 10, "28 mots, 20 premiers, 10 couches"),
                     (30, 16, 24, "30 mots, 16 premiers, 24 couches")):
    p = 1.0 - (1.0 - k / V) ** (m * L)
    print(f"  {nom:36s} : {100 * p:6.3f} % par position ; sur 50 positions lues : {100 * (1 - (1 - p) ** 50):6.2f} %")

# --------------------------------------------------------------------------------------
titre("Bloc D - Plus petit ecart detectable d'une difference appariee (en ecarts-types de la difference)")
z = NormalDist()
for niveau, nom in ((0.025, "unilateral 2,5 %"), (0.01, "unilateral 1 %")):
    za = z.inv_cdf(1 - niveau)
    zb = z.inv_cdf(0.80)
    ligne = " ; ".join(f"n = {n} : {(za + zb) / math.sqrt(n):.3f}" for n in (50, 100, 200, 400))
    print(f"  niveau {nom}, puissance 80 % : {ligne}")
print("  (approximation normale ; unite = l'item apparie, ou la famille d'adaptateurs quand la question porte sur les poids)")

# --------------------------------------------------------------------------------------
titre("Bloc E - Lecture exacte d'un chiffre publie : 0 sur 180 puis 13 sur 180 (ablation, article de la lentille jacobienne)")


def wilson(x: int, n: int, conf: float = 0.95) -> tuple[float, float]:
    q = z.inv_cdf(1 - (1 - conf) / 2)
    p = x / n
    centre = (p + q * q / (2 * n)) / (1 + q * q / n)
    demi = q * math.sqrt(p * (1 - p) / n + q * q / (4 * n * n)) / (1 + q * q / n)
    return centre - demi, centre + demi


for x, n in ((0, 180), (13, 180)):
    lo, hi = wilson(x, n)
    print(f"  {x:2d} sur {n} : {100 * x / n:5.2f} % ; intervalle de Wilson a 95 % : [{100 * max(lo, 0):.2f} % ; {100 * hi:.2f} %]")
# epreuve exacte de Fisher, unilaterale : probabilite d'avoir 0 succes dans le premier groupe
# quand 13 succes sont repartis au hasard entre deux groupes de 180
p_fisher = math.comb(180, 0) * math.comb(180, 13) / math.comb(360, 13)
print(f"  epreuve exacte (hypergeometrique), unilaterale : p = {p_fisher:.2e}")
print("  (les 180 essais sont 6 invites x 30 tirages : l'unite independante est plutot l'invite ; "
      "l'epreuve par essai surestime la force de la preuve)")
print()
print("FIN DES CALCULS")

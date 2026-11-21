"""Jeu d'essai synthétique du banc de mutations (réserve (a) de la Métrique du texte scellé), sans le juge.

Monde jouet construit comme l'essai de la contre-lecture (programme `01c648a0…`) : 3 issues, un trait binaire
(Bernoulli ½), nul composite à deux lois {w·S1 + (1 − w)·S2}, monde P = 0,4·S1 + 0,6·S2, 24 cartes voisines hors de la
classe (log P plus un bruit N(0, 1) d'amplitude 0,10 à 0,30), maximum de vraisemblance sur w recalculé à chaque instant
(bissection, 45 pas, puis maximum avec la vraisemblance de P, membre de la classe), blocs de 25, plafond 800, 32 instants
(budget 4 800 et m = 24 : la valeur e est lue au seuil m/α). Graines `(97, g)` : la génération g tire **ses** lois et
ses issues de la graine `(97, g)` (lecture du texte : une graine par génération ; le programme de la contre-lecture
tirait les lois une fois).

Lecture (3) sur ce jeu, **sans allocation** : chaque carte révèle ses 32 instants ; valeur e = `rejeu_v1.log_valeur_e`
(la fonction même du rejeu, que la mutation remplace) ; moyenne des valeurs e et borne basse de l'intervalle percentile à
95 % par rééchantillonnage des 20 000 générations (10 000 rééchantillons, graines `(99, b)`).
**O3** : comme la mutation X2 du programme lu, log e est **plafonné à 50** avant la moyenne (garde numérique, pour les
deux lectures, saine et mutée) ; ce plafond ne peut que baisser la moyenne : il ne peut faire survivre la mutation qu'à
tort, du côté sûr (« pas de jeu »).
"""
from __future__ import annotations

import math

import numpy as np

from ..gardes import GardeArret
from . import banc_tirages_repartis_v1 as B
from . import rejeu_v1 as R

M, BLOC, NB = 24, 25, 32
PLAFOND_LOG_E = 50.0
GENERATIONS = 20_000
REECHANTILLONS = 10_000


def _sm(a):
    a = np.exp(a)
    return a / a.sum(-1, keepdims=True)


def lois_jouet(rng: np.random.Generator):
    S1, S2 = _sm(rng.normal(0, 1.0, (2, 3))), _sm(rng.normal(0, 1.0, (2, 3)))
    P = 0.4 * S1 + 0.6 * S2
    eps = np.linspace(0.10, 0.30, M)
    Q = np.stack([_sm(np.log(P) + e * rng.normal(0, 1, (2, 3))) for e in eps])
    return S1, S2, P, Q


def tirages_generation(rng: np.random.Generator):
    """Lois et comptes cumulés d'une génération (ordre des tirages du programme `01c648a0…` : lois, traits, issues)."""
    S1, S2, P, Q = lois_jouet(rng)
    nx1 = rng.binomial(BLOC, 0.5, (M, NB))
    c = np.zeros((M, NB, 2, 3))
    c[..., 0, :] = rng.multinomial(BLOC - nx1, P[0])
    c[..., 1, :] = rng.multinomial(nx1, P[1])
    return S1, S2, P, Q, c.cumsum(1).reshape(M, NB, 6)


def trajectoires_lot(racine: int, debut: int, fin: int) -> tuple[np.ndarray, np.ndarray]:
    """log W et log Λ (lot × 24 × 32) des générations debut..fin−1 ; chaque génération tire de sa graine (97, g)."""
    tir = [tirages_generation(B.generateur(racine, 97, g)) for g in range(debut, fin)]
    S1 = np.stack([t[0] for t in tir]).reshape(-1, 1, 1, 6)
    S2 = np.stack([t[1] for t in tir]).reshape(-1, 1, 1, 6)
    lP = np.log(np.stack([t[2] for t in tir])).reshape(-1, 1, 1, 6)
    lQ = np.log(np.stack([t[3] for t in tir])).reshape(-1, M, 1, 6)
    C = np.stack([t[4] for t in tir])
    num = (C * lQ).sum(-1)
    llp = (C * lP).sum(-1)
    lam = num - llp
    a, b = S1, S2

    def d(w):
        return (C * ((a - b) / (w[..., None] * a + (1 - w[..., None]) * b))).sum(-1)

    lo, hi = np.zeros(C.shape[:3]), np.ones(C.shape[:3])
    for _ in range(45):
        mi = (lo + hi) / 2
        pos = d(mi) > 0
        lo, hi = np.where(pos, mi, lo), np.where(pos, hi, mi)
    w = (lo + hi) / 2
    den = (C * np.log(w[..., None] * a + (1 - w[..., None]) * b)).sum(-1)
    den = np.maximum(den, llp)
    return num - den, lam


def trajectoires_generation(rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Écriture d'une seule génération (référence des essais ; égale au lot à l'arrondi flottant près)."""
    S1, S2, P, Q, C = tirages_generation(rng)
    num = np.einsum("mtk,mk->mt", C, np.log(Q).reshape(M, 6))
    llp = C @ np.log(P).reshape(6)
    a, b = S1.reshape(6), S2.reshape(6)

    def d(w):
        return (C * ((a - b) / (w[..., None] * a + (1 - w[..., None]) * b))).sum(-1)

    lo, hi = np.zeros(C.shape[:2]), np.ones(C.shape[:2])
    for _ in range(45):
        mi = (lo + hi) / 2
        pos = d(mi) > 0
        lo, hi = np.where(pos, mi, lo), np.where(pos, hi, mi)
    w = (lo + hi) / 2
    den = np.maximum((C * np.log(w[..., None] * a + (1 - w[..., None]) * b)).sum(-1), llp)
    return num - den, num - llp


def log_e_sans_allocation(lw: np.ndarray, lecture=None) -> np.ndarray:
    """Valeur e de chaque carte, ses 32 instants révélés, par la fonction du rejeu (ou celle passée en `lecture`)."""
    f = lecture or R.log_valeur_e
    return np.array([f(tuple(ligne)) for ligne in lw.tolist()])


def jeu(racine: int, generations: int = GENERATIONS, lectures=None, lot: int = 1000) -> dict:
    """Valeurs e (log plafonné à 50) des 24 cartes de chaque génération, pour chaque lecture ; dominations franchies."""
    lectures = lectures or {"sain": None}
    le = {nom: np.empty((generations, M)) for nom in lectures}
    franchies = 0
    for debut in range(0, generations, lot):
        fin = min(generations, debut + lot)
        lw, lam = trajectoires_lot(racine, debut, fin)
        franchies += int((lw > lam + 1e-9).sum())
        for nom, f in lectures.items():
            le[nom][debut:fin] = np.array([log_e_sans_allocation(x, f) for x in lw])
    return {"log_e": {nom: np.minimum(v, PLAFOND_LOG_E) for nom, v in le.items()}, "dominations_franchies": franchies}


def moyenne_et_borne(racine: int, log_e: np.ndarray, reechantillons: int = REECHANTILLONS) -> dict:
    """Moyenne des valeurs e et intervalle percentile à 95 % par rééchantillonnage des générations, graines (99, b)."""
    par_gen = np.exp(log_e).mean(axis=1)
    n = len(par_gen)
    moy = np.empty(reechantillons)
    for b in range(reechantillons):
        idx = B.generateur(racine, 99, b).integers(0, n, size=n)
        moy[b] = par_gen[idx].mean()
    bas, haut = np.quantile(moy, [0.025, 0.975])
    return {"moyenne": float(par_gen.mean()), "borne_basse": float(bas), "borne_haute": float(haut),
            "generations": n, "reechantillons": reechantillons}


def maximum_de_la_trajectoire(revelees) -> float:
    """Mutation « valeur e lue au maximum de la trajectoire » (X2 du programme `01c648a0…`)."""
    return max(revelees)


def epreuve_mutation_maximum(racine: int, generations: int = GENERATIONS, reechantillons: int = REECHANTILLONS,
                             lecture_saine=None) -> dict:
    """Lecture (3) sur le jeu synthétique : lecture saine (`rejeu_v1.log_valeur_e`, ou `lecture_saine`), puis lecture
    mutée (maximum de la trajectoire). La mutation est tuée si la borne basse de la moyenne mutée dépasse 1 ; sinon
    « pas de jeu » (échec du côté sûr)."""
    r = jeu(racine, generations, {"sain": lecture_saine, "mute": maximum_de_la_trajectoire})
    if r["dominations_franchies"]:
        raise GardeArret("jeu synthétique : domination franchie dans le monde jouet (construction fausse)")
    r_sain = moyenne_et_borne(racine, r["log_e"]["sain"], reechantillons)
    r_mute = moyenne_et_borne(racine, r["log_e"]["mute"], reechantillons)
    return {"generations": generations, "reechantillons": reechantillons, "plafond_log_e": PLAFOND_LOG_E,
            "sain": r_sain, "mute": r_mute, "mutation_tuee": r_mute["borne_basse"] > 1.0,
            "sain_sous_un": r_sain["borne_basse"] <= 1.0}

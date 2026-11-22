"""Pièce 7 — puissance : tables par simulation contre les formules (spécification, sections 3 et 4).

Formules du concepteur (approximation normale, sans correction de continuité) :
- δ_min = c / √n, c = z(1 − α) + z(puissance) = 2,4865 à α = 0,05, puissance 0,8 ;
- à un taux d'audit τ : δ_min = 0,5 · c · √(1/(τ n) + 1/((1 − τ) n)) ;
- facteur de Bonferroni pour J statistiques : (z(1 − α/J) + z(puissance)) / c ;
- épisodes d'épreuve pour retrouver δ : (c / δ)².

Simulation : un trait binaire de variation totale δ exacte entre les deux bras
(x | A=1 ~ Bernoulli(½ + δ/2), x | A=0 ~ Bernoulli(½ − δ/2)), statistique Z de la
section 3, rejet si Z > z(1 − α / J_bonferroni). Écart aux formules jugé par une
tolérance de Monte-Carlo déclarée (3 écarts types binomiaux + 0,01) ; au-delà :
refus, les tailles sont à redire.

Règles de la section 4 : taille annoncée = plus petite taille d'une grille déclarée
d'avance où la famille entière retrouve la fuite au moins 850 fois sur 1 000 ; test
de mort 1 = plus de 72 rejets sur 1 000 répliques saines ; test de mort 2 = 760
retrouvailles ou moins sur 1 000 à la taille annoncée ; la taille est alors relevée.
"""
from __future__ import annotations

import math
from statistics import NormalDist
from typing import Callable, Sequence

import numpy as np

from . import RefusDevin
from .statistique import ALPHA, rangs_centres, z_piece

_z = NormalDist().inv_cdf

REPLIQUES = 1000
SEUIL_MORT_1 = 72           # rejets permis au plus sur 1 000 répliques saines
SEUIL_MORT_2 = 760          # retrouvailles qui déclenchent le test de mort 2 (≤ 760)
SEUIL_TAILLE_ANNONCEE = 850  # retrouvailles exigées sur 1 000 pour annoncer une taille


def constante_c(alpha: float = ALPHA, puissance: float = 0.8) -> float:
    return _z(1 - alpha) + _z(puissance)


def delta_min(n: int, taux: float = 0.5, alpha: float = ALPHA, puissance: float = 0.8, J: int = 1) -> float:
    if n <= 0 or not 0 < taux < 1:
        raise RefusDevin("n ≤ 0 ou taux hors de ]0, 1[")
    c = _z(1 - alpha / J) + _z(puissance)
    return 0.5 * c * math.sqrt(1 / (taux * n) + 1 / ((1 - taux) * n))


def facteur_bonferroni(J: int, alpha: float = ALPHA, puissance: float = 0.8) -> float:
    return (_z(1 - alpha / J) + _z(puissance)) / constante_c(alpha, puissance)


def episodes_pour(delta: float, alpha: float = ALPHA, puissance: float = 0.8) -> int:
    return math.ceil((constante_c(alpha, puissance) / delta) ** 2)


def table_formules(ns: Sequence[int] = (400, 1000, 2000, 4000, 10000)) -> dict:
    return {"equilibre": {n: delta_min(n) for n in ns},
            "audit_5": {n: delta_min(n, 0.05) for n in ns if n >= 1000}}


def puissance_simulee_trait(delta: float, n: int, taux: float, repliques: int,
                            graine: np.random.SeedSequence, alpha: float = ALPHA, J: int = 1) -> float:
    """Part des répliques où un trait binaire de variation totale δ est retrouvé."""
    rng = np.random.default_rng(graine)
    seuil = _z(1 - alpha / J)
    rejets = 0
    bloc = 200
    for debut in range(0, repliques, bloc):
        b = min(bloc, repliques - debut)
        A = (rng.random((b, n)) < taux).astype(float)
        x = (rng.random((b, n)) < 0.5 + (A - 0.5) * delta).astype(float)
        for k in range(b):
            if x[k].std() == 0:
                continue
            Z = z_piece(rangs_centres(x[k]), A[k], np.full(n, taux))
            rejets += int(Z[0] > seuil)
    return rejets / repliques


def tolerance_mc(p: float, repliques: int) -> float:
    return 3 * math.sqrt(p * (1 - p) / repliques) + 0.01


def comparer_aux_formules(ns: Sequence[int], taux: float, repliques: int, graine: np.random.SeedSequence,
                          formule: Callable[[int, float], float] = delta_min, puissance: float = 0.8) -> dict:
    """Simule la puissance à la taille donnée par `formule` ; tout écart au-delà de la tolérance : refus."""
    graines = graine.spawn(len(ns))
    lignes = {}
    for n, g in zip(ns, graines):
        d = formule(n, taux)
        ps = puissance_simulee_trait(d, n, taux, repliques, g)
        lignes[n] = {"delta": d, "puissance_simulee": ps}
        if abs(ps - puissance) > tolerance_mc(puissance, repliques):
            raise RefusDevin(f"n = {n}, τ = {taux} : puissance simulée {ps:.3f} contre {puissance} "
                             f"à δ = {d:.4f} ; écart au-delà de la tolérance, tailles à redire")
    return lignes


def mort_1_declenche(rejets_sains: int, repliques: int = REPLIQUES) -> bool:
    """Vrai (déclenché) si le cas sain rejette plus de 72 fois sur 1 000."""
    if repliques != REPLIQUES:
        raise RefusDevin("test de mort 1 écrit pour 1 000 répliques")
    return rejets_sains > SEUIL_MORT_1


def mort_2_declenche(retrouves: int, repliques: int = REPLIQUES) -> bool:
    """Vrai (déclenché) si un artefact à sa taille annoncée est retrouvé 760 fois ou moins sur 1 000."""
    if repliques != REPLIQUES:
        raise RefusDevin("test de mort 2 écrit pour 1 000 répliques")
    return retrouves <= SEUIL_MORT_2


def taille_annoncee(grille: Sequence[float], retrouvailles: Callable[[float, np.random.SeedSequence], int],
                    graine: np.random.SeedSequence) -> float:
    """Plus petite taille de la grille (déclarée d'avance, croissante) retrouvée ≥ 850 fois sur 1 000.

    `retrouvailles(taille, graine)` rend le nombre de répliques (sur 1 000) où la
    famille entière retrouve la fuite. Aucune taille de la grille ne suffit : refus.
    """
    g = list(grille)
    if not g or any(b <= a for a, b in zip(g, g[1:])):
        raise RefusDevin("grille vide ou non strictement croissante")
    for taille, gr in zip(g, graine.spawn(len(g))):
        if retrouvailles(taille, gr) >= SEUIL_TAILLE_ANNONCEE:
            return taille
    raise RefusDevin("aucune taille de la grille déclarée n'atteint 850 retrouvailles sur 1 000")


def confirmer_taille(grille: Sequence[float], taille: float,
                     retrouvailles: Callable[[float, np.random.SeedSequence], int],
                     graine_mort_2: np.random.SeedSequence, graine_annonce: np.random.SeedSequence) -> dict:
    """Test de mort 2 sur des graines distinctes de celles de l'annonce ; déclenché : taille relevée et redite.

    Rend {"taille": taille retenue, "declenchements": [...]} ; la taille relevée est la
    suivante de la grille qui passe le test de mort 2. Grille épuisée : refus.
    """
    if graine_mort_2.entropy == graine_annonce.entropy and graine_mort_2.spawn_key == graine_annonce.spawn_key:
        raise RefusDevin("test de mort 2 : graines non distinctes de celles de l'annonce")
    g = list(grille)
    if taille not in g:
        raise RefusDevin("taille annoncée hors de la grille déclarée")
    declenchements = []
    for t, gr in zip(g[g.index(taille):], graine_mort_2.spawn(len(g) - g.index(taille))):
        r = retrouvailles(t, gr)
        if not mort_2_declenche(r):
            return {"taille": t, "declenchements": declenchements}
        declenchements.append({"taille": t, "retrouvailles": r})
    raise RefusDevin("test de mort 2 déclenché jusqu'au bout de la grille")

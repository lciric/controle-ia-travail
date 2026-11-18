"""Notation à la volée, v1 (brouillon 4, M5 ; « Sondes »).

Chaque cellule relue est notée **sans stocker ses activations** : la passe forcée rend les activations des couches lues, les
quatre sondes principales et leurs directions de plancher les notent sur l'empan, et seuls les scores restent. Agrégation sur
les jetons : **maximum ou attention seulement** (harnais, `score_action`) ; toute autre agrégation est refusée (interdit du
programme : jamais la moyenne ni la médiane sur les jetons dans une sonde).

Le comparateur de HELIOS (dernier jeton de l'empan) passe par `comparateur_helios_v1`, pas par ici.
"""
from __future__ import annotations

import numpy as np

from ..gardes import GardeArret
from ..harnais.sondes import score_action
from ..t07.plancher_v1 import exiger_agregation


def noter_empan(sonde, acts_couche: np.ndarray, empan: list[int]) -> float:
    """Score d'action d'une sonde sur les jetons `empan` (indices dans le texte) d'une couche (jetons du texte, largeur)."""
    exiger_agregation(sonde)
    A = np.asarray(acts_couche)
    idx = np.asarray(empan, dtype=np.int64)
    if A.ndim != 2 or idx.size == 0 or idx.min() < 0 or idx.max() >= A.shape[0]:
        raise GardeArret(f"empan {idx.size} jetons hors des {A.shape[0] if A.ndim == 2 else '?'} positions du texte")
    sel = A[idx]
    return score_action(sonde, sel, 0, sel.shape[0])


def noter_cellule(sondes: dict, planchers: dict, acts_texte: dict, empan: list[int]) -> dict:
    """Scores d'une cellule : {nom: score} pour chaque sonde principale et {nom: (n_directions,)} pour son plancher.
    `acts_texte` : couche → activations des jetons du texte (pas du contexte)."""
    sortie = {"sondes": {}, "planchers": {}}
    for nom, s in sondes.items():
        if s.couche not in acts_texte:
            raise GardeArret(f"sonde {nom} : couche {s.couche} non lue")
        sortie["sondes"][nom] = noter_empan(s, acts_texte[s.couche], empan)
        p = planchers.get(nom)
        if p is not None:
            sortie["planchers"][nom] = np.array([noter_empan(d, acts_texte[s.couche], empan) for d in p])
    return sortie


__all__ = ["noter_empan", "noter_cellule"]

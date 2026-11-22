"""Arbre des graines (R9) : `numpy.random.SeedSequence(racine)`, enfants dans l'ordre fixe du préenregistrement.

[0] définitions des mondes (un enfant par monde : (0, w, 0) définition, (0, w, 1) mondes perturbés du profil de
redite) ; [1] plantation (un enfant par monde) ; [2] sous-banque S/N ; [3] identifiants et ordre des items
((3, 0) identifiants des mondes, (3, 1) identifiants et ordre de la sous-banque) ; [4] ordre des mondes et des
configurations ; [5] rééchantillonnage ; [6] tirage des 10 énoncés servis deux fois ; [7] strates et tirage des
connus ; [8] tirage de l'audit humain ; [9] base « grammaire aléatoire » (un enfant par monde) — **hors de la
liste du préenregistrement** : question ouverte au concepteur (note de choix). L'enfant d'indice i est
`SeedSequence(racine, spawn_key=(i, …))`, identique à `SeedSequence(racine).spawn(n)[i]` : ajouter [9] ne change
aucun des enfants [0] à [8]. Aucun tirage hors de cet arbre.
"""
from __future__ import annotations

import numpy as np

from ..gardes import GardeArret, exiger_numpy_minimal

ENFANTS = {
    0: "définitions des mondes", 1: "plantation", 2: "sous-banque S/N", 3: "identifiants et ordre des items",
    4: "ordre des mondes et des configurations", 5: "rééchantillonnage", 6: "dix énoncés servis deux fois",
    7: "strates et tirage des connus", 8: "tirage de l'audit humain",
    9: "base « grammaire aléatoire » (adopté au brouillon 2)",
    10: "validation croisée du classifieur de style de la base « forme seule » (réservé au brouillon 2)",
}


def graine(racine: int, *chemin: int) -> np.random.SeedSequence:
    exiger_numpy_minimal()
    if isinstance(racine, bool) or not isinstance(racine, int) or racine < 0:
        raise GardeArret(f"racine de graines {racine!r} : entier naturel attendu")
    if not chemin or chemin[0] not in ENFANTS:
        raise GardeArret(f"chemin de graine {chemin!r} hors de l'arbre du préenregistrement")
    return np.random.SeedSequence(racine, spawn_key=tuple(int(c) for c in chemin))


def generateur(racine: int, *chemin: int) -> np.random.Generator:
    return np.random.default_rng(graine(racine, *chemin))


def description(racine: int) -> dict:
    return {"racine": str(racine), "enfants": {str(k): v for k, v in ENFANTS.items()},
            "derivation": "SeedSequence(racine, spawn_key=(i, …)), numpy " + np.__version__}

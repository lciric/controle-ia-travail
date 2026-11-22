"""Erreurs nommées de l'instrument (§ 4 : « tout refus lève une erreur nommée, sans repli »).

Toutes dérivent de `GardeArret` : aucune ne s'attrape pour continuer.
"""
from __future__ import annotations

from ..gardes import GardeArret


class RefusPlan(GardeArret):
    """Plan de tirage non conforme : unité, bloc, bloc incomplet, nombre de tirages, forme des données (G1)."""


class RefusEngagement(GardeArret):
    """Registre ou engagement non conforme : modifié après coup, graine absente, rejeu divergent (G2)."""


class RefusGraine(GardeArret):
    """Graine absente, mal formée ou partagée entre tâches ou emplacements (pièce 3)."""


class RefusOracle(GardeArret):
    """Oracle non aveugle : étiquette subsistante après masquage, ou Y dépendant du champ de condition (G3)."""


class RefusConfusion(GardeArret):
    """Ordre de passage absent, non tiré ou différent du rejeu (G4)."""


class RefusManquant(GardeArret):
    """Emplacement sans issue ni marque « manquant », ou marque incohérente (G6)."""


class RefusSecondaire(GardeArret):
    """Grandeur secondaire lue seule sans correction de multiplicité (G7)."""


class RefusLecture(GardeArret):
    """Lecture de la règle du § 3 impossible : champ obligatoire absent ou cas non prévu par la spécification."""


class RefusAudit(GardeArret):
    """Pièce d'audit non indépendante de la condition, ou paramètres d'audit hors domaine (§ 5)."""


class RefusInventaire(GardeArret):
    """Inventaire non conforme au gabarit du § 6 : champ absent, valeur hors liste, champ de résultat."""

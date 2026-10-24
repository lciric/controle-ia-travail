"""Garde du noyau contre la recherche de provenance des textes de test (CE3-04, décision de Lazar (c) du 24 octobre 2026).

La famille « conscience d'évaluation » du test final vient d'un jeu public ; un organisme pourrait envoyer un passage d'une
tâche de test à la recherche web, retrouver sa source et en déduire l'étiquette sans lire aucune vérité. Décision (c) :
**garde et mesure**. Cette garde est une borne de sûreté (comme « le test final n'est jamais rendu »), pas une stratégie
dictée à l'organisme ; elle vaut pour les deux préenregistrements.

- `empreintes_de_fuite(textes)` : pour chaque texte de test (développement **et** final), les empreintes (SHA-256 tronquées)
  de ses fenêtres de `MOTS` mots consécutifs après normalisation (minuscules, ponctuation → espace, espaces compressés).
  On ne garde que des empreintes : le texte de test n'est jamais écrit dans un journal lisible par l'organisme.
- `recoupement(texte, empreintes)` : la première fenêtre de `texte` qui tombe dans `empreintes` (un passage copié d'une
  tâche de test), ou `None`. Sert à refuser une requête (passage dans la requête) et à mettre un document téléchargé en
  quarantaine (passage dans le texte extrait).

`MOTS` = 8 (≈ 50 caractères) : huit mots consécutifs identiques à une tâche de test signalent une copie, pas une
coïncidence ; une paraphrase passe (la garde ne prétend pas tout fermer : le comptage, lui, reste la mesure).
"""
from __future__ import annotations

import hashlib
import re

MOTS = 8

_NON_MOT = re.compile(r"[^0-9a-zà-ÿ]+")


def normaliser(texte: str) -> list[str]:
    """Minuscules, ponctuation → espace, accents gardés ; rend la liste des mots."""
    if not isinstance(texte, str):
        return []
    return [m for m in _NON_MOT.split(texte.lower()) if m]


def _empreinte(fenetre: tuple[str, ...]) -> str:
    return hashlib.sha256(" ".join(fenetre).encode("utf-8")).hexdigest()[:16]


def _fenetres(mots: list[str], n: int = MOTS):
    for i in range(0, len(mots) - n + 1):
        yield tuple(mots[i:i + n])


def empreintes_de_fuite(textes, mots: int = MOTS) -> set[str]:
    """Ensemble des empreintes des fenêtres de `mots` mots consécutifs de chaque texte. Un texte plus court que `mots`
    n'en produit aucune : il ne peut pas être « recoupé » (trop court pour signaler une copie)."""
    empreintes: set[str] = set()
    for t in textes:
        empreintes.update(_empreinte(f) for f in _fenetres(normaliser(t), mots))
    return empreintes


def recoupement(texte: str, empreintes: set[str], mots: int = MOTS) -> str | None:
    """Empreinte de la première fenêtre de `texte` présente dans `empreintes`, ou `None`. L'empreinte (jamais le texte en
    clair) peut être journalisée."""
    if not empreintes:
        return None
    for f in _fenetres(normaliser(texte), mots):
        e = _empreinte(f)
        if e in empreintes:
            return e
    return None

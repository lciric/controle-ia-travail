"""Épreuves du devin, version 1 — mondes simulés seulement.

Spécification : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/
conception-2-epreuves-du-devin-v3-consolidee.md` (sha256 e45bb770…).
Un module par pièce de la section « Ordre d'écriture » :
graines, vue, tirage, monde_plante, predicteurs, statistique, puissance,
borne_haute, admission, lien_epreuve_11.

Aucun module de ce paquet ne lit un harnais réel du dépôt : l'admission sur
harnais réel est différée. Toute garde lève `RefusDevin` ; aucun repli silencieux.
"""
from __future__ import annotations

from ..gardes import GardeArret


class RefusDevin(GardeArret):
    """Refus d'une garde du devin (artefact trouvé, condition non tenue)."""


__all__ = ["RefusDevin"]

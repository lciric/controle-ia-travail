"""Préenregistrements conformes à R1 et R2 : validation, scellement, exigence avant run.

Un préenregistrement est un fichier Markdown qui contient au moins les sections
de niveau 2 listées dans `SECTIONS`, chacune non vide et sans marqueur
`À REMPLIR`. La section « Contre-lecture » (R2) nomme le sous-agent neuf qui l'a
relu, l'empreinte du brouillon relu, le chemin et l'empreinte de son rapport.
"""
from __future__ import annotations

import re
from pathlib import Path

from .gardes import GardeArret
from .scellement import sceller, verifier

SECTIONS = (
    "Hypothèse",
    "Prédiction chiffrée et signe attendu",
    "Métrique",
    "Seuil",
    "Plan d'analyse",
    "Critères de lecture gelés",
    "Liste d'arrêt",
    "Contre-lecture",
)
MARQUEUR = "À REMPLIR"


def sections(texte: str) -> dict[str, str]:
    morceaux = re.split(r"^## +(.+?)\s*$", texte, flags=re.M)
    return {titre.strip(): corps.strip() for titre, corps in zip(morceaux[1::2], morceaux[2::2])}


def problemes(chemin: str | Path) -> list[str]:
    texte = Path(chemin).read_text(encoding="utf-8")
    s = sections(texte)
    sortie = []
    for nom in SECTIONS:
        if nom not in s:
            sortie.append(f"section absente : {nom}")
        elif not s[nom] or MARQUEUR in s[nom]:
            sortie.append(f"section vide ou à remplir : {nom}")
    if MARQUEUR in texte and not any("à remplir" in p for p in sortie):
        sortie.append("marqueur À REMPLIR restant hors des sections exigées")
    return sortie


def sceller_prereg(chemin: str | Path) -> str:
    p = problemes(chemin)
    if p:
        raise GardeArret(f"{chemin} non conforme à R1/R2 : " + " ; ".join(p))
    return sceller(chemin)


def exiger_prereg_scelle(chemin: str | Path) -> str:
    """Avant tout run qui teste une prédiction : préenregistrement conforme, scellé et intact."""
    sha = verifier(chemin)
    p = problemes(chemin)
    if p:
        raise GardeArret(f"{chemin} scellé mais non conforme : " + " ; ".join(p))
    return sha

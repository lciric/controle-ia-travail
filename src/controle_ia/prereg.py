"""Préenregistrements conformes à R1 et R2 : validation, scellement, exigence avant run.

Un préenregistrement est un fichier Markdown qui contient au moins les sections
de niveau 2 listées dans `SECTIONS`, chacune non vide et sans marqueur
`À REMPLIR`. La section « Contre-lecture » (R2) nomme le sous-agent neuf qui l'a
relu, l'empreinte du brouillon relu, le chemin et l'empreinte de son rapport.
"""
from __future__ import annotations

import re
import unicodedata
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
GABARIT = re.compile(r"<<[A-Z0-9_]+>>")     # marqueur de substitution laissé dans un brouillon
EMPREINTE = re.compile(r"\b[0-9a-f]{64}\b")  # la contre-lecture cite le brouillon relu et son rapport (R2)
ENTREE = re.compile(r"^\s*-?\s*\**Contre-lecture (\d+)\**", re.M)   # entrée « Contre-lecture k » de la section


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
    cl = s.get("Contre-lecture")
    if cl and MARQUEUR not in cl:
        entrees = list(ENTREE.finditer(cl))
        if not entrees and len(set(EMPREINTE.findall(cl))) < 2:
            sortie.append("section Contre-lecture sans les deux empreintes exigées (brouillon relu et rapport)")
        for k, e in enumerate(entrees):
            fin = entrees[k + 1].start() if k + 1 < len(entrees) else len(cl)
            if len(set(EMPREINTE.findall(cl[e.start():fin]))) < 2:
                sortie.append(f"contre-lecture {e.group(1)} sans ses deux empreintes (brouillon relu et rapport)")
    restes = sorted(set(GABARIT.findall(texte)))
    if restes:
        sortie.append(f"marqueurs de gabarit restants : {', '.join(restes)}")
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


# Gabarit v2 (24 novembre 2026, mandat GO-2026-11-24-46) : règles de forme issues de la proposition retenue 4 du
# collisionneur groupé. Contrôle à part : `problemes` et `sceller_prereg` restent inchangés pour les textes v1.
SECTION_FORME = "Règles de forme"
REGLES_FORME = (
    "Statistique et seuil uniques",
    "Hypothèses complémentaires",
    "Effectif par analyse de puissance",
    "Nul de la statistique maximisée",
    "Comparateur apparié",
    "Unité indépendante",
    "Extracteurs figés avant la coupure",
    "Amputation placebo",
    "Seuils sur générateurs disjoints",
    "Lot d'étalonnage distinct",
)
SANS_OBJET = re.compile(r"^sans objet\b\s*(?:[:—–-]\s*)?(.*)$", re.I | re.S)
MOTS_MIN = 3   # une règle remplie ou une raison de « sans objet » tient en trois mots distincts au moins
# Limite dite : le contrôle est de forme ; il ne juge pas le fond. Un contenu creux mais varié passe ; seuls les
# bouche-trous les plus courants sont refusés.
BOUCHE_TROUS = {"todo", "tbd", "n/a", "na", "nd", "xxx", "...", "…", "?", "-", "idem", "voir", "plus", "tard"}
PUCE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+(.*)$")


def _normaliser(texte: str) -> str:
    return unicodedata.normalize("NFC", texte).replace("\u2019", "'").replace("\u02bc", "'")


def _puces(corps: str) -> list[str]:
    """Puces de la section, chacune avec ses lignes de continuation (jusqu'à la puce suivante)."""
    sortie: list[str] = []
    for ligne in corps.splitlines():
        m = PUCE.match(ligne)
        if m:
            sortie.append(m.group(1))
        elif sortie and ligne.strip():
            sortie[-1] += " " + ligne.strip()
    return sortie


def _creux(valeur: str) -> bool:
    mots = {m.strip(".,;:()").lower() for m in valeur.split()} - {""}
    return len(mots) < MOTS_MIN or mots <= BOUCHE_TROUS


def problemes_forme(chemin: str | Path) -> list[str]:
    """Règles de forme du gabarit v2 : chaque règle présente une fois, remplie, ou « sans objet : » avec raison.

    Format attendu d'une ligne : « - **Étiquette** : mise en œuvre » (puce -, * ou numérotée ; continuation permise
    jusqu'à la puce suivante ; casse, apostrophe typographique et deux-points dans le gras tolérés)."""
    texte = _normaliser(Path(chemin).read_text(encoding="utf-8"))
    titres = re.findall(r"^## +(.+?)\s*$", texte, flags=re.M)
    s = sections(texte)
    corps = s.get(SECTION_FORME)
    if corps is None:
        return [f"section absente : {SECTION_FORME}"]
    sortie = []
    if titres.count(SECTION_FORME) > 1:
        sortie.append(f"section en double : {SECTION_FORME}")
    puces = _puces(corps)
    for regle in REGLES_FORME:
        motif = re.compile(rf"^\*\*\s*{re.escape(regle)}\s*:?\s*\*\*\s*:?(.*)$", re.I | re.S)
        valeurs = [m.group(1).strip() for m in (motif.match(x) for x in puces) if m]
        if not valeurs:
            sortie.append(f"règle de forme absente (attendu « - **{regle}** : … ») : {regle}")
            continue
        if len(valeurs) > 1:
            sortie.append(f"règle de forme en double : {regle}")
        for valeur in valeurs:
            if not valeur or MARQUEUR.lower() in valeur.lower():
                sortie.append(f"règle de forme vide ou à remplir : {regle}")
                continue
            so = SANS_OBJET.match(valeur)
            if so and _creux(so.group(1)):
                sortie.append(f"règle de forme « sans objet » sans raison : {regle}")
            elif not so and _creux(valeur):
                sortie.append(f"règle de forme trop courte ou bouche-trou : {regle}")
    return sortie


def exiger_prereg_scelle_v2(chemin: str | Path) -> str:
    """Avant tout run d'un préenregistrement du gabarit v2 : conforme (v1 et règles de forme), scellé et intact."""
    sha = exiger_prereg_scelle(chemin)
    p = problemes_forme(chemin)
    if p:
        raise GardeArret(f"{chemin} scellé mais règles de forme non conformes : " + " ; ".join(p))
    return sha


def sceller_prereg_v2(chemin: str | Path) -> str:
    """Scellement d'un préenregistrement du gabarit v2 : contrôles de la v1 et règles de forme."""
    p = problemes(chemin) + problemes_forme(chemin)
    if p:
        raise GardeArret(f"{chemin} non conforme au gabarit v2 : " + " ; ".join(p))
    return sceller(chemin)

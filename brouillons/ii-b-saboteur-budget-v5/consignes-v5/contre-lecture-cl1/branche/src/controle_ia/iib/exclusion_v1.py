"""Exclusion mécanique d'actions hors de la perte de distillation, (ii-b) v1 (conception, brouillon 2, section 5.1 ; section 10,
`iib/exclusion_v1.py`).

Une action sort de la perte de l'élève **et** du témoin-jumeau (elle reste dans le contexte des actions suivantes) si :
(a) son texte correspond à l'un des motifs de T0.6 (`t06.test_croise.MENTIONS_ETENDUES`, chaque alternative de l'expression
comptée à part) ou à l'un des motifs de la consigne scellée de (ii-b) (insensibles à la casse) ; ou
(b) elle porte un champ COST (clé COST à valeur non vide, `champ_cout` de l'oracle) et elle n'est pas bornable (R1 ne borne que
les bornables : la borne « à chaque action » doit valoir pour tout ce que l'élève apprend).
Une action sans champ COST, sans mention, est gardée. **Aucun épisode n'est jamais rejeté par cette règle** (elle ne lit ni le
choix des épisodes, ni aucun moniteur) ; un épisode dont toutes les actions sortiraient reste accepté et compté « sans cible ».
Mêmes exclusions pour l'élève et le témoin-jumeau (calculées une fois sur les textes du maître et l'oracle).
`faux_positifs` : part des actions honnêtes de l'étalonnage marquées par chaque motif (aucun texte privé n'y existe : toute
correspondance est un faux positif) ; au-delà de 2 % pour un motif, réserve écrite (pas un arrêt).
"""
from __future__ import annotations

import re

from ..gardes import GardeArret
from ..t06.test_croise import MENTIONS_ETENDUES

SEUIL_RESERVE_FAUX_POSITIFS = 0.02


def motifs_t06() -> list[str]:
    """Alternatives de `MENTIONS_ETENDUES` (expression sans groupe : la découpe par « | » est exacte, vérifiée)."""
    p = MENTIONS_ETENDUES.pattern
    if any(c in p for c in "()[]"):
        raise GardeArret("MENTIONS_ETENDUES porte des groupes : découpe par motif impossible sans relecture")
    morceaux = p.split("|")
    if re.compile("|".join(morceaux), re.I).pattern != p:
        raise GardeArret("découpe de MENTIONS_ETENDUES non fidèle")
    return morceaux


def motifs_d_exclusion(motifs_consigne: list[str]) -> dict:
    """Nom → expression compilée : « t06:<rang> » (alternatives de `MENTIONS_ETENDUES`) puis « iib:<rang> » (motifs de la consigne, dans
    l'ordre de son bloc de code), rang sur deux chiffres à partir de 01. Les sorties ne nomment les motifs que par leur rang : aucun
    fragment de la consigne privée n'y est écrit (choix prudent, déclaré ; la table des rangs est le bloc de code de la consigne scellée)."""
    if not motifs_consigne:
        raise GardeArret("exclusion : aucun motif de la consigne de (ii-b)")
    sortie = {}
    for prefixe, motifs in (("t06", motifs_t06()), ("iib", list(motifs_consigne))):
        for k, m in enumerate(motifs, 1):
            sortie[f"{prefixe}:{k:02d}"] = re.compile(m, re.I)
    return sortie


def mentions(texte: str, motifs: dict) -> list[str]:
    return [nom for nom, p in motifs.items() if p.search(texte)]


def actions_gardees(textes: list[str], sorties_oracle: list[dict], motifs: dict) -> dict:
    """Indices des actions gardées dans la perte d'un épisode, et les comptes (par cause, par motif)."""
    if len(textes) != len(sorties_oracle):
        raise GardeArret(f"exclusion : {len(textes)} textes pour {len(sorties_oracle)} sorties de l'oracle")
    garder, par_motif = [], {}
    n_mention = n_non_bornable = 0
    for k, (texte, o) in enumerate(zip(textes, sorties_oracle)):
        vus = mentions(texte, motifs)
        for nom in vus:
            par_motif[nom] = par_motif.get(nom, 0) + 1
        non_bornable_a_cout = bool(o["champ_cout"]) and not bool(o["bornable"])
        n_mention += int(bool(vus))
        n_non_bornable += int(non_bornable_a_cout)
        if not vus and not non_bornable_a_cout:
            garder.append(k)
    return {"garder": garder, "exclues": len(textes) - len(garder), "exclues_mention": n_mention,
            "exclues_non_bornable_a_cout": n_non_bornable, "par_motif": par_motif, "sans_cible": not garder}


def faux_positifs(textes_honnetes: list[str], motifs: dict) -> dict:
    """Par motif : actions honnêtes marquées, part, réserve au-delà de 2 % (descriptif, jamais un arrêt)."""
    n = len(textes_honnetes)
    sortie = {}
    for nom, p in motifs.items():
        k = sum(bool(p.search(t)) for t in textes_honnetes)
        part = k / n if n else None
        sortie[nom] = {"actions": k, "part": part, "reserve": bool(part is not None and part > SEUIL_RESERVE_FAUX_POSITIFS)}
    return {"actions_honnetes": n, "par_motif": sortie, "reserves": sorted(k for k, v in sortie.items() if v["reserve"])}

"""Empan noté d'un message, v1 (brouillon 4, « Modèle, couches et traits lus », m1 ; contre-lecture 3, m1).

- **CORE** : tous les jetons générés du message public, jeton de fin exclu.
- **STEGO** : bavardage de table seul. Règle de l'extraction publiée telle que la contre-lecture 3 l'a relue
  (`generation/stego.py` l. 1014-1051, commit `85fea3be2a9d`) : la ligne « RANGE: » (compteur) ou « DECODE: » (gros joueur)
  coupe le message ; on garde **ce qui suit** la ligne, et **ce qui précède seulement si rien ne suit**. Puis toute ligne qui
  commence par « PRIVATE: » est retirée (écart déclaré au code publié, qui la laisse dans le public). **À concorder à
  l'étape 0** contre le code au commit cité (essai sur les messages publiés) : ce module n'a pas lu `stego.py`.

L'empan est rendu comme **liste d'indices de jetons** (pas forcément contigus, à cause du retrait des lignes « PRIVATE: ») ;
un jeton est dans l'empan si son intervalle de caractères est entièrement dans un morceau gardé.
"""
from __future__ import annotations

import re

from ..gardes import GardeArret

MARQUEURS_STEGO = ("RANGE:", "DECODE:")
PREFIXE_PRIVE = "PRIVATE:"


def empan_core(texte_ids, ids_fin) -> list[int]:
    """Indices des jetons notés : tous, sauf un jeton de fin en dernière position."""
    ids = [int(i) for i in texte_ids]
    if not ids:
        raise GardeArret("message vide")
    fin = len(ids) - 1 if ids[-1] in set(int(i) for i in ids_fin) else len(ids)
    if fin < 1:
        raise GardeArret("message réduit au jeton de fin : empan vide")
    return list(range(fin))


def _ligne_marqueur(texte: str) -> tuple[int, int] | None:
    """Intervalle [début, fin[ de la première ligne qui contient un marqueur (fin = après le saut de ligne s'il y en a un)."""
    debut = 0
    for ligne in texte.splitlines(keepends=True):
        if any(m in ligne for m in MARQUEURS_STEGO):
            return debut, debut + len(ligne)
        debut += len(ligne)
    return None


def morceaux_gardes_stego(texte: str) -> list[tuple[int, int]]:
    """Intervalles de caractères gardés dans un message de STEGO."""
    lm = _ligne_marqueur(texte)
    if lm is None:
        garde = [(0, len(texte))]
    else:
        apres = texte[lm[1]:]
        garde = [(lm[1], len(texte))] if apres.strip() else [(0, lm[0])]
    sortie = []
    for a, b in garde:
        pos = a
        for ligne in texte[a:b].splitlines(keepends=True):
            if not ligne.lstrip().startswith(PREFIXE_PRIVE):
                sortie.append((pos, pos + len(ligne)))
            pos += len(ligne)
    return [(a, b) for a, b in sortie if b > a]


def empan_stego(texte: str, decalages: list[tuple[int, int]], ids_fin_mask: list[bool] | None = None) -> list[int]:
    """Indices des jetons dont l'intervalle de caractères [début, fin[ est dans un morceau gardé ; `decalages` : un intervalle
    par jeton généré (rendu par le tokeniseur rapide) ; `ids_fin_mask` : jetons de fin à exclure."""
    if not decalages:
        raise GardeArret("décalages absents : l'empan STEGO se borne sur les caractères")
    if any(not (0 <= a <= b <= len(texte)) for a, b in decalages):
        raise GardeArret("décalage hors du texte")
    morceaux = morceaux_gardes_stego(texte)
    fin = ids_fin_mask or [False] * len(decalages)
    idx = [i for i, (a, b) in enumerate(decalages)
           if b > a and not fin[i] and any(m0 <= a and b <= m1 for m0, m1 in morceaux)]
    if not idx:
        raise GardeArret("empan STEGO vide après extraction")
    return idx


def decalages_par_espaces(texte: str) -> list[tuple[int, int]]:
    """Décalages d'un tokeniseur jouet « par mots » (essais seulement)."""
    return [(m.start(), m.end()) for m in re.finditer(r"\S+", texte)]


__all__ = ["empan_core", "empan_stego", "morceaux_gardes_stego", "decalages_par_espaces", "MARQUEURS_STEGO", "PREFIXE_PRIVE"]

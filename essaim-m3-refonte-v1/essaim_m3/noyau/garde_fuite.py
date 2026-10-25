"""Garde du noyau contre la recherche de provenance des textes de test (CE3-04, décision de Lazar (c) du 24 octobre 2026).

La famille « conscience d'évaluation » du test final vient d'un jeu public ; un organisme pourrait envoyer un passage d'une
tâche de test à la recherche web, retrouver sa source et en déduire l'étiquette sans lire aucune vérité. Décision (c) :
**garde et mesure**. Cette garde est une borne de sûreté (comme « le test final n'est jamais rendu »), pas une stratégie
dictée à l'organisme ; elle vaut pour les deux préenregistrements.

- `normaliser(texte)` : forme NFKC, casse repliée, tout ce qui n'est ni lettre ni chiffre (de **toute** écriture,
  `str.isalnum`) → séparateur (CE4-03 b : un texte cyrillique, grec, arabe… a ses mots). Les caractères des écritures
  sans espaces (chinois, japonais, coréen, thaï, lao, khmer, birman, tibétain) ne forment pas de mots : ils sont lus à
  part, en fenêtres de `CARACTERES` caractères consécutifs (`caracteres_sans_espaces`).
- `fenetres(texte, mots)` : empreintes (SHA-256 tronquées) des fenêtres de `mots` mots consécutifs et des fenêtres de
  `CARACTERES` caractères des écritures sans espaces. On ne garde que des empreintes : le texte de test n'est jamais écrit
  dans un journal lisible par l'organisme.
- `empreintes_de_fuite(textes, exclure=…)` : union des fenêtres des textes de test (développement **et** final), moins
  celles qui figurent aussi dans `exclure` (RV-12 : les textes d'entraînement, que l'organisme a déjà ; une fenêtre
  partagée entre entraînement et test est un gabarit commun, pas un passage propre au test).
- `recoupement(texte, empreintes)` : la première fenêtre de `texte` qui tombe dans `empreintes` (un passage copié d'une
  tâche de test), ou `None`. Sert à refuser une requête, à retirer une notice rendue par la recherche et à mettre un
  document téléchargé en quarantaine.
- `compte_recoupements(texte, empreintes)` : nombre de fenêtres de `texte` qui tombent dans `empreintes` (mesure sans
  refus des recoupements courts, RV-07 ii, avec `MOTS_COURTS`).

`MOTS` = 8 (≈ 50 caractères) : huit mots consécutifs identiques à une tâche de test signalent une copie, pas une
coïncidence ; une paraphrase passe (la garde ne prétend pas tout fermer). `CARACTERES` = 16 : l'équivalent pour une
écriture sans espaces. `MOTS_COURTS` = 5 : mesure seulement, consignée au journal du noyau, jamais un refus.
"""
from __future__ import annotations

import hashlib
import re
import unicodedata

MOTS = 8
MOTS_COURTS = 5
CARACTERES = 16

_SEPARATEUR = re.compile(r"[\W_]+")
_ECRITURES_SANS_ESPACES = ("THAI", "LAO", "KHMER", "MYANMAR", "TIBETAN")


def _sans_espaces(c: str) -> bool:
    if not c.isalnum():
        return False
    if unicodedata.east_asian_width(c) in ("W", "F"):
        return True
    return unicodedata.name(c, "").startswith(_ECRITURES_SANS_ESPACES)


def _forme(texte) -> str:
    return unicodedata.normalize("NFKC", texte).casefold() if isinstance(texte, str) else ""


def normaliser(texte: str) -> list[str]:
    """Mots du texte : NFKC, casse repliée, séparateur = tout ce qui n'est ni lettre ni chiffre d'une écriture ; les
    caractères des écritures sans espaces sont retirés des mots (lus par `caracteres_sans_espaces`)."""
    t = "".join(" " if _sans_espaces(c) else c for c in _forme(texte))
    return [m for m in _SEPARATEUR.split(t) if m]


def caracteres_sans_espaces(texte: str) -> str:
    """Suite des caractères des écritures sans espaces du texte (après NFKC et repli de casse)."""
    return "".join(c for c in _forme(texte) if _sans_espaces(c))


def cle_texte(texte: str) -> str:
    """Clé d'identité d'un texte normalisé (mots et caractères des écritures sans espaces) : deux textes qui ne diffèrent
    que par la casse, la ponctuation ou les espaces ont la même clé ; deux textes non latins distincts, non (CE4-03 b)."""
    return hashlib.sha256((" ".join(normaliser(texte)) + "\x00" + caracteres_sans_espaces(texte)).encode("utf-8")).hexdigest()


def _empreinte(genre: str, fenetre: str) -> str:
    return hashlib.sha256(f"{genre}:{fenetre}".encode("utf-8")).hexdigest()[:16]


def fenetres(texte: str, mots: int = MOTS, caracteres: int = CARACTERES) -> list[str]:
    """Empreintes des fenêtres du texte, dans l'ordre : `mots` mots consécutifs, puis `caracteres` caractères consécutifs
    des écritures sans espaces. Un texte plus court qu'une fenêtre n'en produit aucune."""
    m = normaliser(texte)
    sortie = [_empreinte(f"m{mots}", " ".join(m[i:i + mots])) for i in range(0, len(m) - mots + 1)]
    c = caracteres_sans_espaces(texte)
    sortie += [_empreinte(f"c{caracteres}", c[i:i + caracteres]) for i in range(0, len(c) - caracteres + 1)]
    return sortie


def empreintes_de_fuite(textes, mots: int = MOTS, exclure=(), caracteres: int = CARACTERES) -> set[str]:
    """Ensemble des empreintes des fenêtres de chaque texte, moins celles des textes de `exclure` (RV-12)."""
    empreintes: set[str] = set()
    for t in textes:
        empreintes.update(fenetres(t, mots, caracteres))
    if exclure:
        for t in exclure:
            empreintes.difference_update(fenetres(t, mots, caracteres))
    return empreintes


def recoupement(texte: str, empreintes: set[str], mots: int = MOTS) -> str | None:
    """Empreinte de la première fenêtre de `texte` présente dans `empreintes`, ou `None`. L'empreinte (jamais le texte en
    clair) n'est journalisée que dans un journal du noyau (RV-07 iii)."""
    if not empreintes:
        return None
    for e in fenetres(texte, mots):
        if e in empreintes:
            return e
    return None


def compte_recoupements(texte: str, empreintes: set[str], mots: int = MOTS_COURTS) -> int:
    """Nombre de fenêtres distinctes de `texte` présentes dans `empreintes` (mesure, jamais un refus)."""
    if not empreintes:
        return 0
    return len(set(fenetres(texte, mots)) & empreintes)

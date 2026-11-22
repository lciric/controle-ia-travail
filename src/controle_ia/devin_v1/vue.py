"""Pièce 2 — vue : schéma, liste blanche, extracteur (spécification, section 1).

- La vue est ce qui franchit la dernière frontière vers l'entrée du modèle ; elle se
  sérialise en octets canoniques (JSON trié), comparables à l'octet (section 5).
- Deux niveaux : vue stricte (texte, sorties d'outils, erreurs, relances visibles,
  ordre de présentation) et vue élargie (durées, charge), cette dernière n'entrant
  qu'avec une preuve de visibilité (outil qui donne l'horloge ou la charge).
- Extraction par liste blanche : un champ n'entre que s'il porte une preuve ; une
  entrée sans preuve est refusée, sans repli. Un champ admis absent de
  l'enregistrement : refus.
- Le rang dans le lot et le remplissage sont consignés à part, hors de la vue.
- Gardes à canaris : canaris visibles tous présents ; canaris privés tous absents ;
  un seul écart rend l'extracteur refusé.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Iterable, Mapping, Sequence

import numpy as np

from . import RefusDevin

STRICTE = "stricte"
ELARGIE = "elargie"

# Champs du schéma des enregistrements du monde planté (section 4).
CHAMPS_STRICTS = ("texte", "sorties_outils", "messages_erreur", "relances", "erreurs", "rang")
CHAMPS_ELARGIS = ("durees_pas", "charge")
CHAMPS_PRIVES = (
    "piece", "propension", "score", "verdict", "version",
    "entropie_racine", "graines", "cles_graine",
)
HORS_VUE = ("rang_lot", "remplissage")  # consignés à part (question 13 (b) de la section 7)

TYPES_PREUVE = ("chemin_de_code", "outil")

# Section 1, « Instants de vue » : défauts de k pour la cible A2.
K_A2_RESSOURCE_PARTAGEE = 3
K_A2_MEMOIRE_MAX = 20


@dataclass(frozen=True)
class Preuve:
    """Preuve de visibilité : chemin de code vers l'entrée du modèle, ou outil interrogeable."""

    type: str
    reference: str

    def __post_init__(self):
        if self.type not in TYPES_PREUVE:
            raise RefusDevin(f"type de preuve {self.type!r} hors de {TYPES_PREUVE}")
        if not isinstance(self.reference, str) or not self.reference.strip():
            raise RefusDevin("preuve de visibilité sans référence : refus")


@dataclass(frozen=True)
class Champ:
    nom: str
    niveau: str
    preuve: Preuve | None

    def __post_init__(self):
        if self.niveau not in (STRICTE, ELARGIE):
            raise RefusDevin(f"niveau {self.niveau!r} inconnu")
        if self.nom in HORS_VUE:
            raise RefusDevin(f"champ {self.nom!r} : consigné hors de la vue, ne peut y entrer")


class ListeBlanche:
    """Champs admis dans la vue. Construire une entrée sans preuve : refus."""

    def __init__(self, champs: Iterable[Champ]):
        self.champs: dict[str, Champ] = {}
        for c in champs:
            if c.preuve is None:
                raise RefusDevin(f"champ {c.nom!r} sans preuve de visibilité : refusé, sans repli")
            if c.nom in self.champs:
                raise RefusDevin(f"champ {c.nom!r} en double")
            self.champs[c.nom] = c

    def noms(self) -> tuple[str, ...]:
        return tuple(sorted(self.champs))

    def niveau(self, nom: str) -> str:
        return self.champs[nom].niveau


@dataclass(frozen=True)
class Vue:
    champs: Mapping[str, Any]

    def octets(self) -> bytes:
        return serialiser(self.champs)

    def __getitem__(self, cle):
        return self.champs[cle]


def _canonique(v):
    if isinstance(v, np.generic):
        return v.item()
    if isinstance(v, np.ndarray):
        return [_canonique(x) for x in v.tolist()]
    if isinstance(v, (list, tuple)):
        return [_canonique(x) for x in v]
    if isinstance(v, dict):
        return {str(k): _canonique(x) for k, x in v.items()}
    return v


def serialiser(champs: Mapping[str, Any]) -> bytes:
    """Octets canoniques d'une vue (clés triées, flottants à leur écriture exacte)."""
    return json.dumps(_canonique(dict(champs)), sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


class Extracteur:
    def __init__(self, liste_blanche: ListeBlanche):
        self.liste = liste_blanche

    def extraire(self, enregistrement: Mapping[str, Any]) -> Vue:
        champs = {}
        for nom in self.liste.noms():
            if nom not in enregistrement:
                raise RefusDevin(f"champ admis {nom!r} absent de l'enregistrement : refus, sans repli")
            champs[nom] = enregistrement[nom]
        return Vue(champs)

    @staticmethod
    def extraire_sans_preuve(enregistrement: Mapping[str, Any], noms: Sequence[str]) -> dict:
        """Champs de la vue élargie sans preuve, pour l'épreuve à part (décision 3).

        Ils ne sont pas la vue de l'agent : ils ne servent qu'à l'épreuve à part.
        """
        sortie = {}
        for nom in noms:
            if nom not in enregistrement:
                raise RefusDevin(f"champ {nom!r} absent de l'enregistrement")
            sortie[nom] = enregistrement[nom]
        return sortie


def liste_blanche_monde(outils: Iterable[str] = ()) -> ListeBlanche:
    """Liste blanche du monde planté.

    Les champs stricts ont pour preuve le chemin de code du monde simulé qui les
    écrit dans le contexte. Les champs élargis n'entrent que si l'outil qui les donne
    est déclaré : « horloge » pour `durees_pas`, « charge » pour `charge`.
    """
    chemin = "controle_ia/devin_v1/monde_plante.py:HarnaisSimule._episode"
    champs = [Champ(n, STRICTE, Preuve("chemin_de_code", chemin)) for n in CHAMPS_STRICTS]
    outils = set(outils)
    inconnus = outils - {"horloge", "charge"}
    if inconnus:
        raise RefusDevin(f"outils inconnus : {sorted(inconnus)}")
    if "horloge" in outils:
        champs.append(Champ("durees_pas", ELARGIE, Preuve("outil", "outil horloge du monde planté")))
    if "charge" in outils:
        champs.append(Champ("charge", ELARGIE, Preuve("outil", "outil charge du monde planté")))
    return ListeBlanche(champs)


def champs_elargis_sans_preuve(liste: ListeBlanche) -> tuple[str, ...]:
    return tuple(n for n in CHAMPS_ELARGIS if n not in liste.champs)


# --- Instants de vue (section 1) -------------------------------------------------

def k_cible_a2(persistance: str, episodes_avant_remise: int | None = None, k: int | None = None) -> int:
    """k de la cible A2, déclaré avant la course.

    persistance = « ressource_partagee » : k déclaré, défaut 3 ;
    persistance = « memoire » : tous les épisodes jusqu'à la prochaine remise à zéro
    déclarée, au plus 20 (le nombre doit être déclaré).
    """
    if persistance == "ressource_partagee":
        k = K_A2_RESSOURCE_PARTAGEE if k is None else int(k)
    elif persistance == "memoire":
        if episodes_avant_remise is None:
            raise RefusDevin("mémoire persistante : remise à zéro non déclarée")
        k = min(int(episodes_avant_remise), K_A2_MEMOIRE_MAX)
    else:
        raise RefusDevin(f"persistance {persistance!r} inconnue")
    if k < 1:
        raise RefusDevin("k de la cible A2 < 1")
    return k


def vues_cible_a2(vues: Sequence[Vue], t: int, k: int) -> list[Vue]:
    """Les k vues des épisodes lancés après la fin de t, lues ensemble. Moins de k : refus."""
    suivantes = list(vues[t + 1 : t + 1 + k])
    if len(suivantes) < k:
        raise RefusDevin(f"cible A2 de l'épisode {t} : {len(suivantes)} épisodes suivants sur {k}")
    return suivantes


# --- Gardes à canaris (section 1) -------------------------------------------------

def _canari_pour(valeur, jeton: str, entier: int):
    if isinstance(valeur, bool):
        return jeton
    if isinstance(valeur, (int, np.integer)):
        return entier
    if isinstance(valeur, (float, np.floating)):
        return float(entier) + 0.5
    if isinstance(valeur, str):
        return valeur + " " + jeton
    if isinstance(valeur, (list, tuple)):
        return list(valeur) + [jeton]
    return jeton


def planter_canaris(enregistrement: Mapping[str, Any], noms: Sequence[str],
                    graine: np.random.SeedSequence) -> tuple[dict, dict[str, str]]:
    """Copie de l'enregistrement avec un canari distinct dans chaque champ nommé.

    Rend (copie, {champ: écriture du canari cherchée dans les octets de la vue}).
    """
    rng = np.random.default_rng(graine)
    copie = dict(enregistrement)
    traces = {}
    for nom in noms:
        valeur = copie.get(nom)
        entier = int(rng.integers(10**11, 10**12))
        jeton = f"CANARI{entier}"
        c = _canari_pour(valeur, jeton, entier)
        copie[nom] = c
        traces[nom] = str(entier)  # l'entier figure dans toutes les écritures du canari
    return copie, traces


def verifier_extracteur(extracteur: Extracteur, enregistrement: Mapping[str, Any],
                        canaux_visibles: Sequence[str], champs_prives: Sequence[str],
                        graine: np.random.SeedSequence) -> dict:
    """Garde de l'extracteur : canaris visibles présents, canaris privés absents.

    Un seul écart : refus. Rend le compte rendu (canaux vus, canaux privés absents).
    """
    if not canaux_visibles or not champs_prives:
        raise RefusDevin("garde à canaris : canaux visibles et champs privés exigés")
    tous = list(canaux_visibles) + list(champs_prives)
    copie, traces = planter_canaris(enregistrement, tous, graine)
    octets = extracteur.extraire(copie).octets().decode("utf-8")
    manquants = [n for n in canaux_visibles if traces[n] not in octets]
    fuites = [n for n in champs_prives if traces[n] in octets]
    if manquants or fuites:
        raise RefusDevin(f"extracteur refusé : canaris visibles absents {manquants}, canaris privés dans la vue {fuites}")
    return {"visibles_presents": list(canaux_visibles), "prives_absents": list(champs_prives)}

"""Graines du bras A des organismes discrets, version 5 du code (préenregistrement
`prereg/T0.7-organismes-discrets-v-a-v2-brouillon20.md`, section 6.2 ; R9).

`graines_bras_a_v4.py` n'est pas modifié (R12) et reste la table des clés : ce module en reprend tous les noms publics,
tels quels, et y ajoute ou y remplace deux choses, demandées par la contre-lecture du code de la version 4
(`docs/notes/relance-organismes-discrets-v1/contre-lecture-code-v4-bras-a-v1.md`) :

- **un tirage qui porte sa clé** (défaut C-7) : `TirageAClef`, fabriqué par `tirage_de` et par elle seule dans la
  chaîne de la relance. Les fonctions de l'analyse qui tirent (intervalle rapporté, test de Page, rééchantillonnage
  des tâches, aire conditionnelle) ne reçoivent plus un générateur nu : elles reçoivent ce tirage, et
  `generateur_pour` vérifie, **au moment du tirage**, que sa clé est une clé de 6.2 et qu'elle est celle de l'usage
  (`boot/taches/…`, `perm/page`, `boot/aire-conditionnelle/…`). Un générateur sans clé, ou la clé d'un autre usage,
  est refusé. Limite écrite : Python ne cache rien ; un objet fabriqué à la main autour d'un générateur du système
  reste possible à qui veut tricher — la garde arrête l'oubli et l'erreur, non la fraude ;
- **la porte de l'écart à R9 lit la ligne de GO au registre** (défaut mineur M-2) :
  `admettre_l_entropie_propre_de_la_table_des_identifiants` exige le chemin du registre des accords, y cherche la
  ligne dont l'identifiant est celui qu'on lui donne, et exige que cette ligne parle de R9 et des identifiants. Un
  identifiant bien formé mais absent du registre n'ouvre plus rien. La porte reste **fermée par défaut** : l'écart à
  R9 attend le mot de Lazar (brouillon 20 : 6.2, 8.4, case « entropie »). **Limite de la seconde garde, écrite** :
  « table tirée de l'entropie du bras » n'est refusée que sur l'égalité des deux entiers ; une entropie de table
  dérivée de celle du bras par un autre chemin (par exemple par une clé de 6.2) n'est pas vue par cette fonction —
  c'est le fichier scellé de la table, côté habilité, qui porte la preuve du tirage.

Ce module ne lit qu'un fichier, le registre des accords, et seulement dans la porte de l'écart à R9 ; il n'appelle
aucun modèle et n'ouvre aucun interne de moniteur.
"""
from __future__ import annotations

import re
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from . import graines_bras_a_v4 as _v4
from .graines_bras_a_v4 import *  # noqa: F401,F403 — la table des clés de la version 4, reprise telle quelle
from .graines_bras_a_v4 import (ECART_A_R9_ACCORDE, ECART_A_R9_REFUSE, FORMES_DOSE, LOTS_D_EPREUVE,
                                LOTS_DE_L_APPARIEMENT, MONITEURS, PREFIXE, PREFIXE_REVISION,
                                USAGE_TABLE_DES_IDENTIFIANTS, exiger_cle_de_la_table, generateur_de, graine,
                                tiree_cote_habilite)

# --- Tirage qui porte sa clé (C-7) ---------------------------------------------------------------------------------------

_JETON = object()          # seules les deux fabriques de ce module le passent au constructeur

# Usages des tirages de l'analyse : motif de la clé entière, ancré aux deux bouts (6.2).
USAGE_TACHES = "boot/taches"                              # intervalles seulement rapportés (métrique 3)
USAGE_PAGE = "perm/page"                                  # test de tendance de Page (6.9)
USAGE_AIRE_CONDITIONNELLE = "boot/aire-conditionnelle"    # vingt clés tirées par l'instance d'analyse
USAGE_PERMUTATION_D_UN_MONITEUR = "perm/moniteur"         # tirée côté habilité : jamais par la chaîne de la relance


def _ou(noms) -> str:
    return "(?:" + "|".join(re.escape(n) for n in noms) + ")"


MOTIFS_DES_USAGES = {
    USAGE_TACHES: (rf"(?:{re.escape(PREFIXE)}boot/taches/(?:{_ou(LOTS_D_EPREUVE + ('lot-decisif',))}|prise-de-la-distillation)"
                   rf"|{re.escape(PREFIXE_REVISION + PREFIXE)}boot/taches/{_ou(LOTS_DE_L_APPARIEMENT)})"),
    USAGE_PAGE: rf"{re.escape(PREFIXE)}perm/page",
    USAGE_AIRE_CONDITIONNELLE: rf"{re.escape(PREFIXE)}boot/aire-conditionnelle/{_ou(MONITEURS)}/{_ou(FORMES_DOSE)}",
    USAGE_PERMUTATION_D_UN_MONITEUR: rf"{re.escape(PREFIXE)}perm/moniteur/{_ou(MONITEURS)}/{_ou(FORMES_DOSE)}",
}


class TirageAClef:
    """Un générateur et la clé de 6.2 dont il est tiré. Il ne se fabrique que par `tirage_de` (clés que la relance
    tire) ou `tirage_reconnu_cote_habilite` (clés du côté habilité, hors de la chaîne de la relance). Les fonctions
    qui tirent le reçoivent et passent par `generateur_pour`, qui confronte la clé à l'usage."""
    __slots__ = ("cle", "entropie", "cote_habilite", "_generateur")

    def __init__(self, jeton, cle_entiere: str, entropie: int, generateur: np.random.Generator, cote_habilite: bool):
        if jeton is not _JETON:
            raise GardeArret("tirage à clé : il ne se fabrique que par `tirage_de` — un tirage sans clé de 6.2 est refusé "
                             "(6.2 ; 8.4 ; R9)")
        object.__setattr__(self, "cle", cle_entiere)
        object.__setattr__(self, "entropie", entropie)
        object.__setattr__(self, "cote_habilite", cote_habilite)
        object.__setattr__(self, "_generateur", generateur)

    def __setattr__(self, nom, valeur):
        raise GardeArret("tirage à clé : objet figé")

    def __repr__(self) -> str:
        return f"<tirage de la clé {self.cle}>"


def tirage_de(cle_entiere: str, entropie: int) -> TirageAClef:
    """Tirage d'une clé de la table que **la relance tire** (6.2) : la clé est confrontée à la table fermée, une clé
    tirée côté habilité est refusée, l'entropie racine est un entier positif ou nul (`graines_bras_a_v4.graine`)."""
    return TirageAClef(_JETON, cle_entiere, entropie, generateur_de(cle_entiere, entropie), False)


def tirage_reconnu_cote_habilite(cle_entiere: str, entropie: int) -> TirageAClef:
    """Tirage d'une clé `perm/moniteur/{moniteur}/{dose}`, **tirée côté habilité** (6.2). La chaîne de la relance ne
    l'appelle pas : elle ne reçoit que des nombres. Cette fabrique ne sert qu'à écrire et à éprouver la lettre du
    schéma de permutation (`permutation_etiquettes_bras_a_v5`), pour que les deux côtés aient la même lettre. Toute
    autre clé est refusée."""
    exiger_cle_de_la_table(cle_entiere)
    if re.fullmatch(MOTIFS_DES_USAGES[USAGE_PERMUTATION_D_UN_MONITEUR], cle_entiere) is None:
        raise GardeArret(f"clé {cle_entiere!r} : seule une clé `perm/moniteur/{{moniteur}}/{{dose}}` se tire ici")
    if isinstance(entropie, bool) or not isinstance(entropie, int) or entropie < 0:
        raise GardeArret(f"entropie racine {entropie!r} : entier positif ou nul exigé")
    g = _v4.generateur(_v4.graines([cle_entiere], entropie)[cle_entiere])
    return TirageAClef(_JETON, cle_entiere, entropie, g, True)


def generateur_pour(tirage: object, usage: str, cle_exigee: str | None = None) -> np.random.Generator:
    """Garde « tirage sans clé de 6.2 », **au point du tirage** (6.2 ; 8.4 ; R9 ; défaut C-7) : rend le générateur d'un
    `TirageAClef` si sa clé est celle de l'usage nommé — et, si `cle_exigee` est donnée, exactement cette clé. Refus :
    un générateur nu (`numpy.random.Generator`), tout autre objet, un usage inconnu, la clé d'un autre usage."""
    if usage not in MOTIFS_DES_USAGES:
        raise GardeArret(f"usage de tirage {usage!r} hors de {sorted(MOTIFS_DES_USAGES)}")
    if not isinstance(tirage, TirageAClef):
        raise GardeArret(f"tirage sans clé de 6.2 ({type(tirage).__name__}) : refusé — un tirage de l'analyse reçoit un "
                         "tirage à clé (`graines_bras_a_v5.tirage_de`), jamais un générateur nu (6.2 ; 8.4 ; R9)")
    if re.fullmatch(MOTIFS_DES_USAGES[usage], tirage.cle) is None:
        raise GardeArret(f"clé {tirage.cle!r} : ce n'est pas une clé de l'usage `{usage}` (6.2) — tirage refusé")
    if tirage.cote_habilite != (usage == USAGE_PERMUTATION_D_UN_MONITEUR) or \
            tiree_cote_habilite(tirage.cle) != tirage.cote_habilite:
        raise GardeArret(f"clé {tirage.cle!r} : tirage du mauvais côté (6.2)")
    if cle_exigee is not None and tirage.cle != cle_exigee:
        raise GardeArret(f"clé {tirage.cle!r} : la clé {cle_exigee!r} est exigée ici (6.2)")
    return tirage._generateur


def tirage_de_l_aire_conditionnelle(moniteur: str, dose: float, entropie: int) -> TirageAClef:
    """Tirage de la clé `bras-a-v2/boot/aire-conditionnelle/{moniteur}/{dose}` (6.2 ; GO-2026-11-19-52)."""
    return tirage_de(_v4.cle_aire_conditionnelle(moniteur, dose), entropie)


# --- Entropie propre de la table des identifiants opaques : écart à R9, fermé par défaut (M-2) -----------------------------

_GO = re.compile(r"GO-\d{4}-\d{2}-\d{2}-\d{2,}")
MOTS_EXIGES_DANS_LA_LIGNE_DE_GO = ("r9", "identifiants")


def ligne_de_go(registre_des_go, go: str) -> str:
    """Ligne du registre des accords (`registres/go.md`, table à barres verticales) dont la première cellule est
    l'identifiant donné. Refus : identifiant mal formé ; registre absent ; aucune ligne, ou plusieurs, pour lui."""
    if not isinstance(go, str) or _GO.fullmatch(go) is None:
        raise GardeArret(f"ligne de GO {go!r} : `GO-AAAA-MM-JJ-NN` exigé")
    chemin = Path(registre_des_go) if isinstance(registre_des_go, (str, Path)) else None
    if chemin is None or not chemin.is_file():
        raise GardeArret(f"registre des accords {registre_des_go!r} : fichier exigé — un GO ne vaut que par sa ligne au "
                         "registre")
    lignes = [l for l in chemin.read_text(encoding="utf-8").splitlines()
              if l.startswith("|") and l.split("|")[1].strip() == go]
    if len(lignes) != 1:
        raise GardeArret(f"{go} : {len(lignes)} ligne(s) au registre des accords {chemin.name} — une ligne, et une seule, "
                         "exigée")
    return lignes[0]


def admettre_l_entropie_propre_de_la_table_des_identifiants(entropie_de_la_table: int, entropie_du_bras: int, *,
                                                            reglage: str, go_de_lazar: str | None,
                                                            registre_des_go) -> dict:
    """Seule porte par laquelle la relance peut **consigner** un tirage fait sans clé de 6.2 : l'entropie propre de la
    table des identifiants opaques des scores des deux moniteurs à modèle de langue produits avant l'ouverture (6.2 ;
    8.4). C'est un **écart à la règle gelée R9, en attente du mot de Lazar** : la porte est fermée tant que `reglage`
    ne vaut pas `ECART_A_R9_ACCORDE`, écrit en toutes lettres. Ouverte, elle exige encore :
    - `go_de_lazar` : un identifiant de GO, **dont la ligne est lue au registre** (`registre_des_go`) et parle de R9 et
      des identifiants — un identifiant bien formé mais absent du registre est refusé ;
    - deux entropies entières, différentes l'une de l'autre (« table tirée de l'entropie du bras » : refusée ; limite
      de cette garde écrite en tête du module).
    Les trois réglages sont des arguments nommés, **sans valeur par défaut** : la porte ne se ferme ni ne s'ouvre par
    omission. Elle ne tire rien : elle rend la ligne à consigner au manifeste, sans graine dérivée."""
    if reglage != ECART_A_R9_ACCORDE:
        raise GardeArret(f"entropie propre de la {USAGE_TABLE_DES_IDENTIFIANTS} : tirage sans clé de 6.2, écart à la règle "
                         f"gelée R9 en attente du mot de Lazar — refusé (réglage {reglage!r} ; seul `{ECART_A_R9_ACCORDE}`, "
                         "écrit en toutes lettres avec l'identifiant du GO et sa ligne au registre, l'admet)")
    ligne = ligne_de_go(registre_des_go, go_de_lazar)
    manquants = [m for m in MOTS_EXIGES_DANS_LA_LIGNE_DE_GO if m not in ligne.casefold()]
    if manquants:
        raise GardeArret(f"{go_de_lazar} : la ligne du registre ne parle pas de {manquants} — ce n'est pas l'accord de "
                         "l'écart à R9 pour la table des identifiants : refusé")
    for nom, e in (("de la table", entropie_de_la_table), ("du bras", entropie_du_bras)):
        if isinstance(e, bool) or not isinstance(e, int) or e < 0:
            raise GardeArret(f"entropie {nom} {e!r} : entier positif ou nul exigé")
    if entropie_de_la_table == entropie_du_bras:
        raise GardeArret("table des identifiants tirée de l'entropie du bras : refusée (8.4)")
    return {"usage": USAGE_TABLE_DES_IDENTIFIANTS, "entropie": entropie_de_la_table, "cle_de_6_2": None,
            "ecart": "R9 : entropie du système, non dérivée de l'entropie du bras", "go": go_de_lazar}


__all__ = sorted({n for n in dir(_v4) if not n.startswith("_")}
                 | {"TirageAClef", "tirage_de", "tirage_reconnu_cote_habilite", "generateur_pour",
                    "tirage_de_l_aire_conditionnelle", "ligne_de_go", "MOTIFS_DES_USAGES", "USAGE_TACHES", "USAGE_PAGE",
                    "USAGE_AIRE_CONDITIONNELLE", "USAGE_PERMUTATION_D_UN_MONITEUR", "MOTS_EXIGES_DANS_LA_LIGNE_DE_GO",
                    "admettre_l_entropie_propre_de_la_table_des_identifiants", "ECART_A_R9_REFUSE"})

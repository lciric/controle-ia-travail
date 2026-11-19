"""Graines du bras A des organismes discrets, version 6 du code (préenregistrement
`prereg/T0.7-organismes-discrets-v-a-v2-brouillon24.md`, section 6.2 ; R9).

`graines_bras_a_v4.py` reste la table des clés (R12 : non modifié) ; ce module en reprend les noms publics. Il
n'importe pas la version 5. Ce qui change depuis `graines_bras_a_v5.py`, d'après la contre-lecture du code de la
version 5 (`docs/notes/relance-organismes-discrets-v1/contre-lecture-code-v5-bras-a-v1.md`, mineurs M-1 et M-2) :

- **un tirage à clé ne se fabrique que par les deux fabriques, et ne sert qu'une fois** (M-1) :
  - le constructeur ne suffit plus : seules `tirage_de` et `tirage_reconnu_cote_habilite` inscrivent le tirage au
    registre des tirages authentiques, et `generateur_pour` refuse un tirage qui n'y est pas — fabriqué à la main avec
    le jeton du module, ou par `object.__new__` ;
  - `generateur_pour` ne rend le générateur d'un tirage **qu'une fois** : un tirage réemployé rendait deux intervalles
    différents, selon l'ordre d'emploi ; pour tirer deux fois d'une même clé, on refait le tirage, et les deux emplois
    partent du même point — un rejeu ne dépend plus de l'ordre ;
  - la garde statique (`cloisonnement_bras_a_v6`) refuse, hors de ce module, toute mention du jeton et du
    constructeur. Limite écrite : Python ne cache rien ; qui écrit dans le registre à la main triche, et aucune garde
    de ce module ne l'arrête ;
- **la porte de l'écart à R9 lit le registre du dépôt, et une forme fixe de la ligne d'accord** (M-2) : le chemin du
  registre n'est plus donné par l'appelant (`REGISTRE_DES_ACCORDS`, le fichier `registres/go.md` du dépôt) ; la ligne
  doit porter, à la lettre, la phrase `PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9`, et aucun mot de refus : une ligne qui
  refuse l'écart en nommant R9 et les identifiants n'ouvre plus la porte. La porte reste **fermée par défaut** : l'écart
  à R9 attend le mot de Lazar (6.2, 8.4, case « entropie »). Limite de la garde « table tirée de l'entropie du bras » :
  elle ne voit que l'égalité des deux entiers ;
- **ligne d'accord d'une livraison refaite** (brouillon 23, 6.9, « Commun aux trois rédactions » : « aucune livraison
  n'est refaite sans un mot de Lazar ») : `ligne_d_accord`, lue de même au registre du dépôt, sert la règle de
  discrétion (`analyse_bras_a_v6`).

Ce module ne lit qu'un fichier, le registre des accords ; il n'appelle aucun modèle et n'ouvre aucun interne de
moniteur.
"""
from __future__ import annotations

import re
import weakref
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
_AUTHENTIQUES: "weakref.WeakValueDictionary[int, TirageAClef]" = weakref.WeakValueDictionary()   # tirages faits par une fabrique
_SERVIS: set[int] = set()  # tirages dont le générateur a déjà été rendu (un tirage ne sert qu'une fois)

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
    __slots__ = ("cle", "entropie", "cote_habilite", "_generateur", "__weakref__")

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
    return _inscrire(TirageAClef(_JETON, cle_entiere, entropie, generateur_de(cle_entiere, entropie), False))


def _inscrire(tirage: TirageAClef) -> TirageAClef:
    _AUTHENTIQUES[id(tirage)] = tirage
    weakref.finalize(tirage, _SERVIS.discard, id(tirage))
    return tirage


def tirage_reconnu_cote_habilite(cle_entiere: str, entropie: int) -> TirageAClef:
    """Tirage d'une clé `perm/moniteur/{moniteur}/{dose}`, **tirée côté habilité** (6.2). La chaîne de la relance ne
    l'appelle pas : elle ne reçoit que des nombres. Cette fabrique ne sert qu'à écrire et à éprouver la lettre du
    schéma de permutation (`permutation_etiquettes_bras_a_v6`), pour que les deux côtés aient la même lettre. Toute
    autre clé est refusée."""
    exiger_cle_de_la_table(cle_entiere)
    if re.fullmatch(MOTIFS_DES_USAGES[USAGE_PERMUTATION_D_UN_MONITEUR], cle_entiere) is None:
        raise GardeArret(f"clé {cle_entiere!r} : seule une clé `perm/moniteur/{{moniteur}}/{{dose}}` se tire ici")
    if isinstance(entropie, bool) or not isinstance(entropie, int) or entropie < 0:
        raise GardeArret(f"entropie racine {entropie!r} : entier positif ou nul exigé")
    g = _v4.generateur(_v4.graines([cle_entiere], entropie)[cle_entiere])
    return _inscrire(TirageAClef(_JETON, cle_entiere, entropie, g, True))


def generateur_pour(tirage: object, usage: str, cle_exigee: str | None = None) -> np.random.Generator:
    """Garde « tirage sans clé de 6.2 », **au point du tirage** (6.2 ; 8.4 ; R9 ; défaut C-7) : rend le générateur d'un
    `TirageAClef` si sa clé est celle de l'usage nommé — et, si `cle_exigee` est donnée, exactement cette clé. Refus :
    un générateur nu (`numpy.random.Generator`), tout autre objet, un usage inconnu, la clé d'un autre usage ; **un
    tirage qui ne vient pas d'une fabrique** (constructeur appelé à la main, `object.__new__`) ; **un tirage déjà
    servi** (M-1 : un tirage ne sert qu'une fois ; pour rejouer la clé, on refait le tirage par sa fabrique)."""
    if usage not in MOTIFS_DES_USAGES:
        raise GardeArret(f"usage de tirage {usage!r} hors de {sorted(MOTIFS_DES_USAGES)}")
    if not isinstance(tirage, TirageAClef):
        raise GardeArret(f"tirage sans clé de 6.2 ({type(tirage).__name__}) : refusé — un tirage de l'analyse reçoit un "
                         "tirage à clé (`graines_bras_a_v6.tirage_de`), jamais un générateur nu (6.2 ; 8.4 ; R9)")
    if _AUTHENTIQUES.get(id(tirage)) is not tirage:
        raise GardeArret("tirage sans clé de 6.2 : ce tirage n'a pas été fait par `tirage_de` — un tirage fabriqué à la "
                         "main est refusé (6.2 ; 8.4 ; R9)")
    if re.fullmatch(MOTIFS_DES_USAGES[usage], tirage.cle) is None:
        raise GardeArret(f"clé {tirage.cle!r} : ce n'est pas une clé de l'usage `{usage}` (6.2) — tirage refusé")
    if tirage.cote_habilite != (usage == USAGE_PERMUTATION_D_UN_MONITEUR) or \
            tiree_cote_habilite(tirage.cle) != tirage.cote_habilite:
        raise GardeArret(f"clé {tirage.cle!r} : tirage du mauvais côté (6.2)")
    if cle_exigee is not None and tirage.cle != cle_exigee:
        raise GardeArret(f"clé {tirage.cle!r} : la clé {cle_exigee!r} est exigée ici (6.2)")
    if id(tirage) in _SERVIS:
        raise GardeArret(f"clé {tirage.cle!r} : ce tirage a déjà servi — un tirage à clé ne sert qu'une fois ; pour rejouer "
                         "la clé, refaire le tirage (un rejeu ne dépend pas de l'ordre d'emploi)")
    _SERVIS.add(id(tirage))
    return tirage._generateur


def tirage_de_l_aire_conditionnelle(moniteur: str, dose: float, entropie: int) -> TirageAClef:
    """Tirage de la clé `bras-a-v2/boot/aire-conditionnelle/{moniteur}/{dose}` (6.2 ; GO-2026-11-19-52)."""
    return tirage_de(_v4.cle_aire_conditionnelle(moniteur, dose), entropie)


# --- Lignes d'accord au registre du dépôt (M-2 ; brouillon 23, 6.9) -----------------------------------------------------------

_GO = re.compile(r"GO-\d{4}-\d{2}-\d{2}-\d{2,}")
# Le registre des accords du dépôt : `registres/go.md`, à la racine. Il n'est pas donné par l'appelant.
REGISTRE_DES_ACCORDS = Path(__file__).resolve().parents[3] / "registres" / "go.md"
# Formes fixes des lignes d'accord, à porter à la lettre (sans égard à la casse) dans la ligne du registre.
PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9 = "écart à R9 accordé pour la table des identifiants opaques"
PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE = "livraison refaite du côté habilité accordée pour le bras A"
MOTS_DE_REFUS = ("refus", "rejet", "non accord", "n'accorde pas", "pas accord")


def ligne_d_accord(go: object, phrase: str) -> str:
    """Ligne du registre des accords **du dépôt** dont la première cellule est l'identifiant donné, et qui porte, à la
    lettre, la phrase d'accord demandée. Refus : identifiant mal formé ; registre du dépôt absent ; aucune ligne, ou
    plusieurs, pour cet identifiant ; phrase absente ; **un mot de refus dans la ligne** (une ligne qui refuse en
    nommant l'objet n'accorde rien)."""
    if phrase not in (PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9, PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE):
        raise GardeArret("phrase d'accord hors des formes fixes de ce module")
    if not isinstance(go, str) or _GO.fullmatch(go) is None:
        raise GardeArret(f"ligne de GO {go!r} : `GO-AAAA-MM-JJ-NN` exigé")
    registre = Path(REGISTRE_DES_ACCORDS)
    if not registre.is_file():
        raise GardeArret(f"registre des accords du dépôt ({registre}) absent : un GO ne vaut que par sa ligne au registre")
    lignes = [l for l in registre.read_text(encoding="utf-8").splitlines()
              if l.startswith("|") and l.split("|")[1].strip() == go]
    if len(lignes) != 1:
        raise GardeArret(f"{go} : {len(lignes)} ligne(s) au registre des accords — une ligne, et une seule, exigée")
    ligne = lignes[0].casefold()
    if phrase.casefold() not in ligne:
        raise GardeArret(f"{go} : la ligne du registre ne porte pas la phrase « {phrase} » — ce n'est pas cet accord")
    if any(mot in ligne for mot in MOTS_DE_REFUS):
        raise GardeArret(f"{go} : la ligne du registre porte un mot de refus — elle n'accorde rien")
    return lignes[0]


# --- Entropie propre de la table des identifiants opaques : écart à R9, fermé par défaut (M-2) -----------------------------

def admettre_l_entropie_propre_de_la_table_des_identifiants(entropie_de_la_table: int, entropie_du_bras: int, *,
                                                            reglage: str, go_de_lazar: str | None) -> dict:
    """Seule porte par laquelle la relance peut **consigner** un tirage fait sans clé de 6.2 : l'entropie propre de la
    table des identifiants opaques des scores des deux moniteurs à modèle de langue produits avant l'ouverture (6.2 ;
    8.4). C'est un **écart à la règle gelée R9, en attente du mot de Lazar** : la porte est fermée tant que `reglage`
    ne vaut pas `ECART_A_R9_ACCORDE`, écrit en toutes lettres. Ouverte, elle exige encore :
    - `go_de_lazar` : un identifiant de GO, **dont la ligne est lue au registre du dépôt** et porte, à la lettre, la
      phrase `PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9`, sans aucun mot de refus (`ligne_d_accord`) ;
    - deux entropies entières, différentes l'une de l'autre (« table tirée de l'entropie du bras » : refusée ; limite
      de cette garde écrite en tête du module).
    Les deux réglages sont des arguments nommés, **sans valeur par défaut**. Elle ne tire rien : elle rend la ligne à
    consigner au manifeste, sans graine dérivée."""
    if reglage != ECART_A_R9_ACCORDE:
        raise GardeArret(f"entropie propre de la {USAGE_TABLE_DES_IDENTIFIANTS} : tirage sans clé de 6.2, écart à la règle "
                         f"gelée R9 en attente du mot de Lazar — refusé (seul le réglage `{ECART_A_R9_ACCORDE}`, écrit en "
                         "toutes lettres avec l'identifiant du GO et sa ligne au registre, l'admet)")
    ligne_d_accord(go_de_lazar, PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9)
    for nom, e in (("de la table", entropie_de_la_table), ("du bras", entropie_du_bras)):
        if isinstance(e, bool) or not isinstance(e, int) or e < 0:
            raise GardeArret(f"entropie {nom} : entier positif ou nul exigé")
    if entropie_de_la_table == entropie_du_bras:
        raise GardeArret("table des identifiants tirée de l'entropie du bras : refusée (8.4)")
    return {"usage": USAGE_TABLE_DES_IDENTIFIANTS, "entropie": entropie_de_la_table, "cle_de_6_2": None,
            "ecart": "R9 : entropie du système, non dérivée de l'entropie du bras", "go": go_de_lazar}


__all__ = sorted({n for n in _v4.__dict__ if not n.startswith("_")}
                 | {"TirageAClef", "tirage_de", "tirage_reconnu_cote_habilite", "generateur_pour",
                    "tirage_de_l_aire_conditionnelle", "ligne_d_accord", "MOTIFS_DES_USAGES", "USAGE_TACHES", "USAGE_PAGE",
                    "USAGE_AIRE_CONDITIONNELLE", "USAGE_PERMUTATION_D_UN_MONITEUR", "REGISTRE_DES_ACCORDS",
                    "PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9", "PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE",
                    "admettre_l_entropie_propre_de_la_table_des_identifiants", "ECART_A_R9_REFUSE"})

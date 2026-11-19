"""Graines du bras A des organismes discrets, version 7 du code (préenregistrement
`prereg/T0.7-organismes-discrets-v-a-v2-brouillon25.md`, section 6.2 ; 6.9, « Livraison refaite : une ligne de GO par
livraison » ; R9).

`graines_bras_a_v4.py` reste la table des clés (R12 : non modifié) ; ce module en reprend les noms publics. Il
n'importe ni la version 5 ni la version 6. Le tirage à clé est celui de la version 6 (il ne se fabrique que par ses
deux fabriques, et ne sert qu'une fois). Ce qui change, d'après la vérification du code de la version 6 (M-2, M-3) :

- **le registre des accords n'est lu que s'il porte l'empreinte attendue** (M-2 ; mandat de la version 7, point 5).
  La branche qui porte le code peut avoir un `registres/go.md` en retard sur la branche principale : une ligne de GO
  y manquerait, ou une révocation. `ligne_d_accord` reçoit, obligatoirement, l'empreinte attendue du registre — celle
  du registre de la branche principale, que la configuration scellée de l'analyse inscrit
  (`configuration_bras_a_v7`, `pieces_attendues`). Si le registre du dépôt ne porte pas cette empreinte, la lecture
  s'arrête et dit les deux empreintes : **le code ne lit jamais un registre périmé sans le dire**. Aucun réseau : qui
  scelle la configuration sait où est la branche principale ; le code compare seulement ;
- **une révocation annule une ligne** : le registre dit « une révocation est une nouvelle ligne de type
  "révocation" » ; une ligne de ce type qui nomme l'identifiant donné fait refuser l'accord ;
- **formes de refus entières, non plus des fragments** (M-3) : la version 6 refusait toute ligne qui portait
  « refus », et donc une ligne d'accord vraie qui disait « après la livraison refusée du 20 novembre ». Ici la ligne
  est refusée si elle porte l'une des formes entières de `FORMES_DE_REFUS` (« refusé : », « n'accorde pas »…). Le
  texte ne fixe pas les mots de l'accord (note du brouillon 25, partie 3, point 12) : la phrase exigée et la liste
  des formes de refus sont celles de ce module. Limite écrite : une ligne qui refuserait par d'autres mots tout en
  portant la phrase d'accord à la lettre passerait ; la phrase d'accord, exigée à la lettre, est la vraie garde.

Ce module ne lit qu'un fichier, le registre des accords ; il n'appelle aucun modèle et n'ouvre aucun interne de
moniteur.
"""
from __future__ import annotations

import hashlib
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

# --- Tirage qui porte sa clé (C-7 ; celui de la version 6) ---------------------------------------------------------------------------------------

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
    schéma de permutation (`permutation_etiquettes_bras_a_v7`), pour que les deux côtés aient la même lettre. Toute
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
                         "tirage à clé (`graines_bras_a_v7.tirage_de`), jamais un générateur nu (6.2 ; 8.4 ; R9)")
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


# --- Lignes d'accord au registre du dépôt (vérification du code de la version 6, M-2 et M-3 ; brouillon 25, 6.9) ---------------

_GO = re.compile(r"GO-\d{4}-\d{2}-\d{2}-\d{2,}")
_EMPREINTE = re.compile(r"[0-9a-f]{64}")
# Le registre des accords du dépôt : `registres/go.md`, à la racine. Il n'est pas donné par l'appelant.
REGISTRE_DES_ACCORDS = Path(__file__).resolve().parents[3] / "registres" / "go.md"
TYPE_DE_REVOCATION = "révocation"            # en-tête du registre : « une révocation est une nouvelle ligne de type "révocation" »
# Formes fixes des lignes d'accord, à porter à la lettre (sans égard à la casse) dans la ligne du registre.
PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9 = "écart à R9 accordé pour la table des identifiants opaques"
PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE = "livraison refaite du côté habilité accordée pour le bras A"
# Formes entières par lesquelles une ligne refuse (sans égard à la casse). Un fragment (« refus ») n'en est pas une :
# une ligne d'accord peut nommer « la livraison refusée ».
FORMES_DE_REFUS = ("refusé :", "refusée :", "refus :", "n'accorde pas", "n'est pas accordé", "non accordé", "accord refusé",
                   "accord retiré")


def lire_le_registre_des_accords(sha256_attendu_du_registre: object) -> list[str]:
    """Lignes du registre des accords **du dépôt**, lu **seulement s'il porte l'empreinte attendue** — celle du
    registre de la branche principale, inscrite dans la configuration scellée de l'analyse. Refus : empreinte attendue
    absente ou mal formée (aucune valeur par défaut) ; registre absent ; registre d'une autre empreinte — périmé, en
    avance ou retouché : l'arrêt dit les deux empreintes, et ce qu'il faut faire."""
    if not isinstance(sha256_attendu_du_registre, str) or _EMPREINTE.fullmatch(sha256_attendu_du_registre) is None:
        raise GardeArret("registre des accords : l'empreinte attendue du registre de la branche principale est exigée "
                         "(64 signes ; elle vient de la configuration scellée de l'analyse) — sans elle, rien ne dit que le "
                         "registre du dépôt n'est pas périmé")
    registre = Path(REGISTRE_DES_ACCORDS)
    if not registre.is_file():
        raise GardeArret(f"registre des accords du dépôt ({registre}) absent : un GO ne vaut que par sa ligne au registre")
    brut = registre.read_bytes()
    obtenue = hashlib.sha256(brut).hexdigest()
    if obtenue != sha256_attendu_du_registre:
        raise GardeArret(f"registre des accords du dépôt : il porte l'empreinte {obtenue[:16]}…, et la configuration scellée "
                         f"attend {sha256_attendu_du_registre[:16]}… — registre périmé, en avance ou retouché : il n'est pas "
                         "lu. Apporter sur cette branche le registre de la branche principale, ou sceller une configuration "
                         "qui porte l'empreinte du registre en vigueur")
    try:
        return brut.decode("utf-8").splitlines()
    except UnicodeDecodeError:
        raise GardeArret("registre des accords du dépôt : illisible") from None


def _cellules(ligne: str) -> list[str]:
    return [c.strip() for c in ligne.split("|")[1:-1]] if ligne.startswith("|") else []


def ligne_d_accord(go: object, phrase: str, *, sha256_attendu_du_registre: object) -> str:
    """Ligne du registre des accords **du dépôt** dont la première cellule est l'identifiant donné, et qui porte, à la
    lettre, la phrase d'accord demandée. `sha256_attendu_du_registre` est exigé, sans valeur par défaut
    (`lire_le_registre_des_accords`). Refus : identifiant mal formé ; registre absent ou d'une autre empreinte ; aucune
    ligne, ou plusieurs, pour cet identifiant ; phrase absente ; **une forme de refus dans la ligne** ; **une ligne de
    type « révocation » qui nomme cet identifiant**."""
    if phrase not in (PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9, PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE):
        raise GardeArret("phrase d'accord hors des formes fixes de ce module")
    if not isinstance(go, str) or _GO.fullmatch(go) is None:
        raise GardeArret(f"ligne de GO {go!r} : `GO-AAAA-MM-JJ-NN` exigé")
    toutes = lire_le_registre_des_accords(sha256_attendu_du_registre)
    lignes = [l for l in toutes if (_cellules(l) or [""])[0] == go]
    if len(lignes) != 1:
        raise GardeArret(f"{go} : {len(lignes)} ligne(s) au registre des accords — une ligne, et une seule, exigée")
    for l in toutes:
        c = _cellules(l)
        if len(c) >= 3 and c[0] != go and c[2].casefold() == TYPE_DE_REVOCATION and re.search(re.escape(go) + r"(?!\d)", l):
            raise GardeArret(f"{go} : une ligne de type « {TYPE_DE_REVOCATION} » du registre le nomme ({c[0]}) — il n'accorde "
                             "plus rien")
    ligne = lignes[0].casefold()
    if _cellules(lignes[0])[2:3] == [TYPE_DE_REVOCATION] or phrase.casefold() not in ligne:
        raise GardeArret(f"{go} : la ligne du registre ne porte pas la phrase « {phrase} » — ce n'est pas cet accord")
    if any(forme in ligne for forme in FORMES_DE_REFUS):
        raise GardeArret(f"{go} : la ligne du registre porte une forme de refus — elle n'accorde rien")
    return lignes[0]


def empreintes_citees(ligne: str) -> list[str]:
    """Les empreintes entières (64 signes) qu'une ligne du registre cite, dans l'ordre, sans doublon."""
    vues: list[str] = []
    for e in re.findall(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])", ligne):
        if e not in vues:
            vues.append(e)
    return vues


# --- Entropie propre de la table des identifiants opaques : écart à R9, fermé par défaut ------------------------------------

def admettre_l_entropie_propre_de_la_table_des_identifiants(entropie_de_la_table: int, entropie_du_bras: int, *,
                                                            reglage: str, go_de_lazar: str | None,
                                                            sha256_attendu_du_registre: object) -> dict:
    """Seule porte par laquelle la relance peut **consigner** un tirage fait sans clé de 6.2 : l'entropie propre de la
    table des identifiants opaques des scores des deux moniteurs à modèle de langue produits avant l'ouverture (6.2 ;
    8.4). C'est un **écart à la règle gelée R9, en attente du mot de Lazar** : la porte est fermée tant que `reglage`
    ne vaut pas `ECART_A_R9_ACCORDE`, écrit en toutes lettres. Ouverte, elle exige encore :
    - `go_de_lazar` : un identifiant de GO, **dont la ligne est lue au registre du dépôt** — lu seulement s'il porte
      `sha256_attendu_du_registre` — et porte, à la lettre, la phrase `PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9`, sans forme
      de refus ni révocation (`ligne_d_accord`) ;
    - deux entropies entières, différentes l'une de l'autre (« table tirée de l'entropie du bras » : refusée ; cette
      garde ne voit que l'égalité des deux entiers).
    Les trois réglages sont des arguments nommés, **sans valeur par défaut**. Elle ne tire rien : elle rend la ligne à
    consigner au manifeste, sans graine dérivée."""
    if reglage != ECART_A_R9_ACCORDE:
        raise GardeArret(f"entropie propre de la {USAGE_TABLE_DES_IDENTIFIANTS} : tirage sans clé de 6.2, écart à la règle "
                         f"gelée R9 en attente du mot de Lazar — refusé (seul le réglage `{ECART_A_R9_ACCORDE}`, écrit en "
                         "toutes lettres avec l'identifiant du GO et sa ligne au registre, l'admet)")
    ligne_d_accord(go_de_lazar, PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9, sha256_attendu_du_registre=sha256_attendu_du_registre)
    for nom, e in (("de la table", entropie_de_la_table), ("du bras", entropie_du_bras)):
        if isinstance(e, bool) or not isinstance(e, int) or e < 0:
            raise GardeArret(f"entropie {nom} : entier positif ou nul exigé")
    if entropie_de_la_table == entropie_du_bras:
        raise GardeArret("table des identifiants tirée de l'entropie du bras : refusée (8.4)")
    return {"usage": USAGE_TABLE_DES_IDENTIFIANTS, "entropie": entropie_de_la_table, "cle_de_6_2": None,
            "ecart": "R9 : entropie du système, non dérivée de l'entropie du bras", "go": go_de_lazar}


__all__ = sorted({n for n in _v4.__dict__ if not n.startswith("_")}
                 | {"TirageAClef", "tirage_de", "tirage_reconnu_cote_habilite", "generateur_pour",
                    "tirage_de_l_aire_conditionnelle", "ligne_d_accord", "lire_le_registre_des_accords", "empreintes_citees",
                    "FORMES_DE_REFUS", "MOTIFS_DES_USAGES", "USAGE_TACHES", "USAGE_PAGE",
                    "USAGE_AIRE_CONDITIONNELLE", "USAGE_PERMUTATION_D_UN_MONITEUR", "REGISTRE_DES_ACCORDS",
                    "PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9", "PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE",
                    "admettre_l_entropie_propre_de_la_table_des_identifiants", "ECART_A_R9_REFUSE"})

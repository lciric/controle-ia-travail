"""Graines du bras A des organismes discrets, version 12 du code (préenregistrement
`prereg/T0.7-organismes-discrets-v-a-v2-brouillon35.md`, section 6.2 ; conventions, « Le registre lu » ; 6.9,
« Livraison refaite : une ligne de GO par livraison » ; R9).

`graines_bras_a_v4.py` reste la table des clés (R12 : non modifié) ; ce module en reprend les noms publics. Il
n'importe aucune des versions 5 à 11. **Ce qui change à la version 12** (vérification du code de la version 11, M-3 ;
vérification du brouillon 35, C-1) : **`retire_l_inscription`**, la fonction nommée du retrait d'une configuration
inscrite — une ligne dont la cellule de type est exactement « révocation » et qui cite l'empreinte entière de la
configuration ; le programme du constat, version 5, ne lève la garde du registre que par elle. Rien d'autre ne
change : les douze lignes de la vérification à la porte de l'écart à R9 se lisent comme à la version 11.
**Ce qui avait changé à la version 11** (vérification du code de la version 10, M-1 ;
brouillon 34, 13.2 ; vérification du brouillon 34, M-1 et M-2) :
- **les phrases d'accord sont en cellule d'objet exacte** (`dit_l_accord`) : la cellule d'objet de la ligne de GO
  **est** la phrase — comparée sans le gras de Markdown, sans égard à la casse ni aux accents, un point final seul
  admis ; rien avant, rien après. La version 10 cherchait la phrase comme une partie de la ligne : « aucun écart à
  R9 accordé… » ouvrait la porte. **Une ligne de type « révocation » ne vaut jamais accord**, même si sa cellule
  d'objet est la phrase. Les empreintes et les autres mentions sont dans les autres cellules de la ligne ;
- **la porte de l'écart à R9 regarde le registre courant** : avant le tirage de la table, aucune ligne entrée depuis
  le registre figé ne doit nommer la ligne de GO de l'écart (`lignes_entrees_depuis`) ;
- **l'empreinte qu'inscrit une ligne d'inscription** se lit (`empreinte_inscrite`), pour que le programme du constat
  voie au registre une autre configuration de l'analyse du bras A.
**Ce qui avait changé à la version 10** (vérification du code de la version 9, M-2) :
**les préfixes d'empreinte et les identifiants sans tiret sont reconnus.** Une ligne qui retire une configuration en
n'en citant que les premiers signes de l'empreinte — l'usage courant d'un registre — la cite (`cite_l_empreinte` : un
préfixe de **seize signes au moins**, brouillon 32) ; un identifiant de GO se reconnaît **à ses lettres et à ses
chiffres, quels que soient la casse et les séparateurs, sans lettre ni chiffre collé avant ou après** (« GO
2099-01-01-01 » nomme la ligne ; `nomme_l_identifiant`). La ligne d'inscription, elle, porte toujours l'empreinte entière. **Ce qui avait changé à la
version 9** (vérification du code de la version 8, C-1 et
M-2 ; brouillon 30, conventions, « Reconnaître par le sens, non par le type ») :
- **une ligne qui retire se reconnaît à son sens, non à l'orthographe de son type.** Dans l'état figé, une ligne de
  GO que nomme une ligne placée après elle n'ouvre rien, quel que soit le type de cette ligne (`ligne_d_accord`) ;
  dans le registre courant, toute ligne entrée depuis l'état figé qui nomme la ligne de GO employée, ou qui cite
  l'empreinte de la configuration sans être sa ligne d'inscription, est une « ligne neuve à voir »
  (`ligne_neuve_a_voir`, que le programme du constat de lancement appelle). L'identifiant se compare en entier ;
- **la ligne d'inscription d'une configuration a une forme**, la seule forme d'accord que le texte écrit : type
  « inscription », la marque `CONFIG-ANALYSE-DISCRETION-BRAS-A`, puis l'empreinte entière (`est_la_ligne_d_inscription`).
  **Le type et la marque sont deux constantes nommées, ici et nulle part ailleurs** : la session principale peut les
  changer (demande 29 de la pièce du lecteur habilité). Le tirage à clé est celui de la version 6. Ce qui change, d'après la vérification
du code de la version 7 (C-1) et le brouillon 26 :

**Le registre lu est remis au programme comme une pièce.** C'est le registre des accords de la branche principale
**tel qu'il était quand la configuration a été scellée** — son état figé. Il porte la ligne de GO qui ouvre la
livraison ; il ne porte pas la ligne qui inscrit la configuration, écrite après lui. Il est reconnu **à sa seule
empreinte**, celle que la configuration scellée inscrit ; un registre d'une autre empreinte n'est pas lu. Ce module ne
lit donc plus `registres/go.md` du dépôt, qui change à chaque ligne neuve : il lit le fichier qu'on lui remet, et
seulement s'il porte l'empreinte attendue.

**Le point d'entrée** est `lire_le_registre_fige` ; le reste du code l'appelle sans en connaître le dedans.

**Ce que ce module ne fait pas** : le constat de lancement. C'est la session qui lance qui constate, sur le registre
courant de la branche principale, que l'empreinte de la configuration y est inscrite et qu'aucune ligne entrée depuis
l'état figé ne révoque la ligne de GO employée ; elle le consigne, daté, au manifeste du lancement. Si une révocation
est entrée, la lecture ne part pas. Ici, une ligne qu'une révocation nomme **dans l'état figé** n'ouvre rien. Après
la lecture, ce code ne fait rien d'une révocation : il ne retire ni ne confirme.

Restent de la version 7 : les formes de refus entières (`FORMES_DE_REFUS`) et la phrase d'accord exigée à la lettre,
que le texte fixe depuis le brouillon 34. Ce module ne lit que les deux pièces du registre qu'on lui remet — l'état
figé, et, pour la porte de l'écart à R9, le registre courant ; il n'appelle aucun modèle et n'ouvre aucun interne de
moniteur.
"""
from __future__ import annotations

import hashlib
import re
import unicodedata
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
    schéma de permutation (`permutation_etiquettes_bras_a_v12`), pour que les deux côtés aient la même lettre. Toute
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
                         "tirage à clé (`graines_bras_a_v12.tirage_de`), jamais un générateur nu (6.2 ; 8.4 ; R9)")
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


# --- Lignes d'accord au registre, remis comme une pièce (vérification du code de la version 7, C-1 ; brouillon 26) -----------

_GO = re.compile(r"GO-\d{4}-\d{2}-\d{2}-\d{2,}")
_EMPREINTE = re.compile(r"[0-9a-f]{64}")
TYPE_DE_REVOCATION = "révocation"            # en-tête du registre : « une révocation est une nouvelle ligne de type "révocation" »
# Phrases d'accord, fixées à la lettre (brouillon 34, 13.2) : **la cellule d'objet de la ligne de GO est exactement
# la phrase** (`dit_l_accord`).
PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9 = "écart à R9 accordé pour la table des identifiants opaques"
PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE = "livraison refaite du côté habilité accordée pour le bras A"
# Formes entières par lesquelles une ligne refuse (sans égard à la casse). Un fragment (« refus ») n'en est pas une :
# une ligne d'accord peut nommer « la livraison refusée ».
FORMES_DE_REFUS = ("refusé :", "refusée :", "refus :", "n'accorde pas", "n'est pas accordé", "non accordé", "accord refusé",
                   "accord retiré")


# --- Reconnaître par le sens, non par le type (brouillon 30, conventions ; vérification du code de la version 8, C-1, M-2) ---

# **La forme de la ligne d'inscription d'une configuration — les deux constantes que la session principale peut
# changer** (demande 29) : le type de la ligne, et la marque qui précède l'empreinte entière.
TYPE_DE_LA_LIGNE_D_INSCRIPTION = "inscription"
MARQUE_DE_LA_LIGNE_D_INSCRIPTION = "CONFIG-ANALYSE-DISCRETION-BRAS-A"
CELLULE_DU_TYPE = 2                          # table du registre : identifiant, date, type, objet…
# **Laquelle des cellules est celle de l'objet** : la quatrième. Constante nommée, ici et nulle part ailleurs — la
# session principale la confirme, avec les formes d'inscription et de révocation (brouillon 34, 13.2).
CELLULE_DE_L_OBJET = 3
GRAS_DE_MARKDOWN = "**"                      # les cellules d'objet du registre sont d'ordinaire en gras
MOTIF_LIGNE_NEUVE_QUI_NOMME_LA_LIGNE_DE_GO = "ligne neuve à voir : elle nomme la ligne de GO employée"
MOTIF_LIGNE_NEUVE_QUI_CITE_LA_CONFIGURATION = ("ligne neuve à voir : elle cite l'empreinte de la configuration sans être sa "
                                               "ligne d'inscription")


def sans_accent(texte: str) -> str:
    """Le texte sans égard à la casse ni aux accents (« Révocation », « revocation » et « RÉVOCATION » se valent)."""
    return "".join(c for c in unicodedata.normalize("NFKD", texte.casefold()) if not unicodedata.combining(c))


# Entre les parties d'un identifiant de GO, tout ce qui n'est ni lettre ni chiffre est un séparateur, ou rien
# (brouillon 32 ; vérification du code de la version 9, M-2 : « GO 2099-01-01-01 » n'était pas vu).
_ENTRE_LES_PARTIES = r"[^0-9A-Za-z]*"
# Un préfixe d'empreinte compte dès seize signes (brouillon 32, conventions) ; la consigne de tenue du registre demande
# l'empreinte entière.
LONGUEUR_MINIMALE_D_UN_PREFIXE_D_EMPREINTE = 16


def nomme_l_identifiant(ligne: str, identifiant: str) -> bool:
    """Vrai si la ligne écrit cet identifiant de GO, **en entier** : reconnu à ses lettres et à ses chiffres, quels que
    soient la casse et les séparateurs, **sans lettre ni chiffre collé avant ou après**. `GO-2099-01-01-01`,
    `go 2099-01-01-01`, `GO2099-01-01-01` et `GO_2099.01.01.01` le nomment ; `GO-2099-01-01-011`, `XGO-2099-01-01-01`
    et `GO-2099-01-01-01b` ne le nomment pas."""
    parties = re.findall(r"[0-9A-Za-z]+", identifiant)
    if not parties:
        raise GardeArret("identifiant de GO vide")
    motif = r"(?<![0-9A-Za-z])" + _ENTRE_LES_PARTIES.join(re.escape(p) for p in parties) + r"(?![0-9A-Za-z])"
    return re.search(motif, ligne, re.IGNORECASE) is not None


def cite_l_empreinte(ligne: str, empreinte: str) -> bool:
    """Vrai si la ligne écrit cette empreinte, sans égard à la casse : **entière**, où qu'elle soit, **ou abrégée** —
    une suite de seize signes hexadécimaux au moins qui en est le début. Un abrégé plus court n'est pas vu : la
    consigne de tenue du registre demande l'empreinte entière (brouillon 32, 13.2)."""
    e, texte = empreinte.casefold(), ligne.casefold()
    if e in texte:
        return True
    return any(len(suite) >= LONGUEUR_MINIMALE_D_UN_PREFIXE_D_EMPREINTE and e.startswith(suite)
               for suite in re.findall(r"[0-9a-f]+", texte))


def est_la_ligne_d_inscription(ligne: str, sha256_de_la_configuration: str) -> bool:
    """**La ligne d'inscription d'une configuration** (brouillon 30) : une ligne de la table du registre, **de type
    « inscription »**, qui porte **à la lettre** la marque `CONFIG-ANALYSE-DISCRETION-BRAS-A` **puis l'empreinte
    entière** de la configuration — rien entre les deux que des signes qui ne sont ni lettres ni chiffres. C'est la
    seule forme d'accord que le texte écrit."""
    cellules = _cellules(ligne)
    if len(cellules) <= CELLULE_DU_TYPE or sans_accent(cellules[CELLULE_DU_TYPE]) != sans_accent(TYPE_DE_LA_LIGNE_D_INSCRIPTION):
        return False
    return re.search(re.escape(MARQUE_DE_LA_LIGNE_D_INSCRIPTION) + r"[^0-9A-Za-z]*" + re.escape(sha256_de_la_configuration)
                     + r"(?![0-9a-f])", ligne) is not None


def ligne_neuve_a_voir(ligne: str, *, ligne_de_go: str | None, sha256_de_la_configuration: str) -> str | None:
    """**Fonction nommée de la révocation reconnue par son sens** (brouillon 30 ; vérification du code de la version
    8, C-1 et M-2). Pour une ligne **entrée depuis l'état figé**, rend le motif qui rend le constat malsain, ou
    `None` :
    - elle **nomme l'identifiant de la ligne de GO employée**, quel que soit son type — révocation bien ou mal
      orthographiée, décision qui dit l'accord révoqué, simple mention ; même la ligne d'inscription, si elle le nomme ;
    - ou elle **cite l'empreinte de la configuration sans être sa ligne d'inscription** — par exemple pour la retirer.
    **Ce code ne juge pas ce que la ligne veut dire** : il la signale. Le remède est toujours le même : une ligne de
    GO neuve, donc un autre mot de Lazar, et une configuration neuve, scellée sur le nouvel état du registre. Un faux
    malsain coûte une ligne ; une révocation manquée ferait lire sous un accord retiré. `ligne_de_go` vaut `None` pour
    une première livraison, qui n'emploie aucune ligne."""
    if ligne_de_go is not None and nomme_l_identifiant(ligne, ligne_de_go):
        return MOTIF_LIGNE_NEUVE_QUI_NOMME_LA_LIGNE_DE_GO
    if cite_l_empreinte(ligne, sha256_de_la_configuration) and not est_la_ligne_d_inscription(ligne, sha256_de_la_configuration):
        return MOTIF_LIGNE_NEUVE_QUI_CITE_LA_CONFIGURATION
    return None


def empreinte_inscrite(ligne: str) -> str | None:
    """L'empreinte entière qu'inscrit **une ligne d'inscription d'une configuration de l'analyse du bras A** — type
    « inscription », la marque, puis une empreinte entière —, ou `None` si la ligne n'en est pas une. Pour le
    programme du constat : une autre configuration inscrite au registre se voit (vérification du brouillon 34, M-1)."""
    cellules = _cellules(ligne)
    if len(cellules) <= CELLULE_DU_TYPE or sans_accent(cellules[CELLULE_DU_TYPE]) != sans_accent(TYPE_DE_LA_LIGNE_D_INSCRIPTION):
        return None
    trouvee = re.search(re.escape(MARQUE_DE_LA_LIGNE_D_INSCRIPTION) + r"[^0-9A-Za-z]*([0-9a-f]{64})(?![0-9a-f])", ligne)
    return None if trouvee is None else trouvee.group(1)


def retire_l_inscription(ligne: str, sha256_de_la_configuration: str) -> bool:
    """**Fonction nommée du retrait d'une inscription** (vérification du code de la version 11, M-3 ; vérification du
    brouillon 35, C-1). Vrai quand la ligne est une ligne de la table du registre **dont la cellule de type est
    exactement « révocation »** — sans le gras de Markdown, sans égard à la casse ni aux accents — **et qu'elle cite
    l'empreinte entière**, soixante-quatre signes, de la configuration. Un abrégé ne retire rien : le retrait lève
    une garde, et se lit donc au plus strict. C'est un mot de Lazar : seule une ligne de ce type retire une
    configuration inscrite, abandonnée avant sa lecture."""
    cellules = _cellules(ligne)
    if len(cellules) <= CELLULE_DU_TYPE or forme_d_une_cellule(cellules[CELLULE_DU_TYPE]) != forme_d_une_cellule(TYPE_DE_REVOCATION):
        return False
    return sha256_de_la_configuration in empreintes_citees(ligne)


def forme_d_une_cellule(texte: str) -> str:
    """Une cellule du registre, telle qu'on la compare : **sans le gras de Markdown**, sans égard à la casse ni aux
    accents, les blancs réduits à un seul."""
    return " ".join(sans_accent(texte.replace(GRAS_DE_MARKDOWN, "")).split())


def dit_l_accord(ligne: str, phrase: str) -> bool:
    """**Fonction nommée de la phrase d'accord** (brouillon 34, 13.2 et 8.4, « phrases d'accord des lignes de GO » ;
    vérification du code de la version 10, M-1 ; vérification du brouillon 34, M-2). Vrai quand **la cellule d'objet
    de la ligne est exactement la phrase** — sans le gras de Markdown, sans égard à la casse ni aux accents, **un
    point final seul admis** ; rien avant, rien après — **et que la ligne n'est pas de type « révocation »**. Une
    phrase seulement contenue dans la cellule n'ouvre rien : « aucun écart… », « pas d'écart… avant le devis »,
    « … ? à trancher ». Vaut pour les deux phrases."""
    cellules = _cellules(ligne)
    if len(cellules) <= CELLULE_DE_L_OBJET or sans_accent(TYPE_DE_REVOCATION) in sans_accent(cellules[CELLULE_DU_TYPE]):
        return False
    objet, attendue = forme_d_une_cellule(cellules[CELLULE_DE_L_OBJET]), forme_d_une_cellule(phrase)
    return objet in (attendue, attendue + ".")


def lignes_entrees_depuis(lignes_figees: list[str], registre_courant: object) -> list[str]:
    """Les lignes du registre courant entrées depuis l'état figé : le registre courant, remis comme une pièce (le
    chemin d'un fichier), moins chacune des lignes de l'état figé. **Un registre ne perd pas de ligne** : si une
    ligne de l'état figé manque au registre courant, ce n'est pas un état postérieur du même registre — refus."""
    try:
        present = isinstance(registre_courant, (str, Path)) and Path(registre_courant).is_file()
    except OSError:
        present = False
    if not present:
        raise GardeArret("registre des accords : le registre courant de la branche principale est exigé (le chemin d'un "
                         "fichier, remis par la session qui lance)")
    try:
        entrees = Path(registre_courant).read_bytes().decode("utf-8").splitlines()
    except UnicodeDecodeError:
        raise GardeArret("registre des accords, registre courant : illisible") from None
    for ligne in lignes_figees:
        if ligne not in entrees:
            raise GardeArret("registre des accords : le registre courant ne contient pas une ligne de l'état figé "
                             f"({(_cellules(ligne) or ['ligne hors de la table'])[0]}) — ce n'est pas un état postérieur du "
                             "même registre (une ligne du registre n'est jamais retirée ni changée)")
        entrees.remove(ligne)
    return entrees


def lire_le_registre_fige(registre_fige: object, sha256_au_scellement: object) -> list[str]:
    """**Point d'entrée de la lecture du registre des accords.** Lignes du registre **dans son état figé au scellement
    de la configuration**, remis comme une pièce (`registre_fige` : le chemin du fichier) et reconnu **à sa seule
    empreinte**, celle que la configuration scellée inscrit. Refus (gardes ordinaires : rien n'est lu d'aucune
    livraison) : empreinte attendue absente ou mal formée ; pièce absente ; **pièce d'une autre empreinte** — l'arrêt
    dit les deux empreintes ; pièce illisible."""
    if not isinstance(sha256_au_scellement, str) or _EMPREINTE.fullmatch(sha256_au_scellement) is None:
        raise GardeArret("registre des accords : l'empreinte de son état figé au scellement de la configuration est exigée "
                         "(64 signes ; elle vient de la configuration scellée de l'analyse) — sans elle, rien ne dit quel "
                         "registre lire")
    try:
        present = isinstance(registre_fige, (str, Path)) and Path(registre_fige).is_file()
    except OSError:
        present = False
    if not present:
        raise GardeArret("registre des accords : la pièce qui porte son état figé au scellement de la configuration est "
                         "exigée (le chemin d'un fichier) — un GO ne vaut que par sa ligne au registre")
    brut = Path(registre_fige).read_bytes()
    obtenue = hashlib.sha256(brut).hexdigest()
    if obtenue != sha256_au_scellement:
        raise GardeArret(f"registre des accords : la pièce remise porte l'empreinte {obtenue[:16]}…, et la configuration "
                         f"scellée attend {sha256_au_scellement[:16]}… — ce n'est pas le registre dans son état figé au "
                         "scellement de la configuration : il n'est pas lu. Remettre le registre de la branche principale tel "
                         "qu'il était quand cette configuration a été scellée")
    try:
        return brut.decode("utf-8").splitlines()
    except UnicodeDecodeError:
        raise GardeArret("registre des accords, état figé : illisible") from None


def _cellules(ligne: str) -> list[str]:
    return [c.strip() for c in ligne.split("|")[1:-1]] if ligne.startswith("|") else []


def ligne_d_accord(go: object, phrase: str, *, registre_fige: object, sha256_au_scellement: object) -> str:
    """Ligne du registre des accords dont la première cellule est l'identifiant donné, et **dont la cellule d'objet
    est exactement la phrase d'accord demandée** (`dit_l_accord`) — lue dans **l'état du registre figé au scellement
    de la configuration** (`lire_le_registre_fige`). Les deux arguments nommés sont exigés, sans valeur par défaut.
    Refus (gardes ordinaires) : identifiant mal formé ; registre qui ne se lit pas ; aucune ligne, ou plusieurs, pour
    cet identifiant dans l'état figé ; cellule d'objet qui n'est pas la phrase ; ligne de type « révocation » ; une
    forme de refus dans la ligne ; **une ligne de l'état figé, placée après
    elle, qui nomme cet identifiant — quel que soit son type** (brouillon 30 : « une ligne de GO que nomme une ligne
    entrée après elle n'ouvre rien » ; la version 8 ne voyait qu'une ligne de type écrit « révocation »)."""
    if phrase not in (PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9, PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE):
        raise GardeArret("phrase d'accord hors des formes fixes de ce module")
    if not isinstance(go, str) or _GO.fullmatch(go) is None:
        raise GardeArret(f"ligne de GO {go!r} : `GO-AAAA-MM-JJ-NN` exigé")
    toutes = lire_le_registre_fige(registre_fige, sha256_au_scellement)
    lignes = [l for l in toutes if (_cellules(l) or [""])[0] == go]
    if len(lignes) != 1:
        raise GardeArret(f"{go} : {len(lignes)} ligne(s) dans le registre des accords, état figé au scellement de la "
                         "configuration — une ligne, et une seule, exigée")
    place = next(i for i, l in enumerate(toutes) if l is lignes[0])
    for l in toutes[place + 1:]:
        if nomme_l_identifiant(l, go):
            raise GardeArret(f"{go} : une ligne de l'état figé du registre, entrée après lui, le nomme "
                             f"({(_cellules(l) or ['hors de la table'])[0]}) — révocation, ou ligne à voir, quel que soit son "
                             "type : il n'ouvre rien (conventions, « Reconnaître par le sens »)")
    ligne = lignes[0].casefold()
    if not dit_l_accord(lignes[0], phrase):
        raise GardeArret(f"{go} : la cellule d'objet de la ligne du registre n'est pas exactement la phrase « {phrase} », ou "
                         "la ligne est de type « révocation » — ce n'est pas cet accord (13.2)")
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
                                                            registre_fige: object, sha256_au_scellement: object,
                                                            registre_courant: object) -> dict:
    """Seule porte par laquelle la relance peut **consigner** un tirage fait sans clé de 6.2 : l'entropie propre de la
    table des identifiants opaques des scores des deux moniteurs à modèle de langue produits avant l'ouverture (6.2 ;
    8.4). C'est un **écart à la règle gelée R9, en attente du mot de Lazar** : la porte est fermée tant que `reglage`
    ne vaut pas `ECART_A_R9_ACCORDE`, écrit en toutes lettres. Ouverte, elle exige encore :
    - `go_de_lazar` : un identifiant de GO, **dont la ligne est lue dans le registre remis comme une pièce**, dans son
      état figé (`registre_fige`, reconnu à `sha256_au_scellement` : l'état du registre au commit qui inscrit cette
      ligne, dont l'empreinte est dans la configuration scellée du lanceur — brouillon 34, 6.2 et 13.2), et dont la
      cellule d'objet est exactement `PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9`, sans forme de refus ni révocation
      (`ligne_d_accord`) ;
    - `registre_courant` : le registre courant de la branche principale, remis comme une pièce — **avant le tirage de
      la table, aucune ligne entrée depuis l'état figé ne doit nommer cette ligne de GO** (vérification du brouillon
      34, M-2 (c) : une révocation entrée après le commit de l'inscription, mais avant le tirage, n'était pas vue).
      C'est le contrôle que fait le constat de lancement pour une lecture ; reconnu par le sens, quel que soit le
      type de la ligne ;
    - deux entropies entières, différentes l'une de l'autre (« table tirée de l'entropie du bras » : refusée ; cette
      garde ne voit que l'égalité des deux entiers).
    Les cinq réglages sont des arguments nommés, **sans valeur par défaut**. Elle ne tire rien : elle rend la ligne à
    consigner au manifeste, sans graine dérivée."""
    if reglage != ECART_A_R9_ACCORDE:
        raise GardeArret(f"entropie propre de la {USAGE_TABLE_DES_IDENTIFIANTS} : tirage sans clé de 6.2, écart à la règle "
                         f"gelée R9 en attente du mot de Lazar — refusé (seul le réglage `{ECART_A_R9_ACCORDE}`, écrit en "
                         "toutes lettres avec l'identifiant du GO et sa ligne au registre, l'admet)")
    ligne_d_accord(go_de_lazar, PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9, registre_fige=registre_fige,
                   sha256_au_scellement=sha256_au_scellement)
    for ligne in lignes_entrees_depuis(lire_le_registre_fige(registre_fige, sha256_au_scellement), registre_courant):
        if nomme_l_identifiant(ligne, go_de_lazar):
            raise GardeArret(f"{go_de_lazar} : une ligne entrée au registre courant depuis l'état figé le nomme "
                             f"({(_cellules(ligne) or ['hors de la table'])[0]}) — révocation, ou ligne à voir, quel que "
                             "soit son type : l'écart à R9 n'est plus accordé sous cette ligne, le tirage de la table ne "
                             "part pas")
    for nom, e in (("de la table", entropie_de_la_table), ("du bras", entropie_du_bras)):
        if isinstance(e, bool) or not isinstance(e, int) or e < 0:
            raise GardeArret(f"entropie {nom} : entier positif ou nul exigé")
    if entropie_de_la_table == entropie_du_bras:
        raise GardeArret("table des identifiants tirée de l'entropie du bras : refusée (8.4)")
    return {"usage": USAGE_TABLE_DES_IDENTIFIANTS, "entropie": entropie_de_la_table, "cle_de_6_2": None,
            "ecart": "R9 : entropie du système, non dérivée de l'entropie du bras", "go": go_de_lazar}


__all__ = sorted({n for n in _v4.__dict__ if not n.startswith("_")}
                 | {"TirageAClef", "tirage_de", "tirage_reconnu_cote_habilite", "generateur_pour",
                    "tirage_de_l_aire_conditionnelle", "ligne_d_accord", "lire_le_registre_fige", "empreintes_citees",
                    "ligne_neuve_a_voir", "est_la_ligne_d_inscription", "nomme_l_identifiant", "cite_l_empreinte",
                    "sans_accent", "TYPE_DE_LA_LIGNE_D_INSCRIPTION", "MARQUE_DE_LA_LIGNE_D_INSCRIPTION",
                    "dit_l_accord", "forme_d_une_cellule", "empreinte_inscrite", "lignes_entrees_depuis",
                    "CELLULE_DE_L_OBJET", "GRAS_DE_MARKDOWN",
                    "LONGUEUR_MINIMALE_D_UN_PREFIXE_D_EMPREINTE",
                    "MOTIF_LIGNE_NEUVE_QUI_NOMME_LA_LIGNE_DE_GO", "MOTIF_LIGNE_NEUVE_QUI_CITE_LA_CONFIGURATION",
                    "FORMES_DE_REFUS", "MOTIFS_DES_USAGES", "USAGE_TACHES", "USAGE_PAGE",
                    "USAGE_AIRE_CONDITIONNELLE", "USAGE_PERMUTATION_D_UN_MONITEUR",
                    "PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9", "PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE",
                    "admettre_l_entropie_propre_de_la_table_des_identifiants", "ECART_A_R9_REFUSE"})

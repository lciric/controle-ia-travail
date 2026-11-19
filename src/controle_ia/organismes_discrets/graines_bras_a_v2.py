"""Graines du bras A des organismes discrets, version 2 du code (préenregistrement
`prereg/T0.7-organismes-discrets-v-a-v2-brouillon6.md`, section 6.2 ; R9).

Ce qui change depuis `graines_bras_a_v1.py` (écrit sur le brouillon 5, laissé tel quel, R12) :
- **la table des clés est fermée** (6.2 : « aucun autre nom d'analyse n'existe », « un tirage sans clé de cette table est
  refusé par le programme » ; garde neuve de 8.4, « tirage sans clé de 6.2 ») : tout générateur passe par
  `exiger_cle_de_la_table`, qui refuse un usage, un lot, une épreuve, un lecteur, un moniteur ou une forme de dose hors de
  la table ;
- `relu` n'a plus que ses deux clés (`relu/lot-decisif/actions`, `relu/lot-decisif/plans`) ;
- les lecteurs s'appellent `claude` et `carbon` dans les clés, quel que soit le modèle retenu ;
- les clés d'analyse sont nommées : `boot/taches/{lot}`, `boot/taches/prise-de-la-distillation`,
  `boot/aire-conditionnelle/{moniteur}/{dose}`, `perm/page`, `perm/marginales/{dose}` ; `boot/moniteur` et
  `perm/moniteur` aux quatre doses ;
- `alea` n'existe que pour les deux lots `lot-honnete-appariement` et `lot-mecanique-couverture` ;
- la révision bornée ne préfixe que les tirages que 6.2 nomme (`alea`, `join`, `ancr`, `opaq`, `ordr`, `puis`, et
  `boot/taches` des deux lots de l'appariement), et aucun tirage de la couverture ;
- plus aucune fonction ne reçoit de transformation libre de clé (l'argument `cle_fn` de la version 1 laissait passer
  n'importe quelle clé) : la révision est un booléen.

Dérivation, inchangée : une clé textuelle passée à `manifeste.graines` (donc
`SeedSequence(entropie, spawn_key=(cle_de_tache(clé),))`), générateur par `manifeste.generateur`, entier par
`graine_entiere` (formule de `lanceur_bras_a_v2.graine_entiere`, recopiée parce que ce lanceur importe `torch`).

Ce module ne lit aucun fichier, n'appelle aucun modèle et n'ouvre aucun interne de moniteur. Les clés de la base « mots
et coût » et des deux moniteurs à modèle de langue ne sont ici que des **noms** (6.2 les écrit) : leur emploi est du
côté habilité.
"""
from __future__ import annotations

import hashlib
import re
from typing import Iterable, Sequence

import numpy as np

from ..gardes import GardeArret
from ..manifeste import cle_de_tache, generateur, graines

PREFIXE = "bras-a-v2/"
PREFIXE_REVISION = "revision/"            # 6.2 : « le préfixe `revision/` posé devant la clé entière »
PREFIXE_BASE = "bras-a-v2/base-mots-et-cout/"

# --- Noms fixés par la section 6.2 (« formes fixes des parties ») ---------------------------------------------------------
LOTS = ("lot-honnete-appariement", "lot-jumeaux-appariement", "lot-honnete-couverture", "lot-mecanique-couverture",
        "lot-jumeaux-couverture", "ancre-plans-honnetes", "ancre-jumeaux", "ancre-couverture", "lot-decisif")
LOTS_D_EPREUVE = LOTS[:5]                                     # « les cinq lots d'épreuve » de `boot/taches/{lot}`
LOTS_DE_L_APPARIEMENT = ("lot-honnete-appariement", "lot-jumeaux-appariement")
LOTS_ALEA = ("lot-honnete-appariement", "lot-mecanique-couverture")   # texte sans rapport ; dose flagrante
# Lots rejoués sous la révision bornée (6.6 : lot honnête, lot des jumeaux et les deux parties de l'ancre de
# l'appariement ; « aucun tirage de la couverture ») : lecture du rédacteur du code pour `opaq` et `ordr`, signalée.
LOTS_DE_LA_REVISION = ("lot-honnete-appariement", "lot-jumeaux-appariement", "ancre-plans-honnetes", "ancre-jumeaux")
EPREUVES_JOINTES = ("controles-autre-tache", "texte-sans-rapport", "controles-generiques")
PARTIES_ANCRE = ("premiere", "seconde")
LECTEURS = ("claude", "carbon")                              # lecteur 1, lecteur 2 (conventions ; 6.2)
MONITEURS = ("classifieur-lexical", "moniteur-boite-noire", "agregateur-sequentiel", "classifieur-de-surface",
             "juge-autre-lignee")
MONITEURS_A_MODELE_DE_LANGUE = ("moniteur-boite-noire", "juge")   # double nom du juge, déclaré en 6.2
DOSES_VERDICT = (0.5, 0.75, 1.0)
DOSES_FABRIQUEES = (0.25, 0.5, 0.75, 1.0)
FORMES_DOSE = ("dose-0.25", "dose-0.50", "dose-0.75", "dose-1.00")
RELUS = ("actions", "plans")
PAS_PAR_EPISODE = 10
EPISODES_PAR_TACHE = 8
POSITIONS_JUGE = 32
NOMBRE_CLES_BASE = 29                                        # 28 propres à la base, et `bras-a-v2/plis`


def _ou(noms: Iterable[str]) -> str:
    return "(?:" + "|".join(re.escape(n) for n in noms) + ")"


_T = r"(?P<tache>[^\n\r]+)"       # identifiant de tâche « recopié sans retouche » : toute chaîne d'une ligne, non vide
_E, _P = r"e[0-7]", r"p[0-9]"
# Table fermée des clés des usages neufs, après le préfixe `bras-a-v2/` (6.2). Chaque motif est ancré aux deux bouts.
TABLE = {
    "ouve": r"ouve",
    "meca": rf"meca/{_T}",
    "meca-ancre": r"meca-ancre",
    "retr": rf"retr/{_T}/{_E}/{_ou(LECTEURS)}",
    "refp": r"refp",
    "alea": rf"alea/{_ou(LOTS_ALEA)}/{_T}/{_E}/{_P}",
    "join": rf"join/{_ou(EPREUVES_JOINTES)}",
    "ancr": rf"ancr/{_ou(PARTIES_ANCRE)}",
    "opaq": rf"opaq/{_ou(LOTS)}",
    "ordr": rf"ordr/{_ou(LOTS)}",
    "sent": rf"sent/{_T}/{_E}",
    "relu": rf"relu/lot-decisif/{_ou(RELUS)}",
    "puis": rf"puis/{_T}",
    "boot": (rf"boot/(?:taches/(?:{_ou(LOTS_D_EPREUVE + ('lot-decisif',))}|prise-de-la-distillation)"
             rf"|(?:moniteur|aire-conditionnelle)/{_ou(MONITEURS)}/{_ou(FORMES_DOSE)})"),
    "perm": rf"perm/(?:page|moniteur/{_ou(MONITEURS)}/{_ou(FORMES_DOSE)}|marginales/{_ou(FORMES_DOSE)})",
    "lec6": rf"lec6/{_T}",
    "plis": r"plis",
    # deux familles de clés hors des « usages » : les lectures des deux moniteurs à modèle de langue
    "moniteur-boite-noire": rf"moniteur-boite-noire/{_T}/{_E}/{_P}",
    "juge": rf"juge/{_T}/{_E}/{_P}",
}
# Tirages rejoués sous la révision bornée (6.2, dernier paragraphe de la table), et eux seuls.
TABLE_REVISION = {
    "alea": rf"alea/lot-honnete-appariement/{_T}/{_E}/{_P}",
    "join": TABLE["join"],
    "ancr": TABLE["ancr"],
    "opaq": rf"opaq/{_ou(LOTS_DE_LA_REVISION)}",
    "ordr": rf"ordr/{_ou(LOTS_DE_LA_REVISION)}",
    "puis": TABLE["puis"],
    "boot": rf"boot/taches/{_ou(LOTS_DE_L_APPARIEMENT)}",
}


def forme_dose(dose: float) -> str:
    """Forme d'une dose dans une clé (6.2) : `dose-0.25`, `dose-0.50`, `dose-0.75`, `dose-1.00`. Toute autre dose est
    refusée (aucune clé à la dose 0, ni aux témoins)."""
    if isinstance(dose, bool) or not isinstance(dose, (int, float)) or float(dose) not in DOSES_FABRIQUEES:
        raise GardeArret(f"dose {dose!r} hors de {DOSES_FABRIQUEES}")
    return f"dose-{float(dose):.2f}"


def cles_de_la_base() -> list[str]:
    """Les 29 clés de la base « mots et coût » (6.2), à la lettre du texte transmis."""
    cles = [f"{PREFIXE_BASE}aire/{v}/{d}" for v in ("N-029", "mots_et_cout", "cout-brut") for d in FORMES_DOSE]
    cles.append(f"{PREFIXE_BASE}aire/transfert/dose-1.00/temoin-identite")
    cles += [f"{PREFIXE_BASE}plancher/{v}/{d}" for v in ("N-029", "mots_et_cout") for d in FORMES_DOSE]
    cles.append(f"{PREFIXE_BASE}plancher/transfert/dose-1.00/temoin-identite")
    cles += [f"{PREFIXE_BASE}audit-r4/{c}" for c in ("honnete",) + FORMES_DOSE + ("temoin-identite",)]
    cles.append(PREFIXE + "plis")
    if len(cles) != NOMBRE_CLES_BASE or len(set(cles)) != len(cles):
        raise GardeArret(f"{len(cles)} clés de la base au lieu de {NOMBRE_CLES_BASE}")
    return cles


def exiger_cle_de_la_table(cle_entiere: str) -> str:
    """Garde neuve de 8.4, « tirage sans clé de 6.2 » : la clé doit être une clé de la table de 6.2 — clé d'un usage
    neuf (avec, pour les seuls tirages que la révision rejoue, le préfixe `revision/` devant la clé entière), clé de
    lecture d'un moniteur à modèle de langue, ou clé de la base. Rend le nom de l'usage. Tout le reste est refusé."""
    if not isinstance(cle_entiere, str) or not cle_entiere:
        raise GardeArret(f"clé {cle_entiere!r} : texte non vide exigé")
    if cle_entiere in cles_de_la_base():
        return "plis" if cle_entiere == PREFIXE + "plis" else "base-mots-et-cout"
    revision = cle_entiere.startswith(PREFIXE_REVISION)
    reste = cle_entiere[len(PREFIXE_REVISION):] if revision else cle_entiere
    if not reste.startswith(PREFIXE):
        raise GardeArret(f"clé {cle_entiere!r} : préfixe `{PREFIXE}` exigé (6.2)")
    corps = reste[len(PREFIXE):]
    usage = corps.split("/", 1)[0]
    table = TABLE_REVISION if revision else TABLE
    if usage not in table or re.fullmatch(table[usage], corps) is None:
        raise GardeArret(f"clé {cle_entiere!r} hors de la table de la section 6.2"
                         + (" pour la révision bornée" if revision else "") + " : tirage refusé (garde de 8.4)")
    return usage


def cle(usage: str, *parties: object, revision: bool = False) -> str:
    """Clé d'un usage neuf (6.2) : `bras-a-v2/{usage}/{parties…}`, avec le préfixe `revision/` devant la clé entière sous
    la révision bornée. La clé construite est confrontée à la table fermée : un usage, un lot, une épreuve, un lecteur,
    un moniteur ou une forme de dose hors de la table est refusé."""
    morceaux = [usage] + list(parties)
    if any(not isinstance(m, str) or not m for m in morceaux):
        raise GardeArret(f"partie de clé vide ou non textuelle : {morceaux!r}")
    c = (PREFIXE_REVISION if revision else "") + PREFIXE + "/".join(morceaux)
    exiger_cle_de_la_table(c)
    return c


def _position(episode: int, pas: int | None = None) -> tuple[str, ...]:
    for nom, v, borne in (("épisode", episode, EPISODES_PAR_TACHE), ("pas", pas, PAS_PAR_EPISODE)):
        if v is None:
            continue
        if isinstance(v, bool) or not isinstance(v, (int, np.integer)) or not 0 <= int(v) < borne:
            raise GardeArret(f"{nom} {v!r} hors de 0..{borne - 1}")
    return (f"e{int(episode)}",) + (() if pas is None else (f"p{int(pas)}",))


def cle_alea(lot: str, tache: str, episode: int, pas: int, revision: bool = False) -> str:
    """`alea/{lot}/{tâche}/e{k}/p{pas}` : mots tirés qui remplacent la valeur de `CONTROLS` d'une action (texte sans
    rapport au lot honnête de l'appariement ; dose flagrante au lot mécanique de la couverture)."""
    return cle("alea", lot, tache, *_position(episode, pas), revision=revision)


def cle_retrait(tache: str, episode: int, lecteur: str) -> str:
    """`retr/{tâche}/e{k}/{lecteur}` : contrôle retiré de l'artefact de retrait **lu par** ce lecteur."""
    return cle("retr", tache, *_position(episode), lecteur)


def cle_sentinelles(tache: str, episode: int) -> str:
    return cle("sent", tache, *_position(episode))


def cle_moniteur_modele_de_langue(moniteur: str, tache: str, episode: int, pas: int) -> str:
    """Clés des deux moniteurs à modèle de langue, **sans la condition** (6.2) : `moniteur-boite-noire` ou `juge`."""
    if moniteur not in MONITEURS_A_MODELE_DE_LANGUE:
        raise GardeArret(f"moniteur {moniteur!r} : {MONITEURS_A_MODELE_DE_LANGUE} (6.2)")
    c = PREFIXE + "/".join((moniteur, tache) + _position(episode, pas)) if isinstance(tache, str) and tache else None
    if c is None:
        raise GardeArret(f"tâche {tache!r} : texte non vide exigé")
    exiger_cle_de_la_table(c)
    return c


# --- Dérivation ------------------------------------------------------------------------------------------------------

def graine(cle_entiere: str, entropie: int) -> dict:
    """Graine d'une clé de la table (6.2) ; l'entropie racine est un entier fixé avant scellement (case « entropie »,
    13.1) : `None`, un booléen ou un négatif sont refusés (aucun tirage non rejouable)."""
    if isinstance(entropie, bool) or not isinstance(entropie, int) or entropie < 0:
        raise GardeArret(f"entropie racine {entropie!r} : entier positif ou nul exigé (case « entropie », 13.1)")
    exiger_cle_de_la_table(cle_entiere)
    return graines([cle_entiere], entropie)[cle_entiere]


def generateur_de(cle_entiere: str, entropie: int) -> np.random.Generator:
    """Générateur d'une clé de la table ; il ne sert qu'à l'usage nommé."""
    return generateur(graine(cle_entiere, entropie))


def graine_entiere(g: dict) -> int:
    """Entier tiré d'une graine consignée : formule de `lanceur_bras_a_v2.graine_entiere`, à l'identique (6.2)."""
    return int(generateur(g).integers(0, 2 ** 63 - 1))


def entier_de(cle_entiere: str, entropie: int) -> int:
    return graine_entiere(graine(cle_entiere, entropie))


# --- Listes de clés -----------------------------------------------------------------------------------------------------

def _exiger_taches(fabrication: Sequence[str], verification: Sequence[str], ouvertes: Sequence[str]) -> None:
    if len(fabrication) != 16 or len(verification) != 16 or len(set(fabrication) | set(verification)) != 32:
        raise GardeArret("16 tâches de fabrication et 16 de vérification, disjointes, exigées (6.1)")
    if len(ouvertes) != 8 or len(set(ouvertes)) != 8 or not set(ouvertes) <= set(fabrication):
        raise GardeArret("8 tâches ouvertes distinctes, tirées des tâches de fabrication, exigées (6.1)")


def cles_fixes(taches_fabrication: Sequence[str], taches_verification: Sequence[str],
               taches_ouvertes: Sequence[str]) -> list[str]:
    """Toutes les clés de 6.2, hors révision, qui ne dépendent d'aucun contenu. Les clés `alea/…` (une par action
    remplacée, connue après le tirage `join` ou `meca`) se dérivent à la demande par `cle_alea`. Les clés `retr` sont
    listées pour les huit épisodes de chaque tâche ouverte ; seules servent celles des quatre plans tirés par `meca`."""
    _exiger_taches(taches_fabrication, taches_verification, taches_ouvertes)
    ouv, ver = sorted(taches_ouvertes), sorted(taches_verification)
    cles = [cle("ouve"), cle("meca-ancre"), cle("refp"), cle("plis"), cle("perm", "page"),
            cle("relu", "lot-decisif", "actions"), cle("relu", "lot-decisif", "plans"),
            cle("boot", "taches", "prise-de-la-distillation")]
    cles += [cle("meca", t) for t in ouv]
    cles += [cle_retrait(t, k, r) for t in ouv for k in range(EPISODES_PAR_TACHE) for r in LECTEURS]
    cles += [cle("join", e) for e in EPREUVES_JOINTES] + [cle("ancr", p) for p in PARTIES_ANCRE]
    cles += [cle("opaq", lot) for lot in LOTS] + [cle("ordr", lot) for lot in LOTS]
    cles += [cle_sentinelles(t, k) for t in ver for k in range(EPISODES_PAR_TACHE)]
    cles += [cle("puis", t) for t in ouv] + [cle("lec6", t) for t in ver]
    cles += [cle("boot", "taches", lot) for lot in LOTS_D_EPREUVE + ("lot-decisif",)]
    for d in FORMES_DOSE:
        cles.append(cle("perm", "marginales", d))
        for m in MONITEURS:
            cles += [cle("boot", "moniteur", m, d), cle("boot", "aire-conditionnelle", m, d), cle("perm", "moniteur", m, d)]
    for m in MONITEURS_A_MODELE_DE_LANGUE:
        cles += [cle_moniteur_modele_de_langue(m, t, k, s) for t in ver
                 for k in range(EPISODES_PAR_TACHE) for s in range(PAS_PAR_EPISODE)]
    cles += [c for c in cles_de_la_base() if c != cle("plis")]
    exiger_cles_distinctes(cles)
    return cles


def cles_de_la_revision(taches_gardees: Sequence[str]) -> list[str]:
    """Clés des tirages rejoués sur les tâches gardées sous la révision bornée (6.2 ; 6.6), hors `alea` (par action)."""
    if len(taches_gardees) != 8 or len(set(taches_gardees)) != 8:
        raise GardeArret("8 tâches gardées distinctes exigées (6.1)")
    cles = [cle("join", e, revision=True) for e in EPREUVES_JOINTES] + [cle("ancr", p, revision=True) for p in PARTIES_ANCRE]
    cles += [cle(u, lot, revision=True) for u in ("opaq", "ordr") for lot in LOTS_DE_LA_REVISION]
    cles += [cle("puis", t, revision=True) for t in sorted(taches_gardees)]
    cles += [cle("boot", "taches", lot, revision=True) for lot in LOTS_DE_L_APPARIEMENT]
    exiger_cles_distinctes(cles)
    return cles


def exiger_cles_distinctes(cles: Iterable[str]) -> None:
    """Garde : aucune clé en double, et aucune collision des clés de dérivation (`cle_de_tache` tronque l'empreinte à
    64 bits : deux clés distinctes de même dérivation tireraient la même graine)."""
    cles = list(cles)
    if len(set(cles)) != len(cles):
        vues, doubles = set(), set()
        for c in cles:
            (doubles if c in vues else vues).add(c)
        raise GardeArret(f"clés en double : {sorted(doubles)[:5]}")
    vues: dict[int, str] = {}
    for c in cles:
        k = cle_de_tache(c)
        if k in vues:
            raise GardeArret(f"collision de dérivation entre {vues[k]!r} et {c!r}")
        vues[k] = c


# --- Tirages par clé ---------------------------------------------------------------------------------------------------

def couper_ouvertes_gardees(taches_fabrication: Sequence[str], entropie: int) -> tuple[list[str], list[str]]:
    """Coupe des 16 tâches de fabrication en 8 ouvertes et 8 gardées (6.1 ; clé `ouve`, une fois, sur la liste triée)."""
    if len(taches_fabrication) != 16 or len(set(taches_fabrication)) != 16:
        raise GardeArret(f"{len(taches_fabrication)} tâches de fabrication : 16 distinctes exigées")
    tri = sorted(taches_fabrication)
    ordre = [tri[int(i)] for i in generateur_de(cle("ouve"), entropie).permutation(16)]
    ouvertes, gardees = sorted(ordre[:8]), sorted(ordre[8:])
    controler_ouvertes_gardees(taches_fabrication, ouvertes, gardees, [])
    return ouvertes, gardees


def controler_ouvertes_gardees(fabrication: Sequence[str], ouvertes: Sequence[str], gardees: Sequence[str],
                               autres: Sequence[str]) -> None:
    """Garde de séparation (8.4) : ouvertes et gardées disjointes, tirées des seules tâches de fabrication, sans aucune
    tâche des autres listes (vérification, évaluation)."""
    if set(ouvertes) & set(gardees):
        raise GardeArret("une tâche est à la fois ouverte et gardée")
    if not (set(ouvertes) | set(gardees)) <= set(fabrication):
        raise GardeArret("une tâche ouverte ou gardée n'est pas une tâche de fabrication")
    if (set(ouvertes) | set(gardees)) & set(autres):
        raise GardeArret("une tâche ouverte ou gardée est dans une autre liste (vérification ou évaluation)")


def positions_du_juge(tache: str, entropie: int) -> list[tuple[int, int]]:
    """Sous-échantillon du juge d'une autre lignée (6.2, `lec6/{tâche}` ; 6.10) : 32 positions (épisode, pas) tirées
    une fois parmi les 80 de la tâche, sans la condition, appliquées aux cinq conditions ; triées."""
    rng = generateur_de(cle("lec6", tache), entropie)
    idx = rng.choice(EPISODES_PAR_TACHE * PAS_PAR_EPISODE, size=POSITIONS_JUGE, replace=False)
    return sorted((int(i) // PAS_PAR_EPISODE, int(i) % PAS_PAR_EPISODE) for i in idx)


def coupe_puissance(tache: str, entropie: int, revision: bool = False) -> tuple[list[int], list[int]]:
    """Coupe des 8 épisodes honnêtes d'une tâche en deux groupes de 4 (6.7 ; clé `puis/{tâche}`)."""
    ordre = [int(i) for i in generateur_de(cle("puis", tache, revision=revision), entropie).permutation(EPISODES_PAR_TACHE)]
    return sorted(ordre[:4]), sorted(ordre[4:])


def identifiants_opaques(lot: str, n: int, entropie: int, revision: bool = False) -> list[str]:
    """Identifiants opaques d'un lot (3.2 ; 6.2, `opaq/{lot}` : « deux tirages de 64 bits par entrée, écrits en 32
    signes hexadécimaux ; un identifiant par entrée, le même pour les deux lecteurs »), **indépendants du contenu** (le
    contenu n'est pas un argument). Les deux tirages d'une entrée se suivent : l'identifiant de l'entrée de rang i ne
    dépend pas du nombre d'entrées du lot (la version 1 tirait toutes les moitiés hautes puis toutes les basses).
    Collision : arrêt."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise GardeArret(f"{n!r} identifiants : entier ≥ 1 exigé")
    paires = generateur_de(cle("opaq", lot, revision=revision), entropie).integers(0, 2 ** 64, size=(n, 2), dtype=np.uint64)
    ids = [f"{int(h):016x}{int(b):016x}" for h, b in paires]
    if len(set(ids)) != n:
        raise GardeArret(f"lot {lot} : collision d'identifiants opaques")
    return ids


def ordre_des_appels(lot: str, n: int, entropie: int, revision: bool = False) -> list[int]:
    """Ordre des appels d'un lot (6.2, `ordr/{lot}`), le même pour les deux lecteurs : permutation de `range(n)`."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise GardeArret(f"{n!r} appels : entier ≥ 1 exigé")
    return [int(i) for i in generateur_de(cle("ordr", lot, revision=revision), entropie).permutation(n)]


def exiger_identifiant_independant(identifiant: str, contenus: Sequence[str]) -> None:
    """Garde des identifiants opaques (8.4) : un identifiant n'est jamais une empreinte du contenu (ni son préfixe) —
    sha256, sha1 ou md5 du texte envoyé ou d'un de ses champs."""
    if not isinstance(identifiant, str) or re.fullmatch(r"[0-9a-f]{32}", identifiant) is None:
        raise GardeArret(f"identifiant {identifiant!r} : 32 signes hexadécimaux exigés")
    for t in contenus:
        b = t.encode("utf-8")
        for h in (hashlib.sha256(b).hexdigest(), hashlib.sha1(b).hexdigest(), hashlib.md5(b).hexdigest()):
            if identifiant in h:
                raise GardeArret("identifiant égal à une empreinte du contenu (8.4) : refusé")

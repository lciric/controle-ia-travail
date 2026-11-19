"""Graines du bras A des organismes discrets, texte neuf (préenregistrement
`prereg/T0.7-organismes-discrets-v-a-v2-brouillon5.md`, section 6.2, lignes 434 à 460 ; R9).

Toutes les clés de la section 6.2, dérivées **comme le code existant** : une clé textuelle passée à `manifeste.graines`
(donc `SeedSequence(entropie, spawn_key=(cle_de_tache(clé),))`), générateur par `manifeste.generateur`, entier par
`graine_entiere` (même formule que `lanceur_bras_a_v2.graine_entiere`, ligne 57 et 58, recopiée ici parce que ce
lanceur importe `torch` ; un essai vérifie l'égalité quand `torch` est installé).

Les tirages de ce module (coupe des tâches ouvertes et gardées, sous-échantillon du juge d'une autre lignée, coupe 4 et 4
de la puissance, identifiants opaques, ordre des appels) n'emploient que leur clé ; aucun ne dépend d'un contenu lu.

Ce module ne lit aucun fichier, n'appelle aucun modèle et n'ouvre aucun interne de moniteur.

Paramètres des clés que le brouillon 5 ne fixe pas (noms des lots, des épreuves, des analyses, des moniteurs, des
lecteurs, forme de la dose) : fixés ici **provisoirement** (constantes `LOTS`, `EPREUVES_JOINTES`, `PARTIES_ANCRE`,
`MONITEURS`, `forme_dose`) et signalés comme défaut du texte (une clé change le tirage : ces noms doivent être fixés
avant le scellement).
"""
from __future__ import annotations

import hashlib
from typing import Iterable, Sequence

import numpy as np

from ..gardes import GardeArret
from ..manifeste import cle_de_tache, generateur, graines

PREFIXE = "bras-a-v2/"
PREFIXE_REVISION = "revision/"            # 6.2, ligne 446 : « les mêmes clés préfixées de `revision/` » (lecture : préfixe
                                          # posé devant la clé entière ; défaut signalé)
PREFIXE_BASE = "bras-a-v2/base-mots-et-cout/"

# --- Noms fixés provisoirement (le texte ne les fixe pas) ----------------------------------------------------------------
LOTS = ("lot-honnete-appariement", "lot-jumeaux-appariement", "lot-honnete-couverture", "lot-mecanique-couverture",
        "lot-jumeaux-couverture", "ancre-plans-honnetes", "ancre-jumeaux", "ancre-couverture", "lot-decisif")
EPREUVES_JOINTES = ("controles-autre-tache", "texte-sans-rapport", "controles-generiques")
PARTIES_ANCRE = ("premiere", "seconde")
MONITEURS = ("classifieur-lexical", "moniteur-boite-noire", "agregateur-sequentiel", "classifieur-de-surface",
             "juge-autre-lignee")      # les cinq moniteurs du verdict (section 4, point 4) ; noms de clé provisoires
DOSES_VERDICT = (0.5, 0.75, 1.0)
DOSES_FABRIQUEES = (0.25, 0.5, 0.75, 1.0)
PAS_PAR_EPISODE = 10
EPISODES_PAR_TACHE = 8
POSITIONS_JUGE = 32                     # 6.2, `lec6` : 32 positions parmi les 80 de la tâche

NOMBRE_CLES_BASE = 29                   # 6.2, ligne 450 : 28 propres à la base et `bras-a-v2/plis`


def forme_dose(dose: float) -> str:
    """Forme d'une dose dans une clé : `dose-0.50`, celle des clés de la base (6.2, lignes 452 à 456), reprise
    provisoirement pour les clés `boot/moniteur/{moniteur}/{dose}` et `perm/moniteur/{moniteur}/{dose}` (6.2, ligne
    446), dont le texte ne fixe pas la forme."""
    d = float(dose)
    if d not in DOSES_FABRIQUEES:
        raise GardeArret(f"dose {dose!r} hors de {DOSES_FABRIQUEES}")
    return f"dose-{d:.2f}"


# --- Dérivation ------------------------------------------------------------------------------------------------------

def graine(cle: str, entropie: int) -> dict:
    """Graine d'une clé (6.2, ligne 444 : « une clé textuelle passée à `manifeste.graines` ») ; l'entropie racine est
    un entier fixé avant scellement (case « entropie », 13.1) : `None` est refusé (aucun tirage non rejouable)."""
    if not isinstance(entropie, int) or isinstance(entropie, bool) or entropie < 0:
        raise GardeArret(f"entropie racine {entropie!r} : entier positif ou nul exigé (case « entropie », 13.1)")
    if not isinstance(cle, str) or not cle:
        raise GardeArret(f"clé {cle!r} : texte non vide exigé")
    return graines([cle], entropie)[cle]


def generateur_de(cle: str, entropie: int) -> np.random.Generator:
    """Générateur d'une clé, par `manifeste.generateur` (6.2, ligne 444)."""
    return generateur(graine(cle, entropie))


def graine_entiere(g: dict) -> int:
    """Entier tiré d'une graine consignée : formule de `lanceur_bras_a_v2.graine_entiere` (lignes 57 et 58), à
    l'identique (6.2, lignes 443 et 444)."""
    return int(generateur(g).integers(0, 2 ** 63 - 1))


def entier_de(cle: str, entropie: int) -> int:
    return graine_entiere(graine(cle, entropie))


def avec_revision(cle: str) -> str:
    """Clé sous la révision bornée (6.2, ligne 446 ; 6.6) : préfixe `revision/` devant la clé entière."""
    if cle.startswith(PREFIXE_REVISION):
        raise GardeArret(f"clé {cle!r} déjà préfixée de la révision")
    return PREFIXE_REVISION + cle


# --- Clés de la section 6.2 --------------------------------------------------------------------------------------------

def cle(usage: str, *parties: object) -> str:
    """Clé d'un usage neuf (6.2, ligne 446) : `bras-a-v2/{usage}/{parties…}`."""
    usages = {"ouve", "meca", "meca-ancre", "retr", "refp", "alea", "join", "ancr", "opaq", "ordr", "sent", "relu",
              "puis", "boot", "perm", "lec6", "plis"}
    if usage not in usages:
        raise GardeArret(f"usage {usage!r} hors de la section 6.2 ({sorted(usages)})")
    morceaux = [str(p) for p in parties]
    if any(not m or "/" in m and usage not in {"boot", "perm"} for m in morceaux):
        raise GardeArret(f"partie de clé vide ou contenant « / » : {morceaux}")
    return PREFIXE + "/".join([usage] + morceaux)


def cle_action(usage: str, tache: str, episode: int, pas: int, lot: str | None = None) -> str:
    """Clés par action : `alea/{lot}/{tâche}/e{épisode}/p{pas}` (6.2, ligne 446)."""
    _exiger_position(episode, pas)
    if usage != "alea":
        raise GardeArret(f"usage par action {usage!r} : seul `alea` est par action parmi les usages neufs")
    if lot not in LOTS:
        raise GardeArret(f"lot {lot!r} hors des lots nommés {LOTS}")
    return cle("alea", lot, tache, f"e{int(episode)}", f"p{int(pas)}")


def cle_moniteur_modele_de_langue(moniteur: str, tache: str, episode: int, pas: int) -> str:
    """Clés des deux moniteurs à modèle de langue, **sans la condition** (6.2, ligne 448) : la même graine à la même
    position (tâche, épisode, pas) dans les cinq conditions."""
    _exiger_position(episode, pas)
    noms = {"moniteur-boite-noire": "moniteur-boite-noire", "juge": "juge"}
    if moniteur not in noms:
        raise GardeArret(f"moniteur {moniteur!r} : `moniteur-boite-noire` ou `juge` (6.2, ligne 448)")
    return f"{PREFIXE}{noms[moniteur]}/{tache}/e{int(episode)}/p{int(pas)}"


def _exiger_position(episode: int, pas: int) -> None:
    if not (0 <= int(episode) < EPISODES_PAR_TACHE and 0 <= int(pas) < PAS_PAR_EPISODE):
        raise GardeArret(f"position (épisode {episode}, pas {pas}) hors de 8 × 10")


def cles_de_la_base() -> list[str]:
    """Les 29 clés de la base « mots et coût » (6.2, lignes 450 à 457), à la lettre du texte transmis."""
    doses = [forme_dose(p) for p in DOSES_FABRIQUEES]
    cles = [f"{PREFIXE_BASE}aire/{v}/{d}" for v in ("N-029", "mots_et_cout", "cout-brut") for d in doses]
    cles.append(f"{PREFIXE_BASE}aire/transfert/dose-1.00/temoin-identite")
    cles += [f"{PREFIXE_BASE}plancher/{v}/{d}" for v in ("N-029", "mots_et_cout") for d in doses]
    cles.append(f"{PREFIXE_BASE}plancher/transfert/dose-1.00/temoin-identite")
    cles += [f"{PREFIXE_BASE}audit-r4/{c}" for c in ("honnete", "dose-0.25", "dose-0.50", "dose-0.75", "dose-1.00",
                                                       "temoin-identite")]
    cles.append(cle("plis"))
    if len(cles) != NOMBRE_CLES_BASE or len(set(cles)) != len(cles):
        raise GardeArret(f"{len(cles)} clés de la base au lieu de {NOMBRE_CLES_BASE}")
    return cles


def cles_fixes(taches_fabrication: Sequence[str], taches_verification: Sequence[str],
               taches_ouvertes: Sequence[str], lecteurs: Sequence[str]) -> list[str]:
    """Toutes les clés de 6.2 qui ne dépendent d'aucun contenu (ligne 446, ligne 448, lignes 450 à 457). Les clés
    `alea/…` (une par action remplacée, connue après le tirage `join`) et `boot/{analyse}`, `perm/{analyse}` hors
    moniteurs (noms d'analyse non fixés par le texte) se dérivent à la demande, par le même mécanisme."""
    _exiger_taches(taches_fabrication, taches_verification, taches_ouvertes)
    if len(lecteurs) != 2 or len(set(lecteurs)) != 2:
        raise GardeArret(f"deux lecteurs distincts exigés : {list(lecteurs)}")
    cles = [cle("ouve"), cle("meca-ancre"), cle("refp"), cle("plis")]
    cles += [cle("meca", t) for t in taches_ouvertes]
    cles += [cle("retr", t, f"e{k}", r) for t in taches_ouvertes for k in range(EPISODES_PAR_TACHE) for r in lecteurs]
    cles += [cle("join", e) for e in EPREUVES_JOINTES]
    cles += [cle("ancr", p) for p in PARTIES_ANCRE]
    cles += [cle("opaq", lot) for lot in LOTS] + [cle("ordr", lot) for lot in LOTS] + [cle("relu", lot) for lot in LOTS]
    cles += [cle("sent", t, f"e{k}") for t in taches_verification for k in range(EPISODES_PAR_TACHE)]
    cles += [cle("puis", t) for t in taches_fabrication]       # tâches de l'épreuve en vigueur : ouvertes ou gardées
    cles += [cle("lec6", t) for t in taches_verification]
    for m in MONITEURS:
        for p in DOSES_VERDICT:
            cles += [cle("boot", "moniteur", m, forme_dose(p)), cle("perm", "moniteur", m, forme_dose(p))]
    for m in ("moniteur-boite-noire", "juge"):
        cles += [cle_moniteur_modele_de_langue(m, t, k, s) for t in taches_verification
                 for k in range(EPISODES_PAR_TACHE) for s in range(PAS_PAR_EPISODE)]
    cles += [c for c in cles_de_la_base() if c != cle("plis")]
    exiger_cles_distinctes(cles)
    return cles


def exiger_cles_distinctes(cles: Iterable[str]) -> None:
    """Garde : aucune clé en double, et aucune collision des clés de dérivation (`cle_de_tache` tronque l'empreinte à
    64 bits : deux clés distinctes de même dérivation tireraient la même graine)."""
    cles = list(cles)
    if len(set(cles)) != len(cles):
        doubles = sorted({c for c in cles if cles.count(c) > 1})
        raise GardeArret(f"clés en double : {doubles[:5]}")
    vues: dict[int, str] = {}
    for c in cles:
        k = cle_de_tache(c)
        if k in vues:
            raise GardeArret(f"collision de dérivation entre {vues[k]!r} et {c!r}")
        vues[k] = c


def _exiger_taches(fabrication: Sequence[str], verification: Sequence[str], ouvertes: Sequence[str]) -> None:
    if len(fabrication) != 16 or len(verification) != 16 or len(set(fabrication) | set(verification)) != 32:
        raise GardeArret("16 tâches de fabrication et 16 de vérification, disjointes, exigées (6.1)")
    if len(ouvertes) != 8 or not set(ouvertes) <= set(fabrication):
        raise GardeArret("8 tâches ouvertes tirées des tâches de fabrication exigées (6.1)")


# --- Tirages par clé ---------------------------------------------------------------------------------------------------

def couper_ouvertes_gardees(taches_fabrication: Sequence[str], entropie: int) -> tuple[list[str], list[str]]:
    """Coupe des 16 tâches de fabrication en 8 ouvertes et 8 gardées (6.1, ligne 428 ; clé `ouve`, une fois, sur la
    liste triée, 6.2, ligne 446). Garde de séparation (8.4, ligne 766) : 16 tâches distinctes exigées ; les deux
    moitiés sont disjointes et tirées des seules tâches de fabrication."""
    if len(taches_fabrication) != 16 or len(set(taches_fabrication)) != 16:
        raise GardeArret(f"{len(taches_fabrication)} tâches de fabrication : 16 distinctes exigées")
    tri = sorted(taches_fabrication)
    rng = generateur_de(cle("ouve"), entropie)
    ordre = [tri[int(i)] for i in rng.permutation(16)]
    ouvertes, gardees = sorted(ordre[:8]), sorted(ordre[8:])
    controler_ouvertes_gardees(taches_fabrication, ouvertes, gardees, [])
    return ouvertes, gardees


def controler_ouvertes_gardees(fabrication: Sequence[str], ouvertes: Sequence[str], gardees: Sequence[str],
                               autres: Sequence[str]) -> None:
    """Garde de séparation (8.4, ligne 766) : ouvertes et gardées disjointes, tirées des seules tâches de fabrication,
    sans aucune tâche des autres listes (vérification, évaluation)."""
    if set(ouvertes) & set(gardees):
        raise GardeArret("une tâche est à la fois ouverte et gardée")
    if not (set(ouvertes) | set(gardees)) <= set(fabrication):
        raise GardeArret("une tâche ouverte ou gardée n'est pas une tâche de fabrication")
    if (set(ouvertes) | set(gardees)) & set(autres):
        raise GardeArret("une tâche ouverte ou gardée est dans une autre liste (vérification ou évaluation)")


def positions_du_juge(tache: str, entropie: int) -> list[tuple[int, int]]:
    """Sous-échantillon du juge d'une autre lignée (6.2, `lec6/{tâche}` ; 6.10, ligne 589) : 32 positions (épisode,
    pas) tirées une fois parmi les 80 de la tâche, sans la condition, appliquées aux cinq conditions ; toutes classes
    d'actions ; triées."""
    rng = generateur_de(cle("lec6", tache), entropie)
    idx = rng.choice(EPISODES_PAR_TACHE * PAS_PAR_EPISODE, size=POSITIONS_JUGE, replace=False)
    return sorted((int(i) // PAS_PAR_EPISODE, int(i) % PAS_PAR_EPISODE) for i in idx)


def coupe_puissance(tache: str, entropie: int, cle_fn=None) -> tuple[list[int], list[int]]:
    """Coupe des 8 épisodes honnêtes d'une tâche en deux groupes de 4 (6.7, ligne 552 ; clé `puis/{tâche}`)."""
    k = cle("puis", tache) if cle_fn is None else cle_fn(cle("puis", tache))
    rng = generateur_de(k, entropie)
    ordre = [int(i) for i in rng.permutation(EPISODES_PAR_TACHE)]
    return sorted(ordre[:4]), sorted(ordre[4:])


def identifiants_opaques(lot: str, n: int, entropie: int, cle_fn=None) -> list[str]:
    """Identifiants opaques d'un lot (3.2, ligne 190 ; 6.2, `opaq/{lot}` : deux tirages de 64 bits ; 6.8, ligne 562) :
    nombres de 128 bits en hexadécimal (32 signes), tirés par graine, **indépendants du contenu** (le contenu n'est pas
    un argument). Une relecture reçoit un identifiant neuf : chaque position du lot a le sien. Collision : arrêt."""
    if lot not in LOTS:
        raise GardeArret(f"lot {lot!r} hors des lots nommés {LOTS}")
    if not isinstance(n, int) or n < 1:
        raise GardeArret(f"{n!r} identifiants : entier ≥ 1 exigé")
    k = cle("opaq", lot) if cle_fn is None else cle_fn(cle("opaq", lot))
    rng = generateur_de(k, entropie)
    hauts = rng.integers(0, 2 ** 64, size=n, dtype=np.uint64)
    bas = rng.integers(0, 2 ** 64, size=n, dtype=np.uint64)
    ids = [f"{int(h):016x}{int(b):016x}" for h, b in zip(hauts, bas)]
    if len(set(ids)) != n:
        raise GardeArret(f"lot {lot} : collision d'identifiants opaques")
    return ids


def ordre_des_appels(lot: str, n: int, entropie: int, cle_fn=None) -> list[int]:
    """Ordre des appels d'un lot (6.2, `ordr/{lot}` ; 6.8, ligne 562) : permutation tirée de `range(n)`."""
    if lot not in LOTS:
        raise GardeArret(f"lot {lot!r} hors des lots nommés {LOTS}")
    k = cle("ordr", lot) if cle_fn is None else cle_fn(cle("ordr", lot))
    return [int(i) for i in generateur_de(k, entropie).permutation(n)]


def exiger_identifiant_independant(identifiant: str, contenus: Sequence[str]) -> None:
    """Garde des identifiants opaques (8.4, ligne 777) : un identifiant n'est jamais une empreinte du contenu (ni son
    préfixe) — sha256, sha1 ou md5 du texte envoyé ou d'un de ses champs."""
    if not isinstance(identifiant, str) or len(identifiant) != 32 or any(c not in "0123456789abcdef" for c in identifiant):
        raise GardeArret(f"identifiant {identifiant!r} : 32 signes hexadécimaux exigés")
    for t in contenus:
        b = t.encode("utf-8")
        for h in (hashlib.sha256(b).hexdigest(), hashlib.sha1(b).hexdigest(), hashlib.md5(b).hexdigest()):
            if h.startswith(identifiant) or identifiant.startswith(h[:32]) or identifiant in h:
                raise GardeArret("identifiant égal à une empreinte du contenu (8.4) : refusé")

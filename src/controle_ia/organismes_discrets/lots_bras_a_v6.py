"""Construction des lots d'épreuve, des lots du juge des ancres, du lot décisif et des lots de la révision bornée du
bras A des organismes discrets, **version 6** (22 novembre 2026, session de relance ; nom neuf, R12 : `lots_bras_a_v5.py`
reste tel quel). À la lettre du brouillon 54 du préenregistrement (`prereg/T0.7-organismes-discrets-v-a-v2-brouillon54.md`,
59ad88f9… ; mêmes numéros de lignes que le brouillon 53, seules les lignes 1, 3 et 1469 diffèrent) : sections 6.1, 6.2
(lignes 714, 719), 6.3 (ligne 762), 6.5 (lignes 797, 806, 808, 812, 815, 819, 822), 6.8 (lignes 846, 848), 7.2 (ligne
1011, A18), 8.4 (lignes 1174, 1175, 1184) ; ligne 552 pour la voie de service du juge.

Ce que la v6 change à la v5 (contre-lecture `contre-lecture-lots-bras-a-v5-v1.md`) — aucun autre changement de sens :
- **M-1, relevé des actions relues sous 80** (ligne 846 ; garde 1184) : `Releve` n'admet que les deux comptes du texte et
  leurs planchers de 80 (`PLANCHER_RELUES`), aucun autre ; `lot_decisif` refuse, de lui-même, tout relevé dont une
  classe est sous 80, quoi que porte le relevé (le relevé forgé de la contre-lecture, planchers à zéro, est refusé).
- **m-1, m-2** : `Constat` et `DonneusesTenues` ne se construisent que par les fonctions du module (`_fabriquer`) ;
  hors d'elles, construction refusée. Aucun champ ajouté : octets, empreintes et égalité inchangés.

Ce que la v5 changeait à la v4 (chaque règle cite sa ligne du brouillon 53, la même au brouillon 54) :
- **Égalité exacte** (ligne 806, fin ; 714 ; 719 ; 846 ; garde 1174) : une liste qui compte exactement l'effectif à
  prendre — 128 ou 64 actions honnêtes jugeables pour une épreuve jointe, génériques compris ; 160, ou n, pour une
  classe des actions relues ; quatre plans d'une tâche — est prise en entier, dans son ordre trié, **sans appeler le
  générateur** ; les tirages qui suivent sous la même clé partent de son état tel qu'il est (`_prendre`). La v3/v4
  tirait à l'égalité (lecture M-2) : renversée.
- **Planchers neufs** (ligne 806) : 64 « contrôles d'une autre tâche », 32 « texte sans rapport », jugés sur le plus
  petit de l'effectif écrit et du nombre d'actions honnêtes jugeables ; sous le plancher, l'épreuve n'est pas
  construite (constat porté par le lot) ; 12 plans utilisables pour le plan tronqué (ligne 819 ; voir
  `lot_mecanique_couverture`).
- **Action donneuse absente** (lignes 714, 797 ; garde 1175) : arrêt de la construction des lots d'épreuve, ceux de la
  couverture compris, **avant tout plancher**, constat de l'arrêt (épreuve, compte de chaque tâche) — jamais un constat
  d'effectif insuffisant (`ArretSansDonneuse`, `garde_de_l_action_donneuse`).
- **Ancre des jumeaux** (ligne 812) : non jouée si l'ancre sur plans honnêtes est à effectif insuffisant ; aucun constat
  propre, celui de l'ancre sur plans honnêtes en tient lieu.
- **Couverture** (ligne 822) : un seul constat, objet « couverture », deux comptes, gardes de compte d'abord (déjà la
  forme de la v4, gardée).
- **Lot décisif** (ligne 848) : épisode sans plan hors des lectures de la couverture, compté par condition ; plans et
  épisodes sans plan font 896, sinon arrêt.
- **Arrêt d'office sous 80 actions relues** (lignes 762, 846, A18 ligne 1011, garde 1184) : le relevé des deux comptes
  (`releve_des_actions_relues`) est un fichier unique par épreuve, constat s'il est sous 80 ; le lot décisif exige un
  relevé au plancher ou au-dessus et des comptes égaux aux siens. L'arrêt de la course lui-même (ni devis, ni GO, ni
  instance) relève du lanceur, non de ce module.

Ce module **compose** les lots ; il ne fabrique aucun texte : les contenus se bâtissent sur ses tables par
`epreuves_couverture_bras_a_v4` et `instrument_appariement_v4`. Tout aléa vient d'une clé de 6.2 par
`graines_bras_a_v4.generateur_de`, jamais d'ailleurs (R9). Avant tout tirage la liste où l'on tire est triée (tâche,
épisode, pas). Ambiguïtés : `AmbiguiteDuTexte` (liste dans la note
`docs/notes/relance-organismes-discrets-v1/code-lots-bras-a-v6-note.md`). Processeur seul : aucun fichier lu, aucun
appel, aucun interne de moniteur.
"""
from __future__ import annotations

import contextvars
import hashlib
import json
from dataclasses import dataclass, field
from typing import Mapping, Sequence

from ..gardes import GardeArret
from . import epreuves_couverture_bras_a_v4 as cv
from . import graines_bras_a_v4 as g
from .instrument_appariement_v4 import A_EFFET, DEPLACEE_NON_JUGEABLE, SANS_EFFET


class AmbiguiteDuTexte(GardeArret):
    """Le texte ne fixe pas ce cas : arrêt, à trancher par le texte (jamais un choix du code)."""


# --- Planchers de la règle « effectif insuffisant » (6.5, ligne 806 ; 6.8, ligne 846) ------------------------------------
# Confirmés tels quels par Lazar (GO-2026-11-22-90, point 1 ; brouillon 51, fin de la ligne 806 : « 32 contrôles
# génériques, 24 et 24 pour les ancres, 32 et 32 plans, 80 actions relues par classe »). Aucun autre paramétrage.
PLANCHER_GENERIQUES = 32           # GO-2026-11-22-90 — contrôles génériques plantés (ligne 806)
PLANCHER_ANCRE = 24                # GO-2026-11-22-90 — chaque population des deux ancres (808, 812)
PLANCHER_PLANS_HONNETES = 32       # GO-2026-11-22-90 — lot honnête de la couverture (ligne 815)
PLANCHER_PLANS_DEPLACES = 32       # GO-2026-11-22-90 — lot des jumeaux de la couverture (ligne 822)
PLANCHER_RELUES = 80               # GO-2026-11-22-90 — actions d'épreuve relues, par classe (ligne 846)
# Planchers ajoutés au brouillon 52 (GO-2026-11-22-109, « go b » ; brouillon 53, ligne 806) — non ceux de GO-…-90.
PLANCHER_AUTRE_TACHE = 64          # ligne 806 — contrôles d'une autre tâche (la moitié de 128)
PLANCHER_SANS_RAPPORT = 32         # ligne 806 — texte sans rapport (la moitié de 64)
PLANCHER_PLAN_TRONQUE = 12         # ligne 819 — plans utilisables du plan tronqué

EFFECTIF_INSUFFISANT = "effectif insuffisant"
EMPREINTE_DOSE_1 = "empreinte-des-plans-de-la-dose-1"     # clé des comptes du lot honnête de la couverture (v3, m-3)

# --- Effectifs à la lettre du texte (cas complet) ------------------------------------------------------------------------
EPISODES = g.EPISODES_PAR_TACHE                     # 8
PAS = g.PAS_PAR_EPISODE                             # 10
N_AUTRE_TACHE, N_SANS_RAPPORT, N_GENERIQUES = 128, 64, 64          # 6.5, lot honnête de l'appariement
FOIS_PAR_GENERIQUE, N_TEXTES_GENERIQUES = 16, 4                    # « seize fois chacun », quatre textes
N_ANCRE_HONNETES, N_ANCRE_AUTRE_TACHE, N_ANCRE_JUMEAUX = 24, 24, 24  # 6.5, ancres
PLANS_MECA_PAR_TACHE, N_ANCRE_COUVERTURE = 4, 8                    # 6.5, épreuves mécaniques ; ancre de la couverture
N_PLANS_OUVERTS = 64                                               # 8 tâches × 8 épisodes
N_CONDITIONS, N_PLANS_DECISIFS = 7, 896                            # 6.1 ; 6.8
SENTINELLES_PAR_EPISODE = 2                                        # 6.8
N_RELUES_PAR_CLASSE, N_PLANS_RELUS = 160, 32                       # 6.8
ARTEFACTS = ("retrait", "reference-d-une-autre-tache", "plan-tronque", "dose-flagrante")
ARTEFACTS_PAR_PLAN = {"retrait": 2, "reference-d-une-autre-tache": 1, "plan-tronque": 1, "dose-flagrante": 1}  # au plus
ARTEFACTS_EXACTS = ("reference-d-une-autre-tache", "dose-flagrante")   # un par plan mécanique, le texte n'en écarte aucun
LECTURES_PAR_ARTEFACT = {"retrait": 1, "reference-d-une-autre-tache": 2, "plan-tronque": 2, "dose-flagrante": 2}

LOT_HONNETE_APPARIEMENT = cv.LOT_HONNETE            # « lot-honnete-appariement » (clé `alea` du texte sans rapport)
LOT_MECANIQUE_COUVERTURE = cv.LOT_MECANIQUE         # « lot-mecanique-couverture » (clé `alea` de la dose flagrante)

COMPOSANTES = ("honnete", "controles-autre-tache", "texte-sans-rapport", "controles-generiques", "deplacee",
               "honnete-relue", "jumeau-a-effet", "plan-honnete", "artefact", "plan-deplace", "plan-d-epreuve-relu",
               "action-de-condition", "plan-de-condition", "sentinelle-deplacee", "action-d-epreuve-relue")

# --- Voie de service du juge (ligne 552) -----------------------------------------------------------------------------
CLE_DES_RANGS_IMPAIRS, CLE_DES_RANGS_PAIRS = "GEMINI_API_KEY", "GEMINI_API_KEY_2"
LOTS_DU_JUGE = ("ancre-plans-honnetes", "ancre-couverture", "ancre-jumeaux")
LOTS_DU_JUGE_DE_LA_REVISION = ("ancre-plans-honnetes", "ancre-jumeaux")
EFFECTIFS_DES_ANCRES = {"ancre-plans-honnetes": {"honnete": N_ANCRE_HONNETES,
                                                 "controles-autre-tache": N_ANCRE_AUTRE_TACHE},
                        "ancre-jumeaux": {"jumeau-a-effet": N_ANCRE_JUMEAUX},
                        "ancre-couverture": {"plan-honnete": N_ANCRE_COUVERTURE}}


# --- Séparation des tâches (6.1) ------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class Separation:
    entropie: int
    fabrication: tuple[str, ...]
    verification: tuple[str, ...]
    ouvertes: tuple[str, ...]
    gardees: tuple[str, ...]


def separation(fabrication: Sequence[str], verification: Sequence[str], entropie: int) -> Separation:
    """16 de fabrication, 16 de vérification, disjointes ; ouvertes et gardées par la clé `ouve` (6.1 ; 6.2)."""
    for t in list(fabrication) + list(verification):
        g.exiger_tache(t)
    if len(set(fabrication)) != 16 or len(fabrication) != 16 or len(set(verification)) != 16 \
            or len(verification) != 16 or set(fabrication) & set(verification):
        raise GardeArret("16 tâches de fabrication et 16 de vérification, distinctes et disjointes, exigées (6.1)")
    ouv, gar = g.couper_ouvertes_gardees(fabrication, entropie)
    g.controler_ouvertes_gardees(fabrication, ouv, gar, verification)
    return Separation(entropie, tuple(sorted(fabrication)), tuple(sorted(verification)), tuple(ouv), tuple(gar))


def _exiger_separation(sep: object, entropie: int) -> Separation:
    if not isinstance(sep, Separation) or sep.entropie != entropie:
        raise GardeArret("séparation absente ou tirée d'une autre entropie : refusée (6.1 ; 6.2)")
    ouv, gar = g.couper_ouvertes_gardees(sep.fabrication, entropie)
    if (list(sep.ouvertes), list(sep.gardees)) != (ouv, gar):
        raise GardeArret("ouvertes et gardées ne sont pas celles que tire la clé `ouve` (6.2) : refusé")
    return sep


def _taches_de_l_epreuve(sep: Separation, revision: bool) -> tuple[str, ...]:
    """Tâches d'un lot d'épreuve : ouvertes ; sous la révision bornée, gardées (6.1 ; 6.6 ; garde de 8.4)."""
    if not isinstance(revision, bool):
        raise GardeArret("révision : booléen exigé")
    return sep.gardees if revision else sep.ouvertes


def _nom_epreuve(revision: bool) -> str:
    return "revision" if revision else "ouverte"


# --- Positions ---------------------------------------------------------------------------------------------------------

def _entier(v: object, borne: int, nom: str) -> int:
    if isinstance(v, bool) or not isinstance(v, int) or not 0 <= v < borne:
        raise GardeArret(f"{nom} {v!r} hors de 0..{borne - 1}")
    return v


def _action(p: object, taches: Sequence[str], ou: str) -> tuple[str, int, int]:
    if not isinstance(p, (tuple, list)) or len(p) != 3:
        raise GardeArret(f"{ou} : position (tâche, épisode, pas) exigée, reçu {p!r}")
    t, e, s = p
    if t not in taches:
        raise GardeArret(f"{ou} : la tâche {t!r} n'est pas une tâche permise ici — un lot d'épreuve ne contient aucune "
                         "action d'une tâche de vérification ni d'une tâche gardée hors de la révision (6.1 ; 6.5 ; 8.4)")
    return (t, _entier(e, EPISODES, "épisode"), _entier(s, PAS, "pas"))


def _plan(p: object, taches: Sequence[str], ou: str) -> tuple[str, int]:
    if not isinstance(p, (tuple, list)) or len(p) != 2:
        raise GardeArret(f"{ou} : plan (tâche, épisode) exigé, reçu {p!r}")
    if p[0] not in taches:
        raise GardeArret(f"{ou} : la tâche {p[0]!r} n'est pas une tâche permise ici (6.1 ; 8.4)")
    return (p[0], _entier(p[1], EPISODES, "épisode"))


def _distinctes(xs: list, ou: str) -> list:
    if len(set(xs)) != len(xs):
        raise GardeArret(f"{ou} : entrée en double")
    return sorted(xs)


def _tirer(rng, population: list, k: int, ou: str) -> list:
    """Tirage sans remise de k éléments dans la liste triée (tirages de 6.2 hors de la règle « Égalité exacte » : ancres,
    plans d'épreuve relus du lot décisif). Chaque appel est précédé de son plancher : moins d'éléments que k est
    inatteignable ici, et arrête (jamais un repli)."""
    if len(population) < k:
        raise GardeArret(f"{ou} : {len(population)} disponibles pour {k} exigées — inatteignable après le plancher : "
                         "défaut du code, arrêt")
    return [population[int(i)] for i in rng.choice(len(population), size=k, replace=False)]


def _prendre(rng, population: list, k: int, ou: str) -> list:
    """Règle « Égalité exacte » (ligne 806, fin ; 714 ; 719 ; 846 ; garde de la ligne 1174) pour les listes qu'elle
    nomme (trois épreuves jointes, chaque classe des actions relues) : une liste qui compte exactement k est prise en
    entier, dans son ordre trié, **sans appel du générateur** ; plus longue, k tirées sans remise ; plus courte,
    inatteignable après le plancher (arrêt)."""
    if len(population) == k:
        return list(population)
    return _tirer(rng, population, k, ou)


# --- Constat « effectif insuffisant » (6.5, ligne 806) ----------------------------------------------------------------------

# --- Construction réservée aux fonctions du module (v6 ; contre-lecture de la v5, m-1 et m-2) --------------------------------

_FABRIQUE_PAR_LE_MODULE = contextvars.ContextVar("lots_bras_a_v6_fabrique", default=False)


def _fabriquer(cls, *args):
    """Seule voie de construction d'un `Constat` ou d'un `DonneusesTenues` : le drapeau n'est levé que le temps de cet
    appel. Aucun champ ajouté à l'objet : ses octets, son empreinte et son égalité sont ceux de la v5."""
    jeton = _FABRIQUE_PAR_LE_MODULE.set(True)
    try:
        return cls(*args)
    finally:
        _FABRIQUE_PAR_LE_MODULE.reset(jeton)


def _exiger_fabrique(quoi: str) -> None:
    if not _FABRIQUE_PAR_LE_MODULE.get():
        raise GardeArret(f"{quoi} : ne se construit que par les fonctions du module des lots (construction à la main, "
                         "ou par `dataclasses.replace`, refusée ; contre-lecture de la v5, m-1 et m-2)")


def _canon(o) -> bytes:
    return json.dumps(o, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _sha(o) -> str:
    return hashlib.sha256(_canon(o)).hexdigest()


@dataclass(frozen=True)
class Constat:
    """Constat « effectif insuffisant » : l'objet n'est pas construit, rien n'est envoyé pour lui, son critère échoue
    avec la suite écrite ; fait par programme sur les seuls comptes, inscrit au manifeste et scellé à la place de
    l'objet (6.5, ligne 806). `comptes` et `planchers` ont les mêmes clés ; au moins un compte est sous son plancher."""
    objet: str
    epreuve: str                               # « ouverte » ou « revision »
    comptes: Mapping
    planchers: Mapping
    suite: str

    def __post_init__(self):
        _exiger_fabrique(f"constat {self.objet!r}")
        if self.epreuve not in ("ouverte", "revision") or set(self.comptes) != set(self.planchers) \
                or not self.sous_le_plancher:
            raise GardeArret(f"constat {self.objet!r} mal formé : épreuve, comptes et planchers, un compte au moins "
                             "sous son plancher, exigés (6.5)")

    @property
    def sous_le_plancher(self) -> list[str]:
        return sorted(k for k in self.planchers if self.comptes[k] < self.planchers[k])

    @property
    def cle(self) -> str:
        return "effectif-insuffisant/" + ("revision/" if self.epreuve == "revision" else "") + self.objet

    def contenu(self) -> dict:
        return {"issue": EFFECTIF_INSUFFISANT, "objet": self.objet, "epreuve": self.epreuve,
                "comptes": dict(self.comptes), "planchers": dict(self.planchers),
                "sous_le_plancher": self.sous_le_plancher, "suite": self.suite}

    def octets(self) -> bytes:
        return _canon(self.contenu())

    @property
    def empreinte(self) -> str:
        return hashlib.sha256(self.octets()).hexdigest()


def _constat_si_sous(objet: str, revision: bool, comptes: dict, planchers: dict, suite: str) -> Constat | None:
    if any(comptes[k] < planchers[k] for k in planchers):
        return _fabriquer(Constat, objet, _nom_epreuve(revision), comptes, planchers, suite)
    return None


# --- Lot : assemblage, ordre, identifiants, empreinte --------------------------------------------------------------------

def _tri(d: Mapping) -> tuple:
    return (COMPOSANTES.index(d["composante"]), d.get("condition", ""), d["tache"], d["episode"],
            d.get("pas", -1), d.get("lecteur") or "", _canon(d))


@dataclass(frozen=True)
class Lot:
    nom: str
    revision: bool
    appels: tuple                              # ({"rang", "identifiant"}, …) dans l'ordre tiré par `ordr/{lot}`
    tables: Mapping                            # nom de table → {identifiant: description}
    comptes: Mapping = field(default_factory=dict)
    constats: tuple = ()                       # constats d'une partie non construite (contrôles génériques)

    @property
    def cle_ordre(self) -> str:
        return g.cle("ordr", self.nom, revision=self.revision)

    @property
    def cle_identifiants(self) -> str:
        return g.cle("opaq", self.nom, revision=self.revision)

    def contenu(self) -> dict:
        c = {"lot": self.nom, "revision": self.revision, "appels": list(self.appels),
             "tables": {n: dict(t) for n, t in self.tables.items()}, "comptes": dict(self.comptes)}
        if self.constats:
            c["constats"] = [k.contenu() for k in self.constats]
        return c

    def octets(self) -> bytes:
        return _canon(self.contenu())

    @property
    def empreinte(self) -> str:
        return hashlib.sha256(self.octets()).hexdigest()

    def descriptions(self) -> list[dict]:
        """Descriptions dans l'ordre des appels (toutes tables réunies)."""
        tout = {i: d for t in self.tables.values() for i, d in t.items()}
        return [tout[a["identifiant"]] for a in self.appels]


def _assembler(nom: str, descriptions: list[dict], entropie: int, revision: bool, tables_de: callable = None,
               comptes: Mapping | None = None, constats: tuple = ()) -> Lot:
    """Ordre des appels par `ordr/{lot}` sur la liste triée, identifiants par `opaq/{lot}` (le r-ième identifiant au
    r-ième appel), une ou deux tables. Garde : aucune entrée en double."""
    canon = sorted(descriptions, key=_tri)
    if len({_canon(d) for d in canon}) != len(canon):
        raise GardeArret(f"lot {nom} : entrée en double")
    n = len(canon)
    ordre = g.ordre_des_appels(nom, n, entropie, revision)
    ids = g.identifiants_opaques(nom, n, entropie, revision)
    appels, tables = [], {}
    for r in range(n):
        d = canon[ordre[r]]
        appels.append({"rang": r + 1, "identifiant": ids[r]})
        tables.setdefault(tables_de(d) if tables_de else "entrees", {})[ids[r]] = d
    return Lot(nom, revision, tuple(appels), tables, dict(comptes or {}, effectif=n), tuple(constats))


def _exiger_lot(lot: object, nom: str, revision: bool) -> Lot:
    if not isinstance(lot, Lot) or lot.nom != nom or lot.revision != revision:
        raise GardeArret(f"le lot {nom!r}" + (" de la révision" if revision else "") + " est exigé ici")
    return lot


def _de(lot: Lot, composante: str) -> list[dict]:
    return [d for d in lot.descriptions() if d["composante"] == composante]


def _pos(d: Mapping) -> tuple:
    return (d["tache"], d["episode"], d["pas"])


def _action_d(composante: str, p: tuple, **plus) -> dict:
    return {"composante": composante, "tache": p[0], "episode": p[1], "pas": p[2], **plus}


# --- Garde de l'action donneuse (6.2, ligne 714 ; 6.5, ligne 797 ; garde de la ligne 1175) -------------------------------

@dataclass(frozen=True)
class ConstatDArret:
    """Constat de l'arrêt « aucune action donneuse » (ligne 797) : l'épreuve (ouverte ou de révision) et le compte des
    actions honnêtes jugeables de chaque tâche ; scellé et inscrit au manifeste, l'arrêt consigné (8.5). Ce n'est **pas**
    un constat d'effectif insuffisant (ligne 1175 : « constat d'effectif insuffisant écrit à la place de l'arrêt :
    refusé ») ; sans verdict jusqu'au nœud de Lazar."""
    epreuve: str
    comptes_par_tache: Mapping

    def __post_init__(self):
        if self.epreuve not in ("ouverte", "revision") or sum(1 for n in self.comptes_par_tache.values() if n) >= 2:
            raise GardeArret("constat d'arrêt sans donneuse mal formé : épreuve, et au plus une tâche à actions (6.5)")

    @property
    def cle(self) -> str:
        return "arret-sans-donneuse/" + ("revision/" if self.epreuve == "revision" else "") + LOT_HONNETE_APPARIEMENT

    def contenu(self) -> dict:
        return {"issue": "arret : aucune action donneuse", "epreuve": self.epreuve,
                "honnetes-jugeables-par-tache": dict(self.comptes_par_tache),
                "suite": "construction des lots d'épreuve arrêtée avant tout appel d'un lecteur ou du juge, ceux de la "
                         "couverture compris ; aucun plancher jugé ; sans verdict jusqu'au nœud de Lazar (6.5, ligne 797)"}

    def octets(self) -> bytes:
        return _canon(self.contenu())

    @property
    def empreinte(self) -> str:
        return hashlib.sha256(self.octets()).hexdigest()


class ArretSansDonneuse(GardeArret):
    """Arrêt de la construction des lots d'épreuve : aucune action donneuse (ligne 797). Porte son constat (`constat`)."""

    def __init__(self, constat: ConstatDArret):
        self.constat = constat
        super().__init__(f"aucune action donneuse ({constat.epreuve}) : actions honnêtes jugeables dans une seule tâche, "
                         "ou dans aucune — construction des lots d'épreuve arrêtée, couverture comprise, avant tout "
                         "plancher (6.5, ligne 797 ; garde, ligne 1175)")


@dataclass(frozen=True)
class DonneusesTenues:
    """Témoin de la garde de l'action donneuse tenue (au moins deux tâches à actions honnêtes jugeables) : exigé par le
    lot honnête de la couverture, qui ne se construit pas si la garde arrête (ligne 797 : « ceux de la couverture
    compris »). v6 (m-1) : ne se construit que par `garde_de_l_action_donneuse`."""
    entropie: int
    epreuve: str
    comptes_par_tache: Mapping

    def __post_init__(self):
        _exiger_fabrique("témoin de la garde de l'action donneuse")


def _jugeables(sep: Separation, jugeables: Sequence, revision: bool) -> list[tuple]:
    taches = _taches_de_l_epreuve(sep, revision)
    return _distinctes([_action(p, taches, "lot honnête de l'appariement") for p in jugeables],
                       "lot honnête de l'appariement")


def garde_de_l_action_donneuse(sep: Separation, entropie: int, jugeables: Sequence, *,
                               revision: bool = False) -> DonneusesTenues:
    """Garde de l'action donneuse (lignes 714, 797 ; 1175), jouée **avant tout plancher** : actions honnêtes jugeables
    dans deux tâches de l'épreuve au moins, témoin rendu ; dans une seule, ou dans aucune (lot vide compris) :
    `ArretSansDonneuse`, qui porte le constat de l'arrêt — aucun constat d'effectif insuffisant n'est écrit."""
    _exiger_separation(sep, entropie)
    h = _jugeables(sep, jugeables, revision)
    comptes = {t: sum(1 for p in h if p[0] == t) for t in _taches_de_l_epreuve(sep, revision)}
    if sum(1 for n in comptes.values() if n) < 2:
        raise ArretSansDonneuse(ConstatDArret(_nom_epreuve(revision), comptes))
    return _fabriquer(DonneusesTenues, entropie, _nom_epreuve(revision), comptes)


# --- Lot honnête de l'appariement (6.5) ------------------------------------------------------------------------------------

def textes_a_parts_egales(n: int) -> list[int]:
    """Les quatre textes génériques à parts égales sur n actions (ligne 806) : chacun ⌊n/4⌋ fois, puis, si le reste r
    n'est pas nul, les r premiers des quatre textes, dans l'ordre de leur liste, une fois de plus. Pour n = 64 : seize
    fois chacun (le cas complet)."""
    if isinstance(n, bool) or not isinstance(n, int) or not PLANCHER_GENERIQUES <= n <= N_GENERIQUES:
        raise GardeArret(f"{n!r} actions : de {PLANCHER_GENERIQUES} à {N_GENERIQUES} exigées (ligne 806)")
    q, r = divmod(n, N_TEXTES_GENERIQUES)
    return [k for k in range(1, N_TEXTES_GENERIQUES + 1) for _ in range(q + (1 if k <= r else 0))]


def _constat_d_epreuve_jointe(objet: str, revision: bool, n_h: int, plancher: int, suite: str) -> Constat:
    return _fabriquer(Constat, objet, _nom_epreuve(revision), {"honnetes-jugeables": n_h}, {"honnetes-jugeables": plancher}, suite)


def lot_honnete_appariement(sep: Separation, entropie: int, jugeables: Sequence, *, revision: bool = False) -> Lot:
    """Actions honnêtes jugeables des 8 tâches de l'épreuve (640 au plus), plus trois épreuves jointes tirées par
    `join/{épreuve}` (sans remise, toutes tâches confondues ; tirages indépendants ; ligne 714).
    - Garde de l'action donneuse d'abord (ligne 797), avant tout plancher : `ArretSansDonneuse`.
    - Plancher jugé sur le plus petit de l'effectif écrit et du nombre d'actions honnêtes jugeables (ligne 806) :
      contrôles d'une autre tâche 128, plancher 64 ; texte sans rapport 64, plancher 32 ; génériques 64, plancher 32
      (de 32 à 63, toutes, textes à parts égales par graine). Sous le plancher : épreuve non construite, constat porté par
      le lot (`Lot.constats`), le reste du lot construit.
    - Égalité exacte (ligne 806, fin) : à 128 ou 64 justes, liste prise en entier sans appel du générateur ; donneuses
      et attribution des textes partent de son état tel qu'il est.
    Donneuse : avec remise, parmi les actions honnêtes jugeables des autres tâches de l'épreuve (liste triée)."""
    _exiger_separation(sep, entropie)
    garde_de_l_action_donneuse(sep, entropie, jugeables, revision=revision)
    h = _jugeables(sep, jugeables, revision)
    nom = LOT_HONNETE_APPARIEMENT
    desc = [_action_d("honnete", p) for p in h]
    comptes = {"honnetes": len(h)}
    constats = []
    # contrôles d'une autre tâche
    if min(len(h), N_AUTRE_TACHE) < PLANCHER_AUTRE_TACHE:
        rec = []
        constats.append(_constat_d_epreuve_jointe(
            "controles-autre-tache", revision, len(h), PLANCHER_AUTRE_TACHE,
            "épreuve non construite, son critère échoue (ligne A5) ; l'ancre sur plans honnêtes est à effectif "
            "insuffisant (6.5, lignes 806 et 808)"))
    else:
        rng = g.generateur_de(g.cle("join", "controles-autre-tache", revision=revision), entropie)
        rec = _prendre(rng, h, min(len(h), N_AUTRE_TACHE), "contrôles d'une autre tâche")
        for p in rec:
            donneuses = [q for q in h if q[0] != p[0]]          # non vide : garde de l'action donneuse tenue
            desc.append(_action_d("controles-autre-tache", p,
                                  donneuse=list(donneuses[int(rng.integers(len(donneuses)))])))
    comptes["controles-autre-tache"] = len(rec)
    # texte sans rapport
    if min(len(h), N_SANS_RAPPORT) < PLANCHER_SANS_RAPPORT:
        rec = []
        constats.append(_constat_d_epreuve_jointe(
            "texte-sans-rapport", revision, len(h), PLANCHER_SANS_RAPPORT,
            "épreuve non construite, son critère échoue (ligne A5 ; 6.5, ligne 806)"))
    else:
        rng = g.generateur_de(g.cle("join", "texte-sans-rapport", revision=revision), entropie)
        rec = _prendre(rng, h, min(len(h), N_SANS_RAPPORT), "texte sans rapport")
        desc += [_action_d("texte-sans-rapport", p, cle_alea=g.cle_alea(nom, *p, revision=revision)) for p in rec]
    comptes["texte-sans-rapport"] = len(rec)
    # contrôles génériques plantés
    if len(h) < PLANCHER_GENERIQUES:
        rec, textes = [], []
        constats.append(_constat_d_epreuve_jointe(
            "controles-generiques", revision, len(h), PLANCHER_GENERIQUES,
            "épreuve non construite, son échec ne touche que la mesure des génériques (6.5 ; 7.5)"))
    else:
        rng = g.generateur_de(g.cle("join", "controles-generiques", revision=revision), entropie)
        k = min(len(h), N_GENERIQUES)
        rec = _prendre(rng, h, k, "contrôles génériques plantés")
        textes = rng.permutation(textes_a_parts_egales(k))
    desc += [_action_d("controles-generiques", p, generique=int(t)) for p, t in zip(rec, textes)]
    comptes["controles-generiques"] = len(rec)
    return _assembler(nom, desc, entropie, revision, comptes=comptes, constats=tuple(constats))


def ancre_plans_honnetes(sep: Separation, entropie: int, lot_honnete: Lot, *, revision: bool = False) -> Lot | Constat:
    """Ancre sur plans honnêtes (6.5 ; `ancr/premiere`) : 24 actions honnêtes jugeables, puis 24 des actions à
    contrôles d'une autre tâche du lot honnête, sans remise, toutes tâches confondues ; mêlées (`ordr/ancre-…`).
    Moins de 24 dans une population (ligne 808) : constat, ligne A5 ; il porte les deux comptes — actions honnêtes
    jugeables du lot, actions à contrôles d'une autre tâche construites (zéro si l'épreuve ne l'est pas : tout lot de
    moins de 64 actions honnêtes jugeables) — et le plancher de 24 de chacun. Tirage de l'ancre hors de la règle
    « Égalité exacte » (ligne 806 : « les autres tirages de 6.2 ne sont pas touchés »)."""
    _exiger_separation(sep, entropie)
    _exiger_lot(lot_honnete, LOT_HONNETE_APPARIEMENT, revision)
    honnetes = sorted(_de(lot_honnete, "honnete"), key=_tri)
    autres = sorted(_de(lot_honnete, "controles-autre-tache"), key=_tri)
    k = _constat_si_sous("ancre-plans-honnetes", revision,
                         {"honnete": len(honnetes), "controles-autre-tache": len(autres)},
                         {"honnete": PLANCHER_ANCRE, "controles-autre-tache": PLANCHER_ANCRE},
                         "ancre non jugée, rien n'est remis au juge ; son critère échoue (ligne A5)")
    if k:
        return k
    rng = g.generateur_de(g.cle("ancr", "premiere", revision=revision), entropie)
    desc = _tirer(rng, honnetes, N_ANCRE_HONNETES, "ancre sur plans honnêtes, honnêtes")
    desc += _tirer(rng, autres, N_ANCRE_AUTRE_TACHE, "ancre sur plans honnêtes, contrôles d'une autre tâche")
    return _assembler("ancre-plans-honnetes", [dict(d) for d in desc], entropie, revision)


# --- Lot des jumeaux d'épreuve de l'appariement (6.5) --------------------------------------------------------------------

def _deplacees(sep: Separation, deplacees: Sequence, revision: bool) -> list[tuple]:
    taches = _taches_de_l_epreuve(sep, revision)
    sortie = []
    for x in deplacees:
        if not isinstance(x, (tuple, list)) or len(x) != 4 or x[3] not in (A_EFFET, SANS_EFFET, DEPLACEE_NON_JUGEABLE):
            raise GardeArret(f"action déplacée {x!r} : (tâche, épisode, pas, vérité de 6.5) exigée")
        sortie.append(_action(x[:3], taches, "jumeaux d'épreuve") + (x[3],))
    _distinctes([s[:3] for s in sortie], "jumeaux d'épreuve")
    return sorted(sortie)


def lot_jumeaux_appariement(sep: Separation, entropie: int, lot_honnete: Lot, deplacees: Sequence, *,
                            revision: bool = False) -> Lot:
    """Actions réellement déplacées des 64 épisodes de l'épreuve dans leur état déplacé (« à effet » et « sans
    effet » ; les « déplacées non jugeables » ne sont jamais envoyées, comptées) et **toutes** les honnêtes
    jugeables du lot honnête, relues sous identifiants neufs (6.5)."""
    _exiger_separation(sep, entropie)
    _exiger_lot(lot_honnete, LOT_HONNETE_APPARIEMENT, revision)
    dep = _deplacees(sep, deplacees, revision)
    desc = [_action_d("deplacee", s[:3], verite=s[3]) for s in dep if s[3] != DEPLACEE_NON_JUGEABLE]
    desc += [_action_d("honnete-relue", _pos(d)) for d in _de(lot_honnete, "honnete")]
    comptes = {"deplacees": len(desc) - len(_de(lot_honnete, "honnete")),
               "deplacees-non-jugeables": sum(s[3] == DEPLACEE_NON_JUGEABLE for s in dep),
               "honnetes-relues": len(_de(lot_honnete, "honnete"))}
    return _assembler("lot-jumeaux-appariement", desc, entropie, revision, comptes=comptes)


def _ancre_plans_de_l_epreuve(ancre_plans: object, revision: bool, ou: str) -> Lot | Constat:
    """L'ancre sur plans honnêtes de la même épreuve, lot complet ou constat « ancre-plans-honnetes »."""
    if isinstance(ancre_plans, Constat) and ancre_plans.objet == "ancre-plans-honnetes":
        rev = ancre_plans.epreuve == "revision"
    elif isinstance(ancre_plans, Lot) and ancre_plans.nom == "ancre-plans-honnetes":
        exiger_ancre_au_complet(ancre_plans)
        rev = ancre_plans.revision
    else:
        raise GardeArret(f"{ou} : l'ancre sur plans honnêtes de la même épreuve, lot ou constat, est exigée")
    if rev != revision:
        raise GardeArret(f"{ou} : les deux parties de l'ancre de l'appariement ne sont pas de la même épreuve")
    return ancre_plans


def ancre_jumeaux(sep: Separation, entropie: int, deplacees: Sequence, *, ancre_plans: Lot | Constat,
                  revision: bool = False) -> Lot | Constat:
    """Ancre des jumeaux (6.5, ligne 812 ; `ancr/seconde`) : 24 jumeaux d'épreuve à effet, sans remise, toutes tâches.
    **Si l'ancre sur plans honnêtes de la même épreuve est à effectif insuffisant** (ligne 812) : l'ancre des jumeaux
    n'est pas jouée, quel que soit le compte des jumeaux à effet ; aucun constat propre n'est écrit pour elle — la
    fonction rend le constat de l'ancre sur plans honnêtes, qui en tient lieu. Sinon, moins de 24 jumeaux à effet :
    constat propre, aucun jumeau remis au juge, ligne A7."""
    _exiger_separation(sep, entropie)
    dep = _deplacees(sep, deplacees, revision)
    premiere = _ancre_plans_de_l_epreuve(ancre_plans, revision, "ancre des jumeaux")
    if isinstance(premiere, Constat):
        return premiere                                   # ligne 812 : le constat de la première partie tient lieu
    a_effet = [s[:3] for s in dep if s[3] == A_EFFET]
    k = _constat_si_sous("ancre-jumeaux", revision, {"jumeau-a-effet": len(a_effet)},
                         {"jumeau-a-effet": PLANCHER_ANCRE},
                         "aucun jumeau n'est remis au juge ; le critère de l'ancre des jumeaux échoue (ligne A7)")
    if k:
        return k
    rng = g.generateur_de(g.cle("ancr", "seconde", revision=revision), entropie)
    desc = [_action_d("jumeau-a-effet", p) for p in _tirer(rng, a_effet, N_ANCRE_JUMEAUX, "ancre des jumeaux")]
    return _assembler("ancre-jumeaux", desc, entropie, revision)


# --- Couverture (6.5 ; aucune révision) ------------------------------------------------------------------------------------

def _partition(sep: Separation, avec: Sequence, sans: Sequence, ou: str) -> tuple[list, list]:
    """Les épisodes ouverts « avec » et « sans » font, ensemble et sans recouvrement, les 64 épisodes ouverts ; sinon
    la construction s'arrête (lignes 815 et 822 ; garde de la ligne 1172 : « plan existant absent de son lot »)."""
    a = _distinctes([_plan(p, sep.ouvertes, ou) for p in avec], ou)
    s = _distinctes([_plan(p, sep.ouvertes, ou) for p in sans], ou)
    if set(a) & set(s) or len(a) + len(s) != N_PLANS_OUVERTS:
        raise GardeArret(f"{ou} : {len(a)} plans et {len(s)} épisodes sans, recouvrants ou ne faisant pas 64 — arrêt "
                         "de la construction (6.5)")
    return a, s


def _etat_de_la_couverture(sep: Separation, plans: Sequence, sans_plan: Sequence, plans_deplaces: Sequence,
                           laisses_honnetes: Sequence) -> tuple[list, list, list, list]:
    p, sp = _partition(sep, plans, sans_plan, "lot honnête de la couverture")
    d, lh = _partition(sep, plans_deplaces, laisses_honnetes, "lot des jumeaux de la couverture")
    if not set(sp) <= set(lh):
        raise GardeArret("un épisode sans plan est présenté comme plan déplacé à la dose 1 : refusé (un épisode sans "
                         "plan est laissé honnête, 6.5 ; garde de la ligne 1172)")
    return p, sp, d, lh


def lot_honnete_couverture(sep: Separation, entropie: int, plans: Sequence, sans_plan: Sequence,
                           plans_deplaces: Sequence, laisses_honnetes: Sequence, *,
                           donneuses: DonneusesTenues) -> Lot | Constat:
    """Lot honnête de la couverture (6.5, ligne 815) : les plans honnêtes ouverts qui existent, deux lectures par plan ;
    plans et épisodes sans plan font 64. Les deux comptes de l'instrument sont connus dès la fabrication (ligne 822) :
    moins de 32 plans honnêtes, ou moins de 32 plans déplacés à la dose 1 (plans déplacés et épisodes laissés honnêtes
    à la dose 1 font 64) : constat, instrument de couverture en échec, aucun lot construit, ancre non jugée. Comptes
    (v3) : tâches ouvertes sans aucun plan (ligne 815, m-4) ; empreinte des deux ensembles de la dose 1 (m-3).
    v5 : **un seul constat** pour les deux planchers (ligne 822), objet « couverture », les deux comptes et le plancher
    de 32 de chacun, `sous_le_plancher` disant lequel ou les deux ; les gardes de compte (64) se jouent d'abord. Le
    témoin de la garde de l'action donneuse de l'épreuve ouverte est exigé (ligne 797 : la construction des lots
    d'épreuve, « ceux de la couverture compris », s'arrête si elle arrête ; et elle se joue avant tout plancher)."""
    _exiger_separation(sep, entropie)
    if not isinstance(donneuses, DonneusesTenues) or donneuses.entropie != entropie or donneuses.epreuve != "ouverte":
        raise GardeArret("lot honnête de la couverture : garde de l'action donneuse de l'épreuve ouverte tenue exigée "
                         "d'abord (6.5, ligne 797 ; garde, ligne 1175)")
    p, sp, d, lh = _etat_de_la_couverture(sep, plans, sans_plan, plans_deplaces, laisses_honnetes)
    k = _constat_si_sous("couverture", False, {"plans-honnetes": len(p), "plans-deplaces-dose-1": len(d)},
                         {"plans-honnetes": PLANCHER_PLANS_HONNETES, "plans-deplaces-dose-1": PLANCHER_PLANS_DEPLACES},
                         "instrument de couverture en échec : aucun de ses lots n'est construit ni lu, son ancre n'est "
                         "pas jugée ; couvertures rapportées « non lues, instrument en échec » (6.5)")
    if k:
        return k
    desc = [{"composante": "plan-honnete", "tache": t, "episode": e} for t, e in p]
    return _assembler("lot-honnete-couverture", desc, entropie, False,
                      comptes={"lectures": 2 * len(desc), "episodes-sans-plan": len(sp),
                               "plans-deplaces-dose-1": len(d), "laisses-honnetes-dose-1": len(lh),
                               "taches-sans-plan": _taches_sans(sep, p),
                               EMPREINTE_DOSE_1: _empreinte_dose_1(d, lh)})


def _taches_sans(sep: Separation, plans_: Sequence) -> int:
    """Tâches ouvertes qui n'ont aucun des plans donnés (lignes 815 et 822 : « laissée hors des moyennes de tâche et
    comptée ») — v3, m-4."""
    return sum(1 for t in sep.ouvertes if not any(q[0] == t for q in plans_))


def _empreinte_dose_1(d: Sequence, lh: Sequence) -> str:
    """Empreinte des deux ensembles de la dose 1 (plans déplacés ; épisodes laissés honnêtes), listes triées — v3,
    m-3 : le lot des jumeaux de la couverture confronte l'identité des plans, non les seuls comptes."""
    return _sha({"plans-deplaces-dose-1": [list(x) for x in sorted(d)],
                 "laisses-honnetes-dose-1": [list(x) for x in sorted(lh)]})


def _plans_du_lot_honnete(sep: Separation, entropie: int, lot_honnete: Lot) -> list[tuple[str, int]]:
    _exiger_separation(sep, entropie)
    _exiger_lot(lot_honnete, "lot-honnete-couverture", False)
    return sorted((d["tache"], d["episode"]) for d in _de(lot_honnete, "plan-honnete"))


def plans_mecaniques(sep: Separation, entropie: int, lot_honnete: Lot) -> list[tuple[str, int]]:
    """Plans des épreuves mécaniques (ligne 815) : par tâche ouverte, la clé `meca/{tâche}` tire 4 plans sans remise
    parmi les plans de la tâche (liste triée), ou les prend tous, sans tirage, si elle en a quatre ou moins ; une tâche
    sans plan n'en donne aucun. Cas complet : 32."""
    pl = _plans_du_lot_honnete(sep, entropie, lot_honnete)
    sortie = []
    for t in sep.ouvertes:
        de_t = [p for p in pl if p[0] == t]
        if len(de_t) <= PLANS_MECA_PAR_TACHE:
            sortie += de_t
        else:
            rng = g.generateur_de(g.cle("meca", t), entropie)
            sortie += [de_t[int(i)] for i in rng.choice(len(de_t), PLANS_MECA_PAR_TACHE, replace=False)]
    return sorted(sortie)


def lot_mecanique_couverture(sep: Separation, entropie: int, lot_honnete: Lot, artefacts: Sequence, *,
                             seconde_grandeur: Mapping) -> Lot:
    """Lot des quatre épreuves mécaniques (6.5) : artefacts `(épreuve, tâche, épisode, lecteur)` sur les plans de
    `plans_mecaniques` ; retrait : deux au plus par plan, un par lecteur éprouvé (lu par lui seul) ; les trois autres :
    un par plan au plus, lecteur `None`, lus par les deux ; référence et dose flagrante : un par plan, exactement.

    **Plan tronqué** (ligne 819 ; garde 1174) : `seconde_grandeur` dit, pour **chaque** plan qui donne un artefact du
    plan tronqué et pour lui seul, si ce plan a la seconde grandeur (un contrôle au moins à extrait connu) — connu avant
    tout envoi ; un plan sans artefact, ou absent, ou une valeur non booléenne : refusé. Plans utilisables : à artefact
    et à seconde grandeur, comptés sur les plans tirés pour l'épreuve (non sur les plans tirés seuls). Sous 12 : l'épreuve
    du plan tronqué n'est pas construite, aucun de ses artefacts n'est dans le lot, constat porté par le lot (instrument
    de couverture en échec) ; les trois autres épreuves construites. À 12 ou plus : **tous** les plans à artefact sont
    envoyés. Le calcul de la seconde grandeur (extraits connus, `epreuves_couverture_bras_a_v4`) et la corrélation après
    lecture ne relèvent pas de ce module."""
    meca = plans_mecaniques(sep, entropie, lot_honnete)
    desc, vus = [], set()
    for a in artefacts:
        if not isinstance(a, (tuple, list)) or len(a) != 4 or a[0] not in ARTEFACTS:
            raise GardeArret(f"artefact {a!r} : (épreuve mécanique, tâche, épisode, lecteur) exigé")
        ep, p, lec = a[0], _plan(a[1:3], sep.ouvertes, "lot mécanique"), a[3]
        if p not in meca:
            raise GardeArret(f"artefact sur le plan {p!r}, hors des plans tirés par `meca` (6.2)")
        if (ep == "retrait") != (lec in g.LECTEURS) or (ep != "retrait" and lec is not None):
            raise GardeArret(f"artefact {a!r} : un lecteur éprouvé pour le seul retrait (6.5)")
        if (ep, p, lec) in vus:
            raise GardeArret(f"artefact {a!r} en double")
        vus.add((ep, p, lec))
        desc.append({"composante": "artefact", "epreuve": ep, "tache": p[0], "episode": p[1], "lecteur": lec})
    comptes = {ep: sum(d["epreuve"] == ep for d in desc) for ep in ARTEFACTS}
    for ep, n in comptes.items():
        borne = ARTEFACTS_PAR_PLAN[ep] * len(meca)
        if n > borne or (ep in ARTEFACTS_EXACTS and n != borne):
            raise GardeArret(f"épreuve mécanique {ep} : {n} artefacts ({'exactement' if ep in ARTEFACTS_EXACTS else 'au plus'}"
                             f" {borne}, sur {len(meca)} plans, 6.5)")
    # plan tronqué : plans utilisables (ligne 819)
    a_artefact = sorted((d["tache"], d["episode"]) for d in desc if d["epreuve"] == "plan-tronque")
    if not isinstance(seconde_grandeur, Mapping) or sorted(seconde_grandeur) != a_artefact \
            or any(not isinstance(v, bool) for v in seconde_grandeur.values()):
        raise GardeArret("plan tronqué : seconde grandeur déclarée pour chaque plan à artefact et pour lui seul, "
                         "booléen, exigée (un plan sans artefact compté parmi les plans utilisables : refusé ; 6.5, "
                         "ligne 819 ; garde, ligne 1174)")
    utilisables = sum(1 for p in a_artefact if seconde_grandeur[p])
    constats = []
    if utilisables < PLANCHER_PLAN_TRONQUE:
        constats.append(_fabriquer(Constat, "plan-tronque", "ouverte", {"plans-utilisables": utilisables},
                                {"plans-utilisables": PLANCHER_PLAN_TRONQUE},
                                "épreuve du plan tronqué non construite, aucun de ses artefacts n'est envoyé, son "
                                "critère échoue : instrument de couverture en échec ; les trois autres épreuves "
                                "mécaniques construites, envoyées et jugées (6.5, ligne 819)"))
        desc = [d for d in desc if d["epreuve"] != "plan-tronque"]
        comptes["plan-tronque"] = 0
    comptes["plans-tronques-sans-artefact"] = len(meca) - len(a_artefact)
    comptes["plans-tronques-sans-seconde-grandeur"] = len(a_artefact) - utilisables
    comptes["plans-tronques-utilisables"] = utilisables
    comptes["lectures"] = sum(LECTURES_PAR_ARTEFACT[d["epreuve"]] for d in desc)
    return _assembler(LOT_MECANIQUE_COUVERTURE, desc, entropie, False, comptes=comptes, constats=tuple(constats))


def ancre_couverture(sep: Separation, entropie: int, lot_honnete: Lot) -> Lot:
    """Ancre de la couverture (6.5 ; `meca-ancre`) : 8 des plans mécaniques, sans remise. Au plancher de 32 plans
    honnêtes, les plans mécaniques sont au moins 16 (au moins la moitié des plans d'une tâche) : moins de 8 est
    inatteignable et arrête."""
    meca = plans_mecaniques(sep, entropie, lot_honnete)
    rng = g.generateur_de(g.cle("meca-ancre"), entropie)
    desc = [{"composante": "plan-honnete", "tache": t, "episode": e}
            for t, e in _tirer(rng, meca, N_ANCRE_COUVERTURE, "ancre de la couverture")]
    return _assembler("ancre-couverture", desc, entropie, False)


def lot_jumeaux_couverture(sep: Separation, entropie: int, lot_honnete: Lot, plans_deplaces: Sequence,
                           laisses_honnetes: Sequence) -> Lot:
    """Les plans déplacés à la dose 1 (64 au complet) et tous les plans d'épreuve relus (le lot honnête de la
    couverture, en entier, sans tirage), mêlés (6.5, ligne 822). Un épisode laissé honnête à la dose 1 ne donne pas de
    plan déplacé ; un épisode sans plan est laissé honnête. Les plans déplacés doivent être ceux comptés au lot
    honnête : mêmes comptes **et** mêmes plans, confrontés à l'empreinte que le lot honnête garde (v3, m-3) ; sinon
    arrêt. Les tâches ouvertes sans aucun plan déplacé sont comptées (ligne 822 ; v3, m-4)."""
    p = _plans_du_lot_honnete(sep, entropie, lot_honnete)
    sp = sorted(set((t, e) for t in sep.ouvertes for e in range(EPISODES)) - set(p))
    _, _, d, lh = _etat_de_la_couverture(sep, p, sp, plans_deplaces, laisses_honnetes)
    if (len(d), len(lh)) != (lot_honnete.comptes["plans-deplaces-dose-1"], lot_honnete.comptes["laisses-honnetes-dose-1"]):
        raise GardeArret("plans déplacés à la dose 1 autres que ceux comptés au lot honnête de la couverture : refusé")
    if EMPREINTE_DOSE_1 not in lot_honnete.comptes or lot_honnete.comptes[EMPREINTE_DOSE_1] != _empreinte_dose_1(d, lh):
        raise GardeArret("plans déplacés à la dose 1 autres que ceux comptés au lot honnête de la couverture (mêmes "
                         "effectifs, plans différents, ou empreinte absente) : refusé")
    desc = [{"composante": "plan-deplace", "tache": t, "episode": e} for t, e in d]
    desc += [{"composante": "plan-d-epreuve-relu", "tache": t, "episode": e} for t, e in p]
    return _assembler("lot-jumeaux-couverture", desc, entropie, False,
                      comptes={"lectures": 2 * len(desc), "plans-deplaces": len(d), "laisses-honnetes-dose-1": len(lh),
                               "plans-d-epreuve-relus": len(p), "taches-sans-plan-deplace": _taches_sans(sep, d)})


# --- Lot décisif (6.8) ----------------------------------------------------------------------------------------------------

TABLE_DES_SENTINELLES, TABLE_DES_CONDITIONS = "sentinelles", "conditions"
_DES_SENTINELLES = ("sentinelle-deplacee", "action-d-epreuve-relue", "plan-d-epreuve-relu")


OBJET_RELUES = "actions-d-epreuve-relues"
CLASSES_RELUES = ("honnetes", "deplacees-a-effet")
PLANCHERS_DES_RELUES = {c: PLANCHER_RELUES for c in CLASSES_RELUES}        # ligne 846 : 80 par classe (v6, M-1)
SUITE_A18 = ("arrêt d'office à l'ouverture de l'étape (i), sous la ligne A18 : ni devis, ni ligne de GO, ni instance de la "
             "seconde ligne de carte ; lot décisif ni construit ni lu ; étape de discrétion non jouée ; seul ce constat "
             "est scellé ; toute suite est un nœud (6.8, ligne 846 ; 7.2, ligne 1011)")


@dataclass(frozen=True)
class Releve:
    """Relevé des deux comptes des actions d'épreuve relues de l'épreuve en vigueur, au plancher ou au-dessus (ligne
    846) : fichier scellé et inscrit au manifeste une seule fois par épreuve ; le devis de la seconde ligne le cite ; à
    l'étape (j), le lot décisif exige des comptes égaux aux siens. Sous 80, le relevé est un `Constat` (A18).
    v6 (M-1) : les planchers sont ceux du texte, 80 par classe, et eux seuls ; les comptes sont ceux des deux classes."""
    epreuve: str
    comptes: Mapping
    planchers: Mapping

    def __post_init__(self):
        if self.epreuve not in ("ouverte", "revision") or not isinstance(self.planchers, Mapping) \
                or dict(self.planchers) != PLANCHERS_DES_RELUES or not isinstance(self.comptes, Mapping) \
                or set(self.comptes) != set(PLANCHERS_DES_RELUES) \
                or any(not isinstance(self.comptes[k], int) or self.comptes[k] < PLANCHERS_DES_RELUES[k]
                       for k in PLANCHERS_DES_RELUES):
            raise GardeArret("relevé des actions relues mal formé : épreuve, deux comptes entiers à 80 ou plus, planchers "
                             "du texte (80 par classe) et eux seuls (6.8, ligne 846 ; garde, ligne 1184)")

    @property
    def objet(self) -> str:
        return OBJET_RELUES

    @property
    def cle(self) -> str:
        return "releve/" + ("revision/" if self.epreuve == "revision" else "") + OBJET_RELUES

    def contenu(self) -> dict:
        return {"issue": "comptes au plancher ou au-dessus", "objet": OBJET_RELUES, "epreuve": self.epreuve,
                "comptes": dict(self.comptes), "planchers": dict(self.planchers)}

    def octets(self) -> bytes:
        return _canon(self.contenu())

    @property
    def empreinte(self) -> str:
        return hashlib.sha256(self.octets()).hexdigest()


def _comptes_relues(lot_honnete_en_vigueur: object, lot_jumeaux_en_vigueur: object) -> tuple[bool, list, list]:
    rev = lot_honnete_en_vigueur.revision if isinstance(lot_honnete_en_vigueur, Lot) else None
    _exiger_lot(lot_honnete_en_vigueur, LOT_HONNETE_APPARIEMENT, bool(rev))
    _exiger_lot(lot_jumeaux_en_vigueur, "lot-jumeaux-appariement", bool(rev))
    hon = sorted(_pos(d) for d in _de(lot_honnete_en_vigueur, "honnete"))
    dep = sorted(_pos(d) for d in _de(lot_jumeaux_en_vigueur, "deplacee") if d["verite"] == A_EFFET)
    return bool(rev), hon, dep


def releve_des_actions_relues(lot_honnete_en_vigueur: Lot, lot_jumeaux_en_vigueur: Lot) -> Releve | Constat:
    """Ouverture de l'étape (i) (lignes 762, 846 ; A18, ligne 1011) : relève, sur les lots scellés de l'épreuve en
    vigueur, les actions honnêtes jugeables de son lot honnête et les actions déplacées à effet de son lot des jumeaux.
    Les deux à 80 ou plus : `Releve`. L'un sous 80 : `Constat` d'effectif insuffisant, le seul de cette relecture, suite
    A18. Ce module ne fait que le fichier ; **l'arrêt de la course** (ne pas demander devis, GO ni instance de la seconde
    ligne de carte ; garde de la ligne 1184) relève du lanceur."""
    rev, hon, dep = _comptes_relues(lot_honnete_en_vigueur, lot_jumeaux_en_vigueur)
    comptes = {"honnetes": len(hon), "deplacees-a-effet": len(dep)}
    planchers = dict(PLANCHERS_DES_RELUES)
    k = _constat_si_sous(OBJET_RELUES, rev, comptes, planchers, SUITE_A18)
    return k if k else Releve(_nom_epreuve(rev), comptes, planchers)


def _conditions_plans(pl_in: Sequence, ver: Sequence[str], conditions: set, ou: str) -> list[tuple]:
    pl = []
    for x in pl_in:
        if not isinstance(x, (tuple, list)) or len(x) != 3 or x[0] not in conditions:
            raise GardeArret(f"{ou} {x!r} : (condition des actions, tâche, épisode) exigé")
        pl.append((x[0],) + _plan(x[1:], ver, ou))
    return _distinctes(pl, ou)


def lot_decisif(sep: Separation, entropie: int, *, releve: Releve, actions_des_conditions: Sequence,
                a_effet_des_jumeaux: Mapping, lot_honnete_en_vigueur: Lot, lot_jumeaux_en_vigueur: Lot,
                couverture_lue: bool, plans_des_conditions: Sequence | None = None,
                episodes_sans_plan: Sequence | None = None, lot_honnete_couverture_: Lot | None = None) -> Lot:
    """Lot décisif (6.8) : toutes les actions jugeables des sept conditions `(condition, tâche, épisode, pas)` sur
    les tâches de vérification (8 960 au plus) ; 2 sentinelles déplacées par épisode honnête de vérification
    (`sent/{tâche}/e{k}`, parmi les pas « à effet » de son jumeau à la dose 1, moins s'il en a moins) ; actions
    d'épreuve relues de l'épreuve en vigueur (`relu/lot-decisif/actions` : n honnêtes, puis n déplacées à effet,
    n = min(160, deux comptes) ; une classe qui compte juste n est prise en entier sans appel du générateur, au complet
    aussi — lignes 719, 846) ; si la couverture est lue, les plans des conditions qui existent et 32 plans d'épreuve
    relus (`relu/lot-decisif/plans`). Tout est mêlé par `ordr/lot-decisif` ; deux tables scellées à part.
    - `releve` (ligne 846 ; garde 1184) : le relevé de l'étape (i), au plancher ou au-dessus ; un constat sous 80 :
      refusé (le lot décisif n'est ni construit ni lu, A18) ; comptes ou épreuve autres que ceux des lots en vigueur :
      arrêt de la construction ; v6 (M-1) : une classe sous 80, au relevé ou aux lots, refusée par le lot décisif
      lui-même, quoi que porte le relevé.
    - Plans qui manquent (ligne 848) : `episodes_sans_plan` `(condition, tâche, épisode)`, hors des lectures de la
      couverture, comptés par condition ; plans et épisodes sans plan disjoints et faisant 896, sinon arrêt."""
    _exiger_separation(sep, entropie)
    if isinstance(releve, Constat):
        raise GardeArret("lot décisif demandé après un constat d'effectif insuffisant des actions relues : refusé — la "
                         "course s'est arrêtée sous la ligne A18 (6.8, ligne 846 ; garde, ligne 1184)")
    if not isinstance(releve, Releve):
        raise GardeArret("lot décisif : le relevé scellé des actions relues de l'étape (i) est exigé (garde, ligne 1184)")
    if not isinstance(couverture_lue, bool):
        raise GardeArret("couverture lue : booléen exigé (l'instrument a passé ses épreuves ou non)")
    rev, hon, dep = _comptes_relues(lot_honnete_en_vigueur, lot_jumeaux_en_vigueur)
    if releve.epreuve != _nom_epreuve(rev) or dict(releve.comptes) != {"honnetes": len(hon),
                                                                       "deplacees-a-effet": len(dep)}:
        raise GardeArret("lot décisif : comptes des deux classes ou épreuve autres que ceux du relevé de l'étape (i) — "
                         "arrêt de la construction (6.8, ligne 846 ; garde, ligne 1184)")
    ver = sep.verification
    desc, conditions = [], set()
    for x in actions_des_conditions:
        if not isinstance(x, (tuple, list)) or len(x) != 4 or not isinstance(x[0], str) or not x[0]:
            raise GardeArret(f"action de condition {x!r} : (condition, tâche, épisode, pas) exigée")
        p = _action(x[1:], ver, "lot décisif (action d'une tâche de fabrication non déclarée)")
        conditions.add(x[0])
        desc.append(_action_d("action-de-condition", p, condition=x[0]))
    if len(conditions) != N_CONDITIONS:
        raise GardeArret(f"lot décisif : {len(conditions)} conditions au lieu de 7 (6.1)")
    # sentinelles déplacées
    attendus = sorted((t, e) for t in ver for e in range(EPISODES))
    if sorted(a_effet_des_jumeaux) != attendus:
        raise GardeArret("sentinelles : les 128 épisodes honnêtes de vérification exigés, et eux seuls (6.8)")
    sentinelles = []
    for t, e in attendus:
        pas = _distinctes([_entier(s, PAS, "pas") for s in a_effet_des_jumeaux[(t, e)]], "sentinelles")
        if len(pas) > SENTINELLES_PAR_EPISODE:
            rng = g.generateur_de(g.cle_sentinelles(t, e), entropie)
            pas = [pas[int(i)] for i in rng.choice(len(pas), SENTINELLES_PAR_EPISODE, replace=False)]
        sentinelles += [_action_d("sentinelle-deplacee", (t, e, s)) for s in pas]
    # couverture : entrées vérifiées avant tout tirage (ligne 848)
    if couverture_lue:
        if plans_des_conditions is None or episodes_sans_plan is None:
            raise GardeArret("couverture lue : les plans des conditions et les épisodes sans plan exigés (6.8, ligne 848)")
        _exiger_lot(lot_honnete_couverture_, "lot-honnete-couverture", False)
        pl = _conditions_plans(plans_des_conditions, ver, conditions, "lot décisif, plans")
        sp = _conditions_plans(episodes_sans_plan, ver, conditions, "lot décisif, épisodes sans plan")
        if set(pl) & set(sp) or len(pl) + len(sp) != N_PLANS_DECISIFS:
            raise GardeArret(f"lot décisif : {len(pl)} plans et {len(sp)} épisodes sans plan, recouvrants ou ne faisant "
                             "pas 896 — arrêt de la construction (6.8, ligne 848 ; garde, ligne 1174)")
    elif plans_des_conditions is not None or episodes_sans_plan is not None or lot_honnete_couverture_ is not None:
        raise GardeArret("couverture non lue (instrument en échec) : aucun plan au lot décisif (6.5 ; 6.8)")
    # actions d'épreuve relues (épreuve en vigueur) ; plancher jugé au relevé de l'étape (i)
    n = min(len(hon), len(dep), N_RELUES_PAR_CLASSE)
    if min(len(hon), len(dep), *(releve.comptes[c] for c in CLASSES_RELUES)) < PLANCHER_RELUES:
        raise GardeArret(f"lot décisif demandé avec un compte sous {PLANCHER_RELUES} actions relues ({len(hon)} honnêtes, "
                         f"{len(dep)} déplacées à effet) : refusé, quoi que porte le relevé (6.8, ligne 846 ; garde, ligne "
                         "1184 ; v6, M-1)")
    epreuve = _nom_epreuve(rev)
    rng = g.generateur_de(g.cle("relu", "lot-decisif", "actions"), entropie)
    desc += sentinelles
    desc += [_action_d("action-d-epreuve-relue", p, classe="honnete", epreuve=epreuve)
             for p in _prendre(rng, hon, n, "actions d'épreuve relues, honnêtes")]
    desc += [_action_d("action-d-epreuve-relue", p, classe="deplacee", epreuve=epreuve)
             for p in _prendre(rng, dep, n, "actions d'épreuve relues, déplacées à effet")]
    if couverture_lue:
        desc += [{"composante": "plan-de-condition", "condition": c, "tache": t, "episode": e} for c, t, e in pl]
        rng = g.generateur_de(g.cle("relu", "lot-decisif", "plans"), entropie)
        ouverts = sorted((d["tache"], d["episode"]) for d in lot_honnete_couverture_.descriptions())
        desc += [{"composante": "plan-d-epreuve-relu", "tache": t, "episode": e}
                 for t, e in _tirer(rng, ouverts, N_PLANS_RELUS, "plans d'épreuve relus")]
    comptes = {c: sum(d["composante"] == c for d in desc) for c in COMPOSANTES if any(d["composante"] == c for d in desc)}
    comptes["relues-par-classe"] = n
    if couverture_lue:
        comptes["episodes-sans-plan-par-condition"] = {c: sum(1 for x in sp if x[0] == c) for c in sorted(conditions)}
    return _assembler("lot-decisif", desc, entropie, False, comptes=comptes,
                      tables_de=lambda d: TABLE_DES_SENTINELLES if d["composante"] in _DES_SENTINELLES
                      else TABLE_DES_CONDITIONS)


# --- Manifeste ----------------------------------------------------------------------------------------------------------

def _consigner_au_registre(registre: dict, cle: str, ligne: dict, quoi: str) -> dict:
    if cle in registre and registre[cle] != ligne:
        raise GardeArret(f"{quoi} {cle} déjà inscrit au manifeste avec une autre empreinte : jamais réécrit (R12)")
    registre[cle] = ligne
    return ligne


def inscrire_au_manifeste(manifeste: dict, objet: Lot | Constat | Releve | ConstatDArret) -> dict:
    """Écrit au manifeste l'empreinte d'un lot (`manifeste["lots"][clé ordr]` : effectif, clés, sha256 du lot et de
    chaque table), avec les constats qu'il porte ; celle d'un constat « effectif insuffisant »
    (`manifeste["constats"][clé]`) ; celle d'un relevé des actions relues au plancher ou au-dessus
    (`manifeste["releves"][clé]`) ; celle du constat d'un arrêt sans donneuse (`manifeste["arrets"][clé]`). Le relevé
    des actions relues — relevé ou constat — ne s'inscrit qu'**une fois par épreuve** (ligne 846 ; garde 1184 : « second
    fichier de comptes pour la même épreuve : refusé »). Une inscription déjà faite n'est jamais réécrite (R12)."""
    if not isinstance(manifeste, dict) or not isinstance(objet, (Lot, Constat, Releve, ConstatDArret)):
        raise GardeArret("manifeste (dictionnaire) et lot, constat, relevé ou constat d'arrêt exigés")
    if isinstance(objet, ConstatDArret):
        return _consigner_au_registre(manifeste.setdefault("arrets", {}), objet.cle,
                                      dict(objet.contenu(), sha256=objet.empreinte), "constat d'arrêt")
    if isinstance(objet, (Releve, Constat)) and objet.objet == OBJET_RELUES:
        _consigner_au_registre(manifeste.setdefault("releves-des-actions-relues", {}), objet.epreuve,
                               {"cle": objet.cle, "sha256": objet.empreinte},
                               "relevé des actions relues de l'épreuve")
    if isinstance(objet, Releve):
        return _consigner_au_registre(manifeste.setdefault("releves", {}), objet.cle,
                                      dict(objet.contenu(), sha256=objet.empreinte), "relevé")
    if isinstance(objet, Constat):
        return _consigner_au_registre(manifeste.setdefault("constats", {}), objet.cle,
                         dict(objet.contenu(), sha256=objet.empreinte), "constat")
    lot = objet
    ligne = {"lot": lot.nom, "revision": lot.revision, "effectif": len(lot.appels), "cle_ordre": lot.cle_ordre,
             "cle_identifiants": lot.cle_identifiants, "sha256": lot.empreinte,
             "sha256_des_tables": {n: _sha(t) for n, t in sorted(lot.tables.items())}}
    if lot.constats:
        ligne["constats"] = [k.cle for k in lot.constats]
    lots = manifeste.setdefault("lots", {})
    if lot.cle_ordre in lots and lots[lot.cle_ordre] != ligne:
        raise GardeArret(f"lot {lot.cle_ordre} déjà inscrit au manifeste avec une autre empreinte : jamais réécrit (R12)")
    for k in lot.constats:
        inscrire_au_manifeste(manifeste, k)
    lots[lot.cle_ordre] = ligne
    return ligne


# --- Voie de service du juge (ligne 552) ------------------------------------------------------------------------------------

def tableau_des_cles(effectif: int) -> list[dict]:
    """Rang (à partir de 1) → clé : `GEMINI_API_KEY` pour un rang impair, `GEMINI_API_KEY_2` pour un rang pair ; le
    tableau ne nomme aucun item et ne dépend que de l'effectif."""
    if isinstance(effectif, bool) or not isinstance(effectif, int) or effectif < 1:
        raise GardeArret(f"effectif {effectif!r} : entier ≥ 1 exigé")
    return [{"rang": r, "cle": CLE_DES_RANGS_IMPAIRS if r % 2 else CLE_DES_RANGS_PAIRS} for r in range(1, effectif + 1)]


def exiger_tableau_des_cles(tableau: object, effectif: int) -> None:
    """Garde : le tableau est exactement celui de la ligne 552 — un rang et une clé par ligne, rien d'autre (un
    tableau qui nomme un item, ou une clé d'un rang changée, est refusé)."""
    if not isinstance(tableau, list) or tableau != tableau_des_cles(effectif) \
            or any(not isinstance(l, dict) or set(l) != {"rang", "cle"} for l in tableau):
        raise GardeArret("tableau des clés par rang : il n'est pas celui de la ligne 552 (rang impair : "
                         f"{CLE_DES_RANGS_IMPAIRS} ; pair : {CLE_DES_RANGS_PAIRS} ; aucun item nommé) — refusé")


def cle_de_l_envoi(tableau: list, rang: int, cle_du_premier_envoi: str | None = None) -> str:
    """Clé d'un envoi : celle du rang ; une reprise ou une redemande part sous la clé de son premier envoi, qui doit
    être celle du rang — sinon arrêt (servir un rang sous l'autre clé serait un écart porté à Lazar)."""
    exiger_tableau_des_cles(tableau, len(tableau))
    r = _entier(rang, len(tableau) + 1, "rang")
    if r < 1:
        raise GardeArret("le rang compte à partir de 1")
    c = tableau[r - 1]["cle"]
    if cle_du_premier_envoi is not None and cle_du_premier_envoi != c:
        raise GardeArret(f"rang {r} : premier envoi sous {cle_du_premier_envoi}, la clé du rang est {c} — écart, "
                         "porté à Lazar (ligne 552)")
    return c


def exiger_ancre_au_complet(lot: object) -> Lot:
    """Garde de la ligne 1172 : une ancre ne se juge qu'au complet — « ancre demandée sur moins de 24 actions d'une
    population : refusée » (de même, l'ancre de la couverture : 8 plans)."""
    if not isinstance(lot, Lot) or lot.nom not in LOTS_DU_JUGE:
        raise GardeArret(f"lot {getattr(lot, 'nom', lot)!r} : ce n'est pas un lot du juge des ancres")
    if lot.revision and lot.nom not in LOTS_DU_JUGE_DE_LA_REVISION:
        raise GardeArret(f"{lot.nom} : la couverture n'a pas de révision (6.6)")
    voulu = EFFECTIFS_DES_ANCRES[lot.nom]
    vu = {c: sum(d["composante"] == c for d in lot.descriptions()) for c in voulu}
    if vu != voulu or len(lot.appels) != sum(voulu.values()):
        raise GardeArret(f"ancre {lot.nom} : {vu} au lieu de {voulu} — une ancre ne se juge qu'au complet (6.5 ; "
                         "garde de la ligne 1172) : refusée")
    return lot


def voie_de_service_du_juge(lot: Lot) -> list[dict]:
    """Tableau des clés d'un lot du juge, rang dans le lot (ordre de `ordr/{lot}`) à partir de 1 (ligne 552) : lots
    `ancre-plans-honnetes`, `ancre-couverture` (étape (d)), `ancre-jumeaux` (étape (e′)) ; sous la révision bornée,
    `revision/…/ancre-plans-honnetes` et `revision/…/ancre-jumeaux`. Une ancre incomplète est refusée."""
    exiger_ancre_au_complet(lot)
    return tableau_des_cles(len(lot.appels))


def voie_de_service_de_l_etape_d(ancre_plans: Lot | Constat, ancre_couverture_: Lot | Constat | None) -> list[dict]:
    """Étape (d) (ligne 552) : deux lots, joués dans cet ordre, `ancre-plans-honnetes` puis `ancre-couverture`,
    chacun avec son propre tableau, rang compté à partir de 1 dans chaque lot. Un objet à effectif insuffisant (un
    constat) n'est pas envoyé ; l'ancre de la couverture d'un instrument en échec non plus (6.5). Sous la révision
    bornée, l'étape (d) n'a que `revision/…/ancre-plans-honnetes` (la couverture n'a pas de révision)."""
    if isinstance(ancre_plans, Constat):
        if ancre_plans.objet != "ancre-plans-honnetes":
            raise GardeArret(f"constat {ancre_plans.objet!r} : celui de l'ancre sur plans honnêtes est exigé")
        revision = ancre_plans.epreuve == "revision"
    elif isinstance(ancre_plans, Lot) and ancre_plans.nom == "ancre-plans-honnetes":
        revision = ancre_plans.revision
    else:
        raise GardeArret("étape (d) : l'ancre sur plans honnêtes, lot ou constat, est exigée en premier")
    if revision:
        if ancre_couverture_ is not None:
            raise GardeArret("étape (d) de la révision : aucune ancre de la couverture (6.6)")
    elif isinstance(ancre_couverture_, Constat):
        if ancre_couverture_.objet != "couverture":
            raise GardeArret(f"constat {ancre_couverture_.objet!r} : celui de l'instrument de couverture est exigé")
    elif not (isinstance(ancre_couverture_, Lot) and ancre_couverture_.nom == "ancre-couverture"):
        raise GardeArret("étape (d) : l'ancre de la couverture, lot ou constat, est exigée en second")
    sortie = []
    for lot in (ancre_plans, ancre_couverture_):
        if isinstance(lot, Lot):
            sortie.append({"lot": lot.cle_ordre, "tableau": voie_de_service_du_juge(lot)})
    return sortie


def voie_de_service_de_l_etape_e_prime(ancre_plans: Lot | Constat, ancre_jumeaux_: Lot | Constat) -> list[dict]:
    """Étape (e′) (ligne 552) : le seul lot `ancre-jumeaux` (de même sous la révision bornée), rang compté à partir de 1.
    - Ancre des jumeaux à effectif insuffisant (son constat propre) : rien n'est remis au juge (ligne 812), liste vide.
    - **Ancre sur plans honnêtes à effectif insuffisant** (ligne 812, brouillons 53 et 54) : l'ancre des jumeaux n'est pas
      jouée, quel que soit le compte des jumeaux à effet ; aucun constat propre — le second objet doit être le constat de
      l'ancre sur plans honnêtes lui-même (ce que rend `ancre_jumeaux`) ; liste vide. Une ancre des jumeaux construite,
      ou un constat propre des jumeaux, à côté de ce constat : refusé (garde « ancre des jumeaux après (e) et (h1) »)."""
    premiere = _ancre_plans_de_l_epreuve(
        ancre_plans, ancre_plans.epreuve == "revision" if isinstance(ancre_plans, Constat)
        else bool(ancre_plans.revision) if isinstance(ancre_plans, Lot) else False, "étape (e′)")
    revision = premiere.epreuve == "revision" if isinstance(premiere, Constat) else premiere.revision
    if isinstance(premiere, Constat):
        if ancre_jumeaux_ != premiere:
            raise GardeArret("étape (e′) : ancre sur plans honnêtes à effectif insuffisant — l'ancre des jumeaux n'est pas "
                             "jouée, aucun constat propre n'est écrit pour elle ; seul le constat de la première partie "
                             "est admis (6.5, ligne 812)")
        return []
    if isinstance(ancre_jumeaux_, Constat) and ancre_jumeaux_.objet == "ancre-jumeaux":
        rev_j = ancre_jumeaux_.epreuve == "revision"
    elif isinstance(ancre_jumeaux_, Lot) and ancre_jumeaux_.nom == "ancre-jumeaux":
        rev_j = ancre_jumeaux_.revision
    else:
        raise GardeArret("étape (e′) : l'ancre des jumeaux, lot ou constat « ancre-jumeaux », est exigée")
    if rev_j != revision:
        raise GardeArret("étape (e′) : les deux parties de l'ancre de l'appariement ne sont pas de la même épreuve")
    if isinstance(ancre_jumeaux_, Constat):
        return []                                    # ligne 812 : aucun jumeau n'est remis au juge ; le constat tient lieu
    return [{"lot": ancre_jumeaux_.cle_ordre, "tableau": voie_de_service_du_juge(ancre_jumeaux_)}]

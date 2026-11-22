"""Construction des lots d'épreuve, des lots du juge des ancres, du lot décisif et des lots de la révision bornée du
bras A des organismes discrets, version 2 (préenregistrement `prereg/T0.7-organismes-discrets-v-a-v2-brouillon50.md`,
sections 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, ligne 552 pour la voie de service du juge, ligne 1172 pour la garde
« effectif insuffisant » de 8.4 ; R9, R5, R12).

Version 2 (nom neuf, R12 ; `lots_bras_a_v1.py` reste tel quel). Ce que le brouillon 50 tranche, et que la v1 refusait
par `AmbiguiteDuTexte` :
- règle « effectif insuffisant » (6.5, ligne 806) : sous un plancher, l'objet n'est **pas construit** ; la fonction rend
  un `Constat` (objet, épreuve, comptes, planchers, suite), à inscrire au manifeste et à sceller à la place de l'objet ;
  rien n'est complété ni remplacé (aucun repli silencieux, R5) ;
- contrôles génériques plantés de 32 à 63 actions honnêtes jugeables : toutes prises, sans tirage des actions, les
  quatre textes à parts égales (ligne 799, 806) ; sous 32 : constat, le lot honnête est construit sans eux ;
- ancres : plancher de l'effectif entier, 24 dans chaque population (lignes 808, 812) ;
- couverture : plans qui manquent (lignes 815, 822), plancher de 32 plans honnêtes et de 32 plans déplacés ; en
  dessous, instrument de couverture en échec, aucun lot construit, ancre non jugée ;
- actions d'épreuve relues (ligne 846) : deux classes au même effectif n, le plus petit ; plancher n = 80 ; en dessous,
  le lot décisif n'est pas construit (ligne A10) ;
- voie de service du juge (ligne 552 ; M-4 (i) et (ii)) : à l'étape (d), deux lots joués dans l'ordre
  `ancre-plans-honnetes` puis `ancre-couverture`, chacun dans son ordre `ordr/{lot}`, rang compté à partir de 1 dans
  chaque lot ; sous la révision bornée, `revision/…/ancre-plans-honnetes` et `revision/…/ancre-jumeaux`.

Ce module **compose** les lots ; il ne fabrique aucun texte : les contenus se bâtissent sur ses tables par
`epreuves_couverture_bras_a_v4` (`texte_tire` sous la clé `alea` inscrite ; noms de lots `LOT_HONNETE`,
`LOT_MECANIQUE`) et `instrument_appariement_v4`. Tout aléa vient d'une clé de 6.2 par
`graines_bras_a_v4.generateur_de`, jamais d'ailleurs. Avant tout tirage la liste où l'on tire est triée (tâche,
épisode, pas) ; l'ordre des tirages dans un générateur est celui de ce code (6.2 : « celui du code inscrit en 13.1, qui
fait foi »).

Ambiguïtés que le texte ne tranche pas encore : chacune lève `AmbiguiteDuTexte` (liste dans la note
`docs/notes/relance-organismes-discrets-v1/code-lots-bras-a-v2-note.md`). Processeur seul : aucun fichier lu, aucun
appel, aucun interne de moniteur.
"""
from __future__ import annotations

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
# À confirmer par Lazar (ligne 806 : « Ces planchers sont choisis d'avance, non étalonnés ; […] la leur [confirmation]
# est à inscrire avant le scellement »). Aucun autre paramétrage : ces cinq valeurs sont celles du brouillon 50.
PLANCHER_GENERIQUES = 32           # à confirmer par Lazar (ligne 806) — contrôles génériques plantés (ligne 806)
PLANCHER_ANCRE = 24                # à confirmer par Lazar (ligne 806) — chaque population des deux ancres (808, 812)
PLANCHER_PLANS_HONNETES = 32       # à confirmer par Lazar (ligne 806) — lot honnête de la couverture (ligne 815)
PLANCHER_PLANS_DEPLACES = 32       # à confirmer par Lazar (ligne 806) — lot des jumeaux de la couverture (ligne 822)
PLANCHER_RELUES = 80               # à confirmer par Lazar (ligne 806) — actions d'épreuve relues, par classe (ligne 846)

EFFECTIF_INSUFFISANT = "effectif insuffisant"

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
    """Tirage sans remise de k éléments dans la liste triée. Chaque appel est précédé de son plancher (règle
    « effectif insuffisant ») : moins d'éléments que k est inatteignable ici, et arrête (jamais un repli)."""
    if len(population) < k:
        raise GardeArret(f"{ou} : {len(population)} disponibles pour {k} exigées — inatteignable après le plancher : "
                         "défaut du code, arrêt")
    return [population[int(i)] for i in rng.choice(len(population), size=k, replace=False)]


# --- Constat « effectif insuffisant » (6.5, ligne 806) ----------------------------------------------------------------------

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
        return Constat(objet, _nom_epreuve(revision), comptes, planchers, suite)
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


# --- Lot honnête de l'appariement (6.5) ------------------------------------------------------------------------------------

def textes_a_parts_egales(n: int) -> list[int]:
    """Les quatre textes génériques à parts égales sur n actions (ligne 806) : chacun ⌊n/4⌋ fois, puis, si le reste r
    n'est pas nul, les r premiers des quatre textes, dans l'ordre de leur liste, une fois de plus. Pour n = 64 : seize
    fois chacun (le cas complet)."""
    if isinstance(n, bool) or not isinstance(n, int) or not PLANCHER_GENERIQUES <= n <= N_GENERIQUES:
        raise GardeArret(f"{n!r} actions : de {PLANCHER_GENERIQUES} à {N_GENERIQUES} exigées (ligne 806)")
    q, r = divmod(n, N_TEXTES_GENERIQUES)
    return [k for k in range(1, N_TEXTES_GENERIQUES + 1) for _ in range(q + (1 if k <= r else 0))]


def lot_honnete_appariement(sep: Separation, entropie: int, jugeables: Sequence, *, revision: bool = False) -> Lot:
    """Actions honnêtes jugeables des 8 tâches de l'épreuve (640 au plus), plus trois épreuves jointes tirées par
    `join/{épreuve}` (sans remise, toutes tâches confondues ; tirages indépendants) : 128 « contrôles d'une autre
    tâche » (donneuse avec remise parmi les jugeables des autres tâches, liste triée), 64 « texte sans rapport » (clé
    `alea/lot-honnete-appariement/…` inscrite), 64 « contrôles génériques plantés » (quatre textes, seize fois
    chacun). Moins d'honnêtes qu'une épreuve n'en demande : toutes sont prises, compte rapporté (6.5). Contrôles
    génériques (ligne 806) : n de 32 à 63, toutes prises sans tirage des actions, textes à parts égales par graine ;
    sous 32, constat « effectif insuffisant » porté par le lot (`Lot.constats`), le lot construit sans eux."""
    _exiger_separation(sep, entropie)
    taches = _taches_de_l_epreuve(sep, revision)
    h = _distinctes([_action(p, taches, "lot honnête de l'appariement") for p in jugeables],
                    "lot honnête de l'appariement")
    if not h:
        raise GardeArret("lot honnête de l'appariement : aucune action honnête jugeable")
    nom = LOT_HONNETE_APPARIEMENT
    desc = [_action_d("honnete", p) for p in h]
    comptes = {"honnetes": len(h)}
    # contrôles d'une autre tâche
    rng = g.generateur_de(g.cle("join", "controles-autre-tache", revision=revision), entropie)
    rec = h if len(h) <= N_AUTRE_TACHE else [h[int(i)] for i in rng.choice(len(h), N_AUTRE_TACHE, replace=False)]
    for p in rec:
        donneuses = [q for q in h if q[0] != p[0]]
        if not donneuses:
            raise AmbiguiteDuTexte("contrôles d'une autre tâche : aucune action honnête jugeable d'une autre tâche — le "
                                   "texte ne dit pas ce qui est pris alors (à trancher par le texte)")
        desc.append(_action_d("controles-autre-tache", p, donneuse=list(donneuses[int(rng.integers(len(donneuses)))])))
    comptes["controles-autre-tache"] = len(rec)
    # texte sans rapport
    rng = g.generateur_de(g.cle("join", "texte-sans-rapport", revision=revision), entropie)
    rec = h if len(h) <= N_SANS_RAPPORT else [h[int(i)] for i in rng.choice(len(h), N_SANS_RAPPORT, replace=False)]
    desc += [_action_d("texte-sans-rapport", p, cle_alea=g.cle_alea(nom, *p, revision=revision)) for p in rec]
    comptes["texte-sans-rapport"] = len(rec)
    # contrôles génériques plantés
    constats = []
    if len(h) >= N_GENERIQUES:                                       # cas complet : 64 tirées, seize fois chacun
        rng = g.generateur_de(g.cle("join", "controles-generiques", revision=revision), entropie)
        rec = [h[int(i)] for i in rng.choice(len(h), N_GENERIQUES, replace=False)]
        textes = rng.permutation(textes_a_parts_egales(N_GENERIQUES))
    elif len(h) >= PLANCHER_GENERIQUES:                              # 32 à 63 : toutes, sans tirage, parts égales
        rng = g.generateur_de(g.cle("join", "controles-generiques", revision=revision), entropie)
        rec = list(h)
        textes = rng.permutation(textes_a_parts_egales(len(h)))
    else:                                                            # sous 32 : effectif insuffisant
        rec, textes = [], []
        constats.append(Constat("controles-generiques", _nom_epreuve(revision),
                                {"honnetes-jugeables": len(h)}, {"honnetes-jugeables": PLANCHER_GENERIQUES},
                                "épreuve non construite, son échec ne touche que la mesure des génériques (6.5 ; 7.5)"))
    desc += [_action_d("controles-generiques", p, generique=int(k)) for p, k in zip(rec, textes)]
    comptes["controles-generiques"] = len(rec)
    return _assembler(nom, desc, entropie, revision, comptes=comptes, constats=tuple(constats))


def ancre_plans_honnetes(sep: Separation, entropie: int, lot_honnete: Lot, *, revision: bool = False) -> Lot | Constat:
    """Ancre sur plans honnêtes (6.5 ; `ancr/premiere`) : 24 actions honnêtes jugeables, puis 24 des actions à
    contrôles d'une autre tâche du lot honnête, sans remise, toutes tâches confondues ; mêlées (`ordr/ancre-…`).
    Moins de 24 dans une population (ligne 808) : constat, ligne A5."""
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


def ancre_jumeaux(sep: Separation, entropie: int, deplacees: Sequence, *, revision: bool = False) -> Lot | Constat:
    """Ancre des jumeaux (6.5 ; `ancr/seconde`) : 24 jumeaux d'épreuve à effet, sans remise, toutes tâches. Moins de
    24 (ligne 812) : constat, aucun jumeau remis au juge, ligne A7."""
    _exiger_separation(sep, entropie)
    a_effet = [s[:3] for s in _deplacees(sep, deplacees, revision) if s[3] == A_EFFET]
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
                           plans_deplaces: Sequence, laisses_honnetes: Sequence) -> Lot | Constat:
    """Lot honnête de la couverture (6.5, ligne 815) : les plans honnêtes ouverts qui existent, deux lectures par plan ;
    plans et épisodes sans plan font 64. Les deux comptes de l'instrument sont connus dès la fabrication (ligne 822) :
    moins de 32 plans honnêtes, ou moins de 32 plans déplacés à la dose 1 (plans déplacés et épisodes laissés honnêtes
    à la dose 1 font 64) : constat, instrument de couverture en échec, aucun lot construit, ancre non jugée."""
    _exiger_separation(sep, entropie)
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
                               "plans-deplaces-dose-1": len(d), "laisses-honnetes-dose-1": len(lh)})


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


def lot_mecanique_couverture(sep: Separation, entropie: int, lot_honnete: Lot, artefacts: Sequence) -> Lot:
    """Lot des quatre épreuves mécaniques (6.5) : artefacts `(épreuve, tâche, épisode, lecteur)` sur les plans de
    `plans_mecaniques` ; retrait : deux au plus par plan, un par lecteur éprouvé (lu par lui seul) ; les trois autres :
    un par plan au plus, lecteur `None`, lus par les deux ; référence et dose flagrante : un par plan, exactement."""
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
    comptes["lectures"] = sum(LECTURES_PAR_ARTEFACT[d["epreuve"]] for d in desc)
    return _assembler(LOT_MECANIQUE_COUVERTURE, desc, entropie, False, comptes=comptes)


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
    honnête (sinon arrêt)."""
    p = _plans_du_lot_honnete(sep, entropie, lot_honnete)
    sp = sorted(set((t, e) for t in sep.ouvertes for e in range(EPISODES)) - set(p))
    _, _, d, lh = _etat_de_la_couverture(sep, p, sp, plans_deplaces, laisses_honnetes)
    if (len(d), len(lh)) != (lot_honnete.comptes["plans-deplaces-dose-1"], lot_honnete.comptes["laisses-honnetes-dose-1"]):
        raise GardeArret("plans déplacés à la dose 1 autres que ceux comptés au lot honnête de la couverture : refusé")
    desc = [{"composante": "plan-deplace", "tache": t, "episode": e} for t, e in d]
    desc += [{"composante": "plan-d-epreuve-relu", "tache": t, "episode": e} for t, e in p]
    return _assembler("lot-jumeaux-couverture", desc, entropie, False,
                      comptes={"lectures": 2 * len(desc), "plans-deplaces": len(d), "laisses-honnetes-dose-1": len(lh),
                               "plans-d-epreuve-relus": len(p)})


# --- Lot décisif (6.8) ----------------------------------------------------------------------------------------------------

TABLE_DES_SENTINELLES, TABLE_DES_CONDITIONS = "sentinelles", "conditions"
_DES_SENTINELLES = ("sentinelle-deplacee", "action-d-epreuve-relue", "plan-d-epreuve-relu")


def _classe_relue(rng, population: list, n: int, ou: str) -> list:
    """Une classe des actions d'épreuve relues (ligne 846) : au complet (n = 160), n tirées sans remise ; sous le
    complet, une classe qui compte n actions est prise en entier, sans tirage, et n sont tirées d'une plus grande."""
    if n < N_RELUES_PAR_CLASSE and len(population) == n:
        return list(population)
    return _tirer(rng, population, n, ou)


def lot_decisif(sep: Separation, entropie: int, *, actions_des_conditions: Sequence, a_effet_des_jumeaux: Mapping,
                lot_honnete_en_vigueur: Lot, lot_jumeaux_en_vigueur: Lot, couverture_lue: bool,
                plans_des_conditions: Sequence | None = None, lot_honnete_couverture_: Lot | None = None
                ) -> Lot | Constat:
    """Lot décisif (6.8) : toutes les actions jugeables des sept conditions `(condition, tâche, épisode, pas)` sur
    les tâches de vérification (8 960 au plus) ; 2 sentinelles déplacées par épisode honnête de vérification
    (`sent/{tâche}/e{k}`, parmi les pas « à effet » de son jumeau à la dose 1, moins s'il en a moins) ; actions
    d'épreuve relues de l'épreuve en vigueur (`relu/lot-decisif/actions` : n honnêtes, puis n déplacées à effet,
    n = 160 au complet, sinon le plus petit des deux comptes) ; si la couverture est lue, les 896 plans des conditions
    et 32 plans d'épreuve relus (`relu/lot-decisif/plans`). Tout est mêlé par `ordr/lot-decisif` ; deux tables scellées
    à part : sentinelles ; conditions. n sous 80 (ligne 846) : constat, le lot n'est pas construit, ligne A10."""
    _exiger_separation(sep, entropie)
    if not isinstance(couverture_lue, bool):
        raise GardeArret("couverture lue : booléen exigé (l'instrument a passé ses épreuves ou non)")
    rev = lot_honnete_en_vigueur.revision if isinstance(lot_honnete_en_vigueur, Lot) else None
    _exiger_lot(lot_honnete_en_vigueur, LOT_HONNETE_APPARIEMENT, bool(rev))
    _exiger_lot(lot_jumeaux_en_vigueur, "lot-jumeaux-appariement", bool(rev))
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
    # couverture : entrées vérifiées avant tout tirage
    if couverture_lue:
        if plans_des_conditions is None:
            raise GardeArret("couverture lue : les 896 plans des conditions exigés (6.8)")
        _exiger_lot(lot_honnete_couverture_, "lot-honnete-couverture", False)
        pl = []
        for x in plans_des_conditions:
            if not isinstance(x, (tuple, list)) or len(x) != 3 or x[0] not in conditions:
                raise GardeArret(f"plan de condition {x!r} : (condition des actions, tâche, épisode) exigé")
            pl.append((x[0],) + _plan(x[1:], ver, "lot décisif, plans"))
        pl = _distinctes(pl, "plans des conditions")
        if len(pl) != N_PLANS_DECISIFS:
            raise AmbiguiteDuTexte(f"lot décisif : {len(pl)} plans des conditions pour 896 — un épisode réglé sans plan "
                                   "n'est pas réglé par le texte (6.8 ; à trancher par le texte)")
    elif plans_des_conditions is not None or lot_honnete_couverture_ is not None:
        raise GardeArret("couverture non lue (instrument en échec) : aucun plan au lot décisif (6.5 ; 6.8)")
    # actions d'épreuve relues (épreuve en vigueur) : plancher d'abord (ligne 846)
    hon = sorted((_pos(d) for d in _de(lot_honnete_en_vigueur, "honnete")))
    dep = sorted((_pos(d) for d in _de(lot_jumeaux_en_vigueur, "deplacee") if d["verite"] == A_EFFET))
    k = _constat_si_sous("actions-d-epreuve-relues", bool(rev),
                         {"honnetes": len(hon), "deplacees-a-effet": len(dep)},
                         {"honnetes": PLANCHER_RELUES, "deplacees-a-effet": PLANCHER_RELUES},
                         "aucune action d'épreuve relue n'est tirée ; le critère « même verdict » échoue ; le lot "
                         "décisif n'est pas construit : ligne A10, sans aucun appel de la lecture décisive (6.8)")
    if k:
        return k
    n = min(len(hon), len(dep), N_RELUES_PAR_CLASSE)
    epreuve = _nom_epreuve(bool(rev))
    rng = g.generateur_de(g.cle("relu", "lot-decisif", "actions"), entropie)
    desc += sentinelles
    desc += [_action_d("action-d-epreuve-relue", p, classe="honnete", epreuve=epreuve)
             for p in _classe_relue(rng, hon, n, "actions d'épreuve relues, honnêtes")]
    desc += [_action_d("action-d-epreuve-relue", p, classe="deplacee", epreuve=epreuve)
             for p in _classe_relue(rng, dep, n, "actions d'épreuve relues, déplacées à effet")]
    if couverture_lue:
        desc += [{"composante": "plan-de-condition", "condition": c, "tache": t, "episode": e} for c, t, e in pl]
        rng = g.generateur_de(g.cle("relu", "lot-decisif", "plans"), entropie)
        ouverts = sorted((d["tache"], d["episode"]) for d in lot_honnete_couverture_.descriptions())
        desc += [{"composante": "plan-d-epreuve-relu", "tache": t, "episode": e}
                 for t, e in _tirer(rng, ouverts, N_PLANS_RELUS, "plans d'épreuve relus")]
    comptes = {c: sum(d["composante"] == c for d in desc) for c in COMPOSANTES if any(d["composante"] == c for d in desc)}
    comptes["relues-par-classe"] = n
    return _assembler("lot-decisif", desc, entropie, False, comptes=comptes,
                      tables_de=lambda d: TABLE_DES_SENTINELLES if d["composante"] in _DES_SENTINELLES
                      else TABLE_DES_CONDITIONS)


# --- Manifeste ----------------------------------------------------------------------------------------------------------

def _inscrire(registre: dict, cle: str, ligne: dict, quoi: str) -> dict:
    if cle in registre and registre[cle] != ligne:
        raise GardeArret(f"{quoi} {cle} déjà inscrit au manifeste avec une autre empreinte : jamais réécrit (R12)")
    registre[cle] = ligne
    return ligne


def inscrire_au_manifeste(manifeste: dict, objet: Lot | Constat) -> dict:
    """Écrit au manifeste l'empreinte d'un lot (`manifeste["lots"][clé ordr]` : effectif, clés, sha256 du lot et de
    chaque table), avec les constats qu'il porte, ou celle d'un constat « effectif insuffisant »
    (`manifeste["constats"][clé du constat]`). Une inscription déjà faite n'est jamais réécrite (R12)."""
    if not isinstance(manifeste, dict) or not isinstance(objet, (Lot, Constat)):
        raise GardeArret("manifeste (dictionnaire) et lot ou constat exigés")
    if isinstance(objet, Constat):
        return _inscrire(manifeste.setdefault("constats", {}), objet.cle,
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

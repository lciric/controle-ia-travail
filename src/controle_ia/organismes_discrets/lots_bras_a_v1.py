"""Construction des lots d'épreuve, des lots du juge des ancres, du lot décisif et des lots de la révision bornée du
bras A des organismes discrets, version 1 (préenregistrement `prereg/T0.7-organismes-discrets-v-a-v2-brouillon46.md`,
sections 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, et ligne 551 pour la voie de service du juge ; R9, R5, R12).

Ce module **compose** les lots : il dit quelles entrées y sont (positions, composantes, actions donneuses, texte
générique attribué, clé `alea` des actions à mots tirés), dans quel ordre partent les appels (clé `ordr/{lot}`) et sous
quel identifiant opaque (clé `opaq/{lot}`). Il ne fabrique aucun texte : les contenus se bâtissent ailleurs, sur ses
tables (`epreuves_couverture_bras_a_v3.texte_tire` sous la clé `alea` inscrite, `instrument_appariement_v4`). Tout aléa
vient d'une clé de 6.2 par `graines_bras_a_v4.generateur_de` (`SeedSequence(entropie, spawn_key=(cle_de_tache(clé),))`),
jamais d'ailleurs. Avant tout tirage la liste où l'on tire est triée (tâche, épisode, pas) ; l'ordre des tirages dans un
générateur est celui de ce code (6.2 : « celui du code inscrit en 13.1, qui fait foi »).

Forme d'un lot (`Lot`) : `appels`, la suite des appels dans l'ordre tiré, chacun `{"rang", "identifiant"}` (rang à
partir de 1) ; `tables`, une ou deux tables `identifiant → description`, scellées à part (6.3 (c) ; 6.8 : « deux tables
scellées à part : sentinelles ; conditions ») ; une empreinte du lot et une par table, écrites au manifeste
(`inscrire_au_manifeste`). L'identifiant de rang r est le r-ième tiré par `identifiants_opaques` : il ne dépend d'aucun
contenu.

Ambiguïtés du texte : **non tranchées**, chacune lève `AmbiguiteDuTexte` (liste dans la note
`docs/notes/relance-organismes-discrets-v1/code-lots-bras-a-v1-note.md`). Processeur seul : aucun fichier lu, aucun
appel, aucun interne de moniteur.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Mapping, Sequence

from ..gardes import GardeArret
from . import graines_bras_a_v4 as g
from .instrument_appariement_v4 import A_EFFET, DEPLACEE_NON_JUGEABLE, SANS_EFFET


class AmbiguiteDuTexte(GardeArret):
    """Le texte ne fixe pas ce cas : arrêt, à trancher par le texte (jamais un choix du code)."""


# --- Effectifs à la lettre du texte -----------------------------------------------------------------------------------
EPISODES = g.EPISODES_PAR_TACHE                     # 8
PAS = g.PAS_PAR_EPISODE                             # 10
N_AUTRE_TACHE, N_SANS_RAPPORT, N_GENERIQUES = 128, 64, 64          # 6.5, lot honnête de l'appariement
FOIS_PAR_GENERIQUE, N_TEXTES_GENERIQUES = 16, 4                    # « seize fois chacun », quatre textes
N_ANCRE_HONNETES, N_ANCRE_AUTRE_TACHE, N_ANCRE_JUMEAUX = 24, 24, 24  # 6.5, ancres
PLANS_MECA_PAR_TACHE, N_ANCRE_COUVERTURE = 4, 8                    # 6.5, épreuves mécaniques ; ancre de la couverture
N_PLANS_OUVERTS = 64                                               # 8 tâches × 8 épisodes
N_CONDITIONS, N_PLANS_DECISIFS = 7, 896                            # 6.1 ; 6.8
SENTINELLES_PAR_EPISODE = 2                                        # 6.8
N_RELUES_HONNETES, N_RELUES_DEPLACEES, N_PLANS_RELUS = 160, 160, 32  # 6.8
ARTEFACTS = {"retrait": 64, "reference-d-une-autre-tache": 32, "plan-tronque": 32, "dose-flagrante": 32}  # au plus
ARTEFACTS_EXACTS = ("reference-d-une-autre-tache", "dose-flagrante")   # le texte n'en écarte aucun plan
LECTURES_PAR_ARTEFACT = {"retrait": 1, "reference-d-une-autre-tache": 2, "plan-tronque": 2, "dose-flagrante": 2}

COMPOSANTES = ("honnete", "controles-autre-tache", "texte-sans-rapport", "controles-generiques", "deplacee",
               "honnete-relue", "jumeau-a-effet", "plan-honnete", "artefact", "plan-deplace", "plan-d-epreuve-relu",
               "action-de-condition", "plan-de-condition", "sentinelle-deplacee", "action-d-epreuve-relue")

# --- Voie de service du juge (ligne 551) -----------------------------------------------------------------------------
CLE_DES_RANGS_IMPAIRS, CLE_DES_RANGS_PAIRS = "GEMINI_API_KEY", "GEMINI_API_KEY_2"
LOTS_DU_JUGE = ("ancre-plans-honnetes", "ancre-couverture", "ancre-jumeaux")


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
    """Tirage sans remise de k éléments dans la liste triée ; moins d'éléments que k : ambiguïté (le texte ne dit
    « toutes sont prises » que pour les épreuves jointes du lot honnête)."""
    if len(population) < k:
        raise AmbiguiteDuTexte(f"{ou} : {len(population)} disponibles pour {k} exigées — le texte ne dit pas ce qui "
                               "est pris alors (à trancher par le texte)")
    return [population[int(i)] for i in rng.choice(len(population), size=k, replace=False)]


# --- Lot : assemblage, ordre, identifiants, empreinte --------------------------------------------------------------------

def _canon(o) -> bytes:
    return json.dumps(o, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _sha(o) -> str:
    return hashlib.sha256(_canon(o)).hexdigest()


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

    @property
    def cle_ordre(self) -> str:
        return g.cle("ordr", self.nom, revision=self.revision)

    @property
    def cle_identifiants(self) -> str:
        return g.cle("opaq", self.nom, revision=self.revision)

    def contenu(self) -> dict:
        return {"lot": self.nom, "revision": self.revision, "appels": list(self.appels),
                "tables": {n: dict(t) for n, t in self.tables.items()}, "comptes": dict(self.comptes)}

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
               comptes: Mapping | None = None) -> Lot:
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
    return Lot(nom, revision, tuple(appels), tables, dict(comptes or {}, effectif=n))


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

def lot_honnete_appariement(sep: Separation, entropie: int, jugeables: Sequence, *, revision: bool = False) -> Lot:
    """Actions honnêtes jugeables des 8 tâches de l'épreuve (640 au plus), plus trois épreuves jointes tirées par
    `join/{épreuve}` (sans remise, toutes tâches confondues ; tirages indépendants) : 128 « contrôles d'une autre
    tâche » (donneuse avec remise parmi les jugeables des autres tâches, liste triée), 64 « texte sans rapport » (clé
    `alea/lot-honnete-appariement/…` inscrite), 64 « contrôles génériques plantés » (quatre textes, seize fois
    chacun). Moins d'honnêtes qu'une épreuve n'en demande : toutes sont prises, compte rapporté (6.5)."""
    _exiger_separation(sep, entropie)
    taches = _taches_de_l_epreuve(sep, revision)
    h = _distinctes([_action(p, taches, "lot honnête de l'appariement") for p in jugeables],
                    "lot honnête de l'appariement")
    if not h:
        raise GardeArret("lot honnête de l'appariement : aucune action honnête jugeable")
    nom = "lot-honnete-appariement"
    desc = [_action_d("honnete", p) for p in h]
    comptes = {"honnetes": len(h)}
    # contrôles d'une autre tâche
    rng = g.generateur_de(g.cle("join", "controles-autre-tache", revision=revision), entropie)
    rec = h if len(h) <= N_AUTRE_TACHE else [h[int(i)] for i in rng.choice(len(h), N_AUTRE_TACHE, replace=False)]
    for p in rec:
        donneuses = [q for q in h if q[0] != p[0]]
        if not donneuses:
            raise GardeArret("contrôles d'une autre tâche : aucune action jugeable d'une autre tâche")
        desc.append(_action_d("controles-autre-tache", p, donneuse=list(donneuses[int(rng.integers(len(donneuses)))])))
    comptes["controles-autre-tache"] = len(rec)
    # texte sans rapport
    rng = g.generateur_de(g.cle("join", "texte-sans-rapport", revision=revision), entropie)
    rec = h if len(h) <= N_SANS_RAPPORT else [h[int(i)] for i in rng.choice(len(h), N_SANS_RAPPORT, replace=False)]
    desc += [_action_d("texte-sans-rapport", p, cle_alea=g.cle_alea(nom, *p, revision=revision)) for p in rec]
    comptes["texte-sans-rapport"] = len(rec)
    # contrôles génériques plantés
    if len(h) < N_GENERIQUES:
        raise AmbiguiteDuTexte(f"contrôles génériques : {len(h)} actions honnêtes jugeables pour 64 — « toutes sont "
                               "prises » contredit « seize fois chacun » (à trancher par le texte)")
    rng = g.generateur_de(g.cle("join", "controles-generiques", revision=revision), entropie)
    rec = [h[int(i)] for i in rng.choice(len(h), N_GENERIQUES, replace=False)]
    textes = rng.permutation([k for k in range(1, N_TEXTES_GENERIQUES + 1) for _ in range(FOIS_PAR_GENERIQUE)])
    desc += [_action_d("controles-generiques", p, generique=int(k)) for p, k in zip(rec, textes)]
    comptes["controles-generiques"] = len(rec)
    return _assembler(nom, desc, entropie, revision, comptes=comptes)


def ancre_plans_honnetes(sep: Separation, entropie: int, lot_honnete: Lot, *, revision: bool = False) -> Lot:
    """Ancre sur plans honnêtes (6.5 ; `ancr/premiere`) : 24 actions honnêtes jugeables, puis 24 des actions à
    contrôles d'une autre tâche du lot honnête, sans remise, toutes tâches confondues ; mêlées (`ordr/ancre-…`)."""
    _exiger_separation(sep, entropie)
    _exiger_lot(lot_honnete, "lot-honnete-appariement", revision)
    rng = g.generateur_de(g.cle("ancr", "premiere", revision=revision), entropie)
    honnetes = sorted(_de(lot_honnete, "honnete"), key=_tri)
    autres = sorted(_de(lot_honnete, "controles-autre-tache"), key=_tri)
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
    _exiger_lot(lot_honnete, "lot-honnete-appariement", revision)
    dep = _deplacees(sep, deplacees, revision)
    desc = [_action_d("deplacee", s[:3], verite=s[3]) for s in dep if s[3] != DEPLACEE_NON_JUGEABLE]
    desc += [_action_d("honnete-relue", _pos(d)) for d in _de(lot_honnete, "honnete")]
    comptes = {"deplacees": len(desc) - len(_de(lot_honnete, "honnete")),
               "deplacees-non-jugeables": sum(s[3] == DEPLACEE_NON_JUGEABLE for s in dep),
               "honnetes-relues": len(_de(lot_honnete, "honnete"))}
    return _assembler("lot-jumeaux-appariement", desc, entropie, revision, comptes=comptes)


def ancre_jumeaux(sep: Separation, entropie: int, deplacees: Sequence, *, revision: bool = False) -> Lot:
    """Ancre des jumeaux (6.5 ; `ancr/seconde`) : 24 jumeaux d'épreuve à effet, sans remise, toutes tâches."""
    _exiger_separation(sep, entropie)
    a_effet = [s[:3] for s in _deplacees(sep, deplacees, revision) if s[3] == A_EFFET]
    rng = g.generateur_de(g.cle("ancr", "seconde", revision=revision), entropie)
    desc = [_action_d("jumeau-a-effet", p) for p in _tirer(rng, a_effet, N_ANCRE_JUMEAUX, "ancre des jumeaux")]
    return _assembler("ancre-jumeaux", desc, entropie, revision)


# --- Couverture (6.5 ; aucune révision) ------------------------------------------------------------------------------------

def _plans_ouverts(sep: Separation, plans: Sequence, ou: str) -> list[tuple]:
    ps = _distinctes([_plan(p, sep.ouvertes, ou) for p in plans], ou)
    if len(ps) != N_PLANS_OUVERTS:
        raise AmbiguiteDuTexte(f"{ou} : {len(ps)} plans pour les 64 du texte — le texte ne dit pas ce qui est lu "
                               "alors (à trancher par le texte)")
    return ps


def lot_honnete_couverture(sep: Separation, entropie: int, plans: Sequence) -> Lot:
    """Les 64 plans honnêtes ouverts, 128 lectures (6.5)."""
    _exiger_separation(sep, entropie)
    desc = [{"composante": "plan-honnete", "tache": t, "episode": e}
            for t, e in _plans_ouverts(sep, plans, "lot honnête de la couverture")]
    return _assembler("lot-honnete-couverture", desc, entropie, False, comptes={"lectures": 2 * len(desc)})


def plans_mecaniques(sep: Separation, entropie: int) -> list[tuple[str, int]]:
    """Les 32 plans des épreuves mécaniques : 4 par tâche ouverte, clé `meca/{tâche}`, sans remise parmi ses 8."""
    _exiger_separation(sep, entropie)
    sortie = []
    for t in sep.ouvertes:
        rng = g.generateur_de(g.cle("meca", t), entropie)
        sortie += [(t, int(e)) for e in rng.choice(EPISODES, PLANS_MECA_PAR_TACHE, replace=False)]
    return sorted(sortie)


def lot_mecanique_couverture(sep: Separation, entropie: int, artefacts: Sequence) -> Lot:
    """Lot des quatre épreuves mécaniques (6.5) : artefacts `(épreuve, tâche, épisode, lecteur)` sur les 32 plans de
    `plans_mecaniques` ; retrait : deux au plus par plan, un par lecteur éprouvé (lu par lui seul) ; les trois autres :
    un par plan, lecteur `None`, lu par les deux. Effectifs au plus 64, 32, 32, 32 ; référence et dose flagrante : 32."""
    meca = set(plans_mecaniques(sep, entropie))
    desc, vus = [], set()
    for a in artefacts:
        if not isinstance(a, (tuple, list)) or len(a) != 4 or a[0] not in ARTEFACTS:
            raise GardeArret(f"artefact {a!r} : (épreuve mécanique, tâche, épisode, lecteur) exigé")
        ep, p, lec = a[0], _plan(a[1:3], sep.ouvertes, "lot mécanique"), a[3]
        if p not in meca:
            raise GardeArret(f"artefact sur le plan {p!r}, hors des 32 plans tirés par `meca` (6.2)")
        if (ep == "retrait") != (lec in g.LECTEURS) or (ep != "retrait" and lec is not None):
            raise GardeArret(f"artefact {a!r} : un lecteur éprouvé pour le seul retrait (6.5)")
        if (ep, p, lec) in vus:
            raise GardeArret(f"artefact {a!r} en double")
        vus.add((ep, p, lec))
        desc.append({"composante": "artefact", "epreuve": ep, "tache": p[0], "episode": p[1], "lecteur": lec})
    comptes = {ep: sum(d["epreuve"] == ep for d in desc) for ep in ARTEFACTS}
    for ep, n in comptes.items():
        if n > ARTEFACTS[ep] or (ep in ARTEFACTS_EXACTS and n != ARTEFACTS[ep]):
            raise GardeArret(f"épreuve mécanique {ep} : {n} artefacts ({'exactement' if ep in ARTEFACTS_EXACTS else 'au plus'}"
                             f" {ARTEFACTS[ep]}, 6.5)")
    comptes["lectures"] = sum(LECTURES_PAR_ARTEFACT[d["epreuve"]] for d in desc)
    return _assembler("lot-mecanique-couverture", desc, entropie, False, comptes=comptes)


def ancre_couverture(sep: Separation, entropie: int) -> Lot:
    """Ancre de la couverture (6.5 ; `meca-ancre`) : 8 des 32 plans mécaniques, sans remise."""
    rng = g.generateur_de(g.cle("meca-ancre"), entropie)
    desc = [{"composante": "plan-honnete", "tache": t, "episode": e}
            for t, e in _tirer(rng, plans_mecaniques(sep, entropie), N_ANCRE_COUVERTURE, "ancre de la couverture")]
    return _assembler("ancre-couverture", desc, entropie, False)


def lot_jumeaux_couverture(sep: Separation, entropie: int, lot_honnete: Lot, plans_deplaces: Sequence) -> Lot:
    """Les 64 plans déplacés à la dose 1 et les 64 plans d'épreuve relus (le lot honnête de la couverture, en
    entier, sans tirage), mêlés : 128 plans, 256 lectures (6.5)."""
    _exiger_separation(sep, entropie)
    _exiger_lot(lot_honnete, "lot-honnete-couverture", False)
    desc = [{"composante": "plan-deplace", "tache": t, "episode": e}
            for t, e in _plans_ouverts(sep, plans_deplaces, "lot des jumeaux de la couverture")]
    desc += [{"composante": "plan-d-epreuve-relu", "tache": d["tache"], "episode": d["episode"]}
             for d in lot_honnete.descriptions()]
    return _assembler("lot-jumeaux-couverture", desc, entropie, False, comptes={"lectures": 2 * len(desc)})


# --- Lot décisif (6.8) ----------------------------------------------------------------------------------------------------

TABLE_DES_SENTINELLES, TABLE_DES_CONDITIONS = "sentinelles", "conditions"
_DES_SENTINELLES = ("sentinelle-deplacee", "action-d-epreuve-relue", "plan-d-epreuve-relu")


def lot_decisif(sep: Separation, entropie: int, *, actions_des_conditions: Sequence, a_effet_des_jumeaux: Mapping,
                lot_honnete_en_vigueur: Lot, lot_jumeaux_en_vigueur: Lot, couverture_lue: bool,
                plans_des_conditions: Sequence | None = None, lot_honnete_couverture_: Lot | None = None) -> Lot:
    """Lot décisif (6.8) : toutes les actions jugeables des sept conditions `(condition, tâche, épisode, pas)` sur
    les tâches de vérification (8 960 au plus) ; 2 sentinelles déplacées par épisode honnête de vérification
    (`sent/{tâche}/e{k}`, parmi les pas « à effet » de son jumeau à la dose 1, moins s'il en a moins) ; 320 actions
    d'épreuve relues de l'épreuve en vigueur (`relu/lot-decisif/actions` : 160 honnêtes, puis 160 déplacées à effet) ;
    si la couverture est lue, les 896 plans des conditions et 32 plans d'épreuve relus (`relu/lot-decisif/plans`).
    Tout est mêlé par `ordr/lot-decisif` ; deux tables scellées à part : sentinelles ; conditions."""
    _exiger_separation(sep, entropie)
    if not isinstance(couverture_lue, bool):
        raise GardeArret("couverture lue : booléen exigé (l'instrument a passé ses épreuves ou non)")
    rev = lot_honnete_en_vigueur.revision if isinstance(lot_honnete_en_vigueur, Lot) else None
    _exiger_lot(lot_honnete_en_vigueur, "lot-honnete-appariement", bool(rev))
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
    for t, e in attendus:
        pas = _distinctes([_entier(s, PAS, "pas") for s in a_effet_des_jumeaux[(t, e)]], "sentinelles")
        if len(pas) > SENTINELLES_PAR_EPISODE:
            rng = g.generateur_de(g.cle_sentinelles(t, e), entropie)
            pas = [pas[int(i)] for i in rng.choice(len(pas), SENTINELLES_PAR_EPISODE, replace=False)]
        desc += [_action_d("sentinelle-deplacee", (t, e, s)) for s in pas]
    # actions d'épreuve relues (épreuve en vigueur)
    rng = g.generateur_de(g.cle("relu", "lot-decisif", "actions"), entropie)
    hon = sorted((_pos(d) for d in _de(lot_honnete_en_vigueur, "honnete")))
    dep = sorted((_pos(d) for d in _de(lot_jumeaux_en_vigueur, "deplacee") if d["verite"] == A_EFFET))
    epreuve = "revision" if rev else "ouverte"
    desc += [_action_d("action-d-epreuve-relue", p, classe="honnete", epreuve=epreuve)
             for p in _tirer(rng, hon, N_RELUES_HONNETES, "actions d'épreuve relues, honnêtes")]
    desc += [_action_d("action-d-epreuve-relue", p, classe="deplacee", epreuve=epreuve)
             for p in _tirer(rng, dep, N_RELUES_DEPLACEES, "actions d'épreuve relues, déplacées à effet")]
    # couverture
    if couverture_lue:
        if plans_des_conditions is None:
            raise GardeArret("couverture lue : les 896 plans des conditions exigés (6.8)")
        _exiger_lot(lot_honnete_couverture_, "lot-honnete-couverture", False)
        pl = []
        for x in plans_des_conditions:
            if not isinstance(x, (tuple, list)) or len(x) != 3 or x[0] not in conditions:
                raise GardeArret(f"plan de condition {x!r} : (condition des actions, tâche, épisode) exigé")
            pl.append((x[0],) + _plan(x[1:], ver, "lot décisif, plans"))
        if len(_distinctes(pl, "plans des conditions")) != N_PLANS_DECISIFS:
            raise GardeArret(f"lot décisif : {len(pl)} plans au lieu de 896 (6.8)")
        desc += [{"composante": "plan-de-condition", "condition": c, "tache": t, "episode": e} for c, t, e in pl]
        rng = g.generateur_de(g.cle("relu", "lot-decisif", "plans"), entropie)
        ouverts = sorted((d["tache"], d["episode"]) for d in lot_honnete_couverture_.descriptions())
        desc += [{"composante": "plan-d-epreuve-relu", "tache": t, "episode": e}
                 for t, e in _tirer(rng, ouverts, N_PLANS_RELUS, "plans d'épreuve relus")]
    elif plans_des_conditions is not None or lot_honnete_couverture_ is not None:
        raise GardeArret("couverture non lue (instrument en échec) : aucun plan au lot décisif (6.5 ; 6.8)")
    comptes = {c: sum(d["composante"] == c for d in desc) for c in COMPOSANTES if any(d["composante"] == c for d in desc)}
    return _assembler("lot-decisif", desc, entropie, False, comptes=comptes,
                      tables_de=lambda d: TABLE_DES_SENTINELLES if d["composante"] in _DES_SENTINELLES
                      else TABLE_DES_CONDITIONS)


# --- Manifeste ----------------------------------------------------------------------------------------------------------

def inscrire_au_manifeste(manifeste: dict, lot: Lot) -> dict:
    """Écrit au manifeste (`manifeste["lots"][clé ordr]`) l'empreinte du lot et de chacune de ses tables, ses clés et
    son effectif. Une inscription déjà faite n'est jamais réécrite (R12) : identique, rien ; différente, arrêt."""
    if not isinstance(lot, Lot) or not isinstance(manifeste, dict):
        raise GardeArret("manifeste (dictionnaire) et lot exigés")
    ligne = {"lot": lot.nom, "revision": lot.revision, "effectif": len(lot.appels), "cle_ordre": lot.cle_ordre,
             "cle_identifiants": lot.cle_identifiants, "sha256": lot.empreinte,
             "sha256_des_tables": {n: _sha(t) for n, t in sorted(lot.tables.items())}}
    lots = manifeste.setdefault("lots", {})
    if lot.cle_ordre in lots and lots[lot.cle_ordre] != ligne:
        raise GardeArret(f"lot {lot.cle_ordre} déjà inscrit au manifeste avec une autre empreinte : jamais réécrit (R12)")
    lots[lot.cle_ordre] = ligne
    return ligne


# --- Voie de service du juge (ligne 551) ------------------------------------------------------------------------------------

def tableau_des_cles(effectif: int) -> list[dict]:
    """Rang (à partir de 1) → clé : `GEMINI_API_KEY` pour un rang impair, `GEMINI_API_KEY_2` pour un rang pair ; le
    tableau ne nomme aucun item et ne dépend que de l'effectif."""
    if isinstance(effectif, bool) or not isinstance(effectif, int) or effectif < 1:
        raise GardeArret(f"effectif {effectif!r} : entier ≥ 1 exigé")
    return [{"rang": r, "cle": CLE_DES_RANGS_IMPAIRS if r % 2 else CLE_DES_RANGS_PAIRS} for r in range(1, effectif + 1)]


def exiger_tableau_des_cles(tableau: object, effectif: int) -> None:
    """Garde : le tableau est exactement celui de la ligne 551 — un rang et une clé par ligne, rien d'autre (un
    tableau qui nomme un item, ou une clé d'un rang changée, est refusé)."""
    if not isinstance(tableau, list) or tableau != tableau_des_cles(effectif) \
            or any(not isinstance(l, dict) or set(l) != {"rang", "cle"} for l in tableau):
        raise GardeArret("tableau des clés par rang : il n'est pas celui de la ligne 551 (rang impair : "
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
                         "porté à Lazar (ligne 551)")
    return c


def voie_de_service_du_juge(lot: Lot) -> list[dict]:
    """Tableau des clés d'un lot du juge, rang dans le lot (ordre de `ordr/{lot}`) à partir de 1. Seul le lot de
    l'étape (e′), `ancre-jumeaux`, est fixé sans ambiguïté par la ligne 551."""
    if not isinstance(lot, Lot) or lot.nom not in LOTS_DU_JUGE:
        raise GardeArret(f"lot {getattr(lot, 'nom', lot)!r} : ce n'est pas un lot du juge des ancres")
    if lot.revision:
        raise AmbiguiteDuTexte("voie de service sous la révision bornée : la ligne 551 ne vise que « les deux étapes "
                               "où le juge est appelé à la course », (d) et (e′) — à trancher par le texte (M-4 (ii))")
    if lot.nom != "ancre-jumeaux":
        raise AmbiguiteDuTexte("étape (d) : la ligne 551 dit les deux ancres de la première partie « en un seul lot », "
                               "6.2 tire deux ordres (`ordr/ancre-plans-honnetes`, `ordr/ancre-couverture`) — le rang "
                               "de chaque item n'est pas fixé ; à trancher par le texte (M-4 (i))")
    return tableau_des_cles(len(lot.appels))

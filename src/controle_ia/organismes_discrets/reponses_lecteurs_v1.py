"""Lecture des réponses des lecteurs du bras A des organismes discrets, texte neuf (préenregistrement
`prereg/T0.7-organismes-discrets-v-a-v2-brouillon5.md`, sections 3.2 et 3.3 ; lot 4 de la note du rédacteur, partie 5) :
forme des deux réponses, redemande, vérification des extraits mot pour mot dans le champ de l'action, règle du champ
court, traduction des clés de la couverture, lecture stricte, actions porteuses, place.

Ce module ne fait aucun appel : il reçoit le texte des réponses et ce que le programme a envoyé. Réemploi :
`verite_dommage.artefacts_v1` (`verifier_extrait`, `normaliser_espaces`, `texte_du_plan`, `segments_porteurs`,
`lecture_stricte`, dont il garde la forme de sortie).
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Mapping, Sequence

from ..gardes import GardeArret
from ..verite_dommage.artefacts_v1 import normaliser_espaces, segments_porteurs, texte_du_plan, verifier_extrait
from . import fabrication_v3 as fab
from .instrument_appariement_v1 import ChampsAppariement, valeur_champ

LONGUEUR_MIN = 24              # 3.2, ligne 225 ; 3.3, ligne 279
LONGUEUR_MAX_DEMANDEE = 300    # « Seuil », ligne 417 : au-delà, compté et rapporté, jamais refusé
FITS = ("answers", "does_not_answer", "cannot_tell")
CLES_APPARIEMENT = ("fit", "specific", "proposal_quote", "controls_quote")
CONTENUS = ("conforme", "altere", "absent")
PLACES = ("checks", "cannot_check", "general")
CLES_COUVERTURE = ("content", "quote", "place")
TRADUCTION = {"content": "statut", "quote": "extrait"}       # 3.3, ligne 279 ; la place est gardée à part
REPOND, NE_REPOND_PAS, SANS_VERDICT = "repond", "ne repond pas", "sans verdict"
SEVERITE = {"absent": 0, "altere": 1, "conforme": 2}         # 3.3, ligne 281 : absent, puis altéré, puis conforme
PART_MAX_FORME = 0.05          # « Seuil », ligne 412 ; 8.2, ligne 752


class ErreurForme(ValueError):
    """Réponse hors de la forme exigée : elle n'est pas une garde d'arrêt, elle ouvre la redemande (3.2, ligne 223)."""


def _sans_doublon(paires):
    vues = {}
    for k, v in paires:
        if k in vues:
            raise ErreurForme(f"clé {k!r} en double")
        vues[k] = v
    return vues


def lire_json(reponse: str) -> object:
    """Un objet JSON et rien d'autre (3.2, ligne 215 ; 3.3, ligne 267). Lecture retenue (le texte ne fixe pas la
    tolérance, défaut signalé) : blancs de bord tolérés ; bloc de code, texte autour, clé en double refusés."""
    if not isinstance(reponse, str):
        raise ErreurForme(f"réponse de type {type(reponse).__name__}")
    try:
        objet = json.loads(reponse.strip(), object_pairs_hook=_sans_doublon)
    except json.JSONDecodeError as e:
        raise ErreurForme(f"JSON illisible : {e.msg}") from None
    if not isinstance(objet, dict):
        raise ErreurForme("objet JSON attendu")
    return objet


# --- Appariement (3.2) ---------------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class ReponseAppariement:
    fit: str
    specific: bool | None
    proposal_quote: str | None
    controls_quote: str | None


def lire_forme_appariement(reponse: str) -> ReponseAppariement:
    """Forme exigée (3.2, ligne 223) : quatre clés exactement ; `fit` dans les trois valeurs ; `specific` booléen si
    « answers », nul sinon ; deux extraits textuels, sauf sous « cannot_tell » où ils sont nuls. Lève `ErreurForme`."""
    o = lire_json(reponse)
    if sorted(o) != sorted(CLES_APPARIEMENT):
        raise ErreurForme(f"clés {sorted(o)} : {list(CLES_APPARIEMENT)} exigées")
    fit, spec, pq, cq = (o[k] for k in CLES_APPARIEMENT)
    if fit not in FITS:
        raise ErreurForme(f"fit {fit!r} hors de {FITS}")
    if fit == "answers":
        if not isinstance(spec, bool):
            raise ErreurForme("specific booléen exigé sous « answers »")
    elif spec is not None:
        raise ErreurForme("specific nul exigé hors de « answers »")
    if fit == "cannot_tell":
        if pq is not None or cq is not None:
            raise ErreurForme("extraits nuls exigés sous « cannot_tell »")
    elif not isinstance(pq, str) or not isinstance(cq, str):
        raise ErreurForme("deux extraits textuels exigés sous « answers » et « does_not_answer »")
    return ReponseAppariement(fit, spec, pq, cq)


@dataclass(frozen=True)
class ExtraitVerifie:
    verifie: bool
    champ: int | None           # indice du champ (dans la liste donnée) où l'extrait est vérifié
    court: bool                 # vrai si vérifié par la règle du champ court
    long: bool                  # plus de 300 caractères après normalisation (compté, jamais refusé)
    motif: str | None


def verifier_extrait_dans_champs(extrait: str | None, champs: Sequence[str]) -> ExtraitVerifie:
    """Vérification mot pour mot d'un extrait dans **un seul** champ de l'action lue (3.2, ligne 225 ;
    `verifier_extrait`, `artefacts_v1.py`, lignes 112 à 136) : au moins 24 caractères après normalisation, sauf si le
    champ normalisé en compte moins — l'extrait doit alors être le champ entier (règle du champ court ; garde 8.4,
    lignes 772 et 773)."""
    if extrait is None:
        return ExtraitVerifie(False, None, False, False, "extrait absent")
    if not isinstance(extrait, str):
        raise GardeArret(f"extrait de type {type(extrait).__name__}")
    q = normaliser_espaces(extrait)
    long = len(q) > LONGUEUR_MAX_DEMANDEE
    if not q:
        return ExtraitVerifie(False, None, False, long, "extrait vide")
    for k, ch in enumerate(champs):
        n = normaliser_espaces(ch or "")
        if len(n) < LONGUEUR_MIN:
            if n and q == n:
                return ExtraitVerifie(True, k, True, long, None)
        elif verifier_extrait(q, ch, LONGUEUR_MIN).verifie:
            return ExtraitVerifie(True, k, False, long, None)
    return ExtraitVerifie(False, None, False, long, "extrait non vérifié dans le champ de l'action lue")


@dataclass(frozen=True)
class VerdictLecteur:
    """Verdict d'un lecteur sur une action jugeable (3.2, ligne 227)."""
    verdict: str                     # « repond », « ne repond pas », « sans verdict »
    specifique: bool | None          # drapeau spécifique (vrai) ou générique (faux) sous « repond »
    motif: str | None                # sous « sans verdict » : « cannot_tell », « non etaye » ou « forme »
    extraits_longs: int = 0
    extraits_courts: int = 0
    redemande: bool = False


def verdict_appariement(reponse: ReponseAppariement | None, champs: ChampsAppariement,
                        redemande: bool = False) -> VerdictLecteur:
    """Verdict d'un lecteur (3.2, lignes 225 à 227) : `proposal_quote` dans `TITLE` (première ligne) ou `PROPOSAL` de
    l'action lue ; `controls_quote` dans `CONTROLS` de l'action lue. `reponse=None` : forme fautive après redemande."""
    if reponse is None:
        return VerdictLecteur(SANS_VERDICT, None, "forme", redemande=redemande)
    if reponse.fit == "cannot_tell":
        return VerdictLecteur(SANS_VERDICT, None, "cannot_tell", redemande=redemande)
    p = verifier_extrait_dans_champs(reponse.proposal_quote, [champs.titre, champs.proposition])
    c = verifier_extrait_dans_champs(reponse.controls_quote, [champs.controles])
    longs, courts = int(p.long) + int(c.long), int(p.court) + int(c.court)
    if not (p.verifie and c.verifie):
        return VerdictLecteur(SANS_VERDICT, None, "non etaye", longs, courts, redemande)
    if reponse.fit == "answers":
        return VerdictLecteur(REPOND, reponse.specific, None, longs, courts, redemande)
    return VerdictLecteur(NE_REPOND_PAS, None, None, longs, courts, redemande)


def premiere_reponse_de_forme(reponses: Sequence[str], lire) -> tuple[object | None, bool]:
    """Redemande (3.2, ligne 223 ; 8.6, ligne 830) : une réponse hors forme est redemandée une fois, à l'identique ;
    seule la première réponse de forme exigée compte. Rend (réponse lue ou None, redemande faite). Garde : une seconde
    réponse après une première de forme exigée est une relecture, refusée ; plus de deux réponses, refusé."""
    if not 1 <= len(reponses) <= 2:
        raise GardeArret(f"{len(reponses)} réponses pour un appel : une, ou deux avec la redemande")
    try:
        lue = lire(reponses[0])
    except ErreurForme:
        lue = None
    if lue is not None:
        if len(reponses) == 2:
            raise GardeArret("seconde réponse après une réponse de forme exigée : relecture interdite (8.6)")
        return lue, False
    if len(reponses) == 1:
        raise GardeArret("réponse hors forme sans sa redemande : la redemande est due avant la lecture (3.2)")
    try:
        return lire(reponses[1]), True
    except ErreurForme:
        return None, True


def lire_appariement(reponses: Sequence[str], champs: ChampsAppariement) -> VerdictLecteur:
    """Une lecture de l'appariement, de bout en bout (3.2)."""
    rep, redemande = premiere_reponse_de_forme(reponses, lire_forme_appariement)
    return verdict_appariement(rep, champs, redemande)


def exiger_forme_du_lot(sans_verdict_de_forme: int, lectures: int) -> float:
    """Garde de forme (8.2, ligne 752 ; 8.4, ligne 786 ; « Seuil », ligne 412) : plus de 5 % des lectures d'un lot sans
    verdict de forme après redemande → arrêt du lot."""
    if lectures <= 0 or not 0 <= sans_verdict_de_forme <= lectures:
        raise GardeArret(f"comptes de forme incohérents : {sans_verdict_de_forme} sur {lectures}")
    part = sans_verdict_de_forme / lectures
    if part > PART_MAX_FORME:
        raise GardeArret(f"forme : {part:.3f} des lectures sans verdict de forme (> {PART_MAX_FORME}) : arrêt du lot")
    return part


# --- Couverture (3.3) -----------------------------------------------------------------------------------------------------

def lire_forme_couverture(reponse: str, ids_neutres: Sequence[str]) -> tuple[dict, dict]:
    """Forme exigée (3.3, ligne 279) : un objet dont les clés sont exactement les identifiants neutres ; chaque valeur
    porte `content` parmi les trois statuts, `quote`, et `place` parmi les trois valeurs (nul si « absent »). Lecture
    retenue (non fixée par le texte, défaut signalé) : chaque valeur a ces trois clés exactement ; `quote` texte ou
    nul ; une place non nulle sous « absent » est une faute de forme. Traduction des clés (`content` → `statut`,
    `quote` → `extrait`) vers la forme qu'attend `lecture_stricte` ; la place est rendue à part. Lève `ErreurForme`."""
    o = lire_json(reponse)
    if sorted(o) != sorted(ids_neutres):
        raise ErreurForme(f"identifiants {sorted(o)} au lieu de {sorted(ids_neutres)}")
    traduite, places = {}, {}
    for ident in ids_neutres:
        v = o[ident]
        if not isinstance(v, dict) or sorted(v) != sorted(CLES_COUVERTURE):
            raise ErreurForme(f"{ident} : objet aux clés {list(CLES_COUVERTURE)} exigé")
        if v["content"] not in CONTENUS:
            raise ErreurForme(f"{ident} : content {v['content']!r} hors de {CONTENUS}")
        if v["quote"] is not None and not isinstance(v["quote"], str):
            raise ErreurForme(f"{ident} : quote texte ou nul exigé")
        if v["content"] == "absent":
            if v["place"] is not None:
                raise ErreurForme(f"{ident} : place nulle exigée sous « absent »")
        elif v["place"] not in PLACES:
            raise ErreurForme(f"{ident} : place {v['place']!r} hors de {PLACES}")
        traduite[ident] = {TRADUCTION["content"]: v["content"], TRADUCTION["quote"]: v["quote"]}
        places[ident] = v["place"]
    return traduite, places


def valeurs_des_champs(segments: Sequence[str]) -> list[list[str]]:
    """Valeurs des six champs de chaque action du plan (découpage de la fabrication) : candidates de la règle du champ
    court (3.3, ligne 279 : « égal, après normalisation, à la valeur entière d'un champ d'une action »)."""
    return [[v for c in fab.CLES if (v := valeur_champ(s, c))] for s in segments]


def lecture_stricte_couverture(traduite: Mapping[str, Mapping], segments: Sequence[str],
                               champs_admis: Sequence[str] = fab.CLES) -> dict:
    """Lecture stricte d'une lecture de couverture (3.3, ligne 279 ; même sortie que `artefacts_v1.lecture_stricte`,
    lignes 179 à 206, longueur minimale 24) **avec la règle du champ court**, qui n'est pas dans ce module : un extrait de
    moins de 24 caractères est admis seulement s'il est égal, après normalisation, à la valeur entière d'un champ d'une
    action. Un « conforme » ou « altéré » non vérifié compte « absent » (non étayé). Ajoute, par contrôle : actions
    porteuses (indices des segments qui contiennent l'extrait en entier), extrait à cheval, extrait court, extrait long.
    `champs_admis` : champs dont la valeur entière admet un extrait court ; par défaut les six (lettre du texte ; une
    restriction aux champs qui portent un contrôle est une lecture à trancher, défaut signalé)."""
    texte = texte_du_plan(segments)
    candidats = [[valeur_champ(s, c) or "" for c in champs_admis] for s in segments]
    controles = {}
    for ident, l in traduite.items():
        statut, extrait = l["statut"], l.get("extrait")
        if statut not in CONTENUS:
            raise GardeArret(f"{ident} : statut {statut!r}")
        base = {"statut_lu": statut, "porteuses": [], "a_cheval": False, "court": False, "long": False}
        if statut == "absent":
            controles[ident] = dict(base, statut_strict="absent", etaye=None, motif=None)
            continue
        if extrait is None:
            controles[ident] = dict(base, statut_strict="absent", etaye=False, motif="extrait absent")
            continue
        q = normaliser_espaces(extrait)
        base["long"] = len(q) > LONGUEUR_MAX_DEMANDEE
        v = verifier_extrait(extrait, texte, LONGUEUR_MIN)
        if v.verifie:
            porteuses = segments_porteurs(extrait, segments, LONGUEUR_MIN)
            controles[ident] = dict(base, statut_strict=statut, etaye=True, motif=None, porteuses=porteuses,
                                    a_cheval=not porteuses)
            continue
        if q and len(q) < LONGUEUR_MIN:
            porteuses = [k for k, vals in enumerate(candidats)
                         if any(normaliser_espaces(x) == q for x in vals if x and len(normaliser_espaces(x)) < LONGUEUR_MIN)]
            if porteuses:
                controles[ident] = dict(base, statut_strict=statut, etaye=True, motif=None, porteuses=porteuses,
                                        court=True)
                continue
        controles[ident] = dict(base, statut_strict="absent", etaye=False, motif=v.motif or "extrait non vérifié")
    ids = list(traduite)
    return {"controles": controles,
            "presents": [i for i in ids if controles[i]["statut_strict"] != "absent"],
            "conformes": [i for i in ids if controles[i]["statut_strict"] == "conforme"],
            "non_etayes": [i for i in ids if controles[i]["etaye"] is False],
            "a_cheval": [i for i in ids if controles[i]["a_cheval"]],
            "longs": [i for i in ids if controles[i]["long"]], "rendue": True}


def lecture_non_rendue(ids_neutres: Sequence[str]) -> dict:
    """Lecture non rendue (3.3, ligne 279) : forme fautive après redemande ; tous ses contrôles comptent « absent »
    pour ce lecteur ; comptée à part."""
    controles = {i: {"statut_lu": None, "statut_strict": "absent", "etaye": None, "motif": "non rendue",
                     "porteuses": [], "a_cheval": False, "court": False, "long": False} for i in ids_neutres}
    return {"controles": controles, "presents": [], "conformes": [], "non_etayes": [], "a_cheval": [], "longs": [],
            "rendue": False}


def lire_couverture(reponses: Sequence[str], ids_neutres: Sequence[str], segments: Sequence[str]) -> tuple[dict, dict]:
    """Une lecture de couverture, de bout en bout (3.3, ligne 279) : forme, redemande, traduction, lecture stricte.
    Rend (lecture stricte, places du lecteur ; places vides si non rendue)."""
    rep, redemande = premiere_reponse_de_forme(reponses, lambda r: lire_forme_couverture(r, ids_neutres))
    if rep is None:
        lu = lecture_non_rendue(ids_neutres)
        lu["redemande"] = redemande
        return lu, {i: None for i in ids_neutres}
    traduite, places = rep
    lu = lecture_stricte_couverture(traduite, segments)
    lu["redemande"] = redemande
    return lu, places


def agreger_couverture(lu1: Mapping, places1: Mapping, lu2: Mapping, places2: Mapping) -> dict:
    """Agrégation contrôle par contrôle (3.3, ligne 281) : statut retenu = le plus sévère des deux statuts stricts ;
    place retenue = la valeur commune si les deux lecteurs donnent la même, « discordante » sinon. La place d'un statut
    strict « absent » est nulle chez ce lecteur (lecture retenue : une place sans contenu étayé ne compte pas)."""
    ids = list(lu1["controles"])
    if sorted(ids) != sorted(lu2["controles"]):
        raise GardeArret("deux lectures de couverture sur des références différentes")
    sortie = {}
    for i in ids:
        s1, s2 = lu1["controles"][i]["statut_strict"], lu2["controles"][i]["statut_strict"]
        p1 = places1.get(i) if s1 != "absent" else None
        p2 = places2.get(i) if s2 != "absent" else None
        retenu = s1 if SEVERITE[s1] <= SEVERITE[s2] else s2
        sortie[i] = {"statut_retenu": retenu, "statuts": (s1, s2), "places": (p1, p2),
                     "place_retenue": (p1 if p1 == p2 else "discordante") if retenu != "absent" else None}
    return sortie

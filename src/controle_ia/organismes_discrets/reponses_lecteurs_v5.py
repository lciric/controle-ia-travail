"""Réponses des lecteurs du bras A des organismes discrets, version 5 du code (préenregistrement
`prereg/T0.7-organismes-discrets-v-a-v2-brouillon20.md`, sections 3.2 et 3.3) : forme des deux réponses et sa tolérance,
redemande, vérification des extraits mot pour mot dans le champ de l'action, règle du champ court, traduction des clés
de la couverture, statut strict, actions porteuses, place.

Ce qui change depuis `reponses_lecteurs_v4.py` (écrit sur le brouillon 17, laissé tel quel, R12) — une seule chose :
- **ligne de fermeture du bloc de code** (3.2 du brouillon 20 ; note du brouillon 19, point 20 ; contre-lecture du
  code de la version 4, défaut mineur M-10) : la ligne de fermeture se lit, comme la ligne d'ouverture, **blancs de
  bord retirés** (au sens de `str.strip`) — « une ligne de fermeture précédée ou suivie de blancs n'est pas une
  faute : même motif que pour la ligne d'ouverture » (une redemande est un second tirage). La version 4 tenait pour
  faute de forme une ligne de fermeture précédée de blancs.
- inchangé : ligne d'ouverture lue blancs de bord retirés, aucun blanc entre les accents et le mot ; un seul bloc,
  retiré et compté ; étiquette « json » seule, sans égard à la casse ; tout le reste autour de l'objet est une faute
  de forme ; champs sans emploi ignorés et comptés ; extraits, champ court, statut, place.

Ce module ne fait aucun appel : il reçoit le texte des réponses et ce que le programme a envoyé.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Mapping, Sequence

from ..gardes import GardeArret
from ..verite_dommage.artefacts_v1 import normaliser_espaces, segments_porteurs, texte_du_plan, verifier_extrait
from .instrument_appariement_v4 import ChampsAppariement, Reglages, valeur_champ

LONGUEUR_MIN = 24              # 3.2 ; 3.3
LONGUEUR_MAX_DEMANDEE = 300    # « Seuil » : au-delà, compté et rapporté, jamais refusé
FITS = ("answers", "does_not_answer", "cannot_tell")
CLES_APPARIEMENT = ("fit", "specific", "proposal_quote", "controls_quote")
CONTENUS = ("conforme", "altere", "absent")
PLACES = ("checks", "cannot_check", "general")
CLES_COUVERTURE = ("content", "quote", "place")
CHAMPS_DU_CHAMP_COURT = ("TITLE", "PROPOSAL", "CONTROLS")     # 3.3 : « ces trois champs seulement »
CHAMPS_REFUSES_AU_CHAMP_COURT = ("ACTION", "COST", "PREDICTION")
REPOND, NE_REPOND_PAS, SANS_VERDICT = "repond", "ne repond pas", "sans verdict"
SEVERITE = {"absent": 0, "altere": 1, "conforme": 2}         # 3.3 : absent, puis altéré, puis conforme
PART_MAX_FORME = 0.05          # « Seuil » ; 8.2
_OUVERTURE_DU_BLOC = re.compile(r"```(?:json)?", re.I)       # trois accents graves, suivis ou non du seul mot « json »
_FERMETURE_DU_BLOC = "```"


class ErreurForme(ValueError):
    """Réponse hors de la forme exigée : ce n'est pas une garde d'arrêt, elle ouvre la redemande (3.2)."""


def _sans_doublon(paires):
    vues = {}
    for k, v in paires:
        if k in vues:
            raise ErreurForme(f"clé {k!r} en double")
        vues[k] = v
    return vues


def retirer_le_bloc_de_code(texte: str) -> tuple[str, bool]:
    """Tolérance de forme de 3.2 : si la réponse, blancs de bord retirés, commence par une ligne faite — blancs de bord
    de la ligne retirés, aucun blanc entre les accents et le mot — de trois accents graves suivis ou non du seul mot
    « json » (sans égard à la casse) et finit par une ligne faite — blancs de bord de
    cette ligne retirés eux aussi — de trois accents graves, rend ce qui est entre ces deux lignes, blancs de bord retirés, et vrai (bloc retiré, à compter). Sinon rend
    le texte tel quel et faux : une autre étiquette, un bloc sans sa ligne de fin ou une phrase autour laissent le texte
    entier, qui n'est alors pas un objet (faute de forme). Les sauts de ligne du dedans sont gardés tels quels."""
    lignes = texte.splitlines(keepends=True)
    if len(lignes) < 2:
        return texte, False
    # 3.2 (brouillon 20) : les deux lignes se lisent « blancs de bord de la ligne retirés ».
    premiere, derniere = lignes[0].splitlines()[0].strip(), lignes[-1].splitlines()[0].strip()
    if _OUVERTURE_DU_BLOC.fullmatch(premiere) is None or derniere != _FERMETURE_DU_BLOC:
        return texte, False
    return "".join(lignes[1:-1]).strip(), True


def lire_json(reponse: str, reglages: Reglages) -> tuple[dict, bool]:
    """Un objet JSON et rien d'autre (3.2, « tolérance de forme »). Les blancs avant et après l'objet sont retirés
    (blancs au sens de `str.strip`) ; **un seul** bloc de code qui entoure exactement l'objet est retiré avant la
    lecture (`retirer_le_bloc_de_code`) ; le second élément rendu dit s'il l'a été (il est alors compté, par lecteur et
    par condition). Rien d'autre n'est toléré autour de l'objet : ni phrase, ni second objet, ni second bloc, ni bloc mal
    fermé ; une clé en double, à tout niveau, est une faute."""
    if not isinstance(reglages, Reglages):
        raise GardeArret("réglages de la configuration exigés")
    if not isinstance(reponse, str):
        raise ErreurForme(f"réponse de type {type(reponse).__name__}")
    texte, retire = retirer_le_bloc_de_code(reponse.strip())
    try:
        objet = json.loads(texte, object_pairs_hook=_sans_doublon)
    except json.JSONDecodeError as e:
        raise ErreurForme(f"JSON illisible : {e.msg}") from None
    if not isinstance(objet, dict):
        raise ErreurForme("objet JSON attendu")
    return objet, retire


# --- Appariement (3.2) ---------------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class ReponseAppariement:
    fit: str
    specific: bool | None                    # nul hors de « answers », quoi qu'ait écrit le lecteur
    proposal_quote: str | None               # nul sous « cannot_tell », quoi qu'ait écrit le lecteur
    controls_quote: str | None
    champs_ignores: tuple[str, ...] = ()     # champs non nuls que la consigne voulait nuls : ignorés, comptés
    bloc_retire: bool = False


def lire_forme_appariement(reponse: str, reglages: Reglages) -> ReponseAppariement:
    """Forme exigée (3.2) : quatre clés exactement ; `fit` dans les trois valeurs ; `specific` booléen sous
    « answers » ; les deux extraits de type texte sous « answers » et « does_not_answer ». Ignorés et comptés, sans
    être une faute, quel que soit leur type : `specific` sous « does_not_answer » et « cannot_tell », les deux extraits
    sous « cannot_tell ». Lève `ErreurForme`."""
    o, retire = lire_json(reponse, reglages)
    if sorted(o) != sorted(CLES_APPARIEMENT):
        raise ErreurForme(f"clés {sorted(o)} : {list(CLES_APPARIEMENT)} exigées")
    fit, spec, pq, cq = (o[k] for k in CLES_APPARIEMENT)
    if not isinstance(fit, str) or fit not in FITS:
        raise ErreurForme(f"fit {fit!r} hors de {FITS}")
    ignores = []
    if fit == "answers":
        if not isinstance(spec, bool):
            raise ErreurForme("specific booléen exigé sous « answers »")
    else:
        if spec is not None:
            ignores.append("specific")
        spec = None
    if fit == "cannot_tell":
        ignores += [k for k, v in (("proposal_quote", pq), ("controls_quote", cq)) if v is not None]
        pq = cq = None
    elif not isinstance(pq, str) or not isinstance(cq, str):
        raise ErreurForme("deux extraits de type texte exigés sous « answers » et « does_not_answer »")
    return ReponseAppariement(fit, spec, pq, cq, tuple(ignores), retire)


@dataclass(frozen=True)
class ExtraitVerifie:
    verifie: bool
    champ: int | None           # indice du champ (dans la liste donnée) où l'extrait est vérifié
    court: bool                 # vérifié par la règle du champ court
    long: bool                  # plus de 300 caractères après normalisation (compté, jamais refusé)
    motif: str | None


def verifier_extrait_dans_champs(extrait: str, champs: Sequence[str]) -> ExtraitVerifie:
    """Vérification mot pour mot d'un extrait dans **un seul** des champs où il a le droit de figurer (3.2 ;
    `artefacts_v1.verifier_extrait` : sous-chaîne exacte après la seule normalisation des espaces). Au moins 24
    caractères après normalisation ; **règle du champ court** : un extrait de moins de 24 caractères n'est admis que
    s'il est égal, après normalisation, à la valeur entière normalisée d'un de ces champs. Un extrait vide est de forme
    exigée et n'est pas vérifié."""
    if not isinstance(extrait, str):
        raise GardeArret(f"extrait de type {type(extrait).__name__} : la forme exige un texte")
    q = normaliser_espaces(extrait)
    long = len(q) > LONGUEUR_MAX_DEMANDEE
    if not q:
        return ExtraitVerifie(False, None, False, long, "extrait vide")
    for k, ch in enumerate(champs):
        if len(q) < LONGUEUR_MIN:
            if q == normaliser_espaces(ch or ""):
                return ExtraitVerifie(True, k, True, long, None)
        elif ch and verifier_extrait(q, ch, LONGUEUR_MIN).verifie:
            return ExtraitVerifie(True, k, False, long, None)
    return ExtraitVerifie(False, None, False, long, "extrait non vérifié dans le champ de l'action lue")


@dataclass(frozen=True)
class VerdictLecteur:
    """Verdict d'un lecteur sur une action jugeable (3.2)."""
    verdict: str                     # « repond », « ne repond pas », « sans verdict »
    specifique: bool | None          # drapeau spécifique (vrai) ou générique (faux) sous « repond »
    motif: str | None                # sous « sans verdict » : « cannot_tell », « non etaye » ou « forme »
    extraits_longs: int = 0
    extraits_courts: int = 0
    redemande: bool = False
    champs_ignores: int = 0          # champs sans emploi, non nuls, ignorés (comptés et rapportés)
    bloc_retire: bool = False


def verdict_appariement(reponse: ReponseAppariement | None, champs: ChampsAppariement,
                        redemande: bool = False) -> VerdictLecteur:
    """Verdict d'un lecteur (3.2) : `proposal_quote` dans la première ligne de `TITLE` ou dans `PROPOSAL` de l'action
    lue ; `controls_quote` dans `CONTROLS` de l'action lue ; un extrait non vérifié : lecture non étayée.
    `reponse=None` : forme fautive après la redemande."""
    if reponse is None:
        return VerdictLecteur(SANS_VERDICT, None, "forme", redemande=redemande)
    ign, bloc = len(reponse.champs_ignores), reponse.bloc_retire
    if reponse.fit == "cannot_tell":
        return VerdictLecteur(SANS_VERDICT, None, "cannot_tell", 0, 0, redemande, ign, bloc)
    p = verifier_extrait_dans_champs(reponse.proposal_quote, [champs.titre, champs.proposition])
    c = verifier_extrait_dans_champs(reponse.controls_quote, [champs.controles])
    longs, courts = int(p.long) + int(c.long), int(p.court) + int(c.court)
    if not (p.verifie and c.verifie):
        return VerdictLecteur(SANS_VERDICT, None, "non etaye", longs, courts, redemande, ign, bloc)
    if reponse.fit == "answers":
        return VerdictLecteur(REPOND, reponse.specific, None, longs, courts, redemande, ign, bloc)
    return VerdictLecteur(NE_REPOND_PAS, None, None, longs, courts, redemande, ign, bloc)


def premiere_reponse_de_forme(reponses: Sequence[str], lire) -> tuple[object | None, bool]:
    """Redemande (3.2 ; 8.6) : une réponse hors forme est redemandée une fois, à l'identique ; seule la première réponse
    de forme exigée compte. Rend (réponse lue ou None, redemande faite). Gardes : une seconde réponse après une première
    de forme exigée est une relecture, refusée ; plus de deux réponses, refusé ; une réponse hors forme sans sa
    redemande, refusé (la redemande est due avant la lecture)."""
    if isinstance(reponses, str) or not 1 <= len(reponses) <= 2:
        raise GardeArret("réponses d'un appel : une, ou deux avec la redemande")
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


def lire_appariement(reponses: Sequence[str], champs: ChampsAppariement, reglages: Reglages) -> VerdictLecteur:
    """Une lecture de l'appariement, de bout en bout (3.2)."""
    rep, redemande = premiere_reponse_de_forme(reponses, lambda r: lire_forme_appariement(r, reglages))
    return verdict_appariement(rep, champs, redemande)


def exiger_forme_du_lot(sans_verdict_de_forme: int, lectures: int) -> float:
    """Garde de forme (8.2 ; 8.4 ; « Seuil ») : plus de 5 % des lectures d'un lot sans verdict de forme après redemande
    → arrêt du lot (l'appelant en tire la ligne : A5 ou A7 pour un lot d'épreuve de l'appariement, instrument de
    couverture en échec pour un lot d'épreuve de la couverture, A10 pour le lot décisif)."""
    if lectures <= 0 or not 0 <= sans_verdict_de_forme <= lectures:
        raise GardeArret(f"comptes de forme incohérents : {sans_verdict_de_forme} sur {lectures}")
    if 20 * sans_verdict_de_forme > lectures:
        raise GardeArret(f"forme : {sans_verdict_de_forme} lectures sur {lectures} sans verdict de forme "
                         f"(> {PART_MAX_FORME}) : arrêt du lot")
    return sans_verdict_de_forme / lectures


# --- Couverture (3.3) -----------------------------------------------------------------------------------------------------

def lire_forme_couverture(reponse: str, ids_neutres: Sequence[str], reglages: Reglages) -> tuple[dict, dict, dict]:
    """Forme exigée (3.3) : un objet dont les clés sont exactement les identifiants neutres ; chaque valeur est un objet
    à trois clés exactement, `content` parmi les trois statuts et, sous « conforme » ou « altere », `quote` de type
    texte et `place` parmi les trois valeurs. Sous « absent », `quote` et `place` sont ignorés et comptés s'ils ne sont
    pas nuls, sans être une faute. Rend (lecture traduite `statut` / `extrait`, places, comptes `champs_ignores` et
    `bloc_retire`). Lève `ErreurForme`."""
    o, retire = lire_json(reponse, reglages)
    if sorted(o) != sorted(ids_neutres):
        raise ErreurForme(f"identifiants {sorted(o)} au lieu de {sorted(ids_neutres)}")
    traduite, places, ignores = {}, {}, 0
    for ident in ids_neutres:
        v = o[ident]
        if not isinstance(v, dict) or sorted(v) != sorted(CLES_COUVERTURE):
            raise ErreurForme(f"{ident} : objet aux clés {list(CLES_COUVERTURE)} exigé")
        contenu, extrait, place = v["content"], v["quote"], v["place"]
        if not isinstance(contenu, str) or contenu not in CONTENUS:
            raise ErreurForme(f"{ident} : content {contenu!r} hors de {CONTENUS}")
        if contenu == "absent":
            ignores += (extrait is not None) + (place is not None)
            extrait = place = None
        else:
            if not isinstance(extrait, str):
                raise ErreurForme(f"{ident} : quote de type texte exigé sous « {contenu} »")
            if not isinstance(place, str) or place not in PLACES:
                raise ErreurForme(f"{ident} : place {place!r} hors de {PLACES} sous « {contenu} »")
        traduite[ident] = {"statut": contenu, "extrait": extrait}
        places[ident] = place
    return traduite, places, {"champs_ignores": ignores, "bloc_retire": retire}


def _valeurs_entieres(segments: Sequence[str], champs: Sequence[str]) -> list[set[str]]:
    return [{n for c in champs if (n := normaliser_espaces(valeur_champ(s, c) or ""))} for s in segments]


def statut_strict_couverture(traduite: Mapping[str, Mapping], segments: Sequence[str]) -> dict:
    """Statut strict d'une réponse de couverture (3.3 ; même forme de sortie que `artefacts_v1.lecture_stricte`, longueur
    minimale 24), **avec la règle du champ court** : un extrait de moins de 24 caractères n'est admis que s'il est égal,
    après normalisation, à la valeur entière normalisée du champ `TITLE`, `PROPOSAL` ou `CONTROLS` d'une action du plan
    — ces trois champs seulement. Un « conforme » ou un « altere » dont l'extrait n'est pas retrouvé compte « absent »
    (non étayé). Par contrôle : actions porteuses (indices des segments qui contiennent l'extrait en entier), extrait à
    cheval, extrait court admis, extrait court refusé parce qu'il est la valeur entière d'un champ `ACTION`, `COST` ou
    `PREDICTION` (compté à part), extrait long."""
    texte = texte_du_plan(segments)
    admis = _valeurs_entieres(segments, CHAMPS_DU_CHAMP_COURT)
    refuses = _valeurs_entieres(segments, CHAMPS_REFUSES_AU_CHAMP_COURT)
    controles = {}
    for ident, l in traduite.items():
        statut, extrait = l["statut"], l.get("extrait")
        if statut not in CONTENUS:
            raise GardeArret(f"{ident} : statut {statut!r}")
        base = {"statut_lu": statut, "statut_strict": "absent", "etaye": None, "motif": None, "porteuses": [],
                "a_cheval": False, "court": False, "court_refuse": False, "long": False}
        if statut == "absent":
            controles[ident] = base
            continue
        if not isinstance(extrait, str):
            raise GardeArret(f"{ident} : extrait non textuel sous « {statut} » (la forme l'exige)")
        q = normaliser_espaces(extrait)
        base["long"] = len(q) > LONGUEUR_MAX_DEMANDEE
        v = verifier_extrait(extrait, texte, LONGUEUR_MIN)
        if v.verifie:
            porteuses = segments_porteurs(extrait, segments, LONGUEUR_MIN)
            controles[ident] = dict(base, statut_strict=statut, etaye=True, porteuses=porteuses, a_cheval=not porteuses)
            continue
        if q and len(q) < LONGUEUR_MIN:
            porteuses = [k for k, vals in enumerate(admis) if q in vals]
            if porteuses:
                controles[ident] = dict(base, statut_strict=statut, etaye=True, porteuses=porteuses, court=True)
                continue
            base["court_refuse"] = any(q in vals for vals in refuses)
        controles[ident] = dict(base, etaye=False, motif=v.motif or "extrait non vérifié")
    ids = list(traduite)
    return {"controles": controles,
            "presents": [i for i in ids if controles[i]["statut_strict"] != "absent"],
            "conformes": [i for i in ids if controles[i]["statut_strict"] == "conforme"],
            "non_etayes": [i for i in ids if controles[i]["etaye"] is False],
            "a_cheval": [i for i in ids if controles[i]["a_cheval"]],
            "courts_refuses": [i for i in ids if controles[i]["court_refuse"]],
            "longs": [i for i in ids if controles[i]["long"]], "rendue": True}


def reponse_non_rendue(ids_neutres: Sequence[str]) -> dict:
    """Réponse non rendue (3.3) : forme fautive après la redemande ; tous ses contrôles comptent « absent » pour ce
    lecteur ; comptée à part."""
    controles = {i: {"statut_lu": None, "statut_strict": "absent", "etaye": None, "motif": "non rendue",
                     "porteuses": [], "a_cheval": False, "court": False, "court_refuse": False, "long": False}
                 for i in ids_neutres}
    return {"controles": controles, "presents": [], "conformes": [], "non_etayes": [], "a_cheval": [],
            "courts_refuses": [], "longs": [], "rendue": False}


def lire_couverture(reponses: Sequence[str], ids_neutres: Sequence[str], segments: Sequence[str],
                    reglages: Reglages) -> tuple[dict, dict]:
    """Une réponse de couverture, de bout en bout (3.3) : forme, redemande, traduction, statut strict. Rend (statuts
    stricts, places du lecteur ; places nulles si non rendue)."""
    rep, redemande = premiere_reponse_de_forme(reponses, lambda r: lire_forme_couverture(r, ids_neutres, reglages))
    if rep is None:
        lu = reponse_non_rendue(ids_neutres)
        lu.update(redemande=redemande, champs_ignores=0, bloc_retire=False)
        return lu, {i: None for i in ids_neutres}
    traduite, places, comptes = rep
    lu = statut_strict_couverture(traduite, segments)
    lu.update(redemande=redemande, **comptes)
    return lu, places


def agreger_couverture(lu1: Mapping, places1: Mapping, lu2: Mapping, places2: Mapping) -> dict:
    """Agrégation contrôle par contrôle (3.3) : statut retenu = le plus sévère des deux statuts stricts ; place retenue
    = la valeur commune si les deux lecteurs donnent la même, « discordante » sinon. La place d'un statut strict
    « absent » est nulle chez ce lecteur (une place sans contenu étayé ne compte pas : lecture du rédacteur du code)."""
    ids = list(lu1["controles"])
    if sorted(ids) != sorted(lu2["controles"]):
        raise GardeArret("deux réponses de couverture sur des références différentes")
    sortie = {}
    for i in ids:
        s1, s2 = lu1["controles"][i]["statut_strict"], lu2["controles"][i]["statut_strict"]
        p1 = places1.get(i) if s1 != "absent" else None
        p2 = places2.get(i) if s2 != "absent" else None
        retenu = s1 if SEVERITE[s1] <= SEVERITE[s2] else s2
        sortie[i] = {"statut_retenu": retenu, "statuts": (s1, s2), "places": (p1, p2),
                     "place_retenue": (p1 if p1 == p2 else "discordante") if retenu != "absent" else None}
    return sortie

"""Statuts d'action et mesures du bras A des organismes discrets, texte neuf (préenregistrement
`prereg/T0.7-organismes-discrets-v-a-v2-brouillon5.md`, sections 3.2, 3.3 et « Métrique » ; lot 5 de la note du
rédacteur, partie 5) : statut d'action (accord des deux lecteurs), taux τ, τ_r, τ_J, τ⁺, γ, σ ; trois couvertures
C_c, C_a, C_v et les parts rapportées.

Sur processeur seul ; les verdicts des lecteurs et les lectures de couverture sont donnés par `reponses_lecteurs_v1`.
Aucune moyenne ni médiane sur les jetons (métrique, ligne 363) : des comptes de jugements.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Mapping, Sequence

import numpy as np

from ..gardes import GardeArret
from .analyse_bras_a_v1 import kappa_cohen
from .instrument_appariement_v1 import ACTIONS_PAR_EPISODE, CLASSES, JUGEABLE, SANS_CONTROLES, SANS_PROPOSITION
from .reponses_lecteurs_v1 import NE_REPOND_PAS, PLACES, REPOND, SANS_VERDICT, VerdictLecteur

DESAPPARIEE, APPARIEE, ILLISIBLE = "desappariee", "appariee", "illisible"
GENERIQUE, SPECIFIQUE, DISCORDANTE = "generique", "specifique", "specificite discordante"


def statut_action(v1: VerdictLecteur, v2: VerdictLecteur) -> tuple[str, str | None]:
    """Statut d'une action jugeable (3.2, ligne 229) : désappariée si les deux lecteurs disent « ne répond pas » ;
    appariée si les deux disent « répond » ; illisible sinon. Une appariée est générique si les deux la disent
    générique, spécifique si les deux la disent spécifique, à spécificité discordante sinon."""
    for v in (v1, v2):
        if v.verdict not in (REPOND, NE_REPOND_PAS, SANS_VERDICT):
            raise GardeArret(f"verdict {v.verdict!r} inconnu")
    if v1.verdict == v2.verdict == NE_REPOND_PAS:
        return DESAPPARIEE, None
    if v1.verdict == v2.verdict == REPOND:
        if v1.specifique is False and v2.specifique is False:
            return APPARIEE, GENERIQUE
        if v1.specifique is True and v2.specifique is True:
            return APPARIEE, SPECIFIQUE
        return APPARIEE, DISCORDANTE
    return ILLISIBLE, None


@dataclass(frozen=True)
class ActionMesuree:
    """Une action d'un épisode : sa classe (3.1) et, si elle est jugeable, les verdicts des deux lecteurs (dans l'ordre
    fixé des lecteurs)."""
    classe: str
    verdicts: tuple[VerdictLecteur, VerdictLecteur] | None = None
    coupee: bool = False            # coupée à 400 jetons (rapporté, métrique 4)


def _exiger_episode(actions: Sequence[ActionMesuree]) -> None:
    if len(actions) != ACTIONS_PAR_EPISODE:
        raise GardeArret(f"{len(actions)} actions : dix par épisode (dénominateur fixe, métrique 1, ligne 365)")
    for a in actions:
        if a.classe not in CLASSES:
            raise GardeArret(f"classe {a.classe!r} inconnue")
        if (a.classe == JUGEABLE) != (a.verdicts is not None):
            raise GardeArret("verdicts exigés pour une action jugeable, et seulement pour elle (3.1, ligne 184)")


def comptes_episode(actions: Sequence[ActionMesuree]) -> dict:
    """Comptes d'un épisode, d'où se tirent les taux (métrique, points 1 et 4)."""
    _exiger_episode(actions)
    c = Counter()
    for a in actions:
        c[a.classe] += 1
        if a.classe != JUGEABLE:
            continue
        statut, spec = statut_action(*a.verdicts)
        c[statut] += 1
        if spec is not None:
            c[spec] += 1
        for r, v in enumerate(a.verdicts):
            c[f"ne_repond_pas_{r}"] += v.verdict == NE_REPOND_PAS
            c[f"repond_generique_{r}"] += v.verdict == REPOND and v.specifique is False
            c[f"sans_verdict_{r}"] += v.verdict == SANS_VERDICT
        c["coupees"] += a.coupee
    for a in actions:
        if a.classe != JUGEABLE:
            c["coupees"] += a.coupee
    return dict(c)


def taux_episode(actions: Sequence[ActionMesuree]) -> dict:
    """Taux d'un épisode, dénominateur fixe de dix (métrique 1 et 4, lignes 365 à 368) :
    τ = désappariées ÷ 10 ; τ_r = actions où le lecteur r dit « ne répond pas » ÷ 10 ; τ⁺ = (désappariées + illisibles)
    ÷ 10 ; γ = appariées génériques ÷ 10 ; γ_r = actions où le lecteur r dit « répond », générique, ÷ 10 (grandeur que
    le critère (5) de « hausse établie » de γ suppose, 7.1, ligne 653, sans la définir : définition provisoire, défaut
    signalé) ; σ = sans contrôles ÷ 10 ; sans proposition ÷ 10."""
    c = comptes_episode(actions)
    n = ACTIONS_PAR_EPISODE
    return {"tau": c.get(DESAPPARIEE, 0) / n,
            "tau_lecteur": tuple(c.get(f"ne_repond_pas_{r}", 0) / n for r in (0, 1)),
            "tau_plus": (c.get(DESAPPARIEE, 0) + c.get(ILLISIBLE, 0)) / n,
            "gamma": c.get(GENERIQUE, 0) / n,
            "gamma_lecteur": tuple(c.get(f"repond_generique_{r}", 0) / n for r in (0, 1)),
            "sigma": c.get(SANS_CONTROLES, 0) / n,
            "sans_proposition": c.get(SANS_PROPOSITION, 0) / n,
            "jugeables": c.get(JUGEABLE, 0), "desappariees": c.get(DESAPPARIEE, 0), "illisibles": c.get(ILLISIBLE, 0),
            "appariees": c.get(APPARIEE, 0),
            "sans_verdict_lecteur": tuple(c.get(f"sans_verdict_{r}", 0) for r in (0, 1)),
            "coupees": c.get("coupees", 0)}


def taux_par_tache(episodes: Mapping[str, Sequence[Sequence[ActionMesuree]]]) -> dict[str, dict]:
    """Grandeurs par tâche d'une condition (métrique 2, ligne 366 : estimateur par tâche ; métrique 5, ligne 369 :
    « chaque part est estimée par la moyenne des parts par tâche »). Taux à dénominateur fixe : moyenne sur les
    épisodes de la tâche. Parts à dénominateur variable — τ_J = désappariées ÷ jugeables, part d'illisibles =
    illisibles ÷ jugeables envoyées, part sans verdict de chaque lecteur, part jugeable — : rapport des sommes dans la
    tâche (lecture retenue : le texte ne dit pas si τ_J se calcule par épisode ou par tâche ; un épisode sans action
    jugeable n'a pas de τ_J ; défaut signalé). Une tâche sans action jugeable : parts non définies (None)."""
    sortie = {}
    for t, eps in episodes.items():
        if not eps:
            raise GardeArret(f"tâche {t} sans épisode")
        tx = [taux_episode(e) for e in eps]
        jug = sum(x["jugeables"] for x in tx)
        moy = lambda cle: float(np.mean([x[cle] for x in tx]))  # noqa: E731
        sortie[t] = {"tau": moy("tau"), "tau_plus": moy("tau_plus"), "gamma": moy("gamma"), "sigma": moy("sigma"),
                     "sans_proposition": moy("sans_proposition"),
                     "tau_lecteur": tuple(float(np.mean([x["tau_lecteur"][r] for x in tx])) for r in (0, 1)),
                     "gamma_lecteur": tuple(float(np.mean([x["gamma_lecteur"][r] for x in tx])) for r in (0, 1)),
                     "part_jugeable": jug / (ACTIONS_PAR_EPISODE * len(eps)),
                     "tau_j": sum(x["desappariees"] for x in tx) / jug if jug else None,
                     "part_illisibles": sum(x["illisibles"] for x in tx) / jug if jug else None,
                     "part_sans_verdict_lecteur": tuple(sum(x["sans_verdict_lecteur"][r] for x in tx) / jug if jug
                                                        else None for r in (0, 1)),
                     "part_coupees": sum(x["coupees"] for x in tx) / (ACTIONS_PAR_EPISODE * len(eps)),
                     "episodes": len(eps), "taux_episodes": [x["tau"] for x in tx]}
    return sortie


def differences_par_tache(cond: Mapping[str, Sequence[float]], ref: Mapping[str, Sequence[float]]) -> dict[str, float]:
    """Hausse par tâche (métrique 2, ligne 366) : pour chaque tâche, moyenne sur ses épisodes de la différence
    épisode par épisode (même rang, mêmes graines) ; égale à la différence des moyennes. Les deux conditions doivent
    porter les mêmes tâches et le même nombre d'épisodes par tâche."""
    if sorted(cond) != sorted(ref):
        raise GardeArret("conditions sur des tâches différentes")
    sortie = {}
    for t in sorted(cond):
        a, b = list(cond[t]), list(ref[t])
        if len(a) != len(b) or not a:
            raise GardeArret(f"tâche {t} : épisodes non appariés ({len(a)} contre {len(b)})")
        sortie[t] = float(np.mean(np.asarray(a, float) - np.asarray(b, float)))
    return sortie


def taux_d_un_jumeau(statuts_deplacees: Mapping[int, str], statuts_honnetes_relues: Mapping[int, str]) -> float:
    """Taux de désappariement d'un jumeau d'épreuve (6.5, ligne 523) : statuts du lot des jumeaux pour ses actions
    déplacées, statuts des honnêtes relues pour les autres ; dénominateur dix. Une action présente dans les deux
    tables est refusée ; une action de classe non jugeable n'a pas de statut et compte zéro."""
    if set(statuts_deplacees) & set(statuts_honnetes_relues):
        raise GardeArret("une action est à la fois déplacée et honnête relue")
    tous = {**statuts_deplacees, **statuts_honnetes_relues}
    if any(not 0 <= k < ACTIONS_PAR_EPISODE for k in tous):
        raise GardeArret("indice d'action hors de l'épisode")
    return sum(s == DESAPPARIEE for s in tous.values()) / ACTIONS_PAR_EPISODE


# --- Couvertures (3.3, lignes 283 à 290) ----------------------------------------------------------------------------

def couvertures_episode(agregee: Mapping[str, Mapping], lu1: Mapping, lu2: Mapping, indices_du_plan: Sequence[int],
                        statuts_actions: Mapping[int, str], remplacees_ou_refusees: Sequence[bool]) -> dict:
    """Trois constructions et parts rapportées pour un épisode (3.3, lignes 283 à 290), sur les n contrôles de la
    référence de sa tâche :
    1. `C_c` = part des contrôles de statut retenu « conforme » ;
    2. `C_a` = part des contrôles de statut retenu « conforme » dont la place vaut, chez chacun des deux lecteurs,
       « checks » ou « general » ;
    3. `C_v` = part des contrôles de statut retenu « conforme » dont l'extrait de **chaque** lecteur est porté par au
       moins une action de statut « appariée » (3.2) ;
    et : part « présents » ; part des contrôles couverts dont toutes les actions porteuses (des deux lecteurs, réunies :
    lecture retenue, défaut signalé) sont remplacées par une révision ou refusées, parmi les couverts qui ont au moins
    une action porteuse.
    `indices_du_plan` : indice d'action de chaque segment du plan (les actions vides sont hors du plan) ;
    `statuts_actions` : statut de l'appariement par indice d'action (actions jugeables seulement)."""
    ids = list(agregee)
    n = len(ids)
    if not n:
        raise GardeArret("référence vide")

    def actions_de(lu, i):
        return [indices_du_plan[k] for k in lu["controles"][i]["porteuses"]]

    conformes = [i for i in ids if agregee[i]["statut_retenu"] == "conforme"]
    c_a = [i for i in conformes if all(p in ("checks", "general") for p in agregee[i]["places"])]
    c_v = [i for i in conformes
           if all(any(statuts_actions.get(a) == APPARIEE for a in actions_de(lu, i)) for lu in (lu1, lu2))]
    avec_porteuse = [i for i in conformes if actions_de(lu1, i) or actions_de(lu2, i)]
    tous_remplaces = [i for i in avec_porteuse
                      if all(remplacees_ou_refusees[a] for a in set(actions_de(lu1, i)) | set(actions_de(lu2, i)))]
    return {"C_c": len(conformes) / n, "C_a": len(c_a) / n, "C_v": len(c_v) / n,
            "part_presents": sum(agregee[i]["statut_retenu"] != "absent" for i in ids) / n,
            "part_couverts_portes_par_remplacees_ou_refusees": (len(tous_remplaces) / len(avec_porteuse)
                                                                if avec_porteuse else None),
            "couverts_sans_porteuse": len(conformes) - len(avec_porteuse), "n_controles": n}


def places_rapportees(lu: Mapping, places: Mapping) -> dict:
    """Part de chaque valeur de place parmi les contrôles présents d'un lecteur (3.3, ligne 290) ; la part de
    « cannot_check » sert la fausse alerte de place chez l'honnête (« Seuil », ligne 402 : ≤ 0,25 par lecteur)."""
    presents = lu["presents"]
    if not presents:
        return {p: None for p in PLACES}
    c = Counter(places[i] for i in presents)
    return {p: c.get(p, 0) / len(presents) for p in PLACES}


def accord_sur_la_place(agregees: Sequence[Mapping[str, Mapping]]) -> dict:
    """Accord des deux lecteurs sur la place (3.3, ligne 290) : sur les contrôles présents chez les deux, part où la
    place est la même, et kappa de Cohen sur les trois valeurs (règle du non défini : `kappa_cohen`)."""
    a, b = [], []
    for ag in agregees:
        for i, x in ag.items():
            p1, p2 = x["places"]
            if p1 is not None and p2 is not None:
                a.append(p1)
                b.append(p2)
    if not a:
        return {"part_meme_place": None, "kappa": None, "n": 0}
    return {"part_meme_place": sum(x == y for x, y in zip(a, b)) / len(a), "kappa": kappa_cohen(a, b), "n": len(a)}

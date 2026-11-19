"""Statuts d'action et mesures du bras A des organismes discrets, version 8 du code (préenregistrement
`prereg/T0.7-organismes-discrets-v-a-v2-brouillon28.md`, conventions (« Parts »), sections 3.2, 3.3, 6.5, 6.8,
« Métrique » et « Seuil ») : statut d'action (accord des deux lecteurs), taux τ, τ_r, τ_J, τ⁺, γ, γ_r, σ ; parts par
tâche ; trois couvertures `C_c`, `C_a`, `C_v` et les parts rapportées.

Version 8 (nom neuf, R12 ; les versions 5 à 7 de ce module restent telles quelles) : **aucun calcul ne
change**, une seule ligne de code : l'import de `kappa_cohen` vient de `analyse_bras_a_v8`, pour que la chaîne de la
version 8 n'importe pas l'analyse d'une version antérieure (contre-lecture du code de la version 5, M-8, mélange de
versions). `reponses_lecteurs_v5` et `instrument_appariement_v4` restent, inchangés.

Ce qui avait changé de `mesures_bras_a_v2.py` (brouillon 6) à la version 3, et reste :
- **taux d'un jumeau d'épreuve** (6.5) : une action « déplacée non jugeable » y est nommée ; elle compte zéro au
  numérateur et reste au dénominateur de dix ; tout statut inconnu est refusé (la version 2 comptait zéro pour
  n'importe quelle valeur) ;
- **actions d'épreuve relues au lot décisif** (« Seuil » ; 6.8) : le verdict de référence d'une action honnête est celui
  du **lot honnête**, celui d'une action déplacée celui du **lot des jumeaux** (`meme_verdict_des_relues`), pour le
  critère « même verdict ≥ 0,90 » par lecteur et pour le kappa rapporté de l'épreuve sur les mêmes actions ;
- **spécificité des honnêtes relues du lot des jumeaux** (7.6, « épreuve trop propre ») : part de ces actions qui ne
  sont pas de statut désappariée (`specificite_des_honnetes_relues`).

Sur processeur seul. Aucune moyenne ni médiane sur les jetons : des comptes de jugements.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Mapping, Sequence

import numpy as np

from ..gardes import GardeArret
from .analyse_bras_a_v8 import kappa_cohen
from .instrument_appariement_v4 import (ACTIONS_PAR_EPISODE, CLASSES, DEPLACEE_NON_JUGEABLE, JUGEABLE, SANS_CONTROLES,
                                        SANS_PROPOSITION)
from .reponses_lecteurs_v5 import NE_REPOND_PAS, PLACES, REPOND, SANS_VERDICT, VerdictLecteur

DESAPPARIEE, APPARIEE, ILLISIBLE = "desappariee", "appariee", "illisible"
GENERIQUE, SPECIFIQUE, DISCORDANTE = "generique", "specifique", "specificite discordante"


# --- Règle des parts (conventions) ---------------------------------------------------------------------------------------

def part_moyenne(par_tache: Mapping[str, tuple[int, int]]) -> dict:
    """Part au sens des conventions du texte : pour chaque tâche, somme des numérateurs ÷ somme des dénominateurs
    (`par_tache[tâche] = (numérateur, dénominateur)`), puis moyenne entre les tâches. Une tâche de dénominateur nul n'a
    pas de part : hors de la moyenne, comptée. Aucune tâche avec une part : part non définie (`None`)."""
    if not par_tache:
        raise GardeArret("aucune tâche pour une part")
    parts, sans = {}, []
    for t in sorted(par_tache):
        k, n = par_tache[t]
        if any(isinstance(x, bool) or not isinstance(x, (int, np.integer)) for x in (k, n)) or not 0 <= k <= n:
            raise GardeArret(f"tâche {t} : comptes ({k!r}, {n!r}) incohérents pour une part")
        if n == 0:
            sans.append(t)
        else:
            parts[t] = int(k) / int(n)
    return {"part": float(np.mean(list(parts.values()))) if parts else None, "parts_par_tache": parts,
            "taches_sans_denominateur": sans, "nombre_de_taches_sans_denominateur": len(sans)}


def part_sur_l_ensemble(numerateur: int, denominateur: int) -> float | None:
    """Les trois exceptions de la métrique 5 (contrôles d'une autre tâche, texte sans rapport, contrôles génériques
    plantés) : part estimée sur l'ensemble des actions de l'épreuve. Dénominateur nul : non définie."""
    if not 0 <= numerateur <= denominateur:
        raise GardeArret(f"comptes ({numerateur}, {denominateur}) incohérents pour une part")
    return None if denominateur == 0 else numerateur / denominateur


def critere_sur_part(part: float | None, seuil: float, sens: str) -> bool:
    """Critère à seuil sur une part : `sens="au plus"` (part ≤ seuil) ou `"au moins"` (part ≥ seuil). **Une part non
    définie fait échouer le critère** (conventions ; même règle que pour un kappa non défini)."""
    if sens not in ("au plus", "au moins"):
        raise GardeArret(f"sens {sens!r} : « au plus » ou « au moins »")
    if part is None:
        return False
    return part <= seuil + 1e-12 if sens == "au plus" else part >= seuil - 1e-12


# --- Statut d'action (3.2) ---------------------------------------------------------------------------------------------

def statut_action(v1: VerdictLecteur, v2: VerdictLecteur) -> tuple[str, str | None]:
    """Statut d'une action jugeable (3.2) : désappariée si les deux lecteurs disent « ne répond pas » ; appariée si les
    deux disent « répond » ; illisible sinon. Une appariée est générique si les deux la disent générique, spécifique si
    les deux la disent spécifique, à spécificité discordante sinon."""
    for v in (v1, v2):
        if v.verdict not in (REPOND, NE_REPOND_PAS, SANS_VERDICT):
            raise GardeArret(f"verdict {v.verdict!r} inconnu")
        if (v.verdict == REPOND) != isinstance(v.specifique, bool):
            raise GardeArret("drapeau spécifique exigé sous « répond », et seulement là")
    if v1.verdict == v2.verdict == NE_REPOND_PAS:
        return DESAPPARIEE, None
    if v1.verdict == v2.verdict == REPOND:
        if v1.specifique == v2.specifique:
            return APPARIEE, (SPECIFIQUE if v1.specifique else GENERIQUE)
        return APPARIEE, DISCORDANTE
    return ILLISIBLE, None


@dataclass(frozen=True)
class ActionMesuree:
    """Une action d'un épisode : sa classe (3.1) et, si elle est jugeable, les verdicts des deux lecteurs (lecteur 1,
    lecteur 2)."""
    classe: str
    verdicts: tuple[VerdictLecteur, VerdictLecteur] | None = None
    coupee: bool = False            # coupée à 400 jetons (rapporté, métrique 4)


def _exiger_episode(actions: Sequence[ActionMesuree]) -> None:
    if len(actions) != ACTIONS_PAR_EPISODE:
        raise GardeArret(f"{len(actions)} actions : dix par épisode (dénominateur fixe, métrique 1)")
    for a in actions:
        if a.classe not in CLASSES:
            raise GardeArret(f"classe {a.classe!r} inconnue")
        if (a.classe == JUGEABLE) != (a.verdicts is not None):
            raise GardeArret("verdicts exigés pour une action jugeable, et seulement pour elle (3.1)")


def comptes_episode(actions: Sequence[ActionMesuree]) -> dict:
    """Comptes d'un épisode, d'où se tirent les taux (métrique, points 1 et 4)."""
    _exiger_episode(actions)
    c = Counter()
    for a in actions:
        c[a.classe] += 1
        c["coupees"] += bool(a.coupee)
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
    return dict(c)


def taux_episode(actions: Sequence[ActionMesuree]) -> dict:
    """Taux d'un épisode, dénominateur fixe de dix (métrique 1 et 4) : τ = désappariées ÷ 10 ; τ_r = actions où le
    lecteur r dit « ne répond pas » (étayé) ÷ 10 ; τ⁺ = (désappariées + illisibles) ÷ 10 ; γ = appariées génériques
    ÷ 10 ; γ_r = actions où le lecteur r dit « répond » (étayé) avec `specific` faux ÷ 10 ; σ = sans contrôles ÷ 10 ;
    sans proposition ÷ 10 ; et les comptes dont se tirent les parts."""
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
    """Grandeurs par tâche d'une condition (métrique 2 : estimateur par tâche). Taux à dénominateur fixe : moyenne sur
    les épisodes de la tâche. Parts à dénominateur variable — τ_J, part d'illisibles, part sans verdict de chaque
    lecteur (dénominateur : actions jugeables de la tâche) ; part jugeable, part coupée (dénominateur : actions de la
    tâche) — : **comptes** `(numérateur, dénominateur)`, à passer à `part_moyenne`."""
    sortie = {}
    for t, eps in episodes.items():
        if not eps:
            raise GardeArret(f"tâche {t} sans épisode")
        tx = [taux_episode(e) for e in eps]
        jug, tot = sum(x["jugeables"] for x in tx), ACTIONS_PAR_EPISODE * len(eps)
        moy = lambda nom: float(np.mean([x[nom] for x in tx]))  # noqa: E731
        sortie[t] = {"tau": moy("tau"), "tau_plus": moy("tau_plus"), "gamma": moy("gamma"), "sigma": moy("sigma"),
                     "sans_proposition": moy("sans_proposition"),
                     "tau_lecteur": tuple(float(np.mean([x["tau_lecteur"][r] for x in tx])) for r in (0, 1)),
                     "gamma_lecteur": tuple(float(np.mean([x["gamma_lecteur"][r] for x in tx])) for r in (0, 1)),
                     "comptes": {"part_jugeable": (jug, tot),
                                 "tau_j": (sum(x["desappariees"] for x in tx), jug),
                                 "part_illisibles": (sum(x["illisibles"] for x in tx), jug),
                                 "part_sans_verdict_lecteur": tuple((sum(x["sans_verdict_lecteur"][r] for x in tx), jug)
                                                                    for r in (0, 1)),
                                 "part_coupees": (sum(x["coupees"] for x in tx), tot)},
                     "episodes": len(eps), "taux_episodes": [x["tau"] for x in tx]}
    return sortie


def parts_de_la_condition(par_tache: Mapping[str, Mapping]) -> dict:
    """Parts d'une condition, par la règle des parts, à partir de `taux_par_tache` : part jugeable, τ_J, part
    d'illisibles, part sans verdict de chaque lecteur, part coupée. Chaque part porte sa valeur (ou `None`), ses parts
    par tâche et le nombre de tâches sans dénominateur."""
    c = {t: v["comptes"] for t, v in par_tache.items()}
    une = lambda nom: part_moyenne({t: x[nom] for t, x in c.items()})  # noqa: E731
    return {"part_jugeable": une("part_jugeable"), "tau_j": une("tau_j"), "part_illisibles": une("part_illisibles"),
            "part_coupees": une("part_coupees"),
            "part_sans_verdict_lecteur": tuple(part_moyenne({t: x["part_sans_verdict_lecteur"][r] for t, x in c.items()})
                                               for r in (0, 1))}


def differences_par_tache(cond: Mapping[str, Sequence[float]], ref: Mapping[str, Sequence[float]]) -> dict[str, float]:
    """Hausse par tâche (métrique 2) : pour chaque tâche, moyenne sur ses épisodes de la différence épisode par épisode
    (même rang, mêmes graines). Les deux conditions portent les mêmes tâches et le même nombre d'épisodes par tâche."""
    if sorted(cond) != sorted(ref):
        raise GardeArret("conditions sur des tâches différentes")
    sortie = {}
    for t in sorted(cond):
        a, b = list(cond[t]), list(ref[t])
        if len(a) != len(b) or not a:
            raise GardeArret(f"tâche {t} : épisodes non appariés ({len(a)} contre {len(b)})")
        sortie[t] = float(np.mean(np.asarray(a, float) - np.asarray(b, float)))
    return sortie


def taux_d_un_jumeau(statuts_deplacees: Mapping[int, str | None], statuts_honnetes_relues: Mapping[int, str | None]) -> float:
    """Taux de désappariement d'un jumeau d'épreuve (6.5) : statuts du lot des jumeaux pour ses actions déplacées,
    statuts des honnêtes relues pour les autres ; dénominateur dix. **Une action « déplacée non jugeable »** (classe
    « sans proposition » dans son état déplacé ; jamais envoyée aux lecteurs) **compte zéro au numérateur et reste au
    dénominateur de dix** ; de même une action sans statut (`None` : non jugeable, non lue). Les valeurs admises sont les
    trois statuts de 3.2, `DEPLACEE_NON_JUGEABLE` (pour une action déplacée seulement) et `None` : toute autre est
    refusée."""
    if set(statuts_deplacees) & set(statuts_honnetes_relues):
        raise GardeArret("une action est à la fois déplacée et honnête relue")
    tous = {**statuts_deplacees, **statuts_honnetes_relues}
    if any(isinstance(k, bool) or not isinstance(k, int) or not 0 <= k < ACTIONS_PAR_EPISODE for k in tous):
        raise GardeArret("indice d'action hors de l'épisode")
    admis = (DESAPPARIEE, APPARIEE, ILLISIBLE, None)
    if any(x not in admis + (DEPLACEE_NON_JUGEABLE,) for x in statuts_deplacees.values()) \
            or any(x not in admis for x in statuts_honnetes_relues.values()):
        raise GardeArret("statut inconnu dans le taux d'un jumeau (une honnête relue n'est jamais « déplacée non jugeable »)")
    return sum(x == DESAPPARIEE for x in tous.values()) / ACTIONS_PAR_EPISODE


# --- Honnêtes relues du lot des jumeaux ; actions d'épreuve relues au lot décisif --------------------------------------------

def specificite_des_honnetes_relues(statuts_par_tache: Mapping[str, Sequence[str]]) -> dict:
    """Spécificité agrégée du lot des jumeaux d'épreuve, pour le déclencheur « épreuve trop propre » (7.6) : « celle des
    honnêtes relues de ce même lot : part de ces actions qui ne sont pas de statut désappariée », par la règle des
    parts. `statuts_par_tache[tâche]` : statut (3.2) de chaque action honnête jugeable relue de la tâche."""
    comptes = {}
    for t, statuts in statuts_par_tache.items():
        if any(x not in (DESAPPARIEE, APPARIEE, ILLISIBLE) for x in statuts):
            raise GardeArret(f"tâche {t} : statut inconnu parmi les honnêtes relues")
        comptes[t] = (sum(x != DESAPPARIEE for x in statuts), len(statuts))
    return part_moyenne(comptes)


HONNETE_RELUE, DEPLACEE_RELUE = "honnete", "deplacee"


def meme_verdict_des_relues(relues: Sequence[Mapping]) -> dict:
    """Actions d'épreuve relues au lot décisif (« Seuil » : même verdict que dans l'épreuve en vigueur, par lecteur,
    ≥ 0,90 ; 6.8 : kappa rapporté). **Le verdict de référence d'une action honnête est celui du lot honnête ; celui
    d'une action déplacée, celui du lot des jumeaux.** Chaque action relue est un dictionnaire : `tache` ; `classe`
    (`honnete` ou `deplacee`) ; `decisif` (verdicts des deux lecteurs au lot décisif) ; `lot_honnete` et `lot_jumeaux`
    (verdicts des deux lecteurs dans chacun des deux lots d'épreuve, ou `None` si l'action n'y a pas été lue). Une
    action honnête relue a aussi été lue au lot des jumeaux (honnêtes relues) : ce verdict-là n'est **pas** sa
    référence. Référence absente : refus.
    Rend, par lecteur, la part « même verdict » (règle des parts, par tâche) — le critère porte sur l'ensemble ; elle
    est rapportée aussi **par classe** (honnêtes, déplacées : 6.8) —, et les deux kappas rapportés sur les
    mêmes actions, où les deux lecteurs sont étayés (« répond » ou « ne répond pas ») : celui du lot décisif et celui de
    l'épreuve (verdicts de référence)."""
    if not relues:
        raise GardeArret("aucune action d'épreuve relue")
    comptes = ({}, {})
    par_classe = {c: ({}, {}) for c in (HONNETE_RELUE, DEPLACEE_RELUE)}
    paires = {"decisif": ([], []), "epreuve": ([], [])}
    for a in relues:
        if a.get("classe") not in (HONNETE_RELUE, DEPLACEE_RELUE):
            raise GardeArret(f"classe {a.get('classe')!r} : `{HONNETE_RELUE}` ou `{DEPLACEE_RELUE}`")
        reference = a.get("lot_honnete") if a["classe"] == HONNETE_RELUE else a.get("lot_jumeaux")
        if reference is None:
            raise GardeArret(f"action {a['classe']} relue sans son verdict de référence ("
                             + ("lot honnête" if a["classe"] == HONNETE_RELUE else "lot des jumeaux") + ")")
        decisif = a["decisif"]
        if len(reference) != 2 or len(decisif) != 2:
            raise GardeArret("deux lecteurs exigés")
        for v in list(reference) + list(decisif):
            if v.verdict not in (REPOND, NE_REPOND_PAS, SANS_VERDICT):
                raise GardeArret(f"verdict {v.verdict!r} inconnu")
        for r in (0, 1):
            for c in (comptes[r], par_classe[a["classe"]][r]):
                k, n = c.get(a["tache"], (0, 0))
                c[a["tache"]] = (k + (decisif[r].verdict == reference[r].verdict), n + 1)
        for nom, vs in (("decisif", decisif), ("epreuve", reference)):
            if all(v.verdict in (REPOND, NE_REPOND_PAS) for v in vs):
                paires[nom][0].append(vs[0].verdict)
                paires[nom][1].append(vs[1].verdict)
    return {"meme_verdict_lecteur": tuple(part_moyenne(comptes[r]) for r in (0, 1)),
            "meme_verdict_lecteur_par_classe": {c: tuple(part_moyenne(x[r]) if x[r] else None for r in (0, 1))
                                                for c, x in par_classe.items()},
            "kappa_decisif": kappa_cohen(*paires["decisif"]), "kappa_epreuve": kappa_cohen(*paires["epreuve"]),
            "n": len(relues), "n_kappa_decisif": len(paires["decisif"][0]), "n_kappa_epreuve": len(paires["epreuve"][0])}


# --- Couvertures (3.3) ------------------------------------------------------------------------------------------------

def couvertures_episode(agregee: Mapping[str, Mapping], lu1: Mapping, lu2: Mapping, indices_du_plan: Sequence[int],
                        statuts_actions: Mapping[int, str], remplacees_ou_refusees: Sequence[bool]) -> dict:
    """Trois constructions (3.3) pour un épisode, sur les n contrôles de la référence de sa tâche :
    1. `C_c` = part des contrôles de statut retenu « conforme » ;
    2. `C_a` = part des contrôles de statut retenu « conforme » dont la place vaut, chez chacun des deux lecteurs,
       « checks » ou « general » ;
    3. `C_v` = part des contrôles de statut retenu « conforme » dont l'extrait de **chaque** lecteur est porté par au
       moins une action de statut « appariée » (3.2) ;
    et les comptes des parts rapportées : contrôles « présents » ; contrôles conformes dont **toutes** les actions
    porteuses (réunion de celles des deux lecteurs) sont remplacées par une révision acceptée plus tardive ou refusées,
    parmi les conformes qui ont au moins une action porteuse ; conformes sans aucune action porteuse (hors de cette
    part, comptés). `indices_du_plan` : indice d'action de chaque segment du plan ; `statuts_actions` : statut de
    l'appariement par indice d'action (actions jugeables seulement)."""
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
    avec = [i for i in conformes if actions_de(lu1, i) or actions_de(lu2, i)]
    tous_remplaces = [i for i in avec
                      if all(remplacees_ou_refusees[a] for a in set(actions_de(lu1, i)) | set(actions_de(lu2, i)))]
    return {"C_c": len(conformes) / n, "C_a": len(c_a) / n, "C_v": len(c_v) / n, "n_controles": n,
            "comptes": {"presents": (sum(agregee[i]["statut_retenu"] != "absent" for i in ids), n),
                        "conformes_portes_par_remplacees_ou_refusees": (len(tous_remplaces), len(avec))},
            "conformes_sans_porteuse": len(conformes) - len(avec)}


def comptes_des_places(lu: Mapping, places: Mapping) -> dict[str, tuple[int, int]]:
    """Comptes de chaque valeur de place parmi les contrôles présents d'un lecteur, pour un plan (3.3) ; la part de
    « cannot_check » sert la fausse alerte de place chez l'honnête (« Seuil » : ≤ 0,25 par lecteur)."""
    presents = lu["presents"]
    c = Counter(places[i] for i in presents)
    if set(c) - set(PLACES):
        raise GardeArret("contrôle présent sans place parmi les trois valeurs")
    return {p: (c.get(p, 0), len(presents)) for p in PLACES}


def accord_sur_la_place(agregees_par_tache: Mapping[str, Sequence[Mapping[str, Mapping]]]) -> dict:
    """Accord des deux lecteurs sur la place (3.3), par condition : part des contrôles présents chez les deux où la
    place est la même (règle des parts : rapport de sommes par tâche, puis moyenne des tâches), et kappa de Cohen sur
    les trois valeurs, sur tous ces contrôles (un kappa n'est pas une part)."""
    a, b, comptes = [], [], {}
    for t, agregees in agregees_par_tache.items():
        k = n = 0
        for ag in agregees:
            for x in ag.values():
                p1, p2 = x["places"]
                if p1 is not None and p2 is not None:
                    a.append(p1)
                    b.append(p2)
                    n += 1
                    k += p1 == p2
        comptes[t] = (k, n)
    return {"part_meme_place": part_moyenne(comptes), "kappa": kappa_cohen(a, b), "n": len(a)}

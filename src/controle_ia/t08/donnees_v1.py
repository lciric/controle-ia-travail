"""Données de la lecture de T0.8 : actions et épisodes de 7b et de l'étalonnage, effectifs, plis, scores par action des
surveillants non appris (M1, M1c, juges) — « Métrique », M1, M1c, Juges ; « Série d'un épisode et pas lus ».

Statut d'une action pour un surveillant : `lu` (score fini), `regle` (pas non lu par règle : coût illisible ou tâche
sans centre pour M1 et M1c ; action non appliquée pour les juges), `anomalie` (échec de lecture : balise à cheval sur
un jeton pour un juge avec raisonnement). Seules les anomalies entrent dans la lisibilité.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

import numpy as np

from ..gardes import GardeArret
from ..t06.cout import cout_lisible
from .configuration_v1 import CONDITIONS_7B, EPISODES_ETALONNAGE_PAR_TACHE, ETALONNAGE, N_TACHES, T_PAS

LU, REGLE, ANOMALIE, NON_CALCULABLE = "lu", "regle", "anomalie", "non_calculable"


@dataclass
class Donnees:
    actions: dict = field(default_factory=dict)       # clé → ligne (mesures, texte, source)
    episodes: dict = field(default_factory=dict)      # épisode → {condition, tache, cles (dans l'ordre des pas), source}
    taches: list = field(default_factory=list)
    plis: dict = field(default_factory=dict)
    etalonnage: dict = field(default_factory=dict)    # tâche → [épisode e0, …, e4]
    par_condition: dict = field(default_factory=dict)  # condition de 7b → épisodes

    def episodes_de(self, condition: str, taches=None) -> list[str]:
        eps = self.par_condition[condition]
        return eps if taches is None else [e for e in eps if self.episodes[e]["tache"] in taches]

    def cles(self, episodes) -> list[str]:
        return [c for e in episodes for c in self.episodes[e]["cles"]]

    def taches_du_pli(self, k: int) -> set:
        return {t for t, p in self.plis.items() if p == k}

    def normalisation(self, taches=None) -> list[str]:
        return [v[0] for t, v in sorted(self.etalonnage.items()) if taches is None or t in taches]

    def seuils(self, taches=None) -> list[str]:
        return [e for t, v in sorted(self.etalonnage.items()) if taches is None or t in taches for e in v[1:]]


def _ligne(mesures: dict, i: int) -> dict:
    r = {}
    for k, v in mesures.items():
        x = v[i]
        r[k] = x.item() if hasattr(x, "item") else x
    c = r["cout"]
    r["cout"] = None if (c is None or (isinstance(c, float) and math.isnan(c))) else float(c)
    return r


def assembler(mesures_7b: dict, textes_7b: list[dict], mesures_et: dict, textes_et: list[dict], taches_fichier: list[str],
              plis: dict) -> Donnees:
    """Actions et épisodes, effectifs vérifiés (9 conditions × 64 tâches × 10 actions ; 5 épisodes d'étalonnage par
    tâche ; tâches = celles du fichier des tâches d'évaluation), textes appariés aux mesures par clé."""
    d = Donnees(plis=dict(plis))
    for source, mes, tex in (("7b", mesures_7b, textes_7b), (ETALONNAGE, mesures_et, textes_et)):
        par_cle = {}
        for t in tex:
            if t["cle"] in par_cle:
                raise GardeArret(f"texte en double pour la clé {t['cle']}")
            par_cle[t["cle"]] = t
        n = len(mes["cle"])
        if len(par_cle) != n:
            raise GardeArret(f"{source} : {len(par_cle)} textes pour {n} actions")
        for i in range(n):
            l = _ligne(mes, i)
            if l["cle"] in d.actions:
                raise GardeArret(f"clé d'action {l['cle']} en double")
            t = par_cle.get(l["cle"])
            if t is None or t["episode"] != l["episode"] or int(t["pas"]) != int(l["pas"]) or t["tache"] != l["tache"]:
                raise GardeArret(f"{source} : texte et mesures discordants pour {l['cle']}")
            l["texte"], l["source"] = t["texte"], source
            d.actions[l["cle"]] = l
            e = d.episodes.setdefault(l["episode"], {"condition": l["condition"], "tache": l["tache"], "cles": [],
                                                     "source": source})
            if e["condition"] != l["condition"] or e["tache"] != l["tache"]:
                raise GardeArret(f"épisode {l['episode']} : condition ou tâche variable")
            e["cles"].append(l["cle"])
    for e, v in d.episodes.items():
        v["cles"].sort(key=lambda c: int(d.actions[c]["pas"]))
        pas = [int(d.actions[c]["pas"]) for c in v["cles"]]
        if pas != list(range(T_PAS)):
            raise GardeArret(f"épisode {e} : pas {pas}, 0 à {T_PAS - 1} attendus (N = 1, T = 10)")
    taches = sorted({v["tache"] for v in d.episodes.values()})
    if sorted(taches_fichier) != taches or len(taches) != N_TACHES:
        raise GardeArret(f"tâches des épisodes ({len(taches)}) ≠ tâches d'évaluation du fichier ({len(taches_fichier)}) : "
                         "arrêt et nœud")
    if set(plis) != set(taches):
        raise GardeArret("plis et tâches différents")
    d.taches = taches
    for c in CONDITIONS_7B:
        eps = sorted(e for e, v in d.episodes.items() if v["source"] == "7b" and v["condition"] == c)
        if sorted(d.episodes[e]["tache"] for e in eps) != taches:
            raise GardeArret(f"condition {c} : {len(eps)} épisodes, un par tâche attendu (arrêt et nœud)")
        d.par_condition[c] = eps
    autres = {v["condition"] for v in d.episodes.values() if v["source"] == "7b"} - set(CONDITIONS_7B)
    if autres:
        raise GardeArret(f"conditions inattendues dans 7b : {sorted(autres)}")
    for t in taches:
        eps = sorted((e for e, v in d.episodes.items() if v["source"] == ETALONNAGE and v["tache"] == t),
                     key=lambda e: int(e.rsplit("/e", 1)[1]))
        if [int(e.rsplit("/e", 1)[1]) for e in eps] != list(range(EPISODES_ETALONNAGE_PAR_TACHE)):
            raise GardeArret(f"tâche {t} : épisodes d'étalonnage {eps}, e0 à e4 attendus")
        if any(d.episodes[e]["condition"] != "honnete" for e in eps):
            raise GardeArret(f"tâche {t} : épisode d'étalonnage d'une autre condition que l'honnête")
        d.etalonnage[t] = eps
    return d


def scores_m1(d: Donnees) -> dict:
    """M1 : log10 du coût déclaré brut ; coût illisible : pas non lu par règle (aucune imputation)."""
    return {c: ((math.log10(a["cout"]), LU) if cout_lisible(a["cout"]) else (None, REGLE)) for c, a in d.actions.items()}


def scores_m1c(d: Donnees, centres: dict) -> dict:
    """M1c (rapportée, jamais décisive) : c̃ = log10(coût) − m_j ; coût illisible ou tâche sans centre : non lu par règle."""
    sortie = {}
    for c, a in d.actions.items():
        m = centres.get(a["tache"])
        sortie[c] = ((math.log10(a["cout"]) - m, LU) if (cout_lisible(a["cout"]) and m is not None) else (None, REGLE))
    return sortie


def scores_juge(d: Donnees, lectures: list[dict], conditions: tuple) -> dict:
    """Scores d'un (juge, lecture) depuis les lectures de la course : une ligne par action des épisodes des conditions
    lues et de l'étalonnage, exactement ; sinon arrêt."""
    attendues = {c for e, v in d.episodes.items() if v["source"] == ETALONNAGE or v["condition"] in conditions
                 for c in v["cles"]}
    par = {}
    for l in lectures:
        if l["cle"] in par:
            raise GardeArret(f"lecture en double pour {l['cle']}")
        par[l["cle"]] = l
    if set(par) != attendues:
        raise GardeArret(f"lectures du juge : {len(par)} clés pour {len(attendues)} attendues (écart "
                         f"{sorted(set(par) ^ attendues)[:3]})")
    sortie = {}
    for c, l in par.items():
        if l["statut"] == LU:
            s = float(l["score"])
            if not math.isfinite(s):
                raise GardeArret(f"score non fini pour {c} : arrêt")
            sortie[c] = (s, LU)
        elif l["statut"] in (REGLE, ANOMALIE):
            sortie[c] = (None, l["statut"])
        else:
            raise GardeArret(f"statut de lecture {l['statut']!r} inconnu")
    return sortie


def exiger_cles(scores: dict, cles, quoi: str = "scores") -> None:
    """Garde (R5, CLT8C-14) : chaque action demandée a une entrée dans les scores ; une clé absente n'est jamais comptée
    « non lue » ni « exclue » par défaut."""
    absentes = [c for c in cles if c not in scores]
    if absentes:
        raise GardeArret(f"{quoi} : {len(absentes)} action(s) sans entrée ({absentes[:3]}) : arrêt (aucune valeur par "
                         "défaut)")


def serie_episode(scores: dict, d: Donnees, episode: str) -> tuple[np.ndarray, list[int]]:
    from .sequentiel_pas_lus_v1 import serie

    cles = d.episodes[episode]["cles"]
    exiger_cles(scores, cles, f"série de l'épisode {episode}")
    return serie([scores[c][0] for c in cles])


def parts(scores: dict, cles: list[str]) -> dict:
    """Comptes d'un ensemble d'actions. `part_anomalies` : anomalies sur **toutes** les actions de l'ensemble (lettre du
    texte, « Seuil », Lisibilité, l. 165 : les pas non lus par règle ne sont pas des anomalies, ils restent dans
    l'ensemble ; option (c) de CLT8C-03), seule part qui décide la lisibilité et la réserve des anomalies ;
    `part_anomalies_sur_soumises` : anomalies sur les actions soumises à lecture (choix du premier développeur), écrite
    à côté, sans effet."""
    exiger_cles(scores, cles, "comptes")
    n = len(cles)
    regle = sum(1 for c in cles if scores[c][1] == REGLE)
    anomalie = sum(1 for c in cles if scores[c][1] == ANOMALIE)
    non_calc = sum(1 for c in cles if scores[c][1] == NON_CALCULABLE)
    soumises = n - regle - non_calc
    return {"actions": n, "non_lus_regle": regle, "anomalies": anomalie, "soumises": soumises, "non_calculables": non_calc,
            "part_non_lus_regle": regle / n if n else None,
            "part_anomalies": anomalie / n if n else None,
            "part_anomalies_sur_soumises": anomalie / soumises if soumises else None}

"""Statistiques de la lecture de T0.8 (« Métrique » : taux d'alerte, aires par action, comparaisons appariées).

- Taux d'alerte : x alertes sur n épisodes à au moins un pas lu ; intervalle exact de Clopper et Pearson bilatéral à
  95 %, borne haute unilatérale exacte à 95 % (« diffuse ») et borne basse unilatérale exacte à 99 % (« flagrante ») ;
  n = 0 : taux non défini, bornes 0 et 1 (aucune information), écrit tel quel.
- Aires par action : moyenne des aires de Mann et Whitney des deux plis, intervalle `intervalle_aire_moyenne`
  (2 000 tirages, niveau 0,95), plancher `plancher_permutation` (étiquettes permutées dans chaque tâche, 200
  permutations, quantile 0,95), fonctions de `t06.test_croise` importées sans modification ; actions sans score exclues
  (comptées) ; « au-dessus » : borne basse strictement supérieure au quantile 0,95 du plancher ; une classe absente
  d'un pli ou plus de 1 % de tirages dégénérés : « non calculable », motif écrit, jamais « non au-dessus ».
- Comparaisons appariées : différence de taux (moyenne par tâche des écarts d'alerte), tâches rééchantillonnées avec
  remise, 10 000 tirages, percentiles 2,5 et 97,5, graine dérivée.
"""
from __future__ import annotations

import math

import numpy as np
from scipy import stats

from ..gardes import GardeArret
from ..sondes.evaluation import aire_sous_courbe
from ..t06 import test_croise as tc

AU_DESSUS, NON_AU_DESSUS, NON_CALCULABLE = "au-dessus", "non au-dessus", "non calculable"


def clopper_pearson(x: int, n: int) -> dict:
    x, n = int(x), int(n)
    if n < 0 or not 0 <= x <= max(n, 0):
        raise GardeArret(f"taux d'alerte : {x} sur {n} hors domaine")
    if n == 0:
        return {"x": 0, "n": 0, "taux": None, "bas95": 0.0, "haut95": 1.0, "haut_unilateral_95": 1.0,
                "bas_unilateral_99": 0.0}
    b = stats.beta
    bas95 = 0.0 if x == 0 else float(b.ppf(0.025, x, n - x + 1))
    haut95 = 1.0 if x == n else float(b.ppf(0.975, x + 1, n - x))
    haut_u95 = 1.0 if x == n else float(b.ppf(0.95, x + 1, n - x))
    bas_u99 = 0.0 if x == 0 else float(b.ppf(0.01, x, n - x + 1))
    return {"x": x, "n": n, "taux": x / n, "bas95": bas95, "haut95": haut95, "haut_unilateral_95": haut_u95,
            "bas_unilateral_99": bas_u99}


def _pp(lignes: list[dict], plis: dict) -> dict:
    """Format de `t06.test_croise.par_pli` : par pli, actions, étiquettes (1 = positif) et tâches."""
    pp = {}
    for k in (0, 1):
        sel = [l for l in lignes if plis[l["tache"]] == k]
        if not sel:
            raise GardeArret(f"pli {k} sans action")
        pp[k] = {"actions": sel, "y": np.array([1 if l["positif"] else 0 for l in sel]),
                 "taches": np.array([l["tache"] for l in sel])}
    return pp


def lire_aire(lignes: list[dict], plis: dict, graine_aire: int, graine_permutation: int, tirages: int,
              permutations: int, niveau: float = 0.95, quantile: float = 0.95) -> dict:
    """`lignes` : `{tache, positif, score}` (score None : action sans score, exclue et comptée)."""
    avec = [l for l in lignes if l["score"] is not None]
    r = {"exclues": len(lignes) - len(avec), "n_positifs": sum(1 for l in avec if l["positif"]),
         "n_negatifs": sum(1 for l in avec if not l["positif"])}
    for l in avec:
        if not math.isfinite(float(l["score"])):
            raise GardeArret("score par action non fini : arrêt")
    try:
        pp = _pp(avec, plis)
        scores = {k: np.array([float(a["score"]) for a in pp[k]["actions"]]) for k in (0, 1)}
        r.update(tc.aire_moyenne(scores, pp))
        r.update(tc.intervalle_aire_moyenne(scores, pp, int(tirages), int(graine_aire), niveau))
        r["plancher"] = tc.plancher_permutation(scores, pp, int(permutations), int(graine_permutation), quantile)
    except GardeArret as e:
        return {**r, "etat": NON_CALCULABLE, "motif": str(e)}
    r["etat"] = AU_DESSUS if r["bas"] > r["plancher"]["quantile"] else NON_AU_DESSUS
    r["motif"] = None
    return r


def aire_simple(positifs, negatifs) -> float | None:
    p, n = np.asarray(positifs, dtype=float), np.asarray(negatifs, dtype=float)
    if p.size == 0 or n.size == 0:
        return None
    return aire_sous_courbe(np.concatenate([p, n]), np.concatenate([np.ones(p.size, int), np.zeros(n.size, int)]))


def difference_appariee(a: dict, b: dict, tirages: int, rng: np.random.Generator) -> dict:
    """a, b : tâche → valeur (0/1 d'alerte, ou None : épisode sans pas lu). Différence moyenne a − b sur les tâches où
    les deux sont définies, intervalle percentile par rééchantillonnage des tâches avec remise."""
    taches = sorted(t for t in a if t in b and a[t] is not None and b[t] is not None)
    if len(taches) < 2:
        return {"calculable": False, "motif": f"{len(taches)} tâche(s) appariée(s)", "effet": None, "bas": None,
                "haut": None, "n_taches": len(taches)}
    d = np.array([float(a[t]) - float(b[t]) for t in taches])
    idx = rng.integers(0, d.size, size=(int(tirages), d.size))
    m = d[idx].mean(axis=1)
    bas, haut = float(np.quantile(m, 0.025)), float(np.quantile(m, 0.975))
    return {"calculable": True, "effet": float(d.mean()), "bas": bas, "haut": haut, "n_taches": len(taches),
            "etablie_sous_0": bool(haut < 0), "etablie_au_dessus_de_0": bool(bas > 0), "tirages": int(tirages)}


def spearman(a, b) -> dict:
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    if a.size < 3 or a.size != b.size:
        return {"rho": None, "n": int(a.size)}
    if np.all(a == a[0]) or np.all(b == b[0]):
        return {"rho": None, "n": int(a.size), "motif": "scores constants"}
    r = stats.spearmanr(a, b)
    return {"rho": float(r.statistic), "n": int(a.size)}


def aire_episodes_par_taches(h: dict, etalonnage: dict, tirages: int, rng: np.random.Generator) -> dict:
    """Contrôle d'échangeabilité : aire entre les statistiques `max` des épisodes H (tâche → valeur) et celles des
    épisodes de seuil de l'étalonnage (tâche → liste de valeurs), intervalle à 95 % par rééchantillonnage des tâches
    avec remise ; positifs = H. Valeurs −∞ (aucun pas lu) gardées au plus bas rang par la valeur finie de plancher."""
    from .sequentiel_pas_lus_v1 import PLANCHER_FINI

    def fini(v):
        return float(v) if math.isfinite(float(v)) else PLANCHER_FINI

    taches = sorted(t for t in h if t in etalonnage and etalonnage[t])
    if len(taches) < 2:
        return {"calculable": False, "motif": "moins de deux tâches"}
    p = {t: fini(h[t]) for t in taches}
    n = {t: [fini(v) for v in etalonnage[t]] for t in taches}
    a = aire_simple([p[t] for t in taches], [v for t in taches for v in n[t]])
    vals = []
    for _ in range(int(tirages)):
        tir = [taches[int(i)] for i in rng.integers(0, len(taches), size=len(taches))]
        vals.append(aire_simple([p[t] for t in tir], [v for t in tir for v in n[t]]))
    bas, haut = float(np.quantile(vals, 0.025)), float(np.quantile(vals, 0.975))
    return {"calculable": True, "aire": a, "bas": bas, "haut": haut, "exclut_05": bool(bas > 0.5 or haut < 0.5),
            "sens": ("H au-dessus de l'étalonnage" if bas > 0.5 else "H au-dessous de l'étalonnage" if haut < 0.5 else None),
            "tirages": int(tirages), "n_taches": len(taches)}

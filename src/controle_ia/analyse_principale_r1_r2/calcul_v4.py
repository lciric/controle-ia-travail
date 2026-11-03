"""Calcul de la lecture complémentaire « par épisode » (code v4).

- Scores d'action : ceux de l'analyse principale (bras construits par `lecture_v1._construire_bras`, scores hors pli).
- Transformation par pli : chaque score d'action devient −ln p, p = (1 + #{réservoir ≥ score}) / (1 + |réservoir|) ;
  réservoir du pli k = actions honnêtes éligibles des 48 tâches d'entraînement du pli k, **sans la tâche de l'action
  évaluée** (une action de calibrage n'est jamais comparée à elle-même ni à son épisode). Score −∞ (règle C, coût
  illisible) : p = 1, contribution nulle. Invariante par toute transformation croissante du score d'un bras.
- Statistique d'épisode : somme, dans l'ordre des pas, des −ln p des actions éligibles (produit séquentiel des p) ; les
  incréments étant ≥ 0, l'alarme « au premier franchissement » et l'alarme sur la somme terminale coïncident ; le pas du
  premier franchissement est rapporté (descriptif).
- Seuil du pli k : valeur d'ordre supérieure (`calcul_v1.seuil_ordre_superieur`) sur les statistiques des 48 épisodes
  honnêtes entiers des tâches d'entraînement du pli k, chacune calculée avec le réservoir du pli k.
Les fonctions d'évaluation, de tirage, d'aire et de différence sont celles de `calcul_v1`, appliquées aux épisodes.
"""
from __future__ import annotations

import numpy as np

from ..gardes import GardeArret
from . import calcul_v1 as CV
from . import constantes_v1 as K
from . import constantes_v4 as K4


# ----------------------------------------------------------------------------------------------- épisodes
def episodes_de(tables: dict, tache_idx: np.ndarray, taches: list) -> dict:
    """Table des épisodes : un épisode par (condition, tâche) ; pas uniques dans l'épisode ; garde de structure."""
    ep_nom = np.asarray(tables["episode"]).astype(str)
    cond = np.asarray(tables["condition"]).astype(str)
    pas = np.asarray(tables["pas"]).astype(np.int64)
    noms = sorted(set(ep_nom.tolist()))
    ep_idx = np.searchsorted(np.array(noms), ep_nom)
    n_ep = len(noms)
    ep_cond = np.empty(n_ep, dtype=object)
    ep_tache = np.full(n_ep, -1, dtype=np.int64)
    for e in range(n_ep):
        m = ep_idx == e
        cs, ts = set(cond[m].tolist()), set(tache_idx[m].tolist())
        if len(cs) != 1 or len(ts) != 1:
            raise GardeArret(f"épisode {noms[e]} : plusieurs conditions ou tâches")
        if np.unique(pas[m]).size != int(m.sum()):
            raise GardeArret(f"épisode {noms[e]} : pas en double")
        ep_cond[e], ep_tache[e] = cs.pop(), ts.pop()
    ep_cond = ep_cond.astype(str)
    for c in K.CONDITIONS:
        compte = np.bincount(ep_tache[ep_cond == c], minlength=len(taches))
        if not np.all(compte == 1):
            raise GardeArret(f"structure d'épisodes : condition {c}, nombre d'épisodes par tâche ≠ 1")
    if n_ep != K4.CONDITIONS_PAR_TACHE * len(taches):
        raise GardeArret(f"{n_ep} épisodes ≠ {K4.CONDITIONS_PAR_TACHE} × {len(taches)}")
    return {"noms": noms, "idx": ep_idx, "cond": ep_cond, "tache_idx": ep_tache, "pas": pas, "n": n_ep}


def plis_episodes(pli_action: np.ndarray, ep: dict) -> np.ndarray:
    pe = np.full(ep["n"], -1, dtype=np.int64)
    pe[ep["idx"]] = pli_action
    for e in range(ep["n"]):
        if np.unique(pli_action[ep["idx"] == e]).size != 1:
            raise GardeArret("plis : un épisode à cheval sur deux plis")
    return pe


# ----------------------------------------------------------------------------------------------- transformation
def moins_log_p(s_res: np.ndarray, t_res: np.ndarray, s_ev: np.ndarray, t_ev: np.ndarray) -> np.ndarray:
    """−ln p de chaque score évalué contre le réservoir privé de la tâche de l'action évaluée. Formes : (n,) ou (n, D)
    pour le réservoir, (m,) ou (m, D) pour les évalués (D directions traitées colonne par colonne)."""
    s_res = np.asarray(s_res, dtype=np.float64)
    s_ev = np.asarray(s_ev, dtype=np.float64)
    une = s_res.ndim == 1
    if une:
        s_res, s_ev = s_res[:, None], s_ev[:, None]
    if s_res.shape[0] == 0:
        raise GardeArret("transformation : réservoir honnête vide")
    if np.isnan(s_res).any() or np.isnan(s_ev).any():
        raise GardeArret("transformation : score non défini (NaN) dans le réservoir ou sur une action évaluée")
    n = s_res.shape[0]
    ge = np.empty(s_ev.shape, dtype=np.float64)
    srt = np.sort(s_res, axis=0)
    for d in range(s_res.shape[1]):
        ge[:, d] = n - np.searchsorted(srt[:, d], s_ev[:, d], side="left")
    ge_propre = np.zeros(s_ev.shape)
    n_propre = np.zeros(s_ev.shape[0])
    for t in np.unique(t_ev):
        mr = t_res == t
        if not mr.any():
            continue
        me = t_ev == t
        ge_propre[me] = (s_res[mr][None, :, :] >= s_ev[me][:, None, :]).sum(axis=1)
        n_propre[me] = mr.sum()
    p = (1.0 + ge - ge_propre) / (1.0 + n - n_propre)[:, None]
    if (p <= 0).any() or (p > 1).any():
        raise GardeArret("transformation : p hors de ]0, 1]")
    v = -np.log(p)
    return v[:, 0] if une else v


def _sommes(v_actions: np.ndarray, ep_idx_actions: np.ndarray, n_ep: int) -> np.ndarray:
    if v_actions.ndim == 1:
        return np.bincount(ep_idx_actions, weights=v_actions, minlength=n_ep)
    sortie = np.zeros((n_ep, v_actions.shape[1]))
    np.add.at(sortie, ep_idx_actions, v_actions)
    return sortie


def bras_episode(test_actions: np.ndarray, eligible, cond, pli, tache_idx, ep: dict, pli_ep: np.ndarray) -> dict:
    """Bras au niveau de l'épisode, au format de `calcul_v1` (`test`, `calib`, `calib_lignes`) : `test[e]` = statistique
    de l'épisode e avec le réservoir de son propre pli ; `calib[k]` = statistiques des 48 épisodes honnêtes des tâches
    d'entraînement du pli k avec le réservoir du pli k (sans leur propre tâche)."""
    s = np.asarray(test_actions, dtype=np.float64)
    if np.isnan(s[eligible]).any():
        raise GardeArret("bras par épisode : score d'action non défini sur une action éligible")
    test = np.full(ep["n"], np.nan)
    calib, calib_lignes, contributions = {}, {}, np.zeros(s.shape)
    for k in range(K.PLIS):
        res = eligible & (pli != k) & (cond == K.NEGATIF)
        ev_cal = res
        ev_test = eligible & (pli == k)
        v_cal = moins_log_p(s[res], tache_idx[res], s[ev_cal], tache_idx[ev_cal])
        v_test = moins_log_p(s[res], tache_idx[res], s[ev_test], tache_idx[ev_test])
        contributions[ev_test] = v_test
        stat_cal = _sommes(v_cal, ep["idx"][ev_cal], ep["n"])
        lignes = np.flatnonzero((pli_ep != k) & (ep["cond"] == K.NEGATIF))
        if lignes.size != K4.EPISODES_CALIBRAGE:
            raise GardeArret(f"calibrage par épisode : {lignes.size} épisodes honnêtes ≠ {K4.EPISODES_CALIBRAGE}")
        calib[k], calib_lignes[k] = stat_cal[lignes], lignes
        stat_test = _sommes(v_test, ep["idx"][ev_test], ep["n"])
        dans_k = pli_ep == k
        test[dans_k] = stat_test[dans_k]
    if np.isnan(test).any():
        raise GardeArret("bras par épisode : statistique non définie")
    return {"test": test, "calib": calib, "calib_lignes": calib_lignes, "contributions": contributions}


def pas_de_detection(contrib: np.ndarray, eligible, ep: dict, seuils: dict, pli_ep: np.ndarray, alarme_ep) -> dict:
    """Pas du premier franchissement du seuil (dans l'ordre des pas) pour chaque épisode en alarme (descriptif)."""
    sortie = {}
    for e in np.flatnonzero(alarme_ep):
        m = (ep["idx"] == e) & eligible
        o = np.argsort(ep["pas"][m], kind="mergesort")
        cum = np.cumsum(contrib[m][o])
        j = int(np.argmax(cum > seuils[int(pli_ep[e])]))
        sortie[ep["noms"][e]] = int(ep["pas"][m][o][j])
    return sortie


# ----------------------------------------------------------------------------------------------- plancher par épisode
def plancher_episode(X, eligible, cond, pli, tache_idx, ep: dict, pli_ep, U: np.ndarray, alphas) -> dict:
    """Plancher apparié par épisode : chaque direction aléatoire note les actions (entrées centrées réduites par les lignes
    d'entraînement du pli, comme `calcul_v1.plancher`), puis même transformation, même somme, même calibrage sur les 48
    épisodes honnêtes entiers ; rappel par épisode de chaque direction ; plancher = quantile 0,95 des rappels."""
    app = eligible & np.isin(cond, (K.POSITIF, K.NEGATIF))
    alarmes = {a: np.zeros(U.shape[0]) for a in alphas}
    total = 0
    for k in range(K.PLIS):
        tr = app & (pli != k)
        Xt = np.asarray(X[tr], dtype=np.float64)
        mu, sd = Xt.mean(axis=0), Xt.std(axis=0)
        sd = np.where(sd > 1e-8, sd, 1.0)
        res = eligible & (pli != k) & (cond == K.NEGATIF)
        ev = eligible & (pli == k) & (cond == K.POSITIF)
        S_res = ((np.asarray(X[res], dtype=np.float64) - mu) / sd) @ U.T
        S_ev = ((np.asarray(X[ev], dtype=np.float64) - mu) / sd) @ U.T
        v_cal = moins_log_p(S_res, tache_idx[res], S_res, tache_idx[res])
        v_ev = moins_log_p(S_res, tache_idx[res], S_ev, tache_idx[ev])
        cal = _sommes(v_cal, ep["idx"][res], ep["n"])
        lignes = np.flatnonzero((pli_ep != k) & (ep["cond"] == K.NEGATIF))
        cal = cal[lignes]
        sab = np.flatnonzero((pli_ep == k) & (ep["cond"] == K.POSITIF))
        st = _sommes(v_ev, ep["idx"][ev], ep["n"])[sab]
        tri = -np.sort(-cal, axis=0)
        n = cal.shape[0]
        for a in alphas:
            tau = tri[(n * a[0]) // a[1], :]
            alarmes[a] += (st > tau).sum(axis=0)
        total += sab.size
    sortie = {}
    for a in alphas:
        r = alarmes[a] / total
        sortie[CV.nom_alpha(a)] = {"plancher": float(np.quantile(r, K4.QUANTILE_PLANCHER)),
                                   "rappel_moyen": float(r.mean()), "rappel_max": float(r.max())}
    return sortie


__all__ = ["episodes_de", "plis_episodes", "moins_log_p", "bras_episode", "pas_de_detection", "plancher_episode"]

"""Noyau statistique de l'addendum de P3 (A1 à A4, constats G-02 à G-04), hors de l'arbre gelé.

Fonctions pures, sans lecture ni écriture de fichier, qui importent le code gelé sans le modifier :
- `aires_par_rangs` : calcul vectorisé exact des aires sous la courbe (Mann-Whitney, ex aequo pour moitié) sur une
  matrice de scores `(n_actions, n_sondes)`, identique à `sondes.evaluation.aire_sous_courbe` colonne par colonne ;
- `plancher_conjoint` (G-02) : rééchantillonnage conjoint par blocs de tâches de la sonde et de ses sondes de plancher,
  sur le même multi-ensemble d'actions à chaque tirage `b`, pour estimer `Δ(b) = A(b) − quantile_q(aires_plancher(b))` ;
- `contraste_par_blocs` (G-03) : différence d'aires appariée par blocs de tâches entre deux jeux de conditions
  `(pos_a, neg_a)` et `(pos_b, neg_b)` évalués sur les mêmes tâches tirées ;
- `t4_tranches_internes` (G-04 a) : aire stratifiée et écart au plancher stratifié avec recalcul des tranches de
  quantiles `strates_quantiles(valeurs[i], k)` à l'intérieur de chaque tirage bootstrap de tâches ;
- `t1_intra_tache` (G-04 b) : aire stratifiée intra-tâche (la tâche sert de strate) et son plancher stratifié ; si plus
  de `max_degeneres` tirages n'ont aucune paire intra-tâche, renvoie `calculable_bootstrap: False` avec les estimations
  ponctuelles, sans repli silencieux.
Aucune moyenne ni médiane sur les jetons d'une action. Tout paramètre ou tableau invalide lève `GardeArret`.
"""
from __future__ import annotations

import numpy as np

from controle_ia.gardes import GardeArret
from controle_ia.premier_test_ia.statistiques import _tables, aire_stratifiee, strates_quantiles
from controle_ia.sondes.evaluation import aire_sous_courbe


def _verifier_params_bootstrap(n_tirages: int, niveau: float, q: float = 0.95, max_degeneres: float = 0.01) -> None:
    if int(n_tirages) < 1:
        raise GardeArret("au moins un tirage bootstrap attendu")
    if not 0.0 < float(niveau) < 1.0:
        raise GardeArret("niveau de confiance dans ]0, 1[ attendu")
    if not 0.0 < float(q) < 1.0:
        raise GardeArret("quantile du plancher q dans ]0, 1[ attendu")
    if not 0.0 <= float(max_degeneres) <= 1.0:
        raise GardeArret("max_degeneres dans [0, 1] attendu")


def aires_par_rangs(scores_2d, y) -> np.ndarray:
    """Aires sous la courbe (Mann-Whitney, ex aequo pour moitié) pour chaque colonne de `scores_2d` `(n, m)`.

    Algorithme vectorisé exact en `O(m n log n)` par double tri stable (`mergesort`), sans boucle Python sur les
    valeurs uniques : pour chaque colonne triée, le premier et le dernier indice de chaque bloc d'ex aequo donnent
    le rang moyen `(premier + dernier) / 2 + 1`. Égal à `aire_sous_courbe` à la précision machine près.
    """
    S = np.asarray(scores_2d, dtype=np.float64)
    y_arr = np.asarray(y)
    if S.ndim != 2 or y_arr.ndim != 1 or S.shape[0] != y_arr.size:
        raise GardeArret("aires_par_rangs : scores_2d (n, m) et y (n,) de même longueur attendus")
    if S.shape[0] == 0 or S.shape[1] < 1:
        raise GardeArret("aires_par_rangs : au moins une ligne et une colonne attendues")
    if not np.all(np.isfinite(S)):
        raise GardeArret("aires_par_rangs : score non fini")
    if not set(np.unique(y_arr).tolist()) <= {0, 1}:
        raise GardeArret("aires_par_rangs : étiquettes 0 et 1 attendues")
    y_bin = y_arr.astype(np.int64)
    n1 = int(y_bin.sum())
    n0 = int(y_bin.size) - n1
    if n1 == 0 or n0 == 0:
        raise GardeArret("aires_par_rangs : les deux classes 0 et 1 doivent être présentes")

    n, m = S.shape
    ordre = np.argsort(S, axis=0, kind="mergesort")
    S_trie = np.take_along_axis(S, ordre, axis=0)

    diff = np.empty((n, m), dtype=bool)
    diff[0, :] = True
    if n > 1:
        diff[1:, :] = S_trie[1:, :] != S_trie[:-1, :]

    idx = np.arange(n, dtype=np.int64)[:, None]
    premier = np.maximum.accumulate(np.where(diff, idx, 0), axis=0)

    diff_fin = np.empty((n, m), dtype=bool)
    diff_fin[-1, :] = True
    if n > 1:
        diff_fin[:-1, :] = diff[1:, :]
    dernier = np.minimum.accumulate(np.where(diff_fin, idx, n - 1)[::-1, :], axis=0)[::-1, :]

    rangs_moyens = 0.5 * (premier + dernier) + 1.0
    y_trie = y_bin[ordre]
    somme_rangs_pos = (rangs_moyens * y_trie).sum(axis=0, dtype=np.float64)
    u = somme_rangs_pos - n1 * (n1 + 1) / 2.0
    return u / (n1 * n0)


def _aires_stratifiees_2d(scores_2d: np.ndarray, y: np.ndarray, strates: np.ndarray) -> np.ndarray | None:
    """Vecteur des aires stratifiées pour chaque colonne de `scores_2d`, ou `None` si aucune strate n'a de paire."""
    num = np.zeros(scores_2d.shape[1], dtype=np.float64)
    den = 0
    for s in np.unique(strates):
        m = strates == s
        n1 = int(y[m].sum())
        n0 = int(m.sum()) - n1
        if n1 > 0 and n0 > 0:
            num += aires_par_rangs(scores_2d[m], y[m]) * (n1 * n0)
            den += n1 * n0
    return None if den == 0 else (num / den)


def plancher_conjoint(s, plancher, y, tache, n_tirages: int, graine: int, niveau: float = 0.95,
                      q: float = 0.95, max_degeneres: float = 0.01) -> dict:
    """Écart conjoint au plancher par blocs de tâches (G-02) : `Δ(b) = A(b) − quantile_q(aires_plancher(b))`."""
    _verifier_params_bootstrap(n_tirages, niveau, q, max_degeneres)
    s_arr, y_, tache_arr, pl_arr = _tables(s, np.asarray(y), tache, plancher)
    y_bin = np.asarray(y_, dtype=np.int64)
    if not set(np.unique(y_bin).tolist()) <= {0, 1} or y_bin.sum() == 0 or y_bin.sum() == y_bin.size:
        raise GardeArret("plancher_conjoint : étiquettes 0 et 1 attendues, les deux présentes")

    tout = np.column_stack([s_arr, pl_arr])
    aires_obs = aires_par_rangs(tout, y_bin)
    aire_obs = float(aires_obs[0])
    seuil_obs = float(np.quantile(aires_obs[1:], q))
    delta_obs = float(aire_obs - seuil_obs)

    rng = np.random.default_rng(int(graine))
    uniques = np.unique(tache_arr)
    lignes = [np.flatnonzero(tache_arr == t) for t in uniques]
    deltas, aires_s, seuils_pl, degeneres = [], [], [], 0

    for _ in range(int(n_tirages)):
        i = np.concatenate([lignes[k] for k in rng.integers(0, uniques.size, uniques.size)])
        yi = y_bin[i]
        if yi.sum() == 0 or yi.sum() == yi.size:
            degeneres += 1
            continue
        ab = aires_par_rangs(tout[i], yi)
        a_b = float(ab[0])
        q_b = float(np.quantile(ab[1:], q))
        aires_s.append(a_b)
        seuils_pl.append(q_b)
        deltas.append(a_b - q_b)

    if degeneres > max_degeneres * int(n_tirages):
        raise GardeArret(f"plancher_conjoint : {degeneres} tirages dégénérés sur {n_tirages}")

    alpha = (1.0 - float(niveau)) / 2.0
    bas = float(np.quantile(deltas, alpha))
    haut = float(np.quantile(deltas, 1.0 - alpha))
    return {
        "aire": aire_obs,
        "plancher_quantile": seuil_obs,
        "delta_obs": delta_obs,
        "bas": bas,
        "haut": haut,
        "aire_bas": float(np.quantile(aires_s, alpha)),
        "aire_haut": float(np.quantile(aires_s, 1.0 - alpha)),
        "plancher_bas": float(np.quantile(seuils_pl, alpha)),
        "plancher_haut": float(np.quantile(seuils_pl, 1.0 - alpha)),
        "niveau": float(niveau),
        "quantile_plancher": float(q),
        "tirages": len(deltas),
        "degeneres": degeneres,
        "au_dessus_conjoint": bool(bas > 0.0),
    }


def contraste_par_blocs(s, condition, tache, jeu_a: tuple[str, str], jeu_b: tuple[str, str],
                        n_tirages: int, graine: int, niveau: float = 0.95, max_degeneres: float = 0.01) -> dict:
    """Différence d'aires appariée par blocs de tâches entre deux jeux `(pos_a, neg_a)` et `(pos_b, neg_b)` (G-03)."""
    _verifier_params_bootstrap(n_tirages, niveau, 0.95, max_degeneres)
    s_arr, cond_arr, tache_arr, _ = _tables(s, condition, tache)
    pos_a, neg_a = jeu_a
    pos_b, neg_b = jeu_b
    if pos_a == neg_a or pos_b == neg_b:
        raise GardeArret("contraste_par_blocs : positifs et négatifs d'un même jeu doivent différer")

    def _aire_jeu(idx: np.ndarray, pos: str, neg: str) -> float | None:
        c = cond_arr[idx]
        m = (c == pos) | (c == neg)
        if not m.any():
            return None
        y_j = (c[m] == pos).astype(np.int64)
        if y_j.sum() == 0 or y_j.sum() == y_j.size:
            return None
        return float(aire_sous_courbe(s_arr[idx][m], y_j))

    ous_idx = np.arange(s_arr.size, dtype=np.int64)
    aire_a = _aire_jeu(ous_idx, pos_a, neg_a)
    aire_b = _aire_jeu(ous_idx, pos_b, neg_b)
    if aire_a is None or aire_b is None:
        raise GardeArret("contraste_par_blocs : l'un des deux jeux a une classe manquante sur l'échantillon")
    diff_obs = float(aire_a - aire_b)

    rng = np.random.default_rng(int(graine))
    uniques = np.unique(tache_arr)
    lignes = [np.flatnonzero(tache_arr == t) for t in uniques]
    diffs, degeneres = [], 0

    for _ in range(int(n_tirages)):
        i = np.concatenate([lignes[k] for k in rng.integers(0, uniques.size, uniques.size)])
        aa = _aire_jeu(i, pos_a, neg_a)
        ab = _aire_jeu(i, pos_b, neg_b)
        if aa is None or ab is None:
            degeneres += 1
        else:
            diffs.append(aa - ab)

    if degeneres > max_degeneres * int(n_tirages):
        raise GardeArret(f"contraste_par_blocs : {degeneres} tirages dégénérés sur {n_tirages}")

    alpha = (1.0 - float(niveau)) / 2.0
    bas = float(np.quantile(diffs, alpha))
    haut = float(np.quantile(diffs, 1.0 - alpha))
    return {
        "jeu_a": f"{pos_a}-{neg_a}",
        "jeu_b": f"{pos_b}-{neg_b}",
        "aire_a": aire_a,
        "aire_b": aire_b,
        "difference": diff_obs,
        "bas": bas,
        "haut": haut,
        "niveau": float(niveau),
        "tirages": len(diffs),
        "degeneres": degeneres,
        "a_au_dessus_de_b": bool(bas > 0.0),
    }


def t4_tranches_internes(s, plancher, y, valeurs, tache, k: int, n_tirages: int, graine: int,
                         niveau: float = 0.95, q: float = 0.95, max_degeneres: float = 0.01) -> dict:
    """Test T4 avec recalcul des quintiles `strates_quantiles(valeurs[i], k)` dans chaque tirage bootstrap (G-04 a)."""
    _verifier_params_bootstrap(n_tirages, niveau, q, max_degeneres)
    s_arr, y_, tache_arr, pl_arr = _tables(s, np.asarray(y), tache, plancher)
    y_bin = np.asarray(y_, dtype=np.int64)
    val_arr = np.asarray(valeurs, dtype=np.float64)
    if val_arr.shape != s_arr.shape or not np.all(np.isfinite(val_arr)):
        raise GardeArret("t4_tranches_internes : valeurs finies de même longueur que s attendues")
    if int(k) < 1 or not set(np.unique(y_bin).tolist()) <= {0, 1} or y_bin.sum() == 0 or y_bin.sum() == y_bin.size:
        raise GardeArret("t4_tranches_internes : k >= 1 et étiquettes 0 et 1 présentes attendus")

    tout = np.column_stack([s_arr, pl_arr])
    strates_obs = strates_quantiles(val_arr, int(k))
    aires_obs = _aires_stratifiees_2d(tout, y_bin, strates_obs)
    if aires_obs is None:
        raise GardeArret("t4_tranches_internes : aucune paire positif-négatif dans une même tranche")
    aire_obs = float(aires_obs[0])
    seuil_obs = float(np.quantile(aires_obs[1:], q))
    delta_obs = float(aire_obs - seuil_obs)

    rng = np.random.default_rng(int(graine))
    uniques = np.unique(tache_arr)
    lignes = [np.flatnonzero(tache_arr == t) for t in uniques]
    tirages_aire, tirages_delta, degeneres = [], [], 0

    for _ in range(int(n_tirages)):
        i = np.concatenate([lignes[j] for j in rng.integers(0, uniques.size, uniques.size)])
        yi = y_bin[i]
        if yi.sum() == 0 or yi.sum() == yi.size:
            degeneres += 1
            continue
        strates_b = strates_quantiles(val_arr[i], int(k))
        ab = _aires_stratifiees_2d(tout[i], yi, strates_b)
        if ab is None:
            degeneres += 1
            continue
        a_b = float(ab[0])
        q_b = float(np.quantile(ab[1:], q))
        tirages_aire.append(a_b)
        tirages_delta.append(a_b - q_b)

    if degeneres > max_degeneres * int(n_tirages):
        raise GardeArret(f"t4_tranches_internes : {degeneres} tirages dégénérés sur {n_tirages}")

    alpha = (1.0 - float(niveau)) / 2.0
    bas = float(np.quantile(tirages_aire, alpha))
    haut = float(np.quantile(tirages_aire, 1.0 - alpha))
    delta_bas = float(np.quantile(tirages_delta, alpha))
    delta_haut = float(np.quantile(tirages_delta, 1.0 - alpha))
    return {
        "aire": aire_obs,
        "bas": bas,
        "haut": haut,
        "plancher_quantile": seuil_obs,
        "plancher_mediane": float(np.median(aires_obs[1:])),
        "delta_obs": delta_obs,
        "delta_bas": delta_bas,
        "delta_haut": delta_haut,
        "niveau": float(niveau),
        "quantile_plancher": float(q),
        "tirages": len(tirages_aire),
        "degeneres": degeneres,
        "tranches": int(k),
        "au_dessus_du_plancher": bool(bas > seuil_obs),
        "au_dessus_conjoint": bool(delta_bas > 0.0),
    }


def t1_intra_tache(s, plancher, y, tache, n_tirages: int, graine: int, niveau: float = 0.95,
                   q: float = 0.95, max_degeneres: float = 0.01) -> dict:
    """Test T1 stratifié par tâche (G-04 b) : seules les paires `(1, 0)` d'une même tâche entrent dans l'aire."""
    _verifier_params_bootstrap(n_tirages, niveau, q, max_degeneres)
    s_arr, y_, tache_arr, pl_arr = _tables(s, np.asarray(y), tache, plancher)
    y_bin = np.asarray(y_, dtype=np.int64)
    if not set(np.unique(y_bin).tolist()) <= {0, 1} or y_bin.sum() == 0 or y_bin.sum() == y_bin.size:
        raise GardeArret("t1_intra_tache : étiquettes 0 et 1 attendues, les deux présentes")

    tout = np.column_stack([s_arr, pl_arr])
    aires_obs = _aires_stratifiees_2d(tout, y_bin, tache_arr)
    if aires_obs is None:
        return {
            "calculable": False,
            "calculable_bootstrap": False,
            "motif": "aucune tâche ne contient à la fois une action qui gonfle (1) et une qui ne gonfle pas (0)",
            "aire": None,
            "plancher_quantile": None,
            "delta_obs": None,
        }

    aire_obs = float(aires_obs[0])
    seuil_obs = float(np.quantile(aires_obs[1:], q))
    delta_obs = float(aire_obs - seuil_obs)

    uniques = np.unique(tache_arr)
    taches_utiles = sum(1 for t in uniques if 0 < int(y_bin[tache_arr == t].sum()) < int((tache_arr == t).sum()))

    rng = np.random.default_rng(int(graine))
    lignes = [np.flatnonzero(tache_arr == t) for t in uniques]
    tirages_aire, tirages_delta, degeneres = [], [], 0

    for _ in range(int(n_tirages)):
        k_draw = rng.integers(0, uniques.size, uniques.size)
        i = np.concatenate([lignes[j] for j in k_draw])
        # Chaque bloc tiré conserve son identité de tâche pour la stratification intra-tâche
        ab = _aires_stratifiees_2d(tout[i], y_bin[i], tache_arr[i])
        if ab is None:
            degeneres += 1
            continue
        a_b = float(ab[0])
        q_b = float(np.quantile(ab[1:], q))
        tirages_aire.append(a_b)
        tirages_delta.append(a_b - q_b)

    base = {
        "calculable": True,
        "aire": aire_obs,
        "plancher_quantile": seuil_obs,
        "plancher_mediane": float(np.median(aires_obs[1:])),
        "delta_obs": delta_obs,
        "taches_mixtes": int(taches_utiles),
        "niveau": float(niveau),
        "quantile_plancher": float(q),
        "degeneres": degeneres,
    }
    if degeneres > max_degeneres * int(n_tirages):
        return {
            **base,
            "calculable_bootstrap": False,
            "motif_bootstrap": f"{degeneres} tirages sans paire intra-tâche sur {n_tirages} (seuil {max_degeneres})",
            "bas": None,
            "haut": None,
            "delta_bas": None,
            "delta_haut": None,
            "au_dessus_du_plancher": None,
            "au_dessus_conjoint": None,
        }

    alpha = (1.0 - float(niveau)) / 2.0
    bas = float(np.quantile(tirages_aire, alpha))
    haut = float(np.quantile(tirages_aire, 1.0 - alpha))
    delta_bas = float(np.quantile(tirages_delta, alpha))
    delta_haut = float(np.quantile(tirages_delta, 1.0 - alpha))
    return {
        **base,
        "calculable_bootstrap": True,
        "tirages": len(tirages_aire),
        "bas": bas,
        "haut": haut,
        "delta_bas": delta_bas,
        "delta_haut": delta_haut,
        "au_dessus_du_plancher": bool(bas > seuil_obs),
        "au_dessus_conjoint": bool(delta_bas > 0.0),
    }

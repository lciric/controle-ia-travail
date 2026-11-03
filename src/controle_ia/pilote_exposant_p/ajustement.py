"""Ajustement de l'exposant p d'un plan, au protocole du papier, et intervalles par rééchantillonnage.

Protocole repris du code publié (`scripts/fit_pairs.py --per_pair_threshold --exact`, `n_bootstrap 0`) :
- grille médiane sur les ancres (éq. 2 du papier) ;
- seuil par paire T = f · min(max de l'axe 1, max de l'axe 2) de la grille médiane, f = 0,5 (éq. 3) ;
- contour d'iso-réponse au niveau T, fenêtre de 60° (`superellipse.fit_p_one_pass`, `exact_geodesic=True`,
  normalisation sin α cos φ / sin α₁, éq. 13) ; p borné dans [0,5 ; 10] (`fit_superellipse`).

Le calcul lui-même est celui de la copie amont, appelée sans modification.
"""
from __future__ import annotations

import numpy as np

from .amont import superellipse as _se

F_SEUIL = 0.5
FENETRE_DEG = 60.0


def seuil_par_paire(grille_mediane: np.ndarray, f: float = F_SEUIL) -> float:
    return float(f * min(float(grille_mediane[:, 0].max()), float(grille_mediane[0, :].max())))


def ajuster_plan(angles_deg: np.ndarray, grilles: np.ndarray, f: float = F_SEUIL,
                 fenetre_deg: float = FENETRE_DEG) -> dict:
    """`grilles` : (n_ancres, n, n), réponse L2 par ancre. Rend p, nombre de points de contour, résidu, intercepts,
    seuil. p vaut NaN si l'ajustement est impossible (moins de 3 points, axe non franchi)."""
    g = np.asarray(grilles, dtype=np.float64)
    if g.ndim != 3 or g.shape[1] != g.shape[2] or g.shape[1] != len(angles_deg):
        raise ValueError(f"grilles de forme {g.shape} incompatibles avec {len(angles_deg)} angles")
    mg = np.median(g, axis=0)
    T = seuil_par_paire(mg, f)
    r = _se.fit_p_one_pass(np.asarray(angles_deg, dtype=np.float64), mg, T, fenetre_deg, exact_geodesic=True)
    return {"p": float(r["p"]), "n_pts": int(r["n_pts"]), "residu": float(r["mean_radial_frac"]),
            "intercepts": [float(r["intercepts"][0]), float(r["intercepts"][1])], "seuil": T}


def bootstrap_ancres(angles_deg: np.ndarray, grilles: np.ndarray, B: int, rng: np.random.Generator,
                     f: float = F_SEUIL, fenetre_deg: float = FENETRE_DEG) -> list[dict]:
    """Rééchantillonnage des ancres (invites) avec remise ; seuil recalculé à chaque tirage."""
    n = grilles.shape[0]
    return [ajuster_plan(angles_deg, grilles[rng.integers(0, n, n)], f, fenetre_deg) for _ in range(B)]


def intervalle_percentile(valeurs: np.ndarray, niveau: float = 0.95) -> tuple[float, float]:
    v = np.asarray(valeurs, dtype=np.float64)
    v = v[np.isfinite(v)]
    if v.size == 0:
        return float("nan"), float("nan")
    a = (1.0 - niveau) / 2.0
    return float(np.percentile(v, 100 * a)), float(np.percentile(v, 100 * (1 - a)))


def bootstrap_difference(p_plan_par_sous_ensemble: np.ndarray, p_reference_par_plan: np.ndarray, B: int,
                         rng: np.random.Generator, niveau: float = 0.95) -> dict:
    """Δ = moyenne des p du plan lu sur ses sous-ensembles d'ancres indépendants − moyenne des p des plans de la
    famille de référence (plans indépendants, directions disjointes). Intervalle : rééchantillonnage conjoint, avec
    remise, des sous-ensembles d'ancres du plan lu et des plans de la référence ; percentile."""
    a = np.asarray(p_plan_par_sous_ensemble, dtype=np.float64)
    b = np.asarray(p_reference_par_plan, dtype=np.float64)
    a = a[np.isfinite(a)]
    b = b[np.isfinite(b)]
    if a.size < 2 or b.size < 2:
        return {"delta": float("nan"), "ic": [float("nan"), float("nan")], "n_plan": int(a.size), "n_ref": int(b.size)}
    ia = rng.integers(0, a.size, (B, a.size))
    ib = rng.integers(0, b.size, (B, b.size))
    d = a[ia].mean(axis=1) - b[ib].mean(axis=1)
    lo, hi = intervalle_percentile(d, niveau)
    return {"delta": float(a.mean() - b.mean()), "ic": [lo, hi], "n_plan": int(a.size), "n_ref": int(b.size),
            "moyenne_plan": float(a.mean()), "moyenne_ref": float(b.mean()),
            "ic_plan": list(intervalle_percentile(a[ia].mean(axis=1), niveau)),
            "ic_ref": list(intervalle_percentile(b[ib].mean(axis=1), niveau))}


def bootstrap_moyenne(valeurs: np.ndarray, B: int, rng: np.random.Generator, niveau: float = 0.95) -> dict:
    v = np.asarray(valeurs, dtype=np.float64)
    v = v[np.isfinite(v)]
    if v.size < 2:
        return {"moyenne": float(v.mean()) if v.size else float("nan"), "ic": [float("nan"), float("nan")], "n": int(v.size)}
    i = rng.integers(0, v.size, (B, v.size))
    return {"moyenne": float(v.mean()), "mediane": float(np.median(v)), "ic": list(intervalle_percentile(v[i].mean(axis=1), niveau)),
            "n": int(v.size)}

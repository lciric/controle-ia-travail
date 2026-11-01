"""Modèles des bras entraînés : régression logistique à pénalité L2 (bras (i) et témoin lexical), traits du texte du
témoin lexical, aire sous la courbe (Mann-Whitney, ex aequo pour moitié) et directions aléatoires du plancher apparié.

Aucune moyenne ni médiane sur les jetons d'une action n'est calculée ici : les activations arrivent déjà réduites par
action (fichier R1 : moyenne et maximum par dimension, sur l'empan noté par P3). Le bras (i) sur la moyenne est un bras de
diagnostic au sens de N-026 (jamais en production).
"""
from __future__ import annotations

import math

import numpy as np
from scipy.optimize import minimize
from scipy.stats import rankdata

from ..gardes import GardeArret
from . import constantes as C


def aire(scores, y) -> float:
    """Statistique de Mann-Whitney normalisée, ex aequo pour moitié (même formule que `sondes.evaluation`)."""
    s, y = np.asarray(scores, dtype=np.float64), np.asarray(y)
    if s.ndim != 1 or s.shape != y.shape:
        raise GardeArret("aire : scores et étiquettes, vecteurs de même longueur attendus")
    if not np.all(np.isfinite(s)):
        raise GardeArret("aire : score non fini")
    n1, n0 = int((y == 1).sum()), int((y == 0).sum())
    if n1 == 0 or n0 == 0 or n1 + n0 != y.size:
        raise GardeArret("aire : les deux classes 0/1 sont nécessaires")
    r = rankdata(s)
    return float((r[y == 1].sum() - n1 * (n1 + 1) / 2.0) / (n1 * n0))


def ajuster_logistique(X, y, lam: float | None = None) -> dict:
    """Régression logistique : entrées réduites par la moyenne et l'écart type des lignes d'entraînement (écart type
    sous 1e-8 remplacé par 1, colonne constante), minimise Σ [log(1 + e^z) − y z] + λ‖w‖²/2, constante non pénalisée,
    L-BFGS-B depuis zéro, double précision. Une optimisation qui ne converge pas arrête (R5)."""
    lam = C.LAMBDA_L2 if lam is None else float(lam)
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    if X.ndim != 2 or y.shape != (X.shape[0],):
        raise GardeArret(f"logistique : X de forme {X.shape} et y de forme {y.shape} incompatibles")
    if not set(np.unique(y).tolist()) <= {0.0, 1.0} or len(set(y.tolist())) < 2:
        raise GardeArret("logistique : étiquettes 0/1, les deux classes, attendues")
    if not np.all(np.isfinite(X)):
        raise GardeArret("logistique : entrée non finie")
    mu = X.mean(axis=0)
    sd = X.std(axis=0)
    sd = np.where(sd > 1e-8, sd, 1.0)
    Z = (X - mu) / sd

    def objectif(theta):
        w, b = theta[:-1], theta[-1]
        z = Z @ w + b
        p = np.exp(-np.logaddexp(0.0, -z))
        perte = float(np.sum(np.logaddexp(0.0, z) - y * z) + 0.5 * lam * (w @ w))
        r = p - y
        return perte, np.concatenate([Z.T @ r + lam * w, [r.sum()]])

    res = minimize(objectif, np.zeros(Z.shape[1] + 1), jac=True, method="L-BFGS-B",
                   options={"maxiter": int(C.ITERATIONS_MAX), "gtol": float(C.TOLERANCE_GRADIENT)})
    if not res.success or not np.all(np.isfinite(res.x)):
        raise GardeArret(f"logistique : ajustement non convergé ({res.message})")
    return {"mu": mu, "sd": sd, "w": res.x[:-1].copy(), "b": float(res.x[-1]), "iterations": int(res.nit),
            "perte": float(res.fun)}


def logits(modele: dict, X) -> np.ndarray:
    """Score d'action du bras entraîné : log-cote w·((x − μ)/σ) + b."""
    s = ((np.asarray(X, dtype=np.float64) - modele["mu"]) / modele["sd"]) @ modele["w"] + modele["b"]
    if not np.all(np.isfinite(s)):
        raise GardeArret("logistique : score non fini")
    return s


def traits_lexicaux(tables: dict) -> tuple[np.ndarray, list[str]]:
    """Traits du texte seul, une ligne par action, calculés sans modèle de langue (colonnes de `scores-p3.npz`, lues sur
    l'instance par `conditions.mesures_action`) : log10 du coût déclaré lisible (NaN sinon : imputé dans chaque pli par
    la médiane des lignes d'entraînement), indicateur de coût lisible, log(1 + jetons notés), et les treize drapeaux de
    `TRAITS_BOOLEENS`. Le rang du pas n'en est pas : ce n'est pas un trait du texte."""
    cout = np.asarray(tables["cout"], dtype=np.float64)
    lisible = np.isfinite(cout) & (cout > 0)
    log_cout = np.full(cout.shape, np.nan)
    log_cout[lisible] = np.log10(cout[lisible])
    colonnes = [log_cout, lisible.astype(np.float64), np.log1p(np.asarray(tables["jetons_notes"], dtype=np.float64))]
    noms = ["log10_cout", "cout_lisible", "log1p_jetons_notes"]
    for k in C.TRAITS_BOOLEENS:
        if k not in tables:
            raise GardeArret(f"trait {k} absent du fichier des scores")
        colonnes.append(np.asarray(tables[k]).astype(np.float64))
        noms.append(k)
    F = np.column_stack(colonnes)
    if not np.all(np.isfinite(F[:, 1:])):
        raise GardeArret("traits du texte : valeur non finie hors du coût")
    return F, noms


def imputer_cout(F: np.ndarray, lignes_reference: np.ndarray) -> np.ndarray:
    """Copie de F où le log10 du coût illisible (NaN, colonne 0) prend la médiane des coûts lisibles des lignes de
    référence (lignes d'entraînement du pli). Aucune ligne de référence lisible : arrêt."""
    ref = F[lignes_reference, 0]
    ref = ref[np.isfinite(ref)]
    if ref.size == 0:
        raise GardeArret("témoin lexical : aucun coût lisible dans les lignes de référence")
    G = F.copy()
    G[~np.isfinite(G[:, 0]), 0] = float(np.median(ref))
    return G


def directions_plancher(X_entrainement: np.ndarray, n: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Directions aléatoires w ~ N(0, Σ̂), Σ̂ covariance empirique (ddof = 1) des lignes d'entraînement, tirées sans former
    Σ̂ : w = X_cᵀ g / √(n − 1), g ~ N(0, I) ; rend (μ, W) avec W de forme (d, n). Score d'une action : (x − μ)·w
    (sonde centrée, comme le plancher de P3, recette appliquée aux activations moyennes)."""
    X = np.asarray(X_entrainement, dtype=np.float64)
    if X.ndim != 2 or X.shape[0] < 2:
        raise GardeArret("plancher : au moins deux lignes d'entraînement")
    mu = X.mean(axis=0)
    G = rng.standard_normal((X.shape[0], int(n)))
    return mu, (X - mu).T @ G / math.sqrt(X.shape[0] - 1)

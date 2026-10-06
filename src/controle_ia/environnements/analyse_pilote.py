"""Analyse du pilote de l'environnement (a) (T0.5) : décomposition de variance des juges, couverture des cibles,
accord de l'appariement. Sur processeur, à partir des résultats scellés du run.

Décomposition (annexe C.1 de 2606.08892v2, p. 17-18), adaptée à un seul générateur (σ²_générateur = 0) :
- run A : un épisode par tâche, noté une fois ; run B : les mêmes ensembles, notés une seconde fois ;
  run C : un autre épisode par tâche, noté une fois ;
- σ²_ε (bruit du juge) = V[sA − sB] / 2 ; σ²_β (tâche) = Cov[sA, sC] ; σ²_δ (bruit de génération) =
  Cov[sA, sB] − Cov[sA, sC] ; V[s] = σ²_β + σ²_δ + σ²_ε (forme de l'article, équation 22, avec σ²_α = 0).
Une tâche dont une des trois notes manque sort de la décomposition (nombre rapporté), sans imputation.
"""
from __future__ import annotations

import numpy as np

from ..gardes import GardeArret


def _cov(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.mean((x - x.mean()) * (y - y.mean())) * len(x) / (len(x) - 1))


def decomposition_variance(sA, sB, sC) -> dict:
    """Composantes et parts ; les trois tableaux sont alignés par tâche (NaN = note manquante)."""
    a, b, c = (np.asarray(v, dtype=float) for v in (sA, sB, sC))
    if not (a.shape == b.shape == c.shape) or a.ndim != 1:
        raise GardeArret("notes A, B et C non alignées par tâche")
    gardees = ~(np.isnan(a) | np.isnan(b) | np.isnan(c))
    n = int(gardees.sum())
    if n < 3:
        raise GardeArret(f"{n} tâches complètes : décomposition impossible")
    a, b, c = a[gardees], b[gardees], c[gardees]
    eps = float(np.var(a - b, ddof=1) / 2)
    beta = _cov(a, c)
    delta = _cov(a, b) - beta
    total = beta + delta + eps
    parts = {k: (v / total if total > 0 else float("nan")) for k, v in
             (("tache", beta), ("generation", delta), ("juge", eps))}
    return {"taches": n, "taches_incompletes": int((~gardees).sum()),
            "composantes": {"tache": beta, "generation": delta, "juge": eps, "totale": total}, "parts": parts}


def intervalles_parts(sA, sB, sC, tirages: int, rng: np.random.Generator, niveau: float = 0.95) -> dict:
    """Intervalles des parts par rééchantillonnage des tâches (percentiles)."""
    a, b, c = (np.asarray(v, dtype=float) for v in (sA, sB, sC))
    complet = ~(np.isnan(a) | np.isnan(b) | np.isnan(c))
    a, b, c = a[complet], b[complet], c[complet]
    n = len(a)
    if n < 3:
        raise GardeArret(f"{n} tâches complètes : intervalles impossibles")
    tirees = {k: [] for k in ("tache", "generation", "juge")}
    for _ in range(tirages):
        idx = rng.integers(0, n, size=n)
        try:
            d = decomposition_variance(a[idx], b[idx], c[idx])
        except GardeArret:
            continue
        for k in tirees:
            tirees[k].append(d["parts"][k])
    q = (1 - niveau) / 2
    return {k: [float(np.nanquantile(v, q)), float(np.nanquantile(v, 1 - q))] for k, v in tirees.items()}


def kappa_cohen(x, y) -> float:
    """Kappa de Cohen pour deux étiquetages binaires de mêmes éléments."""
    x, y = np.asarray(x, dtype=bool), np.asarray(y, dtype=bool)
    if x.shape != y.shape or x.size == 0:
        raise GardeArret("étiquetages de tailles différentes ou vides")
    po = float(np.mean(x == y))
    pe = float(x.mean() * y.mean() + (1 - x.mean()) * (1 - y.mean()))
    if pe == 1.0:
        raise GardeArret("accord attendu égal à 1 (une seule classe) : kappa indéfini")
    return (po - pe) / (1 - pe)


def couverture(p_oui: dict[tuple[int, str], float], propositions: list[int], cibles: list[str],
               seuil: float = 0.5) -> dict:
    """Couverture d'un ensemble final : part des cibles appariées à au moins une proposition, et cibles couvertes.
    `p_oui[(numéro de proposition, identifiant de cible)]` ; une paire absente arrête (aucune valeur par défaut)."""
    manquantes = [(k, c) for k in propositions for c in cibles if (k, c) not in p_oui]
    if manquantes:
        raise GardeArret(f"{len(manquantes)} paires d'appariement absentes, dont {manquantes[:3]}")
    if not cibles:
        raise GardeArret("aucune cible")
    couvertes = sorted({c for c in cibles for k in propositions if p_oui[(k, c)] >= seuil})
    return {"part": len(couvertes) / len(cibles), "couvertes": couvertes}

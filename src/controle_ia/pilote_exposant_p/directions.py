"""Directions du pilote : différences de moyennes, différences aléatoires, isotropes ; cosinus et règle d'exclusion.

- Différence de moyennes (éq. 4 et 5 du papier) : d = moyenne(b − a) sur les paires, normalisée ; activation du dernier
  jeton à la sortie du bloc ℓ (`hidden_states[ℓ + 1]` du code publié).
- Différence aléatoire (éq. 6 et 7 ; code publié `random_diff_directions.py`, k_avg = 30, famille « Random-diff » du
  papier) : moyenne de 30 différences d'activations tirées au hasard dans une réserve FineWeb-edu de 10 000 entrées,
  paires disjointes, normalisée. Tirage par `numpy.random.Generator` issu d'une `SeedSequence` (R9), et non par la
  graine 42 de torch du code publié (écart déclaré : même construction, autre tirage).
- Isotropes du papier (code publié `random_directions.py`) : `torch.randn` à graine 42 de torch, 33 × d, normalisées ;
  reproduites à l'identique (empreinte publiée vérifiée par les essais) et prises comme stimuli fixes.
- Règle d'exclusion (§4.1 et annexe A du papier) : une paire de directions dont le recouvrement brut |⟨d₁, d₂⟩| est
  ≥ 0,1 est exclue (texte du papier : « < 0,1 » gardé ; le code publié garde ≤ 0,1, écart sans effet pratique).
"""
from __future__ import annotations

import numpy as np

SEUIL_COS = 0.1
K_MOY = 30


def normaliser(v: np.ndarray) -> np.ndarray:
    v = np.asarray(v, dtype=np.float64)
    n = float(np.linalg.norm(v))
    if not np.isfinite(n) or n == 0.0:
        raise ValueError("vecteur nul ou non fini : direction indéfinie")
    return v / n


def difference_de_moyennes(acts_a: np.ndarray, acts_b: np.ndarray) -> np.ndarray:
    """(P, d) et (P, d), appariées ligne à ligne ; rend la direction unitaire de a vers b."""
    a = np.asarray(acts_a, dtype=np.float64)
    b = np.asarray(acts_b, dtype=np.float64)
    if a.shape != b.shape or a.ndim != 2:
        raise ValueError(f"activations appariées de formes {a.shape} et {b.shape}")
    return normaliser((b - a).mean(axis=0))


def differences_aleatoires(reserve: np.ndarray, K: int, rng: np.random.Generator, k_moy: int = K_MOY) -> tuple[np.ndarray, np.ndarray]:
    """K directions, chacune moyenne de `k_moy` différences sur des paires disjointes de la réserve (N, d).
    Rend (directions (K, d), indices (K, k_moy, 2))."""
    N = reserve.shape[0]
    besoin = 2 * K * k_moy
    if N < besoin:
        raise ValueError(f"réserve de {N} entrées < {besoin} nécessaires ({K} directions × {k_moy} paires disjointes)")
    perm = rng.permutation(N)[:besoin]
    i, j = perm[0::2].reshape(K, k_moy), perm[1::2].reshape(K, k_moy)
    r = np.asarray(reserve, dtype=np.float64)
    d = (r[i] - r[j]).mean(axis=1)
    return np.stack([normaliser(x) for x in d]), np.stack([i, j], axis=-1)


def isotropes_papier(n: int = 33, d: int = 4096, graine: int = 42) -> np.ndarray:
    """Directions isotropes du code publié (`torch.Generator().manual_seed(42)`, `torch.randn`, normalisation)."""
    import torch
    import torch.nn.functional as F

    g = torch.Generator().manual_seed(graine)
    return F.normalize(torch.randn(n, d, generator=g), dim=-1).numpy()


def cosinus(d1: np.ndarray, d2: np.ndarray) -> float:
    return float(np.dot(normaliser(d1), normaliser(d2)))


def paire_gardee(d1: np.ndarray, d2: np.ndarray, seuil: float = SEUIL_COS) -> bool:
    return abs(cosinus(d1, d2)) < seuil

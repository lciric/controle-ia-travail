"""Mesures de l'étape 2a, fonctions pures sur des tableaux (exploratoire).

Brouillon v7 du préenregistrement court, étape 2a et section « Seuil », paragraphe « Taille effective » :
- corrélation d'un pas au suivant : corrélation de Pearson des couples (x_t, x_{t+1}) mis en commun sur les épisodes,
  après centrage par épisode (défaut) ; taille effective d'une série AR(1) : n (1 − ρ) / (1 + ρ) ;
- taille effective par familles : ⌊n / (1 + (m̃ − 1) ρ)⌋, m̃ = Σm² / Σm, un ρ négatif compte pour 0 ;
- corrélation par famille de l'indicatrice d'alerte au seuil commun de 20 % : estimateur d'analyse de variance de la
  corrélation intra-classe ;
- taux d'alerte entre deux lots : seuil lu sur le premier lot (20 % en alerte), appliqué au second ; intervalle exact
  (Clopper-Pearson) sur l'effectif, ou sur un effectif effectif donné.
Convention d'alerte : score ≥ seuil, le seuil étant le ⌈q n⌉-ième plus grand score du lot d'étalonnage.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.stats import beta

from ..gardes import GardeArret

TAUX_COMMUN = 0.20


def _vecteur(x, quoi: str) -> np.ndarray:
    a = np.asarray(x, dtype=float)
    if a.ndim != 1 or not np.isfinite(a).all():
        raise GardeArret(f"{quoi} : vecteur fini attendu")
    return a


def correlation_pas_suivant(series, centrer_par_episode: bool = True) -> dict:
    """series : liste de vecteurs (un par épisode, valeurs aux pas successifs)."""
    gauches, droites = [], []
    for s in series:
        a = _vecteur(s, "série")
        if len(a) < 2:
            continue
        if centrer_par_episode:
            a = a - a.mean()
        gauches.append(a[:-1]); droites.append(a[1:])
    if not gauches:
        raise GardeArret("aucune série d'au moins deux pas")
    g, d = np.concatenate(gauches), np.concatenate(droites)
    if g.std() == 0 or d.std() == 0:
        raise GardeArret("corrélation indéfinie : valeurs constantes")
    return {"rho": float(np.corrcoef(g, d)[0, 1]), "couples": int(len(g)), "episodes": len(gauches)}


def taille_effective_serie(n: int, rho: float) -> float:
    if n < 1 or not -1 < rho < 1:
        raise GardeArret(f"n = {n}, ρ = {rho} : n ≥ 1 et ρ dans ]−1 ; 1[ attendus")
    return n * (1 - rho) / (1 + rho)


def taille_famille_ponderee(tailles) -> float:
    m = np.asarray(tailles, dtype=float)
    if m.ndim != 1 or len(m) == 0 or (m < 1).any():
        raise GardeArret("tailles de familles : entiers positifs attendus")
    return float((m ** 2).sum() / m.sum())


def taille_effective_familles(tailles, rho: float) -> int:
    """⌊n / (1 + (m̃ − 1) ρ)⌋, ρ négatif compté 0 (brouillon v7, « Taille effective »)."""
    if not math.isfinite(rho) or rho > 1:
        raise GardeArret(f"ρ = {rho} illisible")
    n = int(np.sum(tailles))
    mt = taille_famille_ponderee(tailles)
    return int(math.floor(n / (1 + (mt - 1) * max(0.0, rho)) + 1e-12))


def seuil_alerte(scores, taux: float = TAUX_COMMUN) -> float:
    s = _vecteur(scores, "scores")
    if not 0 < taux < 1 or len(s) == 0:
        raise GardeArret(f"taux {taux} ou lot vide")
    k = math.ceil(taux * len(s))
    return float(np.sort(s)[::-1][k - 1])


def indicatrice_alerte(scores, seuil: float) -> np.ndarray:
    return (_vecteur(scores, "scores") >= float(seuil)).astype(int)


def correlation_intra_famille(valeurs, familles) -> dict:
    """Estimateur d'analyse de variance : (CMI − CMR) / (CMI + (m₀ − 1) CMR), m₀ = (N − Σm²/N) / (k − 1)."""
    y = _vecteur(valeurs, "valeurs")
    f = np.asarray(familles)
    if len(f) != len(y):
        raise GardeArret("autant de familles que de valeurs attendu")
    noms, inv = np.unique(f, return_inverse=True)
    k, N = len(noms), len(y)
    if k < 2 or N <= k:
        raise GardeArret(f"{k} familles pour {N} valeurs : au moins deux familles et une famille de deux attendues")
    m = np.bincount(inv).astype(float)
    moy_f = np.bincount(inv, weights=y) / m
    moy = y.mean()
    cmi = float((m * (moy_f - moy) ** 2).sum() / (k - 1))
    cmr = float(((y - moy_f[inv]) ** 2).sum() / (N - k))
    m0 = (N - (m ** 2).sum() / N) / (k - 1)
    den = cmi + (m0 - 1) * cmr
    if den == 0:
        raise GardeArret("corrélation intra-famille indéfinie : aucune variance")
    return {"rho": (cmi - cmr) / den, "familles": int(k), "valeurs": int(N), "m0": float(m0),
            "taille_ponderee": taille_famille_ponderee(m)}


def correlation_alerte_par_famille(scores, familles, taux: float = TAUX_COMMUN) -> dict:
    """Indicatrice « en alerte au seuil commun de 20 % » puis corrélation intra-famille ; taille effective."""
    t = seuil_alerte(scores, taux)
    ind = indicatrice_alerte(scores, t)
    c = correlation_intra_famille(ind, familles)
    _, comptes = np.unique(np.asarray(familles), return_counts=True)
    c.update({"seuil": t, "taux_alerte": float(ind.mean()),
              "taille_effective": taille_effective_familles(comptes, c["rho"])})
    return c


def intervalle_exact(x: int, n: int, niveau: float = 0.95) -> tuple[float, float]:
    if not 0 <= x <= n or n < 1:
        raise GardeArret(f"x = {x}, n = {n}")
    a = 1 - niveau
    bas = 0.0 if x == 0 else float(beta.ppf(a / 2, x, n - x + 1))
    haut = 1.0 if x == n else float(beta.ppf(1 - a / 2, x + 1, n - x))
    return bas, haut


def taux_alerte_entre_lots(scores_a, scores_b, taux: float = TAUX_COMMUN, niveau: float = 0.95,
                           effectif_effectif_b: int | None = None) -> dict:
    """Seuil lu sur le lot A, taux d'alerte du lot B, intervalle exact ; avec un effectif effectif, les alertes sont
    ramenées à la même proportion (arrondi vers le bas) et l'intervalle se calcule sur cet effectif."""
    t = seuil_alerte(scores_a, taux)
    ind = indicatrice_alerte(scores_b, t)
    n, x = len(ind), int(ind.sum())
    if effectif_effectif_b is not None:
        if not 1 <= effectif_effectif_b <= n:
            raise GardeArret(f"effectif effectif {effectif_effectif_b} hors de [1, {n}]")
        x, n = int(math.floor(x * effectif_effectif_b / n)), int(effectif_effectif_b)
    bas, haut = intervalle_exact(x, n, niveau)
    return {"seuil": t, "taux_b": float(ind.mean()), "alertes": x, "effectif": n, "intervalle": [bas, haut],
            "taux_vise_dans_l_intervalle": bool(bas <= taux <= haut)}

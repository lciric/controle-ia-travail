"""Seuils, intervalles exacts et formes closes de la simulation d'essaim.

Seuil = (c, γ) : alarme si V > c, ou si V = c et U < γ, où U est un uniforme propre à chaque essaim,
indépendant de l'attaque (test aléatoirisé : taille exacte α pour une statistique discrète). Pour une
statistique continue γ = 1, donc alarme si V ≥ c (convention de T0.3). Sous un réarrangement de
classe C, U est celui de l'essaim honnête dont l'essaim attaqué est issu (nombres aléatoires communs) :
une statistique invariante donne alors la même alarme, trajectoire par trajectoire (T1).

Seuils :
- exacts sous la loi de référence (cases iid N(0, 1)) : somme, max, moyennes par agent et par pas
  (continus), comptages (aléatoirisés, lois binomiales) ;
- Monte-Carlo aléatoirisé (taux empirique exactement α sur l'échantillon de calibrage) ;
- Ville : log(1/α) ;
- conforme sur essaims honnêtes entiers, départage lexicographique par U : taux exact
  1 − ⌈(K + 1)(1 − α)⌉/(K + 1) pour des essaims échangeables.

Formes closes (loi de référence) : classe M par motif de décalage, borne inférieure de la co-élévation
sous synchronisation, taux de fausses alarmes des seuils de référence sous effet d'épisode et sous
équicorrélation entre agents (quadrature de Gauss-Hermite).
"""
from __future__ import annotations

import math

import numpy as np
from scipy import stats

from ..gardes import GardeArret
from ..simulation_t03 import calibrage as cal03

NOEUDS_GH = 200


def _alpha(alpha: float) -> float:
    if not (0.0 < alpha < 1.0):
        raise GardeArret(f"α = {alpha} hors de ]0, 1[")
    return alpha


def seuil_par_case(q: float) -> float:
    """u = quantile 1 − q de la marginale honnête N(0, 1) (toutes les lois de la grille ont cette marginale)."""
    if not (0.0 < q < 1.0):
        raise GardeArret(f"q = {q} hors de ]0, 1[")
    return float(stats.norm.isf(q))


# --- alarmes ---
def alarme(V, U, seuil) -> np.ndarray:
    c, g = seuil
    V, U = np.asarray(V), np.asarray(U)
    if V.shape != U.shape:
        raise GardeArret(f"statistique {V.shape} et départage {U.shape} de formes différentes")
    return (V > c) | ((V == c) & (U < g))


def seuil_continu(c: float) -> tuple[float, float]:
    if not math.isfinite(c):
        raise GardeArret(f"seuil non fini {c}")
    return (float(c), 1.0)


def seuil_ville(alpha: float) -> tuple[float, float]:
    return (math.log(1.0 / _alpha(alpha)), 1.0)


def seuil_mc(valeurs, alpha: float) -> tuple[float, float]:
    """(c, γ) tels que P̂(V > c) + γ P̂(V = c) = α exactement sur l'échantillon de calibrage."""
    v = np.sort(np.asarray(valeurs, dtype=float))
    if v.ndim != 1 or v.size == 0 or not np.all(np.isfinite(v)):
        raise GardeArret("calibrage Monte-Carlo : valeurs absentes ou non finies")
    R = v.size
    j = int(math.floor(_alpha(alpha) * R + 1e-9))
    if j >= R:
        raise GardeArret(f"calibrage Monte-Carlo : R = {R} trop petit pour α = {alpha}")
    c = float(v[R - 1 - j])
    droite, gauche = np.searchsorted(v, c, side="right"), np.searchsorted(v, c, side="left")
    k_sup, k_eg = R - droite, droite - gauche
    g = (alpha * R - k_sup) / k_eg
    if not (-1e-12 <= g < 1.0):
        raise GardeArret(f"calibrage Monte-Carlo : γ = {g} hors de [0, 1[")
    return (c, float(max(g, 0.0)))


def taux_discret(cdf, seuil) -> float:
    """P(V > c) + γ P(V = c) pour V entier de fonction de répartition cdf[k] = P(V ≤ k), k = 0…M."""
    c, g = seuil
    cdf = np.asarray(cdf, dtype=float)
    if c != math.floor(c):
        raise GardeArret(f"seuil {c} non entier pour une statistique de comptage")
    c = int(c)
    if c < 0:
        return 1.0
    if c >= cdf.size:
        return 0.0
    au_dessous = cdf[c - 1] if c >= 1 else 0.0
    return float((1.0 - cdf[c]) + g * (cdf[c] - au_dessous))


def seuil_max_discret(cdf_unite, n: int, alpha: float) -> tuple[float, float]:
    """V = max de n variables entières iid de répartition cdf_unite : seuil aléatoirisé de taille exacte α."""
    _alpha(alpha)
    G = np.minimum(np.asarray(cdf_unite, dtype=float), 1.0) ** n
    queue = 1.0 - G
    ok = np.flatnonzero(queue <= alpha)
    if ok.size == 0:
        raise GardeArret("seuil discret introuvable")
    c = int(ok[0])
    p_eg = G[c] - (G[c - 1] if c >= 1 else 0.0)
    if p_eg <= 0:
        raise GardeArret(f"seuil discret : masse nulle en c = {c}")
    g = (alpha - queue[c]) / p_eg
    if not (-1e-12 <= g <= 1.0 + 1e-12):
        raise GardeArret(f"seuil discret : γ = {g} hors de [0, 1]")
    return (float(c), float(min(max(g, 0.0), 1.0)))


def cdf_binom(n: int, p: float) -> np.ndarray:
    return stats.binom.cdf(np.arange(n + 1), n, p)


def seuils_exacts(K: int, T: int, q: float, alpha: float) -> dict[str, tuple[float, float]]:
    """Seuils exacts sous la loi de référence (cases iid N(0, 1)), taille exacte α."""
    n0 = K * T
    return {
        "somme": seuil_continu(cal03.seuil_somme_exact(alpha, n0)),
        "max": seuil_continu(cal03.seuil_max_exact(alpha, n0)),
        "agent_moyenne": seuil_continu(cal03.seuil_max_exact(alpha, K)),
        "pas_moyenne": seuil_continu(cal03.seuil_max_exact(alpha, T)),
        "comptage": seuil_max_discret(cdf_binom(n0, q), 1, alpha),
        "agent_comptage": seuil_max_discret(cdf_binom(T, q), K, alpha),
        "coelev_comptage": seuil_max_discret(cdf_binom(K, q), T, alpha),
    }


# --- intervalles exacts ---
def intervalle_cp(k: int, R: int, gamma: float) -> tuple[float, float]:
    """Intervalle de Clopper-Pearson bilatéral de niveau 1 − γ."""
    if not (0 <= k <= R) or R < 1:
        raise GardeArret(f"intervalle : k = {k}, R = {R} invalides")
    if not (0.0 < gamma < 1.0):
        raise GardeArret(f"γ = {gamma} hors de ]0, 1[")
    bas = 0.0 if k == 0 else float(stats.beta.ppf(gamma / 2, k, R - k + 1))
    haut = 1.0 if k == R else float(stats.beta.ppf(1 - gamma / 2, k + 1, R - k))
    return bas, haut


# --- calibrage conforme sur essaims entiers, départage par U ---
def rang_conforme(Kc: int, alpha: float) -> int:
    return cal03.rang_conforme(Kc, alpha)


def taux_conforme(Kc: int, alpha: float) -> float:
    return cal03.taux_conforme(Kc, alpha)


def seuil_conforme(V, U, alpha: float) -> tuple[float, float]:
    """j-ième plus petit couple (V, U) en ordre lexicographique, j = ⌈(K + 1)(1 − α)⌉."""
    V, U = np.asarray(V, dtype=float), np.asarray(U, dtype=float)
    if V.ndim != 1 or V.shape != U.shape or V.size == 0 or not np.all(np.isfinite(V)):
        raise GardeArret("calibrage conforme : valeurs absentes, non finies ou de formes différentes")
    j = rang_conforme(V.size, alpha)
    if j > V.size:
        raise GardeArret(f"calibrage conforme : K = {V.size} trop petit pour α = {alpha}")
    i = np.lexsort((U, V))[j - 1]
    return float(V[i]), float(U[i])


def alarme_conforme(V, U, seuil) -> np.ndarray:
    Vj, Uj = seuil
    V, U = np.asarray(V), np.asarray(U)
    return (V > Vj) | ((V == Vj) & (U >= Uj))


def region_conforme(L: int, n_test: int, Kc: int, alpha: float, gamma: float) -> tuple[int, int, float]:
    """Région d'acceptation exacte du nombre total d'alarmes sur L tirages de calibrage conforme, chacun
    suivi de n_test essais : somme de L lois bêta-binomiales (n_test, K + 1 − j, j). Renvoie (bas, haut,
    taux théorique) avec P(S < bas) ≤ γ/2 et P(S > haut) ≤ γ/2."""
    j = rang_conforme(Kc, alpha)
    a, b = Kc + 1 - j, j
    if a < 1:
        raise GardeArret("région conforme : K trop petit")
    un = stats.betabinom.pmf(np.arange(n_test + 1), n_test, a, b)
    taille = L * n_test + 1
    nfft = 1 << (taille - 1).bit_length()
    pmf = np.fft.irfft(np.fft.rfft(un, nfft) ** L, nfft)[:taille]
    pmf = np.clip(pmf, 0.0, None)
    pmf /= pmf.sum()
    cdf = np.cumsum(pmf)
    bas = int(np.flatnonzero(cdf > gamma / 2)[0])
    haut = int(np.flatnonzero(1.0 - cdf <= gamma / 2)[0])
    return bas, haut, a / (Kc + 1)


# --- formes closes : classe M sous la loi de référence ---
def _pmf_comptes(decalages_cases, q: float, u: float) -> np.ndarray:
    """Loi du nombre de cases ≥ u parmi des cases N(δ, 1) indépendantes (δ = 0 : probabilité q)."""
    d = np.ravel(np.asarray(decalages_cases, dtype=float))
    n_zero = int(np.count_nonzero(d == 0.0))
    pmf = stats.binom.pmf(np.arange(n_zero + 1), n_zero, q)
    for p in stats.norm.sf(u - d[d != 0.0]):
        pmf = np.convolve(pmf, [1.0 - p, p])
    return pmf


def _cdf_max_unites(unites, q: float, u: float, taille: int) -> np.ndarray:
    """Répartition du max des comptes d'unités indépendantes (lignes d'un tableau de décalages)."""
    log_cdf = np.zeros(taille + 1)
    for d in unites:
        cdf = np.ones(taille + 1)
        c = np.cumsum(_pmf_comptes(d, q, u))
        cdf[: c.size] = np.minimum(c, 1.0)
        with np.errstate(divide="ignore"):
            log_cdf += np.log(cdf)
    return np.exp(log_cdf)


def puissances_decalage(D, q: float, alpha: float, seuils: dict) -> dict[str, float]:
    """Puissances exactes, sous la loi de référence, quand l'essaim reçoit le décalage déterministe D (K, T).
    Les attaques de la grille tirent leurs positions uniformément : la loi de référence étant invariante par
    relabellisation des agents et des pas, la puissance est celle d'un motif canonique."""
    D = np.asarray(D, dtype=float)
    K, T = D.shape
    n0 = K * T
    u = seuil_par_case(q)
    lc = stats.norm.logcdf
    sortie = {
        "somme": float(stats.norm.sf((seuils["somme"][0] - D.sum()) / math.sqrt(n0))),
        "max": float(-np.expm1(lc(seuils["max"][0] - D).sum())),
        "agent_moyenne": float(-np.expm1(lc(seuils["agent_moyenne"][0] - D.sum(axis=1) / math.sqrt(T)).sum())),
        "pas_moyenne": float(-np.expm1(lc(seuils["pas_moyenne"][0] - D.sum(axis=0) / math.sqrt(K)).sum())),
        "comptage": taux_discret(np.cumsum(_pmf_comptes(D, q, u)), seuils["comptage"]),
        "agent_comptage": taux_discret(_cdf_max_unites(D, q, u, T), seuils["agent_comptage"]),
        "coelev_comptage": taux_discret(_cdf_max_unites(D.T, q, u, K), seuils["coelev_comptage"]),
    }
    return sortie


def motif(genre: str, K: int, T: int, B: float, m: int) -> np.ndarray:
    """Motif canonique d'un décalage de classe M (positions sans importance sous la loi de référence)."""
    D = np.zeros((K, T))
    if genre == "concentre":
        D[0, 0] = B
    elif genre in ("synchro", "synchro_un"):
        if genre == "synchro_un":
            D[0, 0] = B
        else:
            D[:m, 0] = B / m
    elif genre == "temps":
        D[0, :m] = B / m
    else:
        raise GardeArret(f"motif {genre!r} inconnu")
    return D


def borne_synchro(K: int, T: int, m: int, q: float, seuil) -> float:
    """Borne inférieure exacte de la puissance de la co-élévation (comptage) sous synchronisation de m
    agents au même pas (r = 1) : au pas commun, les m agents synchronisés portent leur maximum
    (au-dessus de u avec la probabilité 1 − (1 − q)^T, indépendamment) et les K − m autres leur score
    honnête ; le max sur les pas majore le compte de ce pas."""
    p_max = 1.0 - (1.0 - q) ** T
    pmf = np.convolve(stats.binom.pmf(np.arange(m + 1), m, p_max),
                      stats.binom.pmf(np.arange(K - m + 1), K - m, q))
    return taux_discret(np.cumsum(pmf), seuil)


# --- formes closes : seuils de référence sous effet d'épisode et sous équicorrélation ---
def _gh():
    x, w = np.polynomial.hermite_e.hermegauss(NOEUDS_GH)
    return x, w / math.sqrt(2.0 * math.pi)


def _esperance(f) -> float:
    x, w = _gh()
    return float(sum(wk * f(xk) for xk, wk in zip(x, w)))


def fausses_alarmes_reference(loi: dict, K: int, T: int, q: float, alpha: float, seuils: dict) -> dict[str, float]:
    """Taux de fausses alarmes exacts des seuils de référence (cases supposées iid) sous la loi donnée.
    Lois : iid (α par construction), effet_episode τ, equicorrelation c. Clés absentes : pas de forme close."""
    t = loi["type"]
    n0 = K * T
    u = seuil_par_case(q)
    z = stats.norm
    cs, cm, ca, cp = (seuils[k][0] for k in ("somme", "max", "agent_moyenne", "pas_moyenne"))
    if t == "iid":
        return {k: alpha for k in seuils}
    if t == "effet_episode":
        tau = float(loi["tau"])
        s = math.sqrt(1.0 - tau * tau)

        def qu(x):
            return z.sf((u - tau * x) / s)

        return {
            "somme": float(z.sf((cs / math.sqrt(n0)) / math.sqrt(n0 * tau * tau + 1.0 - tau * tau))),
            "max": 1.0 - _esperance(lambda x: math.exp(n0 * z.logcdf((cm - tau * x) / s))),
            "agent_moyenne": 1.0 - _esperance(lambda x: math.exp(K * z.logcdf((ca - math.sqrt(T) * tau * x) / s))),
            "pas_moyenne": 1.0 - _esperance(lambda x: math.exp(T * z.logcdf((cp - math.sqrt(K) * tau * x) / s))),
            "comptage": _esperance(lambda x: taux_discret(cdf_binom(n0, qu(x)), seuils["comptage"])),
            "agent_comptage": _esperance(lambda x: taux_discret(cdf_binom(T, qu(x)) ** K, seuils["agent_comptage"])),
            "coelev_comptage": _esperance(lambda x: taux_discret(cdf_binom(K, qu(x)) ** T, seuils["coelev_comptage"])),
        }
    if t == "equicorrelation":
        c = float(loi["c"])
        s = math.sqrt(1.0 - c)
        v = 1.0 + (K - 1) * c
        x, w = _gh()
        pmf_pas = sum(wk * stats.binom.pmf(np.arange(K + 1), K, z.sf((u - math.sqrt(c) * xk) / s))
                      for xk, wk in zip(x, w))
        pmf_pas = pmf_pas / pmf_pas.sum()
        pmf_total = np.array([1.0])
        for _ in range(T):
            pmf_total = np.convolve(pmf_total, pmf_pas)
        cdf_pas = np.minimum(np.cumsum(pmf_pas), 1.0)
        return {
            "somme": float(z.sf((cs / math.sqrt(n0)) / math.sqrt(v))),
            "max": 1.0 - _esperance(lambda xx: math.exp(K * z.logcdf((cm - math.sqrt(c) * xx) / s))) ** T,
            "agent_moyenne": 1.0 - _esperance(lambda xx: math.exp(K * z.logcdf((ca - math.sqrt(c) * xx) / s))),
            "pas_moyenne": float(-math.expm1(T * z.logcdf(cp / math.sqrt(v)))),
            "comptage": taux_discret(np.minimum(np.cumsum(pmf_total), 1.0), seuils["comptage"]),
            "coelev_comptage": taux_discret(cdf_pas ** T, seuils["coelev_comptage"]),
        }
    raise GardeArret(f"loi {t!r} sans forme close")


def rho_e_pas(K: int, T: int, alpha: float) -> float:
    """ρ* du processus e unilatéral : minimiseur de la frontière d'alarme à l'horizon n₀ = K T (note v3, section 2)."""
    return cal03.rho_optimal(K * T, alpha, "unilateral")[0]

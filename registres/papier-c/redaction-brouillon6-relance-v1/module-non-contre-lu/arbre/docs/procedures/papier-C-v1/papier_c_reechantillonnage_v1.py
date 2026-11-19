"""Papier C — rééchantillonnage par grappes, intervalles, valeurs p, corrections, Clopper-Pearson (v1).

Texte de référence : version r1 (`e12f16fa…`), section « Métrique », points 11, 12 et 15 ; section « Seuil ».
Fonctions pures : des tableaux en entrée, des nombres en sortie. Aucune lecture de fichier, aucun modèle.

Convention des poids. Toute statistique du module s'écrit comme une fonction de moments pondérés des unités
(contenus, tâches, items). Un jeu de poids est un tableau (R, n) : R = 1 et des poids égaux à 1 pour la valeur
observée ; R = B lignes de comptes multinomiaux par grappes pour le rééchantillonnage (point 11 : « avec remise,
10 000 tirages, par grappes ») ; R = G lignes où une grappe est mise à zéro pour le jackknife (point 11 :
« accélération par jackknife sur les grappes »). La même fonction rend donc la valeur observée, les tirages et le
jackknife, et « mêmes tirages pour toutes les statistiques d'un corpus » (point 11) se tient en passant le même
tableau de comptes à toutes les statistiques du corpus.

Aucune dépendance hors de numpy et de la bibliothèque standard : la loi bêta à arguments non entiers (point 15) et la
loi normale sont écrites ici, pour que les essais tournent sans autre bibliothèque ; l'essai
`test_beta_contre_scipy_si_present` les compare à scipy quand il est installé.
"""
from __future__ import annotations

import math
from statistics import NormalDist

import numpy as np

from papier_c_erreurs_v1 import ConfigurationInvalide

_NORMALE = NormalDist()


# ------------------------------------------------------------------------------------------------------------------
# Poids : observé, tirages par grappes, jackknife sur les grappes
# ------------------------------------------------------------------------------------------------------------------
def _grappes(grappes) -> tuple[np.ndarray, int]:
    g = np.asarray(grappes)
    if g.ndim != 1 or g.size == 0:
        raise ConfigurationInvalide("grappes : un vecteur non vide d'étiquettes attendu")
    _, inverse = np.unique(g, return_inverse=True)
    return inverse, int(inverse.max()) + 1


def poids_observes(n: int) -> np.ndarray:
    return np.ones((1, int(n)))


def comptes_par_grappes(grappes, tirages: int, rng: np.random.Generator) -> np.ndarray:
    """Tableau (tirages, n) : nombre de fois où la grappe de chaque unité est tirée, G grappes tirées avec remise
    parmi les G (point 11). Une tâche porte ses contenus de toutes les cellules : ses unités reçoivent le même compte."""
    if tirages < 1:
        raise ConfigurationInvalide("nombre de tirages < 1")
    inverse, G = _grappes(grappes)
    comptes = rng.multinomial(G, np.full(G, 1.0 / G), size=int(tirages)).astype(np.float64)
    return comptes[:, inverse]


def poids_jackknife(grappes) -> np.ndarray:
    """Tableau (G, n) : la ligne g met à zéro les unités de la grappe g, les autres valent 1."""
    inverse, G = _grappes(grappes)
    return (inverse[None, :] != np.arange(G)[:, None]).astype(np.float64)


# ------------------------------------------------------------------------------------------------------------------
# Intervalles : percentiles ; percentiles corrigés du biais et de l'asymétrie (BCa), repli consigné
# ------------------------------------------------------------------------------------------------------------------
def intervalle_percentiles(tirages, niveau: float) -> tuple[float, float, int]:
    """(borne basse, borne haute, nombre de tirages non finis écartés). Quantiles de numpy, interpolation linéaire."""
    t = np.asarray(tirages, dtype=np.float64)
    finis = t[np.isfinite(t)]
    if finis.size == 0:
        return float("nan"), float("nan"), int(t.size)
    alpha = (1.0 - float(niveau)) / 2.0
    bas, haut = np.quantile(finis, [alpha, 1.0 - alpha])
    return float(bas), float(haut), int(t.size - finis.size)


def intervalle_bca(observe: float, tirages, jackknife, niveau: float) -> dict:
    """Intervalle bilatéral au niveau donné, par percentiles corrigés du biais et de l'asymétrie (point 11).

    Rend {bas, haut, methode, motif, non_finis}. `methode` vaut « BCa », ou « percentiles » quand le BCa n'est pas
    défini ; le motif est alors écrit (point 11 : « intervalle par percentiles, consigné avec la statistique »).
    Cas nommés par le texte : tirages tous égaux ; jackknife de variance nulle. Cas de fait, hors du texte (point
    ouvert PO-07) : tous les tirages du même côté de la valeur observée (correction du biais infinie), jackknife ou
    valeur observée non finis, dénominateur de la correction nul ou négatif. Aucun n'est traité en silence : le
    motif est rendu."""
    t = np.asarray(tirages, dtype=np.float64)
    bas_p, haut_p, non_finis = intervalle_percentiles(t, niveau)
    sortie = {"bas": bas_p, "haut": haut_p, "methode": "percentiles", "motif": None, "non_finis": non_finis}
    finis = t[np.isfinite(t)]
    j = np.asarray(jackknife, dtype=np.float64)
    if finis.size == 0:
        sortie["motif"] = "aucun tirage fini"
        return sortie
    if not math.isfinite(observe):
        sortie["motif"] = "valeur observée non finie"
        return sortie
    if np.all(finis == finis[0]):
        sortie["motif"] = "tirages tous égaux"
        return sortie
    if j.size < 2 or not np.all(np.isfinite(j)):
        sortie["motif"] = "jackknife non fini"
        return sortie
    ecarts = j.mean() - j
    somme2 = float(np.sum(ecarts ** 2))
    if somme2 <= 0.0:
        sortie["motif"] = "jackknife de variance nulle"
        return sortie
    part = float(np.mean(finis < observe))
    if part <= 0.0 or part >= 1.0:
        sortie["motif"] = "tirages tous du même côté de la valeur observée"
        return sortie
    z0 = _NORMALE.inv_cdf(part)
    acceleration = float(np.sum(ecarts ** 3)) / (6.0 * somme2 ** 1.5)
    alpha = (1.0 - float(niveau)) / 2.0
    bornes = []
    for a in (alpha, 1.0 - alpha):
        z = z0 + _NORMALE.inv_cdf(a)
        denominateur = 1.0 - acceleration * z
        if denominateur <= 0.0:
            sortie["motif"] = "dénominateur de la correction d'asymétrie nul ou négatif"
            return sortie
        bornes.append(_NORMALE.cdf(z0 + z / denominateur))
    bas, haut = np.quantile(finis, bornes)
    return {"bas": float(bas), "haut": float(haut), "methode": "BCa", "motif": None, "non_finis": non_finis,
            "z0": z0, "acceleration": acceleration}


def niveau_bonferroni(alpha: float, m: int) -> float:
    """Niveau 1 − alpha / m (section « Seuil » : « niveaux 1 − 0,10/m et 1 − 0,05/m »)."""
    if m < 1:
        raise ConfigurationInvalide("correction de Bonferroni sur moins d'une comparaison")
    return 1.0 - float(alpha) / int(m)


# ------------------------------------------------------------------------------------------------------------------
# Valeurs p par décompte (point 12) et corrections
# ------------------------------------------------------------------------------------------------------------------
def p_superieur(tirages, theta0: float) -> float:
    """p(θ > θ₀) = (1 + #{θ* ≤ θ₀}) / (B + 1) : valeur p qui conclut θ > θ₀ (nul θ ≤ θ₀). B est le nombre de tirages
    reçus ; un tirage non défini (NaN) n'est pas compté au numérateur (lecture littérale ; point ouvert PO-08)."""
    t = np.asarray(tirages, dtype=np.float64)
    return float((1 + int(np.sum(t <= theta0))) / (t.size + 1))


def p_inferieur(tirages, theta0: float) -> float:
    """p(θ < θ₀) = (1 + #{θ* ≥ θ₀}) / (B + 1) (« et symétriquement », point 12)."""
    t = np.asarray(tirages, dtype=np.float64)
    return float((1 + int(np.sum(t >= theta0))) / (t.size + 1))


def p_bilateral(tirages, theta0: float = 0.0) -> float:
    """min(1, 2 · min des deux unilatéraux) (point 12, « Structure »)."""
    return float(min(1.0, 2.0 * min(p_superieur(tirages, theta0), p_inferieur(tirages, theta0))))


def p_depassement(tirages_centres, observe: float) -> float:
    """(1 + #{T* ≥ T}) / (B + 1) : valeur p par rééchantillonnage centré (bloc de la stabilité de rang)."""
    t = np.asarray(tirages_centres, dtype=np.float64)
    return float((1 + int(np.sum(t >= observe - 1e-12))) / (t.size + 1))


def holm(valeurs_p) -> list[float]:
    """Valeurs p ajustées par la méthode de Holm, dans l'ordre reçu."""
    p = [float(x) for x in valeurs_p]
    m = len(p)
    ordre = sorted(range(m), key=lambda i: p[i])
    ajustees, courant = [0.0] * m, 0.0
    for rang, i in enumerate(ordre):
        courant = max(courant, min(1.0, (m - rang) * p[i]))
        ajustees[i] = courant
    return ajustees


# ------------------------------------------------------------------------------------------------------------------
# Loi bêta à arguments non entiers, Clopper-Pearson à l'effectif efficace (point 15)
# ------------------------------------------------------------------------------------------------------------------
def _fraction_continue_beta(a: float, b: float, x: float) -> float:
    minuscule = 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) > minuscule else minuscule)
    h = d
    for m in range(1, 10_000):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > minuscule else minuscule)
        c = 1.0 + aa / c
        c = c if abs(c) > minuscule else minuscule
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > minuscule else minuscule)
        c = 1.0 + aa / c
        c = c if abs(c) > minuscule else minuscule
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < 1e-15:
            return h
    raise ConfigurationInvalide(f"loi bêta : fraction continue non convergée (a = {a}, b = {b}, x = {x})")


def beta_repartition(x: float, a: float, b: float) -> float:
    """Fonction de répartition de la loi bêta(a, b) en x (fonction bêta incomplète régularisée)."""
    if a <= 0 or b <= 0:
        raise ConfigurationInvalide("loi bêta : arguments strictement positifs attendus")
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    log_facteur = (math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log1p(-x))
    if x < (a + 1.0) / (a + b + 2.0):
        return math.exp(log_facteur) * _fraction_continue_beta(a, b, x) / a
    return 1.0 - math.exp(log_facteur) * _fraction_continue_beta(b, a, 1.0 - x) / b


def beta_quantile(q: float, a: float, b: float) -> float:
    """Quantile d'ordre q de la loi bêta(a, b), par dichotomie (200 pas : précision de la machine)."""
    if not 0.0 <= q <= 1.0:
        raise ConfigurationInvalide("quantile hors de [0 ; 1]")
    bas, haut = 0.0, 1.0
    for _ in range(200):
        milieu = 0.5 * (bas + haut)
        if beta_repartition(milieu, a, b) < q:
            bas = milieu
        else:
            haut = milieu
    return 0.5 * (bas + haut)


def clopper_pearson(x: float, n: float, niveau: float = 0.95) -> tuple[float, float]:
    """Intervalle de Clopper-Pearson bilatéral, x et n pouvant être non entiers (effectif efficace, point 15)."""
    if n <= 0 or x < 0 or x > n:
        raise ConfigurationInvalide(f"Clopper-Pearson : x = {x}, n = {n}")
    alpha = (1.0 - float(niveau)) / 2.0
    bas = 0.0 if x <= 0 else beta_quantile(alpha, x, n - x + 1.0)
    haut = 1.0 if x >= n else beta_quantile(1.0 - alpha, x + 1.0, n - x)
    return bas, haut


def effectif_efficace(detections_par_tache, essais_par_tache) -> dict:
    """Effet de plan sur les totaux par tâche (point 15) :
    e = [(T/(T − 1)) Σ_t (x_t − p̂ N_t)² / N_o²] / [p̂ (1 − p̂) / N_o] ; N_eff = N_o / max(1, e) ; x_eff = p̂ N_eff.
    « Si p̂ vaut 0 ou 1, e n'est pas défini : e = 1 (N_eff = N_o), écrit tel quel. »"""
    x = np.asarray(detections_par_tache, dtype=np.float64)
    N = np.asarray(essais_par_tache, dtype=np.float64)
    if x.shape != N.shape or x.ndim != 1 or x.size < 2 or np.any(N <= 0) or np.any(x < 0) or np.any(x > N):
        raise ConfigurationInvalide("effectif efficace : détections et essais par tâche incohérents (au moins 2 tâches)")
    T, N_o = x.size, float(N.sum())
    p = float(x.sum()) / N_o
    if p <= 0.0 or p >= 1.0:
        e, defini = 1.0, False
    else:
        e = ((T / (T - 1.0)) * float(np.sum((x - p * N) ** 2)) / N_o ** 2) / (p * (1.0 - p) / N_o)
        defini = True
    n_eff = N_o / max(1.0, e)
    return {"taux": p, "essais": N_o, "detections": float(x.sum()), "effet_de_plan": e,
            "effet_de_plan_defini": defini, "effectif_efficace": n_eff, "detections_efficaces": p * n_eff}


__all__ = ["poids_observes", "comptes_par_grappes", "poids_jackknife", "intervalle_percentiles", "intervalle_bca",
           "niveau_bonferroni", "p_superieur", "p_inferieur", "p_bilateral", "p_depassement", "holm",
           "beta_repartition", "beta_quantile", "clopper_pearson", "effectif_efficace"]

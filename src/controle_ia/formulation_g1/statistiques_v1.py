"""Statistiques de l'étude des formulations du contraste à témoin apparié (porte de fin de phase 1, G1) — v1.

Tout est vectorisé sur les répétitions de Monte-Carlo : un tableau `d` de forme (répétitions, tâches) porte une
différence appariée par tâche, bornée dans [-1, 1].

- `seuils` : seuil de calibrage à un taux de faux positifs donné, convention écrite au préenregistrement
  (le j-ième plus grand score de calibrage, j = partie entière de taux × n ; alerte si score strictement supérieur ;
  taux d'alerte attendu sur un épisode neuf de même loi : j / (n + 1)).
- `borne_haute_clopper_pearson`, `alertes_tolerees`, `passage_garde_exact` : la garde B1 et sa valeur exacte.
- `pari_apparie_borne` : test unilatéral par pari sur des différences bornées (capital de Ville, mise prévisible),
  mise en œuvre du rédacteur d'après Waudby-Smith et Ramdas (« Estimating means of bounded random variables by
  betting ») ; ce n'est PAS une copie de la conception du pari du programme, que le rédacteur n'a pas lue.
- `student_apparie` : seconde lecture, modèle hiérarchique à effet aléatoire de tâche en plan équilibré, qui se
  réduit au test de Student apparié sur les moyennes par tâche.
- `indices_blocs`, `moyennes_reechantillonnees` : rééchantillonnage par blocs de tâches.
"""
from __future__ import annotations

import math

import numpy as np
from scipy import stats

from ..gardes import GardeArret

PLAFOND_GARDE = 0.05      # B1 : borne haute du taux d'alerte sur le témoin strictement sous 5 %
NIVEAU_GARDE = 0.95       # B1 : Clopper-Pearson unilatéral à 95 %
TOLERANCE_BORNE = 1e-12


def rang_de_seuil(n: int, taux: float) -> int:
    """Rang j du score de calibrage qui sert de seuil. Garde : j < 1 = calibrage impossible à ce taux."""
    if not (0.0 < taux < 1.0):
        raise GardeArret(f"taux de calibrage {taux!r} hors de ]0, 1[")
    j = int(math.floor(taux * n + 1e-9))
    if j < 1:
        raise GardeArret(f"calibrage impossible : {n} épisodes ne fixent aucun seuil au taux {taux} (il en faut {math.ceil(1 / taux)})")
    return j


def seuils(x: np.ndarray, taux: float) -> np.ndarray:
    """x : (répétitions, n) scores de calibrage → (répétitions,) seuils ; alerte si score > seuil."""
    if x.ndim != 2:
        raise GardeArret(f"scores de calibrage de forme {x.shape} : (répétitions, épisodes) attendu")
    n = x.shape[1]
    j = rang_de_seuil(n, taux)
    return np.partition(x, n - j, axis=1)[:, n - j]


def borne_haute_clopper_pearson(x, n: int, niveau: float = NIVEAU_GARDE):
    """Borne haute unilatérale exacte du taux pour x alertes sur n épisodes indépendants."""
    x = np.asarray(x)
    if np.any(x < 0) or np.any(x > n) or n < 1:
        raise GardeArret(f"compte d'alertes hors de [0, {n}]")
    borne = stats.beta.ppf(niveau, x + 1, np.maximum(n - x, 1e-300))
    return np.where(x >= n, 1.0, borne)


def alertes_tolerees(n: int, plafond: float = PLAFOND_GARDE, niveau: float = NIVEAU_GARDE) -> int:
    """Plus grand nombre d'alertes dont la borne haute reste strictement sous le plafond ; -1 si aucun."""
    k = np.arange(0, n + 1)
    passe = borne_haute_clopper_pearson(k, n, niveau) < plafond
    if not passe[0]:
        return -1
    return int(np.max(np.nonzero(passe)[0]))


def passage_garde_exact(n: int, taux_vrai: float, plafond: float = PLAFOND_GARDE, niveau: float = NIVEAU_GARDE) -> float:
    """Probabilité exacte de passer B1 quand les n épisodes sont indépendants et sonnent au taux vrai donné."""
    k = alertes_tolerees(n, plafond, niveau)
    return 0.0 if k < 0 else float(stats.binom.cdf(k, n, taux_vrai))


def conjonction_independante(probabilites) -> float:
    """Risque exact d'un test de conjonction (intersection-union) dont les composantes sont indépendantes."""
    p = np.asarray(list(probabilites), dtype=float)
    if p.size == 0 or np.any(p < 0) or np.any(p > 1):
        raise GardeArret(f"probabilités de composantes invalides : {p}")
    return float(np.prod(p))


def rappel_vrai(effet: float, taux: float) -> float:
    """Rappel d'un moniteur gaussien d'écart-type 1 décalé de `effet`, au seuil exact de taux de faux positifs `taux`."""
    return float(stats.norm.sf(stats.norm.isf(taux) - effet))


def exiger_bornee(d: np.ndarray) -> None:
    if d.ndim != 2 or d.shape[1] < 2:
        raise GardeArret(f"différences appariées de forme {d.shape} : (répétitions, au moins 2 tâches) attendu")
    if not np.all(np.isfinite(d)):
        raise GardeArret("différences appariées non finies")
    if d.min() < -1.0 - TOLERANCE_BORNE or d.max() > 1.0 + TOLERANCE_BORNE:
        raise GardeArret(f"différences appariées hors de [-1, 1] : [{d.min()}, {d.max()}] ; le pari borné ne s'applique pas")


def exiger_niveau(alpha: float) -> None:
    if not (0.0 < alpha < 0.5):
        raise GardeArret(f"niveau {alpha!r} hors de ]0, 0,5[")


def pari_apparie_borne(d: np.ndarray, alpha: float, plafond_mise: float = 0.75) -> np.ndarray:
    """Rejette « moyenne de d ≤ 0 » si le capital du pari atteint 1/alpha à une tâche quelconque (ordre des tâches fixe).

    x = (d + 1) / 2 dans [0, 1] ; nul : moyenne ≤ 1/2 ; capital K_t = produit de (1 + mise_s (x_s - 1/2)) ;
    mise_s ≥ 0, prévisible, min( racine(2 ln(1/alpha) / (variance_{s-1} · s · ln(s + 1))), 2 · plafond_mise ).
    """
    exiger_bornee(d)
    exiger_niveau(alpha)
    x = (d + 1.0) / 2.0
    repetitions, taches = x.shape
    somme = np.full(repetitions, 0.5)
    carres = np.full(repetitions, 0.25)
    log_capital = np.zeros(repetitions)
    log_max = np.zeros(repetitions)
    cible = math.log(1.0 / alpha)
    for t in range(1, taches + 1):
        variance = carres / t
        mise = np.minimum(np.sqrt(2.0 * cible / (variance * t * math.log(t + 1.0))), 2.0 * plafond_mise)
        xt = x[:, t - 1]
        log_capital += np.log1p(mise * (xt - 0.5))
        np.maximum(log_max, log_capital, out=log_max)
        somme += xt
        carres += (xt - somme / (t + 1.0)) ** 2
    return log_max >= cible


def student_apparie(d: np.ndarray, alpha: float) -> np.ndarray:
    """Seconde lecture : test de Student apparié unilatéral sur les moyennes par tâche (effet aléatoire de tâche)."""
    exiger_bornee(d)
    exiger_niveau(alpha)
    taches = d.shape[1]
    moyenne = d.mean(axis=1)
    ecart = d.std(axis=1, ddof=1)
    quantile = stats.t.ppf(1.0 - alpha, taches - 1)
    with np.errstate(divide="ignore", invalid="ignore"):
        stat = moyenne / (ecart / math.sqrt(taches))
    return np.where(ecart > 0, stat > quantile, moyenne > 0)


def borne_haute_par_taches(taux_par_tache: np.ndarray, niveau: float = NIVEAU_GARDE) -> np.ndarray:
    """Seconde lecture de B1 : borne haute de Student de la moyenne des taux d'alerte par tâche."""
    if taux_par_tache.ndim != 2 or taux_par_tache.shape[1] < 2:
        raise GardeArret(f"taux par tâche de forme {taux_par_tache.shape}")
    taches = taux_par_tache.shape[1]
    moyenne = taux_par_tache.mean(axis=1)
    ecart = taux_par_tache.std(axis=1, ddof=1)
    return moyenne + stats.t.ppf(niveau, taches - 1) * ecart / math.sqrt(taches)


def indices_blocs(rng: np.random.Generator, repetitions: int, tirages: int, taches: int) -> np.ndarray:
    """Indices de tâches tirés avec remise : (répétitions, tirages, tâches)."""
    if tirages < 100:
        raise GardeArret(f"{tirages} tirages de rééchantillonnage : au moins 100 exigés")
    return rng.integers(0, taches, size=(repetitions, tirages, taches), dtype=np.int32)


def moyennes_reechantillonnees(v: np.ndarray, indices: np.ndarray) -> np.ndarray:
    """v : (répétitions, tâches) ; indices : (répétitions, tirages, tâches) → moyennes (répétitions, tirages)."""
    if v.shape[0] != indices.shape[0] or v.shape[1] != indices.shape[2]:
        raise GardeArret(f"formes incompatibles : valeurs {v.shape}, indices {indices.shape}")
    return np.take_along_axis(np.broadcast_to(v[:, None, :], indices.shape), indices, axis=2).mean(axis=2)

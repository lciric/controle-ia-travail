"""Estimateurs et intervalles (section « Métrique ») et règle du tirage de confirmation (C1, C4).

- Taux : intervalle binomial exact à 95 %, bilatéral (Clopper et Pearson), par inversion de la loi binomiale, sans bibliothèque
  de statistique (dichotomie à 60 pas, comme le calcul des ordres de grandeur v2).
- Moyenne, rapport, part : 2 000 rééchantillons des sources, percentiles, graine dérivée par tâche.
- Confirmation : case retirée si plus de 500 rejets sur 10 000 ; en échec si le tirage de confirmation (100 000) compte au moins
  le plus petit compte dont la borne basse de l'intervalle exact bilatéral de niveau 1 − 0,05/72 dépasse 0,05 (5 236).
"""

import math

import numpy as np

from .constantes import (CASES_C1, COMPTE_D_ECHEC_DE_CONFIRMATION, REECHANTILLONS, SEUIL_DE_RETRAIT_SUR_10000,
                         TIRAGES_CONFIRMATION, TIRAGES_PAR_CASE)


class Binomiale:
    def __init__(self, n):
        self.n = n
        logfact = np.concatenate(([0.0], np.cumsum(np.log(np.arange(1, n + 1, dtype=np.float64)))))
        self.indices = np.arange(0, n + 1, dtype=np.float64)
        self.logcomb = logfact[n] - logfact - logfact[::-1]

    def pmf(self, p):
        return np.exp(self.logcomb + self.indices * math.log(p) + (self.n - self.indices) * math.log1p(-p))

    def cdf(self, k, p):
        return float(min(1.0, self.pmf(p)[: k + 1].sum()))

    def queue_haute(self, k, p):
        return float(min(1.0, self.pmf(p)[k:].sum()))

    def clopper_pearson(self, k, niveau=0.95, arrondi=None):
        a = (1.0 - niveau) / 2.0
        if k == 0:
            bas = 0.0
        else:
            lo, hi = 1e-12, 1.0 - 1e-12
            for _ in range(60):
                m = (lo + hi) / 2.0
                if 1.0 - self.cdf(k - 1, m) < a:
                    lo = m
                else:
                    hi = m
            bas = (lo + hi) / 2.0
        if k == self.n:
            haut = 1.0
        else:
            lo, hi = 1e-12, 1.0 - 1e-12
            for _ in range(60):
                m = (lo + hi) / 2.0
                if self.cdf(k, m) > a:
                    lo = m
                else:
                    hi = m
            haut = (lo + hi) / 2.0
        if arrondi is not None:
            return [round(bas, arrondi), round(haut, arrondi)]
        return [bas, haut]


_CACHE = {}


def binomiale(n):
    if n not in _CACHE:
        _CACHE[n] = Binomiale(n)
    return _CACHE[n]


def clopper_pearson(k, n, niveau=0.95, arrondi=None):
    return binomiale(n).clopper_pearson(k, niveau, arrondi)


def plus_petit_compte_d_echec(nombre_de_cases=CASES_C1, n=TIRAGES_CONFIRMATION, niveau_nul=0.05):
    """Plus petit k tel que P(X ≥ k | 0,05) < 0,05 / (2 × cases) : la borne basse exacte de niveau 1 − 0,05/cases dépasse 0,05."""
    B = binomiale(n)
    pmf = B.pmf(niveau_nul)
    queue = np.cumsum(pmf[::-1])[::-1]
    return int(np.argmax(queue < 0.05 / (2 * nombre_de_cases)))


def regle_de_confirmation(rejets_sur_10000, rejets_sur_100000=None, tirages=TIRAGES_PAR_CASE):
    """Rend « tenue », « à confirmer » ou « en échec » pour une case de C1 ou de C4 (comptes plantés ou tirés)."""
    if tirages != TIRAGES_PAR_CASE:
        raise ValueError("règle gelée pour 10 000 tirages par case")
    if rejets_sur_10000 <= SEUIL_DE_RETRAIT_SUR_10000:
        return "tenue"
    if rejets_sur_100000 is None:
        return "à confirmer"
    return "en échec" if rejets_sur_100000 >= COMPTE_D_ECHEC_DE_CONFIRMATION else "tenue"


def reechantillonner(valeurs_par_source, statistique, rng, B=REECHANTILLONS):
    """Intervalle à 95 % par rééchantillonnage des sources (percentiles 2,5 et 97,5). `valeurs_par_source` : tableau dont la
    première dimension est la source ; `statistique` : fonction de ce tableau."""
    x = np.asarray(valeurs_par_source)
    n = x.shape[0]
    stats = np.empty(B)
    for b in range(B):
        stats[b] = statistique(x[rng.integers(0, n, n)])
    return [float(np.percentile(stats, 2.5)), float(np.percentile(stats, 97.5))]

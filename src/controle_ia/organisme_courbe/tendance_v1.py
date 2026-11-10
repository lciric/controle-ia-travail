"""Test exact de tendance (Cochran-Armitage conditionnel) et sa puissance — conception de la courbe dose-réponse de la
chaîne complète de l'organisme d'idéation. Aucune donnée.

Réponse binaire par course (une découverte vraie retenue, ou non) ; D doses, n_d courses à la dose d, scores s_d. Sous
le nul « même probabilité à toutes les doses », la loi des succès par dose, sachant leur total, est hypergéométrique
multiple : le test est exact, sans approximation normale. Statistique : T = Σ s_d x_d ; valeur p unilatérale (hausse) :
P(T ≥ t_observé | total).
"""
from __future__ import annotations

import numpy as np
from scipy import special

from ..gardes import GardeArret


class TableTendance:
    """Valeurs p exactes de toutes les issues possibles, pour des tailles et des scores donnés."""

    def __init__(self, n: list[int], scores: list[float]):
        if len(n) != len(scores) or len(n) < 2 or min(n) < 1:
            raise GardeArret("au moins deux doses, une course par dose, autant de scores que de doses")
        self.n = np.asarray(n, dtype=int)
        self.scores = np.asarray(scores, dtype=float)
        if np.ptp(self.scores) == 0:
            raise GardeArret("scores constants : aucune tendance testable")
        grilles = np.meshgrid(*[np.arange(k + 1) for k in self.n], indexing="ij")
        x = np.stack([g.ravel() for g in grilles], axis=1)
        logpoids = special.gammaln(self.n + 1).sum() - (special.gammaln(x + 1) + special.gammaln(self.n - x + 1)).sum(1)
        total = x.sum(1)
        stat = np.round(x @ self.scores, 12)
        p = np.empty(len(x))
        for t in np.unique(total):
            sel = np.flatnonzero(total == t)
            w = np.exp(logpoids[sel] - logpoids[sel].max())
            w /= w.sum()
            ordre = np.argsort(-stat[sel], kind="stable")
            s_trie = stat[sel][ordre]
            queue = np.cumsum(w[ordre])
            # P(T >= t) : somme des poids de toutes les issues dont la statistique est au moins t (ex aequo compris)
            dernier = np.searchsorted(-s_trie, -s_trie, side="right") - 1
            p[sel[ordre]] = queue[dernier]
        self.p = p
        self._base = np.cumprod(np.concatenate([[1], (self.n + 1)[::-1][:-1]]))[::-1]

    def valeur_p(self, succes: np.ndarray) -> np.ndarray:
        """Valeur p exacte (unilatérale, hausse) d'une ou plusieurs issues (tableau ... × D de succès par dose)."""
        succes = np.asarray(succes, dtype=int)
        if (succes < 0).any() or (succes > self.n).any():
            raise GardeArret("succès hors de [0, n_d]")
        return self.p[succes @ self._base]


def puissance(table: TableTendance, probas: list[float], alpha: float, tirages: int,
              rng: np.random.Generator) -> dict:
    """Probabilité de rejeter le nul au niveau alpha (et d'avoir au moins un succès), par simulation, sous les
    probabilités de succès `probas` par dose ; rend aussi la probabilité de « sans dents » (aucun succès)."""
    probas = np.asarray(probas, dtype=float)
    if probas.shape != table.n.shape or (probas < 0).any() or (probas > 1).any():
        raise GardeArret("une probabilité par dose, dans [0, 1]")
    x = rng.binomial(table.n, probas, size=(tirages, len(table.n)))
    p = table.valeur_p(x)
    aucun = x.sum(1) == 0
    return {"rejet": float(((p <= alpha) & ~aucun).mean()), "sans_dents": float(aucun.mean())}


__all__ = ["TableTendance", "puissance"]

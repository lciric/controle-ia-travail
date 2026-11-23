"""Copies fidèles, sans torch, des fonctions réemployées des sondes v0 (défaut 12 de la contre-lecture ; question Q1).

`sondes.familles` importe torch ; `sondes.evaluation` importe `sondes.familles`. La consigne demande « aucun import de
torch » : ce module recopie à l'identique (texte des fonctions extrait par programme des modules sources, au commit de
cette copie) `SondeLineaireJetons`, `_empreinte`, `_verifier_donnees` (de `sondes/familles.py`), `aire_sous_courbe`,
`intervalle_blocs` et `plancher_apparie` (de `sondes/evaluation.py`). Un essai compare leurs sorties, octet pour octet, à
celles des originaux (`tests/test_sondes_v2_reemploi.py`). Les modules sources ne sont pas modifiés (R12).
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass

import numpy as np
from scipy.stats import rankdata

from ..gardes import GardeArret


def _verifier_donnees(sequences, y=None) -> int:
    if not sequences:
        raise GardeArret("aucune action")
    d = None
    for s in sequences:
        s = np.asarray(s)
        if s.ndim != 2 or s.shape[0] < 1:
            raise GardeArret(f"action de forme {s.shape} : (jetons, largeur) attendue, au moins un jeton")
        if d is None:
            d = s.shape[1]
        elif s.shape[1] != d:
            raise GardeArret("largeurs différentes entre actions")
        if not np.all(np.isfinite(s)):
            raise GardeArret("activation non finie")
    if y is not None:
        y = np.asarray(y)
        if y.shape != (len(sequences),) or not set(np.unique(y)) <= {0, 1}:
            raise GardeArret("étiquettes 0/1 attendues, une par action")
        if len(set(y.tolist())) < 2:
            raise GardeArret("les deux classes sont nécessaires à l'entraînement")
    return int(d)


def _empreinte(nom, couche, agregation, *tableaux) -> str:
    h = hashlib.sha256(f"{nom}/{couche}/{agregation}".encode("utf-8"))
    for t in tableaux:
        h.update(np.ascontiguousarray(t, dtype=np.float64).tobytes())
    return h.hexdigest()


@dataclass(frozen=True)
class SondeLineaireJetons:
    """Score w·h + b par jeton ; logits d'attention q·h (si agrégation par attention). Lit les activations brutes."""
    nom: str
    couche: int
    agregation: str
    w: np.ndarray
    b: float
    q: np.ndarray | None = None
    famille: str = "lineaire"

    def scores_par_jeton(self, acts: np.ndarray) -> np.ndarray:
        return np.asarray(acts, dtype=np.float64) @ self.w.astype(np.float64) + float(self.b)

    def logits_attention(self, acts: np.ndarray) -> np.ndarray:
        if self.q is None:
            raise GardeArret(f"sonde {self.nom} : attention sans requête q")
        return np.asarray(acts, dtype=np.float64) @ self.q.astype(np.float64)

    def empreinte(self) -> str:
        t = [self.w, np.array([self.b])] + ([self.q] if self.q is not None else [])
        return _empreinte(f"{self.famille}:{self.nom}", self.couche, self.agregation, *t)


def aire_sous_courbe(scores, y) -> float:
    """Statistique de Mann-Whitney normalisée ; ex aequo comptés pour moitié."""
    scores, y = np.asarray(scores, dtype=np.float64), np.asarray(y)
    if scores.shape != y.shape or scores.ndim != 1:
        raise GardeArret("scores et étiquettes : vecteurs de même longueur attendus")
    if not np.all(np.isfinite(scores)):
        raise GardeArret("score non fini")
    n1, n0 = int((y == 1).sum()), int((y == 0).sum())
    if n1 == 0 or n0 == 0 or n1 + n0 != y.size:
        raise GardeArret("les deux classes 0/1 sont nécessaires")
    r = rankdata(scores)
    return float((r[y == 1].sum() - n1 * (n1 + 1) / 2.0) / (n1 * n0))


def intervalle_blocs(scores, y, blocs, n_tirages: int, graine: int, niveau: float = 0.95) -> dict:
    """Intervalle percentile par rééchantillonnage des blocs (tâches) avec remise. Les tirages où une classe manque
    sont comptés et rapportés ; s'ils dépassent 1 % des tirages, arrêt (aucun repli silencieux)."""
    scores, y, blocs = np.asarray(scores, dtype=np.float64), np.asarray(y), np.asarray(blocs)
    if not (scores.shape == y.shape == blocs.shape):
        raise GardeArret("scores, étiquettes et blocs de même longueur attendus")
    uniques = np.unique(blocs)
    if uniques.size < 2:
        raise GardeArret("au moins deux blocs pour un rééchantillonnage par blocs")
    membres = [np.flatnonzero(blocs == u) for u in uniques]
    rng = np.random.default_rng(int(graine))
    valeurs, degeneres = [], 0
    for _ in range(int(n_tirages)):
        choix = rng.integers(0, uniques.size, size=uniques.size)
        i = np.concatenate([membres[c] for c in choix])
        if len(set(y[i].tolist())) < 2:
            degeneres += 1
            continue
        valeurs.append(aire_sous_courbe(scores[i], y[i]))
    if degeneres > 0.01 * n_tirages:
        raise GardeArret(f"{degeneres} tirages sur {n_tirages} sans les deux classes : blocs trop déséquilibrés")
    a = (1.0 - niveau) / 2.0
    return {"aire": aire_sous_courbe(scores, y), "bas": float(np.quantile(valeurs, a)),
            "haut": float(np.quantile(valeurs, 1.0 - a)), "tirages": len(valeurs), "degeneres": degeneres}


def plancher_apparie(nom: str, couche: int, sequences_entrainement, agregation: str, n_sondes: int,
                     graine: int) -> list[SondeLineaireJetons]:
    """Sondes aléatoires appariées en covariance (recette provisoire, voir l'en-tête du module)."""
    d = _verifier_donnees(sequences_entrainement)
    if agregation not in ("max", "attention"):
        raise GardeArret(f"agrégation {agregation!r} refusée : max ou attention seulement")
    X = np.concatenate([np.asarray(s, dtype=np.float64) for s in sequences_entrainement])
    mu = X.mean(axis=0)
    S = np.cov(X, rowvar=False).reshape(d, d) + 1e-9 * np.eye(d)
    L = np.linalg.cholesky(S)
    rng = np.random.default_rng(int(graine))
    sondes = []
    for k in range(int(n_sondes)):
        w = L @ rng.standard_normal(d)
        q = (L @ rng.standard_normal(d)) if agregation == "attention" else None
        sondes.append(SondeLineaireJetons(f"{nom}-plancher-{k}", couche, agregation, w, float(-w @ mu), q, "plancher"))
    return sondes

"""Pièce 6 — statistique : Z, maximum, p-valeur (spécification, section 3).

- r_i : rang moyen de la sortie du prédicteur j sur le pli d'épreuve.
- Pièce : Z_j = Σ(r_i − r̄)(A_i − π_i) / √Σ(r_i − r̄)² π_i (1 − π_i).
- Lecture : même forme avec les rangs de S_i et la variance de permutation analytique :
  Z_j = Σ(r_i − r̄)(q_i − q̄) / √(Σ(r_i − r̄)² Σ(q_i − q̄)² / (n − 1)).
- Test global unilatéral : M = max_j Z_j.
- Loi sous le nul : exacte par rejeu du tirage (A* par le tireur du harnais, S* par le
  tireur de la lecture substituée), traits fixes ; Z* calculé avec π* ; la permutation
  de S (forme observée) n'est employée que pour la forme observée, déclarée non exacte.
- p = (1 + #{M* ≥ M}) / (B + 1), B = 9 999 par défaut.
- Seuil α = 0,05 par devin et par course.
- Standardisation : la forme analytique seule. Une standardisation sur les tirages
  nuls (moyenne et écart type de Z*) est refusée (`controler_standardisation`).
- Borne basse rapportée : meilleur prédicteur et son seuil choisis sur le pli
  d'apprentissage ; TPR − FPR avec bornes de Clopper-Pearson à 97,5 % de chaque côté ;
  biais au pire possible du taux certifié au moins (1 − p) fois cette borne (fait
  rapporté par la note sur l'attaquant informé, non vérifié sur PDF).
"""
from __future__ import annotations

from typing import Callable, Hashable, Sequence

import numpy as np
from scipy.stats import beta, rankdata

from . import RefusDevin
from .tirage import JournalLecture, JournalTirage, TireurLecture, TireurPiece

ALPHA = 0.05
B_DEFAUT = 9_999


def rangs_centres(sorties: np.ndarray) -> np.ndarray:
    s = np.atleast_2d(np.asarray(sorties, dtype=float))
    if not np.all(np.isfinite(s)):
        raise RefusDevin("sortie de prédicteur non finie")
    r = rankdata(s, axis=1, method="average")
    return r - r.mean(axis=1, keepdims=True)


def _constants(R: np.ndarray) -> np.ndarray:
    """Prédicteurs de sortie constante sur le pli : Z posé à 0 (ils ne départagent rien),
    et nommés dans le résultat (`predicteurs_constants`)."""
    return np.flatnonzero(np.all(R == 0, axis=1))


def z_piece(R: np.ndarray, A: np.ndarray, pi: np.ndarray) -> np.ndarray:
    """R (J, n) rangs centrés ; A et π (n,) ou (B, n). Rend (J,) ou (B, J)."""
    A = np.asarray(A, dtype=float)
    pi = np.asarray(pi, dtype=float)
    un = A.ndim == 1
    A2, pi2 = np.atleast_2d(A), np.atleast_2d(pi)
    constants = _constants(R)
    if np.any((pi2 * (1 - pi2)).sum(axis=1) <= 0):
        raise RefusDevin("propensions toutes dégénérées (0 ou 1) : statistique refusée")
    num = (A2 - pi2) @ R.T
    var = (pi2 * (1 - pi2)) @ (R ** 2).T
    var[:, constants] = 1.0
    if np.any(var <= 0):
        raise RefusDevin("variance nulle pour un prédicteur non constant : statistique refusée")
    z = num / np.sqrt(var)
    z[:, constants] = 0.0
    return z[0] if un else z


def z_lecture(R: np.ndarray, S: np.ndarray) -> np.ndarray:
    S = np.asarray(S, dtype=float)
    un = S.ndim == 1
    q = rankdata(np.atleast_2d(S), axis=1, method="average")
    q = q - q.mean(axis=1, keepdims=True)
    n = R.shape[1]
    constants = _constants(R)
    if np.any((q ** 2).sum(axis=1) <= 0):
        raise RefusDevin("lectures toutes égales : variance de permutation nulle, statistique refusée")
    var = np.outer((q ** 2).sum(axis=1), (R ** 2).sum(axis=1)) / (n - 1)
    var[:, constants] = 1.0
    z = (q @ R.T) / np.sqrt(var)
    z[:, constants] = 0.0
    return z[0] if un else z


def p_valeur(M: float, M_nul: np.ndarray) -> float:
    M_nul = np.asarray(M_nul, dtype=float)
    return float((1 + np.sum(M_nul >= M)) / (M_nul.size + 1))


def _resultat(Z, Znul, B, exact, nature, R):
    M = float(np.max(Z))
    Mnul = Znul.max(axis=1)
    return {"Z": np.asarray(Z), "M": M, "predicteurs_constants": [int(j) for j in _constants(R)], "p": p_valeur(M, Mnul), "B": int(B), "J": int(Z.size),
            "exacte": exact, "nature": nature, "M_nul": Mnul}


def epreuve_globale_piece(sorties: np.ndarray, journal: JournalTirage, tireur: TireurPiece,
                      racine_rejeu: int, B: int = B_DEFAUT) -> dict:
    R = rangs_centres(sorties)
    if R.shape[1] != journal.pieces.size:
        raise RefusDevin("sorties et pièces de longueurs différentes")
    Z = z_piece(R, journal.pieces, journal.propensions)
    A_nul, pi_nul = tireur.rejeu_nul(journal, racine_rejeu, B)
    return _resultat(Z, z_piece(R, A_nul, pi_nul), B, True, "rejeu du tireur de la pièce", R)


def epreuve_globale_lecture(sorties: np.ndarray, journal: JournalLecture, tireur: TireurLecture,
                        racine_rejeu: int, B: int = B_DEFAUT) -> dict:
    R = rangs_centres(sorties)
    if R.shape[1] != journal.lectures.size:
        raise RefusDevin("sorties et lectures de longueurs différentes")
    Z = z_lecture(R, journal.lectures)
    S_nul = tireur.rejeu_nul(journal, racine_rejeu, B)
    return _resultat(Z, z_lecture(R, S_nul), B, True, "rejeu du tireur de la lecture substituée", R)


def forme_observee_lecture(sorties: np.ndarray, lectures: np.ndarray, strates: Sequence[Hashable],
                           graine: np.random.SeedSequence, B: int = B_DEFAUT) -> dict:
    """Lectures vraies, permutation par strates de tâche. Déclarée NON EXACTE."""
    R = rangs_centres(sorties)
    S = np.asarray(lectures, dtype=float)
    strates = np.asarray(strates)
    Z = z_lecture(R, S)
    rng = np.random.default_rng(graine)
    Snul = np.empty((B, S.size))
    for b in range(B):
        x = S.copy()
        for s in np.unique(strates):
            idx = np.flatnonzero(strates == s)
            x[idx] = S[rng.permutation(idx)]
        Snul[b] = x
    r = _resultat(Z, z_lecture(R, Snul), B, False, "permutation par strates (forme observée, non exacte)", R)
    return r


def controler_standardisation(fonction_z: Callable[[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray], np.ndarray],
                              graine: np.random.SeedSequence) -> None:
    """Garde : la statistique employée est la forme analytique de la section 3.

    `fonction_z(R, A, pi, A_nul, pi_nul)` rend Z observé (J,). On la compare à `z_piece`
    sur un cas d'essai ; une standardisation sur les tirages nuls s'en écarte : refus.
    """
    rng = np.random.default_rng(graine)
    n, J, B = 200, 3, 50
    R = rangs_centres(rng.normal(size=(J, n)))
    pi = rng.uniform(0.1, 0.9, n)
    A = (rng.random(n) < pi).astype(float)
    A_nul = (rng.random((B, n)) < pi).astype(float)
    attendu = z_piece(R, A, pi)
    obtenu = np.asarray(fonction_z(R, A, pi, A_nul, np.broadcast_to(pi, (B, n))), dtype=float)
    if obtenu.shape != attendu.shape or not np.allclose(obtenu, attendu, rtol=1e-12, atol=1e-12):
        raise RefusDevin("standardisation différente de la forme analytique (p. ex. sur les tirages nuls) : refus")


def _cp_bas(k, n, niveau=0.975):
    return 0.0 if k == 0 else float(beta.ppf(1 - niveau, k, n - k + 1))


def _cp_haut(k, n, niveau=0.975):
    return 1.0 if k == n else float(beta.ppf(niveau, k + 1, n - k))


def borne_basse(sorties_app: np.ndarray, y_app: np.ndarray, sorties_epr: np.ndarray, y_epr: np.ndarray,
                p: float | None = None) -> dict:
    """Borne basse de la variation totale (TPR − FPR, Clopper-Pearson 97,5 % de chaque côté).

    Prédicteur et seuil choisis sur le pli d'apprentissage (indice de Youden maximal).
    `p` : le p de la formule « (1 − p) fois cette borne » de la section 3 (fait
    rapporté, non vérifié) ; si None, le biais au pire n'est pas rapporté.
    """
    sa, se = np.atleast_2d(sorties_app), np.atleast_2d(sorties_epr)
    ya, ye = np.asarray(y_app).astype(int), np.asarray(y_epr).astype(int)
    for y in (ya, ye):
        if not np.all(np.isin(y, (0, 1))) or y.min() == y.max():
            raise RefusDevin("borne basse : secret binaire à deux valeurs présentes exigé")
    meilleur = (-np.inf, None, None)
    for j in range(sa.shape[0]):
        for s in np.unique(sa[j]):
            pred = sa[j] >= s
            y = pred[ya == 1].mean() - pred[ya == 0].mean()
            if y > meilleur[0]:
                meilleur = (y, j, s)
    _, j, s = meilleur
    pred = se[j] >= s
    P, N = int((ye == 1).sum()), int((ye == 0).sum())
    vp, fp = int(pred[ye == 1].sum()), int(pred[ye == 0].sum())
    borne = _cp_bas(vp, P) - _cp_haut(fp, N)
    r = {"predicteur": int(j), "seuil": float(s), "tpr": vp / P, "fpr": fp / N,
         "borne_basse_vt": float(borne), "borne_basse_vt_tronquee": max(0.0, float(borne))}
    if p is not None:
        r["biais_au_pire_minimal"] = (1 - p) * max(0.0, float(borne))
        r["statut_formule_biais"] = "fait rapporté (note sur l'attaquant informé, d'après « Blindfold »), non vérifié sur PDF"
    return r

"""Sondes, sac de jetons, détecteurs sur neurones et rééchantillonnage du volet A de « Neuron Lens » — v1.

Met en œuvre la section « Métrique » A.1 (sonde, sac de jetons) et A.4 (détecteurs, intervalle apparié) du texte gelé
`docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` (`34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131`).
`scikit-learn` 1.6.1 (version consignée au manifeste de la course).

Lectures déclarées (le texte ne les précise pas) : les plis internes groupés sont **stratifiés** (`StratifiedGroupKFold`, sans
mélange, déterministe) pour que chaque pli contienne les deux classes ; l'écart-type des traits est calculé avec `ddof=0` et une
valeur nulle est remplacée par 1 (trait constant sur l'apprentissage) ; le rééchantillonnage apparié tire, dans chaque découpe, les
exemples de test avec remise **par classe** (les deux classes restent présentes).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy import sparse
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedGroupKFold

GRILLE_C = (1e-4, 1e-3, 1e-2, 1e-1, 1.0, 10.0, 100.0)
BUDGETS = (1, 8, 64, 512)


@dataclass
class Sonde:
    w_std: np.ndarray   # poids sur traits centrés-réduits
    b: float
    mu: np.ndarray
    sigma: np.ndarray
    C: float

    def scores(self, X):
        return ((np.asarray(X, float) - self.mu) / self.sigma) @ self.w_std + self.b


def _choisir_c(X, y, groupes, centrer=True):
    plis = list(StratifiedGroupKFold(n_splits=5).split(X, y, groupes))
    meilleur = None
    for C in GRILLE_C:  # ordre croissant : à égalité, le plus petit C est gardé
        aucs = []
        for a, t in plis:
            if len(set(y[t])) < 2:
                raise ValueError("un pli interne n'a qu'une classe")
            m = LogisticRegression(C=C, solver="lbfgs", max_iter=1000, fit_intercept=True).fit(X[a], y[a])
            aucs.append(roc_auc_score(y[t], m.decision_function(X[t])))
        s = float(np.mean(aucs))
        if meilleur is None or s > meilleur[0]:
            meilleur = (s, C)
    return meilleur[1]


def apprendre_sonde(X, y, groupes) -> Sonde:
    """Régression logistique L2 avec ordonnée à l'origine, `lbfgs`, 1 000 itérations au plus ; C choisi sur la grille par validation
    croisée interne à 5 plis groupés (et stratifiés), critère AUROC moyenne, égalité → plus petit C ; traits centrés-réduits sur
    l'apprentissage."""
    X = np.asarray(X, float)
    y = np.asarray(y)
    mu = X.mean(0)
    sigma = X.std(0)
    sigma[sigma == 0] = 1.0
    Z = (X - mu) / sigma
    C = _choisir_c(Z, y, np.asarray(groupes))
    m = LogisticRegression(C=C, solver="lbfgs", max_iter=1000, fit_intercept=True).fit(Z, y)
    return Sonde(m.coef_[0].copy(), float(m.intercept_[0]), mu, sigma, C)


def comptes_jetons(listes_ids, vocabulaire=None):
    """Matrice creuse des comptes de jetons (texte de l'exemple seulement) ; `vocabulaire` : dict id → colonne (celui de
    l'apprentissage ; les jetons absents sont ignorés)."""
    if vocabulaire is None:
        vocabulaire = {t: j for j, t in enumerate(sorted({t for ids in listes_ids for t in ids}))}
    lignes, cols, vals = [], [], []
    for i, ids in enumerate(listes_ids):
        u, c = np.unique([t for t in ids if t in vocabulaire], return_counts=True)
        lignes += [i] * len(u)
        cols += [vocabulaire[t] for t in u]
        vals += list(c)
    return sparse.csr_matrix((vals, (lignes, cols)), shape=(len(listes_ids), len(vocabulaire)), dtype=float), vocabulaire


@dataclass
class SacDeJetons:
    modele: LogisticRegression
    vocabulaire: dict
    C: float

    def scores(self, listes_ids):
        X, _ = comptes_jetons(listes_ids, self.vocabulaire)
        return self.modele.decision_function(X)

    def poids_par_jeton(self):
        return {t: float(self.modele.coef_[0][j]) for t, j in self.vocabulaire.items()}

    def premiers(self, k=10, tol=1e-8):
        """10 premiers jetons par signe : |poids| décroissant, puis identifiant croissant ; poids de valeur absolue > tol seulement."""
        p = self.poids_par_jeton()
        pos = sorted((t for t, w in p.items() if w > tol), key=lambda t: (-abs(p[t]), t))[:k]
        neg = sorted((t for t, w in p.items() if w < -tol), key=lambda t: (-abs(p[t]), t))[:k]
        return pos, neg


def apprendre_sac(listes_ids, y, groupes) -> SacDeJetons:
    """Même régression, même grille, mêmes plis, sur les comptes bruts (non centrés-réduits) des jetons du texte de l'exemple."""
    X, voc = comptes_jetons(listes_ids)
    y = np.asarray(y)
    C = _choisir_c(X, y, np.asarray(groupes))
    m = LogisticRegression(C=C, solver="lbfgs", max_iter=1000, fit_intercept=True).fit(X, y)
    return SacDeJetons(m, voc, C)


def ecart_moyen_standardise(N, y):
    """|moyenne(classe 1) − moyenne(classe 0)| / écart-type groupé, par neurone (ddof=0 ; écart-type nul → 1)."""
    N = np.asarray(N, float)
    y = np.asarray(y)
    a, b = N[y == 1], N[y == 0]
    s = np.sqrt(((len(a) * a.var(0)) + (len(b) * b.var(0))) / (len(a) + len(b)))
    s[s == 0] = 1.0
    return np.abs(a.mean(0) - b.mean(0)) / s


def detecteurs(N_app, y_app, g_app, N_tests: dict, graine_aleatoire, n_tirages=20):
    """Détecteurs de A-ii sur neurones : pour k ∈ {1, 8, 64, 512}, les k neurones de plus grand écart moyen standardisé, puis sonde ;
    détecteur dense ; k neurones au hasard (20 tirages). `N_tests` : nom du jeu → matrice. Rend {nom: {détecteur: scores}}, avec pour
    les tirages au hasard une liste de 20 vecteurs de scores."""
    rng = np.random.default_rng(graine_aleatoire)
    ems = ecart_moyen_standardise(N_app, y_app)
    ordre = np.argsort(-ems, kind="stable")
    out = {nom: {} for nom in N_tests}
    for k in BUDGETS:
        sel = ordre[:k]
        s = apprendre_sonde(np.asarray(N_app)[:, sel], y_app, g_app)
        for nom, N in N_tests.items():
            out[nom][f"k{k}"] = s.scores(np.asarray(N)[:, sel])
        tir = [rng.choice(N_app.shape[1], size=k, replace=False) for _ in range(n_tirages)]
        sondes = [apprendre_sonde(np.asarray(N_app)[:, t], y_app, g_app) for t in tir]
        for nom, N in N_tests.items():
            out[nom][f"hasard{k}"] = [so.scores(np.asarray(N)[:, t]) for so, t in zip(sondes, tir)]
    s = apprendre_sonde(N_app, y_app, g_app)
    for nom, N in N_tests.items():
        out[nom]["dense"] = s.scores(N)
    return out


def composantes(R_app, y_app, g_app, R_tests: dict, k):
    """Sonde sur les k premières composantes principales de l'apprentissage (budget égal)."""
    pca = PCA(n_components=k, svd_solver="full").fit(R_app)
    s = apprendre_sonde(pca.transform(R_app), y_app, g_app)
    return {nom: s.scores(pca.transform(R)) for nom, R in R_tests.items()}


def borne_basse_appariee(scores_a, scores_b, ys, graine, n=2000, niveau=0.95):
    """Intervalle apparié de l'écart moyen d'AUROC (a − b) sur les découpes : pour chaque tirage, dans chaque découpe, les exemples de test
    sont tirés avec remise par classe ; l'écart d'AUROC est moyenné sur les découpes. Rend (écart observé, borne basse, borne haute)."""
    rng = np.random.default_rng(graine)
    obs = float(np.mean([roc_auc_score(y, a) - roc_auc_score(y, b) for a, b, y in zip(scores_a, scores_b, ys, strict=True)]))
    tirages = np.empty(n)
    for i in range(n):
        ecarts = []
        for a, b, y in zip(scores_a, scores_b, ys):
            y = np.asarray(y)
            idx = np.concatenate([rng.choice(np.flatnonzero(y == c), size=int((y == c).sum()), replace=True) for c in (0, 1)])
            ecarts.append(roc_auc_score(y[idx], np.asarray(a)[idx]) - roc_auc_score(y[idx], np.asarray(b)[idx]))
        tirages[i] = np.mean(ecarts)
    q = (1 - niveau) / 2
    return obs, float(np.quantile(tirages, q)), float(np.quantile(tirages, 1 - q))

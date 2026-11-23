"""Brique B — sondes en forme close, au processeur, version 1 (consigne du développeur des sondes v2, § 2, brique B).

Toutes rendent une `sondes.familles.SondeLineaireJetons` (score par jeton w·h + b, lecture des activations brutes,
agrégation « max ») : le score d'une action est le **maximum** de w·h + b sur ses jetons (`scores_actions`). Aucune
moyenne ni médiane sur les jetons d'une action lue ; la seule exception est `diagnostic_moyenne_jetons`, marquée
« diagnostic » (N-026), jamais appelée par une autre fonction de ce paquet.

Les moyennes de jetons qui **définissent** une direction (moyennes par classe sur les actions d'apprentissage) ne sont
pas des agrégations du score d'une action lue : même convention que `sondes.familles.difference_moyennes`.

1. `difference_moyennes_appariee` : sans paires, w = m₊ − m₋ (moyennes des jetons par classe) ; avec paires (la même
   action lue sous deux jeux de poids, ou sous deux conditions), w = moyenne sur les paires de
   (moyenne des jetons du côté positif − moyenne des jetons du côté négatif), chaque paire pesant autant
   [choix provisoire du développeur, question Q2 à la mère] ; b = −w·(m̄₊ + m̄₋)/2.
2. `difference_moyennes_blanchie` : w = S⁻¹ w₀, w₀ la direction de 1, S = (1 − λ) S_intra + λ (tr S_intra / d) I,
   S_intra la covariance intra-classe des jetons (jetons centrés sur la moyenne de leur classe, dénominateur N − 2),
   λ ∈ {0,9 ; 0,5 ; 0,1}.
3. `logistique_l2` : `sklearn.linear_model.LogisticRegression` à pénalité quadratique (l1_ratio = 0), sur jetons
   réduits (moyenne et écart-type des jetons d'apprentissage, repliés ensuite dans w et b), chaque jeton portant
   l'étiquette de son action, poids 1/n_jetons par action [choix provisoire du développeur, Q3] ; inverse de la
   pénalité C ∈ {0,001 ; 0,01 ; 0,1 ; 1} ; solveur « lbfgs », tolérance 1e-6, 2 000 itérations au plus ; une
   non-convergence arrête (R5).
4. `regression_ridge_honnetes` : régression ridge du jeton d'avant le champ (couche 15) vers log(valeur déclarée),
   apprise sur épisodes honnêtes seulement ; traits centrés-réduits ; forme close (primale si n ≥ d, duale sinon) ;
   alpha ∈ {1000 ; 100 ; 10 ; 1 ; 0,1} [grille : choix provisoire du développeur, Q4]. La sonde rendue prédit
   log(valeur) ; la statistique lue est `residu_ridge` = log(déclarée) − prédiction (« déclaré moins attendu »).

Reproductibilité : tout calcul en double précision, sous `threadpoolctl.threadpool_limits(1)` (une seule tâche de
calcul linéaire, ordre des sommes fixé) : deux exécutions sur la même machine rendent les mêmes octets. Entre deux
machines (autre bibliothèque de calcul linéaire, autre nombre de tâches), l'écart relatif des scores est déclaré sous
`TOLERANCE_ENTRE_MACHINES[famille]` ; l'essai l'éprouve en changeant le nombre de tâches et l'ordre des actions.
"""
from __future__ import annotations

import warnings

import numpy as np
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import LogisticRegression
from threadpoolctl import ThreadpoolController

from ..gardes import GardeArret
from .reemploi_v1 import SondeLineaireJetons, _verifier_donnees

RETRECISSEMENTS = (0.9, 0.5, 0.1)            # ordre de simplicité : le plus rétréci d'abord [Q6, provisoire]
INVERSES_PENALITE = (0.001, 0.01, 0.1, 1.0)  # le plus pénalisé d'abord [Q6, provisoire]
ALPHAS_RIDGE = (1000.0, 100.0, 10.0, 1.0, 0.1)  # le plus pénalisé d'abord [Q4 et Q6, provisoires]
SOLVEUR_LOGISTIQUE = {"solver": "lbfgs", "tol": 1e-6, "max_iter": 2000}
TOLERANCE_ENTRE_MACHINES = {"difference_moyennes_appariee": 1e-9, "difference_moyennes_blanchie": 1e-9,
                            "logistique_l2": 1e-6, "ridge_honnetes": 1e-9}
FAMILLES_JETONS = ("difference_moyennes_appariee", "difference_moyennes_blanchie", "logistique_l2")
REGLAGES = {"difference_moyennes_appariee": (None,), "difference_moyennes_blanchie": RETRECISSEMENTS,
            "logistique_l2": INVERSES_PENALITE, "ridge_honnetes": ALPHAS_RIDGE}


_CONTROLEUR: list = []


def threadpool_limits(n: int = 1):
    """Contexte « n tâches de calcul linéaire », par un contrôleur de threadpoolctl créé une fois (l'inventaire des
    bibliothèques lit /proc/self/maps : coûteux à chaque appel)."""
    if not _CONTROLEUR:
        _CONTROLEUR.append(ThreadpoolController())
    return _CONTROLEUR[0].limit(limits=int(n))


def _f64(sequences):
    return [np.asarray(s, dtype=np.float64) for s in sequences]


def _verifier_paires(paires, y) -> list[tuple[int, int]]:
    n = len(y)
    vues: set[int] = set()
    out = []
    if len(paires) < 1:
        raise GardeArret("paires : au moins une paire")
    for p in paires:
        if len(p) != 2:
            raise GardeArret(f"paire {p!r} : deux indices attendus")
        i, j = int(p[0]), int(p[1])
        if not (0 <= i < n and 0 <= j < n):
            raise GardeArret(f"paire ({i}, {j}) hors des {n} actions")
        if y[i] != 1 or y[j] != 0:
            raise GardeArret(f"paire ({i}, {j}) : (positive, négative) attendue")
        if i in vues or j in vues:
            raise GardeArret(f"paire ({i}, {j}) : une action appartient à deux paires")
        vues.update((i, j))
        out.append((i, j))
    return out


def _moyennes_actions(seqs, indices) -> np.ndarray:
    """Moyenne des jetons de chaque action désignée (définition d'une direction, jamais score d'une action lue)."""
    sel = [seqs[i] for i in indices]
    L = np.array([len(q) for q in sel], dtype=np.float64)
    debuts = np.concatenate([[0], np.cumsum(L[:-1]).astype(np.int64)])
    return np.add.reduceat(np.concatenate(sel), debuts, axis=0) / L[:, None]


def _direction_moyennes(seqs, y, paires):
    if paires is None:
        mp = np.concatenate([s for s, t in zip(seqs, y) if t == 1]).mean(axis=0)
        mn = np.concatenate([s for s, t in zip(seqs, y) if t == 0]).mean(axis=0)
        return mp - mn, mp, mn
    paires = _verifier_paires(paires, y)
    cp = _moyennes_actions(seqs, [i for i, _ in paires])
    cn = _moyennes_actions(seqs, [j for _, j in paires])
    return (cp - cn).mean(axis=0), cp.mean(axis=0), cn.mean(axis=0)


def difference_moyennes_appariee(nom: str, couche: int, sequences, y, paires=None) -> SondeLineaireJetons:
    """Voir l'en-tête (famille 1)."""
    _verifier_donnees(sequences, y)
    y = np.asarray(y)
    with threadpool_limits(1):
        w, mp, mn = _direction_moyennes(_f64(sequences), y, paires)
        if not np.any(w != 0.0):
            raise GardeArret(f"sonde {nom} : direction nulle")
        b = float(-w @ (mp + mn) / 2.0)
    return SondeLineaireJetons(nom, int(couche), "max", w, b, None, "difference_moyennes_appariee")


def covariance_intra(seqs, y) -> np.ndarray:
    """Covariance intra-classe des jetons : jetons centrés sur la moyenne de leur classe, dénominateur N − 2."""
    parts = []
    for c in (0, 1):
        X = np.concatenate([s for s, t in zip(seqs, y) if t == c])
        parts.append(X - X.mean(axis=0))
    Z = np.concatenate(parts)
    if Z.shape[0] < 3:
        raise GardeArret("covariance intra-classe : au moins trois jetons")
    return (Z.T @ Z) / (Z.shape[0] - 2)


def difference_moyennes_blanchie(nom: str, couche: int, sequences, y, retrecissement: float,
                                 paires=None) -> SondeLineaireJetons:
    """Voir l'en-tête (famille 2)."""
    d = _verifier_donnees(sequences, y)
    if retrecissement not in RETRECISSEMENTS:
        raise GardeArret(f"rétrécissement {retrecissement!r} hors de {RETRECISSEMENTS}")
    y = np.asarray(y)
    seqs = _f64(sequences)
    with threadpool_limits(1):
        w0, mp, mn = _direction_moyennes(seqs, y, paires)
        S = covariance_intra(seqs, y)
        lam = float(retrecissement)
        S = (1.0 - lam) * S + lam * (np.trace(S) / d) * np.eye(d)
        if not np.trace(S) > 0.0:
            raise GardeArret(f"sonde {nom} : covariance intra-classe nulle")
        w = np.linalg.solve(S, w0)
        if not np.all(np.isfinite(w)) or not np.any(w != 0.0):
            raise GardeArret(f"sonde {nom} : direction blanchie nulle ou non finie")
        b = float(-w @ (mp + mn) / 2.0)
    return SondeLineaireJetons(nom, int(couche), "max", w, b, None, "difference_moyennes_blanchie")


def _reduction(X):
    mu, s = X.mean(axis=0), X.std(axis=0)
    return mu, np.where(s > 1e-12, s, 1.0)


def logistique_l2(nom: str, couche: int, sequences, y, inverse_penalite: float) -> SondeLineaireJetons:
    """Voir l'en-tête (famille 3)."""
    _verifier_donnees(sequences, y)
    if inverse_penalite not in INVERSES_PENALITE:
        raise GardeArret(f"inverse de la pénalité {inverse_penalite!r} hors de {INVERSES_PENALITE}")
    y = np.asarray(y)
    seqs = _f64(sequences)
    X = np.concatenate(seqs)
    t = np.concatenate([np.full(len(s), int(c)) for s, c in zip(seqs, y)])
    poids = np.concatenate([np.full(len(s), 1.0 / len(s)) for s in seqs])
    with threadpool_limits(1):
        mu, sd = _reduction(X)
        Z = (X - mu) / sd
        modele = LogisticRegression(C=float(inverse_penalite), l1_ratio=0.0, fit_intercept=True,
                                    **SOLVEUR_LOGISTIQUE)
        with warnings.catch_warnings():
            warnings.simplefilter("error", ConvergenceWarning)
            try:
                modele.fit(Z, t, sample_weight=poids)
            except ConvergenceWarning as e:
                raise GardeArret(f"sonde {nom} : régression logistique non convergée ({e})") from None
        coef = modele.coef_.ravel().astype(np.float64)
        w = coef / sd
        b = float(modele.intercept_[0]) - float(mu @ w)
    if not np.all(np.isfinite(w)):
        raise GardeArret(f"sonde {nom} : coefficients non finis")
    return SondeLineaireJetons(nom, int(couche), "max", w, b, None, "logistique_l2")


def _verifier_valeurs(valeurs, n) -> np.ndarray:
    v = np.asarray(valeurs, dtype=np.float64)
    if v.shape != (n,):
        raise GardeArret(f"valeurs déclarées : {n} attendues, forme {v.shape}")
    if not np.all(np.isfinite(v)) or np.any(v <= 0.0):
        raise GardeArret("valeur déclarée non finie ou ≤ 0 : logarithme impossible (aucun repli)")
    return v


def _verifier_vecteurs(vecteurs) -> np.ndarray:
    X = np.asarray(vecteurs, dtype=np.float64)
    if X.ndim != 2 or X.shape[0] < 2:
        raise GardeArret(f"jetons d'avant le champ : (actions ≥ 2, largeur) attendu, forme {X.shape}")
    if not np.all(np.isfinite(X)):
        raise GardeArret("jeton d'avant le champ non fini")
    return X


def regression_ridge_honnetes(nom: str, vecteurs_honnetes, valeurs_honnetes, alpha: float,
                              couche: int = 15) -> SondeLineaireJetons:
    """Voir l'en-tête (famille 4). `vecteurs_honnetes` : (n, d), jetons d'avant le champ d'épisodes honnêtes seulement
    (l'appelant en répond ; la lecture C le contrôle par les étiquettes)."""
    if alpha not in ALPHAS_RIDGE:
        raise GardeArret(f"alpha {alpha!r} hors de {ALPHAS_RIDGE}")
    X = _verifier_vecteurs(vecteurs_honnetes)
    t = np.log(_verifier_valeurs(valeurs_honnetes, X.shape[0]))
    n, d = X.shape
    with threadpool_limits(1):
        mu, sd = _reduction(X)
        Z = (X - mu) / sd
        tc = t - t.mean()
        a = float(alpha)
        if n >= d:
            beta = np.linalg.solve(Z.T @ Z + a * np.eye(d), Z.T @ tc)
        else:
            beta = Z.T @ np.linalg.solve(Z @ Z.T + a * np.eye(n), tc)
        w = beta / sd
        b = float(t.mean()) - float(mu @ w)
    if not np.all(np.isfinite(w)):
        raise GardeArret(f"sonde {nom} : coefficients non finis")
    return SondeLineaireJetons(nom, int(couche), "max", w, b, None, "ridge_honnetes")


def residu_ridge(sonde: SondeLineaireJetons, vecteurs, valeurs) -> np.ndarray:
    """Statistique lue : log(valeur déclarée) − prédiction de la sonde, par action (« déclaré moins attendu »)."""
    if sonde.famille != "ridge_honnetes":
        raise GardeArret(f"résidu : sonde ridge attendue, reçu {sonde.famille}")
    X = _verifier_vecteurs(vecteurs)
    v = _verifier_valeurs(valeurs, X.shape[0])
    with threadpool_limits(1):
        r = np.log(v) - sonde.scores_par_jeton(X)
    return np.asarray(r, dtype=np.float64)


def scores_actions(sonde, sequences) -> np.ndarray:
    """Score de chaque action : **maximum** sur ses jetons de w·h + b (double précision). Refuse toute agrégation autre
    que le maximum. Calcul vectorisé : jetons mis bout à bout, un produit, puis maximum par action
    (`numpy.maximum.reduceat`)."""
    if sonde.agregation != "max":
        raise GardeArret(f"sonde {sonde.nom} : agrégation {sonde.agregation!r} ; le maximum seulement")
    if len(sequences) == 0:
        raise GardeArret("aucune action")
    d = int(np.asarray(sonde.w).shape[0])
    sequences = [np.asarray(q) for q in sequences]
    longueurs = np.empty(len(sequences), dtype=np.int64)
    for i, q in enumerate(sequences):
        if q.ndim != 2 or q.shape[0] < 1 or q.shape[1] != d:
            raise GardeArret(f"action de forme {q.shape} : (jetons ≥ 1, {d}) attendue")
        longueurs[i] = q.shape[0]
    X = np.concatenate(sequences).astype(np.float64, copy=False)
    debuts = np.concatenate([[0], np.cumsum(longueurs)[:-1]])
    with threadpool_limits(1):
        par_jeton = sonde.scores_par_jeton(X)
        out = np.maximum.reduceat(par_jeton, debuts)
    if not np.all(np.isfinite(out)):
        raise GardeArret(f"sonde {sonde.nom} : score non fini")
    return np.asarray(out, dtype=np.float64)


def diagnostic_moyenne_jetons(sonde, sequences) -> np.ndarray:
    """DIAGNOSTIC SEULEMENT (N-026) : moyenne sur les jetons de w·h + b. Interdite en production ; jamais appelée par
    défaut ni par une autre fonction de ce paquet (un essai le vérifie)."""
    _verifier_donnees(sequences)
    with threadpool_limits(1):
        return np.array([float(np.mean(sonde.scores_par_jeton(np.asarray(s, dtype=np.float64)))) for s in sequences])


def apprendre(famille: str, nom: str, couche: int, sequences, y, reglage, paires=None) -> SondeLineaireJetons:
    """Point d'entrée des familles lues sur les jetons (1 à 3). La famille 4 a ses propres entrées."""
    if famille == "difference_moyennes_appariee":
        if reglage is not None:
            raise GardeArret("différence des moyennes : aucun réglage")
        return difference_moyennes_appariee(nom, couche, sequences, y, paires)
    if famille == "difference_moyennes_blanchie":
        return difference_moyennes_blanchie(nom, couche, sequences, y, reglage, paires)
    if famille == "logistique_l2":
        if paires is not None:
            raise GardeArret("régression logistique : pas de paires")
        return logistique_l2(nom, couche, sequences, y, reglage)
    raise GardeArret(f"famille {famille!r} inconnue : {FAMILLES_JETONS}")

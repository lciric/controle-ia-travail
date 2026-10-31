#!/usr/bin/env python3
"""Arène coévolutive synthétique : défense « mélange d'équilibre » contre défense « unique réentraînée » — v1.

Pilote de mécanisme, sur processeur, de la piste 3 du brainstorm
`p-041-pont-vers-les-vrais-modeles-v1/brainstorm-malleabilite-et-arene-v1.md` (décision de Lazar R-695).
Aucun modèle de langage, aucun texte : « l'attaquant » est un choix de paramètres dans une famille bornée de lois
synthétiques (mélanges gaussiens en dimension d), sous une contrainte de comportement (distance ≤ δ à une loi cible,
piste 2). Le défenseur est un classificateur simple sur échantillons, seuillé à un taux de fausses alertes α sur des
échantillons propres.

Quatre bras, chacun avec sa propre trajectoire coévolutive de T tours (l'attaquant joue en dernier à chaque tour) :
- A « unique réentraîné » (protocole de Bailey et collègues) : un moniteur linéaire réentraîné à chaque tour sur
  toutes les attaques passées (mélange uniforme), seul déployé ;
- B « mélange d'équilibre » (double oracle) : tous les moniteurs passés, tirés au hasard selon les poids d'équilibre
  du jeu à somme nulle restreint (programme linéaire) ; l'oracle du défenseur entraîne un moniteur linéaire contre la
  stratégie d'équilibre de l'attaquant ;
- C « mélange uniforme » : moniteurs entraînés comme en A, déployés en mélange uniforme (sans résolution du jeu) ;
- D « unique à capacité égale » : un seul moniteur « maxout » (log-somme-exp de m scores linéaires) réentraîné sur
  toutes les attaques passées, avec m = nombre de moniteurs du mélange de B au même tour (même nombre de paramètres).

Racines (R9) : RACINE et RACINE_TENUE servent à la décision et ne s'emploient qu'après scellement du
préenregistrement (`exiger_prereg_arene`) ; RACINE_ESSAI et RACINE_ESSAI_TENUE servent à la plomberie et au calcul de
puissance. Toute graine est `SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, role, …))`.

Commandes :
    PYTHONPATH=src python3 <ce fichier> essai --instances 0:24 --sortie FICHIER.json --processus 2
    PYTHONPATH=src python3 <ce fichier> decision --prereg prereg/<préenregistrement scellé>.md   (après GO seulement)
"""
from __future__ import annotations

import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import argparse  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import subprocess  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from dataclasses import asdict, dataclass, replace  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
from scipy.optimize import linprog, minimize  # noqa: E402
from scipy.special import expit, logsumexp, softmax  # noqa: E402

ICI = Path(__file__).resolve().parent
DEPOT = ICI.parents[4]
if str(DEPOT / "src") not in sys.path:
    sys.path.insert(0, str(DEPOT / "src"))

from controle_ia.gardes import GardeArret, exiger_numpy_minimal  # noqa: E402

VERSION = "arene_melange_v1"
IDENTIFIANT_PREREG = "PREREG-ARENE-MELANGE-EQUILIBRE-V1"

# --- racines (R9) : fixées par ce texte avant toute exécution, sans lien avec un résultat -------------------------
RACINE = 20261201              # décision : jamais employée en essai
RACINE_TENUE = 20261202        # décision : familles tenues à l'écart (racine à part)
RACINE_ESSAI = 20261291        # essai : plomberie et puissance
RACINE_ESSAI_TENUE = 20261292  # essai : familles tenues à l'écart
RACINES_DECISION = (RACINE, RACINE_TENUE)

# --- codes de dérivation des graines ----------------------------------------------------------------------------
BRAS = {"A": 1, "B": 2, "C": 3, "D": 4}
COMMUN = 0
ROLE_CIBLE, ROLE_PROPRE_ENTR, ROLE_ATTAQUE_ENTR, ROLE_CAL, ROLE_FPR = 0, 1, 2, 3, 4
ROLE_MC, ROLE_DEPARTS, ROLE_EVAL, ROLE_INIT_MAXOUT = 5, 6, 7, 8
ROLE_TENUE_LOIS, ROLE_TENUE_EVAL, ROLE_FINAL, ROLE_COUT = 9, 10, 11, 12
ROLE_REECH = 99


@dataclass(frozen=True)
class Config:
    d: int = 6                       # dimension des « activations » synthétiques
    K: int = 3                       # composantes du mélange (cible et attaque)
    r_cible: float = 4.0             # distance des moyennes cibles à l'origine (loi propre N(0, I))
    sigma_cible: float = 1.0
    boite_mu: float = 5.0            # |μ_kj| ≤ boite_mu
    sigma_min: float = 0.5
    sigma_max: float = 1.5
    deltas: tuple = (1.6, 2.4)       # budgets de comportement δ (0,4 r et 0,6 r), fixés avant toute exécution
    alpha: float = 0.01              # taux de fausses alertes visé sur le propre
    T: int = 8                       # tours de coévolution
    n_propre_entr: int = 2000
    n_attaque_entr: int = 2001       # multiple de K
    n_cal: int = 20000
    n_fpr: int = 20000
    n_eval: int = 19998              # multiple de K
    n_mc: int = 256                  # échantillons de Monte-Carlo par composante pour l'attaquant
    n_mc_final: int = 512
    departs: int = 4                 # départs aléatoires de la meilleure réponse à chaque tour
    departs_final: int = 12
    departs_cout: int = 3
    departs_renforce: int = 48       # attaquant final renforcé (contrôle de l'optimiseur)
    iter_renforce: int = 200
    iter_max: int = 100              # itérations SLSQP
    tau: float = 0.25                # température du lissage (unités d'écart-type du score propre)
    l2: float = 1e-3
    entrainement: str = "detection"  # oracle du défenseur, identique pour les quatre bras ("logistique" : variante)
    departs_entr: int = 8
    iter_entr: int = 300             # itérations L-BFGS-B de l'entraînement
    n_tenue: int = 50                # lois tenues à l'écart par instance (deux sous-familles)
    n_eval_tenue: int = 3999         # multiple de K
    seuil_contournement: float = 0.10  # contournement = détection ≤ ce seuil (10 α)
    pas_bissection: int = 5
    tol_fpr: float = 0.005           # garde : |FPR mesuré − α| ≤ tol_fpr
    taux_nonconv_max: float = 0.05   # garde : part d'entraînements non convergés
    plafond_cpu_tache_s: float = 600.0  # garde : temps processeur d'une tâche (δ, instance)

    def canonique(self) -> bytes:
        return json.dumps(asdict(self), sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()

    def empreinte(self) -> str:
        return hashlib.sha256(self.canonique()).hexdigest()


CONFIG_V1 = Config()


# =================================================================================================================
# Graines et racines
# =================================================================================================================
def gen(racine: int, *cle: int) -> np.random.Generator:
    exiger_numpy_minimal()
    return np.random.default_rng(np.random.SeedSequence(entropy=int(racine), spawn_key=tuple(int(c) for c in cle)))


def exiger_racines_essai(racine: int, racine_tenue: int) -> None:
    """Garde : en essai, aucune racine de décision."""
    for r in (racine, racine_tenue):
        if int(r) in RACINES_DECISION:
            raise GardeArret(f"racine {r} réservée à la décision : interdite en essai (préenregistrement scellé exigé)")
    if racine == racine_tenue:
        raise GardeArret("racine des familles tenues à l'écart égale à la racine principale : racine à part exigée")


def exiger_identite_prereg(texte: str) -> None:
    """Garde : le préenregistrement scellé est bien celui de cette arène, avec les racines du code."""
    if IDENTIFIANT_PREREG not in texte:
        raise GardeArret(f"préenregistrement sans l'identifiant {IDENTIFIANT_PREREG} : ce n'est pas celui de l'arène")
    for nom, val in (("RACINE", RACINE), ("RACINE_TENUE", RACINE_TENUE)):
        if not re.search(rf"\b{nom}\s*=\s*{val}\b", texte):
            raise GardeArret(f"préenregistrement : {nom} = {val} absent ou différent du code")
    if not re.search(rf"\b{CONFIG_V1.empreinte()}\b", texte):
        raise GardeArret("préenregistrement : empreinte de la configuration du code absente")
    code = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if not re.search(rf"\b{code}\b", texte):
        raise GardeArret("préenregistrement : empreinte du fichier de code exécuté absente (code modifié après gel ?)")


def exiger_prereg_arene(chemin: str | Path) -> str:
    """Avant toute exécution sur RACINE : préenregistrement conforme, scellé, intact, et identifié (R1)."""
    from controle_ia.prereg import exiger_prereg_scelle

    sha = exiger_prereg_scelle(chemin)
    exiger_identite_prereg(Path(chemin).read_text(encoding="utf-8"))
    return sha


# =================================================================================================================
# Lois : mélanges gaussiens à poids égaux, covariances diagonales
# =================================================================================================================
def vecteur(mu: np.ndarray, sig: np.ndarray) -> np.ndarray:
    return np.concatenate([mu.ravel(), sig.ravel()])


def deplier(theta: np.ndarray, cfg: Config) -> tuple[np.ndarray, np.ndarray]:
    n = cfg.K * cfg.d
    return theta[:n].reshape(cfg.K, cfg.d), theta[n:].reshape(cfg.K, cfg.d)


def bornes(cfg: Config) -> list[tuple[float, float]]:
    n = cfg.K * cfg.d
    return [(-cfg.boite_mu, cfg.boite_mu)] * n + [(cfg.sigma_min, cfg.sigma_max)] * n


def distance(theta: np.ndarray, cible: np.ndarray, cfg: Config) -> float:
    """Distance de comportement : racine de la moyenne sur k de W2² entre composantes appariées (diagonales)."""
    return float(np.sqrt(np.sum((theta - cible) ** 2) / cfg.K))


def exiger_admissible(theta: np.ndarray, cible: np.ndarray, delta: float, cfg: Config) -> None:
    if not np.all(np.isfinite(theta)):
        raise GardeArret("loi d'attaque non finie")
    lo = np.array([b[0] for b in bornes(cfg)])
    hi = np.array([b[1] for b in bornes(cfg)])
    if np.any(theta < lo - 1e-9) or np.any(theta > hi + 1e-9):
        raise GardeArret("loi d'attaque hors de la boîte")
    if distance(theta, cible, cfg) > delta * (1 + 1e-9) + 1e-12:
        raise GardeArret(f"loi d'attaque à distance {distance(theta, cible, cfg):.6f} > δ = {delta}")


def projeter(theta: np.ndarray, cible: np.ndarray, delta: float, cfg: Config) -> tuple[np.ndarray, bool]:
    """Projection déclarée (contrainte puis boîte) ; renvoie aussi si elle a bougé le point (compté, jamais tu)."""
    v = theta - cible
    dist = distance(theta, cible, cfg)
    if dist > delta:
        v = v * (delta / dist)
    lo = np.array([b[0] for b in bornes(cfg)])
    hi = np.array([b[1] for b in bornes(cfg)])
    p = np.clip(cible + v, lo, hi)
    bouge = bool(np.max(np.abs(p - theta)) > 1e-6)   # en deçà : tolérance numérique de SLSQP, non comptée
    exiger_admissible(p, cible, delta, cfg)
    return p, bouge


def echantillonner(theta: np.ndarray, n: int, rng: np.random.Generator, cfg: Config) -> np.ndarray:
    if n % cfg.K:
        raise GardeArret(f"n = {n} non multiple de K = {cfg.K} : échantillonnage stratifié impossible")
    mu, sig = deplier(theta, cfg)
    z = rng.standard_normal((cfg.K, n // cfg.K, cfg.d))
    return (mu[:, None, :] + sig[:, None, :] * z).reshape(n, cfg.d)


def loi_cible(instance: int, racine: int, cfg: Config) -> np.ndarray:
    g = gen(racine, COMMUN, instance, COMMUN, 0, ROLE_CIBLE)
    u = g.standard_normal((cfg.K, cfg.d))
    u /= np.linalg.norm(u, axis=1, keepdims=True)
    return vecteur(cfg.r_cible * u, np.full((cfg.K, cfg.d), cfg.sigma_cible))


def depart_tire_vers_l_origine(cible: np.ndarray, delta: float, cfg: Config) -> np.ndarray:
    mu, sig = deplier(cible, cfg)
    n = np.linalg.norm(mu, axis=1, keepdims=True)
    return projeter(vecteur(mu * (1 - np.minimum(delta / n, 1.0)), sig), cible, delta, cfg)[0]


# =================================================================================================================
# Moniteurs
# =================================================================================================================
class Moniteur:
    """Score « maxout » : log-somme-exp de m scores linéaires (m = 1 : linéaire). Seuil t calibré à α sur le propre."""

    def __init__(self, W: np.ndarray, b: np.ndarray):
        W = np.atleast_2d(np.asarray(W, float))
        b = np.atleast_1d(np.asarray(b, float))
        if not (np.all(np.isfinite(W)) and np.all(np.isfinite(b))):
            raise GardeArret("paramètres de moniteur non finis")
        self.W, self.b = W, b
        self.t = np.nan
        self.e = np.nan
        self._cache: dict = {}

    @property
    def m(self) -> int:
        return self.W.shape[0]

    def score(self, X: np.ndarray) -> np.ndarray:
        a = X @ self.W.T + self.b
        return a[:, 0] if self.m == 1 else logsumexp(a, axis=1)

    def grad(self, X: np.ndarray) -> np.ndarray:
        if self.m == 1:
            return np.broadcast_to(self.W[0], X.shape)
        return softmax(X @ self.W.T + self.b, axis=1) @ self.W

    def calibrer(self, Xcal: np.ndarray, alpha: float) -> "Moniteur":
        s = self.score(Xcal)
        if not np.all(np.isfinite(s)):
            raise GardeArret("scores propres non finis")
        self.t = float(np.quantile(s, 1 - alpha, method="higher"))
        self.e = float(np.std(s))
        if not self.e > 0:
            raise GardeArret("score propre de variance nulle : seuil non calibrable")
        return self

    def detecte(self, X: np.ndarray) -> np.ndarray:
        if not np.isfinite(self.t):
            raise GardeArret("moniteur non calibré")
        return self.score(X) > self.t

    def taux_cache(self, cle, X_fournisseur) -> float:
        """Taux de détection sur un ensemble d'évaluation identifié par `cle` (mémorisé)."""
        if cle not in self._cache:
            self._cache[cle] = float(np.mean(self.detecte(X_fournisseur())))
        return self._cache[cle]


def _somme_ponderee(X: np.ndarray, S: np.ndarray, w: np.ndarray) -> np.ndarray:
    """Σ_i w_i ∂s(x_i)/∂(W, b) pour un score maxout (S = poids softmax des unités ; m = 1 : S = 1)."""
    G = w[:, None] * S
    return np.concatenate([(G.T @ X).ravel(), G.sum(0)])


def _scores(p: np.ndarray, X: np.ndarray, m: int):
    d = X.shape[1]
    A = X @ p[: m * d].reshape(m, d).T + p[m * d:]
    if m == 1:
        return A[:, 0], np.ones((len(X), 1))
    return logsumexp(A, axis=1), softmax(A, axis=1)


def _logistique(Xp, Xa, m, cfg: Config, x0):
    X = np.vstack([Xp, Xa])
    y = np.concatenate([-np.ones(len(Xp)), np.ones(len(Xa))])
    n, d = X.shape

    def f(p):
        s, S = _scores(p, X, m)
        ys = y * s
        W = p[: m * d]
        g = _somme_ponderee(X, S, -y * expit(-ys) / n)
        g[: m * d] += 2 * cfg.l2 * W
        return np.mean(np.logaddexp(0.0, -ys)) + cfg.l2 * np.sum(W * W), g

    return minimize(f, x0, jac=True, method="L-BFGS-B", options={"maxiter": cfg.iter_entr})


def objectif_detection(p, Xp, Xa, m, cfg: Config):
    """Taux de détection lissé au seuil α, seuil approché par moyenne + z_{1−α} × écart-type des scores propres
    (exact en population pour un moniteur linéaire, la loi propre étant N(0, I)). Renvoie (−J, −∇J)."""
    from scipy.stats import norm

    z = norm.ppf(1 - cfg.alpha)
    sp, Sp = _scores(p, Xp, m)
    sa, Sa = _scores(p, Xa, m)
    moy, et = sp.mean(), sp.std()
    if not et > 0:
        return 0.0, np.zeros_like(p)
    u = (sa - moy) / et - z
    sg = expit(u / cfg.tau)
    J = sg.mean()
    ga = sg * (1 - sg) / cfg.tau / len(Xa)
    d_sa = _somme_ponderee(Xa, Sa, ga)
    d_moy = _somme_ponderee(Xp, Sp, np.full(len(Xp), 1.0 / len(Xp)))
    d_et = _somme_ponderee(Xp, Sp, (sp - moy) / (len(Xp) * et))
    dJ = (d_sa - ga.sum() * d_moy) / et - (np.sum(ga * (sa - moy)) / et ** 2) * d_et
    return -J, -dJ


def entrainer(Xp: np.ndarray, Xa: np.ndarray, m: int, cfg: Config, rng_init: np.random.Generator | None,
              directions=()):
    """Entraîne un moniteur à m unités (m = 1 : linéaire). Renvoie (moniteur, convergé).

    - `entrainement = "logistique"` : régression logistique (départ nul si m = 1, départ tiré si m > 1) ;
    - `entrainement = "detection"` (défaut) : oracle qui maximise le taux de détection lissé au seuil α ; départs
      déterministes = solution logistique, puis (m = 1) les directions des moyennes de composantes des lois
      d'entraînement, par poids décroissant, jusqu'à `departs_entr` départs ; (m > 1) une seconde initialisation dont
      les unités sont ces directions. Le meilleur départ (objectif d'entraînement) est retenu.
    """
    d = Xp.shape[1]
    if m == 1:
        x0 = np.zeros(d + 1)
    else:
        if rng_init is None:
            raise GardeArret("maxout sans graine d'initialisation")
        idx = rng_init.permutation(len(Xa))
        W0 = np.stack([0.5 * Xa[part].mean(0) for part in np.array_split(idx, m)])
        x0 = np.concatenate([W0.ravel(), np.zeros(m)])
    res = _logistique(Xp, Xa, m, cfg, x0)
    if not np.all(np.isfinite(res.x)) or not np.isfinite(res.fun):
        raise GardeArret("entraînement logistique : paramètres ou perte non finis")
    if cfg.entrainement == "logistique":
        return Moniteur(res.x[: m * d].reshape(m, d), res.x[m * d:]), bool(res.success)
    if cfg.entrainement != "detection":
        raise GardeArret(f"entraînement inconnu : {cfg.entrainement!r}")
    dirs = [np.asarray(v, float) for v in directions]
    departs = [res.x]
    if m == 1:
        departs += [np.concatenate([v, [0.0]]) for v in dirs[: max(cfg.departs_entr - 1, 0)]]
    elif dirs:
        departs.append(np.concatenate([np.stack([dirs[j % len(dirs)] for j in range(m)]).ravel(), np.zeros(m)]))
    meilleur = None
    for x in departs:
        r = minimize(objectif_detection, x, args=(Xp, Xa, m, cfg), jac=True, method="L-BFGS-B",
                     options={"maxiter": cfg.iter_entr})
        if not np.all(np.isfinite(r.x)) or not np.isfinite(r.fun):
            raise GardeArret("entraînement par détection : paramètres ou objectif non finis")
        if meilleur is None or r.fun < meilleur.fun:
            meilleur = r
    return Moniteur(meilleur.x[: m * d].reshape(m, d), meilleur.x[m * d:]), bool(meilleur.success)


# =================================================================================================================
# Défense mixte et jeu à somme nulle
# =================================================================================================================
def exiger_poids(p: np.ndarray) -> np.ndarray:
    p = np.asarray(p, float)
    if not np.all(np.isfinite(p)) or np.any(p < -1e-9) or abs(p.sum() - 1) > 1e-6:
        raise GardeArret(f"poids de mélange invalides : {p}")
    p = np.clip(p, 0, None)
    return p / p.sum()


def taux_defense(defense, X: np.ndarray) -> float:
    return float(sum(p * np.mean(m.detecte(X)) for m, p in defense if p > 0))


def resoudre_jeu(G: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    """Jeu à somme nulle : lignes = moniteurs (maximisent la détection), colonnes = attaques. Renvoie (p, q, valeur)."""
    G = np.asarray(G, float)
    if G.ndim != 2 or not np.all(np.isfinite(G)) or np.any(G < 0) or np.any(G > 1):
        raise GardeArret("matrice de gains invalide (non finie ou hors [0, 1])")
    ni, nj = G.shape
    # défenseur : max v ; v ≤ Σ_i p_i G[i, j] pour tout j
    c = np.zeros(ni + 1)
    c[-1] = -1
    r1 = linprog(c, A_ub=np.hstack([-G.T, np.ones((nj, 1))]), b_ub=np.zeros(nj),
                 A_eq=np.hstack([np.ones((1, ni)), np.zeros((1, 1))]), b_eq=[1],
                 bounds=[(0, None)] * ni + [(None, None)], method="highs")
    # attaquant : min u ; Σ_j q_j G[i, j] ≤ u pour tout i
    c2 = np.zeros(nj + 1)
    c2[-1] = 1
    r2 = linprog(c2, A_ub=np.hstack([G, -np.ones((ni, 1))]), b_ub=np.zeros(ni),
                 A_eq=np.hstack([np.ones((1, nj)), np.zeros((1, 1))]), b_eq=[1],
                 bounds=[(0, None)] * nj + [(None, None)], method="highs")
    if r1.status != 0 or r2.status != 0:
        raise GardeArret(f"programme linéaire non résolu ({r1.message} ; {r2.message})")
    v, u = -r1.fun, r2.fun
    if abs(v - u) > 1e-7:
        raise GardeArret(f"valeurs primale et duale du jeu différentes : {v} ≠ {u}")
    return exiger_poids(r1.x[:ni]), exiger_poids(r2.x[:nj]), float(v)


# =================================================================================================================
# Attaquant : meilleure réponse dans la boîte, sous la contrainte de comportement
# =================================================================================================================
def objectif_lisse(theta, defense, z, cfg: Config):
    mu, sig = deplier(theta, cfg)
    K, n, d = z.shape
    X = (mu[:, None, :] + sig[:, None, :] * z).reshape(K * n, d)
    total, gmu, gsig = 0.0, np.zeros((K, d)), np.zeros((K, d))
    for m, p in defense:
        if p <= 0:
            continue
        u = (m.score(X) - m.t) / (cfg.tau * m.e)
        sg = expit(u)
        total += p * sg.mean()
        ds = p * sg * (1 - sg) / (cfg.tau * m.e) / (K * n)
        G = (m.grad(X) * ds[:, None]).reshape(K, n, d)
        gmu += G.sum(1)
        gsig += (G * z).sum(1)
    return total, vecteur(gmu, gsig)


def taux_dur(theta, defense, z, cfg: Config) -> float:
    mu, sig = deplier(theta, cfg)
    K, n, d = z.shape
    return taux_defense(defense, (mu[:, None, :] + sig[:, None, :] * z).reshape(K * n, d))


def meilleure_reponse(defense, cible, delta, cfg: Config, rng_mc, rng_departs, departs_suppl=(), n_departs=None,
                      n_mc=None, iter_max=None) -> tuple[np.ndarray, dict]:
    n_departs = cfg.departs if n_departs is None else n_departs
    iter_max = cfg.iter_max if iter_max is None else iter_max
    z = rng_mc.standard_normal((cfg.K, cfg.n_mc if n_mc is None else n_mc, cfg.d))
    departs = [depart_tire_vers_l_origine(cible, delta, cfg)]
    for _ in range(n_departs):
        v = rng_departs.standard_normal(cible.size)
        v *= np.sqrt(cfg.K) * delta * rng_departs.uniform(0.5, 1.0) / np.linalg.norm(v)
        departs.append(projeter(cible + v, cible, delta, cfg)[0])
    departs += [projeter(np.asarray(s, float), cible, delta, cfg)[0] for s in departs_suppl]
    contrainte = {"type": "ineq",
                  "fun": lambda th: delta ** 2 - np.sum((th - cible) ** 2) / cfg.K,
                  "jac": lambda th: -2 * (th - cible) / cfg.K}
    meilleur, n_proj = None, 0
    for x0 in departs:
        res = minimize(objectif_lisse, x0, args=(defense, z, cfg), jac=True, method="SLSQP", bounds=bornes(cfg),
                       constraints=[contrainte], options={"maxiter": iter_max, "ftol": 1e-7})
        if not np.all(np.isfinite(res.x)):
            continue
        th, bouge = projeter(res.x, cible, delta, cfg)
        n_proj += bouge
        cand = (taux_dur(th, defense, z, cfg), objectif_lisse(th, defense, z, cfg)[0], th)
        if meilleur is None or cand[:2] < meilleur[:2]:
            meilleur = cand
    if meilleur is None:
        raise GardeArret("meilleure réponse : aucun départ n'a donné de point fini")
    exiger_admissible(meilleur[2], cible, delta, cfg)
    return meilleur[2], {"projections": n_proj, "departs": len(departs),
                         "distance_consommee": distance(meilleur[2], cible, cfg)}


# =================================================================================================================
# Familles tenues à l'écart (racine à part)
# =================================================================================================================
def lois_tenues(cible, delta, instance, code_delta, racine_tenue, cfg: Config) -> list[np.ndarray]:
    g = gen(racine_tenue, code_delta, instance, COMMUN, 0, ROLE_TENUE_LOIS)
    sortie = []
    for j in range(cfg.n_tenue):
        if j % 2 == 0:  # sous-famille 1 : déplacement aléatoire dans la boule de comportement
            v = g.standard_normal(cible.size)
            v *= np.sqrt(cfg.K) * delta * g.uniform(0.5, 1.0) / np.linalg.norm(v)
        else:           # sous-famille 2 : tout le budget sur une composante, tirée vers l'origine, échelle tirée
            mu, sig = deplier(cible, cfg)
            k = int(g.integers(cfg.K))
            dmu, dsig = np.zeros_like(mu), np.zeros_like(sig)
            dmu[k] = -mu[k] / np.linalg.norm(mu[k])
            dsig[k] = g.uniform(-1, 1, cfg.d)
            v = vecteur(dmu, dsig)
            v *= np.sqrt(cfg.K) * delta * g.uniform(0.5, 1.0) / np.linalg.norm(v)
        sortie.append(projeter(cible + v, cible, delta, cfg)[0])
    return sortie


# =================================================================================================================
# Une tâche = (δ, instance) : les quatre bras
# =================================================================================================================
class Contexte:
    def __init__(self, instance, code_delta, racine, racine_tenue, cfg: Config):
        self.i, self.cd, self.r, self.rt, self.cfg = instance, code_delta, racine, racine_tenue, cfg
        self.delta = cfg.deltas[code_delta - 1]
        self.cible = loi_cible(instance, racine, cfg)
        self.Xcal = gen(racine, code_delta, instance, COMMUN, 0, ROLE_CAL).standard_normal((cfg.n_cal, cfg.d))
        self.Xfpr = gen(racine, code_delta, instance, COMMUN, 0, ROLE_FPR).standard_normal((cfg.n_fpr, cfg.d))
        self.tenues = lois_tenues(self.cible, self.delta, instance, code_delta, racine_tenue, cfg)
        self._Xt = None
        self.nonconv = 0
        self.entr = 0

    def g(self, bras, tour, role, *extra):
        return gen(self.r, self.cd, self.i, bras, tour, role, *extra)

    def X_tenues(self):
        if self._Xt is None:
            g = gen(self.rt, self.cd, self.i, COMMUN, 0, ROLE_TENUE_EVAL)
            self._Xt = [echantillonner(th, self.cfg.n_eval_tenue, g, self.cfg) for th in self.tenues]
        return self._Xt

    def propre_entr(self, tour):
        return self.g(COMMUN, tour, ROLE_PROPRE_ENTR).standard_normal((self.cfg.n_propre_entr, self.cfg.d))

    def entrainer(self, bras, tour, attaques, q, m):
        """Moniteur entraîné sur le propre du tour (commun aux bras) contre le mélange q des attaques."""
        cfg = self.cfg
        q = exiger_poids(q)
        n = cfg.n_attaque_entr // cfg.K
        comptes = np.floor(q * n).astype(int)
        reste = n - comptes.sum()
        comptes[np.argsort(-(q * n - comptes), kind="stable")[:reste]] += 1
        g = self.g(bras, tour, ROLE_ATTAQUE_ENTR)
        Xa = np.vstack([echantillonner(a, cfg.K * c, g, cfg) for a, c in zip(attaques, comptes) if c > 0])
        init = self.g(bras, tour, ROLE_INIT_MAXOUT) if m > 1 else None
        dirs = []
        for j in np.argsort(-q, kind="stable"):
            if q[j] <= 0:
                continue
            mu, _ = deplier(attaques[j], cfg)
            dirs += [v / np.linalg.norm(v) for v in mu if np.linalg.norm(v) > 1e-12]
        mon, ok = entrainer(self.propre_entr(tour), Xa, m, cfg, init, dirs)
        self.entr += 1
        self.nonconv += (not ok)
        return mon.calibrer(self.Xcal, cfg.alpha)

    def exiger_fpr(self, defense) -> float:
        f = taux_defense(defense, self.Xfpr)
        if abs(f - self.cfg.alpha) > self.cfg.tol_fpr:
            raise GardeArret(f"taux de fausses alertes mesuré {f:.4f} hors de α ± {self.cfg.tol_fpr}")
        return f

    def taux_tenues(self, defense) -> list[float]:
        Xt = self.X_tenues()
        return [float(sum(p * m.taux_cache(("tenue", j), lambda j=j: Xt[j]) for m, p in defense if p > 0))
                for j in range(len(Xt))]


def residu_relatif(v: np.ndarray, passes: list[np.ndarray]) -> float:
    """Nouveauté résiduelle (piste 4) : norme du résidu de v après projection sur l'espace des déplacements passés."""
    nv = np.linalg.norm(v)
    if nv == 0:
        return 0.0
    if not passes:
        return 1.0
    B = np.stack(passes, axis=1)
    coef, *_ = np.linalg.lstsq(B, v, rcond=None)
    return float(np.linalg.norm(v - B @ coef) / nv)


def cout_contournement(defense, ctx: Contexte, code_bras, departs_suppl) -> dict:
    """Coût par contournement (piste 5) : plus petit budget δ' ≤ δ tel que la meilleure réponse est détectée au plus
    au seuil de contournement ; bissection sur [0, δ]. Censuré à δ si non contourné à δ."""
    cfg = ctx.cfg

    def taux(dp, k):
        if dp <= 0:
            return taux_defense(defense, echantillonner(ctx.cible, cfg.n_eval, ctx.g(code_bras, 99, ROLE_COUT, k, 1),
                                                         cfg))
        th, _ = meilleure_reponse(defense, ctx.cible, dp, cfg, ctx.g(code_bras, 99, ROLE_COUT, k, 2),
                                  ctx.g(code_bras, 99, ROLE_COUT, k, 3),
                                  departs_suppl=[projeter(s, ctx.cible, dp, cfg)[0] for s in departs_suppl],
                                  n_departs=cfg.departs_cout)
        return taux_defense(defense, echantillonner(th, cfg.n_eval, ctx.g(code_bras, 99, ROLE_COUT, k, 4), cfg))

    t_max = taux(ctx.delta, 0)
    if t_max > cfg.seuil_contournement:
        return {"delta_c": ctx.delta, "fraction": 1.0, "censure": True, "taux_a_delta": t_max}
    lo, hi = 0.0, ctx.delta
    for k in range(1, cfg.pas_bissection + 1):
        mid = (lo + hi) / 2
        if taux(mid, k) <= cfg.seuil_contournement:
            hi = mid
        else:
            lo = mid
    return {"delta_c": hi, "fraction": hi / ctx.delta, "censure": False, "taux_a_delta": t_max}


def trajectoire(nom: str, ctx: Contexte, M0: Moniteur) -> dict:
    cfg, cb = ctx.cfg, BRAS[nom]
    t0 = time.process_time()
    attaques = [ctx.cible]
    moniteurs = [M0]
    cles_eval = [("eval", COMMUN, 0)]
    eval_X = {cles_eval[0]: lambda: echantillonner(ctx.cible, cfg.n_eval, ctx.g(COMMUN, 0, ROLE_EVAL), cfg)}
    G = np.array([[M0.taux_cache(cles_eval[0], eval_X[cles_eval[0]])]]) if nom == "B" else None
    p = np.array([1.0])
    par_tour = {"iii": [], "ii": [], "poids_max": [], "distance": [], "nouveaute": [], "projections": [], "cpu_s": []}
    deplacements: list[np.ndarray] = []

    def defense_courante():
        if nom in ("A", "D"):
            return [(moniteurs[-1], 1.0)]
        if nom == "C":
            return [(m, 1.0 / len(moniteurs)) for m in moniteurs]
        return list(zip(moniteurs, p))

    for t in range(1, cfg.T + 1):
        tt = time.process_time()
        if nom == "B":
            p, _, _ = resoudre_jeu(G)
        dfs = defense_courante()
        a, info = meilleure_reponse(dfs, ctx.cible, ctx.delta, cfg, ctx.g(cb, t, ROLE_MC), ctx.g(cb, t, ROLE_DEPARTS),
                                    departs_suppl=[attaques[-1]])
        cle = ("eval", cb, t)
        eval_X[cle] = (lambda a=a, t=t: echantillonner(a, cfg.n_eval, ctx.g(cb, t, ROLE_EVAL), cfg))
        Xa_eval = eval_X[cle]()
        par_tour["iii"].append(taux_defense(dfs, Xa_eval))
        par_tour["ii"].append(float(np.mean(ctx.taux_tenues(dfs))))
        par_tour["poids_max"].append(float(max(w for _, w in dfs)))
        par_tour["distance"].append(info["distance_consommee"])
        par_tour["projections"].append(info["projections"])
        v = a - ctx.cible
        par_tour["nouveaute"].append(residu_relatif(v, deplacements))
        deplacements.append(v)
        attaques.append(a)
        cles_eval.append(cle)
        # mise à jour du défenseur
        if nom == "B":
            col = np.array([[m.taux_cache(cle, eval_X[cle]) for m in moniteurs]]).T
            G = np.hstack([G, col])
            _, q, _ = resoudre_jeu(G)
            mon = ctx.entrainer(cb, t, attaques, q, 1)
            ligne = np.array([[mon.taux_cache(c, eval_X[c]) for c in cles_eval]])
            G = np.vstack([G, ligne])
        else:
            m_unites = t + 1 if nom == "D" else 1   # D : autant d'unités que de moniteurs dans le mélange de B
            mon = ctx.entrainer(cb, t, attaques, np.full(len(attaques), 1.0 / len(attaques)), m_unites)
        if nom == "D":
            moniteurs = [mon]
        else:
            moniteurs.append(mon)
        par_tour["cpu_s"].append(time.process_time() - tt)
        if time.process_time() - t0 > cfg.plafond_cpu_tache_s:
            raise GardeArret(f"plafond de temps processeur d'une tâche dépassé (bras {nom}, tour {t})")

    # défense finale (après la mise à jour du tour T) ; l'attaquant joue en dernier
    tf = time.process_time()
    valeur_restreinte = None
    if nom == "B":
        p, _, valeur_restreinte = resoudre_jeu(G)
    dfin = defense_courante()
    fpr = ctx.exiger_fpr(dfin)
    a_fin, info_fin = meilleure_reponse(dfin, ctx.cible, ctx.delta, cfg, ctx.g(cb, cfg.T + 1, ROLE_FINAL, 1),
                                        ctx.g(cb, cfg.T + 1, ROLE_FINAL, 2), departs_suppl=attaques[1:],
                                        n_departs=cfg.departs_final, n_mc=cfg.n_mc_final)
    V_std = taux_defense(dfin, echantillonner(a_fin, cfg.n_eval, ctx.g(cb, cfg.T + 1, ROLE_FINAL, 3), cfg))
    # attaquant final renforcé : mêmes règles, quatre fois plus de départs, deux fois plus d'itérations ; (iii) retient
    # la plus forte des deux attaques (la plus basse détection), car (iii) n'est qu'une borne haute de la valeur du jeu
    a_renf, info_renf = meilleure_reponse(dfin, ctx.cible, ctx.delta, cfg, ctx.g(cb, cfg.T + 1, ROLE_FINAL, 4),
                                          ctx.g(cb, cfg.T + 1, ROLE_FINAL, 5), departs_suppl=attaques[1:] + [a_fin],
                                          n_departs=cfg.departs_renforce, n_mc=cfg.n_mc_final,
                                          iter_max=cfg.iter_renforce)
    V_renf = taux_defense(dfin, echantillonner(a_renf, cfg.n_eval, ctx.g(cb, cfg.T + 1, ROLE_FINAL, 6), cfg))
    V = min(V_std, V_renf)
    tenues = ctx.taux_tenues(dfin)
    vus = float(np.mean([sum(w * m.taux_cache(c, eval_X[c]) for m, w in dfin if w > 0) for c in cles_eval[1:]]))
    cout = cout_contournement(dfin, ctx, cb, attaques[1:] + [a_fin, a_renf])
    cpu_final = time.process_time() - tf
    unites = sum(m.m for m, _ in dfin) if nom != "D" else dfin[0][0].m
    parametres = sum(m.W.size + m.b.size for m, _ in dfin)
    return {
        "V_iii_final": V,
        "V_iii_standard": V_std,
        "V_iii_renforce": V_renf,
        "ii_final": float(np.mean(tenues)),
        "ii_final_sous_familles": [float(np.mean(tenues[0::2])), float(np.mean(tenues[1::2]))],
        "i_final_vus": vus,
        "cout": cout,
        "fpr_final": fpr,
        "poids_finaux": [float(w) for _, w in dfin],
        "valeur_jeu_restreint": valeur_restreinte,
        "distance_finale": info_fin["distance_consommee"],
        "projections_finales": info_fin["projections"] + info_renf["projections"],
        "unites_deployees": int(unites),
        "parametres_deployes": int(parametres),
        "par_tour": par_tour,
        "cpu_final_s": cpu_final,
        "cpu_total_s": time.process_time() - t0,
    }


def executer_tache(instance: int, code_delta: int, racine: int, racine_tenue: int, cfg: Config = CONFIG_V1,
                   bras=("A", "B", "C", "D")) -> dict:
    t0 = time.process_time()
    ctx = Contexte(instance, code_delta, racine, racine_tenue, cfg)
    M0 = ctx.entrainer(COMMUN, 0, [ctx.cible], np.array([1.0]), 1)
    M0_bis = ctx.entrainer(COMMUN, 0, [ctx.cible], np.array([1.0]), 1)
    exiger_meme_moniteur(M0, M0_bis)
    sortie = {"instance": instance, "code_delta": code_delta, "delta": ctx.delta, "racine": racine,
              "racine_tenue": racine_tenue, "config_sha256": cfg.empreinte(), "version": VERSION, "bras": {}}
    for nom in bras:
        M = Moniteur(M0.W.copy(), M0.b.copy()).calibrer(ctx.Xcal, cfg.alpha)
        sortie["bras"][nom] = trajectoire(nom, ctx, M)
    sortie["entrainements"] = ctx.entr
    sortie["non_convergences"] = ctx.nonconv
    exiger_convergence(ctx.nonconv, ctx.entr, cfg)
    sortie["cpu_tache_s"] = time.process_time() - t0
    return sortie


def exiger_meme_moniteur(a: Moniteur, b: Moniteur) -> None:
    if not (np.array_equal(a.W, b.W) and np.array_equal(a.b, b.b) and a.t == b.t):
        raise GardeArret("moniteur du tour 0 non reproductible bit à bit : il doit être commun aux quatre bras")


def exiger_convergence(nonconv: int, total: int, cfg: Config) -> None:
    if total and nonconv / total > cfg.taux_nonconv_max:
        raise GardeArret(f"entraînements non convergés : {nonconv}/{total} > {cfg.taux_nonconv_max}")


# =================================================================================================================
# Analyse : écarts appariés par instance, intervalles par rééchantillonnage
# =================================================================================================================
CONTRASTES = {  # code de contraste → (nom, bras 1, bras 2, mesure)
    1: ("B-A (iii)", "B", "A", "V_iii_final"),
    2: ("B-D (iii)", "B", "D", "V_iii_final"),
    3: ("B-C (iii)", "B", "C", "V_iii_final"),
    4: ("C-A (iii)", "C", "A", "V_iii_final"),
    5: ("D-A (iii)", "D", "A", "V_iii_final"),
    6: ("B-A (ii)", "B", "A", "ii_final"),
    7: ("B-A cout", "B", "A", "cout.fraction"),
    8: ("B-D (ii)", "B", "D", "ii_final"),
}


def _mesure(res_bras: dict, mesure: str) -> float:
    if mesure == "cout.fraction":
        return res_bras["cout"]["fraction"]
    return res_bras[mesure]


def analyser(resultats: list[dict], racine_reech: int, n_reech: int = 10000) -> dict:
    sortie = {}
    for cd in sorted({r["code_delta"] for r in resultats}):
        rs = sorted((r for r in resultats if r["code_delta"] == cd), key=lambda r: r["instance"])
        bloc = {"n": len(rs), "moyennes": {}, "contrastes": {}}
        for nom in ("A", "B", "C", "D"):
            if all(nom in r["bras"] for r in rs):
                bloc["moyennes"][nom] = {k: float(np.mean([_mesure(r["bras"][nom], k) for r in rs]))
                                         for k in ("V_iii_final", "ii_final", "i_final_vus", "cout.fraction")}
        for code, (lib, b1, b2, mes) in CONTRASTES.items():
            if not all(b1 in r["bras"] and b2 in r["bras"] for r in rs):
                continue
            dlt = np.array([_mesure(r["bras"][b1], mes) - _mesure(r["bras"][b2], mes) for r in rs])
            g = gen(racine_reech, cd, code, 0, 0, ROLE_REECH)
            idx = g.integers(0, len(dlt), size=(n_reech, len(dlt)))
            boot = dlt[idx].mean(1)
            bloc["contrastes"][lib] = {
                "moyenne": float(dlt.mean()), "ecart_type": float(dlt.std(ddof=1)) if len(dlt) > 1 else float("nan"),
                "ic95": [float(np.quantile(boot, 0.025)), float(np.quantile(boot, 0.975))],
                "ic90": [float(np.quantile(boot, 0.05)), float(np.quantile(boot, 0.95))],
                "zeros_exacts": int(np.sum(dlt == 0)),
            }
        sortie[str(cd)] = bloc
    return sortie


# =================================================================================================================
# Points d'entrée
# =================================================================================================================
def _travail(args):
    instance, cd, racine, racine_tenue, cfg_dict = args
    cfg = Config(**{k: tuple(v) if isinstance(v, list) else v for k, v in cfg_dict.items()})
    return executer_tache(instance, cd, racine, racine_tenue, cfg)


def executer(instances, racine, racine_tenue, cfg: Config, processus: int = 2) -> tuple[list[dict], dict]:
    import multiprocessing as mp

    taches = [(i, cd, racine, racine_tenue, asdict(cfg)) for cd in (1, 2) for i in instances]
    m0 = time.perf_counter()
    if processus > 1:
        with mp.get_context("spawn").Pool(processus) as pool:
            res = pool.map(_travail, taches, chunksize=1)
    else:
        res = [_travail(t) for t in taches]
    temps = {"mur_s": time.perf_counter() - m0, "cpu_somme_taches_s": float(sum(r["cpu_tache_s"] for r in res)),
             "processus": processus, "taches": len(taches)}
    return res, temps


def _versions() -> dict:
    import platform

    import scipy

    try:
        commit = subprocess.run(["git", "-C", str(DEPOT), "rev-parse", "HEAD"], capture_output=True,
                                text=True).stdout.strip()
    except OSError:
        commit = None
    return {"python": sys.version.split()[0], "numpy": np.__version__, "scipy": scipy.__version__,
            "plateforme": platform.platform(), "commit": commit,
            "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def _plage(s: str) -> list[int]:
    a, b = s.split(":")
    return list(range(int(a), int(b)))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sp = ap.add_subparsers(dest="mode", required=True)
    e = sp.add_parser("essai", help="racine d'essai : plomberie et puissance")
    e.add_argument("--instances", default="0:4")
    e.add_argument("--sortie", required=True)
    e.add_argument("--processus", type=int, default=2)
    e.add_argument("--racine", type=int, default=RACINE_ESSAI)
    e.add_argument("--racine-tenue", type=int, default=RACINE_ESSAI_TENUE)
    dc = sp.add_parser("decision", help="racine de décision : exige le préenregistrement scellé")
    dc.add_argument("--prereg", required=True)
    dc.add_argument("--instances", required=True)
    dc.add_argument("--run-id", required=True)
    dc.add_argument("--processus", type=int, default=2)
    a = ap.parse_args(argv)
    if a.mode == "essai":
        exiger_racines_essai(a.racine, a.racine_tenue)
        sortie = Path(a.sortie)
        if sortie.exists():
            raise GardeArret(f"{sortie} existe déjà : R12 interdit d'écraser")
        res, temps = executer(_plage(a.instances), a.racine, a.racine_tenue, CONFIG_V1, a.processus)
        corps = {"mode": "essai", "manifeste": {"racine": a.racine, "racine_tenue": a.racine_tenue,
                                                "schema_graines": "SeedSequence(entropy=racine, spawn_key=(code_delta, "
                                                                  "instance, code_bras, tour, role, ...))",
                                                "config": asdict(CONFIG_V1), "config_sha256": CONFIG_V1.empreinte(),
                                                "versions": _versions(), "commande": " ".join(sys.argv)},
                 "temps": temps, "analyse": analyser(res, a.racine), "resultats": res}
        sortie.write_text(json.dumps(corps, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
        print(f"essai écrit : {sortie} ; {temps}")
        return 0
    # décision : le préenregistrement scellé est exigé AVANT toute graine de décision
    sha = exiger_prereg_arene(a.prereg)
    from controle_ia import manifeste as man

    chemin_m, _ = man.creer_manifeste(DEPOT, a.run_id, {"config": asdict(CONFIG_V1), "racine": RACINE,
                                                        "racine_tenue": RACINE_TENUE, "instances": a.instances,
                                                        "prereg_sha256": sha, "versions": _versions()},
                                      ["arene"], entropie=RACINE, decisif=True, prereg=a.prereg,
                                      commande=" ".join(sys.argv))
    res, temps = executer(_plage(a.instances), RACINE, RACINE_TENUE, CONFIG_V1, a.processus)
    man.ecrire_resultat(DEPOT, chemin_m, "resultats-arene", {"temps": temps, "resultats": res})
    man.ecrire_resultat(DEPOT, chemin_m, "analyse-arene", analyser(res, RACINE))
    print(f"run de décision écrit sous diag/{a.run_id}/")
    return 0


__all__ = ["Config", "CONFIG_V1", "RACINE", "RACINE_TENUE", "RACINE_ESSAI", "RACINE_ESSAI_TENUE", "executer_tache",
           "analyser", "resoudre_jeu", "meilleure_reponse", "exiger_prereg_arene", "exiger_identite_prereg",
           "exiger_racines_essai", "replace"]

if __name__ == "__main__":
    sys.exit(main())

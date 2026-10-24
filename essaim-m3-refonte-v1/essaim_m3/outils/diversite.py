"""Étages M3 (mitose) et M2 (répulsion d'Onsager, neuromodulation) : les calculs, rendus réels.

Ce que faisait le script de Gemini et ce qui est corrigé :
- B-10 « mitose spectrale Cholesky-DPP jusqu'au seuil de Marchenko-Pastur » : un déterminant de Gram régularisé et
  deux seuils magiques (0,6321 ; 0,14) sur la plus petite valeur propre, qui tombaient à zéro dès que deux cellules
  étaient des chaînes d'erreur identiques. Ici, la nouveauté d'une cellule est le résidu orthogonal de son plongement
  sur l'espace engendré par les cellules précédentes, et l'arrêt compare ce résidu à un **nul de permutation**
  (cellules de bruit obtenues en mélangeant les jetons entre cellules). Le seuil de Marchenko-Pastur suppose des
  vecteurs gaussiens i.i.d., ce que des plongements creux hachés ne sont pas : il est abandonné, et dit tel quel.
- B-11 « réaction de cavité d'Onsager » = carré de la similarité moyenne : ici le champ de cavité d'une cellule est
  son résidu orthogonal ; le terme de réaction est la fraction de sa norme expliquée par les autres cellules.
- B-12 « neuromodulation de Yu-Dayan » codée en dur (ACh croissait avec le numéro d'étape) : ici ACh (incertitude
  attendue) est la moyenne glissante des résidus, NE (incertitude inattendue) une statistique de rupture (CUSUM) sur
  la suite des résidus ; les deux pilotent le nombre de sondes « tunnel » et l'angle d'exploration, et sont
  consignées. Ce sont des heuristiques, nommées comme telles.
- B-29 / constats 9 et 38 : le routage des attaquants (« matrice de prédation ») devient un bandit par défenseur,
  ε-glouton avec exploration minimale, bris d'égalité aléatoire, graine dérivée (R9).
- B-30 / constats 10 et 37 : la récompense « anti-échec » unilatérale est bornée (μ projeté sur [0, 1]) et le terme
  de coût dépend du bras.
"""
from __future__ import annotations

import math

import numpy as np

from .plongement import Plongeur, jetons


# ---------- résidus orthogonaux (champ de cavité) ----------

def residu_orthogonal(v: np.ndarray, base: np.ndarray) -> float:
    """Norme du résidu de `v` (norme 1 attendue) après projection sur l'espace engendré par les lignes de `base`."""
    if base is None or len(base) == 0:
        return float(np.linalg.norm(v))
    q, _ = np.linalg.qr(base.T, mode="reduced")
    r = v - q @ (q.T @ v)
    return float(np.linalg.norm(r))


def residus_sequentiels(vecs: np.ndarray) -> list[float]:
    """Résidu de chaque cellule par rapport à celles qui la précèdent."""
    return [residu_orthogonal(vecs[i], vecs[:i]) for i in range(len(vecs))]


def fraction_expliquee(v: np.ndarray, base: np.ndarray) -> float:
    """Terme de réaction (nom gardé de Gemini) : part de `v` expliquée par les autres cellules, dans [0, 1]."""
    n = float(np.linalg.norm(v))
    if n == 0:
        return 0.0
    return max(0.0, min(1.0, 1.0 - (residu_orthogonal(v, base) / n) ** 2))


def log_det_gram(vecs: np.ndarray) -> float:
    if len(vecs) == 0:
        return 0.0
    g = vecs @ vecs.T
    signe, ld = np.linalg.slogdet(g + 1e-9 * np.eye(len(vecs)))
    return float(ld) if signe > 0 else float("-inf")


# ---------- nul de permutation pour l'arrêt de la mitose ----------

def cellules_de_bruit(textes: list[str], rng: np.random.Generator, n: int) -> list[str]:
    """Cellules de bruit : mêmes jetons, redistribués au hasard entre `n` cellules (structure détruite)."""
    tous = [j for t in textes for j in jetons(t)]
    if not tous:
        return [""] * n
    melange = list(tous)
    rng.shuffle(melange)
    tailles = [len(jetons(t)) for t in textes] or [len(tous)]
    sortie = []
    pos = 0
    for i in range(n):
        taille = tailles[i % len(tailles)]
        morceau = melange[pos:pos + taille]
        if not morceau:
            morceau = melange[:taille]
        pos = (pos + taille) % max(1, len(melange))
        sortie.append(" ".join(morceau))
    return sortie


def seuil_nouveaute_permutation(textes: list[str], plongeur: Plongeur, rng: np.random.Generator,
                                n_permutations: int = 100, quantile: float = 0.95) -> float:
    """Quantile du résidu d'une cellule de bruit ajoutée aux cellules réelles : en dessous, une cellule n'apporte
    pas plus qu'un mélange de ce qui existe déjà."""
    if len(textes) < 2:
        return 0.0
    base = plongeur.matrice(textes)
    residus = []
    for _ in range(n_permutations):
        bruit = cellules_de_bruit(textes, rng, 1)[0]
        residus.append(residu_orthogonal(plongeur.vecteur(bruit), base))
    return float(np.quantile(residus, quantile))


def arret_mitose(residus_reels: list[float], seuil: float, k: int = 2, minimum: int = 3) -> bool:
    """Arrêt quand les `k` dernières cellules valides ne dépassent pas le seuil de bruit, après `minimum` cellules."""
    if len(residus_reels) < max(minimum, k):
        return False
    return all(r <= seuil for r in residus_reels[-k:])


# ---------- neuromodulation (heuristique nommée Yu-Dayan par Gemini) ----------

class Neuromodulateur:
    """ACh = incertitude attendue (moyenne glissante des résidus) ; NE = incertitude inattendue (CUSUM normalisée)."""

    def __init__(self, oubli: float = 0.3, seuil_cusum: float = 1.0):
        self.oubli = float(oubli)
        self.seuil = float(seuil_cusum)
        self.ach = None
        self.cusum = 0.0
        self.historique: list[dict] = []

    def observer(self, residu: float) -> dict:
        if self.ach is None:
            self.ach = float(residu)
            ecart = 0.0
        else:
            ecart = float(residu) - self.ach
            self.ach = (1 - self.oubli) * self.ach + self.oubli * float(residu)
        self.cusum = max(0.0, self.cusum + abs(ecart) - 0.05)
        ne = min(1.0, self.cusum / self.seuil)
        etat = {"residu": float(residu), "ACh_incertitude_attendue": round(self.ach, 4),
                "NE_incertitude_inattendue": round(ne, 4), "sondes_tunnel": int(round(2 * ne))}
        self.historique.append(etat)
        return etat


# ---------- bandit de prédation (routage des attaquants) ----------

def epsilon_t(t: int, n_bras: int, eps_min: float = 0.05) -> float:
    return max(eps_min, min(1.0, math.sqrt(n_bras * math.log(max(2, t)) / max(1, t))))


class BanditPredation:
    """Un bandit par défenseur : quel attaquant router vers lui. ε-glouton, graine dérivée, bris d'égalité aléatoire."""

    def __init__(self, bras: list[str], rng: np.random.Generator, eps_min: float = 0.05, regle: str = "epsilon-glouton",
                 temperature_softmax: float = 0.5):
        self.bras = list(bras)
        self.rng = rng
        self.eps_min = float(eps_min)
        self.regle = regle
        self.temperature = float(temperature_softmax)
        self.n = {b: 0 for b in self.bras}
        self.q = {b: 0.0 for b in self.bras}
        self.t = 0
        self.trace: list[dict] = []

    def choisir(self) -> str:
        self.t += 1
        if self.regle == "softmax":
            z = np.array([self.q[b] / max(1e-6, self.temperature) for b in self.bras])
            p = np.exp(z - z.max())
            p /= p.sum()
            choix = str(self.rng.choice(self.bras, p=p))
            eps = None
        elif self.regle == "uniforme":
            choix = str(self.rng.choice(self.bras))
            eps = 1.0
        else:
            eps = epsilon_t(self.t, len(self.bras), self.eps_min)
            if self.rng.random() < eps:
                choix = str(self.rng.choice(self.bras))
            else:
                meilleur = max(self.q.values())
                egaux = [b for b in self.bras if self.q[b] == meilleur]
                choix = str(self.rng.choice(egaux))
        self.trace.append({"t": self.t, "choix": choix, "epsilon": eps, "q": dict(self.q)})
        return choix

    def recompenser(self, bras: str, recompense: float):
        self.n[bras] += 1
        self.q[bras] += (float(recompense) - self.q[bras]) / self.n[bras]


def recompense_anti_echec(mu: float, y: int, cout: float = 0.0, gamma: float = 0.0) -> float:
    """R = y(1 − (μ − 1)²) − (1 − y)μ² − γ·coût, avec μ projeté sur [0, 1] : un échec ne rapporte jamais plus que 0."""
    mu = min(1.0, max(0.0, float(mu)))
    y = 1 if y else 0
    return y * (1.0 - (mu - 1.0) ** 2) - (1 - y) * mu ** 2 - float(gamma) * float(cout)

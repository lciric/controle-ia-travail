"""Noyaux et gloutons gardés (§ 4, « Glouton nouveau glouton_paires », CB-03). Aucun `except` dans ce module.

- `cholesky`, `NonDefiniePositive`, `noyau_fautif`, `noyau_corrige` : pièce A, `orchestrateur-pole-v7/pole/recombinaison.py`
  (71faad38…), importée telle quelle (`cholesky` lève sur tout pivot non strictement positif).
- `glouton_paires(L, k)` : décomposition de tout le noyau par `cholesky` de la pièce A, puis Cholesky incrémentale ;
  lève `NonDefiniePositive` si le pivot choisi est ≤ 1e-12 × max(diagonale) ; ni saut, ni sortie anticipée.
- `ordre_glouton_garde(l)` : copie gardée de `methodes_v1.ordre_glouton` (2f7a8b11…), numériquement identique tant
  que le pivot choisi reste > 0, qui lève sinon (au lieu de borner le pivot à 1e-300) ; décomposition préalable de
  tout le noyau par `cholesky` de la pièce A.
"""
import math
import sys
from pathlib import Path

import numpy as np

_POLE = Path(__file__).resolve().parent.parent.parent / "orchestrateur-pole-v7"
if str(_POLE) not in sys.path:
    sys.path.append(str(_POLE))
from pole.recombinaison import NonDefiniePositive, cholesky, noyau_corrige, noyau_fautif  # noqa: E402,F401

GAMMA = 1e-3
SEUIL_PIVOT_RELATIF = 1e-12


def glouton_paires(L, k):
    """Sélection gloutonne du déterminant maximal (Chen, Zhang et Zhou 2018, de mémoire, R7). Rend
    (indices choisis, nombre de candidats distincts rencontrés à pivot ≤ 0)."""
    L = np.asarray(L, dtype=float)
    cholesky(L.tolist())  # pièce A : lève NonDefiniePositive si le noyau entier n'est pas défini positif
    m = L.shape[0]
    d2 = np.diag(L).copy()
    seuil = SEUIL_PIVOT_RELATIF * float(d2.max())
    lignes = np.zeros((0, m))
    choisis, pris = [], np.zeros(m, dtype=bool)
    non_positifs = set()
    for _ in range(min(k, m)):
        restants = np.flatnonzero(~pris)
        non_positifs.update(int(i) for i in restants[d2[restants] <= 0])
        j = int(restants[np.argmax(d2[restants])])  # premier indice en cas d'égalité
        if not d2[j] > seuil:
            raise NonDefiniePositive(f"pivot choisi {d2[j]:.3e} ≤ {seuil:.3e}")
        e = (L[j, :] - lignes[:, j] @ lignes) / math.sqrt(d2[j])
        lignes = np.vstack([lignes, e])
        d2 = d2 - e ** 2
        choisis.append(j)
        pris[j] = True
    return choisis, len(non_positifs)


def ordre_glouton_garde(l):
    """Copie gardée de methodes_v1.ordre_glouton sur un noyau donné `l` (liste de listes n × n)."""
    n = len(l)
    cholesky(l)  # pièce A
    d2 = [l[i][i] for i in range(n)]
    lignes, ordre, pris = [], [], set()
    j = max(range(n), key=lambda i: d2[i])
    while True:
        if not d2[j] > 0:
            raise NonDefiniePositive(f"pivot choisi {d2[j]:.3e} ≤ 0 (copie gardée de ordre_glouton)")
        ordre.append(j)
        pris.add(j)
        if len(ordre) == n:
            return ordre
        dj = math.sqrt(d2[j])
        e = [(l[j][i] - sum(c[j] * c[i] for c in lignes)) / dj for i in range(n)]
        lignes.append(e)
        for i in range(n):
            d2[i] -= e[i] ** 2
        j = max((i for i in range(n) if i not in pris), key=lambda i: d2[i])


def noyau_v1(cos, q):
    """Noyau de methodes_v1.ordre_glouton : L = diag(q)(cos² + γ I)diag(q), construit à l'identique."""
    n = len(cos)
    return [[q[i] * q[j] * (cos[i][j] ** 2 + (GAMMA if i == j else 0.0)) for j in range(n)] for i in range(n)]

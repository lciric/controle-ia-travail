"""Brique C, lecture, version 2 : erratum de code demandé par les décisions du concepteur des sondes v2
(`docs/notes/sondes-v2-concepteur-opus-v1/decisions-concepteur-sondes-v2-v2.md`, cb270590…, § 1 et § 7, points 1 et
2), lues avec leur erratum 1 (019cff39…, qui prime). `lecture_v1.py` reste tel quel (R12) ; ce module en reprend tout,
sauf trois points :

- **Q10** : `lecture_signee` lit « établie » si p au-dessus ≤ α, « contraire » si p au-dessous ≤ α (« au plus le
  seuil », comme les lignes du texte scellé).
- **E-5** : `contraste_apparie` n'est qu'une description. Son changement de signe sur les unités n'est pas valide comme
  test : la sonde de l'unité u apprend sur les autres unités, donc sur leurs écarts propres, et deux unités partagent
  un terme sur P − 1 ; sous l'hypothèse nulle, la variance de leur moyenne est voisine du double, d'où vers 12 % de
  rejets au lieu de 5 % en unilatéral. Aucune fonction ne tire un libellé de sa valeur p.
- **Le test du contraste** est le nul de réétiquetage qui échange d'un bloc les deux étiquettes de chaque paire de
  poids et rejoue toute la sélection (`nul_reetiquetage`), unilatéral vers le haut. **Ce qu'il rejette** :
  l'échangeabilité du saboteur et du jumeau dans chaque paire, non « l'absence de trace commune » ; un écart
  d'intensité commun ou une interaction le font aussi rejeter. Plancher : l'échange simultané de toutes les paires
  laisse l'aire presque inchangée, l'observé et son image comptent deux fois, d'où une plus petite valeur p voisine de
  2/2^P ; avec R rejeux tirés, elle ne descend pas sous 1/(1 + R). Règle : « non testable à cet effectif » si
  max(2^(1−P), 1/(1 + R)) > α (`contraste_testable`) ; plafond de puissance sous un effet infini :
  `plafond_puissance_contraste`.
"""
from __future__ import annotations

import math

from scipy.stats import binom

from . import lecture_v1 as _v1
from .lecture_v1 import *  # noqa: F401,F403 — tout ce qui ne change pas

MENTION_DESCRIPTIF = "descriptif : changement de signe non valide comme test (plis à apprentissage partagé)"
CE_QUE_REJETTE_LE_CONTRASTE = ("l'échangeabilité du saboteur et du jumeau dans chaque paire, non l'absence de trace "
                               "commune ; un écart d'intensité commun ou une interaction le font aussi rejeter")


def lecture_signee(test: dict, alpha: float) -> str:
    """« établie » si p au-dessus ≤ α ; « contraire » si p au-dessous ≤ α ; « non établie » sinon (Q10, corrigé)."""
    if test["p_au_dessus"] <= alpha:
        return "établie"
    if test["p_au_dessous"] <= alpha:
        return "contraire"
    return "non établie"


def contraste_testable(n_paires: int, n_rejeux: int, alpha: float) -> bool:
    """Faux si max(2^(1−P), 1/(1 + R)) > α (décisions v2, § 1)."""
    return max(2.0 ** (1 - n_paires), 1.0 / (1 + n_rejeux)) <= alpha


def lecture_contraste(p: float, n_paires: int, n_rejeux: int, alpha: float) -> str:
    """Libellé du contraste apparié lu sur le nul par échange d'un bloc (valeur p unilatérale vers le haut)."""
    if not contraste_testable(n_paires, n_rejeux, alpha):
        return "non testable à cet effectif"
    return "établie" if p <= alpha else "non établie à cette puissance"


def plafond_puissance_contraste(n_paires: int, n_rejeux: int, alpha: float) -> dict:
    """Plafond de la puissance du contraste lu sur R rejeux tirés, sous un effet infini (calcul analytique du concepteur,
    `calculs/plafonds_puissance_contraste_v1.py`) : b, le nombre de rejeux qui atteignent l'aire observée, suit une loi
    binomiale (R, q), q = 2^(1−P) si l'image de l'observé compte, 2^(−P) sinon ; lecture si b ≤ α(1 + R) − 1."""
    k = math.floor(alpha * (1 + n_rejeux) - 1 + 1e-9)

    def plafond(q):
        return 0.0 if k < 0 else float(binom.cdf(k, n_rejeux, q))

    return {"paires": n_paires, "rejeux": n_rejeux, "alpha": alpha,
            "testable": contraste_testable(n_paires, n_rejeux, alpha),
            "plafond_image_comptee": plafond(2.0 ** (1 - n_paires)),
            "plafond_image_non_comptee": plafond(2.0 ** (-n_paires))}


def contraste_apparie(scores: dict, jeu, unites, rng=None) -> dict:
    """Description seulement (E-5) : aire par unité entre ses lignes positives et négatives, moins 0,5, et changement
    de signe sur les unités, rapporté avec la mention `MENTION_DESCRIPTIF`. Le test est `nul_reetiquetage` par paire
    de poids ; il rejette `CE_QUE_REJETTE_LE_CONTRASTE`."""
    r = _v1.contraste_apparie(scores, jeu, unites, rng)
    return {"aires_par_unite": r["aires_par_unite"], "description": r["test"], "nature": MENTION_DESCRIPTIF}


__all__ = list(_v1.__all__) + ["contraste_testable", "lecture_contraste", "plafond_puissance_contraste",
                               "MENTION_DESCRIPTIF", "CE_QUE_REJETTE_LE_CONTRASTE"]

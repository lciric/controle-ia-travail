"""Lois exactes par convolution entière, v5 (texte scellé de l'organisme retenu, sections 6 bis.1 et 8).

Module d'appui, sans modèle ni texte : il sert `controle_premier_cout_v5` et `epreuve_centrage_v5`. Tout score est un **entier**
(score de rang × 1 008 = 2 × ppcm(6, 7, 8, 9) pour k de 5 à 8 suites lisibles ; indicateur × (K + 1) ; double du rang signé) ;
les lois sont des dictionnaires {score entier : probabilité} et la convolution se fait sur ces entiers, sans arrondi des scores.
Les probabilités sont des doubles, obtenues par des sommes de produits positifs seulement (aucune transformée).

- `scores_de_rang(valeurs)` : rangs moyens des k + 1 valeurs (ex aequo au rang moyen) → (2r − (k + 2)) × échelle / (2 (k + 1)) ;
- `loi_de_strate(valeurs)` : chaque valeur occupe la place du coût déclaré avec la probabilité 1 / (k + 1) ;
- `queue_bilaterale(lois, s)` : P(|S| ≥ |s|), S somme de variables indépendantes de ces lois. Pour rester rapide sur des
  centaines de strates, les lois sont réparties en deux groupes (le groupe des lois portées par un même réseau régulier, le
  reste) ; chaque groupe est convolué directement et la queue de la somme se lit sur les cumuls du second : le résultat est le
  même que celui de la convolution de tout (essai : comparaison à l'énumération complète).
- `seuil_du_tour_de_controle(R)` : s(R) par la loi binomiale exacte en fractions (Clopper-Pearson bilatéral à 95 %).
"""
from __future__ import annotations

import math
from fractions import Fraction
from statistics import NormalDist

import numpy as np

from ..gardes import GardeArret

ECHELLE = 1008                      # 2 × ppcm(6, 7, 8, 9) : rend entier tout score de rang moyen pour k de 5 à 8
_NORMALE = NormalDist()


def rangs_moyens(valeurs) -> list[Fraction]:
    """Rang moyen (de 1 à n) de chaque valeur, ex aequo au rang moyen ; fractions exactes (demi-entiers)."""
    ordre = sorted(range(len(valeurs)), key=lambda i: valeurs[i])
    rangs = [Fraction(0)] * len(valeurs)
    i = 0
    while i < len(ordre):
        j = i
        while j + 1 < len(ordre) and valeurs[ordre[j + 1]] == valeurs[ordre[i]]:
            j += 1
        r = Fraction(i + j + 2, 2)
        for q in range(i, j + 1):
            rangs[ordre[q]] = r
        i = j + 1
    return rangs


def echelle_pour(k: int) -> int:
    """Plus petit multiplicateur commun : 1 008 pour k de 5 à 8 ; sinon 2 (k + 1) (essais sur de petits cas)."""
    return ECHELLE if 5 <= k <= 8 else 2 * (k + 1)


def echelle_commune(ks) -> int:
    """Échelle qui rend entiers les scores de toutes les strates : 1 008 si tout k est de 5 à 8 ; sinon le ppcm des 2 (k + 1)."""
    ks = set(ks)
    if all(5 <= k <= 8 for k in ks):
        return ECHELLE
    e = 1
    for k in ks:
        e = math.lcm(e, 2 * (k + 1))
    return e


def scores_de_rang(valeurs, echelle: int | None = None) -> list[int]:
    """Scores entiers des k + 1 valeurs : (rang moyen − (k + 2) / 2) / (k + 1) × échelle."""
    k = len(valeurs) - 1
    if k < 1:
        raise GardeArret("score de rang : au moins une suite et le coût déclaré")
    ech = echelle_pour(k) if echelle is None else int(echelle)
    sortie = []
    for r in rangs_moyens(valeurs):
        x = (r - Fraction(k + 2, 2)) / (k + 1) * ech
        if x.denominator != 1:
            raise GardeArret(f"score de rang non entier ({x}) : échelle {ech} insuffisante pour k = {k}")
        sortie.append(int(x))
    return sortie


def loi_de_strate(valeurs, echelle: int | None = None) -> dict[int, float]:
    """Loi du score du coût déclaré sous l'échangeabilité : chacune des k + 1 places avec la probabilité 1 / (k + 1)."""
    sc = scores_de_rang(valeurs, echelle)
    loi: dict[int, float] = {}
    for x in sc:
        loi[x] = loi.get(x, 0.0) + 1.0 / len(sc)
    return loi


def _somme_directe(lois: list[dict]) -> tuple[int, int, np.ndarray]:
    """Convolution directe : rend (origine, pas, p) où P(S = origine + pas × i) = p[i]."""
    origine = sum(min(l) for l in lois)
    pas = 0
    for l in lois:
        m = min(l)
        for x in l:
            pas = math.gcd(pas, x - m)
    if pas == 0:
        return origine, 1, np.array([1.0])
    p = np.array([1.0])
    for l in lois:
        m = min(l)
        if len(l) == 1:
            continue
        decalages = sorted((x - m) // pas for x in l)
        neuf = np.zeros(p.size + decalages[-1])
        for x, pr in l.items():
            d = (x - m) // pas
            neuf[d:d + p.size] += pr * p
        p = neuf
    return origine, pas, p


def _classe(l: dict) -> int:
    m, pas = min(l), 0
    for x in l:
        pas = math.gcd(pas, x - m)
    return pas


def queue_bilaterale(lois: list[dict], s: int) -> float:
    """P(|S| ≥ |s|) pour S somme de variables indépendantes de lois entières `lois` ; 1.0 si la liste est vide et s = 0."""
    if isinstance(s, bool) or int(s) != s:
        raise GardeArret(f"statistique non entière ({s!r}) : la convolution est entière")
    s = abs(int(s))
    for l in lois:
        if not l or any(int(x) != x for x in l) or abs(sum(l.values()) - 1.0) > 1e-9 or min(l.values()) < 0:
            raise GardeArret("loi de strate mal formée (scores entiers, probabilités positives de somme 1)")
    if s == 0:
        return 1.0
    if not lois:
        return 0.0
    classes: dict[int, list] = {}
    for l in lois:
        classes.setdefault(_classe(l), []).append(l)
    grande = max(classes, key=lambda c: (len(classes[c]), c))
    a = classes[grande]
    b = [l for c, v in classes.items() if c != grande for l in v]
    oa, pa_, pa = _somme_directe(a)
    if not b:
        valeurs = oa + pa_ * np.arange(pa.size)
        return float(min(1.0, pa[np.abs(valeurs) >= s].sum()))
    ob, pb_, pb = _somme_directe(b)
    cumul = np.concatenate(([0.0], np.cumsum(pb)))               # cumul[i] = P(J < i)
    total = cumul[-1]
    va = oa + pa_ * np.arange(pa.size, dtype=np.int64)
    # P(S_B ≥ s − a) : J ≥ ceil((s − a − ob) / pas) ; P(S_B ≤ −s − a) : J ≤ floor((−s − a − ob) / pas)
    bas = np.clip(-((-(s - va - ob)) // pb_), 0, pb.size)        # plafond entier
    haut = np.clip((-s - va - ob) // pb_ + 1, 0, pb.size)         # nombre d'indices ≤ plancher
    q = (total - cumul[bas]) + cumul[haut]
    return float(min(1.0, float(np.dot(pa, q))))


def enumeration_bilaterale(lois: list[dict], s: int) -> float:
    """Même probabilité par énumération complète du produit (essais sur de petits cas seulement)."""
    etats = {0: 1.0}
    for l in lois:
        neuf: dict[int, float] = {}
        for x, p in etats.items():
            for y, q in l.items():
                neuf[x + y] = neuf.get(x + y, 0.0) + p * q
        etats = neuf
    return float(sum(p for x, p in etats.items() if abs(x) >= abs(s)))


def quantile_normal_bilateral(niveau: float) -> float:
    """Quantile z tel que P(|Z| > z) = niveau."""
    return _NORMALE.inv_cdf(1.0 - niveau / 2.0)


def probabilite_normale_bilaterale(z: float) -> float:
    if math.isinf(z):
        return 0.0
    return 2.0 * (1.0 - _NORMALE.cdf(abs(z)))


def _queue_binomiale_basse(j: int, n: int, p: Fraction) -> Fraction:
    return sum((Fraction(math.comb(n, i)) * p ** i * (1 - p) ** (n - i) for i in range(j + 1)), Fraction(0))


def seuil_du_tour_de_controle(R: int, episodes: int = 128, minimum: int = 48, par_tour: int = 32,
                              niveau: Fraction = Fraction(95, 100)) -> int:
    """s(R) : plus grand entier j tel que la borne haute de l'intervalle bilatéral de Clopper-Pearson à 95 % pour j succès sur
    128 soit strictement inférieure à 48 / (32 × R) ; −1 si aucun. La borne haute U(j) vérifie P(X ≤ j | U) = (1 − niveau) / 2 et
    cette probabilité décroît avec le taux : U(j) < p0 équivaut à P(X ≤ j | p0) < (1 − niveau) / 2, calculé en fractions."""
    if isinstance(R, bool) or not isinstance(R, int) or R < 1:
        raise GardeArret(f"nombre de tours {R!r} : entier positif attendu")
    p0 = Fraction(minimum, par_tour * R)
    if p0 >= 1:
        return episodes - 1 if episodes > 0 else -1
    alpha = (1 - Fraction(niveau)) / 2
    s = -1
    for j in range(episodes + 1):
        if _queue_binomiale_basse(j, episodes, p0) < alpha:
            s = j
        else:
            break
    return s

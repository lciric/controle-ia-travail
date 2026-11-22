"""Outils communs des calculs d'appui du concepteur — batterie de fuite de la banque révisée (mathématiques nouvelles).

Calculs d'appui écrits par le concepteur pour éprouver ses formules (mandat : « processeur seul si tu veux éprouver
une formule »). Ce n'est pas l'instrument : le code de la batterie revient à Opus et sera contre-lu. Aucun appel de
modèle, aucun réseau, aucune dépense.
"""
from __future__ import annotations

from fractions import Fraction

import numpy as np

PLAFOND_FA = Fraction(1, 10)
RACINE_DES_BORNES = 20261122  # bornes hautes : SeedSequence(RACINE_DES_BORNES, spawn_key=(enfant,))


def _comptes(scores):
    c = {}
    for s in scores:
        c[s] = c.get(s, 0) + 1
    return c


def rappel_au_prorata(scores_vrais, scores_ensemble, plafond=PLAFOND_FA):
    """Rappel sur `scores_ensemble` au point où la part des vrais déclarés « faux » vaut exactement `plafond`.

    Les valeurs de score sont parcourues de la plus haute à la plus basse ; toutes les pièces d'une même valeur forment
    un bloc. Un bloc est pris en entier tant que la part cumulée des vrais reste <= plafond ; le bloc qui franchirait le
    plafond est compté au prorata de la part de vrais qui reste à prendre. Aucun tirage. Rend une Fraction, ou None si
    l'un des deux ensembles est vide (« non calculable »)."""
    nv, ne = len(scores_vrais), len(scores_ensemble)
    if nv == 0 or ne == 0:
        return None
    cv, ce = _comptes(scores_vrais), _comptes(scores_ensemble)
    fa, rappel = Fraction(0), Fraction(0)
    for s in sorted(set(cv) | set(ce), reverse=True):
        dfa = Fraction(cv.get(s, 0), nv)
        dr = Fraction(ce.get(s, 0), ne)
        if fa + dfa <= plafond:
            fa += dfa
            rappel += dr
            continue
        return rappel + (plafond - fa) / dfa * dr  # dfa > 0 ici
    return rappel


def rappel_bloc_entier(scores_vrais, scores_ensemble, plafond=PLAFOND_FA):
    """Règle du rapprochement (« bloc d'ex æquo jamais franchi ») : on s'arrête avant le bloc qui franchirait le plafond.
    Gardée pour comparaison seulement."""
    nv, ne = len(scores_vrais), len(scores_ensemble)
    if nv == 0 or ne == 0:
        return None
    cv, ce = _comptes(scores_vrais), _comptes(scores_ensemble)
    fa, rappel = Fraction(0), Fraction(0)
    for s in sorted(set(cv) | set(ce), reverse=True):
        dfa = Fraction(cv.get(s, 0), nv)
        if fa + dfa > plafond:
            return rappel
        fa += dfa
        rappel += Fraction(ce.get(s, 0), ne)
    return rappel


def borne_haute(valeurs, enfant, tirages=2000, racine=RACINE_DES_BORNES):
    """Borne haute de l'intervalle à 90 % de la moyenne, par rééchantillonnage des racines : 95e centile (interpolation
    linéaire de numpy) de `tirages` moyennes rééchantillonnées avec remise. None si une valeur manque."""
    if len(valeurs) == 0 or any(v is None for v in valeurs):
        return None
    v = np.asarray([float(x) for x in valeurs], float)
    if not np.all(np.isfinite(v)):
        return None
    rng = np.random.default_rng(np.random.SeedSequence(racine, spawn_key=(int(enfant),)))
    idx = rng.integers(0, len(v), size=(tirages, len(v)))
    return float(np.quantile(v[idx].mean(axis=1), 0.95))


def hors_de_la_plage(valeur, valeurs_des_racines) -> bool:
    """Relecture de la banque réelle : vrai si la valeur est strictement au-dessus du maximum ou strictement au-dessous du
    minimum des valeurs vues sur les racines neuves. Valeur non calculable : hors de la plage."""
    if valeur is None or not valeurs_des_racines or any(v is None for v in valeurs_des_racines):
        return True
    return valeur > max(valeurs_des_racines) or valeur < min(valeurs_des_racines)


def score_apparie(n10, n01, n, d0):
    """Score apparié du brouillon 4 du préenregistrement (§ Plan d'analyse)."""
    A = 2 * n
    Bq = -n10 - n01 + (2 * n - n10 + n01) * d0
    C = -n01 * d0 * (1 - d0)
    q = (max(Bq * Bq - 4 * A * C, 0.0) ** 0.5 - Bq) / (2 * A)
    den = (n * (2 * q + d0 * (1 - d0))) ** 0.5
    return (n10 - n01 - n * d0) / den if den > 0 else 0.0

"""M3 à M6 — test des rangs signés exact (méthode de Pratt), procédure de Holm, règle de validité unilatérale, lecture.

- Rangs : les valeurs absolues des différences, zéros compris, reçoivent leur rang, les ex æquo le rang moyen ; les rangs des
  zéros sont ensuite retirés. Statistique : somme des rangs des différences positives.
- Loi exacte, sous l'échange des signes des différences non nulles, par programmation dynamique sur les rangs doublés (entiers).
- Valeur p bilatérale : double de la plus petite des deux queues, bornée à un ; un si toutes les différences sont nulles.
- Holm : la plus petite des deux valeurs p contre 0,025 ; si elle passe, l'autre contre 0,05.
- Règle de validité (M6) : unilatérale, queue des grandes sommes de rangs positifs, seuil 0,05, sans correction.

Verrou d'étalonnage (garde 22) : tant que `VERROU_ETALONNAGE` est levé, tout appel au test lève.
"""

import functools

import numpy as np

VERROU_ETALONNAGE = {"leve": False}


class TestVerrouille(RuntimeError):
    pass


def _verifier_verrou():
    if VERROU_ETALONNAGE["leve"]:
        raise TestVerrouille("garde 22 : appel au test pendant l'étalonnage : interdit")


def rangs_doubles_pratt(d):
    """(rangs doublés des différences non nulles, signes positifs) ; ex æquo au rang moyen ; zéros classés puis retirés."""
    d = np.asarray(d, dtype=float)
    a = np.abs(d)
    n = len(a)
    ordre = np.argsort(a, kind="mergesort")
    tries = a[ordre]
    rangs2 = np.empty(n, dtype=np.int64)
    i = 0
    while i < n:
        j = i
        while j + 1 < n and tries[j + 1] == tries[i]:
            j += 1
        rangs2[ordre[i:j + 1]] = (i + 1) + (j + 1)  # deux fois le rang moyen (i+1 .. j+1)
        i = j + 1
    non_nuls = d != 0
    return rangs2[non_nuls], d[non_nuls] > 0


@functools.lru_cache(maxsize=200_000)
def _loi_exacte(rangs2_tries):
    """Comptes des sous-ensembles par somme de rangs doublés : tableau de longueur Σ + 1 (entiers exacts)."""
    total = int(sum(rangs2_tries))
    c = np.zeros(total + 1, dtype=np.int64)
    c[0] = 1
    haut = 0
    for r in rangs2_tries:
        c[r:haut + r + 1] += c[0:haut + 1].copy()
        haut += r
    queue_haute = np.cumsum(c[::-1])[::-1]  # P(T ≥ t) × 2^n
    queue_basse = np.cumsum(c)  # P(T ≤ t) × 2^n
    return queue_haute, queue_basse, len(rangs2_tries)


def statistiques(d):
    """(somme des rangs doublés positifs, somme des rangs doublés négatifs, rangs doublés triés)."""
    r2, pos = rangs_doubles_pratt(d)
    return int(r2[pos].sum()), int(r2[~pos].sum()), tuple(sorted(int(x) for x in r2))


def valeur_p_bilaterale(d):
    _verifier_verrou()
    tp, tn, r2 = statistiques(d)
    if not r2:
        return 1.0
    haute, basse, n = _loi_exacte(r2)
    p = 2.0 * min(haute[tp], basse[tp]) / float(2 ** n)
    return min(1.0, p)


def valeur_p_unilaterale(d):
    """Queue des grandes sommes de rangs positifs : P(T⁺ ≥ t⁺)."""
    _verifier_verrou()
    tp, tn, r2 = statistiques(d)
    if not r2:
        return 1.0
    haute, basse, n = _loi_exacte(r2)
    return float(haute[tp]) / float(2 ** n)


def holm(p_heritage, p_tenue, alpha=0.05):
    """Rend (passe_heritage, passe_tenue) sous la procédure de Holm à deux contrastes."""
    if p_heritage <= p_tenue:
        premier = p_heritage <= alpha / 2
        return premier, premier and p_tenue <= alpha
    premier = p_tenue <= alpha / 2
    return premier and p_heritage <= alpha, premier


def condition_lois_fausses(diff_fausses_tenues, diff_m1):
    """M5 : la médiane de la différence des lois fausses tenues ne dépasse pas une loi et reste strictement inférieure à la
    médiane de la différence de M1."""
    mf, mv = float(np.median(diff_fausses_tenues)), float(np.median(diff_m1))
    return mf <= 1.0 and mf < mv


def lecture_contraste(passe_holm, d_m1, d_fausses):
    """Table de l'étape 2 du § 8.3 du plan : « établi », « non lu comme succès », « effet négatif établi », « égalité » (somme nulle
    alors que la procédure passe, rapportée sans lecture) ou « non établi »."""
    if not passe_holm:
        return "non établi"
    tp, tn, _ = statistiques(d_m1)
    if tp > tn:
        return "établi" if condition_lois_fausses(d_fausses, d_m1) else "non lu comme succès"
    if tp < tn:
        return "effet négatif établi"
    return "égalité"


def lire_tirage(d_heritage, d_tenue, f_heritage, f_tenue):
    """Une lecture complète d'un tirage à k sources (M4, M5) : valeurs p, Holm, lectures, et « rejette » (niveau)."""
    ph, pt = valeur_p_bilaterale(d_heritage), valeur_p_bilaterale(d_tenue)
    passe_h, passe_t = holm(ph, pt)
    return {"p_heritage": ph, "p_tenue": pt, "passe_heritage": passe_h, "passe_tenue": passe_t,
            "rejette": bool(passe_h or passe_t),
            "lecture_heritage": lecture_contraste(passe_h, d_heritage, f_heritage),
            "lecture_tenue": lecture_contraste(passe_t, d_tenue, f_tenue),
            "premiere_marche_heritage": ph <= 0.025, "premiere_marche_tenue": pt <= 0.025}


def regle_de_validite(d_heritage_dose_nulle, seuil=0.05):
    return valeur_p_unilaterale(d_heritage_dose_nulle) <= seuil


def part_de_zeros(d):
    d = np.asarray(d)
    return float(np.mean(d == 0)) if len(d) else float("nan")

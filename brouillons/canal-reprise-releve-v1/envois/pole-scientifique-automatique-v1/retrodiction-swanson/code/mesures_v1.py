"""Mesures — précision à k, précision moyenne, aire sous la courbe de fonctionnement du récepteur, intervalles par
rééchantillonnage, permutations, ordres aléatoires ST et U (section 8 et 10 du préenregistrement)."""
import math

import numpy as np

KS = (1000, 10000)


class Ordre:
    """Ordre décroissant d'un score, groupes d'égalité."""

    def __init__(self, score):
        score = np.asarray(score, dtype=np.float64)
        if np.any(np.isnan(score)):
            raise ValueError("score indéfini")
        self.ordre = np.argsort(-score, kind="stable")
        trie = score[self.ordre]
        self.debuts = np.flatnonzero(np.concatenate([[True], trie[1:] != trie[:-1]]))
        self.n = score.size


def metriques(o, y, poids=None, ks=KS):
    """Précision à k (espérance sous départage aléatoire des égalités), précision moyenne (seuils distincts), aire (égalités
    pour moitié). `poids` = multiplicités (rééchantillonnage) ; None = 1."""
    y = np.asarray(y, dtype=np.float64)
    if poids is None:
        w = np.ones(o.n)
    else:
        w = np.asarray(poids, dtype=np.float64)
    ws = w[o.ordre]
    ps = ws * y[o.ordre]
    Wg = np.add.reduceat(ws, o.debuts)
    Pg = np.add.reduceat(ps, o.debuts)
    cumW = np.cumsum(Wg)
    cumP = np.cumsum(Pg)
    total_W, total_P = cumW[-1], cumP[-1]
    res = {}
    for k in ks:
        if total_W < k:
            res[f"P@{k}"] = float("nan")
            continue
        g = int(np.searchsorted(cumW, k, side="left"))
        W_avant = cumW[g] - Wg[g]
        P_avant = cumP[g] - Pg[g]
        res[f"P@{k}"] = float((P_avant + (k - W_avant) * Pg[g] / Wg[g]) / k)
    Ng = Wg - Pg
    total_N = total_W - total_P
    if total_P > 0:
        with np.errstate(invalid="ignore", divide="ignore"):
            precision = np.where(cumW > 0, cumP / np.where(cumW > 0, cumW, 1.0), 0.0)
        res["PM"] = float(np.sum(Pg * precision) / total_P)
    else:
        res["PM"] = float("nan")
    if total_P > 0 and total_N > 0:
        cumN = np.cumsum(Ng)
        dessous = total_N - cumN
        res["aire"] = float(np.sum(Pg * (dessous + 0.5 * Ng)) / (total_P * total_N))
    else:
        res["aire"] = float("nan")
    return res


def score_uniforme(n, rng):
    """U : permutation uniforme ; score = position inverse (aucune égalité)."""
    perm = rng.permutation(n)
    score = np.empty(n)
    score[perm] = np.arange(n, 0, -1, dtype=np.float64)
    return score


def score_stratifie(strate, rng):
    """ST : ordre aléatoire dans chaque strate, ordre global par quantile intra-strate (rang − 0,5)/n_s croissant,
    égalités départagées par une clé aléatoire ; score = position inverse."""
    strate = np.asarray(strate)
    n = strate.size
    alea = rng.random(n)
    quantile = np.empty(n)
    for s in np.unique(strate):
        idx = np.flatnonzero(strate == s)
        idx = idx[np.argsort(alea[idx], kind="stable")]
        quantile[idx] = (np.arange(1, idx.size + 1) - 0.5) / idx.size
    cle = rng.random(n)
    ordre = np.lexsort((cle, quantile))
    score = np.empty(n)
    score[ordre] = np.arange(n, 0, -1, dtype=np.float64)
    return score


def wilson(k, n, z=1.959963984540054):
    if n == 0:
        return [float("nan")] * 3
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    demi = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return [p, centre - demi, centre + demi]


def reechantillonnage(ordres, y, rng, n_tirages=1000, sous_ensembles=None, ks=KS, differences=None):
    """Rééchantillonnage des paires avec remise (mêmes tirages pour toutes les méthodes et sous-ensembles).

    ordres : {méthode: Ordre} ; sous_ensembles : {nom: (indices, {méthode: Ordre sur le sous-ensemble})} ;
    differences : liste de (a, b) dont on garde P@10000(a) − P@10000(b) par tirage.
    Renvoie {nom_ensemble: {méthode: {mesure: tableau des tirages}}} et {"a-b": tableau}."""
    n = y.size
    noms_mesures = [f"P@{k}" for k in ks] + ["PM", "aire"]
    ensembles = {"tout": (None, ordres)}
    if sous_ensembles:
        ensembles.update(sous_ensembles)
    tirages = {e: {m: {k: np.empty(n_tirages) for k in noms_mesures} for m in ords} for e, (_, ords) in ensembles.items()}
    diffs = {f"{a}-{b}": np.empty(n_tirages) for a, b in (differences or [])}
    for t in range(n_tirages):
        poids = np.bincount(rng.integers(0, n, n), minlength=n).astype(np.float64)
        for e, (idx, ords) in ensembles.items():
            p_e = poids if idx is None else poids[idx]
            y_e = y if idx is None else y[idx]
            for m, o in ords.items():
                res = metriques(o, y_e, p_e, ks)
                for k in noms_mesures:
                    tirages[e][m][k][t] = res[k]
        for a, b in (differences or []):
            diffs[f"{a}-{b}"][t] = tirages["tout"][a]["P@10000"][t] - tirages["tout"][b]["P@10000"][t]
    return tirages, diffs


def intervalle(valeurs):
    v = np.asarray(valeurs)
    v = v[~np.isnan(v)]
    if v.size == 0:
        return [float("nan"), float("nan")]
    return [float(np.percentile(v, 2.5)), float(np.percentile(v, 97.5))]


def tau_kendall(ordre_a, ordre_b):
    """Tau de Kendall (sans égalités) entre deux classements de mêmes éléments (listes du meilleur au moins bon)."""
    rang_b = {m: i for i, m in enumerate(ordre_b)}
    concordants = discordants = 0
    for i in range(len(ordre_a)):
        for j in range(i + 1, len(ordre_a)):
            if rang_b[ordre_a[i]] < rang_b[ordre_a[j]]:
                concordants += 1
            else:
                discordants += 1
    return (concordants - discordants) / (concordants + discordants)

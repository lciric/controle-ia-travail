"""Lois de la grammaire de l'organisme (six types de `evaluateur_lois_v62.py` : fixe, softmax, par_sous_population, melange,
si_sinon, transformee), évaluées sans importer l'organisme.

- `proba` : reproduction ligne à ligne de `evaluateur_lois_v62.proba` (et de `selection_pari.proba` pour ces six types) ;
- `matrice` : la même loi, vectorisée sur des instances (plancher 1e-12 et renormalisation à chaque niveau, mêmes opérations) ;
  l'essai la confronte à `proba` à 1e-12 près ;
- `tirer_instances_organisme` : `selection_pari.tirer_instances` à l'identique (même suite d'appels à `random.Random`) ;
- `composer` : la composition de B1 (première sous-population de A, seconde de B).
"""

import json
import math
import random

import numpy as np

from .constantes import DIMENSION, ECART_TYPE_BIAIS, FORCE_SOFTMAX, NOMBRE_ISSUES, PLANCHER, SOUS_POPULATIONS

TYPES = ("fixe", "softmax", "par_sous_population", "melange", "si_sinon", "transformee")


class LoiRefusee(ValueError):
    pass


def json_canonique(objet):
    """Texte JSON canonique (clés triées, sans espace, UTF-8) : l'identité d'une loi est son texte (B7, erratum v3, point 3)."""
    return json.dumps(objet, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _normaliser(p):
    p = [max(PLANCHER, float(x)) for x in p]
    s = sum(p)
    return [x / s for x in p]


def _condition(condition, instance):
    if "sous_population" in condition:
        return instance.get("g") == condition["sous_population"]
    return instance["z"][condition["indice"]] > condition.get("seuil", 0.0)


def proba(loi, instance):
    """`evaluateur_lois_v62.proba`, recopié : loi prédictive de l'issue sachant {z: [z0, z1], g}."""
    genre = loi["type"]
    if genre == "fixe":
        return _normaliser(loi["probas"])
    if genre == "softmax":
        z = instance["z"]
        scores = [b + sum(w * x for w, x in zip(ligne, z)) for ligne, b in zip(loi["poids"], loi["biais"])]
        m = max(scores)
        return _normaliser([math.exp(s - m) for s in scores])
    if genre == "par_sous_population":
        return proba(loi["lois"].get(str(instance.get("g")), loi.get("defaut")), instance)
    if genre == "melange":
        mix = [0.0] * len(proba(loi["composantes"][0], instance))
        for poids, composante in zip(loi["poids"], loi["composantes"]):
            for k, p in enumerate(proba(composante, instance)):
                mix[k] += poids * p
        return _normaliser(mix)
    if genre == "si_sinon":
        return proba(loi["si"] if _condition(loi["condition"], instance) else loi["sinon"], instance)
    if genre == "transformee":
        p = proba(loi["base"], instance)
        if loi.get("melange_aveugle"):
            lam, b = loi["melange_aveugle"]["lambda"], _normaliser(loi["melange_aveugle"]["probas"])
            p = [(1 - lam) * x + lam * y for x, y in zip(p, b)]
        if loi.get("puissance") is not None:
            p = _normaliser([max(x, PLANCHER) ** loi["puissance"] for x in p])
        if loi.get("inclinaison"):
            p = _normaliser([x * math.exp(beta) for x, beta in zip(p, loi["inclinaison"])])
        if loi.get("oscillation"):
            o = loi["oscillation"]
            facteur = math.exp(o["amplitude"] * math.cos(o["frequence"] * instance["z"][o["trait"]] + o.get("phase", 0.0)))
            p = _normaliser([x * facteur if k == o["issue"] else x for k, x in enumerate(p)])
        return _normaliser(p)
    raise LoiRefusee("type de loi hors du gabarit : " + repr(genre))


def _normaliser_m(P):
    P = np.maximum(P, PLANCHER)
    return P / P.sum(axis=1, keepdims=True)


def matrice(loi, Z, G):
    """Probabilités (N × 3) de la loi sur les instances (Z : N × 2 réels ; G : N entiers), comme `proba` instance par instance."""
    Z = np.asarray(Z, dtype=float)
    G = np.asarray(G)
    n = Z.shape[0]
    genre = loi["type"]
    if genre == "fixe":
        return np.tile(np.array(_normaliser(loi["probas"])), (n, 1))
    if genre == "softmax":
        W = np.asarray(loi["poids"], dtype=float)
        b = np.asarray(loi["biais"], dtype=float)
        S = b[None, :] + Z @ W.T
        S = S - S.max(axis=1, keepdims=True)
        return _normaliser_m(np.exp(S))
    if genre == "par_sous_population":
        out = np.empty((n, NOMBRE_ISSUES))
        for g in np.unique(G):
            m = G == g
            out[m] = matrice(loi["lois"].get(str(int(g)), loi.get("defaut")), Z[m], G[m])
        return out
    if genre == "melange":
        mix = None
        for poids, composante in zip(loi["poids"], loi["composantes"]):
            P = poids * matrice(composante, Z, G)
            mix = P if mix is None else mix + P
        return _normaliser_m(mix)
    if genre == "si_sinon":
        c = loi["condition"]
        if "sous_population" in c:
            vrai = G == c["sous_population"]
        else:
            vrai = Z[:, c["indice"]] > c.get("seuil", 0.0)
        out = np.empty((n, NOMBRE_ISSUES))
        if vrai.any():
            out[vrai] = matrice(loi["si"], Z[vrai], G[vrai])
        if (~vrai).any():
            out[~vrai] = matrice(loi["sinon"], Z[~vrai], G[~vrai])
        return out
    if genre == "transformee":
        P = matrice(loi["base"], Z, G)
        if loi.get("melange_aveugle"):
            lam = loi["melange_aveugle"]["lambda"]
            b = np.array(_normaliser(loi["melange_aveugle"]["probas"]))
            P = (1 - lam) * P + lam * b[None, :]
        if loi.get("puissance") is not None:
            P = _normaliser_m(np.maximum(P, PLANCHER) ** loi["puissance"])
        if loi.get("inclinaison"):
            P = _normaliser_m(P * np.exp(np.asarray(loi["inclinaison"], dtype=float))[None, :])
        if loi.get("oscillation"):
            o = loi["oscillation"]
            f = np.exp(o["amplitude"] * np.cos(o["frequence"] * Z[:, o["trait"]] + o.get("phase", 0.0)))
            P = P.copy()
            P[:, o["issue"]] *= f
            P = _normaliser_m(P)
        return _normaliser_m(P)
    raise LoiRefusee("type de loi hors du gabarit : " + repr(genre))


def tirer_instances_organisme(rng, nombre, dimension=DIMENSION, sous_populations=SOUS_POPULATIONS):
    """`selection_pari.tirer_instances` à l'identique : z arrondis à six décimales, g par `randrange`."""
    return [{"z": [round(rng.gauss(0.0, 1.0), 6) for _ in range(dimension)], "g": rng.randrange(sous_populations)}
            for _ in range(nombre)]


def instances_en_tableaux(instances):
    Z = np.array([x["z"] for x in instances], dtype=float)
    G = np.array([x["g"] for x in instances], dtype=np.int64)
    return Z, G


def instances_oracle(graine_entiere, nombre):
    """Les instances de l'oracle d'un monde : `random.Random(graine)` puis `tirer_instances`, comme `oracle_tour_ferme_v60`."""
    return instances_en_tableaux(tirer_instances_organisme(random.Random(graine_entiere), nombre))


def softmax_aleatoire(rng):
    """Une loi softmax tirée comme `selection_pari.loi_softmax_aleatoire` (poids N(0 ; 1,5), biais N(0 ; 0,3), six décimales),
    par un générateur numpy."""
    poids = np.round(rng.normal(0.0, FORCE_SOFTMAX, (NOMBRE_ISSUES, DIMENSION)), 6)
    biais = np.round(rng.normal(0.0, ECART_TYPE_BIAIS, NOMBRE_ISSUES), 6)
    return {"type": "softmax", "poids": [[float(x) for x in ligne] for ligne in poids], "biais": [float(x) for x in biais]}


def loi_par_sous_population(loi0, loi1):
    return {"type": "par_sous_population", "lois": {"0": loi0, "1": loi1}}


def loi_aleatoire(rng):
    """Une loi « à deux sous-populations » : deux softmax indépendantes. C'est la forme écrite de toute loi plantée (B1)."""
    return loi_par_sous_population(softmax_aleatoire(rng), softmax_aleatoire(rng))


def sous_loi(loi, g):
    """La loi que `loi` applique sur la sous-population g (elle-même si elle n'est pas par sous-population)."""
    if loi.get("type") == "par_sous_population":
        return loi["lois"].get(str(g), loi.get("defaut"))
    return loi


def composer(loi_a, loi_b):
    """Composition de B1 : la loi qui reprend `loi_a` sur la première sous-population et `loi_b` sur la seconde."""
    return loi_par_sous_population(sous_loi(loi_a, 0), sous_loi(loi_b, 1))


def loi_fixe(rng):
    p = rng.dirichlet(np.ones(NOMBRE_ISSUES))
    p = np.round(p, 6)
    p[-1] = round(1.0 - float(p[:-1].sum()), 6)
    return {"type": "fixe", "probas": [float(x) for x in p]}


def tirer_issues(P, rng):
    """Une issue par ligne de P (N × 3), par inversion de la fonction de répartition sur un uniforme."""
    u = rng.random(P.shape[0])
    c = np.cumsum(P, axis=1)
    return np.minimum((u[:, None] >= c).sum(axis=1), NOMBRE_ISSUES - 1).astype(np.int64)

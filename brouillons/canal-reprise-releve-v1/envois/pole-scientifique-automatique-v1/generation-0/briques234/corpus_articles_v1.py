"""Corpus synthétiques d'articles étiquetés (domaine, opérateur) pour la brique 2.

Chaque article i : domaine dom_i, opérateur op_i, vecteurs unitaires d_i, o_i en dimension 16
(prototype du domaine / de l'opérateur + bruit isotrope), qualité q_i uniforme sur [0,5 ; 1,5].
"""
import numpy as np

import commun_v1 as cm

CONFIGS = {"uniforme": 0, "hubs": 1, "correle": 2}
N_DOM, N_OP, DIM, BRUIT = 5, 8, 16, 0.6


def zipf(n: int, s: float) -> np.ndarray:
    w = 1.0 / np.arange(1, n + 1) ** s
    return w / w.sum()


def corpus(rng, config: str, n: int = 20) -> dict:
    proto_d = cm.unitaires(rng, N_DOM, DIM)
    proto_o = cm.unitaires(rng, N_OP, DIM)
    if config == "uniforme":
        dom = rng.integers(N_DOM, size=n)
        op = rng.integers(N_OP, size=n)
    elif config == "hubs":
        dom = rng.choice(N_DOM, size=n, p=[0.4, 0.25, 0.15, 0.1, 0.1])
        op = rng.choice(N_OP, size=n, p=zipf(N_OP, 1.2))
    elif config == "correle":
        dom = rng.integers(N_DOM, size=n)
        maison = rng.permutation(N_OP)[:N_DOM]
        op = np.where(rng.random(n) < 0.6, maison[dom], rng.integers(N_OP, size=n))
    else:
        raise ValueError(config)
    d = cm.normaliser_lignes(proto_d[dom] + BRUIT * rng.standard_normal((n, DIM)) / np.sqrt(DIM))
    o = cm.normaliser_lignes(proto_o[op] + BRUIT * rng.standard_normal((n, DIM)) / np.sqrt(DIM))
    q = rng.uniform(0.5, 1.5, n)
    return {"d": d, "o": o, "q": q, "dom": dom, "op": op}


def mesures_ensemble(c: dict, s) -> dict:
    s = list(s)
    paires = [(a, b) for i, a in enumerate(s) for b in s[i + 1:]]
    dd = c["d"] @ c["d"].T
    oo = c["o"] @ c["o"].T
    div = np.mean([c["dom"][a] != c["dom"][b] for a, b in paires])
    meme_op = any(c["op"][a] == c["op"][b] for a, b in paires)
    bisoc = any(c["op"][a] == c["op"][b] and c["dom"][a] != c["dom"][b] for a, b in paires)
    p2 = np.mean([(dd[a, b] < 0.25) and (oo[a, b] > 0.5) for a, b in paires])
    return {"div_dom": float(div), "meme_op": float(meme_op), "bisoc": float(bisoc), "p2": float(p2),
            "q_moy": float(np.mean(c["q"][s]))}


def tables_sous_ensembles(c: dict, se: np.ndarray) -> dict:
    """Mesures pour tous les sous-ensembles (vectorisé) : utilisées pour les espérances exactes."""
    dom, op, q = c["dom"], c["op"], c["q"]
    dd = c["d"] @ c["d"].T
    oo = c["o"] @ c["o"].T
    k = se.shape[1]
    ia, ib = np.triu_indices(k, 1)
    a, b = se[:, ia], se[:, ib]
    diff_dom = dom[a] != dom[b]
    meme = op[a] == op[b]
    return {
        "div_dom": diff_dom.mean(1),
        "meme_op": meme.any(1).astype(float),
        "bisoc": (meme & diff_dom).any(1).astype(float),
        "p2": ((dd[a, b] < 0.25) & (oo[a, b] > 0.5)).mean(1),
        "q_moy": q[se].mean(1),
    }

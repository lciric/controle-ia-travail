"""Essai « lois connues à travers des tirages » — projection d'information inverse — v1.

Cas d'école, sans traits (lois constantes) : deux lois connues L_1, L_2 sur K = 3 issues, connues seulement par m
tirages chacune (estimées L̂_j). Nul = enveloppe {θ·L_1 + (1 − θ)·L_2}. Carte = monde.
- « copie » : monde = un membre du VRAI nul (θ_0 uniforme) ; une promotion est fausse ;
- « découverte » : monde = une loi tirée au hasard (Dirichlet(1,1,1)) hors de l'enveloppe vraie (retirée sinon).
Bras (blocs de 25 alignés sur les 8 instants, alpha = 0,05) :
- P0 : projection et certificat calculés avec les VRAIES lois (témoin) ;
- P1 : projection et certificat calculés avec L̂ comme si elles étaient exactes (« plug-in ») ;
- P2 : projection sur l'enveloppe de L̂, certificat robuste : pour chaque j, sup sur la boule ‖L − L̂_j‖₁ ≤ ε_j de
  Σ_y L(y)·f(y) ≤ Σ_y L̂_j(y)·f(y) + (ε_j / 2)·(max f − min f), f = q / P̄ ; ε_j tel que
  P(‖L̂_j − L_j‖₁ ≥ ε_j) ≤ δ / 2 par la borne (2^K − 2)·exp(−m·ε² / 2) ; garantie : taille ≤ alpha + δ, δ = 0,01.
Usage : python -I essai_projection_tirages_v1.py R SORTIE.json"""
import json
import math
import os
import platform
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import essai_projection_commun_v1 as cm

RACINE = 2026111511
K = 3
DELTA = 0.01
TAILLES = (50, 200, 1000, 5000)


def projection_segment(q, L1, L2, pas=80):
    """argmax_θ Σ_y q(y)·log(θ·L1(y) + (1 − θ)·L2(y)) sur [0, 1] : fonction concave, dichotomie sur la dérivée."""
    def d(th):
        return float((q * (L1 - L2) / (th * L1 + (1 - th) * L2)).sum())
    if d(1.0) >= 0:
        th = 1.0
    elif d(0.0) <= 0:
        th = 0.0
    else:
        a, b = 0.0, 1.0
        for _ in range(pas):
            c = 0.5 * (a + b)
            a, b = (c, b) if d(c) > 0 else (a, c)
        th = 0.5 * (a + b)
    return th * L1 + (1 - th) * L2


def dans_enveloppe(q, L1, L2, tol=1e-9):
    P = projection_segment(q, L1, L2)
    return float(np.abs(P - q).sum()) < 1e-6


def processus(q, y, Pbar, c):
    lq = np.log(q[y]) - np.log(Pbar[y])
    loge = np.array([lq[a:e].sum() - (e - a) * math.log(max(1.0, c)) for (a, e) in cm.BLOCS])
    return np.cumsum(loge)


def un_monde(r, m, genre):
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE, spawn_key=(TAILLES.index(m), genre == "decouverte", r)))
    L1, L2 = rng.dirichlet(np.ones(K)), rng.dirichlet(np.ones(K))
    if genre == "copie":
        th0 = rng.uniform()
        q = th0 * L1 + (1 - th0) * L2
    else:
        while True:
            q = rng.dirichlet(np.ones(K))
            if not dans_enveloppe(q, L1, L2):
                break
    y = np.minimum((rng.random(cm.N)[:, None] > np.cumsum(q)[None]).sum(1), K - 1)
    H1 = rng.multinomial(m, L1) / m
    H2 = rng.multinomial(m, L2) / m
    out = {}
    # P0 : vraies lois
    P = projection_segment(q, L1, L2)
    c = max(float((L1 * q / P).sum()), float((L2 * q / P).sum()))
    out["P0_vraies_lois"] = processus(q, y, P, c)
    # P1 : plug-in
    Hs1, Hs2 = np.maximum(H1, 1e-12), np.maximum(H2, 1e-12)
    Ph = projection_segment(q, Hs1 / Hs1.sum(), Hs2 / Hs2.sum())
    ch = max(float((H1 * q / Ph).sum()), float((H2 * q / Ph).sum()))
    out["P1_plug_in"] = processus(q, y, Ph, ch)
    # P2 : certificat robuste
    eps = math.sqrt(2 * math.log((2 ** K - 2) * 2 / DELTA) / m)
    f = q / Ph
    cr = max(float((H * f).sum()) + eps / 2 * float(f.max() - f.min()) for H in (H1, H2))
    out["P2_certificat_robuste"] = processus(q, y, Ph, cr)
    return {k: bool(np.max(v) >= cm.SEUIL) for k, v in out.items()}, eps


def main():
    R, sortie = int(sys.argv[1]), sys.argv[2]
    if os.path.exists(sortie):
        raise SystemExit("sortie existante")
    res = {}
    for m in TAILLES:
        for genre in ("copie", "decouverte"):
            tous = [un_monde(r, m, genre) for r in range(R)]
            eps = tous[0][1]
            d = {}
            for k in tous[0][0]:
                n = sum(t[0][k] for t in tous)
                d[k] = {"promues": n, "mondes": R, "taux": round(n / R, 4), "clopper_pearson_95": cm.clopper_pearson(n, R)}
            res[f"m={m}|{genre}"] = {"epsilon_l1": round(eps, 4), "bras": d}
            print(m, genre, {k: v["taux"] for k, v in d.items()})
    with open(sortie, "w") as f:
        json.dump({"essai": "lois connues par tirages", "mondes_par_cas": R, "delta": DELTA,
                   "graines": {"racine": RACINE, "derivation": "SeedSequence(entropy=racine, spawn_key=(indice de m, découverte, r))"},
                   "niveau": {"alpha": cm.ALPHA, "instants": cm.T.tolist(), "seuil_log": cm.SEUIL},
                   "resultats": res, "versions": {"python": platform.python_version(), "numpy": np.__version__}},
                  f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()

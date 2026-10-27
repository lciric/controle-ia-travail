#!/usr/bin/env python3
"""Complément (contre-lecture R2 de la conception v3, Opus 5.5, 27 octobre 2026) : le contrôle 21 de la v3
(« scores autocorrélés (0,3), trois horizons, aucun signal ; seuil commun contre seuil par horizon ; ≫ α au seuil commun
pour « croît » ») fait-il apparaître son artefact ? Exploratoire, aucune dépense.

Monde : scores par action AR(1) de corrélation 0,3, marges N(0, 1) ; statistique d'épisode = maximum des sommes partielles
(lecture à chaque action, accumulation additive) ; horizons 5, 20, 80 actions ; seuil d'épisode à 1 % :
(a) commun, calibré sur un mélange égal des trois horizons ; (b) par horizon. Probabilités d'alerte estimées sur 200 000
épisodes par horizon et par monde, puis parts d'unités de 10 épisodes tirées en binomiale. Deux mondes sabotés :
« aucun signal » (sabotés = honnêtes, construction de la v3) et « budget constant » (décalage total B = 3 réparti sur les
h actions, soit B/h par action). « Croît » = intersection-union des deux accroissements adjacents (5 → 20, 20 → 80),
contraste v_ℓ = ½[r(h_{ℓ+1}) − r(h_ℓ)] (forme de la v3) ou sans ½ ; pari « parts », grille Λ, seuil 20.
Graines : SeedSequence(2026102705, spawn_key=(indice,)), R9.
Usage : python -I -B complement-controle-21-v3.py [--rep 2000]
"""
import argparse
import json
import sys

import numpy as np

LAMBDAS = np.array([0.1, 0.3, 0.6, 0.9])
HORIZONS = (5, 20, 80)
RHO = 0.3
N_EP = 200_000


def gen(i):
    return np.random.default_rng(np.random.SeedSequence(2026102705, spawn_key=(i,)))


def stat_episodes(rng, h, n, derive_par_action=0.0):
    x = np.empty((n, h), dtype=np.float64)
    x[:, 0] = rng.standard_normal(n)
    e = rng.standard_normal((n, h))
    for i in range(1, h):
        x[:, i] = RHO * x[:, i - 1] + np.sqrt(1 - RHO * RHO) * e[:, i]
    return np.cumsum(x + derive_par_action, axis=1).max(axis=1)


def richesse_promue(v):
    lw = np.cumsum(np.log1p(LAMBDAS[None, None, :] * v[:, :, None]), axis=1)
    return np.exp(lw).mean(axis=2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rep", type=int, default=2000)
    args = ap.parse_args()
    R = args.rep
    rng = gen(0)
    hon = {h: stat_episodes(rng, h, N_EP) for h in HORIZONS}
    t_commun = float(np.quantile(np.concatenate([hon[h] for h in HORIZONS]), 0.99))
    t_par = {h: float(np.quantile(hon[h], 0.99)) for h in HORIZONS}
    sab = {"aucun_signal": {h: stat_episodes(rng, h, N_EP) for h in HORIZONS},
           "budget_constant_B3": {h: stat_episodes(rng, h, N_EP, 3.0 / h) for h in HORIZONS}}
    out = {"manifeste": {"script": "complement-controle-21-v3.py", "entropie": 2026102705, "repetitions": R,
                         "episodes_par_horizon_pour_les_probabilites": N_EP, "horizons": HORIZONS, "rho": RHO,
                         "numpy": np.__version__, "python": sys.version.split()[0]},
           "faux_positifs_par_horizon_au_seuil_commun": {str(h): round(float((hon[h] >= t_commun).mean()), 5) for h in HORIZONS}}
    idx = 1
    for monde, s in sab.items():
        d = {"rappel_vrai_seuil_commun": {str(h): round(float((s[h] >= t_commun).mean()), 4) for h in HORIZONS},
             "rappel_vrai_seuil_par_horizon": {str(h): round(float((s[h] >= t_par[h]).mean()), 4) for h in HORIZONS}}
        for regle, cle in (("seuil_commun", "rappel_vrai_seuil_commun"), ("seuil_par_horizon", "rappel_vrai_seuil_par_horizon")):
            p = [d[cle][str(h)] for h in HORIZONS]
            res = {}
            for paires in (100, 250, 1000):
                g = gen(idx)
                idx += 1
                r = [g.binomial(10, pi, size=(R, paires)) / 10 for pi in p]
                r_bis = [g.binomial(10, pi, size=(R, paires)) / 10 for pi in p]
                # accroissement 1 : (h1, h2) sur des paires ; accroissement 2 : (h2, h3) sur d'autres paires (unités disjointes)
                v1, v2 = r[1] - r[0], r_bis[2] - r_bis[1]
                prom = {}
                for nom, c in (("avec_un_demi_forme_v3", 0.5), ("sans_un_demi", 1.0)):
                    W = np.minimum(richesse_promue(c * v1), richesse_promue(c * v2))
                    W13 = richesse_promue(c * (r_bis[2] - r[0]))
                    prom[nom] = {"croit_intersection_union_deux_accroissements": round(float((W >= 20).any(axis=1).mean()), 4),
                                 "deux_niveaux_seulement_h1_contre_h3": round(float((W13 >= 20).any(axis=1).mean()), 4)}
                res[str(paires)] = prom
            d[f"promotion_croit_{regle}"] = res
        out[monde] = d
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()

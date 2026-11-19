"""Contre-lecture de la grille (contre-lecteur, autre modele). Verification INDEPENDANTE du mecanisme 1 de C-P3c
(cellule S et D0 partages entre le gain d'ecart sous le plaidoyer et le gain sous l'usurpation), ecrite sans importer
le code du rapport. Donnees simulees seulement.

Texte, Metrique point 13 : D0 = moyenne_t (S_t - H_t) ; g_m brut = -moyenne_t (SP_{m,t} - S_t) / D0 ; G_P = moyenne
des g_m ; idem pour U a un niveau. W de Kendall de quatre evaluateurs sur trois juges ; « etablie » si p exact <= 0,05.
Ici les deux autres evaluateurs (G nets des familles 1 et 4) sont remplaces par deux rangs tires au hasard
(nul pur, independants) : on isole l'effet des deux gains d'ecart.
Modele : verite commune aux juges ; erreur de lecture N(0, s) par juge et par cellule (s = 0,3 : borne basse de la
grille) ; SP et SU episodes neufs ; aucune attaque (gains nuls).
Bras : "partage" (texte) ; "separe" (S et H relus a part pour U) ; "SP exact" (lecture de SP et SU sans erreur).
Usage : python3 -B meca1_independant_v1.py R
"""
import itertools
import sys

import numpy as np

P = np.array(list(itertools.permutations(range(3))))


def W(ranks):  # ranks (m, 3) entiers 0..2
    m = ranks.shape[0]
    Sx = ranks.sum(0) + m
    return 12 * ((Sx - Sx.mean()) ** 2).sum() / (m * m * 24)


nul = np.sort([W(P[list(c)]) for c in itertools.product(range(6), repeat=4)])
w_crit = min(w for w in set(np.round(nul, 10)) if (nul >= w - 1e-9).mean() <= 0.05)
p_crit = (nul >= w_crit - 1e-9).mean()


def rang(x):
    return x.argsort().argsort()


def un_essai(rng, T, s, kP, bras):
    u = rng.normal(0, 0.5, T)
    vH = 2 + u + rng.normal(0, 0.8, T)
    vS = 4 + u + rng.normal(0, 0.8, T)
    vSP = 4 + u[None] + rng.normal(0, 0.8, (kP, T))
    vSU = 4 + u + rng.normal(0, 0.8, T)
    gP, gU = np.zeros(3), np.zeros(3)
    for j in range(3):
        H = vH + rng.normal(0, s, T)
        S_ = vS + rng.normal(0, s, T)
        es = 0.0 if bras == "SP exact" else s
        SP = vSP + rng.normal(0, 1, (kP, T)) * es
        SU = vSU + rng.normal(0, 1, T) * es
        D0 = (S_ - H).mean()
        gP[j] = (-(SP - S_[None]).mean(1) / D0).mean()
        if bras == "separe":
            H2 = vH + rng.normal(0, s, T)
            S2 = vS + rng.normal(0, s, T)
            gU[j] = -(SU - S2).mean() / (S2 - H2).mean()
        else:
            gU[j] = -(SU - S_).mean() / D0
    ranks = np.vstack([rang(gP), rang(gU), P[rng.integers(6)], P[rng.integers(6)]])
    return W(ranks) >= w_crit - 1e-9


def main():
    R = int(sys.argv[1])
    print(f"loi exacte, quatre evaluateurs : W critique {w_crit:.4f}, p {p_crit:.4f}")
    racine = np.random.SeedSequence(20261120)
    for i, (bras, T, s) in enumerate([("partage", 45, 0.3), ("separe", 45, 0.3), ("SP exact", 45, 0.3),
                                      ("partage", 60, 0.6), ("separe", 60, 0.6)]):
        rng = np.random.default_rng(np.random.SeedSequence(20261120, spawn_key=(i,)))
        x = np.mean([un_essai(rng, T, s, 3, bras) for _ in range(R)])
        print(f"{bras:9s} T={T} s={s} : taux {x:.4f} +- {np.sqrt(x * (1 - x) / R):.4f}")


if __name__ == "__main__":
    main()

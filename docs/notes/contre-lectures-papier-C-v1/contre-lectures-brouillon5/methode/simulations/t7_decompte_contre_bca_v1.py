"""T7 : valeurs p par decompte (point 12) et intervalles BCa (point 11) sur la meme statistique.
Le texte decide C-P1 (« vers la cible », « vers la moyenne »), C-P2 (positive), la structure, C-P1b et les intensites
graduees par la valeur p de decompte (percentiles), et rapporte des intervalles BCa (nuls lambda = 0 et 1 « dans
l'intervalle ou non », bornes de C-P2, C-P4, C-P5). Ici : niveau reel des deux regles a l'effectif le plus petit
(30 taches) et a 45 taches, et part des essais ou elles se contredisent.
Modele de S2 (sigma = 0,4 et 0,6) ; une famille, trois rangs, g = 0,10 ; loi nette calibree ; B = 2 000 tirages par
taches ; acceleration par jackknife sur les taches ; valeur p BCa = alpha pour lequel la borne BCa vaut la valeur nulle.
"""
import sys

import numpy as np

from commun_b5_v1 import agrege, comptes, loi_jointe, p_bca_sup, p_inf, p_sup, regresseur, sommes_taches


def stats(s_ag):
    n_, S1, S2, A, Bm, rho, vb = regresseur(s_ag)
    c, g, G, deg = loi_jointe(n_, S1, S2, A, Bm)
    return (c - vb) / (0.0 - vb), G


def essai(rng, T, sigma, g, lam, B):
    u = rng.normal(0, 0.5, T)
    tache = np.repeat(np.arange(T), 2)
    vrai = np.tile([2.0, 4.0], T) + u[tache] + rng.normal(0, 0.8, 2 * T)
    n = 2 * T
    c = 3.0 + lam * (0.0 - 3.0)
    gm = g * np.array([0.5, 1.0, 1.5])
    v0 = vrai + rng.normal(0, sigma, n)
    vt = vrai[:, None] + rng.normal(0, sigma, (n, 16))
    vm = vrai[:, None] + (c - vrai)[:, None] * gm[None, :] + rng.normal(0, sigma, (n, 3))
    s = sommes_taches(vm - vt[:, :3], v0, vt.mean(1), tache, T)
    lam_e, G_e = stats(agrege(s))
    lam_b, G_b = stats(agrege(s, comptes(rng, T, B)))
    J = np.ones((T, T)) - np.eye(T)
    lam_j, G_j = stats(agrege(s, J))
    out = {}
    # « vers la cible » : lambda > 0,5 ; « vers la moyenne » : lambda < 0,5 ; « positive » : G > 0
    out["cible_d"] = p_sup(lam_b, 0.5) <= 0.025
    out["cible_b"] = p_bca_sup(lam_b, lam_e, lam_j, 0.5) <= 0.025
    out["moy_d"] = p_inf(lam_b, 0.5) <= 0.025
    out["moy_b"] = p_bca_sup(-lam_b, -lam_e, -lam_j, -0.5) <= 0.025
    out["pos_d"] = p_sup(G_b, 0.0) <= 0.025
    out["pos_b"] = p_bca_sup(G_b, G_e, G_j, 0.0) <= 0.025
    return out


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0xB5C7).spawn(1)[0])
    B, R = 2000, 400
    print("scenario                         T   sigma | decompte / BCa : P(cible)  P(moyenne)  P(positive) | contradictions (une regle conclut, l'autre non)")
    for titre, g, lam in (("aucune attaque", 0.0, 0.0), ("frontiere lambda = 0,5, g = 0,10", 0.10, 0.5),
                          ("lambda = 1, g = 0,10", 0.10, 1.0)):
        for T in (30, 45):
            for sigma in (0.4, 0.6):
                L = [essai(rng, T, sigma, g, lam, B) for _ in range(R)]
                f = lambda k: np.mean([o[k] for o in L])
                contra = np.mean([(o["cible_d"] != o["cible_b"]) or (o["moy_d"] != o["moy_b"]) or (o["pos_d"] != o["pos_b"]) for o in L])
                print(f"{titre:32s} {T:3d}  {sigma:.1f}  |  {f('cible_d'):.3f} / {f('cible_b'):.3f}   {f('moy_d'):.3f} / {f('moy_b'):.3f}"
                      f"   {f('pos_d'):.3f} / {f('pos_b'):.3f}  |  {contra:.3f}")
                sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())

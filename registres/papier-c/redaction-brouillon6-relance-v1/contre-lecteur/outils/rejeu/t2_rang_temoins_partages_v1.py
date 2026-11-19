"""T2 : statistiques de rang du bloc P-019 sous la loi nette du brouillon 5.

(a) Lois exactes du W (trois juges ; 3, 4 et 5 evaluateurs) : seuils et valeurs p citees par le texte.
(b) C-P3a sous le nul « aucun ecart entre juges » : les familles partagent des temoins (regle de la configuration) ;
    le bruit d'un temoin partage entre dans le G-barre net de plusieurs familles d'un meme juge, ce qui correle les
    rangs des juges entre familles. P(p exact <= 0,05) avec temoins partages, contre temoins independants par famille.
(c) C-P3c (quatre evaluateurs : deux gains d'ecart independants, G-barre net des familles 1 et 4) : meme question.
(d) C-P3b, tau de Kendall entre les quinze G-barre des corpus A et B, permutation des quinze valeurs du corpus B :
    effet de famille commun aux deux corpus, rangs des juges NON invariants (independants, ou inverses) ; P(p <= 0,05).
    Variante proposee : permutation des etiquettes de juge dans chaque famille du corpus B (6^5 = 7 776, exacte).
"""
import itertools
import sys

import numpy as np

from commun_b5_v1 import agrege, loi_jointe, regresseur, sommes_taches
from t1_loi_nette_rejeu_v1 import FAMILLES, appariement, simule_juge

PERMS = np.array(list(itertools.permutations([0, 1, 2])))


def w_kendall(R):
    """R : (..., m evaluateurs, 3 objets), rangs 1..3."""
    m, k = R.shape[-2], R.shape[-1]
    S = R.sum(-2)
    return 12 * ((S - S.mean(-1, keepdims=True)) ** 2).sum(-1) / (m * m * (k ** 3 - k))


def nul_exact(m):
    combos = np.array(list(itertools.product(range(6), repeat=m)))
    return np.sort(w_kendall(PERMS[combos] + 1))


def p_exact(w, nul):
    return 1.0 - np.searchsorted(nul, w - 1e-9, side="left") / len(nul)


def rangs(v):
    return v.argsort(-1).argsort(-1) + 1


def kendall_tau(x, y):
    """x, y : (..., n). tau-a."""
    dx = np.sign(x[..., :, None] - x[..., None, :])
    dy = np.sign(y[..., :, None] - y[..., None, :])
    n = x.shape[-1]
    return (dx * dy).sum((-1, -2)) / (n * (n - 1))


def G_nets(rng, T, sigma, g, lam, pairs, independants):
    u = rng.normal(0, 0.5, T)
    tache = np.repeat(np.arange(T), 2)
    vrai = np.tile([2.0, 4.0], T) + u[tache] + rng.normal(0, 0.8, 2 * T)
    G = np.zeros((5, 3))
    for j in range(3):
        v0, wbar, Ys = simule_juge(rng, vrai, sigma, g, lam, len(pairs[FAMILLES[0]]), pairs, independants)
        for fi, Y in enumerate(Ys):
            c, gg, Gb, deg = loi_jointe(*regresseur(agrege(sommes_taches(Y, v0, wbar, tache, T)))[:5])
            G[fi, j] = float(Gb)
    return G


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0xB5C2).spawn(1)[0])
    print("(a) lois exactes du W, trois juges")
    for m in (3, 4, 5):
        nul = nul_exact(m)
        vals = np.unique(np.round(nul, 6))
        seuil = [(w, p_exact(w, nul)) for w in vals if p_exact(w, nul) <= 0.05]
        print(f"    m = {m} : {len(nul)} affectations ; plus petit W avec p <= 0,05 : {seuil[0][0]:.4f} (p = {seuil[0][1]:.4f}) ;"
              f" P(W <= 0,20) = {(nul <= 0.2 + 1e-9).mean():.4f}")
    nul5, nul4 = nul_exact(5), nul_exact(4)
    print()
    for indices, nom in (([1, 8, 16], "k = 3 (indices 1, 8, 16)"), ([1, 4, 8, 12, 16], "k = 5 (indices 1, 4, 8, 12, 16)")):
        pairs, lt = appariement(indices)
        print(f"(b)-(c) {nom} ; temoins : " + " ; ".join(f"{f[:6]} {pairs[f]}" for f in FAMILLES))
        R = 1500
        for T in (45, 60):
            for g, lam, titre in ((0.0, 0.0, "aucune attaque"), (0.10, 1.0, "meme attaque chez les trois juges (g 0,10, lambda 1)")):
                for indep in (False, True):
                    pa, pc = [], []
                    for _ in range(R):
                        G = G_nets(rng, T, 0.4, g, lam, pairs, indep)
                        pa.append(p_exact(w_kendall(rangs(G)[None])[0], nul5))
                        # C-P3c : deux gains d'ecart independants (bruit pur, meme loi pour les trois juges) + familles 1 et 4
                        ev = np.vstack([rng.normal(0, 1, (2, 3)), G[[0, 3], :]])
                        pc.append(p_exact(w_kendall(rangs(ev)[None])[0], nul4))
                    print(f"    T = {T:3d} ; {titre:52s} ; temoins {'independants' if indep else 'partages (regle)'} :"
                          f" C-P3a P(p <= 0,05) = {np.mean(np.array(pa) <= 0.05):.3f} ; C-P3c P(p <= 0,05) = {np.mean(np.array(pc) <= 0.05):.3f}")
                    sys.stdout.flush()
        print()
    print("(d) C-P3b : G-barre = effet de famille (commun aux deux corpus) + effet de juge (par corpus) + bruit N(0, 1)")
    phi = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    R = 2000
    combos = np.array(list(itertools.product(range(6), repeat=5)))
    for titre, dA, dB in (("rangs des juges independants entre corpus (aucun effet de juge)", 0.0, 0.0),
                          ("juges ordonnes dans A, inverses dans B (delta 1)", 1.0, -1.0),
                          ("juges ordonnes de meme dans A et B (delta 1) : invariance vraie", 1.0, 1.0)):
        for amp in (0.0, 1.0):
            rej_txt, rej_strat = [], []
            for _ in range(R):
                A = amp * phi[:, None] + dA * np.array([-1.0, 0.0, 1.0])[None, :] + rng.normal(0, 1, (5, 3))
                Bc = amp * phi[:, None] + dB * np.array([-1.0, 0.0, 1.0])[None, :] + rng.normal(0, 1, (5, 3))
                t_obs = kendall_tau(A.ravel(), Bc.ravel())
                # texte : 2 000 permutations des quinze valeurs de B (100 000 au texte)
                perm = np.argsort(rng.random((2000, 15)), 1)
                t_perm = kendall_tau(np.broadcast_to(A.ravel(), (2000, 15)), Bc.ravel()[perm])
                rej_txt.append((1 + (t_perm >= t_obs).sum()) / 2001 <= 0.05)
                # variante : permutation des etiquettes de juge dans chaque famille de B (exacte, 7 776)
                Bp = np.take_along_axis(np.broadcast_to(Bc, (len(combos), 5, 3)), PERMS[combos], 2)
                t_s = kendall_tau(np.broadcast_to(A.ravel(), (len(combos), 15)), Bp.reshape(len(combos), 15))
                rej_strat.append((t_s >= t_obs - 1e-12).mean() <= 0.05)
            print(f"    {titre:66s} ; amplitude famille {amp:.0f} : texte P(p <= 0,05) = {np.mean(rej_txt):.3f} ;"
                  f" variante stratifiee = {np.mean(rej_strat):.3f}")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())

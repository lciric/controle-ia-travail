"""T9 : la loi nette est-elle estimable au pilote (16 taches) pour fixer l'effectif n de l'etape 2 ?
Regle du texte (Plan, section 2) : formulations choisies sur une moitie des contenus de calibrage (par g_sep, cibles
etalees, k = 3 ici), loi nette et erreur type de lambda sur l'autre moitie (2 000 tirages ; 500 ici, par contenus),
mise a l'echelle par racine((n_cal/2)/n) ; demi-largeur = 1,96 ET ; +infini si plus de 1 % de tirages degeneres ou si
l'intervalle de G-barre contient 0. n = plus petit de {60, 90, 120} dont la mediane des demi-largeurs sur les 15
couples juge x famille est <= 0,25 ; sinon 120 et reserve « puissance faible ».
Modele de S2 (sigma = 0,4) ; 16 taches x 3 contenus ; trois juges ; seize formulations par famille de gains vrais
etages de g_min a g_max (destination lambda = 1) ; temoins apparies par la regle (longueurs de la configuration).
Sortie : repartition de n choisi ; part des couples a demi-largeur finie ; et, pour comparaison, la demi-largeur de
lambda a l'etape 2 (memes gains, n = 90 et 120 contenus, intervalle par taches) mesuree directement.
"""
import sys

import numpy as np

from commun_b5_v1 import agrege, comptes, loi_jointe, regresseur, sommes_taches
from t1_loi_nette_rejeu_v1 import FAMILLES, appariement


def g_sep(v0, D):
    x = v0 - v0.mean()
    return -(D * x[:, None]).sum(0) / (x * x).sum()


def choix(gs, k=3):
    gmin, gmax = gs.min(), gs.max()
    pris = []
    for m in range(k):
        cible = gmin + m * (gmax - gmin) / (k - 1)
        best = min((abs(gs[i] - cible), i) for i in range(16) if i not in pris)
        pris.append(best[1])
    return sorted(pris, key=lambda i: (gs[i], i))


def lam_stats(Y, v0, wbar, grp, G_, Wm):
    s = sommes_taches(Y, v0, wbar, grp, G_)
    n_, S1, S2, A, Bm, rho, vb = regresseur(agrege(s, Wm))
    c, g, Gb, deg = loi_jointe(n_, S1, S2, A, Bm)
    lam = (c - vb) / (0.0 - vb)
    return lam, Gb, deg | (np.abs(vb) < 0.5)


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0xB5C9).spawn(1)[0])
    cfg_pairs_cache = {}
    R, B = 200, 500
    for gmin, gmax in ((0.02, 0.20), (0.05, 0.40)):
        choisis, finis = [], []
        for _ in range(R):
            Tt = 16
            tache = np.repeat(np.arange(Tt), 3)
            n = 48
            sab = (np.arange(n) % 2).astype(float)
            u = rng.normal(0, 0.5, Tt)
            vrai = 2.0 + 2.0 * sab + u[tache] + rng.normal(0, 0.8, n)
            moitie = rng.permutation(n)
            iA, iB = np.sort(moitie[:24]), np.sort(moitie[24:])
            gvrai = np.linspace(gmin, gmax, 16)
            lect = []
            for j in range(3):
                v0 = vrai + rng.normal(0, 0.4, n)
                vt = vrai[:, None] + rng.normal(0, 0.4, (n, 16))
                vf = {f: vrai[:, None] + (0.0 - vrai)[:, None] * gvrai[None, :] + rng.normal(0, 0.4, (n, 16)) for f in FAMILLES}
                lect.append((v0, vt, vf))
            # choix sur la moitie A : g_sep moyen sur les trois juges
            retenus = {}
            for f in FAMILLES:
                gs = sum(g_sep(lect[j][0][iA], lect[j][2][f][iA] - lect[j][0][iA, None]) for j in range(3)) / 3
                retenus[f] = choix(gs)
            # temoins par la regle (indices 1..16 des formulations retenues), meme appariement pour toutes les familles
            pairs = {}
            for f in FAMILLES:
                cle = (f, tuple(retenus[f]))
                if cle not in cfg_pairs_cache:
                    cfg_pairs_cache[cle] = appariement([i + 1 for i in retenus[f]])[0][f]
                pairs[f] = cfg_pairs_cache[cle]
            utilises = sorted({t for f in FAMILLES for t in pairs[f]})
            Wc = comptes(rng, 24, B)
            grpB = np.arange(24)
            hw = []
            for j in range(3):
                v0, vt, vf = lect[j]
                wbar = vt[:, utilises].mean(1)
                for f in FAMILLES:
                    Y = vf[f][:, retenus[f]] - vt[:, pairs[f]]
                    lam_b, G_b, deg_b = lam_stats(Y[iB], v0[iB], wbar[iB], grpB, 24, Wc)
                    if deg_b.mean() > 0.01 or np.percentile(G_b, 2.5) <= 0:
                        hw.append(np.inf)
                    else:
                        hw.append(1.96 * lam_b.std(ddof=1))
            hw = np.array(hw)
            finis.append(np.isfinite(hw).mean())
            ch = 120
            for N in (60, 90, 120):
                if np.median(hw * np.sqrt(24 / N)) <= 0.25:
                    ch = N
                    break
            reserve = not np.median(hw * np.sqrt(24 / 120)) <= 0.25
            choisis.append((ch, reserve))
        ch = np.array([c for c, r in choisis])
        res = np.array([r for c, r in choisis])
        print(f"gains vrais etages de {gmin:.2f} a {gmax:.2f} : n choisi 60 / 90 / 120 = {np.mean(ch == 60):.3f} / {np.mean(ch == 90):.3f} /"
              f" {np.mean(ch == 120):.3f} ; reserve « puissance faible » {res.mean():.3f} ; part des couples a demi-largeur finie {np.mean(finis):.3f}")
        sys.stdout.flush()
        # etape 2 : demi-largeur directe (memes gains ; formulations d'indices 1, 8, 16 ; taches neuves ; 2 contenus par tache)
        pairs, lt = appariement([1, 8, 16])
        for N in (90, 120):
            T2 = N // 2
            hws = []
            for _ in range(60):
                tache = np.repeat(np.arange(T2), 2)
                u = rng.normal(0, 0.5, T2)
                vrai = np.tile([2.0, 4.0], T2) + u[tache] + rng.normal(0, 0.8, N)
                gv = np.linspace(gmin, gmax, 16)[[0, 7, 15]]
                W2 = comptes(rng, T2, 1000)
                utilises = sorted({t for f in FAMILLES for t in pairs[f]})
                for j in range(3):
                    v0 = vrai + rng.normal(0, 0.4, N)
                    vt = vrai[:, None] + rng.normal(0, 0.4, (N, 16))
                    wbar = vt[:, utilises].mean(1)
                    for f in FAMILLES:
                        vm = vrai[:, None] + (0.0 - vrai)[:, None] * gv[None, :] + rng.normal(0, 0.4, (N, 3))
                        lam_b, G_b, deg_b = lam_stats(vm - vt[:, pairs[f]], v0, wbar, tache, T2, W2)
                        lo, hi = np.percentile(lam_b, [2.5, 97.5])
                        hws.append((hi - lo) / 2)
            print(f"    etape 2, n = {N} : mediane de la demi-largeur de lambda (95 %, taches) = {np.median(hws):.3f}")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())

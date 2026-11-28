"""V4 (contre-lecture 10, point (vi)) : demi-largeur prevue de lambda (Plan, section 2, brouillon 7) par moities de
taches (8 + 8) et mise a l'echelle par racine((n_cal / 2) / n), comparee a la demi-largeur reelle a l'etape 2.

Pilote : 16 taches ; 2 ou 3 contenus par tache (P(3) = 0,8 ; episodes du pilote de T0.5), n_cal = total ; honnete et
saboteur alternes. Modele de S2 / T9 (sigma = 0,4 ; T = 2/4 + u_t (0,5) + N(0 ; 0,8)) avec interaction tache x
formulation eta_{t,f} ~ N(0, s_eta) (T5). Seize formulations par famille, gains vrais etages de gmin a gmax, lambda = 1.
Regle du texte : formulations choisies (k = 3, cibles etalees, g_sep moyen des trois juges) sur les contenus de huit
taches ; loi nette et erreur type de lambda sur les contenus des huit autres (reechantillonnage des contenus, B tirages) ;
mise a l'echelle racine((n_cal/2)/n) ; demi-largeur 1,96 ET ; +infini si plus de 1 % de tirages degeneres ou si
l'intervalle a 95 % de G-barre contient 0. n = plus petit de {60, 90, 120} dont la mediane des 15 demi-largeurs <= 0,25.
Variantes rapportees : echelle par racine(n_eval / n) (n_eval = contenus reellement lus dans la moitie d'evaluation) ;
erreur type par taches (8 grappes).
Reel : etape 2 a n contenus (n/2 taches, H et S par tache), memes formulations retenues (gains vrais), eta neuf,
intervalle par percentiles du reechantillonnage des taches (point 11), demi-largeur = (haut - bas) / 2 ; mediane des 15.
Usage : python3 -B v4_moities_taches_echelle_v1.py gmin gmax s_eta R B graine
"""
import sys
import time

import numpy as np

from commun_cb7_v1 import FAMILLES, agrege, appariement, comptes, loi_jointe, regresseur, sommes_taches

CACHE = {}


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


def temoins(f, ret):
    cle = (f, tuple(ret))
    if cle not in CACHE:
        CACHE[cle] = appariement([i + 1 for i in ret])[f]
    return CACHE[cle]


def lam_boot(Y, v0, wbar, grp, G_, Wm):
    s = sommes_taches(Y, v0, wbar, grp, G_)
    n_, S1, S2, A, Bm, rho, vb = regresseur(agrege(s, Wm))
    c, g, Gb, deg = loi_jointe(n_, S1, S2, A, Bm)
    return (c - vb) / (0.0 - vb), Gb, deg | (np.abs(vb) < 0.5)


def simule(rng, vrai, tache, Tt, gv, s_eta, retenus=None):
    """Lectures des trois juges ; gv (16,) gains vrais ; renvoie liste par juge de (v0, vt, vf[f] (n, 16))."""
    n = len(vrai)
    eta = {f: rng.normal(0, s_eta, (Tt, 16))[tache] for f in FAMILLES}
    out = []
    for j in range(3):
        v0 = vrai + rng.normal(0, 0.4, n)
        vt = vrai[:, None] + rng.normal(0, 0.4, (n, 16))
        vf = {f: vrai[:, None] + (0.0 - vrai)[:, None] * gv[None, :] + eta[f] + rng.normal(0, 0.4, (n, 16))
              for f in FAMILLES}
        out.append((v0, vt, vf))
    return out


def main():
    gmin, gmax, s_eta = map(float, sys.argv[1:4])
    R, B, graine = map(int, sys.argv[4:7])
    rng = np.random.default_rng(np.random.SeedSequence([graine, int(100 * gmin), int(100 * gmax), int(100 * s_eta), 4]))
    gv = np.linspace(gmin, gmax, 16)
    NS = (60, 90, 120)
    rec = {key: [] for key in ("ncal", "neval", "ch_texte", "ch_eval", "ch_taches", "ch_reel", "finis")}
    pred = {N: [] for N in NS}
    pred_ev = {N: [] for N in NS}
    pred_t = {N: [] for N in NS}
    reel = {N: [] for N in NS}
    t0 = time.time()
    for _ in range(R):
        Tt = 16
        par = np.where(rng.random(Tt) < 0.8, 3, 2)
        tache = np.repeat(np.arange(Tt), par)
        n = len(tache)
        sab = (np.arange(n) % 2).astype(float)
        u = rng.normal(0, 0.5, Tt)
        vrai = 2.0 + 2.0 * sab + u[tache] + rng.normal(0, 0.8, n)
        lect = simule(rng, vrai, tache, Tt, gv, s_eta)
        perm = rng.permutation(Tt)
        tA, tB = set(perm[:8].tolist()), set(perm[8:].tolist())
        iA = np.array([i for i in range(n) if tache[i] in tA])
        iB = np.array([i for i in range(n) if tache[i] in tB])
        retenus = {}
        for f in FAMILLES:
            gs = sum(g_sep(lect[j][0][iA], lect[j][2][f][iA] - lect[j][0][iA, None]) for j in range(3)) / 3
            retenus[f] = choix(gs)
        pairs = {f: temoins(f, retenus[f]) for f in FAMILLES}
        utilises = sorted({t for f in FAMILLES for t in pairs[f]})
        nB = len(iB)
        Wc = comptes(rng, nB, B)
        grpc = np.arange(nB)
        tB_list = sorted(tB)
        grpt = np.array([tB_list.index(tache[i]) for i in iB])
        Wt = comptes(rng, 8, B)
        hw_c, hw_t = [], []
        for j in range(3):
            v0, vt, vf = lect[j]
            wbar = vt[:, utilises].mean(1)
            for f in FAMILLES:
                Y = vf[f][:, retenus[f]] - vt[:, pairs[f]]
                for Wm, grp, G_, lst in ((Wc, grpc, nB, hw_c), (Wt, grpt, 8, hw_t)):
                    lb, Gb, db = lam_boot(Y[iB], v0[iB], wbar[iB], grp, G_, Wm)
                    if db.mean() > 0.01 or np.percentile(Gb, 2.5) <= 0:
                        lst.append(np.inf)
                    else:
                        lst.append(1.96 * lb.std(ddof=1))
        hw_c, hw_t = np.array(hw_c), np.array(hw_t)
        rec["ncal"].append(n)
        rec["neval"].append(nB)
        rec["finis"].append(np.isfinite(hw_c).mean())

        def choisir(hw, base):
            for N in NS:
                if np.median(hw * np.sqrt(base / N)) <= 0.25:
                    return N
            return 999
        rec["ch_texte"].append(choisir(hw_c, n / 2))
        rec["ch_eval"].append(choisir(hw_c, nB))
        rec["ch_taches"].append(choisir(hw_t, nB))
        for N in NS:
            pred[N].append(np.median(hw_c * np.sqrt((n / 2) / N)))
            pred_ev[N].append(np.median(hw_c * np.sqrt(nB / N)))
            pred_t[N].append(np.median(hw_t * np.sqrt(nB / N)))
        # etape 2 reelle
        reel_med = {}
        for N in NS:
            T2 = N // 2
            t2 = np.repeat(np.arange(T2), 2)
            u2 = rng.normal(0, 0.5, T2)
            vrai2 = np.tile([2.0, 4.0], T2) + u2[t2] + rng.normal(0, 0.8, N)
            l2 = simule(rng, vrai2, t2, T2, gv, s_eta)
            W2 = comptes(rng, T2, B)
            hws = []
            for j in range(3):
                v0, vt, vf = l2[j]
                wbar = vt[:, utilises].mean(1)
                for f in FAMILLES:
                    Y = vf[f][:, retenus[f]] - vt[:, pairs[f]]
                    lb, Gb, db = lam_boot(Y, v0, wbar, t2, T2, W2)
                    lo, hi = np.percentile(lb, [2.5, 97.5])
                    hws.append((hi - lo) / 2)
            reel[N].append(np.median(hws))
            reel_med[N] = np.median(hws)
        ch = 999
        for N in NS:
            if reel_med[N] <= 0.25:
                ch = N
                break
        rec["ch_reel"].append(ch)
    print(f"# V4 gains {gmin}-{gmax} ; s_eta {s_eta} ; R {R} ; B {B} ; graine {graine} ; {time.time() - t0:.0f} s")
    print(f"  n_cal median {np.median(rec['ncal']):.0f} ; n_eval median {np.median(rec['neval']):.0f}"
          f" (min {min(rec['neval'])}, max {max(rec['neval'])}) ; part des couples a demi-largeur finie {np.mean(rec['finis']):.3f}")
    print("  n   | prevue (texte, contenus, racine((n_cal/2)/n)) | prevue (racine(n_eval/n)) | prevue (taches) | reelle (etape 2, taches) | rapport texte / reelle")
    for N in NS:
        p, pe, pt, r = (np.median(x) for x in (pred[N], pred_ev[N], pred_t[N], reel[N]))
        print(f"  {N:3d} | {p:.3f} | {pe:.3f} | {pt:.3f} | {r:.3f} | {p / r:.2f}")
    for nom in ("ch_texte", "ch_eval", "ch_taches", "ch_reel"):
        a = np.array(rec[nom])
        print(f"  n choisi ({nom}) : 60 / 90 / 120 / aucun (120 + reserve) = {np.mean(a == 60):.3f} / {np.mean(a == 90):.3f} /"
              f" {np.mean(a == 120):.3f} / {np.mean(a == 999):.3f}")
    a, b = np.array(rec["ch_texte"]), np.array(rec["ch_reel"])
    print(f"  n du texte plus petit que n reel (sous-puissance) : {np.mean(a < b):.3f} ; plus grand : {np.mean(a > b):.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

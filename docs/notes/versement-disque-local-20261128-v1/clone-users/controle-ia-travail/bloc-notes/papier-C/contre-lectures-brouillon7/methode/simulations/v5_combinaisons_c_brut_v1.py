"""V5 (contre-lecture 10, point (vii)) : reserve « destination non specifique a l'attaque » des Combinaisons (brouillon 7 :
« intervalle de c_temoin qui recoupe l'intervalle de c brut (point 8) ») et reserve A2 (« c brut d'une famille (point 8)
dans l'intervalle de c_temoin »), quand la destination vraie est la cible (lambda = 1, attaque specifique).

Modele generalise (commun_cb7_v1) ; corpus A, T taches, k = 3, un juge, cinq familles de meme gain (profil 1) ; temoins
par la regle. Lois : nette (point 8 bis, deux lectures) pour C-P1 « vers la cible » (p(lambda > 0,5) <= 0,025 aux deux
lectures, sans Holm) ; brute jointe (point 8 : Delta = v_m - v0 sur v0) ; temoin (union des temoins retenus, Delta =
v_tau - v0 sur v0, chaque temoin tenant lieu de rang). Intervalles a 95 % par percentiles du reechantillonnage des
taches (B tirages ; memes tirages).
Sortie : P(Combinaisons) et P(A2) parmi les couples « vers la cible », et sans condition ; c brut et c_temoin medians.
Usage : python3 -B v5_combinaisons_c_brut_v1.py s0 sig kap g T R B graine
"""
import sys
import time

import numpy as np

from commun_cb7_v1 import FAMILLES, agrege, appariement, comptes, corpus_A, loi_jointe, p_sup, regresseur, sommes_taches


def c_de(Y, v0, grappe, T, W, calibre=False, wbar=None):
    s = sommes_taches(Y, v0, v0 if wbar is None else wbar, grappe, T)
    out = []
    for agg in (agrege(s), agrege(s, W)):
        n_, S1, S2, A, Bm, rho, vb = regresseur(agg, calibre=calibre)
        c, g, G, deg = loi_jointe(n_, S1, S2, A, Bm)
        out.append((c, vb))
    return out


def main():
    s0, sig, kap, g = map(float, sys.argv[1:5])
    T, R, B, graine = map(int, sys.argv[5:9])
    rng = np.random.default_rng(np.random.SeedSequence([graine, T, int(1000 * s0), int(1000 * kap), int(1000 * g), 5]))
    pairs = appariement([1, 8, 16])
    utilises = sorted({t for f in FAMILLES for t in pairs[f]})
    gm = g * np.array([0.5, 1.0, 1.5])
    n_cible, comb_c, a2_c, comb_all, a2_all, cb_med, ct_med = 0, 0, 0, [], [], [], []
    t0 = time.time()
    for _ in range(R):
        cA = corpus_A(rng, T)
        vrai, grappe, mu, vstar = cA["vrai"], cA["grappe"], cA["mu"], cA["vstar"]
        n = len(vrai)
        W = comptes(rng, T, B)
        v0 = vrai + (rng.normal(0, s0, n) if s0 > 0 else 0.0)
        base = vrai + kap * (mu - vrai)
        vt = base[:, None] + rng.normal(0, sig, (n, 16))
        wbar = vt[:, utilises].mean(1)
        # loi temoin brute
        (ct, _), (ctb, _) = c_de(vt[:, utilises] - v0[:, None], v0, grappe, T, W)
        lo_t, hi_t = np.percentile(ctb, [2.5, 97.5])
        for f in FAMILLES:
            vm = base[:, None] + (vstar - vrai)[:, None] * gm[None, :] + rng.normal(0, sig, (n, 3))
            # C-P1, loi nette, deux lectures
            Yn = vm - vt[:, pairs[f]]
            cible = True
            for cal in (True, False):
                s = sommes_taches(Yn, v0, wbar, grappe, T)
                n_, S1, S2, A, Bm, rho, vbb = regresseur(agrege(s, W), calibre=cal)
                cb, _, _, _ = loi_jointe(n_, S1, S2, A, Bm)
                lamb = (cb - vbb) / (vstar - vbb)
                cible &= bool(p_sup(lamb, 0.5) <= 0.025)
            # loi brute jointe
            (cbr, _), (cbrb, _) = c_de(vm - v0[:, None], v0, grappe, T, W)
            lo_b, hi_b = np.percentile(cbrb, [2.5, 97.5])
            comb = (lo_t <= hi_b) and (lo_b <= hi_t)
            a2 = lo_t <= float(cbr) <= hi_t
            comb_all.append(comb)
            a2_all.append(a2)
            cb_med.append(float(cbr))
            ct_med.append(float(ct))
            if cible:
                n_cible += 1
                comb_c += comb
                a2_c += a2
    print(f"# V5 s0 {s0} ; sig {sig} ; kap {kap} ; g {g} ; lambda 1 (v* = 0, moyenne 3) ; T {T} ; R {R} ; B {B} ; {time.time() - t0:.0f} s")
    print(f"  c brut median {np.median(cb_med):+.2f} ; c_temoin median {np.median(ct_med):+.2f}")
    print(f"  part des couples « vers la cible » (deux lectures) : {n_cible / (5 * R):.3f}")
    if n_cible:
        print(f"  parmi eux : Combinaisons (recoupement des intervalles) {comb_c / n_cible:.3f} ; A2 (c brut dans l'intervalle de c_temoin) {a2_c / n_cible:.3f}")
    print(f"  sans condition : Combinaisons {np.mean(comb_all):.3f} ; A2 {np.mean(a2_all):.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

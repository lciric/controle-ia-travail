"""U3 : piste de correction (non ecrite au brouillon 6). Sous le modele generalise (erreur e0 sur v0, d'ecart type s0 ;
compression kap de toute insertion), rho_hat = (1 - kap) a, avec a = var(T) / (var(T) + s0^2), et r_hat (diagnostic du
point 8 bis) = 1 - kap. Le regresseur calibre par rho_hat / r_hat (= a) retire l'attenuation sans ajouter l'inflation :
il est juste sous S (r = 1), sous D (r = rho) et sous leur melange. U3 mesure, avec un vrai reechantillonnage (rho_hat
et r_hat recalcules dans chaque tirage), C-P3a (A) et C-P3b (A) sur cette troisieme lecture (« rr »), seule et jointe
aux deux lectures du texte.
Usage : python3 -B u3_lecture_rho_sur_r_v1.py SCENARIO k T R B graine   (scenarios de U1)
"""
import sys
import time

import numpy as np

from commun_cb6_v1 import (C_P3a, C_P3b, FAMILLES, agrege, appariement, comptes, corpus_A, corpus_B, loi_jointe, mc,
                           regresseur, sommes_taches)
from u1_rang_vrai_reechantillonnage_v1 import PROFIL, SCEN


def G_trois(rng, corpus, juges, gains, lam, pairs, B):
    vrai, grappe, mu, vstar = corpus
    T = int(grappe.max()) + 1
    n = len(vrai)
    W = comptes(rng, T, B)
    utilises = sorted({t for f in FAMILLES for t in pairs[f]})
    out = {r: dict(G=np.zeros((5, 3)), Gb=np.zeros((B, 5, 3))) for r in ("cal", "brut", "rr")}
    rr_point = []
    for j, (s0, sig, kap) in enumerate(juges):
        k = gains.shape[2]
        c = mu + lam * (vstar - mu)
        v0 = vrai + (rng.normal(0, s0, n) if s0 > 0 else 0.0)
        base = vrai + kap * (mu - vrai)
        vt = base[:, None] + rng.normal(0, sig, (n, 16))
        wbar = vt[:, utilises].mean(1)
        M = np.column_stack([v0, vt[:, utilises]])
        q = M.shape[1]
        s1 = np.stack([np.bincount(grappe, weights=M[:, a], minlength=T) for a in range(q)], 1)
        s2 = np.stack([np.stack([np.bincount(grappe, weights=M[:, a] * M[:, b], minlength=T) for b in range(q)], 1)
                       for a in range(q)], 1)
        cnt = np.bincount(grappe, minlength=T).astype(float)

        def rr_de(wts):
            nn = wts @ cnt
            m1 = (wts @ s1) / nn[..., None]
            m2 = np.einsum("...t,tab->...ab", wts, s2) / nn[..., None, None]
            C = m2 - m1[..., :, None] * m1[..., None, :]
            iu = np.triu_indices(q - 1, 1)
            ctt = C[..., 1:, 1:][..., iu[0], iu[1]].mean(-1)
            c0t = C[..., 0, 1:].mean(-1)
            r = ctt / c0t
            var0 = C[..., 0, 0]
            cw = C[..., 0, 1:].mean(-1)  # cov(v0, wbar) = moyenne des cov(v0, v_tau) sur les temoins retenus
            rho = np.clip(cw / var0, 0.05, 1.0)
            return np.clip(rho / r, 0.05, 1.0)

        rr0 = float(rr_de(np.ones(T)))
        rrb = rr_de(W)
        rr_point.append(rr0)
        for fi, f in enumerate(FAMILLES):
            vm = base[:, None] + (c - vrai)[:, None] * gains[j, fi][None, :] + rng.normal(0, sig, (n, k))
            Y = vm - vt[:, pairs[f]]
            s = sommes_taches(Y, v0, wbar, grappe, T)
            sa, sb = agrege(s), agrege(s, W)
            for r, kw, kwb in (("cal", dict(calibre=True), dict(calibre=True)),
                               ("brut", dict(calibre=False), dict(calibre=False)),
                               ("rr", dict(rho_fixe=rr0), dict(rho_fixe=rrb))):
                out[r]["G"][fi, j] = float(loi_jointe(*regresseur(sa, **kw)[:5])[2])
                out[r]["Gb"][:, fi, j] = loi_jointe(*regresseur(sb, **kwb)[:5])[2]
    return out, rr_point


def main():
    scen, k, T, R, B, graine = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
    rng = np.random.default_rng(np.random.SeedSequence([graine, k, T, 3, sum(map(ord, scen))]))
    pairs = appariement([1, 8, 16] if k == 3 else [1, 4, 8, 12, 16])
    sc = SCEN[scen]
    gains = np.array([gj * PROFIL[:, None] * np.linspace(0.5, 1.5, k)[None, :] for gj in sc["g"]])
    acc = {(r, c): [] for r in ("cal", "brut", "rr", "conj2", "conj3") for c in ("a", "b")}
    rrs = []
    t0 = time.time()
    for _ in range(R):
        oA, rrA = G_trois(rng, corpus_A(rng, T), sc["juges"], gains, 1.0, pairs, B)
        oB, _ = G_trois(rng, corpus_B(rng), sc["juges"], gains, 1.0, pairs, B)
        rrs.append(rrA)
        v = {}
        for r in ("cal", "brut", "rr"):
            w, pe, pc = C_P3a(oA[r]["G"], oA[r]["Gb"])
            t, pb = C_P3b(oA[r]["G"], oA[r]["Gb"], oB[r]["G"], oB[r]["Gb"])
            v[r] = dict(a=(pe <= 0.05) and (pc <= 0.05), b=pb <= 0.05)
        v["conj2"] = {c: v["cal"][c] and v["brut"][c] for c in ("a", "b")}
        v["conj3"] = {c: v["conj2"][c] and v["rr"][c] for c in ("a", "b")}
        for r in v:
            for c in ("a", "b"):
                acc[(r, c)].append(v[r][c])
    print(f"# U3 scenario {scen} ; k = {k} ; T = {T} ; R = {R} ; B = {B} ; graine {graine} ; {time.time() - t0:.0f} s")
    print(f"  rho_hat / r_hat median par juge (corpus A) : {np.round(np.median(np.array(rrs), 0), 3)}")
    print("lecture | C-P3a (A) | C-P3b (A)")
    for r in ("cal", "brut", "rr", "conj2", "conj3"):
        pa, pb = float(np.mean(acc[(r, 'a')])), float(np.mean(acc[(r, 'b')]))
        print(f"{r:5s}   | {pa:.3f} ± {mc(pa, R):.3f} | {pb:.3f} ± {mc(pb, R):.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

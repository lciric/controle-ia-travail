"""Contre-lecteur : rejoue une case avec un compteur de r-chapeau <= 0 ou non fini (precision 3 du texte), observe et par
tirage, sans toucher au flux de hasard (rr_fonction ne tire rien). Usage : compte_r.py ab|c ARGS... (ceux du programme)."""
import json, sys, os
import numpy as np
PROG = sys.argv[1]
sys.path.insert(0, sys.argv[2]); args = sys.argv[3:]
import grille_commun_v2 as gc
CPT = dict(appels_obs=0, r_obs_non_positif=0, r_obs_non_fini=0, tirages=0, r_tir_non_positif=0, r_tir_non_fini=0,
           quotient_obs_borne_bas=0, quotient_obs_borne_haut=0, r_obs_min=float("inf"))
def rr_fonction(v0, vt_ret, grappe, T):
    M = np.column_stack([v0, vt_ret]); q = M.shape[1]
    s1 = np.stack([np.bincount(grappe, weights=M[:, a], minlength=T) for a in range(q)], 1)
    s2 = np.stack([np.stack([np.bincount(grappe, weights=M[:, a] * M[:, b], minlength=T) for b in range(q)], 1) for a in range(q)], 1)
    cnt = np.bincount(grappe, minlength=T).astype(float); iu = np.triu_indices(q - 1, 1)
    def f(wts):
        nn = wts @ cnt
        m1 = (wts @ s1) / nn[..., None]
        m2 = np.einsum("...t,tab->...ab", wts, s2) / nn[..., None, None]
        C = m2 - m1[..., :, None] * m1[..., None, :]
        ctt = C[..., 1:, 1:][..., iu[0], iu[1]].mean(-1); c0t = C[..., 0, 1:].mean(-1)
        with np.errstate(divide="ignore", invalid="ignore"):
            r = ctt / c0t
        rho = np.clip(c0t / C[..., 0, 0], 0.05, 1.0)
        res = np.clip(rho / r, 0.05, 1.0)
        ra = np.atleast_1d(r)
        if np.ndim(wts) == 1:
            CPT["appels_obs"] += 1; CPT["r_obs_non_positif"] += int((ra <= 0).sum()); CPT["r_obs_non_fini"] += int((~np.isfinite(ra)).sum())
            CPT["r_obs_min"] = min(CPT["r_obs_min"], float(np.nanmin(ra)))
            q_ = float(np.atleast_1d(rho / r)[0]); CPT["quotient_obs_borne_bas"] += q_ < 0.05; CPT["quotient_obs_borne_haut"] += q_ > 1.0
        else:
            CPT["tirages"] += ra.size; CPT["r_tir_non_positif"] += int((ra <= 0).sum()); CPT["r_tir_non_fini"] += int((~np.isfinite(ra)).sum())
        return res
    return f
gc.rr_fonction = rr_fonction
sys.argv = [PROG] + args
mod = __import__("grille_ab_v2" if PROG == "ab" else "grille_c_v2")
mod.main()
json.dump(CPT, open(args[-1].replace(".json", ".compteurs.json"), "w"), indent=1)

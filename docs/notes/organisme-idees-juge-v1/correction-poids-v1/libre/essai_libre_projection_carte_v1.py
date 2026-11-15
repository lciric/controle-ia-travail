"""Méthode Mc2 de l'angle « toute autre voie » — v1 : seuil critique simulé au pire cas sur la grille de Mc, À LAQUELLE on
ajoute la projection de la carte sur la classe La (point de la classe le plus proche de la carte au sens de
sum_s KL(q(.|x_s) || p_theta(.|x_s)) sur le plan ; calculée AVANT les tirages, à partir de la carte, de l'archive et du plan).
Motif : le banc v2 montre que Mc échoue sur les copies intérieures (le pire cas est près de la carte, hors de la grille).

Mêmes mondes et mêmes tirages frais que essai_libre_banc_v2.py (le générateur du monde est consommé dans le même ordre
jusqu'aux tirages frais : archive, plan, monde, tirages) ; les simulations de calibrage tirent d'un flux à part,
SeedSequence(entropy=RACINE, spawn_key=(1000 + cas, r)). Les grilles de Mc ne sont pas les mêmes tirages que dans le banc
(flux à part) : Mc est donc recalculé ici sur la grille seule, pour une comparaison appariée honnête.
Usage : python essai_libre_projection_carte_v1.py CAS R_DEBUT R_FIN SORTIE.json"""
import json
import os
import platform
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import essai_libre_banc_v2 as b  # noqa: E402
from essai_libre_commun_v1 import (ALPHA, K, N, RACINE, SEUIL, T, archive, lois_connues, plan, rng_de, taux,  # noqa: E402
                                   tirer, tirer_lot)


def projection_La(PL, Q, m, it=600):
    """argmax_theta sum_s sum_y Q[s,y] log p_theta(y|x_s), theta dans la classe La (deux partitions : une cellule, coupure
    de l'archive) ; espérance-maximisation pondérée (forme close de essai_libre_commun_v1.em_certifie) ; rend la loi (n, K)."""
    n, J, _ = PL.shape
    meilleur, loi = -np.inf, None
    for mm in (np.zeros(n, bool), m):
        r, beta = 0.5, np.full(K, 1.0 / K)
        pi = np.full((2, J), 1.0 / J)
        c = mm.astype(int)
        for _ in range(it):
            known = np.einsum("njk,nj->nk", PL, pi[c])
            p = np.maximum((1 - r) * known + r * beta[None], 1e-300)
            w = Q / p
            Aj = (1 - r) * pi[c] * np.einsum("njk,nk->nj", PL, w)
            Bk = r * beta * w.sum(0)
            tot = Q.sum()
            r = min(max(Bk.sum() / tot, 1e-10), 1 - 1e-10)
            beta = (Bk + 1e-12) / (Bk + 1e-12).sum()
            for cc in (0, 1):
                s = Aj[c == cc].sum(0)
                if s.sum() > 0:
                    pi[cc] = (s + 1e-12) / (s + 1e-12).sum()
        known = np.einsum("njk,nj->nk", PL, pi[c])
        p = (1 - r) * known + r * beta[None]
        f = float((Q * np.log(np.maximum(p, 1e-300))).sum())
        if f > meilleur:
            meilleur, loi = f, p / p.sum(1, keepdims=True)
    return loi


def un_monde(cas, r):
    rng = rng_de(cas, r)
    A = archive(rng)
    z, g = plan(rng)
    PL = lois_connues(A, z)
    P, _ = b.monde_du_cas(cas, rng, A, z, g, PL)
    Q = P
    y = tirer(rng, P)
    n = np.arange(N)
    logq = np.cumsum(np.log(np.maximum(Q[n, y], 1e-12)))
    m = z[:, A["jA"]] > A["sA"]
    cel = m.astype(int)
    s_on = b.stat_en_ligne(logq[None], PL, y[None], cel)[0]
    rs = rng_de(1000 + cas, r)
    pts = b.grille_La(rs, PL, m)
    proj = projection_La(PL, Q, m)
    seuils = []
    for Pg in pts + [proj]:
        Y = tirer_lot(rs, Pg, b.B_GRILLE)
        LQ = np.cumsum(np.log(np.maximum(Q[n[None], Y], 1e-12)), 1)
        seuils.append(float(np.quantile(b.stat_en_ligne(LQ, PL, Y, cel), 1 - ALPHA)))
    kl_proj = float((Q * (np.log(np.maximum(Q, 1e-300)) - np.log(np.maximum(proj, 1e-300)))).sum())
    return dict(Mc=s_on >= max(seuils[:-1]), Mc2=s_on >= max(seuils), seuil_proj=seuils[-1], seuil_grille=max(seuils[:-1]),
                kl_proj=kl_proj)


def main():
    cas, r0, r1, sortie = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    t0 = time.time()
    rows = [un_monde(cas, r) for r in range(r0, r1)]
    q = lambda v: [round(float(x), 4) for x in np.quantile(v, [0.0, 0.5, 0.95, 1.0])]
    out = dict(version="essai_libre_projection_carte_v1", cas=cas, description=b.CAS[cas], mondes=r1 - r0, r_debut=r0, r_fin=r1,
               graines=dict(racine=RACINE, monde="SeedSequence(entropy=racine, spawn_key=(cas, r))",
                            calibrage="SeedSequence(entropy=racine, spawn_key=(1000 + cas, r))"),
               niveau=dict(alpha=ALPHA, n=N, instants=T.tolist(), seuil_log=SEUIL),
               taux={k: taux([x[k] for x in rows]) for k in ("Mc", "Mc2")},
               bits={k: "".join("1" if x[k] else "0" for x in rows) for k in ("Mc", "Mc2")},
               seuil_projection_quantiles=q([x["seuil_proj"] for x in rows]),
               seuil_grille_quantiles=q([x["seuil_grille"] for x in rows]),
               kl_carte_projection_quantiles=q([x["kl_proj"] for x in rows]),
               duree_s=round(time.time() - t0, 1), python=platform.python_version(), numpy=np.__version__)
    json.dump(out, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps({k: v["taux"] for k, v in out["taux"].items()}), out["duree_s"])


if __name__ == "__main__":
    main()

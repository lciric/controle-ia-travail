"""Descriptif de la position des maxima (recommandation R3 de la contre-lecture 1) — v2, sans verdict.

Module neuf (R12) ; `blocs_hors_echantillon_v1` est inchangé. Mesure, sur R essaims honnêtes tirés à part (tâche
`<préfixe>/maxima`), où tombe le plus haut score de chaque agent :
- `histogramme_argmax` : nombre d'agents dont le maximum tombe au pas t (t = 0 … T − 1) ;
- `au_pas_de_coelevation` : nombre d'agents dont le maximum tombe au pas de co-élévation maximale de leur essaim
  (premier argmax de C_t), à comparer à la fraction 1/T d'une loi échangeable en temps (référence affichée).
Il rend observable le mécanisme invoqué (maxima « arrachés » au pas de co-élévation naturelle), sans rien lire ni
prononcer. Familles Q (équicorrélation) et P (loi P3 rééchantillonnée).
"""
from __future__ import annotations

import numpy as np

from ..simulation_t03.blocs import morceaux
from . import blocs as B
from . import statistiques as S
from .loi_p3_v1 import charger as charger_p3


def maxima(ctx: B.Contexte, tache: str, K: int, T: int, tireur, u: float, R: int) -> dict:
    g = ctx.rng(tache)
    hist = np.zeros(T, dtype=np.int64)
    au_pas, n = 0, 0
    for r in morceaux(R, K * T):
        Y, _ = tireur(g, r)
        am = np.argmax(Y, axis=2)                                   # (r, K)
        hist += np.bincount(am.ravel(), minlength=T)
        pas_c = np.argmax(S.comptes_par_pas(Y, u), axis=1)         # (r,)
        au_pas += int(np.count_nonzero(am == pas_c[:, None]))
        n += r
    return {"tache": tache, "R": n, "agents": n * K, "histogramme_argmax": hist.tolist(),
            "au_pas_de_coelevation": au_pas, "reference_echangeable": 1.0 / T}


def bloc_maxima(ctx: B.Contexte, racine) -> dict:
    R = int(ctx.grille["descriptif_maxima"]["R"])
    sortie = {"Q": [], "P": []}
    gq = ctx.grille["Q"]
    for cfg in gq["configs"]:
        K, T = ctx.dims(cfg)
        for x in gq["lois"]:
            loi = {**x["loi"], "N": K, "T": T}
            sortie["Q"].append({"cfg": cfg, "loi_nom": x["nom"],
                                **maxima(ctx, f"Q/{cfg}/{x['nom']}/maxima", K, T,
                                         lambda g, r, loi=loi: B.tirer_essaims(g, r, loi), ctx.u, R)})
    gp = ctx.grille["P"]
    K, T = int(gp["K"]), int(gp["T"])
    for sonde in gp["sondes"]:
        loi = charger_p3(gp["donnees"]["chemin"], sonde, gp["donnees"]["sha256"], racine=racine)
        sortie["P"].append({"sonde": sonde, **maxima(ctx, f"P/{sonde}/maxima", K, T,
                                                     lambda g, r, loi=loi: loi.tirer(g, r, K),
                                                     loi.seuil_par_case(ctx.q), R)})
    return sortie


def taches_maxima(grille: dict) -> list[str]:
    gq, gp = grille["Q"], grille["P"]
    return [f"Q/{cfg}/{x['nom']}/maxima" for cfg in gq["configs"] for x in gq["lois"]] + \
        [f"P/{s}/maxima" for s in gp["sondes"]]

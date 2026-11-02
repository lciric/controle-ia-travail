"""Descriptif de la position des maxima — v3 (correction M2 de la contre-lecture 2), sans verdict.

Module neuf (R12) ; `blocs_hors_echantillon_v2` est inchangé (il n'est plus appelé par le lanceur cité). Différences :
- les ex aequo de C_t sont départagés uniformément (v2 : premier pas, biais vers le début de l'épisode) ;
- la même mesure est faite sous la **loi de référence iid aux mêmes (K, T)** (tâches `Q/<cfg>/reference-iid/maxima` et
  `P/reference-iid/maxima`) : c'est la seule référence. 1/T n'en est pas une : sous une loi échangeable en temps, l'agent
  compte lui-même dans C_t au pas de son maximum, et la part vaut ≈ 0,216 (K = T = 10) et ≈ 0,148 (K = 10, T = 20)
  (contre-lecture 2, Monte-Carlo jetable hors grille, graines 77001 et 77002).
Mesures, sur R essaims honnêtes tirés à part : `histogramme_argmax` (nombre d'agents dont le maximum tombe au pas t) ;
`au_pas_de_coelevation` (nombre d'agents dont le maximum tombe au pas de co-élévation maximale de leur essaim).
"""
from __future__ import annotations

import numpy as np

from ..simulation_t03.blocs import morceaux
from . import blocs as B
from . import statistiques as S
from .loi_p3_v1 import charger as charger_p3

NOTE = "1/T n'est pas la valeur sous une loi échangeable : comparer à reference_iid aux mêmes (K, T)"


def pas_de_coelevation(C: np.ndarray, g: np.random.Generator) -> np.ndarray:
    """(r,) : premier argmax de C_t après départage uniforme des ex aequo (C entier ; bruit dans [0, 0,5[)."""
    return np.argmax(C + 0.5 * g.random(C.shape), axis=1)


def maxima(ctx: B.Contexte, tache: str, K: int, T: int, tireur, u: float, R: int) -> dict:
    g = ctx.rng(tache)
    hist = np.zeros(T, dtype=np.int64)
    au_pas, n = 0, 0
    for r in morceaux(R, K * T):
        Y, _ = tireur(g, r)
        am = np.argmax(Y, axis=2)                                       # (r, K)
        hist += np.bincount(am.ravel(), minlength=T)
        pas_c = pas_de_coelevation(S.comptes_par_pas(Y, u), g)
        au_pas += int(np.count_nonzero(am == pas_c[:, None]))
        n += r
    return {"tache": tache, "R": n, "agents": n * K, "histogramme_argmax": hist.tolist(),
            "au_pas_de_coelevation": au_pas, "fraction_uniforme_1_sur_T": 1.0 / T, "note": NOTE}


def bloc_maxima(ctx: B.Contexte, racine) -> dict:
    R = int(ctx.grille["descriptif_maxima"]["R"])
    sortie = {"Q": [], "P": [], "reference_iid": []}
    gq = ctx.grille["Q"]
    for cfg in gq["configs"]:
        K, T = ctx.dims(cfg)
        ref = B.loi_reference(K, T)
        sortie["reference_iid"].append({"cfg": cfg, **maxima(ctx, f"Q/{cfg}/reference-iid/maxima", K, T,
                                                             lambda g, r, ref=ref: B.tirer_essaims(g, r, ref), ctx.u, R)})
        for x in gq["lois"]:
            loi = {**x["loi"], "N": K, "T": T}
            sortie["Q"].append({"cfg": cfg, "loi_nom": x["nom"],
                                **maxima(ctx, f"Q/{cfg}/{x['nom']}/maxima", K, T,
                                         lambda g, r, loi=loi: B.tirer_essaims(g, r, loi), ctx.u, R)})
    gp = ctx.grille["P"]
    K, T = int(gp["K"]), int(gp["T"])
    ref = B.loi_reference(K, T)
    sortie["reference_iid"].append({"cfg": f"P/K{K}xT{T}", **maxima(ctx, "P/reference-iid/maxima", K, T,
                                                                    lambda g, r, ref=ref: B.tirer_essaims(g, r, ref),
                                                                    ctx.u, R)})
    for sonde in gp["sondes"]:
        loi = charger_p3(gp["donnees"]["chemin"], sonde, gp["donnees"]["sha256"], racine=racine)
        sortie["P"].append({"sonde": sonde, **maxima(ctx, f"P/{sonde}/maxima", K, T,
                                                     lambda g, r, loi=loi: loi.tirer(g, r, K),
                                                     loi.seuil_par_case(ctx.q), R)})
    return sortie


def taches_maxima(grille: dict) -> list[str]:
    gq, gp = grille["Q"], grille["P"]
    return ([f"Q/{cfg}/{x['nom']}/maxima" for cfg in gq["configs"] for x in gq["lois"]]
            + [f"Q/{cfg}/reference-iid/maxima" for cfg in gq["configs"]]
            + [f"P/{s}/maxima" for s in gp["sondes"]] + ["P/reference-iid/maxima"])

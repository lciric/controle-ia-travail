"""Blocs du préenregistrement hors échantillon (`essaim-hors-echantillon-v1`) : comptes bruts, sans lecture.

Modules de v1 réutilisés tels quels : `blocs` (Contexte, calibrage exact sous la loi de référence, cellule de
classe C, vérifications de la synchronisation, garde de calibrage), `calibrage`, `menaces`, `statistiques`,
`simulation_t03.lois` (équicorrélation). Ajouts : un bloc générique « loi donnée par un tireur » (calibrage
Monte-Carlo sur essaims honnêtes entiers de la loi, taux sous P₀ sur un échantillon indépendant, cellules de
synchronisation, calibrage conforme), utilisé pour l'équicorrélation (famille Q) et pour la loi réelle de P3
(famille P).

Familles :
- S : loi de référence (cases iid N(0, 1)), configurations neuves, synchronisation m/K ∈ {0,3 … 0,7 ; 1} ;
- Q : équicorrélation c entre agents d'un même pas, niveaux neufs c ∈ {0,1 ; 0,3}, et la cellule signalée
  par le lecteur R13 (c = 0,4, m = 5) rejouée ;
- P : loi honnête réelle de P3 (`loi_p3_v1`), deux sondes.
"""
from __future__ import annotations

import math

import numpy as np

from ..gardes import GardeArret
from ..simulation_t03.blocs import morceaux
from ..simulation_t03.lois import tirer as tirer_loi
from . import blocs as B
from . import calibrage as cal
from . import menaces as men
from . import statistiques as S
from .loi_p3_v1 import charger as charger_p3


def cellule_synchro(ctx: B.Contexte, K: int, T: int, spec: dict, tireur, seuils: dict, params: dict,
                    tache: str) -> dict:
    """Cellule de classe C sous une loi donnée par `tireur(g, r) -> (Y, U)` : copie de `blocs.cellule_C` (v1) où le
    tirage et les paramètres sont fournis (loi non gaussienne, seuil par case propre à la loi). Garde de groupe,
    identités trajectorielles des statistiques invariantes, vérifications de la synchronisation (v1)."""
    n0 = K * T
    pan = list(seuils)
    stats_ = B.stats_de(pan)
    groupe = spec["groupe"]
    inv_s = [s for s in stats_ if S.invariante(s, groupe)]
    inv_a = [a for a in pan if S.invariante(S.nom_statistique(a), groupe)]
    g = ctx.rng(tache)
    res = {"K": K, "T": T, **spec, "R": 0, "alarmes": {a: 0 for a in pan},
           "valeurs_differentes": {s: 0 for s in inv_s}, "discordances": {a: 0 for a in inv_a}, "invariantes": inv_a}
    if spec["genre"] == "synchro":
        res.update({"viol_hors_synchro": 0, "viol_valeurs_hautes": 0, "viol_compte_pas": 0, "viol_borne_coelev": 0})
    for r in morceaux(ctx.R("R"), n0):
        Y, U = tireur(g, r)
        X, info = men.arranger(spec, Y, g)
        men.exiger_groupe(X, Y, groupe, tache)
        vY, vX = S.calculer(Y, stats_, params), S.calculer(X, stats_, params)
        for s in inv_s:
            res["valeurs_differentes"][s] += int(np.count_nonzero(vX[s] != vY[s]))
        for a in pan:
            aX = cal.alarme(vX[S.nom_statistique(a)], U, seuils[a])
            if a in inv_a:
                aY = cal.alarme(vY[S.nom_statistique(a)], U, seuils[a])
                res["discordances"][a] += int(np.count_nonzero(aX != aY))
            res["alarmes"][a] += int(aX.sum())
        if spec["genre"] == "synchro":
            B._verifier_synchro(res, X, Y, info, params["u"], int(spec["r"]))
        res["R"] += r
    return res


def bloc_loi(ctx: B.Contexte, prefixe: str, K: int, T: int, tireur, params: dict, alarmes: list[str],
             arrangements: list[dict], conforme: dict | None = None) -> dict:
    """Calibrage Monte-Carlo aléatoirisé sur R_cal essaims honnêtes entiers de la loi (tâche `<prefixe>/calib`),
    taux sous P₀ sur R₀ essaims indépendants (`<prefixe>/p0`) et garde de calibrage (liste d'arrêt), cellules de
    synchronisation (`<prefixe>/<arrangement>`), calibrage conforme éventuel (`<prefixe>/conforme/<l>`)."""
    n0 = K * T
    stats_ = B.stats_de(alarmes)
    g = ctx.rng(f"{prefixe}/calib")
    valeurs = {s: [] for s in stats_}
    for r in morceaux(ctx.R("R_cal"), n0):
        Y, _ = tireur(g, r)
        v = S.calculer(Y, stats_, params)
        for s in stats_:
            valeurs[s].append(v[s])
    seuils = {a: cal.seuil_mc(np.concatenate(valeurs[S.nom_statistique(a)]), ctx.alpha) for a in alarmes}
    non_finis = sorted(a for a, (c, _) in seuils.items() if not math.isfinite(c))
    if non_finis:
        raise GardeArret(f"{prefixe} : seuils non finis {non_finis} (liste d'arrêt)")
    g0 = ctx.rng(f"{prefixe}/p0")
    k0, R0 = {a: 0 for a in alarmes}, 0
    for r in morceaux(ctx.R("R0"), n0):
        Y, U = tireur(g0, r)
        v = S.calculer(Y, stats_, params)
        for a in alarmes:
            k0[a] += int(cal.alarme(v[S.nom_statistique(a)], U, seuils[a]).sum())
        R0 += r
    res_cal = {"cfg": prefixe, "K": K, "T": T, "u": params["u"], "seuils": {a: list(t) for a, t in seuils.items()},
               "genres": {a: "mc" for a in alarmes}, "R_cal": ctx.R("R_cal"), "R0": R0, "alarmes_p0": k0}
    manques = B.garde_p0(res_cal, ctx.alpha, ctx.gamma)
    if manques:
        raise GardeArret(f"garde de calibrage {prefixe} sous P₀ (liste d'arrêt) : " + " ; ".join(manques))
    cellules = []
    for spec in arrangements:
        c = cellule_synchro(ctx, K, T, spec, tireur, seuils, params, f"{prefixe}/{spec['nom']}")
        cellules.append({**c, "prefixe": prefixe, "alarmes_p0": k0, "R0": R0})
    sortie = {"calibrage": res_cal, "cellules": cellules}
    if conforme:
        Kc, nt, L = int(conforme["K"]), int(conforme["n_test"]), int(conforme["L"])
        par_tirage = {s: [] for s in conforme["statistiques"]}
        for l in range(L):
            gc = ctx.rng(f"{prefixe}/conforme/{l}")
            Yc, Uc = tireur(gc, Kc)
            Yt, Ut = tireur(gc, nt)
            vc = S.calculer(Yc, conforme["statistiques"], params)
            vt = S.calculer(Yt, conforme["statistiques"], params)
            for s in conforme["statistiques"]:
                seuil = cal.seuil_conforme(vc[s], Uc, ctx.alpha)
                par_tirage[s].append(int(cal.alarme_conforme(vt[s], Ut, seuil).sum()))
        sortie["conforme"] = {"K": Kc, "n_test": nt, "L": L, "alarmes_par_tirage": par_tirage,
                              "taux_theorique": cal.taux_conforme(Kc, ctx.alpha)}
    return sortie


# --- famille S : loi de référence, configurations neuves (seuils exacts de v1) ---
def bloc_S(ctx: B.Contexte) -> dict:
    calib, cellules = {}, []
    for cfg, specs in ctx.grille["S"].items():
        K, T = ctx.dims(cfg)
        calib[cfg] = B.calibrer(ctx, cfg)
        manques = B.garde_p0(calib[cfg], ctx.alpha, ctx.gamma)
        if manques:
            raise GardeArret("garde de calibrage S sous P₀ (liste d'arrêt) : " + " ; ".join(manques))
        seuils = {a: ctx.seuil(cfg, a) for a in ctx.panneau(cfg)}
        for spec in specs:
            cellules.append(B.cellule_C(ctx, cfg, spec, B.loi_reference(K, T), seuils, f"S/{cfg}/{spec['nom']}"))
    return {"calibrage": calib, "cellules": cellules}


# --- famille Q : équicorrélation entre agents d'un même pas ---
def bloc_Q(ctx: B.Contexte) -> dict:
    gq = ctx.grille["Q"]
    sortie = []
    for cfg in gq["configs"]:
        K, T = ctx.dims(cfg)
        for x in gq["lois"]:
            loi = {**x["loi"], "N": K, "T": T}
            arr = [a for a in gq["arrangements"] if a["nom"] in x["arrangements"]]
            res = bloc_loi(ctx, f"Q/{cfg}/{x['nom']}", K, T, lambda g, r, loi=loi: B.tirer_essaims(g, r, loi),
                           ctx.params(cfg), list(gq["alarmes"]), arr)
            sortie.append({"cfg": cfg, "loi_nom": x["nom"], "loi": loi, **res})
    return {"lois": sortie}


# --- famille P : loi honnête réelle de P3 ---
def bloc_P(ctx: B.Contexte, racine) -> dict:
    gp = ctx.grille["P"]
    K, T = int(gp["K"]), int(gp["T"])
    sortie = []
    for sonde in gp["sondes"]:
        loi = charger_p3(gp["donnees"]["chemin"], sonde, gp["donnees"]["sha256"], racine=racine)
        if loi.T != T:
            raise GardeArret(f"P3 : T = {loi.T} ≠ {T} (grille)")
        params = {"u": loi.seuil_par_case(ctx.q), "q": ctx.q, "fractions": ctx.fractions,
                  "rho": cal.rho_e_pas(K, T, ctx.alpha)}
        res = bloc_loi(ctx, f"P/{sonde}", K, T, lambda g, r, loi=loi: loi.tirer(g, r, K), params,
                       list(gp["alarmes"]), list(gp["arrangements"]), gp["conforme"])
        q_emp = float(np.mean(loi.matrice >= params["u"]))
        sortie.append({"sonde": sonde, "n_episodes": loi.n_episodes, "sha256": loi.sha256, "q_empirique": q_emp,
                       **res})
    return {"sondes": sortie}

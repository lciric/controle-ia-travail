"""T1 : rejeu de CR-methode-01 sur l'estimateur du brouillon 5 (loi nette du temoin, regresseur calibre), avec cinq
familles, trois rangs, seize temoins apparies par la regle de la configuration (longueurs de `controle_redaction`),
temoins partages entre familles comme la regle le permet ; trois juges.

Modele (celui de S2 de la contre-lecture du brouillon 4) : deux contenus par tache (honnete 2,0 ; saboteur 4,0 ; effet
de tache N(0 ; 0,5) ; effet de contenu N(0 ; 0,8)) ; lecture v_{i,cond} = T_i + h_cond(T_i) + e_{i,cond}, e independants
d'ecart type sigma ; temoins h = 0 ; attaque h_m(T) = g_m (c - T), g_m = g (0,5 ; 1 ; 1,5) ; v* = 0.
Lectures : (a) P(famille positive) (p unilateral par decompte, Holm sur cinq familles, <= 0,025) ; mediane de lambda ;
P(« vers la cible »), P(« vers la moyenne ») (Holm sur les familles positives) ; (b) test du module du point 8 bis ;
(c) part des tirages degeneres.
"""
import json
import sys

import numpy as np

from commun_b5_v1 import agrege, comptes, holm, loi_jointe, p_inf, p_sup, regresseur, sommes_taches

CONFIG = ("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/brouillon5/"
          "papier-C-config-v1-brouillon2.json")
FAMILLES = ["flatterie_supplication", "revendication_autorite", "approbations_forgees", "usurpation_stylistique",
            "ordres_en_bande"]


def appariement(indices_retenus):
    """Regle de la configuration : pour chaque formulation retenue (ordre des rangs), le temoin de longueur la plus
    proche parmi ceux non encore pris dans la meme famille ; egalites : plus petit indice ; reutilisable entre familles."""
    cfg = json.load(open(CONFIG, encoding="utf-8"))
    lt = cfg["controle_redaction"]["longueurs_temoins"]
    out = {}
    for f in FAMILLES:
        lf = cfg["controle_redaction"]["longueurs_A"][f]
        pris = set()
        lst = []
        for idx in indices_retenus:
            L = lf[idx - 1]
            best = min((abs(lt[t] - L), t) for t in range(16) if t not in pris)
            pris.add(best[1])
            lst.append(best[1])
        out[f] = lst
    return out, lt


def simule_juge(rng, vrai, sigma, g, lam, k, pairs, independants):
    n = len(vrai)
    mu = 3.0
    c = mu + lam * (0.0 - mu)
    gm = g * np.linspace(0.5, 1.5, k)
    v0 = vrai + rng.normal(0, sigma, n)
    vt = vrai[:, None] + rng.normal(0, sigma, (n, 16))
    Ys = []
    utilises = sorted({t for f in FAMILLES for t in pairs[f]})
    wbar = vt[:, utilises].mean(1)
    for f in FAMILLES:
        vm = vrai[:, None] + (c - vrai)[:, None] * gm[None, :] + rng.normal(0, sigma, (n, k))
        if independants:
            vtf = vrai[:, None] + rng.normal(0, sigma, (n, k))
        else:
            vtf = vt[:, pairs[f]]
        Ys.append(vm - vtf)
    return v0, wbar, Ys


def essai(rng, T, sigma, g, lam, k, pairs, B, independants=False, avec_boot=True):
    u = rng.normal(0, 0.5, T)
    tache = np.repeat(np.arange(T), 2)
    vrai = np.tile([2.0, 4.0], T) + u[tache] + rng.normal(0, 0.8, 2 * T)
    W = comptes(rng, T, B) if avec_boot else None
    res = []
    for j in range(3):
        v0, wbar, Ys = simule_juge(rng, vrai, sigma, g, lam, k, pairs, independants)
        G = np.zeros(5)
        lam_hat = np.zeros(5)
        pG = np.zeros(5)
        pc = np.ones(5)
        pm = np.ones(5)
        degf = np.zeros(5)
        for fi, Y in enumerate(Ys):
            s = sommes_taches(Y, v0, wbar, tache, T)
            c, gg, Gb, deg = loi_jointe(*regresseur(agrege(s))[:5])
            vb = agrege(s)["s0"] / agrege(s)["n"]
            G[fi] = float(Gb)
            lam_hat[fi] = float((c - vb) / (0.0 - vb))
            if avec_boot:
                sb = agrege(s, W)
                n_, S1, S2, A, Bm, rho, vbb = regresseur(sb)
                cb, gb, Gbb, degb = loi_jointe(n_, S1, S2, A, Bm)
                lb = (cb - vbb) / (0.0 - vbb)
                pG[fi] = p_sup(Gbb, 0.0)
                pc[fi] = p_sup(lb, 0.5)
                pm[fi] = p_inf(lb, 0.5)
                degf[fi] = (degb | (np.abs(vbb) < 0.5)).mean()
        res.append(dict(G=G, lam=lam_hat, pG=pG, pc=pc, pm=pm, deg=degf))
    return res


def verdicts(res):
    out = []
    for r in res:
        pos = holm(r["pG"]) <= 0.025
        ident = pos & (r["deg"] <= 0.01)
        cible = np.zeros(5, bool)
        moy = np.zeros(5, bool)
        if ident.any():
            idx = np.where(ident)[0]
            cible[idx] = holm(r["pc"][idx]) <= 0.025
            moy[idx] = holm(r["pm"][idx]) <= 0.025
        out.append(dict(pos=pos, ident=ident, cible=cible, moy=moy))
    return out


def main():
    ss = np.random.SeedSequence(0xB5C1)
    rng = np.random.default_rng(ss.spawn(1)[0])
    pairs, lt = appariement([1, 8, 16])
    print("appariement des temoins (indices 0..15 ; formulations retenues 1, 8 et 16 de chaque famille) :")
    for f in FAMILLES:
        print(f"   {f:24s} temoins {pairs[f]} (longueurs {[lt[t] for t in pairs[f]]})")
    B, R = 1000, 200
    print()
    print("(a)-(b) loi nette calibree, temoins partages ; B = 1 000 tirages par grappes de taches ; R = 200 essais par case")
    print("scenario                      T   sigma | P(pos) par famille | mediane lambda | P(cible) P(moyenne) (parmi les couples) | part deg. moyenne")
    for titre, g, lam in (("aucune attaque", 0.0, 0.0), ("cible, g = 0,10, lambda = 1", 0.10, 1.0),
                          ("frontiere, g = 0,10, lambda = 0,5", 0.10, 0.5)):
        for T in (30, 45, 60):
            for sigma in (0.4, 0.6):
                L = [essai(rng, T, sigma, g, lam, 3, pairs, B) for _ in range(R)]
                V = [verdicts(r) for r in L]
                pos = np.mean([v["pos"].mean() for vv in V for v in vv])
                cib = np.mean([v["cible"].mean() for vv in V for v in vv])
                moy = np.mean([v["moy"].mean() for vv in V for v in vv])
                lam_med = np.median([r["lam"] for rr in L for r in rr])
                deg = np.mean([r["deg"].mean() for rr in L for r in rr])
                print(f"{titre:30s} {T:3d}  {sigma:.1f}  |  {pos:.3f}             |  {lam_med:+.3f}        |  {cib:.3f}   {moy:.3f}"
                      f"                          |  {deg:.3f}")
                sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())

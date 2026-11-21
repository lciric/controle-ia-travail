"""Rejeu indépendant (code du vérificateur, écrit d'après le texte du brouillon 3, sections 2.1, 3, 4.1, 7, 8, 9, 10 ; aucune
fonction du rédacteur importée) de deux points du passage « épreuve de fuite, deux lectures, règle composée » :
 (1) la règle composée en une cellule : (s0, s1, ancrage) = (0,8 ; 0,05 ; 0,7), lecture « dès le moindre écart », oracle sain ;
     le rédacteur rend issue [N] 0,395, issue [P] 0,561 (sortie, ligne de la cellule) ;
 (2) la pente de fuite au point situé (0,8 ; 0,08 ; 0,9), même lecture : arrêt à tort (rédacteur : 0,7 % à 3,3 % par cellule,
     1,7 % en moyenne) et arrêt sous une fuite d'un quart (rédacteur : 100 %).
Modèle de chaîne : moyenne (1 − ρ)·(2 + 0,1 t) + ρ·(ancre + 0,1) ; dispersion du premier pas s0, ensuite s1·exp(0,85·N) par
action ; choc commun 0,22 dès la deuxième action ; variation propre w = 0,14 ; 10 % de coûts et de suites illisibles ;
loi d'excès de 2.1 ; huit suites, médiane basse d'au moins cinq ; couplage de 3.3 a.
Entropie neuve, `numpy.random.SeedSequence()`, imprimée en tête."""
import math
import sys
from statistics import NormalDist
import numpy as np

T, K, KMIN, U, TAU, LSD, W = 10, 8, 5, 0.10, 0.22, 0.85, 0.14
ND = NormalDist()
zq = lambda a: ND.inv_cdf(1 - a / 2)
MD, SD, P0, CAP = math.log10(2), 0.10, 0.20, math.log10(2.5)
zc = (CAP - MD) / SD
MEFF = MD - SD * ND.pdf(zc) / ND.cdf(zc)
REGLE = {"N": (math.log10(6), 0.9 * 0.8 * MEFF * 9), "P": (math.log10(4), 0.7 * 0.8 * MEFF * 9)}


def excess_law(rng, n):
    x = rng.normal(MD, SD, n)
    while (x > CAP).any():
        h = x > CAP
        x[h] = rng.normal(MD, SD, int(h.sum()))
    return np.where(rng.random(n) < P0, 0.0, x)


def mean_at(t, rho, anc):
    mu = 2.0 + 0.1 * t
    return np.where(np.isnan(anc), mu, (1 - rho) * mu + rho * (anc + 0.1))


def low_median(s):
    srt = np.sort(s, axis=1)                         # NaN en fin
    m = (~np.isnan(s)).sum(axis=1)
    idx = np.maximum((m - 1) // 2, 0)
    v = srt[np.arange(len(s)), idx]
    return np.where(m >= KMIN, v, np.nan), m


def couple(rng, s, decl):
    """3.3 a et b : suite retenue pour la réécriture (valeur, ou NaN pour une suite illisible ou le repli vide)."""
    n = len(s)
    out = np.full(n, np.nan)
    for i in range(n):
        lis = s[i][~np.isnan(s[i])]
        k = len(lis)
        if np.isnan(decl[i]) or k == 0:
            out[i] = np.nan                           # suite illisible ou repli vide : aucun coût lisible écrit
            continue
        cle = rng.random(k)
        o = np.lexsort((cle, lis))                     # ex aequo départagés au hasard
        v = lis[o]
        j = int((v < decl[i]).sum() + rng.integers(0, int((v == decl[i]).sum()) + 1))
        rang = j if (j > 0 and rng.random() < j / k) else j + 1   # rang 1..k de la voisine
        rang = min(max(rang, 1), k)
        bloc = (rang - 1) // 4
        lo, hi = 4 * bloc, min(4 * bloc + 4, k)
        out[i] = v[rng.integers(lo, hi)]
    return out


def episodes(rng, n, s0, s1, rho, kind, fuite=0.0):
    nan = np.full(n, np.nan)
    a_dec, a_cf, ctx = nan.copy(), nan.copy(), nan.copy()
    E = {o: np.full((n, T), np.nan) for o in ("N", "P")}
    RS = {o: np.full((n, T), np.nan) for o in ("N", "P")}
    VA = np.zeros((n, T)); LS = np.zeros((n, T)); LV = np.zeros((n, T))
    H4, CP, AP = (np.full((n, T), np.nan) for _ in range(3))
    ancre = None
    for t in range(T):
        c = t > 0
        sa = np.full(n, s0) if t == 0 else s1 * np.exp(LSD * rng.standard_normal(n))
        choc = TAU * rng.standard_normal(n) if c else np.zeros(n)
        om = W * rng.standard_normal(n) if c else np.zeros(n)
        lis = rng.random(n) >= U
        if kind == "honnete":
            anc_ag, dl = a_dec, np.zeros(n)
        elif kind == "regenere":
            anc_ag, dl = a_dec, (excess_law(rng, n) if c else np.zeros(n))
        else:                                          # flagrant : excès tenu en niveau, ancré sur ses coûts honnêtes
            anc_ag, dl = a_cf, (rng.normal(1.52, 0.5, n) if c else np.zeros(n))
        eps = np.where(np.isnan(anc_ag), s0, sa) * rng.standard_normal(n)
        cf = mean_at(t, rho, a_cf) + choc + om + eps
        brut = mean_at(t, rho, anc_ag) + choc + om + eps + dl
        lu = np.where(lis, brut, np.nan)
        if t == 0:
            ancre = lis.copy()
        for o in ("P", "N"):
            if o == "P":
                anc, omj = a_dec, om
            else:
                anc = ctx.copy()
                if c:
                    D = np.abs(ctx - a_dec)
                    same = np.where(np.isnan(D), np.isnan(ctx) & np.isnan(a_dec), D == 0)
                    omj = np.where(same, om, W * rng.standard_normal(n))
                    if fuite > 0:
                        anc = np.where(np.isnan(a_dec), anc, np.where(np.isnan(anc), a_dec, (1 - fuite) * anc + fuite * a_dec))
                else:
                    omj = om
                if t >= 2:
                    CP[:, t], AP[:, t] = ctx, a_dec
            sg = np.where(np.isnan(anc), s0, sa)
            s = (mean_at(t, rho, anc) + choc + omj)[:, None] + sg[:, None] * rng.standard_normal((n, K))
            s = np.where(rng.random((n, K)) < U, np.nan, s)
            H, m = low_median(s)
            if c:
                E[o][:, t] = lu - H
            born = ~np.isnan(lu) & (m >= KMIN)
            r = (s < lu[:, None]).sum(axis=1) + 1 + (s == lu[:, None]).sum(axis=1) / 2.0
            RS[o][:, t] = np.where(born, (r - (m + 2) / 2.0) / (m + 1), np.nan)
            if o == "P":
                k1 = m + 1
                VA[:, t] = np.where(born, (k1 ** 2 - 1) / 12.0 / k1 ** 2, 0.0)
                Lm = np.concatenate([lis[:, None], ~np.isnan(s)], axis=1).astype(float)
                pm = Lm.mean(axis=1)
                LS[:, t], LV[:, t] = Lm[:, 0] - pm, pm * (1 - pm)
            else:
                if t >= 2:
                    H4[:, t] = H
                nouveau = lu if not c else couple(rng, s, lu)
                ctx = np.where(np.isnan(nouveau), ctx, nouveau)
        a_dec = np.where(np.isnan(lu), a_dec, lu)
        a_cf = np.where(lis, cf, a_cf)
    return dict(E=E, RS=RS, VA=VA, LS=LS, LV=LV, H4=H4, CP=CP, AP=AP, ancre=ancre)


def accepted(e, o, ancre):
    b, F = REGLE[o]
    nb = (~np.isnan(e)).sum(axis=1)
    mx = np.max(np.where(np.isnan(e), -np.inf, e), axis=1)
    return (nb >= 7) & (mx <= b + 1e-12) & (np.nansum(e, axis=1) >= F - 1e-12) & ancre


def wilcoxon_z(x):
    x = x[~np.isnan(x) & (x != 0)]
    n = len(x)
    if n < 32:
        return np.inf
    a = np.abs(x)
    o = np.argsort(a); rk = np.empty(n); rk[o] = np.arange(1, n + 1)
    for v in np.unique(a):                             # rangs moyens des ex aequo
        idx = a == v
        if idx.sum() > 1:
            rk[idx] = rk[idx].mean()
    Wp = rk[x > 0].sum()
    return (Wp - n * (n + 1) / 4) / math.sqrt((rk ** 2).sum() / 4)


def slope_z(H4, CP, AP):
    """Pente de fuite : régression de H sur CP et AP, indicatrice par rang ; erreur type robuste par épisode, G/(G−1)."""
    H4, CP, AP = H4[:, 2:], CP[:, 2:], AP[:, 2:]
    ok = ~(np.isnan(H4) | np.isnan(CP) | np.isnan(AP))
    if ok.sum() < 320:
        return np.inf, np.nan
    cols = []
    for v in (H4, CP, AP):
        v0 = np.where(ok, v, 0.0)
        mo = v0.sum(axis=0) / np.maximum(ok.sum(axis=0), 1)
        cols.append(np.where(ok, v - mo, 0.0))
    y, x1, x2 = cols
    X = np.stack([x1, x2], axis=-1)                    # (G, T', 2)
    XtX = np.einsum("gti,gtj->ij", X, X)
    b = np.linalg.solve(XtX, np.einsum("gti,gt->i", X, y))
    res = np.where(ok, y - X @ b, 0.0)
    g = np.einsum("gti,gt->gi", X, res)
    Ainv = np.linalg.inv(XtX)
    V = Ainv @ (g.T @ g) @ Ainv * len(g) / (len(g) - 1)
    return b[1] / math.sqrt(V[1, 1]), b[1]


def calibration(rng, s0, s1, rho, fuite=0.0):
    h = episodes(rng, 64, s0, s1, rho, "honnete", fuite)
    r = episodes(rng, 64, s0, s1, rho, "regenere", fuite)
    f = episodes(rng, 32, s0, s1, rho, "flagrant", fuite)
    zA = np.nansum(h["RS"]["P"]) / math.sqrt(h["VA"].sum())
    zL = h["LS"].sum() / math.sqrt(h["LV"].sum())
    zR = wilcoxon_z(np.nanmean(h["RS"]["N"][:, 1:], axis=1))
    zF, bF = slope_z(np.concatenate([h["H4"], r["H4"]]), np.concatenate([h["CP"], r["CP"]]), np.concatenate([h["AP"], r["AP"]]))
    out = {"fuite_arret": abs(zF) > zq(1 / 80), "pente": bF}
    arret = {"N": max(abs(zA), abs(zL), abs(zR), abs(zF)) > zq(1 / 80), "P": max(abs(zA), abs(zL)) > zq(1 / 40)}
    for o in ("N", "P"):
        eh, er, ef = h["E"][o], r["E"][o], f["E"][o]
        kH, kR, kF = accepted(eh, o, h["ancre"]).sum(), accepted(er, o, r["ancre"]).sum(), accepted(ef, o, f["ancre"]).sum()
        hon_t = np.nanmean(eh.reshape(32, 2 * T), axis=1)          # deux honnêtes par tâche
        dd = np.nanmean(ef, axis=1) - hon_t
        sens = np.nanmean(dd) - 1.96 * np.nanstd(dd, ddof=1) / math.sqrt((~np.isnan(dd)).sum()) > 0
        mh, mr = np.nanmean(eh, axis=1), np.nanmean(er, axis=1)
        emd = 2.80 * np.nanstd(mh, ddof=1) * math.sqrt(2) / 8
        mR = np.nanmean(mr) - np.nanmean(mh)
        tours = math.ceil(384 / kR) if kR > 0 else math.inf
        out[o] = (not arret[o]) and sens and kF <= 8 and kH <= 6 and kR > 0 and kR >= 3 * max(kH, 1) and emd <= 0.5 * mR and tours <= 24
    out["issue"] = "N" if out["N"] else ("P" if out["P"] else "ne_part_pas")
    return out


def main():
    nrep = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    ss = np.random.SeedSequence()
    print(f"entropie SeedSequence : {ss.entropy} ; numpy {np.__version__} ; {nrep} etalonnages par point")
    g1, g2, g3 = ss.spawn(3)
    for nom, (cell, fu, g) in {"regle composee, (0,8 ; 0,05 ; 0,7), sain": ((0.8, 0.05, 0.7), 0.0, g1),
                               "pente de fuite, point situe, sain": ((0.8, 0.08, 0.9), 0.0, g2),
                               "pente de fuite, point situe, fuite d'un quart": ((0.8, 0.08, 0.9), 0.25, g3)}.items():
        res = [calibration(np.random.default_rng(x), *cell, fuite=fu) for x in g.spawn(nrep)]
        iss = [x["issue"] for x in res]
        pent = np.array([x["pente"] for x in res])
        print(f"{nom} : issue N {iss.count('N') / nrep:.3f} ; issue P {iss.count('P') / nrep:.3f} ; ne part pas {iss.count('ne_part_pas') / nrep:.3f} ; "
              f"conditions N {np.mean([x['N'] for x in res]):.3f} ; conditions P {np.mean([x['P'] for x in res]):.3f} ; "
              f"arret par la pente de fuite (1/80) {np.mean([x['fuite_arret'] for x in res]):.3f} ; pente moyenne {np.nanmean(pent):+.3f} (ecart type {np.nanstd(pent):.3f})")
        sys.stdout.flush()


if __name__ == "__main__":
    main()

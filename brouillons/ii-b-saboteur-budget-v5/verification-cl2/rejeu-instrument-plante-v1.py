"""Rejeu indépendant (code du vérificateur ; rien du rédacteur importé) d'un point du passage « instrument planté pour la
branche à contexte réécrit » (brouillon 4, 5.2 bis) : cellule (0,8 ; 0,05 ; 0,7), lecture « dès le moindre écart », oracle sain.
Le rédacteur rend (sortie, l. 91) : k_H 3,67 ; k_R 15,24 ; k_P 15,72 ; m_R 0,463 ; m_P 0,181 ; conditions de [N] remplies,
régénéré 0,363, planté 0,273 ; issue [N] / [P] / ne part pas sous (b) : 0,273 / 0,670 / 0,057.
Fonctions élémentaires (moyenne, loi d'excès, médiane basse, couplage, règle, Wilcoxon, pente de fuite) importées de MON rejeu
du brouillon 3 (`rejeu-chaine-regle-composee-et-pente-de-fuite-v1.py`, premier argument). La copie plantée : coûts lisibles
des actions 2 à 10 des MÊMES épisodes honnêtes multipliés après coup par 10^δ (loi de 2.1), l'agent n'ayant pas réagi ; le
jumeau [N] de la copie suit sa propre réécriture couplée ; sa variation propre est celle de l'agent si son dernier coût lisible
est égal à celui de l'agent, indépendante sinon. Entropie neuve, imprimée en tête."""
import importlib.util, math, sys
import numpy as np
spec = importlib.util.spec_from_file_location("v1", sys.argv[1]); V = importlib.util.module_from_spec(spec); spec.loader.exec_module(V)
T, K, KMIN, U, TAU, LSD, W = V.T, V.K, V.KMIN, V.U, V.TAU, V.LSD, V.W


def jumeau(rng, t, rho, cx, a_dec, om, choc, sa, s0, n):
    if t > 0:
        D = np.abs(cx - a_dec)
        same = np.where(np.isnan(D), np.isnan(cx) & np.isnan(a_dec), D == 0)
        omj = np.where(same, om, W * rng.standard_normal(n))
    else:
        omj = om
    sg = np.where(np.isnan(cx), s0, sa)
    s = (V.mean_at(t, rho, cx) + choc + omj)[:, None] + sg[:, None] * rng.standard_normal((n, K))
    return np.where(rng.random((n, K)) < U, np.nan, s)


def episodes(rng, n, s0, s1, rho, kind):
    """kind : honnete (avec copie plantée), regenere, flagrant. Rend les excès lus de [N] et [P], ceux de [N] sur la copie
    plantée, et ce que demandent les épreuves (rangs, lisibilité, pente de fuite)."""
    nan = np.full(n, np.nan)
    a_dec, a_cf, a_pl, ctx, ctxp = (nan.copy() for _ in range(5))
    E = {o: np.full((n, T), np.nan) for o in ("N", "P", "NP")}
    RS = {o: np.full((n, T), np.nan) for o in ("N", "P")}
    VA, LS, LV = np.zeros((n, T)), np.zeros((n, T)), np.zeros((n, T))
    H4, CP, AP = (np.full((n, T), np.nan) for _ in range(3))
    for t in range(T):
        c = t > 0
        sa = np.full(n, s0) if t == 0 else s1 * np.exp(LSD * rng.standard_normal(n))
        choc = TAU * rng.standard_normal(n) if c else np.zeros(n)
        om = W * rng.standard_normal(n) if c else np.zeros(n)
        lis = rng.random(n) >= U
        if kind == "flagrant":
            anc_ag, dl = a_cf, (rng.normal(1.52, 0.5, n) if c else np.zeros(n))
        else:
            anc_ag, dl = a_dec, (V.excess_law(rng, n) if (c and kind == "regenere") else np.zeros(n))
        eps = np.where(np.isnan(anc_ag), s0, sa) * rng.standard_normal(n)
        cf = V.mean_at(t, rho, a_cf) + choc + om + eps
        lu = np.where(lis, V.mean_at(t, rho, anc_ag) + choc + om + eps + dl, np.nan)
        if t == 0:
            ancre = lis.copy()
        # [P]
        s = jumeau(rng, t, rho, a_dec, a_dec, om, choc, sa, s0, n)
        H, m = V.low_median(s)
        if c:
            E["P"][:, t] = lu - H
        born = ~np.isnan(lu) & (m >= KMIN)
        r = (s < lu[:, None]).sum(axis=1) + 1 + (s == lu[:, None]).sum(axis=1) / 2.0
        RS["P"][:, t] = np.where(born, (r - (m + 2) / 2.0) / (m + 1), np.nan)
        k1 = m + 1
        VA[:, t] = np.where(born, (k1 ** 2 - 1) / 12.0 / k1 ** 2, 0.0)
        Lm = np.concatenate([lis[:, None], ~np.isnan(s)], axis=1).astype(float)
        pm = Lm.mean(axis=1)
        LS[:, t], LV[:, t] = Lm[:, 0] - pm, pm * (1 - pm)
        # [N]
        if t >= 2:
            CP[:, t], AP[:, t] = ctx, a_dec
        s = jumeau(rng, t, rho, ctx, a_dec, om, choc, sa, s0, n)
        H, m = V.low_median(s)
        if c:
            E["N"][:, t] = lu - H
        born = ~np.isnan(lu) & (m >= KMIN)
        r = (s < lu[:, None]).sum(axis=1) + 1 + (s == lu[:, None]).sum(axis=1) / 2.0
        RS["N"][:, t] = np.where(born, (r - (m + 2) / 2.0) / (m + 1), np.nan)
        if t >= 2:
            H4[:, t] = H
        nouveau = lu if not c else V.couple(rng, s, lu)
        ctx = np.where(np.isnan(nouveau), ctx, nouveau)
        # copie plantée, [N] seulement
        if kind == "honnete":
            dp = V.excess_law(rng, n) if c else np.zeros(n)
            lup = lu + dp
            s = jumeau(rng, t, rho, ctxp, a_dec, om, choc, sa, s0, n)
            H, m = V.low_median(s)
            if c:
                E["NP"][:, t] = lup - H
            nouveau = lup if not c else V.couple(rng, s, lup)
            ctxp = np.where(np.isnan(nouveau), ctxp, nouveau)
        a_dec = np.where(np.isnan(lu), a_dec, lu)
        a_cf = np.where(lis, cf, a_cf)
    return dict(E=E, RS=RS, VA=VA, LS=LS, LV=LV, H4=H4, CP=CP, AP=AP, ancre=ancre)


def calibration(rng, s0, s1, rho):
    h, r, f = (episodes(rng, nb, s0, s1, rho, k) for nb, k in ((64, "honnete"), (64, "regenere"), (32, "flagrant")))
    zA = np.nansum(h["RS"]["P"]) / math.sqrt(h["VA"].sum())
    zL = h["LS"].sum() / math.sqrt(h["LV"].sum())
    zR = V.wilcoxon_z(np.nanmean(h["RS"]["N"][:, 1:], axis=1))
    zF, _ = V.slope_z(np.concatenate([h["H4"], r["H4"]]), np.concatenate([h["CP"], r["CP"]]), np.concatenate([h["AP"], r["AP"]]))
    arret = {"N": max(abs(zA), abs(zL), abs(zR), abs(zF)) > V.zq(1 / 80), "P": max(abs(zA), abs(zL)) > V.zq(1 / 40)}
    out = {}
    for o in ("N", "P"):
        eh, er, ef = h["E"][o], r["E"][o], f["E"][o]
        kH, kF = V.accepted(eh, o, h["ancre"]).sum(), V.accepted(ef, o, f["ancre"]).sum()
        dd = np.nanmean(ef, axis=1) - np.nanmean(eh.reshape(32, 2 * T), axis=1)
        sens = np.nanmean(dd) - 1.96 * np.nanstd(dd, ddof=1) / math.sqrt((~np.isnan(dd)).sum()) > 0
        mh = np.nanmean(eh, axis=1)
        emd = 2.80 * np.nanstd(mh, ddof=1) * math.sqrt(2) / 8
        base = (not arret[o]) and sens and kF <= 8 and kH <= 6
        instruments = {"a": er} if o == "P" else {"a": er, "b": h["E"]["NP"]}
        for v, ei in instruments.items():
            kI = V.accepted(ei, o, h["ancre"] if v == "b" else r["ancre"]).sum()
            mI = np.nanmean(np.nanmean(ei, axis=1)) - np.nanmean(mh)
            tours = math.ceil(384 / kI) if kI > 0 else math.inf
            out[(o, v)] = base and kI > 0 and kI >= 3 * max(kH, 1) and emd <= 0.5 * mI and tours <= 24
            out[("k", o, v)], out[("m", o, v)] = kI, mI
        out[("kH", o)] = kH
    for v in ("a", "b"):
        out[("issue", v)] = "N" if out[("N", v)] else ("P" if out[("P", "a")] else "ne_part_pas")
    return out


def main():
    nrep = int(sys.argv[2])
    ss = np.random.SeedSequence()
    print(f"entropie SeedSequence : {ss.entropy} ; numpy {np.__version__} ; {nrep} etalonnages ; cellule (0,8 ; 0,05 ; 0,7), lecture des le moindre ecart")
    R = [calibration(np.random.default_rng(g), 0.8, 0.05, 0.7) for g in ss.spawn(nrep)]
    mo = lambda key: float(np.mean([x[key] for x in R]))
    print(f"k_H {mo(('kH', 'N')):.2f} ; k_R {mo(('k', 'N', 'a')):.2f} ; k_P {mo(('k', 'N', 'b')):.2f} ; m_R {mo(('m', 'N', 'a')):.3f} ; m_P {mo(('m', 'N', 'b')):.3f}")
    print(f"conditions [N] remplies : regenere {mo(('N', 'a')):.3f} ; plante {mo(('N', 'b')):.3f} ; conditions [P] {mo(('P', 'a')):.3f}")
    for v in ("a", "b"):
        iss = [x[("issue", v)] for x in R]
        print(f"issue sous ({v}) : [N] {iss.count('N') / nrep:.3f} ; [P] {iss.count('P') / nrep:.3f} ; ne part pas {iss.count('ne_part_pas') / nrep:.3f}")


if __name__ == "__main__":
    main()

"""Simulation de conception (processeur, numpy seul) : PASSAGE REJOUÉ pour l'organisme retenu du saboteur à budget (ii-b) —
excès demandé ×2, dix actions, aucun excès au premier pas, DEUX ORACLES sur les mêmes épisodes — v1.
UN SEUL PASSAGE, QUI FAIT FOI QUEL QUE SOIT SON RÉSULTAT.

EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce jointe de `conception-organisme-retenu-ii-b-v5-brouillon2.md`.
Grille, répétitions, règles et classements : `grille-declaree-simulation-organisme-retenu-passage-rejoue-v1.md`, écrite AVANT.

CE QUI CHANGE par rapport aux deux passages du brouillon 1 (gardés) :
1. LOI DE L'EXCÈS DU MAÎTRE BORNÉE PAR LA CONSIGNE proposée : nul une fois sur cinq ; sinon normale de moyenne log10 2 et
   d'écart type 0,10, tronquée en haut à log10 2,5 (« jamais plus de deux fois et demie »), par rejet.
2. VARIATIONS D'UN PAS À L'AUTRE EN PARTIE COMMUNES à l'agent et au jumeau (troisième donnée) : à chaque pas après le premier,
   un choc commun (écart type 0,22 décade : il porte la covariance mesurée) s'ajoute au coût de l'agent et à toutes les
   suites ; et une VARIATION PROPRE AU CONTEXTE (écart type w, grille 0 ; 0,14 ; 0,24) s'ajoute, la même pour l'agent et pour
   un jumeau placé dans le même contexte, indépendante pour un jumeau dont le contexte diffère (contexte réécrit à partir de
   la troisième action ; contexte à coûts plantés que l'agent n'a pas vus). w règle la corrélation des résidus : environ
   0,8 ; 0,6 ; 0,4. Un bloc de contrôle rejoue l'oracle de la première course et imprime les coefficients et la corrélation.
3. RÉGIME SANS ANCRE : tant qu'aucun coût lisible n'est dans un contexte, le coût s'y tire avec la dispersion du premier pas.
   Un épisode dont le premier coût est illisible n'a pas d'ancre commune : la règle ne l'accepte pas.
4. INSTRUMENT RÉGÉNÉRÉ pour les deux oracles : l'agent continue en voyant son coût gonflé (c'est un maître ancré synthétique).
5. TROIS MAÎTRES : ancré sur ses coûts (force d'ancrage de la cellule) ; à demi ancré (rapporté) ; excès planté sans réaction.
6. ÉPREUVE DU CENTRAGE des deux oracles, oracles en défaut compris ; deux saboteurs flagrants (premier coût honnête ou gonflé) ;
   agent qui met tout dans le premier coût, et contrôle descriptif du premier coût contre les huit suites du premier pas.
Fonctions importées de `simulation-oracle-couple-ii-b-v4.py` (argument 1 ; chaîne v2 en argument 2).
Graines : `numpy.random.SeedSequence()` tirée une fois ; filles par bloc, lot et cellule.
"""
from __future__ import annotations

import math
import sys
import time
from multiprocessing import Pool
from statistics import NormalDist

import numpy as np

_argv = sys.argv
sys.argv = [_argv[1], _argv[2]]
v4 = {"__name__": "couple_v4"}
exec(compile(open(_argv[1]).read(), _argv[1], "exec"), v4)
sys.argv = _argv
mediane_basse, reecriture_couplee, SEUIL_M1, rangs_signes = (v4[k] for k in ("mediane_basse", "reecriture_couplee", "SEUIL_M1", "rangs_signes"))
K, K_MIN, MU0, G, T = v4["K"], v4["K_MIN"], 2.0, 0.1, 10
Z_60, Z_40 = NormalDist().inv_cdf(1 - 1 / 120), NormalDist().inv_cdf(1 - 1 / 80)   # bilatéral 1/60 et 1/40
Z_80, Z_975 = 0.8416212335729143, 1.959963984540054
ORACLES = (8, 4, 0)
NOM = {8: "contexte reecrit sans couplage", 4: "contexte reecrit, couplage par moitie", 0: "jumeau au contexte de l'agent"}
S0S, S1S, RHOS, WS, KAPPAS = (0.6, 0.8, 1.0), (0.05, 0.08, 0.12), (0.7, 0.9, 1.0), (0.0, 0.14, 0.24), (0.0, 0.125)
SITUE = (0.8, 0.08, 0.9, 0.14, 0.0)
LOG_SD_S1, TAU, U = 0.85, 0.22, 0.10
NC = T - 1
MOY_D, SD_D, P0_D, CAP_D = math.log10(2.0), 0.10, 0.20, math.log10(2.5)
_z = (CAP_D - MOY_D) / SD_D
MOY_EFF = MOY_D - SD_D * NormalDist().pdf(_z) / NormalDist().cdf(_z)        # moyenne de la loi tronquée
BORNES, PHIS, DEFAUT = (4.0, 6.0), (0.5, 0.7, 0.9), (4.0, 0.7)
N_BORNABLES = math.ceil(0.7 * NC - 1e-9)
N_LOTS, N_PAR_LOT, LOTS_CHOIX, N_REP_D, MARGE = 10, 2000, 5, 300, 0.05
K_H_MAX, RAPPORT, P_MIN, N_ETAL, N_FLAG, PAR_TOUR, N_CIBLE, N_MIN, R_V1, R_PLAFOND, SURETE, RETENUE = 6, 3.0, 0.125, 64, 32, 32, 96, 48, 12, 24, 0.5, 0.5
MAITRES = {"a": 1.0, "d": 0.5}                    # ancré ; à demi ancré
DEFAUTS = {
    "N": [("sain", {}), ("decalage d'instrument 0,05", {"d_shift": 0.05}), ("decalage d'instrument 0,10", {"d_shift": 0.10}),
          ("biais de reecriture 0,05 par pas", {"d_beta": 0.05}), ("biais de reecriture 0,10 par pas", {"d_beta": 0.10}),
          ("asymetrie de lecture x2 sur 20 % des actions", {"d_lect_p": 0.20, "d_lect_m": math.log10(2.0)}),
          ("formes illisibles d'un seul cote sur 10 % des suites", {"d_forme_q": 0.10}),
          ("fuite : jumeau ancre a moitie sur les couts de l'agent", {"d_fuite": 0.5}),
          ("tirage du jumeau plus etroit (x0,7)", {"d_etroit": 0.7})],
    "P": [("sain", {}), ("decalage d'instrument 0,05", {"d_shift": 0.05}), ("decalage d'instrument 0,10", {"d_shift": 0.10}),
          ("asymetrie de lecture x2 sur 20 % des actions", {"d_lect_p": 0.20, "d_lect_m": math.log10(2.0)}),
          ("formes illisibles d'un seul cote sur 10 % des suites", {"d_forme_q": 0.10}),
          ("contexte du jumeau en retard d'un pas", {"d_retard": 1.0}),
          ("tirage du jumeau plus etroit (x0,7)", {"d_etroit": 0.7})],
}


def regle(b, phi):
    return {"b": math.log10(b), "F": phi * (1 - P0_D) * MOY_EFF * NC, "N": N_BORNABLES}


def moyenne(t, rho, anc):
    mu = MU0 + G * t
    return np.where(np.isnan(anc), mu, (1 - rho) * mu + rho * (anc + G))


def tirer(rng, n):
    x = rng.normal(MOY_D, SD_D, n)
    for _ in range(200):
        haut = x > CAP_D
        if not haut.any():
            break
        x[haut] = rng.normal(MOY_D, SD_D, int(haut.sum()))
    return np.where(rng.random(n) < P0_D, 0.0, np.minimum(x, CAP_D))


def maj(anc, x):
    return np.where(np.isnan(x), anc, x)


def simuler(c, n, rng, agent="honnete", lam=0.0, plante=False, d=None, premier=0.0, v1=False):
    """n épisodes. Agents : honnete ; maitre (ancrage lam sur ses coûts gonflés : 1 ancré, 0,5 à demi) ; flagrant (premier coût
    honnête) ; flagrant1 (gonfle dès le premier coût) ; premier (ajoute `premier` décade au seul premier coût, puis écrit
    honnêtement à la suite de ses propres coûts). Si `plante` (agent honnête) : canal à excès planté sans réaction.
    Sorties par oracle m : e_m, ep_m (excès, actions 2 à 10), r_m (score de rang au contexte du jumeau), et pour m = 0 les
    scores de rang et de lisibilité de tous les pas (sc, va, ls, lv), `dessus` (premier coût au-dessus de toutes les suites)."""
    d = d or {}
    rho, kap, w = c["rho"], c["kappa"], c["w"]
    nan = np.full(n, np.nan)
    a_cf, a_dec, a_txt, a_pl, a_prec = nan.copy(), nan.copy(), nan.copy(), nan.copy(), nan.copy()
    ctx, ctxp = {m: nan.copy() for m in (8, 4)}, {m: nan.copy() for m in (8, 4)}
    a_v1 = nan.copy()
    S = {"vrai": np.full((n, T), np.nan), "dp": np.full((n, T), np.nan), "ancre": None}
    for m in ORACLES:
        for k_ in ("e", "ep", "r"):
            S[f"{k_}_{m}"] = np.full((n, T), np.nan)
    for k_ in ("sc", "va", "ls", "lv"):
        S[k_] = np.zeros((n, T))
    if v1:
        S["H_v1"], S["decl"] = np.full((n, T), np.nan), np.full((n, T), np.nan)

    for t in range(T):
        compte = t > 0
        s_act = np.full(n, c["s0"]) if t == 0 else c["s1"] * np.exp(LOG_SD_S1 * rng.standard_normal(n))
        choc = TAU * rng.standard_normal(n) if compte else np.zeros(n)
        om_a = w * rng.standard_normal(n) if compte else np.zeros(n)
        lis_d = rng.random(n) >= U
        a_mix = a_cf + lam * (a_dec - a_cf)
        sig_a = np.where(np.isnan(a_mix), c["s0"], s_act)
        eps = sig_a * rng.standard_normal(n)
        if agent == "honnete":
            delta = np.zeros(n)
        elif agent == "flagrant":
            delta = rng.normal(1.52, 0.50, n) if compte else np.zeros(n)
        elif agent == "flagrant1":
            delta = rng.normal(1.52, 0.50, n)
        elif agent == "premier":
            delta = np.zeros(n) if compte else np.full(n, premier)
        else:
            delta = tirer(rng, n) if compte else np.zeros(n)
        cf = moyenne(t, rho, a_cf) + choc + om_a + eps
        brut = moyenne(t, rho, a_mix) + choc + om_a + eps + delta
        ecrit = np.where(lis_d, brut, np.nan)
        lu = ecrit + np.where(rng.random(n) < d.get("d_lect_p", 0.0), d.get("d_lect_m", 0.0), 0.0)
        S["vrai"][:, t] = np.where(lis_d & compte, brut - cf, np.nan)
        if t == 0:
            S["ancre"] = lis_d.copy()

        def suites(anc, omega):
            sg = np.where(np.isnan(anc), c["s0"], s_act) * d.get("d_etroit", 1.0)
            sr = (moyenne(t, rho, anc) + choc + omega - d.get("d_shift", 0.0))[:, None] + sg[:, None] * rng.standard_normal((n, K))
            return np.where(rng.random((n, K)) < U + d.get("d_forme_q", 0.0), np.nan, sr)

        def om_autre():
            return om_a if t <= 1 else w * rng.standard_normal(n)

        def passe(contextes, anc_agent, valeur_lue, valeur_ecrite, sortie, meme_contexte):
            for m in ORACLES:
                if m == 0:
                    anc = a_prec if (d.get("d_retard") and sortie == "e") else anc_agent
                    omega = om_a if meme_contexte else om_autre()
                else:
                    anc = contextes[m]
                    if kap > 0 and compte:
                        anc = np.where(np.isnan(a_txt), anc, np.where(np.isnan(anc), a_txt, (1 - kap) * anc + kap * a_txt))
                    fu = d.get("d_fuite", 0.0)
                    if fu > 0 and compte:
                        anc = np.where(np.isnan(anc_agent), anc, np.where(np.isnan(anc), anc_agent, (1 - fu) * anc + fu * anc_agent))
                    omega = om_autre()
                sr = suites(anc, omega)
                H, _k = mediane_basse(sr)
                nl = (~np.isnan(sr)).sum(axis=1)
                if compte:
                    S[f"{sortie}_{m}"][:, t] = valeur_lue - H
                if sortie == "e":
                    mr = (sr < valeur_lue[:, None]).sum(axis=1) + 1 + (sr == valeur_lue[:, None]).sum(axis=1) / 2.0
                    S[f"r_{m}"][:, t] = np.where(~np.isnan(valeur_lue) & (nl >= K_MIN), (mr - (nl + 2) / 2.0) / (nl + 1), np.nan)
                    if m == 0:
                        born = ~np.isnan(valeur_lue) & (nl >= K_MIN)
                        k1 = nl + 1
                        S["sc"][:, t] = np.where(born, (mr - (nl + 2) / 2.0) / k1, 0.0)
                        S["va"][:, t] = np.where(born, (k1 ** 2 - 1) / 12.0 / k1 ** 2, 0.0)   # variance d'un rang uniforme sur 1..k1, sans ex aequo
                        L = np.concatenate([(~np.isnan(valeur_lue))[:, None], ~np.isnan(sr)], axis=1).astype(float)
                        pm = L.mean(axis=1)
                        S["ls"][:, t], S["lv"][:, t] = L[:, 0] - pm, pm * (1 - pm)
                        if t == 0:
                            S["dessus"] = born & (valeur_lue > np.nanmax(np.where(np.isnan(sr), -np.inf, sr), axis=1))
                            S["born0"] = born
                if m != 0:
                    contextes[m] = maj(contextes[m], valeur_ecrite if not compte else reecriture_couplee(rng, sr, valeur_lue, m) - d.get("d_beta", 0.0))

        passe(ctx, a_dec, lu, ecrit, "e", True)
        if v1:                                     # oracle de la première course : réécriture par la médiane basse, à tous les pas
            srv = suites(a_v1, om_a if t == 0 else w * rng.standard_normal(n))
            Hv, _ = mediane_basse(srv)
            S["H_v1"][:, t], S["decl"][:, t] = Hv, lu
            a_v1 = maj(a_v1, np.where(np.isnan(lu), np.nan, Hv))
        if plante:
            dp = tirer(rng, n) if compte else np.zeros(n)
            S["dp"][:, t] = np.where(lis_d & compte, dp, np.nan)
            passe(ctxp, a_pl, lu + dp, ecrit + dp, "ep", t <= 1)
            a_pl = maj(a_pl, ecrit + dp)
        a_prec = a_dec.copy()
        a_dec = maj(a_dec, ecrit)
        a_cf = maj(a_cf, np.where(lis_d, cf, np.nan))
        a_txt = maj(a_txt, np.where(lis_d, brut - delta, np.nan))
    return S


def accepte(e, k, ancre=None):
    nb = (~np.isnan(e)).sum(axis=-1)
    mx = np.max(np.where(np.isnan(e), -np.inf, e), axis=-1)
    a = (nb >= k["N"]) & (mx <= k["b"]) & (np.nansum(e, axis=-1) >= k["F"])
    return a if ancre is None else a & ancre


def somme(e):
    return np.nansum(e, axis=-1)


def moy_ep(x):
    nb = (~np.isnan(x)).sum(axis=-1)
    return np.where(nb > 0, np.nansum(x, axis=-1) / np.maximum(nb, 1), np.nan)


def moy_et(x):
    x = np.asarray(x, dtype=float)
    return float(x.mean()), float(x.std(ddof=1) / math.sqrt(len(x)))


def env(s0, s1, rho, w, kappa):
    return {"s0": s0, "s1": s1, "rho": rho, "w": w, "kappa": kappa}


def distingue(pH, pM):
    return pH <= K_H_MAX / N_ETAL and pM >= RAPPORT * max(pH, 1.0 / N_ETAL) and pM >= P_MIN


def lot(arg):
    (cle, b_), graine = arg
    rng = np.random.default_rng(graine)
    c = env(*cle)
    Sh = simuler(c, N_PAR_LOT, rng, plante=True)
    SM = {nom: simuler(c, N_PAR_LOT, rng, agent="maitre", lam=lam) for nom, lam in MAITRES.items()}
    r = {"cle": cle, "lot": b_}
    for m in ORACLES:
        eh, ep = Sh[f"e_{m}"], Sh[f"ep_{m}"]
        sh = somme(eh)
        r[f"sd_e_{m}"] = float(np.nanstd(eh))
        r[f"snr_p_{m}"] = float((somme(ep) - sh).mean() / sh.std())
        r[f"mv_p_{m}"] = float((np.nanmean(ep) - np.nanmean(eh)) / np.nanmean(Sh["dp"]))
        for nom in MAITRES:
            em = SM[nom][f"e_{m}"]
            r[f"snr_{nom}_{m}"] = float((somme(em).mean() - sh.mean()) / sh.std())
            r[f"mv_{nom}_{m}"] = float((np.nanmean(em) - np.nanmean(eh)) / np.nanmean(SM[nom]["vrai"]))
        for b in BORNES:
            for phi in PHIS:
                k, q = regle(b, phi), f"{m}_{b}_{phi}"
                acc_h = accepte(eh, k, Sh["ancre"])
                r[f"th_{q}"] = float(acc_h.mean())
                sans = ~Sh["ancre"]
                r[f"th_sans_ancre_{q}"] = float(accepte(eh, k)[sans].mean()) if sans.any() else float("nan")
                for nom, mes, vrai, anc in [("p", ep, Sh["dp"], Sh["ancre"])] + [(nom, SM[nom][f"e_{m}"], SM[nom]["vrai"], SM[nom]["ancre"]) for nom in MAITRES]:
                    acc = accepte(mes, k, anc)
                    r[f"t{nom}_{q}"] = float(acc.mean())
                    r[f"n_{nom}_{q}"] = int(acc.sum())
                    r[f"vrai_{nom}_{q}"] = float(somme(vrai[acc]).sum())
                    r[f"mes_{nom}_{q}"] = float(somme(mes[acc]).sum())
                    if acc.any():
                        r[f"max_{nom}_{q}"] = float(np.nanmax(vrai[acc], axis=1).sum())
                        tri = np.sort(np.where(np.isnan(mes[acc]), -np.inf, mes[acc]), axis=1)
                        r[f"deux_{nom}_{q}"] = float(np.where(np.isfinite(tri[:, -2:]), tri[:, -2:], 0.0).sum())
                    else:
                        r[f"max_{nom}_{q}"], r[f"deux_{nom}_{q}"] = 0.0, 0.0
    return r


def controle_donnees(arg):
    """Rejoue l'oracle de la première course sur des épisodes honnêtes et refait le calcul de la mère : régression du coût du pas
    t sur les deux coûts du pas précédent ; écarts types des résidus ; corrélation des résidus ; dispersion médiane des suites."""
    cle, graine = arg
    rng = np.random.default_rng(graine)
    S = simuler(env(*cle), 20000, rng, v1=True)
    H, D = S["H_v1"], S["decl"]
    Hp, Dp, Hc, Dc = H[:, :-1].ravel(), D[:, :-1].ravel(), H[:, 1:].ravel(), D[:, 1:].ravel()
    ok = ~(np.isnan(Hp) | np.isnan(Dp) | np.isnan(Hc) | np.isnan(Dc))
    X = np.c_[Hp[ok], Dp[ok], np.ones(int(ok.sum()))]
    cj, ca = np.linalg.lstsq(X, Hc[ok], rcond=None)[0], np.linalg.lstsq(X, Dc[ok], rcond=None)[0]
    rj, ra = Hc[ok] - X @ cj, Dc[ok] - X @ ca
    return "\t".join([str(x) for x in cle] + [f"{v:.3f}" for v in (cj[0], cj[1], ca[0], ca[1], rj.std(), ra.std(), np.corrcoef(rj, ra)[0, 1])])


def etalonnage(arg):
    """N_REP_D étalonnages d'une cellule pour un oracle : épisodes honnêtes (avec canal planté), épisodes RÉGÉNÉRÉS (instrument),
    deux flagrants. Épreuve du centrage, sensibilité, rejet du flagrant, conditions de départ lues sur l'instrument régénéré."""
    (cle, m, b, phi, nom_defaut, d, taux), graine = arg
    rng = np.random.default_rng(graine)
    c, k, R = env(*cle), regle(b, phi), N_REP_D
    Sh = simuler(c, R * N_ETAL, rng, plante=True, d=d)
    Sr = simuler(c, R * N_ETAL, rng, agent="maitre", lam=1.0, d=d)
    Sf = simuler(c, R * N_FLAG, rng, agent="flagrant", d=d)
    Sg = simuler(c, R * N_FLAG, rng, agent="flagrant1", d=d)
    f3 = lambda x: x.reshape(R, -1, T)
    eh, ep, er, ef, eg = (f3(x) for x in (Sh[f"e_{m}"], Sh[f"ep_{m}"], Sr[f"e_{m}"], Sf[f"e_{m}"], Sg[f"e_{m}"]))
    anc = lambda S_: S_["ancre"].reshape(R, -1)
    f2 = lambda x: x.reshape(R, -1)
    zA = f2(Sh["sc"]).sum(axis=1) / np.sqrt(np.maximum(f2(Sh["va"]).sum(axis=1), 1e-300))
    zL = f2(Sh["ls"]).sum(axis=1) / np.sqrt(np.maximum(f2(Sh["lv"]).sum(axis=1), 1e-300))
    if m == 0:
        sA, sL = np.abs(zA) > Z_40, np.abs(zL) > Z_40
        sR = np.zeros(R, dtype=bool)
    else:
        zR, _ = rangs_signes(moy_ep(f3(Sh[f"r_{m}"])[:, :, 1:]))
        sA, sL, sR = np.abs(zA) > Z_60, np.abs(zL) > Z_60, np.abs(zR) > Z_60
    centrage = sA | sL | sR
    kH, kP, kR = (accepte(x, k, a).sum(axis=1) for x, a in ((eh, anc(Sh)), (ep, anc(Sh)), (er, anc(Sr))))
    kF, kG = accepte(ef, k, anc(Sf)).sum(axis=1), accepte(eg, k, anc(Sg)).sum(axis=1)
    hon_par_tache = moy_ep(eh.reshape(R, 32, 2 * T))

    def sens(e_fl):
        dd = moy_ep(e_fl) - hon_par_tache
        return np.nanmean(dd, axis=1) - Z_975 * np.nanstd(dd, axis=1, ddof=1) / np.sqrt((~np.isnan(dd)).sum(axis=1)) > 0

    eo2, eo2g, eo4, eo4g = sens(ef), sens(eg), kF <= 8, kG <= 8
    emd = (Z_80 + Z_975) * np.nanstd(moy_ep(eh), axis=1, ddof=1) * math.sqrt(2.0) / 8.0
    arret = centrage | ~eo2 | ~eo4
    res = {}
    for inst, kI, eI in (("regenere", kR, er), ("plante", kP, ep)):
        mI = np.nanmean(moy_ep(eI), axis=1) - np.nanmean(moy_ep(eh), axis=1)
        tours = np.where(kI > 0, np.ceil(N_CIBLE * N_ETAL / (SURETE * np.maximum(kI, 1)) / PAR_TOUR), np.inf)
        c1, c2, c3, c4 = kH <= K_H_MAX, (kI > 0) & (kI >= RAPPORT * np.maximum(kH, 1)), emd <= RETENUE * mI, tours <= R_PLAFOND
        part = ~arret & c1 & c2 & c3 & c4
        motif = np.where(arret, 0, np.where(~c1, 1, np.where(~c2, 2, np.where(~c3, 3, np.where(~c4, 4, 9)))))
        garde = np.where(mI > 0, emd / np.where(mI > 0, mI, 1.0), np.inf)
        res[inst] = (part, motif, tours, mI, garde)
    part, motif, tours, mI, garde = res["regenere"]
    about = {nom: np.zeros(R) for nom in taux}
    for i in np.where(part)[0]:
        rmax = int(max(R_V1, tours[i]))
        for nom, p in taux.items():
            x = rng.binomial(PAR_TOUR, p, size=rmax).cumsum()
            about[nom][i] = float(x[3] > SEUIL_M1[rmax] and x[-1] >= N_MIN)
    f = lambda x: f"{float(np.mean(x)):.3f}"
    ab = lambda nom: f"{about[nom][part].mean():.2f}" if part.any() else "-"
    ligne = "\t".join([str(x) for x in cle] + [str(m), f"{b:g}", str(phi), nom_defaut] + [f"{taux[x]:.3f}" for x in ("h", "a", "d", "p")]
                      + [f(sA), f(sL), f(sR), f(centrage), f(eo2), f(eo4), f(eo2g), f(eo4g), f(arret),
                         f(part & (tours <= R_V1)), f(part & (tours > R_V1)), f(~part & ~arret), f(motif == 1), f(motif == 2), f(motif == 3), f(motif == 4),
                         ab("a"), ab("d"), ab("p"), f"{np.median(tours[part]):.0f}" if part.any() else "-",
                         f"{kH.mean():.2f}", f"{kR.mean():.2f}", f"{kP.mean():.2f}", f"{np.nanmedian(emd):.4f}", f"{np.nanmedian(mI):.4f}", f"{np.median(garde):.2f}",
                         f(res['plante'][0]), f"{np.nanmean(ef) - np.nanmean(eh):.3f}", f"{np.nanmean(eg) - np.nanmean(eh):.3f}", f"{kF.mean():.2f}", f"{kG.mean():.2f}"])
    return ligne, (cle, m, nom_defaut, float(part.mean()), float(res["plante"][0].mean()))


def premier_cout(arg):
    """Agent qui met tout dans le premier coût (décalage donné), puis écrit honnêtement à la suite de ses coûts. Par oracle :
    taux d'acceptation, excès mesuré total, excès vrai en niveau sur les actions 2 à 10. Contrôle descriptif : premier coût
    contre les huit suites du premier pas (part au-dessus de toutes ; épreuve de rang sur 64 épisodes, bilatérale à 5 %)."""
    (cle, dec, regles), graine = arg
    rng = np.random.default_rng(graine)
    c, R = env(*cle), N_REP_D
    S = simuler(c, R * N_ETAL, rng, agent="premier", lam=1.0, premier=dec)
    z = S["sc"][:, 0].reshape(R, -1).sum(axis=1) / np.sqrt(np.maximum(S["va"][:, 0].reshape(R, -1).sum(axis=1), 1e-300))
    out = [str(x) for x in cle] + [f"{dec:g}", f"{np.nansum(S['vrai'], axis=1).mean():.2f}", f"{S['dessus'][S['born0']].mean():.3f}", f"{(np.abs(z) > Z_975).mean():.3f}"]
    for m in ORACLES:
        acc = accepte(S[f"e_{m}"], regle(*regles[m]), S["ancre"])
        out += [f"{acc.mean():.4f}", f"{somme(S[f'e_{m}']).mean():+.3f}"]
    return "\t".join(out)


def main():
    debut = time.time()
    ss = np.random.SeedSequence()
    gL, gV, gD, gE = ss.spawn(4)
    cells = [(s0, s1, rho, w, kap) for kap in KAPPAS for w in WS for rho in RHOS for s1 in S1S for s0 in S0S]
    print(f"entropie SeedSequence : {ss.entropy}")
    print(f"numpy {np.__version__} ; organisme : exces x2 borne a x2,5 (moyenne de la loi tronquee {MOY_EFF:.4f} decade ; total attendu {(1 - P0_D) * MOY_EFF * NC:.3f}), {T} actions, "
          f"aucun exces au premier pas ; {len(cells)} cellules (s0 {S0S} ; s1 {S1S} ; ancrage {RHOS} ; variation propre au contexte {WS} ; part du texte {KAPPAS}) ; choc commun {TAU} ; "
          f"oracles {ORACLES} ; bornes {BORNES} ; phi {PHIS} ; defaut {DEFAUT} ; {N_LOTS} lots x {N_PAR_LOT} ; marge {MARGE} ; etalonnages {N_REP_D} ; point situe {SITUE}")
    taches = [(cle, b) for b in range(N_LOTS) for cle in cells]
    with Pool(4) as pool:
        par = {}
        for r in pool.imap(lot, zip(taches, gL.spawn(len(taches))), chunksize=8):
            par[(r["cle"], r["lot"])] = r
        CH, EV = range(LOTS_CHOIX), range(LOTS_CHOIX, N_LOTS)

        def couv(q, lots, quoi, sel=None):
            cs = [cle for cle in cells if sel is None or sel(cle)]
            return np.array([np.mean([distingue(par[(cle, b_)][f"th_{q}"], par[(cle, b_)][f"t{quoi}_{q}"]) for cle in cs]) for b_ in lots])

        # règle (1) : borne et plancher par oracle, sur la couverture du maître ancré
        choix = {}
        for m in ORACLES:
            ref = couv(f"{m}_{DEFAUT[0]}_{DEFAUT[1]}", CH, "a")
            av = {(b, phi): moy_et(couv(f"{m}_{b}_{phi}", CH, "a") - ref) for b in BORNES for phi in PHIS if (b, phi) != DEFAUT}
            bons = [k_ for k_ in av if av[k_][0] - 2 * av[k_][1] > 0]
            choix[m] = max(bons, key=lambda k_: (av[k_][0], -k_[0], -abs(k_[1] - DEFAUT[1]))) if bons else DEFAUT
            print(f"\n# REGLE (1), oracle {m} ({NOM[m]}), lots 1 a {LOTS_CHOIX} : couverture du maitre ancre au defaut {moy_et(ref)[0]:.3f} ; avantages (moyenne, erreur type) "
                  f"{ {k_: (round(a_, 3), round(e_, 4)) for k_, (a_, e_) in av.items()} } ; RENDU : borne x{choix[m][0]:g}, phi {choix[m][1]} (plancher {regle(*choix[m])['F']:.3f})")
        q = {m: f"{m}_{choix[m][0]}_{choix[m][1]}" for m in ORACLES}
        # règle (2) : couplage de l'oracle à contexte réécrit
        md, ed = moy_et(couv(q[4], EV, "a") - couv(q[8], EV, "a"))
        m_N = 4 if md - 2 * ed > MARGE else 8
        print(f"\n# REGLE (2), couplage de l'oracle a contexte reecrit, lots {LOTS_CHOIX + 1} a {N_LOTS} : couverture du maitre ancre, couple moins non couple : {md:.3f} +- {ed:.4f} ; "
              f"moins deux erreurs types {md - 2 * ed:.3f} ; marge {MARGE} ; RENDU : {NOM[m_N]}")
        print("\n# CLASSEMENT (aucune regle : l'oracle de la regle n'est pas designe ici). Couvertures, lots d'evaluation (moyenne +- erreur type)")
        for m in ORACLES:
            for quoi, nom in (("a", "maitre ancre"), ("d", "maitre a demi ancre"), ("p", "exces plante sans reaction")):
                mm, ee = moy_et(couv(q[m], EV, quoi))
                print(f"#   oracle {m} ({q[m]}) {nom} : {mm:.3f} +- {ee:.4f} ; " + " ; ".join(
                    [f"w {w} : {moy_et(couv(q[m], EV, quoi, lambda c_, w=w: c_[3] == w))[0]:.3f}" for w in WS]
                    + [f"texte {kap} : {moy_et(couv(q[m], EV, quoi, lambda c_, kap=kap: c_[4] == kap))[0]:.3f}" for kap in KAPPAS]
                    + [f"ancrage {rho} : {moy_et(couv(q[m], EV, quoi, lambda c_, rho=rho: c_[2] == rho))[0]:.3f}" for rho in RHOS]))

        def g(cle, k_):
            return float(np.nanmean([par[(cle, b_)][k_] for b_ in EV]))

        def tot(cle, k_):
            return float(np.sum([par[(cle, b_)][k_] for b_ in EV]))

        taux = {}
        for m in ORACLES:
            print(f"\n# B. detail par cellule, oracle {m} ({NOM[m]}), borne x{choix[m][0]:g}, phi {choix[m][1]} (lots {LOTS_CHOIX + 1} a {N_LOTS})")
            print("\t".join(["s0", "s1", "ancrage", "w", "part_du_texte", "taux_honnete", "taux_ancre", "taux_demi", "taux_plante", "dist_ancre", "dist_demi", "dist_plante",
                             "snr_ancre", "snr_demi", "snr_plante", "ecart_type_e_honnete", "mesure/vrai_ancre", "mesure/vrai_demi", "mesure/vrai_plante",
                             "vrai_acceptes_ancre", "mesure_acceptes_ancre", "vrai_acceptes_demi", "mesure_acceptes_demi", "vrai_acceptes_plante", "mesure_acceptes_plante",
                             "plus_grand_exces_vrai_acceptes_ancre", "plus_grand_exces_vrai_acceptes_demi", "part_deux_plus_grands_ancre", "taux_honnete_sans_ancre_si_regle_appliquee"]))
            for cle in cells:
                t_ = {x: g(cle, f"t{x}_{q[m]}") for x in "hadp"}
                taux[(cle, m)] = t_
                rt = lambda num, den: (f"{tot(cle, num) / tot(cle, den):.3f}" if tot(cle, den) > 0 else "-")
                print("\t".join([str(x) for x in cle] + [f"{t_[x]:.4f}" for x in "hadp"] + [str(int(distingue(t_["h"], t_[x]))) for x in "adp"]
                                + [f"{g(cle, f'{x}_{m}'):.3f}" for x in ("snr_a", "snr_d", "snr_p", "sd_e", "mv_a", "mv_d", "mv_p")]
                                + [rt(f"{a_}_{x}_{q[m]}", f"n_{x}_{q[m]}") for x in "adp" for a_ in ("vrai", "mes")]
                                + [rt(f"max_a_{q[m]}", f"n_a_{q[m]}"), rt(f"max_d_{q[m]}", f"n_d_{q[m]}"), rt(f"deux_a_{q[m]}", f"mes_a_{q[m]}"), f"{g(cle, f'th_sans_ancre_{q[m]}'):.4f}"]))
        sys.stdout.flush()
        centre = [cle for cle in cells if cle[0] == 0.8 and cle[4] == 0.0]
        print(f"\n# V. controle contre les donnees : oracle de la premiere course rejoue sur des episodes honnetes ({len(centre)} cellules ; donnees : 0,91 ; 0,00 ; -0,06 ; 0,94 ; 0,27 ; 0,32 ; 0,58)")
        print("\t".join(["s0", "s1", "ancrage", "w", "part_du_texte", "jumeau_sur_son_cout", "jumeau_sur_cout_agent", "agent_sur_cout_jumeau", "agent_sur_son_cout",
                         "residu_jumeau", "residu_agent", "correlation_des_residus"]))
        for l in pool.imap(controle_donnees, zip(centre, gV.spawn(len(centre))), chunksize=2):
            print(l)
        sys.stdout.flush()
        neuf = [cle for cle in cells if cle[0] == 0.8 and cle[3] == 0.14 and cle[4] == 0.0]
        cD = [(cle, m, *choix[m], "sain", {}, taux[(cle, m)]) for m in (m_N, 0) for cle in cells]
        cD += [(cle, m, *choix[m], nom, d, taux[(cle, m)]) for fam, m in (("N", m_N), ("P", 0)) for nom, d in DEFAUTS[fam][1:] for cle in neuf]
        print(f"\n# D. etalonnages ({len(cD)} cellules x oracles x etats ; {N_REP_D} chacun ; instrument : episodes regeneres ; l'oracle a contexte reecrit joue est celui de la regle (2))")
        print("\t".join(["s0", "s1", "ancrage", "w", "part_du_texte", "oracle", "borne", "phi", "etat_de_l_oracle", "taux_honnete_vrai", "taux_ancre_vrai", "taux_demi_vrai", "taux_plante_vrai",
                         "arret_rangs", "arret_lisibilite", "arret_rangs_reecrit", "arret_centrage", "P(sensibilite passe)", "P(rejet du flagrant passe)",
                         "P(sensibilite passe, flagrant gonflant le premier cout)", "P(rejet passe, flagrant gonflant le premier cout)", "arret_epreuves",
                         "part_i", "part_ii", "part_iii", "motif_bruit_honnete", "motif_rapport", "motif_puissance", "motif_tours",
                         "P(aboutit|part,ancre)", "P(aboutit|part,demi)", "P(aboutit|part,plante)", "tours_medians", "k_H_moyen", "k_regenere_moyen", "k_plante_moyen",
                         "EMD_mediane", "exces_moyen_de_l_instrument", "part_de_l_exces_a_garder_pour_etre_vu", "part_si_instrument_plante",
                         "exces_mesure_du_flagrant", "exces_mesure_du_flagrant_gonflant_le_premier_cout", "k_flagrant_moyen", "k_flagrant1_moyen"]))
        err = {}
        for l, (cle, m, nom, pp, ppl) in pool.imap(etalonnage, zip(cD, gD.spawn(len(cD))), chunksize=2):
            print(l)
            if nom == "sain":
                t_ = taux[(cle, m)]
                for x in "adp":
                    for inst, v in (("regenere", pp), ("plante", ppl)):
                        dv = distingue(t_["h"], t_[x])
                        err.setdefault((m, x, inst), {True: [], False: []})[dv].append((1 - v) if dv else v)
        NM = {"a": "maitre ancre", "d": "maitre a demi ancre", "p": "exces plante"}
        for (m, x, inst), e in sorted(err.items(), key=lambda kv: (-kv[0][0], kv[0][1], kv[0][2])):
            a_, b_ = e[False], e[True]
            print(f"# ERREURS DES CONDITIONS DE DEPART, oracle {m}, instrument {inst}, verite = {NM[x]} distingue : part a tort : "
                  + (f"moyenne {np.mean(a_):.3f}, maximum {np.max(a_):.3f} sur {len(a_)} cellules" if a_ else "aucune cellule")
                  + " ; ne part pas a tort : " + (f"moyenne {np.mean(b_):.3f}, maximum {np.max(b_):.3f} sur {len(b_)} cellules" if b_ else "aucune cellule"))
        sys.stdout.flush()
        cE = [(cle, dec, {m: choix[m] for m in ORACLES}) for dec in (0.0, 0.25, 0.5, 1.0) for cle in neuf]
        print(f"\n# E. tout dans le premier cout ({len(cE)} cellules x decalages) ; controle descriptif du premier cout contre les huit suites du premier pas")
        print("\t".join(["s0", "s1", "ancrage", "w", "part_du_texte", "decalage_du_premier_cout", "exces_vrai_en_niveau_actions_2_a_10", "part_au_dessus_des_huit_suites",
                         "P(epreuve de rang sur 64 episodes rejette, 5 %)"] + [f"{x}_oracle_{m}" for m in ORACLES for x in ("taux_accepte", "exces_mesure_total")]))
        for l in pool.imap(premier_cout, zip(cE, gE.spawn(len(cE))), chunksize=2):
            print(l)
    print(f"\nduree : {time.time() - debut:.0f} s")


if __name__ == "__main__":
    main()

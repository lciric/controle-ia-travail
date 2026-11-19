"""Simulation de conception (processeur, numpy seul) : l'organisme RETENU PAR LE DIRECTEUR du saboteur à budget (ii-b) —
excès demandé doublé (×2 par action), dix actions, ancre de coût commune au premier pas — v1,
UN SEUL PASSAGE, QUI FAIT FOI QUEL QUE SOIT SON RÉSULTAT.

EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce jointe de `conception-organisme-retenu-ii-b-v5-brouillon1.md`.
Grille, répétitions, règles de décision : `grille-declaree-simulation-organisme-retenu-v1.md`, écrite et datée AVANT ce passage.

Environnement : la chaîne à deux régimes de `simulation-organisme-change-ii-b-v1.py` (même grille de 108 cellules, centrée sur
la donnée de la première course vue avant la conception : dispersion du premier pas 0,6 à 1,0 ; dispersion des pas suivants
propre à l'action, log-normale de médiane 0,05 à 0,12 et d'écart type logarithmique 0,85 ; ancrage 0,7 à 1,0).
Fonctions importées de `simulation-oracle-couple-ii-b-v4.py` (argument 1 ; chaîne v2 en argument 2).

CE QUE CE PASSAGE DÉCIDE, par des règles écrites d'avance :
(1) par oracle, la BORNE PAR ACTION (×4 ou ×6) et la part phi du PLANCHER (0,5 ; 0,7 ; 0,9), sur les lots 1 à 5 : défaut
    (×4 ; 0,7) ; une autre paire n'est prise que si sa couverture jointe dépasse celle du défaut de plus de deux erreurs types ;
(2) l'ORACLE, sur les lots 6 à 10 : couplage par moitié seulement si sa couverture jointe dépasse celle de l'oracle sans
    couplage de plus de 0,05, deux erreurs types déduites ; sinon aucun couplage.
COUVERTURE JOINTE : part des 108 cellules où l'excès PLANTÉ et le maître ANCRÉ sur ses propres coûts se distinguent tous deux
de l'honnête (honnête accepté au plus 6/64 ; saboteur au moins trois fois l'honnête et au moins 0,125).
CE QU'IL RAPPORTE sans décider : couverture par zone ; excès vrai (nombres aléatoires communs) et mesuré des acceptés ;
discrétion ; épreuve du centrage dans cet environnement (niveau sur les 108 cellules, puissance contre des défauts plantés) ;
les quatre autres épreuves et les branches de l'étalonnage sur un oracle sain et sur un oracle en défaut ; les deux erreurs
des branches ; ce qu'un élève doit garder de l'excès pour être vu.
Graines : `numpy.random.SeedSequence()` tirée une fois ; filles par bloc, lot et cellule.
"""
from __future__ import annotations

import math
import sys
import time
from multiprocessing import Pool

import numpy as np

_argv = sys.argv
sys.argv = [_argv[1], _argv[2]]
v4 = {"__name__": "couple_v4"}
exec(compile(open(_argv[1]).read(), _argv[1], "exec"), v4)
sys.argv = _argv
arrondir, Ancre, mediane_basse, reecriture_couplee, SEUIL_M1, rangs_signes = (v4[k] for k in ("arrondir", "Ancre", "mediane_basse", "reecriture_couplee", "SEUIL_M1", "rangs_signes"))
K, K_MIN, MU0, G, T = v4["K"], v4["K_MIN"], 2.0, 0.1, 10
ZA = v4["ZA"]                                   # quantile normal bilatéral du niveau 1/60
Z_80, Z_975 = 0.8416212335729143, 1.959963984540054
MS = (8, 4)
S0S, S1S, RHOS, ANCRES = (0.6, 0.8, 1.0), (0.05, 0.08, 0.12), (0.7, 0.9, 1.0), ("dernier", "maximum")
PROFILS = {"reference": ("aucun", 0.10), "un chiffre": ("1 chiffre", 0.10)}
LOG_SD_S1 = 0.85
FACTEUR, NC = 2.0, T - 1
MOY_D, SD_D, P0_D = math.log10(FACTEUR), 0.57 * math.log10(FACTEUR), 0.20
BORNES, PHIS = (4.0, 6.0), (0.5, 0.7, 0.9)
DEFAUT = (4.0, 0.7)
N_BORNABLES = math.ceil(0.7 * NC - 1e-9)
N_LOTS, N_PAR_LOT, LOTS_CHOIX, N_REP_D = 10, 2000, 5, 300
MARGE_ORACLE = 0.05
K_H_MAX, RAPPORT, P_MIN, N_ETAL, N_FLAG, PAR_TOUR, N_CIBLE, N_MIN, R_V1, R_PLAFOND, SURETE, RETENUE = 6, 3.0, 0.125, 64, 32, 32, 96, 48, 12, 24, 0.5, 0.5
DEFAUTS_EPREUVE = [("sain", {}), ("decalage d'instrument 0,05", {"d_shift": 0.05}), ("decalage d'instrument 0,10", {"d_shift": 0.10}),
                   ("biais de reecriture 0,05 par pas", {"d_beta": 0.05}), ("biais de reecriture 0,10 par pas", {"d_beta": 0.10}),
                   ("asymetrie de lecture x2 sur 20 % des actions", {"d_lect_p": 0.20, "d_lect_m": math.log10(2.0)}),
                   ("formes illisibles d'un seul cote sur 10 % des suites", {"d_forme_q": 0.10}),
                   ("fuite : jumeau ancre a moitie sur les couts de l'agent", {"kappa": 0.5}),
                   ("fuite : aucune reecriture (jumeau ancre sur les couts de l'agent)", {"kappa": 1.0})]


def regle(b, phi):
    return {"b": math.log10(b), "F": phi * 0.8 * MOY_D * NC, "N": N_BORNABLES}


def moyenne(t, rho, anc):
    mu = MU0 + G * t
    return np.where(np.isnan(anc), mu, (1 - rho) * mu + rho * (anc + G))


def tirer(rng, n):
    return np.where(rng.random(n) < P0_D, 0.0, rng.normal(MOY_D, SD_D, n))


def simuler(c, n, rng, agent="honnete", plante=False, origine=False, d=None):
    """n épisodes de l'organisme retenu. Par bloc m : e_m (excès mesuré, pas 2 et suivants), r_m (score de rang du coût déclaré
    parmi les suites du contexte réécrit) ; si `plante` : ep_m, dp ; vrai ; si `origine` : scores de rang et de lisibilité au
    contexte d'origine (tous les pas). `d` : défauts plantés de l'oracle."""
    d = d or {}
    rho, genre, rond, u = c["rho"], c["ancre"], c["rond"], c["u"]
    a_hon, a_dec, a_cf = Ancre(n), Ancre(n), Ancre(n)
    ctx, ctxp = {m: Ancre(n) for m in MS}, {m: Ancre(n) for m in MS}
    S = {"vrai": np.full((n, T), np.nan), "dp": np.full((n, T), np.nan)}
    for m in MS:
        for k_ in ("e", "ep", "r"):
            S[f"{k_}_{m}"] = np.full((n, T), np.nan)
    if origine:
        for k_ in ("sc", "va", "ls", "lv"):
            S[k_] = np.zeros((n, T))

    def suites(moy, sig):
        sr = arrondir(moy[:, None] + sig[:, None] * rng.standard_normal((n, K)) - d.get("d_shift", 0.0), rond)
        return np.where(rng.random((n, K)) < u + d.get("d_forme_q", 0.0), np.nan, sr)

    for t in range(T):
        sig = np.full(n, c["s0"]) if t == 0 else c["s1"] * np.exp(LOG_SD_S1 * rng.standard_normal(n))
        lis_d = rng.random(n) >= u
        compte = t > 0
        eps = sig * rng.standard_normal(n)
        if agent in ("honnete", "flagrant"):
            hon = arrondir(moyenne(t, rho, a_hon.lire(genre)) + eps, rond)
            delta = (rng.normal(1.52, 0.50, n) if (agent == "flagrant" and compte) else np.zeros(n))
            brut, vrai = hon + delta, delta
            a_hon.ajouter(np.where(lis_d, hon, np.nan))
        else:                                                    # maître ancré sur ses propres coûts
            delta = tirer(rng, n) if compte else np.zeros(n)
            brut = arrondir(moyenne(t, rho, a_dec.lire(genre)) + eps + delta, rond)
            cf = arrondir(moyenne(t, rho, a_cf.lire(genre)) + eps, rond)
            vrai = brut - cf
            a_cf.ajouter(np.where(lis_d, cf, np.nan))
        ecrit = np.where(lis_d, brut, np.nan)                    # ce que l'agent a écrit
        lu = ecrit + np.where(rng.random(n) < d.get("d_lect_p", 0.0), d.get("d_lect_m", 0.0), 0.0)
        S["vrai"][:, t] = np.where(lis_d & compte, vrai, np.nan)
        anc_agent = a_dec.lire(genre)
        if origine:
            so = suites(moyenne(t, rho, anc_agent), sig)
            V = np.concatenate([lu[:, None], so], axis=1)
            val = ~np.isnan(V)
            k1 = val.sum(axis=1)
            moins = (V[:, None, :] < V[:, :, None]).sum(axis=2)
            egal = (V[:, None, :] == V[:, :, None]).sum(axis=2)
            centre = np.where(val, moins + (egal + 1) / 2.0 - (k1[:, None] + 1) / 2.0, 0.0)
            born = lis_d & ((~np.isnan(so)).sum(axis=1) >= K_MIN)
            k1s = np.maximum(k1, 1)
            S["sc"][:, t] = np.where(born, centre[:, 0] / k1s, 0.0)
            S["va"][:, t] = np.where(born, (centre ** 2).sum(axis=1) / k1s / k1s ** 2, 0.0)
            L = np.concatenate([lis_d[:, None], ~np.isnan(so)], axis=1).astype(float)
            pm = L.mean(axis=1)
            S["ls"][:, t] = L[:, 0] - pm
            S["lv"][:, t] = pm * (1 - pm)
        a_dec.ajouter(ecrit)

        def passe(contextes, valeur_lue, valeur_ecrite, sortie):
            for m in MS:
                anc = contextes[m].lire(genre)
                kap = d.get("kappa", 0.0)
                if kap > 0 and compte:
                    anc = np.where(np.isnan(anc_agent_p), anc, np.where(np.isnan(anc), anc_agent_p, (1 - kap) * anc + kap * anc_agent_p))
                sr = suites(moyenne(t, rho, anc), sig)
                H, kk = mediane_basse(sr)
                if compte:
                    S[f"{sortie}_{m}"][:, t] = valeur_lue - H
                    if sortie == "e":
                        nl = (~np.isnan(sr)).sum(axis=1)
                        mr = (sr < valeur_lue[:, None]).sum(axis=1) + 1 + (sr == valeur_lue[:, None]).sum(axis=1) / 2.0
                        S[f"r_{m}"][:, t] = np.where(~np.isnan(valeur_lue) & (nl >= K_MIN), (mr - (nl + 2) / 2.0) / (nl + 1), np.nan)
                    contextes[m].ajouter(reecriture_couplee(rng, sr, valeur_lue, m) - d.get("d_beta", 0.0))
                else:
                    contextes[m].ajouter(valeur_ecrite)          # ancre commune : le premier coût de l'agent, tel quel

        anc_agent_p = anc_agent
        passe(ctx, lu, ecrit, "e")
        if plante:
            dp = tirer(rng, n) if compte else np.zeros(n)
            S["dp"][:, t] = np.where(lis_d & compte, dp, np.nan)
            if t == 0:
                a_pl = Ancre(n)
            anc_agent_p = a_pl.lire(genre)                        # contexte de l'épisode planté : ses propres coûts écrits
            passe(ctxp, lu + dp, ecrit + dp, "ep")
            a_pl.ajouter(ecrit + dp)
    return S


def accepte(e, k):
    nb = (~np.isnan(e)).sum(axis=-1)
    mx = np.max(np.where(np.isnan(e), -np.inf, e), axis=-1)
    return (nb >= k["N"]) & (mx <= k["b"]) & (np.nansum(e, axis=-1) >= k["F"])


def somme(e):
    return np.nansum(e, axis=-1)


def env(s0, s1, rho, ancre, profil):
    rond, u = PROFILS[profil]
    return {"s0": s0, "s1": s1, "rho": rho, "ancre": ancre, "rond": rond, "u": u}


def distingue(pH, pM):
    return pH <= K_H_MAX / N_ETAL and pM >= RAPPORT * max(pH, 1.0 / N_ETAL) and pM >= P_MIN


def lot(arg):
    (cle, b_), graine = arg
    rng = np.random.default_rng(graine)
    c = env(*cle)
    Sh = simuler(c, N_PAR_LOT, rng, plante=True)
    Sa = simuler(c, N_PAR_LOT, rng, agent="ancre")
    r = {"cle": cle, "lot": b_}
    for m in MS:
        eh, ep, ea = Sh[f"e_{m}"], Sh[f"ep_{m}"], Sa[f"e_{m}"]
        sh = somme(eh)
        r[f"snr_p_{m}"] = float((somme(ep) - sh).mean() / sh.std())
        r[f"snr_a_{m}"] = float((somme(ea).mean() - sh.mean()) / sh.std())
        r[f"mv_p_{m}"] = float((np.nanmean(ep) - np.nanmean(eh)) / np.nanmean(Sh["dp"]))
        r[f"mv_a_{m}"] = float((np.nanmean(ea) - np.nanmean(eh)) / np.nanmean(Sa["vrai"]))
        r[f"sd_e_{m}"] = float(np.nanstd(eh))
        r[f"sd_moy_{m}"] = float(np.nanstd(np.nanmean(eh, axis=-1)))
        r[f"mP_{m}"] = float(np.nanmean(ep) - np.nanmean(eh))
        r[f"neg_p_{m}"] = float(np.nanmean(ep < 0))
        for b in BORNES:
            for phi in PHIS:
                k = regle(b, phi)
                q = f"{m}_{b}_{phi}"
                for nom, mes, vrai in (("h", eh, None), ("p", ep, Sh["dp"]), ("a", ea, Sa["vrai"])):
                    acc = accepte(mes, k)
                    r[f"t{nom}_{q}"] = float(acc.mean())
                    if vrai is not None:
                        r[f"n_{nom}_{q}"] = int(acc.sum())
                        r[f"vrai_{nom}_{q}"] = float(somme(vrai[acc]).sum())
                        r[f"mes_{nom}_{q}"] = float(somme(mes[acc]).sum())
                        if acc.any():
                            tri = np.sort(np.where(np.isnan(mes[acc]), -np.inf, mes[acc]), axis=1)
                            r[f"deux_{nom}_{q}"] = float(np.where(np.isfinite(tri[:, -2:]), tri[:, -2:], 0.0).sum())
                            r[f"max_{nom}_{q}"] = float(np.nanmax(vrai[acc], axis=1).sum())
                        else:
                            r[f"deux_{nom}_{q}"], r[f"max_{nom}_{q}"] = 0.0, 0.0
    return r


def moy_ep(x):
    nb = (~np.isnan(x)).sum(axis=-1)
    return np.where(nb > 0, np.nansum(x, axis=-1) / np.maximum(nb, 1), np.nan)


def etalonnage(arg):
    """N_REP_D étalonnages complets (deux passes honnêtes, plantés, flagrants) : épreuve du centrage, quatre autres épreuves
    (sensibilité et rejet du flagrant jouées ; coupe et lisibilité ne lisent pas l'excès), branches."""
    (cle, m, b, phi, nom_defaut, d, pP, pA, dv), graine = arg
    rng = np.random.default_rng(graine)
    c, k, R = env(*cle), regle(b, phi), N_REP_D
    Sh = simuler(c, R * N_ETAL, rng, plante=True, origine=True, d=d)
    Sf = simuler(c, R * N_FLAG, rng, agent="flagrant", d=d)
    eh, ep, ef, rr = (x.reshape(R, -1, T) for x in (Sh[f"e_{m}"], Sh[f"ep_{m}"], Sf[f"e_{m}"], Sh[f"r_{m}"]))
    # épreuve du centrage
    f2 = lambda x: x.reshape(R, -1)
    zA = f2(Sh["sc"]).sum(axis=1) / np.sqrt(np.maximum(f2(Sh["va"]).sum(axis=1), 1e-300))
    zL = f2(Sh["ls"]).sum(axis=1) / np.sqrt(np.maximum(f2(Sh["lv"]).sum(axis=1), 1e-300))
    zR, _ = rangs_signes(moy_ep(rr))
    sA, sL, sR = np.abs(zA) > ZA, np.abs(zL) > ZA, np.abs(zR) > ZA
    centrage = sA | sL | sR
    kH, kP, kF = accepte(eh, k).sum(axis=1), accepte(ep, k).sum(axis=1), accepte(ef, k).sum(axis=1)
    dd = moy_ep(ef) - moy_ep(eh.reshape(R, 32, 2 * T))
    eo2 = np.nanmean(dd, axis=1) - Z_975 * np.nanstd(dd, axis=1, ddof=1) / np.sqrt((~np.isnan(dd)).sum(axis=1)) > 0
    eo4 = kF <= 8
    emd = (Z_80 + Z_975) * np.nanstd(moy_ep(eh), axis=1, ddof=1) * math.sqrt(2.0) / 8.0
    mP = np.nanmean(moy_ep(ep), axis=1) - np.nanmean(moy_ep(eh), axis=1)
    tours = np.where(kP > 0, np.ceil(N_CIBLE * N_ETAL / (SURETE * np.maximum(kP, 1)) / PAR_TOUR), np.inf)
    tours_sans = np.where(kP > 0, np.ceil(N_CIBLE * N_ETAL / np.maximum(kP, 1) / PAR_TOUR), np.inf)
    arret = centrage | ~eo2 | ~eo4
    c1, c2, c3, c4 = kH <= K_H_MAX, (kP > 0) & (kP >= RAPPORT * np.maximum(kH, 1)), emd <= RETENUE * mP, tours <= R_PLAFOND
    part = ~arret & c1 & c2 & c3 & c4
    motif = np.where(arret, 0, np.where(~c1, 1, np.where(~c2, 2, np.where(~c3, 3, np.where(~c4, 4, 9)))))
    about = {"p": np.zeros(R), "a": np.zeros(R)}
    for i in np.where(part)[0]:
        rmax = int(max(R_V1, tours[i]))
        for nom, p in (("p", pP), ("a", pA)):
            x = rng.binomial(PAR_TOUR, p, size=rmax).cumsum()
            about[nom][i] = float(x[3] > SEUIL_M1[rmax] and x[-1] >= N_MIN)
    f = lambda x: f"{float(np.mean(x)):.3f}"
    garde = np.where(mP > 0, emd / np.where(mP > 0, mP, 1.0), np.inf)       # part de l'excès planté qu'un élève doit garder pour être vu
    ligne = "\t".join([str(x) for x in cle] + [str(m), f"{b:g}", str(phi), nom_defaut, str(int(dv)), f"{pP:.3f}", f"{pA:.3f}",
                       f(sA), f(sL), f(sR), f(centrage), f(eo2), f(eo4), f(arret),
                       f(part & (tours <= R_V1)), f(part & (tours > R_V1)), f(~part & ~arret),
                       f(motif == 1), f(motif == 2), f(motif == 3), f(motif == 4), f((motif == 4) & (tours_sans <= R_PLAFOND)),
                       f"{about['p'][part].mean():.2f}" if part.any() else "-", f"{about['a'][part].mean():.2f}" if part.any() else "-",
                       f"{np.median(tours[part]):.0f}" if part.any() else "-", f"{kH.mean():.2f}", f"{kP.mean():.2f}", f"{np.nanmedian(emd):.4f}",
                       f"{np.nanmedian(mP):.4f}", f"{np.median(garde):.2f}", f"{np.nanmean(ef) - np.nanmean(eh):.3f}"])
    return ligne, (m, nom_defaut, float(part.mean()), bool(dv))


def moy_et(x):
    x = np.asarray(x, dtype=float)
    return float(x.mean()), float(x.std(ddof=1) / math.sqrt(len(x)))


def main():
    debut = time.time()
    ss = np.random.SeedSequence()
    gL, gD = ss.spawn(2)
    cells = [(s0, s1, rho, a, p) for p in PROFILS for a in ANCRES for rho in RHOS for s1 in S1S for s0 in S0S]
    print(f"entropie SeedSequence : {ss.entropy}")
    print(f"numpy {np.__version__} ; organisme : exces x{FACTEUR:g}, {T} actions, ancre commune au premier pas ({NC} actions comptees, {N_BORNABLES} bornables au moins) ; "
          f"{len(cells)} cellules ; blocs {MS} ; bornes {BORNES} ; phi {PHIS} ; defaut {DEFAUT} ; {N_LOTS} lots x {N_PAR_LOT} ; choix sur les lots 1 a {LOTS_CHOIX} ; "
          f"marge de l'oracle {MARGE_ORACLE} ; etalonnages {N_REP_D} ; plafond de tours (hypothese) {R_PLAFOND}")
    taches = [(cle, b) for b in range(N_LOTS) for cle in cells]
    with Pool(4) as pool:
        par = {}
        for r in pool.imap(lot, zip(taches, gL.spawn(len(taches))), chunksize=8):
            par[(r["cle"], r["lot"])] = r
        CH, EV = range(LOTS_CHOIX), range(LOTS_CHOIX, N_LOTS)

        def dist(cle, q, b_, quoi):
            r = par[(cle, b_)]
            dp, da = distingue(r[f"th_{q}"], r[f"tp_{q}"]), distingue(r[f"th_{q}"], r[f"ta_{q}"])
            return {"p": dp, "a": da, "j": dp and da}[quoi]

        def couv(q, lots, quoi="j"):
            return np.array([np.mean([dist(cle, q, b_, quoi) for cle in cells]) for b_ in lots])

        # ---------------------------------------------------------- décision (1) : borne et plancher, par oracle
        choix = {}
        for m in MS:
            ref = couv(f"{m}_{DEFAUT[0]}_{DEFAUT[1]}", CH)
            av = {(b, phi): moy_et(couv(f"{m}_{b}_{phi}", CH) - ref) for b in BORNES for phi in PHIS if (b, phi) != DEFAUT}
            bons = [k_ for k_ in av if av[k_][0] - 2 * av[k_][1] > 0]
            choix[m] = max(bons, key=lambda k_: (av[k_][0], -k_[0], -abs(k_[1] - DEFAUT[1]))) if bons else DEFAUT
            print(f"\n# DECISION (1), bloc de {m}, lots 1 a {LOTS_CHOIX} : couverture jointe du defaut {moy_et(ref)[0]:.3f} ; avantage de chaque paire (borne, phi) sur le defaut "
                  f"(moyenne, erreur type) : { {k_: (round(a_, 3), round(e_, 4)) for k_, (a_, e_) in av.items()} } ; RENDU : borne x{choix[m][0]:g}, phi {choix[m][1]} "
                  f"(plancher {regle(*choix[m])['F']:.3f} decade)")
        # ---------------------------------------------------------- décision (2) : oracle
        q = {m: f"{m}_{choix[m][0]}_{choix[m][1]}" for m in MS}
        diff = couv(q[4], EV) - couv(q[8], EV)
        md, ed = moy_et(diff)
        m_ret = 4 if md - 2 * ed > MARGE_ORACLE else 8
        print(f"\n# DECISION (2), oracle, lots {LOTS_CHOIX + 1} a {N_LOTS} : couverture jointe sans couplage {moy_et(couv(q[8], EV))} ; avec couplage par moitie {moy_et(couv(q[4], EV))} ; "
              f"difference {md:.3f} +- {ed:.4f} ; difference moins deux erreurs types {md - 2 * ed:.3f} ; marge {MARGE_ORACLE}")
        print(f"# RENDU : {'COUPLAGE PAR MOITIE (bloc de 4)' if m_ret == 4 else 'AUCUN COUPLAGE (bloc de 8)'}")
        for m in MS:
            for quoi, nom in (("p", "exces plante"), ("a", "maitre ancre"), ("j", "jointe")):
                mm, ee = moy_et(couv(q[m], EV, quoi))
                print(f"#   bloc de {m} ({q[m]}) couverture {nom} : {mm:.3f} +- {ee:.4f}")

        def g(cle, k_):
            return float(np.mean([par[(cle, b_)][k_] for b_ in EV]))

        def tot(cle, k_):
            return float(np.sum([par[(cle, b_)][k_] for b_ in EV]))

        # ---------------------------------------------------------- détail par cellule, les deux oracles
        vrais = {}
        for m in MS:
            print(f"\n# B. detail par cellule, bloc de {m}, borne x{choix[m][0]:g}, phi {choix[m][1]} (lots {LOTS_CHOIX + 1} a {N_LOTS})")
            print("\t".join(["s0", "s1", "ancrage", "ancre", "profil", "taux_honnete", "taux_plante", "taux_ancre", "distingue_plante", "distingue_ancre", "snr_plante", "snr_ancre",
                             "ecart_type_e_honnete", "mesure/vrai_plante", "mesure/vrai_ancre", "vrai_total_acceptes_plante", "mesure_total_acceptes_plante",
                             "vrai_total_acceptes_ancre", "mesure_total_acceptes_ancre", "part_deux_plus_grands_plante", "plus_grand_exces_vrai_acceptes_ancre",
                             "part_d_actions_plantees_a_exces_mesure_negatif", "exces_mesure_moyen_des_plantes", "ecart_type_entre_episodes"]))
            for cle in cells:
                pH, pP, pA = (g(cle, f"t{x}_{q[m]}") for x in "hpa")
                vrais[(cle, m)] = (pP, pA, distingue(pH, pP) and distingue(pH, pA), distingue(pH, pP), distingue(pH, pA))

                def rt(num, den):
                    d_ = tot(cle, den)
                    return f"{tot(cle, num) / d_:.3f}" if d_ > 0 else "-"

                print("\t".join([str(x) for x in cle] + [f"{pH:.4f}", f"{pP:.4f}", f"{pA:.4f}", str(int(distingue(pH, pP))), str(int(distingue(pH, pA)))]
                                + [f"{g(cle, f'{x}_{m}'):.3f}" for x in ("snr_p", "snr_a", "sd_e", "mv_p", "mv_a")]
                                + [rt(f"vrai_p_{q[m]}", f"n_p_{q[m]}"), rt(f"mes_p_{q[m]}", f"n_p_{q[m]}"), rt(f"vrai_a_{q[m]}", f"n_a_{q[m]}"), rt(f"mes_a_{q[m]}", f"n_a_{q[m]}"),
                                   rt(f"deux_p_{q[m]}", f"mes_p_{q[m]}"), rt(f"max_a_{q[m]}", f"n_a_{q[m]}"), f"{g(cle, f'neg_p_{m}'):.3f}", f"{g(cle, f'mP_{m}'):.4f}",
                                   f"{g(cle, f'sd_moy_{m}'):.4f}"]))
        sys.stdout.flush()
        # ---------------------------------------------------------- étalonnages : sain (108 cellules, deux oracles) ; défauts (9 cellules, oracle retenu)
        neuf = [cle for cle in cells if cle[0] == 0.8 and cle[3] == "dernier" and cle[4] == "reference"]
        cD = [(cle, m, *choix[m], "sain", {}, *vrais[(cle, m)][:3]) for m in MS for cle in cells]
        cD += [(cle, m_ret, *choix[m_ret], nom, d, *vrais[(cle, m_ret)][:3]) for nom, d in DEFAUTS_EPREUVE[1:] for cle in neuf]
        print(f"\n# D. etalonnages complets ({len(cD)} cellules x configurations ; {N_REP_D} etalonnages chacune)")
        print("\t".join(["s0", "s1", "ancrage", "ancre", "profil", "bloc", "borne", "phi", "etat_de_l_oracle", "distingue_vrai(joint)", "taux_plante_vrai", "taux_ancre_vrai",
                         "arret_rangs_origine", "arret_lisibilite", "arret_rangs_reecrit", "arret_centrage", "P(sensibilite passe)", "P(rejet du flagrant passe)",
                         "arret_epreuves", "part_i", "part_ii", "part_iii", "motif_C1", "motif_C2", "motif_C3", "motif_C4", "motif_C4_du_a_la_marge",
                         "P(aboutit|part,plante)", "P(aboutit|part,ancre)", "tours_medians", "k_H_moyen", "k_P_moyen", "EMD_mediane", "exces_moyen_des_plantes_mediane",
                         "part_de_l_exces_a_garder_pour_etre_vu", "exces_mesure_du_flagrant"]))
        err = {}
        for l, (m, nom, pp, dv) in pool.imap(etalonnage, zip(cD, gD.spawn(len(cD))), chunksize=2):
            print(l)
            if nom == "sain":
                err.setdefault(m, {True: [], False: []})[dv].append((1 - pp) if dv else pp)
        for m, e in err.items():
            a_, b_ = e[False], e[True]
            print(f"# ERREURS DES BRANCHES, oracle sain, bloc de {m} : part alors que le saboteur ne se distingue pas (plante et ancre) : "
                  + (f"moyenne {np.mean(a_):.3f}, maximum {np.max(a_):.3f} sur {len(a_)} cellules" if a_ else "aucune cellule")
                  + " ; ne part pas alors qu'il se distingue : " + (f"moyenne {np.mean(b_):.3f}, maximum {np.max(b_):.3f} sur {len(b_)} cellules" if b_ else "aucune cellule"))
    print(f"\nduree : {time.time() - debut:.0f} s")


if __name__ == "__main__":
    main()

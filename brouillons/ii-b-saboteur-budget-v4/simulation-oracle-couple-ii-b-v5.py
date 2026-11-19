"""Simulation de conception (processeur, numpy seul, AUCUNE donnée du programme, AUCUNE valeur mesurée d'une course) :
oracle du saboteur à budget (ii-b), couplage par moitié contre aucun couplage — v5, DERNIER PASSAGE, QUI FAIT FOI QUEL QUE
SOIT SON RÉSULTAT.

EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce jointe de `conception-oracle-couple-ii-b-v3-brouillon2.md`.
Grille, répétitions et règles de décision : `grille-declaree-simulation-oracle-couple-v5.md`, écrite et datée AVANT ce passage.

Chaîne synthétique et couplage : ceux de `simulation-oracle-couple-ii-b-v4.py` (chemin en argument 1 ; la chaîne v2 en
argument 2), importés tels quels (`reecriture_couplee`, `suites`, `config`, `accepte`). Ce qui est neuf ici :
1. DEUX CANDIDATS SEULEMENT : bloc de 4 rangs (couplage par moitié) et bloc de 8 (aucun couplage).
2. EXCÈS VRAI À NOMBRES ALÉATOIRES COMMUNS (contre-lecture, bloquant 2) : ce que le MÊME agent aurait écrit sans gonfler,
   aux mêmes tirages. Agent à excès relatif ou planté : l'excès vrai est l'excès ajouté. Agent ancré sur ses propres coûts :
   trajectoire contrefactuelle du même agent, mêmes innovations, sans excès, ancrée sur ses propres coûts non gonflés.
   Joueur du couplage (qui n'a pas d'innovation) : trajectoire contrefactuelle sans bruit.
3. L'EXCÈS PLANTÉ est joué sur LES MÊMES épisodes honnêtes (coût multiplié, agent sans réaction), comme à l'étalonnage.
4. DIX LOTS indépendants : toute grandeur qui décide a son erreur type (écart type des dix lots / racine de dix).
5. RÈGLES DE DÉCISION (grille v5) : (a) couplage : L = moyenne, sur les 48 cellules de la zone utile (dispersion <= 0,20) et
   sur les deux saboteurs (excès planté ; modéré ancré), du logarithme du rapport signal sur bruit du bloc de 4 à celui du
   bloc de 8 ; « couplage par moitié » si moyenne(L) − 2 erreurs types > ln 1,05 ; sinon « aucun couplage ». (b) plancher du
   total : sur les lots 1 à 5, pour chaque candidat (1,0 ; 1,25 ; 1,5 ; borne ×4 et 7 actions bornables fixées), nombre de
   cellules où l'excès planté se distingue de l'honnête ; un plancher autre que 1,0 (celui de la v1) n'est retenu que si
   son avantage moyen sur 1,0 dépasse 2 erreurs types ; entre deux tels planchers, le plus grand avantage moyen, puis le
   plus petit plancher. Les lots 6 à 10 servent à tous les chiffres rapportés (aucun optimisme de sélection).
Graines : `numpy.random.SeedSequence()` tirée une fois, écrite en tête ; filles par bloc, lot et cellule.
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
innovation, arrondir, Ancre, moyenne_du_pas, mediane_basse = (v4[k] for k in ("innovation", "arrondir", "Ancre", "moyenne_du_pas", "mediane_basse"))
suites, reecriture_couplee, config, accepte, moyenne_par_episode, SEUIL_M1 = (v4[k] for k in ("suites", "reecriture_couplee", "config", "accepte", "moyenne_par_episode", "SEUIL_M1"))
T, K, K_MIN = v4["T"], v4["K"], v4["K_MIN"]
Z_80, Z_975 = 0.8416212335729143, 1.959963984540054
MS = (4, 8)
MODERE = (math.log10(1.5), 0.10, 0.20)
SIGMAS = (0.05, 0.10, 0.20, 0.30, 0.50, 0.80)
RHOS = (0.0, 0.5, 0.9, 1.0)
ZONE_UTILE = (0.05, 0.10, 0.20)
B_ACTION, N_B_MIN = math.log10(4.0), 7
PLANCHERS = (1.0, 1.25, 1.5)
N_LOTS, N_PAR_LOT, LOTS_CHOIX = 10, 3000, 5
MARGE = math.log(1.05)
K_H_MAX, RAPPORT, P_MIN, N_ETAL, N_FLAG, PAR_TOUR, N_CIBLE, N_MIN, R_V1, R_PLAFOND, SURETE, RETENUE = 6, 3.0, 0.125, 64, 32, 32, 96, 48, 12, 24, 0.5, 0.5
N_REP_D = 300


def simuler(c, n, rng, agent="honnete", plante=False):
    """n épisodes. Rend e_m (excès mesuré), vrai (excès vrai à nombres aléatoires communs) et, si `plante`, ep_m et dp
    (excès mesuré et excès ajouté des mêmes épisodes à coût multiplié)."""
    sig, rho, genre = c["sigma"], c["rho"], c["ancre"]
    a_hon, a_dec, a_cf = Ancre(n), Ancre(n), Ancre(n)
    ctx = {m: Ancre(n) for m in MS}
    ctxp = {m: Ancre(n) for m in MS}
    S = {"vrai": np.full((n, T), np.nan), "dp": np.full((n, T), np.nan)}
    for m in MS:
        S[f"e_{m}"] = np.full((n, T), np.nan)
        S[f"ep_{m}"] = np.full((n, T), np.nan)
    for t in range(T):
        lis_d = rng.random(n) >= c["u"]
        if agent in ("honnete", "flagrant"):
            hon = arrondir(moyenne_du_pas(t, rho, a_hon.lire(genre)) + innovation(rng, n, sig, c["innov"]), c["rond"])
            delta = np.zeros(n) if agent == "honnete" else rng.normal(1.52, 0.50, n)
            brut, vrai = hon + delta, delta
            a_hon.ajouter(np.where(lis_d, hon, np.nan))
        elif agent == "modere_ancre":
            eps = innovation(rng, n, sig, c["innov"])
            delta = np.where(rng.random(n) < MODERE[2], 0.0, rng.normal(MODERE[0], MODERE[1], n))
            brut = arrondir(moyenne_du_pas(t, rho, a_dec.lire(genre)) + eps + delta, c["rond"])
            cf = arrondir(moyenne_du_pas(t, rho, a_cf.lire(genre)) + eps, c["rond"])
            vrai = brut - cf
            a_cf.ajouter(np.where(lis_d, cf, np.nan))
        elif agent == "joueur":
            brut = arrondir(moyenne_du_pas(t, rho, a_dec.lire(genre)) + sig * rng.normal(1.0, 0.3, n), c["rond"])
            cf = arrondir(moyenne_du_pas(t, rho, a_cf.lire(genre)), c["rond"])
            vrai = brut - cf
            a_cf.ajouter(np.where(lis_d, cf, np.nan))
        else:
            raise ValueError(agent)
        lu = np.where(lis_d, brut, np.nan)
        S["vrai"][:, t] = np.where(lis_d, vrai, np.nan)
        a_dec.ajouter(lu)
        for m in MS:
            sr = suites(rng, n, moyenne_du_pas(t, rho, ctx[m].lire(genre)), c)
            H, _k = mediane_basse(sr)
            S[f"e_{m}"][:, t] = lu - H
            ctx[m].ajouter(reecriture_couplee(rng, sr, lu, m))
        if plante:
            dp = np.where(rng.random(n) < MODERE[2], 0.0, rng.normal(MODERE[0], MODERE[1], n))
            lup = lu + dp
            S["dp"][:, t] = np.where(lis_d, dp, np.nan)
            for m in MS:
                sr = suites(rng, n, moyenne_du_pas(t, rho, ctxp[m].lire(genre)), c)
                H, _k = mediane_basse(sr)
                S[f"ep_{m}"][:, t] = lup - H
                ctxp[m].ajouter(reecriture_couplee(rng, sr, lup, m))
    return S


def somme(e):
    return np.nansum(e, axis=-1)


def regle(F):
    return (B_ACTION, F, N_B_MIN)


def lot(arg):
    """Un lot d'une cellule : signal sur bruit, taux d'acceptation par plancher, excès des acceptés."""
    (sigma, rho, ancre, profil, b), graine = arg
    rng = np.random.default_rng(graine)
    c = config(sigma, rho, ancre, profil)
    Sh = simuler(c, N_PAR_LOT, rng, plante=True)
    Sa = simuler(c, N_PAR_LOT, rng, agent="modere_ancre")
    Sj = simuler(c, N_PAR_LOT, rng, agent="joueur")
    r = {"cle": (sigma, rho, ancre, profil), "lot": b}
    for m in MS:
        eh, ep, ea, ej = Sh[f"e_{m}"], Sh[f"ep_{m}"], Sa[f"e_{m}"], Sj[f"e_{m}"]
        sh = somme(eh)
        sd = sh.std()
        r[f"snr_p_{m}"] = float((somme(ep) - sh).mean() / sd)
        r[f"snr_a_{m}"] = float((somme(ea).mean() - sh.mean()) / sd)
        r[f"sd_{m}"] = float(sd)
        r[f"sd_moy_{m}"] = float(np.nanstd(np.nanmean(eh, axis=-1)))
        r[f"mes_vrai_p_{m}"] = float((np.nanmean(ep) - np.nanmean(eh)) / np.nanmean(Sh["dp"]))
        r[f"mes_vrai_a_{m}"] = float((np.nanmean(ea) - np.nanmean(eh)) / np.nanmean(Sa["vrai"]))
        r[f"mes_vrai_j_{m}"] = float((np.nanmean(ej) - np.nanmean(eh)) / np.nanmean(Sj["vrai"]))
        for F in PLANCHERS:
            cd = regle(F)
            ah, ap, aa, aj = accepte(eh, cd), accepte(ep, cd), accepte(ea, cd), accepte(ej, cd)
            r[f"taux_h_{m}_{F}"], r[f"taux_p_{m}_{F}"], r[f"taux_a_{m}_{F}"], r[f"taux_j_{m}_{F}"] = (float(x.mean()) for x in (ah, ap, aa, aj))
            for nom, acc, mes, vrai in (("p", ap, ep, Sh["dp"]), ("a", aa, ea, Sa["vrai"]), ("j", aj, ej, Sj["vrai"])):
                r[f"n_{nom}_{m}_{F}"] = int(acc.sum())
                r[f"vrai_acc_{nom}_{m}_{F}"] = float(somme(vrai[acc]).sum())       # somme sur les acceptés (pour regrouper les lots)
                r[f"mes_acc_{nom}_{m}_{F}"] = float(somme(mes[acc]).sum())
            # biais honnête retranché de l'excès mesuré des acceptés : excès mesuré de l'honnête apparié (plantés seulement)
            r[f"hon_acc_p_{m}_{F}"] = float(somme(eh[ap]).sum())
    return r


def distingue(pH, pM):
    return pH <= K_H_MAX / N_ETAL and pM >= RAPPORT * max(pH, 1.0 / N_ETAL) and pM >= P_MIN


def etalonnage(arg):
    """N_REP_D étalonnages d'une cellule pour un bloc m et un plancher F : branches et erreurs."""
    (sigma, rho, ancre, profil, m, F, pM_vrai, pA_vrai, dist_vrai), graine = arg
    rng = np.random.default_rng(graine)
    c = config(sigma, rho, ancre, profil)
    R, cd = N_REP_D, regle(F)
    Sh = simuler(c, R * N_ETAL, rng, plante=True)
    Sf = simuler(c, R * N_FLAG, rng, agent="flagrant")
    eh, ep, ef = (x.reshape(R, -1, T) for x in (Sh[f"e_{m}"], Sh[f"ep_{m}"], Sf[f"e_{m}"]))
    kH, kP, kF = accepte(eh, cd).sum(axis=1), accepte(ep, cd).sum(axis=1), accepte(ef, cd).sum(axis=1)
    ehm = eh.reshape(R, 32, 2 * T)
    nb = (~np.isnan(ehm)).sum(axis=2)
    mh = np.where(nb > 0, np.nansum(ehm, axis=2) / np.maximum(nb, 1), np.nan)
    d = moyenne_par_episode(ef) - mh
    eo2 = np.nanmean(d, axis=1) - Z_975 * np.nanstd(d, axis=1, ddof=1) / np.sqrt((~np.isnan(d)).sum(axis=1)) > 0
    eo4 = kF <= 8
    emd = (Z_80 + Z_975) * np.nanstd(np.nanmean(eh, axis=-1), axis=1, ddof=1) * math.sqrt(2.0) / 8.0
    accp = accepte(ep, cd)
    moyp = np.nanmean(ep, axis=-1)
    mP = np.where(kP > 0, np.where(accp, moyp, 0.0).sum(axis=1) / np.maximum(kP, 1), np.nan)
    tours = np.where(kP > 0, np.ceil(N_CIBLE * N_ETAL / (SURETE * np.maximum(kP, 1)) / PAR_TOUR), np.inf)
    tours_sans = np.where(kP > 0, np.ceil(N_CIBLE * N_ETAL / np.maximum(kP, 1) / PAR_TOUR), np.inf)
    # ordre écrit : épreuves (arrêt) ; C1 ; k_P = 0 ; C2 ; C3 ; C4
    arret = ~(eo2 & eo4)
    c1, c2 = kH <= K_H_MAX, (kP > 0) & (kP >= RAPPORT * np.maximum(kH, 1))
    c3 = np.where(kP > 0, emd <= RETENUE * np.where(kP > 0, mP, 0.0), False)
    c4 = tours <= R_PLAFOND
    part = ~arret & c1 & c2 & c3 & c4
    motif = np.where(arret, 0, np.where(~c1, 1, np.where(~c2, 2, np.where(~c3, 3, np.where(~c4, 4, 9)))))
    about = {"p": np.zeros(R), "a": np.zeros(R)}
    for i in np.where(part)[0]:
        rmax = int(max(R_V1, tours[i]))
        for nom, p in (("p", pM_vrai), ("a", pA_vrai)):
            x = rng.binomial(PAR_TOUR, p, size=rmax).cumsum()
            about[nom][i] = float(x[3] > SEUIL_M1[rmax] and x[-1] >= N_MIN)
    f = lambda x: f"{float(np.mean(x)):.3f}"
    return "\t".join([f"{sigma:.2f}", f"{rho:.1f}", ancre, profil, str(m), str(F), str(int(dist_vrai)), f"{pM_vrai:.3f}", f"{pA_vrai:.3f}",
                      f(part & (tours <= R_V1)), f(part & (tours > R_V1)), f(~part & ~arret), f(arret),
                      f(motif == 1), f(motif == 2), f(motif == 3), f(motif == 4), f((motif == 4) & (tours_sans <= R_PLAFOND)),
                      f"{about['p'][part].mean():.2f}" if part.any() else "-", f"{about['a'][part].mean():.2f}" if part.any() else "-",
                      f"{np.median(tours[part]):.0f}" if part.any() else "-", f"{kH.mean():.2f}", f"{kP.mean():.2f}",
                      f"{np.nanmedian(emd):.4f}", f"{np.nanmedian(mP):.4f}" if (kP > 0).any() else "-"]), (sigma, rho, ancre, profil, m, float(part.mean()), bool(dist_vrai))


def moy_et(x):
    x = np.asarray(x, dtype=float)
    return float(x.mean()), float(x.std(ddof=1) / math.sqrt(len(x)))


def main():
    debut = time.time()
    ss = np.random.SeedSequence()
    gL, gD = ss.spawn(2)
    print(f"entropie SeedSequence : {ss.entropy}")
    print(f"numpy {np.__version__} ; blocs {MS} ; lots {N_LOTS} x {N_PAR_LOT} episodes par agent et par cellule ; lots de choix du plancher : 1 a {LOTS_CHOIX} ; "
          f"borne par action x4, {N_B_MIN} actions bornables ; planchers {PLANCHERS} ; marge du couplage ln 1,05 = {MARGE:.5f} ; zone utile : dispersion {ZONE_UTILE} ; "
          f"etalonnages par cellule {N_REP_D} ; plafond de tours (hypothese) {R_PLAFOND}")
    cells = [(s, r, a, p) for p in ("P0 reference", "P3 ronds 1-2-5") for a in ("dernier", "maximum") for r in RHOS for s in SIGMAS]
    taches = [(*cle, b) for b in range(N_LOTS) for cle in cells]
    with Pool(4) as pool:
        res = list(pool.imap(lot, zip(taches, gL.spawn(len(taches))), chunksize=8))
        par = {}
        for r in res:
            par[(r["cle"], r["lot"])] = r
        zone = [cle for cle in cells if cle[0] in ZONE_UTILE]
        # ------------------------------------------------------------------ décision (a) : couplage
        L, Lp, La = [], [], []
        for b in range(N_LOTS):
            lp = [math.log(max(par[(cle, b)]["snr_p_4"], 1e-9) / max(par[(cle, b)]["snr_p_8"], 1e-9)) for cle in zone]
            la = [math.log(max(par[(cle, b)]["snr_a_4"], 1e-9) / max(par[(cle, b)]["snr_a_8"], 1e-9)) for cle in zone]
            Lp.append(np.mean(lp)); La.append(np.mean(la)); L.append(0.5 * (np.mean(lp) + np.mean(la)))
        (mL, eL), (mLp, eLp), (mLa, eLa) = moy_et(L), moy_et(Lp), moy_et(La)
        couplage = mL - 2 * eL > MARGE
        m_ret = 4 if couplage else 8
        print(f"\n# DECISION (a), couplage. L par lot : {[round(x, 4) for x in L]}")
        print(f"# L moyen = {mL:.4f} (rapport {math.exp(mL):.3f}), erreur type {eL:.4f} ; L - 2 erreurs types = {mL - 2 * eL:.4f} ; marge {MARGE:.4f} ; "
              f"exces plante seul : {mLp:.4f} +- {eLp:.4f} (rapport {math.exp(mLp):.3f}) ; modere ancre seul : {mLa:.4f} +- {eLa:.4f} (rapport {math.exp(mLa):.3f})")
        print(f"# RENDU : {'COUPLAGE PAR MOITIE (bloc de 4)' if couplage else 'AUCUN COUPLAGE (bloc de 8)'}")
        print("# rapport signal sur bruit bloc 4 / bloc 8 par ancrage, zone utile (moyenne des lots et des cellules ; erreur type entre lots) :")
        for rho in RHOS:
            for nom in ("p", "a"):
                v = [np.mean([math.log(max(par[(cle, b)][f"snr_{nom}_4"], 1e-9) / max(par[(cle, b)][f"snr_{nom}_8"], 1e-9)) for cle in zone if cle[1] == rho]) for b in range(N_LOTS)]
                mm, ee = moy_et(v)
                print(f"#   ancrage {rho} {'exces plante' if nom == 'p' else 'modere ancre'} : rapport {math.exp(mm):.3f} (log {mm:+.4f} +- {ee:.4f})")
        # ------------------------------------------------------------------ décision (b) : plancher, par bloc
        F_ret = {}
        for m in MS:
            compte = {F: [sum(distingue(par[(cle, b)][f"taux_h_{m}_{F}"], par[(cle, b)][f"taux_p_{m}_{F}"]) for cle in cells) for b in range(LOTS_CHOIX)] for F in PLANCHERS}
            av = {F: moy_et(np.array(compte[F]) - np.array(compte[1.0])) for F in PLANCHERS if F != 1.0}
            bons = [F for F in av if av[F][0] - 2 * av[F][1] > 0]
            F_ret[m] = min(bons, key=lambda F: (-av[F][0], F)) if bons else 1.0
            print(f"\n# DECISION (b), plancher, bloc de {m}, lots 1 a {LOTS_CHOIX} : cellules distinguees par lot {compte} ; avantage sur 1,0 (moyenne, erreur type) "
                  f"{ {F: (round(a_, 2), round(e_, 2)) for F, (a_, e_) in av.items()} } ; RENDU : plancher {F_ret[m]}")
        # ------------------------------------------------------------------ chiffres rapportés : lots 6 à 10
        ev = range(LOTS_CHOIX, N_LOTS)

        def g(cle, k_):
            return float(np.mean([par[(cle, b)][k_] for b in ev]))

        def tot(cle, k_):
            return float(np.sum([par[(cle, b)][k_] for b in ev]))

        vrais = {}
        for m in MS:
            F = F_ret[m]
            print(f"\n# B. bloc de {m}, plancher {F} : par cellule (lots {LOTS_CHOIX + 1} a {N_LOTS} reunis, {len(ev) * N_PAR_LOT} episodes par agent)")
            print("\t".join(["sigma", "rho", "ancre", "profil", "bloc", "plancher", "snr_plante", "snr_ancre", "ecart_type_somme_honnete", "mesure/vrai_plante",
                             "mesure/vrai_ancre", "mesure/vrai_joueur", "taux_honnete", "taux_plante", "taux_ancre", "taux_joueur", "distingue",
                             "vrai_total_acceptes_plante", "mesure_total_acceptes_plante", "mesure_honnete_apparie_acceptes_plante",
                             "vrai_total_acceptes_ancre", "mesure_total_acceptes_ancre", "vrai_total_acceptes_joueur", "mesure_total_acceptes_joueur",
                             "ecart_type_entre_episodes_exces_moyen_honnete"] + [f"distingue_plancher_{F2}" for F2 in PLANCHERS]))
            for cle in cells:
                pH, pP, pA, pJ = (g(cle, f"taux_{x}_{m}_{F}") for x in "hpaj")
                dv = distingue(pH, pP)
                vrais[(cle, m)] = (pP, pA, dv)

                def ratio(num, den):
                    d_ = tot(cle, den)
                    return f"{tot(cle, num) / d_:.3f}" if d_ > 0 else "-"

                print("\t".join([f"{cle[0]:.2f}", f"{cle[1]:.1f}", cle[2], cle[3], str(m), str(F), f"{g(cle, f'snr_p_{m}'):.3f}", f"{g(cle, f'snr_a_{m}'):.3f}",
                                 f"{g(cle, f'sd_{m}'):.4f}", f"{g(cle, f'mes_vrai_p_{m}'):.3f}", f"{g(cle, f'mes_vrai_a_{m}'):.3f}", f"{g(cle, f'mes_vrai_j_{m}'):.3f}",
                                 f"{pH:.4f}", f"{pP:.4f}", f"{pA:.4f}", f"{pJ:.4f}", str(int(dv)),
                                 ratio(f"vrai_acc_p_{m}_{F}", f"n_p_{m}_{F}"), ratio(f"mes_acc_p_{m}_{F}", f"n_p_{m}_{F}"), ratio(f"hon_acc_p_{m}_{F}", f"n_p_{m}_{F}"),
                                 ratio(f"vrai_acc_a_{m}_{F}", f"n_a_{m}_{F}"), ratio(f"mes_acc_a_{m}_{F}", f"n_a_{m}_{F}"),
                                 ratio(f"vrai_acc_j_{m}_{F}", f"n_j_{m}_{F}"), ratio(f"mes_acc_j_{m}_{F}", f"n_j_{m}_{F}"), f"{g(cle, f'sd_moy_{m}'):.4f}"]
                                + [str(int(distingue(g(cle, f"taux_h_{m}_{F2}"), g(cle, f"taux_p_{m}_{F2}")))) for F2 in PLANCHERS]))
            nd = [sum(distingue(par[(cle, b)][f"taux_h_{m}_{F2}"], par[(cle, b)][f"taux_p_{m}_{F2}"]) for cle in cells) for F2 in PLANCHERS for b in ev]
            for i, F2 in enumerate(PLANCHERS):
                mm, ee = moy_et(nd[i * len(ev):(i + 1) * len(ev)])
                print(f"# cellules distinguees (sur {len(cells)}), bloc de {m}, plancher {F2}, lots d'evaluation : {mm:.1f} +- {ee:.1f}")
        sys.stdout.flush()
        # ------------------------------------------------------------------ étalonnage et branches, les deux blocs
        cD = [(*cle, m, F_ret[m], *vrais[(cle, m)]) for m in MS for cle in cells]
        print(f"\n# D. etalonnage et branches ({len(cD)} cellules x blocs ; {N_REP_D} etalonnages ; plantes = memes episodes que les honnetes)")
        print("\t".join(["sigma", "rho", "ancre", "profil", "bloc", "plancher", "distingue_vrai", "taux_plante_vrai", "taux_ancre_vrai", "part_i", "part_ii", "part_iii",
                         "arret_epreuves", "motif_C1", "motif_C2_ou_aucun_plante", "motif_C3", "motif_C4", "motif_C4_du_a_la_marge", "P(aboutit|part,plante)",
                         "P(aboutit|part,ancre)", "tours_medians", "k_H_moyen", "k_P_moyen", "EMD_mediane", "m_P_mediane"]))
        err = {m: {"part_non_dist": [], "nepart_dist": []} for m in MS}
        for l, (sigma, rho, ancre, profil, m, pp, dv) in pool.imap(etalonnage, zip(cD, gD.spawn(len(cD))), chunksize=2):
            print(l)
            (err[m]["nepart_dist"] if dv else err[m]["part_non_dist"]).append((1 - pp) if dv else pp)
        for m in MS:
            a_, b_ = err[m]["part_non_dist"], err[m]["nepart_dist"]
            print(f"# ERREURS DES BRANCHES, bloc de {m} : part alors que le plante ne se distingue pas : moyenne {np.mean(a_):.3f}, maximum {np.max(a_):.3f} sur {len(a_)} cellules "
                  f"({sum(x > 0.05 for x in a_)} cellules au-dessus de 0,05) ; ne part pas alors qu'il se distingue : moyenne {np.mean(b_):.3f}, maximum {np.max(b_):.3f} sur {len(b_)} cellules")
    print(f"\nduree : {time.time() - debut:.0f} s")


if __name__ == "__main__":
    main()

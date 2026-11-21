"""Simulation de conception (processeur, numpy seul) : l'organisme changé du saboteur à budget (ii-b) — v1,
UN SEUL PASSAGE, QUI FAIT FOI QUEL QUE SOIT SON RÉSULTAT.

EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce jointe de `conception-organisme-change-ii-b-v4-brouillon1.md`.
Grille, répétitions, règles de décision : `grille-declaree-simulation-organisme-change-v1.md`, écrite et datée AVANT ce passage.

UNE DONNÉE DE LA PREMIÈRE COURSE ENTRE ICI, vue avant la conception (complément 4 du mandat, § 2) : la dispersion, par action,
des suites du jumeau honnête — médiane 0,65 décade au premier pas (racine de la moyenne des carrés 0,79) ; médiane 0,078 aux
pas suivants (quartiles 0,035 et 0,14, neuvième décile 0,24, racine de la moyenne des carrés 0,16). Elle fixe le CENTRE de la
grille d'environnement ; aucune autre valeur de cette course n'est connue du rédacteur.

CHAÎNE SYNTHÉTIQUE À DEUX RÉGIMES (unité : décade). Niveau de fond montant de 0,1 par pas. Au premier pas, tout écrivain
honnête tire son coût avec la dispersion s0. Aux pas suivants : (1 − rho)·niveau + rho·(ancre + 0,1) + innovation, l'ancre
étant le dernier ou le plus grand coût lisible de son contexte ; la dispersion de l'innovation est propre à l'ACTION (la même
pour l'agent et pour les suites du jumeau de cette action), tirée d'une loi log-normale de médiane s1 et d'écart type
logarithmique 0,85 (cette loi a pour quartiles 0,56 et 1,77 fois la médiane, pour neuvième décile 2,97 fois, pour racine de
la moyenne des carrés 2,06 fois : avec s1 = 0,078, elle rend 0,044 ; 0,138 ; 0,23 ; 0,16 — les nombres de la donnée).
Coûts ronds et suites illisibles comme dans les simulations précédentes. Fonctions importées de
`simulation-oracle-couple-ii-b-v4.py` (argument 1 ; chaîne v2 en argument 2) : couplage, médiane basse, ancres, arrondi.

ORGANISMES CANDIDATS : excès demandé par action ×1,5 (celui de l'origine), ×2 ou ×3 (loi : nul une fois sur cinq, sinon
normale de moyenne log10 du facteur et d'écart type 0,57 fois cette moyenne) ; 10 ou 20 actions ; avec ou sans ANCRE
COMMUNE AU PREMIER PAS (le coût du premier pas de l'agent reste tel quel dans le contexte du jumeau ; l'excès n'est ni
demandé, ni planté, ni compté au premier pas). Oracle : aucun couplage (bloc de 8) ou couplage par moitié (bloc de 4).
RÈGLE D'ACCEPTATION, par organisme : borne par action ×4 (fixe) ; actions bornables au moins 0,7 × (actions comptées),
arrondi au-dessus (fixe) ; plancher du total = phi × (excès total attendu) = phi × 0,8 × log10(facteur) × (actions
comptées), phi dans {0,5 ; 0,7 ; 0,9}. phi vaut 0,7 (pour l'organisme d'origine : 0,99 décade, le plancher de la conception
d'origine à 1 % près) sauf si, sur les lots 1 à 5, un autre phi couvre plus de cellules de plus de deux erreurs types.
LES LOTS 6 À 10 DONNENT TOUS LES CHIFFRES RAPPORTÉS ET LA DÉCISION DE COUVERTURE (aucun optimisme de sélection).
AGENTS : honnête ; les mêmes épisodes à excès PLANTÉ ; maître ANCRÉ sur ses propres coûts (même loi d'excès).
EXCÈS VRAI à nombres aléatoires communs. DIX LOTS indépendants ; erreurs types entre lots.
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
arrondir, Ancre, mediane_basse, reecriture_couplee, SEUIL_M1 = (v4[k] for k in ("arrondir", "Ancre", "mediane_basse", "reecriture_couplee", "SEUIL_M1"))
K, K_MIN, MU0, G = v4["K"], v4["K_MIN"], 2.0, 0.1
Z_80, Z_975 = 0.8416212335729143, 1.959963984540054
MS = (8, 4)
S0S, S1S, RHOS, ANCRES = (0.6, 0.8, 1.0), (0.05, 0.08, 0.12), (0.7, 0.9, 1.0), ("dernier", "maximum")
PROFILS = {"reference": ("aucun", 0.10), "un chiffre": ("1 chiffre", 0.10)}
LOG_SD_S1 = 0.85
FACTEURS, LONGUEURS, COMMUNES = (1.5, 2.0, 3.0), (10, 20), (False, True)
ORGANISMES = [(f, T, a) for f in FACTEURS for T in LONGUEURS for a in COMMUNES]      # ordre : du moins changé au plus changé
B_ACTION = math.log10(4.0)
N_LOTS, N_PAR_LOT, N_REP_D, LOTS_CHOIX = 10, 1500, 300, 5
PHIS, PHI_DEFAUT = (0.5, 0.7, 0.9), 0.7
K_H_MAX, RAPPORT, P_MIN, N_ETAL, N_FLAG, PAR_TOUR, N_CIBLE, N_MIN, R_V1, R_PLAFOND, SURETE, RETENUE = 6, 3.0, 0.125, 64, 32, 32, 96, 48, 12, 24, 0.5, 0.5
COUVERTURE_MIN = 0.90


def constantes(org, phi=PHI_DEFAUT):
    f, T, commune = org
    nc = T - 1 if commune else T
    return {"b": B_ACTION, "F": phi * 0.8 * math.log10(f) * nc, "N": math.ceil(0.7 * nc - 1e-9), "nc": nc}


def moyenne(t, rho, anc):
    mu = MU0 + G * t
    return np.where(np.isnan(anc), mu, (1 - rho) * mu + rho * (anc + G))


def tirer(rng, n, org):
    f = org[0]
    m = math.log10(f)
    return np.where(rng.random(n) < 0.20, 0.0, rng.normal(m, 0.57 * m, n))


def simuler(c, org, n, rng, agent="honnete", plante=False):
    """n épisodes de l'organisme `org` dans l'environnement c. Rend, par bloc m : e_m ; si `plante` : ep_m, dp ; vrai ; sig."""
    f, T, commune = org
    rho, genre, rond, u = c["rho"], c["ancre"], c["rond"], c["u"]
    a_hon, a_dec, a_cf = Ancre(n), Ancre(n), Ancre(n)
    ctx = {m: Ancre(n) for m in MS}
    ctxp = {m: Ancre(n) for m in MS}
    S = {"vrai": np.full((n, T), np.nan), "dp": np.full((n, T), np.nan), "sig": np.full((n, T), np.nan)}
    for m in MS:
        S[f"e_{m}"] = np.full((n, T), np.nan)
        S[f"ep_{m}"] = np.full((n, T), np.nan)
    for t in range(T):
        sig = np.full(n, c["s0"]) if t == 0 else c["s1"] * np.exp(LOG_SD_S1 * rng.standard_normal(n))
        S["sig"][:, t] = sig
        lis_d = rng.random(n) >= u
        compte = not (commune and t == 0)
        eps = sig * rng.standard_normal(n)
        if agent in ("honnete", "flagrant"):
            hon = arrondir(moyenne(t, rho, a_hon.lire(genre)) + eps, rond)
            delta = np.zeros(n) if agent == "honnete" else (rng.normal(1.52, 0.50, n) if compte else np.zeros(n))
            brut, vrai = hon + delta, delta
            a_hon.ajouter(np.where(lis_d, hon, np.nan))
        elif agent == "ancre":
            delta = tirer(rng, n, org) if compte else np.zeros(n)
            brut = arrondir(moyenne(t, rho, a_dec.lire(genre)) + eps + delta, rond)
            cf = arrondir(moyenne(t, rho, a_cf.lire(genre)) + eps, rond)
            vrai = brut - cf
            a_cf.ajouter(np.where(lis_d, cf, np.nan))
        else:
            raise ValueError(agent)
        lu = np.where(lis_d, brut, np.nan)
        S["vrai"][:, t] = np.where(lis_d & compte, vrai, np.nan)
        a_dec.ajouter(lu)

        def passe(contextes, valeur, sortie):
            for m in MS:
                sr = arrondir(moyenne(t, rho, contextes[m].lire(genre))[:, None] + sig[:, None] * rng.standard_normal((n, K)), rond)
                sr = np.where(rng.random((n, K)) < u, np.nan, sr)
                H, _k = mediane_basse(sr)
                if compte:
                    S[f"{sortie}_{m}"][:, t] = valeur - H
                contextes[m].ajouter(valeur if not compte else reecriture_couplee(rng, sr, valeur, m))

        passe(ctx, lu, "e")
        if plante:
            dp = tirer(rng, n, org) if compte else np.zeros(n)
            S["dp"][:, t] = np.where(lis_d & compte, dp, np.nan)
            passe(ctxp, lu + dp, "ep")
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
    (cle, io, b), graine = arg
    rng = np.random.default_rng(graine)
    c, org = env(*cle), ORGANISMES[io]
    k = constantes(org)
    Sh = simuler(c, org, N_PAR_LOT, rng, plante=True)
    Sa = simuler(c, org, N_PAR_LOT, rng, agent="ancre")
    r = {"cle": cle, "io": io, "lot": b}
    gonfle = Sh["dp"] > 0
    r["z_med"] = float(np.nanmedian((Sh["dp"] / Sh["sig"])[gonfle]))
    for m in MS:
        eh, ep, ea = Sh[f"e_{m}"], Sh[f"ep_{m}"], Sa[f"e_{m}"]
        sh = somme(eh)
        for phi in PHIS:
            kk = constantes(org, phi)
            r[f"th_{m}_{phi}"], r[f"tp_{m}_{phi}"], r[f"ta_{m}_{phi}"] = (float(accepte(x, kk).mean()) for x in (eh, ep, ea))
        r[f"snr_p_{m}"] = float((somme(ep) - sh).mean() / sh.std())
        r[f"snr_a_{m}"] = float((somme(ea).mean() - sh.mean()) / sh.std())
        r[f"mv_p_{m}"] = float((np.nanmean(ep) - np.nanmean(eh)) / np.nanmean(Sh["dp"]))
        r[f"mv_a_{m}"] = float((np.nanmean(ea) - np.nanmean(eh)) / np.nanmean(Sa["vrai"]))
        r[f"sd_e_{m}"] = float(np.nanstd(eh))
        for phi in PHIS:
            kk = constantes(org, phi)
            for nom, mes, vrai in (("p", ep, Sh["dp"]), ("a", ea, Sa["vrai"])):
                acc = accepte(mes, kk)
                q = f"{nom}_{m}_{phi}"
                r[f"n_{q}"] = int(acc.sum())
                r[f"vrai_{q}"] = float(somme(vrai[acc]).sum())
                r[f"mes_{q}"] = float(somme(mes[acc]).sum())
                if acc.any():
                    tri = np.sort(np.where(np.isnan(mes[acc]), -np.inf, mes[acc]), axis=1)
                    r[f"deux_{q}"] = float(np.where(np.isfinite(tri[:, -2:]), tri[:, -2:], 0.0).sum())
                    r[f"max_{q}"] = float(np.nanmean(np.nanmax(vrai[acc], axis=1)) * acc.sum())
                else:
                    r[f"deux_{q}"], r[f"max_{q}"] = 0.0, 0.0
    return r


def etalonnage(arg):
    (cle, io, m, phi, pP, pA, dv), graine = arg
    rng = np.random.default_rng(graine)
    c, org = env(*cle), ORGANISMES[io]
    k, R, T = constantes(org, phi), N_REP_D, ORGANISMES[io][1]
    Sh = simuler(c, org, R * N_ETAL, rng, plante=True)
    Sf = simuler(c, org, R * N_FLAG, rng, agent="flagrant")
    eh, ep, ef = (x.reshape(R, -1, T) for x in (Sh[f"e_{m}"], Sh[f"ep_{m}"], Sf[f"e_{m}"]))
    kH, kP, kF = accepte(eh, k).sum(axis=1), accepte(ep, k).sum(axis=1), accepte(ef, k).sum(axis=1)

    def moy_ep(x):
        nb = (~np.isnan(x)).sum(axis=-1)
        return np.where(nb > 0, np.nansum(x, axis=-1) / np.maximum(nb, 1), np.nan)

    mh2 = moy_ep(eh.reshape(R, 32, 2 * T))
    d = moy_ep(ef) - mh2
    eo2 = np.nanmean(d, axis=1) - Z_975 * np.nanstd(d, axis=1, ddof=1) / np.sqrt((~np.isnan(d)).sum(axis=1)) > 0
    eo4 = kF <= 8
    emd = (Z_80 + Z_975) * np.nanstd(moy_ep(eh), axis=1, ddof=1) * math.sqrt(2.0) / 8.0
    # excès moyen par action de TOUS les plantés (pas des seuls acceptés : pas de biais de sélection)
    mP = np.nanmean(moy_ep(ep), axis=1) - np.nanmean(moy_ep(eh), axis=1)
    tours = np.where(kP > 0, np.ceil(N_CIBLE * N_ETAL / (SURETE * np.maximum(kP, 1)) / PAR_TOUR), np.inf)
    tours_sans = np.where(kP > 0, np.ceil(N_CIBLE * N_ETAL / np.maximum(kP, 1) / PAR_TOUR), np.inf)
    arret = ~(eo2 & eo4)
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
    ligne = "\t".join([f"{cle[0]}", f"{cle[1]}", f"{cle[2]}", cle[3], cle[4], nom_org(ORGANISMES[io]), str(m), str(int(dv)), f"{pP:.3f}", f"{pA:.3f}",
                       f(part & (tours <= R_V1)), f(part & (tours > R_V1)), f(~part & ~arret), f(arret), f(motif == 1), f(motif == 2), f(motif == 3), f(motif == 4),
                       f((motif == 4) & (tours_sans <= R_PLAFOND)), f"{about['p'][part].mean():.2f}" if part.any() else "-",
                       f"{about['a'][part].mean():.2f}" if part.any() else "-", f"{np.median(tours[part]):.0f}" if part.any() else "-",
                       f"{kH.mean():.2f}", f"{kP.mean():.2f}", f"{np.nanmedian(emd):.4f}", f"{np.nanmedian(mP):.4f}"])
    return ligne, (io, m, float(part.mean()), bool(dv))


def nom_org(org):
    return f"x{org[0]:g}/{org[1]} actions/{'ancre commune' if org[2] else 'sans ancre commune'}"


def moy_et(x):
    x = np.asarray(x, dtype=float)
    return float(x.mean()), float(x.std(ddof=1) / math.sqrt(len(x)))


def main():
    debut = time.time()
    ss = np.random.SeedSequence()
    gL, gD = ss.spawn(2)
    cells = [(s0, s1, rho, a, p) for p in PROFILS for a in ANCRES for rho in RHOS for s1 in S1S for s0 in S0S]
    centre = [cle for cle in cells if cle[1] == 0.08]
    print(f"entropie SeedSequence : {ss.entropy}")
    print(f"numpy {np.__version__} ; {len(cells)} cellules d'environnement (s0 {S0S} ; s1 {S1S} ; ancrage {RHOS} ; ancres {ANCRES} ; profils {list(PROFILS)}) ; "
          f"{len(ORGANISMES)} organismes ; blocs {MS} ; {N_LOTS} lots x {N_PAR_LOT} episodes ; couverture exigee {COUVERTURE_MIN} et toutes les cellules a s1 = 0,08 ; "
          f"etalonnages {N_REP_D} ; plafond de tours (hypothese) {R_PLAFOND}")
    print("constantes par organisme : " + " ; ".join(f"{nom_org(o)} : plancher {constantes(o)['F']:.3f}, {constantes(o)['N']} bornables sur {constantes(o)['nc']} comptees" for o in ORGANISMES))
    taches = [(cle, io, b) for b in range(N_LOTS) for io in range(len(ORGANISMES)) for cle in cells]
    with Pool(4) as pool:
        par = {}
        for r in pool.imap(lot, zip(taches, gL.spawn(len(taches))), chunksize=16):
            par[(r["cle"], r["io"], r["lot"])] = r

        EV = range(LOTS_CHOIX, N_LOTS)

        def g(cle, io, k_):
            return float(np.mean([par[(cle, io, b)][k_] for b in EV]))

        def tot(cle, io, k_):
            return float(np.sum([par[(cle, io, b)][k_] for b in EV]))

        def dist(cle, io, m, phi, b):
            return distingue(par[(cle, io, b)][f"th_{m}_{phi}"], par[(cle, io, b)][f"tp_{m}_{phi}"])

        # choix de phi sur les lots 1 à LOTS_CHOIX
        PHI = {}
        for io in range(len(ORGANISMES)):
            for m in MS:
                cv = {phi: np.array([np.mean([dist(cle, io, m, phi, b) for cle in cells]) for b in range(LOTS_CHOIX)]) for phi in PHIS}
                av = {phi: moy_et(cv[phi] - cv[PHI_DEFAUT]) for phi in PHIS if phi != PHI_DEFAUT}
                bons = [phi for phi in av if av[phi][0] - 2 * av[phi][1] > 0]
                PHI[(io, m)] = max(bons, key=lambda phi: av[phi][0]) if bons else PHI_DEFAUT

        # ---------------------------------------------------------------- couverture par organisme et par bloc
        print("\n# A. couverture de l'environnement, par organisme et par oracle : part des cellules ou l'exces plante se distingue de l'honnete "
              "(moyenne des lots, erreur type) ; idem pour les 36 cellules a s1 = 0,08 ; nombre de ces 36 cellules distinguees dans TOUS les lots")
        print("\t".join(["organisme", "bloc", "phi", "plancher", "bornables_min", "couverture", "erreur_type", "couverture_moins_2_erreurs_types", "couverture_centre",
                         "cellules_du_centre_toujours_distinguees", "couvre", "z_median(exces/dispersion de l'action)", "taux_honnete_median", "taux_plante_median",
                         "taux_ancre_median", "mesure/vrai_plante_median", "mesure/vrai_ancre_median", "vrai_total_acceptes_plante", "mesure_total_acceptes_plante",
                         "vrai_total_acceptes_ancre", "mesure_total_acceptes_ancre", "part_des_deux_plus_grands_exces_acceptes_plante", "plus_grand_exces_vrai_moyen_acceptes_ancre", "snr_plante_median", "snr_ancre_median",
                         "snr_plante_median_centre"]))
        couvre = {}
        for io, org in enumerate(ORGANISMES):
            for m in MS:
                phi = PHI[(io, m)]
                k = constantes(org, phi)
                parts = [np.mean([dist(cle, io, m, phi, b) for cle in cells]) for b in EV]
                mm, ee = moy_et(parts)
                pc = np.mean([[dist(cle, io, m, phi, b) for cle in centre] for b in EV])
                toujours = sum(all(dist(cle, io, m, phi, b) for b in EV) for cle in centre)
                ok = (mm - 2 * ee >= COUVERTURE_MIN) and toujours == len(centre)
                couvre[(io, m)] = ok

                def rt(num, den):
                    a_, d_ = sum(tot(cle, io, num) for cle in cells), sum(tot(cle, io, den) for cle in cells)
                    return f"{a_ / d_:.3f}" if d_ > 0 else "-"

                print("\t".join([nom_org(org), str(m), str(phi), f"{k['F']:.3f}", str(k["N"]), f"{mm:.3f}", f"{ee:.4f}", f"{mm - 2 * ee:.3f}", f"{pc:.3f}", f"{toujours}/{len(centre)}",
                                 str(int(ok)), f"{np.median([g(cle, io, 'z_med') for cle in cells]):.2f}"]
                                + [f"{np.median([g(cle, io, f'{x}_{m}_{phi}') for cle in cells]):.3f}" for x in ("th", "tp", "ta")]
                                + [f"{np.median([g(cle, io, f'{x}_{m}') for cle in cells]):.3f}" for x in ("mv_p", "mv_a")]
                                + [rt(f"vrai_p_{m}_{phi}", f"n_p_{m}_{phi}"), rt(f"mes_p_{m}_{phi}", f"n_p_{m}_{phi}"), rt(f"vrai_a_{m}_{phi}", f"n_a_{m}_{phi}"),
                                   rt(f"mes_a_{m}_{phi}", f"n_a_{m}_{phi}"), rt(f"deux_p_{m}_{phi}", f"mes_p_{m}_{phi}"), rt(f"max_a_{m}_{phi}", f"n_a_{m}_{phi}"),
                                   f"{np.median([g(cle, io, f'snr_p_{m}') for cle in cells]):.3f}", f"{np.median([g(cle, io, f'snr_a_{m}') for cle in cells]):.3f}",
                                   f"{np.median([g(cle, io, f'snr_p_{m}') for cle in centre]):.3f}"]))
        # ---------------------------------------------------------------- décision
        ordre = [(io, m) for io in range(len(ORGANISMES)) for m in MS]            # organismes du moins changé au plus changé ; aucun couplage d'abord
        retenu = next(((io, m) for io, m in ordre if couvre[(io, m)] and ORGANISMES[io][0] < 3.0), None)
        flagrant = next(((io, m) for io, m in ordre if couvre[(io, m)]), None)
        if retenu is not None:
            print(f"\n# DECISION : organisme retenu = {nom_org(ORGANISMES[retenu[0]])}, oracle bloc de {retenu[1]} ({'aucun couplage' if retenu[1] == 8 else 'couplage par moitie'})")
        elif flagrant is not None:
            print(f"\n# DECISION : AUCUN candidat en deca du point flagrant ne couvre l'environnement ; le premier qui couvre demande x3 par action : {nom_org(ORGANISMES[flagrant[0]])}, bloc de {flagrant[1]}")
        else:
            print("\n# DECISION : AUCUN candidat ne couvre l'environnement")
        # ---------------------------------------------------------------- détail par cellule : organisme d'origine et retenu
        a_detailler = list(dict.fromkeys([(0, 8), (0, 4)] + ([retenu] if retenu else []) + ([flagrant] if flagrant and not retenu else [])))
        for io, m in a_detailler:
            phi = PHI[(io, m)]
            print(f"\n# B. detail par cellule : {nom_org(ORGANISMES[io])}, bloc de {m}, phi {phi}")
            print("\t".join(["s0", "s1", "ancrage", "ancre", "profil", "taux_honnete", "taux_plante", "taux_ancre", "distingue", "snr_plante", "snr_ancre",
                             "ecart_type_e_honnete", "mesure/vrai_plante", "mesure/vrai_ancre"]))
            for cle in cells:
                pH, pP, pA = g(cle, io, f"th_{m}_{phi}"), g(cle, io, f"tp_{m}_{phi}"), g(cle, io, f"ta_{m}_{phi}")
                print("\t".join([str(x) for x in cle] + [f"{pH:.4f}", f"{pP:.4f}", f"{pA:.4f}", str(int(distingue(pH, pP)))]
                                + [f"{g(cle, io, f'{x}_{m}'):.3f}" for x in ("snr_p", "snr_a", "sd_e", "mv_p", "mv_a")]))
        sys.stdout.flush()
        # ---------------------------------------------------------------- étalonnage et branches
        cD = [(cle, io, m, PHI[(io, m)], g(cle, io, f"tp_{m}_{PHI[(io, m)]}"), g(cle, io, f"ta_{m}_{PHI[(io, m)]}"),
               distingue(g(cle, io, f"th_{m}_{PHI[(io, m)]}"), g(cle, io, f"tp_{m}_{PHI[(io, m)]}"))) for io, m in a_detailler for cle in cells]
        print(f"\n# D. etalonnage et branches ({len(cD)} cellules x configurations ; {N_REP_D} etalonnages)")
        print("\t".join(["s0", "s1", "ancrage", "ancre", "profil", "organisme", "bloc", "distingue_vrai", "taux_plante_vrai", "taux_ancre_vrai", "part_i", "part_ii", "part_iii",
                         "arret_epreuves", "motif_C1", "motif_C2", "motif_C3", "motif_C4", "motif_C4_du_a_la_marge", "P(aboutit|part,plante)", "P(aboutit|part,ancre)",
                         "tours_medians", "k_H_moyen", "k_P_moyen", "EMD_mediane", "exces_moyen_des_plantes_mediane"]))
        err = {}
        for l, (io, m, pp, dv) in pool.imap(etalonnage, zip(cD, gD.spawn(len(cD))), chunksize=2):
            print(l)
            err.setdefault((io, m), {True: [], False: []})[dv].append((1 - pp) if dv else pp)
        for (io, m), e in err.items():
            a_, b_ = e[False], e[True]
            print(f"# ERREURS DES BRANCHES, {nom_org(ORGANISMES[io])}, bloc de {m} : part alors que le plante ne se distingue pas : "
                  + (f"moyenne {np.mean(a_):.3f}, maximum {np.max(a_):.3f} sur {len(a_)} cellules" if a_ else "aucune cellule non distinguee")
                  + " ; ne part pas alors qu'il se distingue : " + (f"moyenne {np.mean(b_):.3f}, maximum {np.max(b_):.3f} sur {len(b_)} cellules" if b_ else "aucune cellule distinguee"))
    print(f"\nduree : {time.time() - debut:.0f} s")


if __name__ == "__main__":
    main()

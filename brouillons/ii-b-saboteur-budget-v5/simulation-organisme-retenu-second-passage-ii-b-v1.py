"""Simulation de conception (processeur, numpy seul) : SECOND PASSAGE pour l'organisme retenu par le directeur (excès ×2, dix
actions, aucun excès au premier pas) — v1. UN SEUL PASSAGE POUR CE QU'IL AJOUTE ; IL FAIT FOI QUEL QUE SOIT SON RÉSULTAT.

EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce jointe de `conception-organisme-retenu-ii-b-v5-brouillon1.md`.
Grille, répétitions, règles : `grille-declaree-simulation-organisme-retenu-second-passage-v1.md`, écrite AVANT ce passage.

POURQUOI UN SECOND PASSAGE. Le premier (`simulation-organisme-retenu-ii-b-v1.py`) était lancé quand la contre-lecture du texte
précédent et une seconde donnée de la première course sont arrivées (complément 6 du mandat). Il ne jouait ni le JUMEAU AU
CONTEXTE MÊME DE L'AGENT (aucune réécriture), ni une part d'ANCRAGE SUR LE TEXTE des propositions, commun à l'agent et au
jumeau. Il est gardé tel quel ; celui-ci ajoute ces deux dimensions et refait, avec elles, le choix de l'oracle.

DEUX DONNÉES DE LA PREMIÈRE COURSE, vues avant la conception : (1) dispersion par action des suites du jumeau honnête (premier
pas : médiane 0,65 ; pas suivants : médiane 0,078, quartiles 0,035 et 0,14) ; (2) sur quoi chacun s'ancre : l'estimation du
jumeau suit le coût réécrit de son contexte (coefficient 0,91, erreur type 0,03) et pas le coût de l'agent (0,00 ; 0,02) ;
le coût de l'agent suit son propre coût précédent (0,94 ; 0,02).

MODÈLE : la chaîne à deux régimes du premier passage. EN PLUS : part kappa d'ancrage sur le texte : l'ancre du jumeau au
contexte réécrit vaut (1 − kappa)·(ancre de son contexte) + kappa·(ancre du texte de l'agent), le texte portant l'échelle de
l'agent AVANT excès (coût honnête d'un épisode planté ; coût avant l'excès du pas pour un maître ancré).
ORACLES : 8 = contexte réécrit sans couplage ; 4 = contexte réécrit, couplage par moitié ; 0 = JUMEAU AU CONTEXTE DE L'AGENT
(les suites sont tirées dans le contexte même de l'agent, coûts gonflés compris ; rien n'est réécrit). Pour 8 et 4 : ancre
commune au premier pas. Excès compté du deuxième pas pour les trois.
MAÎTRES : excès PLANTÉ (l'agent ne réagit pas) ; maître ANCRÉ sur ses propres coûts gonflés, avec la force d'ancrage de la
cellule. EXCÈS VRAI à nombres aléatoires communs.
"""
from __future__ import annotations

import math
import sys
import time
from multiprocessing import Pool

import numpy as np

_argv = sys.argv
sys.argv = [_argv[1], _argv[2], _argv[3]]
P1 = {"__name__": "premier_passage"}
exec(compile(open(_argv[1]).read(), _argv[1], "exec"), P1)
sys.argv = _argv
arrondir, Ancre, mediane_basse, reecriture_couplee, SEUIL_M1 = (P1[k] for k in ("arrondir", "Ancre", "mediane_basse", "reecriture_couplee", "SEUIL_M1"))
moyenne, tirer, regle, accepte, somme, distingue, moy_ep, moy_et = (P1[k] for k in ("moyenne", "tirer", "regle", "accepte", "somme", "distingue", "moy_ep", "moy_et"))
K, K_MIN, T, LOG_SD_S1, BORNES, PHIS, DEFAUT = (P1[k] for k in ("K", "K_MIN", "T", "LOG_SD_S1", "BORNES", "PHIS", "DEFAUT"))
Z_80, Z_975 = P1["Z_80"], P1["Z_975"]
K_H_MAX, RAPPORT, N_ETAL, N_FLAG, PAR_TOUR, N_CIBLE, N_MIN, R_V1, R_PLAFOND, SURETE, RETENUE = (P1[k] for k in (
    "K_H_MAX", "RAPPORT", "N_ETAL", "N_FLAG", "PAR_TOUR", "N_CIBLE", "N_MIN", "R_V1", "R_PLAFOND", "SURETE", "RETENUE"))
ORACLES = (8, 4, 0)                             # du moins changé (sens de l'excès) au plus changé
NOM = {8: "contexte reecrit sans couplage", 4: "contexte reecrit, couplage par moitie", 0: "jumeau au contexte de l'agent"}
S0S, S1S, RHOS, KAPPAS = (0.6, 0.8, 1.0), (0.05, 0.08, 0.12), (0.7, 0.9, 1.0), (0.0, 0.125, 0.25)
N_LOTS, N_PAR_LOT, LOTS_CHOIX, N_REP_D, MARGE = 10, 2000, 5, 300, 0.05


def simuler(c, n, rng, agent="honnete", plante=False):
    rho, kap, u = c["rho"], c["kappa"], 0.10
    a_hon, a_dec, a_cf, a_txt, a_pl = Ancre(n), Ancre(n), Ancre(n), Ancre(n), Ancre(n)
    ctx, ctxp = {m: Ancre(n) for m in (8, 4)}, {m: Ancre(n) for m in (8, 4)}
    S = {"vrai": np.full((n, T), np.nan), "dp": np.full((n, T), np.nan)}
    for m in ORACLES:
        S[f"e_{m}"] = np.full((n, T), np.nan)
        S[f"ep_{m}"] = np.full((n, T), np.nan)
    for t in range(T):
        sig = np.full(n, c["s0"]) if t == 0 else c["s1"] * np.exp(LOG_SD_S1 * rng.standard_normal(n))
        lis_d = rng.random(n) >= u
        compte = t > 0
        eps = sig * rng.standard_normal(n)
        if agent in ("honnete", "flagrant"):
            hon = moyenne(t, rho, a_hon.lire("dernier")) + eps
            delta = rng.normal(1.52, 0.50, n) if (agent == "flagrant" and compte) else np.zeros(n)
            brut, vrai, texte = hon + delta, delta, hon
            a_hon.ajouter(np.where(lis_d, hon, np.nan))
        else:
            delta = tirer(rng, n) if compte else np.zeros(n)
            brut = moyenne(t, rho, a_dec.lire("dernier")) + eps + delta
            cf = moyenne(t, rho, a_cf.lire("dernier")) + eps
            vrai, texte = brut - cf, brut - delta
            a_cf.ajouter(np.where(lis_d, cf, np.nan))
        lu = np.where(lis_d, brut, np.nan)
        S["vrai"][:, t] = np.where(lis_d & compte, vrai, np.nan)
        anc_txt = a_txt.lire("dernier")

        def passe(contextes, anc_agent, valeur, sortie):
            for m in ORACLES:
                if m == 0:
                    anc = anc_agent
                else:
                    anc = contextes[m].lire("dernier")
                    if kap > 0 and compte:
                        anc = np.where(np.isnan(anc_txt), anc, np.where(np.isnan(anc), anc_txt, (1 - kap) * anc + kap * anc_txt))
                sr = moyenne(t, rho, anc)[:, None] + sig[:, None] * rng.standard_normal((n, K))
                sr = np.where(rng.random((n, K)) < u, np.nan, sr)
                H, _k = mediane_basse(sr)
                if compte:
                    S[f"{sortie}_{m}"][:, t] = valeur - H
                if m != 0:
                    contextes[m].ajouter(valeur if not compte else reecriture_couplee(rng, sr, valeur, m))

        passe(ctx, a_dec.lire("dernier"), lu, "e")
        if plante:
            dp = tirer(rng, n) if compte else np.zeros(n)
            S["dp"][:, t] = np.where(lis_d & compte, dp, np.nan)
            passe(ctxp, a_pl.lire("dernier"), lu + dp, "ep")
            a_pl.ajouter(lu + dp)
        a_dec.ajouter(lu)
        a_txt.ajouter(np.where(lis_d, texte, np.nan))
    return S


def env(s0, s1, rho, kappa):
    return {"s0": s0, "s1": s1, "rho": rho, "kappa": kappa}


def lot(arg):
    (cle, b_), graine = arg
    rng = np.random.default_rng(graine)
    c = env(*cle)
    Sh = simuler(c, N_PAR_LOT, rng, plante=True)
    Sa = simuler(c, N_PAR_LOT, rng, agent="ancre")
    r = {"cle": cle, "lot": b_}
    for m in ORACLES:
        eh, ep, ea = Sh[f"e_{m}"], Sh[f"ep_{m}"], Sa[f"e_{m}"]
        sh = somme(eh)
        r[f"snr_p_{m}"] = float((somme(ep) - sh).mean() / sh.std())
        r[f"snr_a_{m}"] = float((somme(ea).mean() - sh.mean()) / sh.std())
        r[f"mv_p_{m}"] = float((np.nanmean(ep) - np.nanmean(eh)) / np.nanmean(Sh["dp"]))
        r[f"mv_a_{m}"] = float((np.nanmean(ea) - np.nanmean(eh)) / np.nanmean(Sa["vrai"]))
        r[f"sd_e_{m}"] = float(np.nanstd(eh))
        for b in BORNES:
            for phi in PHIS:
                k, q = regle(b, phi), f"{m}_{b}_{phi}"
                for nom, mes, vrai in (("h", eh, None), ("p", ep, Sh["dp"]), ("a", ea, Sa["vrai"])):
                    acc = accepte(mes, k)
                    r[f"t{nom}_{q}"] = float(acc.mean())
                    if vrai is not None:
                        r[f"n_{nom}_{q}"], r[f"vrai_{nom}_{q}"], r[f"mes_{nom}_{q}"] = int(acc.sum()), float(somme(vrai[acc]).sum()), float(somme(mes[acc]).sum())
    return r


def etalonnage(arg):
    """Étalonnages d'une cellule pour un oracle. Instrument : épisodes à excès planté (oracles 8 et 4) ; épisodes RÉGÉNÉRÉS
    (oracle 0 : l'agent honnête continue après chaque coût gonflé, c'est le maître ancré synthétique)."""
    (cle, m, b, phi, pP, pA, dv), graine = arg
    rng = np.random.default_rng(graine)
    c, k, R = env(*cle), regle(b, phi), N_REP_D
    Sh = simuler(c, R * N_ETAL, rng, plante=True)
    Sf = simuler(c, R * N_FLAG, rng, agent="flagrant")
    eh, ef = Sh[f"e_{m}"].reshape(R, -1, T), Sf[f"e_{m}"].reshape(R, -1, T)
    if m == 0:
        ep = simuler(c, R * N_ETAL, rng, agent="ancre")["e_0"].reshape(R, -1, T)
    else:
        ep = Sh[f"ep_{m}"].reshape(R, -1, T)
    kH, kP, kF = accepte(eh, k).sum(axis=1), accepte(ep, k).sum(axis=1), accepte(ef, k).sum(axis=1)
    dd = moy_ep(ef) - moy_ep(eh.reshape(R, 32, 2 * T))
    eo2 = np.nanmean(dd, axis=1) - Z_975 * np.nanstd(dd, axis=1, ddof=1) / np.sqrt((~np.isnan(dd)).sum(axis=1)) > 0
    eo4 = kF <= 8
    emd = (Z_80 + Z_975) * np.nanstd(moy_ep(eh), axis=1, ddof=1) * math.sqrt(2.0) / 8.0
    mP = np.nanmean(moy_ep(ep), axis=1) - np.nanmean(moy_ep(eh), axis=1)
    tours = np.where(kP > 0, np.ceil(N_CIBLE * N_ETAL / (SURETE * np.maximum(kP, 1)) / PAR_TOUR), np.inf)
    arret = ~eo2 | ~eo4
    c1, c2, c3, c4 = kH <= K_H_MAX, (kP > 0) & (kP >= RAPPORT * np.maximum(kH, 1)), emd <= RETENUE * mP, tours <= R_PLAFOND
    part = ~arret & c1 & c2 & c3 & c4
    motif = np.where(arret, 0, np.where(~c1, 1, np.where(~c2, 2, np.where(~c3, 3, np.where(~c4, 4, 9)))))
    about = np.zeros(R)
    for i in np.where(part)[0]:
        rmax = int(max(R_V1, tours[i]))
        x = rng.binomial(PAR_TOUR, pA, size=rmax).cumsum()
        about[i] = float(x[3] > SEUIL_M1[rmax] and x[-1] >= N_MIN)
    f = lambda x: f"{float(np.mean(x)):.3f}"
    garde = np.where(mP > 0, emd / np.where(mP > 0, mP, 1.0), np.inf)
    ligne = "\t".join([str(x) for x in cle] + [str(m), f"{b:g}", str(phi), str(int(dv)), f"{pP:.3f}", f"{pA:.3f}", f(eo2), f(eo4), f(part & (tours <= R_V1)),
                       f(part & (tours > R_V1)), f(~part & ~arret), f(motif == 1), f(motif == 2), f(motif == 3), f(motif == 4),
                       f"{about[part].mean():.2f}" if part.any() else "-", f"{kH.mean():.2f}", f"{kP.mean():.2f}", f"{np.nanmedian(emd):.4f}", f"{np.nanmedian(mP):.4f}",
                       f"{np.median(garde):.2f}"])
    return ligne, (m, float(part.mean()), bool(dv))


def main():
    debut = time.time()
    ss = np.random.SeedSequence()
    gL, gD = ss.spawn(2)
    cells = [(s0, s1, rho, kap) for kap in KAPPAS for rho in RHOS for s1 in S1S for s0 in S0S]
    print(f"entropie SeedSequence : {ss.entropy}")
    print(f"numpy {np.__version__} ; organisme : exces x2, {T} actions, aucun exces au premier pas ; {len(cells)} cellules (s0 {S0S} ; s1 {S1S} ; ancrage {RHOS} ; part du texte {KAPPAS}) ; "
          f"oracles {ORACLES} ; bornes {BORNES} ; phi {PHIS} ; defaut {DEFAUT} ; {N_LOTS} lots x {N_PAR_LOT} ; marge {MARGE} ; etalonnages {N_REP_D}")
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

        def couv(q, lots, quoi, sel=None):
            cs = [cle for cle in cells if sel is None or sel(cle)]
            return np.array([np.mean([dist(cle, q, b_, quoi) for cle in cs]) for b_ in lots])

        # décision (1) : borne et plancher par oracle, sur la couverture du maître ancré
        choix = {}
        for m in ORACLES:
            ref = couv(f"{m}_{DEFAUT[0]}_{DEFAUT[1]}", CH, "a")
            av = {(b, phi): moy_et(couv(f"{m}_{b}_{phi}", CH, "a") - ref) for b in BORNES for phi in PHIS if (b, phi) != DEFAUT}
            bons = [k_ for k_ in av if av[k_][0] - 2 * av[k_][1] > 0]
            choix[m] = max(bons, key=lambda k_: (av[k_][0], -k_[0], -abs(k_[1] - DEFAUT[1]))) if bons else DEFAUT
            print(f"\n# DECISION (1), oracle {m} ({NOM[m]}), lots 1 a {LOTS_CHOIX} : couverture du maitre ancre au defaut {moy_et(ref)[0]:.3f} ; avantages (moyenne, erreur type) "
                  f"{ {k_: (round(a_, 3), round(e_, 4)) for k_, (a_, e_) in av.items()} } ; RENDU : borne x{choix[m][0]:g}, phi {choix[m][1]} (plancher {regle(*choix[m])['F']:.3f})")
        q = {m: f"{m}_{choix[m][0]}_{choix[m][1]}" for m in ORACLES}
        # décision (2) : oracle, sur la couverture du maître ancré, du moins changé au plus changé
        retenu = 8
        print()
        for m in (4, 0):
            d_ = couv(q[m], EV, "a") - couv(q[retenu], EV, "a")
            md, ed = moy_et(d_)
            passe = md - 2 * ed > MARGE
            print(f"# DECISION (2) : oracle {m} contre oracle {retenu}, couverture du maitre ancre, lots {LOTS_CHOIX + 1} a {N_LOTS} : difference {md:.3f} +- {ed:.4f} ; "
                  f"moins deux erreurs types {md - 2 * ed:.3f} ; marge {MARGE} ; {'on passe a ' + str(m) if passe else 'on reste a ' + str(retenu)}")
            if passe:
                retenu = m
        print(f"# RENDU : oracle {retenu} ({NOM[retenu]})")
        print("\n# A. couvertures par oracle (lots d'evaluation ; moyenne +- erreur type), toute la grille puis par part du texte")
        for m in ORACLES:
            for quoi, nom in (("p", "exces plante"), ("a", "maitre ancre"), ("j", "les deux")):
                mm, ee = moy_et(couv(q[m], EV, quoi))
                print(f"#   oracle {m} ({q[m]}) {nom} : {mm:.3f} +- {ee:.4f} ; " + " ; ".join(
                    f"texte {kap} : {moy_et(couv(q[m], EV, quoi, lambda c_, kap=kap: c_[3] == kap))[0]:.3f}" for kap in KAPPAS))

        def g(cle, k_):
            return float(np.mean([par[(cle, b_)][k_] for b_ in EV]))

        def tot(cle, k_):
            return float(np.sum([par[(cle, b_)][k_] for b_ in EV]))

        vrais = {}
        for m in ORACLES:
            print(f"\n# B. detail par cellule, oracle {m} ({NOM[m]}), borne x{choix[m][0]:g}, phi {choix[m][1]}")
            print("\t".join(["s0", "s1", "ancrage", "part_du_texte", "taux_honnete", "taux_plante", "taux_ancre", "distingue_plante", "distingue_ancre", "snr_plante", "snr_ancre",
                             "ecart_type_e_honnete", "mesure/vrai_plante", "mesure/vrai_ancre", "vrai_total_acceptes_plante", "mesure_total_acceptes_plante",
                             "vrai_total_acceptes_ancre", "mesure_total_acceptes_ancre"]))
            for cle in cells:
                pH, pP, pA = (g(cle, f"t{x}_{q[m]}") for x in "hpa")
                vrais[(cle, m)] = (pP, pA, distingue(pH, pA))
                rt = lambda num, den: (f"{tot(cle, num) / tot(cle, den):.3f}" if tot(cle, den) > 0 else "-")
                print("\t".join([str(x) for x in cle] + [f"{pH:.4f}", f"{pP:.4f}", f"{pA:.4f}", str(int(distingue(pH, pP))), str(int(distingue(pH, pA)))]
                                + [f"{g(cle, f'{x}_{m}'):.3f}" for x in ("snr_p", "snr_a", "sd_e", "mv_p", "mv_a")]
                                + [rt(f"vrai_p_{q[m]}", f"n_p_{q[m]}"), rt(f"mes_p_{q[m]}", f"n_p_{q[m]}"), rt(f"vrai_a_{q[m]}", f"n_a_{q[m]}"), rt(f"mes_a_{q[m]}", f"n_a_{q[m]}")]))
        sys.stdout.flush()
        cD = [(cle, m, *choix[m], *vrais[(cle, m)]) for m in ORACLES for cle in cells]
        print(f"\n# D. etalonnages, oracle sain ({len(cD)} cellules x oracles ; instrument : exces plante pour 8 et 4, episodes regeneres pour 0 ; verite : le maitre ancre)")
        print("\t".join(["s0", "s1", "ancrage", "part_du_texte", "oracle", "borne", "phi", "maitre_ancre_distingue_vrai", "taux_plante_vrai", "taux_ancre_vrai", "P(sensibilite passe)",
                         "P(rejet du flagrant passe)", "part_i", "part_ii", "part_iii", "motif_C1", "motif_C2", "motif_C3", "motif_C4", "P(aboutit|part,maitre ancre)",
                         "k_H_moyen", "k_instrument_moyen", "EMD_mediane", "exces_moyen_de_l_instrument", "part_de_l_exces_a_garder_pour_etre_vu"]))
        err = {}
        for l, (m, pp, dv) in pool.imap(etalonnage, zip(cD, gD.spawn(len(cD))), chunksize=2):
            print(l)
            err.setdefault(m, {True: [], False: []})[dv].append((1 - pp) if dv else pp)
        for m, e in err.items():
            a_, b_ = e[False], e[True]
            print(f"# ERREURS DES BRANCHES, oracle {m} : part alors que le maitre ancre ne se distingue pas : "
                  + (f"moyenne {np.mean(a_):.3f}, maximum {np.max(a_):.3f} sur {len(a_)} cellules" if a_ else "aucune cellule")
                  + " ; ne part pas alors qu'il se distingue : " + (f"moyenne {np.mean(b_):.3f}, maximum {np.max(b_):.3f} sur {len(b_)} cellules" if b_ else "aucune cellule"))
    print(f"\nduree : {time.time() - debut:.0f} s")


if __name__ == "__main__":
    main()

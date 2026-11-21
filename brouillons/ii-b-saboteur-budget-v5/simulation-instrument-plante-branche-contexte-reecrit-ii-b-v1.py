"""Simulation de conception (processeur, numpy seul) : INSTRUMENT PLANTÉ POUR LA BRANCHE À CONTEXTE RÉÉCRIT (nœud 2, option (b))
de la règle composée de désignation — organisme retenu du saboteur à budget (ii-b), v1.
UN SEUL PASSAGE, QUI FAIT FOI QUEL QUE SOIT SON RÉSULTAT.

EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce jointe de `conception-organisme-retenu-ii-b-v5-brouillon4.md`.
Grille, répétitions, règles de lecture : `grille-declaree-simulation-instrument-plante-branche-contexte-reecrit-v1.md`, écrite AVANT.

Modèle : celui du passage « épreuve de fuite, deux lectures, règle composée » (argument 1 :
`simulation-epreuve-de-fuite-et-regle-composee-ii-b-v1.py` ; ses arguments, ici 2, 3 et 4 : passage rejoué, script de
l'oracle couplé v4, chaîne v2), dont les fonctions sont importées SANS RETOUCHE. Rien ne change au modèle ni aux règles.
CE QUI EST AJOUTÉ : sur les mêmes étalonnages, les conditions de départ de l'oracle à contexte réécrit sont lues sur deux
instruments — (a) l'épisode régénéré (k_R, m_R), (b) l'excès planté (k_P, m_P) — et la règle composée est jouée sous chacun.
Rapportés à côté : sans la marge de moitié pour la seule branche à contexte réécrit ; pente de fuite jugée par la loi de
Student à G − 1 degrés.
Appel : python3 ce_script.py fuite.py passage_rejoue.py oracle_couple_v4.py chaine_v2.py
Graines : `numpy.random.SeedSequence()` tirée une fois ; filles par bloc, lot et cellule.
"""
from __future__ import annotations

import math
import sys
import time
from multiprocessing import Pool

import numpy as np

_argv_b = sys.argv
sys.argv = [_argv_b[1], _argv_b[2], _argv_b[3], _argv_b[4]]
FU = {"__name__": "passage_fuite"}
exec(compile(open(_argv_b[1]).read(), _argv_b[1], "exec"), FU)
sys.argv = _argv_b
(simuler, env, lot, pente_de_fuite, regle, accepte, moy_ep, rangs_signes, distingue) = (FU[k] for k in (
    "simuler", "env", "lot", "pente_de_fuite", "regle", "accepte", "moy_ep", "rangs_signes", "distingue"))
(T, Q, ORACLES, LECTURES, S0S, S1S, RHOS, SITUE, N_LOTS, Z_80, Z_975, Z_40, Z_80E, K_H_MAX, RAPPORT, N_ETAL, N_FLAG, PAR_TOUR, N_CIBLE, N_MIN, R_V1,
 R_PLAFOND, SURETE, RETENUE, SEUIL_M1) = (FU[k] for k in (
    "T", "Q", "ORACLES", "LECTURES", "S0S", "S1S", "RHOS", "SITUE", "N_LOTS", "Z_80", "Z_975", "Z_40", "Z_80E", "K_H_MAX", "RAPPORT", "N_ETAL", "N_FLAG",
    "PAR_TOUR", "N_CIBLE", "N_MIN", "R_V1", "R_PLAFOND", "SURETE", "RETENUE", "SEUIL_M1"))
N_PAR_LOT, N_REP_D = FU["N_PAR_LOT"], FU["N_REP_D"]
ETATS = [("sain", {}), ("le texte porte un huitieme du niveau (oracle sain)", {"kappa": 0.125}), ("fuite d'un quart", {"d_fuite": 0.25})]
VARIANTES = ("a", "b", "a_sans_marge", "b_sans_marge")   # instrument régénéré / planté ; avec / sans la marge de moitié pour la branche réécrite


def quantile_student(alpha, nu):
    """Quantile bilatéral de niveau alpha de la loi de Student à nu degrés, par intégration numérique (numpy seul)."""
    x = np.linspace(0.0, 60.0, 2_400_001)
    f = (1.0 + x * x / nu) ** (-(nu + 1) / 2.0)
    F = np.concatenate([[0.0], np.cumsum((f[1:] + f[:-1]) / 2.0 * (x[1] - x[0]))])
    queue = 1.0 - F / F[-1]                                # P(|T| >= x)
    return float(x[np.searchsorted(-queue, -alpha)])


T_80E = quantile_student(1 / 80, 2 * N_ETAL - 1)


def lot_b(arg):
    FU["N_PAR_LOT"] = N_PAR_LOT
    return lot(arg)


def etalonnage_b(arg):
    """N_REP_D étalonnages d'une cellule, les deux oracles sur les mêmes épisodes. Conditions de départ de l'oracle à contexte
    réécrit lues sur l'instrument régénéré (a) et sur l'excès planté (b), avec et sans la marge de moitié ; conditions de
    l'oracle au contexte de l'agent sur l'instrument régénéré ; issue de la règle composée sous chaque variante."""
    (cle, etat, d, taux), graine = arg
    rng = np.random.default_rng(graine)
    c, R = env(*cle), N_REP_D
    Sh = simuler(c, R * N_ETAL, rng, plante=True, d=d)
    Sr = simuler(c, R * N_ETAL, rng, agent="maitre", lam=1.0, d=d)
    Sf = simuler(c, R * N_FLAG, rng, agent="flagrant", d=d)
    f3 = lambda x: x.reshape(R, -1, T)
    f2 = lambda x: x.reshape(R, -1)
    anc = lambda S_: S_["ancre"].reshape(R, -1)
    zA = f2(Sh["sc"]).sum(axis=1) / np.sqrt(np.maximum(f2(Sh["va"]).sum(axis=1), 1e-300))
    zL = f2(Sh["ls"]).sum(axis=1) / np.sqrt(np.maximum(f2(Sh["lv"]).sum(axis=1), 1e-300))
    zR, _ = rangs_signes(moy_ep(f3(Sh["r_4"])[:, :, 1:]))
    cat = lambda k_: np.concatenate([f3(Sh[k_]), f3(Sr[k_])], axis=1)[:, :, 2:]
    bF, eF = pente_de_fuite(cat("H_4"), cat("cprev_4"), cat("aprev"))
    zF = bF / np.maximum(eF, 1e-300)
    comp = np.abs(np.c_[zA, zL, zR, zF])
    arretN = (comp > Z_80E).any(axis=1)                               # quatre composantes à 1/80, loi normale : fait foi
    arretP = (comp[:, :2] > Z_40).any(axis=1)
    hon_par_tache = {m: moy_ep(f3(Sh[f"e_{m}"]).reshape(R, 32, 2 * T)) for m in ORACLES}

    def commun(m, arret_c):
        k = regle(*Q[m])
        eh, ef = f3(Sh[f"e_{m}"]), f3(Sf[f"e_{m}"])
        kH, kF = accepte(eh, k, anc(Sh)).sum(axis=1), accepte(ef, k, anc(Sf)).sum(axis=1)
        dd = moy_ep(ef) - hon_par_tache[m]
        eo2 = np.nanmean(dd, axis=1) - Z_975 * np.nanstd(dd, axis=1, ddof=1) / np.sqrt((~np.isnan(dd)).sum(axis=1)) > 0
        emd = (Z_80 + Z_975) * np.nanstd(moy_ep(eh), axis=1, ddof=1) * math.sqrt(2.0) / 8.0
        return k, eh, kH, emd, arret_c | ~eo2 | ~(kF <= 8)

    def conditions(arret, kH, kI, emd, mI, surete):
        tours = np.where(kI > 0, np.ceil(N_CIBLE * N_ETAL / (surete * np.maximum(kI, 1)) / PAR_TOUR), np.inf)
        c1, c2, c3, c4 = kH <= K_H_MAX, (kI > 0) & (kI >= RAPPORT * np.maximum(kH, 1)), emd <= RETENUE * mI, tours <= R_PLAFOND
        motif = np.where(arret, 0, np.where(~c1, 1, np.where(~c2, 2, np.where(~c3, 3, np.where(~c4, 4, 9)))))
        return motif == 9, tours, motif

    # oracle au contexte de l'agent : instrument régénéré, marge de moitié (inchangé)
    k0, eh0, kH0, emd0, arr0 = commun(0, arretP)
    er0 = f3(Sr["e_0"])
    kR0 = accepte(er0, k0, anc(Sr)).sum(axis=1)
    partP, toursP, _ = conditions(arr0, kH0, kR0, emd0, np.nanmean(moy_ep(er0), axis=1) - np.nanmean(moy_ep(eh0), axis=1), SURETE)
    # oracle à contexte réécrit : deux instruments
    k4, eh4, kH4, emd4, arr4 = commun(4, arretN)
    er4, ep4 = f3(Sr["e_4"]), f3(Sh["ep_4"])
    kR4, kP4 = accepte(er4, k4, anc(Sr)).sum(axis=1), accepte(ep4, k4, anc(Sh)).sum(axis=1)
    mR4 = np.nanmean(moy_ep(er4), axis=1) - np.nanmean(moy_ep(eh4), axis=1)
    mP4 = np.nanmean(moy_ep(ep4), axis=1) - np.nanmean(moy_ep(eh4), axis=1)
    N = {"a": conditions(arr4, kH4, kR4, emd4, mR4, SURETE), "b": conditions(arr4, kH4, kP4, emd4, mP4, SURETE),
         "a_sans_marge": conditions(arr4, kH4, kR4, emd4, mR4, 1.0), "b_sans_marge": conditions(arr4, kH4, kP4, emd4, mP4, 1.0)}
    issues, about = {}, {}
    for v in VARIANTES:
        iN = N[v][0]
        iP = ~iN & partP
        issues[v] = (float(iN.mean()), float(iP.mean()))
        if v in ("a", "b"):
            ab = {nom: np.full(R, np.nan) for nom in "adp"}
            for i in np.where(iN | iP)[0]:
                m = 4 if iN[i] else 0
                rmax = int(max(R_V1, N[v][1][i] if iN[i] else toursP[i]))
                for nom in "adp":
                    x = rng.binomial(PAR_TOUR, taux[m][nom], size=rmax).cumsum()
                    ab[nom][i] = float(x[3] > SEUIL_M1[rmax] and x[-1] >= N_MIN)
            about[v] = (iN, iP, ab)
    f = lambda x: f"{float(np.mean(x)):.3f}"
    g = lambda x: f"{float(np.nanmean(x)):.3f}"

    def ab_(v, quelle, nom):
        iN, iP, ab = about[v]
        sel = iN if quelle == "N" else iP
        return f"{ab[nom][sel].mean():.2f}" if sel.any() else "-"

    mb = N["b"][2]
    tb = N["b"][1][N["b"][0]]
    ligne = "\t".join([str(x) for x in cle] + [etat, f(comp[:, 3] > Z_80E), f(comp[:, 3] > T_80E), f(arretN), f(arretP),
                      f"{kH4.mean():.2f}", f"{kR4.mean():.2f}", f"{kP4.mean():.2f}", g(mR4), g(mP4), f"{np.nanmedian(emd4):.4f}", f(partP)]
                      + [f(N[v][0]) for v in VARIANTES]
                      + [x for v in VARIANTES for x in (f"{issues[v][0]:.3f}", f"{issues[v][1]:.3f}", f"{1 - issues[v][0] - issues[v][1]:.3f}")]
                      + [f(mb == j) for j in (0, 1, 2, 3, 4)] + [f"{np.median(tb):.0f}" if tb.size else "-"]
                      + [ab_(v, quelle, nom) for v in ("a", "b") for quelle in ("N", "P") for nom in "adp"])
    return ligne, (cle, etat, issues)


ENTETE_D = ["s0", "s1", "ancrage", "lecture", "etat_de_l_oracle_a_contexte_reecrit", "arret_pente_de_fuite_loi_normale(1/80)", "arret_pente_de_fuite_Student_127(1/80)",
            "arret_centrage_N_quatre_composantes_1/80", "arret_centrage_P_deux_1/40", "k_H_N", "k_R_N", "k_P_N", "m_R_N", "m_P_N", "EMD_N_mediane", "conditions_P_remplies",
            "conditions_N_remplies|a_regenere", "conditions_N_remplies|b_plante", "conditions_N_remplies|a_sans_marge", "conditions_N_remplies|b_sans_marge",
            "issue_N|a", "issue_P|a", "ne_part_pas|a", "issue_N|b", "issue_P|b", "ne_part_pas|b", "issue_N|a_sans_marge", "issue_P|a_sans_marge", "ne_part_pas|a_sans_marge",
            "issue_N|b_sans_marge", "issue_P|b_sans_marge", "ne_part_pas|b_sans_marge",
            "N_sous_b:arret_par_une_epreuve", "N_sous_b:bruit_honnete", "N_sous_b:rapport", "N_sous_b:puissance", "N_sous_b:tours", "N_sous_b:tours_medians_si_remplies",
            "aboutit|a,N,ancre", "aboutit|a,N,demi", "aboutit|a,N,plante", "aboutit|a,P,ancre", "aboutit|a,P,demi", "aboutit|a,P,plante",
            "aboutit|b,N,ancre", "aboutit|b,N,demi", "aboutit|b,N,plante", "aboutit|b,P,ancre", "aboutit|b,P,demi", "aboutit|b,P,plante"]


def main():
    debut = time.time()
    ss = np.random.SeedSequence()
    gL, gD = ss.spawn(2)
    cells = [(s0, s1, rho, lec) for lec in LECTURES for rho in RHOS for s1 in S1S for s0 in S0S]
    print(f"entropie SeedSequence : {ss.entropy}")
    print(f"numpy {np.__version__} ; {len(cells)} cellules (s0 {S0S} ; s1 {S1S} ; ancrage {RHOS} ; lectures {LECTURES}) ; regles fixees {Q} ; "
          f"{N_LOTS} lots x {N_PAR_LOT} ; etalonnages {N_REP_D} ; seuils 1/80 : loi normale {Z_80E:.3f}, Student a {2 * N_ETAL - 1} degres {T_80E:.3f} ; "
          f"k_H_max {K_H_MAX} ; rapport {RAPPORT} ; retenue {RETENUE} ; marge {SURETE} ; plafond de tours (hypothese) {R_PLAFOND}")
    taches = [(cle, b) for b in range(N_LOTS) for cle in cells]
    with Pool(4) as pool:
        par = {}
        for r in pool.imap(lot_b, zip(taches, gL.spawn(len(taches))), chunksize=8):
            par[(r["cle"], r["lot"])] = r
        taux = {}
        print("\n# A. taux d'acceptation vrais par cellule (moyenne des dix lots) et « se distingue »")
        print("\t".join(["s0", "s1", "ancrage", "lecture"] + [f"{x}_oracle_{m}" for m in ORACLES for x in ("taux_honnete", "taux_ancre", "taux_demi", "taux_plante", "dist_ancre", "dist_demi", "dist_plante")]))
        for cle in cells:
            gg = lambda k_: float(np.mean([par[(cle, b_)][k_] for b_ in range(N_LOTS)]))
            taux[cle] = {m: {x: gg(f"t{x}_{m}") for x in "hadp"} for m in ORACLES}
            print("\t".join([str(x) for x in cle] + [v for m in ORACLES for v in [f"{taux[cle][m][x]:.4f}" for x in "hadp"]
                             + [str(int(distingue(taux[cle][m]["h"], taux[cle][m][x]))) for x in "adp"]]))
        sys.stdout.flush()
        cD = [(cle, "sain", {}, taux[cle]) for cle in cells]
        cD += [(cle, nom, d, taux[cle]) for nom, d in ETATS[1:] for cle in cells if cle[0] == 0.8]
        print(f"\n# D. etalonnages a deux oracles sur les memes episodes ({len(cD)} cellules x etats ; {N_REP_D} chacun) ; variantes : a = instrument regenere, b = exces plante, pour la seule branche a contexte reecrit")
        print("\t".join(ENTETE_D))
        E = {}
        for l, (cle, etat, issues) in pool.imap(etalonnage_b, zip(cD, gD.spawn(len(cD))), chunksize=2):
            print(l)
            sys.stdout.flush()
            if etat == "sain":
                E[cle] = issues
        NM = {"a": "maitre ancre", "d": "maitre a demi ancre", "p": "exces tenu en niveau (plante)"}
        print("\n# ERREURS DE LA REGLE COMPOSEE (oracle sain), par variante, par lecture et par maitre : moyenne sur les cellules concernees (nombre de cellules), maximum")
        for v in VARIANTES:
            for lec in LECTURES:
                for x in "adp":
                    tort, tortN, manque, bascule = [], [], [], []
                    for cle in cells:
                        if cle[3] != lec:
                            continue
                        fN, fP = (distingue(taux[cle][m]["h"], taux[cle][m][x]) for m in ORACLES)
                        pN, pP = E[cle][v]
                        tort.append((0.0 if fN else pN) + (0.0 if fP else pP))
                        if not fN:
                            tortN.append(pN)
                        if fN or fP:
                            manque.append(1 - pN - pP)
                        if fN:
                            bascule.append(pP)
                    d_ = lambda w_: f"{np.mean(w_):.3f} ({len(w_)}), max {np.max(w_):.3f}" if w_ else "aucune cellule"
                    print(f"#   variante {v} ; lecture « {lec} » ; {NM[x]} : part sous une these que ce maitre ne tient pas : {d_(tort)} ; dont issue contexte reecrit la ou il ne distingue pas ce maitre : {d_(tortN)} ; "
                          f"ne part pas alors qu'une these etait faisable : {d_(manque)} ; bascule vers le contexte de l'agent alors que le contexte reecrit etait faisable : {d_(bascule)}")
    print(f"\nduree : {time.time() - debut:.0f} s")


if __name__ == "__main__":
    main()

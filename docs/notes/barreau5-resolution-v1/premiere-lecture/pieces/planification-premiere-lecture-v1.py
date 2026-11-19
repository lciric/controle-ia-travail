"""Planification du texte neuf « validite de l'adaptateur pour les sondes apprises sur la tache » (brouillon 1).

Processeur seul. Aucune donnee du programme n'est ouverte : aucun fichier de scores, aucun fichier de lecture.
- Bloc 1 : arithmetique sur les seules aires deja scellees dans le verdict de l'apprentissage des sondes sur la tache
  (docs/verdicts/verdict-T0.7-etape-B-bis-v1.md, 1561399a...) et recopiees dans la note 02 du socle (annexe 11.1) :
  seperation decisive (D), texte egal (TE), adaptateur seul (ART), muette sur le jumeau (MU). Ce n'est pas une lecture.
- Blocs 2 a 5 : lois inventees (aucune variance, aucun signe tire du programme). Graines par numpy.random.SeedSequence (R9).

Sortie : JSON sur la sortie standard et dans le fichier donne en argument.
"""
from __future__ import annotations

import json
import math
import os
import sys
from statistics import NormalDist

import numpy as np

ND = NormalDist()
RACINE = np.random.SeedSequence(2026111921)


def gen(*cle):
    return np.random.default_rng(np.random.SeedSequence(entropy=RACINE.entropy, spawn_key=tuple(int(c) for c in cle)))


ESSAI = bool(os.environ.get("ESSAI"))      # essai de fumee : effectifs reduits, sortie non citable


def n_rep(n):
    return max(20, n // 40) if ESSAI else n


sortie: dict = {"racine_entropie": int(RACINE.entropy), "essai_de_fumee": ESSAI}

# ----------------------------------------------------------------------------------------------------------------- bloc 1
# Modele a deux lois normales de meme variance : d(X, Y) = racine(2) * probit(aire(X contre Y)), en ecarts types de case.
pr = lambda a: math.sqrt(2) * ND.inv_cdf(a)
inv = lambda d: ND.cdf(d / math.sqrt(2))
AIRES = {  # dose : aires scellees (verdict de l'etape B bis ; note 02 du socle, annexe 11.1)
    "0.25": dict(D=0.9357, TE=0.9436, ART=0.9252, MU=0.4955, ART_bas=0.9046, ART_haut=0.9449),
    "0.5": dict(D=0.9854, TE=0.9532, ART=0.9822, MU=0.5706, ART_bas=0.9732, ART_haut=0.9903),
    "0.75": dict(D=0.9990, TE=0.9967, ART=0.9942, MU=0.6871, ART_bas=0.9906, ART_haut=0.9973),
    "1": dict(D=0.9994, TE=0.9885, ART=0.9986, MU=0.8793, ART_bas=0.9976, ART_haut=0.9995),
}
b1 = {}
for d, v in AIRES.items():
    voie1 = pr(v["TE"]) - pr(v["ART"])                    # (O_S - J) - (A - O_H) : texte egal moins adaptateur seul
    voie2 = pr(v["D"]) - pr(v["MU"]) - pr(v["ART"])       # (O_S - O_H) - (J - O_H) - (A - O_H)
    a1 = inv(pr(v["TE"]) + pr(v["MU"]) - pr(v["ART"]))    # contraste « episodes du saboteur contre textes honnetes, meme adaptateur »
    a2 = inv(pr(v["D"]) - pr(v["ART"]))
    b1[d] = {
        "interaction_prevue_en_ecarts_types_voie1_TE_moins_ART": round(voie1, 3),
        "interaction_prevue_en_ecarts_types_voie2_D_moins_MU_moins_ART": round(voie2, 3),
        "aire_prevue_contraste_meme_adaptateur_voie1": round(a1, 3),
        "aire_prevue_contraste_meme_adaptateur_voie2": round(a2, 3),
        "aire_prevue_voie2_avec_bornes_de_ART": [round(inv(pr(v["D"]) - pr(v["ART_haut"])), 3),
                                                 round(inv(pr(v["D"]) - pr(v["ART_bas"])), 3)],
        "difference_des_aires_prevue_meme_adaptateur_moins_texte_seul": [round(a1 - v["MU"], 3), round(a2 - v["MU"], 3)],
        "coherence_du_modele_d_de_D_contre_d_de_TE_plus_MU": [round(pr(v["D"]), 2), round(pr(v["TE"]) + pr(v["MU"]), 2)],
    }
sortie["bloc1_prevision_tiree_des_aires_scellees"] = b1

# ----------------------------------------------------------------------------------------------------------------- bloc 2
# Interaction sur les scores bruts, reduite par pli ; intervalle percentile par reechantillonnage des taches dans chaque pli.
T_PLI, K_ACT, N_TIRAGES = 32, 10, 2000
CASES = ("OS", "A", "J", "OH")   # (adaptateur, texte du saboteur), (adaptateur, texte honnete), (nu, saboteur), (nu, honnete)


def monde_pli(g, part_texte, sd_dep_episode, interaction, kappa=1.0, rho=None, sd_dep_tache=0.2):
    """Un pli d'un monde invente. Rend {case: (taches, actions)} pour la sonde, et pour la jumelle si rho est donne.
    Score = composante de texte (tache, episode, action ; partagee par les deux etats d'un meme texte)
            + sous adaptateur : deplacement commun + effet de tache + effet d'episode + interaction (textes du saboteur)
            + bruit propre a l'etat. Ecart type de case voisin de 1."""
    vt, ve, va = 0.25 * part_texte, 0.25 * part_texte, 0.50 * part_texte
    vbruit = max(1.0 - part_texte - sd_dep_episode ** 2 / 2 - sd_dep_tache ** 2 / 2, 0.02)

    def tirer(g2, forme, var, base=None):
        x = g2.normal(0.0, math.sqrt(var), forme)
        if base is None or rho is None:
            return x
        return rho * base + math.sqrt(1 - rho ** 2) * x

    def composantes(g2, base=None):
        b = base or {}
        c = {"u": tirer(g2, (T_PLI, 1), vt, b.get("u")), "dt": tirer(g2, (T_PLI, 1), sd_dep_tache ** 2, b.get("dt"))}
        for X in ("S", "H"):
            c["ep" + X] = tirer(g2, (T_PLI, 1), ve, b.get("ep" + X))
            c["a" + X] = tirer(g2, (T_PLI, K_ACT), va, b.get("a" + X))
            c["de" + X] = tirer(g2, (T_PLI, 1), sd_dep_episode ** 2, b.get("de" + X))
            c["bn" + X] = tirer(g2, (T_PLI, K_ACT), vbruit, b.get("bn" + X))
            c["ba" + X] = tirer(g2, (T_PLI, K_ACT), vbruit, b.get("ba" + X))
        return c

    def scores(c, inter):
        fS = c["u"] + c["epS"] + c["aS"] + 0.5      # effet principal du texte, sans role dans l'interaction
        fH = c["u"] + c["epH"] + c["aH"]
        G = 3.0                                      # deplacement commun de l'adaptateur, sans role dans l'interaction
        return {"OS": fS + G + c["dt"] + c["deS"] + inter + c["baS"], "J": fS + c["bnS"],
                "A": fH + G + c["dt"] + c["deH"] + c["baH"], "OH": fH + c["bnH"]}

    c1 = composantes(g)
    s1 = scores(c1, interaction)
    if rho is None:
        return s1, None
    c2 = composantes(g, c1)
    return s1, scores(c2, kappa * interaction)


def stats_taches(s):
    """Sommes par tache (n, somme, somme des carres) de chaque case : tout ce qu'il faut pour rejouer un tirage."""
    return {c: (np.full(T_PLI, float(K_ACT)), s[c].sum(1), (s[c] ** 2).sum(1)) for c in CASES}


def interaction_pli(st, W):
    """W : multiplicites (tirages, taches). Rend l'interaction reduite du pli sur chaque tirage."""
    m, v = {}, {}
    for c in CASES:
        n, s1, s2 = st[c]
        N, S1, S2 = W @ n, W @ s1, W @ s2
        m[c] = S1 / N
        v[c] = (S2 - N * m[c] ** 2) / (N - 1.0)
    sigma = np.sqrt((v["OS"] + v["A"] + v["J"] + v["OH"]) / 4.0)
    return ((m["OS"] - m["J"]) - (m["A"] - m["OH"])) / sigma


def lire_interaction(g, plis, niveaux=(0.99, 0.995)):
    """Deux plis ; statistique = moyenne des deux plis ; bornes percentiles aux niveaux demandes."""
    un = np.ones((1, T_PLI))
    ponct = float(np.mean([interaction_pli(stats_taches(s), un)[0] for s in plis]))
    tir = np.zeros(N_TIRAGES)
    for s in plis:
        W = g.multinomial(T_PLI, np.full(T_PLI, 1.0 / T_PLI), size=N_TIRAGES).astype(float)
        tir += interaction_pli(stats_taches(s), W) / len(plis)
    out = {"ponctuelle": ponct, "ecart_type_tirages": float(tir.std())}
    for nv in niveaux:
        bas, haut = np.quantile(tir, [(1 - nv) / 2, (1 + nv) / 2])
        out[nv] = (float(bas), float(haut))
    return out


def etat(b):
    return 1 if b[0] > 0 else (-1 if b[1] < 0 else 0)


def campagne(cle, part_texte, sd_dep, inter, rep, kappa=1.0, rho=None):
    g = gen(2, *cle)
    rep = n_rep(rep)
    r = {"sonde": {0.99: [], 0.995: []}, "jumelle": {0.99: [], 0.995: []}, "ponct": [], "s_tir": []}
    for _ in range(rep):
        plis, plis2 = [], []
        for _k in range(2):
            a, b = monde_pli(g, part_texte, sd_dep, inter, kappa, rho)
            plis.append(a)
            plis2.append(b)
        l1 = lire_interaction(g, plis)
        r["ponct"].append(l1["ponctuelle"])
        r["s_tir"].append(l1["ecart_type_tirages"])
        for nv in (0.99, 0.995):
            r["sonde"][nv].append(etat(l1[nv]))
        if rho is not None:
            l2 = lire_interaction(g, plis2)
            for nv in (0.99, 0.995):
                r["jumelle"][nv].append(etat(l2[nv]))
    return r


b2 = {}
SCENARIOS = [(0.5, 0.1), (0.5, 0.3), (0.5, 0.5), (0.8, 0.1), (0.8, 0.3), (0.8, 0.5)]
z99, z80 = ND.inv_cdf(0.995), ND.inv_cdf(0.80)
for i, (pt, sd) in enumerate(SCENARIOS):
    nul = campagne((1, i), pt, sd, 0.0, rep=3000)
    e = np.array(nul["sonde"][0.99])
    e5 = np.array(nul["sonde"][0.995])
    s_vrai = float(np.std(nul["ponct"]))
    ligne = {
        "ecart_type_vrai_de_l_interaction": round(s_vrai, 4),
        "ecart_type_moyen_des_tirages": round(float(np.mean(nul["s_tir"])), 4),
        "taux_fausse_lecture_99_au_dessus": round(float((e == 1).mean()), 4),
        "taux_fausse_lecture_99_contraire": round(float((e == -1).mean()), 4),
        "taux_fausse_lecture_995_au_dessus": round(float((e5 == 1).mean()), 4),
        "taux_fausse_lecture_995_contraire": round(float((e5 == -1).mean()), 4),
        "interaction_minimale_detectable_80_formule": round((z99 + z80) * s_vrai, 3),
        "puissance_99": {},
    }
    for j, mult in enumerate((2.5, 3.0, 3.418, 4.0, 5.0)):
        inter = mult * s_vrai
        alt = campagne((2, i, j), pt, sd, inter, rep=500)
        ligne["puissance_99"][f"interaction_{inter:.3f}"] = round(float((np.array(alt["sonde"][0.99]) == 1).mean()), 3)
    b2[f"part_du_texte_{pt}_ecart_type_d_episode_du_deplacement_{sd}"] = ligne
sortie["bloc2_interaction_scores_bruts"] = b2

# ----------------------------------------------------------------------------------------------------------------- bloc 3
# Conjonction « la sonde et sa jumelle du second ordre de calcul s'accordent ».
b3 = {}
for i, (pt, sd) in enumerate([(0.5, 0.3), (0.8, 0.3)]):
    s_vrai = b2[f"part_du_texte_{pt}_ecart_type_d_episode_du_deplacement_{sd}"]["ecart_type_vrai_de_l_interaction"]
    for j, (rho, kappa) in enumerate([(0.95, 1.0), (0.7, 1.0), (0.7, 0.6), (0.3, 0.6)]):
        nul = campagne((3, i, j, 0), pt, sd, 0.0, rep=3000, kappa=kappa, rho=rho)
        a, b = np.array(nul["sonde"][0.99]), np.array(nul["jumelle"][0.99])
        ligne = {"fausse_tenue_au_dessus": round(float(((a == 1) & (b == 1)).mean()), 4),
                 "fausse_tenue_contraire": round(float(((a == -1) & (b == -1)).mean()), 4),
                 "desaccord_sous_le_nul": round(float((a != b).mean()), 4)}
        for jj, mult in enumerate((3.418, 5.0)):
            alt = campagne((3, i, j, 1 + jj), pt, sd, mult * s_vrai, rep=600, kappa=kappa, rho=rho)
            a, b = np.array(alt["sonde"][0.99]), np.array(alt["jumelle"][0.99])
            ligne[f"interaction_{mult}_ecarts_types_d_estimation"] = {
                "puissance_sonde_seule": round(float((a == 1).mean()), 3),
                "puissance_jumelle_seule": round(float((b == 1).mean()), 3),
                "puissance_conjonction": round(float(((a == 1) & (b == 1)).mean()), 3),
                "non_tranchee": round(float((a != b).mean()), 3)}
        b3[f"part_texte_{pt}_sd_{sd}_correlation_{rho}_rapport_d_effet_{kappa}"] = ligne
sortie["bloc3_conjonction_sonde_et_jumelle"] = b3

# ----------------------------------------------------------------------------------------------------------------- bloc 4
# Tendance : tau de Kendall stratifie par tache, score d'avant le champ du cout contre exces declare ; saboteur moins honnete.


def comptes_tau(scores, exces):
    """scores : (m, n) ; exces : (n,). Rend (m,) concordances moins discordances, et le nombre de paires."""
    n = exces.shape[0]
    if n < 2:
        return np.zeros(scores.shape[0]), 0.0
    iu = np.triu_indices(n, 1)
    se = np.sign(exces[iu[0]] - exces[iu[1]])
    ss = np.sign(scores[:, iu[0]] - scores[:, iu[1]])
    return ss @ se, float(len(iu[0]))


def monde_tau(g, rho_S, rho_H, p_S, p_H, n_dir):
    """Deux plis. Par tache : un episode du saboteur, un de l'honnete ; nombre d'actions lisibles binomial.
    Score = rho * exces + racine(1 - rho^2) * bruit ; n_dir directions de plancher sans lien avec l'exces."""
    plis = []
    for _k in range(2):
        CS, PS, CH, PH, CD = [], [], [], [], []
        for _t in range(T_PLI):
            nS, nH = int(g.binomial(K_ACT, p_S)), int(g.binomial(K_ACT, p_H))
            eS, eH = g.normal(size=nS), g.normal(size=nH)
            sS = rho_S * eS + math.sqrt(1 - rho_S ** 2) * g.normal(size=nS) + g.normal()
            sH = rho_H * eH + math.sqrt(1 - rho_H ** 2) * g.normal(size=nH) + g.normal()
            c, p = comptes_tau(sS[None, :], eS)
            CS.append(c[0]); PS.append(p)
            c, p = comptes_tau(sH[None, :], eH)
            CH.append(c[0]); PH.append(p)
            if n_dir:
                c, _ = comptes_tau(g.normal(size=(n_dir, nS)), eS)
                CD.append(c)
        plis.append((np.array(CS), np.array(PS), np.array(CH), np.array(PH), np.array(CD).T if n_dir else None))
    return plis


def lire_tau(g, plis, n_tir=1000):
    """Tau stratifie du saboteur, de l'honnete, difference ; bornes percentiles a 99 % ; memes tirages pour toutes les grandeurs.
    Avec plancher : tau de chaque direction (moyenne des deux plis), quantile 0,95 recalcule sur chaque tirage."""
    un = np.ones((1, T_PLI))
    avec_plancher = plis[0][4] is not None
    tS = tH = 0.0
    tirS, tirD = np.zeros(n_tir), np.zeros(n_tir)
    tirDir = np.zeros((n_tir, plis[0][4].shape[0])) if avec_plancher else None
    for CS, PS, CH, PH, CD in plis:
        tS += float((un @ CS)[0] / (un @ PS)[0]) / 2
        tH += float((un @ CH)[0] / (un @ PH)[0]) / 2
        W = g.multinomial(T_PLI, np.full(T_PLI, 1.0 / T_PLI), size=n_tir).astype(float)
        a, b = (W @ CS) / (W @ PS), (W @ CH) / (W @ PH)
        tirS += a / 2
        tirD += (a - b) / 2
        if avec_plancher:
            tirDir += (W @ CD.T) / (W @ PS)[:, None] / 2
    out = {"tau_S": tS, "tau_H": tH, "delta": tS - tH,
           "delta_99": tuple(float(x) for x in np.quantile(tirD, [0.005, 0.995]))}
    if avec_plancher:
        dt = tirS - np.quantile(tirDir, 0.95, axis=1)
        out["Dtau_99"] = tuple(float(x) for x in np.quantile(dt, [0.005, 0.995]))
    return out


b4 = {}
for i, (pS, pH, etiquette) in enumerate([(0.75, 0.85, "sept a huit actions lisibles par episode"),
                                         (0.5, 0.85, "cinq actions lisibles par episode du saboteur")]):
    g = gen(4, i)
    taus, deltas, faux_haut, faux_bas = [], [], 0, 0
    REP = n_rep(1500)
    for _ in range(REP):
        l = lire_tau(g, monde_tau(g, 0.0, 0.0, pS, pH, 0))
        taus.append(l["tau_S"]); deltas.append(l["delta"])
        faux_haut += l["delta_99"][0] > 0
        faux_bas += l["delta_99"][1] < 0
    s_tau, s_delta = float(np.std(taus)), float(np.std(deltas))
    ligne = {"ecart_type_du_tau_du_saboteur": round(s_tau, 4), "ecart_type_de_la_difference": round(s_delta, 4),
             "taux_fausse_lecture_99_difference_positive": round(faux_haut / REP, 4),
             "taux_fausse_lecture_99_difference_negative": round(faux_bas / REP, 4),
             "difference_minimale_detectable_80_formule_sans_plancher": round((z99 + z80) * s_delta, 3),
             "tau_minimal_detectable_80_formule_avec_plancher_au_quantile_095_du_nul": round((1.645 + z99 + z80) * s_tau, 3),
             "puissance": {}}
    for j, rho in enumerate((0.2, 0.3, 0.4, 0.5)):
        g2 = gen(4, i, 10 + j)
        ok_delta = ok_tout = 0
        REP2 = n_rep(150)
        for _ in range(REP2):
            l = lire_tau(g2, monde_tau(g2, rho, 0.0, pS, pH, 200))
            ok_delta += l["delta_99"][0] > 0
            ok_tout += (l["delta_99"][0] > 0) and (l["Dtau_99"][0] > 0)
        tau_vrai = 2 / math.pi * math.asin(rho)
        ligne["puissance"][f"correlation_{rho}_tau_vrai_{tau_vrai:.3f}"] = {
            "difference_seule": round(ok_delta / REP2, 3), "difference_et_plancher": round(ok_tout / REP2, 3)}
    # monde « grandeur du nombre » : meme lien chez l'honnete et chez le saboteur
    g3 = gen(4, i, 99)
    faux = 0
    REP3 = n_rep(600)
    for _ in range(REP3):
        l = lire_tau(g3, monde_tau(g3, 0.4, 0.4, pS, pH, 0))
        faux += (l["delta_99"][0] > 0) or (l["delta_99"][1] < 0)
    ligne["monde_grandeur_du_nombre_lien_egal_0.4_taux_de_difference_etablie"] = round(faux / REP3, 4)
    b4[etiquette] = ligne
sortie["bloc4_tendance_avant_le_champ_du_cout"] = b4

# ----------------------------------------------------------------------------------------------------------------- bloc 5
# Famille : nombre de fausses lectures attendu sous le nul global, par lecture.
pire = max(max(v["taux_fausse_lecture_99_au_dessus"], v["taux_fausse_lecture_99_contraire"]) for v in b2.values())
sortie["bloc5_famille"] = {
    "lignes_principales_par_lecture": 8, "lignes_a_seuil_par_lecture": 12,
    "attendu_nominal_principales_deux_sens": round(8 * 0.01, 3), "attendu_nominal_principales_un_sens": round(8 * 0.005, 3),
    "attendu_nominal_lignes_a_seuil_deux_sens": round(12 * 0.01, 3),
    "probabilite_nominale_d_au_moins_une_parmi_8_deux_sens": round(1 - 0.99 ** 8, 4),
    "pire_taux_simule_par_sens_sonde_seule_interaction": round(pire, 4),
    "attendu_au_pire_taux_simule_principales_deux_sens": round(8 * 2 * pire, 3),
}

texte = json.dumps(sortie, indent=1, ensure_ascii=False)
print(texte)
if len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8").write(texte + "\n")

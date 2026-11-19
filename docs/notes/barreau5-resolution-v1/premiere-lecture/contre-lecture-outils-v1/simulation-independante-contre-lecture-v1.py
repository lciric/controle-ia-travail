"""Contre-lecture du brouillon 1 « validite de l'adaptateur pour les sondes apprises sur la tache » : simulation independante.

Lois inventees par le contre-lecteur, differentes de celles du redacteur : bruit d'etat heteroscedastique (ecart type sous
adaptateur different du modele nu), bruit asymetrique (exponentielle centree) ou a queues lourdes (Student 3), effet de tache
du deplacement ; pour la tendance, couts de l'honnete arrondis (ex aequo), nombres d'actions utiles binomiaux.
Aucune donnee du programme. Entropie neuve tiree par SeedSequence() et ecrite dans la sortie (R9).
Estimateurs ecrits a neuf d'apres le texte du brouillon (« Metrique », points 3 et 4 ; « Seuil »), sans importer le code du
redacteur. Ecarts declares au texte : 2 000 tirages (texte : 10 000), 4 000 vecteurs de signes (texte : 100 000),
200 directions de plancher (texte : 800), 1 000 tirages pour la tendance.
"""
import json
import math
import os
import sys

import numpy as np

ENT = int(os.environ["ENTROPIE"]) if os.environ.get("ENTROPIE") else None
SS = np.random.SeedSequence(ENT)
ENT = SS.entropy


def gen(*k):
    return np.random.default_rng(np.random.SeedSequence(ENT, spawn_key=tuple(k)))


T, K = 32, 10
B, NS = 2000, 4000
Z = {0.99: 2.5758, 0.80: 0.8416}


def bruit(g, forme, loi):
    if loi == "normale":
        return g.normal(size=forme)
    if loi == "asym":
        return g.exponential(size=forme) - 1.0
    x = g.standard_t(3, size=forme)
    return x / math.sqrt(3.0)


def pli(g, v, inter):
    """Quatre cases (T, K). v : variante. Texte partage par les deux etats d'un meme texte."""
    pt, sde, kA, loi = v["part_texte"], v["sd_ep"], v["k_adapt"], v["loi"]
    tache = g.normal(0, math.sqrt(pt * 0.3), (T, 1))
    txt = {x: tache + g.normal(0, math.sqrt(pt * 0.2), (T, 1)) + g.normal(0, math.sqrt(pt * 0.5), (T, K))
           + (0.6 if x == "S" else 0.0) for x in "SH"}
    dep_t = g.normal(0, 0.25, (T, 1))
    s = {}
    for x in "SH":
        dep = 3.5 + dep_t + g.normal(0, sde, (T, 1)) + (inter if x == "S" else 0.0)
        s[x + "A"] = txt[x] + dep + kA * math.sqrt(1 - pt) * bruit(g, (T, K), loi)
        s[x + "N"] = txt[x] + math.sqrt(1 - pt) * bruit(g, (T, K), loi)
    return s


def stats_pli(s, W):
    """Interaction reduite du pli sur chaque tirage (W : multiplicites (tirages, T))."""
    m, var = {}, {}
    for c, x in s.items():
        n = W * K
        S1, S2 = W @ x.sum(1), W @ (x ** 2).sum(1)
        N_ = n.sum(1)
        m[c] = S1 / N_
        var[c] = (S2 - N_ * m[c] ** 2) / (N_ - 1)
    sig = np.sqrt((var["SA"] + var["HA"] + var["SN"] + var["HN"]) / 4)
    return ((m["SA"] - m["SN"]) - (m["HA"] - m["HN"])) / sig, sig


def lire(g, plis):
    un = np.ones((1, T))
    I_tir = np.zeros(B)
    I0 = 0.0
    Dk, sk = [], []
    for s in plis:
        i0, sg = stats_pli(s, un)
        I0 += i0[0] / 2
        W = g.multinomial(T, np.full(T, 1 / T), size=B).astype(float)
        I_tir += stats_pli(s, W)[0] / 2
        Dk.append((s["SA"] - s["SN"]).mean(1) - (s["HA"] - s["HN"]).mean(1))
        sk.append(sg[0])
    bas, haut = np.quantile(I_tir, [0.005, 0.995])
    Tobs = 0.5 * sum(D.mean() / sg for D, sg in zip(Dk, sk))
    sig = g.choice([-1.0, 1.0], size=(NS, 2 * T))
    Tst = 0.5 * ((sig[:, :T] * Dk[0]).mean(1) / sk[0] + (sig[:, T:] * Dk[1]).mean(1) / sk[1])
    p = (1 + np.sum(np.abs(Tst) >= abs(Tobs))) / (NS + 1)
    return I0, bas, haut, Tobs, p


def campagne(cle, v, inter, rep):
    g = gen(*cle)
    r = {"I": [], "int_haut": 0, "int_bas": 0, "dbl_haut": 0, "dbl_bas": 0}
    for _ in range(rep):
        I0, bas, haut, Tobs, p = lire(g, [pli(g, v, inter), pli(g, v, inter)])
        r["I"].append(I0)
        r["int_haut"] += bas > 0
        r["int_bas"] += haut < 0
        r["dbl_haut"] += (bas > 0) and (p < 0.01) and (Tobs > 0)
        r["dbl_bas"] += (haut < 0) and (p < 0.01) and (Tobs < 0)
    return r


VARIANTES = {
    "V1_normale_k1.2_ep0.3": dict(part_texte=0.6, sd_ep=0.3, k_adapt=1.2, loi="normale"),
    "V2_asym_k1.5_ep0.5": dict(part_texte=0.6, sd_ep=0.5, k_adapt=1.5, loi="asym"),
    "V3_student3_k1.0_ep0.2": dict(part_texte=0.3, sd_ep=0.2, k_adapt=1.0, loi="student"),
}
REP0 = int(os.environ.get("REP0", "1500"))
REP1 = int(os.environ.get("REP1", "400"))
out = {"entropie": int(ENT), "rep_nul": REP0, "rep_effet": REP1, "tirages": B, "vecteurs_de_signes": NS,
       "interaction": {}}
for i, (nom, v) in enumerate(VARIANTES.items()):
    r0 = campagne((1, i), v, 0.0, REP0)
    se = float(np.std(r0["I"]))
    ligne = {"ecart_type_vrai": round(se, 4),
             "fausse_lecture_intervalle_seul_par_sens": [round(r0["int_haut"] / REP0, 4), round(r0["int_bas"] / REP0, 4)],
             "fausse_lecture_critere_double_par_sens": [round(r0["dbl_haut"] / REP0, 4), round(r0["dbl_bas"] / REP0, 4)],
             "formule_plus_petite_detectable_80": round((Z[0.99] + Z[0.80]) * se, 3), "puissance_critere_double": {}}
    for j, mult in enumerate((3.0, 3.5, 4.0)):
        for sgn in (1, -1):
            r1 = campagne((2, i, j, 1 if sgn > 0 else 0), v, sgn * mult * se, REP1)
            cle = "dbl_haut" if sgn > 0 else "dbl_bas"
            ligne["puissance_critere_double"][f"{'+' if sgn > 0 else '-'}{mult}se_{sgn * mult * se:+.3f}"] = round(r1[cle] / REP1, 3)
    out["interaction"][nom] = ligne

# --------------------------------------------------------------------------------------------------------- tendance


def comptes(score, cout):
    n = len(cout)
    if n < 2:
        return None
    i, j = np.triu_indices(n, 1)
    sc = np.sign(cout[i] - cout[j])
    if score.ndim == 1:
        return float(np.sum(np.sign(score[i] - score[j]) * sc)), float(len(i))
    return np.sign(score[:, i] - score[:, j]) @ sc, float(len(i))


def monde_tau(g, rS, rH, arrondi_H, ndir=200):
    plis = []
    for _ in range(2):
        CS, PS, CH, PH, CD = [], [], [], [], []
        for _t in range(T):
            nS, nH = g.binomial(K, 0.78), g.binomial(K, 0.85)
            while nS < 2:
                nS = g.binomial(K, 0.78)
            while nH < 2:
                nH = g.binomial(K, 0.85)
            eS = g.normal(0.5, 0.6, nS)
            eH = g.normal(0.0, 0.25, nH)
            sS = rS * (eS - 0.5) / 0.6 + math.sqrt(1 - rS ** 2) * g.normal(size=nS)
            sH = rH * eH / 0.25 + math.sqrt(1 - rH ** 2) * g.normal(size=nH)
            cH = np.round(eH / 0.25) * 0.25 if arrondi_H else eH        # cout declare arrondi : ex aequo
            c, p = comptes(sS, eS); CS.append(c); PS.append(p)
            c, p = comptes(sH, cH); CH.append(c); PH.append(p)
            CD.append(comptes(g.normal(size=(ndir, nS)), eS)[0])
        plis.append(tuple(np.array(x) for x in (CS, PS, CH, PH)) + (np.array(CD).T,))
    return plis


def lire_tau(g, plis, nb=1000):
    dS = dH = 0.0
    tS, tD, tDir = np.zeros(nb), np.zeros(nb), np.zeros((nb, plis[0][4].shape[0]))
    for CS, PS, CH, PH, CD in plis:
        dS += CS.sum() / PS.sum() / 2
        dH += CH.sum() / PH.sum() / 2
        W = g.multinomial(T, np.full(T, 1 / T), size=nb).astype(float)
        a, b = (W @ CS) / (W @ PS), (W @ CH) / (W @ PH)
        tS += a / 2
        tD += (a - b) / 2
        tDir += (W @ CD.T) / (W @ PS)[:, None] / 2
    lo, hi = np.quantile(tD, [0.005, 0.995])
    Dt = tS - np.quantile(tDir, 0.95, axis=1)
    return dS - dH, lo, hi, float(np.quantile(Dt, 0.005))


def camp_tau(cle, rS, rH, arrondi, rep):
    g = gen(*cle)
    au_dessus = contraire = delta_haut = 0
    deltas = []
    for _ in range(rep):
        d, lo, hi, dtlo = lire_tau(g, monde_tau(g, rS, rH, arrondi))
        deltas.append(d)
        delta_haut += lo > 0
        au_dessus += (lo > 0) and (dtlo > 0)
        contraire += hi < 0
    return {"moyenne_delta_tau": round(float(np.mean(deltas)), 4), "ecart_type_delta_tau": round(float(np.std(deltas)), 4),
            "delta_seul_au_dessus": round(delta_haut / rep, 4), "regle_du_texte_au_dessus": round(au_dessus / rep, 4),
            "regle_du_texte_contraire": round(contraire / rep, 4)}


RT0 = int(os.environ.get("RT0", "600"))
RT1 = int(os.environ.get("RT1", "200"))
tau = {"rep_nul": RT0, "rep_effet": RT1}
tau["nul_aucun_lien_sans_ex_aequo"] = camp_tau((3, 0), 0.0, 0.0, False, RT0)
tau["nul_aucun_lien_couts_honnetes_arrondis"] = camp_tau((3, 1), 0.0, 0.0, True, RT0)
tau["grandeur_du_nombre_lien_egal_0.4_sans_ex_aequo"] = camp_tau((3, 2), 0.4, 0.4, False, RT0)
tau["grandeur_du_nombre_lien_egal_0.4_couts_honnetes_arrondis"] = camp_tau((3, 3), 0.4, 0.4, True, RT0)
for j, r in enumerate((0.3, 0.35, 0.4, 0.45)):
    tau[f"saboteur_lien_{r}_tau_approx_{2 / math.pi * math.asin(r):.3f}_honnete_0"] = camp_tau((4, j), r, 0.0, False, RT1)
out["tendance"] = tau

texte = json.dumps(out, indent=1, ensure_ascii=False)
print(texte)
if len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8").write(texte + "\n")

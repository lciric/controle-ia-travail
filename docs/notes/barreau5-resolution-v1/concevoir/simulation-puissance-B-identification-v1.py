"""Puissance des contrastes du plan « identification propre » (barreau 5).
Lois INVENTEES, aucune donnee du programme. Processeur seul. Graines par SeedSequence (R9)."""
import itertools, json, math
import numpy as np
from statistics import NormalDist
ND = NormalDist()
def tcrit(df, z=1.6449):  # quantile 0,95 de Student : table exacte aux petits degres, developpement au-dela
    return {1: 6.314, 2: 2.920, 3: 2.353, 4: 2.132, 5: 2.015, 6: 1.943, 7: 1.895}.get(df, z + (z**3 + z) / (4 * df))
SS = np.random.SeedSequence(20261119)
g1, g2, g3, g4, g5 = [np.random.default_rng(s) for s in SS.spawn(5)]
out = {}

# --- Sim 1 : entre adaptateurs, K paires appariees par graine --------------------------------
# D_k = delta + eps_k ; eps ~ N(0, 2 sigma^2 (1-rho)) ; sigma = ecart-type entre graines d'un meme bras.
def sim1(K, delta, rho, n=4000, alpha=0.05):
    sd = math.sqrt(2 * (1 - rho))
    D = delta + sd * g1.standard_normal((n, K))
    t = D.mean(1) / (D.std(1, ddof=1) / math.sqrt(K))
    signs = np.array(list(itertools.product([1, -1], repeat=K)))  # test exact par changement de signe
    perm = np.abs(D) @ signs.T                                    # (n, 2^K) sommes permutees
    p_s = (perm >= D.sum(1, keepdims=True) - 1e-12).mean(1)
    return round(float((t > tcrit(K - 1)).mean()), 3), round(float((p_s < alpha).mean()), 3)
out["sim1"] = {f"K={K},delta={d},rho={r}": sim1(K, d, r)
               for K in (2, 3, 5, 6, 8) for d in (0, 1, 2, 3) for r in (0.0, 0.5)}

# --- Sim 2 : sonde apprise contre le jumeau, et effacement, lus sur une paire tenue a l'ecart ---
# Activation d'une action = bruit N(0,I_d) + deplacement de l'adaptateur.
# Deplacement = s*u_c (commun a tout adaptateur) + tau*g_k (propre a la graine) + delta*u_s (saboteur seul).
def auc(pos, neg):
    r = np.argsort(np.argsort(np.concatenate([pos, neg]))) + 1.0
    return float((r[:len(pos)].sum() - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg)))
def sim2(Ktrain, delta, d=256, s=4.0, tau=2.0, n=320, rep=60):
    res = {"sonde_contre_nu__tenu_sab_contre_jumeau": [], "sonde_contre_jumeau__tenu_sab_contre_jumeau": [],
           "sonde_contre_nu_apres_effacement__tenu_sab_contre_jumeau": [],
           "sonde_contre_nu_apres_effacement__MEME_sab_contre_nu": []}
    for _ in range(rep):
        uc = np.zeros(d); uc[0] = 1; us = np.zeros(d); us[1] = 1
        def adapt(sab):
            return s * uc + tau * (lambda v: v / np.linalg.norm(v))(g2.standard_normal(d)) + (delta * us if sab else 0)
        S = [adapt(True) for _ in range(Ktrain + 1)]; T = [adapt(False) for _ in range(Ktrain + 1)]
        X = lambda shift: g2.standard_normal((n, d)) + shift
        nu_tr, nu_te = X(0), X(0)
        Str = np.vstack([X(a) for a in S[:Ktrain]]); Ttr = np.vstack([X(a) for a in T[:Ktrain]])
        Ste, Tte = X(S[-1]), X(T[-1])
        w_nu = Str.mean(0) - nu_tr.mean(0)                 # sonde « organisme contre modele nu » (etat actuel)
        w_tw = Str.mean(0) - Ttr.mean(0)                   # sonde a negatifs durs
        res["sonde_contre_nu__tenu_sab_contre_jumeau"].append(auc(Ste @ w_nu, Tte @ w_nu))
        res["sonde_contre_jumeau__tenu_sab_contre_jumeau"].append(auc(Ste @ w_tw, Tte @ w_tw))
        # effacement : sous-espace des deplacements moyens des jumeaux d'apprentissage (contre le nu)
        M = np.stack([X(a).mean(0) - nu_tr.mean(0) for a in T[:Ktrain]])
        Q = np.linalg.qr(M.T)[0]; P = lambda Z: Z - (Z @ Q) @ Q.T
        w_e = P(Str).mean(0) - P(nu_tr).mean(0)
        res["sonde_contre_nu_apres_effacement__tenu_sab_contre_jumeau"].append(auc(P(Ste) @ w_e, P(Tte) @ w_e))
        S0 = X(S[0])                                        # le MEME adaptateur saboteur, actions neuves
        res["sonde_contre_nu_apres_effacement__MEME_sab_contre_nu"].append(auc(P(S0) @ w_e, P(nu_te) @ w_e))
    return {k: round(float(np.mean(v)), 3) for k, v in res.items()} | {
        "part_des_tirages_ou_sonde_contre_jumeau_depasse_0.5": round(float(np.mean(
            np.array(res["sonde_contre_jumeau__tenu_sab_contre_jumeau"]) > 0.5)), 3)}
out["sim2"] = {f"Ktrain={K},delta={dl}": sim2(K, dl) for K in (1, 2, 5) for dl in (0.0, 0.5, 1.0, 2.0)}

# --- Sim 3 : a poids constants, actions gonflees contre non gonflees, stratifie par tache -----
# score = effet de tache + effet d'adaptateur + dprime*gonflee + bruit ; la tache decide aussi du taux de gonflement.
def sim3(K, dprime, taches=64, pas=10, p_moy=0.57, part_lisible=0.70, icc=0.3, rep=1500, alpha=0.05):
    ok = 0
    for _ in range(rep):
        a_t = g3.standard_normal(taches) * math.sqrt(icc)
        p_t = np.clip(np.array([ND.cdf(v) for v in ND.inv_cdf(0.81) * 1.6 + 0.8 * a_t + 0.6 * g3.standard_normal(taches)]), 0.02, 0.98)
        diffs = np.zeros(taches); poids = np.zeros(taches)
        for k in range(K):
            lis = g3.random((taches, pas)) < part_lisible
            gon = g3.random((taches, pas)) < p_t[:, None]
            sc = a_t[:, None] + dprime * gon + math.sqrt(1 - icc) * g3.standard_normal((taches, pas))
            for t in range(taches):
                a, b = sc[t][lis[t] & gon[t]], sc[t][lis[t] & ~gon[t]]
                if len(a) and len(b):
                    w = len(a) * len(b) / (len(a) + len(b)); diffs[t] += w * (a.mean() - b.mean()); poids[t] += w
        m = poids > 0; dm = diffs[m] / poids[m]
        ok += dm.mean() / (dm.std(ddof=1) / math.sqrt(len(dm))) > tcrit(len(dm) - 1)
    return round(ok / rep, 3)
aire = lambda dp: round(float(ND.cdf(dp / math.sqrt(2) / math.sqrt(0.7))), 3)  # aire a l'interieur d'une tache
out["sim3"] = {f"K={K},dprime={dp},aire_intra_tache={aire(dp)}": sim3(K, dp)
               for K in (1, 2, 6) for dp in (0.0, 0.1, 0.2, 0.3, 0.5)}

# --- Sim 4 : intervention sur la direction lue, issue = part d'actions gonflees (oracle du cout) ---
def sim4(taches, baisse, m_placebo=10, pas=10, p0=0.57, kappa=4.0, sd_dir=0.02, rep=3000, alpha=0.05):
    ok = 0
    for _ in range(rep):
        pt = g4.beta(p0 * kappa, (1 - p0) * kappa, taches)            # taux propre a la tache
        plac = np.stack([g4.binomial(pas, np.clip(pt + sd_dir * g4.standard_normal(), 0, 1)) for _ in range(m_placebo)]) / pas
        trait = g4.binomial(pas, np.clip(pt * (1 - baisse / p0) + 0, 0, 1)) / pas
        d_trait = (plac.mean(0) - trait).mean()
        # nul empirique : chaque placebo contre la moyenne des autres ; rang du traite parmi m+1 directions
        d_plac = [(np.delete(plac, j, 0).mean(0) - plac[j]).mean() for j in range(m_placebo)]
        ok += (d_trait > max(d_plac))                                  # p = 1/(m+1)
    return round(ok / rep, 3)
out["sim4_niveau_exact"] = "rang parmi m+1 directions : p = 1/(m+1) ; m=10 -> 0,091 ; m=19 -> 0,05"
out["sim4"] = {f"taches={t},baisse={b},placebos={m}": sim4(t, b, m)
               for t in (32, 64) for m in (10, 19) for b in (0.0, 0.03, 0.05, 0.10, 0.15)}

# --- Sim 5 : geometrie, part de la norme de la sonde dans le sous-espace d'ecriture de l'adaptateur ---
d, r = 4096, 256
Qs = np.linalg.qr(g5.standard_normal((d, r)))[0]
W = g5.standard_normal((2000, d)); W /= np.linalg.norm(W, axis=1, keepdims=True)
part = ((W @ Qs) ** 2).sum(1)
out["sim5_nul"] = {"dimension": d, "rang_sous_espace": r, "moyenne": round(float(part.mean()), 4),
                   "ecart_type": round(float(part.std()), 4), "quantile_0.999": round(float(np.quantile(part, 0.999)), 4)}
json.dump(out, open("sortie-simulation-puissance-B-identification-v1.json", "w"), indent=1, ensure_ascii=False)
for k, v in out.items():
    print("##", k)
    if isinstance(v, dict):
        for kk, vv in v.items(): print("  ", kk, vv)
    else: print("  ", v)

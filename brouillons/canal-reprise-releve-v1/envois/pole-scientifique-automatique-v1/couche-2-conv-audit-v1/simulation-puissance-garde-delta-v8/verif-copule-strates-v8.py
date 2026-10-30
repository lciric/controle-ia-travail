"""Vérification des deux mécaniques nouvelles de la v8 : la copule gaussienne sujet–comparateurs (R2) et les strates avec étalonnage (R3).

1. Table des quantiles bêta (copule) : interpolation contre `scipy.special.betaincinv` direct sur 2 000 000 de z tirés (écart maximal sur p) ; espérance et variance
   de q(Z), Z ~ N(0, 1), calculées par quadrature sur la table, contre p₀ et ρ p₀(1 − p₀) exacts (l'espérance doit être tenue) ; ceci pour toutes les paires (p₀, ρ) utilisées.
2. Corrélation de la copule : corrélation de Pearson de (p_A, p_B) attendue par quadrature de Gauss–Hermite à trois dimensions (u, e_A, e_B) sur les tables, contre celle
   tirée par `LoiSynthetique.tirer` (moments_tires), honnêtes et sabotés, c ∈ {0,5 ; 0,8} ; corrélation entre comparateurs aussi.
3. Témoin c → 0 : la copule à c = 10⁻⁶ donne la même loi que le tirage direct `rng.beta` (moments et quantiles de p_A et p_B, puissance de la fiche à 288 unités dans les
   2 erreurs types d'une différence).
4. Strates : espérance de p par strate = p₀(1 + γ d_s) ; espérance totale tenue ; variance totale de p tenue à ρ p₀(1 − p₀) (intra-strate + entre strates) ; l'étalonnage ne
   change pas l'espérance des écarts (E[g] = biais, E[v] = 0,10) ; allocation `bloc` : effectifs par strate à ±1 près.
5. Validité sous l'hypothèse nulle avec étalonnage (R5) : contraste d'écart nul (fiche nulle), avec et sans étalonnage, strates `sujet` γ = 0,4 : part des répétitions où la richesse
   d'un contraste atteint 40 (doit rester ≤ 1/40 = 0,025 plus 2 erreurs types, borne de Ville) ; la garde à la frontière E[g] = δ et le tricheur sont déjà dans chaque cellule.
   Témoin négatif : un « étalonnage » faux (qui ajoute 0,08 à l'espérance des écarts de contraste) fait dépasser la borne.

Usage : python3 -I -B verif-copule-strates-v8.py SCRIPT_V8 SORTIE.json
"""
import hashlib
import importlib.util
import json
import math
import sys
import time

import numpy as np

CHEMIN, SORTIE = sys.argv[1:3]
if not sys.flags.dont_write_bytecode:
    raise SystemExit("lancer avec -B")
spec = importlib.util.spec_from_file_location("v8", CHEMIN)
v8 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v8)
from scipy.special import betaincinv  # noqa: E402

t0 = time.time()
res = {"script_v8_sha256": hashlib.sha256(open(CHEMIN, "rb").read()).hexdigest(), "numpy": np.__version__}
rng = np.random.default_rng(np.random.SeedSequence([20261029, 8]))


# 1. table
PAIRES = [(0.01, 0.05), (0.01, 0.10), (0.01, 0.17), (0.0225, 0.17), (0.4, 0.05), (0.4, 0.10), (0.4, 0.17), (0.5, 0.17), (0.5, 0.05), (0.5, 0.10), (0.0225, 0.05), (0.0225, 0.10),
          (0.01, 0.25), (0.4, 0.25), (0.5, 0.25), (0.01, 0.35), (0.4, 0.35), (0.5, 0.35)]
phi = lambda z: 0.5 * np.vectorize(math.erfc)(-z / math.sqrt(2.0))
tab = []
for p0, rho in PAIRES:
    z = rng.normal(size=2_000_000)
    approx = v8.quantile_bete_de_z(p0, rho, z)
    a, b = v8.parametres_beta(p0, rho)
    exact = betaincinv(a, b, phi(z))
    zz, q = v8.table_quantiles_beta(p0, rho)
    w = np.exp(-zz ** 2 / 2) / math.sqrt(2 * math.pi)
    dz = zz[1] - zz[0]
    E = float(np.sum(q * w) * dz)
    V = float(np.sum((q - E) ** 2 * w) * dz)
    tab.append({"p0": p0, "rho": rho, "a": a, "b": b, "ecart_max_p_interpolation": float(np.max(np.abs(approx - exact))),
                "esperance_table": E, "esperance_exacte": p0, "ecart_esperance_relatif": (E - p0) / p0,
                "variance_table": V, "variance_exacte": rho * p0 * (1 - p0), "ecart_variance_relatif": (V - rho * p0 * (1 - p0)) / (rho * p0 * (1 - p0))})
res["table_quantiles"] = tab
res["table_ok"] = all(t["ecart_max_p_interpolation"] < 2e-3 and abs(t["ecart_esperance_relatif"]) < 2e-3 and abs(t["ecart_variance_relatif"]) < 5e-3 for t in tab)

# 2. corrélation de la copule : quadrature 3D
x, w = np.polynomial.hermite_e.hermegauss(48)
w = w / w.sum()


def attendu(pa, ra_, pb, rb_, c):
    U, EA, EB = np.meshgrid(x, x, x, indexing="ij")
    W = w[:, None, None] * w[None, :, None] * w[None, None, :]
    qa = v8.quantile_bete_de_z(pa, ra_, math.sqrt(c) * U + math.sqrt(1 - c) * EA)
    qb = v8.quantile_bete_de_z(pb, rb_, math.sqrt(c) * U + math.sqrt(1 - c) * EB)
    ma, mb = float(np.sum(W * qa)), float(np.sum(W * qb))
    cov = float(np.sum(W * qa * qb)) - ma * mb
    return cov / math.sqrt(float(np.sum(W * (qa - ma) ** 2)) * float(np.sum(W * (qb - mb) ** 2)))


cop = []
for rho in (0.10, 0.17):
    for c in (0.5, 0.8):
        loi = v8.LoiSynthetique(10, 10, 0.01, 0.4, 0.1, True, 0.0, True, rho, 0.0, 0.0, "beta", rho_b=rho, corr_ab=c)
        m = {}
        r = np.random.default_rng(np.random.SeedSequence([20261029, 81, int(1000 * rho), int(10 * c)]))
        loi.tirer(r, 2000, 288, 288, 8, 0.0, 0.0, m)
        att_h, att_s = attendu(0.01, rho, 0.01, rho, c), attendu(0.5, rho, 0.4, rho, c)
        cop.append({"rho": rho, "c": c, "pearson_pA_pB_honnetes_attendu": att_h, "tire": m["correlation_pA_pB_honnetes"],
                    "pearson_pA_pB_sabotes_attendu": att_s, "tire_sabotes": m["correlation_pA_pB_sabotes"],
                    "correlation_entre_comparateurs_honnetes_tiree": m["correlation_pB_honnetes_entre_comparateurs"],
                    "correlation_entre_comparateurs_sabotes_tiree": m["correlation_pB_sabotes_entre_comparateurs"],
                    "E_fB": m["E_fB"], "E_rB": m["E_rB"], "E_rA": m["E_rA"]})
res["copule_correlations"] = cop
res["copule_ok"] = all(abs(x["pearson_pA_pB_honnetes_attendu"] - x["tire"]) < 0.01 and abs(x["pearson_pA_pB_sabotes_attendu"] - x["tire_sabotes"]) < 0.01 for x in cop)

# 3. témoin c -> 0
reps = 4000
ebh = {"lectures": ["A"], "M": 2, "N": 0, "alpha": 0.05}
loiA = v8.LoiSynthetique(5, 10, 0.01, 0.4, 0.1, True, 0.0, True, 0.17, 0.0, 0.0, "beta", rho_b=0.17)
loiC = v8.LoiSynthetique(5, 10, 0.01, 0.4, 0.1, True, 0.0, True, 0.17, 0.0, 0.0, "beta", rho_b=0.17, corr_ab=1e-6)
res_temoin = {}
for nom, loi in (("direct", loiA), ("copule_1e-6", loiC)):
    e = dict(ebh) | {"nulle_A": loi.variante_nulle(True), "nulle_B": loi.variante_nulle(False)}
    c = v8.cellule(loi, loi, reps, 288, 288, 0.05, [40.0], 8, 0.0125, 20261029, "temoin-copule|" + nom, True, e)
    r = np.random.default_rng(np.random.SeedSequence([20261029, 82]))
    ph = ps = None
    m = {}
    loi.tirer(r, reps, 288, 288, 8, 0.0125, 0.0, m)
    res_temoin[nom] = {"fiche40": c["ebh_A"]["retenues_fiches_du_sujet"], "garde40": c["40.0"]["k_gardes"]["part"], "contraste40": c["40.0"]["k_contrastes"]["part"],
                       "E_fA": m["E_fA"], "E_fB": m["E_fB"], "E_rA": m["E_rA"], "E_rB": m["E_rB"], "ecart_type_pA_honnetes": m["ecart_type_pA_honnetes"],
                       "ecart_type_pB_honnetes": m["ecart_type_pB_honnetes"], "ecart_type_pA_sabotes": m["ecart_type_pA_sabotes"], "ecart_type_pB_sabotes": m["ecart_type_pB_sabotes"]}
d = res_temoin["direct"]["fiche40"] - res_temoin["copule_1e-6"]["fiche40"]
se = math.sqrt(2 * 0.9 * 0.1 / reps)
res["temoin_c_0"] = {**res_temoin, "difference_fiche": d, "erreur_type_difference": se, "dans_2_erreurs_types": abs(d) < 2 * se,
                     "ecarts_types_proches": all(abs(res_temoin["direct"][k] / res_temoin["copule_1e-6"][k] - 1) < 0.03 for k in
                                                 ("ecart_type_pA_honnetes", "ecart_type_pB_honnetes", "ecart_type_pA_sabotes", "ecart_type_pB_sabotes"))}

# 4. strates
st = []
for portee in ("sujet", "commune"):
    for S, gamma, alloc in ((2, 0.4, "bloc"), (3, 0.4, "bloc"), (3, 0.4, "iid"), (3, 0.2, "bloc")):
        loi = v8.LoiSynthetique(5, 10, 0.01, 0.4, 0.1, True, 0.0, True, 0.17, 0.0, 0.0, "beta", rho_b=0.17, strates=(S, gamma, portee, True, alloc))
        r = np.random.default_rng(np.random.SeedSequence([20261029, 83, S, int(10 * gamma), len(portee)]))
        reps_ = 1000
        sh = loi._strate_tirage(r, reps_, 288)
        eff = [int((sh == s).sum(axis=2).min()) for s in range(S)] + [int((sh == s).sum(axis=2).max()) for s in range(S)]
        # p tiré par strate
        pa = loi._p_strate(r, 0.5, 0.17, True, loi._strate_tirage(r, 400, 288), (400, 1, 288))
        ss = loi._strate_tirage(r, 4000, 288)
        pa = loi._p_strate(r, 0.5, 0.17, True, ss, (4000, 1, 288))
        pb = loi._p_strate(r, 0.4, 0.17, portee == "commune", ss, (4000, 8, 288))
        par_strate = [float(pa[ss == s].mean()) for s in range(S)]
        att_strate = loi._moyennes_strates(0.5, True).tolist()
        m_g, m = {}, {}
        g, v = loi.tirer(r, 2000, 288, 288, 8, 0.0125, 0.0, m)
        st.append({"S": S, "gamma": gamma, "portee": portee, "allocation": alloc, "effectifs_min_max_par_strate": eff,
                   "esperance_pA_sabotes_par_strate": par_strate, "attendue": att_strate,
                   "E_pA_sabotes": float(pa.mean()), "variance_pA_sabotes": float(pa.var()), "variance_visee": 0.17 * 0.25,
                   "E_pB_sabotes": float(pb.mean()), "variance_pB_sabotes": float(pb.var()), "variance_visee_B": 0.17 * 0.24,
                   "E_g_calibre": float(g.mean()), "E_g_attendu": 0.0125, "E_v_calibre": float(v.mean()), "E_v_attendu": 0.10,
                   "part_variance_ecart_prevue_contraste": m["part_variance_ecart_prevue_par_strates_contraste"],
                   "part_variance_ecart_prevue_garde": m["part_variance_ecart_prevue_par_strates_garde"]})
res["strates"] = st
ok_st = True
for x in st:
    ok_st &= abs(x["E_pA_sabotes"] - 0.5) < 0.004 and abs(x["variance_pA_sabotes"] / x["variance_visee"] - 1) < 0.03
    ok_st &= abs(x["E_g_calibre"] - x["E_g_attendu"]) < 0.0015 and abs(x["E_v_calibre"] - x["E_v_attendu"]) < 0.004
    ok_st &= all(abs(a - b) < 0.01 for a, b in zip(x["esperance_pA_sabotes_par_strate"], x["attendue"]))
    if x["allocation"] == "bloc":
        S = x["S"]
        ok_st &= max(x["effectifs_min_max_par_strate"][S:]) - min(x["effectifs_min_max_par_strate"][:S]) <= 1
    if x["portee"] == "commune":
        ok_st &= abs(x["E_pB_sabotes"] - 0.4) < 0.004 and abs(x["variance_pB_sabotes"] / x["variance_visee_B"] - 1) < 0.03
res["strates_ok"] = bool(ok_st)

# 5. validité sous l'hypothèse nulle avec étalonnage
borne = 1 / 40
nul = []
for calibre in (False, True):
    loi = v8.LoiSynthetique(5, 10, 0.01, 0.4, 0.0, True, 0.0, True, 0.17, 0.0, 0.0, "beta", rho_b=0.17, strates=(3, 0.4, "sujet", calibre, "bloc"))
    r = np.random.default_rng(np.random.SeedSequence([20261029, 84, int(calibre)]))
    reps_ = 4000
    _, c = v8.processus(loi, r, reps_, 288, 288, 1, 0.05, 0.0, loi)
    part = float((c.max(axis=2).max(axis=0) >= math.log(40)).mean()) if c.ndim == 3 else float((c.max(axis=1) >= math.log(40)).mean())
    nul.append({"etalonnage": calibre, "part_contraste_nul_atteint_40": part, "borne_ville": borne, "erreur_type": math.sqrt(borne * (1 - borne) / reps_)})
# témoin négatif (R5) : un « étalonnage » faux, qui ajoute 0,08 à l'espérance des écarts de contraste, doit faire dépasser la borne de Ville
loi = v8.LoiSynthetique(5, 10, 0.01, 0.4, 0.0, True, 0.0, True, 0.17, 0.0, 0.0, "beta", rho_b=0.17, strates=(3, 0.4, "sujet", False, "bloc"))
r = np.random.default_rng(np.random.SeedSequence([20261029, 85]))
m = {}
g, v = loi.tirer(r, 4000, 288, 288, 1, 0.0, 0.0, m)
v_faux2 = v + 0.08
traj2 = v8.prolonger(v8.log_richesse(v8.ecreter(v_faux2[:, 0, :])), 288)
part_faux2 = float((traj2.max(axis=1) >= math.log(40)).mean())
res["hypothese_nulle"] = {"cas": nul, "temoin_negatif_decalage_d_esperance_plus_0_08": {"part_atteint_40": part_faux2, "decele": part_faux2 > borne + 5 * math.sqrt(borne / 4000)}}
res["hypothese_nulle_ok"] = all(x["part_contraste_nul_atteint_40"] <= borne + 2 * x["erreur_type"] for x in nul) and res["hypothese_nulle"]["temoin_negatif_decalage_d_esperance_plus_0_08"]["decele"]

res["conforme"] = bool(res["table_ok"] and res["copule_ok"] and res["temoin_c_0"]["dans_2_erreurs_types"] and res["temoin_c_0"]["ecarts_types_proches"] and res["strates_ok"]
                       and res["hypothese_nulle_ok"])
res["duree_s"] = round(time.time() - t0, 1)
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write("\n")
print({k: res[k] for k in ("table_ok", "copule_ok", "strates_ok", "hypothese_nulle_ok", "conforme", "duree_s")})
print(json.dumps(res["copule_correlations"], indent=0)[:1500])
print(json.dumps(res["temoin_c_0"], indent=0)[:1500])
print(json.dumps(res["hypothese_nulle"], indent=0))

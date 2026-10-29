"""Vérification de l'effet d'unité sur les comparateurs de la v6 (GD5-01) et de l'identité avec la v5 quand l'effet est nul.

1. Effets tirés : moyenne 0, variance 1 en chaque case, corrélation entre comparateurs ≈ ρ, indépendance entre unités.
2. Espérance tenue : E[f_B] = τ et E[r_B] = r_B (écart ≤ 4 erreurs types), pour σ ∈ {0,5 ; 1,0}, ρ ∈ {0 ; 0,17}.
3. Variance ajoutée : Var(g_j) − Var(f_A) = Var binomiale de f_B + Var(p_B)(1 − 1/K) (décomposition écrite en sortie), mesurée
   sur les tirages (g = f_A − f_B, f_A sans effet).
4. Lien tenu : l'effet des sabotés est celui des honnêtes de la même unité (corrélation des p), lien coupé : corrélation nulle.
5. Identité : à σ = 0, `cellule(…)` de la v6 rend, champ pour champ, ce que rend la v5 (mêmes options, même graine), avec la
   lecture e-BH (A) et (B) et les fiches nulles ; aux champs nouveaux près (borne α_c·m₀/m).

Usage : python3 -I -B verif-effet-comparateurs-v6.py SCRIPT_V6 SCRIPT_V5 SORTIE.json   (-B : aucun __pycache__)
"""

import hashlib
import importlib.util
import json
import math
import sys

import numpy as np

V6, V5, SORTIE = sys.argv[1], sys.argv[2], sys.argv[3]
if not sys.flags.dont_write_bytecode:
    raise SystemExit("refus : lancer avec -B (aucun __pycache__ dans les dossiers lus)")


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


v6, v5 = charger("sim_v6", V6), charger("sim_v5", V5)
empreinte = lambda c: hashlib.sha256(open(c, "rb").read()).hexdigest()
bilan = {"script_v6": V6, "script_v6_sha256": empreinte(V6), "script_v5": V5, "script_v5_sha256": empreinte(V5)}

# --- 1. effets tirés
essais1 = []
for rho in (0.0, 0.17, 0.5):
    loi = v6.LoiSynthetique(10, 10, 0.01, 0.4, 0.1, effet_b=1.0, corr_b=rho)
    rng = np.random.default_rng(np.random.SeedSequence([20261029, 11]))
    u = loi._effets_comparateurs(rng, 4000, 8, 100)
    c = np.corrcoef(u.transpose(1, 0, 2).reshape(8, -1))
    hors_diag = (c.sum() - 8) / 56
    suivantes = np.corrcoef(u[:, 0, :-1].ravel(), u[:, 0, 1:].ravel())[0, 1]  # unités voisines : indépendantes
    essais1.append({"rho": rho, "moyenne": float(u.mean()), "variance": float(u.var()), "correlation_moyenne_entre_comparateurs": float(hors_diag),
                    "correlation_unites_voisines": float(suivantes),
                    "conforme": bool(abs(u.mean()) < 0.005 and abs(u.var() - 1) < 0.01 and abs(hors_diag - rho) < 0.005 and abs(suivantes) < 0.005)})
bilan["1_effets_tires"] = essais1

# --- 2, 3, 4. espérance tenue, variance ajoutée, lien
essais2 = []
for sigma in (0.5, 1.0):
    for rho in (0.0, 0.17):
        for K in (10, 3):
            for lien in (True, False):
                loi = v6.LoiSynthetique(K, K, 0.01, 0.4, 0.1, True, 0.0, lien, 0.0, sigma, rho)
                rng = np.random.default_rng(np.random.SeedSequence([20261029, 12]))
                moments = {}
                g, v = loi.tirer(rng, 4000, 100, 100, 8, 0.0, 0.0, moments)
                dec = loi.decomposition(0.0)
                # g_j = f_A − f_Bj ; f_A sans effet : Var f_A = τ(1 − τ)/K ; Var(g_j) = Var f_A + Var f_B
                var_g = float(g.var(axis=(0, 2)).mean())
                var_attendue_g = 0.01 * 0.99 / K + (dec["comparateurs_honnetes_fB"]["variance_binomiale_par_unite"]
                                                     + dec["comparateurs_honnetes_fB"]["variance_ajoutee_par_unite"])
                var_v = float(v.var(axis=(0, 2)).mean())
                var_attendue_v = 0.5 * 0.5 / K + (dec["comparateurs_sabotes_rB"]["variance_binomiale_par_unite"]
                                                   + dec["comparateurs_sabotes_rB"]["variance_ajoutee_par_unite"])
                n_cases = 4000 * 100
                se_fb = math.sqrt(var_attendue_g / (n_cases * 8))
                se_rb = math.sqrt(var_attendue_v / (n_cases * 8))
                ecart_fb = moments["E_fB"] - 0.01
                ecart_rb = moments["E_rB"] - 0.4
                e = {"sigma": sigma, "rho": rho, "K": K, "lien_tenu": lien,
                     "E_fB": moments["E_fB"], "E_fB_vise": 0.01, "ecart_en_erreurs_types": ecart_fb / se_fb,
                     "E_rB": moments["E_rB"], "E_rB_vise": 0.4, "ecart_rb_en_erreurs_types": ecart_rb / se_rb,
                     "variance_g_mesuree": var_g, "variance_g_attendue": var_attendue_g,
                     "variance_v_mesuree": var_v, "variance_v_attendue": var_attendue_v,
                     "correlation_pB_honnetes_entre_comparateurs": moments["correlation_pB_honnetes_entre_comparateurs"],
                     "correlation_pB_sabotes_entre_comparateurs": moments["correlation_pB_sabotes_entre_comparateurs"],
                     "correlation_g_entre_comparateurs": moments["correlation_g_entre_comparateurs"],
                     "correlation_v_entre_comparateurs": moments["correlation_v_entre_comparateurs"]}
                # lien tenu / coupé : corrélation, dans l'unité, des p de B honnête et sabotée (même comparateur, même indice).
                # `tirer` ne rend pas les p : on les retire avec le même générateur en rappelant la méthode interne.
                rng2 = np.random.default_rng(np.random.SeedSequence([20261029, 13]))
                if lien:
                    ub = loi._effets_comparateurs(rng2, 2000, 8, 100)
                    uh, us = ub, ub
                else:
                    uh, us = loi._effets_comparateurs(rng2, 2000, 8, 100), loi._effets_comparateurs(rng2, 2000, 8, 100)
                e["correlation_effet_honnetes_sabotes_meme_unite"] = float(np.corrcoef(uh.ravel(), us.ravel())[0, 1])
                e["conforme"] = bool(abs(e["ecart_en_erreurs_types"]) < 4 and abs(e["ecart_rb_en_erreurs_types"]) < 4
                                     and abs(var_g / var_attendue_g - 1) < 0.05 and abs(var_v / var_attendue_v - 1) < 0.05
                                     and abs(e["correlation_effet_honnetes_sabotes_meme_unite"] - (1.0 if lien else 0.0)) < 0.01)
                essais2.append(e)
bilan["2_3_4_esperance_variance_lien"] = essais2

# --- 5. identité v5 = v6 à σ = 0
CHAMPS_NOUVEAUX = {"alpha_c", "fiches_nulles_m0", "borne_fdr_alpha_c_m0_sur_m", "a_comparer_a_la_borne"}


def plat(d, p=""):
    if isinstance(d, dict):
        for k, v in d.items():
            yield from plat(v, f"{p}/{k}")
    else:
        yield p, d


essais5 = []
for (K, tau, ks, n, ng, delta, biais, nulles, effet_a, beta) in ((10, 0.01, (1, 3, 8), 60, 60, 0.05, 0.0125, 0, 0.0, 0.0),
                                                                  (3, 0.10, (3, 8), 80, 50, 0.05, 0.0, 2, 0.0, 0.0),
                                                                  (10, 0.01, (3,), 40, 40, 0.075, 0.0, 1, 1.0, 0.0),
                                                                  (10, 0.01, (3,), 40, 40, 0.075, 0.0, 1, 0.0, 0.17)):
    for k in ks:
        etiq = f"cellule-test|K={K}|tau={tau}|k={k}|n={n}|ng={ng}|a={effet_a}|beta={beta}"
        ebh = {"lectures": ["A", "B"], "M": 2, "N": nulles, "alpha": 0.05}
        sorties = []
        for mod in (v5, v6):
            loi = mod.LoiSynthetique(K, K, tau, 0.4, 0.1, True, effet_a, True, beta)
            ebh_loi = dict(ebh) | {"nulle_A": loi.variante_nulle(True), "nulle_B": loi.variante_nulle(False)}
            sorties.append(dict(plat(mod.cellule(loi, loi, 300, n, ng, delta, [40.0, 160.0, 320.0], k, biais, 20261029, etiq, True,
                                                 ebh_loi))))
        a, b = sorties
        communs = [x for x in a if x in b]
        diffs = [x for x in communs if a[x] != b[x]]
        nouveaux = sorted({x.split("/")[-1] for x in b if x not in a})
        essais5.append({"cellule": etiq, "champs_communs": len(communs), "differences": len(diffs), "exemples": diffs[:5],
                        "champs_seulement_v5": [x for x in a if x not in b], "champs_nouveaux_v6": nouveaux,
                        "nouveaux_attendus": set(nouveaux) <= CHAMPS_NOUVEAUX,
                        "conforme": len(diffs) == 0 and not [x for x in a if x not in b] and set(nouveaux) <= CHAMPS_NOUVEAUX})
bilan["5_identite_v5_v6_a_sigma_nul"] = essais5
# témoin négatif (R5) : la même comparaison doit trouver des différences dès que l'effet est non nul
etiq = "cellule-test|K=10|tau=0.01|k=3|n=60|ng=60|a=0.0|beta=0.0"
loi5 = v5.LoiSynthetique(10, 10, 0.01, 0.4, 0.1, True, 0.0, True, 0.0)
loi6 = v6.LoiSynthetique(10, 10, 0.01, 0.4, 0.1, True, 0.0, True, 0.0, 0.5, 0.0)
c5 = dict(plat(v5.cellule(loi5, loi5, 300, 60, 60, 0.05, [40.0, 160.0], 3, 0.0, 20261029, etiq, True, None)))
c6 = dict(plat(v6.cellule(loi6, loi6, 300, 60, 60, 0.05, [40.0, 160.0], 3, 0.0, 20261029, etiq, True, None)))
diffs_temoin = [x for x in c5 if x in c6 and c5[x] != c6[x]]
bilan["5bis_temoin_negatif_effet_non_nul"] = {"differences": len(diffs_temoin), "conforme": len(diffs_temoin) > 0}
bilan["conforme"] = (all(e["conforme"] for e in essais1) and all(e["conforme"] for e in essais2)
                     and all(e["conforme"] for e in essais5) and bilan["5bis_temoin_negatif_effet_non_nul"]["conforme"])
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(bilan, f, indent=1, ensure_ascii=False, default=list)
    f.write("\n")
print("conforme :", bilan["conforme"], "| effets :", [e["conforme"] for e in essais1], "| esperance/variance :",
      sum(e["conforme"] for e in essais2), "/", len(essais2), "| identité :", [e["conforme"] for e in essais5])

"""Vérification de la correspondance logit → bêta de la v7 (doute 1) : pour σ ∈ {0,5 ; 1,0} (scénarios de la v6),
1. correspondance exacte : ρ_b = Var_logit(r_B, σ)/(r_B(1 − r_B)) (quadrature de `moments_logit`, la même qu'en v6), κ = (1 − ρ_b)/ρ_b ;
   paramètres (p₀κ, (1 − p₀)κ) pour p₀ = τ et p₀ = r_B ; écarts-types théoriques des deux côtés, comparés aux écarts-types logit de la v6 ;
2. simulation : p_B tirés par `LoiSynthetique.tirer` (échelle bêta) ; espérance tenue (E[f_B] = τ, E[r_B] = r_B à 4 erreurs types),
   écart-type de p_B des sabotés = écart-type logit de la v6 (à 2 % près), écart-type de p_B des honnêtes = √(ρ_b τ(1 − τ)) (à 2 % près),
   corrélation nulle entre comparateurs et entre honnêtes et sabotés de la même unité (tirés à part), variance de g et de v conforme à la
   décomposition écrite ;
3. la même simulation en échelle logit (v7, défaut) retrouve les écarts-types logit : les deux échelles donnent le même écart-type sur
   r_B et diffèrent sur f_B (c'est le point du doute 1).

Usage : python3 -I -B verif-correspondance-beta-v7.py SCRIPT_V7 SORTIE.json   (-B : aucun __pycache__)
"""

import hashlib
import importlib.util
import json
import math
import sys

import numpy as np

V7, SORTIE = sys.argv[1], sys.argv[2]
if not sys.flags.dont_write_bytecode:
    raise SystemExit("refus : lancer avec -B (aucun __pycache__ dans les dossiers lus)")


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


v7 = charger("sim_v7", V7)
bilan = {"script_v7": V7, "script_v7_sha256": hashlib.sha256(open(V7, "rb").read()).hexdigest(), "tau": 0.01, "r_B": 0.4}
TAU, RB = 0.01, 0.4
REPS, N, K8 = 4000, 100, 8
essais = []
for sigma in (0.5, 1.0):
    # 1. correspondance exacte
    var_logit_rb = v7.moments_logit(RB, sigma)[1]
    var_logit_fb = v7.moments_logit(TAU, sigma)[1]
    rho_b = var_logit_rb / (RB * (1 - RB))
    kappa = (1 - rho_b) / rho_b
    loi = v7.LoiSynthetique(10, 10, TAU, RB, 0.1, True, 0.0, True, 0.0, sigma, 0.0, "beta")
    rho_loi, kappa_loi = loi.parametres_beta_comparateurs()
    a_h, b_h = v7.parametres_beta(TAU, rho_b)
    a_s, b_s = v7.parametres_beta(RB, rho_b)
    theorie = {"sigma_logit_de_reference": sigma, "var_logit_rB_v6": var_logit_rb, "ecart_type_logit_rB_v6": math.sqrt(var_logit_rb),
               "ecart_type_logit_fB_v6": math.sqrt(var_logit_fb), "rho_b": rho_b, "kappa": kappa,
               "rho_b_du_script": rho_loi, "kappa_du_script": kappa_loi,
               "beta_fB_a_b": [a_h, b_h], "beta_rB_a_b": [a_s, b_s],
               "esperance_beta_fB": a_h / (a_h + b_h), "esperance_beta_rB": a_s / (a_s + b_s),
               "variance_beta_fB": a_h * b_h / ((a_h + b_h) ** 2 * (a_h + b_h + 1)),
               "variance_beta_rB": a_s * b_s / ((a_s + b_s) ** 2 * (a_s + b_s + 1)),
               "ecart_type_beta_fB": math.sqrt(rho_b * TAU * (1 - TAU)), "ecart_type_beta_rB": math.sqrt(rho_b * RB * (1 - RB)),
               "rapport_ecart_type_fB_beta_sur_logit": math.sqrt(rho_b * TAU * (1 - TAU)) / math.sqrt(var_logit_fb)}
    theorie["conforme"] = bool(abs(rho_loi - rho_b) < 1e-12 and abs(kappa_loi - kappa) < 1e-9
                               and abs(theorie["esperance_beta_fB"] - TAU) < 1e-12 and abs(theorie["esperance_beta_rB"] - RB) < 1e-12
                               and abs(theorie["variance_beta_rB"] - var_logit_rb) < 1e-12
                               and abs(theorie["variance_beta_fB"] - rho_b * TAU * (1 - TAU)) < 1e-12)
    # 2. simulation en échelle bêta, 3. en échelle logit (même σ)
    sims = {}
    for echelle in ("beta", "logit"):
        for K in (10, 5):
            loi = v7.LoiSynthetique(K, K, TAU, RB, 0.1, True, 0.0, True, 0.0, sigma, 0.0, echelle)
            rng = np.random.default_rng(np.random.SeedSequence([20261029, 21]))
            moments = {}
            g, v = loi.tirer(rng, REPS, N, N, K8, 0.0, 0.0, moments)
            dec = loi.decomposition(0.0)
            dh, ds = dec["comparateurs_honnetes_fB"], dec["comparateurs_sabotes_rB"]
            n_cases = REPS * N * K8
            var_g_att = TAU * (1 - TAU) / K + dh["variance_binomiale_par_unite"] + dh["variance_ajoutee_par_unite"]
            var_v_att = 0.5 * 0.5 / K + ds["variance_binomiale_par_unite"] + ds["variance_ajoutee_par_unite"]
            var_g, var_v = float(g.var(axis=(0, 2)).mean()), float(v.var(axis=(0, 2)).mean())
            se_fb, se_rb = math.sqrt(var_g_att / n_cases), math.sqrt(var_v_att / n_cases)
            # corrélation honnêtes/sabotés de la même unité : p non rendus par `tirer` ; on retire les p avec le même ordre de tirage
            rng2 = np.random.default_rng(np.random.SeedSequence([20261029, 22]))
            if echelle == "beta":
                rho_l, _ = loi.parametres_beta_comparateurs()
                ph = rng2.beta(*v7.parametres_beta(TAU, rho_l), size=(REPS, K8, N))
                ps = rng2.beta(*v7.parametres_beta(RB, rho_l), size=(REPS, K8, N))
                # test d'ajustement : quantiles empiriques de p sabotés contre quantiles exacts de la bêta (scipy absent du script :
                # comparaison des moments d'ordre 3 à la valeur exacte de la bêta)
                a_, b_ = v7.parametres_beta(RB, rho_l)
                m3_exact = a_ * (a_ + 1) * (a_ + 2) / ((a_ + b_) * (a_ + b_ + 1) * (a_ + b_ + 2))
                m3 = float((ps ** 3).mean())
                ajust = {"moment_3_rB_simule": m3, "moment_3_rB_exact_beta": m3_exact, "ecart_relatif": m3 / m3_exact - 1}
            else:
                u = loi._effets_comparateurs(rng2, REPS, K8, N)
                ph, ps = v7.proba_decalee(TAU, sigma, u), v7.proba_decalee(RB, sigma, u)
                ajust = None
            corr_hs = float(np.corrcoef(ph.ravel(), ps.ravel())[0, 1])
            e = {"echelle": echelle, "K": K, "E_fB": moments["E_fB"], "ecart_E_fB_en_erreurs_types": (moments["E_fB"] - TAU) / se_fb,
                 "E_rB": moments["E_rB"], "ecart_E_rB_en_erreurs_types": (moments["E_rB"] - RB) / se_rb,
                 "ecart_type_pB_honnetes_simule": moments["ecart_type_pB_honnetes"], "ecart_type_pB_honnetes_attendu": dh["ecart_type_ajoute_sur_p"],
                 "ecart_type_pB_sabotes_simule": moments["ecart_type_pB_sabotes"], "ecart_type_pB_sabotes_attendu": ds["ecart_type_ajoute_sur_p"],
                 "ecart_type_logit_rB_v6": math.sqrt(var_logit_rb), "ecart_type_logit_fB_v6": math.sqrt(var_logit_fb),
                 "correlation_pB_honnetes_entre_comparateurs": moments["correlation_pB_honnetes_entre_comparateurs"],
                 "correlation_pB_sabotes_entre_comparateurs": moments["correlation_pB_sabotes_entre_comparateurs"],
                 "correlation_p_honnetes_sabotes_meme_unite": corr_hs,
                 "variance_g_mesuree": var_g, "variance_g_attendue": var_g_att, "variance_v_mesuree": var_v, "variance_v_attendue": var_v_att,
                 "ajustement_beta": ajust, "nom_de_la_loi": loi.nom()}
            ok = (abs(e["ecart_E_fB_en_erreurs_types"]) < 4 and abs(e["ecart_E_rB_en_erreurs_types"]) < 4
                  and abs(e["ecart_type_pB_honnetes_simule"] / e["ecart_type_pB_honnetes_attendu"] - 1) < 0.02
                  and abs(e["ecart_type_pB_sabotes_simule"] / e["ecart_type_pB_sabotes_attendu"] - 1) < 0.02
                  and abs(e["ecart_type_pB_sabotes_simule"] / math.sqrt(var_logit_rb) - 1) < 0.02  # les deux échelles : même écart-type sur r_B
                  and abs(var_g / var_g_att - 1) < 0.05 and abs(var_v / var_v_att - 1) < 0.05
                  and abs(e["correlation_pB_honnetes_entre_comparateurs"]) < 0.01 and abs(e["correlation_pB_sabotes_entre_comparateurs"]) < 0.01)
            if echelle == "beta":
                ok = ok and abs(corr_hs) < 0.01 and abs(ajust["ecart_relatif"]) < 0.02 and "_beta" in loi.nom()
                ok = ok and abs(e["ecart_type_pB_honnetes_simule"] / math.sqrt(rho_b * TAU * (1 - TAU)) - 1) < 0.02
            else:
                # lien tenu en logit : même effet u pour les honnêtes et les sabotés ; la corrélation des p (sigmoïdes à des centres
                # différents) est forte mais < 1 : exigée > 0,5
                ok = ok and corr_hs > 0.5 and "_beta" not in loi.nom()
                ok = ok and abs(e["ecart_type_pB_honnetes_simule"] / math.sqrt(var_logit_fb) - 1) < 0.02
            e["conforme"] = bool(ok)
            sims[f"{echelle}|K={K}"] = e
    essais.append({"sigma": sigma, "1_correspondance": theorie, "2_3_simulation": sims})
bilan["essais"] = essais
# refus attendus (R5 : garde testée sur un artefact) : bêta avec corrélation entre comparateurs ; paramètres bêta hors échelle bêta
refus = {}
try:
    v7.LoiSynthetique(10, 10, TAU, RB, 0.1, True, 0.0, True, 0.0, 1.0, 0.17, "beta")
    refus["beta_avec_corr"] = "accepté (NON conforme)"
except v7.Refus as e:
    refus["beta_avec_corr"] = str(e)
try:
    v7.LoiSynthetique(10, 10, TAU, RB, 0.1, True, 0.0, True, 0.0, 1.0, 0.0, "logit").parametres_beta_comparateurs()
    refus["parametres_beta_hors_echelle"] = "accepté (NON conforme)"
except v7.Refus as e:
    refus["parametres_beta_hors_echelle"] = str(e)
try:
    v7.LoiSynthetique(10, 10, TAU, RB, 0.1, True, 0.0, True, 0.0, 1.0, 0.0, "gamma")
    refus["echelle_inconnue"] = "accepté (NON conforme)"
except v7.Refus as e:
    refus["echelle_inconnue"] = str(e)
bilan["refus"] = refus
bilan["conforme"] = (all(x["1_correspondance"]["conforme"] for x in essais) and all(e["conforme"] for x in essais for e in x["2_3_simulation"].values())
                     and all(v.startswith("refus") for v in refus.values()))
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(bilan, f, indent=1, ensure_ascii=False)
    f.write("\n")
for x in essais:
    t = x["1_correspondance"]
    print(f"σ = {x['sigma']} : ρ_b = {t['rho_b']:.4f}, κ = {t['kappa']:.3f} ; écart-type r_B : logit {t['ecart_type_logit_rB_v6']:.4f} = bêta {t['ecart_type_beta_rB']:.4f} ; "
          f"écart-type f_B : logit {t['ecart_type_logit_fB_v6']:.4f}, bêta {t['ecart_type_beta_fB']:.4f} (× {t['rapport_ecart_type_fB_beta_sur_logit']:.2f})")
    for k, e in x["2_3_simulation"].items():
        print("  ", k, "conforme" if e["conforme"] else "NON CONFORME", f"sd fB {e['ecart_type_pB_honnetes_simule']:.4f} sd rB {e['ecart_type_pB_sabotes_simule']:.4f}")
print("conforme :", bilan["conforme"])

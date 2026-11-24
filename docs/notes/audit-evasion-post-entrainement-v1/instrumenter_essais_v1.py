#!/usr/bin/env python3
"""Instrumentation des 14 000 essais du vérificateur v2, sans le modifier :
rejoue les mêmes tirages (mêmes graines, même ordre d'appels au générateur) et
compte ce que chaque test vérifie réellement, ce que les tolérances écartent,
et quelle part de l'espace des paramètres est couverte."""
import importlib.util, json, math, random, sys
spec = importlib.util.spec_from_file_location("v2", sys.argv[1])
v2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(v2)

out = {}
# 1. Théorème 1 : mêmes tirages
rng = random.Random(20261124)
excl_ampA = excl_domB = excl_ampB = 0
nb_ampA_vrai = nb_domB_vrai = nb_ampB_vrai = 0
min_bf = 1; max_eta = 0; min_pf = 1; nb_bf_eq_bh = 0; min_gap_fh = 1
for _ in range(10_000):
    u1, u2, u3 = rng.uniform(0.02, 1.0), rng.uniform(0.02, 1.0), rng.uniform(0.02, 1.0)
    s = u1+u2+u3; p_h, p_v, p_f = u1/s, u2/s, u3/s
    beta_h = rng.uniform(0.55, 1.0); beta_f = rng.uniform(0.20, beta_h)
    beta_v = rng.uniform(0.0, beta_f-1e-3); eta = rng.uniform(0.1, 8.0)
    dr = rng.uniform(0.05, 5.0); c = rng.uniform(0.0, 4.0)
    min_bf = min(min_bf, beta_f); max_eta = max(max_eta, eta); min_pf = min(min_pf, p_f)
    min_gap_fh = min(min_gap_fh, beta_h-beta_f); nb_bf_eq_bh += (beta_f == beta_h)
    lhs_a = (beta_f-beta_v)*p_v*math.exp(eta*dr); rhs_a = (beta_h-beta_f)*p_h
    excl_ampA += abs(lhs_a-rhs_a) <= 1e-9; nb_ampA_vrai += lhs_a > rhs_a
    l = eta*(beta_f*dr-(beta_h-beta_f)*c); r = math.log(p_h/p_f)
    excl_domB += abs(l-r) <= 1e-9; nb_domB_vrai += l > r
    la = p_v*(1-math.exp(-eta*(beta_f-beta_v)*(dr+c)))
    ra = p_h*math.exp(-eta*dr)*(math.exp(eta*((1-beta_f)*dr+(beta_h-beta_f)*c))-1)
    excl_ampB += abs(la-ra) <= 1e-9; nb_ampB_vrai += la > ra
out["theoreme_1"] = dict(tirages=10_000, ecartes_tolerance_ampA=excl_ampA, ecartes_tolerance_domB=excl_domB,
    ecartes_tolerance_ampB=excl_ampB, ampA_vrai=nb_ampA_vrai, domB_vrai=nb_domB_vrai, ampB_vrai=nb_ampB_vrai,
    beta_f_min=round(min_bf,4), eta_max=round(max_eta,4), p_f_min=round(min_pf,5),
    ecart_min_beta_h_moins_beta_f=min_gap_fh, cas_beta_f_egal_beta_h=nb_bf_eq_bh,
    seuil_dominance_A_teste=False, R1_sous_A_teste=False, proposition_limites_testee=False)
# 2. niche
rng2 = random.Random(314159); excl = 0; inv_vrai = 0
for _ in range(2_000):
    bv = rng2.uniform(0.05, 0.90); eta = rng2.uniform(0.2, 5.0); dr = rng2.uniform(0.1, 3.0); c = rng2.uniform(0.0, 3.0)
    th = math.log(1/bv)/(1-bv); val = eta*(dr+c); excl += abs(val-th) <= 1e-9; inv_vrai += val > th
out["niche"] = dict(tirages=2000, priors_fixes=[0.70,0.25,0.05], ecartes=excl, inversion_vraie=inv_vrai)
# 3. R2 : structure du couplage
out["R2"] = dict(tirages=1000, atomes=4, loi_nu0="uniforme",
    couplage="beta_audit = rearrangement exactement anti-monotone de beta_loop (contre-monotonie parfaite)",
    identite_covariance_testee=False, independance_testee=False, cov_negative_sans_association_testee=False)
# 4. R3
rng4 = random.Random(161803); n_pass = 0; gaps = []; dtvs = []
for _ in range(1_000):
    base = [rng4.uniform(0.1, 1.0) for _ in range(6)]; sb = sum(base); po = [x/sb for x in base]
    pert = [max(1e-4, x+rng4.uniform(-0.03, 0.03)) for x in po]; sp = sum(pert); pt = [x/sp for x in pert]
    d = 0.5*sum(abs(a-b) for a, b in zip(po, pt)); pol = [1.0 if po[x] >= pt[x] else 0.0 for x in range(6)]
    to = sum(po[x]*pol[x] for x in range(6)); tt = sum(pt[x]*pol[x] for x in range(6))
    gaps.append(abs((to-tt)-d)); dtvs.append(d); n_pass += to > d+0.05
out["R3"] = dict(tirages=1000, politique="unique, extrémale 1{P_ord>=P_piege} (tau_ord - tau_piege = d_VT exactement)",
    ecart_max_borne_VT=max(gaps), d_VT_min=min(dtvs), d_VT_max=max(dtvs),
    tirages_passant_le_filtre_du_test_de_gain=n_pass,
    C_choisi="C* + 0,5 avec tau_min = tau_ord de la politique elle-meme",
    moniteur_ordinaire="aveugle (survie 1) seulement", survie_piege="exactement eps")
print(json.dumps(out, indent=2, ensure_ascii=False))

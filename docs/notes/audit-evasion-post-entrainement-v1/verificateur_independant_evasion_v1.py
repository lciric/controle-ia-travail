#!/usr/bin/env python3
"""Vérificateur indépendant de l'audit de la note et du manuscrit sur l'évasion
sous filtrage après post-entraînement (v1). Écrit sans réemployer le code de
verifier_exemples_papier_v2.py. Trois voies :
  1. preuve symbolique (sympy) de chaque équivalence algébrique ;
  2. arithmétique exacte (fractions.Fraction) là où les grandeurs sont
     rationnelles, et précision de 80 chiffres (mpmath) pour les exponentielles ;
  3. recherche adverse : domaines larges et extrêmes, points de bord exacts,
     programme linéaire exact pour le pire cas du régime des pièges plantés,
     et contre-exemples aux lectures qui dépassent les énoncés.
Graines : numpy.random.SeedSequence(20261124_0616), une sous-graine par tâche.
Usage : python -I verificateur_independant_evasion_v1.py CHEMIN_MANUSCRIT_TEX SORTIE_JSON
"""
from __future__ import annotations
import json, re, sys, platform
from fractions import Fraction as F
import numpy as np, sympy as sp, mpmath as mp, scipy
from scipy.optimize import linprog

mp.mp.dps = 80
RES: dict = {}
SS = np.random.SeedSequence(202611240616)
GRAINES = dict(zip(["bornes_A", "adverse_mp", "R2", "R3", "rendement_B"], SS.spawn(5)))
def rng(nom): return np.random.default_rng(GRAINES[nom])

# ---------- 1. Preuves symboliques ----------
def symbolique():
    ph, pv, pf, bh, bv, bf, E, eta, dR, C = sp.symbols("p_h p_v p_f b_h b_v b_f E eta dR C", positive=True)
    out = {}
    # 1.1 identité de variance (trois atomes, récompenses hétérogènes absorbées dans les poids w_i)
    w = sp.symbols("w1:4", positive=True); b = sp.symbols("b1:4", positive=True)
    Z = sum(w); m = sum(wi*bi for wi, bi in zip(w, b))/Z
    v = sum(wi*(bi-m)**2 for wi, bi in zip(w, b))/Z
    mpost = sum(wi*bi*bi for wi, bi in zip(w, b))/sum(wi*bi for wi, bi in zip(w, b))
    out["variance_identite_A"] = sp.simplify(mpost - m - v/m) == 0
    # 1.2 amplification absolue sous A : pi_A(f)-pi_no(f) = pf E [ (bf-bv) pv E - (bh-bf) ph ] / (D_A D_no)
    DA = bh*ph + (bv*pv + bf*pf)*E; Dn = ph + (pv+pf)*E
    diff = bf*pf*E/DA - pf*E/Dn
    out["amplification_A_factorisation"] = sp.simplify(diff - pf*E*((bf-bv)*pv*E - (bh-bf)*ph)/(DA*Dn)) == 0
    # 1.3 amplification absolue sous B : D_no' - D_B' = LHS - RHS de (eq:ampB)
    DBp = ph*sp.exp(-eta*(bf*dR-(bh-bf)*C)) + pv*sp.exp(-eta*(bf-bv)*(dR+C)) + pf
    Dnp = ph*sp.exp(-eta*dR) + pv + pf
    lhs = pv*(1-sp.exp(-eta*(bf-bv)*(dR+C))); rhs = ph*sp.exp(-eta*dR)*(sp.exp(eta*((1-bf)*dR+(bh-bf)*C))-1)
    out["amplification_B_equivalence"] = sp.simplify(sp.expand(Dnp - DBp - (lhs - rhs))) == 0
    # et la réécriture de pi_B(f) par division (poids d'origine)
    wh = ph*sp.exp(-eta*(1-bh)*C); wv = pv*sp.exp(eta*(bv*dR-(1-bv)*C)); wf = pf*sp.exp(eta*(bf*dR-(1-bf)*C))
    out["pi_B_f_reecriture"] = sp.simplify(wf/(wh+wv+wf) - pf/DBp) == 0
    # 1.4 cotes furtif/honnête sous B
    out["cote_B_f_sur_h"] = sp.simplify(sp.log(wf/wh) - (sp.log(pf/ph) + eta*(bf*dR-(bh-bf)*C))) == 0 or \
        sp.simplify(sp.expand_log(sp.log(wf/wh), force=True) - sp.expand_log(sp.log(pf/ph), force=True) - eta*(bf*dR-(bh-bf)*C)) == 0
    # 1.5 niche : poids visible B - poids visible A = pv e^{eta dR}(e^{-eta(1-bv)(dR+C)} - bv)
    wvB = pv*sp.exp(eta*(bv*dR-(1-bv)*C)); wvA = bv*pv*sp.exp(eta*dR)
    out["niche_difference_poids_visible"] = sp.simplify(wvB - wvA - pv*sp.exp(eta*dR)*(sp.exp(-eta*(1-bv)*(dR+C)) - bv)) == 0
    # 1.6 régime des pièges : f(tau_min) < 0  <=>  C > C*
    rho, eps, dl, tm = sp.symbols("rho epsilon delta tau", positive=True)
    f = (1-rho)*tm*dR + rho*(tm-dl)*(eps*dR-(1-eps)*C)
    Cstar = ((1-rho)*tm + rho*eps*(tm-dl))/(rho*(1-eps)*(tm-dl))*dR
    # f est affine en C, de pente -rho (tm-dl)(1-eps) < 0 et s'annule en C*
    out["R3_annulation_en_Cstar"] = sp.simplify(f.subs(C, Cstar)) == 0
    out["R3_pente_en_C"] = sp.simplify(sp.diff(f, C) + rho*(tm-dl)*(1-eps)) == 0
    # 1.7 identité de covariance (trois atomes)
    a = sp.symbols("a1:4", positive=True)
    Ea = sum(wi*ai for wi, ai in zip(w, a))/Z
    cov = sum(wi*bi*ai for wi, bi, ai in zip(w, b, a))/Z - m*Ea
    postA = sum(wi*bi*ai for wi, bi, ai in zip(w, b, a))/sum(wi*bi for wi, bi in zip(w, b))
    out["R2_identite_covariance_A"] = sp.simplify(postA - Ea - cov/m) == 0
    return out

# ---------- 2. Modèle à trois strates en grande précision ----------
def poids(p, beta, R, eta, op, C=0):
    ph, pv, pf = p; bh, bv, bf = beta; Rv, Rf = R
    if op == "no": w = [ph, pv*mp.e**(eta*Rv), pf*mp.e**(eta*Rf)]
    elif op == "A": w = [bh*ph, bv*pv*mp.e**(eta*Rv), bf*pf*mp.e**(eta*Rf)]
    else: w = [ph*mp.e**(-eta*(1-bh)*C), pv*mp.e**(eta*(bv*Rv-(1-bv)*C)), pf*mp.e**(eta*(bf*Rf-(1-bf)*C))]
    Z = sum(w); return [x/Z for x in w]

def criteres(p, beta, dR, eta, C):
    ph, pv, pf = p; bh, bv, bf = beta
    c = {}
    c["ampA"] = (bf-bv)*pv*mp.e**(eta*dR) - (bh-bf)*ph
    c["ampB"] = pv*(1-mp.e**(-eta*(bf-bv)*(dR+C))) - ph*mp.e**(-eta*dR)*(mp.e**(eta*((1-bf)*dR+(bh-bf)*C))-1)
    c["domA"] = dR - (mp.log(ph/pf) + mp.log(bh/bf))/eta
    c["domB"] = dR - ((bh-bf)/bf*C + mp.log(ph/pf)/(eta*bf))
    return c

def direct(p, beta, dR, eta, C):
    n = poids(p, beta, (dR, dR), eta, "no"); A = poids(p, beta, (dR, dR), eta, "A"); B = poids(p, beta, (dR, dR), eta, "B", C)
    return dict(ampA=A[2]-n[2], ampB=B[2]-n[2], domA=A[2]-A[0], domB=B[2]-B[0],
                condA=A[2]/(A[1]+A[2]) - n[2]/(n[1]+n[2]), condB=B[2]/(B[1]+B[2]) - n[2]/(n[1]+n[2]))

def tirage_large(g):
    # domaines larges : priors log-uniformes jusqu'à 1e-12, survies près de 0 et 1, eta de 1e-3 à 1e3
    lp = g.uniform(-12, 0, 3); q = 10**lp; q = q/q.sum()
    ph, pv, pf = [mp.mpf(float(x)) for x in q]
    mode = g.integers(0, 4)
    bh = mp.mpf(1) if mode == 0 else mp.mpf(float(1 - 10**g.uniform(-9, -0.05)))
    bf = bh if mode == 1 else bh*mp.mpf(float(10**g.uniform(-6, 0)))
    bv = mp.mpf(0) if mode == 2 else bf*mp.mpf(float(10**g.uniform(-8, 0)))*mp.mpf("0.999999")
    eta = mp.mpf(float(10**g.uniform(-3, 3))); dR = mp.mpf(float(10**g.uniform(-6, 2)))
    C = mp.mpf(0) if mode == 3 else mp.mpf(float(10**g.uniform(-4, 3)))
    return (ph, pv, pf), (bh, bv, bf), dR, eta, C

def recherche_adverse(n=40000):
    g = rng("adverse_mp"); viol = {k: 0 for k in ["ampA", "ampB", "domA", "domB", "condA", "condB", "inversion", "niche_chaine"]}
    bord = {k: 0 for k in viol}; testes = {k: 0 for k in viol}
    for _ in range(n):
        p, beta, dR, eta, C = tirage_large(g)
        bh, bv, bf = beta
        if not (bv < bf <= bh and bf > 0): continue
        d = direct(p, beta, dR, eta, C); c = criteres(p, beta, dR, eta, C)
        for k in ["ampA", "ampB", "domA", "domB"]:
            if k == "ampA" and bf == bh:
                testes[k] += 1; viol[k] += not (d[k] > 0); continue
            testes[k] += 1
            if abs(c[k]) < mp.mpf(10)**-60 or abs(d[k]) < mp.mpf(10)**-60: bord[k] += 1; continue
            viol[k] += (c[k] > 0) != (d[k] > 0)
        for k in ["condA", "condB"]:
            testes[k] += 1
            if abs(d[k]) < mp.mpf(10)**-60: bord[k] += 1; continue
            viol[k] += not (d[k] > 0)
    # niche parfaite : bf = bh = 1 > bv > 0
    for _ in range(n//4):
        lp = g.uniform(-12, 0, 3); q = 10**lp; q = q/q.sum(); p = tuple(mp.mpf(float(x)) for x in q)
        bv = mp.mpf(float(10**g.uniform(-9, -1e-6))); eta = mp.mpf(float(10**g.uniform(-3, 3)))
        dR = mp.mpf(float(10**g.uniform(-6, 2))); C = mp.mpf(float(10**g.uniform(-4, 3))) if g.random() < .9 else mp.mpf(0)
        n0 = poids(p, (1, bv, 1), (dR, dR), eta, "no"); A = poids(p, (1, bv, 1), (dR, dR), eta, "A"); B = poids(p, (1, bv, 1), (dR, dR), eta, "B", C)
        crit = eta*(dR+C) - mp.log(1/bv)/(1-bv)
        testes["inversion"] += 1; testes["niche_chaine"] += 1
        viol["niche_chaine"] += not (A[2] > n0[2])
        if abs(crit) < mp.mpf(10)**-60 or abs(B[2]-A[2]) < mp.mpf(10)**-70: bord["inversion"] += 1; continue
        viol["inversion"] += (crit > 0) != (B[2] > A[2])
    return dict(essais_testes=testes, desaccords=viol, ecartes_au_bord=bord)

def points_de_bord():
    """Aux seuils exacts, les deux membres doivent être égaux (à 1e-70 près)."""
    g = rng("bornes_A"); ecarts = {"ampA": [], "domA": [], "domB": [], "inversion": []}
    for _ in range(2000):
        q = g.dirichlet([1, 1, 1]); p = tuple(mp.mpf(float(x)) for x in q)
        bh = mp.mpf(float(g.uniform(.3, 1))); bf = bh*mp.mpf(float(g.uniform(.05, .95))); bv = bf*mp.mpf(float(g.uniform(0, .95)))
        eta = mp.mpf(float(10**g.uniform(-2, 2))); C = mp.mpf(float(g.uniform(0, 5)))
        ph, pv, pf = p
        s = (mp.log(ph/pv) + mp.log((bh-bf)/(bf-bv)))/eta
        if s > 0:
            n0 = poids(p, (bh, bv, bf), (s, s), eta, "no"); A = poids(p, (bh, bv, bf), (s, s), eta, "A"); ecarts["ampA"].append(abs(A[2]-n0[2]))
        s = (mp.log(ph/pf) + mp.log(bh/bf))/eta
        if s > 0:
            A = poids(p, (bh, bv, bf), (s, s), eta, "A"); ecarts["domA"].append(abs(A[2]-A[0]))
        s = (bh-bf)/bf*C + mp.log(ph/pf)/(eta*bf)
        if s > 0:
            B = poids(p, (bh, bv, bf), (s, s), eta, "B", C); ecarts["domB"].append(abs(B[2]-B[0]))
        bv2 = mp.mpf(float(g.uniform(.01, .99))); dR = mp.mpf(float(g.uniform(.01, 3)))
        Cx = mp.log(1/bv2)/(1-bv2)/eta - dR
        if Cx >= 0:
            A = poids(p, (1, bv2, 1), (dR, dR), eta, "A"); B = poids(p, (1, bv2, 1), (dR, dR), eta, "B", Cx); ecarts["inversion"].append(abs(B[2]-A[2]))
    return {k: dict(n=len(v), ecart_max=mp.nstr(max(v), 5) if v else None) for k, v in ecarts.items()}

def exact_A_rationnel(n=20000):
    """Sous A, tout ne dépend que de E = e^{eta dR} > 0 : vérification exacte en rationnels."""
    g = np.random.default_rng(GRAINES["bornes_A"].spawn(1)[0]); bad = 0; bord = 0
    for _ in range(n):
        d = [F(int(x)) for x in g.integers(1, 10**6, 3)]; s = sum(d); ph, pv, pf = [x/s for x in d]
        k = sorted(F(int(x), 10**6) for x in g.integers(0, 10**6+1, 3))
        bv, bf, bh = k
        if g.random() < .2: bh = bf
        if not (bv < bf <= bh and bf > 0): continue
        E = F(int(g.integers(1, 10**8)), int(g.integers(1, 10**4)))
        pA = bf*pf*E/(bh*ph + (bv*pv+bf*pf)*E); pn = pf*E/(ph + (pv+pf)*E)
        crit = (bf-bv)*pv*E - (bh-bf)*ph
        if crit == 0: bord += 1; bad += pA != pn; continue
        bad += (crit > 0) != (pA > pn)
        # cotes : pi_A(f)/pi_A(h) = bf pf E/(bh ph)
        bad += (bf*pf*E/(bh*ph+(bv*pv+bf*pf)*E)) / (bh*ph/(bh*ph+(bv*pv+bf*pf)*E)) != bf*pf*E/(bh*ph)
    return dict(essais=n, desaccords=bad, egalites_exactes_au_bord=bord)

# ---------- 3. Régime des pièges plantés : pire politique par programme linéaire exact ----------
def pire_gain_exact(c, w, t):
    """max sum c_x tau_x  s.c. sum w_x tau_x >= t, 0<=tau<=1 (sac à dos fractionnaire exact)."""
    tau = [F(1) if cx > 0 else F(0) for cx in c]
    masse = sum(wx*tx for wx, tx in zip(w, tau))
    if masse < t:
        reste = t - masse
        for i in sorted([i for i in range(len(c)) if tau[i] == 0], key=lambda i: c[i]/w[i], reverse=True):
            prend = min(F(1), reste/w[i]); tau[i] = prend; reste -= prend*w[i]
            if reste <= 0: break
        if reste > 0: return None, None
    return sum(cx*tx for cx, tx in zip(c, tau)), tau

def R3(n=3000):
    g = rng("R3"); viol = 0; testes = 0; plancher_positif = 0; plancher_testes = 0; cross = 0; sous_dvt = 0; sous_tmin = 0
    for _ in range(n):
        m = int(g.integers(2, 9))
        po = [F(int(x)) for x in g.integers(1, 1000, m)]; s = sum(po); po = [x/s for x in po]
        pt = [max(F(1, 10**6), x + F(int(y), 10**5)) for x, y in zip(po, g.integers(-3000, 3001, m))]; s = sum(pt); pt = [x/s for x in pt]
        dvt = sum(abs(a-b) for a, b in zip(po, pt))/2
        rho = F(int(g.integers(1, 99)), 100); eps = F(int(g.integers(0, 50)), 100); dR = F(int(g.integers(1, 500)), 100)
        if dvt >= 1: continue
        tmin = dvt + (1-dvt)*F(int(g.integers(1, 100)), 100)
        Cs = ((1-rho)*tmin + rho*eps*(tmin-dvt))/(rho*(1-eps)*(tmin-dvt))*dR
        C = Cs*(1 + F(int(g.integers(1, 200)), 1000))
        # moniteur ordinaire quelconque (survie s_o(x) dans [0,1]) et piège de survie s_t(x) <= eps
        so = [F(int(x), 100) for x in g.integers(0, 101, m)]; st = [eps*F(int(x), 100) for x in g.integers(0, 101, m)]
        # cas le plus défavorable au défenseur : moniteur ordinaire aveugle et survie piège = eps
        if g.random() < .5: so = [F(1)]*m; st = [eps]*m
        c = [(1-rho)*po[x]*(so[x]*dR-(1-so[x])*C) + rho*pt[x]*(st[x]*dR-(1-st[x])*C) for x in range(m)]
        best, tau = pire_gain_exact(c, po, tmin)
        if best is None: continue
        testes += 1; viol += not (best < 0)
        # contrôle croisé en flottants par scipy
        if testes <= 300:
            r = linprog([-float(x) for x in c], A_ub=[[-float(x) for x in po]], b_ub=[-float(tmin)], bounds=[(0, 1)]*m, method="highs")
            cross += abs(-r.fun - float(best)) > 1e-9
        # hors du champ du théorème : meilleure politique sans contrainte de taux (tau_x = 1 si c_x > 0)
        plancher_testes += 1
        pos = [x for x in range(m) if c[x] > 0]
        if pos:
            plancher_positif += 1
            t_opt = sum(po[x] for x in pos)
            sous_dvt += t_opt <= dvt
            sous_tmin += t_opt < tmin
    return dict(instances=testes, pire_gain_positif=viol, desaccords_scipy=cross,
                instances_meilleure_politique_libre=plancher_testes, meilleure_politique_libre_gain_positif=plancher_positif,
                dont_taux_ordinaire_au_plus_dVT=sous_dvt, dont_taux_ordinaire_sous_tau_min=sous_tmin)

# ---------- 4. Contre-exemples aux lectures qui dépassent les énoncés ----------
def contre_exemples():
    out = {}
    # 4.1 R2 sous B : covariance nulle, sans association négative -> la survie à l'audit monte
    bl = [F(1, 10), F(1, 2), F(9, 10)]; ba = [F(9, 10), F(1, 10), F(9, 10)]; w = [F(1, 3)]*3
    Eb = sum(x*y for x, y in zip(w, bl)); Ea = sum(x*y for x, y in zip(w, ba))
    cov = sum(x*y*z for x, y, z in zip(w, bl, ba)) - Eb*Ea
    k = mp.mpf(4)  # eta (dR + C)
    gB = [mp.e**(k*mp.mpf(x.numerator)/x.denominator) for x in bl]
    postB = sum(g_*mp.mpf(a.numerator)/a.denominator for g_, a in zip(gB, ba))/sum(gB)
    out["R2_B_cov_nulle"] = dict(cov_exacte=str(cov), E_audit_base=str(Ea), E_audit_apres_B=mp.nstr(postB, 12),
                                 hausse=mp.nstr(postB - mp.mpf(Ea.numerator)/Ea.denominator, 6))
    # 4.2 hors boucle n'implique pas covariance <= 0 : audit corrélé au filtre (traits partagés), sous A
    bl = [F(1, 10), F(9, 10)]; ba = [F(2, 10), F(8, 10)]; w = [F(1, 2)]*2
    Eb = sum(x*y for x, y in zip(w, bl)); Ea = sum(x*y for x, y in zip(w, ba))
    post = sum(x*y*z for x, y, z in zip(w, bl, ba))/Eb
    out["R2_A_audit_hors_boucle_correle"] = dict(E_audit_base=str(Ea), E_audit_apres_A=str(post), hausse=str(post-Ea))
    # 4.3 sous B, l'enrichissement conditionnel n'est pas universel quand la récompense varie parmi les tricheurs
    # deux tricheurs : (survie 1/2, récompense 1/100) et (survie 9/10, récompense 10), C = 0, eta = 3/10
    eta = mp.mpf("0.3"); C = mp.mpf(0)
    typ = [(mp.mpf("0.5"), mp.mpf("0.01")), (mp.mpf("0.9"), mp.mpf(10))]
    wno = [mp.e**(eta*R) for _, R in typ]; wB = [mp.e**(eta*(b*R-(1-b)*C)) for b, R in typ]
    Eno = sum(w_*b for w_, (b, _) in zip(wno, typ))/sum(wno); EB = sum(w_*b for w_, (b, _) in zip(wB, typ))/sum(wB)
    out["enrichissement_B_non_universel"] = dict(E_survie_sans_moniteur=mp.nstr(Eno, 10), E_survie_sous_B=mp.nstr(EB, 10))
    # 4.4 niche : chaque fois que B dépasse A en furtif, B dépasse aussi A en honnêteté (même cote f/h)
    g = rng("rendement_B"); n = 0; bad = 0
    for _ in range(5000):
        q = g.dirichlet([1, 1, 1]); p = tuple(mp.mpf(float(x)) for x in q)
        bv = mp.mpf(float(g.uniform(.01, .99))); eta = mp.mpf(float(10**g.uniform(-2, 2))); dR = mp.mpf(float(g.uniform(.01, 5))); C = mp.mpf(float(g.uniform(0, 10)))
        A = poids(p, (1, bv, 1), (dR, dR), eta, "A"); B = poids(p, (1, bv, 1), (dR, dR), eta, "B", C)
        if B[2] > A[2]:
            n += 1; # masse tricheuse totale = 1 - pi(h) : il suffit de comparer pi(h) (évite l'arrondi de 1 - 1e-167)
            bad += not (B[0] > A[0] and abs(B[2]/B[0] - A[2]/A[0]) <= mp.mpf(10)**-60*abs(A[2]/A[0]))
    out["niche_B_plus_honnete_aussi"] = dict(cas_ou_B_depasse_A_en_furtif=n, cas_contraires=bad)
    # 4.5 sensibilité au modèle : rejet répété T fois (filtre à chaque tour) -> barrière non évanescente
    ph, pf, bh, bf, eta1, dR = mp.mpf("0.85"), mp.mpf("0.01"), mp.mpf(1), mp.mpf("0.75"), mp.mpf("0.2"), mp.mpf("1.0")
    seuil = mp.log(bh/bf)/eta1
    lignes = []
    for T in [1, 10, 100, 1000]:
        cote_papier = mp.log(bf*pf/(bh*ph)) + T*eta1*dR               # opérateur A du papier à eta = T eta1
        cote_repete = mp.log(pf/ph) + T*(mp.log(bf/bh) + eta1*dR)       # filtre appliqué à chaque tour
        lignes.append(dict(T=T, eta=float(T*eta1), log_cote_A_papier=mp.nstr(cote_papier, 6), log_cote_A_repete=mp.nstr(cote_repete, 6)))
    out["sensibilite_rejet_repete"] = dict(seuil_non_evanescent_dR=mp.nstr(seuil, 6), dR=float(dR), lignes=lignes)
    # 4.5 bis R2 sous B, indépendance exacte : la survie à l'audit ne bouge pas (égalité), contrôle sain
    g2 = rng("R2"); ecart_ind = mp.mpf(0)
    for _ in range(500):
        k = int(g2.integers(2, 6)); bl = g2.uniform(0, 1, k); ql = g2.dirichlet([1]*k); ba = g2.uniform(0, 1, k); qa = g2.dirichlet([1]*k)
        kk = mp.mpf(float(g2.uniform(0, 20)))
        wl = [mp.mpf(float(q))*mp.e**(kk*mp.mpf(float(b))) for q, b in zip(ql, bl)]
        base = sum(mp.mpf(float(q))*mp.mpf(float(a)) for q, a in zip(qa, ba))
        post = sum(wl[i]*mp.mpf(float(qa[j]))*mp.mpf(float(ba[j])) for i in range(k) for j in range(k))/sum(wl)
        ecart_ind = max(ecart_ind, abs(post-base))
    out["R2_B_independance_controle_sain"] = dict(essais=500, ecart_max=mp.nstr(ecart_ind, 4))
    # 4.5 ter sous A, eta -> infini : la masse va aux tricheurs, pas forcément aux furtifs
    p = (F(49, 100), F(1, 2), F(1, 100)); be = (F(1), F(1, 2), F(3, 5))
    lim = be[2]*p[2]/(be[1]*p[1] + be[2]*p[2])
    A = poids(tuple(mp.mpf(x.numerator)/x.denominator for x in p), tuple(mp.mpf(x.numerator)/x.denominator for x in be), (1, 1), 200, "A")
    out["A_limite_part_furtive"] = dict(limite_exacte=str(lim), valeur=mp.nstr(lim.numerator/mp.mpf(lim.denominator), 6),
                                        pi_A_eta200=[mp.nstr(x, 6) for x in A])
    # 4.6 proposition des cas limites : rapport des seuils indéfini quand ph bh = pf bf
    out["proposition_rapport_indefini_si"] = "log(p_h/p_f) + log(beta_h/beta_f) = 0"
    return out

# ---------- 5. Tables du manuscrit recalculées indépendamment ----------
def tables(tex):
    T = open(tex, encoding="utf-8").read()
    def lignes(label):
        bloc = T.split("\\label{%s}" % label)[1].split("\\bottomrule")[0]
        rows = []
        for l in bloc.split("\\midrule")[1].strip().split("\\\\"):
            nums = re.findall(r"-?\d+\.\d+", l.replace("\\mathbf", ""))
            if nums: rows.append([mp.mpf(x) for x in nums])
        return rows
    p = (mp.mpf("0.85"), mp.mpf("0.14"), mp.mpf("0.01")); beta = (mp.mpf(1), mp.mpf("0.05"), mp.mpf("0.75")); C = mp.mpf("2.5")
    ecart = mp.mpf(0); n = 0
    for r in lignes("tab:deltaR"):
        dR = r[0]; n0 = poids(p, beta, (dR, dR), 3, "no"); A = poids(p, beta, (dR, dR), 3, "A"); B = poids(p, beta, (dR, dR), 3, "B", C)
        mien = [n0[2], n0[2]/(n0[1]+n0[2]), A[2], A[2]/(A[1]+A[2]), A[0], B[2], B[0]]
        for a, b in zip(mien, r[1:]): ecart = max(ecart, abs(a-b)); n += 1
    for r in lignes("tab:eta"):
        eta = r[0]; A = poids(p, beta, (mp.mpf("0.6"),)*2, eta, "A"); B = poids(p, beta, (mp.mpf("0.6"),)*2, eta, "B", C)
        for a, b in zip([A[0], A[2], B[0], B[2]], r[1:]): ecart = max(ecart, abs(a-b)); n += 1
    beta_n = (mp.mpf(1), mp.mpf("0.1"), mp.mpf(1))
    for r in lignes("tab:niche"):
        Cv = r[0]; n0 = poids(p, beta_n, (1, 1), 2, "no"); A = poids(p, beta_n, (1, 1), 2, "A"); B = poids(p, beta_n, (1, 1), 2, "B", Cv)
        for a, b in zip([2*(1+Cv), n0[2], A[2], B[2], B[0]], r[1:]): ecart = max(ecart, abs(a-b)); n += 1
    seuils = dict(
        dR_A=mp.nstr((mp.log(p[0]/p[1]) + mp.log((1-mp.mpf("0.75"))/(mp.mpf("0.75")-mp.mpf("0.05"))))/3, 10),
        dR_domA=mp.nstr((mp.log(p[0]/p[2]) + mp.log(1/mp.mpf("0.75")))/3, 10),
        dR_domB=mp.nstr(mp.mpf("0.25")/mp.mpf("0.75")*C + mp.log(p[0]/p[2])/(3*mp.mpf("0.75")), 10),
        niche_seuil=mp.nstr(mp.log(10)/mp.mpf("0.9"), 10), niche_C=mp.nstr(mp.log(10)/mp.mpf("0.9")/2-1, 10),
        R3_Cstar=str(F(16, 100)+F(6, 10000)) + " / " + str(F(294, 10000)) + " = " + mp.nstr(mp.mpf("0.1606")/mp.mpf("0.0294"), 10))
    R1 = poids((mp.mpf("0.9"), mp.mpf("0.09"), mp.mpf("0.01")), (1, mp.mpf("0.1"), mp.mpf("0.9")), (1, mp.mpf("-0.25")), 20, "B", 2)
    seuils["R1_pi_B_h"] = mp.nstr(R1[0], 10)
    rat = [F(1, 2), F(1, 3), F(1, 6)], [F(1, 10), F(2, 5), F(9, 10)]
    E0 = sum(a*b for a, b in zip(*rat)); V0 = sum(a*(b-E0)**2 for a, b in zip(*rat)); Ep = sum(a*b*b for a, b in zip(*rat))/E0
    seuils["exemple_rationnel"] = dict(E0=str(E0), Var0=str(V0), Epost=str(Ep), difference=str(Ep-E0), Var_sur_E=str(V0/E0))
    return dict(valeurs_comparees=n, ecart_max_a_la_table=mp.nstr(ecart, 4), seuils_recalcules=seuils)

if __name__ == "__main__":
    tex, sortie = sys.argv[1], sys.argv[2]
    RES["manifeste"] = dict(python=platform.python_version(), numpy=np.__version__, sympy=sp.__version__, mpmath=mp.__version__,
                            scipy=scipy.__version__, precision_chiffres=mp.mp.dps, graine_racine=202611240616)
    RES["1_symbolique"] = symbolique(); print("symbolique", RES["1_symbolique"], flush=True)
    RES["2a_exact_rationnel_A"] = exact_A_rationnel(); print(RES["2a_exact_rationnel_A"], flush=True)
    RES["2b_points_de_bord"] = points_de_bord(); print(RES["2b_points_de_bord"], flush=True)
    RES["2c_recherche_adverse"] = recherche_adverse(); print(RES["2c_recherche_adverse"], flush=True)
    RES["3_R3_pire_politique"] = R3(); print(RES["3_R3_pire_politique"], flush=True)
    RES["4_contre_exemples_lectures"] = contre_exemples(); print(json.dumps(RES["4_contre_exemples_lectures"], indent=1), flush=True)
    RES["5_tables"] = tables(tex); print(RES["5_tables"], flush=True)
    json.dump(RES, open(sortie, "w", encoding="utf-8"), indent=2, ensure_ascii=False, default=str)

"""Contre-lecture du code v5 — effet du couplage par blocs de 4 (texte scellé 3.3 a) sur la loi de la suite retenue et sur deux
composantes de l'épreuve du centrage de l'oracle à contexte réécrit (chaîne réécrite ; pente de fuite), sous l'hypothèse nulle.
Emploie les fonctions du code contre-lu (`couplage_v5.choisir`, `epreuve_centrage_v5`). Modèle de chaîne simplifié, en décades :
niveau de tâche N(0 ; 0,30) ; premier coût = niveau + N(0 ; 0,8) ; pas t ≥ 2 : niveau du contexte = a × dernier coût du contexte
+ (1 − a) × niveau de tâche + choc commun N(0 ; 0,22) + variation propre N(0 ; w) (indépendante dès que les contextes diffèrent) ;
tirage = niveau + s × bruit, s log-normal de médiane 0,08 (écart type logarithmique 0,85). Bruits : normal ; asymétrique
(log-normal réduit, asymétrie ≈ 1,7) ; arrondi (valeurs rondes 1-2-5 en décades). Régénérés : coût écrit multiplié par 10^δ
(loi de 2.1) et l'agent s'ancre dessus. Comparaison : bloc 4 (le code) et bloc 8 (une suite prise au hasard, loi exacte).
Entropie neuve, tirée une fois et imprimée. Appel : PYTHONPATH=ARBRE/src python3 ce_script.py [répétitions]"""
import math, sys, time
import numpy as np
from controle_ia.iib import couplage_v5 as cp
from controle_ia.iib import epreuve_centrage_v5 as ec

REP = int(sys.argv[1]) if len(sys.argv) > 1 else 200
ss = np.random.SeedSequence()
print(f"# entropie {ss.entropy} ; répétitions {REP} ; {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")
GRILLE = np.log10(np.array([m * 10.0 ** e for e in range(-3, 8) for m in (1, 2, 5)]))

def bruit(rng, n, forme):
    if forme == "asymetrique":
        z = rng.lognormal(0, 0.6, n); return (z - math.exp(0.18)) / math.sqrt((math.exp(0.36) - 1) * math.exp(0.36))
    return rng.normal(0, 1, n)

def arrondir(x, forme):
    x = np.atleast_1d(np.asarray(x, dtype=float))
    if forme != "arrondi":
        return x
    return GRILLE[np.abs(GRILLE[None, :] - x[:, None]).argmin(axis=1)]

def episode(rng, a, w, forme, bloc, regenere):
    mu = rng.normal(0, 0.30); x1 = float(arrondir(mu + rng.normal(0, 0.8), forme)[0])
    xa, xj, lignes = x1, x1, []
    for t in range(1, 10):
        c = rng.normal(0, 0.22); s = 0.08 * math.exp(0.85 * rng.normal())
        va = rng.normal(0, w); vj = va if t == 1 else rng.normal(0, w)
        ma = a * xa + (1 - a) * mu + c + va; mj = a * xj + (1 - a) * mu + c + vj
        d = float(arrondir(ma + s * bruit(rng, 1, forme)[0], forme)[0])
        su = arrondir(mj + s * bruit(rng, 8, forme), forme)
        if regenere and rng.random() >= 0.2:
            while True:
                de = rng.normal(math.log10(2), 0.10)
                if de <= math.log10(2.5): break
            d = d + de
        lin = [10.0 ** v for v in su]
        ch = cp.choisir(lin, 10.0 ** d, rng, bloc)
        xr = math.log10(lin[ch["indice"]])
        est = sorted(lin)[3]
        lignes.append({"pas": t, "episode": None, "phase": None, "bornable": True, "cout_declare": 10.0 ** d,
                       "suites": [{"valeur": v, "lisible": True} for v in lin], "estimation": est,
                       "dernier_cout_contexte": 10.0 ** xj, "dernier_cout_agent": 10.0 ** xa, "_retenue": xr, "_rang9": None})
        # rang de la retenue parmi les neuf valeurs réunies (coût + huit suites)
        reun = sorted([d] + list(su)); lignes[-1]["_rang9"] = int(np.searchsorted(reun, xr, side="left"))
        xa, xj = d, xr
    return lignes

def un_etalonnage(rng, a, w, forme, bloc):
    H, Rg = [], []
    for e in range(64):
        for regen, L in ((False, H), (True, Rg)):
            ls = episode(rng, a, w, forme, bloc, regen)
            for l in ls:
                l["episode"] = f"e{e}"; l["phase"] = "r" if regen else "h"
            L.extend(ls)
    cr = ec.composante_chaine_reecrite(H, 5, 32)
    pf = ec.composante_pente_de_fuite(H, Rg, 320)
    return cr["probabilite"], pf["probabilite"], H

print("forme\tancrage\tw\tbloc\tchaine_reecrite_arrete_1/80\tpente_de_fuite_arrete_1/80\tl_une_des_deux\tvariance_retenue/variance_suite(pas 2)\tpart_rang_milieu_sur_9(pas 2)")
for forme in ("normal", "asymetrique", "arrondi"):
    for a, w in ((0.9, 0.14), (0.9, 0.0)):
        for bloc in (4, 8):
            rng = np.random.default_rng(ss.spawn(1)[0])
            n_cr = n_pf = n_un = 0; vr, vs, milieu, n2 = [], [], 0, 0
            for _ in range(REP):
                pcr, ppf, H = un_etalonnage(rng, a, w, forme, bloc)
                r1, r2 = (pcr is not None and pcr < 1 / 80), (ppf is not None and ppf < 1 / 80)
                n_cr += r1; n_pf += r2; n_un += (r1 or r2)
                for l in H:
                    if l["pas"] == 1:
                        su = np.log10([s["valeur"] for s in l["suites"]]); m = su.mean()
                        sd = su.std()
                        if sd > 0: vr.append((l["_retenue"] - m) / sd); vs.append((su[0] - m) / sd); n2 += 1; milieu += (l["_rang9"] == 4)
            print(f"{forme}\t{a}\t{w}\t{bloc}\t{n_cr / REP:.3f}\t{n_pf / REP:.3f}\t{n_un / REP:.3f}\t{np.var(vr) / np.var(vs):.3f}\t{milieu / n2:.3f}", flush=True)

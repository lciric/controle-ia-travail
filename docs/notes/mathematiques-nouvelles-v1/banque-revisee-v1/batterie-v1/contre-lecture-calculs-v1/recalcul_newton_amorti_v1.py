"""Contre-lecture de la batterie (v2) — la sonde des nombres avec un Newton amorti, et le compte des non-convergences
du Newton pur de la lettre du § 2.2 — v1. Même banc que `recalcul_ecarts_1_2_v1.py` (importé, même dossier).
Emploi : python3 -I recalcul_newton_amorti_v1.py SORTIE.json > SORTIE.txt
"""
import json, sys, os, warnings
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import recalcul_ecarts_1_2_v1 as m
warnings.simplefilter("ignore")
COMPTE = {"fits": 0, "non_converges_newton_pur": 0}

def perte(w, Z, y): s = Z @ w; return float(np.sum(np.logaddexp(0, s) - y * s) + .5 * w @ w)

def logistique_controlee(X, y, lam=1.0):
    mu = X.mean(0); sd = X.std(0); nul = sd == 0; sd[nul] = 1
    Z = (X - mu) / sd; Z[:, nul] = 0; Z = np.hstack([np.ones((len(Z), 1)), Z])
    # 1) Newton pur, lettre du § 2.2 : on compte seulement s'il converge en 50 pas
    w = np.zeros(Z.shape[1]); ok = False
    for _ in range(50):
        p = 1 / (1 + np.exp(-(Z @ w))); g = Z.T @ (p - y) + lam * w
        H = (Z * (p * (1 - p))[:, None]).T @ Z + lam * np.eye(len(w)); pas = np.linalg.solve(H, g); w -= pas
        if not np.all(np.isfinite(w)): break
        if np.abs(pas).max() < 1e-10: ok = True; break
    COMPTE["fits"] += 1; COMPTE["non_converges_newton_pur"] += (not ok)
    # 2) Newton amorti (pas divisé par deux tant que la perte pénalisée ne baisse pas), 200 pas au plus
    w = np.zeros(Z.shape[1]); ok2 = False
    for _ in range(200):
        p = 1 / (1 + np.exp(-(Z @ w))); g = Z.T @ (p - y) + lam * w
        H = (Z * (p * (1 - p))[:, None]).T @ Z + lam * np.eye(len(w)); pas = np.linalg.solve(H, g); t = 1.0; f0 = perte(w, Z, y)
        while perte(w - t * pas, Z, y) > f0 - 1e-4 * t * float(g @ pas) and t > 1e-12: t /= 2
        w = w - t * pas
        if np.abs(t * pas).max() < 1e-10: ok2 = True; break
    assert ok2, "Newton amorti non convergé"
    def score(Xt):
        Zt = (Xt - mu) / sd; Zt[:, nul] = 0
        return np.round(np.hstack([np.ones((len(Zt), 1)), Zt]) @ w, 10)
    return score

m.logistique = logistique_controlee

def main(chemin):
    out = {}
    for nom, var, dose in [("saine", "saine", 1.0), ("grandeur_1", "grandeur", 1.0), ("grandeur_0.25", "grandeur", 0.25),
                           ("relation_1", "relation", 1.0), ("relation_0.5", "relation", 0.5)]:
        COMPTE.update(fits=0, non_converges_newton_pur=0)
        B = {r: m.construire(r, var, dose) for r in m.RACINES}
        S = m.sonde_par_squelette_autres_racines(B)
        res = m.resume([m.exces(B[r][1], S[r], "prorata") for r in m.RACINES], 2)
        out[nom] = dict(nombres_par_squelette_newton_amorti=res, **COMPTE)
        print(nom, out[nom]); sys.stdout.flush()
    json.dump(out, open(chemin, "w"), indent=1, ensure_ascii=False)

if __name__ == "__main__":
    main(sys.argv[1])

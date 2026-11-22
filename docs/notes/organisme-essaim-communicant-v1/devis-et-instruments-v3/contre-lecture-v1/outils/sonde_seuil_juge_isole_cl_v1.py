"""Épreuve près du seuil du test de mort, sous le JUGE ISOLÉ (processus neuf), par le contre-lecteur.
Cartes : loi plantée du monde mêlée à l'uniforme (transformee/melange_aveugle, lambda réglé par bissection) pour viser des gains
vrais contre la marginale de 0,010 à 0,040. Gain vrai : espérance exacte sur 200 000 instances (côté parent, fournisseur).
20 tranches neuves de 400 épisodes par monde (SeedSequence(20261199)). Mesures : (1) écart juge isolé / règle en processus sur les
mêmes tranches ; (2) taux de survie par gain visé ; (3) accord avec le verdict « vrai » (gain ≥ 0,02).
Usage : python -I -B sonde_seuil_juge_isole_cl_v1.py DOSSIER_V3 DOSSIER_TRAVAIL_NEUF SORTIE.json [MONDES…]"""
import json, os, sys
V3, TRAV, OUT = sys.argv[1:4]
MONDES = [int(x) for x in sys.argv[4:]] or list(range(12))
sys.path.insert(0, V3)
import numpy as np
import test_de_mort_programme_v2 as T2
T2.geler_juge()
B, M = T2.B, T2.M
os.makedirs(TRAV, exist_ok=False)
CIBLES = (0.010, 0.015, 0.018, 0.020, 0.022, 0.025, 0.030, 0.040)
RAC = 20261199
def rng(*k): return np.random.default_rng(np.random.SeedSequence(RAC, spawn_key=tuple(k)))
def carte(W, lam, K):
    return {"type": "transformee", "base": W, "melange_aveugle": {"lambda": float(lam), "probas": [1.0] * K}}
def gain_vrai(loi, Pw, Z, G):
    Pc = np.maximum(M.probas(loi, Z, G), M.PLANCHER); m = Pw.mean(axis=0)
    return float(np.mean(np.sum(Pw * (np.log(Pc) - np.log(m)), axis=1)))
res = {"graines": f"SeedSequence({RAC}, spawn_key=(r, ...))", "cibles": CIBLES, "mondes": {}}
for r in MONDES:
    spec, _ = B.regenerer(r); W = M.compiler_monde(spec); D, nsp = spec["dimension"], spec["sous_populations"]
    Z, G = M.tirer_instances(rng(r, 0), 200000, D, nsp); Pw = M.probas(W, Z, G); K = Pw.shape[1]
    Wj = T2.vers_json(W)
    g1 = gain_vrai(Wj, Pw, Z, G)
    cartes = []
    for c in CIBLES:
        if g1 < c: continue
        lo, hi = 0.0, 1.0
        for _ in range(40):
            mid = (lo + hi) / 2
            (lo, hi) = (mid, hi) if gain_vrai(carte(Wj, mid, K), Pw, Z, G) > c else (lo, mid)
        lam = (lo + hi) / 2
        cartes.append({"nom": f"cible-{c:.3f}", "loi": carte(Wj, lam, K), "gain_vrai": gain_vrai(carte(Wj, lam, K), Pw, Z, G), "lambda": lam})
    ch = os.path.join(TRAV, f"tranches-sonde-monde-{r}.json")
    sha = T2.fournir_tranches(W, D, nsp, {f"rep-{q}": rng(r, 1, q) for q in range(20)}, ch)
    v = T2.juger_isole([{"nom": c["nom"], "loi": c["loi"]} for c in cartes], ch, sha, TRAV, f"sonde-{r}")
    tr = json.load(open(ch))["tranches"]
    out = {"gain_loi_du_monde": g1}
    for c in cartes:
        ecarts, surv, accord = [], 0, 0
        vrai = "survit" if c["gain_vrai"] >= 0.02 else "éliminée"
        for q in range(20):
            t = tr[f"rep-{q}"]; Zt, Gt, Yt = np.asarray(t["Z"], float), np.asarray(t["G"], int), np.asarray(t["Y"], int)
            P = M.probas(c["loi"], Zt, Gt); cc = np.bincount(Yt, minlength=P.shape[1]) + 0.5; mg = cc / cc.sum()
            s = float(np.mean(np.log(np.maximum(P[np.arange(len(Yt)), Yt], M.PLANCHER)) - np.log(mg[Yt])))
            x = v[c["nom"]][f"rep-{q}"]
            ecarts.append(abs(s - x["statistique"])); surv += x["verdict"] == "survit"; accord += x["verdict"] == vrai
        out[c["nom"]] = {"gain_vrai": round(c["gain_vrai"], 5), "lambda": round(c["lambda"], 5), "survie_sur_20": surv,
                         "accord_verdict_vrai_sur_20": accord, "ecart_max_isole_vs_en_processus": max(ecarts)}
    res["mondes"][str(r)] = out
    print(r, {k: (v_["survie_sur_20"] if isinstance(v_, dict) else round(v_, 4)) for k, v_ in out.items()}, flush=True)
tot = {}
for r, o in res["mondes"].items():
    for k, x in o.items():
        if isinstance(x, dict):
            t = tot.setdefault(k, [0, 0, 0, 0.0]); t[0] += x["survie_sur_20"]; t[1] += 20; t[2] += x["accord_verdict_vrai_sur_20"]; t[3] = max(t[3], x["ecart_max_isole_vs_en_processus"])
res["agrege"] = {k: {"survie": f"{a}/{n}", "accord_verdict_vrai": f"{c}/{n}", "ecart_max": e} for k, (a, n, c, e) in sorted(tot.items())}
print(json.dumps(res["agrege"], ensure_ascii=False, indent=1))
json.dump(res, open(OUT, "x"), ensure_ascii=False, indent=1, sort_keys=True)

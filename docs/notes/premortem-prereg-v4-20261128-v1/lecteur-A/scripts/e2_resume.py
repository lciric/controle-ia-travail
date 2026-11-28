"""E2 — resume des mondes plantes : taux de l'issue « tenue » par scenario, regle ecrite et variante sans les predicteurs de
cout, avec intervalle de Wilson a 95 % ; critere de mort (plus de 5 % sous un nul ; moins de 50 % a 0,65)."""
import glob, json, math, os, sys
import numpy as np
S = sys.argv[1]
def wilson(k, n, z=1.96):
    if n == 0: return (float("nan"), float("nan"))
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)
res = {}
for f in sorted(glob.glob(os.path.join(S, "e2", "*.jsonl"))):
    L = [json.loads(l) for l in open(f, encoding="utf-8")]
    if not L: continue
    nom = os.path.basename(f)[:-6]
    n = len(L); ke = sum(d["tenue_regle_ecrite"] for d in L); kv = sum(d["tenue_variante_sans_cout"] for d in L)
    s0 = [d["sondes"][0] for d in L]
    q1 = [s["D"]["1"]["q95"] for s in s0 if "D" in s]; q3 = [s["D"]["3"]["q95"] for s in s0 if "D" in s and "3" in s["D"]]
    res[nom] = {"mondes": n, "tenue_regle_ecrite": ke / n, "ic95_ecrite": wilson(ke, n), "tenue_variante_sans_cout": kv / n, "ic95_variante": wilson(kv, n),
                "aire_sonde_1_jeu_1_moyenne": float(np.mean([s["a"]["1"] for s in s0])), "aire_sonde_1_jeu_1_ecart_type": float(np.std([s["a"]["1"] for s in s0])),
                "separation_cout_jeu_1": float(np.mean([max(d["sep_triviaux"]["1"]["log_cout"], d["sep_triviaux"]["1"]["cout_centre"]) for d in L])),
                "separation_cout_jeu_3": float(np.mean([max(d["sep_triviaux"]["3"]["log_cout"], d["sep_triviaux"]["3"]["cout_centre"]) for d in L])),
                "separation_longueur_jeu_1": float(np.mean([d["sep_triviaux"]["1"]["longueur"] for d in L])),
                "quantile_plancher_jeu_1": float(np.mean(q1)) if q1 else None, "quantile_plancher_jeu_3": float(np.mean(q3)) if q3 else None,
                "sondes_arretees_aux_predicteurs_triviaux_3": float(np.mean([not s["triviaux_3"] for d in L for s in d["sondes"]])),
                "secondes_mediane": float(np.median([d["secondes"] for d in L]))}
nuls = {k: v for k, v in res.items() if k.startswith("nul_")}
res["_criteres"] = {
    "plus_de_5pc_sous_un_nul_(regle_ecrite)": {k: v["tenue_regle_ecrite"] for k, v in nuls.items()},
    "plus_de_5pc_sous_un_nul_(variante)": {k: v["tenue_variante_sans_cout"] for k, v in nuls.items()},
    "nul_rejet_inegal": "simule comme un deplacement induit par la selection, de meme forme qu'un signal : son taux est celui de l'alternative de meme aire (alt_0.55, alt_0.60, alt_0.65)",
    "puissance_a_0_65": {k: {"ecrite": v["tenue_regle_ecrite"], "variante": v["tenue_variante_sans_cout"]} for k, v in res.items() if k.startswith("alt_0.65")}}
print(json.dumps(res, ensure_ascii=False, indent=1))

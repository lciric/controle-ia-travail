"""v03 — registre de dépense de la course (lecteur du verdict, R13) : appels par fournisseur, codes, heures ; arrêt fautif
de 10:39 ; 502 (code 5) ; fin des appels d'Argon ; dernier appel Kimi ; écart avec la sortie (appels absents du registre) ;
durées des appels Kimi au relais et ordre de grandeur de la durée du bras Kimi au plan gelé (contrefactuel, déclaré).
Usage : python3 -I -B v03_registre.py REGISTRE.jsonl SORTIE.json RELAIS_KIMI_V1.jsonl RELAIS_KIMI_V2.jsonl SORTIE_JSON"""
import json
import statistics
import sys
from collections import Counter, defaultdict
from datetime import datetime

reg = [json.loads(l) for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
sortie = json.load(open(sys.argv[2], encoding="utf-8"))
relais = [json.loads(l) for f in sys.argv[3:5] for l in open(f, encoding="utf-8") if l.strip()]

debuts = {e["id"]: e for e in reg if e["type"] == "debut"}
fins = {e["id"]: e for e in reg if e["type"] == "fin"}
autres = Counter(e["type"] for e in reg if e["type"] not in ("debut", "fin"))
t = lambda s: datetime.fromisoformat(s.replace("Z", "+00:00"))  # noqa: E731
appels = []
for i, d in debuts.items():
    f = fins.get(i)
    appels.append({"f": d["fournisseur"], "debut": t(d["quand_utc"]), "fin": t(f["quand_utc"]) if f else None,
                   "code": f["code"] if f else None, "statut": f["statut"] if f else None,
                   "cout": f["cout_usd"] if f else None, "origine": f.get("cout_origine") if f else None})
appels.sort(key=lambda a: a["debut"])
par = defaultdict(list)
for a in appels:
    par[a["f"]].append(a)

res = {"lignes": len(reg), "debuts": len(debuts), "fins": len(fins), "autres_types": dict(autres),
       "sans_fin": sum(a["fin"] is None for a in appels)}
for f, L in par.items():
    res[f] = {"appels": len(L), "codes": dict(Counter(a["code"] for a in L)),
              "origines": dict(Counter(a["origine"] for a in L)), "cout": round(sum(a["cout"] or 0 for a in L), 6),
              "premier_debut": L[0]["debut"].isoformat(), "dernier_debut": L[-1]["debut"].isoformat(),
              "derniere_fin": max(a["fin"] for a in L if a["fin"]).isoformat()}
k = par["kimi"]
# arrêt fautif : appels Kimi en code 3 entre 10:39:00 et 10:41:00
fen = [a for a in k if a["code"] == 3 and "10:39:00" <= a["fin"].strftime("%H:%M:%S") <= "10:41:00"]
res["kimi_code3_fenetre_1039_1041"] = {"n": len(fen), "origines": dict(Counter(a["origine"] for a in fen)),
                                       "premiere_fin": min(a["fin"] for a in fen).isoformat(),
                                       "derniere_fin": max(a["fin"] for a in fen).isoformat(),
                                       "pire_cas": [(a["fin"].isoformat(), a["cout"]) for a in fen if a["cout"] > 1e-3]}
res["kimi_code5"] = [(a["debut"].isoformat(), a["fin"].isoformat(), round((a["fin"] - a["debut"]).total_seconds(), 1), a["cout"])
                     for a in k if a["code"] == 5]
res["kimi_ok"] = [(a["debut"].isoformat(), a["fin"].isoformat(), round((a["fin"] - a["debut"]).total_seconds(), 1), a["cout"])
                  for a in k if a["code"] == 0]
res["argon_echecs"] = [(a["debut"].isoformat(), a["fin"].isoformat(), a["code"], a["cout"]) for a in par["argon"] if a["code"] != 0]
res["kimi_debuts_apres_122314"] = sum(1 for a in k if a["debut"].strftime("%H:%M:%S") > "12:23:14")
# sortie : appels par fournisseur
sortie_appels = Counter(s["fournisseur"] for s in sortie["suites"] for x in s["tentatives"] for _ in x["appels"])
res["sortie_appels"] = dict(sortie_appels)
res["absents_du_registre"] = {f: sortie_appels[f] - len(par[f]) for f in sortie_appels}
res["sortie_cout"] = sortie["depense_par_fournisseur_usd"]
# relais Kimi : durées
dur = [r["duree_s"] for r in relais]
res["relais_kimi"] = {"entrees": len(relais), "succes": sum("statut_amont" in r for r in relais),
                      "echecs_502": sum(r.get("statut") == 502 for r in relais), "durees_s": dur,
                      "duree_moyenne_s": round(statistics.mean(dur), 1), "duree_mediane_s": round(statistics.median(dur), 1),
                      "jetons_sortie_succes": [r["usage"]["completion_tokens"] for r in relais if "usage" in r],
                      "cout_relais": round(sum(r["cout_usd"] for r in relais), 6)}
# contrefactuel déclaré : appels Kimi attendus au devis (section 12 : W1 36 à 48, W2 12 à 40 par unité ; 12 unités Kimi
# par monde) à la durée moyenne observée au relais, en série dans le fil Kimi ; plafond de durée 20 h.
bas, haut = 12 * 36 + 12 * 12, 12 * 48 + 12 * 40
m = statistics.mean(dur)
res["contrefactuel_duree_bras_kimi_h"] = {"appels_attendus": [bas, haut], "heures": [round(bas * m / 3600, 1), round(haut * m / 3600, 1)],
                                          "plafond_h": 20, "appels_kimi_tenant_en_20h": int(72000 // m)}
json.dump(res, open(sys.argv[5], "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
print(json.dumps(res, ensure_ascii=False, indent=1, default=str))

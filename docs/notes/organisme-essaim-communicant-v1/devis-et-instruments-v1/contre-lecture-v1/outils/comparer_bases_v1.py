"""Compare la sortie publiée des bases et la sortie rejouée (hors horodatages) ; extrait les chiffres de la note.
Usage : comparer_bases_v1.py PUBLIEE.json REJOUEE.json"""
import json, sys
import statistics as st

a = json.load(open(sys.argv[1], encoding="utf-8"))
b = json.load(open(sys.argv[2], encoding="utf-8"))
for k in sorted(set(a) | set(b)):
    if k in ("debut_utc", "fin_utc"):
        continue
    print("cle", k, "IDENTIQUE" if a.get(k) == b.get(k) else "DIVERGE")
print("python/numpy publies :", a["python"], a["numpy"], "| rejoues :", b["python"], b["numpy"])
print("controles_tenus :", a["controles_tenus"])
print(json.dumps(a["resume"], ensure_ascii=False, indent=1))
pm = a["par_monde"]
print("B3 par monde :", [pm[str(r)]["B3-glouton-borne"]["couverture"] for r in range(12)])
ok = {"gabarit": 12}
print("attribution identique :", sum(pm[str(r)]["controles"]["attribution_identique"] for r in range(12)),
      "| ecart max :", max(pm[str(r)]["controles"]["ecart_max_attribution_cache_contre_reference"] for r in range(12)))
print("K1 fausse :", sum(pm[str(r)]["controles"]["K1"]["attendu_fausse"] for r in range(12)))
print("loi du monde :", [(r, pm[str(r)]["controles"]["loi_du_monde"]["attendu_vraie_et_toutes_non_latentes"]) for r in range(12)])
print("candidats glouton par generation :", [[t["candidats"] for t in pm[str(r)]["trajet_glouton"]] for r in range(12)])
c = [t["candidats"] for r in range(12) for t in pm[str(r)]["trajet_glouton"]]
print("candidats moyenne / mediane :", round(st.mean(c), 1), st.median(c))
for base in ("B1-uniforme", "B2-K1-plus-un-effet-au-hasard", "B3-glouton-borne"):
    print(base, "cartes par monde :", sorted({pm[str(r)][base]["cartes"] for r in range(12)}))

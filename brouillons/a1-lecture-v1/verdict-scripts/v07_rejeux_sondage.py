"""v07 — sondage des rejeux (lecteur du verdict, R13) : rejoue par le code gelé (`ag._rejouer_loi`, mêmes graines) les
entrées d'audit A2 des deux lois promues de W1, de deux lois promues de W2 (dont celle à 187/200), et l'entrée de rejeu
de W1 sous v8 au plus haut taux ; compare au nombre de promotions écrit. Lecture seule du code gelé.
Usage : python3 -I -B v07_rejeux_sondage.py ORCHESTRATOR SORTIE.json MANIFESTE.json SORTIE_JSON"""
import json
import sys
import time

sys.dont_write_bytecode = True
sys.path.insert(0, sys.argv[1])
import pole.attaque_goodhart_v2 as ag  # noqa: E402

sortie = json.load(open(sys.argv[2], encoding="utf-8"))
E = int(json.load(open(sys.argv[3], encoding="utf-8"))["reglages"]["entropie_racine"])
lois = {}
for s in sortie["suites"]:
    e = ag.etiquette_suite(s["monde"], s["fournisseur"], s["condition"], s["juge"])
    for t in s["tentatives"]:
        if t["loi"] is not None:
            lois[(s["monde"], s["carte"], e, t["k"])] = (t["loi"], s["juge"])
a2 = sortie["audit_A2"]
choix = [r for r in a2 if r["monde"] == "W1"]
w2 = [r for r in a2 if r["monde"] == "W2"]
choix += [min(w2, key=lambda r: r["promues"]), w2[0]]
rej_w1 = [r for r in sortie["rejeux"] if r["monde"] == "W1" and r["juge"] == "v8"]
choix += [max(rej_w1, key=lambda r: r["promues"])]
res = []
for r in choix:
    loi, juge = lois[(r["monde"], r["carte"], r["etiquette"], r["k"])]
    d = time.time()
    x = ag._rejouer_loi((E, r["monde"], r["carte"], r["etiquette"], r["k"], loi, r["juge"], r["rejeux"], r["prefixe"]))
    res.append({"prefixe": r["prefixe"], "etiquette": r["etiquette"], "carte": r["carte"], "k": r["k"],
                "ecrit": [r["promues"], r["rejeux"]], "rejoue": [x["promues"], x["rejeux"]],
                "egal": x["promues"] == r["promues"] and x["rejeux"] == r["rejeux"]
                and x["evaluations_impossibles"] == r["evaluations_impossibles"], "secondes": round(time.time() - d, 1)})
    print(res[-1], flush=True)
json.dump({"sondage": res, "tous_egaux": all(x["egal"] for x in res)}, open(sys.argv[4], "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("tous égaux :", all(x["egal"] for x in res))

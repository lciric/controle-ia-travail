"""Ajout déclaré après la première exécution de la démonstration (exploratoire) : le bras « v3 souple » (juge v1, nul des
filles v2 sans le produit des parents, tirage stratifié), mêmes graines 1 à 20, pour éclairer la décision n° 1."""
import json, os, sys, time
V3 = sys.argv[1]
sys.path.insert(0, V3); sys.path.insert(0, os.path.join(V3, "demonstrations"))
import demo_cycle_v3 as d
d.BRAS["v3_souple"] = {"juge": "v1", "nul_filles": "v2_souple", "tirage_recombinaison": "stratifie"}
sortie = sys.argv[2]
os.makedirs(sortie, exist_ok=False)
quand = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
liste = [d.une_course(g, "v3_souple", os.path.join(sortie, "courses", f"graine-{g:02d}-v3_souple"), 4, 0.4, quand)
         for g in range(1, 21)]
somme = {k: sum(x[k] for x in liste) for k in liste[0] if isinstance(liste[0][k], int)}
for k in ("temoins_faux_testes", "temoins_vrais_testes", "fausses_gardees", "vraies_eliminees"):
    somme[k] = sum(x["qualite_temoins"][k] for x in liste)
somme["part_triviales_promues"] = somme["triviales_promues"] / somme["triviales_testees"] if somme["triviales_testees"] else None
somme["part_autres_vraies_promues"] = somme["autres_promues_vraies"] / somme["autres_vraies_testees"] if somme["autres_vraies_testees"] else None
json.dump({"horodatage": quand, "bras": "v3_souple", "total": somme, "par_course": liste}, open(os.path.join(sortie, "bras-souple-v1.json"), "w"), ensure_ascii=False, indent=1)
print(json.dumps(somme, ensure_ascii=False, indent=1))

"""Ajout déclaré après la première exécution de la démonstration C (exploratoire) : le bras « sans mémoire » (mémoire
inactive : aucune garde de redite, aucun héritage), mêmes graines 1 à 20, six générations. Motif : dans les trois bras
d'origine, la garde prédictive refuse la redite d'une survivante quelle que soit la politique ; seul un bras sans mémoire
peut montrer le défaut que la garde empêche (découvertes en double)."""
import json, os, sys, time
V4 = sys.argv[1]
sys.path.insert(0, V4); sys.path.insert(0, os.path.join(V4, "demonstrations"))
import demo_cycle_v4 as d
from pole import pole as module_pole
sortie = sys.argv[2]
os.makedirs(sortie, exist_ok=False)
originale = module_pole.executer_pole
def sans_memoire(*a, **k):
    k["memoire_active"] = False
    return originale(*a, **k)
d.executer_pole = sans_memoire
bras = dict(d.EXPERIENCES["C"]["rien"])
quand = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
liste = [d.une_course(g, bras, os.path.join(sortie, "courses", f"graine-{g:02d}-sans-memoire"), 6, quand) for g in range(1, 21)]
somme = {k: sum(x[k] for x in liste) for k in liste[0]}
json.dump({"horodatage": quand, "bras": "sans_memoire", "total": somme, "par_course": liste},
          open(os.path.join(sortie, "bras-sans-memoire-v1.json"), "w"), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in somme.items() if v}, ensure_ascii=False))

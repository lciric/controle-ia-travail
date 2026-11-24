"""Essai hors réseau du collisionneur v9-v8r : garde d'entrée de l'arrière-plan et rejugement, sur des COPIES de dossiers.
Usage : PYTHONPATH=src python3 -B essai_rejugement_arriere_plan_v8r_v1.py COPIE ESPECES(virgules) CELLULE N [sortie_max effort_max]"""
import importlib.util, sys
sys.path.insert(0, "src")
spec = importlib.util.spec_from_file_location("c", "docs/notes/collisionneur-v9/collisionneur_v9_v8r.py")
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
D, especes, cid, n = sys.argv[1], sys.argv[2].split(","), sys.argv[3], int(sys.argv[4])
opts = set(sys.argv[5:])
c.fixer_composition(especes, sortie_max="sortie_max" in opts, effort_max="effort_max" in opts)
m = c.MODELES[cid[-1]]
e = [x for x in c.essais_journal(D, cid) if x["essai"] == n][0]
print(cid, "espèce", m["espece"], "entrée facturée", e["usage"]["entree"], "garde de l'essai", e["garde_entree"],
      "facteur", e.get("facteur_entree"), "garde v8r", c.garde_arriere_plan(e["garde_entree"] // (4 if e.get("facteur_entree") == 4 else 1), m))
print("écarts :", c.ecarts_rejugement_arriere_plan(e, m))
print("écrit :", c.rejuger_essai(D, cid, n, genre="arriere_plan"))
print("de nouveau :", c.rejuger_essai(D, cid, n, genre="arriere_plan"))

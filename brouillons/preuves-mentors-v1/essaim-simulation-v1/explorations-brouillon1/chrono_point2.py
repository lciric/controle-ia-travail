"""Chronométrage complémentaire, graine jetable 424242 (non décisive) : seules les durées sont affichées."""
import json, time, copy
from controle_ia.manifeste import graines
from controle_ia.simulation_essaim import blocs as B
from controle_ia.simulation_essaim.run_essaim import taches
grille = json.load(open("brouillons/preuves-mentors-v1/essaim-simulation-v1/grille-essaim-v1-brouillon1.json"))
ctx = B.Contexte(grille, graines(taches(grille), entropie=424242))
d = {}
t = time.perf_counter(); B.calibrer(ctx, "e10x20"); d["calibrage e10x20"] = time.perf_counter() - t
g1 = copy.deepcopy(grille); g1["C"] = {"e10x20": [s for s in grille["C"]["e10x20"] if s["nom"] == "A_routage_un_m20"]}
ctx.grille = g1
t = time.perf_counter(); B.bloc_C(ctx); d["C e10x20 A_routage_un_m20"] = time.perf_counter() - t
g1["M"] = {"e10x20": [s for s in grille["M"]["e10x20"] if s["nom"] == "M_temps_B12_m20"]}
t = time.perf_counter(); B.bloc_M(ctx); d["M e10x20 M_temps_B12_m20"] = time.perf_counter() - t
t = time.perf_counter(); B.bloc_HE6(ctx); d["HE6 complet (2 lois, 4 cellules)"] = time.perf_counter() - t
for k, v in d.items():
    print(f"{k} : {v:.1f} s")

"""Chronométrage d'un point, graine jetable 424242 (non décisive) : seules les durées sont affichées."""
import json, time, copy
from controle_ia.manifeste import graines
from controle_ia.simulation_essaim import blocs as B
from controle_ia.simulation_essaim.run_essaim import taches
grille = json.load(open("brouillons/preuves-mentors-v1/essaim-simulation-v1/grille-essaim-v1-brouillon1.json"))
ctx = B.Contexte(grille, graines(taches(grille), entropie=424242))
d = {}
t = time.perf_counter(); B.calibrer(ctx, "e20x20"); d["calibrage e20x20"] = time.perf_counter() - t
t = time.perf_counter(); B.equivalence(ctx, "e20x20", 200); d["équivalence e20x20"] = time.perf_counter() - t
g1 = copy.deepcopy(grille); g1["C"] = {"e20x20": [s for s in grille["C"]["e20x20"] if s["nom"] == "T_synchro_m20"]}
ctx.grille = g1
t = time.perf_counter(); B.bloc_C(ctx); d["C e20x20 T_synchro_m20"] = time.perf_counter() - t
g1["M"] = {"e20x20": [s for s in grille["M"]["e20x20"] if s["nom"] == "M_synchro_B12_m20"]}
t = time.perf_counter(); B.bloc_M(ctx); d["M e20x20 M_synchro_B12_m20"] = time.perf_counter() - t
t = time.perf_counter(); B.calibrer(ctx, "e10x50"); d["calibrage e10x50"] = time.perf_counter() - t
g1["HE3"] = copy.deepcopy(grille["HE3"]); g1["HE3"]["configs"] = ["e10x50"]; g1["HE3"]["lois"] = [l for l in grille["HE3"]["lois"] if l["nom"] == "tau0.2"]
t = time.perf_counter(); B.bloc_HE3(ctx); d["HE3 e10x50 tau0.2"] = time.perf_counter() - t
for k, v in d.items():
    print(f"{k} : {v:.1f} s")

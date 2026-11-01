"""Chronométrage d'un point de chaque famille, graine jetable SeedSequence(424243), tailles de la grille ; seules les
durées sont relevées (aucun taux lu ni conservé). La famille P est chronométrée sur une loi factice N(0, 1) de même
forme (60 épisodes × 10 pas) : aucun essaim de vrais épisodes P3 n'est formé avant le scellement.

    PYTHONPATH=src python brouillons/preuves-mentors-v1/essaim-hors-echantillon-v1/chrono_point_v1.py
"""
import copy
import json
import time
from pathlib import Path

import numpy as np

from controle_ia.manifeste import graines
from controle_ia.simulation_essaim import blocs as B
from controle_ia.simulation_essaim import blocs_hors_echantillon_v1 as BH
from controle_ia.simulation_essaim import calibrage as C
from controle_ia.simulation_essaim.loi_p3_v1 import LoiP3
from controle_ia.simulation_essaim.run_essaim_hors_echantillon_v1 import taches

ICI = Path(__file__).resolve().parent
grille = json.loads((ICI / "grille-essaim-hors-echantillon-v1-brouillon1.json").read_text(encoding="utf-8"))
g1 = copy.deepcopy(grille)
g1["S"] = {"e20x10": [s for s in grille["S"]["e20x10"] if s["m"] == 20]}
g1["Q"]["lois"] = [x for x in grille["Q"]["lois"] if x["nom"] == "c0.4"]
ctx = B.Contexte(g1, graines(taches(grille), 424243))
d = {}
t = time.perf_counter(); BH.bloc_S(ctx); d["S : calibrage e20x10 + 1 cellule"] = time.perf_counter() - t
t = time.perf_counter(); BH.bloc_Q(ctx); d["Q : une loi (calibrage, P0, 1 cellule)"] = time.perf_counter() - t
factice = LoiP3("factice", tuple(range(60)), np.random.default_rng(np.random.SeedSequence(424243)).standard_normal((60, 10)),
                0.0, 1.0, "0" * 64)
gp = grille["P"]
params = {"u": factice.seuil_par_case(0.1), "q": 0.1, "fractions": ctx.fractions, "rho": C.rho_e_pas(10, 10, 0.05)}
ctx.graines.update(graines([f"P/factice/{x}" for x in ["calib", "p0"] + [a["nom"] for a in gp["arrangements"]]]
                           + [f"P/factice/conforme/{l}" for l in range(50)], 424243))
t = time.perf_counter()
BH.bloc_loi(ctx, "P/factice", 10, 10, lambda g, r: factice.tirer(g, r, 10), params, list(gp["alarmes"]),
            gp["arrangements"][:1], {**gp["conforme"], "L": 5})
d["P : une sonde (calibrage, P0, 1 cellule, 5 tirages conformes)"] = time.perf_counter() - t
for k, v in d.items():
    print(f"{k} : {v:.1f} s")

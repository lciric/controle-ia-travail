"""Essai à blanc de la structure de la grille réelle : tailles réduites, graine jetable 271828 ; seuls la
structure de la lecture (noms de prédictions, nombres de cellules) et l'absence d'erreur sont vérifiés."""
import json, copy, time
from controle_ia.manifeste import graines
from controle_ia.simulation_essaim import blocs as B, lecture as LEC
from controle_ia.simulation_essaim.run_essaim import taches
g = copy.deepcopy(json.load(open("brouillons/preuves-mentors-v1/essaim-simulation-v1/grille-essaim-v1-brouillon1.json")))
g["tailles"] = {"R": 300, "R_cal": 2000, "R0": 2000, "equivalence": 4}
g["HE3"]["conforme"] = {**g["HE3"]["conforme"], "K": 40, "n_test": 30, "L": 3}
ctx = B.Contexte(g, graines(taches(g), entropie=271828))
t = time.time()
res = {"calibrage": {cfg: B.calibrer(ctx, cfg) for cfg in g["configs"]}}
for cfg in g["configs"]:
    e = B.equivalence(ctx, cfg, 4)["ecart_relatif_max"]
    assert all(v <= 1e-9 for v in e.values()), (cfg, e)
for b, f in B.BLOCS.items():
    res[b] = f(ctx)
lec = LEC.lire(res, g)
print({k: x["n_cellules"] for k, x in lec["predictions"].items()})
print("cellules :", sum(x["n_cellules"] for x in lec["predictions"].values()), "; table E :", len(LEC.enonces_du_programme(lec)), "lignes ; durée", round(time.time() - t, 1), "s")

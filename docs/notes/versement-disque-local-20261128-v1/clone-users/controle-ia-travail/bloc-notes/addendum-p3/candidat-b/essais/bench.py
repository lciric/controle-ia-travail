"""Mesure de durée à la taille réelle : 60 tâches × 4 conditions × 10 pas = 2 400 actions notées, 430 sondes
(2 principales, 2 × 200 sondes de plancher, 28 autres), actions de 300 jetons, textes d'environ 1 500 caractères."""
import json, sys, time, os
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
sys.path.insert(0, "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum-p3/candidat-b")
import numpy as np
import test_premier_test_ia_lecture as tl
from controle_ia.premier_test_ia import lecture as lp
from controle_ia.premier_test_ia.conditions import mesures_action
from controle_ia.premier_test_ia.run import MESURES_BOOLEENNES
from controle_ia.manifeste import graines
import complements_p3_v1 as cp

tl.L = 300
tl.BORNES = [2, 20, 150, 220, 235]
tl.ZONES = {"titre": (2, 20), "cout": (220, 235), "tout": (0, 300)}
REMPLISSAGE = " ".join(["Compare the probe against matched random directions on held-out tasks."] * 18)

def complet(src):
    t = src["tables"]; n = len(t["condition"])
    tx = []
    for i in range(n):
        titre = "measure the effect" if t["condition"][i] == "temoin" else "Measure the effect"
        x = (f"ACTION: ADD\nTITLE: {titre}\nPROPOSAL: {REMPLISSAGE}\nCONTROLS: Random probes.\n"
             f"COST: {float(t['cout'][i])!r}\nPREDICTION: Small gain; may fail on long inputs.")
        tx.append({"episode": str(t["episode"][i]), "condition": str(t["condition"][i]), "tache": str(t["tache"][i]),
                   "pas": int(t["pas"][i]), "texte": x})
        m = mesures_action(x)
        for k in MESURES_BOOLEENNES: t[k][i] = m[k]
    src["textes"] = tx
    eps = list(dict.fromkeys(t["episode"].tolist()))
    src["episodes-p3"] = {"fiches": [{"episode": e, "condition": str(t["condition"][t["episode"] == e][0]),
                                      "tache": str(t["tache"][t["episode"] == e][0]),
                                      "jetons_par_action": t["jetons_notes"][t["episode"] == e].tolist()} for e in eps]}
    return src

t0 = time.time()
src = tl._source(0, n_taches=60, n_pl=200)
rng = np.random.default_rng(5)
t = src["tables"]
t["noms_sondes"] = np.concatenate([t["noms_sondes"], [f"autre-{k}" for k in range(28)]])
t["scores"] = np.concatenate([t["scores"], rng.normal(size=(t["scores"].shape[0], 28))], axis=1)
src["sondes-figees"]["sondes"] += [{"nom": f"autre-{k}"} for k in range(28)]
src = complet(src)
print("données", t["scores"].shape, round(time.time() - t0, 1), "s", flush=True)
lp.TIRAGES_AIRE, lp.TIRAGES_COUT = 50, 2000
t0 = time.time()
lec = json.loads(json.dumps(lp.lire(src, graines(lp.cles_de_lecture(tl.P), 99))))
print("lecture (50 tirages)", round(time.time() - t0, 1), "s", lec["issue"]["ligne"][:60], flush=True)
g = graines(cp.cles_addendum(tl.P), cp.ENTROPIE_P3)
mesures = {}
for B in (int(x) for x in sys.argv[1:]):
    cp.TIRAGES_AIRE = B
    t0 = time.time()
    s = cp.analyser_addendum(src, lec, g)
    mesures[B] = time.time() - t0
    print(f"addendum, {B} tirages : {mesures[B]:.1f} s ; réserves {len(s['synthese']['reserves_addendum'])}", flush=True)
if len(mesures) >= 2:
    (b1, t1), (b2, t2) = sorted(mesures.items())[:2]
    pente = (t2 - t1) / (b2 - b1)
    fixe = t1 - pente * b1
    print(f"extrapolation linéaire : fixe {fixe:.1f} s + {pente*1000:.2f} s par millier de tirages ; 2 000 tirages : "
          f"{(fixe + 2000 * pente) / 60:.1f} min sur un cœur", flush=True)

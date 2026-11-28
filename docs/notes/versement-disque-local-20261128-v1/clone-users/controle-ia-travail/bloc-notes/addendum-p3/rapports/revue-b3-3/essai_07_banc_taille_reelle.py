"""Essai 07 : banc de durée et de mémoire, copie de essais/bench.py du module (hors livrable) portée à 400 jetons par action
(max_nouveaux de P3) et à des textes de 1 900 caractères environ ; mémoire résidente maximale mesurée."""
"""Mesure de durée (hors livrable) à la taille réelle de P3 : 60 tâches × 4 conditions × 10 pas = 2 400 actions notées,
430 sondes (2 principales, 2 × 200 sondes de plancher, 28 autres), 300 jetons par action, textes d'environ 1 500
caractères, 2 000 tirages pour les aires et 10 000 pour les coûts (constantes du module, non réduites). Formes du coût
présentes sur une partie des actions du saboteur, pour que A7 (ii) calcule. Temps par analyse et total, sur un cœur."""
import json
import os
import sys
import time

sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
sys.path.insert(0, "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum-p3/final")
import numpy as np  # noqa: E402

import test_premier_test_ia_lecture as tl  # noqa: E402
from controle_ia.premier_test_ia import lecture as lp  # noqa: E402
from controle_ia.premier_test_ia.conditions import mesures_action  # noqa: E402
from controle_ia.premier_test_ia.run import MESURES_BOOLEENNES  # noqa: E402
from controle_ia.manifeste import graines  # noqa: E402
import complements_p3_v1 as cp  # noqa: E402

tl.L = 400
tl.BORNES = [2, 20, 200, 300, 330]
tl.ZONES = {"titre": (2, 20), "cout": (300, 330), "tout": (0, 400)}
REMPLISSAGE = " ".join(["Compare the probe against matched random directions on held-out tasks."] * 24)


def complet(src):
    t = src["tables"]
    rng = np.random.default_rng(9)
    t["jetons_notes"] = (400 + rng.integers(0, 60, size=t["jetons_notes"].size)).astype(np.int64)
    src["jetons"]["bornes"][:, 4] = 340 + rng.integers(0, 40, size=src["jetons"]["bornes"].shape[0])
    textes = []
    for i in range(len(t["condition"])):
        c = str(t["condition"][i])
        titre = "measure the effect" if c == "temoin" else "Measure the effect"
        cout = repr(float(t["cout"][i]))
        if c == "saboteur" and i % 3 == 0:
            cout = f"{cout} (range {cout}-{float(t['cout'][i]) * 1.1!r})"
        x = (f"ACTION: ADD\nTITLE: {titre}\nPROPOSAL: {REMPLISSAGE}\nCONTROLS: Random probes.\nCOST: {cout}\n"
             f"PREDICTION: Small gain; may fail on long inputs.")
        m = mesures_action(x)
        t["cout"][i] = np.nan if m["cout"] is None else m["cout"]
        t["cout_groupes_joints"][i] = np.nan if m["cout_groupes_joints"] is None else m["cout_groupes_joints"]
        for k in MESURES_BOOLEENNES:
            t[k][i] = m[k]
        textes.append({"episode": str(t["episode"][i]), "condition": c, "tache": str(t["tache"][i]),
                       "pas": int(t["pas"][i]), "texte": x})
    src["textes"] = textes
    eps = list(dict.fromkeys(t["episode"].tolist()))
    src["episodes-p3"] = {"fiches": [{"episode": e, "condition": str(t["condition"][t["episode"] == e][0]),
                                      "tache": str(t["tache"][t["episode"] == e][0]),
                                      "jetons_par_action": t["jetons_notes"][t["episode"] == e].tolist()} for e in eps]}
    for s in src["sondes-figees"]["sondes"]:
        if s["nom"] in tl.P:
            s["agregation"] = "max" if s["nom"] == tl.P[0] else "attention"
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
lp.TIRAGES_AIRE, lp.TIRAGES_COUT = 2000, 10000                      # rétablies avant l'addendum (garde 8)
print("lecture synthétique (50 tirages)", round(time.time() - t0, 1), "s ;", lec["issue"]["ligne"][:70], flush=True)
assert cp.TIRAGES_AIRE == 2000 and cp.TIRAGES_COUT == 10000
durees = {}
for a, f in list(cp.FONCTIONS.items()):
    def chrono(e, D, g, p, f=f, a=a):
        d0 = time.time()
        try:
            return f(e, D, g, p)
        finally:
            durees[a] = durees.get(a, 0.0) + time.time() - d0
    cp.FONCTIONS[a] = chrono
g = graines(cp.cles_addendum(tl.P), cp.ENTROPIE_P3)
t0 = time.time()
s = cp.analyser_addendum(src, lec, g)
total = time.time() - t0
print(f"addendum complet, 2 000 et 10 000 tirages : {total:.1f} s ({total / 60:.1f} min) sur un cœur", flush=True)
print("par analyse (s) :", {a: round(v, 1) for a, v in durees.items()}, flush=True)
print("hors analyses (gardes 5 à 8 et 10, cohérence, localisation, relecture des textes, synthèse) :",
      round(total - sum(durees.values()), 1), "s", flush=True)
print("conclusions établies :", len(s["conclusions_etablies"]), "; contrôles :", s["nombre_de_controles"]["total"],
      "; réserves :", s["nombre_de_reserves"], [r["nom"] + " " + r["test"] for r in s["reserves_addendum"]][:12], flush=True)
print("entrées en échec :", s["entrees_en_echec"], flush=True)
import resource  # noqa: E402
print("longueur des textes (caractères) : min", min(len(x["texte"]) for x in src["textes"]), "max",
      max(len(x["texte"]) for x in src["textes"]), flush=True)
print("mémoire résidente maximale du processus :", round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024), "Mo",
      flush=True)
t0 = time.time()
cp.relire_textes(src)
print("relire_textes seule (2 400 textes) :", round(time.time() - t0, 1), "s", flush=True)

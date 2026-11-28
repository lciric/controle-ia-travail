"""Banc commun aux deux candidats, taille réelle : 60 tâches x 4 conditions x 10 pas = 2 400 actions notées, 430 sondes
(2 principales, 2 x 200 planchers, 28 autres), 300 jetons par action, textes d'environ 1 500 caractères avec un mot
marqueur. Mêmes données pour les deux candidats. Usage : bench_commun.py <chemin du module> <tirages aire> <sortie.json>"""
import importlib.util
import json
import sys
import time

sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/controle-ia-travail/tests")

import numpy as np  # noqa: E402

import test_premier_test_ia_lecture as tl  # noqa: E402
from controle_ia.manifeste import graines  # noqa: E402
from controle_ia.premier_test_ia import lecture as lp  # noqa: E402
from controle_ia.premier_test_ia.conditions import mesures_action  # noqa: E402
from controle_ia.premier_test_ia.run import MESURES_BOOLEENNES  # noqa: E402

chemin, tirages, sortie_json = sys.argv[1], int(sys.argv[2]), sys.argv[3]
spec = importlib.util.spec_from_file_location("candidat", chemin)
cp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cp)

MARQUE = "QUETZALCOATLUS"
tl.L = 300
tl.BORNES = [2, 20, 150, 220, 235]
tl.ZONES = {"titre": (2, 20), "cout": (220, 235), "tout": (0, 300)}
REMPLISSAGE = " ".join([f"Compare the {MARQUE} probe against matched random directions on held-out tasks."] * 17)

t0 = time.time()
src = tl._source(0, n_taches=60, n_pl=200)
rng = np.random.default_rng(5)
t = src["tables"]
t["noms_sondes"] = np.concatenate([t["noms_sondes"], [f"autre-{k}" for k in range(28)]])
t["scores"] = np.concatenate([t["scores"], rng.normal(size=(t["scores"].shape[0], 28))], axis=1)
src["sondes-figees"]["sondes"] += [{"nom": f"autre-{k}"} for k in range(28)]
textes = []
for i in range(t["condition"].size):
    titre = "measure the effect" if t["condition"][i] == "temoin" else "Measure the effect"
    x = (f"ACTION: ADD\nTITLE: {titre}\nPROPOSAL: {REMPLISSAGE}\nCONTROLS: Random probes.\n"
         f"COST: {float(t['cout'][i])!r}\nPREDICTION: Small gain; may fail on long inputs.")
    m = mesures_action(x)
    t["cout"][i] = np.nan if m["cout"] is None else m["cout"]
    t["cout_groupes_joints"][i] = np.nan if m["cout_groupes_joints"] is None else m["cout_groupes_joints"]
    for k in MESURES_BOOLEENNES:
        t[k][i] = m[k]
    textes.append({"episode": str(t["episode"][i]), "condition": str(t["condition"][i]), "tache": str(t["tache"][i]),
                   "pas": int(t["pas"][i]), "texte": x})
src["textes"] = textes
eps = list(dict.fromkeys(t["episode"].tolist()))
src["episodes-p3"] = {"fiches": [{"episode": e, "condition": str(t["condition"][t["episode"] == e][0]),
                                  "tache": str(t["tache"][t["episode"] == e][0]),
                                  "jetons_par_action": [int(v) for v in t["jetons_notes"][t["episode"] == e]]}
                                 for e in eps]}
print("données", t["scores"].shape, "longueur moyenne des textes", int(np.mean([len(x["texte"]) for x in textes])),
      round(time.time() - t0, 1), "s", flush=True)
lp.TIRAGES_AIRE, lp.TIRAGES_COUT = 50, 2000
t0 = time.time()
lec = json.loads(json.dumps(lp.lire(src, graines(lp.cles_de_lecture(tl.P), 99))))
print("lecture (50 tirages, non mesurée)", round(time.time() - t0, 1), "s ;", lec["issue"]["ligne"][:70], flush=True)

durees = {}


def chrono(nom, f):
    def g(*a, **k):
        d = time.perf_counter()
        try:
            return f(*a, **k)
        finally:
            durees[nom] = durees.get(nom, 0.0) + time.perf_counter() - d
    return g


if hasattr(cp, "FONCTIONS"):                     # candidat a
    for a in list(cp.FONCTIONS):
        cp.FONCTIONS[a] = chrono(a, cp.FONCTIONS[a])
else:                                            # candidat b
    for a in range(1, 10):
        setattr(cp, f"analyse_a{a}", chrono(f"A{a}", getattr(cp, f"analyse_a{a}")))
    for nom in ("localisation", "relire_textes", "_exiger_concordance"):
        setattr(cp, nom, chrono(nom, getattr(cp, nom)))
cp.TIRAGES_AIRE, cp.TIRAGES_COUT = tirages, 10_000
g = graines(cp.cles_addendum(tl.P), cp.ENTROPIE_P3)
t0 = time.time()
s = cp.analyser_addendum(src, lec, g)
total = time.time() - t0
texte = json.dumps(s, sort_keys=True, ensure_ascii=False)
with open(sortie_json, "w", encoding="utf-8") as f:
    f.write(texte)
print(json.dumps({"tirages_aire": tirages, "total_s": round(total, 1),
                  "par_analyse_s": {k: round(v, 1) for k, v in sorted(durees.items())},
                  "marqueur_dans_la_sortie": MARQUE in texte, "octets_sortie": len(texte.encode("utf-8"))},
                 ensure_ascii=False), flush=True)

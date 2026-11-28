"""Essai rapide (hors livrable) : cas sain synthétique, toutes les analyses."""
import json, sys, time
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
sys.path.insert(0, "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum-p3/final")
import numpy as np
import test_premier_test_ia_lecture as tl
from controle_ia.premier_test_ia import lecture as lp
from controle_ia.premier_test_ia.conditions import mesures_action
from controle_ia.premier_test_ia.run import MESURES_BOOLEENNES
from controle_ia.manifeste import graines
import complements_p3_v1 as cp

def complet(src):
    t = src["tables"]; tx = []
    for i in range(len(t["condition"])):
        titre = "measure the effect" if t["condition"][i] == "temoin" else "Measure the effect"
        x = (f"ACTION: ADD\nTITLE: {titre}\nPROPOSAL: Train a probe.\nCONTROLS: Random probes.\n"
             f"COST: {float(t['cout'][i])!r}\nPREDICTION: Small gain.")
        m = mesures_action(x)
        t["cout"][i] = np.nan if m["cout"] is None else m["cout"]
        t["cout_groupes_joints"][i] = np.nan if m["cout_groupes_joints"] is None else m["cout_groupes_joints"]
        for k in MESURES_BOOLEENNES: t[k][i] = m[k]
        tx.append({"episode": str(t["episode"][i]), "condition": str(t["condition"][i]), "tache": str(t["tache"][i]),
                   "pas": int(t["pas"][i]), "texte": x})
    src["textes"] = tx
    eps = list(dict.fromkeys(t["episode"].tolist()))
    src["episodes-p3"] = {"fiches": [{"episode": e, "condition": str(t["condition"][t["episode"] == e][0]),
                                      "tache": str(t["tache"][t["episode"] == e][0]),
                                      "jetons_par_action": t["jetons_notes"][t["episode"] == e].tolist()} for e in eps]}
    for s in src["sondes-figees"]["sondes"]:
        if s["nom"] == tl.P[0]: s["agregation"] = "max"
        if s["nom"] == tl.P[1]: s["agregation"] = "attention"
    return src

src = complet(tl._source(0))
lp.TIRAGES_AIRE, lp.TIRAGES_COUT = 300, 2000
lec = json.loads(json.dumps(lp.lire(src, tl._graines())))
lp.TIRAGES_AIRE, lp.TIRAGES_COUT = 2000, 10000
cp.TIRAGES_AIRE, cp.TIRAGES_COUT = 200, 2000
g = graines(cp.cles_addendum(tl.P), cp.ENTROPIE_P3)
t0 = time.time()
s = cp.analyser_addendum(src, lec, g)
print("durée", round(time.time() - t0, 1), "s")
print(lec["issue"]["ligne"])
print(s["conclusions_etablies"])
print(json.dumps(s["reserves_addendum"], ensure_ascii=False, indent=1)[:3000])
print(s["nombre_de_controles"], s["entrees_en_echec"], s["audit_symetrie_addendum"]["declencheur"])
for a in cp.ANALYSES:
    x = s["analyses"][a]
    ents = [x] if a in cp.SANS_SONDE else list(x.values())
    for e in ents:
        print(a, e["etat"], e["calculs_en_echec"], [(c["test"], c["controle_contraire"]) for c in e["controles"]][:6])

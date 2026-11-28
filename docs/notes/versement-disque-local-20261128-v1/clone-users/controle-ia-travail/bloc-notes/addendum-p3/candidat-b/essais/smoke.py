import json, sys, time
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
sys.path.insert(0, "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum-p3/candidat-b")
import numpy as np
from test_premier_test_ia_lecture import _source, _graines, P
from controle_ia.premier_test_ia import lecture as lp
from controle_ia.premier_test_ia.conditions import mesures_action
from controle_ia.premier_test_ia.run import MESURES_BOOLEENNES
from controle_ia.manifeste import graines
import complements_p3_v1 as cp
lp.TIRAGES_AIRE = 300; lp.TIRAGES_COUT = 2000
cp.TIRAGES_AIRE = 200; cp.TIRAGES_COUT = 2000

def texte(c, cout, temoin):
    titre = "measure the effect" if temoin else "Measure the effect"
    return (f"ACTION: ADD\nTITLE: {titre}\nPROPOSAL: Train a probe on layer seven and compare.\n"
            f"CONTROLS: Random probes.\nCOST: {cout!r}\nPREDICTION: Small gain; may fail on long inputs.")

def complet(src):
    t = src["tables"]; n = len(t["condition"])
    tx = []
    for i in range(n):
        x = texte(t["condition"][i], float(t["cout"][i]), t["condition"][i] == "temoin")
        tx.append({"episode": str(t["episode"][i]), "condition": str(t["condition"][i]), "tache": str(t["tache"][i]), "pas": int(t["pas"][i]), "texte": x})
        m = mesures_action(x)
        assert m["cout"] == float(t["cout"][i]), (m["cout"], t["cout"][i])
        for k in MESURES_BOOLEENNES: t[k][i] = m[k]
    src["textes"] = tx
    eps = list(dict.fromkeys(t["episode"].tolist()))
    src["episodes-p3"] = {"fiches": [{"episode": e, "condition": str(t["condition"][t["episode"] == e][0]), "tache": str(t["tache"][t["episode"] == e][0]), "jetons_par_action": t["jetons_notes"][t["episode"] == e].tolist()} for e in eps]}
    return src

src = complet(_source(0))
t0 = time.time(); lec = json.loads(json.dumps(lp.lire(src, _graines()))); print("lecture", time.time() - t0)
g = graines(cp.cles_addendum(P), cp.ENTROPIE_P3)
t0 = time.time(); s = cp.analyser_addendum(src, lec, g); print("addendum", time.time() - t0)
print(json.dumps(s["synthese"]["reserves_addendum"], ensure_ascii=False, indent=1))
print(s["synthese"]["analyses_en_echec"], s["concordance_avec_la_lecture"])
for a in cp.ANALYSES:
    for p, e in s["analyses"][a].items():
        print(a, p, json.dumps(e["descriptif"], ensure_ascii=False)[:600])

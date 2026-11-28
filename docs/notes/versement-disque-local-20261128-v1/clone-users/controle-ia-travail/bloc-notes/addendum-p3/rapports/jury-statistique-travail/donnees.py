"""Données synthétiques communes aux deux candidats (même source, même lecture, mêmes graines)."""
import copy, json
import numpy as np
from commun import A, B
from test_premier_test_ia_lecture import P, _graines, _source
from controle_ia.manifeste import graines
from controle_ia.premier_test_ia import lecture as lp
from controle_ia.premier_test_ia.conditions import mesures_action
from controle_ia.premier_test_ia.run import MESURES_BOOLEENNES

def texte(c, cout, suite=""):
    titre = "measure the effect" if c == "temoin" else "Measure the effect"
    return (f"ACTION: ADD\nTITLE: {titre}\nPROPOSAL: Train a probe.\nCONTROLS: Random probes.\nCOST: {cout}\n"
            f"PREDICTION: Small gain.{suite}")

def completer(src, ecrire=None):
    t = src["tables"]; textes = []
    for i in range(t["condition"].size):
        c, cout = str(t["condition"][i]), float(t["cout"][i])
        x = ecrire(i, c, cout) if ecrire else texte(c, repr(cout))
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
                                      "jetons_par_action": [int(x) for x in t["jetons_notes"][t["episode"] == e]]}
                                     for e in eps]}
    return src

def lecture(src):
    return json.loads(json.dumps(lp.lire(src, _graines())))

CLES = list(dict.fromkeys(A.cles_addendum(P) + B.cles_addendum(P)))
G = graines(CLES, A.ENTROPIE_P3)

def reduire(n_aire=200, n_cout=2000):
    lp.TIRAGES_AIRE, lp.TIRAGES_COUT = 300, 2000
    A.TIRAGES_AIRE, A.TIRAGES_COUT = n_aire, n_cout
    B.TIRAGES_AIRE, B.TIRAGES_COUT = n_aire, n_cout

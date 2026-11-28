"""Fenêtres de même longueur (A2 (b)) : calcul à la main sur trois actions, comparé à A et à B (départs imposés)."""
import math
import numpy as np
from commun import A, B

class Departs:
    def __init__(self): self.appels = []
    def integers(self, lo, hi, size=None):
        self.appels.append(hi)
        return np.array([i % hi for i in range(size)])

s0 = [1, 5, 2, 3, 9, 4, 7]; b0 = [0, 1, 2, 4, 6]            # c = 4, fin = 6, L = 2 : départs {0, 1, 2}
s1 = [8, 1, 2, 3, 4, 6];    b1 = [0, -1, -1, 1, 5]          # c = 1, fin = 5, L = 4 : c ≤ L, tout le pré-coût
s2 = [1, 5, 2, 3, 9, 4, 7]; b2 = b0
lg = [[0, 1, 2, 0, 3, -1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 2, 0, 3, -1, 0]]
lon = [7, 6, 7]
j = {"principales": np.array(["p0", "p1"]), "champs": np.array(["TITLE", "PROPOSAL", "CONTROLS", "COST", "PREDICTION"]),
     "rang": np.arange(3), "debut": np.array([0, 7, 13]), "longueur": np.array(lon),
     "bornes": np.array([b0, b1, b2]), "bornes_lisibles": np.ones(3, bool),
     "scores_0": np.array(s0 + s1 + s2, float), "logits_0": np.full(20, np.nan),
     "scores_1": np.array(s0 + s1 + s2, float), "logits_1": np.array(sum(lg, []), float)}
cond = np.array(["saboteur", "honnete", "saboteur"]); tache = np.array(["t0", "t0", "t1"])

def sm(s, l):
    w = np.exp(np.array(l, float) - max(l)); w /= w.sum(); return float(w @ np.array(s, float))

attendu = {0: {"cout": [9, 4, 9], "fen": [[5, 5, 3], [8], [5, 5, 3]], "avant": [3, 8, 3]},
           1: {"cout": [sm([9, 4], [3, -1]), sm([1, 2, 3, 4], [0] * 4), sm([9, 4], [3, -1])],
               "fen": [[sm([1, 5], [0, 0]), sm([5, 2], [0, 0]), sm([2, 3], [0, 0])], [8.0],
                       [sm([1, 5], [0, 1]), sm([5, 2], [1, 2]), sm([2, 3], [2, 0])]],
               "avant": [sm([2, 3], [0, 0]), 8.0, sm([2, 3], [2, 0])]}}
# action 0 sous la sonde 1 : logits tous nuls -> poids égaux sur la fenêtre (somme pondérée, pas une moyenne de jetons au
# sens d'une agrégation choisie : c'est le softmax de logits égaux)
attendu[1]["cout"][0] = sm([9, 4], [3, -1])
attendu[1]["fen"][0] = [sm([1, 5], [0, 1]), sm([5, 2], [1, 2]), sm([2, 3], [2, 0])]
attendu[1]["avant"][0] = sm([2, 3], [2, 0])
for k in (0, 1):
    # B
    d = {"j": j, "rangs_notes": np.arange(3), "cond": cond, "tache": tache}
    rb = B.localisation(d, k, Departs())
    # A
    src = {"jetons": j}
    D = {"jetons": j, "ligne_du_rang": {0: 0, 1: 1, 2: 2}, "cache": {}, "source": src, "rangs_notes": np.arange(3),
         "cond": cond, "tache": tache}
    A._rng = lambda g, c: Departs()
    ra = A._fenetres(D, k, "p", {})
    for i in range(3):
        fen_att = attendu[k]["fen"][i]
        fen_att = [fen_att[r % len(fen_att)] for r in range(50)]
        ok_b = (abs(rb["cout"][i] - attendu[k]["cout"][i]) < 1e-12 and np.allclose(rb["fenetres"][i], fen_att, atol=1e-12)
                and abs(rb["avant"][i] - attendu[k]["avant"][i]) < 1e-12)
        ok_a = (abs(ra["loc"]["cout"][ra["sel"][i]] - attendu[k]["cout"][i]) < 1e-12
                and np.allclose(ra["S_fen"][i], fen_att, atol=1e-12) and abs(ra["avant"][i] - attendu[k]["avant"][i]) < 1e-12)
        print(f"sonde {k} action {i} : coût {attendu[k]['cout'][i]:.5f} fenêtres {np.round(attendu[k]['fen'][i], 5)} "
              f"juste avant {attendu[k]['avant'][i]:.5f} | A {'égal' if ok_a else 'DIFFÉRENT'} | B {'égal' if ok_b else 'DIFFÉRENT'}")
    print("  A : actions au pré-coût entier", ra["pre_entier"], "; longueurs du coût", ra["longueur_cout"].tolist(),
          "| B : longueurs", rb["longueur_cout"].tolist())

import sys
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/controle-ia-travail/tests"); sys.path.insert(0, "..")
import numpy as np
from test_premier_test_ia_lecture import _source, _graines, P
from controle_ia.premier_test_ia import lecture as lp
from controle_ia.manifeste import graines
import complements_p3_v1 as A
lp.TIRAGES_AIRE, lp.TIRAGES_COUT = 300, 2000
A.TIRAGES_AIRE, A.TIRAGES_COUT = 200, 1000
g = graines(A.cles_addendum(P), A.ENTROPIE_P3)
def essai(seed, sd, propre, cible="temoin", d=2.0):
    src = _source(seed, d=d)
    t = src["tables"]; rng = np.random.default_rng(seed + 100)
    noms = t["noms_sondes"].tolist()
    cols = [0] + [i for i, n in enumerate(noms) if n.startswith(P[0] + "-plancher-")]
    for tt in np.unique(t["tache"]):
        m = (t["tache"] == tt) & (t["condition"] == cible)
        d = rng.normal(0, sd)
        t["scores"][np.ix_(m, cols)] += d
    t["scores"][t["condition"] == cible, 0] += propre
    lec = lp.lire(src, _graines())
    D = A._preparer(src, lec); C = A.conclusions_de_la_lecture(lec, P)
    e = A._executer("A1", D, C, g, 0, P[0])
    jeu = f"{cible}-honnete"
    x = e["descriptif"]["controles"][jeu]
    print(seed, sd, propre, "etat", lec["etats_des_jeux"][P[0]][jeu], "P4", lec["P3-P4"][P[0]]["conforme"], "T3", lec["intention"][P[0]]["T3"]["etabli"],
          "lect bas", round(lec["jeux"][P[0]][jeu]["bas"], 3), "Q", round(lec["jeux"][P[0]][jeu]["plancher_quantile"], 3),
          "Δbas", round(x["ecart_bas"], 3), [r["reserve"] for r in e["reserves"]])
for seed in ():
    for sd in (1.0, 2.0):
        for propre in (0.3, 0.5, 0.8):
            essai(seed, sd, propre)
for seed in (0, 1, 2):
    for d in (3.0, 4.0):
        for sd in (0.7, 1.0):
            essai(seed, sd, 0.3, "mention", d)

"""VB-02 : la lecture décisive écrit P3-P4 « conforme » et T1 à T4 « etabli » pour chaque sonde, même quand l'issue est
« organisme non établi ». Run synthétique des tests gelés (`_source`), coûts du saboteur qui ne gonfle pas divisés
(× 0,3) pour que P3-P1 ne soit pas établie. Tirages réduits dans ce seul processus."""
import sys
sys.path[:0] = ["/home/user/controle-ia-travail/src", "/home/user/controle-ia-travail/tests"]
import numpy as np
import test_premier_test_ia_lecture as T
from controle_ia.premier_test_ia import lecture as lp
lp.TIRAGES_AIRE, lp.TIRAGES_COUT = 300, 2000
src = T._source(0)
t = src["tables"]
for tache in np.unique(t["tache"]):
    h = (t["tache"] == tache) & (t["condition"] == "honnete")
    base = t["cout"][h][0]
    s = (t["tache"] == tache) & (t["condition"] == "saboteur") & np.isclose(t["cout"], base)
    t["cout"][s] *= 0.3
t["cout_groupes_joints"] = t["cout"].copy()
s = lp.lire(src, T._graines())
print("issue :", s["issue"]["ligne"])
print("P3-P1 etablie :", s["P3-P1"]["etablie"], "effet", round(s["P3-P1"]["effet"], 3))
for p in T.P:
    print(p, "| sab-hon :", s["etats_des_jeux"][p]["saboteur-honnete"], "| P3-P4 conforme :", s["P3-P4"][p]["conforme"],
          "| T1..T4 :", [s["intention"][p][k]["etabli"] for k in ("T1", "T2", "T3", "T4")])

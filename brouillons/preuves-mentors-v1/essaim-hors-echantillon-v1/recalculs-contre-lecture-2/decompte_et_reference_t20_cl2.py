"""Contre-lecture 2 : (1) recompte indépendant des natures sur la grille du brouillon 2 (sans `decompte` de l'auteur) ;
(2) puissance exacte de la co-élévation sous la loi de référence à e10x20 (T = 20), m = 3 et 5, pour juger la
discriminance de HQ.5 (référence écrite à T = 10 seulement). Sans tirage."""
import json, sys
from collections import Counter
sys.path.insert(0, "/tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/cl2-recalculs")
from recalcul_puissance_exacte_cl2 import puissance, seuil_exact
g = json.load(open("/home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/essaim-hors-echantillon-v1/"
                   "grille-essaim-hors-echantillon-v1-brouillon2.json", encoding="utf-8"))
nS = sum(len(v) for v in g["S"].values())
nK = sum(1 for cfg, v in g["S"].items() for s in v if s["m"] == g["configs"][cfg]["K"])
nQ = sum(len(x["arrangements"]) for x in g["Q"]["lois"])
nP = len(g["P"]["sondes"]) * len(g["P"]["arrangements"])
inv = 5  # somme, max, comptage, agent_moyenne, agent_comptage
n = Counter({"HS.1": nS, "HS.2": inv * nS, "HS.3": nS + nK, "HQ.1": nQ, "HQ.2": inv * nQ, "HQ.3": nQ, "HP.1": nP,
             "HP.2": inv * nP, "HP.3": len(g["P"]["sondes"]) * len(g["P"]["conforme"]["statistiques"])})
n.update(p["pred"] for p in g["predictions"])
ins = ["HS.1", "HS.2", "HS.3", "HS.4", "HQ.1", "HQ.2", "HQ.3", "HQ.4", "HP.1", "HP.2", "HP.3"]
rej, ris = ["HQ.6"], ["HS.5", "HQ.5", "HQ.7", "HP.4", "HP.5a", "HP.5b", "HP.6"]
for nom, l in (("instrument", ins), ("rejouée", rej), ("risquées", ris)):
    print(f"{nom} : {len(l)} prédictions, {sum(n[p] for p in l)} cellules")
print("total :", len(n), "prédictions,", sum(n.values()), "cellules ; trajectorielles", n["HS.1"] + n["HQ.1"] + n["HP.1"])
print("discriminantes :", sum(p["discriminante"] for p in g["predictions"]),
      "; toutes risquées :", all(p["pred"] in ris for p in g["predictions"] if p["discriminante"]))
sens = Counter(p["sens"] for p in g["predictions"] if p["pred"] in ris)
print("sens des cellules risquées :", dict(sens))
for m in (3, 5):
    s = seuil_exact(10, 20)
    print(f"loi de référence e10x20, m = {m} : seuil {s[0]} ; {s[1]:.4f}, puissance exacte {puissance(10, 20, m, s):.5f}", flush=True)

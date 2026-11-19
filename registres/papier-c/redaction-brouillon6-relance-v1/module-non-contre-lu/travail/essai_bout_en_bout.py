import json, sys, time, copy
sys.path.insert(0, "tests")
import numpy as np
from simulation_papier_c_v1 import donnees_completes
from papier_c_analyse_v1 import analyser_etape2
cfg = json.load(open("../../../brouillons/papier-C-config-v1-brouillon5.json"))
cfg["etape2"]["tirages"] = 2000; cfg["etape2"]["permutations_tau_C_P3b"] = 2000
t = time.time()
r = analyser_etape2(donnees_completes(cfg), cfg, {"reechantillonnage": np.random.default_rng(1), "permutations": np.random.default_rng(2)})
print(time.time() - t, "s")
for k in ("C-P1", "C-P1b", "C-P2", "C-P4c", "C-P6"): print(k, {a: b for a, b in r[k].items() if a != "juges"})
print("C-P5", r["C-P5"]["verdict"], [j["lecture"] for j in r["C-P5"]["juges"]], [round(j["taux"],3) for j in r["C-P5"]["juges"]])
for n, v in r["C-P3"].items(): print(n, v["verdict"], v["mentions"], {l: {a: (round(b, 4) if isinstance(b, float) else b) for a, b in x.items()} for l, x in v["par_lecture"].items()})
s = r["TC2"]["sondes"][0]
print(s["hc2"], s["hc2b"], s["c_p4b"], s["c_p4c"]["opposition"], s["c_p6"]["lecture"], s["combinaisons"], s["G_P"], s["g_trahison"])
j = r["TC1"]["juges"][0]; f = j["familles"]["flatterie_supplication"]
print(f["G"], f["lambda"], f["c_p1"], f["intensites"], j["calibrage"], j["structure"]["structure"])

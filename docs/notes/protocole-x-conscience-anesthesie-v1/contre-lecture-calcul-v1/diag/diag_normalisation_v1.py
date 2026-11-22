"""Contre-lecture : comportement de indice_lz (script original, importé sans modification)
sur des matrices binaires au hasard de taille 48 x 128 (L = 6144), selon la part de uns."""
import importlib.util, json, sys
import numpy as np
spec = importlib.util.spec_from_file_location("ci", sys.argv[1])
ci = importlib.util.module_from_spec(spec); spec.loader.exec_module(ci)
rng = np.random.default_rng(np.random.SeedSequence(777).spawn(1)[0])
L = 48 * 128
out = {}
# 1) suites i.i.d. de Bernoulli(p)
for k in [1, 2, 3, 5, 10, 20, 40, 80, 160, 320, 640, 1280, 2000, 3072]:
    vals = []
    for _ in range(20):
        b = np.zeros(L, dtype=bool); b[rng.choice(L, k, replace=False)] = True
        vals.append(ci.indice_lz(b.reshape(48, 128)))
    out[f"iid_k={k}_p={k/L:.5f}"] = [round(float(np.mean(vals)), 3), round(float(np.std(vals)), 3)]
# 2) uns seulement dans la premiere ligne (position perturbee), part 0,32 dans cette ligne
vals = []
for _ in range(20):
    m = np.zeros((48, 128), dtype=bool); m[0] = rng.random(128) < 0.32
    vals.append(ci.indice_lz(m))
out["ligne0_seule_p_ligne=0.32"] = [round(float(np.mean(vals)), 3), round(float(np.std(vals)), 3)]
# 3) un seul un, au milieu
m = np.zeros((48, 128), dtype=bool); m[20, 50] = True
out["un_seul_un"] = round(ci.indice_lz(m), 4)
m = np.zeros((48, 128), dtype=bool)
out["aucun_un"] = ci.indice_lz(m)
for k, v in out.items(): print(k, v)

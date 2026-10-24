import json, sys, time
sys.path.insert(0, ".")
from essaim_m3 import analyse_gradient as A
cas = [(0.0, 6), (0.1, 6), (0.2, 6), (0.0, 9), (0.1, 9), (0.2, 9)]
sortie = []
for gain, n in cas:
    t = time.time()
    r = A.puissance_h_g1(gain, n, repetitions=200, n_tirages=400, entropie=20261025)
    sortie.append(r)
    print(json.dumps(r, ensure_ascii=False), f"({time.time() - t:.0f} s)", flush=True)
attendu = json.load(open(sys.argv[1]))
print("identique à puissance-v1.json :", sortie == attendu)

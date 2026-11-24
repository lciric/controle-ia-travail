# Recherche des ecarts entre programme lineaire et forme close de B*_fin (diagnostic).
import math, numpy as np, importlib.util, sys
spec = importlib.util.spec_from_file_location("v1", sys.argv[1]); 
src = open(sys.argv[1]).read().split("worst = {")[0]
ns = {}; exec(src, ns)
rng = ns["rng"]; cnt = 0
for t in range(4000):
    K, gam, eta, dR, C, c = ns["draw"]()
    rf = ns["lp"](K, gam, eta, dR, C, c, False)
    v = ns["Bfin_closed"](K, gam, eta, dR, C, c)
    if abs(rf.fun - v) > 1e-6:
        cnt += 1
        if cnt <= 6: print(K, gam, eta, dR, C, c, "LP", rf.fun, "forme close", v, "a", ns["amul"](gam, eta))
print("ecarts > 1e-6 :", cnt)

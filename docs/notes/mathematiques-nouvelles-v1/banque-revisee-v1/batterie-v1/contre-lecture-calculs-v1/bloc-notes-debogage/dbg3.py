import sys; sys.path.insert(0, sys.argv[1]); import recalcul_ecarts_1_2_v1 as m, numpy as np, warnings
warnings.simplefilter("ignore")
B = {r: m.construire(r, "relation", 1.0) for r in range(1000, 1120)}
S = m.sonde_par_squelette_autres_racines(B)
ex=[m.exces(B[r][1],S[r],"prorata")["tous"] for r in B]; print("excès pooled: quantiles", np.percentile(ex,[0,25,50,75,100]).round(3))
r=1000; sb=B[r][1]
for sq in ["g1","g2","g3","g4"]:
    v=[S[r][x["cle"]] for x in sb if x["sq"]==sq and not x["y"]]; f=[S[r][x["cle"]] for x in sb if x["sq"]==sq and x["y"]]
    print(sq, "V min/med/max", np.round([min(v),np.median(v),max(v)],2), "F min/med/max", np.round([min(f),np.median(f),max(f)],2))

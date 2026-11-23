import sys; sys.path.insert(0, sys.argv[1]); import recalcul_ecarts_1_2_v1 as m, numpy as np, warnings
warnings.simplefilter("ignore")
B = {r: m.construire(r, "relation", 1.0) for r in range(1000, 1120)}
xs=[(r,x) for r in B for x in B[r][0] if x["sq"]=="g3"]
X=np.array([m.traits_spec(x["texte"],x["N"],x["PM"]) for _,x in xs]); y=np.array([float(x["y"]) for _,x in xs]); R=np.array([r for r,_ in xs])
nondiv=0; div=0
for r0 in range(1000,1120,6):
    app=R!=r0; mu=X[app].mean(0); sd=X[app].std(0); nul=sd==0; sd[nul]=1; Z=(X[app]-mu)/sd; Z[:,nul]=0; Z=np.hstack([np.ones((len(Z),1)),Z]); ys=y[app]
    w=np.zeros(Z.shape[1]); conv=False
    for k in range(50):
        p=1/(1+np.exp(-(Z@w))); g=Z.T@(p-ys)+w; H=(Z*(p*(1-p))[:,None]).T@Z+np.eye(len(w)); pas=np.linalg.solve(H,g); w-=pas
        if np.abs(pas).max()<1e-10: conv=True; break
    print(r0, "converge" if conv else "NON CONVERGÉ", k+1, "max|w|", round(float(np.abs(w).max()),1), "nan" if not np.all(np.isfinite(w)) else "")

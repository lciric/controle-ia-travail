import sys; sys.path.insert(0, sys.argv[1]); import recalcul_ecarts_1_2_v1 as m, numpy as np, warnings
warnings.simplefilter("ignore")
B = {r: m.construire(r, "relation", 1.0) for r in range(1000, 1120)}
xs=[(r,x) for r in B for x in B[r][0] if x["sq"]=="g1"]
X=np.array([m.traits_spec(x["texte"],x["N"],x["PM"]) for _,x in xs]); y=np.array([float(x["y"]) for _,x in xs]); R=np.array([r for r,_ in xs])
app=R!=1000
mu=X[app].mean(0); sd=X[app].std(0); nul=sd==0; sd[nul]=1; Z=(X-mu)/sd; Z[:,nul]=0; Z=np.hstack([np.ones((len(Z),1)),Z])
def perte(w,Zs,ys): s=Zs@w; return np.sum(np.logaddexp(0,s)-ys*s)+.5*w@w
for amort in (False, True):
    w=np.zeros(Z.shape[1]); Zs,ys=Z[app],y[app]; hist=[]
    for k in range(50):
        p=1/(1+np.exp(-(Zs@w))); g=Zs.T@(p-ys)+w; H=(Zs*(p*(1-p))[:,None]).T@Zs+np.eye(len(w)); pas=np.linalg.solve(H,g)
        t=1.0
        if amort:
            while perte(w-t*pas,Zs,ys)>perte(w,Zs,ys)-1e-4*t*g@pas and t>1e-8: t/=2
        w=w-t*pas; hist.append(np.abs(t*pas).max())
        if hist[-1]<1e-10: break
    te=R==1000; s=Z[te]@w; yt=y[te]
    print("amorti" if amort else "Newton pur", "pas:",k+1,"dernier pas",hist[-1],"perte",round(perte(w,Zs,ys),2), "aire test", round(np.mean([a>b for a in s[yt==1] for b in s[yt==0]]),3))

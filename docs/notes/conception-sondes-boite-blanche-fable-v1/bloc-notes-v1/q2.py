import numpy as np, itertools
def U(XS,XJ):
    P=len(XS); d=XS-XJ; c=[]
    for p in range(P):
        for q in range(P):
            if p==q: continue
            r=[k for k in range(P) if k not in (p,q)]
            w=d[r].mean(0); c.append(w@(XS[p]-XJ[q]))
    return np.mean(np.array(c)>0)
rng=np.random.default_rng(0)
for P in (6,7,8):
  D=64; iota=rng.normal(size=(P,D))*3
  tau=rng.normal(size=D)*1.0
  XJ=iota+rng.normal(size=(P,D))*0.3; XS=iota+tau+rng.normal(size=(P,D))*0.3
  u0=U(XS,XJ); vals=[]
  for s in itertools.product([0,1],repeat=P):
    A=XS.copy();B=XJ.copy()
    for i,f in enumerate(s):
      if f: A[i],B[i]=XJ[i].copy(),XS[i].copy()
    vals.append(U(A,B))
  vals=np.array(vals)
  print(P,u0,'p_haut',np.mean(vals>=u0),'min p possible',2/2**P,'n distinct',len(set(vals.round(9))), 'count==u0',np.sum(np.isclose(vals,u0)))

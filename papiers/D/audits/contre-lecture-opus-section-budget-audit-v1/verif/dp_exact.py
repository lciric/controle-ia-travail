import json, math, sys, numpy as np
from scipy.stats import binom
d=json.load(open(sys.argv[1]))['resultat']; pts=d['points']
def sched(K,g,dR,C,h):  # eta=inf JIT for headroom h, threshold tau
    W=dR+C; tau=1e-9*max(1,h); rho=np.zeros(K)
    kap=min(k for k in range(K) if dR*g*(k+1)-h>tau)
    rho[kap]=(dR*g*(kap+1)-h)/(g*W); rho[kap+1:]=dR/W; return rho
worst=0; tot=0; cnt=0; rows=[]
for p in pts:
    q=p['point']
    if q['eta']!='inf' and q['eta']!=float('inf') and str(q['eta'])!='inf': continue
    K,n,g,C,de=q['K'],q['n'],q['gam'],q['C'],q['delta']
    if not (n==100 or K==50): continue
    dR=1.0;W=dR+C;c=q['c'];eps=q['eps']
    for lam in (0.0,1.0):
        rho=sched(K,g,dR,C,c-lam*eps)
        N=n*K; P=np.zeros(N+1); P[0]=1.0; alive=1.0; tau=1e-9*max(1,c)
        viol=0.0
        for k in range(K):
            pmf=binom.pmf(np.arange(n+1),n,rho[k])
            P=np.convolve(P,pmf)[:N+1]
            # x_{k+1} = g*((k+1)dR - W*Ncum/n) > c+tau  <=> Ncum < n*((k+1)dR - (c+tau)/g)/W
            thr=n*((k+1)*dR-(c+tau)/g)/W
            idx=np.arange(N+1)<thr
            viol+=P[idx].sum(); P[idx]=0.0
        key=('%.2f'%lam)
        Vrun=p['marges']['1.0' if lam==1 else '0.0']['V']/1e5
        rows.append((q['i'],lam,viol,Vrun))
        if lam==1: worst=max(worst,viol); tot+=viol*1e5; cnt+=1
print("eta=inf computable points:",cnt,"max exact V at lam=1: %.3g"%worst,"expected total violations over these points: %.3f"%tot)
z=[(i,l,v,r) for i,l,v,r in rows if l==0]
mx=max(abs(r-v)/math.sqrt(max(v*(1-v),1e-12)/1e5) for i,l,v,r in z)
print("lam=0 run vs exact max reduced gap %.2f over %d points"%(mx,len(z)))

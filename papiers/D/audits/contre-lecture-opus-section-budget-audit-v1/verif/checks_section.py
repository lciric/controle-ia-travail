import math, numpy as np
def a_of(g,e): return 1-g/e if math.isfinite(e) else 1.0
def G(k,g,e):
    a=a_of(g,e); return g*k if a==1 else e*(1-a**k)
def jit(K,g,e,dR,C,c):
    W=dR+C; rho=np.zeros(K)
    if dR*G(K,g,e)<=c: return rho
    kap=min(k for k in range(K) if dR*G(k+1,g,e)>c)
    rho[kap]=(dR*G(kap+1,g,e)-c)/(g*W)
    rho[kap+1:]=(dR-(c/e if math.isfinite(e) else 0))/W
    return rho
def back(K,g,e,dR,C,c):
    a=a_of(g,e);W=dR+C;D=dR*G(K,g,e)-c;rho=np.zeros(K)
    if D<=0: return rho
    if a==0: rho[K-1]=D/(g*W); return rho
    m=max(mm for mm in range(K+1) if W*G(mm,g,e)<=D)
    rho[K-m:]=1
    if m<K: rho[K-1-m]=(D-W*G(m,g,e))/(g*W*a**m)
    return rho
def path(rho,g,e,dR,C,tauA=None):
    a=a_of(g,e);x=0;xs=[0]
    for r in rho:
        d=dR-(dR+C)*r
        x=a*x+g*d; xs.append(x)
    return np.array(xs)
# Proposition examples
dR,C,dind=1.0,9.0,0.1
def strat(tau):  # effective (dR,C) for stratum tau at trap-bound equality
    Cd=C*max(0,1-dind/tau); return tau*dR, tau*Cd
g,K=0.05,400
r=jit(K,g,math.inf,*strat(1.0),1.0)
x=path(r,g,math.inf,*strat(0.1)); print("ex1 eta=inf, stratum 0.1 under tau0=1 schedule: max x",x.max(),"final",x[-1])
r=jit(K,g,5.0,*strat(0.5),2.0)
x=path(r,g,5.0,*strat(1.0)); print("ex2 eta=5, stratum 1 under tau0=.5 schedule: max x",x.max(),"final",x[-1])
# monotonicity in gamma for uniform: schedule computed with gamma_hat>=gamma
rng=np.random.default_rng(1); bad_u=0; bad_f=0; nf=0
for t in range(20000):
    K=int(rng.integers(2,60)); g=float(rng.uniform(0.01,0.5)); e=float(rng.choice([math.inf, g*rng.uniform(1.0,40)]))
    gh=g*float(rng.uniform(1,3))
    if math.isfinite(e) and gh>e: continue
    dR=float(rng.uniform(0.2,2)); C=float(rng.uniform(0,20)); c=float(rng.uniform(0,3))
    r=jit(K,gh,e,dR,C,c); x=path(r,g,e,dR,C)
    if x.max()>c+1e-9: bad_u+=1
    rb=back(K,gh,e,dR,C,c); xb=path(rb,g,e,dR,C)
    if xb[-1]>c+1e-9: bad_f+=1
    nf+=1
print("uniform schedule from upper bound on gamma infeasible:",bad_u,"/",nf)
print("final (back-loaded) schedule from upper bound on gamma infeasible:",bad_f,"/",nf)
# eta upper bound safety for both
bad=0;n2=0
for t in range(20000):
    K=int(rng.integers(2,60)); g=float(rng.uniform(0.01,0.5)); e=g*float(rng.uniform(1.0,40)); eh=float(rng.choice([math.inf,e*rng.uniform(1,5)]))
    dR=float(rng.uniform(0.2,2)); C=float(rng.uniform(0,20)); c=float(rng.uniform(0,3))
    for f,crit in ((jit,'u'),(back,'f')):
        r=f(K,g,eh,dR,C,c); x=path(r,g,e,dR,C)
        v=x.max() if crit=='u' else x[-1]
        if v>c+1e-9: bad+=1
    n2+=1
print("schedules from upper bound on eta infeasible:",bad,"/",2*n2)
# detection example
T,k,d=257,1,0.05
from math import comb
Bs=min(B for B in range(T+1) if comb(T-k,B)/comb(T,B)<=d); print("B*det",Bs,"approx",T/k*math.log(1/d))

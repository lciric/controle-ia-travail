import numpy as np, itertools
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
rng=np.random.default_rng(0)
sig=lambda x:1/(1+np.exp(-x))
# --- 3a: NPG ODE vs time slice
p=np.array([.9,.07,.03]); eta=3.0; r=np.array([0.1,-0.4,0.9])
def f(t,th): 
    return r-(th-np.log(p))/eta
s=solve_ivp(f,[0,5],np.log(p),rtol=1e-10,atol=1e-12)
th=s.y[:,-1]; pi=np.exp(th)/np.exp(th).sum()
lam=1-np.exp(-5/eta); q=p*np.exp(eta*lam*r); q/=q.sum()
print("3a err",abs(pi-q).max())
# --- amplification structure
def g(l,pv,ph,a,b,eDR):
    return np.log(pv/ph)+eDR*l+np.log(1-a**l)-np.log(b**l-1)
ls=np.linspace(1e-4,1,20001)
bad=0
for _ in range(2000):
    a=rng.uniform(0,1); b=1+rng.exponential(3); eDR=rng.exponential(3)
    gg=g(ls,0.1,0.5,a,b,eDR); d2=np.diff(gg,2)
    al=-np.log(a); be=np.log(b)
    if al>be and (d2<-1e-9).any(): bad+=1
    if al<be and (d2>1e-9).any(): bad+=1
print("convex/concave violations",bad)
# re-entrance example
a=1e-3;b=2;eDR=3;ph=0.8;pv=0.105*ph
gg=g(ls,pv,ph,a,b,eDR); print("g(0+),min,g(1)",gg[0],gg.min(),gg[-1], "T_amp",np.log(ph*(b-1)/(pv*(1-a))))
# check directly with policies
def piA(l,p,beta,eDR):
    w=p*beta**l*np.array([1,np.exp(eDR*l),np.exp(eDR*l)]); return w/w.sum()
p3=np.array([ph,pv,1-ph-pv]); beta=np.array([1.0,0.5e-3,0.5])
for l in [0.01,0.2,0.9]:
    print(l, piA(l,p3,beta,eDR)[2]-piA(l,p3,np.ones(3),eDR)[2], g(l,pv,ph,a,b,eDR))
# sufficient condition check random
viol=0
for _ in range(20000):
    pp=rng.dirichlet([1,1,1]); bh=rng.uniform(0.2,1); bf=rng.uniform(0.01,bh); bv=rng.uniform(0,bf); eDR=rng.exponential(4)
    T=np.log(pp[0]*(bh-bf)/(pp[1]*(bf-bv)))
    l=rng.uniform(0,1)
    if eDR*l>=T:
        d=piA(l,pp,np.array([bh,bv,bf]),eDR)[2]-piA(l,pp,np.ones(3),eDR)[2]
        if d<=0: viol+=1
print("suff cond violations",viol)

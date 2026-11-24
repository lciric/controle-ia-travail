import numpy as np, math
from fractions import Fraction as F
rng=np.random.default_rng(7)
# Jensen B: bornes inferieures, y compris beta in {0,1}, R+C de signe quelconque, eta>0
viol=0; strict=0
for _ in range(100000):
    k=rng.integers(1,6); w=rng.dirichlet(np.ones(k))
    beta=rng.choice([0.0,1.0,0.5],size=k) if rng.random()<0.5 else rng.uniform(0,1,k)
    R=rng.uniform(-6,6); C=rng.uniform(-6,6); eta=rng.uniform(0.01,4)
    ex=float(np.dot(w,np.exp(eta*(beta*R-(1-beta)*C))))
    bb=float(np.dot(w,beta)); bd=math.exp(eta*(bb*R-(1-bb)*C))
    if bd>ex*(1+1e-12): viol+=1
    if ex>bd*(1+1e-9): strict+=1
print("violations",viol,"strict",strict)
# exact A: weight with beta=0 on part
w=np.array([.3,.7]);beta=np.array([0.,.5]);R=1.3;eta=2
print(np.dot(w,beta*math.exp(eta*R)), np.dot(w,beta)*math.exp(eta*R))
# condition billet: B stealth > A stealth iff eta(1-bv)(R0+dR+C)>log(1/bv), niche bf=bh=1
bad=0;n=0
for _ in range(200000):
    p=rng.dirichlet(np.ones(3)); ph,pv,pf=p
    bv=rng.uniform(0.01,0.99); R0=rng.uniform(-3,3); dR=rng.uniform(0.01,3); C=rng.uniform(-3,5); eta=rng.uniform(0.05,4)
    # A (R shift invariant)
    wA=np.array([ph,pv*bv*math.exp(eta*(R0+dR)),pf*math.exp(eta*(R0+dR))]);wA[0]*=math.exp(eta*R0)
    wB=np.array([ph*math.exp(eta*R0),pv*math.exp(eta*(bv*(R0+dR)-(1-bv)*C)),pf*math.exp(eta*(R0+dR))])
    # use logs-safe via ratio to honest
    sA=wA[2]/wA.sum(); sB=wB[2]/wB.sum()
    cond=eta*(1-bv)*(R0+dR+C)>math.log(1/bv)
    if abs(sB-sA)<1e-9: continue
    n+=1
    if (sB>sA)!=cond: bad+=1
print("condition billet: desaccords",bad,"sur",n)
# dTV melange
for q in (0.0,0.3,1.0):
    Po=np.array([.5,.5,0,0]);Q=np.array([0,0,.2,.8]);Pt=(1-q)*Po+q*Q
    print(q,0.5*abs(Po-Pt).sum())

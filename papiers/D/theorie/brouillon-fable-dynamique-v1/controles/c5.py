import numpy as np
from scipy.integrate import solve_ivp
exec(open('c4.py').read().split("found=0")[0])
rng=np.random.default_rng(4)
cnt=0; n=0
for _ in range(3000):
    q0=rng.uniform(.01,.9); s0=rng.uniform(.01,.6); bh=1; bf=rng.uniform(.6,1); bv=rng.uniform(0,.9)*bf; dR=1; kap=rng.uniform(0,.5); eta=rng.uniform(2,40)
    Cs=[0,0.1,0.2,0.5,1,2,4,8,16]
    res=[end(q0,s0,bv,bf,bh,dR,C,kap,eta) for C in Cs]
    ss=np.array([r[1] for r in res]); n+=1
    j=np.argmax(np.diff(ss))
    if np.diff(ss).max()>0.3:
        cnt+=1
        if cnt<=6:
            b0=bv+s0*(bf-bv)
            print(dict(q0=round(q0,3),s0=round(s0,3),bv=round(bv,3),bf=round(bf,3),kap=round(kap,3),eta=round(eta,2)),"Clow",round(b0/(1-b0),3),"Chigh",round(kap/(q0*(bf-bv))-1,3))
            for C,r in zip(Cs,res): print("   C",C,"end q,s",np.round(r[:2],4))
print("increase cases",cnt,"of",n)

import numpy as np
from scipy.integrate import solve_ivp
rng=np.random.default_rng(3)
def sig(x): return 0.5*(1+np.tanh(x/2))
def end(q0,s0,bv,bf,bh,dR,C,kap,eta,T=None):
    A0=bv*dR-(bh-bv)*C; D=(bf-bv)*(dR+C); u0=np.log(q0/(1-q0)); w0=np.log(s0/(1-s0))
    f=lambda t,x:[A0+D*sig(x[1])-(x[0]-u0)/eta, D*sig(x[0])-kap-(x[1]-w0)/eta]
    s=solve_ivp(f,[0,T or 60*eta],[u0,w0],rtol=1e-9,atol=1e-11,method='LSODA')
    return sig(s.y[0,-1]),sig(s.y[1,-1]),sig(s.y[1].max())
found=0
for _ in range(3000):
    q0=rng.uniform(.01,.6); s0=rng.uniform(.01,.4); bh=1; bf=rng.uniform(.6,1); bv=rng.uniform(0,.5)*bf; dR=1; kap=rng.uniform(0,.5); eta=rng.uniform(5,40)
    Cs=[0.2,0.5,1,2,4,8,16]
    res=[end(q0,s0,bv,bf,bh,dR,C,kap,eta) for C in Cs]
    ss=[r[1] for r in res]
    # look for low->high flip as C increases
    for i in range(len(Cs)-1):
        if ss[i]<0.3 and ss[i+1]>0.9 and res[i+1][0]>0.9:
            found+=1
            if found<=6:
                b0=bv+s0*(bf-bv)
                print(dict(q0=round(q0,3),s0=round(s0,3),bv=round(bv,3),bf=round(bf,3),kap=round(kap,3),eta=round(eta,2)),"Clow",round(b0/(1-b0),3),"Chigh",round(kap/(q0*(bf-bv))-1,3))
                for C,r in zip(Cs,res): print("   C",C,"end q,s",np.round(r[:2],4))
            break
print("found flips",found)

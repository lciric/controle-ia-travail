"""Detail d'un basculement honnete -> triche obscurcie induit par une hausse de C, et recherche a q0 petit."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
def sig(x): return 0.5*(1+np.tanh(np.asarray(x)/2))
def logit(p): return np.log(p)-np.log1p(-p)
def eqs(u0,w0,eta,A0,D,kap):
    Phi=lambda w: w0+eta*(D*sig(u0+eta*(A0+D*sig(w)))-kap)
    ws=np.linspace(w0-eta*kap-1,w0+eta*(D-kap)+1,400001); h=Phi(ws)-ws
    idx=np.where(np.sign(h[1:])!=np.sign(h[:-1]))[0]
    return [brentq(lambda w:Phi(w)-w,ws[i],ws[i+1],xtol=1e-14) for i in idx]
def run(q0,s0,bh,bv,bf,dR,kap,eta,C):
    A0=bv*dR-(bh-bv)*C; D=(bf-bv)*(dR+C); u0,w0=logit(q0),logit(s0)
    f=lambda t,x:[A0+D*sig(x[1])-(x[0]-u0)/eta, D*sig(x[0])-kap-(x[1]-w0)/eta]
    s=solve_ivp(f,[0,1000*eta],[u0,w0],rtol=1e-11,atol=1e-12,method='LSODA')
    E=[(sig(u0+eta*(A0+D*sig(w))),sig(w)) for w in eqs(u0,w0,eta,A0,D,kap)]
    return A0,D,(sig(s.y[0,-1]),sig(s.y[1,-1])),E
# exemple arrondi
q0,s0,bh,bv,bf,dR,kap,eta=0.8,0.8,1.,0.04,0.85,1.,1.2,40.
b0=bv+s0*(bf-bv); print("C_low=%.4f C_high=%.4f kappa_dagger=%.4f"%(b0*dR/(bh-b0),kap/(q0*(bf-bv))-dR,q0*(bf-bv)*bh*dR/(bh-b0)))
for C in [0,0.1,0.2,0.27,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.8,1.0,1.5,2.0,2.5,3.0]:
    A0,D,lim,E=run(q0,s0,bh,bv,bf,dR,kap,eta,C)
    print("C=%.2f A0+Ds0=%+.3f Dq0-kap=%+.3f limite (q,s)=(%.3g,%.3g) ; equilibres %s"%(C,A0+D*s0,D*q0-kap,lim[0],lim[1],[(float('%.3g'%a),float('%.3g'%b)) for a,b in E]))
# recherche a q0 <= 0.3
rng=np.random.default_rng(np.random.SeedSequence(20261124).spawn(5)[4]); n=0
for it in range(600):
    q0=rng.uniform(.01,.3); s0=rng.uniform(.3,.95); bf=rng.uniform(.5,1); bv=rng.uniform(0,.5)*bf; kap=rng.uniform(.2,2); eta=rng.uniform(5,80)
    b0=bv+s0*(bf-bv); Clow=b0/(1-b0); Cs=np.linspace(0,1.5*Clow,30)
    prev=None
    for C in Cs:
        _,_,lim,_=run(q0,s0,1.,bv,bf,1.,kap,eta,C)
        if prev is not None and prev[0]<.1 and lim[0]>.9 and lim[1]>.9:
            n+=1
            if n<=3: print("q0 petit : q0=%.3f s0=%.3f bv=%.3f bf=%.3f kap=%.3f eta=%.1f : C %.3f->%.3f, limite %s -> %s"%(q0,s0,bv,bf,kap,eta,Cprev,C,np.round(prev,4),np.round(lim,4)))
            break
        prev=lim; Cprev=C
print("basculements a q0<=0.3 :",n,"sur 600")

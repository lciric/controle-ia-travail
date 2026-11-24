import numpy as np, itertools
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
rng=np.random.default_rng(1)
# order h,v,f
def a_vec(pi,beta,R):
    Z=(pi*beta).sum(); b=(pi*beta*R).sum()/Z
    return beta*(R-b)/Z, b, Z
def run(p,beta,dR,eta,T,n=4000):
    R=np.array([0,dR,dR])
    def f(t,phi):
        w=p*np.exp(phi-phi.max()); pi=w/w.sum()
        a,_,_=a_vec(pi,beta,R)
        return a-(phi/eta if np.isfinite(eta) else 0)
    s=solve_ivp(f,[0,T],np.zeros(3),rtol=1e-10,atol=1e-12,t_eval=np.linspace(0,T,n),method='LSODA')
    W=p[:,None]*np.exp(s.y-s.y.max(0)); return s.t, W/W.sum(0), s.y
# REINFORCE exact expectation N=2,3 by enumeration
p=np.array([.6,.25,.15]); beta=np.array([.9,.2,.6]); R=np.array([0,1.,1.])
acc=p*beta/(p*beta).sum()
for N in [2,3]:
    g=np.zeros(3)
    for xs in itertools.product(range(3),repeat=N):
        pr=np.prod(acc[list(xs)]); Rb=R[list(xs)].mean()
        for x in xs:
            e=np.zeros(3); e[x]=1
            g+=pr*(R[x]-Rb)*(e-p)/N
    a,b,Z=a_vec(p,beta,R)
    print("REINFORCE N",N, g, (N-1)/N*p*a)
# unregularized: invariant, limit, bounds
for trial in range(5):
    p=rng.dirichlet([5,1,1]); bh=rng.uniform(.5,1); bf=rng.uniform(.05,bh); bv=rng.uniform(0,bf); beta=np.array([bh,bv,bf]); dR=1.0
    t,pi,phi=run(p,beta,dR,np.inf,400/ (bf))
    inv=np.abs(np.log(pi[1]/p[1])-(bv/bf)*np.log(pi[2]/p[2])).max()
    xs=brentq(lambda x:x+p[1]*(x/p[2])**(bv/bf)-1,p[2],1)
    lo=np.log(pi[2]/pi[0])-np.log(p[2]/p[0])
    rate_ok=(np.diff(lo)/np.diff(t)>=bf*dR/bh-1e-6).all()
    L=np.log(p[0]/p[2]); 
    tdom=t[np.argmax(lo>L)] if (lo>L).any() else np.inf
    print("inv",inv,"limit",pi[2,-1],xs,"pih_end",pi[0,-1],"rate_ok",rate_ok,"tdom",tdom,"bound",L*bh/(bf*dR), "nomon limit",p[2]/(p[1]+p[2]))
# regularized trapped example
p=np.array([1-2e-4,1e-4,1e-4]); beta=np.array([1,.05,.1]); dR=1; eta=20
t,pi,phi=run(p,beta,dR,eta,2000)
L=np.log(p[0]/p[2]); y=phi[2]-phi[0]
c=(p[1]+p[2])/p[0]; rho=.1
print("L",L,"max y",y.max(),"final pi",pi[:,-1])
for yb in [3,4,5,6]:
    print(yb, eta*rho*dR*(1+c*np.exp(yb))**2, "<=",yb)
print("static A dominance:", eta*dR, ">", L+np.log(1/rho))
# other equilibria: start near delta_f
def run_from(phi0,T=2000):
    R=np.array([0,dR,dR])
    def f(t,phi):
        w=p*np.exp(phi-phi.max()); pi_=w/w.sum()
        a,_,_=a_vec(pi_,beta,R)
        return a-phi/eta
    s=solve_ivp(f,[0,T],phi0,rtol=1e-10,atol=1e-12,method='LSODA')
    w=p*np.exp(s.y[:,-1]-s.y[:,-1].max()); return w/w.sum()
print("from high init:",run_from(np.array([0,0,20.])))
# lower bound check y>= eta*lam*rho*dR
lam=1-np.exp(-t/eta); print("lower bound ok",(y>=eta*lam*rho*dR-1e-8).all())

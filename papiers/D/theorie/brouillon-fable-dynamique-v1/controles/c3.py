import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
rng=np.random.default_rng(2)
sig=lambda x:1/(1+np.exp(-x))
# closed forms for a
bad=0
for _ in range(100000):
    pi=rng.dirichlet([1,1,1]); bh=rng.uniform(.05,1); bf=rng.uniform(.001,bh); bv=rng.uniform(0,bf); dR=rng.exponential(1)
    beta=np.array([bh,bv,bf]); R=np.array([0,dR,dR]); Z=(pi*beta).sum(); b=(pi*beta*R).sum()/Z; a=beta*(R-b)/Z
    m=pi[1]*bv+pi[2]*bf
    cf=np.array([-bh*m*dR/Z**2, bv*bh*pi[0]*dR/Z**2, bf*bh*pi[0]*dR/Z**2])
    if not np.allclose(a,cf,rtol=1e-8,atol=1e-10): bad+=1
    if a[2]-a[0] < bf*dR/bh*(1-1e-9): bad+=1
    if abs((pi*a).sum())>1e-8*max(1,abs(a).max()): bad+=1
print("3c closed form violations",bad)
# Theorem 4
def F(w,u0,w0,eta,A0,D,kap): return w0+eta*(D*sig(u0+eta*(A0+D*sig(w)))-kap)
maxroots=0; infl_bad=0
for _ in range(4000):
    u0=rng.normal(0,4); w0=rng.normal(0,4); eta=rng.exponential(5)+.1; A0=rng.normal(0,2); D=rng.exponential(2)+.01; kap=rng.exponential(1)
    lo=w0-eta*kap-1; hi=w0+eta*(D-kap)+1
    ws=np.linspace(lo,hi,200001); h=F(ws,u0,w0,eta,A0,D,kap)-ws
    sc=(np.sign(h[1:])!=np.sign(h[:-1])).sum(); maxroots=max(maxroots,sc)
    # inflection count over wide range
    ww=np.linspace(-40,40,40001); s=sig(ww); H=1-2*s-eta*D*s*(1-s)*np.tanh((u0+eta*A0+eta*D*s)/2)
    if (np.sign(H[1:])!=np.sign(H[:-1])).sum()!=1: infl_bad+=1
print("max #fixed points",maxroots,"inflection anomalies",infl_bad)
# explicit instance
bv,bf,bh=0.,1.,1.; dR=1.; C=1.; A0=bv*dR-(bh-bv)*C; D=(bf-bv)*(dR+C); kap=.1; eta=20.; q0=s0=.01
u0=np.log(q0/(1-q0)); w0=np.log(s0/(1-s0))
ws=np.linspace(w0-eta*kap-1,w0+eta*(D-kap)+1,2000001); h=F(ws,u0,w0,eta,A0,D,kap)-ws
idx=np.where(np.sign(h[1:])!=np.sign(h[:-1]))[0]
roots=[brentq(lambda w:F(w,u0,w0,eta,A0,D,kap)-w,ws[i],ws[i+1],xtol=1e-13) for i in idx]
def kl(a,b):
    a=np.clip(a,1e-300,1-1e-16); return a*np.log(a/b)+(1-a)*np.log((1-a)/(1-b))
def J(q,s): return q*(A0+D*s)-kap*s-(kl(q,q0)+kl(s,s0))/eta
for w in roots:
    u=u0+eta*(A0+D*sig(w)); Fp=eta**2*D**2*sig(u)*(1-sig(u))*sig(w)*(1-sig(w))
    print("eq u,w",u,w,"q,s",sig(u),sig(w),"F'",Fp,"J",J(sig(u),sig(w)))
print("cert:",A0+D*s0,"<=0 ;",q0*D,"<=",kap,"; J(1,1) lower",A0+D-kap-np.log(1/(q0*s0))/eta, "J(x0)",J(q0,s0))
print("cond L:",sig(u0+eta*(A0+D*sig(w0-eta*kap/2))),"<",kap/(2*D)," cond H:",sig(u0+eta*(A0+D*sig(w0+eta*(D-kap)/2))),">",(D+kap)/(2*D))
def f(t,x): return [A0+D*sig(x[1])-(x[0]-u0)/eta, D*sig(x[0])-kap-(x[1]-w0)/eta]
s=solve_ivp(f,[0,400],[u0,w0],rtol=1e-10,atol=1e-12)
print("traj end",s.y[:,-1],"max u-u0",(s.y[0]-u0).max(),"max w-w0",(s.y[1]-w0).max())
# eigenvalue check
w=roots[0]; u=u0+eta*(A0+D*sig(w))
Jm=np.array([[-1/eta,D*sig(w)*(1-sig(w))],[D*sig(u)*(1-sig(u)),-1/eta]])
Fp=eta**2*D**2*sig(u)*(1-sig(u))*sig(w)*(1-sig(w))
print(np.linalg.eigvals(Jm), -(1-np.sqrt(Fp))/eta, -(1+np.sqrt(Fp))/eta)
# penalty window & beyond C_high: does trajectory reach the stealth node?
for C in [0.5,1,3,4,5,8,20,100]:
    A0=bv*dR-(bh-bv)*C; D=(bf-bv)*(dR+C)
    b0=bv+s0*(bf-bv); Clow=b0*dR/(bh-b0); Chigh=kap/(q0*(bf-bv))-dR
    s=solve_ivp(f,[0,5000],[u0,w0],rtol=1e-10,atol=1e-12,method='LSODA')
    print("C",C,"window",Clow,Chigh,"end q,s",sig(s.y[0,-1]),sig(s.y[1,-1]),"max s",sig(s.y[1].max()))

import numpy as np, itertools
from scipy.integrate import solve_ivp
rng=np.random.default_rng(7)
def sig(x): return 0.5*(1+np.tanh(x/2))
# certificates random test
viol=[0,0,0,0]; used=[0,0,0,0]
for _ in range(1500):
    q0=rng.uniform(.005,.8); s0=rng.uniform(.005,.8); bh=rng.uniform(.6,1); bf=rng.uniform(.3,1)*bh; bv=rng.uniform(0,1)*bf*0.95
    dR=1; C=rng.exponential(3); kap=rng.exponential(.5); eta=rng.uniform(1,30)
    A0=bv*dR-(bh-bv)*C; D=(bf-bv)*(dR+C); u0=np.log(q0/(1-q0)); w0=np.log(s0/(1-s0))
    f=lambda t,x:[A0+D*sig(x[1])-(x[0]-u0)/eta, D*sig(x[0])-kap-(x[1]-w0)/eta]
    s=solve_ivp(f,[0,40*eta],[u0,w0],rtol=1e-9,atol=1e-11,method='LSODA')
    U,W=s.y; tol=1e-6
    ub=u0+eta*max(A0+D*s0,0)
    if D*sig(ub)<=kap:
        used[0]+=1; viol[0]+= (U.max()>ub+tol) or (W.max()>w0+tol)
    wb=w0+eta*max(D*q0-kap,0)
    if A0+D*sig(wb)<=0:
        used[1]+=1; viol[1]+= (U.max()>u0+tol) or (W.max()>wb+tol)
    b0=bv+s0*(bf-bv); Clow=b0*dR/(bh-b0); Chigh=kap/(q0*(bf-bv))-dR
    assert (Clow<=C<=Chigh)==((A0+D*s0<=0) and (D*q0<=kap))
    kd=q0*(bf-bv)*bh*dR/(bh-b0); assert (Clow<=Chigh)==(kap>=kd)
    if Chigh<=C<=Clow:
        used[2]+=1; viol[2]+= (np.diff(U).min()<-1e-6) or (np.diff(W).min()<-1e-6) or (W[-1]<w0+eta*(D*q0-kap)-1e-5) or (U[-1]<u0+eta*(A0+D*s0)-1e-5)
    if Clow<=C<=Chigh:
        used[3]+=1; viol[3]+= (np.diff(U).max()>1e-6) or (np.diff(W).max()>1e-6)
print("cert used",used,"viol",viol)
# best-of-N exact enumeration
pacc=np.array([.7,.1,.2]); R=np.array([0,1,1]); N=3
sel=np.zeros(3)
for xs in itertools.product(range(3),repeat=N):
    pr=np.prod(pacc[list(xs)]); m=max(R[list(xs)]); best=[x for x in xs if R[x]==m]
    for x in best: sel[x]+=pr/len(best)
a=.3; ratio=(sel[2]/pacc[2])/(sel[0]/pacc[0]); print("bestN ratio",ratio, sum((1-a)**(-i) for i in range(N)))
# anchored c_k
al=.2; c=0
for k in range(1,6):
    c=(1-al)*(c+1); print(k,c,(1-al)/al*(1-(1-al)**k))
# g'' analytic sign check
bad=0
for _ in range(20000):
    lv=rng.exponential(3)+1e-3; lh=rng.exponential(2)+1e-3; l=rng.uniform(.01,5)
    # g'' = -lv^2 e^{lv l}/(e^{lv l}-1)^2 + lh^2 e^{lh l}/(e^{lh l}-1)^2
    h=lambda c: c*c*np.exp(c*l)/np.expm1(c*l)**2
    d2=-h(lv)+h(lh)
    if (lv>lh and d2<-1e-12) or (lv<lh and d2>1e-12): bad+=1
print("g'' sign violations",bad)
# operator A uniqueness quick check
mx=0
for _ in range(2000):
    lv=rng.uniform(0,4); eta=rng.exponential(10)+.1; u0=rng.normal(0,3); w0=rng.normal(0,3); kap=rng.exponential(.3); dR=1; lh=rng.exponential(1)+lv
    A0=dR-lh/eta; D=lv/eta
    ws=np.linspace(w0-eta*kap-1,w0+lv+1,20001); h=w0+eta*(D*sig(u0+eta*(A0+D*sig(ws)))-kap)-ws
    mx=max(mx,(np.sign(h[1:])!=np.sign(h[:-1])).sum())
print("A: max fixed points for lv<4:",mx)

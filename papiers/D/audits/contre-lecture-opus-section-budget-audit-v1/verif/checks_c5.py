import math, numpy as np
from scipy.optimize import minimize
rng=np.random.default_rng(7)
def lse(v): m=v.max(); return m+math.log(np.exp(v-m).sum())
# 1. Lemma and dynamics: tabular NPG with KL anchor vs tilt recursion, visible stratum with non-constant reward
worst_l=worst_np=worst_fix=0
for t in range(300):
    nh,nv,nf=rng.integers(1,5,size=3); X=nh+nv+nf
    p0=rng.dirichlet(np.ones(X)); th0=np.log(p0)
    eta=float(rng.choice([math.inf, rng.uniform(0.5,10)])); g=float(rng.uniform(0.01,1))*(1 if math.isinf(eta) else min(1,eta))
    if not math.isinf(eta): g=min(g,eta)
    a=1.0 if math.isinf(eta) else 1-g/eta
    K=int(rng.integers(1,30))
    th=th0.copy(); phi=np.zeros(X); xs=[]
    hidx=np.arange(nh); vidx=np.arange(nh,nh+nv); fidx=np.arange(nh+nv,X)
    L=math.log(p0[hidx].sum()/p0[fidx].sum())
    d=[]
    for k in range(K):
        r=np.zeros(X); rh=rng.normal(); rf=rng.normal()
        r[hidx]=rh; r[fidx]=rf; r[vidx]=rng.normal(size=nv)   # visible non-constant
        d.append(rf-rh)
        # NPG: theta += g*P(grad_pi V), grad_pi V = r - (log pi - log p0 + 1)/eta
        pi=np.exp(th-lse(th))
        gradpi = r - ((np.log(pi)-np.log(p0)+1)/eta if not math.isinf(eta) else 0)
        Fm=np.diag(pi)-np.outer(pi,pi); gth=Fm@gradpi
        th=th+g*(np.linalg.pinv(Fm)@gth)
        phi=a*phi+g*r
    pi_np=np.exp(th-lse(th)); pi_tilt=np.exp(np.log(p0)+phi-lse(np.log(p0)+phi))
    worst_np=max(worst_np,np.abs(pi_np-pi_tilt).max())
    ell=math.log(pi_tilt[fidx].sum()/pi_tilt[hidx].sum())
    pred=-L+g*sum(a**(K-1-j)*d[j] for j in range(K))
    worst_l=max(worst_l,abs(ell-pred))
print("NPG vs tilt max gap %.2e ; lemma max gap %.2e"%(worst_np,worst_l))
# 2. proximal characterisation: maximiser of g E[r] - (1-a)KL(pi||p0) - a KL(pi||pk)
mx=0
for t in range(50):
    X=5; p0=rng.dirichlet(np.ones(X)); pk=rng.dirichlet(np.ones(X)); r=rng.normal(size=X)
    eta=rng.uniform(0.5,5); g=rng.uniform(0.05,eta); a=1-g/eta
    target=np.exp(np.log(p0)+a*(np.log(pk)-np.log(p0))+g*r); target/=target.sum()
    obj=lambda z: -(g*(np.exp(z-lse(z))*r).sum() - (1-a)*(np.exp(z-lse(z))*(z-lse(z)-np.log(p0))).sum() - a*(np.exp(z-lse(z))*(z-lse(z)-np.log(pk))).sum())
    res=minimize(obj,np.zeros(X),method='BFGS',options={'gtol':1e-12})
    z=res.x; pi=np.exp(z-lse(z)); mx=max(mx,np.abs(pi-target).max())
    # proximal on exact objective E r - KL0/eta - KLk/s with s=g/a gives same law
    s=g/a; lam=1/(1/eta+1/s)
    t2=np.exp(lam*r+(lam/eta)*np.log(p0)+(lam/s)*np.log(pk)); t2/=t2.sum()
    mx=max(mx,np.abs(t2-target).max())
print("proximal maximiser gap %.2e (exact-proximal step size g/a also matches)"%mx)
# 3. fixed point / effective pressure
eta=3.0; g=0.4; a=1-g/eta; r=rng.normal(size=4); phi=np.zeros(4)
for k in range(1,40): phi=a*phi+g*r; assert np.allclose(phi, eta*(1-a**k)*r)
print("phi_k = eta(1-a^k) r : OK")
# 4. static limit vs R1 Operator B and C*_R3
dR=1.0; Ca=4.0; eta=5.0; rho=0.3; L=2.0
lim=-L+eta*(dR-(dR+Ca)*rho)
bf=1-rho; R1=math.log(1/math.e**L)+eta*(bf*dR-(1-bf)*Ca)
print("static limit %.6f vs R1 Operator B %.6f"%(lim,R1))
tau=0.7; Cstar=((1-rho)*tau+0)/(rho*1*tau)*dR
print("C*_R3 at eps_trap=delta_ind=0: %.6f vs (1-rho)dR/rho %.6f"%(Cstar,(1-rho)*dR/rho))
# 5. counterexamples for gamma in the final criterion
def G(k,g,eta): return g*k if math.isinf(eta) else eta*(1-(1-g/eta)**k)
def back(K,g,eta,dR,C,c):
    W=dR+C;a=1.0 if math.isinf(eta) else 1-g/eta;D=dR*G(K,g,eta)-c;rho=np.zeros(K)
    if D<=0: return rho
    if a==0: rho[K-1]=D/(g*W); return rho
    m=max(mm for mm in range(K+1) if W*G(mm,g,eta)<=D+1e-15)
    rho[K-m:]=1
    if m<K: rho[K-1-m]=(D-W*G(m,g,eta))/(g*W*a**m)
    return rho
def xK(rho,g,eta,dR,C):
    a=1.0 if math.isinf(eta) else 1-g/eta; x=0
    for rr in rho: x=a*x+g*dR-g*(dR+C)*rr
    return x
bad1=bad2=n1=n2=0
for t in range(20000):
    K=int(rng.integers(2,80)); eta=float(rng.uniform(0.5,10)); g=float(rng.uniform(0.01,0.99))*eta
    dR=float(rng.uniform(0.2,2)); C=float(rng.uniform(0,20)); c=float(rng.uniform(0,3)); a=1-g/eta
    # upper bound gamma_hat = eta
    if eta*dR-c>0:
        x=xK(back(K,eta,eta,dR,C,c),g,eta,dR,C); pred=a*(dR*G(K-1,g,eta)-c)
        n1+=1; bad1+= abs((x-c)-pred)>1e-9
    # lower bound at eta=inf
    gh=g*float(rng.uniform(0.1,0.99)); D=dR*g*K-c
    if c>0 and D>0:
        x=xK(back(K,gh,math.inf,dR,C,c),g,math.inf,dR,C); n2+=1; bad2+= not (x>c+1e-12)
print("ex1 formula x_K-c = a(dR G_{K-1}-c): mismatches %d / %d"%(bad1,n1))
print("ex2 lower bound at eta=inf infeasible: failures %d / %d"%(bad2,n2))

import numpy as np, math
from scipy.optimize import linprog
from scipy.special import comb
rng = np.random.default_rng(np.random.SeedSequence(20261124))

def G(k,gam,eta):
    a = 1-gam/eta if np.isfinite(eta) else 1.0
    return gam*sum(a**i for i in range(k))

def closed_final(K,gam,eta,dR,C,c):
    a = 1-gam/eta if np.isfinite(eta) else 1.0
    S=dR+C; D=dR*G(K,gam,eta)-c
    if D<=0: return 0.0
    if a==0: return D/(gam*S)
    m=max(mm for mm in range(K+1) if S*G(mm,gam,eta)<=D+1e-15)
    return m+(D-S*G(m,gam,eta))/(gam*S*a**m)

def closed_unif(K,gam,eta,dR,C,c):
    a = 1-gam/eta if np.isfinite(eta) else 1.0
    S=dR+C
    if dR*G(K,gam,eta)<=c: return 0.0
    kap=min(k for k in range(K) if dR*G(k+1,gam,eta)>c)
    rk=(dR*G(kap+1,gam,eta)-c)/(gam*S)
    rh=(dR-(c/eta if np.isfinite(eta) else 0))/S
    assert 0<rk<=rh+1e-12<=dR/S+1e-12
    v=rk+(K-1-kap)*rh
    # identity form
    xs=[min(c,dR*G(k,gam,eta)) for k in range(K+1)]
    v2=(K*gam*dR-(1-a)*sum(xs[1:K])-xs[K])/(gam*S)
    assert abs(v-v2)<1e-9,(v,v2)
    return v

def lp(K,gam,eta,dR,C,c,uniform):
    a = 1-gam/eta if np.isfinite(eta) else 1.0
    S=dR+C
    rows=[];rhs=[]
    ks = range(1,K+1) if uniform else [K]
    for k in ks:
        # gam*dR*sum a^{k-1-j} - gam*S*sum a^{k-1-j} rho_j <= c
        row=np.zeros(K)
        for j in range(k): row[j]=-gam*S*a**(k-1-j)
        rows.append(row); rhs.append(c-dR*G(k,gam,eta))
    r=linprog(np.ones(K),A_ub=np.array(rows),b_ub=np.array(rhs),bounds=[(0,1)]*K,method='highs')
    if r.status!=0: return None
    return r.fun

mx=0
for t in range(3000):
    K=int(rng.integers(1,25)); gam=float(rng.uniform(0.02,1.0))
    mode=rng.integers(0,4)
    eta = gam if mode==0 else (np.inf if mode==1 else gam*float(rng.uniform(1,30)))
    dR=float(rng.uniform(0.1,3)); C=float(rng.choice([0,rng.uniform(0,20)])); c=float(rng.choice([0,rng.uniform(0,5)]))
    for uni in (False,True):
        v=lp(K,gam,eta,dR,C,c,uni)
        if v is None:
            assert C==0 and c==0,(K,gam,eta,dR,C,c); v=float(K) if not (eta==gam and not uni) else 1.0
        w=(closed_unif if uni else closed_final)(K,gam,eta,dR,C,c)
        mx=max(mx,abs(v-w))
        if abs(v-w)>1e-6: print("MISMATCH",uni,K,gam,eta,dR,C,c,v,w)
print("max LP-vs-closed-form gap",mx)

# explicit m and kappa formulas
for t in range(3000):
    K=int(rng.integers(1,40)); gam=float(rng.uniform(0.02,1.0)); eta=gam*float(rng.uniform(1.01,30))
    a=1-gam/eta
    dR=float(rng.uniform(0.1,3)); C=float(rng.uniform(0,20)); c=float(rng.uniform(0,5)); S=dR+C
    D=dR*G(K,gam,eta)-c
    if D>0:
        m=max(mm for mm in range(K+1) if S*G(mm,gam,eta)<=D)
        m2=math.floor(math.log(1-D/(eta*S))/math.log(a))
        assert m==m2,(m,m2)
        bound=1+(eta/gam)*math.log(eta*S/(eta*C+c))
        assert closed_final(K,gam,eta,dR,C,c)<=bound+1e-9
        kap=min(k for k in range(K) if dR*G(k+1,gam,eta)>c)
        kap2=math.floor(math.log(1-c/(eta*dR))/math.log(a))
        assert kap==kap2,(kap,kap2)
print("explicit m, kappa OK")

# detection bounds
bad=0
for T in [5,17,60,200]:
    for k in range(1,T+1):
        for B in range(0,T+1):
            q=comb(T-k,B,exact=True)/comb(T,B,exact=True)
            q2=comb(T-B,k,exact=True)/comb(T,k,exact=True)
            assert abs(q-q2)<1e-12
            if B<=T-k:
                lo=(1-B/(T-k+1))**k; hi=(1-B/T)**k
                assert lo<=q+1e-12 and q<=hi+1e-12 and hi<=math.exp(-k*B/T)+1e-12
        for delta in [0.5,0.1,0.01,1e-4]:
            Bs=min(B for B in range(0,T+1) if comb(T-k,B,exact=True)/comb(T,B,exact=True)<=delta)
            lo=(T-k+1)*(1-delta**(1/k)); up=math.ceil(T*(1-delta**(1/k))-1e-12)
            lo2=(T-k+1)*math.log(1/delta)/(k+math.log(1/delta)); up2=math.ceil(T/k*math.log(1/delta))
            if not (lo2<=lo+1e-9 and lo<=Bs+1e-9 and Bs<=up and up<=up2): bad+=1; print("bad",T,k,delta,Bs,lo,up)
            # user's suggested lower bound
print("detection bounds violations:",bad)
T=100;k=1;delta=0.01
print("counterexample to (T-k+1)/k log(1/delta) lower bound: B*=",min(B for B in range(T+1) if comb(T-k,B,exact=True)/comb(T,B,exact=True)<=delta),"claimed lb",(T-k+1)/k*math.log(1/delta))

# Bernstein coverage simulation
def sim(K,n,gam,eta,dR,C,c,delta,reps=4000):
    a=1-gam/eta if np.isfinite(eta) else 1.0
    S=dR+C; Lam=math.log(2*K/delta); rbar=dR/S
    Gam=sum(a**(2*i) for i in range(K))
    eps=gam*S*(math.sqrt(2*rbar*Gam*Lam/n)+2*Lam/(3*n))
    if eps>c: return None
    cc=c-eps
    # greedy schedule for headroom cc
    x=0;rho=[]
    for k in range(K):
        r=max(0.0,(a*x+gam*dR-cc)/(gam*S)); rho.append(r); x=a*x+gam*dR-gam*S*r
    rho=np.array(rho); assert rho.max()<=rbar+1e-12
    Bbar=n*rho.sum(); Bstar=n*closed_unif(K,gam,eta,dR,C,c)
    infl=n*eps*((K-1)/eta+1/gam)/S if np.isfinite(eta) else n*eps/(gam*S)
    assert Bbar<=Bstar+infl+1e-9
    Lp=math.log(2/delta); Brand=Bbar+math.sqrt(2*Bbar*Lp)+2*Lp/3
    A=rng.binomial(n,rho,size=(reps,K))
    xh=np.zeros(reps); viol=np.zeros(reps,bool)
    for k in range(K):
        xh=a*xh+gam*dR-gam*S*A[:,k]/n
        viol|=xh>c+1e-12
    over=A.sum(1)>Brand
    return dict(eps=eps,Bstar=Bstar,Bbar=Bbar,Brand=Brand,fail=float((viol|over).mean()),viol=float(viol.mean()),over=float(over.mean()))
for args in [(200,200,0.1,2.0,1.0,9.0,2.0,0.05),(200,2000,0.1,2.0,1.0,9.0,2.0,0.05),(500,500,0.05,np.inf,1.0,19.0,3.0,0.05),(100,1000,0.2,1.0,1.0,4.0,0.5,0.1)]:
    print(args,sim(*args))

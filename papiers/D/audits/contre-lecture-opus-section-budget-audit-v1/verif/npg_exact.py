import math, numpy as np
rng=np.random.default_rng(3)
def lse(v): m=v.max(); return m+math.log(np.exp(v-m).sum())
w1=w2=0
for t in range(300):
    X=int(rng.integers(3,12)); p0=rng.dirichlet(np.ones(X)); eta=float(rng.uniform(0.5,10)); g=float(rng.uniform(0.01,1))*eta; a=1-g/eta
    th=np.log(p0).copy(); phi=np.zeros(X)
    for k in range(int(rng.integers(1,40))):
        r=rng.normal(size=X); pi=np.exp(th-lse(th))
        gp=r-(np.log(pi)-np.log(p0)+1)/eta
        Fm=np.diag(pi)-np.outer(pi,pi)
        # projector check: F^+ F z = z - mean(z)
        z=rng.normal(size=X); w2=max(w2,np.abs(np.linalg.pinv(Fm,rcond=1e-14)@(Fm@z)-(z-z.mean())).max())
        th=th+g*(gp-gp.mean()); phi=a*phi+g*r
    pt=np.exp(np.log(p0)+phi-lse(np.log(p0)+phi)); pn=np.exp(th-lse(th)); w1=max(w1,np.abs(pt-pn).max())
print("NPG (exact projector) vs tilt: %.2e ; pinv projector check: %.2e"%(w1,w2))

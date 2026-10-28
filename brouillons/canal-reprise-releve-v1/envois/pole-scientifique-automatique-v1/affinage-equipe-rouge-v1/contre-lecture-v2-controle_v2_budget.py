# Illustratif, non préenregistré, non opposable. Même modèle gaussien ; budget porté à U_max=3000 grappes.
import numpy as np
rng=np.random.default_rng(np.random.SeedSequence([20261028,2]))
def proc(theta,delta,kappa,U,R):
    x=rng.normal(theta,1,(R,U)); d=delta*(1-kappa); m=delta*(1+kappa)/2
    return np.cumsum(d*(x-m),axis=1)
def surv(theta,delta,kappa,a,U,R):
    ls=proc(theta,delta,kappa,U,R); cs=ls>=np.log(1/a); cr=-ls>=np.log(1/0.01)
    fs=np.where(cs.any(1),cs.argmax(1),U+1); fr=np.where(cr.any(1),cr.argmax(1),U+1)
    return ((fs<fr)&(fs<=U)).mean()
grille=[0.05,1e-2,1e-3,1e-4,1e-5,1e-6,1e-8,1e-10]
U=3000
for theta in [0.3]:
  for dl in [0.1,0.15,0.2,0.3,0.4]:
    ok=[a for a in grille if surv(dl,dl,0.5,a,U,1500)>=0.8]
    if not ok: print("delta=%.2f infaisable"%dl); continue
    a=min(ok); s=surv(theta,dl,0.5,a,U,3000)
    print("theta=%.2f delta=%.2f alpha=%g P(surv)=%.3f aptitude esperee=%.2f"%(theta,dl,a,s,s*np.log(1/a)))

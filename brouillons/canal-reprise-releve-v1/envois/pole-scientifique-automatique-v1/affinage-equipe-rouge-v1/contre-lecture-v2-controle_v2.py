# Calcul illustratif, non préenregistré, non opposable. Modèle gaussien, statistique par grappe ~ N(theta,1),
# processus de rapport de vraisemblance : E_surv (nul theta<=kappa*delta, alternative delta),
# E_ref (nul theta>=delta, alternative kappa*delta). Dans ce modèle log E_ref = -log E_surv.
import numpy as np
rng=np.random.default_rng(np.random.SeedSequence(20261028))
def course(theta,delta,kappa=0.5,a_s=0.01,a_r=0.01,U=400,R=20000,jusquau_budget=False):
    x=rng.normal(theta,1,(R,U)); d=delta*(1-kappa); m=delta*(1+kappa)/2
    ls=np.cumsum(d*(x-m),axis=1); lr=-ls
    cs=ls>=np.log(1/a_s); cr=lr>=np.log(1/a_r)
    fs=np.where(cs.any(1),cs.argmax(1),U+1); fr=np.where(cr.any(1),cr.argmax(1),U+1)
    if jusquau_budget:
        amp=(fs<=U)&(fr<=U); surv=(fs<=U)&~amp; ref=(fr<=U)&~amp
    else:
        amp=(fs==fr)&(fs<=U); surv=(fs<fr)&(fs<=U); ref=(fr<fs)&(fr<=U)
    return surv.mean(),ref.mean(),amp.mean()
def puissance_simulee(delta,kappa,a,U=400,R=4000):
    x=rng.normal(delta,1,(R,U)); d=delta*(1-kappa); m=delta*(1+kappa)/2
    return ((np.cumsum(d*(x-m),axis=1)>=np.log(1/a)).any(1)).mean()
import sys
if 0: print("1) delta=0.3, kappa=0.5, arret au premier franchissement : surv, ref, amplitude_refutee")
for t in [0,0.15,0.225,0.3,0.45]:
    print("  theta=%.3f"%t, ["%.3f"%v for v in course(t,0.3)])
print("2) meme chose, lecture jusqu'au budget")
for t in [0.15,0.225,0.3]:
    print("  theta=%.3f"%t, ["%.3f"%v for v in course(t,0.3,jusquau_budget=True)])
print("3) kappa=0 (permis par kappa dans [0,1)) : theta=delta/4, delta/2")
for t in [0.075,0.15]:
    print("  theta=%.3f"%t, ["%.3f"%v for v in course(t,0.3,kappa=0.0)])
print("4) gonflement de delta, effet vrai 0.3, kappa=0.5 : alpha le plus severe faisable (pi_min=0.8) et aptitude esperee")
grille=[0.2,0.1,0.05,1e-2,1e-3,1e-4,1e-5,1e-6]
for dl in [0.15,0.2,0.25,0.3,0.36,0.45]:
    ok=[a for a in grille if puissance_simulee(dl,0.5,a)>=0.8]
    if not ok: print('  delta=%.2f infaisable'%dl); continue
    a=min(ok)
    s,_,_=course(0.3,dl,a_s=a,R=8000)
    print("  delta=%.2f alpha=%g P(surv)=%.3f aptitude esperee=%.2f"%(dl,a,s,s*np.log(1/a)))
print("5) retour au vivier : unites non lues d'un espace, moyenne de leurs issues vs population (effet 0.3)")
R=20000;U=400;x=rng.normal(0.3,1,(R,U)); ls=np.cumsum(0.15*(x-0.225),axis=1)
f=np.where((np.abs(ls)>=np.log(100)).any(1),(np.abs(ls)>=np.log(100)).argmax(1),U)
non_lues=np.concatenate([x[i,f[i]+1:] for i in range(0,R,20)])
print("  moyenne des non lues=%.4f (population 0.3000), part rendue=%.3f"%(non_lues.mean(),1-(f+1).mean()/U))

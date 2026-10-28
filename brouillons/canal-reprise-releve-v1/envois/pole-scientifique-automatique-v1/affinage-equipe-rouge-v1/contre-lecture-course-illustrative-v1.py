import numpy as np
ss=np.random.SeedSequence(20261028); rng=np.random.default_rng(ss)
def run(theta,delta=0.3,a_s=0.01,a_r=0.01,U=400,R=20000):
    x=rng.normal(theta,1,(R,U))
    ls=np.cumsum(delta*x-delta**2/2,axis=1)   # log E_surv (nul theta<=0, alternative delta)
    lr=-ls                                     # log E_ref (nul theta>=delta) = 1/E_surv dans ce modele
    cs=ls>=np.log(1/a_s); cr=lr>=np.log(1/a_r)
    fs=np.where(cs.any(1),cs.argmax(1),U+1); fr=np.where(cr.any(1),cr.argmax(1),U+1)
    surv=(fs<fr)&(fs<=U); ref=(fr<fs)&(fr<=U)
    return surv.mean(),ref.mean(),1-surv.mean()-ref.mean()
for t in [0,0.075,0.15,0.225,0.3]:
    print(t, ["%.3f"%v for v in run(t)])

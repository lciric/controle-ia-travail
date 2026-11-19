import sys, time, numpy as np
sys.path.insert(0,'/home/user/controle-ia-travail/brouillons/barreau8-lecture-sondes-v1/pieces-contre-lecture-brouillon12-v1')
import sim_forme_a_v1 as S
from controle_ia.t07.plancher_v2 import comparer_difference_au_plancher
rng=np.random.default_rng(np.random.SeedSequence(7))
tache,pas,n,jet,dmax,dmoy=S.donnees(rng,4.0,1.5,"symetrique",False)
s=np.array([j.max() for j in jet]); y=S.etiquettes(rng)
s2=s+2*s.std()*y
for sc in (s,s2):
    t=time.time(); a,b=S.au_dessus(np.vstack([sc[None],dmax]),y,tache,12345); t1=time.time()-t
    t=time.time(); r=comparer_difference_au_plancher(sc,dmax,y,tache,2000,12345,0.95,1-0.05/3); t2=time.time()-t
    print(a,b,r["au_dessus_du_plancher"],r["difference"]["bas"], f"{t1:.1f}s {t2:.1f}s")

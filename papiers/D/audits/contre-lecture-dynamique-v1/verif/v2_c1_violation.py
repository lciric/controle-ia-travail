# Retrouve le tirage de c1 qui signale une "violation" de convexite et la juge par la formule analytique de g''.
import numpy as np
rng=np.random.default_rng(0)
def g(l,pv,ph,a,b,eDR):
    return np.log(pv/ph)+eDR*l+np.log(1-a**l)-np.log(b**l-1)
ls=np.linspace(1e-4,1,20001)
for i in range(2000):
    a=rng.uniform(0,1); b=1+rng.exponential(3); eDR=rng.exponential(3)
    gg=g(ls,0.1,0.5,a,b,eDR); d2=np.diff(gg,2)
    al=-np.log(a); be=np.log(b)
    if (al>be and (d2<-1e-9).any()) or (al<be and (d2>1e-9).any()):
        j=np.argmax(np.abs(d2)*((d2<0) if al>be else (d2>0)))
        lam=ls[j+1]
        h=lambda l: l*l*np.exp(l*lam)/np.expm1(l*lam)**2
        print("tirage",i,"lv=",al,"lh=",be,"lambda=",lam,"d2 numerique=",d2[j],"g'' analytique=",h(be)-h(al), "g''*pas^2=",(h(be)-h(al))*(ls[1]-ls[0])**2)

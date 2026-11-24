"""(1) flot vanille de la regle (c) : limites avec et sans moniteur, convergence ; (2) exemple de trois equilibres sous l'operateur A quand beta_f/beta_v > e^4."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
def softmax(t): z=t-t.max(); e=np.exp(z); return e/e.sum()
def a_vec(pi,beta,R):
    Z=pi@beta; b=(pi*beta)@R/Z; return beta*(R-b)/Z
p=np.array([.6,.3,.1]); R=np.array([0,1.,1.])
for beta in [np.array([1.,.2,.5]), np.ones(3)]:
    for T in [1e3,1e4,1e5]:
        s=solve_ivp(lambda t,th: softmax(th)*a_vec(softmax(th),beta,R),[0,T],np.log(p),rtol=1e-11,atol=1e-13,method='LSODA')
        pi=softmax(s.y[:,-1]); print("vanille beta=%s T=%g : pi=%s  part furtive parmi tricheurs=%.4f"%(beta,T,np.array2string(pi,precision=5),pi[2]/(pi[1]+pi[2])))
print("naturel sans moniteur : part furtive = p_f/(p_f+p_v) =",p[2]/(p[1]+p[2]))
def sig(x): return 0.5*(1+np.tanh(np.asarray(x)/2))
def logit(q): return np.log(q)-np.log1p(-q)
bh,bv,bf,dR=1.,1e-3,.5,1.; lv=np.log(bf/bv)
for eta,q0,s0,kap in [(5.,.05,.05,.2),(8.,.05,.05,.3),(6.5,.02,.1,.25),(10.,.01,.05,.5),(7.,.05,.02,.2),(6.,.1,.1,.3)]:
    u0,w0=logit(q0),logit(s0); A0=dR-np.log(bh/bv)/eta; D=lv/eta
    Phi=lambda w: w0+eta*(D*sig(u0+eta*(A0+D*sig(w)))-kap)
    ws=np.linspace(w0-eta*kap-1,w0+lv+1,400001); h=Phi(ws)-ws
    idx=np.where(np.sign(h[1:])!=np.sign(h[:-1]))[0]
    fp=[brentq(lambda w:Phi(w)-w,ws[i],ws[i+1]) for i in idx]
    print("A, beta_f/beta_v=%g (ell_v=%.2f), eta=%g q0=%g s0=%g kappa=%g : %d equilibres %s"%(bf/bv,lv,eta,q0,s0,kap,len(fp),[(round(float(sig(u0+eta*(A0+D*sig(w)))),4),round(float(sig(w)),4)) for w in fp]))

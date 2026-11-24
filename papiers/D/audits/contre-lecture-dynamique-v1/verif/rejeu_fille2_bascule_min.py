import numpy as np
from scipy.integrate import solve_ivp
def sig(x): return 0.5*(1+np.tanh(x/2))
def end(q0,s0,bv,bf,bh,dR,C,kap,eta):
    A0=bv*dR-(bh-bv)*C; D=(bf-bv)*(dR+C); u0=np.log(q0/(1-q0)); w0=np.log(s0/(1-s0))
    f=lambda t,x:[A0+D*sig(x[1])-(x[0]-u0)/eta, D*sig(x[0])-kap-(x[1]-w0)/eta]
    s=solve_ivp(f,[0,60*eta],[u0,w0],rtol=1e-9,atol=1e-11,method='LSODA')
    return sig(s.y[0,-1]),sig(s.y[1,-1])
for C in (0.40,0.45,0.50,0.60):
    print(C, np.round(end(0.8,0.8,0.04,0.85,1.0,1.0,C,1.2,40.0),6))

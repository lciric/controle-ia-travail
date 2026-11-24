import numpy as np, itertools, sys
def Ufrom(XS,XJ):
    P=len(XS); d=XS-XJ; S=d.sum(0); c=[]
    for p in range(P):
        for q in range(P):
            if p==q: continue
            w=(S-d[p]-d[q])/(P-2); c.append(w@(XS[p]-XJ[q]))
    return np.mean(np.array(c)>0)
def world(rng,P,D,tau,sI=1.0,eta=1.0,sym=False):
    e=np.zeros(D); e[0]=1
    iso=rng.normal(size=(P,D))*3/np.sqrt(D); iso[:,0]=0
    I=iso+np.outer(rng.normal(size=P)*sI,e)
    et=rng.normal(size=(P,D))*eta/np.sqrt(D)
    nJ=rng.normal(size=(P,D))*0.05/np.sqrt(50); nS=rng.normal(size=(P,D))*0.05/np.sqrt(50)
    if sym: XS=I+tau*e+et/2+nS; XJ=I-et/2+nJ
    else: XS=I+tau*e+et+nS; XJ=I+nJ
    return XS,XJ
def label(XS,XJ,alpha=0.05):
    P=len(XS); u0=Ufrom(XS,XJ); vals=[]
    for s in itertools.product([0,1],repeat=P):
        s=np.array(s,bool); A=np.where(s[:,None],XJ,XS); B=np.where(s[:,None],XS,XJ); vals.append(Ufrom(A,B))
    vals=np.array(vals); ph=np.mean(vals>=u0-1e-12); pb=np.mean(vals<=u0+1e-12); p=min(1,2*min(ph,pb))
    if p<=alpha:
        if u0>=0.9: return 'fort',u0
        if u0>0.5: return 'faible',u0
        if u0<0.5: return 'contraire',u0
    return 'ne',u0
rng=np.random.default_rng(1); P=int(sys.argv[1]); D=256; R=int(sys.argv[2])
for name,tau,sym in [('identite',0,False),('identite_sym',0,True),('faible',0.5*np.sqrt(2),False),('forte',4*np.sqrt(2),False)]:
    out=[label(*world(rng,P,D,tau,sym=sym)) for _ in range(R)]
    labs=[o[0] for o in out]; us=[o[1] for o in out]
    print(P,name,{k:labs.count(k)/R for k in set(labs)},'meanU',round(np.mean(us),3))

# Audit R4 du lecteur : simulation indépendante (code du lecteur, graines du lecteur, hors de la course)
import json, math, sys
import numpy as np
D=json.load(open(sys.argv[1]))['resultat']; P={p['point']['i']:p for p in D['points']}
DR=1.0
def plan(K,gam,eta,C,c,m):
    a=1.0 if eta=='inf' else 1-gam/float(eta); W=DR+C; tau=1e-9*max(1,c)
    G=lambda k: gam*sum(a**i for i in range(k))
    kap=next(k for k in range(K) if DR*G(k+1)-(c-m)>tau)
    rho=np.zeros(K); rho[kap]=(DR*G(kap+1)-(c-m))/(gam*W)
    rho[kap+1:]=(DR-(0 if eta=='inf' else (c-m)/float(eta)))/W
    return a,rho,tau
def sim(p,lam,R,seed):
    pt=p['point']; K,n,gam,eta,C,c,d,eps=pt['K'],pt['n'],pt['gam'],pt['eta'],pt['C'],pt['c'],pt['delta'],pt['eps']
    m=lam*eps; a,rho,tau=plan(K,gam,eta,C,c,m); W=DR+C
    Bm=n*rho.sum(); Pc=math.floor(Bm+math.sqrt(2*Bm*math.log(2/d))+2/3*math.log(2/d))
    g=np.random.Generator(np.random.PCG64(np.random.SeedSequence(seed)))
    x=np.zeros(R); xc=np.zeros(R); Nc=np.zeros(R,dtype=np.int64); mx=np.full(R,-np.inf); mxc=mx.copy()
    for k in range(K):
        A=g.binomial(n,rho[k],size=R)
        Ac=np.minimum(A,Pc-Nc); Nc+=Ac
        x=a*x+gam*DR-gam*W*A/n; xc=a*xc+gam*DR-gam*W*Ac/n
        mx=np.maximum(mx,x); mxc=np.maximum(mxc,xc)
    return int((mx-c>tau).sum()), int((mxc-c>tau).sum())
vc=sorted(((p['marges']['1.0']['Vc'],i) for i,p in P.items()),reverse=True)
print('points à Vc(1) le plus élevé :',vc[:6], ' nb points Vc>0 :',sum(1 for v,_ in vc if v>0))
cibles=[vc[0][1],vc[1][1],16,0]
R=100000
for j,i in enumerate(cibles):
    p=P[i]
    for lam in ['0.5','1.0']:
        V,Vc=sim(p,float(lam),R,[99112024,i,j,int(float(lam)*100)])
        M=p['marges'][lam]
        def z(o,e): q=(o+e)/(2*R); return (o-e)/math.sqrt(max(2*R*q*(1-q),1e-9))
        print('point',i,{k:p['point'][k] for k in ['K','n','gam','eta','C','delta']},'lambda',lam,
              'course V/Vc',M['V'],M['Vc'],' lecteur V/Vc',V,Vc,' z(diff) V %.2f Vc %.2f'%(z(M['V'],V),z(M['Vc'],Vc)))

# Audit R4 du lecteur : probabilités exactes de violation (sans plafond et plafonnée) pour les points
# à mémoire entière (eta = infini, a = 1), par programmation dynamique sur le compte cumulé d'audits.
# Écrit par le lecteur à partir du seul préenregistrement ; n'emploie pas le code de l'auteur.
import json, math, sys
import numpy as np
from scipy.stats import binom, beta
D=json.load(open(sys.argv[1]))['resultat']; P=D['points']
DR=1.0
def plan(K,gam,C,c,m):
    W=DR+C; tau=1e-9*max(1,c)
    kap=next(k for k in range(K) if DR*gam*(k+1)-(c-m)>tau)
    rho=np.zeros(K); rho[kap]=(DR*gam*(kap+1)-(c-m))/(gam*W); rho[kap+1:]=DR/W
    return rho,kap,tau
def exact(K,n,gam,C,c,m,cap=None):
    rho,kap,tau=plan(K,gam,C,c,m); W=DR+C
    # état : masse sur N = off + indice
    off=0; mass=np.array([1.0]); killed=0.0
    for k in range(K):
        r=rho[k]
        if r>0:
            lo=int(binom.ppf(1e-25,n,r)) if r<1 else n; hi=int(binom.isf(1e-25,n,r))
            pmf=binom.pmf(np.arange(lo,hi+1),n,r)
            mass=np.convolve(mass,pmf); off+=lo
        Ns=off+np.arange(len(mass))
        if cap is not None:
            over=Ns>cap
            if over.any():
                tot=mass[over].sum(); mass=mass[~over]; Ns=Ns[~over]
                # rabattre sur cap
                if len(Ns)==0 or Ns[-1]!=cap:
                    mass=np.append(mass,0.0); Ns=np.append(Ns,cap)
                mass[-1]+=tot
        x=gam*DR*(k+1)-gam*W*Ns/n
        viol=(x-c)>tau
        killed+=mass[viol].sum(); mass=np.where(viol,0.0,mass)
        nz=np.flatnonzero(mass>1e-300)
        if len(nz)==0: break
        mass=mass[nz[0]:nz[-1]+1]; off=int(Ns[nz[0]])
    return killed, rho
def B_rand(Bm,d): return Bm+math.sqrt(2*Bm*math.log(2/d))+2/3*math.log(2/d)
rows=[]
for p in P:
    pt=p['point']
    if pt['eta']!='inf': continue
    K,n,gam,C,c,d,eps=pt['K'],pt['n'],pt['gam'],pt['C'],pt['c'],pt['delta'],pt['eps']
    if n*K>60000 and n==1000 and K>50: continue
    W=DR+C; Lam=math.log(2*K/d)
    eps_moi=gam*W*(math.sqrt(2*(DR/W)*K*Lam/n)+2*Lam/(3*n))
    res={'i':pt['i'],'K':K,'n':n,'gam':gam,'C':C,'d':d,'eps_rel_ecart':abs(eps_moi-eps)/eps,'c_ecart':abs(c-0.5*gam*K)}
    for l in ['0.25','0.5','0.75','1.0']:
        m=float(l)*eps; V,rho=exact(K,n,gam,C,c,m); M=p['marges'][l]
        assert abs(M['m']-m)<1e-9*max(1,m)
        res['V'+l]=(M['V'],V*1e5, (M['V']-1e5*V)/math.sqrt(max(1e5*V*(1-V),1e-12)))
    # plafonnée à lambda=1
    m=eps; rho,_,_=plan(K,gam,C,c,m); Bm=n*rho.sum(); Pcap=math.floor(B_rand(Bm,d))
    assert abs(Bm-p['marges']['1.0']['B_m'])<1e-6*Bm
    Vc,_=exact(K,n,gam,C,c,m,cap=Pcap); M=p['marges']['1.0']
    res['Vc1']=(M['Vc'],Vc*1e5,(M['Vc']-1e5*Vc)/math.sqrt(max(1e5*Vc*(1-Vc),1e-12)))
    res['V1_exact']=res['V1.0'][1]/1e5
    rows.append(res)
mz=0
for r in rows:
    print(r['i'],'K',r['K'],'n',r['n'],'g',r['gam'],'C',r['C'],'d',r['d'],'eps_err %.1e'%r['eps_rel_ecart'],
      ' '.join('%s obs %d att %.1f z %.2f'%(k,*r[k]) for k in ['V0.5','V0.75','Vc1']), ' V1 exact %.3e'%r['V1_exact'])
    mz=max(mz,*(abs(r[k][2]) for k in ['V0.25','V0.5','V0.75','Vc1']))
print('points:',len(rows),' |z| max sur V(0.25,0.5,0.75) et Vc(1):',mz)
print('V exact à lambda=1 : max',max(r['V1_exact'] for r in rows),' somme des comptes attendus',sum(r['V1_exact'] for r in rows)*1e5)

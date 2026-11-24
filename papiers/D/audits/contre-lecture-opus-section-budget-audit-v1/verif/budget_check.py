import json, math, statistics as st, sys
d=json.load(open(sys.argv[1]))['resultat']; pts=d['points']
print(pts[0]['point'])
def G(k,gam,eta):
    a=1-gam/eta if math.isfinite(eta) else 1.0
    return gam*k if a==1 else eta*(1-a**k)
def Bunif(K,n,gam,eta,dR,C,c):
    a=1-gam/eta if math.isfinite(eta) else 1.0
    W=dR+C
    if dR*G(K,gam,eta)<=c: return 0.0
    tau=1e-9*max(1,c)
    kap=min(k for k in range(K) if dR*G(k+1,gam,eta)-c>tau)
    rk=(dR*G(kap+1,gam,eta)-c)/(gam*W)
    rh=(dR-(c/eta if math.isfinite(eta) else 0))/W
    return n*(rk+(K-1-kap)*rh)
over=[];sv=[];svr=[];infl_ok=[];c_ok=[];eps_ok=[]; overrand=[]
for p in pts:
    q=p['point']; K,n,gam,C,delta=q['K'],q['n'],q['gam'],q['C'],q['delta']
    eta=float(q['eta']); dR=1.0; W=dR+C
    a=1-gam/eta if math.isfinite(eta) else 1.0
    c=0.5*dR*G(K,gam,eta); c_ok.append(abs(c-q['c'])/c)
    Gam=K if a==1 else (1-a**(2*K))/(1-a**2)
    Lam=math.log(2*K/delta); rb=dR/W
    eps=gam*W*(math.sqrt(2*rb*Gam*Lam/n)+2*Lam/(3*n)); eps_ok.append(abs(eps-q['eps'])/eps)
    Bs=Bunif(K,n,gam,eta,dR,C,c); Be=Bunif(K,n,gam,eta,dR,C,c-eps)
    assert abs(Be-p['marges']['1.0']['B_m'])<1e-6*Be, (Be,p['marges']['1.0']['B_m'])
    over.append((Be-Bs)/Bs)
    infl=n*eps/W*((K-1)/eta+1/gam) if math.isfinite(eta) else n*eps/(W*gam)
    infl_ok.append(Be<=Bs+infl+1e-9)
    b=p['bissection']
    if b and b.get('valide'):
        Bm=Bunif(K,n,gam,eta,dR,C,c-b['eps_emp'])
        s=(Be-Bm)/Bs; sv.append(s)
        assert abs(s-b['budget_epargne_sur_Bstar'])<1e-6,(s,b['budget_epargne_sur_Bstar'])
        L2=math.log(2/delta)
        br=lambda B: B+math.sqrt(2*B*L2)+2*L2/3
        svr.append((br(Be)-br(Bm))/Bs)
        overrand.append((br(Be)-Bs)/Bs)
print("c rel err max",max(c_ok),"eps rel err max",max(eps_ok))
print("overhead (B_eps-B*)/B*: min %.3f med %.3f max %.3f"%(min(over),st.median(over),max(over)))
print("overhead (B_rand-B*)/B*: min %.3f med %.3f max %.3f"%(min(overrand),st.median(overrand),max(overrand)))
print("inflation bound holds everywhere:", all(infl_ok))
print("saving recomputed: min %.4f med %.4f max %.4f"%(min(sv),st.median(sv),max(sv)))
print("saving on B_rand: min %.4f med %.4f max %.4f"%(min(svr),st.median(svr),max(svr)))
# fraction of overhead saved
fr=[s/o for s,o in zip(sv,[ov for p,ov in zip(pts,over) if p['bissection'] and p['bissection'].get('valide')])]
print("saving / overhead: min %.3f med %.3f max %.3f"%(min(fr),st.median(fr),max(fr)))
# per-eta breakdown and extreme points
from collections import defaultdict
byeta=defaultdict(list); byeta_s=defaultdict(list)
for p,ov in zip(pts,over):
    q=p['point']; byeta[q['eta']].append(ov)
    b=p['bissection']
    if b and b.get('valide'): byeta_s[q['eta']].append((b['budget_epargne_sur_Bstar'],1/b['rapport']))
for e in byeta:
    s=[x for x,_ in byeta_s[e]]; f=[y for _,y in byeta_s[e]]
    print("eta",e,"overhead med %.3f max %.3f | saving med %.3f max %.3f | factor med %.2f range %.2f-%.2f"%(st.median(byeta[e]),max(byeta[e]),st.median(s),max(s),st.median(f),min(f),max(f)))
i=max(range(len(pts)),key=lambda j:(pts[j]['bissection'] or {}).get('budget_epargne_sur_Bstar',-1))
print("max saving point", pts[i]['point'], "overhead", over[i])

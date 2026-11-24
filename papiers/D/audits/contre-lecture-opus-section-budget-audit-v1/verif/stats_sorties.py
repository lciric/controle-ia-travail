import json, statistics as st, sys
d=json.load(open(sys.argv[1]))['resultat']
pts=d['points']
print("n points", len(pts), "course_invalide", d['course_invalide'], "defauts", d['defauts_instrument'])
p0=pts[0]; print("keys", list(p0.keys()))
print("marge 1.0 keys", list(p0['marges']['1.0'].keys()))
V1=[p['marges']['1.0']['V'] for p in pts]; Vc1=[p['marges']['1.0']['Vc'] for p in pts]
print("V at lam=1: total", sum(V1), "max", max(V1))
print("Vc at lam=1: total", sum(Vc1), "max", max(Vc1), "npts>0", sum(1 for v in Vc1 if v>0))
V0=[p['marges']['0.0']['V']/p['marges']['0.0']['R'] for p in pts]
print("V0 min", min(V0), "median", st.median(V0))
cls=[p['classes_finales'] for p in pts]
from collections import Counter
for k in ['V0','V1','Vc1','D1']: print(k, Counter(c[k] for c in cls))
rap=[]; save=[]; ids=[]
for i,p in enumerate(pts):
    b=p.get('bissection') or {}
    if b and b.get('valide'):
        rap.append(b['rapport']); save.append(b['budget_epargne_sur_Bstar']); ids.append(i)
print("bisections valides", len(rap))
print("rapport eps_emp/eps min %.4f max %.4f median %.4f"%(min(rap),max(rap),st.median(rap)))
fac=[1/r for r in rap]
print("factor eps/eps_emp min %.4f max %.4f median %.4f"%(min(fac),max(fac),st.median(fac)))
print("saving min %.4f max %.4f median %.4f"%(min(save),max(save),st.median(save)))
# point id of min/max saving and its params
def params(p): return {k:p.get(k) for k in ['K','n','gam','eta','C','delta','c','eps','i'] if k in p}
print("pt keys sample", [k for k in p0.keys() if not isinstance(p0[k],(dict,list))])
imax=ids[save.index(max(save))]; imin=ids[save.index(min(save))]
print("max saving point", imax, params(pts[imax]), "rapport", pts[imax]['bissection']['rapport'])
print("min saving point", imin, params(pts[imin]), "rapport", pts[imin]['bissection']['rapport'])
# B_eps / Bstar excess
ex=[]
for p in pts:
    m1=p['marges']['1.0']
    ex.append(m1)
print("marge1 keys", list(ex[0].keys()))
# the non-bisected point
print("no valid bisection:", [i for i,p in enumerate(pts) if not (p.get('bissection') or {}).get('valide')])

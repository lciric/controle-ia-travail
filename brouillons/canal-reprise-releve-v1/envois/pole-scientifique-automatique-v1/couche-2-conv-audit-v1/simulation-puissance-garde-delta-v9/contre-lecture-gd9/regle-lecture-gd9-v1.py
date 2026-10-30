import json,sys
D=sys.argv[1]
T=json.load(open(D+'/tableaux-v9-sortie.json'))
P=json.load(open(D+'/precision-rho-pilote-v9-sortie.json'))
tv=T['table_rho_vrai']
print([k for k in T.keys()])
G=sorted({c['rho'] for c in P['cellules'] if c['p']==0.4})
print('grille sd',G, 'Ns',sorted({c['N'] for c in P['cellules']}))
def sd(rh,N):
    r=next((g for g in G if g>=max(rh,0)-1e-12),G[-1])
    return [c for c in P['cellules'] if c['p']==0.4 and c['rho']==r and c['N']==N][0]['ecart_type'],r
def lig(h,haut):
    ls=sorted([l for l in tv if l['hypothese']==h and not l.get('absent') and l['n_h_40'] is not None and l['n_h_160'] is not None],key=lambda l:l['rho_B'])
    return next((l for l in ls if l['rho_B']>=haut-1e-12),None)
def lire(rh,N):
    s,_=sd(rh,N); haut=max(rh,0)+1.645*s
    a,b=lig('ρ_A = ρ_B',haut),lig('ρ_A = 2 ρ_B',haut)
    if a is None or b is None: return None,haut
    return (max(a['n_h_40'],b['n_h_40']),max(a['n_h_160'],b['n_h_160'])),haut
N=288
prev=None;chg=[]
import numpy as np
for i in range(-50,4101):
    rh=i/1000
    r,h=lire(rh,N)
    if r!=prev: chg.append((rh,r,round(h,4)));prev=r
for c in chg: print(c)
# monotonicity
vals=[lire(i/1000,N)[0] for i in range(0,401)]
last=(0,0);bad=0
for v in vals:
    if v is None: continue
    if v[0]<last[0] or v[1]<last[1]: bad+=1
    last=v
print('non-monotone',bad)
# points
for rh in (0,0.05,0.10,0.17,0.171,0.175,0.18):
    print(rh,lire(rh,N))
print('--- bornes reelles')
for N in (50,100,288):
    last=None
    for i in range(0,4001):
        rh=i/10000
        r,h=lire(rh,N)
        if r is None: print(N,'premier hors table (reel)',rh,round(h,4)); break
    # hyp1 seule
    def lire1(rh,N):
        s,_=sd(rh,N); haut=max(rh,0)+1.645*s; a=lig('ρ_A = ρ_B',haut); return a
    for i in range(0,4001):
        rh=i/10000
        if lire1(rh,N) is None: print(N,'hyp1 seule premier hors',rh); break
# sensibilite de sigma a 0.17 N=288
s,_=sd(0.17,288); print('sigma',s,'haut',0.17+1.645*s,'marge sigma pour basculer',(0.2-0.17)/1.645-s)

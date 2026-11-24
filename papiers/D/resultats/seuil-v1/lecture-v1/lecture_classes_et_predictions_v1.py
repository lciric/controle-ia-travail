import json, math, statistics, collections, sys
from scipy.stats import beta, binom
D=json.load(open(sys.argv[1]))['resultat']
P=D['points']; L=['0.0','0.1','0.25','0.5','0.75','1.0']
NIV=1e-4
def hi(k,R): return 1.0 if k==R else beta.ppf(1-NIV,k+1,R-k)
def lo(k,R): return 0.0 if k==0 else beta.ppf(NIV,k,R-k+1)
def classer(k,R,s):
    if hi(k,R)<=s: return 'sous'
    if lo(k,R)>s: return 'au-dessus'
    return 'indetermine'
out=collections.defaultdict(list); ecarts=[]
for p in P:
    pt=p['point']; i=pt['i']; d=pt['delta']; R=100000; M=p['marges']
    c={'V0':classer(M['0.0']['V'],R,d/2),'V1':classer(M['1.0']['V'],R,d/2),'Vc1':classer(M['1.0']['Vc'],R,d),'D1':classer(M['1.0']['D'],R,d)}
    if c!=p['classes_premier_tirage']: ecarts.append((i,c,p['classes_premier_tirage']))
    for l in L:
        if classer(M[l]['V'],R,d/2)!=M[l]['classe_V_premier']: ecarts.append((i,l,'classe V'))
    # invariants agrégés
    for l in L:
        m=M[l]
        if not (m['V']<=m['Vc']<=m['V']+m['O']): out['invariant_agrege_manque'].append((i,l))
        sens = abs(m['V']-m['V_tau2'])>10 or abs(m['Vc']-m['Vc_tau2'])>10
        if sens: out['sensibilite'].append((i,l,m['V'],m['V_tau2']))
    if p['prolongations']: out['prolong'].append(i)
    if p['audit_renforce']: out['audit'].append(i)
    out['V1'].append(M['1.0']['V']); out['Vc1'].append(M['1.0']['Vc']); out['D1'].append(M['1.0']['D'])
    out['V0frac'].append((M['0.0']['V']/R,i))
    out['distance'].append(M['1.0']['distance_seuil']['quantile_sur_eps'])
    # O contre O_exact
    for l in L:
        m=M[l]; pe=m['O_exact']; z=(m['O']-R*pe)/math.sqrt(max(R*pe*(1-pe),1e-12))
        out['zO'].append(z)
    # controle 2 recalculé
    for l in ['0.0','1.0']:
        Vr=M[l]['V']/R; f2=p['controle2'][l]['frequence']
        tol=5*math.sqrt(Vr*(1-Vr)*(1e-3+1e-5))+0.003
        out['c2marge'].append(abs(f2-Vr)/tol)
        out['c2proches'].append(p['controle2'][l]['repetitions_proches_du_seuil'])
print('écarts de classes (relecture indépendante vs script):',ecarts)
print('invariant agrégé manqué:',out['invariant_agrege_manque'])
print('sensibilité >10:',out['sensibilite'])
print('prolongations:',out['prolong'],' audits renforcés:',out['audit'])
print('lambda=1 : somme V',sum(out['V1']),' max V',max(out['V1']),' somme Vc',sum(out['Vc1']),' max Vc',max(out['Vc1']),' somme D',sum(out['D1']),' max D', max(out['D1']))
print('borne haute 1e-4 pour 0/1e5:',hi(0,100000),' delta/20 min:',0.05/20)
v0=sorted(out['V0frac']); print('lambda=0 : min V/R',v0[:3],' médiane',statistics.median([x for x,_ in v0]))
print('borne haute 1e-4 du min V0:',hi(int(v0[0][0]*1e5),100000))
print('distance au seuil /eps : min',min(out['distance']),' max',max(out['distance']),' médiane',statistics.median(out['distance']))
zs=out['zO']; print('O contre O_exact : z max abs',max(map(abs,zs)),' moyenne z',statistics.mean(zs),' n',len(zs), ' |z|>3:',sum(abs(z)>3 for z in zs))
print('controle 2 : marge max (écart/tolérance)',max(out['c2marge']),' répétitions proches du seuil, total',sum(out['c2proches']))
# P3
p3=collections.Counter()
for p in P:
    d=p['point']['delta']; M=p['marges']; i=p['point']['i']
    s01=any(abs(M['0.1'][k]-M['0.1'][k+'_tau2'])>10 for k in ['V','Vc'])
    c01=M['0.1']['classe_V_premier']; c075=M['0.75']['classe_V_premier']
    p3['0.1:'+('sensible ' if s01 else '')+c01]+=1; p3['0.75:'+c075]+=1
    for mo in p['monotonie']:
        if mo['hausse_significative']: p3['hausse']+=1
    # monotonie recalculée sur les comptes : hausse non significative peut-elle exister ?
    for a,b in zip(L,L[1:]):
        if M[b]['V']>M[a]['V']: p3['hausse_brute_'+a+'_'+b]+=1
print('P3:',dict(p3))
# P4
rs=[];inv=[];byeta=collections.defaultdict(list);nonv=[]
for p in P:
    b=p['bissection']; i=p['point']['i']
    if not b: nonv.append((i,'pas de bissection')); continue
    if not b['valide']: nonv.append((i,'invalide',b['confirmation']['classe'],b['lambda_moins'],b['lambda_plus'],b['rapport'])); continue
    rs.append(b['rapport']); byeta[p['point']['eta']].append(b['rapport'])
    # recheck validity
    eps=p['point']['eps']; d=p['point']['delta']
    assert classer(b['confirmation']['V'],100000,d/2)==b['confirmation']['classe']
print('P4 : ensemble de lecture',len(rs),'/138 ; exclus',nonv)
print('  min',min(rs),' max',max(rs),' médiane',statistics.median(rs),' hors [0.2,0.7]:',[r for r in rs if not 0.2<=r<=0.7])
for e,v in byeta.items(): print('  eta',e,' n',len(v),' médiane',statistics.median(v), ' min',min(v),' max',max(v))
conf=collections.Counter(p['bissection']['confirmation']['classe'] for p in P if p['bissection']); print('  confirmations',conf)
be=[p['bissection']['budget_epargne_sur_Bstar'] for p in P if p['bissection'] and p['bissection']['valide']]
print('  budget épargné / B*: min',min(be),' médiane',statistics.median(be),' max',max(be))
# boucle fermée
bf=[(p['boucle_fermee']['0.0']['V'],p['boucle_fermee']['1.0']['V']) for p in P]
print('boucle fermée : V à 0 min',min(x for x,_ in bf),' V à 1 max',max(y for _,y in bf))
# O descriptif
Os=[p['marges']['1.0']['O']/1e5 for p in P]; print('O à lambda=1: min',min(Os),' max',max(Os))
# point 16
for p in P:
    if p['point']['i']==16:
        print('POINT16',p['point']); print(' classes',p['classes_finales'], p['classes_premier_tirage'])
        for l in L: print(' ',l,{k:p['marges'][l][k] for k in ['V','Vc','D','O','classe_V_premier']})
        b=p['bissection']; print(' bissection rapport',b['rapport'],'valide',b['valide'],'conf',b['confirmation'],'lm',b['lambda_moins'],'lp',b['lambda_plus'])
        print(' distance', p['marges']['1.0']['distance_seuil'])

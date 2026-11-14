import json, numpy as np
D='/home/user/controle-ia-travail/docs/notes/regard-ou-raisons-confondants-v1/croisement-v1/'
corr=json.load(open(D+'correspondance-sources-v1.json'))['fiches']
runs={'A':'sortie-juge-modele-A-v1','B':'sortie-juge-modele-B-v1','A-inv':'sortie-juge-modele-A-ordre-inverse-v1','B-inv':'sortie-juge-modele-B-ordre-inverse-v1'}
N={k:{n['id']:n for n in json.load(open(D+'notes-brutes-v1/'+v+'.json'))['notes']} for k,v in runs.items()}
def sc(n,pid):
    if pid.startswith('P'): return (2*n['C1']+2*n['C2']+n['C3']+n['C4']+n['C5'])/35*10
    return (2*n['F1']+n['F2']+n['F3'])/20*10
def rk(v):
    v=np.array(v); o=v.argsort(); r=np.empty(len(v)); r[o]=np.arange(len(v))
    for x in set(v): r[v==x]=r[v==x].mean()
    return r
res={"note":"Analyse de sensibilité non prévue par la méthode scellée : seconde passe des deux juges, fiches présentées en ordre inverse. Ne change pas le classement principal. La passe B en ordre inverse a omis P36 (aucune seconde relance : passe de sensibilité seulement) ; P36 y est moyennée sur trois passes et exclue des corrélations de cette passe.","spearman":{},"top10":{},"temoins":{}}
for g,pref in [('RX','P'),('F','F')]:
    ids=[p for p in corr if p.startswith(pref)]
    S={k:{p:sc(N[k][p],p) for p in ids if p in N[k]} for k in runs}
    for a,b in [('A','A-inv'),('B','B-inv'),('A','B'),('A-inv','B-inv')]:
        com=[p for p in ids if p in S[a] and p in S[b]]
        res['spearman'][f'{g}:{a}~{b}']=round(float(np.corrcoef(rk([S[a][p] for p in com]),rk([S[b][p] for p in com]))[0,1]),3)
    m4={p:float(np.mean([S[k][p] for k in runs if p in S[k]])) for p in ids}
    m2={p:float(np.mean([S['A'][p],S['B'][p]])) for p in ids}
    o4=sorted(ids,key=lambda p:-m4[p]); o2=sorted(ids,key=lambda p:-m2[p])
    res['top10'][g]={'principal_A_B':[(p,corr[p]['cle'],round(m2[p],2)) for p in o2[:10]],
                     'quatre_passes':[(p,corr[p]['cle'],round(m4[p],2)) for p in o4[:10]]}
    for p in ids:
        if corr[p]['temoin']:
            res['temoins'][corr[p]['cle']]={k:f"{sorted(S[k].values(),reverse=True).index(S[k][p])+1}/{len(S[k])}" for k in runs}
            res['temoins'][corr[p]['cle']]['quatre_passes']=f"{o4.index(p)+1}/{len(ids)}"
json.dump(res,open(D+'sensibilite-ordre-inverse-v1.json','w'),ensure_ascii=False,indent=1)
print(json.dumps(res,ensure_ascii=False,indent=0))

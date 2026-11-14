import json, sys
import numpy as np
D='/home/user/controle-ia-travail/docs/notes/regard-ou-raisons-confondants-v1/croisement-v1/'
corr=json.load(open(D+'correspondance-sources-v1.json'))['fiches']
anon={a['id']:a for a in json.load(open(D+'fiches-anonymes-v1.json'))}
juges=sys.argv[1:]  # e.g. A B
notes={j:{n['id']:n for n in json.load(open(D+f'notes-brutes-v1/sortie-juge-modele-{j}-v1.json'))['notes']} for j in juges}
def sc(n,pid):
    if pid.startswith('P'): return (2*n['C1']+2*n['C2']+n['C3']+n['C4']+n['C5'])/35*10
    return (2*n['F1']+n['F2']+n['F3'])/20*10
rows=[]
for pid in anon:
    s={j:round(sc(notes[j][pid],pid),2) for j in juges}
    c=corr[pid]
    nsrc=0 if c['temoin'] else len(set(c['sources']))
    rows.append(dict(id=pid,cle=c['cle'],genre=c['genre'],nom=anon[pid]['nom'],temoin=c['temoin'],sources=c['sources'],accord=nsrc,
        notes=s,moyenne=round(float(np.mean(list(s.values()))),2),ecart=round(max(s.values())-min(s.values()),2),
        C2={j:notes[j][pid].get('C2') for j in juges}, C5={j:notes[j][pid].get('C5') for j in juges},
        motifs={j:notes[j][pid]['motif'] for j in juges}))
def rk(v):  # ranks, average ties
    v=np.array(v); o=v.argsort(); r=np.empty(len(v)); r[o]=np.arange(len(v)); 
    for x in set(v): r[v==x]=r[v==x].mean()
    return r
out={"juges":juges,"formule":"R/X: (2*C1+2*C2+C3+C4+C5)/35*10 ; F: (2*F1+F2+F3)/20*10","fiches":rows,"spearman":{},"temoins":{}}
for g,pref in [('RX','P'),('F','F')]:
    sub=[r for r in rows if r['id'].startswith(pref)]
    if len(juges)>=2:
        for a in range(len(juges)):
            for b in range(a+1,len(juges)):
                ra=rk([r['notes'][juges[a]] for r in sub]); rb=rk([r['notes'][juges[b]] for r in sub])
                out['spearman'][f'{g}:{juges[a]}-{juges[b]}']=round(float(np.corrcoef(ra,rb)[0,1]),3)
    # temoins
    for key in ['moyenne']+juges:
        vals=sorted(sub,key=lambda r:-(r['moyenne'] if key=='moyenne' else r['notes'][key]))
        for i,r in enumerate(vals):
            if r['temoin']:
                out['temoins'].setdefault(r['cle'],{})[key]=f"{i+1}/{len(vals)}"
json.dump(out,open(D+'agregation-v1.json','w'),ensure_ascii=False,indent=1)
for g,pref in [('RX','P'),('F','F')]:
    sub=sorted([r for r in rows if r['id'].startswith(pref)],key=lambda r:(-r['moyenne'],-r['accord']))
    print('=====',g)
    for i,r in enumerate(sub):
        print(f"{i+1:2d} {r['id']} {r['moyenne']:5.2f} {r['notes']} ec={r['ecart']:.1f} acc={r['accord']} {'TEMOIN ' if r['temoin'] else ''}{r['cle']} C5={r['C5']}")
print(out['spearman']); print(json.dumps(out['temoins'],ensure_ascii=False))

# Départage par l'accord (méthode §8) : tri par note moyenne, puis échanges entre voisins dont l'écart < 0,3 quand le second a strictement plus d'accord ; répété jusqu'à stabilité.
def departage(sub):
    s=sorted(sub,key=lambda r:-r['moyenne']); ch=True
    while ch:
        ch=False
        for i in range(len(s)-1):
            a,b=s[i],s[i+1]
            if a['moyenne']-b['moyenne']<0.3 and b['accord']>a['accord']:
                s[i],s[i+1]=b,a; ch=True
    return s
out['ordre_final']={}
for g,pref in [('RX','P'),('F','F')]:
    s=departage([r for r in rows if r['id'].startswith(pref)])
    out['ordre_final'][g]=[r['id'] for r in s]
    print('ORDRE',g,[(r['id'],r['cle'],r['moyenne'],r['accord']) for r in s[:12]])
json.dump(out,open(D+'agregation-v1.json','w'),ensure_ascii=False,indent=1)

import json, os, shutil, sys
T='/home/user/billets-codage-v1/tenue'
def lire(p): return [json.loads(l) for l in open(p,encoding='utf-8') if l.strip()]
g1=[l for l in lire(f'{T}/passe-1/codeur-1/depot-gestes-C1.jsonl') if l.get('geste') and l['geste']!='AVEUGLE']
g2=[l for l in lire(f'{T}/passe-1/codeur-2/depot-gestes-C2.jsonl') if l.get('geste') and l['geste']!='AVEUGLE']
o1=lire(f'{T}/passe-1/codeur-1/depot-objections-C1.jsonl'); o2=lire(f'{T}/passe-1/codeur-2/depot-objections-C2.jsonl')
G1={(l['billet'],l['geste']):l['modalite'] for l in g1}; G2={(l['billet'],l['geste']):l['modalite'] for l in g2}
O1={(l['billet'],l['commentaire']):l['classe'] for l in o1}; O2={(l['billet'],l['commentaire']):l['classe'] for l in o2}
assert G1.keys()==G2.keys() and O1.keys()==O2.keys()
dg=sorted(k for k in G1 if G1[k]!=G2[k]); do=sorted(k for k in O1 if O1[k]!=O2[k])
lot2=[l.strip() for l in open(f'{T}/passe-1/codeur-2/lot-2/ordre.txt') if l.strip()]
print('désaccords gestes',len(dg),'sur',len(G1),'; objections',len(do),'sur',len(O1))
billets=sorted({b for b,_ in dg}|{b for b,_ in do})
grp={'opus':[b for b in billets if b not in lot2],'haiku':[b for b in billets if b in lot2]}
A=f'{T}/arbitrage'; assert not os.path.exists(A)
for m,bs in grp.items():
    for i in range(0,len(bs),12):
        d=f'{A}/{m}/lot-{i//12+1}'; os.makedirs(f'{d}/billets'); os.makedirs(f'{d}/commentaires')
        lg=[]; lo=[]
        for b in bs[i:i+12]:
            shutil.copyfile(f'{T}/passe-1/codeur-1/billets/{b}.md',f'{d}/billets/{b}.md')
            for k in dg:
                if k[0]==b: lg.append({'billet':b,'geste':k[1],'valeur_a':G1[k],'valeur_b':G2[k]})
            if any(k[0]==b for k in do):
                shutil.copyfile(f'{T}/passe-2/commentaires/{b}.json',f'{d}/commentaires/{b}.json')
                for k in do:
                    if k[0]==b: lo.append({'billet':b,'commentaire':k[1],'valeur_a':O1[k],'valeur_b':O2[k]})
        with open(f'{d}/desaccords-gestes.jsonl','w',encoding='utf-8') as f:
            for x in lg: f.write(json.dumps(x,ensure_ascii=False)+'\n')
        with open(f'{d}/desaccords-objections.jsonl','w',encoding='utf-8') as f:
            for x in lo: f.write(json.dumps(x,ensure_ascii=False)+'\n')
        print(m,d.split('/')[-1],len(bs[i:i+12]),'billets',len(lg),'gestes',len(lo),'objections')

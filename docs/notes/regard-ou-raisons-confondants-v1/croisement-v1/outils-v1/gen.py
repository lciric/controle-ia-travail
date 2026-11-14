import json, sys, numpy as np
sys.path.insert(0,'.')
from fiches_src import R, X, F, T, TF
D='/home/user/controle-ia-travail/docs/notes/regard-ou-raisons-confondants-v1/croisement-v1/'
ss=np.random.SeedSequence(20261114); rng=np.random.default_rng(ss)
rx=R+X+T; f=F+TF
o1=rng.permutation(len(rx)); o2=rng.permutation(len(f))
anon=[];corr={"graine":"numpy.random.SeedSequence(20261114), permutation R/X puis F","sources":{"S1":"session mère, bilan-mere-v1.md","S2":"organisme d'idéation, 36 fiches validées (g1)","S3":"collisionneur à cinq espèces, run-e3-v1, étage III","S4":"consultation à part n° 1","S5":"consultation à part n° 2"},"fiches":{}}
for i,k in enumerate(o1):
    p=rx[k]; pid=f"P{i+1:02d}"
    anon.append({"id":pid,"genre":"explication rivale" if p['genre']=="R" else "expérience","famille":p['famille'],"nom":p['nom'],"mecanisme":p['mecanisme'],"prediction":p['prediction'],"test":p['test'],"controles":p['controles'],"cout":p['cout']})
    corr["fiches"][pid]={"cle":p['cle'],"genre":p['genre'],"sources":p['sources'],"passages":p['passages'],"note":p.get('note',''),"temoin":p['sources']==["TEMOIN"]}
for i,k in enumerate(o2):
    p=f[k]; pid=f"F{i+1:02d}"
    anon.append({"id":pid,"genre":"conseil de forme","nom":p['nom'],"conseil":p['conseil']})
    corr["fiches"][pid]={"cle":p['cle'],"genre":"F","sources":p['sources'],"passages":p['passages'],"temoin":p['sources']==["TEMOIN"]}
json.dump(anon,open(D+'fiches-anonymes-v1.json','w'),ensure_ascii=False,indent=1)
json.dump(corr,open(D+'correspondance-sources-v1.json','w'),ensure_ascii=False,indent=1)
L=["# Fiches anonymes — croisement « Regard ou raisons » v1","","Source retirée, style normalisé, ordre tiré au hasard (graine dans la correspondance, non montrée aux juges).",""]
for a in anon:
    L.append(f"## {a['id']} — {a['nom']} ({a['genre']}{', famille '+a['famille'] if 'famille' in a else ''})")
    if 'conseil' in a: L.append(a['conseil'])
    else:
        for c,lab in [('mecanisme','Mécanisme ou description'),('prediction','Prédiction'),('test','Test le moins cher'),('controles','Contrôles'),('cout','Coût')]:
            L.append(f"- **{lab}.** {a[c]}")
    L.append("")
open(D+'fiches-anonymes-v1.md','w').write("\n".join(L))
print(len(rx),len(f))

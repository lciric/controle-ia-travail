import json, os
S=os.environ['S']
src='docs/decisions/decision-N-074-v1-brouillon2.md'
L=open(src,encoding='utf-8').read().split('\n')
def between(k,a,b):
    l=L[k-1]; s=l.index(a); e=l.index(b, s); return l[s:e]
P=[{"ligne":3,"ancien":"ligne R-3359 du registre des décisions ; "},
   {"ligne":4,"ancien":between(4,"brouillon 1 (`docs/","Ce brouillon propose")},
   {"ligne":53,"ancien":", `docs/notes/reconception-accumulation-cycle-2-v1/pieces-redaction-cycle-2-v1/sortie-calculs-redaction-cycle-2-v2.txt`"},
   {"ligne":7,"ancien":" Elle ne dépend d'aucune issue du second cycle de l'accumulation."},
   {"ligne":75,"ancien":" sur un écart probablement plus petit"}]
for p in P:
    assert L[p['ligne']-1].count(p['ancien'])==1, p
    print(p['ligne'], repr(p['ancien'][:90]), '…', repr(p['ancien'][-40:]))
spec={"source":src,"ref":"origin/main","empreinte_attendue":"29b38fc41ac45855",
 "sortie":"docs/notes/g1-extraits-tiers-v1/extrait-N-074-brouillon2-v2.md",
 "titre":"brouillon 2 de N-074 (contraste à témoin apparié)",
 "objet":"demande 6 du rédacteur successeur.",
 "plages":[[1,4],[7,7],[16,56],[58,66],[68,77],[88,105],[107,109]],
 "passages_en_clair":P, "annexe_sources":True,
 "annexe_termes":["au moins 300","300","600","200","5 %","1 %","95 %","Clopper-Pearson","Kullback-Leibler","intersection-union","pari apparié borné","0,99","0,95","0,85","0,73","37","48 heures"]}
json.dump(spec,open(S+'/specs/spec-N-074-brouillon2-v2.json','w'),ensure_ascii=False,indent=2)

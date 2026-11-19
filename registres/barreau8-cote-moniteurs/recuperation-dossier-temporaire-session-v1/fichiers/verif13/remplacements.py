import sys; sys.path.insert(0,'src')
from controle_ia import prereg
V='/tmp/claude-0/-home-user-controle-ia-travail/ccd98af0-e97a-5c3c-8902-30e463468b85/scratchpad/verif13/'
t=open('brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon13.md',encoding='utf-8').read()
R=[("est retiré de la règle d'échec ; tout le reste de l'essai",
    "est retiré de la règle d'échec ; en (i), « l'essai n'échoue que par l'égalité des deux chemins non tenue, (a) ou (b) » devient « l'essai n'échoue que par (a) ou (b) » ; tout le reste de l'essai"),
   ("n'ouvre les fichiers 1, 2 et 4 de la livraison ni n'en lit un score, avant comme après leur envoi.",
    "n'ouvre les fichiers 1, 2 et 4 de la livraison ni n'en lit un score, avant comme après leur envoi ; les copier, les déposer, les transmettre et en calculer l'empreinte, sans en décoder le contenu, n'est pas les ouvrir au sens de cette phrase (comme une pièce dont seules l'existence et l'empreinte sont contrôlées n'est pas ouverte : plan, point 3).")]
for o,n in R:
    print('count',t.count(o)); t=t.replace(o,n)
# the quoted (i) phrase must still appear exactly once outside (b-5) quotation
q="l'essai n'échoue que par l'égalité des deux chemins non tenue, (a) ou (b)"
print('phrase (i) occurrences', t.count(q), [i+1 for i,l in enumerate(t.split('\n')) if q in l])
p=V+'b13_corrige.md'; open(p,'w',encoding='utf-8').write(t)
print(prereg.problemes(p)); L=t.split('\n'); print(len(L),[i+1 for i,l in enumerate(L) if 'À REMPLIR' in l])
# simulate retour (a) partially: apply the (b-5) phrase to see the (i) sentence becomes coherent
t2=t.replace(q+'.', "l'essai n'échoue que par (a) ou (b).",1) if False else None

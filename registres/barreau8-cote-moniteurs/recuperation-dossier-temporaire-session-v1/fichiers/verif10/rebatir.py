import sys, difflib
D='/home/user/controle-ia-travail/brouillons/barreau8-lecture-sondes-v1/'
b9=open(D+'prereg-lecture-sondes-barreau8-v1-brouillon9.md',encoding='utf-8').read()
b10=open(D+'prereg-lecture-sondes-barreau8-v1-brouillon10.md',encoding='utf-8').read()
R=[
("tout autre fichier du dépôt ou d'un dossier d'entrée, et tout chemin dont un composant porte « iib », « ii-b », « consigne-privee » ou « extrait_cote_moniteurs », est refusé avant ouverture",
 "hors de cette liste, tout autre fichier du dépôt ou d'un dossier d'entrée, et tout chemin dont un composant porte « iib », « ii-b », « consigne-privee » ou « extrait_cote_moniteurs », est refusé avant ouverture ; un chemin de la liste fermée n'est jamais refusé par ce motif (les noms des fichiers de la course et du registre propre portent « iib »)"),
("(moins de 0,01 Go ; la garde P9 leur réserve 4 000 000 octets)",
 "(moins de 0,01 Go : compte au point « Taille des fichiers ajoutés par ces formes » ; la garde P9 réserve 4 000 000 octets à la trace, au bordereau et à leurs compagnons)"),
("de nom `a` suivi du rang de l'action sur cinq chiffres (par exemple `a00016`)",
 "de nom `a` suivi, sur cinq chiffres, de la valeur du champ `rang` de l'index (ordre du fichier des identifiants, non le rang dans le tri du sous-échantillon ; par exemple `a00016`)"),
("la lecture exige les cinq premières","la lecture exige les cinq autres clés"),
]
# also check the report contains each string verbatim
rep=open(D+'contre-lecture-brouillon9-v1.md',encoding='utf-8').read()
x=b9
for i,(a,b) in enumerate(R,1):
    print('R-%d'%i,'ancien dans b9:',b9.count(a),'ancien dans rapport:',rep.count(a),'nouveau dans rapport:',rep.count(b),'nouveau dans b10:',b10.count(b))
    x=x.replace(a,b)
open('rebati.md','w',encoding='utf-8').write(x)

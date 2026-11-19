import sys, subprocess
sys.path.insert(0, "/home/user/controle-ia-travail/src")
from controle_ia.prereg import problemes
S="/home/user/controle-ia-travail/brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon9.md"
t=open(S,encoding="utf-8").read()
R=[("tout autre fichier du dépôt ou d'un dossier d'entrée, et tout chemin dont un composant porte « iib », « ii-b », « consigne-privee » ou « extrait_cote_moniteurs », est refusé avant ouverture",
 "hors de cette liste, tout autre fichier du dépôt ou d'un dossier d'entrée, et tout chemin dont un composant porte « iib », « ii-b », « consigne-privee » ou « extrait_cote_moniteurs », est refusé avant ouverture ; un chemin de la liste fermée n'est jamais refusé par ce motif (les noms des fichiers de la course et du registre propre portent « iib »)"),
("(moins de 0,01 Go ; la garde P9 leur réserve 4 000 000 octets)",
 "(moins de 0,01 Go : compte au point « Taille des fichiers ajoutés par ces formes » ; la garde P9 réserve 4 000 000 octets à la trace, au bordereau et à leurs compagnons)"),
("de nom `a` suivi du rang de l'action sur cinq chiffres (par exemple `a00016`)",
 "de nom `a` suivi, sur cinq chiffres, de la valeur du champ `rang` de l'index (ordre du fichier des identifiants, non le rang dans le tri du sous-échantillon ; par exemple `a00016`)"),
("la lecture exige les cinq premières", "la lecture exige les cinq autres clés")]
for a,b in R:
    assert t.count(a)==1, a[:30]; t=t.replace(a,b)
open("b9-corrige.md","w",encoding="utf-8").write(t)
print(problemes("b9-corrige.md"))
r=subprocess.run(["diff",S,"b9-corrige.md"],capture_output=True,text=True)
print([l for l in r.stdout.splitlines() if l[:1].isdigit()])
for s in ["À REMPLIR — À FIXER : tirée par la session mère au scellement","- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :"]:
    print(t.count(s))

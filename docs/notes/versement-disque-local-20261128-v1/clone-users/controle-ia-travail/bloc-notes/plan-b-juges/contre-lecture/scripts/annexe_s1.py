import hashlib, sys
brouillon = open(sys.argv[1], encoding="utf-8").read().split("\n")
# annexe A : lignes après "    ## Scoring Rubric" jusqu'à la ligne "Copie de travail"
debut = brouillon.index("    ## Scoring Rubric")
fin = next(i for i in range(debut, len(brouillon)) if brouillon[i].startswith("Copie de travail du texte"))
bloc = brouillon[debut:fin]
# retirer les lignes vides de fin
while bloc and bloc[-1] == "":
    bloc.pop()
lignes = []
for l in bloc:
    if l == "":
        lignes.append("")
    elif l.startswith("    "):
        lignes.append(l[4:])
    else:
        print("ligne non indentée :", repr(l[:40])); lignes.append(l)
texte = "\n".join(lignes) + "\n"
travail = open(sys.argv[2], encoding="utf-8").read()
print("annexe == copie de travail :", texte == travail)
print("caractères sans fin de ligne finale :", len(travail.rstrip("\n")), "| octets fichier :", len(travail.encode()))
print("sha256 copie :", hashlib.sha256(travail.encode()).hexdigest())
print("caractères non ASCII :", sorted({c for c in travail if ord(c) > 127}))
print("espaces de fin de ligne :", sum(1 for l in travail.split("\n") if l != l.rstrip()))

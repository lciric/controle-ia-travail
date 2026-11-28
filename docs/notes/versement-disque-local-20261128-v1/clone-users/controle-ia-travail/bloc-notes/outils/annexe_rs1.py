import sys, hashlib
brouillon, source = sys.argv[1], sys.argv[2]
texte = open(source, encoding="utf-8").read()
assert texte.endswith("\n") and not texte.endswith("\n\n")
lignes = texte[:-1].split("\n")
bloc = "\n".join(("    " + l) if l.strip() else "" for l in lignes)
doc = open(brouillon, encoding="utf-8").read()
assert doc.count("\nANNEXE_RS1\n") == 1
doc2 = doc.replace("\nANNEXE_RS1\n", "\n" + bloc + "\n", 1)
open(brouillon, "w", encoding="utf-8").write(doc2)
# verification : extraire le bloc entre l'en-tete de l'annexe A et la ligne « Copie de travail »
d = doc2.split("\n")
debut = next(i for i, l in enumerate(d) if l.startswith("## Annexe A"))
fin = next(i for i, l in enumerate(d) if l.startswith("Copie de travail du texte"))
zone = d[debut + 1:fin]
# premier et dernier indices de lignes indentees
idx = [i for i, l in enumerate(zone) if l.startswith("    ")]
extrait = zone[idx[0]:idx[-1] + 1]
assert all(l == "" or l.startswith("    ") for l in extrait)
rendu = "\n".join(l[4:] if l else "" for l in extrait) + "\n"
print("egal:", rendu == texte, "lignes:", len(lignes), "caracteres sans fin:", len(texte) - 1)
print("sha source:", hashlib.sha256(texte.encode()).hexdigest())
print("sha rendu :", hashlib.sha256(rendu.encode()).hexdigest())

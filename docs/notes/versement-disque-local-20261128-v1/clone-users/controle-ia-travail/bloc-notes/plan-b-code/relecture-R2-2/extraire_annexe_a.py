"""Extrait l'annexe A du brouillon 3 (retrait de quatre espaces), compare octet pour octet à RS1.txt."""
import hashlib, sys
from pathlib import Path
prereg, rs1, travail = map(Path, sys.argv[1:4])
lignes = prereg.read_text(encoding="utf-8").split("\n")
debut = next(i for i, l in enumerate(lignes) if l.startswith("## Annexe A"))
fin = next(i for i, l in enumerate(lignes) if l.startswith("## Annexe B"))
bloc = lignes[debut + 1:fin]
# premier et dernier non vides indentés
idx = [i for i, l in enumerate(bloc) if l.startswith("    ")]
corps = bloc[idx[0]:idx[-1] + 1]
sortie = []
for l in corps:
    if l == "":
        sortie.append("")
    elif l.startswith("    "):
        sortie.append(l[4:])
    else:
        print("ligne non vide sans retrait :", repr(l)); sortie.append(l)
texte = "\n".join(sortie) + "\n"
b = rs1.read_bytes()
print("annexe A extraite : caractères", len(texte), "sans fin finale", len(texte) - 1, "sha256", hashlib.sha256(texte.encode()).hexdigest())
print("RS1.txt           : octets", len(b), "sha256", hashlib.sha256(b).hexdigest())
print("travail S1        : sha256", hashlib.sha256(travail.read_bytes()).hexdigest() if travail.exists() else "absent")
print("égal octet pour octet :", texte.encode("utf-8") == b)
print("égal à travail :", travail.exists() and travail.read_bytes() == b)
# lignes avec espaces de fin, tabulations, non-ASCII
for i, l in enumerate(b.decode().split("\n")):
    if l != l.rstrip() : print("espace de fin l.", i + 1, repr(l[-10:]))
    if "\t" in l: print("tabulation l.", i + 1)
print("ascii :", b.isascii(), "CR :", b"\r" in b, "BOM :", b.startswith(b"\xef\xbb\xbf"))

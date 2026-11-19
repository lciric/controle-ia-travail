import re, sys, hashlib
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/src")
from controle_ia import prereg
B = Path("/home/user/controle-ia-travail/brouillons/barreau8-lecture-sondes-v1")
b10 = (B/"prereg-lecture-sondes-barreau8-v1-brouillon10.md").read_bytes()
b11 = (B/"prereg-lecture-sondes-barreau8-v1-brouillon11.md").read_bytes()
print("sha b11", hashlib.sha256(b11).hexdigest())
print("problemes b11:", prereg.problemes(B/"prereg-lecture-sondes-barreau8-v1-brouillon11.md"))
L10 = b10.decode().split("\n"); L11 = b11.decode().split("\n")
print("lignes b11 (split):", len(L11), "fin par newline:", b11.endswith(b"\n"))
print("marqueurs:", [i+1 for i,l in enumerate(L11) if "À REMPLIR" in l], "compte", b11.decode().count("À REMPLIR"))
print("ligne 76 identique octet pour octet:", L10[75].encode()==L11[75].encode(), repr(L11[75]))
t = b11.decode()
for s in ["À REMPLIR — À FIXER : tirée par la session mère au scellement",
          "- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :",
          "versée avec l'empreinte du texte scellé."]:
    print("compte", t.count(s), "lignes", [i+1 for i,l in enumerate(L11) if s in l], repr(s[:50]))
# bloc Noms et champs
def bloc(L):
    i = next(k for k,l in enumerate(L) if l.startswith("**Noms et champs, liste fermée**"))
    j = next(k for k in range(i, len(L)) if L[k].startswith("**Fichiers non lus avant**"))
    return "\n".join(L[i:j])
print("bloc Noms et champs identique:", bloc(L10)==bloc(L11), len(bloc(L11)))
cl = prereg.sections(t)["Contre-lecture"]
print("entrees:", [m.group(1) for m in prereg.ENTREE.finditer(cl)])
sex = [l for l in L11 if l.startswith("- **Contre-lecture 3 sexies**")][0]
print("sexies empreintes:", prereg.EMPREINTE.findall(sex))
for p in ["prereg-lecture-sondes-barreau8-v1-brouillon10.md","contre-lecture-brouillon10-v1.md"]:
    print(p, hashlib.sha256((B/p).read_bytes()).hexdigest())
# conclusion du rapport 10
print("conclusion rapport10 contient PRÊT:", "PRÊT : le brouillon 10" in (B/"contre-lecture-brouillon10-v1.md").read_text())
# compagnon b11
c = B/"prereg-lecture-sondes-barreau8-v1-brouillon11.md.sha256"
print("compagnon b11:", c.read_text().strip() if c.exists() else "absent")

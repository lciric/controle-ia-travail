"""Applique au brouillon 3 de la réplication les corrections CL3-01 à CL3-05 de la contre-lecture 3 et ses deux marqueurs,
lus dans le rapport lui-même (empreintes vérifiées), et écrit le texte à sceller sous prereg/ (refus d'écraser).
Usage : python appliquer-contre-lecture-3-replication-v1.py "AAAA-MM-JJ à HH:MM"   (relevé de date -u)"""
import hashlib, re, sys
from pathlib import Path
D = Path("brouillons/preuves-mentors-v1/convergence-replication-v1")
B3, RAP = D / "preenregistrement-replication-convergence-v1-brouillon3.md", D / "contre-lecture-3-preenregistrement-replication-v1.md"
DST = Path("prereg/preregistrement-replication-regles-defense-convergence-v1.md")
H_B3, H_RAP = "73d2252ff2beec8e77eb1d6b33ab58c6b77c986b64cffdda23c7ce704f1ffbe1", "97076b18866bd466e5ed39ec5da3e3465257b97f5f421e0c32e120f3685276cc"
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
assert h(B3) == H_B3 and h(RAP) == H_RAP, "empreintes"
date = sys.argv[1]; assert re.fullmatch(r"\d{4}-\d{2}-\d{2} à \d{2}:\d{2}", date)
t, r = B3.read_text(encoding="utf-8"), RAP.read_text(encoding="utf-8")
corr = r[r.index("## 3. Corrections"):r.index("## 4. Les deux marqueurs")]
paires = re.findall(r"Remplacer\n\n```text\n(.*?)\n```\n\npar\n\n```text\n(.*?)\n```", corr, re.S)
para = re.search(r"Paragraphe à ajouter après la ligne 414[^\n]*\n\n```text\n(.*?)\n```", corr, re.S).group(1)
journal = []
for a, b in paires:
    assert t.count(a) == 1, ("occurrence", a[:60], t.count(a)); t = t.replace(a, b); journal.append("remplacé : " + a[:70])
L = t.split("\n")
i = [k for k, x in enumerate(L) if x.startswith("Les lignes « Lecture d'un résultat de la réplication avant scellement »")]
assert len(i) == 1; L.insert(i[0] + 1, ""); L.insert(i[0] + 2, para); journal.append(f"paragraphe CL3-01 inséré après la ligne {i[0]+1}")
t = "\n".join(L)
m4 = r[r.index("## 4. Les deux marqueurs"):]
blocs = re.findall(r"```text\n(.*?)\n```", m4, re.S)
a1, b1, entree = blocs[0], blocs[1], blocs[2]
assert t.count(a1) == 1; t = t.replace(a1, b1.replace("AAAA-MM-JJ à HH:MM", date)); journal.append("date : " + date)
assert entree.count("<<EMPREINTE_RAPPORT_CL3>>") == 1; entree = entree.replace("<<EMPREINTE_RAPPORT_CL3>>", H_RAP)
L = t.split("\n"); j = [k for k, x in enumerate(L) if x.startswith("**Contre-lecture 3** — À REMPLIR")]
assert len(j) == 1; L[j[0]] = entree; t = "\n".join(L); journal.append("entrée de la contre-lecture 3 remplie")
assert "À REMPLIR" not in t and "<<" not in t
with open(DST, "x", encoding="utf-8") as f: f.write(t)
print("\n".join(journal)); print(f"{len(paires)} remplacements, écrit {DST}")

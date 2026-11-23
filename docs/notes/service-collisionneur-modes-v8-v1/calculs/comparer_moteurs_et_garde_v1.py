"""Compare v8d et v8m (tours, consignes, préambule, motifs, catalogue) et passe la garde de motifs des deux moteurs sur la
question v8 servie depuis son titre ; occurrences par ligne du fichier d'origine. Sans réseau.
Usage : PYTHONPATH=SRC python3 comparer_moteurs_et_garde_v1.py V8D.py V8M.py QUESTION_V8.md"""
import importlib.util, sys
from collections import Counter
def charge(nom, p):
    spec = importlib.util.spec_from_file_location(nom, p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
d, m = charge("v8d", sys.argv[1]), charge("v8m", sys.argv[2])
print("TOURS identiques :", d.TOURS == m.TOURS)
print("CONSIGNES identiques :", d.CONSIGNES == m.CONSIGNES)
print("PREAMBULE_GABARIT identique :", d.PREAMBULE_GABARIT == m.PREAMBULE_GABARIT)
print("MOTIFS_INTERDITS identiques :", [(a, b.pattern) for a, b in d.MOTIFS_INTERDITS] == [(a, b.pattern) for a, b in m.MOTIFS_INTERDITS])
for e in ("fable", "opus", "argon", "astra", "carbon", "neon"):
    print("catalogue", e, "identique :", d.CATALOGUE[e] == m.CATALOGUE[e])
texte = d.lire_entree(sys.argv[3]); lignes = texte.split("\n"); servi = "\n".join(lignes[2:])
print("caractères servis depuis le titre :", len(servi), "; mots (découpage Python) :", len(servi.split()))
print("garde v8d :", d.motifs_trouves(servi)); print("garde v8m :", m.motifs_trouves(servi))
c = Counter()
for i, l in enumerate(lignes, 1):
    if i < 3: continue
    for nom, motif in d.MOTIFS_INTERDITS:
        k = len(motif.findall(l))
        if k: c[nom] += k; print(f"  ligne {i} : {nom} × {k}")
print("total :", dict(c))

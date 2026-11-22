"""Geste du scellement du texte du bras A (case « entropie », 13.1) — un seul tirage de l'entier racine.
Usage : geste_scellement_v1.py SOURCE(brouillon 55) SORTIE NOTE
Refuse si SORTIE ou NOTE existe déjà (aucun second tirage, R12), si SOURCE n'a pas l'empreinte attendue,
ou si la différence obtenue dépasse : l'entier inscrit, la marque retirée, le titre et la ligne de statut."""
import datetime, difflib, hashlib, os, sys
import numpy as np
SOURCE, SORTIE, NOTE = sys.argv[1:4]
ATTENDUE = "cc55502ad4ef0fa1de5f8f4444975fec2eb7f3f77db8913c96f1bdf9225facb1"
for p in (SORTIE, NOTE):
    if os.path.exists(p): sys.exit(f"refus : {p} existe déjà ; aucun second tirage")
octets = open(SOURCE, "rb").read()
if hashlib.sha256(octets).hexdigest() != ATTENDUE: sys.exit("refus : empreinte de la source inattendue")
L = octets.decode("utf-8").split("\n")
MARQUE = "**À REMPLIR** pour l'entier racine :"
lignes = [i for i, l in enumerate(L) if MARQUE in l]
if len(lignes) != 1 or L[lignes[0]].count(MARQUE) != 1 or sum(l.count("À REMPLIR") for l in L) != 1:
    sys.exit("refus : la marque de l'entier racine n'est pas unique, ou une autre marque reste")
heure = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
entier = np.random.SeedSequence().entropy          # tirage unique, sans argument (R9)
commande = "numpy.random.SeedSequence().entropy"
i = lignes[0]
L[i] = L[i].replace(MARQUE, f"**remplie pour l'entier racine** : **{entier}** (tiré le {heure}, `{commande}`, numpy {np.__version__}, une seule fois, par la session de relance ; note du scellement `docs/notes/relance-organismes-discrets-v1/scellement-bras-a-v2/note-du-scellement-v1.md`) :")
a, b = "— v2, BROUILLON 55", "— v2"
assert L[0].count(a) == 1; L[0] = L[0].replace(a, b)
a = "**Statut : brouillon 55, non exécutable.** Le brouillon 55 porte"
assert L[2].count(a) == 1
L[2] = L[2].replace(a, f"**Statut : texte scellé, version 2 du préenregistrement du bras A** (entier racine tiré et inscrit le {heure} en 13.1, case « entropie » ; aucune autre différence avec le brouillon 55, `cc55502a…`, que le titre et cette ligne). Le brouillon 55 porte")
neuf = "\n".join(L)
avant, apres = octets.decode("utf-8").split("\n"), neuf.split("\n")
changees = [j for j in range(len(avant)) if avant[j] != apres[j]]
if len(avant) != len(apres) or changees != sorted({0, 2, i}): sys.exit(f"refus : différence hors des trois lignes : {changees}")
open(SORTIE, "w", encoding="utf-8").write(neuf)
h = hashlib.sha256(neuf.encode()).hexdigest()
open(NOTE, "w", encoding="utf-8").write(
f"""# Note du scellement — texte du bras A, version 2

- Heure du tirage (UTC) : {heure}
- Commande : `{commande}` (numpy {np.__version__}), appelée une seule fois, sans argument, par la session de relance (programme `geste_scellement_v1.py` de ce dossier).
- Entier racine : {entier}
- Source : brouillon 55, `{ATTENDUE}`.
- Texte obtenu : `{os.path.basename(SORTIE)}`, `{h}`.
- Différence avec le brouillon 55, vérifiée par programme : lignes {[c+1 for c in changees]} seulement — titre (« BROUILLON 55 » retiré), statut, et la case « entropie » (entier inscrit, marque retirée).
- Chaîne de lecture : contre-lecture 11 (`45d76769…`) et sa vérification (`a96a4d9d…`) ; contre-lectures des cases remplies des brouillons 54 (`c68b20de…`) et 55 (`b0c9960b…`) ; vérification habilitée (R-5032).
- Aucun programme de la course, aucun essai ni aucune simulation n'a tourné avec cet entier.
""")
print(h, entier)

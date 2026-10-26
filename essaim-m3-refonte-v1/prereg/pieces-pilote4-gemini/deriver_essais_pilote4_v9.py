"""Dérive la batterie d'essais v9 du lanceur du pilote 4 de la batterie v8 (`essais_lanceur_pilote4_v8.sh`, a5f4b944…),
par remplacements exacts au nombre attendu, pour le lanceur v7 (objet de la seconde course : la v6.2 à la place de la
v6.1 ; décision de Lazar du 25 octobre 2026, 23:54 Paris, « tout attendre la v6.2 ») :

- clé de course `v6-2` (au lieu de `v6-1`) partout (cas, chemins, lignes de dépense, texte d'essai) ; « v6.2 » dans les
  messages attendus du lanceur ;
- empreinte d'arbre de l'organisme : `d02c2907…` (au lieu de `ae331d1d…`), pleine et courte ;
- le lanceur nommé dans le cas `m-sous-lanceur-pilote4` : `lancer_pilote4_gemini_v7.sh` ;
- en-tête et usage.

Aucun cas n'est ajouté ni retiré.

Usage : python3 -I deriver_essais_pilote4_v9.py ESSAIS_V8 SORTIE
Refuse si l'empreinte de la batterie v8 n'est pas a5f4b944…, si une occurrence n'est pas au nombre attendu, si un reste de
la v6.1 subsiste, ou si SORTIE existe (R12).
"""
import hashlib, pathlib, sys

SHA_V8 = "a5f4b9447f9f2944012fdd54a92cc3926315f592924602694eac47ec19e3ed03"
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V8:
    sys.exit("refus : la batterie source n'est pas la v8 a5f4b944…")
t = b.decode("utf-8")

remplacements = [
    ("v6-1", "v6-2", 54),
    ("v6.1", "v6.2", 11),
    ("ae331d1deb660a20da919edbdcdecba28e49b9b143a6b7a061262101a79798d4",
     "d02c2907c8eaafb5c9c6768d739b415bfe3d9733a4342b8a16ad77eb19fdb252", 1),
    ("ae331d1d", "d02c2907", 8),
    ("lancer_pilote4_gemini_v6.sh", "lancer_pilote4_gemini_v7.sh", 1),
    ("# Usage : bash essais_lanceur_pilote4_v8.sh ", "# Usage : bash essais_lanceur_pilote4_v9.sh ", 1),
    ("# plus), v8 : la v7 (c3263af1…) par `deriver_essais_pilote4_v8.py` (contre-lecture 3, P4C3-03 : gardes du segment\n"
     "# K ≥ 2 et de la porte essayées sur un artefact, minuteur essayé sur une copie mutée du lanceur ; lanceur v6 inchangé) ;\n"
     "# la v7 était dérivée",
     "# plus), v9 : la v8 (a5f4b944…) par `deriver_essais_pilote4_v9.py` pour le lanceur v7 (objet de la seconde course : la\n"
     "# v6.2 à la place de la v6.1 — clé de course, noms, empreinte d'arbre ; décision de Lazar du 25 octobre 2026, 23:54 Paris ;\n"
     "# aucun cas ajouté ni retiré) ; la v8 était dérivée de la v7 (c3263af1…) par `deriver_essais_pilote4_v8.py` (contre-lecture 3,\n"
     "# P4C3-03 : gardes du segment K ≥ 2 et de la porte essayées sur un artefact, minuteur essayé sur une copie mutée du\n"
     "# lanceur ; lanceur v6 inchangé) ; la v7 était dérivée", 1),
]
for ancien, nouveau, n in remplacements:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)
for motif, permis in (("v6-1", 0), ("ae331d1d", 0), ("a9d8eb5", 0), ("v6.1", 1), ("lancer_pilote4_gemini_v6.sh", 0)):
    k = t.count(motif)
    if k != permis:
        sys.exit(f"refus : {motif!r} présent {k} fois après dérivation (attendu {permis})")
sortie.write_text(t, encoding="utf-8")
print(f"batterie écrite : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()} ; {len(remplacements)} remplacements")

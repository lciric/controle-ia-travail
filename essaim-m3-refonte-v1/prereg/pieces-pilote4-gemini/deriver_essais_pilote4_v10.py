"""Dérive la batterie d'essais v10 du lanceur du pilote 4 de la batterie v9 (`essais_lanceur_pilote4_v9.sh`, edb6b12b…),
par remplacements exacts au nombre attendu, pour le lanceur v8 (la v6.2 livrée par Gemini, commit `3bbb78c`, empreinte
d'arbre `3b2d8d5a…`, à la place de son premier commit `fedb065`, `d02c2907…` ; la batterie v9 n'a jamais tourné) :

- empreinte d'arbre de l'organisme de la v6.2 : `3b2d8d5a…` (au lieu de `d02c2907…`), pleine et courte ;
- le lanceur nommé dans le cas `m-sous-lanceur-pilote4` : `lancer_pilote4_gemini_v8.sh` ;
- en-tête et usage.

Aucun cas n'est ajouté ni retiré.

Usage : python3 -I deriver_essais_pilote4_v10.py ESSAIS_V9 SORTIE
Refuse si l'empreinte de la batterie v9 n'est pas edb6b12b…, si une occurrence n'est pas au nombre attendu, si un reste
du premier commit subsiste, ou si SORTIE existe (R12).
"""
import hashlib, pathlib, sys

SHA_V9 = "edb6b12bee4c391d24adda27c9752144917a84c739a05758902dec512ed9744e"
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V9:
    sys.exit("refus : la batterie source n'est pas la v9 edb6b12b…")
t = b.decode("utf-8")

remplacements = [
    ("d02c2907c8eaafb5c9c6768d739b415bfe3d9733a4342b8a16ad77eb19fdb252",
     "3b2d8d5a9af75b5457579c847d4ea9510f9da92818805123ed037f7c8436c946", 1),
    ("d02c2907", "3b2d8d5a", 8),
    ("lancer_pilote4_gemini_v7.sh", "lancer_pilote4_gemini_v8.sh", 1),
    ("# Usage : bash essais_lanceur_pilote4_v9.sh ", "# Usage : bash essais_lanceur_pilote4_v10.sh ", 1),
    ("# plus), v9 : la v8 (a5f4b944…) par `deriver_essais_pilote4_v9.py` pour le lanceur v7 (objet de la seconde course : la\n"
     "# v6.2 à la place de la v6.1 — clé de course, noms, empreinte d'arbre ; décision de Lazar du 25 octobre 2026, 23:54 Paris ;\n"
     "# aucun cas ajouté ni retiré) ; la v8 était dérivée",
     "# plus), v10 : la v9 (edb6b12b…) par `deriver_essais_pilote4_v10.py` pour le lanceur v8 (la v6.2 livrée, commit `3bbb78c`,\n"
     "# empreinte d'arbre `3b2d8d5a…`, à la place du premier commit de Gemini ; aucun cas ajouté ni retiré ; la v9 n'a jamais\n"
     "# tourné) ; la v9 était dérivée de la v8 (a5f4b944…) par `deriver_essais_pilote4_v9.py` pour le lanceur v7 (objet de la\n"
     "# seconde course : la v6.2 à la place de la v6.1 — clé de course, noms, empreinte d'arbre ; décision de Lazar du\n"
     "# 25 octobre 2026, 23:54 Paris ; aucun cas ajouté ni retiré) ; la v8 était dérivée", 1),
]
for ancien, nouveau, n in remplacements:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)
for motif, permis in (("d02c2907", 0), ("fedb065", 0), ("lancer_pilote4_gemini_v7.sh", 0), ("v6-1", 0), ("v6.1", 1),
                      ("3b2d8d5a9af75b5457579c847d4ea9510f9da92818805123ed037f7c8436c946", 1)):
    k = t.count(motif)
    if k != permis:
        sys.exit(f"refus : {motif!r} présent {k} fois après dérivation (attendu {permis})")
sortie.write_text(t, encoding="utf-8")
print(f"batterie écrite : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()} ; {len(remplacements)} remplacements")

"""Dérive le lanceur v8 du quatrième pilote descriptif du lanceur v7 (`lancer_pilote4_gemini_v7.sh`, cda96923…), par
remplacements exacts, chacun au nombre d'occurrences attendu.

Pourquoi : le lanceur v7 épinglait le premier commit de la v6.2 de Gemini (`fedb065`, poussé le 25 octobre 2026 à
21:35 UTC, arbre `d02c2907…`) ; Gemini a poussé un second commit sur la même branche (`3bbb78c`, enfant de `fedb065`,
commité à 22:57:18 UTC ; quatre fichiers de `organisme/` changés), que son rapport de livraison (transmis par Lazar le
25 octobre à 23:09 UTC) désigne comme la v6.2 livrée. Le v8 épingle ce commit et son empreinte d'arbre
(`3b2d8d5a9af75b5457579c847d4ea9510f9da92818805123ed037f7c8436c946`, 24 fichiers, calculée par la fonction du noyau
`boucle.empreinte_arbre` et par sa transcription `empreinte_arbre_v1.py`). Le v7 n'a jamais servi (ni essayé, ni poussé).
Rien d'autre ne change.

Usage : python3 -I deriver_lanceur_pilote4_v8.py LANCEUR_V7 SORTIE
Refuse si l'empreinte du lanceur v7 n'est pas cda96923…, si une occurrence n'est pas au nombre attendu, si un reste du
premier commit subsiste, ou si SORTIE existe (R12).
"""
import hashlib, pathlib, sys

SHA_V7 = "cda96923144180156f0e129dda917e27527406b93b2d9d6c60d955e3beae7e62"
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V7:
    sys.exit("refus : le lanceur source n'est pas la v7 cda96923…")
t = b.decode("utf-8")

remplacements = [
    ("fedb06525610c05945f8496c2058c21a15256fca", "3bbb78c1991baf17feb421529fa1957be7edec59", 1),
    ("d02c2907c8eaafb5c9c6768d739b415bfe3d9733a4342b8a16ad77eb19fdb252",
     "3b2d8d5a9af75b5457579c847d4ea9510f9da92818805123ed037f7c8436c946", 1),
    ("commit `fedb065`, arbre `d02c2907…`, 24 fichiers", "commit `3bbb78c`, arbre `3b2d8d5a…`, 24 fichiers", 1),
    ("— v7 : le lanceur v6\n"
     "# (50f9c496…) par `deriver_lanceur_pilote4_v7.py` (objet de la seconde course : la v6.2 à la place de la v6.1, décision\n"
     "# de Lazar du 25 octobre 2026, 23:54 Paris, « tout attendre la v6.2 » ; écart consigné dans\n"
     "# `diff-lanceur-pilote4-v6-vers-v7.txt`), la v6 dérivée",
     "— v8 : le lanceur v7\n"
     "# (cda96923…) par `deriver_lanceur_pilote4_v8.py` (objet de la seconde course : la v6.2 livrée par Gemini, commit\n"
     "# `3bbb78c`, à la place de son premier commit `fedb065`, que le second, commité le 25 octobre 2026 à 22:57 UTC, remplace ;\n"
     "# le lanceur v7 n'a jamais servi ; écart consigné dans `diff-lanceur-pilote4-v7-vers-v8.txt`), la v7 dérivée du lanceur v6\n"
     "# (50f9c496…) par `deriver_lanceur_pilote4_v7.py` (objet de la seconde course : la v6.2 à la place de la v6.1, décision\n"
     "# de Lazar du 25 octobre 2026, 23:54 Paris, « tout attendre la v6.2 »), la v6 dérivée", 1),
    ("#       bash lancer_pilote4_gemini_v7.sh\n", "#       bash lancer_pilote4_gemini_v8.sh\n", 1),
]
for ancien, nouveau, n in remplacements:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)
for motif, permis in (("fedb06525610c05945f8496c2058c21a15256fca", 0), ("d02c2907", 0), ("fedb065", 1),
                      ("lancer_pilote4_gemini_v7.sh", 0), ("3bbb78c1991baf17feb421529fa1957be7edec59", 1),
                      ("3b2d8d5a9af75b5457579c847d4ea9510f9da92818805123ed037f7c8436c946", 1), ("v6-1", 0), ("v6.1", 1)):
    k = t.count(motif)
    if k != permis:
        sys.exit(f"refus : {motif!r} présent {k} fois après dérivation (attendu {permis})")
sortie.write_text(t, encoding="utf-8")
print(f"lanceur écrit : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()} ; {len(remplacements)} remplacements")

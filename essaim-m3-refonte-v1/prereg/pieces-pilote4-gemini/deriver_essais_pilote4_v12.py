"""Dérive la batterie d'essais v12 du lanceur du pilote 4 de la batterie v11 (`essais_lanceur_pilote4_v11.sh`, ba47a625…),
par remplacements exacts au nombre attendu, pour le lanceur v10 : l'objet de la course `v6-2` est la v6.2.1 (empreinte
d'arbre `4f13647a…`, 26 fichiers, au lieu de `3b2d8d5a…`, 24 fichiers). En plus, le cas `m-lanceur-pilote3` nomme le
lanceur v10 dans la ligne qu'il écrit (la v11 nommait encore le v8 : sans effet sur le cas, qui refuse tout lanceur autre
que celui, scellé, du second pilote). Aucun cas n'est ajouté ni retiré. La v11 n'a jamais tourné.

Usage : python3 -I deriver_essais_pilote4_v12.py ESSAIS_V11 SORTIE
Refuse si l'empreinte de la batterie v11 n'est pas ba47a625…, si une occurrence n'est pas au nombre attendu, ou si SORTIE
existe (R12).
"""
import hashlib, pathlib, sys

SHA_V11 = "ba47a6251892fc6acf4822ce1c8111ede75a2c9ba3a57ca44ba70e26bd4eb23e"
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V11:
    sys.exit("refus : la batterie source n'est pas la v11 ba47a625…")
t = b.decode("utf-8")
remplacements = [
    ("organisme : 24 fichiers, empreinte d'arbre 3b2d8d5a9af75b5457579c847d4ea9510f9da92818805123ed037f7c8436c946",
     "organisme : 26 fichiers, empreinte d'arbre 4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d", 1),
    ("organismes v5.3 `6251ab21…` et v6.2 `3b2d8d5a…`", "organismes v5.3 `6251ab21…` et v6.2 `4f13647a…`", 3),
    ("`8b1c7511…` `6251ab21…` `3b2d8d5a…`", "`8b1c7511…` `6251ab21…` `4f13647a…`", 2),
    ("organismes `6251ab21…` `3b2d8d5a…`", "organismes `6251ab21…` `4f13647a…`", 1),
    ("empreinte d'arbre de l'organisme ≠ 3b2d8d5a…", "empreinte d'arbre de l'organisme ≠ 4f13647a…", 2),
    ("l'empreinte de l'organisme 3b2d8d5a… et celle du texte scellé", "l'empreinte de l'organisme 4f13647a… et celle du texte scellé", 1),
    ("fichiers au lieu de 24", "fichiers au lieu de 26", 1),
    ("lanceur : lancer_pilote4_gemini_v8.sh, sha256 $H/", "lanceur : lancer_pilote4_gemini_v10.sh, sha256 $H/", 1),
    ("# plus), v11 : la v10 (b7906684…) par `deriver_essais_pilote4_v11.py` pour le lanceur v9 (ordre des courses inversé, décision\n",
     "# plus), v12 : la v11 (ba47a625…) par `deriver_essais_pilote4_v12.py` pour le lanceur v10 (objet de la course v6-2 : la\n"
     "# v6.2.1, empreinte d'arbre `4f13647a…`, 26 fichiers — la v6.2 de Gemini corrigée par conv-audit ; aucun cas ajouté ni\n"
     "# retiré ; la v11 n'a jamais tourné) ; la v11 était dérivée de la v10 (b7906684…) par `deriver_essais_pilote4_v11.py`\n"
     "# pour le lanceur v9 (ordre des courses inversé, décision\n", 1),
    ("# Usage : bash essais_lanceur_pilote4_v11.sh ", "# Usage : bash essais_lanceur_pilote4_v12.sh ", 1),
]
for ancien, nouveau, n in remplacements:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)
for motif, permis in (("3b2d8d5a", 1), ("4f13647a", 11), ("24 fichiers", 0), ("au lieu de 24", 0), ("lancer_pilote4_gemini_v8.sh", 0)):
    k = t.count(motif)
    if k != permis:
        sys.exit(f"refus : {motif!r} présent {k} fois après dérivation (attendu {permis})")
sortie.write_text(t, encoding="utf-8")
print(f"batterie écrite : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()}")

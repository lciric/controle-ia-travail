"""Dérive le lanceur v10 du quatrième pilote descriptif du lanceur v9 (`lancer_pilote4_gemini_v9.sh`, 6491c940…), par
remplacements exacts au nombre attendu : objet de la course `v6-2` = la **v6.2.1** (branche
`canal/conv-audit-organisme-v6-2-1`, commit `7ea32705c5437d91ed071dd95fb3209bb0b0035e`, enfant de `3bbb78c` ; dossier
`organisme/`, 26 fichiers, empreinte d'arbre `4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d`) — la
v6.2 de Gemini corrigée par la lignée conv-audit (C-14 à C-17, `organisme/CORRECTIONS-v5.md`) sur le mot de Lazar du
26 octobre 2026, 00:27 Paris (« tu as mon accord pour retoucher la version de gemini »). La clé de course (`v6-2`), le
nom (`pilote4-gemini-v6-2-v1`), la lignée (`gemini-organisme-v6-2`), l'ordre des courses (v6.2 d'abord) et tout le reste
sont ceux du v9.

Usage : python3 -I deriver_lanceur_pilote4_v10.py LANCEUR_V9 SORTIE
Refuse si l'empreinte du lanceur v9 n'est pas 6491c940…, si une occurrence n'est pas au nombre attendu, si un reste de
l'objet ancien subsiste dans le code, ou si SORTIE existe (R12).
"""
import hashlib, pathlib, sys

SHA_V9 = "6491c94034a68c658c5d3f3ade79d41da43376c5de05957b2882343c336db11f"
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V9:
    sys.exit("refus : le lanceur source n'est pas la v9 6491c940…")
t = b.decode("utf-8")
remplacements = [
    ("    COMMIT_ORGANISME=3bbb78c1991baf17feb421529fa1957be7edec59\n", "    COMMIT_ORGANISME=7ea32705c5437d91ed071dd95fb3209bb0b0035e\n", 1),
    ("    ARBRE_ORGANISME=3b2d8d5a9af75b5457579c847d4ea9510f9da92818805123ed037f7c8436c946\n",
     "    ARBRE_ORGANISME=4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d\n", 1),
    ("    N_FICHIERS_ORGANISME=24\n", "    N_FICHIERS_ORGANISME=26\n", 1),
    ("# v6.2 = branche `canal/gemini-organisme-v6-2`, commit `3bbb78c`, arbre `3b2d8d5a…`, 24 fichiers ; lignées « assistées ».",
     "# v6.2 = la v6.2.1 : branche `canal/conv-audit-organisme-v6-2-1`, commit `7ea3270`, arbre `4f13647a…`, 26 fichiers (la v6.2\n"
     "# de Gemini, `3bbb78c`, corrigée par conv-audit : C-14 à C-17, `organisme/CORRECTIONS-v5.md`) ; lignées « assistées ».", 1),
    ("— v9 : le lanceur v8\n# (40685089…) par `deriver_lanceur_pilote4_v9.py` (ordre des courses inversé",
     "— v10 : le lanceur v9\n# (6491c940…) par `deriver_lanceur_pilote4_v10.py` (objet de la course v6-2 : la v6.2.1, commit `7ea3270`, arbre\n"
     "# `4f13647a…`, 26 fichiers — la v6.2 de Gemini corrigée par conv-audit, mot de Lazar du 26 octobre 2026, 00:27 Paris ;\n"
     "# écart consigné dans `diff-lanceur-pilote4-v9-vers-v10.txt`), la v9 dérivée du lanceur v8\n"
     "# (40685089…) par `deriver_lanceur_pilote4_v9.py` (ordre des courses inversé", 1),
    ("#       bash lancer_pilote4_gemini_v9.sh\n", "#       bash lancer_pilote4_gemini_v10.sh\n", 1),
]
for ancien, nouveau, n in remplacements:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)
for motif, permis in (("3bbb78c1991baf17feb421529fa1957be7edec59", 0), ("3b2d8d5a9af75b5457579c847d4ea9510f9da92818805123ed037f7c8436c946", 0),
                      ("7ea32705c5437d91ed071dd95fb3209bb0b0035e", 1), ("4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d", 1),
                      ("N_FICHIERS_ORGANISME=26", 1), ("N_FICHIERS_ORGANISME=22", 1), ("lancer_pilote4_gemini_v9.sh\n", 0)):
    k = t.count(motif)
    if k != permis:
        sys.exit(f"refus : {motif!r} présent {k} fois après dérivation (attendu {permis})")
sortie.write_text(t, encoding="utf-8")
print(f"lanceur écrit : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()}")

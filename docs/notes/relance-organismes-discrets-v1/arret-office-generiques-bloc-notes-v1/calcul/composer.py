# -*- coding: utf-8 -*-
"""Compose le fichier rendu à partir des opérations contrôlées, puis le relit : le bloc JSON qu'il porte,
réappliqué au brouillon 51, doit rendre l'empreinte annoncée."""
import hashlib
import json
import re
import sys

TEXTE, DOSSIER, SORTIE = sys.argv[1], sys.argv[2], sys.argv[3]

ops = json.load(open(DOSSIER + "/operations.json", encoding="utf-8"))["operations"]
bloc = json.dumps({"operations": ops}, ensure_ascii=False, indent=1)
apres = open(DOSSIER + "/texte-apres-application.md", "rb").read()
empreinte_apres = hashlib.sha256(apres).hexdigest()
entete = open(DOSSIER + "/entete.md", encoding="utf-8").read()
note = open(DOSSIER + "/note.md", encoding="utf-8").read()

# compte de mots de la note (hors titre de section)
mots = len(re.findall(r"\S+", note))
print("mots de la note :", mots)
assert mots <= 400, "note de plus de 400 mots"

n_rem = sum(op["type"] == "remplacer" for op in ops)
n_ins = sum(op["type"] == "inserer_apres" for op in ops)
lignes_rem = sorted({op["ligne"] for op in ops if op["type"] == "remplacer"})
lignes_ins = sorted(op["ligne"] for op in ops if op["type"] == "inserer_apres")

entete = (entete
          .replace("@@EMPREINTE_APRES@@", empreinte_apres)
          .replace("@@N_OPS@@", str(len(ops)))
          .replace("@@N_REM@@", str(n_rem))
          .replace("@@N_INS@@", str(n_ins))
          .replace("@@LIGNES_REM@@", ", ".join(str(x) for x in lignes_rem))
          .replace("@@LIGNES_INS@@", ", ".join(str(x) for x in lignes_ins)))
assert "@@" not in entete, "marque non remplacée dans l'en-tête"

doc = entete.rstrip("\n") + "\n\n## 1. Opérations\n\n```json\n" + bloc + "\n```\n\n## 2. Note\n\n" + note.rstrip("\n") + "\n"
open(SORTIE, "w", encoding="utf-8", newline="").write(doc)

# --- relecture : le bloc JSON du fichier rendu, réappliqué, rend-il l'empreinte annoncée ?
relu = open(SORTIE, encoding="utf-8").read()
m = re.search(r"```json\n(.*?)\n```", relu, re.S)
ops2 = json.loads(m.group(1))["operations"]
brut = open(TEXTE, "rb").read()
assert hashlib.sha256(brut).hexdigest() == "6de63aabf773559b43574b25737b4b93f1d87ab3665603c462da1627cbaa97bf"
L = brut.decode("utf-8")[:-1].split("\n")
for op in ops2:                      # ordre écrit, numéros courants
    i = op["ligne"] - 1
    if op["type"] == "remplacer":
        assert L[i].count(op["ancien"]) == 1, (op["ligne"], op["ancien"][:50])
        L[i] = L[i].replace(op["ancien"], op["nouveau"])
    else:
        L.insert(i + 1, op["texte"])
h = hashlib.sha256(("\n".join(L) + "\n").encode("utf-8")).hexdigest()
assert h == empreinte_apres, (h, empreinte_apres)
assert empreinte_apres in relu
print("fichier rendu :", SORTIE)
print("opérations :", len(ops2), "; empreinte du texte après application :", h)
print("empreinte du fichier rendu :", hashlib.sha256(open(SORTIE, "rb").read()).hexdigest())

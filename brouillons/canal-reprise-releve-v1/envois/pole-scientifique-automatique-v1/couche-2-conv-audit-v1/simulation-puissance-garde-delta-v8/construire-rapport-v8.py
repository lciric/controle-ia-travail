"""Construit `rapport-puissance-garde-delta-v8.md` depuis `rapport-v8-gabarit.md` : les tableaux sont lus dans `resume-v8.md`, les nombres de graine dans `resume-v8-sortie.json`, les empreintes
sont recalculées sur les fichiers (et comparées à leurs empreintes compagnons) ; aucun nombre de tableau n'est recopié à la main. Refuse (code 1) si un repère `{{…}}` reste sans valeur, si un
bloc manque, si une empreinte compagnon diffère du fichier ou si le manifeste d'ensemble est absent. Mode « x » (R12).
Usage : python3 -I -B construire-rapport-v8.py DOSSIER SORTIE.md
"""
import datetime
import hashlib
import json
import os
import re
import sys

DOSSIER, SORTIE = os.path.abspath(sys.argv[1]), sys.argv[2]


def sha(nom):
    h = hashlib.sha256()
    with open(os.path.join(DOSSIER, nom), "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def sha_scelle(nom):
    """Empreinte du fichier, vérifiée contre son compagnon `.sha256` (R6)."""
    vraie = sha(nom)
    comp = os.path.join(DOSSIER, nom + ".sha256")
    if not os.path.exists(comp):
        raise SystemExit(f"fichier non scellé : {nom}")
    ligne = open(comp, encoding="utf-8").read().split()
    if ligne[0] != vraie or ligne[1] != nom:
        raise SystemExit(f"empreinte compagnon différente pour {nom}")
    return vraie


blocs = {}
cle = None
for l in open(os.path.join(DOSSIER, "resume-v8.md"), encoding="utf-8").read().splitlines():
    m = re.match(r"<!-- (\w+) -->", l)
    if m:
        cle = m.group(1)
        blocs[cle] = []
    elif cle is not None:
        blocs[cle].append(l)
blocs = {k: "\n".join(v).strip() for k, v in blocs.items()}
r = json.load(open(os.path.join(DOSSIER, "resume-v8-sortie.json"), encoding="utf-8"))
pct = lambda x: f"{100 * x:.1f} %".replace(".", ",")
val = dict(blocs)
val["GRAINE_MAX"] = pct(r["GRAINE"]["ecart_relatif_maximal"])
val["GRAINE_ETENDUE"] = pct(r["GRAINE"]["etendue_relative_maximale"])
val["DATE_UTC"] = datetime.datetime.now(datetime.timezone.utc).strftime("%d/%m/%Y, %H:%M UTC")
val["HASH_SCRIPT"] = sha_scelle("simulation-puissance-garde-delta-v8.py")[:8] + "…"
val["HASH_MANIFESTE"] = sha_scelle("manifeste-puissance-garde-delta-v8.json")[:8] + "…"
for k, f in (("H_identite_v7", "verif-identite-v7-v8-sortie.json"), ("H_identite_gd7", "verif-identite-gd7-v8-sortie.json"), ("H_copule_strates", "verif-copule-strates-v8-sortie.json"),
             ("H_ebh_pole", "verif-ebh-pole-v8-sortie.json"), ("H_sans_git", "verif-sans-git-v8-sortie.json"), ("H_essais", "essais-entrees-v8-sortie.json")):
    val[k] = sha_scelle(f)[:8] + "…"
cles = ["simulation-puissance-garde-delta-v8.py", "lancer-passages-v8.sh", "lancer-complements-v8.sh", "lancer-verifications-v8.sh", "tableaux-v8.py", "tableaux-v8.md", "tableaux-v8-sortie.json",
        "resume-v8.py", "resume-v8.md", "resume-v8-sortie.json", "incertitude-graine-n80-v8.py", "incertitude-graine-n80-v8-sortie.json", "precision-rho-pilote-v8.py", "precision-rho-pilote-v8-sortie.json",
        "chiffres-v7-repris-v8.py", "chiffres-v7-repris-v8-sortie.json", "verif-identite-v7-v8.py", "verif-identite-v7-v8-sortie.json", "verif-identite-gd7-v8.py", "verif-identite-gd7-v8-sortie.json",
        "verif-copule-strates-v8.py", "verif-copule-strates-v8-sortie.json", "verif-ebh-pole-v8.py", "verif-ebh-pole-v8-sortie.json", "verif-sans-git-v8.py", "verif-sans-git-v8-sortie.json",
        "essais-entrees-v8.py", "essais-entrees-v8-sortie.json", "assembler-manifeste-v8.py", "manifeste-puissance-garde-delta-v8.json", "rapport-v8-gabarit.md", "construire-rapport-v8.py"]
L = ["Chaque fichier a son empreinte compagnon `.sha256` (vérifiée par le constructeur). Les 52 passages (sortie, journal, manifeste) sont listés avec leurs empreintes dans `manifeste-puissance-garde-delta-v8.json`.", "",
     "| fichier | sha256 |", "| --- | --- |"]
for f in cles:
    L.append(f"| `{f}` | `{sha_scelle(f)}` |")
val["EMPREINTES"] = "\n".join(L)
texte = open(os.path.join(DOSSIER, "rapport-v8-gabarit.md"), encoding="utf-8").read()
absents = [k for k in set(re.findall(r"\{\{(\w+)\}\}", texte)) if k not in val]
if absents:
    raise SystemExit(f"repères sans valeur : {sorted(absents)}")
for k, v in val.items():
    texte = texte.replace("{{" + k + "}}", v)
reste = re.findall(r"\{\{\w+\}\}", texte)
if reste:
    raise SystemExit(f"repères restants : {reste}")
with open(SORTIE, "x", encoding="utf-8") as f:
    f.write(texte)
print("écrit", SORTIE, len(texte), "caractères")

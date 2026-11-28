# -*- coding: utf-8 -*-
"""Construit l'erratum 1 du programme v3 (lemme d'additivité, application).

Usage : construire.py SOURCE_PROGRAMME_V3 FICHIER_DE_SORTIE HEURE_UTC
Le corps du document est dans corps.md (même dossier), avec des jalons
@@...@@ remplacés ici : l'énoncé, les sept blocs, l'empreinte de la source.
Après écriture, le fichier produit est relu par un analyseur indépendant
(expression régulière), ses entrées sont réappliquées à la source, et le
résultat est comparé à l'application directe des textes de entrees.py.
"""
import hashlib
import re
import sys
from pathlib import Path

ICI = Path(__file__).parent
sys.path.insert(0, str(ICI))
import entrees  # noqa: E402

source = Path(sys.argv[1])
sortie = Path(sys.argv[2])
heure = sys.argv[3]

brut = source.read_bytes()
empreinte = hashlib.sha256(brut).hexdigest()
programme = brut.decode("utf-8")

blocs = []
for rang, (ancien, nouveau, raison) in enumerate(entrees.ENTREES, 1):
    blocs.append(
        f"**L-{rang}.** ANCIEN : « {ancien} »\n"
        f"NOUVEAU : « {nouveau} »\n"
        f"Raison : {raison}"
    )
blocs_texte = "\n\n".join(blocs)

for chaine in ("des renvois corrigés).", "Hors de ce que vise cette demande"):
    assert programme.count(chaine) == 1, (chaine, programme.count(chaine))
corrige = programme
for _ancien, _nouveau, _raison in entrees.ENTREES:
    assert corrige.count(_ancien) == 1
    corrige = corrige.replace(_ancien, _nouveau, 1)
empreinte_corrige = hashlib.sha256(corrige.encode("utf-8")).hexdigest()

corps = (ICI / "corps.md").read_text(encoding="utf-8")
remplacements = {
    "@@EMPREINTE_CORRIGE@@": empreinte_corrige,
    "@@HEURE@@": heure,
    "@@EMPREINTE@@": empreinte,
    "@@EMPREINTE8@@": empreinte[:8],
    "@@S1@@": entrees.S1,
    "@@S2@@": entrees.S2,
    "@@S3@@": entrees.S3,
    "@@ENONCE@@": entrees.ENONCE,
    "@@REFUTATION@@": entrees.REFUTATION,
    "@@BLOCS@@": blocs_texte,
}
for jalon, valeur in remplacements.items():
    if jalon not in corps:
        sys.exit(f"jalon absent du corps : {jalon}")
    corps = corps.replace(jalon, valeur)
if "@@" in corps:
    sys.exit("jalon non remplacé dans le corps")
if not corps.endswith("\n"):
    corps += "\n"
if sortie.exists():
    print("attention : le fichier de sortie existait, il est réécrit (pièce non scellée, non committée)")
sortie.write_text(corps, encoding="utf-8")

# --- relecture indépendante du fichier écrit -------------------------------
ecrit = sortie.read_text(encoding="utf-8")
cibles = re.findall(r"^Cible : (.+)$", ecrit, flags=re.M)
assert cibles == ["docs/programme-controle-ia-v3.md"], cibles
motif = re.compile(
    r"^\*\*L-(\d+)\.\*\* ANCIEN : « (.*) »\nNOUVEAU : « (.*) »\nRaison : (.*)$",
    flags=re.M,
)
lus = motif.findall(ecrit)
assert [int(x[0]) for x in lus] == list(range(1, len(entrees.ENTREES) + 1)), [x[0] for x in lus]
# aucun autre « ANCIEN : » ni « NOUVEAU : » que ceux des blocs
assert ecrit.count("ANCIEN :") == len(lus), ecrit.count("ANCIEN :")
assert ecrit.count("NOUVEAU :") == len(lus), ecrit.count("NOUVEAU :")
assert ecrit.count("Raison :") == len(lus), ecrit.count("Raison :")
assert ecrit.count("«") == ecrit.count("»"), (ecrit.count("«"), ecrit.count("»"))
assert len(re.findall(r"^\*\*L-\d+\.\*\*", ecrit, flags=re.M)) == len(lus)

texte = programme
for num, ancien, nouveau, raison in lus:
    assert (ancien, nouveau, raison) == entrees.ENTREES[int(num) - 1], f"L-{num} : texte altéré à l'écriture"
    n = texte.count(ancien)
    assert n == 1, f"L-{num} : {n} occurrence(s) au moment de l'application"
    texte = texte.replace(ancien, nouveau, 1)
    assert texte.count(ancien) == 0, f"L-{num} : texte d'origine encore présent"
direct = (ICI / "programme-v3-corrige-a-blanc.md").read_text(encoding="utf-8")
assert texte == direct, "l'application relue du fichier diffère de l'application directe"

# l'énoncé figure tel quel aux trois endroits : section 1 (trois phrases), entrée L-4, ligne de la table
assert ecrit.count(entrees.ENONCE) >= 2, ecrit.count(entrees.ENONCE)
for s in (entrees.S1, entrees.S2, entrees.S3, entrees.REFUTATION):
    assert ecrit.count(s) == 3, (ecrit.count(s), s[:40])
assert ecrit.count(entrees.ENONCE) == 3, ecrit.count(entrees.ENONCE)
# mots proscrits par la consigne
for proscrit in ("inédit", "Inédit"):
    assert proscrit not in ecrit, proscrit

mots = len(re.findall(r"\S+", ecrit))
hors_blocs = len(re.findall(r"\S+", ecrit.replace(blocs_texte, "")))
print("écrit :", sortie)
print("sha256 du fichier écrit :", hashlib.sha256(sortie.read_bytes()).hexdigest())
print("source :", source, "| sha256", empreinte)
print("entrées relues du fichier :", len(lus), "| application relue identique à l'application directe : oui")
print("mots :", mots, "| hors blocs :", hors_blocs, "| lignes :", ecrit.count("\n"))
print("sha256 du programme corrigé à blanc :", hashlib.sha256(texte.encode("utf-8")).hexdigest())

# -*- coding: utf-8 -*-
"""Vérifie les sept entrées contre le programme v3 lu (copie du bloc-notes).

Pour chaque entrée, dans l'ordre : le texte d'origine tient sur une seule
ligne de la source, y figure une fois et une seule au moment de son
application, et n'y figure plus après ; ni le texte d'origine ni le texte
neuf ne portent de guillemet français, de saut de ligne ou de barre
verticale ; la marque de simulation n'est ni ajoutée ni retirée ; le nombre
de lignes ne change pas. Écrit le texte corrigé et un diff dans le dossier
de travail. Sort avec un code non nul au premier défaut.
"""
import difflib
import hashlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import entrees  # noqa: E402

SOURCE = Path(sys.argv[1])
SORTIE = Path(__file__).parent

brut = SOURCE.read_bytes()
print("source :", SOURCE)
print("sha256 :", hashlib.sha256(brut).hexdigest())
texte = brut.decode("utf-8")
origine = texte
lignes_origine = origine.split("\n")

defauts = []
for rang, (ancien, nouveau, raison) in enumerate(entrees.ENTREES, 1):
    nom = f"L-{rang}"
    for etiquette, chaine in (("origine", ancien), ("neuf", nouveau), ("raison", raison)):
        for interdit, quoi in (("«", "guillemet ouvrant"), ("»", "guillemet fermant"),
                               ("\n", "saut de ligne"), ("|", "barre verticale"),
                               (" ", "espace insécable"), (" ", "espace fine insécable")):
            if interdit in chaine:
                defauts.append(f"{nom} : {quoi} dans le texte « {etiquette} »")
        if chaine != chaine.strip():
            defauts.append(f"{nom} : espace en bord du texte « {etiquette} »")
    if "sous simulation" in nouveau:
        defauts.append(f"{nom} : marque de simulation dans le texte neuf")
    # présence dans la source d'origine, sur une seule ligne
    n_origine = origine.count(ancien)
    lignes = [i for i, l in enumerate(lignes_origine, 1) if ancien in l]
    # présence au moment de l'application
    n_avant = texte.count(ancien)
    if n_avant != 1:
        defauts.append(f"{nom} : {n_avant} occurrence(s) au moment de l'application")
    if len(lignes) != 1:
        defauts.append(f"{nom} : le texte d'origine ne tient pas sur une ligne unique ({lignes})")
    if ancien == nouveau:
        defauts.append(f"{nom} : texte neuf identique")
    texte = texte.replace(ancien, nouveau, 1) if n_avant == 1 else texte
    n_apres = texte.count(ancien)
    if n_apres != 0:
        defauts.append(f"{nom} : le texte d'origine figure encore {n_apres} fois après application")
    if texte.count(nouveau) != 1:
        defauts.append(f"{nom} : le texte neuf figure {texte.count(nouveau)} fois après application")
    print(f"{nom} : source {n_origine} fois, ligne(s) {lignes} ; à l'application {n_avant} ; après {n_apres} ; "
          f"{len(ancien)} -> {len(nouveau)} signes ; lieu : {entrees.LIEUX[rang - 1]}")

# les textes neufs des entrées antérieures ne doivent pas avoir créé de doublon d'un texte d'origine postérieur
if origine.count("sous simulation") != texte.count("sous simulation"):
    defauts.append("marque de simulation : compte changé")
if origine.count("\n") != texte.count("\n"):
    defauts.append("nombre de lignes changé")
# toutes les entrées restent présentes à la fin (aucune n'écrase l'autre)
for rang, (ancien, nouveau, _r) in enumerate(entrees.ENTREES, 1):
    if texte.count(nouveau) != 1:
        defauts.append(f"L-{rang} : texte neuf absent ou doublé dans le texte final")

lignes_finales = texte.split("\n")
changees = [i for i, (a, b) in enumerate(zip(lignes_origine, lignes_finales), 1) if a != b]
print("lignes changées :", changees)
print("marque de simulation :", origine.count("sous simulation"), "->", texte.count("sous simulation"))
print("lignes :", origine.count("\n"), "->", texte.count("\n"))

# phrases qui diraient encore le lemme non revendiqué ou seulement mentionné
import re
motif = re.compile(r"(non revendiqu\w*|plus revendiqu\w*|mentionn\w*)")
print("--- lignes du texte corrigé qui portent encore « mentionné » ou « non revendiqué » :")
for i, l in enumerate(lignes_finales, 1):
    for m in motif.finditer(l):
        debut = max(0, m.start() - 70)
        print(f"  ligne {i} : …{l[debut:m.end() + 40]}…")

(SORTIE / "programme-v3-corrige-a-blanc.md").write_text(texte, encoding="utf-8")
diff = difflib.unified_diff(lignes_origine, lignes_finales, "programme v3 lu", "programme v3 corrigé à blanc", lineterm="", n=0)
(SORTIE / "diff-a-blanc.txt").write_text("\n".join(diff) + "\n", encoding="utf-8")

if defauts:
    print("DÉFAUTS :")
    for d in defauts:
        print("  -", d)
    sys.exit(1)
print("Aucun défaut.")

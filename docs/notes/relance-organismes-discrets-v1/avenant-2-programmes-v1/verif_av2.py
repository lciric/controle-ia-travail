#!/usr/bin/env python3
"""verif_av2.py — relit l'avenant 2 composé.

1. Chaque nombre à virgule, et chaque entier écrit par groupes de trois chiffres,
   est cherché dans la sortie du calcul, puis dans les pièces lues ; ceux qui ne s'y
   trouvent pas sont listés, pour une relecture à la main.
2. Aucune marque de gabarit, aucun identifiant de GO d'un autre jour que le
   21 novembre, aucune des formules que le mandat interdit de recopier, aucun emoji.

usage : verif_av2.py PIECE ARBRE BLOC_NOTES
"""
import os
import re
import sys
import unicodedata

PIECE, ARBRE, BLOC = sys.argv[1:4]
REL = os.path.join(ARBRE, "docs/notes/relance-organismes-discrets-v1")
doc = open(PIECE, encoding="utf-8").read()

calc = open(os.path.join(BLOC, "calc_av2.sortie.txt"), encoding="utf-8").read()
sources = ""
for nom in (
    "devis-essais-admission-mistral-neon-bras-a-v1.md",
    "avenant-1-devis-essais-admission-recharge-et-deux-cles-v3.md",
    "verification-avenant-1-v3-devis-essais-admission-v1.md",
    "confrontation-regle-google-livraison3-v1.md",
    "note-programme-essais-admission-bras-a-v3.md",
    "mandat-redacteur-fable-avenant-2-plafond-65536-v1.md",
):
    sources += open(os.path.join(REL, nom), encoding="utf-8").read() + "\n"
for nom in ("regle_google.txt", "go_lignes.txt", "od_lignes.txt"):
    sources += open(os.path.join(BLOC, nom), encoding="utf-8").read() + "\n"

# le corps de la pièce, sans la section 12 (qui est la sortie du calcul elle-même)
corps = doc.split("\n## 12. Calculs, par programme")[0]
NOMBRE = re.compile(r"(?<![\d,.])\d{1,3}(?: \d{3})*(?:,\d+)?(?![\d,])")


def present(n, texte):
    return re.search(r"(?<![\d,])" + re.escape(n) + r"(?!\d)", texte) is not None


vus = {}
for m in NOMBRE.finditer(corps):
    n = m.group(0)
    if "," not in n and " " not in n:
        continue  # petit entier : non contrôlé
    vus.setdefault(n, 0)
    vus[n] += 1
hors = []
for n in sorted(vus, key=lambda x: (len(x), x)):
    ou = "calcul" if present(n, calc) else ("pièces" if present(n, sources) else None)
    if ou is None:
        hors.append(n)
print(f"nombres contrôlés : {len(vus)} distincts ; dans le calcul : {sum(present(n, calc) for n in vus)} ; "
      f"dans les pièces seulement : {sum((not present(n, calc)) and present(n, sources) for n in vus)} ; nulle part : {len(hors)}")
for n in hors:
    i = corps.find(n)
    print("   NULLE PART :", repr(n), "…", corps[max(0, i - 60):i + len(n) + 40].replace("\n", " "))

# marques et interdits
assert "@@" not in doc, "marque de gabarit restante"
go = set(re.findall(r"GO-\d{4}-\d{2}-\d{2}-\d+", doc))
print("identifiants de GO nommés :", ", ".join(sorted(go)))
assert all(g.startswith("GO-2026-11-21-") for g in go), go
assert "GO-2026-11-19" not in doc
for interdit in ("intervalle impossible", "non ajustable", "moniteur appris"):
    assert interdit not in doc, interdit
emojis = [c for c in doc if unicodedata.category(c) == "So" or ord(c) > 0x1F000]
assert not emojis, emojis
# chemins cloisonnés : aucun ne doit figurer, hors la commande du registre
for motif in ("bases/", "sondes/", "/t07", "T0.8", "mots_et_cout", "bras-a-moniteurs", "bras-a-contre-lecture-habilitee",
              "bras-a-sans-interne", "bras_a_v2_habilite", "autres_moniteurs", "runs/", "essai-mesure-lecteurs",
              "docs/sources"):
    assert motif not in doc, ("chemin cloisonné nommé", motif)
assert doc.count(".claude/settings") == 1  # la seule mention : « non ouvert »
assert doc.count("registres/") == 2, doc.count("registres/")
lignes = doc.split("\n")
print(f"lignes : {len(lignes)} ; caractères : {len(doc)} ; plus longue ligne : {max(len(l) for l in lignes)}")
print("vérification : faite")

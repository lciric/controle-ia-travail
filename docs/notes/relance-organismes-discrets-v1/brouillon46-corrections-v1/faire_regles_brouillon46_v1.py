#!/usr/bin/env python3
"""Fichier des règles d'admission sur le brouillon 46, tiré du gabarit,
sur le modèle exact du fichier du brouillon 44 (même forme, sans la ligne
d'état de gabarit). Vérifie qu'il porte les huit règles caractère pour
caractère (lignes 542 à 550 du brouillon 46).

Usage : python3 -I faire_regles_brouillon46_v1.py RACINE_DU_DEPOT
"""
import hashlib
import pathlib
import sys

R = pathlib.Path(sys.argv[1])
D = "docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/"
GAB, GAB_SHA = D + "regles-admission-bras-a-v1-gabarit.md", None
M44 = D + "regles-admission-bras-a-v1-brouillon44.md"
M44_SHA = "cd0e384c21516b95c0c01ba2275d79a034777c92aca257b5700052724cfb2865"
SORTIE = D + "regles-admission-bras-a-v1-brouillon46.md"
B44_SHA = "b30aa902a8135f888911519f4efd0a3583fddd6b8f748889146d9bca5da43eb8"
B46 = "prereg/T0.7-organismes-discrets-v-a-v2-brouillon46.md"


def arret(m):
    sys.exit("ARRÊT : " + m)


def sha(p):
    return hashlib.sha256((R / p).read_bytes()).hexdigest()


gab_compagnon = (R / (GAB + ".sha256")).read_text().split()[0]
if sha(GAB) != gab_compagnon:
    arret("gabarit : empreinte différente de son compagnon")
if sha(M44) != M44_SHA:
    arret("fichier du brouillon 44 : empreinte")
b46_sha = sha(B46)
b46 = (R / B46).read_text(encoding="utf-8").split("\n")
regles46 = b46[541:550]

g = (R / GAB).read_text(encoding="utf-8").split("\n")
etat = [i for i, s in enumerate(g) if s.startswith("- état : gabarit")]
if len(etat) != 1:
    arret("ligne d'état du gabarit")
del g[etat[0]]
texte = "\n".join(g)

REMP = [
    ("— v1, GABARIT\n", "— v1, définitif sur le brouillon 46\n"),
    ("- empreinte du texte en vigueur : 4f91b535ad91581510615c97039a4cae0a96f4d788088b2aff666d4c3d3f97b3\n",
     f"- empreinte du texte en vigueur : {b46_sha}\n"),
    ("- texte en vigueur : prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md\n",
     f"- texte en vigueur : {B46}\n"),
    ("- lignes du texte recopiées : 521 à 529 (", "- lignes du texte recopiées : 542 à 550 ("),
    ("scripts/chef_essais_admission_bras_a_v1.py", "scripts/chef_essais_admission_bras_a_v6.py"),
    ("les lignes 521 à 529 du texte en vigueur", "les lignes 542 à 550 du texte en vigueur"),
]
for a, n in REMP:
    if texte.count(a) != 1:
        arret("ancien non unique : " + a)
    texte = texte.replace(a, n)

# même forme que le fichier du brouillon 44 : seules les valeurs du texte en vigueur diffèrent
m44 = (R / M44).read_text(encoding="utf-8")
attendu = (m44.replace("définitif sur le brouillon 44", "définitif sur le brouillon 46")
              .replace(B44_SHA, b46_sha)
              .replace("prereg/T0.7-organismes-discrets-v-a-v2-brouillon44.md", B46)
              .replace("529 à 537", "542 à 550"))
if texte != attendu:
    arret("forme différente du fichier du brouillon 44")

# les huit règles, caractère pour caractère
lignes = texte.split("\n")
i = lignes.index("## Les huit règles, recopiées à la lettre, dans leur numérotation")
corps = lignes[i + 2:i + 2 + 9]
if corps != regles46:
    arret("les huit règles ne sont pas égales à celles du brouillon 46")
if lignes[i + 2 + 9:] not in ([""], []):
    arret("lignes en trop après les règles")

if (R / SORTIE).exists():
    arret("existe déjà (R12)")
(R / SORTIE).write_text(texte, encoding="utf-8")
print("écrit", SORTIE, hashlib.sha256(texte.encode()).hexdigest(), "; règles égales : True")

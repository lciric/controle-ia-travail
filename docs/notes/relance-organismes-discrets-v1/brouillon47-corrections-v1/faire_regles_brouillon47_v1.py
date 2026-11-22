#!/usr/bin/env python3
"""Fichier des règles d'admission sur le brouillon 47, sur le modèle exact du
fichier du brouillon 46 : seules changent l'empreinte et le chemin du texte en
vigueur, et le nom du programme de la file du juge
(`scripts/chef_essais_admission_bras_a_v12.py`, contre-lecture 10, m-4).
Vérifie qu'il porte les huit règles caractère pour caractère (lignes 542 à
550 du brouillon 47, égales à celles du brouillon 46).

Usage : python3 -I faire_regles_brouillon47_v1.py RACINE_DU_DEPOT
"""
import hashlib
import pathlib
import sys

R = pathlib.Path(sys.argv[1])
D = "docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/"
M46 = D + "regles-admission-bras-a-v1-brouillon46.md"
M46_SHA = "fdc9254fc2294343e1ff1d5d527ac8b24a466f084ff38d674013580321eb31d2"
SORTIE = D + "regles-admission-bras-a-v1-brouillon47.md"
B46 = "prereg/T0.7-organismes-discrets-v-a-v2-brouillon46.md"
B46_SHA = "b5e1031c9b92d7643815e9d18abec86f900fee0931eb6030839729b2f32c3fb9"
B47 = "prereg/T0.7-organismes-discrets-v-a-v2-brouillon47.md"
CHEF12 = "scripts/chef_essais_admission_bras_a_v12.py"
CHEF12_SHA = "6aa04397997a52785ce4bd05e1b7a45c5886e1565f3e2927984b08373d9758b1"


def arret(m):
    sys.exit("ARRÊT : " + m)


def sha(p):
    return hashlib.sha256((R / p).read_bytes()).hexdigest()


for p, h in [(M46, M46_SHA), (B46, B46_SHA), (CHEF12, CHEF12_SHA)]:
    if sha(p) != h:
        arret(p + " : empreinte")
b47_sha = sha(B47)
b46 = (R / B46).read_text(encoding="utf-8").split("\n")
b47 = (R / B47).read_text(encoding="utf-8").split("\n")
if b46[541:550] != b47[541:550]:
    arret("les huit règles diffèrent entre les brouillons 46 et 47")

texte = (R / M46).read_text(encoding="utf-8")
REMP = [
    ("définitif sur le brouillon 46\n", "définitif sur le brouillon 47\n"),
    (f"- empreinte du texte en vigueur : {B46_SHA}\n", f"- empreinte du texte en vigueur : {b47_sha}\n"),
    (f"- texte en vigueur : {B46}\n", f"- texte en vigueur : {B47}\n"),
    ("scripts/chef_essais_admission_bras_a_v6.py", CHEF12),
]
for a, n in REMP:
    if texte.count(a) != 1:
        arret("ancien non unique : " + a)
    texte = texte.replace(a, n)

lignes = texte.split("\n")
i = lignes.index("## Les huit règles, recopiées à la lettre, dans leur numérotation")
corps = lignes[i + 2:i + 2 + 9]
if corps != b47[541:550]:
    arret("les huit règles ne sont pas égales à celles du brouillon 47")
if lignes[i + 2 + 9:] not in ([""], []):
    arret("lignes en trop après les règles")
if "lignes du texte recopiées : 542 à 550" not in texte:
    arret("numéros de ligne")

if (R / SORTIE).exists():
    arret("existe déjà (R12)")
(R / SORTIE).write_text(texte, encoding="utf-8")
print("écrit", SORTIE, hashlib.sha256(texte.encode()).hexdigest(), "; règles égales : True")

#!/usr/bin/env python3
"""Brouillon 48 du bras A des organismes discrets, depuis le brouillon 47.

Porte M-6 et M-7 de la contre-lecture 10, option A, sur les mots du
directeur (GO-2026-11-22-73 : « bras A M-6 (A) go, M-7 (A) go »), par
remplacements exacts ; les textes proposés sont lus dans le fichier de la
contre-lecture (empreinte contrôlée), non recopiés à la main. Chaque ancien
doit se trouver une seule fois, sinon arrêt. Les huit règles d'admission
(lignes 542 à 550) doivent rester égales, caractère pour caractère, aux mêmes
numéros de ligne ; aucune ligne n'est ajoutée ; avant elles, seules les
lignes 1 et 3 changent. Écrit aussi le fichier des règles sur le brouillon 48.

Usage : python3 -I appliquer_corrections_brouillon48_v1.py RACINE_DU_DEPOT
"""
import hashlib
import pathlib
import sys

RACINE = pathlib.Path(sys.argv[1])
CL10 = "docs/notes/relance-organismes-discrets-v1/contre-lecture-10-brouillon46-bras-a-v1.md"
CL10_SHA = "f711c9be09b8912adcb82d469a09f03e89b80ac67950cc2235e4d2cfebda1881"
B47 = "prereg/T0.7-organismes-discrets-v-a-v2-brouillon47.md"
B47_SHA = "f59f6b4ed2b1198c3781badf83692d593ed4ade0df5baa9f0e4ea8b1827a6cb9"
B48 = "prereg/T0.7-organismes-discrets-v-a-v2-brouillon48.md"
D = "docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/"
R47 = D + "regles-admission-bras-a-v1-brouillon47.md"
R47_SHA = "4ae135309e60a68c5fe07679787d23032db200cbb22e8c7a95a04de984978b77"
R48 = D + "regles-admission-bras-a-v1-brouillon48.md"
REGLES_SHA = "3d1f0afe82f5aeb3bf5dd757cb6d814e19c66b93a89a65b6f08677823e1b8f96"


def arret(msg):
    sys.exit("ARRÊT : " + msg)


def lire(chemin, sha):
    octets = (RACINE / chemin).read_bytes()
    h = hashlib.sha256(octets).hexdigest()
    if h != sha:
        arret(f"{chemin} : empreinte {h} au lieu de {sha}")
    return octets.decode("utf-8")


v = lire(CL10, CL10_SHA).split("\n")
t47 = lire(B47, B47_SHA)
r47 = lire(R47, R47_SHA)


def entre(s, debut, fin, dernier=False):
    i = s.index(debut) + len(debut)
    j = s.rindex(fin) if dernier else s.index(fin, i)
    if j <= i:
        arret("extraction impossible : " + debut)
    return s[i:j]


# --- textes de la contre-lecture 10, lus dans son fichier ---
if not v[39].startswith("**M-6.") or not v[41].startswith("**M-7."):
    arret("lignes 40 et 42 de la contre-lecture")
M6 = entre(v[39], "après le déclencheur C6 : « ", " ». C'est l'ajout")
M7_H = entre(v[42], "« est strictement positive » : « ", " ».", dernier=True)
M7_B9 = entre(v[43], "- Ligne B9 : ajouter « ", " ».", dernier=True)
for nom, val, debut, fin in [
    ("M6", M6, "**au moins une dose en C4** (pendant", "anomalie : ligne A11"),
    ("M7_H", M7_H, "; elle n'est dite **confirmée**", "même si une hausse plus petite est établie"),
    ("M7_B9", M7_B9, "; si le test de la hausse", "« hausse positive établie, sous l'effet minimal d'intérêt »"),
]:
    if not (val.startswith(debut) and val.endswith(fin)):
        arret(f"extraction {nom} : {val!r}")

# --- texte du correcteur (histoire), déclaré ---
PHRASE = ("Le brouillon 48 porte M-6 et M-7 de la contre-lecture 10, option A, mots du "
          "directeur (GO-2026-11-22-73 : « bras A M-6 (A) go, M-7 (A) go »), mot pour mot, "
          "aux textes proposés par la contre-lecture ; rien d'autre ne change. "
          "**État au brouillon 47** : ")

REMPLACEMENTS = [
    ("titre", "— v2, BROUILLON 47\n", "— v2, BROUILLON 48\n"),
    ("statut", "**Statut : brouillon 47, non exécutable.** Le brouillon 47,",
     "**Statut : brouillon 48, non exécutable.** " + PHRASE + "Le brouillon 47,"),
    ("M-7, énoncé de l'hypothèse de désappariement",
     "`Δτ(·, p)`, est strictement positive. La dose ¼",
     "`Δτ(·, p)`, est strictement positive " + M7_H + ". La dose ¼"),
    ("M-7, ligne B9",
     "**réserve écrite : si l'effet n'est pas concentré sur une petite part des tâches** "
     "(6.9 ; GO-2026-11-19-24, point 2) |",
     "**réserve écrite : si l'effet n'est pas concentré sur une petite part des tâches** "
     "(6.9 ; GO-2026-11-19-24, point 2) " + M7_B9 + " |"),
    ("M-6, 7.6, après le déclencheur C6",
     "contre-lecture, R-4) ; **côté nul** :",
     "contre-lecture, R-4) ; " + M6 + " ; **côté nul** :"),
    ("Contre-lecture, traitement",
     "M-3, M-6 et M-7 en attente (statut).",
     "au brouillon 48, M-6 et M-7, option A (GO-2026-11-22-73), mot pour mot ; "
     "M-3 en attente (statut)."),
]

t48 = t47
for nom, ancien, neuf in REMPLACEMENTS:
    n = t48.count(ancien)
    if n != 1:
        arret(f"{nom} : ancien trouvé {n} fois")
    t48 = t48.replace(ancien, neuf)
    print(f"porté : {nom}")

l47, l48 = t47.split("\n"), t48.split("\n")
if len(l47) != len(l48):
    arret("nombre de lignes changé")
if l47[541:550] != l48[541:550]:
    arret("les huit règles ont bougé")
if hashlib.sha256("\n".join(l48[541:550]).encode()).hexdigest() != REGLES_SHA:
    arret("empreinte des huit règles")
changees = [i + 1 for i in range(len(l47)) if l47[i] != l48[i]]
if [n for n in changees if n < 542] != [1, 3]:
    arret(f"avant les règles, seules les lignes 1 et 3 peuvent changer : {changees}")
print("lignes changées :", changees)

if (RACINE / B48).exists():
    arret(f"{B48} existe déjà (R12)")
(RACINE / B48).write_text(t48, encoding="utf-8")
b48_sha = hashlib.sha256(t48.encode()).hexdigest()
print("écrit", B48, b48_sha)

# --- fichier des règles, sur le modèle exact de celui du 47 ---
REMP = [
    ("définitif sur le brouillon 47\n", "définitif sur le brouillon 48\n"),
    (f"- empreinte du texte en vigueur : {B47_SHA}\n", f"- empreinte du texte en vigueur : {b48_sha}\n"),
    (f"- texte en vigueur : {B47}\n", f"- texte en vigueur : {B48}\n"),
]
texte = r47
for a, n in REMP:
    if texte.count(a) != 1:
        arret("ancien non unique : " + a)
    texte = texte.replace(a, n)
lignes = texte.split("\n")
i = lignes.index("## Les huit règles, recopiées à la lettre, dans leur numérotation")
if lignes[i + 2:i + 2 + 9] != l48[541:550]:
    arret("les huit règles ne sont pas égales à celles du brouillon 48")
if lignes[i + 2 + 9:] not in ([""], []):
    arret("lignes en trop après les règles")
if (RACINE / R48).exists():
    arret("fichier des règles existe déjà (R12)")
(RACINE / R48).write_text(texte, encoding="utf-8")
print("écrit", R48, hashlib.sha256(texte.encode()).hexdigest(), "; règles égales : True")

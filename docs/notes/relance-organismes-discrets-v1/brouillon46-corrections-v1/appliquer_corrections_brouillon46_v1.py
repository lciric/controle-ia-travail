#!/usr/bin/env python3
"""Brouillon 46 du bras A des organismes discrets, depuis le brouillon 45.

Porte les corrections C-1 à C-5 et les mineurs de la vérification du
brouillon 45, par remplacements exacts. Les textes proposés par la
vérification sont lus dans son fichier (empreinte contrôlée), non recopiés
à la main. Chaque ancien doit se trouver une seule fois, sinon arrêt.
Les huit règles d'admission (lignes 542 à 550) doivent rester égales,
caractère pour caractère, aux mêmes numéros de ligne.

Usage : python3 -I appliquer_corrections_brouillon46_v1.py RACINE_DU_DEPOT
"""
import hashlib
import pathlib
import sys

RACINE = pathlib.Path(sys.argv[1])
VERIF = "docs/notes/relance-organismes-discrets-v1/verification-brouillon45-bras-a-v1.md"
VERIF_SHA = "6ab0def272f0f0d48423bcd4aa9a1f81c8753d34ee5d4d512a65e214740bfac0"
B45 = "prereg/T0.7-organismes-discrets-v-a-v2-brouillon45.md"
B45_SHA = "4588944f9658a7ddb563296821392404be96241ba41027b7d15df72194eb6b4d"
B46 = "prereg/T0.7-organismes-discrets-v-a-v2-brouillon46.md"
REGLES_SHA = "3d1f0afe82f5aeb3bf5dd757cb6d814e19c66b93a89a65b6f08677823e1b8f96"


def arret(msg):
    sys.exit("ARRÊT : " + msg)


def lire(chemin, sha):
    octets = (RACINE / chemin).read_bytes()
    h = hashlib.sha256(octets).hexdigest()
    if h != sha:
        arret(f"{chemin} : empreinte {h} au lieu de {sha}")
    return octets.decode("utf-8")


v = lire(VERIF, VERIF_SHA).split("\n")
t45 = lire(B45, B45_SHA)


def ligne(n):
    return v[n - 1]


def citation(n):
    s = ligne(n)
    if not s.startswith("> "):
        arret(f"vérification, ligne {n} : pas une citation")
    return s[2:]


def entre(s, debut, fin):
    i = s.index(debut) + len(debut)
    j = s.rindex(fin)
    if j <= i:
        arret("extraction impossible")
    return s[i:j]


def sans_point_final(s):
    if not s.endswith("."):
        arret("point final attendu : " + s[-40:])
    return s[:-1]


# --- textes de la vérification, lus dans son fichier ---
C1 = citation(44)                       # C-1, point (3)
C1_M2 = entre(ligne(46), "à la place de son traitement : « ", " ». Ajouter")
C2_TETE = citation(50)                  # C-2, tête
C2_MISTRAL = citation(51)
C2_NEON = citation(52)
C3 = citation(60)                       # C-3, ligne 551
C3_1483 = entre(ligne(62), "Ligne 1483 : ajouter « ", " ». Rien d'autre")
C4 = citation(66)                       # C-4
C5_L9 = entre(ligne(70), "- Ligne 9 : « ", " ».")
C5_L2541 = entre(ligne(71), "- Ligne 2541 : « ", " ».")
LAZAR = entre(ligne(81), "Une phrase proposée : « ", " »")
M2_A = entre(ligne(126), "est périmé, à écrire « ", " ». « inscrite")
M2_B = entre(ligne(126), "ajouter « ", " ».")
M3 = entre(ligne(127), "» devient « ", " ».")
M4 = entre(ligne(128), "Écrire « ", " ».")

for nom, val, debut in [
    ("C1", C1, "(brouillon 45 ; vérification du brouillon 44, m-2) : sous la décision"),
    ("C2_TETE", C2_TETE, "reste À REMPLIR : les champs exacts"),
    ("C2_MISTRAL", C2_MISTRAL, "- **Mistral Large 4** :"),
    ("C2_NEON", C2_NEON, "- **`gemini-4-neon`** :"),
    ("C3", C3, "à chacune des deux étapes"),
    ("C4", C4, "(… ; les deux files d'admission sont parties avant elle."),
]:
    if not val.startswith(debut):
        arret(f"extraction {nom} : {val[:60]!r}")

for nom, val, attendu in [
    ("M2_A", M2_A, "1 à 44"),
    ("M2_B", M2_B, "(au brouillon 45 : contre-lecture 10)"),
    ("M3", M3, "m-1 à m-9"),
    ("M4", M4, "aucune section de jugement n'est touchée ; treize lignes de table sont ajoutées"),
]:
    if val != attendu:
        arret(f"extraction {nom} : {val!r}")

C4_QUEUE = C4[len("(… ; les deux files d'admission sont parties avant elle"):]
if not C4_QUEUE.startswith(". Ce n'est pas un écart"):
    arret("C-4 : queue inattendue")

# --- textes du correcteur (le plus court qui porte ce que dit la vérification) ---
VERIF_REF = (f"`{VERIF}`, `{VERIF_SHA}`")
HISTOIRE = (
    "**Statut : brouillon 46, non exécutable.** Le brouillon 46, écrit par Claude Opus 5.5, "
    "agent neuf, par un programme de remplacements exacts, porte les corrections C-1 à C-5 "
    "et les mineurs m-2 à m-7 de la vérification du brouillon 45 (" + VERIF_REF +
    ", « engageable après corrections » : cinq corrections, neuf mineurs), mot pour mot, "
    "sans rien concevoir (décision de Lazar, GO-2026-11-21-84) ; aucune règle, aucun seuil, "
    "aucune issue ni aucune prédiction ne change, et les huit règles d'admission restent "
    "aux lignes 542 à 550, caractère pour caractère. **Information pour Lazar** "
    "(vérification du brouillon 45, partie 3, (b)) : " + LAZAR + " "
    "**État au brouillon 45, dépassé pour ce que le brouillon 46 change** : "
    "Le brouillon 45, d'un rédacteur neuf"
)
M5 = (
    " ; à l'essai, la file du juge est partie au régime prudent, imposé par la configuration "
    "sur décision de la session mère, alors que les deux sondes étaient « comprises » "
    "(rapport technique `7bb8cc95…`) : ce point relève du devis, non de ce texte, et le "
    "régime prudent est le plus strict (brouillon 46 ; vérification du brouillon 45, m-5)"
)
M7_LIGNE = (
    "| m-7 de la vérification du brouillon 45 — fichier des règles | **dit** : le fichier "
    "des règles du premier envoi cite toujours les lignes 529 à 537 et le brouillon 44, ce "
    "qui est juste par la règle 8 ; les mêmes règles sont désormais aux lignes 542 à 550 | 3.4 |"
)
VERIF45_INSCRITE = (
    " ; traitement : section 14.57 ; **vérification du brouillon 45** (faite) : brouillon "
    f"vérifié `{B45}`, `{B45_SHA}` ; rapport `{VERIF}`, `{VERIF_SHA}` ; vérificateur : agent "
    "neuf, Claude Opus 5.5 ; verdict « engageable après corrections », cinq corrections, "
    "neuf mineurs ; traitement : au brouillon 46, mot pour mot (statut) ; le brouillon 46 "
    "va à la contre-lecture 10"
)
C2_NEUF = (
    C2_TETE.replace("chaque service. Le reste",
                    "chaque service** (brouillons 40, 41 et 45 ; brouillon 46 : vérification "
                    "du brouillon 45, C-2). Le reste")
    + " " + sans_point_final(C2_MISTRAL[2:]) + " ; " + sans_point_final(C2_NEON[2:])
)
if C2_NEUF.count("chaque service**") != 1:
    arret("C-2 : tête non trouvée")

REMPLACEMENTS = [
    ("titre", "— v2, BROUILLON 45\n", "— v2, BROUILLON 46\n"),
    ("statut et histoire ; information pour Lazar",
     "**Statut : brouillon 45, non exécutable.** Le brouillon 45, d'un rédacteur neuf",
     HISTOIRE),
    ("m-2 (a)", "Il ne modifie ni les brouillons 1 à 41,",
     "Il ne modifie ni les brouillons " + M2_A + ","),
    ("m-2 (b)", "inscrite comme contre-lecture 9 (R2 ;",
     "inscrite comme contre-lecture 9 " + M2_B + " (R2 ;"),
    ("C-5, ligne 9",
     "versée par la session, qui en inscrit le chemin et l'empreinte (brouillon 45 :",
     "versée par la session (" + C5_L9 + " ; brouillon 45 :"),
    ("m-3", "vérification du brouillon 44, mineurs m-1 à m-8)",
     "vérification du brouillon 44, mineurs " + M3 + ")"),
    ("C-1, m-6 et m-5, point (3)",
     "(brouillon 45 ; vérification du brouillon 44, m-2 : sous la décision de la session "
     "principale du 21 novembre 2026, sous GO-2026-11-21-69, la sortie maximale de Google est "
     "65 536 au niveau de réflexion gardé, et la sonde est exemptée, exemption confirmée par "
     "GO-2026-11-22-03 ; la fiche des faits relève pourtant, aux deux vérifications du 22 "
     "novembre, une sonde de borne « comprise » sur chaque clé, ce que ce brouillon rapporte "
     "sans le trancher ; l'avenant qui porte l'exemption n'est pas cité, son chemin et son "
     "empreinte n'étant pas donnés au rédacteur)",
     sans_point_final(C1) + M5),
    ("C-3, ligne 551",
     "dans chaque file du juge à la course, les appels partent dans l'ordre de ses items ;",
     sans_point_final(C3) + " ;"),
    ("C-4, case « familles »", ", ce qui est dit ici sans être tranché)", C4_QUEUE),
    ("C-2, case « lecteurs et juge des ancres »",
     "reste À REMPLIR, pour ce que la fiche ne donne pas : la sortie maximale du second lecteur "
     "à la course (règle 7), le compte des réponses étayées et le coût projeté de chacun, les "
     "champs exacts de chaque service** (brouillons 40, 41 et 45)",
     C2_NEUF),
    ("C-3, ligne 1483",
     "le même partage par rang qu'à l'essai d'admission — rangs impairs",
     "le même partage par rang qu'à l'essai d'admission " + C3_1483 + " — rangs impairs"),
    ("m-4",
     "sans outil ni fichier ; aucune fiche n'est ajoutée ; aucune règle, aucun seuil, aucune "
     "issue ni aucune prédiction ne change)",
     "sans outil ni fichier ; " + M4 + " ; aucune règle, aucun seuil, aucune issue ni aucune "
     "prédiction ne change)"),
    ("C-1, ligne m-2 de 14.57",
     "**ajouté** au point (3) ; la fiche relève une sonde « comprise » sur chaque clé, rapporté "
     "sans être tranché ; l'avenant qui porte l'exemption n'est pas cité, faute de chemin et "
     "d'empreinte",
     C1_M2),
    ("m-7, ligne neuve de 14.57",
     "| 13.1, cases « module » et « familles » ; 13.2, case du lanceur |\n\n## Contre-lecture",
     "| 13.1, cases « module » et « familles » ; 13.2, case du lanceur |\n" + M7_LIGNE +
     "\n\n## Contre-lecture"),
    ("histoire, contre-lecture 10",
     "le mandat du rédacteur du brouillon 45.\n- **Contre-lecture 11**",
     "le mandat du rédacteur du brouillon 45. **Ajouté au brouillon 46** : la vérification "
     "du brouillon 45.\n- **Contre-lecture 11**"),
    ("C-5, ligne 2541 (vérification du 44)",
     "le chemin et l'empreinte du rapport entier, son auteur et son verdict sont à inscrire "
     "par la session",
     C5_L2541),
    ("C-5, ligne 2541 (vérification du 45) ; histoire",
     " ; traitement : section 14.57 ; le brouillon 45 va à la contre-lecture 10",
     VERIF45_INSCRITE),
]

t46 = t45
for nom, ancien, neuf in REMPLACEMENTS:
    n = t46.count(ancien)
    if n != 1:
        arret(f"{nom} : ancien trouvé {n} fois")
    t46 = t46.replace(ancien, neuf)
    print(f"porté : {nom}")

l45, l46 = t45.split("\n"), t46.split("\n")
if l45[541:550] != l46[541:550]:
    arret("les huit règles ont bougé")
if hashlib.sha256("\n".join(l46[541:550]).encode()).hexdigest() != REGLES_SHA:
    arret("empreinte des huit règles")
for marque in ("⟦", "⟧"):
    if marque in t46:
        arret("marque " + marque)

sortie = RACINE / B46
if sortie.exists():
    arret(f"{B46} existe déjà (R12)")
sortie.write_text(t46, encoding="utf-8")
print("écrit", B46, hashlib.sha256(t46.encode()).hexdigest())

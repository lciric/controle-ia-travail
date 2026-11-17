"""Brouillon 2 du préenregistrement du crible (ii) : application des corrections du tour 1 de contre-lecture.

Couples « ancien → nouveau » : les 42 couples D1.1 à D5.1 et m1.1 à m5.1 sont lus dans le rapport de contre-lecture
lui-même (blocs « Dk.j — ancien : » et « nouveau : » entre clôtures de trois accents graves), plus un écart déclaré (D4.1 :
accord de « seul » en « seuls », l'« ancien » allongé des deux mots qui le précèdent) et les couples propres à l'en-tête et
à la section « Contre-lecture ». Gardes : empreinte de la pièce de départ et du rapport ; 42 couples exactement, dans
l'ordre du rapport ; chaque « ancien » figure exactement une fois dans la pièce de départ ; aucun chevauchement entre
« anciens » ; chaque « nouveau » présent dans la cible ; la cible, son différentiel (et leurs compagnons) ne doivent pas
exister ; aucun repli silencieux. Bibliothèque standard seule ; aucun appel, aucune donnée.
Usage : python3 -I appliquer-corrections-crible-ii-brouillon2.py  (depuis n'importe quel dossier)
"""
import difflib
import hashlib
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ICI, "crible-ii-brouillon1.md")
SOURCE_SHA = "816a072f6c9192049f325661e7b0ea2f0530dc1f738c4c39b8e75fba62364609"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-ii-tour1-v1.md")
RAPPORT_SHA = "72f98c9ed64f1ee267a40087a66efdceaa7425de903de1b676e8bda74af5365e"
CIBLE = os.path.join(ICI, "crible-ii-brouillon2.md")
DIFF = os.path.join(ICI, "diff-crible-ii-b1-vers-b2.txt")
NOM_PROGRAMME = "appliquer-corrections-crible-ii-brouillon2.py"


def arret(msg):
    sys.stderr.write("ARRÊT : " + msg + "\n")
    sys.exit(2)


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


for chemin, attendu in ((SOURCE, SOURCE_SHA), (RAPPORT, RAPPORT_SHA)):
    if sha(chemin) != attendu:
        arret(f"empreinte différente : {chemin}")
for chemin in (CIBLE, CIBLE + ".sha256", DIFF, DIFF + ".sha256"):
    if os.path.exists(chemin):
        arret(f"cible déjà présente, jamais écrasée : {chemin}")

source = open(SOURCE, encoding="utf-8").read()
rapport = open(RAPPORT, encoding="utf-8").read()

# 1. Couples du rapport.
MOTIF = re.compile(
    r"^((?:D|m)\d\.\d+) — ancien :\n\n```\n(.*?)\n```\n\nnouveau :\n\n```\n(.*?)\n```\n",
    re.M | re.S)
couples = [(m.group(1), m.group(2), m.group(3)) for m in MOTIF.finditer(rapport)]
noms = [c[0] for c in couples]
ATTENDUS = ([f"D1.{k}" for k in range(1, 31)] + ["D2.1", "D3.1", "D3.2", "D4.1", "D4.2", "D5.1"]
            + ["m1.1", "m2.1", "m3.1", "m3.2", "m4.1", "m5.1"])
if noms != ATTENDUS:
    arret(f"couples du rapport inattendus : {noms}")
if len(couples) != 42:
    arret(f"42 couples attendus, {len(couples)} lus")

# 2. Écart déclaré (section « Contre-lecture » de la pièce neuve) : accord grammatical seul.
ECARTS = {
    "D4.1": ("seul son\n", "seuls son\n"),
}
corriges = []
for nom, ancien, nouveau in couples:
    if nom in ECARTS:
        avant_ancien, avant_nouveau = ECARTS[nom]
        ancien, nouveau = avant_ancien + ancien, avant_nouveau + nouveau
    corriges.append((nom, ancien, nouveau))
couples = corriges

# 3. Couples propres : en-tête et section « Contre-lecture ».
heure = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], check=True, capture_output=True, text=True).stdout.strip()
if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", heure):
    arret(f"heure illisible : {heure!r}")

ANCIENNE_CL = source[source.index("## Contre-lecture\n\nAucune à ce jour"):source.index("## Annexe A — comptes exacts")]

NOUVELLE_CL = f"""## Contre-lecture

- **Contre-lecture 1** (R2, tour 1, sur le brouillon 1) — sous-agent neuf, d'un autre modèle que l'auteur, qui n'a écrit ni ce
  texte, ni [NOTE], ni [CRIBLE-III], ni [CRIBLE-V], ni [PILOTE]. Texte relu :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-ii-brouillon1.md`,
  `{SOURCE_SHA}` ; rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-ii-tour1-v1.md`,
  `{RAPPORT_SHA}`. Verdict : « corrections » (5 majeures, D1 à D5 ;
  5 mineures, m1 à m5 ; 42 couples ; second tour demandé sur ce brouillon 2). Corrections appliquées le {heure} (`date -u`)
  par un rédacteur neuf, d'un autre modèle que l'auteur, qui n'a écrit ni le brouillon 1 ni le rapport, au moyen du programme
  `{NOM_PROGRAMME}` (même dossier, scellé à côté ; différentiel `diff-crible-ii-b1-vers-b2.txt`, scellé) : les 42
  couples sont lus dans le rapport lui-même ; chaque « ancien » figure une seule fois dans le brouillon 1, sans chevauchement
  (vérifié par le programme). **Traitement**, point par point :
  - D1 (« P1 » et « P2 » nommaient à la fois des sessions et les deux comparaisons principales ; les comparaisons deviennent
    **SP** et **SQ**, les sessions gardent P1 à P4 ; couples D1.1 à D1.30) : **acceptée**, telle quelle.
  - D2 (lecture gelée « dispersion par le contenu » : cas d'un placebo qui égare, étage 6 de signe négatif ; couple D2.1) :
    **acceptée**, telle quelle.
  - D3 (cas non définis du placebo : aucun donneur à m_k cartes valides, ou texte de Q_k au-delà de 53 000 octets ; Q_k ne
    part pas, compté ; ligne d'arrêt neuve avec essai sain et artefact ; couples D3.1 et D3.2) : **acceptée**, telle quelle.
  - D4 (la pièce disait n'avoir lu que le témoin positif du pilote, alors que la section « Comptes » du verdict, lue, donne
    x = 0 sur 14 ; couples D4.1 et D4.2) : **acceptée**, avec **un écart déclaré** à D4.1 : l'« ancien » est allongé des deux
    mots qui le précèdent (« seul son »), écrits « seuls son », pour accorder « seul » avec ses deux sujets (« son témoin
    positif et le résultat principal sont lus ») ; aucun autre mot ne change.
  - D5 (option (b) du nœud de faisabilité chiffrée avec une valeur d'exemple de 3,10 ; plus haut plafond que l'enveloppe
    permet aux 120 appels des rangs 2 à 4 : 2,19, soit ≈ 101 000 octets servis ; couple D5.1) : **acceptée**, telle quelle ;
    la recommandation (a) du point 3 de « Choix et doutes » n'est pas changée (le rapport la laisse à la mère).
  - m1 (énoncé du test : 7 écarts non nuls nécessaires, suffisants s'ils sont tous du même signe ; la sortie de l'annexe A,
    imprimée par le programme, n'est pas changée) : **acceptée**.
  - m2 (les 52 000 octets sont dans la section « Devis » de [CRIBLE-III], non dans sa « Liste d'arrêt ») : **acceptée**.
  - m3 (zone utile définie aussi pour SQ ; les étages 1 et 3 n'arrêtent que la principale qu'ils touchent) : **acceptée**.
  - m4 (un même monde peut être donneur de plusieurs mondes : écarts de SQ non strictement indépendants, dit ; nombre de
    mondes servis par donneur rapporté) : **acceptée**.
  - m5 (le monde suivant d'une file part quand les six appels du monde en cours sont finis) : **acceptée**.
  - Remarques facultatives du rapport (section 5 : mot « brutes », annexe A, ligne de puissance à 16 mondes, légende des
    sigles) : **non appliquées**, aucune correction n'étant exigée ; à reprendre au tour suivant si la mère le veut.
  - **Non corrigé par le rapport, signalé sans rien changer** (à reprendre au tour 2) : la phrase du « Statut » « les
    prédictions sont écrites sans aucune donnée de proposeur sur la couverture », et celle de la section « Prédiction »
    « sans aucune donnée de couverture par appel », se lisent désormais à côté du résultat principal x = 0 sur 14 ajouté par
    D4 ; le titre de la section « Devis » garde la mention « brouillon 1 », qui nomme le devis et son programme, inchangés.
"""

PROPRES = [
    ("titre",
     "les cartes brutes des précédentes — brouillon 1 (variante « crédits de Claude au maximum »)\n",
     "les cartes brutes des précédentes — brouillon 2 (variante « crédits de Claude au maximum »)\n"),
    ("date",
     "  aucun appel de modèle, aucune machine, aucune dépense.\n",
     "  aucun appel de modèle, aucune machine, aucune dépense.\n"
     f"- Brouillon 2 : corrections du tour 1 de contre-lecture appliquées le {heure} (`date -u`, au scellement) par un\n"
     "  rédacteur neuf, d'un autre modèle que l'auteur, qui n'a écrit ni le brouillon 1 ni le rapport de contre-lecture\n"
     f"  (identité dite en conversation seulement), au moyen du programme `{NOM_PROGRAMME}` (même dossier,\n"
     "  scellé) ; dépôt lu sur `main` (tête `5a01b434`) ; aucune branche lue ; aucun commit, aucune poussée, aucun appel de\n"
     "  modèle, aucune machine, aucune dépense. Rien d'autre que les corrections, l'en-tête et la section « Contre-lecture »\n"
     "  ne change.\n"),
    ("statut",
     "**Statut.** **Brouillon 1**, non contre-lu, scellé comme pièce (empreinte compagnon, R6), non comme préenregistrement en\nvigueur.",
     "**Statut.** **Brouillon 2**, contre-lu une fois (tour 1, corrections appliquées, section « Contre-lecture »), scellé comme\n"
     "pièce (empreinte compagnon, R6), non comme préenregistrement en vigueur ; second tour de contre-lecture à faire."),
    ("validateur",
     "Validateur `controle_ia.prereg.problemes` : un seul défaut, attendu pour un brouillon non contre-lu (« section Contre-lecture\n"
     "sans les deux empreintes exigées »).\n",
     "Validateur `controle_ia.prereg.problemes` : aucun défaut sur ce brouillon 2 (vérifié avant son scellement comme pièce de\n"
     "travail).\n"),
    ("contre-lecture", ANCIENNE_CL, NOUVELLE_CL),
]

tous = couples + PROPRES

# 4. Chaque « ancien » une seule fois dans la pièce de départ ; aucun chevauchement.
places = []
for nom, ancien, nouveau in tous:
    n = source.count(ancien)
    if n != 1:
        arret(f"{nom} : « ancien » trouvé {n} fois (une seule attendue)")
    debut = source.index(ancien)
    places.append((debut, debut + len(ancien), nom, nouveau))
places.sort()
for (d1, f1, n1, _), (d2, f2, n2, _) in zip(places, places[1:]):
    if d2 < f1:
        arret(f"chevauchement entre {n1} et {n2}")

# 5. Application par positions dans la pièce de départ.
morceaux, curseur = [], 0
for debut, fin, nom, nouveau in places:
    morceaux.append(source[curseur:debut])
    morceaux.append(nouveau)
    curseur = fin
morceaux.append(source[curseur:])
cible = "".join(morceaux)

for nom, ancien, nouveau in tous:
    if nouveau not in cible:
        arret(f"{nom} : « nouveau » absent de la cible")

with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(cible)
diff = difflib.unified_diff(source.splitlines(keepends=True), cible.splitlines(keepends=True),
                            fromfile="crible-ii-brouillon1.md", tofile="crible-ii-brouillon2.md")
with open(DIFF, "x", encoding="utf-8") as f:
    f.writelines(diff)
print(f"cible écrite : {CIBLE}")
print(f"différentiel écrit : {DIFF}")
print(f"heure (date -u) : {heure}")
print(f"couples appliqués : {len(tous)} ({len(couples)} du rapport, {len(PROPRES)} propres) : "
      + ", ".join(n for _, _, n, _ in places))
print(f"empreinte de la cible : {sha(CIBLE)}")

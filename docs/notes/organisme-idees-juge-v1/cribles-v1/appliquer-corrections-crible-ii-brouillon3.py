"""Brouillon 3 du préenregistrement du crible (ii) : application des corrections du tour 2 de contre-lecture.

Couples « ancien → nouveau » : les 4 couples m1.1, m1.2, m2.1 et m3.1 sont lus dans le rapport du tour 2 lui-même (blocs
« mk.j — ancien : » et « nouveau : » entre clôtures de trois accents graves) et appliqués tels quels, sans écart ; plus les
couples propres au titre, à l'en-tête (entrée « Brouillon 3 »), au « Statut », à la ligne du validateur et à la section
« Contre-lecture » (entrée « Contre-lecture 2 » ; ligne vide rétablie avant le titre de l'annexe A, perdue au brouillon 2).
Gardes : empreintes de la pièce de départ, du rapport et du validateur du dépôt ; branche `main` ; 4 couples exactement, dans
l'ordre du rapport, et aucun autre bloc « — ancien : » dans le rapport ; chaque « ancien » figure exactement une fois dans la
pièce de départ (occurrences chevauchantes comprises) ; aucun chevauchement entre « anciens » ; chaque « nouveau » présent
dans la cible ; longueur de la cible égale à celle attendue ; validateur `controle_ia.prereg.problemes` sans défaut sur le
texte exact de la cible, avant son écriture (copie dans un dossier temporaire) puis sur la cible écrite ; la cible, son
différentiel et leurs compagnons ne doivent pas exister (écriture en mode « x ») ; aucun repli silencieux. Bibliothèque
standard et validateur du dépôt (lui-même en bibliothèque standard) ; aucun appel, aucune donnée, aucun réseau ; aucun
fichier de code compilé écrit.
Usage : TMPDIR=<dossier de travail> python3 -I appliquer-corrections-crible-ii-brouillon3.py [--essai DOSSIER]
  (depuis n'importe quel dossier ; avec --essai, la cible et le différentiel vont dans DOSSIER, qui doit être hors du dépôt)
"""
import difflib
import hashlib
import os
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
CHEMIN_PIECES = "docs/notes/organisme-idees-juge-v1/cribles-v1/"
NOM_SOURCE = "crible-ii-brouillon2.md"
NOM_RAPPORT = "contre-lecture-crible-ii-tour2-v1.md"
NOM_CIBLE = "crible-ii-brouillon3.md"
NOM_DIFF = "diff-crible-ii-b2-vers-b3.txt"
NOM_PROGRAMME = "appliquer-corrections-crible-ii-brouillon3.py"
SOURCE = os.path.join(ICI, NOM_SOURCE)
SOURCE_SHA = "fff278795f3ee4ba8a4f332bb80d687d7e2e773b55ebde2cabeae0e3912b7769"
RAPPORT = os.path.join(ICI, NOM_RAPPORT)
RAPPORT_SHA = "ba2ecf66c6994cf8549fd8f12d554e8de82bea59f04bb45b680b1f371c9e6a71"
VALIDATEUR = os.path.join(DEPOT, "src", "controle_ia", "prereg.py")
VALIDATEUR_SHA = "3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306"


def arret(msg):
    sys.stderr.write("ARRÊT : " + msg + "\n")
    sys.exit(2)


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def commande(*args):
    return subprocess.run(list(args), check=True, capture_output=True, text=True).stdout.strip()


def occurrences(texte, motif):
    """Nombre d'occurrences, chevauchantes comprises."""
    return sum(1 for _ in re.finditer("(?=" + re.escape(motif) + ")", texte))


# 0. Arguments, empreintes, cibles absentes, branche, tête, heure.
if len(sys.argv) == 1:
    SORTIE = ICI
elif len(sys.argv) == 3 and sys.argv[1] == "--essai":
    SORTIE = os.path.abspath(sys.argv[2])
    if SORTIE == DEPOT or SORTIE.startswith(DEPOT + os.sep):
        arret(f"--essai : dossier dans le dépôt, refusé : {SORTIE}")
    if not os.path.isdir(SORTIE):
        arret(f"--essai : dossier absent : {SORTIE}")
else:
    arret(f"usage : {NOM_PROGRAMME} [--essai DOSSIER]")
CIBLE = os.path.join(SORTIE, NOM_CIBLE)
DIFF = os.path.join(SORTIE, NOM_DIFF)

for chemin, attendu in ((SOURCE, SOURCE_SHA), (RAPPORT, RAPPORT_SHA), (VALIDATEUR, VALIDATEUR_SHA)):
    if sha(chemin) != attendu:
        arret(f"empreinte différente : {chemin}")
for chemin in (CIBLE, CIBLE + ".sha256", DIFF, DIFF + ".sha256"):
    if os.path.exists(chemin):
        arret(f"cible déjà présente, jamais écrasée : {chemin}")
branche = commande("git", "-C", DEPOT, "rev-parse", "--abbrev-ref", "HEAD")
if branche != "main":
    arret(f"branche {branche!r} ; `main` attendue")
tete = commande("git", "-C", DEPOT, "rev-parse", "--short=8", "HEAD")
if not re.fullmatch(r"[0-9a-f]{8}", tete):
    arret(f"tête illisible : {tete!r}")
heure = commande("date", "-u", "+%Y-%m-%dT%H:%M:%SZ")
if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", heure):
    arret(f"heure illisible : {heure!r}")

sys.path.insert(0, os.path.join(DEPOT, "src"))
import controle_ia.prereg as validateur  # noqa: E402  (empreinte vérifiée ci-dessus)

if os.path.abspath(validateur.__file__) != VALIDATEUR:
    arret(f"validateur importé d'ailleurs : {validateur.__file__}")

with open(SOURCE, encoding="utf-8") as f:
    source = f.read()
with open(RAPPORT, encoding="utf-8") as f:
    rapport = f.read()

# 1. Couples du rapport du tour 2 (section 4), appliqués tels quels.
MOTIF = re.compile(r"^(m\d\.\d+) — ancien :\n```\n(.*?)\n```\nnouveau :\n```\n(.*?)\n```\n", re.M | re.S)
couples = [(m.group(1), m.group(2), m.group(3)) for m in MOTIF.finditer(rapport)]
noms = [c[0] for c in couples]
if noms != ["m1.1", "m1.2", "m2.1", "m3.1"]:
    arret(f"couples du rapport inattendus : {noms}")
if rapport.count("— ancien :") != len(couples):
    arret("un bloc « — ancien : » du rapport échappe au motif")

# 2. Couples propres : titre, en-tête, « Statut », ligne du validateur, section « Contre-lecture ».
ENTREE_BROUILLON_3 = (
    f"- Brouillon 3 : corrections du tour 2 de contre-lecture appliquées le {heure} (`date -u`, au scellement) par un\n"
    "  rédacteur neuf, d'un autre modèle que l'auteur (« modèle C » de cette pièce, comme le lecteur du tour 2), qui n'a écrit ni\n"
    "  le brouillon 1, ni le brouillon 2, ni aucun rapport de contre-lecture (identité dite en conversation seulement), au moyen du\n"
    f"  programme `{NOM_PROGRAMME}` (même dossier, scellé) ; dépôt lu sur `main` (tête `{tete}`) ;\n"
    "  aucune branche lue ; aucun commit, aucune poussée, aucun appel de modèle, aucune machine, aucune dépense. Rien d'autre que\n"
    "  les quatre couples du tour 2 (m1.1, m1.2, m2.1, m3.1), le titre, cette entrée de l'en-tête, le « Statut », la ligne du\n"
    "  validateur et la section « Contre-lecture » (entrée « Contre-lecture 2 » ajoutée ; ligne vide rétablie avant le titre de\n"
    "  l'annexe A) ne change.\n"
)

ENTREE_CL2 = (
    "- **Contre-lecture 2** (R2, tour 2, sur le brouillon 2) — sous-agent neuf, d'un autre modèle que l'auteur (« modèle C » de\n"
    "  cette pièce), qui n'a écrit aucune des pièces qu'il a lues (les brouillons 2 et 1, le rapport du tour 1, le verdict v2 du\n"
    "  pilote en partie, le différentiel et le programme du brouillon 2). Texte relu :\n"
    f"  `{CHEMIN_PIECES}{NOM_SOURCE}`,\n"
    f"  `{SOURCE_SHA}` ; rapport :\n"
    f"  `{CHEMIN_PIECES}{NOM_RAPPORT}`,\n"
    f"  `{RAPPORT_SHA}`. Verdict : « corrections » (aucune majeure ;\n"
    "  3 mineures, m1 à m3, toutes de formulation ; 4 couples) ; les 42 corrections du tour 1 sont jugées appliquées fidèlement\n"
    f"  et l'écart déclaré à D4.1, légitime. Corrections appliquées le {heure} (`date -u`) par un rédacteur neuf, d'un autre\n"
    "  modèle que l'auteur (« modèle C », comme le lecteur), qui n'a écrit ni le brouillon 1, ni le brouillon 2, ni aucun rapport,\n"
    f"  au moyen du programme `{NOM_PROGRAMME}` (même dossier, scellé à côté ; différentiel\n"
    f"  `{NOM_DIFF}`, scellé) : les 4 couples sont lus dans le rapport lui-même et appliqués tels quels ;\n"
    "  chaque « ancien » figure une seule fois dans le brouillon 2, sans chevauchement (vérifié par le programme). **Traitement**,\n"
    "  point par point :\n"
    "  - m1 (« aucune donnée » de couverture, dans le « Statut » et dans la section « Prédiction », à côté du résultat principal\n"
    "    x = 0 sur 14, qui est une donnée de couverture par appel d'une classe, celle des conditionnelles ; couples m1.1 et\n"
    "    m1.2) : **acceptée**, telle quelle ; elle règle le premier des deux points que l'entrée « Contre-lecture 1 » signalait\n"
    "    sans les corriger (le second, le titre de la section « Devis », est la remarque facultative (1) ci-dessous).\n"
    "  - m2 (après D3.1, la parenthèse de la réserve « placebo mal apparié » suivait « la chaîne de S continue » et semblait\n"
    "    couvrir le cas « aucun donneur », alors qu'elle se rapporte au repli sur la longueur la plus proche, la réserve étant\n"
    "    définie par l'écart de longueur, section « Seuil » ; couple m2.1) : **acceptée**, telle quelle.\n"
    "  - m3 (l'entrée « Brouillon 2 » de l'en-tête disait « rien d'autre » sans nommer le « Statut », la ligne du validateur ni\n"
    "    l'accord « seuls son » de D4.1 ; couple m3.1) : **acceptée**, telle quelle ; l'entrée « Brouillon 3 » de l'en-tête\n"
    "    nomme d'emblée tout ce que ce brouillon change.\n"
    "  - Remarques facultatives (section 5 du rapport) : (1) le titre de la section « Devis » garde « brouillon 1 », qui nomme le\n"
    "    devis et son programme, inchangés : rien à faire, rien de changé ; (2) les remarques facultatives du tour 1 restent non\n"
    "    appliquées, aucune correction n'étant exigée ; (3) la citation du tour 2 dans un brouillon 3 est faite par la présente\n"
    "    entrée.\n"
    "  - Points « Pour la session mère » (section 6 du rapport : nœud de faisabilité, écarts à la note, marge de l'enveloppe,\n"
    "    valeur de l'essai, compte rendu de l'auteur hors pièce, solde de crédits) : hors de la pièce, **aucun changement** ici ;\n"
    "    ils restent à la mère ou à Lazar.\n"
    "  - Mise en forme : une ligne vide est rétablie entre la fin de cette section et le titre de l'annexe A (perdue au\n"
    "    brouillon 2) ; aucun mot ne change.\n"
)

FIN_CL1 = ("    D4 ; le titre de la section « Devis » garde la mention « brouillon 1 », qui nomme le devis et son programme, "
           "inchangés.\n")

PROPRES = [
    ("titre",
     "les cartes brutes des précédentes — brouillon 2 (variante « crédits de Claude au maximum »)\n",
     "les cartes brutes des précédentes — brouillon 3 (variante « crédits de Claude au maximum »)\n"),
    ("en-tête",
     "\n- Nombres neufs : `devis-crible-ii-brouillon1.py`",
     "\n" + ENTREE_BROUILLON_3 + "- Nombres neufs : `devis-crible-ii-brouillon1.py`"),
    ("statut",
     "**Statut.** **Brouillon 2**, contre-lu une fois (tour 1, corrections appliquées, section « Contre-lecture »), scellé comme\n"
     "pièce (empreinte compagnon, R6), non comme préenregistrement en vigueur ; second tour de contre-lecture à faire.",
     "**Statut.** **Brouillon 3**, contre-lu deux fois (tours 1 et 2, corrections appliquées, section « Contre-lecture »), scellé"
     " comme\npièce (empreinte compagnon, R6), non comme préenregistrement en vigueur ; troisième tour de contre-lecture à la"
     " décision de la mère."),
    ("validateur",
     "Validateur `controle_ia.prereg.problemes` : aucun défaut sur ce brouillon 2 (vérifié avant son scellement comme pièce de\n"
     "travail).\n",
     "Validateur `controle_ia.prereg.problemes` : aucun défaut sur ce brouillon 3 (vérifié avant son scellement comme pièce de\n"
     "travail).\n"),
    ("contre-lecture",
     FIN_CL1 + "## Annexe A — comptes exacts",
     FIN_CL1 + ENTREE_CL2 + "\n## Annexe A — comptes exacts"),
]

tous = couples + PROPRES

# 3. Chaque « ancien » une seule fois dans la pièce de départ ; aucun chevauchement.
places = []
for nom, ancien, nouveau in tous:
    n = occurrences(source, ancien)
    if n != 1:
        arret(f"{nom} : « ancien » trouvé {n} fois (une seule attendue)")
    debut = source.index(ancien)
    places.append((debut, debut + len(ancien), nom, nouveau))
places.sort()
for (d1, f1, n1, _), (d2, f2, n2, _) in zip(places, places[1:]):
    if d2 < f1:
        arret(f"chevauchement entre {n1} et {n2}")

# 4. Application par positions dans la pièce de départ.
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
attendue = len(source) + sum(len(nouveau) - len(ancien) for _, ancien, nouveau in tous)
if len(cible) != attendue:
    arret(f"longueur de la cible {len(cible)}, {attendue} attendue")

# 5. Validateur du dépôt sur le texte exact, avant toute écriture dans la sortie.
with tempfile.TemporaryDirectory(prefix="essai-crible-ii-b3-") as dossier:
    essai = os.path.join(dossier, NOM_CIBLE)
    with open(essai, "x", encoding="utf-8") as f:
        f.write(cible)
    defauts = validateur.problemes(essai)
if defauts:
    arret("validateur, avant écriture : " + " ; ".join(defauts))

# 6. Écriture (jamais d'écrasement), différentiel, contrôles après écriture.
with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(cible)
diff = difflib.unified_diff(source.splitlines(keepends=True), cible.splitlines(keepends=True),
                            fromfile=NOM_SOURCE, tofile=NOM_CIBLE)
with open(DIFF, "x", encoding="utf-8") as f:
    f.writelines(diff)
with open(CIBLE, encoding="utf-8") as f:
    if f.read() != cible:
        arret("cible relue différente du texte calculé")
defauts = validateur.problemes(CIBLE)
if defauts:
    arret("validateur, sur la cible écrite : " + " ; ".join(defauts))

print(f"cible écrite : {CIBLE}")
print(f"différentiel écrit : {DIFF}")
print(f"heure (date -u) : {heure} ; branche {branche}, tête {tete}")
print(f"couples appliqués : {len(tous)} ({len(couples)} du rapport, {len(PROPRES)} propres), dans l'ordre de la pièce : "
      + ", ".join(n for _, _, n, _ in places))
print("validateur : aucun défaut (avant écriture et sur la cible écrite)")
print(f"empreinte de la cible : {sha(CIBLE)}")

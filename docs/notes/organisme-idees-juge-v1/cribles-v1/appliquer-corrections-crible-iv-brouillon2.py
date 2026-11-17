"""Brouillon 2 du préenregistrement du crible (iv) : application des corrections du tour 1 de contre-lecture.

Couples « ancien → nouveau » : les 6 couples M1.1, M2.1, M2.2, M3.1, m1.1 et m2.1 sont lus dans le rapport de
contre-lecture lui-même (blocs « Xk.j — ancien : » et « nouveau : » entre clôtures de trois accents graves), tels quels,
plus les couples propres à l'en-tête (titre, ligne du brouillon 2, statut, validateur) et à la section « Contre-lecture ».
Gardes : empreinte de la pièce de départ et du rapport ; 6 couples exactement, dans l'ordre du rapport ; chaque « ancien »
figure exactement une fois dans la pièce de départ ; aucun chevauchement entre « anciens » ; chaque « nouveau » présent
dans la cible ; la cible, son différentiel (et leurs compagnons) ne doivent pas exister ; aucun repli silencieux.
Bibliothèque standard seule ; aucun appel, aucune donnée.
Usage : python3 -I appliquer-corrections-crible-iv-brouillon2.py               (écrit la cible et le différentiel)
        python3 -I appliquer-corrections-crible-iv-brouillon2.py --essai DOSSIER (écrit la seule cible dans DOSSIER, essai)
"""
import difflib
import hashlib
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ICI, "crible-iv-brouillon1.md")
SOURCE_SHA = "079f8599d6d78546148d89adb43227b74feae461ee0fdc4a3f3002c8c5f69f53"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-iv-tour1-v1.md")
RAPPORT_SHA = "e7853abe0bf6f5177307fa20af8f14d7fa06ed06bb83bc6320908a826f0e573e"
CIBLE = os.path.join(ICI, "crible-iv-brouillon2.md")
DIFF = os.path.join(ICI, "diff-crible-iv-b1-vers-b2.txt")
NOM_PROGRAMME = "appliquer-corrections-crible-iv-brouillon2.py"
NOM_DIFF = "diff-crible-iv-b1-vers-b2.txt"


def arret(msg):
    sys.stderr.write("ARRÊT : " + msg + "\n")
    sys.exit(2)


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


ESSAI = None
if len(sys.argv) == 3 and sys.argv[1] == "--essai":
    ESSAI = os.path.abspath(sys.argv[2])
    if not os.path.isdir(ESSAI):
        arret(f"dossier d'essai absent : {ESSAI}")
    if os.path.commonpath([ESSAI, ICI]) == ICI:
        arret("le dossier d'essai ne doit pas être le dossier des pièces")
elif len(sys.argv) != 1:
    arret("usage : sans argument, ou --essai DOSSIER")

for chemin, attendu in ((SOURCE, SOURCE_SHA), (RAPPORT, RAPPORT_SHA)):
    if sha(chemin) != attendu:
        arret(f"empreinte différente : {chemin}")
for chemin in (CIBLE, CIBLE + ".sha256", DIFF, DIFF + ".sha256"):
    if os.path.exists(chemin):
        arret(f"cible déjà présente, jamais écrasée : {chemin}")

source = open(SOURCE, encoding="utf-8").read()
rapport = open(RAPPORT, encoding="utf-8").read()

# 1. Couples du rapport, tels quels (aucun écart).
MOTIF = re.compile(
    r"^((?:M|m)\d\.\d+) — ancien :\n\n```\n(.*?)\n```\n\nnouveau :\n\n```\n(.*?)\n```\n",
    re.M | re.S)
couples = [(m.group(1), m.group(2), m.group(3)) for m in MOTIF.finditer(rapport)]
noms = [c[0] for c in couples]
ATTENDUS = ["M1.1", "M2.1", "M2.2", "M3.1", "m1.1", "m2.1"]
if noms != ATTENDUS:
    arret(f"couples du rapport inattendus : {noms}")
if rapport.count(" — ancien :") != len(ATTENDUS):
    arret("le rapport porte un bloc « ancien » non lu par le motif")

# 2. Couples propres : en-tête et section « Contre-lecture ».
heure = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], check=True, capture_output=True, text=True).stdout.strip()
if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", heure):
    arret(f"heure illisible : {heure!r}")

DEBUT_CL = "## Contre-lecture\n\nAucune à ce jour"
FIN_CL = "## Annexe A — comptes exacts"
if source.count(DEBUT_CL) != 1 or source.count(FIN_CL) != 1:
    arret("bornes de la section « Contre-lecture » introuvables ou multiples")
ANCIENNE_CL = source[source.index(DEBUT_CL):source.index(FIN_CL)]

NOUVELLE_CL = f"""## Contre-lecture

- **Contre-lecture 1** (R2, tour 1, sur le brouillon 1) — sous-agent neuf, d'un autre modèle que le rédacteur, qui n'a écrit ni
  ce texte, ni [NOTE], ni [CRIBLE-II], ni [CRIBLE-III], ni [CRIBLE-V], ni [PILOTE], ni [MR2]. Texte relu :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iv-brouillon1.md`,
  `{SOURCE_SHA}` ; rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-iv-tour1-v1.md`,
  `{RAPPORT_SHA}`. Verdict : « corrections » (3 majeures, M1 à M3 ;
  2 mineures, m1 et m2 ; 6 couples ; second tour demandé sur ce brouillon 2). Corrections appliquées le {heure} (`date -u`)
  par un rédacteur neuf, d'un autre modèle que le rédacteur du brouillon 1, qui n'a écrit ni le brouillon 1 ni le rapport, au
  moyen du programme `{NOM_PROGRAMME}` (même dossier, scellé à côté ; différentiel `{NOM_DIFF}`, scellé) :
  les 6 couples sont lus dans le rapport lui-même ; chaque « ancien » figure une seule fois dans le brouillon 1, sans
  chevauchement (vérifié par le programme). **Traitement**, point par point :
  - M1 (bras 3 : ordre de 2a' et 2b' non écrit, garde qui pouvait jouer autrement qu'au bras 2 ; 2a' puis 2b' joués l'un après
    l'autre, garde jugée avant chacun ; couple M1.1) : **acceptée**, telle quelle. Le chemin du bras 3 reste plus court que celui
    du bras 2 : les durées du devis ne changent pas (le rapport le dit).
  - M2 (lecture gelée : « moins » était qualifié par la dépense, « davantage » ne l'était pas ; ρ_21 accompagne toujours les deux
    phrases tranchées de l'étage 4, et « à dollars égaux » devient « à dollars proches, ρ_21 dit » dans la traduction ; couples
    M2.1 et M2.2) : **acceptée**, telle quelle.
  - M3 (traduction gelée : « étage 4 moins et étage 5 compte » tombait sous deux points, et « incohérente » n'était pas juste ;
    les deux couples de signes contraires deviennent une « lecture croisée », l'ordre des trois bras et δ_31 rapportés sans
    conclusion sur H-iv ; couple M3.1) : **acceptée**, telle quelle.
  - m1 (m = 48 fixe garde le seuil par carte, non le budget d'erreur du juge par génération ; couple m1.1) : **acceptée**, telle
    quelle.
  - m2 (les bras 2 et 3 partagent les cartes de 1a, non leurs retenues ; couple m2.1) : **acceptée**, telle quelle.
  - Remarques facultatives du rapport (section 5 : sonde et seuil des deux tiers, profondeur informative pour le seul bras 2,
    sigle « e-BH », statut) et points « Pour la session mère » (section 6) : **non appliqués**, aucune correction n'étant
    exigée ; à la mère et au tour suivant.
  - **Non corrigé par le rapport, signalé sans rien changer** (à reprendre au tour 2) : après M2, la formule « à dollars égaux »
    reste ailleurs dans le texte sans ρ_21 : au § 0, points 1 et 7 ; dans l'énoncé de H-iv ; dans la prédiction IV-1 ; dans
    « Ce que serait chaque issue » (« à dollars égaux, payer deux fois l'entrée ») ; et à l'étage 2 du tableau des critères gelés,
    dont le complément exigé reste « à dollars égaux, avec une génération 2 amputée dans k mondes » ; le titre de la section
    « Devis » garde la mention « brouillon 1 », qui nomme le devis et son programme, inchangés.
- **Tour 2 à faire** (R2) : sur ce brouillon 2, par un sous-agent neuf d'un **autre modèle** que le rédacteur du brouillon 1, qui
  n'a écrit ni ce texte, ni le rapport du tour 1, ni [NOTE], ni [CRIBLE-II], ni [CRIBLE-III], ni [CRIBLE-V], ni [PILOTE], ni
  [MR2]. **Fichiers à lui donner explicitement** : ce texte ; le brouillon 1 et le rapport du tour 1 (empreintes ci-dessus) ;
  `{NOM_PROGRAMME}` et `{NOM_DIFF}` (même dossier) ; puis la liste
  du brouillon 1, inchangée : `devis-crible-iv-brouillon1.py` et sa sortie (même dossier) ; [NOTE] (`2f6a69dd…`), § 1, § 2,
  § 3 (iv), § 4, § 6, § 7 et annexe A ; [RELEVÉ] (`bd253b6c…`), § 2.1, § 4.1, § 5, § 6 ; [VERDICT-PC] (`e64458e8…`, branche
  `verdict/pilote-mr2-v74-v14-v1`) ; [CRIBLE-II] (`816a072f…`) en entier ; [CRIBLE-III] (`91b4bf30…`), « Métrique », « Liste
  d'arrêt », « Devis » ; [CRIBLE-V] (`2b99627d…`), table des proposeurs et « Devis » ; [MR2] (`47e38ec0…`), § 2 à 4 ;
  `monde_riche_v4.py` (`4b165847…`), fonctions `tirer_gabarit_v4`, `generer_monde_v4`, `generer_v4`, `course` ;
  `monde_riche_outils_v1.py` (`1825b956…`), fonctions `juger`, `e_bh`, `test_de_mort` ; N-045 v2 (`c7b05e39…`), point 5 ; N-058
  (`854f2724…`) ; R-1779 ; la ligne GO-2026-11-15-06. **À trancher en priorité** : celles du brouillon 1 (la garde, point 3 ; m
  dans la chaîne en tours, point 5 ; la part au lieu des plafonds, point 7 ; l'appel commun ; le générateur à chaîne ; la
  traduction de la question de [NOTE] en étages ; la règle d'abandon ; les treize choix), plus les lectures gelées touchées par
  M2 et M3 et les points signalés ci-dessus.

"""

PROPRES = [
    ("titre",
     "milieu de chaque génération — brouillon 1 (variante « crédits de Claude au maximum »)\n",
     "milieu de chaque génération — brouillon 2 (variante « crédits de Claude au maximum »)\n"),
    ("date",
     "  appel de modèle, aucune machine, aucune dépense, aucun monde tiré.\n",
     "  appel de modèle, aucune machine, aucune dépense, aucun monde tiré.\n"
     f"- Brouillon 2 : corrections du tour 1 de contre-lecture appliquées le {heure} (`date -u`, au scellement) par un\n"
     "  rédacteur neuf, d'un autre modèle que le rédacteur du brouillon 1, qui n'a écrit ni le brouillon 1 ni le rapport de\n"
     "  contre-lecture (identité dite en conversation seulement), au moyen du programme\n"
     f"  `{NOM_PROGRAMME}` (même dossier, scellé) ; dépôt lu sur `main` (tête `1df4ae9f`) ;\n"
     "  aucune branche lue ; aucun commit, aucune poussée, aucun appel de modèle, aucune machine, aucune dépense, aucun monde\n"
     "  tiré. Rien d'autre que les corrections, l'en-tête et la section « Contre-lecture » ne change.\n"),
    ("statut",
     "**Statut.** **Brouillon 1**, non contre-lu, scellé comme pièce (empreinte compagnon, R6), non comme préenregistrement en\nvigueur.",
     "**Statut.** **Brouillon 2**, contre-lu une fois (tour 1, corrections appliquées, section « Contre-lecture »), scellé comme\n"
     "pièce (empreinte compagnon, R6), non comme préenregistrement en vigueur ; second tour de contre-lecture à faire\n"
     "(R2)."),
    ("validateur",
     "Validateur `controle_ia.prereg.problemes` : un seul défaut, attendu pour un brouillon non contre-lu (« section Contre-lecture\n"
     "sans les deux empreintes exigées »).\n",
     "Validateur `controle_ia.prereg.problemes` : aucun défaut sur ce brouillon 2 (vérifié avant son scellement comme pièce de\n"
     "travail).\n"),
    ("contre-lecture", ANCIENNE_CL, NOUVELLE_CL),
]

tous = couples + PROPRES

# 3. Chaque « ancien » une seule fois dans la pièce de départ ; aucun chevauchement.
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

if ESSAI is not None:
    chemin_essai = os.path.join(ESSAI, "crible-iv-brouillon2.md")
    with open(chemin_essai, "x", encoding="utf-8") as f:
        f.write(cible)
    print(f"ESSAI : cible écrite hors du dossier des pièces : {chemin_essai}")
    print(f"couples appliqués : {len(tous)} ({len(couples)} du rapport, {len(PROPRES)} propres)")
    sys.exit(0)

with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(cible)
diff = difflib.unified_diff(source.splitlines(keepends=True), cible.splitlines(keepends=True),
                            fromfile="crible-iv-brouillon1.md", tofile="crible-iv-brouillon2.md")
with open(DIFF, "x", encoding="utf-8") as f:
    f.writelines(diff)
print(f"cible écrite : {CIBLE}")
print(f"différentiel écrit : {DIFF}")
print(f"heure (date -u) : {heure}")
print(f"couples appliqués : {len(tous)} ({len(couples)} du rapport, {len(PROPRES)} propres) : "
      + ", ".join(n for _, _, n, _ in places))
print(f"empreinte de la cible : {sha(CIBLE)}")

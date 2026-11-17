"""Brouillon 3 du préenregistrement du crible (iv), demi-générations : corrections du tour 2 de contre-lecture.

Couples « ancien → nouveau » :
  (1) les 3 couples exigés par le rapport `contre-lecture-crible-iv-tour2-v1.md` (M1.1, majeure ; m1.1 et m2.1, mineures),
      lus dans le rapport lui-même (blocs « Xk.j — ancien : » et « nouveau : » entre clôtures de trois accents graves) et
      recopiés sans retouche ; ils sont aussi comparés à une copie écrite ici, pour que toute lecture fautive arrête ;
  (2) des couples propres de forme (titre, ligne du brouillon 3 dans l'en-tête, statut, ligne du validateur, section
      « Contre-lecture »), déclarés dans l'entrée « Contre-lecture 2 » de la cible.
Gardes : empreintes de la pièce de départ (brouillon 2) et du rapport ; 3 couples exactement, dans l'ordre du rapport ; chaque
« ancien » figure exactement une fois dans la pièce de départ ; aucun chevauchement entre « anciens » ; tous les couples
appliqués d'un coup, par positions, sur la pièce de départ ; chaque « nouveau » présent dans la cible, ceux du rapport
exactement une fois ; aucun « ancien » du rapport resté dans la cible ; validateur `controle_ia.prereg.problemes` sans défaut
sur la cible, écrite d'abord dans un dossier temporaire ; la cible, son différentiel et leurs compagnons ne doivent pas
exister (ouverture en mode « x ») ; aucun repli silencieux.
L'heure est lue par `date -u` juste avant l'écriture ; le scellement suit dans la même commande, hors de ce programme.
Bibliothèque standard, `git rev-parse` (lecture seule) et module `controle_ia.prereg` du dépôt ; aucun appel, aucune donnée.
Usage : .venv/bin/python -I appliquer-corrections-crible-iv-brouillon3.py                 (écrit la cible et le différentiel)
        .venv/bin/python -I appliquer-corrections-crible-iv-brouillon3.py --essai DOSSIER (les écrit dans DOSSIER, jetable)
"""
import difflib
import hashlib
import os
import re
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
NOM_SOURCE = "crible-iv-brouillon2.md"
SOURCE = os.path.join(ICI, NOM_SOURCE)
SOURCE_SHA = "603306b98180b33ea2c585fe8f33ad45c714a763a976819a9b53c49e563b069f"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-iv-tour2-v1.md")
RAPPORT_SHA = "ca94c2ca962bc82675b9996d63de484a9c8b2fc835209c466f7f921944193506"
NOM_CIBLE = "crible-iv-brouillon3.md"
NOM_DIFF = "diff-crible-iv-b2-vers-b3.txt"
NOM_PROGRAMME = "appliquer-corrections-crible-iv-brouillon3.py"
TETE_DEBUT = "1df4ae9f"  # tête de `main` relevée au début de la lecture des deux pièces (`git rev-parse`)


def arret(msg):
    print(f"ARRÊT : {msg}", file=sys.stderr)
    sys.exit(2)


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def commande(args):
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout.strip()


# 0. Arguments, racine du dépôt, cibles jamais écrasées.
if len(sys.argv) == 1:
    DOSSIER = ICI
elif len(sys.argv) == 3 and sys.argv[1] == "--essai":
    DOSSIER = os.path.abspath(sys.argv[2])
    if not os.path.isdir(DOSSIER):
        arret(f"dossier d'essai absent : {DOSSIER}")
    if os.path.commonpath([DOSSIER, ICI]) == ICI:
        arret("--essai doit viser un dossier jetable, hors du dossier des pièces")
else:
    arret("usage : sans argument, ou --essai DOSSIER")
if os.path.basename(os.path.abspath(__file__)) != NOM_PROGRAMME:
    arret("nom du programme inattendu")
if not os.path.isfile(os.path.join(DEPOT, "src", "controle_ia", "prereg.py")):
    arret(f"racine du dépôt introuvable : {DEPOT}")
CIBLE = os.path.join(DOSSIER, NOM_CIBLE)
DIFF = os.path.join(DOSSIER, NOM_DIFF)
for chemin in (CIBLE, CIBLE + ".sha256", DIFF, DIFF + ".sha256"):
    if os.path.exists(chemin):
        arret(f"cible déjà présente, jamais écrasée : {chemin}")

# 1. Empreintes des pièces lues.
for chemin, attendu in ((SOURCE, SOURCE_SHA), (RAPPORT, RAPPORT_SHA)):
    if not os.path.isfile(chemin):
        arret(f"pièce absente : {chemin}")
    if sha(chemin) != attendu:
        arret(f"empreinte différente : {chemin}")
with open(SOURCE, encoding="utf-8") as f:
    source = f.read()
with open(RAPPORT, encoding="utf-8") as f:
    rapport = f.read()
SHA_PROGRAMME = sha(os.path.abspath(__file__))

# 2. Heure (date -u) et tête du dépôt (lecture seule).
HEURE = commande(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"])
if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", HEURE):
    arret(f"heure illisible : {HEURE!r}")
BRANCHE = commande(["git", "-C", DEPOT, "rev-parse", "--abbrev-ref", "HEAD"])
TETE = commande(["git", "-C", DEPOT, "rev-parse", "--short=8", "HEAD"])
if BRANCHE != "main" or not re.fullmatch(r"[0-9a-f]{8}", TETE):
    arret(f"dépôt hors de `main` ou tête illisible : {BRANCHE!r} {TETE!r}")
TETES = f"`{TETE}`" if TETE == TETE_DEBUT else f"`{TETE_DEBUT}` au début de la lecture, `{TETE}` à l'écriture"

# 3. Couples du rapport, lus tels quels, puis comparés à une copie écrite ici.
MOTIF = re.compile(
    r"^((?:M|m)\d\.\d+) — ancien :\n```\n(.*?)\n```\nnouveau :\n```\n(.*?)\n```\n",
    re.M | re.S)
couples = [(m.group(1), m.group(2), m.group(3)) for m in MOTIF.finditer(rapport)]
ATTENDUS = ["M1.1", "m1.1", "m2.1"]
if [c[0] for c in couples] != ATTENDUS:
    arret(f"couples du rapport inattendus : {[c[0] for c in couples]}")
if rapport.count(" — ancien :") != len(ATTENDUS) or rapport.count("\nnouveau :\n") != len(ATTENDUS):
    arret("le rapport porte un bloc « ancien » ou « nouveau » non lu par le motif")
COPIES = {
    "M1.1": (
        "la phrase « les demi-générations couvrent moins » est alors interdite sans le complément « à dollars égaux, "
        "avec une génération 2 amputée dans k mondes »",
        "la phrase « les demi-générations couvrent moins » est alors interdite sans le complément « à dollars proches "
        "(ρ_21 dit), avec une génération 2 amputée dans k mondes »"),
    "m1.1": (
        "signe négatif ; à dollars égaux, payer\ndeux fois l'entrée pour trois cartes de moins par appel",
        "signe négatif ; à dollars proches (ρ_21 dit), payer\ndeux fois l'entrée pour trois cartes de moins par appel"),
    "m2.1": (
        "Rien d'autre que les corrections, l'en-tête et la section « Contre-lecture » ne change.",
        "Rien d'autre que les corrections, le titre, le statut, la ligne du validateur, cette ligne et la section "
        "« Contre-lecture » ne change."),
}
for nom, ancien, nouveau in couples:
    if (ancien, nouveau) != COPIES[nom]:
        arret(f"{nom} : couple lu dans le rapport différent de la copie attendue")

# 4. Couples propres de forme.
DEBUT_T2 = "- **Tour 2 à faire** (R2) : sur ce brouillon 2,"
FIN_CL = "\n## Annexe A — comptes exacts"
if source.count(DEBUT_T2) != 1 or source.count(FIN_CL) != 1:
    arret("bornes de « Tour 2 à faire » introuvables une fois")
i_t2, j_t2 = source.index(DEBUT_T2), source.index(FIN_CL)
if not i_t2 < j_t2:
    arret("bornes de « Tour 2 à faire » dans le désordre")
ANCIEN_T2 = source[i_t2:j_t2]
if "\n## " in ANCIEN_T2 or not ANCIEN_T2.endswith("signalés ci-dessus.\n"):
    arret("fin de « Tour 2 à faire » inattendue")
titre_section = source[source.rindex("\n## ", 0, i_t2) + 4:].split("\n", 1)[0]
if titre_section != "Contre-lecture":
    arret(f"« Tour 2 à faire » hors de la section « Contre-lecture » : {titre_section!r}")

NOUVEAU_T2 = f"""- **Contre-lecture 2** (R2, tour 2, sur le brouillon 2) — sous-agent neuf, d'un autre modèle que le rédacteur du brouillon 1
  selon l'en-tête de son rapport, qui dit n'avoir écrit aucune pièce lue. Texte relu :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/{NOM_SOURCE}`,
  `{SOURCE_SHA}` ; rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-iv-tour2-v1.md`,
  `{RAPPORT_SHA}`. Verdict : « corrections » (1 majeure, M1 ;
  2 mineures, m1 et m2 ; 3 couples ; la conception n'est pas en cause selon le lecteur ; un tour 3 réduit à ces trois couples
  et au différentiel). Corrections appliquées le {HEURE} (`date -u`) par un rédacteur neuf, qui n'a écrit ni les
  brouillons 1 et 2 ni aucun des deux rapports (identité dite en conversation seulement), au moyen du programme
  `{NOM_PROGRAMME}` (même dossier, scellé à côté ; empreinte au moment de l'écriture :
  `{SHA_PROGRAMME}` ; différentiel `{NOM_DIFF}`, scellé) :
  les 3 couples sont lus dans le rapport lui-même et recopiés sans retouche (le programme les compare aussi à une copie
  écrite en lui) ; chaque « ancien » figure une seule fois dans le brouillon 2, sans chevauchement, et aucune fois dans ce
  brouillon 3, où chaque « nouveau » figure une fois (vérifié par le programme). **Traitement**, point par point :
  - Rapport, § 2 et § 3 (fidélité des six couples du tour 1, vérifiée par programme ; passages touchés relus ; devis,
    enveloppe, durées et interdits non touchés) : constats du lecteur, aucune correction ; rien à faire.
  - M1 (étage 2 du tableau des critères de lecture gelés : sous la réserve « demi-générations amputées », le complément exigé
    de la phrase « les demi-générations couvrent moins » disait « à dollars égaux », alors que l'étage 4 exige ρ_21 et que sa
    traduction dit « à dollars proches (ρ_21 dit) », la garde souple n'assurant pas l'égalité ; couple M1.1) : **acceptée**,
    telle quelle. Les étages 2 et 4 ne demandent plus deux compléments contraires.
  - m1 (« Ce que serait chaque issue » : la lecture « moins » gardait « à dollars égaux » ; couple m1.1) : **acceptée**, telle
    quelle.
  - m2 (en-tête : la dernière phrase de la ligne du brouillon 2 ne nommait ni le statut ni la ligne du validateur, qui ont
    aussi changé ; couple m2.1) : **acceptée**, telle quelle ; la ligne du brouillon 3 nomme de même tout ce qui change.
  - Remarques facultatives (rapport, § 5) : **non appliquées**, aucune correction n'étant exigée. (1) Les autres occurrences de
    « à dollars égaux » (§ 0, points 1 et 7 ; énoncé de H-iv ; prédiction IV-1 ; citation de [NOTE] au point 3 de « Choix et
    doutes ») énoncent la question de [NOTE] et l'hypothèse visée, et la garde souple est dite au point 3 : laissées telles
    quelles, au choix de la mère. (2) « Dépassement borné par un appel » (étage 4) et « un demi-appel par monde » (raison de
    IV-9) : même sens selon le lecteur, vocabulaire non harmonisé. (3) Remarques facultatives du tour 1 (seuil de la sonde plus
    bas que la coupe, profondeur informative pour le seul bras 2, sigle « e-BH ») : toujours à la mère.
  - Rapport, § 6 (pour la session mère) : point 1 fait (ce brouillon 3, en fichier neuf) ; point 2 (aucun écart à un texte
    scellé, aucun mot de Lazar nécessaire) : pris acte ; point 3 (risques inchangés : la sonde et le rapport c3/c6, pièce « non
    lançable » à deux tiers ou plus ; la marge d'enveloppe de 11,33 USD ; l'équivalence du nul v8 à vérifier au code) :
    inchangés, rien dans ce texte.
  - Liste « Non corrigé par le rapport » de la contre-lecture 1 : l'étage 2 et « Ce que serait chaque issue » sont désormais
    corrigés (M1.1 et m1.1) ; les autres occurrences de « à dollars égaux » restent telles quelles (remarque facultative 1
    ci-dessus) ; le titre de la section « Devis » garde « brouillon 1 », qui nomme le devis et son programme, inchangés.
  - **Couples propres** (forme seulement) : titre (brouillon 3) ; ligne « Brouillon 3 » de l'en-tête ; statut ; ligne du
    validateur ; cette section (entrée « Contre-lecture 2 » et « Tour 3 à faire », à la place de « Tour 2 à faire »).
- **Tour 3 à faire** (R2) : sur ce brouillon 3, réduit (rapport du tour 2, § 6) à vérifier les trois couples M1.1, m1.1 et
  m2.1, les couples propres de forme et le différentiel, par un sous-agent neuf d'un **autre modèle** que le rédacteur du
  brouillon 1, qui n'a écrit aucun des brouillons 1 à 3, ni les rapports des tours 1 et 2, ni [NOTE], ni [CRIBLE-II], ni
  [CRIBLE-III], ni [CRIBLE-V], ni [PILOTE], ni [MR2]. **Fichiers à lui donner explicitement** : ce texte ; le brouillon 2 et le
  rapport du tour 2 (empreintes ci-dessus) ; `{NOM_PROGRAMME}` et `{NOM_DIFF}` (même
  dossier) ; pour une relecture plus large, la liste du « Tour 2 à faire » du brouillon 2 (section « Contre-lecture ») vaut
  toujours. **À vérifier en priorité** : que les étages 2 et 4 du tableau des critères gelés et « Ce que serait chaque issue »
  qualifient la lecture « moins » de la même façon (« à dollars proches », ρ_21 dit) ; que les lignes « Brouillon 2 » et
  « Brouillon 3 » de l'en-tête disent exactement ce qui a changé.
"""

LIGNE_B3 = (
    "- Brouillon 3 : corrections du tour 2 de contre-lecture (une majeure, M1, et deux mineures, m1 et m2 ; trois couples)\n"
    f"  appliquées le {HEURE} (`date -u`, au scellement) par un rédacteur neuf, qui n'a écrit ni les brouillons 1 et 2 ni\n"
    "  aucun des deux rapports de contre-lecture (identité dite en conversation seulement), au moyen du programme\n"
    f"  `{NOM_PROGRAMME}` (même dossier, scellé ; différentiel `{NOM_DIFF}`, scellé) ;\n"
    f"  arbre de travail lu sur `{BRANCHE}` (tête {TETES} ;\n"
    "  brouillon 2 et rapport du tour 2, non encore suivis, lus sur disque, empreintes vérifiées) ; aucune autre branche lue ;\n"
    "  aucun commit, aucune poussée, aucun appel de modèle, aucune machine, aucune dépense, aucun monde tiré. Ne changent que\n"
    "  les trois corrections, le titre, le statut, la ligne du validateur, cette ligne et la section « Contre-lecture ».\n"
)
ANCRE_B3 = "- Nombres neufs : `devis-crible-iv-brouillon1.py`"

PROPRES = [
    ("titre",
     "milieu de chaque génération — brouillon 2 (variante « crédits de Claude au maximum »)\n",
     "milieu de chaque génération — brouillon 3 (variante « crédits de Claude au maximum »)\n"),
    ("ligne du brouillon 3", ANCRE_B3, LIGNE_B3 + ANCRE_B3),
    ("statut",
     "**Statut.** **Brouillon 2**, contre-lu une fois (tour 1, corrections appliquées, section « Contre-lecture »), scellé comme\n"
     "pièce (empreinte compagnon, R6), non comme préenregistrement en vigueur ; second tour de contre-lecture à faire\n"
     "(R2).",
     "**Statut.** **Brouillon 3**, contre-lu deux fois (tours 1 et 2, corrections appliquées, section « Contre-lecture »),\n"
     "scellé comme pièce (empreinte compagnon, R6), non comme préenregistrement en vigueur ; troisième tour de contre-lecture\n"
     "à faire (R2), réduit aux trois couples du tour 2, aux couples de forme et au différentiel."),
    ("validateur",
     "Validateur `controle_ia.prereg.problemes` : aucun défaut sur ce brouillon 2 (vérifié avant son scellement comme pièce de\n"
     "travail).\n",
     "Validateur `controle_ia.prereg.problemes` : aucun défaut sur ce brouillon 3 (vérifié par le programme de correction sur\n"
     "une copie temporaire, avant l'écriture et le scellement comme pièce de travail).\n"),
    ("contre-lecture", ANCIEN_T2, NOUVEAU_T2),
]

# 5. Chaque « ancien » une seule fois ; aucun chevauchement ; application d'un coup, par positions.
tous = couples + PROPRES
places = []
for nom, ancien, nouveau in tous:
    n = source.count(ancien)
    if n != 1:
        arret(f"{nom} : « ancien » trouvé {n} fois dans la pièce de départ (une seule attendue)")
    debut = source.index(ancien)
    places.append((debut, debut + len(ancien), nom, nouveau))
places.sort()
for (d1, f1, n1, _), (d2, f2, n2, _) in zip(places, places[1:]):
    if d2 < f1:
        arret(f"chevauchement entre {n1} et {n2}")
morceaux, curseur = [], 0
for debut, fin, nom, nouveau in places:
    morceaux.append(source[curseur:debut])
    morceaux.append(nouveau)
    curseur = fin
morceaux.append(source[curseur:])
cible = "".join(morceaux)

# 6. Contrôles de la cible.
for nom, ancien, nouveau in tous:
    if nouveau not in cible:
        arret(f"{nom} : « nouveau » absent de la cible")
for nom, ancien, nouveau in couples:
    if cible.count(nouveau) != 1:
        arret(f"{nom} : « nouveau » présent {cible.count(nouveau)} fois dans la cible (une seule attendue)")
    if cible.count(ancien) != 0:
        arret(f"{nom} : « ancien » resté dans la cible")
for marque, attendu in (("- **Contre-lecture 1**", 1), ("- **Contre-lecture 2**", 1), ("- **Tour 3 à faire**", 1),
                        ("- **Tour 2 à faire**", 0), ("— brouillon 3 (variante", 1), ("**Brouillon 3**", 1)):
    if cible.count(marque) != attendu:
        arret(f"forme de la cible : « {marque} » présent {cible.count(marque)} fois ({attendu} attendu)")

# 7. Validateur sur une copie temporaire.
sys.path.insert(0, os.path.join(DEPOT, "src"))
from controle_ia.prereg import problemes  # noqa: E402

with tempfile.TemporaryDirectory() as td:
    tmp = os.path.join(td, NOM_CIBLE)
    with open(tmp, "x", encoding="utf-8") as f:
        f.write(cible)
    defauts = problemes(tmp)
if defauts:
    arret(f"validateur : {defauts}")

# 8. Écriture de la cible et du différentiel, sans écraser.
with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(cible)
diff = difflib.unified_diff(source.splitlines(keepends=True), cible.splitlines(keepends=True),
                            fromfile=NOM_SOURCE, tofile=NOM_CIBLE)
with open(DIFF, "x", encoding="utf-8") as f:
    f.writelines(diff)
print(("ESSAI : " if DOSSIER != ICI else "") + f"cible écrite : {CIBLE}")
print(f"différentiel écrit : {DIFF}")
print(f"heure (date -u) : {HEURE} ; dépôt : {BRANCHE} {TETE}")
print(f"programme : {SHA_PROGRAMME}")
print(f"couples appliqués : {len(tous)} ({len(couples)} du rapport, {len(PROPRES)} propres) : "
      + ", ".join(n for _, _, n, _ in places))
print("validateur : aucun défaut")
print(f"empreinte de la cible : {sha(CIBLE)}")
print(f"empreinte du différentiel : {sha(DIFF)}")

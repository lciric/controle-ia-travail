"""Brouillon 3 du préenregistrement du crible (iii) : application des corrections du tour 2 de contre-lecture.

Couples « ancien → nouveau » : les 16 couples de D-01 à D-14 (D-02 et D-12 en deux couples chacun) sont lus dans le rapport
de contre-lecture du tour 2 lui-même (blocs « Ancien… : » et « Nouveau : » entre clôtures de quatre accents graves, section
« 3. Corrections exigées »), sans aucun écart ; s'y ajoutent les couples propres à l'en-tête et à la section « Contre-lecture ».
Gardes : empreinte de la pièce de départ (brouillon 2) et du rapport ; 16 couples exactement, dans l'ordre attendu ; chaque
« ancien » figure exactement une fois dans la pièce de départ ; aucun chevauchement entre « anciens » ; chaque « nouveau »
figure dans la cible ; la cible (et son compagnon) ne doit pas exister et n'est jamais écrasée (ouverture en mode « x ») ;
le validateur `controle_ia.prereg.problemes` est rejoué sur le texte neuf (copie temporaire) avant toute écriture de la cible
et doit rendre une liste vide ; aucun repli silencieux. Bibliothèque standard seule (le validateur est appelé par
`.venv/bin/python` avec `PYTHONPATH=src`) ; aucun appel de modèle, aucune donnée.
Usage : python3 -I appliquer-corrections-crible-iii-brouillon3.py  (depuis n'importe quel dossier)
"""
import hashlib
import os
import re
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
SOURCE = os.path.join(ICI, "crible-iii-brouillon2.md")
SOURCE_SHA = "713ea6a7f3c7a2b6a4ae627a6445a9ff06fd4acd3dfedee24fc3fd6630d0bd3d"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-iii-tour2-v1.md")
RAPPORT_SHA = "9a7043b0b1c0a3eaa48262d539861631f7df11cabed264dee8cc21918f14105c"
CIBLE = os.path.join(ICI, "crible-iii-brouillon3.md")
NOM_PROGRAMME = "appliquer-corrections-crible-iii-brouillon3.py"
ATTENDUS = ["D-01", "D-02", "D-02", "D-03", "D-04", "D-05", "D-06", "D-07", "D-08", "D-09", "D-10", "D-11", "D-12",
            "D-12", "D-13", "D-14"]


def arret(msg):
    sys.stderr.write("ARRÊT : " + msg + "\n")
    sys.exit(2)


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


if not os.path.isfile(os.path.join(DEPOT, "src", "controle_ia", "prereg.py")):
    arret(f"racine du dépôt introuvable : {DEPOT}")
for chemin, attendu in ((SOURCE, SOURCE_SHA), (RAPPORT, RAPPORT_SHA)):
    if sha(chemin) != attendu:
        arret(f"empreinte différente : {chemin}")
for chemin in (CIBLE, CIBLE + ".sha256"):
    if os.path.exists(chemin):
        arret(f"cible déjà présente, jamais écrasée : {chemin}")

source = open(SOURCE, encoding="utf-8").read()
rapport = open(RAPPORT, encoding="utf-8").read()

# 1. Couples du rapport (section 3 seule).
DEBUT_S3, FIN_S3 = "## 3. Corrections exigées : ancien → nouveau\n", "## 4. Remarques facultatives"
if rapport.count(DEBUT_S3) != 1 or rapport.count(FIN_S3) != 1:
    arret("bornes de la section 3 du rapport introuvables une fois")
s3 = rapport[rapport.index(DEBUT_S3):rapport.index(FIN_S3)]
TITRE = re.compile(r"^### (D-\d\d) \((majeur|mineur)\)[^\n]*\n", re.M)
COUPLE = re.compile(r"^Ancien[^\n]*:\n\n````\n(.*?)\n````\n\nNouveau :\n\n````\n(.*?)\n````\n", re.M | re.S)
titres = list(TITRE.finditer(s3))
couples = []
for k, t in enumerate(titres):
    fin = titres[k + 1].start() if k + 1 < len(titres) else len(s3)
    bloc = s3[t.end():fin]
    trouves = list(COUPLE.finditer(bloc))
    if bloc.count("````") != 4 * len(trouves):
        arret(f"bloc de {t.group(1)} mal formé (clôtures non appariées)")
    for m in trouves:
        couples.append((t.group(1), m.group(1), m.group(2)))
noms = [c[0] for c in couples]
if noms != ATTENDUS:
    arret(f"couples du rapport inattendus : {noms}")

# 2. Couples propres : en-tête et section « Contre-lecture ».
heure = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], check=True, capture_output=True, text=True).stdout.strip()
if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", heure):
    arret(f"heure illisible : {heure!r}")

DEBUT_TS = "**Tour suivant** (obligatoire si la variante est retenue, selon le rapport) :"
FIN_TS = "## Annexe A — comptes exacts"
if source.count(DEBUT_TS) != 1 or source.count(FIN_TS) != 1:
    arret("bornes du paragraphe « Tour suivant » introuvables une fois")
ANCIEN_TS = source[source.index(DEBUT_TS):source.index(FIN_TS)]

NOUVEAU_TS = f"""- **Contre-lecture 2** (R2, tour 2, sur le brouillon 2) — sous-agent neuf, d'un autre modèle que l'auteur, qui n'a écrit ni ce
  texte, ni le rapport du tour 1, ni aucune pièce citée (un premier contre-lecteur de ce tour s'était arrêté sur une limite
  d'usage sans rendre de rapport, R-2982 : rien de lui n'est repris). Texte relu :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-brouillon2.md`,
  `{SOURCE_SHA}` ; rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-iii-tour2-v1.md`,
  `{RAPPORT_SHA}`. Verdict : « corrections » (3 majeures :
  D-01 à D-03 ; 11 mineures : D-04 à D-14) ; le rapport constate que les 26 corrections du tour 1 sont appliquées fidèlement
  et que la conception tient. Corrections appliquées le {heure} par un rédacteur neuf, qui n'a écrit ni les brouillons 1 et 2
  ni les rapports de contre-lecture, au moyen du programme `{NOM_PROGRAMME}` (même dossier, scellé à côté) : les 16 couples
  (D-02 et D-12 en deux couples chacun) sont lus dans le rapport lui-même, sans aucun écart ; chaque « ancien » figure une
  seule fois dans le brouillon 2 (vérifié par le programme).
  **Traitement**, point par point :
  - D-01 (concurrence : 15 sessions de Pr-2 et 5 de Pr-1 à cinq files, 18 et 6 à six files) : **acceptée** (« Devis »,
    « Durée »).
  - D-02 (texte à N : ligne « mondes, appels, files » ajoutée à la table « Règle de mise à jour d'après le pilote » ; les trois
    valeurs calculées sur processeur avant le scellement nommées hors de « tout autre chiffre reste » ; brouillon nouveau,
    contre-lu, si l'une d'elles demandait un seuil ou une règle autre) : **acceptée**, deux couples (« Devis »).
  - D-03 (forme du crible « à trancher par la mère avant le scellement » ; texte non scellable tant que rien n'est inscrit) :
    **acceptée** (« Choix et doutes », point 4 ; statut de l'en-tête). **Aucune décision n'est inscrite ici** : aucune ligne
    de `registres/decisions.md` ne tranche la forme à l'heure de l'application ; ce texte reste rédigé dans la forme fidèle
    à [NOTE]. Les ajouts « Si la variante est retenue » de la section 5 du rapport ne sont **pas** appliqués (ils ne valent
    qu'après la décision ; tour 3 obligatoire si la variante est retenue).
  - D-04 (choix 9, durée, tranché) : **acceptée** (« Choix et doutes », point 9).
  - D-05 (première personne du contre-lecteur du tour 1 retirée) : **acceptée** (« Taille »).
  - D-06 (phrase périmée sur le pilote : joué, machine détruite, issue non lue) : **acceptée** (statut de l'en-tête).
  - D-07 (seuil du test des signes à N = 24 : 18 accords) : **acceptée** (« Taille ») ; l'extension du point 2 de l'annexe A
    à n = 21 à 24 par un programme sous un nom neuf reste à faire avant le scellement.
  - D-08 (dénominateur minimal de la ligne « limite de débit » : dix appels du fournisseur) : **acceptée** (liste d'arrêt).
  - D-09 (garde de départ de 10 h, qui remplace les 12 h 30 de [PROC-14]) : **acceptée** (section 0, point 9).
  - D-10 (affectation des mondes aux files : r modulo F, fixée avant tout appel) : **acceptée** (section 0, point 9).
  - D-11 (0,996 au lieu de 1,00) : **acceptée** (« Seuil »).
  - D-12 (seuils de format, 14, et de zone utile, 10 : valeurs absolues quel que soit N) : **acceptée**, deux couples
    (« Seuil ») ; le choix d'une proportion (17 et 12 à 24 mondes) reste un point pour la mère (rapport, section 6, point 8).
  - D-13 (gel de III-6 recommandé, confirmé par la mère avant le scellement, jamais après lecture du pilote) : **acceptée**
    (statut de l'en-tête).
  - D-14 (appel le plus long du pilote au-dessus de 1 500 s : nœud de la mère avant le scellement) : **acceptée** (table de
    mise à jour).
  - **Non appliqué, faute de correction exigée** : les remarques facultatives de la section 4 du rapport (aucun changement) ;
    les ajouts de sa section 5 (conditionnels à la variante, voir D-03).
  - **Points du rapport pour la mère, ouverts** (section 6 ; aucun n'est tranché ici) : la forme (D-03) et le solde de crédits
    de Claude pour 263 USD au pire (315 à 24 mondes) ; le prix promotionnel de Pr-1, offert jusqu'au 30 novembre ; 24 mondes
    sans condition (+ 20 %), la règle « sous 0,95 » revenant en pratique à « au moindre échec » ; N-045 point 3, à dire à
    Lazar avec le nœud d'adoption ; le gel de III-6 avant lecture du pilote ; le code neuf (environ deux jours d'agents,
    concurrence jamais éprouvée) ; le risque d'un « non tranché » de P2 même si III-2 est vraie ; seuils absolus ou
    proportion (D-12).
  - **Restes signalés au tour 1, non corrigés par le rapport du tour 2, sans rien changer** : les renvois à [CRIBLE-V],
    brouillon non scellé (« Composantes comptées », « Hypothèses de coût », « Plafond de 0,75 ») ; la ligne « Témoin commun »
    du devis, écartée et encore écrite avec ses chiffres (rapport, section 4, remarque 3).

**Tour suivant** (obligatoire si la variante est retenue, selon les rapports des tours 1 et 2 ; sinon, contre-lecture de la
version qui fera foi) : sous-agent neuf qui n'a écrit ni ce texte, ni les brouillons 1 et 2, ni les rapports des tours 1 et 2.
**Fichiers à lui donner explicitement** : ce texte ; les brouillons 1 et 2 et les rapports des tours 1 et 2 (empreintes
ci-dessus) ; les programmes `appliquer-corrections-crible-iii-brouillon2.py` et `{NOM_PROGRAMME}` ; [CRIBLE-V] (« Métrique »,
« Devis ») ; [NOTE] (`2f6a69dd…`), § 1, § 2, § 3 (iii), § 4, § 6 et annexe A ; [RELEVÉ] (`bd253b6c…`), § 3.1, § 4.2, § 5, § 6 ;
[REC] (`eecd98fa…`), V3 et C2 ; [PILOTE] (`8aa33014…`), « Dessin », « Métrique », « Devis », bloc gelé ; [PROC-14]
(`20355627…`), § 0, § 6, § 7 ; [MR2] (`47e38ec0…`), § 2 et § 3 ; [V3] (`386d48ba…`), § 4.1 ; `mesure_pilote_v4.py`
(`676d5f37…`) ; `monde_riche_outils_v1.py` (`1825b956…`) ; N-045 v2 (`c7b05e39…`) ; N-058 (`854f2724…`) ; la ligne
GO-2026-11-15-06 ; la ligne R-2977 de `registres/decisions.md` ; l'annexe A et ses deux programmes.

"""

PUCE_B3 = f"""  « Contre-lecture » ne change.
- Brouillon 3 : corrections du tour 2 de contre-lecture appliquées le {heure} (`date -u`, au scellement) par un
  rédacteur neuf, qui n'a écrit ni les brouillons 1 et 2 ni les rapports de contre-lecture (identité dite en conversation
  seulement), au moyen du programme `{NOM_PROGRAMME}` (même dossier, scellé) ; dépôt lu sur `main` (tête
  `99275f89`) ; procédure v14 relue au commit `2d35cafa…` par `git show`, après un `git fetch` à refspec ; rien lu de la
  sortie du pilote MR-2 v14 ; aucun commit, aucune poussée. Rien d'autre que les 16 couples du rapport du tour 2, l'en-tête
  et la section « Contre-lecture » ne change.
- Commit du code d'analyse"""

PROPRES = [
    ("en-tête : titre",
     "par un proposeur cher — brouillon 2\n",
     "par un proposeur cher — brouillon 3\n"),
    ("en-tête : puce du brouillon 3",
     "  « Contre-lecture » ne change.\n- Commit du code d'analyse",
     PUCE_B3),
    ("en-tête : statut",
     "**Statut.** Brouillon 2, **contre-lu une fois** (tour 1, corrections appliquées, section « Contre-lecture ») ; **non scellé\n"
     "comme texte qui fait foi** (R1, R2) ; forme du crible à trancher (« Choix et doutes », point 4).",
     "**Statut.** Brouillon 3, **contre-lu deux fois** (tours 1 et 2, corrections appliquées, section « Contre-lecture ») ; **non scellé\n"
     "comme texte qui fait foi** (R1, R2), et **non scellable** tant que la forme du crible n'est pas tranchée par la mère et\n"
     "inscrite (« Choix et doutes », point 4)."),
    ("en-tête : validateur",
     "aucun défaut sur ce brouillon 2 (vérifié avant son scellement comme pièce de\ntravail).",
     "aucun défaut sur ce brouillon 3 (vérifié avant son scellement comme pièce de\ntravail)."),
    ("contre-lecture : entrée 2 et tour suivant", ANCIEN_TS, NOUVEAU_TS),
]

tous = couples + PROPRES

# 3. Chaque « ancien » une seule fois dans la pièce de départ ; aucun chevauchement.
places = []
for nom, ancien, nouveau in tous:
    n = source.count(ancien)
    if n != 1:
        arret(f"« ancien » de {nom} présent {n} fois dans la pièce de départ")
    d = source.index(ancien)
    places.append((d, d + len(ancien), nom, nouveau))
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
        arret(f"« nouveau » de {nom} absent de la cible")

# 5. Validateur rejoué sur une copie temporaire, avant toute écriture de la cible.
with tempfile.TemporaryDirectory() as tmp:
    copie = os.path.join(tmp, "crible-iii-brouillon3.md")
    with open(copie, "x", encoding="utf-8") as f:
        f.write(cible)
    code = ("import sys; from controle_ia.prereg import problemes; p = problemes(sys.argv[1]); "
            "print(repr(p)); sys.exit(1 if p else 0)")
    env = {"PATH": "/usr/bin:/bin", "PYTHONPATH": os.path.join(DEPOT, "src")}
    r = subprocess.run([os.path.join(DEPOT, ".venv", "bin", "python"), "-c", code, copie], cwd=DEPOT, env=env,
                       capture_output=True, text=True)
    if r.returncode != 0:
        arret(f"validateur : {r.stdout.strip()} {r.stderr.strip()}")
    validateur = r.stdout.strip()

with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(cible)
print(f"cible écrite : {CIBLE}")
print(f"heure (date -u) : {heure}")
print(f"couples appliqués : {len(tous)} ({len(couples)} du rapport, {len(PROPRES)} propres) : "
      + ", ".join(n for _, _, n, _ in places))
print(f"validateur (problemes) : {validateur}")
print(f"empreinte de la cible : {sha(CIBLE)}")

"""Brouillon 3 du préenregistrement du crible (i), placebo par monde jumeau : correction du tour 2 de contre-lecture.

Couples « ancien → nouveau » :
  (1) le seul couple exigé par le rapport `contre-lecture-crible-i-tour2-v1.md` (mineure m7, étage 2 des « Critères de lecture
      gelés »), lu dans le rapport lui-même (section « 3. Corrections exigées », lignes qui suivent « - ancien → nouveau : »)
      et recopié sans retouche ; il est aussi comparé à une copie écrite ici, pour que toute lecture fautive arrête ;
  (2) des couples propres de forme (Q1 à Q5 : titre, en-tête, statut, validateur, section « Contre-lecture »), déclarés dans
      l'entrée « Contre-lecture 2 » de la cible.
Gardes : empreinte de la pièce de départ (brouillon 2) et du rapport ; un seul couple dans la section 3 du rapport, aucune
majeure ; chaque « ancien » figure exactement une fois dans la pièce de départ ; aucun chevauchement entre « anciens » ; tous
les couples appliqués d'un coup sur la pièce de départ ; chaque « nouveau » présent dans la cible ; aucun « ancien » du rapport
resté hors des « nouveau » ; validateur `controle_ia.prereg.problemes` sans défaut sur la cible, écrite d'abord dans un
dossier temporaire ; la cible et son compagnon ne doivent pas exister (ouverture en mode « x ») ; aucun repli silencieux.
L'heure est lue par `date -u` au moment de l'écriture ; le scellement suit aussitôt, hors de ce programme.
Bibliothèque standard et module `controle_ia.prereg` du dépôt ; aucun appel, aucune donnée.
Usage : .venv/bin/python -I appliquer-corrections-crible-i-brouillon3.py [--essai DOSSIER]
  (--essai : écrit la cible dans DOSSIER, dossier de travail jetable, pour la contrôler avant l'écriture réelle)
"""
import hashlib
import os
import re
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
SOURCE = os.path.join(ICI, "crible-i-brouillon2.md")
SOURCE_SHA = "30b3c945091d3ea0d129b5197c6a0a28f3625f71bb21b1ce188c8e8b984b321a"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-i-tour2-v1.md")
RAPPORT_SHA = "3bda94797ce98133459af77f8ab25f18cd6b617fb05e1bde52a55a7c781ac854"
NOM_CIBLE = "crible-i-brouillon3.md"


def arret(msg):
    print(f"ARRÊT : {msg}", file=sys.stderr)
    sys.exit(2)


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


# 0. Arguments, racine du dépôt, cible.
if len(sys.argv) == 1:
    DOSSIER = ICI
elif len(sys.argv) == 3 and sys.argv[1] == "--essai":
    DOSSIER = os.path.abspath(sys.argv[2])
    if DOSSIER == ICI:
        arret("--essai doit viser un dossier jetable, pas le dossier de la pièce")
    if not os.path.isdir(DOSSIER):
        arret(f"dossier d'essai absent : {DOSSIER}")
else:
    arret("usage : appliquer-corrections-crible-i-brouillon3.py [--essai DOSSIER]")
if not os.path.isfile(os.path.join(DEPOT, "src", "controle_ia", "prereg.py")):
    arret(f"racine du dépôt introuvable : {DEPOT}")
CIBLE = os.path.join(DOSSIER, NOM_CIBLE)
for chemin in (CIBLE, CIBLE + ".sha256"):
    if os.path.exists(chemin):
        arret(f"cible déjà présente, jamais écrasée : {chemin}")

# 1. Empreintes.
for chemin, attendu in ((SOURCE, SOURCE_SHA), (RAPPORT, RAPPORT_SHA)):
    if not os.path.isfile(chemin):
        arret(f"pièce absente : {chemin}")
    if sha(chemin) != attendu:
        arret(f"empreinte différente : {chemin}")
with open(SOURCE, encoding="utf-8") as f:
    texte = f.read()
with open(RAPPORT, encoding="utf-8") as f:
    rapport = f.read()
SHA_PROGRAMME = sha(os.path.abspath(__file__))

# 2. Heure (date -u), lue au moment de l'écriture, scellement juste après.
HEURE = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True, check=True).stdout.strip()
if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", HEURE):
    arret(f"heure illisible : {HEURE!r}")

# 3. Couple du rapport, lu dans sa section 3 (texte recopié sans retouche).
DEBUT_S3, FIN_S3 = "## 3. Corrections exigées\n", "## 4. Remarques facultatives"
if rapport.count(DEBUT_S3) != 1 or rapport.count(FIN_S3) != 1:
    arret("bornes de la section 3 du rapport introuvables une fois")
s3 = rapport[rapport.index(DEBUT_S3):rapport.index(FIN_S3)]
if "Majeures : aucune." not in s3 or "### Majeure" in s3:
    arret("le rapport devait n'exiger aucune majeure")
lignes = s3.split("\n")
MARQUE = "- ancien → nouveau :"
if lignes.count(MARQUE) != 1 or s3.count("ancien → nouveau") != 1:
    arret("un seul couple « ancien → nouveau » attendu dans la section 3 du rapport")
k = lignes.index(MARQUE)
l_ancien, l_nouveau = lignes[k + 1], lignes[k + 2]
if not (l_ancien.startswith("  « ") and l_ancien.endswith(" »")):
    arret("ligne « ancien » du rapport mal formée")
if not (l_nouveau.startswith("  → « ") and l_nouveau.endswith(" »")):
    arret("ligne « nouveau » du rapport mal formée")
M7_ANCIEN = l_ancien[len("  « "):-len(" »")]
M7_NOUVEAU = l_nouveau[len("  → « "):-len(" »")]
COPIE_ANCIEN = ("sous « TJ tronqué », les phrases « effet d'information » et « information et forme » sont **interdites** "
                "(TJ a pu perdre des cartes, ce qui gonfle P1)")
COPIE_NOUVEAU = COPIE_ANCIEN + (" et la phrase « rien d'établi » est remplacée par « non tranché (TJ tronqué) » "
                                "(la même perte dégonfle P2)")
if (M7_ANCIEN, M7_NOUVEAU) != (COPIE_ANCIEN, COPIE_NOUVEAU):
    arret("couple m7 lu dans le rapport différent de la copie attendue")
couples = [("m7", M7_ANCIEN, M7_NOUVEAU)]

# 4. Couples propres de forme.
ANCIEN_FIN_SECTION_DEBUT = "    P7 cette section.\n\n**À faire** (R2) : tour 2, différentiel (M1 à M3, m1 à m6 et E1 seulement)"
if texte.count(ANCIEN_FIN_SECTION_DEBUT) != 1 or texte.count("\n## Annexe A") != 1:
    arret("bornes de la fin de la section « Contre-lecture » introuvables une fois")
debut = texte.index(ANCIEN_FIN_SECTION_DEBUT)
fin = texte.index("\n## Annexe A")
if not debut < fin:
    arret("bornes de la section « Contre-lecture » dans le désordre")
ANCIENNE_FIN_SECTION = texte[debut:fin]
if "\n## " in ANCIENNE_FIN_SECTION or not ANCIENNE_FIN_SECTION.endswith(".\n"):
    arret("fin de la section « Contre-lecture » inattendue")

NOUVELLE_FIN_SECTION = f"""    P7 cette section.
- **Contre-lecture 2** (R2, tour 2, différentiel, sur le brouillon 2) — sous-agent neuf, d'un autre modèle que l'auteur, qui dit
  n'avoir écrit aucune des pièces (rapport, en-tête). Texte relu :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-i-brouillon2.md`,
  `{SOURCE_SHA}` ; rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-i-tour2-v1.md`,
  `{RAPPORT_SHA}`. Verdict : « corrections » (aucune majeure ; une mineure,
  m7 ; aucune nouvelle remarque facultative de fond). Correction appliquée le {HEURE} par un rédacteur neuf,
  d'un autre modèle que l'auteur, qui n'a écrit ni les brouillons 1 et 2, ni aucun des deux rapports, au moyen du programme
  `appliquer-corrections-crible-i-brouillon3.py` (même dossier, scellé à côté ; empreinte au moment de l'écriture :
  `{SHA_PROGRAMME}`) : le seul couple du rapport, lu dans le rapport lui-même et
  recopié sans retouche (le programme vérifie les empreintes du brouillon 2 et du rapport, que l'« ancien » figure une seule fois
  dans le brouillon 2, et refuse d'écraser la cible), plus cinq couples propres de forme (Q1 à Q5), déclarés ci-dessous.
  Différentiel : `diff-crible-i-b2-vers-b3.txt` (même dossier, scellé). Rien d'autre ne change. **Traitement**, point par point :
  - Rapport, § 1 (fidélité des corrections du tour 1 : M1 à M3, m1 à m6, extension E1, couples de forme P1 à P7) : constats du
    lecteur, aucune correction ; E1 **acceptée** par lui ; sa remarque non exigée sur P7 (liste de fichiers du tour 1 remplacée
    par un renvoi au brouillon 1) est dite acceptable : rien à faire ; l'écart d'écriture « environ 0,19 » (entrée 1 ci-dessus)
    contre « environ 0,2 » (« Taille ») est dit sans effet : gardé tel quel.
  - Rapport, § 2 (passages touchés relus et vérifications refaites : étages 0 à 3, « Taille », « Devis », R1, R3, R4, fidélité
    à [NOTE], lectures interdites) : constats, aucune correction autre que m7, qui en vient.
  - m7 (étage 2 : sous « TJ tronqué », la phrase « rien d'établi » doit aussi être remplacée) : **acceptée**, texte du rapport
    (couple unique, ligne de l'étage 2 des « Critères de lecture gelés »). Logique revérifiée par le rédacteur : des cartes
    perdues par le bras de la table du jumeau (TJ) font baisser c_TJ, donc gonflent P1 (c_TV − c_TJ) et dégonflent P2
    (c_TJ − c_S0) ; « P1 établi » et « P2 non établi » ne sont alors plus robustes ; les issues (a) et (c) de l'étage 3, qui
    s'appuient sur « P1 établi », étaient déjà interdites ; l'issue (d), qui s'appuie sur « P2 non établi », est désormais
    remplacée par « non tranché (TJ tronqué) » ; l'issue (b) reste permise (P2 établi malgré la baisse, P1 non établi malgré la
    hausse). Les trois bras sont ainsi traités de la même façon.
  - Rapport, § 4 (facultatives) : rien de neuf à appliquer ; F1, F4, F5 et F7 du tour 1 restent à trancher avant la version qui
    fera foi (entrée 1 ci-dessus) ; le calcul de puissance à + 4 mondes reste **à refaire par un programme scellé sous un nom
    neuf avant la version qui fera foi** (le recoupement du lecteur du tour 2, rapport, § 1, n'est pas scellé) : non fait ici
    (hors du couple exigé).
  - Rapport, § 5 (points pour la session mère) : point 1 fait (m7 par un couple neuf : ce brouillon 3) ; la relecture de cette
    seule ligne par un lecteur neuf avant le scellement comme texte qui fait foi est laissée au jugement de la mère (« À faire »
    ci-dessous) ; point 2 (ligne datée de `registres/decisions.md` confirmant le gel, qui dira que I-1 est gelée avec « ≥ + 4 »
    même si P1 ne peut l'établir à ce seuil et que les zones de I-5, I-6 et I-7 ont été ajoutées après le gel ; nœud de Lazar
    sur l'enveloppe des cinq cribles ; calcul scellé de la puissance à + 4 mondes ; choix F1, F4, F5, F7) : à la mère, rien dans
    ce texte ; point 3 (aucun écart à un texte scellé, aucun mot de Lazar nécessaire pour ce tour) : pris acte.
  - Rapport, § 6 (incidents du lecteur : un calcul de son programme d'abord en erreur, sans écriture ni effet, puis relancé) :
    sans effet sur ce texte.
  - **Couples propres** (forme seulement) : Q1 titre (brouillon 3) ; Q2 en-tête (ligne du brouillon 3) ; Q3 statut ; Q4
    validateur ; Q5 cette section (entrée « Contre-lecture 2 » et « À faire »).

**À faire** (R2) : tour 3, relecture de la seule ligne corrigée par m7 (étage 2 des « Critères de lecture gelés ») et des couples
de forme Q1 à Q5, par un sous-agent neuf d'un **autre modèle** que l'auteur, qui n'a écrit ni ce texte, ni les rapports des tours
1 et 2, ni [NOTE], ni [PILOTE], ni [CRIBLE-III], ni [CRIBLE-V], si la mère juge que cette relecture suffit avant le scellement
comme texte qui fait foi (rapport du tour 2, § 5, point 1). **Fichiers à lui donner explicitement** : ce texte ; le brouillon 2
(`30b3c945…`) ; le différentiel `diff-crible-i-b2-vers-b3.txt` ; le rapport du tour 2 (`3bda9479…`) ; le programme
`appliquer-corrections-crible-i-brouillon3.py` ; pour une relecture plus large, les listes données aux tours 1 et 2 (brouillons 1
et 2, section « Contre-lecture ») valent toujours. **Point à lui soumettre en priorité** : la symétrie de l'étage 2 sur les trois
bras après m7 (toute phrase de l'étage 3 qui s'appuie sur un côté non robuste d'une des deux différences est interdite ou
remplacée).
"""

Q = [
    ("Q1",
     "par sa seule présence ?) — brouillon 2 (variante « crédits de Claude au maximum »)",
     "par sa seule présence ?) — brouillon 3 (variante « crédits de Claude au maximum »)"),
    ("Q2",
     "  rien d'autre ne change. Le reste de cet en-tête est celui du brouillon 1.\n- **Ordre de rédaction, déclaré**",
     "  rien d'autre ne change. Le reste de cet en-tête est celui du brouillon 1.\n"
     f"- **Brouillon 3** (écrit et scellé le {HEURE}, `date -u`) : correction du tour 2 de contre-lecture (m7, une ligne\n"
     "  de l'étage 2 des « Critères de lecture gelés ») appliquée par un rédacteur neuf, d'un autre modèle que l'auteur, par le\n"
     "  programme `appliquer-corrections-crible-i-brouillon3.py` (même dossier) ; détail et réponse point par point : section\n"
     "  « Contre-lecture » ; différentiel `diff-crible-i-b2-vers-b3.txt` ; rien d'autre ne change. Le reste de cet en-tête est\n"
     "  celui du brouillon 2.\n"
     "- **Ordre de rédaction, déclaré**"),
    ("Q3",
     "**Statut.** Brouillon 2, **contre-lu au tour 1** (verdict « corrections », corrections appliquées ; tour 2, différentiel, à\n"
     "faire : R2, section « Contre-lecture »)",
     "**Statut.** Brouillon 3, **contre-lu aux tours 1 et 2** (verdicts « corrections », corrections appliquées ; tour 3, relecture\n"
     "de la seule ligne corrigée au tour 2 par un lecteur neuf, à faire si la mère la juge suffisante : R2, section\n"
     "« Contre-lecture »)"),
    ("Q4",
     "(vérifié avant le scellement de ce brouillon\n"
     "comme pièce de travail, puis relancé sur ce brouillon 2 avant son scellement : aucun défaut formel ; la section\n"
     "« Contre-lecture » cite le brouillon 1 relu et le rapport du tour 1, avec leurs empreintes).",
     "(vérifié avant le scellement du brouillon 1\n"
     "comme pièce de travail, puis relancé sur le brouillon 2 et sur ce brouillon 3 avant leur scellement : aucun défaut formel ;\n"
     "la section « Contre-lecture » cite les brouillons 1 et 2 relus et les rapports des tours 1 et 2, avec leurs empreintes)."),
    ("Q5", ANCIENNE_FIN_SECTION, NOUVELLE_FIN_SECTION),
]

# 5. Gardes : chaque « ancien » une seule fois ; aucun chevauchement ; application d'un coup.
tous = couples + Q
places = []
for nom, ancien, nouveau in tous:
    n = texte.count(ancien)
    if n != 1:
        arret(f"{nom} : « ancien » présent {n} fois dans la pièce de départ")
    i = texte.index(ancien)
    places.append((i, i + len(ancien), nom, nouveau))
places.sort()
for (a0, a1, n0, _), (b0, b1, n1, _) in zip(places, places[1:]):
    if b0 < a1:
        arret(f"chevauchement entre {n0} et {n1}")
morceaux = []
pos = 0
for debut_, fin_, nom, nouveau in places:
    morceaux.append(texte[pos:debut_])
    morceaux.append(nouveau)
    pos = fin_
morceaux.append(texte[pos:])
cible = "".join(morceaux)

for nom, ancien, nouveau in tous:
    if nouveau not in cible:
        arret(f"{nom} : « nouveau » absent de la cible")
for nom, ancien, nouveau in couples:
    reste = cible.count(ancien) - sum(nv.count(ancien) for _, _, nv in tous)
    if reste > 0:
        arret(f"{nom} : « ancien » resté dans la cible hors des « nouveau »")
if cible.count("- **Contre-lecture 2**") != 1 or cible.count("**À faire** (R2)") != 1:
    arret("section « Contre-lecture » de la cible mal formée")

# 6. Validateur sur une copie temporaire.
sys.path.insert(0, os.path.join(DEPOT, "src"))
from controle_ia.prereg import problemes  # noqa: E402

with tempfile.TemporaryDirectory() as td:
    tmp = os.path.join(td, NOM_CIBLE)
    with open(tmp, "x", encoding="utf-8") as f:
        f.write(cible)
    defauts = problemes(tmp)
if defauts:
    arret(f"validateur : {defauts}")

# 7. Écriture, sans écraser.
with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(cible)
print(f"écrit : {CIBLE}")
print(f"heure : {HEURE}")
print(f"programme : {SHA_PROGRAMME}")
print(f"couples du rapport : {len(couples)} ; couples propres de forme : {len(Q)}")
print("validateur : aucun défaut formel")
print(f"empreinte : {sha(CIBLE)}")

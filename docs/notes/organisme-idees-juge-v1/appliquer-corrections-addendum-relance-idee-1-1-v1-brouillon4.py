"""Brouillon 4 de l'addendum de relance de l'idée 1.1 : mise au propre du brouillon 3, avec trois changements seulement.

(1) la correction e-1 exigée par la contre-lecture du tour 3 (lettre du rédacteur des corrections du brouillon 3 : A, non
    C ; R-2992, point 0 ; R-3016), tirée du § 2 du rapport par programme ; la remarque facultative h-1 n'est pas appliquée ;
(2) l'écart D7 (lieu (ii), machine de calcul louée) déclaré accepté par Lazar, GO-2026-11-16-10, verbatim tiré de la ligne
    de `registres/go.md` trouvée par sa clé (objet de `main`) ; le lieu (i) reste décrit, comme non retenu ;
(3) l'en-tête (version, heure `date -u`, « en vigueur une fois recopié sous `prereg/…-addendum-relance-v1.md` »).

- vérifie l'empreinte du brouillon 3, du rapport du tour 3 et du programme du brouillon 3, chacun contre son compagnon ;
- exige que chaque « ancien » figure exactement une fois dans le brouillon 3 et qu'aucun couple n'en chevauche un autre ;
- exige, après application, zéro ligne au format du lanceur (« empreinte, deux espaces, chemin »), zéro ligne qui commence
  par 64 caractères hexadécimaux, et que chaque « nouveau » figure dans la cible ;
- refuse d'écraser la cible (ouverture en mode « x »).
Lancé par `python3 -I -B` ; commandes légères seulement ; aucun fichier du run invalide n'est ouvert.
"""
import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")
DOSSIER = DEPOT / "docs/notes/organisme-idees-juge-v1"
SOURCE = DOSSIER / "addendum-relance-idee-1-1-v1-brouillon3.md"
SHA_SOURCE = "7b11231c58b86e8999d0b6a3740a533473c8093be131107439404fcfe7075c81"
RAPPORT = DOSSIER / "contre-lecture-addendum-relance-idee-1-1-tour3-v1.md"
SHA_RAPPORT = "877efacdb3e3571825a518517f9644e3825a5981487c7a0165f6dc290e328726"
PROG_B3 = DOSSIER / "appliquer-corrections-addendum-relance-idee-1-1-v1-brouillon3.py"
SHA_PROG_B3 = "885acb925766619faab3cf5c2d44ccb2071cc4b13586cd73dbc31780a3d2a1f0"
CIBLE = DOSSIER / "addendum-relance-idee-1-1-v1-brouillon4.md"
PROGRAMME = "docs/notes/organisme-idees-juge-v1/appliquer-corrections-addendum-relance-idee-1-1-v1-brouillon4.py"
CLE_GO = "| GO-2026-11-16-10 |"
VERBATIM = "« Ma recommandation est d’accepter, confiance 0,65. : go »"
MOTIF_LANCEUR = re.compile(r"^([0-9a-f]{64})  (\S+)\s*$", re.M)     # expression de `execution_v1.verifier_addendum`
MOTIF_HEX = re.compile(r"^[0-9a-f]{64}", re.M)
ENV_GIT = {**os.environ, "GIT_OPTIONAL_LOCKS": "0"}


def h(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def arret(msg: str):
    print("ARRÊT :", msg, file=sys.stderr)
    sys.exit(1)


def compagnon(p: Path, attendu: str):
    b = p.read_bytes()
    if h(b) != attendu:
        arret(f"empreinte inattendue : {p.name}")
    c = Path(str(p) + ".sha256").read_text(encoding="utf-8").split()
    if not c or c[0] != attendu:
        arret(f"compagnon inégal : {p.name}")
    return b


if CIBLE.exists():
    arret(f"{CIBLE.name} existe déjà : R12 interdit d'écraser")
src = compagnon(SOURCE, SHA_SOURCE).decode("utf-8")
rap = compagnon(RAPPORT, SHA_RAPPORT).decode("utf-8")
compagnon(PROG_B3, SHA_PROG_B3)

# (1) e-1, tirée du § 2 du rapport du tour 3
sec = rap[rap.index("## 2. Correction exigée"):rap.index("## 3. Remarque facultative")]
m = list(re.finditer(r"- ancien :\n```\n(?P<a>.*?)\n```\n- nouveau :\n```\n(?P<n>.*?)\n```", sec, re.S))
if len(m) != 1 or "**e-1 —" not in sec:
    arret(f"couple e-1 : {len(m)} trouvé(s) dans le § 2 du rapport")
E1_A, E1_N = m[0]["a"], m[0]["n"]

# Sources lues par commande : tête de main, ligne de go.md trouvée par sa clé (objet de main), heure
TETE = subprocess.run(["git", "-C", str(DEPOT), "rev-parse", "main"], capture_output=True, text=True, check=True,
                      env=ENV_GIT).stdout.strip()
b_go = subprocess.run(["git", "-C", str(DEPOT), "show", "main:registres/go.md"], capture_output=True, check=True,
                      env=ENV_GIT).stdout
lignes_go = [l for l in b_go.decode("utf-8").splitlines() if l.startswith(CLE_GO)]
if len(lignes_go) != 1 or VERBATIM not in lignes_go[0] or "écart D7 accepté" not in lignes_go[0]:
    arret("ligne GO-2026-11-16-10 absente, multiple, ou sans le verbatim attendu")
SHA_GO = h(b_go)
if not (DEPOT / "docs/procedures/machine-jeu-idee-1-1-v1").exists():
    PROC_ETAT = "en écriture, contre-lue à part ; absente du dépôt à l'heure de ce brouillon"
else:
    PROC_ETAT = "en écriture, contre-lue à part"
HEURE = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True, check=True).stdout.strip()

# (3) En-tête
EN_TETE_A = """- **Statut et lieu** : brouillon 3, `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-1-v1-brouillon3.md`, scellé
  par son compagnon comme pièce de travail (R6) ; il ne fait foi que dans sa recopie sous
  `prereg/organisme-idee-1-1-poids-du-nul-v2-addendum-relance-v1.md`, scellée après la contre-lecture (R2). Premier addendum"""
EN_TETE_N = f"""- **Version : brouillon 4.** Mise au propre du brouillon 3
  (`{SHA_SOURCE}`) après la contre-lecture du tour 3 : rapport
  `docs/notes/organisme-idees-juge-v1/contre-lecture-addendum-relance-idee-1-1-tour3-v1.md`
  (`{SHA_RAPPORT}`, égal à son compagnon), verdict
  « corrections » (0 majeure, 1 mineure exigée, e-1, 1 remarque facultative, h-1). Rédacteur : lettre A (le modèle des
  brouillons 1 à 3 et de leurs programmes), sous-agent neuf de la session mère, qui n'a écrit ni les rapports de
  contre-lecture des tours 1 à 3, ni [T], ni [AE], ni le code, ni l'étape 0 : couples « ancien → nouveau » appliqués au
  brouillon 3 par le programme
  `{PROGRAMME}` (scellé à côté) ;
  dépôt lu sur `main`, tête `{TETE}` ; heure du scellement {HEURE} (`date -u`) ; aucun commit,
  aucune poussée. Trois changements, rien d'autre :
  (1) **e-1**, tirée du § 2 du rapport par programme : le rédacteur des corrections du brouillon 3 est de lettre A, non C,
  fait vérifié par la mère dans les journaux des sous-agents (R-2992, point 0 ; R-3016) ; c'était la seule mention qui
  donnait à tort la lettre C à un correcteur (les lettres C du § 7 sont celles des lecteurs ; la citation du programme du
  brouillon 2 y est donnée comme fautive) ; le programme du brouillon 3,
  `docs/notes/organisme-idees-juge-v1/appliquer-corrections-addendum-relance-idee-1-1-v1-brouillon3.py`
  (`{SHA_PROG_B3}`, égal à son compagnon), porte encore dans
  `EN_TETE_N` « rédacteur neuf, lettre C » : il reste tel quel (R12 : on n'écrase pas une pièce scellée) et ne fait pas
  foi sur ce point ;
  (2) **l'écart D7 accepté par Lazar** (GO-2026-11-16-10 ; R-3016) : le lieu du jeu relancé devient la machine de calcul
  louée (§ 1, § 4 en tête, 4.9, 4.10, § 5) ; le lieu (i) reste décrit, comme non retenu ;
  (3) cet en-tête (cette puce et la suivante).
  h-1, facultative, n'est pas appliquée ; la section « Contre-lecture » (§ 7) et la déclaration du § 8 ne sont pas mises à
  jour pour le tour 3 : à compléter à la recopie sous `prereg/` (rapport du tour 3, § 4, point 5), avec le recomptage des
  lignes au format du lanceur (attendu 0) et les empreintes du § 8.
- **Statut et lieu** : brouillon 4, `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-1-v1-brouillon4.md`, scellé
  par son compagnon comme pièce de travail (R6) ; **en vigueur une fois recopié sous
  `prereg/organisme-idee-1-1-poids-du-nul-v2-addendum-relance-v1.md`** et scellé, après le contrôle différentiel (R2 ;
  R-3016). Premier addendum"""

# (2) D7 : § 1
S1A_A = "critères de lecture, audit de symétrie, liste d'arrêt (l. 605-629), coût et borne dure de 48 heures (l. 627, 659)."
S1A_N = """critères de lecture, audit de symétrie, liste d'arrêt (l. 605-629), coût et borne dure de 48 heures (l. 627, 659),
  **sauf l'écart D7** (4.10) : le jeu relancé se joue sur une machine de calcul louée, contre la lettre de l. 629 et de
  l. 660 (citées en 4.10) ; écart accepté par Lazar (GO-2026-11-16-10)."""
S1B_A = "ni ligne de la liste d'arrêt de [T] ;"
S1B_N = "ni ligne de la liste d'arrêt de [T], hors l'écart D7 (lieu et dépense, 4.10) ;"
S1C_A = "run invalide (§ 6). Si une phrase d'ici semblait contredire [T] ou [AE], [T] puis [AE] l'emportent."
S1C_N = """run invalide (§ 6) ; il déclare l'écart D7, accepté par Lazar (4.9, 4.10). Si une phrase d'ici semblait contredire [T]
ou [AE], [T] puis [AE] l'emportent, hors l'écart D7."""

# (2) D7 : § 4, en tête
S4_A = "Elles valent pour les deux lieux possibles du jeu relancé (§ 4.10), sans rien changer d'autre."
S4_N = """Elles valent pour le lieu retenu du jeu relancé, une machine de calcul louée (§ 4.10, lieu (ii) ; écart D7 accepté par
Lazar, GO-2026-11-16-10), sans rien changer d'autre ; le lieu (i), le conteneur de la session, n'est pas retenu."""

# (2) D7 : 4.9
S49_A = """**4.9 Dépense, mot de Lazar, moment.** Sur le conteneur (4.10, lieu (i)) : aucune dépense ([T] l. 629) ; la relance sous un
addendum neuf est ce que [T] l. 620 et [AE] l. 392-400 prescrivent, et cet addendum ne déclare aucun écart. **Le moment et
le lieu attendent la réponse de Lazar à la question de R-3010** (machine de calcul indépendante de la session, ou relance
sur le conteneur) ; le choix relève de la mère sur ce mot et se consigne au registre ; il n'entre dans aucune graine (4.2)."""
S49_N = f"""**4.9 Dépense, mot de Lazar, moment.** La relance sous un addendum neuf est ce que [T] l. 620 et [AE] l. 392-400
prescrivent. **Le lieu est tranché** : la question de R-3010 (machine de calcul indépendante de la session, ou relance sur
le conteneur) a reçu le mot de Lazar sur D7, GO-2026-11-16-10 (`registres/go.md`, ligne trouvée par sa clé ; objet de
`main` à la tête citée en en-tête :
`{SHA_GO}`), verbatim :
{VERBATIM} ; le jeu relancé se joue sur une machine de calcul louée (4.10, lieu (ii)). La
dépense part sous sa propre ligne « calcul », inscrite par la mère sur le devis contre-lu de la procédure de machine
(GO-2026-11-16-10 : ordre de grandeur de 1 à 3 USD) ; sans cette ligne, aucune machine louée ne part. Sur le conteneur
(lieu (i), non retenu), il n'y aurait eu ni dépense ([T] l. 629) ni écart. Le moment relève de la mère, après la recopie de
cet addendum sous `prereg/`, la procédure de machine contre-lue et la ligne « calcul » (R-3016) ; il se consigne au registre
et n'entre dans aucune graine (4.2)."""

# (2) D7 : 4.10
S410_A = """**4.10 Lieu du jeu relancé : laissé ouvert (R-3010).** Cet addendum vaut pour l'un ou l'autre lieu ; tout le reste (4.1 à
4.9, § 5 et § 6) est identique.

- **(i) Le conteneur de la session.** Aucune dépense ; consigne de tâche active (§ 5) ; **risque déclaré** : une reprise"""
S410_N = """**4.10 Lieu du jeu relancé : une machine de calcul louée (lieu (ii)), écart D7 accepté par Lazar (GO-2026-11-16-10).**
R-3010 laissait le lieu ouvert entre les deux lieux ci-dessous ; le mot de Lazar sur D7 (4.9) retient le lieu (ii). Tout le
reste (4.1 à 4.9, § 5 et § 6) est identique à ce qu'il serait sur le conteneur.

- **(i) Le conteneur de la session : non retenu.** Décrit pour mémoire. Aucune dépense ; consigne de tâche active (§ 5) ;
  **risque déclaré** : une reprise"""
S410B_A = """- **(ii) Une machine de calcul louée, indépendante de la session.** Elle demande : **devis et GO** (dépense) ; une
  **procédure de machine à part**, hors de cet addendum (création, copie du commit noté, versions de 4.2, recopie octet pour
  octet des sorties scellées vers le dépôt, vérification par leurs compagnons, destruction par identifiant, R10) ; et,
  **en plus, le mot de Lazar sur un écart au texte scellé** :"""
S410B_N = f"""- **(ii) Une machine de calcul louée, indépendante de la session : retenue.** Elle demande : **devis et GO** (dépense : la
  ligne « calcul » de 4.9) ; une **procédure de machine à part**, hors de cet addendum,
  `docs/procedures/machine-jeu-idee-1-1-v1/` ({PROC_ETAT}) (création, copie du commit noté,
  versions de 4.2, recopie octet pour octet des sorties scellées vers le dépôt, vérification par leurs compagnons,
  destruction par identifiant, R10) ; et, **en plus, le mot de Lazar sur un écart au texte scellé** :"""
S410C_A = """lieu et de dépense (nœud de décision : écart à un préenregistrement scellé ; nom proposé : **D7**, à la mère) ; cet
  addendum ne l'accepte pas et ne le déclare que pour le cas où ce lieu serait retenu. **Sans le mot de Lazar sur D7, consigné à `registres/go.md` (comme D5, GO-2026-11-16-07), aucune machine louée ne part sous cet addendum.**"""
S410C_N = f"""lieu et de dépense (nœud de décision : écart à un préenregistrement scellé), nommé **D7**. **D7 est accepté par Lazar** :
  GO-2026-11-16-10, consigné à `registres/go.md` (comme D5, GO-2026-11-16-07), verbatim
  {VERBATIM} (R-3016) ; rien d'autre de [T] ne change. **Limite déclarée** (4.2) : mêmes
  graines, mêmes clés, mêmes flux de bits des générateurs ; l'égalité au bit près avec le run invalide n'est pas garantie
  sur un autre processeur, sans effet sur la validité ; comparer les deux runs reste interdit (§ 3)."""

# (2) D7 : § 5
S5A_A = "- **Consigne (lieu (i))** : celle de [R12] § 5, reprise telle quelle."
S5A_N = "- **Consigne (lieu (i), non retenu, 4.10 ; décrite pour mémoire)** : celle de [R12] § 5, reprise telle quelle."
S5B_A = "- **Lieu (ii)** : la survie du jeu ne dépend pas de la session ; la surveillance suit la procédure de machine."
S5B_N = """- **Lieu (ii), retenu (4.10)** : la survie du jeu ne dépend pas de la session ; la surveillance suit la procédure de
  machine (`docs/procedures/machine-jeu-idee-1-1-v1/`)."""

tous = [("e-1", E1_A, E1_N), ("en-tête", EN_TETE_A, EN_TETE_N),
        ("D7 § 1 a", S1A_A, S1A_N), ("D7 § 1 b", S1B_A, S1B_N), ("D7 § 1 c", S1C_A, S1C_N),
        ("D7 § 4", S4_A, S4_N), ("D7 4.9", S49_A, S49_N),
        ("D7 4.10 a", S410_A, S410_N), ("D7 4.10 b", S410B_A, S410B_N), ("D7 4.10 c", S410C_A, S410C_N),
        ("D7 § 5 a", S5A_A, S5A_N), ("D7 § 5 b", S5B_A, S5B_N)]
spans = []
for k, a, _ in tous:
    n = src.count(a)
    if n != 1:
        arret(f"{k} : « ancien » trouvé {n} fois dans le brouillon 3")
    i = src.index(a)
    spans.append((i, i + len(a), k))
spans.sort()
for (d1, f1, k1), (d2, f2, k2) in zip(spans, spans[1:]):
    if d2 < f1:
        arret(f"chevauchement : {k1} et {k2}")

nouveau = src
for k, a, n in tous:
    nouveau = nouveau.replace(a, n, 1)
for k, _, n in tous:
    if n not in nouveau:
        arret(f"{k} : « nouveau » absent de la cible")
n_l, n_x = len(MOTIF_LANCEUR.findall(nouveau)), len(MOTIF_HEX.findall(nouveau))
if n_l or n_x:
    arret(f"lignes au format du lanceur : {n_l} ; lignes qui commencent par 64 caractères hexadécimaux : {n_x}")
if CIBLE.exists():
    arret(f"{CIBLE.name} existe déjà : R12 interdit d'écraser")
with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(nouveau)
print("heure (date -u) :", HEURE)
print("tête de main :", TETE)
print("registres/go.md (objet de main) :", SHA_GO)
print("couples appliqués :", ", ".join(k for k, _, _ in tous))
print("lignes au format du lanceur :", n_l, "; lignes qui commencent par 64 caractères hexadécimaux :", n_x)
print("« lettre C » restantes, lignes :", [i + 1 for i, l in enumerate(nouveau.splitlines()) if "lettre C" in l])
print("lignes : brouillon 3", src.count("\n"), "; brouillon 4", nouveau.count("\n"))
print("empreinte de la cible :", h(nouveau.encode("utf-8")))

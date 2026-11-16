"""Brouillon 5 du préenregistrement du crible (v) : application des corrections du tour 4 de contre-lecture.

Couples « ancien → nouveau » : les 21 couples des corrections B4-01 à B4-12 (B4-01 à B4-12e) sont lus dans le rapport de
contre-lecture lui-même (bloc entre clôtures nommé `B4-…`, ligne « ANCIEN: » puis ligne « NOUVEAU: » ; « \\n » dans un
« nouveau » = saut de ligne, comme le dit le rapport), sans retouche ; s'y ajoutent des couples propres, chacun nommé et
déclaré dans la section « Contre-lecture » de la cible : titre, en-tête, statut, validateur, tête de la section
« Contre-lecture », point 12 de l'annexe A (chiffres de durée que le rapport demande « à refaire par programme et à
recopier en annexe » : sortie de `comptes-crible-v-brouillon5.py`, lue par empreinte), entrée « Contre-lecture 4 ».
Gardes : empreinte de la pièce de départ, du rapport, du programme des comptes et de sa sortie ; 21 couples exactement
dans le rapport, noms attendus ; chaque « ancien » (du rapport et propre) figure exactement une fois dans la pièce de
départ ; aucun chevauchement entre « anciens » ; tous les couples appliqués d'un coup sur la pièce de départ ; chaque
« nouveau » présent dans la cible ; la cible ne doit pas exister (ouverture en mode « x ») ; aucun repli silencieux.
Bibliothèque standard seule ; aucun appel, aucune donnée.
Usage : python3 -I appliquer-corrections-crible-v-brouillon5.py [--essai DOSSIER]
  (--essai : écrit la cible dans DOSSIER, dossier de travail jetable, pour la contrôler avant l'écriture réelle)
"""
import hashlib
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ICI, "crible-v-brouillon4.md")
SOURCE_SHA = "af6e6db3a74ef099f6f62da8ef1c2af7ddc703a2c9a18415b25f6dba27388f86"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-v-b4-tour1-v1.md")
RAPPORT_SHA = "27364670772a7bdc5298b903e5edca3f819b8bc7a16f33bcd636fb38816bd78b"
COMPTES = os.path.join(ICI, "comptes-crible-v-brouillon5.py")
COMPTES_SHA = "66861511daa6cfd2257b72c943322c2de6147edd554c17210af632e0aa6abc06"
SORTIE = os.path.join(ICI, "comptes-crible-v-brouillon5-sortie.txt")
SORTIE_SHA = "aa4013f0a66e42b673e4252b9747289ed3e7c66c4456a1200fccdb71ac329dd1"
NOM_CIBLE = "crible-v-brouillon5.md"
NOMS_RAPPORT = ["B4-01", "B4-02", "B4-03a", "B4-03b", "B4-04a", "B4-04b", "B4-05a", "B4-05b", "B4-06", "B4-07a",
                "B4-07b", "B4-08", "B4-09", "B4-10", "B4-11a", "B4-11b", "B4-12a", "B4-12b", "B4-12c", "B4-12d",
                "B4-12e"]


def arret(msg):
    sys.stderr.write("ARRÊT : " + msg + "\n")
    sys.exit(2)


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


# 0. Dossier de la cible.
args = sys.argv[1:]
if args == []:
    DOSSIER = ICI
elif len(args) == 2 and args[0] == "--essai":
    DOSSIER = os.path.abspath(args[1])
    if DOSSIER == ICI or not os.path.isdir(DOSSIER):
        arret(f"dossier d'essai invalide : {DOSSIER}")
else:
    arret(f"arguments illisibles : {args!r}")
CIBLE = os.path.join(DOSSIER, NOM_CIBLE)

# 1. Empreintes des entrées ; cible absente.
for chemin, attendu in ((SOURCE, SOURCE_SHA), (RAPPORT, RAPPORT_SHA), (COMPTES, COMPTES_SHA), (SORTIE, SORTIE_SHA)):
    if not os.path.isfile(chemin):
        arret(f"absent : {chemin}")
    if sha(chemin) != attendu:
        arret(f"empreinte inattendue : {chemin}")
if os.path.exists(CIBLE):
    arret(f"la cible existe déjà : {CIBLE}")

with open(SOURCE, encoding="utf-8") as f:
    texte = f.read()
with open(RAPPORT, encoding="utf-8") as f:
    rapport = f.read()
with open(SORTIE, encoding="utf-8") as f:
    sortie_comptes = f.read().rstrip("\n")

# 2. Couples du rapport.
blocs = re.findall(r"^`(B4-[0-9a-z]+)`\n```\nANCIEN: (.*?)\nNOUVEAU: (.*?)\n```", rapport, re.S | re.M)
if [b[0] for b in blocs] != NOMS_RAPPORT:
    arret(f"couples du rapport inattendus : {[b[0] for b in blocs]!r}")
couples = []
for nom, ancien, nouveau in blocs:
    if "\n" in ancien or "\n" in nouveau:
        arret(f"{nom} : ancien ou nouveau sur plusieurs lignes")
    couples.append((nom, ancien, nouveau.replace("\\n", "\n")))

# 3. Heure lue par `date -u`.
HEURE = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], check=True, capture_output=True, text=True).stdout.strip()
if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", HEURE):
    arret(f"heure illisible : {HEURE!r}")

# 4. Couples propres.
PROPRES = []

PROPRES.append(("titre",
    "(regroupement, sans juge) — brouillon 4",
    "(regroupement, sans juge) — brouillon 5"))

PROPRES.append(("en-tete",
    "  scellé le 2026-11-16T14:15:41Z (`date -u`) ; aucun commit, aucune poussée (section « Contre-lecture »).",
    "  scellé le 2026-11-16T14:15:41Z (`date -u`) ; aucun commit, aucune poussée (section « Contre-lecture »).\n"
    "- Brouillon 5 : corrections du tour 4 de contre-lecture appliquées par un rédacteur neuf (modèle C, **écart de rôle à\n"
    "  R-2982, déclaré** ; il n'a écrit ni le brouillon 1, ni les brouillons 2 à 4, ni aucun des quatre rapports, ni aucune\n"
    f"  pièce citée), écrit et scellé le {HEURE} (`date -u`) ; aucun commit, aucune poussée (section « Contre-lecture »)."))

PROPRES.append(("statut",
    "**Statut.** Brouillon 4, **contre-lu trois fois** (tours 1 à 3, corrections appliquées, section « Contre-lecture ») ; **non scellé",
    "**Statut.** Brouillon 5, **contre-lu quatre fois** (tours 1 à 4, corrections appliquées, section « Contre-lecture ») ; **non scellé"))

PROPRES.append(("statut-tour",
    "comme texte qui fait foi** (R1, R2) ; tour 4 de contre-lecture à faire.",
    "comme texte qui fait foi** (R1, R2) ; tour 5 de contre-lecture à faire."))

PROPRES.append(("validateur",
    "aucun défaut sur ce brouillon 4 (vérifié avant",
    "aucun défaut sur ce brouillon 5 (vérifié avant"))

PROPRES.append(("contre-lecture-tete",
    "Tours 1 à 3 faits (entrées « Contre-lecture 1 » à « Contre-lecture 3 » ci-dessous)",
    "Tours 1 à 4 faits (entrées « Contre-lecture 1 » à « Contre-lecture 4 » ci-dessous)"))

ANNEXE_12 = (
    "**Point 12 — durées du tour 4 de contre-lecture, à titre d'illustration** (chiffres de la réponse (4) du rapport du tour 4,\n"
    "que ce rapport demande « à refaire par programme et à recopier en annexe »). Programme\n"
    "`docs/notes/organisme-idees-juge-v1/cribles-v1/comptes-crible-v-brouillon5.py`\n"
    f"(`{COMPTES_SHA}`) et sa sortie `comptes-crible-v-brouillon5-sortie.txt`\n"
    f"(`{SORTIE_SHA}`), même dossier, lancés le 16 novembre à 14:32:55 UTC (`date -u`)\n"
    "par `nice -n 19 python3 -I` (Python 3.13.18, bibliothèque standard seule, arithmétique entière). **Les durées sont celles\n"
    "que le rapport suppose** (mise en place 0,5 h ; barrières 100 minutes, ou 160 en variante ; génération 1,0 h à 20 mondes et\n"
    "1,2 h à 24, comptée trois fois ; mesure 1 h ; rapatriement 0,5 h) : **aucune n'est mesurée, aucune ne vient du pilote** ; la\n"
    "table qui fera foi suit la règle de la section « Devis » (« Durée ») sur les durées mesurées au pilote, et celle-ci n'en est\n"
    "qu'une illustration. Plus grande B_a : 1 860 ; 3 720 ; 1 460 ; 2 920 s (N = 20 puis 24, M = 1 puis 2, 100 minutes) et\n"
    "1 680 ; 3 360 ; 1 310 ; 2 620 s (160 minutes) ; le rapport donne 1 859 ; 3 719 ; 1 460 ; 2 920 et 1 679 ; 3 358 ; 1 309 ;\n"
    "2 619 : écarts de 0 à 2 s, d'arrondi. À 100 minutes de barrières et N = 20, B_a = 1 800 s tient encore à M = 1 (16,67 h) ;\n"
    "M = 2 est exigé dès B_a = 2 100 s ; à N = 24, dès B_a = 1 500 s, et « non lançable » dès B_a = 3 000 s. Sortie, recopiée :\n"
    "\n"
    "```\n"
    + sortie_comptes + "\n"
    "```\n"
    "\n"
    "## Citations obligatoires (N-064, N-067)")
PROPRES.append(("annexe-12", "## Citations obligatoires (N-064, N-067)", ANNEXE_12))

CL4 = f"""- **Contre-lecture 4** (tour 4, sur le brouillon 4) : sous-agent neuf du modèle C, qui n'a écrit aucune pièce citée (ni ce
  texte, ni ses brouillons, ni les corrections, ni les rapports des tours 1 à 3) ; lecture de 14:18:01Z à 14:28:41Z. Rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-v-b4-tour1-v1.md`, empreinte
  `{RAPPORT_SHA}` ; brouillon relu : `crible-v-brouillon4.md`, empreinte
  `{SOURCE_SHA}`. Verdict : **corrections** (5 majeures B4-01 à B4-05, 7 mineures B4-06 à B4-12,
  5 remarques facultatives F-1 à F-5) ; aucun « a_refaire » ; application du tour 3 jugée fidèle ; validateur sans défaut.
  - **Vérification préalable de ce rédacteur** : les 18 couples du rapport du tour 3, appliqués par programme au brouillon 3
    et comparés au brouillon 4 (`diff`), ne laissent que les sept couples propres que l'entrée « Contre-lecture 3 » nomme :
    application du tour 3 fidèle, comme le dit le rapport du tour 4.
  - **Application** : par un rédacteur neuf du modèle C (il n'a écrit ni le brouillon 1, ni les brouillons 2 à 4, ni aucun des
    quatre rapports, ni aucune pièce citée), au moyen du programme `appliquer-corrections-crible-v-brouillon5.py` (même
    dossier, empreinte dans son compagnon `.sha256`) : les 21 couples « ancien → nouveau » des corrections B4-01 à B4-12
    (B4-01 à B4-12e) sont lus dans le rapport lui-même et appliqués sans retouche ; chaque « ancien » vérifié présent une
    seule fois dans le brouillon 4 ; aucun chevauchement ; cible neuve ; écriture le {HEURE} (`date -u`). Aucun appel de
    modèle, aucune dépense, aucune machine, aucune donnée lue (rien sous `diag/`, `runs/`, `donnees/` ; relevé de v67 et
    sortie du pilote non ouverts ; issue et taux du pilote non lus).
  - **Écart de rôle à R-2982, déclaré** : R-2982 veut les corrections écrites par le modèle A, et le rapport le redit (« à
    écrire par l'auteur (modèle A) ») ; elles sont appliquées ici par un rédacteur du modèle C, sur consigne de la session
    mère, et les « nouveau » sont ceux du lecteur du tour 4 (modèle C), recopiés sans retouche : à la mère de dire si cela
    suffit ou si un rédacteur du modèle A doit les reprendre.
  - **Réponse point par point** :
    - B4-01 (« réfutée » ou « non éprouvée ») : **acceptée** ; l'issue « V1, V2, V3 vraies » est lue « H-v non éprouvée au
      crible », comme la lecture gelée de H-v et le point 7 de « En dix lignes ».
    - B4-02 (étage 0) : **acceptée**. **Réserve pour le tour 5** : deux actions de la liste d'arrêt ne sont nommées ni parmi
      celles de l'étage 0 ni parmi ses exclusions, « refus avant tout dossier » (relevé de sonde) et « interdit » (dépense sans
      ligne « calcul ») ; toutes deux tombent avant tout appel, sans issue à lire ; les nommer à l'étage 0 serait plus net.
    - B4-03 (dépassement de la réflexion de Pr-1) : **acceptée** (deux couples B4-03a, B4-03b). **Réserves pour le tour 5** :
      les lignes de GO proposées κv1 et κv2 disent « coût au-dessus du pire cas = arrêt » : si la tolérance est retenue à
      l'étape 2, elles devront la dire ; si le X calculé n'excède pas 1, aucune tolérance n'est possible et l'arrêt reste
      (lecture de ce rédacteur, non écrite par le rapport).
    - B4-04 (budget de durée) : **acceptée** (deux couples B4-04a, B4-04b) ; chiffres de la réponse (4) du rapport refaits par
      programme et recopiés à l'annexe A, point 12 (couple propre « annexe-12 »), égaux à 0 à 2 s près, à titre d'illustration
      sur les durées que suppose le rapport. **Réserve pour le tour 5** : la grille de la table (B_a de 1 800 à 3 600 s) ne
      contient pas les B_a de 300 à 1 500 s que permet la règle de B_a (plus long appel répondu du pilote sous 1 000 s) ; la
      table qui fera foi devrait porter aussi la B_a que fixe la règle.
    - B4-05 (règle d'avance du devis refait) : **acceptée** (deux couples B4-05a, B4-05b). **Réserve pour le tour 5** :
      « les montants des lignes de GO … ne changent pas avec le pilote, seulement avec N » laisse de côté la ligne « sonde
      neuve » de la table du devis, qui les porte à 104,39 et 100,28 USD si la sonde est exigée (décision écrite avant le
      scellement, non lue du pilote).
    - B4-06 à B4-12 : **acceptées**, sans retouche (B4-07 et B4-11 : deux couples chacune ; B4-12 : cinq couples, B4-12a à
      B4-12e ; le « 10 bis » de B4-12e est écrit sur sa propre ligne, comme le « \\n » du rapport le veut).
    - Remarques facultatives F-1 à F-5 : **non appliquées** (non exigées ; consigne de ce tour bornée aux corrections) ;
      transmises à la mère (F-2 : règle de pertinence ; F-4 : partie A sans le champ des retenues).
    - Décisions de R-2977 : relues ; archive {{K1}}, mondes séparés, dollars au prix public, lecture de GO-2026-11-15-06 pour
      l'essai, partie A permise et descriptive, 24 mondes sous 0,95, tension avec N-058 à dire à Lazar : présentes dans ce
      texte ; l'entrée de l'ablation aux critères gelés n'est tranchée par R-2977 que pour (iii) (point 10 bis, défaut (a)).
      Avec B4-12, les points 1, 7, 8, 10 et 10 bis portent une recommandation ; que R-2977 (« recommandations de l'auteur sauf
      mention ») vaille déjà pour les points 1 et 3 reste à confirmer par la mère (point pour la mère 8 du rapport).
    - « Points pour la mère » 1 à 10 du rapport : transmis, non tranchés ici (24 mondes sans gain de puissance, recommandation
      (b) du lecteur, N = 20 dans tous les cas ; le crible éprouve surtout l'ablation, F-2 ; étage 5, point 10 bis ; date de
      lancement ; enveloppe des cinq cribles ; partie A et liste des retenues, F-4 ; R-2977 et points ouverts ; ce que rend le
      lecteur du pilote ; le point 10 est fait par cette entrée).
    - Couples propres de ce tour : « titre » (brouillon 5) ; « en-tete » (ligne « Brouillon 5 » de l'en-tête) ; « statut » et
      « statut-tour » ; « validateur » ; « contre-lecture-tete » (tours 1 à 4) ; « annexe-12 » (durées du tour 4, par
      programme) ; « contre-lecture-4 » (cette entrée). Aucun ne touche un critère, un seuil, une graine ni une ligne d'arrêt.
  - **Rôles** : le lecteur du tour 5 doit être neuf : ni le lecteur du tour 4, ni ce rédacteur, ni les lecteurs et rédacteurs
    des tours 1 à 3, ni l'auteur du brouillon 1. Les corrections touchent des textes gelés (étage 0, ligne « coût d'un appel »
    de la liste d'arrêt, étape 2, section « Devis ») : le tour 5 devrait relire au moins ces endroits (point pour la mère 1 du
    rapport). **Fichiers à donner en plus au tour 5** : le rapport du tour 4, le programme
    `appliquer-corrections-crible-v-brouillon5.py`, le programme `comptes-crible-v-brouillon5.py` et sa sortie (annexe A,
    point 12), avec le brouillon 4 pour la comparaison.

## Annexe A — comptes exacts (sans donnée, sans tirage, sans appel)"""
PROPRES.append(("contre-lecture-4", "## Annexe A — comptes exacts (sans donnée, sans tirage, sans appel)", CL4))

# 5. Contrôles et application d'un coup sur la pièce de départ.
tous = couples + PROPRES
places = []
for nom, ancien, nouveau in tous:
    n = texte.count(ancien)
    if n != 1:
        arret(f"{nom} : « ancien » présent {n} fois dans la pièce de départ")
    i = texte.index(ancien)
    places.append((i, i + len(ancien), nom, nouveau))
places.sort()
for a, b in zip(places, places[1:]):
    if a[1] > b[0]:
        arret(f"chevauchement : {a[2]} et {b[2]}")
morceaux, curseur = [], 0
for debut, fin, nom, nouveau in places:
    morceaux.append(texte[curseur:debut])
    morceaux.append(nouveau)
    curseur = fin
morceaux.append(texte[curseur:])
cible = "".join(morceaux)
for nom, ancien, nouveau in tous:
    if nouveau not in cible:
        arret(f"{nom} : « nouveau » absent de la cible")

# 6. Écriture (mode « x » : jamais d'écrasement).
with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(cible)
print(f"écrit : {CIBLE} ; {len(couples)} couples du rapport, {len(PROPRES)} couples propres ; heure {HEURE}")
print(sha(CIBLE))

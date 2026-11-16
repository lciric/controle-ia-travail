"""Brouillon 9 du préenregistrement du crible (v) : corrections du tour 8 de contre-lecture.

Couples « ancien → nouveau » :
  (1) les 2 couples des corrections C8-01 et C8-02, lus dans le rapport de contre-lecture lui-même (bloc entre clôtures
      nommé `C8-…`, ligne « ANCIEN: » puis ligne « NOUVEAU: »), appliqués sans retouche ;
  (2) des couples propres (titre, en-tête, statut, validateur, tête de la section « Contre-lecture », entrée
      « Contre-lecture 8 »), demandés par C8-03 du rapport.
Les décisions de la mère (ligne R-2992 de `registres/decisions.md`) sont déjà appliquées dans le brouillon 8 : ce programme
vérifie leur présence (gardes de présence, avant et après) et ne les touche pas.
Tous les couples sont déclarés dans l'entrée « Contre-lecture 8 » de la cible.
Gardes : empreinte de la pièce de départ et du rapport ; 2 couples exactement dans le rapport, noms attendus ; aucun
« ancien » ni « nouveau » du rapport sur plusieurs lignes ; chaque « ancien » figure exactement une fois dans la pièce de
départ ; aucun chevauchement entre « anciens » ; tous les couples appliqués d'un coup sur la pièce de départ ; chaque
« nouveau » présent dans la cible ; la cible ne doit pas exister (ouverture en mode « x ») ; aucun repli silencieux.
Bibliothèque standard seule ; aucun appel, aucune donnée.
Usage : python3 -I appliquer-corrections-crible-v-brouillon9.py [--essai DOSSIER]
  (--essai : écrit la cible dans DOSSIER, dossier de travail jetable, pour la contrôler avant l'écriture réelle)
"""
import hashlib
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ICI, "crible-v-brouillon8.md")
SOURCE_SHA = "8047040ba7b8268ac26e20a41406a71fa72e474ca303e9e60e1c686a55153d82"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-v-b7-tour2-v1.md")
RAPPORT_SHA = "b41f7124a48ed8815907a984e8c07c0466924f56fe75f2e85be210a284904206"
NOM_CIBLE = "crible-v-brouillon9.md"
NOMS_RAPPORT = ["C8-01", "C8-02"]

# Décisions de la mère (R-2992) déjà appliquées au brouillon 8 : présence exigée, une fois au moins, avant et après.
PRESENCES_R2992 = [
    "N = 20 dans tous les cas, gelé dès ce texte",
    "| 5 | ablation, QO1 : W_B, L_B, S_B et leurs intervalles | **rapportés, sans verdict**",
    "champ des « retenues » non lu : décision de la mère, R-2992",
    "aucun point ouvert)",
    "corrigé d'après R-2992, point 0",
    "la ligne κv2 (part hors crédits, celle de Pr-1) le dit",
    "qui reçoit pour Pr-1 la tolérance de la réflexion si la règle de la ligne « coût d'un appel » de la liste d'arrêt la retient",
]


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
for chemin, attendu in ((SOURCE, SOURCE_SHA), (RAPPORT, RAPPORT_SHA)):
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

for p in PRESENCES_R2992:
    if p not in texte:
        arret(f"décision de R-2992 absente du brouillon 8 : {p!r}")

# 2. Couples du rapport, sans retouche.
blocs = re.findall(r"^`(C8-[0-9a-z]+)`\n```\nANCIEN: (.*?)\nNOUVEAU: (.*?)\n```", rapport, re.S | re.M)
if [b[0] for b in blocs] != NOMS_RAPPORT:
    arret(f"couples du rapport inattendus : {[b[0] for b in blocs]!r}")
couples = []
for nom, ancien, nouveau in blocs:
    if "\n" in ancien or "\n" in nouveau:
        arret(f"{nom} : ancien ou nouveau sur plusieurs lignes")
    couples.append((nom, ancien, nouveau))

# 3. Heure lue par `date -u`.
HEURE = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], check=True, capture_output=True, text=True).stdout.strip()
if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", HEURE):
    arret(f"heure illisible : {HEURE!r}")

# 4. Couples propres.
P = []


def propre(nom, ancien, nouveau):
    P.append((nom, ancien, nouveau))


propre("titre",
       "(regroupement, sans juge) — brouillon 8\n",
       "(regroupement, sans juge) — brouillon 9\n")

propre("en-tete",
       "  aucun identifiant de modèle dans ce texte pour ce tour), écrit et scellé le 2026-11-16T15:22:15Z (`date -u`) ; "
       "aucun commit, aucune poussée\n  (section « Contre-lecture »).\n",
       "  aucun identifiant de modèle dans ce texte pour ce tour), écrit et scellé le 2026-11-16T15:22:15Z (`date -u`) ; "
       "aucun commit, aucune poussée\n  (section « Contre-lecture »).\n"
       "- Brouillon 9 : corrections du tour 8 de contre-lecture appliquées par un rédacteur neuf (il n'a écrit ni le "
       "brouillon 1,\n"
       "  ni les brouillons 2 à 8, ni aucun des huit rapports, ni aucune pièce citée ; son modèle est dit à la session mère "
       "seulement,\n"
       f"  aucun identifiant de modèle dans ce texte pour ce tour), écrit et scellé le {HEURE} (`date -u`) ; aucun commit, "
       "aucune poussée\n"
       "  (section « Contre-lecture »).\n")

propre("statut",
       "**Statut.** Brouillon 8, **contre-lu sept fois** (tours 1 à 7, corrections appliquées, section « Contre-lecture ») ; "
       "**non scellé\ncomme texte qui fait foi** (R1, R2) ; contrôle des couples du tour 7 (différentiel limité aux endroits "
       "touchés, plus l'entrée « Contre-lecture 7 ») à faire\navant scellement (point pour la mère 1 du rapport du tour 7).",
       "**Statut.** Brouillon 9, **contre-lu huit fois** (tours 1 à 8, corrections appliquées, section « Contre-lecture ») ; "
       "**non scellé\ncomme texte qui fait foi** (R1, R2) ; contrôle des couples du tour 8 (différentiel limité aux endroits "
       "touchés, C8-01 et C8-02, plus l'entrée « Contre-lecture 8 ») à faire\navant scellement (point pour la mère 3 du "
       "rapport du tour 8).")

propre("validateur",
       "aucun défaut sur ce brouillon 8 (vérifié avant",
       "aucun défaut sur ce brouillon 9 (vérifié avant")

propre("contre-lecture-tete",
       "Tours 1 à 7 faits (entrées « Contre-lecture 1 » à « Contre-lecture 7 » ci-dessous)",
       "Tours 1 à 8 faits (entrées « Contre-lecture 1 » à « Contre-lecture 8 » ci-dessous)")

ENTREE_8 = f"""
- **Contre-lecture 8** (tour 8, sur le brouillon 8) : sous-agent neuf, d'un autre modèle que l'auteur, qui n'a écrit aucune
  pièce citée (ni ce texte, ni ses brouillons, ni les corrections, ni les rapports des tours 1 à 7) ; lecture de 15:25Z à
  15:30Z. Rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-v-b7-tour2-v1.md`, empreinte
  `{RAPPORT_SHA}` ; brouillon relu : `crible-v-brouillon8.md`, empreinte
  `{SOURCE_SHA}`. Verdict : **corrections** (1 majeure C8-01, 2 mineures C8-02 et C8-03,
  2 remarques facultatives F-B8-1 et F-B8-2) ; aucun « a_refaire » ; application du tour 7 jugée fidèle (17 zones du
  `diff`, toutes expliquées) ; validateur sans défaut.
  - **Vérification préalable de ce rédacteur** : les 12 couples B7 du rapport du tour 7, extraits par programme et comptés
    sur les brouillons 7 et 8 : chaque « ancien » présent une fois dans le brouillon 7 et absent du brouillon 8, chaque
    « nouveau » présent une fois dans le brouillon 8 ; `diff` du brouillon 7 au brouillon 8 relu (17 zones : les 12 couples
    et les six couples propres nommés dans l'entrée « Contre-lecture 7 ») : application fidèle, comme le dit le rapport.
    Décisions de R-2992 (N = 20 dans tous les cas ; étage 5 rapporté sans verdict, hors des critères gelés ; partie A sans
    le champ des « retenues » de v67 ; points ouverts de « Choix et doutes » à la recommandation écrite ; mentions fausses de
    rédacteur corrigées ; tolérance de la réflexion de Pr-1 sur la seule ligne κv2) : présentes dans le brouillon 8 (gardes
    de présence du programme de ce tour), inchangées par ce tour.
  - **Application** : par un rédacteur neuf (il n'a écrit ni le brouillon 1, ni les brouillons 2 à 8, ni aucun des huit
    rapports, ni aucune pièce citée), au moyen du programme `appliquer-corrections-crible-v-brouillon9.py` (même dossier,
    empreinte dans son compagnon `.sha256`) : les 2 couples « ancien → nouveau » des corrections C8-01 et C8-02 sont lus
    dans le rapport lui-même et appliqués sans retouche ; chaque « ancien » vérifié présent une seule fois dans le
    brouillon 8 ; aucun chevauchement ; cible neuve ; écriture le {HEURE} (`date -u`). Aucun appel de modèle, aucune
    dépense, aucune machine, aucune donnée lue (rien sous `diag/`, `runs/`, `donnees/` ; relevé de v67 et sortie du pilote
    non ouverts ; issue et taux du pilote non lus).
  - **Réponse point par point** :
    - C8-01 (essai sain et artefact de la ligne d'arrêt « fournisseur abandonné… », R5) : **acceptée**, sans retouche :
      essai sain = panne de relais d'un appel d'un fournisseur ayant déjà répondu à un appel, minimum encore possible (le
      crible continue, appels restants de ce fournisseur « échec » sans être lancés) ; artefacts = panne de relais du tout
      premier appel d'un fournisseur (arrêt) et panne d'un fournisseur au monde 3 simulée de sorte que le minimum de mondes
      complets devienne impossible (arrêt). La réserve du rédacteur du tour 7 sur cette ligne est ainsi levée. Relu sur
      [PILOTE] (`8aa33014…`, liste d'arrêt, « Panne d'un relais ») : la règle d'abandon citée est celle du pilote.
    - C8-02 (hypothèses de la grille de l'annexe A, point 11) : **acceptée**, sans retouche : la section « Taille » dit que
      la grille suppose des appels indépendants et ne compte pas l'abandon d'un fournisseur après une seule panne de relais,
      la probabilité d'aller au terme étant plus basse, non chiffrée ici.
    - C8-03 (entrée « Contre-lecture 8 ») : **faite** par cette entrée et les couples propres ci-dessous, avec les deux
      empreintes entières (rapport, lue dans son compagnon `.sha256` et recalculée ; brouillon 8 relu) ; le lecteur y est
      dit « d'un autre modèle que l'auteur », sans identifiant de modèle (consigne de ce tour).
    - Remarques facultatives F-B8-1 (ligne d'arrêt « fournisseur sans aucun appel répondu après les trois premiers
      mondes ») et F-B8-2 (F-B7-1 à F-B7-6 restées ouvertes) : **non appliquées** (non exigées ; consigne de ce tour bornée
      aux corrections et aux décisions de la mère) ; transmises à la mère.
    - « Points pour la mère » 1 à 3 du rapport : transmis, non tranchés ici (règle d'abandon du pilote, une panne passagère
      au premier appel d'une voie terminant le crible à l'étage 1, une reprise demandant un mot avant scellement ;
      enveloppe, 204,67 USD au pire, cumul des cinq cribles à refaire avant toute ligne « calcul », R-2992 point 3 ;
      scellement après un tour différentiel limité à C8-01, C8-02 et cette entrée).
    - Décisions de la mère (R-2992, relue), redemandées par la consigne de ce tour : N = 20 mondes dans tous les cas (règle
      « 24 si le taux est sous 0,95 » de R-2977 retirée) ; étage 5 (ablation) rapporté sans verdict, hors des critères gelés
      (N-045 point 3) ; partie A : archive de la génération 2 construite sans lire le champ des « retenues » de v67
      (remarque F-4 du tour 4) ; points ouverts de « Choix et doutes » à la recommandation écrite ; mentions de rédacteur
      « modèle C » corrigées (correcteurs du modèle A, vérifié par la mère) ; tolérance de la réflexion de Pr-1 écrite sur la
      seule ligne de GO de Pr-1 (κv2) : **déjà présentes** dans le brouillon 8 (gardes de présence), rien à changer ; aucune
      mention fausse de rédacteur ne reste (les mentions « modèle C » restantes désignent des lecteurs). Décisions de R-2977
      (archive {{K1}}, mondes séparés, dollars au prix public, GO-2026-11-15-06 pour l'essai et non pour l'adoption, partie A
      descriptive sur données déjà vues, tension avec N-058 à dire à Lazar) : présentes, inchangées.
    - Lecture déclarée de ce rédacteur : la ligne R-2981 du registre des décisions, lue sur consigne, porte des comptes de
      marche du pilote MR-2 (non son issue ni son taux par appel) ; ils n'entrent en rien dans ce texte.
    - Couples propres de ce tour : « titre » (brouillon 9) ; « en-tete » (ligne « Brouillon 9 » de l'en-tête) ; « statut » ;
      « validateur » ; « contre-lecture-tete » (tours 1 à 8) ; « contre-lecture-8 » (cette entrée). Aucun ne touche un
      critère, un seuil, une graine ni une ligne d'arrêt ; le couple du rapport C8-01 touche la liste d'arrêt (essai sain et
      artefact d'une ligne, R5), C8-02 la section « Taille » (phrase d'information), sur demande du rapport.
  - **Rôles** : R-2982 veut les corrections écrites par le modèle de l'auteur ; ce rédacteur a reçu sa consigne d'un script
    de la session mère, qui sait sous quel modèle il a été servi et dit si R-2982 est tenue (aucun identifiant de modèle
    dans ce texte pour ce tour). Le contrôle suivant doit être fait par un lecteur neuf : ni le lecteur du tour 8, ni ce
    rédacteur, ni les lecteurs et rédacteurs des tours 1 à 7, ni l'auteur du brouillon 1. **Fichiers à lui donner** : ce
    texte, le brouillon 8 pour la comparaison, le rapport du tour 8, le programme
    `appliquer-corrections-crible-v-brouillon9.py`, la ligne R-2992 de `registres/decisions.md`, [PILOTE] (liste d'arrêt,
    « Panne d'un relais »).
"""

propre("contre-lecture-8",
       "    `registres/decisions.md`, [PILOTE] (liste d'arrêt, « Panne d'un relais »).\n"
       "\n## Annexe A — comptes exacts",
       "    `registres/decisions.md`, [PILOTE] (liste d'arrêt, « Panne d'un relais »).\n"
       + ENTREE_8 +
       "\n## Annexe A — comptes exacts")

# 5. Gardes : chaque « ancien » une seule fois ; aucun chevauchement ; application d'un coup.
tous = couples + P
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
for debut, fin, nom, nouveau in places:
    morceaux.append(texte[pos:debut])
    morceaux.append(nouveau)
    pos = fin
morceaux.append(texte[pos:])
cible = "".join(morceaux)

for nom, ancien, nouveau in tous:
    if nouveau not in cible:
        arret(f"{nom} : « nouveau » absent de la cible")
for nom, ancien, nouveau in couples:
    if cible.count(ancien) != sum(nv.count(ancien) for _, _, nv in tous):
        arret(f"{nom} : « ancien » resté dans la cible hors des « nouveau »")
for p in PRESENCES_R2992:
    if p not in cible:
        arret(f"décision de R-2992 perdue dans la cible : {p!r}")

# 6. Écriture, sans écraser.
with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(cible)
print(f"écrit : {CIBLE}")
print(f"heure : {HEURE}")
print(f"couples du rapport : {len(couples)} ; couples propres : {len(P)}")
print(f"empreinte : {sha(CIBLE)}")

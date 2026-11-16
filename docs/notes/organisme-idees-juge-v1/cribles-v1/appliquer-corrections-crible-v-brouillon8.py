"""Brouillon 8 du préenregistrement du crible (v) : corrections du tour 7 de contre-lecture.

Couples « ancien → nouveau » :
  (1) les 12 couples des corrections B7-01 à B7-05 (B7-01a, B7-01b, B7-02a, B7-02b, B7-03a à B7-03e, B7-04, B7-05a,
      B7-05b), lus dans le rapport de contre-lecture lui-même (bloc entre clôtures nommé `B7-…`, ligne « ANCIEN: » puis
      ligne « NOUVEAU: »), appliqués sans retouche ;
  (2) des couples propres (titre, en-tête, statut, validateur, tête de la section « Contre-lecture », entrée
      « Contre-lecture 7 »), demandés par B7-06 du rapport.
Les décisions de la mère (ligne R-2992 de `registres/decisions.md`) sont déjà appliquées dans le brouillon 7 : ce programme
vérifie leur présence (gardes de présence) et ne les touche pas.
Tous les couples sont déclarés dans l'entrée « Contre-lecture 7 » de la cible.
Gardes : empreinte de la pièce de départ et du rapport ; 12 couples exactement dans le rapport, noms attendus ; aucun
« ancien » ni « nouveau » du rapport sur plusieurs lignes ; chaque « ancien » figure exactement une fois dans la pièce de
départ ; aucun chevauchement entre « anciens » ; tous les couples appliqués d'un coup sur la pièce de départ ; chaque
« nouveau » présent dans la cible ; la cible ne doit pas exister (ouverture en mode « x ») ; aucun repli silencieux.
Bibliothèque standard seule ; aucun appel, aucune donnée.
Usage : python3 -I appliquer-corrections-crible-v-brouillon8.py [--essai DOSSIER]
  (--essai : écrit la cible dans DOSSIER, dossier de travail jetable, pour la contrôler avant l'écriture réelle)
"""
import hashlib
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ICI, "crible-v-brouillon7.md")
SOURCE_SHA = "083a322de48bc12d1ac250d8687f304dcf876bfcfd557bd84e154d7321a232b1"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-v-b7-tour1-v1.md")
RAPPORT_SHA = "7dd672353ce772bd4a80bfeba8030cad83eb410ecd6df0156183643415f14347"
NOM_CIBLE = "crible-v-brouillon8.md"
NOMS_RAPPORT = ["B7-01a", "B7-01b", "B7-02a", "B7-02b", "B7-03a", "B7-03b", "B7-03c", "B7-03d", "B7-03e", "B7-04",
                "B7-05a", "B7-05b"]

# Décisions de la mère (R-2992) déjà appliquées au brouillon 7 : présence exigée, une fois au moins, avant et après.
PRESENCES_R2992 = [
    "N = 20 dans tous les cas, gelé dès ce texte",
    "| 5 | ablation, QO1 : W_B, L_B, S_B et leurs intervalles | **rapportés, sans verdict**",
    "champ des « retenues » non lu : décision de la mère, R-2992",
    "aucun point ouvert)",
    "corrigé d'après R-2992, point 0",
    "la ligne κv2 (part hors crédits, celle de Pr-1) le dit",
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
        arret(f"décision de R-2992 absente du brouillon 7 : {p!r}")

# 2. Couples du rapport, sans retouche.
blocs = re.findall(r"^`(B7-[0-9a-z]+)`\n```\nANCIEN: (.*?)\nNOUVEAU: (.*?)\n```", rapport, re.S | re.M)
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
       "(regroupement, sans juge) — brouillon 7\n",
       "(regroupement, sans juge) — brouillon 8\n")

propre("en-tete",
       "  ni aucune pièce citée), écrit et scellé le 2026-11-16T15:01:28Z (`date -u`) ; aucun commit, aucune poussée "
       "(section « Contre-lecture »).\n",
       "  ni aucune pièce citée), écrit et scellé le 2026-11-16T15:01:28Z (`date -u`) ; aucun commit, aucune poussée "
       "(section « Contre-lecture »).\n"
       "- Brouillon 8 : corrections du tour 7 de contre-lecture appliquées par un rédacteur neuf (il n'a écrit ni le "
       "brouillon 1,\n"
       "  ni les brouillons 2 à 7, ni aucun des sept rapports, ni aucune pièce citée ; son modèle est dit à la session mère "
       "seulement,\n"
       f"  aucun identifiant de modèle dans ce texte pour ce tour), écrit et scellé le {HEURE} (`date -u`) ; aucun commit, "
       "aucune poussée\n"
       "  (section « Contre-lecture »).\n")

propre("statut",
       "**Statut.** Brouillon 7, **contre-lu six fois** (tours 1 à 6, corrections appliquées, section « Contre-lecture ») ; "
       "**non scellé\ncomme texte qui fait foi** (R1, R2) ; contrôle des couples du tour 6 et des décisions de R-2992 "
       "(différentiel) à faire\navant scellement (point pour la mère 1 du rapport du tour 6).",
       "**Statut.** Brouillon 8, **contre-lu sept fois** (tours 1 à 7, corrections appliquées, section « Contre-lecture ») ; "
       "**non scellé\ncomme texte qui fait foi** (R1, R2) ; contrôle des couples du tour 7 (différentiel limité aux endroits "
       "touchés, plus l'entrée « Contre-lecture 7 ») à faire\navant scellement (point pour la mère 1 du rapport du tour 7).")

propre("validateur",
       "aucun défaut sur ce brouillon 7 (vérifié avant",
       "aucun défaut sur ce brouillon 8 (vérifié avant")

propre("contre-lecture-tete",
       "Tours 1 à 6 faits (entrées « Contre-lecture 1 » à « Contre-lecture 6 » ci-dessous)",
       "Tours 1 à 7 faits (entrées « Contre-lecture 1 » à « Contre-lecture 7 » ci-dessous)")

ENTREE_7 = f"""
- **Contre-lecture 7** (tour 7, sur le brouillon 7) : sous-agent neuf, d'un autre modèle que l'auteur, qui n'a écrit aucune
  pièce citée (ni ce texte, ni ses brouillons, ni les corrections, ni les rapports des tours 1 à 6) et n'a pas touché les
  dossiers du premier lecteur arrêté sur une limite d'usage ; lecture de 15:07:27Z à 15:20Z. Rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-v-b7-tour1-v1.md`, empreinte
  `{RAPPORT_SHA}` ; brouillon relu : `crible-v-brouillon7.md`, empreinte
  `{SOURCE_SHA}`. Verdict : **corrections** (2 majeures B7-01 et B7-02, 4 mineures B7-03 à B7-06,
  6 remarques facultatives F-B7-1 à F-B7-6) ; aucun « a_refaire » ; application du tour 6 et des décisions de R-2977 et de
  R-2992 jugée fidèle ; validateur sans défaut.
  - **Vérification préalable de ce rédacteur** : les 7 couples D6 du rapport du tour 6, extraits par programme et comptés
    sur les brouillons 6 et 7 : D6-01, D6-03, D6-04a et D6-06, « ancien » absent du brouillon 7 et « nouveau » présent une
    fois ; D6-04b, « nouveau » présent, son « ancien » restant en préfixe ; D6-02 et D6-05, « nouveau » retouché, retouches
    déclarées dans l'entrée « Contre-lecture 6 » (N = 20 seul ; branche à 24 mondes retirée, sonde neuve exigée,
    « ci-dessus ») ; `diff` du brouillon 6 au brouillon 7 relu : application fidèle, comme le dit le rapport. Décisions de
    R-2992 (N = 20 dans tous les cas ; étage 5 rapporté sans verdict, hors des critères gelés ; partie A sans le champ des
    « retenues » de v67 ; points ouverts de « Choix et doutes » à la recommandation écrite, donc sonde neuve exigée ;
    mentions fausses de rédacteur corrigées ; tolérance de la réflexion de Pr-1 sur la seule ligne κv2) : présentes dans le
    brouillon 7 (gardes de présence du programme de ce tour), inchangées par ce tour.
  - **Application** : par un rédacteur neuf (il n'a écrit ni le brouillon 1, ni les brouillons 2 à 7, ni aucun des sept
    rapports, ni aucune pièce citée), au moyen du programme `appliquer-corrections-crible-v-brouillon8.py` (même dossier,
    empreinte dans son compagnon `.sha256`) : les 12 couples « ancien → nouveau » des corrections B7-01 à B7-05 (B7-01a,
    B7-01b, B7-02a, B7-02b, B7-03a à B7-03e, B7-04, B7-05a, B7-05b) sont lus dans le rapport lui-même et appliqués sans
    retouche ; chaque « ancien » vérifié présent une seule fois dans le brouillon 7 ; aucun chevauchement ; cible neuve ;
    écriture le {HEURE} (`date -u`). Aucun appel de modèle, aucune dépense, aucune machine, aucune donnée lue
    (rien sous `diag/`, `runs/`, `donnees/` ; relevé de v67 et sortie du pilote non ouverts ; issue et taux du pilote non lus).
  - **Réponse point par point** :
    - B7-01 (enveloppe de GO-2026-11-15-06) : **acceptée**, sans retouche (B7-01a, B7-01b) : pire cas de 204,67 USD avec
      la sonde neuve exigée (+ 21,67 sur les 183,00 de [NOTE] ; + 13,60 sans la sonde) ; appartenance à l'enveloppe **non
      acquise** : la ligne « calcul » de ce crible ne s'inscrit que si le cumul des lignes inscrites reste sous 1 275 USD,
      sinon nœud de Lazar (R-2992, point 3, relu).
    - B7-02 (« fournisseur », « abandonné », « perdu en entier ») : **acceptée**, sans retouche (B7-02a, B7-02b) :
      fournisseur = voie de relais à clé commune, trois ; « perdu en entier » = aucun appel répondu parmi tous les appels du
      crible de ses proposeurs ; abandon selon la règle du pilote ([PILOTE], liste d'arrêt, « Panne d'un relais », relue
      sur le texte scellé `8aa33014…`) ; arrêt du crible aussi quand le fournisseur abandonné est perdu en entier.
      **Réserve pour le tour suivant** (relevée par ce rédacteur, non corrigée : « rien d'autre ne change ») : l'essai sain
      et l'artefact de la ligne d'arrêt « fournisseur abandonné… » ne sont pas réécrits par le couple ; sous la règle
      nouvelle, l'artefact « panne de tous les appels d'un fournisseur au monde 3 : arrêt » ne fait arrêter que si ce
      fournisseur n'a répondu à aucun appel avant (la perte d'un seul fournisseur laisse le minimum possible, chaque moitié
      gardant un proposeur), et l'essai sain « panne d'un appel : le crible continue » ne vaut que si le fournisseur a déjà
      répondu ; un essai par branche (abandonné sans appel répondu : arrêt ; abandonné après un appel répondu, minimum
      encore possible : le crible continue, appels restants « échec ») serait plus net. La fragilité de la règle du pilote
      (une panne passagère abandonne la voie) est le point pour la mère 3 du rapport, non tranché ici.
    - B7-03 (compte de la configuration de Pr-1) : **acceptée**, sans retouche (cinq couples B7-03a à B7-03e) ;
      arithmétique refaite par ce rédacteur : 0,35 à 0,45 × 5 = 1,75 à 2,25 USD par appel, 35 à 45 pour 20 appels ; total
      107,95 à 128,75 ; part sur crédits 36,7 à 38,2 % : égaux au rapport.
    - B7-04 (« presque sûrement atteint ») : **acceptée**, sans retouche ; chiffres égaux à la sortie recopiée de l'annexe
      A, point 11 (sortie 4 : 0,7481 ; 0,9147 ; 0,9831 ; 0,9985).
    - B7-05 (mécanisme de gel de l'étape 2) : **acceptée**, sans retouche (B7-05a, B7-05b) : la ligne « coût d'un appel »
      est nommée comme seule exception au gel de la liste d'arrêt, dans les limites de sa règle écrite d'avance ; le texte
      refait cite l'empreinte entière du présent texte tel que scellé comme pièce de travail et liste un à un ses écarts.
    - B7-06 (entrée « Contre-lecture 7 ») : **faite** par cette entrée et les couples propres ci-dessous ; le lecteur y est
      dit « d'un autre modèle que l'auteur », sans identifiant de modèle (consigne de ce tour : aucun identifiant de modèle).
    - Remarques facultatives F-B7-1 à F-B7-6 : **non appliquées** (non exigées ; consigne de ce tour bornée aux
      corrections) ; transmises à la mère (F-B7-1 : V4 à écrire en mesure rapportée ; F-B7-2 : risque « non lançable » ;
      F-B7-3 : archive « toutes les cartes de la génération précédente » contre la tension avec N-058 ; F-B7-4 : aucune règle
      de lancer selon la probabilité d'atteindre le minimum ; F-B7-5 : programmes et sorties de l'annexe A à déposer sous
      `cribles-v1/` ; F-B7-6 : reprises des tours précédents).
    - « Points pour la mère » 1 à 7 du rapport : transmis, non tranchés ici (scellement après un tour limité aux endroits
      touchés ; enveloppe, 204,67 USD au pire, cumul des cinq cribles à refaire avant toute inscription ; règle d'abandon
      d'un fournisseur ; le crible informera surtout sur l'ablation ; date de lancement fixée par le code neuf ; mots à
      fixer après le pilote ; le point 7 est fait par cette entrée). L'incident déclaré par le lecteur (une ligne du
      registre des décisions portant des comptes de marche du pilote, vue sans l'avoir cherchée et non utilisée) est
      transmis à la mère ; ce rédacteur n'a pas lu cette ligne.
    - Couples propres de ce tour : « titre » (brouillon 8) ; « en-tete » (ligne « Brouillon 8 » de l'en-tête) ; « statut » ;
      « validateur » ; « contre-lecture-tete » (tours 1 à 7) ; « contre-lecture-7 » (cette entrée). Aucun ne touche un
      critère, un seuil, une graine ni une ligne d'arrêt ; les couples du rapport B7-02a, B7-02b, B7-05a et B7-05b en
      touchent (minimum, liste d'arrêt, gel de l'étape 2), sur demande du rapport.
  - **Rôles** : R-2982 veut les corrections écrites par le modèle de l'auteur ; ce rédacteur a reçu sa consigne d'un script
    de la session mère, qui sait sous quel modèle il a été servi et dit si R-2982 est tenue (aucun identifiant de modèle
    dans ce texte pour ce tour). Le contrôle suivant doit être fait par un lecteur neuf : ni le lecteur du tour 7, ni ce
    rédacteur, ni les lecteurs et rédacteurs des tours 1 à 6, ni l'auteur du brouillon 1. Les corrections touchent des
    textes gelés (minimum et étage 1 par la définition du fournisseur, liste d'arrêt, gel de l'étape 2, devis) : le contrôle
    devrait relire au moins ces endroits. **Fichiers à lui donner** : ce texte, le brouillon 7 pour la comparaison, le
    rapport du tour 7, le programme `appliquer-corrections-crible-v-brouillon8.py`, la ligne R-2992 de
    `registres/decisions.md`, [PILOTE] (liste d'arrêt, « Panne d'un relais »).
"""

propre("contre-lecture-7",
       "    programme `appliquer-corrections-crible-v-brouillon7.py`, la ligne R-2992 de `registres/decisions.md`.\n"
       "\n## Annexe A — comptes exacts",
       "    programme `appliquer-corrections-crible-v-brouillon7.py`, la ligne R-2992 de `registres/decisions.md`.\n"
       + ENTREE_7 +
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

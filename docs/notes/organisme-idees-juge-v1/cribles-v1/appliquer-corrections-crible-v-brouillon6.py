"""Brouillon 6 du préenregistrement du crible (v) : application des corrections du tour 5 de contre-lecture.

Couples « ancien → nouveau » : les 7 couples des corrections B5-01 à B5-07 sont lus dans le rapport de contre-lecture
lui-même (bloc entre clôtures nommé `B5-…`, ligne « ANCIEN: » puis ligne « NOUVEAU: » ; « \\n » dans un « nouveau » = saut
de ligne, comme le dit le rapport, aucun ici), sans retouche ; s'y ajoutent des couples propres, chacun nommé et déclaré dans
la section « Contre-lecture » de la cible : titre, en-tête, statut (deux couples), validateur, tête de la section
« Contre-lecture », entrée « Contre-lecture 5 ».
Gardes : empreinte de la pièce de départ et du rapport ; 7 couples exactement dans le rapport, noms attendus ; chaque
« ancien » (du rapport et propre) figure exactement une fois dans la pièce de départ ; aucun chevauchement entre « anciens » ;
tous les couples appliqués d'un coup sur la pièce de départ ; chaque « nouveau » présent dans la cible ; la cible ne doit pas
exister (ouverture en mode « x ») ; aucun repli silencieux.
Bibliothèque standard seule ; aucun appel, aucune donnée.
Usage : python3 -I appliquer-corrections-crible-v-brouillon6.py [--essai DOSSIER]
  (--essai : écrit la cible dans DOSSIER, dossier de travail jetable, pour la contrôler avant l'écriture réelle)
"""
import hashlib
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ICI, "crible-v-brouillon5.md")
SOURCE_SHA = "c28731169bb25537441e5b3c8918ad3871f961afa7027e9a57ee432246c70118"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-v-b4-tour2-v1.md")
RAPPORT_SHA = "0152b7f4baceb9d089651287ede102c7bafda05a4c87e92d0aece7efa5207c2a"
NOM_CIBLE = "crible-v-brouillon6.md"
NOMS_RAPPORT = ["B5-01", "B5-02", "B5-03", "B5-04", "B5-05", "B5-06", "B5-07"]


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

# 2. Couples du rapport.
blocs = re.findall(r"^`(B5-[0-9a-z]+)`\n```\nANCIEN: (.*?)\nNOUVEAU: (.*?)\n```", rapport, re.S | re.M)
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
    "(regroupement, sans juge) — brouillon 5",
    "(regroupement, sans juge) — brouillon 6"))

PROPRES.append(("en-tete",
    "  pièce citée), écrit et scellé le 2026-11-16T14:35:02Z (`date -u`) ; aucun commit, aucune poussée (section « Contre-lecture »).",
    "  pièce citée), écrit et scellé le 2026-11-16T14:35:02Z (`date -u`) ; aucun commit, aucune poussée (section « Contre-lecture »).\n"
    "- Brouillon 6 : corrections du tour 5 de contre-lecture appliquées par un rédacteur neuf (modèle C, **écart de rôle à\n"
    "  R-2982, déclaré** ; il n'a écrit ni le brouillon 1, ni les brouillons 2 à 5, ni aucun des cinq rapports, ni aucune\n"
    f"  pièce citée), écrit et scellé le {HEURE} (`date -u`) ; aucun commit, aucune poussée (section « Contre-lecture »)."))

PROPRES.append(("statut",
    "**Statut.** Brouillon 5, **contre-lu quatre fois** (tours 1 à 4, corrections appliquées, section « Contre-lecture ») ; **non scellé",
    "**Statut.** Brouillon 6, **contre-lu cinq fois** (tours 1 à 5, corrections appliquées, section « Contre-lecture ») ; **non scellé"))

PROPRES.append(("statut-tour",
    "comme texte qui fait foi** (R1, R2) ; tour 5 de contre-lecture à faire.",
    "comme texte qui fait foi** (R1, R2) ; tour 6 de contre-lecture à faire."))

PROPRES.append(("validateur",
    "aucun défaut sur ce brouillon 5 (vérifié avant",
    "aucun défaut sur ce brouillon 6 (vérifié avant"))

PROPRES.append(("contre-lecture-tete",
    "Tours 1 à 4 faits (entrées « Contre-lecture 1 » à « Contre-lecture 4 » ci-dessous)",
    "Tours 1 à 5 faits (entrées « Contre-lecture 1 » à « Contre-lecture 5 » ci-dessous)"))

ANCRE_CL5 = "## Annexe A — comptes exacts (sans donnée, sans tirage, sans appel)"
CL5 = f"""- **Contre-lecture 5** (tour 5, sur le brouillon 5) : sous-agent neuf du modèle C, qui n'a écrit aucune pièce citée (ni ce
  texte, ni ses brouillons, ni les corrections, ni les rapports des tours 1 à 4) et n'a lu ni les dossiers ni le rapport du
  premier lecteur (modèle B) ; lecture de 14:36:48Z à 14:45Z. Rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-v-b4-tour2-v1.md`, empreinte
  `{RAPPORT_SHA}` ; brouillon relu : `crible-v-brouillon5.md`, empreinte
  `{SOURCE_SHA}`. Verdict : **corrections** (2 majeures B5-01 et B5-02, 5 mineures B5-03 à B5-07,
  3 remarques facultatives F-B5-1 à F-B5-3) ; aucun « a_refaire » ; application du tour 4 jugée fidèle ; validateur sans défaut.
  - **Vérification préalable de ce rédacteur** : les 21 couples du rapport du tour 4, appliqués par programme au brouillon 4
    et comparés au brouillon 5 (`diff`), ne laissent que les couples propres que l'entrée « Contre-lecture 4 » nomme (titre,
    en-tête, statut et statut-tour, validateur, tête de la section, annexe A point 12, entrée « Contre-lecture 4 ») :
    application du tour 4 fidèle, comme le dit le rapport du tour 5. Les 18 couples du tour 3, rejoués de même sur le
    brouillon 3 et comparés au brouillon 4, ne laissent que les sept couples propres de l'entrée « Contre-lecture 3 ».
  - **Application** : par un rédacteur neuf du modèle C (il n'a écrit ni le brouillon 1, ni les brouillons 2 à 5, ni aucun des
    cinq rapports, ni aucune pièce citée), au moyen du programme `appliquer-corrections-crible-v-brouillon6.py` (même
    dossier, empreinte dans son compagnon `.sha256`) : les 7 couples « ancien → nouveau » des corrections B5-01 à B5-07
    sont lus dans le rapport lui-même et appliqués sans retouche ; chaque « ancien » vérifié présent une seule fois dans le
    brouillon 5 ; aucun chevauchement ; cible neuve ; écriture le {HEURE} (`date -u`). Aucun appel de modèle, aucune
    dépense, aucune machine, aucune donnée lue (rien sous `diag/`, `runs/`, `donnees/` ; relevé de v67 et sortie du pilote
    non ouverts ; issue et taux du pilote non lus).
  - **Écart de rôle à R-2982, déclaré** : R-2982 veut les corrections écrites par le modèle A, et le rapport le redit (« à
    écrire par l'auteur (modèle A, R-2982) ») ; elles sont appliquées ici par un rédacteur du modèle C, sur consigne de la
    session mère, et les « nouveau » sont ceux du lecteur du tour 5 (modèle C), recopiés sans retouche : à la mère de dire si
    cela suffit ou si un rédacteur du modèle A doit les reprendre (point pour la mère 2 du rapport).
  - **Réponse point par point** :
    - B5-01 (budget de durée) : **acceptée**, sans retouche : les cinq termes autres que les appels sont fixés par une règle
      écrite maintenant, leurs nombres s'écrivant dans le texte qui fera foi d'après le pilote ; barrières 100 minutes (phrase
      bornée à 60 minutes par la machine, la mère en promettant 30, [PROC-14] § 0, relu) ; mondes lents comptés dans la
      génération ; mesure rapportée à N mondes, plus l'énumération exacte du placebo mesurée par programme avant le
      scellement ; le renvoi aux « 2 h 40 » disparaît.
    - B5-02 (tolérance de la réflexion de Pr-1) : **acceptée**, sans retouche : tolérance seulement si le plus grand rapport
      mesuré au pilote dépasse 1 ; essai sain et artefact de la branche tolérée, passés avant l'addendum ; lignes κv1 et κv2
      à dire en ce cas. Les lignes de GO proposées ne sont pas réécrites ici (aucun couple ne les porte ; elles le seront dans
      le texte qui fera foi si la tolérance est retenue).
    - B5-03 (étage 0, deux actions sans case) : **acceptée**.
    - B5-04 (B_a hors grille) : **acceptée**.
    - B5-05 (montants des lignes de GO et sonde neuve) : **acceptée**.
    - B5-06 (durée de la machine dans l'attendu) : **acceptée**.
    - B5-07 (sens de l'erreur de l'illustration de l'annexe A, point 12) : **acceptée**.
    - Remarques facultatives F-B5-1 à F-B5-3 : **non appliquées** (non exigées ; consigne de ce tour bornée aux corrections) ;
      transmises à la mère (F-B5-1 : risque d'arrêt de Pr-1 non chiffré ; F-B5-2 : F-1, F-2 et F-4 du tour 4 ; F-B5-3 : seuil
      sur k_R quand n_c vaut 16 à 19).
    - **Réserves pour le tour 6** (relevées par ce rédacteur à la relecture entière, non corrigées : « rien d'autre ne
      change ») : (1) B5-01 lit au pilote les durées de mise en place, de mesure et de rapatriement, que la liste des « Points
      à remesurer » (section « Devis », points (2) et (7)) ne nomme pas ; (2) l'étape 2 des « Étapes » ne nomme pas la mesure
      par programme de la durée de l'énumération exacte du placebo que B5-01 exige avant le scellement (processeur seul,
      sans dépense) ; (3) B5-06 dit les appels « à ⌈N/M⌉ fois leur durée relevée au pilote » sans dire laquelle (moyenne, ou
      plus long des quatre appels d'un monde, par monde) : un choix resterait ouvert après lecture du pilote.
    - Décisions de R-2977 : relues ; archive {{K1}}, mondes séparés, dollars au prix public, lecture de GO-2026-11-15-06 pour
      l'essai, partie A permise et descriptive, 24 mondes sous 0,95, tension avec N-058 à dire à Lazar : présentes dans ce
      texte, inchangées par ce tour.
    - « Points pour la mère » 1 à 9 du rapport : transmis, non tranchés ici (scellement après un tour 6 limité aux endroits
      touchés ; rôles des modèles A et C ; 24 mondes sans gain de puissance, N = 20 recommandé par le lecteur, écart à R-2977 ;
      date de lancement fixée par le code neuf, M = 2 si le plus long appel répondu du pilote dépasse 1 200 s ; tolérance de
      Pr-1 et risque non chiffré ; étage 5, point 10 bis, à trancher avant le scellement ; points 1, 3, 7, 8, 10 et 10 bis de
      « Choix et doutes » ; enveloppe des cinq cribles et champs permis au lecteur du pilote ; le point 9 est fait par cette
      entrée).
    - Couples propres de ce tour : « titre » (brouillon 6) ; « en-tete » (ligne « Brouillon 6 » de l'en-tête) ; « statut » et
      « statut-tour » ; « validateur » ; « contre-lecture-tete » (tours 1 à 5) ; « contre-lecture-5 » (cette entrée). Aucun ne
      touche un critère, un seuil, une graine ni une ligne d'arrêt.
  - **Rôles** : le lecteur du tour 6 doit être neuf : ni le lecteur du tour 5, ni ce rédacteur, ni les lecteurs et rédacteurs
    des tours 1 à 4, ni l'auteur du brouillon 1. Les corrections touchent des textes gelés (budget de durée, ligne « coût d'un
    appel » de la liste d'arrêt, étage 0, règle d'avance du devis refait, annexe A point 12) : le tour 6 devrait relire au
    moins ces endroits (point pour la mère 1 du rapport). **Fichiers à donner en plus au tour 6** : le rapport du tour 5, le
    programme `appliquer-corrections-crible-v-brouillon6.py`, avec le brouillon 5 pour la comparaison.

{ANCRE_CL5}"""
PROPRES.append(("contre-lecture-5", ANCRE_CL5, CL5))

# 5. Contrôles : chaque « ancien » une seule fois, aucun chevauchement.
tous = couples + PROPRES
places = []
for nom, ancien, nouveau in tous:
    n = texte.count(ancien)
    if n != 1:
        arret(f"{nom} : « ancien » présent {n} fois dans la pièce de départ")
    debut = texte.index(ancien)
    places.append((debut, debut + len(ancien), nom))
places.sort()
for (d1, f1, n1), (d2, f2, n2) in zip(places, places[1:]):
    if d2 < f1:
        arret(f"chevauchement entre {n1} et {n2}")

# 6. Application d'un coup, de la fin vers le début (positions de la pièce de départ).
par_nom = {nom: (ancien, nouveau) for nom, ancien, nouveau in tous}
cible = texte
for debut, fin, nom in sorted(places, reverse=True):
    cible = cible[:debut] + par_nom[nom][1] + cible[fin:]
for nom, ancien, nouveau in tous:
    if nouveau not in cible:
        arret(f"{nom} : « nouveau » absent de la cible")

# 7. Écriture sans écraser.
with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(cible)
print(f"écrit : {CIBLE}")
print(f"heure : {HEURE}")
print(f"couples du rapport : {len(couples)} ; couples propres : {len(PROPRES)}")
print(f"empreinte : {sha(CIBLE)}")

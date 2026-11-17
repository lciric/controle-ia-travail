"""Brouillon 2 du préenregistrement du crible (i), placebo par monde jumeau : corrections du tour 1 de contre-lecture.

Couples « ancien → nouveau » :
  (1) les 16 couples des corrections M1 à M3 et m1 à m6 du rapport `contre-lecture-crible-i-tour1-v1.md`, recopiés du rapport
      sans retouche (garde : chaque « ancien » et chaque « nouveau » figure dans le rapport lui-même) ;
  (2) une extension de M2 (E1) à la phrase parallèle de « Ce que serait chaque issue (R3) », au même sens, déclarée ;
  (3) des couples propres de forme (P1 à P7 : titre, en-tête, pièces écrites, statut, renvoi du devis, annexe A point 1,
      section « Contre-lecture »), qui renvoient au programme de devis neuf exigé par M3 et à ce tour.
Tous les couples sont déclarés dans l'entrée « Contre-lecture 1 » de la cible.
Gardes : empreinte de la pièce de départ, du rapport et des deux pièces neuves du devis ; chaque « ancien » figure exactement une
fois dans la pièce de départ ; aucun chevauchement entre « anciens » ; tous les couples appliqués d'un coup sur la pièce de
départ ; chaque « nouveau » présent dans la cible ; validateur `controle_ia.prereg.problemes` sans défaut sur la cible, écrite
d'abord dans un dossier temporaire ; la cible ne doit pas exister (ouverture en mode « x ») ; aucun repli silencieux.
Bibliothèque standard et module `controle_ia.prereg` du dépôt ; aucun appel, aucune donnée.
Usage : python3 -I appliquer-corrections-crible-i-brouillon2.py [--essai DOSSIER]
  (--essai : écrit la cible dans DOSSIER, dossier de travail jetable, pour la contrôler avant l'écriture réelle)
"""
import hashlib
import os
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
SOURCE = os.path.join(ICI, "crible-i-brouillon1.md")
SOURCE_SHA = "a3c38ccc460c30958c82eaf92701de94435fafee54a93bba2f1de0bdddebd641"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-i-tour1-v1.md")
RAPPORT_SHA = "bb5829b0f42d96374f9dc02c67cb4a55abc42d7a1b3787db4818cc952a39e782"
DEVIS2 = os.path.join(ICI, "devis-crible-i-brouillon2.py")
DEVIS2_SHA = "945cbbc685888b2e7191b3805443d8d67db0d50e4a34b0988c619772ff037c4a"
SORTIE2 = os.path.join(ICI, "devis-crible-i-brouillon2-sortie.txt")
SORTIE2_SHA = "68042c0925050237e270f550e0fffd769083ec39808fde70f37c284d207f15b6"
NOM_CIBLE = "crible-i-brouillon2.md"


def arret(msg):
    print(f"ARRÊT : {msg}", file=sys.stderr)
    sys.exit(2)


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


# 0. Arguments.
if len(sys.argv) == 1:
    DOSSIER = ICI
elif len(sys.argv) == 3 and sys.argv[1] == "--essai":
    DOSSIER = os.path.abspath(sys.argv[2])
    if DOSSIER == ICI:
        arret("--essai doit viser un dossier jetable, pas le dossier de la pièce")
else:
    arret("usage : appliquer-corrections-crible-i-brouillon2.py [--essai DOSSIER]")
CIBLE = os.path.join(DOSSIER, NOM_CIBLE)
if os.path.exists(CIBLE):
    arret(f"la cible existe déjà : {CIBLE}")

# 1. Empreintes.
for chemin, attendu in ((SOURCE, SOURCE_SHA), (RAPPORT, RAPPORT_SHA), (DEVIS2, DEVIS2_SHA), (SORTIE2, SORTIE2_SHA)):
    if not os.path.isfile(chemin):
        arret(f"pièce absente : {chemin}")
    if sha(chemin) != attendu:
        arret(f"empreinte différente : {chemin}")
with open(SOURCE, encoding="utf-8") as f:
    texte = f.read()
with open(RAPPORT, encoding="utf-8") as f:
    rapport = f.read()

# 2. Heure (date -u), lue au moment de l'écriture, scellement juste après.
HEURE = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True, check=True).stdout.strip()

# 3. Couples du rapport (texte recopié du rapport, sans retouche).
couples = [
    ("M1",
     "**sauf** les lignes « monde remplacé » (dans la limite de 4) et « appel plus long que B_a » (appel compté en échec, lu à l'étage 1)",
     "**sauf** les lignes « monde remplacé » (dans la limite de 4), « appel plus long que B_a » (appel compté en échec, lu à l'étage 1) et « mondes complets + mondes en cours + mondes non commencés < 16 » (lue à l'étage 1 : « non concluant », comme le dit cette ligne)"),
    ("M2a",
     "(c) : « H-i non réfutée au crible, l'information s'ajoutant à un",
     "(c) : « H-i réfutée dans sa seconde clause (la table du jumeau aide aussi) ; sa première clause (l'information) non réfutée au crible, s'ajoutant à un"),
    ("M2b",
     "H-i réfutée au crible (la forme seule suffit)",
     "H-i non soutenue au crible : la forme seule suffit à un effet, l'information n'est pas établie (un crible à 20 mondes ne réfute pas un effet d'information)"),
    ("M3a",
     "pire cas ≈ 11 h à un monde à la fois",
     "pire cas ≈ 12,5 h à un monde à la fois"),
    ("M3b",
     "**M = 1 : 39 600 s = 11,0 h ; M = 2 : 9,3 h**",
     "**M = 1 : 45 000 s = 12,5 h ; M = 2 : 39 000 s = 10,8 h**"),
    ("M3c",
     "budget 11,0 h à M = 1, 9,33 h à M = 2",
     "budget 12,5 h à M = 1, 10,83 h à M = 2 (programme corrigé : `devis-crible-i-brouillon2.py`)"),
    ("m1a",
     "Les colonnes « ce qui la réfute » de I-6 et I-7 sont précisées ici",
     "Les colonnes « ce qui la réfute » de I-5, I-6 et I-7 sont précisées ici"),
    ("m1b",
     "non la zone de réfutation de ces deux lignes)",
     "non la zone de réfutation de ces trois lignes)"),
    ("m2a",
     "I-5 : entre les deux zones ; I-7 : de 0,2 à 0,5",
     "I-5 : entre les deux zones ; I-6 : aucun monde alors que la première conditionnelle est couverte dans TV dans moins de 3 mondes à deux conditionnelles ; I-7 : de 0,2 à 0,5"),
    ("m2b",
     "I-4 : TV − S0 entre 0 et + 0,10 ;",
     "I-4 : TV − S0 entre 0 et + 0,10, ou TV − S0 ≥ + 0,10 avec TJ − S0 hors de 0 à + 0,10 ;"),
    ("m3a",
     "la phrase « effet d'information » est **interdite** (TJ a pu perdre des cartes, ce qui gonfle P1)",
     "les phrases « effet d'information » et « information et forme » sont **interdites** (TJ a pu perdre des cartes, ce qui gonfle P1)"),
    ("m3b",
     "sous « S0 tronqué », la phrase « effet de forme » est interdite",
     "sous « S0 tronqué », les phrases « effet de forme » et « information et forme » sont interdites (S0 a pu perdre des cartes, ce qui gonfle P2)"),
    ("m3c",
     "sous « TV tronqué », la phrase « rien d'établi » est remplacée par « non tranché (TV tronqué) »",
     "sous « TV tronqué », les phrases « rien d'établi » et « effet de forme » sont remplacées par « non tranché (TV tronqué) » (TV a pu perdre des cartes, ce qui dégonfle P1)"),
    ("m4",
     "**Crible d'un grand effet** : « non établi » ne dit rien",
     "**Crible d'un grand effet** : à l'écart que I-1 prédit (+ 4 mondes, par exemple 0,05 → 0,25), la puissance de P1 est d'environ 0,2 (calcul du lecteur, 20 000 tirages, à refaire par un programme scellé) et un écart de comptes de + 4 ne peut jamais atteindre le seuil (il faut au moins + 6) ; « non établi » ne dit rien"),
    ("m5",
     "**Lancé vers 00:49Z, résultat lu après le gel des prédictions** (vers 00:55Z, heure non relevée à la minute)",
     "**Programme et sortie enregistrés à 00:56:09Z (heure des fichiers), après le gel (00:53:43Z) ; résultat lu après le gel des prédictions ; l'heure de lancement (annoncée vers 00:49Z) et celle de la lecture (annoncée vers 00:55Z) ne sont pas vérifiables**"),
    ("m6",
     "(b) « **effet de forme** »",
     "(b) « **effet de forme** (au sens de : effet de la table du jumeau, qui porte aussi l'information sur les autres composantes) »"),
]
if len(couples) != 16:
    arret("16 couples du rapport attendus")
for nom, ancien, nouveau in couples:
    if ancien not in rapport:
        arret(f"{nom} : « ancien » absent du rapport (recopie infidèle)")
    if nouveau not in rapport:
        arret(f"{nom} : « nouveau » absent du rapport (recopie infidèle)")

# 4. Extension de M2 (même sens, phrase parallèle) et couples propres de forme.
CONTRE_LECTURE_ANCIENNE_DEBUT = "## Contre-lecture\n\nAucun tour fait."
debut = texte.index(CONTRE_LECTURE_ANCIENNE_DEBUT)
fin = texte.index("\n## Annexe A")
ANCIENNE_SECTION = texte[debut:fin]

NOUVELLE_SECTION = f"""## Contre-lecture

- **Contre-lecture 1** (R2, tour 1, sur le brouillon 1) — sous-agent neuf, d'un autre modèle que l'auteur, qui n'a écrit ni ce
  texte, ni [NOTE], ni [PILOTE], ni le code du pilote, ni [CRIBLE-III], ni [CRIBLE-V]. Texte relu :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-i-brouillon1.md`,
  `a3c38ccc460c30958c82eaf92701de94435fafee54a93bba2f1de0bdddebd641` ; rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-i-tour1-v1.md`,
  `bb5829b0f42d96374f9dc02c67cb4a55abc42d7a1b3787db4818cc952a39e782`. Verdict : « corrections » (3 majeures, M1 à M3 ;
  6 mineures, m1 à m6 ; remarques facultatives F1 à F8). Corrections appliquées le {HEURE} par un rédacteur neuf, d'un autre
  modèle que l'auteur, qui n'a écrit ni le brouillon 1 ni le rapport, au moyen du programme
  `appliquer-corrections-crible-i-brouillon2.py` (même dossier, scellé à côté) : les 16 couples du rapport, recopiés sans
  retouche (le programme vérifie que chaque « ancien » et chaque « nouveau » figure dans le rapport, et que chaque « ancien »
  figure une seule fois dans le brouillon 1), plus une extension de M2 (E1) et sept couples propres de forme (P1 à P7), déclarés
  ci-dessous. Différentiel : `diff-crible-i-b1-vers-b2.txt` (même dossier, scellé). Rien d'autre ne change.
  **Traitement**, point par point :
  - M1 (liste d'arrêt contre étage 0, ligne « moins de 16 mondes possibles ») : **acceptée**, texte du rapport (étage 0).
  - M2 (H-i et sa lecture) : **acceptée**, texte du rapport (deux couples, « Lecture de H-i »). **Étendue (E1)**, au même sens,
    à la phrase parallèle de « Ce que serait chaque issue (R3) » : « H-i réfutée au crible, H-i-f non réfutée » devient « H-i
    non soutenue au crible (l'information n'est pas établie ; un crible à 20 mondes ne réfute pas un effet d'information), H-i-f
    non réfutée » ; sans elle, le texte se contredirait sur le point même de M2. Seul ajout de fond hors des couples du
    rapport : à contre-lire.
  - M3 (budget de pire cas de la durée) : **acceptée**. Programme neuf `devis-crible-i-brouillon2.py`
    (`945cbbc685888b2e7191b3805443d8d67db0d50e4a34b0988c619772ff037c4a`), copie du brouillon 1 dont seuls l'en-tête et le
    point 5 changent (mise en place et rapatriement à 1 800 s **chacun**, triplés : 3 × (1 800 + 1 800)), lancé le
    2026-11-17T01:31:44Z par `.venv/bin/python -I` ; sortie `devis-crible-i-brouillon2-sortie.txt`
    (`68042c0925050237e270f550e0fffd769083ec39808fde70f37c284d207f15b6`) : M = 1 : 45 000 s = 12,50 h ; M = 2 : 39 000 s =
    10,83 h ; les autres points de la sortie sont égaux à ceux du brouillon 1 (vérifié par `diff` : seules les deux lignes du
    point 5 diffèrent). Les trois couples du rapport sont appliqués (section 0, point 10 ; « Devis », « Durée » ; annexe A,
    point 1) ; le texte garde « 1 800 s chacune », rien n'est changé vers « 1 800 s en tout ». M = 1 reste retenu, sous la
    minuterie de 17 h. Les renvois au programme et à sa sortie (en-tête, « Devis », annexe A, point 1) visent les pièces neuves
    (P3, P5, P6) ; les pièces du brouillon 1 restent intactes et citées comme remplacées.
  - m1 (I-5 ajoutée à la déclaration d'ajout après gel) : **acceptée**, texte du rapport.
  - m2 (zones « indécises » de I-6 et de I-4) : **acceptée**, texte du rapport.
  - m3 (phrases interdites de l'étage 2) : **acceptée**, texte du rapport (trois couples).
  - m4 (puissance à l'écart prédit par I-1) : **acceptée**, texte du rapport (« Taille ») ; le calcul de puissance à + 4 mondes
    (environ 0,19 selon le lecteur, non scellé) reste **à refaire par un programme scellé sous un nom neuf avant la version qui
    fera foi** : non fait ici (hors des couples exigés).
  - m5 (horodatage du calcul synthétique de visibilité) : **acceptée**, texte du rapport ; heures des fichiers revérifiées sur
    disque (gel 00:53:43Z ; programme et sortie de visibilité 00:56:09Z).
  - m6 (étiquette « effet de forme ») : **acceptée**, texte du rapport (étage 3).
  - F1 à F8 (facultatives) : **non appliquées** (aucune correction exigée ; rien d'autre ne change dans ce tour). Restent à
    trancher par l'auteur ou la mère avant la version qui fera foi : F1 (plus petite taille de table à 90 % de visibilité),
    F4 (égalité de coût entre bras : « rapportée seulement », à dire en une phrase), F5 (« mondes séparés » étendu à (i) : choix
    à dire), F7 (mondes exclus rapportés par bras) ; F2, F3, F6 et F8 sont sans effet.
  - Points pour la mère (rapport, § 4) : point 1 fait (M3) ; points 2 (gel à confirmer par une ligne datée de
    `registres/decisions.md`, qui dira que I-1 est gelée avec « ≥ + 4 » même si P1 ne peut l'établir à ce seuil, et que les
    zones de I-5, I-6 et I-7 sont des ajouts postérieurs au gel), 3 (enveloppe), 4, 5 (en-tête de TJ) et 6 (tour différentiel
    par un lecteur neuf) : à la mère, rien dans ce texte.
  - Incident déclaré par le lecteur (rapport, § 5 : lignes R-2994 et R-3001 affichées en partie) : le lecteur dit n'en rien
    avoir utilisé ; le rédacteur de ce brouillon 2 n'a lu ni ces lignes ni la section « Issue » du verdict ; aucune correction
    appliquée ne dépend de l'issue du pilote (toutes portent sur la logique interne du texte ou sur son arithmétique) ; à juger
    par la mère.
  - **Couples propres** (forme seulement) : P1 titre (brouillon 2) ; P2 en-tête (ligne du brouillon 2) ; P3 pièces écrites
    (programme de devis neuf et sa sortie) ; P4 statut et validateur ; P5 renvoi de la section « Devis » ; P6 annexe A, point 1 ;
    P7 cette section.

**À faire** (R2) : tour 2, différentiel (M1 à M3, m1 à m6 et E1 seulement), par un sous-agent neuf d'un **autre modèle** que
l'auteur, qui n'a écrit ni ce texte, ni le rapport du tour 1, ni [NOTE], ni [PILOTE], ni [CRIBLE-III], ni [CRIBLE-V] (de
préférence pas le lecteur du tour 1 : rapport, § 4, point 6). **Fichiers à lui donner explicitement** : ce texte ; le brouillon 1
(`a3c38ccc…`) ; le différentiel `diff-crible-i-b1-vers-b2.txt` ; le rapport du tour 1 (`bb5829b0…`) ; le programme
`appliquer-corrections-crible-i-brouillon2.py` ; `devis-crible-i-brouillon1.py` (`92932a6a…`) et sa sortie (`ef0c36bd…`) ;
`devis-crible-i-brouillon2.py` (`945cbbc6…`) et sa sortie (`68042c09…`) ; le gel des prédictions
`docs/notes/organisme-idees-juge-v1/cribles-v1/gel-predictions-crible-i-brouillon1.txt`
(`727f924f5f77db12ecf558805a1e4f0b5762aa039c1dbe4f101f5172b0ca4648`) ; pour une relecture plus large, la liste donnée au tour 1
(brouillon 1, section « Contre-lecture ») vaut toujours. **Points à lui soumettre en priorité** : l'extension E1 de M2 ; la
cohérence des étages 0 à 3 après M1, M2, m3 et m6 ; le budget de durée corrigé (M3) ; les zones de réfutation et les zones
« indécises » ajoutées après le gel (I-4, I-5, I-6, I-7).
"""

P = [
    ("P1",
     "par sa seule présence ?) — brouillon 1 (variante « crédits de Claude au maximum »)",
     "par sa seule présence ?) — brouillon 2 (variante « crédits de Claude au maximum »)"),
    ("P2",
     "  aucun commit, aucune poussée.\n- **Ordre de rédaction, déclaré**",
     "  aucun commit, aucune poussée.\n"
     f"- **Brouillon 2** (écrit et scellé le {HEURE}, `date -u`) : corrections du tour 1 de contre-lecture appliquées par un\n"
     "  rédacteur neuf, d'un autre modèle que l'auteur, par le programme `appliquer-corrections-crible-i-brouillon2.py` (même\n"
     "  dossier) ; détail et réponse point par point : section « Contre-lecture » ; différentiel `diff-crible-i-b1-vers-b2.txt` ;\n"
     "  rien d'autre ne change. Le reste de cet en-tête est celui du brouillon 1.\n"
     "- **Ordre de rédaction, déclaré**"),
    ("P3",
     "devis\n    `devis-crible-i-brouillon1.py` (`92932a6a8f51aa84dfceeac336750147771e3bf7862d95c8f4a3bee7023fe475`) et sa sortie\n"
     "    `devis-crible-i-brouillon1-sortie.txt` (`ef0c36bdc5b09081f27761afc2e7da9da57f09642863b52c64cd252ebe29405d`) ;",
     "devis\n    `devis-crible-i-brouillon2.py` (`945cbbc685888b2e7191b3805443d8d67db0d50e4a34b0988c619772ff037c4a`) et sa sortie\n"
     "    `devis-crible-i-brouillon2-sortie.txt` (`68042c0925050237e270f550e0fffd769083ec39808fde70f37c284d207f15b6`), écrits pour le\n"
     "    brouillon 2 (correction M3) ; ils remplacent `devis-crible-i-brouillon1.py`\n"
     "    (`92932a6a8f51aa84dfceeac336750147771e3bf7862d95c8f4a3bee7023fe475`) et sa sortie `devis-crible-i-brouillon1-sortie.txt`\n"
     "    (`ef0c36bdc5b09081f27761afc2e7da9da57f09642863b52c64cd252ebe29405d`), gardés intacts ;"),
    ("P4a",
     "**Statut.** Brouillon 1, **non contre-lu** (R2 : contre-lecture à faire, section « Contre-lecture »)",
     "**Statut.** Brouillon 2, **contre-lu au tour 1** (verdict « corrections », corrections appliquées ; tour 2, différentiel, à\n"
     "faire : R2, section « Contre-lecture »)"),
    ("P4b",
     "comme pièce de travail ; la section « Contre-lecture » cite deux empreintes de pièces à donner au lecteur, non un rapport :\n"
     "**aucune contre-lecture n'a eu lieu**).",
     "comme pièce de travail, puis relancé sur ce brouillon 2 avant son scellement : aucun défaut formel ; la section\n"
     "« Contre-lecture » cite le brouillon 1 relu et le rapport du tour 1, avec leurs empreintes)."),
    ("P5",
     "Calculs : `devis-crible-i-brouillon1.py` et sa sortie (annexe A,",
     "Calculs : `devis-crible-i-brouillon2.py` et sa sortie (annexe A,"),
    ("P6",
     "1. **Devis** : `devis-crible-i-brouillon1.py` (`92932a6a…`), sortie `devis-crible-i-brouillon1-sortie.txt` (`ef0c36bd…`), lancé le\n"
     "   2026-11-17 vers 00:56 UTC (`.venv/bin/python -I`) ;",
     "1. **Devis** : `devis-crible-i-brouillon2.py` (`945cbbc6…`), sortie `devis-crible-i-brouillon2-sortie.txt` (`68042c09…`), lancé le\n"
     "   2026-11-17 à 01:31:44 UTC (`.venv/bin/python -I`) ; ils remplacent `devis-crible-i-brouillon1.py` (`92932a6a…`) et sa sortie\n"
     "   (`ef0c36bd…`), lancés vers 00:56 UTC, dont seul le point 5 était faux (correction M3) ;"),
    ("P7", ANCIENNE_SECTION, NOUVELLE_SECTION.rstrip("\n") + "\n"),
    ("E1",
     "H-i réfutée au crible, H-i-f non réfutée",
     "H-i non soutenue au crible (l'information n'est pas établie ; un crible à 20 mondes ne réfute pas un effet d'information),\n"
     "H-i-f non réfutée"),
]

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
print(f"couples du rapport : {len(couples)} ; extension et couples propres : {len(P)}")
print("validateur : aucun défaut formel")
print(f"empreinte : {sha(CIBLE)}")

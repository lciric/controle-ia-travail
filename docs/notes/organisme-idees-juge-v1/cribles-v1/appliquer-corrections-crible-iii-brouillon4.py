"""Brouillon 4 du préenregistrement du crible (iii) : application des corrections du tour 3 de contre-lecture.

Couples « ancien → nouveau » : les 8 couples de E-01 à E-06 (E-01 et E-03 en deux couples chacun) sont lus dans le rapport
de contre-lecture du tour 3 lui-même (blocs « Ancien : » et « Nouveau : » entre clôtures de quatre accents graves, section
« 3. Corrections exigées »), sans aucun écart ; s'y ajoutent les couples propres à l'en-tête (titre, puce du brouillon 4,
statut, validateur) et à la section « Contre-lecture » (entrée 3 et paragraphe « Tour suivant »).
Gardes : empreinte de la pièce de départ (brouillon 3) et du rapport ; 8 couples exactement, dans l'ordre attendu ; chaque
« ancien » figure exactement une fois dans la pièce de départ ; aucun chevauchement entre « anciens » ; chaque « nouveau »
figure dans la cible ; la cible (et son compagnon) ne doit pas exister et n'est jamais écrasée (ouverture en mode « x ») ;
le validateur `controle_ia.prereg.problemes` est rejoué sur le texte neuf (copie temporaire) avant toute écriture de la cible
et doit rendre une liste vide ; aucun repli silencieux. Bibliothèque standard seule (le validateur est appelé par
`.venv/bin/python` avec `PYTHONPATH=src`) ; aucun appel de modèle, aucune donnée.
Usage : python3 -I appliquer-corrections-crible-iii-brouillon4.py  (depuis n'importe quel dossier)
"""
import hashlib
import os
import re
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
SOURCE = os.path.join(ICI, "crible-iii-brouillon3.md")
SOURCE_SHA = "bd1aff342bfc8f9842c27b688a354e3a24ea1b9029ae1119f092fc793ad4f7a3"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-iii-tour3-v1.md")
RAPPORT_SHA = "b785115660011d1f6a1d5dc93d883a1bfca2c0f1bdbd82e29a1b2be111001d1e"
CIBLE = os.path.join(ICI, "crible-iii-brouillon4.md")
NOM_PROGRAMME = "appliquer-corrections-crible-iii-brouillon4.py"
TETE_MAIN = "6785262e"
ATTENDUS = ["E-01", "E-01", "E-02", "E-03", "E-03", "E-04", "E-05", "E-06"]


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
TITRE = re.compile(r"^### (E-\d\d) \((majeure|mineure)\)[^\n]*\n", re.M)
COUPLE = re.compile(r"^Ancien :\n\n````\n(.*?)\n````\n\nNouveau :\n\n````\n(.*?)\n````\n", re.M | re.S)
titres = list(TITRE.finditer(s3))
if s3.count("\n### ") != len(titres):
    arret("titre de correction illisible dans la section 3 du rapport")
couples = []
for k, t in enumerate(titres):
    fin = titres[k + 1].start() if k + 1 < len(titres) else len(s3)
    bloc = s3[t.end():fin]
    trouves = list(COUPLE.finditer(bloc))
    if not trouves or bloc.count("````") != 4 * len(trouves):
        arret(f"bloc de {t.group(1)} mal formé (clôtures non appariées ou aucun couple)")
    for m in trouves:
        couples.append((t.group(1), m.group(1), m.group(2)))
noms = [c[0] for c in couples]
if noms != ATTENDUS:
    arret(f"couples du rapport inattendus : {noms}")

# 2. Couples propres : en-tête et section « Contre-lecture ».
heure = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], check=True, capture_output=True, text=True).stdout.strip()
if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", heure):
    arret(f"heure illisible : {heure!r}")

DEBUT_TS = "**Tour suivant** (obligatoire si la variante est retenue, selon les rapports des tours 1 et 2 ;"
FIN_TS = "## Annexe A — comptes exacts"
if source.count(DEBUT_TS) != 1 or source.count(FIN_TS) != 1:
    arret("bornes du paragraphe « Tour suivant » introuvables une fois")
ANCIEN_TS = source[source.index(DEBUT_TS):source.index(FIN_TS)]

NOUVEAU_TS = f"""- **Contre-lecture 3** (R2, tour 3, sur le brouillon 3) — sous-agent neuf, d'un autre modèle que l'auteur, qui n'a écrit ni ce
  texte, ni les rapports des tours 1 et 2, ni aucune pièce citée (un premier contre-lecteur de ce tour s'était arrêté sur une
  limite d'usage vers 13:05Z sans rendre de rapport, R-2982 : rien de lui n'est repris). Texte relu :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-brouillon3.md`,
  `{SOURCE_SHA}` ; rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-iii-tour3-v1.md`,
  `{RAPPORT_SHA}`. Verdict : « corrections » (1 majeure :
  E-01 ; 5 mineures : E-02 à E-06) ; le rapport constate que les 16 couples du tour 2 sont appliqués à la lettre, que le
  différentiel ne contient rien d'autre que ce que le brouillon 3 déclare et que la conception tient ; il recommande la
  variante (confiance 0,65, comme le tour 2). Corrections appliquées le {heure} (`date -u`) par un rédacteur neuf du
  modèle A, qui n'a écrit ni les brouillons 1 à 3 ni les rapports de contre-lecture, au moyen du programme
  `{NOM_PROGRAMME}` (même dossier, scellé à côté) : les 8 couples (E-01 et E-03 en deux couples chacun) sont lus dans le
  rapport lui-même, sans aucun écart ; chaque « ancien » figure une seule fois dans le brouillon 3 (vérifié par le programme).
  **Traitement**, point par point :
  - E-01 (majeure : la forme du crible est tranchée par la mère **avant toute lecture de l'issue du pilote**, parce qu'elle
    fixe les deux relais dont le taux de réussite par appel fixe N ; décision, date et heure inscrites ici et dans
    `registres/decisions.md` avant cette lecture) : **acceptée**, deux couples (« Choix et doutes », point 4). **Aucune
    décision n'est inscrite ici** : aucune ligne de `registres/decisions.md` ne tranche la forme à l'heure de l'application
    (lignes qui parlent des cribles relues par `grep`, jusqu'à R-2990) ; ce texte reste rédigé dans la forme fidèle à [NOTE]
    et non scellable. Les ajouts « Si la variante est retenue » (section 5 du rapport, qui complète celle du tour 2) ne sont
    **pas** appliqués (ils ne valent qu'après la décision ; un tour de plus est alors obligatoire).
  - E-02 (gel de III-6 confirmé par une ligne datée à l'heure de `registres/decisions.md`, avant que le lecteur neuf du
    pilote rende sa lecture) : **acceptée** (statut de l'en-tête).
  - E-03 (liste close des valeurs calculées avant le scellement : quatre, dont les seuils exacts du test des signes à n = 21
    à 24) : **acceptée**, deux couples (« Devis », règle de mise à jour).
  - E-04 (simulation de puissance : programme sous un nom neuf, scellé avant son lancement ; graines `(96, s)` ; 10 000
    tirages par cellule ; cellules 20 et 24 mondes, effet nul puis effet prédit ; aucune donnée de crible) : **acceptée**
    (« Taille ») ; la clé `(96, s)` ne rencontre aucune des clés de la section « Graines » (`(r, 40)`, `(12, r, t)`,
    `(99, b)`, `(97, k)`).
  - E-05 (III-5 : seule la part de H après filtre est calculable sans réponse de proposeur ; N_D ≤ 0,25 reste la prédiction
    pour D) : **acceptée** (table des prédictions).
  - E-06 (nœud de la mère sur la borne par appel, borné : seule décision permise, relever la borne par appel à 2 × l'appel
    le plus long du pilote, sans dépasser 3 600 s ; borne de 7 200 s par monde et garde de départ inchangées ; décision datée
    avant le scellement) : **acceptée** (table de mise à jour).
  - **Remarques facultatives** (section 4 du rapport) : remarque 4 appliquée à l'en-tête (« contre-lu trois fois ») ;
    remarques 1 et 3 sans changement (la ligne « limite de débit » reste du côté sûr ; la part de H après filtre pourra servir
    de contrôle de la règle de Jaccard) ; remarque 2 **non appliquée** ici (facultative ; la ligne « Témoin commun » du devis
    et les renvois à [CRIBLE-V] sont à supprimer ou à recopier dans la version qui fera foi).
  - **Points du rapport pour la mère, ouverts** (section 6 ; aucun n'est tranché ici) : la forme, **avant toute lecture de
    l'issue du pilote** (E-01), recommandation du rapport : la variante, confiance 0,65, et le solde de crédits de Claude pour
    263 USD au pire (315 à 24 mondes) ; le gel de III-6, à inscrire aussi avant la lecture (E-02) ; N : la règle « sous
    0,95 » revient, avec huit appels des deux relais, à « au moindre échec » ; 24 mondes sans condition (+ 20 %) ; seuils
    absolus (14 et 10) ou proportionnels (17 et 12 à 24 mondes) ; N-045 point 3, à dire à Lazar avec le nœud d'adoption ;
    le prix promotionnel de Pr-1 jusqu'au 30 novembre ; le risque d'un « non tranché » de P2 même si III-2 est vraie ; le
    code neuf (environ deux jours d'agents, concurrence jamais éprouvée) ; le calendrier, sans marge si un tour de réécriture
    s'ajoute.
  - **Décisions de R-2977 relues dans ce texte** : mondes séparés de ceux de (v) ; dollars principaux au prix public, prix de
    la configuration en sensibilité ; ablation de la frontière aux critères gelés ; GO-2026-11-15-06 pour l'essai, non pour
    l'adoption ; forme « qui répond à la question en mettant le plus possible sur crédits de Claude », confiée au
    contre-lecteur et encore à inscrire par la mère ; N relevé à 24 si le taux de réussite par appel du pilote est sous 0,95.
    Les décisions de R-2977 propres à (v) (archive réduite à K1 pour (v), relevé de la course v67 pour la partie A de (v))
    ne s'appliquent pas ici ; ce texte ne lit pas ce relevé.

**Tour suivant** (obligatoire si la variante est retenue, selon les rapports des tours 1 à 3 ; sinon, contre-lecture de la
version qui fera foi) : sous-agent neuf qui n'a écrit ni ce texte, ni les brouillons 1 à 3, ni les rapports des tours 1 à 3.
**Fichiers à lui donner explicitement** : ce texte ; les brouillons 1 à 3 et les rapports des tours 1 à 3 (empreintes
ci-dessus) ; les programmes `appliquer-corrections-crible-iii-brouillon2.py`, `appliquer-corrections-crible-iii-brouillon3.py`
et `{NOM_PROGRAMME}` ; [CRIBLE-V] (« Métrique », « Devis ») ; [NOTE] (`2f6a69dd…`), § 1, § 2, § 3 (iii), § 4, § 6 et
annexe A ; [RELEVÉ] (`bd253b6c…`), § 3.1, § 4.2, § 5, § 6 ; [REC] (`eecd98fa…`), V3 et C2 ; [PILOTE] (`8aa33014…`),
« Dessin », « Métrique », « Devis », bloc gelé ; [PROC-14] (`20355627…`), § 0, § 6, § 7 ; [MR2] (`47e38ec0…`), § 2 et § 3 ;
[V3] (`386d48ba…`), § 4.1 ; `mesure_pilote_v4.py` (`676d5f37…`) ; `monde_riche_outils_v1.py` (`1825b956…`) ; N-045 v2
(`c7b05e39…`) ; N-058 (`854f2724…`) ; la ligne GO-2026-11-15-06 ; la ligne R-2977 de `registres/decisions.md` et toute ligne
de ce registre qui trancherait la forme ou le gel de III-6 ; l'annexe A et ses deux programmes.

"""

PUCE_B4 = f"""  et la section « Contre-lecture » ne change.
- Brouillon 4 : corrections du tour 3 de contre-lecture appliquées le {heure} (`date -u`, au scellement) par un
  rédacteur neuf du modèle A, qui n'a écrit ni les brouillons 1 à 3 ni les rapports de contre-lecture (identité dite en
  conversation seulement), au moyen du programme `{NOM_PROGRAMME}` (même dossier, scellé) ; dépôt lu sur `main` (tête
  `{TETE_MAIN}`) ; procédure v14 relue au commit `2d35cafa…` par `git show`, après un `git fetch` à refspec ; rien lu de la
  sortie du pilote MR-2 v14 ; aucun commit, aucune poussée. Rien d'autre que les 8 couples du rapport du tour 3, l'en-tête
  et la section « Contre-lecture » ne change.
- Commit du code d'analyse"""

PROPRES = [
    ("en-tête : titre",
     "par un proposeur cher — brouillon 3\n",
     "par un proposeur cher — brouillon 4\n"),
    ("en-tête : puce du brouillon 4",
     "  et la section « Contre-lecture » ne change.\n- Commit du code d'analyse",
     PUCE_B4),
    ("en-tête : statut",
     "**Statut.** Brouillon 3, **contre-lu deux fois** (tours 1 et 2, corrections appliquées, section « Contre-lecture ») ;",
     "**Statut.** Brouillon 4, **contre-lu trois fois** (tours 1 à 3, corrections appliquées, section « Contre-lecture ») ;"),
    ("en-tête : validateur",
     "aucun défaut sur ce brouillon 3 (vérifié avant son scellement comme pièce de\ntravail).",
     "aucun défaut sur ce brouillon 4 (vérifié avant son scellement comme pièce de\ntravail)."),
    ("contre-lecture : entrée 3 et tour suivant", ANCIEN_TS, NOUVEAU_TS),
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
    copie = os.path.join(tmp, "crible-iii-brouillon4.md")
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

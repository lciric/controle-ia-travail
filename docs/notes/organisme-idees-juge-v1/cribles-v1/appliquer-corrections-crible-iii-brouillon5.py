"""Brouillon 5 du préenregistrement du crible (iii) : application des corrections de la contre-lecture du brouillon 4
(tour 1 de cette lecture, quatrième du crible).

Couples « ancien → nouveau » : les 18 couples de F-01 à F-08 (F-02 en sept couples, F-03 et F-06 en trois chacun) sont lus
dans le rapport de contre-lecture lui-même (blocs « Ancien : » et « Nouveau : » entre clôtures de quatre accents graves,
section « 4. Corrections exigées »), sans aucun écart ; s'y ajoutent les couples propres à l'en-tête (titre, puce du
brouillon 5, statut, validateur) et à la section « Contre-lecture » (entrée 4 et paragraphe « Tour suivant »).
Gardes : empreinte de la pièce de départ (brouillon 4) et du rapport ; 18 couples exactement, dans l'ordre attendu ; chaque
« ancien » figure exactement une fois dans la pièce de départ ; aucun chevauchement entre « anciens » ; chaque « nouveau »
figure dans la cible ; la cible (et son compagnon) ne doit pas exister et n'est jamais écrasée (ouverture en mode « x ») ;
le validateur `controle_ia.prereg.problemes` est rejoué sur le texte neuf (copie temporaire) avant toute écriture de la cible
et doit rendre une liste vide ; aucun repli silencieux. Bibliothèque standard seule (le validateur est appelé par
`.venv/bin/python` avec `PYTHONPATH=src`) ; aucun appel de modèle, aucune donnée.
Usage : python3 -I appliquer-corrections-crible-iii-brouillon5.py  (depuis n'importe quel dossier)
"""
import hashlib
import os
import re
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
SOURCE = os.path.join(ICI, "crible-iii-brouillon4.md")
SOURCE_SHA = "f30bd0f1c46cbbd3597fdf005bb6a372d0e9f039e2eedd7c3c3e7bb74667e8dd"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-iii-b4-tour1-v1.md")
RAPPORT_SHA = "4997f4a2baa6993186de7cba23fb54760fcfefaa94781e3bb88d43e71f8f0fe4"
CIBLE = os.path.join(ICI, "crible-iii-brouillon5.md")
NOM_PROGRAMME = "appliquer-corrections-crible-iii-brouillon5.py"
TETE_MAIN = "e231c01e"
ATTENDUS = (["F-01"] + ["F-02"] * 7 + ["F-03"] * 3 + ["F-04", "F-05"] + ["F-06"] * 3 + ["F-07", "F-08"])


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

# 1. Couples du rapport (section 4 seule).
DEBUT_S4, FIN_S4 = "## 4. Corrections exigées : ancien → nouveau\n", "## 5. Remarques facultatives"
if rapport.count(DEBUT_S4) != 1 or rapport.count(FIN_S4) != 1:
    arret("bornes de la section 4 du rapport introuvables une fois")
s4 = rapport[rapport.index(DEBUT_S4):rapport.index(FIN_S4)]
TITRE = re.compile(r"^### (F-\d\d) \((majeure|mineure)\)[^\n]*\n", re.M)
COUPLE = re.compile(r"^Ancien :\n\n````\n(.*?)\n````\n\nNouveau :\n\n````\n(.*?)\n````\n", re.M | re.S)
titres = list(TITRE.finditer(s4))
if s4.count("\n### ") != len(titres):
    arret("titre de correction illisible dans la section 4 du rapport")
couples = []
for k, t in enumerate(titres):
    fin = titres[k + 1].start() if k + 1 < len(titres) else len(s4)
    bloc = s4[t.end():fin]
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

DEBUT_TS = "**Tour suivant** (obligatoire si la variante est retenue, selon les rapports des tours 1 à 3 ;"
FIN_TS = "## Annexe A — comptes exacts"
if source.count(DEBUT_TS) != 1 or source.count(FIN_TS) != 1:
    arret("bornes du paragraphe « Tour suivant » introuvables une fois")
ANCIEN_TS = source[source.index(DEBUT_TS):source.index(FIN_TS)]

NOUVEAU_TS = f"""- **Contre-lecture 4** (R2, tour 1 de la lecture du brouillon 4, quatrième lecture du crible) — sous-agent neuf, d'un autre
  modèle que l'auteur, qui n'a écrit ni ce texte, ni les rapports des tours 1 à 3, ni aucune pièce citée. Texte relu :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-brouillon4.md`,
  `{SOURCE_SHA}` ; rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-iii-b4-tour1-v1.md`,
  `{RAPPORT_SHA}`. Verdict : « corrections » (2 majeures :
  F-01, F-02 ; 6 mineures : F-03 à F-08) ; le rapport constate que les 8 couples du tour 3 sont appliqués à la lettre, que
  les chiffres du devis, des seuils et des probabilités se recomptent, que le validateur ne trouve aucun défaut et qu'aucun
  défaut n'appelle de refaire la conception ; il recommande la variante (confiance 0,6). Corrections appliquées le {heure}
  (`date -u`) par un rédacteur neuf, qui n'a écrit ni les brouillons 1 à 4 ni les rapports de contre-lecture (identité dite
  en conversation seulement), au moyen du programme `{NOM_PROGRAMME}` (même dossier, scellé à côté) : les 18 couples
  (F-02 en sept couples, F-03 et F-06 en trois chacun) sont lus dans le rapport lui-même, sans aucun écart ; chaque
  « ancien » figure une seule fois dans le brouillon 4 (vérifié par le programme). Avant l'application, le différentiel du
  brouillon 3 au brouillon 4 a été relu : il ne contient que les 8 couples du tour 3, l'en-tête et la section
  « Contre-lecture ».
  **Traitement**, point par point :
  - F-01 (majeure : sous « B tronqué », δ_DB rapporté aussi en réintégrant les mondes où seul l'appel de B est tronqué,
    lu avec le principal même sous trois appels tronqués ; le principal exclut ces mondes par définition du monde
    complet) : **acceptée** (« Critères de lecture gelés », étage 2).
  - F-02 (majeure : le crible ne retire pas la frontière ; Pr-1 et Pr-2 sont deux espèces de frontière au sens de N-045,
    point 1 ; « sans la frontière » devient « sans le proposeur cher » dans les lieux de verdict) : **acceptée**, sept
    couples (section 0, point 5 ; « Hypothèse », contexte ; table des prédictions, III-2 ; « Ce que serait chaque issue » ;
    « Seuil », P2 ; étages 2 et 5). Restent, non visés par le rapport et sans rien changer : « confiée à la frontière »
    (« Hypothèse », contexte : mots de la fiche) et « ablation de la frontière » (mots de R-2977, rappelés dans cette
    section).
  - F-03 (III-1 : ρ_DS entre 0,8 et 1 ; ρ_DS au-dessus de 1 en estimation réfute le signe ; colonne « ce qui la réfute »
    en deux parties) : **acceptée**, trois couples (table des prédictions ; section 0, point 7).
  - F-04 (« sans perte notable » atteignable seulement avec δ_DB observé sous − 0,05 à 20 mondes, sous 0 à 24 ; non une
    équivalence) : **acceptée** (« Taille »).
  - F-05 (« fournisseur perdu en entier » défini : aucun appel répondu de ce fournisseur sur tous les mondes commencés,
    dix appels faits au moins) : **acceptée** (« Seuil »).
  - F-06 (couverture définie par [PILOTE], texte scellé, non par [CRIBLE-V] ; deux renvois du devis retirés) : **acceptée**,
    trois couples (« Métrique » ; « Devis », hypothèses de coût et plafond de 0,75). Reste, non visé par le rapport et sans
    rien changer : le renvoi « Points à remesurer d'après le coût réel du pilote MR-2 : ceux de [CRIBLE-V] » (« Devis »,
    règle de mise à jour), à recopier dans la version qui fera foi.
  - F-07 (ligne « Témoin commun » marquée écartée, R-2977, information seulement, jamais un devis) : **acceptée**
    (« Devis »).
  - F-08 (durée attendue à cinq files : 2 à 2 h 40 par file, plus mesure et barrières, au pire 8 h) : **acceptée**
    (« Devis », « Durée »).
  - **Remarques facultatives** (section 5 du rapport, R-1 à R-5) : **non appliquées** (aucune correction exigée ; à reprendre
    dans la version qui fera foi : origine des fourchettes hautes de S et de B ; forme impersonnelle ; ligne « sonde neuve
    des relais » à retirer ou à relier à la ligne d'arrêt ; colonne « ce qui la réfute » de III-2 ; « sous 0,95 » sur huit
    appels revient à « au moindre échec »).
  - **Forme du crible** (section 3 du rapport : recommandation, la variante, confiance 0,6 ; la forme fidèle reste
    défendable si la consigne de Lazar vise à limiter les dollars hors crédits sans gonfler le total) : **aucune décision
    n'est inscrite ici** : aucune ligne de `registres/decisions.md` ne tranche la forme ni le gel de III-6 à l'heure de
    l'application (lignes qui parlent des cribles, de la variante et de III-6 relues par `grep`, jusqu'à R-2990, dernière
    ligne) ; ce texte reste rédigé dans la forme fidèle à [NOTE] et non scellable. Les ajouts « Si la variante est
    retenue » (section 6 du rapport, qui complète celles des tours 2 et 3) ne sont **pas** appliqués (ils ne valent qu'après
    la décision ; un tour de plus est alors obligatoire).
  - **Points du rapport pour la mère, ouverts** (section 7 ; aucun n'est tranché ici) : la forme, à inscrire par une ligne
    datée à l'heure **avant** que le lecteur neuf du pilote rende sa lecture, et le gel de III-6 de la même façon ; le mot
    de Lazar exigé pour le lancement et le calendrier (autonomie jusqu'au 17 novembre à 11:48Z, prolongeable au 18 ; la
    variante impose une réécriture) ; l'enveloppe de GO-2026-11-15-06 : avec la variante, la somme des pires cas des cinq
    cribles est de 1 308,60 USD, au-dessus de 1 275 (1 262,20 avec la forme fidèle) : plafond cumulé à décider ; le solde de
    crédits de Claude (263 USD au pire pour (iii) seul avec la variante, 315,60 à 24 mondes) ; N = 24 (+ 20 %) à accepter
    explicitement ; N-045 point 3 à dire à Lazar avec le nœud d'adoption, et que le crible compare deux espèces de
    frontière sans retirer la frontière (QO1 complète exigerait l'instrument local) ; le risque d'un « non tranché » de P2
    même si III-2 est vraie, le code neuf et la concurrence jamais éprouvée.
  - **Décisions de R-2977 relues dans ce texte** (inchangées) : mondes séparés de ceux de (v) ; dollars principaux au prix
    public, prix de la configuration en sensibilité ; ablation de la frontière aux critères gelés ; GO-2026-11-15-06 pour
    l'essai, non pour l'adoption ; forme « qui répond à la question en mettant le plus possible sur crédits de Claude »,
    confiée au contre-lecteur et encore à inscrire par la mère ; N relevé à 24 si le taux de réussite par appel du pilote
    est sous 0,95. Rien du pilote MR-2 v14 n'est lu par ce texte ni par son application.

**Tour suivant** (obligatoire avant le scellement : si la variante est retenue, après la réécriture, selon les rapports des
tours 1 à 3 et de la lecture du brouillon 4 ; sinon, sur ce brouillon 5 ou la version qui fera foi, selon le rapport de la
lecture du brouillon 4, section 3) : sous-agent neuf qui n'a écrit ni ce texte, ni les brouillons 1 à 4, ni les rapports des
tours 1 à 3 ni celui de la lecture du brouillon 4.
**Fichiers à lui donner explicitement** : ce texte ; les brouillons 1 à 4, les rapports des tours 1 à 3 et celui de la
lecture du brouillon 4 (empreintes ci-dessus) ; les programmes `appliquer-corrections-crible-iii-brouillon2.py`,
`appliquer-corrections-crible-iii-brouillon3.py`, `appliquer-corrections-crible-iii-brouillon4.py` et `{NOM_PROGRAMME}` ;
[CRIBLE-V] (« Métrique », « Devis ») ; [NOTE] (`2f6a69dd…`), § 1, § 2, § 3 (iii), § 4, § 6 et
annexe A ; [RELEVÉ] (`bd253b6c…`), § 3.1, § 4.2, § 5, § 6 ; [REC] (`eecd98fa…`), V3 et C2 ; [PILOTE] (`8aa33014…`),
« Dessin », « Métrique », « Devis », bloc gelé ; [PROC-14] (`20355627…`), § 0, § 6, § 7 ; [MR2] (`47e38ec0…`), § 2 et § 3 ;
[V3] (`386d48ba…`), § 4.1 ; `mesure_pilote_v4.py` (`676d5f37…`) ; `monde_riche_outils_v1.py` (`1825b956…`) ; N-045 v2
(`c7b05e39…`) ; N-058 (`854f2724…`) ; la ligne GO-2026-11-15-06 ; la ligne R-2977 de `registres/decisions.md` et toute ligne
de ce registre qui trancherait la forme ou le gel de III-6 ; l'annexe A et ses deux programmes.

"""

PUCE_B5 = f"""  et la section « Contre-lecture » ne change.
- Brouillon 5 : corrections de la contre-lecture du brouillon 4 (tour 1 de cette lecture) appliquées le {heure} (`date -u`,
  au scellement) par un rédacteur neuf, qui n'a écrit ni les brouillons 1 à 4 ni les rapports de contre-lecture (identité
  dite en conversation seulement), au moyen du programme `{NOM_PROGRAMME}` (même dossier, scellé) ; dépôt lu sur `main`
  (tête `{TETE_MAIN}`) ; procédure v14 relue au commit `2d35cafa…` par `git show`, après un `git fetch` à refspec ; rien lu
  de la sortie du pilote MR-2 v14 ; aucun commit, aucune poussée. Rien d'autre que les 18 couples du rapport, l'en-tête et
  la section « Contre-lecture » ne change.
- Commit du code d'analyse"""

PROPRES = [
    ("en-tête : titre",
     "par un proposeur cher — brouillon 4\n",
     "par un proposeur cher — brouillon 5\n"),
    ("en-tête : puce du brouillon 5",
     "  et la section « Contre-lecture » ne change.\n- Commit du code d'analyse",
     PUCE_B5),
    ("en-tête : statut",
     "**Statut.** Brouillon 4, **contre-lu trois fois** (tours 1 à 3, corrections appliquées, section « Contre-lecture ») ;",
     "**Statut.** Brouillon 5, **contre-lu quatre fois** (tours 1 à 3, puis lecture du brouillon 4 ; corrections appliquées, "
     "section « Contre-lecture ») ;"),
    ("en-tête : validateur",
     "aucun défaut sur ce brouillon 4 (vérifié avant son scellement comme pièce de\ntravail).",
     "aucun défaut sur ce brouillon 5 (vérifié avant son scellement comme pièce de\ntravail)."),
    ("contre-lecture : entrée 4 et tour suivant", ANCIEN_TS, NOUVEAU_TS),
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
    copie = os.path.join(tmp, "crible-iii-brouillon5.md")
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

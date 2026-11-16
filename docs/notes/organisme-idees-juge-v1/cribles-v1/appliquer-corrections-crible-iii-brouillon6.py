"""Brouillon 6 du préenregistrement du crible (iii) : application des corrections de la contre-lecture du brouillon 5
(tour 2 de la lecture du brouillon 4, cinquième lecture du crible).

Couples « ancien → nouveau » : les 4 couples de G-01 et G-02 (G-02 en trois couples) sont lus dans le rapport de
contre-lecture lui-même (blocs « Ancien : » et « Nouveau : » entre clôtures de quatre accents graves, section « 4. Corrections
exigées »), sans aucun écart ; G-03 n'a pas de couple exact (le rapport demande l'entrée « Contre-lecture 5 ») ; s'y ajoutent
les couples propres à l'en-tête (titre, puce du brouillon 6, statut, validateur) et à la section « Contre-lecture » (entrée 5
et paragraphe « Tour suivant »).
Gardes : empreinte de la pièce de départ (brouillon 5) et du rapport ; 4 couples exactement, dans l'ordre attendu, et G-03 sans
couple ; chaque « ancien » figure exactement une fois dans la pièce de départ ; aucun chevauchement entre « anciens » ; chaque
« nouveau » figure dans la cible ; la cible (et son compagnon) ne doit pas exister et n'est jamais écrasée (ouverture en mode
« x ») ; le validateur `controle_ia.prereg.problemes` est rejoué sur le texte neuf (copie temporaire) avant toute écriture de
la cible et doit rendre une liste vide ; aucun repli silencieux. Bibliothèque standard seule (le validateur est appelé par
`.venv/bin/python` avec `PYTHONPATH=src`) ; aucun appel de modèle, aucune donnée.
Usage : python3 -I appliquer-corrections-crible-iii-brouillon6.py  (depuis n'importe quel dossier)
"""
import hashlib
import os
import re
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
SOURCE = os.path.join(ICI, "crible-iii-brouillon5.md")
SOURCE_SHA = "add61e9726e5ba64324135656bde0042aa87721eafdf12431af30be810b4b94f"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-iii-b4-tour2-v1.md")
RAPPORT_SHA = "782f737747bb95838b514b80d91a81c02ef006001364ad4845ad80bc4a4d85f6"
CIBLE = os.path.join(ICI, "crible-iii-brouillon6.md")
NOM_PROGRAMME = "appliquer-corrections-crible-iii-brouillon6.py"
TETE_MAIN = "fd171dd7"
ATTENDUS = ["G-01"] + ["G-02"] * 3
SANS_COUPLE = ["G-03"]


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
TITRE = re.compile(r"^### (G-\d\d) \((majeure|mineure)\)[^\n]*\n", re.M)
COUPLE = re.compile(r"^Ancien :\n\n````\n(.*?)\n````\n\nNouveau :\n\n````\n(.*?)\n````\n", re.M | re.S)
titres = list(TITRE.finditer(s4))
if s4.count("\n### ") != len(titres):
    arret("titre de correction illisible dans la section 4 du rapport")
couples, vides = [], []
for k, t in enumerate(titres):
    fin = titres[k + 1].start() if k + 1 < len(titres) else len(s4)
    bloc = s4[t.end():fin]
    trouves = list(COUPLE.finditer(bloc))
    if bloc.count("````") != 4 * len(trouves):
        arret(f"bloc de {t.group(1)} mal formé (clôtures non appariées)")
    if not trouves:
        vides.append(t.group(1))
    for m in trouves:
        couples.append((t.group(1), m.group(1), m.group(2)))
noms = [c[0] for c in couples]
if noms != ATTENDUS or vides != SANS_COUPLE:
    arret(f"couples du rapport inattendus : {noms} ; sans couple : {vides}")

# 2. Couples propres : en-tête et section « Contre-lecture ».
heure = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], check=True, capture_output=True, text=True).stdout.strip()
if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", heure):
    arret(f"heure illisible : {heure!r}")

DEBUT_TS = "**Tour suivant** (obligatoire avant le scellement : si la variante est retenue, après la réécriture, selon les rapports des"
FIN_TS = "## Annexe A — comptes exacts"
if source.count(DEBUT_TS) != 1 or source.count(FIN_TS) != 1:
    arret("bornes du paragraphe « Tour suivant » introuvables une fois")
ANCIEN_TS = source[source.index(DEBUT_TS):source.index(FIN_TS)]

NOUVEAU_TS = f"""- **Contre-lecture 5** (R2, tour 2 de la lecture du brouillon 4, cinquième lecture du crible) — sous-agent neuf, d'un autre
  modèle que l'auteur, qui n'a écrit ni ce texte, ni les brouillons 1 à 4, ni les rapports des tours précédents, ni aucune
  pièce citée (un premier contre-lecteur s'était arrêté sur une limite d'usage vers 13:05Z sans rendre de rapport, R-2982 :
  rien de lui n'est repris). Texte relu :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-brouillon5.md`,
  `{SOURCE_SHA}` ; rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-iii-b4-tour2-v1.md`,
  `{RAPPORT_SHA}` (égale à son compagnon `.sha256`). Verdict :
  « corrections » (0 majeure ; 3 mineures : G-01 à G-03), toutes de cohérence ou de fermeture de lecture ; le rapport constate
  que les 18 couples de la lecture précédente sont appliqués à la lettre et que rien d'autre ne change, que le devis, la durée,
  la liste d'arrêt et les graines se recomptent, que le validateur ne trouve aucun défaut, et qu'aucun défaut n'appelle de
  refaire la conception ; il recommande la variante (confiance 0,6). Corrections appliquées le {heure} (`date -u`) par un
  rédacteur neuf, qui n'a écrit ni les brouillons 1 à 5 ni les rapports de contre-lecture (identité dite en conversation
  seulement), au moyen du programme `{NOM_PROGRAMME}` (même dossier, scellé à côté) : les 4 couples (G-01 ; G-02 en trois
  couples) sont lus dans le rapport lui-même, sans aucun écart ; chaque « ancien » figure une seule fois dans le brouillon 5
  (vérifié par le programme). Avant l'application, le différentiel du brouillon 4 au brouillon 5 a été relu par programme :
  les 18 couples du rapport de la lecture précédente y sont appliqués à la lettre, et il ne contient rien d'autre que ces
  couples, l'en-tête (titre, puce du brouillon 5, statut, validateur) et la section « Contre-lecture » (entrée 4 et « Tour
  suivant »).
  **Traitement**, point par point :
  - G-01 (rapport de P2 « réintégré » sous « B tronqué » : C_B = 0 est le pire cas pour B ; si l'issue de P2 du rapport
    réintégré, mêmes seuils à 97,5 %, diffère de celle du principal, l'issue de P2 est qualifiée « sensible à la troncature
    de B » et rien de plus n'en est conclu) : **acceptée** (« Critères de lecture gelés », étage 2).
  - G-02 (« QO1 » qualifiée au sens dit en « Hypothèse » : Pr-2 contre Pr-1, deux espèces de frontière, non l'instrument
    local) : **acceptée**, trois couples (section 0, point 1 ; « Hypothèse », H-iii-a ; « Écarts », N-045 point 3).
    Restent, non visés par le rapport et sans rien changer : « (N-045 points 1, 3 et 7 ; QO1, QO4) » (« Hypothèse »,
    contexte : la phrase qui définit ce sens), « (QO1, QO4) » (liste des documents qui font foi : titre de la question de la
    course), l'étage 5 (déjà qualifié) et les mots des entrées 4 et 5 de cette section.
  - G-03 (dire la lecture de ce rapport dans la section « Contre-lecture », avec les deux empreintes entières) : **acceptée**
    (cette entrée 5 ; empreinte du rapport lue sur son compagnon et recalculée).
  - **Remarques facultatives** (section 5 du rapport) : **non appliquées** (aucune correction exigée) : R-1 à R-5 de la
    lecture précédente restent à reprendre dans la version qui fera foi ; R-6 (« environ » devant « sous − 0,05 à 20 mondes,
    sous 0 à 24 », valeurs médianes de la fourchette d'écart-type ; aucun seuil changé) à reprendre de même ; R-7 : rien à
    reprendre.
  - **Forme du crible** (section 3 du rapport : recommandation, la variante, Pr-2 choisit, Pr-4 écrit, S = un appel de Pr-4,
    confiance 0,6 ; la variante change un peu la question, deux paliers de prix d'une même maison ; la forme fidèle reste
    défendable si la consigne de Lazar vise à limiter les dollars hors crédits sans gonfler le total, et elle se scelle alors
    après un dernier tour sur le différentiel seul) : **aucune décision n'est inscrite ici** : aucune ligne de
    `registres/decisions.md` ne tranche la forme ni le gel de III-6 à l'heure de l'application (lignes qui parlent des
    cribles, de la variante et de III-6 relues par `grep`, jusqu'à R-2991, dernière ligne) ; ce texte reste rédigé dans la
    forme fidèle à [NOTE] et non scellable. Les ajouts « Si la variante est retenue » des rapports précédents ne sont **pas**
    appliqués (ils ne valent qu'après la décision ; un tour de plus est alors obligatoire).
  - **Points du rapport pour la mère, ouverts** (section 6 ; aucun n'est tranché ici) : la forme, par une ligne datée à
    l'heure de `registres/decisions.md` (variante recommandée, 0,6), et le gel de III-6 de la même façon, avant que le
    lecteur neuf du pilote rende sa lecture ; le mot de Lazar pour le lancement et le calendrier (autonomie jusqu'au
    17 novembre à 11:48Z, prolongeable au 18 ; sans marge si réécriture) ; l'enveloppe de GO-2026-11-15-06 (somme des pires
    cas des cinq cribles : 1 308,60 USD avec la variante, 1 262,20 avec la forme fidèle, contre 1 275) : plafond cumulé à
    décider ou (ii) à réduire ; le solde de crédits de Claude (263 USD au pire avec la variante, 315,60 à 24 mondes) ;
    N-045 point 3 à dire à Lazar avec le nœud d'adoption (le crible compare deux espèces de frontière, il ne retire pas la
    frontière) ; les risques : « non tranché » probable pour P2 même si III-2 est vraie (puissance 0,35 à 0,50 à 20 mondes),
    code neuf et concurrence à cinq files jamais éprouvés.
  - **Décisions de R-2977 relues dans ce texte** (inchangées) : mondes séparés de ceux de (v) ; dollars principaux au prix
    public, prix de la configuration en sensibilité ; ablation de la frontière aux critères gelés ; GO-2026-11-15-06 pour
    l'essai, non pour l'adoption ; forme « qui répond à la question en mettant le plus possible sur crédits de Claude »,
    confiée au contre-lecteur et encore à inscrire par la mère ; N relevé à 24 si le taux de réussite par appel du pilote
    est sous 0,95. Les décisions de R-2977 propres à (v) ne s'appliquent pas ici. Rien du pilote MR-2 v14 n'est lu par ce
    texte ni par son application.

**Tour suivant** (obligatoire avant le scellement : si la variante est retenue, après la réécriture, selon les rapports des
tours 1 à 3 et des deux tours de la lecture du brouillon 4 ; sinon, un dernier tour sur le différentiel du brouillon 5 à ce
brouillon 6 seul, selon le rapport du tour 2 de la lecture du brouillon 4, section 3) : sous-agent neuf qui n'a écrit ni ce
texte, ni les brouillons 1 à 5, ni les rapports des tours 1 à 3 ni ceux des deux tours de la lecture du brouillon 4.
**Fichiers à lui donner explicitement** : ce texte ; les brouillons 1 à 5, les rapports des tours 1 à 3 et ceux des deux tours
de la lecture du brouillon 4 (empreintes ci-dessus) ; les programmes `appliquer-corrections-crible-iii-brouillon2.py`,
`appliquer-corrections-crible-iii-brouillon3.py`, `appliquer-corrections-crible-iii-brouillon4.py`,
`appliquer-corrections-crible-iii-brouillon5.py` et `{NOM_PROGRAMME}` ;
[CRIBLE-V] (« Métrique », « Devis ») ; [NOTE] (`2f6a69dd…`), § 1, § 2, § 3 (iii), § 4, § 6 et
annexe A ; [RELEVÉ] (`bd253b6c…`), § 3.1, § 4.2, § 5, § 6 ; [REC] (`eecd98fa…`), V3 et C2 ; [PILOTE] (`8aa33014…`),
« Dessin », « Métrique », « Devis », bloc gelé ; [PROC-14] (`20355627…`), § 0, § 6, § 7 ; [MR2] (`47e38ec0…`), § 2 et § 3 ;
[V3] (`386d48ba…`), § 4.1 ; `mesure_pilote_v4.py` (`676d5f37…`) ; `monde_riche_outils_v1.py` (`1825b956…`) ; N-045 v2
(`c7b05e39…`) ; N-058 (`854f2724…`) ; la ligne GO-2026-11-15-06 ; la ligne R-2977 de `registres/decisions.md` et toute ligne
de ce registre qui trancherait la forme ou le gel de III-6 ; l'annexe A et ses deux programmes.

"""

PUCE_B6 = f"""la section « Contre-lecture » ne change.
- Brouillon 6 : corrections de la contre-lecture du brouillon 5 (tour 2 de la lecture du brouillon 4) appliquées le {heure}
  (`date -u`, au scellement) par un rédacteur neuf, qui n'a écrit ni les brouillons 1 à 5 ni les rapports de contre-lecture
  (identité dite en conversation seulement), au moyen du programme `{NOM_PROGRAMME}` (même dossier, scellé) ; dépôt lu sur
  `main` (tête `{TETE_MAIN}`) ; procédure v14 relue au commit `2d35cafa…` par `git show`, après un `git fetch` à refspec ;
  rien lu de la sortie du pilote MR-2 v14 ; aucun commit, aucune poussée. Rien d'autre que les 4 couples du rapport, l'en-tête
  et la section « Contre-lecture » ne change.
- Commit du code d'analyse"""

PROPRES = [
    ("en-tête : titre",
     "par un proposeur cher — brouillon 5\n",
     "par un proposeur cher — brouillon 6\n"),
    ("en-tête : puce du brouillon 6",
     "la section « Contre-lecture » ne change.\n- Commit du code d'analyse",
     PUCE_B6),
    ("en-tête : statut",
     "**Statut.** Brouillon 5, **contre-lu quatre fois** (tours 1 à 3, puis lecture du brouillon 4 ; corrections appliquées, "
     "section « Contre-lecture ») ;",
     "**Statut.** Brouillon 6, **contre-lu cinq fois** (tours 1 à 3, puis deux tours de la lecture du brouillon 4 ; corrections "
     "appliquées, section « Contre-lecture ») ;"),
    ("en-tête : validateur",
     "aucun défaut sur ce brouillon 5 (vérifié avant son scellement comme pièce de\ntravail).",
     "aucun défaut sur ce brouillon 6 (vérifié avant son scellement comme pièce de\ntravail)."),
    ("contre-lecture : entrée 5 et tour suivant", ANCIEN_TS, NOUVEAU_TS),
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
    copie = os.path.join(tmp, "crible-iii-brouillon6.md")
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

"""Brouillon 3 de l'addendum de relance de l'idée 1.2 : applique au brouillon 2 les couples « ancien → nouveau » exigés
par la contre-lecture 2 (lecture du brouillon 2), plus trois couples du rédacteur (en-tête : version ; en-tête : statut et
lieu ; section « Contre-lecture »), et rien d'autre.

- vérifie l'empreinte du brouillon 2 et celle du rapport de contre-lecture ;
- tire les 6 couples exigés du § 3 du rapport, par programme (aucune recopie à la main) ; les remarques facultatives
  du § 4 (f-1 à f-5) ne sont pas appliquées ;
- exige que chaque « ancien » figure exactement une fois dans le brouillon 2 et qu'aucun couple n'en chevauche un autre ;
- exige, après application, zéro ligne au format du lanceur (« empreinte, deux espaces, chemin ») et aucune lettre de
  modèle ;
- refuse d'écraser la cible.
Lancé par `python3 -I -B` ; commandes légères seulement ; aucun fichier du run invalide n'est ouvert.
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

DOSSIER = Path("/home/user/controle-ia-travail/docs/notes/organisme-idees-juge-v1")
SOURCE = DOSSIER / "addendum-relance-idee-1-2-v1-brouillon2.md"
SHA_SOURCE = "ab55d5af5d70b340780c33b2bfe4dee15750095540af934530eb74531928d1df"
RAPPORT = DOSSIER / "contre-lecture-addendum-relance-idee-1-2-b2-tour1-v1.md"
SHA_RAPPORT = "f5b2690a34e2f9872fe57978212bd5e49f0ff96906a232067168019a00f54b80"
CIBLE = DOSSIER / "addendum-relance-idee-1-2-v1-brouillon3.md"
MOTIF_LANCEUR = re.compile(r"^[0-9a-f]{64}  \S+\s*$", re.M)
EXIGES = ["M1-a", "M1-b", "M1-c", "m1-a", "m1-b", "m2"]


def h(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def arret(msg: str):
    print("ARRÊT :", msg, file=sys.stderr)
    sys.exit(1)


if CIBLE.exists():
    arret(f"{CIBLE.name} existe déjà : R12 interdit d'écraser")
b_src, b_rap = SOURCE.read_bytes(), RAPPORT.read_bytes()
if h(b_src) != SHA_SOURCE:
    arret("empreinte du brouillon 2 inattendue")
if h(b_rap) != SHA_RAPPORT:
    arret("empreinte du rapport de contre-lecture inattendue")
src, rap = b_src.decode("utf-8"), b_rap.decode("utf-8")

# § 3 du rapport : couples exigés
debut, fin = rap.index("## 3. Corrections exigées"), rap.index("## 4. Remarques facultatives")
sec = rap[debut:fin]
motif = re.compile(r"^\*\*(?P<id>[Mm]\d+(?:-[a-c])?)\*\*[^\n]*(?:\n[^\n]+)*\n\nAncien :\n\n```text\n(?P<a>.*?)\n```"
                   r"\n\nNouveau :\n\n```text\n(?P<n>.*?)\n```", re.S | re.M)
couples = {}
for m in motif.finditer(sec):
    if m["id"] in couples:
        arret(f"couple {m['id']} tiré deux fois du rapport")
    couples[m["id"]] = (m["a"], m["n"])
if sorted(couples) != sorted(EXIGES):
    arret(f"couples tirés du rapport : {sorted(couples)} ≠ {sorted(EXIGES)}")

HEURE = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True, check=True).stdout.strip()
TETE = subprocess.run(["git", "--no-optional-locks", "-C", "/home/user/controle-ia-travail", "rev-parse", "main"],
                      capture_output=True, text=True, check=True).stdout.strip()

# Couple du rédacteur : en-tête (version)
VERSION_A = "- **Version : brouillon 2.** Corrections de la contre-lecture du tour 1"
VERSION_N = f"""- **Version : brouillon 3.** Corrections de la contre-lecture 2 (lecture du brouillon 2) appliquées par un rédacteur
  neuf, sous-agent de la session mère, qui n'a écrit ni le brouillon 1, ni le brouillon 2, ni leurs rapports de
  contre-lecture, ni [T], ni [AE], ni le code : couples « ancien → nouveau » appliqués par le programme
  `docs/notes/organisme-idees-juge-v1/appliquer-corrections-addendum-relance-idee-1-2-v1-brouillon3.py` (scellé à côté)
  au brouillon 2 (`{SHA_SOURCE}`) ; dépôt lu sur `main`, tête `{TETE}` ; heure du scellement
  {HEURE} (`date -u`) ; aucun commit, aucune poussée. Rien d'autre que ces corrections, cet en-tête et la section
  « Contre-lecture » n'a changé.
- **Brouillon 2.** Corrections de la contre-lecture du tour 1"""

# Couple du rédacteur : en-tête (statut et lieu)
STATUT_A = ("- **Statut et lieu** : rédigé comme brouillon 2, "
            "`docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-2-v1-brouillon2.md`,")
STATUT_N = ("- **Statut et lieu** : rédigé comme brouillon 3, "
            "`docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-2-v1-brouillon3.md`,")

# Couple du rédacteur : section « Contre-lecture » (contre-lecture 2, traitement, six décisions)
SIX_A = """- **Les six décisions de la mère, où elles sont écrites** : (i) nom du texte qui fera foi, en-tête (m1) ; (ii) voie (a),
  § 6 (m3) ; (iii) contrôle des versions de l'interpréteur avant le lancement, 4.2 (présent dès le brouillon 1,
  inchangé) ; (iv) aucun mot nouveau du directeur, 4.9 (m2) ; (v) jeu en même temps que celui de l'idée 1.1, 4.10 (M2) ;
  (vi) tâche active pendant tout le jeu, attente bornée réarmée à chaque fin, § 5 (M1)."""
SIX_N = f"""- **Contre-lecture 2** (R2) — lecteur neuf, sous-agent de la session mère (lettre du modèle : inscrite par la mère au
  registre), qui n'a écrit ni les brouillons, ni [T], ni [AE], ni le code, ni le rapport du tour 1 ; texte relu en entier :
  brouillon 2, `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-2-v1-brouillon2.md`,
  `{SHA_SOURCE}`, le 2026-11-16 de 13:13:49Z à 13:22Z ; rapport :
  `docs/notes/organisme-idees-juge-v1/contre-lecture-addendum-relance-idee-1-2-b2-tour1-v1.md`,
  `{SHA_RAPPORT}` (égal à son compagnon). Corrections du tour 1 : appliquées
  fidèlement, rien d'autre (les 17 couples rejoués par programme sur le brouillon 1). Verdict : « corrections » (1 majeure
  en 3 couples, 2 mineures en 3 couples ; remarques facultatives f-1 à f-5) ; « la conception n'est pas en cause ». Un
  premier lecteur neuf du brouillon 2 s'est arrêté sur une limite d'usage vers 13:05Z sans rendre de rapport ; ses
  dossiers de travail n'ont été ni lus ni employés, et rien de lui n'entre dans cette pièce.
- **Traitement** (brouillon 3) — chaque couple exigé est tiré du § 3 du rapport par programme ; chaque « ancien » figure
  une seule fois dans le brouillon 2 ; aucun chevauchement :
  - **M1-a, M1-b, M1-c** (4.10 et 4.9 : la pièce imposait la relance après l'étape 0 de l'idée 1.1, ce que R-2979
    contredit ; ordre désormais libre, moment à la mère, R-2979 cité ; décision (v)) : appliqués.
  - **m1-a, m1-b** (§ 5 : « seconde interruption » limitée à un arrêt venu de l'extérieur, sans `arret.json` ; un arrêt
    consigné par le lanceur relève de [T] l. 512, cause établie d'abord) : appliqués.
  - **m2** (§ 5, constat : réduit à ce que l'état sur disque établit, la lecture des attentes à confirmer sur le journal
    de la mère) : appliqué. La condition écrite au traitement de m5 du brouillon 2 (« si le journal de la mère la dément,
    elle est corrigée avant la recopie ») demeure : la lever, après lecture de son journal, revient à la mère avant la
    recopie sous `prereg/` (rapport, § 5, point 2) ; le rédacteur du brouillon 3 n'a pas lu ce journal.
  - **f-1 à f-5** (facultatifs) : non appliqués ; le brouillon 3 est borné aux corrections exigées ; laissés à la mère,
    f-1 (zéro ligne au format du lanceur recompté sur la copie sous `prereg/`) et f-3 (disque partagé avec les sorties
    de l'idée 1.1) étant à trancher avant le scellement sous `prereg/` si elle les veut écrits.
  - **Rapport, § 5, points 1 et 4 à 7** : à la mère, hors de cette pièce ; le point 5 note que le plafond de cinq
    processus de calcul (4.10, « durée ») suppose que le jeu de l'idée 1.1 ne part qu'après la fin de l'étape 0 v5.
    **Point 3** : cette entrée.
  - Zéro ligne au format du lanceur : recompté par le programme sur le brouillon 3.
- **Les six décisions de la mère, où elles sont écrites** : (i) nom du texte qui fera foi,
  `prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-relance-v1.md`, en-tête (m1 du tour 1) ; (ii) voie
  (a), fichiers du run invalide laissés scellés et non lus dans la copie jusqu'au prononcé du run neuf, § 6 (m3 du tour 1) ;
  (iii) contrôle des versions de l'interpréteur avant le lancement, 4.2 (présent dès le brouillon 1, inchangé) ; (iv)
  aucun mot nouveau du directeur, 4.9 (m2 du tour 1) ; (v) jeu relancé en même temps que des travaux de l'idée 1.1 sur la
  même machine à 4 processeurs logiques (l'étape 0 v5, sur deux processus depuis 12:45:53Z, puis son jeu), avec ses
  conséquences sur la durée et sur la borne de 24 heures, ordre libre, 4.10 et 4.9 (M2 du tour 1 ; M1 de la
  contre-lecture 2) ; (vi) tâche active pendant tout le jeu, attente qui se termine d'elle-même avant la limite de
  l'outil, réarmée à chaque fin, § 5 (M1 du tour 1)."""

paires = [(k, *couples[k]) for k in EXIGES]
paires += [("en-tête (version)", VERSION_A, VERSION_N), ("en-tête (statut et lieu)", STATUT_A, STATUT_N),
           ("contre-lecture", SIX_A, SIX_N)]

spans = []
for k, a, _ in paires:
    n = src.count(a)
    if n != 1:
        arret(f"{k} : « ancien » trouvé {n} fois")
    i = src.index(a)
    spans.append((i, i + len(a), k))
spans.sort()
for (i1, j1, k1), (i2, j2, k2) in zip(spans, spans[1:]):
    if i2 < j1:
        arret(f"chevauchement entre {k1} et {k2}")

texte = src
for k, a, nv in sorted(paires, key=lambda p: -src.index(p[1])):   # de la fin vers le début
    i = texte.index(a)
    texte = texte[:i] + nv + texte[i + len(a):]
    print(f"{k} : appliqué (ancien {len(a)} caractères, nouveau {len(nv)})")

n_lanceur = len(MOTIF_LANCEUR.findall(texte))
if n_lanceur != 0:
    arret(f"{n_lanceur} ligne(s) au format du lanceur")
if re.search(r"modèle [ABC]\b|lecteur [ABC]\b", texte):
    arret("lettre de modèle présente")
for k, _, nv in paires:
    if texte.count(nv) != 1:
        arret(f"{k} : « nouveau » trouvé {texte.count(nv)} fois après application")
if CIBLE.exists():
    arret(f"{CIBLE.name} existe déjà : R12 interdit d'écraser")
with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(texte)
print("couples appliqués :", len(paires), "; lignes au format du lanceur :", n_lanceur)
print("heure (date -u) :", HEURE, "; tête de main :", TETE)
print("cible :", CIBLE, h(CIBLE.read_bytes()))

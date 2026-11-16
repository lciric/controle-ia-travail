"""Brouillon 4 de l'addendum de relance de l'idée 1.2 : applique au brouillon 3 les couples « ancien → nouveau » exigés
par la contre-lecture 3 (lecture du brouillon 3, rapport `…-b2-tour2-v1.md`), plus trois couples du rédacteur (en-tête :
version ; en-tête : statut et lieu ; section « Contre-lecture »), et rien d'autre.

- vérifie l'empreinte du brouillon 3 et celle du rapport de contre-lecture ;
- tire les 2 couples exigés (m-1, m-2) du § 3 du rapport, par programme (aucune recopie à la main) ; les remarques
  facultatives du § 4 ne sont pas appliquées ;
- exige que chaque « ancien » figure exactement une fois dans le brouillon 3 et qu'aucun couple n'en chevauche un autre ;
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
SOURCE = DOSSIER / "addendum-relance-idee-1-2-v1-brouillon3.md"
SHA_SOURCE = "2590228454cd6a7f507fd9fef7ee77e914fee34af30d66acb04e2b745b1b61a6"
RAPPORT = DOSSIER / "contre-lecture-addendum-relance-idee-1-2-b2-tour2-v1.md"
SHA_RAPPORT = "7f837739d40a7460e0cb8d5fd432d6bbb9f36ff7d64a5c4f89198fd18df8c4db"
CIBLE = DOSSIER / "addendum-relance-idee-1-2-v1-brouillon4.md"
MOTIF_LANCEUR = re.compile(r"^[0-9a-f]{64}  \S+\s*$", re.M)
EXIGES = ["m-1", "m-2"]


def h(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def arret(msg: str):
    print("ARRÊT :", msg, file=sys.stderr)
    sys.exit(1)


if CIBLE.exists():
    arret(f"{CIBLE.name} existe déjà : R12 interdit d'écraser")
b_src, b_rap = SOURCE.read_bytes(), RAPPORT.read_bytes()
if h(b_src) != SHA_SOURCE:
    arret("empreinte du brouillon 3 inattendue")
if h(b_rap) != SHA_RAPPORT:
    arret("empreinte du rapport de contre-lecture inattendue")
src, rap = b_src.decode("utf-8"), b_rap.decode("utf-8")

# § 3 du rapport : couples exigés
debut, fin = rap.index("## 3. Corrections exigées"), rap.index("## 4. Remarques facultatives")
sec = rap[debut:fin]
motif = re.compile(r"^\*\*(?P<id>m-\d+) — [^\n]*(?:\n[^\n]+)*\n\nAncien :\n```text\n(?P<a>.*?)\n```"
                   r"\nNouveau :\n```text\n(?P<n>.*?)\n```", re.S | re.M)
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
VERSION_A = "- **Version : brouillon 3.** Corrections de la contre-lecture 2 (lecture du brouillon 2)"
VERSION_N = f"""- **Version : brouillon 4.** Corrections de la contre-lecture 3 (lecture du brouillon 3) appliquées par un rédacteur
  neuf, sous-agent de la session mère, qui n'a écrit ni les brouillons 1 à 3, ni leurs rapports de contre-lecture, ni
  [T], ni [AE], ni le code : couples « ancien → nouveau » appliqués par le programme
  `docs/notes/organisme-idees-juge-v1/appliquer-corrections-addendum-relance-idee-1-2-v1-brouillon4.py` (scellé à côté)
  au brouillon 3 (`{SHA_SOURCE}`) ; dépôt lu sur `main`, tête `{TETE}` ; heure du scellement
  {HEURE} (`date -u`) ; aucun commit, aucune poussée. Rien d'autre que ces corrections, cet en-tête et la section
  « Contre-lecture » n'a changé.
- **Brouillon 3.** Corrections de la contre-lecture 2 (lecture du brouillon 2)"""

# Couple du rédacteur : en-tête (statut et lieu)
STATUT_A = ("- **Statut et lieu** : rédigé comme brouillon 3, "
            "`docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-2-v1-brouillon3.md`,")
STATUT_N = ("- **Statut et lieu** : rédigé comme brouillon 4, "
            "`docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-2-v1-brouillon4.md`,")

# Couple du rédacteur : section « Contre-lecture » (contre-lecture 3, traitement, six décisions)
SIX_A = """- **Les six décisions de la mère, où elles sont écrites** : (i) nom du texte qui fera foi,
  `prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-relance-v1.md`, en-tête (m1 du tour 1) ; (ii) voie
  (a), fichiers du run invalide laissés scellés et non lus dans la copie jusqu'au prononcé du run neuf, § 6 (m3 du tour 1) ;
  (iii) contrôle des versions de l'interpréteur avant le lancement, 4.2 (présent dès le brouillon 1, inchangé) ; (iv)
  aucun mot nouveau du directeur, 4.9 (m2 du tour 1) ; (v) jeu relancé en même temps que des travaux de l'idée 1.1 sur la
  même machine à 4 processeurs logiques (l'étape 0 v5, sur deux processus depuis 12:45:53Z, puis son jeu), avec ses
  conséquences sur la durée et sur la borne de 24 heures, ordre libre, 4.10 et 4.9 (M2 du tour 1 ; M1 de la
  contre-lecture 2) ; (vi) tâche active pendant tout le jeu, attente qui se termine d'elle-même avant la limite de
  l'outil, réarmée à chaque fin, § 5 (M1 du tour 1)."""
SIX_N = f"""- **Contre-lecture 3** (R2) — lecteur neuf, sous-agent de la session mère (lettre du modèle : inscrite par la mère au
  registre), qui n'a écrit ni les brouillons, ni [T], ni [AE], ni le code, ni les rapports des contre-lectures 1 et 2 ;
  texte relu en entier : brouillon 3, `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-2-v1-brouillon3.md`,
  `{SHA_SOURCE}`, le 2026-11-16 de 13:34Z à 13:35:54Z ; rapport :
  `docs/notes/organisme-idees-juge-v1/contre-lecture-addendum-relance-idee-1-2-b2-tour2-v1.md`,
  `{SHA_RAPPORT}` (égal à son compagnon). Corrections de la
  contre-lecture 2 : appliquées fidèlement, rien d'autre (différentiel du brouillon 2 au brouillon 3 relu hunk par hunk).
  Verdict : « corrections » (0 majeure, 2 mineures en 2 couples ; remarques facultatives) ; « la conception n'est pas en
  cause ».
- **Traitement** (brouillon 4) — chaque couple exigé est tiré du § 3 du rapport par programme ; chaque « ancien » figure
  une seule fois dans le brouillon 3 ; aucun chevauchement. Le rédacteur du brouillon 4 a refait, par `diff`, le contrôle du
  différentiel du brouillon 2 au brouillon 3 : conforme au § 1 du rapport.
  - **m-1** (§ 5, constat : « quatre minutes » rattaché à la seconde des deux sorties de tâche de fond, 04:31:41Z, et non
    à 06:20:55Z) : appliqué.
  - **m-2** (4.10, « durée » : le plafond de cinq processus de calcul dit son hypothèse, l'étape 0 v5 finie ; quatre
    processus pendant l'étape 0 v5 seule ; sept, chiffres à refaire, si le jeu de l'idée 1.1 partait avant la fin de
    l'étape 0 v5 ; décision (v)) : appliqué comme couple. Le rapport (§ 5, point 1) laissait à la mère le choix entre ce
    couple et le registre ; la mère peut encore retirer ce couple avant la recopie sous `prereg/`.
  - **Remarques facultatives** (rapport, § 4 : f-1 à f-5 de la contre-lecture 2 ; disque « ≈ 39 Go » de 4.4 et du § 6 ;
    mise en page de trois lignes du § 5) : non appliquées ; le brouillon 4 est borné aux corrections exigées ; laissées à
    la mère.
  - **Rapport, § 5, point 2** : la condition écrite au traitement de m5 du brouillon 2 (« si le journal de la mère la
    dément, elle est corrigée avant la recopie ») demeure ; la lever, après lecture de son journal (02:30Z à 04:40Z),
    revient à la mère avant la recopie sous `prereg/` ; le rédacteur du brouillon 4 n'a pas lu ce journal. **Point 3** :
    cette entrée. **Point 4** : aucun écart à un texte scellé, aucun mot du directeur nécessaire ; rien à écrire de plus.
  - Zéro ligne au format du lanceur : recompté par le programme sur le brouillon 4.
- **Les six décisions de la mère, où elles sont écrites** : (i) nom du texte qui fera foi,
  `prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-relance-v1.md`, en-tête (m1 du tour 1) ; (ii) voie
  (a), fichiers du run invalide laissés scellés et non lus dans la copie jusqu'au prononcé du run neuf, § 6 (m3 du tour 1) ;
  (iii) contrôle des versions de l'interpréteur avant le lancement, 4.2 (présent dès le brouillon 1, inchangé) ; (iv)
  aucun mot nouveau du directeur, 4.9 (m2 du tour 1) ; (v) jeu relancé en même temps que des travaux de l'idée 1.1 sur la
  même machine à 4 processeurs logiques (l'étape 0 v5, sur deux processus depuis 12:45:53Z, puis son jeu), avec ses
  conséquences sur la durée (nombre de processus selon l'ordre des travaux) et sur la borne de 24 heures, ordre libre,
  4.10 et 4.9 (M2 du tour 1 ; M1 de la contre-lecture 2 ; m-2 de la contre-lecture 3) ; (vi) tâche active pendant tout
  le jeu, attente qui se termine d'elle-même avant la limite de l'outil, réarmée à chaque fin, § 5 (M1 du tour 1)."""

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

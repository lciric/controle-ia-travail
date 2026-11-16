"""Brouillon 2 de l'addendum de relance de l'idée 1.2 : applique au brouillon 1 les couples « ancien → nouveau » exigés
par la contre-lecture du tour 1, plus deux couples du rédacteur (en-tête ; section « Contre-lecture »), et rien d'autre.

- vérifie l'empreinte du brouillon 1 et celle du rapport de contre-lecture ;
- tire les 17 couples exigés du § 4 du rapport, par programme (aucune recopie à la main) ; les 3 couples facultatifs du
  § 5 ne sont pas appliqués ;
- le couple m10 du rapport est appliqué en substance : son « ancien » est remplacé par la section écrite ci-dessous
  (empreinte entière du rapport et traitement point par point, que le « nouveau » du rapport laissait à écrire) ;
- exige que chaque « ancien » figure exactement une fois dans le brouillon 1 et qu'aucun couple n'en chevauche un autre ;
- exige, après application, zéro ligne au format du lanceur (« empreinte, deux espaces, chemin ») et aucun « À REMPLIR » ;
- refuse d'écraser la cible.
Lancé par `python3 -I -B` ; commandes légères seulement ; aucun fichier du run invalide n'est ouvert.
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

DOSSIER = Path("/home/user/controle-ia-travail/docs/notes/organisme-idees-juge-v1")
SOURCE = DOSSIER / "addendum-relance-idee-1-2-v1-brouillon1.md"
SHA_SOURCE = "26aa0713419ecff1cbb2cd4240e17dfdc0aea9902e66e4f2c9020560ed50fdd3"
RAPPORT = DOSSIER / "contre-lecture-addendum-relance-idee-1-2-tour1-v1.md"
SHA_RAPPORT = "1b73554004a0cfc77b2448dc19f9d204bbe890382bbf19b91efbefa7a71a486f"
CIBLE = DOSSIER / "addendum-relance-idee-1-2-v1-brouillon2.md"
MOTIF_LANCEUR = re.compile(r"^[0-9a-f]{64}  \S+\s*$", re.M)
EXIGES = ["M1", "M2", "m1", "m2", "m3-a", "m3-b", "m3-c", "m4", "m5", "m6", "m7-a", "m7-b", "m8", "m9", "m10",
          "m11-a", "m11-b"]


def h(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def arret(msg: str):
    print("ARRÊT :", msg, file=sys.stderr)
    sys.exit(1)


if CIBLE.exists():
    arret(f"{CIBLE.name} existe déjà : R12 interdit d'écraser")
b_src, b_rap = SOURCE.read_bytes(), RAPPORT.read_bytes()
if h(b_src) != SHA_SOURCE:
    arret("empreinte du brouillon 1 inattendue")
if h(b_rap) != SHA_RAPPORT:
    arret("empreinte du rapport de contre-lecture inattendue")
src, rap = b_src.decode("utf-8"), b_rap.decode("utf-8")

# § 4 du rapport : couples exigés
debut, fin = rap.index("## 4. Corrections exigées"), rap.index("## 5. Remarques facultatives")
sec = rap[debut:fin]
motif = re.compile(r"^\*\*(?P<id>[Mm]\d+(?:-[ab-c])?)\*\* \((?:majeure|mineure)\)[^\n]*\n\nAncien :\n\n```text\n(?P<a>.*?)\n```"
                   r"\n\nNouveau :\n\n```text\n(?P<n>.*?)\n```", re.S | re.M)
couples = {m["id"]: (m["a"], m["n"]) for m in motif.finditer(sec)}
if sorted(couples) != sorted(EXIGES):
    arret(f"couples tirés du rapport : {sorted(couples)} ≠ {sorted(EXIGES)}")

HEURE = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True, check=True).stdout.strip()
TETE = subprocess.run(["git", "--no-optional-locks", "-C", "/home/user/controle-ia-travail", "rev-parse", "main"],
                      capture_output=True, text=True, check=True).stdout.strip()

# Couple du rédacteur : en-tête (version, heure, lieu)
EN_TETE_A = """  commit, aucune poussée.
- **Statut et lieu** : rédigé comme brouillon 1, `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-2-v1-brouillon1.md`,
  scellé par son compagnon comme pièce de travail (R6) ;"""
EN_TETE_N = f"""  commit, aucune poussée.
- **Version : brouillon 2.** Corrections de la contre-lecture du tour 1 appliquées par un rédacteur neuf, sous-agent de la
  session mère, qui n'a écrit ni le brouillon 1, ni son rapport de contre-lecture, ni [T], ni [AE], ni le code : couples
  « ancien → nouveau » appliqués par le programme
  `docs/notes/organisme-idees-juge-v1/appliquer-corrections-addendum-relance-idee-1-2-v1-brouillon2.py` (scellé à côté)
  au brouillon 1 (`{SHA_SOURCE}`) ; dépôt lu sur `main`, tête `{TETE}` ; heure du scellement
  {HEURE} (`date -u`) ; aucun commit, aucune poussée. Rien d'autre que ces corrections, cet en-tête et la section
  « Contre-lecture » n'a changé.
- **Statut et lieu** : rédigé comme brouillon 2, `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-2-v1-brouillon2.md`,
  scellé par son compagnon comme pièce de travail (R6) ;"""

# Couple m10 appliqué en substance : section « Contre-lecture »
M10_N = f"""- **Contre-lecture 1** (R2) — lecteur neuf, sous-agent de la session mère (lettre du modèle : inscrite par la mère au
  registre), qui n'a écrit ni ce brouillon ni aucune pièce de l'idée 1.2 ; texte relu : brouillon 1,
  `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-2-v1-brouillon1.md`,
  `{SHA_SOURCE}` ; rapport :
  `docs/notes/organisme-idees-juge-v1/contre-lecture-addendum-relance-idee-1-2-tour1-v1.md`,
  `{SHA_RAPPORT}` (égal à son compagnon) ; programme de l'annexe A
  rejoué le 2026-11-16 à 12:21:47Z sur la tête `1332acb3` de `main` : même sortie, aux heures, à la tête, à la durée de
  marche de la machine et aux empreintes des registres près. Verdict : « corrections » (2 majeures, 11 mineures, en 17
  couples exigés ; 3 couples facultatifs ; remarques F4 à F10 sans couple) ; « la conception n'est pas en cause ».
- **Traitement** (brouillon 2) — chaque couple exigé est tiré du § 4 du rapport par programme ; chaque « ancien » figure
  une seule fois dans le brouillon 1 ; aucun chevauchement :
  - **M1** (§ 5, consigne : attente qui se termine d'elle-même avant la limite de l'outil, réarmée à chaque fin ; décision
    (vi) de la mère) : appliqué.
  - **M2** (4.10 neuf : jeu relancé en même temps que le jeu de l'idée 1.1 sur la même machine, conséquences sur la durée
    et sur la borne de 24 heures ; décision (v)) : appliqué.
  - **m1** (nom `…-addendum-relance-v1.md` confirmé, « v2 » de R-2964 erreur de plume ; décision (i)) : appliqué.
  - **m2** (pas de mot nouveau de Lazar, avec ses raisons ; décision (iv)) : appliqué.
  - **m3-a, m3-b, m3-c** (voie (a) retenue par la mère ; décision (ii)) : appliqués.
  - **m4** (instant de l'arrêt ≈ 04:36Z, non 06:13Z) : appliqué.
  - **m5** (trois reprises au moins ; sort de l'attente) : appliqué tel que proposé. La lecture « deux attentes menées
    jusqu'à la limite de l'outil, la seconde non réarmée » est celle du contre-lecteur, tirée des seules heures et tailles
    des fichiers ; le rédacteur du brouillon 2 ne l'a pas confirmée sur le journal de la mère, qu'il n'a pas lu ; elle
    concorde avec la décision (vi). Si le journal de la mère la dément, elle est corrigée avant la recopie sous `prereg/`,
    les heures, qui sont des faits, gardées.
  - **m6, m7-a, m7-b, m8, m9** : appliqués.
  - **m10** : appliqué en substance — cette section ; l'empreinte entière du rapport et le traitement y sont écrits
    directement, au lieu des mots que le « nouveau » du rapport laissait à la mère.
  - **m11-a, m11-b** (espace disque) : appliqués ; le seuil de 1 Go reste celui que propose le rapport, à fixer par la
    mère (rapport, § 6, point 4).
  - **f1, f2, f3** (facultatifs) : non appliqués ; le brouillon 2 est borné aux corrections exigées ; laissés à la mère.
  - **F4 à F10** (sans couple) : non appliqués ; laissés à la mère, F4 (comparaison des deux oracles après le prononcé)
    étant à trancher avant le scellement sous `prereg/` si elle la veut permise.
  - **Rapport, § 6, points 4, 5, 6 et 9** (variante de la voie (a) si la place manque ; déclaration symétrique dans
    l'addendum de l'idée 1.1 ; limite d'usage de la session ; lettre du modèle) : à la mère, hors de cette pièce.
  - **Rapport, § 6, point 7** : recompté par le programme sur le brouillon 2 : zéro ligne au format du lanceur.
- **Les six décisions de la mère, où elles sont écrites** : (i) nom du texte qui fera foi, en-tête (m1) ; (ii) voie (a),
  § 6 (m3) ; (iii) contrôle des versions de l'interpréteur avant le lancement, 4.2 (présent dès le brouillon 1,
  inchangé) ; (iv) aucun mot nouveau du directeur, 4.9 (m2) ; (v) jeu en même temps que celui de l'idée 1.1, 4.10 (M2) ;
  (vi) tâche active pendant tout le jeu, attente bornée réarmée à chaque fin, § 5 (M1)."""

paires = [(k, *couples[k]) for k in EXIGES if k != "m10"]
paires.append(("m10 (en substance)", couples["m10"][0], M10_N))
paires.append(("en-tête", EN_TETE_A, EN_TETE_N))

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
for marqueur in ("À REMPLIR", "à confirmer par elle", "plus long délai"):
    if marqueur in texte:
        arret(f"marqueur « {marqueur} » encore présent")
if n_lanceur != 0:
    arret(f"{n_lanceur} ligne(s) au format du lanceur")
if CIBLE.exists():
    arret(f"{CIBLE.name} existe déjà : R12 interdit d'écraser")
with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(texte)
print("couples appliqués :", len(paires), "; lignes au format du lanceur :", n_lanceur)
print("heure (date -u) :", HEURE, "; tête de main :", TETE)
print("cible :", CIBLE, h(CIBLE.read_bytes()))

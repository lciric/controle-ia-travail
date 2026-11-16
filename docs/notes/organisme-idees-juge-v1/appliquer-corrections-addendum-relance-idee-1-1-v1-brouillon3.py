"""Brouillon 3 de l'addendum de relance de l'idée 1.1 : applique au brouillon 2 le couple « ancien → nouveau » exigé par
la contre-lecture du tour 2 (d-1), plus deux couples du rédacteur (en-tête ; section « Contre-lecture », § 7), et rien
d'autre.

- vérifie l'empreinte du brouillon 2 et celle du rapport de contre-lecture du tour 2 ;
- tire le couple exigé (d-1) du § 3 du rapport, par programme (aucune recopie à la main) ; les remarques facultatives g-1
  et g-2 du § 4 ne sont pas appliquées (déclaré dans la section « Contre-lecture ») ;
- exige que chaque « ancien » figure exactement une fois dans le brouillon 2 et qu'aucun couple n'en chevauche un autre ;
- exige, après application, zéro ligne au format du lanceur (« empreinte, deux espaces, chemin »), zéro ligne qui commence
  par 64 caractères hexadécimaux, et que chaque « nouveau » figure dans la cible ;
- refuse d'écraser la cible.
Lancé par `python3 -I -B` ; commandes légères seulement ; aucun fichier du run invalide n'est ouvert.
"""
import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")
DOSSIER = DEPOT / "docs/notes/organisme-idees-juge-v1"
SOURCE = DOSSIER / "addendum-relance-idee-1-1-v1-brouillon2.md"
SHA_SOURCE = "566304ede89c8aab86682bd9a7602e20b307e97fadce2071ea46ffed87a3ee4a"
RAPPORT = DOSSIER / "contre-lecture-addendum-relance-idee-1-1-tour2-v1.md"
SHA_RAPPORT = "9460579c29d43f9129c96657a38ebacea899aac03288502ee078c5319f965675"
PROG_B2 = DOSSIER / "appliquer-corrections-addendum-relance-idee-1-1-v1-brouillon2.py"
SHA_PROG_B2 = "0316488690ffc88c2c2826cfd992334da8a68c6c5af92fa6214be381106459ff"
CIBLE = DOSSIER / "addendum-relance-idee-1-1-v1-brouillon3.md"
PROGRAMME = "docs/notes/organisme-idees-juge-v1/appliquer-corrections-addendum-relance-idee-1-1-v1-brouillon3.py"
MOTIF_LANCEUR = re.compile(r"^([0-9a-f]{64})  (\S+)\s*$", re.M)     # expression de `execution_v1.verifier_addendum`
MOTIF_HEX = re.compile(r"^[0-9a-f]{64}", re.M)
EXIGES = ["d-1"]


def h(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def arret(msg: str):
    print("ARRÊT :", msg, file=sys.stderr)
    sys.exit(1)


def deballer(s: str) -> str:
    """Retire les délimiteurs de code qui entourent un « ancien » ou un « nouveau » du rapport."""
    s = s.rstrip("\n")
    if s.startswith("`") and s.endswith("`") and len(s) > 2:
        return s[1:-1]
    arret(f"délimiteurs inattendus : {s[:60]!r}")


if CIBLE.exists():
    arret(f"{CIBLE.name} existe déjà : R12 interdit d'écraser")
b_src, b_rap = SOURCE.read_bytes(), RAPPORT.read_bytes()
if h(b_src) != SHA_SOURCE:
    arret("empreinte du brouillon 2 inattendue")
if h(b_rap) != SHA_RAPPORT:
    arret("empreinte du rapport de contre-lecture du tour 2 inattendue")
if h(PROG_B2.read_bytes()) != SHA_PROG_B2:
    arret("empreinte du programme d'application du brouillon 2 inattendue")
src, rap = b_src.decode("utf-8"), b_rap.decode("utf-8")

# § 3 du rapport : couple exigé
debut, fin = rap.index("## 3. Correction exigée"), rap.index("## 4. Remarques facultatives")
sec = rap[debut:fin]
motif = re.compile(r"^\*\*(?P<id>d-\d) — [^\n]*\n(?:[^\n]*\n)*?\n- ancien : (?P<a>[^\n]*)\n- nouveau : (?P<n>[^\n]*)$", re.M)
couples = {m["id"]: (deballer(m["a"]), deballer(m["n"])) for m in motif.finditer(sec)}
if sorted(couples) != EXIGES:
    arret(f"couples tirés du rapport : {sorted(couples)} ≠ {EXIGES}")

HEURE = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True, check=True).stdout.strip()
TETE = subprocess.run(["git", "-C", str(DEPOT), "rev-parse", "main"], capture_output=True, text=True, check=True,
                      env={**os.environ, "GIT_OPTIONAL_LOCKS": "0"}).stdout.strip()

# Couple du rédacteur : en-tête (version, heure, lieu)
EN_TETE_A = """- **Statut et lieu** : brouillon 2, `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-1-v1-brouillon2.md`, scellé
  par son compagnon comme pièce de travail (R6) ;"""
EN_TETE_N = f"""- **Version : brouillon 3.** Correction de la contre-lecture du tour 2 (lecture du brouillon 2) appliquée par un
  rédacteur neuf, lettre C, sous-agent de la session mère, qui n'a écrit ni les brouillons 1 et 2, ni leur programme
  d'application, ni les rapports de contre-lecture des tours 1 et 2, ni [T], ni [AE], ni le code, ni l'étape 0 : couples
  « ancien → nouveau » appliqués par le programme
  `{PROGRAMME}` (scellé à côté)
  au brouillon 2 (`{SHA_SOURCE}`) ; dépôt lu sur `main`, tête `{TETE}` ; heure du scellement
  {HEURE} (`date -u`) ; aucun commit, aucune poussée. Rien d'autre que cette correction, cet en-tête et la section
  « Contre-lecture » (§ 7) n'a changé ; la déclaration du § 8 reste celle du rédacteur du brouillon 1.
- **Statut et lieu** : brouillon 3, `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-1-v1-brouillon3.md`, scellé
  par son compagnon comme pièce de travail (R6) ;"""

# Couple du rédacteur : section « Contre-lecture » (§ 7), entrée du tour 2
CL_A = """- **Contre-lecture 2** : à faire (R2), par un lecteur neuf qui n'a écrit ni les brouillons, ni le rapport du tour 1, ni
  [T], ni [AE], ni le code, ni l'étape 0.
"""
CL_N = f"""- **Contre-lecture 2** (R2) — lecteur neuf, sous-agent de la session mère, lettre C, qui n'a écrit ni la pièce, ni le
  rapport du tour 1, ni [T], ni [AE], ni le code, ni l'étape 0 ; texte relu en entier : brouillon 2,
  `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-1-v1-brouillon2.md`,
  `{SHA_SOURCE}` ; rapport :
  `docs/notes/organisme-idees-juge-v1/contre-lecture-addendum-relance-idee-1-1-tour2-v1.md`,
  `{SHA_RAPPORT}` (égal à son compagnon) ; lu le 2026-11-16 de
  20:37Z à 20:39Z sur la tête `a6bc9938` de `main` ; différentiel brouillon 1 / brouillon 2 : six zones, rien d'autre ;
  programme de l'annexe A rejoué de 20:38:02Z à 20:38:05Z : sortie identique à la recopie, aux trois seules lignes d'heure
  près. Verdict : « corrections » — 0 majeure, 1 mineure (un couple exigé, d-1), 2 remarques facultatives (g-1, g-2) ;
  « la conception n'est pas en cause ». c-1, c-2 et c-4 jugés appliqués mot pour mot ; c-3 appliqué à un renvoi près
  (« [T] l. 492-493 »), écart jugé justifié et accepté.
- **Traitement** (brouillon 3) — le couple exigé est tiré du § 3 du rapport par programme ; son « ancien » figure une seule
  fois dans le brouillon 2 ; aucun chevauchement avec les deux couples du rédacteur (en-tête, cette entrée) :
  - **d-1** (en-tête, puce « Version : brouillon 2 » : lettre et statut du rédacteur des corrections du tour 1) : appliqué
    tel quel. D'après la consigne du tour, les corrections du brouillon 2 ont été faites par le modèle A, celui du
    brouillon 1 ; le cas réservé par le rapport (corrections appliquées en fait par un rédacteur de lettre C) n'est donc
    pas celui-ci.
  - **Incohérence déclarée** (rapport, § 3, dernier alinéa) : le programme d'application du brouillon 2,
    `docs/notes/organisme-idees-juge-v1/appliquer-corrections-addendum-relance-idee-1-1-v1-brouillon2.py`
    (`{SHA_PROG_B2}`, égal à son compagnon), porte encore dans `EN_TETE_N`
    l'ancien texte (« rédacteur neuf, lettre C, […] qui n'a écrit ni le brouillon 1 ») ; il reste tel quel (R12 : on
    n'écrase pas une pièce scellée) et ne fait pas foi sur ce point : l'en-tête corrigé par d-1 l'emporte. Rejoué, il
    refuserait d'ailleurs d'écrire, sa cible existant déjà.
  - **g-1** (« ce brouillon », au § 3, désigne le brouillon 1) : non appliqué ; facultatif, laissé au nettoyage de la
    recopie sous `prereg/`, comme le propose le rapport ; le § 8 dit déjà que la déclaration reste celle du rédacteur du
    brouillon 1.
  - **g-2** (f-1 à f-4 du tour 1 non appliqués, choix jugé recevable) : rien à faire ; choix maintenu.
- **Points pour la mère (rapport du tour 2, § 5)** : point 1 (lettre du rédacteur des corrections) : réglé par d-1, sur la
  consigne du tour ; à corriger par la mère si elle sait autrement. Points 2 (D7 à demander à Lazar en toutes lettres avec
  la question de R-3010 ; sans son mot, aucune machine louée ne part), 3 (`--reprendre` accepté par le code dans la copie
  du run invalide ; l'opérateur ne le passe jamais) et 4 (risque du lieu (i) ; égalité au bit près non garantie sur un
  autre processeur) : à la mère, hors de cette pièce, qui en dit déjà ce qui la concerne (4.2, 4.4, 4.10 et § 5). Point 5 :
  à la recopie sous `prereg/`, recompter les lignes au format du lanceur (attendu 0), recalculer les empreintes du § 8 et
  compléter cette section. Recompté par le programme sur le brouillon 3 : zéro ligne au format du lanceur, zéro ligne qui
  commence par 64 caractères hexadécimaux.
- **Contre-lecture 3** : le rapport du tour 2 juge la pièce scellable une fois d-1 réglé ; un tour 3, s'il est demandé par
  la mère, se fait par un lecteur neuf (R2) qui n'a écrit ni les brouillons, ni leurs programmes d'application, ni les
  rapports des tours 1 et 2, ni [T], ni [AE], ni le code, ni l'étape 0.
"""

tous = [(k, *couples[k]) for k in EXIGES] + [("en-tête", EN_TETE_A, EN_TETE_N), ("contre-lecture", CL_A, CL_N)]
spans = []
for k, a, _ in tous:
    n = src.count(a)
    if n != 1:
        arret(f"{k} : « ancien » trouvé {n} fois dans le brouillon 2")
    i = src.index(a)
    spans.append((i, i + len(a), k))
spans.sort()
for (d1, f1, k1), (d2, f2, k2) in zip(spans, spans[1:]):
    if d2 < f1:
        arret(f"chevauchement : {k1} et {k2}")

nouveau = src
for k, a, n in tous:
    nouveau = nouveau.replace(a, n, 1)
for k, _, n in tous:
    if n not in nouveau:
        arret(f"{k} : « nouveau » absent de la cible")
n_l, n_x = len(MOTIF_LANCEUR.findall(nouveau)), len(MOTIF_HEX.findall(nouveau))
if n_l or n_x:
    arret(f"lignes au format du lanceur : {n_l} ; lignes qui commencent par 64 caractères hexadécimaux : {n_x}")
if CIBLE.exists():
    arret(f"{CIBLE.name} existe déjà : R12 interdit d'écraser")
with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(nouveau)
print("heure (date -u) :", HEURE)
print("tête de main :", TETE)
print("couples appliqués :", ", ".join(k for k, _, _ in tous))
print("lignes au format du lanceur :", n_l, "; lignes qui commencent par 64 caractères hexadécimaux :", n_x)
print("lignes : brouillon 2", src.count("\n"), "; brouillon 3", nouveau.count("\n"))
print("empreinte de la cible :", h(nouveau.encode("utf-8")))

"""Brouillon 2 de l'addendum de relance de l'idée 1.1 : applique au brouillon 1 les couples « ancien → nouveau » exigés
par la contre-lecture du tour 1 (c-1 à c-4), plus deux couples du rédacteur (en-tête ; section « Contre-lecture », § 7),
et rien d'autre.

- vérifie l'empreinte du brouillon 1 et celle du rapport de contre-lecture ;
- tire les 4 couples exigés du § 2 du rapport, par programme (aucune recopie à la main) ; les remarques facultatives f-1
  à f-4 du § 3 ne sont pas appliquées ;
- c-3 est appliqué à un renvoi près : « [T] l. 492 » devient « [T] l. 492-493 » (les mots de [T] sur l'essai d'égalité E0
  s'étendent sur ces deux lignes) ; ce changement est déclaré dans la section « Contre-lecture » ;
- exige que chaque « ancien » figure exactement une fois dans le brouillon 1 et qu'aucun couple n'en chevauche un autre ;
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
SOURCE = DOSSIER / "addendum-relance-idee-1-1-v1-brouillon1.md"
SHA_SOURCE = "009d8bbf5acd5c5ff48b6adcf5cca3e2232d33a94f6e69ebc2facec105148ee1"
RAPPORT = DOSSIER / "contre-lecture-addendum-relance-idee-1-1-tour1-v1.md"
SHA_RAPPORT = "aaacb41501553702deeda80d12a692ee1c1e485ef8f7f0ed87cfa080f5b6b51e"
CIBLE = DOSSIER / "addendum-relance-idee-1-1-v1-brouillon2.md"
PROGRAMME = "docs/notes/organisme-idees-juge-v1/appliquer-corrections-addendum-relance-idee-1-1-v1-brouillon2.py"
MOTIF_LANCEUR = re.compile(r"^([0-9a-f]{64})  (\S+)\s*$", re.M)     # expression de `execution_v1.verifier_addendum`
MOTIF_HEX = re.compile(r"^[0-9a-f]{64}", re.M)
EXIGES = ["c-1", "c-2", "c-3", "c-4"]


def h(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def arret(msg: str):
    print("ARRÊT :", msg, file=sys.stderr)
    sys.exit(1)


def deballer(s: str) -> str:
    """Retire les délimiteurs de code qui entourent un « ancien » ou un « nouveau » du rapport."""
    s = s.rstrip("\n")
    if s.startswith("`` ") and s.endswith(" ``"):
        return s[3:-3]
    if s.startswith("`") and s.endswith("`"):
        return s[1:-1]
    arret(f"délimiteurs inattendus : {s[:60]!r}")


if CIBLE.exists():
    arret(f"{CIBLE.name} existe déjà : R12 interdit d'écraser")
b_src, b_rap = SOURCE.read_bytes(), RAPPORT.read_bytes()
if h(b_src) != SHA_SOURCE:
    arret("empreinte du brouillon 1 inattendue")
if h(b_rap) != SHA_RAPPORT:
    arret("empreinte du rapport de contre-lecture inattendue")
src, rap = b_src.decode("utf-8"), b_rap.decode("utf-8")

# § 2 du rapport : couples exigés
debut, fin = rap.index("## 2. Corrections exigées"), rap.index("## 3. Remarques facultatives")
sec = rap[debut:fin]
motif = re.compile(r"^\*\*(?P<id>c-\d) — [^\n]*\n(?:[^\n]*\n)*?\n- ancien : (?P<a>[^\n]*)\n- nouveau : (?P<n>[^\n]*)$", re.M)
couples = {m["id"]: (deballer(m["a"]), deballer(m["n"])) for m in motif.finditer(sec)}
if sorted(couples) != EXIGES:
    arret(f"couples tirés du rapport : {sorted(couples)} ≠ {EXIGES}")

# c-3 : renvoi à [T] porté aux deux lignes où s'étendent ses mots (annexe A, [7] : l. 492 et 493)
a3, n3 = couples["c-3"]
if n3.count("[T] l. 492 ;") != 1:
    arret("c-3 : renvoi « [T] l. 492 ; » introuvable ou multiple dans le « nouveau »")
couples["c-3"] = (a3, n3.replace("[T] l. 492 ;", "[T] l. 492-493 ;"))

HEURE = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True, check=True).stdout.strip()
TETE = subprocess.run(["git", "-C", str(DEPOT), "rev-parse", "main"], capture_output=True, text=True, check=True,
                      env={**os.environ, "GIT_OPTIONAL_LOCKS": "0"}).stdout.strip()

# Couple du rédacteur : en-tête (version, heure, lieu)
EN_TETE_A = """- **Statut et lieu** : brouillon 1, `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-1-v1-brouillon1.md`, scellé
  par son compagnon comme pièce de travail (R6) ;"""
EN_TETE_N = f"""- **Version : brouillon 2.** Corrections de la contre-lecture du tour 1 (lecture du brouillon 1) appliquées par un
  rédacteur neuf, lettre C, sous-agent de la session mère, qui n'a écrit ni le brouillon 1, ni son rapport de
  contre-lecture, ni [T], ni [AE], ni le code, ni l'étape 0 : couples « ancien → nouveau » appliqués par le programme
  `{PROGRAMME}` (scellé à côté)
  au brouillon 1 (`{SHA_SOURCE}`) ; dépôt lu sur `main`, tête `{TETE}` ; heure du scellement
  {HEURE} (`date -u`) ; aucun commit, aucune poussée. Rien d'autre que ces corrections, cet en-tête et la section
  « Contre-lecture » (§ 7) n'a changé ; la déclaration du § 8 reste celle du rédacteur du brouillon 1.
- **Statut et lieu** : brouillon 2, `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-1-v1-brouillon2.md`, scellé
  par son compagnon comme pièce de travail (R6) ;"""

# Couple du rédacteur : section « Contre-lecture » (§ 7)
CL_A = """## 7. Contre-lecture

À faire (R2) : lecteur neuf, qui n'a écrit ni ce brouillon, ni [T], ni [AE], ni le code, ni l'étape 0. Points que le
rédacteur lui signale :

1. **Lieu (ii) et D7** (4.10) : la lettre de [T] l. 629 et 660 fait d'une machine louée un écart au texte scellé, au-delà du
   devis et du GO ; le lecteur dira si cette lecture est juste et si l'addendum peut, comme demandé, « valoir pour les deux
   lieux sans rien changer d'autre » en ne faisant que déclarer cet écart.
2. **Branche de reprise** (4.4) : le code accepterait `--reprendre` dans la copie du run invalide ; seule la règle de [AE]
   et de cet addendum l'interdit.
3. **Égalité au bit près** (4.2) : limite déclarée sur un autre processeur ; le lecteur dira si elle doit peser sur le
   choix du lieu.
4. **Zéro ligne au format du lanceur** : recompté par programme sur ce brouillon (§ 8) ; à recompter sur la copie sous
   `prereg/`.
"""
CL_N = f"""## 7. Contre-lecture

- **Contre-lecture 1** (R2) — lecteur neuf, sous-agent de la session mère, lettre C, qui n'a écrit ni la pièce, ni [T],
  ni [AE], ni le code, ni l'étape 0 ; texte relu en entier : brouillon 1,
  `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-1-v1-brouillon1.md`,
  `{SHA_SOURCE}` ; rapport :
  `docs/notes/organisme-idees-juge-v1/contre-lecture-addendum-relance-idee-1-1-tour1-v1.md`,
  `{SHA_RAPPORT}` (égal à son compagnon) ; lu le 2026-11-16 de
  20:28:53Z à 20:33Z sur la tête `a6bc9938` de `main` ; programme de l'annexe A rejoué de 20:29:08Z à 20:29:11Z : sortie
  identique à la recopie, aux trois seules lignes d'heure près. Verdict : « corrections » — 0 majeure, 4 mineures (4 couples
  exigés, c-1 à c-4), 4 remarques facultatives (f-1 à f-4) ; « la conception n'est pas en cause ».
- **Sept points du rapport (§ 1)** : cause et qualification « run invalide », preuves (rejouées), conditions de la relance,
  consigne de tâche active et seconde interruption, format et hygiène : conformes ; validité pour les deux lieux : oui, sous
  c-4 ; « mêmes tirages » : confirmé par le code, avec deux précisions, objets de c-1 à c-3.
- **Traitement** (brouillon 2) — chaque couple exigé est tiré du § 2 du rapport par programme ; chaque « ancien » figure
  une seule fois dans le brouillon 1 ; aucun chevauchement :
  - **c-1** (4.2, dernier alinéa : temps de calcul de chaque répétition, `temps_s`) : appliqué tel quel.
  - **c-2** (§ 3, dernière puce : « durées » précisées) : appliqué tel quel.
  - **c-3** (4.2, première puce : clé de l'essai d'égalité E0) : appliqué, à un renvoi près. Le « nouveau » du rapport
    cite « [T] l. 492 » ; les mots de [T] « essai d'égalité E0 `(98, r)` » s'étendent sur les lignes 492 et 493 (annexe A,
    [7]) ; le renvoi écrit est donc « [T] l. 492-493 ». Les clés écrites, `(98, r, 0)` et `(98, r, 1)`, sont celles du
    code : `cle=(98, r)` à `etape0_idee_1_1_v5.py` l. 174, prolongée par 0 ou par 1 dans le banc (l. 481 et 636).
  - **c-4** (4.10, lieu (ii) : sans le mot de Lazar sur D7, consigné à `registres/go.md`, aucune machine louée ne part
    sous cet addendum) : appliqué tel quel.
  - **f-1 à f-4** (facultatifs : « parmi les sept relevés » ; liens durs des paquets de `.git` et disque ; aléa de hachage
    de Python ; charge de la machine) : non appliqués ; le brouillon 2 est borné aux corrections exigées, comme les
    brouillons de [R12] ; laissés à la mère.
- **Points pour la mère (rapport, § 4)** : points 1 (écart D7 à dire en toutes lettres dans la question de R-3010), 2 (PID
  4953 de la relance de l'idée 1.2, absent à 20:31Z), 3 (risque du lieu (i)), 4 (`--reprendre` accepté par le code) et 5
  (égalité au bit près) : à la mère, hors de cette pièce, qui en dit déjà ce qui la concerne (4.2, 4.4, 4.10 et § 5).
  Point 6 : tour 2 par un lecteur neuf (ci-dessous) ; à la recopie sous `prereg/`, recompter les lignes au format du
  lanceur et recalculer les empreintes du § 8. Point 7 : cette entrée.
- **Points que le rédacteur du brouillon 1 signalait au lecteur**, avec la réponse du rapport :
  1. **Lieu (ii) et D7** (4.10) : lecture juste (rapport, § 1, point 6) ; l'addendum vaut pour les deux lieux sous c-4,
     appliquée.
  2. **Branche de reprise** (4.4) : exact (rapport, § 1, point 4) ; l'opérateur ne passe jamais `--reprendre`.
  3. **Égalité au bit près** (4.2) : sans effet sur la validité ; elle peut peser, à la marge, pour le lieu (ii) (rapport,
     § 4, point 5).
  4. **Zéro ligne au format du lanceur** : zéro sur le brouillon 1 (rapport, § 1, point 7) ; recompté par le programme sur
     le brouillon 2 : zéro ligne au format du lanceur, zéro ligne qui commence par 64 caractères hexadécimaux ; à
     recompter sur la copie sous `prereg/`.
- **Contre-lecture 2** : à faire (R2), par un lecteur neuf qui n'a écrit ni les brouillons, ni le rapport du tour 1, ni
  [T], ni [AE], ni le code, ni l'étape 0.
"""

tous = [(k, *couples[k]) for k in EXIGES] + [("en-tête", EN_TETE_A, EN_TETE_N), ("contre-lecture", CL_A, CL_N)]
spans = []
for k, a, _ in tous:
    n = src.count(a)
    if n != 1:
        arret(f"{k} : « ancien » trouvé {n} fois dans le brouillon 1")
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
print("lignes : brouillon 1", src.count("\n"), "; brouillon 2", nouveau.count("\n"))
print("empreinte de la cible :", h(nouveau.encode("utf-8")))

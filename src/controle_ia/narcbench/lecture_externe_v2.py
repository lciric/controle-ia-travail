"""Commande de la lecture du bras externe NARCBench, v2 — **ne se lance qu'après le scellement du texte court et l'inscription de
la ligne de code** (R1) ; processeur, 0 USD (R-2175, D-3 (a)). Écrite par le développeur v2, corrigée après la contre-lecture
du code (`contre-lecture-code-externe-v2-v1.md`, `9b90884a…`), les contre-lectures 1 et 2 du texte court (`…-brouillon1-cl1.md`,
`9217284f…` ; `…-brouillon2-cl2.md`, `f813ece0…`) et alignée sur le brouillon 2 (`prereg/narcbench-bras-externe-v1-brouillon2.md`,
`7bb21dc0…`, numéros de sa liste d'arrêt) ; **jamais jouée sur les données réelles**.

**Registre propre, fixé** : `registres/narcbench-externe-v1.md` **du dépôt** (aucune option `--registre`), lignes
`| CLÉ | AAAA-MM-JJTHH:MM:SSZ | chemin relatif | sha256 |` (format de `t07/registre_v1`), trois clés seulement :
`SCELLEMENT-NARC-EXT` (le texte scellé), `CODE-NARC-EXT` (la fiche du code, JSON scellé), `LECTURE-NARC-EXT` (écrite par la mère
après la lecture).

**Configuration canonique** (`lire_configuration_texte` ; contrôle préalable `verifier-texte`) : sous le titre exact
`## Configuration canonique de la commande`, **six lignes seules** `clé : valeur` (une espace de part et d'autre du deux-points,
rien d'autre sur la ligne ; lignes vides et clôtures ```` ``` ```` tolérées, toute autre ligne refusée), chacune **la seule ligne du
texte entier** qui commence par `<clé> :` :
    augmentation : papier                                  (papier | code ; égale à --augmentation)
    couches-familles : bande                               (bande | qwen3_32b=<c>[+<c>…];llama_3_1_70b=<c>[+<c>…] ; égale à --couches-familles)
    run-id : AAAAMMJJ-HHMMSS-narc-externe-v2               (la forme, exactement ; --run-id doit la suivre, date et heure valides)
    registre : registres/narcbench-externe-v1.md           (exactement le registre fixé)
    texte : prereg/narcbench-bras-externe-v1.md            (chemin relatif ; égal à --texte et au chemin de SCELLEMENT-NARC-EXT)
    Entropie : <entier>                                    (chiffres seuls, ≥ 2³² = 4 294 967 296 ; égal à --entropie, en entier)

Ordre (plan d'analyse n° 2 du texte) ; chaque étape arrête tout au premier écart (R5, aucun repli silencieux) :
1. **n° 3, registre** (refus, code 2) : `SCELLEMENT-NARC-EXT` et `CODE-NARC-EXT` exactement une fois, bien formées,
   strictement antérieures à l'ouverture, `CODE` strictement postérieure à `SCELLEMENT`, sceaux conformes ; toute autre clé
   → refus (`LECTURE-NARC-EXT` présente : n° 4, « déjà jouée », nœud) ; texte cité conforme au gabarit des préenregistrements ;
2. **n° 5, configuration** (refus, code 2) : section et six lignes, comparées aux options ;
3. **n° 6, commit** (arrêt, code 1) : `--depot` racine du dépôt git, arbre propre, fiche cohérente (commit présent, HEAD ou un
   ancêtre, liste des `src/controle_ia/narcbench/*.py` égale), **paquet `controle_ia` exécuté égal fichier pour fichier à
   `src/controle_ia/` du commit de la fiche** (règle DF-02 de T0.7) ;
4. **n° 4, déjà jouée** (refus, code 2) : dossier `runs/*-narc-externe-v2` ou résultat `diag/*/externe-narcbench-v2.json` ;
5. **n° 7, scikit-learn** (arrêt, code 1) : version installée = version de la fiche = 1.9.1, sinon rien n'est lu ;
6. **n° 2, transfert ; n° 1, données** (arrêt, code 1) : aucun dossier ni fichier de l'étage de transfert sous les données ;
   tailles et empreintes des huit fichiers (R11) ;
7. **n° 8 et 9 sur les métadonnées** (arrêt, code 1, avant le manifeste ; écart A28 : décision de texte) : deux colludeurs par
   épisode de collusion et aucun dans un témoin, pour **toutes** les procédures ; exclusions par étage et modèle, plus de 10 %
   → arrêt, nœud ; plis gardés par modèle (ils nomment des graines) ;
8. manifeste du run (`decisif=False`, graines par `SeedSequence` de l'entropie du texte, une tâche par tirage, R9) ;
   ouverture des activations ; témoin (`reproduire_helios_v2`, scores gardés), cellules, règles C et T, phrases, réponse
   (`cellules_externe_v2`), comptes structurels (écart A19), garde de reproduction rapportée sans valeur de lecture ; mémoire
   insuffisante (n° 11) → arrêt, nœud ; résultat sans valeur non finie, scellé `diag/<run_id>/externe-narcbench-v2.json`.

Journal (écart A23 : le brouillon 2 dit « aucun journal », la contre-lecture 2 recommande de le garder ; décision de texte) :
`registres/narcbench-externe-v1.md.ouvertures.md`, lignes `REFUS-NARC-EXT` (tout arrêt avant l'ouverture), `OUVERTURE-NARC-EXT`,
`ARRET-NARC-EXT` ; rien si `registres/` manque ; il salit l'arbre : la mère le committe avant toute relance.

Contrôles préalables, sans registre ni données (avant de sceller le texte ou d'inscrire la ligne de code) :
    PYTHONPATH=src python -m controle_ia.narcbench.lecture_externe_v2 verifier-texte prereg/<texte>.md
    PYTHONPATH=src python -m controle_ia.narcbench.lecture_externe_v2 fiche-code --depot . --commit <40 caractères>
Lecture (racine du dépôt ; les valeurs viennent du texte scellé) :
    PYTHONPATH=src:/home/user/narcbench-paquets-v2 .venv/bin/python -m controle_ia.narcbench.lecture_externe_v2 --depot . \
        --texte prereg/narcbench-bras-externe-v1.md --donnees /home/user/narcbench-donnees-v2 \
        --run-id <AAAAMMJJ-HHMMSS>-narc-externe-v2 --entropie <entier du texte> --augmentation papier --couches-familles bande
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
import math
import re
import subprocess
import sys
from datetime import datetime, timezone
from importlib import metadata
from pathlib import Path

import numpy as np

import controle_ia

from .. import prereg
from ..gardes import GardeArret, etat_git
from ..manifeste import creer_manifeste, ecrire_resultat, generateur
from ..t07.registre_v1 import CLE, DATE, FORMAT_DATE, SHA, RefusRegistre, date_utc, sceau_conforme, sha256_de
from . import cellules_externe_v2 as CE
from . import chargeur_externe_v1 as C
from . import externe_v2 as X2

REGISTRE = "registres/narcbench-externe-v1.md"
JOURNAL = REGISTRE + ".ouvertures.md"
CLE_SCELLEMENT, CLE_CODE, CLE_LECTURE = "SCELLEMENT-NARC-EXT", "CODE-NARC-EXT", "LECTURE-NARC-EXT"
CLES_BRAS = (CLE_SCELLEMENT, CLE_CODE, CLE_LECTURE)
SECTION_CONFIGURATION = "Configuration canonique de la commande"
CLES_CONFIGURATION = ("augmentation", "couches-familles", "run-id", "registre", "texte", "Entropie")
FORME_RUN = "AAAAMMJJ-HHMMSS-narc-externe-v2"
MOTIF_RUN = re.compile(r"[0-9]{8}-[0-9]{6}-narc-externe-v2")
SUFFIXE_RUN = "narc-externe-v2"
ENTROPIE_MINIMALE = 2 ** 32
VERSION_SKLEARN = "1.9.1"
PREFIXE_PAQUET = "src/controle_ia/"
PREFIXE_FICHE = "src/controle_ia/narcbench/"
COMMIT = re.compile(r"[0-9a-f]{40}")
NOMS_PUBLIES = {"qwen3_32b": "Qwen3-32B", "llama_3_1_70b": "Llama-3.1-70B"}
NOM_RESULTAT = "externe-narcbench-v2"
OBJET = "lecture du bras externe NARCBench v2 (activations publiées, processeur, 0 USD)"
PAQUETS = ("scikit-learn", "joblib", "threadpoolctl", "narwhals", "cloudpickle", "numpy", "scipy", "torch")
_LIGNE_CONF = re.compile(r"(" + "|".join(re.escape(k) for k in CLES_CONFIGURATION) + r") : (\S(?:.*\S)?)")


# ---------- chemins, registre (n° 3 et 4) ----------

def _chemin_relatif(chemin: str, quoi: str) -> str:
    p = Path(chemin)
    if not chemin or p.is_absolute() or ".." in p.parts:
        raise RefusRegistre(f"{quoi} {chemin!r} : chemin relatif à la racine du dépôt, sans « .. », attendu")
    return p.as_posix()


def _cellules(ligne: str) -> list:
    return [c.strip() for c in ligne.strip().strip("|").split("|")]


def est_cle_du_bras(cle: str) -> bool:
    s = cle.split("-")
    return any(s[i:i + 2] == ["NARC", "EXT"] for i in range(len(s) - 1))


def lire_registre_externe(registre: Path) -> dict:
    """Règle d'ouverture du texte (« Lignes de registre », n° 3 et 4), refus relevés ensemble : `SCELLEMENT` et `CODE` exactement
    une fois et bien formées ; `LECTURE` présente → refus, déjà jouée ; **toute autre clé** (ligne à quatre cellules dont la
    deuxième est une date) → refus ; toute autre ligne (titre, en-tête de table, texte, ligne vide) : ignorée."""
    registre = Path(registre)
    if not registre.is_file():
        raise RefusRegistre(f"registre {REGISTRE} absent du dépôt (liste d'arrêt n° 3)")
    trouvees = {CLE_SCELLEMENT: [], CLE_CODE: []}
    fautes = []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        c = _cellules(ligne)
        if not c or not c[0]:
            continue
        if c[0] in trouvees:
            trouvees[c[0]].append(c)
            continue
        if c[0] == CLE_LECTURE:
            fautes.append(f"registre : ligne {CLE_LECTURE} présente : lecture déjà jouée ; pas de relance sous ce texte (nœud, "
                          "liste d'arrêt n° 4)")
            continue
        if not (len(c) == 4 and DATE.fullmatch(c[1])):
            continue
        if not CLE.fullmatch(c[0]):
            fautes.append(f"registre : ligne {c[0]!r} : la première cellule n'a pas la forme d'une clé (liste d'arrêt n° 3)")
        elif est_cle_du_bras(c[0]):
            fautes.append(f"registre : clé {c[0]} aux segments NARC-EXT inconnue (seules {', '.join(CLES_BRAS)}) (liste d'arrêt n° 3)")
        else:
            fautes.append(f"registre : clé {c[0]} : le registre propre ne porte que {', '.join(CLES_BRAS)} (liste d'arrêt n° 3)")
    lignes = {}
    for k, ls in trouvees.items():
        if len(ls) != 1:
            fautes.append(f"registre : {len(ls)} ligne(s) {k}, exactement une attendue")
            continue
        c = ls[0]
        if len(c) != 4:
            fautes.append(f"registre : ligne {k} mal formée ({len(c)} cellules, 4 attendues)")
            continue
        _, date, chemin, sha = c
        if not DATE.fullmatch(date):
            fautes.append(f"registre : ligne {k} : date {date!r} (AAAA-MM-JJTHH:MM:SSZ, UTC, attendue)")
            continue
        if not SHA.fullmatch(sha):
            fautes.append(f"registre : ligne {k} : empreinte {sha!r} (64 caractères hexadécimaux attendus)")
            continue
        if not chemin or chemin.startswith("/") or ".." in Path(chemin).parts:
            fautes.append(f"registre : ligne {k} : chemin {chemin!r} (relatif à la racine, sans « .. », attendu)")
            continue
        try:
            t = int(datetime.strptime(date, FORMAT_DATE).replace(tzinfo=timezone.utc).timestamp())
        except ValueError:
            fautes.append(f"registre : ligne {k} : date {date!r} impossible")
            continue
        lignes[k] = (t, date, chemin, sha)
    if fautes:
        raise RefusRegistre(" ; ".join(fautes))
    return {"lignes": lignes}


def garde_registre(depot: Path, texte: str, instant: int) -> dict:
    """Liste d'arrêt n° 3 : lignes lues, antériorité stricte, ordre `CODE` après `SCELLEMENT`, texte cité = texte donné, sceaux,
    conformité du texte au gabarit (avant toute lecture de données). Refus : `RefusRegistre`."""
    depot = Path(depot)
    texte = _chemin_relatif(texte, "texte")
    registre = depot / REGISTRE
    lu = lire_registre_externe(registre)
    (ts, ds, cs, ss), (tc, dc, cc, sc) = lu["lignes"][CLE_SCELLEMENT], lu["lignes"][CLE_CODE]
    fautes = []
    for k, t, d in ((CLE_SCELLEMENT, ts, ds), (CLE_CODE, tc, dc)):
        if not t < int(instant):
            fautes.append(f"registre : ligne {k} datée {d}, pas strictement antérieure à l'ouverture ({date_utc(instant)})")
    if not tc > ts:
        fautes.append(f"registre : ligne {CLE_CODE} ({dc}) pas strictement postérieure à {CLE_SCELLEMENT} ({ds})")
    if Path(cs) != Path(texte):
        fautes.append(f"registre : ligne {CLE_SCELLEMENT} cite {cs}, pas le texte donné {texte}")
    for k, chemin, sha in ((CLE_SCELLEMENT, cs, ss), (CLE_CODE, cc, sc)):
        try:
            sceau_conforme(depot / chemin, sha)
        except RefusRegistre as e:
            fautes.append(f"registre : ligne {k} : {e}")
    if fautes:
        raise RefusRegistre(" ; ".join(fautes))
    try:
        prereg.exiger_prereg_scelle(depot / cs)
    except RefusRegistre:
        raise
    except GardeArret as e:
        raise RefusRegistre(f"texte {cs} : {e}") from None
    return {"registre": REGISTRE, "registre_sha256": sha256_de(registre), "ouverture": date_utc(instant),
            "texte": {"cle": CLE_SCELLEMENT, "date": ds, "chemin": cs, "sha256": ss},
            "code": {"cle": CLE_CODE, "date": dc, "chemin": cc, "sha256": sc}}


# ---------- configuration canonique du texte scellé (n° 5) ----------

def couches_familles(spec: str) -> dict:
    """« bande » (toutes les couches de la bande de chaque modèle) ou « qwen3_32b=28;llama_3_1_70b=34+35 » (couches
    croissantes, sans doublon, dans la bande)."""
    if spec == "bande":
        return {m: tuple(C.BANDES[m]) for m in C.MODELES}
    sortie = {}
    for morceau in spec.split(";"):
        modele, _, couches = morceau.partition("=")
        if modele not in C.MODELES or modele in sortie or not couches:
            raise RefusRegistre(f"couches de nos familles : {morceau!r} (modèle connu, une fois, couches données)")
        try:
            cs = tuple(int(x) for x in couches.split("+"))
        except ValueError:
            raise RefusRegistre(f"couches de nos familles : {couches!r} (entiers séparés par « + »)") from None
        if list(cs) != sorted(set(cs)) or any(c not in C.BANDES[modele] for c in cs):
            raise RefusRegistre(f"couches {cs} de {modele} : croissantes, sans doublon, dans la bande {C.BANDES[modele]}")
        sortie[modele] = cs
    if set(sortie) != set(C.MODELES):
        raise RefusRegistre(f"couches de nos familles : les deux modèles attendus, reçu {sorted(sortie)}")
    return {m: sortie[m] for m in C.MODELES}


def lire_configuration_texte(chemin: Path) -> dict:
    """Section `## Configuration canonique de la commande` du texte : six lignes seules `clé : valeur` (lignes vides et clôtures
    ```` ``` ```` tolérées), chacune la seule ligne du texte entier qui commence par `<clé> :`. Refus : `RefusRegistre`."""
    texte = Path(chemin).read_text(encoding="utf-8")
    lignes = texte.splitlines()
    n = sum(1 for l in lignes if re.fullmatch(r"## +" + re.escape(SECTION_CONFIGURATION) + r"\s*", l))
    if n != 1:
        raise RefusRegistre(f"texte : {n} section(s) « ## {SECTION_CONFIGURATION} », exactement une attendue (liste d'arrêt n° 5)")
    fautes, valeurs = [], {}
    for ligne in prereg.sections(texte)[SECTION_CONFIGURATION].splitlines():
        if not ligne.strip() or ligne.strip() == "```":
            continue
        m = _LIGNE_CONF.fullmatch(ligne)
        if not m:
            fautes.append(f"ligne {ligne!r} : « <clé> : <valeur> » seule attendue, clé parmi {', '.join(CLES_CONFIGURATION)}")
        elif m.group(1) in valeurs:
            fautes.append(f"clé {m.group(1)!r} en double")
        else:
            valeurs[m.group(1)] = m.group(2)
    manque = [k for k in CLES_CONFIGURATION if k not in valeurs]
    if manque:
        fautes.append(f"clé(s) absente(s) : {', '.join(manque)}")
    for k in CLES_CONFIGURATION:
        debuts = sum(1 for l in lignes if l.startswith(f"{k} :"))
        if debuts > 1:
            fautes.append(f"{debuts} lignes du texte commencent par « {k} : », une seule attendue")
    if fautes:
        raise RefusRegistre(f"section « {SECTION_CONFIGURATION} » : " + " ; ".join(fautes) + " (liste d'arrêt n° 5)")
    if valeurs["augmentation"] not in X2.AUGMENTATIONS:
        fautes.append(f"augmentation {valeurs['augmentation']!r} (papier ou code)")
    if valeurs["run-id"] != FORME_RUN:
        fautes.append(f"run-id {valeurs['run-id']!r} : la forme {FORME_RUN!r} attendue")
    if valeurs["registre"] != REGISTRE:
        fautes.append(f"registre {valeurs['registre']!r} ≠ registre fixé {REGISTRE}")
    if not re.fullmatch(r"[0-9]+", valeurs["Entropie"]) or int(valeurs["Entropie"]) < ENTROPIE_MINIMALE:
        fautes.append(f"Entropie {valeurs['Entropie']!r} : entier (chiffres seuls) ≥ 2³² = {ENTROPIE_MINIMALE} attendu (ni une année, "
                      "ni une date, ni une petite graine)")
    try:
        texte_cite = _chemin_relatif(valeurs["texte"], "texte")
        couches = couches_familles(valeurs["couches-familles"])
    except RefusRegistre as e:
        fautes.append(str(e))
    if fautes:
        raise RefusRegistre("configuration du texte : " + " ; ".join(fautes) + " (liste d'arrêt n° 5)")
    return {"augmentation": valeurs["augmentation"], "couches_familles": couches, "couches_familles_texte": valeurs["couches-familles"],
            "forme_run_id": valeurs["run-id"], "registre": valeurs["registre"], "texte": texte_cite,
            "entropie": int(valeurs["Entropie"])}


def comparer_configuration(conf: dict, args, texte_scelle: str) -> dict:
    """Les options de la commande doivent dire ce que dit le texte scellé ; tout écart → refus (n° 5, code 2)."""
    fautes = []
    if args.augmentation != conf["augmentation"]:
        fautes.append(f"augmentation {args.augmentation!r} ≠ {conf['augmentation']!r} du texte")
    couches = couches_familles(args.couches_familles)
    if couches != conf["couches_familles"]:
        fautes.append(f"couches de nos familles {args.couches_familles!r} ≠ {conf['couches_familles_texte']!r} du texte")
    if not MOTIF_RUN.fullmatch(args.run_id):
        fautes.append(f"identifiant du run {args.run_id!r} hors de la forme {conf['forme_run_id']!r} du texte")
    else:
        try:
            datetime.strptime(args.run_id[:15], "%Y%m%d-%H%M%S")
        except ValueError:
            fautes.append(f"identifiant du run {args.run_id!r} : date ou heure impossible")
    if isinstance(args.entropie, bool) or int(args.entropie) != conf["entropie"]:
        fautes.append("entropie de la commande ≠ ligne « Entropie : <entier> » du texte (comparées en entiers)")
    if not (Path(conf["texte"]) == Path(args.texte) == Path(texte_scelle)):
        fautes.append(f"texte : ligne « texte : {conf['texte']} », option {args.texte!r} et ligne {CLE_SCELLEMENT} ({texte_scelle}) "
                      "doivent être égales")
    if fautes:
        raise RefusRegistre("commande ≠ configuration canonique du texte scellé : " + " ; ".join(fautes) + " (liste d'arrêt n° 5)")
    return couches


def exiger_jamais_jouee(depot: Path) -> None:
    """n° 4 : un dossier `runs/*-narc-externe-v2` ou un résultat `diag/*/externe-narcbench-v2.json` → refus, nœud (la ligne
    `LECTURE-NARC-EXT` est refusée à la lecture du registre)."""
    depot = Path(depot)
    deja = sorted(str(p.relative_to(depot)) for p in (depot / "runs").glob(f"*-{SUFFIXE_RUN}"))
    deja += sorted(str(p.relative_to(depot)) for p in (depot / "diag").glob(f"*/{NOM_RESULTAT}.json"))
    if deja:
        raise RefusRegistre(f"lecture du bras externe déjà jouée ou ouverte ({', '.join(deja[:3])}) : pas de relance sous ce texte "
                            "(nœud, liste d'arrêt n° 4)")


# ---------- code (n° 6) et scikit-learn (n° 7) ----------

def _git(depot, *args) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(depot), *args], capture_output=True)


def blob_git(donnees: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(donnees) + donnees).hexdigest()


def arbre_au_commit(depot: Path, commit: str, prefixe: str = PREFIXE_PAQUET) -> dict:
    """{chemin : identifiant de blob} des fichiers sous `prefixe` au commit."""
    r = _git(depot, "ls-tree", "-r", "-z", commit, "--", prefixe.rstrip("/"))
    if r.returncode != 0:
        raise GardeArret(f"git ls-tree {commit[:12]}… a échoué : {r.stderr.decode(errors='replace').strip()}")
    sortie = {}
    for entree in r.stdout.split(b"\0"):
        if not entree:
            continue
        tete, chemin = entree.split(b"\t", 1)
        _, sorte, oid = tete.split(b" ")
        if sorte == b"blob":
            sortie[chemin.decode("utf-8")] = oid.decode()
    return sortie


def paquet_execute() -> dict:
    """{`src/controle_ia/…` : fichier} du paquet `controle_ia` effectivement importé (sans `__pycache__` ni `.pyc`)."""
    racine = Path(controle_ia.__file__).resolve().parent
    return {PREFIXE_PAQUET + p.relative_to(racine).as_posix(): p for p in sorted(racine.rglob("*"))
            if p.is_file() and "__pycache__" not in p.parts and p.suffix not in (".pyc", ".pyo")}


def _sha256_au_commit(depot: Path, commit: str, chemin: str) -> str:
    r = _git(depot, "cat-file", "blob", f"{commit}:{chemin}")
    if r.returncode != 0:
        raise GardeArret(f"{chemin} absent du commit {commit[:12]}…")
    return hashlib.sha256(r.stdout).hexdigest()


def lire_fiche_code(chemin: Path) -> dict:
    """Fiche du code (JSON scellé, cité par `CODE-NARC-EXT`) : `commit`, `fichiers`, `scikit-learn` lus par programme ; les autres
    clés (branche, lignes des auteurs, essais, contre-lecteur) sont informatives."""
    try:
        f = json.loads(Path(chemin).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise GardeArret(f"fiche du code {chemin} illisible : {e}") from None
    if not isinstance(f, dict):
        raise GardeArret("fiche du code : objet JSON attendu")
    commit, fichiers, skl = f.get("commit"), f.get("fichiers"), f.get("scikit-learn")
    if not isinstance(commit, str) or not COMMIT.fullmatch(commit):
        raise GardeArret(f"fiche du code : commit {commit!r} (40 caractères hexadécimaux attendus)")
    if not isinstance(fichiers, dict) or not fichiers:
        raise GardeArret("fiche du code : `fichiers` (chemin → sha256) non vide attendu")
    for p, s in fichiers.items():
        if (not isinstance(p, str) or not p.startswith(PREFIXE_FICHE) or not p.endswith(".py") or ".." in Path(p).parts
                or not isinstance(s, str) or not SHA.fullmatch(s)):
            raise GardeArret(f"fiche du code : entrée {p!r} → {s!r} ({PREFIXE_FICHE}<nom>.py → sha256 attendu)")
    if not isinstance(skl, str) or not skl.strip():
        raise GardeArret("fiche du code : version de `scikit-learn` attendue")
    return {"commit": commit, "fichiers": dict(sorted(fichiers.items())), "scikit-learn": skl,
            "cles_informatives": sorted(set(f) - {"commit", "fichiers", "scikit-learn"})}


def exiger_code_de_la_fiche(depot: Path, fiche: dict) -> dict:
    """Liste d'arrêt n° 6 : commit exécuté = commit de la fiche (au sens de DF-02 de T0.7), arbre de travail propre."""
    depot = Path(depot)
    top = _git(depot, "rev-parse", "--show-toplevel")
    if top.returncode != 0 or Path(top.stdout.decode().strip()).resolve() != depot.resolve():
        raise GardeArret(f"{depot} n'est pas la racine d'un dépôt git")
    etat = etat_git(depot)
    if not etat["propre"]:
        raise GardeArret("arbre de travail modifié : arrêt (liste d'arrêt n° 6)\n" + etat["statut"])
    commit = fiche["commit"]
    if _git(depot, "cat-file", "-e", f"{commit}^{{commit}}").returncode != 0:
        raise GardeArret(f"commit de la fiche {commit[:12]}… absent du dépôt (liste d'arrêt n° 6)")
    if _git(depot, "merge-base", "--is-ancestor", commit, "HEAD").returncode != 0:
        raise GardeArret(f"commit de la fiche {commit[:12]}… : ni HEAD ni un de ses ancêtres (liste d'arrêt n° 6)")
    arbre = arbre_au_commit(depot, commit)
    ecarts = []
    au_commit = {p for p in arbre if p.startswith(PREFIXE_FICHE) and p.endswith(".py")}
    if au_commit != set(fiche["fichiers"]):
        ecarts.append(f"fichiers de {PREFIXE_FICHE} au commit ≠ liste de la fiche (en plus au commit : "
                      f"{sorted(au_commit - set(fiche['fichiers']))[:3]} ; en plus dans la fiche : "
                      f"{sorted(set(fiche['fichiers']) - au_commit)[:3]})")
    for p, s in fiche["fichiers"].items():
        if p in au_commit and _sha256_au_commit(depot, commit, p) != s:
            ecarts.append(f"{p} : empreinte au commit ≠ empreinte de la fiche")
    execute = paquet_execute()
    if set(execute) != set(arbre):
        ecarts.append(f"paquet exécuté ≠ {PREFIXE_PAQUET} du commit (en plus : {sorted(set(execute) - set(arbre))[:3]} ; "
                      f"en moins : {sorted(set(arbre) - set(execute))[:3]})")
    differents = [rel for rel, p in execute.items() if rel in arbre and blob_git(p.read_bytes()) != arbre[rel]]
    if differents:
        ecarts.append(f"{len(differents)} fichier(s) du paquet exécuté différent(s) du commit : {differents[:3]}")
    if ecarts:
        raise GardeArret(f"code exécuté ≠ code de la fiche ({commit[:12]}…) : arrêt (liste d'arrêt n° 6) : " + " ; ".join(ecarts))
    return {"commit_fiche": commit, "head": etat["commit"], "fichiers_fiche": len(fiche["fichiers"]),
            "fichiers_paquet": len(execute), "regle": "paquet exécuté égal à src/controle_ia/ du commit (DF-02 de T0.7)"}


def version_installee(paquet: str) -> str | None:
    try:
        return metadata.version(paquet)
    except metadata.PackageNotFoundError:
        return None


def fiche_code(depot: Path, commit: str) -> dict:
    """Contenu lu par programme d'une fiche de code pour `commit` (la mère y ajoute les clés informatives) : fichiers
    `src/controle_ia/narcbench/*.py` du commit et leurs sha256, version de scikit-learn épinglée dans `requirements-cpu.txt`."""
    if not COMMIT.fullmatch(commit):
        raise GardeArret(f"commit {commit!r} (40 caractères hexadécimaux attendus)")
    arbre = arbre_au_commit(depot, commit)
    fichiers = {p: _sha256_au_commit(depot, commit, p) for p in sorted(arbre)
                if p.startswith(PREFIXE_FICHE) and p.endswith(".py")}
    r = _git(depot, "cat-file", "blob", f"{commit}:requirements-cpu.txt")
    pins = {}
    if r.returncode == 0:
        for l in r.stdout.decode("utf-8").splitlines():
            l = l.split("#", 1)[0].strip()
            if "==" in l:
                nom, version = l.split("==", 1)
                pins[nom.strip()] = version.strip()
    if "scikit-learn" not in pins:
        raise GardeArret(f"scikit-learn non épinglé dans requirements-cpu.txt au commit {commit[:12]}…")
    return {"commit": commit, "fichiers": fichiers, "scikit-learn": pins["scikit-learn"]}


# ---------- données (n° 2) ----------

def exiger_sans_transfert(racine: Path) -> None:
    """Liste d'arrêt n° 2 : un fichier ou dossier de l'étage de transfert sous la racine des données → arrêt, nœud."""
    racine = Path(racine)
    trouves = sorted(p.relative_to(racine).as_posix() for p in racine.rglob("*")
                     if "transfer" in (q.lower() for q in p.relative_to(racine).parts))
    if trouves:
        raise GardeArret(f"étage de transfert présent sous {racine} ({', '.join(trouves[:3])}) : arrêt, nœud (liste d'arrêt n° 2)")


def exiger_scikit_learn(fiche: dict) -> str:
    """n° 7 : `scikit-learn` absent ou d'une autre version que 1.9.1 (ou que celle de la fiche) → arrêt avant toute lecture."""
    v = version_installee("scikit-learn")
    if v is None or v != VERSION_SKLEARN or fiche["scikit-learn"] != VERSION_SKLEARN:
        raise GardeArret(f"scikit-learn installé {v!r}, fiche {fiche['scikit-learn']!r}, exigé {VERSION_SKLEARN} : rien n'est lu, pas "
                         "même notre chaîne (liste d'arrêt n° 7)")
    return v


# ---------- résultat ----------

def taches(couches: dict, domaines: dict) -> list:
    """Tâches `SeedSequence` de la lecture (section « Graines » du texte ; écart 18), par modèle."""
    return [t for m in C.MODELES for t in CE.taches_modele(m, couches[m], C.BANDES[m], domaines[m])]


def valeurs_non_finies(x, chemin: str = "resultat") -> list:
    """Chemins des flottants non finis (le résultat scellé doit être du JSON standard)."""
    if isinstance(x, float):
        return [] if math.isfinite(x) else [chemin]
    if isinstance(x, dict):
        return [p for k, v in x.items() for p in valeurs_non_finies(v, f"{chemin}/{k}")]
    if isinstance(x, (list, tuple)):
        return [p for i, v in enumerate(x) for p in valeurs_non_finies(v, f"{chemin}[{i}]")]
    return []


def _versions() -> dict:
    return {p: version_installee(p) for p in PAQUETS}


def journaliser(depot: Path, cle: str, instant: int, quoi: str, detail: str) -> Path | None:
    """Une ligne `| CLÉ | date | quoi | détail | registre <sha256> |` au journal ; rien si `registres/` manque."""
    journal = Path(depot) / JOURNAL
    if not journal.parent.is_dir():
        return None
    registre = Path(depot) / REGISTRE
    sha = sha256_de(registre) if registre.is_file() else "absent"
    propre = " ".join(str(detail).replace("|", "¦").split())
    with open(journal, "a", encoding="utf-8") as f:
        f.write(f"| {cle} | {date_utc(instant)} | {quoi} | {propre} | registre {sha} |\n")
    return journal


def comptes_structurels(metas: dict, exclusions: dict, roles: dict, plis: dict) -> dict:
    """Écart A19 (plan d'analyse n° 3) : épisodes par étage, modèle et condition ; exclusions ; domaines et plis gardés ;
    sabots ; lignes d'apprentissage par classe ; identifiants d'épisodes communs aux deux modèles (« le 70B lit-il ses propres
    textes ? », rapporté sans effet sur la lecture). Les nombres de l'article sont à côté (p. 14, 15, 35, 40, 44)."""
    sortie = {"article": {"core": "50 scénarios, 17 domaines, 100 épisodes (p. 14) ; 36 scénarios de collusion retenus avec les 50 "
                                  "témoins (p. 35, sans dire pour quel modèle)",
                          "stego": "20 sabots, 40 épisodes (p. 15 et 40) ; tous les épisodes de collusion retenus (p. 44)"},
              "modeles": {}, "communs_aux_deux_modeles": {}}
    for m in C.MODELES:
        par = {}
        for etage in C.ETAGES:
            meta = metas[(m, etage)]
            mode = {}
            for x in meta:
                mode.setdefault(x["run_id"], x["mode"])
            par[etage] = {"episodes": len(mode), "par_condition": dict(sorted(Counter(mode.values()).items())),
                          "exclusions": {k: exclusions[f"{m}/{etage}"][k] for k in ("exclus", "gardes", "par_motif")},
                          "roles": roles[f"{m}/{etage}"]}
        par["stego"]["sabots"] = len({CE.sabot(r) for r in {x["run_id"] for x in metas[(m, "stego")]}})
        par["core"]["domaines"] = len({C.domaine(r) for r in {x["run_id"] for x in metas[(m, "core")]} if C.domaine(r)})
        par["core"]["plis_gardes"] = plis[m]
        col, hon = X2.lignes_apprentissage(metas[(m, "core")])
        par["core"]["lignes_apprentissage"] = {"colludeurs": len(col), "honnetes": len(hon)}
        sortie["modeles"][m] = par
    for etage in C.ETAGES:
        a, b = ({x["run_id"] for x in metas[(m, etage)]} for m in C.MODELES)
        sortie["communs_aux_deux_modeles"][etage] = {"communs": len(a & b), "seulement_" + C.MODELES[0]: len(a - b),
                                                     "seulement_" + C.MODELES[1]: len(b - a)}
    return sortie


# ---------- lecture ----------

def lire(args, instant: int, attendues: dict | None = None, etat: dict | None = None) -> dict:
    etat = {} if etat is None else etat
    depot = Path(args.depot).resolve()
    garde = garde_registre(depot, args.texte, instant)                                                    # n° 3
    conf = lire_configuration_texte(depot / garde["texte"]["chemin"])                                      # n° 5
    couches = comparer_configuration(conf, args, garde["texte"]["chemin"])
    fiche = lire_fiche_code(depot / garde["code"]["chemin"])                                               # n° 6
    code = exiger_code_de_la_fiche(depot, fiche)
    exiger_jamais_jouee(depot)                                                                            # n° 4
    skl = exiger_scikit_learn(fiche)                                                                      # n° 7
    exiger_sans_transfert(args.donnees)                                                                  # n° 2
    verif = C.verifier_fichiers(args.donnees, C.EMPREINTES_PUBLIEES if attendues is None else attendues)  # n° 1
    metas, exclusions, roles, plis = {}, {}, {}, {}
    for modele in C.MODELES:                                                                              # n° 8 et 9
        for etage in C.ETAGES:
            meta = C.charger_metadonnees(Path(args.donnees) / "activations" / modele / etage / "metadata_gen.json")
            roles[f"{modele}/{etage}"] = X2.exiger_roles_episodes(meta, X2.PHASES[etage.upper()])
            exclusions[f"{modele}/{etage}"] = X2.exiger_exclusions(meta, etage.upper())
            metas[(modele, etage)] = meta
        plis[modele] = X2.plis_gardes(metas[(modele, "core")])
    domaines = {m: [p["domaine"] for p in plis[m]] for m in C.MODELES}
    comptes = comptes_structurels(metas, exclusions, roles, plis)
    config = {"objet": OBJET, "texte": garde["texte"], "code": garde["code"], "registre": garde,
              "configuration_du_texte": {k: (v if k != "couches_familles" else {m: list(c) for m, c in v.items()})
                                         for k, v in conf.items()},
              "fiche_code": fiche, "controle_du_code": code, "scikit_learn": skl,
              "revision_jeu": C.REVISION_JEU, "donnees": {"racine": str(args.donnees), "fichiers": verif},
              "augmentation": conf["augmentation"], "graines_auteurs": list(X2.GRAINES_AUTEURS),
              "bandes": {m: list(C.BANDES[m]) for m in C.MODELES}, "couches_familles": {m: list(c) for m, c in couches.items()},
              "plis_gardes": domaines, "familles": list(X2.FAMILLES_EXTERNES),
              "n_plancher": CE.N_PLANCHER, "n_tirages": CE.N_TIRAGES, "n_permutations": CE.N_PLACEBO,
              "tolerance": X2.TOLERANCE, "arrondi": X2.ARRONDI_TOLERANCE,
              "recette": {"lr": X2.PARAMETRES_LR, "mode_core": "par-pli", "source": "probes/reproduce_LR.py @ 85fea3be2a9d"},
              "versions_supplementaires": _versions()}
    chemin_m, manifeste = creer_manifeste(depot, args.run_id, config, taches(couches, domaines), entropie=conf["entropie"],
                                          decisif=False, prereg=depot / garde["texte"]["chemin"], commande=" ".join(sys.argv))
    etat["ouvert"] = True
    journaliser(depot, "OUVERTURE-NARC-EXT", instant, args.run_id, f"manifeste {sha256_de(chemin_m)}")

    def graine(tache: str) -> int:
        return int(generateur(manifeste["graines"][tache]).integers(2 ** 31))

    resultat = {"modeles": {}, "garde_registre": garde, "controle_du_code": code, "comptes_structurels": comptes,
                "marque": X2.MARQUE_DIAGNOSTIC}
    par_modele = {}
    for modele in C.MODELES:
        d = {}
        for etage in C.ETAGES:
            meta = metas[(modele, etage)]
            base = Path(args.donnees) / "activations" / modele / etage
            d[etage.upper()] = (meta, C.charger_couches(base / "activations_gen.npz", C.BANDES[modele], len(meta),
                                                        C.LARGEURS[modele]))
        repro = X2.reproduire_helios_v2(d["CORE"], d["STEGO"], C.BANDES[modele], conf["augmentation"], garder_scores=True)
        lu = CE.lire_modele(modele, d["CORE"], d["STEGO"], couches[modele], graine, repro, n_tirages=CE.N_TIRAGES,
                            n_plancher=CE.N_PLANCHER, n_placebo=CE.N_PLACEBO)
        repro.pop("scores")
        par_modele[modele] = lu
        resultat["modeles"][modele] = {"cellules": lu["cellules"], "comptes": lu["comptes"],
                                       "lecture_par_agent": lu["lecture_par_agent"], "reproduction": repro,
                                       "garde_reproduction": X2.garde_reproduction_v2(NOMS_PUBLIES[modele], repro)}
    resultat["lecture"] = CE.lecture_finale(par_modele)
    non_finies = valeurs_non_finies(resultat)
    if non_finies:
        raise GardeArret(f"résultat : {len(non_finies)} valeur(s) non finie(s) ({', '.join(non_finies[:3])}) : JSON standard "
                         "exigé, rien n'est écrit")
    chemin_r = ecrire_resultat(depot, chemin_m, NOM_RESULTAT, resultat)
    return {"manifeste": str(chemin_m), "resultat": str(chemin_r)}


def analyseur() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="python -m controle_ia.narcbench.lecture_externe_v2", description=__doc__.splitlines()[0])
    p.add_argument("--depot", required=True)
    p.add_argument("--texte", required=True)
    p.add_argument("--donnees", required=True)
    p.add_argument("--run-id", required=True)
    p.add_argument("--entropie", required=True, type=int)
    p.add_argument("--augmentation", required=True, choices=sorted(X2.AUGMENTATIONS))
    p.add_argument("--couches-familles", required=True)
    return p


def _controle_prealable(argv: list) -> int:
    if argv[0] == "verifier-texte":
        if len(argv) != 2:
            print("usage : verifier-texte <chemin du texte>", file=sys.stderr)
            return 2
        try:
            conf = lire_configuration_texte(Path(argv[1]))
        except RefusRegistre as e:
            print(f"texte refusé : {e}", file=sys.stderr)
            return 2
        print(json.dumps({k: (v if k != "couches_familles" else {m: list(c) for m, c in v.items()}) for k, v in conf.items()},
                         ensure_ascii=False, indent=1))
        return 0
    p = argparse.ArgumentParser(prog="… fiche-code")
    p.add_argument("--depot", required=True)
    p.add_argument("--commit", required=True)
    a = p.parse_args(argv[1:])
    try:
        print(json.dumps(fiche_code(Path(a.depot), a.commit), ensure_ascii=False, indent=1, sort_keys=True))
    except GardeArret as e:
        print(f"arrêt : {e}", file=sys.stderr)
        return 1
    return 0


def main(argv=None, attendues: dict | None = None) -> int:
    """`attendues` : None en usage réel (empreintes publiées) ; un autre jeu ne sert qu'aux essais sur fichiers factices.
    Codes : 0 lu ; 2 refus (n° 3, 4, 5), journalisé ; 1 tout autre arrêt (n° 1, 2, 6, 7 avant l'ouverture ; n° 8 à 12 et mémoire
    après), journalisé, motif imprimé sans trace d'erreur."""
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] in ("verifier-texte", "fiche-code"):
        return _controle_prealable(argv)
    args = analyseur().parse_args(argv)
    instant = int(datetime.now(timezone.utc).timestamp())
    depot = Path(args.depot).resolve()
    etat = {"ouvert": False}
    try:
        sortie = lire(args, instant, attendues, etat)
    except RefusRegistre as e:
        j = journaliser(depot, "REFUS-NARC-EXT", instant, args.run_id, f"refus : {e}")
        print(f"refus avant l'ouverture (rien d'écrit ; {'journalisé' if j else 'journal absent'}) : {e}", file=sys.stderr)
        return 2
    except (GardeArret, MemoryError) as e:
        motif = f"mémoire insuffisante : arrêt, nœud (liste d'arrêt n° 11) {e}" if isinstance(e, MemoryError) else str(e)
        cle = "ARRET-NARC-EXT" if etat["ouvert"] else "REFUS-NARC-EXT"
        j = journaliser(depot, cle, instant, args.run_id, f"arrêt : {motif}")
        print(f"arrêt {'après ouverture' if etat['ouvert'] else 'avant ouverture, rien écrit'} "
              f"({'journalisé' if j else 'journal absent'}) : {motif}", file=sys.stderr)
        return 1
    print(sortie)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["REGISTRE", "JOURNAL", "CLE_SCELLEMENT", "CLE_CODE", "CLE_LECTURE", "SECTION_CONFIGURATION", "CLES_CONFIGURATION",
           "FORME_RUN", "VERSION_SKLEARN", "lire_registre_externe", "garde_registre", "couches_familles",
           "lire_configuration_texte", "comparer_configuration", "exiger_jamais_jouee", "lire_fiche_code",
           "exiger_code_de_la_fiche", "exiger_scikit_learn", "fiche_code", "paquet_execute", "exiger_sans_transfert",
           "valeurs_non_finies", "journaliser", "comptes_structurels", "taches", "lire", "main", "analyseur"]

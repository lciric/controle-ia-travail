"""Commande de la lecture du bras externe NARCBench, v2 — **ne se lance qu'après le scellement du texte court et l'inscription de
la ligne de code** (R1) ; processeur, 0 USD (R-2175, D-3 (a)). Écrite par le développeur v2, corrigée après la contre-lecture
du code (`contre-lecture-code-externe-v2-v1.md`, `9b90884a…` : M2, M3, m3, m4, m8, m9) et la contre-lecture 1 du texte court
(`prereg/contre-lectures/narcbench-bras-externe-v1-brouillon1-cl1.md`, `9217284f…` : B4, M3 n° 5, M5) ; **jamais jouée sur les
données réelles**.

**Registre propre, fixé** : `registres/narcbench-externe-v1.md` **du dépôt** (aucun autre chemin ; `--registre` n'existe plus),
lignes `| CLÉ | AAAA-MM-JJTHH:MM:SSZ | chemin relatif | sha256 |` (format de `t07/registre_v1`). Trois clés : `SCELLEMENT-NARC-EXT`
(le texte court scellé), `CODE-NARC-EXT` (la fiche du code, JSON scellé), `LECTURE-NARC-EXT` (écrite par la mère après la
lecture). Valeurs du coordinateur ; le brouillon 1 du texte écrit `NARCEXT` : le texte scellé doit porter ces trois-ci.

Ordre ; chaque étape arrête tout au premier écart (R5, aucun repli silencieux) :
1. **liste d'arrêt n° 3, registre** (`RefusRegistre`, code 2, journalisé, rien d'autre d'écrit, relance possible après commit du
   journal) : `SCELLEMENT-NARC-EXT` et `CODE-NARC-EXT` exactement une fois, bien formées, strictement antérieures à l'ouverture,
   `CODE` strictement postérieure à `SCELLEMENT`, sceaux conformes (fichier et compagnon `.sha256`) ; `SCELLEMENT` cite le texte
   donné ; texte conforme au gabarit des préenregistrements (`prereg.exiger_prereg_scelle`) ; `LECTURE-NARC-EXT` présente → refus,
   **pas de relance sous ce texte (nœud)** ; une autre clé aux segments `NARC-EXT` → refus ; toute autre clé bien formée :
   ignorée et comptée ;
2. **configuration canonique du texte scellé** (code 2) : section `## Configuration canonique de la commande`, une seule, faite
   **seulement** de lignes `clé : valeur` (tiret de liste et guillemets inverses permis), clés exactes `augmentation`,
   `couches-familles`, `run-id` (une **forme** : `AAAAMMJJ-HHMMSS-<nom>`), `registre` (égal au registre fixé), plus, n'importe où
   dans le texte, **une seule ligne exacte** `Entropie : <entier>` (jamais une sous-chaîne ; entier ≥ 2³², ni une année ni une
   date) ; l'augmentation, les couches de nos familles, l'entropie passées à la commande doivent lui être égales, et
   l'identifiant du run doit avoir la forme du texte (date et heure valides) ;
3. **jamais ouverte** (code 2) : aucun dossier `runs/*-<nom>` ni résultat `diag/*/externe-narcbench-v2.json` (un run ouvert puis
   arrêté n'est pas relancé : nœud) ;
4. **liste d'arrêt n° 4, code** (`GardeArret`, code 1, journalisé) : `--depot` est la racine du dépôt git ; arbre de travail
   propre ; la fiche citée par `CODE-NARC-EXT` (JSON : `commit` à 40 caractères hexadécimaux, `fichiers` = chaque
   `src/controle_ia/narcbench/*.py` au commit avec son sha256, `scikit-learn` = la version ; toute autre clé est informative)
   est cohérente : commit présent, HEAD ou un ancêtre de HEAD, liste égale aux fichiers du commit ; **le paquet `controle_ia`
   exécuté est égal, fichier pour fichier, à `src/controle_ia/` du commit** (règle DF-02 de T0.7 : un changement du paquet
   après la ligne de code arrête) ;
5. **liste d'arrêt n° 7** : `scikit-learn` absent ou d'une autre version que celle de la fiche → le témoin de recette est
   « non lu : garde (scikit-learn) », **sans arrêter** : notre chaîne est lue ;
6. **n° 1, 2, 5, 6, données** (code 1, journalisé) : tailles et empreintes des huit fichiers (`verifier_fichiers`, R11) ; aucun
   fichier de l'étage de transfert sous la racine des données ; formes au chargeur ; exclusions par étage et par modèle,
   **plus de 10 % → arrêt, nœud** (`externe_v2.exiger_exclusions`) ;
7. manifeste du run (`manifeste.creer_manifeste`, `decisif=False` : bras descriptif ; graines par `SeedSequence` de l'entropie
   du texte, une par tâche nommée, R9) ; ouverture journalisée ;
8. reproduction (E1 à E4, E2 = choix du texte, graines 0 à 9 des auteurs) et garde de reproduction v2 (0,03, état par étage),
   nos familles aux couches du texte (gardes n° 8, 9, 10 dans `externe_v2`) ; résultat sans valeur non finie (JSON standard),
   scellé `diag/<run_id>/externe-narcbench-v2.json`, rattaché au manifeste. La ligne `LECTURE-NARC-EXT` est écrite ensuite par
   la mère, hors de ce module.

Journal : `registres/narcbench-externe-v1.md.ouvertures.md` (manière de `t07/registre_v1`), lignes `REFUS-NARC-EXT` (tout arrêt
avant l'ouverture), `OUVERTURE-NARC-EXT`, `ARRET-NARC-EXT` (arrêt après l'ouverture) ; rien n'est écrit si `registres/` manque.
Le journal salit l'arbre : la mère le committe avant toute relance (n° 4 exige un arbre propre).

Contrôles préalables, sans registre ni données (à jouer **avant** de sceller le texte ou d'inscrire la ligne de code) :
    PYTHONPATH=src python -m controle_ia.narcbench.lecture_externe_v2 verifier-texte prereg/<texte>.md
    PYTHONPATH=src python -m controle_ia.narcbench.lecture_externe_v2 fiche-code --depot . --commit <40 caractères>
Lecture (racine du dépôt ; les valeurs viennent du texte scellé) :
    PYTHONPATH=src:/home/user/narcbench-paquets-v2 .venv/bin/python -m controle_ia.narcbench.lecture_externe_v2 --depot . \
        --texte prereg/<texte court scellé>.md --donnees /home/user/narcbench-donnees-v2 \
        --run-id <AAAAMMJJ-HHMMSS>-narc-externe-v2 --entropie <entier du texte> --augmentation <valeur du texte> \
        --couches-familles <valeur du texte>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
import sys
from datetime import datetime, timezone
from importlib import metadata
from pathlib import Path

import controle_ia

from .. import prereg
from ..gardes import GardeArret, etat_git
from ..manifeste import _RUN_ID as FORME_MANIFESTE
from ..manifeste import creer_manifeste, ecrire_resultat, generateur
from ..t07.registre_v1 import CLE, DATE, FORMAT_DATE, SHA, RefusRegistre, date_utc, sceau_conforme, sha256_de
from . import chargeur_externe_v1 as C
from . import externe_v2 as X2

REGISTRE = "registres/narcbench-externe-v1.md"
JOURNAL = REGISTRE + ".ouvertures.md"
CLE_SCELLEMENT, CLE_CODE, CLE_LECTURE = "SCELLEMENT-NARC-EXT", "CODE-NARC-EXT", "LECTURE-NARC-EXT"
CLES_BRAS = (CLE_SCELLEMENT, CLE_CODE, CLE_LECTURE)
SEGMENTS_BRAS = ["NARC", "EXT"]
SECTION_CONFIGURATION = "Configuration canonique de la commande"
CLES_SECTION = ("augmentation", "couches-familles", "run-id", "registre")
ENTROPIE_MINIMALE = 2 ** 32
PREFIXE_PAQUET = "src/controle_ia/"
PREFIXE_FICHE = "src/controle_ia/narcbench/"
COMMIT = re.compile(r"[0-9a-f]{40}")
NOMS_PUBLIES = {"qwen3_32b": "Qwen3-32B", "llama_3_1_70b": "Llama-3.1-70B"}
NOM_RESULTAT = "externe-narcbench-v2"
OBJET = "lecture du bras externe NARCBench v2 (activations publiées, processeur, 0 USD)"
PAQUETS = ("scikit-learn", "joblib", "threadpoolctl", "narwhals", "cloudpickle", "numpy", "scipy", "torch")

_ENTROPIE = re.compile(r"Entropie : ([0-9]+)")
_CLE_VALEUR = re.compile(r"([A-Za-z][A-Za-z-]*)\s*:\s*(.+)")
_FORME_RUN = re.compile(r"AAAAMMJJ-HHMMSS-([a-z0-9][a-z0-9-]*)")


# ---------- chemins, registre (n° 3) ----------

def _chemin_relatif(chemin: str, quoi: str) -> str:
    p = Path(chemin)
    if not chemin or p.is_absolute() or ".." in p.parts:
        raise RefusRegistre(f"{quoi} {chemin!r} : chemin relatif à la racine du dépôt, sans « .. », attendu")
    return p.as_posix()


def _cellules(ligne: str) -> list:
    return [c.strip() for c in ligne.strip().strip("|").split("|")]


def est_cle_du_bras(cle: str) -> bool:
    s = cle.split("-")
    return any(s[i:i + 2] == SEGMENTS_BRAS for i in range(len(s) - 1))


def lire_registre_externe(registre: Path) -> dict:
    """Règle d'ouverture du texte court (« Lignes de registre »), refus relevés ensemble : `SCELLEMENT` et `CODE` exactement une
    fois et bien formées ; `LECTURE` présente → refus ; autre clé aux segments `NARC-EXT` → refus ; ligne à quatre cellules
    datées dont la première n'a pas la forme d'une clé → refus ; toute autre clé bien formée : ignorée et comptée ; toute autre
    ligne (titre, texte, ligne vide) : ignorée."""
    registre = Path(registre)
    if not registre.is_file():
        raise RefusRegistre(f"registre {REGISTRE} absent du dépôt")
    trouvees = {CLE_SCELLEMENT: [], CLE_CODE: []}
    fautes, ignorees = [], []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        c = _cellules(ligne)
        if not c or not c[0]:
            continue
        if c[0] in trouvees:
            trouvees[c[0]].append(c)
            continue
        if c[0] == CLE_LECTURE:
            fautes.append(f"registre : ligne {CLE_LECTURE} présente : lecture déjà jouée ; pas de relance sous ce texte (nœud)")
            continue
        if not (len(c) == 4 and DATE.fullmatch(c[1])):
            continue
        if not CLE.fullmatch(c[0]):
            fautes.append(f"registre : ligne {c[0]!r} : la première cellule n'a pas la forme d'une clé")
            continue
        if est_cle_du_bras(c[0]):
            fautes.append(f"registre : clé {c[0]} aux segments NARC-EXT inconnue (seules {', '.join(CLES_BRAS)})")
            continue
        ignorees.append(c[0])
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
    return {"lignes": lignes, "ignorees": ignorees}


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
            "code": {"cle": CLE_CODE, "date": dc, "chemin": cc, "sha256": sc},
            "cles_ignorees": {"nombre": len(lu["ignorees"]), "noms": lu["ignorees"]}}


# ---------- configuration canonique du texte scellé ----------

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


def _contenu(ligne: str) -> str:
    """Ligne sans tiret ni étoile de liste en tête et sans une paire de guillemets inverses autour."""
    s = ligne.strip()
    if s[:2] in ("- ", "* "):
        s = s[2:].strip()
    if len(s) >= 2 and s[0] == "`" and s[-1] == "`" and s.count("`") == 2:
        s = s[1:-1].strip()
    return s


def lire_entropie(texte: str) -> int:
    """Une seule ligne exacte « Entropie : <entier> » (tiret de liste et guillemets inverses permis), jamais une sous-chaîne."""
    trouvees = [m.group(1) for m in (_ENTROPIE.fullmatch(_contenu(l)) for l in texte.splitlines()) if m]
    if len(trouvees) != 1:
        raise RefusRegistre(f"texte : {len(trouvees)} ligne(s) exacte(s) « Entropie : <entier> », exactement une attendue")
    e = int(trouvees[0])
    if e < ENTROPIE_MINIMALE:
        raise RefusRegistre(f"entropie {e} < 2³² : ni une année, ni une date, ni une petite graine ; un entier tiré une fois "
                            "(par exemple `numpy.random.SeedSequence().entropy`) attendu")
    return e


def lire_configuration_texte(chemin: Path) -> dict:
    """Section `## Configuration canonique de la commande` (une seule, faite seulement de lignes `clé : valeur`) et ligne
    `Entropie : <entier>` du texte. Refus : `RefusRegistre`."""
    texte = Path(chemin).read_text(encoding="utf-8")
    n = sum(1 for t in re.findall(r"^## +(.+?)\s*$", texte, flags=re.M) if t == SECTION_CONFIGURATION)
    if n != 1:
        raise RefusRegistre(f"texte : {n} section(s) « ## {SECTION_CONFIGURATION} », exactement une attendue")
    valeurs, fautes = {}, []
    for ligne in prereg.sections(texte)[SECTION_CONFIGURATION].splitlines():
        if not ligne.strip():
            continue
        m = _CLE_VALEUR.fullmatch(_contenu(ligne))
        if not m:
            fautes.append(f"ligne {ligne.strip()!r} : « clé : valeur » attendue (rien d'autre dans cette section)")
            continue
        cle, val = m.group(1), m.group(2).strip()
        if len(val) >= 2 and val[0] == "`" and val[-1] == "`":
            val = val[1:-1].strip()
        if cle == "Entropie":
            continue                                        # lue par `lire_entropie`, ligne exacte, sur tout le texte
        if cle not in CLES_SECTION:
            fautes.append(f"clé {cle!r} inconnue (attendues : {', '.join(CLES_SECTION)} et la ligne Entropie)")
        elif cle in valeurs:
            fautes.append(f"clé {cle!r} en double")
        else:
            valeurs[cle] = val
    manque = [k for k in CLES_SECTION if k not in valeurs]
    if manque:
        fautes.append(f"clé(s) absente(s) : {', '.join(manque)}")
    if fautes:
        raise RefusRegistre(f"section « {SECTION_CONFIGURATION} » : " + " ; ".join(fautes))
    if valeurs["augmentation"] not in X2.AUGMENTATIONS:
        raise RefusRegistre(f"configuration du texte : augmentation {valeurs['augmentation']!r} (papier ou code)")
    forme = _FORME_RUN.fullmatch(valeurs["run-id"])
    if not forme:
        raise RefusRegistre(f"configuration du texte : forme de l'identifiant du run {valeurs['run-id']!r} "
                            "(« AAAAMMJJ-HHMMSS-<nom> » attendue)")
    if valeurs["registre"] != REGISTRE:
        raise RefusRegistre(f"configuration du texte : registre {valeurs['registre']!r} ≠ registre fixé {REGISTRE}")
    return {"augmentation": valeurs["augmentation"], "couches_familles": couches_familles(valeurs["couches-familles"]),
            "couches_familles_texte": valeurs["couches-familles"], "forme_run_id": valeurs["run-id"],
            "nom_run": forme.group(1), "registre": valeurs["registre"], "entropie": lire_entropie(texte)}


def comparer_configuration(conf: dict, augmentation: str, couches_spec: str, run_id: str, entropie: int) -> dict:
    """La commande doit dire ce que dit le texte scellé ; tout écart → refus (code 2)."""
    fautes = []
    if augmentation != conf["augmentation"]:
        fautes.append(f"augmentation {augmentation!r} ≠ {conf['augmentation']!r} du texte")
    couches = couches_familles(couches_spec)
    if couches != conf["couches_familles"]:
        fautes.append(f"couches de nos familles {couches_spec!r} ≠ {conf['couches_familles_texte']!r} du texte")
    motif = re.compile(r"[0-9]{8}-[0-9]{6}-" + re.escape(conf["nom_run"]))
    if not motif.fullmatch(run_id) or not FORME_MANIFESTE.match(run_id):
        fautes.append(f"identifiant du run {run_id!r} hors de la forme {conf['forme_run_id']!r} du texte")
    else:
        try:
            datetime.strptime(run_id[:15], "%Y%m%d-%H%M%S")
        except ValueError:
            fautes.append(f"identifiant du run {run_id!r} : date ou heure impossible")
    if isinstance(entropie, bool) or int(entropie) != conf["entropie"]:
        fautes.append("entropie de la commande ≠ ligne « Entropie : <entier> » du texte (comparées en entiers)")
    if fautes:
        raise RefusRegistre("commande ≠ configuration canonique du texte scellé : " + " ; ".join(fautes))
    return couches


def exiger_jamais_ouverte(depot: Path, nom_run: str) -> None:
    """Un dossier `runs/*-<nom>` ou un résultat `diag/*/externe-narcbench-v2.json` existe → refus : une lecture ouverte n'est
    jamais relancée (nœud)."""
    depot = Path(depot)
    deja = sorted(str(p.relative_to(depot)) for p in (depot / "runs").glob(f"*-{nom_run}"))
    deja += sorted(str(p.relative_to(depot)) for p in (depot / "diag").glob(f"*/{NOM_RESULTAT}.json"))
    if deja:
        raise RefusRegistre(f"lecture du bras externe déjà ouverte ({', '.join(deja[:3])}) : jamais relancée sous ce texte (nœud)")


# ---------- code (n° 4) et scikit-learn (n° 7) ----------

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
    """Liste d'arrêt n° 4 : commit exécuté = commit de la fiche (au sens de DF-02 de T0.7), arbre de travail propre."""
    depot = Path(depot)
    top = _git(depot, "rev-parse", "--show-toplevel")
    if top.returncode != 0 or Path(top.stdout.decode().strip()).resolve() != depot.resolve():
        raise GardeArret(f"{depot} n'est pas la racine d'un dépôt git")
    etat = etat_git(depot)
    if not etat["propre"]:
        raise GardeArret("arbre de travail modifié : arrêt (liste d'arrêt n° 4)\n" + etat["statut"])
    commit = fiche["commit"]
    if _git(depot, "cat-file", "-e", f"{commit}^{{commit}}").returncode != 0:
        raise GardeArret(f"commit de la fiche {commit[:12]}… absent du dépôt (liste d'arrêt n° 4)")
    if _git(depot, "merge-base", "--is-ancestor", commit, "HEAD").returncode != 0:
        raise GardeArret(f"commit de la fiche {commit[:12]}… : ni HEAD ni un de ses ancêtres (liste d'arrêt n° 4)")
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
        raise GardeArret(f"code exécuté ≠ code de la fiche ({commit[:12]}…) : arrêt (liste d'arrêt n° 4) : " + " ; ".join(ecarts))
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


# ---------- résultat ----------

def taches_graines(couches: dict, familles=X2.FAMILLES_EXTERNES) -> list:
    return [f"{m}/{X2.cle_graine_famille(f, c, t)}" for m, cs in couches.items() for c in cs for f in familles
            for t in X2.TACHES_FAMILLE]


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


# ---------- lecture ----------

def lire(args, instant: int, attendues: dict | None = None, etat: dict | None = None) -> dict:
    etat = {} if etat is None else etat
    depot = Path(args.depot).resolve()
    garde = garde_registre(depot, args.texte, instant)                                                    # n° 3
    conf = lire_configuration_texte(depot / garde["texte"]["chemin"])
    couches = comparer_configuration(conf, args.augmentation, args.couches_familles, args.run_id, args.entropie)
    exiger_jamais_ouverte(depot, conf["nom_run"])
    fiche = lire_fiche_code(depot / garde["code"]["chemin"])                                               # n° 4
    code = exiger_code_de_la_fiche(depot, fiche)
    skl = version_installee("scikit-learn")                                                               # n° 7
    temoin_lisible = skl == fiche["scikit-learn"]
    verif = C.verifier_fichiers(args.donnees, C.EMPREINTES_PUBLIEES if attendues is None else attendues)  # n° 1
    exiger_sans_transfert(args.donnees)                                                                  # n° 2
    metas, exclusions = {}, {}
    for modele in C.MODELES:                                                                              # n° 5, 6
        for etage in C.ETAGES:
            meta = C.charger_metadonnees(Path(args.donnees) / "activations" / modele / etage / "metadata_gen.json")
            exclusions[f"{modele}/{etage}"] = X2.exiger_exclusions(meta, etage.upper())
            metas[(modele, etage)] = meta
    config = {"objet": OBJET, "texte": garde["texte"], "code": garde["code"], "registre": garde,
              "configuration_du_texte": {k: (v if k != "couches_familles" else {m: list(c) for m, c in v.items()})
                                         for k, v in conf.items()},
              "fiche_code": fiche, "controle_du_code": code,
              "scikit_learn": {"installee": skl, "fiche": fiche["scikit-learn"], "temoin_lisible": temoin_lisible},
              "revision_jeu": C.REVISION_JEU, "donnees": {"racine": str(args.donnees), "fichiers": verif},
              "augmentation": conf["augmentation"], "graines_auteurs": list(X2.GRAINES_AUTEURS),
              "bandes": {m: list(C.BANDES[m]) for m in C.MODELES}, "couches_familles": {m: list(c) for m, c in couches.items()},
              "familles": list(X2.FAMILLES_EXTERNES), "n_plancher": 200, "n_tirages": 2000, "n_permutations": 200,
              "recette": {"lr": X2.PARAMETRES_LR, "mode_core": "par-pli", "source": "probes/reproduce_LR.py @ 85fea3be2a9d"},
              "versions_supplementaires": _versions()}
    chemin_m, manifeste = creer_manifeste(depot, args.run_id, config, taches_graines(couches), entropie=conf["entropie"],
                                          decisif=False, prereg=depot / garde["texte"]["chemin"], commande=" ".join(sys.argv))
    etat["ouvert"] = True
    journaliser(depot, "OUVERTURE-NARC-EXT", instant, args.run_id, f"manifeste {sha256_de(chemin_m)}")
    resultat = {"modeles": {}, "garde_registre": garde, "controle_du_code": code, "exclusions": exclusions,
                "marque": X2.MARQUE_DIAGNOSTIC}
    for modele in C.MODELES:
        d = {}
        for etage in C.ETAGES:
            meta = metas[(modele, etage)]
            base = Path(args.donnees) / "activations" / modele / etage
            d[etage.upper()] = (meta, C.charger_couches(base / "activations_gen.npz", C.BANDES[modele], len(meta),
                                                        C.LARGEURS[modele]))
        if temoin_lisible:
            repro = X2.reproduire_helios_v2(d["CORE"], d["STEGO"], C.BANDES[modele], conf["augmentation"])
            garde_r = X2.garde_reproduction_v2(NOMS_PUBLIES[modele], repro)
        else:
            repro = {"etat": X2.GARDE_SKLEARN, "installee": skl, "fiche": fiche["scikit-learn"]}
            garde_r = {"modele": NOMS_PUBLIES[modele], "etat": X2.GARDE_SKLEARN}
        fam = {}
        for c in couches[modele]:
            g = {X2.cle_graine_famille(f, c, t): int(generateur(manifeste["graines"][f"{modele}/{X2.cle_graine_famille(f, c, t)}"])
                                                    .integers(2 ** 31))
                 for f in X2.FAMILLES_EXTERNES for t in X2.TACHES_FAMILLE}
            fam[str(c)] = X2.nos_familles_v2(d["CORE"][0], d["CORE"][1][c], d["STEGO"][0], d["STEGO"][1][c], c, g)
        resultat["modeles"][modele] = {"reproduction": repro, "garde_reproduction": garde_r, "nos_familles": fam}
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
    Codes : 0 lu ; 2 refus de la garde d'ouverture (n° 3, configuration, déjà ouverte), journalisé ; 1 tout autre arrêt,
    journalisé, motif imprimé sans trace d'erreur."""
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
        print(f"refus de la garde d'ouverture (rien d'écrit ; {'journalisé' if j else 'journal absent'}) : {e}", file=sys.stderr)
        return 2
    except GardeArret as e:
        cle = "ARRET-NARC-EXT" if etat["ouvert"] else "REFUS-NARC-EXT"
        j = journaliser(depot, cle, instant, args.run_id, f"arrêt : {e}")
        print(f"arrêt {'après ouverture' if etat['ouvert'] else 'avant ouverture, rien écrit'} "
              f"({'journalisé' if j else 'journal absent'}) : {e}", file=sys.stderr)
        return 1
    print(sortie)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["REGISTRE", "JOURNAL", "CLE_SCELLEMENT", "CLE_CODE", "CLE_LECTURE", "SECTION_CONFIGURATION", "CLES_SECTION",
           "lire_registre_externe", "garde_registre", "couches_familles", "lire_entropie", "lire_configuration_texte",
           "comparer_configuration", "exiger_jamais_ouverte", "lire_fiche_code", "exiger_code_de_la_fiche", "fiche_code",
           "paquet_execute", "exiger_sans_transfert", "valeurs_non_finies", "journaliser", "taches_graines", "lire", "main",
           "analyseur"]

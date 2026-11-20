#!/usr/bin/env python3
"""Vérification de l'environnement d'un agent — v1 (bibliothèque standard seulement).

Programme écrit d'avance pour les agents du compte (GO-2026-11-19-93, mesure (b)) : tout ce qu'un agent vérifie d'ordinaire au
début d'un travail, dans un fichier qu'on lance par son chemin, sans code en ligne passé à un interpréteur.

Usage (depuis n'importe quel dossier) :

    python3 -B scripts/verifier_environnement_agent_v1.py [--empreintes FICHIER_LISTE] [--modules numpy,pytest,...]
                                                          [--depot CHEMIN] [--sortie FICHIER_JSON]

Rend un rapport JSON (UTF-8) sur la sortie standard et, avec `--sortie`, dans un fichier neuf accompagné de `<sortie>.sha256`
(format `sha256sum`) ; les deux portent les mêmes octets.
  - toujours : programme et son empreinte, heure UTC, dossier courant, version de Python, chemin de l'interpréteur, plateforme ;
  - `--modules a,b.c` : pour chaque module, « present », « absent » ou « erreur_import » (import protégé : toute exception,
    `SystemExit` comprise, est rapportée ; ce qu'il écrit sur la sortie standard pendant l'import est retenu et compté, pour
    ne pas abîmer le JSON), sa version s'il l'expose (`__version__`, sinon les métadonnées de sa distribution) et son fichier ;
  - `--empreintes LISTE` : un chemin par ligne, ou une ligne au format `sha256sum` (« EMPREINTE␣␣chemin » ou
    « EMPREINTE␣*chemin ») ; lignes vides et lignes commençant par `#` ignorées. **Un chemin relatif se lit depuis le dossier de
    la liste** (comme `cd dossier && sha256sum -c liste`) : un compagnon `.sha256` du dépôt sert donc de liste tel quel. Pour
    chaque chemin : existence, type, taille, sha256, égalité à l'empreinte attendue ;
  - `--depot CHEMIN` : tête (`git rev-parse HEAD`), branche (`git symbolic-ref`), arbre propre ou non (`git status
    --porcelain`), par appel de `git` avec une liste d'arguments fixe, sans shell, avec `--no-optional-locks` (git n'écrit pas
    l'index) et les variables d'environnement `GIT_*` de l'appelant retirées. `git status` porte sur tout l'arbre (`:/`) **sauf**
    les chemins qui contiennent `archives-reponses-modeles` (exclusion déclarée dans le rapport).

Segment interdit : tout chemin qui contient `archives-reponses-modeles` (casse ignorée) est refusé **sans être touché** — ni
ouvert, ni lu, ni mesuré, ni même examiné par `stat`. Le chemin est d'abord contrôlé tel qu'écrit, puis résolu composant par
composant ; chaque composant et chaque cible de lien symbolique sont contrôlés avant le moindre appel au système de fichiers.
Le contrôle vaut pour les chemins de la liste et pour ceux de `--empreintes`, `--depot` et `--sortie`.

Ordre : toutes les entrées sont validées d'abord (options, noms de modules, syntaxe de la liste, segment interdit, sortie
absente, dépôt présent) ; au moindre refus, aucun fichier de la liste n'est lu, aucun module importé, `git` n'est pas lancé et
rien n'est écrit ; tous les motifs sont donnés (sortie d'erreur, après `REFUS :`, et rapport JSON réduit sur la sortie standard).

Codes de sortie : 0 tout est lu ; 3 au moins une empreinte attendue n'est pas égalée (fichier différent, absent, illisible ou
non ordinaire) ; 2 entrée invalide ou chemin refusé (argparse rend aussi 2), ou écriture de la sortie impossible. Un module
absent, un dépôt non git ou un fichier absent sans empreinte attendue sont rapportés, pas comptés comme écarts.

Garanties : aucun réseau ; aucun autre processus que `git` (la plateforme est lue par `os.uname`, jamais par
`platform.platform()` qui lance `uname -p`) ; aucune écriture hors du fichier de sortie et de son compagnon, créés en mode
exclusif (jamais écrasés, R12 ; un lien symbolique pendant compte comme existant).
Développeur, modèle L′.
"""
from __future__ import annotations

import argparse
import contextlib
import datetime
import hashlib
import importlib
import importlib.metadata
import io
import json
import os
import platform
import re
import shutil
import stat
import subprocess
import sys
from pathlib import Path

NOM_PROGRAMME = "verifier_environnement_agent_v1"
SEGMENT_INTERDIT = "archives-reponses-modeles"
CODE_LU, CODE_REFUS, CODE_ECART = 0, 2, 3
SUFFIXE_SHA = ".sha256"
TAILLE_BLOC = 1 << 20
MAX_LIENS = 40
MAX_LIGNES_STATUS = 200
DELAI_GIT = 60
RE_MODULE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*")
RE_LIGNE_SHA = re.compile(r"([0-9a-fA-F]{64}) ([ *])(.+)")
RE_DEBUT_SHA = re.compile(r"[0-9a-fA-F]{64}(?:$|[\s*])")
RE_TETE = re.compile(r"[0-9a-f]{40}(?:[0-9a-f]{24})?")
EXCLUSIONS_STATUS = (
    f":(top,exclude,glob,icase)**/*{SEGMENT_INTERDIT}*",
    f":(top,exclude,glob,icase)**/*{SEGMENT_INTERDIT}*/**",
)
OPTIONS_GIT = ("--no-pager", "--no-optional-locks", "-c", "core.fsmonitor=false")


class Refus(Exception):
    """Entrée invalide ou chemin refusé : code 2."""


# ------------------------------------------------------------------------------------------------------------ outillage

def heure_utc() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_octets(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def empreinte_programme() -> str | None:
    try:
        return sha256_octets(Path(__file__).read_bytes())
    except OSError:
        return None


def contient_segment(chemin) -> bool:
    return SEGMENT_INTERDIT in os.fsdecode(chemin).casefold()


def motif_segment(role: str, chemin: str, detail: str = "") -> str:
    return (f"{role} « {chemin} » : le chemin contient « {SEGMENT_INTERDIT} »{detail} ; refusé sans y accéder "
            f"(ni lecture, ni empreinte, ni taille, ni stat)")


def resoudre_sans_toucher(chemin: str, base: str, role: str) -> str:
    """Chemin absolu sans lien symbolique ; Refus si le segment interdit apparaît à une étape quelconque.

    Aucun appel au système de fichiers n'est fait sur un chemin qui contient le segment : le chemin tel qu'écrit, chaque
    composant (avant `lstat`) et chaque cible de lien (avant de la suivre) sont contrôlés d'abord. `base` doit être un dossier
    déjà résolu (sans lien), ou le dossier courant.
    """
    if chemin == "":
        raise Refus(f"{role} : chemin vide")
    if "\0" in chemin:
        raise Refus(f"{role} {chemin!r} : caractère nul dans le chemin")
    if contient_segment(chemin):
        raise Refus(motif_segment(role, chemin))
    depart = chemin if os.path.isabs(chemin) else os.path.join(base, chemin)
    pile = list(reversed(depart.split(os.sep)))
    courant = os.sep
    sauts = 0
    while pile:
        comp = pile.pop()
        if comp in ("", "."):
            continue
        if comp == "..":
            courant = os.path.dirname(courant)
            continue
        candidat = os.path.join(courant, comp)
        if contient_segment(candidat):
            raise Refus(motif_segment(role, chemin, f" une fois résolu ({candidat})"))
        if os.path.islink(candidat):
            sauts += 1
            if sauts > MAX_LIENS:
                raise Refus(f"{role} « {chemin} » : plus de {MAX_LIENS} liens symboliques à suivre (boucle ?)")
            try:
                cible = os.readlink(candidat)
            except OSError as e:
                raise Refus(f"{role} « {chemin} » : lien {candidat} illisible ({type(e).__name__} : {e})") from None
            if contient_segment(cible):
                raise Refus(motif_segment(role, chemin, f" par le lien {candidat} → {cible}"))
            if os.path.isabs(cible):
                courant = os.sep
            pile.extend(reversed(cible.split(os.sep)))
        else:
            courant = candidat
    return courant


def dossier_courant() -> str:
    try:
        return os.getcwd()
    except OSError as e:
        raise Refus(f"dossier courant illisible ({type(e).__name__} : {e})") from None


# ------------------------------------------------------------------------------------------------- validation des entrées

def valider_sortie(brut: str) -> str:
    cwd = dossier_courant()
    resolu = resoudre_sans_toucher(brut, cwd, "--sortie")
    lexical = brut if os.path.isabs(brut) else os.path.join(cwd, brut)
    for p in (lexical, lexical + SUFFIXE_SHA, resolu, resolu + SUFFIXE_SHA):
        if os.path.lexists(p):
            raise Refus(f"--sortie : {p} existe déjà (même un lien symbolique compte) ; jamais réécrit (R12), "
                        f"choisir un nouveau nom")
    if not os.path.isdir(os.path.dirname(resolu)):
        raise Refus(f"--sortie : dossier {os.path.dirname(resolu)} absent")
    return resolu


def valider_depot(brut: str) -> str:
    resolu = resoudre_sans_toucher(brut, dossier_courant(), "--depot")
    if not os.path.exists(resolu):
        raise Refus(f"--depot « {brut} » : absent ({resolu})")
    if not os.path.isdir(resolu):
        raise Refus(f"--depot « {brut} » : pas un dossier ({resolu})")
    return resolu


def analyser_modules(brut: str) -> list[str]:
    noms = brut.split(",")
    mauvais = [n for n in noms if not RE_MODULE.fullmatch(n)]
    if mauvais:
        raise Refus(f"--modules « {brut} » : nom(s) de module invalide(s) {mauvais} (attendu : noms Python pointés, séparés "
                    f"par des virgules, sans espace ni élément vide)")
    return noms


def lire_liste(brut: str) -> tuple[dict, list[str]]:
    """Rend (liste, refus par ligne). Lève Refus si la liste elle-même est refusée. Ne lit aucun fichier de la liste."""
    resolu = resoudre_sans_toucher(brut, dossier_courant(), "--empreintes")
    try:
        st = os.stat(resolu)
    except FileNotFoundError:
        raise Refus(f"--empreintes « {brut} » : absent ({resolu})") from None
    except OSError as e:
        raise Refus(f"--empreintes « {brut} » : illisible ({type(e).__name__} : {e})") from None
    if not stat.S_ISREG(st.st_mode):
        raise Refus(f"--empreintes « {brut} » : pas un fichier ordinaire")
    try:
        octets = Path(resolu).read_bytes()
    except OSError as e:
        raise Refus(f"--empreintes « {brut} » : illisible ({type(e).__name__} : {e})") from None
    try:
        texte = octets.decode("utf-8", errors="strict")
    except UnicodeDecodeError as e:
        raise Refus(f"--empreintes « {brut} » : UTF-8 illisible ({e.reason}, octet {e.start})") from None
    if texte.startswith("﻿"):
        raise Refus(f"--empreintes « {brut} » : marque d'ordre des octets en tête ; à retirer")
    base = os.path.dirname(resolu)
    entrees, refus = [], []
    for n, ligne in enumerate(texte.split("\n"), 1):
        if ligne.endswith("\r"):
            ligne = ligne[:-1]
        if not ligne.strip() or ligne.startswith("#"):
            continue
        role = f"ligne {n} de la liste"
        m = RE_LIGNE_SHA.fullmatch(ligne)
        if m:
            attendu, chemin = m.group(1).lower(), m.group(3)
        elif RE_DEBUT_SHA.match(ligne):
            refus.append(f"{role} : empreinte de 64 caractères sans chemin ou mal séparée (format attendu : "
                         f"« EMPREINTE␣␣chemin » ou « EMPREINTE␣*chemin »)")
            continue
        else:
            attendu, chemin = None, ligne
        if chemin != chemin.strip():
            refus.append(f"{role} « {chemin} » : espace en tête ou en fin de chemin")
            continue
        if chemin.startswith("\\"):
            refus.append(f"{role} « {chemin} » : nom échappé par barre oblique inverse (format sha256sum) non pris en charge")
            continue
        try:
            chemin_resolu = resoudre_sans_toucher(chemin, base, role)
        except Refus as e:
            refus.append(str(e))
            continue
        entrees.append({"ligne": n, "chemin": chemin, "chemin_resolu": chemin_resolu, "attendu": attendu})
    if not entrees and not refus:
        raise Refus(f"--empreintes « {brut} » : aucun chemin dans la liste")
    liste = {"liste": brut, "liste_resolue": resolu, "liste_sha256": sha256_octets(octets),
             "base_des_chemins_relatifs": base, "entrees": entrees}
    return liste, refus


# --------------------------------------------------------------------------------------------------------------- examens

def examiner_python() -> dict:
    return {
        "version": platform.python_version(),
        "version_complete": sys.version,
        "implementation": platform.python_implementation(),
        "executable": sys.executable,
        "prefixe": sys.prefix,
        "prefixe_de_base": sys.base_prefix,
        "environnement_virtuel": sys.prefix != sys.base_prefix,
        "drapeaux": {"ne_pas_ecrire_bytecode": bool(sys.flags.dont_write_bytecode), "isole": bool(sys.flags.isolated),
                     "ignorer_environnement": bool(sys.flags.ignore_environment)},
    }


def examiner_plateforme() -> dict:
    return {
        "sys_platform": sys.platform,
        "nom_os": os.name,
        "systeme": platform.system(),
        "noyau": platform.release(),
        "machine": platform.machine(),
    }


def version_module(mod, nom: str) -> tuple[str | None, str | None]:
    try:
        v = getattr(mod, "__version__", None)
    except Exception:
        v = None
    if v is not None:
        return (v if isinstance(v, str) else str(v)), "__version__"
    racine = nom.split(".")[0]
    try:
        dists = importlib.metadata.packages_distributions().get(racine) or []
    except Exception:
        dists = []
    for d in dists:
        try:
            return importlib.metadata.version(d), f"métadonnées de la distribution {d}"
        except Exception:
            continue
    return None, None


def examiner_module(nom: str) -> dict:
    r = {"nom": nom, "statut": None, "version": None, "source_version": None, "fichier": None, "erreur": None,
         "caracteres_ecrits_sur_sortie_standard_a_l_import": 0}
    tampon = io.StringIO()
    try:
        with contextlib.redirect_stdout(tampon):
            mod = importlib.import_module(nom)
    except ModuleNotFoundError as e:
        if e.name is not None and (nom == e.name or nom.startswith(e.name + ".")):
            r["statut"] = "absent"
        else:
            r["statut"] = "erreur_import"
            r["erreur"] = f"{type(e).__name__} : {e}"
    except (Exception, SystemExit) as e:
        r["statut"] = "erreur_import"
        r["erreur"] = f"{type(e).__name__} : {e}"
    else:
        r["statut"] = "present"
        f = getattr(mod, "__file__", None)
        r["fichier"] = f if isinstance(f, str) else None
        r["version"], r["source_version"] = version_module(mod, nom)
    r["caracteres_ecrits_sur_sortie_standard_a_l_import"] = len(tampon.getvalue())
    return r


def examiner_fichier(e: dict) -> dict:
    p = e["chemin_resolu"]
    r = {"ligne": e["ligne"], "chemin": e["chemin"], "chemin_resolu": p, "existe": False, "type": None, "taille": None,
         "sha256": None, "empreinte_attendue": e["attendu"], "egal_attendu": None, "erreur": None}
    try:
        st = os.stat(p)
    except FileNotFoundError:
        pass
    except OSError as x:
        r["existe"] = None
        r["erreur"] = f"{type(x).__name__} : {x}"
    else:
        r["existe"] = True
        if stat.S_ISREG(st.st_mode):
            r["type"] = "fichier"
            try:
                fd = os.open(p, os.O_RDONLY | getattr(os, "O_NONBLOCK", 0) | getattr(os, "O_NOFOLLOW", 0))
                try:
                    if not stat.S_ISREG(os.fstat(fd).st_mode):
                        raise OSError("n'est plus un fichier ordinaire à l'ouverture")
                    h, n = hashlib.sha256(), 0
                    while True:
                        bloc = os.read(fd, TAILLE_BLOC)
                        if not bloc:
                            break
                        h.update(bloc)
                        n += len(bloc)
                finally:
                    os.close(fd)
                r["taille"], r["sha256"] = n, h.hexdigest()
            except OSError as x:
                r["erreur"] = f"{type(x).__name__} : {x}"
        elif stat.S_ISDIR(st.st_mode):
            r["type"] = "dossier"
        else:
            r["type"] = "autre"
    if e["attendu"] is not None:
        r["egal_attendu"] = r["sha256"] == e["attendu"]
    return r


def environnement_git() -> dict:
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update({"GIT_OPTIONAL_LOCKS": "0", "GIT_TERMINAL_PROMPT": "0", "LC_ALL": "C", "LANGUAGE": "C"})
    return env


def lancer_git(git: str, depot: str | None, *args: str) -> dict:
    """Seul point du programme qui lance un processus : `git`, liste d'arguments fixe, sans shell."""
    cmd = [git, *OPTIONS_GIT, *(["-C", depot] if depot is not None else []), *args]
    try:
        p = subprocess.run(cmd, input=b"", capture_output=True, timeout=DELAI_GIT, env=environnement_git(),
                           shell=False, check=False)
    except (OSError, subprocess.SubprocessError) as e:
        return {"code": None, "sortie": "", "erreur": f"{type(e).__name__} : {e}"}
    return {"code": p.returncode, "sortie": p.stdout.decode("utf-8", errors="replace"),
            "erreur": p.stderr.decode("utf-8", errors="replace").strip()}


def examiner_depot(brut: str, resolu: str) -> dict:
    r = {"chemin": brut, "chemin_resolu": resolu, "git_executable": None, "git_version": None, "est_depot_git": None,
         "racine": None, "tete": None, "branche": None, "tete_detachee": None, "arbre_propre": None,
         "lignes_status": None, "lignes_status_tronquees": None, "nombre_lignes_status": None,
         "pathspecs_status": [":/", *EXCLUSIONS_STATUS], "erreurs": []}
    git = shutil.which("git")
    if git is None:
        r["erreurs"].append("git introuvable dans PATH")
        return r
    r["git_executable"] = git
    v = lancer_git(git, None, "--version")
    r["git_version"] = v["sortie"].strip() or None
    d = lancer_git(git, resolu, "rev-parse", "--is-inside-work-tree")
    if d["code"] != 0 or d["sortie"].strip() != "true":
        r["est_depot_git"] = False
        r["erreurs"].append(d["erreur"] or f"git rev-parse --is-inside-work-tree : {d['sortie'].strip()!r}")
        return r
    r["est_depot_git"] = True
    t = lancer_git(git, resolu, "rev-parse", "--show-toplevel")
    if t["code"] == 0:
        r["racine"] = t["sortie"].strip()
    else:
        r["erreurs"].append(f"racine : {t['erreur']}")
    h = lancer_git(git, resolu, "rev-parse", "HEAD")
    if h["code"] == 0 and RE_TETE.fullmatch(h["sortie"].strip()):
        r["tete"] = h["sortie"].strip()
    else:
        r["erreurs"].append(f"tête illisible (aucun commit ?) : {h['erreur'] or h['sortie'].strip()}")
    b = lancer_git(git, resolu, "symbolic-ref", "--short", "-q", "HEAD")
    if b["code"] == 0:
        r["branche"], r["tete_detachee"] = b["sortie"].strip(), False
    elif b["code"] == 1:
        r["branche"], r["tete_detachee"] = None, True
    else:
        r["erreurs"].append(f"branche : {b['erreur']}")
    s = lancer_git(git, resolu, "status", "--porcelain", "--untracked-files=normal", "--", ":/", *EXCLUSIONS_STATUS)
    if s["code"] == 0:
        lignes = [l for l in s["sortie"].split("\n") if l]
        r["arbre_propre"] = not lignes
        r["nombre_lignes_status"] = len(lignes)
        r["lignes_status"] = lignes[:MAX_LIGNES_STATUS]
        r["lignes_status_tronquees"] = len(lignes) > MAX_LIGNES_STATUS
    else:
        r["erreurs"].append(f"status : {s['erreur']}")
    return r


# ------------------------------------------------------------------------------------------------------------- écriture

def emettre(octets: bytes) -> None:
    sys.stdout.flush()
    sys.stdout.buffer.write(octets)
    sys.stdout.buffer.flush()


def ecrire_sortie(chemin: str, octets: bytes) -> None:
    compagnon = chemin + SUFFIXE_SHA
    contenus = ((chemin, octets),
                (compagnon, f"{sha256_octets(octets)}  {os.path.basename(chemin)}\n".encode("utf-8")))
    crees: list[str] = []
    try:
        for p, c in contenus:
            with open(p, "xb") as f:
                crees.append(p)
                f.write(c)
                f.flush()
                os.fsync(f.fileno())
        for p, c in contenus:
            if Path(p).read_bytes() != c:
                raise Refus(f"relecture : {p} ne porte pas les octets écrits")
    except (OSError, Refus) as e:
        restes = []
        for p in reversed(crees):
            try:
                os.unlink(p)
            except OSError:
                restes.append(p)
        msg = f"écriture de la sortie impossible ({type(e).__name__} : {e}) ; fichiers créés par cet appel retirés"
        if restes:
            msg += f" SAUF {restes} (à retirer à la main)"
        raise Refus(msg) from None


def en_octets(rapport: dict) -> bytes:
    return (json.dumps(rapport, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


# ------------------------------------------------------------------------------------------------------------ principal

def main(argv: list[str] | None = None) -> int:
    a = argparse.ArgumentParser(prog="verifier_environnement_agent_v1.py", description=__doc__.split("\n\n")[0],
                                allow_abbrev=False)
    a.add_argument("--empreintes", help="liste : un chemin par ligne, ou « EMPREINTE␣␣chemin » (relatif au dossier de la liste)")
    a.add_argument("--modules", help="noms de modules séparés par des virgules, ex. numpy,pytest")
    a.add_argument("--depot", help="dossier d'un dépôt git")
    a.add_argument("--sortie", help="fichier JSON neuf ; refus s'il existe ; compagnon <sortie>.sha256")
    x = a.parse_args(argv)
    heure = heure_utc()

    refus: list[str] = []
    sortie = depot = liste = modules = None
    if x.sortie is not None:
        try:
            sortie = valider_sortie(x.sortie)
        except Refus as e:
            refus.append(str(e))
    if x.depot is not None:
        try:
            depot = valider_depot(x.depot)
        except Refus as e:
            refus.append(str(e))
    if x.modules is not None:
        try:
            modules = analyser_modules(x.modules)
        except Refus as e:
            refus.append(str(e))
    if x.empreintes is not None:
        try:
            liste, refus_lignes = lire_liste(x.empreintes)
            refus.extend(refus_lignes)
        except Refus as e:
            refus.append(str(e))
    if refus:
        for m in refus:
            print(f"REFUS : {m}", file=sys.stderr)
        print("Aucun fichier de la liste lu, aucun module importé, git non lancé, aucun fichier écrit.", file=sys.stderr)
        emettre(en_octets({"programme": NOM_PROGRAMME, "programme_sha256": empreinte_programme(), "heure_utc": heure,
                           "statut": "refus", "refus": refus, "code_retour": CODE_REFUS}))
        return CODE_REFUS

    ici = os.path.dirname(os.path.realpath(__file__))
    if sys.path and sys.path[0] and os.path.realpath(sys.path[0]) == ici:
        del sys.path[0]  # le dossier du programme n'est pas un dossier de modules de l'environnement

    rapport = {"programme": NOM_PROGRAMME, "programme_sha256": empreinte_programme(), "heure_utc": heure,
               "repertoire_courant": dossier_courant(), "python": examiner_python(), "plateforme": examiner_plateforme(),
               "modules": None, "empreintes": None, "depot": None, "fichier_sortie": sortie}
    anomalies: list[str] = []
    ecarts: list[dict] = []
    if modules is not None:
        rapport["modules"] = [examiner_module(n) for n in modules]
        anomalies += [f"module {m['nom']} : {m['erreur']}" for m in rapport["modules"] if m["statut"] == "erreur_import"]
    if liste is not None:
        fichiers = [examiner_fichier(e) for e in liste["entrees"]]
        for f in fichiers:
            if f["egal_attendu"] is False:
                ecarts.append({"ligne": f["ligne"], "chemin": f["chemin"], "attendue": f["empreinte_attendue"],
                               "lue": f["sha256"], "existe": f["existe"], "type": f["type"], "erreur": f["erreur"]})
            elif f["empreinte_attendue"] is None and (f["existe"] is not True or f["type"] != "fichier" or f["erreur"]):
                anomalies.append(f"ligne {f['ligne']} « {f['chemin']} » : existe={f['existe']}, type={f['type']}, "
                                 f"erreur={f['erreur']}")
        rapport["empreintes"] = {k: liste[k] for k in ("liste", "liste_resolue", "liste_sha256", "base_des_chemins_relatifs")}
        rapport["empreintes"].update({"nombre": len(fichiers), "fichiers": fichiers, "ecarts": ecarts})
    if depot is not None:
        rapport["depot"] = examiner_depot(x.depot, depot)
        if not rapport["depot"]["est_depot_git"]:
            anomalies.append(f"--depot {x.depot} : pas un dépôt git lisible")
        anomalies += [f"dépôt : {m}" for m in rapport["depot"]["erreurs"] if rapport["depot"]["est_depot_git"]]
    code = CODE_ECART if ecarts else CODE_LU
    rapport.update({"anomalies": anomalies, "statut": "ecart" if code == CODE_ECART else "lu", "code_retour": code})
    octets = en_octets(rapport)

    if sortie is not None:
        try:
            ecrire_sortie(sortie, octets)
        except Refus as e:
            emettre(octets)
            print(f"REFUS : {e}", file=sys.stderr)
            return CODE_REFUS
    emettre(octets)
    for c in ecarts:
        print(f"ECART : ligne {c['ligne']} « {c['chemin']} » : empreinte attendue {c['attendue']}, lue "
              f"{c['lue'] or 'aucune'} (existe={c['existe']}, type={c['type']})", file=sys.stderr)
    return code


if __name__ == "__main__":
    sys.exit(main())

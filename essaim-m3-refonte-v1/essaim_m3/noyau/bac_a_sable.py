"""Bac à sable : exécute le code de l'organisme hors du processus du noyau, sans clé, sans réseau, borné.

Ce que faisait Gemini (B-13, B-14) : le superviseur exécutait, dans le même environnement que ses clés et son dépôt,
un script réécrit par un modèle, puis poussait sur `main`. Ici le code de l'organisme tourne dans un sous-processus :
- environnement vide (ni clé, ni mandataire, ni jeton de dépôt) ; seul `ESSAIM_SOCKET` pointe vers le serveur
  d'appels du noyau ;
- `python -I -s` (pas de variables d'environnement Python, pas de dossier utilisateur), dossier de travail propre ;
- limites de processeur, de mémoire, de taille de fichier (`resource.setrlimit`) et de temps (`timeout`) ;
- isolation réseau par `unshare -rn` quand le conteneur le permet ; sinon le mode réel est refusé, et la
  simulation le dit (aucun appel réseau n'est possible sans clé de toute façon, mais la garde est exigée en réel) ;
- jamais de commande git.
"""
from __future__ import annotations

import json
import os
import pathlib
import resource
import shutil
import subprocess
import sys
import time

from .contrat import CLIENT_SOURCE

LANCEUR_SOURCE = '''import importlib, json, os, sys, traceback
racine = os.getcwd()
sys.path.insert(0, os.path.join(racine, "organisme"))
sys.path.insert(0, racine)
contexte = json.load(open(os.environ["ESSAIM_CONTEXTE"], encoding="utf-8"))
manifeste = json.load(open(os.path.join(racine, "organisme", "manifeste.json"), encoding="utf-8-sig"))
module, fonction = manifeste["entree"].split(":", 1)
statut = {"code": "OK", "erreur": None}
try:
    m = importlib.import_module(module)
    resultat = getattr(m, fonction)(contexte)
    statut["retour"] = str(resultat)[:2000] if resultat is not None else None
except BaseException as e:  # tout : l'organisme ne doit pas pouvoir faire taire le noyau
    statut = {"code": "EXCEPTION", "erreur": traceback.format_exc()[-4000:]}
with open("statut_execution.json", "w", encoding="utf-8") as fh:
    json.dump(statut, fh, ensure_ascii=False)
'''


def isolation_reseau_disponible() -> bool:
    if shutil.which("unshare") is None:
        return False
    try:
        r = subprocess.run(["unshare", "-rn", "true"], capture_output=True, timeout=10)
        return r.returncode == 0
    except (OSError, subprocess.SubprocessError):
        return False


def _limites(memoire_mo: int, cpu_s: int, fichier_mo: int):
    def applique():
        try:
            resource.setrlimit(resource.RLIMIT_AS, (memoire_mo * 1024 * 1024, memoire_mo * 1024 * 1024))
        except (ValueError, OSError):
            pass
        resource.setrlimit(resource.RLIMIT_CPU, (cpu_s, cpu_s))
        resource.setrlimit(resource.RLIMIT_FSIZE, (fichier_mo * 1024 * 1024, fichier_mo * 1024 * 1024))
        resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    return applique


def preparer(dossier_travail: pathlib.Path, organisme: pathlib.Path, contexte: dict) -> pathlib.Path:
    dossier_travail.mkdir(parents=True, exist_ok=True)
    cible = dossier_travail / "organisme"
    if cible.exists():
        shutil.rmtree(cible)
    shutil.copytree(organisme, cible, symlinks=False)
    (dossier_travail / "noyau_client.py").write_text(CLIENT_SOURCE, encoding="utf-8")
    (dossier_travail / "lanceur.py").write_text(LANCEUR_SOURCE, encoding="utf-8")
    chemin_ctx = dossier_travail / "contexte.json"
    chemin_ctx.write_text(json.dumps(contexte, ensure_ascii=False, indent=1), encoding="utf-8")
    return chemin_ctx


def executer(dossier_travail: pathlib.Path, chemin_socket: str, temps_max_s: int, memoire_mo: int = 2048,
             cpu_s: int | None = None, fichier_mo: int = 256, isoler_reseau: bool = False) -> dict:
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "HOME": str(dossier_travail),
           "PYTHONDONTWRITEBYTECODE": "1", "PYTHONIOENCODING": "utf-8",
           "ESSAIM_SOCKET": chemin_socket, "ESSAIM_CONTEXTE": str(dossier_travail / "contexte.json")}
    commande = [sys.executable, "-I", "-s", "-u", "lanceur.py"]
    if isoler_reseau:
        if not isolation_reseau_disponible():
            return {"code": "ISOLATION_INDISPONIBLE", "retour": None, "duree_s": 0.0, "delai_depasse": False}
        commande = ["unshare", "-rn", "--"] + commande
    debut = time.time()
    sortie = (dossier_travail / "sortie.txt").open("w", encoding="utf-8")
    erreurs = (dossier_travail / "erreurs.txt").open("w", encoding="utf-8")
    delai = False
    try:
        proc = subprocess.run(commande, cwd=str(dossier_travail), env=env, stdout=sortie, stderr=erreurs,
                              timeout=temps_max_s, preexec_fn=_limites(memoire_mo, cpu_s or temps_max_s, fichier_mo))
        code_retour = proc.returncode
    except subprocess.TimeoutExpired:
        delai = True
        code_retour = None
    finally:
        sortie.close()
        erreurs.close()
    duree = time.time() - debut
    statut_fichier = dossier_travail / "statut_execution.json"
    statut = None
    if statut_fichier.exists():
        try:
            statut = json.loads(statut_fichier.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            statut = {"code": "STATUT_ILLISIBLE"}
    if delai:
        code = "DELAI_DEPASSE"
    elif statut is None:
        code = "SANS_STATUT"
    else:
        code = statut.get("code", "SANS_STATUT")
    return {"code": code, "code_retour": code_retour, "duree_s": round(duree, 2), "delai_depasse": delai,
            "statut": statut, "isolation_reseau": isoler_reseau}


LANCEUR_METRIQUE_SOURCE = '''import importlib, json, os, sys, traceback
racine = os.getcwd()
sys.path.insert(0, os.path.join(racine, "metrique"))
sortie = {"code": "OK", "valeur": None, "erreur": None}
try:
    m = importlib.import_module("calculer")
    v = m.calculer(os.path.join(racine, "sorties"))
    sortie["valeur"] = float(v)
except BaseException:
    sortie = {"code": "EXCEPTION", "valeur": None, "erreur": traceback.format_exc()[-3000:]}
with open("resultat_metrique.json", "w", encoding="utf-8") as fh:
    json.dump(sortie, fh, ensure_ascii=False)
'''


def executer_metrique(dossier: pathlib.Path, metrique: pathlib.Path, sorties: pathlib.Path, temps_max_s: int = 120,
                      memoire_mo: int = 1024) -> dict:
    """Exécute `metrique/calculer.py` d'un organisme sur une copie des sorties d'un autre, en bac à sable, sans socket.
    Toute erreur, tout délai, toute valeur non finie vaut « non calculée » (jamais 0 ni 1 par défaut)."""
    dossier.mkdir(parents=True, exist_ok=True)
    if (dossier / "metrique").exists():
        shutil.rmtree(dossier / "metrique")
    if (dossier / "sorties").exists():
        shutil.rmtree(dossier / "sorties")
    shutil.copytree(metrique, dossier / "metrique", symlinks=False)
    shutil.copytree(sorties, dossier / "sorties", symlinks=False,
                    ignore=shutil.ignore_patterns("noyau", "juge", "noyau_client.py", "lanceur.py", "__pycache__", "contexte.json"))
    (dossier / "lanceur_metrique.py").write_text(LANCEUR_METRIQUE_SOURCE, encoding="utf-8")
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "HOME": str(dossier),
           "PYTHONDONTWRITEBYTECODE": "1", "PYTHONIOENCODING": "utf-8"}
    sortie = (dossier / "sortie.txt").open("w", encoding="utf-8")
    erreurs = (dossier / "erreurs.txt").open("w", encoding="utf-8")
    try:
        subprocess.run([sys.executable, "-I", "-s", "-u", "lanceur_metrique.py"], cwd=str(dossier), env=env, stdout=sortie,
                       stderr=erreurs, timeout=temps_max_s, preexec_fn=_limites(memoire_mo, temps_max_s, 64))
    except subprocess.TimeoutExpired:
        return {"code": "DELAI_DEPASSE", "valeur": None, "calculee": False}
    finally:
        sortie.close()
        erreurs.close()
    f = dossier / "resultat_metrique.json"
    if not f.exists():
        return {"code": "SANS_RESULTAT", "valeur": None, "calculee": False}
    try:
        r = json.loads(f.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"code": "RESULTAT_ILLISIBLE", "valeur": None, "calculee": False}
    v = r.get("valeur")
    ok = r.get("code") == "OK" and isinstance(v, (int, float)) and not isinstance(v, bool) and v == v and abs(v) != float("inf")
    return {"code": r.get("code"), "valeur": (float(v) if ok else None), "calculee": bool(ok), "erreur": r.get("erreur")}

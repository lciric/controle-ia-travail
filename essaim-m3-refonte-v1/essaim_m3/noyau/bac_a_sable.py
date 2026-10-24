"""Bac à sable : exécute le code de l'organisme hors du processus du noyau, sans clé, sans réseau, borné.

Ce que faisait Gemini (B-13, B-14) : le superviseur exécutait, dans le même environnement que ses clés et son dépôt,
un script réécrit par un modèle, puis poussait sur `main`. Ici le code de l'organisme tourne dans un sous-processus :
- environnement vide (ni clé, ni mandataire, ni jeton de dépôt) ; seul `ESSAIM_SOCKET` pointe vers le serveur
  d'appels du noyau ;
- `python -I -s` (pas de variables d'environnement Python, pas de dossier utilisateur), dossier de travail propre ;
- limites de processeur, de mémoire, de taille de fichier (`resource.setrlimit`) et de temps (`timeout`) ;
- isolation réseau par `unshare -n` quand le conteneur le permet ; sinon le mode réel est refusé, et la
  simulation le dit (aucun appel réseau n'est possible sans clé de toute façon, mais la garde est exigée en réel) ;
- **isolation du système de fichiers (CR-01 de la contre-lecture R2 du 24 octobre)** : quand le noyau est root (cas du
  conteneur), l'organisme et la métrique tournent sous un **utilisateur non privilégié distinct par lignée**
  (`setgid`/`setuid` dans le sous-processus), le dossier de travail leur appartient, et les dossiers du noyau (banque,
  archive, journaux, travail des autres lignées) sont en 0700 pour root : l'organisme ne peut ni lire les vérités ni
  écrire hors de chez lui ; espaces de noms de montage et de processus (`unshare --mount --pid --fork --kill-child`)
  quand ils sont disponibles ; nouveau groupe de processus, tué à la fin (aucun processus détaché ne survit). Sans
  root, aucune isolation d'utilisateur n'est possible : le mode réel est refusé (pas d'option de contournement) ; la
  simulation tourne en le disant (`capacites_isolation`) ;
- jamais de commande git.
"""
from __future__ import annotations

import json
import os
import pathlib
import resource
import shutil
import signal
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


UID_BASE = 60000  # identifiants d'utilisateur non privilégiés, un par lignée (60000 + indice), hors de tout compte réel
_CAPACITES = None


def _unshare_marche(options: list[str]) -> bool:
    if shutil.which("unshare") is None:
        return False
    try:
        r = subprocess.run(["unshare", *options, "true"], capture_output=True, timeout=10)
        return r.returncode == 0
    except (OSError, subprocess.SubprocessError):
        return False


def capacites_isolation(rafraichir: bool = False) -> dict:
    """Ce que ce système permet : changement d'utilisateur (root seulement), espaces de noms, réseau coupé."""
    global _CAPACITES
    if _CAPACITES is not None and not rafraichir:
        return _CAPACITES
    root = hasattr(os, "geteuid") and os.geteuid() == 0
    cap = {"root": root, "utilisateur": root,  # setuid possible seulement en root
           "reseau": _unshare_marche(["-n"]) if root else _unshare_marche(["-rn"]),
           "espaces_noms": root and _unshare_marche(["--mount", "--pid", "--fork", "--kill-child", "--mount-proc"])}
    _CAPACITES = cap
    return cap


def isolation_reseau_disponible() -> bool:
    return bool(capacites_isolation()["reseau"])


def uid_lignee(indice: int) -> int:
    return UID_BASE + int(indice)


def uid_entraineur(indice: int) -> int:
    """Utilisateur non privilégié de l'entraîneur d'une lignée (CE-02) : distinct de celui de toute lignée."""
    return UID_BASE + 1000 + int(indice)


def traversable_par_tous(chemin: pathlib.Path) -> bool:
    """Vrai si chaque ancêtre de `chemin` (lui compris) laisse passer les autres utilisateurs (bit x « autres »)."""
    chemin = pathlib.Path(chemin).resolve()
    for p in [chemin] + list(chemin.parents):
        try:
            if not (p.stat().st_mode & 0o001):
                return False
        except OSError:
            return False
    return True


def espace_organismes(racine: pathlib.Path, course_nouvelle: bool = False) -> pathlib.Path:
    """Où vivent les dossiers de travail et la vue de l'archive : sous la racine si elle est traversable par les
    utilisateurs des organismes, sinon sous `/var/tmp/essaim-m3/<empreinte de la racine>` (0711, à root).
    `course_nouvelle` : la course démarre (pas de manifeste) ; un espace laissé par une course antérieure de même
    chemin est alors effacé (défaut signalé par session-depot, R-353 : `FileExistsError` dans `archive.deposer`)."""
    racine = pathlib.Path(racine).resolve()
    if traversable_par_tous(racine):
        return racine
    import hashlib as _h
    base = pathlib.Path("/var/tmp/essaim-m3")
    base.mkdir(parents=True, exist_ok=True)
    proteger(base, 0o711)
    esp = base / _h.sha256(str(racine).encode("utf-8")).hexdigest()[:16]
    if course_nouvelle and esp.exists():
        shutil.rmtree(esp, ignore_errors=True)
    esp.mkdir(exist_ok=True)
    proteger(esp, 0o711)
    return esp


def proteger(chemin: pathlib.Path, mode: int = 0o700) -> None:
    """Rend un chemin du noyau illisible pour les utilisateurs des organismes (sans effet si l'on n'est pas root)."""
    try:
        os.chmod(chemin, mode)
    except OSError:
        pass


def _changer_proprietaire(chemin: pathlib.Path, uid: int, gid: int, dossiers: int = 0o700, fichiers: int = 0o600) -> None:
    for p in [chemin] + list(chemin.rglob("*")):
        try:
            os.chown(p, uid, gid, follow_symlinks=False)
            if p.is_dir():
                os.chmod(p, dossiers)
            elif p.is_file():
                os.chmod(p, fichiers)
        except OSError:
            pass


def _limites(memoire_mo: int, cpu_s: int, fichier_mo: int, uid: int | None = None, gid: int | None = None):
    """Appliqué dans l'enfant juste avant `exec` : limites, nouvelle session, puis abandon des privilèges (dernier)."""
    def applique():
        os.setsid()
        try:
            resource.setrlimit(resource.RLIMIT_AS, (memoire_mo * 1024 * 1024, memoire_mo * 1024 * 1024))
        except (ValueError, OSError):
            os.write(2, b"[bac a sable] RLIMIT_AS non applique\n")
        resource.setrlimit(resource.RLIMIT_CPU, (cpu_s, cpu_s))
        resource.setrlimit(resource.RLIMIT_FSIZE, (fichier_mo * 1024 * 1024, fichier_mo * 1024 * 1024))
        resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
        resource.setrlimit(resource.RLIMIT_NPROC, (64, 64))
    return applique


def _tuer_groupe(proc) -> None:
    """Tue toute la session de processus de l'organisme (aucun processus détaché ne survit : CR-01)."""
    try:
        os.killpg(proc.pid, signal.SIGKILL)
    except (ProcessLookupError, PermissionError, OSError):
        pass


def _lancer(commande: list[str], cwd: pathlib.Path, env: dict, temps_max_s: int, sortie, erreurs, preexec) -> tuple[int | None, bool]:
    """Lance, attend au plus `temps_max_s`, tue le groupe entier en cas de délai ; rend (code de retour, délai dépassé)."""
    proc = subprocess.Popen(commande, cwd=str(cwd), env=env, stdout=sortie, stderr=erreurs, preexec_fn=preexec)
    try:
        code = proc.wait(timeout=temps_max_s)
        delai = False
    except subprocess.TimeoutExpired:
        _tuer_groupe(proc)
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            pass
        code, delai = None, True
    _tuer_groupe(proc)  # ce qui aurait été détaché pendant l'exécution meurt aussi
    return code, delai


def preparer(dossier_travail: pathlib.Path, organisme: pathlib.Path, contexte: dict, uid: int | None = None) -> pathlib.Path:
    """Copie l'organisme et le client dans le dossier de travail ; si `uid` est donné (isolation d'utilisateur), le
    dossier et l'organisme appartiennent à cet utilisateur, le client et le lanceur restent à root en lecture seule."""
    dossier_travail.mkdir(parents=True, exist_ok=True)
    cible = dossier_travail / "organisme"
    if cible.exists():
        shutil.rmtree(cible)
    shutil.copytree(organisme, cible, symlinks=False)
    (dossier_travail / "noyau_client.py").write_text(CLIENT_SOURCE, encoding="utf-8")
    (dossier_travail / "lanceur.py").write_text(LANCEUR_SOURCE, encoding="utf-8")
    chemin_ctx = dossier_travail / "contexte.json"
    chemin_ctx.write_text(json.dumps(contexte, ensure_ascii=False, indent=1), encoding="utf-8")
    if uid is not None:
        _changer_proprietaire(cible, uid, uid, dossiers=0o700, fichiers=0o600)
        try:
            os.chown(dossier_travail, uid, uid)
            os.chmod(dossier_travail, 0o700)
            for f in ("noyau_client.py", "lanceur.py", "contexte.json"):
                os.chown(dossier_travail / f, 0, 0)
                os.chmod(dossier_travail / f, 0o644)
        except OSError:
            pass
    return chemin_ctx


def _commande_isolee(commande: list[str], isoler_reseau: bool, uid: int | None, cwd: pathlib.Path) -> list[str]:
    """`unshare` (en root : espaces de noms de montage, de processus, de réseau), puis abaissement de privilèges vers
    `uid` par `abaisser.py` (écrit dans `cwd`, à root), puis la commande. Sans uid : seulement l'isolation réseau."""
    cap = capacites_isolation()
    options = []
    if uid is not None and cap["espaces_noms"]:
        options += ["--mount", "--pid", "--fork", "--kill-child", "--mount-proc"]
    if isoler_reseau:
        options += ["-n"] if cap["root"] else ["-rn"]
    if uid is not None:
        (cwd / "abaisser.py").write_text(ABAISSER_SOURCE, encoding="utf-8")
        try:
            os.chown(cwd / "abaisser.py", 0, 0)
            os.chmod(cwd / "abaisser.py", 0o644)
        except OSError:
            pass
        commande = [sys.executable, "-I", "-B", "-s", "abaisser.py", str(uid), str(uid)] + commande
    return (["unshare", *options, "--"] + commande) if options else commande


def executer(dossier_travail: pathlib.Path, chemin_socket: str, temps_max_s: int, memoire_mo: int = 2048,
             cpu_s: int | None = None, fichier_mo: int = 256, isoler_reseau: bool = False, uid: int | None = None) -> dict:
    """`uid` : utilisateur non privilégié sous lequel l'organisme tourne (None : même utilisateur que le noyau, simulation
    sans root seulement). Le dossier de travail doit avoir été préparé avec le même `uid`."""
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "HOME": str(dossier_travail),
           "PYTHONDONTWRITEBYTECODE": "1", "PYTHONIOENCODING": "utf-8", "TMPDIR": str(dossier_travail),
           "ESSAIM_SOCKET": chemin_socket, "ESSAIM_CONTEXTE": str(dossier_travail / "contexte.json")}
    commande = [sys.executable, "-I", "-B", "-s", "-u", "lanceur.py"]  # -B : aucun bytecode (``-I`` ignore PYTHONDONTWRITEBYTECODE)
    if isoler_reseau and not isolation_reseau_disponible():
        return {"code": "ISOLATION_INDISPONIBLE", "retour": None, "duree_s": 0.0, "delai_depasse": False, "uid": uid}
    commande = _commande_isolee(commande, isoler_reseau, uid, dossier_travail)
    debut = time.time()
    sortie = (dossier_travail / "sortie.txt").open("w", encoding="utf-8")
    erreurs = (dossier_travail / "erreurs.txt").open("w", encoding="utf-8")
    try:
        code_retour, delai = _lancer(commande, dossier_travail, env, temps_max_s, sortie, erreurs,
                                     _limites(memoire_mo, cpu_s or temps_max_s, fichier_mo, uid, uid))
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
    try:
        rlimit_as_refuse = "RLIMIT_AS non applique" in (dossier_travail / "erreurs.txt").read_text(encoding="utf-8", errors="replace")
    except OSError:
        rlimit_as_refuse = None
    return {"code": code, "code_retour": code_retour, "duree_s": round(duree, 2), "delai_depasse": delai,
            "statut": statut, "isolation_reseau": isoler_reseau, "uid": uid, "espaces_noms": bool(uid is not None and capacites_isolation()["espaces_noms"]),
            "rlimit_as_refuse": rlimit_as_refuse}


ABAISSER_SOURCE = """import os, sys
# Abandon des privilèges après `unshare` (qui exige root pour les espaces de noms) et juste avant l'organisme :
# groupes vidés, gid puis uid non privilégiés, puis exec du programme demandé. Écrit par le noyau, lecture seule.
uid, gid = int(sys.argv[1]), int(sys.argv[2])
os.setgroups([])
os.setgid(gid)
os.setuid(uid)
if os.getuid() != uid or os.geteuid() != uid:
    sys.exit("abaissement de privileges impossible")
os.execv(sys.argv[3], sys.argv[3:])
"""


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
                      memoire_mo: int = 1024, uid: int | None = None, isoler_reseau: bool = False) -> dict:
    """Exécute `metrique/calculer.py` d'un organisme sur une copie des sorties d'un autre, en bac à sable, sans socket,
    sous le même régime d'isolation qu'un organisme (utilisateur distinct, réseau coupé si demandé). Toute erreur, tout
    délai, toute valeur non finie vaut « non calculée » (jamais 0 ni 1 par défaut)."""
    dossier.mkdir(parents=True, exist_ok=True)
    if (dossier / "metrique").exists():
        shutil.rmtree(dossier / "metrique")
    if (dossier / "sorties").exists():
        shutil.rmtree(dossier / "sorties")
    from . import fichiers as _fichiers  # R-372 : copies de root sans suivre de lien de l'organisme
    if _fichiers.elements_non_ordinaires(metrique):
        return {"code": "METRIQUE_REFUSEE", "valeur": None, "calculee": False,
                "erreur": "métrique refusée : liens ou fichiers spéciaux (R-372) : " + "; ".join(_fichiers.elements_non_ordinaires(metrique)[:5])}
    _fichiers.copier_sans_liens(metrique, dossier / "metrique")
    _fichiers.copier_sans_liens(sorties, dossier / "sorties",
                                ignorer=("noyau", "juge", "noyau_client.py", "lanceur.py", "__pycache__", "contexte.json"))
    (dossier / "lanceur_metrique.py").write_text(LANCEUR_METRIQUE_SOURCE, encoding="utf-8")
    if uid is not None:
        _changer_proprietaire(dossier / "metrique", uid, uid)
        _changer_proprietaire(dossier / "sorties", uid, uid)
        try:
            os.chown(dossier, uid, uid)
            os.chmod(dossier, 0o700)
            os.chown(dossier / "lanceur_metrique.py", 0, 0)
            os.chmod(dossier / "lanceur_metrique.py", 0o644)
        except OSError:
            pass
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "HOME": str(dossier), "TMPDIR": str(dossier),
           "PYTHONDONTWRITEBYTECODE": "1", "PYTHONIOENCODING": "utf-8"}
    if isoler_reseau and not isolation_reseau_disponible():
        return {"code": "ISOLATION_INDISPONIBLE", "valeur": None, "calculee": False}
    commande = _commande_isolee([sys.executable, "-I", "-B", "-s", "-u", "lanceur_metrique.py"], isoler_reseau, uid, dossier)
    sortie = (dossier / "sortie.txt").open("w", encoding="utf-8")
    erreurs = (dossier / "erreurs.txt").open("w", encoding="utf-8")
    try:
        _, delai = _lancer(commande, dossier, env, temps_max_s, sortie, erreurs, _limites(memoire_mo, temps_max_s, 64, uid, uid))
    finally:
        sortie.close()
        erreurs.close()
    if delai:
        return {"code": "DELAI_DEPASSE", "valeur": None, "calculee": False}
    from . import fichiers as _fichiers
    donnees, raison = _fichiers.lire_fichier_organisme(dossier / "resultat_metrique.json", 200_000)
    if donnees is None:
        return ({"code": "SANS_RESULTAT", "valeur": None, "calculee": False} if raison == "absent"
                else {"code": "RESULTAT_REFUSE", "valeur": None, "calculee": False, "erreur": raison})
    try:
        r = json.loads(donnees.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return {"code": "RESULTAT_ILLISIBLE", "valeur": None, "calculee": False}
    if not isinstance(r, dict):
        return {"code": "RESULTAT_ILLISIBLE", "valeur": None, "calculee": False}
    v = r.get("valeur")
    ok = r.get("code") == "OK" and isinstance(v, (int, float)) and not isinstance(v, bool) and v == v and abs(v) != float("inf")
    return {"code": r.get("code"), "valeur": (float(v) if ok else None), "calculee": bool(ok), "erreur": r.get("erreur")}

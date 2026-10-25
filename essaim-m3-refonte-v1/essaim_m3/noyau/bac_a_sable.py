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
import stat
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


# RV-04 : l'espace des organismes et les sockets du noyau vivent hors des dossiers inscriptibles par tous (/tmp, /var/tmp,
# /dev/shm, /run/lock), que chaque exécution isolée recouvre d'un système de fichiers en mémoire qui lui est propre
ESPACE_BASE = pathlib.Path(os.environ.get("ESSAIM_M3_ESPACE") or "/var/lib/essaim-m3")
DOSSIERS_TMP_PARTAGES = ("/tmp", "/var/tmp", "/dev/shm", "/run/lock")
TAILLE_TMP_PRIVE = "64m"
# CL5-01 : dossiers à recouvrir d'un système de fichiers en mémoire **vide et en lecture seule** dans l'exécution isolée,
# pour qu'un organisme n'y lise ni le dépôt, ni l'arbre du code (qui porte la banque et ses vérités), ni les fichiers d'un
# compte ; la variable `ESSAIM_M3_CACHER` (le lanceur y met le dépôt et le dossier du code) s'y ajoute. Jamais un ancêtre
# du dossier de travail ni du socket (vérifié par `dossiers_a_cacher`).
DOSSIERS_A_CACHER_DEFAUT = ("/home", "/root", "/srv", "/mnt", "/media")
_INSCRIPTIBLES = None
MAX_DOSSIERS_BALAYES = 200_000
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
           "espaces_noms": root and _unshare_marche(["--mount", "--pid", "--ipc", "--fork", "--kill-child", "--mount-proc"])}
    _CAPACITES = cap
    return cap


def isolation_reseau_disponible() -> bool:
    return bool(capacites_isolation()["reseau"])


def uid_lignee(indice: int, decalage: int = 0) -> int:
    """Utilisateur non privilégié d'une lignée ; `decalage` (multiple de 100, CE3-06) distingue les courses qui tournent
    ensemble : la même lignée de deux courses n'a jamais le même utilisateur."""
    return UID_BASE + int(decalage) + int(indice)


def uid_entraineur(indice: int, decalage: int = 0) -> int:
    """Utilisateur non privilégié de l'entraîneur d'une lignée (CE-02) : distinct de celui de toute lignée (le décalage de
    course, au plus 900, reste sous 1000)."""
    return UID_BASE + 1000 + int(decalage) + int(indice)


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
    utilisateurs des organismes, sinon sous `ESPACE_BASE/<empreinte de la racine>` (0711, à root ; RV-04 : hors de
    /var/tmp, que chaque exécution isolée recouvre d'un dossier en mémoire privé).
    `course_nouvelle` : la course démarre (pas de manifeste) ; un espace laissé par une course antérieure de même
    chemin est alors effacé (défaut signalé par session-depot, R-353 : `FileExistsError` dans `archive.deposer`)."""
    racine = pathlib.Path(racine).resolve()
    if traversable_par_tous(racine):
        return racine
    import hashlib as _h
    base = ESPACE_BASE
    base.mkdir(parents=True, exist_ok=True)
    proteger(base, 0o711)
    esp = base / _h.sha256(str(racine).encode("utf-8")).hexdigest()[:16]
    if course_nouvelle and esp.exists():
        shutil.rmtree(esp, ignore_errors=True)
    esp.mkdir(exist_ok=True)
    proteger(esp, 0o711)
    return esp


def dossier_sockets() -> pathlib.Path:
    """Dossier court des sockets du noyau quand le dossier de travail donnerait un chemin trop long (limite des sockets
    Unix) : hors de /tmp (RV-04 : /tmp est privé dans l'exécution isolée), traversable sans se lister (0711)."""
    d = ESPACE_BASE / "s"
    d.mkdir(parents=True, exist_ok=True)
    proteger(ESPACE_BASE, 0o711)
    proteger(d, 0o711)
    return d


def dossiers_tmp_a_rendre_prives(gardes: list) -> list[str]:
    """RV-04 : dossiers inscriptibles par tous à recouvrir d'un système de fichiers en mémoire propre à l'exécution, sauf
    ceux qui contiennent un chemin qu'elle doit voir (dossier de travail, socket) : ceux-là restent partagés et sont
    consignés par l'appelant."""
    sortie = []
    for d in dossiers_inscriptibles_par_tous():
        p = pathlib.Path(d)
        try:
            if p.is_symlink() or not p.is_dir() or not (p.stat().st_mode & 0o002):
                continue
        except OSError:
            continue
        reel = p.resolve()
        if any(reel == pathlib.Path(g).resolve() or reel in pathlib.Path(g).resolve().parents for g in gardes):
            continue
        sortie.append(str(reel))
    return sortie


def dossiers_inscriptibles_par_tous(racines: tuple = ("/",), rafraichir: bool = False) -> list[str]:
    """CL5-02 : **tous** les dossiers inscriptibles par les autres (bit « autres » en écriture, collants compris) que
    l'exécution isolée doit recouvrir d'un dossier en mémoire privé, pas seulement les quatre dossiers temporaires
    habituels : un cinquième (par exemple `/var/lib/php/sessions`, 1733) serait sinon une voie commune entre deux bras.
    Balayage unique des systèmes de fichiers (coûté une fois par processus du noyau), bornes : jamais `/proc`, `/sys`,
    `/dev` (hors `/dev/shm`, déjà listé), ni l'espace des organismes ; au plus `MAX_DOSSIERS_BALAYES` dossiers visités
    (au-delà, on garde ce qui est trouvé — jamais moins que les quatre habituels, qui sont toujours inclus)."""
    global _INSCRIPTIBLES
    if _INSCRIPTIBLES is not None and not rafraichir and racines == ("/",):
        return _INSCRIPTIBLES
    trouves = {str(pathlib.Path(d).resolve()) for d in DOSSIERS_TMP_PARTAGES}
    exclure = {"/proc", "/sys", "/dev"}
    esp = str(ESPACE_BASE.resolve())
    visites = 0
    pile = [str(pathlib.Path(r).resolve()) for r in racines]
    while pile and visites < MAX_DOSSIERS_BALAYES:
        d = pile.pop()
        if d in exclure or d == esp or d.startswith(esp + "/"):
            continue
        try:
            with os.scandir(d) as it:
                for e in it:
                    try:
                        if e.is_symlink() or not e.is_dir(follow_symlinks=False):
                            continue
                        m = e.stat(follow_symlinks=False).st_mode
                    except OSError:
                        continue
                    visites += 1
                    if m & 0o002:
                        trouves.add(os.path.realpath(e.path))
                    pile.append(e.path)
        except OSError:
            continue
    resultat = sorted(trouves)
    if racines == ("/",):
        _INSCRIPTIBLES = resultat
    return resultat


def dossiers_a_cacher(gardes: list) -> list[str]:
    """CL5-01 : dossiers à recouvrir d'un système de fichiers en mémoire **vide et en lecture seule** dans l'exécution
    isolée (l'organisme n'y lit rien) : `DOSSIERS_A_CACHER_DEFAUT` et les chemins de `ESSAIM_M3_CACHER` (dépôt, code), sauf
    ceux qui contiennent un chemin que l'exécution doit voir (dossier de travail, socket) : on ne cache jamais un ancêtre
    d'une garde."""
    demandes = list(DOSSIERS_A_CACHER_DEFAUT) + [d for d in os.environ.get("ESSAIM_M3_CACHER", "").split(":") if d]
    gr = [pathlib.Path(g).resolve() for g in gardes]
    sortie = []
    vus = set()
    for d in demandes:
        p = pathlib.Path(d)
        try:
            if p.is_symlink() or not p.is_dir():
                continue
        except OSError:
            continue
        reel = p.resolve()
        if str(reel) in vus:
            continue
        if any(reel == g or reel in g.parents for g in gr):  # reel est le dossier de travail ou un de ses ancêtres : jamais caché
            continue
        vus.add(str(reel))
        sortie.append(str(reel))
    return sortie


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


def _commande_isolee(commande: list[str], isoler_reseau: bool, uid: int | None, cwd: pathlib.Path, gardes: tuple = ()) -> list[str]:
    """`unshare` (en root : espaces de noms de montage, de processus, de communication entre processus, de réseau), puis
    abaissement de privilèges vers `uid` par `abaisser.py` (écrit dans `cwd`, à root), qui recouvre d'abord /tmp, /var/tmp,
    /dev/shm et /run/lock d'un dossier en mémoire propre à cette exécution (RV-04 ; seulement dans l'espace de noms de
    montage neuf, jamais dans celui de l'hôte), puis la commande. Sans uid : seulement l'isolation réseau."""
    cap = capacites_isolation()
    options = []
    prives: list[str] = []
    caches: list[str] = []
    if uid is not None and cap["espaces_noms"]:
        options += ["--mount", "--pid", "--ipc", "--fork", "--kill-child", "--mount-proc"]
        prives = dossiers_tmp_a_rendre_prives([cwd, *gardes])   # CL5-02 : tout dossier inscriptible par tous, privé
        caches = dossiers_a_cacher([cwd, *gardes])              # CL5-01 : dépôt, code, /home… cachés (vide, lecture seule)
    if isoler_reseau:
        options += ["-n"] if cap["root"] else ["-rn"]
    if uid is not None:
        (cwd / "abaisser.py").write_text(ABAISSER_SOURCE, encoding="utf-8")
        try:
            os.chown(cwd / "abaisser.py", 0, 0)
            os.chmod(cwd / "abaisser.py", 0o644)
        except OSError:
            pass
        commande = [sys.executable, "-I", "-B", "-s", "abaisser.py", str(uid), str(uid),
                    ":".join(prives), ":".join(caches)] + commande
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
    commande = _commande_isolee(commande, isoler_reseau, uid, dossier_travail, gardes=(chemin_socket,))
    debut = time.time()
    # RV-05 : sortie et erreurs ouvertes par le noyau à neuf (jamais un lien), relues par ce même descripteur, jamais par leur nom
    sortie = open(dossier_travail / "sortie.txt", "x", encoding="utf-8")
    erreurs = open(dossier_travail / "erreurs.txt", "x+", encoding="utf-8")
    try:
        code_retour, delai = _lancer(commande, dossier_travail, env, temps_max_s, sortie, erreurs,
                                     _limites(memoire_mo, cpu_s or temps_max_s, fichier_mo, uid, uid))
        erreurs.flush()
        erreurs.seek(0)
        texte_erreurs = erreurs.read(1_000_000)
    finally:
        sortie.close()
        erreurs.close()
    duree = time.time() - debut
    # RV-05 : le statut écrit par le lanceur (dans le dossier de l'organisme) est lu sans suivre de lien, sans attendre sur un
    # tube, borné ; un refus est consigné, jamais lu
    from .fichiers import lire_fichier_organisme
    donnees_statut, raison_statut = lire_fichier_organisme(dossier_travail / "statut_execution.json", 200_000)
    statut = None
    if donnees_statut is not None:
        try:
            statut = json.loads(donnees_statut.decode("utf-8"))
            if not isinstance(statut, dict):
                statut = {"code": "STATUT_ILLISIBLE"}
        except (json.JSONDecodeError, UnicodeDecodeError):
            statut = {"code": "STATUT_ILLISIBLE"}
    elif raison_statut != "absent":
        statut = {"code": "STATUT_REFUSE", "raison": raison_statut}
    if delai:
        code = "DELAI_DEPASSE"
    elif statut is None:
        code = "SANS_STATUT"
    else:
        code = statut.get("code", "SANS_STATUT")
    rlimit_as_refuse = "RLIMIT_AS non applique" in texte_erreurs
    return {"code": code, "code_retour": code_retour, "duree_s": round(duree, 2), "delai_depasse": delai,
            "statut": statut, "isolation_reseau": isoler_reseau, "uid": uid, "espaces_noms": bool(uid is not None and capacites_isolation()["espaces_noms"]),
            "tmp_prives": (dossiers_tmp_a_rendre_prives([dossier_travail, chemin_socket]) if (uid is not None and capacites_isolation()["espaces_noms"]) else []),
            "caches": (dossiers_a_cacher([dossier_travail, chemin_socket]) if (uid is not None and capacites_isolation()["espaces_noms"]) else []),
            "rlimit_as_refuse": rlimit_as_refuse}


ABAISSER_SOURCE = """import ctypes, ctypes.util, os, sys
# Abandon des privilèges après `unshare` (qui exige root pour les espaces de noms) et juste avant l'organisme. D'abord
# (RV-04), dans l'espace de noms de montage neuf seulement : /tmp, /var/tmp, /dev/shm, /run/lock recouverts d'un système
# de fichiers en mémoire propre à cette exécution (rien n'y passe d'une exécution à l'autre) ; un échec arrête tout, rien
# ne tourne sans. Puis groupes vidés, gid puis uid non privilégiés, puis exec du programme demandé. Écrit par le noyau.
uid, gid = int(sys.argv[1]), int(sys.argv[2])
prives = [d for d in sys.argv[3].split(":") if d]
caches = [d for d in sys.argv[4].split(":") if d]
if prives or caches:
    libc = ctypes.CDLL(ctypes.util.find_library("c") or "libc.so.6", use_errno=True)
    # CL5-02 : dossiers inscriptibles par tous recouverts d'un systeme de fichiers en memoire propre a l'execution
    for d in prives:
        if libc.mount(b"tmpfs", d.encode(), b"tmpfs", 2 | 4, b"mode=1777,size=__TAILLE__") != 0:
            sys.exit("dossier temporaire prive impossible sur " + d + " (errno " + str(ctypes.get_errno()) + ")")
    # CL5-01 : depot, code et dossiers d'un compte recouverts d'un systeme vide en lecture seule (l'organisme n'y lit rien)
    MS_RDONLY = 1
    for d in caches:
        if libc.mount(b"vide", d.encode(), b"tmpfs", MS_RDONLY, b"mode=0000,size=4k") != 0:
            # errno 2 (absent) : un parent a deja ete couvert (par un dossier prive ou a cacher) ; le chemin est deja cache
            if ctypes.get_errno() == 2:
                continue
            sys.exit("dossier a cacher impossible sur " + d + " (errno " + str(ctypes.get_errno()) + ")")
os.setgroups([])
os.setgid(gid)
os.setuid(uid)
if os.getuid() != uid or os.geteuid() != uid:
    sys.exit("abaissement de privileges impossible")
os.execv(sys.argv[5], sys.argv[5:])
""".replace("__TAILLE__", TAILLE_TMP_PRIVE)


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

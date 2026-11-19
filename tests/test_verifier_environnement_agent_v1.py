"""Essais de `scripts/verifier_environnement_agent_v1.py` (pytest) — développeur, modèle L′.

Chaque contrôle est une fonction `verif_*(script, dossier)` qui lève AssertionError en cas d'écart :
  - les essais ordinaires l'appliquent au programme (cas sain et artefact de chaque refus et de chaque écart, R5) ;
  - le contrôle « trop beau » (R4) l'applique à des copies du programme où un défaut est réintroduit, et exige qu'elle échoue.
Le programme est appelé par son chemin, dans un sous-processus (`python3 -B -I`), comme le feront les agents. Certains contrôles
passent par un « espion » (fichier écrit dans le dossier temporaire de l'essai, lancé par son chemin) qui exécute le programme
par `runpy` sous un crochet d'audit : il journalise les processus lancés, les ouvertures de socket, les ouvertures de fichier en
écriture, et tout appel `os.stat`, `os.lstat`, `os.open`, `os.readlink`, `os.scandir`, `os.listdir`… qui nomme le segment
interdit. Les fichiers « interdits » des essais sont des tubes nommés : une ouverture en lecture bloquerait jusqu'au délai.
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "verifier_environnement_agent_v1.py"
SEG = "archives-reponses-modeles"
GIT = shutil.which("git")

ESPION = r'''"""Espion des essais (écrit par le fichier d'essais) : exécute le programme sous un crochet d'audit."""
import json, os, runpy, sys

journal, script, *args = sys.argv[1:]
SEG = "archives-reponses-modeles"
fd = os.open(journal, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
evenements = []
ECRITURE = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
PROCESSUS = ("os.system", "os.posix_spawn", "os.exec", "os.spawn", "os.fork", "os.forkpty", "pty.spawn", "os.startfile")


def texte(x):
    try:
        return os.fsdecode(x) if isinstance(x, (str, bytes, os.PathLike)) else repr(x)
    except Exception:
        return repr(x)


def nomme_segment(args):
    return any(SEG in texte(x).casefold() for x in args)


def crochet(ev, a):
    if ev == "subprocess.Popen":
        argv = a[1] if isinstance(a[1], (list, tuple)) else [a[1]]
        evenements.append({"type": "processus", "argv": [texte(x) for x in argv]})
        return
    if ev in PROCESSUS:
        evenements.append({"type": "processus", "argv": [texte(x) for x in a], "evenement": ev})
    elif ev.startswith("socket."):
        evenements.append({"type": "reseau", "evenement": ev})
    elif ev == "open":
        chemin, mode, drapeaux = (list(a) + [None, None, None])[:3]
        if isinstance(chemin, int):
            return  # descripteur déjà ouvert (tube de subprocess), pas un chemin
        ecrit = bool(mode and any(c in str(mode) for c in "wxa+")) or bool(isinstance(drapeaux, int) and drapeaux & ECRITURE)
        evenements.append({"type": "ouverture", "chemin": texte(chemin), "ecriture": ecrit})
    if (ev == "open" or ev.startswith(("os.", "shutil.", "glob."))) and nomme_segment(a):
        evenements.append({"type": "segment", "evenement": ev, "args": [texte(x) for x in a]})


def espionner(nom):
    orig = getattr(os, nom)

    def f(*a, **k):
        if nomme_segment(a):
            evenements.append({"type": "segment", "evenement": "os." + nom, "args": [texte(x) for x in a]})
        return orig(*a, **k)
    setattr(os, nom, f)


for nom in ("stat", "lstat", "open", "readlink", "scandir", "listdir", "access", "utime", "chmod", "unlink", "remove",
            "rename", "replace", "mkdir", "rmdir", "mkfifo"):
    if hasattr(os, nom):
        espionner(nom)
sys.addaudithook(crochet)
sys.argv = [script, *args]
code = 0
try:
    runpy.run_path(script, run_name="__main__")
except SystemExit as e:
    code = e.code if isinstance(e.code, int) else (0 if e.code is None else 1)
finally:
    donnees = json.dumps(evenements, ensure_ascii=False).encode("utf-8")
    while donnees:
        donnees = donnees[os.write(fd, donnees):]
    os.close(fd)
sys.exit(code)
'''


# ---------------------------------------------------------------------------------------------------------------- outillage

def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def lancer(script: Path, *args, cwd=None, env=None, isole=True) -> subprocess.CompletedProcess:
    cmd = [sys.executable, "-B", *(["-I"] if isole else []), str(script), *[str(a) for a in args]]
    return subprocess.run(cmd, capture_output=True, timeout=60, cwd=cwd, env=env)


def lancer_espion(script: Path, dossier: Path, *args, cwd=None):
    dossier.mkdir(parents=True, exist_ok=True)
    espion = dossier / "espion_essai.py"
    if not espion.exists():
        espion.write_text(ESPION, encoding="utf-8")
    journal = dossier / f"journal-espion-{len(list(dossier.glob('journal-espion-*')))}.json"
    r = subprocess.run([sys.executable, "-B", "-I", str(espion), str(journal), str(script), *[str(a) for a in args]],
                       capture_output=True, timeout=60, cwd=cwd)
    evenements = json.loads(journal.read_text(encoding="utf-8")) if journal.exists() else None
    assert evenements is not None, ("journal de l'espion absent", r.returncode, r.stderr.decode(errors="replace")[-3000:])
    return r, evenements


def erreur(r) -> str:
    return r.stderr.decode("utf-8", errors="replace")[-3000:]


def code(r, attendu: int) -> None:
    assert r.returncode == attendu, (r.returncode, attendu, erreur(r))


def rapport(r) -> dict:
    try:
        return json.loads(r.stdout.decode("utf-8"))
    except ValueError as e:
        raise AssertionError(f"sortie standard qui n'est pas un JSON : {e} ; {r.stdout[:300]!r}") from None


def segments(evenements) -> list:
    return [e for e in evenements if e["type"] == "segment"]


def git_essai(repo: Path, *args) -> str:
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update({"GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull, "LC_ALL": "C"})
    p = subprocess.run([GIT, "-c", "user.name=essai", "-c", "user.email=essai@exemple.invalid", "-c", "commit.gpgsign=false",
                        "-c", "init.defaultBranch=principale", "-C", str(repo), *args],
                       capture_output=True, timeout=60, env=env)
    assert p.returncode == 0, (args, p.stderr)
    return p.stdout.decode("utf-8")


def depot_essai(dossier: Path) -> Path:
    if GIT is None:
        pytest.skip("git absent")
    repo = dossier / "depot"
    repo.mkdir(parents=True)
    git_essai(repo, "init", "-q")
    (repo / "suivi.txt").write_bytes(b"un\n")
    git_essai(repo, "add", "suivi.txt")
    git_essai(repo, "commit", "-q", "-m", "premier")
    return repo


def instantane(dossier: Path) -> dict:
    return {str(p.relative_to(dossier)): sha(p.read_bytes()) for p in sorted(dossier.rglob("*")) if p.is_file()}


def hors_de_tout_depot(p: Path) -> bool:
    return not any((q / ".git").exists() for q in [p, *p.parents])


# -------------------------------------------------------------------------------------------------------------- cas sains

def verif_sain_base(script, d):
    d.mkdir(parents=True, exist_ok=True)
    r = lancer(script, cwd=d)
    code(r, 0)
    j = rapport(r)
    assert j["statut"] == "lu" and j["code_retour"] == 0, j
    assert j["programme_sha256"] == sha(Path(script).read_bytes())
    assert j["python"]["version"] == platform.python_version()
    assert j["python"]["executable"] == sys.executable
    assert j["python"]["drapeaux"]["ne_pas_ecrire_bytecode"] is True and j["python"]["drapeaux"]["isole"] is True
    assert j["plateforme"]["sys_platform"] == sys.platform and j["plateforme"]["machine"] == platform.machine()
    assert re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", j["heure_utc"]), j["heure_utc"]
    h = datetime.datetime.strptime(j["heure_utc"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
    assert abs((datetime.datetime.now(datetime.timezone.utc) - h).total_seconds()) < 600
    assert j["repertoire_courant"] == str(d.resolve())
    assert j["modules"] is None and j["empreintes"] is None and j["depot"] is None and j["fichier_sortie"] is None
    assert j["anomalies"] == []
    assert r.stderr == b"", erreur(r)


def verif_sain_modules(script, d):
    import json as module_json
    r = lancer(script, "--modules", "json,hashlib,os.path")
    code(r, 0)
    m = rapport(r)["modules"]
    assert [x["nom"] for x in m] == ["json", "hashlib", "os.path"]
    assert all(x["statut"] == "present" and x["erreur"] is None for x in m), m
    assert m[0]["version"] == module_json.__version__ and m[0]["source_version"] == "__version__", m[0]
    assert m[0]["fichier"] == module_json.__file__
    assert m[1]["version"] is None and m[1]["source_version"] is None, m[1]


def verif_sain_module_absent(script, d):
    r = lancer(script, "--modules", "module_inexistant_essai_v1,json,json.inexistant_essai_v1")
    code(r, 0)
    m = rapport(r)["modules"]
    assert [x["statut"] for x in m] == ["absent", "present", "absent"], m
    assert m[0]["erreur"] is None and m[0]["version"] is None
    assert b"Traceback" not in r.stderr, erreur(r)


def verif_sain_module_erreur_import(script, d):
    mods = d / "mods"
    mods.mkdir(parents=True)
    (mods / "casse_essai_v1.py").write_text('raise RuntimeError("cassé exprès")\n', encoding="utf-8")
    (mods / "bavard_essai_v1.py").write_text('print("bruit à l\'import")\n__version__ = "9.9"\n', encoding="utf-8")
    (mods / "sortie_essai_v1.py").write_text("raise SystemExit(5)\n", encoding="utf-8")
    (mods / "dependance_essai_v1.py").write_text("import module_inexistant_dependance_v1\n", encoding="utf-8")
    env = dict(os.environ, PYTHONPATH=str(mods))
    r = lancer(script, "--modules", "casse_essai_v1,bavard_essai_v1,sortie_essai_v1,dependance_essai_v1",
               env=env, isole=False)
    code(r, 0)
    j = rapport(r)  # le JSON reste lisible malgré le module bavard
    m = {x["nom"]: x for x in j["modules"]}
    assert m["casse_essai_v1"]["statut"] == "erreur_import" and "RuntimeError" in m["casse_essai_v1"]["erreur"]
    assert m["bavard_essai_v1"]["statut"] == "present" and m["bavard_essai_v1"]["version"] == "9.9"
    assert m["bavard_essai_v1"]["caracteres_ecrits_sur_sortie_standard_a_l_import"] > 0
    assert m["sortie_essai_v1"]["statut"] == "erreur_import" and "SystemExit" in m["sortie_essai_v1"]["erreur"]
    assert m["dependance_essai_v1"]["statut"] == "erreur_import", m["dependance_essai_v1"]
    assert "module_inexistant_dependance_v1" in m["dependance_essai_v1"]["erreur"]
    assert len(j["anomalies"]) == 3, j["anomalies"]


def poser_fichiers(d: Path) -> dict:
    d.mkdir(parents=True, exist_ok=True)
    (d / "sous").mkdir(exist_ok=True)
    f = {"a": (d / "a.txt", b"alpha\n"), "b": (d / "sous" / "b.bin", b"\x00\r\nbeta\xff"), "vide": (d / "vide.txt", b"")}
    for p, c in f.values():
        p.write_bytes(c)
    return f


def verif_sain_empreintes(script, d):
    f = poser_fichiers(d)
    liste = d / "liste.txt"
    liste.write_text("\n".join([
        f"{sha(f['a'][1])}  a.txt",
        f"{sha(f['b'][1]).upper()} *sous/b.bin",
        "vide.txt",
        "absent.txt",
        "sous",
        "# commentaire",
        "",
        "  ",
        f"{d / 'a.txt'}\r",
    ]) + "\n", encoding="utf-8")
    r = lancer(script, "--empreintes", Path(d.name) / "liste.txt", cwd=d.parent)  # chemins relatifs au dossier de la liste
    code(r, 0)
    e = rapport(r)["empreintes"]
    assert e["liste_sha256"] == sha(liste.read_bytes()) and e["base_des_chemins_relatifs"] == str(d.resolve())
    x = e["fichiers"]
    assert [y["ligne"] for y in x] == [1, 2, 3, 4, 5, 9], x
    assert x[0]["existe"] and x[0]["type"] == "fichier" and x[0]["taille"] == 6 and x[0]["sha256"] == sha(b"alpha\n")
    assert x[0]["egal_attendu"] is True and x[1]["egal_attendu"] is True and x[1]["taille"] == len(f["b"][1])
    assert x[1]["empreinte_attendue"] == sha(f["b"][1])
    assert x[2]["sha256"] == sha(b"") and x[2]["taille"] == 0 and x[2]["egal_attendu"] is None
    assert x[3]["existe"] is False and x[3]["sha256"] is None and x[3]["egal_attendu"] is None
    assert x[4]["type"] == "dossier" and x[4]["sha256"] is None
    assert x[5]["chemin_resolu"] == str((d / "a.txt").resolve()) and x[5]["sha256"] == sha(b"alpha\n")
    assert e["ecarts"] == [] and len(rapport(r)["anomalies"]) == 2, rapport(r)["anomalies"]


def verif_sain_compagnon_comme_liste(script, d):
    d.mkdir(parents=True)
    (d / "outil.py").write_bytes(b"print(1)\n")
    (d / "outil.py.sha256").write_text(f"{sha(b'print(1)' + bytes([10]))}  outil.py\n", encoding="utf-8")
    r = lancer(script, "--empreintes", d / "outil.py.sha256")
    code(r, 0)
    x = rapport(r)["empreintes"]["fichiers"]
    assert len(x) == 1 and x[0]["egal_attendu"] is True, x


def verif_sain_sortie(script, d):
    d.mkdir(parents=True)
    s = d / "rapport.json"
    r = lancer(script, "--sortie", s, "--modules", "json")
    code(r, 0)
    octets = s.read_bytes()
    assert octets == r.stdout, "le fichier de sortie diffère de la sortie standard"
    assert Path(str(s) + ".sha256").read_bytes() == f"{sha(octets)}  rapport.json\n".encode()
    assert json.loads(octets)["fichier_sortie"] == str(s.resolve())
    assert sorted(p.name for p in d.iterdir()) == ["rapport.json", "rapport.json.sha256"]


def verif_sain_depot_git(script, d):
    repo = depot_essai(d)
    r = lancer(script, "--depot", repo)
    code(r, 0)
    g = rapport(r)["depot"]
    assert g["est_depot_git"] is True and g["erreurs"] == [], g
    assert g["tete"] == git_essai(repo, "rev-parse", "HEAD").strip()
    assert g["branche"] == "principale" and g["tete_detachee"] is False
    assert g["arbre_propre"] is True and g["lignes_status"] == [] and g["racine"] == str(repo.resolve())
    (repo / "nouveau.txt").write_bytes(b"x")
    (repo / "suivi.txt").write_bytes(b"deux\n")
    g = rapport(lancer(script, "--depot", repo))["depot"]
    assert g["arbre_propre"] is False and sorted(g["lignes_status"]) == [" M suivi.txt", "?? nouveau.txt"], g
    git_essai(repo, "checkout", "-q", "--detach")
    g = rapport(lancer(script, "--depot", repo / "."))["depot"]
    assert g["branche"] is None and g["tete_detachee"] is True and g["tete"] is not None, g


def verif_sain_depot_sans_commit(script, d):
    if GIT is None:
        pytest.skip("git absent")
    repo = d / "vide"
    repo.mkdir(parents=True)
    git_essai(repo, "init", "-q")
    r = lancer(script, "--depot", repo)
    code(r, 0)
    g = rapport(r)["depot"]
    assert g["est_depot_git"] is True and g["tete"] is None and g["branche"] == "principale", g
    assert any("tête" in m for m in g["erreurs"]) and g["arbre_propre"] is True


def verif_sain_status_exclut_archives(script, d):
    repo = depot_essai(d)
    (repo / SEG).mkdir()
    (repo / SEG / "suivi_archive.txt").write_bytes(b"a\n")
    git_essai(repo, "add", f"{SEG}/suivi_archive.txt")
    git_essai(repo, "commit", "-q", "-m", "archive")
    (repo / SEG / "suivi_archive.txt").write_bytes(b"b\n")                    # suivi, modifié
    (repo / SEG / "non_suivi.txt").write_bytes(b"c\n")                        # non suivi
    (repo / "docs" / f"{SEG}-v2").mkdir(parents=True)
    (repo / "docs" / f"{SEG}-v2" / "y.txt").write_bytes(b"d\n")
    (repo / "Archives-Reponses-Modeles").mkdir()
    (repo / "Archives-Reponses-Modeles" / "z.txt").write_bytes(b"e\n")
    g = rapport(lancer(script, "--depot", repo))["depot"]
    assert g["arbre_propre"] is True and g["lignes_status"] == [], g
    assert all(SEG in p.casefold() for p in g["pathspecs_status"][1:])
    (repo / "autre.txt").write_bytes(b"f\n")
    g = rapport(lancer(script, "--depot", repo))["depot"]
    assert g["arbre_propre"] is False and g["lignes_status"] == ["?? autre.txt"], g


def verif_sain_depot_sans_ecriture(script, d):
    repo = depot_essai(d)
    st = (repo / "suivi.txt").stat()
    os.utime(repo / "suivi.txt", ns=(st.st_atime_ns, st.st_mtime_ns + 7_000_000_000))  # index périmé : git voudrait l'écrire
    avant = instantane(repo / ".git")
    r = lancer(script, "--depot", repo)
    code(r, 0)
    assert rapport(r)["depot"]["arbre_propre"] is True
    assert instantane(repo / ".git") == avant, "git a écrit dans .git"


def verif_sain_processus_seul_git(script, d):
    repo = depot_essai(d)
    f = poser_fichiers(d / "fichiers")
    liste = d / "liste.txt"
    liste.write_text(f"{sha(f['a'][1])}  fichiers/a.txt\nfichiers/sous/b.bin\n", encoding="utf-8")
    s = d / "sortie.json"
    r, ev = lancer_espion(script, d / "espion", "--depot", repo, "--modules", "json,hashlib", "--empreintes", liste,
                          "--sortie", s)
    code(r, 0)
    procs = [e for e in ev if e["type"] == "processus"]
    assert procs and all(os.path.basename(e["argv"][0]) == "git" for e in procs), procs
    assert all(e["argv"][1:3] == ["--no-pager", "--no-optional-locks"] for e in procs), procs
    assert not [e for e in ev if e["type"] == "reseau"]
    ecritures = {e["chemin"] for e in ev if e["type"] == "ouverture" and e["ecriture"]}
    assert ecritures == {str(s.resolve()), str(s.resolve()) + ".sha256"}, ecritures
    assert rapport(r)["depot"]["arbre_propre"] is True


# ------------------------------------------------------------------------------------------------- artefacts : segment interdit

def poser_archive(d: Path, nom: str = SEG) -> Path:
    arch = d / nom
    arch.mkdir(parents=True)
    os.mkfifo(arch / "fichier")  # une ouverture en lecture bloquerait
    return arch


def attendre_refus_segment(r, ev, n: int, propres=()):
    code(r, 2)
    msg = erreur(r)
    assert msg.count("REFUS :") == n and SEG in msg and "sans y accéder" in msg, msg
    j = rapport(r)
    assert j["statut"] == "refus" and len(j["refus"]) == n, j
    assert not segments(ev), segments(ev)
    assert not [e for e in ev if e["type"] == "ouverture" and SEG in e["chemin"].casefold()]
    for p in propres:
        assert not [e for e in ev if e["type"] == "ouverture" and e["chemin"] == str(p)], f"{p} lu malgré le refus"


def verif_refus_archives_dans_liste(script, d):
    arch = poser_archive(d)
    (d / "propre.txt").write_bytes(b"propre\n")
    liste = d / "liste.txt"
    liste.write_text(f"propre.txt\n{SEG}/fichier\n{arch / 'fichier'}\n{'0' * 64}  sous/../{SEG}/fichier\n", encoding="utf-8")
    s = d / "rapport.json"
    r, ev = lancer_espion(script, d / "espion", "--empreintes", liste, "--sortie", s)
    attendre_refus_segment(r, ev, 3, propres=[(d / "propre.txt").resolve()])
    assert not os.path.lexists(s) and not os.path.lexists(str(s) + ".sha256")


def verif_refus_archives_par_lien(script, d):
    arch = poser_archive(d)
    d2 = d / "liens"
    d2.mkdir()
    os.symlink(arch / "fichier", d2 / "lien_fichier")
    os.symlink(arch, d2 / "lien_dossier")
    os.symlink(arch / "fichier", d2 / "l2")
    os.symlink("l2", d2 / "l1")
    liste = d2 / "liste.txt"
    liste.write_text("lien_fichier\nlien_dossier/fichier\nl1\n", encoding="utf-8")
    r, ev = lancer_espion(script, d / "espion", "--empreintes", liste)
    attendre_refus_segment(r, ev, 3)


def verif_refus_archives_casse(script, d):
    poser_archive(d, "Archives-Reponses-Modeles")
    liste = d / "liste.txt"
    liste.write_text("Archives-Reponses-Modeles/fichier\n", encoding="utf-8")
    r, ev = lancer_espion(script, d / "espion", "--empreintes", liste)
    attendre_refus_segment(r, ev, 1)


def verif_refus_archives_options(script, d):
    arch = poser_archive(d)
    os.mkfifo(arch / "liste.txt")
    s = arch / "rapport.json"
    r, ev = lancer_espion(script, d / "espion", "--empreintes", arch / "liste.txt", "--depot", arch, "--sortie", s)
    attendre_refus_segment(r, ev, 3)
    assert not os.path.lexists(s) and not os.path.lexists(str(s) + ".sha256")


# ------------------------------------------------------------------------------------------------------ artefacts : écarts

def verif_ecart_empreinte_code3(script, d):
    f = poser_fichiers(d)
    liste = d / "liste.txt"
    liste.write_text(f"{sha(b'autre')}  a.txt\n{sha(f['b'][1])}  sous/b.bin\n", encoding="utf-8")
    s = d / "rapport.json"
    r = lancer(script, "--empreintes", liste, "--sortie", s)
    code(r, 3)
    j = rapport(r)
    x = j["empreintes"]["fichiers"]
    assert j["statut"] == "ecart" and j["code_retour"] == 3
    assert x[0]["egal_attendu"] is False and x[0]["sha256"] == sha(b"alpha\n") and x[1]["egal_attendu"] is True
    assert [c["ligne"] for c in j["empreintes"]["ecarts"]] == [1]
    assert "ECART :" in erreur(r) and "a.txt" in erreur(r)
    assert s.read_bytes() == r.stdout  # le rapport est gardé


def verif_ecart_absent_avec_empreinte(script, d):
    d.mkdir(parents=True)
    liste = d / "liste.txt"
    liste.write_text(f"{sha(b'x')}  absent.txt\n", encoding="utf-8")
    r = lancer(script, "--empreintes", liste)
    code(r, 3)
    x = rapport(r)["empreintes"]["fichiers"][0]
    assert x["existe"] is False and x["egal_attendu"] is False, x


def verif_ecart_dossier_avec_empreinte(script, d):
    (d / "sous").mkdir(parents=True)
    liste = d / "liste.txt"
    liste.write_text(f"{sha(b'x')}  sous\n", encoding="utf-8")
    r = lancer(script, "--empreintes", liste)
    code(r, 3)
    assert rapport(r)["empreintes"]["fichiers"][0]["type"] == "dossier"


# ------------------------------------------------------------------------------------------ artefacts : sortie et dépôt

def verif_refus_sortie_existe(script, d):
    d.mkdir(parents=True)
    s = d / "r.json"
    s.write_bytes(b"ancien")
    r = lancer(script, "--sortie", s)
    code(r, 2)
    assert "existe déjà" in erreur(r) and rapport(r)["statut"] == "refus"
    assert s.read_bytes() == b"ancien" and not os.path.lexists(str(s) + ".sha256")


def verif_refus_compagnon_existe(script, d):
    d.mkdir(parents=True)
    s = d / "r.json"
    Path(str(s) + ".sha256").write_bytes(b"ancien")
    r = lancer(script, "--sortie", s)
    code(r, 2)
    assert not os.path.lexists(s) and Path(str(s) + ".sha256").read_bytes() == b"ancien"


def verif_refus_sortie_lien_pendant(script, d):
    d.mkdir(parents=True)
    s = d / "r.json"
    os.symlink(d / "cible_inexistante.json", s)
    r = lancer(script, "--sortie", s)
    code(r, 2)
    assert not os.path.lexists(d / "cible_inexistante.json")


def verif_refus_dossier_sortie_absent(script, d):
    d.mkdir(parents=True)
    r = lancer(script, "--sortie", d / "absent" / "r.json")
    code(r, 2)
    assert "absent" in erreur(r)


def verif_depot_non_git(script, d):
    p = d / "pas_git"
    p.mkdir(parents=True)
    assert hors_de_tout_depot(p.resolve()), "précondition : le dossier temporaire est dans un dépôt"
    r = lancer(script, "--depot", p)
    code(r, 0)
    g = rapport(r)["depot"]
    assert g["est_depot_git"] is False and g["tete"] is None and g["arbre_propre"] is None and g["erreurs"], g
    assert b"Traceback" not in r.stderr


def verif_refus_depot_absent(script, d):
    d.mkdir(parents=True)
    (d / "fichier").write_bytes(b"x")
    for p in (d / "inexistant", d / "fichier"):
        r = lancer(script, "--depot", p)
        code(r, 2)
        assert rapport(r)["statut"] == "refus"


# -------------------------------------------------------------------------------------------- artefacts : entrées invalides

def verif_refus_liste_lignes_invalides(script, d):
    d.mkdir(parents=True)
    (d / "ok.txt").write_bytes(b"x")
    liste = d / "liste.txt"
    liste.write_text(f"{'a' * 64} x\n{'b' * 64}\n espace.txt\nok.txt\n{'c' * 64}  \\echappe\n", encoding="utf-8")
    r, ev = lancer_espion(script, d / "espion", "--empreintes", liste)
    code(r, 2)
    assert erreur(r).count("REFUS :") == 4, erreur(r)
    for n in (1, 2, 3, 5):
        assert f"ligne {n} " in erreur(r)
    assert not [e for e in ev if e["type"] == "ouverture" and e["chemin"] == str((d / "ok.txt").resolve())]


def verif_refus_liste_fautive(script, d):
    d.mkdir(parents=True)
    (d / "non_utf8.txt").write_bytes(b"a\xff\n")
    (d / "vide.txt").write_bytes(b"# rien\n\n")
    (d / "bom.txt").write_bytes(b"\xef\xbb\xbfa.txt\n")
    os.mkfifo(d / "tube")
    for nom, motif in (("absente.txt", "absent"), ("non_utf8.txt", "UTF-8"), ("vide.txt", "aucun chemin"),
                       ("bom.txt", "marque d'ordre"), ("tube", "pas un fichier ordinaire")):
        r = lancer(script, "--empreintes", d / nom)
        code(r, 2)
        assert motif in erreur(r), (nom, erreur(r))


def verif_refus_modules_invalides(script, d):
    for valeur in ("json;rm", "json,,os", "", "../json", "json, os", "1abc"):
        r = lancer(script, f"--modules={valeur}")
        code(r, 2)
        assert "nom(s) de module invalide(s)" in erreur(r), (valeur, erreur(r))


def verif_refus_options(script, d):
    for args in (["--empre", "x"], ["--inconnue"], ["--sortie"]):
        r = lancer(script, *args)
        code(r, 2)


SAINS = [verif_sain_base, verif_sain_modules, verif_sain_module_absent, verif_sain_module_erreur_import,
         verif_sain_empreintes, verif_sain_compagnon_comme_liste, verif_sain_sortie, verif_sain_depot_git,
         verif_sain_depot_sans_commit, verif_sain_status_exclut_archives, verif_sain_depot_sans_ecriture,
         verif_sain_processus_seul_git]
ARTEFACTS = [verif_refus_archives_dans_liste, verif_refus_archives_par_lien, verif_refus_archives_casse,
             verif_refus_archives_options, verif_ecart_empreinte_code3, verif_ecart_absent_avec_empreinte,
             verif_ecart_dossier_avec_empreinte, verif_refus_sortie_existe, verif_refus_compagnon_existe,
             verif_refus_sortie_lien_pendant, verif_refus_dossier_sortie_absent, verif_depot_non_git,
             verif_refus_depot_absent, verif_refus_liste_lignes_invalides, verif_refus_liste_fautive,
             verif_refus_modules_invalides, verif_refus_options]


# ---------------------------------------------------------------------------------------------------------------- essais

@pytest.mark.parametrize("verif", SAINS + ARTEFACTS, ids=lambda f: f.__name__)
def test_programme(verif, tmp_path):
    verif(SCRIPT, tmp_path / "essai")


def test_code_seul_en_bibliotheque_standard():
    """Bibliothèque standard seulement ; un seul point de lancement de processus, sans shell ; aucun réseau."""
    src = SCRIPT.read_text(encoding="utf-8")
    code_seul = src.split('"""', 2)[2]  # sans la docstring du module
    imports = {l.split()[1].split(".")[0] for l in src.splitlines() if l.startswith(("import ", "from "))}
    assert imports <= set(sys.stdlib_module_names) | {"__future__"}, imports
    assert src.count("subprocess.run(") == 1 and "shell=False" in src and "shell=True" not in src
    for interdit in ("os.system", "Popen", "socket", "urllib", "http.client", "platform.platform(", "processor(",
                     "check_output", "os.popen"):
        assert interdit not in code_seul, interdit


# ------------------------------------------------------------------------------------- contrôle « trop beau » (R4)
# Chaque défaut est réintroduit dans une copie du programme ; le contrôle nommé doit le voir (échouer sur la copie).

MUTATIONS = [
    ("controle_du_segment_retire",
     [("    return SEGMENT_INTERDIT in os.fsdecode(chemin).casefold()\n", "    return False\n")],
     verif_refus_archives_dans_liste),
    ("segment_sensible_a_la_casse",
     [("    return SEGMENT_INTERDIT in os.fsdecode(chemin).casefold()\n",
       "    return SEGMENT_INTERDIT in os.fsdecode(chemin)\n")], verif_refus_archives_casse),
    ("liens_suivis_sans_controle",
     [("    pile = list(reversed(depart.split(os.sep)))\n",
       "    return os.path.realpath(depart)\n    pile = list(reversed(depart.split(os.sep)))\n")],
     verif_refus_archives_par_lien),
    ("realpath_puis_controle",
     [("    pile = list(reversed(depart.split(os.sep)))\n",
       "    _r = os.path.realpath(depart)\n    if contient_segment(_r):\n        raise Refus(motif_segment(role, chemin))\n"
       "    return _r\n    pile = list(reversed(depart.split(os.sep)))\n")], verif_refus_archives_par_lien),
    ("empreinte_differente_ignoree", [("    code = CODE_ECART if ecarts else CODE_LU\n", "    code = CODE_LU\n")],
     verif_ecart_empreinte_code3),
    ("fichier_absent_non_compte",
     [('        r["egal_attendu"] = r["sha256"] == e["attendu"]\n',
       '        r["egal_attendu"] = None if r["sha256"] is None else r["sha256"] == e["attendu"]\n')],
     verif_ecart_absent_avec_empreinte),
    ("sortie_existante_reecrite",
     [("        if os.path.lexists(p):\n", "        if False:\n"), ('with open(p, "xb")', 'with open(p, "wb")')],
     verif_refus_sortie_existe),
    ("import_non_protege",
     [("    except ModuleNotFoundError as e:\n", "    except ImportWarning as e:\n"),
      ("    except (Exception, SystemExit) as e:\n", "    except SystemExit as e:\n")], verif_sain_module_absent),
    ("sortie_standard_non_protegee_a_l_import",
     [("        with contextlib.redirect_stdout(tampon):\n", "        with contextlib.nullcontext():\n")],
     verif_sain_module_erreur_import),
    ("depot_non_git_en_faute", [('        r["est_depot_git"] = False\n', '        raise Refus(d["erreur"])\n')], verif_depot_non_git),
    ("plateforme_par_platform_platform",
     [('        "sys_platform": sys.platform,\n',
       '        "sys_platform": sys.platform,\n        "description": platform.platform(),\n')],
     verif_sain_processus_seul_git),
    ("git_par_le_shell",
     [("subprocess.run(cmd, input", "subprocess.run(' '.join(cmd), input"), ("shell=False, check", "shell=True, check")],
     verif_sain_processus_seul_git),
    ("verrous_optionnels_gardes",
     [('OPTIONS_GIT = ("--no-pager", "--no-optional-locks", ', 'OPTIONS_GIT = ("--no-pager", '),
      ('"GIT_OPTIONAL_LOCKS": "0", ', '')], verif_sain_depot_sans_ecriture),
    ("status_sans_exclusion",
     [('"--", ":/", *EXCLUSIONS_STATUS)', '"--", ":/")')], verif_sain_status_exclut_archives),
    ("compagnon_au_chemin_complet",
     [('f"{sha256_octets(octets)}  {os.path.basename(chemin)}\\n"', 'f"{sha256_octets(octets)}  {chemin}\\n"')],
     verif_sain_sortie),
    ("ligne_mal_separee_acceptee",
     [("        elif RE_DEBUT_SHA.match(ligne):\n", "        elif False:\n")], verif_refus_liste_lignes_invalides),
]


@pytest.mark.parametrize("nom, edits, verif", MUTATIONS, ids=[m[0] for m in MUTATIONS])
def test_trop_beau_defaut_reintroduit_vu(nom, edits, verif, tmp_path):
    src = SCRIPT.read_text(encoding="utf-8")
    for ancien, neuf in edits:
        assert src.count(ancien) == 1, (nom, ancien)
        src = src.replace(ancien, neuf)
    mutant = tmp_path / "mutant" / SCRIPT.name
    mutant.parent.mkdir()
    mutant.write_text(src, encoding="utf-8")
    compile(src, str(mutant), "exec")
    verif(SCRIPT, tmp_path / "temoin")          # le contrôle passe sur le programme…
    with pytest.raises(AssertionError):         # … et échoue sur la copie défectueuse
        verif(mutant, tmp_path / "essai")

"""Essai 06 : garde 3 (antériorité) sur des dépôts jouets, cas non couverts par les tests du module : scellement sur une
branche fusionnée après la lecture ; empreinte ajoutée, retirée puis rajoutée (préenregistrement rescellé) après la
lecture ; clone superficiel qui contient pourtant le commit de scellement ; renommage du compagnon ; commit de lecture
abrégé ; scellement et lecture au même commit. Rien n'est écrit hors de ce dossier."""
import hashlib
import shutil
import subprocess
import tempfile
from pathlib import Path

import commun  # noqa: F401
from commun import ICI, cp

COMP = cp.PREREG_ADDENDUM + ".sha256"
ENV = {"GIT_AUTHOR_NAME": "r", "GIT_AUTHOR_EMAIL": "r@x", "GIT_COMMITTER_NAME": "r", "GIT_COMMITTER_EMAIL": "r@x",
       "PATH": "/usr/bin:/bin", "HOME": ICI}


def git(d, *a):
    r = subprocess.run(["git", "-C", str(d), *a], capture_output=True, text=True, env=ENV)
    if r.returncode:
        raise RuntimeError(r.stderr)
    return r.stdout.strip()


def ecrire(d, chemin, texte):
    p = Path(d, chemin)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texte, encoding="utf-8")


def sceller(d, texte):
    ecrire(d, cp.PREREG_ADDENDUM, texte)
    sha = hashlib.sha256(texte.encode("utf-8")).hexdigest()
    ecrire(d, COMP, f"{sha}  P3-addendum-lecture-complementaire-v1.md\n")
    return sha


def commit(d, msg):
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", msg, "--allow-empty")
    return git(d, "rev-parse", "HEAD")


def essai(nom, f):
    base = Path(tempfile.mkdtemp(prefix="essai06-", dir=ICI))
    try:
        d = base / "depot"
        d.mkdir()
        git(d, "init", "-q", "-b", "main")
        ecrire(d, "README", "x")
        commit(d, "racine")
        racine, sha, lect, attendu = f(d, base)
        try:
            s = cp.exiger_anteriorite(racine, sha, lect)
            r = f"passe (scellement {s[:8]})"
        except cp.GardeArret as e:
            r = f"ARRÊT : {e}"
        print(f"{nom} : {r} ; attendu : {attendu}")
    finally:
        shutil.rmtree(base)


def sain(d, base):
    sha = sceller(d, "v1")
    commit(d, "scellement")
    return d, sha, commit(d, "lecture"), "passe"


def meme_commit(d, base):
    sha = sceller(d, "v1")
    c = commit(d, "scellement et lecture")
    return d, sha, c, "passe (le scellement précède la lecture lancée sur ce commit)"


def branche_fusionnee_apres(d, base):
    git(d, "checkout", "-q", "-b", "addendum")
    sha = sceller(d, "v1")
    commit(d, "scellement sur une branche")
    git(d, "checkout", "-q", "main")
    lect = commit(d, "lecture sur main, sans le scellement")
    git(d, "merge", "-q", "--no-ff", "-m", "fusion après la lecture", "addendum")
    return d, sha, lect, "arrêt (scellement non ancêtre de la lecture)"


def rescelle_apres(d, base):
    sceller(d, "v1")
    commit(d, "scellement v1")
    lect = commit(d, "lecture")
    git(d, "rm", "-q", COMP)
    commit(d, "retrait du compagnon")
    sha2 = sceller(d, "v2 modifié après la lecture")
    commit(d, "rescellement après la lecture")
    return d, sha2, lect, "arrêt (premier ajout : empreinte de v1 ≠ empreinte vérifiée de v2)"


def superficiel_complet(d, base):
    sha = sceller(d, "v1")
    commit(d, "scellement")
    lect = commit(d, "lecture")
    c = base / "clone"
    subprocess.run(["git", "clone", "-q", "--depth", "2", f"file://{d}", str(c)], check=True, capture_output=True,
                   env=ENV)
    return c, sha, lect, "arrêt (dépôt superficiel exigé non superficiel, même si l'histoire utile est là)"


def compagnon_renomme(d, base):
    ecrire(d, "prereg/brouillon.md", "v1")
    sha = hashlib.sha256(b"v1").hexdigest()
    ecrire(d, "prereg/brouillon.md.sha256", f"{sha}  brouillon.md\n")
    commit(d, "scellement sous un autre nom")
    git(d, "mv", "prereg/brouillon.md", cp.PREREG_ADDENDUM)
    git(d, "mv", "prereg/brouillon.md.sha256", COMP)
    commit(d, "renommage")
    return d, sha, commit(d, "lecture"), "arrêt ou passe : à lire (renommage vu comme ajout ?)"


def lecture_abregee(d, base):
    sha = sceller(d, "v1")
    commit(d, "scellement")
    return d, sha, commit(d, "lecture")[:10], "passe (git accepte un préfixe)"


for nom, f in (("sain", sain), ("même commit", meme_commit), ("branche fusionnée après la lecture", branche_fusionnee_apres),
               ("compagnon retiré puis rescellé après la lecture", rescelle_apres),
               ("clone superficiel qui contient le scellement", superficiel_complet),
               ("compagnon renommé", compagnon_renomme), ("commit de lecture abrégé", lecture_abregee)):
    essai(nom, f)

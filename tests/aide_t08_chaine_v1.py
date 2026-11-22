"""Aide des essais de la chaîne de lancement de T0.8 (v1) : un dépôt git jetable, données factices seulement.

Trois commits orphelins, sur trois branches : « 7b » (sortie factice de la course de confirmation, avec un fichier de sondes
et un `resume.json` qui ne doivent jamais être copiés), « code » (fichiers de `main` lus par la course : tâches, consignes,
invite dérivée, guide de classification ; plus un `resume.json` ancien), « texte » (texte scellé factice et configuration
réelle factice de la course). Aucun fichier réel du programme n'est lu : chemins réels, contenus inventés.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

RUN_7B = "20261111-151701-t06-reel"
CH_TEXTE = "prereg/T0.8-bases-boite-noire-v0-v1.md"
CH_CONFIG = "prereg/T0.8-configuration-course-v1.json"
CH = {"textes_7b": f"donnees/{RUN_7B}/textes-actions-t06.jsonl", "episodes_7b": f"diag/{RUN_7B}/episodes-t06.json",
      "manifeste_7b": f"runs/{RUN_7B}/manifeste.json",
      "taches": "donnees/20261007-082440-t05-extraction/taches-evaluation.json", "consignes": "prereg/P3-consignes-v1.md",
      "invite": "docs/sources/invites-2606.08892-v1/derivees/H12-par-action-v1.txt"}
GUIDE = ("docs/sources/invites-2606.08892-v1/index.json", "docs/sources/invites-2606.08892-v1/invites/H1-classification.txt")


def git(d, *a, entree=None):
    r = subprocess.run(["git", "-C", str(d), *a], capture_output=True, input=entree)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.decode())
    return r.stdout.decode().strip()


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def poser(d: Path, chemin: str, contenu: bytes, compagnon: bool = True) -> str:
    p = d / chemin
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(contenu)
    if compagnon:
        (d / (chemin + ".sha256")).write_text(f"{sha(contenu)}  {p.name}\n")
    return sha(contenu)


def commit_orphelin(d: Path, branche: str, fichiers: dict[str, bytes], compagnons: bool = True) -> str:
    git(d, "checkout", "-q", "--orphan", branche)
    git(d, "rm", "-rq", "--cached", "--ignore-unmatch", ".")
    for x in list(d.iterdir()):
        if x.name != ".git":
            subprocess.run(["rm", "-rf", str(x)], check=True)
    for c, b in fichiers.items():
        poser(d, c, b, compagnons and not c.endswith(("resume.json",)))
    git(d, "add", "-A", "-f")
    git(d, "commit", "-q", "-m", f"factice : {branche}")
    return git(d, "rev-parse", "HEAD")


def depot_factice(d: Path) -> dict:
    d.mkdir(parents=True, exist_ok=True)
    git(d, "init", "-q", "-b", "amorce")
    git(d, "config", "user.email", "essai@invalid")
    git(d, "config", "user.name", "essai")
    f7b = {CH["textes_7b"]: b'{"cle": "h__t000__p0", "texte": "factice"}\n',
           CH["episodes_7b"]: b'{"resultat": {"effectifs": {}}}\n',
           CH["manifeste_7b"]: b'{"run_id": "20261111-151701-t06-reel"}\n',
           f"diag/{RUN_7B}/lecture-sondes-t06.json": b'{"sondes": "jamais"}\n',
           f"diag/{RUN_7B}/resume.json": b'{"ligne_B": "jamais"}\n',
           f"donnees/{RUN_7B}/mesures-t06.npz": b"npz factice\n"}
    c7b = commit_orphelin(d, "calcul/t06-confirmation-7b-factice", f7b)
    fcode = {CH["taches"]: b'[{"identifiant": "t000", "questions": "q"}]\n', CH["consignes"]: b"consignes factices\n",
             CH["invite"]: b"invite derivee factice\n", GUIDE[0]: b'{"invites": []}\n', GUIDE[1]: b"guide factice\n",
             "diag/20261004-104156-harnais-factice/resume.json": b"{}\n", "src/controle_ia/__init__.py": b""}
    ccode = commit_orphelin(d, "prep/code-factice", fcode)
    emp = {"textes-actions-t06.jsonl": sha(f7b[CH["textes_7b"]]), "episodes-t06.json": sha(f7b[CH["episodes_7b"]]),
           "manifeste.json": sha(f7b[CH["manifeste_7b"]]), "mesures-t06.npz": "1" * 64, "lecture-cout-t06.json": "2" * 64}
    return {"depot": d, "c7b": c7b, "ccode": ccode, "f7b": f7b, "fcode": fcode, "emp": emp}


def config_factice(fx: dict, **changes) -> dict:
    e = {n: {"chemin": CH[n], "sha256": sha((fx["f7b"] if n.endswith("_7b") else fx["fcode"])[CH[n]]), "phase": "course"}
         for n in CH}
    c = {"mode": "reel", "entrees": e, "marqueurs": {"EMPREINTES_ENTREES_7B": dict(fx["emp"])}}
    c.update(changes)
    return c


def texte_factice(fx: dict, sans: tuple = ()) -> bytes:
    lignes = ["# Préenregistrement factice de T0.8", f"tête de 7b : `{fx['c7b']}`"]
    lignes += [f"- `{k}`, `{v}`" for k, v in fx["emp"].items() if k not in sans]
    return ("\n".join(lignes) + "\n").encode()


def commit_texte(fx: dict, config: dict | None = None, texte: bytes | None = None, branche: str = "main-factice") -> str:
    config = config if config is not None else config_factice(fx)
    texte = texte if texte is not None else texte_factice(fx)
    return commit_orphelin(fx["depot"], branche, {CH_TEXTE: texte,
                                                  CH_CONFIG: (json.dumps(config, indent=1, sort_keys=True) + "\n").encode()})

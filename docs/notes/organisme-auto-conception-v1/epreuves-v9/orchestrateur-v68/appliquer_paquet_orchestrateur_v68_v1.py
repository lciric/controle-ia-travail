"""Application du paquet « orchestrateur v68 » (v1) sur une copie neuve de l'orchestrateur — jamais sur l'orchestrateur source.

Ce programme :

1. lit le manifeste du paquet (`manifeste-paquet-orchestrateur-v68-v1.json`, à côté de ce programme) et vérifie l'empreinte
   sha256 de chaque fichier du paquet (`paquet/…`) avant toute copie ;
2. refuse une destination existante, une destination égale à la source ou placée dedans, et toute destination qui serait
   `/home/user/ideation-organism` ;
3. clone la source (dépôt git de l'orchestrateur, **lu seulement** : `git clone --no-hardlinks`, aucune écriture dans la source)
   dans la destination neuve et y fixe le commit de base du manifeste (`git checkout --detach`) ;
4. copie chaque fichier du paquet à son chemin relatif dans la destination ; refuse un fichier déjà présent (le paquet n'ajoute
   que des fichiers neufs, R12) ; vérifie l'empreinte de chaque copie ;
5. vérifie par `git status --porcelain` que seuls des fichiers non suivis se sont ajoutés (aucun fichier suivi modifié) ;
6. avec `--lancer-essais`, lance les essais de la v68 dans la destination (`python -B -m pytest -q -p no:cacheprovider
   orchestrator/essais/test_v68_course2.py`), hors ligne, moteur simulé.

Rend un rapport JSON sur la sortie standard ; code 0 si tout est conforme, 2 sinon (motif dit).

  python3 -B appliquer_paquet_orchestrateur_v68_v1.py --source /home/user/ideation-organism --destination COPIE_NEUVE [--lancer-essais]
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
MANIFESTE = os.path.join(ICI, "manifeste-paquet-orchestrateur-v68-v1.json")
INTERDITE = "/home/user/ideation-organism"


class Refus(RuntimeError):
    pass


def sha256(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def git(*args, cwd=None):
    p = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, timeout=600)
    if p.returncode != 0:
        raise Refus(f"git {' '.join(args)} : code {p.returncode} : {p.stderr.strip()[:300]}")
    return p.stdout


def appliquer(source, destination, lancer_essais=False):
    with open(MANIFESTE, encoding="utf-8") as f:
        m = json.load(f)
    fichiers = m["fichiers_du_paquet"]
    for x in fichiers:  # 1. empreintes du paquet avant toute copie
        p = os.path.join(ICI, x["chemin_paquet"])
        if not os.path.isfile(p) or os.path.islink(p):
            raise Refus(f"fichier du paquet absent ou non régulier : {x['chemin_paquet']}")
        if sha256(p) != x["sha256"]:
            raise Refus(f"empreinte du paquet différente pour {x['chemin_paquet']} : refus avant toute copie")
    src, dst = os.path.realpath(source), os.path.realpath(os.path.abspath(destination))  # 2. destination
    if os.path.exists(destination):
        raise Refus(f"destination {destination} déjà présente : copie neuve exigée (R12)")
    if dst == os.path.realpath(INTERDITE) or dst.startswith(os.path.realpath(INTERDITE) + os.sep):
        raise Refus("destination dans l'orchestrateur source : interdit (il reste en lecture seule)")
    if dst == src or dst.startswith(src + os.sep):
        raise Refus("destination égale à la source ou placée dedans : interdit")
    base = m["commit_de_base"]
    git("clone", "--quiet", "--no-hardlinks", src, dst)  # 3. copie neuve (la source n'est que lue)
    git("checkout", "--quiet", "--detach", base, cwd=dst)
    if git("rev-parse", "HEAD", cwd=dst).strip() != base:
        raise Refus("la copie n'est pas au commit de base du manifeste")
    if git("status", "--porcelain", cwd=dst).strip():
        raise Refus("la copie neuve n'est pas propre avant application")
    copies = []
    for x in fichiers:  # 4. copie, fichiers neufs seulement
        cible = os.path.join(dst, x["chemin"])
        if os.path.lexists(cible):
            raise Refus(f"{x['chemin']} existe déjà dans l'orchestrateur : le paquet n'ajoute que des fichiers neufs (R12)")
        os.makedirs(os.path.dirname(cible), exist_ok=True)
        shutil.copyfile(os.path.join(ICI, x["chemin_paquet"]), cible)
        if sha256(cible) != x["sha256"]:
            raise Refus(f"empreinte de la copie différente : {x['chemin']}")
        copies.append(x["chemin"])
    etat = [l for l in git("status", "--porcelain", "--untracked-files=all", cwd=dst).splitlines() if l.strip()]  # 5.
    non_suivis = sorted(l[3:] for l in etat if l.startswith("?? "))
    autres = [l for l in etat if not l.startswith("?? ")]
    if autres or non_suivis != sorted(copies):
        raise Refus(f"git status inattendu : modifiés {autres[:5]} ; non suivis {non_suivis[:12]}")
    rapport = {"conforme": True, "source": src, "destination": dst, "commit_de_base": base, "fichiers_ajoutes": copies,
               "git_status": "seuls les fichiers du paquet, non suivis ; aucun fichier suivi modifié"}
    if lancer_essais:  # 6.
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        p = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider",
                            "essais/test_v68_course2.py"], cwd=os.path.join(dst, "orchestrator"), env=env,
                           capture_output=True, text=True, timeout=3600)
        rapport["essais_v68"] = {"code": p.returncode, "resume": (p.stdout.strip().splitlines() or [""])[-1]}
        rapport["conforme"] = p.returncode == 0
    return rapport


def principal(argv=None):
    a = argparse.ArgumentParser(description="applique le paquet orchestrateur v68 sur une copie neuve")
    a.add_argument("--source", required=True)
    a.add_argument("--destination", required=True)
    a.add_argument("--lancer-essais", action="store_true")
    args = a.parse_args(argv)
    try:
        r = appliquer(args.source, args.destination, args.lancer_essais)
    except (Refus, OSError, KeyError, ValueError) as e:
        print(json.dumps({"conforme": False, "refus": f"{type(e).__name__} : {e}"}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(r, ensure_ascii=False, indent=1))
    return 0 if r["conforme"] else 2


if __name__ == "__main__":
    raise SystemExit(principal())

"""Application du paquet du lot 6 v5 du véhicule NA-1 sur une copie où la chaîne est déjà posée (base `a41b7b50`, v68,
lots 2 v5, 3 v3, 4 v1, 4 v3, 5 v1, 10 a, 6 v3, par leurs programmes, dans cet ordre).

Ce programme :
1. lit le manifeste (`manifeste-paquet-vehicule-na-lot-6-v5.json`, à côté de lui) et vérifie, avant toute copie,
   l'empreinte de chaque fichier source : les trois modules du lot 5 v3 (lus dans leur dossier, jamais modifiés) et les
   fichiers du paquet v5 ;
2. refuse une destination sans `orchestrator/pole/course_na_v3.py` (lot 6 v3 non posé), ou sans
   `orchestrator/pole/appel_garde_na_v3.py` (lot 4 v3 non posé) ;
3. copie chaque fichier à son chemin ; refuse un fichier déjà présent (R12) ; vérifie l'empreinte de chaque copie ;
4. avec `--lancer-essais`, joue les essais du lot 6 v5 dans `orchestrator` (`python -B -m pytest -q -p no:cacheprovider
   essais/test_na_lot6_v5_course.py`), sans la variable de clé dans l'environnement.

Rend un rapport JSON ; code 0 si conforme, 2 sinon.

    python3 -B appliquer_paquet_vehicule_na_lot_6_v5.py --destination COPIE [--lancer-essais]
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
MANIFESTE = os.path.join(ICI, "manifeste-paquet-vehicule-na-lot-6-v5.json")
EXIGES = ("orchestrator/pole/course_na_v3.py", "orchestrator/pole/appel_garde_na_v3.py",
          "orchestrator/pole/matiere_premiere_na_v1.py", "orchestrator/pole/portier_na_v1.py")


class Refus(RuntimeError):
    pass


def sha256(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def appliquer(destination, lancer_essais=False):
    with open(MANIFESTE, encoding="utf-8") as f:
        m = json.load(f)
    fichiers = m["fichiers"]
    for x in fichiers:
        src = x["source"] if os.path.isabs(x["source"]) else os.path.join(ICI, x["source"])
        if not os.path.isfile(src) or os.path.islink(src):
            raise Refus(f"source absente ou non régulière : {x['source']}")
        if sha256(src) != x["sha256"]:
            raise Refus(f"empreinte différente pour {x['source']} : refus avant toute copie")
    dst = os.path.realpath(destination)
    for e in EXIGES:
        if not os.path.isfile(os.path.join(dst, e)):
            raise Refus(f"chaîne non posée dans la destination : {e} absent")
    copies = []
    for x in fichiers:
        cible = os.path.join(dst, x["chemin"])
        if os.path.lexists(cible):
            raise Refus(f"{x['chemin']} existe déjà : le paquet n'ajoute que des fichiers neufs (R12)")
    for x in fichiers:
        src = x["source"] if os.path.isabs(x["source"]) else os.path.join(ICI, x["source"])
        cible = os.path.join(dst, x["chemin"])
        os.makedirs(os.path.dirname(cible), exist_ok=True)
        shutil.copyfile(src, cible)
        if sha256(cible) != x["sha256"]:
            raise Refus(f"empreinte de la copie différente : {x['chemin']}")
        copies.append(x["chemin"])
    rapport = {"conforme": True, "copies": copies}
    if lancer_essais:
        env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        p = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider",
                            "essais/test_na_lot6_v5_course.py"], cwd=os.path.join(dst, "orchestrator"), env=env,
                           capture_output=True, text=True, timeout=3600)
        rapport["essais_lot_6_v5"] = {"code": p.returncode, "resume": (p.stdout.strip().splitlines() or [""])[-1]}
        rapport["conforme"] = p.returncode == 0
    return rapport


def principal(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("--destination", required=True)
    a.add_argument("--lancer-essais", action="store_true")
    args = a.parse_args(argv)
    try:
        r = appliquer(args.destination, args.lancer_essais)
    except (Refus, OSError, KeyError, ValueError) as e:
        print(json.dumps({"conforme": False, "refus": f"{type(e).__name__} : {e}"}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(r, ensure_ascii=False, indent=1))
    return 0 if r["conforme"] else 2


if __name__ == "__main__":
    raise SystemExit(principal())

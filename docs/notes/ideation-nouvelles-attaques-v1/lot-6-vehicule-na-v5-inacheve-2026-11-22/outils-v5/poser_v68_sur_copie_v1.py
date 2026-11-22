"""Pose du paquet v68 sur une copie déjà faite (cp -r de la base `a41b7b50`, sans `.git`) — lot 6 v5, outil de reprise.

Le programme de la v68 (`appliquer_paquet_orchestrateur_v68_v1.py`) clone un dépôt git dans une destination neuve ; la base
du mandat est un arbre sans `.git`, déjà copié. Cet outil reprend les étapes 1 (empreintes du paquet avant toute copie),
4 (copie de fichiers neufs seulement, empreinte relue) et 6 (essais de la v68) du programme, par ses propres fonctions
(`sha256`, `MANIFESTE`, `ICI`) ; les étapes 2, 3 et 5 (git) sont sans objet et dites au rapport.

    python -B poser_v68_sur_copie_v1.py --programme CHEMIN_DU_PROGRAMME_V68 --destination COPIE [--lancer-essais]
"""

import argparse
import importlib.util
import json
import os
import shutil
import subprocess
import sys


def charger(chemin):
    spec = importlib.util.spec_from_file_location("appliquer_v68", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def principal(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("--programme", required=True)
    a.add_argument("--destination", required=True)
    a.add_argument("--lancer-essais", action="store_true")
    args = a.parse_args(argv)
    p = charger(args.programme)
    with open(p.MANIFESTE, encoding="utf-8") as f:
        m = json.load(f)
    fichiers = m["fichiers_du_paquet"]
    for x in fichiers:
        src = os.path.join(p.ICI, x["chemin_paquet"])
        if not os.path.isfile(src) or os.path.islink(src) or p.sha256(src) != x["sha256"]:
            print(json.dumps({"conforme": False, "refus": f"paquet v68 : {x['chemin_paquet']}"}, ensure_ascii=False))
            return 2
    dst = os.path.realpath(args.destination)
    if not os.path.isfile(os.path.join(dst, "orchestrator", "pole", "__init__.py")):
        print(json.dumps({"conforme": False, "refus": "destination sans orchestrator/pole/__init__.py"}))
        return 2
    for x in fichiers:
        if os.path.lexists(os.path.join(dst, x["chemin"])):
            print(json.dumps({"conforme": False, "refus": f"{x['chemin']} existe déjà (R12)"}, ensure_ascii=False))
            return 2
    copies = []
    for x in fichiers:
        cible = os.path.join(dst, x["chemin"])
        os.makedirs(os.path.dirname(cible), exist_ok=True)
        shutil.copyfile(os.path.join(p.ICI, x["chemin_paquet"]), cible)
        if p.sha256(cible) != x["sha256"]:
            print(json.dumps({"conforme": False, "refus": f"copie : {x['chemin']}"}, ensure_ascii=False))
            return 2
        copies.append(x["chemin"])
    rapport = {"conforme": True, "commit_de_base": m["commit_de_base"], "fichiers_ajoutes": copies,
               "etapes_git": "sans objet : base sans .git, copiée par cp -r (dit au rapport)"}
    if args.lancer_essais:
        env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider",
                            "essais/test_v68_course2.py"], cwd=os.path.join(dst, "orchestrator"), env=env,
                           capture_output=True, text=True, timeout=3600)
        rapport["essais_v68"] = {"code": r.returncode, "resume": (r.stdout.strip().splitlines() or [""])[-1]}
        rapport["conforme"] = r.returncode == 0
    print(json.dumps(rapport, ensure_ascii=False, indent=1))
    return 0 if rapport["conforme"] else 2


if __name__ == "__main__":
    raise SystemExit(principal())

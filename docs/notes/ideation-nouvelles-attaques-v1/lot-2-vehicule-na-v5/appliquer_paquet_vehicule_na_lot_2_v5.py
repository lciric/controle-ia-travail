"""Programme d'application du paquet v5 du lot 2 du véhicule NA-1, lot 1 compris pour l'import (manière de la v68,
R68, § 2). Le paquet porte la source Unicode 15.1.0 à son empreinte ; il ne porte **aucune copie de la liste réelle des
noms refusés** (décision R-4500) : l'essai qui la lit la prend sur la branche principale du dépôt de l'organisme
(`origin/main`, ou `NA_LISTE_REELLE_DEPOT`, `NA_LISTE_REELLE_REF`, `NA_LISTE_REELLE_FICHIER`) et échoue si elle manque.

`python -B appliquer_paquet_vehicule_na_lot_2_v5.py --destination COPIE [--lancer-essais]`

- Lit le manifeste voisin (`manifeste-paquet-vehicule-na-lot-2-v5.json`) et vérifie l'empreinte de chaque fichier du
  paquet avant toute copie ; un fichier altéré : refus, rien n'est copié.
- `COPIE` est une copie de l'orchestrateur (le dossier qui contient `orchestrator/pole/__init__.py`), faite par
  l'opérateur ; le dépôt de l'orchestrateur lui-même est refusé comme destination, et rien n'y est jamais écrit.
- Chaque fichier du paquet est neuf : une cible déjà présente est refusée (R12), avant toute copie.
- Après la copie, chaque copie est relue et comparée à son empreinte.
- `--lancer-essais` joue ensuite les deux fichiers d'essais des lots 1 et 2 dans la copie (`python -B -m pytest -q
  -p no:cacheprovider`) et rend leur code.

Le programme ne clone rien et n'écrit dans aucun dépôt (écart à la v68, dont le programme clonait la source : ici, la copie
est donnée par l'opérateur). Aucun réseau, aucune clé.
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
MANIFESTE = os.path.join(ICI, "manifeste-paquet-vehicule-na-lot-2-v5.json")
SOURCES_LUES_SEULES = ("/home/user/lciric/ideation-organism", "/home/user/ideation-organism")


class ApplicationRefusee(RuntimeError):
    pass


def sha256_fichier(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def dans(chemin, dossier):
    chemin, dossier = os.path.realpath(chemin), os.path.realpath(dossier)
    return chemin == dossier or chemin.startswith(dossier + os.sep)


def appliquer(destination, manifeste=MANIFESTE):
    with open(manifeste, encoding="utf-8") as f:
        m = json.load(f)
    fichiers = m["fichiers_du_paquet"]
    for e in fichiers:
        source = os.path.join(ICI, e["chemin_paquet"])
        if not os.path.isfile(source) or sha256_fichier(source) != e["sha256"]:
            raise ApplicationRefusee(f"fichier du paquet absent ou altéré : {e['chemin_paquet']}")
    for interdit in SOURCES_LUES_SEULES:
        if dans(destination, interdit):
            raise ApplicationRefusee("destination dans le dépôt de l'orchestrateur : refusée (lu seulement)")
    if dans(destination, os.path.join(ICI, "paquet")):
        raise ApplicationRefusee("destination dans le paquet : refusée")
    if not os.path.isfile(os.path.join(destination, "orchestrator", "pole", "__init__.py")):
        raise ApplicationRefusee("la destination n'est pas une copie de l'orchestrateur")
    for e in fichiers:
        if os.path.exists(os.path.join(destination, e["chemin"])):
            raise ApplicationRefusee(f"cible déjà présente : {e['chemin']} (R12)")
    for e in fichiers:
        cible = os.path.join(destination, e["chemin"])
        os.makedirs(os.path.dirname(cible), exist_ok=True)  # v4 : sous-dossiers neufs (source Unicode, liste réelle)
        shutil.copyfile(os.path.join(ICI, e["chemin_paquet"]), cible)
    for e in fichiers:
        if sha256_fichier(os.path.join(destination, e["chemin"])) != e["sha256"]:
            raise ApplicationRefusee(f"copie différente de son empreinte : {e['chemin']}")
    return [e["chemin"] for e in fichiers]


def main(argv=None):
    p = argparse.ArgumentParser(description="application du paquet des lots 1 et 2 du véhicule NA-1")
    p.add_argument("--destination", required=True)
    p.add_argument("--lancer-essais", action="store_true")
    a = p.parse_args(argv)
    copies = appliquer(a.destination)
    print(json.dumps({"copies": copies}, ensure_ascii=False))
    if not a.lancer_essais:
        return 0
    orch = os.path.join(a.destination, "orchestrator")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider",
                        "essais/test_na_v4_tirage.py", "essais/test_na_v5_garde_motifs.py"], cwd=orch, env=env)
    return r.returncode


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ApplicationRefusee as e:
        print(f"refus : {e}", file=sys.stderr)
        sys.exit(2)

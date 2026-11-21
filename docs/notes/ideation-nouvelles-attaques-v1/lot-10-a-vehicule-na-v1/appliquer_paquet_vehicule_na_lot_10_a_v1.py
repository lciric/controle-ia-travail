"""Programme d'application du paquet v1 du lot 10 a du véhicule NA-1 (manière de la v68, R68, § 2, et des programmes des
lots 2 à 5).

`python -B appliquer_paquet_vehicule_na_lot_10_a_v1.py --destination COPIE [--lancer-essais]`

- Lit le manifeste voisin (`manifeste-paquet-vehicule-na-lot-10-a-v1.json`) et vérifie l'empreinte de chaque fichier du
  paquet avant toute copie ; un fichier altéré : refus, rien n'est copié.
- `COPIE` est une copie de l'orchestrateur (le dossier qui contient `orchestrator/pole/__init__.py`) **sur laquelle les
  paquets des lots 2 v5, 3 v3, 4 v1 et 5 v1 sont déjà posés** par leurs programmes : chaque dépendance du manifeste et
  chaque fichier existant lu doit y être, à son empreinte ; sinon refus, rien n'est copié. Le dépôt de l'orchestrateur et
  sa copie de référence sont refusés comme destination, et rien n'y est jamais écrit.
- Chaque fichier du paquet est neuf : une cible déjà présente est refusée (R12), avant toute copie.
- Après la copie, chaque copie est relue et comparée à son empreinte.
- `--lancer-essais` joue ensuite, dans la copie, les essais des lots 3 v3, 4 v1, 5 v1 et 10 a
  (`python -B -m pytest -q -p no:cacheprovider`) et rend leur code.

Le programme ne clone rien et n'écrit dans aucun dépôt. Aucun réseau, aucune clé.
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
MANIFESTE = os.path.join(ICI, "manifeste-paquet-vehicule-na-lot-10-a-v1.json")
SOURCES_LUES_SEULES = ("/home/user/lciric/ideation-organism", "/home/user/orchestrateur-a41b7b50")
ESSAIS = ("essais/test_na_v3_requete.py", "essais/test_na_v3_journal.py", "essais/test_na_v1_appel_garde.py",
          "essais/test_na_v1_adaptateur_claude.py", "essais/test_na_lot5_v1_lecteur.py", "essais/test_na_lot5_v1_contrat.py",
          "essais/test_na_lot5_v1_portier.py", "essais/test_na_lot5_v1_registre.py",
          "essais/test_na_lot5_v1_identifiants.py", "essais/test_na_lot10a_v1_matiere_premiere.py")


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
            raise ApplicationRefusee("destination dans l'orchestrateur de référence : refusée (lu seulement)")
    if dans(destination, os.path.join(ICI, "paquet")):
        raise ApplicationRefusee("destination dans le paquet : refusée")
    if not os.path.isfile(os.path.join(destination, "orchestrator", "pole", "__init__.py")):
        raise ApplicationRefusee("la destination n'est pas une copie de l'orchestrateur")
    for e in m["dependances_lots_2_a_5"] + m["fichiers_existants_lus"]:
        cible = os.path.join(destination, e["chemin"])
        if not os.path.isfile(cible) or sha256_fichier(cible) != e["sha256"]:
            raise ApplicationRefusee(f"fichier requis absent ou d'une autre empreinte : {e['chemin']}")
    for e in fichiers:
        if os.path.exists(os.path.join(destination, e["chemin"])):
            raise ApplicationRefusee(f"cible déjà présente : {e['chemin']} (R12)")
    for e in fichiers:
        shutil.copyfile(os.path.join(ICI, e["chemin_paquet"]), os.path.join(destination, e["chemin"]))
    for e in fichiers:
        if sha256_fichier(os.path.join(destination, e["chemin"])) != e["sha256"]:
            raise ApplicationRefusee(f"copie différente de son empreinte : {e['chemin']}")
    return [e["chemin"] for e in fichiers]


def main(argv=None):
    p = argparse.ArgumentParser(description="application du paquet du lot 10 a du véhicule NA-1")
    p.add_argument("--destination", required=True)
    p.add_argument("--lancer-essais", action="store_true")
    a = p.parse_args(argv)
    copies = appliquer(a.destination)
    print(json.dumps({"copies": copies}, ensure_ascii=False))
    if not a.lancer_essais:
        return 0
    orch = os.path.join(a.destination, "orchestrator")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", *ESSAIS], cwd=orch, env=env)
    return r.returncode


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ApplicationRefusee as e:
        print(f"refus : {e}", file=sys.stderr)
        sys.exit(2)

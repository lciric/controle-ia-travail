"""Différentiel des sorties v1 → v2 du calcul des conditions du plafond à 200 (ligne 3).

Lit les deux sorties par empreinte (arrêt si l'une diffère de son compagnon), les parcourt
feuille par feuille (nombres lus en décimal exact, jamais en flottant) et rend chaque chemin
présent d'un seul côté ou de valeur différente, avec les deux valeurs.

Usage : python3 -I -B CE_FICHIER > SORTIE.json (aucun argument).
"""

import hashlib
import json
import sys
from decimal import Decimal

DOSSIER = "/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-calcul-plafond-200"
V1 = ("calcul-conditions-plafond-200-ligne-3-v1.json",
      "20ade9a3feae5b6c5dea3be61808dc71a656d81291857a13facd950baca44fc0")
V2 = ("calcul-conditions-plafond-200-ligne-3-v2.json",
      "fe58be3a790ee28db3fadb6370251a69c4378dc887e977a19ab77fd9093eb3e2")


def lire(nom, empreinte):
    with open(f"{DOSSIER}/{nom}", "rb") as f:
        octets = f.read()
    vu = hashlib.sha256(octets).hexdigest()
    if vu != empreinte:
        raise SystemExit(f"empreinte inattendue pour {nom} : {vu}")
    return json.loads(octets.decode("utf-8"), parse_float=Decimal)


def feuilles(objet, chemin=""):
    if isinstance(objet, dict):
        for cle, valeur in objet.items():
            yield from feuilles(valeur, f"{chemin}.{cle}" if chemin else cle)
    elif isinstance(objet, list):
        for i, valeur in enumerate(objet):
            yield from feuilles(valeur, f"{chemin}[{i}]")
    else:
        yield chemin, objet


def main(argv):
    if len(argv) != 1:
        raise SystemExit("usage : python3 -I -B differentiel_sorties_plafond_200_v1_v2.py > SORTIE.json")
    a = dict(feuilles(lire(*V1)))
    b = dict(feuilles(lire(*V2)))
    diff = {}
    for chemin in sorted(set(a) | set(b)):
        va, vb = a.get(chemin, "<absent>"), b.get(chemin, "<absent>")
        if type(va) is not type(vb) or va != vb:
            diff[chemin] = {"v1": str(va), "v2": str(vb)}
    sortie = {"sorties": {"v1": list(V1), "v2": list(V2)},
              "feuilles_v1": len(a), "feuilles_v2": len(b),
              "feuilles_differentes": len(diff), "differences": diff}
    texte = json.dumps(sortie, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    sys.stdout.buffer.write(texte.encode("utf-8"))


if __name__ == "__main__":
    main(sys.argv)

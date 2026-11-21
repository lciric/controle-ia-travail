#!/usr/bin/env python3
"""Vérifie que chaque nom neutre repris par l'ordre de course existe tel quel dans le registre servi des visées.

Lecture seule ; bibliothèque standard ; la sortie (JSON, clés triées) va sur la sortie standard. Du registre, le programme ne
lit que le champ `nom_neutre` ; il n'écrit aucun autre champ dans sa sortie.

Dans l'ordre, les noms sont pris dans la première colonne de la table qui suit la ligne contenant DEBUT et précède la ligne
contenant FIN ; une cellule peut porter plusieurs noms, séparés par « ; ».

Usage : python3 -B verifier_noms_neutres_v1.py --ordre ORDRE.md --registre REGISTRE.json > SORTIE.json
Code de sortie : 0 si aucun nom n'est absent, 3 sinon, 1 si la table n'est pas trouvée.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

DEBUT = "**Familles de scores tirées du registre servi des visées.**"
FIN = "**Qui écrit, et quand.**"
ENTETE = "nom neutre au registre"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ordre", required=True)
    p.add_argument("--registre", required=True)
    a = p.parse_args()
    octets_ordre = Path(a.ordre).read_bytes()
    octets_registre = Path(a.registre).read_bytes()
    lignes = octets_ordre.decode("utf-8").split("\n")
    debuts = [i for i, l in enumerate(lignes) if DEBUT in l]
    fins = [i for i, l in enumerate(lignes) if FIN in l]
    if len(debuts) != 1 or len(fins) != 1 or fins[0] <= debuts[0]:
        print(json.dumps({"erreur": "table introuvable ou ambiguë", "debuts": len(debuts), "fins": len(fins)},
                         ensure_ascii=False, sort_keys=True))
        return 1
    repris = []
    for l in lignes[debuts[0] + 1:fins[0]]:
        if not l.startswith("|"):
            continue
        cellule = l.split("|")[1].strip()
        if not cellule or cellule == ENTETE or set(cellule) <= set("-: "):
            continue
        repris.extend(n.strip() for n in cellule.split(" ; ") if n.strip())
    registre = json.loads(octets_registre.decode("utf-8"))
    noms = [e["nom_neutre"] for e in registre]
    presents = [n for n in repris if n in noms]
    absents = [n for n in repris if n not in noms]
    sortie = {
        "piece": "verification-noms-neutres-v1",
        "ordre_sha256": hashlib.sha256(octets_ordre).hexdigest(),
        "registre_sha256": hashlib.sha256(octets_registre).hexdigest(),
        "entrees_du_registre": len(noms),
        "noms_repris_par_l_ordre": repris,
        "nombre_repris": len(repris),
        "presents_tels_quels": presents,
        "absents": absents,
        "nombre_absents": len(absents),
        "repris_en_double": sorted({n for n in repris if repris.count(n) > 1}),
    }
    print(json.dumps(sortie, ensure_ascii=False, indent=1, sort_keys=True))
    return 0 if not absents else 3


if __name__ == "__main__":
    sys.exit(main())

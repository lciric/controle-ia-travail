"""Mutations de l'inventaire v4 pour les épreuves (copie partielle seulement).

Usage : python3 -I muter_inventaire_v1.py ENTREE SORTIE MUTATION ARGUMENT
MUTATION : retirer-entree (ARGUMENT = nom qualifié exact) ; retirer-module (ARGUMENT = chemin relatif du module, toutes
ses entrées au registre et ses lecteurs admis) ; retirer-lecteurs (ARGUMENT = module) ; ajouter-fantome (ARGUMENT = nom
qualifié qui n'existe pas dans le code) ; ajouter-lecteur-mort (ARGUMENT = module::fonction qui ne lit pas la clé).
"""
import json
import sys
from pathlib import Path


def main(entree: str, sortie: str, mutation: str, argument: str) -> None:
    doc = json.loads(Path(entree).read_text(encoding="utf-8"))
    reg, lec = doc["registre"], doc["lecteurs_de_cibles_admis"]
    avant = (len(reg), len(lec))
    if mutation == "retirer-entree":
        del reg[argument]
    elif mutation == "retirer-module":
        for k in [k for k in reg if k.startswith(argument + "::")]:
            del reg[k]
        lec.pop(argument, None)
    elif mutation == "retirer-lecteurs":
        del lec[argument]
    elif mutation == "ajouter-fantome":
        reg[argument] = {"statut": doc["statuts"]["EXEMPT"], "raison": "entrée fantôme de l'épreuve"}
    elif mutation == "ajouter-lecteur-mort":
        module, nom = argument.split("::")
        lec.setdefault(module, []).append(nom)
    else:
        raise SystemExit(f"mutation inconnue : {mutation}")
    if (len(reg), len(lec)) == avant and mutation not in ("ajouter-fantome", "ajouter-lecteur-mort"):
        raise SystemExit("mutation sans effet")
    Path(sortie).write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(mutation, argument, ": registre", avant[0], "->", len(reg), "; modules lecteurs", avant[1], "->", len(lec))


if __name__ == "__main__":
    main(*sys.argv[1:])

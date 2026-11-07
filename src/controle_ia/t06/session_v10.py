"""Chaîne de session de T0.6, v10 (lanceur v11, E3 du 7 novembre ; nom neuf, R12 : `session_v9.py` et les précédents restent tels quels).

Seule différence avec `session_v9.py` : le texte RÉEL que Vast rend pour une instance détruite, relevé en E3 (instance 59623267, fille 6, 22:27:24Z) :
`vastai show instance <ID> --raw` rend, en code 0, `{"instances": null}` (trois lignes). Ce texte, seul, est une **absence probable** et non une absence établie :
`instance_seule` le refuse comme NON CONCLUANT, avec un message qui nomme la cause. L'absence n'est établie que par une liste d'inventaire NON vide qui ne contient pas
l'identifiant, à deux relevés (inchangé dans le lanceur : code de retour 1 de `presente`). `{"id": null}`, un texte 500 et un 404 sans message exact restent non concluants
(`session_v9`).

    python -I -m controle_ia.t06.session_v10 seule REPONSE.json ID    (code 0 répond, 2 non concluant, 4 introuvable établi par le seul texte)
    autres sous-commandes : celles de `session_v9`.
"""
from __future__ import annotations

import json
import sys

from . import session_v9 as s9
from .session import GardeSession

filtre_recherche, choisir_offre, corriger_prix = s9.filtre_recherche, s9.choisir_offre, s9.corriger_prix
verifier_plafond_epreuve, instance_presente = s9.verifier_plafond_epreuve, s9.instance_presente


def absence_probable(texte: str) -> bool:
    """Vrai pour le texte réel d'une instance détruite : un objet dont la seule clé est `instances` et vaut `null`."""
    try:
        v = json.loads(texte.strip())
    except ValueError:
        return False
    return isinstance(v, dict) and list(v) == ["instances"] and v["instances"] is None


def instance_seule(texte: str, ident: str) -> bool:
    if absence_probable(texte):
        raise GardeSession('réponse {"instances": null} : absence probable, établie seulement par une liste d\'inventaire non vide sans l\'instance, à deux relevés : non concluante')
    return s9.instance_seule(texte, ident)


def main(argv: list[str]) -> int:
    if len(argv) == 3 and argv[0] == "seule":
        try:
            texte = open(argv[1], encoding="utf-8", errors="replace").read()
            absente = not instance_seule(texte, argv[2])
        except OSError as e:
            print(f"réponse de show instance illisible ({e.__class__.__name__})")
            return 2
        except GardeSession as e:
            print(str(e))
            return 2
        if absente:
            print(f"instance {argv[2]} INTROUVABLE")
            return 4
        print(f"instance {argv[2]} répond")
        return 0
    return s9.main(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

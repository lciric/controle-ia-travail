"""Fichiers cités par la configuration de la course de dose–réponse, à extraire sur l'instance (amorce v3).

Bibliothèque standard seule : l'amorce l'appelle avec le `python3` de l'image, avant toute installation. Les clés
`piece_jointe`, `consignes_premier_test` et `banque` sont toujours extraites ; `designation_critere_3` l'est quand elle
n'est pas `null` (texte de désignation pour le critère 3, `prereg/G0-critere-3-designation-course-v1.md`, vérifié sur
l'instance par `controles_v2.controler_registre` : sans lui, arrêt après l'installation — défaut de l'amorce v2). Chaque
chemin est relatif au dépôt, sans composant `..`, sans caractère de motif ni fin de ligne ; sinon refus, jamais un repli.
Sortie : un motif d'extraction partielle par ligne, `/<chemin>*` (le compagnon `.sha256` est compris).

    python3 -I -B -c "import sys; sys.path.insert(0, 'src'); from controle_ia.dose_reponse import extraction_v1 as e; sys.exit(e.main(sys.argv[1:]))" CONFIG.json
"""
from __future__ import annotations

import json
import sys
from pathlib import PurePosixPath

CLES_TOUJOURS = ("piece_jointe", "consignes_premier_test", "banque")
CLE_DESIGNATION = "designation_critere_3"


class Refus(ValueError):
    pass


def _chemin(spec, cle: str) -> str:
    if not isinstance(spec, dict) or not isinstance(spec.get("chemin"), str):
        raise Refus(f"{cle} : objet avec un chemin attendu")
    p = spec["chemin"]
    if not p or p.startswith("/") or ".." in PurePosixPath(p).parts or any(c in p for c in "*?[]\n\r\\"):
        raise Refus(f"{cle} : chemin illisible ou hors du dépôt ({p!r})")
    return p


def chemins_cites(config: dict) -> list[str]:
    if not isinstance(config, dict):
        raise Refus("configuration illisible")
    chemins = [_chemin(config.get(k), k) for k in CLES_TOUJOURS]
    if CLE_DESIGNATION not in config:
        raise Refus(f"clé {CLE_DESIGNATION} absente (null ou objet attendu)")
    d = config[CLE_DESIGNATION]
    if d is not None:
        chemins.append(_chemin(d, CLE_DESIGNATION))
    return ["/" + p + "*" for p in chemins]


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("usage : extraction_v1 CONFIG.json")
        return 2
    try:
        with open(argv[0], encoding="utf-8") as f:
            motifs = chemins_cites(json.load(f))
    except (OSError, ValueError) as e:
        print(f"ARRÊT : {e}")
        return 1
    print("\n".join(motifs))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

"""Garde du code qui tournera, v7 : celle de la v2 (`sparks_exp7_nul_v2/garde_code.py`, chargée par son chemin pour rester
importable seule, bibliothèque standard), avec la liste fermée v7 (`sparks_exp7_nul_v7/liste-fermee-v1.txt` : fichiers de
la v2 à la v7 ensemble).

    python -m controle_ia.sparks_exp7_nul_v7.garde_code liste DEPOT COMMIT_CODE
    python -m controle_ia.sparks_exp7_nul_v7.garde_code lancement DEPOT COMMIT_CODE [COMMIT_LANCE]
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_CHEMIN_V2 = Path(__file__).resolve().parents[1] / "sparks_exp7_nul_v2" / "garde_code.py"
_spec = importlib.util.spec_from_file_location("garde_code_v2", _CHEMIN_V2)
g2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(g2)

GardeCode, COMMIT_BASE, CHEMIN_ADDENDUM, lire_liste = g2.GardeCode, g2.COMMIT_BASE, g2.CHEMIN_ADDENDUM, g2.lire_liste
sha256_octets, verifier_lancement, difference = g2.sha256_octets, g2.verifier_lancement, g2.difference
LISTE = "src/controle_ia/sparks_exp7_nul_v7/liste-fermee-v1.txt"


def verifier_liste_fermee(depot: Path, commit: str, base: str = COMMIT_BASE, liste: list[str] | None = None) -> dict:
    if liste is None:
        liste = lire_liste(g2._git(depot, "show", f"{commit}:{LISTE}"))
    return g2.verifier_liste_fermee(depot, commit, base, liste)


def main(argv: list[str]) -> int:
    try:
        if argv[0] == "liste":
            r = verifier_liste_fermee(Path(argv[1]), argv[2])
            print(f"LISTE FERMÉE CONFORME : {r['n_fichiers']} fichiers")
        elif argv[0] == "lancement":
            verifier_liste_fermee(Path(argv[1]), argv[2])
            r = verifier_lancement(Path(argv[1]), argv[2], argv[3] if len(argv) > 3 else "HEAD")
            print(f"LANCEMENT CONFORME : code {r['commit_code'][:12]}, addendum {r['sha256_addendum'][:12]}")
        else:
            raise IndexError
    except (GardeCode, IndexError) as err:
        print(f"CODE REFUSÉ : {err}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

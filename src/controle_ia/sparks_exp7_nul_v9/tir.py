"""Tir réel de SPARKS-EXP7-NUL, v9 : le contrôle de la v5 (`sparks_exp7_nul_v5/tir.py`, chargé par son chemin,
bibliothèque standard), avec en plus le **périmètre** de la ligne de GO (contre-lecture du delta v8, point 17) : il doit
nommer « SPARKS » et « tir » (mot entier, casse indifférente pour « tir »). Une autre ligne de GO valide (par exemple
celle d'une sonde) est refusée.

    python3 -I -B tir.py verifier GO_MD GO_ID PRIX_CARTE PRIX_STOCKAGE MINUTES [AAAA-MM-JJ]   → ECHEANCE_UTC_S=… DEVIS_USD=…
"""
from __future__ import annotations

import importlib.util
import re
import sys
from datetime import date
from pathlib import Path

_V5 = Path(__file__).resolve().parents[1] / "sparks_exp7_nul_v5" / "tir.py"
_s = importlib.util.spec_from_file_location("tir_v5_pour_v9", _V5)
t5 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(t5)

GardeTir, devis_tir, PLAFOND_MAX_USD = t5.GardeTir, t5.devis_tir, t5.PLAFOND_MAX_USD


def verifier_perimetre(chemin: Path, go_id: str) -> str:
    try:
        lignes = t5.go2.lire(chemin)
    except t5.go2.GardeGo as e:
        raise GardeTir(str(e)) from None
    propres = [l for l in lignes if l["id"] == go_id]
    if not propres:
        raise GardeTir(f"{go_id} absent du registre : la mère pose la ligne du tir d'abord")
    p = propres[0]["perimetre"]
    if "SPARKS" not in p or not re.search(r"(?<![A-Za-zÀ-ÿ])tir(?![A-Za-zÀ-ÿ])", p, re.I):
        raise GardeTir(f"{go_id} : périmètre {p!r} : « SPARKS » et « tir » exigés (une autre ligne de GO ne vaut pas)")
    return p


def preparer(chemin_go: Path, go_id: str, prix_carte: float, prix_stockage: float, minutes: int,
             aujourd_hui: date | None = None, maintenant_s: int | None = None) -> dict:
    verifier_perimetre(chemin_go, go_id)
    return t5.preparer(chemin_go, go_id, prix_carte, prix_stockage, minutes, aujourd_hui, maintenant_s)


def main(argv: list[str]) -> int:
    try:
        if argv[0] != "verifier":
            raise IndexError
        j = date.fromisoformat(argv[6]) if len(argv) > 6 else None
        r = preparer(Path(argv[1]), argv[2], float(argv[3]), float(argv[4]), int(argv[5]), j)
        print(f"ECHEANCE_UTC_S={r['echeance_utc_s']} DEVIS_USD={r['devis_usd']} PLAFOND_USD={r['plafond_usd']:g}")
    except (GardeTir, IndexError, ValueError) as err:
        print(f"TIR REFUSÉ : {err}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

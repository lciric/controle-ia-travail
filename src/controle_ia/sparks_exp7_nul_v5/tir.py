"""Tir réel de la minuterie et des redémarrages de SPARKS-EXP7-NUL, avant le scellement (R-1477 ; contre-lecture du delta
v4, points 4, 23 et 24). Bibliothèque standard seule (lue par le lanceur avant toute installation).

Le tir tourne sous une **ligne de GO à part** (`GO_ID` en paramètre, posée par la mère) : type « calcul », accordée par
Lazar, dans sa validité, non révoquée, plafond écrit **au plus 5 USD**. Le devis du tir doit tenir sous ce plafond :

    devis = prix de la carte × (durée de tir + 15 min de relance + 10 min de marge) / 60
          + prix du stockage × (durée de tir + 60 min) / 60

La durée de tir est l'échéance courte de la minuterie : de 20 à 30 minutes après la création.

    python3 -I -B tir.py verifier GO_MD GO_ID PRIX_CARTE PRIX_STOCKAGE MINUTES [AAAA-MM-JJ]   → ECHEANCE_UTC_S=… DEVIS_USD=…
"""
from __future__ import annotations

import importlib.util
import re
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path

_V2 = Path(__file__).resolve().parents[1] / "sparks_exp7_nul_v2" / "go.py"
_s = importlib.util.spec_from_file_location("go_v2_tir", _V2)
go2 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(go2)

PLAFOND_MAX_USD = 5.0
MINUTES_MIN, MINUTES_MAX = 20, 30
RELANCE_MIN, MARGE_MIN, STOCKAGE_EN_PLUS_MIN = 15, 10, 60


class GardeTir(RuntimeError):
    pass


def verifier_go_tir(chemin: Path, go_id: str, aujourd_hui: date | None = None) -> float:
    """Plafond (USD) de la ligne de GO du tir, après contrôle ; refus sinon."""
    if not re.fullmatch(r"GO-\d{4}-\d{2}-\d{2}-\d{2}", go_id or ""):
        raise GardeTir(f"GO_ID {go_id!r} illisible")
    j = aujourd_hui or datetime.now(timezone.utc).date()
    try:
        lignes = go2.lire(chemin)
    except go2.GardeGo as e:
        raise GardeTir(str(e)) from None
    propres = [l for l in lignes if l["id"] == go_id]
    if not propres:
        raise GardeTir(f"{go_id} absent du registre : la mère pose la ligne du tir d'abord")
    g = propres[0]
    if g["type"] != "calcul" or g["par"] != "Lazar":
        raise GardeTir(f"{go_id} : type {g['type']!r} ou auteur {g['par']!r} (calcul, Lazar attendus)")
    m = re.fullmatch(r"(\d+(?:[.,]\d+)?)\s*USD", g["plafond"])
    if not m:
        raise GardeTir(f"{go_id} : plafond {g['plafond']!r} illisible")
    plafond = float(m.group(1).replace(",", "."))
    if plafond > PLAFOND_MAX_USD:
        raise GardeTir(f"{go_id} : plafond {plafond:g} USD > {PLAFOND_MAX_USD:g} USD permis pour un tir")
    try:
        a, e = date.fromisoformat(g["accorde"]), date.fromisoformat(g["echeance"])
    except ValueError:
        raise GardeTir(f"{go_id} : dates illisibles") from None
    if not a <= j <= e:
        raise GardeTir(f"{go_id} : hors de sa validité ({a} → {e}) le {j}")
    if [l for l in lignes if l["type"] == "révocation" and (go_id in l["perimetre"] or go_id in l["ref"])]:
        raise GardeTir(f"{go_id} révoqué")
    return plafond


def devis_tir(prix_carte: float, prix_stockage: float, minutes: int) -> float:
    if prix_carte <= 0 or prix_stockage < 0:
        raise GardeTir("prix illisibles")
    if not MINUTES_MIN <= int(minutes) <= MINUTES_MAX:
        raise GardeTir(f"durée de tir {minutes} min hors de [{MINUTES_MIN} ; {MINUTES_MAX}]")
    return (prix_carte * (minutes + RELANCE_MIN + MARGE_MIN) / 60
            + prix_stockage * (minutes + STOCKAGE_EN_PLUS_MIN) / 60)


def preparer(chemin_go: Path, go_id: str, prix_carte: float, prix_stockage: float, minutes: int,
             aujourd_hui: date | None = None, maintenant_s: int | None = None) -> dict:
    plafond = verifier_go_tir(chemin_go, go_id, aujourd_hui)
    d = devis_tir(prix_carte, prix_stockage, minutes)
    if d > plafond:
        raise GardeTir(f"devis du tir {d:.2f} USD > plafond {plafond:g} USD de {go_id}")
    now = int(time.time()) if maintenant_s is None else maintenant_s
    return {"plafond_usd": plafond, "devis_usd": round(d, 4), "echeance_utc_s": now + int(minutes) * 60}


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

"""Vérification du GO de dépense avant toute création d'instance (consigne du développeur, point 6).

Exige dans `registres/go.md` la ligne `GO-2026-11-04-04` : type « calcul », plafond « 25 USD », accordée par Lazar,
date du jour entre l'accord et l'échéance, aucune ligne de type « révocation » qui la cite. Même lecture du tableau
que la garde `.claude/hooks/garde_calcul.py` (8 colonnes). Usage :

    python -m controle_ia.sparks_exp7_nul_v1.go registres/go.md [AAAA-MM-JJ]
"""
from __future__ import annotations

import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

GO_ID = "GO-2026-11-04-04"
PLAFOND_USD = 25.0
LIGNE_GO = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")


class GardeGo(RuntimeError):
    pass


def lire(chemin: Path) -> list[dict]:
    if not Path(chemin).is_file():
        raise GardeGo(f"registre {chemin} absent")
    lignes = []
    for n, l in enumerate(Path(chemin).read_text(encoding="utf-8").splitlines(), 1):
        if not LIGNE_GO.match(l):
            continue
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) != 8:
            raise GardeGo(f"ligne {n} : 8 colonnes attendues, {len(c)}")
        lignes.append(dict(zip(("id", "accorde", "type", "perimetre", "plafond", "echeance", "par", "ref"), c)))
    return lignes


def verifier(chemin: Path, aujourd_hui: date | None = None, go_id: str = GO_ID, plafond: float = PLAFOND_USD) -> dict:
    j = aujourd_hui or datetime.now(timezone.utc).date()
    lignes = lire(chemin)
    propres = [l for l in lignes if l["id"] == go_id]
    if not propres:
        raise GardeGo(f"{go_id} absent du registre")
    g = propres[0]   # la validité reste celle de la première ligne (extensions éventuelles ignorées)
    if g["type"] != "calcul":
        raise GardeGo(f"{go_id} : type {g['type']!r}, « calcul » attendu")
    if g["par"] != "Lazar":
        raise GardeGo(f"{go_id} : non accordé par Lazar")
    m = re.fullmatch(r"(\d+(?:[.,]\d+)?)\s*USD", g["plafond"])
    if not m or float(m.group(1).replace(",", ".")) != plafond:
        raise GardeGo(f"{go_id} : plafond {g['plafond']!r}, « {plafond:g} USD » attendu")
    try:
        a, e = date.fromisoformat(g["accorde"]), date.fromisoformat(g["echeance"])
    except ValueError:
        raise GardeGo(f"{go_id} : dates illisibles") from None
    if not a <= j <= e:
        raise GardeGo(f"{go_id} : hors de sa validité ({a} → {e}) le {j}")
    rev = [l["id"] for l in lignes if l["type"] == "révocation" and (go_id in l["perimetre"] or go_id in l["ref"])]
    if rev:
        raise GardeGo(f"{go_id} révoqué par {', '.join(rev)}")
    return {"go": go_id, "plafond_usd": plafond, "echeance": str(e), "verifie_le": str(j)}


def main(argv: list[str]) -> int:
    try:
        r = verifier(Path(argv[0]), date.fromisoformat(argv[1]) if len(argv) > 1 else None)
    except (GardeGo, IndexError) as err:
        print(f"GO REFUSÉ : {err}", file=sys.stderr)
        return 2
    print(f"GO CONFORME : {r['go']} plafond {r['plafond_usd']:g} USD échéance {r['echeance']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

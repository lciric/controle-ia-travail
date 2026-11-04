"""Vérification du GO de dépense avant toute création d'instance, pour l'addendum n° 1 (version neuve de
`sparks_exp7_nul_v1/go.py`, R12 ; contre-lecture de l'addendum, point 28).

Exige dans `registres/go.md`, pour `GO-2026-11-04-04` :
- la **ligne de base** (la première à cet identifiant) : type « calcul », plafond « 25 USD », accordée par Lazar ;
- **et** une **ligne d'extension** au même identifiant, plafond « 40 USD », selon la règle R-389 (celle de
  `.claude/hooks/garde_calcul.py`) : périmètre qui commence par « extension », même type, accordée par Lazar, ni
  antérieure à la première ni d'échéance plus lointaine ; la validité (dates) reste celle de la première ligne ;
- la date du jour entre l'accord et l'échéance de la première ligne ; aucune ligne de type « révocation » qui cite
  l'identifiant.
Toute autre ligne au même identifiant (doublon qui n'est pas une extension conforme) refuse. Bibliothèque standard
seule (l'amorce l'importe avant toute installation). Usage :

    python -m controle_ia.sparks_exp7_nul_v2.go registres/go.md [AAAA-MM-JJ]
"""
from __future__ import annotations

import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

GO_ID = "GO-2026-11-04-04"
PLAFOND_BASE_USD = 25.0
PLAFOND_USD = 40.0
LIGNE_GO = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")
COLONNES = ("id", "accorde", "type", "perimetre", "plafond", "echeance", "par", "ref")


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
        lignes.append(dict(zip(COLONNES, c), ligne=n))
    return lignes


def _plafond(g: dict) -> float | None:
    m = re.fullmatch(r"(\d+(?:[.,]\d+)?)\s*USD", g["plafond"])
    return float(m.group(1).replace(",", ".")) if m else None


def _date(s: str, quoi: str) -> date:
    try:
        return date.fromisoformat(s)
    except ValueError:
        raise GardeGo(f"{quoi} : date illisible {s!r}") from None


def verifier(chemin: Path, aujourd_hui: date | None = None, go_id: str = GO_ID, plafond: float = PLAFOND_USD,
             plafond_base: float = PLAFOND_BASE_USD) -> dict:
    j = aujourd_hui or datetime.now(timezone.utc).date()
    lignes = lire(chemin)
    propres = [l for l in lignes if l["id"] == go_id]
    if not propres:
        raise GardeGo(f"{go_id} absent du registre")
    g, autres = propres[0], propres[1:]
    if g["type"] != "calcul":
        raise GardeGo(f"{go_id} : type {g['type']!r}, « calcul » attendu")
    if g["par"] != "Lazar":
        raise GardeGo(f"{go_id} : non accordé par Lazar")
    if _plafond(g) != plafond_base:
        raise GardeGo(f"{go_id} : plafond de la première ligne {g['plafond']!r}, « {plafond_base:g} USD » attendu")
    a, e = _date(g["accorde"], go_id), _date(g["echeance"], go_id)
    extensions = []
    for x in autres:      # règle R-389 : toute ligne de plus au même identifiant est une extension conforme, ou refus
        ax, ex = _date(x["accorde"], f"{go_id}, ligne {x['ligne']}"), _date(x["echeance"], f"{go_id}, ligne {x['ligne']}")
        if not (x["perimetre"].lower().startswith("extension") and x["type"] == g["type"] and x["par"] == "Lazar"
                and ax >= a and ex <= e):
            raise GardeGo(f"{go_id} : ligne {x['ligne']} en double, non conforme à la règle des extensions (R-389)")
        extensions.append(x)
    ext40 = [x for x in extensions if _plafond(x) == plafond]
    if not ext40:
        raise GardeGo(f"{go_id} : aucune ligne d'extension à « {plafond:g} USD »")
    if not a <= j <= e:
        raise GardeGo(f"{go_id} : hors de sa validité ({a} → {e}) le {j}")
    rev = [l["id"] for l in lignes if l["type"] == "révocation" and (go_id in l["perimetre"] or go_id in l["ref"])]
    if rev:
        raise GardeGo(f"{go_id} révoqué par {', '.join(rev)}")
    return {"go": go_id, "plafond_usd": plafond, "echeance": str(e), "verifie_le": str(j),
            "lignes": [g["ligne"]] + [x["ligne"] for x in extensions], "ligne_extension": ext40[-1]["ligne"]}


def main(argv: list[str]) -> int:
    try:
        r = verifier(Path(argv[0]), date.fromisoformat(argv[1]) if len(argv) > 1 else None)
    except (GardeGo, IndexError, ValueError) as err:
        print(f"GO REFUSÉ : {err}", file=sys.stderr)
        return 2
    print(f"GO CONFORME : {r['go']} plafond {r['plafond_usd']:g} USD (ligne d'extension {r['ligne_extension']}) "
          f"échéance {r['echeance']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

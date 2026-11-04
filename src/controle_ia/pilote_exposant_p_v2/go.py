"""Vérification d'un GO de calcul dans `registres/go.md`, par l'amorce, avant toute création d'instance (contre-lecture
R2, I7 et couple P20 ; consigne du brouillon 2, B6). Bibliothèque standard seulement : l'amorce l'appelle avant toute
installation.

Règles (format du registre : 8 colonnes, `| id | accordé le | type | périmètre | plafond | échéance | accordé par |
référence |`, lu comme le lit la garde `.claude/hooks/garde_calcul.py`) :
- l'identifiant cité existe une seule fois (un doublon de cet identifiant arrête ; les doublons d'autres identifiants
  sont rapportés, jamais tus) ;
- type « calcul » ; accordé par « Lazar » ; date du jour dans [accordé le ; échéance] ;
- aucune ligne de type « révocation » ne le cite (périmètre ou référence) ;
- plafond lisible en USD, au moins égal au pire cas du devis ;
- périmètre qui nomme l'étude (« exposant p ») : un GO d'une autre étude ne vaut pas.

    python -I -B -m controle_ia.pilote_exposant_p_v2.go --registre F --go-id GO-AAAA-MM-JJ-NN --montant 16 [--date D]
Sortie : une ligne JSON ; code 0 si le GO vaut, 1 sinon (motif dans la ligne).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

LIGNE_GO = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")
FORMAT_ID = re.compile(r"^GO-\d{4}-\d{2}-\d{2}-\d{2}$")
MONTANT = re.compile(r"(\d+(?:[.,]\d+)?)\s*USD")
ETUDE = "exposant p"


class GoInvalide(Exception):
    """Le GO cité ne vaut pas pour ce lancement."""


def lire(texte: str) -> tuple[list[dict], list[str]]:
    lignes, problemes = [], []
    for n, ligne in enumerate(texte.splitlines(), 1):
        if not LIGNE_GO.match(ligne):
            continue
        c = [x.strip() for x in ligne.strip().strip("|").split("|")]
        if len(c) != 8:
            problemes.append(f"ligne {n} : {len(c)} colonnes au lieu de 8")
            continue
        lignes.append({"n": n, "id": c[0], "accorde": c[1], "type": c[2], "perimetre": c[3], "plafond": c[4],
                       "echeance": c[5], "par": c[6], "ref": c[7]})
    return lignes, problemes


def verifier(texte: str, go_id: str, montant_min: float, aujourd_hui: date, etude: str = ETUDE) -> dict:
    if not FORMAT_ID.match(go_id or ""):
        raise GoInvalide(f"identifiant de GO {go_id!r} illisible (GO-AAAA-MM-JJ-NN)")
    lignes, problemes = lire(texte)
    trouvees = [x for x in lignes if x["id"] == go_id]
    if not trouvees:
        raise GoInvalide(f"{go_id} absent du registre" + (f" (lignes illisibles : {problemes})" if problemes else ""))
    if len(trouvees) > 1:
        raise GoInvalide(f"{go_id} en double dans le registre (lignes {[x['n'] for x in trouvees]})")
    g = trouvees[0]
    if g["type"] != "calcul":
        raise GoInvalide(f"{go_id} est de type « {g['type']} », pas « calcul »")
    if g["par"] != "Lazar":
        raise GoInvalide(f"{go_id} n'est pas accordé par Lazar")
    try:
        a, e = date.fromisoformat(g["accorde"]), date.fromisoformat(g["echeance"])
    except ValueError:
        raise GoInvalide(f"{go_id} : dates illisibles") from None
    if not a <= aujourd_hui <= e:
        raise GoInvalide(f"{go_id} hors de sa période de validité ({a} → {e} ; aujourd'hui {aujourd_hui})")
    rev = [x["id"] for x in lignes if x["type"] == "révocation" and (go_id in x["perimetre"] or go_id in x["ref"])]
    if rev:
        raise GoInvalide(f"{go_id} révoqué par {', '.join(rev)}")
    m = MONTANT.search(g["plafond"])
    if not m:
        raise GoInvalide(f"{go_id} : plafond « {g['plafond']} » sans montant lisible en USD")
    plafond = float(m.group(1).replace(",", "."))
    if plafond < montant_min:
        raise GoInvalide(f"{go_id} : plafond {plafond} USD < pire cas du devis {montant_min} USD")
    if etude.lower() not in g["perimetre"].lower():
        raise GoInvalide(f"{go_id} : le périmètre ne nomme pas l'étude « {etude} »")
    ids = [x["id"] for x in lignes]
    doublons = sorted({i for i in ids if ids.count(i) > 1})
    return {"go_id": go_id, "valide": True, "plafond_usd": plafond, "pire_cas_devis_usd": montant_min,
            "periode": [str(a), str(e)], "aujourd_hui": str(aujourd_hui), "ligne": g["n"],
            "avertissements": ([f"identifiants en double ailleurs dans le registre : {doublons}"] if doublons else [])
            + ([f"lignes illisibles : {problemes}"] if problemes else [])}


def principal(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registre", required=True)
    ap.add_argument("--go-id", required=True)
    ap.add_argument("--montant", type=float, required=True, help="pire cas du devis, USD")
    ap.add_argument("--date", default=None, help="AAAA-MM-JJ (défaut : date UTC du jour)")
    ap.add_argument("--etude", default=ETUDE)
    a = ap.parse_args(argv)
    jour = date.fromisoformat(a.date) if a.date else datetime.now(timezone.utc).date()
    try:
        texte = Path(a.registre).read_text(encoding="utf-8")
        r = verifier(texte, a.go_id, a.montant, jour, a.etude)
    except (GoInvalide, OSError) as e:
        print(json.dumps({"go_id": a.go_id, "valide": False, "motif": str(e)}, ensure_ascii=False))
        return 1
    print(json.dumps(r, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())

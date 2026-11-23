#!/usr/bin/env python3
"""Sonde d'Astra avant la course d'affinage (v11) — version 3.

Version 3 (R12 ; la v2, `scripts/sonde_astra_affinage_v2.py`, `17994492…`, et la v1 restent en place). Écrite le 22 novembre
2026 pour le lanceur v11 de la course d'affinage (pièce de classe B). Ce qui change, et rien d'autre :
1. modèle **`gpt-6.2-astra`** (au lieu de `gpt-6-astra` ; décision « Astra = gpt-6.2-astra », règle de Lazar, branche du compte
   organisme, commit `9fb4cdc60`) : `MODELE_DEMANDE_POLE`, `--modele`, et le modèle servi exigé (`gpt-6.2-astra` ou suffixé
   d'une date) ;
2. prix passés **explicitement** à la commande : `--prix-entree 8 --prix-sortie 40` USD par million (prix relevés de
   `gpt-6.2-astra`, palier jusqu'à 272 000 jetons d'entrée, R-4905 de `registres/decisions.md` sur `main` ; 16 / 60 au-delà,
   jamais atteint par une consigne triviale) ; la v2 laissait la commande à ses défauts (10 / 50), qui ne sont plus les prix
   du modèle ;
3. version écrite au rapport : `sonde_astra_affinage_v3`.
La commande épinglée (`commande_astra_v1.py`, `986cf71e…`) ne change pas ; elle réduit d'elle-même la sortie à ce que le
plafond de 0,05 USD paie au prix donné (environ 1 000 jetons pour cette consigne à 40 USD le million) ; le pire cas reste sous
0,05 USD. Le relais jeté de la sonde doit être lancé aux mêmes prix (8 / 40) : la sonde commune v2
(`scripts/sonde_astra_courses_v2.py`) le contrôle avant l'appel.

Usage : python3 -I -B scripts/sonde_astra_affinage_v3.py COMMANDE_ASTRA URL_RELAIS_JETE PID_RELAIS_JETE SORTIE.json
Code 0 si la sonde passe (code 0 de la commande, coût ≤ 0,05, modèle servi `gpt-6.2-astra` ou suffixé d'une date), 1 sinon,
2 sur un usage refusé. Bibliothèque standard seulement.

Texte de la v2 (en-tête) : voir `scripts/sonde_astra_affinage_v2.py`.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

VERSION = "sonde_astra_affinage_v3"
EMPREINTE_COMMANDE = "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71"
PLAFOND_USD = 0.05
MODELE = "gpt-6.2-astra"
PRIX = ("8", "40")  # USD par million (entrée, sortie), gpt-6.2-astra, R-4905 (palier ≤ 272 000 jetons d'entrée)
CONSIGNE = "Réponds par le seul mot : prêt."
URL_LOCALE = re.compile(r"^http://127\.0\.0\.1:\d{2,5}$")


def date_u() -> str:
    return subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True, timeout=10).stdout.strip()


def sonder(commande: Path, url: str, pid: int, python: str = sys.executable, horodatage=date_u) -> dict:
    h = hashlib.sha256(commande.read_bytes()).hexdigest()
    if h != EMPREINTE_COMMANDE:
        raise ValueError(f"commande d'une autre empreinte ({h[:12]}…) que la commande épinglée")
    if not URL_LOCALE.match(url):
        raise ValueError("adresse du relais jeté hors boucle locale")
    env = {"PATH": "/usr/bin:/bin", "PLAFOND_SESSION_USD": str(PLAFOND_USD), "ROLE_POLE": "proposeur_ideation",
           "MODELE_DEMANDE_POLE": MODELE}
    p = subprocess.run([python, "-I", "-B", str(commande), "--url-relais", url, "--modele", MODELE, "--prix-entree", PRIX[0], "--prix-sortie", PRIX[1], "--max-sortie-jetons", "4096",
                        "--sortie-min-jetons", "16", "--delai-s", "120"], input=CONSIGNE.encode("utf-8"), env=env,
                       capture_output=True, timeout=180)
    lignes = [x for x in p.stdout.decode("utf-8", "replace").splitlines() if x.strip()]
    try:
        o = json.loads(lignes[-1]) if lignes else {}
    except ValueError:
        o = {}
    cout = o.get("cout_usd")
    servi = o.get("modele_servi")
    ok = (p.returncode == 0 and isinstance(cout, (int, float)) and cout <= PLAFOND_USD and isinstance(servi, str)
          and re.fullmatch(re.escape(MODELE) + r"(-\d{4}-?\d{2}-?\d{2})?", servi) is not None)
    return {"version": VERSION, "horodatage_utc": horodatage(), "code": p.returncode, "ok": bool(ok), "cout_usd": cout,
            "modele_servi": servi, "commande_sha256": h, "relais_url": url, "relais_pid": pid, "plafond_usd": PLAFOND_USD,
            "erreur": (o.get("erreur") or "")[:300] if not ok else None, "signale": "appel réel trivial, au plus 0,05 USD (R-3273)"}


def principal(argv: list) -> int:
    if len(argv) != 4:
        print(json.dumps({"refus": "usage : COMMANDE_ASTRA URL_RELAIS_JETE PID_RELAIS_JETE SORTIE.json"}), file=sys.stderr)
        return 2
    sortie = Path(argv[3])
    try:
        if sortie.exists():
            raise ValueError(f"{sortie} existe déjà (R12)")
        res = sonder(Path(argv[0]), argv[1], int(argv[2]))
    except (ValueError, OSError, subprocess.SubprocessError) as e:
        print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    donnees = (json.dumps(res, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(sortie, "xb") as f:
        f.write(donnees)
    with open(str(sortie) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{hashlib.sha256(donnees).hexdigest()}  {sortie.name}\n")
    print(json.dumps({"sonde": str(sortie), "ok": res["ok"], "cout_usd": res["cout_usd"]}, ensure_ascii=False))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(principal(sys.argv[1:]))

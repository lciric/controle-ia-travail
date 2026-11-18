#!/usr/bin/env python3
"""Sonde d'Astra avant la course d'affinage (v6) — version 2.

Version 2 (R12 ; la v1, `cb0266a7…`, reste en place) — contre-lecture de la v5, constat 2 : (a) le relais jeté de la sonde
réservait 0,40 USD par appel (réserve par défaut du relais compatible OpenAI) au-delà de son plafond de 0,05 USD : la sonde
échouait toujours en 402 ; les commandes v6 le lancent avec `--reserve-par-appel 0.01` (le relais réserve alors le pire cas de
la requête, ≤ 0,05 USD, même formule que la commande) ; (b) la sortie n'est plus bornée à 512 jetons (risque de troncature,
qui aurait rendu Astra « absente » sans rien dire de sa fiabilité) : `--max-sortie-jetons 4096`, que la commande réduit
d'elle-même à ce que le plafond de 0,05 USD paie après le pire cas d'entrée (environ 760 jetons pour cette consigne) ; le pire
cas reste sous 0,05 USD. Le reste est la v1.

Texte de la v1 :

Sonde d'Astra avant la course d'affinage (v5) — version 1. R-3273 : Astra n'est déclarée qu'après **un appel trivial** par
sa commande épinglée (`commande_astra_v1.py`, `986cf71e…`), **signalé**, pour **0,05 USD au plus**, par un **relais jeté**
(le relais de la course doit rester neuf : lancé après la sonde, ou distinct).

La sonde ne tient aucune clé : elle lance la commande épinglée (interpréteur courant, `-I -B`) avec un environnement minimal
(`PATH`, `PLAFOND_SESSION_USD=0.05`, `ROLE_POLE=proposeur_ideation`, `MODELE_DEMANDE_POLE=gpt-6-astra`), une consigne
triviale sur l'entrée standard, et des sorties réduites pour que le pire cas tienne sous 0,05 USD au prix de la commande
(10 / 50 USD par million) : en v2, `--max-sortie-jetons 4096 --sortie-min-jetons 16`, réduit par la commande au plafond. Elle lit la dernière
ligne JSON de la commande et écrit, **scellé**, un fichier de résultat : code, coût, modèle servi, empreinte de la commande,
adresse et PID du relais jeté, heure (`date -u`) ; jamais le texte rendu, jamais une clé.

Usage : python3 -I -B scripts/sonde_astra_affinage_v1.py COMMANDE_ASTRA URL_RELAIS_JETE PID_RELAIS_JETE SORTIE.json
Code 0 si la sonde passe (code 0 de la commande, coût ≤ 0,05, modèle servi `gpt-6-astra` ou suffixé d'une date), 1 sinon,
2 sur un usage refusé. Bibliothèque standard seulement.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

VERSION = "sonde_astra_affinage_v2"
EMPREINTE_COMMANDE = "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71"
PLAFOND_USD = 0.05
MODELE = "gpt-6-astra"
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
    p = subprocess.run([python, "-I", "-B", str(commande), "--url-relais", url, "--modele", MODELE, "--max-sortie-jetons", "4096",
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

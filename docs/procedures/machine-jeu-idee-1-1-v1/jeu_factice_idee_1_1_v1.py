#!/usr/bin/env python3
"""Jeu factice de la répétition locale de la machine du jeu relancé de l'idée 1.1, v1.

Remplace `scripts/jouer_idee_1_1_v5.py` dans `repetition_machine_jeu_idee_1_1_v1.sh` seulement (l'amorce refuse
`JEU_FACTICE` hors répétition). N'importe rien du dépôt, ne tire rien, ne calcule rien : il écrit, dans la copie jouet, des
sorties **factices** de même forme que celles du jeu (`runs/<run>/manifeste.json`, `diag/organisme-idees-juge-v1/<run>/`
avec `depart.json`, `lignes/NN-RRRR.json`, `sortie.json` ou `arret.json`), chacune scellée par un compagnon
« <empreinte>  <nom> ». Mêmes gardes de forme que le vrai lanceur : argument `--addendum` exact, arbre propre au départ ;
TERM changé en arrêt écrit (`arret.json`, code 1). Modes (`JEU_FACTICE_MODE`) : `sain` (sortie scellée, code 0) ; `arret`
(arrêt écrit après deux tranches, code 1) ; `faux` (un compagnon faux, code 0) ; `hors` (un fichier écrit hors des deux
dossiers du run, code 0) ; `lent` (`JEU_FACTICE_TRANCHES` tranches d'une seconde, pour la minuterie).
"""
from __future__ import annotations

import hashlib
import json
import os
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ADDENDUM = "prereg/organisme-idee-1-1-poids-du-nul-v2-addendum-empreintes-v1.md"


def sceller(p: Path) -> None:
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    (p.parent / (p.name + ".sha256")).write_text(f"{h}  {p.name}\n", encoding="utf-8")


def ecrire(p: Path, corps) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "x", encoding="utf-8") as f:
        f.write(json.dumps(corps, ensure_ascii=False, sort_keys=True) + "\n")
    sceller(p)


def main() -> int:
    mode = os.environ.get("JEU_FACTICE_MODE", "sain")
    if sys.argv[1:] != ["--addendum", ADDENDUM]:
        print("ARRÊT : argument --addendum attendu exactement", file=sys.stderr)
        return 1
    st = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all"], capture_output=True, text=True)
    if st.returncode != 0 or st.stdout.strip():
        print("ARRÊT : arbre de travail non propre", file=sys.stderr)
        return 1
    run = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-idee-1-1-poids-du-nul-v5"
    ecrire(Path("runs") / run / "manifeste.json", {"factice": True, "run_id": run, "note": "répétition, aucune donnée"})
    d = Path("diag") / "organisme-idees-juge-v1" / run
    ecrire(d / "depart.json", {"factice": True, "run_id": run, "debut_epoch": time.time()})

    def sur_term(signum, frame):
        ecrire(d / "arret.json", {"factice": True, "motif": "signal TERM reçu (répétition)"})
        print("ARRÊT : signal TERM (factice)", file=sys.stderr)
        sys.exit(1)

    signal.signal(signal.SIGTERM, sur_term)
    n = int(os.environ.get("JEU_FACTICE_TRANCHES", "5"))
    for k in range(n):
        ecrire(d / "lignes" / f"00-{k:04d}.json", {"factice": True, "tranche": k})
        if mode == "arret" and k == 1:
            ecrire(d / "arret.json", {"factice": True, "motif": "garde factice (répétition)"})
            print("ARRÊT : garde factice", file=sys.stderr)
            return 1
        time.sleep(1.0 if mode == "lent" else 1.5)
    if mode == "faux":
        (d / "lignes" / "00-0001.json.sha256").write_text("0" * 64 + "  00-0001.json\n", encoding="utf-8")
    if mode == "hors":
        Path("donnees").mkdir(exist_ok=True)
        Path("donnees/hors-du-run-factice.txt").write_text("factice\n", encoding="utf-8")
    ecrire(d / "sortie.json", {"factice": True, "run_id": run, "tranches": n})
    print(json.dumps({"run_id": run, "sortie": "factice", "tranches": n}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

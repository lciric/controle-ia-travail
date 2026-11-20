"""Passage de mutations v5 du code de lecture du barreau 5 (développeur du code de lecture, 20 novembre 2026) : le couple
P1 de la contre-lecture de la seconde programmation (`contre-lecture-seconde-programmation-v1.md`, 35254454…), défait.
Même procédé que `mutations-code-lecture-v4.py` : copie de travail unique ; témoin sans mutation exigé vert ; « attrapée »
si pytest rend le code 1 ; l'« avant » paraît une fois exactement dans le fichier d'origine, sinon « introuvable ».

Usage : python -B mutations-code-lecture-v5.py COPIE BASETEMP  — imprime le bilan en JSON.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

DEPOT = Path(__file__).resolve().parents[6]
L = "src/controle_ia/barreau5_familles/lecture_v1.py"
EL = "tests/test_barreau5_familles_lecture_v1.py"
A_COPIER = ["src", "tests/conftest.py", EL, "prereg/T0.6-organismes-config-7b-v1.json",
            "prereg/T0.6-organismes-config-7b-v1.json.sha256",
            "prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md", "pyproject.toml",
            "docs/sources/invites-2606.08892-v1"]

MUTATIONS = [
    ("P1", L, "P1 défait : le motif « niveau non atteignable » suivi de son ancienne suite",
     '        return {"code": "N", "niveau": None, "motifs": ["niveau non atteignable"]}',
     '        return {"code": "N", "niveau": None, "motifs": ["niveau non atteignable : moins de six familles présentes dans "\n'
     '                                                         "l\'épreuve E3 (liste d\'arrêt, point 13 ; nœud)"]}', [EL]),
]


def jouer(copie: Path, base: Path, nom: str, essais) -> dict:
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHONPATH": str(copie / "src"), "TMPDIR": "/dev/shm",
           "PYTHONDONTWRITEBYTECODE": "1", "HOME": os.environ.get("HOME", "/root")}
    debut = time.time()
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "-x", "--basetemp",
                        str(base / nom), *essais], cwd=str(copie), env=env, capture_output=True, text=True)
    lignes = [x for x in r.stdout.splitlines() if x.strip()]
    echec = [x for x in lignes if x.startswith(("FAILED", "ERROR"))]
    return {"code": r.returncode, "duree_s": round(time.time() - debut, 1), "fin": lignes[-1] if lignes else "",
            "premier_echec": echec[0] if echec else None}


def main(argv: list[str]) -> int:
    copie, base = Path(argv[0]), Path(argv[1])
    if copie.exists():
        raise SystemExit(f"{copie} existe déjà : une seule copie de travail, neuve")
    for rel in A_COPIER:
        s, d = DEPOT / rel, copie / rel
        d.parent.mkdir(parents=True, exist_ok=True)
        if s.is_dir():
            shutil.copytree(s, d, ignore=shutil.ignore_patterns("__pycache__"))
        else:
            shutil.copy2(s, d)
    base.mkdir(parents=True, exist_ok=False)
    bilan = {"temoins": {"EL": jouer(copie, base, "temoin-EL", [EL])}, "mutations": []}
    print(f"témoin EL : code {bilan['temoins']['EL']['code']} ({bilan['temoins']['EL']['fin']})", file=sys.stderr, flush=True)
    if bilan["temoins"]["EL"]["code"] != 0:
        print(json.dumps(bilan, ensure_ascii=False, indent=1))
        raise SystemExit("le témoin sans mutation échoue : aucun compte de mutations")
    for mid, fichier, quoi, avant, apres, essais in MUTATIONS:
        origine = (DEPOT / fichier).read_text(encoding="utf-8")
        x = {"id": mid, "fichier": fichier, "defaut": quoi}
        if origine.count(avant) != 1:
            x.update({"etat": "introuvable", "occurrences": origine.count(avant)})
            bilan["mutations"].append(x)
            print(f"{mid} introuvable", file=sys.stderr, flush=True)
            continue
        cible = copie / fichier
        cible.write_text(origine.replace(avant, apres), encoding="utf-8")
        try:
            r = jouer(copie, base, mid, essais)
        finally:
            cible.write_text(origine, encoding="utf-8")
        etat = "attrapée" if r["code"] == 1 else ("MANQUÉE" if r["code"] == 0 else f"erreur de l'outil (code {r['code']})")
        x.update({"etat": etat, **r})
        bilan["mutations"].append(x)
        print(f"{mid} {etat} ({r['duree_s']} s) {r['premier_echec'] or ''}", file=sys.stderr, flush=True)
    print(json.dumps(bilan, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

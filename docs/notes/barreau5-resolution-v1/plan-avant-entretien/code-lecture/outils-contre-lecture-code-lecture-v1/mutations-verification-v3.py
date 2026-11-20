"""Mutations du contre-lecteur à la vérification du code de lecture v4 du barreau 5 (20 novembre 2026) : trois défauts sur
les couples A (tâches retenues, addendum 1, point 2) et B (borne de la phrase E, point 3).

Même procédé que les outils précédents : une copie de travail sous le bloc-notes ; chaque « avant » exactement une fois ;
attrapée si pytest rend le code 1 ; témoin sans mutation exigé vert ; fichier remis à l'identique.

Usage : python -B mutations-verification-v3.py COPIE BASETEMP
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
A_COPIER = ["src", "tests/conftest.py", EL, "pyproject.toml"]

MUTATIONS = [
    ("Y1", "couple A : chaque membre reprend sa moyenne sur ses propres tâches à coût lisible (l'ancienne lecture)",
     "float(np.mean([par_membre[membre][t] for t in retenues])) if retenues else None",
     "float(np.mean(list(par_membre[membre].values()))) if par_membre[membre] else None"),
    ("Y2", "couple A, cas limite : une famille sans tâche retenue compte pour une différence nulle au lieu d'être absente",
     "float(np.mean([par_membre[membre][t] for t in retenues])) if retenues else None",
     "float(np.mean([par_membre[membre][t] for t in retenues])) if retenues else 0.0"),
    ("Y3", "couple B : la borne de la phrase E vaut Δ_app entier, et non sa moitié",
     "{_x(SEUIL_EMPREINTE * sep['delta_app'])} n'est pas exclue.", "{_x(sep['delta_app'])} n'est pas exclue."),
]


def copier(copie: Path) -> None:
    if copie.exists():
        raise SystemExit(f"{copie} existe déjà : une seule copie de travail, neuve")
    for rel in A_COPIER:
        s, d = DEPOT / rel, copie / rel
        d.parent.mkdir(parents=True, exist_ok=True)
        if s.is_dir():
            shutil.copytree(s, d, ignore=shutil.ignore_patterns("__pycache__"))
        else:
            shutil.copy2(s, d)


def jouer(copie: Path, base: Path, nom: str) -> dict:
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHONPATH": str(copie / "src"), "TMPDIR": "/dev/shm",
           "PYTHONDONTWRITEBYTECODE": "1", "HOME": os.environ.get("HOME", "/root")}
    debut = time.time()
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--basetemp",
                        str(base / nom), EL], cwd=str(copie), env=env, capture_output=True, text=True)
    lignes = [x for x in r.stdout.splitlines() if x.strip()]
    echecs = [x.split("::")[-1].split(" ")[0] for x in lignes if x.startswith("FAILED") or x.startswith("ERROR")]
    return {"code": r.returncode, "duree_s": round(time.time() - debut, 1), "fin": lignes[-1][:200] if lignes else "",
            "essais_en_echec": echecs}


def main(argv: list[str]) -> int:
    copie, base = Path(argv[0]), Path(argv[1])
    copier(copie)
    base.mkdir(parents=True, exist_ok=False)
    temoin = jouer(copie, base, "temoin")
    print(f"témoin : code {temoin['code']} ({temoin['fin']})", flush=True)
    if temoin["code"] != 0:
        raise SystemExit("le témoin sans mutation échoue : aucun compte de mutations")
    origine = (DEPOT / L).read_text(encoding="utf-8")
    bilan = []
    for mid, quoi, avant, apres in MUTATIONS:
        n = origine.count(avant)
        if n != 1:
            bilan.append({"id": mid, "etat": "introuvable", "occurrences": n})
            print(f"{mid} introuvable ({n})", flush=True)
            continue
        (copie / L).write_text(origine.replace(avant, apres), encoding="utf-8")
        try:
            r = jouer(copie, base, mid)
        finally:
            (copie / L).write_text(origine, encoding="utf-8")
        etat = "attrapée" if r["code"] == 1 else ("MANQUÉE" if r["code"] == 0 else f"erreur de l'outil (code {r['code']})")
        bilan.append({"id": mid, "defaut": quoi, "etat": etat, **r})
        print(f"{mid} {etat} ({r['duree_s']} s) : {', '.join(r['essais_en_echec'])}", flush=True)
    print(json.dumps({"jouees": sum(b["etat"] in ("attrapée", "MANQUÉE") for b in bilan),
                      "attrapees": sum(b["etat"] == "attrapée" for b in bilan)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

"""Condition 3 de R-2359 (R-2355) : versions du manifeste de 7b comparées à celles d'un environnement Python (.venv).

Usage (depuis la racine du dépôt de l'hôte de l'auditeur) :
    python3 -I comparer-versions-7b-venv-v1.py RACINE REGISTRE PYTHON_VENV

- REGISTRE : `registres/scellements-v1.md` ; la ligne `RUN-CONFIRMATION-T06` y est lue comme le prescrit la consigne
  scellée de l'audit (§ 4) : ligne commençant par `| RUN-CONFIRMATION-T06 | `, quatre cellules, présente une fois ;
- **avant toute ouverture** : le chemin a la forme `runs/<RUN_7B>/manifeste.json` et `<RUN_7B>` diffère de la course 7a
  (`20261109-070232-t06-reel`) ;
- puis le manifeste est vérifié (compagnon `.sha256` et empreinte de la ligne égaux) ; **seul son champ `versions` est lu
  et affiché** ; aucun autre champ, aucun dossier listé ;
- les versions de PYTHON_VENV sont obtenues par la fonction même de la chaîne (`controle_ia.manifeste.versions`),
  exécutée par cet interprète ;
- sortie : tableau JSON par clé (manifeste, environnement, égal) ; code 0 si toutes les bibliothèques et la version de Python
  sont égales, 1 si une diffère (constat), 2 sur une garde (arrêt, rien comparé). La plateforme est rapportée, non jugée.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

RUN_7A = "20261109-070232-t06-reel"
CLE = "RUN-CONFIRMATION-T06"


class Arret(Exception):
    pass


def lire_ligne(registre: Path) -> tuple[str, str]:
    lignes = [l for l in registre.read_text(encoding="utf-8").splitlines() if l.startswith(f"| {CLE} | ")]
    if len(lignes) != 1:
        raise Arret(f"ligne {CLE} trouvée {len(lignes)} fois (une exigée)")
    cellules = [c.strip() for c in lignes[0].strip().strip("|").split("|")]
    if len(cellules) != 4:
        raise Arret(f"ligne {CLE} : {len(cellules)} cellules (quatre exigées)")
    _, _, chemin, sha = cellules
    if not re.fullmatch(r"[0-9a-f]{64}", sha):
        raise Arret(f"ligne {CLE} : empreinte mal formée")
    return chemin, sha


def controler_chemin(chemin: str) -> str:
    m = re.fullmatch(r"runs/([^/]+)/manifeste\.json", chemin)
    if not m:
        raise Arret(f"chemin de la ligne {CLE} hors de la forme runs/<RUN_7B>/manifeste.json")
    if m.group(1) == RUN_7A:
        raise Arret("la ligne cite la course 7a : arrêt avant toute ouverture")
    return m.group(1)


def versions_manifeste(racine: Path, chemin: str, sha_ligne: str) -> dict:
    p = racine / chemin
    comp = p.with_name(p.name + ".sha256")
    if not p.is_file() or not comp.is_file():
        raise Arret("manifeste ou compagnon absent")
    sha = hashlib.sha256(p.read_bytes()).hexdigest()
    if sha != sha_ligne or comp.read_text(encoding="utf-8").split()[0] != sha:
        raise Arret("empreinte du manifeste différente de la ligne ou du compagnon")
    v = json.loads(p.read_text(encoding="utf-8")).get("versions")
    if not isinstance(v, dict) or not v:
        raise Arret("champ versions absent ou vide")
    return v


def versions_venv(racine: Path, python: str) -> dict:
    code = ("import json, sys; sys.path.insert(0, 'src'); "
            "from controle_ia.manifeste import versions; print(json.dumps(versions()))")
    r = subprocess.run([python, "-I", "-c", code], cwd=racine, capture_output=True, text=True)
    if r.returncode != 0:
        raise Arret(f"interprète {python} : échec ({r.stderr.strip()[-200:]})")
    return json.loads(r.stdout)


def principal(argv: list[str]) -> int:
    if len(argv) != 4:
        print(__doc__)
        return 2
    racine, registre, python = Path(argv[1]), Path(argv[2]), argv[3]
    try:
        chemin, sha = lire_ligne(registre)
        run = controler_chemin(chemin)
        vm = versions_manifeste(racine, chemin, sha)
        vv = versions_venv(racine, python)
    except Arret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 2
    table, differe = [], False
    for k in sorted(set(vm) | set(vv)):
        egal = vm.get(k) == vv.get(k)
        jugee = k != "plateforme"
        if jugee and not egal:
            differe = True
        table.append({"cle": k, "manifeste": vm.get(k), "environnement": vv.get(k), "egal": egal, "jugee": jugee})
    print(json.dumps({"run_7b": run, "ligne": {"chemin": chemin, "sha256": sha}, "python": python,
                      "comparaison": table, "toutes_egales": not differe}, ensure_ascii=False, indent=1))
    return 1 if differe else 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv))

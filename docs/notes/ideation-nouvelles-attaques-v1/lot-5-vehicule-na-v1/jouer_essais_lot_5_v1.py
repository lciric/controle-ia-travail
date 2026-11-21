"""Joue les essais du lot 5 du véhicule NA-1 dans une copie d'application, depuis la racine de l'orchestrateur, et écrit le
journal (noms d'essais relatifs à cette racine, aucun chemin complet).

`python -B jouer_essais_lot_5_v1.py ORCHESTRATOR JOURNAL.txt` ; le journal ne doit pas exister (R12). Aucun réseau,
aucune clé.
"""

import os
import subprocess
import sys

ESSAIS = ("essais/test_na_lot5_v1_lecteur.py", "essais/test_na_lot5_v1_contrat.py", "essais/test_na_lot5_v1_portier.py",
          "essais/test_na_lot5_v1_registre.py", "essais/test_na_lot5_v1_identifiants.py")


def main(argv):
    if len(argv) != 2:
        print("usage : jouer_essais_lot_5_v1.py ORCHESTRATOR JOURNAL.txt", file=sys.stderr)
        return 2
    orch, journal = argv
    if os.path.exists(journal):
        print("journal existant : on n'écrase jamais (R12)", file=sys.stderr)
        return 2
    env = {"PATH": os.environ.get("PATH", ""), "PYTHONDONTWRITEBYTECODE": "1", "LANG": "C.UTF-8"}
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-rA", "-p", "no:cacheprovider", *ESSAIS],
                       cwd=orch, env=env, capture_output=True, text=True)
    with open(journal, "x", encoding="utf-8") as f:
        f.write(r.stdout)
    lignes = [l for l in r.stdout.splitlines() if l.strip()]
    print(lignes[-1] if lignes else "")
    return r.returncode


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

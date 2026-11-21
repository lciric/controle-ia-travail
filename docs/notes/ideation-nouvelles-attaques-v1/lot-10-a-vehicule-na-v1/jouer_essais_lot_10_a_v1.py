"""Joue les essais du lot 10 a dans une copie où le paquet est posé, depuis son dossier `orchestrator` (noms relatifs), et
écrit leur sortie dans un journal neuf (R12).

`python -B jouer_essais_lot_10_a_v1.py COPIE JOURNAL.txt`
"""

import os
import subprocess
import sys


def main(copie, journal):
    if os.path.exists(journal):
        print("journal existant : on n'écrase jamais (R12)", file=sys.stderr)
        return 2
    orch = os.path.join(copie, "orchestrator")
    env = {"PATH": os.environ.get("PATH", ""), "PYTHONDONTWRITEBYTECODE": "1", "LANG": "C.UTF-8"}
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-v", "-p", "no:cacheprovider",
                        "essais/test_na_lot10a_v1_matiere_premiere.py"], cwd=orch, env=env, capture_output=True, text=True)
    sortie = r.stdout.replace(copie, "<copie>")
    with open(journal, "x", encoding="utf-8") as f:
        f.write(sortie)
    print(sortie.strip().splitlines()[-1])
    return r.returncode


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))

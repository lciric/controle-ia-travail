"""Ce que l'interprète factice doit recevoir si le lanceur exécute la commande du complément 1 v3, ses trois chemins remplacés
par RACINE, INTERPRETE et SORTIES : calculé depuis la ligne du complément seule (aucun appel au lanceur), au format de
interprete-factice-v4.sh (cwd=, PYTHONPATH=, puis arg= par argument, le 0e étant l'interprète).
Usage : argv-attendu-v4.py COMPLEMENT RACINE INTERPRETE SORTIES
"""
import sys


def main(args):
    if len(args) != 4:
        print(__doc__)
        return 2
    complement, racine, interprete, sorties = args
    with open(complement, encoding="utf-8") as fh:
        lignes = [l for l in fh.read().split("\n") if l.startswith("env -C ")]
    if len(lignes) != 1:
        print("ÉCHEC : une seule ligne « env -C » attendue dans le complément", file=sys.stderr)
        return 1
    mots = lignes[0].split(" ")
    r0, i0, s0 = mots[8], mots[4], mots[10]

    def sub(m):
        if m == s0:
            return sorties
        if m == i0:
            return interprete
        if m == r0:
            return racine
        if m.startswith(r0 + "/"):
            return racine + m[len(r0):]
        return m

    cwd = sub(mots[2])
    assert mots[3] == "PYTHONPATH=src"
    print(f"cwd={cwd}")
    print("PYTHONPATH=src")
    for m in mots[4:]:
        print(f"arg={sub(m)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

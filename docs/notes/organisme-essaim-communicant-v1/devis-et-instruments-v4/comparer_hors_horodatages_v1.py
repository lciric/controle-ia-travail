#!/usr/bin/env python3
"""Compare deux sorties JSON en ignorant les seuls horodatages (clés `t`, `debut_utc`, `fin_utc`). Bibliothèque standard.
Usage : python -I -B comparer_hors_horodatages_v1.py A.json B.json   → code 0 si égales hors horodatages, 1 sinon."""
import json
import sys

HORODATAGES = {"t", "debut_utc", "fin_utc"}


def nettoyer(x):
    if isinstance(x, dict):
        return {k: nettoyer(v) for k, v in x.items() if k not in HORODATAGES}
    if isinstance(x, list):
        return [nettoyer(v) for v in x]
    return x


def main(argv):
    if len(argv) != 3:
        return 2
    a, b = (nettoyer(json.load(open(p, encoding="utf-8"))) for p in argv[1:])
    egal = a == b
    print(("égales" if egal else "DIFFÉRENTES") + f" hors horodatages : {argv[1]} | {argv[2]}")
    return 0 if egal else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

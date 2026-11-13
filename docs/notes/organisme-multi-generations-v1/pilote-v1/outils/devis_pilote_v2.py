"""Devis du pilote, v2 (R-2506 : 4 mondes MR-2, bras A seul, 16 appels) : reprend `devis_pilote_v1.py` (`99d5d677…`, importé,
inchangé) avec 4 mondes et un bras. Pire = plafonds de session ; attendu = coûts centraux du devis v2 (estimés).
Usage : `python3 -I -B devis_pilote_v2.py SORTIE.json`. Bibliothèque standard ; aucun appel."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import devis_pilote_v1 as D1  # noqa: E402


def main(argv):
    if len(argv) != 2 or os.path.exists(argv[1]):
        print("usage : devis_pilote_v2.py SORTIE.json (neuve)")
        return 2
    D1.MONDES = 4
    res = {"hypotheses": {"mondes": 4, "bras": "A seul", "appels": 16,
                          "plafond_session": {m: D1.D2.PLAFOND_SESSION[m] for m in D1.FAMILLE},
                          "central_proposeur": {m: D1.D2.CENTRAL_PROPOSEUR[m] for m in D1.FAMILLE}},
           "quatre_mondes_bras_A": D1.devis(1)}
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(res, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

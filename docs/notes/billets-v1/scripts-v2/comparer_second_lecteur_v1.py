"""Compare les décisions du second lecteur à celles du premier, après scellement du journal du second.

Rapporte, à part pour les lignes tirées au hasard (seules extrapolables), pour les cas « limite » du
premier lecteur, et pour l'ensemble : accord brut, kappa de Cohen, table de contingence, désaccords.
Usage : comparer_second_lecteur_v1.py JOURNAL_1 JOURNAL_2 ECHANTILLON SORTIE
"""
import json
import sys


def kappa(paires):
    n = len(paires)
    if n == 0:
        return None
    po = sum(a == b for a, b in paires) / n
    p1 = sum(a == "oui" for a, _ in paires) / n
    p2 = sum(b == "oui" for _, b in paires) / n
    pe = p1 * p2 + (1 - p1) * (1 - p2)
    return None if pe == 1 else (po - pe) / (1 - pe)


def bloc(paires, ids):
    t = {f"{a}/{b}": sum((x, y) == (a, b) for x, y in paires) for a in ("oui", "non") for b in ("oui", "non")}
    k = kappa(paires)
    return {
        "n": len(paires),
        "accord_brut": (sum(a == b for a, b in paires) / len(paires)) if paires else None,
        "kappa_de_cohen": k,
        "table_premier/second": t,
        "desaccords": [i for i, (a, b) in zip(ids, paires) if a != b],
    }


def main(j1: str, j2: str, ech: str, sortie: str) -> None:
    un = {d["identifiant"]: d for d in (json.loads(l) for l in open(j1, encoding="utf-8") if l.strip())}
    deux = {d["identifiant"]: d for d in (json.loads(l) for l in open(j2, encoding="utf-8") if l.strip())}
    ids = json.load(open(ech, encoding="utf-8"))["identifiants"]
    manquants = [i for i in ids if i not in deux]
    assert not manquants, f"identifiants sans décision du second lecteur : {manquants[:5]}"
    assert all(deux[i]["decision"] in ("oui", "non") for i in ids), "décision hors de oui / non"
    lim = [i for i in ids if "limite" in (un[i].get("motif") or "").lower()]
    hasard = [i for i in ids if i not in set(lim)]
    p = lambda L: [(un[i]["decision"], deux[i]["decision"]) for i in L]
    res = {
        "version": 1,
        "tires_au_hasard_hors_limite": bloc(p(hasard), hasard),
        "cas_limite_du_premier_lecteur": bloc(p(lim), lim),
        "ensemble": bloc(p(ids), ids),
    }
    json.dump(res, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for nom in ("tires_au_hasard_hors_limite", "cas_limite_du_premier_lecteur", "ensemble"):
        b = res[nom]
        print(nom, "n =", b["n"], "accord brut =", b["accord_brut"], "kappa =", b["kappa_de_cohen"], "désaccords =", len(b["desaccords"]))


if __name__ == "__main__":
    main(*sys.argv[1:5])

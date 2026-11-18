"""Tire l'échantillon relu en aveugle par le second lecteur du tri (mandat du second lecteur, v1).

Entrée : journal du tri du premier lecteur (identifiant, décision, motif). Sortie : identifiants seuls,
mélangés, sans décision ni motif ni marque « limite ». Tous les cas marqués « limite » par le premier
lecteur, plus 72 autres tirés sans remise ; graine écrite dans le mandat avant le tirage (R9).
Usage : tirer_echantillon_second_lecteur_v1.py JOURNAL SORTIE
"""
import json
import sys

import numpy as np

ENTROPIE = 0x5EC0_2026_1118_1830  # écrite dans le mandat avant le tirage
N_AUTRES = 72


def main(journal: str, sortie: str) -> None:
    lignes = [json.loads(l) for l in open(journal, encoding="utf-8") if l.strip()]
    ids = [d["identifiant"] for d in lignes]
    assert len(ids) == len(set(ids)), "identifiant répété dans le journal"
    limites = sorted(d["identifiant"] for d in lignes if "limite" in (d.get("motif") or "").lower())
    autres = sorted(i for i in ids if i not in set(limites))
    assert len(autres) >= N_AUTRES, "pas assez de lignes hors « limite »"
    gen = np.random.default_rng(np.random.SeedSequence(ENTROPIE))
    tires = [autres[k] for k in sorted(gen.choice(len(autres), size=N_AUTRES, replace=False).tolist())]
    tout = limites + tires
    ordre = gen.permutation(len(tout)).tolist()
    json.dump(
        {"version": 1, "entropie": hex(ENTROPIE), "n": len(tout), "identifiants": [tout[k] for k in ordre]},
        open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1,
    )
    print(f"échantillon : {len(tout)} identifiants ({len(limites)} « limite », {len(tires)} autres), écrits sans décision")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

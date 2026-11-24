"""Rejoue les deux tirages d'échantillons codés à la main et vérifie qu'ils coïncident avec les fichiers de codage.

- précision des unités : 60 unités, tâche « precision-unites-v2 » (dérivation v0) ;
- étiquettes « VÉRIFIÉ » : 8 lignes par espèce, tâche « echantillon-verifie » (dérivation v0).
"""
import json
import sys

from audit_commun_v2 import SORTIES, graine


def main():
    U = json.loads((SORTIES / "unites-v1.json").read_text())["unites"]
    rng, _ = graine("precision-unites-v2", derivation="v0")
    idx = sorted(int(i) for i in rng.choice(len(U), 60, replace=False))
    P = json.loads((SORTIES / "precision-unites-v1.json").read_text())
    ok1 = [r["indice"] for r in P["echantillon"]] == idx and all(U[r["indice"]]["id"] == r["id"] for r in P["echantillon"])
    E = json.loads((SORTIES / "erreurs-v1.json").read_text())["verifie_strict"]
    rng, _ = graine("echantillon-verifie", derivation="v0")
    tir = []
    for e in ["argon", "carbon", "neon", "astra", "opus", "fable"]:
        ech = E[e]["echantillon"]
        tir += [(e, int(i)) for i in sorted(rng.choice(len(ech), min(8, len(ech)), replace=False))]
    V = json.loads((SORTIES / "codage-verifie-v1.json").read_text())
    ok2 = [(l["espece"], l["indice"]) for l in V["lignes"]] == tir
    print("précision des unités :", "identique" if ok1 else "DIFFÉRENT")
    print("étiquettes VÉRIFIÉ :", "identique" if ok2 else "DIFFÉRENT")
    return 0 if ok1 and ok2 else 1


if __name__ == "__main__":
    sys.exit(main())

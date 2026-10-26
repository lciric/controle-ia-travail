"""Audit NON préenregistré n° 2 — composition par strate des 10 000 premiers de chaque méthode (part de la précision qui
tient au choix des strates à fort taux de base). Aucune décision n'en dépend ; résultats dans resultats/audit-strates-v1.json."""
import hashlib
import json
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)

import corpus_v1 as co  # noqa: E402

R = "/var/tmp/retrodiction-swanson-v1/sortie/resultats"


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


def main():
    sortie = dict(debut=co.heure_utc(), fichiers_lus={}, decoupages={})
    bilan = json.load(open(f"{R}/scores-bilan-v1.json"))
    sortie["fichiers_lus"]["scores-bilan-v1.json"] = sha(f"{R}/scores-bilan-v1.json")
    for nom in ("principal", "placebo"):
        for k in ("scores", "issues"):
            sortie["fichiers_lus"][f"{k}-{nom}-v1.npz"] = sha(f"{R}/{k}-{nom}-v1.npz")
        sc = dict(np.load(f"{R}/scores-{nom}-v1.npz"))
        y = dict(np.load(f"{R}/issues-{nom}-v1.npz"))["y"].astype(np.int64)
        strates = bilan["decoupages"][nom]["strates"]
        n_strates = len(strates)
        base = np.bincount(sc["strate"], weights=y, minlength=n_strates) / np.maximum(
            np.bincount(sc["strate"], minlength=n_strates), 1)
        res = {}
        for m in ("S", "AA", "RA", "CN", "PA"):
            tete = np.argsort(-sc[m], kind="stable")[:10000]
            compte = np.bincount(sc["strate"][tete], minlength=n_strates)
            positives = np.bincount(sc["strate"][tete], weights=y[tete], minlength=n_strates)
            # précision attendue si la tête gardait sa composition par strate mais tirait au hasard dans chaque strate
            attendu_composition = float(np.sum(compte * base) / 10000)
            res[m] = dict(composition={strates[s]: int(compte[s]) for s in range(n_strates) if compte[s]},
                          positives={strates[s]: int(positives[s]) for s in range(n_strates) if compte[s]},
                          precision_due_a_la_seule_composition=attendu_composition,
                          precision_observee=float(y[tete].mean()))
        sortie["decoupages"][nom] = res
    sortie["fin"] = co.heure_utc()
    chemin = f"{R}/audit-strates-v1.json"
    with open(chemin, "x", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
    with open(chemin + ".sha256", "x") as f:
        f.write(f"{sha(chemin)}  audit-strates-v1.json\n")
    print(json.dumps(sortie, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()

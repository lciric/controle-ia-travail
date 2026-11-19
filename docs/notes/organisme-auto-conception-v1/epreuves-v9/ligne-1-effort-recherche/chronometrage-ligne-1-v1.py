"""Chronométrage seul, pour le devis de temps du préenregistrement de la ligne 1 (version 2).

Aucune issue, aucune richesse, aucun gain n'est lu, gardé ni imprimé : le programme n'imprime que des durées.
Aucun appel de modèle, aucune connexion. Racine de graines 20261119, étrangère aux racines de l'épreuve
(2026111900 à 2026111903). Le dépôt de l'organisme est lu sans y écrire (lancer avec `python3 -B`).

Usage : python3 -B chronometrage-ligne-1-v1.py /chemin/vers/ideation-organism/orchestrator
"""
import random
import sys
import time

sys.path.insert(0, sys.argv[1])
from pole import a_blanc_v59 as A  # noqa: E402
from pole import selection_pari as sp  # noqa: E402

RACINE = 20261119
monde = A.charger_monde(sys.argv[1])
base = {"type": "softmax", "poids": [[0.4, -0.2], [-0.3, 0.5], [0.1, 0.2]], "biais": [0.1, -0.1, 0.0]}
lois = {
    "softmax": base,
    "transformee": {"type": "transformee", "base": base, "puissance": 1.3, "inclinaison": [0.0, 0.2, -0.1]},
    "si_sinon": {"type": "si_sinon", "condition": {"indice": 0, "seuil": 1.3},
                 "si": {"type": "fixe", "probas": [0.75, 0.125, 0.125]},
                 "sinon": {"type": "fixe", "probas": [0.3, 0.3, 0.4]}},
}
for loi in lois.values():
    sp.valider_loi(loi, A.K, A.DIM)

for nom, loi in lois.items():
    n = 20
    t = time.perf_counter()
    for i in range(n):
        A.juger_carte(loi, monde, {}, RACINE, f"chrono-v2|{nom}|{i}")
    print(f"jugement ({A.TIRAGES} tirages, archive vide), loi {nom} : {(time.perf_counter() - t) / n:.4f} seconde par jugement")

for nom, loi in lois.items():
    n = 5
    t = time.perf_counter()
    for i in range(n):
        A.oracle(loi, monde, RACINE + i)
    print(f"oracle de a_blanc_v59 ({A.ORACLE} instances, loi du monde recalculée), loi {nom} : "
          f"{(time.perf_counter() - t) / n:.4f} seconde par carte")

rng = random.Random(RACINE)
instances = sp.tirer_instances(rng, A.ORACLE, A.DIM)
t = time.perf_counter()
P = [sp.proba(monde["loi"], x, [], 0) for x in instances]
print(f"loi du monde sur {A.ORACLE} instances, une fois par monde : {time.perf_counter() - t:.4f} seconde")
for nom, loi in lois.items():
    n = 5
    t = time.perf_counter()
    for i in range(n):
        for x in instances:
            sp.proba(loi, x, [], 0)
    print(f"oracle à loi du monde en cache ({A.ORACLE} évaluations de la carte), loi {nom} : "
          f"{(time.perf_counter() - t) / n:.4f} seconde par carte")

tranche = sp.tirer_instances(rng, A.EPISODES_TRANCHE, A.DIM)
for nom, loi in lois.items():
    n = 50
    t = time.perf_counter()
    for i in range(n):
        for x in tranche:
            sp.proba(loi, x, [], 0)
    print(f"tri sur tranche ({A.EPISODES_TRANCHE} évaluations), loi {nom} : {(time.perf_counter() - t) / n:.5f} seconde par essai")

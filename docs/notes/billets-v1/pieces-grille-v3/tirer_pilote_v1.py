"""Tire les douze billets de l'essai pilote (grille brouillon 3, section 10.2).

Graine écrite dans la grille avant le tirage. Vivier : identifiants de la moitié développement v2
(manifeste, champ `moitie`), triés, hors des billets de développement du marquage 2, hors des billets
cités dans les sections A et B de la grille (champ `billets_cites_sections_A_B` de la sortie du
vérificateur). Ne lit aucun texte.

Usage : python tirer_pilote_v1.py MANIFESTE_V2 MARQUES_2 VERIFICATION_JSON SORTIE_JSON
"""
import hashlib
import json
import sys

import numpy as np

ENTROPIE = 3157736039062014214863425892070428530
N = 12


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main(m2p, marq2p, verp, sortie):
    man = json.load(open(m2p, encoding="utf-8"))
    dev = sorted(b["identifiant"] for b in man["billets"] if b["moitie"] == "developpement")
    classe = {b["identifiant"]: b["classe"] for b in man["billets"]}
    marq2 = {d["identifiant"] for d in json.load(open(marq2p, encoding="utf-8"))["desaccords_dans_le_corpus"]}
    cites = set(json.load(open(verp, encoding="utf-8"))["billets_cites_sections_A_B"])
    vivier = [i for i in dev if i not in marq2 and i not in cites]
    s_principal, s_complement = np.random.SeedSequence(ENTROPIE).spawn(2)
    if len(vivier) >= N:
        idx = np.random.default_rng(s_principal).choice(len(vivier), N, replace=False)
        tires = [vivier[k] for k in idx]
        complement = []
    else:
        tires = list(vivier)
        reste = [i for i in dev if i not in marq2 and i not in vivier]
        idx = np.random.default_rng(s_complement).choice(len(reste), N - len(tires), replace=False)
        complement = [reste[k] for k in idx]
        tires += complement
    res = {
        "version": "v1", "entropie": ENTROPIE, "numpy": np.__version__,
        "manifeste_v2": {"chemin": m2p, "sha256": sha(m2p)},
        "marques2": {"chemin": marq2p, "sha256": sha(marq2p)},
        "verification": {"chemin": verp, "sha256": sha(verp)},
        "vivier": len(vivier), "complement_hors_vivier": complement,
        "billets": tires,
        "classes": {i: classe[i] for i in tires},
    }
    json.dump(res, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"vivier {len(vivier)} ; tirés : {tires}")


if __name__ == "__main__":
    main(*sys.argv[1:5])

#!/usr/bin/env python3
"""Archive (R6) de l'observation du brouillon 1 qui a précédé le changement d'oracle et de seuil de contournement.

Le brouillon 1 déclare, sans fichier : sur l'instance 0 de sa racine d'essai (20261291 / 20261292), δ = 1,6, l'oracle
logistique donnait des poids d'équilibre purs et B ≈ A (« 0,070 contre 0,069 ») ; avec le seuil de contournement 0,5,
le contournement de B était gratuit. Ces lectures ont été faites avec des versions intermédiaires du code, non
conservées (sans attaquant final renforcé). Ce script les **reproduit** avec le code v1 remis (`arene_melange_v1.py`,
inchangé), sur la même racine et la même tâche, pour les quatre combinaisons essayées :
    (a) oracle logistique, seuil 0,5 ; (b) oracle détection, seuil 0,5 ;
    (c) oracle détection, seuil 0,10 (= CONFIG_V1, doit égaler bit à bit la tâche du pilote v2 du brouillon 1) ;
    (d) oracle logistique, seuil 0,10 (« variante logistique » du code v1).
Il n'emploie ni la racine de décision ni les racines de la v2. Sortie : un JSON nouveau (refuse d'écraser).

    PYTHONPATH=src python3 archive-observation-oracle-v1.py SORTIE.json
"""
from __future__ import annotations

import json
import multiprocessing as mp
import sys
import time
from dataclasses import asdict
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))

VARIANTES = {"a_logistique_seuil_0.5": ("logistique", 0.5), "b_detection_seuil_0.5": ("detection", 0.5),
             "c_detection_seuil_0.10": ("detection", 0.10), "d_logistique_seuil_0.10": ("logistique", 0.10)}


def _une(nom):
    import arene_melange_v1 as v1

    oracle, seuil = VARIANTES[nom]
    cfg = v1.replace(v1.CONFIG_V1, entrainement=oracle, seuil_contournement=seuil)
    r = v1.executer_tache(0, 1, v1.RACINE_ESSAI, v1.RACINE_ESSAI_TENUE, cfg)
    return nom, asdict(cfg), r


def sans_temps(x):
    if isinstance(x, dict):
        return {k: sans_temps(v) for k, v in x.items() if "cpu" not in k}
    if isinstance(x, list):
        return [sans_temps(v) for v in x]
    return x


def main(argv):
    import arene_melange_v1 as v1
    from controle_ia.gardes import GardeArret

    if len(argv) != 1:
        print(__doc__)
        return 2
    sortie = Path(argv[0])
    if sortie.exists():
        raise GardeArret(f"{sortie} existe déjà : R12 interdit d'écraser")
    if v1.RACINE_ESSAI != 20261291 or v1.RACINE_ESSAI_TENUE != 20261292:
        raise GardeArret("racines du code v1 inattendues")
    m0 = time.perf_counter()
    with mp.get_context("spawn").Pool(2) as pool:
        res = pool.map(_une, list(VARIANTES), chunksize=1)
    mur = time.perf_counter() - m0
    pilote = json.loads((ICI / "essai-pilote-racine-essai-v2.json").read_text(encoding="utf-8"))
    tache_pilote = next(r for r in pilote["resultats"] if r["instance"] == 0 and r["code_delta"] == 1)
    resume, corps = {}, {}
    for nom, cfg, r in res:
        b = r["bras"]
        resume[nom] = {x: {"V_iii_final": b[x]["V_iii_final"], "cout_fraction": b[x]["cout"]["fraction"],
                           "cout_censure": b[x]["cout"]["censure"], "taux_a_delta": b[x]["cout"]["taux_a_delta"]}
                       for x in "ABCD"}
        resume[nom]["B_poids_finaux"] = b["B"]["poids_finaux"]
        resume[nom]["B_equilibre_pur"] = max(b["B"]["poids_finaux"]) > 1 - 1e-9
        corps[nom] = {"config": cfg, "resultat": r}
    identique = sans_temps(dict(corps["c_detection_seuil_0.10"]["resultat"])) == sans_temps(dict(tache_pilote))
    texte = {"objet": "archive de l'observation du brouillon 1 (oracle et seuil de contournement)",
             "code_v1_sha256": v1._versions()["code_sha256"], "versions": v1._versions(),
             "racine": v1.RACINE_ESSAI, "racine_tenue": v1.RACINE_ESSAI_TENUE, "tache": {"instance": 0, "delta": 1.6},
             "mur_s": mur, "variante_c_identique_au_pilote_v2_hors_temps": identique,
             "resume": resume, "variantes": corps}
    sortie.write_text(json.dumps(texte, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"identique_pilote_v2": identique, "mur_s": round(mur, 1), "resume": resume}, indent=1,
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

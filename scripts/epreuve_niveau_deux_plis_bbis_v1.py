"""Épreuve de niveau de la règle (a) en deux plis de l'étape B bis (`prereg/T0.7-etape-B-bis-v1.md`, « Seuil », avant-dernier
point ; « Liste d'arrêt » ; plan, point 12, clé `bbis/epreuve-niveau`), v1. **Données synthétiques seulement** (aucune donnée de
7a, 7b, T0.7 ni de P3-bis).

Pour chaque cellule de l'épreuve — `nul` (aucun signal : sonde et directions échangeables, sans écart de classe) et
`signal-commun` (la sonde et ses directions portent le même signal, écart de classe 0,5 en unités de bruit) — `n_jeux` jeux
synthétiques de la forme de 7b (64 tâches en deux plis de 32, dix positifs et dix négatifs par tâche, une sonde et `n_directions`
directions appariées par indice entre plis, effets de tâche et de classe communs à toutes les lignes, écart type 0,3), lus par **la
fonction de production** `t07bbis.plis_v1.regle_a` (tirages de `plis_v1.poids_plis`, `n_tirages`) au niveau 99 % ; taux de
fausse lecture « au-dessus » = part des jeux dont la borne basse de D est strictement positive (la sonde y est échangeable avec
ses directions : toute lecture « au-dessus » est fausse). **Règle écrite au texte, appliquée mécaniquement** (`niveau_retenu`) :
si le taux dépasse 0,01 (deux fois le nominal de 0,005) en estimation ponctuelle dans une cellule, le niveau décisif devient
99,5 % ; sinon 99 %. Le coût de calcul sur processeur (secondes murales, secondes de processus du parent, cœurs) est écrit avec le
résultat.

Graines (R9) : `numpy.random.SeedSequence(entropie, spawn_key=(cle_de_tache("bbis/epreuve-niveau"),))`, une graine fille par
cellule, puis une par jeu (`spawn`) ; les données et la graine des tirages d'un jeu en dérivent : le résultat ne dépend pas du
nombre de processus. L'épreuve complète (1 000 jeux par cellule, 800 directions, 2 000 tirages, 64 tâches) se joue **après la
contre-lecture du code**, sous l'entropie inscrite avec `CODE-BBIS` ; une épreuve réduite est marquée « non complète » et ne vaut
pas l'épreuve du texte (la fiche de `CODE-BBIS` la refuse).

Usage : `PYTHONPATH=src python scripts/epreuve_niveau_deux_plis_bbis_v1.py --entropie E --sortie F.json [--jeux 1000]
[--directions 800] [--tirages 2000] [--taches 64] [--processus N] [--essai]` (la sortie est scellée ; elle ne doit pas exister).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from multiprocessing import Pool

import numpy as np

from controle_ia.manifeste import cle_de_tache
from controle_ia.t07bbis import plis_v1 as pv
from controle_ia.t07bbis.commun_v1 import NIVEAU_DECISIF, NIVEAU_DECISIF_REPLI, exiger_entropie

CLE = "bbis/epreuve-niveau"
CELLULES = {"nul": 0.0, "signal-commun": 0.5}
SIGMA_TACHE = 0.3
ACTIONS_PAR_CLASSE = 10
SEUIL_TAUX = 0.01


def jeu_synthetique(ss: np.random.SeedSequence, delta: float, n_taches: int, n_directions: int):
    """Un jeu : par pli, scores (1 + n_directions, actions), étiquettes, codes de tâches ; et la graine des tirages."""
    rng = np.random.default_rng(ss)
    plis = []
    par_pli = n_taches // 2
    for _ in range(2):
        code = np.repeat(np.arange(par_pli), 2 * ACTIONS_PAR_CLASSE)
        y = np.tile(np.r_[np.ones(ACTIONS_PAR_CLASSE, int), np.zeros(ACTIONS_PAR_CLASSE, int)], par_pli)
        u = rng.normal(0.0, SIGMA_TACHE, size=(par_pli, 2))[code, y]          # effets de tâche et de classe, communs
        X = delta * y[None, :] + u[None, :] + rng.standard_normal((1 + n_directions, y.size))
        plis.append((X, y, code))
    return plis, int(rng.integers(0, 2 ** 63 - 1))


def _un(args):
    ss, delta, n_taches, n_directions, n_tirages = args
    plis, graine = jeu_synthetique(ss, delta, n_taches, n_directions)
    j = pv.jeu(plis, [n_taches // 2, n_taches // 2], controle=False)
    W = pv.poids_plis([n_taches // 2, n_taches // 2], n_tirages, graine)
    r = pv.regle_a(j, W, NIVEAU_DECISIF)
    return bool(r["au_dessus"]), float(r["bas"]), float(r["aire"]), float(r["Q"])


def niveau_retenu(taux: dict) -> tuple[float, list]:
    """Règle du texte : un taux > 0,01 (estimation ponctuelle) dans une cellule → 99,5 % ; sinon 99 %."""
    depasse = [n for n, t in taux.items() if float(t) > SEUIL_TAUX]
    return (NIVEAU_DECISIF_REPLI if depasse else NIVEAU_DECISIF), depasse


def jouer(entropie: int, n_jeux: int, n_directions: int, n_tirages: int, n_taches: int, processus: int = 1,
          reelle: bool = True) -> dict:
    exiger_entropie(int(entropie), reelle)
    if n_taches % 2 or n_taches < 4:
        raise SystemExit("nombre pair de tâches, au moins quatre")
    racine = np.random.SeedSequence(int(entropie), spawn_key=(cle_de_tache(CLE),))
    filles = dict(zip(CELLULES, racine.spawn(len(CELLULES))))
    t0, c0 = time.perf_counter(), time.process_time()
    sortie = {"cellules": {}}
    for nom, delta in CELLULES.items():
        taches = [(ss, delta, n_taches, n_directions, n_tirages) for ss in filles[nom].spawn(int(n_jeux))]
        if processus > 1:
            with Pool(int(processus)) as p:
                res = p.map(_un, taches)
        else:
            res = [_un(t) for t in taches]
        n_au_dessus = sum(1 for r in res if r[0])
        sortie["cellules"][nom] = {"delta": delta, "jeux": len(res), "au_dessus": n_au_dessus, "taux": n_au_dessus / len(res),
                                   "bas_max": max(r[1] for r in res), "aire_mediane": float(np.median([r[2] for r in res])),
                                   "Q_median": float(np.median([r[3] for r in res]))}
    niveau, depasse = niveau_retenu({n: c["taux"] for n, c in sortie["cellules"].items()})
    sortie.update({
        "niveau_teste": NIVEAU_DECISIF, "seuil_taux": SEUIL_TAUX, "cellules_au_dela_du_seuil": depasse,
        "niveau_decisif_retenu": niveau,
        "regle": "taux > 0,01 en estimation ponctuelle dans une cellule → niveau décisif 99,5 % ; sinon 99 % (texte, « Seuil »)",
        "parametres": {"jeux_par_cellule": int(n_jeux), "directions": int(n_directions), "tirages": int(n_tirages),
                       "taches": int(n_taches), "actions_par_classe_et_tache": ACTIONS_PAR_CLASSE, "sigma_tache": SIGMA_TACHE,
                       "processus": int(processus)},
        "graine": {"cle": CLE, "spawn_key": [str(cle_de_tache(CLE))], "entropie": str(entropie)},
        "cout": {"secondes_murales": time.perf_counter() - t0, "secondes_processus_parent": time.process_time() - c0,
                 "coeurs_visibles": os.cpu_count(), "processeur": "processeur seulement, 0 USD"},
        "complete": bool(n_jeux >= 1000 and n_directions == 800 and n_tirages == 2000 and n_taches == 64)})
    if not sortie["complete"]:
        sortie["avertissement"] = "épreuve réduite (essai) : ne vaut pas l'épreuve de niveau du texte"
    return sortie


def main(argv=None) -> int:
    from controle_ia.scellement import sceller
    ap = argparse.ArgumentParser(description="épreuve de niveau de la règle (a) en deux plis (B bis)")
    ap.add_argument("--entropie", type=int, required=True)
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--jeux", type=int, default=1000)
    ap.add_argument("--directions", type=int, default=800)
    ap.add_argument("--tirages", type=int, default=2000)
    ap.add_argument("--taches", type=int, default=64)
    ap.add_argument("--processus", type=int, default=1)
    ap.add_argument("--essai", action="store_true", help="entropie courte permise (essais seulement)")
    a = ap.parse_args(argv)
    if os.path.exists(a.sortie):
        raise SystemExit(f"{a.sortie} existe déjà (R12)")
    r = jouer(a.entropie, a.jeux, a.directions, a.tirages, a.taches, a.processus, reelle=not a.essai)
    with open(a.sortie, "x", encoding="utf-8") as f:
        f.write(json.dumps(r, indent=1, ensure_ascii=False, sort_keys=True) + "\n")
    sceller(a.sortie)
    print(json.dumps({k: r[k] for k in ("cellules", "niveau_decisif_retenu", "complete")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

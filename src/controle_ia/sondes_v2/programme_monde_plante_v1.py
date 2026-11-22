"""Programme de l'épreuve à vérité plantée, version 1 (brique D).

Pour chaque taille demandée (unités, tâches, actions par tâche et par source) et chaque monde engagé dans
`verites_mondes_plantes_v1.json` (scellé avant toute exécution), rejoue le monde sur des graines dérivées (R9), lit
chaque réplique avec la brique C, compare mécaniquement les lectures aux vérités engagées, et rapporte, avec
l'intervalle exact de Clopper-Pearson : la **puissance** (part des répliques où une lecture attendue positive est
faite), le **taux de fausse lecture** (part des répliques où une lecture attendue négative est contredite), le taux
d'arrêt des gardes pour le monde-artefact. Le rapport dit donc, pour chaque taille, ce que le programme sait voir.

    python -m controle_ia.sondes_v2.programme_monde_plante_v1 --sortie DOSSIER --taille 6,6,3 [--taille 8,10,4 …]
        [--repliques 20] [--nul 39] [--alpha 0.05] [--seuil-identite 0.9] [--d 256] [--entropie N]
        [--famille difference_moyennes_appariee] [--mondes trace_commune,…]

Sorties (jamais écrasées, R12 ; scellées, R6) : `rapport-monde-plante-v1-<entropie>.json` et le journal des gels.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import asdict
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..scellement import sceller
from . import lecture_v1 as lc
from . import monde_plante_v1 as mp


def _taille(texte: str) -> tuple[int, int, int]:
    try:
        u, t, a = (int(x) for x in texte.split(","))
    except ValueError:
        raise GardeArret(f"taille {texte!r} : « unités,tâches,actions » attendu") from None
    return u, t, a


def executer(sortie, tailles, repliques: int, n_nul: int, alpha: float, seuil_identite: float, d: int,
             entropie: int | None, famille: str = "difference_moyennes_appariee", mondes=None,
             k_externes: int = 5, journal_progres=None) -> Path:
    verites, sha_verites = mp.charger_verites()
    noms = list(verites["mondes"]) if mondes is None else list(mondes)
    inconnus = set(noms) - set(verites["mondes"])
    if inconnus:
        raise GardeArret(f"mondes non engagés : {sorted(inconnus)}")
    if repliques < 1 or n_nul < 1 or not 0.0 < alpha < 1.0:
        raise GardeArret("répliques ≥ 1, nul ≥ 1, 0 < α < 1")
    sortie = Path(sortie)
    sortie.mkdir(parents=True, exist_ok=True)
    taches = [f"{u},{t},{a}/{m}/{r}" for (u, t, a) in tailles for m in noms for r in range(repliques)]
    g = lc.deriver_graines(taches, entropie)
    ent = g[taches[0]]["entropie"]
    chemin = sortie / f"rapport-monde-plante-v1-{ent}.json"
    journal = sortie / f"journal-gels-monde-plante-v1-{ent}.jsonl"
    if chemin.exists() or journal.exists():
        raise GardeArret(f"{chemin} ou son journal existe déjà (R12)")
    rapport = {"format": "rapport-monde-plante-v1", "verites_sha256": sha_verites,
               "arguments": {"tailles": [list(x) for x in tailles], "repliques": repliques, "nul": n_nul,
                             "alpha": alpha, "seuil_identite": seuil_identite, "d": d, "famille": famille,
                             "mondes": noms, "k_externes": k_externes},
               "manifeste": lc.manifeste_lecture({"programme": "programme_monde_plante_v1"}, g), "tailles": {}}
    debut = time.time()
    for taille in tailles:
        cle_t = ",".join(map(str, taille))
        par_monde = {}
        for m in noms:
            p = mp.parametres_du_monde(verites, m, taille, d)
            attendue = verites["mondes"][m]["lecture_attendue"]
            lectures, conformites = [], []
            for r in range(repliques):
                rng = lc.generateur(g[f"{cle_t}/{m}/{r}"])
                res = mp.lire_monde(p, rng, journal, f"{cle_t}/{m}/{r}", alpha, seuil_identite, n_nul, famille,
                                    k_externes)
                lectures.append(res["lectures"])
                conformites.append(mp.comparer(res["lectures"], attendue))
                if journal_progres is not None:
                    journal_progres(f"{cle_t} {m} réplique {r + 1}/{repliques}")
            criteres = {}
            for c, v in attendue.items():
                conformes = sum(x[c] for x in conformites)
                if v["nature"] == "fausse_lecture":
                    x, quoi = repliques - conformes, "taux_fausse_lecture"
                elif v["nature"] == "puissance":
                    x, quoi = conformes, "puissance"
                else:
                    x, quoi = conformes, "taux_arret_garde"
                bas, haut = mp.clopper_pearson(x, repliques)
                criteres[c] = {"nature": v["nature"], "admises": v["admises"], quoi: x / repliques,
                               "compte": x, "repliques": repliques, "intervalle_95": [bas, haut]}
            table = {}
            for c in mp.CRITERES:
                vals = [l.get(c) for l in lectures]
                table[c] = {str(k): vals.count(k) for k in sorted({str(v) for v in vals})}
            par_monde[m] = {"parametres": asdict(p), "criteres": criteres, "table_des_lectures": table}
        rapport["tailles"][cle_t] = par_monde
    rapport["duree_secondes"] = time.time() - debut
    chemin.write_text(json.dumps(rapport, ensure_ascii=False, indent=1, sort_keys=True, allow_nan=False) + "\n",
                      encoding="utf-8")
    sceller(chemin)
    if journal.exists():
        sceller(journal)
    return chemin


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--taille", action="append", required=True, type=_taille)
    ap.add_argument("--repliques", type=int, default=20)
    ap.add_argument("--nul", type=int, default=39)
    ap.add_argument("--alpha", type=float, default=None)
    ap.add_argument("--seuil-identite", type=float, default=None)
    ap.add_argument("--d", type=int, default=256)
    ap.add_argument("--entropie", type=int, default=None)
    ap.add_argument("--famille", default="difference_moyennes_appariee")
    ap.add_argument("--mondes", default=None)
    ap.add_argument("--k-externes", type=int, default=5)
    a = ap.parse_args(argv)
    v, _ = mp.charger_verites()
    chemin = executer(a.sortie, a.taille, a.repliques, a.nul,
                      v["alpha_par_defaut"] if a.alpha is None else a.alpha,
                      v["seuil_identite_haute_par_defaut"] if a.seuil_identite is None else a.seuil_identite,
                      a.d, a.entropie, a.famille, None if a.mondes is None else a.mondes.split(","), a.k_externes,
                      journal_progres=lambda m: print(m, file=sys.stderr, flush=True))
    print(chemin)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)

"""Programme de l'épreuve à vérité plantée, version 2 (brique D ; erratum 1, § 6).

Pour chaque effectif demandé (paires, tâches, actions par tâche et par source) et chaque monde engagé dans
`verites_mondes_plantes_v2.json` (scellé et committé avant toute exécution), rejoue le monde sur des graines dérivées
nommées (R9 ; erratum 1, § 5), lit chaque réplique, compare mécaniquement aux vérités engagées et rapporte, avec
l'intervalle exact de Clopper-Pearson à 95 % : la puissance, le taux de fausse lecture, le taux d'arrêt de la garde, et
pour les critères « description » la part de chaque lecture.

    python -m controle_ia.sondes_v2.programme_monde_plante_v2 --sortie DOSSIER --taille 8,8,3 [--taille …]
        [--repliques 500] [--nul 39] [--tirages 2000] [--alpha …] [--u-fort …] [--seuil-identite …] [--d 256]
        [--entropie N] [--mondes a,b] [--k-externes 5]

Sorties scellées, jamais écrasées : `rapport-monde-plante-v2-<entropie>.json` et le journal des gels.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import asdict
from pathlib import Path

from ..gardes import GardeArret
from ..manifeste import graines
from ..scellement import sceller
from . import lecture_v1 as lc
from . import monde_plante_v2 as mp
from . import statistiques_v1 as st


def _taille(texte: str) -> tuple[int, int, int]:
    try:
        u, t, a = (int(x) for x in texte.split(","))
    except ValueError:
        raise GardeArret(f"taille {texte!r} : « paires,tâches,actions » attendu") from None
    return u, t, a


def executer(sortie, tailles, repliques: int, n_nul: int, n_tirages: int, seuils: dict, d: int,
             entropie: int | None, mondes=None, k_externes: int = 5, famille: str = "difference_moyennes_appariee",
             journal_progres=None) -> Path:
    verites, sha = mp.charger_verites()
    noms = list(verites["mondes"]) if mondes is None else list(mondes)
    if set(noms) - set(verites["mondes"]):
        raise GardeArret(f"mondes non engagés : {sorted(set(noms) - set(verites['mondes']))}")
    if repliques < 1 or n_nul < 1 or n_tirages < 1 or not 0.0 < seuils["alpha"] < 1.0:
        raise GardeArret("répliques, nul et tirages ≥ 1 ; 0 < α < 1")
    racine = graines(["racine"], entropie)["racine"]
    ent = int(racine["entropie"])
    sortie = Path(sortie)
    sortie.mkdir(parents=True, exist_ok=True)
    chemin = sortie / f"rapport-monde-plante-v2-{ent}.json"
    journal = sortie / f"journal-gels-monde-plante-v2-{ent}.jsonl"
    if chemin.exists() or journal.exists():
        raise GardeArret(f"{chemin} ou son journal existe déjà (R12)")
    rapport = {"format": "rapport-monde-plante-v2", "verites_sha256": sha,
               "arguments": {"tailles": [list(x) for x in tailles], "repliques": repliques, "nul": n_nul,
                             "tirages": n_tirages, "seuils": seuils, "d": d, "mondes": noms,
                             "k_externes": k_externes, "famille": famille},
               "graines": {"entropie_racine": str(ent), "schema": "manifeste.graines([f'{taille}/{monde}/{r}/{nom}'], "
                           "entropie_racine), nom dans statistiques_v1.GRAINES_NOMMEES"},
               "manifeste": lc.manifeste_lecture({"programme": "programme_monde_plante_v2"}, {"racine": racine}),
               "tailles": {}}
    debut = time.time()
    for taille in tailles:
        cle_t = ",".join(map(str, taille))
        par_monde = {}
        for m in noms:
            p = mp.parametres_du_monde(verites, m, taille, d)
            attendue = verites["mondes"][m]["lecture_attendue"]
            lectures, conformites = [], []
            for r in range(repliques):
                _, rngs = st.generateurs_nommes(ent, f"{cle_t}/{m}/{r}/")
                res = mp.lire_monde(p, rngs, journal, f"{cle_t}/{m}/{r}", seuils, n_nul, n_tirages, famille,
                                    k_externes)
                lectures.append(res["lectures"])
                conformites.append(mp.comparer(res["lectures"], attendue))
                if journal_progres is not None:
                    journal_progres(f"{cle_t} {m} réplique {r + 1}/{repliques}")
            criteres = {}
            for c, v in attendue.items():
                conformes = sum(x[c] for x in conformites)
                quoi, x = {"fausse_lecture": ("taux_fausse_lecture", repliques - conformes),
                           "puissance": ("puissance", conformes), "garde": ("taux_arret_garde", conformes),
                           "description": ("part_admise", conformes)}[v["nature"]]
                criteres[c] = {"nature": v["nature"], "admises": v["admises"], quoi: x / repliques, "compte": x,
                               "repliques": repliques, "intervalle_95": list(mp.clopper_pearson(x, repliques))}
            table = {}
            for c in mp.CRITERES:
                vals = [str(l.get(c)) for l in lectures]
                table[c] = {k: vals.count(k) for k in sorted(set(vals))}
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
    ap.add_argument("--repliques", type=int, default=None)
    ap.add_argument("--nul", type=int, default=39)
    ap.add_argument("--tirages", type=int, default=2000)
    ap.add_argument("--alpha", type=float, default=None)
    ap.add_argument("--u-fort", type=float, default=None)
    ap.add_argument("--seuil-identite", type=float, default=None)
    ap.add_argument("--d", type=int, default=256)
    ap.add_argument("--entropie", type=int, default=None)
    ap.add_argument("--mondes", default=None)
    ap.add_argument("--k-externes", type=int, default=5)
    a = ap.parse_args(argv)
    v, _ = mp.charger_verites()
    dfaut = v["defauts"]
    seuils = {"alpha": dfaut["alpha"] if a.alpha is None else a.alpha,
              "u_fort": dfaut["u_fort"] if a.u_fort is None else a.u_fort,
              "seuil_identite": dfaut["seuil_identite"] if a.seuil_identite is None else a.seuil_identite}
    chemin = executer(a.sortie, a.taille, dfaut["repliques"] if a.repliques is None else a.repliques, a.nul,
                      a.tirages, seuils, a.d, a.entropie, None if a.mondes is None else a.mondes.split(","),
                      a.k_externes, journal_progres=lambda m: print(m, file=sys.stderr, flush=True))
    print(chemin)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)

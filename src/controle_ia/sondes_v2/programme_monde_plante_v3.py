"""Programme de l'épreuve à vérité plantée, version 3 (brique D ; errata 1 et 2 ; texte scellé des diagnostics
préalables, e8dca00b…).

Deux modes, chacun sur les mondes engagés dans `verites_mondes_plantes_v3.json` (scellé avant toute exécution) :
- « complet » (`--taille paires,tâches,actions`, une famille) : toutes les lignes ;
- « étalon » (`--cas paires,familles,tâches,actions`, ou `--grille` : toute la grille engagée, paires 4 à 16,
  familles 1 à 4, tâches 8 à 64, actions 1 ou 2) : étalon de transport par famille, contrôle d'intensité, sonde
  d'identité quand un critère la demande ; une case par combinaison (erratum 2, § 6).
Chaque réplique tire ses graines nommées (statistiques_v1.GRAINES_NOMMEES) d'une entropie racine (R9) ; chaque critère
rend la part admise, son intervalle exact à 95 % et, s'il a une borne, son passage.

    python -m controle_ia.sondes_v2.programme_monde_plante_v3 --sortie DOSSIER (--taille P,T,A | --cas P,F,T,A |
        --grille) [--repliques 500] [--nul 39] [--tirages 2000] [--alpha …] [--u-fort …] [--d 256] [--entropie N]
        [--mondes a,b] [--k-externes 5]

Sorties scellées, jamais écrasées : `rapport-monde-plante-v3-<mode>-<entropie>.json` et le journal des gels.
"""
from __future__ import annotations

import argparse
import itertools
import json
import sys
import time
from pathlib import Path

from ..gardes import GardeArret, etat_git
from ..manifeste import graines
from ..scellement import sceller
from . import lecture_v1 as lc
from . import monde_plante_v3 as mp
from . import statistiques_v1 as st


def _entiers(texte: str, n: int) -> tuple:
    try:
        v = tuple(int(x) for x in texte.split(","))
    except ValueError:
        v = ()
    if len(v) != n:
        raise GardeArret(f"{texte!r} : {n} entiers séparés par des virgules attendus")
    return v


def executer(sortie, mode: str, cas: list[tuple], repliques: int, n_nul: int, n_tirages: int, seuils: dict, d: int,
             entropie: int | None, mondes=None, k_externes: int = 5, famille: str = "difference_moyennes_appariee",
             journal_progres=None, n_nul_identite: int = 200, autoriser_depot_sale: bool = False) -> Path:
    """`cas` : en mode « complet », (paires, tâches, actions) ; en mode « étalon », (paires, familles, tâches,
    actions)."""
    if mode not in ("complet", "etalon"):
        raise GardeArret(f"mode {mode!r}")
    verites, sha = mp.charger_verites()
    noms = [m for m, v in verites["mondes"].items() if mode in v["modes"]] if mondes is None else list(mondes)
    for m in noms:
        if m not in verites["mondes"] or mode not in verites["mondes"][m]["modes"]:
            raise GardeArret(f"monde {m!r} non engagé pour le mode {mode}")
    if repliques < 1 or n_nul < 1 or n_tirages < 1 or not 0.0 < seuils["alpha"] < 1.0:
        raise GardeArret("répliques, nul et tirages ≥ 1 ; 0 < α < 1")
    # R9 (défaut 1 de la contre-lecture) : commit et état du dépôt du code qui tourne ; dépôt sale refusé sauf
    # autorisation explicite, alors consignée en réserve
    git = etat_git(Path(__file__).resolve().parents[3])
    reserves = []
    if not git["propre"]:
        if not autoriser_depot_sale:
            raise GardeArret("arbre de travail non propre : committer avant le run, ou autoriser explicitement")
        reserves.append("arbre de travail non propre au lancement (autorisé explicitement)")
    racine = graines(["racine"], entropie)["racine"]
    ent = int(racine["entropie"])
    sortie = Path(sortie)
    sortie.mkdir(parents=True, exist_ok=True)
    chemin = sortie / f"rapport-monde-plante-v3-{mode}-{ent}.json"
    journal = sortie / f"journal-gels-monde-plante-v3-{mode}-{ent}.jsonl"
    if chemin.exists() or journal.exists():
        raise GardeArret(f"{chemin} ou son journal existe déjà (R12)")
    rapport = {"format": "rapport-monde-plante-v3", "mode": mode, "verites_sha256": sha,
               "arguments": {"cas": [list(x) for x in cas], "repliques": repliques, "nul": n_nul,
                             "tirages": n_tirages, "seuils": seuils, "d": d, "mondes": noms,
                             "k_externes": k_externes, "famille": famille, "nul_identite": n_nul_identite},
               "graines": {"entropie_racine": str(ent), "schema": "manifeste.graines([f'{mode}/{cas}/{monde}/{r}/{nom}'],"
                           " entropie_racine), nom dans statistiques_v1.GRAINES_NOMMEES"},
               "cases": {}}
    rapport["manifeste"] = lc.manifeste_lecture({"programme": "programme_monde_plante_v3", "mode": mode,
                                                 "verites_sha256": sha, **rapport["arguments"]},
                                                {"racine": racine}, git["commit"])
    rapport["manifeste"].update(depot_propre=git["propre"], reserves=reserves)
    debut = time.time()
    for c in cas:
        cle_c = ",".join(map(str, c))
        if mode == "complet":
            n_p, n_f, n_t, n_a = c[0], 1, c[1], c[2]
        else:
            n_p, n_f, n_t, n_a = c
        par_monde = {}
        for m in noms:
            p = mp.parametres(verites, m, n_p, n_f, n_t, n_a, d, mode)
            criteres = [k for k in verites["mondes"][m]["criteres"]
                        if mode == "complet" or k["lecture"] in mp.CRITERES_ETALON]
            avec_id = any(k["lecture"] == "identite" for k in criteres)
            lectures = []
            for r in range(repliques):
                _, rngs = st.generateurs_nommes(ent, f"{mode}/{cle_c}/{m}/{r}/")
                if mode == "complet":
                    lectures.append(mp.lire_monde(p, rngs, journal, f"{cle_c}/{m}/{r}", seuils, n_nul, n_tirages,
                                                  famille, k_externes, n_nul_identite=n_nul_identite))
                else:
                    lectures.append(mp.lire_etalon(p, rngs, seuils, n_tirages, n_nul_identite, avec_id))
                if journal_progres is not None:
                    journal_progres(f"{mode} {cle_c} {m} réplique {r + 1}/{repliques}")
            sortie_c = []
            for k in criteres:  # défaut 4 : un critère engagé dont la lecture manque arrête (aucune omission)
                lues = [l for l in lectures if k["lecture"] in l]
                if not lues:
                    raise GardeArret(f"monde {m} : critère engagé « {k['lecture']} » jamais lu")
                if len(lues) != len(lectures) and k["lecture"] != "fuite" and m != "fuite_de_pli":
                    raise GardeArret(f"monde {m} : critère « {k['lecture']} » manquant dans une réplique")
                oui, n = mp.compter(lues, k)
                sortie_c.append({**k, **mp.passage(oui, n, k)})
            table = {}
            for crit in mp.CRITERES:
                vals = [mp.base_libelle(str(v)) for l in lectures for v in l.get(crit, [])]
                if vals:
                    table[crit] = {x: vals.count(x) for x in sorted(set(vals))}
            par_monde[m] = {"criteres": sortie_c, "table_des_lectures": table}
        rapport["cases"][cle_c] = par_monde
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
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--taille", action="append", type=lambda t: _entiers(t, 3))
    g.add_argument("--cas", action="append", type=lambda t: _entiers(t, 4))
    g.add_argument("--grille", action="store_true")
    ap.add_argument("--repliques", type=int, default=None)
    ap.add_argument("--nul", type=int, default=199)
    ap.add_argument("--tirages", type=int, default=2000)
    ap.add_argument("--alpha", type=float, default=None)
    ap.add_argument("--u-fort", type=float, default=None)
    ap.add_argument("--d", type=int, default=256)
    ap.add_argument("--entropie", type=int, default=None)
    ap.add_argument("--mondes", default=None)
    ap.add_argument("--k-externes", type=int, default=5)
    ap.add_argument("--nul-identite", type=int, default=200)
    ap.add_argument("--autoriser-depot-sale", action="store_true")
    a = ap.parse_args(argv)
    v, _ = mp.charger_verites()
    df = v["defauts"]
    seuils = {"alpha": df["alpha"] if a.alpha is None else a.alpha, "u_fort": df["u_fort"] if a.u_fort is None
              else a.u_fort}
    if a.taille:
        mode, cas = "complet", a.taille
    else:
        gr = v["grille_etalon"]
        mode = "etalon"
        cas = a.cas or list(itertools.product(gr["paires"], gr["familles"], gr["taches"], gr["actions"]))
    chemin = executer(a.sortie, mode, cas, df["repliques"] if a.repliques is None else a.repliques, a.nul,
                      a.tirages, seuils, a.d, a.entropie, None if a.mondes is None else a.mondes.split(","),
                      a.k_externes, journal_progres=lambda m: print(m, file=sys.stderr, flush=True),
                      n_nul_identite=a.nul_identite, autoriser_depot_sale=a.autoriser_depot_sale)
    print(chemin)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)

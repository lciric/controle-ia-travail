"""Audit NON préenregistré (règle de symétrie : ce qui paraît anormal, dans un sens ou dans l'autre, est audité) —
rétrodiction Swanson v1. Aucune décision n'en dépend ; résultats dans resultats/audit-v1.json.

1. Permutations supplémentaires (200) : l'aire moyenne sous permutation des méthodes à score était à −2 à −2,8
   erreurs-types de 0,5 sur 20 permutations (découpage principal) ; fluctuation ou biais ?
2. Part de chaque groupe dans les documents d'avant (explique la domination des strates « physique »).
3. Fraction de la masse de S passant par le top 1 % (explique la petite taille de la strate dominée).
4. Recouvrement des têtes de liste (10 000 premiers) entre méthodes, et fréquence documentaire des termes en tête.
"""
import hashlib
import json
import math
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)

import corpus_v1 as co  # noqa: E402
import mesures_v1 as me  # noqa: E402

R = "/var/tmp/retrodiction-swanson-v1/sortie/resultats"
DONNEES = "/var/tmp/retrodiction-swanson-v1/donnees/arxiv-2003-2016-v1.parquet"
GRAINE_AUDIT = 20261027


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


def main():
    debut = co.heure_utc()
    sortie = dict(debut=debut, graine=dict(entropie=GRAINE_AUDIT), fichiers_lus={}, decoupages={})
    import duckdb

    con = duckdb.connect(config={"autoinstall_known_extensions": False, "autoload_known_extensions": False})
    parts = con.execute("""
        WITH d AS (SELECT id, annee, categories FROM read_parquet(?)
                   QUALIFY row_number() OVER (PARTITION BY id ORDER BY categories, title, abstract) = 1)
        SELECT annee, categories FROM d WHERE annee <= 2010""", [DONNEES]).fetchall()
    con.close()
    from termes_v1 import GROUPES, groupe_de

    for nom, fin in (("principal", 2010), ("placebo", 2006)):
        g = np.bincount([groupe_de(c) for a, c in parts if a <= fin], minlength=7)
        sortie.setdefault("parts_groupes_avant", {})[nom] = {GROUPES[i]: [int(g[i]), float(g[i] / g.sum())]
                                                              for i in range(7)}
    rng = np.random.default_rng(np.random.SeedSequence(GRAINE_AUDIT))
    for nom in ("principal", "placebo"):
        chemins = {k: f"{R}/{k}-{nom}-v1.npz" for k in ("scores", "issues", "vocabulaire")}
        for k, c in chemins.items():
            sortie["fichiers_lus"][os.path.basename(c)] = sha(c)
        sc, iss, voc = (dict(np.load(chemins[k])) for k in ("scores", "issues", "vocabulaire"))
        y = iss["y"].astype(np.int64)
        n = y.size
        res = {}
        # 1. permutations supplémentaires
        methodes = ["S", "AA", "RA", "CN", "PA"]
        ordres = {m: me.Ordre(sc[m]) for m in methodes}
        aires = {m: [] for m in methodes}
        p10 = {m: [] for m in methodes}
        for _ in range(200):
            y_p = y[rng.permutation(n)]
            for m in methodes:
                r_ = me.metriques(ordres[m], y_p, ks=(10000,))
                aires[m].append(r_["aire"])
                p10[m].append(r_["P@10000"])
        n_pos, n_neg = int(y.sum()), int(n - y.sum())
        et_aire = math.sqrt((n_pos + n_neg + 1) / (12.0 * n_pos * n_neg))
        p = n_pos / n
        et_p = math.sqrt(p * (1 - p) / 10000)
        res["permutations_200"] = {m: dict(aire_moyenne=float(np.mean(aires[m])),
                                           ecart_moyenne_en_et=float((np.mean(aires[m]) - 0.5) / (et_aire / math.sqrt(200))),
                                           et_empirique_aire=float(np.std(aires[m], ddof=1)), et_theorique_aire=et_aire,
                                           P10000_moyenne=float(np.mean(p10[m])),
                                           ecart_P10000_en_et=float((np.mean(p10[m]) - p) / (et_p / math.sqrt(200))))
                                   for m in methodes}
        # 3. fraction de la masse de S passant par le top 1 %
        K, Kt = sc["K"], sc["K_top"]
        frac = Kt / K
        res["fraction_masse_top1"] = dict(mediane=float(np.median(frac)), quantile_90=float(np.quantile(frac, 0.9)),
                                          quantile_99=float(np.quantile(frac, 0.99)), maximum=float(frac.max()),
                                          n_superieur_0_5=int(np.sum(frac > 0.5)))
        # 4. recouvrement des têtes et fréquences des termes en tête
        df = voc["df"]
        tetes = {m: set(np.argsort(-sc[m], kind="stable")[:10000].tolist()) for m in methodes}
        res["recouvrement_tetes_10000"] = {f"{a}|{b}": len(tetes[a] & tetes[b]) for i, a in enumerate(methodes)
                                           for b in methodes[i + 1:]}
        res["df_moyen_tete_10000"] = {}
        for m in methodes:
            idx = np.array(sorted(tetes[m]))
            res["df_moyen_tete_10000"][m] = dict(df_A=float(df[sc["A"][idx]].mean()), df_C=float(df[sc["C"][idx]].mean()),
                                                 positives=int(y[idx].sum()))
        res["df_moyen_toutes_paires"] = dict(df_A=float(df[sc["A"]].mean()), df_C=float(df[sc["C"]].mean()))
        tout = np.flatnonzero(y == 1)
        res["df_moyen_positives"] = dict(df_A=float(df[sc["A"][tout]].mean()), df_C=float(df[sc["C"][tout]].mean()))
        sortie["decoupages"][nom] = res
    sortie["fin"] = co.heure_utc()
    chemin = f"{R}/audit-v1.json"
    with open(chemin, "x", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
    with open(chemin + ".sha256", "x") as f:
        f.write(f"{sha(chemin)}  audit-v1.json\n")
    print(json.dumps(sortie, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()

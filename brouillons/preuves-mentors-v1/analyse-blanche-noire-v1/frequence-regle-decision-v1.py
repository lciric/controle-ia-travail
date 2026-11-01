"""Fréquence d'erreur de la règle de décision sous l'hypothèse nulle (contre-lecture 1, point C15).

Répliques synthétiques **sans aucun effet** (générateur jouet des essais, `tests/test_analyse_blanche_noire_v1.py::
_donnees`, forces nulles ; jamais R1, R2, R4), lues par le code v2 (`controle_ia.analyse_blanche_noire`) : bras (i)
(régression sur les activations moyennes, couche par validation interne) et témoin lexical (L), mêmes découpages, même
calibrage, même statistique, même rééchantillonnage des tâches que l'analyse ; comparaison (i) − (L), m = 1.
Deux règles comptées sur les mêmes répliques :
- règle v1 (abandonnée) : valeur p bilatérale de la **différence de puissance** < 0,05 → « établie » ou « contraire » ;
- règle v2 (brouillon 2) : `lecture_v2.ligne_comparaison` (aire d'épisode bilatérale, filtre de signe sur la puissance).
Une « erreur » est un état « établie » ou « contraire » sous le nul ; « non concluante » est compté à part.
Taille réduite (dimension 12, 44 tâches, 2 découpages, 1 000 tirages) : la logique est la même que la taille gelée.
Graines : `SeedSequence` de l'entropie écrite ci-dessous, une graine dérivée par réplique.
Lancement (depuis la racine du dépôt) :
`PYTHONPATH=src:tests python3 brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/frequence-regle-decision-v1.py 200`
"""
import sys
import time
from multiprocessing import Pool

import numpy as np

ENTROPIE = 20261101_2330
CONSTANTES = {"DIMENSION": 12, "TIRAGES": 1000, "DECOUPAGES": 2, "N_PLANCHER": 20}


def replique(i_graine):
    i, graine = i_graine
    from controle_ia.analyse_blanche_noire import constantes as C
    for k, v in CONSTANTES.items():
        setattr(C, k, v)
    from controle_ia.analyse_blanche_noire import evaluation as E
    from controle_ia.analyse_blanche_noire import lecture as L1
    from controle_ia.analyse_blanche_noire import lecture_v2 as LB2
    from controle_ia.analyse_blanche_noire.evaluation_v2 import BrasEntraineV2, difference_v2
    from controle_ia.analyse_blanche_noire.modeles import imputer_cout, traits_lexicaux
    from test_analyse_blanche_noire_v1 import _donnees

    ss = np.random.SeedSequence(ENTROPIE, spawn_key=(i,))
    g_donnees, g_dec, g_tir = ss.spawn(3)
    seed = int(g_donnees.generate_state(1)[0])
    d = _donnees(seed, force_i=0.0, force_juge=0.0, force_cout=0.0)
    t = d["tables"]
    jeu = E.Jeu(t["tache"], t["condition"], t["episode"], t["pas"])
    autres = ("honnete", "temoin", "mention")
    A = d["moyenne"]
    F, _ = traits_lexicaux(t)
    bras = {"i": BrasEntraineV2("i", {c: L1._couche(A, j) for j, c in enumerate(C.COUCHES)}, autres),
            "L": BrasEntraineV2("L", {"traits": lambda l=None: F if l is None else F[l]}, autres, preparer=imputer_cout)}
    rng_dec = np.random.default_rng(g_dec)
    decs = [E.decouper(jeu.taches, rng_dec) for _ in range(C.DECOUPAGES)]
    so = {b: [E.sorties_croisees(jeu, br, p) for p in decs] for b, br in bras.items()}
    Cm = E.comptes_tirages(len(jeu.taches), C.TIRAGES, np.random.default_rng(g_tir))
    mes = {b: E.mesures_bras(jeu, so[b], Cm) for b in so}
    st = C.STATISTIQUE_PRINCIPALE
    res = {b: {s: {k: E.resume(v["point"], v["tirages"]) for k, v in mes[b][s].items()} for s in C.STATISTIQUES}
           for b in mes}
    lu = {"i": True, "L": True}
    comps = LB2.comparer(jeu, mes, res, lu, {}, (("i", "L"),), 1)
    etat_v2 = LB2.ligne_comparaison("i-L", comps["i-L"])[0]
    dp = difference_v2(mes["i"][st]["puissance"], mes["L"][st]["puissance"], 1)
    etat_v1 = "erreur" if dp.get("p_bilaterale", 1.0) < 0.05 else "aucune"
    return {"etat_v2": etat_v2, "etat_v1": etat_v1, "aire_i": res["i"][st]["aire"]["estimation"],
            "aire_L": res["L"][st]["aire"]["estimation"], "fa_i": res["i"][st]["fausses_alarmes"]["estimation"],
            "fa_L": res["L"][st]["fausses_alarmes"]["estimation"], "p_aire": comps["i-L"]["aire"].get("p_bilaterale"),
            "p_puissance": dp.get("p_bilaterale")}


def main(n):
    t0 = time.time()
    with Pool(2) as pool:
        r = pool.map(replique, [(i, None) for i in range(n)])
    v2 = [x["etat_v2"] for x in r]
    err2 = sum(e in ("etablie", "contraire") for e in v2)
    nc = sum(e == "non concluante" for e in v2)
    err1 = sum(x["etat_v1"] == "erreur" for x in r)
    p_a = np.array([x["p_aire"] for x in r], dtype=float)

    def ic(k, n_):                                   # intervalle de Wilson à 95 %
        z, p = 1.959964, k / n_
        c = (p + z * z / (2 * n_)) / (1 + z * z / n_)
        h = z * np.sqrt(p * (1 - p) / n_ + z * z / (4 * n_ * n_)) / (1 + z * z / n_)
        return c - h, c + h
    print("# Sortie de frequence-regle-decision-v1.py (répliques nulles, aucune donnée réelle)")
    print(f"entropie {ENTROPIE} ; constantes réduites {CONSTANTES} ; répliques {n} ; durée {time.time() - t0:.0f} s")
    print(f"règle v2 : erreurs (établie ou contraire) {err2}/{n} = {err2 / n:.4f}, Wilson 95 % "
          f"[{ic(err2, n)[0]:.4f} ; {ic(err2, n)[1]:.4f}] ; non concluantes {nc}/{n}")
    print(f"règle v1 (différence de puissance, p bilatérale < 0,05) : erreurs {err1}/{n} = {err1 / n:.4f}, Wilson 95 % "
          f"[{ic(err1, n)[0]:.4f} ; {ic(err1, n)[1]:.4f}]")
    print(f"valeur p bilatérale de l'aire : part < 0,05 = {np.mean(p_a < 0.05):.4f} ; quantiles 10/50/90 % = "
          f"{np.quantile(p_a, [0.1, 0.5, 0.9]).round(3).tolist()}")
    for k in ("aire_i", "aire_L", "fa_i", "fa_L"):
        v = np.array([x[k] for x in r], dtype=float)
        print(f"{k} : moyenne {v.mean():.4f}, écart type {v.std(ddof=1):.4f}, min {v.min():.4f}, max {v.max():.4f}")
    print("états v2 :", {e: v2.count(e) for e in sorted(set(v2))})


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 200)

"""Fréquence d'erreur de la règle de décision sous l'hypothèse nulle (contre-lecture 1, point C15), v2 : famille de
quatre comparaisons avec le juge (N-029 accordée, R-1086), et famille « R1 seul » ((i) − (L)) sur les mêmes répliques.

Répliques synthétiques **sans aucun effet** (générateur jouet des essais, `tests/test_analyse_blanche_noire_v1.py::
_donnees`, forces nulles ; jamais R1, R2, R4), lues par le code v2 (`controle_ia.analyse_blanche_noire`) : bras (i)
(régression sur les activations moyennes, couche par validation interne), juge (ii) (scores jouets sans effet), sondes
génériques (iii) et témoin lexical (L), mêmes découpages, même calibrage, même statistique, même rééchantillonnage des
tâches que l'analyse ; famille de Holm de quatre comparaisons (i) − (ii), (ii) − (iii) tromperie, (ii) − (iii) enjeux,
(i) − (L), m = 4 ; et famille « R1 seul », (i) − (L), m = 1.
Deux règles comptées sur les mêmes répliques :
- règle abandonnée : Holm sur les valeurs p bilatérales de la **différence de puissance** → rejet = erreur ;
- règle v2 (brouillon 2) : `lecture_v2.ligne_comparaison` (Holm sur l'aire d'épisode bilatérale, filtre de signe sur la
  puissance).
Une « erreur » de famille est au moins une comparaison « établie » ou « contraire » sous le nul ; « non concluante » est
comptée à part.
Taille réduite (dimension 12, 44 tâches, 2 découpages, 1 000 tirages) : la logique est la même que la taille gelée.
Graines : `SeedSequence` de l'entropie écrite ci-dessous, une graine dérivée par réplique.
Lancement (depuis la racine du dépôt) :
`PYTHONPATH=src:tests python3 brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/frequence-regle-decision-v2.py 200`
"""
import sys
import time
from multiprocessing import Pool

import numpy as np

ENTROPIE = 20261102_0005
CONSTANTES = {"DIMENSION": 12, "TIRAGES": 1000, "DECOUPAGES": 2, "N_PLANCHER": 20}


def replique(i_graine):
    i, graine = i_graine
    from controle_ia.analyse_blanche_noire import constantes as C
    for k, v in CONSTANTES.items():
        setattr(C, k, v)
    from controle_ia.analyse_blanche_noire import evaluation as E
    from controle_ia.analyse_blanche_noire import lecture as L1
    from controle_ia.analyse_blanche_noire import constantes_v2 as C2
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
            "L": BrasEntraineV2("L", {"traits": lambda l=None: F if l is None else F[l]}, autres, preparer=imputer_cout),
            "ii": E.BrasFixe("ii", d["juge"]),
            "iii_tromperie": E.BrasFixe("iii_tromperie", t["scores"][:, 0]),
            "iii_enjeux": E.BrasFixe("iii_enjeux", t["scores"][:, 1])}
    rng_dec = np.random.default_rng(g_dec)
    decs = [E.decouper(jeu.taches, rng_dec) for _ in range(C.DECOUPAGES)]
    so = {b: [E.sorties_croisees(jeu, br, p) for p in decs] for b, br in bras.items()}
    Cm = E.comptes_tirages(len(jeu.taches), C.TIRAGES, np.random.default_rng(g_tir))
    mes = {b: E.mesures_bras(jeu, so[b], Cm) for b in so}
    st = C.STATISTIQUE_PRINCIPALE
    res = {b: {s: {k: E.resume(v["point"], v["tirages"]) for k, v in mes[b][s].items()} for s in C.STATISTIQUES}
           for b in mes}
    lu = {b: True for b in bras}
    sortie = {"aire_" + b: res[b][st]["aire"]["estimation"] for b in bras}
    sortie.update({"fa_" + b: res[b][st]["fausses_alarmes"]["estimation"] for b in bras})
    for nom, fam in (("complet", C2.COMPARAISONS_HOLM), ("r1", C2.COMPARAISONS_HOLM_R1_SEUL)):
        comps = LB2.comparer(jeu, mes, res, lu, {}, fam, len(fam))
        sortie["etats_" + nom] = [LB2.ligne_comparaison(k, c)[0] for k, c in comps.items()]
        sortie["p_aire_" + nom] = [c["aire"].get("p_bilaterale") for c in comps.values()]
        pp = {f"{a}-{b}": difference_v2(mes[a][st]["puissance"], mes[b][st]["puissance"], len(fam)).get("p_bilaterale")
              for a, b in fam}
        sortie["ancienne_" + nom] = any(v["rejetee"] for v in E.holm(pp).values())
    return sortie


def main(n):
    t0 = time.time()
    with Pool(2) as pool:
        r = pool.map(replique, [(i, None) for i in range(n)])

    def ic(k, n_):                                   # intervalle de Wilson à 95 %
        z, p = 1.959964, k / n_
        c = (p + z * z / (2 * n_)) / (1 + z * z / n_)
        h = z * np.sqrt(p * (1 - p) / n_ + z * z / (4 * n_ * n_)) / (1 + z * z / n_)
        return f"[{c - h:.4f} ; {c + h:.4f}]"
    print("# Sortie de frequence-regle-decision-v2.py (répliques nulles, aucune donnée réelle)")
    print(f"entropie {ENTROPIE} ; constantes réduites {CONSTANTES} ; répliques {n} ; durée {time.time() - t0:.0f} s")
    for nom, titre in (("complet", "famille de quatre (avec le juge)"), ("r1", "famille « R1 seul », (i) − (L)")):
        err = sum(any(e in ("etablie", "contraire") for e in x["etats_" + nom]) for x in r)
        nc = sum(any(e == "non concluante" for e in x["etats_" + nom]) for x in r)
        anc = sum(x["ancienne_" + nom] for x in r)
        etats = [e for x in r for e in x["etats_" + nom]]
        print(f"{titre} : règle v2 : au moins une établie ou contraire {err}/{n} = {err / n:.4f}, Wilson 95 % "
              f"{ic(err, n)} ; au moins une non concluante {nc}/{n} ; règle abandonnée (Holm sur la puissance) : "
              f"{anc}/{n} = {anc / n:.4f}, Wilson 95 % {ic(anc, n)}")
        print(f"  états : {dict((e, etats.count(e)) for e in sorted(set(etats)))}")
    for k in sorted(x for x in r[0] if x.startswith(("aire_", "fa_"))):
        v = np.array([x[k] for x in r], dtype=float)
        print(f"{k} : moyenne {v.mean():.4f}, écart type {v.std(ddof=1):.4f}, min {v.min():.4f}, max {v.max():.4f}")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 200)

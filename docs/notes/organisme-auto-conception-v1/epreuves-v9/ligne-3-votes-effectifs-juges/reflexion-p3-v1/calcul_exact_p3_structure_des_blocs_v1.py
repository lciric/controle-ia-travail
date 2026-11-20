"""Complément au calcul exact de P3 : le gain d'une pondération dépend-il de la forme des blocs ? — v1.

Le banc ne joue qu'une forme de blocs à cinq juges : {1, 2}, {3, 4}, {5} (loi 4 du texte). Ce complément reprend la
même construction (choc commun à tout le collège avec probabilité ρ / 3 ; sinon, bloc par bloc, tirage commun du
bloc avec probabilité (ρ − ρ / 3) / (1 − ρ / 3)) pour d'autres partitions des cinq juges, **qui ne sont pas au
banc** : elles ne servent qu'à dire si « aucun gain en blocs » tient à la corrélation par blocs en général ou à la
partition choisie. Taux d'erreur égaux et symétriques. Aucun tirage, aucun fichier lu, fractions exactes.

Il importe les fonctions de `calcul_exact_p3_ligne_3_v1.py` (même dossier), sans rien y changer.

Usage : python3 calcul_exact_p3_structure_des_blocs_v1.py SORTIE.json
"""
import json
import platform
import sys
from fractions import Fraction

import calcul_exact_p3_ligne_3_v1 as base

VERSION = "calcul-exact-p3-structure-des-blocs-v1"
PARTITIONS = {
    "2+2+1 (loi 4 du banc)": [[0, 1], [2, 3], [4]],
    "3+1+1": [[0, 1, 2], [3], [4]],
    "2+1+1+1": [[0, 1], [2], [3], [4]],
    "3+2": [[0, 1, 2], [3, 4]],
    "4+1": [[0, 1, 2, 3], [4]],
}
TAUX = [Fraction(1, 10), Fraction(2, 10), Fraction(3, 10)]


def loi_erreurs_partition(partition, pp, rho):
    q_tous = rho / 3
    q_bloc = (rho - rho / 3) / (1 - rho / 3)
    P = {}
    for e in base.ERREURS:
        tous = pp if sum(e) == base.J else (1 - pp if sum(e) == 0 else Fraction(0))
        prod = Fraction(1)
        for bloc in partition:
            eb = [e[j] for j in bloc]
            indep = base.produit(pp if x else 1 - pp for x in eb)
            if len(bloc) == 1:
                prod *= indep
            else:
                commun = pp if all(eb) else (1 - pp if not any(eb) else Fraction(0))
                prod *= q_bloc * commun + (1 - q_bloc) * indep
        P[e] = q_tous * tous + (1 - q_tous) * prod
    if sum(P.values()) != 1:
        raise AssertionError("la loi ne somme pas à 1")
    return P


def cellule(nom, partition, pp, rho):
    E = loi_erreurs_partition(partition, pp, rho)
    Pg = {v: E[tuple(1 - x for x in v)] for v in base.ERREURS}
    Pb = dict(E)
    m, C = base.cov_erreurs(E)
    p = [pp] * base.J
    plantee = base.rho_moyenne_plantee(C, C)
    ee_maj = base.taux(base.quota(3), Pg, Pb)[2]
    bayes = [v for v in base.ERREURS if Pg[v] > Pb[v]]
    ee_bayes = base.taux(bayes, Pg, Pb)[2]
    w, repli, coupe = base.poids_C_population(C, C, p, p)
    acc, eg, seuil = base.regle_lineaire(w, p, p)
    ee_c = base.taux(acc, Pg, Pb)[2]
    ee_c_autre = base.taux(acc + eg, Pg, Pb)[2] if eg else None
    moyenne = sum(w) / base.J
    return {
        "partition": nom, "taux": float(pp), "rho_de_bloc": float(rho), "rho_moyenne_plantee": float(plantee),
        "erreur_equilibree_majorite_stricte": float(ee_maj),
        "erreur_equilibree_regle_de_bayes": float(ee_bayes),
        "majorite_stricte_est_la_regle_de_bayes_exactement": bool(ee_maj == ee_bayes),
        "gain_maximal_de_toute_regle_sur_la_majorite_stricte": float(ee_maj - ee_bayes),
        "bras_C_population_regle": base.nom_de_regle(acc),
        "bras_C_population_poids_rapportes_a_leur_moyenne": [float(x / moyenne) for x in w],
        "bras_C_population_poids_bornes": coupe,
        "bras_C_population_configurations_a_egalite_au_seuil": len(eg),
        "bras_C_population_gain_sur_la_majorite_stricte_lettre": float(ee_maj - ee_c),
        "bras_C_population_gain_sur_la_majorite_stricte_si_bascule": None if ee_c_autre is None else float(ee_maj - ee_c_autre),
    }


def main(argv):
    if len(argv) != 2:
        raise SystemExit("usage : python3 calcul_exact_p3_structure_des_blocs_v1.py SORTIE.json")
    # Garde : la partition 2+2+1 doit rendre la loi 4 du calcul de base, à la fraction près.
    for rho in base.RHOS:
        if loi_erreurs_partition(PARTITIONS["2+2+1 (loi 4 du banc)"], Fraction(2, 10), rho) != base.loi_erreurs(4, [Fraction(2, 10)] * base.J, rho):
            raise AssertionError("garde : la partition 2+2+1 ne rend pas la loi 4")
    cellules = [cellule(nom, part, pp, rho) for nom, part in PARTITIONS.items() for pp in TAUX for rho in base.RHOS]
    synthese = {}
    for nom in PARTITIONS:
        sel = [c for c in cellules if c["partition"] == nom]
        hauts = [c for c in sel if c["rho_de_bloc"] >= 0.6]
        synthese[nom] = {
            "cellules": len(sel),
            "majorite_stricte_est_la_regle_de_bayes_dans_toutes": all(c["majorite_stricte_est_la_regle_de_bayes_exactement"] for c in sel),
            "gain_maximal_de_toute_regle_max_sur_toutes_les_cellules": max(c["gain_maximal_de_toute_regle_sur_la_majorite_stricte"] for c in sel),
            "a_rho_0.6_ou_plus_gain_maximal_de_toute_regle_min_max": [
                min(c["gain_maximal_de_toute_regle_sur_la_majorite_stricte"] for c in hauts),
                max(c["gain_maximal_de_toute_regle_sur_la_majorite_stricte"] for c in hauts)],
            "a_rho_0.6_ou_plus_gain_du_bras_C_en_population_min_max": [
                min(c["bras_C_population_gain_sur_la_majorite_stricte_lettre"] for c in hauts),
                max(c["bras_C_population_gain_sur_la_majorite_stricte_lettre"] for c in hauts)],
        }
    resultat = {
        "version": VERSION,
        "nature": ("calcul exact, fractions exactes ; aucun tirage, aucun fichier lu, aucune mesure de l'étage 1 ; seule la "
                   "partition 2+2+1 est au banc, les autres sont un complément de théorie"),
        "python": platform.python_version(),
        "garde_partition_2_2_1_egale_loi_4": True,
        "synthese": synthese,
        "cellules": cellules,
    }
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=1, sort_keys=True, allow_nan=False)
        f.write("\n")
    print(json.dumps(synthese, ensure_ascii=False, indent=1, sort_keys=True))
    for c in cellules:
        if c["taux"] == 0.2 and c["rho_de_bloc"] in (0.6, 0.9):
            print(c["partition"], "| taux 0,2 | rho", c["rho_de_bloc"], "| EE majorité", round(c["erreur_equilibree_majorite_stricte"], 4),
                  "| EE Bayes", round(c["erreur_equilibree_regle_de_bayes"], 4),
                  "| gain max", round(c["gain_maximal_de_toute_regle_sur_la_majorite_stricte"], 4),
                  "| C pop.", c["bras_C_population_regle"], round(c["bras_C_population_gain_sur_la_majorite_stricte_lettre"], 4),
                  "| poids", [round(x, 3) for x in c["bras_C_population_poids_rapportes_a_leur_moyenne"]])


if __name__ == "__main__":
    main(sys.argv)

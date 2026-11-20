"""Mise en table de la sortie de `calcul_exact_p3_ligne_3_v1.py` — v1.

Lit le seul fichier JSON donné en argument ; n'ajoute aucun calcul de fond (différences et arrondis seulement).
Usage : python3 tableau_calcul_exact_p3_v1.py ENTREE.json SORTIE.md
"""
import json
import sys


def a(x, d=4):
    if x is None:
        return "—"
    return f"{x:.{d}f}".replace(".", ",")


def gain_double(bloc):
    g1 = bloc["gain_sur_la_majorite_stricte_lettre"]
    g2 = bloc["gain_sur_la_majorite_stricte_si_bascule"]
    return a(g1) if g2 is None else f"{a(g1)} / {a(g2)}"


def main(argv):
    if len(argv) != 3:
        raise SystemExit("usage : python3 tableau_calcul_exact_p3_v1.py ENTREE.json SORTIE.md")
    with open(argv[1], encoding="utf-8") as f:
        r = json.load(f)
    lignes = []
    lignes.append("# Table du calcul exact de P3 (cinq juges scriptés, lois 1 et 4) — v1")
    lignes.append("")
    lignes.append(f"Source : sortie de `{r['version']}` ; {r['nature']}.")
    lignes.append("")
    lignes.append("Colonnes : EE = erreur équilibrée. « gain » = EE de la majorité stricte moins EE de la règle (positif : la "
                  "règle fait mieux que la majorité stricte). « Bayes » = la meilleure fonction des cinq votes. « C pop. », "
                  "« P pop. » = règle du bras à étalonnage infini ; deux valeurs « x / y » quand une configuration tombe "
                  "exactement sur le seuil (x : lettre du code, égalité « non notable » ; y : si l'égalité bascule). "
                  "« PE » = bras « poids égaux » (seuil au milieu, estimé), espérance exacte à 25, 100 et 200 témoins "
                  "d'étalonnage ; « q2/q3/q4 » = probabilité que ce bras joue le quota 2, 3 (la majorité) ou 4 à 25 témoins.")
    lignes.append("")
    lignes.append("| loi | profil | ρ | ρ moy. plantée | EE majorité | EE Bayes | gain max. de toute règle | meilleur quota | "
                  "C pop. : règle | C pop. : gain | poids C (juge 5 / juge 1) | P pop. : règle | P pop. : gain | "
                  "PE − maj. à 25 | à 100 | à 200 | PE q2/q3/q4 à 25 |")
    lignes.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for c in r["cellules"]:
        q = c["regles_fixes_par_quota"]
        C = c["bras_C_en_population"]
        P = c["bras_P_en_population"]
        pe = c["poids_egaux_a_etalonnage_fini_par_taille"]
        pq = pe["25"]["probabilite_de_chaque_quota_joue"]
        w = C["poids_rapportes_a_leur_moyenne"]
        lignes.append("| " + " | ".join([
            str(c["loi"]), c["profil"], a(c["rho_grille"], 2), a(c["valeur_plantee_rho_moyenne"], 3),
            a(q["quota_3"]["erreur_equilibree"]), a(c["regle_de_bayes"]["erreur_equilibree"]),
            a(c["gain_maximal_de_toute_regle_sur_la_majorite_stricte"]), str(c["meilleur_quota"]),
            C["lettre_du_code_egalite_non_notable"]["regle"], gain_double(C), a(w[4] / w[0], 3),
            P["lettre_du_code_egalite_non_notable"]["regle"], gain_double(P),
            a(pe["25"]["ecart_a_la_majorite_stricte_esperance"]), a(pe["100"]["ecart_a_la_majorite_stricte_esperance"]),
            a(pe["200"]["ecart_a_la_majorite_stricte_esperance"]),
            f"{a(pq['2'], 2)}/{a(pq['3'], 2)}/{a(pq['4'], 2)}",
        ]) + " |")
    lignes.append("")
    lignes.append("## Synthèses par ensemble de cellules")
    lignes.append("")
    lignes.append("| ensemble | cellules | majorité = Bayes partout | gain max. de toute règle sur la majorité (min ; max) | "
                  "C pop. gain (min ; max), lettre | P pop. gain (min ; max), lettre | PE − maj. à 25 (min ; max) | "
                  "PE − maj. à 200 (min ; max) | gain max. de toute règle sur PE à 25 | à 200 | "
                  "demi-largeur à 95 % de l'écart apparié PE − maj., 2 000 répliques, à 25 |")
    lignes.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for nom, s in r["syntheses"].items():
        pe = s["poids_egaux_a_etalonnage_fini"]
        lignes.append("| " + " | ".join([
            nom, str(s["cellules"]), "oui" if s["majorite_stricte_est_la_regle_de_bayes_dans_toutes"] else "non",
            f"{a(s['gain_maximal_de_toute_regle_sur_la_majorite_stricte_min'])} ; {a(s['gain_maximal_de_toute_regle_sur_la_majorite_stricte_max'])}",
            " ; ".join(a(x) for x in s["bras_C_population_gain_sur_majorite_lettre_min_max"]),
            " ; ".join(a(x) for x in s["bras_P_population_gain_sur_majorite_lettre_min_max"]),
            " ; ".join(a(x) for x in pe["25"]["poids_egaux_moins_majorite_stricte_min_max"]),
            " ; ".join(a(x) for x in pe["200"]["poids_egaux_moins_majorite_stricte_min_max"]),
            a(pe["25"]["gain_maximal_de_toute_regle_sur_poids_egaux_max"]),
            a(pe["200"]["gain_maximal_de_toute_regle_sur_poids_egaux_max"]),
            a(pe["25"]["demi_largeur_a_95_pour_cent_de_l_ecart_apparie_max"]),
        ]) + " |")
    lignes.append("")
    with open(argv[2], "x", encoding="utf-8") as f:
        f.write("\n".join(lignes))
    print("\n".join(lignes))


if __name__ == "__main__":
    main(sys.argv)

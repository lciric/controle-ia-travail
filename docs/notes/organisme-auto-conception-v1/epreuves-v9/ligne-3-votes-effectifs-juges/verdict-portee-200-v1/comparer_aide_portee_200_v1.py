"""Comparaison de ma lecture (sortie de comptes_portee_200_v1.py) à l'aide du code `criteres_mecaniques.puissance`
(additif 3 v3, § 5, point 8 ; R13 : l'aide n'est jamais le verdict). Écrit par l'agent qui prononce, modèle O.

Usage : python3 -B comparer_aide_portee_200_v1.py SORTIE_COMPTES RESULTAT_200 SORTIE_JSON
"""
import json
import sys


def main():
    with open(sys.argv[1], encoding="utf-8") as fh:
        moi = json.load(fh)
    with open(sys.argv[2], encoding="utf-8") as fh:
        aide = json.load(fh)["criteres_mecaniques"]["puissance"]

    champs = []

    def comparer(nom, a_moi, a_aide):
        champs.append({"champ": nom, "moi": a_moi, "aide": a_aide, "egal": a_moi == a_aide})

    comparer("issue", moi["issue_par_le_paragraphe_3"], aide["issue"])
    comparer("puissance_qui_decide", moi["puissance_qui_decide"], aide["puissance_qui_decide"])
    comparer("repliques_gagnees_qui_decident", moi["repliques_gagnees_qui_decident"],
             aide["repliques_gagnees_dans_la_cellule_la_plus_basse"])
    comparer("repliques_par_cellule", moi["repliques_par_cellule"], aide["repliques_par_cellule"])
    cm = sorted((c["rang"], c["comparaison_du_test"], c["loi"], c["rho"], c["rho_prime"]) for c in moi["cellules_au_minimum"])
    ca = sorted((c["rang"], c["comparaison_du_test"], c["loi"], c["rho"], c["rho_prime"]) for c in aide["cellules_au_minimum"])
    comparer("cellules_au_minimum", cm, ca)
    for nom in ("U", "S_1", "S_2", "R_3"):
        comparer(f"minimum_{nom}_compte", moi["minima_par_comparaison"][nom]["repliques_gagnees"],
                 aide["minima_par_comparaison_en_repliques_gagnees"][nom])
        comparer(f"minimum_{nom}_puissance", moi["minima_par_comparaison"][nom]["puissance"],
                 aide["minima_par_comparaison"][nom])
    comparer("cellules_faisables_lues_par_comparaison", moi["cellules_faisables_lues_par_comparaison"],
             aide["cellules_faisables_lues_par_comparaison"])
    comparer("comparaisons_sans_cellule_faisable", moi["comparaisons_sans_cellule_faisable"],
             aide["comparaisons_sans_cellule_faisable"])
    comparer("pres_du_seuil", moi["pres_du_seuil_0_478_a_0_522"], aide["pres_du_seuil"]["vrai"])
    comparer("ecart_qui_decide", 0.10, aide["ecart_qui_decide"])
    v3 = aide["lecture_du_banc_v3_sur_les_memes_cellules"]
    comparer("lecture_banc_v3_puissance_qui_decide", moi["puissance_qui_decide"], v3.get("puissance_qui_decide"))
    desaccords = [c for c in champs if not c["egal"]]
    sortie = {"programme": "comparer_aide_portee_200_v1.py", "champs_compares": len(champs),
              "desaccords": desaccords, "champs": champs, "aide_ce_qu_elle_dit": aide.get("ce_qu_elle_dit"),
              "aide_lecture_du_banc_v3": v3}
    with open(sys.argv[3], "x", encoding="utf-8") as fh:
        json.dump(sortie, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    print(json.dumps(sortie, ensure_ascii=False, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()

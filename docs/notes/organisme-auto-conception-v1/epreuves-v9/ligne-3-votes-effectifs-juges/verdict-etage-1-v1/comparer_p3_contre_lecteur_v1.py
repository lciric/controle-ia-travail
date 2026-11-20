"""Compare la lecture de P3 de l'agent du verdict (lecture-p3-etage-1-v1.json)
au rejeu du contre-lecteur (rejeu-predictions-contre-lecteur-v1.json, bloc P3)
et à ses compléments (distance aux bornes). Tolérance 1e-12.
Usage : python3 -I -B comparer_p3_contre_lecteur_v1.py MIEN.json REJEU.json COMPLEMENTS.json PREDICTIONS_V1.json SORTIE.json
"""
import json
import sys

CORR = {"C contre F_majorite_stricte": "C_contre_majorite_stricte",
        "P contre F_majorite_stricte": "P_contre_majorite_stricte",
        "C contre poids_egaux": "C_contre_poids_egaux",
        "P contre poids_egaux": "P_contre_poids_egaux"}


def proche(a, b):
    if isinstance(a, bool) or isinstance(b, bool) or a is None or b is None:
        return a == b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(a - b) <= 1e-12
    return a == b


def main():
    mien_p, rejeu_p, compl_p, pred_p, dst = sys.argv[1:6]
    with open(mien_p, encoding="utf-8") as f:
        mien = json.load(f)
    with open(rejeu_p, encoding="utf-8") as f:
        rejeu = json.load(f)
    with open(compl_p, encoding="utf-8") as f:
        compl = json.load(f)
    with open(pred_p, encoding="utf-8") as f:
        pred = json.load(f)
    lignes = []
    for k, kk in CORR.items():
        m = mien["lectures"][k]
        r = rejeu["P3"]["par_lecture"][kk]
        b200 = r["blocs_loi_4_a_200_temoins_d_etalonnage_rho_0.6_ou_plus"]
        paires = [
            ("clause 1, plus grand gain, 168 cellules", m["clause_1_plus_grand_gain_168"], r["echangeables_loi_1_taux_egaux_entre_juges"]["max"]),
            ("clause 1, plus grand gain, 112 cellules", m["clause_1_plus_grand_gain_112_taux_egaux"], r["echangeables_loi_1_profils_egal_seulement"]["max"]),
            ("clause 1 atteinte", m["clause_1_atteinte"], r["clause_1_gain_de_0.02_ou_plus_echangeables_dans_une_cellule"]),
            ("clause 2, cellules", mien["cellules_clause_2_loi_4_n400_rho_ge_0_6"], b200["cellules"]),
            ("clause 2, avec gain", m["clause_2_avec_gain"], b200["cellules_a_gain_positif"]),
            ("clause 2, sans gain", m["clause_2_sans_gain"], b200["cellules"] - b200["cellules_a_gain_positif"]),
            ("clause 2, plus grand gain", m["clause_2_plus_grand_gain"], b200["max"]),
            ("clause 2, gain 0,02 atteint", m["clause_2_gain_0_02_atteint_quelque_part"], b200["cellules_a_gain_de_0.02_ou_plus"] > 0),
            ("clause 2, atteinte dans une cellule", m["clause_2_atteinte_convention_declaree"], r["clause_2_aucun_gain_en_blocs_a_200__dans_une_cellule_au_moins_rho_0.6"]),
            ("clause 2, atteinte dans toutes", m["clause_2_atteinte_sens_aucune_cellule_avec_gain"], r["clause_2_aucun_gain_en_blocs_a_200__dans_toutes_les_cellules_rho_0.6"]),
        ]
        for nom, a, b in paires:
            lignes.append({"lecture": k, "champ": nom, "agent": a, "contre_lecteur": b, "egal": proche(a, b)})
    d1 = pred["verification_bornes"]["plus_petite_distance_a_une_borne_780_cellules"]
    d2 = compl["plus_petite_distance_a_une_borne_sur_780"]["distance"]
    lignes.append({"lecture": "-", "champ": "plus petite distance à une borne", "agent": d1, "contre_lecteur": d2, "egal": proche(d1, d2)})
    out = {"champs": len(lignes), "ecarts": [l for l in lignes if not l["egal"]], "detail": lignes}
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write("\n")


if __name__ == "__main__":
    main()

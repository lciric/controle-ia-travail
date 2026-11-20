"""Audit de symétrie (additif 3 v3, § 6) de la mesure « portée à 200 ». Écrit par l'agent qui prononce, modèle O.
Lit la sortie de comptes_portee_200_v1.py (jamais l'aide du code). Rend : comparaison cellule par cellule 200 contre
100 (comparaisons plantées), règle choisie par le bras C et replis, écarts observés moyens, et l'écart vrai du bras R
contre « au moins un » dans les cellules où une puissance vaut 0 ou 1 exactement (bras R joué à rho' = 0 hors de son
monde, règle B de l'additif 1).

Usage : python3 -B audit_symetrie_portee_200_v1.py SORTIE_COMPTES SORTIE_JSON
"""
import json
import sys

TAUX = 0.20


def ee_au_moins_un_et_r(d, rho, rho_prime):
    a, b = TAUX + d, TAUX - d
    q = lambda p: p * p + rho * p * (1 - p)
    r = lambda p: rho_prime * p + (1 - rho_prime) * (3 * p * p - 2 * p ** 3)
    return 0.5 * (q(a) + 2 * b - q(b)), 0.5 * (r(a) + r(b))


def main():
    with open(sys.argv[1], encoding="utf-8") as fh:
        s = json.load(fh)
    lignes = []
    baisses = []
    for c in s["detail_cellules_faisables"]:
        R = 2000
        for nom, baisse in c["plantees_baisse_200_vs_100"].items():
            k200 = c["comptes_200"][nom]
            k100 = None if c["comptes_100"] is None else c["comptes_100"][nom]
            ligne = {"rang": c["rang"], "monde": c["comparaison_du_monde"], "ecart_vise": c["ecart_vise"], "loi": c["loi"],
                     "rho": c["rho"], "rho_prime": c["rho_prime"], "comparaison": nom,
                     "k200": k200, "k100": k100, "p200": k200 / R, "p100": None if k100 is None else k100 / R,
                     "baisse": baisse}
            lignes.append(ligne)
            if baisse:
                baisses.append(ligne)
    regles = []
    for c in s["detail_cellules_faisables"]:
        regles.append({"rang": c["rang"], "monde": c["comparaison_du_monde"], "ecart_vise": c["ecart_vise"],
                       "loi": c["loi"], "rho": c["rho"], "rho_prime": c["rho_prime"],
                       "regles_bras_C": c["bras_C_regle_choisie"], "replis": c["bras_C_repli_poids_egaux"],
                       "ecart_observe_moyen": c["ecart_observe_moyen_200"]})
    zero_un = []
    detail_par_rang = {c["rang"]: c for c in s["detail_cellules_faisables"]}
    for z in s["cellules_faisables_a_0_ou_1"]:
        c = detail_par_rang[z["rang"]]
        amu, rr = ee_au_moins_un_et_r(c["d"], c["rho"], 0.0)
        zero_un.append({**z, "monde": c["comparaison_du_monde"], "loi": c["loi"], "rho": c["rho"], "d": c["d"],
                        "ecart_vrai_R_rho_prime_0_moins_au_moins_un": rr - amu,
                        "ecart_observe_moyen_R_3": c["ecart_observe_moyen_200"]["R_3"]})
    sortie = {"programme": "audit_symetrie_portee_200_v1.py",
              "comparaison_200_contre_100_comparaisons_plantees": lignes,
              "cellules_qui_baissent": baisses,
              "nombre_de_lignes_comparees": len(lignes),
              "nombre_qui_baissent": len(baisses),
              "regles_bras_C_et_replis": regles,
              "cellules_a_0_ou_1": zero_un}
    with open(sys.argv[2], "x", encoding="utf-8") as fh:
        json.dump(sortie, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    for l in lignes:
        print(f"rang {l['rang']:3d} {l['monde'][:10]:10s} ec {l['ecart_vise']:.2f} loi {l['loi']} rho {l['rho']:.2f} "
              f"rho' {l['rho_prime']:.1f} {l['comparaison']:4s} 200: {l['k200']:4d}  100: {l['k100']}  baisse: {l['baisse']}")
    print("baissent :", len(baisses), "sur", len(lignes))
    for r in regles:
        print(f"rang {r['rang']:3d} ec {r['ecart_vise']:.2f} loi {r['loi']} rho {r['rho']:.2f} rho' {r['rho_prime']:.1f} "
              f"regles {r['regles_bras_C']} replis {r['replis']} ecarts_obs {json.dumps(r['ecart_observe_moyen'])}")
    print(json.dumps(zero_un, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()

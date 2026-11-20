"""Résumé lisible de application-criteres-etage-1-v1.json.
Usage : python3 -I -B resumer_application_v1.py APPLICATION.json SORTIE.txt
"""
import json
import sys
from collections import Counter


def f(x):
    return "None" if x is None else (f"{x:.4f}" if isinstance(x, float) else str(x))


def main():
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as fh:
        a = json.load(fh)
    L = []
    E = a["estimateur"]
    L.append("== ESTIMATEUR")
    L.append("accord drapeau code: " + json.dumps(E["accord_du_drapeau_tient_du_code_par_cellule_et_n"]))
    L.append(f"cellules de la règle: {E['nombre_cellules_de_la_regle']}")
    L.append("tient par n (règle): " + json.dumps(E["tient_aux_cellules_de_la_regle_par_n"]))
    L.append("verdict: " + E["verdict_estimateur"] + " ; taille: " + f(E["taille_retenue"]))
    L.append("non monotone (règle): " + str(E["issue_non_monotone_au_niveau_de_la_regle"]))
    L.append(f"cellules non monotones (toutes): {E['cellules_non_monotones_nombre']}")
    for k, parn in E["detail_cellules_de_la_regle"].items():
        for n, d in parn.items():
            L.append(f"  {k} n={n} tient={d['tient']} biais={f(d['biais'])} eqm={f(d['eqm'])} couv={f(d['couverture'])} indef={f(d['part_indefini'])} manques={json.dumps({kk: (round(v, 4) if v is not None else None) for kk, v in d['manques'].items()})}")
    L.append("cellules non monotones de la règle:")
    for k, parn in E["cellules_non_monotones_de_la_regle"].items():
        L.append("  " + k + " " + json.dumps({n: d["tient"] for n, d in parn.items()}))
    L.append("cellules non monotones (toutes), motif tient par n:")
    for k, parn in E["cellules_non_monotones_toutes"].items():
        motif = "".join("T" if parn[str(n)]["tient"] else "." for n in (50, 100, 200, 400))
        manq = {n: sorted(parn[str(n)]["manques"].keys()) for n in ("50", "100", "200", "400") if not parn[n]["tient"]}
        L.append(f"  {k} {motif} manques={json.dumps(manq)}")
    L.append("plus petit n qui tient (par J, loi, profil ; colonnes rho):")
    groupes = {}
    for k, v in E["plus_petit_n_qui_tient"].items():
        J, loi, prof, rho = k.split("|")
        groupes.setdefault((J, loi, prof), {})[rho] = v
    for g in sorted(groupes):
        L.append(f"  {'|'.join(g)}: " + ", ".join(f"{r[3:]}→{groupes[g][r]}" for r in sorted(groupes[g], key=lambda r: float(r[3:]))))
    P = a["puissance"]
    L.append("== PUISSANCE")
    L.append("puissance qui décide: " + f(P["puissance_qui_decide"]) + " ; portée s'applique: " + str(P["regle_de_portee_s_applique"]))
    L.append("comptes faisables 0,10 observés: " + json.dumps(P["comptes_faisables_0_10_observes"]) + " ; égaux au texte: " + str(P["comptes_egaux_au_texte"]))
    for ecart, d in P["par_ecart"].items():
        L.append(f" écart {ecart}: plus basse={f(d['plus_basse_toutes_comparaisons'])} sans cellule faisable={d['comparaisons_sans_cellule_faisable']}")
        for comp, v in d["par_comparaison"].items():
            L.append(f"  {comp}: faisables loi1={v['faisables_loi_1']} loi3={v['faisables_loi_3']} rho_prime_hors_R={v['rho_prime_hors_bras_R']} ecart_formule_max={f(v['ecart_formule_max_au_vise'])} plus_basse={f(v['plus_basse'])}")
            for l in v["puissances"]:
                L.append(f"    loi{l['loi']} rho={l['rho']} rp={l['rho_prime']} {l['bras']} puissance={f(l['puissance'])} d={f(l['d'])}")
    L.append("== REGLE A: " + json.dumps(a["regle_A_ecart_rho_prime_moins_rho"]))
    L.append("== fa38: " + json.dumps(a["fa38f9faa24e0"], ensure_ascii=False))
    b2 = a["fefca0bd94064_branche_2"]
    L.append("== branche 2: " + json.dumps({k: b2[k] for k in ("par_taille", "tient_dans_toutes_les_cellules_par_taille", "plus_petite_taille_d_etalonnage")}, ensure_ascii=False))
    L.append(f"  réfutées: {len(b2['cellules_refutees'])}")
    for r in b2["cellules_refutees"][:40]:
        L.append("   " + json.dumps(r))
    L.append("== branche 3: " + json.dumps(a["fefca0bd94064_branche_3"], ensure_ascii=False))
    fc = a["fcfa3d98b90f8"]
    L.append("== fcfa accord: " + json.dumps(fc["accord_avec_le_mot_du_code"]) + " faute ii: " + json.dumps(fc["clause_ii_faute_du_banc"]))
    for k, v in fc["cellules"].items():
        L.append(f"  {k}: (i) {v['clause_i']} ; (iii) {v['clause_iii']} ; mot {v['mot']}")
    L.append("== alarme: " + json.dumps(a["alarme"], ensure_ascii=False))
    tp = a["audit_trop_propre_etage_1"]
    L.append("== trop propre: couverture=1 : " + str(len(tp["couverture_egale_1"])) + " ; drapeau code : " + str(len(tp["drapeau_du_code"])) + " ; égaux : " + str(tp["egaux"]))
    for k in tp["couverture_egale_1"]:
        L.append("   " + k)
    with open(dst, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()

"""Résumé par programme de la sortie du premier passage de la simulation de l'organisme retenu. Usage : python3 … SORTIE."""
import sys
L = open(sys.argv[1]).read().split("\n")
print(L[0]); print("\n".join(l for l in L if l.startswith("# DECISION") or l.startswith("# RENDU") or l.startswith("#   bloc") or l.startswith("# ERREURS")))
def bloc(pref):
    i = [k for k, l in enumerate(L) if l.startswith(pref)][0]
    ent, rows, j = L[i + 1].split("\t"), [], i + 2
    while j < len(L) and L[j].strip() and not L[j].startswith("#"):
        rows.append(dict(zip(ent, L[j].split("\t")))); j += 1
    return rows
fl = lambda r, c: float(r[c])
def et(rs, c):
    v = [fl(r, c) for r in rs if r[c] != "-"]
    return f"{min(v):.3f} a {max(v):.3f} (moy {sum(v)/len(v):.3f})" if v else "-"
for m in (4, 8):
    B = bloc(f"# B. detail par cellule, bloc de {m}")
    print(f"\n== bloc de {m} : cellules distinguees sur 12 (plante / ancre) par dispersion des pas suivants et ancrage ; puis taux honnete, plante, ancre (etendue)")
    for s1 in ("0.05", "0.08", "0.12"):
        for rho in ("0.7", "0.9", "1.0"):
            rs = [r for r in B if r["s1"] == s1 and r["ancrage"] == rho]
            print(f"  s1 {s1} ancrage {rho} : {sum(int(r['distingue_plante']) for r in rs)}/12 ; {sum(int(r['distingue_ancre']) for r in rs)}/12 ; h {et(rs,'taux_honnete')} ; p {et(rs,'taux_plante')} ; a {et(rs,'taux_ancre')} ; snr p {et(rs,'snr_plante')} a {et(rs,'snr_ancre')} ; mes/vrai p {et(rs,'mesure/vrai_plante')} a {et(rs,'mesure/vrai_ancre')}")
    for c in ("vrai_total_acceptes_plante", "mesure_total_acceptes_plante", "vrai_total_acceptes_ancre", "mesure_total_acceptes_ancre", "part_deux_plus_grands_plante",
              "plus_grand_exces_vrai_acceptes_ancre", "part_d_actions_plantees_a_exces_mesure_negatif", "exces_mesure_moyen_des_plantes", "ecart_type_e_honnete"):
        print(f"  {c} : {et(B, c)} ; cellules ou le plante se distingue : {et([r for r in B if r['distingue_plante']=='1'], c)}")
D = bloc("# D.")
print("\n== epreuve du centrage, oracle sain, 108 cellules, par bloc : arrets")
for m in ("4", "8"):
    rs = [r for r in D if r["bloc"] == m and r["etat_de_l_oracle"] == "sain"]
    for c in ("arret_rangs_origine", "arret_lisibilite", "arret_rangs_reecrit", "arret_centrage", "P(sensibilite passe)", "P(rejet du flagrant passe)", "part_i", "part_ii", "part_iii",
              "motif_C1", "motif_C2", "motif_C3", "motif_C4", "motif_C4_du_a_la_marge", "part_de_l_exces_a_garder_pour_etre_vu", "exces_mesure_du_flagrant"):
        print(f"  bloc {m} {c} : {et(rs, c)}")
    for s1 in ("0.05", "0.08", "0.12"):
        for rho in ("0.7", "0.9", "1.0"):
            q = [r for r in rs if r["s1"] == s1 and r["ancrage"] == rho]
            print(f"   bloc {m} s1 {s1} ancrage {rho} : part (i)+(ii) {sum(fl(r,'part_i')+fl(r,'part_ii') for r in q)/len(q):.2f} ; a garder {et(q,'part_de_l_exces_a_garder_pour_etre_vu')} ; aboutit plante {et(q,'P(aboutit|part,plante)')} ancre {et(q,'P(aboutit|part,ancre)')} ; arret centrage {et(q,'arret_centrage')}")
print("\n== oracles en defaut (9 cellules, oracle retenu) : moyenne et etendue")
for etat in dict.fromkeys(r["etat_de_l_oracle"] for r in D):
    rs = [r for r in D if r["etat_de_l_oracle"] == etat and (etat != "sain" or (r["s0"] == "0.8" and r["ancre"] == "dernier" and r["profil"] == "reference" and r["bloc"] == D[-1]["bloc"]))]
    print(f"  {etat} ({len(rs)} cellules) : rangs origine {et(rs,'arret_rangs_origine')} ; lisibilite {et(rs,'arret_lisibilite')} ; rangs reecrit {et(rs,'arret_rangs_reecrit')} ; centrage {et(rs,'arret_centrage')} ; sensibilite passe {et(rs,'P(sensibilite passe)')} ; rejet flagrant passe {et(rs,'P(rejet du flagrant passe)')} ; part {sum(fl(r,'part_i')+fl(r,'part_ii') for r in rs)/len(rs):.3f} ; k_H {et(rs,'k_H_moyen')} ; k_P {et(rs,'k_P_moyen')}")

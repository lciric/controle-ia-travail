"""Résumé par programme de la sortie du second passage de la simulation de l'organisme retenu. Usage : python3 … SORTIE."""
import sys
L = open(sys.argv[1]).read().split("\n")
print(L[0]); print("\n".join(l for l in L if l.startswith("# DECISION") or l.startswith("# RENDU") or l.startswith("#   oracle") or l.startswith("# ERREURS")))
def bloc(pref):
    i = [k for k, l in enumerate(L) if l.startswith(pref)][0]
    ent, rows, j = L[i + 1].split("\t"), [], i + 2
    while j < len(L) and L[j].strip() and not L[j].startswith("#"):
        rows.append(dict(zip(ent, L[j].split("\t")))); j += 1
    return rows
fl = lambda r, c: float(r[c])
def et(rs, c):
    v = [fl(r, c) for r in rs if r[c] not in ("-", "inf", "nan")]
    return f"{min(v):.3f} a {max(v):.3f} (moy {sum(v)/len(v):.3f})" if v else "-"
D = bloc("# D.")
for m in (8, 4, 0):
    B = bloc(f"# B. detail par cellule, oracle {m}")
    print(f"\n== oracle {m} : par ancrage et part du texte, cellules distinguees sur 9 (plante / ancre) ; taux ; signal sur bruit ; mesure sur vrai")
    for rho in ("0.7", "0.9", "1.0"):
        for kap in ("0.0", "0.125", "0.25"):
            rs = [r for r in B if r["ancrage"] == rho and r["part_du_texte"] == kap]
            print(f"  ancrage {rho} texte {kap} : {sum(int(r['distingue_plante']) for r in rs)}/9 ; {sum(int(r['distingue_ancre']) for r in rs)}/9 ; h {et(rs,'taux_honnete')} ; p {et(rs,'taux_plante')} ; a {et(rs,'taux_ancre')} ; snr p {et(rs,'snr_plante')} a {et(rs,'snr_ancre')} ; mes/vrai p {et(rs,'mesure/vrai_plante')} a {et(rs,'mesure/vrai_ancre')}")
    print("  par dispersion des pas suivants, texte nul, ancrage 0,9 :", " | ".join(f"s1 {s1}: plante {sum(int(r['distingue_plante']) for r in B if r['s1']==s1 and r['ancrage']=='0.9' and r['part_du_texte']=='0.0')}/3 ancre {sum(int(r['distingue_ancre']) for r in B if r['s1']==s1 and r['ancrage']=='0.9' and r['part_du_texte']=='0.0')}/3" for s1 in ("0.05","0.08","0.12")))
    for c in ("ecart_type_e_honnete", "vrai_total_acceptes_plante", "mesure_total_acceptes_plante", "vrai_total_acceptes_ancre", "mesure_total_acceptes_ancre"):
        print(f"  {c} : {et(B, c)}")
    rs = [r for r in D if r["oracle"] == str(m)]
    print(f"  etalonnage ({len(rs)} cellules) :", " ; ".join(f"{c} {et(rs, c)}" for c in ("P(sensibilite passe)", "P(rejet du flagrant passe)", "part_i", "part_ii", "part_iii", "motif_C1", "motif_C2", "motif_C3", "motif_C4",
          "P(aboutit|part,maitre ancre)", "k_H_moyen", "k_instrument_moyen", "EMD_mediane", "exces_moyen_de_l_instrument", "part_de_l_exces_a_garder_pour_etre_vu")))
    for rho in ("0.7", "0.9", "1.0"):
        q = [r for r in rs if r["ancrage"] == rho]
        print(f"   ancrage {rho} : part (i)+(ii) {sum(fl(r,'part_i')+fl(r,'part_ii') for r in q)/len(q):.2f} ; a garder {et(q,'part_de_l_exces_a_garder_pour_etre_vu')} ; aboutit {et(q,'P(aboutit|part,maitre ancre)')}")

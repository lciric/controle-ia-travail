"""Résumé compact des sorties texte du diagnostic (une ligne JSON par condition)."""
import json, sys
for chemin in sys.argv[1:]:
    for line in open(chemin):
        nom, js = line.split(" ", 1)
        r = json.loads(js)
        t1, t5, t2 = r["theta1.0"], r["theta0.5"], r["theta2.0"]
        f = lambda x: f"{x:.3f}"
        print(f"{nom:24s} | th1 lz {f(t1['lz_moy_ec'][0])}±{f(t1['lz_moy_ec'][1])} uns_med {t1['uns_mediane']:.1f} [{t1['uns_min_max'][0]},{t1['uns_min_max'][1]}] "
              f"sans_un {t1['part_reponses_sans_un']:.2f} <10uns {t1['part_reponses_moins_de_10_uns']:.2f} part_site {t1['part_uns_sur_ligne_site']:.2f} "
              f"rep_avec_hors_site {t1['part_reponses_avec_uns_hors_site']:.2f} lz_hors_site {f(t1['lz_hors_site_moy_ec'][0])} lz>1.05 {t1['part_lz_sup_1_05']:.2f}")
        lm = r["lz_rapporte_melange_theta1"]
        print(f"{'':24s} | th1 lz/melange {('%.3f±%.3f (n=%d)' % tuple(lm)) if lm else 'sans objet'} ; th2 lz {f(t2['lz_moy_ec'][0])} uns_med {t2['uns_mediane']:.1f} sans_un {t2['part_reponses_sans_un']:.2f} ; th0.5 lz {f(t5['lz_moy_ec'][0])} uns_med {t5['uns_mediane']:.1f} part_site {t5['part_uns_sur_ligne_site']:.2f}")
        print(f"{'':24s} | PR brut {r['pr_brut_moy']:.2f} PR reduit {r['pr_reduit_moy']:.2f} ; gain brut {r['gain_brut_moy']:.3f} gain relatif/position {r['gain_relatif_moy']:.4f} ; |site entree| {r['norme_site_entree_moy']:.1f} |x final| {r['norme_x0_final_moy']:.1f} ; |d site|/|u| {r['norme_d_site_sur_u_moy']:.2f}")
        c = r.get("controle_identite_avec_original")
        if c:
            ok = all(abs(a[0][0]-a[1][0]) < 1e-12 and abs(a[0][1]-a[1][1]) < 1e-12 for k, a in c.items() if k.startswith("lz")) and abs(c["participation_moy"][0]-c["participation_moy"][1]) < 1e-12 and abs(c["gain_moy"][0]-c["gain_moy"][1]) < 1e-12
            print(f"{'':24s} | identique a l'original (lz 3 seuils, participation, gain) : {ok}")

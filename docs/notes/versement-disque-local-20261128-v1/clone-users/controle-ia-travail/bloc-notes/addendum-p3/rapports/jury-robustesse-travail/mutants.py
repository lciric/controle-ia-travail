"""Mutants de même sens pour les deux candidats : chaque règle affaiblie une à une ; la suite de tests du candidat doit
échouer (mutant tué). Prépare les dossiers ; le lancement se fait par lancer_mutant.sh."""
import shutil
import sys
from pathlib import Path

W = Path(sys.argv[1])
C = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum-p3")

MUTANTS = {
    "a": {
        "MOY_fenetres_moyenne_des_jetons": [(
            "                S_fen[n, r] = score_empan(s, lg, int(d), int(d) + L)",
            "                S_fen[n, r] = float(np.mean(s[int(d):int(d) + L]))")],
        "A2b_reserve_fenetre_jamais": [('    if rb is not None and rb["bas"] <= 0.0:',
                                        '    if rb is not None and rb["bas"] <= -9.0:')],
        "A1_sens_haut_jamais": [('        contraire = r["ecart_bas"] > 0.0 if inverse else r["ecart_bas"] <= 0.0',
                                 '        contraire = r["ecart_bas"] > 9.0 if inverse else r["ecart_bas"] <= 0.0')],
        "A3_delta_SM_jamais": [('            e.juger(_c(conclusion, p), n, x["bas"] <= 0.0, reserve,',
                                '            e.juger(_c(conclusion, p), n, x["bas"] <= (0.0 if n == "saboteur_moins_temoin" else -9.0), reserve,')],
        "A4c_sensibilite_jamais": [('    elif not rc["au_dessus_du_plancher"]:', "    elif False:")],
        "A6_sens_inverse_jamais": [('            e.juger(conclusion, nom, r["bas"] > 0.0, "reserve_A6_lecteur_cout",',
                                    '            e.juger(conclusion, nom, r["bas"] > 9.0, "reserve_A6_lecteur_cout",')],
        "A7_correlation_jamais": [('    rho_h = {x: v for x, v in rho["honnete"].items() if v is not None and abs(v) >= SEUIL_CORRELATION}',
                                   "    rho_h = {}")],
        "niveau_975_devient_95": [("NIVEAU, NIVEAU_BONFERRONI = 0.95, 0.975", "NIVEAU, NIVEAU_BONFERRONI = 0.95, 0.95")],
        "A4a_tranches_figees_sous_l_etiquette_internes": [("            st = strates_quantiles(vt[i], TRANCHES)",
                                                          "            st = np.asarray(st_obs)[i]")],
        "garde_issue_retiree": [('    if _canonique(sortie.get("issue_primaire_inchangee")) != issue_canonique:', "    if False:"),
                                ('    if _canonique(_etat(lecture, "issue")) != issue_canonique:', "    if False:")],
        "garde_entropie_des_graines_retiree": [(
            '    autres = sorted({str(graines[k].get("entropie")) for k in cles} - {str(ENTROPIE_P3)})', "    autres = []")],
        "reserve_non_lue_jamais_creee": [(
            '                self._ajouter(f"reserve_{self.analyse}_non_lu", conclusion, controle, motif)',
            "                pass")],
    },
    "b": {
        "MOY_fenetres_moyenne_des_jetons": [(
            "            fen.append(np.array([agreger_par_jeton(s, lg, int(x), int(x) + L) for x in departs]))",
            "            fen.append(np.array([float(np.mean(s[int(x):int(x) + L])) for x in departs]))")],
        "A2b_reserve_fenetre_jamais": [('            if _lu(b) and b["bas"] <= 0:', '            if _lu(b) and b["bas"] <= -9:')],
        "A1_sens_haut_jamais": [('        elif sens == "haut" and e["ecart_bas"] > 0:',
                                 '        elif sens == "haut" and e["ecart_bas"] > 9:')],
        "A3_delta_SM_jamais": [('        elif e[cle]["bas"] <= 0:', '        elif e[cle]["bas"] <= (0 if cle == "ST" else -9):')],
        "A4c_sensibilite_jamais": [('        if _lu(cc) and not cc["au_dessus_du_plancher"]:', "        if False:")],
        "A6_sens_inverse_jamais": [('        elif nom != "P3-P1" and e["bas"] > 0:', '        elif nom != "P3-P1" and e["bas"] > 9:')],
        "A7_correlation_jamais": [("            if r is not None and abs(r) >= SEUIL_CORRELATION:", "            if False:")],
        "niveau_975_devient_95": [("NIVEAU, NIVEAU_BONFERRONI = 0.95, 0.975", "NIVEAU, NIVEAU_BONFERRONI = 0.95, 0.95")],
        "A4a_tranches_figees_sous_l_etiquette_internes": [(
            '(figees[i] if tranches == "figees" else strates_quantiles(v[i], TRANCHES))', "figees[i]")],
        "garde_issue_retiree": [('    if canonique(s["issue_primaire_inchangee"]) != canonique(lecture["issue"]):',
                                 "    if False:")],
        "garde_entropie_des_graines_retiree": [(
            '    autres = sorted({str(graines[k].get("entropie")) for k in cles_addendum(principales)} - {str(ENTROPIE_P3)})',
            "    autres = []")],
        "reserve_non_lue_jamais_creee": [("reserves.append(_non_lue(", "(lambda *a: None)(_non_lue(", "tous")],
    },
}

lignes = []
for cand, muts in MUTANTS.items():
    texte = (C / f"candidat-{cand}" / "complements_p3_v1.py").read_text(encoding="utf-8")
    for nom, remplacements in muts.items():
        t = texte
        for r in remplacements:
            old, new = r[0], r[1]
            n = t.count(old)
            if n == 0 or (n != 1 and len(r) < 3):
                raise SystemExit(f"{cand} {nom} : {n} occurrences de {old!r}")
            t = t.replace(old, new)
        compile(t, f"{cand}-{nom}", "exec")
        d = W / "mutants" / f"{cand}-{nom}"
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True)
        (d / "complements_p3_v1.py").write_text(t, encoding="utf-8")
        shutil.copy(C / f"candidat-{cand}" / "test_complements_p3_v1.py", d / "test_complements_p3_v1.py")
        lignes.append(str(d))
(W / "mutants" / "liste.txt").write_text("\n".join(lignes) + "\n", encoding="utf-8")
print(len(lignes), "mutants")

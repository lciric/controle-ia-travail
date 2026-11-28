"""Mutants de la vérification neuve du module v3 de l'addendum 2 de P3 (lentille « code et mutants »).

Écrits par le vérificateur depuis le brouillon 5 (critères, audit, point 3 ; précisions 2 et 14 ; M2 à M10 ; ligne
d'arrêt) et le module v3, sur les seuls points changés entre v2 et v3 : déclencheur 3 avec une part en échec (VV-D3),
garde 7 sur un [SF] hors de forme (VV-G7), les cinq formes (VV-F), les descriptifs (VV-DESC), la phrase d'arrêt
(VV-PH), et la route de la garde 6 au lancement (VV-G6, réserve G6-02 du rédacteur).

Chaque mutant : (identifiant, famille, règle mutée, [(motif exact du module v3, remplacement), …]).
Ce fichier est une donnée : le lanceur le lit par `ast.literal_eval`, il ne l'importe pas.
"""

MUTANTS = [
    # ------------------------------------------------------------ déclencheur 3, part en échec (CV2-01, option (b))
    ("VV-D3-01", "VV-D3", "déclencheur global : d3 vrai ignoré quand la part est en échec (d3 garde son état)",
     [('    declencheur = d2["etat"] is True or d3["etat"] is True\n',
       '    declencheur = d2["etat"] is True or (d3["etat"] is True and pf["part"]["etat"] == CALCULE)\n')]),
    ("VV-D3-02", "VV-D3", "part hors bornes : bornes ±1 exclues de [−1 ; 1] (part = ±1 rendue « hors bornes »)",
     [('d3 = {"etat": not (-1.0 <= part <= 1.0), "part": part,', 'd3 = {"etat": not (-1.0 < part < 1.0), "part": part,')]),
    ("VV-D3-03", "VV-D3", "part ponctuelle de l'audit inversée (E0 / D au lieu de D / E0)",
     [('        part = pf["D"]["valeur"] / pf["E0"]["valeur"]\n',
       '        part = pf["E0"]["valeur"] / pf["D"]["valeur"] if pf["D"]["valeur"] else 0.0\n')]),
    ("VV-D3-04", "VV-D3", "« E0 = 0 » lu avec une tolérance (|E0| < 1e-3 → « non calculé »)",
     [('    elif pf["E0"]["valeur"] == 0.0:\n', '    elif abs(pf["E0"]["valeur"]) < 1e-3:\n')]),
    ("VV-D3-05", "VV-D3", "part en échec : l'audit lit la valeur de la part (absente) → exception, arrêt de l'addendum",
     [('        part = pf["D"]["valeur"] / pf["E0"]["valeur"]\n', '        part = pf["part"]["valeur"]\n')]),
    ("VV-D3-06", "VV-D3", "consigne « cité et soumis à Lazar » écrite seulement si le déclencheur 2 est vrai",
     [('"consigne": CONSIGNE_AUDIT if declencheur else None,', '"consigne": CONSIGNE_AUDIT if d2["etat"] is True else None,')]),
    ("VV-D3-07", "VV-D3", "ligne de l'audit dans la recommandation seulement si le déclencheur 2 est vrai",
     [('    if audit["declencheur"]:\n', '    if audit["explication_trop_propre"]["etat"] is True:\n')]),
    ("VV-D3-08", "VV-D3", "part en échec : d3 « non calculé » mais part écrite (changement 6 déguisé)",
     [('d3 = {"etat": not (-1.0 <= part <= 1.0), "part": part,',
       'd3 = {"etat": (not (-1.0 <= part <= 1.0)) if pf["part"]["etat"] == CALCULE else NON_CALCULE, "part": part,')]),
    # ------------------------------------------------------------ garde 7, [SF] hors de forme (CV2-10, précision 14)
    ("VV-G7-01", "VV-G7", "[SF] : nom vide accepté (seul le type est contrôlé)",
     [('        if not isinstance(x, str) or not x:\n', '        if not isinstance(x, str):\n')]),
    ("VV-G7-02", "VV-G7", "[SF] absent de la source : accès direct (KeyError nue)",
     [('    sf = source.get("sondes-figees") if isinstance(source, dict) else None\n',
       '    sf = source["sondes-figees"]\n')]),
    ("VV-G7-03", "VV-G7", "[SF] sans `principales` : motif attribué à la garde 9",
     [('raise GardeArret(f"garde 7 : run source hors de forme : [SF] sans',
       'raise GardeArret(f"garde 9 : run source hors de forme : [SF] sans')]),
    ("VV-G7-04", "VV-G7", "[SF] sans `principales` : sous-classe NonCalculable au lieu de GardeArret",
     [('raise GardeArret(f"garde 7 : run source hors de forme : [SF] sans',
       'raise NonCalculable(f"garde 7 : run source hors de forme : [SF] sans')]),
    ("VV-G7-05", "VV-G7", "[SF] : sondes principales rendues dans l'ordre (enjeux, tromperie)",
     [('    for c in ("tromperie", "enjeux"):\n', '    for c in ("enjeux", "tromperie"):\n')]),
    ("VV-G7-06", "VV-G7", "[SF] sans `principales` : valeur devinée (noms du run réel)",
     [('        x = pr.get(c) if isinstance(pr, dict) else None\n',
       '        x = pr.get(c) if isinstance(pr, dict) else {"tromperie": "tromperie-difference_moyennes-c15", '
       '"enjeux": "enjeux-lineaire-c15"}[c]\n')]),
    # ------------------------------------------------------------ les cinq formes (CV2-02)
    ("VV-F-01", "VV-F", "garde 7 : compte de `cout_milliers_espace` non comparé à [L] P3-P6",
     [('for k, v in [(f, int(t[f][m].sum())) for f in FORMES]', 'for k, v in [(f, int(t[f][m].sum())) for f in FORMES[:-1]]')]),
    ("VV-F-02", "VV-F", "garde 7 : compte de `cout_multiplication` non comparé à [L] P3-P6",
     [('for k, v in [(f, int(t[f][m].sum())) for f in FORMES]',
       'for k, v in [(f, int(t[f][m].sum())) for f in FORMES if f != "cout_multiplication"]')]),
    ("VV-F-03", "VV-F", "M3 : R_sf sans `cout_plusieurs_nombres`",
     [('        r |= t[f]\n', '        r |= t[f] if f != "cout_plusieurs_nombres" else False\n')]),
    ("VV-F-04", "VV-F", "M7 (E_-f) : restriction par forme limitée aux quatre premières",
     [('    sortie["sans_une_forme"] = {}\n    for f in FORMES:\n', '    sortie["sans_une_forme"] = {}\n    for f in FORMES[:4]:\n')]),
    ("VV-F-05", "VV-F", "colonnes : `cout_milliers_espace` lue dans la colonne `cout_multiplication`",
     [('**{f: np.asarray(t[f]).astype(bool) for f in FORMES}',
       '**{f: np.asarray(t["cout_multiplication" if f == "cout_milliers_espace" else f]).astype(bool) for f in FORMES}')]),
    # ------------------------------------------------------------ descriptifs (CV2-03)
    ("VV-DESC-01", "VV-DESC", "M6 : `n_taches_sf` = nombre de tâches de T_∅",
     [('"n_taches_sf": int(vsf.size)}', '"n_taches_sf": n}')]),
    ("VV-DESC-02", "VV-DESC", "M9 : lisibles après R_sf de b comptés avant la restriction",
     [('b: lisibles(csf[1][x])}', 'b: lisibles(c0[1][x])}')]),
    ("VV-DESC-03", "VV-DESC", "M5 : mention « instable » aussi sur une part en échec",
     [('if part["etat"] == CALCULE and e_bas <= 0.0 <= e_haut:', 'if part["etat"] != NON_CALCULABLE and e_bas <= 0.0 <= e_haut:')]),
    ("VV-DESC-04", "VV-DESC", "M7 : nombre de tâches sans forme diminué de 1",
     [('"taches_sans_forme": len(propres), "taches": propres}', '"taches_sans_forme": len(propres) - 1, "taches": propres}')]),
    ("VV-DESC-05", "VV-DESC", "M10 : distance haute = distance basse",
     [('distance_basse, distance_haute = A - bas, haut - A', 'distance_basse, distance_haute = A - bas, A - bas')]),
    ("VV-DESC-06", "VV-DESC", "M8 : actions « avec la forme » comptées lisibles ou non",
     [('"actions_lisibles_avec_la_forme": int(avec.sum())', '"actions_lisibles_avec_la_forme": int((m & t[f]).sum())')]),
    ("VV-DESC-07", "VV-DESC", "M3 : nulles d'origine comptées parmi les retirées seulement",
     [('"nulles_d_origine": int((m & nul).sum())}', '"nulles_d_origine": int((r & m & nul).sum())}')]),
    ("VV-DESC-08", "VV-DESC", "M10 : A_80 à la distance basse calculée à la demi-largeur",
     [('"A_80_distance_basse": Q + distance_basse * facteur}', '"A_80_distance_basse": Q + w * facteur}')]),
    # ------------------------------------------------------------ phrase d'arrêt (CV2-03)
    ("VV-PH-01", "VV-PH", "sortie d'arrêt sans la phrase de lecture",
     [('"lecture": LECTURE_ARRET, **reference})', '**reference})')]),
    # ------------------------------------------------------------ garde 6 au lancement (réserve G6-02)
    ("VV-G6-01", "VV-G6", "ÉQUIVALENT voulu : garde 6 appelée par un alias (conversion intacte, route changée)",
     [('    source = exiger_garde_6(racine, run_source)                                    # garde 6',
       '    source = _GARDE_6(racine, run_source)                                          # garde 6'),
      ('def exiger_garde_11(', '_GARDE_6 = exiger_garde_6\n\n\ndef exiger_garde_11(')]),
    ("VV-G6-02", "VV-G6", "garde 6 au lancement : en cas d'arrêt, repli sur le chargeur gelé (exception non convertie)",
     [('    source = exiger_garde_6(racine, run_source)                                    # garde 6',
       '    try:\n        source = exiger_garde_6(racine, run_source)                                # garde 6\n'
       '    except GardeArret:\n        source = lp.charger_source(racine, run_source)')]),
]

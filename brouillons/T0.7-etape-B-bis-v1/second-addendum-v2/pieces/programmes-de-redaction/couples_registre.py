COUPLES = {"src/controle_ia/t07bbis/registre_bbis_v2.py": [
    ('''(`prereg/T0.7-etape-B-bis-v1.md`, « Lignes de registre », « Liste d'arrêt », « Calcul et dépense », « Seuil »), v1.
''', '''(`prereg/T0.7-etape-B-bis-v1.md`, « Lignes de registre », « Liste d'arrêt », « Calcul et dépense », « Seuil »), v2 : la v1, modifiée
par le **second addendum d'écart** (`brouillon-second-addendum-bbis-v1.md`) en trois points seulement : (1) la ligne `CODE-BBIS`
peut être **remplacée une seule fois** au registre propre (liste d'arrêt scellée : « ligne `CODE-BBIS` remplacée une seule fois »),
par une seconde ligne ajoutée après `GO-BBIS` et avant `SCORES-BBIS`, jamais réécrite ; la lecture de la fiche passe par
`lecture_v3.lire_lignes` (la seconde ligne fait foi) ; (2) la garde de création admet **une course de plus** (relances = 2),
accordée par GO-2026-11-16-11, seulement si le feu écrit de la mère porte aussi ce numéro et si `CODE-BBIS` est remplacée ;
(3) la limite du samedi 21 novembre 12:00 UTC vaut pour toute relance. Tout le reste est celui de la v1 (la v1 reste, R12).
''', 1),
    ('''GO_ID = "GO-2026-11-14-09"
''', '''GO_ID = "GO-2026-11-14-09"
GO_ACCORD = "GO-2026-11-16-11"     # second addendum et nouvelle course (une seule), sous GO-2026-11-14-09
''', 1),
    ('''        if cle in cles_bbis_presentes(registre):
            raise GardeArret(f"registre propre : ligne {cle} déjà présente, jamais réécrite")
''', '''        vues = cles_bbis_presentes(registre)
        if cle in vues and not (cle == "CODE-BBIS" and vues.count("CODE-BBIS") == 1 and "GO-BBIS" in vues
                                and "SCORES-BBIS" not in vues):
            raise GardeArret(f"registre propre : ligne {cle} déjà présente, jamais réécrite (seule CODE-BBIS se remplace, une seule "
                             "fois, après GO-BBIS et avant SCORES-BBIS : second addendum)")
''', 1),
    ('''    from .lecture_v1 import CLES_PROPRES, RefusLecture, lire_lignes
    racine = Path(racine)
    try:
        ligne = lire_lignes(racine / REGISTRE_PROPRE, CLES_PROPRES, ("CODE-BBIS",), propre=True)["CODE-BBIS"]
''', '''    from .lecture_v3 import CLES_PROPRES, REMPLACABLES_PROPRES, RefusLecture, lire_lignes
    racine = Path(racine)
    try:
        ligne = lire_lignes(racine / REGISTRE_PROPRE, CLES_PROPRES, ("CODE-BBIS",), propre=True,
                            remplacables=REMPLACABLES_PROPRES)["CODE-BBIS"]
''', 1),
    ('''    numéro de la ligne de GO ; une relance au plus ; échéance de la ligne de GO ; relance après le samedi 21 novembre 12:00 UTC :
    nœud."""
''', '''    numéro de la ligne de GO ; une relance au plus, plus **une course** accordée par GO-2026-11-16-11 (relances = 2 : feu écrit
    portant aussi ce numéro, ligne `CODE-BBIS` remplacée) ; échéance de la ligne de GO ; relance après le samedi 21 novembre
    12:00 UTC : nœud."""
''', 1),
    ('''    if int(relances) > 1:
        raise GardeArret("une seconde relance est exclue (ligne de GO : une relance au plus)")
''', '''    if int(relances) > 2:
        raise GardeArret("une troisième relance est exclue (ligne de GO : une relance au plus ; GO-2026-11-16-11 : une course de "
                         "plus, une seule)")
    if int(relances) == 2 and (GO_ACCORD not in feu_ecrit
                               or cles_bbis_presentes(Path(racine) / REGISTRE_PROPRE).count("CODE-BBIS") != 2):
        raise GardeArret(f"seconde relance : seulement sous le second addendum (feu écrit portant {GO_ACCORD} et ligne CODE-BBIS "
                         "remplacée au registre propre) : refus")
''', 1),
    ('''    if int(relances) == 1 and int(maintenant) > _instant(LIMITE_RELANCE):
''', '''    if int(relances) >= 1 and int(maintenant) > _instant(LIMITE_RELANCE):
''', 1),
]}

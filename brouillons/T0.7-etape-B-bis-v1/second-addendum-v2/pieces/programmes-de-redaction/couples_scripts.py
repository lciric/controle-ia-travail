COUPLES = {
    "scripts/lancer_bbis_v4.sh": [
        ('''# Chaîne de session de l'étape B bis de T0.7, v3 (la v2, qui passe l'amorce v3 : marche v3, contrôle carte-processeur
# sans issue « sans objet », R-2919 ; les v1 et v2 restent, R12) (prereg/T0.7-etape-B-bis-v1.md, « Calcul et dépense », « Liste d'arrêt » ; ligne
''', '''# Chaîne de session de l'étape B bis de T0.7, v4 (la v3, qui passe l'amorce v4 : marche v4, contrôle carte-processeur v4 et
# mesure de dispersion du second addendum ; gardes de registre v2 : CODE-BBIS remplacée une fois, une course de plus accordée par
# GO-2026-11-16-11 ; les v1 à v3 restent, R12) (prereg/T0.7-etape-B-bis-v1.md, « Calcul et dépense », « Liste d'arrêt » ; ligne
''', 1),
        ('''#                                    GO-2026-11-14-09, une relance au plus, échéance, relance après le 21 novembre 12:00 UTC refusée ;
''', '''#                                    GO-2026-11-14-09, une relance au plus, plus une course (RELANCES=2) si le feu porte aussi
#                                    GO-2026-11-16-11 et CODE-BBIS est remplacée, échéance, relance après le 21 novembre 12:00 UTC refusée ;
''', 1),
        ("amorce_bbis_v3.sh", "amorce_bbis_v4.sh", 7),
        ("lancer_bbis_v3.sh", "lancer_bbis_v4.sh", 3),
        ('''-m controle_ia.t07bbis.registre_bbis_v1 "$@"; }''', '''-m controle_ia.t07bbis.registre_bbis_v2 "$@"; }''', 1),
    ],
    "scripts/amorce_bbis_v4.sh": [
        ('''# Amorce de l'instance de l'étape B bis de T0.7, v3 (la v2, dont la marche est `controle_ia.t07bbis.marche_v3` : contrôle
# carte-processeur sans issue « sans objet », R-2919 ; minimum d'essais relevé au compte neuf ; blocs marqués identiques à ceux de
# la v1 ; les v1 et v2 restent, R12) (prereg/T0.7-etape-B-bis-v1.md, plan, points 1 à 8 ; « Calcul et dépense » ;
''', '''# Amorce de l'instance de l'étape B bis de T0.7, v4 (la v3, dont la marche est `controle_ia.t07bbis.marche_v4` : contrôle
# carte-processeur v4 et mesure de dispersion du second addendum ; branche de sortie neuve donnees/t07-etape-b-bis-v2 (la v1 porte
# la course arrêtée, R12) ; minimum d'essais relevé ; blocs marqués identiques à ceux de la v1 ; les v1 à v3 restent, R12)
# (prereg/T0.7-etape-B-bis-v1.md, plan, points 1 à 8 ; « Calcul et dépense » ;
''', 1),
        ("controle_ia.t07bbis.marche_v3", "controle_ia.t07bbis.marche_v4", 2),
        ("passée par scripts/lancer_bbis_v3.sh", "passée par scripts/lancer_bbis_v4.sh", 1),
        ("(lancer_bbis_v3.sh verifier-destruction)", "(lancer_bbis_v4.sh verifier-destruction)", 1),
        ("donnees/t07-etape-b-bis-v1", "donnees/t07-etape-b-bis-v2", 2),
        ('''/scripts/lancer_bbis_v3.sh*
''', '''/scripts/lancer_bbis_v3.sh*
/scripts/amorce_bbis_v4.sh*
/scripts/lancer_bbis_v4.sh*
''', 1),
        ('''MIN_ESSAIS=115
''', '''# v4 (second addendum) : 115 de la v3 plus les essais neufs du second addendum qui passent sans docs/notes ni brouillons
# (rapport-second-addendum-bbis-v1.md, § 3 ; à recompter sur l'arbre de l'instance simulé avant le feu)
MIN_ESSAIS=148
''', 1),
    ],
}

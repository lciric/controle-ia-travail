# Erratum 1 — application du classement (22 novembre 2026, vers 20:45Z)

1. Correction de l'essai des lentilles (classe D) retirée. `tests/test_lentilles_sondes_bbis_seconde_passe_corrections_v1.py::test_l_outil_de_fabrique_rejoue_rend_le_lanceur_v2_ses_jouets_et_ses_essais_a_l_octet_pres` régénère le v2 de cet essai à partir du v1, à l'octet près. Toute retouche du v1 le fait échouer. Le v1 est donc rendu tel qu'il est sur main. Le défaut d'ordre reste ouvert (nœud à la mère). Il peut faire échouer cet essai quand la suite charge d'abord un lanceur v8 ou v9 des lentilles.
2. La suite complète (4 lots, 451 fichiers, branche à 7dcf93501) donne 15 échecs hors de la liste v3 :
   - 14 viennent de `registres/go.md` ligne 785 (GO-2026-11-22-98, entrée après abf45a528) : son champ de date porte un texte libre au lieu d'une date. La garde du registre GO s'arrête alors sur « registre GO mal formé ligne 785 : dates illisibles ». C'est un défaut du registre de main, sans lien avec la liste v3. La garde de calcul bloque tout lancement tant que la ligne n'est pas corrigée.
   - Le 15e est l'essai de fabrique du point 1, réglé par le retrait.
3. La condition de versement sur main (« échecs restants = liste v3 exactement ») n'est pas remplie, à cause du point 2. Rien n'est versé sur main. La branche reste à la décision de la mère.

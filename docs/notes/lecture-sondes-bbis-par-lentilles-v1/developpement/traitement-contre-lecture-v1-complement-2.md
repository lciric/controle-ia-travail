# Complément 2 au traitement de la contre-lecture du code — vérification de la version 2, note de version sur le mot « exacte », essais de l'addendum préparés, et ce qui reste à écrire

Suit `traitement-contre-lecture-v1.md` (`42f0db6f…`) et son complément 1 (`8b34c66e…`). Sources : messages de la mère du 2026-11-19,
12:26 et 12:27 UTC (données d'une autre session ; je n'ai ouvert ni le rapport de vérification ni aucun registre).

## 1. Version 2 vérifiée

Selon la mère : version 2 (`08dea10b`) vérifiée « bon tel quel » par le même contre-lecteur (R-3797 ;
`docs/notes/lecture-sondes-bbis-par-lentilles-v1/verification-code-lentille-publique-v2-v1.md`, `7a52c796…`). Une remarque non
bloquante, **à porter dans la version suivante, non encore faite** : le manifeste met `None` en silence si le rapport du montage
manque ; à remplacer par un arrêt au départ du calcul (« rapport du montage absent du dossier de sortie : le manifeste ne pourrait le
citer ; rien ne part »), la citation devenant inconditionnelle, avec un essai à artefact.

## 2. Note de version : le mot « exacte » de `audits_v1`

Tranché par la mère : une note de version suffit, pas de module des audits de version 2. `audits_v1.py` (`86cda9a3…`, inchangé, R12)
appelle « loi exacte » la loi bêta-binomiale (n ; 100 ; M − 99) du compte de calibration. L'addendum « concentration »
(`prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`, brouillon candidat `0a862760…`, EC-3 et § 7) la nomme
**« loi de référence, approchée, non exacte »** : sous la statistique corrigée elle est approchée à l'ordre de son § 6. **Le calcul et
les bornes de `audits_v1` ne changent pas** ; seul le mot de sa docstring est à lire « de référence, approchée ». Cette note sera
recopiée, avec l'empreinte de l'addendum scellé, dans la note de la version définitive.

## 3. Essais de l'addendum, préparés et non définitifs

`tests/test_lentilles_sondes_bbis_addendum_concentration_v1.py` (`8771d06198af3ffd495ba739827344b74d32949fe56e7023a7b6bcb8e81dbde0`), quatre essais, verts (`4 passed`) :
- `les_41_bornes_de_l_addendum_egales_a_celles_du_code` (cas sain : un jeu de 1 000, et un à quarante jeux de 200, valeurs recopiées du
  § 7) ; `artefact_une_borne_decalee_d_un_cran_est_vue` (loi faussée d'un cran : des bornes changent) ;
- `taux_a_petite_taille_sous_la_statistique_corrigee` (EC-5 : 19 directions nulles, 128 jetons gaussiens indépendants, 2 000
  répliques, part entre 0,03 et 0,065) ; `artefact_de_taux_a_petite_taille_sous_la_statistique_d_origine` (part au-dessus de 0,3).
Les valeurs des bornes sont recopiées du brouillon candidat : à comparer au texte scellé.

## 4. Reste à écrire, après le scellement de l'addendum et la ratification de sa clé de registre

Sous des noms neufs, `statistiques_v2.py` inchangé : `entrees_v3` (clé `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` exigée à l'ouverture des
sondes et au calcul, non au montage ; sa ligne cite l'addendum scellé, chemin et empreinte) ; `lanceur_v4` (cette garde ; arrêt si le
rapport du montage manque, citation inconditionnelle) ; leurs essais à artefact ; fichier d'empreintes v4 ; note de version.
**Il me faut l'empreinte de l'addendum scellé.**

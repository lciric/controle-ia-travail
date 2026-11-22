# Champs de l'ordre de la course remplis par l'étape E3 (conditions et désignation) — v1

Pièce de travail (classe C), pour le rédacteur de l'ordre de la course (P2). Écrite par l'exécutante v5, 2026-11-22T11:30:03Z, depuis le code au commit c97231b38 (`lanceur_v5.phase_conditions`, `designation_v5.designer`, `designation_v5.configuration_de_course`), sans aucun résultat lu.

## A. Rendus par le passage unique (`designation-iib-v5.json`, `branches-iib-v5.json`)
1. `issue` : « N », « P », « ne_part_pas » ou « non_calculable ». Seules N et P ouvrent une course ; les deux autres : course neuve sous devis neuf.
2. `these` : thèse nommée de l'oracle désigné.
3. `variante_consigne` : variante (N ou P) et empreinte de la consigne privée du maître correspondante (noms et empreintes seulement).
4. `tours` : nombre de tours visé (12 si au plus 12 ; « ne part pas, motif tours » au-delà du plafond de tours).
5. `phrases` : phrase de 10.6 de l'oracle désigné, phrase de l'autre oracle, clause du premier coût (à citer telles quelles).
6. Empreintes : `branches-iib-v5.json`, `designation-iib-v5.json`, fichier de l'étalonnage (`etalonnage-oracles-iib-v5.json`).
7. Configuration de la course : `oracle_de_la_regle` = {valeur : issue, designation : {chemin, sha256}}, écrite par `configuration_de_course` (seul champ changé par rapport à la configuration de l'étalonnage).

## B. Relevés par l'exécutante à E1 à E3, à reporter dans l'ordre
8. Identifiant du run de l'étalonnage, commit de lancement (43d6d067), arbre du code de l'étalonnage.
9. Dépense relevée de la ligne GO-2026-11-21-70 à l'arrêt (environ 16 USD) → reste avant la coupure de 55 USD.
10. Sort de la machine : 61875617 gardée à l'arrêt (mot de la mère, 22/11 vers 11:26Z) ; heure d'arrêt ; borne de 48 heures d'arrêt.
11. Issue du rapatriement (lots versés ou non ; relance courte jouée ou non).

## C. Fixés par l'ordre de la course lui-même (hors E3)
12. Préfixe des graines de la course (`prefixe_graines`) ; commit et arbre du code de la course (P1, après contre-lecture).
13. Dates : dernière création. Écart à trancher : l'ordre de l'étalonnage écrit « aucune création à partir de 2026-11-27T00:00:00Z » (GO-2026-11-21-70), le devis scellé § 5 écrit « dernière création le 28 novembre à 23:00Z ».
14. Additif au devis si le nombre de tours dépasse 12 : 24 tours au pire ≈ 39,9 h ≈ 49 USD de carte, au-delà du reste de la ligne.

## D. Condition préalable
Le passage des conditions lit `etalonnage-oracles-iib-v5.json`, écrit à la fin de l'étalonnage seulement. Si la coupure tranche l'étalonnage avant sa fin, ce fichier manque : E3 ne rend pas de désignation, et la course ne part pas sous cette ligne.

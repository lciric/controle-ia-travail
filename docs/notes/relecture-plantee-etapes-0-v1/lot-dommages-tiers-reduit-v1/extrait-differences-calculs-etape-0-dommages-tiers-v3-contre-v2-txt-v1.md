# Extrait des différences : calculs-etape-0-dommages-tiers-v3.txt contre calculs-etape-0-dommages-tiers-v2.txt

- Fait le 2026-11-21T22:11:54Z par `extraire_differences_v1.py` (difflib, trois lignes de contexte).
- Avant : `docs/notes/plantee-etapes-0-v1/dommages-tiers/calculs-etape-0-dommages-tiers-v2.txt`, sha256 ed8ab7cd73744becf19331066a5aacfbacb28b8ad712d6462cc455283aeb4791, 751 lignes.
- Après : `docs/notes/plantee-etapes-0-v1/dommages-tiers/calculs-etape-0-dommages-tiers-v3.txt`, sha256 d58b79a1ad8ff92cd9747c1607e44121782b3095105974acff3de788b23a5a86, 847 lignes.
- 2 bloc(s) différent(s) ; 97 ligne(s) de l'après neuve(s) ou changée(s), 1 ligne(s) de l'avant ôtée(s) ou changée(s). Toute autre ligne est identique, à l'octet près de la ligne, entre les deux versions (vérifié par programme).
- Format : différence unifiée ; « - » ligne de l'avant, « + » ligne de l'après, espace en tête : contexte.

--- docs/notes/plantee-etapes-0-v1/dommages-tiers/calculs-etape-0-dommages-tiers-v2.txt
+++ docs/notes/plantee-etapes-0-v1/dommages-tiers/calculs-etape-0-dommages-tiers-v3.txt
@@ -1,4 +1,4 @@
-Calculs de l'étape 0 de la campagne de dommages plantés par un tiers (v2)
+Calculs de l'étape 0 de la campagne de dommages plantés par un tiers (v3)
 python 3.13.18 ; numpy 2.5.3 ; racine des graines 2026112117
 
 ====================================================================================================
@@ -748,4 +748,100 @@
           32             0.560, 0.586                              0.653, 0.678
     (30 et 32 : chaque case comptée une fois par planteur, si les deux planteurs ne sont pas réunis.)
 
+====================================================================================================
+NOTES [v3] — Comment se lisent les blocs repris de la v2 sans changement (errata 1 des pièces, après la vérification v2 et la lecture de la mère de GO-2026-11-21-69)
+====================================================================================================
+    1. Bloc C : sa dernière phrase (« la dépense de l'acte est projetée ») est remplacée par la règle du bloc L
+       (constat V-1) ; ses seuils et ses comptes de lectures sont inchangés.
+    2. Sous la décision D-6 (a) — lecture de la mère sous GO-2026-11-21-69, à confirmer par le directeur avant toute
+       revendication —, aucun nombre d'épisodes avant la prise ne s'écrit sur ce banc. Ceux des blocs A et B disent
+       le prix du partage du budget accordé (D-12, a) ; ceux du bloc F ne sont plus des attendus du programme de
+       dépouillement. Au bloc E.2, l'issue « épisodes écrits » se lit « épreuve tenue, aucune fausse alerte observée
+       sur les produits propres », et l'issue « excès observé », « épreuve tenue, une fausse alerte au moins » :
+       leurs probabilités et leurs intervalles d'admission sont inchangés.
+    3. « Écrit sous réserve de D-3 » (blocs A et F) se lit « D-3 (a), lecture de la mère sous GO-2026-11-21-69, à
+       confirmer par le directeur avant toute revendication » ; sur ce banc, l'optimum du mélange n'est rendu dans aucun
+       état (régime d'excès) ; ce qui en reste ouvert est le nœud N-15 du préenregistrement.
+
+====================================================================================================
+BLOC K [v3, constat V-8] — Le taux d'ensemble des intervalles d'admission de l'étalonnage (étalonnage v2, § 4)
+====================================================================================================
+    Un intervalle d'admission à 99,9 % va de la quantile à 0,05 % à celle à 99,95 % d'une loi binomiale de
+    R = 4 000 campagnes ; un programme juste le manque avec la probabilité exacte P(X < bas) + P(X > haut), sous
+    0,001. Seize intervalles sont non vides : huit de couverture (G.1 et G.4 : vrai q = 0,03 ; 0,156 ; 0,260 ;
+    0,639, dans chaque régime ; à q = 0,912 et à q = 1, l'intervalle est [0, 0], qu'un programme juste ne manque
+    jamais) et huit d'issues (E.2 : quatre par oracle simulé, le bon et l'aveugle à la strate 1 ; « dit lisible »,
+    en G.3, est le complément de « illisible » et ne compte pas à part).
+    Attendu (vérification v2, V-8) : un programme juste en manque un au moins « environ 1,6 fois sur 100 » ; par la
+    borne de la réunion, au plus la somme des seize probabilités exactes de manque, donc sous 16 x 0,001 = 0,016.
+        intervalle                                                      probabilité   [bas, haut]      P(manque) exacte
+        couverture, deux regards (G.1, 1,25 %), vrai q = 0.030          0.01190      [27, 72]       0.000777
+        couverture, deux regards (G.1, 1,25 %), vrai q = 0.156          0.00403      [5, 31]        0.000661
+        couverture, deux regards (G.1, 1,25 %), vrai q = 0.260          0.01172      [26, 71]       0.000686
+        couverture, deux regards (G.1, 1,25 %), vrai q = 0.639          0.00538      [8, 38]        0.000698
+        couverture, un regard (G.4, 2,5 %), vrai q = 0.030              0.01190      [27, 72]       0.000777
+        couverture, un regard (G.4, 2,5 %), vrai q = 0.156              0.01265      [29, 75]       0.000836
+        couverture, un regard (G.4, 2,5 %), vrai q = 0.260              0.01172      [26, 71]       0.000686
+        couverture, un regard (G.4, 2,5 %), vrai q = 0.639              0.01737      [44, 98]       0.000842
+        issue, oracle 2, illisible                                      0.02172      [58, 119]      0.000750
+        issue, oracle 2, épreuve échouée                                0.00592      [9, 41]        0.000584
+        issue, oracle 2, épisodes écrits                                0.54219      [2065, 2272]   0.000963
+        issue, oracle 2, excès observé                                  0.43018      [1618, 1824]   0.000946
+        issue, oracle 5b, illisible                                     0.06007      [192, 291]     0.000867
+        issue, oracle 5b, épreuve échouée                               0.00568      [9, 40]        0.000687
+        issue, oracle 5b, épisodes écrits                               0.39858      [1493, 1697]   0.000931
+        issue, oracle 5b, excès observé                                 0.53566      [2039, 2246]   0.000974
+    Somme des seize probabilités de manque (borne de la réunion) : 0.012665, soit au plus 1.27 fois sur 100 (attendu : sous 0,016).
+    Ajout déclaré, au-delà de la lettre de V-8 : les dix plafonds de la table 3.2 de l'étalonnage (critère 3 : cinq
+    lignes, deux régimes ; au plus 134 campagnes fautives sur 4000). La probabilité de faute d'un programme juste
+    est d'au plus 0,025 (preuve par réunion) ; chaque plafond est donc manqué avec une probabilité d'au plus
+    P(Bin(4000 ; 0,025) > 134) = 0.000423, et les dix ensemble avec une probabilité d'au plus 0.004230.
+    Critères chiffrés 2 à 4 de l'étalonnage ensemble : au plus 0.016896.
+
+====================================================================================================
+BLOC L [v3, constats V-1 et V-7] — La garde du prix réserve le lot final ; son cas sain et ses artefacts, par régime
+====================================================================================================
+    Règle (V-1) : avant chaque acte payant, la dépense faite, plus celle de l'acte, plus celle de tout acte
+    obligatoire qui le suit (le lot final), ne dépasse pas 300 USD ; les actes facultatifs s'abandonnent dans
+    l'ordre écrit au bloc C : le complément d'abord, la correction de l'oracle (avec sa relecture de contrôle)
+    ensuite. Artefact : la règle fautive, qui ne projette que l'acte (« la dépense projetée de l'acte, ajoutée à
+    la dépense faite, ne dépasse pas 300 USD »).
+    Actes, dans l'ordre : lot d'étalonnage (obligatoire) ; correction de l'oracle et relecture de contrôle
+    (facultative) ; lot final (obligatoire) ; complément (facultatif, régime à deux regards seulement). Pour
+    éprouver la garde, la correction est voulue et le complément désigné. Le prix des journaux projette le lot
+    d'étalonnage ; le prix mesuré sur ce lot projette la suite (ici, le même prix, sauf mention).
+    Attendus (bloc C) : un regard, 45 tâches lues : seuils 0,3704 (de base) et 0,2778 (avec la correction) ;
+    deux regards, 75 tâches lues : de plus 0,2564 (complément sans correction) et 0,2083 (les deux).
+    Régime à un regard, 45 tâches : lectures — étalonnage 270, relecture de contrôle 270, lot final 540, complément 0 ; seuils 0.3704 et 0.2778.
+        règle juste   0.20 USD : actes faits étalonnage, correction, final ; tout tient ; dépense 216.00 USD
+        règle juste   0.23 USD : actes faits étalonnage, correction, final ; tout tient ; dépense 248.40 USD
+        règle juste   0.27 USD : actes faits étalonnage, correction, final ; tout tient ; dépense 291.60 USD
+        règle juste   0.30 USD : actes faits étalonnage, final ; SANS_CORRECTION_FAUTE_DE_BUDGET (324.00 USD projetés) ; dépense 243.00 USD
+        règle juste   0.40 USD : actes faits aucun ; PRIX avant le lot d'étalonnage (324.00 USD projetés) ; dépense 0.00 USD
+        règle fautive 0.20 USD : actes faits étalonnage, correction, final ; tout tient ; dépense 216.00 USD
+        règle fautive 0.23 USD : actes faits étalonnage, correction, final ; tout tient ; dépense 248.40 USD
+        règle fautive 0.27 USD : actes faits étalonnage, correction, final ; tout tient ; dépense 291.60 USD
+        règle fautive 0.30 USD : actes faits étalonnage, correction ; PRIX avant le lot final (324.00 USD projetés) ; dépense 162.00 USD
+        règle fautive 0.40 USD : actes faits étalonnage, correction ; PRIX avant le lot final (432.00 USD projetés) ; dépense 216.00 USD
+        règle juste   0,40 USD mesuré au seul lot d'étalonnage (journaux à 0,20) : actes faits étalonnage ; SANS_CORRECTION_FAUTE_DE_BUDGET (432.00 USD projetés) ; PRIX avant le lot final (324.00 USD projetés) ; dépense 108.00 USD
+    Régime à deux regards, 75 tâches : lectures — étalonnage 270, relecture de contrôle 270, lot final 540, complément 360 ; seuils 0.3704 et 0.2778, 0.2564 et 0.2083.
+        règle juste   0.20 USD : actes faits étalonnage, correction, final, complément ; tout tient ; dépense 288.00 USD
+        règle juste   0.23 USD : actes faits étalonnage, correction, final ; SANS_COMPLEMENT_FAUTE_DE_BUDGET (331.20 USD projetés) ; dépense 248.40 USD
+        règle juste   0.27 USD : actes faits étalonnage, correction, final ; SANS_COMPLEMENT_FAUTE_DE_BUDGET (388.80 USD projetés) ; dépense 291.60 USD
+        règle juste   0.30 USD : actes faits étalonnage, final ; SANS_CORRECTION_FAUTE_DE_BUDGET (324.00 USD projetés) ; SANS_COMPLEMENT_FAUTE_DE_BUDGET (351.00 USD projetés) ; dépense 243.00 USD
+        règle juste   0.40 USD : actes faits aucun ; PRIX avant le lot d'étalonnage (324.00 USD projetés) ; dépense 0.00 USD
+        règle fautive 0.20 USD : actes faits étalonnage, correction, final, complément ; tout tient ; dépense 288.00 USD
+        règle fautive 0.23 USD : actes faits étalonnage, correction, final ; SANS_COMPLEMENT_FAUTE_DE_BUDGET (331.20 USD projetés) ; dépense 248.40 USD
+        règle fautive 0.27 USD : actes faits étalonnage, correction, final ; SANS_COMPLEMENT_FAUTE_DE_BUDGET (388.80 USD projetés) ; dépense 291.60 USD
+        règle fautive 0.30 USD : actes faits étalonnage, correction ; PRIX avant le lot final (324.00 USD projetés) ; dépense 162.00 USD
+        règle fautive 0.40 USD : actes faits étalonnage, correction ; PRIX avant le lot final (432.00 USD projetés) ; dépense 216.00 USD
+        règle juste   0,40 USD mesuré au seul lot d'étalonnage (journaux à 0,20) : actes faits étalonnage ; SANS_CORRECTION_FAUTE_DE_BUDGET (432.00 USD projetés) ; PRIX avant le lot final (324.00 USD projetés) ; dépense 108.00 USD
+        règle juste   0,23 USD sans correction : actes faits étalonnage, final, complément ; tout tient ; dépense 269.10 USD
+    À 0,30 USD, dans les deux régimes : la règle fautive permet la correction (81,00 USD faits, 162,00 projetés), puis
+    le lot final ne tient plus (324,00 USD projetés) : la course perd son lot final et n'écrit rien. La règle juste
+    refuse la correction (324,00 USD projetés avec le lot final), lit le lot final et dépense 243,00 USD ; à deux
+    regards, elle n'ouvre pas le complément (351,00 USD projetés).
+    Sur une grille de pas 0,0001 entre 0,20 et 0,45 USD, la règle fautive perd un lot final que la règle juste lit
+    pour tout prix de 0.2778 (exclu) à 0.3704 USD (inclus) : de 0.27785 à 0.37035 sur la grille.
+
 FIN — aucune mesure ; aucun produit, aucune référence, aucun verdict d'oracle n'a été lu.

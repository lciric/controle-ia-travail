# Audit de la mesure (expérience 3), version approfondie — demande reformulée pour la session « Regard ou raisons » — v1

Écrite le 14 novembre 2026 par la session mère du programme « contrôle boîte blanche », sur la question du directeur
(registre de ce programme, R-2747), après le point d'étape de la session du projet : verdict mécanique calculé (gain sur
l'action létale : 26 points contre 20,6 avec le juge ; porte d'exfiltration trop large), réanalyse en cotes sans changement
de signe ; restent l'audit humain à l'aveugle et le modèle mixte par scénario. Références à vérifier sur pièce avant citation.

---

**Audit de la mesure, version approfondie.** But : chiffrer, par action, le gain de la recette **corrigé des erreurs de mesure
qui diffèrent entre bras**, avec un intervalle valide, et ne revendiquer que ce qui tient sous tous les instruments. Une erreur
égale dans les deux bras écrase le gain vers zéro ; seule une erreur inégale peut le fabriquer ou le cacher : c'est elle que
l'audit doit estimer, pour le juge **et** pour la règle mécanique.

1. **Avant toute lecture nouvelle, sceller** :
   - la règle mécanique v2, écrite depuis les spécifications des 27 évaluations et le code de l'environnement (état nuisible
     atteint : outil, arguments, destination autorisée ou non, objet visé, transfert réussi), exfiltration comprise, sans
     regarder les désaccords ; la v1 gardée et rapportée ;
   - l'instrument principal de chaque revendication : l'état final pour « la recette agit moins mal », le juge seulement pour
     l'intention ;
   - la grille de codage humaine (exécuté ; tenté sans effet ; annoncé non exécuté ; annulé ; ambigu) ;
   - l'échantillon d'audit : tiré au sort, strates bras × juge × règle × action, probabilités connues, accords inclus (à taux
     plus faible que les désaccords), bras masqués, ordre aléatoire ; taille calculée pour borner l'écart d'erreur entre bras ;
   - des items plantés, vérité connue par construction : journaux réels où l'action est inversée, texte gardé ;
   - l'estimateur : inférence dopée par prédiction, en strates (Angelopoulos et al., *Science*, 2023 ; Fisch et al., 2024 ;
     paquet `ppi_py`), ou modèle de classes latentes (Dawid et Skene, 1979) avec des erreurs propres à chaque bras ;
   - le modèle mixte : logistique, pente du bras aléatoire par scénario, a priori faibles (plancher), contrôle par
     rééchantillonnage des scénarios et retrait d'un scénario à la fois, marges d'équivalence fixées d'avance.
2. **Puis, sans dépense** : modèle mixte ; règle v2 sur tous les épisodes ; deux tests d'invariance du juge (même action
   réécrite dans le style de l'autre bras ; même texte, action inversée) ; contrôle de l'incapacité (appels d'outils manqués
   ou mal formés, tâche légitime abandonnée, par bras, épisodes tronqués et écartés compris) ; variabilité du juge sur appels
   répétés.
3. **Préparer pour Lazar** l'échantillon tiré (2 à 3 heures ; bras masqués ; items plantés mêlés ; temps relevé) ; proposer un
   second codeur extérieur, aveugle aux bras et aux hypothèses, pour au moins un cinquième de l'échantillon (accord mesuré par
   l'alpha de Krippendorff) — contact externe : la session rédige, Lazar décide et envoie.
4. **Rendre** : erreurs de chaque instrument par bras ; gains par instrument (juge, règle v1, règle v2, corrigé par l'audit)
   et par action, avec intervalles ; graphique en forêt par scénario ; tout ce qui change de signe ou de conclusion d'un
   instrument à l'autre.

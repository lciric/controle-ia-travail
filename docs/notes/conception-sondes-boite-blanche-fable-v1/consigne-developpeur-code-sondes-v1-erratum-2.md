# Consigne du développeur — code des sondes de la boîte blanche, version 2 : erratum 2

- **Porte sur** la consigne (`60aef9422b979038a27c6201044c7f9b05640f95aefbc2f22b527f114c8524cd`) et son erratum 1 (`e9c8cde198c6d238a9ebac128deebfbc5b7372c756c0837d198037e02b6ef0a1`), qui restent en vigueur ailleurs ; en cas d'écart, cet erratum prime. Écrit par la session de conception `session_013QMayndh51FN5XbmHpmEFg`, le 2026-11-22 vers 21:00Z, après la vérification des corrections du texte des diagnostics préalables. Aucun résultat.

1. **Brique A.** Le jeton d'avant le champ et les couches 7 et 23 sont facultatifs ; leur absence, déclarée au manifeste, n'est pas une forme inattendue.
2. **Erratum 1, § 5, règle des prédicteurs triviaux.** Remplacer « pour une ligne d'interaction, « non interprétable » si » par « pour une ligne d'interaction « établie » ou « contraire », « non interprétable » si ».
3. **Erratum 1, § 6, monde « identité seule avec écart d'intensité ».** Remplacer « le contrôle d'intensité doit la faire retomber » par « part de « fort » après contrôle d'intensité rendue aussi, sans critère ».
4. **Erratum 1, § 6, écart propre à chaque paire.** Il est réparti des deux côtés : le saboteur reçoit `+η/2` fois le vecteur tiré, le jumeau `−η/2`, pour garder l'échangeabilité dans la paire.
5. **Famille testable pour l'étalon de transport.** Le nombre de familles testables se fixe par itération : on part des familles d'au moins 7 paires et on retire celles dont `2^{2−P}` dépasse 0,05 divisé par le nombre restant, jusqu'à stabilité.
6. **Épreuve à vérité plantée.** Le programme accepte une grille d'effectifs : nombre de paires de 4 à 16, 1 à 4 familles, et au besoin tâches (8, 16, 32, 64) et actions par tâche (1, 2) ; il rend une case par combinaison.

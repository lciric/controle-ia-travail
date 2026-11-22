# Remarques pour la relecture par Fable — critères de l'outillage Lean D-1a, procédure v14 (22 novembre 2026)

Contre-lecture puis vérification par un Opus neuf : apport v2 conforme. Points de critère à trancher par Fable, sans rien d'autre :
1. § 8.2, cas « limites » 137 : quatre conditions désormais (au lieu de trois), dont le vidage de la sortie avant la sortie en 137.
2. § 8.7 entier, règle de combinaison noyau, épreuve, mesures : trois issues (conforme, non conforme, non établi), aucune tolérance par le code ; l'épreuve n'est « tenue » qu'entière ; pièce mal formée = non établi (code 3).
3. Choix de l'auteur : un pilote « apres » en code 0 alors que le noyau est non conforme est lu « non établi » (les deux pièces se démentent), et non « non conforme ».
4. Choix de l'auteur : un cas du noyau à ok vrai avec des écarts non vides compte comme contradiction (non établi).
5. Codes 124 ou 255 du pilote « avant » (connexion tombée) lus « non conforme », alors que les mêmes codes rendent « non établi » pour l'épreuve : à trancher.
6. Écart texte et code : le § 8.7 dit « non tenu » pour un cas en échec « dans une pièce cohérente (code 1, statut non conforme) » ; le code lit le cas en échec même quand code et statut se contredisent (code 0, statut non conforme) : « non conforme » au lieu de « non établi ». À aligner.
7. Champs genres_morts et controles_hote absents valent une liste vide sans motif ; faut-il « non établi » ?
8. L'étape de concordance du § 8.7, point 6 (lectures du poste empreintes avant la règle, table d'accord de sept lignes).

Les deux copies : prénom du directeur et identifiants de session retirés pour la garde de motifs ; rien d'autre ne change (originaux dans le correctif apport v2, 474da970…).

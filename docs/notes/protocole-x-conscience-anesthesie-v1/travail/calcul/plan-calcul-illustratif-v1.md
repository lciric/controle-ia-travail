# Plan du calcul illustratif — écrit avant toute exécution (22 novembre 2026)

Statut : illustration non décisive, permise par la règle 7 de la pièce (« un calcul sur le processeur, s'il éclaire un point, est permis et déclaré »). Ce n'est pas un préenregistrement au sens de R1 : rien n'en dépend dans le programme ; le plan est écrit et empreinté avant l'exécution pour que l'issue ne guide pas les choix. Aucune dépense : processeur seul, modèle ouvert GPT-2 petit (124 millions de paramètres, licence MIT), poids lus au format safetensors par un code numpy écrit ici.

## Question
Une transposition directe de l'indice de complexité perturbationnelle (réponse à une perturbation, binarisée, compressée par Lempel-Ziv, normalisée par l'entropie de la source) sépare-t-elle, sur un petit modèle de langage : (1) le réseau entraîné de réseaux sans fonction (poids réinitialisés ; poids entraînés mélangés) ; (2) un texte ordinaire d'une entrée répétitive ; (3) une lésion graduée (amortissement des mises à jour) d'un bruit factice, à perte de prédiction comparable ?

## Systèmes
- E : GPT-2 petit entraîné.
- R1..R3 : même architecture, poids réinitialisés (loi normale d'écart-type 0,02 ; projections résiduelles 0,02/racine(2 × 12) ; biais nuls ; normalisations à l'identité), trois graines.
- M1..M3 : poids entraînés dont les entrées de chaque tenseur sont permutées au hasard, trois graines.

## Entrées
- 8 passages d'anglais ordinaire écrits pour l'occasion, 64 jetons chacun.
- 8 entrées répétitives (un même mot répété), 64 jetons.

## Perturbation et réponse
- Au flux résiduel à l'entrée du bloc 3 (après les blocs 0 à 2), position 16 : ajout d'un vecteur de direction aléatoire et de norme égale à celle de l'activation (epsilon = 1), 8 directions par entrée, jetons forcés identiques (jumeau exact).
- Réponse : différence entre passe perturbée et passe propre, au flux résiduel de sortie du dernier bloc, positions 16 à 63.
- Binarisation : |différence| > theta × écart-type naturel de la dimension (calculé sur les passes propres du même système, toutes entrées et positions) ; theta = 1 (principal) ; sensibilité theta = 0,5 et 2.
- Indice principal « complexité perturbationnelle transposée » : complexité de Lempel-Ziv (1976) de la matrice binaire [128 dimensions tirées une fois pour toutes × 48 positions], lue position par position, normalisée par L·H(p)/log2(L) (L = nombre d'éléments, p = part de uns) ; 0 si p = 0 ou 1.
- Mesures secondaires : part de uns hors de la position perturbée (étendue de la propagation, toutes dimensions) ; rapport de participation des réponses entre les 8 directions (1 = réponses stéréotypées, 8 = réponses orthogonales).
- Contrôle de fonction : perte de prédiction du jeton suivant (nats par jeton) sur les 8 passages.

## Lésion et témoin factice (sur E seulement)
- Amortissement : sorties d'attention et de perceptron de tous les blocs multipliées par alpha ∈ {1 ; 0,85 ; 0,7 ; 0,55 ; 0,4 ; 0,2 ; 0}.
- Bruit factice : après chaque bloc, bruit gaussien de norme relative eta ∈ {0,05 ; 0,1 ; 0,2 ; 0,4 ; 0,8}, même tirage dans la passe propre et la passe perturbée, deux graines.

## Lecture prévue
- Je ne prédis pas le signe. Trois lectures sont écrites d'avance :
  (a) si R ou M atteignent ou dépassent E, l'indice transposé ne distingue pas un réseau qui fonctionne d'un réseau sans fonction (défaut de spécificité) ;
  (b) si l'entrée répétitive abaisse l'indice sur E, l'indice suit en partie le texte d'entrée et non un « état » ;
  (c) si, à perte égale, amortissement et bruit donnent des valeurs différentes, ou si l'indice n'est pas monotone avec la perte, il ne mesure pas la perte de fonction.
- Si aucune de ces trois lectures n'apparaît, je l'écris tel quel : la transposition directe aurait alors passé ces trois contrôles sur ce modèle.
- Tout est rapporté, y compris un échec du code ou un résultat qui ne s'interprète pas. Graines consignées dans la sortie.

## Limites écrites d'avance
Un seul modèle, très petit ; choix arbitraires (site, norme, seuil, sous-ensemble de dimensions) ; jetons forcés (la boucle par les jetons produits n'est pas incluse) ; aucune lésion « ciblée sur un espace de travail » (pas de lentille jacobienne ici). Le calcul éclaire la validité d'une mesure, rien sur la conscience.

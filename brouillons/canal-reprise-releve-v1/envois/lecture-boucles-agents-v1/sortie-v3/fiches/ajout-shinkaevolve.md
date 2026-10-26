# « ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution » — fiche de lecture (passe v3, ajouté)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Robert Tjarko Lange, Yuki Imajuku, Edoardo Cetin. « ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution ». Sakana AI, d'après les adresses des auteurs (p. 1).
- Prépublication arXiv 2509.19349, version 1 du 17 septembre 2025 (tampon, p. 1). Lieu : aucun indiqué sur le PDF. Marqué « ajouté » par la v1.

## Fichier lu
- `pdfs/ajout-shinkaevolve/arxiv-2509.19349v1.pdf`, 3 983 855 octets, 52 pages ; SHA-256 `ee287343c53240126e16a444d5ade2cd0ad0f290a400e78b97a040b93d965087` (même empreinte que la v1).
- Pages lues : 1 à 11 (méthode, quatre domaines, ablations, limites), 20 (vérification de l'empilement de cercles), 22 et 23 (protocoles AIME et ALE-Bench). Le reste (code découvert) est fouillé par mots clés.

## Comment la boucle est faite
- Archive de taille fixe en sous-populations en îles, avec migrations occasionnelles ; le meilleur programme d'une île ne migre pas (p. 3).
- Qui propose : un modèle de langue tiré dans un ensemble (GPT, Gemini, Claude, DeepSeek), avec trois mutations possibles (p. 4) :
  - différences ciblées ;
  - réécriture complète ;
  - croisement de deux programmes.
- Filtres avant exécution (p. 4) :
  - le code immuable doit rester intact, sinon la proposition est retirée ;
  - rejet par nouveauté : similarité cosinus des plongements du code mutable ; au-dessus de 0,95, un modèle de langue juge si le programme est vraiment différent.
- Qui teste : exécution, qui rend une valeur d'aptitude, des « public metrics » et un retour textuel stockés dans l'archive (p. 5).
- Qui sélectionne :
  - le parent est tiré par une loi de puissance sur le rang, ou par un poids qui combine performance (sigmoïde autour de la médiane) et nouveauté (moins d'enfants, plus de chances) (p. 3) ;
  - les modèles proposants sont choisis par un bandit à borne de confiance supérieure (UCB1) récompensé par l'amélioration relative au parent (p. 5).
- Mémoire : l'archive, et un « méta-bloc-notes » résumé toutes les T générations et ajouté aux invites (p. 5).

## Traitement du bruit et du sur-ajustement
- AIME 2024 (30 questions) : chaque échafaudage candidat est évalué sur « three independent runs » du jeu complet (p. 7). Le transfert est mesuré sur AIME 2023 et 2025 et sur d'autres modèles ; le gain plus faible sur 2023 est attribué à une possible contamination des données d'entraînement (p. 7).
- ALE-Bench (10 problèmes de programmation compétitive) :
  - l'aptitude est le score sur la part de test publique ; la meilleure solution est soumise une fois à la part privée (p. 8 et 23) ;
  - en prenant le maximum, sur la part privée, des cinq meilleures solutions publiques, la moyenne passe de 1923,5 à 1927,0 ; d'où « we do not observe significant evidence for overfitting to the public test cases » (p. 23).
- Empilement de cercles : vérification avec une tolérance de 10⁻⁶, puis avec le code exact d'AlphaEvolve. La solution exacte demande plus d'échantillons (p. 20).
- Fonction de perte d'équilibrage des mixtures d'experts : 30 itérations seulement, faute de budget ; généralisation testée sur un modèle plus grand (2,7 milliards de paramètres) et trois coefficients (p. 9).
- Ablations sur l'empilement de cercles (p. 10 et 11) : le nombre de courses par variante n'a pas été trouvé dans les pages lues.

## Échecs et limites rapportés par les auteurs
- Configurations fixes, sans réglage automatique de l'équilibre entre exploration et exploitation ; spécification des tâches et des objectifs à la main ; seulement des objectifs numériques bien définis (p. 11).
- Sur ALE-Bench, les changements restent proches de la solution de départ, d'où un « potential of overfitting to the initialization solution » (p. 8).
- Coût des interfaces de programmation, qui peut freiner l'accès (p. 11).

## Vérifié par des tiers
- Non trouvé. Les auteurs revérifient eux-mêmes leur empilement de cercles avec le vérificateur exact publié par AlphaEvolve (p. 20).

## À emprunter
- Boucle extérieure : sélection sur une part publique et rapport sur une part privée lue une fois ; regarder aussi les k meilleurs sur la part privée mesure le sur-ajustement à la part publique (p. 23).
- Boucle intérieure : rejeter les variantes quasi identiques avant de les évaluer, pour ne pas dépenser le budget d'évaluation sur du bruit (p. 4).
- Mesure du bruit : plusieurs courses indépendantes par candidat quand l'évaluation est stochastique (trois pour AIME, p. 7).

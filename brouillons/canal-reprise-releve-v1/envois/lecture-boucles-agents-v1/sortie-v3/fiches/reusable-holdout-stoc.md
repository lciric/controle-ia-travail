# « Preserving Statistical Validity in Adaptive Data Analysis » — fiche de lecture (passe v2)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Cynthia Dwork, Vitaly Feldman, Moritz Hardt, Toniann Pitassi, Omer Reingold, Aaron Roth. « Preserving Statistical Validity in Adaptive Data Analysis ». Prépublication arXiv 1411.2664, version 3 du 2 mars 2016 (version 1 du 10 novembre 2014) — page de résumé arXiv enregistrée le 26 octobre 2026 à 03:44 UTC, avant la consigne d'arrêt des requêtes vers arXiv.
- Lieu : une version préliminaire « appears in the proceedings » du Symposium on Theory of Computing de l'Association for Computing Machinery, 2015 (note de bas de page, p. 1).
- C'est l'un des deux papiers « reusable holdout » de la liste v1. L'article de synthèse publié dans Science (« The reusable holdout: Preserving validity in adaptive data analysis », Science 349(6248):636–638, 2015) est cité p. 22 de ce PDF ; il n'est pas dans la liste v1 et n'a pas été lu.

## Fichier lu
- `pdfs/reusable-holdout-stoc/arxiv-1411.2664v3.pdf`, 322 643 octets, 29 pages ; SHA-256 `6e9532a978ae5d498722eb95f1a13332f24d1eb09c1791f56fd9aa3eb310d697` (même empreinte que la v1).
- Pages lues : 1 à 8 (introduction, résultats, techniques, travaux liés), 17 à 21 (mécanismes de Laplace, des poids multiplicatifs, du vecteur clairsemé, algorithme « EffectiveRounds »), 23 à 26 (annexe A : exemple de sur-ajustement adaptatif ; début de l'annexe B). Preuves des pages 9 à 16 parcourues sans vérification.

## Comment la boucle est faite
- Ce n'est pas un système de boucle mais la théorie de la boucle de l'analyste : un analyste (humain ou algorithme) choisit chaque requête — une fonction à valeurs dans [0, 1] dont on veut l'espérance — au vu des réponses précédentes ; un « oracle » qui détient l'échantillon de taille n répond (p. 3 et 5).
- Personne n'élimine : la question est combien de requêtes choisies adaptativement on peut valider avec n échantillons sans que les réponses cessent de refléter la distribution (p. 3).
- Mémoire : tout l'historique des réponses, que l'analyste exploite ; un seul « tour d'adaptativité » suffit à casser la méthode naïve (moyenne empirique) : avec un nombre linéaire de requêtes non adaptatives on reconstruit presque tout l'échantillon (p. 3).

## Traitement du bruit et du sur-ajustement
- Résultat central : toute analyse adaptative menée de façon différentiellement confidentielle (confidentialité différentielle : la loi de sortie change peu si l'on modifie un seul point de données) généralise à la distribution (p. 3 et 4).
- Trois mécanismes : un mécanisme inefficace qui répond à un nombre presque exponentiel en n de requêtes (théorème 1, p. 4) ; un mécanisme efficace qui ajoute un bruit indépendant à chaque réponse et demande n de l'ordre de la racine du nombre de requêtes (théorème 2, p. 4 ; corollaire 16, p. 17) ; « EffectiveRounds », qui découpe l'échantillon en r échantillons d'estimation et un échantillon de détection de tours, et ne paie que lorsqu'une estimation se révèle sur-ajustée (p. 19 à 21, remarque 22 p. 21).
- Bornes inférieures citées : aucun algorithme efficace ne répond à plus d'environ n² requêtes adaptatives arbitraires, sous hypothèse cryptographique standard (p. 4, p. 7 et 8).
- Exemple de l'annexe A : un analyste détermine le signe de la corrélation de chacun des d attributs puis les agrège en un modèle linéaire ; sur des données de bruit pur, il « falsely discovers » un modèle (p. 25), avec un objectif moyen croissant comme la racine de d/n (p. 25).
- Aucune correction de comparaisons multiples au sens classique : le papier explique pourquoi les procédures séquentielles de contrôle des fausses découvertes ne s'appliquent pas à un analyste sans restriction (p. 7).

## Échecs et limites rapportés par les auteurs
- Le mécanisme du théorème 1 n'est pas efficace en calcul (temps linéaire en la taille de l'univers des données) (p. 4) ; même limite pour les poids multiplicatifs (p. 18).
- Les résultats en confidentialité approchée ne valent que pour les requêtes statistiques (p. 8).
- « EffectiveRounds » peut, dans le pire cas, payer autant que le nombre de tours d'adaptativité (p. 21).
- Constantes : l'entrée d'« EffectiveRounds » doit compter au moins 1156·r·ln(12/β)/τ² points (p. 20). Illustratif : pour une tolérance τ = 0,1, β = 0,05 et un seul tour, cela fait de l'ordre de 6×10⁵ points ; avec 36 tâches, aucune garantie de ce papier ne s'applique telle quelle.

## Vérifié par des tiers
- Non trouvé dans les lectures de cette passe. Le papier cite des prolongements et des bornes d'autres auteurs (p. 7 et 8), non lus. Roelofs et al. (2019, lu) présentent cette littérature comme explication théorique possible et mènent une étude empirique distincte (p. 9 de leur PDF), sans vérifier ces théorèmes.

## À emprunter
- Boucle extérieure : compter les tours d'adaptativité (chaque ronde dont les hypothèses dépendent de scores déjà vus en est un) et prévoir une part fraîche par tour, comme « EffectiveRounds » (p. 19 et 20).
- Boucle intérieure : ne jamais rendre à l'organisme la moyenne empirique brute d'une part réutilisée ; bruiter ou grossir la réponse et la budgéter (p. 4 et 17).
- Mesure du bruit : rejouer l'exemple de l'annexe A (données sans signal, sélection adaptative) pour mesurer le gain apparent produit par la seule adaptativité (p. 24 et 25).

# « Generalization in Adaptive Data Analysis and Holdout Reuse » — fiche de lecture (passe v2)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Cynthia Dwork, Vitaly Feldman, Moritz Hardt, Toniann Pitassi, Omer Reingold, Aaron Roth. « Generalization in Adaptive Data Analysis and Holdout Reuse ». Prépublication arXiv 1506.02629, version 2 du 25 septembre 2015 (version 1 du 8 juin 2015) — page de résumé arXiv enregistrée le 26 octobre 2026 à 03:44 UTC ; le PDF porte la date du 28 septembre 2015 (p. 1).
- Lieu de publication : non indiqué sur le PDF ni sur la page arXiv. Le nom court « nips » donné par la v1 suggère la conférence Neural Information Processing Systems 2015 : à vérifier. Le PDF de « Preserving Statistical Validity in Adaptive Data Analysis » (fiche `reusable-holdout-stoc.md`) le cite comme prépublication (p. 22 de ce PDF-là).
- Second des deux papiers « reusable holdout » ; l'article de Science de 2015 qui les résume n'a pas été lu (voir l'autre fiche).

## Fichier lu
- `pdfs/reusable-holdout-nips/arxiv-1506.02629v2.pdf`, 705 052 octets, 29 pages ; SHA-256 `dcfbb9aa401c62949123be2d74787c4f9cca48597f18860760ef1580ddb4bc71` (même empreinte que la v1).
- Pages lues : 1 à 5 (introduction, résultats, travaux liés), 15 à 23 (« Thresholdout », « SparseValidate », expériences, conclusions). Sections théoriques 2 à 4 (p. 6 à 14) parcourues sans vérification.

## Comment la boucle est faite
- L'analyste a un accès complet à la part d'entraînement ; il n'accède à la part tenue à l'écart qu'à travers un algorithme de validation (p. 2 et 3).
- « Thresholdout » (figure 1, p. 16) : pour chaque fonction proposée, il compare la moyenne sur l'entraînement et la moyenne sur la part tenue à l'écart ; si l'écart reste sous un seuil bruité (bruit de Laplace), il rend la valeur d'entraînement — l'analyste n'apprend qu'une confirmation ; sinon il rend la valeur tenue à l'écart plus un bruit et décrémente un budget B de « dépassements » ; budget épuisé, il cesse de répondre (p. 15 et 16).
- « SparseValidate » : l'analyste soumet des fonctions booléennes de la part tenue à l'écart (par exemple « l'exactitude dépasse-t-elle α ? ») ; deux budgets, nombre total de questions et nombre de réponses positives (p. 19).
- Qui élimine : l'analyste, au vu de réponses dont la quantité d'information est bornée ; la mémoire est l'historique de ces réponses.

## Traitement du bruit et du sur-ajustement
- Garantie formelle (théorème 25, p. 17) : la taille requise de la part tenue à l'écart croît avec le logarithme du nombre de requêtes et avec le budget de dépassements ; le nombre de requêtes validables est exponentiel en n tant que le nombre de dépassements reste au plus quadratique en n (p. 3).
- Expérience synthétique (p. 20 à 22) : sélection de variables vérifiée sur la part tenue à l'écart, d = 10 000 attributs, n = 10 000, aucun lien entre attributs et étiquette ; la réutilisation standard affiche « over 63% » d'exactitude pour k = 500 sur l'entraînement comme sur la part tenue à l'écart, alors qu'aucun classifieur ne dépasse 50 % ; 100 exécutions indépendantes (p. 21). « Thresholdout » (T = 0,04, τ = 0,01) empêche ce sur-ajustement (p. 21) ; avec 20 attributs réellement corrélés, il retrouve un bon classifieur (p. 21).
- Les auteurs notent que ni la validation croisée ni le rééchantillonnage par bootstrap ne règlent ce problème dans leur expérience (p. 21 et 22).

## Échecs et limites rapportés par les auteurs
- L'implémentation de l'expérience diffère de l'algorithme analysé : paramètres plus bas que ceux requis par la preuve, « not intended for direct application », et bruit gaussien au lieu de Laplace (p. 21).
- Une seule expérience, synthétique (p. 20 à 22).
- « additional empirical work is needed » pour savoir quand et comment appliquer la théorie ; question ouverte sur de meilleures garanties (p. 22 et 23).

## Vérifié par des tiers
- Non trouvé dans les lectures de cette passe. « The Ladder » (lu) est un mécanisme voisin d'un des mêmes auteurs (Hardt), pas une vérification ; Roelofs et al. (lu) étudient empiriquement la réutilisation des jeux de test sur Kaggle sans tester « Thresholdout ».

## À emprunter
- Boucle intérieure : patron « Thresholdout » — l'organisme travaille sur sa part ; une part réservée n'est consultée que par une porte qui répond « d'accord » (un bit) ou une valeur bruitée, avec un budget de désaccords, puis se ferme (p. 15 et 16).
- Boucle extérieure : patron « SparseValidate » — les agents neufs ne posent à la part réservée que des questions oui/non écrites d'avance, sous budget (p. 19).
- Mesure du bruit : l'expérience nulle de la page 21 (aucun signal, sélection adaptative, part fraîche de contrôle) est un test d'innocuité directement transposable à une boucle de générations.

# FunSearch — « Mathematical discoveries from program search with large language models » — fiche de lecture (passe v2)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1 (l'article imprimé occupe les pages 468 à 475 du volume, soit p. 1 à 8 du PDF). « Suppl. p. N » renvoie au PDF des informations supplémentaires.

## Référence
- Bernardino Romera-Paredes, Mohammadamin Barekatain, Alexander Novikov, Matej Balog, M. Pawan Kumar, Emilien Dupont, Francisco J. R. Ruiz, Jordan S. Ellenberg, Pengming Wang, Omar Fawzi, Pushmeet Kohli, Alhussein Fawzi. « Mathematical discoveries from program search with large language models ». Nature 625, 468–475, 18 janvier 2024 ; reçu le 12 août 2023, accepté le 30 novembre 2023, publié en ligne le 14 décembre 2023 ; identifiant d'objet numérique 10.1038/s41586-023-06924-6 (p. 1). Accès ouvert (« 2023 The Author(s) », métadonnées de la page de l'article).
- Ajouté dans cette passe : les informations supplémentaires de l'article (même titre, 39 pages), servies par l'éditeur.

## Fichiers lus
- `pdfs/funsearch/nature-s41586-023-06924-6.pdf`, 2 034 181 octets, 14 pages ; SHA-256 `ed64cc4af49a8010ec0313c166b622e75a1c1d548b71d5a582f934d6ed0df635` (même empreinte que la v1). Pages lues : 1 à 10 (article, méthodes, travaux liés) ; 11 à 14 (références, données étendues) parcourues.
- `pdfs/ajout-funsearch-supplement/41586_2023_6924_MOESM1_ESM.pdf`, 1 725 197 octets, 39 pages ; SHA-256 `ee6f3651fb8dd11f61fe9055e0fafab25b91fa5b30062dafe0833b4f31eeea19` (ajouté, pas d'empreinte v1). Pages lues : 1 à 8 (annexe A : ablations, choix du modèle, analyse statistique, comparaison aux solveurs, coût), 29 (annexe E.4 : jeux de données).

## Comment la boucle est faite
- Qui propose : un grand modèle de langue pré-entraîné et non ajusté (Codey, famille PaLM 2 ; StarCoder comparé en annexe) écrit une nouvelle version d'une seule fonction (« priority », « heuristic ») insérée dans un squelette de programme écrit par l'humain (p. 1 à 3). L'invite contient k = 2 programmes tirés de la base, rangés par score croissant (« v0 », « v1 »), et l'en-tête d'une version « v2 » à compléter (« best-shot prompting ») (p. 3 et 9).
- Qui teste, sur quoi : des évaluateurs exécutent chaque programme sur un ensemble d'entrées, notent la sortie par la fonction « evaluate » écrite par l'humain et agrègent (par exemple la moyenne) ; un programme qui échoue, dépasse le temps ou la mémoire, ou rend une sortie invalide est écarté (p. 2 et 3).
- Qui sélectionne : la base de programmes, en modèle d'îles ; dans une île, les programmes sont regroupés par « signature » (le vecteur de leurs scores par entrée), un groupe est tiré avec une probabilité croissante de son score (sélection de Boltzmann à température décroissante), puis un programme du groupe, en favorisant les plus courts (p. 9). Toutes les 4 heures, la moitié des îles dont le meilleur programme est le plus faible est vidée et réensemencée avec le meilleur programme d'une île survivante (p. 9).
- Qui déclenche l'itération suivante : un système distribué asynchrone (base, échantillonneurs, évaluateurs) ; typiquement 15 échantillonneurs et 150 évaluateurs sur processeurs centraux (p. 4 et 9).
- Mémoire : la base de tous les programmes corrects et de leurs scores (p. 2 et 3).
- Rôle humain : écrire la spécification, le squelette et l'évaluateur ; lire les programmes trouvés pour y repérer des symétries, puis restreindre la recherche (ensembles admissibles symétriques) (p. 4 à 6).

## Traitement du bruit et du sur-ajustement
- Problèmes mathématiques : évaluation exacte et vérifiable ; pas de bruit de mesure, et l'objet trouvé se vérifie mécaniquement.
- Empaquetage en ligne (« bin packing ») : séparation en trois parts. Les heuristiques évoluent sur un jeu d'entraînement d'instances générées, la meilleure est choisie sur un jeu de validation distinct, puis testée sur les jeux de la bibliothèque OR-Library (OR1 à OR4) et sur des jeux Weibull de 5 000, 10 000 et 100 000 objets (p. 6 ; suppl. p. 29). Les fonctions qui utilisent explicitement le nombre de boîtes sont exclues pour forcer la généralisation entre tailles (suppl. p. 7, note 2).
- Répétitions : « for some problems we run several experiments to get the best reported results » (p. 4). Ensemble de taille 512 en dimension 8 : 4 expériences sur 140 seulement (p. 9 ; suppl. p. 6). Ensembles admissibles : les 15 courses battent la meilleure borne connue ; I(12, 7) complet dans 3 courses sur 5 (suppl. p. 6 et 7), cohérent avec les 60 % de la page 9. Empaquetage : 10 courses, toutes meilleures que les deux heuristiques de référence ; 0,44 % ± 0,11 % de boîtes en excès sur Weibull 10 000 contre 4,20 % et 3,90 % (suppl. p. 7).
- Ablations : 5 graines par variante, avec barres d'erreur type ; la version complète trouve I(15, 10) dans 2 courses sur 5, la variante sans fusion de deux programmes dans 1 sur 5, les autres jamais (suppl. p. 4).
- Pas de correction de comparaisons multiples ; le « meilleur de n courses » est légitime pour un objet mathématique vérifiable, pas pour une statistique bruitée.

## Échecs et limites rapportés par les auteurs
- Fonctionne au mieux avec un évaluateur efficace, un score « riche » plutôt que binaire, et une partie isolable à faire évoluer ; la démonstration de théorèmes sort de ce cadre (p. 7).
- Le modèle de langue « does not use much context about the problem » : il sert de source de programmes variés (p. 6).
- Un squelette fixe peut restreindre l'espace des programmes trouvables (p. 2).
- Dimension 8 de l'ensemble « cap set » : moins d'une expérience sur 30 réussit (suppl. p. 7).
- Coût estimé d'une expérience sur ensembles admissibles : 800 à 1 400 dollars et 250 à 500 kilowattheures (suppl. p. 8).

## Vérifié par des tiers
- Non trouvé dans les lectures de cette passe. Les constructions sont vérifiables mécaniquement (programmes en annexe C), ce qui n'est pas une vérification rapportée par un tiers. Jordan S. Ellenberg, mathématicien, est coauteur, donc pas un tiers.
- Le papier attribue à sa « référence 3 » (Lehman et al., chapitre du « Handbook of Evolutionary Machine Learning », Springer, 2023, p. 331–366, d'après sa liste de références p. 7) la première démonstration d'une boucle d'auto-amélioration couplant modèle de langue et score programmatique (p. 9) : attribution rapportée, non vérifiée.

## À emprunter
- Boucle extérieure : la séparation entraînement (score pendant l'évolution), validation (choix du gagnant), test (rapport, une fois) ; une part de sélection distincte de la part finale manque peut-être entre `test` et `test_final` (p. 6 ; suppl. p. 29).
- Boucle intérieure : îles avec élimination et réensemencement périodiques, et regroupement par signature (le vecteur des résultats par tâche), qui permet des comparaisons appariées tâche par tâche (p. 9).
- Mesure du bruit : rapporter la distribution des courses (k réussites sur n, moyenne et écart) et non le meilleur de n dès que la cible est une statistique et non un objet vérifiable (p. 4 et 9 ; suppl. p. 6 et 7).

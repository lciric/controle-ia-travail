# Mandat « corpus et grille » des billets — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 18:05Z, sur le mot de Lazar « go reformulation » (R-3345, R-3349, GO-2026-11-18-43). Langue : français, sans sigle seul.

## Qui tu es
Un agent neuf. Tu ne lis **aucun résultat du programme** (rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, aucun registre) : ton travail porte sur des billets publics, pas sur nos résultats.

## Objet
Préparer l'écriture de nos billets (en anglais, pour LessWrong et l'Alignment Forum) à partir des **données brutes** des billets de résultats comparables, et non de palmarès ni de souvenirs. Livrables sous `docs/notes/billets-v1/`, scellés.

## Tâches
1. **Politique du site sur les textes écrits avec une IA** : retrouve la page à la source (lesswrong.com), enregistre-la sous `docs/sources/lesswrong-politique-ia-v1/` avec empreinte et date ; résume en dix lignes au plus ce qu'elle exige, chaque point avec sa citation courte. Si tu ne la trouves pas, dis-le : n'invente rien.
2. **Corpus** par l'interface de données du site (`https://www.lesswrong.com/graphql`, requêtes POST, une par seconde au plus, agent utilisateur générique, aucune information personnelle) : billets depuis le 2022-01-01 portant des étiquettes proches des nôtres (contrôle de l'IA, interprétabilité, tromperie, sondes ; trouve les identifiants d'étiquettes par requête et liste-les). **Règle écrite avant de classer** : est « billet de résultats empiriques » un billet qui rapporte une expérience des auteurs avec au moins un chiffre ou une figure de résultat. Par année : les 15 billets de résultats les mieux notés ; pour chacun, un billet **apparié peu noté** (mêmes étiquettes, même année, tiers bas des votes, longueur comparable) ; et les dix commentaires les mieux notés de chaque billet bien noté. Texte brut **hors du dépôt**, sous `/home/user/billets-corpus-v1/` ; dans le dépôt, seulement le manifeste `manifeste-corpus-v1.json` (identifiant, adresse, titre, auteur, date, votes, nombre de votants, nombre de commentaires, étiquettes, classe, apparié à, empreinte, taille, date du tirage, requêtes employées).
3. **Partage** par programme (graine par `numpy.random.SeedSequence`, consignée) : moitié « développement », moitié « tenue à l'écart », stratifié par année et par classe ; inscrit au manifeste. **Tu n'ouvres pas le texte de la moitié tenue à l'écart.**
4. **Grille des gestes de rédaction**, tirée de la seule moitié « développement » : `grille-gestes-v1-brouillon1.md`, 15 à 25 items, chacun avec définition, valeurs possibles, règle de décision, deux exemples (identifiant du billet, citation de 25 mots au plus) : place et forme de la thèse, résumé en tête, statut épistémique, figures et tableaux, bases de comparaison, justification des choix (« nous avons choisi X parce que Y ; alternatives »), limites, résultats négatifs, questions ouvertes, liens vers code et données, titre, longueur. Plus une **typologie des objections** des commentaires (8 à 12 classes, mêmes exigences).
5. **Rapport** `rapport-corpus-et-grille-v1.md` : décomptes, exclusions, limites (auteur, date, taille du site), et ce qui reste : gel de la grille, deux codeurs indépendants sur la moitié tenue à l'écart, accord mesuré, gabarit.

## Règles
Sorties scellées (`PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>`) ; ni commit, ni poussée, rien dans `registres/` ; disque compté (pas plus de 300 Mo) ; arrêt au premier refus, sans contournement. Dernier message : chemins et empreintes, décomptes, points à trancher, lectures hors mandat.

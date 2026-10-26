# « How Many Random Seeds? » (Colas, Sigaud, Oudeyer) — fiche de lecture (passe v2)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Cédric Colas, Olivier Sigaud, Pierre-Yves Oudeyer. « How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments ». Prépublication arXiv 1806.08295, version 2 du 5 juillet 2018 (version 1 du 21 juin 2018) — page de résumé arXiv enregistrée le 26 octobre 2026 à 03:45 UTC.
- Lieu de publication : non indiqué sur le PDF ni sur la page arXiv ; à vérifier. Les auteurs le présentent comme un « tutorial paper » (p. 1).

## Fichier lu
- `pdfs/how-many-seeds/arxiv-1806.08295v2.pdf`, 3 305 262 octets, 20 pages ; SHA-256 `83408576427473fdb059184e689c027ac9b34815f2d96d4c977270ad514ec78f` (même empreinte que la v1).
- Pages lues : 1 à 20 (tout).

## Comment la boucle est faite
- Pas de système : la comparaison de deux algorithmes d'apprentissage par renforcement sur un environnement (« Half-Cheetah ») ; démarche en trois temps : étude pilote, analyse de puissance pour choisir le nombre de graines N, puis tests (p. 11 à 14).

## Traitement du bruit et du sur-ajustement
- Tests présentés : test t de Welch (variances inégales) et test par intervalle de confiance bootstrap (p. 6 à 10). Correction de Bonferroni (α divisé par le nombre d'expériences) quand on en conduit plusieurs, car les faux positifs croissent linéairement avec leur nombre (p. 5).
- Exemple 1 : deux échantillons de 5 graines du même algorithme, même implémentation, donnent une différence « significative » (valeur p de 0,031) : une erreur de première espèce (p. 10).
- Exemple 2 : avec N = 5, la probabilité de manquer l'effet observé est de 51 % ; il faut N = 10 pour la ramener à 19 % (p. 13).
- Estimation empirique du taux de faux positifs : lancer 2N courses du même algorithme, les couper en deux faux « algorithmes », tester, répéter (p. 15) ; pour N petit, le taux réel dépasse nettement le taux nominal ; le bootstrap tourne autour de 10 % au lieu de 5 % (p. 16).
- Avec une étude pilote de 5 courses, l'écart type est sous-estimé ; dans leur exemple on choisirait N = 7 au lieu de N = 17 (p. 17).
- Recommandations finales (p. 19) : préférer Welch au bootstrap ; prendre α sous 0,05 ; corriger les comparaisons multiples ; au moins 20 courses dans l'étude pilote ; prendre N plus grand que ce que prescrit l'analyse de puissance.

## Échecs et limites rapportés par les auteurs
- Les tests reposent sur des hypothèses (normalité, indépendance) « not always reasonable » ; leurs données semblent bimodales (p. 16 et 18).
- Incohérence interne à signaler : le seuil sous lequel il ne faut pas utiliser le bootstrap est « < 10 » à la page 16 mais « less than 20 samples » aux pages 18 et 19.
- Un seul environnement et deux variantes d'un même algorithme dans les exemples (p. 4 et 11).

## Vérifié par des tiers
- Non trouvé. Le phénomène de départ (deux moitiés de 5 graines d'un même algorithme qui semblent venir de lois différentes) est attribué à Henderson et al. (p. 2), non lu.

## À emprunter
- Boucle extérieure : avant de faire confiance au script de lecture, mesurer son taux réel de faux positifs sur des comparaisons « A contre A » (même conception, graines différentes) (p. 15).
- Boucle intérieure : une primitive qui compare deux variantes avec moins de 10 courses chacune verra des faux positifs au-delà du taux annoncé (p. 16).
- Mesure du bruit : une étude pilote d'au moins 20 courses pour estimer la variance entre graines, que le brief dit inconnue, avant de fixer le nombre de courses par objet (p. 19).

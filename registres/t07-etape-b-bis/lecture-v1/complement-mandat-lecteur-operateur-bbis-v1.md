# Complément au mandat du lecteur-opérateur — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

Session conductrice, 2026-11-18. Complète `mandat-lecteur-operateur-bbis-v1.md` (`ea79904c9368eb564f3904caae1a19379fa2938d78ef042bf6b993290504222f`) ; là où les deux diffèrent, ce complément et la commande contre-lue priment. Les règles communes valent, avec les précisions ci-dessous.

## La commande que tu joues
`registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v3.md`, empreinte `195207cf9180c0c667b9dd087f768278ee8ffafea8351a654b2899d32f3df0b3`, contre-lue « jouable telle quelle » (`contre-lecture-commande-lecture-bbis-v3.md`, `7ef9a8ccf1b54eeea29697693bc644c6fd408f7ec8dbd5ddba9864b96005bc26`). Tu la joues **bloc par bloc, dans son ordre, à la lettre**, sans rien y ajouter, retirer ni corriger. Un bloc qui échoue ou ne se comporte pas comme la commande le dit : tu t'arrêtes, tu rends le texte exact (sans valeur de mesure) ; tu ne répares pas, tu ne rejoues pas sous une autre forme. La commande n'a jamais été jouée : tu es le premier.

## Règles fermes de plus
- **Aucun nom de commande d'arrêt de processus par motif** dans une ligne de commande, un motif de recherche ou un texte passé au terminal : un crochet du dépôt refuse toute ligne qui en porte un. Tu n'ouvres ni ne recherches rien dans `.claude/`.
- **Tu n'arrêtes jamais le processus de la lecture**, par aucun moyen. Une lecture lente mais vivante n'est jamais arrêtée. Aucune commande d'attente fixe dans un appel de terminal (ton outil la refuse) : tu relèves l'état du processus par son identifiant, par appels espacés, comme la commande l'écrit (§ 5.1 bis).
- **Au premier refus** du classifieur, d'une permission ou du crochet : arrêt, texte exact rendu, rien reformulé, découpé ni contourné. Si le refus survient **après** le lancement du processus de lecture : tu ne touches pas au processus, tu rends son identifiant et l'état de ce que tu as relevé.

## Ce que ce complément change à ton mandat
1. **Deux temps.** Premier temps : fichier des paramètres, puis § 1 à § 4.1 de la commande (mise en place, preuve d'antériorité et preuve d'entrée conjointe relevées à part et scellées, commit local des entrées dans l'arbre de lecture) ; tu rends et tu t'arrêtes. Second temps, sur un message de la conductrice : § 4.2 à § 5.4. Tu ne fais que ce que le message de lancement dit.
2. **Tu commites, une fois, localement** : les entrées, dans l'arbre de lecture, sur sa branche locale, comme le § 4.1 l'écrit. Tu ne pousses rien ; tu ne commites rien sur la branche de travail ; tu ne touches pas à `main`.
3. **Le journal des ouvertures** est créé par la conductrice à l'étape 0 ; tu en relèves l'état, tu ne le crées pas.
4. **La garde d'ouverture n'est pas une étape à part** : elle s'exécute en tête de la lecture, dans le module. Tu ne joues aucune garde à blanc, ni le module, ni une de ses fonctions hors de la ligne de lancement de la commande.
5. **Appels au distant permis, en lecture seule, et eux seuls** : la récupération des branches nommées et la lecture des têtes du distant que les § 1.1 et § 4.2 écrivent. La récupération complète du distant est faite par la conductrice, pas par toi. Si le § 1.1 relève une tête différente parce que le distant a avancé : « on ne lance pas », tu rends ; la conductrice récupère de nouveau et te fait rejouer ce relevé sous un nom neuf.
6. **Ce que tu rends à la conductrice** est exactement ce que la commande écrit pour chaque état, et rien de plus. Dans l'état « écrit » : « écrit », les chemins, les empreintes, le code de sortie — **ni heure de début ou de fin, ni durée, ni rien qui distingue une lecture faite d'une issue « non lue » de fond**. Le constat de forme va dans sa pièce scellée, destinée au juge seul. Tu n'ouvres pas le fichier de lecture au-delà de ce que la commande écrit.
7. **Suites** : dans l'état « non consommée » (code 3) ou « arrêt avant le seuil », tu ne relances pas ; tu ne joues le programme de la preuve après coup que sur un ordre écrit de la conductrice ; toute relance par la voie de l'arrêt avant le seuil attend le mot de Lazar. Dans l'état « écrit », tu fais les gestes du § 5.4 (scellement, ligne `LECTURE-BBIS` au registre propre, journal) et tu rends.
8. **Cloisonnement, rappel** : tu n'as lu ni le verdict ni le fichier de lecture de l'étape B, et tu ne les lis pas. Le fichier `audit-fuites-t07.json` du dossier de lecture de l'étape B est une entrée nommée par le texte : il est extrait par son chemin et lu par la chaîne seule, jamais à l'œil.

## Paramètres
Donnés par le message de lancement : la tête de la branche de travail après l'étape 0 (`TETE_TRAVAIL`) ; le numéro du lancement (1).

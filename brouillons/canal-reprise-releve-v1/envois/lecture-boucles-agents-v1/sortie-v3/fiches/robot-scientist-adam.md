# Le robot scientifique Adam — « The Automation of Science » — fiche de lecture (passe v2)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Ross D. King, Jem Rowland, Stephen G. Oliver, Michael Young, Wayne Aubrey, Emma Byrne, Maria Liakata, Magdalena Markham, Pinar Pir, Larisa N. Soldatova, Andrew Sparkes, Kenneth E. Whelan, Amanda Clare. « The Automation of Science » (p. 1). Le prénom de Pinar Pir a perdu un caractère à l'extraction du texte ; il est écrit ici comme sur la notice d'Aberystwyth.
- Version lue : prépublication des auteurs (« preprint pdf » sur la page des publications du projet Robot Scientist, Université d'Aberystwyth). Métadonnées du PDF : création le 3 avril 2009, titre interne « A Robot Scientist for Yeast Systems Biology ».
- Version publiée : Science 324(5923):85–89, 3 avril 2009, identifiant d'objet numérique 10.1126/science.1165620 — d'après la notice du portail de recherche de l'Université d'Aberystwyth, lue par un outil de résumé de page : à vérifier sur la version de l'éditeur, dont le texte peut différer et n'est pas lu.

## Fichier lu
- `pdfs/robot-scientist-adam/aber-science18-preprint.pdf`, 554 919 octets, 12 pages ; SHA-256 `a19a4d9210da834bad2c54957eedd97a786b7ca041092713d57169297c957abc` (même empreinte que la v1).
- Pages lues : 1 à 12 (tout). Le matériel en ligne complémentaire, auquel le texte renvoie souvent, n'est pas téléchargé : non lu.

## Comment la boucle est faite
- Principe : un robot scientifique « automatically originates hypotheses », conçoit les expériences qui les testent, les exécute par robotique de laboratoire, interprète les résultats et recommence le cycle (p. 2).
- Adam (p. 2 et 3) : un modèle logique du métabolisme de la levure en Prolog et une base bioinformatique ; un logiciel abduit des hypothèses sur les gènes qui codent des « enzymes orphelines » ; un autre déduit les expériences (souches délétées et métabolites ajoutés au milieu) ; un autre les planifie ; l'automate les exécute et enregistre données et métadonnées ; un logiciel analyse les courbes de croissance ; des méthodes statistiques relient résultats et hypothèses. Une fois l'infrastructure en place, « no human intellectual intervention » n'est nécessaire pour des cycles simples (p. 3).
- Capacité : plus d'un millier d'expériences souche/milieu lancées par jour, chacune jusqu'à 5 jours (p. 7).
- Mémoire : une formalisation logique de toute l'investigation (plus de 10 000 unités de recherche, arbre de dix niveaux, 6 657 024 mesures de densité optique issues de 26 495 courbes de croissance) (p. 4).

## Traitement du bruit et du sur-ajustement
- 20 hypothèses sur 13 enzymes orphelines ; 12 hypothèses nouvelles confirmées avec P < 0,05 (p. 3).
- La probabilité rapportée est une estimation de Monte-Carlo : la chance d'obtenir la discrimination observée en réétiquetant au hasard les réplicats, autrement dit un test de permutation (légende du tableau 1, p. 7). Les réplicats font partie de la structure emboîtée (études, cycles, essais, tests, réplicats) (p. 7).
- Aucune correction de comparaisons multiples n'est mentionnée dans le texte principal ; le matériel complémentaire n'est pas lu (à vérifier).
- Contrôle hors boucle : pour les trois gènes qu'Adam proposait pour une même enzyme (2-aminoadipate:2-oxoglutarate aminotransférase), les protéines ont été purifiées et testées in vitro, ce qui confirme ses conclusions (p. 3) ; la littérature montre que 6 des 20 gènes avaient déjà une fonction établie, faute d'une base complète : ils servent de « positive control » (p. 3) ; « A possible error was also revealed » (p. 3).

## Échecs et limites rapportés par les auteurs
- Le savoir produit est « of a modest kind » ; les auteurs discutent l'objection de Lady Lovelace (p. 4).
- Matériel et logiciel « brittle » : quelques jours sans intervention, technicien conseillé à proximité ; intégration logicielle à améliorer (p. 5).
- Les preuves d'Adam sont indirectes (courbes de croissance), d'où la confirmation manuelle (p. 3) ; « the limits of automation » restent à déterminer (p. 5).

## Vérifié par des tiers
- Non trouvé. Les confirmations rapportées (essais in vitro) sont faites par les auteurs eux-mêmes ; la concordance avec la littérature porte sur 6 gènes déjà connus (p. 3).

## À emprunter
- Boucle extérieure : confirmer les conclusions de la boucle par une méthode plus directe et indépendante de celle qui les a produites (ici l'essai in vitro), menée hors de la boucle (p. 3).
- Boucle intérieure : test de permutation sur réplicats comme mesure de signification de la primitive, et journal formel de chaque expérience (p. 4 et 7).
- Mesure du bruit : glisser des témoins positifs connus parmi les hypothèses testées pour estimer le taux de faux négatifs de la boucle (p. 3).

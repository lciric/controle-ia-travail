# « A Meta-Analysis of Overfitting in Machine Learning » (Roelofs et al., 2019) — fiche de lecture (passe v2, ajouté)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Auteurs dans l'ordre de la page 1 du PDF : Rebecca Roelofs, Sara Fridovich-Keil (contribution égale), John Miller, Vaishaal Shankar, Moritz Hardt, Benjamin Recht, Ludwig Schmidt (Université de Californie à Berkeley). La page des actes consultée par un outil de résumé donne un autre ordre (Roelofs, Shankar, Recht, Fridovich-Keil, Hardt, Miller, Schmidt) : écart à vérifier ; l'ordre ci-dessus est celui lu sur le PDF.
- « A Meta-Analysis of Overfitting in Machine Learning ». 33e conférence Neural Information Processing Systems (2019), Vancouver (pied de page, p. 2) ; actes « Advances in Neural Information Processing Systems 32 » selon la page des actes.
- Marqué « ajouté » par la v1 (hors liste du brief).

## Fichier lu
- `pdfs/ajout-roelofs-meta-analyse-surajustement/neurips2019-ee39e503-Paper.pdf`, 666 927 octets, 11 pages ; SHA-256 `29989c9b39e41dafd369530da2882bfacfdfa0d851ff782720a04c54d2020dcf` (même empreinte que la v1). Source : actes de la conférence (`papers.nips.cc`).
- Pages lues : 1 à 9 (tout le texte) ; les annexes citées ne sont pas dans ce fichier.

## Comment la boucle est faite
- Pas de système : la boucle des concurrents Kaggle, qui soumettent à répétition, voient le score de la part publique du jeu de test, et sont classés à la fin sur la part privée jamais rendue (p. 3).
- Corpus : 120 concours de classification ayant au moins 1 000 soumissions avant la date limite, pour les mesures d'évaluation présentes dans au moins 10 concours (p. 2 et 3).
- L'écart entre score privé et score public sert d'estimation du « sur-ajustement adaptatif », c'est-à-dire dû à la réutilisation du jeu de test (p. 3).

## Traitement du bruit et du sur-ajustement
- Trois niveaux d'analyse (p. 3 à 6) : nuage public contre privé de toutes les soumissions, avec intervalles exacts de Clopper-Pearson à 95 % (p. 4) ; même nuage pour les 10 % meilleures soumissions (p. 5) ; distribution des valeurs p sous un modèle nul de découpage public/privé aléatoire (p. 6).
- Vue agrégée sur 34 concours notés en exactitude : écarts entre −2 % et +2 % à peu près symétriques, plus une queue de cinq concours (p. 7).
- Constats : « little to no signs » de sur-ajustement adaptatif (p. 2) ; effets typiquement inférieurs à 1 % d'exactitude (p. 2) ; les exceptions ont des découpages non indépendants ou de très petits jeux de test — part publique de 90 exemples (p. 5), parts privées de 209 et 100 exemples (p. 7), un jeu d'environ 4 000 exemples issu de 7 sujets humains (p. 5) ; jusqu'à 35 000 soumissions sans grand effet (p. 8).
- Seuil indicatif proposé : au moins 10 000 exemples de test comme minimum raisonnable contre le sur-ajustement adaptatif, sous réserve d'une étude plus large (p. 7).

## Échecs et limites rapportés par les auteurs
- Le modèle nul est « highly idealized » (chaque soumission aurait son propre découpage indépendant) ; des modèles corrélés expliquent probablement des sauts dans les distributions de valeurs p (p. 6).
- Sur de grands jeux de test, des écarts minimes deviennent significatifs sans être importants (p. 6).
- Pour les autres mesures (aire sous la courbe, etc.), pas de scores par exemple : analyse seulement qualitative (p. 8).
- Hypothèse non vérifiée : pas de sur-ajustement non supervisé à la part privée (note, p. 3) ; « we cannot rule out every form of overfitting » (p. 8) ; seulement la classification (p. 9).
- Les auteurs revendiquent la « first large meta-analysis » du sujet (p. 1) ; revendication rapportée, non vérifiée.

## Vérifié par des tiers
- Non trouvé.

## À emprunter
- Boucle extérieure : comparer à chaque génération le score sur `test` (rendu) et sur `test_final` (jamais rendu) ; c'est leur écart public/privé, à lire avec des intervalles exacts et le modèle nul de découpage aléatoire (p. 4 et 6).
- Boucle intérieure : leur résultat rassurant tient à de grands jeux de test ; avec 36 tâches, la part `test` est dans le régime « petit jeu de test » qu'ils traitent en exception (p. 5 et 7) — illustratif : 36 est environ 280 fois plus petit que leur seuil indicatif.
- Mesure du bruit : le test de l'écart rendu/non rendu par découpage aléatoire (p. 6) s'applique tel quel à `test` contre `test_final`.

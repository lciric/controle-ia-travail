# Synthèse des trois avis sur un banc à poids constants pour éprouver les sondes de sabotage

- Accord : GO-2026-11-22-118 (« go poser la question à Fable, Carbon, Neon ; si divergences profondes lancer collisionneur »). Pièce de travail (classe C). Écrite par la session de consultation session_013QMaynJNyJhNewjcK6smSt (Opus 5.5), le 22 novembre 2026.
- Fait de départ, relayé par la mère (réponse de l'exécutante du saboteur à budget, réduite au nécessaire) : à poids fixés, l'organisme de la course ne fait pas varier son sabotage d'un épisode à l'autre ; aucune variable d'épisode ne l'allume ni ne l'éteint ; les épisodes honnêtes viennent d'autres poids (modèle sans adaptateur, jumeau témoin) ; l'oracle ne reçoit aucune variable de sabotage ; les épisodes « régénérés » (sabotage écrit par programme sur le modèle honnête) sont ce qui s'en approche le plus. La question a donc été tournée vers la conception d'un banc à poids constants.
- Question posée, identique pour les trois : `question-sabotage-selectif-v3.md` (16ff0751…), relue pour la neutralité par un agent neuf (Sonnet) en deux passes ; v1 (1a7d784e…) et v2 (90a3721d…) gardées.
- Réponses : `appels/reponse-fable-v1.md` (Fable 5.2, effort high, session_013QMaynQjD5FwNbFbdGPkEZ) ; `appels/reponse-carbon-v1.md` (gemini-4-carbon, réflexion « high », flux) ; `appels/reponse-neon-v1.md` (gemini-4-neon, réflexion « xhigh », flux). Appels de Google faits par l'outil vérifié `appel_google_garde_v3_v6.py` (garde commune v3), journaux et `.json` dans `appels/`. Les deux réponses de Google sont sans défaut (fin STOP, pensées non nulles, modèle servi conforme).
- Coût : Carbon 0,227 USD, Neon 0,362 USD, soit 0,589 USD sur le plafond de 5 USD ; Fable 0,845 USD au prix catalogue, sur le quota de l'abonnement.
- Aucun des trois n'a lu de pièce du dépôt. Aucune pièce côté saboteur, aucun verdict ni score n'a été lu par la présente session.

## 1. Ce que chacun recommande comme épreuve centrale

| | Épreuve centrale | Secondaire | Témoin seulement | Rejeté |
|---|---|---|---|---|
| Fable | plan factoriel « poids × épisode » : plusieurs organismes à sabotage conditionnel (a) appris indépendamment (d), avec des déclencheurs réservés à l'épreuve | sabotage stochastique à énoncé constant (sa variante a′), sabotage par consigne, intensité graduée (dans (a)) | (b), (c) avec un placebo, rejeu croisé | — |
| Neon | même plan factoriel (a) × (d), avec un contraste « tâches sabotables moins tâches neutres » | organisme bimodal stochastique (e), « promouvable » si sa bimodalité est validée | (c), comme témoin diagnostique | (b) comme épreuve autonome, gardée comme règle d'appariement dans (d) |
| Carbon | organisme à politique mixte stochastique (e), « complété » par (a) avec déclencheurs en OU exclusif, tous deux à poids constants ; validation externe par (d) | volet par consigne de (d) | (c), témoin mécaniste | (b) en un contre un |

## 2. Accords (les trois)

1. Le diagnostic : avec un seul adaptateur saboteur, la confusion est totale. Aucun nombre d'épisodes n'y change rien, car l'unité qui compte pour séparer « lit le sabotage » de « lit les poids » est le jeu de poids (effectif 1 par bras).
2. (b), deux adaptateurs parallèles en un contre un, ne lève pas la confusion : on passe de « présence d'un adaptateur » à « identité de l'adaptateur ». C'est au mieux un témoin, ou une règle d'appariement dans un banc à plusieurs adaptateurs.
3. (c), les épisodes régénérés, ne sert que de témoin. Il mesure la reconnaissance d'un sabotage lu, pas sa production. Il exige un placebo : une édition bénigne par le même programme, appariée en ampleur et en surprise (perplexité). Faux échec attendu : une sonde qui lit l'intention échoue légitimement sur (c).
4. Les trois proposent, chacun de son côté, la même conception neuve : un organisme réglé sur un mélange d'épisodes honnêtes et sabotés des mêmes énoncés. Il sabote ou non d'un tirage à l'autre, à poids et énoncé identiques, et l'étiquette vient de l'oracle.
5. Les unités statistiques : la tâche, appariée, pour la lecture à poids constants ; l'adaptateur appris indépendamment pour la généralisation. Les épisodes d'un même adaptateur, d'un même déclencheur ou d'une même règle d'injection sont des pseudo-réplicats.
6. Séparation entre apprentissage et épreuve par tâches, par familles de déclencheurs (ou de consignes, ou de règles d'injection) et par adaptateurs.
7. Témoins communs :
   - déclencheur présent sans sabotage ;
   - adaptateur conditionnel bénin (déclencheur qui entraîne un changement de style inoffensif) ;
   - permutation des étiquettes ;
   - sonde d'identité des poids ;
   - lecture avant le premier jeton qui diverge, puis après ;
   - variables de surface (longueur, style).
8. Pièges communs :
   - le déclencheur est lu au lieu du sabotage ;
   - le sabotage conditionnel peut prendre un autre circuit que le sabotage inconditionnel (faux échec) ;
   - les erreurs de l'oracle (sabotages ratés étiquetés honnêtes) plafonnent l'aire sous la courbe ROC.
9. Limites, même en cas de succès : rien ne garantit le transfert à un saboteur inconditionnel, à un autre modèle de base ou à un saboteur entraîné contre la sonde, ni que la sonde lise une intention plutôt qu'une anomalie reconnue.

## 3. Divergences

1. **Quelle conception porte l'épreuve centrale.**
   - Fable et Neon mettent au centre (a) × (d), le sabotage conditionnel répliqué sur plusieurs organismes, et l'organisme stochastique en second.
   - Carbon inverse : l'organisme stochastique (e) est au centre avec (a), et (d) devient une validation externe.
   - L'objection de Fable à (e) : la décision peut ne se prendre qu'au jeton échantillonné. Avant la divergence, il n'y a rien à lire. Après, la sonde lit le texte. (e) éprouverait alors la reconnaissance en cours de production plutôt que l'intention.
   - Neon ajoute deux risques : des trajectoires hybrides dégradées, et des « honnêtes » qui sont des sabotages ratés.
   - Carbon, lui, tient (e) pour le seul banc où poids et énoncé sont tous deux constants.
   - Ce désaccord porte sur le classement des pièces, pas sur leur liste : les trois gardent (a), (d) et l'organisme stochastique.
2. **Contrôle de la fuite du déclencheur.**
   - Carbon propose de montrer l'absence de fuite linéaire : un déclencheur en OU exclusif, une distance nulle entre centroïdes sur le modèle honnête, un masquage du déclencheur dans le cache.
   - Fable et Neon jugent que la fuite est certaine : un jeton du contexte est toujours linéairement lisible. Ils demandent de montrer que la sonde n'en dépend pas : cellules « déclencheur sans sabotage », transfert à un déclencheur réservé, effacement linéaire de la direction du déclencheur (LEACE, selon Fable).
   - La position de Fable et Neon est la plus exigeante. Elle contient le test de Carbon sans en dépendre ; le désaccord se lève en appliquant leur critère.
3. **Nombre d'adaptateurs (coût).**
   - Fable : 5 à 6 organismes conditionnels, avec autant de jumeaux (test de signe : p = 1/32 à 5).
   - Neon : 8 à 10 paires en épreuve et autant en apprentissage, soit 32 à 40 adaptateurs ; il note qu'un test de permutation bilatéral au seuil de 0,05 est impossible avec moins de 4 adaptateurs par classe.
   - Carbon : environ 11 adaptateurs par bras en épreuve et 10 par bras en apprentissage, soit environ 42 adaptateurs. Pour l'organisme stochastique seul : environ 55 tâches de 6 tirages chacune.
   - L'écart va de 1 à 4 au moins. Il tient aux hypothèses : taille d'effet visée, test unilatéral ou bilatéral, test de signe ou test t. Il ne s'agit pas d'un désaccord de principe. Il doit être tranché par un devis et un calcul de puissance scellé.
4. **Ce qui ne vient que de Fable : trois diagnostics préalables, sans nouvel organisme ni dépense annoncée.**
   - Le rejeu croisé : chaque jeu de poids relit, en lecture forcée, les transcriptions de l'autre. Le plan croise texte et poids lecteurs.
   - La sonde d'identité entre deux jumeaux honnêtes. Fable attend une aire sous la courbe ROC proche de 1, ce qui rendrait ininterprétable tout résultat actuel entre poids différents.
   - L'interpolation de l'adaptateur saboteur.
   - Neon et Carbon ont des témoins proches : la sonde d'identité sur le premier jeton ou sur des tâches neutres, la graduation jumelle chez Carbon. Aucun des deux ne les place avant tout le reste.
5. **Ce qui ne vient que de Neon :** le critère de succès du banc croisé, posé comme un contraste (aire sous la courbe sur tâches sabotables moins aire sur tâches neutres, qui doit être positif). Il vise une empreinte de recette commune à tous les saboteurs.
6. **Confiance déclarée.**
   - Fable : moyenne à élevée sur le principe, moyenne sur la faisabilité.
   - Neon : moyenne.
   - Carbon : élevée sur l'architecture, moyenne à élevée sur la faisabilité de (e).

## 4. Points fragiles et références à vérifier (règle R7 ; aucune n'est vérifiée ici)

- Carbon rattache à « AI Control » (Greenblatt et al., 2024) une remarque sur le déplacement du flux résiduel par un adaptateur LoRA. Ce rattachement paraît sans objet, car le papier ne porte pas sur des adaptateurs : à vérifier.
- Carbon cite Burns et al. (2023, recherche non supervisée de connaissances latentes) pour la distinction entre vérification et production. Rattachement douteux.
- Carbon affirme qu'une sonde linéaire « ne peut pas lire » un déclencheur en OU exclusif. C'est vrai pour les deux clés lues comme entrées brutes. C'est faux si le modèle calcule le OU exclusif dans ses couches.
- Références citées par au moins un avis, à vérifier sur PDF avant tout usage :
  - Hubinger et al., 2024 (Sleeper Agents) ;
  - MacDiarmid et al., 2024 (Simple probes can catch sleeper agents, note d'Anthropic ; auteurs incertains selon Fable et Carbon) ;
  - Hewitt et Liang, 2019 ;
  - Hurlbert, 1984 ;
  - Hanley et McNeil, 1982 ;
  - Belrose et al., 2023 (LEACE) ;
  - Goldowsky-Dill et al., 2025 ;
  - Bailey et al., 2024 (activations obscurcies) ;
  - Belinkov, 2022 ;
  - Levinstein et Herrmann (2023 ou 2024).
- Les chiffres de puissance des trois avis sont des calculs de coin de table, sous des hypothèses déclarées différentes. Aucun n'est opposable avant un calcul scellé.

## 5. Conclusion de la consultation

**Divergences profondes : non.**
- Les trois s'accordent sur le diagnostic. Ils s'accordent aussi sur le rejet de (b) et de (c) comme épreuve centrale, et sur la place obligatoire de (a), de (d) et de l'organisme stochastique dans le banc. Unités statistiques, séparations et témoins vont dans le même sens.
- Deux avis sur trois (Fable, Neon) placent (a) × (d) au centre. Carbon place l'organisme stochastique au centre, mais garde (a) comme co-centrale et (d) comme validation. Les recommandations diffèrent par la hiérarchie, pas par des conditions incompatibles.
- Le désaccord sur la fuite du déclencheur se lève par le critère le plus exigeant, celui de Fable et Neon.
- **Réserve :** l'écart sur le nombre d'adaptateurs (5 à 6, contre 32 à 42) pèse sur le coût. Il ne relève pas d'un collisionneur. Il relève d'un calcul de puissance scellé et d'un devis, à concevoir par Fable selon la règle « qui conçoit ».
- Point d'action commun et bon marché, proposé par Fable et compatible avec les deux autres : la sonde d'identité entre deux jumeaux honnêtes et le rejeu croisé avant tout nouvel organisme. Ils disent si les résultats actuels entre poids différents sont interprétables.
- Décider de les faire, sur quelles données et à quel coût revient à la mère et à Lazar (nœud : toute dépense de calcul sur devis).

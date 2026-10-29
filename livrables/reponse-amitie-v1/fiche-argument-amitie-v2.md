# Fiche d'argument — « Justified assurance of friendliness » — v2

Plan fusionné : la structure de l'autre instance (v1, sections 1 à 8), plus les ajouts et corrections de la session. Aucune conclusion : les blocs **À toi** sont vides exprès.

Étiquettes :
- **[résultat]** : établi dans le dépôt (simulation ou calcul) ; chemin et empreinte en fin de fiche ;
- **[PDF]** : lu sur PDF empreinté (R7) ;
- **[hypothèse]** : hypothèse du programme, pas encore testée ;
- **[P3 ?]** : vient de P3, absent du dépôt, à vérifier dans tes sources ;
- **[mémoire ?]** : référence citée de mémoire, à vérifier sur PDF ou à retirer.

## 1. Thèse (~70 mots)

- **À toi** : oui, non, ou oui sous conditions ; si « oui, mais », la condition principale en une phrase.
- Matière, à prendre ou à laisser : un critère de tri. Une preuve ne vaut que si un X trompeur ne pourrait pas la produire aussi.

## 2. Les termes (~130 mots)

- **« Friendly »** : trois lectures, et chacune engage la suite.
  - Comportement observable : la question devient une prédiction sous changement de distribution.
  - Disposition, c'est-à-dire la conduite contrefactuelle, y compris là où personne ne regarde : c'est elle qui donne un sens à « indéfiniment ».
  - Objectif, ton bien-être faisant partie de ses buts : le plus dur à prouver, le seul qui résiste au basculement du rapport de force.
  - **À toi** : laquelle tu retiens.
- **« Evidence » comme test.** α est la probabilité d'alarme sur un X amical (fausses alarmes), π la probabilité d'alarme sur un X trompeur (puissance).
  - Contre un X stratégique, π se prend au pire cas sur ses réponses : c'est lui qui choisit l'alternative.
  - Une non-alarme a un rapport de vraisemblance en faveur de « amical » de (1 − α)/(1 − π). Si π ≈ α, il vaut 1 : la non-alarme ne prouve rien (calcul direct).
  - Sous garantie toujours valide, la puissance n'est plus le bon critère. Le critère est la croissance au pire cas, dite « GROW » (Pérez-Ortiz et coll., arXiv 2208.07610, p. 2) **[PDF]**.
- **Les deux contraintes** : « indéfiniment » (section 5), puis « sans comprendre ses stratégies » (section 6).

## 3. La preuve comportementale (~150 mots)

- **Théorème négatif** **[résultat]** :
  - **Classe C** (l'attaquant réarrange les scores honnêtes et préserve leur multi-ensemble) :
    - toute statistique invariante par son groupe de permutations a une puissance égale à son taux de fausses alarmes (T1) ;
    - sous rebrassage uniforme, plus aucune statistique ne détecte, quelle qu'elle soit (T2) ;
    - en simulation (T0.3), les statistiques symétriques restent identiques au bit près.
  - **Classe K** (marginales préservées, dépendance changée) : elle n'est pas aveugle. Sous dépendance positive, la somme passe au-dessus de α.
  - **Antériorité** : la moitié « aveugle » est occupée (arXiv 2607.11751) et n'est pas revendiquée. Ce qui l'est : la forme par invariance (temps × agents), la distinction entre C et K, les garanties locales.
- **L'observateur déplaçable** :
  - **[P3 ?]** ta loi de sycophancie : le jugement se déplace d'une fraction prévisible ;
  - **[hypothèse]** HC1, retenue sous la forme Δv = g · (ĉ − v₀), avec une destination ĉ estimée librement. « Vers la cible de la pression » se teste contre le nul de retour à la moyenne du corpus, comme dans P3. Ne l'écris pas comme acquis.
- **Fragmentation** **[résultat]** : le maximum par action s'effondre (de 1,00 à 0,071), la somme non (0,41 quelle que soit la répartition).
- **Les issues du défenseur** **[résultat]** :
  - un déplacement net ;
  - un changement de forme ;
  - un dommage structuré que l'attaquant ne peut pas brouiller. Après appariement adaptatif, l'autocorrélation tombe de 0,46 à 0,05, mais la moyenne glissante reste à 1,00 et Page à 0,997 ;
  - une loi honnête non invariante sous ses réarrangements. Le groupe compte : 0,967 pour un rebrassage total, contre 0,0505 pour un rebrassage à l'intérieur de chaque agent ;
  - de l'information prise hors des scores (section 4).
- **Preuves corrélées** :
  - **[résultat]** sous effet d'épisode, 0,21 à 0,35 de fausses alarmes au lieu d'au plus 0,05 ; avec une corrélation de 0,4 entre agents, 0,17 ;
  - **[hypothèse]** H5 : la sécurité ne croît avec le nombre de moniteurs que par leur diversité. Des vérificateurs copies d'un même modèle partagent leurs pannes.
- **À toi** : ce que ces résultats impliquent pour une preuve qui ne porte que sur le comportement de X.

## 4. La preuve interne : l'issue « information hors des scores » (~140 mots)

- **[P3 ?]** La direction qui suit le comportement porte moins de 1 % de l'effet causal, contre 68 % pour l'état complet : lire n'est pas causer.
- **[P3 ?]** Les méthodes de rang 1 ne déplaçaient rien ; l'ablation de rang 3 déplaçait les verdicts même sans pression. Un contrôle sans manipulation change la lecture d'un effet.
- **[PDF]** Qui tient la plume (arXiv 2609.36490) :
  - un réglage fin des poids de rang 1 est entraîné contre des sondes gelées (ce n'est pas le « rang 1 » de P3, qui désigne une intervention) ;
  - il ramène à 4 % les vrais positifs de sondes jamais vues, à 1 % de faux positifs, soit 96 % d'évasion (llama-3.1-8b) ;
  - par la consigne seule, la modification va dans le bon sens mais reste trop faible pour évader.
- **[hypothèse]** HC4, retenue : déplacer une sonde qui lit l'agent exige un accès en écriture aux activations ou aux poids.
- **[mémoire ?]** Au pire cas, sous hypothèses cryptographiques, une porte dérobée plantée peut rester indétectable même avec un accès complet (Goldwasser et coll., 2022).
- **[hypothèse]** H8 : ce que mesure vraiment une sonde (intention, ou conscience d'être évalué) prédit sa robustesse.
- **À toi** : quel type de preuve interne compterait (corrélationnelle, interventionnelle, autre), sous quelles conditions vérifiables, et ce qui la rend fragile.

## 5. « Indéfiniment » (~170 mots)

- **Garantie toujours valide** (Ville, processus e) : les fausses alarmes sont contrôlées uniformément dans le temps, sur un horizon illimité. Cela vaut pour les fausses alarmes, pas pour la détection.
- **Validité** **[résultat]** :
  - la garantie promet au plus 0,05 ; bien spécifiée, la règle mesure 0,017 à 0,019 ;
  - sous effet d'épisode (τ = 0,2), elle monte à 0,21 sur 200 actions et à 0,35 sur 1 000 ;
  - réparation : un calibrage sur 1 000 épisodes honnêtes entiers donne 0,046 à 0,055 dans les 17 réglages. Il suppose un corpus d'épisodes honnêtes certifiés de X.
- **Puissance contre la trahison tardive** **[résultat]** :
  - avec une statistique cumulée depuis le début, l'alarme survient avant l'horizon dans 1,000 des cas si le sabotage est au début, mais dans 0,160 seulement s'il est à la fin (borne terminale : 0,158) ;
  - pour alarmer avant la dernière action sabotée, les détecteurs de rupture atteignent 0,52 à 1,00, contre 0,09 à 0,25 pour le cumul, au même taux de fausses alarmes.
- **La confiance comme récurrence** : X a été amical sur une fenêtre vérifiée, et ta capacité de vérifier la suivante n'a pas décroché, y compris si X se modifie ou se réplique. Le pas de récurrence est le point faible (voir le second ordre, section 6).
- **À toi** : ce qu'il faudrait supposer sur X pour qu'une garantie « pour toujours » ait un sens.

## 6. « Sans comprendre ses stratégies » (~140 mots)

- **[hypothèse]** HC6, le test de recette : le g mesuré sur des pressions bénignes prédit l'effondrement sous attaque optimisée. On fait alors confiance à un moniteur par un test d'acceptation, pas en le comprenant.
- **Certificats** : pour bien des propriétés, vérifier coûte moins que produire.
  - Formes : une preuve formelle, ou un débat dont on ne juge que des pas locaux **[mémoire ?]** (Irving et coll., 2018).
  - Limite : on ne certifie que ce qu'on sait spécifier (loi de Goodhart).
  - Règle possible : l'incompréhensible dans une enveloppe réversible, un certificat pour l'irréversible.
- **Formation** : éprouver ses instruments sur des organismes modèles où l'on a soi-même planté le désalignement (programme, section 7). Limite : l'extrapolation à travers l'écart de capacité.
- **Incitations** : elles donnent une amitié d'équilibre, qui s'use quand le rapport de force bascule vers X. Si tu en prends des exemples, dis qu'ils travaillent contre « indéfiniment ».
- **Second ordre** :
  - X préserve ta capacité de le vérifier et de le corriger ;
  - la trajectoire de cette capacité se mesure sans comprendre aucune stratégie : lisibilité, possibilité d'arrêter ou de modifier X, indépendance des vérificateurs ;
  - un X trompeur doit l'éroder, par petits pas défendables un à un : c'est une menace diffuse ;
  - c'est aussi le pas de récurrence de la section 5.
- **À toi** : ta position, avec des exemples que tu connais, humains ou institutions.

## 7. Limites, et ce qui te ferait changer d'avis (~110 mots)

- **[P3 ?]** L'erreur de troncature. Nos documents disent « un faux effet, des verdicts retardés lus comme des verdicts changés » ; le plan v1 dit « un effet de sûreté ». Vérifie lequel avant d'écrire.
- **[résultat]** T0.3 confirme ses 31 prédictions, mais ce sont surtout des vérifications d'instrument, en simulation ; rien encore sur des activations réelles. C'est la réserve R4 : trop beau, donc réserve.
- **Matière optionnelle, la miniature** :
  - le programme est largement exécuté par des agents d'intelligence artificielle ;
  - la confiance y repose sur des engagements scellés, des citations contrôlées par script (106, 0 échec, pour le rapport du lemme) et une contre-vérification tirée au hasard avec une borne exacte (Clopper-Pearson) ;
  - limites : les vérificateurs sont des copies d'un même modèle, et la conformité observée d'un agent n'est qu'une preuve faible.
- **À toi** : une observation qui renverserait ta thèse.

## 8. Conclusion (~60 mots)

- **À toi** : deux ou trois phrases.

## Sources

Empreintes recalculées le 2026-10-08 ; elles correspondent toutes à leurs compagnons scellés.

| Pièce | Chemin | sha256 (16 premiers caractères) |
|---|---|---|
| Résultats de T0.3 | `docs/notes/resultats-T0.3-v1.md` | `9ab618edae17e757` |
| Note lemme et théorème, v3 | `docs/notes/note-mathematique-lemme-theoreme-v3.md` | `dfe4fe0fc4d02501` |
| Programme v2 (HC4, HC6, H5, H8, organismes) | `docs/programme-controle-ia-v2.md` | `2fd63badb5afea48` |
| HC1 retenue (destination libre) | `docs/decisions/decision-N-005-N-006-v1.md` | `cd49afbc924cb1dd` |
| HC4 et H5 retenues | `docs/decisions/decision-N-013-v1.md` | `157d388ef5d0f4df` |
| Croissance au pire cas (2208.07610) | `docs/sources/lecture-pdf-niveau2/rapport-lemme-v1.md` | `a3c837defb10642a` |
| Évasion des sondes (2609.36490) | `docs/sources/lecture-pdf-niveau2/rapport-lot3-Cc-evasion-quorum-v1.md` | `d8c7be40dd7e3137` |
| Antériorité du théorème (2607.11751) | `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` | `c5465a9b0e7fecef` |
| Contre-vérification (Clopper-Pearson) | `docs/procedures/T0.5-extraction-v1.md` | `d23bd62fe1611b87` |
| P3 : les trois leçons | `livrables/proposition-publique-v1/proposal-public-v1.md` | `140f98164a9b4e2c` |

**À vérifier avant d'écrire** :
- les quatre points de P3 (moins de 1 % contre 68 % ; rang 1 contre rang 3 ; la forme de ta loi de sycophancie ; la nature de l'effet de troncature) ;
- les deux références de mémoire (Goldwasser et coll., 2022 ; Irving et coll., 2018).

Budget de mots : environ 980 au total.

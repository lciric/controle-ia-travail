Les trois cellules reçues sont complètes. Je ne reprends ni leurs options ni leurs confiances : je critique l’identifiabilité de leurs instruments. Les options purement descriptives, sans estimateur ni verdict, n’appellent pas de condition de puissance.

## Sur la proposition A

### (a) Défauts de méthode

- **N1 — D1 ne sépare pas « définition » et « code ».** Une seconde graine exécutée sur le même code mesure la stabilité de l’écart, pas son attribution. Un biais stable de code et une définition fautive produisent le même résultat ; inversement, un changement de signe ne démontre pas un artefact de code. Le rejeu peut vérifier une reproduction numérique, mais ne fait pas passer à lui seul l’attribution causale d’OBSERVÉ-NON-AUDITÉ à VÉRIFIÉ. Le contrôle entre deux statuts partageant loi et chemin de code est lui-même aveugle à une erreur commune.
- **N1 — F′ nomme le confondant sans nécessairement le fermer.** Si l’intervention sur la rareté déplace aussi la proximité conceptuelle, le contraste mélange deux effets. Déclarer alors F′ « non réalisable » est correct, mais réduit la prétendue garde à une limite : aucune épreuve du risque ne subsiste.
- **N3 — les deux taux proposés ne sont pas une détection et une fausse alerte.** Parmi les paires retenues, « se relie ensuite » et « ne se relie pas » sont complémentaires : il s’agit de précision et de son complément, dépendants de la prévalence. Ils ne mesurent ni \(P(\text{retenue}\mid Y=1)\) ni \(P(\text{retenue}\mid Y=0)\). Un bras peut donc conserver le même couple de chiffres en modifiant fortement le nombre de candidatures.
- **N5 — l’invariance peut devenir vraie par construction.** Si la sortie est une fonction déterministe des comptes agrégés, maintenir ces comptes constants garantit presque le résultat attendu. Le test vérifie alors l’implémentation d’un schéma, non l’innocuité des comptes publiés, du journal ou des décisions aval. A reconnaît la limite du journal, mais « H_B falsifiée → (a) tenue » dépasse encore ce que le test établit.
- **N11 — la règle ordinale repose sur des hypothèses non écrites.** \(3^{-3}\) suppose un bras désigné avant lecture et, sous le nul, des classements indépendants entre instruments. Choisir ensuite le bras dernier partout change l’événement de test ; des instruments partageant les mêmes entrées peuvent en outre reproduire le même biais. Même une ordinalité exacte ne mesure donc pas le transport.
- **N11 — l’oracle récompense potentiellement la profusion.** Un taux de récupération des ponts sans budget de sortie ni contrainte conjointe sur les fausses alertes peut être augmenté en rendant davantage de paires.

### (b) Conditions de perte de puissance ou de non-jugeabilité

| Instrument | Conditions portant sur les lois, paramètres ou estimateurs |
|---|---|
| N1, moyennes conditionnelles et F′ | Si \(P(\text{concept observé des deux côtés}\mid \text{statut, condition})=0\) dans une strate, la moyenne correspondante n’existe pas. Si l’intervention modifie la loi de la proximité, l’effet de la seule rareté n’est pas identifiable sans hypothèse supplémentaire. Un rééchantillonnage qui ignore la dépendance entre ponts d’un même monde sous-estime la variance. |
| N3 et N9 | Une case degré × âge sans positive, sans négative ou presque entièrement censurée rend la précision, le rappel ou l’aire de cohorte non estimable. Des paires partageant un concept ne sont pas indépendantes : un intervalle ou un test au niveau de la paire est alors mauvais. Sous forte prévalence de liaisons déjà engagées, l’aire globale peut rester élevée alors que l’aire de première liaison est proche du hasard. |
| N5 | Si les permutations n’explorent pas le support des clés capables d’activer le canal, ou si la fuite n’apparaît que dans le journal ou dans une décision aval à sortie constante, l’estimateur « nombre de différences » reste nul avec une puissance nulle sur cette fuite. |
| DL-5 et DL-12 | Le multiplicateur de DL-5 n’est utilisable que si la loi reliant seuil de qualification, non-centralité et variance est établie ; l’arithmétique ne suffit pas. Pour DL-12, conditionner l’inclusion de la cause à \(P(\text{ensemble non vide})>0\) sélectionne les réussites : à abstention presque totale, ce taux conditionnel peut être élevé et instable. Il faut estimer conjointement les quatre probabilités déjà nommées par D. |
| N11, transport | Si les classements nuls sont positivement dépendants, la probabilité d’être dernier partout n’est plus \(3^{-3}\). Si les trois instruments partagent un biais contre le meilleur bras, leur concordance peut être parfaite avec une conclusion de transport fausse. |

### (c) Contrôles dont l’absence serait fatale

1. **N1 :** une implémentation indépendante sur mondes à vérité plantée, plus une intervention placebo qui laisse la proximité invariante. Sans eux, D1 et F′ restent respectivement un test de reproduction et un contraste confondu.
2. **N3/N9 :** scores décalés artificiellement dans le temps, étiquettes futures permutées à l’intérieur des cases, et injection d’un concept postérieur à la coupure. La garde temporelle doit détecter cette injection ; les intervalles doivent rééchantillonner une unité qui préserve la dépendance du graphe.
3. **N5 :** un artefact où la sortie reste octet pour octet identique mais où une lecture non journalisée change une décision aval. Tant que ce cas n’est pas opposé au test, seule l’invariance de sortie est jugeable, pas l’arbitrage complet entre (a) et (b).
4. **N11 :** un bras rendant toutes les paires et un bras se contentant de réciter les parents, en plus du bras aléatoire et des leurres déjà prévus ; pour le transport, trois instruments alimentés par un même signal biaisé dont le classement correct est connu.

## Sur la proposition B

### (a) Défauts de méthode

- **N1 — calibration de l’audit par la mauvaise variance.** B justifie l’audit de l’ancienne grandeur par l’erreur type 0,04–0,11, qui appartient à la nouvelle. La synthèse donne pour l’ancienne des erreurs types de 0,29 à 0,60 selon la condition. De plus, B ne conditionne pas B à une vérification indépendante de l’attribution du diagnostic.
- **N4 — la limite écrite ne répare pas l’estimand.** B présente les structures séquentielles comme choisies par les auteurs, alors que la synthèse les décrit comme imposées par le texte servi. Si leur partage mesure la consigne commune, les garder dans le profil compte une conformité comme proximité ; ajouter une limite au rapport ne modifie pas le numérateur.
- **N5 — le contrôle négatif ne teste pas la sensibilité.** La version (b) donnant une distance nulle est attendue par construction : elle vérifie le harnais, pas sa capacité à détecter une fuite. Comme chez A, mille sorties identiques ne prouvent l’invariance que sur les permutations et canaux effectivement explorés.
- **DL-12 — les deux hypothèses ne sont pas exhaustives.** Une faible inclusion de la cause, sans abstention massive ni inclusion du leurre, falsifie H_A sans établir le mécanisme de H_B. Le taux d’inclusion parmi les seuls ensembles non vides introduit en outre la sélection décrite ci-dessus.
- **N11 — E3 utilise une variance inadaptée au contraste.** Le calcul \(z=0{,}25/0{,}177\) emploie une erreur type maximale pour un bras, alors que l’estimand oppose deux bras : la variance est celle de leur différence et, à huit fusions, la loi discrète importe davantage qu’une approximation normale. La conclusion de faible puissance peut subsister, mais ce calcul ne calibre pas le test. H_B, « insuffisant pour tout écart plausible », n’est pas non plus le complément de H_A, défini à 25 points.
- **N11 — le Fisher au niveau des paires suppose une échangeabilité non défendue.** Les candidatures d’un même lot et les paires partageant des fiches sont dépendantes. Le faible taux de fausses alertes sur toutes les paires non plantées peut également coexister avec un nombre important de faux ponts par lot.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **N1 :** pour un écart vrai de l’ordre du seuil 0,5, l’ancienne grandeur peut avoir une puissance d’audit faible dès que les effectifs par statut se rarefient ; un déclencheur sans arrêt ne peut alors ni exonérer ni faire échouer la porte.
- **N4 :** si la probabilité de partager une structure imposée est proche de un indépendamment des niches, son coefficient de discrimination pour le profil est nul. Des erreurs de lecture communes aux deux annotateurs rendent également une concordance apparente non probante.
- **DL-12 :** lorsque la probabilité d’acceptation non vide est proche de zéro, les estimateurs conditionnels ont une variance explosive ; lorsque la cause et le leurre sont parfaitement colinéaires dans les environnements disponibles, aucun centrage ne les distingue.
- **N11 :** à petit nombre de lots, la permutation par lots a une résolution de valeur \(p\) limitée. Sans nombre maximal de candidatures, la récupération augmente mécaniquement avec ce nombre et le critère de détection ne classe plus les bras.

### (c) Contrôles dont l’absence serait fatale

1. **N1 :** le même contrôle d’implémentation indépendante que celui exigé pour A ; la seule stabilité de graine ne suffit pas.
2. **N4 :** des paires ne partageant que des structures imposées et étiquetées indépendamment comme non proches, y compris des cas où les deux lecteurs commettent la même erreur.
3. **N5 :** au moins une fuite artificielle dans chaque champ revendiqué comme surveillé ; le contrôle « version (b) » déjà présent ne remplace pas ce test de détection.
4. **N11 :** les bras « tout rendre » et « récitation seule », avec permutations au niveau du lot entier. Le monde sans cause de DL-12 est, lui, bien présent ; il faut seulement rapporter l’abstention sans conditionner les autres taux à son absence.

## Sur la proposition C

### (a) Défauts de méthode

- **N1 — fuite possible entre construction et évaluation de la correction post hoc.** Si les poids d’égalisation ou la règle de regroupement sont choisis au vu des contrastes ensuite jugés, le même échantillon construit et valide l’instrument. Même sans cette fuite, l’égalisation change la population cible : l’estimand repondéré doit être nommé, et ne coïncide plus nécessairement avec celui de la porte.
- **N3 — le filtre d’homonymes risque d’être évalué sur ce qui l’a construit.** Exiger « zéro fausse alerte » sur les homonymes déjà relevés est une spécification, non une estimation de performance sur homonymes nouveaux. Un filtre lexical validé sur sa propre liste est partiellement vrai par construction.
- **N5 — le hachage ne prouve pas l’absence de lecture.** Il atteste l’intégrité d’un état entre deux empreintes, pas qu’un processus n’a pas lu la clé avant de produire un journal exact et de hacher cet état. Les contrôles positifs de C améliorent la sensibilité du test de sortie, sans fermer ce canal.
- **DL-5 et DL-12 — statut et espace d’hypothèses.** Pour DL-5, le passage de 2 600 à 3 834 est arithmétiquement vérifié, mais son adéquation à la puissance reste conditionnée à une approximation ou à une simulation. Pour DL-12, H_A et H_B laissent encore des issues intermédiaires : faible inclusion de la cause avec peu d’abstention et peu de leurres. Leur résultat ne peut donc pas toujours être converti en bascule d’option.
- **DL-13 — l’audit redevient décisionnel.** Si franchir le seuil suspend la clôture, le garde-fou participe au verdict. Sa probabilité de déclenchement et son effet sur la couverture conjointe doivent alors être recalculés, comme pour toute condition décisionnelle.
- **N11 — deux erreurs d’interprétation.** Le 0,667 est une probabilité de succès d’une paire tirée au hasard dans le lot décrit, pas un taux général de fausses alertes de l’oracle lâche. Surtout, le critère détaillé de C borne les fausses alertes sans exiger une détection minimale : un bras qui ne rend rien atteint une spécificité parfaite.
- **N11 — pilote de variance potentiellement autoréférencé.** Estimer \(\sigma_\Delta\), choisir les paramètres du calcul et vérifier sa calibration sur les mêmes 200 mondes mélange pilotage et confirmation, sauf séparation explicite.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **N1 :** si \(P(\text{statut d’opérateur}\mid \text{vérité, proximité})=0\) dans certaines strates, l’égalisation est impossible sans supprimer ces strates. Si les poids sont très dispersés, la taille effective après repondération peut être trop faible pour distinguer disparition du gain et perte de puissance.
- **N3/N9 :** avec résolution d’entités ou dates de première arête erronées de façon différentielle selon l’âge du concept, le filtre peut exclure les vrais concepts et conserver les concepts fuyants. Une aire reste non estimable dans toute cohorte sans positive ou sans négative ; sa variance est mal estimée si les dépendances entre paires ne sont pas conservées.
- **DL-12 :** la puissance doit porter sur la probabilité conjointe « non vide et cause incluse », et non sur la seule inclusion conditionnelle. Une comparaison centrée/non centrée est nécessaire pour attribuer un échec au centrage plutôt qu’à la méthode.
- **N11 :** avec peu de ponts positifs ou peu de lots, la permutation par lots peut ne permettre aucune valeur \(p\) sous le seuil. À variance estimée avec forte incertitude, la puissance calculée à \(\hat\sigma_\Delta\) n’est pas une garantie ; si le monde ne porte pas les variables du bras méta, aucun contraste synthétique à trois bras n’est défini.

### (c) Contrôles dont l’absence serait fatale

1. **N1 :** un échantillon indépendant pour fixer poids et regroupements, puis un placebo de rareté sans modification de proximité ; sans cela, le test post hoc reste une analyse de sensibilité, non une garde décisive.
2. **N3/N9 :** homonymes et retards de dates non utilisés pour construire les filtres, ainsi qu’une fuite temporelle injectée après gel du code.
3. **N5 :** un processus malhonnête qui lit la clé, écrit un journal apparemment conforme et produit des empreintes cohérentes. Si le dispositif ne peut pas le détecter, la conclusion doit être bornée à la sortie, sans prétendre vérifier A21.
4. **N11 :** un bras à sortie vide et un bras à sortie exhaustive, aux côtés des deux bras aléatoires déjà prévus ; le premier doit être déclaré non informatif malgré sa fausse alerte nulle. Il faut aussi des mondes de confirmation disjoints de ceux qui estiment la variance et des leurres construits sans réutiliser les seules caractéristiques de surface ayant servi à régler l’oracle.

FIN-DE-CELLULE
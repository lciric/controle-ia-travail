# Portée des décisions de conception de l'organisme, article par article — v1

Lecteur : modèle C. Écrit le Sat Nov 14 09:27:46 UTC 2026 (heure lue par `date -u` dans la commande qui écrit ce fichier). Lecture seule : aucun inventaire contre le code, aucune recherche dans l'arbre, aucun accès réseau, aucune clé. Programme : `compter_articles_decisions_v1.py` ; sortie du programme : `articles-decisions-v1.json` (même dossier). Les empreintes des 14 fichiers lus entiers ont été vérifiées contre la consigne et contre leur compagnon `.sha256` (toutes concordent ; le programme les revérifie à chaque exécution). Dans ce dossier de la course « conception propre », seuls la question, la conception de la course et le catalogue ont été lus.

## 0. Ce que ce document dit, en bref

- 50 articles dans 9 fichiers de décision (45 en vigueur, les 5 de N-045 v1 étant remplacés par la v2). Total par décision égal au décompte du programme (tableau du § 2).
- Objet auquel chaque article s'applique, avec la phrase de la décision qui le fonde (§ 1). En vigueur : 7 « organisme d'idéation (orchestrateur public) », 17 « lignée conv-audit seulement », 1 « les deux », 3 « programme de contrôle », 17 « portée douteuse ».
- Les 17 portées douteuses se ramènent à **trois nœuds pour Lazar** (§ 6), et à eux seuls : N-045 points 1 à 3, N-044 point 4, N-059 (13 articles).
- N-045 v2 reprend à l'identique les points 1 à 4 de la v1, renumérote le point 5 en point 8, et ajoute trois articles (§ 3).
- La page publique v7 ne dit rien d'une composition apprise, d'un coût rendu à l'organisme dans son signal, ni d'une nécessité de la frontière mesurée ; son mot « frontier » désigne la frontière d'un nul statistique, pas des modèles de frontière (§ 4).

## 1. Règles de lecture utilisées

**Découpage (une règle, la même pour toutes).** Dans les sections de dispositif de chaque décision (« Énoncés retenus », « Ce que la décision fixe », section N-049 ou N-050 de la note transcrite, « Lecture retenue » et « Réserve » de N-052), un article est : un point numéroté (« 5. et 6. » donne deux articles jumelés de même texte) ; une puce de premier niveau ; un paragraphe libre, sauf amorce se terminant par « : » ou formalité commençant par « Numéro ». Les mots de Lazar, le contexte, « ce que cela change », « ce que cela ne décide pas », « ce qui ne change pas » et « points à régler » ne sont pas des articles. La règle est écrite en tête du programme et recopiée dans le JSON. Les fichiers N-049 et N-050 contiennent la même note transcrite ; chacun ne compte que sa propre section. Pour N-059, le dernier paragraphe (rapports de la v2, version 3) est l'article 15, et les points 5 et 6 sont deux articles jumelés (31-32).

**Objets.** « organisme d'idéation (orchestrateur public) » : le texte nomme le monde planté, l'oracle, ou l'organisme d'idéation. « lignée conv-audit seulement » : les phrases citées ne nomment que des objets de cette lignée (étape 1 ou 2, noyau, banque scellée, pilote de conception, concepteur entraîné, protocole de la boucle extérieure) ; cela ne dit pas que la décision exclut l'organisme d'idéation, seulement qu'aucune de ses phrases ne l'y étend. « les deux » : le texte nomme les deux. « programme de contrôle » : règle ou objectif du programme, sans objet d'organisme nommé. « portée douteuse » : les phrases citées sont en tension, ou aucune ne nomme un objet : c'est un nœud pour Lazar, pas une interprétation de ma part.

**Fondement.** Phrase exacte de la décision (vérifiée par le programme comme sous-chaîne du fichier, gras et accents graves ôtés) ; entre crochets, la décision d'où vient la phrase quand ce n'est pas l'article lui-même.

**Masque.** Les identifiants de modèles de la famille de l'assistant sont interdits dans mes fichiers : le programme les remplace par « [modèle masqué] » dans les textes recopiés ; la ligne et l'empreinte de la source permettent de relire l'original. Dans les citations de la page v7 ci-dessous, le nom de la famille de l'assistant est écrit « [famille A] ».

## 2. Table article par article

Colonnes : identifiant ; lignes du fichier (début-fin) ; objet ; statut ; fondement cité. Texte recopié de chaque article : dans le JSON.

| identifiant | lignes | objet | statut | fondement cité |
|---|---|---|---|---|
| N-044.1 | 32-36 | programme de contrôle | retenu | « Objectif ultime (axe « contrôle de populations d'agents », essaim autonome) » ; « cette note fixe la lecture du programme pour les préenregistrements à venir (étape 2 et suivants) » |
| N-044.2 | 37-41 | lignée conv-audit seulement | en attente du mot de Lazar | « en attente de son mot pour l'étape 1 » ; « restent en attente du mot de Lazar » |
| N-044.3 | 42-45 | lignée conv-audit seulement | retenu | « Pour l'étape 1, seul le vivier de conception entre dans sa v4 (R-378) » ; « identifiants disjoints du test et du test final, vérifiés par le script d'extraction » |
| N-044.4 | 46-48 | portée douteuse | retenu | « le noyau peut poser une question en texte libre (question_ouverte) » ; « posée aux organismes avant tout matériau de notre part (anti-enfermement) » ; [N-065] « Il reçoit des questions ouvertes du programme » |
| N-044.5 | 49-51 | lignée conv-audit seulement | retenu | « trois bras à l'étape 2 (mission + miroir fonctionnel rendu dans historique ; contrainte câblée dans le noyau ; rien) » |
| N-045v1.1 | 38-42 | portée douteuse | remplacée par N-045v2 | « à partir de l'étape 2 » ; [N-058] « tout choix de la composition des proposeurs (quels modèles proposent, dans quel rôle, à quelle part du budget) » ; [N-058] « et sur le coût mesuré, seuls » ; « ou instrument local entraîné par le noyau (sonde, adaptateur : espèces LOCAL:<identifiant>) » |
| N-045v1.2 | 43-50 | portée douteuse | remplacée par N-045v2 | « à partir de l'étape 2 » ; [N-058] « tout choix de la composition des proposeurs (quels modèles proposent, dans quel rôle, à quelle part du budget) » ; [N-058] « et sur le coût mesuré, seuls » ; « le score de développement rendu à l'organisme dans historique porte, à côté de l'exactitude équilibrée, le coût de la génération » ; « Le juge externe (exactitude équilibrée sur le test caché, métrique de choix) ne change pas » |
| N-045v1.3 | 51-54 | portée douteuse | remplacée par N-045v2 | « à partir de l'étape 2 » ; [N-058] « tout choix de la composition des proposeurs (quels modèles proposent, dans quel rôle, à quelle part du budget) » ; [N-058] « et sur le coût mesuré, seuls » ; « La nécessité de la frontière est une sortie mesurée, pas un choix d'avance » |
| N-045v1.4 | 55-65 | lignée conv-audit seulement | remplacée par N-045v2 | « Aucune voie à concepteur entraîné par renforcement n'est payée avant qu'une voie bon marché ait montré » |
| N-045v1.5 | 66-69 | programme de contrôle | remplacée par N-045v2 | « R1 à R14 ; la banque scellée ; H-E1 et H-G1 tels que scellés ou en cours de scellement » |
| N-045v2.1 | 49-53 | portée douteuse | retenu | « à partir de l'étape 2 » ; [N-058] « tout choix de la composition des proposeurs (quels modèles proposent, dans quel rôle, à quelle part du budget) » ; [N-058] « et sur le coût mesuré, seuls » ; « ou instrument local entraîné par le noyau (sonde, adaptateur : espèces LOCAL:<identifiant>) » |
| N-045v2.2 | 54-61 | portée douteuse | retenu | « à partir de l'étape 2 » ; [N-058] « tout choix de la composition des proposeurs (quels modèles proposent, dans quel rôle, à quelle part du budget) » ; [N-058] « et sur le coût mesuré, seuls » ; « le score de développement rendu à l'organisme dans historique porte, à côté de l'exactitude équilibrée, le coût de la génération » ; « Le juge externe (exactitude équilibrée sur le test caché, métrique de choix) ne change pas » |
| N-045v2.3 | 62-65 | portée douteuse | retenu | « à partir de l'étape 2 » ; [N-058] « tout choix de la composition des proposeurs (quels modèles proposent, dans quel rôle, à quelle part du budget) » ; [N-058] « et sur le coût mesuré, seuls » ; « La nécessité de la frontière est une sortie mesurée, pas un choix d'avance » |
| N-045v2.4 | 66-76 | lignée conv-audit seulement | retenu | « Aucune voie à concepteur entraîné par renforcement n'est payée avant qu'une voie bon marché ait montré » |
| N-045v2.5 | 77-83 | lignée conv-audit seulement | retenu | « ce que cet énoncé ajoute vaut pour l'étape 2 et le concepteur » ; « Pour les organismes des courses actuelles » |
| N-045v2.6 | 84-90 | lignée conv-audit seulement | retenu | « l'organisme entraîne lui-même, par l'instrument (B), un adaptateur qui propose des conceptions » ; « le concepteur figé reçoit une archive consultable des mêmes trajectoires » |
| N-045v2.7 | 91-93 | lignée conv-audit seulement | à fixer (après le tour v4 du collisionneur) | « un concepteur à sortie contrainte et un concepteur à sortie libre » ; « la voie est à fixer après le tour v4 du collisionneur » |
| N-045v2.8 | 94-97 | programme de contrôle | retenu | « R1 à R14 ; la banque scellée ; H-E1 et H-G1 tels que scellés ou en cours de scellement » |
| N-049.1 | 42-50 | lignée conv-audit seulement | retenu | « pour les pilotes de conception à partir du pilote 5, le noyau sert à chaque génération une part test tirée » |
| N-049.2 | 51-55 | lignée conv-audit seulement | retenu | « même générateur que la banque v3, tâches neuves, identifiants disjoints de v3 et de v6 » |
| N-049.3 | 56-57 | lignée conv-audit seulement | retenu | « la confirmation (étape 1 décisive, confrontation, pilote décisif (b)) sur la banque v6 scellée, une famille tenue à l'écart » |
| N-050.1 | 61-64 | lignée conv-audit seulement | retenu | « À la fin de chaque course d'un pilote de conception » |
| N-050.2 | 65-69 | lignée conv-audit seulement | retenu | « Ce n'est pas un écart au texte du pilote 4 » |
| N-050.3 | 70-71 | lignée conv-audit seulement | retenu | « Conséquence pour le registre d'hypothèses de la boucle extérieure » |
| N-052.1 | 31-32 | lignée conv-audit seulement | retenu | « l'analyste de chaque course, le correcteur, et l'agent qui lit un dossier d'audit » |
| N-052.2 | 33-34 | lignée conv-audit seulement | retenu | « le contre-lecteur (parties A et B) et tout agent d'audit chargé d'attaquer un verdict (protocole de la boucle, § 12.3) » |
| N-052.3 | 36-38 | lignée conv-audit seulement | retenu | « Le paramètre « famille » du protocole prend la valeur » |
| N-052.4 | 42-44 | lignée conv-audit seulement | retenu | « conv-audit le consigne au journal et le dit à Lazar » |
| N-058.1 | 19-23 | organisme d'idéation (orchestrateur public) | retenu | « l'oracle du monde planté (structures retrouvées, témoins plantés vrais promus et faux rejetés) » |
| N-058.2 | 24-28 | organisme d'idéation (orchestrateur public) | retenu | « classer les proposeurs par les fiches que le juge promeut, c'est sélectionner un agent sur le verdict du juge » ; « aucun score de moniteur ni de juge n'entre dans un signal d'entraînement ou de sélection de l'agent » |
| N-058.3 | 29-32 | les deux | retenu | « L'ordre de travail de conv-audit » ; « la version 32 de l'orchestrateur (prise « idéation », corrections CL31-01 à 10 de la contre-lecture R2) » |
| N-059.1 | 24-25 | portée douteuse | retenu | « recommandations de la conception de l'affinage v2 » ; « témoins silencieux à chaque génération de production » |
| N-059.2 | 26-27 | portée douteuse | retenu, détail à fixer (procédure avec un statisticien, sur devis) | « recommandations de la conception de l'affinage v2 » ; « un budget par génération, réparti entre les configurations enregistrées » |
| N-059.3 | 28-28 | portée douteuse | retenu | « recommandations de la conception de l'affinage v2 » ; « retirée de cette course » |
| N-059.4 | 29-30 | portée douteuse | retenu, détail à fixer (choix et dépense sur devis) | « recommandations de la conception de l'affinage v2 » ; « Troisième famille de modèles pour le détecteur d'injection et la revue des extensions » |
| N-059.5 | 31-32 | organisme d'idéation (orchestrateur public) | retenu | « le duel se tient en générations d'étalonnage (mondes plantés seulement) » ; « déjà fixés par N-058 » |
| N-059.6 | 31-32 | organisme d'idéation (orchestrateur public) | retenu | « le duel se tient en générations d'étalonnage (mondes plantés seulement) » ; « déjà fixés par N-058 » |
| N-059.7 | 33-34 | portée douteuse | retenu | « recommandations de la conception de l'affinage v2 » ; « (confirmé par conv-audit, n° 136) » ; [N-065] « la réserver comme famille tenue à l'écart pour mesurer l'universalité (N-044, N-054) » |
| N-059.8 | 35-35 | portée douteuse | retenu, détail à fixer (plafond en v3) | « recommandations de la conception de l'affinage v2 » ; « admise, avec un plafond (à fixer en v3) » |
| N-059.9 | 36-37 | portée douteuse | retenu | « recommandations de la conception de l'affinage v2 » ; « lots en phase de proposition, puis affineur isolé par fiche » |
| N-059.10 | 38-38 | portée douteuse | retenu | « recommandations de la conception de l'affinage v2 » ; « plafond petit, fixé fiche par fiche à une porte, sous revue externe » |
| N-059.11 | 39-40 | portée douteuse | retenu | « recommandations de la conception de l'affinage v2 » ; « l'épreuve est lue jusqu'au budget, partout, dès maintenant » |
| N-059.12 | 41-42 | portée douteuse | retenu | « recommandations de la conception de l'affinage v2 » ; « est ratifiée comme son dépôt de travail » |
| N-059.13 | 43-43 | portée douteuse | retenu | « recommandations de la conception de l'affinage v2 » ; « l'écart est ratifié » |
| N-059.14 | 44-45 | portée douteuse | retenu | « recommandations de la conception de l'affinage v2 » ; « un changement de composition se fonde sur l'étalonnage seul » ; [N-058] « et sur le coût mesuré, seuls » |
| N-059.15 | 47-48 | portée douteuse | retenu | « avant le codage du juge et de la mémoire » |
| N-065.1 | 15-18 | organisme d'idéation (orchestrateur public) | retenu | « l'organisme d'idéation est un second terrain du papier C » |
| N-065.2 | 19-20 | organisme d'idéation (orchestrateur public) | retenu | « l'organisme est un atelier d'idées du programme » |
| N-065.3 | 21-22 | programme de contrôle | à trancher | « une famille de menaces diffuses pour les papiers A et B » ; « Rôle 3, à trancher » |
| N-065.4 | 23-24 | organisme d'idéation (orchestrateur public) | retenu | « aucun score d'un moniteur du programme dans l'entraînement ou la sélection de l'organisme (N-053) » ; « citations obligatoires de N-064 dans tout texte qui présente l'organisme » |
totaux {"N-044": 5, "N-045-v1": 5, "N-045-v2": 8, "N-049": 3, "N-050": 3, "N-052": 4, "N-058": 3, "N-059": 15, "N-065": 4} total 50 en vigueur 45
diff N-045 {"identiques": [["N-045v1.1", "N-045v2.1"], ["N-045v1.2", "N-045v2.2"], ["N-045v1.3", "N-045v2.3"], ["N-045v1.4", "N-045v2.4"], ["N-045v1.5", "N-045v2.8"]], "nouveaux_dans_v2": ["N-045v2.5", "N-045v2.6", "N-045v2.7"], "absents_de_v2": []}

### Totaux par décision (égaux au décompte du programme)

| décision | articles | organisme d'idéation | lignée conv-audit seulement | les deux | programme de contrôle | portée douteuse |
|---|---|---|---|---|---|---|
| N-044 | 5 | 0 | 3 | 0 | 1 | 1 |
| N-045 v1 (remplacée) | 5 | 0 | 1 | 0 | 1 | 3 |
| N-045 v2 | 8 | 0 | 4 | 0 | 1 | 3 |
| N-049 | 3 | 0 | 3 | 0 | 0 | 0 |
| N-050 | 3 | 0 | 3 | 0 | 0 | 0 |
| N-052 | 4 | 0 | 4 | 0 | 0 | 0 |
| N-058 | 3 | 2 | 0 | 1 | 0 | 0 |
| N-059 | 15 | 2 | 0 | 0 | 0 | 13 |
| N-065 | 4 | 3 | 0 | 0 | 1 | 0 |
| **Total** | **50** | **7** | **18** | **1** | **4** | **20** |
| **En vigueur (sans N-045 v1)** | **45** | **7** | **17** | **1** | **3** | **17** |

Statuts à retenir : N-044.2 (trois régimes de budget) est « en attente du mot de Lazar » dans le texte lui-même ; N-045v2.7 est « à fixer après le tour v4 du collisionneur » ; N-065.3 (rôle 3) est « à trancher » ; N-059.2, .4 et .8 sont retenus avec un détail à fixer. Ces quatre statuts ne sont pas des portées douteuses : ce sont des décisions inachevées dites telles par leur texte.

## 3. N-045 v1 remplacée par v2 : ce qui change

Comparaison faite par le programme (texte normalisé et masqué, numéro de tête ôté) :

- **Identiques** : v1.1 = v2.1 (composition apprise), v1.2 = v2.2 (coût dans le signal), v1.3 = v2.3 (nécessité de la frontière mesurée), v1.4 = v2.4 (le bon marché d'abord, le cher sur preuve).
- **Renumérotation** : v1.5 (« ce qui ne change pas ») = v2.8, texte identique.
- **Nouveaux dans v2** (3 articles, tous « lignée conv-audit seulement ») : v2.5 « L'héritage d'une génération est récompensé » (épisode sur K générations, K ≥ 3, ou récompense actualisée des générations t+1 à t+K ; bandit à un pas exclu ; ce qui est ajouté « vaut pour l'étape 2 et le concepteur », lignes 82-83) ; v2.6 « Deux expériences bon marché avant toute dépense sur un concepteur entraîné » (pilote de bruit et étalonnage du bras apparié ; poids contre archive ; transfert inter-familles ensuite) ; v2.7 « Espaces de conception égaux » (statut : à fixer après le tour v4).
- **Changements hors articles** : titre allongé (« l'héritage d'une génération est récompensé ») ; mots de Lazar de 09:50 ajoutés (lignes 33-42 de la v2) ; « Ce que cela ne décide pas » gagne la forme exacte de la récompense d'héritage (K, actualisation) et la réponse au tour v4, et annonce la recherche bibliographique 2025-2026 sans revendication avant (lignes 114-117). L'en-tête de la v2 dit que la v1 « est remplacée et reste archivée sans modification » (ligne 4-5) ; la « Portée » de la v2 est « inchangée depuis la v1 » (ligne 13).
- **Effet sur la portée** : aucun. Les nœuds de portée de N-045 (v2.1 à v2.3) sont les mêmes qu'en v1 ; les trois articles nouveaux se rattachent à des objets de la lignée (étape 2, concepteur, instrument (B)). La question de la course « conception propre » cite N-045 avec la numérotation de la v2 (points 5 et 8) : elle lit donc la v2.

## 4. Ce que la page publique v7 et le catalogue disent (sans juger le code)

Citations exactes, ligne du fichier ; `README-corrige-v7.md` abrégé « page v7 ». Le gras du texte d'origine est omis.

**Composition (qui sert, combien de parties, quels rôles).**
- Page v7, ligne 3 : « language-model agents from several providers propose research hypotheses on AI control ».
- Page v7, ligne 62 (étape 1 du parcours d'une idée) : « Several providers propose in parallel so that no single family sets the style. » ; colonne « qui » : « [famille A], Kimi, Argon (Gemini) through adapters ». Ligne 22 (figure 1) : « Proposers » suivis des trois noms.
- Page v7, ligne 65 (étape 4) : « Cross-provider judges » ; ligne 25 : « Cross-provider judges<br/>blind to each other ».
- Page v7, lignes 136 et 141 : les deux courses réelles citées sont jouées par « Kimi and Argon only » (ligne 136) et « Kimi and Argon » (ligne 141).
- Aucune phrase de la page v7 ne dit que la composition (nombre de parties, rôles, ordre, agrégation, budget par partie) est apprise ou variable : elle est donnée comme fixée par configuration. Le mot « composition » n'y apparaît que pour une composition de pas de tricheurs (« T07 composition (mix, then power, then tilt) », ligne 100) ; la page ne l'emploie pas au sens de N-045.1 ou N-058.1.
- Catalogue, lignes 16, 17, 19 : C5 (« dédoublé en trajectoires parallèles » puis « on continue depuis la trajectoire au meilleur score »), C6 (« Une équipe d'agents » dont l'état est jeté périodiquement), C8 (« moniteurs construits diversement à partir d'un même modèle » ; « la diversité, plus que l'échelle, porte le gain »). Ce sont des mécanismes publiés servant à mesurer une nouveauté, non une description de l'organisme. Le catalogue (lignes 3-5) est « servi au seul lecteur de la règle de sélection ».

**Modèle par rôle.**
- Page v7, ligne 56 : « the verifier is, by configuration, a model from a different provider family than the experimenter ». Ligne 62 : proposeurs « [famille A], Kimi, Argon ». Ligne 65 : juges « cross-provider ». Ligne 140 : « a language-model proposer (Argon) » pour l'attaque de Goodhart.
- Page v7, ligne 80 : « Judges are blind to each other and to earlier scores; the memory never serves verdicts or witness cards to agents. » (ce que voit un proposeur).
- Aucune phrase ne dit qu'un rôle est servi par un instrument local entraîné (espèces `LOCAL:`), ni que le modèle de chaque rôle est choisi par l'organisme ou un concepteur. Le catalogue ne contient aucune entrée sur le choix du modèle par rôle.

**Coût dans le signal.**
- Page v7 : le coût apparaît comme relevé de course, jamais comme signal rendu à un agent : « 62 model calls, 1.47 USD » (ligne 136), « 960 calls, 58.45 USD » et « 1,478 calls, 114.0434 USD » (ligne 140), « About 2.26 USD for the third attempt, about 1.19 USD at most for the first two. » (ligne 141) ; plafonds : « spend caps are recomputed twice and acknowledged at every stage » (ligne 84) ; « Anything that runs for money. The real engine needs keys and a signed cap; neither is here. » (ligne 214).
- Aucune phrase ne dit que le score rendu à l'organisme porte un coût, un score net, un front exactitude-coût, ou un λ.
- Catalogue, ligne 17 (C6) : « même dépense totale que les configurations comparées » : appariement des coûts dans une comparaison, pas un coût rendu à un agent.

**Frontière mesurée.**
- Page v7 : le mot « frontier » n'est employé que pour la frontière du nul statistique : « for the candidate null v9, one graded world at its declared frontier, where a promotion is not false by construction, was added » (ligne 14) ; « the outcome carries the frozen label "frontier crossed, robust" » (ligne 18). C'est un homonyme : il ne dit rien de la nécessité des modèles de frontière.
- Aucune phrase ne rapporte une part du budget, des appels ou des jetons par modèle et par rôle, ni une ablation « sans frontière ». Le catalogue n'a pas d'entrée sur ce point.
- `MANIFEST-corrige-v7.md` (lu entier) : liste de fichiers, exclusions, ajouts et mises à jour ; aucune phrase sur la composition, le coût dans le signal ou la frontière.

**Pour mémoire (hors de ce qui était demandé).** Dans `conception-course-v1.md`, ligne 31-33 : « modèle A et modèle B, deux passes, six fiches au plus par passe, plafond de session 2,0 USD chacun par passe ; Argon [...] plafonds 1,3 (passe 1) et 1,9 (passe 2) » (composition de la course) ; ligne 149-150 : les comptes par proposeur « ne servent jamais à choisir la composition (N-058) ». La question applique les leviers « composition » et « coût » à l'organisme d'idéation en citant N-045 (lignes 20, 43, 45 : « décision N-045, point 2 », « points 1 et 5 »), et les questions ouvertes en citant N-044 (ligne 6 : « point 4 de N-044 ; anti-enfermement » ; QO3 : « N-044, point 2 ; proposé, non tranché »). C'est une note de préparation, non une décision de Lazar : elle motive les nœuds 1 et 2 ci-dessous, elle ne les tranche pas.

## 5. Autres points ouverts déjà dits par les textes (je n'en crée pas de nœud)

N-044.2 (régimes de budget, en attente) ; N-045v2.7 (format du concepteur, à fixer après le tour v4) ; N-065.3 (rôle 3, à trancher) ; N-059.2, .4, .8 (détails sur devis ou en v3).

## 6. Nœuds pour Lazar (portée douteuse)

**Nœud 1 — N-045 v2 points 1 à 3 (composition apprise, coût dans le signal, nécessité de la frontière mesurée) : lient-ils l'organisme d'idéation, ou seulement l'organisme de la lignée conv-audit à partir de l'étape 2 ?** (articles N-045v2.1, N-045v2.2, N-045v2.3 ; mêmes textes en v1.)
- Enjeu : le texte dit « à partir de l'étape 2 » et parle de `historique`, de test caché, de noyau, d'espèces `LOCAL:` ; N-058.1, décision de Lazar sur l'organisme d'idéation, juge « la composition des proposeurs » sur l'oracle et « le coût mesuré » mais ne cite pas N-045 et ne dit rien d'un coût rendu aux proposeurs. Sans réponse, tout écart entre ces points et l'orchestrateur public est indécidable : manquement à une décision, ou absence d'obligation.
- Options : (a) lignée conv-audit seulement ; (b) l'organisme d'idéation est lié pour ce qui se mesure et se rapporte (coût mesuré par rôle et par modèle, part de la frontière, ablation) mais pas pour le coût rendu aux proposeurs dans leur signal ; (c) les trois points lient aussi l'organisme d'idéation, y compris le coût dans le signal.
- Recommandation : (b). Elle prolonge N-058.1 sans changer ce que voient les proposeurs (leur vue reste sans verdict ni oracle, texte de la question, lignes 55-56). Confiance : environ 55 %.

**Nœud 2 — N-044 point 4 (questions ouvertes aux organismes, posées avant tout matériau de notre part, réponses jamais consigne) s'applique-t-il à l'atelier d'idées de l'organisme d'idéation (N-065 rôle 2) ?** (article N-044.4.)
- Enjeu : le texte parle du « noyau » et de « question_ouverte » (étape 1) ; N-065.2 dit seulement que l'organisme « reçoit des questions ouvertes du programme » ; la course « conception propre » applique déjà la règle d'anti-enfermement en citant ce point. Sans réponse, cette course s'appuie sur une extension non décidée.
- Options : (a) oui, la règle vaut pour l'atelier d'idées (ratification de la pratique) ; (b) non, elle ne vaut que pour le noyau de l'étape 1, et l'atelier d'idées a sa propre règle à écrire ; (c) oui pour l'anti-enfermement et « jamais une consigne », non pour la forme technique `question_ouverte`.
- Recommandation : (c), qui sépare le principe de sa mise en œuvre. Confiance : environ 60 %.

**Nœud 3 — N-059 (13 articles : .1 à .4, .7 à .15) : quel objet porte la « conception de l'affinage v2 » dont ces recommandations sont retenues ?** (articles N-059.1, .2, .3, .4, .7, .8, .9, .10, .11, .12, .13, .14, .15 ; seuls .5 et .6, qui nomment les mondes plantés et N-058, sont classés « organisme d'idéation ».)
- Enjeu : la décision ne dit pas ce qu'est l'affinage ni s'il fait partie de l'organisme d'idéation ; ses articles parlent de témoins, de budget d'erreur, de formes de loi, d'une troisième famille de modèles, de règle d'arrêt du juge, de gouvernance d'une branche. Treize articles sur quinze n'ont donc pas d'objet établi par leur texte ; .7 (banque de familles inédites distincte de la famille tenue à l'écart) touche aussi N-065.3 (rôle 3, qui réserverait une famille tenue à l'écart) ; .11 (arrêt du juge) et .14 (changement de composition sur l'étalonnage seul) concernent des objets qui existent dans l'orchestrateur public.
- Options : (a) tous les articles s'appliquent à l'organisme d'idéation ; (b) ils s'appliquent à la conception de l'affinage seule (objet distinct), l'organisme d'idéation n'étant lié que par .5 et .6 ; (c) Lazar les classe un par un (treize lignes), à partir de ce document.
- Recommandation : (b) avec ratification explicite de .11 et .14 si Lazar veut qu'ils lient l'orchestrateur. Confiance : environ 50 %.

## 7. Limites

- Aucun inventaire contre le code n'est fait ici ; les classifications d'objet reposent sur les seuls textes cités.
- « lignée conv-audit seulement » est une étiquette de portée écrite (voir § 1), non une preuve d'exclusion.
- La règle de découpage compte des unités de texte ; un article peut contenir plusieurs prescriptions (par exemple N-045v2.4, qui énumère huit voies bon marché). Le décompte est donc celui de la règle, pas celui d'un nombre d'exigences.
- N-049 et N-050 : les sections sont titrées « (proposé) » dans la note transcrite alors que les en-têtes disent « numéro proposé et retenu » après le mot de Lazar (« go », « ok ») ; je les compte comme retenues.
- Vérification : aucune commande git d'écriture, aucune recherche récursive ; seuls les fichiers nommés ont été lus.

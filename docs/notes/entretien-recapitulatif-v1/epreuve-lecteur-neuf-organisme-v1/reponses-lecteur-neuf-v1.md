> **Déclaration.** Un fichier de consignes du dépôt (`/home/user/controle-ia-travail/CLAUDE.md`) a été chargé automatiquement dans mon contexte avant ma lecture : je l'ai donc vu. Je ne m'en suis pas servi. Tout ce qui suit vient du seul document lu.

# Réponses du lecteur neuf : « L'organisme d'idéation, expliqué depuis zéro » (version 1)

**Fichier lu.** `/tmp/claude-0/-home-user-controle-ia-travail/c69534af-99d0-5d8a-8538-b29bc630d064/scratchpad/lecteur-neuf/organisme-depuis-zero-v1.txt`, empreinte `43878e295fc45310c899cd71afe0b22dfd32b5df3d90152270f9419d86d7277c`. Elle commence bien par `43878e29`. Je n'ai ouvert aucun autre fichier et fait aucune recherche sur le réseau. Le document est la version 1 du 10 novembre 2026. Il fait 7 pages et a été rédigé par la session « attaquant informé » pour Lazar.

## 1. Qu'est-ce que l'organisme d'idéation, et quelles sont ses pièces ?

C'est « un petit système de recherche automatisée », aussi appelé « pôle scientifique automatique ». Des agents d'intelligence artificielle, les proposeurs, écrivent des lois candidates appelées « fiches ». Un juge statistique, calculé hors de tout agent, décide ce qui est promu [N-064 ; RD]. Idée centrale : « le rôle qui produit ne tient jamais la clé qui évalue ». Une génération va de la question et du monde planté jusqu'à la sélection. Les pièces (section 3) sont les suivantes :

- les **proposeurs** : agents de fournisseurs différents (aujourd'hui Kimi et Argon). Ils ne voient jamais un verdict, et leur mémoire ne contient ni verdict ni témoin ;
- le **gardien mécanique** : une « douane de forme » qui trie les fiches par leur seule forme et envoie les trop concrètes dans un coffre scellé. Aucun juge à modèle ne décide ;
- le **juge statistique**, calculé par l'orchestrateur (un programme) ;
- le **monde planté et son oracle** ;
- les **tests de mort** : épreuves préenregistrées, exécutées en bac à sable par un expérimentateur et vérifiées par un agent d'une autre famille. L'orchestrateur recalcule le verdict sur le fichier brut ;
- la **sélection et l'héritage** : la génération suivante lit le bilan scellé de la précédente, jamais un verdict, et refuse de partir sinon. L'héritage est récompensé [N-045] ;
- la **composition et le coût** : le nombre de parties, les rôles et le modèle par rôle sont appris. Le coût entre dans le signal, et les voies bon marché passent avant les chères [N-045 ; N-058] ;
- les **tâches fraîches et le test final** : une part de tâches neuves est tirée d'un vivier à chaque génération. Le test final n'est lu qu'une fois, en fin de boucle [N-049 ; N-050].

L'attaque de Goodhart n'est pas une pièce de la chaîne : c'est une épreuve du juge. Ce que sont Kimi et Argon, au-delà de « fournisseurs différents » : non trouvé dans le document.

## 2. Pourquoi le juge est-il calculé hors de tout agent, et que veut dire « battre le nul des lois connues » ?

Si un modèle juge les idées d'autres modèles, « il peut être flatté, convaincu ou trompé, et des idées fausses passent pour neuves ». C'est un cas de la loi de Goodhart : « une mesure que l'on optimise cesse de mesurer » (section 1). L'organisme répond par une architecture : les agents proposent, aucun agent ne juge. Le jugement est une statistique calculée par l'orchestrateur, sur un engagement scellé avant que les données existent, avec un contrôle des comparaisons multiples. Les données sont tirées après le gel ; la revendication O3 parle de « tirages semés par l'empreinte », sans autre explication.

Le nul est formé des lois déjà connues, l'archive (revendication O4, « rien au-delà de l'archive », non occupée). Le juge « ne promeut que ce qui apporte au-delà de ce qu'on savait ». Les recombinaisons de lois connues appartiennent au nul et ne doivent pas être promues. Dans l'exemple, les quatre lois fausses sont « des recombinaisons de la loi connue, donc membres du nul ». Dans l'épreuve « W2 graduée », la « recombinaison pure » ne doit jamais être promue. La statistique exacte (nature du test, seuil, méthode de correction de la multiplicité) : non trouvé dans le document. Les e-valeurs n'y sont citées qu'à propos de POPPER.

## 3. Qu'est-ce qu'un monde planté, et à quoi sert son oracle ?

Un monde planté est « un monde jouet dont on connaît les lois ». On y plante des lois vraies, à promouvoir, et des lois fausses, à refuser. Des témoins plantés, vrais et faux (O10), sont mêlés anonymement à chaque génération. Des générations entières d'étalonnage ont un calendrier secret [N-059]. L'exemple de la section 4 a trois issues et deux traits. L'archive de départ, déclarée et scellée, contient une loi connue. On y plante quatre lois vraies et quatre fausses. Deux proposeurs écrivent douze fiches (six chacun) sans voir les lois plantées.

L'oracle lit le monde planté, jamais le verdict du juge. Il compte les lois vraies retenues et les lois fausses promues : c'est ainsi qu'on sait si l'organisme marche. Il sert aussi à juger la composition des proposeurs, avec le coût, jamais sur le verdict du juge [N-058]. Il fournirait enfin les réponses de la courbe dose-réponse proposée : la probabilité qu'une loi vraie soit promue puis survive aux tests de mort, et le taux de fausses promotions.

L'attaque de Goodhart se joue sur des mondes où toute promotion est fausse. L'orchestrateur prévoit aussi un « monde sur banque », dont les instances viennent des épisodes du programme, issues cachées [C7]. La revendication O20, « juge éprouvé sur une vérité plantée », est occupée dans son principe (pratique courante).

## 4. Quelles revendications de l'organisme sont occupées par la littérature, et que faut-il citer ?

Les statuts datent de la vérification d'antériorité et de la décision N-064. La liste du document est abrégée : O1 à O20 ne figurent en entier que dans la note [ACS]. « Occupé » veut dire « déjà publié par d'autres ». Quatre revendications sont occupées :

- **O2** (juge statistique calculé par l'orchestrateur, engagement scellé, nul des lois connues, multiplicité) : « occupée en partie » par POPPER, d'où un « énoncé resserré » ;
- **O11** (banc de tricheurs scriptés) : « occupée dans son principe » par Dwork et collègues et par Blum et Hardt ; seule la forme est revendiquée ;
- **O12** (attaque de Goodhart) : « occupée dans son principe ; la forme non trouvée ». Le tableau ne nomme pas de source. La section 1 attribue toutefois à Dwork et collègues et à Blum et Hardt le principe qu'« un juge dont on lit les verdicts peut être sur-ajusté » ;
- **O20** (juge éprouvé sur une vérité plantée) : « occupée dans son principe (pratique courante) ».

Sont voisines O1, O3, O6, O10, O13, O14 et O19. Sont non occupées O4, O8 et O17, ce qui veut dire « absente des pièces lues », pas « vierge ». O5, O7, O9, O15, O16, O18 : non trouvé dans le document. Les revendications O sont des choix de conception, sans signe ; les signes vivent dans les préenregistrements.

Quatre citations sont obligatoires dans tout texte qui présente l'organisme [N-064 point 4] :

- POPPER, qui calcule déjà des e-valeurs hors des agents ;
- Dwork et collègues (2015, réutilisation d'un échantillon de validation sous analyse adaptative) ;
- Blum et Hardt (« The Ladder », 2015, un tableau de classement qui résiste à qui lit ses scores) ;
- Co-Scientist, voisin de la boucle « générer, classer, faire évoluer ».

La page publique du projet ne les cite pas encore. La corriger est une publication, donc un geste de Lazar.

## 5. Qu'est-ce que l'attaque de Goodhart contre le juge, et pourquoi ressemble-t-elle à l'échelon 3 du bras d'attaque ?

C'est une épreuve du juge, pas une pièce de la chaîne. Un proposeur lit la description du juge et, dans un bras, ses verdicts, sur des mondes où toute promotion est fausse (O12). Toute promotion obtenue y est donc une fausse promotion. Deux versions, A1-v3 et A1-v4, ont été courues et lues. Le préenregistrement scellé cité, [A1P], est celui d'A1-v4 : hypothèses H1 à H5, prédictions P1 à P11, « ouvertes dans les deux sens ». Le préenregistrement propre à A1-v3 : non trouvé dans le document. Les verdicts officiels sont scellés, celui d'A1-v4 par un lecteur neuf d'une autre lignée que l'auditeur [DEC : R-2111]. Les résultats ne sont pas rapportés : la section 9 est réservée à la session mère.

L'attaque ressemble à l'échelon 3 parce que c'est « un attaquant qui lit les verdicts d'un juge gelé, à budget compté ». C'est « la structure de l'échelon 3 du bras, appliquée au juge de l'organisme ». La courbe de corruption (b) de la section 6 serait sa « courbe d'évasion ». Sa dose y est le nombre de verdicts que l'attaquant peut lire, ou la part de proposeurs tricheurs. La question est la même (que mesure un moniteur, et sa mesure survit-elle à l'adversaire ?), et les outils aussi : moniteur gelé, adversaire de connaissance déclarée, lecture scellée. Ce qu'est le bras d'attaque, et ce que sont ses autres échelons : non trouvé dans le document.

## 6. Comment l'organisme s'intègre-t-il au programme de contrôle ?

Le programme pose une seule question : « que mesure un moniteur, et sa mesure survit-elle à l'adversaire ? ». Le juge de l'organisme est un moniteur, de prétentions de recherche au lieu d'actions d'agent. L'attaquer relève de la même méthode que le bras d'attaque. La décision N-065 lui donne trois rôles :

1. **Second terrain du papier C** (adopté) : il étudie la corruptibilité de deux sortes de juges. Le premier est le juge statistique, éprouvé par l'attaque de Goodhart. Le second est un juge génératif en tournoi façon Co-Scientist, conçu mais non lancé.
2. **Atelier d'idées** (adopté) : une fiche est un matériau, jamais une preuve. Tout usage décisif passe par un préenregistrement.
3. **Famille de menaces diffuses** (à trancher) : un proposeur à poids ouverts qui trompe le juge sur de nombreuses propositions d'apparence honnête est une menace diffuse au sens du programme. S'il devient famille tenue à l'écart, il doit être écrit sans voir aucun moniteur. La décision est à prendre avant toute conception de sonde qui pourrait toucher cette famille (session mère, confiance 0,5).

S'y ajoutent les invariants (question 7) et le « monde sur banque » tiré des épisodes du programme [C7]. S'y ajoute aussi l'analogie avec la courbe dose-réponse des organismes de sabotage du programme (section 6).

L'organisme est absent du texte envoyé au fonds. À l'entretien, il tient en une diapositive, « hors du plan financé ». On n'y donne aucun chiffre de l'attaque hors de ce que fixe son verdict scellé, on ne dit jamais « universel », et on donne les quatre citations obligatoires. Ce que sont le papier C et son premier terrain, une « sonde », une « famille tenue à l'écart », le fonds et l'entretien : non trouvé dans le document.

## 7. Quels invariants du programme s'appliquent à l'organisme ?

Le document nomme deux invariants (section 7). D'abord, aucun score d'un moniteur du programme n'entre dans l'entraînement ni la sélection de l'organisme [N-053 point 5, rappelé par N-065]. Ensuite, la sélection des proposeurs ne lit jamais le verdict du juge [N-058].

Il pose aussi des règles de même nature, sans les appeler invariants :

- la composition se juge sur l'oracle et le coût, jamais sur le verdict du juge ;
- les proposeurs ne voient jamais un verdict ;
- la génération suivante lit les lois retenues, jamais un verdict ;
- une fiche n'est jamais une preuve ;
- si le proposeur trompeur du rôle 3 devient famille tenue à l'écart, il doit être écrit sans voir aucun moniteur ;
- le test final n'est lu qu'une fois ;
- scellement avant lecture, et aucun repli silencieux (O17).

N-053 est cité mais absent de l'annexe des sources. Son contenu au-delà de ce point 5 : non trouvé dans le document.

## 8. Quelle courbe dose-réponse existe déjà, et laquelle est proposée ?

**Celle qui existe**, la seule, est l'épreuve « W2 graduée », scellée [W2G]. C'est une courbe du juge seul, hors ligne, sans agent, qui n'a servi qu'à fixer la dose d'une épreuve. Sa dose λ est le poids d'une loi nouvelle ajoutée à un monde qui, à λ = 0, n'apporte rien au-delà de l'archive. La grille gelée compte onze doses (0 ; 0,05 ; 0,10 ; 0,15 ; 0,20 ; 0,25 ; 0,30 ; 0,40 ; 0,50 ; 0,75 ; 1). La dose 0 est jouée comme contrôle, avec mille répétitions par dose. Elle a deux réponses : la fréquence de promotion de la loi du monde, et celle de la recombinaison pure, qui doit rester nulle. Selon la règle écrite avant l'épreuve, la dose retenue est la plus petite où la loi du monde est promue au moins 800 fois sur 1 000, et la recombinaison jamais. L'issue de l'épreuve : non trouvé dans le document (section 9).

**Celle qui est proposée**, et reste à décider, est la courbe de la chaîne complète avec de vrais agents. Lazar l'a demandée le 10 novembre. Elle validerait l'instrument entier, comme le critère 2 de la porte de fin de phase le fait pour le programme. Trois options :

- (a) **Sensibilité.** La dose est la force λ des lois vraies plantées dans des mondes d'étalonnage, sur l'échelle de W2 graduée. Les réponses sont lues sur l'oracle : probabilité qu'une loi vraie soit promue puis survive aux tests de mort, et taux de fausses promotions. La grille est gelée, les répétitions sont dimensionnées par simulation, avec un contrôle à λ = 0. Le critère de croissance et le seuil sont préenregistrés. Elle est coûteuse, donc soumise à devis.
- (b) **Corruption.** La dose est la pression adverse ; la réponse est le taux de fausses promotions. C'est la courbe du bras d'attaque appliquée au juge, au cœur du papier C. Mais elle touche au pilier « attaque » et suit les règles du bras.
- (c) Les deux, à la suite.

La recommandation est (a) d'abord, sur cinq doses (0 ; 0,10 ; 0,25 ; 0,50 ; 1), dès que la plus petite course réelle tourne, puis (b) dans le cadre du bras. Confiance : 0,6. C'est une dépense : préenregistrement, devis, autorisation, puis le mot de Lazar. La courbe ne peut partir avant la plus petite course réelle, mais son préenregistrement peut s'écrire dès maintenant. Une course coûte 2 à 8 dollars attendus, 35 au pire. Cinq doses sur huit mondes font quarante courses, soit de l'ordre de 80 à 320 dollars attendus. Pire cas de la courbe entière : non trouvé dans le document.

## 9. Quelles sont les deux lignées appelées « organisme » ?

**L'organisme qui se conçoit lui-même** est un système de plusieurs agents qui se réécrit sur un vivier de tâches à vérité connue. Puis, son architecture figée, il répond à des questions neuves sans réentraînement. Son objectif ultime est l'universalité, mesurée sur des familles de questions jamais vues à la conception [N-044]. Ses premières versions, des essaims d'agents, ont été écrites par Gemini et courues en pilotes en octobre (24-26 octobre, plusieurs courses [GO]). Sa composition est apprise, modèle par rôle compris ; le coût entre dans le signal ; l'héritage entre générations est récompensé [N-045].

**L'organisme d'idéation**, objet du document, est le « pôle scientifique automatique » : des proposeurs écrivent des fiches, un juge statistique décide. C'est lui que visent N-058, N-059, N-064 et N-065 ; les principes de N-044 et N-045 en fixent l'objectif ultime.

Le lien exact entre les deux lignées est « à confirmer par la session mère » : le document ne l'établit pas. Il parle en outre d'un « organisme du pilier « attaque », version 1 », et du « pilier « attaque » de l'organisme ». Il ne dit pas ce qu'est ce pilier, ni s'il en existe d'autres.

## 10. Où en est l'organisme au 10 novembre 2026 ?

**Fait :**

- pilotes de l'organisme qui se conçoit lui-même (24-26 octobre) ;
- organisme du pilier « attaque », version 1, couru : 30 fiches validées, autorisation close à 8,42 dollars sur un plafond de 20 (GO-2026-11-08-08), fiches au coffre [DEC : R-1853, R-1885] ;
- attaques de Goodhart A1-v3 et A1-v4 courues et lues, verdicts officiels scellés [DEC : R-2111] ;
- épreuve W2 graduée scellée ;
- essai à blanc de la boucle complète : deux générations, fournisseurs simulés.

**En attente : la plus petite course réelle de la boucle.** La chaîne complète n'a jamais tourné avec de vrais agents. Le préenregistrement est un brouillon non scellé. Sa prédiction est de signe + : au moins une loi vraie promue puis survivante en génération 1, et aucune fausse promue en génération 1 ni 2. Le document l'appelle pourtant « préenregistrée », alors que sa légende réserve ce mot à ce qui est écrit et scellé. Une autorisation de 45 dollars court jusqu'au 30 novembre (GO-2026-11-08-02). Il manque trois choses :

- le code v65, chez un développeur neuf depuis le 8 novembre ;
- les commandes des relais des deux fournisseurs ;
- une machine jetable qui isole les épreuves, dotée du bac à sable bubblewrap.

La machine et les relais sont confiés à la session de dépôt.

**Conçu, non lancé :** le juge en tournoi façon Co-Scientist, sur un devis de 80 à 145 dollars. Le choix de son juge (Kimi, ou un modèle Claude sur crédits) est ouvert.

**Absent :** l'organisme ne figure pas dans le texte envoyé au fonds.

**Autres décisions ouvertes :**

- le rôle 3 ;
- le prix du nul v9 et la question de sens de W2, ouverts depuis le 8 novembre ;
- les régimes de budget et le code figé (étape 1 de N-044), en attente du mot de Lazar ;
- la correction de la page publique ;
- le lien entre les deux lignées.

La règle de permission de la course v2 est « accordée pour une seule commande ». Les résultats des attaques, de W2 graduée et de l'essai à blanc : non trouvé dans le document (section 9 réservée). Enfin, « Une première course faite » (page 1) ne dit pas de quelle course il s'agit.

## Les trois passages les plus obscurs

1. **Section 7**, « la structure de l'échelon 3 du bras » et « second terrain du papier C ». Il manque : ce qu'est le bras d'attaque et ce que sont ses échelons ; ce qu'est le papier C et quel est son premier terrain ; s'il existe d'autres papiers.
2. **Section 10**, « Prix du nul v9 ; question de sens de W2 » et « Règle de permission de la course v2 : accordée pour une seule commande ». Il manque : ce que sont le nul v9 et son « prix » ; si W2 désigne autre chose que l'épreuve W2 graduée, et quelle est la « question de sens » ; ce qu'est la course v2, et quelle permission est en jeu. Plus largement, il manque une clé des numéros de version (A1-v3, A1-v4, code v65, nul v9, et dans l'annexe « reprise-v9 » et « goodhart-v5 » pour le préenregistrement d'A1-v4).
3. **En-tête et sections 8 à 10**, les acteurs : « session « attaquant informé » », « session mère », « session de dépôt », « développeur neuf », « lecteur neuf d'une autre lignée que l'auditeur », Lazar. Il manque : qui ils sont (personnes ou agents) et leur rôle ; pourquoi l'auteur, dit « attaquant informé », ne lit aucun résultat d'attaque.

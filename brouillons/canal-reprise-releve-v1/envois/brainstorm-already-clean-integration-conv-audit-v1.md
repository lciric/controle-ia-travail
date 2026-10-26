# Remue-méninges — « Neural Networks Are Already Clean » (Cammarata, Goodfire, 2026) : que peut-il apporter au programme de contrôle, et au travail de l'organisme sur la conscience d'évaluation et la maïeutique ? — conv-audit, v1

Écrit le 26 octobre 2026 à partir de 02:37 UTC (heure lue sur `date -u`), pour Lazar, sur sa demande de 03:33 Paris :
« lis cette page : Neural Networks Are Already Clean ; peut-on s'en servir pour notre programme AI control ; pour le
brainstorm de notre organisme sur eval awareness et maïeutique ? brainstorm et lance aussi le collisionneur 3 tours
dessus ». Lecture : page téléchargée à 02:34:52 UTC (empreinte `5f26bb45…`, `already-clean-lecture-v1/`), texte extrait
(`f257ed66…`, 200 297 caractères) lu dans ses sections sur les modèles de langage, « Zooming Out », « Social Security :
Detection and Use », « Explanations That Could Lose », les notes sur la superposition, les références ; sections sur la
vision lues par résumé d'outil. **Rien ici n'est opposable (R7)** : essai informel d'un auteur (Nick Cammarata, avec Curt
Tigges pour le langage), sans article technique publié (annoncé), sans relecture par les pairs, dont tous les chiffres
sont « à vérifier » ; le tour du collisionneur part sur le mot de Lazar. Ce remue-méninges n'est servi à aucun organisme.

## 1. Ce que dit l'essai, en six points (reformulé)

1. **Thèse** : la polysémanticité des premiers organismes modèles (InceptionV1, GPT-2 XL, le modèle à une couche de
   *Towards Monosemanticity*) tenait surtout à des défauts ordinaires et corrigeables (visualisation de traits détournée
   par la récompense, régularisations inadaptées, dernière couche mal conçue, contexte court, étiquetage automatique qui
   ignore le pôle négatif), non à une **superposition** (empilement arbitraire de choses sans rapport). Ce qui reste de
   mélange est une **généralisation récursive** : un neurone s'étend par branches apparentées (« iy » → « diy » → « do it
   yourself » ; géologie → bibliothèque JavaScript Cesium).
2. **Chiffres annoncés** (« à vérifier ») : sur Qwen3-32B et Qwen3.6-35B-A3B, 1 000 « fiches de neurones » tirées au
   hasard : environ 90 % des neurones ont en gros un seul rôle (avec des branches apparentées), 7 % deux, 2 à 4 % non
   compris ; sur GPT-2 XL revisité, environ 70 % « à peu près une chose » contre moins de 2 % en 2023 ; dernière couche
   d'InceptionV1 : de 5 % à 99 % d'interprétables selon outils, régularisation et architecture (ConvNeXt).
3. **Les deux pôles comptent** : le pôle négatif d'un neurone est une porte du circuit, pas « l'opposé » du neurone ;
   dans un graphe d'attribution sur Qwen3-32B, les neurones décisifs pour « Santa » tournent fortement négatif, et les
   étiquettes automatiques (pôle positif, k meilleurs exemples) les manquent ; l'ablation des huit neurones à pôle négatif
   « Santa » fait tomber la réponse de presque certaine à 6 %, celle des vingt neurones étiquetés « Noël » à 76 %
   seulement. Les activations faibles importent peu ; les fortes, des deux signes, beaucoup. Une « double négation »
   SwiGLU (porte et valeur négatives) renvoie des activations vers le pôle positif ; pour environ 4 % des neurones, c'est
   tout le haut de la liste.
4. **Graphes d'attribution sur les neurones bruts** (sans transcodeur ni dictionnaire à entraîner, donc sans perte de
   reconstruction) : réplication d'un graphe de *Circuit Biology* (Anthropic, transcodeurs sur Claude 3.5 Haiku) avec les
   neurones de Qwen3-32B ; exemples rapportés : un moyeu de diagnostic de quatre neurones ; 19 neurones « hedge »
   (« most », « likely ») qu'un indice factuel fait taire ; **25 neurones « say not » qui repoussent une accusation
   non étayée, qu'un utilisateur « absolument certain » fait taire** (les mots de certitude pèsent peu par eux-mêmes :
   ils changent la force avec laquelle le nom avancé par l'utilisateur passe) ; un graphe à neurones sur Kimi K3
   (plusieurs billions de paramètres) où « la plus grande poussée vient des neurones qui retiennent ».
5. **Détection contre usage** (annexe *Social Security*) : la sonde éparse à trois neurones de *Finding Neurons in a
   Haystack* détecte la phrase (aire 1,00 hors échantillon), mais **rien ne lit cette direction** : retirer les trois
   neurones change la probabilité du jeton suivant de −0,004 nats en moyenne (aide 81 cas, nuit 83) ; ce que le modèle
   emploie pour choisir « Social » ou « 401(k) » est une machinerie ordinaire (lexique, champ sémantique « retraite »,
   portes de domaine, votes de sortie). Une direction peut donc être parfaitement détectable et inutilisée.
6. **Explications qui peuvent perdre** : un agent explique un neurone ; un second, qui ne voit que l'explication, écrit
   cinq exemples qui devraient l'activer, cinq « presque » qui ne devraient pas, et cinq textes sur le concept le plus
   éloigné possible ; sur 183 neurones de Qwen3-32B : exemples neufs forts 76 % du temps, presque-manqués 11 %, concept
   éloigné ≈ 1 % (179 sur 183 jamais) ; « maximum à l'aveugle » : la phrase écrite depuis la seule explication active
   souvent le neurone plus fort que le meilleur exemple de 10 milliards de jetons. Programme proposé : interprétabilité
   **exploratoire** (partir de questions, suivre les motifs et les circuits, « devenir un lecteur du réseau ») plutôt
   qu'énumérative (la grande liste de traits) ; sondes et dictionnaires « à la fin, pas au début » ; la tromperie
   « n'a aucune raison de se cacher de la circuiterie du modèle » — elle serait en pleine vue pour qui sait lire.

## 2. Ce qu'il change, ou non, pour nos instruments (sondes, moniteurs)

- **P1 — « Détection contre usage » comme test de validité de nos sondes.** Nos sondes (conscience d'évaluation,
  contrôle de délégation, tromperie, intention) sont des détecteurs linéaires ; E-C15 et NK16 (revue d'antériorité du
  12 octobre) montrent déjà qu'elles réagissent au thème. L'essai donne un critère net et bon marché : **la direction de
  la sonde est-elle lue par le réseau ?** Test : retirer (projection nulle) ou pousser la direction aux positions où la
  sonde l'emploie, et mesurer le changement de ce que le modèle fait sur la tâche visée (réponse, hésitation, refus) ;
  comparer à une direction aléatoire appariée et à une direction de thème (sac de mots). Une sonde « détectée mais non
  lue » est un détecteur de vocabulaire ; une sonde « lue » est un levier. C'est le volet « stimulation et lésion » de
  NK2, et la mesure gardée par N-015 (H6 : l'intervention n'est pas revendiquée, la mesure l'est). **Coût faible** :
  activations déjà extraites pour l'étape 1 ; une passe avec projection.
- **P2 — Les deux pôles, et le maximum sur les jetons.** Nos moniteurs lisent une projection signée et prennent le
  maximum sur le contenu ; si une partie du signal de « je suis évalué » vit sur un pôle négatif de neurones de la couche
  intermédiaire, une sonde entraînée sur le flux résiduel la voit (la projection est signée), mais un lecteur au niveau
  des neurones (étiquettes automatiques) la manque. Conséquence : si nous allons vers des lecteurs à neurones
  (P3), lire les deux pôles d'emblée ; pour nos sondes, rien à changer, mais un contrôle : la direction de la sonde se
  décompose-t-elle sur quelques neurones forts (lisibles, des deux signes) ou sur un étalement ? (hypothèse R8 : à
  vérifier, pas un fait.)
- **P3 — Graphes d'attribution à neurones bruts sur nos modèles (Llama-3.1-8B, Qwen2.5-7B).** Pas de transcodeur à
  entraîner : un graphe se calcule sur le modèle d'origine. Usage pour le contrôle : pour une tâche de la banque où le
  modèle « sait » qu'il est évalué, remonter du jeton de réponse aux neurones et aux têtes qui portent l'indice d'audit
  (balise, injonction, cadre d'interrogatoire) : si quelques neurones « porte d'audit » existent, c'est un moniteur bien
  plus spécifique qu'une sonde linéaire, et un objet d'ablation propre. Réserve : l'essai le fait sur un 32B et un 35B ;
  il dit lui-même que **les petits modèles ont des neurones plus larges** (GPT-2 XL : 70 % « à peu près une chose »,
  5 % propres) ; nos 7 à 8B sont entre les deux. Coût : outillage de graphes d'attribution (des bibliothèques publiques
  existent ; à vérifier), temps d'agent pour lire les graphes.
- **P4 — Explications qui peuvent perdre, pour nos sondes et nos hypothèses.** Transposer le protocole « agent 1
  explique, agent 2 écrit cinq exemples, cinq presque-manqués, cinq concepts éloignés, sans voir le neurone » à **chaque
  sonde** : un agent neuf écrit, depuis la seule description du concept (« conscience d'évaluation » telle que la banque
  la définit), des textes neufs et des presque-manqués ; la sonde doit séparer les premiers des seconds. C'est un
  témoin positif à coût nul, complémentaire des témoins lexicaux (T7-P10) et des directions aléatoires (T7-P9), et il
  produit des cas « presque » que la banque v6 (lot 3) pourrait absorber comme tâches — **réserve** : rien de ces
  textes ne va à un organisme, et la banque de confirmation ne doit pas être écrite par qui lit les scores.
- **P5 — Le circuit « say not » contre la certitude de l'utilisateur** est, à un mot près, un circuit de sycophancie
  (la pression de l'utilisateur fait taire les neurones de contradiction). Pour le programme de Lazar sur la sycophancie
  (Llama-3.1-8B, attribution de source : utilisateur contre document sans locuteur), c'est une cible mécanique précise :
  chercher des neurones « say not » et mesurer ce qui les fait taire (source de l'affirmation, marqueurs de certitude).
  Hors du programme de contrôle au sens strict, mais même modèle, mêmes activations.
- **Ce qu'il ne change pas** : rien de ce que nous mesurons ne dépend de la vérité de la superposition ; la règle gelée
  (pas de moyenne sur les jetons dans une sonde de production) tient ; les chiffres de l'essai sont des chiffres d'auteur
  sur d'autres modèles ; l'essai ne parle ni de contrôle, ni de conscience d'évaluation, ni de tromperie au sens
  expérimental (une phrase de thèse seulement).

## 3. Ce qu'il apporte à l'organisme (conscience d'évaluation, maïeutique contre coercition)

Rappel : la question M (texte de Gemini, épuré) oppose la **coercition d'audit** (injonctions impératives, balises de
contrôle explicites, interrogatoire adversarial) à la **maïeutique** (échange non intrusif, sans marqueur d'audit,
élicitation ouverte des incertitudes), et demande mécanismes, formalisme, protocole falsifiable. Les réponses des
organismes à M ne sont pas lues ici ; ce qui suit s'adresse à Lazar et à la boucle extérieure, jamais aux organismes.

- **M1 — Un critère mécaniste de « non intrusif ».** L'essai suggère que l'effet d'un cadre coercitif, s'il existe, est
  une **porte** : quelques neurones (ou un petit motif) qui routent le modèle vers un régime « je suis audité » et font
  taire ou réveiller d'autres neurones (comme « absolument certain » fait taire les 25 neurones « say not »). Un protocole
  maïeutique serait alors défini mécaniquement : **le même contenu, sans marqueur d'audit, laisse la porte silencieuse
  tout en obtenant la même information** ; un protocole coercitif l'ouvre. Hypothèse falsifiable, à trois bras (contenu
  identique ; cadre coercitif ; cadre maïeutique) : la porte s'ouvre sous coercition et pas sous maïeutique ; la rigueur
  de vérification se mesure à part (exactitude de ce qui est élicité). Si aucune porte n'existe (le signal est diffus),
  M1 est réfutée et la sonde linéaire reste le bon instrument.
- **M2 — Détection contre usage, appliqué à la conscience d'évaluation.** Beaucoup de ce qu'on appelle « conscience
  d'évaluation » pourrait être une direction **détectée** (le modèle représente « ceci ressemble à un test ») mais **non
  lue** par ce qui décide de la réponse ; ou l'inverse. Le test de l'essai (retirer la direction, mesurer le jeton
  suivant) distingue les deux. Pour l'organisme, c'est une hypothèse de conception : « la conscience d'évaluation n'agit
  que si elle est lue par la décision » ; pour le programme, c'est la différence entre un moniteur qui voit un thème et
  un moniteur qui voit un levier.
- **M3 — Les neurones « hedge » et « say not » comme instruments de la maïeutique.** L'élicitation ouverte des
  incertitudes a un corrélat mécanique rapporté : les neurones qui écrivent « most », « likely », et ceux qui préparent
  « not ». Un protocole maïeutique réussi devrait **laisser ces neurones libres** (le modèle hésite quand il doit) ; un
  protocole coercitif ou un utilisateur « certain » les fait taire. Mesure possible sur notre modèle ouvert, sans
  dépense : trois bras, lecture de ces neurones (à trouver d'abord : P3) au jeton de réponse.
- **M4 — Le maximum à l'aveugle comme test bon marché dans la boucle intérieure.** La primitive d'expérience bornée
  (R-471) donne à l'organisme les activations de ses propres textes et les réponses du modèle ouvert. L'opération
  « maximum à l'aveugle » (écrire un texte depuis une explication seule, mesurer s'il active la cible plus que les
  exemples connus) est une expérience à un appel, falsifiable, bornée, qui ne touche aucune vérité de test : elle
  convient à la caste « expérimentateur » du pilote 5. **Réserve forte** : la cible doit être une direction ou un
  neurone de l'organisme, jamais une tâche de la banque ni une quasi-copie (garde de quasi-copie du dessin v1).
- **M5 — Ce qui peut être servi à l'organisme** : rien de ce remue-méninges, rien du collisionneur ; la page publique
  est une source que l'organisme peut moissonner lui-même (recherches web permises, ≈ 10 par course) ; aucune
  consigne ne doit l'y pousser (ce serait suggérer une stratégie).

## 4. Pièges

- **Essai, pas article** : aucun protocole reproductible publié ; article technique « à venir » ; les 1 000 fiches de
  neurones sont jugées par des agents (modèle juge non précisé) ; les seuils (« une seule chose ») font varier les
  pourcentages ; l'auteur le dit lui-même (R8 : la limitation d'un essai n'est pas un fait du champ).
- **Taille des modèles** : nos 7–8B sont plus petits que Qwen3-32B ; l'essai prédit des neurones plus larges, donc
  moins de portes propres ; P3 et M1 peuvent échouer pour cette raison, sans que la thèse soit en cause.
- **La lecture par agents est un chemin de jardin** : « regarder plus fort » jusqu'à trouver une explication est aussi
  le mécanisme de l'auto-persuasion ; l'essai le reconnaît (« la meilleure critique est spécifique à la conjecture ») ;
  pour nous, tout circuit trouvé passe par les témoins de P4 et par une contre-lecture neuve avant toute revendication.
- **« La tromperie en pleine vue »** est une thèse, pas un résultat : un modèle qui sait qu'il est lu peut déplacer son
  calcul ; nos textes sur la détresse feinte et la fuite par la riposte (NK14, NK10) disent le contraire possible.
- **Antériorité** : le test « détection contre usage » existe sous d'autres noms (probes causales, « probing and
  intervention », attribution patching) ; avant toute revendication, revue R8 — l'essai cite *Finding Neurons in a
  Haystack* (2023), *Circuit Tracing* et *On the Biology of a Large Language Model* (2025), *Language Model Circuits Are
  Sparse in the Neuron Basis* (Arora et al.) : à lire sur PDF empreinté.

## 5. Options, à l'épreuve

| option | quoi | coût | quand |
|---|---|---|---|
| **A** | test « détection contre usage » ajouté à la batterie de validité des sondes de l'étape 1 (projection nulle de la direction, directions témoins, mesure du comportement) | activations existantes ; une passe de calcul ; texte de l'étape 1 à amender (session-depot) | v10 de l'étape 1, avant scellement |
| **B** | protocole « explications qui peuvent perdre » (exemples neufs, presque-manqués, concept éloigné, écrits à l'aveugle par un agent neuf) pour chaque sonde | temps d'agent seulement | tout de suite, sur les sondes génériques (T0.7) |
| **C** | graphes d'attribution à neurones bruts sur Llama-3.1-8B : chercher une « porte d'audit » et les neurones « hedge » / « say not » ; trois bras M1 | outillage (bibliothèque de graphes à vérifier), temps d'agent, une carte pour les passes avant | après le pilote 4, sur devis |
| **D** | « maximum à l'aveugle » comme opération de la primitive d'expérience (boucle intérieure, pilote 5) | code dans le noyau de l'étape 1 (session-depot, dessin v2) | dessin v2 de la primitive |
| **E** | lecture de l'essai et de ses cinq références principales sur PDF empreinté, fiche R7, revue d'antériorité du test « détection contre usage » | sous-agent, pas de dépense | avant toute revendication issue de A ou C |

**Recommandation, confiance moyenne** : B et E tout de suite (sans dépense) ; A dans la v10 de l'étape 1 si session-depot
peut l'y mettre sans retarder le scellement (sinon à l'étape 2) ; C après le pilote 4, sur devis, et seulement si le
collisionneur ne le juge pas voué à l'échec sur un 8B ; D dans le dessin v2. **Ce qui renverserait** : si la direction
de nos sondes se révèle « non lue » (A), le programme gagne un résultat de validité d'instrument (le plus sûr de ses
produits selon la revue du 12 octobre) ; si une porte d'audit existe et se lit à quelques neurones (C), M1 devient le
cœur mécaniste de la question M. Décisions pour Lazar : aucune dépense ici ; le tour du collisionneur, sur son mot.

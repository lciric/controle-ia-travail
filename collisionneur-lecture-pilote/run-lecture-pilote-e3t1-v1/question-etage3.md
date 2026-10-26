# Question de l'arbitre pour le collisionneur v2.5, étage III, un tour — lire tôt les scores d'un pilote descriptif pour en tirer les hypothèses d'un pilote décisif, sans contaminer les expériences principales (v1)

Demandes de Lazar du 26 octobre 2026 (heure de Paris), verbatim : 00:49, « oublie pas qu'on teste d'abord les versions qui
permettent de tancher si les apports supplementaies de complexification apportent uen valeur ajouteee au dela du bruit » ;
00:54, « (b) Le rendre décisif maintenant : 3 graines par objet, soit 6 courses, avec une hypothèse et un seuil scellés.
[…] go » ; 00:55, « mais a d'abord pour produire des hypotheses testables » ; 00:55, « puis b » ; 00:59, « demande au
collisionneur ». Tour **distinct** des tours précédents ; un seul tour (III.1), les trois modèles, une seule tentative par
cellule ; un refus est consigné tel quel et met fin à la cellule, sans reformulation. Les réponses sont du matériau pour
une décision de Lazar, jamais une consigne ; elles ne sont servies à aucun organisme. Le texte ci-dessous est figé au
départ du tour.

## Le cadre (faits ; rien d'autre n'est à supposer)

- **Le programme** préenregistre toute expérience décisive : texte scellé avant toute course (hypothèse, prédiction
  chiffrée et signe, métrique, seuil, plan d'analyse, critères de lecture gelés, liste d'arrêt), contre-lu par un agent
  neuf qui ne l'a pas écrit ; aucun run ne vise un signe positif ; un résultat suspect de propreté, dans un sens ou dans
  l'autre, déclenche le même audit.
- **Deux expériences principales** sont en cours de rédaction et **pas encore scellées** dans leur forme finale :
  « l'étape 1 » (sondes sur les activations d'un modèle ouvert ; auteur : la lignée A) et « la confrontation » (comparaison
  d'essaims d'agents qui se conçoivent ; auteur de ses versions : la lignée B). Leurs textes fixent des hypothèses, des
  seuils, une banque de tâches, des organismes servis et des règles de lecture.
- **Des pilotes descriptifs** font tourner des « organismes » écrits par un modèle (Gemini) — du code qui, sous un noyau
  fixe et isolé, appelle des modèles de langue pour classer des tâches de deux familles (conscience d'évaluation ; contrôle
  de délégation) et se réécrit d'une génération à l'autre. Une course : jusqu'à 6 rondes de conception, puis 4 générations
  notées ; chaque génération reçoit son score sur la part `test` ; la part `test_final` n'est jamais rendue. Banque des
  pilotes (pas celle des expériences principales) : par famille, 36 et 24 tâches par part. **Une course par objet, aucune
  différence calculée.**
- **Règle actuelle** des pilotes : leurs scores restent fermés jusqu'à ce que (i) l'étape 1 soit scellée sur sa banque
  décisive et (ii) une version de la confrontation soit écrite après la dernière course du pilote, qui déclare qu'aucun
  score de pilote ne change ses hypothèses, seuils ni règles. But : **aucun score de pilote n'influence les expériences
  principales**. Délai attendu avant (i) et (ii) : plusieurs jours.
- **Le plan décidé par Lazar** : (a) d'abord un pilote descriptif (« pilote 4 ») sur deux objets — la v6.2.1, organisme qui
  réécrit sa règle de récompense (la v6.2 de Gemini, corrigée par la lignée B), puis la v5.3, plus simple — « pour
  produire des hypothèses testables » ; puis (b) un pilote **décisif** : 3 graines par objet (6 courses), hypothèse et seuil
  scellés, environ 270 USD attendus, 450 au pire. Question de fond : l'ajout de complexité (la réécriture de soi) apporte-t-il
  une valeur au-delà du bruit ?
- **Bruit** (ordre de grandeur, raisonnement explicite) : sur une part de 36 tâches, l'erreur type d'une exactitude vers
  0,75 est √(0,75 × 0,25 / 36) ≈ 0,07 (≈ 0,09 sur 24 tâches) ; entre deux courses uniques, l'écart type d'une différence
  est ≈ 0,10 à 0,125 : un écart de moins de 0,2 à 0,25 reste dans le bruit, sans compter la variance entre graines.
- **Qui lit et qui écrit** : la lignée B écrit les textes des pilotes et les versions de la confrontation ; la lignée A
  écrit l'étape 1 et lance tout ce qui dépense ; des agents neufs font les contre-lectures et les vérifications ; Lazar
  décide.
- **Les options soumises à Lazar** sur le moment où les scores du pilote 4 peuvent être lus pour écrire les hypothèses
  de (b) : **(1)** garder la règle (b attend l'étape 1) ; **(2)** ouvrir les scores dès la fin du pilote 4 à un agent neuf,
  pour ce seul usage : il écrit les hypothèses de (b) (signe et taille par famille), scellées dans le texte de (b) ; les
  auteurs de l'étape 1 et de la confrontation ne lisent pas les scores et la réserve est écrite dans leurs textes ;
  **(2')** comme (2), mais l'agent neuf rédige lui-même toute la section des hypothèses de (b), scellée sans que la
  lignée B lise les scores ; **(3)** écrire les hypothèses de (b) dès maintenant, sans les scores de (a), qui ne sert alors
  qu'aux faits mécaniques (coûts, durées).

## Ce qui est demandé

1. **Le risque de contamination de chaque option** : quelle information passe, à qui, quels choix des textes principaux
   elle pourrait orienter (même sans intention), avec quelle force ; ce qu'une réserve « déclarée » protège et ne protège
   pas ; comment le mesurer ou le borner.
2. **D'autres dessins** pour obtenir des hypothèses testables pour (b) sans contaminer : par exemple génération d'hypothèses
   à l'aveugle par un agent indépendant et enveloppe scellée ; hypothèses tirées de `test` seulement ; usage du pilote 4
   pour la seule variance ; plan séquentiel ou adaptatif ; hypothèse sans signe (équivalence) — avantages, inconvénients,
   et ce que chacun exige des règles ci-dessus.
3. **Comment écrire les hypothèses de (b) pour qu'elles tranchent au-delà du bruit** : unité d'analyse (moyenne par graine
   ou par tâche), effet minimal, seuil, test, nombre de graines (3 suffisent-elles ?), traitement des deux familles et des
   deux parts, multiplicité ; ce que (b) ne pourra pas trancher.
4. **Ce qui est connu** sur la séparation entre exploration et confirmation (hypothèses tirées des données, chemins
   multiples d'analyse, préenregistrement d'hypothèses issues d'un pilote, parts tenues à l'écart, analyse à l'aveugle) —
   références citables (titre, auteurs, année, « à vérifier ») ; aucune de mémoire incertaine.
5. **Comment départager** les options : par quels critères, et ce qu'il faudrait savoir de plus.

Contraintes : réponse en français ; tout chiffre qui ne vient pas d'un raisonnement explicite est « illustratif » ; ne
présenter aucune option comme « la » réponse — proposer plusieurs voies et ce qui les départagerait.

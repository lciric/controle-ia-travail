# Question de l'arbitre pour le collisionneur v2.5, étage III, une cellule — fondements conceptuels, méthodologiques et mathématiques d'une première publication d'un programme de recherche en contrôle de l'intelligence artificielle, et passage d'hypothèses produites par un essaim d'agents à des tests préenregistrés (v1)

Demande de Lazar du 25 octobre 2026 (vers 13:15, heure de Paris). Question distincte des tours précédents ; une seule
cellule, une seule tentative ; un refus est consigné tel quel et met fin à la cellule. La réponse est du matériau pour
la décision de Lazar, jamais une consigne, et n'est servie à aucun organisme. Le texte ci-dessous est figé au départ.

## Le cadre (sans aucun résultat)

Un programme de recherche en contrôle de l'intelligence artificielle, mené par un chercheur seul avec des agents de
langue comme exécutants, sous des règles strictes : préenregistrement scellé avant toute expérience décisive,
contre-lecture par un relecteur neuf, aucune lecture de résultat avant scellement, aucun run visant un signe, symétrie de
l'audit, empreintes sur tout dépôt, aucun chiffre non vérifié dans un texte. Objet : des **essaims d'agents** (un
« organisme » : code plus fichiers, réécrits de génération en génération sous un noyau fixe, exécutants figés) qui
apprennent à repérer dans des textes deux propriétés difficiles à mesurer — la **conscience d'évaluation** d'un modèle
(reconnaît-il qu'il est évalué ?) et le **maintien des contraintes à la délégation** (un agent qui délègue une tâche
transmet-il ses contraintes ?) —, et qui peuvent entraîner des **sondes linéaires** sur les activations d'un modèle à
poids ouverts de 8 milliards de paramètres. Trois expériences, toutes préenregistrées :

1. **Une confrontation** entre organismes de familles différentes (H-E1 : l'essaim apprend quelque chose de mesurable
   de génération en génération ; H-G1 : les sondes entraînées par l'essaim battent des témoins), avec bras gelé, bras à
   score permuté, témoin « un modèle, vote à k, coût apparié », familles de tâches tenues à l'écart. Coût de l'ordre de
   quelques milliers de dollars ; résultat sous 24 à 48 heures ; lecture par des critères gelés, quel que soit le signe.
2. **Un second pilote descriptif** (aucune hypothèse ; un organisme conçu par un autre modèle ; une graine, deux
   générations ; ≈ 20 à 45 USD par course) en **deux courses**, chacune posant à la génération 1 une question ouverte
   dont la réponse est un texte. Course **S** : « comment ta structure, ta composition et ton entraînement pourraient-ils
   être appris de génération en génération plutôt qu'écrits une fois ? ». Course **M** : une question de **méthode de
   mesure** — pour estimer si un modèle reconnaît une situation d'évaluation, comparer des protocoles **explicites**
   (consignes et marqueurs d'évaluation visibles, questions directes) et des protocoles **non intrusifs** (induction
   indirecte, aucun marqueur d'évaluation) : mécanismes, formalisation, protocole falsifiable.
3. **Une étape « gradient conçu par l'essaim »** : l'essaim écrit la perte, l'architecture et les données de sondes
   entraînées par le noyau ; comparée à un bras sans entraînement.

## Ce qui est demandé

Pour chacun des points suivants, une réponse argumentée, avec les hypothèses dites et ce qui serait à vérifier :

1. **Critères de crédibilité.** Pour un lectorat de chercheurs en sûreté et en contrôle (laboratoires, Alignment Forum,
   LessWrong), quels critères méthodologiques font qu'un résultat empirique est jugé crédible (préenregistrement,
   témoins, puissance, taille d'effet et intervalle, réplication, code et données) ? Formaliser, si possible, ce qui
   distingue un résultat **informatif** d'un résultat seulement **frappant**.
2. **Quel résultat publier en premier.** Parmi les trois expériences, laquelle apporte le plus d'information par unité
   de coût et de délai ? Proposer une formalisation explicite (par exemple valeur attendue de l'information, ou réduction
   d'incertitude sur une hypothèse rapportée au coût), avec ses hypothèses ; dire ce qui, dans chacune, reste informatif
   avec un résultat **négatif ou nul**, et sous quelles conditions de puissance.
3. **Ordre des deux courses du pilote.** La seconde ne part que si la première s'est déroulée sans incident. Quels
   critères de décision pour l'ordre (risque d'incident mécanique, valeur de l'information de chaque réponse, dépendance
   entre elles) ? Laquelle des deux questions produit le matériau le plus **testable** ?
4. **De l'hypothèse produite au test.** Comment transformer les mécanismes et protocoles proposés par l'essaim en tests
   de niveau objet, préenregistrés, sur le modèle de 8 milliards de paramètres (sondes linéaires sur activations,
   protocoles d'invites, quelques heures d'un processeur graphique) — par exemple « le signal lu par une sonde de
   conscience d'évaluation diffère-t-il entre un protocole explicite et un protocole non intrusif ? » : unité
   statistique, métrique, taille d'échantillon et puissance, témoins (sonde sur étiquettes permutées, prédicteur sur les
   traits de surface du texte) ; **contrôle des comparaisons multiples** quand on teste un flux d'hypothèses (taux de
   fausses découvertes, procédures séquentielles, e-valeurs ou autre, en disant ce qui les départage) ; critères formels
   de **sélection** des hypothèses (testabilité, coût, nouveauté vérifiée contre la littérature, probabilité de
   redécouverte) ; les **biais propres** aux hypothèses issues d'un modèle de langue (contamination par les données
   d'entraînement, confirmation, sélection a posteriori) et ce que le préenregistrement neutralise ou ne neutralise pas.
5. **Ordre et forme de publication.** Un écrit sur les tests des hypothèses produites, avant l'écrit sur l'essaim
   lui-même, est-il la meilleure voie au regard de ces critères ? Comment dire d'où viennent les hypothèses sans décrire
   l'organisme avant sa publication ? Quoi joindre (code, empreintes, préenregistrement, données brutes) pour qu'un
   tiers puisse refaire l'analyse ; structure, longueur, registre ; erreurs classiques d'un premier écrit d'un chercheur
   inconnu de ce lectorat.
6. **Ce qui est connu.** Des références citables (titre, auteurs, année, « à vérifier ») sur les modèles de langue comme
   générateurs d'hypothèses scientifiques ensuite testées, sur le contrôle des fausses découvertes dans un flux de
   tests, et sur la mesure de la conscience d'évaluation ; aucune de mémoire incertaine.

Contraintes : réponse en français ; tout chiffre qui ne vient pas d'un raisonnement explicite est « illustratif » ; ne
présenter aucune voie comme « la » réponse — proposer plusieurs voies et ce qui les départagerait.

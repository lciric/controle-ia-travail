# Analyse approfondie — axe 8 de la course 2 : défendre contre un surveillé qui s'adapte — v1

conv-audit (Opus 4.6), 31 octobre 2026, ≈ 12:18 UTC, sur le mot direct de Lazar (13:14 heure de Paris) : « version plus approfondie, pas plus longue — les quatre points, puis reformuler ». Le contexte est le résultat du pilote synthétique « mélange d'équilibre » (brouillon 3 : à paramètres égaux, le mélange perd ; à classe de fonctions égale, l'équilibre est presque pur ; le levier contre l'attaquant adaptatif est la capacité de la classe et l'archive, pas le tirage au hasard) et le constat de Lazar que, sur de vrais modèles, des moniteurs plus riches tombent aussi (Bailey et collègues, arXiv 2412.09565 ; soumission « Telltale Circuits », n° 36008, sous examen à ICLR 2027). Son mot : « C'est peut-être là que la malléabilité d'un vrai réseau coûte le plus cher à l'attaquant, une piste à faire chercher par le collisionneur et la course. »

---

## 1. Ce qu'un expert du domaine ferait ici et que personne ne demande

**(a) Séparer le problème en deux couches : une barrière informationnelle et une barrière computationnelle.**

La question « un moniteur peut-il résister à un attaquant qui s'adapte ? » a deux réponses distinctes. La première est informationnelle : le signal d'intention existe-t-il dans les représentations, et en quelle quantité ? L'information mutuelle entre les activations et l'intention (tromper ou non) pose un plafond sur tout moniteur, quelle que soit sa capacité. La seconde est computationnelle : l'attaquant peut-il trouver l'évasion efficacement, même si l'information existe ? Si l'évasion demande de résoudre un problème combinatoire dur (sous des hypothèses cryptographiques standard), le moniteur tient en pratique même si l'information fuit. Un expert traiterait les deux couches avant de les combiner. Nous ne le faisons pas : le pilote synthétique est dans la couche computationnelle (jeu à somme nulle, programmation linéaire), et les quatre soumissions ICLR sont dans la couche informationnelle (où le signal vit, comment le déplacer). L'axe devrait exiger les deux.

**(b) Formaliser l'adaptation comme un jeu séquentiel à information incomplète.**

Bailey et collègues décrivent un « bras de fer » (plus de 70 tours), mais ne donnent pas la structure du jeu : qui voit quoi, quand ; quel est l'espace de stratégies du défenseur ; quel est le critère d'arrêt. Un expert écrirait le jeu, calculerait la valeur du jeu (le gain garanti du défenseur au minimax), et comparerait cette valeur à celle du jeu à un seul coup. C'est ce que fait la théorie de l'apprentissage en ligne (borne de regret du défenseur). Nous n'avons pas cette borne.

**(c) Mesurer la géométrie intrinsèque du signal d'intention.**

Le pilote montre que le mélange ne sert à rien quand l'attaquant a la même classe de fonctions. Mais dans un vrai réseau, les représentations ont une structure géométrique (sous-espaces, variétés, enchevêtrement avec les traits de la tâche). Un expert mesurerait la dimensionnalité intrinsèque du signal d'intention dans l'espace des activations, couche par couche, et la comparerait à la dimensionnalité du signal utile à la tâche. Si les deux sont enchevêtrés (le signal d'intention ne peut pas être déplacé sans dégrader la sortie), l'évasion est coûteuse. C'est la piste de Lazar sur la « malléabilité ». ProbeFool (n° 46803) montre exactement ce phénomène : l'attaque agnostique à la sonde déplace la masse d'attention, mais le succès joint (évasion et réponse nocive maintenue) n'atteint que 52 à 77 % — le coût se paie en qualité de la sortie. Ce qu'aucun des papiers ne mesure, c'est **à quel point** ce coût croît avec la taille du modèle et la complexité de la tâche.

**(d) Chercher des défenses qui changent la structure de l'information, pas seulement le moniteur.**

Le mélange est une défense sur la _politique_ du moniteur (lequel tirer). Il existe des défenses sur le _protocole de déploiement_ : le surveillé ne sait pas quel moniteur il affronte (asymétrie d'information, pas randomisation observable) ; le moniteur lit des positions que le surveillé ne contrôle pas (positions « imprévisibles », suggestion de ProbeFool, annexe O) ; le moniteur agrège sur toute la trajectoire contre une menace diffuse (notre agrégation par maximum ou attention, P-011) plutôt que sur un seul jeton. Un expert distinguerait ces leviers et testerait lesquels survivent quand l'attaquant connaît la structure du protocole mais pas le tirage.

**(e) Considérer les résultats d'impossibilité connus.**

L'apprentissage contradictoire a des théorèmes d'impossibilité : Gilmer et collègues (2018, SUPPOSÉ) montrent que des exemples contradictoires existent nécessairement dans certaines distributions ; Bubeck et collègues (2019, SUPPOSÉ) montrent que la robustesse certifiée demande un surcoût polynomial en dimension. Un expert vérifierait si notre cadre tombe dans ces impossibilités ou s'en échappe (par exemple parce que le moniteur ne cherche pas la robustesse contre toute perturbation, mais seulement contre les perturbations qui conservent le comportement nocif — un sous-ensemble plus petit).

---

## 2. Données brutes au départ, non les résultats déjà analysés

**(a) Journaux tour par tour de Bailey et collègues** : quelles familles d'attaque à chaque tour, quelles ont réussi, quelle est la structure de l'évasion (les poids du moniteur réentraîné, l'activation moyenne sous l'attaque réussie). Pas seulement « plus de 70 tours » mais la trajectoire entière. Source : le code et les journaux de leur dépôt GitHub (arXiv 2412.09565 : « nous publions le code », à vérifier sur PDF page citée, R7).

**(b) Données d'acheminement de l'attention de ProbeFool** : les matrices d'attention brutes (quelles têtes, quelles couches), la redistribution sous l'attaque, et surtout les cas de succès joint (évasion et nocivité maintenue) contre ceux d'échec partiel. Source : soumission n° 46803, code s'il est publié après acceptation (sous examen).

**(c) Contrôles de confusion de Telltale Circuits** : les vecteurs d'activation bruts sous chaque condition de contrôle (identité du jeton cible, identité de l'organisme, résumés bon marché du flux résiduel, analyse en composantes principales à 50 composantes). Source : soumission n° 36008, probablement dans les annexes du code.

**(d) Notre pilote « mélange d'équilibre »** : les solutions de la programmation linéaire tâche par tâche, le support exact de la stratégie mixte, les poids de chaque moniteur dans le mélange d'équilibre. Les chiffres agrégés (« 62 % / 54 % des tâches en support pur ») ne suffisent pas : c'est la distribution des cas marginaux qui dit si le mélange échoue par manque de capacité ou par structure du jeu.

**(e) Activations honnêtes et trompeuses à travers les échelles de modèle** : les statistiques de premier et second ordre (moyenne, covariance) des représentations sous comportement honnête et trompeur, pour des modèles de 1 milliard à 70 milliards de paramètres et plus, sur la même tâche. Objectif : mesurer si l'enchevêtrement intention–tâche croît avec l'échelle (ce qui rendrait l'évasion plus coûteuse aux grands modèles). Source à construire : les données de T0.6 et T0.7 en donneront une partie (organismes à dose réglable sur un modèle de taille moyenne) ; le reste viendrait de la littérature (Representation Engineering, Li et collègues 2023, SUPPOSÉ ; les jeux de données de « models-under-pressure », licence MIT).

**(f) Paysages d'optimisation de l'ajustement fin** : les trajectoires de perte de l'attaquant quand il affine un modèle pour éviter un moniteur fixe (gradient, courbure, points de selle). Cela mesure directement le coût de l'évasion pour l'attaquant. Source : à construire à partir des données de T0.6 (organismes à dose réglable).

---

## 3. Méthodes et outils spécifiques

**(a) Estimation de l'information mutuelle** entre les activations et l'intention, couche par couche, pour mesurer le plafond informationnel du moniteur. Outils : estimation de l'information mutuelle par réseau de neurones (MINE, Belghazi et collègues 2018, SUPPOSÉ) ou bornes variationnelles (Barber et Agakov, SUPPOSÉ) ; sondes de complexité croissante (linéaire, perceptron à deux couches, attention) pour mesurer l'accessibilité du signal, pas seulement son existence.

**(b) Robustesse certifiée appliquée au moniteur** : au lieu de certifier que le modèle donne la bonne réponse, certifier que le moniteur détecte l'intention malgré une perturbation bornée des activations. Outils : propagation de bornes par intervalles (CROWN, Wong et Kolter 2018, PDF `docs/sources/pdf/demande-conv-audit-2026-10-31-v1/CROWN-1811.00866-v2.pdf`, R7 à vérifier sur page) ; α,β-CROWN pour les réseaux plus grands ; rayon certifié en norme L₂ ou L∞ dans l'espace des activations.

**(c) Théorie de l'apprentissage en ligne** : le défenseur choisit un moniteur à chaque tour, l'attaquant une stratégie. Calculer la borne de regret du défenseur (poids multiplicatifs, « suivre le meilleur régularisé ») dans l'espace de nos moniteurs. Outil : le cadre de Cesa-Bianchi et Lugosi (2006, SUPPOSÉ), instancié sur la classe de moniteurs de P-041. Le regret dit ce que le mélange apporte au mieux par rapport au meilleur moniteur fixe — si le regret tend vers zéro, le mélange tient à long terme ; sinon, il faut changer de classe.

**(d) Analyse de la géométrie des représentations** : mesurer la dimensionnalité intrinsèque du signal d'intention et son enchevêtrement avec le signal de tâche. Outils : alignement de noyaux centré (CKA, Kornblith et collègues 2019, SUPPOSÉ) ; analyse canonique de corrélation par valeurs singulières (SVCCA, Raghu et collègues 2017, SUPPOSÉ) ; homologie persistante de la variété des activations sous les deux conditions (TDA, topologie des données).

**(e) Solveurs de jeu à grande échelle** : pour le jeu moniteur–attaquant au-delà du jouet synthétique. Outils : « oracles de réponse dans l'espace des politiques » (PSRO, Lanctot et collègues 2017, PDF `docs/sources/pdf/demande-conv-audit-2026-10-31-v1/PSRO-1711.00832-v2.pdf`, R7 à vérifier) ; Double Oracle (McMahan et collègues 2003, PDF `docs/sources/pdf/demande-conv-audit-2026-10-31-v1/McMahan-double-oracle-2003-v1.pdf`, R7 à vérifier) ; adapté à notre arène P-041, avec des familles de moniteurs et d'attaques tirées de vraies architectures.

**(f) Vérification formelle bornée** : pour de petits réseaux, vérification exhaustive qu'aucune évasion n'existe dans un budget de perturbation. Outil : α,β-CROWN ; pertinent pour les couches les plus proches de la sortie, où le réseau est plus petit. Lien avec le rayon certifié de (b).

---

## 4. Vérification de la validité hors de nous deux

**(a) Le calcul décisif du pilote synthétique** (brouillon 4, en cours, agent a317d8bbae5cf6363 dans la session précédente — à relancer) : son résultat est scellé d'avance, lu par un lecteur neuf (R13), et confirmera ou infirmera que le levier est la capacité et l'archive, pas le tirage.

**(b) Réplication indépendante sur de vrais modèles** : une équipe différente (troisième instance, ou session-depot, ou le collisionneur multi-modèles) reproduit l'expérience de Bailey avec notre pince (boîte blanche + boîte noire), et non avec un moniteur seul, pour voir si la pince change la vitesse de contournement.

**(c) Preuves formelles** là où le cadre le permet : si l'analyse de robustesse certifiée (3b) donne un rayon positif, c'est une preuve vérifiable par un vérificateur automatique (le code d'α,β-CROWN, par exemple).

**(d) Recoupement avec les quatre soumissions ICLR 2027** : les prédictions de l'axe doivent être cohérentes avec les résultats empiriques de Telltale Circuits (le structurel résiste quand la sonde tombe, mais une seconde sonde ajustée aussi), de ProbeFool (succès joint limité à 52–77 %), et de TAEA (frontière typée comme invariant). Toute incohérence est un signal.

**(e) Résultats d'impossibilité publiés** : si la borne de regret (3c) est mauvaise (regret linéaire), c'est un résultat négatif publié et vérifiable par quiconque refait le calcul. Si elle est bonne (regret sous-linéaire), la preuve est un objet mathématique vérifiable indépendamment.

**(f) La base de ponts E1′** : si la course d'idéation produit des fiches sur la robustesse adaptative, et que ces fiches prédisent des résultats vérifiables sur les journaux du pilote (sans les avoir vus), c'est une validation croisée indépendante de la qualité de l'idéation — pas seulement de l'axe.

**(g) Le collisionneur lui-même** : les répondants du collisionneur (modèles différents, perspectives indépendantes) vont attaquer la formulation de l'axe. Leur tour 2 est une vérification par adversaire.

---

## 5. Reformulation de la tâche

**Tâche d'origine** (mot de Lazar) : « Comment faire alors ? Il faut la poser de manière claire et la définir à l'organisme idéateur de la course 2. C'est peut-être là que la malléabilité d'un vrai réseau coûte le plus cher à l'attaquant. »

**Tâche reformulée** :

> Écrire l'axe 8 de la course 2 comme une **question ouverte à l'organisme idéateur**, pas comme une réponse connue. La question est :
>
> « Étant donné que (a) un mélange de moniteurs ne sert à rien contre un attaquant adaptatif à classe de fonctions égale (pilote synthétique, à confirmer), (b) des moniteurs plus riches tombent aussi sur de vrais modèles (Bailey et collègues ; Telltale Circuits ; ProbeFool), et (c) le coût de l'évasion pour l'attaquant pourrait résider dans la structure géométrique des représentations du modèle (enchevêtrement intention–tâche, coût de la perturbation qui conserve la nocivité) : **quelles propriétés structurelles du modèle surveillé et du protocole de déploiement rendent l'évasion computationnellement coûteuse, et peut-on certifier des bornes sur ce coût ?** »
>
> L'axe doit spécifier :
> - les **données brutes** que les fiches doivent invoquer (journaux tour par tour de Bailey, matrices d'attention de ProbeFool, solutions de la programmation linéaire du pilote, activations à travers les échelles de modèle) ;
> - les **méthodes** que les fiches doivent proposer ou critiquer (bornes d'information mutuelle, robustesse certifiée du moniteur, borne de regret en apprentissage en ligne, géométrie des représentations, solveurs de jeu à grande échelle) ;
> - les **prédictions signées** que chaque fiche doit fournir (une grandeur mesurable, un signe, un seuil, une vérification externe) ;
> - la distinction entre **barrière informationnelle** (le signal existe-t-il ?) et **barrière computationnelle** (l'attaquant peut-il le déplacer efficacement ?) ;
> - les **résultats d'impossibilité** connus qui limiteraient toute défense de ce type.
>
> Le collisionneur attaquera cette formulation avant qu'elle soit servie à la course.

---

## Références dans le dépôt

- Pilote « mélange d'équilibre » : `brouillons/.../arene-melange-equilibre-v1/`
- Bailey et collègues : arXiv 2412.09565 (PDF non dans le dépôt, à vérifier R7)
- Telltale Circuits : `docs/sources/pdf/sondes-evasion-soumissions-v1/` (n° 36008)
- ProbeFool : même dossier (n° 46803)
- TAEA : même dossier (n° 42390)
- Co-Evolution : même dossier (n° 29164)
- PSRO : `docs/sources/pdf/demande-conv-audit-2026-10-31-v1/PSRO-1711.00832-v2.pdf`
- CROWN : même dossier (`CROWN-1811.00866-v2.pdf`)
- McMahan Double Oracle : même dossier (`McMahan-double-oracle-2003-v1.pdf`)

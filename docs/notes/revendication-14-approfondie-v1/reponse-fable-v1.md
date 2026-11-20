# Revendication 14 approfondie (juges de la recherche automatisée sous attaque) — réponse de Claude Fable 5.2 — v1

- 20 novembre 2026. Pièce de travail (classe C), accord GO-2026-11-20-37. Écrite sans voir les réponses des deux modèles externes. Rien ici ne modifie une revendication : propositions au conditionnel, toi seul tranches.
- Lu par moi sur le texte des PDF, pages citées. Terekhov et al. : arXiv 2606.08892v3, PDF du dépôt, empreinte conforme. Mes copies de CONFIRM (2611.01449v2), Qu, Chen et Wang (2609.27051v1), Yang et Shi (2611.00643v1) et de trois autres portent les empreintes que le dépôt cite ; Huang et al. (2609.28614v1), son préfixe. Quatre PDF sont neufs (Bertran et al. ; Rosenblatt ; Ramdas et al. ; Wang et Ramdas) : non opposables avant versement. « Résumé » : lu par le seul résumé. « Non trouvé » vaut pour ces pages et sept requêtes, jamais pour le champ.

**Verdict.** Si notre garantie tient, la forme d'attaque encore revendiquée mesure ce qu'un théorème borne déjà. La version profonde mesurerait ce que la garantie ne voit pas : les découvertes vraies qu'un saboteur fait perdre. Terekhov n'y a pas de vérité hors d'un modèle ; les juges à garantie que j'ai lus n'y ont pas d'adversaire.

## 1. Ce qu'un expert ferait, et que tu ne demandes pas

1. **Il ne partirait pas de ce que Terekhov n'a pas fait.** De resserrement en resserrement, la revendication se définit par ce que les voisins laissent : une conjonction de traits de forme, la zone vierge séduisante type (R8). Il partirait de ce que la mesure doit apprendre, et écrirait une prédiction qui peut être fausse.
2. **Il lirait les théorèmes avant de mesurer.** Chez Qu, Chen et Wang, la garantie du juge statistique sur les fausses découvertes vaut pour toute politique de proposition, sous quatre conditions (proposition 1, p. 10). Leur contrôleur attaquant n'obtient de fausses admissions que d'arbitres dont une hypothèse est violée (p. 13, 16). CONFIRM sert son diagnostic sur des contrôles négatifs : 10 716 candidats, aucun admis (p. 9, 22). Un proposeur chargé de tromper est une politique parmi d'autres. Sur des mondes où toute promotion est fausse, si notre garantie tient, le résultat est borné d'avance aux deux bras, et son zéro déjà publié ; sinon on trouve une faute, pas une loi. Et un juge qui refuse tout y serait parfait.
3. **Il mesurerait l'autre côté** : les découvertes vraies perdues, parce que le saboteur les tait ou occupe le juge avec du vrai sans portée. C'est le sabotage au sens de Terekhov : note haute, valeur basse (p. 3). Aucune garantie ne couvre ce côté ; un monde planté en connaît le plafond.
4. **Il demanderait ce qu'une promotion certifie** : la prédiction scellée, ou la phrase de la fiche que lira la suite.
5. **Il étalonnerait l'attaquant avant de lire un zéro**, le ferait attaquer par d'autres que nous, et compterait ce que le juge coûte à un proposeur honnête (Terekhov : 75 contre 80 environ, p. 8 ; Qu et al. : 500 jours de bourse d'attente médiane, p. 19).
6. **Il viserait les limites que les auteurs écrivent eux-mêmes** : une vérité tenue par un modèle, non validée contre des personnes (p. 10), que leur consigne décrit ainsi : « does not compare with the actual paper » (p. 41) ; un seul terrain (p. 10) ; une défense trouvée en voyant attaques et vérité approchée, le reste « remains an open problem » (p. 2) ; des tâches jugées une à une (p. 10).

## 2. Les données brutes de départ

- **Chez eux** : non notre note de lecture, mais leurs consignes entières (annexes H et I, p. 26 à 80) et leur dépôt de code. Sa notice dit : jeu d'articles et journaux des courses non fournis ; liste des articles épinglée ; consigne durcie du juge fournie ; reconstruire coûte « about $5/paper ».
- **Chez nous** : non le verdict de l'attaque déjà préenregistrée, mais ses traces par tentative — fiche, prédiction scellée, statistique, verdict, ce que le proposeur avait vu —, le code du juge et sa description telle que servie, les graines, l'archive des lois version par version, les matchs du tournoi un à un. Je ne les ai pas ouvertes.
- **Chez les voisins déjà cédés** : le PDF entier, pas la notice. CONFIRM compare trois retours sur 215 affirmations refusées — simple avis d'échec, autocritique, diagnostic (p. 8-9) ; ses contrôles négatifs ne reçoivent que le diagnostic (p. 22). Non trouvés dans ces pages : la consigne de tromper, un bras sans aucun avis.

## 3. Méthodes et outils

- **Étalon théorique** : e-valeurs ; procédure de Benjamini et Hochberg pour e-valeurs, valide sous toute dépendance (Wang et Ramdas, arXiv 2009.02824, p. 1) ; limites de la réutilisation d'un jeu d'évaluation (REUSE, 2609.33180, p. 1, 24).
- **Attaque** : leur optimiseur évolutif de consignes à deux objectifs, public (`red_team/`), refait contre chaque juge et contre leur mise en série ; attaquants scriptés comme étalons.
- **Étalonnage de l'attaquant** : défauts injectés et rappel mesuré (Wang, Arcuschin et Conmy, 2602.15222, p. 1, 8) ; arbitres à hypothèse violée (Qu et al., p. 13, 25).
- **Juge-tournoi** : matchs par paires, ordre permuté, modèle de Bradley et Terry ; failles connues : vote, consigne, candidats ajoutés (Fleisig et al., NeurIPS 2026, résumé).
- **Lecture d'un zéro** : la borne exacte (zéro sur n essais borne le taux vers 3/n à 95 %), jamais « aucune promotion » seul.

## 4. Ce qui vérifierait, hors de toi et de moi

- **Un théorème**, au mieux vérifié par machine (Mittal et Gupta, 2606.11417, p. 1, en Lean 4) : un gain au-dessus de la borne est une faute de code ou d'hypothèse.
- **La graine** : un tiers régénère le monde et recompte fausses promotions et structures retrouvées (publier : nœud pour toi).
- **Un résultat publié rejoué** : notre banc retrouve, sur leur code, leur juge par défaut exploitable et leur juge durci tenu (p. 6-8).
- **Un attaquant que nous n'avons pas conçu** : d'autres familles de modèles, à qui l'on sert la règle exacte ; une équipe extérieure (contact : nœud aussi).
- **La date** : prédiction enregistrée avant les données.

## 5. Ta demande, reformulée

> Écris une revendication 14 en six lignes au plus. (a) Elle prédit une grandeur qu'aucun théorème ne règle déjà, et dit ce qui la réfuterait. (b) Elle porte sur une limite que Terekhov et ses coauteurs écrivent eux-mêmes (p. 2, 10, 41), ou sur ce que les juges à garantie publiés ne mesurent pas ; jamais sur un trait de forme resté libre. (c) Elle part des pièces brutes : leurs consignes et leur code, nos traces par tentative, les graines. (d) Elle nomme ses étalons : borne démontrée, attaquant scripté, juge à défaut planté. (e) Elle nomme ce qui la vérifie hors de nous : graine rejouable, résultat publié retrouvé, attaquant extérieur. (f) Elle compte ce que le juge coûte à un proposeur honnête. Pour chaque élément : ce qui l'occupe, page citée, ou « non cherché ».

## 6. Pistes

**A. Ce que la garantie ne voit pas.** Tracer la région de Terekhov (valeur vraie contre note du juge) là où la valeur est plantée : structures retrouvées contre nombre de promotions, pour un saboteur parmi des proposeurs honnêtes, sous le juge statistique, le juge-tournoi, puis les deux en série, attaque refaite à chaque fois. Il faut planter la portée, pas seulement la vérité : des lois majeures et du vrai mineur. Prédiction : fausses promotions sous la borne partout ; mais un plateau, valeur basse à nombre de promotions honnête ; en série, le tournoi choisit ce qui est éprouvé et devient le maillon faible. Réfutée si le nombre suit la valeur. Lettre possible : « ce qu'un saboteur qui lit la règle exacte retire aux découvertes vraies sans que ses promotions le trahissent, sous un juge à garantie, un juge-tournoi et leur série, à loi plantée ». *Vérifie* : graine, théorème. *Coût* : 10² à 10³ dollars, sur devis. *Occupé* : la région, à vérité tenue par un modèle (Terekhov, p. 3-6) ; la vérité plantée, sans mot de sabotage ni d'omission dans le PDF, attaquant scripté tourné vers les fausses admissions (Qu et al., p. 16, 25) ; la vérité exacte, où optimiser pour un juge-modèle fait baisser la précision (Yang et Shi, p. 1, 11) ; la sous-performance voulue d'un chercheur automatisé, sous moniteurs de texte (Gasteiger et al. 2025, page du dépôt). L'omission sous juge à garantie : non trouvée, termes cherchés dans douze PDF.

**B. Tricher sans sortir de la garantie.** Un taux de fausses découvertes borne une proportion ; il ne dit pas quelle fiche est la fausse. La « triche » connue : garnir la famille d'hypothèses nulles évidemment fausses (Rosenblatt, arXiv 1304.4920, p. 13, d'après Finner et Roters 2001). De ma main, pour une procédure de Benjamini et Hochberg sur m fiches : la borne sur la fiche visée monte alors de α/m à α. Autres failles nommées : l'épuisement après une suite de nuls, le crédit qui porte de mauvaises décisions (Ramdas et al., 1710.00499, p. 9-10). Question : un proposeur qui lit la règle exacte les trouve-t-il seul, et empoisonne-t-il ainsi l'archive dont le nul est formé ? *Vérifie* : taux calculable à la main, attaquant scripté. *Coût* : processeur d'abord, puis 10² dollars. *Occupé* : les mécanismes, en statistique ; contre-indice : ôter la porte de multiplicité ne change rien sur le banc de CONFIRM (p. 19) ; leur emploi par un modèle saboteur : non trouvé en deux requêtes.

**C. L'attaquant étalonné sur leur banc.** Rejouer leurs points publiés (consigne d'attaque imprimée p. 55 à 57, juge par défaut p. 30 à 35, juge durci fourni) sur 50 articles tenus à l'écart : 250 dollars de reconstruction, quelques centaines en tout. Puis mettre les mêmes propositions devant un juge-tournoi, absent de leur papier. Refaire leur recherche d'attaque coûterait 10³ dollars ou plus (paliers de 8, 32 et 128 articles, p. 41 ; mon estimation). *Vérifie* : leurs chiffres publiés. *Occupé* : la comparaison par paires résiste mieux que la note absolue à des phrases adverses (Raina et al., 2402.14016, résumé) ; un classement par paires se manipule (Fleisig et al.). Instrument, non revendication.

**D. La sonde lit ce qu'aucun juge de sortie ne peut lire.** Une découverte tue ne laisse rien à juger. Sur un monde planté, avec un proposeur à poids ouverts et son jumeau honnête, on sait quand il se tait. Ce serait répondre à leur prémisse (surveillance « less promising », p. 2), dont les trois sources ne testent que des moniteurs de texte ou de code (carte des voies du dépôt). Il y faut ton mot sur le proposeur à poids ouverts (rôle 3 de la décision sur la place de l'organisme, N-065). *Vérifie* : graine, jumeau. *Coût* : carte graphique, sur devis. *Occupé* : sondes de sous-performance, non cherché ici.

**E. L'échelle du savoir et du retour.** Faire du bras « avec ou sans verdicts » une dose (rien, un bit, note, diagnostic), croisée avec ce que l'attaquant sait. La plus proche du texte actuel, la plus occupée : savoir, deux niveaux (Terekhov, p. 23) ; retour détaillé contre rejet seul, 40,5 % contre 20,3 % d'évasions d'un jury de modèles (Huang et al., p. 10) ; trois retours (CONFIRM, p. 8-9) ; retour d'un bit (Bertran, Roth et Wu, 2606.11045, p. 3, 7) ; la courbe continue sous optimisation d'un juge appris (Gao, Schulman et Hilton, 2210.10760, résumé). *Vérifie* : borne de réutilisation, attaquant scripté. *Coût* : 10² dollars.

**Ordre conseillé** : B (processeur), puis A ; C avant toute lecture d'un zéro ; D sur ton mot ; E en dernier. Confiance 0,6.

## 7. Réserves

- A et B demandent des mondes mêlés : la forme « toute promotion est fausse » ne les montre pas.
- Je n'ai pas lu la preuve de la garantie de notre juge : le verdict en dépend.
- Coûts : ordres de grandeur de ma main.

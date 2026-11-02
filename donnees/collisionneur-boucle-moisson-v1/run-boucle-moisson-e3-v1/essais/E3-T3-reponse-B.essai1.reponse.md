# Proposition B — Tour III.3 : réponse aux critiques

---

## (a) Traitement critique par critique

Je traite chaque critique adressée à B par les propositions A, C et D. Je ne fusionne ni ne lisse les critiques entre elles ; je les prends une par une.

---

### Critiques de A sur B

**A.1 — « Exp. 1 vrai par construction : 20 résumés suffisent presque sûrement. »**

**Acceptée en partie, transformée en test.** A a raison que 20 résumés par fiche dans un domaine pertinent contiennent presque sûrement *quelque chose* d'absent de la fiche. Le témoin « requêtes au hasard dans le vocabulaire » est trop faible. Je remplace le contrôle négatif d'Exp. 1 : voir Exp. 1 corrigée ci-dessous. Cependant, A affirme aussi que le témoin c1 (« 5 premiers mots du titre ») serait meilleur — c'est un raccourci : c1 et Exp. 1 mesurent deux choses différentes (c1 mesure le rappel d'antériorités connues ; Exp. 1 mesure l'apport d'information nouvelle). Le vrai témoin manquant est celui que A nomme en (c) : requêtes construites à partir des seules antériorités déjà citées. J'adopte ce témoin.

**A.2 — « Exp. 1 — lecteur confondu : Opus 5.5 est juge de la course 2. »**

**Acceptée.** C'est une fuite d'instrument. Correction : le lecteur neuf d'Exp. 1 est un modèle qui n'est ni proposeur, ni juge, ni aiguilleur dans la course 2. Candidats : Fable 5.1 (retiré du rôle de proposeur en course 2, mais utilisé en antériorité — acceptable si le lecteur est isolé et n'a pas accès aux verdicts), ou un modèle extérieur au tableau § 1.3. Je fixe : Fable 5.1, instance isolée, sans accès aux fiches de course 2 ni aux verdicts.

**A.3 — « c1 récompense retrouver les antériorités déclarées ; Exp. 1 pénalise ramener ce que la fiche cite. Contradiction. »**

**Acceptée.** La contradiction est réelle : c1 tel que rédigé calibre le moissonneur sur un objectif (rappel de références connues) qui n'est pas celui de la boucle (apporter de l'information nouvelle). Correction : c1 est réécrit. Le moissonneur doit retrouver non pas les antériorités déclarées, mais des œuvres *que la fiche ne cite pas* et qui sont jugées pertinentes par un lecteur aveugle. Le test de rappel d'antériorités connues devient un contrôle secondaire de cohérence (le moissonneur ne doit pas être *pire* qu'une recherche par antériorités citées), pas la métrique principale.

A note aussi que les fiches de la course 1 sont sous `donnees/`, non lisibles par conv-audit. C'est un fait (§ 10, VÉRIFIÉ). L'expérience requiert un accès par session-depot ou un GO explicite de Lazar.

**A.4 — « Exp. 2 — métrique monotone. »**

**Acceptée.** Un modèle qui ne supprime jamais et copie une référence de la moisson atteint « progrès » dans ~100 % des cas. La métrique est morte. Correction : voir Exp. 2 corrigée. Le progrès doit être mesuré par un critère qui pénalise les ajouts non pertinents et qui peut régresser.

**A.5 — « Exp. 3 — témoin hors domaine, Jaccard sur résumés absents. »**

**Acceptée.** La moisson OpenAlex (197 681 œuvres) ne contient pas de résumés (§ 4.1 de la pièce 3, VÉRIFIÉ) ; le bras basique adapté au format fiche–article ne peut pas calculer un Jaccard de concepts sur des résumés absents. De plus, les paires au hasard dans un vivier hors domaine échouent à l'étage 1 par format, pas par infertilité. Correction : voir Exp. 3 corrigée.

**A.6 — « Exp. 4 — seuil absolu, 'dents' mécaniques. »**

**Acceptée en partie.** A a raison que le seuil absolu (+5 points) bascule avec le taux de base (pièce 2, réserve 3, RAPPORTÉ). Cependant, le but d'Exp. 4 n'est pas de valider une méthode de prédiction de liens mais de savoir si le *terrain* (contrôle de l'IA) permet une rétrodiction lexicale discriminante. L'absence d'appariement degré/âge est un vrai défaut. Correction : seuil relatif, appariement degré/âge, fenêtre placebo.

**A.7 — « Exp. 5 — biais d'estimateur par effectif décroissant. »**

**Acceptée.** Le calcul d'A est correct : avec K = 50 étiquettes et n passant de 128 à 30, le biais de Miller-Madow produit à lui seul ~22 % de baisse apparente, atteignant le seuil de 20 % sans convergence réelle. Correction : voir Exp. 5 corrigée.

**A.8 — « c2 — planteur non aveugle. »**

**Acceptée.** Si les paires « fertiles » sont construites par quelqu'un qui connaît la formule du bras, la détection est tautologique. Correction : le planteur est aveugle à la formule du bras ; les paires fertiles sont définies par un lecteur qui ne connaît que les résumés, pas les scores.

**A.9 — Contrôles négatifs absents.**

J'adopte les six contrôles nommés par A en (c), intégrés dans les expériences corrigées ci-dessous.

---

### Critiques de C sur B

**C.1 — « Exp. 2 vrai par construction : tous les champs sont remplis dès la passe 1, donc Δ_champs = 0. »**

**Acceptée.** La garde de forme impose que tous les champs soient remplis (§ 1.2 point 4, § 3.2, VÉRIFIÉ). Δ_champs est donc toujours 0 pour une fiche valide. C a aussi raison que compter les antériorités sans pénaliser leur fausseté rend le progrès vrai par construction. Même conclusion qu'A.4 : la métrique est morte. Voir Exp. 2 corrigée.

**C.2 — « Exp. 1 — fuite d'étiquette, aveugle brisé. »**

**Acceptée.** Si le lecteur voit les requêtes qui ont produit les résumés, il sait quel bras est ciblé. Correction : le lecteur reçoit les résumés moissonnés mélangés (ciblés et témoins) sans indication de leur provenance. L'évaluation est en aveugle.

**C.3 — « Exp. 5 — confondants : taille du support, bruit vs convergence, permutations périodiques. »**

**Acceptée.** C ajoute aux défauts signalés par A un point important : une entropie marginale ne détecte pas les cycles. Un système qui alterne entre deux états à haute entropie « tourne en rond » sans que le ratio baisse. Voir Exp. 5 corrigée.

**C.4 — « c3 — incompatibilité d'instrument : la signature brute est un vecteur de prédictions sur des épisodes, pas sur du texte. »**

**Acceptée.** C'est un défaut grave. La signature brute de la mémoire (pièce 4a) est définie pour des lois mathématiques exécutables sur une sonde fixe. Les fiches de course sont du texte sans traduction en loi testable (§ 1.1 : « prise idéation conçue, pas construite », VÉRIFIÉ). L'instrument c3 ne peut pas prendre en entrée les fiches de la course 1. Correction : c3 est restreint au cadre où la prise idéation existe, c'est-à-dire reporté. Pour le pré-pilote et la course 2, la mémoire anti-redite repose sur le Jaccard textuel (qui a des dents sur paraphrases, copies, jargon rare — pièce 4a — mais pas sur les variantes quantitatives). Je déclare cette limitation.

**C.5 — « Exp. 4 — tautologie du seuil absolu. »**

Même critique qu'A.6. Déjà acceptée.

**C.6 — Contrôles négatifs absents (C nomme 3 contrôles).**

- Exp. 1 : « recherche par les seules antériorités citées » — identique à A, adopté.
- Exp. 2 : « script d'ajout aléatoire » — adopté comme témoin mécanique.
- Exp. 3 : « ablation de la fiche (article seul → fiche) » — adopté.

---

### Critiques de D sur B

**D.1 — « Les règles de décision ne sont plus exclusives après ajout des marges. »**

**Acceptée.** La zone entre les seuils de H_A et H_B est un no man's land où le test est non concluant. Ce n'est pas un défaut de conception mais un fait probabiliste ; il doit être déclaré. Correction : chaque expérience a trois issues : H_A retenue, H_B retenue, non concluant (zone tampon). B4 (inférence forte) exige que chaque issue falsifie quelque chose. « Non concluant » falsifie la puissance du design, pas une hypothèse substantive. Je le déclare.

**D.2 — « Exp. 1 confond volume, ciblage et réécriture. »**

Même substance qu'A.1 et C.2. Déjà acceptée.

**D.3 — « Exp. 2 récompense l'addition, pas le progrès. »**

Même substance qu'A.4 et C.1. Déjà acceptée.

**D.4 — « Exp. 3 mesure une préférence de juges, non la fertilité. »**

**Acceptée en partie.** D a raison que « notable » selon les juges-modèles n'est pas « fertile au sens de survie ou descendance ». Cependant, dans l'état actuel (tests de mort non activés, prise idéation non construite), la survie n'est pas observable. Je déclare la limitation et propose un test conditionnel : si/quand les tests de mort sont activés, Exp. 3 est refaite avec la survie comme issue.

**D.5 — « Exp. 4 teste un signal lexical, pas la validité pour des idées de méthode. »**

**Acceptée.** Exp. 4 ne peut pas prouver que la rétrodiction lexicale vaut pour des idées de méthode. Elle peut seulement montrer que le terrain a ou n'a pas de signal lexical. C'est une condition nécessaire, pas suffisante. Je déclare la limitation.

**D.6 — « Exp. 5 assimile concentration et stérilité. »**

Même substance qu'A.7 et C.3. Déjà acceptée.

**D.7 — « c1–c5 : circularités multiples. »**

Partiellement couvert par les critiques précédentes (c2 planteur, c3 incompatibilité, c5 effectif). J'ajoute : pour c5, l'accord humain/machine vérifie la plomberie, pas la justesse du script. Correction : c5 inclut un script volontairement erroné (boucle infinie, résultat faux, résultat absent) pour vérifier que le bac échoue correctement.

**D.8 — Contrôles négatifs : moisson croisée, augmentations dégradées, placebo degré–âge, copies exactes.**

Adoptés dans les expériences corrigées.

---

## (b) Expériences corrigées

### Exp. 1 corrigée — La moisson ciblée apporte-t-elle plus qu'une recherche par co-citation ?

**H_A** : Les résumés ramenés par des requêtes dérivées des *concepts et trous* de la fiche contiennent au moins un élément nouveau pertinent (jugé par un lecteur aveugle) dans ≥ 50 % des fiches, *et* ce taux dépasse celui du témoin de ≥ 15 points.

**H_B** : Le taux ciblé est < 50 %, ou l'écart avec le témoin est < 15 points.

- **Témoin principal** (remplace le « hasard dans le vocabulaire ») : requêtes construites à partir des *identifiants des antériorités citées* par la fiche (co-citation directe), mêmes API, mêmes quotas.
- **Témoin secondaire** : 5 premiers mots du titre (recherche par mots-clés bruts).
- **Aveugle** : le lecteur (Fable 5.1, instance isolée, pas juge ni proposeur en course 2) reçoit les résumés mélangés sans indication du bras. Il juge chaque résumé indépendamment comme « contient un élément pertinent absent de la fiche » ou « non ».
- **Contrôle de ε** : 5 fiches reçoivent les résumés d'une *autre* fiche (appariement croisé) ; le taux de « pertinent » sur ces paires mesure le bruit de fond du lecteur.
- **Matériau** : 20 fiches de la course 1 (accès par session-depot, GO de Lazar requis).
- **Falsification** : H_A → taux < 50 % ou écart < 15 points. H_B → taux ≥ 50 % et écart ≥ 15 points avec ε < 0,30.

### Exp. 2 corrigée — L'affinement itératif produit-il un progrès vérifiable ?

**Définition du progrès** (remplace le comptage monotone) : Après k = 3 tours, un évaluateur aveugle reçoit v_initiale et v_finale en ordre aléatoire et juge, sur chaque champ : (i) plus précis / même / moins précis ; (ii) cohérent avec les autres champs / incohérent. Le progrès est défini par : au moins un champ plus précis, aucun champ incohérent ajouté, aucun champ moins précis.

**H_A** : Taux de progrès ≥ 0,50 et supérieur de ≥ 15 points au contrôle.

**H_B** : Taux < 0,50 ou écart < 15 points.

- **Contrôle 1** (remplace « réécriture sans moisson ») : le proposeur réécrit 3 fois *avec une moisson croisée* (résumés d'une autre fiche, appariement aléatoire).
- **Contrôle 2** (ajouté, adopté de C) : un script ajoute mécaniquement une référence tirée au hasard dans OpenAlex et une prédiction factice. Si ce script atteint ≥ 0,30 de « progrès » selon l'évaluateur, la métrique est morte et l'expérience est arrêtée.
- **Évaluateur** : modèle distinct du proposeur et du lecteur d'Exp. 1, aveugle au bras.

### Exp. 3 corrigée — L'appariement fiche–article est-il plus fertile que le hasard apparié ?

**Changements** :
- Le vivier d'articles est une moisson *fraîche* avec résumés (arXiv + OpenAlex, métadonnées et résumés, décision en vigueur § 2), pas la moisson en vrac sans résumés.
- Le témoin est apparié sur l'axe et le sous-domaine (même distribution d'axes que les paires sélectionnées).
- **Contrôle d'ablation** (adopté de C) : Kimi écrit une fiche à partir du seul résumé de l'article (sans la fiche appariée). Si ce bras obtient autant de « notables », l'appariement bisociatif est illusoire.
- L'adaptation du Jaccard est fixée sur un lot de calibration disjoint du lot d'épreuve.
- **Déclaration** : avec 24 fusions par bras, la puissance est ~0,25 pour un effet de 10 points (calcul de C, accepté). Le test peut être non concluant. Si non concluant, le résultat est « effectif insuffisant », pas « H_B retenue ».

### Exp. 4 corrigée — Rétrodiction lexicale dans le domaine contrôle de l'IA

**Changements** :
- **Seuil relatif** (remplace le seuil absolu) : la meilleure méthode de voisinage doit multiplier le taux de base par ≥ 10 (ratio, pas différence absolue).
- **Appariement degré/âge** : chaque paire positive est appariée à k paires négatives dans la même case (degré, âge), comme proposé dans la pièce 3 § 4.4. Les métriques sont rapportées sur l'échantillon apparié *et* sur l'échantillon brut.
- **Fenêtre placebo** : 2019→2021, coupure fin 2018 ; même chaîne. Si les deux fenêtres donnent des verdicts opposés, le seuil est fragile et le test est non concluant.
- **Fuite** : aucun modèle de langage dans le prédicteur (méthodes de graphe uniquement). Déclaré.
- **Limitation déclarée** : Exp. 4 teste le signal lexical, pas la validité pour des idées de méthode.

### Exp. 5 corrigée — La boucle tourne-t-elle en rond ?

**Changements** :
- **Entropie à effectif constant** : à chaque tour, sous-échantillonnage de n = min(n_1, …, n_5) fiches actives. L'entropie est calculée sur le sous-échantillon. Cela élimine le biais de Miller-Madow lié à la décroissance de n_t.
- **Mesure complémentaire** : taux de paires de fiches dont le Jaccard de concepts dépasse 0,8 (proxy de redite). Si ce taux augmente de ≥ 50 % entre le tour 1 et le tour 5, la boucle converge.
- **Contrôle 1** : tours permutés (les fiches du tour 3 sont mélangées avec celles du tour 1, même calcul). Si la permutation donne le même ratio, la métrique ne mesure pas la dynamique.
- **Contrôle 2** : boucle de copies exactes (les fiches ne changent pas entre tours). Le ratio doit être ~1,0 ; sinon l'estimateur est biaisé.
- **Contrôle 3** : boucle à synonymes gonflés (chaque tour ajoute des synonymes aléatoires). L'entropie doit augmenter ; si elle baisse, l'estimateur est défectueux.

---

### Calibrations corrigées

**c1 corrigé** : La métrique principale est le taux d'œuvres *non citées par la fiche* jugées pertinentes par un lecteur aveugle. Le rappel d'antériorités connues est un contrôle secondaire (masquage d'une antériorité, mesure du rappel, adopté de A).

**c2 corrigé** : Le planteur est aveugle à la formule du bras. Les paires fertiles sont identifiées par un lecteur qui ne voit que les résumés.

**c3** : Reporté jusqu'à la construction de la prise idéation. Pour la course 2, la mémoire anti-redite repose sur le Jaccard textuel (limitation déclarée : ne détecte pas les variantes quantitatives).

**c5 corrigé** : Inclut 3 scripts défectueux (boucle infinie, RESULTAT: absent, valeur fausse). Effectif porté à 10+10 si le budget le permet (GO de Lazar). La borne inférieure de Clopper-Pearson à n = 5 est 0,28 (calcul de C, accepté) ; à n = 10, elle monte à 0,44 pour 8/10 — toujours faible, mais déclaré.

---

## (c) Réponse à la question de l'arbitre

### Ce qui est établi

1. **Le moissonneur est codé mais n'a jamais servi en conditions réelles.** VÉRIFIÉ (§ 2). Aucun fait ne montre qu'une moisson ciblée apporte quelque chose à une fiche. La boucle moisson ↔ fiches repose donc entièrement sur une HYPOTHÈSE non testée.

2. **Les trois bras du bisociateur sont conçus pour des paires fiche–fiche, pas fiche–article.** VÉRIFIÉ (§ 7). Le bras basique a un verdict « non concluant » sur mondes inventés (§ 7.1). Le vocabulaire de Gu-Krenn ne couvre pas le contrôle de l'IA (pièce 3, § 5, VÉRIFIÉ). Apparier fiches et articles exige une adaptation non triviale dont aucune mesure n'existe.

3. **La mémoire aide si et seulement si les vraies associations se regroupent.** OBSERVÉ-NON-AUDITÉ (pièces 4a, 4b). La condition « regroupement dans le monde réel » n'est pas vérifiée.

4. **Les tests de mort sont codés, jamais activés.** VÉRIFIÉ (§ 9.2). La couche 1 réelle a « pas de dents » (0/20, § 9.4.A.3). Aucune fiche de course n'est devenue une hypothèse testée (§ 10).

5. **La prise idéation (fiche → loi testable) n'est pas construite.** VÉRIFIÉ (§ 1.1). Sans elle, la chaîne course → pôle est coupée.

6. **La rétrodiction de Swanson montre que la cooccurrence lexicale future ≠ découverte féconde.** RAPPORTÉ (pièce 2 : « L'issue mesurée est la cooccurrence lexicale future, pas une découverte féconde »).

### Ce qui n'est pas établi

- Que la moisson ciblée apporte de l'information utile à une fiche (HYPOTHÈSE).
- Que l'affinement itératif produit un progrès mesurable et non une reformulation (HYPOTHÈSE).
- Que l'appariement fiche–article est faisable et fertile avec les bras existants (HYPOTHÈSE).
- Que la rétrodiction lexicale fonctionne dans le domaine du contrôle de l'IA (HYPOTHÈSE).
- Que la boucle ne tourne pas en rond (HYPOTHÈSE).
- Que le gain de nouveauté est mesurable (HYPOTHÈSE — aucune métrique définie).

### L'expérience à faire en premier

**Exp. 4 corrigée (rétrodiction lexicale dans le domaine contrôle de l'IA).**

Raison : c'est le test le moins cher (~0 $, processeur existant, si le corpus ≤ 1M documents) qui falsifie le plus de présupposés. Si H_B est retenue (taux de base trop faible ou signal lexical absent), alors :
- La composante rétrodiction de la boucle est invalide pour ce domaine.
- L'évaluation préenregistrée par rétrodiction (point (f) de la demande de Lazar) n'a pas de fondement.
- Le substitut Gu-Krenn dans le domaine IA n'a pas de terrain.

Si H_A est retenue, on passe à Exp. 1 corrigée (moisson ciblée utile ?), qui coûte ~5 $ et falsifie la raison d'être de la boucle elle-même. La course 2 procède en parallèle, sans la boucle, comme prévu dans le pré-pilote.

FIN-DE-CELLULE
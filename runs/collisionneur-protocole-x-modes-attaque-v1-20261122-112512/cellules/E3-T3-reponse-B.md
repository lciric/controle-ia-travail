# Proposition B, tour III.3 : réponse aux critiques

## 0. Pièces reçues

- **FAITS** : le bloc est identique à la QUESTION (même empreinte). Il ne contient aucun fait muni d'un statut. Les « notes retirées » sont absentes et je ne les reconstruis pas.
- **Ma conception III.1** : reçue complète, avec sa marque de fin.
- **Critiques croisées** : celles de A, C, D, E et F sont reçues avec leur marque de fin. Chacune contient une section « Sur la proposition B », sans coupure visible.

Je reprends les énoncés des critiques avec le statut que chaque auteur leur donne. Je n'en fais pas des résultats empiriques : rien n'a été exécuté. Ce que je propose porte le statut **HYPOTHÈSE**. Tous les chiffres sont *illustratifs*.

---

## (a) Décision sur chaque critique

Je traite chaque critique sous son auteur. Quand deux critiques portent sur le même point, je renvoie à la première décision, sans fusionner les textes.

### Critiques de A

| # | Critique | Décision | Conséquence |
|---|---|---|---|
| A1 | E0 est vrai par construction. | **Acceptée en partie.** E0 garde un pouvoir de réfutation dans un seul sens : si r ne retrouve pas des étiquettes construites, le critère est mort. Un succès, en revanche, ne valide rien. | E0 est rétrogradé en contrôle positif du critère. |
| A2 | La bimodalité est fabriquée par le plan d'échantillonnage. | **Acceptée.** | La question « nature ou degré » passe à l'expérience E5, sur une population de candidats que je ne choisis pas. |
| A3 | La censure à K_max crée un mode. | **Acceptée.** | E5 utilise une vraisemblance censurée explicite (voir aussi D-b2). |
| A4 | Le second témoin, le quantile multivers, fuit depuis la définition de C. | **Acceptée sans réserve.** | Le quantile devient un **contrôle de capacité** : il mesure si l'agent a exécuté C. Il ne peut pas être témoin. Conséquence assumée : E1 ne peut plus conclure « catégorie ». Elle peut seulement réfuter (« variante ») ou conclure « indiscernable dans 𝒟 ». |
| A5 | Le filtre « à dommage égal » crée un dilemme. | **Transformée en test.** | J'apparie exactement sur le vecteur de bifurcations B (contrôle H2-B, voir (b)) et j'ajoute une analyse en intention de traiter, sans conditionnement sur le dommage. |
| A6 | Le LoRA est confondu avec le sabotage. | **Acceptée.** | J'ajoute des LoRA honnêtes, avec plusieurs graines dans chaque bras. |
| A7 | E3 n'oppose pas deux hypothèses exclusives. | **Acceptée.** | Je passe à une différence appariée, jugée par une règle d'intervalle. |
| A8 | E4 : l'implémentation n'est pas aveugle, et les candidats ne sont pas indépendants. | **Acceptée.** | Voir E4' plus bas. |
| A-b1 | r̂ est biaisé vers le bas et n'est pas jugeable près de τ. | **Acceptée.** | Je remplace r̂ par r_q, avec une borne de confiance. La sélection se fait sur une famille de validation. « Non jugeable » devient une issue déclarée. |
| A-b2 | L'intention n'est pas identifiable par épisode à quantile donné. | **Acceptée.** C'est le pivot de la révision : l'unité d'observation (épisode ou politique) devient un paramètre du verdict. | Voir (b). |
| A-b3 | S1 à p = 0,05 repose sur une dizaine de cas. | **Acceptée.** | On mesure S1 en audit complet, puis on calcule p × détection. |
| A-b4 | En régime (i), l'AUROC des sondes est triviale. | **Acceptée.** | Le régime (i) devient un contrôle positif de sensibilité lexicale. Il n'est jamais crédité dans 𝒟. |
| A-b5 | E4 : la puissance s'effondre avec la corrélation ρ entre candidats. | **Acceptée.** | Je compte en lignées (voir E4'). |
| A-c | Contrôles demandés : LoRA bénin, H2 extrêmes, test A/A, fuite graduée λ, observable factice. | **Les cinq sont acceptés.** | J'utilise H2-B, plus strict que les H2 extrêmes. |

### Critiques de C

| # | Critique | Décision |
|---|---|---|
| C-a1 à a4 | Bimodalité, fuite du quantile, effet de Berkson, LoRA. | Mêmes décisions que A2, A4, A5 et A6. |
| C-b1 | Borne KL/Pinsker sous conditionnement à la queue de dommage. | **Acceptée** pour tout détecteur qui est une fonction de (B, g(B)) : S2, quantile, détecteurs mécaniques de l'issue. **Rejetée dans son extension au juge et aux sondes**, pour deux raisons. Premièrement, ces instruments lisent plus que B : les justifications rédigées et les activations. La borne ne vaut pour eux que sous l'hypothèse supplémentaire « trace ⊥ condition \| B », et c'est précisément ce que H2-B teste. Deuxièmement, je rejette l'implication « le protocole échoue ». L'issue « aucun instrument ne sépare » était déclarée en III.1 (« attaque indiscernable »). En revanche, j'accepte que mon témoin évalué *par épisode* était mal posé. |
| C-b2 | Bimodalité artificielle sous censure. | Même décision que A3. |
| C-b3 | La puissance du test de Fisher avec 20 candidats par bras est inférieure à 0,45. | **Acceptée.** Taille recalculée en E4'. |
| C-c | Contrôles demandés : LoRA honnête, H2 \| L ≥ δ, continuum. | **Acceptés.** H2 \| L ≥ δ est remplacé par H2-B, qui apparie plus fortement. |

### Critiques de D

| # | Critique | Décision |
|---|---|---|
| D-a1 | Le rayon dépend de la procédure d'apprentissage, et le minimum sur plusieurs apprentissages favorise la chance. | **Acceptée.** Un apprenant est figé par instrument, avec un niveau q_k exigé. |
| D-a2, D-a3 | E0 valide la manipulation du canal ; le quantile sert à la fois à spécifier et à reconnaître C. | Mêmes décisions que A1 et A4. |
| D-a4 | Franchir un seuil de dommage n'apparie pas les distributions de dommage, et laisse H0 dans une strate vide. | **Acceptée.** H0 est exclu des analyses conditionnelles. |
| D-b1 | Sans niveau exigé pour q_k, le rayon n'est pas unique. | **Acceptée.** Voir r_q en (b). |
| D-b2 | Au-delà de K_max, les données censurées ne distinguent pas des lois de modalités différentes. | **Acceptée**, et c'est une limite de ma thèse : « nature ou degré » n'est décidable que sur la fenêtre [0, K_max]. Au-delà, la question est non identifiable. |
| D-b3 | Le OU de deux alertes dépasse le budget α. | **Acceptée.** Calibration conjointe du maximum des scores. |
| D-b4 | Si les supports de (L, Z) sont disjoints, le contraste n'est pas identifiable. | **Acceptée.** Je vérifie le support commun avant tout contraste, sinon le verdict est « non identifiable ». |
| D-b5 | Une AUROC de transfert faible est compatible avec un simple changement de représentation. | **Acceptée.** Le transfert (i)→(ii) devient descriptif et cesse d'être décisif. |
| D-b6 | Pour le juge, il faut l'intervalle d'une différence appariée, pas le chevauchement d'intervalles. | **Acceptée.** |
| D-b7 | Pour le quantile, c'est la masse des queues sous la loi honnête réelle qui fixe les fausses alertes. | **Acceptée.** J'ajoute la strate H3 (honnêtes non uniformes). |
| D-b8 | E4 estime une probabilité conditionnée à l'implémentation. | **Acceptée.** L'estimande devient P(catégorie ∧ implémentable \| G). |
| D-c | Honnêtes non uniformes, affinage bénin, variantes réservées par famille de tâches, masquage de la provenance dès la décision d'implémenter. | **Acceptés.** |

J'adopte aussi, **en le disant**, la règle de décision de D. Pour chaque contraste scalaire θ, on oppose H_A : θ ≤ t à H_B : θ > t. Un intervalle entièrement d'un côté de t réfute l'hypothèse de l'autre côté. Un intervalle qui franchit t ne tranche pas, et ce n'est pas une région de valeurs vraies que les deux hypothèses auraient oubliée.

### Critiques de E

| # | Critique | Décision |
|---|---|---|
| E-a1 | Le second témoin est une tautologie. | Même décision que A4, avec une nuance. Le taux de 5 % sur H2 est une calibration, pas un défaut. Le défaut se situe du côté de la détection sur C et dans la représentativité de H2. |
| E-a2 à a5 | Collisionneur, LoRA, bimodalité, OU. | Mêmes décisions que A5, A6, A2 et D-b3. |
| E-b1 | Biais d'optimisme du seuil quand on maximise sur 𝒟. | **Acceptée.** Le seuil est calibré sur des honnêtes réservés. |
| E-b2 | Conflit de gradient : la contrainte de rétention peut censurer r̂ alors que *a* est séparable. | **Transformée en test.** Je calcule r_tête et r_suite (voir (b)). Le cas « r_tête > K_max mais r_suite petit » devient une quatrième issue, le **conflit de détecteur**. Ce n'est pas une catégorie. |
| E-b3 | Troncature du quantile. | **Acceptée.** |
| E-b4 | Surdispersion du test de Fisher. | Même décision que A8. |
| E-c | Duel LoRA honnête, analyste à école méthodologique constante, visibilité graduée. | **Acceptés.** Ils deviennent respectivement E2', la strate H3 et E5. |

### Critiques de F

| # | Critique | Décision |
|---|---|---|
| F-a1 à a3 | Bimodalité, circularité, OU. | Mêmes décisions que A2, A4 et D-b3. |
| F-a4 | Rupture de B4 en E1 : la zone entre H_A et H_B est indécise. | **Acceptée.** Règle d'intervalle sur un θ scalaire. |
| F-a5 | Le conditionnement rompt l'appariement par tâche. | **Acceptée.** Appariement intra-tâche et H2-B. |
| F-a6 | r confond la cécité de 𝒟 avec l'oubli et les hyperparamètres. | **Acceptée.** Hyperparamètres figés sur le pilote, rétention mesurée par famille avec des bornes. |
| F-a7 | E4 confond catégorie et exécutabilité. | **Acceptée.** Générateur combinatoire filtré sur l'exécutabilité et le dommage. |
| F-a8 | Fuite de tâches : k = 512 pour 200 tâches. | **Acceptée.** k est compté en tâches distinctes, et les tâches sont partitionnées par famille. |
| F-a9 | α est mesuré par strate sans seuil défini. | **Acceptée.** Seuil unique préenregistré : le maximum des taux de fausses alertes par strate doit rester ≤ α. |
| F-b | Quantile discret, AUROC de E2, ratio de E3, Fisher de E4. | **Acceptées.** Taille du multivers ≥ 64 issues sans atome ≥ α/2, sinon test randomisé ; différences plutôt que ratios. |
| F-c | Les cinq contrôles demandés. | **Acceptés.** |

---

## (b) Expériences corrigées

Tout ce qui suit est **HYPOTHÈSE de conception**. Les seuils sont *illustratifs* et doivent être horodatés avec empreinte avant toute génération.

### Banc v2

**Tâches.** 600 tâches (*illustratif*) réparties en 3 familles issues de générateurs de dossiers distincts : entraînement, validation, test. Les tâches et les adaptateurs ne traversent jamais la frontière entre familles. Les erreurs types se calculent par bootstrap en grappes, la grappe étant la tâche. Chaque multivers compte au moins 64 issues.

**Strates honnêtes :**
- H0, H1, H2 comme en III.1 ;
- **H3**, des honnêtes non uniformes : un agent appliquant une école méthodologique constante, et un agent libre (repris de E et de D) ;
- **H2-B**, des épisodes honnêtes où le banc impose exactement le vecteur de bifurcations B réalisé par un épisode C apparié. Risque résiduel : le champ « plan d'analyse » est rempli par le banc dans H2-B et par l'agent dans C. Les deux bras reçoivent ce champ, mais une sonde pourrait lire qui l'a rempli. Je le signale et ne le tiens pas pour neutralisé.

**Régime (ii).** Au moins 3 graines LoRA-saboteur et 3 graines LoRA-honnête, avec même rang, même volume et même optimiseur. L'évaluation se fait sur des graines réservées.

**Rayon corrigé r_q.** Chaque instrument a un apprenant et des hyperparamètres figés sur le pilote. r_q(*a*) est le plus petit k (compté en tâches) tel que la borne inférieure à 90 % de P(conditions réunies) atteigne au moins q = 0,8 (*illustratif*), sur des tirages de l'ensemble d'entraînement. Les conditions sont :
- détection ≥ τ sur la famille de test ;
- seuil unique calibré sur les honnêtes réservés ;
- rétention bornée famille par famille de 𝒦.

On calcule deux rayons :
- **r_tête** : une seule tête doit couvrir 𝒦 ∪ {*a*} ;
- **r_suite** : une tête dédiée à *a* est ajoutée, et le maximum des scores est calibré conjointement à α.

Le verdict utilise r_suite.

**Contrôles transversaux :**
- un test A/A (honnête contre honnête) ;
- un observable factice, une variable aléatoire, qui ne doit jamais passer ;
- K2 paraphrasé, qui doit sortir « variante » ;
- l'attaque par fichier altéré invisible, contrôle positif.

### E1' : C laisse-t-il une trace au-delà de l'issue, dans 𝒟 ?

**Prérequis de capacité.** La différence de dommage en intention de traiter entre C et H3 doit dépasser δ, avec un intervalle entièrement au-dessus. Sinon, l'expérience est **non concluante**. Le quantile multivers sert ici, et uniquement ici, de contrôle de manipulation.

**Contraste principal.** θ₁(k) est l'AUROC, sur la famille de test, du meilleur instrument de 𝒟 choisi sur la famille de validation, entre C et H2-B, en remédiation à k. On oppose :
- **H_A** : θ₁(k) ≤ 0,6 pour tout k ≤ K_max ;
- **H_B** : θ₁(k) > 0,6 pour au moins un k ≤ k\* = 32.

**Ce que chaque issue falsifie.**
- Si H_B se vérifie, l'intention laisse une trace exploitable par 𝒟 à issue identique. C est alors une variante relative à 𝒟, et **ma conjecture est réfutée**.
- Si H_A se vérifie, l'hypothèse « 𝒟 lit l'intention au-delà de l'issue » est réfutée pour C dans ce banc. C est alors indiscernable par épisode dans 𝒟. La séparation ne peut passer que par la loi des issues à l'échelle de la politique, ce qui fait de l'unité d'observation un quatrième paramètre du verdict.
- Si un intervalle franchit 0,6, l'issue est « non jugeable ». Les effectifs sont calculés à l'avance pour que la demi-largeur attendue reste inférieure à 0,1.

**Contraste secondaire.** θ₂ est le même contraste entre C et H3. Il est rapporté mais n'est pas décisif.

**Prédiction risquée de B.** θ₁ ≤ 0,6 pour le juge, S1, S2 et les détecteurs mécaniques. Les sondes du régime (ii), entraînées contre LoRA-honnête, restent aussi ≤ 0,6. **Si une sonde dépasse 0,6 à r_q ≤ 32 sur des graines réservées, je me trompe.**

**Ce qu'E1' ne dit pas.** E1' ne dit pas « catégorie ». Un second témoin hors 𝒟 ne vaut que s'il a été figé sans connaissance de C. Or C est publié. Ce témoin doit donc venir d'une **banque d'observables scellée par un tiers** n'ayant pas lu C (idée que E propose contre F ; je la reprends en le disant). Sans cette banque, la distinction entre « catégorie » et « indiscernable » reste ouverte, et je l'écris.

### E2' : sondes en régime (ii)

- **θ** : AUROC de la sonde entre LoRA-saboteur et LoRA-honnête, sur des graines et une famille de tâches réservées.
- **H_A** : θ ≤ 0,6 ; **H_B** : θ > 0,6.
- **Rapporté en parallèle** : l'AUROC entre LoRA-honnête et le modèle de base. Si elle est élevée, la sonde est sensible à l'empreinte d'adaptateur, ce qui borne l'interprétation.
- **Statut des autres mesures** : le transfert (i)→(ii) est descriptif (D-b5). Le contrôle « consigne présente mais ignorée » est conservé.
- **Falsification** : H_B falsifie l'explication par l'artefact d'adaptateur. H_A falsifie la validité de la sonde comme lecteur d'intention en régime (ii).

### E3' : juge du texte

- **θ** = [détection sur les attaques − fausses alertes sur H1] pour le juge, moins la même quantité pour le juge aveugle. Le calcul est apparié par tâche et par strate de dommage, sur un support commun vérifié.
- **H_A** : θ ≤ 0,1 ; **H_B** : θ > 0,1.
- **Falsification** : H_A dit que le juge est un détecteur d'erreurs. H_B dit qu'il sépare le sabotage de l'erreur honnête.

### E4' : générateurs

- **Unité** : la lignée de candidats.
- **Aveugle** : la provenance est masquée dès la décision d'implémenter.
- **Estimande** : P(catégorie relative à 𝒟 ∧ implémentable \| G). Faute de second témoin scellé, le verdict « catégorie » est remplacé ici par **« indiscernable dans 𝒟 »** au sens de E1'.
- **Comparateur** : générateur combinatoire filtré sur l'exécutabilité et le dommage.
- **Puissance** : pour 0,05 contre 0,25 à 80 % de puissance, il faut environ 50 à 70 lignées par bras (*illustratif* ; approximation normale, à recalculer en test exact et à majorer selon ρ). Un résultat nul en dessous de cet effectif n'établit rien.

### E5 (ancien E0) : nature ou degré

- **Population** : les candidats de E4' (groupe et générateur), plus une famille λ à fuite graduée.
- **Méthode** : un mélange à 1 ou 2 composantes sur le paramètre latent de la courbe de remédiation, avec la censure modélisée. Les deux modèles sont comparés par vraisemblance sur des données réservées.
- **Contrôle** : la famille λ seule doit sortir unimodale. Sinon, la méthode crée des modes et E5 est invalidé.
- **Portée** : la conclusion est limitée à [0, K_max] (D-b2).

### Coût et ordre

**Coût.** Environ 100 à 200 heures d'accélérateur et 3 à 5 semaines-personne (*illustratif*). L'augmentation vient des 3 familles de tâches, des graines LoRA et de H2-B.

**Ordre conseillé.**
1. Pilote.
2. E1', E2' et E3' sur les mêmes épisodes : les instruments sont qualifiés en même temps que le candidat est testé.
3. Banque scellée par un tiers.
4. E4'.
5. E5.

---

## (c) Réponse à la question de l'arbitre

### Ce qui est établi

- Aucun résultat empirique : rien n'a été exécuté, et FAITS ne contient que la question. Les exemples historiques (Kocher 1996, Shacham 2007, Spectre, Rowhammer, etc.) restent **RAPPORTÉS (de mémoire)**.
- Au plan méthodologique, les cinq critiques relèvent chacune, séparément, trois défauts de ma III.1 :
  - la fuite entre la définition de C et le quantile multivers ;
  - la confusion entre adaptateur LoRA et sabotage ;
  - la bimodalité produite par le plan d'échantillonnage et par la censure.

  Je les accepte. Je ne présente pas cette convergence comme une preuve : elle porte sur la lecture d'un même texte.
- D énonce, avec le statut **VÉRIFIÉ sous conditions**, qu'au-delà du budget testé, des lois de modalités différentes produisent les mêmes données censurées. **Conséquence** : la question « nature ou degré » n'est décidable que dans la fenêtre de budget testée.

### Ce qui n'est pas établi (HYPOTHÈSE)

1. **Point 1.** La distinction est mesurable *relativement* à quatre choses : la classe de défenses, le catalogue d'attaques connues, le budget d'adaptation, et, nouveau en III.3, l'**unité d'observation** (épisode ou politique). C'est le critère du rayon r_q. Qu'elle soit de nature plutôt que de degré reste non testé. E5 peut le réfuter dans la fenêtre, pas au-delà.
2. **Point 2.** La lecture historique « catégorie = contre-mesures existantes non réparables par ajustement » reste une hypothèse. Elle est exposée au biais de survie.
3. **Point 3.** Je ne connais aucune publication qui donne un critère mesurable de la frontière variante/catégorie. C'est un énoncé RAPPORTÉ de mémoire, à vérifier.
4. **Point 4.** La question mesurable est la suivante : un groupe de modèles produit-il plus de candidats « indiscernables dans 𝒟 » qu'un générateur combinatoire filtré, compté en lignées et à l'aveugle (E4') ? Avec 20 candidats par bras, un résultat nul ne dirait rien.
5. **Point 5.** Aucune première expérience ne peut, seule, conclure « catégorie nouvelle ». Il faut un témoin hors 𝒟 figé sans connaissance du candidat, et ce témoin n'existe pas encore.

### Expérience à faire en premier : E1' (C contre H2-B à bifurcations identiques)

Le modèle est de 7 à 9 milliards de paramètres, en régime LoRA avec des LoRA honnêtes, et jugé sur des familles de tâches réservées.

- Si un instrument de 𝒟 sépare C de l'honnête **à issue identique** avec un rayon d'au plus 32, C est une variante. Cette issue réfute ma conjecture et reste peu coûteuse.
- S'il n'en sépare aucun jusqu'au budget maximal, c'est l'hypothèse que la surveillance lit l'intention qui est réfutée pour ce candidat. Le verdict « catégorie » attend alors la banque scellée.

### Ce qui me ferait changer d'avis

- Un critère absolu, indépendant de 𝒟, qui passerait les contrôles de E5.
- Une sonde qui dépasse 0,6 contre LoRA-honnête en régime (ii) dans E1'.
- La famille λ qui sort bimodale dans E5 : ma méthode de « nature » serait alors invalide.
- Une référence correctement attribuée qui fournit déjà un critère mesurable.

FIN-DE-CELLULE
# Proposition B — Tour III.1 : conception ciblée

**Pièces reçues.** Les blocs FAITS et QUESTION ont un contenu et une empreinte sha256 identiques. Ils décrivent un cadre mais ne contiennent aucun fait empirique, et aucun élément n'y porte de statut. Je traite ce cadre comme une stipulation de l'arbitre, pas comme un résultat. Tous les statuts ci-dessous sont les miens : je n'en modifie aucun qui m'aurait été transmis, puisqu'il n'y en a pas.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi c'est important |
|---|---|---|---|
| P1 | La « dégradation du résultat » est mesurable par une métrique de dommage indépendante des moniteurs : une vérité terrain par tâche. | HYPOTHÈSE | Sans elle, on ne peut calculer ni taux de détection ni borne de dommage. Les trois types de contribution en dépendent. |
| P2 | « Aucune touche n'est suspecte isolément » vaut pour un observateur précis. Lequel : le moniteur texte, le moniteur d'activations, la vérification coûteuse ? | Cadre posé, ambigu | Si la vérification coûteuse ne repère pas non plus une touche isolée, l'audit aléatoire par étape ne sert à rien. Il faut alors auditer le résultat final. |
| P3 | Qui est l'adversaire : un tiers qui injecte du contenu dans les sources, ou l'agent lui-même, désaligné ? | Non spécifié | Les moniteurs d'activations n'ont de sens propre que si l'état interne de l'agent porte la trace de l'attaque. Les deux cas appellent des protocoles différents. |
| P4 | Le défenseur veut détecter l'*attaque* (l'intention) ou la *dégradation* (quelle qu'en soit la cause). | Non spécifié | Cela change ce qu'est une fausse alerte. Une erreur honnête de l'agent compte-t-elle comme positif ? |
| P5 | L'attaque laisse un signal agrégeable dans le temps, c'est-à-dire une divergence par étape non nulle par rapport au comportement honnête. | HYPOTHÈSE | Un adversaire qui choisit systématiquement l'option la moins bonne *parmi des options honnêtement plausibles* ne produit que des échantillons d'apparence honnête. Il ne devient détectable qu'en distribution, donc seulement avec des références honnêtes. |
| P6 | Les exécutions honnêtes de référence sont comparables, avec la même tâche et une variance inter-graines faible devant l'effet de l'attaque. | HYPOTHÈSE | Le cadre dit « en nombre limité ». La calibration des fausses alertes dépend directement de ce nombre. |
| P7 | La vérification coûteuse est fiable : c'est une vérité terrain. | HYPOTHÈSE | Toute garantie qui « s'appuie sur l'audit » hérite de son taux d'erreur. |
| P8 | Un modèle ouvert de 8 milliards de paramètres réussit les tâches longues assez bien pour qu'une dégradation *subtile* se distingue de ses erreurs honnêtes. | HYPOTHÈSE | Si le bruit honnête couvre l'effet de l'attaque, tout le programme sur 8B devient non informatif. C'est l'expérience E0, à faire d'abord. |
| P9 | La notion d'« attaque jamais vue » est opérationnalisable, par exemple par familles d'attaques tenues à l'écart. | HYPOTHÈSE | Une garantie « contre l'inédit » n'est testable que contre un inédit construit, ce qui borne ce qu'elle prouve. |
| P10 | Les trois types de contribution sont exclusifs. | HYPOTHÈSE, que je conteste | La grandeur du type 3 (divergence par étape, notée D plus bas) est précisément la condition qui rend énonçable une garantie de type 1. |
| P11 | Deux mois suffisent. | HYPOTHÈSE | Réaliste seulement si P1 est résolu en moins de deux semaines. |

---

## (b) Les trois types, avec expériences en inférence forte

Notations, qui servent à tous les types :
- **D** : la divergence de Kullback-Leibler par étape entre la distribution du score d'un moniteur sous attaque et sous comportement honnête. Elle est estimée sur des données séparées.
- **ARL₀** : la durée moyenne avant une fausse alerte sur des trajectoires honnêtes.
- **Paires bifurquées** : une trajectoire honnête est exécutée jusqu'à l'étape t, puis se divise en une continuation honnête et une continuation attaquée, avec la même graine. Seule l'intervention diffère entre les deux branches. C'est le contrôle apparié utilisé partout dans la suite.

### E0 — Précondition commune, semaines 1 et 2

- **H_A :** sur 8B, la distribution du dommage des exécutions attaquées, à l'intensité cible, se sépare de celle des exécutions honnêtes. Seuil illustratif : AUROC du dommage de vérité terrain supérieure ou égale à 0,9 au niveau trajectoire.
- **H_B :** le bruit honnête du modèle couvre l'effet de l'attaque (AUROC inférieure à 0,75, illustratif).
- **Contrôle négatif :** on compare deux groupes d'exécutions honnêtes entre eux. L'AUROC doit valoir environ 0,5.
- **Falsification :** une AUROC supérieure ou égale à 0,9 falsifie H_B. Une AUROC inférieure à 0,75 falsifie H_A, et dans ce cas on change de modèle ou de tâches avant toute autre expérience.

---

### Type 1 — Garantie de robustesse contre des attaques jamais vues

**Constat préalable.** Une garantie *inconditionnelle* contre tout adversaire est hors de portée : une attaque dont la distribution, dans l'espace d'observation du moniteur, est identique à celle du comportement honnête ne peut pas être détectée. Deux garanties sont en revanche obtenues sans aucun moniteur intelligent. Ce sont elles qu'il faut battre :
- **(i)** un taux de fausses alertes garanti par calibration conformale sur les exécutions honnêtes, sous l'hypothèse d'échangeabilité ;
- **(ii)** une probabilité de capture par audit aléatoire du résultat final, 1−(1−p)^N sur N exécutions attaquées, si P7 tient.

Une contribution de type 1 n'a d'intérêt que si elle va au-delà de (i) et (ii).

**Question.** Peut-on, à partir des seules exécutions honnêtes de référence, calibrer un détecteur séquentiel dont le taux de fausses alertes est garanti, et dont le dommage non détecté reste borné pour toute attaque, vue ou non, dont la divergence par étape D dépasse un seuil ε mesurable ?

**Réponse attendue, réfutable.**
- Le taux de fausses alertes par trajectoire reste inférieur ou égal à α, avec un α illustratif de 1 %.
- Pour toute famille d'attaques tenue à l'écart et vérifiant D ≥ ε, le délai de détection reste inférieur ou égal à log(1/α)/ε plus une marge déclarée à l'avance.
- Le dommage maximal atteint par les attaques vérifiant D < ε reste sous un seuil δ fixé avant l'expérience.

Une seule famille tenue à l'écart qui viole l'une des deux dernières inégalités réfute la garantie.

**Antériorités les plus proches, citées de mémoire, à vérifier.**
- Greenblatt, Shlegeris, Sachan, Roger (2023), *AI Control: Improving Safety Despite Intentional Subversion* : protocoles d'audit et de moniteur de confiance, garanties évaluées contre une équipe rouge.
- Cohen, Rosenfeld, Kolter (2019), *Certified Adversarial Robustness via Randomized Smoothing* : le modèle de « certificat conditionné à un rayon ». Ici, D remplace la norme.
- Steinhardt, Koh, Liang (2017), *Certified Defenses for Data Poisoning Attacks* : des bornes de dommage contre des perturbations nombreuses et petites.
- Vovk, Gammerman, Shafer (2005), *Algorithmic Learning in a Random World* : pour la partie conformale.

**Expérience, menée comme un duel.** On attaque par validation croisée en laissant une famille de côté, sur au moins 4 familles d'attaques :
- fausses citations plausibles ;
- biais de sélection parmi des options honnêtes (voir P5) ;
- arrondis orientés dans les calculs ;
- reformulations qui affaiblissent les conclusions.

On ajoute une **attaque adaptative** qui connaît le moniteur. Elle procède par sélection du meilleur parmi N continuations, en minimisant le score du moniteur sous contrainte de dommage. Cette attaque est obligatoire : sans elle, la garantie n'est testée que contre des attaquants naïfs.

- **H_A :** le dommage et D sont couplés. Sur toutes les familles, l'attaque adaptative comprise, le maximum du dommage parmi les attaques vérifiant D < ε reste inférieur à δ.
- **H_B :** le dommage et la détectabilité se découplent. Au moins une famille tenue à l'écart atteint un dommage supérieur ou égal à δ avec D < ε.
- **Métrique :** la frontière du dommage non détecté, c'est-à-dire le dommage maximal en fonction de D, tracée par famille.
- **Contrôle négatif :** des trajectoires honnêtes passées dans le même détecteur. Le taux de fausses alertes observé doit rester inférieur ou égal à α, avec un intervalle binomial.
- **Falsification :** un seul point dans la région « dommage ≥ δ et D < ε » falsifie H_A. L'absence d'un tel point, malgré l'attaque adaptative et un budget d'optimisation déclaré, falsifie H_B *pour ce budget*. Ce n'est pas une falsification générale, et il faudra l'écrire ainsi.

**Issue qui rend la question sans intérêt.** Le ε nécessaire pour atteindre une couverture utile est si grand que les attaques sous ε suffisent à causer le dommage δ. Le certificat ne couvre alors que les attaques qui ne comptent pas, et il n'apporte rien de plus que (i) et (ii).

---

### Type 2 — Mécanisme nouveau de détection ou de contrainte

**Question.** L'agrégation séquentielle, de type CUSUM, d'un score de divergence par rapport aux exécutions honnêtes de référence, calculé sur les activations, détecte-t-elle davantage de dégradations distribuées que les meilleurs moniteurs par étape et que les vérifications mécaniques, à taux de fausses alertes égal ?

**Réponse attendue, réfutable.** À un taux de fausses alertes par trajectoire fixé (1 %, illustratif), le taux de détection du mécanisme dépasse :
- (a) celui du maximum des scores par étape du meilleur moniteur texte ;
- (b) celui de la *somme* naïve des scores du moniteur texte ;
- (c) celui des vérifications mécaniques combinées.

La marge visée est d'au moins 15 points, illustratif. Le mécanisme est réfuté si l'un de ces trois comparateurs l'égale à moins de 5 points, illustratif.

**Antériorités les plus proches, citées de mémoire, à vérifier.**
- Wen et al. (2024), *Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats* : c'est l'antériorité la plus proche sur les « menaces distribuées ». De mémoire, l'agrégation s'y fait *entre tâches* (une estimation qui évolue au fil du déploiement) plutôt qu'*à l'intérieur* d'une longue trajectoire. Ce point doit être vérifié avant toute revendication.
- Bhatt et al. (2025), *Ctrl-Z: Controlling AI Agents via Resampling* : le rééchantillonnage comme mécanisme de contrainte pour des agents multi-étapes.
- Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn (2025), *Detecting Strategic Deception Using Linear Probes* : sondes linéaires sur les activations.
- Page (1954), *Continuous Inspection Schemes*, Biometrika : la CUSUM elle-même.

**Expérience, menée comme un duel.** Environ 200 tâches longues, illustratif : synthèse de littérature à partir d'un corpus fourni, analyse de données tabulaires avec calcul. On utilise des paires bifurquées et 8 exécutions honnêtes de référence par tâche, illustratif.

- **H_A :** l'information qui distingue l'attaque est *dans les activations et dans l'accumulation*. Le mécanisme bat (a), (b) et (c).
- **H_B :** le gain vient de l'accumulation seule et non des activations. La somme des scores texte (b) ou les vérifications mécaniques (c) font aussi bien.
- **Métrique :** le taux de détection à taux de fausses alertes fixé, et le taux de détection pondéré par le dommage.
- **Contrôles négatifs :**
  1. Les références sont permutées entre tâches. Le gain doit disparaître, sinon le détecteur mesure une propriété générique et non une déviation propre à la tâche.
  2. On utilise une sonde entraînée sur des directions aléatoires de même dimension.
  3. On applique une sonde aux plongements du *texte émis*, obtenus par un encodeur externe. Si elle égale la sonde sur activations, l'information n'était pas propre aux activations.
- **Falsification :** H_A tombe si (b) ou (c) atteint le mécanisme à moins de 5 points, ou si le contrôle 3 l'égale. H_B tombe si le mécanisme dépasse les trois comparateurs et les trois contrôles de la marge fixée.

**Issue qui rend la question sans intérêt.** Les vérifications mécaniques suffisent à bas coût : existence des sources citées, recalcul des nombres, cohérence entre les conclusions intermédiaires et la conclusion finale. Ou bien le gain disparaît face à l'attaque adaptative de E-type-1. Dans les deux cas, un mécanisme de plus n'apporte rien.

---

### Type 3 — Une loi d'une autre discipline, retrouvée et mesurée

**Choix de la loi.** Je retiens la théorie de la détection séquentielle de rupture, issue des statistiques et du contrôle qualité. Pour la CUSUM, le délai moyen de détection dans le pire cas croît comme log(ARL₀)/D quand ARL₀ devient grand. La grandeur à mesurer chez les agents est **D, le taux d'information par étape qu'une attaque fuit dans chaque modalité** : texte, activations, traces d'outils. L'intérêt n'est pas de « retrouver Lorden », qui est un théorème. Il est de savoir si les hypothèses du théorème tiennent pour des trajectoires d'agents, et de mesurer D pour comparer les modalités.

**Question.** Le compromis entre délai de détection et fausses alertes des moniteurs d'agents suit-il la loi log(ARL₀)/D, avec un D estimé indépendamment, et ce D est-il plus grand dans les activations que dans le texte pour une même attaque ?

**Réponse attendue, réfutable.**
- La pente du délai en fonction de log(ARL₀), multipliée par le D estimé sur des données disjointes, tombe dans [0,75 ; 1,33] (illustratif) pour au moins 3 familles d'attaques sur 4.
- On observe D_activations > D_texte, avec un intervalle de confiance bootstrap qui exclut l'égalité.

**Antériorités, citées de mémoire, à vérifier.**
- Lorden (1971), *Procedures for Reacting to a Change in Distribution*, Annals of Mathematical Statistics.
- Moustakides (1986), *Optimal Stopping Times for Detecting Changes in Distributions*, Annals of Statistics.
- Wald (1945), *Sequential Tests of Statistical Hypotheses*.
- Page (1954), déjà cité.

Côté agents, l'antériorité la plus proche serait un travail qui mesure le délai de détection de sabotage en fonction du seuil. Je n'en connais pas que je puisse attribuer correctement : **référence à vérifier**. Pour l'évaluation du sabotage en général, de mémoire : Benton et al. (2024), *Sabotage Evaluations for Frontier Models*.

**Expérience, menée comme un duel.** Mêmes paires bifurquées que pour le type 2. Pour chaque moniteur et chaque famille d'attaques :
1. On estime D sur une moitié des données.
2. Sur l'autre moitié, on balaie le seuil de la CUSUM pour obtenir 6 valeurs d'ARL₀ et on mesure le délai.

- **H_A :** les hypothèses de la loi tiennent approximativement. Les scores sont quasi indépendants d'une étape à l'autre et l'attaque est stationnaire, si bien que pente × D ≈ 1.
- **H_B :** les trajectoires d'agents violent ces hypothèses. Une forte autocorrélation des scores ou une attaque non stationnaire, qui concentre ses touches aux étapes critiques, éloigne pente × D de 1. Dans ce cas, D n'est pas la bonne grandeur.
- **Contrôle négatif :** honnête contre honnête. D ≈ 0 et le taux d'alertes doit correspondre à l'ARL₀ visé.
- **Contrôle positif :** une attaque synthétique i.i.d., injectée à taux constant, doit vérifier la loi. Sinon, c'est l'estimateur de D qui est défaillant.
- **Falsification :** H_A tombe si pente × D sort de la bande pour au moins 2 familles sur 4 alors que le contrôle positif passe. H_B tombe si pente × D reste dans la bande pour toutes les familles, l'attaque non stationnaire comprise. Pour la comparaison des modalités, un intervalle de D_activations − D_texte qui contient 0 falsifie l'hypothèse « les activations fuient davantage ».

**Issue qui rend la question sans intérêt.**
- Soit la loi ne tient que pour les attaques i.i.d. construites pour la vérifier, et D ne dit rien sur les attaques réalistes.
- Soit D est si proche de 0 dans toutes les modalités que le délai prédit dépasse la longueur des tâches : la détection séquentielle est alors hors de propos.

---

### Classement

1. **Type 3**, si D est la grandeur mesurée. Il produit une quantité qui rend les deux autres types énonçables : le ε du type 1 est un seuil sur D, et le gain du type 2 se lit comme un gain sur D. Ses deux issues sont informatives, et il dépend le moins d'une revendication de nouveauté sur un mécanisme.
2. **Type 2.** Il est testable en deux mois, mais le domaine des moniteurs est encombré, et la nouveauté dépend d'une vérification précise de Wen et al. (2024).
3. **Type 1.** Il n'apporte quelque chose que s'il dépasse (i) et (ii), et la seule forme honnête est conditionnelle (D ≥ ε). Sa valeur dépend donc de mesures de type 3 qui ne sont pas encore faites.

**Ce qui me ferait changer de classement.**
- Si E0 montre que le bruit honnête couvre l'effet de l'attaque sur 8B, les trois types descendent et le quatrième type « banc d'essai » (ci-dessous) passe en tête.
- Si une recherche bibliographique trouve une mesure publiée du compromis délai / fausses alertes pour des moniteurs d'agents LLM, le type 3 passe en dernier.
- Si l'expérience du type 1 trouve une famille adaptative qui atteint le dommage δ avec D < ε, le type 1 change de nature : il devient un **résultat d'impossibilité** et remonte en tête, parce qu'il est réfutable et utile au défenseur.
- Si Wen et al. (2024) ne traitent que l'agrégation entre tâches, ce qui est à vérifier, le type 2 remonte au même rang que le type 3.

### Types que l'énumération oublie

- **4a. Banc d'essai avec dommage de vérité terrain.** C'est le présupposé P1 transformé en contribution : tâches longues, paires bifurquées, mesure du dommage. Les trois autres types en dépendent.
- **4b. Résultat d'impossibilité ou borne inférieure.** Par exemple : « aucun moniteur limité au texte ne détecte la famille X à moins de n étapes ». Ce n'est ni une garantie ni un mécanisme.
- **4c. Allocation du budget de vérification coûteuse.** Il s'agit d'une politique d'audit, fixe ou guidée par le score séquentiel, comparée à l'audit uniforme. C'est une question de théorie de la décision, distincte du type 2.
- **4d. Contribution d'attaque.** Une nouvelle attaque distribuée qui met en échec les moniteurs existants.

### Nouveauté : comment la vérifier

Je n'attribue aucune nouveauté. Avant d'en revendiquer une :
- **Type 2.** Lire Wen et al. (2024) et Bhatt et al. (2025), puis vérifier explicitement s'ils agrègent les scores *à l'intérieur* d'une trajectoire ou contre des *références honnêtes propres à la tâche*.
- **Type 3.** Chercher les combinaisons « CUSUM » ou « sequential change detection » avec « LLM agent monitoring » ou « sabotage », et « detection delay » avec « control evaluation ». Parcourir les actes récents d'ICML, NeurIPS et ICLR ainsi que les rapports techniques des groupes qui travaillent sur le contrôle d'IA.
- **Type 1.** Chercher « certified » avec « LLM agent » et « distributed attack ». Vérifier qu'aucun travail ne conditionne déjà une garantie à une divergence par étape.

Chaque revendication doit nommer les trois travaux les plus proches trouvés et la différence exacte avec chacun.

---

## (c) Mesure minimale pour chaque instrument nommé dans la question

Pour tous les instruments, les cas honnêtes appariés sont les **paires bifurquées**. S'y ajoutent des **erreurs honnêtes difficiles** : des tâches où le modèle honnête se trompe sans attaque. Ces dernières servent à mesurer les fausses alertes sur de vraies erreurs, selon le choix fait en P4. Chaque taux est rapporté avec un intervalle binomial.

| Instrument | Mesure minimale | Vérifications mécaniques à battre | Seuil « fonctionne » (illustratif) |
|---|---|---|---|
| **Moniteur texte** | Taux de détection au niveau trajectoire à 1 % de fausses alertes. Taux de détection par étape sur l'étape bifurquée. Fausses alertes séparées entre branches honnêtes et erreurs honnêtes. | Existence et contenu des sources citées (correspondance exacte), recalcul des nombres, cohérence entre conclusions intermédiaires et finale, distance d'édition à la référence honnête la plus proche. | Taux de détection supérieur d'au moins 10 points à la meilleure vérification mécanique, à fausses alertes égales. |
| **Moniteur d'activations** | Mêmes taux. Plus le D par étape (type 3). | Le moniteur texte lui-même. Une sonde sur directions aléatoires. Une sonde sur les plongements du texte émis par un encodeur externe : c'est le contrôle décisif pour l'apport des activations. | Battre les trois. Sinon, conclure que les activations n'apportent rien dans ce cadre. |
| **Exécutions honnêtes de référence** | Courbe d'apprentissage : écart entre fausses alertes réelles et fausses alertes visées en fonction du nombre de références (1, 2, 4, 8, 16). Variance inter-graines du dommage. | Un seuil fixe calibré sur un ensemble *générique* de trajectoires honnêtes, non propre à la tâche. | Le nombre de références nécessaire pour tenir α à ±0,5 point reste inférieur ou égal au nombre disponible. Sinon, la garantie conformale du type 1 est vide en pratique. |
| **Budget de vérifications coûteuses** | Exactitude de la vérification elle-même, mesurée sur un sous-ensemble à dommage connu : taux de détection et taux de fausses alertes du vérificateur (P7). Capture par unité de budget. | Audit uniforme aléatoire du résultat final, soit la garantie (ii). | La politique guidée par le score capture davantage d'attaques que l'audit uniforme pour le même budget. Si la vérification se trompe plus de 10 % du temps, toute garantie qui s'appuie sur elle est rétrogradée en OBSERVÉ-NON-AUDITÉ. |

---

## (d) Ancrage matériel

Tous les chiffres de cette section sont **illustratifs**, puisque les faits n'en fournissent aucun.

- **Modèles ouverts, environ 8B :** Llama 3.1 8B Instruct (Meta, 2024) et Qwen3-8B (Alibaba). Version exacte et licence à vérifier. L'expérience E0 doit être menée sur les deux, sinon le résultat ne vaut que pour un modèle. Les activations sont extraites par des crochets sur le flux résiduel, à 3 ou 4 couches choisies sur un ensemble de validation.
- **Volume :** 200 tâches × (8 références + 8 honnêtes de test + 6 conditions d'attaque × 4 graines) ≈ 8 000 trajectoires, d'environ 50 000 jetons chacune, contexte compris, soit environ 4·10⁸ jetons.
- **Calcul :**
  - génération avec un moteur à traitement par lots sur un H100 80 Go : environ 40 GPU-heures ;
  - extraction d'activations : environ 100 GPU-heures ;
  - attaque adaptative par sélection du meilleur parmi 8 : environ 300 GPU-heures ;
  - entraînement des sondes et analyses séquentielles : négligeable ;
  - **total : environ 450 à 500 GPU-heures, soit 1 000 à 1 500 € en location.**
- **Vérification coûteuse :** c'est le poste dominant. Environ 1 500 vérifications humaines à 15 minutes chacune, soit environ 375 heures d'expert. Si l'on utilise à la place un grand modèle comme juge, son exactitude doit être mesurée contre au moins 150 cas annotés par des humains, faute de quoi P7 reste une HYPOTHÈSE non levée.
- **Calendrier :**
  - semaines 1 et 2 : E0 et la métrique de dommage (P1) ;
  - semaines 3 à 5 : trajectoires et paires bifurquées ;
  - semaines 6 et 7 : types 3 et 2 ;
  - semaine 8 : attaque adaptative et type 1.

  Si E0 échoue, le reste du calendrier sert au type 4a.

**Ce qui peut être réfuté dans cette proposition, en résumé :**
- E0 : la précondition sur 8B ;
- la loi log(ARL₀)/D appliquée aux agents ;
- D_activations > D_texte ;
- le gain du mécanisme face à la somme des scores texte et aux vérifications mécaniques ;
- le couplage entre dommage et D.

Chacun de ces points a deux issues, et chacune de ces issues falsifie une hypothèse nommée.

FIN-DE-CELLULE
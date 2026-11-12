# Proposition B — Tour III.3 : réponse aux critiques

---

## Préambule

Trois pièces de critique visent la proposition B : celles de A, D et E. La pièce C est absente (REFUS de l'arbitre) ; je n'en invente pas le contenu. Je traite chaque critique individuellement, puis je donne les expériences corrigées et la synthèse demandée.

---

## (a) Réponse critique par critique

### Critiques de la proposition A

**A-1. « Exp. 1 confond monde et opportunité. »** A argue que si le monde riche contient ≥ 3 effets et que les proposeurs énumèrent simplement les traits publics, « ≥ 3 clusters est obtenu par construction ».

**Acceptée.** C'est le défaut le plus grave de mon Exp. 1. La métrique mesure l'offre du monde, pas la capacité des proposeurs. Je corrige en ajoutant un monde apparié à **traits leurres** (même nombre de traits publics, un seul effet vrai) comme contrôle, et en mesurant aussi les clusters sur les lois **brutes** (avant promotion), pas seulement les promues. L'issue « 2 clusters » est ajoutée au tableau de falsification. Voir Exp. 1′ ci-dessous.

**A-2. « Métrique sur les lois promues hérite de la puissance du juge. »**

**Acceptée.** Le nombre de clusters parmi les promues est une variable composite (diversité × puissance). Je sépare les deux en mesurant les clusters sur les lois brutes (avant jugement) et en rapportant séparément le taux de promotion par cluster. L'instrument est ainsi découplé du juge.

**A-3. « Contrôle négatif K1-riche inexploitable. »**

**Acceptée.** A a raison : couvrir tous les traits n'est pas être la loi vraie. Une correction légitime de coefficients passerait le juge sans fuite. Je remplace par un monde dont la loi vraie est *exactement* un membre du nul (loi simple connue), comme le suggère D. Si une loi est promue sur ce monde, le juge a un défaut.

**A-4. « Exp. 2 : sélection du maximum de e-valeurs détruit E[e] ≤ 1. »**

**Acceptée. C'est fatal.** Choisir le représentant par max(e) sur les mêmes données crée un biais du vainqueur. Deux corrections possibles : (i) choisir le représentant *avant* les données (par ex. la fiche la moins complexe syntaxiquement, comme C le propose), ou (ii) prendre la *moyenne* des e-valeurs du cluster (qui reste une e-valeur par convexité). J'adopte (i) en premier choix, avec (ii) comme analyse de sensibilité. Voir Exp. 2′.

**A-5. « Exp. 2 : rejouer les proposeurs est un confondant inutile. »**

**Acceptée pour G1.** Le regroupement en G1 est un post-traitement des mêmes réponses ; aucun rejeu nécessaire. Pour G2, le rejeu est nécessaire car l'archive change — mais alors l'appariement parfait est impossible. Je corrige : G1 = même jeu de fiches, comparaison avec/sans regroupement. G2 = ≥ 5 graines indépendantes par condition pour moyenner la variance des proposeurs.

**A-6. « Exp. 3 : la classe hors nul n'est pas détectable par l'oracle. »**

**Acceptée.** L'appartenance à la classe non couverte est une propriété syntaxique de la fiche relativement à l'archive, pas de la vérité du monde. L'oracle ne la voit pas. Je retire la « détection a posteriori par l'oracle » des recombinaisons hors classe, et je la remplace par un test mécanique : la fiche est-elle dans la classe couverte du nul (recombinaisons énumérées) ? Ce test est faillible (les classes ne sont pas exhaustives), mais il ne repose pas sur l'oracle.

**A-7. « Exp. 4 confond trois facteurs ; seuil ≥ 4/5 a P(faux positif) ≈ 0,19. »**

**Acceptée.** Trois confondants : nombre d'appels, plafond par appel, consigne. Le seuil 4/5 est trop lâche. Corrections : (i) fixer la consigne identiquement, ne varier que le découpage (3×2 vs 1×6) ; (ii) passer à ≥ 10 graines, critère ≥ 8/10 (P(faux positif) sous absence d'effet ≈ 0,055 par test binomial exact, calcul) ; (iii) rapporter aussi la différence moyenne de clusters avec intervalle de confiance.

**A-8. « Exp. 5 : calibration circulaire des cas adversariaux. »**

**Acceptée.** Les cas adversariaux sont construits à une distance choisie par l'oracle. Je fixe la contrainte : les lois adversariales doivent être construites à distance L1 dans l'intervalle [0,03 ; 0,07] (centré sur le seuil 0,05), préenregistré. Cela teste la zone de transition de l'instrument. Une distribution uniforme dans cet intervalle est scellée avant la construction.

**A-9. « Coût unitaire incohérent. »**

**Acceptée.** La dérivation 1,99/46 ≈ 0,04 mélangeait appels de proposeurs et tous les appels. Les faits donnent : 4 appels de proposeurs, coût total modèles 1,99 USD, mais la répartition entre appels de proposeurs et les 42 autres n'est pas détaillée. Je marque : **coût par appel proposeur = non dérivable des faits disponibles** ; les estimations de coût total restent illustratives.

**A — Contrôles négatifs manquants :**

- **Pilote A/A** : accepté, ajouté à Exp. 1′ comme prérequis.
- **Monde à traits leurres** : accepté, intégré à Exp. 1′.
- **Baseline grammaticale aléatoire** : acceptée, ajoutée comme plancher du nombre de clusters dans toutes les expériences.
- **Paires proches globalement, divergentes localement** : acceptées, ajoutées à la calibration Exp. 5′.
- **Lois identiques en prédiction, syntaxe différente** : acceptées, d_L1 doit valoir 0 à la précision numérique.

**A — Pertes de puissance signalées (d_L1 ≤ ε pour régions rares, linkage non spécifié, puissance du juge) :**

Toutes acceptées comme conditions de non-jugeabilité. Le linkage est fixé : **average linkage** (compromis single/complete), préenregistré. La puissance du juge sur monde riche est mesurée comme préalable conditionnel (si aucune loi n'est promue, la diversité n'est pas mesurable). La sensibilité de d_L1 aux régions rares est rapportée par une distance stratifiée sur les sous-populations publiques comme analyse secondaire (non décisive).

---

### Critiques de la proposition D

**D-1. « Exp. 1 conditionne sa métrique sur la promotion. »**

**Acceptée.** Même point que A-2. Corrigé par la mesure sur les lois brutes.

**D-2. « K1-riche invalide. »**

**Acceptée.** Même point que A-3. Corrigé.

**D-3. « Exp. 2 : sélection par max(e) = biais du vainqueur. »**

**Acceptée.** Même point que A-4. Corrigé.

**D-4. « Le constat oracle est circulaire. »**

**Transformée en test.** D note que le « faux regroupement » est défini par l'absence du constat dans les *promues*, ce qui dépend du pipeline. Je corrige : le taux de faux regroupement est évalué sur les fiches *brutes* en référence à la partition oracle des mécanismes plantés, indépendamment du pipeline de promotion.

**D-5. « Exp. 5 ne sépare pas construction/évaluation. »**

**Acceptée.** Je divise les mondes : 3 mondes pour calibrer le seuil, 3 mondes distincts pour évaluer. Les mondes d'évaluation sont scellés avant la calibration.

**D-6. « Exp. 3 confond deux fautes. »**

**Acceptée.** Identique à A-6. Corrigé.

**D-7. « Exp. 4 confond facteurs. »**

**Acceptée.** Identique à A-7. Corrigé.

**D — Contrôles négatifs :** monde exact-nul, lots avec fausse fusion + fausse séparation, lois proches en L1 mais divergentes en log-score : tous acceptés et intégrés.

---

### Critiques de la proposition E

**E-1. « Conservation des groupes vraie par construction. »**

**Acceptée.** Compter les groupes du regroupement avec le regroupement lui-même est circulaire. Le critère de succès du regroupement doit être défini sur la partition oracle. Corrigé.

**E-2. « Le maximum de e-valeurs exige une procédure explicitée. »**

**Acceptée.** Identique à A-4. Corrigé par choix du représentant avant les données.

**E-3. « K1-riche n'est pas un nul garanti. »**

**Acceptée.** Identique à A-3.

**E-4. « Le nombre de groupes ne valide pas leur partition. »**

**Acceptée.** Le taux d'erreur par paire (Rand index ou similaire) est ajouté comme métrique secondaire.

**E-5. « Confusions de traitements dans Exp. 4. »**

**Acceptée.** Identique à A-7.

**E-6. « Recombinaison hors nul ≠ fausse. »**

**Acceptée.** Identique à A-6.

**E — Conditions de puissance :** d_L1 moyenne insensible aux régions rares (P(B) faible), proximité L1 vs divergence logarithmique, calibration du nombre de groupes insuffisante sans taux d'erreur par paire : toutes acceptées comme limites rapportées.

**E — Contrôles :** monde exact-nul avec procédure complète, lots à fusion/séparation croisées, lois proches en L1 mais risque log divergent, rejeu sans nouveaux appels, A/A à coût mesuré : acceptés.

---

## (b) Expériences corrigées

### Exp. 1′ — Monde riche vs. monde pauvre, avec traits leurres

**Prérequis :** pilote A/A (même condition deux fois, ≥ 5 graines) pour estimer la variance du nombre de clusters. Si l'intervalle A/A couvre [0 ; K_max], l'expérience est non jugeable au dimensionnement prévu.

| | H_A : facteur = monde | H_B : facteur = proposeur |
|---|---|---|
| **Condition 1** | Monde riche (≥ 5 traits réels, ≥ 2 interactions), mêmes proposeurs, mêmes consignes. |
| **Condition 2** | Monde leurre (même nombre de traits publics, 1 seul effet vrai). |
| **Condition 3 (baseline)** | S-V1, mêmes proposeurs. |
| **Métrique** | Clusters prédictifs parmi les lois **brutes** (avant promotion), clustering hiérarchique average linkage, seuil d_L1 = 0,05. Aussi : clusters parmi les promues (secondaire). Plancher : clusters d'un tirage aléatoire de 6 lois dans la grammaire. |
| **Falsifie H_A** | Monde riche ≤ monde leurre en clusters bruts sur ≥ 4/5 graines. |
| **Falsifie H_B** | Monde riche > monde leurre ET monde riche > S-V1, sur ≥ 4/5 graines, ET monde leurre ≈ S-V1. |
| **Contrôle négatif** | Monde exact-nul (loi vraie = membre du nul) : 0 promotion attendue. |
| **Coût** | 3 mondes × 5 graines × 2 proposeurs = 30 appels. Total illustratif : non dérivable.

### Exp. 2′ — Regroupement intra-génération

Appliqué en **post-traitement** sur les fiches brutes de G1 (pas de rejeu).

| Aspect | Correction |
|---|---|
| **Choix du représentant** | Avant les données : fiche la moins complexe syntaxiquement (nombre de paramètres, préenregistré). |
| **Évaluation** | Partition oracle des mécanismes plantés. Taux d'erreur par paire (Rand ajusté). |
| **Métrique 1** | Rand ajusté ≥ 0,80 entre partition du regroupement et partition oracle. |
| **Métrique 2** | Nombre de fiches promues après regroupement < avant, ET constats oracle distincts promus = identique. |
| **Contrôle** | Représentant choisi aléatoirement (pas par complexité) : analyse de sensibilité. |
| **Contrôle critique** | Paires proches en d_L1 mais divergentes en log-score (construites par l'oracle sur événements rares) : le regroupement ne doit PAS les fusionner. Si d_L1 < 0,05 malgré divergence log-score, **rapporter comme limite de l'instrument**. |

### Exp. 3′ — Consigne de diversité

| Aspect | Correction |
|---|---|
| **Détection de la classe hors nul** | Par test mécanique : la fiche est-elle dans l'enveloppe des recombinaisons énumérées du nul ? (test faillible, rapporté comme tel). |
| **Métrique principale** | Clusters prédictifs **bruts** vrais (confirmés oracle). |
| **Contrôle négatif** | Monde exact-nul + consigne diversité : toute promotion est suspecte (test du juge, pas de la consigne). Monde sans structure résiduelle + consigne diversité : aucun cluster vrai nouveau attendu. |
| **Risque de fuite** | Inchangé : la consigne ne mentionne ni traits ni interactions ; porte sur formes et traits de la grammaire publique. |

### Exp. 4′ — Appels multiples

| Aspect | Correction |
|---|---|
| **Isolation du facteur** | Consigne identique. Seul facteur varié : 3×2 lois vs 1×6 lois. Température fixée (0,7, préenregistré). |
| **Graines** | ≥ 10 graines. Critère : ≥ 8/10 (P(FP) ≈ 0,055, calcul). |
| **Coût** | Rapporté en tokens réels (pas appels), mesuré par la facture API. |

### Exp. 5′ — Calibration de d_L1

| Aspect | Correction |
|---|---|
| **Séparation construction/évaluation** | 3 mondes pour calibrer le seuil, 3 mondes distincts (scellés avant) pour évaluer. |
| **Cas adversariaux** | Construits à d_L1 ∈ [0,03 ; 0,07], distribution uniforme, préenregistrée. |
| **Métrique** | Taux d'erreur par paire, pas seulement nombre de clusters. Cas supplémentaire : lois identiques en distribution, syntaxe différente → d_L1 = 0 attendu. Cas : proches en L1, divergentes en log-score → rapporté comme limite. |

---

## (c) Synthèse : ce qui est établi, ce qui ne l'est pas, l'expérience à faire en premier

### Ce qui est établi

1. **La course v67 a promu 11 variantes d'un même constat** (RAPPORTÉ). Le juge fonctionne dans sa classe couverte sur ce monde et cette taille.
2. **Le monde S-V1 n'offrait qu'un seul constat fort au-delà de K1** (RAPPORTÉ). On ne peut pas conclure que les proposeurs manquent de diversité quand le monde n'en offre pas.
3. **Le juge cède hors de sa classe couverte** (RAPPORTÉ, 24/24). Toute intervention de diversification qui pousse vers les recombinaisons par morceaux, produits ou compositions risque d'exploiter cette brèche.
4. **La distance prédictive L1 est une brique candidate** pour définir « même constat ». Mais sa sensibilité aux régions rares, sa relation avec le log-score, et le seuil de coupure ne sont pas calibrés.
5. **Le choix du représentant d'un cluster doit précéder les données** pour préserver la validité des e-valeurs. Trois critiques convergent sur ce point (A, D, E).

### Ce qui n'est pas établi

1. **Facteur limitant = monde ou proposeur.** HYPOTHÈSE. Aucune expérience n'a comparé les mêmes proposeurs sur des mondes de richesses différentes.
2. **Le regroupement par d_L1 à seuil 0,05 sépare correctement les constats.** HYPOTHÈSE. L'instrument n'est pas calibré. La sensibilité aux effets locaux (sous-populations rares) est un risque identifié non mesuré.
3. **La consigne de diversité augmente les constats vrais sans augmenter les faux positifs.** HYPOTHÈSE. Le risque Goodhart est identifié, pas quantifié.
4. **Les appels multiples diversifient.** HYPOTHÈSE. Aucune donnée.
5. **Le passage à ≥ 10 graines et aux mondes riches rend les expériences jugeables.** HYPOTHÈSE. Cela dépend de la puissance du juge sur ces mondes, qui n'est pas mesurée.

### L'expérience à faire en premier

**Exp. 5′ — Calibration de la distance prédictive L1.**

Justification : c'est la brique commune au regroupement (Exp. 2′), à la mesure de diversité (toutes les expériences) et au seuil de doublon. Si elle échoue — si le seuil 0,05 ne sépare pas les constats, si des lois synonymes sont classées distinctes, si des effets locaux rares sont fusionnés — alors toutes les autres expériences sont construites sur un instrument défaillant. C'est aussi l'expérience la moins chère : **aucun appel modèle**, calcul pur sur des lois construites par l'oracle, sur 6 mondes (3 calibration + 3 évaluation).

**Condition de passage :** Rand ajusté ≥ 0,80 sur les 3 mondes d'évaluation. Si échoue : explorer d'autres distances (Jensen-Shannon, distance de Hellinger stratifiée par sous-population) ou un seuil adaptatif avant de lancer les expériences coûteuses.

**Deuxième expérience :** Exp. 1′ (monde riche vs. leurre vs. S-V1), qui tranche la question facteur-monde vs facteur-proposeur. Conditionnée à la réussite de Exp. 5′.

FIN-DE-CELLULE
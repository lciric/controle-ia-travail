# Proposition B — Tour III.1 : Conception ciblée

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut | Commentaire |
|---|---|---|---|
| 1 | Les deux sources (Argon, Opus 5.5) sont **indépendantes** au sens capture-recapture (probabilité de découvrir une famille pour l'une ne dépend pas de l'autre) | **HYPOTHÈSE** | Le fait 6 montre un lecteur unique de la lignée d'une source ; le fait 5 ne dit rien sur l'indépendance des données d'entraînement entre fournisseurs |
| 2 | La population de familles est **fermée** (nombre fini, fixe pendant l'énumération) | **HYPOTHÈSE** | Fait 9 note explicitement « hypothèse non satisfaite par des familles découvertes » ; rien n'empêche qu'une source invente une famille nouvelle |
| 3 | Chaque famille a la **même probabilité de capture** (homogénéité) | **HYPOTHÈSE** | Les familles combinées (fait 5 : 4 chez Argon, 3 chez Opus, aucune commune) suggèrent une hétérogénéité de complexité, donc de capturabilité |
| 4 | L'appariement par grille fermée est **exact** (ni faux positifs, ni faux négatifs) | **HYPOTHÈSE** | Fait 5-6 : appariement non bijectif (1→2), fait par un lecteur de la lignée d'une source ; aucune mesure d'accord inter-annotateurs n'est rapportée |
| 5 | Les bancs publics (fait 10-11) fournissent des **trajectoires étiquetables au niveau des familles** sous licence compatible | **HYPOTHÈSE** | Fait 11 le dit explicitement |
| 6 | Le régime « aveugle » et le régime « informé » (fait 1, N-056) produisent des **résultats comparables** entre eux | **HYPOTHÈSE** | Aucune mesure de l'écart n'existe dans les pièces |
| 7 | Cinq instances indépendantes suffisent pour un modèle capture-recapture multi-sources | **HYPOTHÈSE** | Aucun calcul de puissance n'est fourni |

---

## (b) Expériences décisives (duels H_A / H_B)

### Duel 1 — Estimation du nombre total de familles

**H_A :** Lincoln-Petersen (LP) avec deux sources donne une estimation non biaisée du nombre total N de familles (population fermée, sources indépendantes, capturabilité homogène).

**H_B :** Les hypothèses de LP sont violées (dépendance entre sources, hétérogénéité de capturabilité) et une borne inférieure de Chao (référence : Chao, 1987, « Estimating the population size for capture-recapture data with unequal catchability », *Biometrics*, 43(4), 783–791) donne une estimation significativement différente.

- **Métrique :** Biais relatif = (N̂ − N_vrai) / N_vrai, et intervalle de confiance à 95 % de chaque estimateur, mesurés sur des mondes simulés à vérité connue.
- **Seuil :** Si sur 1 000 mondes simulés avec hétérogénéité de capturabilité (coefficient de variation de la probabilité de capture > 0,3, illustratif), le biais relatif de LP dépasse 20 % (illustratif) dans plus de 50 % des cas tandis que Chao reste en dessous, H_A est falsifiée.
- **Contrôle négatif :** Mondes simulés où les hypothèses de LP sont satisfaites (sources indépendantes, capturabilité uniforme). Les deux estimateurs doivent alors converger (biais < 5 %, illustratif).
- **Issue qui falsifie H_A :** LP surestime systématiquement N dans les mondes hétérogènes. **Issue qui falsifie H_B :** Chao ne fait pas significativement mieux que LP même sous hétérogénéité, ce qui indiquerait que l'hétérogénéité n'est pas le facteur dominant.

### Duel 2 — Définition opérationnelle de l'universalité

**H_A :** L'universalité définie comme « pire cas sur la classe déclarée » (min_f∈F performance(f) ≥ τ) discrimine mieux les défenses que la définition par « proportion de familles au-dessus d'un seuil ».

**H_B :** La définition par proportion (« au moins 1 − ε des familles passent le seuil τ ») est plus informative parce que le pire cas est dominé par les familles extrêmes et instable avec peu de familles.

- **Métrique :** Puissance de discrimination — probabilité qu'un test sépare correctement une défense universelle d'une défense non universelle, mesurée sur des ensembles simulés de k familles (k ∈ {30, 60, 150}, illustratif) avec des distributions de performance connues.
- **Seuil :** Si la définition pire-cas nécessite plus de 3× le nombre de familles pour atteindre la même puissance (0,80, illustratif) que la définition par proportion, H_A est falsifiée (le pire cas est trop coûteux en données pour être praticable).
- **Contrôle négatif :** Une défense qui échoue sur exactement une famille sur k. Les deux définitions doivent la détecter comme non universelle.
- **Issue qui falsifie H_A :** Le pire cas ne discrimine pas avec k ≤ 60. **Issue qui falsifie H_B :** La proportion masque un effondrement sur une famille unique que le pire cas capte systématiquement.

### Duel 3 — Indépendance des sources

**H_A :** Les deux sources (Argon, Opus 5.5) sont effectivement indépendantes au sens capture-recapture.

**H_B :** Une dépendance positive existe (les mêmes familles « faciles à découvrir » sont trouvées par les deux), ce qui fait surestimer m et sous-estimer N.

- **Métrique :** Test d'indépendance sur la table 2×2 (découvert / non découvert par chaque source), chi² ou test exact de Fisher, sur les données réelles plus cinq sources supplémentaires (fait 4).
- **Seuil :** p < 0,05 du test d'indépendance.
- **Contrôle négatif :** Sources constituées par partition aléatoire d'un ensemble unique de familles (indépendance assurée par construction) ; le test ne doit pas rejeter.
- **Issue qui falsifie H_A :** Rejet de l'indépendance → LP invalide, recourir à des modèles log-linéaires multi-sources. **Issue qui falsifie H_B :** Non-rejet → LP reste un estimateur raisonnable (sous réserve d'homogénéité).

---

## (c) Mesure minimale de chaque instrument nommé

### Instrument 1 : Estimateur du nombre de familles

La base à battre est le **comptage brut** des familles observées (34 ou 35 selon la convention d'appariement, fait 7).

| Critère | Mesure minimale | Base à battre | Protocole |
|---|---|---|---|
| Biais | Biais relatif moyen sur ≥ 500 mondes simulés (illustratif) à N_vrai connu | Biais du comptage brut (toujours négatif, = −(N−n_obs)/N) | Varier N_vrai ∈ {30, 50, 80, 120} (illustratif), nombre de sources {2, 5}, hétérogénéité (CV de p_capture ∈ {0, 0.3, 0.6}, illustratif) |
| Couverture nominale | Proportion des IC à 95 % contenant N_vrai, sur 1 000 répliques (illustratif) | Le comptage brut ne produit pas d'IC ; base = 0 % de couverture | ≥ 90 % de couverture effective (illustratif) pour être retenu |
| RMSE | Racine de l'erreur quadratique moyenne | RMSE du comptage brut | L'estimateur retenu doit réduire le RMSE d'au moins 30 % (illustratif) sous hétérogénéité |

**Cas honnêtes appariés :** mondes simulés où les familles sont tirées avec probabilités de capture hétérogènes (distribution Beta(a,b), illustratif), avec le même nombre de sources que les données réelles.

### Instrument 2 : Mesure d'universalité

La base à battre est le **taux de détection moyen** sur les familles vues (sans pondération).

| Critère | Mesure minimale | Base à battre |
|---|---|---|
| Taux de détection (sensibilité) | Sur les familles tenues à l'écart : proportion où la défense atteint le seuil τ déclaré | Sensibilité sur les familles vues (entraînement) |
| Taux de fausses alertes | Proportion des éléments honnêtes classés comme sabotage, sur des éléments honnêtes appariés (même distribution de tâches, même longueur, même modèle) | Taux de fausses alertes d'un classificateur trivial (majorité ou seuil constant sur la base de log-perplexité) |
| Écart vu/écart | |Sensibilité_vues − Sensibilité_écart| | > 0,10 (illustratif) signale un manque d'universalité |

**Vérifications mécaniques à battre :** un moniteur qui ne lit que la longueur du texte et un classificateur log-perplexité (pas d'accès aux activations). Si la mesure d'universalité ne sépare pas ces vérifications triviales d'un moniteur entraîné, elle est non informative.

---

## Bloc 1 — Quatre propositions préalables

### 1(a) Définition opérationnelle de l'universalité (≤ 1 200 mots pour le bloc entier)

**Option α — Pire cas sur classe déclarée.** Énoncé : « Pour toute famille f dans la classe F déclarée avant la mesure, performance(défense, f) ≥ τ. » Avant la mesure : déclarer F (liste ou règle générative), τ, la métrique. Autorise : « la défense atteint τ sur chaque famille de F ». N'autorise pas : une affirmation sur des familles hors F. Vérification tiers : le tiers tire ou sélectionne des familles dans F, mesure, vérifie que le minimum empirique ≥ τ. Faiblesse : le pire cas empirique sous-estime le pire cas réel si |F| est grand et le nombre de familles testées petit ; instable pour k < 60 (cf. duel 2).

**Option β — Écart vu / tenu à l'écart.** Énoncé : « |perf_vue − perf_écart| ≤ δ avec probabilité 1 − α. » Avant : déclarer δ, α, le protocole d'affectation des familles. Autorise : « la défense ne se dégrade pas de plus de δ face à des familles inédites ». N'autorise pas : un quantificateur universel. Vérification tiers : fournir des familles inédites, mesurer l'écart. Force : directement interprétable comme généralisation. Faiblesse : dépend du mécanisme de découverte des familles tenues à l'écart ; si elles sont trop faciles, δ est trompeur.

**Option γ — Proportion au-dessus d'un seuil.** Énoncé : « Au moins 1 − ε de la population de familles F satisfait perf ≥ τ, avec confiance 1 − α. » Avant : déclarer ε, τ, α, la loi de tirage ou le mécanisme de découverte. Autorise : une affirmation probabiliste. N'autorise pas : un pire cas absolu. Vérification tiers : tirage ou énumération, comptage des succès, test binomial. Force : robuste aux valeurs aberrantes, calcul de taille d'échantillon standard (fait 9). Faiblesse : suppose un tirage représentatif ou un modèle de biais de sélection.

**Séparation « universelle sur classe déclarée » vs. « robuste à l'inconnu ».** La première est une affirmation conditionnelle à F : elle est falsifiable si on produit une famille dans F qui échoue. La seconde est une affirmation sur les familles hors F : elle n'est pas falsifiable sans hypothèse sur la distribution des familles inconnues. La seule passerelle est un modèle de population (capture-recapture, couverture de Good-Turing) qui estime la masse de probabilité des familles non observées.

**Recommandation :** Option γ comme définition primaire (puissance statistique suffisante avec k raisonnable), complétée par l'écart β comme diagnostic de généralisation.

### 1(b) Régime d'information

La question suppose que le régime (aveugle/informé) est bien défini et que les deux versions (fait 1, N-056) sont comparables — **HYPOTHÈSE**. Régime recommandé :

- **Aveugle :** le banc ne connaît ni les seuils ni les familles vues. Il produit des familles, les soumet, reçoit un verdict binaire. Avantage : pas de sur-ajustement du banc. Inconvénient : moins de puissance.
- **Informé :** le banc connaît le protocole de défense et les familles vues (pas les poids des sondes). Avantage : recherche adversariale ciblée. Inconvénient : risque de biais de confirmation.
- **Cloison :** la liste des familles d'entraînement, les seuils et les poids des sondes ne passent jamais vers les concepteurs de familles tenues à l'écart. Le protocole de mesure (métrique, format d'entrée/sortie) est partagé.
- **Budget :** au moins 100 éléments par famille (illustratif) pour stabiliser la sensibilité par famille à ±5 % (illustratif, intervalle de Clopper-Pearson).
- **Rapport par palier :** d'abord les familles vues (validation), puis les familles tenues à l'écart (test), sans retour en arrière.

### 1(c) Combien de familles, par simulation

**Énoncé cible :** Avec confiance 1 − α, la part de la population de familles où la défense échoue est inférieure à ε. Sous tirage i.i.d. et zéro échec, la formule du fait 9 s'applique : k ≥ ln α / ln(1 − ε). Pour ε = 0,05, α = 0,05 : k ≥ 59 (fait 9 : 58,40 → 59).

**Problèmes :**
1. *Les familles sont découvertes, non tirées :* la garantie est conditionnelle au mécanisme de découverte. Si les sources sous-représentent les familles difficiles, la borne est optimiste. La simulation peut démontrer la couverture *conditionnellement au modèle de population* (par ex. Beta-Binomial), mais **suppose** que ce modèle est correct — **HYPOTHÈSE**.
2. *Hétérogénéité entre familles :* la performance varie entre familles. Un modèle à deux niveaux (performance ~ Beta(a,b) entre familles, Binomial(n, p_f) entre éléments d'une famille) permet de calculer la variance totale. Avec un ICC élevé (>0,3, illustratif), il faut plus de familles et moins d'éléments par famille.
3. *Dépendance entre familles proches :* les familles combinées (fait 5) sont probablement corrélées. Regrouper par blocs et appliquer un test de permutation par blocs.
4. *Règle d'arrêt séquentielle :* un test séquentiel de proportion (par ex. mélange de séquences de Ville, référence à vérifier) permet de s'arrêter dès qu'on peut conclure, tout en contrôlant le taux d'erreur.

**Ce que la simulation peut démontrer :** la couverture de l'IC et le biais de l'estimateur sous le modèle de population choisi. **Ce qu'elle suppose :** le modèle de population et la représentativité du mécanisme de découverte.

### 1(d) Combien de familles encore inconnues

**Vérification des calculs :** LP avec m = 18 : 28 × 25 / 18 = 700/18 = 38,889 → **correct**. LP avec m = 19 : 700/19 = 36,842 → **correct**. Chapman avec m = 18 : (29 × 26)/19 − 1 = 754/19 − 1 = 39,684 − 1 = 38,684 → **correct**. Chapman avec m = 19 : 754/20 − 1 = 37,70 − 1 = 36,70 → **correct**. Les calculs du fait 8 sont vérifiés.

**Convention d'appariement :** m = 18 (côté Argon) ignore la non-bijectivité ; m = 19 (côté Opus) la corrige partiellement. La convention m = 19 se défend mieux car elle reflète le nombre effectif de paires concordantes observées côté Opus — la famille Argon qui recouvre deux familles Opus fournit bien deux appariements distincts. Mais LP suppose un appariement bijectif ; la non-bijectivité viole le modèle. Ni l'une ni l'autre ne sont pleinement satisfaisantes.

**Hypothèses et direction du biais :**
- *Dépendance positive entre sources :* inflat m → sous-estime N. Probable ici (même question, données d'entraînement partiellement recouvrantes entre LLMs).
- *Hétérogénéité de capturabilité :* les familles faciles sont sur-représentées dans l'intersection → LP sous-estime N. Chao (1987, op. cit.) corrige en utilisant les singletons : N̂_Chao ≥ N̂_LP.
- *Erreur d'appariement :* faux appariements (faux positifs) surestiment m → sous-estiment N. Faux négatifs sous-estiment m → surestiment N. Direction nette indéterminée sans mesure de l'accord.
- *Population non fermée :* si de nouvelles familles peuvent être inventées, N n'est pas défini sans contrainte temporelle ; la couverture de Good-Turing (C = 1 − f₁/n, où f₁ est le nombre de familles vues une seule fois) est plus pertinente que N̂.

**Estimateurs multi-sources :** Avec cinq sources (fait 4) : modèles log-linéaires sur la table 2⁵ (Cormack, 1989, « Log-linear models for capture-recapture », *Biometrics*, 45(2), 395–413 ; référence à vérifier pour les pages exactes), avec sélection de modèle (AIC/BIC) pour tester l'indépendance. Classes latentes si l'indépendance conditionnelle suffit. Approche bayésienne : prior sur N, actualisation par les données multi-sources (Castledine, 1981, référence à vérifier).

**Refus commun :** Si plusieurs sources refusent de produire certaines familles (même censure), les familles censurées sont invisibles à toutes les sources, ce qui crée une masse inobservable. Modéliser par une probabilité de censure π₀ ; N_observable = N(1 − π₀) ; l'estimateur ne porte que sur la partie observable. Documenter la question posée et les motifs de refus.

---

## Bloc 3 — Questions candidates pour le texte III

### Q1 — Couverture estimée par capture-recapture multi-sources

*Mesurer la couverture de Good-Turing et l'estimation de N par modèle log-linéaire sur cinq sources indépendantes.*

1. **Avantage :** exploite les cinq sources prévues (fait 4) pour estimer la masse manquante sans hypothèse de capturabilité uniforme.
2. **Piège :** si les sources partagent les mêmes données d'entraînement, l'indépendance est violée et le modèle log-linéaire sous-estime N.
3. **Validation extérieure :** confronter la prédiction de masse manquante à des familles extérieures (≥ 10 familles, illustratif) provenant de bancs publics ; si la proportion de familles extérieures non appariées aux familles connues tombe dans l'IC prédit, l'estimateur est calibré.
4. **Risque hors périmètre :** faible — ne décrit aucun comportement, seulement des estimateurs et des tests d'indépendance.

### Q2 — Écart de performance vu / tenu à l'écart comme mesure de généralisation

*Borner l'écart |sensibilité_vue − sensibilité_écart| et tester s'il est significativement différent de zéro.*

1. **Avantage :** mesure directe de l'universalité (option β), interprétable comme sur-ajustement de la défense.
2. **Piège :** si les familles tenues à l'écart sont systématiquement plus faciles que les familles vues, l'écart est trompeur dans le sens optimiste.
3. **Validation extérieure :** prédiction scellée de l'écart (par ex. δ ≤ 0,10, illustratif) confrontée à ≥ 15 familles extérieures (illustratif).
4. **Risque hors périmètre :** faible — métrique de performance sans description de comportement.

### Q3 — Calibration du test binomial de proportion sous découverte non aléatoire

*Estimer la sensibilité du test « zéro échec sur k familles → ε < ε₀ » lorsque les familles sont découvertes et non tirées.*

1. **Avantage :** quantifie la perte de garantie due au biais de sélection dans la découverte.
2. **Piège :** requiert un modèle de biais de sélection ; si le modèle est mal spécifié, la correction est pire que le test naïf.
3. **Validation extérieure :** simulation avec vérité connue (mondes simulés), comparaison de la couverture effective à la couverture nominale sur ≥ 500 répliques (illustratif).
4. **Risque hors périmètre :** faible — purement statistique.

### Q4 — Accord inter-annotateurs sur l'appariement de familles

*Mesurer l'accord (kappa de Cohen ou kappa de Fleiss) entre plusieurs lecteurs indépendants sur l'appariement de familles, et borner l'erreur d'appariement dans l'estimateur de N.*

1. **Avantage :** le fait 6 montre un lecteur unique ; quantifier l'erreur d'appariement est un préalable à tout estimateur de N.
2. **Piège :** si les lecteurs partagent les mêmes biais (même famille de modèles), le kappa surestime l'accord réel.
3. **Validation extérieure :** trois lecteurs de fournisseurs différents (illustratif), kappa ≥ 0,70 (illustratif) pour considérer l'appariement fiable.
4. **Risque hors périmètre :** faible — mesure d'accord sur des étiquettes, pas de contenu.

### Q5 — Puissance du plan d'évaluation en fonction du nombre de familles et d'éléments par famille

*Calculer la puissance du test d'universalité (option γ) en fonction de k (familles) et n (éléments/famille), sous un modèle hiérarchique Beta-Binomial.*

1. **Avantage :** permet de dimensionner le banc avant de le construire.
2. **Piège :** la spécification du modèle hiérarchique (paramètres a, b) est arbitraire sans données pilotes.
3. **Validation extérieure :** prédiction de la variance inter-familles confrontée aux données des cinq sources (≥ 30 familles au total, illustratif).
4. **Risque hors périmètre :** faible — calcul de puissance, pas de contenu.

---

## Bloc 4 — Organisation des cinq instances

### Consigne (même ou différente)

**Options :** (i) même consigne exacte ; (ii) consignes avec variations contrôlées (par ex. niveau de contrainte). **Recommandation :** même consigne. Avantage : les différences proviennent des modèles, pas des instructions ; nécessaire pour les modèles capture-recapture (même probabilité *a priori* d'être soumis à chaque famille). Inconvénient : réduit la diversité intentionnelle. Confiance : moyenne — **HYPOTHÈSE** que la même consigne assure la comparabilité.

### Prévention des fuites

**Options :** (i) scellement cryptographique (hash horodaté) avant soumission ; (ii) exécution en environnement isolé sans réseau. **Recommandation :** les deux. Chaque instance soumet le hash SHA-256 de sa liste de familles à un tiers de confiance avant que toute autre instance ne soit consultée. Avantage : vérifiable post-hoc. Inconvénient : ne protège pas contre les fuites via les données d'entraînement partagées. Confiance : élevée sur le protocole, faible sur la contamination des données — **HYPOTHÈSE** que les données d'entraînement sont suffisamment différentes.

### Appariement sans biais de lecteur unique

**Options :** (i) panel de trois lecteurs (modèles de fournisseurs différents, aucun de la lignée des sources), vote majoritaire ; (ii) appariement automatique par similarité textuelle des schémas de construction (embedding + seuil), validé par un lecteur humain. **Recommandation :** option (i) avec mesure du kappa de Fleiss (cf. Q4). Avantage : corrige le biais identifié au fait 6. Inconvénient : coût de trois passes. Confiance : moyenne — **HYPOTHÈSE** que des modèles de fournisseurs différents ont des biais d'appariement indépendants.

### Test d'indépendance

Construire la table de contingence 2⁵ (cinq sources × découvert/non-découvert). Tester l'indépendance par les interactions d'ordre ≥ 2 dans un modèle log-linéaire (Cormack, 1989, référence citée ci-dessus). Si des paires de sources partagent le même fournisseur de données d'entraînement, regrouper ces paires et tester l'indépendance conditionnelle. Confiance : élevée sur le test, **HYPOTHÈSE** sur la connaissance des données d'entraînement.

### Utilisation comme sources multiples pour l'estimation

Avec cinq sources et l'appariement multi-lecteurs, ajuster un modèle M_t (hétérogénéité temporelle, ici : hétérogénéité de source) ou M_h (hétérogénéité de famille). Sélection par AIC. La borne inférieure de Chao multi-sources (Chao & al., 2001, « An overview of closed capture-recapture models », *Journal of Agricultural, Biological, and Environmental Statistics*, 6(2), 158–175 ; référence à vérifier pour pages exactes) sert de plancher. Confiance : moyenne — cinq sources est un minimum pour des modèles à plus de deux paramètres.

### Refus d'une instance

**Si une instance refuse :** (i) documenter le motif et la question posée ; (ii) ne pas reformuler (fait 14, cohérence avec le protocole du collisionneur) ; (iii) traiter cette source comme censurée dans le modèle capture-recapture (probabilité de capture = 0 pour cette source sur toutes les familles) ; (iv) si deux instances ou plus refusent, le plan à cinq sources perd sa puissance — prévoir deux instances de remplacement (fournisseurs différents, **HYPOTHÈSE** sur leur disponibilité). Confiance : faible — le protocole dépend de la coopération de fournisseurs tiers.

---

## Bloc 2 — Données de départ à recommander

Je ne dispose pas d'informations fiables sur le format, la licence ou le schéma d'étiquetage de SHADE-Arena, ControlArena, MonitoringBench, SLEIGHT-Bench ni Liars' Bench. Le fait 10 confirme leur existence nominale dans les documents du programme ; le fait 11 marque comme **HYPOTHÈSE** leur étiquetabilité et leur compatibilité de licence. **Je ne connais pas ces bancs suffisamment pour décrire leurs propriétés de format ou de licence ; toute description serait inventée.**

**Recommandation générale :** (i) les journaux de refus (fait 12) sont les plus indépendants du programme car ils documentent ce que le programme *n'a pas fait* — utiles comme source supplémentaire de capture-recapture (les refus révèlent des familles non explorées) ; (ii) les propositions brutes d'une course précédente (fait 12) fournissent une troisième source d'énumération, mais leur indépendance vis-à-vis des deux premières sources est douteuse (même contexte de conception) ; (iii) un seul banc public, choisi après vérification de sa licence et de son étiquetage au niveau des familles, comme source extérieure maximalement indépendante. Coût de mise au format : **HYPOTHÈSE** — non estimable sans accès aux données.

---

## (d) Ancrage matériel

Modèles ouverts 8B et 70B (fait 3, RAPPORTÉ). Simulations capture-recapture (1 000 mondes × 5 sources) : calcul CPU négligeable (< 1 h sur un poste standard, illustratif). Évaluation des défenses sur familles tenues à l'écart (100 éléments × 60 familles × 2 modèles) : ≈ 12 000 inférences ; sur 70B en FP16, ≈ 40 GPU-heures A100 (illustratif). Coût total estimé : < 500 USD en location cloud (illustratif).

FIN-DE-CELLULE
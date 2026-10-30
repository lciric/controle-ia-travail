

# Proposition B — Tour III.3 : Réponse aux critiques et page finale

---

## (a) Traitement critique par critique

Je ne traite que les critiques visant B, issues des propositions A, C et D. Chaque critique est acceptée, rejetée avec raison, ou transformée en test.

### Critiques de A sur B

**A.1 — Contradiction sur le signe du biais de LP (Duel 1).** *Acceptée.* Le bloc 1(d) affirme correctement que l'hétérogénéité sous-estime N (dépendance positive gonflant m) ; l'issue falsifiante du duel 1 indiquait « LP surestime », ce qui est incohérent. Le duel est corrigé ci-dessous.

**A.2 — Duel 2, vrai par construction.** *Acceptée partiellement.* Le reproche est juste : comparer deux définitions sur leur propre critère est circulaire. Cependant, la question pertinente subsiste : à budget fixe de familles, quelle définition produit un test d'universalité plus puissant ? Le duel est reformulé avec un estimand commun (la probabilité de détecter une défense non universelle, définie extérieurement).

**A.3 — Duel 3, table 2×2 inidentifiable et contrôle négatif erroné.** *Acceptée.* Avec deux sources, la cellule (0,0) est inobservable ; le χ² est impossible. Le contrôle par partition produit des listes disjointes, pas indépendantes. Le duel 3 est reformulé pour cinq sources et le contrôle est remplacé par un tirage Bernoulli indépendant sur population connue.

**A.4 — Fuite entre régime informé et cloison.** *Acceptée.* La distinction entre banc et concepteurs de familles était implicite. Corrigé : le banc informé est une procédure automatisée recevant le protocole de défense ; les concepteurs de familles tenues à l'écart ne sont jamais le banc informé et n'ont jamais accès aux familles vues.

**A.5 — Convention m=19 avec n₁=28 : unités incohérentes.** *Acceptée.* La remarque de C est formellement décisive (voir C.3 ci-dessous). Le calcul doit être fait dans une unité cohérente. Corrigé en adoptant le recodage en grain grossier.

**A.6 — Budget par famille arithmétiquement faux.** *Acceptée.* À p̂=0,5, 100 éléments donnent ±0,10, non ±0,05. Pour ±0,05 bilatéral (Clopper-Pearson), il faut ≈385 éléments (illustratif). Le budget est corrigé à 400 éléments par famille (illustratif).

**A.7 — Q1 et Q2, confusion calibration/déplacement de loi.** *Transformée en test.* L'objection est que des familles extérieures suivent une loi de découverte différente des sources internes, donc un désaccord ne distingue pas « N̂ mal calibré » de « loi différente ». *Test :* Prédiction scellée portant sur la *couverture de Good-Turing* (proportion de familles extérieures déjà connues), non sur N̂. Si la couverture prédite est compatible avec l'observée à ±0,15 (illustratif), le modèle est transportable ; sinon, documenter l'écart comme mesure du déplacement de loi.

**A.8 — Q4, kappa inadapté à un graphe biparti non bijectif.** *Acceptée.* Le kappa porte sur des étiquettes catégorielles, pas sur des arêtes de graphe. Corrigé : remplacer par un accord au niveau des arêtes (proportion d'arêtes concordantes entre lecteurs, pondérée par le nombre d'arêtes candidates), complété par le taux de faux liens et de liens manqués sur un jeu d'étalonnage à vérité connue.

**A.9 — Fuite instrument 2 : éléments honnêtes pour seuils et fausses alertes.** *Acceptée.* Les seuils doivent être fixés sur un jeu de calibration disjoint du jeu de mesure des fausses alertes. Ajouté explicitement.

### Critiques de C sur B

**C.1 — Contradiction Duel 1 (direction du biais LP).** *Acceptée* (même que A.1). Corrigé.

**C.2 — Contrôle négatif du Duel 2 incompatible avec H_B (1/60 passe ε=0,05).** *Acceptée.* Le contrôle exigeant rejet par les deux définitions est incohérent quand ε>0. Corrigé : le contrôle négatif utilise une défense dont le taux d'échec réel est exactement ε (par construction dans un monde simulé) ; les deux définitions doivent rendre un verdict à leur propre niveau, sans concordance imposée.

**C.3 — m=19 avec n₁=28 : division pommes/demi-pommes.** *Acceptée.* L'argument formel est irréfutable : LP suppose une algèbre d'événements commune. *Solution retenue :* recodage en grain grossier (fusionner les deux familles Opus en une, aligné sur Argon) → n₁=28, n₂=24, m=18, LP=37,3, Chapman=36,7 (calcul refaisable : 28×24/18=37,33 ; 29×25/19−1=37,16). L'alternative (grain fin, éclater la famille Argon → n₁=29, n₂=25, m=19) doit être rapportée en parallèle. *Les deux conventions sont des HYPOTHÈSES sur la granularité des familles.*

**C.4 — Confusion censure/capture pour les journaux de refus.** *Acceptée.* Un refus de répondre ne produit pas une observation de famille étiquetée. Les journaux de refus ne sont pas une source de capture-recapture. Corrigé : ils sont utilisés uniquement pour estimer un taux de censure par fournisseur (proportion de questions refusées), qui entre comme paramètre de sensibilité dans le modèle de population, pas comme colonne de la matrice d'incidence.

**C.5 — Instabilité de Chao sous faux négatifs d'appariement.** *Transformée en test.* C montre formellement que f₁²/f₂ explose quand les faux négatifs détruisent des doublets et créent des singletons. *Test :* sur des mondes simulés à vérité connue, injecter un bruit d'appariement calibré à κ=0,70 (seuil retenu) et mesurer le biais de Chao2. Si le biais dépasse 50 % (illustratif) de N_vrai, le seuil κ=0,70 est insuffisant et doit être relevé.

**C.6 — Non-identifiabilité de Δ_réel sous déplacement de difficulté.** *Acceptée.* L'écart vu/écart confond sur-ajustement et différence de difficulté entre mécanismes de découverte. *Correction :* l'écart β n'est retenu que comme diagnostic, pas comme définition primaire. La définition primaire reste la proportion γ, mesurée sur les familles tenues à l'écart *sous leur propre loi de découverte*, avec le caveat explicite que cette loi est conditionnelle au mécanisme.

**C.7 — Sous-couverture du modèle Beta-Binomial sous distribution bimodale.** *Transformée en test.* *Test :* simuler un monde bimodal (fraction ε_vrai de familles à p=0,10, reste à p=0,98, illustratif) et mesurer la couverture du calcul de puissance Beta-Binomial. Si la couverture effective < 0,50 (illustratif), ajouter un modèle de mélange discret comme alternative.

### Critiques de D sur B

**D.1 — Duel 1 teste la robustesse, pas la validité de LP.** *Acceptée* (convergent avec A.1). Reformulé.

**D.2 — Contrôle Duel 2 contredit la proportion.** *Acceptée* (convergent avec C.2). Reformulé.

**D.3 — Test d'indépendance à deux sources inapplicable ; partition inadéquate.** *Acceptée* (convergent avec A.3). Reformulé pour cinq sources.

**D.4 — Convention m=19 sans recodage cohérent.** *Acceptée* (convergent avec A.5/C.3).

**D.5 — Journaux de refus ne sont pas une source de capture.** *Acceptée* (convergent avec C.4).

**D.6 — Familles extérieures ne calibrent Good-Turing que sous même loi.** *Transformée en test* (convergent avec A.7).

**D.7 — Kappa mesure l'accord, pas l'exactitude.** *Acceptée.* Complété par le contrôle sur jeu à vérité connue (taux de faux liens et liens manqués).

**D.8 — Plan Beta-Binomial fragile sous loi discrète/multimodale.** *Transformée en test* (convergent avec C.7).

---

## (b) Expériences corrigées

### Duel 1 corrigé — Estimation de N : LP/Chapman vs Chao2, cinq sources

**H_A :** Sous le régime réel (hétérogénéité probable, dépendance possible), Chapman à cinq sources fournit un estimateur dont le biais relatif est ≤10 % (illustratif) et dont l'IC à 95 % couvre N_vrai.

**H_B :** L'hétérogénéité et la dépendance entre sources font que Chapman sous-estime N ; la borne inférieure Chao2 corrigée (Chao, 1987) fournit un plancher plus fiable, c'est-à-dire que Chao2 ≤ N_vrai avec probabilité ≥ 0,95 là où Chapman échoue.

- **Métrique :** (i) Biais relatif (N̂−N_vrai)/N_vrai ; (ii) Taux de couverture de l'IC à 95 % ; (iii) Propriété de borne : P(Chao2 ≤ N_vrai).
- **Seuil :** Sur ≥1000 mondes simulés avec CV de p_capture ∈ {0,3 ; 0,6} (illustratif) et odds-ratio de dépendance entre paires de sources ∈ {1,5 ; 3,0} (illustratif) : si la couverture de Chapman < 0,85 (illustratif) dans plus de 50 % des scénarios, H_A falsifiée. Si Chao2 > N_vrai dans plus de 10 % des scénarios (illustratif), H_B falsifiée (la propriété de borne est perdue).
- **Contrôle négatif :** (a) Monde homogène, sources indépendantes : les deux estimateurs convergent, biais < 5 %, couverture ≥ 0,93 (illustratif). (b) Monde sans masse manquante (N = n_obs) : les deux estimateurs rendent ≈ n_obs.
- **Contrôle d'appariement :** Injecter un bruit d'appariement (taux de faux négatifs calibré à κ=0,70) et mesurer l'inflation de Chao2.

### Duel 2 corrigé — Puissance comparative des définitions d'universalité

**H_A :** La définition par proportion (γ : « au moins 1−ε des familles passent τ ») détecte une défense non universelle (taux d'échec réel = 2ε, illustratif) avec une puissance ≥ 0,80 en utilisant k ≤ 60 familles (illustratif).

**H_B :** La définition par pire cas (α : min_f perf(f) ≥ τ) détecte la même défense non universelle avec une puissance ≥ 0,80 en utilisant k ≤ 60 familles.

- **Estimand commun :** probabilité de rejeter correctement l'universalité pour une défense dont le taux d'échec réel est fixé à 2ε.
- **Métrique :** Puissance empirique sur ≥ 1000 répliques, pour k ∈ {30, 60, 90} (illustratif).
- **Seuil :** Si une définition atteint 0,80 de puissance à k=60 et l'autre non, celle qui échoue est falsifiée comme praticable dans ce régime.
- **Contrôle négatif :** Défense réellement universelle (taux d'échec = 0) : les deux définitions acceptent, taux de fausse alarme ≤ α déclaré.
- **Issue qui falsifie H_A :** La proportion ne rejette pas à k=60 parce que les échecs sont trop dilués. **Issue qui falsifie H_B :** Le pire cas est instable (variance trop élevée) et rejette des défenses universelles.

### Duel 3 corrigé — Indépendance des sources, cinq sources

**H_A :** Les cinq sources sont conditionnellement indépendantes étant donné un effet d'hétérogénéité de famille (modèle M_h).

**H_B :** Des dépendances résiduelles entre sources (par lignée de fournisseur) subsistent au-delà de l'hétérogénéité (interactions d'ordre 2 dans le modèle log-linéaire).

- **Métrique :** ΔAIC entre modèle M_h (effets principaux seuls) et modèle M_h + interactions par paires de lignée.
- **Seuil :** ΔAIC > 4 (illustratif) en faveur du modèle avec interactions → H_A falsifiée.
- **Contrôle négatif :** Cinq listes générées par tirages Bernoulli indépendants sur une population de N=40 (illustratif) avec hétérogénéité Beta(2,5) (illustratif) : le test ne doit pas rejeter M_h (ΔAIC < 2, illustratif).
- **Contrôle positif :** Deux listes issues du même modèle (même tirage Bernoulli dupliqué + bruit) : le test doit détecter la dépendance.
- **Limite :** Avec N≈40 et 2⁵−1=31 cellules, les effectifs sont faibles ; utiliser un test de rapport de vraisemblance avec correction pour petits effectifs ou bootstrap paramétrique (référence à vérifier).

---

## (c) Page de réponse à la question de l'arbitre

### Définition retenue

**Option γ (proportion au-dessus d'un seuil)** comme définition primaire : « Avec confiance 1−α, la part de la population de familles où la défense échoue est inférieure à ε. » Cette définition est falsifiable, dimensionnable, et vérifiable par un tiers via un test binomial (ou sa généralisation hiérarchique). Elle est complétée par l'écart β (|perf_vue − perf_écart|) comme diagnostic de généralisation, avec le caveat que cet écart confond sur-ajustement et déplacement de difficulté (critique de C acceptée). La séparation entre « universelle sur la classe déclarée » et « robuste à l'inconnu » passe par un modèle de couverture (Good-Turing ou Chao2) dont les hypothèses sont explicites et testables, mais non démontrées.

### Estimateur retenu

**Chao2 à cinq sources** comme borne inférieure du nombre total de familles, complété par Chapman comme estimateur ponctuel. Convention d'unité : grain grossier (fusion des scissions côté Opus pour aligner sur Argon), avec rapport parallèle en grain fin. L'incertitude d'appariement est propagée par mesure du taux de faux liens sur un jeu d'étalonnage, non par imputation multiple (critique de C sur Rubin acceptée indirectement). L'indépendance des sources est testée par modèle log-linéaire parcimonieux (interactions par lignée seulement, 1 à 2 ddl).

### Questions candidates révisées (cinq)

**Q1.** *Estimer la couverture et la borne inférieure de N par Chao2 multi-sources sur cinq instances, et calibrer par simulation sous hétérogénéité et dépendance.* Validation : simulation à vérité connue (≥1000 mondes), incluant un monde sans masse manquante et un monde avec bruit d'appariement κ=0,70.

**Q2.** *Borner l'écart de performance vu/écart et tester s'il est distinguable du déplacement de difficulté.* Validation : prédiction scellée de l'écart, confrontée à ≥15 familles extérieures (illustratif), avec covariable de difficulté indépendante de la défense si disponible.

**Q3.** *Mesurer la sensibilité du test binomial « zéro échec → ε < ε₀ » au biais de découverte, sous un modèle de sélection paramétrique.* Validation : couverture effective vs. nominale sur ≥500 mondes simulés, incluant un monde bimodal.

**Q4.** *Mesurer le taux de faux liens et de liens manqués de l'appariement multi-lecteurs sur un jeu d'étalonnage à vérité connue, et propager cette erreur dans l'estimateur de N.* Validation : trois lecteurs de fournisseurs différents, accord au niveau des arêtes ≥0,80 (illustratif) ; contrôle sur liste-copie (m attendu = n) et listes sans lien (m attendu = 0).

**Q5.** *Calculer la puissance du plan d'évaluation (définition γ) en fonction de k familles et n éléments par famille, sous un modèle hiérarchique incluant un mélange discret comme alternative au Beta-Binomial.* Validation : confronter la variance inter-familles prédite aux données des cinq sources.

### Organisation des cinq instances (cinq lignes)

1. **Consigne :** même consigne exacte pour les cinq instances, nécessaire à la comparabilité capture-recapture ; les différences proviennent des modèles.
2. **Anti-fuites :** chaque instance soumet le hash SHA-256 de sa liste à un tiers de confiance avant que toute autre instance ne soit consultée ; exécution sans réseau.
3. **Appariement :** panel de trois lecteurs de fournisseurs différents (aucun de la lignée des sources), accord mesuré au niveau des arêtes du graphe biparti sur un jeu d'étalonnage à vérité connue ; taux de faux liens et liens manqués rapportés.
4. **Indépendance :** modèle log-linéaire parcimonieux (interactions par lignée seulement) sur la table 2⁵, avec contrôle négatif par Bernoulli indépendant et contrôle positif par duplication.
5. **Refus :** documenter le motif, ne pas reformuler, traiter comme censure dans le modèle de population (paramètre de sensibilité π₀), prévoir deux instances de remplacement de fournisseurs différents.

### Ce qui est établi, ce qui ne l'est pas

**Établi (VÉRIFIÉ) :** les calculs LP et Chapman sous les deux conventions (fait 8) ; la borne à zéro échec et ses limites (fait 9) ; l'existence de 34–35 familles observées ; la non-bijectivité de l'appariement et le lecteur unique de lignée partiale (faits 5–7).

**Non établi (HYPOTHÈSE) :** l'indépendance des sources ; l'homogénéité de capturabilité ; la fermeture de la population ; l'exactitude de l'appariement ; la représentativité des familles découvertes ; la transportabilité de la couverture de Good-Turing vers des sources extérieures ; la spécification correcte du modèle Beta-Binomial.

**Expérience à faire en premier :** La simulation de calibration des estimateurs de N (Duel 1 corrigé). Elle ne nécessite aucune donnée supplémentaire, seulement du calcul CPU (< 1 h, illustratif), et elle tranche la question préalable à toutes les autres : dans quel régime d'hétérogénéité et de dépendance Chapman et Chao2 sont-ils fiables, et à partir de quelle erreur d'appariement Chao2 perd sa propriété de borne ? Sans cette réponse, aucun dimensionnement du plan d'évaluation n'est fondé.

FIN-DE-CELLULE
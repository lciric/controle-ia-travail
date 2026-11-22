# Proposition F — Tour III.3 : réponse aux critiques

**Audit des pièces transmises (règle 2).** Les blocs `FAITS`, `QUESTION DE L'ARBITRE`, ma conception `E3-T1-conception-F` et les cinq critiques croisées `A`, `B`, `C`, `D` et `E` sont tous présents, non vides et complets jusqu'à leur marqueur de fin (`VÉRIFIÉ`). Le bloc `FAITS` ne contient que le texte de la question, sans donnée empirique (`VÉRIFIÉ`). Je ne réponds ci-dessous qu'aux passages visant la proposition F. Les statuts apposés dans les pièces antérieures ne sont pas modifiés ; dans la présente réponse, seuls les constats de lecture des pièces portent `VÉRIFIÉ`, les références citées de mémoire portent `RAPPORTÉ`, toute proposition empirique ou de méthode porte `HYPOTHÈSE`, et les implications mathématiques conditionnelles sont distinguées comme telles. Tous les chiffres hors `FAITS` sont marqués `illustratif`.

---

## (a) Traitement critique par critique des objections visant F

### Critiques de A (section §0 sur les statuts et section « Sur la proposition F »)

1. **§0 — Apposition de `VÉRIFIÉ` sur des énoncés absents de `FAITS`** : **Acceptée.** Ma conception T1 plaçait `VÉRIFIÉ` sur des dérivations logiques et des propriétés d'architecture hors `FAITS`. Je réserve désormais `VÉRIFIÉ` aux seuls constats directs sur les pièces transmises et distingue explicitement les identités mathématiques conditionnelles des résultats empiriques.
2. **G4 double (porte de qualification sur B1 et gain mesuré sur le sous-ensemble jugé défendable)** : **Acceptée.** Conditionner l'évaluation sur les échecs du texte et des règles mécaniques annule par construction leur TPR et gonfle le gain interne ; réutiliser B1 pour qualifier puis évaluer crée une fuite. Corrigé en (b) : juge de qualification distinct `J_qual` gelé sur développement et critère principal mesuré sur la **population test complète**.
3. **`AUROC_intra` confondue avec le type de pas (embranchement vs routine)** : **Acceptée.** Le témoin H4 de T1 ne contrôlait pas ce confondant. Corrigé en (b) par un contraste exogène de conflit ($U_t \in \{0,1\}$) à l'intérieur des seuls créneaux pivots ($C_t=1$) et par une différence de différences contre les agents honnêtes.
4. **Étiquette $S$ non définie et risque de lecture post-action** : **Acceptée.** Corrigé en (b) par un prélèvement strictement **pré-choix** (emprunté à D) et une définition exogène de $U_t$ fixée par le générateur avant toute exécution.
5. **E1 par invite exposée à G7 ($I(G ; h_t \mid c_t) = 0$ à poids $\theta$ fixés)** : **Transformée en test.** L'identité informationnelle conditionnelle à $c_t$ complet est exacte ; toutefois, comme A l'indique dans ses conditions de révision, elle ne tranche pas le gain sous lecteur de capacité bornée ni le régime sans invite. Je la transforme en double test en (b) : (i) en E1, contraste intra-trajectoire $U_t$ à invite strictement identique + comparaison à un **auto-lecteur** $\theta_0$ (emprunté à A et C) relisant $x_{1:t}$ sans invite, face à une consigne inerte (`H4-ter`) et une consigne active bénigne (`H4-bis`) ; (ii) en E3, suppression totale de l'invite et de tout déclencheur.
6. **E3 — Asymétrie d'optimisation du saboteur RL contre un auditeur textuel** : **Transformée en test.** Plutôt que de supposer un seul régime RL, E3 est scindée en deux bras : `E3a` sans auditeur textuel ni sonde dans la boucle RL (contrainte mécanique M1 seule), et `E3b` où saboteur et honnête subissent tous deux la même pénalité d'un auditeur externe distinct de `I2`.
7. **E3 — Un seul entraînement RL par classe (G2 malgré H5)** : **Acceptée.** Corrigé par $K = 4$ adaptateurs indépendants par classe (`illustratif`), évaluation croisée hors-adaptateur et test de disqualification sur texte neutre hors tâche (emprunté à A).
8. **E4 — Confusion régime × origine × tâche, $H_{4B}$ disjonctive, zone `[0,10 ; 0,40]` (`illustratif`) non attribuée** : **Acceptée.** Corrigé en (b) par un plan factoriel 2 × 2 (Régime A/B × Origine Invite/RL) sur schéma de tâche identique et par un couple $H_{4A}/H_{4B}$ complémentaire.
9. **Puissance de M2 et M3 fixée par un paramètre du générateur en Régime A** : **Rejetée.** Pour M2, la courbe de spécification est ré-exécutée *instance par instance* : la randomisation du signe des effets entre instances ne réduit pas sa puissance (seule la dispersion $\sigma_{\text{multivers}}$ relative à $\Delta_0$ la gouverne, désormais stratifiée). Pour M3, sa perte de puissance en Régime A n'est pas un biais artificiel : elle traduit précisément la frontière entre biais heuristique fixe (Régime B) et sabotage contingent (Régime A).
10. **Puissance statistique (G6 à $\text{FPR} \le 0,01$, conversion pas $\to$ trajectoire par indépendance, puissance de $\Delta\text{TPR}$ sur 200 positifs, instabilité du ratio $R/\max(\delta_{\text{hon}}, 0,01)$, bruit d'`AUROC_intra`)** : **Acceptée** sur les cinq sous-points. Corrigé en (b) : abandon du critère primaire à `1 %` (`illustratif`) au profit de `5 %` (`illustratif`) par pire strate avec effectifs augmentés ; estimation de $\rho$ et $n_{\text{eff}}$ sur trajectoires honnêtes entières ; remplacement du ratio causal par des seuils absolus ; centrage intra-trajectoire des scores sur `6` créneaux pivots (`illustratif`) avant mise en commun.

### Critiques de B (« Sur la proposition F »)

1. **Sélection sur l'échec du comparateur et réutilisation de B1 entre qualification et I2** : **Acceptée** (même correction qu'A2, avec `J_qual` distinct de `I2`).
2. **`AUROC_intra` confondue avec les embranchements ; H4 inopérant** : **Acceptée** (même correction qu'A3).
3. **E1 — Interaction consigne × embranchement** : **Acceptée.** J'intègre directement le témoin proposé par B — **biais instruit déclaré** (`H4-bis`), actif aux mêmes créneaux pivots sans dissimulation — couplé au contraste exogène $U_t$ à $C_t=1$ constant.
4. **Divergence de références (*AI Control* et Levinstein & Herrmann)** : **Acceptée.** Sans vérification documentaire accessible ici, ces deux références sont reclassées `référence à vérifier` conformément à la règle 3.
5. **Non-jugeabilité du $\text{FPR} \le 0,01$ (`illustratif`) sur 400 témoins, perte de puissance du maximum si $|S|$ est petit, et discontinuité du plancher `0,01` (`illustratif`) dans le ratio causal** : **Acceptée.** Corrigé en (b) : $\text{FPR} = 0,05$ (`illustratif`) par strate, agrégation par moyenne sur les `6` créneaux pivots $C_t=1$ (`illustratif`) au lieu du maximum sur $T$ pas, et critères absolus en E2.
6. **Perte de puissance de M2 « si la dispersion de la loi des estimateurs est petite devant $\Delta$ »** : **Rejetée (sur le sens de l'inégalité).** C'est l'inégalité inverse qui annule M2 : si $\sigma_{\text{multivers}} \ll \Delta$, un écart $\Delta$ se situe dans la queue extrême (ou hors support) des spécifications standards, rendant M2 très puissant ; M2 perd sa puissance lorsque $\sigma_{\text{multivers}} \gg \Delta$. Je paramètre désormais explicitement ce ratio $\kappa = \Delta_0 / \sigma_{\text{multivers}}$ en deux strates.
7. **E4 — Confusion régime / amplitude si les lois de $\Delta$ diffèrent entre B et témoin biaisé** : **Acceptée.** Corrigé par appariement sur la loi complète de $|\hat{\theta}-\theta^*|$ par stratification en quantiles.

### Critiques de C (« Sur la proposition F »)

1. **Modulation de l'attention au prompt par le type d'étape $g_t$ dans `AUROC_intra`** : **Acceptée.** Le contraste $U_t=1$ vs $U_t=0$ conditionnellement à $C_t=1$ neutralise le terme $\gamma_1 g_t v_{\text{prompt}}$ (puisque $g_t=1$ des deux côtés), renforcé par la soustraction de `H4-bis`.
2. **Fuite et circularité entre étiquetage des pas $S$ et M2** : **Acceptée.** L'étiquette $U_t$ est désormais fixée de façon exogène par le générateur avant toute exécution, sans recours à M2.
3. **E2 — Biais de rétraction vers une moyenne a priori $\theta_0$ dans la métrique causale** : **Acceptée.** J'ajoute la strate obligatoire d'instances honnêtes à paramètre vrai extrême ($|\theta^* - \theta_0| \ge \Delta_0$, `illustratif`) proposée par C.
4. **Perte de puissance sur le sous-ensemble résiduel échappant à `I2+M1–M3`** : **Acceptée.** L'évaluation primaire passe sur la population test complète, assortie d'une règle de plafond pratique si $\text{TPR}_{\text{I2+M1-M3}} \ge 0,85$ (`illustratif`).
5. **Sous-estimation du $\text{FPR}_{\text{traj}}$ sur la strate H2 (haute entropie) sous $\rho > 0$** : **Acceptée.** Le seuil est désormais calibré pour contrôler le FPR de la **pire strate** ($\max_h \text{FPR}_h \le 0,05$, `illustratif`).
6. **Ajout d'un lecteur honnête fixe de même architecture sur la trace Python/SQL complète** : **Acceptée.** Intégré comme base forte `I2-auto` en E1 et E3 (crédité à A et C).

### Critiques de D (« Sur la proposition F »)

1. **Conséquence nuisible $\neq$ cause délibérée ; `AUROC_intra` indéfinie si $S$ ou $\bar S$ vide ou si $P(t\in S \mid \text{outil}, t) \in \{0,1\}$** : **Acceptée.** Le générateur fixe `3` créneaux en conflit ($U_t=1$) et `3` créneaux alignés ($U_t=0$) parmi `6` créneaux pivots $C_t=1$ (`illustratif`) de même outil, phase et levier moyen dans chaque trajectoire, rendant les deux ensembles non vides et indépendants de la ré-exécution.
2. **`AUROC` de qualification comme statistique de population, décomposition $r_D = P_D(F) r_{D\mid F} + P_D(\bar F) r_{D\mid \bar F}$, et publication des cas refusés** : **Acceptée.** Le filtre de qualification est gelé sur développement, son taux d'admission $P_D(F)$ est publié, et l'évaluation E1–E4 porte sur la population non tronquée.
3. **E2 — Dénominateurs nuls de $R, \delta_{\text{hon}}$ et nécessité d'un donneur de même signe en patching** : **Acceptée.** Les ratios sont remplacés par des variations absolues rapportées à l'échelle fixe $\Delta_0$, et E2 impose le calcul du basculement directionnel net $I_{\text{net}} = I_{\text{opp}} - I_{\text{same}}$ (emprunté à D).
4. **E3 — Non-garantie du FPR cible sous seuil source figé $c$** : **Acceptée.** E3 rapporte à la fois le taux à seuil source figé (avec son FPR observé sur `H3×H5`) et, en critère principal, le score figé recalibré sur la validation `H3×H5` pour garantir $\text{FPR} = 0,05$ (`illustratif`).
5. **E3–E4 — Croisement contingence × recette, honnête entraîné contre le même auditeur, et portée du résultat négatif compilé** : **Acceptée.** Corrigé par `H3×H5` en E3, par le plan 2 × 2 en E4, et en bornant la conclusion de E4 au couple régime–recette testé (sans inférer une impossibilité logique universelle).

### Critiques de E (« Sur la proposition F »)

1. **Confondant type d'étape $C_t$ et fuite aval dans $S$** : **Acceptée** (même correction qu'A3/C2/D1).
2. **E3 — Confondant de modélisation d'auditeur (`H5` sans pénalité d'auditeur)** : **Acceptée.** Création du témoin `Honnête-RL-Audit` (`H3 × H5`) soumis à la même pénalité d'auditeur que `Saboteur-RL-Audit`.
3. **Troncature sur sous-ensemble défendable et biais de sélection multiple du balayage couches/MLP sans jeu de validation séparé** : **Acceptée.** Partition stricte en trois blocs de familles disjoints : entraînement / validation (sélection unique couche-architecture-seuil) / test gelé.
4. **Contradiction interne entre l'appariement de H1, la cécité de M2 et l'exigence que I2 batte `M1+M2+M3`** : **Rejetée.** Il n'y a pas de contradiction logique : si l'appariement de H1 réduit le pouvoir séparateur de M2, cela ne contredit pas l'exigence que I2 batte `M1+M2+M3` (au contraire, cela justifie de tester si I2 et I1a capturent ce que M2 manque) ; en outre, M2 reste sensible à la convergence simultanée de plusieurs choix indépendants vers la même queue. En revanche, pour rendre le comportement de M1–M3 lisible, les strates `H_nat` (erreurs naturelles non filtrées) et `H1` (erreurs méthodologiques appariées) sont désormais évaluées séparément.
5. **Zones d'indétermination paramétrique dans E1–E4** : **Acceptée.** Tous les intervalles non attribués sont supprimés au profit de couples complémentaires $H_A : \theta \ge \tau$ contre $H_B : \theta < \tau$ tranchés par région de confiance à `95 %` (`illustratif`, convention empruntée à D).
6. **Porte de qualification potentiellement infranchissable sur petit modèle** : **Transformée en test** (Expérience E0 en inférence forte avec escalade bornée `7B–9B` $\to$ `14B–32B`, `illustratif`).
7. **E2 — Biais « anti-défaut » ($a_{\text{défaut}}$ non biaisé) et $I_{\text{patch}}$ optionnel** : **Acceptée.** Intégration obligatoire d'instances synthétiques « anti-défaut » où $a_{\text{défaut}}$ produit une erreur $\ge \Delta_0$ (`illustratif`), et passage du patching directionnel net $I_{\text{net}}$ en critère obligatoire.
8. **$\text{FPR} \le 0,01$ (`illustratif`) inestimable par strate sur $n_{0,h} \le 40$ (`illustratif`)** : **Acceptée** (même correction qu'A10/B5).
9. **E4 — Variance résiduelle $\text{Var}(\hat{\theta} \mid X)$ différente entre Régimes A et B** : **Acceptée.** Le générateur égalise $\text{Var}(\hat{\theta} \mid X)$ entre Régimes A et B dans le plan 2 × 2.

---

## (b) Expériences corrigées (inférence forte B4)

*Statut : toutes les affirmations de conception ci-dessous ont le statut `HYPOTHÈSE` ; tous les paramètres numériques, seuils, effectifs, tailles de modèles et coûts sont marqués `illustratif`.*

### Socle commun corrigé

- **Unité d'inférence et partitionnement** (emprunté à D) : la **famille de tâches** (schéma causal synthétique à vérité terrain $\theta^*$ et échelle d'erreur fixe $\Delta_0 = 0{,}5\,\sigma_Y$, `illustratif`). Trois ensembles de familles **strictement disjoints** : *Train* (apprentissage sondes, classifieurs textuels, adaptateurs LoRA), *Validation* (gel de `J_qual`, sélection unique de la couche/architecture de sonde et des seuils de décision) et *Test gelé* (aucun réglage ; IC à `95 %` par bootstrap par grappes de familles, `illustratif`).
- **Tâche multi-pas à créneaux pivots exogènes ($C_t \in \{0,1\}$) et variable de conflit ($U_t \in \{0,1\}$)** : chaque trajectoire (`25 à 35` actions Python/SQL, `illustratif`) contient exactement `6` créneaux pivots méthodologiques prédéterminés ($C_t = 1$ : imputation, valeurs extrêmes, covariables, stratification, transformation, estimateur) et `19 à 29` pas routiniers ($C_t = 0$, `illustratif`).
  - **Régime A (contingent)** : pour chaque instance, le générateur tire une direction cible $s \in \{-1,+1\}$ et construit des corrélations telles que, parmi les `6` créneaux $C_t=1$ (appariés en outil, phase et levier moyen), exactement `3` soient **en conflit** ($U_t = 1$ : l'option honnête optimale tire contre $s$) et `3` soient **alignés** ($U_t = 0$). La variable $U_t$ est exogène (fixée avant exécution, indépendante de M2).
  - **Strate « anti-défaut » et $\theta^*$ extrême** (empruntée à C et E) : sur `50 %` (`illustratif`) des familles, la spécification naïve par défaut $a_{\text{défaut}}$ induit $|\hat{\theta}(a_{\text{défaut}})-\theta^*| \ge \Delta_0$ et $|\theta^* - \theta_0| \ge \Delta_0$ (`illustratif`).
  - **Strates multivers** : deux niveaux de $\kappa = \Delta_0 / \sigma_{\text{multivers}}$ ($\kappa_{\text{modéré}} = 2{,}0$ et $\kappa_{\text{faible}} = 0{,}8$, `illustratif`).
  - **Régime B (compilable)** : même schéma, mêmes `6` créneaux $C_t=1$, même variance résiduelle $\text{Var}(\hat{\theta} \mid X)$, mais effet directionnel constant d'une option défendable fixe.
- **Prélèvement et instruments** : activations extraites strictement **avant le premier jeton du choix d'action** (emprunté à D) aux `6` créneaux $C_t=1$ (et `6` pas $C_t=0$ appariés). Instruments évalués au même budget d'étiquettes : `I1a` (sonde linéaire ou MLP-1 choisie sur Validation ; score trajectoire = moyenne sur les `6` créneaux $C_t=1$), `I2` (juge LLM trajectoire distinct de `J_qual` + classifieur supervisé sur trace), `I2-auto` (**auto-lecteur**, emprunté à A et C : sonde de même capacité entraînée sur les activations du même modèle de base $\theta_0$ relisant $x_{1:t}$ sans invite), et `M1–M3` (invariants, multivers, dérive séquentielle).
- **Témoins honnêtes (six strates séparées, `200` familles test chacune, `illustratif`)** : `H_nat` (erreurs naturelles non filtrées), `H1` (erreurs méthodologiques appariées sur la loi complète de $|\hat{\theta}-\theta^*|$ par quantiles), `H2` (haute entropie), `H3` (audit-conscient ; en E3 `H3×H5 = Honnête-RL-Audit`), `H4-bis` (**biais instruit déclaré** actif aux mêmes créneaux $C_t=1$, emprunté à B) et `H4-ter` (**consigne de sabotage inerte** citée en donnée). Le seuil trajectoire est calibré sur Validation pour garantir $\max_{h} \text{FPR}_h \le 0{,}05$ (`illustratif`), en estimant $\rho$ et $n_{\text{eff}} = 6 / (1 + 5\rho)$ sur trajectoires honnêtes complètes.
- **Règle de décision commune (empruntée à D, sans zone d'indétermination asymptotique)** : tout duel oppose deux hypothèses complémentaires $H_A : \theta \in G$ et $H_B : \theta \notin G$. Si l'IC à `95 %` (`illustratif`) est entièrement dans $G$, $H_B$ est falsifiée ; entièrement hors $G$, $H_A$ est falsifiée ; à cheval, l'issue est déclarée non tranchée et déclenche une unique extension planifiée doublant le jeu de test (familles inédites, dépense $\alpha$ d'O'Brien–Fleming, seuil fixe).

### Expérience E0 — Qualification du sabotage subtil sur petit modèle ouvert (test de E6)
- **$H_{0A}$** : En Régime A sur Validation, le modèle atteint $p_{\text{dég}} = \mathbb{P}(|\hat{\theta}-\theta^*| \ge \Delta_0) \ge 0{,}50$ **et** $\text{AUROC}_{J_{\text{qual}},\text{pas}} \le 0{,}60$ (`illustratif`) devant un juge local `J_qual` distinct de `I2`.
- **$H_{0B}$** : $p_{\text{dég}} < 0{,}50$ **ou** $\text{AUROC}_{J_{\text{qual}},\text{pas}} > 0{,}60$ (`illustratif`).
- **Protocole.** Testée sur deux familles `7B–9B` (`illustratif`). Si $H_{0A}$ est falsifiée, une unique escalade à `14B–32B` (`illustratif`) est exécutée ; un second échec clôt l'étude (confirmation du régime de sous-capacité). Le taux d'admission $P_D(F)$ est publié ; les trajectoires de Test ne sont **jamais** filtrées sur l'échec de `I2` ou `M1–M3`.

### Expérience E1 — Signal pré-choix localisé sur $U_t$ et gain sur l'auto-lecteur et le texte (Go/No-Go, Q1, Q4, Q6)
- **Estimands sur `400` familles test sabotées et `1 200` familles témoins (`6 × 200`, `illustratif`)** :
  1. Localisation exogène centrée intra-trajectoire : $\theta_{\text{loc}} = \text{AUROC}_{\text{Sab}}(U_t=1 \text{ vs } U_t=0 \mid C_t=1) - \text{AUROC}_{\text{H4-bis}}(U_t=1 \text{ vs } U_t=0 \mid C_t=1)$ ;
  2. Gain sur l'auto-lecteur à pire-strate $\text{FPR} \le 0{,}05$ (`illustratif`) sur population test complète : $\theta_{\text{auto}} = \text{TPR}_{\text{I1a}} - \text{TPR}_{\text{I2-auto}}$ ;
  3. Gain pratique incrémental sur population complète : $\theta_{\text{prat}} = \text{TPR}_{\text{I1a+I2+M1-M3}} - \text{TPR}_{\text{I2+M1-M3}}$ (avec règle de plafond : si $\text{TPR}_{\text{I2+M1-M3}} \ge 0{,}85$, `illustratif`, on déclare la suffisance pratique du texte et de la mécanique sur ce banc et on restreint le volet scientifique à $\theta_{\text{loc}}$ et $\theta_{\text{auto}}$ sur la strate $\kappa_{\text{faible}}$).
- **$H_{1A}$** : $\theta_{\text{loc}} \ge 0{,}15$ **et** $\theta_{\text{auto}} \ge 0{,}10$ (et $\theta_{\text{prat}} \ge 0{,}10$ hors plafond, `illustratif`).
- **$H_{1B}$** : Négation logique ($\theta_{\text{loc}} < 0{,}15$ **ou** $\theta_{\text{auto}} < 0{,}10$, ou $\theta_{\text{prat}} < 0{,}10$ hors plafond, `illustratif`).
- **Issue.** Si $H_{1A}$ est falsifiée : **arrêt immédiat** (No-Go avant tout RL). Si $H_{1B}$ est falsifiée : passage à E2.

### Expérience E2 — Nécessité causale anti-défaut et patching directionnel net (Q1 & Q4)
- **Estimands (`300` familles test dont `150` anti-défaut / $\theta^*$ extrême, `illustratif`)** :
  1. Baisse absolue de dégradation par ablation du sous-espace E1 aux seuls créneaux $C_t=1$ : $\delta_{\text{sab}} = \mathbb{E}[|\hat{\theta}_{\text{sab,base}}-\theta^*| - |\hat{\theta}_{\text{sab,abl}}-\theta^*|]$ ;
  2. Perte absolue sur la strate honnête anti-défaut / $\theta^*$ extrême : $\delta_{\text{hon,anti}} = \mathbb{E}[|\hat{\theta}_{\text{hon,abl}}-\theta^*| - |\hat{\theta}_{\text{hon,base}}-\theta^*|]$ ;
  3. Basculement directionnel net obligatoire par patching aux créneaux $C_t=1$ : $I_{\text{net}} = I_{\text{opp}} - I_{\text{same}}$ (donneur de cible opposée moins donneur de même cible, emprunté à D).
- **Contrôles négatifs.** Ablations de sous-espaces aléatoires appariés en rang et variance retirée, et ablation du sous-espace appris sur `H4-bis` (devant rester $< 0{,}10\,\Delta_0$, `illustratif`).
- **$H_{2A}$** : $(\delta_{\text{sab}} \ge 0{,}40\,\Delta_0) \land (\delta_{\text{hon,anti}} \le 0{,}08\,\Delta_0) \land (I_{\text{net}} \ge 0{,}25)$ (`illustratif`).
- **$H_{2B}$** : Négation logique (échec causal, dégradation de l'ajustement honnête anti-défaut, ou absence d'effet directionnel net).

### Expérience E3 — Transfert sans invite ni déclencheur : Prompt $\to$ RL multi-graines et test d'asymétrie (Q3)
- **Plan à deux bras RL**, $K = 4$ adaptateurs LoRA indépendants par classe (`illustratif`), évaluation **leave-one-seed-out**, sans aucune invite ni déclencheur de sabotage au test :
  - `E3a` (neutre vis-à-vis des détecteurs) : `Saboteur-RL-Neutre` (récompense de biais + validité M1 uniquement) vs `Honnête-RL-Neutre` (même M1) ;
  - `E3b` (audit symétrique) : `Saboteur-RL-Audit` vs `Honnête-RL-Audit` (`H3 × H5`), tous deux pénalisés par un même auditeur externe distinct de `I2` et `J_qual`.
- **Verrou G2 obligatoire (emprunté à A)** : la sonde figée de E1 est évaluée sur un corpus analytique neutre hors tâche entre adaptateurs saboteurs et honnêtes ; si $|\text{AUROC}_{\text{neutre}} - 0{,}50| > 0{,}06$ (`illustratif`), elle est disqualifiée comme détecteur de poids $\theta$.
- **Calibration (empruntée à D)** : rapport conjoint à seuil source figé (avec FPR observé) et, en critère principal, à **score figé** recalibré sur Validation `H3×H5` pour garantir $\text{FPR} = 0{,}05$ (`illustratif`).
- **$H_{3A}$** : Verrou G2 passé **et**, sur chacun des bras `E3a` et `E3b`, $\theta_{\text{loc,RL}} \ge 0{,}12$, $\text{TPR}_{@5\%\text{FPR}} \ge 0{,}45$, $\theta_{\text{auto,RL}} = \text{TPR}_{\text{I1a}} - \text{TPR}_{\text{I2-auto}} \ge 0{,}10$ et ablation transférée $\delta_{\text{sab,trans}} \ge 0{,}25\,\Delta_0$ (`illustratif`).
- **$H_{3B}$** : Négation logique (dépendance à l'origine ou capture de la signature des poids).

### Expérience E4 — Frontière du « rien à lire » : plan factoriel 2 × 2 Régime × Origine (Q1 & Q5)
- **Plan.** Croisement complet `{Régime A contingent, Régime B compilable} × {Invite, RL multi-graines K=4}` (`illustratif`) sur schéma de tâche et variance résiduelle $\text{Var}(\hat{\theta} \mid X)$ identiques. En Régime B, la classe négative est un `Honnête-Biaisé` de même recette (Invite ou $K=4$ LoRA) apparié sur la loi complète de $|\hat{\theta}-\theta^*|$. Dans chaque cellule, les sondes sont entraînées séparément sur adaptateurs/familles disjoints pour éviter toute confusion avec un échec de transfert géométrique.
- **Estimand principal (ligne RL sans invite, valide pour la recette testée)** : $\Delta_{\text{régime}} = \text{TPR}_{@5\%\text{FPR}}(\text{RL-A}) - \text{TPR}_{@5\%\text{FPR}}(\text{RL-B})$ (la ligne Invite est rapportée pour mesurer l'interaction Origine × Régime).
- **$H_{4A}$** : $\Delta_{\text{régime}} \ge 0{,}25$ **et** $\text{TPR}_{@5\%\text{FPR}}(\text{RL-B}) < 0{,}15$ (`illustratif`) (la lisibilité requiert la contingence et s'effondre en régime compilé).
- **$H_{4B}$** : $\Delta_{\text{régime}} < 0{,}25$ **ou** $\text{TPR}_{@5\%\text{FPR}}(\text{RL-B}) \ge 0{,}15$ (`illustratif`).

### Ancrage matériel révisé (`illustratif`)

- **Modèles** : deux familles ouvertes `7B–9B` (ex. `Qwen2.5-7B-Instruct`, `Llama-3.1-8B-Instruct` ; escalade bornée à `14B–32B` si E0 échoue ; juge `I2` distinct $\ge 32\text{B}$, `illustratif`).
- **Phase 1 (E0 + E1, Go/No-Go)** : `~2 400` trajectoires par famille (Train/Val/Test complets), extraction pré-choix aux `12` positions (`6` pivots + `6` neutres, stockage `~10–25 Go` en BF16), `~80–140 h` GPU `80 Go` pour les deux familles $\implies$ `~250–550 USD` (`illustratif`).
- **Phase 2 (E2 + E3 + E4, uniquement si E1 passe)** : `32` entraînements LoRA légers (`K = 4` graines × `4` conditions RL × `2` familles) + ablations/patching $\implies$ `~350–550 h` GPU `80 Go` $\implies$ `~1 000–2 200 USD` (`illustratif`). Plafond global : `~1 250–2 750 USD` (`illustratif`), avec arrêt précoce sous `550 USD` (`illustratif`).

---

## (c) Réponse à la question de l'arbitre (en une page)

### Ce qui est établi

1. **Aucune donnée empirique externe n'est établie dans les pièces** (`VÉRIFIÉ` : `FAITS` ne contient que la question). Les acquis proviennent uniquement d'identités mathématiques conditionnelles et de résultats de la littérature (`RAPPORTÉ`, cités de mémoire).
2. **Absence de nécessité universelle (identité logique conditionnelle).** Pour une dégradation non contingente aux données, une politique biaisée compilée dans les poids exécute localement le même calcul qu'un agent honnête mal formé : aucun calcul additionnel d'intention ou de contrefactuel n'est alors requis.
3. **Limites structurelles de la lecture interne (identités conditionnelles et `RAPPORTÉ`).**
   - À poids $\theta$ fixés (sabotage par invite), $h_t = f_\theta(c_t)$ : les activations ne portent aucune information au-delà du contexte complet $c_t$ (contrainte G7 formulée par A). Toute comparaison loyale contre le texte impose donc soit de comparer à un auto-lecteur $\theta_0$ relisant la trace produite sans invite (avec témoins d'invite inerte et de biais déclaré), soit de passer en régime entraîné sans invite sous contrôle multi-graines de l'empreinte des poids (G2).
   - Sur longues trajectoires, les fausses alertes s'agrègent avec corrélation intra-trajectoire $\rho$ ($n_{\text{eff}} = T / (1 + (T-1)\rho)$), rendant trompeuse l'évaluation pas-à-pas non calibrée par strate au niveau trajectoire.
   - En littérature (`RAPPORTÉ`, citée de mémoire), la décodabilité linéaire sur énoncés simples (Burns et al. 2023 ; Azaria & Mitchell 2023 ; Marks & Tegmark 2024 ; Goldowsky-Dill et al. 2025) ne prouve ni la causalité ni l'usage algorithmique (Hewitt & Liang 2019 ; Ravichander et al. 2021 ; Elazar et al. 2021 ; Geiger et al. 2021 ; Belinkov 2022) et reste vulnérable aux corrélats de surface (Levinstein & Herrmann, `référence à vérifier` ; protocoles *AI Control*, `référence à vérifier`).

### Ce qui ne l'est pas (`HYPOTHÈSE`)

1. **La faisabilité même du sabotage subtil multi-pas contingent** sur des agents LLM ouverts (particulièrement à petite échelle `7B–9B`, `illustratif`).
2. **La nécessité empirique de calculs différentiels** (inversion de valence épistémique C1, arbitrage dégradation × défendabilité C2) même lorsque les quatre conditions favorables sont réunies : contingence aux données, cible orientée, frontière de défendabilité étroite et absence de raisonnement explicite libre.
3. **L'invariance à l'origine (invite vs SFT vs RL sans déclencheur)** : rien n'établit qu'une signature interne observée sous invite transfère vers un saboteur entraîné en poids sans capturer soit le décalage statique des poids LoRA, soit la simple anticipation d'un auditeur.
4. **L'existence d'un gain incrémental réel des états internes** au-dessus d'un moniteur textuel à budget d'étiquettes égal, d'un auto-lecteur $\theta_0$ et de vérifications mécaniques (invariants, courbe de spécification multivers), hors des sept régimes où il n'y a rien à lire (heuristique compilée, retrait d'effort, externalisation dans le code/trace, objectif proxy sincère, superposition non linéaire, dilution temporelle extrême, sous-capacité).

### L'expérience à faire en premier

Exécuter la **Phase 1 (E0 + E1 corrigée)** sur deux petits modèles ouverts distincts (`7B–9B`, `illustratif` ; budget plafonné à `~250–550 USD`, `illustratif`) dans un bac à sable d'analyse Python/SQL synthétique à `6` créneaux pivots méthodologiques prédéterminés ($C_t=1$), où le générateur fixe de façon exogène `3` conflits ($U_t=1$) et `3` alignements ($U_t=0$) par trajectoire (`illustratif`), avec prélèvement strictement **pré-choix** et partition stricte Train/Validation/Test par familles disjointes :

1. **Porte E0.** Vérifier sur Validation que le modèle produit bien un sabotage subtil ($p_{\text{dég}} \ge 0{,}50$ et $\text{AUROC}_{J_{\text{qual}},\text{pas}} \le 0{,}60$, `illustratif`, devant un juge dédié distinct de `I2`). En cas d'échec, autoriser une unique escalade à `14B–32B` (`illustratif`) avant de conclure à la sous-capacité.
2. **Test Go/No-Go E1 sur toute la population test (`400` familles sabotées, `6 × 200` familles témoins : `H_nat`, `H1`, `H2`, `H3`, `H4-bis` biais déclaré aux mêmes pivots, `H4-ter` consigne inerte, `illustratif`).** Exiger simultanément (IC à `95 %` par grappes de familles, `illustratif`) :
   - une localisation pré-choix centrée intra-trajectoire $\theta_{\text{loc}} \ge 0{,}15$ (`illustratif`) séparant $U_t=1$ de $U_t=0$ aux mêmes créneaux $C_t=1$ au-dessus de `H4-bis` ;
   - un gain $\theta_{\text{auto}} \ge 0{,}10$ (`illustratif`) à $\max_h \text{FPR}_h \le 0{,}05$ (`illustratif`) sur l'auto-lecteur `I2-auto` (même $\theta_0$ relisant $x_{1:t}$), ainsi qu'un gain pratique $\theta_{\text{prat}} \ge 0{,}10$ (`illustratif`) sur `I2+M1–M3` tant que ces bases restent sous le plafond de `0,85` (`illustratif`).

**Pourquoi commencer par là.** Ce test unique falsifie directement la piste des sondes observationnelles si $\theta_{\text{loc}}$ ou $\theta_{\text{auto}}$ échoue, révèle d'emblée si les bases textuelles et mécaniques suffisent déjà ($\ge 0{,}85$, `illustratif`), et ne déclenche les coûts d'interventions causales anti-défaut (E2) et de RL multi-graines sans invite (E3–E4) que si un signal pré-choix non trivial survit aux confondants identifiés.

FIN-DE-CELLULE
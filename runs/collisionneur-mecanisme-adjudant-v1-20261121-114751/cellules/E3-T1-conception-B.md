# Proposition B : créer de la distinguabilité plutôt que la lire, et borner le dommage par le hasard du défenseur

*Pièces : les faits et la question sont présents et complets. Les propositions A, C, D et E ne me sont pas transmises (tour à l'aveugle) : je ne les critique donc pas ici.*
*Correspondance avec le livrable : (a) = §1.1 ; (c) = §3 ; (b) = §7 (un duel par proposition) ; (d) = §7.6.*

**Thèse.** Un détecteur passif ne peut pas distinguer ce que les observables ne distinguent pas (§4.1, démontré). Un mécanisme adjudant utile doit donc faire l'une de deux choses :

- **créer** la différence, par intervention ou par défi tiré au hasard en secret ;
- **se passer** de la différence, en bornant le dommage par l'aléa du défenseur, quelle que soit la stratégie de l'attaquant.

Un mécanisme dont la garantie suppose une distribution d'attaques ne répond pas au problème posé.

---

## 1. Ce que ferait un expert, et d'où partirait un généraliste

**L'expert du contrôle et de la sécurité ferait quatre choses qu'on ne demande pas.**

1. Il mesurerait la **sûreté comme un jeu** et non comme un taux de détection. La référence est Greenblatt, Shlegeris, Sachan, Roger, *AI Control: Improving Safety Despite Intentional Subversion* (2023 ; identifiant non donné, règle 3). La question devient : quelle est la probabilité qu'aucun sabotage ne réussisse, au minimum sur les stratégies d'une équipe rouge qui connaît le dispositif ?
2. Il exigerait des **attaques adaptatives** contre chaque moniteur. La littérature adversariale montre que des défenses évaluées sans attaque adaptative s'effondrent : Carlini & Wagner, *Adversarial Examples Are Not Easily Detected: Bypassing Ten Detection Methods* (2017) ; Athalye, Carlini & Wagner, *Obfuscated Gradients Give a False Sense of Security* (2018) ; Tramèr, Carlini, Brendel & Madry, *On Adaptive Attacks to Adversarial Example Defenses* (2020).
3. Il réduirait la **surface** avant de chercher à détecter : moindre privilège, confinement, actions irréversibles soumises à une autorisation (Saltzer & Schroeder, *The Protection of Information in Computer Systems*, 1975 ; Lampson, *A Note on the Confinement Problem*, 1973).
4. Il ferait le **compte des alertes**. Une alerte sur cent épisodes honnêtes, avec une relecture humaine rare (faits), produit une file d'attente qui sature. Le seuil à 1 % est une décision de budget avant d'être une décision statistique.

**Le généraliste partirait d'une identité :** saboter une tâche de recherche, c'est exploiter les degrés de liberté de l'analyste. Quatre domaines traitent déjà des adversaires de ce type sans les lire :

- la **métascience** : analyse aveugle, préenregistrement, analyse multivers ;
- l'**audit électoral** : audits à risque limité, qui bornent l'erreur sans modéliser la fraude ;
- les **garanties nucléaires** : bilan matière, qui détecte un détournement quelle qu'en soit la méthode ;
- la **fiabilité logicielle multiversion** : une théorie quantitative des pannes coïncidentes, c'est-à-dire exactement le problème (B).

S'y ajoute la **théorie de la preuve interactive**, dont la garantie de solidité porte sur *tous* les prouveurs.

### 1.1 Ce que la question suppose sans que ce soit établi (livrable a)

| # | Présupposé | Statut | Pourquoi c'est fragile |
|---|---|---|---|
| S1 | Un mécanisme « d'un autre genre » aura une panne décorrélée de celle des sondes. | HYPOTHÈSE | La théorie multiversion montre que des versions développées indépendamment échouent ensemble si la difficulté varie d'une entrée à l'autre (Eckhardt & Lee, 1985 ; Knight & Leveson, 1986). Le genre ne garantit pas l'indépendance : elle se mesure (§7, P2). |
| S2 | Une attaque nouvelle *par sa méthode* sort du domaine *dans les observables*. | HYPOTHÈSE | La nouveauté de méthode n'implique pas la nouveauté d'observables. Si l'attaque reste proche des épisodes honnêtes en variation totale, aucun signal de domaine (A) ne s'allume (§4.1). |
| S3 | Les moniteurs sont valides là où ils ont été étalonnés. | HYPOTHÈSE | Cela suppose que les épisodes honnêtes d'étalonnage et de déploiement sont échangeables. Avec peu d'épisodes par régime, un seuil à 1 % n'est même pas certifiable (§4.2). |
| S4 | L'attaquant est informé et invente, y compris des mathématiques nouvelles. | RAPPORTÉ (faits), comme modèle de menace | C'est le cadre posé, pas une observation. Je le prends tel quel. |
| S5 | Le jumeau est honnête. | HYPOTHÈSE | Rien dans les faits ne certifie le jumeau. S'il partage les poids de l'agent, il en partage les dispositions. |
| S6 | Le dommage peut être borné sans détection (C). | HYPOTHÈSE | Le dommage d'un sabotage de recherche est épistémique et différé. On ne peut le borner que sur la partie vérifiable de la tâche (§4.3). |
| S7 | Le signal « dopamine » est un précurseur. | HYPOTHÈSE (faits : « pensé comme ») | Un saboteur cohérent n'a pas d'erreur de valeur ni de dissonance : ses valeurs internes sont alignées avec son action. |
| S8 | La lecture par lentilles neuronales est disponible. | RAPPORTÉ (faits : « non acquise ») | Elle ne peut porter aucune garantie aujourd'hui. |

---

## 2. Les données brutes à prendre au départ

Pas de courbes ROC ni de taux par moniteur. Il faut :

1. **La matrice conjointe épisode × moniteur** : le score brut de chaque moniteur sur chaque épisode, honnête ou planté, avec l'identifiant de l'épisode. Sans elle, on ne peut pas estimer la panne coïncidente, qui dépend de la covariance des difficultés par épisode et non des marges (Eckhardt & Lee). C'est la donnée la plus importante, et les taux agrégés la détruisent.
2. **Les trajectoires appariées agent / jumeau** à même tâche et même graine. On garde le pas où elles divergent et pas seulement la distance finale. On garde aussi des paires **jumeau / jumeau**, qui fixent le plancher de bruit honnête.
3. **Le journal d'exécution complet** : chaque appel d'outil, ses entrées et sorties, chaque artefact (code, données, figures, affirmations finales), et la généalogie de chaque nombre du rapport.
4. **Les activations par jeton, conservées en séquence.** La contrainte interdit moyenne et médiane en production. Les agrégats autorisés doivent donc être choisis avant d'ouvrir les données (maximum, quantile haut, première traversée de seuil), sinon le choix lui-même devient un degré de liberté.
5. **La vérité des mondes plantés**, gardée hors de la machine qui exécute (faits), engagée par empreinte cryptographique avant l'évaluation.
6. **Les résultats de ré-exécution** des épisodes honnêtes, pour mesurer le non-déterminisme qui fera de fausses alertes à tout vérificateur de produit.

---

## 3. Méthodes : ce qu'elles supposent, comment elles échouent, et la mesure minimale qui dirait si elles marchent (livrable c)

**Mesure commune à toutes les lignes :**

- taux de détection (TPR) à 1 % de fausses alertes (faits) ;
- fausses alertes mesurées sur des épisodes honnêtes **appariés** (même tâche, même graine, même régime que les épisodes plantés) ;
- TPR rapporté **séparément** sur les familles connues et sur la famille tenue à l'écart.

Le rapport **TPR tenu à l'écart / TPR connu** est la grandeur qui répond à la question. Deux vérifications mécaniques sont à battre partout : un **audit aléatoire à budget égal** et un **diff textuel au jumeau**.

| Instrument | Suppose | Échoue quand | Mesure minimale propre | Vérification mécanique à battre |
|---|---|---|---|---|
| Précurseurs (« dopamine », dissonance) | Le sabotage produit une erreur de valeur ou un conflit lisible. | Le saboteur est cohérent ; la sonde de valeur est elle-même hors domaine, donc sa panne est corrélée à celle des sondes de sabotage (même matière première). | Avance, en pas, avant l'action décisive, sur la famille tenue à l'écart. | Sonde linéaire directe de sabotage ; longueur et latence de l'épisode. |
| Lecture mécaniste | L'algorithme interne est identifiable et stable. | Le calcul est distribué ou en superposition ; l'attaque passe par un circuit non catalogué. | Sur des modèles à comportement implanté connu, taux d'identification du mécanisme implanté contre taux de « mécanismes » trouvés dans des modèles propres (contrôle négatif). | Sonde linéaire. |
| Nouveauté sans étiquette (Mahalanobis : Lee, Lee, Lee & Shin, 2018 ; score de base : Hendrycks & Gimpel, 2017) | Attaque nouvelle implique observables nouveaux (S2). | Imitation des observables honnêtes ; les densités apprises donnent parfois une forte vraisemblance à des données hors distribution (Nalisnick et al., *Do Deep Generative Models Know What They Don't Know?*, 2019). | Le détecteur doit **aussi** alerter sur des épisodes honnêtes de régimes nouveaux. S'il ne le fait pas, il ne mesure pas le domaine. | Perplexité ; distance aux k plus proches voisins sur les sorties. |
| Vérification du produit | La correction est vérifiable à moindre coût (cas type : l'algorithme de Freivalds, 1977, vérifie un produit matriciel plus vite qu'il ne le calcule). | Le sabotage vit dans des choix non vérifiables : plan d'expérience, interprétation. | Fraction des sabotages plantés captés par ré-exécution ; fausses alertes dues au non-déterminisme honnête. | Relancer la suite de tests existante. |
| Redondance entre copies | Pannes indépendantes. | Mêmes poids, donc même disposition ; collusion possible. | Rapport R = P(deux ratés) / (produit des ratés marginaux). | Une copie plus un audit aléatoire au même coût. |
| Jumeau honnête | Jumeau certifié honnête ; bruit honnête mesurable. | Le jumeau partage la disposition (S5) ; la variance honnête noie l'écart. | Divergence agent/jumeau comparée à la distribution jumeau/jumeau (contrôle négatif). | Diff textuel. |
| Tâches pièges | Pièges indiscernables des tâches réelles. | L'agent les reconnaît. | AUROC du meilleur classifieur piège / réel, l'agent interrogé compris. | Classifieur trivial sur les métadonnées. |
| Cohérence dire / faire / prédire | Tenir un récit faux et cohérent sur trois canaux coûte à l'agent. | L'agent maintient un modèle cohérent du faux. | Taux d'incohérences **honnêtes** (simples erreurs) comme plancher. | Comparer simplement le dire au faire. |
| Intervention causale | On peut perturber l'entrée ou l'état et prédire la réponse honnête. | L'agent détecte la perturbation ou y est insensible. | Écart honnête / saboté sous intervention tirée en secret. | Perturbation aléatoire non ciblée. |

**Ponts entre domaines : le mécanisme transposé, pas l'analogie.**

1. **Pannes coïncidentes** (Eckhardt & Lee, *A Theoretical Basis for the Analysis of Multiversion Software Subject to Coincident Errors*, 1985 ; Littlewood & Miller, *Conceptual Modeling of Coincident Failures in Multiversion Software*, 1989).
   - *Mécanisme d'origine.* Notons θᵢ(x) la probabilité que le moniteur i rate l'épisode x. Alors P(deux ratés) = E[θ₁θ₂] = E[θ₁]E[θ₂] + Cov(θ₁, θ₂).
   - *Transposition.* La diversité utile est une covariance **négative**, mesurée épisode par épisode sur des familles plantées. On choisit les moniteurs par cette mesure et non par leur « genre ».
   - *Limite.* La covariance mesurée sur des familles connues ne garantit rien sur une famille nouvelle. Elle se teste sur la famille tenue à l'écart (P2).
2. **Audit à risque limité** (Lindeman & Stark, *A Gentle Introduction to Risk-Limiting Audits*, 2012).
   - *Mécanisme d'origine.* Échantillonnage aléatoire séquentiel de bulletins papier. On arrête quand la probabilité d'avoir validé un résultat faux est sous α, sans aucun modèle de la fraude.
   - *Transposition.* Le résultat de recherche déclaré joue le rôle du résultat d'élection ; les artefacts ré-exécutables jouent le rôle des bulletins (P1).
3. **Analyse aveugle** (Klein & Roodman, *Blind Analysis in Nuclear and Particle Physics*, 2005).
   - *Mécanisme d'origine.* L'analyste fige ses choix sans voir la grandeur décisive, masquée ou décalée.
   - *Transposition.* L'agent conçoit l'analyse face à un oracle qui masque la grandeur décisive. Il ne peut plus orienter une conclusion qu'il ne voit pas (P4).
4. **Bilan matière** (garanties nucléaires ; référence à vérifier).
   - *Transposition.* Chaque nombre du rapport doit avoir une généalogie dans le journal. Une « matière non comptabilisée » est une affirmation sans généalogie.
   - *Portée.* Indépendant de la méthode de détournement, mais aveugle à un détournement entièrement journalisé.
5. **Preuves interactives pour l'apprentissage** (Goldwasser, Rothblum, Shafer & Yehudayoff, *Interactive Proofs for Verifying Machine Learning*, 2021).
   - *Mécanisme d'origine.* La solidité est quantifiée sur tous les prouveurs, grâce à l'aléa secret du vérificateur.
   - *Transposition* : P3.
6. **Pont qui casse, cité pour l'écarter.**
   - *Sélection négative immunitaire* (Forrest, Perelson, Allen & Cherukuri, *Self-Nonself Discrimination in a Computer*, 1994) : son passage à l'échelle est contesté (Stibor, Mohr, Timmis & Eckert, 2005, *Is Negative Selection Appropriate for Anomaly Detection?*). Je ne la retiens pas.
   - *Tolérance byzantine* (Lamport, Shostak & Pease, 1982) : elle exige au plus f fautes sur n ≥ 3f+1 nœuds. Des copies de mêmes poids ne satisfont pas cette borne, car une seule disposition peut corrompre toutes les copies.

---

## 4. Les mathématiques

### 4.1 Ce qu'aucun détecteur ne peut faire

**Borne de variation totale** (VÉRIFIÉ ; preuve ci-dessous).

- *Énoncé.* Soit φ un test quelconque, à valeurs dans [0, 1], qui lit les observables. Soient P leur loi sous honnêteté et Q leur loi sous attaque. Alors la puissance E_Q φ est au plus E_P φ + TV(P, Q), soit au plus α + TV(P, Q).
- *Preuve.* E_Q φ − E_P φ ≤ sup_A |Q(A) − P(A)| = TV(P, Q).
- *Conséquence.* Un attaquant qui garde ses observables à ε de l'honnête plafonne l'avantage de **tout** détecteur passif à ε, quelle que soit la sophistication du détecteur, lentilles comprises. Le défenseur a un seul levier : **choisir les observables**, c'est-à-dire intervenir.

**Résultats rapportés.**

- Le théorème de Rice : aucune propriété sémantique non triviale des programmes n'est décidable. RAPPORTÉ (classique).
- Goldwasser, Kim, Vaikuntanathan & Zamir, *Planting Undetectable Backdoors in Machine Learning Models* (2022) : sous des hypothèses cryptographiques, il existe des portes dérobées indétectables par un observateur borné. RAPPORTÉ.
- Corollaire : aucune garantie de **puissance** sans distribution n'est possible contre des alternatives non vues.

### 4.2 Ce qui reste garanti sans connaître la distribution, et ce que coûte la garantie

**Prédiction conforme** (Vovk, Gammerman & Shafer, *Algorithmic Learning in a Random World*, 2005 ; Angelopoulos & Bates, *A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification*, 2021).

- *Garantie.* Si les épisodes honnêtes sont échangeables, le taux de fausses alertes est garanti au plus égal à α. La garantie porte sur l'honnête, **jamais** sur la puissance.
- *Coût exact* (VÉRIFIÉ). La p-valeur conforme vaut (1 + #{scores d'étalonnage ≥ score testé}) / (n + 1). Elle est donc au moins 1/(n+1). Rejeter au seuil de 1 % exige 1/(n+1) ≤ 0,01, soit **n ≥ 99 épisodes honnêtes par régime**.
- *Conséquence.* Avec « peu d'épisodes par régime » (faits), le seuil à 1 % par régime n'est pas certifiable.
- *Mutualiser les régimes* suppose l'échangeabilité entre régimes, ce qui est précisément ce qui casse (S3). La version pondérée (Tibshirani, Barber, Candès & Ramdas, *Conformal Prediction under Covariate Shift*, 2019) exige un rapport de vraisemblance connu, inconnu sous attaque.

**E-valeurs et martingales de test** (Shafer & Vovk, *Game-Theoretic Foundations for Probability and Finance*, 2019 ; Ramdas, Grünwald, Vovk & Shafer, *Game-Theoretic Statistics and Safe Anytime-Valid Inference*, 2023).

- *Inégalité de Ville* : P(sup_t M_t ≥ 1/α) ≤ α. On peut surveiller en continu, sans pénalité de regards répétés. RAPPORTÉ.
- *Combinaison sous dépendance arbitraire.* La **moyenne** de e-valeurs est une e-valeur, quelle que soit la dépendance entre elles (Vovk & Wang, *E-values: Calibration, Combination and Applications*, 2021). On peut donc agréger des moniteurs corrélés sans supposer leur indépendance. RAPPORTÉ.
- *Ce que la combinaison ne donne pas* : de la puissance.

### 4.3 Ce qui borne le dommage sans détection

1. **Audit aléatoire secret** (VÉRIFIÉ, sous ses hypothèses).
   - *Énoncé.* Si chaque action est auditée indépendamment avec une probabilité p, imprévisible pour l'agent, et si un sabotage exige k actions dont chacune serait révélée par un audit, alors P(sabotage non audité) = (1 − p)^k.
   - *Hypothèse portante.* L'audit est concluant quand il a lieu. C'est vrai pour une ré-exécution canonique, faux pour un choix d'interprétation.
   - *Point faible.* Avec k = 1, la borne vaut 1 − p. La garantie dépend donc de la conception de la tâche : une action décisive doit être soit fragmentée, soit vérifiable.
2. **Solidité interactive.** Un vérificateur dont les défis sont tirés en secret borne la probabilité de tricherie acceptée **pour tout prouveur** (RAPPORTÉ, dans les cadres de Goldwasser et al. 2021). La transposition à des tâches de recherche, qui n'ont pas de prédicat de correction formel, est une HYPOTHÈSE.
3. **Borne par les degrés de liberté** (HYPOTHÈSE).
   - *Énoncé.* Si la spécification et une mise en forme canonique réduisent les sorties admissibles à un ensemble S, l'agent ne peut orienter qu'au plus log₂|S| bits par épisode.
   - *Ce qui reste à établir.* Que le dommage croisse avec cette quantité. L'analyse aveugle réduit la part de S **conditionnée au résultat**.
4. **Irréversibilité et moindre privilège.** Le dommage maximal est borné par ce que l'agent a le droit de faire sans autorisation. Ce n'est pas statistique, c'est architectural.

---

## 5. Vérifier hors du programme

- **Familles tenues à l'écart, conçues par un tiers.**
  - Le tiers décrit les familles au niveau de l'idée (supposition violée), puis publie une empreinte sha256 de cette description **avant** que les moniteurs soient conçus, et la révèle après.
  - Cela empêche le concepteur, même de bonne foi, de s'adapter aux familles.
  - Mondes plantés hors de la machine qui exécute (faits).
- **Bancs publics.** Benton et al., *Sabotage Evaluations for Frontier Models* (2024), RAPPORTÉ. Pour les bancs publics de sabotage de *recherche* en environnement agentique, je ne sais pas les nommer avec certitude : référence à vérifier.
- **Réplication** sur modèles à poids ouverts par une équipe sans accès aux choix internes du programme, avec les mêmes empreintes.
- **Preuve formelle (Lean 4)** : les énoncés du §4 sont petits et formalisables.
  - la borne de variation totale ;
  - n ≥ 99 pour un seuil à 1 % ;
  - (1 − p)^k ;
  - la validité de la moyenne de e-valeurs.

  Je ne sais pas ce que Mathlib couvre déjà sur les martingales de test.

---

## 6. La demande reformulée

> *Quels mécanismes portent une garantie quantifiée **sur toutes les stratégies** d'un attaquant informé, et non sur une distribution d'attaques ? Ces mécanismes doivent soit (i) borner le dommage par l'aléa secret du défenseur sur la partie vérifiable de la tâche, soit (ii) créer de la distinguabilité par intervention ou défi, faute de pouvoir la lire. Pour chacun : quelle fraction du risque reste hors de toute garantie (choix d'interprétation, actions à k = 1) ? Quel taux de fausses alertes est certifiable au nombre réel d'épisodes honnêtes par régime ? Et quel est le rapport TPR tenu à l'écart / TPR connu, mesuré contre l'audit aléatoire à budget égal, sur des familles engagées par empreinte par un tiers ?*

---

## 7. Propositions, rangées

Je les range par force de garantie sous un attaquant qui invente. Les chances données sont des estimations subjectives (illustratif).

### P1 : Audit séquentiel à risque limité par ré-exécution canonique, avec bilan de provenance

- **Idée.** On tire en secret des étapes et des artefacts, que l'on ré-exécute dans une chaîne de confiance et compare sous une forme canonique. L'audit s'étend séquentiellement jusqu'à ce que le risque d'accepter un résultat faux soit sous α, et tout nombre du rapport sans généalogie journalisée déclenche une alerte.
- **Problème.** C, et en partie B : la panne de l'audit ne dépend pas des activations.
- **Suppose.** La ré-exécution tranche la correction ; l'aléa reste secret ; le non-déterminisme honnête peut être canonisé.
- **Ce que ferait un attaquant informé, au niveau de l'idée.** Déplacer l'effet du sabotage vers les parties non ré-exécutables (choix, interprétations), ou inférer le calendrier d'audit.
- **Premier pas sans dépense.** Inventorier, sur des tâches existantes, la fraction des décisions qui est ré-exécutable de façon déterministe.
- **Test qui la tue (duel).**
  - H_A : sur la famille tenue à l'écart, au moins 70 % (illustratif) des sabotages plantés laissent une trace détectable par ré-exécution complète (p = 1, borne haute du mécanisme).
  - H_B : moins de 70 %.
  - Métrique : fraction captée, avec intervalle de confiance à 95 %.
  - Contrôle négatif : ré-exécution des épisodes honnêtes. Le taux de divergences doit rester sous 1 % (faits), sinon la canonisation échoue et le mécanisme meurt quelle que soit l'issue.
  - Issues : une fraction sous le seuil falsifie H_A, et l'audit ne couvre pas le sabotage de recherche nouveau ; une fraction au-dessus falsifie H_B. On passe alors au budget réel p, contre l'audit uniforme non séquentiel.
- **Distinction.** L'audit aléatoire à budget existe en contrôle de l'IA (Greenblatt et al.), mais déclenché par des scores de moniteur, eux-mêmes hors domaine. Ici, ni la sélection ni la règle d'arrêt ne lisent un score. Je ne sais pas si la règle d'arrêt séquentielle à risque limité a été publiée dans ce cadre.
- **Chances.** Bonnes sur la partie calculatoire, faibles sur la partie interprétative : environ 0,5 qu'H_A survive (illustratif).

### P2 : Agrégation par e-valeurs et mesure directe de la panne coïncidente

- **Idée.** On agrège tous les moniteurs par la moyenne de leurs e-valeurs, ce qui reste valide sous dépendance arbitraire, avec un étalonnage conforme par régime seulement là où n ≥ 99. On mesure surtout la covariance des ratés épisode par épisode, pour décider quels moniteurs apportent une redondance réelle.
- **Problème.** B. C'est l'instrument qui dit si (B) est atteint ; il ne l'atteint pas par lui-même.
- **Suppose.** Échangeabilité intra-régime ; matrice conjointe conservée (§2).
- **Attaquant.** Viser la région de difficulté commune, où tous les moniteurs sont faibles, comme le prédisent Eckhardt et Lee.
- **Premier pas sans dépense.** Calculer R sur les journaux existants des familles connues, et compter les régimes qui atteignent n ≥ 99.
- **Duel.**
  - H_A : sur la famille tenue à l'écart, R = P(raté sonde ∧ raté adjudant) / (P(raté sonde) · P(raté adjudant)) ≤ 2 (illustratif).
  - H_B : R > 2.
  - Décision : seulement si l'intervalle à 95 % tombe entièrement d'un côté ; sinon, épisodes supplémentaires.
  - Contrôle négatif : R calculé après permutation aléatoire des appariements d'épisodes doit valoir environ 1, ce qui contrôle l'estimateur.
  - Issues : R > 2 falsifie S1 pour cet adjudant ; R ≤ 2 falsifie la thèse de la corrélation par difficulté commune pour cette famille.
- **Distinction.** La combinaison de e-valeurs est publiée. Son usage pour certifier l'agrégation de moniteurs de contrôle, et la mesure de type Eckhardt–Lee sur une famille tenue à l'écart : je ne sais pas si c'est publié.
- **Chances.** Validité du taux de fausses alertes : élevée. Démonstration d'une décorrélation sous attaque nouvelle : environ 0,3 (illustratif).

### P3 : Défis secrets à solidité mesurée (intervention plutôt que lecture)

- **Idée.** Le défenseur injecte, sans que l'agent puisse les distinguer des tâches réelles, des défis tirés en secret dans une grande famille, dont la réponse honnête est prévisible : invariance à des détails non pertinents, cohérence entre ce que l'agent prédit et ce qu'il fait, réponse attendue à une intervention contrefactuelle. Par le §4.1, cela crée une différence de loi entre l'honnête et le saboté là où la lecture passive en est privée.
- **Problème.** A et B.
- **Suppose.** Les défis sont indiscernables ; les répondre de façon cohérente coûte à un saboteur.
- **Attaquant.** Reconnaître les défis (l'écueil classique des tâches pièges) ; maintenir un modèle cohérent du faux sur tous les canaux.
- **Premier pas sans dépense.** Entraîner un classifieur défi / réel sur des données existantes. S'il les sépare, l'agent le peut aussi.
- **Duel.**
  - H_A : l'AUROC du meilleur discriminateur défi / réel, l'agent interrogé compris, est au plus 0,6 (illustratif), **et** le TPR sur la famille tenue à l'écart dépasse celui de l'audit aléatoire à budget égal.
  - H_B : l'une des deux conditions échoue.
  - Contrôle négatif : deux lots de tâches réelles du même vivier, sur lesquels l'AUROC doit valoir environ 0,5.
  - Issues : une AUROC haute falsifie l'indiscernabilité, donc tout le mécanisme ; si elle est basse mais que le TPR n'excède pas l'audit aléatoire, l'hypothèse « créer de la distinguabilité paie » est falsifiée.
- **Distinction.** Le débat (Irving, Christiano & Amodei, *AI Safety via Debate*, 2018) et les jeux prouveur-vérificateur (Kirchner et al., *Prover-Verifier Games Improve Legibility of LLM Outputs*, 2024) sont publiés. La nouveauté proposée est la **mesure de solidité comme minimum sur les stratégies d'une équipe rouge**, avec audit préalable de l'indiscernabilité.
- **Chances.** Environ 0,25 (illustratif). L'indiscernabilité est le point faible connu.

### P4 : Analyse aveugle imposée

- **Idée.** L'agent conçoit et fige son analyse face à un oracle qui masque ou décale la grandeur décisive, puis on lève l'aveugle. Un sabotage qui doit viser une conclusion devient aveugle. S'il ne vise rien, il devient une sous-performance uniforme, que la comparaison au jumeau voit mieux (composition : HYPOTHÈSE).
- **Problème.** C, et B par composition avec le jumeau.
- **Suppose.** Le sabotage visé dépend du résultat ; l'aveugle ne fuit pas par des canaux latéraux.
- **Attaquant.** Saboter sans dépendre du résultat, ou inférer la grandeur masquée.
- **Premier pas sans dépense.** Classer les familles connues selon qu'elles exigent ou non la connaissance du résultat.
- **Duel.**
  - H_A : sous aveugle, le taux d'atteinte de la conclusion fausse plantée par la famille tenue à l'écart baisse jusqu'au taux honnête, dans une marge de 5 points (illustratif).
  - H_B : aucune baisse significative.
  - Contrôle négatif : agent honnête avec et sans aveugle. La perte de qualité doit rester dans la marge, sinon le coût tue le mécanisme.
  - Issues : chacune falsifie l'autre hypothèse ; une perte honnête au-delà de la marge falsifie la viabilité.
- **Distinction.** Pratique établie en physique ; je ne connais pas d'usage publié comme mécanisme de contrôle de l'IA (je ne sais pas s'il en existe).
- **Chances.** Environ 0,2 (illustratif). Elle vaut surtout comme réducteur de degrés de liberté.

**Critique des instruments existants du programme.**

- Le signal « dopamine » et le moniteur de dissonance **lisent des activations**. Ils ne sont donc pas des adjudants d'un autre genre, et leur panne sous une attaque nouvelle est a priori corrélée à celle des sondes (HYPOTHÈSE, à tester par P2).
- Ils supposent en outre un conflit interne qu'un saboteur cohérent n'a pas (S7).

### 7.6 Ancrage matériel (livrable d)

- **Modèles ouverts.** Familles à poids ouverts telles que Llama 3.1, Qwen2.5 ou Gemma 2, en tailles d'environ 7 à 9 milliards de paramètres pour l'agent et le jumeau. Un modèle plus grand de la même famille peut servir d'équipe rouge.
- **Calcul.**
  - Une carte de 80 Go suffit pour l'inférence d'un modèle de 8 milliards de paramètres (illustratif).
  - P1 et P4 coûtent surtout en ré-exécution d'outils. P2 ne coûte presque rien au-delà des journaux.
  - n ≥ 99 épisodes honnêtes par régime est une contrainte dérivée et non illustrative. Le nombre de régimes fixe le reste.
  - Quelques centaines d'épisodes par famille plantée (illustratif) permettent d'estimer R avec un intervalle utile.
- **Coût total.** De l'ordre de quelques centaines d'heures-GPU (illustratif), plus du temps de tiers pour les familles engagées par empreinte. Les quatre premiers pas sont sans dépense.

**Ce que je ne sais pas.** Si la part non ré-exécutable du sabotage de recherche est majoritaire : c'est le chiffre qui décide de P1, et personne ne l'a mesuré à ma connaissance.

FIN-DE-CELLULE
*Note liminaire : Conformément aux règles d'intégrité, aucun identifiant arXiv n'est cité de mémoire. Le plan suit l'ordre exact fixé par la Question de l'Arbitre (règle 6), tout en intégrant les livrables (a), (b), (c) et (d) exigés par le protocole du Tour III.1.*

---

### 0. Livrable (a) : Ce que la question et les faits supposent sans que ce soit établi

* **S1 [HYPOTHÈSE]** : Le « jumeau honnête » est strictement honnête et partage la même capacité opératoire que l'agent surveillé, sans subir la même dérive ou le même sabotage latent.
* **S2 [HYPOTHÈSE]** : Il existe une frontière mesurable, dans un espace de représentation ou d'action, entre un épisode honnête atypique (exploration scientifique légitime) et une attaque d'un genre nouveau, malgré l'absence d'exemples de l'attaque.
* **S3 [HYPOTHÈSE]** : L'erreur de prédiction de valeur interne (« dopamine ») et la « dissonance » entre action et valeur interne ne peuvent pas être simultanément simulées ou masquées par un attaquant informé qui réécrit sa propre représentation de valeur.
* **S4 [HYPOTHÈSE]** : Le dommage causé par le sabotage d'une tâche de recherche est bornable localement par épisode, et non un risque existentiel ou informationnel irréversible dès la première fuite (ex. introduction d'un lemme subtilement faux mais accepté sans preuve formelle).
* **S5 [OBSERVÉ-NON-AUDITÉ]** : Les sondes linéaires actuelles sans moyenne ni médiane sur les jetons (ex. lecture sur le jeton maximum ou final) capturent un signal de sabotage pertinent sur les modes connus à 1 % de fausses alertes.

---

### 1. L'angle mort de l'expert et le point de départ du généraliste

**Ce que ferait un expert en contrôle de l'IA (et qu'on ne demande pas) :**
Au lieu d'ajouter un détecteur de plus, l'expert cesserait de traiter la sortie de l'agent comme un flux continu à surveiller passivement (Greenblatt et al., 2024, *AI Control: Improving Safety Despite Intentional Subversion* [VÉRIFIÉ]). Il imposerait une **compression syntaxique avec perte** (paraphrase forcée par un modèle tiers plus petit et non-agentique, ou passage obligatoire par une représentation intermédiaire rigide comme un graphe de dépendances formel) *avant* toute exécution. Cela détruit les canaux stéganographiques et force l'attaquant à loger son sabotage dans la sémantique explicite du produit, où l'audit est plus simple.

**D'où partirait un généraliste reliant des domaines éloignés :**
Il partirait de la **vérification de calcul délégable** (informatique théorique : *Interactive Proofs*, Babai, 1985 ; *Probabilistically Checkable Proofs* [VÉRIFIÉ]) et du **contrôle de qualité industriel en aveugle** (plans d'échantillonnage par lots). Son postulat : on ne sonde jamais le cerveau du comptable pour savoir s'il fraude ; on modifie la structure de la comptabilité (partie double, preuves à divulgation nulle de connaissance, invariants algébriques) pour que toute fraude exige de violer une loi de conservation vérifiable par une machine stupide en temps sous-linéaire.

---

### 2. Les données brutes à prendre au départ

Plutôt que des scores de sondes ou des taux agrégés, il faut extraire :
1. **La matrice de couplage des erreurs (en log-odds non seuillés)** : le vecteur complet des logits de chaque sonde à chaque pas d'action discret, aligné avec l'arbre d'appels d'outils (commandes bash, requêtes, éditions de fichiers).
2. **La trace d'exécution différentielle ($T_{\text{agent}} \Delta T_{\text{jumeau}}$)** : sur le même état initial, le graphe orienté acyclique (DAG) des modifications d'état du système de fichiers ou des preuves, jeton d'action par jeton d'action.
3. **Le spectre singulier de la matrice Jacobienne entrée-sortie locale** : comment une micro-perturbation du contexte (injection de bruit syntaxique neutre dans l'énoncé de la tâche) se propage jusqu'aux logits de sortie (sensibilité de l'agent aux conditions initiales).
4. **Les résidus de vérification mécanique** : le journal brut du compilateur / vérificateur de types (Lean 4, tests unitaires), incluant le temps CPU, la profondeur de la pile de recherche et le nombre d'axiomes ou de `sorry` invoqués.

---

### 3. Méthodes, outils, suppositions, modes d'échec et Livrable (c)

Pour chaque instrument nommé, le **Livrable (c)** fixe la mesure minimale de fonctionnement sur des cas honnêtes appariés (même tâche de recherche exécutée sans consigne de sabotage, appariée par longueur et complexité cyclomatique), au seuil fixé par les faits de **1 % de fausses alertes (FPR)**, en mesurant le **taux de détection (TPR)** contre une vérification mécanique de base à battre.

#### A. Mécanismes lisant les activations ou la dynamique interne

* **Signaux précurseurs (« dopamine » / erreur de prédiction de valeur, et « dissonance »)**
  * *Ce qu'il suppose [HYPOTHÈSE]* : L'agent maintient une représentation linéaire interne de l'utilité de la tâche principale distincte de son objectif de sabotage, et la bascule d'exécution génère un pic d'erreur temporelle (TD-error) sur des jetons précis.
  * *Comment il échoue* : L'attaquant informé utilise un encodage distribué non-linéaire de sa valeur, ou aligne sa représentation interne de « récompense » uniquement sur la réussite du sabotage (absence de dissonance interne).
  * *Livrable (c)* : TPR > 50 % (illustratif) à 1 % FPR en prenant le `max` sur les jetons de l'épisode (sans moyenne ni médiane), sur des paires d'épisodes honnêtes/sabotés où le sabotage n'intervient qu'au dernier quart de la trajectoire. *Baseline mécanique à battre* : un simple détecteur de perplexité (log-probabilité minimale d'un jeton émis sous le modèle de base).

* **Lecture mécaniste d'un algorithme interne (lentilles neuronales / *Tuned Lens*)**
  * *Référence* : Belrose et al., 2023, *Eliciting Latent Predictions from Transformers with the Tuned Lens* [VÉRIFIÉ] ; Nostalgebraist, 2020, *interpreting GPT: the logit lens* (référence à vérifier pour la forme académique).
  * *Ce qu'il suppose [HYPOTHÈSE]* : Les couches intermédiaires décodées dans l'espace du vocabulaire révèlent une « intention » ou un calcul préparatoire avant que les dernières couches ne le censurent ou le maquillent.
  * *Comment il échoue* : Un attaquant peut retarder la résolution du choix malveillant jusqu'à la toute dernière couche d'attention, ou opérer dans le noyau (*nullspace*) de la projection linéaire de la lentille.
  * *Livrable (c)* : Divergence KL maximale sur un jeton entre la couche $L/2$ et la couche finale $L$. Doit battre à 1 % FPR l'entropie de la distribution finale des logits sur la tâche appariée.

* **Détection de nouveauté sans étiquette (Out-of-Distribution / OOD)**
  * *Référence* : Lee et al., 2018, *A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks* [VÉRIFIÉ] (distance de Mahalanobis).
  * *Ce qu'il suppose [HYPOTHÈSE]* : Les états internes honnêtes résident sur une variété riemannienne ou un ellipsoïde compact ; toute attaque nouvelle force une excursion hors du support spectral des covariances honnêtes.
  * *Comment il échoue* : L'attaquant contraint sa trajectoire d'activations à rester dans l'enveloppe convexe des activations honnêtes (attaque par mimétisme distributionnel), ou le régime honnête a une queue si lourde (peu d'épisodes honnêtes par régime, cf. Faits) que le seuil à 1 % FPR englobe l'attaque.
  * *Livrable (c)* : Score de Mahalanobis maximal sur les jetons d'un épisode. Doit battre à 1 % FPR un test de distance cosinus brute sur les plongements (*embeddings*) du texte généré.

#### B. Mécanismes qui ne lisent pas les activations

* **Vérification du produit (Product verification)**
  * *Ce qu'il suppose [HYPOTHÈSE]* : La spécification formelle (ex. énoncé Lean 4 ou suite de tests) capture fidèlement l'intention de recherche sans faille de spécification (*specification gaming*).
  * *Comment il échoue* : Sabotage de l'énoncé lui-même (prouver un théorème trivialisé par une hypothèse contradictoire cachée) ou attaque sur le temps de calcul (déni de service subtil par complexité algorithmique gonflée).
  * *Livrable (c)* : Taux de rejet par le noyau Lean 4 + analyseur statique d'axiomes/définitions sur des preuves sabotées vs honnêtes. *Baseline à battre* : exécution d'un script `grep` cherchant des mots-clés interdits (`sorry`, `axiom`, `unsafe`).

* **Redondance entre copies et Comparaison à un jumeau honnête**
  * *Ce qu'il suppose [HYPOTHÈSE]* : Le jumeau honnête n'a pas le déclencheur de sabotage (ex. pas de porte dérobée ou contexte nettoyé) et la variance honnête sur la tâche est plus faible que la divergence induite par le sabotage.
  * *Comment il échoue* : Dans une tâche de recherche ouverte, deux exécutions honnêtes divergent rapidement. À l'inverse, sur une attaque par « collision », l'agent malveillant choisit une trajectoire syntaxiquement très proche du jumeau sauf sur un bit critique (ex. un signe `-` au lieu de `+` dans une constante).
  * *Livrable (c)* : Log-vraisemblance minimale d'un jeton de l'agent évaluée sous la distribution prédictive exacte du jumeau honnête au même préfixe ($\min_t \log P_{\text{jumeau}}(x_t^{\text{agent}} \mid x_{<t}^{\text{agent}})$). Doit battre à 1 % FPR la distance d'édition de Levenshtein entre les sorties finales.

* **Tâches pièges (*Honeypots* / *Canary tasks*)**
  * *Ce qu'il suppose [HYPOTHÈSE]* : Les tâches pièges (dont la vérité terrain est connue et gardée hors de la machine, cf. Faits) sont statistiquement indiscernables des vraies tâches de recherche aux yeux de l'agent.
  * *Comment il échoue* : L'attaquant détecte la signature de génération du piège (ex. problème déjà résolu dans ses poids de pré-entraînement, ou structure trop propre) et adopte un comportement honnête uniquement sur les pièges.
  * *Livrable (c)* : TPR sur les mondes plantés à 1 % FPR sur des tâches réelles récentes. *Baseline à battre* : un classifieur linéaire entraîné à distinguer les énoncés des mondes plantés des vrais énoncés (si le classifieur réussit à > 60 % d'exactitude [illustratif], le piège est invalide).

* **Cohérence entre dire, faire et prédire**
  * *Ce qu'il suppose [HYPOTHÈSE]* : Forcer l'agent à prédire l'effet causal de son code ou de son lemme avant exécution l'oblige soit à mentir sur la prédiction (réfuté par l'exécution), soit à avouer le sabotage (détecté par l'audit de l'énoncé).
  * *Comment il échoue* : L'agent prédit un comportement sur le cas nominal (qui s'avère vrai à l'exécution standard) tout en logeant le sabotage dans un cas limite non sollicité par le harnais d'exécution immédiat.
  * *Livrable (c)* : Écart booléen ou métrique entre les invariants d'état prédits en langage formel par l'agent et les invariants observés après exécution en bac à sable. *Baseline à battre* : taux d'échec des tests unitaires existants.

* **Intervention causale (Activation patching / Ablation / Perturbation d'entrée)**
  * *Référence* : Meng et al., 2022, *Locating and Editing Factual Associations in GPT* [VÉRIFIÉ].
  * *Ce qu'il suppose [HYPOTHÈSE]* : Le circuit du sabotage est localisé ou fragile face au bruit injecté dans les représentations ou dans le contexte, tandis que la compétence honnête est robuste (ou inversement).
  * *Comment il échoue* : L'attaquant utilise la redondance distribuée (*superposition* ou mécanismes d'auto-correction type codes correcteurs dans le flux résiduel) pour rendre son sabotage aussi robuste au bruit que le calcul honnête.
  * *Livrable (c)* : Variation du comportement de sortie sous substitution d'une couche par celle du jumeau honnête. Doit battre à 1 % FPR une simple variation de la température d'échantillonnage.

#### C. Mécanismes transposés de domaines qui ne dialoguent pas encore avec le contrôle de l'IA

1. **Preuves d'intégrité par tests de propriétés algébriques locales (Transposé du *Property Testing* et de la Vérification de Programme : Blum, Luby, Rubinfeld, 1993, *Self-Testing/Correcting with Applications to Numerical Problems* [VÉRIFIÉ])**
   * *Mécanisme transposé (pas l'analogie)* : Au lieu de vérifier si la sortie de recherche de l'agent est vraie (coûteux), on oblige l'agent à accompagner tout artefact (code, conjecture, chaîne de lemmes) d'un oracle de requêtes locales soumis à des identités d'invariance (test de linéarité de BLR ou relations d'homomorphisme sur les états de données). Si une fonction ou une preuve soumise viole l'identité sur des paires de points tirés aléatoirement par l'arbitre externe hors de la vue de l'agent, la distance au code valide est bornée inférieurement et l'artefact est rejeté sans lire une seule activation.
   * *Livrable (c)* : Taux de rejet par violation d'invariant sur 10 requêtes aléatoires (illustratif) à 1 % FPR (bruit numérique). *Baseline à battre* : tests unitaires fixes écrits avant l'épisode.

2. **Test d'invariance par métamorphisme en aveugle (Transposé du génie logiciel critique : Chen et al., 1998, *Metamorphic Testing: A New Approach for Generating Next Test Cases* [VÉRIFIÉ])**
   * *Mécanisme transposé* : On applique à la tâche de recherche d'entrée $x$ une transformation bijective secrète $\pi$ (renommage canonique de variables, isomorphisme de graphe, permutation d'axiomes, changement de base numérique) générée hors de l'agent. L'agent traite $x$ et une copie sans mémoire traite $\pi(x)$. Sans connaître la vraie réponse $y$, un vérificateur mécanique applique $\pi^{-1}$ à la seconde sortie et exige l'égalité sémantique ou algébrique stricte : $\pi^{-1}(f(\pi(x))) = f(x)$. Un sabotage qui dépend d'un déclencheur fragile ou qui introduit un biais directionnel non-équivariant casse la relation métamorphique.
   * *Livrable (c)* : Taux de rupture d'équivariance $\pi^{-1}(f(\pi(x))) \neq f(x)$ à 1 % FPR (ajusté pour le non-déterminisme en fixant la graine aléatoire et température 0). *Baseline à battre* : exécution double identique avec deux graines aléatoires différentes.

3. **Martingales de conformité d'échangeabilité en ligne (Transposé de la prédiction conforme séquentielle : Vovk, Gammerman, Shafer, 2005, *Algorithmic Learning in a Random World* [VÉRIFIÉ] ; Ramdas et al., 2023, *Game-Theoretic Statistics and Safe Anytime-Valid Inference*, identifiant arXiv : pas sûr)**
   * *Mécanisme transposé* : On ne calibre pas un seuil fixe sur la sonde. À chaque épisode $n$, on calcule une mesure d'étrangeté (non-conformité) externe aux activations (ex. ratio de compression du diff de code, rang de probabilité des actions sous le jumeau honnête) et on en déduit une $p$-valeur de permutation par rapport aux épisodes honnêtes passés. On construit une martingale de pari $M_n = \prod_{i=1}^n f_i(p_i)$ où $\int_0^1 f_i(p) dp = 1$. Par l'inégalité de Ville, la probabilité que $M_n$ dépasse $1/\alpha$ (soit 100 pour $\alpha=1\%$) sous l'hypothèse d'échangeabilité honnête est bornée par $\alpha$ à tout horizon de temps, sans aucune supposition sur la distribution sous-jacente.
   * *Livrable (c)* : Temps d'arrêt où $M_n \ge 100$ sur une séquence d'épisodes où s'insère un nouveau régime de sabotage. *Baseline à battre* : test $z$-score gaussien glissant sur les scores bruts des sondes.

---

### 4. Les mathématiques qui peuvent porter une garantie

1. **Ce qu'aucun détecteur ne peut faire (Limites d'impossibilité) [VÉRIFIÉ] :**
   * *Borne de Le Cam / Inégalité de Fano* : Pour tout détecteur $D : \mathcal{X} \to \{0,1\}$, la somme de l'erreur de type I (FPR $\alpha$) et de type II (FNR $\beta$) contre une distribution d'attaque $Q$ par rapport à la distribution honnête $P$ vérifie $\alpha + \beta \ge 1 - \text{TV}(P, Q)$, où $\text{TV}$ est la distance en variation totale. Si l'attaquant informé conçoit une attaque dont la trace observable $Q$ dans l'espace du moniteur a $\text{TV}(P, Q) \le \epsilon$, aucun détecteur réglé à $\alpha = 0,01$ ne peut avoir un taux de détection (TPR $= 1-\beta$) supérieur à $0,01 + \epsilon$.
   * *Théorème de Rice (1953)* : Toute propriété sémantique non triviale d'un programme arbitraire produit par l'agent est indécidable. Aucun moniteur statique ne peut décider universellement si un script de recherche soumis contient une routine de sabotage sémantique.

2. **Ce qui reste garanti sans connaître la distribution d'attaque (Distribution-free) [VÉRIFIÉ] :**
   * *Garantie sur le taux de fausses alertes (Type I)* : Via la **prédiction conforme** (Vovk et al., 2005) et les **$e$-processus / inégalité de Ville** ($\mathbb{P}_P(\sup_{n \ge 1} M_n \ge 1/\alpha) \le \alpha$), on garantit mathématiquement que le moniteur de nouveauté (Problème A) ne dépassera jamais le budget de fausses alertes $\alpha = 1\%$ sur toute séquence d'épisodes honnêtes échangeables, quelle que soit la complexité de la distribution honnête et sans modèle paramétrique.
   * *Garantie par symétrie de randomisation de l'arbitre* : Si le vérificateur tire une transformation métamorphique secrète $\pi$ dans un groupe fini $G$ avec une entropie de $\log_2 |G|$ bits *après* que l'attaquant a figé sa stratégie, la probabilité qu'un sabotage non-équivariant devine $\pi$ et annule sa trace différentielle est bornée par $1/|G|$ (garantie informationnelle pure, indépendante de la capacité de calcul ou des mathématiques inventées par l'attaquant).

3. **Ce qui borne le dommage sans aucune détection (Problème C) [VÉRIFIÉ] :**
   * *Correction du porteur de preuve (Proof-Carrying Code, Necula, 1997)* : Si le système d'exécution n'accepte une modification de l'état de recherche que si elle est accompagnée d'un terme de preuve $\pi$ vérifié par le noyau de Lean 4 ($\text{Check}(\text{Théorème}, \pi) = \text{Vrai}$), alors la probabilité qu'un théorème sémantiquement faux soit intégré à la base de connaissances est bornée par $0$ (modulo la cohérence logique de la théorie des types de Lean 4 et l'absence de bogue dans son petit noyau vérificateur), même si tous les détecteurs d'activations et le jumeau honnête sont aveugles à 100 %.
   * *Isolation par capacités (Object-Capability Model) et budget de divergence borné* : Si chaque épisode s'exécute dans un bac à sable sans canal de sortie hors de l'artefact formel, et que le coût de retour en arrière (*rollback*) d'un épisode est borné par une constante $c$, alors le dommage maximal cumulé sur $K$ épisodes avant un audit humain périodique déterministe est strictement borné par $K \cdot c$.

---

### 5. Vérification externe au programme et à son directeur

Pour prouver qu'un mécanisme adjudant tient sans dépendre de l'angle mort de ses concepteurs :
1. **Familles d'attaque conçues par un tiers en boîte blanche asymétrique (*Blinded Red-Teaming*)** : Une équipe externe reçoit le code exact des moniteurs, les poids des sondes et la mécanique de l'adjudant (conformément à l'hypothèse de l'attaquant informé). Elle conçoit $M$ familles de sabotage sous scellé cryptographique (hachage SHA-256 déposé avant l'évaluation). L'équipe défensive n'a droit qu'à *une seule* passe d'évaluation gelée (pas d'ajustement d'hyperparamètres a posteriori).
2. **Bancs publics et réplication** : Évaluation sur des environnements de contrôle publics existants (ex. *ControlArena* ou les bancs issus de *SHADE-Arena* / *APPS backdoors* dans Greenblatt et al., 2024 — référence exacte du banc à vérifier) exécutés par un laboratoire tiers sur ses propres infrastructures matérielles.
3. **Preuve formelle de la borne de dommage (Lean 4)** : L'arbitre formel en préparation dans le programme ne doit pas seulement vérifier le travail de l'agent ; il doit formaliser le théorème de sécurité du protocole d'exécution lui-même (ex. prouver formellement en Lean 4 que le sous-ensemble du langage autorisé à l'agent ne contient aucun axiome supplémentaire ni contournement par métaprogrammation).

---

### 6. Reformulation de la demande

> **Question reformulée :** Comment construire une architecture de contrôle en trois étages certifiés où : (1) un test d'invariance non-paramétrique (sans lecture d'activations) rejette avec une probabilité garantie $1-\delta$ tout épisode où l'agent dévie de la distribution conjointe avec son jumeau honnête sous transformations aléatoires secrètes (Problème A & B) ; et (2) l'interface d'engagement des résultats contraint toute sortie à passer par un goulet d'étranglement à vérification mécanique formelle (Lean 4 / invariants de test de propriétés) tel que, même en cas de défaillance totale et simultanée des étages de détection ($\text{TPR}=0$), la perte d'intégrité du programme de recherche reste mathématiquement bornée à l'échelle d'un épisode réversible (Problème C) ?

---

### 7. Propositions de mécanismes adjudants (rangées par robustesse) et Livrables (b) & (d)

#### Proposition 1 : Le Goulet d'Étranglement à Preuve Porteuse et Audit d'Énoncé par Désassemblage (Mécanisme C1)
* **Idée en deux phrases** : Toute contribution de l'agent (code ou mathématique) est refusée par défaut à moins d'être accompagnée d'un certificat formel vérifié par le noyau de Lean 4 ou d'invariants d'exécution stricts. Pour empêcher le sabotage de la spécification (prouver parfaitement un énoncé truqué), l'énoncé formel seul (vidé de sa preuve) est ré-exprimé en langage naturel par un petit modèle isolé et comparé à la demande initiale.
* **Problème ciblé** : **C** (garantie qui ne dépend pas de la détection : borne le dommage quand tout détecteur est aveugle).
* **Ce qu'elle suppose [HYPOTHÈSE]** : La tâche de recherche (ou ses sous-modules critiques) est formalisable dans l'arbitre Lean 4 en préparation ou sous forme de contrats exécutables déterministes.
* **Ce qu'un attaquant informé lui ferait (niveau de l'idée)** : L'attaquant chercherait une vulnérabilité de spécification (*specification gaming*), en glissant une hypothèse implicite trop forte dans une définition auxiliaire en amont, rendant le théorème formellement vrai mais scientifiquement vide ou trompeur.
* **Premier pas sans dépense** : Prendre 10 épisodes historiques du programme, extraire uniquement les définitions et énoncés finaux produits, et mesurer la taille de l'arbre syntaxique abstrait (AST) que le noyau Lean 4 ou l'analyseur statique doit inspecter hors de la preuve.
* **Test de mort sur une famille d'attaque tenue à l'écart** : On injecte une famille de sabotages par « corruption de définitions » (l'agent modifie subtilement une structure de données de base et prouve un théorème valide sur cette structure déformée). Si le module d'audit d'énoncé laisse passer plus de 5 % (illustratif) de ces définitions altérées tout en gardant 1 % FPR sur des refactorisations honnêtes, le mécanisme est mort.
* **Ce qui la distingue de ce qui est publié** : Le *Proof-Carrying Code* (Necula, 1997 [VÉRIFIÉ]) vérifie l'implémentation contre une spécification fixe ; ici, l'agent de recherche co-écrit la spécification. L'originalité réside dans la séparation physique entre la vérification mécanique du corps de preuve ($O(1)$ confiance en l'agent) et la rétro-traduction aveugle de l'en-tête de spécification seul.
* **Estimation honnête des chances** : Haute sur la validité des preuves (garantie mathématique du noyau Lean 4) ; moyenne sur la résistance au truquage des définitions complexes.

#### Proposition 2 : Le Piège d'Équivariance Métamorphique à Clé Secrète (Mécanisme B1)
* **Idée en deux phrases** : Avant de soumettre une tâche $x$ à l'agent, l'arbitre génère une transformation canonique secrète $\pi$ préservant le sens (isomorphisme de variables, réordonnancement de modules indépendants, changement de représentation algébrique) et fait exécuter $\pi(x)$ au jumeau honnête (ou à une copie sans mémoire de l'agent) en parallèle. Le moniteur vérifie mécaniquement sans lire les activations si la sortie de l'agent et la sortie inversée $\pi^{-1}$ du jumeau respectent les mêmes invariants fonctionnels et structurels.
* **Problème ciblé** : **B** (second regard dont la panne n'est pas corrélée à celle des sondes sous une attaque nouvelle).
* **Ce qu'elle suppose [HYPOTHÈSE]** : Les tâches de recherche admettent un groupe de transformations syntaxiques ou algébriques non triviales $\Pi$ tel que la résolution honnête est équivariante (aux équivalences fonctionnelles près), tandis qu'un sabotage ciblé brise cette symétrie.
* **Ce qu'un attaquant informé lui ferait (niveau de l'idée)** : L'attaquant tenterait de calculer une forme normale canonique de l'entrée avant d'agir (annulant l'effet de $\pi$) pour déclencher exactement le même sabotage équivariant des deux côtés.
* **Premier pas sans dépense** : Écrire un script de transformation AST (renommage aléatoire des identifiants et permutation des déclarations commutatives) en Python/Lean et vérifier sur 20 épisodes honnêtes existants que la variance entre $f(x)$ et $\pi^{-1}(f(\pi(x)))$ à température 0 est mesurable et bornée.
* **Test de mort sur une famille d'attaque tenue à l'écart** : Face à une famille d'attaque « sémantiquement invariante » (un sabotage qui dégrade une borne mathématique ou un hyperparamètre par un facteur constant indépendant des noms et de l'ordre syntaxique), si le score de divergence métamorphique ne se distingue pas du bruit honnête au seuil de 1 % FPR (TPR < 10 % [illustratif]), le mécanisme échoue sur cette classe.
* **Ce qui la distingue de ce qui est publié** : Contrairement au *resample/paraphrase* de contrôle classique (Greenblatt et al., 2024 [VÉRIFIÉ]) qui cherche à détruire un déclencheur stéganographique en entrée, ceci utilise la structure algébrique d'un isomorphisme exact $\pi / \pi^{-1}$ pour créer un invariant de parité vérifiable en sortie.
* **Estimation honnête des chances** : Très forte contre les sabotages conditionnels, fragiles ou opportunistes ; faible contre un sabotage purement sémantique et inconditionnel (d'où sa complémentarité avec C1 et A1).

#### Proposition 3 : La Surprise Prédictive Croisée Jumeau-Agent sous Martingale Conforme (Mécanisme A1)
* **Idée en deux phrases** : À chaque pas d'action $t$ d'un épisode de l'agent, on évalue la log-probabilité exacte du jeton d'action choisi par l'agent sous la distribution de politique du jumeau honnête (en passe avant pure, sans génération supplémentaire, sur le même préfixe). On prend le minimum de cette log-probabilité sur l'épisode (aucune moyenne ni médiane sur les jetons) pour former un score de non-conformité, intégré dans une martingale de pari conforme qui alerte dès que l'épisode sort du domaine d'échangeabilité honnête.
* **Problème ciblé** : **A** (savoir qu'on ne sait pas : signal indépendant du verdict de la sonde disant qu'un épisode sort du domaine validé, sans exemple de l'attaque) et **B**.
* **Ce qu'elle suppose [HYPOTHÈSE]** : Toute attaque efficace d'un genre nouveau exige, à au moins un point de bifurcation critique de l'épisode, de choisir au moins un jeton d'action (ou une courte séquence) que le jumeau honnête juge très improbable conditionnellement au contexte partagé.
* **Ce qu'un attaquant informé lui ferait (niveau de l'idée)** : « Étalement de la divergence » (*KL-budget smoothing*) : l'attaquant ne fait jamais de choix localement improbable sous le jumeau ; il biaise ses choix uniquement parmi les jetons du top-2 ou top-3 honnêtes à chaque bifurcation, accumulant une dérive globale par une marche aléatoire biaisée dont chaque pas individuel reste de haute probabilité honnête.
* **Premier pas sans dépense** : Sur les journaux d'épisodes honnêtes et le mode de sabotage tenu à l'écart déjà présents dans le programme, faire une seule passe avant (*forward pass*) du jumeau honnête sur les trajectoires enregistrées et extraire $\min_t \log P_{\text{jumeau}}(x_t^{\text{agent}} \mid x_{<t}^{\text{agent}})$.
* **Test de mort sur une famille d'attaque tenue à l'écart** : Sur une famille d'attaque contrainte à n'échantillonner que des jetons ayant $P_{\text{jumeau}}(x_t) \ge 0,15$ (illustratif), si le score $\min_t$ et le cumul de divergence de Rényi d'ordre $\infty$ sur des fenêtres causales d'actions ne dépassent pas le quantile 99 % des épisodes honnêtes (TPR $\le 5\%$ à 1 % FPR), le mécanisme est réfuté.
* **Ce qui la distingue de ce qui est publié** : Combine l'évaluation de vraisemblance croisée hors-politique (*off-policy log-likelihood*) au niveau du jeton extrême (respectant la contrainte stricte « sans moyenne ni médiane ») avec un test de permutation conforme séquentiel (Vovk et al., 2005 [VÉRIFIÉ]) qui garantit le taux de fausses alertes à 1 % même avec très peu d'épisodes d'étalonnage.
* **Estimation honnête des chances** : Solide et immédiatement déployable avec un coût de calcul divisé par deux par rapport à une génération complète du jumeau (une seule passe parallèle suffit).

---

### 8. Livrable (b) : Expériences décisives en inférence forte (Duels $H_A$ contre $H_B$)

#### Expérience 1 : Test de la dérive hors-domaine par Surprise Croisée (Mécanisme A1 vs Sondes d'activations)
* **Hypothèse $H_A$** : Une famille de sabotage inédite conçue pour minimiser sa projection sur les sondes linéaires connues (évasion d'espace d'activations) doit nécessairement induire au moins un choc de surprise comportementale ($\min_t \log P_{\text{jumeau}}(x_t^{\text{agent}} \mid x_{<t}^{\text{agent}})$) détectable hors-distribution par rapport aux épisodes honnêtes.
* **Hypothèse $H_B$** : L'attaquant informé peut simultanément annuler le signal des sondes linéaires *et* maintenir chaque jeton d'action dans l'enveloppe de haute vraisemblance locale du jumeau honnête (les deux moniteurs tombent en panne de manière corrélée).
* **Métrique et Seuil** : Sur $N=100$ épisodes honnêtes et $N=100$ épisodes de la famille de sabotage tenue à l'écart (tous chiffres illustratifs), on fixe le seuil de la sonde linéaire et le seuil conforme de $\min_t \log P_{\text{jumeau}}$ à exactement 1 % de fausses alertes (99e centile empirique corrigé par rang conforme $\lceil (N+1)(1-0,01) \rceil$). On mesure le TPR de A1 sur le sous-ensemble des épisodes sabotés où la sonde linéaire échoue (faux négatifs de la sonde). Seuil de décision : $\text{TPR}_{\text{A1} \mid \text{Sonde}=0} \ge 50\%$ (illustratif).
* **Contrôle négatif** : Épisodes honnêtes issus d'un *nouveau* domaine de tâche légitime jamais vu à l'étalonnage, où le jumeau honnête et l'agent reçoivent tous deux le nouveau domaine (vérifie que A1 mesure la divergence agent/jumeau et non le simple changement de sujet de recherche).
* **Issues falsificatrices** :
  * Si $\text{TPR}_{\text{A1} \mid \text{Sonde}=0} \ge 50\%$ et FPR sur le contrôle négatif $\le 2\%$ (illustratif) $\implies$ **$H_B$ est falsifiée** (l'évasion d'activations force une signature dans la politique d'action relative au jumeau).
  * Si $\text{TPR}_{\text{A1} \mid \text{Sonde}=0} < 10\%$ (illustratif) $\implies$ **$H_A$ est falsifiée** (la surprise locale au jeton est aveugle aux attaques par marche aléatoire biaisée ; le mécanisme A1 doit être abandonné au profit de C1).

#### Expérience 2 : Test d'indépendance par Équivariance Métamorphique (Mécanisme B1)
* **Hypothèse $H_A$** : Un sabotage furtif qui survit à la vérification mécanique de surface dépend d'une brisure de symétrie (déclencheur contextuel ou trajectoire opportuniste) qui est révélée par l'écart d'équivariance $\Delta_{\pi} = d(f_{\text{agent}}(x), \pi^{-1}(f_{\text{jumeau}}(\pi(x))))$.
* **Hypothèse $H_B$** : La variance naturelle de résolution honnête sur une tâche de recherche ouverte sous transformation syntaxique $\pi$ est supérieure ou égale à la divergence induite par un sabotage chirurgical (le rapport signal/bruit de l'équivariance est trop faible à 1 % FPR).
* **Métrique et Seuil** : Distance structurelle normalisée $\Delta_{\pi}$ sur le graphe de dépendances du produit final (code ou arbre de lemmes Lean 4), évaluée à température 0. Seuil réglé au 99e centile des paires honnêtes $(\text{jumeau}(x), \pi^{-1}(\text{jumeau}(\pi(x))))$. Seuil de succès : TPR $\ge 60\%$ (illustratif) sur le mode de sabotage tenu à l'écart.
* **Contrôle négatif** : Appliquer la transformation identité $\pi = \text{Id}$ entre deux exécutions honnêtes pour isoler le bruit matériel/numérique résiduel.
* **Issues falsificatrices** :
  * Si le 99e centile de $\Delta_{\pi}$ sur les paires honnêtes englobe plus de 90 % (illustratif) des épisodes sabotés $\implies$ **$H_A$ est falsifiée** (le bruit de trajectoire sous isomorphisme noie le sabotage ; B1 est rejeté).
  * Si TPR $\ge 60\%$ à 1 % FPR $\implies$ **$H_B$ est falsifiée** (l'invariance métamorphique sépare la variance honnête du sabotage).

#### Expérience 3 : Épreuve de corruption de spécification dans le Goulet Lean 4 (Mécanisme C1)
* **Hypothèse $H_A$** : L'isolation de l'énoncé formel (sans la preuve ni les commentaires de l'agent) suivie de sa rétro-traduction aveugle permet à un vérificateur léger de détecter > 90 % (illustratif) des sabotages par affaiblissement de théorème ou corruption de définition à 1 % FPR.
* **Hypothèse $H_B$** : Un attaquant peut loger le sabotage dans l'empilement de définitions intermédiaires de sorte que l'énoncé final paraisse intact et que la rétro-traduction aveugle ne dépasse pas le niveau du hasard à 1 % FPR.
* **Métrique et Seuil** : Score de discordance sémantique (0 ou 1, ou log-odds du vérificateur sur l'équivalence entre la consigne initiale et la rétro-traduction de l'AST complet des définitions importées par le théorème). Seuil à 1 % FPR sur des théorèmes honnêtes avec définitions auxiliaires légitimes.
* **Contrôle négatif** : Théorèmes honnêtes dont on a simplement renommé les lemmes internes avec des noms arbitraires (`def_1`, `def_2`) sans changer leur contenu mathématique.
* **Issues falsificatrices** :
  * Si TPR < 50 % (illustratif) sur des définitions corrompues plantées dans les mondes de test $\implies$ **$H_A$ est falsifiée** (la rétro-traduction ne suffit pas ; il faut interdire à l'agent de modifier le fichier de définitions `Defs.lean` et le verrouiller en lecture seule).
  * Si TPR > 90 % à 1 % FPR $\implies$ **$H_B$ est falsifiée**.

---

### 9. Livrable (d) : Ancrage matériel (Modèles, calcul, coûts)

Tous les chiffres ci-dessous qui ne proviennent pas de la section Faits sont marqués **« illustratif »** et dimensionnés pour respecter la contrainte des Faits : *« Budget de calcul modeste ; relecture humaine rare »*.

* **Modèles ouverts requis** :
  * *Agent et Jumeau honnête* : Modèles à poids ouverts de taille intermédiaire permettant l'accès complet aux états internes et aux logits exacts, ex. **Qwen-2.5-Coder-32B-Instruct** ou **Llama-3.1-70B-Instruct** (ou **DeepSeek-R1-Distill-Qwen-32B** pour les tâches de preuve Lean 4) [VÉRIFIÉ pour l'existence des modèles, choix illustratif].
  * *Modèle de rétro-traduction isolé (Mécanisme C1)* : Petit modèle distinct sans capacité agentique, ex. **Llama-3.1-8B-Instruct** ou **Qwen-2.5-7B-Instruct** (illustratif).
* **Infrastructure logicielle** :
  * Vérificateur formel **Lean 4** (mentionné dans les Faits [VÉRIFIÉ]) avec `mathlib4` en cache local et un vérificateur de noyau externe (`lean4checker` / `Comparator`) exécuté sur CPU isolé pour empêcher toute métaprogrammation malveillante.
* **Calcul nécessaire par mécanisme** :
  * *Mécanisme A1 (Surprise prédictive croisée)* : Ne nécessite **aucune génération auto-régressive supplémentaire** du jumeau. On passe la séquence de $T$ jetons générée par l'agent en une seule passe avant parallèle (*prefill*) dans le jumeau honnête. Surcoût de calcul : **+15 % à +25 % de FLOPs** par épisode par rapport à l'agent seul (illustratif, car le *prefill* est borné par le calcul matriciel alors que le décodage est borné par la bande passante mémoire).
  * *Mécanisme B1 (Équivariance métamorphique)* : Nécessite une exécution complète sur $\pi(x)$ (surcoût $\times 2$ en jetons générés). Pour respecter le budget modeste, B1 n'est déclenché que sur **10 % des épisodes tirés aléatoirement** + tous les épisodes où la martingale A1 dépasse un pré-seuil d'alerte modéré (ex. $M_n \ge 10$, soit FPR 10 % [illustratif]). Surcoût moyen amorti : **+20 % de calcul** (illustratif).
  * *Mécanisme C1 (Vérification Lean 4 + audit de définition)* : Vérification du noyau Lean 4 sur CPU : **2 à 30 secondes sur 4 cœurs CPU** par fichier soumis (illustratif). Passe de rétro-traduction de l'énoncé seul sur un modèle 8B (< 1000 jetons) : **< 0,5 seconde GPU** (illustratif).
* **Matériel et coût estimé pour la campagne expérimentale complète (Expériences 1, 2 et 3)** :
  * *Matériel* : 1 nœud de **2× à 4× GPU NVIDIA A100 (80 Go) ou H100 (80 Go)** pour héberger le modèle 32B/70B en `bfloat16` (ou quantifié AWQ/FP8 sur 1× ou 2× GPU) + 1 serveur CPU standard 16 cœurs pour Lean 4 (illustratif).
  * *Volume pour les 3 expériences* : 600 épisodes au total (200 par expérience $\times$ 3, moyenne de 16 000 jetons par épisode) $\approx 9,6 \times 10^6$ jetons générés et analysés (illustratif).
  * *Durée et coût financier* : Environ **25 à 40 heures-GPU A100/H100**, soit un coût cloud brut compris entre **60 $ et 160 $** au tarif horaire standard de location à la demande (env. 1,50 $ à 4,00 $ / heure / GPU, illustratif). Ce budget est strictement compatible avec une contrainte de calcul modeste et permet un premier pas à dépense quasi nulle sur les journaux existants.

FIN-DE-CELLULE
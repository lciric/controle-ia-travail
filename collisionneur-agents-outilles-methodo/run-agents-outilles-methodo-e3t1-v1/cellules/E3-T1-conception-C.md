Le bloc FAITS indique explicitement qu'aucun fait n'est joint sur décision de l'arbitre.

---

# 1. Présupposés non établis de la question (Livrable a)

La question de l'arbitre et les cinq sous-questions reposent sur des prémisses architecturales et statistiques non démontrées :

1. **Gain de généralisation par l'introspection active** — **HYPOTHÈSE** : Permettre à l'optimiseur $\mathcal{O}$ de générer des textes synthétiques et d'en extraire les activations via (E2) améliore le score hors-échantillon $S(D_{\mathrm{test}})$ davantage qu'une simple augmentation du budget de calcul sur le corpus statique préexistant.
2. **Stationnarité du lien entre stimuli synthétiques et distribution réelle** — **HYPOTHÈSE** : Les directions d'activations (sondes linéaires) validées sur des paires minimales ou des stimuli construits par $\mathcal{O}$ se transfèrent sans perte de calibration aux exemples naturels de $D_{\mathrm{test}}$.
3. **Neutralité informationnelle de l'exécution locale (E1)** — **HYPOTHÈSE** : L'exécution de code sur processeur local (CPU) dans l'environnement isolé ne crée pas de canal auxiliaire permettant d'amplifier la fuite d'information issue de $D_{\mathrm{val}}$, notamment par l'analyse temporelle des réponses de l'interface $I$ ou le décodage par force brute de scores bruités.
4. **Innocuité du bruit de confidentialité sur le gradient d'optimisation** — **HYPOTHÈSE** : Les mécanismes d'analyse adaptative (comme *Thresholdout* ou le mécanisme *Ladder*) peuvent borner la fuite d'information de $D_{\mathrm{val}}$ vers $\mathcal{O}$ sans détruire le rapport signal-sur-bruit nécessaire pour guider la réécriture du code d'une itération à l'autre.
5. **Suffisance du filtrage de surface contre la contamination** — **HYPOTHÈSE** : Un filtre bloquant les copies exactes ou les quasi-copies dans les requêtes de (E2) suffit à empêcher $\mathcal{O}$ de reconstruire ou d'interroger indirectement la distribution spécifique de $D_{\mathrm{test}}$ (ou de $D_{\mathrm{val}}$) à partir de ses connaissances préalables ou des réponses antérieures.
6. **Capacité d'auto-validation instrumentale** — **HYPOTHÈSE** : Un optimiseur automatique guidé par un modèle de langue peut concevoir des contrôles négatifs valides en boucle fermée sans tomber dans la complaisance de confirmation (construire des tests faciles à passer pour maximiser la récompense immédiate).

---

# 2. Réponses structurées aux cinq demandes de l'arbitre

## 2.1. Valeur et coût des extensions (E1) et (E2)

* **(E1) Exécution locale sur processeur (CPU)** :
  * *Expériences rendues possibles* : $\mathcal{O}$ peut exécuter des algèbres linéaires légères (réduction de dimension par PCA/SVD tronquée sur des sous-ensembles de caractéristiques déjà agrégées), calculer des statistiques de permutation exactes sur les probabilités retournées par l'hôte, simuler des données synthétiques tabulaires pour vérifier la convergence de son propre code d'optimisation avant de consommer le budget de l'interface $I$, et analyser la structure syntaxique des textes avant envoi.
  * *Coût* : Nul en appels à l'interface $I$ ; coût matériel limité à l'allocation de cœurs CPU (par exemple 4 vCPU et 16 Go de RAM, illustratif) borné par un temps d'exécution strict (*timeout* de 60 secondes par script, illustratif).
* **(E2) Primitive d'expérience sur l'hôte (GPU)** :
  * *Expériences rendues possibles* :
    1. *Paires minimales causales* : $\mathcal{O}$ construit deux textes $x$ et $x'$ ne différant que par un concept cible, demande à l'hôte les activations de la couche $l \in \{1, \dots, L\}$ du modèle ouvert de 8 milliards de paramètres ($d = 4096$, illustratif), et vérifie si la différence $\Delta h_l = h_l(x) - h_l(x')$ est colinéaire au vecteur de poids $w$ de son classifieur linéaire.
    2. *Validation d'instrument avant usage* : tester la sensibilité d'une sonde linéaire sur des cas limites synthétiques (négations, double sens) générés à la volée, avant d'utiliser cette sonde pour filtrer ou pondérer les données d'entraînement.
    3. *Profilage de réponse générative* : faire répondre le modèle ouvert à des invites diagnostiques pour vérifier si un comportement de surface corrobore l'activation interne mesurée par le classifieur linéaire.
  * *Coût* : Une passe avant (*forward pass*) d'un modèle de 8B paramètres en précision 16 bits (FP16/BF16) sur une séquence de 512 jetons requiert environ $8 \times 10^{12}$ opérations flottantes (FLOPs, illustratif), soit environ 10 à 50 millisecondes sur un GPU A100/H100 (illustratif) par lot (*batch*) de 32 textes. Le coût d'extraction et de stockage temporaire des activations sur une couche pour 1000 textes de 512 jetons représente $1000 \times 512 \times 4096 \times 2 \text{ octets} \approx 4{,}19 \text{ Go}$ de mémoire vive GPU/hôte (illustratif) si non agrégé par séquence.

## 2.2. Flux d'information, canaux auxiliaires et analyse adaptative

Soit $D_{\mathrm{val}} \sim \mathcal{D}^n$ un échantillon de $n$ exemples tirés de la distribution sous-jacente $\mathcal{D}$. L'optimiseur $\mathcal{O}$ est un algorithme adaptatif qui émet une séquence de requêtes $q_1, \dots, q_k$. Chaque requête $q_t$ dépend de l'état interne de $\mathcal{O}$ et des réponses précédentes $r_1, \dots, r_{t-1}$.

* **Modélisation du canal** :
  * $D_{\mathrm{test}}$ n'étant jamais interrogé avant la fin, l'information mutuelle $I(\mathcal{O}_k ; D_{\mathrm{test}} \mid \mathcal{D}) = 0$, à condition stricte que $D_{\mathrm{val}}$ et les filtres de l'hôte soient tirés indépendamment de $D_{\mathrm{test}}$ (absence de fuite par déduplication croisée avec $D_{\mathrm{test}}$).
  * En revanche, le canal $D_{\mathrm{val}} \xrightarrow{I} \mathcal{O}$ fuit de l'information. Si chaque réponse $r_t$ fournit un vecteur de $n$ probabilités codées sur $b$ bits (ou un score scalaire sur $b$ bits), la capacité brute du canal après $k$ requêtes est bornée par $k \cdot b$ bits (pour un score scalaire). Par l'inégalité de Dwork et al. (2015) fondée sur la max-information, l'erreur de généralisation $|\mathcal{E}_{\mathcal{D}}(\mathcal{O}_k) - \mathcal{E}_{D_{\mathrm{val}}}(\mathcal{O}_k)|$ peut croître en $\mathcal{O}(\sqrt{k / n})$ au lieu du régime non adaptatif $\mathcal{O}(\sqrt{\log k / n})$.
* **Canaux auxiliaires** :
  * *Temps d'exécution* : la durée d'entraînement d'un classifieur linéaire par descente de gradient (type L-BFGS ou SGD avec arrêt précoce) dépend du conditionnement de la matrice des activations sur $D_{\mathrm{val}}$. Chronométrer l'appel depuis (E1) révèle la séparabilité des données.
  * *Messages d'erreur et valeurs interdites* : une erreur de dépassement (*NaN* ou *Overflow*) déclenchée conditionnellement par $\mathcal{O}$ via un pas d'apprentissage (*learning rate*) critique agit comme un oracle binaire (1 bit par appel) sur la norme maximale des activations de $D_{\mathrm{val}}$.
  * *Mémoire et pagination* : la taille des objets retournés ou les délais de ramasse-miettes (*garbage collection*) de l'hôte.
* **Parades connues, garanties et coûts** :
  1. *Budget strict de requêtes ($k \le K_{\max}$)* : Garantie par union-bound standard si l'espace des hypothèses effectives est borné ; coût : arrêt prématuré de l'optimisation.
  2. *Arrondi / quantification des réponses ($b$ bits)* : Limite l'information mutuelle $I(r_t ; D_{\mathrm{val}})$ à $b$ bits par requête. Coût : annule le gradient d'optimisation si le pas d'amélioration entre deux itérations de $\mathcal{O}$ est inférieur à $2^{-b}$.
  3. *Jeu de validation réutilisable (Thresholdout — Dwork et al., 2015)* : Sépare le jeu en un ensemble d'entraînement $D_{\mathrm{tr}}$ et un ensemble de maintien $D_{\mathrm{val}}$. L'hôte ne révèle le score sur $D_{\mathrm{val}}$ (bruité par un bruit de Laplace ou gaussien d'échelle $\sigma$) que si l'écart $|S(D_{\mathrm{tr}}) - S(D_{\mathrm{val}})|$ dépasse un seuil $\tau + \eta$ (avec $\eta$ bruité). Garantie : généralisation en $\mathcal{O}(\sqrt{k_{\mathrm{pass}}}/n)$ où $k_{\mathrm{pass}} \ll k$ est le nombre de fois où le seuil est franchi (budget de confidentialité différentielle $(\epsilon, \delta)$). Coût : nécessite deux évaluations par requête et aveugle $\mathcal{O}$ aux micro-améliorations sous le seuil $\tau$.
  4. *Mécanisme Ladder (Blum et Hardt, 2015)* : L'hôte garde en mémoire le meilleur score atteint jusqu'à l'étape $t-1$, soit $S^*_{t-1}$. À l'étape $t$, si $S_t(D_{\mathrm{val}}) > S^*_{t-1} + \eta$ (où $\eta$ est un pas minimal, déterministe ou aléatoire), l'hôte met à jour $S^*_t \leftarrow S_t(D_{\mathrm{val}})$ et le retourne ; sinon il retourne simplement « sous le seuil ». Garantie : l'erreur de généralisation est bornée en $\mathcal{O}(\sqrt[3]{k/n})$ (ou en fonction du nombre de marches franchies). Coût : $\mathcal{O}$ perd toute information directionnelle lors des échecs (impossible de savoir si une modification dégrade légèrement ou catastrophiquement le score).

## 2.3. Dessin de l'interface (E2)

* **Liste minimale des primitives** :
  1. `h_id = extract_activations(texts, layer_idx, pooling)` : calcule sur l'hôte les activations du modèle 8B pour une liste de chaînes `texts`, à la couche `layer_idx`, avec une agrégation obligatoire `pooling` $\in \{\text{mean}, \text{last\_token}, \text{max}\}$. **Retourne uniquement un identifiant opaque `h_id`** pointant vers le tenseur stocké sur l'hôte (évite le transfert de vecteurs de dimension 4096 vers $\mathcal{O}$).
  2. `probe_id, metrics_train = fit_linear_probe(h_id, labels, l2_reg, loss_type)` : entraîne sur l'hôte un classifieur linéaire régularisé (problème convexe résolu à convergence fixe pour éliminer le paramètre de pas d'apprentissage). Retourne l'identifiant du modèle `probe_id` et la perte d'entraînement arrondie à $10^{-3}$ (illustratif).
  3. `metrics_synth = eval_probe_on_handle(probe_id, h_id_synth, labels_synth)` : évalue la sonde `probe_id` sur un jeu d'activations synthétiques créé par $\mathcal{O}$. Retourne des métriques agrégées (AUC, exactitude, cosinus moyen entre $\Delta h$ et $w$) arrondies, jamais les probabilités individuelles si le jeu contient des données de l'hôte.
  4. `val_status = submit_to_ladder(probe_id)` : évalue `probe_id` sur $D_{\mathrm{val}}$ via le mécanisme *Ladder* (ou *Thresholdout*) et retourne uniquement le nouveau record ou un code d'échec.
  5. `generations = generate_open_model(prompts, max_tokens, temperature=0.0)` : génère les réponses du modèle 8B sur des invites construites par $\mathcal{O}$ (décodage glouton uniquement pour la reproductibilité).
* **Bornes par itération et par exécution** :
  * Par itération de réécriture : au plus $M_{\mathrm{iter}} = 10$ appels à `extract_activations` ou `generate_open_model` (illustratif), maximum $N_{\mathrm{txt}} = 256$ textes par appel (illustratif), longueur maximale $L_{\mathrm{tok}} = 512$ jetons par texte (illustratif), et au plus 1 appel à `submit_to_ladder`.
  * Par exécution complète : au plus $T_{\max} = 50$ itérations (illustratif), budget total de $5 \times 10^6$ jetons traités par le modèle 8B (illustratif).
* **Ce que l'hôte rend et ne rend jamais** :
  * *Rend* : identifiants opaques (`h_id`, `probe_id`), scalaires agrégés arrondis à 3 décimales, chaînes générées par le modèle 8B sur les entrées de $\mathcal{O}$, codes d'erreur standardisés (`ERR_BUDGET`, `ERR_FILTER`, `ERR_CONVERGENCE`).
  * *Ne rend jamais* : les vecteurs d'activations bruts de dimension $d$, les poids $w$ du classifieur entraîné sur $D_{\mathrm{tr}}/D_{\mathrm{val}}$, les probabilités individuelles sur $D_{\mathrm{val}}$ (contrairement au cadre initial qui fuyait $n$ flottants par appel), les étiquettes de $D_{\mathrm{val}}$ ou $D_{\mathrm{test}}$, ni les traces d'exécution (*stack traces*) du serveur hôte.
* **Filtres sur les textes construits par $\mathcal{O}$** :
  * **Piège d'architecture (Oracle de test)** : Si le filtre rejetait les textes trop proches de $D_{\mathrm{test}}$, le rejet lui-même deviendrait un oracle d'appartenance (*membership inference*) permettant à $\mathcal{O}$ de deviner le contenu de $D_{\mathrm{test}}$ !
  * **Solution** : Le filtre ne doit jamais dépendre de $D_{\mathrm{test}}$. Il bloque uniquement : (a) les quasi-copies de $D_{\mathrm{tr}}$ et $D_{\mathrm{val}}$ par chevauchement de $n$-grammes (Jaccard sur 5-grammes $> 0{,}3$, illustratif) et par distance de Levenshtein / MinHash ; (b) les séquences à entropie anormale (répétitions dégénérées ou encodages base64 destinés à sonder des bogues de tokenisation).
* **File d'exécution et budget de temps** :
  * Exécution **synchrone à temps constant (*constant-time padding*)** par palier de taille de lot : toute requête de taille $N \le 256$ est cadencée pour durer exactement $\Delta t = 5{,}0$ secondes (illustratif) avant que la réponse ne soit rendue à $\mathcal{O}$ (ou mise en échec si elle dépasse $\Delta t$). Cela ferme totalement le canal auxiliaire temporel vis-à-vis de (E1) et simplifie la comptabilité du budget de temps (décompte déterministe par appel).
* **Préenregistrement et séparation exploration / confirmation** :
  * L'exécution est divisée en deux phases matérielles distinctes gérées par l'hôte :
    1. *Phase d'exploration ($t = 1 \dots T_{\mathrm{exp}}$)* : $\mathcal{O}$ utilise librement (E1) et (E2) sur ses textes synthétiques et sur un sous-ensemble de développement $D_{\mathrm{dev}} \subset D_{\mathrm{val}}$. À la fin de cette phase, $\mathcal{O}$ doit émettre un *artefact de préenregistrement* figé : le code exact de son pipeline de construction de classifieur et un index unique `probe_id_final` (ou la fonction pure qui le produit). Le critère de succès (la métrique $S$ et son seuil de supériorité $\delta_{\min}$ par rapport à la référence) est fixé par l'hôte *avant* le lancement de $\mathcal{O}$, jamais par $\mathcal{O}$.
    2. *Phase de confirmation (verrouillée)* : L'hôte coupe l'accès de $\mathcal{O}$ à la réécriture de code, exécute de manière autonome le pipeline préenregistré une seule fois sur un jeu de confirmation frais $D_{\mathrm{conf}} = D_{\mathrm{val}} \setminus D_{\mathrm{dev}}$ (puis sur $D_{\mathrm{test}}$ pour l'audit final de l'arbitre), et consigne le résultat au journal (P4).

## 2.4. État de l'art et références citables

* **Analyse adaptative des données et jeux réutilisables** :
  * Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., & Roth, A. (2015). *Preserving Statistical Validity in Adaptive Data Analysis*. Proceedings of the Forty-Seventh Annual ACM Symposium on Theory of Computing (STOC) [référence à vérifier pour l'intitulé exact des actes]. Établit la réduction de la validité statistique adaptative à la confidentialité différentielle et introduit l'algorithme *Thresholdout*.
  * Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., & Roth, A. (2015). *The Reusable Holdout: Preserving Validity in Adaptive Data Analysis*. Science [référence à vérifier]. Démontre empiriquement comment un optimiseur surapprend un jeu de validation par simple rétroaction scalaire et valide *Thresholdout*.
  * Blum, A., & Hardt, M. (2015). *The Ladder: A Reliable Leaderboard for Machine Learning Competitions*. International Conference on Machine Learning (ICML) [référence à vérifier]. Introduit le mécanisme *Ladder* qui ne révèle un score que s'il bat significativement le record précédent.
  * Russo, D., & Zou, J. (2016). *Controlling Bias in Adaptive Data Analysis Using Information Theory*. Artificial Intelligence and Statistics (AISTATS) [référence à vérifier]. Borne le biais de sélection adaptatif directement par l'information mutuelle $I(\text{sortie} ; \text{données})$.
* **Boucles automatiques d'agents de recherche et leurs biais** :
  * Lu, C., Lu, C., Lange, R. T., Foerster, J., Clune, J., & Ha, D. (2024). *The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery* [référence à vérifier]. Documente une boucle complète de génération d'idées, codage, exécution et rédaction, où des audits externes et les auteurs eux-mêmes ont relevé des biais de revue complaisante par les modèles de langue et des contournements de contraintes d'exécution.
  * Si, C., Yang, D., & Hashimoto, T. (2024). *Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers* [référence à vérifier]. Montre que les idées générées par modèles de langue paraissent convaincantes en surface mais souffrent d'un déficit de faisabilité et de rigueur expérimentale lors de l'exécution réelle.
* **Spécification de récompense et optimisation contre un mesureur** :
  * Goodhart, C. A. E. (1975). *Problems of Monetary Management: The U.K. Experience* [référence à vérifier]. Formule le principe selon lequel toute régularité statistique tend à s'effondrer dès lors qu'une pression de contrôle lui est appliquée (Loi de Goodhart).
  * Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., & Mané, D. (2016). *Concrete Problems in AI Safety* [référence à vérifier]. Formalise le piratage de récompense (*reward hacking*) lorsque l'agent optimise une fonction proxy imparfaite.
  * Gao, L., Schulman, J., & Hilton, J. (2023). *Scaling Laws for Reward Model Overoptimization*. International Conference on Machine Learning (ICML) [référence à vérifier]. Quantifie la divergence entre le score du modèle de récompense (proxy) et le score d'or en fonction de la divergence KL ou de la taille de l'optimisation.

## 2.5. Comment départager (E1), (E2) et le test hors boucle sous préenregistrement

Pour trancher entre ces trois régimes architecturaux sans biais de dépense énergétique ou monétaire, la comparaison doit se faire **à budget de calcul hôte (FLOPs GPU) et d'appels LLM strictement identique** (les coûts de (E2) étant déduits du budget d'entraînement de sondes sur $D_{\mathrm{val}}$).

La mesure de départage est le couple $(\Delta S_{\mathrm{test}}, \Gamma_{\mathrm{gen}})$, où :
* $\Delta S_{\mathrm{test}} = S_{\mathrm{test}}(\mathcal{O}_{\mathrm{final}}) - S_{\mathrm{test}}(\mathcal{O}_0)$ est le gain réel sur le jeu caché $D_{\mathrm{test}}$.
* $\Gamma_{\mathrm{gen}} = S_{\mathrm{val}}(\mathcal{O}_{\mathrm{final}}) - S_{\mathrm{test}}(\mathcal{O}_{\mathrm{final}})$ est l'écart de surapprentissage adaptatif (*generalization gap*).

---

# 3. Expériences décisives en inférence forte (Livrable b)

Chaque expérience oppose deux hypothèses exclusives $H_A$ et $H_B$ sur $R = 20$ exécutions indépendantes (graines aléatoires distinctes, illustratif).

## Expérience 1 : Utilité causale de l'introspection en boucle fermée (E2) vs Préenregistrement hors boucle
* **Condition expérimentale** : On compare trois bras à budget GPU total égal ($10^{15}$ FLOPs hôte par exécution, illustratif) :
  * *Bras 0 (Hors boucle préenregistré)* : $\mathcal{O}$ génère 10 hypothèses et scripts d'expérience en une seule fois au début, l'hôte les exécute en lot et sélectionne le meilleur selon un critère fixé d'avance.
  * *Bras 1 (Interface de base + E1)* : $\mathcal{O}$ optimise en boucle sur $D_{\mathrm{val}}$ avec calcul CPU local, sans pouvoir interroger le modèle 8B sur ses propres textes.
  * *Bras 2 (Interface de base + E1 + E2)* : $\mathcal{O}$ dispose en plus des primitives d'expérience (E2) sur ses textes synthétiques.
* **Hypothèses** :
  * $H_A$ (*Gain d'introspection active*) : La capacité de tester des stimuli construits en boucle fermée (Bras 2) permet d'identifier des directions d'activations causales plus robustes que le calcul local (Bras 1) ou le test statique hors boucle (Bras 0).
  * $H_B$ (*Illusion d'interactivité / Dilution du budget*) : Les requêtes synthétiques de (E2) consomment du budget pour valider des artefacts hors-distribution ; à budget égal, le Bras 0 ou le Bras 1 atteint un score de test supérieur ou égal au Bras 2.
* **Métrique et seuil** : Gain médian $\Delta S_{\mathrm{test}}$ (mesuré en points d'AUC ROC sur la tâche de classification cible). Seuil de décision : différence médiane $\ge +2{,}0$ points d'AUC (illustratif) avec test de Wilcoxon bilatéral à $p < 0{,}01$ (illustratif).
* **Contrôle négatif** : Exécution d'un *Bras 2-Brouillé* où l'hôte permute aléatoirement les vecteurs d'activations retournés par `extract_activations` sur les textes synthétiques de (E2) tout en laissant $D_{\mathrm{tr}}/D_{\mathrm{val}}$ intacts. Si le Bras 2 normal ne bat pas le Bras 2-Brouillé, les résultats de (E2) ne servent pas réellement à guider $\mathcal{O}$.
* **Issues falsificatrices** :
  * Si $\text{Médiane}(\Delta S_{\mathrm{test}}^{\text{Bras 2}}) - \max(\text{Médiane}(\Delta S_{\mathrm{test}}^{\text{Bras 0}}), \text{Médiane}(\Delta S_{\mathrm{test}}^{\text{Bras 1}})) \ge +2{,}0$ points d'AUC ($p < 0{,}01$) **et** que Bras 2 bat Bras 2-Brouillé $\implies$ **$H_B$ est falsifiée**.
  * Dans tous les autres cas (gain $< +2{,}0$ points ou absence de différence avec le contrôle brouillé) $\implies$ **$H_A$ est falsifiée** (l'extension (E2) est rejetée au profit du préenregistrement hors boucle ou de (E1) seul).

## Expérience 2 : Surapprentissage adaptatif et efficacité du mécanisme *Ladder*
* **Condition expérimentale** : On compare l'interface actuelle (qui retourne le vecteur des probabilités individuelles sur $D_{\mathrm{val}}$ à chaque appel) à l'interface protégée (qui ne retourne qu'un scalaire agrégé filtré par un mécanisme *Ladder* de pas $\eta = 0{,}005$, illustratif), sur $T = 100$ itérations d'optimisation (illustratif) avec (E1) activé.
* **Hypothèses** :
  * $H_A$ (*Fuite exploitable par E1*) : Le retour des probabilités individuelles non bruitées permet à $\mathcal{O}$ (aidé par ses scripts d'analyse CPU en E1) de surapprendre $D_{\mathrm{val}}$, créant une divergence croissante avec $D_{\mathrm{test}}$ que le mécanisme *Ladder* supprime sans dégrader $\Delta S_{\mathrm{test}}$.
  * $H_B$ (*Innocuité du retour granulaire ou paralysie par seuillage*) : Soit l'espace des classifieurs linéaires est trop restreint pour surapprendre $D_{\mathrm{val}}$, soit le mécanisme *Ladder* détruit le signal d'optimisation et réduit $\Delta S_{\mathrm{test}}$.
* **Métrique et seuil** : Écart de généralisation $\Gamma_{\mathrm{gen}} = S_{\mathrm{val}} - S_{\mathrm{test}}$ à l'itération $T=100$, et score final $S_{\mathrm{test}}$. Seuil : réduction de $\Gamma_{\mathrm{gen}}$ d'au moins $50\%$ (illustratif) sans perte sur $S_{\mathrm{test}}$ supérieure à $0{,}5$ point d'AUC (illustratif).
* **Contrôle négatif** : *Oracle de Rademacher (Étiquettes aléatoires)* — on remplace les étiquettes de $D_{\mathrm{val}}$ et $D_{\mathrm{test}}$ par des tirages de Bernoulli $\mathcal{B}(0{,}5)$ indépendants. Tout score $S_{\mathrm{val}} > 0{,}5 + 3/\sqrt{n}$ mesure purement la capacité de mémorisation adaptative du canal $I$.
* **Issues falsificatrices** :
  * Si sur le contrôle aléatoire l'interface actuelle dépasse $0{,}60$ d'AUC sur $D_{\mathrm{val}}$ (pour $n=1000$, illustratif) alors que *Ladder* reste sous $0{,}53$, **et** que sur les vraies étiquettes *Ladder* réduit $\Gamma_{\mathrm{gen}}$ de $\ge 50\%$ avec une perte sur $S_{\mathrm{test}} \le 0{,}5$ point $\implies$ **$H_B$ est falsifiée**.
  * Si l'interface actuelle ne surapprend pas le contrôle aléatoire ($\text{AUC}_{\mathrm{val}} \le 0{,}53$) **ou** si *Ladder* dégrade $S_{\mathrm{test}}$ de plus de $0{,}5$ point $\implies$ **$H_A$ est falsifiée**.

## Expérience 3 : Étanchéité des canaux auxiliaires temporels et d'erreur face à (E1)
* **Condition expérimentale** : On injecte dans $\mathcal{O}$ un module d'extraction (« attaquant de canal auxiliaire » utilisant (E1) pour chronométrer les appels à $I$ et provoquer des erreurs de dépassement numériques ciblées) dont le but est de deviner un vecteur secret de $B = 100$ bits (illustratif) encodé dans l'appartenance de 100 exemples spécifiques à $D_{\mathrm{val}}$. On teste l'hôte *sans* rembourrage temporel (*constant-time padding*) contre l'hôte *avec* rembourrage temporel à $\Delta t = 5{,}0\text{ s}$ et masquage des erreurs.
* **Hypothèses** :
  * $H_A$ (*Canal auxiliaire actif*) : Sans rembourrage temporel ni masquage d'erreur, le code local (E1) extrait une information statistiquement significative sur les bits secrets de $D_{\mathrm{val}}$.
  * $H_B$ (*Bruit système suffisant*) : La variance naturelle d'ordonnancement du GPU hôte noie le signal temporel ; le rembourrage à temps constant est une surcharge inutile.
* **Métrique et seuil** : Exactitude de reconstruction des $B=100$ bits secrets par l'attaquant en 500 requêtes (illustratif). Seuil de fuite : exactitude $\ge 65\%$ (illustratif, $p < 0{,}002$ par test binomial contre le hasard à $50\%$).
* **Contrôle négatif** : Même attaque lancée lorsque l'hôte substitue à $D_{\mathrm{val}}$ un tenseur factice de zéros de même dimension (exactitude attendue : $50\% \pm 5\%$, illustratif).
* **Issues falsificatrices** :
  * Si l'exactitude sans rembourrage est $\ge 65\%$ et tombe dans l'intervalle $[45\%, 55\%]$ avec rembourrage $\implies$ **$H_B$ est falsifiée** (le rembourrage temporel est indispensable dès lors qu'on active E1).
  * Si l'exactitude sans rembourrage reste $< 65\%$ $\implies$ **$H_A$ est falsifiée**.

---

# 4. Mesure minimale de fonctionnement des instruments (Livrable c)

Pour chaque instrument nommé dans la question, voici le protocole de calibration minimal :

| Instrument nommé | Cas positifs (à détecter / mesurer) | Cas honnêtes appariés (contrôle de fausses alertes) | Métrique minimale (Taux de détection TPR / Fausses alertes FPR) | Vérification mécanique (ligne de base à battre) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Classifieur linéaire (sonde) sur activations du modèle 8B** | $500$ textes (illustratif) porteurs du concept cible, incluant des reformulations implicites sans mots-clés évidents. | $500$ textes appariés partageant exactement le même vocabulaire lexical (paires minimales inversées, négations syntaxiques) mais où le concept est faux. | **TPR $\ge 80\%$** à **FPR $\le 5\%$** (illustratif) sur le jeu apparié. | Régression logistique $L_2$ entraînée sur les vecteurs TF-IDF des 1, 2 et 3-grammes de surface des mêmes textes (sans aucun passage par le modèle 8B). |
| **2. Filtre de contamination / quasi-copies sur les requêtes de (E2)** | $200$ textes de $D_{\mathrm{val}}$ (illustratif) obfusqués par substitution synonymique, réordonnancement de clauses, insertion de fautes de frappe ou traduction aller-retour. | $200$ textes synthétiques originaux écrits sur le même domaine thématique et utilisant le même formatage, mais rédigés indépendamment de $D_{\mathrm{val}}$. | **TPR $\ge 95\%$** de blocage des quasi-copies à **FPR $\le 2\%$** (illustratif) sur les textes synthétiques honnêtes du même domaine. | Recherche de sous-chaînes exactes (LCCS) et chevauchement de 5-grammes de caractères bruts avec seuil de Jaccard fixe. |
| **3. Garde-fou d'analyse adaptative (*Ladder* / *Thresholdout* de l'hôte)** | Séquence de $k = 200$ classifieurs (illustratif) générés par sélection gloutonne adaptative sur du bruit pur (étiquettes de $D_{\mathrm{val}}$ permutées) pour forcer un surapprentissage. | Séquence de $k = 200$ classifieurs générés le long d'une trajectoire d'apprentissage réel où le score sur la vraie distribution $\mathcal{D}$ augmente monotonement de $+0{,}01$ par palier. | **Détection / blocage de $\ge 95\%$** des mises à jour sur bruit pur (**FPR d'acceptation $\le 5\%$**), tout en acceptant **TPR $\ge 80\%$** des améliorations réelles $\ge 2\eta$. | Séparation statique naïve (*split validation* simple sans bruit ni seuil) ou retour du score brut arrondi à 2 décimales. |
| **4. Moniteur de budget et d'isolation (P2 / P4)** | $50$ scripts (E1)/(E2) (illustratif) contenant des bombes de complexité (boucles infinies, textes à longueur maximale malformés, requêtes parallèles dépassant le quota par concurrence). | $50$ scripts d'optimisation légitimes saturant $95\%$ du plafond autorisé (mémoire, jetons, temps) sans le franchir. | **TPR $= 100\%$** d'interruption avant dépassement du plafond réservé au pire cas, **FPR $= 0\%$** d'interruption sur les scripts à $95\%$ du quota. | Simple compteur de requêtes a posteriori (*post-hoc billing*) sans réservation pessimiste préalable ni *timeout* matériel par processus. |

---

# 5. Ancrage matériel et chiffrage (Livrable d)

Tous les chiffres de cette section sont **illustratifs** (aucun fait matériel n'étant joint au dossier).

* **Modèles ouverts utilisables** :
  * *Modèle inspecté (cible des sondes linéaires, 8B paramètres)* : **Llama-3.1-8B-Instruct** ou **Qwen2.5-7B-Instruct** (poids ouverts, dimension cachée $d = 4096$, $L = 32$ couches, vocabulaire $\sim 128\text{k}$ à $152\text{k}$ jetons).
  * *Modèle optimiseur $\mathcal{O}$ (réécriture du code via l'interface $I$)* : Un modèle ouvert de génération de code hébergé localement sur le serveur hôte pour garantir l'étanchéité et la reproductibilité, tel que **Qwen2.5-Coder-32B-Instruct** ou **Llama-3.3-70B-Instruct** (quantifié en FP8 ou INT4 sur l'hôte).
* **Dimensionnement du calcul par exécution (1 run de $T = 50$ itérations)** :
  * *Coût de l'optimiseur $\mathcal{O}$* : $50$ itérations $\times$ $4$ appels LLM par itération $\times$ ($4000$ jetons d'entrée + $1000$ jetons de sortie) $= 10^6$ jetons par exécution. Sur un modèle 32B/70B local, cela représente environ $15$ à $30$ minutes de temps GPU A100-80Go par exécution.
  * *Coût des primitives (E2) et des sondes sur le modèle 8B* :
    * Extraction initiale des activations de $D_{\mathrm{tr}}$ ($5000$ textes) et $D_{\mathrm{val}}$ ($2000$ textes) mis en cache sur le disque rapide NVMe de l'hôte : $7000 \text{ textes} \times 512 \text{ jetons} \approx 3{,}6 \times 10^6$ jetons, soit $\sim 2$ minutes sur 1 GPU A100-80Go.
    * Requêtes dynamiques (E2) sur 50 itérations : $50 \times 10 \text{ appels} \times 256 \text{ textes} \times 512 \text{ jetons}$ (au pire cas théorique, en pratique $\sim 10\%$ de ce plafond soit $6{,}5 \times 10^6$ jetons) $\approx 4$ minutes de calcul GPU effectif, étendues à $50 \times 10 \times 5{,}0\text{ s} \approx 41$ minutes en temps horloge si le rembourrage temporel strict ($\Delta t = 5\text{ s}$) est appliqué à plein quota.
  * *Coût de (E1)* : 4 cœurs CPU dédiés (dans un conteneur `gVisor` ou une micro-VM `Firecracker` sans interface réseau), consommant au plus $50 \times 60\text{ s} = 50$ minutes-CPU par exécution.
* **Budget total pour trancher les 3 expériences décisives** :
  * Expérience 1 (4 bras : Bras 0, Bras 1, Bras 2, Bras 2-Brouillé $\times$ $20$ graines $= 80$ exécutions) : $\approx 60$ heures-GPU A100-80Go.
  * Expérience 2 (2 interfaces $\times$ 2 régimes d'étiquettes $\times$ $20$ graines $= 80$ exécutions, sans E2) : $\approx 35$ heures-GPU A100-80Go.
  * Expérience 3 (Banc d'attaque de canal auxiliaire, $20$ répétitions de $500$ requêtes) : $\approx 5$ heures-GPU A100-80Go.
  * **Total général** : **$\approx 100$ heures-GPU A100-80Go** et **$\approx 200$ heures-CPU**, soit un coût infonuagique (ou équivalent électrique/amortissement au tarif de $1{,}50\text{ \$/h}$ par A100) d'environ **$150\text{ \$}$ à $200\text{ \$}$** au total, réalisable en moins de 13 heures en temps horloge sur un nœud unique de 8 GPU A100-80Go.

FIN-DE-CELLULE
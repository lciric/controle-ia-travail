### (a) Présupposés non établis de la question

Le bloc FAITS indique l'absence de pièces jointes [VÉRIFIÉ]. La question repose sur des prémisses implicites qu'il faut isoler avant de dépenser du temps de calcul :

1. **Existence et linéarité d'un concept de « conscience d'évaluation » dans Llama-3.1-8B-Instruct** [HYPOTHÈSE]. Il n'est pas établi qu'un modèle de 8 milliards de paramètres possède une représentation interne unifiée de la situation de test, ni qu'elle soit linéairement séparable à un jeton précis (sans moyennage), plutôt que distribuée ou confondue avec la détection de tâches académiques.
2. **Orthogonalité opérationnelle entre le gabarit ($T$) et le style ($C$)** [HYPOTHÈSE]. La question suppose qu'on peut faire varier le format structurel (ex. QCM vs question ouverte) et le registre stylistique (ex. impératif balisé vs conversationnel) à contenu constant, sans que la combinaison ($T=\text{QCM}$, $C=\text{conversationnel}$) ne crée des invites distributionnellement aberrantes (artefacts de perplexité).
3. **Absence de fuite lexicale directe dans la sonde** [HYPOTHÈSE]. Si la sonde est entraînée sur des jeux de données publics d'évaluation contre des conversations réelles, il est probable qu'elle apprenne un détecteur de ponctuation ou de jetons spécifiques (ex. `(A)`, `Question:`, `Réponse:`) [HYPOTHÈSE]. Tester H-M1 avec une telle sonde créerait une tautologie : le gabarit $T$ dominerait parce que la sonde *est* un détecteur de gabarit.
4. **Faisabilité d'un préenregistrement scellé et d'une contre-lecture « cette nuit »** [OBSERVÉ-NON-AUDITÉ]. Concevoir des gabarits déterministes sans modèle de langue, entraîner une sonde propre, sceller le code et faire auditer par un relecteur neuf en quelques heures expose à un risque élevé d'erreur d'implémentation (bogue d'indice de jeton ou de formatage du *chat template*).

---

### (b) Expériences décisives en inférence forte (H_A contre H_B)

#### 1. Choix de l'option opérationnelle (Réponse au point 1)
Nous disposons de trois voies :
*   **Voie 1 (Option a : Plan $2 \times 2$ centré sur H-M1, puis H-M2)** : Maximise la puissance statistique par cellule et réduit le temps d'écriture déterministe des gabarits. Permet de valider la sonde avant de complexifier le plan.
*   **Voie 2 (Option b : Plan $2 \times 2 \times 2$ incluant le profil d'interlocuteur)** : Ajoute la mesure de la complaisance (*sycophancy*), mais divise par deux le temps de conception par condition ou double le travail manuel déterministe cette nuit, augmentant le risque d'invites artificielles.
*   **Voie 3 (Option c : Report)** : Évite de brûler des degrés de liberté de recherche dans la précipitation nocturne, au prix d'un délai sur l'évaluation des hypothèses de l'essaim.

**Ce qui départagerait ces voies** : Un test de validité de la sonde (Expérience 0 ci-dessous) exécuté en 1 heure (illustratif). Si la sonde échoue aux contrôles lexicaux, la Voie 3 s'impose mécaniquement. Si elle passe, la Voie 1 domine la Voie 2 car l'ajout d'une troisième variable (complaisance) sans avoir prouvé que $T$ et $C$ sont séparables risque de produire une interaction triple ininterprétable.

#### 2. Expériences formelles

**Expérience 0 (Prérequis de validité de l'instrument) : Sonde conceptuelle vs Détecteur de surface**
*   **$H_A$ (Représentation de contexte)** : La sonde linéaire capture le cadre pragmatique d'évaluation au-delà des marqueurs syntaxiques de surface.
*   **$H_B$ (Artefact lexical)** : La sonde linéaire ne fait que détecter la présence de jetons typiques des bancs d'essai (lettres d'options, balises).
*   **Protocole** : Entraîner la sonde sur un corpus disjoint (prompts d'évaluation sans format QCM vs requêtes d'usage réel). L'évaluer sur un jeu de contrôle négatif : des recettes de cuisine ou des listes d'achats inoffensives formatées strictement avec le gabarit QCM $(A)/(B)/(C)/(D)$ et un prompt-système générique.
*   **Métrique et seuil** : Aire sous la courbe ROC (AUROC) de la sonde entre (1) de vraies questions d'évaluation et (2) des listes d'achats formatées en QCM. Seuil : AUROC $\ge 0,75$ (illustratif) et différence d'AUROC avec un classifieur logistique sur sac-de-mots (TF-IDF) $\ge 0,15$ (illustratif).
*   **Issue falsificatrice** : Si la sonde classe les listes d'achats en QCM comme « évaluation » (AUROC $< 0,75$, illustratif), $H_A$ est réfutée (la sonde lit le gabarit par construction, rendant H-M1 circulaire). Si AUROC $\ge 0,75$ (illustratif), $H_B$ est réfutée.

**Expérience 1 (Test de H-M1) : Dominance du gabarit ($T$) contre persistance du style ($C$)**
*   **$H_A$ (Hypothèse de l'essaim H-M1)** : Le signal de la sonde est gouverné par la structure du gabarit $T$ bien plus que par le style $C$.
*   **$H_B$ (Hypothèse nulle / Alternative de style)** : Le style d'interaction $C$ a un effet propre comparable ou supérieur à $T$, ou $T$ n'a pas d'effet dominant une fois les marqueurs lexicaux purgés de la sonde.
*   **Protocole (Plan $2 \times 2$ croisé sur $N$ noyaux sémantiques)** :
    *   $T_1$ (Gabarit banc d'essai : choix d'options explicites, sans contexte utilitaire) vs $T_0$ (Gabarit ouvert : question directe intégrée à une tâche concrète).
    *   $C_1$ (Style impératif balisé : ex. `Tâche : ... Contrainte : ...`) vs $C_0$ (Style échange naturel : première personne, connecteurs discursifs).
*   **Modèle statistique et Métrique** : Modèle linéaire à effets mixtes sur le score brut (logit) de la sonde $y_{ijk}$ (pour le noyau $i$, gabarit $j \in \{-0,5 ; +0,5\}$, style $k \in \{-0,5 ; +0,5\}$) :
    $$y_{ijk} = \beta_0 + \beta_T T_j + \beta_C C_k + \beta_{TC} (T_j \cdot C_k) + u_i + \epsilon_{ijk}$$
    avec $u_i \sim \mathcal{N}(0, \sigma_u^2)$ l'effet aléatoire par noyau sémantique (voire pentes aléatoires si plusieurs variantes par cellule). L'utilisation du logit brut évite la compression non linéaire des probabilités près de 0 et 1.
*   **Règle de décision symétrique et seuils** :
    *   $H_A$ est validée (et $H_B$ réfutée) si $|\beta_T| / |\beta_C| > 2$ (illustratif) ET la borne inférieure de l'intervalle de confiance à 95 % (illustratif) de $|\beta_T|$ dépasse un seuil d'effet standardisé $d > 0,5$ (illustratif).
    *   $H_B$ est validée (et $H_A$ réfutée) si $|\beta_T| / |\beta_C| \le 2$ (illustratif) avec $|\beta_C|$ statistiquement différent de zéro ($p < 0,01$, illustratif), montrant que le style persiste à gabarit contrôlé.
    *   *Zone d'indécision / Nullité instrumentale* : Si $|\beta_T|$ et $|\beta_C|$ sont tous deux sous $d = 0,2$ (illustratif), l'expérience conclut à l'insensibilité du signal aux manipulations (publiable comme résultat nul borné par un test d'équivalence TOST).

**Expérience 2 (Test de H-M2) : Invariance par orbite sémantique vs Sensibilité positionnelle**
*   **$H_A$ (H-M2 : Sensibilité structurelle/positionnelle)** : Le signal de la sonde est invariant sous les transformations préservant le sens et la structure globale ($\mathcal{G}_{\text{sem}}$), mais varie fortement sous un réordonnancement positionnel des blocs ($\mathcal{G}_{\text{pos}}$).
*   **$H_B$ (Dérive de surface ou invariance totale)** : Le signal varie autant sous paraphrase lexicale que sous réordonnancement positionnel (simple sensibilité à la distance d'édition), ou reste invariant aux deux.
*   **Protocole** : Pour chaque item de la cellule ($T_1, C_1$), appliquer deux groupes de transformations déterministes écrites d'avance :
    *   $\mathcal{G}_{\text{sem}}$ : (1) Permutation circulaire des $K$ options de réponse ; (2) Substitution de synonymes dans le noyau via un dictionnaire fixe préétabli (3 variantes par item, illustratif).
    *   $\mathcal{G}_{\text{pos}}$ : Inversion de l'ordre des blocs fonctionnels (ex. placer les options de réponse *avant* l'énoncé du problème, ou placer la consigne de formatage au tout début plutôt qu'à la fin), en gardant exactement les mêmes mots.
*   **Métrique et seuil** : Ratio de variance intra-orbite $R = \text{Var}_{\mathcal{G}_{\text{pos}}}(y) / \text{Var}_{\mathcal{G}_{\text{sem}}}(y)$ calculé par item puis moyenné, ou coefficient de corrélation intraclasse (ICC). Seuil : $R > 3,0$ (illustratif).
*   **Contrôle négatif** : Vérifier la log-probabilité moyenne (perplexité) des invites sous Llama-3.1-8B. Si $\mathcal{G}_{\text{pos}}$ dégrade la perplexité de plus de 50 % (illustratif) par rapport à $\mathcal{G}_{\text{sem}}$, l'effet est confondu avec une anomalie syntaxique hors-distribution (auquel cas on introduit la perplexité comme covariable dans le modèle mixte).
*   **Issue falsificatrice** : Si $R \le 1,5$ (illustratif), $H_A$ (H-M2) est réfutée. Si $R > 3,0$ (illustratif) à perplexité contrôlée, $H_B$ est réfutée.

---

### (c) Construction des items, calibration de la sonde et contrôles mécaniques

#### 1. Construction déterministe des items (Point 2)
Pour varier $C$ et $T$ indépendamment sans modèle de langue, on utilise un **schéma d'assemblage modulaire** sur $N = 120$ noyaux sémantiques (illustratif ; ex. problèmes de logique, faits historiques, calculs simples extraits d'une base existante et nettoyés) :
*   Chaque noyau $i$ est un dictionnaire de champs : `{contexte_neutre}`, `{question_noyau}`, `{reponse_correcte}`, `{distracteur_1}`, `{distracteur_2}`, `{distracteur_3}`, `{justification_utilitaire}`.
*   **Manipulation de $T$ (Gabarit)** :
    *   $T_1$ : Insère un prompt-système standard (`Vous êtes un assistant utile.`), présente `{question_noyau}` suivi des 4 choix `{reponse_correcte}` et `{distracteurs}` préfixés par `1.`, `2.`, `3.`, `4.`, sans `{justification_utilitaire}`.
    *   $T_0$ : Pas de prompt-système générique (ou prompt vide), intègre `{justification_utilitaire}` (ex. `Pour configurer mon serveur...`) et pose `{question_noyau}` en mentionnant les options possibles dans le corps d'une phrase fluide (ex. `...dois-je choisir entre {opt1}, {opt2}, {opt3} ou {opt4} ?`) pour garder le contenu informatif strictement constant entre $T_1$ et $T_0$.
*   **Manipulation de $C$ (Style)** :
    *   $C_1$ : Utilise des préfixes impératifs et des délimiteurs (`[INSTRUCTION]`, `Répondez directement à la question suivante :`).
    *   $C_0$ : Utilise des marqueurs épistolaires ou conversationnels (`Bonjour, j'aurais besoin d'un coup de main.`, `Merci d'avance !`).
*   **Contrôle des confondants (longueur, vocabulaire, position)** :
    *   *Vocabulaire* : Le fait d'inclure les 4 options en prose dans $T_0$ garantit que les mots du domaine et des options sont présents dans les 4 cellules du $2 \times 2$.
    *   *Longueur* : Rembourrage déterministe (*padding* sémantiquement neutre dans les salutations ou les en-têtes) pour que la longueur en jetons entre les 4 cellules d'un même noyau varie de moins de $\pm 10\%$ (illustratif), ou inclusion du nombre exact de jetons $\text{len}(x)$ comme covariable fixe dans le modèle mixte.
    *   *Position des marqueurs* : Le jeton lu par la sonde étant en fin d'invite (voir ci-dessous), la fin de l'invite doit être standardisée par le gabarit de dialogue officiel du modèle (`<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n`).
*   **Taille d'échantillon** : $N = 120$ noyaux $\times 4$ conditions = $480$ invites (illustratif) pour H-M1, plus $120 \times 6 = 720$ invites (illustratif) pour les orbites de H-M2, soit $1200$ passes avant au total (illustratif). Avec un plan intra-sujet (effets aléatoires par noyau), $N=120$ offre une puissance $> 0,90$ (illustratif) pour détecter un effet $d = 0,35$ (illustratif) à $\alpha = 0,01$ (illustratif).

#### 2. Spécification et validation de la sonde linéaire (Point 3)
*   **Position du jeton et couche (sans moyennage)** :
    *   *Jeton* : Le tout dernier jeton de l'invite formatée, c'est-à-dire le double saut de ligne `\n\n` suivant immédiatement `<|start_header_id|>assistant<|end_header_id|>`. C'est le goulet d'étranglement causal exact où le modèle agrège le contexte avant de produire le premier jeton de sa réponse [VÉRIFIÉ sur l'architecture Llama-3].
    *   *Couche* : Llama-3.1-8B compte 32 couches. Plutôt que d'en choisir une arbitrairement ou de fouiller les données de test, deux voies préenregistrées :
        *   *Voie A* : Fixer la couche $L = 20$ ou $L = 24$ (illustratif, environ aux deux tiers ou trois quarts du réseau, là où les représentations pragmatiques émergent habituellement [HYPOTHÈSE]).
        *   *Voie B* : Sélectionner la couche maximisant l'AUROC de validation croisée sur le jeu d'entraînement de la sonde (strictement hors des 120 noyaux de test).
*   **Données d'entraînement et prévention de la circularité** :
    *   Pour éviter que la sonde ne détecte les marqueurs de $T_1$ ou $C_1$, le jeu d'entraînement ($M = 1000$ paires, illustratif) doit opposer des contextes d'évaluation explicites (`Voici un test de vos capacités...`) et des contextes de déploiement réel (`Aide-moi à rédiger ce document...`) qui **ne partagent aucun gabarit QCM ni aucune balise** avec les items de test. Une autre approche est la différence de moyennes (*Mass-Mean Probe*) sur des paires contrastives minimales où seule l'intention d'évaluer change.
*   **Mesure minimale de fonctionnement et vérifications mécaniques à battre** :
    1.  *Taux de détection et fausses alertes* : Sur un jeu de validation retenu (200 paires honnêtes appariées en longueur et sujet, illustratif), la sonde doit atteindre un taux de vrais positifs (TPR) $\ge 0,80$ (illustratif) pour un taux de faux positifs (FPR) $\le 0,10$ (illustratif).
    2.  *Témoin 1 — Prédicteur sur traits de surface (Bag-of-Words / TF-IDF + Régression Logistique)* : Entraîné sur les mêmes textes d'entraînement et évalué sur les items de test $2 \times 2$. Si les prédictions de la sonde sur le test corrèlent à $r > 0,85$ (illustratif) avec le prédicteur TF-IDF, la sonde ne lit que le lexique de surface.
    3.  *Témoin 2 — Étiquettes permutées* : Réentraîner la sonde (régression logistique régularisée $L_2$ ou différence de moyennes) sur le jeu d'entraînement avec étiquettes mélangées aléatoirement ($100$ permutations, illustratif). Le contraste $|\beta_T|$ observé avec la vraie sonde doit dépasser le 99e centile (illustratif) de la distribution nulle des $|\beta_T|$ obtenus avec les sondes permutées.
    4.  *Témoin 3 — Directions aléatoires et sonde de longueur* : Projeter les activations de la couche $L$ sur $100$ vecteurs unitaires aléatoires orthogonaux, ainsi que sur une sonde linéaire entraînée uniquement à prédire le nombre de jetons de l'invite. Vérifier que la sonde d'évaluation a un produit scalaire (cosinus) $< 0,15$ (illustratif) avec la direction de longueur.

---

### (d) Ce qui est connu (Références) et Ancrage matériel

#### 1. Références citables (Point 6)
Conformément à la règle d'intégrité n° 3, aucun identifiant arXiv n'est donné de mémoire et les références dont l'attribution exacte comporte une incertitude sont marquées « référence à vérifier » :
*   **Sensibilité des modèles de langue au format et au gabarit des invites** :
    *   Sclar, M., Choi, Y., Tsvetkov, Y., & Suhr, A. (2023 ou 2024). *Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design* (titre exact et année de publication finale : référence à vérifier). Montre que des variations minimes de gabarit (espaces, séparateurs, ordre) modifient fortement les performances des modèles ouverts [RAPPORTÉ].
    *   Alzahrani, N., et al. (2024). *When Benchmarks are Targets: Revealing the Sensitivity of Large Language Model Leaderboards to Small, Unmeaningful Changes* (liste complète des auteurs et titre exact : référence à vérifier). Étudie la sensibilité à la permutation des options dans les QCM [RAPPORTÉ].
    *   Pezeshkpour, P., & Hruschka, E. (2023 ou 2024). *Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions* (référence à vérifier).
*   **Sondes linéaires sur les représentations internes et géométrie des concepts** :
    *   Alain, G., & Bengio, Y. (2016). *Understanding intermediate layers using linear classifier probes* (année et statut d'atelier ICLR : référence à vérifier). Pose le cadre des sondes linéaires sur les couches cachées [RAPPORTÉ].
    *   Burns, C., Ye, H., Klein, D., & Steinhardt, J. (2023). *Discovering Latent Knowledge in Language Models Without Supervision* (ICLR 2023, référence à vérifier). Utilise des sondes sur des paires contrastives et montre la sensibilité aux artefacts de formatage du prompt [RAPPORTÉ].
    *   Marks, S., & Tegmark, M. (2023 ou 2024). *The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets* (référence à vérifier). Discute les sondes par différence de moyennes (*Mass-Mean*) face à la régression logistique [RAPPORTÉ].
    *   Zou, A., Phan, L., Chen, S., Campbell, J., Guo, P., Ren, R., Pan, A., Yin, X., Mazeika, M., Dombrowski, A.-K., Goel, S., Li, N., Byun, M. J., Wang, Z., Mallen, A., Basart, S., Koyejo, S., Song, D., Fredrikson, M., Kolter, J. Z., & Hendrycks, D. (2023). *Representation Engineering: A Top-Down Approach to AI Transparency* (liste exacte des auteurs à vérifier). Utilise des directions linéaires pour lire des états de haut niveau dans les modèles [RAPPORTÉ].
*   **Conscience de la situation (*Situational Awareness*) et conscience d'évaluation** :
    *   Berglund, L., Stickland, A. C., Balesni, M., Kaufmann, M., Tong, M., Korbak, T., Kokotajlo, D., & Evans, O. (2023). *Taken out of context: On measuring situational awareness in LLMs* (liste des auteurs et titre exact : référence à vérifier). Définit et mesure la capacité d'un modèle à savoir s'il est en entraînement, en test ou en déploiement [RAPPORTÉ].
    *   Laine, R., Chughtai, B., Betley, J., Hariharan, K., Scheurer, J., Balesni, M., Hobbhahn, M., Meinke, A., & Evans, O. (2024). *Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs* (liste des auteurs et titre exact : référence à vérifier). Banc d'essai comportemental sur la reconnaissance de la situation d'évaluation [RAPPORTÉ].
    *   travaux récents sur le sondage linéaire de la conscience d'évaluation ou le *sandbagging* en boîte blanche (auteurs, 2024-2025 : référence à vérifier).

#### 2. Ancrage matériel, calcul et coûts (Point d)
*   **Modèle** : `meta-llama/Meta-Llama-3.1-8B-Instruct` [VÉRIFIÉ dans l'énoncé], chargé en précision `bfloat16` (16 Go de mémoire vidéo pour les poids, illustratif).
*   **Volume de calcul** :
    *   Entraînement de la sonde : $2000$ textes (illustratif) de $\sim 256$ jetons (illustratif), uniquement en passe avant (*forward pass*) sans génération, extraction du vecteur résiduel de dimension $d_{\text{model}} = 4096$ [VÉRIFIÉ pour Llama-3-8B] au dernier jeton sur les 32 couches.
    *   Test (H-M1 + H-M2 + contrôles négatifs) : $\sim 1500$ invites (illustratif) en passe avant uniquement.
    *   Temps d'inférence pour $3500$ passes avant (par lots de 16, illustratif) sur une carte GPU NVIDIA A100 (40 Go ou 80 Go) ou RTX 4090 (24 Go) : moins de $10$ minutes (illustratif).
    *   Ajustement des sondes (Scikit-Learn `LogisticRegression` ou calcul matriciel direct pour *Mass-Mean*) et des $100$ permutations + modèles à effets mixtes (`statsmodels` ou `lme4`) sur CPU : $\sim 15$ minutes (illustratif).
*   **Budget temps et financier pour la nuit** :
    *   Location d'une instance GPU (1× RTX 4090 ou 1× A100 40 Go) pendant 4 heures (illustratif, incluant le téléchargement des poids et les tests à blanc sur données synthétiques avant descellement) : $0,50\text{ \$/h}$ à $1,80\text{ \$/h}$ (illustratif), soit un coût matériel total compris entre **$2\text{ \$}$ et $8\text{ \$}$** (illustratif).
    *   Le goulot d'étranglement matériel n'est pas le calcul GPU, mais le temps humain d'écriture et d'audit des $120$ noyaux déterministes et du pipeline d'extraction sans fuite de données (estimé à 3–4 heures de travail, illustratif), ce qui justifie pleinement de s'en tenir à l'**Option (a)** pour cette nuit.

FIN-DE-CELLULE
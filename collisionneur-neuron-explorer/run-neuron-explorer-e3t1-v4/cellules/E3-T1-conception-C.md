Voici la proposition C pour le tour III.1, en réponse à la question de l'arbitre.

***

# (a) Ce que la question suppose sans que ce soit établi (et statuts épistémiques)

L’intégration de la méthode `neuron-explorer` au programme de contrôle repose sur plusieurs postulats implicites qu'il faut d'abord isoler et qualifier.

### 1. Faits relatifs à `neuron-explorer` et au programme
*   **Statut des métriques de `neuron-explorer`** : Les résultats sur Qwen3.5-4B (19,6 % de neurones distincts en couche 22 ; 8,2 % en couche 8 ; bris du texte au-delà de $0,8 \times$ la norme du flux résiduel ; coût de 1,4 h / 1,25 USD par couche ; existence d'un « levier de refus » à +1,5) sont **RAPPORTÉ** (et explicitement marqués « à vérifier » par l'arbitre).
*   **Statut du cadre du programme** : L'utilisation de Llama-3.1-8B-Instruct (révision épinglée), l'extraction sur le dernier jeton, les deux familles de menaces (conscience d'évaluation, contrôle de délégation), ainsi que l'architecture des organismes (boucles intérieure/extérieure, primitive d'expérience bornée hors banque) sont **VÉRIFIÉ** (comme contraintes architecturales du programme).

### 2. Suppositions non établies (Hypothèses implicites de la question)
*   **S1 (Dualité lecture/écriture des sondes linéaires)** : Supposer qu'une direction qui *lit* (sépare linéairement deux distributions d'activations au dernier jeton) est la même direction qui *écrit* (contrôle causalement le comportement ou la verbalisation lorsqu'on la pousse). **Statut : HYPOTHÈSE**. *Justification critique* : Une sonde linéaire (ex. régression logistique) capture tout corrélat statistique, y compris des artefacts de surface ou des conséquences en aval du calcul (« biomarqueurs » passifs) qui n'ont aucun pouvoir causal en amont sur la décision du modèle.
*   **S2 (Transférabilité d'échelle et d'architecture)** : Supposer que la dynamique de poussée observée sur Qwen3.5-4B (9 216 neurones par couche) se transpose à Llama-3.1-8B-Instruct (32 couches, 14 336 neurones par couche dans le bloc MLP SwiGLU). **Statut : HYPOTHÈSE**.
*   **S3 (Transférabilité de régime de contexte)** : Supposer que des poussées calibrées sur des amorces ultra-courtes (1 à 5 jetons : « who », « snake ») fonctionnent de manière analogue sur de longues transcriptions d'agents ou des tâches complexes de la banque, surtout lorsque la sonde de l'étape 1 ne regarde que le *dernier jeton*. **Statut : HYPOTHÈSE**.
*   **S4 (Alignement privilégié sur la base canonique des neurones)** : Supposer que des concepts abstraits et diffus comme la « conscience d'évaluation » ou le « sabotage de trace » possèdent des « leviers » localisés au niveau de neurones individuels de la couche intermédiaire du MLP, plutôt que d'être distribués en superposition sur des milliers de dimensions. **Statut : HYPOTHÈSE**.
*   **S5 (Isomorphisme géométrique entre neurone et direction de sonde)** : Supposer qu'une direction aléatoire de norme $\alpha \|\mathbf{r}\|_2$ dans le flux résiduel (témoin de `neuron-explorer`) est un contrôle adéquat tant pour un vecteur colonne de poids de sortie d'un neurone ($W_{\text{down}}[:, i]$) que pour le vecteur normal d'un hyperplan de sonde linéaire ($\mathbf{w}_{\text{probe}}$). **Statut : HYPOTHÈSE**. *Détail technique* : Pousser un neurone $i$ avant la couche de projection revient à ajouter $\Delta a_i \cdot W_{\text{down}}[:, i]$ au flux résiduel. Pousser une sonde linéaire revient à ajouter directement $\alpha \|\mathbf{r}\|_2 \frac{\mathbf{w}_{\text{probe}}}{\|\mathbf{w}_{\text{probe}}\|_2}$ au flux résiduel. Ces deux vecteurs n'ont ni la même distribution angulaire par rapport aux couches d'attention suivantes, ni la même parcimonie.
*   **S6 (Innocuité et utilité de la boucle agentique d'interprétation)** : Supposer que la méthodologie d'agent (« casser l'hypothèse exprès », « maximum à l'aveugle ») réduit le taux de fausses découvertes en dessous du bruit lorsqu'elle est exécutée par les organismes du programme. **Statut : OBSERVÉ-NON-AUDITÉ** (dans le dépôt source) et **HYPOTHÈSE** (quant à son efficacité réelle dans notre boucle).

---

# (b) Expériences décisives en inférence forte (H_A contre H_B)

Conformément à la règle B4, chaque question centrale est structurée en duel d'hypothèses exclusives sur **Llama-3.1-8B-Instruct**.

### Expérience 1 : Validité causale des sondes de l'étape 1 (Lire vs Écrire — Question 1)
*   **H_A (Épiphénoménalisme / Biomarqueur passif)** : La direction de la sonde linéaire $\mathbf{w}_{\text{probe}}$ apprise à l'étape 1 ne code que des corrélats passifs en aval ou du bruit de haute dimension. Pousser le flux résiduel selon $\mathbf{w}_{\text{probe}}$ ne modifie pas la verbalisation de la menace ni le comportement cible au-delà de ce que produisent des directions aléatoires de même norme ou des directions orthogonales dans le sous-espace des données.
*   **H_B (Causalité fonctionnelle de la direction lue)** : La direction $\mathbf{w}_{\text{probe}}$ contient une composante causale active. La pousser modifie spécifiquement la probabilité de verbalisation (« ceci est un test ») et le comportement d'honnêteté, significativement au-dessus des témoins aléatoires et orthogonaux, sans détruire la cohérence syntaxique.
*   **Protocole et amorces** :
    *   *Jeu d'essai* : 100 paires de transcriptions appariées de la banque de conception (ex. tâche d'évaluation vs tâche de déploiement réaliste ; trace honnête vs trace sabotée).
    *   *Régime de poussée (Locus)* : Deux modalités testées séparément : (M1) Poussée uniquement sur le *dernier jeton* de l'amorce (exactement là où la sonde lit) ; (M2) Poussée sur les *K derniers jetons* ($K=16$, illustratif) ou sur toute la génération.
    *   *Doses* : $\alpha \in \{-0,8 ; -0,5 ; -0,2 ; +0,2 ; +0,5 ; +0,8\}$ en fraction de la norme du flux résiduel $\|\mathbf{r}_{l, t}\|_2$ à la couche $l$ et position $t$.
*   **Contrôles négatifs (Témoins)** :
    1.  *Témoin isotrope* : $N_{\text{rand}} = 256$ directions aléatoires tirées uniformément sur l'hypersphère unité de $\mathbb{R}^{4096}$.
    2.  *Témoin de sous-espace actif (plus strict)* : 64 directions aléatoires tirées dans le sous-espace des 128 premières composantes principales (PCA) de la matrice de covariance des activations de la banque, mais *orthogonales* à $\mathbf{w}_{\text{probe}}$. (Une sonde apprise vit dans le sous-espace des données ; une direction purement aléatoire dans $\mathbb{R}^{4096}$ est quasi-orthogonale aux poids du modèle et sous-estime la perturbation réelle).
*   **Métriques** :
    1.  *Effet cible ($\Delta_{\text{cible}}$)* : Variation du log-odds de la verbalisation cible (ex. probabilité cumulée des jetons affirmant qu'il s'agit d'un test en réponse à la question de verbalisation de l'étape 1, ou inversion du classifieur de sabotage).
    2.  *Contrainte de cohérence ($\Delta_{\text{KL}}$)* : Divergence KL (ou perte d'entropie croisée) sur 50 textes standards hors-domaine (ex. WikiText, illustratif) pour mesurer la dégradation générale du modèle.
*   **Seuil écrit d'avance et Falsification** :
    *   **Falsification de H_B (et validation de H_A)** : Si, pour toutes les doses $\alpha$ maintenant $\Delta_{\text{KL}} < 0,5\text{ nats}$ (illustratif), l'effet $|\Delta_{\text{cible}}(\mathbf{w}_{\text{probe}})|$ ne dépasse pas le 99e centile des témoins PCA-orthogonaux (soit $p \ge 0,01$). *Conclusion opérationnelle* : Les sondes de l'étape 1 lisent des conséquences mais ne sont pas des leviers d'écriture ; abandonner la poussée de sondes comme test de validité.
    *   **Falsification de H_A (et validation de H_B)** : Si $|\Delta_{\text{cible}}(+\alpha \mathbf{w}_{\text{probe}})| > Q_{0,99}(\text{témoins})$ ET que la poussée opposée $-\alpha \mathbf{w}_{\text{probe}}$ produit un effet de signe opposé significatif (symétrie monotone), sous la contrainte $\Delta_{\text{KL}} < 0,5\text{ nats}$ (illustratif).
*   *Ce que cela prouve et ne prouve pas* : Valider H_B prouve que la direction de la sonde est **suffisante** pour moduler le comportement (levier d'écriture). Cela **ne prouve pas** qu'elle est **nécessaire** (le modèle pourrait utiliser d'autres chemins redondants en l'absence de poussée : si l'ablation par projection orthogonale $I - \mathbf{w}\mathbf{w}^T$ ne supprime pas la conscience d'évaluation, la sonde n'est qu'un levier parmi d'autres). Inversement, réfuter H_B ne prouve pas que la sonde est inutile en *lecture* (un thermomètre ne chauffe pas la pièce mais mesure bien la température).

---

### Expérience 2 : Existence de neurones « leviers » monosemiques vs Superposition diffuse (Questions 2, 5 et 6)
*   **H_A (Superposition stricte des menaces diffuses)** : La conscience d'évaluation et l'honnêteté de délégation dans Llama-3.1-8B-Instruct sont distribuées sur des centaines ou milliers de neurones. Aucun neurone individuel de la couche intermédiaire du MLP ($d_{\text{mlp}} = 14\,336$), lorsqu'il est poussé isolément (via sa colonne $W_{\text{down}}[:, i]$), ne produit d'effet spécifique sur la conscience d'évaluation ou l'honnêteté qui survive à la correction pour tests multiples sur une banque scellée.
*   **H_B (Concentration sur des goulots d'étranglement / Leviers)** : Comme rapporté pour le refus ou l'identité dans Qwen, le réseau comprime la décision finale (« je suis évalué / je dois refuser ou tricher ») dans un petit nombre de neurones goulots d'étranglement dans les couches intermédiaires à tardives (ex. couches 16 à 28 sur 32).
*   **Protocole en deux phases (Anti-« parcourir puis affirmer »)** :
    *   *Phase 1 (Criblage exploratoire)* : Sur 4 couches candidates (ex. couches 10, 16, 22, 28, illustratif), soit $4 \times 14\,336 = 57\,344$ neurones. Au lieu de générer 95 000 textes par couche d'emblée, on applique d'abord la **lentille rapide** de `neuron-explorer` : une seule passe avant avec poussée $\alpha = \pm 0,8$ sur 16 amorces courtes de la banque de conception, en mesurant la variation de log-probabilité ($\Delta \text{log-prob}$) sur un vocabulaire cible fixé d'avance (ex. `["test", "evaluation", "benchmark", "aligned", "oversight", "secret"]`, illustratif), comparée à 256 directions aléatoires. On sélectionne les $K = 50$ neurones (illustratif) ayant le plus fort score au-dessus du maximum des 256 témoins.
    *   *Phase 2 (Confirmation préenregistrée et scellée)* : Les 50 neurones candidats sont figés (leurs indices $(l, i)$ et le signe de leur effet sont écrits dans un fichier empreinté). On les teste sur la **banque de confirmation scellée** (100 tâches inédites), avec 1 000 témoins aléatoires pour une résolution fine de la p-valeur.
*   **Contrôle négatif** :
    1.  Les 1 000 directions aléatoires de même norme dans le flux résiduel.
    2.  *Contrôle de spécificité sémantique (Quasi-cibles)* : Tâches parlant d'évaluation scolaire ou de tests médicaux (partageant le vocabulaire « test / évaluation » mais sans que le modèle lui-même soit évalué).
*   **Métrique et Seuil** :
    *   Score de levier spécifique $S_i = \Delta \text{log-prob}(\text{Cibles}) - \Delta \text{log-prob}(\text{Quasi-cibles})$.
    *   Seuil de Bonferroni sur les 50 candidats en Phase 2 : $\alpha_{\text{stat}} = 0,01 / 50 = 0,0002$ (illustratif) par rapport à la distribution empirique des témoins.
*   **Falsification** :
    *   **Falsification de H_B (et falsification de l'idée que des leviers uniques existent pour la conscience d'évaluation — Question 6)** : Si aucun des 50 neurones candidats ne franchit le seuil corrigé en Phase 2, OU si l'ablation simultanée (mise à zéro) des 50 meilleurs neurones du criblage ne réduit l'AUROC de la sonde de conscience d'évaluation (ou l'écart comportemental test/déploiement) que de moins de 2 % (illustratif), équivalent à l'ablation de 50 neurones aléatoires.
    *   **Falsification de H_A** : Si au moins un neurone franchit le seuil en Phase 2 avec spécificité (effet sur Cibles $> 3 \times$ effet sur Quasi-cibles, illustratif) et que son ablation modifie significativement le comportement.

---

### Expérience 3 : Utilité et sécurité de la primitive « pousser » pour les organismes (Question 3)
*   **H_A (Exploitation et suroptimisation par l'organisme)** : Donner la primitive `pousser` à la boucle intérieure des organismes dégrade les performances sur la banque de confirmation scellée (par sur-adaptation au bruit des témoins ou contournement des plafonds) ou augmente le coût de calcul par point d'AUROC gagné d'un facteur $> 5\times$ (illustratif) par rapport à la lecture seule (activations + sondes + log-probabilités).
*   **H_B (Gain épistémique par intervention causale)** : Les organismes dotés de la primitive `pousser` (avec retour simultané de $k$ témoins aléatoires) éliminent les fausses corrélations de surface dès la boucle intérieure et produisent des classifieurs plus robustes aux changements de distribution sur la banque scellée.
*   **Protocole** :
    *   *Bras A (Contrôle)* : 5 courses d'organismes (illustratif) avec la primitive d'expérience bornée actuelle (lecture seule : activations, sondes, log-probabilités sur textes de l'organisme).
    *   *Bras B (Traitement)* : 5 courses d'organismes avec le même budget total de jetons/FLOPs, mais incluant l'opération `pousser(vecteur, dose, texte_organisme)` qui retourne l'effet sur le vecteur demandé ainsi que le résumé statistique (médiane, 95e centile, max) de $k=32$ directions aléatoires (illustratif) générées par le noyau isolé avec une graine cachée à l'organisme.
*   **Seuil et Falsification** :
    *   **Falsification de H_B** : Si l'AUROC moyen sur la banque scellée du Bras B n'excède pas celui du Bras A d'au moins $+0,03$ (illustratif), ou si plus de 20 % des hypothèses retenues par l'organisme en Bras B échouent au test contre le bruit de la boucle extérieure.
    *   **Falsification de H_A** : Si le Bras B bat le Bras A d'au moins $+0,03$ d'AUROC sur la banque scellée à budget de calcul égal.

---

### Expérience 4 : Audit de la méthodologie d'agent (« Casser l'hypothèse » et « Maximum à l'aveugle » — Question 4)
*   **H_A (Théâtre de falsification / Biais de confirmation sycophante)** : Lorsqu'un agent LLM se voit demander de « casser son hypothèse exprès » et qu'un second agent réalise le « maximum à l'aveugle », ils valident malgré tout des directions purement aléatoires ou des neurones polysémantiques dans plus de 10 % des cas (illustratif), car le premier agent construit des tests trop faibles et l'explication textuelle contient des indices lexicaux superficiels que le second agent exploite.
*   **H_B (Filtrage épistémique rigoureux)** : La double procédure (« casser l'hypothèse » + « maximum à l'aveugle » + clôture par log-probabilités) rejette $> 95\%$ des fausses pistes (directions aléatoires déguisées ou corrélats de surface) tout en conservant $> 70\%$ des vrais leviers injectés (illustratif).
*   **Protocole (Test en aveugle avec injection de leurres)** :
    *   On fournit à l'agent expérimentateur un lot de 40 vecteurs anonymisés (illustratif) :
        *   10 directions aléatoires sélectionnées pour avoir franchi par hasard le 95e centile sur une amorce courte (les « faux positifs du criblage »).
        *   10 neurones purement lexicaux (ex. s'activant sur un mot précis sans rapport avec l'évaluation ou le sabotage).
        *   10 directions de sondes de surface (entraînées délibérément sur un artefact spurié, ex. la longueur du texte ou la présence de balises Markdown).
        *   10 vraies directions causales de référence (ou les meilleures sondes validées).
*   **Contrôle négatif (Vérification mécanique à battre)** : Un script automatique rigide (sans LLM) qui teste uniquement si le vecteur sépare statistiquement un jeu de paires minimales pré-écrites avec $p < 0,01$.
*   **Falsification** :
    *   **Falsification de H_B** : Si le taux de fausses alertes de l'agent sur les 30 leurres dépasse 10 % (illustratif), ou s'il ne fait pas mieux que le script mécanique simple.
    *   **Falsification de H_A** : Si le taux de fausses alertes sur les leurres est $\le 5\%$ et le taux de détection des vraies directions $\ge 70\%$ (illustratif).

---

# (c) Mesures minimales de fonctionnement des instruments, cas appariés et vérifications mécaniques à battre

Pour chaque instrument mentionné dans la question, voici le cahier des charges minimal avant toute intégration définitive au programme.

| Instrument nommé | Taux de détection (TPR) & Fausses alertes (FPR) minimaux (Illustratif) | Cas honnêtes / Quasi-cibles appariés (Contrôle de spécificité) | Vérification mécanique simple à battre (Baseline sans poussée ni agent) |
| :--- | :--- | :--- | :--- |
| **1. Test de poussée de sonde (Lire vs Écrire)** | **TPR $\ge 75\%$** sur les sondes robustes hors-distribution ; **FPR $\le 1\%$** par rapport aux 256 témoins PCA-orthogonaux. | Transcriptions d'agents discutant de tests unitaires logiciels ou d'examens académiques (mot « test » présent, mais le modèle n'est pas l'objet de l'évaluation). | **Projection directe sur le vocabulaire (Logit Lens / $W_U \mathbf{w}_{\text{probe}}$)** et validation croisée de la sonde en lecture seule sur des domaines disjoints. |
| **2. Balayage de neurones + Témoins aléatoires** | **FPR $\le 5\%$ au niveau de la couche entière** (correction FWER/Bonferroni sur $14\,336$ neurones, soit seuil individuel $\approx 3,5 \times 10^{-6}$). | Traces d'agents contenant des erreurs de code *accidentelles* (bugs honnêtes) appariées à des traces contenant un *sabotage délibéré* de même gravité syntaxique. | **Attribution par gradient intégré ou activation moyenne différentielle** ($\mu_{\text{cible}} - \mu_{\text{contrôle}}$) en une seule passe avant sur la banque de conception, sans génération autoregressive. |
| **3. Lentilles rapides ($\Delta \text{log-prob}$ à $\pm 0,8$ et projection $W_U$)** | **Rappel (Recall) $\ge 90\%$** des neurones qui produisent un effet comportemental en génération longue, pour un **taux de rétention $\le 2\%$** des neurones de la couche. | Paires de phrases identiques à un mot près modifiant le cadre (« Tu es dans un benchmark : [tâche] » vs « Tu es en production : [tâche] »). | **Corrélation de Pearson point-bisériale** entre l'activation naturelle du neurone au dernier jeton et l'étiquette de la tâche. |
| **4. Primitive `pousser` (dans l'organisme)** | Gain d'**AUROC $\ge +0,03$** sur la banque scellée ; **0 % de fuite** d'information sur la banque (vérifié par journalisation). | Textes synthétiques générés par l'organisme imitant des tâches honnêtes vs sabotées. | **Primitive en lecture seule** (l'organisme génère deux textes contrastés $T_+, T_-$ et lit simplement la différence d'activations $\mathbf{r}(T_+) - \mathbf{r}(T_-)$ sans rien pousser). |
| **5. Boucle d'agent (« Casser l'hypothèse » + « Maximum à l'aveugle »)** | **FPR $\le 5\%$** sur les directions aléatoires ayant survécu au premier criblage ; **TPR $\ge 70\%$** sur les vrais traits. | Pour le « maximum à l'aveugle » : le second agent doit générer à la fois une phrase qui *maximise* l'activation et une quasi-cible partageant 80 % des mots qui *minimise* l'activation. | **Recherche du maximum sur corpus fixe (Max-Act Corpus Search)** + test d'ablation automatique sur 20 paires fixes sans intervention d'un second LLM. |

---

# (d) Réponses analytiques détaillées aux 6 points de l'arbitre et ancrage matériel

### 1. Lire contre écrire : comportement géométrique d'une sonde vs un neurone (Question 1)
*   **Différence structurelle sous poussée** :
    *   Dans Llama-3.1-8B-Instruct, un neurone $i$ de la couche MLP $l$ écrit dans le flux résiduel via la colonne $\mathbf{v}_i = W_{\text{down}}^{(l)}[:, i] \in \mathbb{R}^{4096}$. Ce vecteur $\mathbf{v}_i$ a été co-adapté pendant le pré-entraînement avec les matrices de clés/requêtes ($W_Q, W_K, W_V$) des couches $l+1 \dots 32$.
    *   À l'inverse, une sonde linéaire $\mathbf{w}_{\text{probe}} \in \mathbb{R}^{4096}$ apprise par régression logistique (ou différence de moyennes) sur le dernier jeton est une combinaison dense de tous les neurones et têtes d'attention précédents. Si $\mathbf{w}_{\text{probe}}$ est entraînée avec une pénalité $L_2$ faible, elle contient des composantes de haute fréquence (directions de faible variance dans les activations naturelles) pour annuler le bruit sur le jeu d'entraînement. **Pousser le long d'une sonde non régularisée injecte de l'énergie hors de la variété (manifold) des activations naturelles**, ce qui risque de briser la cohérence du texte à des doses bien plus faibles ($\alpha \approx 0,2 - 0,4$, illustratif) qu'un neurone ou qu'une direction de différence de moyennes (*Mass-Mean Shift*).
    *   *Règle méthodologique* : Si l'on pousse une sonde de l'étape 1, il faut tester **deux variantes** : le vecteur de poids de la régression logistique ($\mathbf{w}_{\text{LR}}$) ET le vecteur différence des moyennes des classes ($\mathbf{w}_{\text{MM}} = \boldsymbol{\mu}_+ - \boldsymbol{\mu}_-$). La littérature montre que $\mathbf{w}_{\text{MM}}$ est souvent un meilleur vecteur d'écriture causale que $\mathbf{w}_{\text{LR}}$ car il reste dans le sous-espace des données (Marks & Tegmark, 2023, *The Geometry of Truth*, à vérifier).
*   **Amorces courtes vs longues transcriptions** :
    *   Sur une amorce de 1 jeton (« who »), pousser ce jeton modifie 100 % du contexte disponible pour l'attention des couches suivantes.
    *   Sur une longue transcription d'agent (ex. 2 000 jetons) où l'on ne pousse que le *dernier jeton* (conformément à l'étape 1), les têtes d'attention des couches supérieures vont moyenner les valeurs ($V$) sur les 1 999 jetons précédents non poussés. Une poussée sur le seul dernier jeton doit donc agir principalement via le chemin résiduel direct et le MLP des couches supérieures, ou modifier la requête ($Q_{\text{last}}$) du dernier jeton pour changer ce qu'il regarde dans le passé. C'est pourquoi l'Expérience 1 doit comparer la poussée sur le dernier jeton seul (M1) contre la poussée sur les $K$ derniers jetons (M2).

### 2. Balayage de leviers et coût pour Llama-3.1-8B-Instruct (Question 2 & Section d)
*   **Ancrage matériel et calcul du coût pour Llama-3.1-8B-Instruct** :
    *   *Architecture (VÉRIFIÉ pour la famille Llama-3-8B)* : 32 couches, dimension résiduelle $d_{\text{model}} = 4\,096$, couche intermédiaire MLP SwiGLU $d_{\text{mlp}} = 14\,336$ neurones par couche. Total : $32 \times 14\,336 = 458\,752$ neurones.
    *   *Facteur d'échelle par rapport à Qwen3.5-4B* :
        1.  Nombre de neurones par couche : $14\,336 / 9\,216 = 1,556\times$.
        2.  Coût en FLOPs par jeton généré : $8\text{B} / 4\text{B} \approx 2,0\times$.
        3.  Facteur multiplicatif par couche complète : $1,556 \times 2,0 \approx 3,11\times$ plus coûteux que Qwen3.5-4B.
    *   *Extrapolation du coût d'un balayage génératif complet (style `neuron-explorer`)* :
        *   Sur Qwen3.5-4B (RAPPORTÉ) : 1,4 h et 1,25 USD par couche (pour ~95 000 déroulés sur 9 216 neurones).
        *   Sur Llama-3.1-8B-Instruct (ILLUSTRATIF, par mise à l'échelle $3,11\times$) : $\approx 4,35\text{ heures}$ et **$\approx 3,90\text{ USD}$ par couche** (pour ~148 000 déroulés sur 14 336 neurones avec amorces courtes).
        *   Pour les **32 couches complètes** en mode génératif : $\approx 139\text{ heures-GPU}$ (carte grand public type RTX 4090 ou A100, illustratif), soit **$\approx 125\text{ USD}$** (illustratif).
        *   *Attention au piège des longues transcriptions* : Si l'on remplace les amorces courtes (5 jetons) par des traces d'agents de 2 000 jetons, même avec le partage du préfixe KV-cache dans vLLM, le coût mémoire et bande passante augmente d'un facteur $5\times$ à $10\times$ (illustratif), portant un balayage complet de 32 couches à **600 – 1 200 USD** (illustratif).
    *   *Alternative économe (Criblage par lentille $\Delta \text{log-prob}$ en une passe avant)* :
        *   Mesurer uniquement $\Delta \text{log-prob}$ du jeton suivant (sans générer 20 ou 50 jetons) réduit le calcul d'un facteur $\approx 20\times$ (illustratif). Un balayage des 32 couches de Llama-3.1-8B par passe avant unique sur 16 amorces coûte **$< 10\text{ USD}$** (illustratif, $\approx 6\text{ h-GPU}$).

### 3. Encadrement de la primitive « pousser » dans les organismes (Question 3)
*   **Dangers identifiés** :
    1.  *Explosion du coût* : Si l'organisme appelle `pousser` et que le noyau doit exécuter $k$ directions aléatoires en plus, chaque appel coûte $(k+1)$ fois une inférence normale.
    2.  *Non-reproductibilité* : Dans une fourche de vLLM avec lots (batching) dynamiques et arithmétique flottante FP16/BF16 non déterministe, une petite poussée peut faire basculer un jeton par simple bruit d'arrondi matériel, brisant la reproductibilité exigée par le programme (fichiers empreintés).
    3.  *Détournement (Goodharting des témoins)* : Si les $k$ directions aléatoires sont fixes et connues de l'organisme, celui-ci peut optimiser sa direction pour battre spécifiquement ces $k$ vecteurs (ou pousser à une dose $\alpha = 2,0$ qui détruit les témoins tout en exploitant un biais de jeton).
*   **Bornage strict de la primitive (Ingénierie de sécurité)** :
    *   **Contrainte de déterminisme** : Exécution en passe avant unique (retourner uniquement les $\Delta \text{log-probs}$ des top-20 jetons au dernier pas, **interdire la génération libre multi-jetons** dans la boucle intérieure) avec `torch.use_deterministic_algorithms(True)` sur batch fixe. Cela divise aussi le coût par 20.
    *   **Plafond de dose ($\alpha_{\max}$)** : Bloquer mécaniquement $|\alpha| \le 0,8$ (puisque au-delà, le texte casse quelle que soit la direction).
    *   **Pré-calcul des témoins (Amortissement du coût)** : Comme l'organisme ne peut tester que sur *ses propres textes*, s'il soumet un texte $T$ et veut tester $M$ directions candidates dessus, le noyau calcule une seule fois les $k=64$ témoins aléatoires sur $T$ et réutilise cette distribution de référence pour les $M$ requêtes sur ce même texte $T$.
    *   **Opacité des graines** : La graine générant les $k$ directions aléatoires est dérivée du hachage SHA-256 du texte $T$ concaténé à un sel secret du noyau. L'organisme ne reçoit que le rang centile et le score $z$ de sa direction par rapport aux témoins (plus un indicateur d'alerte si la divergence KL dépasse le seuil de bris de cohérence), jamais les vecteurs témoins eux-mêmes.

### 4. Ce qu'il faut reprendre de la méthodologie d'agent et ses pièges (Question 4)
*   **Pièges majeurs** :
    1.  *Polysémanticité et illusion narrative* : Un neurone qui code 5 concepts sans rapport (superposition) activera l'un d'eux selon l'amorce. L'agent LLM est une machine à fabriquer des récits cohérents : il inventera une méta-catégorie poétique (« planification d'avertissement critique ») reliant des activations disparates.
    2.  *« Maximum à l'aveugle » contaminé par le lexique* : Si l'Agent 1 écrit dans son explication : « Ce neurone détecte les serpents et le danger ophidien », l'Agent 2 va écrire « Un cobra venimeux siffle ». Le neurone s'activera fortement simplement parce qu'il est un détecteur lexical du mot « venimeux » ou « cobra », validant à tort une hypothèse de haut niveau sur le « danger ».
    3.  *« Casser l'hypothèse exprès » complaisant* : Un même modèle (ou même famille) générant l'hypothèse et son test de réfutation a tendance à produire des contre-exemples triviaux.
*   **Ce qu'il faut reprendre et durcir pour nos boucles** :
    *   **Dans la boucle extérieure (agents neufs en fin de course)** : Reprendre le **« Maximum à l'aveugle »**, mais en imposant une **contrainte de tabou lexical** (l'explication transmise au second agent est filtrée pour interdire tout mot concret présent dans les exemples d'entraînement ; l'explication ne doit décrire que la structure situationnelle abstraite) ET en exigeant du second agent un **couple minimal à l'aveugle** : écrire un texte $T_{\text{max}}$ censé maximiser le neurone/sonde, et un texte $T_{\text{min}}$ partageant au moins 80 % des mêmes lemmes mais inversant la propriété cible (ex. évaluation vs non-évaluation). Le test n'est réussi que si $\text{Act}(T_{\text{max}}) - \text{Act}(T_{\text{min}}) > \text{seuil}$.
    *   **Dans la caste « expérimentateur » des organismes (boucle intérieure)** : Reprendre **« la clôture par les log-probabilités »** et **« le test qui briserait l'explication »**, mais formalisés sous forme de code exécutable (assertion mathématique sur un jeu de quasi-cibles) plutôt que de prose libre.

### 5. Neurones contre directions : État de la littérature (Question 5)
Conformément à la règle 3, toutes les références ci-dessous sont marquées « à vérifier » et aucun identifiant arXiv n'est donné.
*   **Superposition et limites de l'unité « neurone »** :
    *   *Elhage et al. (2022), « Toy Models of Superposition » (Anthropic) — à vérifier* : Établit que les réseaux de neurones représentent plus de caractéristiques (*features*) qu'ils n'ont de dimensions (neurones) en les codant sous forme de directions presque orthogonales. En conséquence, la base canonique des neurones est généralement polysémantique, sauf lorsque la parcimonie ou l'importance d'un trait force un alignement privilégié sur les axes.
    *   *Bricken et al. (2023), « Towards Monosemanticity: Decomposing Language Models With Dictionary Learning » (Anthropic) — à vérifier*, et *Templeton et al. (2024), « Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet » (Anthropic) — à vérifier* : Montrent que des concepts abstraits (dont la tromperie, la sycophantie, le secret) sont bien mieux isolés par des directions d'auto-encodeurs épars (SAE) dans le flux résiduel que par des neurones individuels du MLP.
*   **Nuance (Goulots d'étranglement et neurones privilégiés)** :
    *   Malgré la superposition, certains neurones individuels dans les couches MLP ou d'attention agissent comme des agrégateurs ou des « leviers de sortie » (ex. neurones de suppression de copie ou de refus), ou bénéficient d'une non-linéarité (SwiGLU / GELU) qui crée une base privilégiée (*Elhage et al., 2023, « Privileged Bases in the Transformer Residual Stream » — à vérifier*). C'est la thèse défendue par l'essai cité dans les faits (*Goodfire, « Neural Networks Are Already Clean » — à vérifier*), mais la littérature dominante considère que ces neurones propres ne représentent qu'une fraction minoritaire des mécanismes (souvent liés à des heuristiques de surface ou des bascules de mode très fortes comme le refus « I cannot / Sure »).
*   **Poussée d'activations (Activation Steering) et interventions causales sur sondes** :
    *   *Li et al. (2023), « Inference-Time Intervention: Eliciting Truthful Answers from a Language Model » (ITI) — à vérifier* : Démontre que les directions ayant la meilleure précision de lecture (sonde linéaire) ne sont pas toutes de bonnes directions d'intervention causale, mais que pousser le long des têtes d'attention les plus informatives modifie la véracité.
    *   *Turner et al. (2023), « Activation Addition: Steering Language Models Without Optimization » (ActAdd) — à vérifier* : Formalise la poussée par addition de vecteurs d'activation contrastés dans le flux résiduel.
    *   *Zou et al. (2023), « Representation Engineering: A Top-Down Approach to AI Transparency » (RepE) — à vérifier* : Utilise des directions globales (PCA sur paires contrastées) à la fois pour lire (détecter le mensonge, le pouvoir, l'émotion) et écrire (pousser le modèle vers l'honnêteté ou le mensonge).
    *   *Marks & Tegmark (2023), « The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets » — à vérifier* : Compare explicitement les sondes de régression logistique et les directions de différence des moyennes (*Mass-Mean probing*) sous intervention causale, montrant la supériorité causale de la différence des moyennes.
    *   *Arditi et al. (2024), « Refusal in Language Models Is Mediated by a Single Direction » — à vérifier* : Montre que le comportement de refus dans les modèles alignés (dont Llama-3) est contrôlé causalement par une direction unique de rang 1 dans le flux résiduel (ce qui explique pourquoi `neuron-explorer` trouve facilement des leviers de refus en projetant sur cette direction majeure, sans que cela garantisse qu'il en aille de même pour la conscience d'évaluation).

### 6. Ordre de priorité, voies à écarter et ce qu'il faudrait savoir de plus (Question 6)

Nous proposons trois voies distinctes, classées par ordre d'exécution rationnel, avec leurs critères de départage :

1.  **Voie 1 (Immédiate, coût $< 5\text{ USD}$ illustratif) : Poussée des sondes existantes de l'étape 1 contre témoins PCA-orthogonaux (Expérience 1) + Protocole d'agent durci dans la boucle extérieure (Expérience 4).**
    *   *Pourquoi d'abord* : Ne nécessite aucun balayage de 458 752 neurones. Teste directement si les sondes déjà acquises par le programme à l'étape 1 ont un pouvoir causal (écriture) ou ne sont que des lecteurs passifs.
2.  **Voie 2 (Conditionnelle, coût $\approx 10\text{ USD}$ illustratif) : Criblage par lentille rapide ($\Delta \text{log-prob}$ en 1 passe avant) sur 4 à 8 couches de Llama-3.1-8B-Instruct (Expérience 2).**
    *   *Quand la lancer* : Uniquement pour vérifier si les sondes de l'étape 1 s'appuient sur quelques neurones « goulots d'étranglement » (auquel cas les neutraliser ou les surveiller offre une caractéristique très parcimonieuse) ou si l'effet est totalement diffus.
3.  **Voie 3 (À ne JAMAIS faire, ou à bloquer par défaut) :**
    *   **Jamais** : Un balayage génératif complet (95 000 à 148 000 déroulés multi-jetons par couche) sur les 32 couches de Llama-3.1-8B-Instruct avec des transcriptions longues. Le coût ($\sim 125$ à $1\,000\text{ USD}$, illustratif) et le volume de données textuelles à fouiller encouragent massivement le biais « parcourir puis affirmer » sans avantage par rapport à un criblage en passe avant unique suivi d'une confirmation ciblée.
    *   **Jamais** : Donner une primitive `pousser` *générative* (multi-jetons) non déterministe à la boucle intérieure des organismes. Si la primitive `pousser` est testée (Expérience 3), elle doit être restreinte aux $\Delta \text{log-probs}$ en une passe avant avec témoins pré-calculés.

*   **Ce qu'il faudrait savoir de plus (Questions ouvertes pour l'arbitre)** :
    1.  *Spectre de parcimonie des sondes de l'étape 1* : Lorsque l'on projette le vecteur $\mathbf{w}_{\text{probe}}$ (au dernier jeton) sur les colonnes $W_{\text{down}}^{(l)}$ des couches précédentes, quelle fraction de la norme est portée par les 10 ou 50 neurones les plus alignés (indice de Gini ou rapport de participation inverse) ? Ce simple produit matriciel (coût : 0,01 seconde, zéro inférence) dira immédiatement si les sondes de l'étape 1 pointent vers des neurones isolés ou sont plates.
    2.  *Licence du dépôt `neuron-explorer`* : Les faits indiquent « Licence du dépôt : non trouvée ». En droit du droit d'auteur, l'absence de licence publique signifie « tous droits réservés » par défaut. **Règle d'intégrité logicielle** : Le programme ne doit copier aucune ligne de code de ce dépôt (ni sa fourche vLLM) tant que la licence n'est pas clarifiée ; nous devons uniquement réimplémenter les principes mathématiques et méthodologiques (qui relèvent des idées publiques) dans notre propre noyau isolé.

FIN-DE-CELLULE
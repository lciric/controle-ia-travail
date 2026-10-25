### État des pièces transmises
Le bloc FAITS ne contient aucun fait empirique par décision explicite de l'arbitre (statut : RAPPORTÉ).

---

### (a) Ce que la question suppose sans que ce soit établi

La question repose sur six postulats non démontrés dans les faits transmis. Chacun porte le statut d'**HYPOTHÈSE** :

1. **H_P1 (Surpassement structurel — HYPOTHÈSE)** : À budget de jetons et de calcul d'inférence constant, une topologie multi-agents découverte par recherche générative obtient un score de généralisation hors-distribution (sur des familles de tâches de classification jamais vues) supérieur à celui d'un agent unique ou d'un ensemble plat (vote majoritaire simple).
2. **H_P2 (Navigabilité du paysage de performance — HYPOTHÈSE)** : L'espace discret-continu des programmes et topologies d'agents possède une corrélation locale suffisante pour qu'un opérateur de réécriture guidé par un score scalaire sur un jeu de développement ($D_{\text{dev}}$) fasse mieux qu'un échantillonnage aléatoire avec sélection du meilleur (*Best-of-$N$*).
3. **H_P3 (Transférabilité des sondes auto-conçues — HYPOTHÈSE)** : Les activations résiduelles d'un modèle à poids ouverts de 8 milliards de paramètres ($8\text{B}$) contiennent des représentations linéaires ou faiblement non linéaires généralisables à de nouvelles familles de tâches, et un concepteur automatique peut synthétiser une fonction de perte et un jeu de données d'entraînement permettant de les extraire sans sur-ajustement immédiat.
4. **H_P4 (Stabilité de l'auto-récompense LoRA — HYPOTHÈSE)** : Un adaptateur de faible rang (LoRA) affiné par apprentissage par renforcement (RL) sous une fonction de récompense écrite par le système lui-même améliore la performance sur les tâches cibles sans provoquer un effondrement de la distribution de sortie ou un contournement de la récompense (*reward hacking*).
5. **H_P5 (Décomposabilité du mérite inter- et intra-générationnel — HYPOTHÈSE)** : Face à une récompense scalaire globale en fin de génération, il est possible d'attribuer le crédit (mérite) aux composants internes (agents, sondes, LoRA, format de mémoire) avec un rapport signal-bruit suffisant pour guider les générations suivantes.
6. **H_P6 (Invariance de la généralisation — HYPOTHÈSE)** : Les gains accumulés de génération en génération sur une suite de familles d'entraînement/développement ($\mathcal{F}_{\text{train}}$) se transfèrent positivement à des familles tenues à l'écart ($\mathcal{F}_{\text{test}}$), plutôt que d'encoder des heuristiques spécifiques à $\mathcal{F}_{\text{train}}$.

---

### (b) Formalisation, conception et expériences décisives (Points 1, 2, 5)

#### 1. Formalisation de l'apprentissage de génération en génération (Point 1)

On modélise l'évolution sur un horizon de $G$ générations comme un processus de décision markovien de méta-niveau (Méta-MDP) :
*   **Espace d'états / de recherche ($\mathcal{S}$)** : Un système à la génération $g$ est un n-uplet $S_g = (\mathcal{G}_g, \Pi_g, \mathcal{M}_g, \Theta_g, B_g)$ où :
    *   $\mathcal{G}_g = (V_g, E_g)$ est un graphe orienté (DAG ou avec cycles bornés) définissant la topologie des échanges et la règle d'agrégation finale ;
    *   $\Pi_g = \{(\text{prompt}_v, \text{modèle}_v)\}_{v \in V_g}$ est la composition (rôles et modèles affectés à chaque nœud) ;
    *   $\mathcal{M}_g \in \Sigma^*$ est la mémoire textuelle ou structurée transmise de $g-1$ à $g$ (taille bornée par $|M_{\max}|$ jetons) ;
    *   $\Theta_g = (\theta_{\text{probe}, g}, \theta_{\text{LoRA}, g})$ regroupe les poids continus des instruments appris par gradient ;
    *   $B_g \in \Delta^{|V_g|}$ est le vecteur d'allocation du budget de calcul par nœud ($\sum_v B_{g,v} \le B_{\max}$).
*   **Acteur (Qui apprend ?)** : Trois régimes distincts s'opposent :
    1.  *Concepteur figé* : Un modèle de langue aux poids gelés $\Psi_0$ agit par apprentissage en contexte sur l'historique des générations $(S_{1:g}, R_{1:g})$. Ce qui est appris : le programme $(\mathcal{G}_g, \Pi_g)$, la mémoire $\mathcal{M}_g$ et le code d'entraînement produisant $\Theta_g$.
    2.  *Concepteur entraîné* : La politique de conception $\Psi_\phi$ voit ses propres poids $\phi$ mis à jour (par RL ou affinage supervisé avec rejet) entre les méta-épisodes.
    3.  *Système auto-référentiel* : Un sous-graphe de $S_g$ est dédié à l'écriture de $S_{g+1}$ (pas de séparation entre système et concepteur).
*   **Ce qui reste figé** : Les poids de base du modèle $8\text{B}$, l'évaluateur externe qui calcule le score sur $D_{\text{dev}}$, le budget maximal $B_{\max}$ par tâche, et l'interpréteur de code sécurisé.
*   **Signal ($R_g$)** : Le score scalaire retourné sur $D_{\text{dev}}$ (ex. : exactitude équilibrée ou opposé de l'entropie croisée), pénalisé par le coût : $R_g = \text{Score}(S_g, D_{\text{dev}}) - \lambda \cdot \text{Coût}(S_g)$.
*   **Répartition du mérite (Attribution du crédit)** :
    *   *Intra-génération (entre éléments)* : Estimation par valeur de Shapley tronquée (ablation ou remplacement d'un nœud $v \in V_g$ par un appel neutre sur un sous-échantillon de $D_{\text{dev}}$) ou par différence contrefactuelle $\Delta_v = R(S_g) - R(S_g \setminus \{v\})$.
    *   *Inter-générations* : Sur l'arbre des modifications génératives, le mérite d'une mutation à l'étape $g$ est évalué par l'avantage temporel TD($\lambda$) ou par la valeur maximale atteinte dans sa descendance à l'horizon $G$ : $V(S_g) = \max_{g' \in \text{desc}(g)} R_{g'} - R_{g-1}$.

#### 2. Conception des instruments par gradient (Point 2)

*   **Instrument (A) — Sondes sur activations du modèle $8\text{B}$** :
    *   *Architecture* : Classifieur linéaire régularisé $f_W(h) = \sigma(W h + b)$, sonde d'attention (pondération apprise sur la séquence des jetons $h_{1:T}$), ou perceptron multicouche (MLP) à 1 couche cachée avec goulot d'étranglement ($d_{\text{bottleneck}} = 64$, illustratif).
    *   *Couches lues* : Couches intermédiaires à tardives (typiquement entre $50\%$ et $85\%$ de la profondeur, soit les couches 16 à 28 sur un modèle de 32 couches — illustratif), ou combinaison convexe apprise des couches (pondération scalaire type ELMo).
    *   *Pertes* : Entropie croisée avec pénalité $\ell_1/\ell_2$ (Lasso/Ridge) pour forcer la parcimonie, perte contrastée supervisée (SupCon), ou perte de marge (Hinge loss).
    *   *Données* : Paires (texte, étiquette vraie) issues de $D_{\text{train}}$, ou paires (texte, trace de raisonnement, succès/échec de l'agent) générées par le système aux générations précédentes.
    *   *Apport au système* : Détection rapide à coût nul (sans génération de jetons) de la difficulté de la tâche (routage), vérification de la cohérence interne (détection de tromperie ou d'incertitude), ou classifieur d'appoint dans l'agrégation finale.
*   **Instrument (B) — Adaptateur LoRA affiné par RL** :
    *   *Récompenses* : (i) *Binaire* (exactitude exacte sur $D_{\text{train}}$) — simple mais sujette à l'exploitation si le raisonnement intermédiaire est faux ; (ii) *Règle de score propre* (score de Brier ou log-probabilité sur la verbalisation d'une confiance $p \in [0,1]$) — force la calibration ; (iii) *Collective / Marginale* (récompense égale au gain marginal du système global lorsque la sortie du LoRA est injectée dans le graphe $\mathcal{G}_g$ par rapport à sa moyenne de groupe).
    *   *Algorithmes* : GRPO (*Group Relative Policy Optimization*, qui élimine le besoin d'un réseau critique en normalisant la récompense sur $K$ tirages par tâche), RLOO (*REINFORCE Leave-One-Out*), ou DPO (*Direct Preference Optimization*) itératif sur paires générées.
    *   *Données* : Milliers de tâches issues de $\mathcal{F}_{\text{train}}$, filtrées dynamiquement pour ne retenir que les tâches à variance non nulle (où le taux de succès sur $K$ tirages est compris dans $]0, 1[$).
    *   *Apport au système* : Spécialisation d'un agent dans un rôle précis (ex. : extracteur de caractéristiques, critique calibré, ou agrégateur robuste) que le prompt seul ne parvient pas à stabiliser sur un modèle $8\text{B}$.

#### 3. Généralisation et surveillance des dérives (Point 5)

*   **Protocole de généralisation** : Partition stricte au niveau des *familles* de tâches : $\mathcal{F} = \mathcal{F}_{\text{train}} \sqcup \mathcal{F}_{\text{val}} \sqcup \mathcal{F}_{\text{test}}$. À chaque génération $g$, les instruments $\Theta_g$ s'entraînent sur $D_{\text{train}} \sim \mathcal{F}_{\text{train}}$, et le concepteur reçoit le score sur $D_{\text{dev}} \sim \mathcal{F}_{\text{train}}$ (avec une fraction sur $\mathcal{F}_{\text{val}}$ si l'on teste la méta-validation). $\mathcal{F}_{\text{test}}$ n'est évalué qu'une seule fois à $g=G$.
*   **Bras apparié gelé** : Un système à budget de jetons et de calcul d'entraînement strictement identique, où le concepteur tire $G$ configurations indépendamment (sans mémoire inter-générationnelle ni mise à jour conditionnelle au score précédent) ou utilise une topologie fixe (vote majoritaire + LoRA standard affiné par entropie croisée sur $D_{\text{train}}$).
*   **Mesures des quatre dérives pendant l'apprentissage** :
    1.  *Effondrement de la diversité des rôles* : Calculer la divergence de Jensen-Shannon moyenne entre les distributions de prédictions des agents $\frac{2}{|V|(|V|-1)} \sum_{u < v} \text{JSD}(P_u \| P_v)$ sur $D_{\text{dev}}$, ainsi que la similarité cosinus des représentations des prompts système. Une baisse sous un seuil $\tau_{\text{div}} = 0,05$ bits (illustratif) signale un effondrement (clonage d'agents).
    2.  *Sur-ajustement au jeu de développement* : Maintenir un sous-ensemble caché $D_{\text{holdout}} \sim \mathcal{F}_{\text{train}}$ (même distribution que $D_{\text{dev}}$, mais son score n'est jamais communiqué au concepteur). Suivre l'écart $\Delta_{\text{gen}}(g) = \text{Score}(S_g, D_{\text{dev}}) - \text{Score}(S_g, D_{\text{holdout}})$ par rapport à la borne de concentration de Hoeffding $\sqrt{\frac{\ln(2G/\delta)}{2|D_{\text{dev}}|}}$.
    3.  *Exploitation d'une faiblesse du score (Goodhart)* : Injecter dans $D_{\text{dev}}$ $10\%$ (illustratif) de tâches « canaris » dont les étiquettes sont inversées ou dont le format comporte un biais superficiel corrélé artificiellement sur un petit lot, et mesurer l'écart entre le score optimisé et un score d'audit orthogonal (ex. : score de Brier vs exactitude brute).
    4.  *Baisse des signalements aux humains (abstention/escalade)* : Introduire dans l'espace d'action une option d'abstention/signalement (coût fixe $c_{\text{esc}}$) et injecter des tâches intrinsèquement ambiguës ou hors-domaine (étiquettes aléatoires $\mathcal{U}\{0,1\}$). Mesurer le taux de signalement $T_{\text{esc}}(g)$ sur ces tâches impossibles. Sous une récompense collective purement axée sur l'exactitude sans pénalité lourde d'erreur confiante, une chute de $T_{\text{esc}}(g)$ vers $0$ mesure la dérive de dissimulation.

---

#### 4. Six expériences décisives en inférence forte (H_A contre H_B)

**Expérience E1 — Accumulation générative contre échantillonnage aléatoire à budget égal**
*   **$H_A$ (Apprentissage cumulatif)** : Le guidage séquentiel de génération en génération ($g=1 \dots G$) avec mémoire et sélection permet de découvrir des structures $S_G$ plus performantes sur $\mathcal{F}_{\text{test}}$ qu'une recherche aléatoire non guidée.
*   **$H_B$ (Illusion de recherche)** : Le paysage de conception est trop discontinu ; les gains observés proviennent uniquement de l'exploration du volume d'échantillons (équivalent à un tirage aléatoire *Best-of-$G$*).
*   **Protocole et contrôle négatif** : Comparer le système évolutif sur $G=30$ générations (illustratif) au contrôle négatif *Best-of-$30$* où le même concepteur génère 30 systèmes indépendamment ($g=1$ répété 30 fois sans retour de score ni mémoire), seul le meilleur sur $D_{\text{dev}}$ étant retenu à la fin. Budget de jetons et d'entraînement d'instruments strictement égalisé.
*   **Métrique et seuil** : Différence d'exactitude macro-moyennée $\Delta \text{Acc}$ sur $\mathcal{F}_{\text{test}}$ (sur 10 graines aléatoires d'initialisation, illustratif). Seuil : $\Delta \text{Acc} \ge +2,5$ points de pourcentage (illustratif) avec $p < 0,01$ (test de permutation apparié).
*   **Falsification** : Si $\Delta \text{Acc} < +2,5\%$ ou non significatif, $H_A$ est falsifiée (la réécriture itérative est inutile). Si $\Delta \text{Acc} \ge +2,5\%$ avec $p < 0,01$, $H_B$ est falsifiée.

**Expérience E2 — Attribution contrefactuelle du mérite contre récompense globale scalaire**
*   **$H_A$ (Nécessité de la décomposition du crédit)** : Fournir au concepteur le vecteur des contributions marginales $\Delta_v$ de chaque agent/instrument accélère la convergence et élève le plafond sur $\mathcal{F}_{\text{test}}$ par rapport au seul score scalaire global $R_g$.
*   **$H_B$ (Suffisance du score global)** : Le concepteur infère les défauts structurels à partir des traces d'exécution brutes et du score global $R_g$ ; le calcul explicite des valeurs de Shapley/ablations gaspille le budget d'évaluation.
*   **Protocole et contrôle négatif** : Bras A : $80\%$ du budget d'évaluation sert à scorer $D_{\text{dev}}$, $20\%$ sert à calculer les ablations par nœud $\Delta_v$ communiquées au concepteur (illustratif). Bras B (contrôle négatif) : $100\%$ du budget d'évaluation sert à scorer $D_{\text{dev}}$ (jeu plus grand de $25\%$), seul le scalaire $R_g$ est transmis.
*   **Métrique et seuil** : Aire sous la courbe d'apprentissage (AUC du score sur $D_{\text{holdout}}$ de $g=1$ à $G$) et score final sur $\mathcal{F}_{\text{test}}$. Seuil : gain de $+2,0\%$ (illustratif) sur $\mathcal{F}_{\text{test}}$ en faveur du Bras A.
*   **Falsification** : Un gain $\ge +2,0\%$ du Bras A falsifie $H_B$ ; un score du Bras B supérieur ou à moins de $2,0\%$ du Bras A falsifie $H_A$.

**Expérience E3 — Sondes auto-conçues (A) contre heuristiques sur les log-probabilités de sortie**
*   **$H_A$ (Gain d'information interne)** : Les sondes entraînées sur les activations cachées du modèle $8\text{B}$ selon la perte et l'architecture choisies par le concepteur captent un signal de vérité/incertitude inaccessible dans les logits de la couche de sortie.
*   **$H_B$ (Redondance des sondes)** : Les sondes auto-conçues ne font que réapprendre bruyamment l'entropie prédictive des jetons de sortie ou sur-ajustent $D_{\text{train}}$.
*   **Protocole et contrôle négatif** : Remplacer dans le système final $S_G$ toutes les sondes (A) par un classifieur logistique fixe à 3 variables calculées uniquement sur les logits de sortie du modèle $8\text{B}$ (entropie de Shannon du premier jeton de réponse, marge entre les 2 premiers logits, log-probabilité moyenne de la séquence) — contrôle négatif mécanique.
*   **Métrique et seuil** : Différence d'AUROC des classifieurs d'incertitude et différence d'exactitude du système complet sur $\mathcal{F}_{\text{test}}$. Seuil : $\Delta \text{AUROC} \ge +0,04$ et $\Delta \text{Acc}_{\text{système}} \ge +1,5\%$ (illustratifs).
*   **Falsification** : Si le contrôle sur les logits de sortie fait aussi bien (écart $< 0,04$ AUROC ou $< 1,5\%$ Acc), $H_A$ est falsifiée. Sinon, $H_B$ est falsifiée.

**Expérience E4 — LoRA par RL à récompense auto-écrite (B) contre LoRA supervisé (SFT) et récompense binaire fixe**
*   **$H_A$ (Supériorité de la récompense auto-conçue)** : Une fonction de récompense composite (ex. : règle de score propre ou récompense collective) écrite par le concepteur pour entraîner le LoRA par RL produit un agent mieux intégré au graphe $\mathcal{G}_g$ qu'une récompense binaire d'exactitude fixe ou qu'un affinage supervisé (SFT).
*   **$H_B$ (Dérive d'auto-récompense)** : L'auto-écriture de la récompense induit du *reward hacking* ou une variance d'optimisation inférieure à un SFT par entropie croisée ou un RL à récompense binaire exacte fixe sur $D_{\text{train}}$.
*   **Protocole et contrôle négatif** : À topologie $\mathcal{G}_g$ fixée, comparer trois variantes d'entraînement de l'instrument (B) à nombre d'étapes de gradient égal : (1) RL avec récompense écrite par le concepteur ; (2) Contrôle négatif 1 : RL (GRPO) avec récompense binaire fixe $\mathbb{I}(\hat{y} = y)$ ; (3) Contrôle négatif 2 : SFT par rejet (*Rejection Sampling Fine-Tuning*) sur les traces correctes.
*   **Métrique et seuil** : Exactitude sur $\mathcal{F}_{\text{test}}$ et erreur de calibration attendue (ECE). Seuil : $\Delta \text{Acc} \ge +2,0\%$ et $\Delta \text{ECE} \le -0,03$ (illustratifs) pour (1) contre le meilleur des contrôles (2) et (3).
*   **Falsification** : Si (2) ou (3) égale ou bat (1) selon ce seuil, $H_A$ est falsifiée. Si (1) franchit les deux seuils, $H_B$ est falsifiée.

**Expérience E5 — Généralisation hors-famille contre mémorisation structurelle**
*   **$H_A$ (Apprentissage d'un méta-algorithme de coopération)** : L'évolution sur $\mathcal{F}_{\text{train}}$ découvre une division du travail (vérification, débat, routage, agrégation calibrée) qui se transfère aux familles disjointes $\mathcal{F}_{\text{test}}$.
*   **$H_B$ (Sur-ajustement structurel aux familles vues)** : La structure $S_G$ encode des biais spécifiques aux distributions d'étiquettes, longueurs de textes et pièges de $\mathcal{F}_{\text{train}}$, dégradant sa performance dès qu'on change de famille de tâches.
*   **Protocole et contrôle négatif** : Évaluer la trajectoire $S_1, \dots, S_G$ conjointement sur $D_{\text{holdout}} \sim \mathcal{F}_{\text{train}}$ et sur $\mathcal{F}_{\text{test}}$ (ex. : entraînement sur classification de sentiments, détection de sophismes et inférence textuelle ; test sur classification juridique, diagnostic clinique textuel et détection de code vulnérable — illustratif). Contrôle négatif : la structure initiale non entraînée $S_0$ (ensemble par vote majoritaire de 5 agents, illustratif) à budget d'inférence égalisé.
*   **Métrique et seuil** : Ratio de transfert de gain $\rho = \frac{\text{Score}(S_G, \mathcal{F}_{\text{test}}) - \text{Score}(S_0, \mathcal{F}_{\text{test}})}{\text{Score}(S_G, D_{\text{holdout}}) - \text{Score}(S_0, D_{\text{holdout}})}$. Seuil : $\rho \ge 0,50$ avec un gain absolu sur $\mathcal{F}_{\text{test}} \ge +3,0\%$ (illustratifs).
*   **Falsification** : Si $\rho < 0,50$ (le gain s'effondre de plus de moitié hors famille) ou gain absolu $< 3,0\%$, $H_A$ est falsifiée. Si $\rho \ge 0,50$ et gain $\ge 3,0\%$, $H_B$ est falsifiée.

**Expérience E6 — Préservation des signalements humains sous récompense de règle de score propre contre récompense collective brute**
*   **$H_A$ (Alignement épistémique par règle de score propre)** : Imposer une règle de score strictement propre (log-score ou Brier avec option d'abstention à coût fixe) au niveau de l'agrégateur maintient le taux de signalement aux humains sur les cas ambigus au fil des générations.
*   **$H_B$ (Érosion inévitable de l'escalade)** : La pression de sélection inter-générationnelle pousse le système à parier systématiquement plutôt qu'à s'abstenir pour maximiser l'espérance empirique sur un échantillon fini $D_{\text{dev}}$, faisant chuter les signalements quel que soit le format de récompense.
*   **Protocole et contrôle négatif** : Injecter $15\%$ (illustratif) de cas indécidables (étiquettes bruitées à $50\%$) dans $D_{\text{dev}}$ et $\mathcal{F}_{\text{test}}$. Comparer l'évolution sur $G$ générations sous (1) une récompense basée sur le score de Brier avec abstention rémunérée au niveau de l'entropie maximale, contre (2) un contrôle négatif utilisant l'exactitude collective standard où une abstention vaut $0,5$ point et une bonne réponse $1$ point.
*   **Métrique et seuil** : Rappel de signalement (taux d'abstention sur les $15\%$ de cas indécidables) et taux de fausses alertes (abstention sur les cas clairs où le modèle de base a une exactitude $> 90\%$) à la génération $G$. Seuil : Rappel $\ge 0,70$ pour un taux de fausses alertes $\le 0,10$ (illustratifs).
*   **Falsification** : Si le régime (1) tombe sous un rappel de $0,70$ ou dépasse $0,10$ de fausses alertes à $g=G$, $H_A$ est falsifiée. Si (1) respecte le seuil alors que (2) s'effondre sous un rappel de $0,30$ (illustratif), $H_B$ est falsifiée.

---

### (c) Mesure minimale de fonctionnement des instruments nommés

Pour chaque instrument mentionné dans la question, le tableau suivant définit la mesure minimale prouvant qu'il fonctionne avant ou pendant son intégration, son taux de détection (TPR) et de fausses alertes (FPR) exigés (tous les chiffres sont **illustratifs**), les cas honnêtes appariés et la vérification mécanique triviale à battre :

| Instrument | Tâche de mesure minimale (Isolée) | Cas honnêtes appariés (Contrôle de non-dégénérescence) | Vérification mécanique à battre (Baseline triviale) | Seuils minimaux (TPR / FPR ou Gain — illustratifs) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Sonde (A) sur modèle $8\text{B}$** | Prédire si la réponse d'un agent $8\text{B}$ sur une tâche hors-entraînement est fausse ou incertaine à partir du flux résiduel $h_l$. | Paires de tâches de même longueur, même domaine et même étiquette cible, l'une résolue correctement par l'agent, l'autre échouée (appariement par score de propension sur la longueur et la perplexité). | Classifieur logistique sur : (1) l'entropie du logit de sortie de l'agent, (2) la perplexité du texte d'entrée, (3) la longueur en jetons. | **TPR $\ge 0,75$** de détection d'erreur de l'agent pour un **FPR $\le 0,15$** sur les réponses justes ; gain de **$\ge +0,05$ AUROC** sur la vérification mécanique. |
| **2. Adaptateur LoRA par RL (B)** | Améliorer la classification et la calibration d'un agent $8\text{B}$ appelé seul sur $\mathcal{F}_{\text{val}}$ par rapport au modèle $8\text{B}$ de base. | Tâches de $\mathcal{F}_{\text{val}}$ où le modèle de base avec un prompt *few-shot* optimisé (5 exemples) est évalué au même budget de jetons de génération. | Modèle $8\text{B}$ de base avec échantillonnage de $K=4$ réponses et vote majoritaire (auto-cohérence simple sans modification de poids), ou LoRA entraîné par SFT classique. | Gain d'exactitude **$\ge +2,5\%$** sur le modèle de base ; réduction de l'ECE de **$\ge 25\%$** ; détection des exemples hors-distribution avec **TPR $\ge 0,70$ / FPR $\le 0,15$** via la confiance verbalisée. |
| **3. Règle d'agrégation apprise** | Identifier la bonne étiquette lorsque la majorité des agents se trompe mais qu'une minorité (1 ou 2 agents) détient un argument valide. | Cas d'accord majoritaire correct appariés (où la majorité a raison face à un agent dissident bruité) pour vérifier que l'agrégateur n'inverse pas systématiquement le vote. | Vote majoritaire pondéré mécaniquement par la confiance moyenne (log-probabilité) de chaque agent (pondération de Platt statique). | **TPR $\ge 0,40$** de sauvetage des minorités correctes (contre $0,00$ pour le vote majoritaire pur) pour un **FPR $\le 0,03$** (dégradation des majorités correctes) ; bat le vote pondéré par logits de **$\ge +1,5\%$** d'exactitude globale. |
| **4. Mémoire inter-générationnelle ($\mathcal{M}_g$)** | Éviter de ré-explorer à la génération $g$ une modification structurelle ou d'hyperparamètre qui a dégradé le score aux générations $1 \dots g-1$. | Propositions de mutations structurelles syntaxiquement proches mais fonctionnellement nouvelles et bénéfiques (qui ne doivent pas être bloquées par la mémoire). | Filtre mécanique par hachage syntaxique (distance d'édition de Levenshtein ou de Jaccard sur les trigrammes du code/graphe $\mathcal{G}_g$) bloquant les quasi-doublons exacts. | **TPR $\ge 0,85$** de rejet des motifs d'échec sémantiquement équivalents déjà testés, pour un **FPR $\le 0,10$** de rejet de mutations bénéfiques inédites ; gain d'efficacité d'échantillonnage de **$\ge +20\%$** sur le filtre de Jaccard. |
| **5. Concepteur évolutif ($\Psi$)** | Proposer à l'étape $g+1$ un système $S_{g+1}$ tel que $\text{Score}(S_{g+1}, D_{\text{holdout}}) > \text{Score}(S_g, D_{\text{holdout}})$. | Réécritures neutres (refactorisation du code ou permutation des identifiants d'agents sans changement fonctionnel) qui doivent donner une variation de score nulle. | Recherche locale mécanique par grille aléatoire (*Random Search* / *Hill-Climbing* par mutation aléatoire d'un hyperparamètre ou d'un prompt via un gabarit fixe). | Taux de mutations véritablement améliorantes sur $D_{\text{holdout}}$ (**TPR**) **$\ge 0,30$** avec un taux de fausses améliorations (gain sur $D_{\text{dev}}$ mais baisse sur $D_{\text{holdout}}$, **FPR**) **$\le 0,10$** ; bat le *Hill-Climbing* mécanique d'un facteur **$\ge 1,5\times$** sur le taux de succès. |

---

### (d) Ancrage matériel : voies moins chères et chiffrage de la voie chère (Points 3 et 4)

#### Modèles ouverts d'ancrage
Pour garantir la reproductibilité et l'accès aux activations internes comme aux poids :
*   **Modèle de base $8\text{B}$ pour les agents et les instruments (A) et (B)** : `Llama-3.1-8B-Instruct` ou `Qwen-2.5-7B-Instruct` (poids ouverts, 32 ou 28 couches, dimension résiduelle $d_{\text{model}} = 4096$ ou $3584$).
*   **Modèle concepteur à poids ouverts (pour la voie chère ou locale)** : `Qwen-2.5-72B-Instruct` ou `Llama-3.3-70B-Instruct` (poids ouverts, affinable par LoRA/QLoRA sur nœud multi-GPU).

#### Point 3 — Six voies moins chères (différentes entre elles)

Tous les coûts et volumes de calcul ci-dessous sont **illustratifs** (basés sur un tarif moyen de location cloud de $2,50\text{ \$/heure}$ par carte GPU H100 80 Go).

1.  **Voie R1 — Évaluation multi-fidélité par réduction successive (*Successive Halving* / Hyperband sur les générations)** :
    *   *Principe* : Au lieu d'évaluer chaque candidat $S_g$ sur l'intégralité de $D_{\text{dev}}$ ($2\,000$ tâches) et d'entraîner le LoRA sur $5\,000$ tâches, $80\%$ des candidats sont filtrés sur un micro-jeu de $100$ tâches stratifiées et $200$ pas de LoRA ; seuls les $20\%$ survivants passent à l'échelle complète.
    *   *Ordre de grandeur du coût* : **$150\text{ \$}$ à $400\text{ \$}$** ($60$ à $160$ heures-GPU H100 — illustratif).
    *   *Ce qu'on y perd* : Élimination prématurée des structures ou récompenses RL à démarrage lent (qui ont besoin de nombreux pas de gradient LoRA pour émerger).
2.  **Voie R2 — Substitution des agents de frontière par un unique modèle $8\text{B}$ partagé à multi-adaptateurs LoRA** :
    *   *Principe* : Aucun appel à des modèles propriétaires de frontière ; tous les rôles du graphe $\mathcal{G}_g$ sont servis par la même instance `Llama-3.1-8B` en mémoire GPU (via vLLM/SGLang avec changement dynamique d'adaptateur LoRA par requête et mise en cache des préfixes KV).
    *   *Ordre de grandeur du coût* : **$80\text{ \$}$ à $200\text{ \$}$** ($30$ à $80$ heures-GPU H100, coût d'API nul — illustratif).
    *   *Ce qu'on y perd* : Plafond de raisonnement complexe et de synthèse de code plus bas qu'avec des modèles de frontière ($> 100\text{B}$ paramètres) ; risque de corrélation des erreurs entre agents partageant le même tronc pré-entraîné.
3.  **Voie R3 — Optimisation bayésienne sur un graphe maximal pré-câblé (*Supernet* continu)** :
    *   *Principe* : Au lieu de laisser un concepteur réécrire du code libre, on fige un graphe orienté acyclique maximal de $N=8$ nœuds (illustratif) contenant déjà des sondes et un LoRA générique, et l'on n'apprend que les poids continus des arêtes $w_{ij} \in [0,1]$, le choix discret du modèle par nœud et 5 hyperparamètres d'entraînement via un processus gaussien ou CMA-ES.
    *   *Ordre de grandeur du coût* : **$50\text{ \$}$ à $120\text{ \$}$** ($20$ à $50$ heures-GPU H100 — illustratif).
    *   *Ce qu'on y perd* : Impossibilité d'inventer de nouvelles fonctions de perte pour les sondes (A), de nouvelles formules de récompense pour le LoRA (B), ou des boucles algorithmiques conditionnelles non prévues dans le graphe maximal.
4.  **Voie R4 — Pré-calcul hors-ligne d'une banque de traces et d'activations figées** :
    *   *Principe* : On exécute une seule fois un ensemble de modèles de base sur $D_{\text{train}}$ et $D_{\text{dev}}$ en sauvegardant sur disque les réponses textuelles, les logits et les vecteurs d'activations des couches 16, 20, 24, 28 (en `float16`). Les générations suivantes entraînent les sondes (A) et testent les règles d'agrégation et de routage uniquement par lecture matricielle sur ce cache, sans ré-exécuter le modèle $8\text{B}$.
    *   *Ordre de grandeur du coût* : **$20\text{ \$}$ à $50\text{ \$}$** ($8$ à $20$ heures-GPU H100 + $500\text{ Go}$ de stockage SSD — illustratif).
    *   *Ce qu'on y perd* : Impossible d'entraîner le LoRA (B) en interaction dynamique avec le graphe (puisque modifier les poids LoRA invalide le cache des activations et des textes générés) ni de modifier les prompts des agents en amont.
5.  **Voie R5 — Remplacement du RL de l'instrument (B) par un affinage supervisé par rejet (*Rejection Sampling SFT*) ou DPO hors-ligne** :
    *   *Principe* : Au lieu d'entraîner le LoRA (B) par RL en ligne (qui requiert de générer $K$ trajectoires par tâche à chaque étape de gradient), le concepteur écrit une fonction de score qui filtre une banque statique de réponses déjà générées pour garder les $10\%$ meilleures, sur lesquelles un simple SFT ou DPO est exécuté en 1 époque.
    *   *Ordre de grandeur du coût* : **$100\text{ \$}$ à $250\text{ \$}$** ($40$ à $100$ heures-GPU H100, réduisant d'un facteur $10\times$ le coût de l'instrument B — illustratif).
    *   *Ce qu'on y perd* : Le LoRA ne peut pas explorer des stratégies de réponse absentes de la distribution initiale du modèle $8\text{B}$ de base.
6.  **Voie R6 — Modèle de substitution (*Surrogate Model*) prédisant le score d'une génération avant exécution** :
    *   *Principe* : On entraîne un prédicteur léger (forêt aléatoire ou petit transformeur sur les caractéristiques du graphe $\mathcal{G}_g$, de la perte de la sonde et de la récompense LoRA) sur les 50 premières générations évaluées réellement. Ensuite, le concepteur génère $1\,000$ candidats par génération et n'exécute sur GPU que les $5$ meilleurs selon la borne supérieure de confiance (UCB) du prédicteur.
    *   *Ordre de grandeur du coût* : **$200\text{ \$}$ à $450\text{ \$}$** ($80$ à $180$ heures-GPU H100 — illustratif).
    *   *Ce qu'on y perd* : Si le modèle de substitution est mal calibré sur une innovation architecturale inédite, il la rejette à tort (biais conservateur).

---

#### Point 4 — Chiffrage détaillé de la voie chère

On chiffre ici la voie complète : un **concepteur à poids ouverts de $70\text{B}$ de paramètres** (`Llama-3.3-70B` ou `Qwen-2.5-72B`) **entraîné par renforcement (GRPO)**, où chaque épisode de RL du concepteur consiste à dérouler une trajectoire complète de $G = 10$ générations d'un système composé d'agents de frontière (par API ou grand modèle servi) et des instruments (A) et (B) entraînés par gradient sur le modèle $8\text{B}$ à chaque génération. Tous les chiffres ci-dessous sont **illustratifs** mais liés par un raisonnement arithmétique explicite.

1.  **Décomposition d'une seule génération (1 pas dans l'épisode)** :
    *   *Conception* : Le concepteur $70\text{B}$ lit l'historique et génère le code de la génération ($8\,000$ jetons d'entrée, $4\,000$ jetons de sortie) $\rightarrow \approx 0,02$ heure-GPU H100.
    *   *Entraînement de l'instrument (A) (Sonde)* : Extraction des activations du modèle $8\text{B}$ sur $5\,000$ tâches de $512$ jetons ($2,56 \times 10^6$ jetons) + entraînement du MLP/classifieur $\rightarrow \approx 0,15$ heure-GPU H100.
    *   *Entraînement de l'instrument (B) (LoRA par RL en ligne)* : $3\,000$ tâches $\times$ $K=4$ tirages GRPO de $512$ jetons générés par le modèle $8\text{B}$ ($6,14 \times 10^6$ jetons générés + passe arrière LoRA) $\rightarrow \approx 1,20$ heure-GPU H100.
    *   *Évaluation du système multi-agents sur $D_{\text{dev}}$* : $1\,000$ tâches de développement $\times$ $5$ appels d'agents par tâche en moyenne $\times$ $1\,000$ jetons (entrée + sortie) par appel $= 5 \times 10^6$ jetons par génération :
        *   Si les agents principaux sont servis par des modèles de frontière via API (au tarif moyen combiné de $5,00\text{ \$} / 10^6$ jetons — illustratif) : **$25,00\text{ \$}$ d'API** par génération.
        *   Les appels aux instruments locaux ($8\text{B}$ + sonde) sur $D_{\text{dev}}$ : $\approx 0,13$ heure-GPU H100.
    *   **Sous-total pour 1 génération** : **$1,50$ heure-GPU H100** (soit **$3,75\text{ \$}$** à $2,50\text{ \$/h}$) + **$25,00\text{ \$}$ d'API de frontière** = **$28,75\text{ \$}$ par génération**.

2.  **Coût d'un épisode complet ($G = 10$ générations séquentielles)** :
    *   Calcul GPU local (instruments A, B et inférence $8\text{B}$) : $10 \times 1,50 = \mathbf{15\text{ heures-GPU H100}}$ (**$37,50\text{ \$}$**).
    *   Appels aux agents de frontière : $10 \times 25,00\text{ \$} = \mathbf{250,00\text{ \$}}$.
    *   Mise à jour par gradient RL (GRPO) du concepteur $70\text{B}$ en fin d'épisode (sur la trajectoire de $10 \times 12\,000 = 120\,000$ jetons) : $\approx \mathbf{0,5\text{ heure-GPU H100}}$ (**$1,25\text{ \$}$**).
    *   **Coût total par épisode** : **$15,5$ heures-GPU H100 + $250\text{ \$}$ d'API $\approx 288,75\text{ \$}$ par épisode**.

3.  **Nombre d'épisodes nécessaires et total en ordre de grandeur** :
    *   Pour que l'apprentissage par renforcement (GRPO) stabilise la politique d'un concepteur $70\text{B}$ sur un horizon long à récompense bruitée, il faut de l'ordre de $125$ pas de mise à jour de politique avec un groupe de $M=8$ épisodes parallèles par pas, soit **$1\,000$ épisodes au total** (illustratif).
    *   **Calcul total sur carte graphique** : $1\,000 \times 15,5 = \mathbf{15\,500\text{ heures-GPU H100}}$ (soit environ $24$ jours continus sur un cluster de $32$ cartes H100 — illustratif), représentant **$\approx 38\,750\text{ \$}$** de calcul GPU.
    *   **Facture d'agents de frontière** : $1\,000 \times 250\text{ \$} = \mathbf{250\,000\text{ \$}}$.
    *   **Coût total de la voie chère** : **$\approx 288\,750\text{ \$}$** (ordre de grandeur : **$250\,000\text{ \$}$ à $350\,000\text{ \$}$** — illustratif).

4.  **Ce qui ferait baisser ce coût (leviers de réduction directe)** :
    *   *Levier 1 (Suppression des API de frontière pendant l'entraînement du concepteur)* : Remplacer les agents de frontière par un modèle ouvert `Qwen-2.5-72B` quantifié en FP8 servi localement sur H100 divise par $5$ le poste d'évaluation (économisant $\approx 200\,000\text{ \$}$ — illustratif), les agents de frontière n'étant appelés qu'en test final.
    *   *Levier 2 (Horizons courts par amorçage sur états intermédiaires)* : Au lieu de dérouler $G=10$ générations depuis $g=0$ à chaque épisode, entraîner le concepteur sur des transitions à $1$ pas ($S_g \to S_{g+1}$) échantillonnées depuis un tampon de rejeu (*Replay Buffer*), réduisant la durée d'un épisode d'un facteur $10\times$.
    *   *Levier 3 (Apprentissage hors-politique par DPO itératif du concepteur)* : Remplacer les $1\,000$ épisodes de RL en ligne par 3 rondes de DPO sur $200$ trajectoires générées (réduction d'un facteur $5\times$, ramenant le coût total sous les $50\,000\text{ \$}$ — illustratif).

---

### (e) Ce qui est connu : références citables (Point 6)

Conformément à la règle d'intégrité n° 3 et au point 6 de la question, toutes les références ci-dessous sont données avec auteurs, année et titre, sans identifiant arXiv, et portent la mention explicite « à vérifier » :

*   **Optimisation automatique d'architectures d'agents et de graphes de calcul** :
    *   Shengran Hu, Cong Lu, Jeff Clune (2024), *Automated Design of Agentic Systems* — référence à vérifier.
    *   Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, Zhiyuan Zhang, Keshav Santhanam, Sri Vardhamanan, Saiful Haq, Ashutosh Sharma, Thomas T. Joshi, Hanna Moazam, Heather Miller, Matei Zaharia, Christopher Potts (2023), *DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines* — référence à vérifier.
    *   Guibin Zhang, Yanwei Yue, Zhixun Li, Sukwon Yun, Guancheng Wan, Kun Wang, Dawei Cheng, Jeffrey Xu Yu, Tianlong Chen (2024), *GPTSwarm: Language Agents as Optimizable Graphs* — référence à vérifier.
    *   Mert Yuksekgonul, Federico Bianchi, Joseph Boen, Sheng Liu, Zhi Huang, Carlos Guestrin, James Zou (2024), *TextGrad: Automatic "Differentiation" via Text* — référence à vérifier.
*   **Coopération, débat multi-agents et agrégation** :
    *   Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, Igor Mordatch (2023), *Improving Factuality and Reasoning in Language Models through Multiagent Debate* — référence à vérifier.
    *   Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou (2023), *Self-Consistency Improves Chain of Thought Reasoning in Language Models* — référence à vérifier.
*   **Sondes linéaires sur activations internes (Instrument A)** :
    *   Guillaume Alain, Yoshua Bengio (2016), *Understanding intermediate layers using linear classifier probes* — référence à vérifier.
    *   Collin Burns, Haotian Ye, Dan Klein, Jacob Steinhardt (2023), *Discovering Latent Knowledge in Language Models Without Supervision* — référence à vérifier.
    *   Kenneth Li, Oam Patel, Fernanda Viégas, Hanspeter Pfister, Martin Wattenberg (2023), *Inference-Time Intervention: Eliciting Truthful Answers from a Language Model* — référence à vérifier.
    *   Amos Azaria, Tom Mitchell (2023), *The Internal State of an LLM Knows When It's Lying* — référence à vérifier.
*   **Adaptateurs de faible rang et RL pour modèles de langue (Instrument B)** :
    *   Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen (2021), *LoRA: Low-Rank Adaptation of Large Language Models* — référence à vérifier.
    *   Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y. K. Li, Y. Wu, Daya Guo (2024), *DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models* (introduisant GRPO) — référence à vérifier.
    *   Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, Chelsea Finn (2023), *Direct Preference Optimization: Your Language Model is Secretly a Reward Model* — référence à vérifier.
    *   Weizhe Yuan, Richard Yuanzhe Pang, Kyunghyun Cho, Sainbayar Sukhbaatar, Jing Xu, Jason Weston (2024), *Self-Rewarding Language Models* — référence à vérifier.
*   **Règles de score propres, calibration et exploitation des récompenses** :
    *   Tilmann Gneiting, Adrian E. Raftery (2007), *Strictly Proper Scoring Rules, Prediction, and Estimation* — référence à vérifier.
    *   Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger (2022), *Defining and Characterizing Reward Hacking* — référence à vérifier.

FIN-DE-CELLULE
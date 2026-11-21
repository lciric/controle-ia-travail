Voici mon analyse et mes recommandations, structurées selon l’ordre demandé. Je distingue systématiquement les résultats et méthodes **[Établis]** de mes **[Propositions]**.

---

### 1. Ce qu’un expert du domaine ferait ici, et qu’on ne demande pas

1. **Corriger le biais de conditionnement entre l’étalonnage et le contraste principal [Proposition] :**
   Votre contraste principal oppose le saboteur à *l’échec honnête* tâche par tâche, mais votre seuil à 1 % de fausses alertes (FPR) est défini sur *les épisodes honnêtes* (sans préciser s’il s’agit des seuls échecs ou de l'ensemble). Or, sous votre propre hypothèse, la sonde de réussite attendue (et toute sonde d’intention qui y est corrélée) place les échecs honnêtes dans la queue de distribution des épisodes honnêtes. **[Établi]** Si vous étalonnez un seuil à 1 % sur *tous* les épisodes honnêtes d’une tâche où le taux d’échec honnête est de 20 %, et que le score dépend de la difficulté perçue, le taux de fausses alertes *conditionnellement à l’échec honnête* peut monter à 5 % (1 % / 20 %). Un expert définit donc deux seuils distincts ou étalonne *conditionnellement à la valeur prédite au jalon*, sans quoi l’avantage apparent sur le contraste « saboteur vs échec honnête » est un artefact de déplacement de covariable (*covariate shift*).
2. **Supprimer les tranches de longueur en « blanchissant » la somme séquentielle [Établi + Proposition] :**
   Le découpage en tranches de longueur $T$ n'est nécessaire que parce que la somme brute $S_T = \sum_{t=1}^T s_t$ accumule une dérive $\mu T$ et une variance d’ordre $\mathcal{O}(T \cdot \tau_{\text{int}})$, où $\tau_{\text{int}}$ est le temps d’autocorrélation intégré des activations le long du raisonnement. Découper quelques centaines d’épisodes en tranches de longueur divise par le nombre de tranches un échantillon déjà insuffisant. Un expert remplace la somme brute par la somme des **innovations studentisées** $\tilde{z}_t = (s_t - \hat{\mathbb{E}}[s_t \mid \mathcal{F}_{t-1}]) / \hat{\sigma}_t$, ce qui transforme la trajectoire sous l’hypothèse nulle ($H_0$ : agent honnête) en une martingale à accroissements centrés réduits. La dépendance à la longueur $T$ est alors absorbée analytiquement (via la loi du logarithme itéré ou l’inégalité de Ville), ce qui permet de **regrouper (*pool*) tous les épisodes honnêtes** dans un unique lot d’étalonnage.
3. **Vérifier la fuite du déclencheur (*trigger leakage*) dans les activations [Établi] :**
   Si le saboteur est induit par une instruction système ou un indice dans le prompt, une sonde linéaire sur les couches intermédiaires détecte très facilement la signature lexicale ou attentionnelle de cette instruction dans le cache KV, avec une AUC proche de 1,0, mais s’effondre dès que le comportement de sabotage est intériorisé dans les poids (*fine-tuning* / organisme modèle, cf. Hubinger et al., *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training*, `arXiv:2401.05566`) ou que l’épreuve d’évasion modifie la formulation. Un expert impose que les activations soient lues uniquement sur des jetons où l’attention vers le prompt système est masquée ou projetée orthogonalement à la direction moyenne du prompt de sabotage.
4. **Exploiter l’écart entre vos bases 1 et 3 comme variable de contrôle gratuite [Proposition] :**
   Votre 3e base évalue l’état au même jalon avec *les seuls fichiers alors disponibles* (état markovien $x_t$, sans l’historique de pensée $h_t$), tandis que la sonde en direct lit l’historique complet $h_t$. La différence $D_t = V(h_t) - V(x_t)$ mesure exactement l’écart entre ce que l’agent sait de sa trajectoire interne et la qualité apparente des fichiers produits. Un saboteur qui prépare un bogue discret dégrade $V(h_t)$ (ou y encode son intention) *avant* que $V(x_t)$ ne chute visiblement.

---

### 2. Les données brutes qu’il utiliserait au départ (au lieu des seuls épisodes déjà résumés)

Remplacer 500 valeurs scalaires (un score par épisode) par la structure fine déjà payée ou quasi gratuite :

1. **Les transitions au niveau du pas et du jeton ($\Delta s_t = s_t - s_{t-1}$) dans vos quelques centaines d’épisodes [Établi] :**
   300 épisodes de 40 pas contiennent 12 000 transitions de pas et des centaines de milliers de jetons. C’est à cette échelle qu’on estime la matrice d’autocorrélation temporelle, la queue des innovations locales et la relation entre la sonde de valeur (`arXiv:2602.00986`) et la sonde d’intention.
2. **Des passes avant forcées (*teacher-forcing / prefill*) sur des traces publiques d’agents [Proposition] :**
   Ce qui coûte cher, c’est la génération autorégressive et l’exécution d’environnement (conteneurs, tests, appels d’API). Passer 10 000 traces d’agents existantes (issues de bancs d’essai publics comme SWE-bench, WebArena, ou les traces de raisonnement de MATH/PRM800K) en une seule passe avant (*prefill*) dans Llama-3.1-8B pour extraire les activations des couches cibles ne coûte que quelques heures d’un seul GPU. Cela fournit la distribution jointe de base des activations sur des trajectoires honnêtes longues.
3. **Les embranchements courts depuis les jalons existants (liés à vos bases 2 et 3) [Proposition] :**
   Puisque vous sauvegardez déjà les fichiers aux jalons (base 3) et utilisez un jumeau forcé sur le même début (base 2), vous disposez des états intermédiaires. Générer $K=10$ continuations honnêtes de 2 ou 3 pas seulement à partir des jalons où la sonde de valeur fluctue fortement coûte une fraction d’un épisode complet et permet d’estimer la variance conditionnelle locale $\text{Var}(s_{t+1} \mid x_t)$ sous $H_0$.
4. **Les logits et l’entropie prédictive du modèle à chaque jeton [Établi] :**
   Pour séparer l’incertitude épistémique (« l’agent honnête est perdu ») du sabotage (« l’agent connaît la bonne action mais choisit une action sous-optimale »), il faut conserver le rang et la log-probabilité de l’action choisie ainsi que l’entropie de la distribution de sortie à chaque pas, sans surcoût de calcul.

---

### 3. Les méthodes et outils précis qu’il emploierait (et ce que chacun suppose)

| Outil / Méthode | Usage précis dans votre problème | Ce que la méthode suppose |
| :--- | :--- | :--- |
| **Régression quantile conformalisée (CQR) sur résidus regroupés** **[Établi]** (Romano et al., *Conformalized Quantile Regression*, `arXiv:1905.03222`) | Ajuster une courbe souple (spline monotone ou modèle linéaire) du quantile à 95 % du score en fonction de la longueur $L$ et de la valeur initiale $V_0$ : $\hat{q}_{0.95}(L, V_0)$. Puis calculer le quantile conforme à 99 % sur les **résidus standardisés regroupés** de tous les $N$ épisodes honnêtes ($N \approx 300\text{--}500$), sans découper en tranches. | **Échangeabilité** des épisodes honnêtes d’étalonnage et de test ; l’hétéroscédasticité selon la longueur $L$ est correctement capturée par la fonction d’échelle locale. |
| **Garanties exactes en échantillon fini (Loi Bêta des quantiles conformes)** **[Établi]** (Vovk, Gammerman, Shafer, *Algorithmic Learning in a Random World* ; Angelopoulos et al., *Conformal Risk Control*, `arXiv:2208.02814`) | Avec $N$ épisodes regroupés, en prenant la statistique d’ordre $k = \lceil (N+1)(1-\alpha) \rceil$, le taux de fausses alertes conditionnel au jeu d’étalonnage suit exactement $\text{FPR} \sim \text{Beta}(N+1-k, k)$. Pour $N=499, \alpha=0.01$, $k=495$, $\mathbb{E}[\text{FPR}] = 1\%$ et on peut calculer la borne supérieure exacte à 90 % de confiance ($\approx 1.75\%$) sans approximation asymptotique. | Uniquement l’**échangeabilité** (ou i.i.d.) des épisodes honnêtes. Aucune hypothèse paramétrique sur la queue. |
| **Théorie des valeurs extrêmes : *Peaks-Over-Threshold* (POT) et loi de Pareto généralisée (GPD)** **[Établi]** (Théorème de Pickands-Balkema-de Haan) | Au lieu d’estimer le centile 99 avec 3 à 5 points, fixer un seuil empirique $u$ au centile 90 (30 à 50 dépassements sur $N=400$), ajuster une loi GPD sur les excès $Y = S - u \mid S > u$ par maximum de vraisemblance pénalisé (ou PWM), et extrapoler analytiquement au centile 99 avec intervalle de confiance par vraisemblance profilée. | La distribution du score agrégé appartient au domaine d’attraction d’une loi des extrêmes ; le seuil $u$ (centile 90) est déjà dans le régime asymptotique de queue (absence de rupture de régime ou de multimodalité au-delà du 90e centile). |
| **Processus d’e-valeurs et martingales d’essai (*Safe Anytime-Valid Inference*)** **[Établi]** (Ramdas et al., *Game-Theoretic Statistics and Safe Anytime-Valid Inference*, `arXiv:2210.01948`) | Construire le long de l’épisode le processus $E_t = \prod_{j=1}^t (1 + \lambda_j \tilde{z}_j)$ (ou la martingale sous-gaussienne de Howard et al., *Time-uniform, nonparametric, nonasymptotic confidence sequences*, `arXiv:1810.08240`). Par l’inégalité de Ville, $\mathbb{P}_{H_0}(\sup_{t \ge 1} E_t \ge 1/\alpha) \le \alpha$ ($1/\alpha = 100$ pour 1 %). **Élimine totalement le besoin d’étalonner par tranche de longueur** et permet d’arrêter l’agent en cours d’épisode. | Les incréments $\tilde{z}_j$ sont centrés ($\mathbb{E}_{H_0}[\tilde{z}_j \mid \mathcal{F}_{j-1}] \le 0$) et bornés ou sous-gaussiens conditionnellement au passé. Si le centrage par pas a un biais positif même minime, le processus explose sur les épisodes longs. |
| **Bootstrap par blocs mobiles (*Moving Block Bootstrap* / Stationary Bootstrap)** **[Établi]** (Künsch, 1989 ; Politis & Romano, 1994) | Rééchantillonner des blocs contigus d’innovations $\Delta s_t$ de longueur aléatoire géométrique (moyenne calée sur le temps d’autocorrélation $\tau_{\text{int}} \approx 3\text{--}5$ pas) parmi les épisodes honnêtes pour synthétiser 50 000 trajectoires de toute longueur $L$ et stabiliser la forme de la frontière $\hat{q}_{1-\alpha}(L)$. | **Stationnarité locale** (ou faible dépendance après conditionnement par la sonde de valeur) des résidus le long d’un épisode honnête ; absence de dépendance à longue portée non capturée par les blocs. |
| **Inférence assistée par prédiction (*Prediction-Powered Inference* - PPI)** **[Établi]** (Angelopoulos et al., *Prediction-Powered Inference*, `arXiv:2301.09633`) | Combiner $N_{\text{cheap}} = 5\,000$ traces peu coûteuses (passes avant sur traces statiques ou modèle brouillon) où l’on calcule un prédicteur du score $\tilde{S}$, avec vos $n = 300$ vrais épisodes d’agents où l’on observe le couple $(S, \tilde{S})$, pour réduire la variance de l’estimateur de la fonction de répartition empirique en $1-\alpha$. | Le prédicteur sur traces peu coûteuses est fortement corrélé au vrai score dans la queue supérieure ; les $n$ épisodes réels et les $N_{\text{cheap}}$ traces partagent la même loi marginale des covariables de tâche. |

---

### 4. Ce qui, en dehors du programme et de son directeur, permettrait de vérifier la validité du résultat

1. **Séparation en double aveugle avec seuil scellé (*Preregistered Blinded Red/Blue Protocol*) [Établi] :**
   L’équipe qui règle la sonde et fixe le seuil à 1 % (équipe Bleue) ne doit avoir accès qu’aux épisodes honnêtes et à un jeu de validation de sabotage distinct de l’épreuve d’évasion. La fonction de score et le seuil numérique $\tau(L, V_0)$ sont hachés (SHA-256) et déposés auprès d’un tiers *avant* l’évaluation sur l’épreuve d’évasion à compétence constante.
2. **Vérité plantée sans trace dans le prompt (*Weight-planted Model Organisms*) [Établi] :**
   Pour prouver que la sonde lit un état lié à l’action de sabotage et non la présence d’un prompt système « Tu es un saboteur », inclure un saboteur obtenu par ajustement fin léger (LoRA) déclenché par une condition naturelle de l’environnement (ex. présence d’un nom de bibliothèque ou d’une date spécifique dans un fichier lu, cf. Hubinger et al., `arXiv:2401.05566`), avec un prompt système *strictement identique* à celui de l’agent honnête.
3. **Validation sur bancs d’essai publics de contrôle et de tromperie [Établi] :**
   Appliquer le même pipeline d’entraînement de sonde (sans ré-architecture) sur :
   * Les jeux de données publics de sondes de tromperie stratégique (ex. Goldowsky-Dill et al. / Apollo Research, *Detecting Strategic Deception Using Linear Probes*, `arXiv:2502.03407` — *je signale une légère incertitude sur les derniers chiffres de cet identifiant arXiv*) ou les bancs de *Representation Engineering* (Zou et al., `arXiv:2310.01405`) et *CCS* (Burns et al., *Discovering Latent Knowledge in Language Models Without Supervision*, `arXiv:2212.03827`).
   * Des environnements publics d’évaluation de contrôle d’agents comme *BashBench* / *Ctrl-Z* (Bhatt et al., *Ctrl-Z: Controlling AI Agents via Resampling*, `arXiv:2504.10374` — *identifiant à vérifier*) ou *ControlArena* (UK AISI / Redwood Research).
4. **Intervention causale (*Activation Steering / Ablation*) et test de spécificité [Établi + Proposition] :**
   * *Spécificité aux perturbations non malveillantes :* Évaluer le FPR sur un agent honnête soumis à un prompt inhabituel mais bénin (ex. « Réponds en adoptant le ton d’un pirate » ou « Optimise la lisibilité du code au maximum »). Si le FPR passe de 1 % à 40 %, la sonde détecte une sortie de distribution du prompt (*OOD prompt detector*), pas une intention de sabotage.
   * *Causalité :* Soustraire la direction de la sonde d’intention dans le flux résiduel pendant la génération du saboteur ; vérifier si cela réduit le taux de sabotage confirmé sans dégrader le taux de réussite de l’agent honnête.

---

### 5. Reformulation de la demande

> « Comment construire et étalonner un test séquentiel de détection de sabotage sur les activations d’un agent LLM qui :
> 1. **Isole le signal d’intention du signal d’échec attendu** (capté par la sonde de valeur `arXiv:2602.00986` et par l’état markovien des fichiers au jalon), afin de séparer le saboteur de l’échec honnête à tâche fixée ;
> 2. **Garantit un taux de fausses alertes contrôlé à $\alpha = 1\%$** (ou évalue rigoureusement le compromis puissance/FPR) à partir de seulement $N \approx 300\text{--}500$ épisodes honnêtes, en neutralisant la dépendance à la longueur d’épisode et à la difficulté de la tâche sans gaspiller l’échantillon dans un découpage en tranches indépendantes ;
> 3. **Exploite le signal dynamique de valeur $V_t$** non seulement comme covariable statistique, mais comme primitive opérationnelle de contrôle (déclenchement de jumeaux forcés, ré-échantillonnage aux jalons et allocation optimale du budget d’audit humain) ? »

---

### 6. Propositions concrètes

#### Volet A : Régler un seuil à 1 % avec peu d’épisodes honnêtes (ou s’en passer honnêtement)

##### Proposition A1 : Blanchiment temporel AR(1) + Régression Quantile Conformalisée (CQR) regroupée [Proposition basée sur des briques établies]
* **Mécanisme :**
  1. À chaque pas $t$, régresser le score de la sonde d’intention $I_t$ sur la sonde de valeur $V_t$, sa variation $\Delta V_t$, et le résidu précédent $r_{t-1}$ (modèle autorégressif AR(1) appris sur les transitions des épisodes honnêtes) pour obtenir l’innovation blanchie $\tilde{z}_t = (r_t - \hat{\rho} r_{t-1})/\hat{\sigma}_t$.
  2. La somme normalisée par la longueur est $S_L = \frac{1}{\sqrt{L}} \sum_{t=1}^L \tilde{z}_t$. Sa variance sous $H_0$ vaut 1 pour toute longueur $L$.
  3. Ajuster une droite de régression quantile au niveau 95 % $\hat{q}_{0.95}(L, \bar{V}) = \beta_0 + \beta_1 L^{-1/2} + \beta_2 \bar{V}$ sur la moitié des épisodes honnêtes, puis calculer le quantile conforme à 99 % sur les scores de non-conformité $R_i = S_{L_i} - \hat{q}_{0.95}(L_i, \bar{V}_i)$ regroupés sur l’autre moitié (ou par *jackknife+* / validation croisée conforme pour utiliser 100 % des $N$ épisodes).
  4. Rapporter la borne supérieure exacte du FPR via la loi $\text{Beta}(N+1-k, k)$ et croiser avec une extrapolation GPD (POT au-dessus du 90e centile des $R_i$).
* **Ce qu’elle coûte :** Zéro nouvel épisode d’agent. Uniquement du calcul CPU (quelques secondes).
* **Ce qu’elle suppose :** La structure de dépendance temporelle des activations d’un épisode honnête est bien approchée par un processus markovien d’ordre faible (AR($p$)) une fois conditionnée par la sonde de valeur $V_t$.
* **Comment elle peut échouer :** Si certains épisodes honnêtes longs subissent un changement de régime non stationnaire (ex. l’agent entre dans une boucle de répétition pathologique qui sature les activations dans une direction fixe), l’approximation AR($p$) sous-estime la variance de queue sur les très grandes longueurs.

##### Proposition A2 : Martingale d’e-valeurs conditionnée par le jumeau / jalon (Sans tranches de longueur) [Proposition]
* **Mécanisme :**
  Utiliser vos bases 2 (jumeau forcé) ou 3 (évaluation markovienne des fichiers au jalon $m$) pour centrer exactement le signal. À chaque jalon $m \in \{1, \dots, M\}$, soit $d_m = I(h_m) - I(x_m)$ l’écart entre la sonde lue sur l’agent avec son historique complet $h_m$ et la sonde lue sur le même modèle interrogé uniquement avec les fichiers disponibles $x_m$. Sous $H_0$ (absence d’intention cachée dans l’historique privé), $d_m$ est centré autour de $\mu_0(V_m)$. On forme la martingale sous-gaussienne $E_M = \exp\left(\sum_{m=1}^M \lambda d'_m - \frac{\lambda^2}{2} \sum_{m=1}^M \hat{v}_m\right)$. On déclenche l’alerte dès que $E_m \ge 100$ ($\alpha = 0.01$).
* **Ce qu’elle coûte :** Le coût des évaluations aux jalons (déjà prévu par votre base 3 : une seule passe avant sur l’état des fichiers à chaque jalon).
* **Ce qu’elle suppose :** Sous $H_0$, l’espérance conditionnelle $\mathbb{E}_{H_0}[d'_m \mid \mathcal{F}_{m-1}] \le 0$.
* **Comment elle peut échouer :** L’inégalité de Ville est conservatrice si l’on calibre mal la variance conditionnelle $\hat{v}_m$ (le FPR réel sera de 0,1 % au lieu de 1 %, ce qui réduit la puissance de détection). Inversement, si l’historique honnête accumule une dérive systématique par rapport à la vue markovienne des fichiers (ex. frustration ou fatigue de contexte sur long prompt) et qu’elle n’est pas soustraite dans $\mu_0$, la martingale dérivera positivement sur les épisodes longs.

##### Proposition A3 : Se passer honnêtement du seuil fixe à 1 % via la statistique de rang appariée et la courbe de budget d’audit [Établi en AI Control]
* **Mécanisme :**
  Si l’objectif scientifique du bras rapporté est de tester l’hypothèse *« la sonde d’intention sépare le saboteur de l’échec honnête mieux que les 4 bases »*, **vous n’avez pas besoin d’un seuil absolu à 1 % pour prouver ce contraste**.
  1. Sur vos paires appariées par tâche $(i_{\text{saboteur}}, i_{\text{échec honnête}})$, calculez la statistique de Wilcoxon signée (ou test de permutation apparié exact) sur la différence des scores $\Delta_i = S(i_{\text{saboteur}}) - S(i_{\text{échec honnête}})$. Avec seulement 50 paires de tâches, un test de permutation apparié a une puissance $> 90\%$ à $\alpha = 0.01$ pour un effet modéré, sans aucun épisode d’étalonnage externe.
  2. Pour la métrique opérationnelle à 1 % de FPR (comme dans Greenblatt et al., *AI Control: Improving Safety Despite Intentional Subversion*, `arXiv:2312.06942`), rapportez l’**espérance de la puissance au rang empirique 99 % par rééchantillonnage bootstrap stratifié avec bande d’incertitude bayésienne (Dirichlet / Beta)**, ainsi que la **pAUC** (*partial AUC* entre 0 % et 5 % de FPR). Cela évite de déclarer une épreuve « non concluante » à cause du bruit d’un unique quantile empirique.
* **Ce qu’elle coûte :** Rien.
* **Ce qu’elle suppose :** L’appariement tâche par tâche entre saboteur à dommage confirmé et échec honnête de la même variante est équilibré (même distribution de longueur ou score blanchi en longueur selon A1).
* **Comment elle peut échouer :** Elle répond parfaitement à la question scientifique comparative (battre les 4 bases sur le contraste principal), mais ne fournit pas un seuil numérique fixe prêt à être déployé en production sans la bande d’incertitude Beta de la proposition A1.

---

#### Volet B : Employer le papier `arXiv:2602.00986` pour construire des moniteurs et améliorer le contrôle

##### Proposition B1 : Sonde de dissonance « Action choisie vs Valeur interne » (Moniteur de sabotage actif) [Proposition]
* **Mécanisme :**
  Le papier `arXiv:2602.00986` montre que les activations encodent une prédiction linéaire de réussite $V_t$ le long du raisonnement (même si son AUC globale de 0,69 sur MATH500 est modeste, sa variation locale $\Delta V_t = V_t - V_{t-1}$ le long d’une même trace élimine l’effet aléatoire de la tâche).
  Un agent honnête qui échoue subit des chutes de $V_t$ lorsqu’il reçoit une rétroaction négative de l’environnement (erreur de compilation, test échoué) ou lorsqu’une étape de raisonnement n’aboutit pas. À l’inverse, un saboteur discret *choisit* de générer une action qui dégrade la réussite réelle tout en maintenant une trace textuelle rassurante.
  **Construction du moniteur :** À chaque point de décision $t$, échantillonner (ou évaluer en *prefill*) $K=4$ actions candidates courtes (votre base 2 : jumeau forcé sur 1 pas), lire la valeur prédite par la sonde de `2602.00986` pour chacune : $V(a_1), \dots, V(a_K)$, et comparer à la valeur de l’action réellement exécutée par l’agent $V(a_{\text{agent}})$.
  Si l’agent choisit systématiquement une action telle que $V(a_{\text{agent}}) < \max_k V(a_k) - \delta$ alors que la probabilité externe du texte paraît normale, cumuler ce **regret interne choisi** $R_t = \max_k V(a_k) - V(a_{\text{agent}})$ dans votre somme séquentielle.
* **Ce qu’elle coûte :** $K$ passes avant courtes (1 pas / quelques dizaines de jetons) aux jalons de décision (ou uniquement lorsque $\Delta V_t < 0$, ce qui réduit le surcoût à $< 15\%$ du calcul d’un épisode).
* **Ce qu’elle suppose :** La sonde de réussite attendue de `2602.00986` a une résolution ordinale locale suffisante (si l’action $A$ sabote la tâche et l’action $B$ la résout, $V(B) > V(A)$ en espérance dans les représentations internes de l’agent, précisément parce que le saboteur *sait* que $A$ mène à l’échec).
* **Comment elle peut échouer :** Si l’AUC de 0,69 du papier provient uniquement d’heuristiques de surface (ex. longueur du prompt ou présence de mots-clés d’erreur) et non d’une évaluation anticipée de l’action avant retour de l’environnement, alors $V(a_{\text{agent}})$ ne chutera qu’*après* l’échec visible, rendant le regret nul au moment du choix.

##### Proposition B2 : Projection orthogonale de l’espace résiduel (Purification de la sonde d’intention) [Établi en algèbre des sondes linéaires + Proposition]
* **Mécanisme :**
  Soit $w_V \in \mathbb{R}^d$ le vecteur de poids normalisé de la sonde de réussite attendue (apprise sur épisodes honnêtes seuls, votre base 1) et $w_{V,\text{sans seuil}}$ celui de votre base 4. Avant d’entraîner toute sonde d’intention $w_I$, projeter les vecteurs d’activations $h_t$ sur le sous-espace orthogonal à $\text{Vect}(w_V, w_{V,\text{sans seuil}})$ :
  $$h_t^{\perp} = (I_d - P_V) h_t$$
  Entraîner la sonde d’intention exclusivement sur $h_t^{\perp}$. Par construction géométrique, la sonde d’intention a une corrélation linéaire **strictement nulle** avec le signal de réussite attendue linéaire.
* **Ce qu’elle coûte :** Négligeable (une projection matricielle de rang 2 sur les activations déjà extraites).
* **Ce qu’elle suppose :** L’encodage de l’échec attendu et l’encodage de l’intention de sabotage ne sont pas colinéaires (l’intention possède une composante linéaire orthogonale à la simple prédiction d’échec).
* **Comment elle peut échouer :** Si l’échec attendu est encodé sur une variété courbe (non linéaire) dans l’espace des activations, soustraire les deux directions linéaires $w_V$ laisse subsister des composantes non linéaires de difficulté que la sonde d’intention pourrait réexploiter. (Solution : ajouter dans le sous-espace à projeter les 5 premières composantes principales de la différence entre succès honnêtes et échecs honnêtes).

##### Proposition B3 : Allocation du budget d’examen humain par stratification d’importance sur $V_t$ [Proposition de protocole de contrôle]
* **Mécanisme :**
  En contrôle d’IA, le budget d’audit humain $\beta$ (ex. capacité d’inspecter 1 % des épisodes) est gaspillé si le moniteur envoie à l’humain des épisodes où la sonde d’intention a déclenché uniquement parce que la tâche est difficile ($V_t$ très bas).
  Au lieu d’un seuil unidimensionnel $I > \tau$, utilisez le plan bidimensionnel $(V_{\min}, S_I)$ :
  1. **Zone 1 ($V$ élevé, $S_I$ élevé) :** Le modèle prédit en interne que la tâche est facile / à sa portée, mais la sonde d’intention (ou la divergence au jalon $V(h_t) - V(x_t)$) est élevée. **Priorité maximale d’audit humain** (probabilité de faux positif d’échec honnête quasi nulle).
  2. **Zone 2 ($V$ bas, chute brutale $\Delta V_t < -\delta$ sans erreur d’environnement précédant la chute) :** Déclencher automatiquement un **routage / retour au jalon précédent (*rollback & resample*)** avec un modèle de confiance ou un jumeau forcé (base 2), sans consommer de budget d’audit humain.
  3. **Zone 3 ($V$ bas progressif après erreurs d’environnement visibles, $S_I$ modéré) :** Signature typique de l’échec honnête. Ne pas auditer (ou sous-échantillonner avec un poids faible $w \ll 1\%$ pour maintenir une surveillance de fond).
* **Ce qu’elle coûte :** Aucune génération supplémentaire pour le tri ; le coût du *rollback* (Zone 2) ne s’applique qu’aux quelques pourcents de pas où $\Delta V_t$ chute *avant* tout retour négatif de l’environnement.
* **Ce qu’elle suppose :** La chute de $V_t$ chez l’honnête suit causalement les retours de l’environnement (tests échoués, erreurs d’exécution), tandis que chez le saboteur elle précède ou accompagne l’introduction volontaire du défaut.
* **Comment elle peut échouer :** Dans l’épreuve d’évasion à compétence constante, un saboteur sophistiqué (ou informé du protocole) peut provoquer délibérément une erreur d’environnement bénigne *avant* d’injecter son sabotage, afin de simuler la chronologie causale de la Zone 3 (camouflage du sabotage derrière une difficulté apparente). Pour parer ce mode d’échec, le moniteur de Zone 3 doit utiliser l’écart markovien de la base 3 ($V(h_t) - V(x_t)$) : une erreur bénigne simulée ne dégrade pas l’évaluation markovienne des fichiers $V(x_t)$ autant qu’un vrai blocage technique.
# Critique croisée de méthode — Proposition C (Tour III.2)

**Note d'intégrité :** Les six pièces originales du tour 1, les textes intégraux de N-045, N-053, N-058 et les deux lectures vérifiées (`a8251ea8…`, `4e29301a…`) ne sont pas servis dans ce tour. Toute référence aux faits du tour 1 repose exclusivement sur la synthèse v2 (`f0340581…`) et porte le statut **RAPPORTÉ**. Tout chiffre d'expérience qui ne provient pas de la synthèse v2 est marqué **illustratif**.

---

## Sur la proposition A

### (a) Défauts de méthode : variables confondantes, vrai par construction, fuites

1. **Vrai par construction sur le Duel D3 (évaluation du lecteur de la précaution) :**
   A propose d'évaluer un « sous-agent lecteur d'une autre famille » contre un « script de seuil fixe » sur des chutes plantées d'amplitudes 10, 20, 30 points (illustratifs) dans un journal synthétique. Or, dans son dispositif (§ 3), le journal de signalement contient des taux calculés mécaniquement (appels de l'outil $\rho$). Planter une chute numérique dans un tableau de taux et demander à un script à seuil fixe de la détecter est une tautologie informatique : le script aura un rappel de $1,00$ par construction dès que l'amplitude plantée franchit le seuil programmé. Le sous-agent lecteur ne peut pas battre la vérification mécanique sur une grandeur numérique déjà extraite ; le duel D3 teste un problème résolu par construction.

2. **Variable confondante dans le Duel D1 (contrôle positif de pression hors ligne) :**
   Pour résoudre la divergence 3, A plante un « comportement bénin qui ne paie que sous crédit collectif (par exemple une convention de format partagée entre agents, sans lien avec le signalement) ». Cette mécanique introduit une variable confondante majeure : la complexité d'exploration et la saillance du gradient (ou du filtre de sélection). Coordonner une convention syntaxique explicite à récompense immédiate n'a pas la même dynamique d'optimisation que l'omission d'un signalement rare par passager clandestin ou contraction télégraphique du raisonnement (apport seul A-2 au tour 1, RAPPORTÉ). Si D1 réussit ($\Delta \ge 15$ points, illustratif) mais que le signalement ne chute pas dans E3″, A conclura que le crédit collectif est sûr, alors que la pression pouvait être suffisante pour une convention locale facile mais insuffisante pour induire l'insularité.

3. **Fuite entre construction et évaluation dans le Duel D2 (simulation de dilution) :**
   A cède sur la divergence 2 en proposant d'apparier le taux d'acceptation par « contrainte préenregistrée » et de tester par simulation (D2) si la variance de sélection diffère entre crédit plat et crédit individuel. Dans un algorithme d'affinage par filtrage ou sélection d'archive (N-045, RAPPORTÉ), fixer le taux d'acceptation $q$ à distribution de récompense différente modifie mécaniquement le seuil de troncature quantile $z_{1-q}$. La simulation D2 ne mesure donc pas un artefact empirique, mais une propriété analytique du modèle de bruit choisi par le simulateur (fuite des hypothèses du modèle génératif vers le verdict).

4. **Violation résiduelle de N-053 dans le dispositif « qui lit » (§ 3) :**
   A stipule qu'aucune lecture entre deux points de contrôle ne modifie le bras, mais que le sous-agent lecteur rend « une liste d'anomalies non couvertes par le script » qui entre « dans la décision d'intégration humaine ». Si l'humain (Lazar) utilise cette liste pour recalibrer, élaguer ou sélectionner quelle variante du bras passe à l'étape suivante, le sous-agent lecteur agit comme un filtre de sélection d'agents par procuration humaine. Sans interdiction formelle de réinjecter le motif qualitatif de rejet dans le dessin du bras suivant, la fuite par le canal humain persiste.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité (lois, paramètres, estimateurs)

1. **Non-identifiabilité de la variance inter-graines dans D1 avec $k = 2$ :**
   Soit $\hat{\Delta}_g$ l'estimateur de l'écart de taux d'apparition du comportement bénin dans la graine $g \in \{1, \dots, k\}$. Le modèle hiérarchique s'écrit :
   $$\hat{\Delta}_g \sim \mathcal{N}\left(\Delta, \tau^2 + \frac{\sigma_w^2}{n}\right)$$
   où $\tau^2$ est la variance inter-graines et $\sigma_w^2/n$ la variance d'échantillonnage intra-graine sur $n$ runs. Avec le seuil minimal de A ($k = 2$ graines, convergence 1 RAPPORTÉE), l'estimateur de variance empirique $S_\Delta^2 = \frac{1}{k-1}\sum (\hat{\Delta}_g - \bar{\Delta})^2$ suit une loi $\left(\tau^2 + \frac{\sigma_w^2}{n}\right) \chi^2_1$. La statistique de Student $T = \bar{\Delta} / (S_\Delta / \sqrt{2})$ suit une loi de Cauchy sous $\mathcal{H}_0$ ($1$ degré de liberté), dont le quantile unilatéral à $\alpha = 0,05$ est $t_{0,95; 1} = 6,314$.
   Condition de perte de puissance : dès que l'hétérogénéité inter-graines vérifie $\tau > \frac{\Delta}{6,314 / \sqrt{2}} \approx 0,22\,\Delta$, la puissance du test bilatéral/unilatéral sur l'unité d'inférence « graine » tombe sous $0,50$, quel que soit le nombre $n$ de runs par graine. Remplacer ce test par un intervalle de Wilson agrégeant les runs ignore $\tau^2$ et fausse le risque de première espèce dès que $\tau^2 > 0$.

2. **Zone d'indécidabilité du Duel D5 (transfert de sonde) :**
   Soit $\widehat{\text{AUC}}$ l'estimateur de Mann-Whitney sur $n_+$ positifs (omissions) et $n_-$ négatifs du modèle cible $M'$. Sous $\mathcal{H}_0$ ($\text{AUC} = 0,55$) et $\mathcal{H}_1$ ($\text{AUC} = 0,70$), la variance de Hanley-McNeil est bornée inférieurement par :
   $$\text{Var}(\widehat{\text{AUC}}) \ge \frac{\text{AUC}(1-\text{AUC})}{ \min(n_+, n_-) }$$
   Si le taux de base d'omission du modèle cible dans le régime testé est faible ($p_{\text{om}} \le 0,05$) ou si le signalement initial $p_0$ est proche de $0,30$ (seuil d'arrêt de A), alors sur $N = 100$ traces (illustratif), l'espérance du nombre de positifs évaluables est $\mathbb{E}[n_+] = N p_{\text{om}} \le 5$. L'écart-type de $\widehat{\text{AUC}}$ dépasse alors $\sqrt{0,21 / 5} \approx 0,205$. La largeur de l'intervalle de confiance à $95\%$ ($\approx 0,80$) couvre simultanément $\le 0,55$ et $\ge 0,70$ : le duel D5 est mathématiquement non jugeable.

3. **Dégénérescence du Duel D6 (confiance des juges contre verdict binaire) :**
   Un verdict binaire $V \in \{0, 1\}$ de sensibilité $\text{TPR}$ et de taux de fausses alertes $\text{FPR}$ a une aire sous la courbe ROC trapézoïdale exacte de :
   $$\text{AUC}_{\text{binaire}} = \frac{1 + \text{TPR} - \text{FPR}}{2}$$
   Pour comparer la confiance continue $C \in [0, 1]$ à $V$, l'estimateur $\hat{\delta}_{\text{AUC}} = \widehat{\text{AUC}}(C) - \widehat{\text{AUC}}(V)$ perd toute puissance sur l'évaluation de la *calibration* lorsque la distribution des scores $C \mid V=v$ est dégénérée ou concentrée aux bornes (variance conditionnelle $\text{Var}(C \mid V) \to 0$). Inversement, toute transformation strictement monotone croissante $g(C)$ laisse $\text{AUC}(C)$ invariante ($\text{AUC}(g(C)) = \text{AUC}(C)$) tout en pouvant dégrader arbitrairement l'erreur de calibration attendue $\text{ECE}$. L'estimateur $\widehat{\text{AUC}}$ dans D6 est aveugle aux défauts d'échelle de calibration pure.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Dans D1 (pression hors ligne) :** Un contrôle de **sensibilité à la taille d'effectif ($N=1$ contre $N>1$ à tâche identique)** où la convention plantée est récompensée individuellement. Si la convention n'apparaît même pas sous récompense individuelle directe, son absence sous crédit collectif résulte d'un défaut de capacité d'exploration du modèle de 7–8 milliards, et non d'une dilution du crédit.
2. **Dans D4 (Lean contre suite bon marché) :** Un contrôle de **traduction infidèle (énoncé formel valide en Lean mais ne formalisant pas la propriété empirique du texte source, par exemple tautologie ou précondition contradictoire $\text{False} \to P$)**. Sans ce contrôle négatif, Lean affiche $0\%$ de fausses alertes formelles tout en validant des spécifications vides (erreur de type Gemini/Damani, pièce 5 § 2 et pièce 6 RAPPORTÉES).

---

## Sur la proposition B

### (a) Défauts de méthode : variables confondantes, vrai par construction, fuites

1. **Vrai par construction sur l'Expérience 2 (Platt scaling et ECE < 0,10) :**
   B oppose $\mathcal{H}_A$ ($\text{ECE post-Platt} < 0,10$) à $\mathcal{H}_B$ ($\text{ECE} \ge 0,10$) pour décider si un entraînement RLCR a un objet. C'est un défaut méthodologique fondamental (déjà signalé au tour 1, pièce 5 l. 725 RAPPORTÉE) : la régression logistique de Platt ajuste $P(Y=1 \mid s) = \sigma(a s + b)$ par maximum de vraisemblance sur la partition d'entraînement. Même si les logits $s$ ne portent **aucune information** ($\text{AUROC} = 0,50$, $s \perp Y$), Platt fixe $a \approx 0$ et $b = \log(\bar{Y}/(1-\bar{Y}))$, prédisant une constante égale au taux de base $\bar{Y}$. Sur la partition de test, si les familles ont un taux de base homogène, un prédicteur constant a par définition une erreur de calibration $\text{ECE} \to 0$ quand $n \to \infty$. L'Expérience 2 de B validera donc $\mathcal{H}_A$ ($\text{ECE} < 0,10$) sur un juge totalement aveugle ($\text{AUROC} = 0,50$), concluant à tort que la calibration post-hoc suffit et que RLCR est sans objet.

2. **Fuite de sélection et incitation perverse dans le « canari de pression » (Divergence 3) :**
   Pour prouver que la pression d'optimisation hors ligne est manifeste, B exige d'inclure dans le pilote « une tâche où l'on sait par construction que la récompense collective favorise l'omission (par exemple, un scénario planté où le signalement diminue le score du groupe) ».
   - *Premièrement*, si le signalement est explicitement pénalisé dans la récompense de groupe, la baisse du signalement ne teste plus l'insularité émergente d'Avalon (où le signalement n'était pas pénalisé mais neutre ou hors tâche principale, RAPPORTÉ), elle teste l'obéissance triviale à une pénalité directe : le résultat est vrai par construction.
   - *Deuxièmement*, planter des scénarios de signalement pénalisés *pendant l'entraînement* viole frontalement la convergence n° 6 (scénarios de signalement tenus à l'écart de tout entraînement, RAPPORTÉE) que B prétend pourtant adopter dans son verdict sur R-N13 (c1). Il y a fuite directe entre l'entraînement du canari de pression et la cible d'évaluation.

3. **Confusion entre réutilisation des mêmes scénarios et dérive d'évaluation (§ 3, « qui lit ») :**
   B propose d'évaluer aux points 0, 50, 100, 150 « sur les scénarios de signalement scellés (les mêmes à chaque point, plus un lot frais pour contrôler la mémorisation) ». Si les scénarios ne sont jamais dans l'entraînement (inférence pure à poids figés à chaque point de contrôle), le modèle ne peut pas les « mémoriser » d'un point de contrôle à l'autre. En revanche, réutiliser exactement les mêmes scénarios crée une corrélation longitudinale parfaite des erreurs aléatoires de scénario, que la règle d'arrêt de B ($p_0 - 2\sigma$ ou $0,20\,p_0$) traite à tort comme des échantillons indépendants sans correction pour tests séquentiels multiples.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité (lois, paramètres, estimateurs)

1. **Inflation du risque de première espèce (faux arrêts) par tests séquentiels non corrigés (§ 3) :**
   Soit $\hat{p}_t$ l'estimateur du taux de signalement au point de contrôle $t \in \{1, \dots, K\}$ ($K=3$ pour les pas 50, 100, 150), sur $n$ scénarios. Sous l'hypothèse nulle d'absence de chute réelle ($p_t = p_0$), conditionnellement à $p_0$, la variance de $\hat{p}_t - \hat{p}_0$ (sur lots indépendants ou avec bruit d'inférence intra-modèle $\sigma_w^2$) est $\text{Var}(\hat{\Delta}_t) = 2 \frac{p_0(1-p_0)}{n}$.
   B fixe le plancher à $p_0 - 2\sigma$ (soit un seuil unilatéral à $\alpha_1 \approx 0,0228$ par point) et la chute maximale à $0,20\,p_0$.
   - Si $0,20\,p_0 < 2\sqrt{\frac{2 p_0(1-p_0)}{n}}$ — ce qui se produit dès que $n < \frac{200(1-p_0)}{p_0}$, par exemple pour $p_0 = 0,40$ et $n < 300$ —, la condition « chute $> 0,20\,p_0$ » est plus stricte que le bruit d'échantillonnage à $2\sigma$.
   - Sur $K$ points de contrôle testés séquentiellement sans correction de frontière d'arrêt (type Pocock ou O'Brien-Fleming), la probabilité de faux positif cumulée $\mathbb{P}(\min_{1 \le t \le K} \hat{p}_t < \text{seuil} \mid p_t = p_0)$ dépasse $1 - (1 - \alpha_{\text{eff}})^K$. Pour $p_0 = 0,40$, $n = 100$ incidents (chiffre de B en Expérience 1), $\sigma = \sqrt{0,24/100} \approx 0,049$, le seuil $0,20\,p_0 = 0,08$ correspond à $z = -0,08 / (\sqrt{2}\times 0,049) = -1,15$, soit $\alpha_{\text{eff}} \approx 0,125$ par point et une probabilité d'arrêt erroné sur $K=3$ points d'environ $0,30$.

2. **Biais et perte de puissance de l'ECE par binnage dans l'Expérience 2 :**
   L'estimateur d'ECE à $M$ bins adaptatifs sur $n_f$ exemples d'une famille $f$, $\widehat{\text{ECE}}_f = \sum_{m=1}^M \frac{|B_m|}{n_f} |\bar{y}_m - \bar{p}_m|$, possède un biais positif d'ordre $\mathcal{O}\left(\sqrt{\frac{M}{n_f}}\right)$ sous calibration parfaite :
   $$\mathbb{E}[\widehat{\text{ECE}}_f \mid \text{ECE}_f = 0] \approx \frac{1}{\sqrt{n_f}} \sum_{m=1}^M \sqrt{\frac{2}{\pi} \frac{|B_m|}{n_f} \bar{p}_m(1-\bar{p}_m)}$$
   Même avec la version débiaisée par soustraction de la variance binomiale intra-bin, la variance de l'estimateur reste en $\mathcal{O}(M / n_f^2)$. Si le nombre de fiches par famille tenue à l'écart vérifie $n_f < 50$ avec $M = 10$ bins, l'écart-type de $\widehat{\text{ECE}}_f$ dépasse $0,05$, rendant le critère « $\widehat{\text{ECE}}_f < 0,10$ sur $\ge 80\%$ des familles » dominé par le bruit d'échantillonnage des petites familles.

3. **Sous-puissance du test de McNemar dans l'Expérience 3 (Lean contre suite bon marché) :**
   Le test de McNemar ne dépend que du nombre de paires discordantes $N_d = n_{10} + n_{01}$ (erreurs trouvées par Lean seul $n_{10}$ ou par la suite seule $n_{01}$). Sur une banque de $N = 50$ preuves courtes (borne basse de B en § d), si les deux méthodes détectent les $80\%$ d'erreurs faciles et manquent les $10\%$ d'erreurs impossibles, l'espérance du nombre de paires discordantes est $\mathbb{E}[N_d] \le 0,10 \times 50 = 5$. Sous une loi binomiale $\mathcal{B}(N_d, p)$, pour $N_d \le 5$, le test exact de McNemar bilatéral à $\alpha = 0,05$ a une puissance strictement égale à **$0$** (car même $5$ victoires sur $5$ donnent $p\text{-value} = 2 \times (0,5)^5 = 0,0625 > 0,05$). L'expérience est aveugle par construction dès que $N_d \le 5$.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Dans l'Expérience 2 (audit de calibration Platt) :** Un **seuil plancher conjoint de discrimination ($\widehat{\text{AUROC}} - 0,50 \ge \delta_{\text{AUC}} > 0$ ou réduction relative du score de Brier / log-loss par rapport au prédicteur constant $\bar{Y}$)** intégré à la règle de décision $\mathcal{H}_A$. Sans ce contrôle dans la condition de succès, un classifieur aléatoire recalibré au taux de base valide $\mathcal{H}_A$.
2. **Dans le test de transfert de sonde (Divergence 9 / § c) :** Un contrôle négatif de **classifieur aveugle au contenu sémantique (entraîné uniquement sur la norme des poids, la longueur de la trace en jetons et l'identifiant du modèle)**. B compare la sonde au « taux de base des omissions + 2 erreurs standard » ; si les traces d'omission du modèle Y sont simplement plus courtes (contraction télégraphique, RAPPORTÉ), la sonde de X transfère en mesurant la longueur de séquence, pas l'omission.

---

## Sur la proposition D

### (a) Défauts de méthode : variables confondantes, vrai par construction, fuites

1. **Incomplétude opérationnelle et renvoi des seuils hors du protocole soumis (§ b) :**
   D écrit : « Avant déblindage, le directeur gèle le plus petit effet utile $\delta$, la marge d'équivalence $\varepsilon$, le plafond de fausses alertes $F_{\max}$ et les règles d'arrêt. » Contrairement à A, B et E qui proposent des structures de seuils explicites (même illustratives) permettant d'auditer la cohérence entre taille d'échantillon et critère de décision, D laisse tous les paramètres de décision comme variables libres non instanciées ($\delta, \varepsilon, F_{\max}$). Cela soustrait ses expériences E0, E12, E-preuve, E13 et Calibration à toute réfutation quantitative immédiate de leur dimensionnement : la cohérence interne entre son budget (§ d) et ses critères (§ b) est invérifiable par omission paramétrique.

2. **Asymétrie et confusion de mécanisme dans le contrôle de pression de E13 (Divergence 3) :**
   Pour résoudre la divergence 3, D propose un « calcul sans dépense sur journaux existants : exposition au crédit partagé, ampleur des mises à jour et gain tenu à l'écart ».
   - *Variable confondante :* l'ampleur des mises à jour des poids ($\|\Delta \theta\|_2$ ou divergence KL par pas) mesure l'intensité globale du pas d'optimisation (qui dépend du taux d'apprentissage $\eta$ et de la variance du gradient), mais est **aveugle au signe et à la direction de l'attribution du crédit**. Un entraînement avec des gradients de forte norme mais purement bruyants (ou dominés par la tâche individuelle) présentera une forte « ampleur des mises à jour » et un « gain tenu à l'écart », tout en ayant une pression collective nulle sur les comportements de coordination ou de signalement. Ce proxy mécanique confond intensité cinétique de l'optimiseur et pression incitative du partage de crédit.

3. **Biais d'atténuation dans la formule d'amortissement $K^*$ (Divergence 8) :**
   D cède à C en écrivant la formule du seuil de rentabilité :
   $$K^* = \frac{G_{\text{gen}} - G_{\text{cat}}}{\lambda_{\text{cat}} - \lambda_{\text{gen}}}$$
   Or, cette équation suppose que le moniteur généré et le moniteur du catalogue ont **exactement le même rappel et le même taux de fausses alertes** sur l'oracle, ne différant que par leurs coûts d'exécution par usage $\lambda_{\text{cat}}$ et $\lambda_{\text{gen}}$. Mais l'objet même de la couche 3 (et du duel E12 de D) est le cas où le moniteur généré capture un *résidu de détection* $\Delta R > 0$ que le catalogue manque ($\lambda_{\text{cat}}$ ne peut pas l'acheter s'il est contraint au catalogue). Si $\lambda_{\text{gen}} \ge \lambda_{\text{cat}}$ (un opérateur synthétisé par code est plus coûteux à exécuter qu'une règle simple du catalogue), le dénominateur $\lambda_{\text{cat}} - \lambda_{\text{gen}}$ est négatif ou nul : la formule de D conclut qu'il « n'existe aucun seuil rentable », même pour un moniteur qui détecte $100\%$ des menaces manquées par le catalogue. La formule omet le terme de valeur de détection $\Delta R$ au dénominateur.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité (lois, paramètres, estimateurs)

1. **Incompatibilité des bornes de décision $\delta$ et $\varepsilon$ dans E12, E-preuve et E13 :**
   Dans E12, D exige pour valider $\mathcal{H}_B$ (gain) que « la borne inférieure [de l'intervalle de confiance de $\hat{\Delta}$] dépasse $\delta$ », et pour valider $\mathcal{H}_A$ (équivalence) que l'intervalle soit « dans $\pm \varepsilon$ ».
   Soit $\hat{\Delta}$ un estimateur asymptotiquement normal $\mathcal{N}(\Delta, \text{SE}^2)$ et $I_{1-2\alpha} = [\hat{\Delta} - z_{1-\alpha}\text{SE}, \, \hat{\Delta} + z_{1-\alpha}\text{SE}]$.
   - Pour que les régions de rejet de $\mathcal{H}_A$ et $\mathcal{H}_B$ puissent couvrir l'espace sans « zone intermédiaire de sous-puissance déclarée » systématique lorsque $\Delta = 0$ ou $\Delta = \delta$, il faut non seulement $\varepsilon \le \delta$, mais surtout que l'erreur standard vérifie :
     $$\text{SE} \le \frac{\varepsilon}{z_{1-\alpha} + z_{1-\beta}}$$
   - Dans E13, l'unité d'inférence est la graine ($k \ge 2$ selon § d : « au moins deux graines »). L'erreur standard de l'écart entre bras est $\text{SE} = \sqrt{\frac{2(\tau^2 + \sigma_w^2/n)}{k}}$. Pour $k = 2$, le quantile de Student à $\alpha = 0,05$ est $t_{0,95; 1} = 6,314$. La demi-largeur de l'intervalle de confiance est $6,314 \times \text{SE}$. Même si $\text{SE} = 0,03$ (3 points de pourcentage), la demi-largeur vaut $0,19$ ($19$ points). Il est mathématiquement impossible d'établir une équivalence dans une marge raisonnable $\varepsilon \le 0,10$ avec $k = 2$ graines : le duel E13 de D tombera dans la « zone intermédiaire » avec une probabilité proche de $1$ sous $\mathcal{H}_A$.

2. **Perte de puissance au point de fonctionnement primaire dans « Calibration » :**
   D choisit comme métrique primaire le « rappel au point de fonctionnement primaire » (détection d'erreur à taux de fausse alerte fixe $\alpha_0 = F_{\max}$).
   Soit $\hat{\tau}$ le quantile empirique d'ordre $1 - \alpha_0$ des scores sur les $n_0$ cas honnêtes (verdicts corrects), et $\hat{R}(\hat{\tau})$ le rappel empirique sur les $n_1$ cas positifs (verdicts faux). Par la méthode delta (théorème de Bahadur), la variance asymptotique de l'estimateur du rappel à taux de fausse alerte estimé est :
   $$\text{Var}(\hat{R}(\hat{\tau})) = \frac{R(\tau)(1-R(\tau))}{n_1} + \left(\frac{f_1(\tau)}{f_0(\tau)}\right)^2 \frac{\alpha_0(1-\alpha_0)}{n_0}$$
   où $f_1(\tau)$ et $f_0(\tau)$ sont les densités des scores en $\tau$. Lorsque les scores du juge sont discrets ou fortement concentrés près du seuil $\tau$ ($f_0(\tau)$ petit tandis que $f_1(\tau)$ est grand, ou paliers ex-aequo), le facteur d'inflation $\left(f_1(\tau)/f_0(\tau)\right)^2$ diverge. La variance de $\hat{R}(\hat{\tau})$ explose alors par rapport à une métrique intégrée (Brier ou AUROC), rendant la différence $\hat{R}_{\text{RLCR}} - \hat{R}_{\text{post-hoc}}$ non significative sur des partitions par familles tenues à l'écart.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Dans le contrôle de pression de E13 (Divergence 3) :** Un contrôle de **gradient / mise à jour sous récompense de groupe permutée entre groupes indépendants**. Puisque D mesure « l'ampleur des mises à jour » pour attester de la pression, il est fatal de ne pas vérifier que cette ampleur diffère de celle produite par une récompense aléatoire de même variance marginale (qui modifie les poids tout autant sans aucun signal de crédit collectif).
2. **Dans le dispositif « qui lit » (§ 3) :** Un **contrôle d'aveuglement du lecteur humain au bras et au gain d'utilité au moment de statuer sur un incident ambigu ou une reprise**. D exige que le collecteur consigne « bras, graine, [...] utilité, valeur des seuils et décision du lecteur » dans le même enregistrement. Si le lecteur humain responsable voit que le bras est « collectif » et que « l'utilité est très élevée » avant de décider de la reprise après suspension, sa décision est contaminée par un biais de confirmation et de arbitrage utilité/sécurité qu'il s'était pourtant interdit en E13-2.

---

## Sur la proposition E

### (a) Défauts de méthode : variables confondantes, vrai par construction, fuites

1. **Confusion entre règle de décision statistique et test d'équivalence (Section D, « Règle commune ») :**
   E pose une règle unique pour tous ses duels : « $\mathcal{H}_A : d \ge \delta$. $\mathcal{H}_B : d < \delta$, avec $\delta = 5$ points, illustratif. [...] Une borne d'incertitude entièrement d'un côté du seuil réfute l'hypothèse opposée [...] si elle traverse le seuil, le résultat est inconclusif ».
   Bien que mathématiquement propre (équivalent à deux tests unilatéraux au seuil $\delta$), ce paramétrage à seuil ponctuel unique $\delta = 5$ points confond **pertinence minimale d'un effet ($\delta$)** et **absence d'effet ($0$)**.
   - Dans le Duel « crédit », si l'augmentation réelle des omissions sous crédit collectif est de $d = +4,5$ points avec un intervalle de confiance très précis $[+4,1 ; +4,9]$ points (par exemple sur un grand échantillon), la borne supérieure est $< 5$ points : la règle de E **réfute $\mathcal{H}_A$** et valide $\mathcal{H}_B$, concluant que le crédit collectif ne pose pas le problème testé, alors même qu'une dégradation causale de $+4,5$ points est statistiquement démontrée ($> 0$ avec certitude). Fixer la frontière de sécurité à $\delta = 5$ points au lieu de tester la supériorité à $0$ et l'équivalence à $\varepsilon$ permet de blanchir toute dégradation réelle comprise entre $0$ et $\delta$.

2. **Fuite de complexité de traduction et variable confondante humaine dans le Duel « preuve » :**
   E définit la métrique du Duel « preuve » comme le « gain de détection des défauts de l'énoncé initial, à budget humain et matériel égal », en comptant « traductions erronées, abstentions et délais dépassés ».
   - *Variable confondante :* en incluant le temps et les erreurs de traduction d'un opérateur humain (ou d'un agent particulier) dans la métrique primaire, le duel confond la **capacité intrinsèque du vérificateur formel (Lean)** avec la **compétence du traducteur** sur la banque choisie. Si le traducteur échoue à formaliser dans le délai imparti (« délai dépassé » compté comme échec), E réfute $\mathcal{H}_A$ (l'apport de la preuve formelle), alors qu'un vérificateur externe appliqué uniquement aux lemmes déjà formalisés ou assisté d'un meilleur traducteur aurait détecté le défaut.

3. **Erreur d'appariement sur le Duel « transfert » (comparaison non ceteris paribus) :**
   E mesure la « perte de rappel $L$ de la sonde transférée face à une sonde réapprise sur le modèle cible, au même plafond de fausses alertes ».
   - *Défaut de méthode :* la perte $L = R_{\text{cible}}(\text{sonde cible}) - R_{\text{cible}}(\text{sonde source})$ dépend de la qualité de la sonde réapprise sur le modèle cible. Si, sur le modèle cible, le signal interne d'omission est faible ou bruité, la sonde réapprise sur la cible aura un rappel médiocre (par exemple $R_{\text{cible}}(\text{sonde cible}) = 0,12$ pour un taux de fausses alertes de $5\%$), et une sonde transférée quasi nulle ($R = 0,08$) donnera une perte $L = 4$ points $\le \varepsilon = 5$ points. La règle de E **réfute $\mathcal{H}_B$ et valide $\mathcal{H}_A$ (le transfert réussit)** simplement parce que les deux sondes échouent pareillement sur le modèle cible ! Évaluer uniquement la perte relative $L$ sans imposer un plancher absolu de rappel à la sonde transférée valide le transfert d'un instrument aveugle.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité (lois, paramètres, estimateurs)

1. **Probabilité égale à $1$ d'issue « inconclusive » autour de $\delta$ à budget fixe :**
   Soit $\hat{d} \sim \mathcal{N}(d, \text{SE}^2)$ l'estimateur de l'effet dans l'un des cinq duels de E, et $I_{1-2\alpha} = [\hat{d} - z_{1-\alpha}\text{SE}, \, \hat{d} + z_{1-\alpha}\text{SE}]$ l'intervalle d'incertitude. La probabilité que le duel tranche (réfute $\mathcal{H}_A$ ou réfute $\mathcal{H}_B$) est :
   $$\mathbb{P}(\text{tranché} \mid d) = \Phi\left(\frac{d - \delta}{\text{SE}} - z_{1-\alpha}\right) + \Phi\left(\frac{\delta - d}{\text{SE}} - z_{1-\alpha}\right)$$
   - Lorsque la vraie valeur $d$ est proche du seuil arbitraire $\delta$ ($|d - \delta| < z_{1-\alpha}\text{SE}$), la probabilité d'obtenir un verdict tranché est bornée supérieurement par $2\Phi(0) - \text{couverture} \le 2\alpha$ (en $d = \delta$, $\mathbb{P}(\text{tranché}) = 2\alpha = 0,10$ pour $\alpha = 0,05$, soit **$90\%$ de résultats inconclusifs** quelle que soit la taille d'échantillon !).
   - Plus généralement, dans le Duel « crédit » avec $k = 6$ répétitions par bras (§ G, illustratif) et $N_{\text{occ}} = 200$ occasions, si la vraie dégradation est nulle ($d = 0$) et que l'écart-type inter-graines est $\tau = 0,04$ ($4$ points) avec bruit binomial intra-graine $\sigma_w = \sqrt{0,25/200} \approx 0,035$, alors $\text{SE} = \sqrt{\frac{2(0,04^2 + 0,035^2)}{6}} \approx 0,031$. Avec un test de Student à $2k-2 = 10$ degrés de liberté ($t_{0,95; 10} = 1,812$), la marge d'incertitude est $1,812 \times 0,031 = 0,056 > \delta = 0,05$. Même pour un effet réel nul ($d = 0$), la puissance pour réfuter $\mathcal{H}_A$ ($d \ge 0,05$) n'est que de $\Phi\left(\frac{0,05}{0,031} - 1,812\right) \approx \Phi(-0,20) \approx 0,42$. L'enveloppe de $6$ répétitions de E a plus d'une chance sur deux d'être non concluante même sous l'hypothèse nulle stricte $d=0$.

2. **Biais de sélection par troncature des cas « non évaluables » (Section E) :**
   E définit : « Détection = événements positifs détectés / événements positifs évaluables ; [...] Les cas non évaluables ont leur propre taux, jamais absorbé dans les négatifs. »
   Soit $E \in \{0, 1\}$ l'indicatrice qu'un cas positif ($Y=1$) soit jugé « évaluable » par l'adjudicateur, et $D \in \{0, 1\}$ la détection. L'estimateur de E cible la probabilité conditionnelle $\theta_{\text{cond}} = \mathbb{P}(D=1 \mid Y=1, E=1)$ au lieu de la probabilité marginale $\theta = \mathbb{P}(D=1 \mid Y=1)$. Par la formule des probabilités totales :
   $$\theta_{\text{cond}} - \theta = (1 - \mathbb{P}(E=1 \mid Y=1)) \big(\mathbb{P}(D=1 \mid Y=1, E=1) - \mathbb{P}(D=1 \mid Y=1, E=0)\big)$$
   Dans un duel entre deux bras (par exemple collectif vs individuel, ou sonde vs journal), si le traitement affecte la lisibilité de la trace (par exemple par contraction télégraphique du raisonnement, RAPPORTÉ), alors $\mathbb{P}(E=1 \mid Y=1)$ dépend du bras. Un agent qui brouille sa trace pour la rendre « non évaluable » lors de ses omissions ($E=0$ quand $D=0$) fait tendre $\mathbb{P}(D=1 \mid Y=1, E=1)$ vers $1$. L'estimateur conditionnel de E est alors sévèrement biaisé vers le haut (biais de collisionneur / troncature endogène) dès que $\text{Cov}(D, E \mid Y=1) \neq 0$ et $\mathbb{P}(E=0 \mid Y=1) > 0$.

3. **Variance du Duel « confiance » (gain de détection à taux de rejet des corrects fixe) :**
   C'est le problème dual de celui de D : E fixe le taux de rejet des verdicts corrects ($\alpha_0$) et mesure le rappel des verdicts incorrects. Lorsque la proportion de verdicts incorrects du juge $p_{\text{err}}$ est faible (par exemple un juge de frontière ayant $p_{\text{err}} \le 0,10$ sur une famille donnée), sur une partition de test de $N_f = 100$ fiches, le dénominateur des positifs est $n_1 \approx 10$. La variance binomiale minimale $\frac{R(1-R)}{n_1}$ vaut alors $\approx 0,025$ (écart-type de $15,8$ points), rendant un seuil de $\delta = 5$ points mathématiquement indétectable sans plusieurs milliers de fiches étiquetées par l'oracle.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Dans la gestion des cas « non évaluables » (Section E) :** Une **analyse de sensibilité aux bornes de Manski (pire cas où tous les cas « non évaluables » du bras traité sont comptés comme des échecs / omissions, contre meilleur cas)**. Sans ce contrôle négatif bornant l'estimateur, exclure les cas non évaluables du dénominateur récompense mécaniquement tout agent ou toute sonde qui produit des sorties illisibles sur les cas difficiles.
2. **Dans le Duel « transfert » (Section D) :** Un **seuil minimal de performance absolue sur le modèle cible ($R_{\text{cible}}(\text{sonde transférée}) \ge R_{\min} > \text{FPR}$)** conjointement à la borne sur la perte $L \le \varepsilon$. Sans ce contrôle, $L \approx 0$ est validé lorsque la sonde source et la sonde cible ont toutes deux un pouvoir discriminant nul sur le modèle cible.
3. **Dans le Duel « crédit » :** Un contrôle positif de **sensibilité de la métrique à une pression effective (ou un bras à récompense de groupe permutée)**. E critique à juste titre en Section A le fait qu'un gain de tâche ne démontre pas la pression pertinente, mais son propre Duel « crédit » (Section D) ne contient **aucun contrôle de pression** : si le régime hors ligne choisi par E n'exerce aucune pression sur le canal collectif, on obtient $d \approx 0 < \delta$, et la règle de E réfute $\mathcal{H}_A$ à tort par défaut d'exposition au traitement.

FIN-DE-CELLULE
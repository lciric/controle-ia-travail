## (a) Ce que la question suppose sans que ce soit établi

- **1(b) Étanchéité informationnelle** : Le banc d'évaluation simulé en version informée de la défense peut être paramétré par les seuils et le protocole de la défense sans fuite inverse vers les concepteurs de la défense ni besoin d'agent opérationnel — **HYPOTHÈSE**.
- **1(b) Parallélisme des versions** : Les deux versions du banc d'évaluation (aveugle et informée de la défense, VÉRIFIÉ, fait 1) peuvent évaluer exactement les mêmes schémas de familles sans modifier leur validité — **HYPOTHÈSE**.
- **1(c) Loi d'échantillonnage** : Le processus de découverte des familles par énumération par des modèles suit une loi de probabilité stationnaire assimilable à un tirage pondéré sur une population bien définie — **HYPOTHÈSE** (contredite pour le tirage uniforme par le fait 9, VÉRIFIÉ).
- **1(c) Décomposition de la variance** : La performance d'une défense se décompose proprement selon un modèle hiérarchique à deux niveaux (variance inter-familles et variance intra-famille sur les éléments) — **HYPOTHÈSE**.
- **1(d) Clôture et granularité** : L'ensemble des familles possibles forme une population finie, discrète et fermée $N$ à une échelle de granularité objective — **HYPOTHÈSE** (mise en doute par la fusion 1-pour-2 observée, VÉRIFIÉ, faits 5 et 7).
- **1(d) Indépendance des captures** : Les sources énumérant les familles (Argon, Opus 5.5 et les cinq instances prévues, VÉRIFIÉ fait 5 et RAPPORTÉ fait 4) ont des probabilités de découverte mutuellement indépendantes conditionnellement à la consigne — **HYPOTHÈSE**.
- **1(d) Homogénéité de capture** : Toutes les familles ont la même probabilité d'être énumérées par une source donnée — **HYPOTHÈSE**.
- **1(d) Exactitude de l'appariement** : Un lecteur armé d'une grille fermée identifie sans faux positifs ni faux négatifs les équivalences entre schémas de familles — **HYPOTHÈSE** (fragilisée par le biais de lignée du lecteur unique Sonnet 5.5, VÉRIFIÉ, fait 6).

---

## (b) Expériences décisives en duel $H_A$ contre $H_B$

### Duel 1 — Biais des estimateurs de cardinalité sous hétérogénéité et dépendance ($K = 5$ sources)
* **$H_A$ (Équiprobabilité et indépendance — modèle log-linéaire sans interaction $M_t$)** : L'hétérogénéité de visibilité des familles et la corrélation inter-modèles sont négligeables ; l'estimateur de Darroch ($M_t$, extension multi-sources de Lincoln-Petersen) estime la taille de la population $N$ sans biais négatif sévère.
* **$H_B$ (Hétérogénéité et dépendance — borne inférieure de Chao1 / modèle $M_{th}$)** : Les familles ont des probabilités de découverte très inégales (loi Bêta ou Zipf) et les sources sont positivement corrélées ; $M_t$ sous-estime fortement $N$, tandis que l'estimateur de Chao (Chao, 1984, *Nonparametric Estimation of the Number of Classes in a Population*) ou un modèle log-linéaire avec effets d'hétérogénéité ($M_{th}$) réduit ce biais et maintient la couverture nominale.
* **Protocole et métrique** : Sur un banc de $1\,000$ mondes simulés (illustratif) de taille vraie $N = 100$ familles (illustratif) où $K = 5$ sources (RAPPORTÉ, fait 4) tirent des familles avec probabilités $p_{ij} \sim \text{Beta}(0,5 ; 2,0)$ corrélées entre sources ($\rho = 0,40$, illustratif), on mesure le biais relatif moyen $\text{BR} = \mathbb{E}[(\hat{N} - N)/N]$ et le taux de couverture empirique de l'intervalle de confiance à $95\%$ (illustratif).
* **Seuil** : $|\text{BR}| \le 0,10$ et couverture $\ge 0,90$ (illustratifs).
* **Contrôle négatif** : Monde simulé uniforme indépendant ($p_{ij} = 0,40$ constant, $\rho = 0$, illustratif) où $M_t$ et Chao1 doivent tous deux vérifier $|\text{BR}| \le 0,03$ et couverture $\ge 0,94$ (illustratifs).
* **Issue qui falsifie chaque hypothèse** : Si sous le monde hétérogène corrélé, $M_t$ affiche $\text{BR} < -0,15$ ou une couverture $< 0,80$ alors que Chao1/$M_{th}$ borne validement $N$ (couverture de la borne inférieure $\ge 0,90$, illustratif), $H_A$ est falsifiée. Si $M_t$ maintient $|\text{BR}| \le 0,10$ et une couverture $\ge 0,90$ sans que $M_{th}$ n'améliore la couverture, $H_B$ est falsifiée.

### Duel 2 — Validité de la borne à zéro échec sous découverte pondérée par la taille
* **$H_A$ (Validité de la borne binomiale naïve)** : Le calcul à zéro échec $n \ge \ln(0,05)/\ln(1-\varepsilon)$ (soit $n = 29$ pour $\varepsilon = 0,10$, VÉRIFIÉ, fait 9) garantit au seuil de confiance $95\%$ que la proportion en cardinalité de familles où la défense échoue dans la population totale $N$ est inférieure à $\varepsilon$, même lorsque les familles sont découvertes sans remise selon une loi de visibilité $w_i$ inégale.
* **$H_B$ (Biais de découverte — nécessité d'une pondération de Horvitz-Thompson ou d'un déficit de couverture Good-Turing)** : Les familles à faible visibilité $w_i$ sont sur-représentées dans le reste non découvert et présentent un taux d'échec plus élevé ; la borne binomiale à $n = 29$ viole sa garantie nominale, et seul un estimateur corrigé par la masse manquante de Good-Turing $\hat{p}_0 = f_1 / M$ (Good, 1953, *The Population Frequencies of Species and the Estimation of Population Parameters*) et les probabilités d'inclusion $\hat{\pi}_i$ préserve le niveau $1 - \alpha$.
* **Protocole et métrique** : Sur $1\,000$ mondes simulés (illustratif) de $N = 150$ familles (illustratif) avec visibilités $w_i \propto i^{-1}$ (loi de Zipf, illustratif) où une proportion vraie $\varepsilon_{\text{vrai}} = 0,15 > 0,10$ (illustratif) des familles (concentrée dans le décile de plus faible visibilité $w_i$) met la défense en échec, on tire $n = 29$ familles sans remise proportionnellement à $w_i$. Métrique : taux d'erreur de type I empirique $\hat{\alpha}$ (fréquence à laquelle les $29$ familles tirées ont $0$ échec, concluant à tort $\varepsilon \le 0,10$).
* **Seuil** : $\hat{\alpha} \le 0,05$ (nominal, VÉRIFIÉ, fait 9).
* **Contrôle négatif** : Échantillonnage aléatoire simple uniforme ($w_i = 1/N$) avec $\varepsilon_{\text{vrai}} = 0,15$, où $\hat{\alpha}$ doit être $\le (1 - 0,15)^{29} \approx 0,009 < 0,05$ (calcul refaisable, illustratif).
* **Issue qui falsifie chaque hypothèse** : Si sous tirage Zipf, $\hat{\alpha} > 0,10$ (illustratif) pour la règle binomiale naïve alors que la règle augmentée de la masse manquante $\hat{\varepsilon}_{\text{corr}} = \varepsilon_{\text{binomial}} + \hat{p}_0$ maintient $\hat{\alpha} \le 0,05$, $H_A$ est falsifiée. Si la règle naïve maintient $\hat{\alpha} \le 0,05$ sous tous les régimes d'anti-corrélation visibilité/échec testés, $H_B$ est falsifiée.

### Duel 3 — Biais de lignée et non-bijectivité dans l'appariement de familles
* **$H_A$ (Suffisance du lecteur unique à grille fermée)** : Un lecteur unique de la même lignée qu'une des sources (comme Sonnet 5.5 pour Opus 5.5, VÉRIFIÉ, fait 6) produit un graphe d'intersection dont l'estimateur de Chapman $\hat{N}$ ne diffère pas significativement de celui d'un jury multi-fournisseurs aveuglé résolvant la granularité par partitionnement de graphe.
* **$H_B$ (Distorsion par lignée et granularité asymétrique)** : Le lecteur de même lignée sur-apparie ou segmente plus finement les familles de sa propre lignée (expliquant l'écart $m = 18$ contre $m = 19$, VÉRIFIÉ, fait 7), ce qui déplace $\hat{N}$ au-delà de l'erreur d'échantillonnage par rapport à un jury croisé de $3$ lecteurs de fournisseurs distincts sur textes anonymisés.
* **Protocole et métrique** : Sur les $28 + 25 = 53$ descriptions brutes des deux sources (VÉRIFIÉ, fait 5) anonymisées et réordonnées, faire construire la matrice d'adjacence par $J = 3$ modèles de fournisseurs différents (illustratif). Métrique : statistique $\kappa$ de Fleiss inter-juges et écart absolu $|\hat{N}_{\text{unique}} - \hat{N}_{\text{jury}}|$.
* **Seuil** : $|\hat{N}_{\text{unique}} - \hat{N}_{\text{jury}}| \le 2,0$ familles et asymétrie de recouvrement $\Delta m = |m_{1\to 2} - m_{2\to 1}| = 0$ après réduction canonique des composantes connexes (illustratifs).
* **Contrôle négatif** : Paires de descriptions dupliquées synthétiquement (synonymes stricts) et paires disjointes injectées dans le lot, où les deux protocoles doivent atteindre un rappel et une précision $\ge 0,98$ (illustratif).
* **Issue qui falsifie chaque hypothèse** : Si $|\hat{N}_{\text{unique}} - \hat{N}_{\text{jury}}| > 2,0$ ou si le taux de fusion $1$-vers-$2$ diffère significativement selon la lignée du lecteur ($p < 0,05$ au test exact de Fisher, illustratif), $H_A$ est falsifiée. Dans le cas contraire, $H_B$ est falsifiée.

---

## (c) Mesure minimale de chaque instrument nommé

Les instruments nommés dans la question (au niveau méthodologique et statistique) sont : (1) l'**estimateur du nombre total de familles** $\hat{N}$ (et de la masse manquante $\hat{p}_0$), et (2) la **mesure d'universalité** $\hat{U}$ (statistique de décision certifiant la défense sur l'ensemble des familles, appuyée sur les scores des sondes sur activations internes, des moniteurs boîte noire et de leur agrégateur séquentiel).

| Instrument statistique | Cas « honnêtes » appariés (mondes nuls / conformes) | Taux de détection (puissance) et de fausses alertes (calibrage) minimaux | Vérification mécanique (base naïve) à battre |
|---|---|---|---|
| **1. Estimateur de cardinalité $\hat{N}$ et de couverture $\hat{C}$** (Chao1 / modèle log-linéaire sur $K$ sources) | Mondes simulés à vérité terrain connue $N \in [35, 200]$ (illustratif) où la couverture réelle atteinte par l'union des sources est suffisante ($C_{\text{vrai}} \ge 0,90$, illustratif). | **Détection (sous-couverture)** : identifier avec puissance $\ge 0,85$ (illustratif) les mondes où la part de familles non vues dépasse $1 - C_{\text{vrai}} > 0,10$. **Fausse alerte** : déclarer à tort une couverture insuffisante dans $\le 0,05$ des mondes bien couverts (illustratif) ; couverture de l'IC à $95\%$ sur $N$ comprise entre $0,92$ et $0,98$ (illustratif). | **Comptage brut des familles observées** $S_{\text{obs}} = |\bigcup_{k=1}^K S_k|$ (soit $34$ ou $35$ sur les données de départ, VÉRIFIÉ, fait 7) et estimateur de Lincoln-Petersen non corrigé de l'hétérogénéité. |
| **2. Mesure d'universalité $\hat{U}_{\varepsilon, \tau, \alpha}$** (borne supérieure de confiance $1-\alpha$ sur la proportion de familles où le rappel de la défense au seuil de fausse alerte $\alpha_{\text{FA}}$ est $< \tau$) | Trajectoires sans sabotage diffus appariées par domaine, longueur et distribution de tokens (issues des mêmes modèles $8\text{B}$ et $70\text{B}$, RAPPORTÉ, fait 3), servant à calibrer le seuil de fausse alerte $\alpha_{\text{FA}}$ des sondes, moniteurs et de l'agrégateur séquentiel. | **Calibration sur cas honnêtes** : taux de fausses alertes empirique sur trajectoires honnêtes tenues à l'écart $\le \alpha_{\text{FA}} = 0,01$ (illustratif, écart $\le 0,002$). **Détection d'univers non universels** : rejeter l'universalité dans $\ge 0,95$ des mondes simulés où la proportion vraie de familles défaillantes est $\varepsilon_{\text{vrai}} > \varepsilon = 0,05$, tout en acceptant à tort l'universalité dans $\le \alpha = 0,05$ des cas (illustratifs). | **Moyenne globale non stratifiée** du taux de détection sur l'ensemble des trajectoires fusionnées (qui masque l'échec complet sur des familles rares mais petites en nombre d'éléments) et **écart simple vues / tenues à l'écart** sans borne sur la masse manquante. |

---

## Bloc 1 — Quatre propositions préalables

### (a) Définition opérationnelle de l'universalité

Soit $\mathcal{F}$ une classe de familles, $\mathcal{D}$ la loi de découverte sur $\mathcal{F}$, et $M(f) \in [0,1]$ la performance de la défense sur la famille $f \in \mathcal{F}$ (définie comme la probabilité de détection sur les éléments de $f$ lorsque le seuil de la défense est calibré pour un taux de fausses alertes $\le \alpha_{\text{FA}}$ sur des éléments honnêtes appariés).

1. **Pire cas sur une classe déclarée ($\min_{f \in \mathcal{F}} M(f) \ge \tau$)** :
   * *À déclarer d'avance* : la grammaire formelle définissant $\mathcal{F}$, le seuil d'efficacité par famille $\tau$, le taux de fausses alertes $\alpha_{\text{FA}}$.
   * *Énoncé autorisé* : $\forall f \in \mathcal{F}_{\text{observé}}, \hat{M}(f) \ge \tau - \delta_n$ (avec confiance $1-\alpha$ sur le tirage des éléments intra-famille).
   * *Non autorisé* : toute garantie sur $\mathcal{F} \setminus \mathcal{F}_{\text{observé}}$ sans énumération exhaustive prouvée de $\mathcal{F}$ (impossible si $\mathcal{F}$ est ouverte).
   * *Vérification par un tiers* : rejouer la défense figée sur chaque $f$ et vérifier le minimum empirique.
2. **Écart de généralisation entre familles vues ($\mathcal{F}_{\text{vu}}$) et tenues à l'écart ($\mathcal{F}_{\text{écart}}$)** :
   * *À déclarer d'avance* : le protocole de scellement de $\mathcal{F}_{\text{écart}}$ (VÉRIFIÉ, fait 1 ; RAPPORTÉ, fait 4) et la tolérance d'écart $\Delta_{\max}$.
   * *Énoncé autorisé* : $|\mathbb{E}_{f \sim \mathcal{D}_{\text{vu}}}[M(f)] - \mathbb{E}_{f \sim \mathcal{D}_{\text{écart}}}[M(f)]| \le \Delta_{\max}$ avec confiance $1-\alpha$.
   * *Non autorisé* : affirmer que la défense fonctionne dans l'absolu (elle peut être uniformément médiocre sur les deux ensembles) ou sur des familles hors de la loi des générateurs.
   * *Vérification par un tiers* : vérifier les empreintes cryptographiques d'horodatage de la défense avant ouverture des scellés de $\mathcal{F}_{\text{écart}}$, puis calculer la différence des moyennes.
3. **Quantile / proportion de familles satisfaisant un seuil ($\text{PAC-familles}$)** :
   * *À déclarer d'avance* : $\tau$ (seuil de réussite d'une famille), $\varepsilon$ (proportion maximale de familles défaillantes tolérée), $1-\alpha$ (confiance), et la loi d'échantillonnage $\mathcal{D}$.
   * *Énoncé autorisé* : $\mathbb{P}_{\mathcal{D}}\big( \mathbb{P}_{f \sim \mathcal{D}}(M(f) < \tau) \le \varepsilon \big) \ge 1 - \alpha$.
   * *Non autorisé* : garantir la performance sous un changement de distribution ($\mathcal{D}' \neq \mathcal{D}$), car les familles sont découvertes et non tirées uniformément (VÉRIFIÉ, fait 9).
   * *Vérification par un tiers* : compter le nombre de familles $k$ où $\hat{M}(f) < \tau$ parmi les $n$ familles tenues à l'écart et vérifier la borne de Clopper-Pearson.
4. **Autre (recommandée) — Proportion certifiée corrigée de la masse manquante (PAC-Good-Turing)** :
   * *Définition* : on borne la probabilité totale d'échec en combinant l'échec sur les familles découvertes et la masse de probabilité des familles non encore découvertes $\hat{p}_0 = f_1 / \sum_{k} n_k$ (où $f_1$ est le nombre de familles vues par une seule source) : $\hat{\varepsilon}_{\text{tot}} = (1 - \hat{p}_0)\hat{\varepsilon}_{\text{obs}} + \hat{p}_0 \cdot 1 \le \varepsilon_{\text{tot}}$.
   * *Séparation fondamentale* : « **Universelle sur la classe déclarée** » est une propriété interne à la mesure $\mathcal{D}$ des générateurs connus ($\hat{\varepsilon}_{\text{obs}} \le \varepsilon$) ; « **Robuste à l'inconnu** » exige en outre que la masse manquante $\hat{p}_0$ estimée par capture-recapture multi-sources soit bornée ($\hat{p}_0 \le \varepsilon_0$) et que le déficit de performance sur les singletons ($f_1$, familles les plus rares) ne diverge pas par rapport aux familles communes ($f_{\ge 2}$).

### (b) Régime d'information de l'évaluation

Conformément à la décision N-056 (VÉRIFIÉ, fait 1), le banc d'évaluation adverse simulé est monté en deux versions sans dépense d'agent opérationnel (RAPPORTÉ, fait 2) :

| Paramètre du banc | Palier 1 : Régime Aveugle | Palier 2 : Régime Informé de la défense |
|---|---|---|
| **Existence de la défense** | Connue uniquement en tant que principe général (présence d'un contrôle). | Connue (architecture sonde + moniteur texte + agrégation séquentielle). |
| **Liste des familles vues ($\mathcal{F}_{\text{vu}}$)** | Inaccessible aux instances générant $\mathcal{F}_{\text{écart}}$. | Accessible uniquement pour exclure les doublons après scellement, ou pour paramétrer les variantes d'évaluation. |
| **Protocole et nature des signaux** | Inconnus du générateur d'éléments d'évaluation. | Connus (quelles couches d'activations sont lues, quelle fenêtre de texte est lue par le moniteur, quelle règle d'agrégation séquentielle est appliquée). |
| **Seuils exacts ($\tau, \alpha_{\text{FA}}$) et poids des sondes** | Strictement inconnus. | Seuils d'alerte par étape connus du simulateur de trajectoires ; poids exacts des sondes tenus secrets (ou exposés en sous-palier 2b pour tester l'invariance du sous-espace). |

* **Budget d'évaluation** : Fixé d'avance dans le préenregistrement en (i) nombre de familles $n$, (ii) nombre d'éléments (trajectoires) $m$ par famille, (iii) nombre de jetons (tokens) et d'étapes séquentielles par trajectoire, et (iv) budget de calcul en FLOPs par modèle ($8\text{B}$ et $70\text{B}$, RAPPORTÉ, fait 3).
* **Rapport par palier** : Le rapport publie séparément la courbe ROC/rappel au Palier 1 et au Palier 2, ainsi que la chute de performance $\Delta M(f) = M_{\text{aveugle}}(f) - M_{\text{informé}}(f)$ par famille.
* **Cloisonnement strict (interdictions)** : Il est interdit de partager des descriptions, statistiques, gradients, erreurs ou identifiants de $\mathcal{F}_{\text{écart}}$ vers l'équipe de conception ou d'entraînement des sondes/moniteurs avant le gel cryptographique définitif du code et des seuils de la défense (VÉRIFIÉ, fait 1 ; RAPPORTÉ, fait 4). Un mode complet est tenu à l'écart de la conception des moniteurs (décision N-054, VÉRIFIÉ, fait 1). Toute ré-optimisation des seuils après lecture de $\mathcal{F}_{\text{écart}}$ invalide le certificat et rétrograde les familles de $\mathcal{F}_{\text{écart}}$ au statut de $\mathcal{F}_{\text{vu}}$.

### (c) Combien de familles, par simulation

* **Énoncé cible** : Garantir avec confiance $1 - \alpha$ ($95\%$, VÉRIFIÉ, fait 9) que la proportion de familles de la classe où la probabilité de détection de la défense est inférieure à $\tau$ ne dépasse pas $\varepsilon$ : $\mathbb{P}(\mathbb{P}_{f}(M(f) < \tau) \le \varepsilon) \ge 1 - \alpha$.
* **Modèle génératif à deux niveaux et dépendance** :
  1. *Population et découverte* : $N$ familles organisées en $G$ grappes (clusters phylogénétiques de familles proches). La famille $i$ de la grappe $g$ a une propension de découverte $w_i \sim \text{Gamma}(a, b)$ et une difficulté latente $\theta_i = \mu + u_g + v_i$, avec $u_g \sim \mathcal{N}(0, \sigma_{\text{grappe}}^2)$ (dépendance entre familles proches) et $v_i \sim \mathcal{N}(0, \sigma_{\text{fam}}^2)$ (variance inter-familles).
  2. *Variance intra-famille* : Pour la famille $i$, on tire $m$ éléments d'évaluation ; le score ou la détection de l'élément $j$ suit $Y_{ij} \sim \text{Bernoulli}(\text{logit}^{-1}(\theta_i))$, d'où une variance intra-famille $\sigma_{\text{intra}, i}^2 = M(f_i)(1 - M(f_i))/m$.
* **Calcul de $n$ et $m$** : Sous tirage indépendant idéal et $\sigma_{\text{intra}}^2 \to 0$, la borne à zéro échec donne $n \ge \ln(0,05)/\ln(1-\varepsilon)$, soit $29$ familles pour $\varepsilon = 0,10$, $59$ pour $\varepsilon = 0,05$ et $149$ pour $\varepsilon = 0,02$ (VÉRIFIÉ, fait 9). En présence de dépendance intra-grappe (corrélation intra-classe $\rho_{\text{grappe}} = \sigma_{\text{grappe}}^2 / (\sigma_{\text{grappe}}^2 + \sigma_{\text{fam}}^2)$) et de poids de découverte inégaux $w_i$, la taille d'échantillon effective est réduite par le facteur d'effet de plan $\text{DEFF} = [1 + (\bar{n}_{\text{grappe}} - 1)\rho_{\text{grappe}}] \cdot (1 + \text{CV}^2(w))$, où $\text{CV}(w)$ est le coefficient de variation des probabilités de découverte. Il faut alors $n_{\text{requis}} \approx n_{\text{binomial}} \times \text{DEFF}$ (par exemple, pour $\varepsilon = 0,10$ et $\text{DEFF} = 1,5$, $n_{\text{requis}} \approx 44$ familles, illustratif) et $m \ge 30$ éléments par famille (illustratif) pour que l'incertitude intra-famille ne domine pas.
* **Règle d'arrêt séquentielle** : Utilisation d'un test séquentiel de rapport de vraisemblance (SPRT de Wald) ou de bornes de confiance valides à tout instant (*always-valid p-values* par martingales de Ville) permettant d'arrêter l'évaluation dès qu'un échec franc ($M(f_i) < \tau$) falsifie la borne à zéro échec, ou de poursuivre jusqu'à un palier préenregistré avec contrôle exact de l'erreur familiale $\alpha$.
* **Analyses de sensibilité et biais de découverte** : Comme les familles sont découvertes et non tirées au hasard (VÉRIFIÉ, fait 9), la simulation fait varier la corrélation $\rho(\theta_i, w_i) \in [-0,8 ; +0,8]$ (illustratif) entre visibilité d'une famille et performance de la défense.
* **Ce que la simulation démontre et ce qu'elle suppose** : La simulation démontre le calibrage (erreur de type I $\le \alpha$) et la puissance de la règle de décision *conditionnellement* à la classe de lois génératives $(\sigma_{\text{grappe}}^2, \sigma_{\text{fam}}^2, \text{CV}(w), \rho(\theta, w))$ explorée ; elle *suppose* (sans pouvoir le prouver par elle-même) que le monde réel des familles appartient à l'enveloppe des paramètres simulés.

### (d) Combien de familles encore inconnues

* **Vérification des calculs (VÉRIFIÉ, faits 7 et 8)** : Avec $n_1 = 28$ (Argon) et $n_2 = 25$ (Opus 5.5) :
  * Convention $m = 18$ (unités d'Argon, $34$ familles observées) : Lincoln-Petersen $\hat{N}_{\text{LP}} = \frac{28 \times 25}{18} = \frac{700}{18} \approx 38,89$ ; Chapman $\hat{N}_{\text{C}} = \frac{(28+1)(25+1)}{18+1} - 1 = \frac{754}{19} - 1 \approx 38,68$.
  * Convention $m = 19$ (unités d'Opus, $35$ familles observées) : Lincoln-Petersen $\hat{N}_{\text{LP}} = \frac{28 \times 25}{19} = \frac{700}{19} \approx 36,84$ ; Chapman $\hat{N}_{\text{C}} = \frac{29 \times 26}{20} - 1 = \frac{754}{20} - 1 = 36,70$.
* **Quelle convention se défend et pourquoi** : Aucune des deux formules brutes n'est algébriquement cohérente telle quelle pour $m=19$, car si l'on adopte la granularité fine d'Opus (où la famille fusionnée d'Argon compte pour $2$ unités), alors $n_1$ exprimé dans cette même unité d'Opus vaut $28 + 1 = 29$ et non $28$ (ce qui donnerait $\hat{N}_{\text{C}}(29, 25, 19) = \frac{30 \times 26}{20} - 1 = 38,0$, calcul refaisable). En conservant $n_1 = 28$ et $n_2 = 25$, **la convention $m = 18$ (quotient par les composantes connexes du graphe biparti d'appariement)** est la seule mathématiquement cohérente : toute paire ou multiplet relié par au moins une arête d'équivalence forme une unique classe d'équivalence canonique, ce qui ramène $n_2$ effectif à $24$ classes ($18$ communes $+ 6$ propres) ou conserve $m = 18$ comme borne plus conservatrice (donnant $\hat{N} \approx 38,7$, soit au moins $4$ à $5$ familles inconnues).
* **Sens des biais lors de la violation des hypothèses** :
  1. *Dépendance positive entre sources* (entraînement sur des corpus web proches, même formulation de la question, VÉRIFIÉ, fait 6) : augmente $m$, donc **sous-estime** $N$ ($\hat{N} < N$).
  2. *Hétérogénéité des probabilités de capture* (certaines familles canoniques sont évidentes pour tous les modèles, d'autres rares) : crée une corrélation positive apparente des captures, donc **sous-estime** $N$ (biais négatif classique de Lincoln-Petersen).
  3. *Erreur d'appariement* : les faux positifs d'appariement (favorisés si le lecteur partage la lignée d'une source, VÉRIFIÉ, fait 6) gonflent $m$ et **sous-estiment** $N$ ; les faux négatifs (oubli d'apparier deux formulations différentes) réduisent $m$ et **surestiment** $N$.
  4. *Population non fermée* : si l'espace des schémas est continu ou dépend de la finesse d'analyse, $N$ n'est pas borné ; $\hat{N}$ ne mesure plus une taille finie, mais l'inverse de l'indice de concentration de Simpson $\left(\sum_i p_i^2\right)^{-1}$ de la loi de génération à la granularité choisie.
* **Estimateurs multi-sources ($K \ge 5$, RAPPORTÉ, fait 4)** :
  * *Bornes inférieures de Chao* (Chao1 en fréquences $N_{\text{Chao1}} = S_{\text{obs}} + \frac{f_1^2}{2 f_2}$ ; Chao2 en incidence sur $K$ sources $N_{\text{Chao2}} = S_{\text{obs}} + \frac{K-1}{K}\frac{Q_1^2}{2 Q_2}$, où $Q_1$ est le nombre de familles vues par exactement $1$ source et $Q_2$ par exactement $2$ sources) : valides comme bornes inférieures sous hétérogénéité arbitraire.
  * *Good-Turing* : estime directement la probabilité totale des familles non encore vues $\hat{p}_0 = Q_1 / \sum_{k=1}^K n_k$ (couverture $\hat{C} = 1 - \hat{p}_0$), qui reste bien définie même si $N = \infty$.
  * *Modèles log-linéaires (Cormack, 1989, Log-linear models for capture-recapture) et classes latentes* : ajustent sur le tableau de contingence $2^K - 1$ des présences/absences des termes d'interaction entre paires de sources $\lambda_{kk'}$ (corrigeant la dépendance) et des mélanges finis (classes latentes d'hétérogénéité).
  * *Approche bayésienne non paramétrique* : processus de Pitman-Yor ou de Dirichlet permettant de prédire la courbe d'accumulation de nouvelles familles pour $K+1, K+2$ sources supplémentaires.
* **Test d'indépendance et traitement du refus commun** :
  * Avec $K \ge 3$ sources, on teste l'indépendance deux à deux conditionnelle en comparant par rapport de vraisemblance (ou critère AIC/BIC) le modèle log-linéaire sans interaction $M_t$ aux modèles avec termes d'interaction $\lambda_{kk'}$ sur les tables $2 \times 2 \times 2$.
  * *Refus commun (censure partagée par les garde-fous de tous les fournisseurs)* : toute famille dont la probabilité de sortie est nulle chez les $K$ fournisseurs ($p_{i1} = \dots = p_{iK} = 0$) appartient à un « zéro structurel » totalement invisible aux données d'énumération des modèles. On ne peut l'estimer qu'en introduisant une $(K+1)$-ième source de nature différente non soumise aux mêmes filtres de génération : la taxonomie extraite des bancs publics académiques (VÉRIFIÉ, fait 10) et l'analyse des journaux de refus passés (RAPPORTÉ, fait 12).

---

## Bloc 2 — Données de départ à recommander

Je recommande par ordre de priorité : **(1) les trajectoires brutes de trois bancs publics externes**, **(2) les propositions brutes d'une course précédente**, et **(3) les journaux de refus de questions passées** (RAPPORTÉ, fait 12). Les données brutes priment sur les résumés car un résumé fige la grille de lecture d'un annotateur unique (reproduisant le biais du fait 6, VÉRIFIÉ) et détruit la variance intra-famille nécessaire au modèle hiérarchique du Bloc 1(c).

### 1. Trois bancs publics candidats (noms VÉRIFIÉ, fait 10 ; propriétés détaillées HYPOTHÈSE, fait 11)
* **ControlArena** (référence à vérifier) :
  * *Propriétés (HYPOTHÈSE, fait 11)* : journaux d'exécution structurés (JSON/trajectoires séquentielles d'appels et de réponses), licence ouverte académique à vérifier, étiquetage natif par scénario et mode d'évaluation qu'il faut projeter sur notre grille de familles.
  * *Indépendance et recouvrement* : forte indépendance vis-à-vis du programme (conçu par des tiers), mais risque moyen à élevé de recouvrement avec les données de pré-entraînement des modèles récents si le dépôt est public avant leur date de coupure.
  * *Coût et usage* : coût de mise au format modéré (normalisation des schémas JSON) ; sert de source externe $K+1$ dans la capture-recapture et de lot de familles extérieures pour le Palier 1.
* **SHADE-Arena** (référence à vérifier) :
  * *Propriétés (HYPOTHÈSE, fait 11)* : trajectoires multi-étapes horodatées avec étiquettes de présence/absence de comportement cible ; licence et format exacts non vérifiés dans les pièces (HYPOTHÈSE).
  * *Indépendance et recouvrement* : indépendant des concepteurs de nos défenses ; risque de contamination des poids ouverts $8\text{B}/70\text{B}$ (RAPPORTÉ, fait 3) mesurable par test de perplexité / détection de n-grammes sur les consignes du banc.
  * *Coût et usage* : coût d'alignement moyen (regroupement des trajectoires en familles homogènes) ; idéal pour calibrer la variance intra-famille $\sigma_{\text{intra}}^2$.
* **Liars' Bench** (cité dans `CLAUDE.md`, décision N-061, VÉRIFIÉ, fait 10 ; référence à vérifier) :
  * *Propriétés (HYPOTHÈSE, fait 11)* : paires ou séquences d'énoncés étiquetées pour l'évaluation de sondes internes et de moniteurs ; je ne connais pas par vérification directe dans les pièces sa licence exacte ni son schéma de fichiers (HYPOTHÈSE, fait 11).
  * *Coût et usage* : coût de formatage faible pour les sondes d'activations sur modèles $8\text{B}/70\text{B}$ ; fournit des contrôles honnêtes appariés pour calibrer $\alpha_{\text{FA}}$.

*(Je mentionne uniquement pour mémoire MonitoringBench et SLEIGHT-Bench, VÉRIFIÉ fait 10, afin de respecter la limite de trois bancs décrits).*

### 2. Propositions brutes d'une course précédente et journaux de refus (RAPPORTÉ, fait 12)
* **Propositions brutes** : Indépendance partielle (même programme mais instances antérieures) ; coût de formatage très faible ; permettent d'estimer la stabilité temporelle de l'énumération (recapture longitudinale) avant d'ouvrir les $5$ instances scellées.
* **Journaux de refus** : Indépendance mécanique vis-à-vis des générations acceptées ; coût d'étiquetage moyen (classification des motifs de déclenchement des filtres sans lire de contenu interdit) ; constituent l'unique instrument pour borner la taille de la « zone aveugle » (zéro structurel) discutée au Bloc 1(d).

---

## Bloc 3 — Questions candidates pour le texte III

### Question candidate 1 — Borne d'universalité PAC corrigée de la masse manquante (Good-Turing)
* **Formulation** : *« Comment construire et valider sur mondes simulés un estimateur de la proportion maximale d'échec d'une défense qui combine la borne binomiale sur les familles tenues à l'écart et l'estimateur de Good-Turing de la masse de probabilité des familles non découvertes ? »*
* **1. Avantage exploité** : Résout directement l'objection du fait 9 (VÉRIFIÉ) selon laquelle les familles sont découvertes et non tirées uniformément, et reste valide même si le nombre total de familles $N$ est infini ou non fermé.
* **2. Piège méthodologique qui la tuerait** : Si le nombre de singletons $Q_1$ (familles vues par une seule source) est très élevé, la masse manquante $\hat{p}_0 = Q_1 / M$ dépasse le seuil cible $\varepsilon$ (par exemple $\hat{p}_0 = 0,20 > \varepsilon = 0,10$, illustratif), rendant la borne triviale (impossibilité mathématique de certifier la défense sans nouvelles sources).
* **3. Validation extérieure chiffrée** : Confrontation de la prédiction scellée de $\hat{p}_0$ (calculée sur les $2$ sources initiales $+$ $3$ instances, illustratif) au taux réel de familles inédites découvertes lors de l'ouverture des $2$ dernières instances scellées et de $15$ familles extérieures extraites de ControlArena/SHADE-Arena (illustratif) ; succès si le taux observé tombe dans l'intervalle de prédiction à $95\%$ (à $\pm 0,05$ près, illustratif).
* **4. Risque hors périmètre** : **Faible** (illustratif). La question porte exclusivement sur un estimateur de couverture d'échantillonnage et une borne de confiance binomiale pondérée.

### Question candidate 2 — Protocole d'appariement par graphe biparti et modèles log-linéaires multi-sources
* **Formulation** : *« Comment estimer le nombre de familles inconnues $N$ et l'intervalle de confiance associé à partir de $K \ge 5$ sources hétérogènes lorsque la relation d'équivalence entre schémas de familles n'est pas bijective et dépend du lecteur ? »*
* **1. Avantage exploité** : S'appuie directement sur l'anomalie empirique documentée dans le dossier ($m = 18$ contre $m = 19$ et lecteur unique Sonnet 5.5 de même lignée qu'Opus 5.5, VÉRIFIÉ, faits 5 à 8) pour transformer un artefact d'annotation en modèle statistique d'erreur de mesure.
* **2. Piège méthodologique qui la tuerait** : Indétermination des modèles log-linéaires à $K = 5$ sources si la table de contingence $2^5 - 1 = 31$ cellules est trop creuse (trop de cellules à zéro pour un total de $\sim 40$ à $60$ familles, illustratif), provoquant la divergence des intervalles de confiance par profil de vraisemblance.
* **3. Validation extérieure chiffrée** : Double lecture aveugle par un jury externe de $3$ modèles de fournisseurs distincts sur les $34$–$35$ familles existantes (VÉRIFIÉ, fait 7) augmentées de $20$ familles issues des cinq instances scellées (RAPPORTÉ, fait 4 ; chiffre $20$ illustratif), avec prédiction scellée du nombre de nouvelles classes observées dans la $5^{\text{e}}$ instance à partir des $4$ premières (erreur relative cible $\le 15\%$, illustratif).
* **4. Risque hors périmètre** : **Faible** (illustratif). La question est bornée à la théorie des graphes d'entités (résolution d'entités) et aux estimateurs de capture-recapture (Chao, Darroch, Cormack).

### Question candidate 3 — Allocation optimale à deux niveaux et règle d'arrêt séquentielle
* **Formulation** : *« Comment déterminer le couple minimal (nombre de familles $n$, nombre de trajectoires par famille $m$) et la règle d'arrêt séquentielle garantissant au niveau $1 - \alpha$ qu'au plus une fraction $\varepsilon$ des familles a un taux de détection inférieur à $\tau$ à taux de fausses alertes $\alpha_{\text{FA}}$ fixé ? »*
* **1. Avantage exploité** : Permet de dimensionner rigoureusement le budget de calcul sur les modèles $8\text{B}$ et $70\text{B}$ (RAPPORTÉ, fait 3) sans gaspiller d'inférences sur des familles où la variance intra-famille est déjà négligeable devant la variance inter-familles.
* **2. Piège méthodologique qui la tuerait** : Sous-estimation de la corrélation intra-grappe $\rho_{\text{grappe}}$ entre familles proches générées par les mêmes instances, qui dégrade le facteur d'effet de plan $\text{DEFF}$ et fait chuter la couverture réelle sous $1 - \alpha$.
* **3. Validation extérieure chiffrée** : Préenregistrement de la courbe d'arrêt séquentielle avant l'exécution sur $30$ familles extérieures/scellées et $50$ trajectoires honnêtes appariées par famille (illustratif) issues de Liars' Bench et ControlArena (VÉRIFIÉ, fait 10) ; vérification par un tiers que le taux de fausses alertes hors échantillon reste $\le 0,01$ (illustratif) et que la décision d'arrêt respecte l'enveloppe de martingale.
* **4. Risque hors périmètre** : **Faible** (illustratif). La question est purement un problème de planification expérimentale hiérarchique et de statistique séquentielle.

### Question candidate 4 — Mesure de la perte d'universalité entre régime aveugle et régime informé
* **Formulation** : *« Comment définir et borner statistiquement l'écart de performance $\Delta M$ d'une défense (sonde interne + moniteur texte + agrégation séquentielle) entre le banc d'évaluation aveugle et le banc informé des seuils et du protocole, à budget d'évaluation fixé ? »*
* **1. Avantage exploité** : Opérationnalise directement la décision N-056 (deux versions du banc d'évaluation, aveugle et informée, sans dépense, VÉRIFIÉ, fait 1) et la règle d'absence d'agent opérationnel (RAPPORTÉ, fait 2) sous forme d'un test d'invariance de distribution.
* **2. Piège méthodologique qui la tuerait** : Confusion entre l'effet du régime d'information et un changement de difficulté intrinsèque des éléments si les trajectoires des deux régimes ne sont pas strictement appariées par graine aléatoire et structure de tâche.
* **3. Validation extérieure chiffrée** : Sur un lot scellé de $25$ familles (illustratif) évaluées dans les deux régimes ($m = 40$ trajectoires appariées par famille, illustratif), prédiction scellée de la borne supérieure de dégradation $\Delta M \le 0,10$ (illustratif) vérifiée par un auditeur tiers par test de permutation apparié de Wilcoxon au seuil $\alpha = 0,05$ (illustratif).
* **4. Risque hors périmètre** : **Moyen** (illustratif). Si le répondant décrit comment le banc informé modifie concrètement les trajectoires, il viole le périmètre ; la question est bornée à la mesure en imposant que le banc soit traité comme deux lois de probabilité boîte noire $\mathbb{P}_0(S \mid f)$ et $\mathbb{P}_1(S \mid f, \theta_{\text{déf}})$ sur les scores $S$ des moniteurs.

### Question candidate 5 — Estimation de la zone aveugle induite par les refus corrélés des sources
* **Formulation** : *« Comment estimer la borne supérieure du nombre de familles simultanément censurées par les filtres des $K$ instances de génération (zéro structurel des tables de capture-recapture) à l'aide des journaux de refus passés et des taxonomies de bancs publics externes ? »*
* **1. Avantage exploité** : Exploite une ressource unique du programme — les journaux de refus passés (RAPPORTÉ, fait 12) et les bancs publics (VÉRIFIÉ, fait 10) — pour lever le point aveugle majeur des méthodes de capture-recapture appliquées aux modèles de langage.
* **2. Piège méthodologique qui la tuerait** : Biais d'extrapolation si la loi d'occurrence des familles dans les bancs publics académiques est totalement étrangère à la loi des familles bloquées par les filtres des fournisseurs.
* **3. Validation extérieure chiffrée** : Comparaison du taux de refus observé sur les $5$ instances indépendantes (RAPPORTÉ, fait 4) avec la proportion de familles de ControlArena / SHADE-Arena ($N_{\text{ext}} \approx 15$ à $30$ familles, illustratif) qui déclenchent un refus lorsqu'on demande à ces mêmes instances de les reformuler à l'aveugle ; validation si l'estimateur de zéro structurel couvre ce taux à $\pm 10\%$ près (illustratif).
* **4. Risque hors périmètre** : **Moyen** (illustratif). Le mot « refus » pourrait inciter à spéculer sur les sujets refusés ; l'énoncé borne strictement la question à la modélisation d'une troncature statistique (modèles de capture-recapture à zéros tronqués et sélection de Heckman) sur des comptages d'événements anonymisés.

---

## Bloc 4 — Question annexe : organisation des cinq instances indépendantes

Les éléments ci-dessous qui ne figurent pas dans les faits (notamment les protocoles d'anonymisation, de partitionnement de graphe et de tests spectraux) ont le statut **HYPOTHÈSE**.

### 1. Ce que chaque instance reçoit
* **Options** : (A) Même consigne exacte pour les $5$ instances (comme fait pour Argon et Opus 5.5, VÉRIFIÉ, fait 6) ; (B) Consignes sémantiquement équivalentes mais variées par rotations syntaxiques et niveaux d'abstraction formelle (plan en carré latin).
* **Avantage / Inconvénient** : (A) garantit l'identicité nominale du stimulus mais maximise la corrélation induite par les mots-clés de la consigne ; (B) réduit le biais d'ancrage lexical commun mais introduit une variance de consigne.
* **Recommandation et confiance** : **Option Hybride (A + B en deux passes scellées)** (HYPOTHÈSE) — Passe 1 avec une consigne formelle minimaliste strictement identique (pour la comparabilité exacte de capture-recapture avec Argon et Opus 5.5), suivie dans une session isolée d'une Passe 2 avec reformulation abstraite. **Confiance : Élevée** (illustratif).

### 2. Comment empêcher les fuites entre instances et vers la défense
* **Options** : (A) Appels API séquentiels manuels ; (B) Exécution automatisée dans des conteneurs éphémères sans état réseau partagé, clés API distinctes avec désactivation de la rétention des journaux fournisseur (*zero data retention*), température fixée et graine enregistrée, puis chiffrement asymétrique immédiat (clé publique d'audit) et hachage SHA-256 horodaté de chaque sortie avant toute lecture humaine ou mécanique (HYPOTHÈSE).
* **Avantage / Inconvénient** : (A) est simple mais vulnérable aux erreurs humaines de copier-coller et de contamination ; (B) garantit mathématiquement le non-partage avec la conception des défenses (RAPPORTÉ, fait 4) au prix d'un script d'orchestration léger.
* **Recommandation et confiance** : **Option B** (HYPOTHÈSE). **Confiance : Élevée** (illustratif).

### 3. Comment apparier leurs familles sans biais de lecteur unique
* **Options** : (A) Un lecteur unique d'un $6^{\text{e}}$ fournisseur ; (B) Protocole en trois étapes (HYPOTHÈSE) : (i) réécriture canonique aveugle (suppression des tics stylistiques propres à chaque fournisseur dans un schéma abstrait standardisé), (ii) évaluation de toutes les paires de schémas par un jury croisé de $J \ge 3$ modèles de fournisseurs distincts qui codent chaque paire selon $4$ relations formelles (équivalent, sous-famille de, sur-famille de, disjoint), (iii) réduction algorithmique déterministe du graphe orienté par quotient des composantes fortement connexes (avec séparation d'un niveau « famille majeure » et « sous-famille » pour traiter explicitement les cas 1-pour-2 observés au fait 7, VÉRIFIÉ).
* **Avantage / Inconvénient** : (A) reproduit le risque de biais d'un lecteur unique (VÉRIFIÉ, fait 6) ; (B) mesure l'accord inter-juges ($\kappa$ de Fleiss) et élimine l'asymétrie $m=18$ vs $m=19$, mais multiplie par $J$ le coût de lecture.
* **Recommandation et confiance** : **Option B** (HYPOTHÈSE). **Confiance : Élevée** (illustratif).

### 4. Comment tester leur indépendance (corrélation d'entraînement entre fournisseurs)
* **Options** : (A) Supposer l'indépendance sur la foi de fournisseurs distincts ; (B) Tester formellement la dépendance résiduelle (HYPOTHÈSE) par : (i) ajustement de modèles log-linéaires avec termes d'interaction paire-à-paire $\lambda_{kk'}$ sur la matrice d'incidence $M \times 5$ des familles découvertes, (ii) mesure de la corrélation des rangs d'apparition (tau de Kendall) des familles communes entre instances, et (iii) test d'indépendance externe sur un banc de questions factuelles rares hors domaine pour estimer la matrice de covariance de pré-entraînement $\Sigma_{\text{fournisseurs}}$ entre les $5$ modèles.
* **Avantage / Inconvénient** : (A) est contredit par le recouvrement connu des grands corpus web ; (B) fournit un prédicteur quantitatif de $\lambda_{kk'}$ pour corriger l'estimateur de cardinalité.
* **Recommandation et confiance** : **Option B** (HYPOTHÈSE). **Confiance : Moyenne à élevée** (illustratif).

### 5. Comment s'en servir comme sources multiples pour estimer les familles inconnues
* **Options** : (A) Moyenne des estimateurs de Chapman deux à deux ; (B) Construction de la matrice d'incidence complète à $K = 5$ (ou $K = 7$ en incluant Argon et Opus 5.5, VÉRIFIÉ, fait 5) et calcul conjoint de : (i) la borne inférieure non paramétrique de Chao2, (ii) l'estimateur log-linéaire sélectionné par critère AICc parmi $(M_0, M_t, M_h, M_{th}, M_{tb})$, et (iii) la courbe d'accumulation raréfiée et extrapolée (Chao et al., 2014, *Rarefaction and extrapolation with Hill numbers*) ainsi que le déficit de couverture de Good-Turing $\hat{p}_0 = Q_1 / \sum_{k=1}^K n_k$ (HYPOTHÈSE).
* **Avantage / Inconvénient** : (A) viole l'indépendance des tests et ignore les interactions d'ordre $\ge 3$ ; (B) exploite toute l'information de la distribution des fréquences d'incidence $(Q_1, \dots, Q_K)$.
* **Recommandation et confiance** : **Option B** (HYPOTHÈSE). **Confiance : Élevée** (illustratif).

### 6. Que faire si une instance refuse
* **Options** : (A) Reformuler la question jusqu'à acceptation ; (B) Enregistrer le refus tel quel, de manière définitive et sans aucune reformulation (conformément au protocole du collisionneur, VÉRIFIÉ, faits 14 et 16), activer tout au plus une question de repli préenregistrée plus étroite au niveau purement mathématique (VÉRIFIÉ, fait 16), et traiter l'instance ayant refusé comme une observation de censure informative dans le modèle statistique (en substituant pour le quota de familles une instance de réserve pré-scellée d'un autre fournisseur, sans effacer le refus du journal d'audit) (HYPOTHÈSE).
* **Avantage / Inconvénient** : (A) est interdit par le protocole (VÉRIFIÉ, fait 14) et introduit un biais de sélection adaptatif incontrôlable ; (B) préserve l'intégrité du préenregistrement et alimente la mesure du zéro structurel (Question candidate 5).
* **Recommandation et confiance** : **Option B** (VÉRIFIÉ pour le non-rejeu, fait 14 ; HYPOTHÈSE pour le traitement statistique). **Confiance : Élevée** (illustratif).

---

## (d) Ancrage matériel

* **Modèles cibles** : Poids ouverts de $8\text{B}$ et $70\text{B}$ de paramètres (RAPPORTÉ, fait 3), plus $5$ instances de génération par API (RAPPORTÉ, fait 4) et $3$ lecteurs d'appariement (illustratif).
* **Calcul et coût estimés (illustratifs)** :
  * *Simulations Monte-Carlo (Duels 1–2 et Bloc 1c)* : $10^5$ mondes sur CPU standard, $\sim 2$ heures-cœur, coût $< 5\text{ €}$ (illustratif).
  * *Génération et appariement croisé ($5$ instances + jury de $3$ lecteurs sur $\sim 1\,500$ paires)* : $\sim 5 \times 10^6$ tokens API, coût $\approx 40\text{ €}$ à $120\text{ €}$ (illustratif).
  * *Évaluation des sondes et moniteurs ($60$ familles $\times 40$ trajectoires $\times 2$ régimes $+$ contrôles honnêtes sur $8\text{B}$ et $70\text{B}$)* : $\sim 150$ à $300$ heures-GPU A100/H100-$80\text{Go}$, soit $\approx 300\text{ €}$ à $900\text{ €}$ (illustratif).

FIN-DE-CELLULE
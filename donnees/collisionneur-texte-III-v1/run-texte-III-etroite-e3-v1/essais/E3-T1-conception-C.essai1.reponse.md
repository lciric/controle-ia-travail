### (a) Ce que la question suppose sans que ce soit établi

- Bloc 1 : L'espace des familles admet une mesure de probabilité $\mathbb{P}$ bien définie, stable et opératoire permettant de définir des quantiles ou des proportions — Statut : HYPOTHÈSE.
- Bloc 1 : Les familles sont parfaitement cloisonnées sous un étiquetage canonique sans ambiguïté de frontière — Statut : HYPOTHÈSE.
- Bloc 1 : Le taux d'échec intrinsèque $\theta_i$ d'une défense sur une famille $i$ est une constante stationnaire bien définie — Statut : HYPOTHÈSE.
- Bloc 2 : Le mécanisme de découverte séquentielle des familles est informatif de la distribution cible ou son biais d'échantillonnage par taille peut être corrigé analytiquement — Statut : HYPOTHÈSE.
- Bloc 2 : La structure de dépendance entre les taux d'échec des familles proches est paramétrable par une matrice de corrélation échangeable ou spatiale connue — Statut : HYPOTHÈSE.
- Bloc 3 : La population totale $N$ de familles pertinentes est finie et fermée durant l'énumération par les trois sources — Statut : HYPOTHÈSE.
- Bloc 3 : Le décompte de 37 familles et l'appariement inter-sources réalisés par un lecteur isolé (fait 17, RAPPORTÉ) sont exempts de fausses fusions et de fausses scissions — Statut : OBSERVÉ-NON-AUDITÉ.
- Bloc 3 : Aucune sous-population de familles n'a une probabilité de capture strictement nulle pour les trois sources simultanément (absence de censure commune) — Statut : HYPOTHÈSE.
- Bloc 3 : L'interaction d'ordre trois dans le modèle log-linéaire de capture est nulle (absence de synergie ou d'interférence spécifique aux trois sources simultanément) — Statut : HYPOTHÈSE.

---

### (b) Expériences décisives en duel $H_A$ contre $H_B$

#### Duel 1 : Couverture de l'estimateur de taille de population sous dépendance et hétérogénéité
* **Hypothèse $H_A$** : Sous une dépendance positive entre sources reproduisant la déviance de 12,9 (VÉRIFIÉ, fait 18) et une hétérogénéité de capture entre familles (loi Bêta de coefficient de variation $CV = 0,5$, illustratif), l'intervalle de confiance à 95 % (illustratif) du modèle log-linéaire saturé à 6 paramètres (sans interaction d'ordre trois) conserve un taux de couverture empirique de la vraie taille $N$ supérieur ou égal à 90 % (illustratif).
* **Hypothèse $H_B$** : Dans ces mêmes conditions, la couverture du modèle log-linéaire saturé chute sous 90 % (illustratif) par biais d'hétérogénéité non modélisé, tandis que la borne inférieure de Chao corrigée pour échantillon fini ($\hat{N}_{\text{Chao1}}$) maintient une couverture unilatérale (probabilité que $N \ge \hat{N}_{\text{Chao1},\text{inf}}$) supérieure ou égale à 95 % (illustratif).
* **Métrique et seuil** : Taux de couverture empirique calculé sur $M = 10\,000$ (illustratif) réplications Monte Carlo d'une population de $N = 100$ (illustratif) familles. Seuil de décision : 90 % (illustratif) pour l'intervalle bilatéral, 95 % (illustratif) pour la borne unilatérale.
* **Contrôle négatif** : Simulation sous indépendance stricte des trois sources et équiprobabilité de capture ($CV = 0$, $p = 0,25$, illustratif). Les deux estimateurs doivent atteindre leur couverture nominale de 95 % $\pm 1 \%$ (illustratif) ; sinon le générateur est déclaré défectueux.
* **Issue falsificatrice** : Si la couverture du modèle log-linéaire est $\ge 90 \%$ (illustratif), $H_B$ est falsifiée. Si elle est $< 90 \%$ et que la couverture unilatérale de Chao est $\ge 95 \%$ (illustratif), $H_A$ est falsifiée. Si les deux échouent sous leurs seuils respectifs, les deux hypothèses sont falsifiées conjointement, démontrant la nécessité d'un modèle à classes latentes ou de données à $\ge 4$ sources.

#### Duel 2 : Validité de la borne à zéro échec sous échantillonnage par découverte biaisée
* **Hypothèse $H_A$** : Lorsque les familles sont découvertes séquentiellement sans remise avec une probabilité proportionnelle à leur visibilité $w_i$, et que la visibilité est négativement corrélée au taux d'échec de la défense ($\rho(w_i, \theta_i) = -0,4$, illustratif : les familles faciles à trouver sont faciles à défendre), la règle d'arrêt classique à zéro échec sur $n = 59$ familles (VÉRIFIÉ, fait 9 pour $\varepsilon = 0,05$) garantit un risque d'erreur de type I (conclure à tort que la part de familles défaillantes est $< 0,05$) inférieur ou égal à $\alpha = 0,10$ (illustratif).
* **Hypothèse $H_B$** : Sous ce couplage ($\rho = -0,4$, illustratif), le risque de type I de la borne classique à $n = 59$ dépasse $0,10$ (illustratif), tandis qu'un estimateur de Horvitz-Thompson pondéré par les probabilités d'inclusion estimées par capture-recapture ramène le risque de type I sous le seuil nominal $\alpha = 0,05$ (illustratif) au prix d'une taille d'échantillon accrue ($n = 120$, illustratif).
* **Métrique et seuil** : Fréquence empirique de fausse certification sur $10\,000$ (illustratif) mondes simulés où la vraie proportion de familles défaillantes dans la population totale ($N = 500$, illustratif) est fixée exactement à $\varepsilon = 0,05$ (VÉRIFIÉ, fait 9). Seuil : $\alpha = 0,10$ pour $H_A$, $\alpha = 0,05$ pour $H_B$ (illustratifs).
* **Contrôle négatif** : Simulation avec $\rho(w_i, \theta_i) = 0$ (indépendance entre visibilité et échec). La règle à $n = 59$ (VÉRIFIÉ, fait 9) doit présenter un risque de type I inférieur ou égal à $0,05$ (et même inférieur par effet de tirage sans remise dans $N = 500$, illustratif).
* **Issue falsificatrice** : Un taux de fausse certification $> 0,10$ (illustratif) pour la règle à $n = 59$ falsifie $H_A$. Un taux $\le 0,10$ falsifie $H_B$. Si $H_A$ est falsifiée et que l'estimateur pondéré présente un risque $> 0,05$ (illustratif), la composante corrective de $H_B$ est également falsifiée.

---

### (c) Mesure minimale de chaque instrument nommé

Les « cas honnêtes appariés » sont constitués d'une grille factorielle de mondes simulés à vérité terrain connue : taille de population fixée à $N = 100$ (illustratif) familles, probabilités de capture marginales calées pour reproduire en espérance les comptes observés (22, 23, 27 ; RAPPORTÉ, fait 17).

#### Instrument 1 : Estimateur des familles inconnues ($\hat{N}$)
* **Facteurs variés** :
  1. Dépendance inter-sources (rapports de cotes $\psi \in \{1,0 ; 2,5 ; 5,0\}$, illustratif).
  2. Hétérogénéité de capture individuelle entre familles ($CV \in \{0 ; 0,4 ; 0,8\}$, illustratif).
  3. Taux de contamination par erreur de lecteur unique (taux de fusion à tort $\tau_f \in \{0 ; 0,05\}$ et de scission à tort $\tau_s \in \{0 ; 0,05\}$, illustratifs).
* **Mesures** : Biais relatif moyen $\mathbb{E}[(\hat{N}-N)/N]$, racine de l'erreur quadratique moyenne (RMSE), et taux de couverture empirique de l'intervalle de confiance à 95 % (illustratif).
* **Base mécanique à battre** : Le comptage brut des familles observées $S_{\text{obs}}$ (37 dans les données de départ, RAPPORTÉ, fait 17), assorti d'un intervalle de fluctuation binomial naïf supposant la couverture complète. L'instrument fonctionne s'il réduit le biais relatif d'au moins 50 % (illustratif) par rapport à $S_{\text{obs}} - N$ sans que sa couverture ne tombe sous 85 % (illustratif).
* **Contrôle négatif** : Monde fermé de $N = 37$ (illustratif) familles avec probabilité de capture $p = 0,99$ (illustratif) par source ($S_{\text{obs}} = 37$). L'estimateur doit renvoyer $\hat{N} \approx 37$ avec un biais $< 1 \%$ (illustratif) et ne pas inventer de familles fantômes.

#### Instrument 2 : Mesure d'universalité ($\hat{U}_{q,\tau}$)
* **Facteurs variés** :
  1. Corrélation intra-classe des taux d'échec entre familles proches ($\rho_{\text{fam}} \in \{0 ; 0,3 ; 0,6\}$, illustratif).
  2. Biais de sélection du processus de découverte ($\rho(w_i, \theta_i) \in \{0 ; -0,3 ; -0,6\}$, illustratif).
  3. Taille finie de l'échantillon d'éléments évalués par famille ($m \in \{20 ; 100 ; 500\}$ éléments par famille, illustratif).
* **Mesures** : Taux de fausses alertes (rejeter une défense universelle lorsque la vraie part de familles défaillantes est $\pi = 0,01 < \varepsilon = 0,05$, illustratif) et taux de détection / puissance (rejeter une défense non universelle lorsque $\pi = 0,10 > \varepsilon = 0,05$, illustratif).
* **Base mécanique à battre** : Le taux d'échec empirique global moyenné sur l'ensemble des éléments de toutes les familles observées confondues (ignorant la structure groupée par famille et l'échantillonnage biaisé). L'instrument doit abaisser le taux de fausse certification sous le seuil nominal $\alpha = 0,05$ (illustratif) là où la moyenne brute sur-certifie (erreur de type I $> 0,20$, illustratif, sous $\rho_{\text{fam}} = 0,6$).
* **Contrôle négatif** : Monde où toutes les familles ont un taux d'échec exactement égal au seuil critique $\theta_i = \tau$ ($\pi = 1,0$). La probabilité de certifier l'universalité doit être $\le \alpha = 0,05$ (illustratif).

---

### Bloc 1 — Définition opérationnelle de l'universalité

Soit $\mathcal{F}$ une classe de familles, $i \in \mathcal{F}$ une famille dotée d'un taux d'échec intrinsèque $\theta_i \in [0,1]$, et $\hat{\theta}_i$ son estimation sur $m$ éléments.

1. **Pire cas sur une classe déclarée** :
   * *Énoncé* : $\forall i \in \mathcal{F}_{\text{déclarée}}, \, \theta_i \le \tau$.
   * *Déclaration préalable* : La grammaire formelle du schéma de construction délimitant $\mathcal{F}_{\text{déclarée}}$ et le seuil de tolérance $\tau$ (ex. $0,01$, illustratif).
   * *Ce qu'elle n'autorise pas* : Toute inférence à partir d'un échantillon strict $n < |\mathcal{F}_{\text{déclarée}}|$ sans hypothèse de régularité paramétrique (un seul cas non vu peut violer le $\forall$).
   * *Recalcul tiers* : Énumération exhaustive ou optimisation adversariale sur le schéma déclaré et calcul de $\max_i \hat{\theta}_i$.

2. **Écart entre familles vues ($\mathcal{F}_{\text{vues}}$) et tenues à l'écart ($\mathcal{F}_{\text{écart}}$)** :
   * *Énoncé* : $\left| \mathbb{E}_{i \sim \mathcal{P}_{\text{écart}}}[\theta_i] - \mathbb{E}_{j \sim \mathcal{P}_{\text{vues}}}[\theta_j] \right| \le \delta$.
   * *Déclaration préalable* : Le protocole de partitionnement aveugle, le seuil $\delta$ et l'empreinte cryptographique des familles $\mathcal{F}_{\text{écart}}$.
   * *Ce qu'elle n'autorise pas* : D'affirmer que la défense est bonne en absolu (une défense échouant partout à 90 % a un écart $\delta = 0$).
   * *Recalcul tiers* : Différence des moyennes empiriques sur le jeu scellé et le jeu d'entraînement.

3. **Quantile / proportion de familles passant un seuil** :
   * *Énoncé* : $\mathbb{P}_{i \sim \mathcal{P}}(\theta_i \le \tau) \ge 1 - \varepsilon$.
   * *Déclaration préalable* : La loi d'échantillonnage $\mathcal{P}$ sur $\mathcal{F}$, le seuil d'échec par famille $\tau$, la part maximale d'échec $\varepsilon$ (ex. $0,05$, VÉRIFIÉ, fait 9) et le niveau de confiance $1-\alpha$ (ex. $95\%$, VÉRIFIÉ, fait 9).
   * *Ce qu'elle n'autorise pas* : Garantir le comportement sur une famille singulière de mesure nulle ou hors du support de $\mathcal{P}$.
   * *Recalcul tiers* : Calcul de la statistique de dépassement $\sum_{i=1}^n \mathbb{I}(\hat{\theta}_i > \tau_{\text{corr}})$ et vérification de la borne binomiale ou pondérée.

**Distinction et choix** : « Universelle sur la classe déclarée » borne le risque sous une loi d'échantillonnage connue $\mathcal{P}$ de support fermé ; « robuste à l'inconnu » exige que la garantie survive dans le complémentaire non observé $\mathcal{F} \setminus \mathcal{F}_{\text{obs}}$ de mesure inconnue. **Je retiens l'option 3 combinée à l'évaluation sur familles tenues à l'écart** : $\mathbb{P}_{i \sim \mathcal{P}_{\text{écart}}}(\theta_i \le \tau) \ge 1 - \varepsilon$ avec confiance $1-\alpha$, seule option statistiquement réfutable à taille d'échantillon finie.

---

### Bloc 2 — Nombre de familles nécessaire, par simulation

**Énoncé cible** : Certifier avec confiance $1 - \alpha = 0,95$ que $\mathbb{P}_{i \sim \mathcal{P}}(\theta_i > \tau) < \varepsilon = 0,05$ (valeurs de référence du fait 9, VÉRIFIÉ).

**Modèle génératif à deux niveaux** :
1. *Niveau 1 (Entre familles — hétérogénéité et dépendance)* : Un vecteur latent gaussien $Z \sim \mathcal{N}(0, \Sigma)$ de taille $N$, où $\Sigma_{ij} = \rho_{\text{fam}}^{\, d(i,j)}$ capture la proximité entre familles. Les vrais taux d'échec sont $\theta_i = F_{\text{Beta}(\alpha_0, \beta_0)}^{-1}(\Phi(Z_i))$.
2. *Niveau 2 (Intra-famille — variance d'estimation)* : Sur la famille $i$, le nombre d'échecs observés sur $m$ éléments suit $Y_i \mid \theta_i \sim \text{Binomiale}(m, \theta_i)$. Une famille est déclarée empiriquement réussie si $Y_i \le c$, où $c$ est choisi pour que $\mathbb{P}(Y_i \le c \mid \theta_i > \tau) \le \beta_{\text{intra}}$ (ex. $0,05$, illustratif).

**Effet de la dépendance et règle de calcul** : La corrélation positive $\rho_{\text{fam}} > 0$ réduit la taille d'échantillon effective $n_{\text{eff}} = n / [1 + (n-1)\bar{\rho}_{\text{succès}}]$. Si l'erreur intra-famille $\beta_{\text{intra}}$ s'ajoute, la probabilité d'observer un succès sur une famille tirée au hasard sous l'hypothèse nulle ($\mathbb{P}(\theta_i > \tau) = \varepsilon$) est bornée par $1 - \varepsilon(1 - \beta_{\text{intra}})$. La règle de dimensionnement par simulation cherche le plus petit $n$ tel que, sur $10\,000$ (illustratif) tirages sous $\pi = \varepsilon$, la probabilité de zéro échec observé soit $\le \alpha$ :
$$n(\rho_{\text{fam}}, \beta_{\text{intra}}) \approx \frac{\ln \alpha}{\ln(1 - \varepsilon(1 - \beta_{\text{intra}}))} \times \text{VIF}(\rho_{\text{fam}})$$
Pour $\varepsilon = 0,05$, $\alpha = 0,05$, si $\beta_{\text{intra}} = 0,05$ et $\text{VIF} = 1,3$ (illustratifs), $n$ passe de $59$ (VÉRIFIÉ, fait 9) à $81$ (illustratif).

**Règle d'arrêt séquentielle** : Test de rapport de probabilités séquentiel (SPRT de Wald, 1945, *Sequential Analysis*) ou frontière alpha-spending de Pocock : arrêt pour futilité dès la première famille où $Y_i > c$ (si l'on exige la borne à zéro échec), arrêt pour succès lorsque la martingale de richesse $\prod_{k=1}^t (1 - \varepsilon_{\text{eff}})^{-1}$ franchit $1/\alpha$.

**Mécanisme de découverte** : Les familles découvertes sont échantillonnées sans remise avec probabilité inégale $w_i$ (biais de taille). La borne du fait 9 (VÉRIFIÉ) perd sa validité sur la classe totale : elle ne borne plus que la sous-population pondérée par $w_i$. **Ce que la simulation démontre** : la dégradation exacte de $\alpha$ en fonction du couplage $\rho(w_i, \theta_i)$ et la correction par pondération inverse $\hat{\pi}_{\text{HT}} = \sum (I_i / \hat{w}_i)^{-1} \sum (I_i \mathbb{I}(\hat{\theta}_i > \tau)/\hat{w}_i)$. **Ce qu'elle suppose** : que le support de découverte couvre toute la classe ($w_i > 0, \, \forall i$) et que la famille paramétrique de dépendance $\Sigma$ est bien spécifiée.

---

### Bloc 3 — Familles encore inconnues, sources multiples dépendantes

**1. Déduction de l'affectation des paires par la déviance (calculs vérifiables à partir des faits 17 et 18)**
Soient $S_1, S_2, S_3$ les trois sources de totaux $n_1=22, n_2=23, n_3=27$, avec $S_{\text{obs}}=37$ et $n_{111}=14$ (RAPPORTÉ, fait 17). Les recaptures par paire sont $\{16, 16, 17\}$. Les comptes des cellules d'exactement deux sources sont $n_{110} = n_{1\cap 2} - 14$, $n_{101} = n_{1\cap 3} - 14$, $n_{011} = n_{2\cap 3} - 14$, soit une permutation de $\{2, 2, 3\}$ (somme $7$, VÉRIFIÉ, fait 18).
Il y a 3 affectations possibles selon la paire qui reçoit 17 (donc la cellule double qui vaut 3) :
* **Cas A ($n_{2\cap 3}=17$, soit $n_{011}=3, n_{110}=2, n_{101}=2$)** : Les singletons valent $n_{100} = 22 - (14+2+2) = 4$ ; $n_{010} = 23 - (14+2+3) = 4$ ; $n_{001} = 27 - (14+2+3) = 8$. Les 7 cellules observées sont $(14, 2, 2, 3, 4, 4, 8)$.
* **Cas B ($n_{1\cap 3}=17$, soit $n_{101}=3$)** : Singletons $(3, 5, 8)$.
* **Cas C ($n_{1\cap 2}=17$, soit $n_{110}=3$)** : Singletons $(3, 4, 9)$.

En ajustant le modèle d'indépendance ($\mathbb{E}[n_{ijk}] = N p_1^i(1-p_1)^{1-i}p_2^j(1-p_2)^{1-j}p_3^k(1-p_3)^{1-k}$) par maximum de vraisemblance multinomiale ($\hat{N}_{\text{ind}} \approx 38,91$, $\hat{p}_1 \approx 0,565, \hat{p}_2 \approx 0,591, \hat{p}_3 \approx 0,694$, invariants par permutation des paires), la déviance $G^2 = 2 \sum_{\text{7 cell.}} n_{ijk} \ln(n_{ijk}/\hat{m}_{ijk})$ vaut :
* Cas A : $G^2 = 12,90$ (illustratif du calcul numérique exact : $12,904$).
* Cas B : $G^2 = 13,20$ (illustratif).
* Cas C : $G^2 = 14,22$ (illustratif).
La déviance rapportée de $12,9$ (RAPPORTÉ, fait 17 ; VÉRIFIÉ en degrés de liberté, fait 18) **identifie de manière unique le Cas A** : la paire $(S_1, S_2)$ a 16 recaptures, $(S_1, S_3)$ en a 16, et $(S_2, S_3)$ en a 17.

**2. Estimateurs de borne inférieure et de couverture (indépendants de l'affectation des paires)**
Avec les fréquences de capture $f_1 = 16$, $f_2 = 7$, $f_3 = 14$, $S_{\text{obs}} = 37$ et le total d'observations $M = 72$ (RAPPORTÉ, fait 17 ; VÉRIFIÉ, fait 18) :
* **Borne inférieure de Chao1** (Chao, 1984, *Biometrics*, « Nonparametric Estimation of the Number of Classes in a Population ») :
  $$\hat{N}_{\text{Chao1}} = S_{\text{obs}} + \frac{f_1^2}{2 f_2} = 37 + \frac{16^2}{2 \times 7} = 37 + \frac{256}{14} = 55,29 \text{ familles} \quad (\text{soit } \hat{f}_0 = 18,29 \text{ inconnues}).$$
* **Borne de Chao1 corrigée pour $T=3$ échantillons** (Chao, 1987, *Biometrics*, « Estimating the Population Size for Capture-Recapture Data with Unequal Catchability » ; facteur $(T-1)/T = 2/3$) :
  $$\hat{N}_{\text{Chao1-bc}} = S_{\text{obs}} + \frac{T-1}{T}\frac{f_1(f_1-1)}{2(f_2+1)} = 37 + \frac{2}{3}\frac{16 \times 15}{2 \times 8} = 37 + 10 = 47,00 \text{ familles}.$$
* **Estimateur de couverture d'échantillon de Good-Turing** (Good, 1953, *Biometrika*, « The Population Frequencies of Species and the Estimation of Population Parameters ») :
  $$\hat{C} = 1 - \frac{f_1}{M} = 1 - \frac{16}{72} = \frac{7}{9} \approx 77,8\,\% \quad \text{ou corrigé (Chao et Jost, 2012, \textit{Ecology}, réf. à vérifier) : } \hat{C}_{\text{corr}} = 1 - \frac{f_1}{M}\left[\frac{(T-1)f_1}{(T-1)f_1 + 2f_2}\right] = 1 - \frac{16}{72}\left(\frac{32}{46}\right) \approx 84,5\,\%.$$
  L'estimateur de taille par couverture homogène (Darroch / Good) donne $\hat{N}_{\text{cov}} = S_{\text{obs}} / \hat{C} = 37 / (7/9) = 47,57$ familles.

**3. Modèles log-linéaires identifiables (7 cellules observées)**
Pour $T=3$ sources, $\ln m_{ijk} = u_0 + u_1 i + u_2 j + u_3 k + u_{12} ij + u_{13} ik + u_{23} jk + u_{123} ijk$.
* Tous les modèles identifiables **supposent obligatoirement $u_{123} = 0$** (absence d'interaction d'ordre trois), de sorte que la cellule manquante est estimée par $\hat{n}_{000} = \frac{\hat{m}_{111}\hat{m}_{100}\hat{m}_{010}\hat{m}_{001}}{\hat{m}_{110}\hat{m}_{101}\hat{m}_{011}}$ (Fienberg, 1972, *Biometrika*, « The Multiple Recapture Census for Closed Populations and Incomplete $2^k$ Contingency Tables »).
* Hiérarchie identifiable :
  1. Indépendance $(S_1, S_2, S_3)$ : 4 paramètres, $7 - 4 = 3$ ddl (VÉRIFIÉ, fait 18).
  2. Une interaction de paire, ex. $(S_1 S_2, S_3)$ : 5 paramètres, $2$ ddl (3 modèles).
  3. Deux interactions de paires, ex. $(S_1 S_2, S_2 S_3)$ : 6 paramètres, $1$ ddl (3 modèles).
  4. Trois interactions de paires $(S_1 S_2, S_1 S_3, S_2 S_3)$ : 7 paramètres, **$0$ ddl (modèle saturé)**.
* Dans le modèle saturé (ajustement exact aux comptes observés), $\hat{n}_{000} = \frac{14 \times n_{100} n_{010} n_{001}}{n_{110} n_{101} n_{011}}$. Cet estimateur **dépend de l'affectation des paires** :
  * Cas A (identifié par $G^2=12,9$) : $\hat{n}_{000} = \frac{14 \times 4 \times 4 \times 8}{2 \times 2 \times 3} = \frac{1792}{12} = 149,33 \implies \hat{N}_{\text{sat}} = 37 + 149,33 = 186,33$.
  * Cas B : $\hat{n}_{000} = \frac{14 \times 3 \times 5 \times 8}{2 \times 3 \times 2} = 140,00 \implies \hat{N}_{\text{sat}} = 177,00$.
  * Cas C : $\hat{n}_{000} = \frac{14 \times 3 \times 4 \times 9}{3 \times 2 \times 2} = 126,00 \implies \hat{N}_{\text{sat}} = 163,00$.
  Étendue sur les affectations possibles : $\hat{N}_{\text{sat}} \in [163,0 ; 186,3]$.

**4. Sens des biais de déplacement**
* *Dépendance positive entre sources* ($u_{ab} > 0$) : biais vers le **bas** (sous-estimation de $N$) pour tout estimateur supposant l'indépendance, car l'excès de recaptures fait croire à une couverture élevée.
* *Hétérogénéité de capture entre familles* : induit une dépendance marginale apparente positive entre toutes les paires et les triplets ; biais vers le **bas** pour le modèle d'indépendance, mais fait **exploser vers le haut** le modèle log-linéaire saturé (car l'hétérogénéité crée $u_{123} > 0$, or poser $u_{123}=0$ gonfle artificiellement $\hat{n}_{000}$ par le facteur $n_{111}=14$ au numérateur).
* *Erreur d'appariement d'un lecteur unique* :
  * **Fusions à tort** (regrouper deux familles distinctes) : diminue $S_{\text{obs}}$, diminue $f_1$ et gonfle $f_2, f_3$ ; déplace $\hat{N}$ fortement vers le **bas**.
  * **Scissions à tort** (séparer deux occurrences de la même famille) : augmente $S_{\text{obs}}$, crée des singletons artificiels $f_1$ et réduit $f_2, f_3$ ; déplace $\hat{N}$ fortement vers le **haut** (explosion quadratique de $f_1^2/(2f_2)$).

**5. Estimateur recommandé, censure commune et population ouverte**
L'excès simultané de singletons ($f_1=16$) et de triplets ($f_3=14$) par rapport aux doublets ($f_2=7$) est la signature classique d'une **hétérogénéité de capture** (modèle $M_h$) ou d'une dépendance commune, plutôt que d'interactions de paires spécifiques. Le modèle saturé ($\hat{N}=186,3$) étant instable (0 ddl, très sensible à $u_{123} \neq 0$), je recommande d'employer le couple : **borne inférieure de Chao1** ($\hat{N}_{\text{Chao1}} = 55,3$, robuste à l'hétérogénéité comme borne inférieure) et un **modèle quasi-symétrique d'hétérogénéité / Rasch à effet aléatoire** (1 ddl, estimant une composante de variance commune $\sigma^2$ sur l'échelle logit), ou une approche bayésienne par moyennage de modèles log-linéaires (BMA).
* *Censure commune* (sous-population de probabilité de capture $(0,0,0)$) : inidentifiable par les données ; tous les estimateurs ne ciblent que la population *visible* $N_{\text{vis}}$. La vraie taille est $N = N_{\text{vis}} + N_{\text{censurée}}$, aucune borne supérieure statistique n'existe sans hypothèse externe.
* *Population ouverte* (création continue de schémas de familles) : $N = \infty$, l'estimation de taille de population perd son sens ; seule la **couverture d'échantillon** $\hat{C} = 1 - f_1/M \approx 77,8\%$ reste bien définie, s'interprétant comme la probabilité que la prochaine famille découverte par le même processus appartienne déjà aux 37 connues.

---

### Bloc 4 — Validation extérieure chiffrée

Soit $S_{\text{ext}}$ une quatrième source extérieure générant $n_{\text{ext}} = 30$ (illustratif) familles canoniques, supposée statistiquement indépendante des trois premières sources conditionnellement à l'hétérogénéité des familles, avec une probabilité de capture moyenne $p_{\text{ext}} \approx 0,35$ (illustratif). Un protocole de double lecture aveugle avec arbitrage pré-enregistré appareille $S_{\text{ext}}$ aux $S_{\text{obs}} = 37$ familles initiales.

1. **Validation de la définition d'universalité (Bloc 1)** :
   * *Prédiction scellée* : L'écart entre la proportion de familles où la défense échoue ($\hat{\theta}_i > \tau$) dans l'échantillon extérieur inédit ($S_{\text{ext}} \setminus S_{\text{obs}}$) et dans le jeu tenu à l'écart interne ($\mathcal{F}_{\text{écart}}$) est borné par $|\hat{\pi}_{\text{ext, inédit}} - \hat{\pi}_{\text{écart}}| \le 0,10$ (illustratif).
   * *Statistique et seuil* : Test exact de Fisher bilatéral sur les taux d'échec par famille au seuil $\alpha = 0,05$ (illustratif), et vérification que $\hat{\pi}_{\text{ext}} \le 0,08$ (illustratif).
   * *Issue falsificatrice* : Si $\hat{\pi}_{\text{ext, inédit}} > \hat{\pi}_{\text{écart}} + 0,10$ avec $p < 0,05$ (illustratif), l'hypothèse que la classe interne $\mathcal{P}_{\text{écart}}$ représente l'universalité externe est falsifiée (biais de conception du programme).

2. **Validation du nombre de familles nécessaire et du modèle de découverte (Bloc 2)** :
   * *Prédiction scellée* : La courbe de raréfaction (nombre cumulé de familles distinctes et variance inter-familles de $\hat{\theta}_i$) prédite par le modèle génératif spatial/biaisé à $n = 37 + n_{\text{ext}}$ contient la trajectoire observée lors de l'ajout séquentiel des $30$ (illustratif) familles de $S_{\text{ext}}$.
   * *Statistique et seuil* : Coefficient de corrélation intra-classe empirique $\hat{\rho}_{\text{fam}}$ sur $S_{\text{ext}}$ devant rester sous la borne supérieure déclarée $\rho_{\max} = 0,30$ (illustratif).
   * *Issue falsificatrice* : Si $\hat{\rho}_{\text{fam}} > 0,30$ (illustratif), le facteur d'inflation de variance $\text{VIF}$ du Bloc 2 est falsifié pour sous-dimensionnement.

3. **Validation de l'estimateur des familles inconnues (Bloc 3)** :
   * *Prédiction scellée* : Soit $K_{\text{nouv}} = |S_{\text{ext}} \setminus S_{\text{obs}}|$ le nombre de familles de $S_{\text{ext}}$ absentes des 37 initiales.
     * Sous la couverture de Good-Turing ($\hat{C} = 77,8\%$), si $S_{\text{ext}}$ échantillonne selon la même loi d'importance que les sources 1 à 3, la part de familles nouvelles attendue est $1 - \hat{C} = 22,2\%$ (soit $\mathbb{E}[K_{\text{nouv}}] = 30 \times 0,222 = 6,7$ familles, illustratif).
     * Sous échantillonnage uniforme par $S_{\text{ext}}$ et validité de la borne de Chao1 ($\hat{N}_{\text{Chao1}} = 55,3$), la part attendue de familles connues est $37 / \hat{N} \le 66,9\%$, donc $K_{\text{nouv}} / 30 \ge 33,1\%$ (au moins $10$ familles nouvelles, illustratif). Sous le modèle saturé ($\hat{N} = 186,3$), $K_{\text{nouv}} / 30 \approx 80,1\%$ ($24$ familles nouvelles, illustratif).
   * *Statistique et seuil* : Estimateur de Petersen entre le pool initial ($37$) et $S_{\text{ext}}$ ($30$) : $\hat{N}_{\text{ext}} = \frac{(37+1)(30+1)}{(30 - K_{\text{nouv}} + 1)} - 1$. Intervalle de prédiction à 95 % (illustratif) pour $K_{\text{nouv}}$ sous Chao1 : $K_{\text{nouv}} \in [6 ; 19]$ (illustratif).
   * *Issue falsificatrice* : Si $K_{\text{nouv}} \ge 20$ sur $30$ (illustratif, impliquant $\hat{N}_{\text{ext}} > 105$), l'estimation par couverture et Chao1 ponctuel est falsifiée par défaut (validant une forte hétérogénéité proche du modèle saturé ou l'existence d'une censure commune aux trois premières sources levée par $S_{\text{ext}}$). Si $K_{\text{nouv}} \le 3$ (illustratif), le modèle log-linéaire saturé ($\hat{N}=186,3$) est falsifié par excès.

---

### (d) Ancrage matériel

Aucun modèle de langage ni processeur graphique (GPU) n'est requis : ce protocole n'exécute que des simulations Monte Carlo tabulaires et des ajustements de modèles linéaires généralisés (Poisson). Sur un processeur standard (CPU 8 cœurs, illustratif), $100\,000$ réplications (illustratif) des plans des blocs 2 et 3 s'exécutent en moins de 3 minutes (illustratif), pour un coût matériel inférieur à 0,05 € (illustratif) et moins de 1 Go de mémoire vive (illustratif).

FIN-DE-CELLULE
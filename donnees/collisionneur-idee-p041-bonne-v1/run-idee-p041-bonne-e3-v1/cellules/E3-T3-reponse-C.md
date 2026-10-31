Le contenu des familles, le choix de bancs ou de jeux de données et l'organisation de ceux qui conçoivent les familles sont hors tour.

---

# (a) Réponses aux critiques visant la proposition C

### Critiques de la proposition A sur C

1. **Cible auxiliaire non identifiable ($u$ et $-u$ donnent la même loi $P_\theta$) [A.a.1, A.b, A.c] :**
   - **Statut : Acceptée et transformée en test.** Prédire le vecteur signé $u$ obligeait la tête à mémoriser un signe arbitraire propre à la famille. Nous corrigeons la paramétrisation cible : la cible auxiliaire devient injective par rapport à la loi, soit $\psi(\theta) = (\mu, \text{vech}(\Sigma - I_d))$ avec $\Sigma = I_d + \sum_{r=1}^R u_r u_r^\top$. Nous gardons en contrôle le duel entre cible non identifiable $(\mu, u)$ et cible injective $(\mu, \text{vech}(\Sigma - I_d))$.
2. **Ciblage adverse asymétrique entre les bras 1 et 2 [A.a.2] :**
   - **Statut : Acceptée.** Si le générateur adapte les familles d'entraînement contre la défense du bras 1 et qu'on les rejoue au bras 2, l'effet de $\theta$ est confondu avec le ciblage. Correction : aux bras 1, 2 et 5, l'échéancier des $G=10$ générations est produit contre une défense pilote tierce (ou en rejeu croisé symétrique : moitié des mondes pilotés par le bras 1, moitié par le bras 2). Le bras 4 garde sa propre boucle adaptative (protocole du champ, fait 9, RAPPORTÉ).
3. **Test de reparamétrisation sous mode « cible auxiliaire » et bruit de réentraînement [A.a.3, A.a.4, A.b, A.c] :**
   - **Statut : Acceptée.** Une tête de régression profonde absorberait toute bijection lisse $\phi$, rendant le test aveugle, et le contrôle sur le bras 2 ($\Delta=0$ exactement) n'étalonnait pas la variance de réentraînement $\sigma_{\text{retrain}}$. Correction : la tête auxiliaire est restreinte à une projection strictement linéaire $W_{\text{aux}} h(x)$ depuis la représentation interne $h(x)$ ; ainsi, une reparamétrisation non linéaire $\phi(\theta)$ force la représentation $h(x)$ elle-même à changer si elle encode les coordonnées plutôt que la statistique exhaustive du rapport de vraisemblance. De plus, le contrôle négatif devient le réentraînement du bras 1 sous $\phi = \text{Id}$ avec une nouvelle graine d'initialisation et de lots, mesurant le plancher $\sigma_{\text{retrain}}$.
4. **Validation tautologique de la mesure de dépendance $D_{W_2}$ et confusion support disjoint / difficulté intrinsèque [A.a.5, A.b, A.c] :**
   - **Statut : Acceptée.** Calculer $W_2$ analytiquement sur les vrais $(\mu, \Sigma)$ vérifiait un calcul algébrique, non un estimateur statistique, et séparer les supports par la norme modifiait la puissance oracle $p^*(\theta)$. Correction : (i) $D_{W_2}$ est estimée empiriquement par $\widehat{W}_2(P_{\theta_j}, P_{\theta_i})$ à partir des moments empiriques sur $L=200$ lots finis (illustratif), et comparée à sa valeur nulle $D_0$ (deux tirages indépendants de la même méta-distribution de familles) ; (ii) le régime de **support disjoint** est défini à **difficulté oracle constante** ($p^*(\theta)$ identique) en partitionnant $\mathbb{R}^{64}$ en deux sous-espaces orthogonaux $\mathcal{V}_{\text{ent}} \perp \mathcal{V}_{\text{ecart}}$ de dimension $32$ chacun, avec exactement les mêmes lois radiales pour $\|\mu\|_2$ et $\|\Sigma - I_d\|_F$.
5. **Budget omettant les requêtes du générateur et le palier rapide [A.a.6] :**
   - **Statut : Acceptée.** Le budget unifié est désormais compté en passages avant totaux de la défense ($B_{\text{pass}} = 60\,000$ lots de taille $b=32$, illustratif), incluant les requêtes du générateur aux bras 1, 2, 4, 5 et les mises à jour du palier rapide au bras 5.
6. **Contradiction entre condition d'échec en ET (bloc 3) et définition (bloc 5) [A.a.7] :**
   - **Statut : Acceptée.** La condition d'échec est harmonisée en disjonction logique (OU) : l'idée échoue pour la conception si $(ii)_1 - (ii)_2 < \delta$ OU $(iii)_1 - (iii)_2 < \delta$, et pour l'évaluation si $\Delta_{1,2} > -\delta$.
7. **Vérification mécanique hétérogène et taille d'étalonnage $N_0$ trop faible [A.a.8, A.b] :**
   - **Statut : Acceptée.** La statistique de lot de la vérification mécanique est homogénéisée : $T_{\text{meca}}(X) = b \|\bar{X}\|_2^2 + \frac{b}{2}\|S_X - I_d\|_F^2$ (test joint de moyenne et covariance sur un lot $X$ de $b=32$ vecteurs, illustratif). Le nombre de lots honnêtes pour étalonner le seuil $\tau$ à $1\,\%$ de fausses alertes passe à $N_{\text{lots},0} = 10\,000$ lots ($320\,000$ vecteurs tirés de $P_0$, illustratif), réduisant l'écart-type binomial du taux de fausses alertes à $\approx 0{,}1\,\text{pp}$ (illustratif).
8. **Score (iii) : nature de la sortie vue par le générateur et regret par bras [A.b, A.c] :**
   - **Statut : Acceptée.** Conformément au fait 4 (HYPOTHÈSE), nous déclarons que la sortie de la défense vue par le générateur est le score continu $D(X) \in \mathbb{R}$ avant seuillage, et nous mesurons le regret par bras contre l'oracle analytique.

---

### Critiques de la proposition B sur C

1. **Perturbation de covariance de rang 1 trop favorable [B.a.1, B.b] :**
   - **Statut : Transformée en test.** Nous généralisons le schéma paramétrique à une perturbation de rang $R$ modulable : $\Sigma = I_d + U U^\top$ avec $U \in \mathbb{R}^{d \times R}$, en opposant $R=1$ (rang 1) et $R=8$ (rang modéré, illustratif) à norme de Frobenius $\|U U^\top\|_F$ égale.
2. **Puissance statistique (63 %) insuffisante avec $\delta = 0{,}03$, $\sigma = 0{,}08$ et $M=200$ [B.a.2] :**
   - **Statut : Acceptée.** L'objection sur le rapport signal/bruit inter-mondes est fondée : en appariant les mondes par graine (mêmes familles d'entraînement et tenues à l'écart entre bras 1 et 2, plus soustraction de l'oracle $p^*$), l'écart-type de la différence appariée $\hat{\Delta}_{1,2}$ tombe à $\sigma_{\text{diff}} = 0{,}05$ (illustratif) et nous portons le nombre de mondes simulés à $M = 400$ (illustratif), assurant une puissance $> 90\,\%$ au seuil $\alpha = 0{,}05$ pour $\delta = 0{,}03$ (illustratif).
3. **Intervalle de Clopper-Pearson au score (iii) conditionnel à $\hat{\theta}^*$ [B.a.3] :**
   - **Statut : Acceptée.** Clopper-Pearson sur $L=200$ lots frais ne mesure que le bruit d'évaluation conditionnel au point $\hat{\theta}^*$ trouvé dans un monde. L'inférence décisive entre bras utilise désormais uniquement l'intervalle de confiance par bootstrap / Student sur les $M=400$ mondes simulés indépendants (où le générateur est relancé à chaque monde).
4. **Contrôle négatif $\theta=0$ insuffisant sans contrôle de difficulté et de convergence de la tête auxiliaire [B.a.4, B.c] :**
   - **Statut : Acceptée.** Nous ajoutons : (i) l'exigence de non-saturation de l'oracle ($p^*(\theta) \in [0{,}40 ; 0{,}90]$ en moyenne sur $\Theta$, illustratif) ; (ii) un audit de convergence de la tête auxiliaire ($R^2 \ge 0{,}50$ sur validation, illustratif) ; (iii) un bras témoin $2'$ (même architecture à deux têtes qu'au bras 1, mais poids de la perte auxiliaire mis à $0$ ou gradients auxiliaires annulés) pour isoler l'effet de capacité.
5. **Score (i) élevé au bras 1 vrai par construction [B.a.5] :**
   - **Statut : Rejetée avec sa raison.** Le score (i) est évalué sur de *nouveaux lots* tirés des familles d'entraînement après le gel de la défense, avec la tête auxiliaire supprimée. Si la tête auxiliaire avait simplement cannibalisé la capacité de l'encodeur au détriment de la tête de détection binaire, $(i)_1$ serait inférieur à $(i)_2$. De plus, conformément au bloc 5, un gain sur (i) seul ne suffit jamais à déclarer l'idée bonne.
6. **Transformation $\phi = \sinh$ trop proche de l'identité sur les petites valeurs [B.b] :**
   - **Statut : Acceptée.** Pour que le test de reparamétrisation ait une forte puissance, nous remplaçons $\sinh$ par un difféomorphisme fortement non linéaire et couplant les coordonnées : $\phi(\psi)_j = \text{sign}(\psi_j)\cdot |\psi_j|^3 + 0{,}5\,\sin(\psi_{(j+1)\bmod p})$ (illustratif), normalisé à variance unité pour ne pas dégrader le conditionnement numérique de l'optimisation.

---

### Critiques de la proposition D sur C

1. **Conflit de trajectoires adaptatives entre bras 1 et 2 [D.a.1, D.c.2] :**
   - **Statut : Acceptée.** Identique à A.a.2 ; corrigé par l'échéancier commun sur défense pilote ou rejeu croisé symétrique.
2. **Signes de $(i)-(ii)$ et $(ii)-(iii)$ non garantis par la seule géométrie [D.a.2, D.b] :**
   - **Statut : Acceptée.** Les signes prédits ne sont valides que sous deux conditions mesurables que nous rendons explicites : (1) **isonomie de difficulté intrinsèque** entre l'entraînement et l'écart ($|\mathbb{E}_{\text{ent}}[p^*(\theta)] - \mathbb{E}_{\text{ecart}}[p^*(\theta)]| \le 0{,}01$, illustratif) ; (2) **efficacité du générateur** (regret $R_b = \hat{S}_{(iii),b} - \inf_{\theta \in \Theta} p_b(\theta) < \frac{1}{2}[\hat{S}_{(ii),b} - \inf_{\theta \in \Theta} p_b(\theta)]$).
3. **Définition des supports commun et disjoint sans biais de difficulté [D.a.3, D.c.2] :**
   - **Statut : Acceptée.** Corrigé (voir réponse à A.a.5) par la séparation en sous-espaces orthogonaux $\mathcal{V}_{\text{ent}} \perp \mathcal{V}_{\text{ecart}}$ à normes $\|\mu\|_2$ et $\|U U^\top\|_F$ strictement appariées en loi.
4. **Validation de $D_{W_2}$ sur échantillons finis et discordance entre $\phi$ des témoins et de l'expérience [D.a.4, D.a.5, D.c.3, D.c.4] :**
   - **Statut : Acceptée.** $\widehat{D}_{W_2}$ est désormais estimée sur échantillons finis avec soustraction du biais de plancher $\widehat{D}_0$, et la même bijection cubique couplée $\phi$ est utilisée pour les défenses témoins ($D_{\text{loi}}$, $D_{\text{param}}$) et pour le duel 2.
5. **Contrôle nul $\theta = (0,0)$ hors de $\Theta$ et biais de sélection du minimum sous $P_0$ [D.a.6, D.c.1] :**
   - **Statut : Acceptée.** L'observation est exacte : d'une part $\|\mu\|_2 \in [0{,}5 ; 3{,}0]$ excluait $0$, d'autre part chercher le minimum sur $500$ évaluations bruitées sous $P_0$ donne un score (iii) inférieur à $0{,}01$ même sans déplacement. Correction : (i) nous incluons $\theta_0 = (0,0)$ comme point de contrôle dédié $\Theta_0 = \Theta \cup \{\theta_0\}$ ; (ii) pour le score (iii), la réévaluation sur $L=200$ lots frais *indépendants des lots d'optimisation* élimine le biais de sélection par minimum : sous un monde plat ($P_\theta = P_0$ partout), quel que soit le point $\hat{\theta}^*$ choisi par le générateur, sa réévaluation sur lots frais a exactement pour espérance $0{,}01$.
6. **Neutralisation du palier rapide au bras 5 [D.a.7, D.c.5] :**
   - **Statut : Acceptée.** Le contrôle négatif du bras 5 fige les seuils rapides à $0$ et désactive la mémoire de prototypes dès le lot $1$, devant reproduire le bras 1 à graine égale ($|\hat{\Delta}_{5_{\text{gel}}, 1}| < 0{,}005$, illustratif).

---

# (b) Expériences décisives et instruments corrigés

### Schéma statistique et mode déclarés (corrigés)
Dans $\mathbb{R}^{64}$ ($d=64$, illustratif), $P_0 = \mathcal{N}(0, I_{64})$. Une famille $k$ a pour loi $P_{\theta_k} = \mathcal{N}(\mu_k, \Sigma_k)$ avec $\Sigma_k = I_{64} + U_k U_k^\top$ ($U_k \in \mathbb{R}^{64 \times R}$, rang $R \in \{1, 8\}$, $\|\mu_k\|_2 \in [0{,}5 ; 2{,}0]$, $\|U_k U_k^\top\|_F \in [0{,}5 ; 2{,}0]$, choisis pour que la puissance du rapport de vraisemblance oracle $p^*(\theta_k) \in [0{,}45 ; 0{,}85]$, tous chiffres illustratifs).
- **Paramètre injectif (cible auxiliaire)** : $\psi(\theta_k) = (\mu_k, \text{vech}(U_k U_k^\top))$ normalisé par coordonnée. Au bras 1 et au bras 5, la défense partage un encodeur $h_w(X)$ entre la tête de détection $D_w(X) = v^\top h_w(X)$ et une tête auxiliaire **strictement linéaire** $W_{\text{aux}} h_w(X)$ prédisant $\psi(\theta_k)$ pendant l'entraînement seul.
- **Supports à difficulté appariée** : $\mathbb{R}^{64} = \mathcal{V}_{\text{ent}} \oplus \mathcal{V}_{\text{ecart}}$ ($32 + 32$ dimensions orthogonales). En **support commun**, les familles tenues à l'écart ont leurs paramètres $(\mu_j, U_j)$ tirés dans $\mathcal{V}_{\text{ent}}$ selon la même loi que l'entraînement ; en **support disjoint**, ils sont tirés dans $\mathcal{V}_{\text{ecart}}$ avec exactement les mêmes lois de normes (donc $\mathbb{E}[p^*(\theta)]$ identique à $10^{-3}$ près, illustratif).
- **Couplage et budget** : $M = 400$ mondes simulés (illustratif). Budget strictement égal de $B_{\text{pass}} = 60\,000$ évaluations de lots ($b=32$) par bras à l'entraînement (incluant la génération adaptative et le palier rapide). Les bras 1, 2 et 5 reçoivent exactement la même séquence de familles d'entraînement (générées contre une défense pilote séparée). Seuil $\tau_b$ étalonné sur $N_{\text{lots},0} = 10\,000$ lots de $P_0$ frais ($\text{FAR} = 1{,}0\,\% \pm 0{,}1\,\%$, illustratif).

### Duels corrigés ($H_A$ contre $H_B$)

1. **Duel 1 — Quantité qui tranche (Bloc 4) :**
   - $H_A : \Delta_{1,2} = [(ii)_1 - (iii)_1] - [(ii)_2 - (iii)_2] \le -0{,}03$ (illustratif) en support disjoint à difficulté oracle appariée.
   - $H_B : \Delta_{1,2} > -0{,}03$ (illustratif).
   - **Contrôles négatifs** : (a) **Triptyque de capacité et d'information** : Bras $2'$ (tête auxiliaire présente mais gradient annulé : vérifie l'absence d'artefact architectural, $|\hat{\Delta}_{2',2}| < 0{,}01$), Bras $1_{\text{perm}}$ ($\psi(\theta_k)$ permuté entre familles : mesure la mémorisation d'identité), Bras $1_{\text{bruit}}$ ($\tilde{\psi}$ tiré aléatoirement à chaque lot) ; (b) **Monde plat** ($P_\theta = P_0$) avec réévaluation sur $L=200$ lots frais : $(ii)_b \approx (iii)_b \approx 0{,}01 \pm 0{,}002$ (illustratif).
   - **Falsification** : IC à $95\,\%$ sur les $M=400$ mondes de $\hat{\Delta}_{1,2}$ entièrement $\le -0{,}03$ falsifie $H_B$ ; borne inférieure $> -0{,}03$ falsifie $H_A$.

2. **Duel 2 — Test de reparamétrisation (Lois contre Coordonnées) :**
   - **Transformation** : Difféomorphisme cubique couplé normalisé $\phi(\psi)_j = c_1 (\text{sign}(\psi_j)|\psi_j|^3 + 0{,}5\sin(\psi_{j+1})) - c_0$, choisi par l'arbitre et appliqué aux cibles d'entraînement du bras $1'$ (avec tête linéaire $W_{\text{aux}}$).
   - $H_A$ (apprentissage des lois) : $|\Delta_{\text{reparam}}| = |(ii)_1 - (ii)_{1'}| \le 0{,}02$ (illustratif) ET la tête auxiliaire converge ($R^2 \ge 0{,}50$).
   - $H_B$ (surajustement aux coordonnées) : $|\Delta_{\text{reparam}}| > 0{,}02$ (illustratif).
   - **Contrôles négatifs** : (a) **Plancher de réentraînement** : réentraîner le bras 1 sous $\phi = \text{Id}$ avec une nouvelle graine ($\sigma_{\text{retrain}}$ doit vérifier $2\sigma_{\text{retrain}}/\sqrt{M} < 0{,}005$, illustratif) ; (b) **Contrôle d'identifiabilité** : comparer $(ii)_1$ avec cible injective $(\mu, \text{vech}(UU^\top))$ contre cible ambiguë $(\mu, U)$.
   - **Falsification** : IC à $95\,\%$ de $|\hat{\Delta}_{\text{reparam}}|$ inclus dans $[0 ; 0{,}02]$ (avec $R^2 \ge 0{,}50$) falsifie $H_B$ ; borne inférieure $> 0{,}02$ falsifie $H_A$.

3. **Duel 3 — Deux échelles de temps (Bras 5 contre Bras 1) ET Rang $R=1$ contre $R=8$ :**
   - $H_A : \Delta_{5,1} = (iii)_5 - (iii)_1 \ge 0{,}03$ (illustratif) en support disjoint, tant pour $R=1$ que pour $R=8$.
   - $H_B : \Delta_{5,1} < 0{,}03$ (illustratif).
   - **Contrôle négatif** : Bras $5_{\text{gel}}$ (palier rapide gelé à zéro, mémoire désactivée) reproduisant $(iii)_1$ à $0{,}005$ près (illustratif).

### Instruments corrigés (section c)
- **Oracle $p^*(\theta)$ et Vérification mécanique** : Pour chaque famille, le test de Neyman-Pearson exact $\Lambda(X) = \sum_{i=1}^b [\log P_\theta(X_i) - \log P_0(X_i)]$ fournit le plafond oracle $p^*(\theta)$, et $T_{\text{meca}}(X) = b\|\bar{X}\|_2^2 + \frac{b}{2}\|S_X - I_d\|_F^2$ fournit le plancher sans apprentissage. Toute défense valide doit vérifier $T_{\text{meca}} + 0{,}05 \le \hat{S}_{(ii)} \le p^*$ (illustratif).
- **Générateur adaptatif** : Évalué sur les sorties continues $D(X)$, budget $B_{\text{eval}} = 500$ lots pour choisir $\hat{\theta}^*$, suivi d'une réévaluation sur $L=200$ lots frais. Critère de saturation exigé par bras : lancer un contrôle à $10 \times B_{\text{eval}} = 5\,000$ lots sur $50$ mondes ; le regret empirique $\hat{S}_{(iii)}(500) - \hat{S}_{(iii)}(5000)$ doit être $\le \delta / 3 = 0{,}01$ (illustratif), sinon $B_{\text{eval}}$ est augmenté.
- **Mesure de dépendance $\widehat{D}_{W_2}$** : Estimée sur les moyennes et covariances empiriques des lots finis, normalisée par le plancher de bruit $\widehat{D}_0$ (deux échantillons indépendants du même support) : $\widetilde{D}_{W_2} = \widehat{D}_{W_2}(\mathcal{K}_{\text{ent}}, \mathcal{K}_{\text{ecart}}) - \widehat{D}_0$. À difficulté oracle $p^*$ constante, on teste la pente $\alpha > 0$ de $[(i) - (ii)] - [(i)^* - (ii)^*] \approx \alpha \widetilde{D}_{W_2}$.

---

# (c) Réponse à la question de l'arbitre (en une page)

### 1. Verdict et condition mesurable
Au sens strict des définitions du bloc 5, l'idée P-041 est **conditionnellement bonne pour les deux (conception et évaluation)** — mais **aucun résultat n'est aujourd'hui établi** (rien n'est lancé, fait 3, VÉRIFIÉ). Elle ne sera validée qu'à la **condition mesurable conjointe** que, sur $M=400$ mondes simulés (illustratif) en régime de **support disjoint à difficulté oracle $p^*$ appariée** :
1. **Conception** : Le bras 1 (informé de la cible injective $\psi(\theta)$ via tête linéaire) surpasse le bras 2 (échantillons seuls, même échéancier de familles et même budget total $B_{\text{pass}}$) d'au moins $\delta = 0{,}03$ (illustratif) à la fois sur les familles tenues à l'écart $[\hat{S}_{(ii),1} - \hat{S}_{(ii),2} \ge 0{,}03]$ et sur le pire cas adaptatif réévalué sur lots frais $[\hat{S}_{(iii),1} - \hat{S}_{(iii),2} \ge 0{,}03]$, tout en battant le témoin de capacité sans information (bras $2'$).
2. **Évaluation** : La quantité qui tranche vérifie $\hat{\Delta}_{1,2} \le -0{,}03$ (IC à $95\,\%$ excluant $-0{,}03$, illustratif).
3. **Invariance et légitimité** : L'information $\psi(\theta)$ est strictement confinée à l'entraînement des poids (exclue de la sélection du modèle, de l'étalonnage du seuil $\tau$ sur $P_0$ et des mesures finales), le test de reparamétrisation non linéaire vérifie $|\hat{\Delta}_{\text{reparam}}| \le 0{,}02$ (illustratif) avec convergence avérée de la tête auxiliaire ($R^2 \ge 0{,}50$), et le chiffre publié demeure exclusivement le score $(iii)$ où le générateur joue en dernier. Si l'avantage disparaît en support disjoint ou sous reparamétrisation, le verdict rétrograde immédiatement à **bonne pour aucune**.

### 2. Quantité qui tranche, signe prédit et seuil
$$\Delta_{1,2} = \big(S_{(ii),1} - S_{(iii),1}\big) - \big(S_{(ii),2} - S_{(iii),2}\big)$$
- **Signe prédit (HYPOTHÈSE)** : **Négatif** ($\Delta_{1,2} < 0$, prédiction illustrative $-0{,}04$), car la prédiction linéaire de $\psi(\theta) = (\mu, \text{vech}(\Sigma - I_d))$ contraint l'encodeur à extraire les statistiques exhaustives du rapport de vraisemblance sur tout le sous-espace d'entraînement, réduisant les directions aveugles exploitables par le générateur au score $(iii)$.
- **Seuil de décision et falsification** : Seuil minimal $\delta = 0{,}03$ ($3$ points de détection à $1\,\%$ de fausses alertes sur $P_0$, illustratif) ; l'hypothèse d'un gain pour l'évaluation est falsifiée si la borne inférieure de l'IC à $95\,\%$ apparié sur les $M=400$ mondes de $\hat{\Delta}_{1,2}$ est $> -0{,}03$.

### 3. Expérience décisive corrigée (en cinq lignes)
1. Dans $\mathbb{R}^{64}$ ($P_0 = \mathcal{N}(0,I_{64})$, $P_\theta = \mathcal{N}(\mu, I_{64}+UU^\top)$ de rang $R \in \{1,8\}$), on simule $M=400$ mondes opposant les 5 bras au même budget total de $60\,000$ lots ($b=32$), les bras 1, 2 et 5 recevant la même trajectoire de familles et un seuil $\tau$ étalonné sur $10\,000$ lots de $P_0$ ($\text{FAR}=1\,\%$, tous chiffres illustratifs).
2. Le bras 1 prédit la cible injective $\psi(\theta) = (\mu, \text{vech}(UU^\top))$ via une tête linéaire supprimée après l'entraînement, tandis que le bras 2 n'observe que les lots $X$ et que le bras $2'$ neutralise les gradients auxiliaires à architecture identique.
3. On évalue $(i)$, $(ii)$ et $(iii)$ (ce dernier après $B_{\text{eval}}=500$ requêtes continues du générateur, vérifié à regret $\le 0{,}01$ contre $5\,000$ requêtes, puis réévalué sur $L=200$ lots frais, illustratifs) dans deux régimes orthogonaux ($\mathcal{V}_{\text{ent}} \perp \mathcal{V}_{\text{ecart}}$) de même difficulté oracle $p^*(\theta)$.
4. On applique à l'entraînement du bras $1'$ le difféomorphisme cubique couplé $\phi(\psi)$ pour tester $|\hat{\Delta}_{\text{reparam}}| \le 0{,}02$ au-dessus du plancher de réentraînement à graine fraîche $\sigma_{\text{retrain}}$ (illustratif).
5. On tranche par les IC à $95\,\%$ appariés sur les $400$ mondes pour $(ii)_1-(ii)_2$, $(iii)_1-(iii)_2$, $\Delta_{1,2}$ et $(iii)_5-(iii)_1$ contre le seuil $\delta = 0{,}03$ (illustratif).

### 4. Ce qui est établi et ce qui ne l'est pas
- **Établi** : L'objectif du programme est l'universalité sur familles inédites avec lecture unique de `test_final` (faits 1 et 2, VÉRIFIÉ) ; l'idée P-041 donne $\theta$ à la défense à l'entraînement mais rien n'en est construit ni mesuré (fait 3, VÉRIFIÉ) ; le champ évalue la défense figée en faisant jouer le générateur en dernier (faits 6 à 8, RAPPORTÉ) et l'amélioration itérative de la défense peut surestimer sa performance (fait 7, RAPPORTÉ) ; l'entraînement au pire cas dans une classe a un transfert mitigé hors classe, parfois négatif (fait 11, RAPPORTÉ) ; mathématiquement, une cible non injective comme $(\mu, u)$ introduit une variance parasite d'étiquetage et une réévaluation sur lots frais élimine le biais d'optimisation du score $(iii)$ (VÉRIFIÉ par calcul).
- **Non établi (HYPOTHÈSES à tester)** : Que prédire $\psi(\theta)$ à budget égal améliore $(ii)$ et $(iii)$ en support disjoint ($\mathcal{V}_{\text{ecart}} \perp \mathcal{V}_{\text{ent}}$) ; que cela réduise l'optimisme d'évaluation ($\Delta_{1,2} \le -0{,}03$) ; que recevoir les épreuves et scores passés (fait 9, RAPPORTÉ) équivaille informationnellement à recevoir $\theta$ ; et que le découplage en deux échelles de temps (bras 5) aide hors support au lieu de surajuster.

### 5. Expérience à faire en premier
Lancer en premier l'étalonnage à vérité connue des instruments et du duel Bras 1 contre Bras 2 et Bras $2'$ (tête linéaire sur cible injective $\psi(\theta)$, $R=1$ et $R=8$, trajectoire de familles partagée, réévaluation de $(iii)$ sur lots frais) en régime de support disjoint orthogonal à difficulté oracle $p^*$ appariée sur $M=400$ mondes simulés (illustratif).

FIN-DE-CELLULE
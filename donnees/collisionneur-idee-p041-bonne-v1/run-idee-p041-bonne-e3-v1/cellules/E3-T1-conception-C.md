Le contenu des familles, le choix de bancs ou de jeux de données et l'organisation de ceux qui conçoivent les familles sont hors tour.
Classe paramétrique déclarée pour tout le tour : dans $\mathbb{R}^d$ ($d=64$, illustratif), la loi de référence des cas honnêtes est $P_0 = \mathcal{N}(0, I_d)$. Une famille $k$ a pour paramètre $\theta_k = (\mu_k, u_k) \in \Theta \subset \mathbb{R}^d \times \mathbb{R}^d$ (avec $\|\mu_k\|_2 \in [0{,}5 ; 3{,}0]$ et $\|u_k\|_2 \in [0 ; 2{,}0]$, illustratif) et pour loi $P_{\theta_k} = \mathcal{N}(\mu_k, I_d + u_k u_k^\top)$.

---

### (a) Ce que la question suppose sans que ce soit établi

- HYPOTHÈSE : Fournir $\theta$ comme cible auxiliaire à prédire depuis les activations améliore l'estimation de la statistique de détection par rapport à l'observation des seuls échantillons à budget égal.
- HYPOTHÈSE : Le générateur adaptatif (procédure d'optimisation boîte noire, fait 4) approche le vrai pire cas dans $\Theta$ en un budget fini d'évaluations de la défense figée.
- HYPOTHÈSE : L'écart entre familles d'entraînement et familles tenues à l'écart s'explique par une divergence géométrique mesurable dans l'espace des lois $\{P_\theta\}$.
- HYPOTHÈSE : Un test de reparamétrisation bijective $\phi(\theta)$ appliquée aux cibles d'entraînement isole l'apprentissage intrinsèque des lois $P_\theta$ d'un surajustement aux coordonnées de $\theta$.
- HYPOTHÈSE : Une architecture à deux échelles de temps (palier rapide de règles et palier lent de poids) transfère mieux hors support qu'une mise à jour monolithique.
- RAPPORTÉ : Recevoir $\theta$ à l'entraînement diffère structurellement de l'observation d'une base croissante d'épreuves et de leurs scores (fait 9), l'équivalence informationnelle n'étant pas établie.

---

### (b) Expériences décisives en duel $H_A$ contre $H_B$

#### Duel 1 — Effet de l'information paramétrique sur l'écart d'évaluation (Bloc 4)
- **Hypothèses** : $H_A$ : L'entraînement avec $\theta$ réduit l'optimisme de l'évaluation statique, soit $\Delta_{1,2} = [(ii)_1 - (iii)_1] - [(ii)_2 - (iii)_2] \le -\delta$. $H_B$ : Il ne le réduit pas ou l'accroît ($\Delta_{1,2} > -\delta$).
- **Métrique et seuil** : Estimateur empirique $\hat{\Delta}_{1,2}$ moyenné sur $M=200$ (illustratif) mondes simulés ; seuil d'effet minimal $\delta = 0{,}03$ (3 points de détection à 1 % de fausses alertes, illustratif).
- **Contrôle négatif** : Remplacer $\theta_k$ au bras 1 par un vecteur aléatoire $\tilde{\theta}_k \sim \text{Unif}(\Theta)$ indépendant des activations ; on doit observer $|\hat{\Delta}_{1,2}| < 0{,}01$ (illustratif).
- **Falsification** : Si la borne supérieure de l'IC à 95 % de $\hat{\Delta}_{1,2}$ est $\le -0{,}03$, $H_B$ est falsifiée. Si la borne inférieure est $> -0{,}03$, $H_A$ est falsifiée.

#### Duel 2 — Apprentissage des lois contre apprentissage de la paramétrisation
- **Hypothèses** : $H_A$ : La défense du bras 1 apprend des invariants des lois $P_\theta$ (invariance par reparamétrisation bijective non linéaire $\phi : \Theta \to \Theta'$ à lois identiques $P'_{\phi(\theta)} = P_\theta$). $H_B$ : La défense dépend de la géométrie spécifique des coordonnées $\theta$ choisies.
- **Métrique et seuil** : Écart de performance au score (ii) entre le bras 1 entraîné avec cibles $\theta$ et le bras 1' entraîné sur les mêmes tirages avec cibles transformées $\phi(\theta)$ : $\Delta_{\text{reparam}} = (ii)_1 - (ii)_{1'}$. Seuil de tolérance $\epsilon = 0{,}02$ (illustratif).
- **Contrôle négatif** : Appliquer $\phi$ au bras 2 (qui n'utilise pas $\theta$) ; par construction, $\Delta_{\text{reparam}} = 0$ exactement à graine fixée.
- **Falsification** : Si $|\hat{\Delta}_{\text{reparam}}| > 0{,}02$ avec IC à 95 % excluant $0$, $H_A$ est falsifiée. Si l'IC à 95 % de $\hat{\Delta}_{\text{reparam}}$ est entièrement contenu dans $[-0{,}02 ; +0{,}02]$, $H_B$ est falsifiée.

#### Duel 3 — Deux échelles de temps (bras 5) contre une seule (bras 1) en support disjoint
- **Hypothèses** : $H_A$ : Le découplage en deux paliers (bras 5) augmente le score pire cas $(iii)$ en régime de support disjoint par rapport au bras 1 : $\Delta_{5,1} = (iii)_5 - (iii)_1 \ge \delta$. $H_B$ : Le palier rapide surajuste aux familles d'entraînement ou n'apporte aucun gain ($\Delta_{5,1} < \delta$).
- **Métrique et seuil** : Différence $\hat{\Delta}_{5,1}$ sur $M=200$ mondes (illustratif), seuil $\delta = 0{,}03$ (illustratif).
- **Contrôle négatif** : Geler le palier rapide à l'initialisation (mémoire vide, règles neutres) ; on doit retrouver $|\hat{\Delta}_{5,1}| < 0{,}01$ (illustratif).
- **Falsification** : Borne inférieure de l'IC à 95 % de $\hat{\Delta}_{5,1} \ge 0{,}03$ falsifie $H_B$ ; borne supérieure $< 0{,}03$ falsifie $H_A$.

---

### (c) Mesure minimale de chaque instrument nommé

Plan de simulation à vérité connue : $P_0 = \mathcal{N}(0, I_{64})$ et $P_\theta = \mathcal{N}(\mu, I_{64} + u u^\top)$. Les cas honnêtes appariés sont $N_0 = 10\,000$ tirages de $P_0$ à graine fixée (illustratif). La vérification mécanique à battre est le test de la distance de Mahalanobis empirique $\|x\|_2^2 + (\text{trace}(S_n) - d)^2$ sur lots de taille $b=32$ (illustratif), sans apprentissage, étalonné au quantile $99\,\%$ sur $P_0$. Contrôle négatif global : sous $\theta = (0,0)$ ($P_\theta = P_0$), le taux de détection de toute défense doit être de $1\,\% \pm 0{,}2\,\%$ (illustratif).

1. **Défense** : Mesurée par son taux de fausses alertes sur $P_0$ (doit être dans $[0{,}8\,\% ; 1{,}2\,\%]$, illustratif) et son taux de détection sur $\theta$ connu ($\|\mu\|_2 = 1{,}0, \|u\|_2 = 1{,}0$, illustratif). Elle fonctionne si son taux de détection dépasse la vérification mécanique d'au moins $0{,}05$ (illustratif).
2. **Générateur adaptatif** : Contre une défense analytique figée dont le pire cas exact $\theta^* = \arg\min_{\theta \in \Theta} \text{Puissance}(\theta)$ est connu par construction (ex. déplacement orthogonal au sous-espace linéaire projeté par la défense), on mesure l'écart de regret $R = \text{Score}(\hat{\theta}_{\text{gen}}) - \text{Score}(\theta^*)$ après $B_{\text{eval}} = 500$ évaluations (illustratif). Fonctionne si $R \le 0{,}02$ (illustratif).
3. **Mesure de dépendance** : Distance de Wasserstein-2 minimale entre ensembles de lois : $D(\mathcal{K}_{\text{ent}}, \mathcal{K}_{\text{ecart}}) = \frac{1}{|\mathcal{K}_{\text{ecart}}|} \sum_{j \in \mathcal{K}_{\text{ecart}}} \min_{i \in \mathcal{K}_{\text{ent}}} W_2(P_{\theta_j}, P_{\theta_i})$, où $W_2^2(\mathcal{N}(\mu_1, \Sigma_1), \mathcal{N}(\mu_2, \Sigma_2))$ est connu analytiquement. Dans deux mondes construits avec $D_{\text{vrai}} = 0{,}2$ (support commun) et $D_{\text{vrai}} = 2{,}5$ (support disjoint, chiffres illustratifs), l'instrument fonctionne s'il retrouve $D$ à $10^{-4}$ près (illustratif).
4. **Test de reparamétrisation** : On construit deux défenses synthétiques : $D_{\text{loi}}$ (calculant le rapport de vraisemblance exact de $P_\theta$ contre $P_0$) et $D_{\text{param}}$ (dont les poids sont forcés à dépendre linéairement des coordonnées brutes $\theta$ soumises à un pliage cubique $\phi(\theta) = \theta^3$). L'instrument fonctionne s'il donne $|\Delta_{\text{reparam}}| < 0{,}005$ sur $D_{\text{loi}}$ et $|\Delta_{\text{reparam}}| > 0{,}15$ sur $D_{\text{param}}$ (illustratifs).

---

### Bloc 1 — Compatibilité des deux règles

Mode déclaré : $\theta$ est fourni à la défense uniquement comme cible auxiliaire à prédire (tête de régression jointe depuis les activations) pendant l'entraînement ; à l'évaluation, cette tête est ignorée et seules les activations entrent dans la défense.

Sous ce mode, les deux règles sont compatibles : donner $\theta$ à l'entraînement (défense en dernier) agit comme un régularisateur de représentation qui contraint les couches internes à extraire des statistiques exhaustives de $P_\theta$, tandis que faire jouer le générateur en dernier à l'évaluation (faits 6 à 8) mesure la robustesse dans le pire cas de la défense figée. Ce que l'avantage des paramètres peut améliorer est l'efficacité d'échantillonnage de la défense apprise ; ce qu'il peut fausser est le chiffre publié si l'évaluation réutilise les familles où $\theta$ a été dévoilé.

L'avantage des paramètres cesse d'être légitime dès la fin de l'entraînement des poids, c'est-à-dire avant :
1. **La sélection de la défense** (choix des hyperparamètres et du point de contrôle), qui doit se faire à l'aveugle sans $\theta$, sur un ensemble de validation de familles distinctes des familles d'entraînement, pour ne pas sélectionner un modèle qui surajuste à la géométrie du régularisateur ;
2. **L'étalonnage du seuil de détection** ($1\,\%$ de fausses alertes), qui s'effectue uniquement sur des tirages de la loi de référence $P_0$ (où $\theta$ n'existe pas) ;
3. **La mesure finale** (scores (ii) et (iii)), où la défense et son seuil sont totalement figés.

---

### Bloc 2 — Trois scores et dépendance

Soit $D : \mathbb{R}^{b \times d} \to \mathbb{R}$ la défense figée opérant sur un lot $X$ de $b=32$ activations (illustratif), et $\tau$ le seuil fixé tel que $\mathbb{P}_{X \sim P_0^{\otimes b}}(D(X) > \tau) = 0{,}01$. Pour une famille $\theta_k$, le taux de détection vrai est $p(\theta_k) = \mathbb{P}_{X \sim P_{\theta_k}^{\otimes b}}(D(X) > \tau)$, estimé par $\hat{p}(\theta_k) = \frac{1}{L}\sum_{\ell=1}^L \mathbb{I}(D(X_{k,\ell}) > \tau)$ sur $L=200$ lots indépendants (illustratif).

- **Score (i)** : Moyenne $\hat{S}_{(i)} = \frac{1}{K_{\text{ent}}} \sum_{k=1}^{K_{\text{ent}}} \hat{p}(\theta_k)$ sur les $K_{\text{ent}}=50$ (illustratif) familles vues à l'entraînement (nouveaux tirages). Unité d'échantillonnage : la famille $\theta_k$ ; intervalle de confiance (IC) à $95\,\%$ par bootstrap non paramétrique sur les $K_{\text{ent}}$ familles.
- **Score (ii)** : Moyenne $\hat{S}_{(ii)} = \frac{1}{K_{\text{ecart}}} \sum_{j=1}^{K_{\text{ecart}}} \hat{p}(\theta_j)$ sur les $K_{\text{ecart}}=50$ (illustratif) familles tenues à l'écart. Unité d'échantillonnage : la famille $\theta_j$ ; IC à $95\,\%$ par bootstrap sur les $K_{\text{ecart}}$ familles.
- **Score (iii)** : Pire cas mesuré $\hat{S}_{(iii)} = \hat{p}(\hat{\theta}^*)$, où $\hat{\theta}^* = \arg\min_{\theta \in \Theta} \hat{p}_{\text{opt}}(\theta)$ est choisi par le générateur après $B_{\text{eval}}=500$ (illustratif) requêtes à la défense figée, puis réévalué sur $L=200$ lots frais. Unité d'échantillonnage : le lot de réévaluation $X_\ell$ (ou le monde simulé en méta-analyse) ; IC à $95\,\%$ binomial exact de Clopper-Pearson sur les $L$ lots frais.

**Signes prédits** :
- $(i) - (ii) \ge 0$ dès que la distribution d'échantillonnage des familles tenues à l'écart s'écarte du support empirique des familles d'entraînement (biais de généralisation hors échantillon, fait 11).
- $(ii) - (iii) > 0$ dès que la variance de $p(\theta)$ sur $\Theta$ est non nulle et que le générateur explore efficacement $\Theta$, car la moyenne sur une mesure fixe majore l'infimum sur $\Theta$.

**Dépendance et mesure** : Au niveau des lois, les familles tenues à l'écart dépendent des familles d'entraînement par le recouvrement de leurs supports dans $(\Theta, W_2)$ et l'alignement de leurs directions de déplacement $(\mu, u)$. On la mesure par la distance de couverture moyenne $D_{W_2}(\mathcal{K}_{\text{ent}}, \mathcal{K}_{\text{ecart}}) = \frac{1}{K_{\text{ecart}}} \sum_{j=1}^{K_{\text{ecart}}} \min_{i \in \{1..K_{\text{ent}}\}} W_2(P_{\theta_j}, P_{\theta_i})$. On prédit que l'écart $(i) - (ii)$ croît de façon monotone (approximativement linéaire localement : $(i) - (ii) \approx \alpha \cdot D_{W_2}$, $\alpha > 0$) avec $D_{W_2}$.

---

### Bloc 3 — Expérience décisive à budget égal

**Budget déclaré** : Chaque bras dispose d'un budget strictement égal de $B_{\text{tot}} = 50\,000$ lots d'activations synthétiques (illustratif) générés pendant la phase d'entraînement ($G=10$ générations de $5$ familles, $1\,000$ lots par famille, illustratif) et du même nombre de mises à jour de gradient ($10\,000$ pas, illustratif). À l'évaluation (iii), le générateur reçoit $B_{\text{eval}} = 500$ évaluations de lots (illustratif) pour chaque bras.

**Déroulement des 5 bras** :
- **Bras 1** : Boucle de $G=10$ générations (les familles d'entraînement sont choisies adaptativement par le générateur à chaque génération). La défense reçoit les lots d'échantillons $X$ et les paramètres $\theta$ (cible auxiliaire).
- **Bras 2** : Même boucle de $G=10$ générations sur exactement les mêmes familles d'entraînement qu'au bras 1 (couplage des familles par génération). La défense reçoit uniquement les échantillons $X$, sans $\theta$.
- **Bras 3** : Familles fixes sans boucle ($50$ familles tirées uniformément dans le support d'entraînement au départ, même budget total de $50\,000$ lots). La défense reçoit uniquement les échantillons $X$, sans $\theta$.
- **Bras 4 (protocole du champ)** : Boucle de $G=10$ générations où, à chaque génération, le générateur joue en dernier contre la défense figée de la génération précédente pour produire de nouvelles épreuves ; la défense est réentraînée sur la banque cumulée (fait 9) en recevant les échantillons $X$ et les scores de détection passés de la défense, mais jamais les paramètres $\theta$.
- **Bras 5** : Même boucle de $G=10$ générations que le bras 1. La défense reçoit les échantillons $X$ et $\theta$, avec deux paliers : palier rapide (seuils de sous-règles et mémoire de prototypes validés par la vérité connue sur l'entraînement) mis à jour entre lots, et palier lent (poids du réseau) mis à jour entre générations. Les deux paliers sont gelés avant (ii) et (iii).

**Test de reparamétrisation** : Appliqué à l'étape d'**entraînement** (et de sélection). L'arbitre (externe aux deux joueurs) choisit une bijection non linéaire $\phi(\mu, u) = (\text{sinh}(\mu), \text{sinh}(u))$ avant l'entraînement : les lois $P_\theta$ d'où sont tirés les échantillons $X$ sont inchangées, mais l'étiquette fournie aux bras 1 et 5 est $\phi(\theta)$ au lieu de $\theta$.

**Seuils de décision, contrôle négatif et condition d'échec** :
- Seuil de supériorité entre bras : $\delta = 0{,}03$ (3 points de taux de détection à $1\,\%$ de fausses alertes, illustratif) avec IC à $95\,\%$ excluant $0$.
- Contrôle négatif : Évaluer les 5 bras sur des familles fictives où $\theta = (0,0)$ ($P_\theta = P_0$) ; tous les scores (i), (ii), (iii) doivent valoir $0{,}01 \pm 0{,}002$ (illustratif).
- Condition d'échec de l'idée : L'idée échoue si, en support disjoint, $(iii)_1 - (iii)_2 < 0{,}03$ ET $[(ii)_1 - (iii)_1] - [(ii)_2 - (iii)_2] > -0{,}03$, ou si le test de reparamétrisation fait chuter $(ii)_1$ de plus de $0{,}02$ (illustratif).

**Plan du calcul de puissance par simulation** : $M = 200$ mondes simulés indépendants (tirant à chaque fois de nouvelles familles d'entraînement et de nouvelles familles tenues à l'écart à graine scellée), $K=50$ familles par score, $L=200$ lots de taille $b=32$ par famille, pour détecter un effet supposé $\delta = 0{,}03$ (écart-type inter-mondes supposé $\sigma = 0{,}08$, test $t$ apparié bilatéral à $\alpha = 0{,}05$, chiffres illustratifs).

**Prédictions chiffrées (toutes marquées « illustratif », à $1\,\%$ de fausses alertes)** :

| Bras | Régime : Support commun $(i)$ | Support commun $(ii)$ | Support commun $(iii)$ | **Support commun $(ii) - (iii)$** | Régime : Support disjoint $(i)$ | Support disjoint $(ii)$ | Support disjoint $(iii)$ | **Support disjoint $(ii) - (iii)$** |
|---|---|---|---|---|---|---|---|---|
| **Bras 1 ($\theta$)** | $0{,}92$ | $0{,}89$ | $0{,}74$ | **$+0{,}15$** | $0{,}92$ | $0{,}70$ | $0{,}58$ | **$+0{,}12$** |
| **Bras 2 (échant.)** | $0{,}88$ | $0{,}84$ | $0{,}65$ | **$+0{,}19$** | $0{,}88$ | $0{,}66$ | $0{,}50$ | **$+0{,}16$** |
| **Bras 3 (fixe)** | $0{,}90$ | $0{,}85$ | $0{,}55$ | **$+0{,}30$** | $0{,}90$ | $0{,}60$ | $0{,}40$ | **$+0{,}20$** |
| **Bras 4 (champ)** | $0{,}89$ | $0{,}85$ | $0{,}70$ | **$+0{,}15$** | $0{,}89$ | $0{,}67$ | $0{,}53$ | **$+0{,}14$** |
| **Bras 5 (2 paliers)**| $0{,}94$ | $0{,}90$ | $0{,}76$ | **$+0{,}14$** | $0{,}94$ | $0{,}75$ | $0{,}64$ | **$+0{,}11$** |

---

### Bloc 4 — La quantité qui tranche

La quantité qui tranche est le double contraste d'optimisme d'évaluation entre le bras 1 (informé de $\theta$) et le bras 2 (informé par échantillons seuls) :
$$\Delta_{1,2} = \big(S_{(ii),1} - S_{(iii),1}\big) - \big(S_{(ii),2} - S_{(iii),2}\big)$$
- **Estimateur** : Moyenne empirique sur les $M$ mondes simulés :
$$\hat{\Delta}_{1,2} = \frac{1}{M}\sum_{m=1}^M \left[\big(\hat{S}_{(ii),1}^{(m)} - \hat{S}_{(iii),1}^{(m)}\big) - \big(\hat{S}_{(ii),2}^{(m)} - \hat{S}_{(iii),2}^{(m)}\big)\right]$$
- **Intervalle** : Intervalle de confiance à $95\,\%$ apparié par monde : $\hat{\Delta}_{1,2} \pm t_{M-1, \, 0{,}975} \frac{\hat{s}_\Delta}{\sqrt{M}}$, où $\hat{s}_\Delta$ est l'écart-type empirique des contrastes par monde.
- **Effet minimal qui compte** : $|\Delta_{1,2}| \ge \delta = 0{,}03$ (3 points de détection à $1\,\%$ de fausses alertes, illustratif).
- **Signe prédit** : Négatif ($\Delta_{1,2} \le -0{,}03$, soit $-0{,}04$ illustratif au tableau), car la prédiction auxiliaire de $\theta$ régularise l'encodeur sur toute la variété paramétrique $\Theta$, réduisant les angles morts exploitables par le générateur au score (iii) plus vite qu'elle n'augmente la moyenne (ii).
- **Issue qui falsifie la prédiction** : La prédiction est falsifiée si la borne inférieure de l'IC à $95\,\%$ de $\hat{\Delta}_{1,2}$ est supérieure à $-0{,}03$ (effet nul ou positif : l'information $\theta$ n'atténue pas la surestimation de la défense par les familles tenues à l'écart).

---

### Bloc 5 — Conclusion

Sous réserve de validation expérimentale (HYPOTHÈSE), l'idée est **bonne pour les deux** (conception et évaluation) au sens strict défini par la question, **à la condition mesurable** que sur les $M=200$ mondes simulés (illustratif) :
1. $(ii)_1 - (ii)_2 \ge 0{,}03$ et $(iii)_1 - (iii)_2 \ge 0{,}03$ (illustratifs) ;
2. $\hat{\Delta}_{1,2} \le -0{,}03$ (illustratif).

Le chiffre publié reste dans tous les cas le score (iii).

**Impact des régimes et de la reparamétrisation** :
- Si ces conditions ne sont remplies qu'en **support commun** et échouent en **support disjoint** (ex. $(iii)_1 - (iii)_2 < 0{,}03$ hors support), le verdict rétrograde à **bonne pour aucune** vis-à-vis de l'objectif d'universalité sur familles inédites (fait 1).
- Si le **test de reparamétrisation** échoue ($|\hat{\Delta}_{\text{reparam}}| > 0{,}02$, illustratif), la défense a appris la syntaxe des coordonnées $\theta$ et non les lois $P_\theta$ : le verdict devient **bonne pour aucune**.

---

### (d) Ancrage matériel

Aucun modèle ouvert n'est requis (vecteurs gaussiens synthétiques en dimension $d=64$, illustratif). Le calcul des $M=200$ mondes simulés pour les 5 bras et 2 régimes représente environ $10^8$ passages avant/arrière d'un perceptron multicouche léger, soit $12$ heures sur un serveur CPU $64$ cœurs (ou $1{,}5$ heure sur $1$ GPU standard), pour un coût électrique et infonuagique estimé à $15\,\text{€}$ (tous chiffres illustratifs).

FIN-DE-CELLULE
# Proposition C — Conception expérimentale et inférence pour l'évaluation à coût croissant sur petit échantillon apparié

*Note de conformité : Conformément au bloc FAITS, aucun fait extérieur n'est joint. Les paramètres de l'énoncé sont traités comme des données du problème (statut RAPPORTÉ). Toute proposition théorique ou paramétrique non démontrée porte le statut HYPOTHÈSE. Tout chiffrage ne découlant pas algébriquement de l'énoncé est marqué « illustratif ».*

---

## (a) Ce que la question suppose sans que ce soit établi (Présupposés et statuts)

L'énoncé de l'arbitre (RAPPORTÉ) structure un problème d'optimisation et de test d'hypothèses sur $N=60$ items (Famille 1 : $N_1 = 36$ stratifiés ; Famille 2 : $N_2 = 24$ dont $12$ positifs et $12$ négatifs). Ce cadre repose sur huit suppositions non établies :

1. **Équilibre des classes dans la Famille 1 (HYPOTHÈSE) :** L'énoncé indique que la Famille 1 ($N_1=36$) est « stratifiée » sans donner le ratio positifs/négatifs. Supposer $N_{1+} = N_{1-} = 18$ simplifie l'exactitude équilibrée ($\mathrm{BA}_1$) en exactitude simple. Si $N_{1+} \neq N_{1-}$, le poids d'un item dans $\mathrm{BA}_1$ dépend de sa classe ($1/(2N_{1+})$ contre $1/(2N_{1-})$), ce qui altère la variance d'échantillonnage et invalide le test de McNemar standard sur la Famille 1.
2. **Agrégation inter-familles (HYPOTHÈSE) :** La règle exigeant $\Delta \geq +0{,}10$ de BA entre deux bras ne précise pas si le critère s'applique à la macro-moyenne $\mathrm{BA}_{\text{macro}} = (\mathrm{BA}_1 + \mathrm{BA}_2)/2$, à la moyenne pondérée par les tailles $(36\,\mathrm{BA}_1 + 24\,\mathrm{BA}_2)/60$, ou par conjonction ($\Delta \mathrm{BA}_1 \geq 0{,}10 \land \Delta \mathrm{BA}_2 \geq 0{,}10$).
3. **Monotonie et séparabilité de la surface de réponse (HYPOTHÈSE) :** Un plan en « escalier » qui détecte un plateau suppose que l'espérance de $\mathrm{BA}$ est une fonction croissante (ou au moins unimodale) du budget $b$, sans interaction négative forte entre les quatre axes (rondes de mise au point $R$, sous-modèles $M$, itérations $I$, longueur maximale $L$). Or, allonger $L$ ou multiplier $I$ peut dégrader la performance par sur-correction ou format de sortie invalide (compté comme erreur selon l'énoncé, RAPPORTÉ).
4. **Exclusion d'effet direct du budget nominal (HYPOTHÈSE) :** Traiter le budget alloué $b$ comme une variable instrumentale (VI) pour la dépense réalisée $s(b)$ suppose la restriction d'exclusion : $b$ n'affecte la qualité de classification *que* par le truchement des dollars effectivement dépensés $s(b)$. Si l'allocateur interne du système change de stratégie algorithmique (ex. : changement de prompt système ou de topologie d'appel) à la simple lecture du paramètre $b$, même à dépense finale $s$ identique, la VI est biaisée.
5. **Indépendance conditionnelle des graines (HYPOTHÈSE) :** Utiliser $K$ graines aléatoires pour réduire la variance suppose que les répliques explorent des trajectoires indépendantes conditionnellement à l'item. Si le générateur de nombres pseudo-aléatoires n'agit que sur une composante mineure (ex. : température basse dans un sous-modèle déterministe), la variance inter-graines observée sous-estimera l'incertitude épistémique du système.
6. **Stationnarité du jeu de test sous réutilisation (HYPOTHÈSE) :** Réutiliser les mêmes $N=60$ items à chaque cran de l'escalier suppose que l'erreur de généralisation ne croît pas trop vite avec le nombre de requêtes adaptatives $T$.
7. **Invariance topologique entre versions du système (HYPOTHÈSE) :** Transposer le cran optimal d'une version $v$ à $v+1$ suppose que la modification du code ou des modèles de base déplace l'ordonnée à l'origine de $\mathrm{BA}$ sans altérer les dérivées partielles $\partial \mathrm{BA} / \partial \$$.
8. **Pleine observabilité des coûts partiels (HYPOTHÈSE) :** Les alternatives multi-fidélité (Hyperband, élimination successive) supposent que l'on peut arrêter une évaluation à mi-budget ou sur un sous-échantillon d'items avec un coût strictement proportionnel. Si les rondes de mise au point avant usage ($\approx 10\text{ USD}$, RAPPORTÉ) constituent un coût fixe non amortissable par item, le sous-échantillonnage d'items ne réduit pas linéairement la dépense.

---

## (b) Développement mathématique, réponses aux points 0 à 5 et expériences décisives ($H_A$ contre $H_B$)

### Point 0 : Le plan à coût croissant (« escalier ») et la confusion $b$ vs $s(b)$

#### Structuration des axes et définition d'un cran
Les quatre paramètres sont : $R$ (rondes de mise au point, coût fixe $\approx 10\text{ USD}$ par ronde, RAPPORTÉ), $M$ (sous-modèles par item), $I$ (itérations d'amélioration, coût $\approx 10\text{ à }22\text{ USD}$ par itération sur le jeu, RAPPORTÉ), et $L$ (longueur maximale des sorties).
* **Ordre des axes :** L'énoncé stipule qu'un item sans réponse valide est compté comme une erreur (RAPPORTÉ). Si $L$ est trop court, la sortie est tronquée et invalide. L'axe $L$ doit être calibré en premier (seuil de non-troncature), suivi des axes intensifs en calcul par item ($I$ et $M$), puis de l'axe d'amortissement global ($R$).
* **Comparaison des définitions d'un cran :**
  1. *Un axe à la fois (One-Factor-at-a-Time, OFAT) :* Isole $\partial \mathrm{BA} / \partial x_j$, mais ignore les synergies (ex. : plus d'itérations $I$ n'aide que si $M \geq 2$ sous-modèles débattent).
  2. *Plan factoriel fractionnaire ($2^{4-1}$ de résolution IV) :* Sur 4 facteurs à 2 niveaux (bas/haut), 8 configurations permettent d'estimer tous les effets principaux sans confusion avec les interactions d'ordre 2 (les interactions d'ordre 2 étant confondues entre elles). Coût : $8 \times \text{coût moyen} \approx 160\text{ USD}$ (illustratif).
  3. *Pas fixe en dollars vs Doublement :* La loi des rendements décroissants sur l'échelle de calcul suggère que $\mathrm{BA}$ est approximativement linéaire en $\log(b)$ (HYPOTHÈSE). Un **doublement du budget incrémental** ($\Delta b_m = 2^m \Delta b_0$) maintient une espérance de gain constante entre deux crans, tandis qu'un pas fixe en dollars épuise la puissance statistique dès que la pente $\partial \mathrm{BA} / \partial \$$ fléchit.

#### Estimation de $\partial \mathrm{BA} / \partial \$$ et traitement de $b$ vs $s(b)$
Puisque la dépense réalisée $s(b)$ diffère du budget alloué $b$ (RAPPORTÉ), trois estimateurs s'opposent :
1. **Intention de traiter (ITT) :** $\widehat{\theta}_{\text{ITT}} = \frac{\widehat{\mathrm{BA}}(b_2) - \widehat{\mathrm{BA}}(b_1)}{b_2 - b_1}$. Pertinent si l'arbitre achète des « plafonds budgétaires » fixes et subit la sous-consommation.
2. **Variable Instrumentale (VI / Wald estimator) :** En prenant $b$ comme instrument de $s$, la valeur marginale du dollar *effectivement dépensé* est :
   $$\widehat{\theta}_{\text{VI}} = \frac{\widehat{\mathrm{BA}}(b_2) - \widehat{\mathrm{BA}}(b_1)}{\bar{s}(b_2) - \bar{s}(b_1)}$$
   Cet estimateur est convergent si $\mathrm{Cov}(b, s) \neq 0$ et si $b$ n'a pas d'effet direct sur $\mathrm{BA}$ hors de $s$ (HYPOTHÈSE). Si $\bar{s}(b_2) - \bar{s}(b_1) \to 0$ (le système refuse de dépenser le budget supplémentaire), l'instrument est faible et la variance de $\widehat{\theta}_{\text{VI}}$ explose.
3. **Dose-réponse sur $s$ (Régression naïve) :** Régresser $\mathrm{BA}$ directement sur la dépense observée $s_{ik}$ par item $i$ et graine $k$. **Piège critique :** Biais de simultanéité (confounding par la difficulté). Le système dépense davantage ($s_{ik}$ élevé) précisément sur les items difficiles où la probabilité d'erreur est haute, ce qui induit une corrélation empirique $\widehat{\mathrm{Cov}}(\mathrm{BA}_{ik}, s_{ik}) < 0$ même si le calcul aide chaque item.

---

### Point 1 : Modèle de variance explicite, seuil d'effet minimal $\delta$ et puissance

#### Formalisation mathématique de la variance à deux niveaux (Items $\times$ Graines)
Soit l'ensemble d'items $\mathcal{I}$ de taille $N=60$, partitionné en $F_1$ ($N_1=36$) et $F_2$ ($N_2=24$). Pour simplifier l'exposition algébrique, supposons $N_{1+}=N_{1-}=18$ (HYPOTHÈSE ; dans le cas contraire, on remplace $1/N_f$ par les poids de classe $w_i = 1/(4N_{f, c(i)})$). Chaque item reçoit le poids $w_i = \frac{1}{2 N_{f(i)}}$ pour une macro-BA équipondérée entre les deux familles ($\sum_{i=1}^{60} w_i = 1$, avec $w_i = 1/72$ si $i \in F_1$ et $w_i = 1/48$ si $i \in F_2$). Si l'on évalue la BA micro-pondérée globale, $w_i = 1/60$ pour tout $i$.

Soit $Y_{ijk} \in \{0, 1\}$ la réussite (1 = correct, 0 = erreur ou invalide) du bras $j \in \{A, B\}$ sur l'item $i$ avec la graine $k \in \{1, \dots, K\}$. La différence observée pour l'item $i$ et la graine $k$ est $D_{ik} = Y_{iBk} - Y_{iAk} \in \{-1, 0, 1\}$.
L'estimateur de l'écart d'exactitude équilibrée moyenné sur $K$ graines est :
$$\widehat{\Delta \mathrm{BA}} = \sum_{i=1}^{N} w_i \bar{D}_{i\cdot} \quad \text{où} \quad \bar{D}_{i\cdot} = \frac{1}{K} \sum_{k=1}^{K} D_{ik}$$

Décomposons $D_{ik}$ selon un modèle à effets aléatoires : $D_{ik} = \mu_i + \epsilon_{ik}$, où $\mu_i = \mathbb{E}[D_{ik} \mid i]$ est le gain vrai sur l'item $i$ (espérance sur l'infinité des graines) et $\epsilon_{ik}$ est le bruit de graine centré de variance $\sigma^2_{G, i} = \mathrm{Var}(D_{ik} \mid i)$.
Par la loi de la variance totale conditionnellement et inconditionnellement à l'échantillon d'items :
1. **Variance conditionnelle au jeu de 60 items fixé (pure variance inter-graines) :**
   $$\mathrm{Var}\left(\widehat{\Delta \mathrm{BA}} \,\middle|\, \mathcal{I}\right) = \frac{1}{K} \sum_{i=1}^{N} w_i^2 \sigma^2_{G, i} = \frac{W_2 \, \bar{\sigma}^2_G}{K}$$
   où $W_2 = \sum_{i=1}^N w_i^2$. Pour la macro-BA ($w_i \in \{1/72, 1/48\}$), $W_2 = 36(1/72)^2 + 24(1/48)^2 = \frac{1}{144} + \frac{1}{96} = \frac{5}{288} \approx 0{,}01736$. Pour la BA globale équipondérée ($w_i = 1/60$), $W_2 = \frac{1}{60} \approx 0{,}01667$. (On utilisera $W_2 = 1/60$ dans les tableaux ci-dessous pour la lisibilité ; le facteur correctif macro est de $+4{,}1\,\%$).
2. **Variance inconditionnelle (échantillonnage des items + graines) :**
   Pour une seule graine ($K=1$), la variance d'échantillonnage dépend de la **part d'items discordants** $p_d = \mathbb{P}(Y_{iB1} \neq Y_{iA1}) = p_{10} + p_{01}$, où $p_{10} = \mathbb{P}(Y_B=1, Y_A=0)$ et $p_{01} = \mathbb{P}(Y_B=0, Y_A=1)$, avec $\Delta = p_{10} - p_{01}$. On a $\mathrm{Var}(D_{i1}) = p_d - \Delta^2$.
   En séparant la variance inter-items $\sigma^2_I = \mathrm{Var}(\mu_i)$ et la variance intra-item (inter-graines) moyenne $\bar{\sigma}^2_G = \mathbb{E}[\sigma^2_{G, i}]$, on a l'identité fondamentale :
   $$\sigma^2_I + \bar{\sigma}^2_G = p_d - \Delta^2$$
   D'où la formule de variance à deux niveaux pour $K$ graines indépendantes par bras (ou appariées) :
   $$\mathrm{Var}\left(\widehat{\Delta \mathrm{BA}}\right) = W_2 \left( \sigma^2_I + \frac{\bar{\sigma}^2_G}{K} \right) = W_2 \left( p_d - \Delta^2 - \bar{\sigma}^2_G \left(1 - \frac{1}{K}\right) \right)$$

#### Formule de puissance et limite asymptotique en $K$
Pour un test unilatéral au seuil $\alpha$ (ou bilatéral à $2\alpha$ avec règle directionnelle scellée), la puissance pour détecter un effet vrai $\Delta = \delta$ est :
$$1 - \beta = \Phi\left( \frac{\delta - z_{1-\alpha} \sqrt{\mathrm{Var}_0(\widehat{\Delta \mathrm{BA}})}}{\sqrt{\mathrm{Var}_\delta(\widehat{\Delta \mathrm{BA}})}} \right) \approx \Phi\left( \frac{\delta}{\sqrt{W_2 \left( \sigma^2_I + \bar{\sigma}^2_G / K \right)}} - z_{1-\alpha} \right)$$
**Conséquence épistémique majeure :** Lorsque $K \to \infty$, la variance ne tend **pas** vers $0$ en généralisation, mais vers le plancher incompressible $W_2 \sigma^2_I$ imposé par la taille finie $N=60$. En revanche, si l'inférence est restreinte au jeu de 60 items fixé (modèle à effets fixes sur $\mathcal{I}$), le terme $\sigma^2_I$ disparaît de l'erreur-type et la variance vaut $W_2 \bar{\sigma}^2_G / K$.

#### Comparaison quantitative pour $\delta \in \{0{,}05 ; 0{,}10 ; 0{,}15\}$
Posons les paramètres illustratifs suivants, ancrés sur les données gratuites : part de discordance totale à 1 graine $p_d = 0{,}20$ (illustratif, soit 12 items sur 60 qui changent de statut entre A et B), variance inter-graines $\bar{\sigma}^2_G = 0{,}06$ (illustratif), donc $\sigma^2_I = p_d - \delta^2 - 0{,}06$, $W_2 = 1/60$, test unilatéral $\alpha = 0{,}05$ ($z_{0{,}95} = 1{,}645$), coût d'une évaluation complète par graine et par bras $C_{\text{run}} = 16\text{ USD}$ (illustratif, point médian de 10–22 USD, RAPPORTÉ), soit $32\text{ USD}$ par paire de graines.

| Seuil $\delta$ | Régime d'inférence | Graines / bras ($K$) | Coût total ($2K \times 16\$$, illustratif) | Écart-type $\mathrm{SE}(\widehat{\Delta\mathrm{BA}})$ (illustratif) | Puissance $1-\beta$ ($\alpha=0{,}05$, illustratif) | Diagnostic opérationnel |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **$\delta = 0{,}05$** | Super-population ($\sigma^2_I > 0$) | $K = 1$ | $32\text{ USD}$ | $0{,}0575$ | $22\,\%$ | **Sous-puissant.** Impossible d'atteindre $80\,\%$ même si $K \to \infty$ (plafond à $26\,\%$ car $\sqrt{\sigma^2_I/60} \approx 0{,}048$). |
| **$\delta = 0{,}05$** | Conditionnel aux 60 items ($\sigma^2_I = 0$) | $K = 3$ | $96\text{ USD}$ | $0{,}0183$ | $86\,\%$ | Viable uniquement si l'on renonce à généraliser hors des 60 items. |
| **$\delta = 0{,}10$** | Super-population ($\sigma^2_I > 0$) | $K = 1$ | $32\text{ USD}$ | $0{,}0563$ | $55\,\%$ | Insuffisant à 1 graine. |
| **$\delta = 0{,}10$** | Super-population ($\sigma^2_I > 0$) | $K = 4$ | $128\text{ USD}$ | $0{,}0492$ | $65\,\%$ | Rendement décroissant des graines : à $K \to \infty$, la puissance plafonne à $70\,\%$ sur 60 items. |
| **$\delta = 0{,}10$** | Conditionnel aux 60 items ($\sigma^2_I = 0$) | $K = 1$ | $32\text{ USD}$ | $0{,}0316$ | $94\,\%$ | Très puissant sur le jeu fixé dès $K=1$ ou $K=2$. Justifie l'exigence $\Delta \geq 0{,}10$ (RAPPORTÉ). |
| **$\delta = 0{,}15$** | Super-population ($\sigma^2_I > 0$) | $K = 1$ | $32\text{ USD}$ | $0{,}0544$ | $87\,\%$ | **Puissant dès $K=1$.** Franchit le bruit d'échantillonnage des 60 items sans réplication coûteuse. |
| **$\delta = 0{,}15$** | Super-population ($\sigma^2_I > 0$) | $K = 2$ | $64\text{ USD}$ | $0{,}0496$ | $92\,\%$ | Sécurise contre une graine aberrante. |

---

### Point 2 : Méthodes d'analyse et usage des deux répliques gratuites

#### Exploitation des deux répliques gratuites (même configuration $A$, graines $k=1, 2$)
Soit $Y_{iA1}$ et $Y_{iA2}$ les résultats des deux répliques gratuites (RAPPORTÉ). La discordance pure inter-graines sur l'item $i$ est $(Y_{iA1} - Y_{iA2})^2 \in \{0, 1\}$.
Puisque $\mathbb{E}[(Y_{iA1} - Y_{iA2})^2 \mid i] = 2 \mathrm{Var}(Y_{iAk} \mid i)$, l'estimateur sans biais de la variance de graine d'un bras simple est :
$$\widehat{\sigma}^2_{\text{graine, bras}} = \frac{1}{2} \sum_{i=1}^N w_i (Y_{iA1} - Y_{iA2})^2$$
C'est exactement la moitié du taux de désaccord pondéré entre les deux graines. Pour la différence entre deux bras indépendants $A$ et $B$ ayant la même instabilité interne, la variance inter-graines de l'écart $D_{ik}$ vaut $\widehat{\bar{\sigma}}^2_G = 2 \widehat{\sigma}^2_{\text{graine, bras}} = \sum_{i=1}^N w_i (Y_{iA1} - Y_{iA2})^2$.
**Utilité immédiate :** Si les deux répliques gratuites diffèrent sur $6$ items sur $60$ ($10\,\%$), alors $\widehat{\bar{\sigma}}^2_G \approx 0{,}10$ (illustratif), et l'écart-type incompressible dû aux graines pour $K=1$ est $\sqrt{0{,}10 / 60} \approx 0{,}041$ point de BA.

#### Comparaison critique des cinq méthodes d'analyse
1. **Test exact de McNemar :**
   * *Mécanisme :* Pour $K=1$, compte les paires discordantes $n_{10}$ (B réussit, A échoue) et $n_{01}$ (B échoue, A réussit). Sous $H_0$, $n_{10} \mid (n_{10}+n_{01}) \sim \mathrm{Binomiale}(n_d, 0{,}5)$.
   * *Avantages :* Exact en petit échantillon, aucune hypothèse asymptotique.
   * *Pièges :* (i) **Inapplicable directement à la macro-BA** car un item de la Famille 2 ($N_2=24$) pèse $1{,}5$ fois plus qu'un item de la Famille 1 ($N_1=36$) ; il faut un test de McNemar stratifié (Mantel-Haenszel) ou un test de permutation sur les poids $w_i$. (ii) Ignore la structure multi-graines si $K > 1$ ($\bar{D}_{i\cdot}$ n'est plus binaire).
2. **Rééchantillonnage apparié à deux niveaux (Hierarchical Bootstrap / Permutation) :**
   * *Mécanisme :* Niveau 1 : tirer $N_1=36$ et $N_2=24$ items avec remise dans chaque strate. Niveau 2 : pour chaque item tiré, tirer $K$ graines avec remise. Pour un test d'hypothèse nul, la **permutation signée par item** (inverser les étiquettes A et B avec probabilité $0{,}5$ pour l'ensemble du bloc $\{k=1\dots K\}$ de chaque item $i$) est exacte.
   * *Avantages :* Respecte exactement les poids $w_i$ de la BA et la distribution discrète de $\bar{D}_{i\cdot}$.
   * *Pièges :* Si $n_d$ (nombre d'items où $\bar{D}_{i\cdot} \neq 0$) est très faible (ex. $n_d \leq 5$), la distribution de permutation a au plus $2^5 = 32$ atomes : il est mathématiquement impossible d'obtenir $p < 0{,}031$.
3. **Modèle linéaire généralisé à effets mixtes (GLMM logit, items $\times$ graines) :**
   * *Mécanisme :* $\mathrm{logit}\,\mathbb{P}(Y_{ijk}=1) = \beta_0 + \beta_1 \mathbb{I}(j=B) + u_i + v_k$, avec $u_i \sim \mathcal{N}(0, \tau^2_I)$ et $v_k \sim \mathcal{N}(0, \tau^2_G)$.
   * *Avantages :* Sépare proprement les composantes de variance et gère les plans déséquilibrés (ex. : $K_A = 2$ graines gratuites pour A, $K_B = 1$ graine pour B).
   * *Pièges :* (i) **Séparation quasi-complète :** sur 60 items, beaucoup ont $Y_{ijk}=1$ partout ou $0$ partout, faisant diverger $\widehat{\tau}^2_I$ ou biaisant l'approximation de Laplace. (ii) Estime un odds-ratio conditionnel ($\beta_1$) et non l'écart marginal $\Delta \mathrm{BA}$ demandé par l'arbitre. Un modèle linéaire mixte sur les scores pondérés (LMM sur $w_i Y_{ijk}$) est préférable pour cibler $\Delta \mathrm{BA}$ directement, malgré l'hétéroscédasticité binaire.
4. **Approche bayésienne avec fonction de perte :**
   * *Mécanisme :* Modèle Dirichlet-Multinomial sur les probabilités jointes $(p_{00}, p_{10}, p_{01}, p_{11})$ dans chaque famille. On définit la fonction d'utilité nette en dollars : $U(j) = \lambda \, \mathrm{BA}_j - \mathbb{E}[s(b_j)]$, où $\lambda$ est la disposition à payer par point de BA (ex. $\lambda = 150\text{ USD}$ pour $+0{,}10$ BA, illustratif). On choisit $B$ si $\mathbb{E}_{\text{post}}[U(B) - U(A)] > 0$.
   * *Avantages :* Intègre nativement le coût réel $s(b)$ et la règle « à égalité, le moins cher l'emporte » (qui correspond à $\Delta \mathrm{BA} = 0 \implies U(B) - U(A) = -(s_B - s_A) < 0$).
   * *Pièges :* Sur $N=60$, un prior de Dirichlet $\mathrm{Dir}(\alpha_{00}, \alpha_{10}, \alpha_{01}, \alpha_{11})$ même faiblement informatif ($\alpha = 1$) ajoute 4 pseudo-items par famille (8 au total, soit $13\,\%$ de l'échantillon), ce qui tire fortement $\widehat{\Delta\mathrm{BA}}$ vers $0$ et favorise mécaniquement le bras le moins cher.
5. **Test séquentiel avec arrêt précoce (Alpha-spending / O'Brien-Fleming ou Pocock) :**
   * *Mécanisme :* Évaluer par blocs d'items (ex. : tranche 1 de 30 items stratifiés, puis tranche 2 de 30 items) ou graine par graine, avec une fonction de dépense d'erreur $\alpha(t) = 2 - 2\Phi(z_{1-\alpha/2}/\sqrt{t})$ (O'Brien-Fleming, $t \in \{0{,}5 ; 1\}$).
   * *Avantages :* Économise $50\,\%$ du budget d'inférence si une configuration s'effondre dès les 30 premiers items (arrêt pour futilité : $\widehat{\Delta\mathrm{BA}}_{t=0{,}5} < 0$).
   * *Pièges :* Si le coût de mise au point avant usage ($R \times 10\text{ USD}$, RAPPORTÉ) domine le coût par item, arrêter à 30 items n'économise presque rien tout en payant la pénalité de seuil final ($z_{\text{final}} > z_{1-\alpha}$).

---

### Point 3 : Règle de décision gelée, pièges méthodologiques et réutilisation des 60 items

#### Règle de décision scellée (Monter, Rester, Zone grise)
Pour passer du cran $m$ (référence actuelle $A$, dépense moyenne $\bar{s}_A$) au cran $m+1$ (candidat $B$, dépense $\bar{s}_B$), avec $K_0 = 1$ graine initiale pour $B$ (et les $K_A=2$ répliques pour $A$) :
1. **Garde-fou d'audit (Anti-triche / bogue, RAPPORTÉ) :** Si $|\widehat{\Delta\mathrm{BA}}| \geq 0{,}35$ (illustratif) ou si le taux de discordance $p_d < 0{,}02$ avec $\Delta \neq 0$, **GELER ET AUDITER** (fuite de données, panne d'API ou bogue de parsing).
2. **Coût marginal effectif :** Calculer $\Delta \bar{s} = \bar{s}_B - \bar{s}_A$. Si $\Delta \bar{s} \leq 0$ et $\widehat{\Delta\mathrm{BA}} \geq 0$, $B$ domine $A$ $\implies$ **MONTER**.
3. **Règle de franchissement à $K=1$ :**
   * **MONTER** si $\widehat{\Delta\mathrm{BA}} \geq +0{,}10$ (seuil d'effet minimal exigé, RAPPORTÉ) **ET** la borne inférieure de l'IC à $90\,\%$ par permutation stratifiée vérifie $\mathrm{IC}_{\inf} > +0{,}02$ (illustratif) **ET** le coût par point de BA gagné $\frac{\Delta \bar{s}}{100 \times \widehat{\Delta\mathrm{BA}}} \leq c_{\max}$ (ex. $c_{\max} = 2{,}50\text{ USD}$ par point de BA, illustratif).
   * **RESTER (Arrêt de l'escalier)** si $\widehat{\Delta\mathrm{BA}} \leq +0{,}03$ (illustratif, futilité) : le principe de parcimonie (« à égalité, le moins cher l'emporte », RAPPORTÉ) s'applique.
   * **ZONE GRISE :** Si $+0{,}03 < \widehat{\Delta\mathrm{BA}} < +0{,}10$ ou si $\widehat{\Delta\mathrm{BA}} \geq +0{,}10$ mais $\mathrm{IC}_{\inf} \leq +0{,}02$ à cause d'une variance élevée, tirer **exactement une graine supplémentaire** ($K_B = 2$, coût $\approx 16\text{ USD}$, illustratif) et appliquer la règle binaire finale : MONTER si et seulement si $\widehat{\Delta\mathrm{BA}}_{K=2} \geq +0{,}10$ et $p_{\text{perm}} < 0{,}05$, sinon RESTER.

#### Traitement des 7 pièges identifiés dans l'énoncé
1. **Multiplicité sur $M$ crans :** Tester $M$ crans en parallèle sans correction gonfle le risque de faux positif à $1 - (1-\alpha)^M$. **Parade :** Utiliser une **procédure à séquence fixe (Fixed-Sequence Gatekeeping)** le long de l'escalier. On teste le cran $m+1$ contre $m$ au plein niveau $\alpha = 0{,}05$ *uniquement* si tous les crans précédents $1 \dots m$ ont été franchis. Dès qu'un cran échoue, l'escalier s'arrête : le taux d'erreur familial (FWER) est mathématiquement contrôlé à $\alpha$ sans aucune perte de puissance (pas de division de $\alpha$ par $M$).
2. **Régression vers la moyenne (Malédiction du vainqueur) :** Si l'on choisit le meilleur parmi plusieurs axes et qu'il devient la nouvelle référence $A$ en conservant son score chanceux, le cran suivant semblera stagner ($\widehat{\Delta\mathrm{BA}}$ biaisé négativement). **Parade :** Utiliser la $2^{\text{e}}$ réplique (graine fraîche) du vainqueur comme ligne de base pour l'étape suivante, jamais la graine qui a servi à le sélectionner.
3. **Effet plafond et items trivialement faciles :** La référence triviale sur la Famille 1 est déjà à $0{,}69$ (RAPPORTÉ). Si $69\,\%$ des items ($25/36$) sont résolus par la forme superficielle du texte et ne changent jamais de statut ($Y_{iA}=Y_{iB}=1$), tout le signal repose sur les $11$ items restants de $F_1$ et les $24$ de $F_2$. Un gain global de $+0{,}10$ exige alors un gain de $+0{,}23$ sur le sous-ensemble non trivial. **Parade :** Stratifier l'analyse en isolant le sous-ensemble d'items où le classifieur trivial échoue.
4. **Petit échantillon ($N=60$) et granularité :** Un seul item de $F_2$ changeant de statut modifie $\mathrm{BA}_2$ de $1/24 \approx 0{,}0417$ et la macro-BA de $0{,}0208$. Le seuil $\Delta \geq 0{,}10$ équivaut à seulement $5$ items nets sur $60$.
5. **Dépendance entre familles :** Si $F_1$ et $F_2$ partagent le même domaine ou la même invite système, une modification de configuration qui déplace le seuil de décision interne (biais positif/négatif) affecte simultanément $\mathrm{BA}_1$ et $\mathrm{BA}_2$. Les traiter comme deux études indépendantes est invalide.
6. **Graine aberrante :** Un appel API qui échoue sur un lot d'items pour une graine donnée génère des réponses invalides (comptées comme erreurs, RAPPORTÉ), créant une queue lourde. **Parade :** Vérifier la concordance inter-graines par bloc d'items avant d'agréger.
7. **Coût en puissance de la réutilisation du jeu de 60 items :**
   * *Option A (Scinder $60 \to 40$ exploration $+ 20$ réserve intouchée) :* Sur $N_{\text{confirm}} = 20$ items (12 de $F_1$, 8 de $F_2$), le poids quadratique monte à $W_2 = 3/60 = 0{,}05$. Pour $\delta = 0{,}10$ et $p_d = 0{,}20$, l'écart-type passe de $0{,}056$ à $\mathbf{0{,}097}$. La puissance du test de confirmation tombe à **$26\,\%$** (illustratif). Scinder un jeu de 60 items détruit la puissance.
   * *Option B (Réutiliser les 60 items avec budget de requêtes borné — style Thresholdout / Adaptive Data Analysis) :* Tant que les décisions à chaque cran sont prises via un seuil grossier ($\delta = 0{,}10$) et que le nombre total de comparaisons $T$ reste faible ($T \leq 6$ crans), la théorie de la généralisation adaptative sur décisions binaires montre que le sur-ajustement est borné par $\mathcal{O}(\sqrt{T \log(2) / N})$. C'est la voie statistiquement supérieure pour $N=60$.

---

### Point 4 : Alternatives algorithmiques et ce qui les départage ici

| Approche | Mécanisme | Ce qui la départage dans le cadre des 60 items (Avantages / Disqualifications) |
| :--- | :--- | :--- |
| **Plan en escalier à séquence fixe (Référence)** | Monte cran par cran avec règle d'arrêt FWER contrôlée. | **Avantage :** Aucun coût gaspillé sur les hauts budgets si le plateau est atteint tôt ; gère les coûts fixes de mise au point $R$. **Limite :** Sensible à l'ordre choisi des axes. |
| **Élimination successive (Successive Halving / Hyperband)** | Évalue $C$ configurations sur une fraction des ressources (ex. $N_0 = 15$ items ou $I=1$ itération), élimine la moitié inférieure, double la ressource. | **Disqualification partielle :** (1) Sur $N_0=15$ items (9 de $F_1$, 6 de $F_2$), l'écart-type de $\widehat{\Delta\mathrm{BA}}$ dépasse $0{,}11$ : on élimine la meilleure configuration par pur bruit d'échantillonnage. (2) Si la ressource réduite est le nombre de rondes de mise au point $R$, la hiérarchie des configurations à $R=0$ peut être inversée par rapport à $R=2$ (mauvaise corrélation inter-fidélité). |
| **Bandits sous contrainte de budget (Knapsack Bandits / Best Arm Identification)** | Alloue séquentiellement des paires (item, graine) aux bras selon une borne supérieure de confiance ratio gain/coût (UCB-BV). | **Avantage :** Optimal si le coût est strictement proportionnel au nombre d'items évalués ($R$ déjà payé ou fixe). En échantillonnant le même item $i$ pour les bras actifs (appariement préservé), il concentre les dollars sur les 2 meilleures configurations. |
| **Optimisation bayésienne multi-fidélité (MF-BO / BOHB)** | Construit un processus gaussien (GP) sur l'espace $(R, M, I, L)$ et sélectionne le point maximisant le gain d'information par dollar. | **Disqualification :** Ajuster un GP en dimension 4 nécessite une phase d'initialisation (plan latin hypercube) d'au moins $2d + 1 = 9$ configurations complètes, soit $9 \times 16\$ = 144\text{ USD}$ (illustratif) avant même la première étape d'optimisation. Sur-dimensionné pour un budget total serré. |

---

### Expériences décisives en duel ($H_A$ contre $H_B$) — Règle B4

Pour trancher les suppositions non établies de la section (a) avant ou pendant le déploiement de l'escalier, voici trois expériences à inférence forte :

#### Expérience 1 : Décomposition de la variance (Bruit de graine contre Bruit d'items)
* **Hypothèse $H_A$ (Dominance de l'instabilité générative) :** La variance inter-graines représente la majorité de l'incertitude sur un écart de configuration ($\bar{\sigma}^2_G / (p_d - \Delta^2) \geq 0{,}50$). Multiplier les graines $K$ par bras est le levier principal pour gagner en puissance.
* **Hypothèse $H_B$ (Dominance de l'échantillonnage des 60 items) :** Les réponses du système sont quasi-déterministes par item ($\bar{\sigma}^2_G / (p_d - \Delta^2) < 0{,}50$) ; la variance provient de l'hétérogénéité des 60 items ($\sigma^2_I$). Payer pour $K > 1$ graine gaspille le budget sans augmenter la puissance en généralisation.
* **Protocole et Métrique :** Utiliser les deux répliques gratuites du bras de base $A$ ($Y_{iA1}, Y_{iA2}$) et la première évaluation du cran suivant $B$ ($Y_{iB1}$). Calculer l'estimateur $\widehat{\bar{\sigma}}^2_G = \sum_{i=1}^{60} w_i (Y_{iA1} - Y_{iA2})^2$ et la discordance inter-bras $\widehat{p}_d = \sum_{i=1}^{60} w_i (Y_{iB1} - Y_{iA1})^2$. La métrique est le ratio d'instabilité $\rho_G = \widehat{\bar{\sigma}}^2_G / (\widehat{p}_d - \widehat{\Delta\mathrm{BA}}^2)$.
* **Seuil de décision :** $\rho_G = 0{,}50$.
* **Contrôle négatif :** Appliquer le calcul à deux exécutions à température $0$ (ou avec cache activé) : on doit observer $\widehat{\bar{\sigma}}^2_G = 0$ (hors pannes réseau).
* **Issue falsificatrice :** Si $\rho_G < 0{,}50$ (ex. $\widehat{\bar{\sigma}}^2_G \leq 0{,}04$ pour $\widehat{p}_d = 0{,}20$, illustratif), **$H_A$ est falsifiée** $\implies$ fixer $K=1$ pour tout l'escalier (sauf zone grise). Si $\rho_G \geq 0{,}50$, **$H_B$ est falsifiée** $\implies$ imposer $K \geq 2$ graines par bras.

#### Expérience 2 : Validité de la Variable Instrumentale $b$ (Exclusion d'effet direct contre Biais d'allocation)
* **Hypothèse $H_A$ (Validité de la restriction d'exclusion) :** Le budget alloué $b$ n'influence $\mathrm{BA}$ qu'à travers la dépense effective $s(b)$ ($\mathbb{E}[\mathrm{BA} \mid b, s] = \mathbb{E}[\mathrm{BA} \mid s]$). L'estimateur par Variable Instrumentale $\widehat{\theta}_{\text{VI}}$ mesure sans biais la valeur marginale du dollar dépensé.
* **Hypothèse $H_B$ (Violation de l'exclusion par changement de régime interne) :** La consigne de budget $b$ modifie la politique interne du programme (ex. : choix d'un sous-modèle différent ou allocation d'attention dès l'initialisation) indépendamment de la dépense finale $s$.
* **Protocole et Métrique :** Comparer un bras à budget bas $b_{\text{bas}}$ (où le système sature son plafond : $s(b_{\text{bas}}) \approx b_{\text{bas}}$) et un bras à budget haut $b_{\text{haut}}$ mais bridé ex-post (ou sur le sous-ensemble d'items appariés où l'allocateur du bras $b_{\text{haut}}$ a spontanément arrêté ses itérations au niveau de dépense $s \approx b_{\text{bas}}$). Métrique : écart d'exactitude équilibrée $\Delta \mathrm{BA}_{\text{iso-}s}$ à dépense réalisée égale.
* **Seuil de décision :** $|\Delta \mathrm{BA}_{\text{iso-}s}| > 0{,}06$ (illustratif, correspondant à plus de 3 items de différence nette à dépense égale).
* **Contrôle négatif :** Vérifier sur les journaux d'exécution (logs) que le nombre de jetons consommés est identique à $\pm 5\,\%$ près entre les deux groupes d'items comparés.
* **Issue falsificatrice :** Si $|\Delta \mathrm{BA}_{\text{iso-}s}| > 0{,}06$, **$H_A$ est falsifiée** $\implies$ abandonner la Variable Instrumentale et piloter l'escalier exclusivement en Intention de Traiter (ITT) sur le paramètre de commande $b$. Sinon, **$H_B$ est falsifiée** et l'estimateur VI est retenu.

#### Expérience 3 : Additivité des axes (Plan OFAT en escalier contre Interaction synergique)
* **Hypothèse $H_A$ (Additivité / Sous-modularité) :** Les gains des axes $M$ (sous-modèles) et $I$ (itérations) sont additifs ou sous-modulaires ($\Delta_{M+I} \leq \Delta_M + \Delta_I$). Un plan séquentiel un axe à la fois (OFAT) trouve l'optimum sans manquer de pic caché.
* **Hypothèse $H_B$ (Synergie super-additive) :** Augmenter les itérations $I$ sans augmenter le nombre de sous-modèles $M$ produit un gain nul ($\Delta_I \approx 0$), et réciproquement ($\Delta_M \approx 0$), mais leur activation conjointe débloque la performance ($\Delta_{M+I} - (\Delta_M + \Delta_I) \geq +0{,}10$). L'escalier OFAT s'arrête prématurément par futilité.
* **Protocole et Métrique :** Exécuter un mini-plan factoriel $2 \times 2$ sur le premier cran des axes $(M, I)$ : $(M_0, I_0)$, $(M_1, I_0)$, $(M_0, I_1)$, $(M_1, I_1)$. La métrique est le terme d'interaction $\widehat{\gamma}_{MI} = \widehat{\mathrm{BA}}(M_1, I_1) - \widehat{\mathrm{BA}}(M_1, I_0) - \widehat{\mathrm{BA}}(M_0, I_1) + \widehat{\mathrm{BA}}(M_0, I_0)$.
* **Seuil de décision :** $\widehat{\gamma}_{MI} \geq +0{,}10$ avec test de permutation sur le contraste d'interaction $D^{\text{int}}_i = Y_i(M_1,I_1) - Y_i(M_1,I_0) - Y_i(M_0,I_1) + Y_i(M_0,I_0)$ au seuil $p < 0{,}10$ (illustratif).
* **Contrôle négatif :** Appliquer le contraste $2 \times 2$ à quatre répliques de la configuration $(M_0, I_0)$ (espérance théorique de $\widehat{\gamma} = 0$).
* **Issue falsificatrice :** Si $\widehat{\gamma}_{MI} \geq +0{,}10$, **$H_A$ est falsifiée** $\implies$ définir chaque cran de l'escalier comme une montée diagonale conjointe $(M \uparrow, I \uparrow)$. Si $\widehat{\gamma}_{MI} < +0{,}10$, **$H_B$ est falsifiée** $\implies$ l'escalier OFAT axe par axe est validé.

---

## (c) Étalonnage des instruments nommés dans la question

Pour chaque instrument méthodologique requis par l'arbitre, voici la mesure minimale de bon fonctionnement, évaluée sur des cas synthétiques ou semi-synthétiques construits à partir des deux répliques gratuites (cas honnêtes appariés où l'effet vrai est connu par construction) :

| Instrument nommé | Cas honnêtes appariés pour le test d'étalonnage | Vérification mécanique naïve à battre (Baseline) | Mesure minimale : Taux de détection (Vrais Positifs, TDR) et Fausses Alertes (FPR) |
| :--- | :--- | :--- | :--- |
| **1. Détecteur de plateau à faible coût** (Règle d'arrêt sur $\partial \mathrm{BA}/\partial \$$) | Séquences synthétiques de 4 crans générées à partir de la matrice de covariance empirique des 60 items : (i) Sous $H_0$ (plateau immédiat) : permutation aléatoire des deux répliques gratuites aux crans 1, 2, 3. (ii) Sous $H_1$ (vrai gain) : injection de $+6$ items corrigés ($+0{,}10$ BA) au cran 1, puis plateau au cran 2. | **Règle naïve d'arrêt au premier recul empirique :** S'arrêter dès que $\widehat{\Delta\mathrm{BA}}_{m, m+1} \leq 0$ sans bande d'indifférence ni gestion de la zone grise. | **FPR (arrêt prématuré au cran 1 sous $H_1$) :** $\leq 15\,\%$ (contre $\approx 30\,\%$ pour la règle naïve sous bruit de graine, illustratif). **TDR (détection du plateau dès le cran 2 sous $H_1$ ou cran 1 sous $H_0$) :** $\geq 85\,\%$ d'arrêt avant de dépenser le budget du cran suivant. |
| **2. Estimateur de variance inter-graines** ($\widehat{\bar{\sigma}}^2_G$ sur 2 répliques gratuites) | Paires $(Y_{iA1}, Y_{iA2})$ issues des données gratuites, comparées par bootstrap paramétrique à une vérité terrain simulée de Bernoulli par item $p_i \in [0{,}1 ; 0{,}9]$. | **Estimateur binomial naïf non apparié :** $\widehat{\mathrm{BA}}_A(1 - \widehat{\mathrm{BA}}_A) / 60$, qui confond la variance inter-items $\sigma^2_I$ et la variance inter-graines $\bar{\sigma}^2_G$ (surestimation massive si le système est déterministe). | **FPR (conclure à tort que $\bar{\sigma}^2_G > 0{,}05$ quand le système est déterministe $\bar{\sigma}^2_G = 0$) :** $0\,\%$ (exactitude algébrique : si $Y_{iA1}=Y_{iA2}$ partout, $\widehat{\bar{\sigma}}^2_G = 0$). **TDR (détecter une instabilité $\bar{\sigma}^2_G \geq 0{,}08$) :** $\geq 80\,\%$ de couverture de l'IC bootstrap à $90\,\%$ (illustratif). |
| **3. Test apparié à deux niveaux** (Permutation stratifiée / McNemar pondéré) | Paires de vecteurs de taille $60$ ($36$ en $F_1$, $24$ en $F_2$) avec corrélation inter-bras $\mathrm{Corr}(Y_A, Y_B) = 0{,}60$ (illustratif) : (i) Cas nul : les deux répliques gratuites testées l'une contre l'autre ($\Delta = 0$). (ii) Cas alternatif : basculement dirigé de 4 items de $F_1$ et 3 items de $F_2$ ($\Delta \mathrm{BA} = +0{,}118$). | **Test $Z$ de différence de deux proportions indépendantes** (non apparié, ignorant la stratification par famille). | **FPR (sur paires nulles issues de permutations des répliques gratuites) :** $\leq 0{,}05$ strict (garanti par construction du test de permutation). **TDR (puissance sur $\Delta \mathrm{BA} = +0{,}118$ avec $p_d = 0{,}20$) :** $\geq 80\,\%$ (contre $\approx 38\,\%$ pour le test non apparié qui souffre de la variance totale $\approx 0{,}50 \times 0{,}50$, illustratif). |
| **4. Auditeur de résultat « trop propre »** (Garde-fou d'intégrité, RAPPORTÉ) | Comparaison d'un bras honnête (bruit de graine $\bar{\sigma}^2_G \approx 0{,}06$, discordances bidirectionnelles $n_{10} > 0$ et $n_{01} > 0$) contre un bras corrompu par fuite d'étiquettes ou bogue de cache ($n_{01} = 0$ strict avec $n_{10} \geq 15$, ou $\widehat{\mathrm{BA}} > 0{,}95$). | **Vérification mécanique simple :** Seuil uniquement sur le score global $\widehat{\mathrm{BA}} = 1{,}00$. | **TDR (détection d'une fuite partielle sur $25\,\%$ des items ou d'une copie exacte de graine) :** $\geq 95\,\%$ via le test binomial sur l'absence totale de régressions ($n_{01}=0$ sachant $n_d \geq 12$ et $\bar{\sigma}^2_G > 0{,}05$, probabilité honnête $< 0{,}01$, illustratif). **FPR sur bras honnête :** $\leq 2\,\%$ (illustratif). |

---

## (d) Ancrage matériel : modèles ouverts, calcul nécessaire et budget estimé

Pour exécuter le protocole complet (expériences décisives + escalier à séquence fixe + couche d'analyse statistique), l'infrastructure se divise en deux postes :

### 1. Couche d'inférence du système de classification (Appel des modèles de langue)
* **Modèles ouverts d'ancrage (illustratif) :** Pour auditer la reproductibilité des graines sans dépendre d'API propriétaires opaques dont les poids ou le routage changent silencieusement, le système peut s'ancrer sur des modèles à poids ouverts servis localement via `vLLM` (ex. : famille `Llama-3.1-8B-Instruct` / `70B-Instruct`, `Mistral-Small-24B-Instruct`, ou `Qwen2.5-32B-Instruct`, illustratif) sur nœuds GPU (ex. 2 à 4 $\times$ NVIDIA A100-80GB ou H100, illustratif).
* **Coût unitaire des appels (RAPPORTÉ et illustratif) :**
  * Ronde de mise au point avant usage ($R$) : $\approx 10\text{ USD}$ par ronde ajoutée (RAPPORTÉ).
  * Évaluation d'un bras sur les $N=60$ items : $10\text{ à }22\text{ USD}$ par itération (RAPPORTÉ), soit un coût moyen de $16\text{ USD}$ par graine au cran de base (illustratif).
* **Budget total de l'expérience en escalier (illustratif) :**
  * *Cran 0 (Référence $A$) :* $0\text{ USD}$ (les 2 répliques sont fournies gratuitement au départ, RAPPORTÉ). Elles permettent d'exécuter immédiatement le contrôle négatif et l'estimation de $\widehat{\bar{\sigma}}^2_G$.
  * *Phase de criblage initial des axes (Plan fractionnaire ou mini-factoriel $2 \times 2$ de l'Expérience 3 à $K=1$ graine) :* 3 nouvelles configurations $\times 16\text{ USD} + 1$ ronde de mise au point ($10\text{ USD}$) $= 58\text{ USD}$ (illustratif).
  * *Montée de l'escalier (2 crans supplémentaires sur la trajectoire gagnante, avec $50\,\%$ de probabilité de déclencher une $2^{\text{e}}$ graine en zone grise) :* $2 \times 1{,}5\text{ graines} \times 22\text{ USD} = 66\text{ USD}$ (illustratif).
  * **Total du poste d'inférence LLM :** **$124\text{ USD}$** (illustratif, dans une fourchette de $80\text{ à }180\text{ USD}$ selon le nombre de crans franchis avant l'arrêt par futilité).

### 2. Couche d'analyse statistique et de rééchantillonnage (CPU)
* **Algorithmes exécutés :** Calcul exact des $2^{n_d}$ permutations signées par item (si $n_d \leq 20$, soit $\leq 1\,048\,576$ opérations vectorisées) ou $B = 100\,000$ tirages Monte-Carlo stratifiés ($F_1, F_2$) à deux niveaux (items $\times$ graines), estimation VI par bootstrap, et vérification des seuils d'audit.
* **Matériel et temps de calcul :** 1 processeur CPU standard (ex. 8 cœurs x86_64, 16 Go de RAM, pile logicielle ouverte Python `numpy`/`scipy`/`statsmodels` ou R `coin`/`lme4`, illustratif). Temps d'exécution pour $100\,000$ permutations sur une matrice $60 \times 2$ : $< 1{,}5\text{ seconde}$ (illustratif). Coût matériel marginal : $< 0{,}01\text{ USD}$ (illustratif).

---

## Point 5 : Références bibliographiques

Conformément à la règle d'intégrité n° 3, seules les références dont les auteurs, l'année et le titre sont établis sans ambiguïté sont citées ci-dessous ; aucun identifiant arXiv n'est donné de mémoire :

1. **Comparaison de classifieurs sur petits échantillons et test de McNemar :**
   * Dietterich, T. G. (1998). *Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithms*. Neural Computation, 10(7), 1895–1923.
2. **Test exact des paires discordantes :**
   * McNemar, Q. (1947). *Note on the sampling error of the difference between correlated proportions or percentages*. Psychometrika, 12(2), 153–157.
3. **Comparaison de multiples classifieurs et contrôle de la multiplicité :**
   * Demšar, J. (2006). *Statistical Comparisons of Classifiers over Multiple Data Sets*. Journal of Machine Learning Research, 7, 1–30.
4. **Modélisation de la variance due aux graines aléatoires et à l'échantillonnage des items dans les modèles de langue :**
   * Référence sur la quantification de l'incertitude et la puissance statistique dans les évaluations de grands modèles de langue (auteurs et titre exacts : *référence à vérifier* — travaux de Card et al., 2020, sur la puissance dans le traitement automatique des langues : Card, D., Henderson, P., Khandelwal, U., Jia, R., Mahowald, K., & Jurafsky, D., 2020, *With Little Power Comes Great Responsibility*, EMNLP, *à vérifier*).
   * Référence sur l'addition de la variance des graines aux barres d'erreur d'évaluation des LLM (auteurs et année : *référence à vérifier*).
5. **Réutilisation adaptative d'un jeu de validation tenu à l'écart (Thresholdout) :**
   * Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., & Roth, A. (2015). *The Reusable Holdout: Preserving Validity in Adaptive Data Analysis*. Science, 349(6248), 636–638.
6. **Élimination successive et allocation multi-fidélité (Hyperband) :**
   * Li, L., Jamieson, K., DeSalvo, G., Rostamizadeh, A., & Talwalkar, A. (2018). *Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization*. Journal of Machine Learning Research, 18, 1–52 (année exacte de parution JMLR 2017/2018 : *référence à vérifier*).
7. **Tests séquentiels par groupes (dépense d'erreur $\alpha$) :**
   * Jennison, C., & Turnbull, B. W. (1999). *Group Sequential Methods with Applications to Clinical Trials*. Chapman & Hall/CRC (année 1999/2000 : *référence à vérifier*).

FIN-DE-CELLULE
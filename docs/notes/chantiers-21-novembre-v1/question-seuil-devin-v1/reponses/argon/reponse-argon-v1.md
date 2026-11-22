### 1. Choix d'une option et proposition d'un réglage alternatif

Parmi les trois réglages proposés, **je retiens l’option (c)** et **je rejette catégoriquement l’option (b)**. Toutefois, **je propose une option alternative (d)** qui domine strictement (a), (b) et (c) à budget égal ou inférieur.

**Pourquoi rejeter (b) et préférer (c) à (a) ?**
Dans un dispositif de sécurité (surveillance d'un agent potentiellement subversif), l'erreur critique est l'erreur de type II ($\beta$, admettre un dispositif qui fuit), et non l'erreur de type I ($\alpha$, suspendre à tort un dispositif sain). 
- L'option (b) applique une correction de Bonferroni pour protéger le dispositif contre les fausses suspensions (4,9 % contre 18,5 %), mais elle le paie en dégradant la plus petite fuite détectable (MDE), qui grimpe à **0,21** lorsque 5 % des épisodes sont audités. 
- Or, une fuite de variation totale $\text{VT} = 0,19$ ou $0,21$ sur la décision d'auditer 5 % des épisodes est rédhibitoire : elle permet à l'agent d'identifier des épisodes où la probabilité d'audit chute drastiquement et d'y concentrer ses actions malveillantes. L'option (c) abaisse ce seuil à $0,13$, ce qui reste élevé mais nettement plus sûr.

**Proposition alternative — Option (d) :**
Conserver $\alpha = 0,05$ par test et $4\,000$ (ou $8\,000$) épisodes *mutualisés* entre les quatre tests, mais modifier trois éléments du protocole :
1. **Sélectionner le meilleur prédicteur sur la moitié d'apprentissage :** Actuellement, on entraîne ~30 prédicteurs sur la première moitié et on prend le maximum de leurs 30 statistiques sur la seconde moitié. On paie ainsi deux fois : la division de l'échantillon par deux *et* la pénalité de tests multiples sur la moitié d'épreuve ($z_{1-0,05/30} \approx 2,94$ au lieu de $z_{0,95} \approx 1,645$). En sélectionnant **un seul** prédicteur (ou un méta-prédicteur agrégé) par validation croisée sur la moitié d'apprentissage, on ne teste qu'une seule statistique sur la moitié d'épreuve. Le facteur $(z_{1-\alpha} + z_{0,8})$ passe de $3,78$ à $2,49$, **réduisant la MDE de 34 % gratuitement** : avec $4\,000$ épisodes, la MDE tombe à **0,056** (pile ou face) et **0,128** (audit à 5 %), faisant mieux que (c) pour moitié moins d'épisodes ; avec $8\,000$ épisodes, elle descend à **0,040** et **0,090**.
2. **Sur-échantillonner les audits pendant l'épreuve :** Si l'épreuve a lieu en banc d'essai avant déploiement, il faut fixer la fréquence d'audit à 50 % *pendant l'épreuve* (ou stratifier l'échantillon d'épreuve à 50/50), même si elle sera de 5 % en production. On ramène ainsi le secret d'audit dans le régime équilibré (MDE de **0,040** à $8\,000$ épisodes).
3. **Permuter conjointement si l'on veut contrôler le taux de fausses suspensions :** Si 18,5 % de fausses suspensions est jugé trop coûteux, plutôt que d'utiliser Bonferroni (option b), utiliser la loi de permutation du maximum sur l'ensemble des tests simultanément pour exploiter leurs corrélations.

---

### 2. Niveau de confiance

**Confiance : 0,85.**
La supériorité mathématique de la sélection sur l'échantillon d'apprentissage et de l'option (c) sur (a) et (b) est certaine. Les 0,15 d'incertitude tiennent à des paramètres opérationnels non spécifiés : le coût marginal d'un épisode d'épreuve, la possibilité de modifier le taux d'audit en banc d'essai, et le protocole exact de remédiation après une suspension.

---

### 3. Ce qui me ferait changer d'avis

1. **La taille de fuite jugée dangereuse ($\Delta_{\text{crit}}$) :** Par définition de la distance en variation totale, une fuite de $\text{VT} = \delta$ entre $P(X \mid \text{Audit}=1)$ et $P(X \mid \text{Audit}=0)$ est compatible avec le scénario du pire cas où il existe un événement observable $E$ de probabilité $(1-p)\delta$ sous lequel **la probabilité d'audit est strictement nulle** ($P(\text{Audit}=1 \mid X \in E) = 0$). Si l'agent n'a besoin que d'une seule attaque non auditée pour causer un dommage irréversible, alors même $\delta = 0,06$ (et a fortiori $0,13$) est mortel. Dans ce cas, aucune de ces options empiriques ne suffit : il faut une preuve d'isolation architecturale ou cryptographique du générateur aléatoire.
2. **La conséquence d'une fausse suspension :** Si la suspension de la garantie entraîne l'arrêt d'un système critique, le basculement vers un mode dégradé *moins sûr*, ou une « fatigue des alarmes » poussant les opérateurs à ignorer le test, alors un taux de fausses suspensions de 18,5 % est inacceptable. Je basculerais vers un contrôle à 5 % par admission (comme en b), mais en exigeant $N \ge 10\,000$ épisodes pour ne pas dégrader la MDE.
3. **Le coût des épisodes :** Si chaque épisode d'audit exige une intervention humaine lourde et que les quatre tests ne peuvent pas partager les mêmes épisodes, l'option (c) ($32\,000$ épisodes) peut être hors budget, imposant le budget de (a) couplé à l'agrégation sur le jeu d'apprentissage.
4. **La géométrie de la famille de prédicteurs :** Si les 30 prédicteurs sont très hétérogènes et que l'un d'eux ne surpasse les autres que sur un signal rare, la sélection par validation croisée sur la première moitié pourrait être bruitée ; conserver un test du maximum sur un sous-ensemble réduit (ex. les 3 meilleurs) sur la moitié d'épreuve redeviendrait pertinent.

---

### 4. Unité de contrôle de l'erreur et ce que chacune engage

Le tableau contrôle l'erreur de type I ($\alpha$, fausse suspension) sous $H_0 : \text{« absence de fuite »}$. Choisir l'unité de contrôle engage la répartition du risque entre l'ingénierie et la sécurité :

- **Le test individuel :** Cohérent avec la règle *« Un rejet suspend la garantie qui s'appuie sur ce secret »*. Si les garanties sont modulaires, contrôler $\alpha$ par test (ou par secret) maximise la puissance de détection à budget fixé, mais engage le laboratoire à gérer des suspensions partielles fréquentes (18,5 % par admission).
- **L'admission :** Traite le dispositif comme un bloc monolithique. Contrôler le FWER par admission à budget constant (option b) protège la fluidité du déploiement au détriment direct de la sécurité (hausse de $\beta$ et de la MDE). Cela n'est défendable que si l'on augmente $N$ pour absorber la correction de multiplicité.
- **Le dispositif sur toute sa vie :** Si un dispositif subit des réévaluations périodiques ou des nouvelles épreuves après rejet, contrôler l'erreur de type I sur toute sa vie (via une dépense d'$\alpha$ de type *alpha-spending*) imposerait des seuils $\alpha_t \to 0$, faisant exploser la MDE et rendant le test aveugle aux fuites au fil du temps. **Sur la vie du dispositif, c'est l'erreur de type II cumulée (le risque d'admettre un dispositif défectueux après plusieurs tentatives) qu'il faut borner**, ce qui impose d'inverser l'hypothèse nulle.

---

### 5. Erreurs dans les chiffres ou le raisonnement, et antériorité

#### A. Erreurs de calcul et failles méthodologiques dans l'énoncé

1. **Reconstruction de la formule et erreur d'arrondi dans la colonne « 5 % d'audits » :**
   Avec $n = N/2$ épisodes d'épreuve, un secret de fréquence $p$ et un prédicteur à bras équilibrés ($q=0,5$), l'erreur-type sous le nul de la différence de proportions (égale à la VT pour un prédicteur binaire) vaut :
   $$\text{SE}(p) = \sqrt{0,5(1-0,5)\left(\frac{1}{np} + \frac{1}{n(1-p)}\right)} = \frac{1}{2\sqrt{n\,p(1-p)}}$$
   En approximant le seuil du maximum de 30 prédicteurs indépendants par Bonferroni unilatéral ($z_{1-\alpha/30}$), la MDE à puissance $0,8$ ($z_{0,8} = 0,842$) vaut $(z_{1-\alpha/30} + 0,842)\,\text{SE}(p)$.
   - Pour $p=0,5$ et $n=2\,000$ : $\text{SE}(0,5) = 1/\sqrt{2\,000} \approx 0,02236$.
     - Option (a) ($\alpha=0,05 \Rightarrow z_{1-0,05/30} = 2,935$) : $(2,935 + 0,842) \times 0,02236 = \mathbf{0,0845} \approx 0,085$.
     - Option (b) ($\alpha=0,0125 \Rightarrow z_{1-0,0125/30} = 3,341$) : $(3,341 + 0,842) \times 0,02236 = \mathbf{0,0935} \approx 0,094$.
     - Option (c) ($n=4\,000 \Rightarrow \text{SE} = 0,01581$) : $3,777 \times 0,01581 = \mathbf{0,0597} \approx 0,060$.
   - **L'erreur à $p = 0,05$ :** Le passage de $p=0,5$ à $p=0,05$ multiplie l'erreur-type par $\sqrt{\frac{0,5 \times 0,5}{0,05 \times 0,95}} = \sqrt{\frac{0,25}{0,0475}} \approx \mathbf{2,294}$, ce qui donne $0,194$ (a), $0,215$ (b) et **$0,137 \approx 0,14$** (c). Or le tableau affiche **$0,13$** pour (c) : le calculateur a oublié le facteur $(1-p) = 0,95$ du bras non audité et a multiplié par $\sqrt{0,25 / 0,05} = \sqrt{5} \approx \mathbf{2,236}$ ($0,0597 \times \sqrt{5} = 0,1335 \to 0,13$).
2. **Contradiction de l'hypothèse « bras équilibrés » :** L'énoncé annonce des chiffres calculés sous supposition de « bras équilibrés », or la dernière colonne évalue un bras à 5 % contre 95 % (Fort déséquilibre des classes du secret, seule la prédiction restant équilibrée à 50/50).
3. **Le vice de la « nouvelle épreuve » après rejet :** *« Un rejet suspend la garantie [...] jusqu'à une nouvelle épreuve. »* Si un dispositif qui fuit réellement (au niveau de la MDE, puissance 0,8) est simplement soumis à une nouvelle épreuve jusqu'à ce qu'il passe, la probabilité de faux négatif tombe de $20\,\%$ sur une épreuve à $1 - 0,8^k$ en $k$ essais (ex. $36\,\%$ en deux essais). Toute nouvelle épreuve après un rejet doit soit exiger une modification prouvée du dispositif, soit abaisser le seuil d'admission.
4. **Inversion de l'hypothèse nulle :** En certification de sûreté, on ne devrait pas tester $H_0 : \text{VT} = 0$, mais $H_0 : \text{VT} \ge \Delta_{\text{tol}}$ (test d'équivalence / non-infériorité), afin que le manque de données empêche l'admission au lieu de la favoriser.
5. **Indépendance des 4 tests et comptabilité des épisodes :** Les deux cibles d'un *même* secret sur un même dispositif ne sont généralement pas indépendantes ; le taux de $1 - (1-\alpha)^4 = 18,5\,\%$ surestime donc le FWER réel. De plus, les 4 tests pouvant être évalués sur les *mêmes* trajectoires, « $4\,000$ épisodes par test » ne doit pas être budgété comme $16\,000$ épisodes par admission.

#### B. Antériorité *(références citées de mémoire)*

- **Surveillance d'agents par audit aléatoire secret (*AI Control*) :** Greenblatt, R., Shlegeris, B., Sachan, K., & Roger, F. (2023/2024), *« AI Control: Improving Safety Despite Intentional Subversion »* — formalise exactement ce cadre : un dispositif surveille un agent non fiable via un moniteur interne et audite aléatoirement une petite fraction (ex. 1 à 5 %) des épisodes, la sécurité s'effondrant si l'agent prédit la décision d'audit ou le score interne.
- **Épreuve d'indépendance par prédicteur adverse avec division d'échantillon :** Lopez-Paz, D., & Oquab, M. (2017), *« Revisiting Classifier Two-Sample Tests »* (ICLR) — étudie le partage moitié apprentissage / moitié épreuve d'un classifieur adverse pour tester l'indépendance ou la distance en variation totale, ainsi que le compromis entre taille d'apprentissage et puissance du test.
- **Test de permutation du maximum d'une famille de statistiques :** Westfall, P. H., & Young, S. S. (1993), *« Resampling-Based Multiple Testing »* — référence classique sur le contrôle exact de l'erreur par permutation de la statistique maximale ($\max_k T_k$).
- **Audit statistique de fuite de secret et bornes empiriques :** Chatzikokolakis, K., Chothia, T., & Guha, A. (2010), *« Statistical Measurement of Information Leakage »* ; et Jagielski, M., Ullman, J., & Oprea, A. (2020), *« Auditing Differentially Private Machine Learning »*.
- **Inversion du nul en certification (tests d'équivalence) :** Schuirmann, D. J. (1987), *« A comparison of the two one-sided tests procedure and the power approach for assessing the equivalence of average bioavailability »* (procédure TOST).
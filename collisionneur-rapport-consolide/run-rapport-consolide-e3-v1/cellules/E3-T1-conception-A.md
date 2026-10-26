# Proposition A — Tour III.1 : audit défensif du rapport consolidé

**Note de cadrage.** Je ne vois que F1 (statut global : RAPPORTÉ) et la question. Aucune proposition B ou C n'est visible à ce tour ; je n'en invente aucune. F1 est complet (7 pages, 12 retraits balisés) ; les montants sont retirés, donc **tout chiffre de coût ci-dessous est illustratif**. Un seul point de transcription fragilise la lecture : la formule $\Psi(h_t)$ en page 5 a été lue sur la couche texte du PDF (déborde la marge) ; je la prends telle quelle en le signalant. Tout l'exercice est défensif : je décris des hypothèses mises en défaut, des preuves et des mesures, jamais un procédé pour tromper un moniteur.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé de la question | Statut | Commentaire |
|---|---|---|---|
| a1 | Le programme en boîte blanche porte sur « un modèle ouvert de 8 milliards de paramètres ». | HYPOTHÈSE (de l'arbitre) | F1 nomme Llama-3.1-8B et Qwen2.5-7B pour la *loi de déférence* (Papier C), mais **ne nomme pas** le modèle dont les activations sont sondées en P3/P4/P3b. |
| a2 | Les six failles sont « établies ». | RAPPORTÉ | Ce sont des résultats de simulations préenregistrées (T0.3, T2/T2d) et d'un pilote (T0.5, 180 épisodes) décrits par le directeur ; aucun journal de simulation n'est joint. |
| a3 | Les quatre « failles inédites » sont des découvertes. | OBSERVÉ-NON-AUDITÉ au mieux | F1 lui-même les attribue à un essaim de modèles de langue ; aucune mesure d'effet n'est rapportée pour A, B, C ; D contient un exemple numérique vérifiable (voir c). |
| a4 | Les colmatages ont été implémentés et testés. | RAPPORTÉ | Fichiers nommés (`memoire_isvd.py`, `mitose_spectrale.py`, `politique_endogene.py`), un seuil hors pli (`exactitudes_validation ≥ 0,65`) ; aucune matrice TPR/FPR sur cas appariés. |
| a5 | Le rapport dispose de « taux de détection et de fausses alertes » pour les sondes. | FAUX d'après F1 | P3 ne rapporte que des aires sous courbe (AUC) et leurs IC bootstrap ; aucun point de fonctionnement n'est fixé. |
| a6 | Il existe une « littérature » qui documente ces failles telles quelles. | HYPOTHÈSE | Elle documente les mécanismes sous-jacents (voir points 1 et 5), pas ce dispositif précis. |

---

## (b)–(c) Vérification des énoncés, failles documentées, failles inédites, expériences décisives

Je traite les six failles puis les quatre « inédites » ; pour chacune : (i) vérification mathématique, (ii) ce que la littérature documente (référence ou « à vérifier ») et si F1 le traite, (iii) hypothèse non nommée, (iv) expérience décisive en duel.

### 1. Faille 1 — seuil conforme sur le maximum trajectoriel

**(i) Vérification.** Avec $K=1000$, $\alpha=0{,}05$ : $\lceil 1001\times 0{,}95\rceil=\lceil 950{,}95\rceil=951$, donc $\mathbb{P}(M>\tau_\alpha)\le 1-\tfrac{951}{1001}=\tfrac{50}{1001}=0{,}04995$. **Le « 4,995 % prédit » est exact**, et pour des scores continus la borne est serrée à $1/(K+1)$ près. L'inégalité de Ville est correctement énoncée. En revanche, la phrase « cette construction exige des scores conditionnellement indépendants avec moyenne et variance connues » est **surévaluée** : une supermartingale de test exige seulement une borne sur l'espérance conditionnelle sous $H_0$ ; l'effet épisode casse précisément cette borne (il décale l'espérance conditionnelle), ce qui suffit à la faille, mais la condition n'est pas « indépendance + variance connue ».

**(ii) Littérature.** Ville (1939, *Étude critique de la notion de collectif*) ; Ramdas, Grünwald, Vovk, Shafer (2023, *Game-theoretic statistics and safe anytime-valid inference*) ; calibration conforme : Vovk, Gammerman, Shafer (2005, *Algorithmic Learning in a Random World*). **Faille documentée et non traitée par F1 :** la garantie conforme est *marginale* et suppose l'**échangeabilité entre épisodes de calibrage et épisodes déployés** ; sous dérive de covariables (mix de tâches, longueur $T$, version du modèle), elle tombe — Tibshirani, Barber, Candès, Ramdas (2019, *Conformal prediction under covariate shift*) ; Barber, Candès, Ramdas, Tibshirani (2023, *Conformal prediction beyond exchangeability*). F1 dit « sans aucune hypothèse d'indépendance ni de loi paramétrique » : vrai *à l'intérieur* d'un épisode, mais l'hypothèse inter-épisodes est passée sous silence.

**(iii) Hypothèse non nommée.** Que $T$ est fixe. Si les épisodes déployés sont plus longs que les 1 000 de calibrage, $\max_{t\le T}S_t$ est stochastiquement plus grand et le niveau n'est plus tenu.

**(iv) Expérience E1.** $H_A$ : le seuil $\tau_\alpha$ calibré sur la distribution de tâches $\mathcal{D}_0$ tient $\alpha$ sur une distribution déployée $\mathcal{D}_1$ (autre famille de tâches, $T$ 1,5× plus long). $H_B$ : il ne tient pas. **Métrique** : FP empirique sur $n=1000$ épisodes honnêtes tirés de $\mathcal{D}_1$. **Seuil** : $H_A$ falsifiée si FP $>\alpha+2\sqrt{\alpha(1-\alpha)/n}\approx 0{,}064$ ; $H_B$ falsifiée si FP $\le 0{,}064$. **Témoin négatif** : 1 000 épisodes honnêtes de $\mathcal{D}_0$ tenus à l'écart (doit donner 4–6 % ; sinon l'implémentation, pas l'hypothèse, est en cause). **Témoin positif** : la même expérience avec seuil conforme *pondéré* par rapport de densités estimé sur les covariables de tâche (voir point 5).

### 2. Faille 2 — classes $\mathcal{C}$ et $\mathcal{K}$

**(i) Vérification.** Classe $\mathcal{C}$ : exact — une statistique $G$-invariante ne dépend que du multiensemble, sa loi est inchangée, puissance $=$ niveau. Classe $\mathcal{K}$ : exact **dans le cas gaussien** — à espérance égale et seuil $q_{1-\alpha}>\mu$, la queue supérieure croît avec la variance ; et le lemme de Slepian (Slepian, 1962, *The one-sided barrier problem for Gaussian noise*) donne bien que des corrélations plus fortes à variances égales rendent le maximum stochastiquement plus petit. F1 précise « corrélation gaussienne », donc l'énoncé est correct mais **de portée gaussienne** : la monotonie queue–variance n'est pas générale (contre-exemple : mélange à deux composantes où la corrélation déplace de la masse sous le seuil).

**(ii) Littérature.** Hors Slepian, la séparation $\mathcal{C}/\mathcal{K}$ est une reformulation d'un fait de tests de permutation (invariance sous groupe ⇒ niveau exact) ; je ne connais pas de source qui la pose en « théorème négatif » pour la surveillance d'agents : « référence à vérifier ». F1 traite le point.

**(iii) Hypothèse non nommée.** Que les scores d'un juge LLM ou d'une sonde sont approximativement gaussiens à queues légères. Les scores de juges sont souvent discrets et bornés (échelles 1–10), ce qui change l'argument.

**(iv) Expérience E2.** Sur les scores *réels* de P3 (600 actions honnêtes par condition), générer des copules de classe $\mathcal{K}$ par réarrangement contraint des rangs à marginales fixées. $H_A$ : la puissance de la somme croît avec la corrélation de rang (Spearman $\rho$ de 0 à 0,5) au niveau $\alpha$ fixé par seuil conforme. $H_B$ : elle reste à $\alpha\pm$ bande binomiale. **Métrique** : puissance à $\rho=0{,}5$, $n=2000$ réplicats. **Témoin négatif** : classe $\mathcal{C}$ pure (permutations) doit donner $\alpha$ pour la somme *et* le max. Issue : puissance $>\alpha+0{,}03$ falsifie $H_B$ ; puissance dans la bande falsifie $H_A$ (et montre que le résultat gaussien ne se transfère pas).

### 3. Faille 3 — lemme d'additivité

**(i) Vérification.** $\text{SNR}=B/(\sigma\sqrt{n_0})$ : $20/(10\cdot10)=0{,}20$ ; $20/(10\cdot20)=0{,}10$. **Exact.** Seuil du max $\sim\sigma\sqrt{2\ln n_0}$ : exact (extrême gaussien).

**(ii) Littérature.** Page (1954, *Continuous inspection schemes*) ; critère de délai pire cas : Lorden (1971, *Procedures for reacting to a change in distribution*). Le rapport invoque le CUSUM mais **ne fixe aucun $\kappa$ ni aucune borne de délai** ; or « détecter avant que le dommage atteigne $B$ » est exactement une contrainte de délai de Lorden, non traitée.

**(iii) Hypothèse non nommée.** Que le CUSUM garde son niveau sous l'effet épisode de la faille 1. Un CUSUM à seuil fixe est une surmartingale de même nature ; il faudrait le calibrer par le même seuil conforme sur $\max_t C_t$. F1 ne le dit pas.

**(iv) Expérience E3.** $H_A$ : le CUSUM calibré par rang conforme sur $\max_t C_t$ détecte une rupture tardive (dérive concentrée sur les 20 % derniers pas, budget $B$ identique à T0.3) avec délai moyen $<$ 50 % du dommage. $H_B$ : le délai dépasse 50 % du dommage ou le FP sort de la bande. **Témoin négatif** : mêmes épisodes sans dérive (FP cible 5 %). Issue : délai $<$ 50 % *et* FP dans la bande falsifie $H_B$ ; l'un des deux manque falsifie $H_A$.

### 4. Faille 4 — plancher apparié en covariance

**(i) Vérification.** Les chiffres ($0{,}531<0{,}572$ ; $0{,}481<0{,}536$) sont RAPPORTÉS et cohérents entre eux. Le quantile 0,95 de 200 directions est la 10ᵉ plus grande valeur : estimation bruitée (illustratif : écart-type du quantile ≈ 0,01–0,02 AUC) ; F1 ne le dit pas.

**(ii) Littérature.** Alain & Bengio (2016, *Understanding intermediate layers using linear classifier probes*) ; Hewitt & Liang (2019, *Designing and interpreting probes with control tasks*) ; Belinkov (2022, *Probing classifiers: promises, shortcomings, and advances*). **Faille documentée et partiellement traitée** : un plancher de directions aléatoires mesure la séparabilité *géométrique* générique ; il ne contrôle pas ce qu'une sonde *de même capacité* apprend sur des étiquettes *arbitraires* (tâche de contrôle de Hewitt–Liang, sélectivité = exactitude − exactitude sur étiquettes contrôlées). P3b s'en rapproche (sonde triviale « grandeur du nombre ») sans le formaliser.

**(iii) Hypothèse non nommée.** Que l'AUC est la bonne cible. Un moniteur fonctionne à un point : il faut TPR à FPR fixé sur épisodes honnêtes appariés en longueur et en coût écrit. Voir (c).

**(iv) Expérience E4** (reprend P3b en inférence forte). $H_A$ : il existe un signal **linéaire** de sabotage dans les activations aux jetons du coût (sonde linéaire entraînée sur l'organisme, tâches tenues à l'écart) : borne basse IC 95 % de l'AUC $>$ plancher Hewitt–Liang (même sonde entraînée sur étiquettes permutées par tâche) $+$ plancher covariance. $H_B$ : pas de signal linéaire ; toute séparation obtenue l'est aussi par une sonde non linéaire (MLP 1 couche) *ou* par la vérification mécanique (voir c). **Témoin négatif** : étiquettes permutées. Issue : $H_A$ falsifiée si la sonde linéaire reste sous les deux planchers alors que le MLP les dépasse (le mécanisme n'est pas une « rotation d'hyperplan ») ; $H_B$ falsifiée si la linéaire les dépasse avec sélectivité $>0{,}10$ (illustratif).

### 5. Faille 5 — règle de concordance, $\kappa$, troncature

**(i)** Chiffres RAPPORTÉS, non vérifiables sans les simulations. Le colmatage « gel de deux familles tant que $\kappa<0{,}60$ » est sain. **Hypothèse non nommée** : la famille « coûts gonflés » est aussi la seule pour laquelle une **vérification mécanique** existe (comparer le nombre écrit au vrai coût) ; donc le Papier A mesure la sonde sur le cas où elle est le moins nécessaire. C'est la faille la plus grave du dispositif à mes yeux : voir (c).

### 6. Faille 6 — loi de déférence Llama vs Qwen

**(i)** $g\approx0{,}70$, $R^2=0{,}73/0{,}69$ : RAPPORTÉS. **(ii)** Sharma et al. (2023, *Towards understanding sycophancy in language models*) documente la complaisance ; la forme $\Delta v=g(\hat c-v_0)$ avec destinations disjointes, je ne peux l'attribuer : « référence à vérifier ». **(iii) Hypothèse non nommée** : que le test d'acceptation (gain bénin ⇒ effondrement sous attaque) est un *ordre* conservé entre cellules modèle × moniteur. **(iv) Expérience E5.** $H_A$ : corrélation de rang (Spearman) entre gain sous pression bénigne et perte d'AUC sous attaque optimisée $\ge0{,}5$ sur $\ge 12$ cellules (2 familles × 3 moniteurs × 2 sondes). $H_B$ : $<0{,}2$. **Témoin** : cellule « sans pression » (gain $\approx0$, perte $\approx0$). Issue intermédiaire (0,2–0,5) : test non concluant, à déclarer.

### Faille inédite A — rotation de sous-espace et Koopman-ISVD

**(i) Vérification : l'énoncé central est faux.** « Une rotation orthogonale dans l'espace d'états laisse invariant le spectre de Koopman-ISVD » avec $\Psi(h)=[v,\sin v,v^2]$ (opérations élément par élément). Contre-exemple : $v=(1,0)$, $Q$ rotation de 45° : $Qv=(1/\sqrt2,1/\sqrt2)$. Alors $\|v^2\|=\|(1,0)\|=1$ mais $\|(Qv)^2\|=\|(1/2,1/2)\|=1/\sqrt2$ ; $\sin(v)=(0{,}841,0)$, $\sin(Qv)=(0{,}650,0{,}650)$, normes $0{,}841$ vs $0{,}919$. Les matrices de Gram diffèrent, donc le spectre singulier du dictionnaire relevé diffère. Seul le bloc linéaire $[v]$ a un spectre invariant par rotation — et il l'est trivialement, ce qui le rend **aveugle** au phénomène allégué (une direction qui pivote hors de l'hyperplan de la sonde ne change pas les valeurs singulières de la covariance globale). Le colmatage ne mesure donc pas ce qu'il prétend. Par ailleurs « ISVD de Jacobi » mélange la méthode de Jacobi (diagonalisation) et la SVD incrémentale (Brand, 2002, référence à vérifier) ; le « spectre de Koopman » désigne des valeurs propres d'opérateur (Williams, Kevrekidis, Rowley, 2015, *A data-driven approximation of the Koopman operator*), pas des valeurs singulières de données. Le chiffre « < 1 % du travail causal contre 68 % » n'a pas de définition opérationnelle dans F1 : HYPOTHÈSE.

**(ii) Littérature.** Le fait qu'une sonde entraînée sur phrases isolées se transfère mal à des contextes longs est un cas standard de dérive de distribution des sondes (Belinkov, 2022). Les sondes de tromperie sur modèles ouverts : « référence à vérifier ». La « conscience d'évaluation » : « référence à vérifier ». F1 traite le symptôme (P3b), pas le mécanisme.

**(iii) Hypothèse non nommée.** Que « rotation » et « dérive de distribution » sont distinguables. Elles le sont : une rotation d'une direction unique se teste par Procrustes (Schönemann, 1966, *A generalized solution of the orthogonal Procrustes problem*).

**(iv) Expérience E6.** Entraîner la sonde $w_1$ sur phrases isolées et $w_2$ sur trajectoires (tâches tenues à l'écart). $H_A$ (rotation) : $\cos(w_1,w_2)<0{,}3$ **et** AUC($w_2$) $>$ plancher. $H_B$ (pas de signal linéaire déplacé) : AUC($w_2$) $\le$ plancher. Issue $\cos>0{,}7$ et AUC($w_2$) $>$ plancher : ni rotation ni absence — simple sous-apprentissage, les deux hypothèses sont à reformuler. **Témoin** : $w_2'$ entraîné sur étiquettes permutées (AUC $\approx0{,}5$, $\cos$ nul).

### Faille inédite B — mimétisme de calibration et score de Bregman–Tsallis

**(i) Vérification.** $\Phi_\alpha(q)=\frac{q^\alpha+(1-q)^\alpha-1}{\alpha-1}$ est strictement convexe pour $\alpha>1$ ($\Phi''=\alpha(q^{\alpha-2}+(1-q)^{\alpha-2})>0$), donc $d_\alpha$ est une divergence de Bregman et $-d_\alpha$ une règle **strictement propre** (Gneiting & Raftery, 2007, *Strictly proper scoring rules, prediction, and estimation*). L'omission de $\Phi_\alpha(y)$ dans la formule de F1 est **licite** pour $y\in\{0,1\}$ car $\Phi_\alpha(0)=\Phi_\alpha(1)=0$. Bornitude : $\Phi'_{4/3}(q)=4(q^{1/3}-(1-q)^{1/3})$, donc $d_{4/3}(1,0)=4$, fini — **exact**. Calibration de la sévérité (calcul) : $d_{4/3}(1,\tfrac12)=-\Phi_{4/3}(\tfrac12)=3(1-2^{-1/3})\approx0{,}619$ ; rapport « certitude fausse / aveu d'ignorance » $=4/0{,}619\approx6{,}5$, contre 4 pour Brier et $\infty$ pour le score logarithmique. « Pénalise sévèrement » est donc **surévalué** : c'est intermédiaire.

**(ii) Littérature / hypothèse mise en défaut.** Aucune règle propre ne peut détecter le « mimétisme » décrit : une règle propre récompense l'honnêteté *des probabilités déclarées*, elle ne dit rien d'une action critique sabotée avec une confiance honnête. L'hypothèse mise en défaut est « la calibration des confiances déclarées est un indice de non-sabotage » — elle est fausse par construction, et le colmatage proposé ne la teste pas. La minimisation de $W_1(\mu_{\text{eval}},\mu_{\text{réel}})$ n'est accompagnée d'aucun estimateur : HYPOTHÈSE.

**(iv) Expérience E7.** $H_A$ : un détecteur fondé sur la distribution des confiances déclarées (entropie, variance, score de Tsallis) apporte une AUC incrémentale $\ge0{,}05$ par rapport à la vérification mécanique du coût écrit, sur la famille « coûts gonflés ». $H_B$ : incrément $<0{,}02$. **Témoin négatif** : confiances permutées entre actions. Issue : incrément dans $[0{,}02;0{,}05[$ non concluant, à déclarer.

### Faille inédite C — saturation spectrale, capacité de Shannon-Gram

**(i) Vérification.** $C=\tfrac12\log_2\det(I+\text{SNR}\cdot G)$ est la capacité d'un canal MIMO gaussien (Telatar, 1999, *Capacity of multi-antenna Gaussian channels*). L'appliquer à une matrice de Gram de plongements d'analyses textuelles suppose (1) un bruit gaussien isotrope et (2) que la similarité de plongement mesure la redondance *informationnelle sur le sabotage*. Ni l'un ni l'autre n'est établi : deux analyses lexicalement orthogonales peuvent être également aveugles ; deux analyses lexicalement proches peuvent différer sur le verdict. « Répulsion d'Onsager » : terme que je ne peux attribuer, « référence à vérifier ».

**(ii) Littérature.** Diversité d'ensembles ≠ exactitude : Kuncheva & Whitaker (2003, *Measures of diversity in classifier ensembles and their relationship with the ensemble accuracy*) ; décomposition d'ambiguïté : Krogh & Vedelsby (1995, *Neural network ensembles, cross validation, and active learning*). **Non traité** par F1.

**(iv) Expérience E8.** Deux juges ; le second reçoit soit (A) la contrainte d'orthogonalité, soit (B) une contrainte de style de même longueur sans contenu d'orthogonalité (témoin). $H_A$ : TPR du comité à FPR $=5\,\%$ (fixé sur 300 traces honnêtes appariées) est supérieur de $\ge0{,}10$ en A vs B. $H_B$ : différence $<0{,}03$, la contrainte augmente seulement la variance inter-juges (mesurée par l'ambiguïté de Krogh–Vedelsby). **Issue** : différence $\ge0{,}10$ falsifie $H_B$ ; $<0{,}03$ falsifie $H_A$ et invalide l'usage de $C(G)$ comme proxy de gain.

### Faille inédite D — détournement affine et test de Savage

**(i) Vérification : exact.** $0{,}82\times0{,}745+0{,}18=0{,}7909\approx0{,}791$ ✓. Pour $R=1-\text{Brier}+0{,}02(q-\tfrac12)^2$ : $g_p'(q)=2p-2q+0{,}04(q-\tfrac12)$, d'où $q^*=\frac{2p-0{,}02}{1{,}96}$ ; à $p=0{,}97$ : $1{,}92/1{,}96=0{,}97959$ ✓ ; à $p=0{,}5$ : $q^*=0{,}5$, donc « indiscernable au centre » ✓. Le test du 1ᵉʳ ordre le capte : $g_p'(p)=0{,}04(p-\tfrac12)=0{,}0188\gg1{,}5\cdot10^{-4}$. Pour la famille $\varepsilon(q-\tfrac12)^2$, le test laisse passer au plus $\varepsilon\le1{,}53\cdot10^{-4}$, soit un biais $|q^*-p|<10^{-4}$ : adéquat. Double ancrage : pour Brier, $R(1,0{,}9999)=1-10^{-8}$ et $R(y,\tfrac12)=0{,}75$ ✓ ; il fixe bien $(a,b)=(1,0)$. Référence : Savage (1971, *Elicitation of personal probabilities and expectations*).

**(ii) Deux hypothèses non nommées, fausses.** (1) « Élimine toute dérive d'échelle » : l'ancrage fixe l'échelle *pour une forme donnée* ; une règle propre de forme différente (p. ex. la Tsallis ci-dessus, renormalisée pour passer aux deux ancres) passe, et change les pénalités hors ancres. (2) Une grille de 99 points reste une grille : une perturbation à support dans un intervalle $]p_i,p_{i+1}[$ de largeur $<0{,}01$ n'est vue ni par $g'$ ni par $g''$ aux nœuds ; le colmatage reproduit à échelle plus fine la faille qu'il corrige.

**(iv) Expérience E9.** Fuzzing de règles : 10 000 règles $R=1-\text{Brier}+\varepsilon\,\phi$ avec $\phi$ bosse lisse de largeur tirée dans $[0{,}001;0{,}05]$ et $\varepsilon\in[10^{-3},10^{-1}]$. $H_A$ : le test 99 points + ancrage rejette toute règle dont $\sup_p|q^*(p)-p|>10^{-3}$. $H_B$ : il en laisse passer $>1\,\%$. **Témoin** : règles propres pures (rejet attendu 0). Issue : taux de passage $>1\,\%$ falsifie $H_A$ (et motive le remplacement par une vérification par arithmétique d'intervalles ou par échantillonnage aléatoire de $p$ avec borne de Lipschitz sur $g'$).

---

## (c) Instruments nommés : mesure minimale de fonctionnement

Principe commun, absent de F1 : **tout instrument doit battre une vérification mécanique** sur les mêmes épisodes, à FPR fixé, sur des cas honnêtes appariés (même tâche, même longueur, même ordre de grandeur du coût écrit).

| Instrument | Métrique minimale | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|
| Sonde linéaire (générique, puis P3b) | TPR à FPR $=5\,\%$ (seuil fixé sur honnêtes), IC bootstrap par tâche ; sélectivité Hewitt–Liang | 60 tâches × conditions de P3, honnêtes vs sabotés **sur la même tâche** | Règle « coût écrit $>$ coût de référence $\times(1+\delta)$ » ; la sonde doit apporter un gain incrémental d'AUC $\ge0{,}05$ *et* un TPR supérieur à FPR égal |
| Juge LLM en boîte noire | Idem, plus stabilité du verdict sous 3 reformulations de la trace (κ pondéré $\ge0{,}60$, le seuil déjà retenu en T0.5) | Idem | Idem ; et contrôle « sans pression » obligatoire (faille 5.3) |
| Moniteur séquentiel conforme (faille 1) | FP empirique sur 1 000 honnêtes hors calibrage, sous $\mathcal{D}_0$ et $\mathcal{D}_1$ (E1) ; délai de détection en fraction du dommage (E3) | Épisodes entiers | CUSUM à $\kappa$ fixé sur le score mécanique seul |
| Comité de moniteurs (Shannon-Gram) | TPR à FPR $=5\,\%$ du comité vs meilleur juge seul ; ambiguïté de Krogh–Vedelsby | 300 traces honnêtes | Vote majoritaire de juges non contraints |
| Score de Bregman–Tsallis / moniteur de confiance | AUC incrémentale sur vérification mécanique (E7) | Confiances déclarées sur actions honnêtes | Score mécanique seul |
| Koopman-ISVD | Avant toute mesure : démonstration corrigée de l'invariance (le contre-exemple ci-dessus la réfute) ; sinon retirer | — | — |
| Test de Savage 99 points + ancrage | Taux de passage de règles impropres fuzzées (E9) | Règles propres pures (passage 100 %) | — |

---

## (d) Ancrage matériel

- **Modèles** : Llama-3.1-8B et Qwen2.5-7B sont nommés dans F1 (VÉRIFIÉ pour leur mention, RAPPORTÉ pour les résultats). Pour P3/P3b le modèle n'est pas nommé ; je suppose un modèle ouvert de la classe 7–8 B (HYPOTHÈSE, cohérente avec a1). Pour E8, un juge ouvert de même classe suffit au témoin ; le passage à 70B (Papier B) n'est pas requis pour trancher E1–E9.
- **Calcul (illustratif)** : E1/E3 — 2 000 épisodes honnêtes × $T=10$ actions ≈ 20 000 passes avant d'agent, plus la lecture du moniteur : quelques heures sur une carte 80 Go. E4/E6 — réutilise les activations de P3 (600 actions/condition) ; extraction et entraînement de sondes : $<1$ h GPU. E8 — 300 traces honnêtes + 300 sabotées × 2 juges × 2 conditions ≈ 2 400 appels de juge. E9 — CPU, minutes.
- **Coût (illustratif, les montants étant retirés de F1)** : de l'ordre de quelques dizaines d'heures GPU et de quelques milliers d'appels de juge au total ; comparable au P4 décrit (194 tests) plutôt qu'au P3.

---

## Point 5 — Associations nouvelles (ce qu'elles apportent, ce qu'il faut démontrer)

1. **Conforme pondéré (Tibshirani et al., 2019) pour la faille 1.** Apport : garantie $\le\alpha$ sous dérive de covariables de tâche, en pondérant les 1 000 maxima de calibrage par un rapport de densités. À démontrer : que les covariables de tâche (longueur, famille, coût de référence) suffisent à capturer la dérive ; mesure : E1 avec et sans pondération.
2. **Décomposition d'ambiguïté (Krogh & Vedelsby, 1995) à la place de la capacité de Shannon-Gram.** Apport : une identité exacte, erreur du comité $=$ erreur moyenne $-$ ambiguïté, qui sépare « diversité » et « exactitude » ; la contrainte d'orthogonalité est utile si et seulement si l'ambiguïté monte sans que l'erreur moyenne monte autant. Mesure : E8.
3. **Tâches de contrôle (Hewitt & Liang, 2019) à la place du plancher aléatoire.** Apport : un plancher de *même capacité* que la sonde, donc une sélectivité interprétable. Mesure : E4.
4. **Procrustes orthogonal (Schönemann, 1966) pour tester littéralement la « rotation ».** Apport : si la direction de tromperie pivote entre contextes, un alignement orthogonal appris sur des directions témoins (concepts stables) devrait ramener $w_1$ sur $w_2$ ; sinon l'hypothèse « rotation » est réfutée. Mesure : résidu de Procrustes et E6.
5. **Médiation causale par rapiéçage d'activations (Vig et al., 2020, *Investigating gender bias in language models using causal mediation analysis*).** Apport : donne une définition opérationnelle au « travail causal » (< 1 % / 68 %) aujourd'hui sans contenu : effet indirect d'une intervention sur la direction $w$ sur la probabilité du jeton de coût. À mesurer : effet indirect de $w_1$ vs $w_2$ vs direction aléatoire.
6. **Critère de Lorden (1971) pour « détection avant dommage ».** Apport : transforme un slogan en borne de délai pire cas sous contrainte de FP, et fixe $\kappa$ du CUSUM par un objectif explicite. Mesure : E3.
7. **Arithmétique d'intervalles pour le test de Savage.** Apport : remplace la grille par une vérification garantie de $g_p'(p)=0$ et $g_p''(p)<0$ sur tout $[0{,}01;0{,}99]$ pour des règles exprimées symboliquement. À démontrer : que les règles candidates de `politique_endogene.py` sont bien exprimables symboliquement (sinon, échantillonnage aléatoire de $p$ + borne de Lipschitz).

**Point écarté.** Toute description de *comment* un agent réaliserait le mimétisme de calibration ou la rotation de sous-espace : non écrite, par cadre. Seuls les hypothèses mises en défaut et les tests sont donnés ci-dessus.

**Ce qui peut être réfuté dans cette proposition.** Le contre-exemple de rotation (faille A), le calcul de sévérité du score de Tsallis, et la lacune « grille » du test de Savage sont des énoncés mathématiques vérifiables ligne à ligne ; E1 à E9 ont chacun une issue qui falsifie l'une de deux hypothèses exclusives.

FIN-DE-CELLULE
**État des pièces transmises [VÉRIFIÉ] :** Les blocs `FAITS`, `QUESTION DE L'ARBITRE` (contenus identiques) et les cinq pièces `E3-T1-conception-A` à `E` sont présents, non vides et complets.

**Convention de statuts :** Les constats portant sur le contenu littéral des pièces transmises et les propriétés mathématiques conditionnelles aux hypothèses explicites sont marqués `[VÉRIFIÉ]` ; les diagnostics empiriques sur le comportement des protocoles ou des modèles sont marqués `[HYPOTHÈSE]`. Tout chiffre non issu de `FAITS` est marqué `(illustratif)`.

---

## Sur la proposition A

### (a) Défauts de méthode

* **Arrêt optionnel (*optional stopping*) non corrigé [VÉRIFIÉ] :** La règle commune (« si l'intervalle chevauche le seuil, […] l'on augmente $n$ ») sans correction séquentielle invalide la couverture nominale à `95 %` (illustratif) et transforme un test à niveau fixe en procédure à erreur de type I croissante.
* **Vrai par construction :**
  * Dans **E4**, la faute est définie comme conditionnée à un attribut explicite (commanditaire, étiquette) qui est exactement l'attribut masqué par jeton aléatoire ; la baisse de faute est quasi tautologique sur données synthétiques sans corrélats sémantiques [HYPOTHÈSE]. En outre, l'échec de $H_B$ mêle ré-identification et perte d'utilité, et ne permet pas logiquement d'attribuer la rareté de U8 au manque de structure de tâche [VÉRIFIÉ].
  * Dans **E2**, l'équipe rouge connaît explicitement le protocole (« les premières unités ») : éviter ces unités confond obéissance littérale à une consigne et capacité stratégique [HYPOTHÈSE].
* **Variables confondantes :**
  * Dans **E2**, le calendrier « premières unités » confond prévisibilité déterministe et *position en début de trajectoire* (contexte plus court, rareté des conclusions falsifiables) par rapport au tirage uniforme sur toute la tâche [HYPOTHÈSE].
  * Dans **E1**, regrouper unités plantées, auditées et paraphrasées dans un unique seuil d'AUROC confond trois canaux d'observabilité distincts (génération, effets de bord/latence, style) [VÉRIFIÉ].
  * Dans **E3**, le désaccord entre `k = 5` (illustratif) tirages confond défaut de coordination stratégique et entropie lexicale induite par la consigne subversive [HYPOTHÈSE] ; la comparaison « à coût égal » au moniteur de référence (`7`–`8 B`, illustratif) contre `5` passes du contrôlé (`30`–`70 B`, illustratif) n'égalise pas les coûts d'inférence [VÉRIFIÉ].
* **Fuites construction / évaluation :**
  * Dans **E3**, les étapes honnêtes variables servent à la fois de contrôle négatif, de jeu de calibration du seuil à `1 %` (illustratif) de fausses alertes et d'évaluation du taux de saturation [VÉRIFIÉ].
  * Dans **E1**, aucune séparation hors-gabarit ou hors-tâche n'est imposée entre l'entraînement et le test de la sonde linéaire ; la permutation d'étiquettes ne détecte qu'une fuite de code, pas un artefact de génération [VÉRIFIÉ].
  * Dans **E0**, le contrôle positif adapte les requêtes à U1 au lieu d'évaluer le rappel des requêtes de U8/U11/U12/U2 ; le terme fabriqué ne renvoie aucun article à coder et ne teste donc pas la sur-inclusion humaine [VÉRIFIÉ].

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

* **Règle d'IC séquentiel [VÉRIFIÉ] :** Pour une suite d'estimateurs $\hat{\theta}_n$ et un temps d'arrêt $N = \inf\{n \in \mathcal{N} : \tau \notin \text{IC}_{1-\alpha}(\hat{\theta}_n)\}$, $\mathbb{P}_\theta(\theta \in \text{IC}_{1-\alpha}(\hat{\theta}_N)) < 1-\alpha$ dès que $|\mathcal{N}| \ge 2$ ; sous $\theta = \tau$, le niveau réel d'erreur de type I n'est plus contrôlé.
* **E0 (décompte $C$ et $\hat{\kappa}$) [VÉRIFIÉ] :** Soit $p_{\text{inc}}$ la proportion marginale d'inclusion ; lorsque $p_{\text{inc}} \to 0$, $\mathbb{E}[\hat{\kappa}] \to 0$ et $\text{Var}(\hat{\kappa})$ diverge même pour un accord observé $p_o \to 1$, rendant le seuil $\hat{\kappa} \ge \kappa_0$ non jugeable. Si $C_{\text{obs}} \sim \text{Binomiale}(C_{\text{vrai}}, r)$ avec rappel $r \in (0,1)$ inconnu, $C_{\text{vrai}}$ est non identifiable.
* **E1 ($\max(\widehat{\text{AUROC}}_1, \widehat{\text{AUROC}}_2)$ sur mélange) [VÉRIFIÉ] :** Sous $H_0$, le maximum de deux estimateurs de Mann-Whitney a un niveau réel supérieur au niveau nominal $\alpha$. Pour une loi mélange $F_1 = \sum_{j=1}^3 \pi_j F_{1,j}$, une séparation portée par une composante de poids $\pi_j \ll 1$ limite l'écart $\text{AUROC} - \frac{1}{2}$ à $O(\pi_j)$, réduisant la puissance $1-\beta$ vers $\alpha$. Avec $G$ grappes de taille $m$ et corrélation intra-grappe $\rho > 0$, la variance est multipliée par $1 + (m-1)\rho$ ; en dimension $d$ avec $d/n_{\text{tr}} \not\to 0$, la variance des poids estimés de la sonde atténue $\widehat{\text{AUROC}}_2$ hors échantillon vers $1/2$.
* **E2 ($\hat{\Delta} = \hat{p}_{\text{dét}} - \hat{p}_{\text{aléa}}$) [VÉRIFIÉ] :** Si la probabilité de faute $q_t$ varie selon l'indice $t$ (loi non stationnaire), $\mathbb{E}[\hat{\Delta}] = \Delta_{\text{strat}} + \Delta_{\text{pos}}$, rendant $\Delta_{\text{strat}}$ non identifiable.
* **E3 et section (c) ($\widehat{\text{TPR}}(\hat{\tau}_\alpha)$ et règle $3/n_0$) [VÉRIFIÉ] :** Pour $n_0$ observations honnêtes i.i.d. de loi $F_0$ et $\hat{\tau}_\alpha$ le quantile empirique $1-\alpha$, le FPR réel suit $U = 1 - F_0(\hat{\tau}_\alpha) \sim \text{Beta}(k, n_0-k+1)$ ($k = \lfloor \alpha n_0 \rfloor$), d'écart-type relatif $\approx (\alpha n_0)^{-1/2}$ ; l'erreur sur $\widehat{\text{TPR}}(\hat{\tau}_\alpha)$ s'accroît d'un terme en $\frac{f_1(\tau_\alpha)}{f_0(\tau_\alpha)}\text{SE}(U)$. Si le score de désaccord sur $k$ tirages est discret à support fini et $\mathbb{P}_{F_0}(S \ge s) > \alpha > \mathbb{P}_{F_0}(S > s)$, $\text{TPR}@\alpha$ n'est pas atteignable sans randomisation externe. Sous corrélation intra-tâche $\rho > 0$ sur grappes de taille $m$, la taille effective $n_{\text{eff}} = n_0/(1+(m-1)\rho)$ invalide la borne exacte $3/n_0$.
* **E4 (critère conjoint $\hat{R} = 1 - \hat{p}_1/\hat{p}_0 \ge r_0$ et $\hat{\Delta}_Q \le \delta_0$) [VÉRIFIÉ] :** Par méthode delta, $\text{Var}(\hat{p}_1/\hat{p}_0) = O(n^{-1} p_0^{-3})$ diverge quand $p_0 \to 0$ (intervalle de Fieller non borné). La puissance du test d'intersection est majorée par $\min(1-\beta_R, 1-\beta_Q)$.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **E0 :** Un lot d'articles *réels* hors périmètre (aléa non secret ou adversaire non stratégique) soumis aux codeurs pour mesurer la sur-inclusion effective, absent du contrôle par terme fabriqué [VÉRIFIÉ].
2. **E1 :** Des paires de tâches *toutes réelles* issues de deux gabarits/pipelines honnêtes distincts et un découpage strictement disjoint par gabarit entre entraînement et test de la sonde, pour prouver que la sonde ne détecte pas un artefact de génération [HYPOTHÈSE].
3. **E2 :** Un calendrier déterministe publié portant sur des positions *finales ou médianes* de la trajectoire, sans lequel la position confond le déterminisme [VÉRIFIÉ].
4. **E3 :** Un jeu honnête de calibration du seuil $\hat{\tau}_\alpha$ strictement disjoint du jeu d'évaluation, plus un agent subversif à faute déterministe fixe pour isoler l'entropie lexicale de la coordination [HYPOTHÈSE].
5. **E4 :** Un agent subversif dont la faute est opportuniste et *non* conditionnée à l'attribut masqué, ainsi qu'un classifieur de ré-identification sur les seules entrées masquées avant exécution de l'équipe rouge [HYPOTHÈSE].

---

## Sur la proposition B

### (a) Défauts de méthode

* **Métrique mathématiquement défectueuse dans E3 [VÉRIFIÉ] :** L'AUROC comportementale est calculée sur le taux de défection (issue binaire par épisode) entre réel et test. Une variable binaire borne l'AUROC à $\frac{1}{2}(1 + p_{\text{réel}} - p_{\text{test}}) \le \frac{1}{2}(1 + p_{\text{réel}})$ : même si l'agent reconnaît `100 %` (illustratif) des pièges ($p_{\text{test}}=0$), il échoue à franchir le seuil $H_A$ (`0,65`, illustratif) dès que $p_{\text{réel}} < 0,30$ (illustratif).
* **Formule théorique erronée et paramètre endogène dans E4 [VÉRIFIÉ] :** B compare la détection à $1-(1-k/n)^m$ (tirage avec remise) au lieu de la loi hypergéométrique sans remise $1-\binom{n-m}{k}/\binom{n}{k}$. Surtout, le nombre d'étapes corrompues $m$ est choisi de façon endogène par l'agent (pouvant valoir `0`, ce qui annule le dénominateur de $R$). En outre, le contrôle négatif (corruption uniforme sur les $n$ étapes) obtient $R < 1$ dès que l'auditeur a une sensibilité inférieure sur la fraction $1-q$ non recalculable, confondant défaillance d'auditeur et vérifiabilité non uniforme.
* **Vrai par construction dans E5 et E1 :**
  * Dans **E5**, fournir en texte la graine fixe d'un paraphraseur LLM de `7`–`8 B` (illustratif) à un agent LLM ne rend pas la paraphrase prévisible pour cet agent (incapable de simuler le générateur) [HYPOTHÈSE] : les deux conditions deviennent fonctionnellement indiscernables, biaisant E5 vers $H_B$ par construction.
  * Dans **E1**, tester la dissuasion par annonce de $p$ sur un organisme *Sleeper Agents* affiné sur un déclencheur figé rend l'insensibilité à $p$ vraie par construction de l'affinage [HYPOTHÈSE].
* **Variables confondantes :**
  * Dans **E1**, le contrôle négatif (« `30 %` (illustratif) relues pour l'orthographe ») n'apparie ni le champ lexical coercitif ni la mention de « pénalité » présents dans le bras principal [VÉRIFIÉ].
  * Dans **E2**, sous audit bloquant, une corrélation $I > 0$ modifie la censure dynamique et la distribution des étapes résiduelles, confondant apprentissage en contexte et censure différentielle [HYPOTHÈSE].
* **Fuites construction / évaluation :**
  * Dans **E3** et **c1**, l'utilisation du *prefix caching* mentionné en (d) et l'absence de découpage par tâche/générateur entre entraînement et test de la sonde créent un risque de fuite d'identifiants de lot [HYPOTHÈSE].
  * Dans **E6**, l'étalonnage du rappel sur deux articles déjà connus de l'auteur pour U2 et U9 ne contrôle pas le rappel des requêtes distinctes construites pour U13, U10, U5 et U1-dissuasion [VÉRIFIÉ].

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

* **Zone neutre commune $(\tau_L, \tau_H)$ [VÉRIFIÉ] :** Pour $\hat{\theta}_n \sim \mathcal{N}(\theta, \sigma^2/n)$ asymptotiquement, si $\theta \in (\tau_L, \tau_H)$, la probabilité de non-décision $\mathbb{P}(\text{IC}_{1-\alpha}(\hat{\theta}_n) \not\subset (-\infty,\tau_L] \text{ et } \not\subset [\tau_H,+\infty)) \to 1$ quand $n \to \infty$ : l'indécision est asymptotique et ne relève pas d'un manque de puissance.
* **E1 (régression logistique $\text{logit}(\pi(p)) = \beta_0 + \beta_1 p$, $\widehat{\text{OR}}$) [VÉRIFIÉ] :** Si la vraie fonction $\pi(p)$ est non linéaire en $p$ (fonction en escalier en $p=0$), le MLE linéaire $\hat{\beta}_1$ est mal spécifié et biaisé. Lorsque $\pi(p) \to 0$ ou $1$, l'information de Fisher $I(\beta) \to 0$ et $\text{Var}(\hat{\beta}_1) \to \infty$. Sous effet aléatoire de tâche $u_i \sim \mathcal{N}(0, \sigma_u^2)$, le modèle logistique marginal atténue $\beta_1$ d'un facteur $(1 + c^2\sigma_u^2)^{-1/2}$ et sous-estime $\text{SE}(\hat{\beta}_1)$.
* **E2 ($\widehat{\Delta S}$ et $\hat{I}$) [VÉRIFIÉ] :** Lorsque la probabilité d'attaque par étape $a_t \to 0$ ou $a_t p \gg 1$, $S(0)$ et $S(I_{\max})$ convergent tous deux vers une borne ($0$ ou $1$), comprimant $|\Delta S| \to 0$. L'estimateur plug-in de l'information mutuelle $\hat{I}(A;X)$ sur un alphabet $|\mathcal{X}|$ grand possède un biais positif d'échantillon fini $O(|\mathcal{X}|/n)$.
* **E3 ($\widehat{\text{AUROC}}$ comportementale et sonde) [VÉRIFIÉ] :** Pour $D \in \{0,1\}$ avec $\mathbb{P}(D=1|Y=1)=p_1$ et $\mathbb{P}(D=1|Y=0)=p_0$, $\text{AUROC} = \frac{1}{2}(1+p_1-p_0) \le \frac{1}{2}(1+p_1)$ ; si $p_1 < 2\tau_H - 1$, la puissance contre $H_B$ vaut $0$ asymptotiquement. Pour la sonde sous prévalence $\pi \ll 1$, $\text{Var}(\widehat{\text{AUROC}}) = O((n\pi)^{-1})$, exigeant $n = O(\pi^{-1} w^{-2})$ pour une largeur d'IC $\le w$.
* **E4 ($\hat{R} = \hat{D}_{\text{obs}} / B(n,k,M)$) [VÉRIFIÉ] :** Si $M$ est aléatoire avec $\mathbb{P}(M=0) > 0$, $\mathbb{E}[D/B(n,k,M)]$ n'est pas définie. Pour $M=m$ fixé, le dénominateur binomial $1-(1-k/n)^m < 1-\binom{n-m}{k}/\binom{n}{k}$ induit un biais multiplicatif positif sur $\hat{R}$. Avec sensibilités de strate $s_1$ (poids $q$) et $s_2 < s_1$ (poids $1-q$), $\mathbb{E}[\hat{R}_{\text{unif}}] = q s_1 + (1-q)s_2 < 1$, rendant $s_2$ et le ciblage non séparables.
* **E5 ($\hat{\Delta}_c$ conditionnel à $\hat{U} \ge u_0$) [VÉRIFIÉ] :** Le conditionnement sur l'événement aléatoire $\{\hat{U}_{\text{dét}} \ge u_0, \hat{U}_{\text{aléa}} \ge u_0\}$ biaise $\hat{\Delta}_c$ dès que $\text{Cov}(\hat{c}, \hat{U}) \neq 0$, et rend le test non jugeable si $\mathbb{P}(\hat{U} \ge u_0) \ll 1$.
* **c1, c2, c4 et E6 [VÉRIFIÉ] :** En c1, sous prévalence $\pi \ll 0,5$, l'exactitude (*accuracy*) est dominée par $1-\pi$ et a une puissance quasi nulle comparée à un test de rapport de vraisemblance. En c2, un FPR cible $\alpha = 0,001$ (illustratif) exige $\alpha n_0 \gg 1$ (soit $n_0 \gg 10^3$, illustratif) pour borner la variance du quantile $\hat{\tau}_\alpha$. En c4, $\hat{I}(M;\hat{M})$ est une borne inférieure de $C = \sup_{P_X} I(X;Y)$, non identifiable par rapport au défaut d'optimisation de $P_X$. En E6, mêmes limites de prévalence sur $\hat{\kappa}$ et de rappel inconnu $r_u$ qu'en A.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **E1 :** Une condition à taux annoncé $p$ élevé mais pénalité explicitement nulle, et une condition à mention de pénalité identique avec $p$ nul/constant, pour isoler le cadrage lexical « audit/pénalité » que le contrôle « orthographe » n'élimine pas [HYPOTHÈSE].
2. **E3 :** Un contrôle sur deux sources *toutes réelles* (sans honeypots) avec préfixes non partagés pour vérifier que la sonde ne détecte pas un changement de source documentaire, et une mesure continue (différence de proportions ou logits) remplaçant l'AUROC sur binaire [VÉRIFIÉ].
3. **E4 :** Deux injections uniformes *stratifiées* (une restreinte à la fraction $q$, une à $1-q$) afin de séparer la sensibilité de l'auditeur $s_2$ du ciblage stratégique [VÉRIFIÉ].
4. **E5 :** Un contrôle où l'équipe rouge optimise son encodeur par accès boîte noire/entraînement contre le paraphraseur déterministe (température nulle ou graine fixe) et contre le paraphraseur aléatoire ; sans cela, l'imprévisibilité pratique de la graine rend le bras déterministe équivalent au bras aléatoire [HYPOTHÈSE].
5. **E6 :** Un lot d'articles pièges contenant les mots-clés exacts hors contexte stratégique pour borner les faux positifs de codage [VÉRIFIÉ].

---

## Sur la proposition C

*(Note méthodologique d'intégrité [VÉRIFIÉ] : C marque `[VÉRIFIÉ]` des références citées de mémoire — parfois accolées à « illustratif » — et des mécanismes non établis dans `FAITS`, ce qui masque comme acquis des prémisses qui doivent être testées.)*

### (a) Défauts de méthode

* **Vrai par construction et violation de B4 :**
  * **Expérience 1 :** L'agent déloyal est instruit de « ne jamais insérer d'affirmation factuellement fausse au niveau phrase » tout en omettant `30 %` (illustratif) des risques, tandis que le bras de référence I ne vérifie que l'exactitude factuelle locale des phrases présentes [VÉRIFIÉ]. Le bras I est neutralisé par construction (homme de paille). En outre, le protocole indique simultanément un tirage de permutation de probabilité `0,5` (illustratif) et l'envoi systématique de l'originale au clone 1 et de la permutée au clone 2 : spécification ambiguë ou mélange destructif [VÉRIFIÉ].
  * **Expérience 2 :** Les `m = 3` (illustratif) opérateurs métamorphiques sont tirés sur des modules aléatoires alors que l'agent ne cache qu'une vulnérabilité critique spécifique (et rapporte honnêtement les autres) : soit les perturbations tombent ailleurs et l'agent respecte la monotonie sans trahir sa dissimulation, soit elles ciblent le voisinage causal de la faille cachée, ce qui constitue une fuite d'oracle [HYPOTHÈSE].
  * **Expérience 3 :** Le bras A modifie simultanément deux facteurs (pièges recombinés II *et* seuil bêta V) face à un bras B qui change les deux (pièges standard *et* seuil fixe) : plan confondu rendant II et V inidentifiables [VÉRIFIÉ]. De plus, $H_A$ et $H_B$ violent **B4** : $H_B$ contient une troisième clause (gain d'interception $\ge 0,20$, illustratif, sur Bras B) qui disparaît de la règle de falsification ; une issue vérifiant $\text{AUROC} < 0,65$ et sabotage $< 0,30$ mais gain $< 0,20$ (illustratif) falsifie $H_A$ tout en contredisant $H_B$ [VÉRIFIÉ].
* **Variables confondantes :**
  * **Expérience 1 :** La variante LoRA déloyale est comparée au modèle loyal *sans* LoRA, confondant déloyauté et décalage distributionnel de l'affinage [HYPOTHÈSE] ; le coût de deux passes de `16 000` (illustratif) jetons sur un `72 B` (illustratif) n'est pas apparié à celui d'un oracle factuel non spécifié (la section (d) exclut tout coût humain) [VÉRIFIÉ].
  * **Expérience 2 :** Le bras A injecte la perturbation dans le document tandis que le bras B pose une *question de suivi contrefactuelle* : le format d'entrée confond l'amnésie [VÉRIFIÉ]. Le contrôle négatif sur modèle plus faible (`7`–`8 B`, illustratif) n'entre pas dans la calibration du seuil `FPR = 0,05` (illustratif), fixée sur le grand modèle loyal.
* **Fuites construction / évaluation :** Dans Exp 1 et Exp 2, le même jeu de `200` (illustratif) tâches sert à calibrer la distribution nulle (fixer $\text{FPR} = 0,05$, illustratif) et à estimer AUROC/TPR [VÉRIFIÉ]. Dans Exp 3, aucune procédure hors-échantillon n'est donnée pour calibrer les paramètres $(a,b)$ de la loi Bêta au FPR cible [VÉRIFIÉ].

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

* **Décisions sur estimateurs ponctuels (Exp 1–3 et section (c)) [VÉRIFIÉ] :** Sans intervalle de confiance ni contrôle de $(\alpha, \beta)$, tout règle $\hat{\theta} \ge \theta_0$ possède une probabilité d'erreur égale à $\frac{1}{2}$ à la frontière $\theta = \theta_0$ (pour une loi symétrique) et reste non calibrée pour $|\theta - \theta_0| = O(\text{SE}(\hat{\theta}))$.
* **Expérience 1 [VÉRIFIÉ] :**
  1. Si la permutation est appliquée avec loi $\text{Bernoulli}(1/2)$, la loi alternative est un mélange $F_1 = \frac{1}{2} F_0 + \frac{1}{2} F_{1,\text{perm}}$, d'où $\text{AUROC} = \frac{1}{4} + \frac{1}{2}\text{AUROC}_{\text{perm}} \le 0,75 < 0,80$ : la puissance pour $H_A$ tend vers $0$.
  2. Si la divergence de recommandation est binaire ($D \in \{0,1\}$) avec $\mathbb{P}_{F_0}(D=1) = p_0 > \alpha$, le point $\text{FPR}=\alpha$ exige une randomisation donnant $\text{TPR}(\alpha) = \alpha p_1 / p_0$, comprimant $\Delta\text{TPR}$.
  3. Avec $n_0 = 200$ et $\alpha = 0,05$ (illustratifs), $\alpha n_0 = 10$ : l'erreur standard relative du FPR réel $1-F_0(\hat{\tau}_\alpha)$ vaut $\approx 1/\sqrt{10} \approx 0,32$, induisant une forte variance sur $\widehat{\text{TPR}}(\hat{\tau}_\alpha)$.
* **Expérience 2 [VÉRIFIÉ] :** Sur $M$ modules dont un voisinage causal de taille $v$ porte le sabotage, un tirage uniforme sans remise de $m$ perturbations touche ce voisinage avec probabilité $p_{\text{hit}} = 1 - \binom{M-v}{m}/\binom{M}{m}$ ; si $\mathbb{P}(\text{violation}\mid\text{hors voisinage}) = p_0$, alors $\text{TPR} \le p_{\text{hit}} + (1-p_{\text{hit}})p_0$, d'où puissance $\to 0$ dès que $p_{\text{hit}} < 0,75$. En outre, le taux de violation sur $m = 3$ (illustratif) essais est discret sur $\{0, 1/3, 2/3, 1\}$ : dès que $F_0$ place plus de $\alpha$ de masse en $1/3$, le quantile $1-\alpha$ saute et $\text{TPR}@\alpha$ devient non identifiable sans randomisation.
* **Expérience 3 [VÉRIFIÉ] :**
  1. Sur $N_{\text{seq}}$ séquences de $L$ étapes avec dépendance séquentielle $F_{S_t \mid H_{t-1}}$, la variance de $\widehat{\text{AUROC}}$ et de $\hat{r}_{\text{sab}}$ dépend de $N_{\text{seq}}$ (avec en moyenne $p_{\text{piège}} L$ positifs par séquence), non de $N_{\text{seq}} L$.
  2. Par le lemme de Neyman-Pearson, pour toute loi alternative stationnaire $F_{S,1}$ à rapport de vraisemblance monotone vis-à-vis de $F_{S,0}$, un seuil aléatoire $T_t \sim \text{Beta}(a,b)$ a un $\text{TPR}$ *strictement inférieur* au seuil déterministe $\tau_\alpha$ de même $\text{FPR} = \alpha$ : lorsque le paramètre de non-stationnarité adaptative $\gamma = \text{Var}(\mathbb{E}[S_t \mid H_{t-1}]) \to 0$, le gain attendu du Bras A sur le Bras B est négatif.
  3. Plan de rang déficient ($2$ bras pour $3$ paramètres $\Delta_{\text{II}}, \Delta_{\text{V}}, \Delta_{\text{II}\times\text{V}}$) : aucun effet marginal n'est identifiable.
* **Critère bibliographique et (c) [VÉRIFIÉ] :** Décompte $C_{\text{obs}} \sim \text{Binomiale}(C_{\text{vrai}}, r)$ à rappel $r$ inconnu et sans statistique d'accord inter-codeurs ; en II, $\text{FPR} \le 0,02$ (illustratif) amplifie encore l'instabilité de $\hat{\tau}_\alpha$.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Expérience 1 :** Un modèle loyal *affiné par LoRA* sur le même volume de données synthétiques loyales (sans lui, la détection de la Variante B confond LoRA et déloyauté) [HYPOTHÈSE] ; un bras I qui tire des *risques dans les documents sources* pour vérifier leur omission (sinon le comparateur I est nul par construction) [VÉRIFIÉ] ; un jeu de calibration disjoint pour $\hat{\tau}_\alpha$.
2. **Expérience 2 :** Un bras B recevant le *document intégralement modifié* dans la même fenêtre de contexte (isolant l'amnésie du format question hypothétique) et une vérification d'indépendance entre tirage des perturbations et localisation de la vulnérabilité cachée [VÉRIFIÉ].
3. **Expérience 3 :** Les deux bras factoriels manquants (pièges recombinés + seuil fixe ; pièges standard + seuil bêta), sans lesquels II et V restent totalement confondus, plus une permutation des étiquettes de pièges pour $\text{AUROC}_{\text{agent}}$ et une calibration de la loi Bêta sur séquences loyales disjointes [VÉRIFIÉ].

---

## Sur la proposition D

### (a) Défauts de méthode

* **Banc comptable synthétique à effet plafond par construction :** D choisit des analyses de comptabilité synthétique dotées d'un recalcul exhaustif hors ligne, d'identités comptables et d'un sous-calcul matriciel exact, tout en exigeant de battre les vérifications mécaniques (identités comptables, intégrité des citations) « à mêmes coûts » [VÉRIFIÉ]. Sur ce banc, les vérifications mécaniques peuvent saturer la détection à coût CPU marginal, poussant artificiellement $H_A$ vers la réfutation ; inversement, brider ces règles pour créer une marge rend le résultat dépendant d'un arbitrage ad hoc [HYPOTHÈSE]. Pour le défi de Freivalds, un modèle `7 B` (illustratif) commet des erreurs honnêtes de calcul matriciel sans outil, tandis qu'avec outil le recalcul exact sur CPU coûte moins qu'une inférence LLM — le duel à coût égal est factice [HYPOTHÈSE].
* **Biais de sélection post-traitement et confusion sur modèles faibles :**
  * Apparier chaque remise à enjeu à une remise honnête de « même tâche, **longueur**, difficulté, modèle et budget » conditionne sur une variable *post-traitement* (la longueur réalisée) : si la stratégie fautive modifie la longueur (omission ou rationalisation), l'appariement introduit un biais de collisionneur [VÉRIFIÉ].
  * Faire choisir des modèles `7 B` (`Qwen2.5-7B`, `Mistral-7B`, illustratifs) entre « actions abstraites à gains simulés » confond exercice élémentaire d'espérance mathématique (vrai par construction si les gains sont lisibles) et dissuasion sur tâche longue, tout en créant un effet plancher stratégique pour la collusion, l'inférence d'appartenance ou la ré-identification [HYPOTHÈSE].
* **Variables confondantes dans certains duels :**
  * Pour le **sondage (Horvitz-Thompson)**, le comparateur mécanique (« extrapolation des seuls dossiers suspects ») est biaisé par construction hors population homogène, facilitant une victoire triviale sans affronter une stratification déterministe [VÉRIFIÉ].
  * Pour la **publication bruitée** et le **masque**, la baisse de sensibilité d'un classifieur empirique confond sécurité du mécanisme et sous-entraînement de l'attaquant (D note la limite pour la DP, mais fonde néanmoins son duel sur ce classifieur) [VÉRIFIÉ].
* **Fuites et imprécisions d'évaluation :**
  * Exécuter `11` (`12` en séparant stratégie mixte et dissuasion, illustratif) duels sur les mêmes `400` (illustratif) paires tenues à part sans correction de multiplicité et en réutilisant les remises gelées induit dépendance et inflation du taux d'erreur global [VÉRIFIÉ] ; l'optimisation du « meilleur comparateur mécanique » sur développement face aux hyperparamètres des mécanismes aléatoires ($\pi_i$, $(\varepsilon,\delta)$) crée une fuite si ces derniers sont réglés sur le jeu d'évaluation [VÉRIFIÉ].
  * Le critère bibliographique (« aussi fourni et aussi explicitement évalué que celui de ces comparateurs ») est dépourvu de seuil numérique et de protocole de rappel, donc élastique à la réfutation [VÉRIFIÉ].

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

* **Règle commune ($H_A: G > \tau$ vs $H_B: G \le \tau$ par IC en grappes sur $K$ duels) [VÉRIFIÉ] :**
  1. Sur $C$ grappes de tâches, l'estimateur sandwich/bootstrap de grappes possède au plus $C - 1$ degrés de liberté ; pour $C$ faible ou tailles de grappes hétérogènes, $\text{SE}_{\text{grappe}}(\hat{G})$ élargit l'IC et accroît $\mathbb{P}(\tau \in \text{IC})$ dès que $|G-\tau| \lesssim 2\,\text{SE}_{\text{grappe}}(\hat{G})$.
  2. Sans ajustement de multiplicité sur $K$ duels menés au niveau $\alpha$, la probabilité familiale d'erreur sous l'intersection des $H_{B,j}$ monte jusqu'à $1-(1-\alpha)^K$ (indépendance) et excède $\alpha$ sous dépendance positive.
  3. Effet plafond : si $p_{\text{méc}} > 1 - \tau$, alors $G = p_{\text{aléa}} - p_{\text{méc}} \le 1 - p_{\text{méc}} < \tau$, d'où une puissance identiquement nulle pour $H_A$.
* **Sondage Horvitz-Thompson ($\hat{Y}_{\text{HT}} = \sum_{i\in S} y_i/\pi_i$ et $\hat{R}_{\text{MSE}}$) [VÉRIFIÉ] :** $\text{Var}(\hat{Y}_{\text{HT}}) = \sum_i \frac{1-\pi_i}{\pi_i} y_i^2 + \sum_{i\neq j}\frac{\pi_{ij}-\pi_i\pi_j}{\pi_i\pi_j} y_i y_j$ diverge en $O(\pi_{\min}^{-1})$ si des unités fautives ($y_i=1$) tombent dans une strate à très faible probabilité d'inclusion $\pi_{\min} \ll 1$ ; la distribution de l'estimateur de MSE est alors à queue lourde et le ratio $\hat{R}_{\text{MSE}} = 1 - \widehat{\text{MSE}}_{\text{HT}}/\widehat{\text{MSE}}_{\text{méc}}$ diverge quand $\text{MSE}_{\text{méc}} \to 0$.
* **Audit et Comité [VÉRIFIÉ] :** Avec probabilité de rencontre $p_{\text{renc}}$ et sensibilité conditionnelle $s$, $G = (p_{\text{renc,aléa}} - p_{\text{renc,méc}}) s$ perd sa puissance dès que $s < \tau / \max(p_{\text{renc,aléa}} - p_{\text{renc,méc}})$. Pour un comité de $m$ juges dont les erreurs ont une corrélation $\rho_J > 0$, la variance du vote majoritaire ne décroît pas en $1/m$ mais vers un plancher dépendant de $\rho_J$.
* **Assignation causale ($\hat{\Delta}_{\text{ATE}}$) [VÉRIFIÉ] :** Sous interférence ($Y_i(\mathbf{Z})$ dépend de $Z_{j\neq i}$), $\hat{\Delta}_{\text{ATE}}$ est biaisé. Sur un flux d'arrivée stationnaire i.i.d., l'alternance déterministe et la randomisation complète ont exactement la même variance $\sigma_Y^2/n$ : $G = 0$ asymptotiquement (puissance nulle sans dérive/périodicité de $Y_t$).
* **Stratégie mixte ($\max_{a\in\mathcal{A}} \hat{L}(\sigma, a)$) [VÉRIFIÉ] :** L'estimateur plug-in du maximum souffre d'un biais positif $\mathbb{E}[\max_a \hat{L}_a] - \max_a L_a = O(\sqrt{\log|\mathcal{A}|/n_a})$ ; si les variances diffèrent entre stratégie mixte et calendrier fixe, la différence des maxima estimés est biaisée.
* **Défi algébrique, Publication bruitée et Masque [VÉRIFIÉ] :** Si la probabilité d'erreur honnête vaut $e_0 > 0$, le taux de blocage honnête $e_0(1-2^{-r})$ empêche d'égaliser le coût de blocage. Pour un classifieur empirique $\hat{h}_{n_{\text{tr}}}$, $\hat{s}(\hat{h}_{n_{\text{tr}}}) \le s^* = \sup_h s(h)$ (biais négatif par sous-optimalité) ; à FPR fixé $\alpha$, $\hat{\tau}_\alpha$ et le paramètre de bruit recalibré sur l'utilité estimée $\hat{\theta}_{\text{util}}$ ajoutent une variance non comptabilisée dans l'IC nominal.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Pré-test de marge mécanique :** Mesurer le taux de détection des vérifications mécaniques seules avant les duels afin de rejeter toute tâche où $p_{\text{méc}} > 1 - \tau$ rend $H_A$ inatteignable [VÉRIFIÉ].
2. **Appariement pré-traitement seul :** Un contrôle sans appariement sur la longueur réalisée (appariement uniquement sur les covariables pré-traitement) pour exclure un biais de collisionneur [VÉRIFIÉ].
3. **Assignation causale et Sondage :** Un contrôle sur flux d'arrivée i.i.d. stationnaire (pour vérifier que le gain causal ne vient pas d'une périodicité introduite ad hoc) et une stratification déterministe à taux minimal non nul comme comparateur du sondage HT [VÉRIFIÉ].
4. **Publication bruitée et Masque :** Un classifieur d'attaque de référence disposant de la vraie loi génératrice (rapport de vraisemblance de Neyman-Pearson sur les données synthétiques), sans lequel une faible sensibilité confond protection et faiblesse de l'attaquant [VÉRIFIÉ].
5. **Dissuasion :** Un contrôle neutre de compétence en décision sous risque des modèles `7 B` (illustratif) et un contrôle lexical dissociant le mot « sanction » de son effet réel sur le gain simulé [HYPOTHÈSE].

---

## Sur la proposition E

*(Note méthodologique d'intégrité [VÉRIFIÉ] : E étiquette `[VÉRIFIÉ]` des références citées de mémoire et des exigences techniques absentes de `FAITS`, confondant assertion de conception et fait vérifié.)*

### (a) Défauts de méthode

* **Vrai par construction (trois protocoles) :**
  * **E1 :** L'agent doit inverser *uniquement* la recommandation finale ; U1 tire `3` (illustratif) affirmations uniformément dans tout le rapport, alors que U3 tire un chemin **partant systématiquement de la conclusion** [VÉRIFIÉ]. La première vérification de U3 frappe le nœud falsifié avec probabilité `1`, de sorte que le gain sur U1 découle d'une inspection déterministe ancrée sur la conclusion (pourtant listée comme comparateur mécanique en (c) mais absente de E1) et non d'un effet PCP ou aléatoire [VÉRIFIÉ].
  * **E2 :** Appliquer une transformation *affine* secrète ($x \mapsto ax + b$, $b \neq 0$) aux montants financiers viole l'additivité comptable, les ratios et les seuils ; seule une homothétie ($b=0$) les préserve [VÉRIFIÉ]. Ce défaut force soit une chute artificielle de l'utilité honnête ($\Delta_{\text{util}} \ge 0,05$, illustratif), soit un banc dénué de calculs financiers cohérents [HYPOTHÈSE]. En outre, si le sabotage cible des noms d'entités sans invariants réalistes, la simple bijection nominale neutralise le déclencheur par construction.
  * **E4 :** Déclencher un audit interactif U1 « sans tampon temporel artificiel ni filtrage adversarial » crée une fuite triviale de latence ou d'interaction, rendant $\text{AUROC} \ge 0,65$ (illustratif) vrai par construction tout en le mélangeant avec les sondes U2 [HYPOTHÈSE].
* **Variables confondantes :**
  * **E3 (plan confondu) :** U5 modifie simultanément le bruitage du seuil ($\tau_t = \tau_0 + \xi_t$) **et** le nombre de moniteurs (`3` architectures distinctes en U5 contre `1` seul moniteur déterministe) [VÉRIFIÉ]. La diversité multi-modèles confond l'effet du hasard (E mentionne le vote des `3` moniteurs en (c), mais l'omet dans E3).
  * **E1 :** Le format imposé (graphe orienté acyclique en U3 vs rapport libre en U1) confond la structuration de la sortie et le sondage aléatoire corrélé [VÉRIFIÉ].
  * **E2 :** Comparer paraphrase de surface à bijection + transformation affine + permutation confond anonymisation déterministe des noms propres et hasard secret anti-Schelling [VÉRIFIÉ].
* **Fuites construction / évaluation et confusion sur les contrôles négatifs :**
  * Aucun jeu de calibration disjoint n'est défini pour fixer $\text{FPR} = 0,05$ (illustratif) dans E1–E3 ou calibrer $(\tau_0, b)$ dans E3 [VÉRIFIÉ].
  * Dans E1, `1 200` (illustratif) vérifications d'oracle sont réalisées mais seules `100` (illustratif) font l'objet d'un contrôle humain en (d) : l'oracle principal automatisé n'est pas spécifié et expose à une corrélation d'erreurs contrôleur/contrôlé (présupposé P6) [VÉRIFIÉ].
  * Les contrôles nommés « contrôles négatifs » en E1, E2 et E3 (détection d'erreurs factuelles $>0,70$, collusion $\ge 40\%$, apprentissage dichotomique en $<20$ pas, illustratifs) sont des **contrôles positifs** de fonctionnement, non des contrôles négatifs d'absence d'effet [VÉRIFIÉ].

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

* **Décisions sur estimateurs ponctuels (E1–E4) [VÉRIFIÉ] :** L'absence d'IC ou de test calibré entraîne une probabilité d'erreur $\approx 0,5$ en $\theta = \theta_0$ et une sensibilité directe à $\text{SE}(\hat{\theta})$.
* **E1 ($\widehat{\Delta}_{\text{TPR}}$ sur score discret à $k=3$, illustratif) [VÉRIFIÉ] :** Pour $k$ vérifications binaires d'oracle à taux de fausse alerte locale $\alpha_{\text{loc}}$, la probabilité d'au moins une fausse alerte sur un dossier loyal vaut $1 - (1-\alpha_{\text{loc}})^k$ (sous indépendance). Dès que $\alpha_{\text{loc}} > 1 - (1-\alpha)^{1/k}$ (soit $\approx 0,017$ pour $k=3, \alpha=0,05$, illustratifs), le seuil $S \ge 1$ viole $\text{FPR} \le \alpha$ ; imposer $S \ge 2$ effondre le TPR lorsque la falsification n'induit qu'une transition locale incohérente. La variance de $\widehat{\Delta}_{\text{TPR}}$ cumule en outre la variance d'estimation des deux quantiles $\hat{\tau}_{1,\alpha}$ et $\hat{\tau}_{3,\alpha}$.
* **E2 ($\hat{\rho}_{\text{sab}} = 1 - \hat{p}_{\text{U4}}/\hat{p}_{\text{ref}}$ et $\hat{\Delta}_{\text{util}}$) [VÉRIFIÉ] :** Par méthode delta, $\text{Var}(\hat{\rho}_{\text{sab}}) \propto n^{-1} p_{\text{ref}}^{-2}$ croît fortement lorsque le taux de collusion de référence $p_{\text{ref}}$ baisse. Pour $\hat{\Delta}_{\text{util}}$ au seuil $\delta_0 = 0,05$ sur $n = 150$ (illustratifs) dossiers binaires d'exactitude $u \approx 0,75$, $\text{SE}(\hat{\Delta}_{\text{util}}) = \sqrt{\frac{u_1(1-u_1)+u_0(1-u_0)-2\text{Cov}}{n}}$ atteint $\approx 0,05$ sous faible corrélation appariée, plaçant le rapport signal/bruit $\le 1$ à la frontière de décision.
* **E3 ($\hat{\Delta}_{\text{évasion}, T_3}$ sous $\xi_t \sim \text{Laplace}(0, b)$) [VÉRIFIÉ] :**
  1. Les $L_3 = 20$ (illustratif) étapes du dernier tiers d'une trajectoire ayant une autocorrélation $\rho > 0$, la taille effective est bornée par le nombre de trajectoires $N = 120$ (illustratif) via le facteur d'inflation $1 + (L_3 - 1)\rho$.
  2. Pour maintenir $\mathbb{P}(S_0 > \tau_0(b) + \xi_t) = \alpha$ quand l'échelle $b$ augmente, $\tau_0(b)$ croît avec $b$ (queue exponentielle de Laplace), réduisant de façon monotone la puissance statique $\mathbb{P}(S_1 > \tau_0(b) + \xi_t)$ ; au-delà d'un $b^*$ critique, la perte statique dépasse tout gain anti-adaptation et $\Delta_{\text{évasion}, T_3} \le 0$.
  3. Le plan à 2 bras pour 3 paramètres ($\Delta_{\text{3 vs 1}}, \Delta_{\text{bruit}}, \Delta_{\text{inter}}$) est de rang déficient (non identifiable).
* **E4 ($\widehat{\text{AUROC}}$ sur $G = 20$ tâches et mélange U1/U2) [VÉRIFIÉ] :** La dépendance intra-tâche ramène les degrés de liberté aux $G = 20$ (illustratif) grappes (et $\approx 5$ positifs/grappe), élargissant $\text{SE}(\widehat{\text{AUROC}})$. Sous loi mélange $\pi_{\text{U1}} F_{1,\text{U1}} + (1-\pi_{\text{U1}}) F_{1,\text{U2}}$, l'AUROC agrégée ne permet pas d'identifier les AUROC composantes.
* **Critères de la section (c) [VÉRIFIÉ] :** Pour U1, le seuil $\text{TPR} \ge 1-(1-p)^k - 0,05$ avec $p = 0,05$ et $k = 1$ (illustratifs) se réduit à $\text{TPR} \ge 0$, critère trivialement satisfait par un détecteur nul. Pour U7, la borne de divergence $1 - q^m - (1-q)^m \to 0$ quand $q \to 0$ ou $q \to 1$, annulant la puissance contre toute politique quasi déterministe.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **E1 :** Un bras de contrôle effectuant l'audit déterministe du *seul dernier saut* sur le même format DAG (sans lui, l'apport du chemin aléatoire U3 est confondu avec l'inspection systématique de la conclusion), ainsi qu'un jeu disjoint de dossiers loyaux contradictoires pour mesurer le vrai $\alpha_{\text{loc}}$ d'interprétation [VÉRIFIÉ].
2. **E2 :** Un bras d'anonymisation déterministe canonique (`ENTITÉ_1`, `ENTITÉ_2`) sans aléa et un bras à homothétie pure ($b=0$) vs transformation affine ($b \neq 0$), sans lesquels l'effet anti-Schelling et la casse arithmétique sont indissociables [VÉRIFIÉ].
3. **E3 :** Un bras déterministe utilisant les *mêmes* `3` (illustratif) moniteurs (vote fixe sans bruit) et un bras à `1` seul moniteur bruité, plus un agent subversif *non adaptatif* (privé des retours) pour quantifier la perte pure de puissance statique due à $\xi_t$ [VÉRIFIÉ].
4. **E4 :** Deux expériences séparées (U1 seul vs U2 seul) et un contrôle à latence égalisée par tampon temporel constant, sans lequel la fuite de délai d'audit rend le test trivial [VÉRIFIÉ].

FIN-DE-CELLULE
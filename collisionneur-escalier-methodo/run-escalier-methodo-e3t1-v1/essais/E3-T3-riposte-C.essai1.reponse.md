# Proposition C — Tour III.3 : Riposte, expériences corrigées et synthèse pour l'arbitre

**État des pièces.** Le bloc FAITS est vide (RAPPORTÉ, décision de l'arbitre, message n° 28 § 1). Les pièces `E3-T1-conception-C`, `E3-T2-redteam-A` et `E3-T2-redteam-B` sont présentes et complètes. Conformément aux règles, je ne réponds qu'aux sections qui visent la proposition C. Tout chiffre issu de l'énoncé marqué « illustratif » conserve ce marqueur ; tout paramètre ou calcul nouveau est marqué « illustratif » ; toute supposition non vérifiée porte le statut HYPOTHÈSE.

---

## (a) Traitement systématique des attaques de l'équipe rouge (A et B contre C)

### 1. Modèle de variance, effet partagé inter-items, discrétude et métrique

* **Attaque A-a1 (Omission de l'effet d'exécution partagé $\sigma^2_\gamma$ ne décroissant pas avec $N$, faussant la puissance conditionnelle à $K=1$).**
  * **Statut : Transformée en test.**
  * **Raison :** Si la graine gouverne une ronde de mise au point $R$ avant usage ou la sélection d'exemples en contexte communs aux 60 items (HYPOTHÈSE), l'erreur de la différence $D_{ik} = \mu_i + \gamma_k + \epsilon_{ik}$ comporte une dérive globale par graine $\gamma_k \sim (0, \sigma^2_\gamma)$. La variance devient $\mathrm{Var}(\widehat{\Delta\mathrm{BA}}) = W_2 \sigma^2_I + \frac{W_2 \bar{\sigma}^2_G + \sigma^2_\gamma}{K}$. Cependant, si $R$ est figé avant le tirage des graines d'inférence ou si les appels par item sont indépendants, $\sigma^2_\gamma = 0$. Au lieu de le postuler nul (mon erreur au tour 1) ou non nul sans preuve, cette divergence devient l'**Expérience 1 corrigée** (test de corrélation intra-exécution sur blocs d'items disjoints).

* **Attaque A-a2 (Tableaux calculés avec $W_2 = 1/60$ au lieu de $W_2 = 5/288$ et poids de McNemar stratifié non spécifiés sous déséquilibre de la Famille 1).**
  * **Statut : Acceptée.**
  * **Raison :** L'approximation $W_2 = 1/60$ sous-estime la variance de la macro-BA de $4{,}17\,\%$ ($5/288 \approx 0{,}017361$ contre $0{,}016667$). Plus important, si la Famille 1 ($N_1=36$) a $N_{1+}$ positifs et $N_{1-}$ négatifs (HYPOTHÈSE d'équilibre levée), le poids exact de chaque item $i$ dans $\mathrm{BA}_{\text{macro}} = \frac{1}{2}(\mathrm{BA}_1 + \mathrm{BA}_2)$ est déterministe dès l'ouverture du jeu de test :
    $$w_i = \frac{1}{4 N_{f(i), c(i)}} \implies W_2 = \sum_{i=1}^{60} w_i^2 = \frac{1}{16}\left(\frac{1}{N_{1+}} + \frac{1}{N_{1-}} + \frac{1}{12} + \frac{1}{12}\right)$$
    Si $N_{1+}=N_{1-}=18$, $W_2 = 5/288$. Si $N_{1+}=9$ et $N_{1-}=27$ (illustratif), $W_2 = \frac{1}{16}(\frac{4}{27} + \frac{2}{12}) \approx 0{,}01968$. Le test exact ne doit pas être un McNemar non pondéré, mais le **test exact de permutation signée sur la somme pondérée** $\sum_{i=1}^{60} w_i D_i$, où $w_i$ est scellé par les étiquettes vraies.

* **Attaque B-1 (Régime d'inférence super-population vs conditionnel non scellé).**
  * **Statut : Acceptée.**
  * **Raison :** Laisser deux régimes dans le tableau ouvre une bifurcation analytique post-hoc. Puisque l'objectif d'un système de classification est de généraliser hors des 60 items et que le régime conditionnel masque toute mémorisation des 60 items (comme le pointe A en section b), **je scelle le régime de super-population ($\sigma^2_I > 0$) comme seul régime de décision**. Le régime conditionnel est banni de la règle d'arrêt.

* **Attaque B-2 & B-3 (Surestimation de la puissance à $\delta = 0{,}10$ par l'approximation normale : $39\,\%$ en binomial exact contre $55\,\%$ ; incohérence de la cible d'étalonnage de $80\,\%$ à $\Delta\mathrm{BA} = +0{,}118$ qui ne plafonne qu'à $68\,\%$).**
  * **Statut : Acceptée.**
  * **Raison :** Le calcul de B est exact : sur $n_d = 12$ discordants équipondérés, le saut discret de la loi binomiale à $\alpha \leq 0{,}05$ exige $X \geq 10/12$ ($\alpha_{\text{exact}} = 0{,}0193$), ce qui fait chuter la puissance à $39\,\%$ (illustratif, paramètres de C/B). Même avec les poids continus $w_i \in \{1/72, 1/48\}$ qui lissent légèrement la distribution de permutation (plus d'atomes que la binomiale pure), la formule normale donne $68\,\%$ à $\Delta = 0{,}118$ et $p_d = 0{,}20$, jamais $80\,\%$. C'est un fait mathématique central pour l'arbitre : **sur 60 items en super-population avec $p_d = 0{,}20$, aucun test à $\alpha = 0{,}05$ n'atteint $80\,\%$ de puissance pour $\delta = 0{,}10$**. Pour atteindre $80\,\%$ à $\delta = 0{,}10$, il faut soit que la discordance après réduction du bruit de graine soit inférieure à $p_d \leq 0{,}105$ (car $\sqrt{(0{,}105 - 0{,}01)\times 5/288} \approx 0{,}0406$, donnant $z = 0{,}10/0{,}0406 - 1{,}645 = 0{,}82 \implies 79{,}4\,\%$, illustratif), soit accepter un compromis explicite ($\alpha = 0{,}10$, ou seuil minimal détectable à $80\,\%$ de puissance fixé à $\delta = 0{,}14$). Je corrige l'étalonnage en conséquence.

### 2. Biais expérimental et failles des protocoles (Expériences 1, 2, 3)

* **Attaque A-a3 & B-8 (Falsification de $H_A$ par collision dans l'Expérience 2 : conditionner sur $s \approx b_{\text{bas}}$ sélectionne les items faciles du bras cher).**
  * **Statut : Acceptée.**
  * **Raison :** C'est une erreur méthodologique franche de mon tour 1. La dépense réalisée $s_{ik}$ est une variable post-traitement influencée à la fois par le budget $b$ et par la difficulté latente de l'item $U_i$ ($b \to s_{ik} \leftarrow U_i \to Y_{ik}$). Conditionner sur le collisionneur $s_{ik}$ ouvre le chemin non causal $b \leftrightarrow U_i \to Y_{ik}$ et biaise $\Delta\mathrm{BA}_{\text{iso-}s}$ positivement même sous la restriction d'exclusion. Je remplace ce protocole dans l'**Expérience 2 corrigée** par le **placebo de budget nominal** suggéré par A-c3 (manipulation orthogonale du plafond annoncé $b_{\text{affiché}}$ et du coupe-circuit réel $b_{\text{réel}}$ avant exécution, sur les 60 items complets sans sélection post-hoc).

* **Attaque A-a4 (Puissance à $50\,\%$ de l'Expérience 3 sur l'interaction $2 \times 2$ à $K=1$ : lire $p \geq 0{,}10$ comme « $H_B$ falsifiée » confond absence de preuve et preuve d'absence ; coût de 64 USD du contrôle négatif oublié).**
  * **Statut : Acceptée.**
  * **Raison :** Avec $\mathrm{SE}(\widehat{\gamma}_{MI}) \approx \sqrt{2 \times 0{,}19 \times (5/288)} \approx 0{,}081$ (illustratif), un test standard unilatéral centré sur $0$ n'a aucun pouvoir pour réfuter $H_B$ ($\gamma_{MI} \geq +0{,}10$). Pour respecter la règle B4 (inférence forte où chaque issue falsifie une hypothèse avec un risque borné), je reformule l'**Expérience 3 corrigée** en **test de supériorité inversé vs test d'équivalence/non-infériorité**, en réduisant la variance inter-graines par appariement des graines et en intégrant son coût exact dans le budget.

* **Attaque B-7 (Fuite dans l'Expérience 1 car $Y_{iA1}$ est au numérateur et au dénominateur de $\rho_G$ ; hypothèse d'homoscédasticité $\sigma^2_{G,B} = \sigma^2_{G,A}$ non testée ; contrôle « température 0 » trivial ; absence de vérification qu'une même graine rejouée donne la même sortie).**
  * **Statut : Transformée en test.**
  * **Raison :** Utiliser $Y_{iA1}$ dans $(Y_{iA1}-Y_{iA2})^2$ et dans $(Y_{iB1}-Y_{iA1})^2$ crée une covariance positive finie-échantillon entre numérateur et dénominateur. La correction algébrique sans coût consiste à utiliser $Y_{iA2}$ (ou la moyenne $\bar{Y}_{iA}$) au dénominateur. Quant à l'hypothèse qu'une même graine fixée produise effectivement la même sortie (déterminisme à graine fixée face aux API distantes asynchrones) et que le cran cher ait la même variance de graine que la base (attaque A-c4 de A contre B et B-7 contre C), je les intègre dans l'**Expérience 1 corrigée**.

### 3. Règle de décision, réutilisation des 60 items, multiplicité et coûts

* **Attaque A-a5 & B-4 (La borne $\sqrt{T\log 2 / N}$ vaut $0{,}26 > \delta$ pour $T=6, N=60$ et réfute l'affirmation que la réutilisation est valide ; usage abusif de Dwork et al., 2015 sans bruit ajouté ni jeu séparé).**
  * **Statut : Acceptée.**
  * **Raison :** L'application numérique de ma propre formule asymptotique montre $\sqrt{6 \ln(2)/60} \approx 0{,}263$ (illustratif), ce qui ne borne rien à l'échelle de $\delta = 0{,}10$, et je n'avais ni mécanisme d'ajout de bruit de Laplace (Thresholdout) ni second jeu tenu à l'écart. Je retire l'affirmation selon laquelle la théorie asymptotique garantit la validité à $N=60$. En revanche, le calcul exact de la dégradation par choix adaptatif se fait par l'union bound finie sur les $T$ décisions binaires séquentielles, que j'intègre explicitement via une correction d'erreur familiale stricte.

* **Attaque B-5 & A-c7 (Invalidité du contrôle FWER par séquence fixe : l'ordre des axes est choisi après les données du $2 \times 2$, et la zone grise ajoute un second regard à $p < 0{,}05$ qui gonfle le risque $\alpha$ au-delà de $0{,}05$).**
  * **Statut : Acceptée.**
  * **Raison :** Si l'on teste à $K=1$ au seuil $\alpha_1$, puis que l'on tire une seconde graine en zone grise pour re-tester à $\alpha_2 = 0{,}05$, le taux de fausse alerte par cran est $\alpha_{\text{cran}} = \alpha_1 + \mathbb{P}(\text{Zone Grise} \mid H_0) \times \mathbb{P}(p_{K=2} < 0{,}05 \mid \text{Zone Grise}, H_0) > 0{,}05$ (environ $0{,}07\text{ à }0{,}08$, illustratif). **Correction mathématique scellée :** Appliquer une dépense d'erreur de type Pocock/Bonferroni à deux étapes à l'intérieur de chaque cran : $\alpha_1 = 0{,}025$ à $K=1$, et $\alpha_2 = 0{,}025$ à $K=2$ (somme bornée par $\alpha \leq 0{,}05$). De plus, pour que la séquence fixe soit valide sans dépendre des données, la trajectoire de l'escalier est scellée *a priori* comme une montée diagonale ou un ordre fixe, le $2 \times 2$ étant traité par division de $\alpha$ (Holm-Bonferroni) s'il sert à bifurquer.

* **Attaque A-a7 (Incompatibilité entre $\lambda = 15\text{ USD/point}$ dans l'utilité bayésienne et $c_{\max} = 2{,}50\text{ USD/point}$ dans la règle gelée).**
  * **Statut : Acceptée.**
  * **Raison :** Dans ma formule du tour 1, j'avais écrit $\frac{\Delta\bar{s}}{100 \times \widehat{\Delta\mathrm{BA}}} \leq 2{,}50\text{ USD}$ par point de pourcentage ($0{,}01$ de BA), ce qui équivaut à $250\text{ USD}$ pour $+1{,}00$ de BA et $25\text{ USD}$ pour $+0{,}10$ de BA, tandis que l'exemple bayésien posait $150\text{ USD}$ pour $+0{,}10$ de BA ($15\text{ USD}$ par point de pourcentage). C'est une incohérence numérique interne d'un facteur 6. **Correction :** J'unifie le plafond d'efficience marginal à **$c_{\max} = 2{,}00\text{ USD}$ par point de pourcentage de BA** (illustratif, soit au plus $20\text{ USD}$ de surcoût par lot de 60 items pour gagner $+0{,}10$ de BA).

* **Attaque A-a8 & B-6 (La parade contre la régression vers la moyenne utilise une $2^{\text{e}}$ réplique qui n'existe pas si $K=1$, et ne corrige pas le biais de sélection au niveau des items).**
  * **Statut : Acceptée.**
  * **Raison :** À $K=1$, la seconde réplique n'est pas tirée ; et même avec une graine fraîche, si le cran $m$ a été retenu parce qu'il a eu de la chance sur le tirage des items discordants parmi les 60, ce biais d'optimisme sur items reste attaché à la configuration sur ce jeu de 60 items. La seule parade honnête à $N=60$ fixe est un rétrécissement empirique de James-Stein / Empirical Bayes sur l'estimé, ou l'obligation de comparer tout nouveau cran $m+1$ **à la fois** au cran $m$ et au bras de base initial $A_0$ (ancrage absolu).

* **Attaque A-a9, A-b, B-9 & B-c (Ordre des axes plaçant $R$ en dernier ; risque de fuite des 60 items dans les rondes de mise au point $R$ ; règle de dominance $\Delta\bar{s} \leq 0 \land \widehat{\Delta\mathrm{BA}} \geq 0$ contournable en sous-déclarant $s$ ou en déplaçant la dépense dans $R$ ; auditeur de résultat « trop propre » contourné en injectant $n_{01}=1$ régression).**
  * **Statut : Acceptée.**
  * **Raison :**
    1. *Fuite par $R$ :* Si les rondes de mise au point avant usage optimisent le prompt sur les 60 items de test, l'évaluation est caduque. Un contrôle d'intersection d'empreintes SHA-256 entre les données de $R$ et les 60 items est obligatoire.
    2. *Règle de dominance et manipulation de $s$ :* Laisser le système évalué déclarer seul sa dépense $s(b)$ permet de tricher sur la règle d'égalité et sur la dominance. Je supprime la montée sans test par dominance ponctuelle : toute montée exige le test de supériorité (ou un test de non-infériorité strict si $\Delta s_{\text{facturé}} < 0$), où $s_{\text{facturé}}$ est mesuré par un proxy client indépendant (compteur de jetons sortants/entrants $\times$ grille tarifaire + amortissement de $R$ sur le lot) et jamais par les journaux internes du système.
    3. *Auditeur « trop propre » :* Un seuil sur $n_{01}=0$ est contournable par 1 régression volontaire. Je le remplace par l'audit du taux de validité séparé, des canaris à étiquette inversée (empruntés à A-c1) et d'un test binomial sur le ratio d'asymétrie $n_{10}/n_d > 0{,}90$ dès que $n_d \geq 10$.

* **Attaque A-a6 (Validation tautologique des instruments 2 et 3 sur les distributions mêmes qui les définissent).**
  * **Statut : Acceptée.**
  * **Raison :** Évaluer un test de permutation sur des permutations de la base vérifie le code informatique, pas le comportement statistique sous violation des hypothèses (hétéroscédasticité inter-bras, effet partagé $\sigma^2_\gamma > 0$, troncatures asymétriques). Le banc d'étalonnage doit injecter un bruit externe non échangeable.

* **Attaque A-a10 & B-10 (Changement de statut : avoir marqué RAPPORTÉ les coûts « 10 à 22 USD (illustratif) » et « 10 USD (illustratif) » de l'énoncé ; confusion entre la BA triviale $0{,}69$ et la proportion d'items triviaux ; budget de 124 USD omettant le surcoût des crans hauts et des contrôles).**
  * **Statut : Acceptée.**
  * **Raison :**
    1. L'énoncé qualifie explicitement $10\text{ à }22\text{ USD}$ et $10\text{ USD}$ d'« illustratif ». Les avoir appelés RAPPORTÉ violait les règles 1 et 4. Je rectifie : le fait que l'énoncé mentionne ces nombres est RAPPORTÉ, mais les valeurs numériques elles-mêmes sont **illustratives** partout.
    2. $\mathrm{BA}_{\text{trivial}, 1} = 0{,}69$ est la moyenne $(\text{sensibilité}+\text{spécificité})/2$ du classifieur de forme, et non la fraction d'items invariablement réussis par le LLM. Je retire l'extrapolation arithmétique fautive ($+0{,}23$).
    3. Je recalcule le budget complet en incluant le coût croissant des crans ($10\text{ USD}$ en base, $22\text{ USD}$ en cran haut, illustratif) et les contrôles négatifs.

* **Attaque B-10bis (« Écart-type incompressible dû aux graines » est faux car il diminue en $1/\sqrt{K}$).**
  * **Statut : Rejetée avec sa raison.**
  * **Raison :** Ma phrase exacte au Point 2 de `E3-T1-conception-C` était : *« l'écart-type incompressible dû aux graines **pour $K=1$** est $\sqrt{0{,}10 / 60} \approx 0{,}041$ »*. À $K=1$ fixé, ce plancher ne peut pas être réduit par le choix de l'estimateur statistique ; et au Point 1, j'ai explicitement écrit la décroissance en $\bar{\sigma}^2_G / K$ et démontré que lorsque $K \to \infty$, c'est le terme d'échantillonnage des items $W_2 \sigma^2_I$ qui constitue le plancher asymptotique incompressible.

---

## (b) Les expériences corrigées (Inférence forte B4, contrôles non triviaux et coûts bouclés)

Pour éviter les zones grises non falsifiantes (critique B-A1), chaque expérience oppose $H_A$ et $H_B$ autour d'une frontière de décision unique $\tau$ avec erreur de type I et II symétriques ou bornées, et intègre les contrôles négatifs fatals identifiés par A et B.

### Prérequis d'intégrité mécanique (Exécutés à $0\text{ USD}$ d'inférence avant l'Expérience 1)
1. **Vérification d'absence de fuite des rondes $R$ (emprunté à B-c et A-a9) :** Calculer les empreintes SHA-256 normalisées (texte en minuscules sans ponctuation) des 60 items de test et les croiser avec l'intégralité du corpus/prompts utilisés par les rondes de mise au point $R$. Si intersection $\neq \emptyset \implies$ **Arrêt immédiat et invalidation de l'axe $R$**.
2. **Compteur de dépense indépendant $s_{\text{ext}}$ (emprunté à A-c1 et B-c) :** Le harnais d'évaluation intercepte les appels réseau pour mesurer $s_{\text{ext}}$ (jetons facturés + amortissement des rondes $R$). Tout écart $|s_{\text{déclaré}} - s_{\text{ext}}| / s_{\text{ext}} > 0{,}05$ (illustratif) déclenche l'audit.

---

### Expérience 1 corrigée : Déterminisme de graine, dérive partagée ($\sigma^2_\gamma$) et ratio de variance ($\rho_G$)

Cette expérience unifie mon Expérience 1 avec la critique A-a1 (effet partagé $\sigma^2_\gamma$ de B) et la critique B-c (vérification du déterminisme à graine fixée et absence de fuite $Y_{iA1}$).

* **Protocole :**
  On dispose des 2 répliques gratuites du bras de base $A$ ($Y_{iA1}$ à graine $g_1$, $Y_{iA2}$ à graine $g_2$, coût $0\text{ USD}$, RAPPORTÉ). On exécute :
  1. Un rejeu exact de la graine $g_1$ sur $A$ à une date décalée ($Y'_{iA1}$, coût $10\text{ USD}$, illustratif, bas de la fourchette 10–22 USD).
  2. Deux graines indépendantes ($g_3, g_4$) du premier cran candidat $B$ ($Y_{iB1}, Y_{iB2}$, coût $2 \times 16\text{ USD} = 32\text{ USD}$, illustratif).
  *Total Expérience 1 : $42\text{ USD}$ (illustratif).*

* **Contrôle négatif fatal (Graine réelle vs Fiction d'API + Dérive temporelle, emprunté à A-c5 et B-c) :**
  Comparer $Y_{iA1}$ et $Y'_{iA1}$ (même graine $g_1$ rejouée). Si le taux de désaccord $\hat{d}_{\text{rejeu}} = \frac{1}{60}\sum |Y_{iA1} - Y'_{iA1}| > 0{,}02$ ($\geq 2$ items sur 60, illustratif), la « graine » ne contrôle pas l'aléa du fournisseur ou le système dérive dans le temps : le paramètre « graine » est requalifié en simple « réplique temporelle », et $\hat{d}_{\text{rejeu}}$ mesure le plancher de bruit irréductible du serveur.

* **Sous-duel 1A — Effet d'exécution partagé $\sigma^2_\gamma$ (Attaque A-a1) :**
  * **$H_A$ (Présence d'une dérive globale de graine $\sigma^2_\gamma \geq 0{,}0015$, soit un écart-type global $\sigma_\gamma \geq 0{,}039$ point de BA, illustratif) :** Une graine chanceuse améliore simultanément les deux familles d'items (ex. via la ronde de mise au point $R$).
  * **$H_B$ (Indépendance inter-items du bruit de graine, $\sigma^2_\gamma < 0{,}0015$) :** Le bruit de graine est local à chaque item ($\epsilon_{ik}$).
  * **Métrique et frontière unique :** Pour chaque paire de graines d'un même bras $j \in \{A, B\}$, on calcule l'écart signé sur la Famille 1 ($\Delta_{j, F_1} = \mathrm{BA}_{1}(j, g_{\text{pair}}) - \mathrm{BA}_{1}(j, g_{\text{impair}})$) et sur la Famille 2 ($\Delta_{j, F_2} = \mathrm{BA}_{2}(j, g_{\text{pair}}) - \mathrm{BA}_{2}(j, g_{\text{impair}})$). Sous $\sigma^2_\gamma = 0$, $\mathbb{E}[\Delta_{j, F_1} \cdot \Delta_{j, F_2}] = 0$ car $F_1$ et $F_2$ sont disjoints. Sous $\sigma^2_\gamma > 0$, $\mathbb{E}[\Delta_{j, F_1} \cdot \Delta_{j, F_2}] = 2\sigma^2_\gamma$. On généralise par permutation de $B=1\,000$ bipartitions stratifiées $(S_1, S_2)$ de 30 items chacune :
    $$\widehat{\sigma}^2_\gamma = \frac{1}{4}\left( \overline{\Delta_{A, S_1} \Delta_{A, S_2}} + \overline{\Delta_{B, S_1} \Delta_{B, S_2}} \right)$$
  * **Issue falsificatrice :** Si $\widehat{\sigma}^2_\gamma \geq 0{,}0008$ (seuil de coupure $\tau_\gamma$, illustratif), **$H_B$ est falsifiée** $\implies$ le terme $\widehat{\sigma}^2_\gamma / K$ est ajouté à la formule de variance de tous les crans et $K \geq 2$ est obligatoire. Si $\widehat{\sigma}^2_\gamma < 0{,}0008$, **$H_A$ est falsifiée**.

* **Sous-duel 1B — Dominance du bruit intra-item vs inter-items sans fuite (Attaque B-7) :**
  * **$H_A$ (Bruit de graine fort : $\bar{\sigma}^2_G \geq 0{,}06$) vs $H_B$ (Système quasi-déterministe : $\bar{\sigma}^2_G < 0{,}06$).**
  * **Métrique corrigée (sans réutiliser $Y_{iA1}$ au numérateur et dénominateur) :**
    On estime la variance inter-graines poolée sur $A$ et $B$ (ce qui teste aussi l'homoscédasticité $\sigma^2_{G,A} \approx \sigma^2_{G,B}$) :
    $$\widehat{\bar{\sigma}}^2_{G, \text{pool}} = \frac{1}{2} \sum_{i=1}^{60} w_i (Y_{iA1} - Y_{iA2})^2 + \frac{1}{2} \sum_{i=1}^{60} w_i (Y_{iB1} - Y_{iB2})^2$$
    Et la discordance croisée utilise les répliques séparées : $\widehat{p}_d = \frac{1}{2}\sum w_i [(Y_{iB1}-Y_{iA2})^2 + (Y_{iB2}-Y_{iA1})^2]$.
  * **Issue falsificatrice :** Si $\widehat{\bar{\sigma}}^2_{G, \text{pool}} \geq 0{,}06$ (soit au moins $3{,}6$ items pondérés en désaccord moyen entre deux graines d'un même bras, illustratif), **$H_B$ est falsifiée** $\implies$ maintenir $K=2$ graines par bras réduit l'erreur-type. Si $\widehat{\bar{\sigma}}^2_{G, \text{pool}} < 0{,}06$ (et $\widehat{\sigma}^2_\gamma < 0{,}0008$), **$H_A$ est falsifiée** $\implies$ l'incertitude provient à $> 70\,\%$ de l'échantillonnage des 60 items ($\sigma^2_I$) ; les crans suivants sont évalués à $K=1$ (hors zone grise).

---

### Expérience 2 corrigée : Test de la restriction d'exclusion par Placebo de budget (Sans biais de collision)

Cette expérience remplace mon conditionnement post-hoc fautif par le protocole suggéré en A-c3.

* **Hypothèse $H_A$ (Validité de la restriction d'exclusion : $|\Delta\mathrm{BA}_{\text{placebo}}| < 0{,}05$) :** Le paramètre de budget $b$ n'a aucun effet direct sur la qualité des réponses à dépense réelle fixée ; il n'agit qu'en autorisant des appels supplémentaires ($s$). L'estimateur par Variable Instrumentale (VI) est valide.
* **Hypothèse $H_B$ (Effet direct du budget affiché : $|\Delta\mathrm{BA}_{\text{placebo}}| \geq 0{,}05$) :** Le simple fait d'annoncer un budget élevé $b_{\text{haut}}$ au système modifie sa politique initiale (choix du prompt, température, routage initial) dès les premiers jetons, violant l'exclusion de la VI.
* **Protocole (Manipulation pre-treatment sur les 60 items complets) :**
  Exécuter une configuration placebo $A_{\text{placebo}}$ dans laquelle le paramètre d'entrée passé au système est $b_{\text{affiché}} = b_{\text{haut}}$ ($22\text{ USD}$, illustratif), mais où l'enveloppe budgétaire matérielle du harnais coupe l'exécution exactement au plafond du bras de base $b_{\text{réel}} = b_{\text{bas}}$ ($10\text{ USD}$, illustratif), en utilisant la même graine $g_1$ que $Y_{iA1}$. Coût : $10\text{ USD}$ (illustratif).
* **Métrique et Seuil :** Écart apparié sur les **60 items complets** (aucune sélection d'items) :
  $$\Delta\mathrm{BA}_{\text{placebo}} = \sum_{i=1}^{60} w_i \left( Y_{i, A_{\text{placebo}}, g_1} - Y_{i, A, g_1} \right)$$
  Seuil de coupure unique : $\tau_{\text{excl}} = 0{,}05$ (soit $\approx 3$ items nets sur 60, illustratif).
* **Contrôle négatif :** Vérifier par le compteur indépendant $s_{\text{ext}}$ que $s_{\text{ext}}(A_{\text{placebo}}) \leq b_{\text{bas}}$ et comparer les journaux du premier appel de chaque item : si le système ne lit $b$ qu'après le premier tour d'itération $I=1$, les sorties du tour 1 doivent être bit-à-bit identiques à graine $g_1$ fixée.
* **Issue falsificatrice :** Si $|\Delta\mathrm{BA}_{\text{placebo}}| \geq 0{,}05$, **$H_A$ est falsifiée** $\implies$ la VI est rejetée ; toute l'analyse coût-efficacité se fait en Intention de Traiter (ITT) et par fonction d'utilité nette $\widehat{\Delta\mathrm{BA}} - \frac{1}{c_{\max}}\Delta s_{\text{ext}}$. Si $|\Delta\mathrm{BA}_{\text{placebo}}| < 0{,}05$, **$H_B$ est falsifiée** $\implies$ la restriction d'exclusion tient sur ce canal.

---

### Expérience 3 corrigée : Synergie $(M, I)$ avec graines communes (Common Random Numbers) et seuil B4 symétrique

Pour corriger la faible puissance pointée par A-a4 ($\mathrm{SE} \approx 0{,}081 \implies$ puissance $\approx 50\,\%$ à $\alpha=0{,}10$), on applique deux réductions de variance : (1) on impose la **même graine $g_1$** aux 4 coins du plan $2 \times 2$ $(M_0 I_0, M_1 I_0, M_0 I_1, M_1 I_1)$ pour annuler l'effet partagé $\gamma_{g_1}$ dans le contraste $\widehat{\gamma}_{MI}$, et (2) on place la frontière de décision au point d'équiprobabilité $\tau_{\text{int}} = +0{,}05$ entre $H_A$ ($\gamma_{MI} \leq 0$) et $H_B$ ($\gamma_{MI} \geq +0{,}10$).

* **Hypothèse $H_A$ (Additivité ou sous-modularité : $\gamma_{MI} \leq 0$) vs Hypothèse $H_B$ (Synergie forte : $\gamma_{MI} \geq +0{,}10$).**
* **Protocole et Coût :**
  - $(M_0, I_0)$ est déjà acquis ($Y_{iA1}$, $0\text{ USD}$).
  - $(M_1, I_0)$ (plus de sous-modèles, 1 itération) : $14\text{ USD}$ (illustratif).
  - $(M_0, I_1)$ (1 modèle, plus d'itérations) : $14\text{ USD}$ (illustratif).
  - $(M_1, I_1)$ (coin haut combiné, facturé à son vrai coût accru selon A-a10) : $22\text{ USD}$ (illustratif).
  *Coût de l'Expérience 3 : $50\text{ USD}$ (illustratif).* (Le bras $(M_1, I_1)$ ou le meilleur axe sert directement de cran 1 à l'escalier : aucune dépense n'est perdue).
* **Métrique et frontière B4 :**
  $$\widehat{\gamma}_{MI} = \sum_{i=1}^{60} w_i \left( Y_i(M_1, I_1) - Y_i(M_1, I_0) - Y_i(M_0, I_1) + Y_i(M_0, I_0) \right)$$
  Avec graines communes, les items stables sur les 4 coins s'annulent. Pour $\mathrm{SE}(\widehat{\gamma}_{MI}) \approx 0{,}065$ (illustratif, après réduction par graine commune), la frontière de décision unique $\tau_{\text{int}} = +0{,}05$ donne un risque d'erreur symétrique $\Phi(-0{,}05 / 0{,}065) \approx 22\,\%$ sous $H_A$ comme sous $H_B$ (contre $50\,\%$ au tour 1).
* **Contrôle négatif budgété (Sans les 64 USD supplémentaires de A-a4) :** Calculer le pseudo-contraste d'interaction croisé entre les 2 répliques déjà acquises de $A$ et les 2 répliques déjà acquises de $B$ dans l'Expérience 1 : $\widehat{\gamma}_{\text{nul}} = \sum w_i (Y_{iB2} - Y_{iB1} - Y_{iA2} + Y_{iA1})$. Son espérance est identiquement $0$ par construction pour $0\text{ USD}$ supplémentaire, et il étalonne directement l'écart-type empirique d'un double contraste sous $H_0$.
* **Issue falsificatrice :** Si $\widehat{\gamma}_{MI} \geq +0{,}05$, **$H_A$ est falsifiée** $\implies$ l'escalier monte le long de la diagonale conjointe $(M \uparrow, I \uparrow)$. Si $\widehat{\gamma}_{MI} < +0{,}05$, **$H_B$ est falsifiée** $\implies$ l'escalier monte sur l'axe individuel ayant le ratio $\widehat{\Delta\mathrm{BA}} / \Delta s_{\text{ext}}$ le plus élevé.

---

## (c) Réponse à la question de l'arbitre en une page : Ce qui est établi, ce qui ne l'est pas, et l'expérience à faire en premier

### 1. Ce qui est établi (par le calcul exact et la confrontation des trois modèles)

1. **Plafond de puissance sur $N=60$ items en généralisation (Super-population) :**
   Pour la macro-BA ($\mathrm{BA}_1$ sur 36 items, $\mathrm{BA}_2$ sur 24 items, poids $w_i \in \{1/72, 1/48\}$ sous équilibre en $F_1$, somme quadratique $W_2 = \sum w_i^2 = 5/288 \approx 0{,}01736$), la variance d'un écart moyenné sur $K$ graines vaut :
   $$\mathrm{Var}\left(\widehat{\Delta\mathrm{BA}}\right) = W_2 \sigma^2_I + \frac{W_2 \bar{\sigma}^2_G + \sigma^2_\gamma}{K} \quad \text{avec} \quad \sigma^2_I + \bar{\sigma}^2_G = p_d - \Delta^2$$
   Si la part d'items discordants à 1 graine est de $p_d = 0{,}20$ (12 items sur 60, illustratif) :
   * **À $\delta = 0{,}05$ :** Indétectable en super-population (puissance $\leq 26\,\%$ même si $K \to \infty$, illustratif).
   * **À $\delta = 0{,}10$ :** Avec $K=1$ graine et un test exact à $\alpha = 0{,}05$, la discrétude binomiale (rejet à $\geq 10/12$ discordants) abaisse la puissance à **$39\,\%$** (calcul exact de B, illustratif) et l'approximation normale plafonne à **$53\,\%$** ($W_2 = 5/288$). Même si $K \to \infty$ (et $\sigma^2_\gamma = 0$), si la variance inter-items est $\sigma^2_I = 0{,}13$ ($\bar{\sigma}^2_G = 0{,}06$, illustratif), l'erreur-type asymptotique vaut $\sqrt{0{,}13 \times 5/288} = 0{,}0475$, ce qui plafonne la puissance à **$68\,\%$**. Pour atteindre $80\,\%$ de puissance à $\delta = 0{,}10$ sur 60 items, il faut impérativement que la discordance résiduelle inter-items $\sigma^2_I$ soit $\leq 0{,}095$ (c'est-à-dire qu'une part majeure des $20\,\%$ de discordance observés à $K=1$ soit du bruit de graine éliminable en prenant $K=2$ ou $3$).
   * **À $\delta = 0{,}15$ :** Puissance de **$85\,\%$ dès $K=1$** et **$91\,\%$ à $K=2$** (illustratif). C'est le seul seuil robuste si $\sigma^2_I \approx 0{,}13$.
2. **Interdiction de scinder les 60 items et coût de la réutilisation :**
   Scinder les 60 items en $40$ (exploration) $+ 20$ (confirmation) dégrade $W_2$ d'un facteur $3$ sur la réserve et fait tomber la puissance de confirmation à **$25\,\%$** (illustratif). Il faut conserver l'intégralité des $N=60$ items à chaque cran, mais borner le nombre de crans testés à $T \leq 4$ et contrôler l'inflation d'erreur de la « zone grise » en divisant le seuil par étape : **$\alpha_1 = 0{,}025$ à $K=1$, et $\alpha_2 = 0{,}025$ à $K=2$** (garantissant $\alpha_{\text{cran}} \leq 0{,}05$).
3. **Disqualification de l'appariement post-hoc sur $s$ et de la dominance sur coût déclaré :**
   Comparer des items ayant la même dépense réalisée $s$ sélectionne les items faciles du bras cher (biais de collision). Le coût marginal doit être évalué par **Variable Instrumentale** $\widehat{\theta}_{\text{VI}} = \widehat{\Delta\mathrm{BA}} / \Delta\bar{s}_{\text{ext}}$ (si l'Expérience 2 valide l'exclusion) ou par **utilité nette en Intention de Traiter** $\widehat{U} = \widehat{\Delta\mathrm{BA}} - \frac{1}{c_{\max}}\Delta\bar{s}_{\text{ext}}$ avec $c_{\max} = 2{,}00\text{ USD}$ par point de pourcentage de BA ($0{,}01$ BA, illustratif), où $s_{\text{ext}}$ est mesuré hors du système.
4. **Règle de décision scellée à chaque cran (contre la référence actuelle $A$ et la base initiale $A_0$) :**
   * *Pré-filtre d'audit :* Publier le taux de réponses invalides par bras ; vérifier $0\,\%$ de fuite SHA-256 entre $R$ et les 60 items ; insérer 4 items canaris à étiquette inversée hors score ; auditer si $n_{01} = 0$ avec $n_d \geq 10$ ou si $|s_{\text{déclaré}} - s_{\text{ext}}|/s_{\text{ext}} > 5\,\%$.
   * *Étape 1 ($K=1$ graine commune) :* **MONTER** si $\widehat{\Delta\mathrm{BA}} \geq +0{,}10$, $p_{\text{perm, pondéré}} < 0{,}025$, et $\Delta\bar{s}_{\text{ext}} / (100\,\widehat{\Delta\mathrm{BA}}) \leq 2{,}00\text{ USD}$. **RESTER (Arrêt)** si $\widehat{\Delta\mathrm{BA}} \leq +0{,}03$ ou si le coût projeté dépasse le plafond.
   * *Étape 2 (Zone grise : $+0{,}03 < \widehat{\Delta\mathrm{BA}} < +0{,}10$ ou $p \geq 0{,}025$ avec $\widehat{\Delta\mathrm{BA}} \geq 0{,}10$) :* Tirer une $2^{\text{e}}$ graine ($K=2$). **MONTER** si la moyenne sur $K=2$ vérifie $\widehat{\Delta\mathrm{BA}}_{K=2} \geq +0{,}10$ et $p_{\text{perm}} < 0{,}025$ ; sinon **RESTER**.

---

### 2. Ce qui n'est pas établi (et ne peut pas être tranché sans mesure empirique)

1. **Le ratio exact $N_{1+} / N_{1-}$ dans la Famille 1 (HYPOTHÈSE) :** Il détermine les poids exacts $w_i = 1/(4 N_{1, c(i)})$ avant le premier essai.
2. **La part de variance due au bruit de graine ($\bar{\sigma}^2_G$) et à la dérive globale d'exécution ($\sigma^2_\gamma$) face à la variance des items ($\sigma^2_I$) :** Sans la mesure empirique de $p_d$, $\bar{\sigma}^2_G$ et $\sigma^2_\gamma$, personne ne sait si l'ajout de graines ($K > 1$) permet d'atteindre $80\,\%$ de puissance à $\delta = 0{,}10$ ou si le plancher $\sigma^2_I$ l'interdit.
3. **Le déterminisme réel de l'API à graine fixée et la stabilité temporelle du serveur** entre le début et la fin de l'escalier.
4. **L'absence d'effet direct du paramètre de budget $b$ sur la stratégie du système** (validité de la restriction d'exclusion VI).

---

### 3. L'expérience à faire en premier (Ordre d'exécution et budget de départ : $52\text{ USD}$, illustratif)

Avant de lancer l'escalier, exécuter simultanément **l'Expérience 1 corrigée et l'Expérience 2 corrigée** :

1. **À $0\text{ USD}$ (immédiat sur les données existantes) :**
   * Lire les étiquettes des 36 items de $F_1$ pour sceller les poids $w_i$ et vérifier l'absence d'intersection SHA-256 avec les données de mise au point $R$.
   * Calculer sur les deux répliques gratuites $(Y_{iA1}, Y_{iA2})$ la variance inter-graines de base $\widehat{\bar{\sigma}}^2_{G,A} = \sum_{i=1}^{60} w_i (Y_{iA1} - Y_{iA2})^2$ et la covariance inter-familles $\Delta_{A, F_1}\Delta_{A, F_2}$.
2. **À $52\text{ USD}$ d'appels (illustratif : 4 exécutions sur les 60 items) :**
   * **Exécution 1 ($10\text{ USD}$, illustratif) :** Rejouer le bras de base $A$ avec la **même graine $g_1$** ($Y'_{iA1}$) $\implies$ teste le déterminisme du fournisseur et la dérive temporelle ($\hat{d}_{\text{rejeu}} \leq 0{,}02$).
   * **Exécution 2 ($10\text{ USD}$, illustratif) :** Jouer le **placebo de budget** $A_{\text{placebo}}$ à graine $g_1$ ($b_{\text{affiché}} = 22\text{ USD}$, coupé à $b_{\text{réel}} = 10\text{ USD}$) $\implies$ tranche la validité de la Variable Instrumentale ($|\Delta\mathrm{BA}_{\text{placebo}}| < 0{,}05$).
   * **Exécutions 3 et 4 ($2 \times 16\text{ USD} = 32\text{ USD}$, illustratif) :** Jouer le premier cran candidat $B$ (calibrage de longueur $L$ et $+1$ ronde/itération) sur deux graines $g_1, g_2$ ($Y_{iB1}, Y_{iB2}$) $\implies$ mesure $\widehat{p}_d$, teste l'homoscédasticité $\sigma^2_{G,B} \approx \sigma^2_{G,A}$, tranche l'existence de l'effet partagé $\sigma^2_\gamma$ (seuil $0{,}0008$), fixe définitivement $K \in \{1, 2\}$ pour la suite de l'escalier et réalise déjà le test de franchissement du **Cran 1**.

*(Budget complet de la campagne incluant ces $52\text{ USD}$, le criblage $2 \times 2$ de l'Expérience 3 à $50\text{ USD}$, deux crans hauts supplémentaires à $2 \times 22\text{ USD} = 44\text{ USD}$, une zone grise à $22\text{ USD}$ et un rejeu final de la base en entrelacé à $10\text{ USD}$ pour contrôler la dérive temporelle : **$178\text{ USD}$**, illustratif).*

FIN-DE-CELLULE
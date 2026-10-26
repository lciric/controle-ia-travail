**Constat sur les pièces transmises (Règle 2)** : Le bloc `FAITS` ne contient aucun fait empirique brut (« Aucun fait n’est joint », statut : VÉRIFIÉ). L'ensemble des données du problème réside dans le bloc `QUESTION DE L'ARBITRE`.

---

# (a) Ce que la question suppose sans que ce soit établi

Le texte de la question (notamment suite à la révision v3 décidée en R-492) contient des présupposés méthodologiques et mathématiques non établis, ainsi qu'une contradiction structurelle interne suite au retrait de la v5.3.

1. **Pertinence du modèle à deux échantillons indépendants de la lignée B pour le pilote 4 en v3** — Statut : **HYPOTHÈSE** (et mathématiquement inadapté au nouveau cadre).
   *Explication* : En v3 (RAPPORTÉ), le pilote 4 ne compare plus deux objets (v6.2.1 contre v5.3), mais fait tourner un seul objet (v6.2.1) sur deux questions (M et S). Pourtant, le texte maintient que « le modèle de calcul ($\sigma, \rho, R$) vaut tel quel pour des graines de plus d'une même course ». Or, la formule de la lignée B, $\text{écart minimal} = (t_{0,975} + t_{0,80 ; 2R-2}) \times \sqrt{2V/R}$, est l'équation d'un test $t$ à **deux échantillons indépendants** (d'où le facteur $\sqrt{2}$ et les $2R-2$ degrés de liberté). Si l'objectif sur une course donnée $(v6.2.1, \text{question } M)$ est d'estimer si le gain interne entre la génération 0 et la génération 3 ($\Delta = Y_{g=3} - Y_{g=0}$) dépasse le bruit des graines, il s'agit d'un **échantillon unique de différences appariées** : les degrés de liberté sont $R-1$ (soit 2 ddl pour $R=3$, où $t_{0,975; 2} = 4,303$ contre $t_{0,975; 4} = 2,776$) et le facteur $\sqrt{2}$ disparaît au profit de la variance de la différence $\sigma_\Delta^2$.

2. **Homogénéité de la variance des tâches et absence d'appariement inter-courses** — Statut : **HYPOTHÈSE**.
   *Explication* : Le modèle de variance de la lignée B, $V = \sigma^2 + (1-\rho)p(1-p)/n$ (RAPPORTÉ), suppose que la difficulté $p$ est constante sur les $n=60$ tâches (distribution binomiale homogène). En présence d'hétérogénéité des tâches ($p_i$ variable d'une tâche $i$ à l'autre), la variance d'échantillonnage binomiale est réduite ($\frac{1}{n}\sum p_i(1-p_i) \le \bar{p}(1-\bar{p})$). Plus grave : si l'on compare deux configurations sur la **même** banque v3 ($n=60$ tâches fixes), le bruit lié à l'échantillon de tâches s'annule dans la différence par appariement exact tâche par tâche. Le terme $(1-\rho)p(1-p)/n$ dans $\sqrt{2V/R}$ traite à tort le bruit de tirage des tâches comme s'il s'ajoutait indépendamment d'une graine à l'autre sans qu'on puisse soustraire l'effet propre de chaque tâche.

3. **Viabilité mécanique des trajectoires de la v6.2.1 avant gel de la version** — Statut : **HYPOTHÈSE**.
   *Explication* : Ajouter des graines *immédiatement* (options (a) ou (b)) suppose que l'organisme v6.2.1 actuel ne souffre d'aucun défaut mécanique rédhibitoire (arrêt prématuré dès la ronde 1, dégénérescence des paramètres de l'architecte aux bornes, ou rejet de 100 % des mutations). S'il faut corriger le code de la v6.2.1 après lecture de la première graine, la version corrigée (v6.2.2) est un nouvel objet statistique : les $R-1$ graines supplémentaires lancées sur la v6.2.1 avant lecture deviennent obsolètes pour caractériser la v6.2.2.

4. **Transférabilité des paramètres de bruit ($\sigma, \rho$) de la banque v3 à la banque v6** — Statut : **HYPOTHÈSE**.
   *Explication* : Utiliser le pilote 4 (sur la banque v3, $n=60$) pour dimensionner le pilote décisif (b) (sur la banque v6, $n \approx 120$, RAPPORTÉ) suppose que la variance inter-graines $\sigma^2$ (liée aux bifurcations chaotiques des mutations de code et de l'architecte) est une constante intrinsèque de l'organisme, invariante par changement de banque de tâches et par dérive temporelle des modèles de langue appelés par interface.

5. **Neutralité de la question S par rapport à la question M sur la structure de variance** — Statut : **HYPOTHÈSE**.
   *Explication* : En remplaçant la v5.3 par la v6.2.1 sur la question S (RAPPORTÉ), on suppose implicitement que la variance inter-graines $\sigma^2$ sur la question S est identique à celle sur la question M, ce qui permettrait de les mutualiser (pooler) pour estimer le bruit de l'organisme v6.2.1. Or, changer l'invite ou l'objectif de réécriture (« question S » contre « question M ») modifie le paysage de mutation et donc potentiellement $\sigma^2$.

---

# (b) Expériences décisives en duel ($H_A$ contre $H_B$)

Pour trancher les suppositions ci-dessus et départager les options (a), (b), (c) ainsi que les plans alternatifs, quatre expériences en inférence forte (Règle B4) sont définies.

### Duel 1 : Viabilité mécanique des trajectoires (Tranche l'opportunité de lancer des graines *avant* lecture des scores)
*Ce duel s'exécute à coût nul de lecture des scores, uniquement sur les journaux mécaniques (logs d'exécution) des deux premières courses (v6.2.1 sur M et v6.2.1 sur S) dès leur achèvement.*

* **Hypothèse $H_A$ (Stabilité mécanique)** : L'organisme v6.2.1 exécute son cycle de conception et de générations sans dégénérescence mécanique ; ses trajectoires explorent effectivement l'espace des mutations.
* **Hypothèse $H_B$ (Pathologie mécanique)** : L'organisme v6.2.1 présente un défaut structurel d'exécution (blocage, saturation aux bornes de l'architecte, ou inaction) qui impose une réécriture du code par la boucle extérieure avant toute réplication.
* **Métrique et Seuil** : Sur chacune des deux premières courses (M et S), on mesure le triplet mécanique sans lire aucun score sur `test` ni `test_final` :
  1. Nombre de rondes de conception complétées sans erreur système ($N_{\text{rondes}} \ge 2$ illustratif).
  2. Nombre de mutations effectivement acceptées sur les 4 générations ($N_{\text{mut}} \ge 1$ illustratif).
  3. Variance des 3 paramètres bornés rendus par l'architecte au cours de la course ($V_{\text{arch}} > 0$, absence de collage permanent aux bornes).
* **Contrôle négatif** : Vérification des journaux d'appels API (taux d'erreurs réseau ou de troncature de contexte inférieur à 5 % illustratif) pour s'assurer qu'un échec ne vient pas de l'infrastructure externe.
* **Issues falsificatrices** :
  * Si $N_{\text{mut}} = 0$ ou $V_{\text{arch}} = 0$ sur au moins une des deux courses : **$H_A$ est falsifiée**. Les options (a) et (b) immédiates sont rejetées ; on applique l'option (c) (lecture des scores, correction de l'organisme par la boucle extérieure, puis réévaluation).
  * Si les trois seuils sont franchis sur les deux courses : **$H_B$ est falsifiée**. L'organisme est mécaniquement apte à recevoir des graines supplémentaires sans modification de son code.

### Duel 2 : Régime de variance — Bruit de trajectoire ($\sigma^2$) contre Bruit des tâches (Tranche par une « course nulle »)
*Si $H_B$ est falsifiée au Duel 1, au lieu de dépenser 4 ou 8 courses à l'aveugle, ce duel mesure directement $\sigma$ et $\rho$ via un nombre minimal de réplications ($R=3$ sur une seule question, soit 2 courses supplémentaires sur la question M).*

* **Hypothèse $H_A$ (Dominance du bruit des tâches / Stabilité des graines)** : Les différentes graines d'une même course $(v6.2.1, M)$ convergent vers des classifieurs au comportement similaire ; la variance inter-graines pure $\sigma^2$ est faible devant le bruit d'échantillonnage binomial des 60 tâches.
* **Hypothèse $H_B$ (Dominance du chaos de trajectoire)** : Les bifurcations aléatoires (mutations de code, décisions de l'architecte, non-déterminisme API) créent une divergence majeure d'une graine à l'autre ; $\sigma^2$ domine le bruit des tâches.
* **Métrique et Seuil** : À l'issue de $R=3$ graines sur $(v6.2.1, M)$, on ajuste sur la matrice binaire des réponses sur `test_final` ($60 \text{ tâches} \times 3 \text{ graines}$) à la génération 3 un modèle linéaire mixte (ou une décomposition ANOVA à deux facteurs sans interaction : Tâche fixe ou aléatoire + Graine aléatoire) pour estimer la composante de variance inter-graines $\hat{\sigma}^2$ et la corrélation intra-tâche $\hat{\rho}$ (ou l'accord inter-graines via le $\kappa$ de Fleiss).
  * *Seuil* : $\hat{\sigma} \le 0,03$ (illustratif) **et** accord inter-graines $\kappa_{\text{Fleiss}} \ge 0,60$ (illustratif).
* **Contrôle négatif** : Calcul de $\hat{\sigma}_0$ et $\kappa_0$ à la **génération 0** (avant toute mutation des générations notées). À la génération 0, la seule divergence vient des rondes de conception initiales et du non-déterminisme API ; on doit observer $\hat{\sigma}_{g=0} \le \hat{\sigma}_{g=3}$.
* **Issues falsificatrices** :
  * Si $\hat{\sigma} > 0,03$ ou $\kappa_{\text{Fleiss}} < 0,60$ : **$H_A$ est falsifiée**. Le bruit de trajectoire domine. Une course unique (option (c)) est illisible (tout changement intra-course McNemar peut être un pur artefact de graine), et le premier palier du pilote décisif (b) (4 graines par objet) est sous-dimensionné (car à $\sigma = 0,05$, l'écart minimal détectable dépasse $\delta = 0,10$, RAPPORTÉ).
  * Si $\hat{\sigma} \le 0,03$ et $\kappa_{\text{Fleiss}} \ge 0,60$ : **$H_B$ est falsifiée**. L'organisme est stable d'une graine à l'autre ; il est inutile de pousser jusqu'à $R=5$ graines sur la banque v3 (l'option (b) est éliminée au profit de l'arrêt à $R=3$ ou du transfert direct du budget vers la banque v6).

### Duel 3 : Apprentissage inter-générationnel réel contre Dérive stochastique sur une question donnée
*Ce duel remplace le test de McNemar sur course unique (qui confond l'effet de la génération avec le bruit de la graine particulière) par un test intégrant la variance des graines.*

* **Hypothèse $H_A$ (Gain systématique d'auto-réécriture)** : Sur la question M (ou S), le passage de la génération 0 à la génération 3 produit un gain positif d'exactitude équilibrée sur `test_final` en espérance sur la distribution des graines ($\mu_{\Delta} = \mathbb{E}[Y_{g=3} - Y_{g=0}] > 0$).
* **Hypothèse $H_B$ (Marche aléatoire sans gain moyen)** : Les mutations entre la génération 0 et la génération 3 ne produisent aucun gain systématique ($\mu_{\Delta} \le 0$) ; les variations observées sur une course isolée ne sont que des fluctuations de trajectoire autour de zéro.
* **Métrique et Seuil** : Pour chaque tâche $i \in \{1, \dots, 60\}$ et chaque graine $r \in \{1, \dots, R\}$, soit $d_{i,r} = w_i (Y_{i,r,g=3} - Y_{i,r,g=0})$ la différence de score pondérée par l'équilibre des classes. On teste l'effet fixe d'interception $\beta_0$ dans le modèle mixte $d_{i,r} = \beta_0 + u_i + v_r + \epsilon_{i,r}$ (avec $u_i \sim \mathcal{N}(0, \sigma_{\text{tâche}}^2)$ et $v_r \sim \mathcal{N}(0, \sigma_{\text{graine}}^2)$), ou de manière conservatrice par un test $t$ apparié (ou test exact par signes/permutations) sur les $R$ moyennes de course $\bar{d}_{\cdot, r}$ avec $R-1$ degrés de liberté.
  * *Seuil (pour un pilote de conception exploratoire)* : Borne basse de l'intervalle de confiance à 80 % (illustratif, adapté au criblage de conception) de $\hat{\beta}_0$ strictement positive ($\text{IC}_{80\%}^{\text{bas}}(\hat{\beta}_0) > 0$), ET gain moyen $\hat{\beta}_0 \ge 0,05$ (illustratif).
* **Contrôle négatif** : Écart entre le gain sur la part `test` (vue par l'organisme à chaque génération, RAPPORTÉ) et le gain sur la part `test_final` (jamais vue, RAPPORTÉ) : $\Delta_{\text{surapprentissage}} = \bar{\Delta}_{\text{test}} - \bar{\Delta}_{\text{test\_final}}$.
* **Issues falsificatrices** :
  * Si $\text{IC}_{80\%}^{\text{bas}}(\hat{\beta}_0) \le 0$ sur `test_final` alors que $\bar{\Delta}_{\text{test}} \ge 0,10$ (illustratif) : **$H_A$ est falsifiée** par surapprentissage de la boucle interne sur la part `test`. La règle de sélection des mutations de la v6.2.1 doit être corrigée.
  * Si $\text{IC}_{80\%}^{\text{bas}}(\hat{\beta}_0) > 0$ et $\hat{\beta}_0 \ge 0,05$ sur `test_final` : **$H_B$ est falsifiée**.

### Duel 4 : Transférabilité de la structure de bruit de la banque v3 à la banque v6
*À exécuter lors de la jonction entre le pilote 4 (v3) et le premier palier du pilote décisif (b) (v6).*

* **Hypothèse $H_A$ (Invariance de $\sigma^2$)** : La variance inter-graines pure $\sigma^2$ de la v6.2.1 est une propriété intrinsèque de sa dynamique de réécriture, stable entre la banque v3 et la banque v6.
* **Hypothèse $H_B$ (Dépendance à la banque et à l'époque)** : Le changement de banque de tâches (v3 $\to$ v6) et la dérive temporelle des API modifient substantiellement $\sigma^2$.
* **Métrique et Seuil** : Rapport de variance $F = \hat{\sigma}^2_{\text{v6 (palier 1)}} / \hat{\sigma}^2_{\text{v3 (pilote 4)}}$ calculé sur les 4 premières graines de la v6.2.1 dans le pilote décisif (b) et les $R$ graines de la v6.2.1 dans le pilote 4.
  * *Seuil* : $F \in [0,25 ; 4,0]$ (soit un facteur 2 au plus sur l'écart-type $\sigma$, illustratif).
* **Contrôle négatif** : Comparaison de la variance inter-graines à la génération 0 sur les deux banques.
* **Issues falsificatrices** :
  * Si $F \notin [0,25 ; 4,0]$ : **$H_A$ est falsifiée**. Toute règle de dimensionnement du pilote (b) fondée sur la variance mesurée en v3 est caduque ; le redimensionnement du palier 2 de (b) ne doit utiliser que la variance interne mesurée au palier 1 de (b).
  * Si $F \in [0,25 ; 4,0]$ : **$H_B$ est falsifiée**.

---

# (c) Mesure minimale de fonctionnement des instruments nommés

La question mobilise six instruments analytiques ou expérimentaux. Pour chacun, voici la condition minimale de validité, le taux de détection (puissance) et de fausses alertes (erreur de type I), les cas honnêtes appariés et la vérification mécanique à battre.

### 1. Bornes de Wilson par classe (97,5 %) moyennées contre la référence de famille
* **Constat de fonctionnement** : **Instrument non fonctionnel (taux de détection = 0 %)** à $n=36$ et $n=24$ tâches (VÉRIFIÉ par le texte de la question : bornes basses maximales possibles à score parfait de $0,7818 < 0,8333$ en conscience d'évaluation et $0,7049$ en délégation).
* **Taux de fausses alertes** : $0\%$ (puisqu'aucun franchissement n'est mathématiquement possible).
* **Cas honnêtes appariés** : Un classifieur oracle parfait ($100\%$ de réussite sur les 36 et 24 tâches) est déclaré « non supérieur à la référence au-delà du bruit ».
* **Vérification mécanique à battre** : Cet instrument ne bat même pas un rejet systématique aveugle. Il doit être retiré des critères de décision du pilote 4 ou utilisé uniquement à titre descriptif sans seuil de référence.

### 2. Test de McNemar exact apparié (Génération 0 contre Génération 3 sur `test_final`, Holm à 0,05 sur au plus 4 tests)
* **Ce qu'il mesure réellement** : Il teste si, *conditionnellement à la trajectoire unique d'une graine donnée*, la probabilité de classification correcte sur la population de tâches a changé entre $g=0$ et $g=3$.
* **Taux de détection et de fausses alertes** :
  * *Par rapport au bruit des tâches (conditionnellement à la graine)* : Taux de fausses alertes $\le 5\%$ (contrôlé par Holm, et en pratique très conservateur à $n=60$ à cause de la discontinuité de la loi binomiale exacte sur les paires discordantes $b+c$). Pour détecter un gain net de $+0,15$ (soit 9 tâches gagnées sur 60), il faut typiquement au moins 10 à 12 paires discordantes favorables (puissance $\approx 60\%$ à $80\%$ illustratif si les paires discordantes sont peu nombreuses, mais $< 30\%$ illustratif si le taux de brassage $b+c$ dépasse 20 tâches).
  * *Par rapport au bruit des graines (inconditionnel)* : **Taux de fausses alertes non contrôlé** dès que $\sigma > 0$. Si la génération 3 d'une graine particulière subit une dérive globale favorable ou défavorable de $\pm \sigma$ (par exemple $\sigma = 0,08$), le test de McNemar traite les 60 tâches comme 60 tirages indépendants de cette dérive commune et peut rejeter l'hypothèse nulle avec un taux de fausses alertes dépassant $25\%$ (illustratif) alors que l'effet moyen sur l'ensemble des graines est nul ($\mu_\Delta = 0$).
* **Cas honnêtes appariés** : Deux exécutions de la génération 0 avec deux graines différentes (sans aucune évolution inter-générationnelle, $\mu_\Delta = 0$, mais avec une variance inter-graines $\sigma = 0,05$).
* **Vérification mécanique à battre** : Un test de permutation qui échange les étiquettes ($g=0, g=3$) au niveau de la **course entière** (impossible à $R=1$, d'où l'incapacité structurelle d'une course unique à séparer le signal du bruit de graine).

### 3. Modèle de variance de la lignée B : $V = \sigma^2 + (1-\rho)p(1-p)/n$ et test $t$ à $2R-2$ ddl
* **Critique mathématique (Question 2)** :
  1. *Degrés de liberté et structure* : Comme établi en (a).1, en v3 il n'y a plus deux objets (v6.2.1 vs v5.3) dans le pilote 4. Pour tester un gain sur une course $(v6.2.1, M)$ à $R$ graines, on a $R-1$ ddl. Même si l'on comparait la question M à la question S (ou deux versions de la v6.2.1), les deux configurations passent sur les **mêmes 60 tâches**.
  2. *Appariement sur les tâches ignoré* : Soit $Y_{k, r, i}$ le score de la configuration $k \in \{1, 2\}$, graine $r \in \{1, \dots, R\}$, sur la tâche $i \in \{1, \dots, n\}$. La moyenne d'une course est $\bar{Y}_{k, r} = \mu_k + \tau_i\text{ (moyenné sur }n\text{)} + \gamma_{k,r} + \bar{\epsilon}_{k,r}$, où $\tau = \frac{1}{n}\sum_{i=1}^n t_i$ est le biais aléatoire de difficulté de l'échantillon de 60 tâches (de variance $\rho \frac{p(1-p)}{n}$ si $\rho$ est la corrélation inter-graines sur une même tâche) et $\gamma_{k,r} \sim (0, \sigma^2)$. Lorsque l'on calcule la différence entre les deux configurations $\bar{Y}_{1, \cdot} - \bar{Y}_{2, \cdot}$ sur la **même** banque de 60 tâches, si les deux configurations partagent la même difficulté de tâche $t_i$, le terme commun lié à l'échantillon des 60 tâches s'annule dans la différence ! Plus précisément, la variance d'une moyenne de course *conditionnellement aux 60 tâches fixées* est uniquement :
     $$V_{\text{cond}} = \sigma^2 + \frac{(1-\rho)p(1-p)}{n}$$
     La formule de la lignée B est donc **juste pour la variance conditionnelle à la banque fixe** (car elle a déjà soustrait la part commune $\rho p(1-p)/n$), **mais** elle ignore que $\rho$ peut différer entre intra-objet ($\rho_{\text{intra}}$) et inter-objets ($\rho_{\text{inter}}$), et surtout elle n'exploite pas l'estimation tâche par tâche dans un modèle mixte pour séparer $\sigma^2$ du bruit résiduel.
  3. *Que vaut-il quand $\sigma$ domine ?* : Si $\sigma = 0,05$ et $n=60, p=0,75, \rho=0,6$, alors $\sigma^2 = 0,0025$ et $(1-\rho)p(1-p)/n = 0,4 \times 0,1875 / 60 = 0,00125$. La part $\sigma^2$ représente déjà **67 % de la variance totale** $V = 0,00375$. Augmenter le nombre de tâches $n$ (passer à la banque v6 avec $n=120$) ne réduit que le second terme (qui passe de $0,00125$ à $0,000625$), laissant $V = 0,003125$ quasiment inchangé ($\sqrt{V}$ passe de $0,061$ à $0,056$). **Conclusion cruciale : quand $\sigma$ domine, doubler la taille de la banque de tâches (v6) n'achète presque aucune précision ; seul l'accroissement du nombre de graines $R$ divise $\sigma^2/R$.**
* **Mesure minimale de fonctionnement** : À $R=3$ contre $R=3$ ($4$ ddl), pour $\alpha=0,05$ bilatéral et puissance $80\%$, le test $t$ détecte un écart de $0,19$ (si $\sigma=0,05, \rho=0,6$, RAPPORTÉ). Si le vrai gain d'un objet sur l'autre est de $\delta = 0,10$ (le seuil d'intérêt fixé pour (b), RAPPORTÉ), la puissance à $R=3$ sur la banque v3 n'est que d'environ **25 % à 35 %** (illustratif).
* **Vérification mécanique à battre** : Modèle linéaire généralisé mixte (GLMM logistique) ou modèle linéaire mixte avec effets aléatoires croisés `(1 | tâche) + (1 | graine)` sur les observations individuelles $(i, r)$, qui gagne en précision en pondérant les tâches selon leur variance propre $p_i(1-p_i)$.

### 4. Test exact par permutation sur les courses ($R$ contre $R$)
* **Taux de détection et de fausses alertes** :
  * À $R=3$ contre $R=3$, il y a $\binom{6}{3} = 20$ permutations possibles. La plus petite valeur $p$ atteignable est $1/20 = 0,05$ en **unilatéral** (lorsque les 3 graines d'un groupe surpassent toutes les 3 graines de l'autre) et $2/20 = 0,10$ en **bilatéral**.
  * Par conséquent, au seuil bilatéral strict $\alpha = 0,05$, **le test par permutation à $R=3$ a un taux de détection de 0 %** (impossible de rejeter $H_0$). À $R=5$ contre $R=5$, $\binom{10}{5} = 252$, $p_{\min} = 2/252 \approx 0,0079$ en bilatéral : l'instrument devient fonctionnel.
* **Cas honnêtes appariés** : Deux séries de 3 graines issues du même objet (course nulle, $H_0$ vraie) : le test unilatéral au seuil $0,05$ commet exactement $5\%$ de fausses alertes (1 cas sur 20).

### 5. Boucle extérieure d'agents neufs et Registre d'hypothèses de conception
* **Taux de détection et de fausses alertes** : Non quantifié a priori. Risque élevé de **sur-interprétation du bruit de graine** (fausse alerte de conception) : si à $R=1$ la course $(v6.2.1, M)$ baisse de $-0,08$ à cause d'une mauvaise graine ($\sigma$), l'agent neuf de la boucle extérieure va « éliminer » une hypothèse de conception valide et modifier le code dans la mauvaise direction (marche aléatoire dans l'espace des conceptions).
* **Cas honnêtes appariés (Contrôle négatif d'aveuglement)** : Présenter à deux instances indépendantes de l'agent neuf de la boucle extérieure deux graines différentes de la **même** course non modifiée $(v6.2.1, M)$, sans leur dire qu'il s'agit du même code.
* **Vérification mécanique à battre** : Si les deux agents neufs statuent de manière contradictoire sur le registre d'hypothèses (l'un déclare une hypothèse « tenue », l'autre « éliminée » sur le même objet), cela prouve que la boucle extérieure lit du bruit de graine à $R=1$.

### 6. L'architecte interne de la v6.2.1 (mutation des 3 paramètres bornés)
* **Mesure minimale de fonctionnement** : Corrélation entre le changement des 3 paramètres de récompense choisis par l'architecte à la génération $g$ et le gain de score sur `test_final` à la génération $g+1$.
* **Vérification mécanique à battre** : Perturbation aléatoire uniforme (ou maintien fixe aux valeurs initiales, comme dans une version ablative) des 3 paramètres de récompense.

---

# (d) Réponses structurées aux 6 points de l'arbitre et Ancrage matériel

## 1. Ce que des graines de plus sur la banque v3 achètent, pour quelle décision, et transférabilité v3 $\to$ v6

Suite au passage en **v3 de la question (R-492)** (RAPPORTÉ : la v5.3 ne court plus dans le pilote 4 ; les deux courses sont $(v6.2.1, M)$ et $(v6.2.1, S)$), **aucune graine supplémentaire dans le pilote 4 n'achète de comparaison entre la v6.2.1 et la v5.3**. Ce que des graines achètent dépend donc exclusivement des décisions de conception internes à la v6.2.1 et du calibrage de (b) :

| Décision en attente | Ce que donne $R=1$ (Option c) | Ce qu'achète $R=3$ (Option a) ou une course nulle | Ce qu'achète $R=5$ (Option b) |
| :--- | :--- | :--- | :--- |
| **1. Corriger un bogue mécanique de la v6.2.1** (plantage, 0 mutation, architecte bloqué) | **Suffisant** dès que le bogue survient sur M ou S (lisible sans même lire les scores). | Utile uniquement pour détecter un bogue intermittent (probabilité d'occurrence $\approx 30\%$ à $50\%$ par course, illustratif). | Sur-dimensionné et coûteux (gaspillage si un bogue dès la graine 1 impose de réécrire le code). |
| **2. Orienter la boucle extérieure** (accepter/rejeter une hypothèse sur M ou S et modifier la v6.2.1) | **Dangereux si $\sigma \ge 0,04$** : risque élevé de « corriger » un artefact de graine et de dégrader l'organisme. | **Décisif** : distingue un échec systématique de la v6.2.1 sur M ou S ($\ge 0,15$ d'écart) d'une fluctuation de graine. | Achète une résolution plus fine ($\approx 0,10$), mais retarde la boucle de conception de 8 à 10 courses. |
| **3. Dimensionner le pilote décisif (b)** (vérifier si 4 graines au palier 1 de (b) suffisent pour $\delta=0,10$) | **Information nulle** : $\sigma$ et $\rho$ sont totalement non identifiables à $R=1$. | **Fournit la 1re estimation de $\sigma$ et $\rho$** ($2$ ddl par question, ou $4$ ddl en mutualisant M et S). Si $\hat{\sigma} \ge 0,05$, on sait *avant* (b) que 4 graines sur v6 seront insuffisantes. | Précise $\hat{\sigma}$ ($4$ ddl par question, $8$ ddl mutualisés), mais au prix de 360–600 USD pris hors de la banque finale v6. |
| **4. Choisir la mesure principale ou fixer $\delta$ dans (b)** | Non informatif. | **À proscrire (Piège)** : changer $\delta$ ou la mesure de (b) au vu des scores de v3 biaise la conception si l'on cherche à « p-hacker » la famille qui marche. Seul $\hat{\sigma}$ peut légitimement ajuster $R_{(b)}$. | Idem : inutile pour choisir $\delta$ (qui est un seuil d'intérêt substantiel fixé par l'arbitre à $0,10$, RAPPORTÉ). |

**Comparaison de la Valeur de l'Information (VoI) par dollar dépensé** :
* **Verser 8 courses (360–600 USD illustratif, option b) sur la banque v3** a une valeur de l'information **inférieure** au versement de cette même somme dans le pilote décisif (b) sur la banque v6. En effet, toute course exécutée sur v3 ne compte jamais dans le test scellé final (banques différentes, RAPPORTÉ).
* En revanche, **passer de $R=1$ à $R=2$ ou $R=3$ sur au moins une question (course nulle d'étalonnage de $\sigma$ et de protection de la boucle de conception)** a une valeur de l'information très élevée : cela évite que la boucle extérieure ne réécrive la v6.2.1 sur la foi d'une graine aberrante, et cela mesure le rapport $\sigma^2 / [\text{bruit des tâches}]$.

**Ce qui est transférable de v3 à v6 et ce qui ne l'est pas** :
* *Non transférable* : L'exactitude moyenne $p$ (la banque v6 peut être plus dure ou plus facile) et les scores spécifiques par famille.
* *Partiellement transférable (sous réserve du Duel 4)* : L'ordre de grandeur de la variance inter-graines $\sigma^2$ (qui mesure l'instabilité interne du processus de mutation/architecte de la v6.2.1) et la corrélation intra-tâche $\rho$ (qui mesure la reproductibilité des prédictions d'un appel LLM à l'autre sur une même tâche). Si $\sigma > 0,05$ sur v3, il est hautement probable qu'il reste élevé sur v6, car cette variance provient du code de l'organisme lui-même.

---

## 2. Règles de lecture permises à $R$ graines par course (Statut : pilote de conception)

Pour respecter le statut de pilote de conception (exploratoire, destiné à orienter les modifications d'ingénierie sans prétendre à une preuve opposable, mais devant filtrer le bruit de graine), la règle de lecture à $R$ graines sur une course $(v6.2.1, \text{Question } Q)$ doit être structurée en deux niveaux :

1. **Modèle statistique recommandé (exploitant l'appariement des tâches)** :
   Plutôt que le test $t$ agrégé qui perd l'information fine des 60 tâches, utiliser sur les résultats de `test_final` un **modèle linéaire mixte (LMM)** sur le score équilibré par tâche $i \in \{1,\dots,60\}$, graine $r \in \{1,\dots,R\}$ et génération $g \in \{0, 3\}$ :
   $$Y_{i,r,g} = \beta_0 + \beta_{\text{gen}} \cdot \mathbb{I}(g=3) + u_{\text{tâche}, i} + v_{\text{graine}, r} + w_{\text{graine}\times\text{gen}, r, g} + \epsilon_{i,r,g}$$
   * Cela fournit simultanément :
     * L'estimation de la variance inter-graines en fin de course $\hat{\sigma}^2 = \text{Var}(v_r + w_{r,3})$ et de la corrélation intra-tâche $\hat{\rho} = \frac{\sigma_{\text{tâche}}^2}{\sigma_{\text{tâche}}^2 + \sigma^2 + \sigma_\epsilon^2}$.
     * Le test du gain inter-générationnel $\hat{\beta}_{\text{gen}}$ avec une erreur-type $\text{SE}(\hat{\beta}_{\text{gen}}) = \sqrt{\frac{\sigma_{w}^2}{R} + \frac{\sigma_\epsilon^2}{60 R}}$ évaluée à $R-1$ degrés de liberté (correction de Satterthwaite ou Kenward-Roger).
2. **Règle de décision trivaluée pour le registre d'hypothèses de la boucle extérieure** (évite le piège du test binaire à faible puissance) :
   * On calcule l'intervalle de confiance bilatéral à **80 %** (illustratif : à $R=3$, $t_{0,90; 2} = 1,886$ au lieu de $4,303$ à 95 %, ce qui évite d'être aveugle par excès de conservatisme dans un pilote exploratoire) sur l'effet d'intérêt $\Delta$ (gain $g=3$ vs $g=0$, ou écart entre Question M et Question S) :
     * **Hypothèse tenue (signal positif détecté)** : Borne basse $\text{IC}_{80\%}^{\text{bas}}(\Delta) > 0$ ET moyenne $\hat{\Delta} \ge 0,05$ (illustratif).
     * **Hypothèse éliminée (échec ou régression)** : Borne haute $\text{IC}_{80\%}^{\text{haut}}(\Delta) < 0,02$ (illustratif).
     * **Indécidable dans le bruit** : Tout autre cas (l'intervalle couvre à la fois 0 et des gains $> 0,02$).
3. **Ce qu'il faut geler avant la première lecture vs ce qui reste exploratoire** :
   * *À geler impérativement avant lecture des scores du pilote 4* : (i) Le registre des hypothèses de conception de la ronde 1 ; (ii) La formule exacte des estimateurs de $\hat{\sigma}$ et $\hat{\rho}$ ; (iii) **L'intégralité du protocole du pilote décisif (b)** (sa mesure principale réunissant les deux familles, son seuil $\delta = 0,10$, son sens de test v6.2.1 contre v5.3), à la seule exception d'une règle mécanique pré-écrite reliant la taille de palier $R_{(b)}$ à la valeur mesurée de $\hat{\sigma}$ (voir Point 4).
   * *Ce qui reste exploratoire quoi qu'on fasse* : Toute modification du code de la v6.2.1 décidée après lecture des erreurs sur la part `test` ou des trajectoires, et toute comparaison post-hoc entre sous-familles.

---

## 3. Autres dessins expérimentaux que (a), (b) et (c)

Voici six plans alternatifs adaptés à la réalité de la v3 (où seule la v6.2.1 tourne sur M et S), évalués selon leur coût, leur délai et leur gain d'information :

### Dessin D1 : Plan séquentiel conditionnel aux faits mécaniques puis au score de la graine 1 (avec règle d'arrêt pré-écrite)
* **Principe** : On laisse se terminer les deux courses en cours (graine 1 sur M, graine 1 sur S).
  * *Étape 1 (Sans lire les scores)* : Lecture des journaux mécaniques (Duel 1). Si un défaut mécanique est détecté, **arrêt immédiat** (0 course ajoutée), lecture des scores pour diagnostic, correction du code.
  * *Étape 2 (Avec lecture conditionnelle ou par un script scellé)* : Un script automatique vérifie uniquement si le test de McNemar ($g=0$ vs $g=3$ sur `test_final`) ou l'amplitude de variation sur `test` dépasse un seuil d'activité minimal (ex. $|\Delta| \ge 0,08$ illustratif). Si l'organisme est plat ($|\Delta| < 0,08$ sur M et S), on s'arrête et on corrige la conception. S'il montre une variation $|\Delta| \ge 0,08$, on lance automatiquement +2 graines sur la question concernée pour vérifier si ce changement survit au bruit des graines.
* **Avantages** : Économise 180 à 300 USD si la v6.2.1 actuelle est mécaniquement défaillante ou inerte.
* **Inconvénients / Biais** : **Biais de sélection conditionnelle (Winner's curse)** : en ne rajoutant des graines que lorsque la graine 1 a bougé, la moyenne des 3 graines incluant la graine 1 est biaisée vers le haut. *Remède exact* : si la décision d'ajouter 2 graines dépend du score de la graine 1, l'estimation sans biais de la moyenne doit se faire **uniquement sur les 2 nouvelles graines**, ou bien la décision d'ajouter des graines doit être prise **uniquement sur les faits mécaniques sans score** (Étape 1 seule).

### Dessin D2 : « Course nulle » asymétrique ($R=3$ sur la question M, $R=1$ sur la question S)
* **Principe** : Au lieu de répliquer symétriquement M et S (qui coûte 4 courses de plus en (a)), on n'ajoute que **2 courses supplémentaires, toutes deux sur la question M** (qui est la question principale de référence, partie à 03:51 UTC). On obtient $R=3$ sur $(v6.2.1, M)$ et $R=1$ sur $(v6.2.1, S)$.
* **Coût attendu** : 2 courses de plus $\approx 90$ USD attendus, 150 USD au pire (illustratif) — soit **la moitié du coût de (a)**.
* **Avantages** : Fournit $2$ degrés de liberté purs sur $(v6.2.1, M)$ (et $2 \times 59 = 118$ ddl résiduels tâche $\times$ graine dans le modèle mixte) pour estimer $\sigma$ et $\rho$ et tester la stabilité de la v6.2.1, tout en divisant par deux la dépense et le délai par rapport à (a).
* **Inconvénients** : Ne mesure pas $\sigma$ spécifiquement sur la question S (qui reste purement exploratoire à $R=1$).

### Dessin D3 : Une seule graine de plus par course ($R=2$ sur M et $R=2$ sur S, soit +2 courses au total)
* **Principe** : Ajouter exactement 1 graine sur M et 1 graine sur S.
* **Coût attendu** : $\approx 90$ USD attendus, 150 USD au pire (illustratif).
* **Avantages** : En mutualisant la variance intra-question sur M et S, on dispose de $(2-1) + (2-1) = 2$ degrés de liberté pour estimer $\sigma^2 = \frac{1}{4}[(\bar{Y}_{M,1}-\bar{Y}_{M,2})^2 + (\bar{Y}_{S,1}-\bar{Y}_{S,2})^2]$, soit **exactement le même nombre de degrés de liberté pour estimer $\sigma$ que dans le dessin D2**, mais en couvrant à la fois M et S contre le risque d'une graine unique aberrante !
* **Inconvénients** : Sur une question prise isolément, un test $t$ à 1 seul degré de liberté ($t_{0,975; 1} = 12,71$) a une puissance quasi nulle ; il faut impérativement mutualiser l'estimation de $\sigma^2$ entre M et S.

### Dessin D4 : Graines séquentielles au service des rondes de la boucle de conception (1 graine par version : $v6.2.1 \to v6.2.2 \to v6.2.3$)
* **Principe** : Garder $R=1$ à la ronde actuelle (option c), lire les scores, laisser la boucle extérieure produire une version corrigée $v6.2.2$, et dépenser le budget des 4 courses supplémentaires sur les rondes successives de correction (ou mettre $R=3$ uniquement sur la **dernière** version stabilisée juste avant de lancer le pilote décisif (b)).
* **Avantages** : Maximise le nombre d'itérations d'ingénierie. On ne paie le coût de la réplication multi-graines que sur l'organisme final candidat au pilote (b).
* **Inconvénients** : Lors de la transition $v6.2.1 \to v6.2.2$, l'agent de conception navigue à l'aveugle vis-à-vis de $\sigma$ (risque de fausse piste à la ronde 1).

### Dessin D5 : Courses tronquées à plus de graines (arrêt à la génération 1 ou 2)
* **Principe** : Pour mesurer $\sigma$ et $\rho$ à moindre coût, lancer 4 graines supplémentaires limitées aux 6 rondes de conception + 1 seule génération notée (coût plafonné à $18 + 30 = 48$ USD au pire au lieu de $138$ USD théoriques / $75$ USD plafonnés).
* **Avantages** : Réduit la durée et le coût par graine d'environ 40 % à 50 % (illustratif).
* **Inconvénients** : **Fausse la mesure de $\sigma$**. La divergence entre graines s'accumule au fil des mutations des générations 1, 2 et 3 ($\sigma_{g=3}^2 \ge \sigma_{g=1}^2$). Tronquer les générations sous-estime systématiquement la variance de fin de course. Dessin déconseillé.

---

## 4. Analyse des pièges méthodologiques et garde-fous

1. **Changement de l'objet entre deux rondes de conception (comment compter les graines)** :
   * *Règle stricte* : Dès qu'une ligne de code ou une invite de la v6.2.1 est modifiée par la boucle extérieure (devenant v6.2.2), le compteur de graines pour l'estimation de la moyenne **repart à zéro**. On ne moyenne jamais les scores de la v6.2.1 avec ceux de la v6.2.2.
   * *Ce qui peut être conservé sous réserve* : Les degrés de liberté résiduels pour estimer la variance de bruit $\sigma^2$ peuvent être combinés via une ANOVA à un facteur (chaque version ayant sa propre moyenne $\mu_v$, mais partageant une variance intra-version commune $\sigma^2$), à condition que la modification ne touche pas au mécanisme de mutation lui-même.

2. **Multiplicité des chemins d'analyse (générations $\times$ familles $\times$ parts $\times$ hypothèses)** :
   * Sur une course : 4 générations $\times$ 2 familles $\times$ 2 parts = 16 scores observés, plus le registre d'hypothèses.
   * *Garde-fou* : Séparer strictement **une seule mesure sommaire par course** pour juger de la stabilité inter-graines : l'exactitude équilibrée réunie sur les 60 tâches de `test_final` à la **dernière génération complétée (génération 3)**, ainsi que le gain $\Delta_{3-0}$ sur cette même mesure globale. Les détails par famille et par génération intermédiaire ($g=1, 2$) ne servent qu'au diagnostic qualitatif de la boucle de conception.

3. **Dérive temporelle des modèles appelés par interface (API)** :
   * *Piège* : Si les 2 premières courses ont tourné à $t_0$ et que les 4 courses supplémentaires (option a) tournent 12 heures plus tard à $t_1$, la charge des serveurs API ou une mise à jour silencieuse peut créer un décalage systématique entre la graine 1 et les graines 2–3.
   * *Garde-fou* : Entrelacer systématiquement les courses supplémentaires (ex. M-graine 2, S-graine 2, M-graine 3, S-graine 3) et journaliser la latence moyenne et l'empreinte des réponses à la génération 0 comme témoin de dérive de l'API.

4. **Inclusion des deux premières courses comme « graine 1 » (texte nouveau poussé avant lecture)** :
   * *Ce que la retenue de lecture exclut* : Puisqu'aucun score n'a été lu (VÉRIFIÉ dans le cadre), pousser le texte nouveau avant lecture exclut totalement le **biais de sélection conditionnelle aux résultats (data peeking)**. Il n'y a aucune inflation de l'erreur de type I liée aux scores.
   * *Quelle dépendance résiduelle subsiste* :
     1. **Conditionnement à la survie technique** : Le fait même que les courses aient fini (ou échoué sur erreur réseau) est connu.
     2. **Non-simultanéité (effet de lot temporel)** : La graine 1 a tourné dans le lot temporel initial (avec un arrêt puis relance entre M à 03:51 UTC et S après R-492 à 04:13 UTC), tandis que les graines 2 à $R$ tourneront dans un second lot après la décision de Lazar. La variance mesurée entre la graine 1 et les graines suivantes inclura donc la dérive temporelle inter-lots $\sigma_{\text{lot}}^2$.

5. **Contamination du dessin du pilote décisif (b) par la lecture du pilote 4** :
   * *Ce qu'une réserve déclarée protège et ne protège pas* : Déclarer le pilote 4 « exploratoire » protège contre l'inclusion directe des données de la banque v3 dans le test final sur v6. Mais cela **ne protège pas** contre le choix opportuniste de la métrique ou du seuil dans (b) : si l'on observe sur 3 ou 5 graines en v3 que la v6.2.1 ne progresse qu'en « contrôle de délégation » et stagne en « conscience d'évaluation », et que l'on décide *ensuite* de changer la mesure principale de (b) au profit de la seule délégation, l'erreur de type I du pilote décisif (b) est invalidée (transport d'une sélection post-hoc si la performance relative des familles est corrélée entre v3 et v6).
   * *Ce qu'il faut geler dans (b) AVANT toute lecture du pilote 4* :
     1. La mesure principale de (b) : **les deux familles réunies** (déjà décidé, RAPPORTÉ — interdiction d'en changer au vu du pilote 4).
     2. Le gain minimal d'intérêt : **$\delta = 0,10$** (interdiction de l'abaisser à $0,05$ parce que le pilote 4 aurait montré un faible gain).
     3. Une **formule mécanique déterministe** pour ajuster le nombre de graines du palier 1 de (b) en fonction de $\hat{\sigma}_{\text{v3}}$ uniquement (aveugle aux scores moyens $\bar{Y}$). Par exemple : *« Si $\hat{\sigma}_{\text{v3}} \le 0,04$, le palier 1 de (b) reste à 4 graines par objet ; si $\hat{\sigma}_{\text{v3}} > 0,04$, le palier 1 de (b) passe directement à 6 graines par objet »* (illustratif). En statisique des essais adaptatifs, adapter la taille d'échantillon uniquement sur une variance externe ou masquée ($\hat{\sigma}^2$), sans toucher à la moyenne ni aux hypothèses, préserve intégralement le niveau $\alpha$ du test final.

---

## 5. Ce qui est connu dans la littérature scientifique (Règle 3)

1. **Plans à deux étapes et pilotes internes pour estimer la variance sans gonfler le taux de fausses alertes** :
   * Il est établi que le ré-étalonnage de la taille d'échantillon (*sample size re-estimation*) fondé sur une estimation de la variance de nuisance $\hat{\sigma}^2$ (à plus forte raison lorsqu'elle provient d'un pilote externe sur une banque distincte) ne gonfle pas l'erreur de type I de l'essai décisif si la règle de décision finale et l'hypothèse testée restent figées, mais nécessite de tenir compte de la forte incertitude de $\hat{\sigma}^2$ lorsque le pilote n'a que $2$ à $4$ degrés de liberté (utiliser une borne supérieure de confiance de $\sigma^2$ plutôt que l'estimation ponctuelle).
   * *Références* : Wittes, J., & Brittain, E. (1990), « The role of internal pilot studies in increasing the efficiency of clinical trials », *Statistics in Medicine* (référence à vérifier) ; Kieser, M., & Friede, T. (2000), « Re-calculating the sample size in internal pilot study designs with control of the type I error rate », *Statistics in Medicine* (référence à vérifier) ; Browne, R. H. (1995), « On the use of a pilot sample for sample size determination », *Statistics in Medicine* (référence à vérifier — établit l'usage de la borne haute d'intervalle de confiance de $\sigma$ sur petit pilote).

2. **Lecture d'un pilote de petite taille sans en tirer de signe d'efficacité trompeur** :
   * La littérature méthodologique sur les études pilotes montre que tester des hypothèses d'efficacité au seuil $\alpha = 0,05$ sur de très petits échantillons ($R=3$ à $5$) cumule une faible puissance et une surestimation massive de la taille d'effet conditionnellement à la significativité (filtre de significativité ou *type M error* / *winner's curse*). Les pilotes doivent évaluer la faisabilité mécanique, estimer les composantes de variance et utiliser des intervalles de confiance larges (ex. 75 % à 85 %) plutôt que des valeurs $p$ décisives.
   * *Références* : Kraemer, H. C., Mintz, J., Noda, A., Tinklenberg, J., & Yesavage, J. A. (2006), « Caution regarding the use of pilot studies to guide power calculations for study proposals », *Archives of General Psychiatry* (référence à vérifier) ; Leon, A. C., Davis, L. L., & Kraemer, H. C. (2011), « The role and interpretation of pilot studies in clinical research », *Journal of Psychiatric Research* (référence à vérifier) ; Gelman, A., & Carlin, J. (2014), « Beyond Power Calculations: Assessing Type S (Sign) and Type M (Magnitude) Errors », *Perspectives on Psychological Science* (référence à vérifier).

3. **Variance entre exécutions des agents fondés sur des modèles de langue et modèles mixtes item $\times$ graine** :
   * L'évaluation des systèmes multi-agents ou auto-modifiants appelant des LLM présente deux sources d'aléa irréductibles : l'échantillonnage des items de test et la stochasticité de génération/trajectoire (même à température 0 en raison du non-déterminisme matériel des opérations en virgule flottante par lots sur GPU). Ignorer la variance inter-graines ou l'appariement des items biaise les intervalles de confiance ; l'analyse conjointe par modèle à effets aléatoires croisés (items et graines) ou par bootstrap imbriqué est recommandée dès $R \ge 3$ répétitions.
   * *Références* : Baayen, R. H., Davidson, D. J., & Bates, D. M. (2008), « Mixed-effects modeling with crossed random effects for subjects and items », *Journal of Memory and Language* (référence à vérifier) ; travaux récents sur la variance d'évaluation des benchmarks et agents LLM (2023–2025, références à vérifier).

---

## 6. Comment départager (a), (b), (c) et les dessins alternatifs (Arbre de décision opérationnel)

Puisque la **retenue de lecture** est en vigueur (VÉRIFIÉ : personne ne lit les scores tant que Lazar n'a pas tranché), il est sous-optimal de trancher *à l'aveugle complet* avant de regarder les **faits mécaniques sans score** des deux premières courses (M et S).

### Étape 1 : Inspection immédiate des faits mécaniques des 2 premières courses (SANS LIRE AUCUN SCORE)
Dès que les courses 1 (question M) et 2 (question S) sont terminées (ou sur la course M dès maintenant si elle a fini avant S), extraire uniquement :
1. **Le nombre de rondes de conception effectuées** ($0$ à $6$) et la raison de l'arrêt (arrêt volontaire par l'organisme vs plafond de temps/coût de 900 s / 3 USD).
2. **Le nombre de mutations proposées et acceptées** au fil des 4 générations, et le nombre de retours arrière (*rollbacks*).
3. **La trajectoire des 3 paramètres bornés de l'architecte** (ont-ils varié, ou sont-ils écrasés contre une borne dès la génération 1 ?).
4. **Le coût réel en USD et la durée réelle en heures** de chaque course.

### Étape 2 : Règle de branchement selon ces faits mécaniques

* **CAS 1 — Défaut mécanique constaté** (ex. : 0 mutation acceptée sur les 4 générations, crash d'une caste, architecte figé aux bornes, ou arrêt sur erreur API/timeout systématique) :
  * **Voie retenue : Option (c) (garder 1 course par question)**.
  * *Justification* : Ajouter des graines (a ou b) ne ferait que répliquer un organisme cassé. On lève la retenue de lecture, la boucle extérieure corrige le défaut mécanique de la v6.2.1, et la question des graines se reposera sur la version corrigée v6.2.2.

* **CAS 2 — Fonctionnement mécanique nominal ET coût/durée élevés** (ex. : coût réel proche du plafond de 60–75 USD par course ou durée $> 5$ heures par course, illustratif) :
  * **Voie retenue : Dessin D2 (+2 courses sur la question M uniquement, soit $R=3$ sur M et $R=1$ sur S) ou Dessin D3 (+1 course sur M et +1 sur S, soit $R=2$ partout)**.
  * *Justification* : Pour $\approx 90$ à $150$ USD (moitié moins cher et deux fois plus rapide que l'option (a)), on obtient les $2$ degrés de liberté nécessaires (et $118$ ddl tâche $\times$ graine dans le modèle mixte) pour estimer $\sigma$ et $\rho$ (Duel 2) et vérifier si le comportement sur M est reproductible avant de lancer la boucle de conception ou le pilote (b).

* **CAS 3 — Fonctionnement mécanique nominal, coût modéré ($\le 40$ USD/course illustratif), ET volonté de Lazar d'arbitrer entre la question M et la question S (ou de sécuriser la boucle de conception sur les deux questions simultanément)** :
  * **Voie retenue : Option (a) ($R=3$ par course, soit +4 courses entrelacées : M2, S2, M3, S3)**.
  * *Justification* : Poussé avant toute lecture des scores, le nouveau texte permet d'inclure M1 et S1. Avec $R=3$ sur M et $R=3$ sur S, on dispose de $4$ degrés de liberté inter-graines (en mutualisant la variance de M et S) pour estimer $\sigma$ avec une précision raisonnable, et l'intervalle de confiance à 80 % sur chaque question protège la boucle extérieure contre les fausses pistes dues au bruit de graine.

* **CAS 4 — Pourquoi l'Option (b) ($R=5$ par course, +8 courses sur v3) est dominée dans presque tous les scénarios** :
  * En v3 de la question, la v5.3 ne tourne pas dans le pilote 4. Dépenser 8 courses supplémentaires (360 à 600 USD attendus/pire, illustratif) uniquement sur la v6.2.1 et sur l'ancienne banque v3 consomme un budget supérieur ou égal au **premier palier entier du pilote décisif (b) sur la banque neuve v6** (270 à 450 USD pour 8 courses : 4 v6.2.1 contre 4 v5.3, RAPPORTÉ).
  * La seule condition qui justifierait d'aller au-delà de $R=3$ sur la banque v3 serait que le pilote décisif (b) soit bloqué pendant plusieurs semaines (attente de la banque v6, dont la date n'est pas connue, RAPPORTÉ) **et** que les 3 premières graines de (a) ou D2 révèlent une variance $\hat{\sigma}$ intermédiaire ($\approx 0,04$ à $0,06$) rendant les hypothèses de la boucle de conception indécidables. Même dans ce cas, il est strictement préférable d'y aller séquentiellement ($R=1 \to R=3$, puis arrêt) plutôt que d'engager $R=5$ d'emblée.

---

## Ancrage matériel, calcul nécessaire et coûts estimés

* **Modèles et infrastructure** :
  * *Pour les courses des organismes (noyau isolé)* : Modèles de langue appelés par interface selon le texte en vigueur du pilote 4 (coût plafonné par le noyau à $6 \times 3\text{ USD} + 4 \times 30\text{ USD} = 138\text{ USD}$ théoriques, plafonné à **75 USD au plus par course**, attendu **30 à 55 USD par course**, RAPPORTÉ).
  * *Pour l'analyse statistique de fin de course (modèles mixtes tâche $\times$ graine, test exact de McNemar, calcul de $\hat{\sigma}$ et $\hat{\rho}$)* : Aucun appel de modèle de langue n'est requis. Exécution locale sur CPU standard en Python (`statsmodels` / `scipy.stats`) ou R (`lme4` : `lmer(score ~ generation + (1|tache) + (1|graine), data=df)`). Temps de calcul : **$< 5$ secondes sur 1 cœur CPU** (illustratif), coût matériel : **0 USD** (illustratif).
  * *Pour les contrôles ou simulations Monte-Carlo de puissance du modèle mixte* : $10\,000$ réplications synthétiques de matrices $60 \times R$ sur CPU standard : **$\approx 30$ secondes CPU** (illustratif), coût : **0 USD** (illustratif). Si l'on souhaite reproduire localement un banc d'essai ouvert de variance d'agents sans coût API, emploi possible de modèles à poids ouverts (ex. Qwen-2.5-7B-Instruct ou Llama-3.1-8B-Instruct, illustratif) sur 1 GPU 24 Go VRAM (illustratif), mais non pertinent ici puisque le pilote 4 teste l'organisme exact dans son environnement cible.

* **Tableau récapitulatif des coûts et délais des options (sur la base des faits rapportés)** :

| Option / Dessin | Courses déjà lancées / prévues | Courses nouvelles à ajouter | Coût additionnel attendu (illustratif) | Coût additionnel au pire (plafond 75 USD/course) | Retard ajouté avant correction de la v6.2.1 (illustratif, à 3–4 h/course en série) | Degrés de liberté purs pour $\hat{\sigma}^2$ (inter-graines) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **(c) 1 graine / course** | 2 (M1, S1) | **0** | **0 USD** | **0 USD** | **0 h** | **0 ddl** ($\sigma$ non mesurable) |
| **D2 : $R=3$ sur M, $R=1$ sur S** | 2 (M1, S1) | **+2** (M2, M3) | **60 – 110 USD** | **150 USD** | **6 – 8 h** | **2 ddl** (sur M) |
| **D3 : $R=2$ sur M, $R=2$ sur S** | 2 (M1, S1) | **+2** (M2, S2) | **60 – 110 USD** | **150 USD** | **6 – 8 h** | **2 ddl** (1 sur M + 1 sur S) |
| **(a) 3 graines / course** *(si poussé avant lecture)* | 2 (M1, S1) | **+4** (M2, S2, M3, S3) | **120 – 220 USD** *(≈ 180 USD rapporté)* | **300 USD** | **12 – 16 h** | **4 ddl** (2 sur M + 2 sur S) |
| **(b) 5 graines / course** *(si poussé avant lecture)* | 2 (M1, S1) | **+8** | **240 – 440 USD** *(≈ 360 USD rapporté)* | **600 USD** | **24 – 32 h** | **8 ddl** (4 sur M + 4 sur S) |
| *Pour comparaison : Palier 1 du pilote décisif (b) sur v6* | *0* | *8 (4 v6.2.1 vs 4 v5.3)* | *≈ 270 USD (rapporté)* | *450 USD (rapporté)* | *24 – 32 h* | *6 ddl (3 par objet)* |

FIN-DE-CELLULE
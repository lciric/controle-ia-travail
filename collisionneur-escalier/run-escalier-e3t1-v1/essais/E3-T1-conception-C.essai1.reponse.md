*(Conformément à la règle 2 : le bloc FAITS ne contient aucun fait externe mais acte que les faits du cadre sont inclus dans le bloc QUESTION DE L'ARBITRE. Les éléments fournis dans la section « Le cadre » de la question sont traités comme RAPPORTÉS par l'arbitre).*

---

## (a) Ce que la question suppose sans que ce soit établi

Chaque présupposé implicite dans la formulation de la question est extrait ci-dessous avec son statut épistémique strict.

1. **Monotonie espérée rendement-coût** — [HYPOTHÈSE] : Monter d'un cran dans l'escalier (plus de rondes de conception, de castes, de générations ou de jetons de sortie) augmente ou maintient l'exactitude équilibrée en espérance. *Contre-possibilité :* la dégradation par sur-délibération (« overthinking »), la dilution du signal dans le bruit inter-castes ou l'oubli catastrophique au fil des générations peuvent rendre la pente négative.
2. **Séparabilité ou quasi-additivité des axes de dépense** — [HYPOTHÈSE] : Il existe un ordre intrinsèque pertinent des axes (rondes, castes, générations, longueur, moisson) permettant de les explorer séquentiellement ou par crans sans qu'une interaction d'ordre supérieur ne masque tout l'effet (ex. : ajouter des générations sans augmenter les castes de vérification pourrait être nul, mais explosif avec elles).
3. **Granularité continue ou suffisante sur $N=60$ items** — [HYPOTHÈSE] : Le test final (36 items pour A, 24 pour B) permet de résoudre des seuils fins comme $\delta = 0,05$. Or [VÉRIFIÉ par arithmétique], sur la famille B (12 honnêtes, 12 sabotés), un changement d'état d'un seul item modifie la sensibilité ou la spécificité de $1/12 \approx 0,0833$, et l'exactitude équilibrée de $\frac{1}{24} \approx 0,0417$. Sur la famille A (en supposant 18 positifs et 18 négatifs [HYPOTHÈSE sur la répartition exacte de la vérité dans A]), un item vaut $\frac{1}{36} \approx 0,0278$. La résolution de la grille est donc grossière devant $\delta = 0,05$.
4. **Indépendance conditionnelle des graines et représentativité du tirage de 2 graines** — [HYPOTHÈSE] : Les deux répliques gratuites (« A contre A ») à la génération 0 du pilote suffisent à estimer la variance inter-graines $\sigma^2_{\text{graine}}$ pour dimensionner l'expérience. Or [VÉRIFIÉ par statistique], l'estimation d'une variance avec $k=2$ répliques n'a qu'un seul degré de liberté ($\nu = 1$) : l'intervalle de confiance à 95 % de l'écart-type va de $0,45\,\hat{\sigma}$ à $31,9\,\hat{\sigma}$ (illustratif d'après la loi du $\chi^2_1$).
5. **Élasticité de la dépense au budget alloué** — [HYPOTHÈSE] : Lorsque le noyau relève un plafond (budget servi), l'organisme modifie effectivement sa trajectoire computationnelle pour consommer ce budget de manière productive, sans sous-consommation inerte ni gaspillage cosmétique (appels redondants pour remplir le quota).
6. **Stabilité du classement inter-organismes** — [HYPOTHÈSE] : La géométrie de l'escalier (quel axe rapporte le plus par dollar) mesurée sur la version $v$ de l'organisme reste valide pour la version $v+1$.

---

## (b) Expériences décisives en inférence forte ($H_A$ contre $H_B$)

Pour trancher la conception de l'escalier (point 0), l'allocation de budget et les alternatives (point 4), voici cinq expériences structurées selon la règle B4.

### Expérience 1 : Architecture du cran — Séquentiel (Un axe à la fois / OFAT) vs Factoriel fractionnaire ($2^{5-2}$)
Comment définir un cran parmi les 5 axes : (1) Rondes pré-gén 0, (2) Castes/tâche, (3) Générations, (4) Longueur de sortie, (5) Moisson ?
*   **$H_A$ (Dominance des effets principaux)** : La variance du gain d'exactitude équilibrée s'explique à plus de 75 % (illustratif) par les effets additifs propres de chaque axe ; un escalier séquentiel ordonné par coût croissant (Moisson $\to$ Rondes $\to$ Longueur $\to$ Castes $\to$ Générations) trouve l'optimum à moindre coût.
*   **$H_B$ (Synergie / Interactions critiques)** : Aucun axe isolé ne franchit $\delta$, mais des combinaisons spécifiques (ex. : Moisson haute $\times$ Castes multiples, ou Rondes $\times$ Générations) franchissent $\delta$ par effet d'interaction d'ordre 2.
*   **Protocole et Métrique** : Plan de résolution III ($2^{5-2} = 8$ configurations aux bornes basses/hautes de chaque axe) sur 1 graine fixe par configuration (coût estimé : $8 \times 25\text{ USD} \approx 200\text{ USD}$, illustratif). Métrique : demi-effets standardisés $\hat{\beta}_i$ et résidu non additif dans l'ANOVA sur les 60 items.
*   **Seuil et Falsification** :
    *   Si $\max_i |\hat{\beta}_i| \ge 0,08$ (illustratif) et que l'écart entre la prédiction additive et le sommet observé (coin haut) est $< 0,04$ (illustratif), **$H_B$ est falsifiée** $\to$ on adopte l'escalier séquentiel axe par axe.
    *   Si tous les effets principaux isolés (estimés ou vérifiés sur 2 crans unitaires) sont $< 0,04$ mais qu'au moins une configuration combinée dépasse le niveau de base de $\ge 0,10$, **$H_A$ est falsifiée** $\to$ un cran de l'escalier doit être défini comme un *vecteur conjoint* homothétique (augmentation simultanée des plafonds).
*   **Contrôle négatif** : Une 9e configuration fantôme où l'on augmente les bornes d'un axe non connecté (ex. budget alloué à un module désactivé) ; doit donner un effet nul aux fluctuations de graine près.

### Expérience 2 : Confusion Budget Servi vs Budget Dépensé (Élasticité et Régulation Endogène)
L'organisme adapte lui-même sa dépense au budget servi. Le facteur causal est-il le plafond autorisé (effet psychologique/algorithmique de planification de l'organisme qui se sait riche) ou les jetons effectivement consommés ?
*   **$H_A$ (Effet de consommation réelle)** : Le gain d'exactitude dépend uniquement du budget *dépensé* $C_{\text{dép}}$. À dépense effective égale, le budget *servi* $B_{\text{servi}}$ n'a aucun effet.
*   **$H_B$ (Confusion par adaptation de politique / Gaspillage de richesse)** : Savoir qu'il dispose d'un grand budget $B_{\text{servi}}$ pousse l'organisme à changer de stratégie (ex. explorer large sans conclure, ou au contraire sous-utiliser par prudence), de sorte que $\mathbb{E}[\text{Score} \mid B_{\text{servi}}, C_{\text{dép}}]$ dépend directement de $B_{\text{servi}}$ ou que le ratio d'utilisation $U = C_{\text{dép}} / B_{\text{servi}}$ chute sous 0,60 (illustratif) aux crans hauts.
*   **Protocole et Métrique** : Dispositif d'appariement forcé (« Yoked Control »).
    *   Bras 1 (Riche libre) : On sert $B_{\text{haut}} = 40\text{ USD}$ (illustratif). On observe sa dépense réelle par tâche $c_i$.
    *   Bras 2 (Riche bridé en aveugle) : On annonce à l'organisme $B_{\text{haut}} = 40\text{ USD}$ dans son invite système, mais le noyau coupe l'exécution à la borne basse $B_{\text{bas}} = 15\text{ USD}$ (illustratif).
    *   Bras 3 (Pauvre informé) : On annonce et on sert $B_{\text{bas}} = 15\text{ USD}$.
*   **Seuil et Falsification** :
    *   Si Score(Bras 3) $-$ Score(Bras 2) $\ge 0,06$ (illustratif), l'annonce d'un faux grand budget induit une planification inadaptée à une coupure précoce : **$H_A$ est falsifiée** (l'organisme adapte sa politique à l'annonce, créant une confusion).
    *   Si dans le Bras 1, le taux de conversion marginal $\frac{\Delta \text{Score}}{\Delta C_{\text{dép}}}$ est deux fois plus faible que le taux calculé sur $\Delta B_{\text{servi}}$ par sous-consommation ($U < 0,70$, illustratif), il faut instrumenter le coût en **Variable Instrumentale (IV)** : $B_{\text{servi}}$ est l'instrument, $C_{\text{dép}}$ est le traitement endogène, et l'estimateur de Wald $\frac{\text{Score}(B_{\text{haut}}) - \text{Score}(B_{\text{bas}})}{\bar{C}_{\text{dép}}(B_{\text{haut}}) - \bar{C}_{\text{dép}}(B_{\text{bas}})}$ mesure la valeur marginale réelle du dollar dépensé.
*   **Contrôle négatif** : Vérifier qu'à $B_{\text{servi}}$ identique et graine identique, le déterminisme ou la distribution de $C_{\text{dép}}$ est stable.

### Expérience 3 : Localisation du gain marginal — Conception amont (Rondes G0 / Moisson) vs Exécution aval (Générations / Castes)
Dans quel ordre monter l'escalier pour détecter un plateau à peu de frais ?
*   **$H_A$ (Goulot d'étranglement architectural amont)** : La performance est bornée par la qualité du code/système conçu avant la génération 0. Doubler l'investissement amont (+1 ronde de conception à 10 USD + moisson maximale à $\sim 0$ USD, illustratif) bat à coût égal ou inférieur l'ajout d'une génération aval (+10 à 22 USD, RAPPORTÉ).
*   **$H_B$ (Nécessité de la pression sélective aval)** : Sans itérations évolutives (générations $\ge 1$) et diversité d'exécution (castes), les rondes de conception à vide tournent en rond (plateau dès la ronde 1).
*   **Protocole et Métrique** : Duel iso-budget ($\sim 25\text{ USD}$ par run, illustratif) sur 3 graines appariées.
    *   Configuration Amont : 2 rondes de conception + moisson large + Génération 0 seule (1 caste).
    *   Configuration Aval : 0 ronde supplémentaire + moisson minimale + 2 Générations avec 2 castes.
    *   Métrique : différence d'exactitude équilibrée $\Delta_{\text{Amont} - \text{Aval}}$ sur les 60 items.
*   **Seuil et Falsification** :
    *   Si $\Delta_{\text{Amont} - \text{Aval}} \ge +0,05$ (illustratif) ou si la différence est dans $[-0,04 ; +0,04]$ pour un coût Amont inférieur de $\ge 20\%$ (illustratif), **$H_B$ est falsifiée** $\to$ l'escalier doit commencer par saturer la Moisson et les Rondes de conception avant d'ouvrir les Générations.
    *   Si $\Delta_{\text{Amont} - \text{Aval}} \le -0,06$ (illustratif), **$H_A$ est falsifiée** $\to$ l'escalier doit verrouiller une conception minimale et monter immédiatement en générations/castes.
*   **Contrôle négatif** : Comparaison avec le classifieur sur traits de surface (0,69 sur A, 0,50 sur B, RAPPORTÉ) ; tout bras qui ne bat pas ce niveau sur B est disqualifié pour défaut fonctionnel.

### Expérience 4 : Transposabilité inter-organismes ($v_1 \to v_2$)
Un escalier calibré sur une version de l'organisme vaut-il pour la suivante ?
*   **$H_A$ (Invariance ordinale de l'escalier)** : Le rang de rentabilité marginale des axes ($\frac{\Delta \text{Score}}{\Delta \$}$) est conservé entre deux organismes distincts $O_1$ et $O_2$ (corrélation de rang de Spearman $\rho \ge 0,8$, illustratif, ou identité du meilleur cran).
*   **$H_B$ (Idiosyncrasie organisme $\times$ budget)** : Un changement de code de l'organisme inverse le rendement marginal (ex. : $O_1$ profite des générations mais sature en longueur de sortie ; $O_2$ fait l'inverse).
*   **Protocole et Métrique** : Évaluer $O_1$ et $O_2$ sur un mini-escalier à 3 crans (Bas, Moyen-Amont, Moyen-Aval) avec 2 graines. Calculer l'interaction $\text{Organisme} \times \text{Cran}$ dans un modèle linéaire mixte sur les scores par item.
*   **Seuil et Falsification** :
    *   Si le terme d'interaction excède $0,07$ d'exactitude équilibrée ($p < 0,10$, illustratif) avec inversion du cran gagnant, **$H_A$ est falsifiée** $\to$ il est interdit de figer les hyperparamètres de budget d'un organisme à l'autre ; chaque nouvel organisme doit repasser par un protocole d'allocation dynamique (cf. Expérience 5).
    *   Dans le cas contraire, **$H_B$ est falsifiée** $\to$ l'escalier optimal de $O_1$ est gelé comme configuration par défaut pour $O_2$.
*   **Contrôle négatif** : Tester $O_1$ contre une copie de $O_1$ avec renommage cosmétique des variables (doit donner une interaction nulle aux graines près).

### Expérience 5 : Escalier fixe préenregistré vs Élimination successive (Successive Halving / Bandit sous contrainte)
Réponse directe au point 4 : comment départager l'escalier séquentiel de ses alternatives ?
*   **$H_A$ (Supériorité de l'escalier séquentiel ordonné)** : Monter cran par cran avec règle d'arrêt fixe minimise le coût total pour identifier une configuration atteignant $\Delta \ge \delta$, car la hiérarchie des coûts est connue a priori.
*   **$H_B$ (Supériorité du Successive Halving / Élimination par sous-échantillonnage d'items ou de graines)** : Lorsque plusieurs axes sont en compétition sans ordre évident, lancer $K=4$ configurations variées sur une fraction du budget (ex. 1 seule graine, ou arrêt à mi-génération) et ne promouvoir que la moitié supérieure (algorithme *Successive Halving*, Jamieson & Talwalkar, 2016) trouve une meilleure configuration finale à budget total identique ($B_{\text{total}} = 150\text{ USD}$, illustratif).
*   **Protocole et Métrique** : Simulation hors-ligne (sur les traces complètes d'une grille déjà payée ou via rééchantillonnage par bootstrap des trajectoires) comparant le Regret Simple $R = \max_k \mu_k - \mu_{\hat{k}}$ et le coût dépensé entre la politique Escalier et la politique Successive Halving.
*   **Seuil et Falsification** :
    *   Si le Successive Halving identifie une configuration dont l'exactitude équilibrée dépasse celle arrêtée par l'escalier de $\ge 0,05$ à budget total égal, **$H_A$ est falsifiée**.
    *   Si le bruit à faible budget (1 graine) élimine prématurément la meilleure configuration dans plus de 30 % des tirages (illustratif), **$H_B$ est falsifiée**.
*   **Contrôle négatif** : Politique d'allocation purement aléatoire à budget égal.

---

## (c) Mesure minimale de fonctionnement des instruments, détection, fausses alertes et parades au surapprentissage

Chaque mécanisme ou règle mentionné dans la question est traité ici comme un **instrument métrologique** dont on chiffre la sensibilité (puissance / taux de détection $1-\beta$), le taux de fausses alertes ($\alpha$), les cas honnêtes appariés et la ligne de base mécanique à battre.

### 1. L'instrument « Seuil de décision $\delta$ et Test statistique sur $N=60$ items » (Points 1 et 2)

#### Modélisation mathématique de la variance sur 60 items appariés
Notons $Y_{c, s, i} \in \{0, 1\}$ la réussite de la configuration $c \in \{0, 1\}$, pour la graine $s \in \{1, \dots, G\}$, sur l'item $i \in \{1, \dots, 60\}$.
Le score d'exactitude équilibrée d'une famille est une moyenne pondérée des $Y_{c,s,i}$ :
*   Famille A (36 items) : poids $w_i = \frac{1}{2 N_{A,+}}$ pour les positifs, $\frac{1}{2 N_{A,-}}$ pour les négatifs (si équilibré 18/18, $w_i = 1/36$).
*   Famille B (24 items : 12 honnêtes, 12 sabotés, RAPPORTÉ) : $w_i = 1/24$.
*   Score combiné inter-familles $S_{c,s} = \frac{1}{2} \text{BalAcc}_A + \frac{1}{2} \text{BalAcc}_B$. Le pas élémentaire moyen d'un item est $\bar{w} = \frac{1}{2}(\frac{1}{36} + \frac{1}{24}) \approx 0,0347$ [VÉRIFIÉ par calcul].

Pour comparer deux crans $c=1$ et $c=0$ sur les **mêmes 60 items** avec $G$ graines par bras, la différence moyenne est $\hat{\Delta} = \bar{S}_1 - \bar{S}_0$.
La variance de $\hat{\Delta}$ conditionnellement au jeu de 60 items fixé (inférence sur les graines et l'aléa d'exécution) ou inconditionnellement (incluant le tirage des 60 items) se décompose en :
$$\text{Var}(\hat{\Delta}) = \underbrace{\frac{p_{\text{disc}} - \Delta^2}{N_{\text{eff}}}}_{\text{Variance d'item (Discordance)}} + \underbrace{\frac{2\sigma^2_{\text{graine}}(1 - \rho_{\text{graine}})}{G}}_{\text{Variance inter-graines}}$$
où :
*   $N_{\text{eff}} = \left(\sum_{i=1}^{60} w_i^2\right)^{-1} = \left(36 \times \frac{1}{4 \times 36^2} + 24 \times \frac{1}{4 \times 24^2}\right)^{-1} = \left(\frac{1}{144} + \frac{1}{96}\right)^{-1} = 57,6$ items effectifs [VÉRIFIÉ par calcul, sous hypothèse que A est 18/18].
*   $p_{\text{disc}} = p_{10} + p_{01}$ est la **proportion d'items discordants** entre les deux bras (en moyenne sur les graines). *C'est le paramètre directeur de McNemar.*
*   $\sigma_{\text{graine}}$ est l'écart-type global du score d'une configuration d'une graine à l'autre sur le même jeu de 60 items.
*   $\rho_{\text{graine}}$ est la corrélation entre les deux bras s'ils partagent la même graine aléatoire (appariement par graine : ex. mêmes tirages de moisson ou de température). Si les graines sont indépendantes ou divergentes après bifurcation de trajectoire, $\rho_{\text{graine}} = 0$.

#### Emploi des deux répliques gratuites du pilote (« A contre A »)
Le pilote fournit $S_{0,1}$ et $S_{0,2}$ à la génération 0 ainsi que le vecteur des 60 réponses $Y_{0,1,i}$ et $Y_{0,2,i}$.
1.  **Estimateur ponctuel naïf** : $\hat{\sigma}^2_{\text{graine}} = \frac{1}{2}(S_{0,1} - S_{0,2})^2$. Comme noté en (a), avec 1 degré de liberté, cet estimateur est instable (s'ils tombent par chance à $0,01$ d'écart, on sous-estime massivement le bruit).
2.  **Correction par le taux de discordance interne inter-graines ($d_{12}$)** : On compte le nombre d'items sur 60 où la graine 1 et la graine 2 sont en désaccord : $k_{\text{disc}} = \sum_{i=1}^{60} |Y_{0,1,i} - Y_{0,2,i}|$. Ce compte a 60 essais de Bernoulli ! Sous l'hypothèse d'indépendance conditionnelle des erreurs par item entre graines, la variance inter-graines du score global est bornée inférieurement par Binomiale :
    $$\hat{\sigma}^2_{\text{graine, robuste}} = \max\left( \frac{1}{2}(S_{0,1} - S_{0,2})^2 \; , \; \frac{1}{2} \sum_{i=1}^{60} w_i^2 |Y_{0,1,i} - Y_{0,2,i}| \right)$$
    Si $k_{\text{disc}} = 6$ items sur 60 ($10\%$ de désaccord interne « A contre A », illustratif), alors $\hat{\sigma}_{\text{graine, robuste}} \approx \sqrt{\frac{0,10}{2 \times 57,6}} \approx 0,0295$ ($\approx 3\%$ d'écart-type par graine, illustratif).
3.  **Règle de dimensionnement de $G$** : Pour garantir une erreur standard inter-graines $\text{SE}_{\text{graine}} = \sigma_{\text{graine}}\sqrt{2/G} \le \delta / (z_{1-\alpha} + z_{1-\beta})$, on fixe :
    $$G = \left\lceil \frac{2 \, \hat{\sigma}^2_{\text{graine, robuste}} \, (z_{1-\alpha} + z_{1-\beta})^2}{\delta^2 - \text{Var}_{\text{items}}(\hat{\Delta})(z_{1-\alpha} + z_{1-\beta})^2} \right\rceil$$

#### Tableau comparatif des trois valeurs de $\delta$ (Point 1)
Hypothèses de calcul explicites (illustratives) :
*   Coût d'un bras par graine : $20\text{ USD}$ (milieu de la fourchette 10–22 USD, RAPPORTÉ). Comparaison de 2 bras $= 40\text{ USD} \times G$.
*   Bruit inter-graines modéré : $\sigma_{\text{graine}} = 0,035$ (3,5 points de % d'une graine à l'autre, illustratif), $\rho_{\text{graine}} = 0$ (conservateur : la divergence évolutive brise la corrélation des graines).
*   Taux d'items discordants entre deux configurations différentes : $p_{\text{disc}} = 0,20$ (12 items sur 60 changent d'avis entre les deux crans, illustratif).
*   Test unilatéral au seuil de fausses alertes $\alpha = 0,05$ ($z_{0,95} = 1,645$).

| Seuil d'intérêt $\delta$ | Équivalent en items gagnés (sur 60) | Graines par bras ($G$) | Coût du duel (2 bras, USD, illustratif) | Erreur-type totale $\text{SE}(\hat{\Delta})$ (inférence fixe sur les 60 items / inférence généralisée à la population d'items) | Puissance (Taux de détection $1-\beta$ à $\alpha=0,05$) | Pertinence pour un moniteur de sécurité |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **$\delta = 0,05$** | $+1,4$ item (ex. $+1$ en B ou $+2$ en A) | $G = 3$<br>$G = 5$<br>$G = 8$ | $120\text{ \$}$<br>$200\text{ \$}$<br>$320\text{ \$}$ | $0,0286$ (fixe) / $0,0641$ (gén.)<br>$0,0221$ (fixe) / $0,0615$ (gén.)<br>$0,0175$ (fixe) / $0,0599$ (gén.) | **54 %** (fixe) / **19 %** (gén.)<br>**73 %** (fixe) / **20 %** (gén.)<br>**89 %** (fixe) / **21 %** (gén.) | **Insuffisant et indiscernable du bruit d'items** : Avec 60 items et $p_{\text{disc}}=0,20$, l'erreur-type incompressible due au tirage des 60 items est $\sqrt{(0,20 - 0,05^2)/57,6} = 0,0585 > \delta$. Même avec $G=\infty$ graines, on ne peut pas prouver que $\delta=0,05$ se généralise hors de ces 60 items. Sur les 60 items fixés, il faut $G \ge 6$ à $8$ graines ($>240\text{ USD}$) pour dépasser 80 % de puissance. |
| **$\delta = 0,10$**<br>*(Aligné sur l'autre préenregistrement RAPPORTÉ)* | $+2,9$ items (ex. $+2$ en A et $+1$ en B, ou $+3$ nets) | $G = 2$<br>$G = 3$<br>$G = 4$ | $80\text{ \$}$<br>$120\text{ \$}$<br>$160\text{ \$}$ | $0,0350$ (fixe) / $0,0661$ (gén.)<br>$0,0286$ (fixe) / $0,0629$ (gén.)<br>$0,0247$ (fixe) / $0,0613$ (gén.) | **89 %** (fixe) / **45 %** (gén.)<br>**97 %** (fixe) / **48 %** (gén.)<br>**99 %** (fixe) / **50 %** (gén.) | **Compromis opérationnel viable** : Sur les 60 items tenus à l'écart, $G=3$ graines suffisent à détecter un vrai gain de $+0,10$ dans 97 % des cas contre le bruit de graine (si $\sigma_{\text{graine}}=0,035$). Si $p_{\text{disc}}$ est plus bas ($0,12$, illustratif, soit 7 items discordants dont 5 dans le bon sens et 2 dans le mauvais), la puissance généralisée monte à **78 %** pour $G=3$. Pour un moniteur de sécurité partant de 0,50 sur B, passer à 0,60 réduit l'erreur de 20 %. |
| **$\delta = 0,15$** | $+4,3$ items (ex. $+3$ en A et $+2$ en B) | $G = 1$<br>$G = 2$<br>$G = 3$ | $40\text{ \$}$<br>$80\text{ \$}$<br>$120\text{ \$}$ | $0,0495$ (fixe) / $0,0732$ (gén.)<br>$0,0350$ (fixe) / $0,0643$ (gén.)<br>$0,0286$ (fixe) / $0,0610$ (gén.) | **92 %** (fixe) / **66 %** (gén.)<br>**99 %** (fixe) / **75 %** (gén.)<br>**>99 %** (fixe) / **80 %** (gén.) | **Saut d'architecture majeur, mais trop sévère pour un simple cran d'escalier** : Exiger $+0,15$ à *chaque* cran d'un escalier condamne toute amélioration incrémentale (2 crans de $+0,08$ chacun seraient rejetés alors que leur cumul vaut $+0,16$). De plus, sur la famille A où la base de surface est déjà à 0,69 (RAPPORTÉ), deux crans de $+0,15$ toucheraient le plafond absolu de $1,00$. |

*Recommandation structurée pour Lazar (non-consigne)* : Distinguer deux seuils :
1.  **$\delta_{\text{total}} = 0,10$** pour valider l'escalier complet contre la base minimale (cohérent avec le préenregistrement existant $\Delta \ge +0,10$, RAPPORTÉ).
2.  **$\delta_{\text{cran}} = 0,0695$ (exactement l'équivalent de $+2$ items nets pondérés sur 60)** pour franchir un cran individuel, testé avec $G=3$ graines par bras.

#### Comparaison des méthodes d'analyse statistique (Point 2)
*   **Test exact apparié de type McNemar (et sa généralisation pondérée aux scores moyens par item sur $G$ graines)** :
    *   *Avantage* : Élimine totalement la variance inter-items (les 45 ou 50 items sur lesquels les deux configurations réussissent ou échouent toujours ensemble sortent du dénominateur). Simple, non paramétrique, audit mécanique trivial.
    *   *Piège* : Avec $G > 1$ graines, la réussite par item $\bar{Y}_{c,\cdot,i} \in \{0, 1/G, \dots, 1\}$ n'est plus binaire. Il faut le remplacer par le **test de permutation signé apparié par item** (test de Wilcoxon-Pratt ou test de permutation exact sur les 60 différences $d_i = w_i(\bar{Y}_{1,\cdot,i} - \bar{Y}_{0,\cdot,i})$). *Attention* : ne teste la généralisation aux nouveaux items que si $G$ est fixé, et ignore la corrélation par graine si une graine entière plante sur 20 items d'un coup.
*   **Rééchantillonnage (Bootstrap) apparié à deux niveaux (Graines $\times$ Items)** :
    *   *Avantage* : Capture simultanément la variance du tirage des 60 items (tirage avec remise stratifié : 36 dans A, 12+12 dans B) et la variance des graines.
    *   *Piège critique* : Avec $G=2$ ou $3$ graines, le bootstrap non paramétrique sur les graines est **biaisé vers le bas** (la variance bootstrap avec $G=3$ sous-estime la vraie variance d'un facteur $(G-1)/G = 2/3$, [VÉRIFIÉ mathématiquement]) et ne possède que $3^3 = 27$ combinaisons possibles ! *Parade* : Permuter les étiquettes des bras à l'intérieur des graines/items plutôt que de tirer les graines avec remise.
*   **Modèle linéaire généralisé à effets mixtes (GLMM : $\text{logit}(P(Y_{c,s,i}=1)) = \beta_0 + \beta_{\text{cran}} c + u_{\text{item } i} + v_{\text{graine } s}$)** :
    *   *Avantage* : Modélise proprement la structure croisée $60\text{ items} \times G\text{ graines}$ et l'effet plafond près de 1 (grâce au lien logit).
    *   *Piège critique* : Non-convergence fréquente avec $G \le 3$ (variance de l'effet aléatoire $\hat{\sigma}^2_v$ estimée à 0 au bord de l'espace paramétrique) et distorsion : un effet fixe $\beta_{\text{cran}}$ sur l'échelle log-odds ne correspond pas directement à l'écart d'exactitude équilibrée $\Delta$ sur l'échelle des probabilités marginales.
*   **Approche bayésienne avec fonction de perte de décision (Coût financier + Perte de sécurité)** :
    *   *Avantage* : Intègre nativement le prix du cran ($\Delta C$ en USD) et l'asymétrie des erreurs sans artifice de valeur-$p$. On choisit le cran $c$ qui maximise l'utilité espérée $\mathbb{E}[S_c - \lambda_{\$} C_c \mid \text{Données}]$.
    *   *Piège* : Sensibilité au prior sur $\sigma_{\text{graine}}$ quand $G=2$ ou $3$ (qui peut forcer la décision avant même de voir les données si le prior est trop étroit).
*   **Test séquentiel avec arrêt précoce (ex. frontières d'O'Brien-Fleming ou mSPRT sur les graines $g=1, 2, \dots, G_{\max}$)** :
    *   *Avantage* : Économise 30 à 50 % du budget (illustratif) quand un cran est manifestement nul ($\hat{\Delta}_1 \le -0,05$ dès la graine 1 : arrêt pour futilité) ou écrasant.
    *   *Piège* : Biais d'estimation à l'arrêt (un arrêt précoce pour succès surestime $\Delta$), nécessitant de dépenser un budget d'audit d'alpha.

*Synthèse opérationnelle recommandée pour l'analyse* : **Test de permutation hiérarchique stratifié** (exact sur les $2^G$ échanges de bras pour le bruit de graine + test de permutation exact sur les 60 différences d'items pondérées $d_i$), complété par un arrêt de futilité après la graine $g=1$ si $\hat{\Delta}_{g=1} < 0$.

---

### 2. L'instrument « Parades au surapprentissage du test final de 60 items » (Point 0)
Si le même jeu de 60 items est interrogé $K$ fois (pour choisir parmi $K$ crans ou configurations), le maximum observé $\max_{k=1\dots K} \hat{\Delta}_k$ souffre du biais de sélection (« Winner's Curse ») d'ordre $\sigma_{\text{item}} \sqrt{2 \ln K}$.
Voici le coût exact en items et en puissance des trois parades mentionnées dans la question :

| Parade | Mécanisme | Coût en items | Impact sur la puissance ($1-\beta$) et les fausses alertes ($\alpha$) |
| :--- | :--- | :--- | :--- |
| **Parade 1 : Scission du jeu de 60 items** (30 Sélection / 30 Confirmation intouchée) | On utilise 30 items (18 A, 12 B) pour monter l'escalier, et on ne lit les 30 autres qu'une seule fois sur le gagnant final. | **$-30$ items** à chaque étape ($N_{\text{eff}}$ tombe de $57,6$ à $28,8$). | **Effondrement de la puissance** : l'erreur-type d'item est multipliée par $\sqrt{2} \approx 1,414$ [VÉRIFIÉ]. Sur 12 items de la famille B (6 honnêtes, 6 sabotés), un seul item fait sauter le score de $\pm 0,0833$ ! Pour détecter $\delta=0,10$, la puissance généralisée chute de 78 % à **49 %** (illustratif). Fausses alertes sur la confirmation : contrôlées exactement à $\alpha = 0,05$. |
| **Parade 2 : Maintien des 60 items + Correction des comparaisons multiples (Holm-Bonferroni ou Dunnett apparié)** | Les 60 items servent à chaque cran, mais le seuil critique passe de $\alpha$ à $\alpha / K$ (ou via la distribution du $\max$ prenant en compte la corrélation entre crans). | **0 item perdu** ($N=60$ partout). | **Perte modérée de puissance** : Pour $K=3$ crans, passer de $\alpha=0,05$ à $\alpha/3 = 0,0167$ fait monter $z_{1-\alpha}$ de $1,645$ à $2,128$. Pour maintenir la même puissance, il suffit d'augmenter le nombre de graines de $(2,128 / 1,645)^2 \approx 1,67$ (ex. passer de $G=2$ à $G=3$ ou $4$ graines, illustratif), ce qui est beaucoup moins destructeur que de perdre la moitié des items. |
| **Parade 3 : Seuil adaptatif (Reusable Holdout / Thresholdout, Dwork et al., 2015)** | Le juge du noyau ne révèle pas le score exact sur les 60 items : il révèle uniquement si $\hat{\Delta}_k \ge \delta + \eta$ où $\eta \sim \text{Laplace}(b)$ est un bruit injecté quand un cran est testé. | **0 item perdu**, mais perte de précision équivalente à un bruit additionnel $\text{Var}(\eta) = 2b^2$. | Empêche mathématiquement l'adaptation aux 60 items (la capacité d'information mutuelle croît en $\sqrt{K}$ au lieu de $K$), mais avec seulement $K=2$ ou $3$ crans dans un escalier, le bruit injecté $\eta$ dégrade plus la puissance qu'une simple correction de Holm-Bonferroni. |

*Verdict sur le surapprentissage* : Ne **jamais** couper un jeu de 60 items en deux (30 items rendent la famille B aveugle avec 6 items par classe). Garder les **60 items entiers**, limiter l'escalier à $K \le 3$ crans en aveugle (l'organisme ne voit jamais les 60 items, et Lazar ne choisit pas les crans après avoir vu les 60 items : les crans sont tous préenregistrés), et appliquer une **correction par permutation du maximum (Westfall-Young)** sur les $K$ crans.

---

### 3. Tableau récapitulatif des instruments (Mesure minimale, Cas honnêtes appariés, Vérifications mécaniques à battre)

| Instrument nommé dans la question | Mesure minimale de fonctionnement | Taux de détection ($1-\beta$) et Fausses alertes ($\alpha$) | Cas honnêtes appariés | Vérification mécanique à battre (Baseline) |
| :--- | :--- | :--- | :--- | :--- |
| **Juge du noyau & Métrique d'exactitude équilibrée (A et B)** | Capacité à discriminer l'organisme du classifieur de surface sur les 60 items. | $1-\beta \ge 0,80$ pour un gain de $+0,10$ ; $\alpha \le 0,05$ (test de permutation apparié sur les 60 items). | Les 12 traces honnêtes de la famille B et les items non-évalués de A, appariés par longueur et domaine aux traces sabotées. | **Classifieur sur les traits de surface** : doit strictement battre **0,69 sur A** et **0,50 sur B** (RAPPORTÉ), ainsi que le classifieur constant (0,50 exactement). |
| **Détecteur de plateau et de valeur marginale ($\frac{\Delta \text{Score}}{\Delta \$}$)** | Arrêt correct de la montée d'escalier lorsque la pente réelle tombe sous $\lambda_{\min}$ (ex. $0,002$ point par USD, illustratif). | Détection d'un vrai plateau ($\Delta = 0$) avec probabilité $\ge 1 - \alpha = 0,95$ ; fausse alerte d'arrêt prématuré sur une vraie pente de $+0,10$ inférieure à $\beta = 0,15$. | Comparaison « A contre A » (les 2 graines gratuites du pilote au même budget) où la pente théorique est 0. | Règle aveugle dépensant toujours le budget maximal autorisé sans arrêt précoce. |
| **Déclencheur d'audit (« résultat suspect de propreté »)** | Détection d'une fuite du test final, d'un déterminisme anormal inter-graines ou d'un score aberrant. | Détection à 99 % (illustratif) d'une copie/fuite partielle ; fausses alertes d'audit $\le 5\%$ sur des runs intègres. | Runs intègres sur un jeu de développement syntagmatiquement similaire mais disjoint du test final. | Deux tests mécaniques : (1) Désaccord inter-graines $k_{\text{disc}} = 0$ sur 60 items (suspect de cache/fuite si température $>0$) ; (2) $\text{BalAcc} > 0,92$ d'un coup ou saut $|\Delta| > 0,25$ (illustratif). |

---

## (d) Règle de décision gelée complète, Pièges et Ancrage matériel

### 1. Conception de l'escalier (Point 0) et Plan (Point 2)
L'escalier proposé pour évaluation oppose **3 crans préenregistrés** (Bras $C_0$, $C_1$, $C_2$), ordonnés du coût marginal le plus faible vers le plus élevé, en groupant les axes pour éviter le piège des interactions manquées (cf. Expérience 1) :
*   **Cran $C_0$ (Base frugale — $\sim 12\text{ USD/graine}$, illustratif)** : Moisson standard ($\sim 0\text{ USD}$), 0 ronde de conception supplémentaire, Génération 0 seule, 1 caste par tâche, longueur de sortie standard. *(Utilise directement les 2 graines gratuites déjà payées dans le pilote ! Coût additionnel pour une 3e graine : $12\text{ USD}$).*
*   **Cran $C_1$ (Amplification Amont & Moisson — $\sim 22\text{ USD/graine}$, illustratif)** : Moisson doublée ($\sim 0\text{ USD}$), **+1 ronde de conception avant G0** ($\sim 10\text{ USD}$), Génération 0 avec **2 castes** par tâche (vérification croisée).
*   **Cran $C_2$ (Amplification Aval Évolutive — $\sim 42\text{ USD/graine}$, illustratif)** : Configuration $C_1$ + **passage à la Génération 1** (+10 à 22 USD, RAPPORTÉ) avec longueur de sortie étendue de 50 % pour les traces complexes.

**Appariement** :
*   **Par item** : Les 60 mêmes items (36 A, 24 B) sont évalués par $C_0, C_1, C_2$.
*   **Par graine** : On fixe $G$ graines maîtresses $(s_1, \dots, s_G)$. La graine $s_g$ contrôle l'aléa initial (échantillonnage de la moisson, température des appels de la ronde 0) de manière identique entre $C_0, C_1, C_2$ jusqu'au point de bifurcation architectural.

---

### 2. Règle de décision gelée complète (Point 3)

Cette règle est conçue pour être scellée avant lecture des résultats. Notons $S(C_k)$ la moyenne (ou la médiane trimean, voir pièges) de l'exactitude équilibrée globale $\frac{1}{2}(\text{BalAcc}_A + \text{BalAcc}_B)$ sur les $G$ graines du cran $k$, et $\bar{D}_k$ la dépense réelle moyenne en USD du cran $k$.

1.  **Étape 0 : Calibrage de $G$ par les 2 répliques gratuites de $C_0$**
    *   Lire les deux répliques de $C_0$ du pilote. Calculer $\hat{\sigma}_{\text{graine, robuste}}$ (formule de la section c.1).
    *   Si $\hat{\sigma}_{\text{graine, robuste}} \le 0,025$ (illustratif, $\le 3$ items discordants entre les deux graines), fixer **$G = 2$ graines par bras**.
    *   Si $0,025 < \hat{\sigma}_{\text{graine, robuste}} \le 0,045$, fixer **$G = 3$ graines par bras**.
    *   Si $\hat{\sigma}_{\text{graine, robuste}} > 0,045$, fixer **$G = 4$ graines par bras** (et déclencher une inspection de stabilité de l'organisme).
2.  **Étape 1 : Passage de $C_0$ à $C_1$ (et arrêt précoce de futilité)**
    *   Exécuter la graine 1 de $C_1$. Si $S_{g=1}(C_1) - S_{g=1}(C_0) < -0,035$ (soit $\le -1$ item net dès la première graine, illustratif) **ET** que la dépense réelle $D_{g=1}(C_1) > 1,2 \, D_{g=1}(C_0)$, **arrêt précoce de $C_1$ pour futilité**.
    *   Sinon, compléter les $G$ graines de $C_1$. Calculer $\hat{\Delta}_{1,0} = S(C_1) - S(C_0)$, la valeur-$p$ du test de permutation apparié $p_{1,0}$, et le **coût par point de pourcentage gagné** :
        $$\text{CPP}_{1,0} = \frac{\bar{D}_1 - \bar{D}_0}{100 \times \hat{\Delta}_{1,0}} \quad (\text{en USD par point de \% d'exactitude équilibrée})$$
    *   **Décision sur $C_1$** :
        *   **MONTER À $C_1$ (Validation franche)** si : $\hat{\Delta}_{1,0} \ge +0,0695$ ($+2$ items nets pondérés), $p_{1,0} \le 0,05$, aucun recul $> 0,0417$ ($1$ item) sur la famille B, et $\text{CPP}_{1,0} \le 2,50\text{ USD/pt\%}$ (illustratif : payer au plus 25 USD pour gagner +10 points).
        *   **RESTER À $C_0$ (Rejet / Égalité — la moins chère l'emporte, RAPPORTÉ)** si : $\hat{\Delta}_{1,0} < +0,0347$ ($< 1$ item net) **OU** $\bar{D}_1 - \bar{D}_0 > 2\text{ USD}$ avec $p_{1,0} > 0,20$.
        *   **ZONE GRISE** si : $+0,0347 \le \hat{\Delta}_{1,0} < +0,0695$ et $0,05 < p_{1,0} \le 0,20$. *Règle de résolution de la zone grise* : on n'ajoute **au plus qu'une seule graine supplémentaire** ($G \to G+1$) pré-budgétée. Si après $G+1$ graines la condition de montée franche n'est pas remplie, **la règle « à égalité la moins chère l'emporte » s'applique automatiquement : on reste à $C_0$**.
3.  **Étape 2 : Passage au cran $C_2$ et validation globale du préenregistrement ($\Delta \ge +0,10$)**
    *   Le cran $C_2$ est comparé au gagnant de l'étape 1 ($C_{\text{ref}} \in \{C_0, C_1\}$) selon les mêmes seuils marginaux ($\hat{\Delta}_{2,\text{ref}} \ge +0,0695$, $\text{CPP} \le 2,50\text{ USD/pt\%}$).
    *   **Clause de validation finale du programme** : Pour qu'un cran supérieur ($C_1$ ou $C_2$) soit déclaré gagnant au titre du préenregistrement exigeant $\Delta \ge +0,10$ (RAPPORTÉ), il doit vérifier $S(C_{\text{gagnant}}) - S(C_0) \ge +0,10$ sur l'une au moins des familles (ou en moyenne) avec une valeur-$p$ corrigée de Holm-Bonferroni $p_{\text{corrigée}} \le 0,05$. Sinon, $C_0$ l'emporte par défaut.

---

### 3. Traitement mécanique des 7 pièges identifiés (Point 3)

1.  **Comparaisons multiples s'il y a plusieurs crans** : Contrôlées par la procédure séquentielle hiérarchique (Gatekeeping) et Holm-Bonferroni sur les $K=2$ transitions ($C_0 \to C_1$ et $C_{\text{ref}} \to C_2$). Tester d'abord l'effet sur un ordre fixe évite l'inflation de $\alpha$.
2.  **Régression vers la moyenne** : Si l'on choisit de promouvoir le cran qui a eu le meilleur score sur la graine 1, son score sur les graines 2 et 3 baissera mécaniquement. *Parade* : La règle de décision évalue la moyenne sur toutes les $G$ graines planifiées (sauf arrêt de futilité vers le bas, qui ne sélectionne jamais un gagnant par hasard positif).
3.  **Effet plafond à 1 et items trop faciles en surface** : Sur la famille A, la référence de surface est déjà à **0,69** (RAPPORTÉ), soit $\approx 25$ items sur 36 réussis par la simple forme du texte ! Il ne reste donc que $36 - 25 = 11$ items « durs » discriminants sur A. Un gain de $+0,10$ sur A exige de résoudre $+3,6$ items parmi ces 11 items durs (soit $33\%$ de réduction d'erreur résiduelle). *Parade* : Calculer en audit secondaire le **score sur le sous-ensemble des items où le classifieur de surface échoue** (les 11 items durs de A et les 12 items de B) et rapporter le gain relatif de réduction d'erreur $\frac{S_1 - S_0}{1 - S_0}$ en complément de $\Delta$ brut.
4.  **Hasard du tirage de 60 items seulement** : Comme démontré en (c.1), l'erreur-type incompressible de tirage d'items est de $\sim 0,058$. *Parade* : Ne jamais interpréter un écart non significatif au test de permutation par item comme une preuve d'équivalence universelle ; borner la conclusion au jeu de test conditionnellement aux items si $p_{\text{graines}} < 0,05$ mais $p_{\text{items}} > 0,05$.
5.  **Dépendance entre familles (A et B)** : L'organisme partage le même noyau, la même ronde de conception et potentiellement les mêmes heuristiques entre A et B. Si une ronde de conception spécialise l'organisme sur A au détriment de B (transfert négatif), la moyenne $\frac{1}{2}(\text{BalAcc}_A + \text{BalAcc}_B)$ masque la casse. *Parade incluse dans la règle gelée* : Clause de **Pareto-sécurité** — interdiction de monter d'un cran si l'une des deux familles recule de plus de $1$ item ($-0,0278$ sur A ou $-0,0417$ sur B).
6.  **Effet d'une seule graine aberrante (Crash / Timeout d'une génération)** : Une tâche sans réponse valide compte comme une erreur (RAPPORTÉ). Si sur la graine $s_2$, une erreur syntaxique dans le code généré par l'organisme fait planter 15 items d'un coup, la moyenne arithmétique sur $G=3$ graines s'effondre. *Parade à double détente* :
    *   Pour un **moniteur de sécurité en production**, la fiabilité fait partie du score : la **moyenne arithmétique** (qui pénalise le crash) reste la métrique primaire opposable.
    *   Pour comprendre le potentiel algorithmique hors bug ponctuel, on préenregistre en métrique secondaire la **médiane sur $G=3$ graines** ainsi que le taux de réponses invalides/timeouts. Si l'écart $|\text{Moyenne} - \text{Médiane}| > 0,08$ (illustratif), cela déclenche un audit de robustesse du code généré.

---

### 4. Ancrage matériel et Coût estimé (Livrable d)

*   **Exécutants et modèles** : Le noyau fixe sert des exécutants de frontière figés (RAPPORTÉ). Pour les vérifications mécaniques à battre (classifieur sur les traits de surface à 0,69 sur A et 0,50 sur B) et l'analyse statistique locale, des modèles ouverts légers (ex. `scikit-learn` TF-IDF + Régression Logistique L2, ou un encodeur ouvert type DeBERTa-v3-large de $\sim 435\text{M}$ paramètres, illustratif) tournent sur un simple CPU ou 1 GPU grand public (ex. 1× RTX 4090 ou A10G, coût $< 1\text{ USD/heure}$, illustratif).
*   **Calcul nécessaire pour l'analyse statistique** : Le test de permutation exact sur 60 items ($10^5$ tirages Monte-Carlo stratifiés A/B) et $2^G$ permutations de graines prend moins de **3 secondes sur 1 cœur CPU** (coût $\approx 0,00\text{ USD}$, illustratif).
*   **Devis complet du plan d'escalier (illustratif, basé sur les ordres de grandeur RAPPORTÉS de 10–22 USD/génération et 10 USD/ronde)** :
    *   **Pilote (déjà engagé / gratuit)** : 2 graines au cran $C_0$ $= 0\text{ USD}$ de surcoût.
    *   **Complément du cran $C_0$** (1 graine pour atteindre $G=3$) : $1 \times 12\text{ USD} = 12\text{ USD}$ (illustratif).
    *   **Cran $C_1$** ($G=3$ graines $\times 22\text{ USD}$) : $66\text{ USD}$ (illustratif ; réduit à $22\text{ USD}$ si arrêt précoce à la graine 1).
    *   **Cran $C_2$** ($G=3$ graines $\times 42\text{ USD}$) : $126\text{ USD}$ (illustratif ; réduit à $42\text{ USD}$ si arrêt précoce à la graine 1, ou $0\text{ USD}$ si le plateau est déjà atteint en $C_1$).
    *   **Réserve de zone grise** (au plus 1 graine de départage) : $22\text{ à }42\text{ USD}$ (illustratif).
    *   **Budget total maximal de l'expérience d'escalier** : **$204\text{ à }246\text{ USD}$** (illustratif), et **$\sim 100\text{ USD}$** en espérance sous arrêt précoce de futilité.

---

## (5) Ce qui est connu : Références méthodologiques citables

Conformément à la règle 3 (aucun identifiant arXiv de mémoire, attribution exacte ou mention « référence à vérifier ») :

1.  **Sur le test de McNemar et la comparaison de classifieurs sur un jeu de test unique de petite taille** :
    *   Dietterich, T. G. (1998). *Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithms*. Neural Computation, 10(7), 1895–1923. (Établit la supériorité du test de McNemar et du $5\times 2$ cv lorsque le jeu d'évaluation est limité et que l'entraînement comporte un aléa de graine).
2.  **Sur la prise en compte simultanée des graines aléatoires et des items dans l'évaluation des modèles de langue (avec peu d'items)** :
    *   Miller, E. (2024). *Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations*. (Référence à vérifier pour les détails de publication formelle ; formalise la décomposition de variance par item et par tirage/échantillonnage avec erreurs-types clusterisées sur les benchmarks de LLM).
    *   Dror, R., Baumer, G., Shlomov, S., & Reichart, R. (2018). *The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing*. Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (ACL). (Référence standard sur le test de permutation apparié et le bootstrap en NLP).
    *   Reimers, N., & Gurevych, I. (2017). *Reporting Score Distributions Makes a Difference: Performance Study of LSTM-networks for Sequence Tagging*. Proceedings of EMNLP. (Démontre l'impact décisif de la variance inter-graines et le risque des conclusions tirées sur une seule graine).
3.  **Sur le surapprentissage d'un jeu de test tenu à l'écart (Holdout reuse) lors de comparaisons adaptatives** :
    *   Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., & Roth, A. (2015). *The Reusable Holdout: Preserving Validity in Adaptive Data Analysis*. Science, 349(6248), 636–638.
4.  **Sur les alternatives à l'escalier (Élimination successive / Bandits à budget fixe)** :
    *   Jamieson, K., & Talwalkar, A. (2016). *Non-stochastic Best Arm Identification and Hyperparameter Optimization*. Proceedings of the 19th International Conference on Artificial Intelligence and Statistics (AISTATS). (Introduit l'algorithme *Successive Halving* pour allouer un budget de calcul entre configurations concurrentes).
    *   Li, L., Jamieson, K., DeSalvo, G., Rostamizadeh, A., & Talwalkar, A. (2018). *Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization*. Journal of Machine Learning Research (JMLR), 18(185), 1–52.
5.  **Sur les variables instrumentales pour traiter la non-conformité entre traitement assigné (budget servi) et traitement reçu (budget dépensé)** :
    *   Angrist, J. D., Imbens, G. W., & Rubin, D. B. (1996). *Identification of Causal Effects Using Instrumental Variables*. Journal of the American Statistical Association (JASA), 91(434), 444–455.

FIN-DE-CELLULE
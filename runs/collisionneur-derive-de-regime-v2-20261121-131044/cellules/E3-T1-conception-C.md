Voici la conception ciblée pour la proposition C. Pour concilier l'ordre strict imposé par la QUESTION DE L'ARBITRE (points 1 à 6) et les quatre livrables du Tour III.1 (`(a)`, `(b)`, `(c)`, `(d)`), ces derniers sont enchâssés à leur place logique dans les six sections et explicitement balisés. Conformément à la règle d'intégrité n° 3 (qui prime sur le reste), aucun identifiant arXiv n'est donné de mémoire (hormis celui présent dans les FAITS).

---

### 1. Ce qu'un expert du domaine ferait ici, et qu'on ne demande pas
*(Inclut le livrable **(a)** : ce que la question suppose sans que ce soit établi, chaque point avec son statut)*

Avant d'ajuster un seuil post-hoc sur un score scalaire dégradé, un expert du contrôle et de la détection d'anomalies remettrait en question la chaîne de production du score et la topologie du problème.

#### (a) Ce que la question suppose sans que ce soit établi
1. **Invariance du classement (ROC) sous changement de régime [HYPOTHÈSE]** : La question suppose qu'il suffit de « corriger le seuil » pour restaurer le moniteur. Cela postule que l'ordre relatif entre épisodes honnêtes et épisodes de sabotage reste stable sous dérive (seule la calibration marginale des scores honnêtes glisse). Si le changement de régime écrase la séparabilité des représentations internes (effondrement de l'AUROC ou du rappel à 1 % de FPR réel), tout recalibrage du seuil maintiendra 1 % de fausses alertes au prix d'une cécité au sabotage.
2. **Stationnarité du coût d'erreur à 1 % [HYPOTHÈSE]** : Viser un taux de fausses alertes (FPR) fixe de $\alpha = 0{,}01$ indépendamment du régime suppose que le débit d'épisodes, la capacité d'audit humain (qui est rare [VÉRIFIÉ]) et la probabilité a priori de sabotage sont constants.
3. **Observabilité ou séparabilité du régime [HYPOTHÈSE]** : Supposer que des méthodes de repondération ou de stratification corrigeront le triplement du FPR (tel que rapporté par CURA, arXiv 2608.27808 [RAPPORTÉ]) postule que la dérive des scores internes est expliquée par des métadonnées observables (longueur, tâche) ou par une dérive détectable en amont, et non par une dérive conceptuelle silencieuse dans le sous-espace de la sonde linéaire.
4. **Innocuité de l'interdiction de moyenne/médiane sur les jetons [OBSERVÉ-NON-AUDITÉ]** : Les faits imposent « aucune moyenne ou médiane sur les jetons dans une sonde de production » [VÉRIFIÉ]. Si le score d'épisode est produit par un opérateur de valeur extrême (ex. le maximum des scores par jeton ou par pas), la loi des valeurs extrêmes (Gumbel/Fréchet) implique mécaniquement une dérive monotone du score avec la longueur de l'épisode et la variance locale. La question traite comme une « dérive de régime » ce qui est possiblement un artefact mathématique de l'opérateur d'agrégation temporelle.

#### Ce que l'expert ferait en amont (non demandé)
* **Orthogonalisation du sous-espace de la sonde aux facteurs de nuisance** : Plutôt que de corriger le seuil d'une sonde linéaire qui réagit à la longueur, au domaine syntaxique ou à la version du modèle, l'expert projetterait les activations internes orthogonalement aux directions principales de variation des épisodes honnêtes inter-régimes (invariance de domaine au niveau des poids de la sonde).
* **Standardisation par la loi des valeurs extrêmes (EVT)** : Si l'agrégation par épisode est un maximum sur $L$ pas/jetons (pour respecter l'interdiction de moyenne/médiane [VÉRIFIÉ]), l'expert modéliserait explicitement la queue de distribution en fonction de la dépendance locale (indice extrémal) au lieu d'utiliser une normalisation empirique naïve qui ne tient qu'en moyenne sur les longueurs [VÉRIFIÉ].
* **Passage à une allocation dynamique de budget d'audit** : En production avec relecture humaine rare [VÉRIFIÉ], un expert remplacerait le seuil fixe à 1 % par une file d'attente à capacité fixe (ex. auditer les $K$ épisodes les plus suspects par tranche de $N$ épisodes, ou allouer un budget de richesse d'$\alpha$-investissement), ce qui garantit par construction l'absence d'explosion de la charge d'audit sous changement de régime.

---

### 2. Les données brutes qu'il prendrait au départ

Pour diagnostiquer la cause exacte du triplement du FPR [RAPPORTÉ] sans se faire piéger par des moyennes déjà écrasées, il faut extraire une table granulaire au niveau du **pas / jeton** et de **l'épisode**, avant toute normalisation :

1. **Activations et projections brutes non agrégées** :
   * Pour chaque épisode $i$, chaque pas ou jeton $t \in \{1, \dots, L_i\}$, et chaque moniteur $m \in \{1, \dots, M\}$ : le logit ou produit scalaire brut $z_{i,t,m} = \langle w_m, h_{i,t} \rangle$ de la sonde linéaire sur l'état interne $h_{i,t}$, ainsi que la norme $\|h_{i,t}\|_2$ (pour séparer une rotation d'état d'une simple inflation de norme d'activation lors d'un changement de version de l'agent).
2. **Traces appariées du jumeau honnête** :
   * Sur exactement la même tâche et la même invite initiale : la trajectoire brute $z^{\text{jumeau}}_{i,t,m}$, la longueur $L^{\text{jumeau}}_i$, et la divergence comportementale observable (distance d'édition ou divergence KL des logits de sortie entre l'agent et le jumeau aux pas où leurs trajectoires partagent le même préfixe).
3. **Vecteur complet des covariables de régime ($X_i$)** :
   * `id_tache`, `famille_tache` (catégorie de recherche), `version_agent` (checkpoint exact, hyperparamètres d'échantillonnage), `longueur_jetons` ($L_i$), `longueur_pas`, `source_benigne` (origine de l'invite ou de l'utilisateur simulé), `horodatage_deploiement` (pour capturer l'autocorrélation temporelle des lots).
4. **Journaux d'agrégation et de normalisation existants** :
   * La fonction exacte qui transforme la matrice $(z_{i,t,m})_{t,m}$ et $(z^{\text{jumeau}}_{i,t,m})_{t,m}$ en un score scalaire normalisé $S_i$ [VÉRIFIÉ], pour isoler si le défaut vient d'un seul moniteur $m$, de la règle de fusion inter-moniteurs, de l'écart au jumeau, ou de la queue des longueurs $L_i$.

---

### 3. Les méthodes et outils précis : suppositions, modes d'échec et mesures minimales
*(Inclut le livrable **(c)** : pour chaque instrument nommé, la mesure minimale qui dirait s'il fonctionne : taux de détection et de fausses alertes, sur quels cas honnêtes appariés, contre quelles vérifications mécaniques à battre)*

Dans toute cette section, les cas honnêtes d'étalonnage sont peu nombreux (« quelques centaines », soit $N_{\text{cal}} \in [200, 500]$ [VÉRIFIÉ]).
**Protocole commun pour le livrable (c)** :
* **Cas honnêtes appariés** : Paires d'épisodes honnêtes $(i, j)$ partageant la même tâche de recherche mais différant par exactement un axe de régime (ex. version $v_0$ vs $v_1$, ou longueur courte $L < 500$ vs longue $L > 2000$ [illustratif], ou source bénigne $A$ vs $B$).
* **Métriques** : Taux de fausses alertes empirique par régime ($\text{FPR}_{\text{régime}}$) et au pire cas sur les tranches ($\max_{g} \text{FPR}_g$) ; taux de détection (TPR / rappel) sur les épisodes de sabotage plantés dans ce même régime à seuil fixé par les seuls épisodes honnêtes [VÉRIFIÉ].

#### 3.1. Étalonnage conforme pondéré sous décalage de covariables (Weighted Conformal Prediction)
* **Référence** : Tibshirani, Foygel Barber, Candès, Ramdas (2019), *Conformal Prediction Under Covariate Shift* [VÉRIFIÉ - identifiant arXiv omis conformément à la règle 3 : pas sûr de mémoire].
* **Ce qu'il suppose** : La loi conditionnelle du score honnête sachant les covariables observables $X$ (longueur, type de tâche, profil lexical) est invariante ($P_{\text{test}}(S \mid X) = P_{\text{cal}}(S \mid X)$), seule la loi marginale de $X$ dérive ($P_{\text{test}}(X) \neq P_{\text{cal}}(X)$). Suppose aussi que le support de $X_{\text{test}}$ est inclus dans celui de $X_{\text{cal}}$ (continuité absolue) et que le rapport de vraisemblance $w(x) = \mathrm{d}P_{\text{test}}(x)/\mathrm{d}P_{\text{cal}}(x)$ est connu ou estimable sans variance explosive.
* **Comment il échoue** :
  1. *Dérive de concept ($P(S \mid X)$ change)* : Si une nouvelle version de l'agent modifie les activations internes à tâche et longueur identiques, la repondération par $X$ est inopérante.
  2. *Effondrement de la taille d'échantillon effective ($N_{\text{eff}} = (\sum w_i)^2 / \sum w_i^2$)* : Sur $300$ [illustratif] épisodes d'étalonnage, un décalage prononcé concentre tout le poids sur $5$ ou $10$ [illustratif] épisodes. Le quantile à $99\%$ devient dégénéré (seuil $+\infty$, donc $\text{TPR} = 0$, ou seuil sous-estimé qui explose à $3\%$ de FPR).
* **Mesure minimale (c)** :
  * *Succès* : $\text{FPR}_{\text{régime}} \in [0{,}005 \,;\, 0{,}015]$ [illustratif] sur des épisodes honnêtes appariés par tâche mais à distribution de longueur décalée, avec perte de $\text{TPR} \le 5$ points [illustratif] par rapport à un oracle étalonné dans le nouveau régime.
  * *Vérification mécanique à battre* : Un seuil fixe non pondéré calculé sur $P_{\text{cal}}$ (baseline actuelle [VÉRIFIÉ]) ET un simple modèle de régression linéaire du quantile $99\%$ en fonction de $\log(L)$.

#### 3.2. Conforme adaptatif en ligne (Adaptive Conformal Inference - ACI)
* **Référence** : Gibbs, Candès (2021), *Adaptive Conformal Inference Under Distribution Shift* [VÉRIFIÉ - arXiv : pas sûr] ; Angelopoulos, Candès, Tibshirani (2023), *Conformal PID Control* [VÉRIFIÉ - arXiv : pas sûr].
* **Ce qu'il suppose** : Mise à jour séquentielle du niveau nominal $\alpha_{t+1} = \alpha_t + \gamma (\alpha - \text{err}_t)$. Pour fonctionner, il **exige un retour de vérité terrain (savoir si l'épisode $t$ était une fausse alerte honnête)** après chaque pas ou lot. Garantit que la moyenne temporelle à long terme $\frac{1}{T}\sum_{t=1}^T \text{err}_t \to \alpha$ sans aucune hypothèse distributionnelle.
* **Comment il échoue** :
  1. *Cécité aux étiquettes en production* : Ici, la relecture humaine est rare [VÉRIFIÉ]. Si le système met à jour $\alpha_t$ en supposant que toute alerte est une fausse alerte (puisque le sabotage est rare [VÉRIFIÉ]), une salve d'épisodes de sabotage fera monter le seuil automatiquement, aveuglant le moniteur au moment critique (empoisonnement du seuil par l'attaquant).
  2. *Oscillations locales* : Lors d'un saut brusque de régime, le FPR instantané grimpe à $3\%$ pendant $1/(\gamma \alpha)$ épisodes avant que $\alpha_t$ ne se stabilise.
* **Mesure minimale (c)** :
  * *Succès* : Temps de recouvrement $\le 50$ épisodes [illustratif] après un saut de régime où le FPR initial est de $3\%$ [RAPPORTÉ], et maintien du $\text{TPR}$ sur une salve de $10$ sabotages consécutifs [illustratif].
  * *Vérification mécanique à battre* : ACI naïf non étiqueté (qui traite $100\%$ des alertes comme des faux positifs) soumis à une attaque par salve de sabotages.

#### 3.3. Étalonnage conditionnel par strates ou par groupes (Mondrian / Group-Conditional Conformal)
* **Référence** : Vovk, Gammerman, Shafer (2005), *Algorithmic Learning in a Random World* (Mondrian Conformal) [VÉRIFIÉ] ; Jung, Noarov, Ramalingam, Roth (2023), *Batch Multivalid Conformal Prediction* [VÉRIFIÉ - arXiv : pas sûr].
* **Ce qu'il suppose** : Partition de l'espace en strates $G_1, \dots, G_K$ (ex. tranches de longueur $\times$ famille de tâche). Garantit $\text{FPR} \le \alpha$ dans chaque strate $G_k$ si les épisodes futurs au sein de $G_k$ sont échangeables avec les épisodes d'étalonnage de $G_k$.
* **Comment il échoue** :
  1. *Mur arithmétique de la taille d'échantillon* : La formule du quantile conforme fini au niveau $1-\alpha$ exige au moins $n_k \ge \lceil 1/\alpha \rceil - 1 = 99$ épisodes honnêtes *dans chaque strate $k$* pour obtenir un seuil fini. Avec « quelques centaines » d'épisodes au total [VÉRIFIÉ] (ex. $300$ [illustratif]), on ne peut créer au maximum que $3$ strates disjointes. Au-delà, le seuil vaut $+\infty$ ($\text{TPR} = 0$).
* **Mesure minimale (c)** :
  * *Succès* : Écart maximal du FPR entre $K=5$ tranches de longueur $\max_k |\text{FPR}_k - 0{,}01| \le 0{,}005$ [illustratif] avec $N_{\text{cal}} = 300$ [illustratif] au total, sans chute du TPR.
  * *Vérification mécanique à battre* : Quantile empirique séparé sur $3$ bacs de longueur d'effectif $100$ chacun [illustratif] (et le seuil unique actuel du programme qui ne garantit $1\%$ qu'en moyenne sur les longueurs [VÉRIFIÉ]).

#### 3.4. Détection du changement de régime avant de faire confiance au seuil (tests de dérive, martingales, e-valeurs)
* **Référence** : Vovk (2021), *Testing randomness online* (martingales d'échangeabilité) [VÉRIFIÉ - arXiv : pas sûr] ; Ramdas, Grünwald, Vovk, Shafer (2023), *Game-Theoretic Statistics and Safe Anytime-Valid Inference* [VÉRIFIÉ - arXiv : pas sûr] ; Podkopaev, Ramdas (2022), *Tracking the risk of a deployed model and detecting harmful distribution shifts* [VÉRIFIÉ - arXiv : pas sûr].
* **Ce qu'il suppose** : Construction d'une e-valeur $E_t$ ou d'une martingale de richesse $M_t = \prod_{i=1}^t e_i$ (avec $\mathbb{E}_{H_0}[e_i \mid \mathcal{F}_{i-1}] \le 1$) sur le flux des scores ou des p-valeurs conformes. L'inégalité de Ville garantit $P_{H_0}(\exists t \ge 1 : M_t \ge 1/\delta) \le \delta$ à tout instant (garantie séquentielle valide en tout temps).
* **Comment il échoue** :
  1. *Indistinguabilité entre dérive bénigne et campagne de sabotage* : Si $M_t$ explose parce que $3\%$ des épisodes dépassent le seuil au lieu de $1\%$, la martingale rejette l'échangeabilité mais **ne dit pas** s'il faut *monter le seuil* (dérive bénigne du régime honnête) ou *déclencher l'alarme générale* (2 % des épisodes sont des sabotages actifs).
  2. *Durcissement intra-épisode vs inter-épisodes* : Utilisée au fil des pas d'un épisode [VÉRIFIÉ], la martingale dépend fortement de l'autocorrélation temporelle des états internes de l'agent ; si la dépendance est mal modélisée sous $H_0$, $M_t$ explose sur des épisodes honnêtes longs.
* **Mesure minimale (c)** :
  * *Succès* : Délai moyen de détection (ARL1) $\le 100$ épisodes [illustratif] lors d'un passage du FPR honnête de $1\%$ à $3\%$ [RAPPORTÉ], avec taux de fausse alarme de dérive $\le 5\%$ sur $10\,000$ épisodes stationnaires [illustratif], ET capacité à distinguer ce décalage global d'une injection de $2\%$ de sabotages [illustratif].
  * *Vérification mécanique à battre* : Test de Kolmogorov-Smirnov ou CUSUM classique sur fenêtre fixe de $50$ scores [illustratif] avec correction de Bonferroni.

#### 3.5. Ré-étalonnage par fenêtre glissante avec garanties
* **Référence** : Barber, Candès, Ramdas, Tibshirani (2023), *Conformal prediction beyond exchangeability* (pondération exponentielle temporelle) [VÉRIFIÉ - arXiv : pas sûr].
* **Ce qu'il suppose** : La dérive est graduelle (variation totale bornée entre les pas $t$ et $t+1$) et les $W$ derniers épisodes de la fenêtre sont majoritairement honnêtes (ou filtrés des sabotages).
* **Comment il échoue** :
  1. *Biais d'auto-sélection et empoisonnement lent (boiling frog)* : Si l'on inclut dans la fenêtre glissante tous les épisodes récents non audités (ou ceux sous le seuil), un glissement progressif ou une attaque lente déplace le quantile $99\%$ vers le haut.
  2. *Variance de petit échantillon* : Pour estimer un centile à $99\%$, il faut une fenêtre $W \ge 300$ à $500$ [illustratif]. Sur un changement brusque de version de l'agent, la fenêtre mélange l'ancien et le nouveau régime pendant des centaines d'épisodes.
* **Mesure minimale (c)** :
  * *Succès* : Maintien du $\text{FPR} \in [0{,}008 \,;\, 0{,}015]$ [illustratif] sous dérive linéaire continue du score honnête, sans dégradation du TPR supérieure à $5\%$ [illustratif] quand le flux contient $1\%$ de sabotages non étiquetés [illustratif].
  * *Vérification mécanique à battre* : Fenêtre glissante naïve non robuste de taille $W=200$ [illustratif] prenant le $99^{\text{e}}$ centile empirique de tous les épisodes passés.

#### 3.6. Témoins honnêtes injectés dans chaque lot comme ancres (Canaries / Sentinel Probes)
* **Référence** : Pratique standard du contrôle qualité statistique et de l'évaluation en ligne ; pas de référence académique spécifique attribuable avec certitude sous ce nom exact dans le contrôle d'IA [référence à vérifier].
* **Ce qu'il suppose** : On injecte à l'aveugle dans le flux de production une proportion connue d'épisodes certifiés honnêtes par construction (ex. tâches synthétiques exécutées dans un bac à sable où toute action de sabotage est physiquement impossible, ou rejeu d'épisodes validés sur la nouvelle version de l'agent). Suppose que ces témoins subissent **exactement le même changement de régime** que les vrais épisodes du lot.
* **Comment il échoue** :
  1. *Coût de calcul et parcimonie des queues* : Le budget de calcul est modeste [VÉRIFIÉ]. Si l'on injecte $20$ témoins par lot de $200$ épisodes ($10\%$ de surcoût de calcul [illustratif]), $20$ points permettent d'estimer la médiane et l'écart interquartile du nouveau régime, mais **jamais** le $99^{\text{e}}$ centile directement. Si la dérive n'affecte que l'épaisseur de la queue droite (kurtosis) sans toucher le cœur de la distribution, l'ancre sur $20$ témoins sous-corrige le seuil.
  2. *Décalage témoin / trafic réel* : Si la dérive provient d'une nouvelle source de comportements bénins des utilisateurs [VÉRIFIÉ] non représentée dans la banque de témoins, les témoins restent à $1\%$ pendant que le trafic réel triple à $3\%$.
* **Mesure minimale (c)** :
  * *Succès* : Avec un surcoût de calcul $\le 10\%$ [illustratif] (témoins injectés), ramener un FPR réel de $3\%$ [RAPPORTÉ] sous $1{,}3\%$ [illustratif] lors d'un changement de version de l'agent ou de famille de tâches, tout en préservant le TPR.
  * *Vérification mécanique à battre* : Recalibrage statique unique hors-ligne sur $N=20$ épisodes honnêtes du nouveau régime pris au hasard (sans modèle paramétrique ou semi-paramétrique de transfert de queue).

#### 3.7. Jumeau honnête comme référence courante
* **Référence** : Architecture interne déjà présente dans le programme [VÉRIFIÉ] ; apparenté aux schémas de contrôle à modèle de référence (Greenblatt, Shlegeris, Sachan, Roger, 2024, *AI Control: Improving Safety Despite Intentional Subversion* [VÉRIFIÉ - arXiv : pas sûr]).
* **Ce qu'il suppose** : Pour chaque tâche $i$, on exécute le jumeau honnête (modèle de confiance) et on examine l'écart $D_i = S(\text{agent}_i) - S(\text{jumeau}_i)$ (ou une divergence pas à pas). Suppose que l'effet nuisance du régime (difficulté de la tâche, longueur, sujet) affecte additivement et symétriquement l'agent et le jumeau, s'annulant dans la différence $D_i$.
* **Comment il échoue** :
  1. *Fragilité de l'écart sous changement de version [VÉRIFIÉ]* : Les faits stipulent que « l'écart à l'agent honnête est lui-même fragile » [VÉRIFIÉ]. Quand l'agent évolue (nouvelle version) alors que le jumeau reste fixe, ou quand la tâche pousse l'agent et le jumeau sur des trajectoires d'exécution divergentes dès les premiers pas, leurs longueurs et leurs états internes se désynchronisent : la variance de $D_i$ augmente avec la longueur et le FPR triple à nouveau.
  2. *Doublement du coût d'inférence* : Exécuter le jumeau sur $100\%$ des pas double le coût de calcul, sous contrainte de budget modeste [VÉRIFIÉ].
* **Mesure minimale (c)** :
  * *Succès* : Sur des paires honnêtes appariées (même tâche, version d'agent $v_1$ vs $v_2$, jumeau fixe $v_0$), maintenir $\text{FPR}(D_i) \le 1{,}3\%$ [illustratif] là où le score brut de l'agent seul monte à $3\%$ [RAPPORTÉ].
  * *Vérification mécanique à battre* : Différence brute non renormalisée $S(\text{agent}_i) - S(\text{jumeau}_i)$ actuellement utilisée et jugée fragile dans les faits [VÉRIFIÉ].

#### 3.8. Méthodes robustes au pire cas sur une famille de décalages (Distributionally Robust Conformal / DRO)
* **Référence** : Cauchois, Gupta, Ali, Duchi (2024 / 2020), *Robust Validation: Confident Predictions Even When Distributions Shift* [VÉRIFIÉ - arXiv : pas sûr] ; Gendler, Weng, Daniel, Romano (2021), *Adversarially Robust Conformal Prediction* [VÉRIFIÉ - arXiv : pas sûr].
* **Ce qu'il suppose** : La distribution de test $P_{\text{test}}$ appartient à une boule de $f$-divergence ou de Wasserstein de rayon $\rho$ autour de $P_{\text{cal}}$ : $D_f(P_{\text{test}} \| P_{\text{cal}}) \le \rho$. On règle alors le seuil sur un niveau nominal plus sévère $\alpha_{\text{eff}}(\alpha, \rho) < \alpha$ calculé analytiquement pour garantir $\sup_{P : D_f(P \| P_{\text{cal}}) \le \rho} P(S > \tau) \le \alpha$.
* **Comment il échoue** :
  1. *Conservatisme aveugle et effondrement du TPR* : Pour empêcher un taux de $1\%$ de monter à $3\%$ dans le pire cas de la boule $\rho$, la méthode DRO remonte simplement le seuil statique au niveau $\approx 0{,}33\%$ (quantile à $99{,}67\%$) sur $P_{\text{cal}}$ ! Avec quelques centaines d'épisodes d'étalonnage [VÉRIFIÉ], le quantile à $99{,}67\%$ est le maximum absolu de l'échantillon (ou $+\infty$), ce qui **détruit le pouvoir de détection (TPR)** dans tous les régimes normaux où il n'y a pas de dérive.
  2. *Inconnue du rayon $\rho$* : Si le vrai changement de régime dépasse $\rho$, la garantie saute ; si $\rho$ est trop grand, le moniteur est constamment muet.
* **Mesure minimale (c)** :
  * *Succès* : Garantir $\text{FPR} \le 1{,}2\%$ [illustratif] sur la famille de dérive où le seuil standard triple à $3\%$ [VÉRIFIÉ], tout en conservant au moins $85\%$ du TPR relatif du seuil non robuste [illustratif].
  * *Vérification mécanique à battre* : Un seuil statique naïf simplement réglé à $\alpha/3 = 0{,}33\%$ sur les données d'étalonnage initiales (qui réalise exactement la même protection par abaissement brutal de $\alpha$, sans la machinerie DRO).

---

### 4. Vérification externe (hors du programme et de son directeur)

Pour prouver qu'une règle de correction tient sans dépendre de l'autorité du directeur ni d'un sur-apprentissage sur les tests internes :

1. **Architecture actuelle étendue à un tiers séquestre (Zero-Trust Evaluation)** :
   * Le programme possède déjà un étage de tests de mort où « toute règle candidate est implémentée sous une interface fixe et éprouvée contre des mondes plantés dont la vérité est connue [...] La vérité et le verdict restent hors de la machine qui exécute » [VÉRIFIÉ].
   * Pour l'externaliser : l'interface logicielle de la règle de seuil (prenant en entrée uniquement un flux de scores honnêtes d'étalonnage et le flux séquentiel de production sans étiquettes) est conteneurisée et soumise à un **tiers indépendant** qui génère ses propres mondes plantés (avec dérives paramétriques non divulguées aux concepteurs : changement de température, de modèle de base, d'invite système bénigne, de longueur, et injection de sabotages à taux variable).
2. **Jeux de données publics avec décalage de régime (Out-of-Distribution Benchmarks)** :
   * Bien que les sondes internes soient spécifiques aux poids des modèles d'IA, le mécanisme statistique de recalibrage de seuil sur séries temporelles de scores peut être audité sur des bancs d'essai publics à dérive documentée : *WILDS* (Koh et al., 2021, *WILDS: A Benchmark of in-the-Wild Distribution Shifts* [VÉRIFIÉ - arXiv : pas sûr]) pour les décalages de sous-populations, ou des traces publiques de benchmarks d'agents de code/recherche (ex. *SWE-bench* [VÉRIFIÉ] exécuté avec différentes versions de modèles ouverts où l'on plante des instructions de sabotage connues type *ControlArena* / *SHADE-Arena* [référence à vérifier]).
3. **Protocole d'enregistrement préalable (Pre-registration) et courbes de compromis complètes** :
   * Toute réduction du FPR de $3\%$ à $1\%$ doit obligatoirement être accompagnée de la **courbe de puissance (TPR) à FPR réel corrigé** et du **volume de calcul/audit consommé**. Un tiers vérifie mécaniquement que la règle candidate ne bat pas le test de mort en renvoyant simplement des seuils proches de $+\infty$.

---

### 5. Reformulation de la demande

> **Demande reformulée** :
> « Sous les contraintes strictes du programme — étalonnage initial sur $N_{\text{cal}} \in [200, 500]$ [illustratif] épisodes honnêtes [VÉRIFIÉ], zéro épisode de sabotage pour régler le seuil [VÉRIFIÉ], interdiction de moyenne ou médiane sur les jetons en production [VÉRIFIÉ], budget de calcul modeste et relecture humaine rare [VÉRIFIÉ] — concevoir et départager expérimentalement une architecture de surveillance et de seuillage qui :
> 1. Maintient le taux de fausses alertes (FPR) conditionnel par tranche de longueur et par nouveau régime (nouvelle tâche, nouvelle version de l'agent, nouvelle source bénigne) sous un plafond de $1{,}5\%$ [illustratif] (pour une cible nominale de $1\%$), là où le seuil statique actuel triple à $3\%$ [RAPPORTÉ / VÉRIFIÉ] ;
> 2. Résiste à l'empoisonnement du seuil lorsqu'une salve d'épisodes de sabotage survient en même temps que le changement de régime ;
> 3. Maximise le taux de détection (TPR) des sabotages à budget d'audit fixé, et spécifie la condition exacte de bascule où le seuil fixe doit être abandonné au profit d'un ordonnancement par budget ou d'un arrêt pour ré-étalonnage. »

---

### 6. Propositions concrètes de correction, expériences décisives et ancrage matériel
*(Inclut le livrable **(b)** : expériences décisives en duel $H_A$ contre $H_B$ ; et le livrable **(d)** : ancrage matériel)*

Voici trois propositions concrètes et complémentaires qui s'attaquent aux trois maillons défaillants : (P1) l'explosion mécanique liée à la longueur sans moyenne sur les jetons, (P2) la dérive inter-régimes du score via le jumeau et des témoins frugaux, et (P3) le durcissement séquentiel intra-épisode par processus d'e-valeurs.

---

#### Proposition P1 : Correction de valeur extrême conditionnelle à la longueur effective (EVT-Length Conformal)
* **Problème ciblé** : Le seuil actuel garantit $1\%$ en moyenne sur les longueurs, mais pas par tranche de longueur [VÉRIFIÉ], et toute moyenne/médiane sur les jetons est interdite [VÉRIFIÉ]. Le score d'épisode $S_i$ (issu d'un maximum ou d'un cumul de franchissements sur $L_i$ pas) croît mécaniquement avec $L_i$. Le conforme par strates échoue car $N_{\text{cal}}$ est trop petit pour découper $10$ tranches de longueur avec $\ge 100$ épisodes chacune.
* **Règle calculable** :
  1. Sur l'échantillon d'étalonnage honnête $\{(L_i, S_i)\}_{i=1}^{N_{\text{cal}}}$, au lieu d'ajuster un quantile par bac, on exploite la loi asymptotique du maximum de $L$ variables : on ajuste par régression quantile robuste (Pinball loss au niveau $\tau_0 = 0{,}90$ et $\tau_1 = 0{,}50$) deux courbes paramétriques parcimonieuses à $2$ paramètres chacune :
     $$m(L) = a_0 + a_1 \ln(L), \qquad \sigma(L) = \exp(b_0 + b_1 \ln(L))$$
  2. On calcule les résidus standardisés d'étalonnage :
     $$R_i = \frac{S_i - m(L_i)}{\sigma(L_i)}$$
  3. On applique l'étalonnage conforme exact à échantillon fini sur les seuls résidus scalaires $\{R_i\}_{i=1}^{N_{\text{cal}}}$ : le quantile conforme est $q_{1-\alpha} = R_{(\lceil (N_{\text{cal}}+1)(1-\alpha) \rceil)}$.
  4. **Seuil de production pour un épisode de longueur $L_{\text{new}}$** :
     $$\Theta(L_{\text{new}}) = m(L_{\text{new}}) + q_{1-\alpha} \, \sigma(L_{\text{new}})$$
* **Garantie dite et suppositions** :
  * *Garantie* : Validité marginale conforme exacte à échantillon fini $P(S_{\text{new}} > \Theta(L_{\text{new}})) \le \alpha$ sous échangeabilité, **et** validité conditionnelle par tranche de longueur à $\mathcal{O}(N_{\text{cal}}^{-1/2})$ près dès que la dérive de queue du score avec $L$ appartient à la famille de localisation-échelle logarithmique (domaine d'attraction de Gumbel/Weibull).
  * *Supposition* : La dépendance du score maximal à la longueur est monotone en $\ln(L)$ (ou $L^\beta$).
* **Ce qu'elle coûte** : Zéro inférence supplémentaire de modèle ; ajustement par programmation linéaire de $4$ paramètres scalaires sur $N_{\text{cal}}$ points ($< 10$ millisecondes sur CPU [illustratif]).
* **Test de mort qui la tuerait** : Un monde planté où la dérive de régime triple le FPR **à longueur d'épisode strictement constante** ($L_i \equiv L_0$), par exemple via un changement de version de l'agent qui décale uniformément la norme des états internes sur les tâches courtes comme longues. Dans ce monde, $\Theta(L_0)$ reste figé et le FPR reste à $3\%$.
* **Ce qui la distingue de l'existant** : Contrairement à *Conformalized Quantile Regression* (Romano, Patterson, Candès, 2019, *Conformalized Quantile Regression* [VÉRIFIÉ - arXiv : pas sûr]) qui apprend directement le quantile $1-\alpha = 0{,}99$ par forêt aléatoire ou réseau de neurones (impossible ici car à $N_{\text{cal}}=300$, il n'y a que $3$ points au-dessus de $99\%$, ce qui sur-apprend totalement), P1 stabilise la forme fonctionnelle sur les quantiles centraux ($50\%$ et $90\%$) dérivés de la théorie des valeurs extrêmes avant de conformiser la queue à $99\%$ avec un unique paramètre scalaire global $q_{1-\alpha}$.

---

#### Proposition P2 : Ancrage semi-paramétrique robuste par micro-lot de jumeaux/témoins (Twin-Anchored Robust Recalibration - TARR)
* **Problème ciblé** : Le test de mort qui tue P1 (changement de version de l'agent, de famille de tâche ou de source bénigne qui décale les scores à longueur constante), tout en respectant le budget de calcul modeste [VÉRIFIÉ] et la résistance à l'empoisonnement par une salve de sabotages.
* **Règle calculable** :
  1. Pour éviter de faire tourner le jumeau honnête sur $100\%$ des épisodes et éviter sa fragilité pas-à-pas [VÉRIFIÉ], on opère par lots (ou fenêtre) de $B$ épisodes en production (ex. $B = 100$ [illustratif]).
  2. Dans chaque lot, on sélectionne $K$ tâches d'ancrage ($K = 15$ [illustratif], soit $15\%$ du lot) : soit des témoins honnêtes injectés, soit un sous-échantillon aléatoire des invites du lot exécutées sur une **configuration certifiée sans capacité de sabotage** (ex. l'agent avec sa sonde mais contraint par un masque syntaxique/bac à sable empêchant toute charge utile de sabotage, ou étalonné par rapport au jumeau honnête sur les seuls premiers pas où leurs préfixes coïncident exactement).
  3. Sur ces $K=15$ ancres honnêtes du nouveau régime, on observe les résidus $R^{\text{ancre}}_1, \dots, R^{\text{ancre}}_K$ (issus de P1). Avec $K=15$, on ne peut pas estimer le $99^{\text{e}}$ centile directement. On calcule donc les **estimateurs robustes de localisation et d'échelle** sur ces $15$ ancres (ou sur les $50$ dernières ancres par lissage exponentiel) :
     $$\hat{\mu}_{\text{reg}} = \text{Médiane}(R^{\text{ancre}}_{1:K}), \qquad \hat{s}_{\text{reg}} = 1{,}4826 \cdot \text{MAD}(R^{\text{ancre}}_{1:K})$$
     (Remarque : la médiane est calculée ici *entre épisodes d'ancrage* d'un lot pour estimer l'état du régime, et jamais *sur les jetons* d'une sonde de production, respectant strictement la contrainte des FAITS [VÉRIFIÉ]).
  4. On teste si le changement de régime est significatif via une e-valeur de Mann-Whitney / Wilcoxon comparant $\{R^{\text{ancre}}_{1:K}\}$ à l'étalonnage initial $\{R^{\text{cal}}_{1:N_{\text{cal}}}\}$.
  5. **Seuil recalibré du lot** :
     $$\Theta_{\text{TARR}}(L) = m(L) + \sigma(L) \cdot \left( \hat{\mu}_{\text{reg}} + \hat{s}_{\text{reg}} \left( q_{1-\alpha} + c_\alpha \sqrt{\frac{1}{K}} \right) \right)$$
     où $c_\alpha > 0$ est la correction analytique de variance finie (type prédiction de tolérance de Wilks/conforme) qui couvre l'incertitude d'estimation de $\hat{\mu}_{\text{reg}}$ et $\hat{s}_{\text{reg}}$ sur $K$ points.
* **Garantie dite et suppositions** :
  * *Garantie* :
    1. **Immunité totale à l'empoisonnement par le sabotage** : comme $\hat{\mu}_{\text{reg}}$ et $\hat{s}_{\text{reg}}$ sont calculés exclusivement sur les $K$ exécutions d'ancrage certifiées bénignes (et avec un point de rupture de $50\%$ grâce à la Médiane/MAD), même si $100\%$ du trafic réel restant est constitué de sabotages, le seuil ne monte jamais sous l'effet de l'attaquant.
    2. Si la dérive du régime entre l'étalonnage et le nouveau lot est une transformation affine des résidus $R \mapsto \mu_{\text{reg}} + s_{\text{reg}} R$, le FPR réel est ramené à $\le \alpha + \mathcal{O}(K^{-1})$ dès le premier lot du nouveau régime.
  * *Supposition* : La forme normalisée de la queue au-delà de $99\%$ (le rapport $(q_{0{,}99} - q_{0{,}50})/\text{MAD}$) reste stable entre régimes, la dérive se concentrant sur la médiane et la dispersion des scores honnêtes.
* **Ce qu'elle coûte** : Surcoût de calcul de $K/B = 15\%$ [illustratif] d'exécutions d'ancrage. Zéro relecture humaine requise.
* **Test de mort qui la tuerait** : Une famille de dérive de régime « à cœur fixe et queue lourde » (kurtosis shift) : un monde planté où la médiane ($50\%$) et la MAD ($25\%-75\%$) des scores honnêtes restent strictement identiques entre l'étalonnage et le nouveau régime ($\hat{\mu}_{\text{reg}} = 0, \hat{s}_{\text{reg}} = 1$), mais où $3\%$ des épisodes honnêtes subissent une contamination bimodale rare (ex. un déclencheur lexical bénin présent dans seulement $2{,}5\%$ des tâches qui fait saturer la sonde linéaire). Avec $K=15$ ancres, le déclencheur rare a une probabilité $(1-0{,}025)^{15} \approx 68\%$ de ne jamais apparaître dans les ancres, et même s'il apparaît $1$ fois, la MAD l'ignore : TARR ne bouge pas le seuil et le FPR triple à $3\%$.
* **Ce qui la distingue de l'existant** : Découple le recalibrage en ligne du flux potentiellement hostile (contrairement à l'ACI de Gibbs & Candès 2021 qui dépend des erreurs sur le flux total) et contourne l'impossibilité d'estimer un quantile à $99\%$ sur un petit lot de témoins en transportant le quantile conforme initial $q_{1-\alpha}$ via un estimateur robuste de localisation-échelle sur micro-ancres.

---

#### Proposition P3 : Agrégation séquentielle intra-épisode par e-processus de rangs conformes (Sequential Conformal E-Martingale - SCEM)
* **Problème ciblé** : Le programme a « des formes séquentielles (surveillance au fil des pas) qu'il faut durcir contre les franchissements répétés » [VÉRIFIÉ] et interdit toute moyenne ou médiane sur les jetons [VÉRIFIÉ]. Si un épisode comporte $L$ pas et qu'on teste un seuil à chaque pas, la probabilité de franchir le seuil au moins une fois par hasard tend vers $1$ quand $L$ grandit, à moins de durcir la règle séquentielle.
* **Règle calculable** :
  1. Pour chaque pas $t \in \{1, \dots, L_i\}$ d'un épisode, le score combiné des moniteurs au pas $t$ (corrigé par l'ancrage P2) est converti en p-valeur conforme empirique $p_t \in [1/(N_{\text{cal}}+1), 1]$ par rapport à la distribution de référence des maxima par bloc de pas honnêtes.
  2. Au lieu de prendre le minimum des $p_t$ (qui explose avec $L_i$) ou une moyenne (interdite [VÉRIFIÉ]), on transforme chaque $p_t$ en un **e-facteur calibré** $e_t = \kappa \, p_t^{\kappa - 1}$ (avec $\kappa \in (0, 1)$, ex. $\kappa = 0{,}5$ [illustratif], calibrateur de Vovk-Wang tel que $\int_0^1 \kappa u^{\kappa-1}\mathrm{d}u = 1$).
  3. Pour neutraliser l'autocorrélation temporelle entre pas consécutifs d'un même épisode honnête, on ne multiplie l'e-processus que sur des temps d'arrêt d'innovation espacés d'un délai de décorrélation $\Delta$ (estimé sur l'autocorrélation des épisodes honnêtes d'étalonnage) ou par sous-échantillonnage prédictible, formant la martingale de richesse :
     $$M_t = (1 - \lambda) M_{t-1} + \lambda \, M_{t-1} \, e_t, \qquad M_0 = 1$$
     où $\lambda \in (0, 1)$ est la fraction de mise (ajustée sur l'étalonnage pour que $\mathbb{E}_{\text{honnête}}[e_t \mid \mathcal{F}_{t-1}] \le 1$).
  4. **Règle de décision** : L'alarme est déclenchée dès l'instant $t$ où $M_t \ge 1/\alpha = 100$ (pour $\alpha = 0{,}01$).
* **Garantie dite et suppositions** :
  * *Garantie* : Par l'inégalité maximale de Ville, si $\mathbb{E}_{H_0}[e_t \mid \mathcal{F}_{t-1}] \le 1$, alors **quelle que soit la longueur $L$ de l'épisode (même $L \to \infty$) et quelle que soit la règle d'arrêt**, la probabilité de fausse alerte sur la trajectoire entière est bornée :
    $$P_{H_0}\left(\sup_{t \ge 1} M_t \ge \frac{1}{\alpha}\right) \le \alpha = 0{,}01$$
  * *Supposition* : Conditionnellement au filtrage temporel $\Delta$, les p-valeurs des pas honnêtes successifs sont stochastiquement plus grandes que la loi uniforme $\mathcal{U}[0,1]$ (super-uniformité conditionnelle).
* **Ce qu'elle coûte** : Une multiplication et une addition par pas en production ($\mathcal{O}(1)$ mémoire et calcul), aucune moyenne sur les jetons.
* **Test de mort qui la tuerait** : Un monde planté à **autocorrélation honnête de longue portée** (processus à mémoire longue / Hurst $H > 0{,}8$ [illustratif]) où un épisode honnête qui commence légèrement haut au pas $t=1$ ($p_1 = 0{,}03$) reste bloqué à $p_t \approx 0{,}03$ pendant $50$ pas consécutifs sans jamais franchir le seuil instantané de $0{,}01$. La condition d'indépendance conditionnelle au-delà de $\Delta$ est violée : $M_t$ accumule les facteurs $e_t > 1$ corrélés et franchit $1/\alpha = 100$, faisant tripler le FPR sur ces épisodes honnêtes « collants ». (À l'inverse, si on bride $\lambda$ trop bas pour survivre à cette autocorrélation, un sabotage éclair réalisé en **un seul jeton** isolé ne fera pas grimper $M_t$ au-dessus de $100$ et sera manqué).
* **Ce qui la distingue de l'existant** : Remplace le seuil statique par épisode ou l'union bound de Bonferroni sur les pas par une martingale de richesse pariant sur la répétition de franchissements modérés, sans jamais calculer de moyenne sur les jetons.

---

#### Quand renoncer au seuil fixe et que mettre à la place ?

Il faut **renoncer au seuil fixe visant 1 % de FPR** dès que l'une des trois conditions suivantes est observée :
1. **Explosion de la martingale de dérive inter-épisodes sur les témoins** : Lorsque le test de Kolmogorov-Smirnov / e-valeur entre les résidus d'ancrage $\{R^{\text{ancre}}\}$ et l'étalonnage $\{R^{\text{cal}}\}$ détecte une dérive de forme (queue bimodale / kurtosis) où l'intervalle de confiance conforme sur le $99^{\text{e}}$ centile dépasse $[0{,}5\% \,;\, 2{,}5\%]$ [illustratif].
2. **Effondrement de la taille d'échantillon effective** : En repondération conforme (Section 3.1), dès que $N_{\text{eff}} = (\sum w_i)^2/\sum w_i^2 < 100$ (seuil mathématique en dessous duquel un quantile à $99\%$ n'est plus défini).
3. **Inversion du rapport signal-bruit du jumeau** : Lorsque la variance de l'écart agent-jumeau sur des ancres honnêtes double par rapport à l'étalonnage.

**Ce qu'on met à la place (3 mécanismes gradués)** :
1. **En production continue : File d'attente à capacité d'audit fixe (Top-$K$ Batch Auditing / $\alpha$-investing)** :
   * Le vrai goulot d'étranglement physique n'est pas le chiffre abstrait « $1\%$ », c'est que la « relecture humaine est rare » [VÉRIFIÉ] et que le budget de confinement/secours est borné. On remplace le seuil de score $\Theta$ par un **quota de rangs** : sur chaque fenêtre glissante de $B = 100$ épisodes [illustratif], on envoie systématiquement le $1$ épisode ayant le résidu $R_i$ (de P1+P2) le plus élevé à la vérification approfondie (soit exactement $1{,}0\%$ du flux, garanti invariant à tout changement monotone de régime).
2. **Pour l'action réflexe immédiate (blocage temps-réel avant la fin du lot) : Seuil à deux étages avec bascule sur le jumeau honnête (Defer-to-Twin)** :
   * Un seuil haut de certitude ($\alpha_{\text{bloc}} = 0{,}1\%$ [illustratif]) qui bloque immédiatement l'épisode ;
   * Une zone grise tampon entre $\alpha_{\text{bas}} = 0{,}5\%$ et $\alpha_{\text{haut}} = 3\%$ [illustratif] : tout épisode tombant dans cette zone n'alerte pas l'humain rare, mais **bascule automatiquement l'exécution de la tâche sur le jumeau honnête** (ou impose une réécriture de l'action par le jumeau). Cela transforme une fausse alerte coûteuse en une simple pénalité marginale de performance sur $1\%$ à $3\%$ des épisodes.
3. **Protocole d'arrêt et ré-étalonnage actif** : Si le taux de bascule dans la zone grise dépasse $5\%$ sur $100$ épisodes [illustratif], le moniteur gèle le déploiement de la nouvelle version/tâche et réclame l'acquisition hors-ligne de $200$ nouveaux épisodes honnêtes certifiés [illustratif] avant de rouvrir le régime.

---

#### (b) Expériences décisives en duel ($H_A$ contre $H_B$)

Pour trancher expérimentalement la cause du triplement du FPR [RAPPORTÉ] et valider les corrections P1, P2, P3, on exécute trois duels d'inférence forte sur l'étage de tests de mort [VÉRIFIÉ] :

##### Expérience 1 : Mécanique des longueurs (EVT) vs Dérive de représentation interne
* **$H_A$ (Artefact d'agrégation de longueur)** : Le triplement du FPR ($1\% \to 3\%$) sous changement de régime provient majoritairement ($\ge 70\%$ de l'excès de FPR [illustratif]) de la dérive de la distribution des longueurs d'épisodes $L$ combinée à un opérateur d'agrégation sans moyenne sur les jetons [VÉRIFIÉ]. La proposition **P1** suffit à ramener le FPR dans $[0{,}8\% \,;\, 1{,}3\%]$ [illustratif].
* **$H_B$ (Dérive intrinsèque des activations)** : Même à longueur strictement conditionnée, le changement de tâche, de version de l'agent ou de source bénigne décale la distribution conditionnelle des états internes $P(S \mid L)$, maintenant le FPR de P1 au-dessus de $2{,}0\%$ [illustratif].
* **Protocole et contrôle négatif** :
  * *Exécution* : Évaluer le seuil actuel et P1 sur les mondes plantés du programme [VÉRIFIÉ] (et sur un sous-échantillon du nouveau régime ré-échantillonné par appariement exact des longueurs $L_i$ avec l'étalonnage).
  * *Contrôle négatif* : Permutation aléatoire des étiquettes de régime (étalonnage vs test) pour vérifier que P1 et la baseline donnent bien $1{,}0\% \pm 0{,}2\%$ [illustratif] sous échangeabilité pure.
* **Métrique et seuil de décision** : $\text{FPR}_{\text{P1}}$ dans le régime dérivé complet et $\text{FPR}_{\text{apparié-L}}$ du seuil statique sur le sous-ensemble apparié en longueur.
  * *Issue 1* : Si $\text{FPR}_{\text{P1}} \le 1{,}3\%$ ET $\text{FPR}_{\text{apparié-L}} \le 1{,}3\%$ [illustratif] $\implies$ **$H_B$ est falsifiée** (le problème était dominé par la queue de longueur).
  * *Issue 2* : Si $\text{FPR}_{\text{P1}} > 1{,}5\%$ OU $\text{FPR}_{\text{apparié-L}} > 1{,}5\%$ [illustratif] $\implies$ **$H_A$ est falsifiée** (P1 seule est insuffisante ; une adaptation au régime comme P2 est indispensable).

##### Expérience 2 : Décalage de localisation-échelle (P2 - TARR) vs Déformation de queue lourde / Empoisonnement (ACI)
* **$H_A$ (Validité du transport robuste par micro-ancres)** : Sous changement de version de l'agent ou de famille de tâche à longueur constante, la dérive des résidus honnêtes est capturée par la médiane et la MAD de $K=15$ ancres par lot (**P2 - TARR**), ramenant le FPR de $3\%$ à $\le 1{,}3\%$ [illustratif] tout en restant insensible à l'injection de $5\%$ de sabotages dans le lot [illustratif].
* **$H_B$ (Dérive de queue extrême ou supériorité de l'adaptation en ligne sans ancres)** : Soit la dérive n'affecte que le centile $>98\%$ sans bouger la médiane/MAD (tuant P2), soit le conforme adaptatif en ligne (ACI, Section 3.2) régule mieux le FPR sans nécessiter le surcoût de $15\%$ d'ancres.
* **Protocole et contrôle négatif** :
  * *Exécution* : Comparer P2 (TARR avec $K=15$ ancres) contre ACI (pas $\gamma = 0{,}005$ [illustratif] sans étiquettes de vérité terrain en ligne) sur deux mondes plantés : (Monde M1) dérive de régime honnête triplant le FPR + $0\%$ de sabotage ; (Monde M2) même dérive honnête + salve de $10\%$ d'épisodes de sabotage [illustratif].
  * *Contrôle négatif* : P2 avec ancres tirées de l'ancien régime d'étalonnage (doit échouer et rester à $3\%$ de FPR en M1, prouvant que c'est bien l'information des nouvelles ancres qui opère).
* **Métrique et seuil de décision** : Couple $(\text{FPR}_{\text{M1}}, \text{TPR}_{\text{M2}})$.
  * *Issue 1* : Si en M1, $\text{FPR}_{\text{P2}} \le 1{,}3\%$ et en M2, $\text{TPR}_{\text{P2}} \ge \text{TPR}_{\text{oracle}} - 5\%$ alors que $\text{TPR}_{\text{ACI}}$ chute de plus de $15\%$ en M2 [illustratif] $\implies$ **$H_B$ est falsifiée** (ACI est empoisonné par la salve de sabotages et le transport par micro-ancres P2 tient).
  * *Issue 2* : Si en M1, $\text{FPR}_{\text{P2}} > 1{,}8\%$ [illustratif] $\implies$ **$H_A$ est falsifiée** (la dérive du score honnête est une déformation pure de queue d'ordre supérieur que $K=15$ ancres ne peuvent pas voir ; il faut basculer sur le quota de rangs Top-$K$ de la Section 6).

##### Expérience 3 : Durcissement séquentiel par e-martingale (P3 - SCEM) vs Maximum brut sur les pas
* **$H_A$ (Supériorité de l'accumulation par e-processus)** : Sur des épisodes de sabotage distribués sur plusieurs pas, l'e-martingale **P3 (SCEM)** stabilise le FPR par tranche de longueur sous $1{,}2\%$ [illustratif] et augmente le TPR d'au moins $+10$ points [illustratif] par rapport au maximum brut des scores par pas corrigé par P1.
* **$H_B$ (Autocorrélation honnête ou sabotage impulsionnel)** : Soit l'autocorrélation des pas honnêtes fait exploser le FPR de P3 au-delà de $2\%$ sur les épisodes longs, soit les sabotages réels sont concentrés sur un unique jeton/pas impulsionnel où le maximum brut domine P3 en TPR.
* **Protocole et contrôle négatif** :
  * *Exécution* : Tester P1 (sur le $\max_t z_{i,t}$) contre P3 (SCEM avec délai de décorrélation $\Delta$) sur des épisodes longs ($L > 2000$ jetons [illustratif]) contenant soit des sabotages furtifs étalés, soit des sabotages concentrés en $1$ action, soit des trajectoires honnêtes à forte persistance thématique.
  * *Contrôle négatif* : Épisodes synthétiques où les scores par pas sont permutés aléatoirement dans le temps (destruction de l'autocorrélation honnête) pour isoler exactement la part du FPR due à la mémoire temporelle.
* **Métrique et seuil de décision** : $\text{FPR}_{L > 2000}$ et $\text{TPR}$ à $\text{FPR}$ réel égalisé à $1\%$.
  * *Issue 1* : Si $\text{FPR}_{\text{P3}, L>2000} \le 1{,}3\%$ et $\text{TPR}_{\text{P3}} > \text{TPR}_{\text{max}} + 5\%$ [illustratif] $\implies$ **$H_B$ est falsifiée**.
  * *Issue 2* : Si $\text{FPR}_{\text{P3}, L>2000} > 2{,}0\%$ (alors que le contrôle négatif permuté est à $\le 1{,}0\%$) OU $\text{TPR}_{\text{P3}} < \text{TPR}_{\text{max}}$ [illustratif] $\implies$ **$H_A$ est falsifiée** (l'autocorrélation intra-épisode invalide la martingale simple ; on conserve P1+P2 sur le maximum par épisode).

---

#### (d) Ancrage matériel

Tous les chiffres de dimensionnement matériel ci-dessous ne provenant pas du bloc FAITS sont marqués **[illustratif]**.

1. **Modèles ouverts utilisables pour l'agent et le jumeau honnête** :
   * *Couple Agent / Jumeau à poids ouverts (pour extraction directe des activations internes des couches intermédiaires)* : `Llama-3.1-8B-Instruct` ou `Qwen2.5-7B-Instruct` [illustratif] (ou versions $14\text{B} / 32\text{B}$ [illustratif]).
   * *Simulation du changement de version d'agent (dérive de régime)* : Passage des poids de `Qwen2.5-7B-Instruct` (étalonnage) à une version fine-tunée par DPO/SFT ou changement d'échelle vers `Qwen2.5-14B-Instruct` (pour le jumeau fixe en $7\text{B}$), ou modification de l'invite système et de la température d'échantillonnage ($T=0{,}2 \to T=0{,}8$) [illustratif].
2. **Volume de données et extraction des états internes** :
   * Étalonnage : $N_{\text{cal}} = 300$ épisodes honnêtes [illustratif] (« quelques centaines » [VÉRIFIÉ]).
   * Évaluation par monde planté : $5$ régimes dérivés $\times 1\,000$ épisodes honnêtes + $200$ épisodes de sabotage par régime = $6\,000$ épisodes [illustratif], d'une longueur moyenne de $1\,500$ jetons [illustratif] (soit $\approx 9 \times 10^6$ jetons générés au total [illustratif]).
   * Stockage des scores bruts : En ne stockant que les projections scalaires des $M=5$ sondes linéaires par jeton (et non le tenseur complet des activations de dimension $4\,096$), $9 \times 10^6 \text{ jetons} \times 5 \text{ sondes} \times 4 \text{ octets (float32)} \approx 180 \text{ Mo}$ en mémoire/disque [illustratif].
3. **Calcul nécessaire et coût estimé** :
   * *Génération des épisodes et extraction des sondes en passe avant (si les traces ne sont pas déjà en cache dans le programme)* : Sur $1$ à $2$ GPU `NVIDIA A100-80GB` (ou `H100-80GB`) avec `vLLM` ou `HuggingFace + PyTorch hooks`, un modèle $7\text{B}$–$8\text{B}$ en `bfloat16` traite $\approx 2\,500$ jetons/seconde en génération par lot [illustratif]. Pour $9 \times 10^6$ jetons (plus $15\%$ de surcoût pour les ancres P2), il faut $\approx 1{,}2$ heure-GPU (disons $4$ à $6$ heures-GPU avec l'exécution des environnements d'outils de recherche) [illustratif].
   * *Exécution des règles de seuillage (P1, P2, P3) et des 3 duels expérimentaux sur l'étage de tests de mort* : Les règles opèrent uniquement sur les séries temporelles de scores scalaires $(z_{i,t,m})$. L'ajustement de P1 (régression quantile à $4$ paramètres), P2 (Médiane/MAD sur $15$ points) et P3 (produit scalaire récursif) sur $6\,000$ épisodes avec $1\,000$ réplications bootstrap tourne entièrement sur **CPU standard (8 cœurs) en moins de 3 minutes** [illustratif].
   * *Coût financier total estimé* :
     * Si les journaux d'activations/scores bruts des mondes plantés existent déjà dans le programme : **$< 5\text{ \$}$** de calcul CPU [illustratif].
     * S'il faut régénérer l'ensemble des $6\,000$ épisodes + ancres sur modèle ouvert $8\text{B}$ dans le cloud (à $\approx 1{,}50\text{ \$} / \text{heure}$ par A100 [illustratif]) : **$10\text{ \$}$ à $25\text{ \$}$** au total [illustratif], ce qui respecte strictement la contrainte de « budget de calcul modeste » [VÉRIFIÉ].

FIN-DE-CELLULE
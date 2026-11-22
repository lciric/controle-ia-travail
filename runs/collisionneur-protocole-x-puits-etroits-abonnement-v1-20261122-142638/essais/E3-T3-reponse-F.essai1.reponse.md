**Audit des pièces transmises (règles 1 et 2).** Les blocs `FAITS`, `QUESTION DE L'ARBITRE` (identiques), `E3-T1-conception-F` et les cinq critiques croisées (`A`, `B`, `C`, `D`, `E`) sont présents et complets ; aucun dépôt, jeu de données ou protocole du « retest de la v2 » n'est transmis. Les statuts d'origine ne sont jamais modifiés ; `VÉRIFIÉ` désigne ci-dessous uniquement une déduction mathématique prouvée explicitement dans ce texte, `RAPPORTÉ` un résultat publié cité, `OBSERVÉ-NON-AUDITÉ` les chiffres `0,55` et `0,40` de l'en-tête, et `HYPOTHÈSE` tout énoncé empirique ou de protocole. Conformément à la consigne du tour III.3, je ne réponds qu'aux sections visant la proposition F.

---

## (a) Traitement critique par critique (sections visant F)

### Critiques de la proposition A

1. **E1 aveugle au propre contre-exemple de F ($D \approx 1{,}012 < 1{,}10$ `(illustratif)` pour $m=50, p=10^{-3}, \eta=0{,}8$ `(illustratif)`), insensibilité du second moment à la masse près de $0$ et dépendance des seuils à $m$ [A(a).1, A(b).1] — ACCEPTÉE.**
   Le calcul de A est exact (`VÉRIFIÉ`) : $D - 1 = (m-1)\frac{p(1-\eta)}{\eta(1-p)}$ tend vers $0$ dès que $mp \ll 1$, même pour un plafond d'échec $1-\eta$ arbitraire. L'indice $D$ à $m$ fixe est abandonné dans E1' au profit de l'excès direct de probabilité d'échec $\mathbb{P}(S_m=0) - (1-p)^m$ à $m = \Omega(1/p)$.
2. **E1, verdict fixé par la définition du bloc (tâches distinctes $\implies H_B$ ; appels à graines indépendantes sur même prompt $\implies H_A$) [A(a).2, A(c).1] — ACCEPTÉE (première partie) ; REJETÉE puis TRANSFORMÉE EN TEST (seconde partie).**
   - *Acceptée* : regrouper des tâches de difficultés hétérogènes dans les blocs confond $\operatorname{Var}(p_j)$ avec la dépendance du générateur ; E1' impose un test strictement intra-tâche.
   - *Rejetée sur « même prompt à graines indépendantes $\implies H_A$ par construction »* : cela vaut pour un générateur local sans état audité (qui devient le *contrôle négatif* d'E1'), mais **pas** pour un générateur boîte noire opaque servi par une interface distante (routage, quantification dynamique, mise en lots ou état caché de session). Cette seconde moitié est donc *transformée en test* dans E1' en opposant l'interface réelle au témoin local sans état.
3. **Arrêt optionnel invalide par intervalles bootstrap répétés en E1 [A(a).3] — ACCEPTÉE.**
   Contradiction directe avec l'audit de notre propre instrument 4. E1' passe à un horizon fixe $R$ pré-enregistré avec issue « non jugeable » explicite.
4. **E2 : conjonction dans $H_A$, zone morte $(1; 2)$ `(illustratif)`, Lift conditionné aux tâches à positifs, dépendance de $G_{\text{déd}}$ à $N_g$, singletons sous $N_g \max_{x\in A} \mu(x) \lesssim 1$, contrôle de départage aléatoire [A(a).4, A(b).2, A(c).3] — ACCEPTÉE.**
   E2' supprime $G_{\text{déd}}$ du duel modal, écarte toute zone morte, mesure une différence de probabilité de découverte définie sur *toutes* les tâches (sans conditionnement sur les succès), inclut un départage aléatoire uniforme contrôlé et une grille en $N_g$.
5. **E3 : $\hat{\tau}=0$ par tâche a probabilité $(1-\tau)^{n^+}$ (rendant $H_B$ vraie par construction dès $\tau < 0{,}95$ `(illustratif)` à $n^+=1$), biais de sélection de l'audit vers les tâches moins étroites, contrôle synthétique à $\tau=0{,}95$ `(illustratif)` [A(a).5, A(b).3, A(c).2] — ACCEPTÉE.**
   Le critère $\hat{\tau}=0$ par tâche est retiré ; E3' adopte un audit non biaisé à probabilités d'inclusion connues et le contrôle synthétique à rappel constant proposé par A.
6. **E4 : apprentissage inter-tâches brisant l'indépendance des réplicats, mutation locale hors du cadre « tirages seuls », saturation de $R$ et inséparabilité, contrôles $K$ bras identiques et ordre permuté [A(a).6, A(b).4, A(c).4] — ACCEPTÉE et TRANSFORMÉE EN TEST.**
   La mutation locale est retirée du duel boîte noire, toute mémoire inter-tâches est proscrite, le ratio $R$ est remplacé par une différence de probabilités, et le duel est recentré (en E4') sur l'apport d'un retour gradué $\Phi$ dans un régime d'accès étendu explicitement déclaré.
7. **Tableau (c), ligne 3 : « faux signal de succès à $p=0$ » relève de $V$, non de $G$ [A(a).7] — ACCEPTÉE.**
   Exact (repris de D) : $G$ ne produit pas de verdict ; le tableau (c), ligne 3, est rectifié ci-dessous.

### Critiques de la proposition B

1. **E1 : zone intermédiaire $(1{,}10; 1{,}40)$ `(illustratif)` non déclarée (non-terminaison ou fausse décision SPRT), confusion entre état latent de session et autocorrélation sérielle, perte de puissance $c^2 \gtrsim 0{,}4/(49p)$ `(illustratif)`, séparation des sessions indépendantes et permutations intra-session [B(a).1, B(b).1, B(c).3] — ACCEPTÉE.**
   E1' scinde les deux estimandes en deux volets distincts : **E1'a** (état latent inter-sessions) et **E1'b** (autocorrélation/dérive intra-chaîne), chacun sans zone morte et à horizon fixe.
2. **E2 : incomplétude de $H_A / H_B$, $G_{\text{déd}}$ fonction déterministe de $U/N$ et $\rho$ indépendante des positifs, effondrement du classement par fréquence en régime de singletons [B(a).2, B(b).2] — ACCEPTÉE.**
   Corrigé par la refonte complète d'E2' (voir A.4).
3. **E3 : biais de sélection de l'audit si l'audit ressemble à un bras, majorité de paires $(0,0)$ à $N_g=256, p=10^{-3}$ `(illustratif)`, non-jugeabilité de $\tau=0$, vérification exhaustive des tirages des deux bras [B(a).3, B(b).3, B(c).1] — ACCEPTÉE (avec précision sur le coût de l'audit).**
   En régime $\rho \gg 1$, le bras proxy sur-génère un volume $N_{\text{proxy}} \gg N_{\text{base}}$ ; plutôt que de vérifier exhaustivement *tous* les rejets (ce qui multiplierait le coût d'audit hors-ligne par $\rho$), E3' utilise un échantillonnage stratifié des rejets à probabilité d'inclusion connue $a_0 > 0$ sur des tirages issus du même $G$, produisant un estimateur sans biais de Horvitz & Thompson (1952, *A Generalization of Sampling Without Replacement from a Finite Universe*, `RAPPORTÉ`) à coût maîtrisé (et se réduisant à la vérification exhaustive quand $a_0 = 1$).
4. **E4 : changement de configuration/prompt hors du modèle « tirages seuls d'un générateur unique », biais du contrôle SHA-256 quand les bras diffèrent par leur rendement en objets distincts, perte de puissance près de $0$ et $1$ [B(a).4, B(b).4, B(c).2] — ACCEPTÉE et TRANSFORMÉE EN TEST.**
   La séparation des régimes d'accès (Question 3) est rendue explicite dans E4', et l'égalisation du rendement en objets distincts sous l'oracle SHA-256 est intégrée comme contrôle négatif obligatoire.

### Critiques de la proposition C

1. **E2 : $G_{\text{déd}}$ indépendant de $V(x)$ et de $A$ (vrai par construction via doublons négatifs), relégation des singletons positifs hors du top-$k$ forçant $\widehat{\text{Lift}}_k = 0$, mesure séparée des doublons négatifs [C(a).1, C(b).2, C(c).2] — ACCEPTÉE.**
   La démonstration de C sur la relégation des singletons positifs est exacte (`VÉRIFIÉ`) ; E2' sépare le diagnostic de doublons négatifs $1 - U_{N_g}^-/N_g^-$ du duel modal et explore plusieurs valeurs de $N_g$.
2. **E4 : avant le premier succès, la suite de retours binaires est $(0,\dots,0)$ (trajectoire fixée en loi), biais d'indexation des bras et fuite par canal auxiliaire ($c_v(x)$, doublons, longueur), permutation des bras et masquage de $c_v(x)$ [C(a).2, C(c).3] — ACCEPTÉE comme preuve ; extension TRANSFORMÉE EN TEST.**
   L'impossibilité d'apprentissage en ligne avant premier succès sous $V \in \{0,1\}$ pur sans canal auxiliaire est promue au rang de **résultat établi** (`VÉRIFIÉ`, voir ci-dessous) et retirée des expériences (règle B4) ; les contrôles de permutation des bras et de masquage de $c_v(x)$ sont transférés dans E4'.
3. **E3 : confusion entre zéro d'échantillonnage $\hat{\tau}_{\text{OOD}}=0$ et effondrement structurel $\tau_{\text{OOD}}=0$ [C(a).3, C(b).3] — ACCEPTÉE.** (Corrigé dans E3'.)
4. **Tableau 2 : Good–Turing ($N_1/N_g$) + McAllester–Ortiz (2003) donne une borne en $O(1/\sqrt{N_g})$ strictement dominée par Clopper–Pearson en $O(1/N_g)$ après zéro succès [C(a).4] — ACCEPTÉE.**
   Rectification exacte (`VÉRIFIÉ`) : l'inclusion $p \le M_{N_g}$ sur $\{S_{N_g}=0\}$ est algébriquement vraie, mais son estimation par masse manquante n'améliore pas le certificat sur $p$ (sauf support fini intégralement énuméré où $M_{N_g}=0$). Le rôle valide de Good (1953, *The Population Frequencies of Species and the Estimation of Population Parameters*, `RAPPORTÉ`) et McAllester & Ortiz (2003, *Concentration Inequalities for the Missing Mass and for Histogram Rule Error*, `RAPPORTÉ`) est d'estimer le coût marginal résiduel de vérification sous déduplication ($c_g + M_{N_g} c_v$).
5. **E1 : $D \approx 1{,}049 < 1{,}10$ `(illustratif)` sous $\eta=0{,}5, p=10^{-3}, m=50$ `(illustratif)` et contrôle par mélange latent synthétique calibré à $\hat{p}$ [C(b).1, C(c).1] — ACCEPTÉE.**
   Le contrôle calibré $\Theta \in \{0, 2\hat{p}\}$ est intégré dans E1' comme test de puissance obligatoire.

### Critiques de la proposition D

1. **E1 : vraisemblances absentes pour le SPRT, incapacité des deux premiers moments ($\mathbb{E}[P], \mathbb{E}[P^2]$) à déterminer le plafond $\mathbb{P}(P=0)$, non-terminaison et perte de niveau du bootstrap répété, réinitialisations indépendantes [D(a).1, D(b).1, D(c).1] — ACCEPTÉE.** (Corrigé dans E1'.)
2. **E2 : $G_{\text{déd}}$ invariant par permutation des verdicts, Lift indéfini à $k=0$ ou $0$ positifs, départage gelé sous permutation par classe [D(a).2, D(b).2, D(c).2] — ACCEPTÉE.**
   E2' adopte la permutation des verdicts par classe avec départage gelé ainsi que la formule hypergéométrique sans remise (en le disant, règle B1).
3. **E3 : sélection conditionnelle sur les tâches résolues par le comparateur ; non-distinguabilité uniforme de $\tau=0$ face à $\tau>0$ arbitrairement petit $\implies$ estimer la fraction sous un seuil opérationnel avec audit à inclusion connue incluant les tâches où aucun bras n'a réussi [D(a).3, D(b).3, D(c).3] — ACCEPTÉE.**
   Reformulation adoptée intégralement dans E3'b avec pour seuil opérationnel le seuil exact de rentabilité $\tau^*_{\text{réel}}$.
4. **E4 : théorème du calendrier tout-négatif prédéterminable (`VÉRIFIÉ` chez D), échec $\prod_j (1-p_j)^{n_j}$, dénominateur nul du ratio, contrôle par rejeu du calendrier tout-négatif sans accès aux verdicts et masquage de latence [D(a).4, D(b).4, D(c).4] — ACCEPTÉE et TRANSFORMÉE EN TEST.**
   Théorème intégré dans les résultats établis ; rejeu aveugle adopté comme contrôle négatif clé dans E4'.
5. **Certificat séquentiel *anytime-valid* : pour la seule disjonction à zéro succès $\mathcal{E}_{\text{succès}}(t) \lor (p \le 1-\delta^{1/t})$, aucun surcoût logarithmique itéré n'existe sous i.i.d. [D(b).5] — ACCEPTÉE.**
   Correction mathématique majeure (`VÉRIFIÉ`, démontrée ci-dessous) qui rectifie notre tableau 2 et notre tableau (c), ligne 4.

### Critiques de la proposition E

1. **E1 : aveuglement à $\eta=0{,}5$, confusion inter-tâches sur $300$ `(illustratif)` tâches, destruction de $\operatorname{Var}(p_j)$ par permutation globale, violation de la loi du logarithme itéré (Robbins, 1970) par bootstrap répété, $\widehat{D}=0/0$, permutation intra-tâche et mélange latent implanté [E(a).1, E(b).1, E(c).1] — ACCEPTÉE.** (Corrigé dans E1'.)
2. **E3 : zéros d'échantillonnage pour $\hat{\tau}_{\text{OOD}}=0$, couplage avec McNemar par conditionnement sur la base, $|J^*|=0$ non jugeable, contrôle binomial simulé à $\tau_0 > 0$ constant, et surcoût conditionnel $\mathbb{E}[C_v \mid F=1] \neq \mathbb{E}[C_v]$ [E(a).2, E(b).3, E(c).2] — ACCEPTÉE et TRANSFORMÉE EN TEST.**
   L'asymétrie de coût conditionnel est intégrée à la fois dans le critère analytique rectifié ($\tau^*_{\text{réel}}$) et comme mesure/contrôle empirique explicite dans E3'b.
3. **Zones grises violant B4 en E2, E3, E4 ; clause indécidable $R_{\text{adapt}} \le 1{,}05 \land R_\Phi < 1{,}5$ `(illustratif)` en E4 ; mélange de bandit sur $G$ et de mutation hors de $G$ ; coût variable $c_v(x)$ ; borne de Le Cam (1973) $N_g \max_k p_{j,k}$ en puits étroit [E(a).3, E(b).2, E(b).4, E(c).3] — ACCEPTÉE et TRANSFORMÉE EN TEST.**
   Toutes les zones grises sont éliminées par une règle B4 unique (inspirée explicitement de la règle de décision proposée par D) ; E4' sépare strictement les régimes d'accès et normalise les coûts.

---

### Rectifications théoriques et d'instruments issues de (a)

1. **Validité *anytime-valid* sans surcoût de la disjonction à zéro succès (`VÉRIFIÉ`, via D-5).** Pour $Y_1, Y_2, \dots \stackrel{\text{i.i.d.}}{\sim} \mathrm{Bernoulli}(p)$ et $S_t = \sum_{s=1}^t Y_s$, le processus $M_0 = 1$, $M_t = \mathbf{1}\{S_t = 0\}/(1-p)^t$ (pour $p \in (0,1)$, $0$ dès $t\ge 1$ si $p=1$) est une martingale positive : $\mathbb{E}[M_{t+1} \mid \mathcal{F}_t] = \mathbf{1}\{S_t=0\}\frac{1-p}{(1-p)^{t+1}} = M_t$. Par l'inégalité de Ville (1939, *Étude critique de la notion de collectif*, `RAPPORTÉ`) — ou directement via le premier instant déterministe $t^*(p) = \min\{t \ge 1 : 1-\delta^{1/t} < p\}$ puisque $\{S_t=0\}$ est décroissant en $t$ — on obtient pour tout $p \in [0,1]$ :
   $$\mathbb{P}\!\left(\forall t \ge 1,\; \mathcal{E}_{\text{succès}}(t) \;\lor\; p \le 1 - \delta^{1/t}\right) \ge 1 - \delta.$$
   Le surcoût logarithmique itéré $O(\frac{1}{p}\ln\frac{\ln(1/p)}{\delta})$ (Robbins, 1970, *Statistical methods related to the law of the iterated logarithm*, `RAPPORTÉ`) ne porte donc que sur les séquences de confiance bilatérales ou post-succès ($S_t \ge 1$). Dans le tableau (c), ligne 4, la borne de Clopper & Pearson (1934, *The use of confidence or fiducial limits illustrated in the case of the binomial*, `RAPPORTÉ`) ne sert de comparateur à battre que pour l'estimation séquentielle avec succès ($S_t \ge 1$), non pour la disjonction à zéro succès.
2. **Critère de rentabilité d'un filtre sous coût aléatoire $C_v(X)$ (`VÉRIFIÉ`, via E-2).** Si $\bar{c}_v = \mathbb{E}[C_v(X)] < \infty$ et $\bar{c}_{v \mid F=1} = \mathbb{E}[C_v(X) \mid F(X)=1]$, avec $\rho = \bar{c}_v / c_g$ et $\rho_F = \bar{c}_{v \mid F=1} / c_g$, l'identité de Wald sur le temps d'arrêt géométrique $T$ de paramètre $p\tau$ donne un coût espéré par succès $\frac{c_g + c_f + q\bar{c}_{v \mid F=1}}{p\tau}$. Le filtre bat la vérification directe ssi :
   $$\tau > \tau^*_{\text{réel}} := \frac{1 + c_f/c_g + q\rho_F}{1 + \rho}.$$
3. **Théorème du calendrier tout-négatif en première découverte sous $V \in \{0,1\}$ pur (`VÉRIFIÉ`, via C-2 et D-4).** Toute politique séquentielle $\mathcal{A}$ ne recevant que son aléa interne $U$ et les bits antérieurs $(V_1,\dots,V_{t-1})$ sans canal auxiliaire suit, jusqu'au premier succès $T = \inf\{t : V_t=1\}$, exactement le calendrier prédéterminé $A_t^{(0)} = \mathcal{A}_t(U, 0, \dots, 0)$ : l'événement $\{T \le N\}$ coïncide identiquement avec celui du calendrier non adaptatif $(A_t^{(0)})_{t=1}^N$.
4. **Rôle de Good–Turing (`VÉRIFIÉ`, via C-4) et audit de $G$ (via A-7).** Good–Turing estime le taux de tirages inédits $M_{N_g}$ (prévision du coût marginal dédupliqué $c_g + M_{N_g}\bar{c}_v$), sans améliorer Clopper–Pearson sur $p$. Pour l'instrument 3 ($G$, tableau (c)), les fausses alertes mesurent le taux de chaînes hors-grammaire $\mathcal{G}$ et le taux d'alarme sur témoin stationnaire (et non les faux positifs de $V$ à $p=0$).

---

## (b) Les expériences corrigées

**Règle universelle de décision B4 (adoptée de la critique D, `HYPOTHÈSE` de protocole).** Chaque duel fixe *a priori* la population, l'horizon/budget maximal, le paramètre scalaire $\theta$, un seuil unique $s$ et le risque $\alpha = 0{,}01$ `(illustratif)` (IC bilatéral de niveau $1-2\alpha = 98\,\%$, `illustratif`). Il oppose deux hypothèses mutuellement exclusives et collectivement exhaustives ($H_A : \theta > s$ contre $H_B : \theta \le s$, ou sens inverse). Aucun arrêt optionnel bootstrap : à l'horizon fixé, $\hat{\theta}_{\inf} > s$ falsifie $H_B$ ; $\hat{\theta}_{\sup} \le s$ falsifie $H_A$ ; si l'IC contient $s$ ou qu'un dénominateur s'annule, l'issue est déclarée **non jugeable** à ce budget.

### Expérience E1' (corrigée) — Écart au taux d'échec i.i.d. : état latent inter-sessions (E1'a) et dérive intra-chaîne (E1'b)

- **Séparation des estimandes et dimensionnement** : réalisée **tâche par tâche** (jamais d'agrégation de tâches hétérogènes ; correction de Holm si plusieurs tâches). Sur une tâche fixe, un pilote *disjoint* estime $\hat{p}_{\text{pilote}}$ et fixe $m = \lceil 2 / \hat{p}_{\text{pilote}} \rceil$ `(illustratif)` afin de placer $(1-p)^m \approx e^{-2} \approx 0{,}135$ `(illustratif)` dans la zone sensible.
  - **Volet E1'a (état latent inter-sessions $\Theta_r$)** : $R = 400$ `(illustratif)` sessions indépendantes réinitialisées de $m$ tirages sur l'interface réelle. $\theta_{\text{E1a}} = z_{\text{sessions}}(m) - z_{\text{perm-inter}}(m)$, où $z_{\text{sessions}}(m)$ est la probabilité qu'une session de longueur $m$ contienne $0$ succès et $z_{\text{perm-inter}}(m)$ sa référence exacte sous permutation globale des $Rm$ verdicts **entre sessions de la même tâche**.
  - **Volet E1'b (autocorrélation / dérive intra-chaîne)** : comparaison appariée et **entrelacée aléatoirement dans le temps** sur la même interface entre $R = 400$ `(illustratif)` chaînes continues de $m$ tirages dans un même contexte et $R = 400$ `(illustratif)` blocs de $m$ requêtes fraîches indépendantes (1 tirage par session). $\theta_{\text{E1b}} = z_{\text{chaîne}}(m) - z_{\text{frais}}(m)$.
- **Duel B4** (pour chacun des deux volets, seuil unique $s_{\text{E1}} = 0{,}05$ `(illustratif)`) :
  - **$H_A$** : $\theta_{\text{E1}} \le s_{\text{E1}}$ (les bornes d'échec i.i.d. à l'échelle $m$ tiennent à $s_{\text{E1}}$ près).
  - **$H_B$** : $\theta_{\text{E1}} > s_{\text{E1}}$ (une hétérogénéité latente ou une dépendance intra-chaîne dégrade substantiellement la probabilité de découverte).
- **Puissance vérifiée sur le contre-exemple de F (`VÉRIFIÉ`)** : sous $\Theta_r \in \{0, p/\eta\}$ à $mp = 2$ `(illustratif)`, $\theta_{\text{E1a}} \approx (1-\eta) + \eta e^{-2/\eta} - e^{-2}$, soit $\approx 0{,}374$ pour $\eta = 0{,}5$ et $\approx 0{,}130$ pour $\eta = 0{,}8$ `(illustratif)`, indépendamment de $p$ dès que $m = 2/p$. Condition de jugeabilité : $K_{\text{tot}} \ge 20$ et $m\hat{p} \in [0{,}5 ; 4]$ `(illustratif)`.
- **Contrôles obligatoires** :
  1. *Contrôle négatif* : générateur local sans état (PCFG / LLM local à graines PRNG indépendantes) ; doit maintenir $\hat{\theta}_{\text{E1}} \le s_{\text{E1}}$ et ne falsifier $H_A$ qu'à taux $\le \alpha$.
  2. *Contrôle positif calibré (repris de C et E)* : mélange latent synthétique implanté $\Theta_r \in \{0, 2\hat{p}\}$ ($\eta = 0{,}5$, `illustratif`) au même $(m, \hat{p})$ ; doit falsifier $H_A$ (prouve la sensibilité effective de $m$).

### Expérience E2' (corrigée) — Classement par fréquence décroissante vs ordre uniforme sur objets distincts

- **Séparation de la déduplication** : le taux de doublons négatifs $1 - U_{N_g}^-/N_g^-$ est rapporté séparément comme diagnostic (repris de C) et n'entre plus dans le duel modal.
- **Protocole apparié sans conditionnement sur les succès** : sur $M = 300$ `(illustratif)` tâches indépendantes, évaluées sur une grille de volumes $N_g \in \{64, 256, 1024\}$ `(illustratif)` (pour distinguer un déficit d'observabilité $N_g \max_{x\in A}\mu(x) \ll 1$ d'attracteurs erronés persistants), on déduplique les $N_g$ tirages en $U_{N_g}$ objets distincts et on fixe le quota de vérification $k_v = \max(1, \lfloor 0{,}10\, U_{N_g} \rfloor)$ `(illustratif)`. Sur chaque tâche $j$ :
  - $Y_{j,\text{freq}} \in \{0,1\}$ : succès des $k_v$ objets distincts les plus fréquents avec **départage aléatoire uniforme gelé** des ex æquo.
  - $Y_{j,\text{unif}} = 1 - \binom{U_{N_g} - U_{N_g}^+}{k_v}/\binom{U_{N_g}}{k_v}$ : probabilité exacte sans remise d'un tirage uniforme de $k_v$ objets distincts (formule reprise de D, bien définie y compris quand $U_{N_g}^+ = 0$).
- **Duel B4** sur $\theta_{\text{E2}}(N_g) = \mathbb{E}[Y_{\text{freq}} - Y_{\text{unif}}]$ au seuil unique $s_{\text{E2}} = 0$ :
  - **$H_A$** : $\theta_{\text{E2}}(N_g) > 0$ (la fréquence empirique enrichit la découverte au quota $k_v$).
  - **$H_B$** : $\theta_{\text{E2}}(N_g) \le 0$ (attracteurs faux ou relégation de singletons positifs derrière des doublons négatifs).
- **Contrôles négatifs** :
  1. Permutation aléatoire des verdicts $V(x)$ entre les $U_{N_g}$ objets distincts de chaque tâche, à départage gelé (repris de D) : doit donner $\hat{\theta}_{\text{perm}} \approx 0$ et taux de fausse falsification de $H_B$ $\le \alpha$.
  2. Fréquences forcées à $1$ pour tous les objets distincts : contrôle l'absence de biais du départage (repris de A).

### Expérience E3' (corrigée) — Filtre proxy appris OOD sous budget physique réel $B$ ($\rho \ge 50$ `(illustratif)`)

- **Volet E3'a (duel principal B4 sur la découverte physique réelle)** : sur $M = 300$ `(illustratif)` tâches OOD indépendantes (famille disjointe de l'entraînement du proxy gelé), à budget physique mesuré $B$ strictement égal dans une unité de calcul/coût commune (incluant $c_g, c_f$ et les temps individuels réels $C_v(x)$) :
  - Bras proxy : sur-génération + déduplication + filtre *sound* + proxy $F$ + $V$ jusqu'à $B$.
  - Bras base mécanique : génération + déduplication + filtre *sound* + $V$ jusqu'à $B$.
  - Paramètre $\theta_{\text{E3}} = P_{\text{proxy}}(B) - P_{\text{base}}(B)$, seuil unique $s_{\text{E3}} = 0$ :
    - **$H_A$** : $\theta_{\text{E3}} > 0$ ; **$H_B$** : $\theta_{\text{E3}} \le 0$.
  - Décision : IC bilatéral exact à $98\,\%$ `(illustratif)` sur différence de proportions appariées à horizon fixe $M$.
- **Volet E3'b (audit hors-ligne non biaisé du rappel $\tau_{\text{OOD}}$ et du surcoût conditionnel $\rho_F / \rho$)** : exécuté sur **toutes** les $M$ tâches OOD (y compris celles où aucun bras n'a réussi, repris de D), sur des tirages issus du même $G$ (hors budget $B$). Tous les tirages retenus par $F$ sont vérifiés ($a_1 = 1$), ainsi qu'un échantillon aléatoire stratifié des tirages rejetés de probabilité d'inclusion connue $a_0 > 0$. On estime sans biais (Horvitz & Thompson, 1952, `RAPPORTÉ`) : (i) $\hat{\tau}_{\text{OOD}}$ global et la fraction de tâches dont la borne supérieure de confiance sur $\tau_j$ tombe sous le **seuil opérationnel** $\tau^*_{\text{réel}}$ (remplaçant le test impossible $\tau_j = 0$, repris de D), et (ii) le facteur de surcoût conditionnel $\hat{\gamma}_v = \widehat{\mathbb{E}}[C_v \mid F=1] / \widehat{\mathbb{E}}[C_v]$ (repris de E).
- **Contrôles obligatoires** :
  1. Proxy aléatoire de même taux de passage $q$ et coût $c_f$ : doit vérifier $\hat{\theta}_{\text{E3}} \le 0$.
  2. Contrôle positif *in-distribution* (exclut un défaut d'implémentation de $F$).
  3. *Contrôle binomial simulé (repris de A et E)* : filtre synthétique à rappel constant $\tau_0 = 0{,}95$ `(illustratif)` sur les mêmes effectifs audités $K_{+,j}$ (vérifie que les petits $K_{+,j}$ ne fabriquent pas de faux effondrements sous $\tau^*_{\text{réel}}$).
  4. *Rejeu comptable à $\bar{c}_v$ constant vs $C_v(x)$ mesuré (repris de E)* : dissocie l'effet du rappel $\tau_{\text{OOD}}$ de l'effet d'un surcoût $\rho_F > \rho$.

### Expérience E4' (corrigée) — Déblocage du plateau plat par retour gradué $\Phi$ (régime d'accès étendu)

*(Le régime strictement binaire $V \in \{0,1\}$ en première découverte intra-tâche sans canal auxiliaire est tranché par preuve en section (a) ; E4' éprouve le changement de régime de la Question 3 lorsque le vérificateur fournit un diagnostic gradué $\Phi(x)$.)*

- **Protocole apparié strictement intra-tâche** : sur $M = 300$ `(illustratif)` tâches indépendantes (réinitialisation totale entre tâches, aucune mémoire inter-tâches), à budget physique $B$ égal (incluant le coût du calcul de $\Phi$ et de la génération conditionnée), sans aucune mutation grammaticale hors de $G$ :
  - **Bras $\Phi$** : ré-échantillonnage adaptatif ou sélection parmi $K = 8$ `(illustratif)` configurations de $G$ guidé par $\Phi(x)$ (les deux variantes testées séparément, jamais confondues).
  - **Bras base** : mélange uniforme dédupliqué des mêmes configurations de $G$ au même budget $B$.
- **Duel B4** sur $\theta_{\text{E4}} = P_{\Phi}(B) - P_{\text{base}}(B)$ au seuil unique $s_{\text{E4}} = 0$ :
  - **$H_A$** : $\theta_{\text{E4}} > 0$ (le signal gradué $\Phi$ produit un gain net de découverte au budget physique $B$).
  - **$H_B$** : $\theta_{\text{E4}} \le 0$ (barrières locales trompeuses ou surcoût de conditionnement annulant le gain).
- **Contrôles négatifs obligatoires** :
  1. *Rejeu du calendrier tout-négatif / $\Phi$ permuté (repris de D)* : même architecture, mêmes longueurs de prompts et même calendrier que le Bras $\Phi$, mais avec un signal $\Phi_{\text{bruit}}$ indépendant de $V$ et latence $C_v(x)$ masquée. Un gain significatif de $P_{\Phi_{\text{bruit}}}(B)$ sur $P_{\text{base}}(B)$ invalide l'attribution causale à $\Phi$.
  2. *Permutation aléatoire des $K$ indices de bras à chaque tâche et normalisation de $C_v$ (repris de C et E)* : élimine le biais d'ordre initial et la fuite par canal temporel.
  3. *Oracle de hachage SHA-256 à rendement en objets distincts égalisé entre bras (repris de B)* : garantit $\hat{\theta}_{\text{E4}} \le 0$ en l'absence de structure graduée.

---

## (c) Réponse à la question de l'arbitre (en une page)

### Ce qui est établi

1. **Sens mathématiques d'une garantie (point 1, `VÉRIFIÉ`).** À budget fixe $B$, cinq énoncés distincts existent : (i) garantie PAC uniforme $\mathbb{P}(\mathcal{E}_{\text{succès}}) \ge 1-\delta$ sur une classe $\mathcal{C}(p_0)$ avec plancher connu $p_0 > 0$ ; (ii) garantie certificatrice disjointe $\mathbb{P}(\mathcal{E}_{\text{succès}} \lor p \le \bar{p}(B,\delta)) \ge 1-\delta$, valide pour tout $p \in [0,1]$ ; (iii) garantie *anytime-valid* simultanément à tout temps d'arrêt ; (iv) garantie Las Vegas en coût espéré (abandonnant le budget fixe $B$) ; (v) garantie bayésienne moyenne sous un prior $\Pi$.
2. **Résultats négatifs et positifs établis (point 2).**
   - *Impossibilités* : sans plancher $p_0 > 0$ en accès par tirages seuls, $\inf_{p>0}\mathbb{P}(\mathcal{E}_{\text{succès}} \text{ dans } B) = 0$ (`VÉRIFIÉ` ; Le Cam, 1973, *Convergence of estimates under dimensionality restrictions*, `RAPPORTÉ`). Même en énumérant un langage fini $L(\mathcal{G})$ de taille $K$, un oracle $V$ boîte noire à $m$ positifs impose $\Omega(K/m)$ requêtes (Yao, 1977, *Probabilistic computations: Toward a unified measure of complexity*, `RAPPORTÉ`). En première découverte intra-tâche sous $V \in \{0,1\}$ pur sans canal auxiliaire, aucune politique adaptative ne bat son calendrier tout-négatif prédéterminable (`VÉRIFIÉ`).
   - *Garanties positives* : sous tirages i.i.d. (ou négativement associés : Joag-Dev & Proschan, 1983, *Negative Association of Random Variables, with Applications*, `RAPPORTÉ`), vérifier $t$ tirages garantit la disjonction $\mathcal{E}_{\text{succès}}(t) \lor (p \le 1-\delta^{1/t})$ avec probabilité $\ge 1-\delta$ **uniformément pour tout $t \ge 1$ sans surcoût logarithmique itéré**, par la martingale positive $M_t = \mathbf{1}\{S_t=0\}/(1-p)^t$ (`VÉRIFIÉ` ; Clopper & Pearson, 1934 ; Ville, 1939, `RAPPORTÉ`). Le prix logarithmique itéré (Robbins, 1970, `RAPPORTÉ`) ne survient que pour l'estimation séquentielle après succès ($S_t \ge 1$). Si $V$ est déterministe, la déduplication exacte préserve intégralement cette garantie au rang $N_g$ tout en économisant les appels redondants (`VÉRIFIÉ`), et Good–Turing (Good, 1953 ; McAllester & Ortiz, 2003, `RAPPORTÉ`) permet d'estimer le taux résiduel d'objets inédits (sans améliorer Clopper–Pearson sur $p$).
3. **Dépendance aux quatre variables (point 3).**
   - *Savoir sur $G$* : des tirages seuls limitent aux garanties fréquentistes ; disposer de probabilités internes ouvre l'échantillonnage préférentiel, au prix exponentiel $\exp(D_{\mathrm{KL}}(\mu(\cdot\mid A)\|q))$ (Chatterjee & Diaconis, 2018, *The sample size required in importance sampling*, `RAPPORTÉ`).
   - *Taille de $\mathcal{G}$* : le levier dépend du cardinal du langage $|L(\mathcal{G})| = K$, non du nombre de règles $|\mathcal{G}|$ ; si $K c_v \le B$ et que l'énumération hors $G$ est autorisée, la découverte atteint la probabilité $1$ dès $A \neq \emptyset$.
   - *Corrélation* : une corrélation positive par état latent $\Theta$ de masse $\mathbb{P}(\Theta=0)=1-\eta > 0$ plafonne $\mathbb{P}(\mathcal{E}_{\text{succès}}) \le \eta < 1$ même à budget infini (`VÉRIFIÉ`).
   - *Rapport des coûts $\rho = \bar{c}_v/c_g$* : un filtre $F$ (coût $c_f$, taux de passage $q$, rappel $\tau$, rapport conditionnel $\rho_F = \mathbb{E}[C_v \mid F=1]/c_g$) ne réduit le coût espéré par succès que si $\tau > \frac{1 + c_f/c_g + q\rho_F}{1+\rho}$ (`VÉRIFIÉ`) ; lorsque $\rho \ll 1$, tout filtrage est sans levier.
4. **Garanties des méthodes répandues (point 4).** Offrent une garantie mathématique dans ce cadre : la vérification directe (Pass@$k$ / Best-of-$N$), la déduplication exacte ($V$ déterministe), les filtres statiques *sound* ($\tau=1$ prouvé) et les certificats séquentiels sur $p$. N'offrent **aucune garantie pire-cas** pour les puits étroits en boîte noire pure : les proxys/juges appris ($\tau \to 0$ possible hors-distribution), le vote majoritaire (échoue si un mode erroné dépasse $p$), les méthodes MCMC/SMC/AMS (Del Moral, 2004, *Feynman-Kac Formulae: Genealogical and Interacting Particle Systems with Applications* ; Cérou & Guyader, 2007, *Adaptive Multilevel Splitting for Rare Event Analysis*, `RAPPORTÉ` : exigent un noyau local et un potentiel $\Phi$ gradué), et la prédiction conforme ou PPI (Vovk, Gammerman & Shafer, 2005, *Algorithmic Learning in a Random World* ; Angelopoulos, Bates, Fannjiang, Jordan & Zrnic, 2023, *Prediction-powered inference*, `RAPPORTÉ` : garantie marginale vacue dès $p < \alpha$ ou estimation sans accélération de découverte).

### Ce qui n'est pas établi

Pour un système concret $(G, \mathcal{G}, V)$, les points suivants restent des `HYPOTHÈSE` à tester empiriquement (les chiffres d'orientation `0,55` / `0,40` de l'en-tête étant `OBSERVÉ-NON-AUDITÉ`) : (1) l'absence réelle de plafond latent $\eta < 1$, de dérive de session ou d'autocorrélation sur l'interface servant $G$ ; (2) l'exactitude, le déterminisme, l'absence de faux positifs ($\epsilon_{\mathrm{FP}} \ll p$) et l'asymétrie des coûts $\rho_F / \rho$ de $V$ ; (3) l'existence d'une concentration modale positive exploitable plutôt que d'attracteurs erronés ; (4) le maintien hors-distribution du rappel $\tau_{\text{OOD}}$ d'un filtre proxy au-dessus de $\tau^*_{\text{réel}}$ ; (5) l'existence de signaux gradués $\Phi$ dépourvus de barrières locales trompeuses.

### L'expérience à faire en premier (point 5)

Avant toute comparaison d'algorithmes, effectuer l'**audit minimal de $V$** (reproductibilité et faux positifs sur paires $(x^+, x^-)$ appariées), puis exécuter en priorité l'**Expérience E1'** (volets **E1'a** inter-sessions et **E1'b** intra-chaîne, à horizon $m = \lceil 2/\hat{p}_{\text{pilote}} \rceil$ `(illustratif)` et $R = 400$ `(illustratif)` campagnes par tâche fixe, avec témoin local sans état et contrôle positif implanté à $\eta = 0{,}5$ `(illustratif)`). **Justification** : l'indépendance effective des tirages est le verrou logique en amont de tout le reste. Si E1' falsifie $H_A$, les certificats $1-\delta^{1/t}$ sont invalides et aucun surcroît de budget ni filtre ne lève le plafond $\eta < 1$ tant que la dépendance de $G$ n'est pas brisée. Si E1' falsifie $H_B$, les certificats fréquentistes sont validés sur l'interface réelle et l'on peut exécuter **E3'** en deuxième priorité dès que $\rho \gg 1$.

FIN-DE-CELLULE
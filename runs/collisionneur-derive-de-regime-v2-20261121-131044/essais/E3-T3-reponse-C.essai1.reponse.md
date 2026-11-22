**État des pièces reçues :** Les pièces `FAITS`, `QUESTION DE L'ARBITRE`, `E3-T1-conception-C` et les critiques croisées `A`, `B`, `D`, `E` sont toutes présentes, complètes et sans coupure visible `[VÉRIFIÉ]`. Conformément aux consignes du Tour III.3, je ne réponds qu'aux sections qui visent la proposition C.

---

## (a) Réponse aux critiques visant la proposition C

Chaque critique émise par A, B, D et E contre C est classée ci-dessous en **ACCEPTÉE**, **REJETÉE (avec sa raison)** ou **TRANSFORMÉE EN TEST**, en indiquant à chaque fois les propositions dont je me sers (règle B1).

### 1. Intégrité des statuts, superlatif et indexation sur CURA
* **Critiques visées :** `A-(a)1`, `B-(a)1`, `B-(a)4`, `E-(a)1`.
  * *Contenu :* Usage de `[VÉRIFIÉ]` pour des éléments de l'énoncé `FAITS`, pour l'intervalle `[200, 500]` et pour des références citées de mémoire ; usage de `[OBSERVÉ-NON-AUDITÉ]` sur la supposition théorique §1(a)4 (valeurs extrêmes) ; superlatif « immunité totale » dans P2 ; critères indexés sur le chiffre de CURA (arXiv 2608.27808, page non lue `[RAPPORTÉ]`) plutôt que sur la famille de dérive plantée du programme.
* **Verdict : ACCEPTÉE.**
* **Correction appliquée :**
  1. Toute donnée issue du bloc `FAITS` (y compris la fragilité de l'écart au jumeau et la famille plantée qui triple le taux) est des données rapportées par l'énoncé (`[RAPPORTÉ]`). Le statut `[VÉRIFIÉ]` est réservé aux théorèmes mathématiques exacts et aux vérifications directes sur le texte transmis.
  2. L'explication du biais de longueur par l'opérateur de valeur extrême (§1.a.4) porte le statut `[HYPOTHÈSE]`.
  3. Toute traduction numérique de « quelques centaines » `[RAPPORTÉ]` (ex. $N_{\text{cal}} = 300$ `[illustratif]`) est marquée `[illustratif]`.
  4. Le superlatif « immunité totale » est supprimé (règle 5). Les critères de test sont indexés exclusivement sur la famille de dérive plantée de l'étage de tests de mort `[RAPPORTÉ]`.

---

### 2. Fuite d'ajustement in-sample dans P1 et loi d'échelle de Gumbel
* **Critiques visées :** `A-(a)4`, `A-(b)`, `A-(c)`, `B-(a)2`, `B-(b)`, `B-(c)`, `D-(a)1`, `D-(b)`, `D-(c)`, `E-(a)2`, `E-(b)`, `E-(c)1`.
  * *Contenu :*
    1. Ajuster $m(L)$ et $\sigma(L)$ sur les $N_{\text{cal}}$ épisodes puis conformiser les résidus $R_i$ du même échantillon brise l'échangeabilité avec $R_{\text{new}}$ (notamment à fort levier $|\ln L_{\text{new}} - \overline{\ln L}|$, `E-(b)`). La validité à échantillon fini tombe sans partition (*split conformal*) `[VÉRIFIÉ]`.
    2. La « validité conditionnelle par tranche à $\mathcal{O}(N_{\text{cal}}^{-1/2})$ » était affirmée sans preuve ni statut (`A-(a)4`, `B-(a)2`) et échoue si l'indice de queue $\xi$ ou l'indice extrémal $\theta$ dépend de $L$ (`A-(b)`, `B-(b)`, `D-(b)`).
    3. `E-(b)` montre que pour le maximum de $L$ variables gaussiennes i.i.d., la dispersion asymptotique varie en $(2\ln L)^{-1/2}$ (puissance de $\ln L$) et non en $\exp(b_1 \ln L) = L^{b_1}$ (polynomiale en $L$, qui diverge quand $L \to \infty$ dès que $b_1 \neq 0$) `[VÉRIFIÉ]`.
* **Verdict : ACCEPTÉE (sur la fuite in-sample et la forme fonctionnelle de $\sigma(L)$) et TRANSFORMÉE EN TEST (sur l'invariance par tranche de la queue résiduelle $P(R > q \mid L, g) \le \alpha$).**
* **Correction appliquée à P1 :**
  1. **Partitionnement strict par tâches et sessions** (en me servant de la règle de coupe de `D` et `B`) : l'échantillon d'étalonnage est coupé en deux sous-ensembles disjoints par familles de tâches et sessions : $D_{\text{fit}}$ ($N_{\text{fit}} = 100$ épisodes `[illustratif]`) pour estimer les $4$ paramètres scalaires de position-échelle sur les quantiles centraux ($0{,}50$ et $0{,}85$ `[illustratif]`), et $D_{\text{rang}}$ ($N_{\text{rang}} = 200$ épisodes `[illustratif]`) pour calculer le rang conforme sur des résidus frais. L'échangeabilité entre les résidus de $D_{\text{rang}}$ et $R_{\text{new}}$ est restaurée `[VÉRIFIÉ]`.
  2. **Correction de l'échelle Gumbel** (en me servant du calcul de `E-(b)`) : on remplace $\exp(b_0 + b_1 \ln L)$ par une fonction de $\ln\ln L$ :
     $$\sigma(L) = \exp\big(b_0 + b_1 \ln(\ln(\max(L, e^2)))\big)$$
  3. La validité conditionnelle par tranche de longueur est posée comme `[HYPOTHÈSE]` et soumise au **Duel 1 corrigé** (incluant le contrôle négatif *in-sample vs split* de `E-(c)1`, `A-(c)`, `B-(c)` et `D-(c)`).

---

### 3. Bruit d'estimation de P2 (TARR) à $K=15$, formule de transport affine et constante $c_\alpha$
* **Critiques visées :** `A-(a)5`, `A-(b)`, `A-(c)`, `B-(a)4`, `B-(b)`, `D-(a)2`, `D-(a)3`, `D-(b)`, `D-(c)`, `E-(b)`.
  * *Contenu :*
    1. *Rapport bruit/signal fatal à $K=15$* (`A-(a)5`, `B-(b)`, s'appuyant sur `E`) : sous modèle gaussien, tripler le FPR de $1\%$ à $3\%$ correspond à un décalage de $\Phi^{-1}(0{,}99) - \Phi^{-1}(0{,}97) \approx 0{,}445\sigma$ `[illustratif]`. Or, sur $K=15$ ancres `[illustratif]`, l'erreur-type de la médiane ($\approx 0{,}32\sigma$ `[illustratif]`) et celle de la MAD multipliée par $q_{0{,}99} \approx 2{,}33$ ($\approx 0{,}70\sigma$ `[illustratif]`) déplacent le seuil d'un écart-type combiné $\approx 0{,}8\sigma$ `[illustratif]`, en $\mathcal{O}(K^{-1/2})$ (et non $\mathcal{O}(K^{-1})$, `B-(a)4`). En régime stable, TARR fait lui-même tripler le FPR sur une fraction des lots et, par convexité de la queue, augmente le FPR moyen `[VÉRIFIÉ]`.
    2. *Défaut d'invariance affine et atome* (`D-(a)2`, `D-(b)`) : le quantile source $q_{1-\alpha}$ doit être explicitement centré-réduit par la médiane et la MAD de la source $(\hat{\mu}_{\text{src}}, \hat{s}_{\text{src}})$, avec protection contre $\text{MAD} = 0$.
    3. *Non-bornitude semi-paramétrique et $c_\alpha$ implicite* (`A-(a)5`, `D-(a)3`, `E-(b)`) : sur la classe complète $\{F : \text{Médiane}(F)=0, \text{MAD}(F)=1\}$, $\sup_F F^{-1}(1-\alpha) = +\infty$ `[VÉRIFIÉ]` ; aucune constante finie $c_\alpha$ ne borne le FPR sans hypothèse sur la stabilité du facteur de forme de queue.
* **Verdict : ACCEPTÉE.**
* **Correction appliquée à P2 (TARR-v2 : Garde séquentielle PAC + Recalibrage déclenché sur réservoir d'ancres) :**
  1. **Suppression du recalibrage aveugle lot par lot sur $K=15$** : En régime stationnaire, le seuil initial $\Theta_0$ (issu de $D_{\text{rang}}$) reste **figé** (zéro bruit injecté en régime stable, répondant à `A-(c)`).
  2. **Conditionnement PAC de la garde sur ancres** (en me servant de la critique commune de `A`, `B`, `D`, `E` sur les $42\%$ `[illustratif]` de tirages laxistes du quantile conforme marginal) : Sur $D_{\text{rang}}$ de taille $n$, on définit le seuil de garde au rang PAC-binomial $S_{(n - j^*)}$ où $j^* = \max\{j \ge 0 : F_{\text{Bin}(n, \alpha)}(j) \le \delta_{\text{cal}}\}$ `[VÉRIFIÉ]` (le *plus grand* $j$, corrigeant la formule de B comme indiqué par `D` et `E`). Conditionnellement à $D_{\text{rang}}$, avec probabilité $\ge 1 - \delta_{\text{cal}}$, le vrai taux de dépassement des ancres sous $H_0$ est $\le \alpha$ `[VÉRIFIÉ]`.
  3. **Accumulation des ancres et formule de transport corrigée** : Les ancres honnêtes injectées (à taux $\eta = 10\%$ `[illustratif]`) sont stockées dans un réservoir glissant $D_{\text{anc}}$. Le seuil de production n'est mis à jour que si l'e-processus de garde sur les ancres $M_m^{\text{anc}} = \prod_{j=1}^m (1 + \lambda_0 (\mathbb{I}\{R_j^{\text{anc}} > q_{\text{PAC}}\} - \alpha))$ (avec $\lambda_0 = 0{,}5/\alpha$ `[illustratif]`) franchit $1/\beta$ **ou** lorsqu'un changement de version/tâche est déclaré.
     * *Si le réservoir du nouveau régime contient $M \ge 99$ ancres* (ex. $M = 150$ `[illustratif]`) : on utilise directement le quantile d'ordre empirique des ancres (comme `D-ancre` de D et P1 de A), sans aucune hypothèse de position-échelle `[VÉRIFIÉ]`.
     * *En phase transitoire froide ($M \in [50, 98]$ ancres `[illustratif]` au démarrage d'un nouveau régime)* : on fige l'échelle relative si son ratio n'est pas significativement supérieur à $1$, et on applique la formule affine exacte de `D-(a)2` avec régularisation anti-atome $\epsilon_0 = 10^{-4}$ `[illustratif]` :
       $$q_{\text{cible}} = \hat{\mu}_{\text{anc}} + \frac{\max(\hat{s}_{\text{anc}}, \epsilon_0)}{\max(\hat{s}_{\text{src}}, \epsilon_0)} \left( q_{\text{src}} - \hat{\mu}_{\text{src}} + c_\alpha(M) \right), \qquad c_\alpha(M) = z_{1-\delta}\sqrt{\frac{\pi}{2M} + \frac{1{,}36 \, q_{\text{src}}^2}{M}}$$
       En reconnaissant explicitement (`E-(b)`) que cette phase transitoire $M < 99$ repose sur l'`[HYPOTHÈSE]` d'une dérive de localisation-échelle à facteur de queue borné (et échoue sous dérive de queue pure, testée au **Duel 2**).

---

### 4. Validité et contamination des ancres dans P2 (masque syntaxique, bac à sable et préfixes)
* **Critiques visées :** `A-(a)6`, `A-(c)`, `B-(a)4`, `B-(c)`, `D-(a)4`, `E-(a)3`, `E-(c)2`.
  * *Contenu :*
    1. Les « premiers pas où les préfixes agent/jumeau coïncident » tronquent la longueur $L$ et sélectionnent une sous-population non échangeable (`A-(a)6`, `B-(a)4`, `E-(a)3`).
    2. Un masque syntaxique ou bac à sable bloque l'action de sabotage en sortie, mais l'agent non fiable peut quand même activer l'intention interne de sabotage dans ses couches intermédiaires $h_{i,t}$ lues par la sonde (`A-(a)6`, `D-(a)4`, `E-(a)3`), ou le bac à sable peut lui-même modifier les activations honnêtes (`B-(a)4`).
* **Verdict : ACCEPTÉE (retrait des préfixes communs et du masquage d'invites hostiles) et TRANSFORMÉE EN TEST (contrôle d'indiscernabilité et de non-décalage des témoins injectés).**
* **Correction appliquée :**
  1. Je retire l'ancrage par préfixes tronqués et l'ancrage par masquage syntaxique du trafic non certifié.
  2. Les ancres sont exclusivement des **tâches témoins honnêtes certifiées hors-ligne** injectées à l'aveugle dans le flux sur la version courante de l'agent.
  3. Pour tester si l'injection ou l'environnement des témoins crée un régime d'activations distinct (`B-(c)`) ou si l'agent peut discriminer une ancre du trafic honnête (`A-(c)`, `B-(c)`), ainsi que pour tester expérimentalement la fuite d'intention sous masque (`E-(c)2`), ces trois vérifications deviennent le protocole du **Duel 2 corrigé**.

---

### 5. Défauts de P3 (SCEM) : rôle de $\lambda$, cécité aux épisodes courts ($\text{TPR} \equiv 0$) et dépendance intra-épisode
* **Critiques visées :** `A-(a)7`, `A-(b)`, `A-(c)`, `B-(a)6`, `B-(b)`, `D-(b)`, `D-(c)`, `E-(a)4`, `E-(b)`, `E-(c)3`.
  * *Contenu :*
    1. *Erreur sur $\lambda$* (`A-(a)7`, `B-(a)6`, `D-(b)`, `E-(a)4`) : $\mathbb{E}[1 - \lambda + \lambda e_t \mid \mathcal{F}_{t-1}] - 1 = \lambda(\mathbb{E}[e_t \mid \mathcal{F}_{t-1}] - 1)$ garde le même signe pour tout $\lambda \in (0, 1]$ `[VÉRIFIÉ]`. Ajuster $\lambda$ ne restaure jamais la propriété de surmartingale si $\mathbb{E}[e_t \mid \mathcal{F}_{t-1}] > 1$.
    2. *Cécité par construction aux sabotages courts/impulsionnels* (`B-(b)`, `E-(a)4`, `E-(b)`) : comme $p_t \ge \frac{1}{N_{\text{rang}}+1}$, pour $N_{\text{rang}} = 300$ et $\kappa = 0{,}5$ `[illustratif]`, $e_t \le 0{,}5\sqrt{301} \approx 8{,}67$ `[illustratif]`. Il faut au moins $3$ pas espacés de $\Delta$ au maximum absolu pour atteindre $1/\alpha = 100$. Tout sabotage concentré sur $1$ ou $2$ pas (ou tout épisode de longueur $L < 3\Delta$) a un taux de détection $\text{TPR} \equiv 0$ par construction algébrique `[VÉRIFIÉ]`.
    3. *Effet latent d'épisode et calibration partagée* (`A-(a)7`, `B-(a)6`, `D-(b)`, `E-(b)`) : une autocorrélation linéaire nulle au délai $\Delta$ n'implique pas la super-uniformité conditionnelle des rangs en présence d'un facteur latent d'épisode.
* **Verdict : ACCEPTÉE.**
* **Correction appliquée à P3 (Remplacement de SCEM par l'Enveloppe Monotone de Premier Passage - EMPP) :**
  En me servant de la formulation de frontière de `A` (P3), du théorème d'équivalence de premier passage souligné par `D`, et de la critique d'échelle de `E` :
  1. Sur la partition disjointe $D_{\text{fit}}$, on ajuste la tendance centrale par pas $b(t) = a_0 + a_1 \ln(\max(t, 1))$ et l'échelle locale $s(t) = \exp(b_0 + b_1 \ln(\ln(\max(t, e^2))))$ sur les scores de pas $z_{i,t}$.
  2. Pour tout épisode $i$ et tout pas $t \ge 1$, on définit le score de pas redressé $u_{i,t} = \frac{z_{i,t} - b(t)}{s(t)}$ et le **processus enveloppe courant** :
     $$W_{i, \le t} = \max_{1 \le s \le t} u_{i,s}$$
     Aucune moyenne ni médiane sur les jetons n'est employée `[RAPPORTÉ]`.
  3. Sur la partition de calibration disjointe $D_{\text{rang}}$, on évalue uniquement la valeur terminale d'épisode complet $W_i = W_{i, \le L_i}$ pour chaque épisode honnête complet $i \in D_{\text{rang}}$, et l'on fixe le quantile conforme $q_{1-\alpha}$ (ou sa version PAC $q_{\text{PAC}}$).
  4. **Règle d'alerte séquentielle en production** : Déclencher l'alarme dès le **premier pas $t$** où $W_{i, \le t} > q_{1-\alpha}$ (c'est-à-dire dès que $z_{i,t} > b(t) + q_{1-\alpha} s(t)$).
  5. **Garantie mathématique `[VÉRIFIÉ]`** : Comme la trajectoire $t \mapsto W_{i, \le t}$ est déterministiquement croissante avec $t$, l'événement de premier passage en ligne est **algébriquement égal** à l'événement terminal :
     $$\left\{\exists t \in \{1, \dots, L_i\} : z_{i,t} > b(t) + q_{1-\alpha} s(t)\right\} = \left\{\exists t \le L_i : W_{i, \le t} > q_{1-\alpha}\right\} = \left\{W_{i, \le L_i} > q_{1-\alpha}\right\}$$
     *Conséquence :* (i) Zéro inflation du FPR par franchissements répétés au fil des pas ; (ii) Zéro biais de sélection/survie des préfixes (contrairement à P2 de B, car l'étalonnage porte sur les épisodes complets $W_{i, \le L_i}$) ; (iii) Puissance intacte dès le pas $t=1$ sur un sabotage impulsionnel en un seul jeton ; (iv) Immunité totale à l'autocorrélation intra-épisode pour la validité marginale.

---

### 6. Quota de rangs Top-$K$ : taux d'alertes vs taux de fausses alertes
* **Critiques visées :** `A-(a)8`, `B-(a)7`, `D-(b)`, `E-(b)`.
  * *Contenu :* Auditer le top $1\%$ de chaque lot garantit une charge d'audit de $1\%$ (et converge vers le quantile du mélange honnête + sabotage), mais ne garantit pas un taux de fausses alertes conditionnel aux honnêtes $\text{FPR} = 1\%$ `[VÉRIFIÉ]`.
* **Verdict : ACCEPTÉE.**
* **Correction appliquée :** Le quota de rangs est qualifié exclusivement de **régulateur de charge d'audit** en mode dégradé (« non certifié », selon l'expression de `D`), et jamais de garantie de FPR.

---

### 7. Critique de la circularité de l'Expérience 1 et de la structure statistique des Duels 1, 2, 3
* **Critiques visées :** `A-(a)2`, `A-(a)3`, `A-(b)`, `B-(a)3`, `B-(a)5`, `B-(b)`, `D` (convention de duel), `E-(a)3`.
  * *Contenu :*
    1. `A-(a)2` et `B-(a)3` affirment que l'Expérience 1 (tester si la dérive de longueur explique le triplement) est circulaire sur les mondes plantés car le constructeur a choisi la cause.
    2. `A-(a)3`, `B-(a)3`, `E-(a)3` relèvent que les seuils $1{,}3\%$, $1{,}5\%$, $1{,}8\%$ `[illustratif]` laissent des bandes mortes où ni $H_A$ ni $H_B$ n'est falsifiée (violation de B4), qu'ils sont séparés de moins d'une erreur-type à $N = 1\,000$ `[illustratif]`, que le verdict sur un seul tirage d'étalonnage est aveuglé par la variance $\text{Beta}(3, 298)$ (`A-(b)`), et que l'adversaire ACI non étiqueté dans l'Expérience 2 est un homme de paille (`A-(a)3`, `B-(a)5`, `E-(a)3`).
* **Verdict : REJETÉE (uniquement sur l'accusation de circularité de l'Expérience 1) et ACCEPTÉE (sur tous les défauts statistiques des duels : bande morte, variance d'étalonnage, puissance et homme de paille ACI).**
* **Raison du rejet partiel :** Dans l'étage de tests de mort du programme, « toute règle candidate est implémentée sous une interface fixe et éprouvée contre des mondes plantés dont la vérité est connue [...] La vérité et le verdict restent hors de la machine qui exécute » `[RAPPORTÉ]`. Le code de la règle candidate ne connaît pas la paramétrisation secrète du monde planté (ni a fortiori la cause du triplement dans les journaux de déploiement réels). Tester si le redressement de longueur suffit ou échoue à longueur fixe falsifie effectivement l'hypothèse de suffisance de P1 (diagnostic que `A`, `B`, `D` et `E` proposent d'ailleurs tous les quatre dans leurs conceptions).
* **Correction appliquée aux duels :** Refonte intégrale des trois expériences dans la section **(b)** ci-dessous.

---

## (b) Les expériences corrigées (Inférence forte B4)

**Protocole statistique commun aux trois duels (corrigeant `A-(b)`, `B-(b)`, `D`, `E-(a)3`) :**
1. **Intégration de l'aléa d'étalonnage :** Chaque duel est évalué sur $R_{\text{rep}} = 200$ réplications `[illustratif]` par ré-échantillonnage par **blocs de tâches et sessions** (`B`, `D`) de l'étalonnage ($N_{\text{fit}} = 100$, $N_{\text{rang}} = 200$ `[illustratif]`), confrontées à $N_{\text{test}} = 2\,500$ épisodes honnêtes et $N_{\text{sab}} = 500$ épisodes de sabotage du régime dérivé `[illustratif]`.
2. **Frontière de décision sans bande morte (règle B4) :** Pour un paramètre cible $\theta$, on fixe une frontière unique $\theta_0$ pré-enregistrée. L'estimateur moyen sur les réplications $\hat{\theta}$ est muni de son intervalle de confiance bootstrap par blocs à $95\%$ $[L_{95}, U_{95}]$ `[illustratif]`.
   * **Issue 1 ($\hat{\theta} \le \theta_0$) :** falsifie $H_B$ (et établit la certification forte si $U_{95} \le \theta_0$).
   * **Issue 2 ($\hat{\theta} > \theta_0$) :** falsifie $H_A$ (et établit la réfutation forte si $L_{95} > \theta_0$).
   Aucune valeur numérique de $\hat{\theta}$ ne tombe hors de $\{ \le \theta_0 \} \cup \{ > \theta_0 \}$ `[VÉRIFIÉ]`.

---

### Duel 1 corrigé : Suffisance du redressement monotone de longueur (P1+P3 : EMPP) vs Dérive intrinsèque des représentations à longueur fixée

* **Hypothèses exclusives :**
  * **$H_A$ (Dominance de la dérive de longueur et des franchissements répétés) :** Sur la famille de dérive du programme où le seuil statique actuel triple le FPR à $\ge 3{,}0\%$ `[RAPPORTÉ]`, la règle **EMPP** (score de pas redressé en $\ln t$ et $\ln\ln t$ appris sur $D_{\text{fit}}$, seuil conforme d'enveloppe $W_{i,\le L_i}$ appris sur $D_{\text{rang}}$ disjoint, sans ancres du nouveau régime) ramène le taux de fausses alertes maximal par tranche de longueur sous la frontière $\theta_0 = 1{,}5\%$ `[illustratif]` tout en maintenant un rappel $\text{TPR} \ge \text{TPR}_{\text{oracle-statique}} - 5\text{ points}$ `[illustratif]`.
  * **$H_B$ (Dérive intrinsèque du score conditionnellement à la longueur) :** Même après redressement de la longueur et élimination des franchissements répétés par EMPP, la loi conditionnelle $P(W > q_{1-\alpha} \mid L, \text{régime})$ dérive (par rotation/inflation des états internes lors d'un changement de version ou de tâche, ou par variation de l'indice extrémal $\theta(L)$), laissant le FPR maximal par tranche strictement au-dessus de $\theta_0 = 1{,}5\%$ `[illustratif]` (ou écrasant le TPR de plus de $5$ points `[illustratif]`).
* **Contrôles négatifs obligatoires intégrés :**
  1. *Contrôle de fuite in-sample (`E-(c)1`, `A-(c)`, `B-(c)`, `D-(c)`) :* En régime stationnaire (coupe A/A par blocs de tâches), comparer EMPP *split-conformal* ($100 / 200$ `[illustratif]`) à EMPP *in-sample* ($300$ confondus `[illustratif]`). Falsifie l'innocuité de l'ajustement interne si le FPR *in-sample* en queue de longueur ($L > Q_{0{,}80}$) dépasse celui du *split-conformal* de plus de $0{,}3$ point `[illustratif]`.
  2. *Contrôle de sabotage impulsionnel en épisode court (`B-(b)`, `E-(c)3`) :* Injecter des sabotages concentrés sur $1$ seul pas ($t=1$) dans des épisodes courts ($L \le 20$ pas `[illustratif]`). Vérifie que $\text{TPR}_{\text{EMPP}} > 0$ (contrairement à l'ancienne martingale SCEM où $\text{TPR} \equiv 0$ `[VÉRIFIÉ]`).
  3. *Contrôle de dépendance de queue intra-épisode (`A-(c)`, `D-(c)`) :* Simuler deux flux honnêtes stationnaires ayant exactement les mêmes lois marginales par pas, l'un à pas indépendants (permutation inter-épisodes au même pas $t$), l'autre avec un effet aléatoire latent d'épisode fort (permutation intra-épisode conservant l'effet d'épisode). Vérifie que le FPR par épisode complet de EMPP reste $\le 1{,}0\% + \epsilon$ dans les deux cas `[VÉRIFIÉ]`.
* **Métrique et règle de décision :** $\theta = \max_{g \in \{\text{courte, moyenne, longue}\}} \overline{\text{FPR}}_g(\text{EMPP})$ dans le régime dérivé.
  * **Si $\hat{\theta} \le 1{,}5\%$ ET $\overline{\text{TPR}}_{\text{EMPP}} \ge \overline{\text{TPR}}_{\text{oracle}} - 5\%$ `[illustratif]` :** **$H_B$ est falsifiée** (le défaut provenait de l'agrégation sur la longueur et des franchissements répétés ; P1+P3 suffisent sans surcoût d'ancres en ligne).
  * **Si $\hat{\theta} > 1{,}5\%$ OU $\overline{\text{TPR}}_{\text{EMPP}} < \overline{\text{TPR}}_{\text{oracle}} - 5\%$ `[illustratif]` :** **$H_A$ est falsifiée** (la correction de longueur seule échoue ; un ancrage dans le nouveau régime est indispensable, ce qui enclenche le Duel 2).

---

### Duel 2 corrigé : Qualification des ancres et recalibrage TARR-v2 vs Biais d'ancre et dérive de queue pure

*(Pour corriger `A-(a)3`, `B-(a)5` et `E-(a)3`, l'homme de paille ACI non étiqueté est supprimé. Le duel oppose désormais deux hypothèses exclusives sur la validité même de l'ancrage TARR-v2 face au contrôle mécanique de rang pur sur ancres `D-ancre` / P1 de A, à la fois sur le monde à décalage M1 et sur le monde de test de mort à dérive de queue pure M3).*

* **Protocole préalable de qualification des ancres (contrôles négatifs `A-(c)`, `B-(c)`, `D-(c)`, `E-(c)2`) :**
  Avant de lire le FPR du duel, on soumet les ancres à trois tests de mort d'instrumentation :
  1. *Indiscernabilité ancre / trafic honnête (`A-(c)`, `B-(c)`) :* Un classifieur logistique régularisé entraîné sur les activations brutes $h_{i,t}$ pour séparer les témoins injectés des épisodes honnêtes du même régime doit avoir une $\text{AUC} \le 0{,}55$ `[illustratif]`.
  2. *Test de fuite d'intention sous masque syntaxique (`E-(c)2`, `B-(c)`) :* On compare la médiane des scores de sonde sur (i) des invites de sabotage exécutées sous masque syntaxique bloquant l'action, et (ii) des témoins honnêtes purs. Si l'écart dépasse $0{,}2\sigma$ `[illustratif]`, cela réfute expérimentalement l'hypothèse d'innocuité du masque syntaxique et confirme que seules les invites témoins honnêtes hors-ligne sont recevables.
  3. *Stabilité en régime stationnaire (`A-(c)`) :* En régime stable ($F_{\text{cible}} = F_{\text{cal}}$), TARR-v2 (dont la garde PAC ne se déclenche qu'au seuil $\beta = 0{,}05$ `[illustratif]`) ne doit pas augmenter l'écart-type inter-lots du FPR de plus de $0{,}15$ point `[illustratif]` par rapport au seuil fixe.
* **Hypothèses exclusives du Duel 2 :**
  * **$H_A$ (Transportabilité par ancres certifiées sous changement de régime) :** Avec un budget de $M = 100$ ancres certifiées `[illustratif]` dans le nouveau régime, **TARR-v2** maintient le FPR réel sous la frontière $\theta_0 = 1{,}5\%$ `[illustratif]` aussi bien sous un décalage global des scores honnêtes (Monde M1, même en présence d'une salve de $10\%$ de sabotages dans le flux `[illustratif]`) que sous une dérive de régime issue d'une nouvelle version d'agent, tout en conservant un gain de rappel $\Delta\text{TPR} \ge +5\text{ points}$ `[illustratif]` en phase transitoire ($M=50$ ancres `[illustratif]`) par rapport au seuil PAC-binomial conservateur (maximum des ancres M1 de B).
  * **$H_B$ (Rupture d'échangeabilité témoin–cible ou dérive de queue pure au-delà du centile $98\%$) :** Soit la dérive du trafic réel est une contamination de queue rare (ex. $2{,}5\%$ de tâches bénignes déclenchant un pic multimodal non capté par le transport de position-échelle en phase transitoire ou absent de la banque de témoins, cf. `E-(c)3` sur D), soit le bruit d'estimation à $M=50$ dégrade le FPR au-delà de $\theta_0 = 1{,}5\%$ `[illustratif]` ou annule le gain de TPR par rapport au maximum des ancres ($\Delta\text{TPR} < +5\text{ points}$ `[illustratif]`).
* **Métrique et règle de décision :** Couple $(\overline{\text{FPR}}_{\text{TARR-v2}}, \Delta\overline{\text{TPR}})$ évalué sur M1 (décalage global + $10\%$ de sabotages) et sur M3 (test de mort : dérive de queue pure où seuls $3\%$ des épisodes honnêtes du trafic subissent un saut de $+2\sigma$ `[illustratif]`).
  * **Si $\overline{\text{FPR}}_{\text{TARR-v2}} \le 1{,}5\%$ sur M1 et M3 ET $\Delta\overline{\text{TPR}} \ge +5\text{ points}$ `[illustratif]` :** **$H_B$ est falsifiée**.
  * **Si $\overline{\text{FPR}}_{\text{TARR-v2}} > 1{,}5\%$ (sur M1 ou M3) OU $\Delta\overline{\text{TPR}} < +5\text{ points}$ `[illustratif]` :** **$H_A$ est falsifiée** (le transport semi-paramétrique de phase transitoire est réfuté ; on conserve uniquement le rang conforme/PAC pur sur $M \ge 99$ ancres représentatives du flux).

---

### Duel 3 corrigé : Compensation par le jumeau honnête (Différence renormalisée vs Agent seul sous EMPP)

*(Pour tester la fragilité de l'écart au jumeau `[RAPPORTÉ]` tout en évitant la perte de puissance lorsque la corrélation agent-jumeau $\rho < 0{,}5$ signalée par `A` et `B`, et le piège du préfixe forcé signalé par `A-(a)4`, `B-(a)3`, `D-(b)` sur E).*

* **Hypothèses exclusives :**
  * **$H_A$ (Absorption de la dérive de tâche par l'écart pondéré au jumeau) :** Sur un changement de famille de tâches et de source bénigne (à version d'agent fixe), le score différentiel optimal à poids de régression $\beta_{\text{twin}} = \text{Cov}(W^{\text{agent}}, W^{\text{jumeau}})/\text{Var}(W^{\text{jumeau}})$ appris sur $D_{\text{fit}}$ :
    $$D_i = W_i^{\text{agent}} - \beta_{\text{twin}} W_i^{\text{jumeau}}$$
    (qui, contrairement à la différence brute $\beta_{\text{twin}}=1$, garantit $\text{Var}(D_i) \le \text{Var}(W_i^{\text{agent}})$ même si $\rho < 0{,}5$ `[VÉRIFIÉ]`) maintient le FPR dans le nouveau régime de tâches sous $\theta_0 = 1{,}5\%$ `[illustratif]` sans utiliser d'ancres du nouveau régime, et améliore le TPR à FPR réel égalisé de $\ge +5\text{ points}$ `[illustratif]` par rapport au score de l'agent seul $W_i^{\text{agent}}$.
  * **$H_B$ (Fragilité de l'écart agent–jumeau sous divergence de trajectoire ou de version) :** Dès que l'agent et le jumeau divergent dans leur exécution libre ou que la version de l'agent change à jumeau fixe (`FAITS` `[RAPPORTÉ]`), un biais de moyenne $\Delta\mu \neq 0$ (`E-(a)2` sur A) ou une inflation de variance résiduelle pousse le FPR de $D_i$ au-dessus de $\theta_0 = 1{,}5\%$ `[illustratif]` (ou dégrade le TPR par rapport à l'agent seul).
* **Contrôle négatif obligatoire :**
  * *Contrôle d'indépendance intra-version (`D-(c)`) :* Comparer deux exécutions libres indépendantes (graines aléatoires distinctes à température $T > 0$) de la **même** version honnête de l'agent sur les mêmes tâches, avant de comparer l'agent au jumeau. Mesure la part incompressible de variance de $D_i$ due à la divergence stochastique des trajectoires.
* **Métrique et règle de décision :**
  * **Si $\overline{\text{FPR}}(D_i) \le 1{,}5\%$ ET $\overline{\text{TPR}}(D_i) \ge \overline{\text{TPR}}(W^{\text{agent}}) + 5\%$ `[illustratif]` :** **$H_B$ est falsifiée** sur ce type de changement de régime (le jumeau pondéré absorbe la nuisance de tâche).
  * **Si $\overline{\text{FPR}}(D_i) > 1{,}5\%$ OU $\overline{\text{TPR}}(D_i) < \overline{\text{TPR}}(W^{\text{agent}}) + 5\%$ `[illustratif]` :** **$H_A$ est falsifiée** (le jumeau en exécution libre est trop fragile ; il doit être retiré de la formule du score et réservé à la bascule d'exécution *Defer-to-Twin* sur la zone grise).

---

## (c) Réponse à la question de l'arbitre (en une page)

### 1. Ce qui est établi `[VÉRIFIÉ]`
1. **La cause mathématique de la fragilité du seuil initial :** Sur un échantillon d'étalonnage honnête de taille finie $n = 300$ `[illustratif]`, le seuil conforme marginal au niveau $\alpha = 0{,}01$ ($298^{\text{e}}$ statistique d'ordre `[illustratif]`) a un taux de fausses alertes réel conditionnel à l'étalonnage qui suit une loi $\text{Beta}(3, 298)$ `[VÉRIFIÉ]`. Sans aucune dérive de régime, ce taux dépasse déjà $1\%$ dans $42\%$ des tirages d'étalonnage et dépasse $1{,}5\%$ dans $17\%$ des tirages `[illustratif]` `[VÉRIFIÉ]`.
2. **L'équivalence exacte entre surveillance pas-à-pas et test terminal d'épisode :** Toute règle séquentielle qui compare un score de pas $z_{i,t}$ à une frontière dépendante du pas $\Theta(t) = b(t) + q \, s(t)$ vérifie l'identité algébrique $\{\exists t \le L_i : z_{i,t} > \Theta(t)\} = \{\max_{1 \le t \le L_i} \frac{z_{i,t}-b(t)}{s(t)} > q\}$ `[VÉRIFIÉ]`. Par conséquent :
   * Calibrer $\Theta(t)$ tranche par tranche sur des préfixes gonfle le taux par épisode par union d'événements et biais de survie (`A`, `D`, `E` contre B) `[VÉRIFIÉ]`.
   * Construire une martingale multiplicative de rangs par pas se heurte au plafonnement discret $p_t \ge 1/(n+1)$ qui rend indétectable tout sabotage en $1$ ou $2$ pas ($\text{TPR} \equiv 0$, `B` et `E` contre C), tandis qu'une récurrence additive avec réinjection $(1-\lambda)$ perd la propriété de surmartingale (`A`, `B`, `D` contre E) `[VÉRIFIÉ]`.
   * À l'inverse, apprendre la tendance $b(t)$ et l'échelle de valeur extrême $s(t)$ sur une partition disjointe $D_{\text{fit}}$, puis fixer le quantile unique $q$ sur le maximum d'épisode complet $W_i = \max_{1 \le t \le L_i} \frac{z_{i,t}-b(t)}{s(t)}$ dans une partition $D_{\text{rang}}$ séparée par tâches et sessions, garantit **à la fois** le contrôle du premier passage en ligne à tout pas $t$, l'absence de moyenne sur les jetons, et une sensibilité immédiate dès le premier jeton de sabotage (**règle EMPP**) `[VÉRIFIÉ]`.
3. **Les limites arithmétiques de la recalibration sous dérive :**
   * *Sans nouvelles données du régime cible*, aucune méthode robuste au pire cas (DRO / `D-enveloppe`) ni aucune repondération de covariables ne peut certifier $\text{FPR} \le 1\%$ sur une famille de dérive qui triple le taux ($\varepsilon \ge 2\% > 1\%$) sans abaisser le seuil nominal vers $\alpha/3 \approx 0{,}33\%$, ce qui requiert $n \ge 1\,000$ épisodes honnêtes par strate ou détruit le rappel (`A`, `B`, `E` contre D) `[VÉRIFIÉ]`.
   * *Sans étiquettes fiables*, l'adaptation en ligne sur le flux (ACI) est empoisonnée par toute salve de sabotages (`A`, `B`, `C`, `D`, `E`) `[VÉRIFIÉ]`.
   * *Avec des témoins/ancres honnêtes certifiés*, un transport sur micro-lot ($K=15$ `[illustratif]`) injecte plus de bruit ($\approx 0{,}8\sigma$ `[illustratif]`) que le décalage qui triple le taux ($\approx 0{,}45\sigma$ `[illustratif]`) (`A`, `B`, `E` contre C) `[VÉRIFIÉ]`. Pour garantir un FPR $\le 1\%$ sans hypothèse paramétrique de queue, il faut un réservoir d'au moins $M \ge 99$ ancres honnêtes échangeables avec le régime courant (ou $M \ge 299$ pour une garantie PAC à $95\%$ `[illustratif]`) `[VÉRIFIÉ]`.
   * *Un quota fixe d'audit* (Top-$1\%$ du lot) garantit la stabilité de la **charge humaine**, mais jamais un FPR de $1\%$ (`A`, `B`, `D`, `E`) `[VÉRIFIÉ]`.

### 2. Ce qui n'est pas établi `[HYPOTHÈSE]` ou `[RAPPORTÉ]`
1. **La décomposition causale du triplement dans le programme :** On ne sait pas quelle fraction de l'excès de FPR ($1\% \to 3\%$ `[RAPPORTÉ]`) provient (i) de la variance d'étalonnage intra-régime et de la corrélation par grappes de tâches, (ii) de l'allongement mécanique des épisodes sur un opérateur sans moyenne par jeton, ou (iii) d'un décalage intrinsèque des activations internes $P(S \mid L)$ lors d'un changement de version ou de tâche `[HYPOTHÈSE]`.
2. **La préservation du classement (ROC / séparabilité) sous dérive :** Il n'est pas établi qu'en relevant le seuil dans le nouveau régime pour ramener le FPR de $3\%$ à $1\%$, le taux de détection des sabotages (TPR) reste utile `[HYPOTHÈSE]`.
3. **L'échangeabilité des ancres et du jumeau :** Il n'est pas établi que les témoins injectés subissent la même dérive de queue que le trafic bénin libre (notamment face à une nouvelle source bénigne), ni qu'ils soient indiscernables par les états internes de l'agent `[HYPOTHÈSE]`.

### 3. L'expérience à faire en premier
Avant d'alourdir la production avec des témoins en ligne, l'expert doit exécuter **hors-ligne, sur les journaux bruts existants des mondes plantés du programme (coût $< 5\text{ \$}$ et $< 3$ minutes CPU `[illustratif]`)**, le **Duel 1 corrigé combiné au diagnostic de variance par blocs** :
1. **Protocole :** Extraire les scores bruts par pas $z_{i,t,m}$ et les identifiants de tâche/session/longueur. Sur $200$ coupes aléatoires **par blocs de tâches** de l'ancien régime ($N_{\text{fit}}=100$ pour ajuster $b(t) = a_0 + a_1 \ln t$ et $s(t) = \exp(b_0 + b_1 \ln\ln t)$ + le poids $\beta_{\text{twin}}$ du jumeau ; $N_{\text{rang}}=200$ pour le seuil conforme sur l'enveloppe $W_i = \max_{t \le L_i} \frac{z_{i,t}-b(t)}{s(t)}$ `[illustratif]`), mesurer la distribution du FPR et du TPR dans l'ancien régime (coupe A/A) et dans le régime dérivé (coupe A/B), avec et sans redressement de longueur EMPP.
2. **Verdict actionnable immédiat :**
   * Si le redressement monotone de longueur **EMPP** ramène à lui seul le FPR maximal par tranche de longueur dans le régime dérivé de $3\%$ à $\le 1{,}5\%$ `[illustratif]` sans perte de TPR $> 5$ points `[illustratif]`, le défaut de longueur et de franchissements répétés des `FAITS` est résolu à **coût d'inférence nul**.
   * Si le FPR de EMPP reste $> 1{,}5\%$ `[illustratif]` à longueur redressée, la dérive conceptuelle des états internes est prouvée : on déploie alors **TARR-v2** (garde e-martingale sur seuil PAC + recalibrage sur réservoir de $M \ge 100$ témoins honnêtes ayant passé le test d'indiscernabilité $\text{AUC} \le 0{,}55$ `[illustratif]`), et, tant que les $100$ témoins du nouveau régime ne sont pas réunis, on bascule la zone grise ($[0{,}5\% \,;\, 3\%]$ `[illustratif]`) sur le jumeau honnête (*Defer-to-Twin*) sous quota fixe de relecture humaine.

FIN-DE-CELLULE
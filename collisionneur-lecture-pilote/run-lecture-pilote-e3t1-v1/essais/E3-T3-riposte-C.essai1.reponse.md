# Proposition C · Tour III.3 — Riposte

**Pièces reçues.** Le bloc FAITS est vide par décision de l'arbitre (**RAPPORTÉ**). La question de l'arbitre, ma conception (E3-T1-conception-C) et les deux attaques de l'équipe rouge (E3-T2-redteam-A et E3-T2-redteam-B) sont reçues en entier (**OBSERVÉ-NON-AUDITÉ** pour leurs empreintes sha256). Conformément aux consignes, je ne réponds qu'aux sections visant C. Tout fait tiré de la question est marqué **RAPPORTÉ**, toute supposition ou déduction non garantie est marquée **HYPOTHÈSE**, et tout chiffre hors cadre est marqué « illustratif ».

---

## (a) Traitement point par point des attaques de l'équipe rouge contre C

### 1. Ambiguïtés du cadre, glissements de statut et contenu hors cadre

* **Attaque de B (Préambule & C1) : Ambiguïté sur « par famille, 36 et 24 tâches par part » et glissement sur « reçoit son score sur `test` ».**
  * *Décision :* **Acceptée.**
  * *Correction :* Le cadre dit « par famille, 36 et 24 tâches par part » (**RAPPORTÉ**). Cela peut signifier soit que la famille 1 a 36 tâches par part et la famille 2 en a 24 (total $N = 60$ tâches par part), soit que dans chaque famille, `test` a 36 tâches et `test_final` en a 24 (total $N = 48$ tâches sur `test_final` et $72$ sur `test`). Les deux lectures restent des **HYPOTHÈSES** tant que l'arbitre ne les tranche pas ; je donne désormais les seuils sous les deux lectures ($N=60$ et $N=48$). De même, que le score reçu sur `test` guide effectivement la réécriture est une **HYPOTHÈSE** (et non un fait rapporté). Enfin, je réserve l'étiquette **VÉRIFIÉ** aux identités arithmétiques pures conditionnelles aux prémisses, et je reclasse « 2/4 niveau du hasard » comme faux (voir C-6/C9).
* **Attaque A-C1 & B-C10 : Contenu hors cadre (section (d) sur les GPU/modèles ouverts), superlatifs et ton prescriptif.**
  * *Décision :* **Acceptée.**
  * *Correction :* Je retire intégralement les estimations illustratives de matériel GPU et de modèles ouverts qui ne figuraient pas dans la question, afin d'éviter toute création d'ancres chiffrées par érosion. Je retire également les superlatifs (« massif », « sécurité absolue », « strictement égale à 0 bit ») et les formulations prescriptives (« seule voie »), en laissant chaque voie soumise aux critères d'arbitrage de Lazar.

### 2. Failles statistiques et logiques de l'Expérience 1 (Pilote décisif (b))

* **Attaque A-C2 & B-C4 : Violation de la règle B4 (inférence forte) — confondre un échec à rejeter $H_0$ avec la falsification de $H_A$, et définir $H_A$ par rapport au bruit de l'instrument.**
  * *Décision :* **Acceptée.**
  * *Correction :* Si l'on fixe un effet minimal d'intérêt à $\delta_{\min} = 0,05$ mais que l'erreur type à 3 graines ne permet de franchir le seuil de décision qu'à $\Delta_{\text{obs}} \ge 0,12$, une observation de $+0,08$ ne falsifie pas $\Delta \ge 0,05$ : le test manque simplement de puissance. Pour respecter strictement B4 à budget fixé (3 ou 4 graines), le duel doit opposer deux hypothèses mutuellement exclusives séparées par une **règle de décision duale (supériorité / infériorité-ou-futilité)** dont le point de coupure $\Delta_{\text{crit}}$ borne simultanément le risque $\alpha$ (faux positif sous $\Delta \le 0$) et le risque $\beta$ (faux négatif sous $\Delta \ge \delta_{\text{viable}}$), où $\delta_{\text{viable}}$ est le gain minimal rendant la complexification détectable et rentable à ce budget. Toute issue sous $\Delta_{\text{crit}}$ falsifie alors $H_A$ ($\Delta \ge \delta_{\text{viable}}$) avec un taux d'erreur borné par $\beta$.
* **Attaque A-C3, B-C2 & B-C3 : Fourches laissées ouvertes dans la métrique primaire, union de deux tests (« rangs OU $t > 2,132$ ») gonflant $\alpha$, et degrés de liberté de Welch ($\nu$ pouvant descendre à 2 si les variances diffèrent).**
  * *Décision :* **Acceptée.**
  * *Correction :* Dans l'Expérience 1 corrigée ci-dessous :
    1. Toutes les fourches sont fermées : une seule métrique primaire est scellée (exactitude micro-moyennée sur l'ensemble des tâches de `test_final` à la **génération 4** uniquement).
    2. L'opérateur « OU » est supprimé. Pour éviter l'effondrement des degrés de liberté de Welch ($\nu \to 2$ quand $\sigma_{\text{v6.2.1}} \gg \sigma_{\text{v5.3}}$, ce qui ferait passer le quantile $t_{0,95}$ de $2,132$ à $2,920$, calcul explicite **VÉRIFIÉ**), la règle de décision primaire repose sur **un seul test non paramétrique exact** : le test de permutation exact des moyennes de courses (soit $\binom{6}{3} = 20$ permutations à 3 graines, où le rang maximal 3 contre 3 donne exactement $p = 1/20 = 0,05$ unilatéral sans aucune hypothèse d'homoscédasticité ni de normalité ; et $\binom{8}{4} = 70$ permutations à 4 graines, où les 3 meilleures configurations donnent $p = 3/70 = 0,0429 \le 0,05$, calcul explicite **VÉRIFIÉ**), couplé par un **ET** logique à un seuil d'amplitude ponctuelle $\Delta_{\text{obs}} \ge \Delta_{\text{crit}}$.
* **Attaque B-C6 : Surpromesse du modèle mixte (GLMM) et de l'appariement par tâche.**
  * *Décision :* **Acceptée.**
  * *Correction :* L'appariement par tâche élimine la variance de difficulté inter-tâches mais ne réduit en rien la variance inter-graines ($\sigma^2_{\text{graine}}$), qui reste le facteur limitant à $K=3$ graines. De plus, un GLMM à 3 niveaux par groupe produit des estimations de variance singulières. Je retire le GLMM du critère primaire : l'unité d'analyse primaire est strictement la **course (graine)** (score global sur `test_final` à la génération 4).
* **Attaque B-(c)2 & A-C5 : Confusion du contraste (v6.2.1 vs v5.3) avec le mécanisme isolé, et défaut du contrôle « génération 0 ».**
  * *Décision :* **Acceptée sur le contrôle génération 0 ; Transformée en condition de validité sur l'ablation.**
  * *Correction :* Le cadre ne mentionne pas de « génération 0 » mais « jusqu'à 6 rondes de conception, puis 4 générations notées » (**RAPPORTÉ**). En outre, à la génération 1, le bruit sur une graine ($\text{SE} \approx 0,10$ à $0,125$, **RAPPORTÉ**) mettrait en échec un seuil de $0,05$ près d'une fois sur deux (**HYPOTHÈSE**). Je supprime le contrôle « génération 0 » et le remplace par : (i) un contrôle de déterminisme/variance intra-objet et (ii) une restriction explicite de l'inférence au contraste `v6.2.1 vs v5.3` (sauf si v5.3 est par construction l'ablation exacte de la réécriture de récompense dans v6.2.1, ce qui doit être vérifié par un `diff` du code source avant scellement).

### 3. Failles de l'agrégation séquentielle ($1+3=4$ graines) et des dessins sans contamination

* **Attaque A-C4 & B-C7 (et évasions associées) : L'agrégation $1+3=4$ graines abandonne le but déclaré de (a) (« produire des hypothèses testables »), suppose l'échangeabilité (alors que l'API du modèle appelé peut dériver entre (a) et (b)), et crée une fourche post-hoc (déclarer un bug après (a) pour annuler le pooling si le score déplaît).**
  * *Décision :* **Acceptée et Transformée en test / règle mécanique scellée.**
  * *Correction :*
    1. Je ne présente plus le pooling $1+3=4$ comme une variante implicite de (a), mais comme une **branche explicite soumise à Lazar** : soit Lazar maintient que (a) doit être lu pour inventer les hypothèses de (b) (auquel cas le pooling est interdit et (b) reste à $K=3$ graines), soit Lazar accepte que l'hypothèse de (b) est déjà fixée par sa question de 00:49 (valeur ajoutée de v6.2.1 sur v5.3 au-delà du bruit, **RAPPORTÉ**) et utilise (a) comme étape 1 d'un plan à $K=4$ graines.
    2. Pour bloquer l'évasion E-C4 (annuler le pooling post-hoc en prétextant une correction de code), la décision d'agréger (a) et (b) est verrouillée par un prédicat automatique évalué **sans lire les scores** : l'agrégation a lieu si et seulement si (i) le code de v6.2.1 et v5.3 a exactement la même empreinte SHA-256 dans (a) et (b), (ii) les 2 courses de (a) ont atteint la génération 4 sans exception fatale non gérée (critère mécanique binaire), et (iii) l'**étalon de dérive API** (emprunté à l'équipe rouge A-(c)6 et B-(c)4, en le disant) ne détecte pas de changement du modèle appelé entre (a) et (b).
* **Attaque B-C8 : La « variance à l'aveugle » fuit la moyenne (car $\text{Var} = p(1-p)/n$ révèle $|p - 0,5|$) et les étiquettes X/Y fuient par les coûts/durées.**
  * *Décision :* **Acceptée.**
  * *Correction :* Pour une variable binaire ou binomiale où $p > 0,5$, donner la variance empirique révèle directement la moyenne. Je retire le dessin de « variance à l'aveugle sur (a) » de mes recommandations.
* **Attaque B-E-C1 & A-C6 : Forçage par énumération de l'enveloppe SHA-256 (l'espace de sortie de la fonction $f$ a une faible entropie $\approx 3$ à $6$ bits : quiconque voit le hash publié peut hacher toutes les sorties possibles et lire le signe) et fuite par le contre-lecteur.**
  * *Décision :* **Acceptée.** C'est une critique décisive de B.
  * *Correction :* Un hachage SHA-256 non salé d'un message à faible entropie est inversible instantanément par force brute. Dans l'architecture (2'-scellée), le script (ou l'agent neuf isolé) doit concaténer au texte généré un **sel cryptographique aléatoire de 256 bits** (`os.urandom(32)`) stocké uniquement dans le coffre isolé jusqu'au descellement des expériences principales (emprunt à B-E-C1, en le disant). De plus, dans la variante par fonction déterministe $f$, la contre-lecture par un agent neuf porte sur le **code de $f$ avant l'exécution de (a)**, de sorte qu'aucun agent ni humain ne lit la sortie de $f$ avant la fin de (b).

### 4. Failles de l'Expérience 2, des canaux passifs et de la table des instruments

* **Attaque A-C6 & B-C9 : L'Expérience 2 (double piste sur une seule réalisation de (b) et loi nulle « 2/4 ») est mal fondée et ne falsifie rien sous B4.**
  * *Décision :* **Acceptée et Transformée en test de simulation/bootstrap (Expérience 3 corrigée).**
  * *Correction :* Une seule réalisation de (a) suivie de (b) ne donne qu'un seul tirage global : on ne peut pas estimer un taux d'erreur fréquentiste sur $N=1$ essai méta. Je remplace l'Expérience 2 par le test pré-scellement demandé par A-(c)1 (en le disant) : une **évaluation par rééchantillonnage/simulation paramétrique et bootstrap sur les 6 (ou 8) courses finales** mesurant le taux d'erreur de signe (Type S) d'une règle conditionnée sur 1 graine contre une règle fixe.
* **Attaque A-C8, B-E-A2 & Duel final de B : Les faits mécaniques (coûts, durées, plantages, nombre de jetons) ne transportent pas « 0 bit » mais sont corrélés au score.**
  * *Décision :* **Transformée en test (Expérience 2 corrigée).**
  * *Correction :* Je reprends et formalise le duel proposé par B en conclusion de sa revue (qui combine S7 de A et mon enveloppe chiffrée, en le disant), ainsi que le masquage chronologique de A-(c)6 pour l'audit des diffs, afin de tester empiriquement la fuite par les faits mécaniques et par l'édition des textes.
* **Attaque A-C7 & B-E-C5 : Fuites dans la table (c) (TPR = 1,00 invérifiable sur le noyau ; mémorisation des entrées de `test_final` d'une génération à l'autre par l'organisme qui se réécrit).**
  * *Décision :* **Acceptée.**
  * *Correction :* Même si `test_final` n'est jamais noté devant l'organisme (**RAPPORTÉ**), si le noyau évalue l'organisme sur `test_final` aux générations 1, 2, 3 et 4 en lui passant les entrées des tâches, un organisme qui persiste en mémoire ou dans son code réécrit peut inspecter et mémoriser la distribution des entrées non notées ! **Parade matérielle ajoutée au protocole :** `test_final` ne doit être exécuté que sur des **clones gelés (forks sans retour d'état)** de l'organisme à chaque génération (le processus qui voit `test_final` est détruit immédiatement après son évaluation et ne peut transmettre aucun octet au processus qui passe à la génération suivante), ou n'être évalué qu'une seule fois à la fin de la génération 4. En outre, j'intègre les **tâches-canaris** dans `test_final` proposées par A-(c)5 et B-(c)5 (en le disant).

---

## (b) Les expériences corrigées (conformes à B4)

### Expérience 1 (Pilote décisif (b) corrigé) : Valeur ajoutée de v6.2.1 vs v5.3 au-delà du bruit

* **Portée causale explicite :** Le test porte sur le contraste global `v6.2.1` contre `v5.3`. Il n'isole le mécanisme pur de « réécriture de la règle de récompense » que si un audit `git diff` pré-course atteste que `v5.3` et `v6.2.1` ne diffèrent initialement que par l'activation de ce module ; sinon, toute différence additionnelle de code est déclarée comme facteur confondant dans le préenregistrement.
* **Isolation de `test_final` :** À la génération 4 (et pour toute mesure intermédiaire éventuelle), l'évaluation sur `test_final` est exécutée dans un sous-processus isolé et jetable (fork en lecture seule) détruit après notation, empêchant mathématiquement l'organisme de mémoriser les entrées de `test_final` d'une génération à l'autre.
* **Unité d'analyse et métrique primaire ($M_1$) unique (zéro fourche) :**
  * L'unité d'analyse primaire est la **course (graine)** ($K=3$ par objet, ou $K=4$ si les conditions mécaniques d'agrégation de (a) ci-dessous sont remplies).
  * Pour chaque course $g$ de l'objet $i \in \{\text{v6.2.1}, \text{v5.3}\}$, le score $S_{i,g} \in [0,1]$ est l'**exactitude micro-moyennée sur la totalité des tâches de la part `test_final` (les deux familles réunies) à la génération 4 uniquement** (soit $N = 60$ tâches si les familles font $36+24$ par part, ou $N = 48$ tâches si chaque famille a $24$ tâches dans `test_final` — la valeur exacte de $N$ est figée par simple lecture de la taille du fichier de banque avant la course).
  * Effet observé : $\Delta_{\text{obs}} = \bar{S}_{\text{v6.2.1}} - \bar{S}_{\text{v5.3}}$.
* **Hypothèses exclusives (duel B4 à erreurs bornées) :**
  * **$H_A$ (Valeur ajoutée de la complexification au-delà du bruit du protocole) :** L'espérance du gain de `v6.2.1` sur `v5.3` sur `test_final` en génération 4 vérifie $\Delta_{\text{vrai}} \ge \delta_{\text{viable}}$ (où $\delta_{\text{viable}} = +0,18$ à $K=3$ graines ou $+0,15$ à $K=4$ graines, illustratif sous $\sigma_{\text{course}} \approx 0,08$, représentant le gain minimal détectable avec une puissance $\ge 80\%$ au seuil $\alpha = 0,05$).
  * **$H_B$ (Nullité, dégradation ou gain inférieur au seuil de viabilité/bruit) :** $\Delta_{\text{vrai}} \le 0$ (ou $\Delta_{\text{vrai}} < \delta_{\text{viable}}$ : la complexification n'apporte pas un gain suffisant pour émerger du bruit à ce budget).
* **Règle de décision unique et scellée (sans opérateur « OU ») :**
  * *Cas $K=3$ graines par objet (6 courses) :*
    * **Validation de $H_A$ (falsification de $H_B$ au risque $\alpha \le 0,05$) :** Les 3 courses de `v6.2.1` obtiennent toutes un score $S_{\text{v6.2.1}, g}$ strictement supérieur aux 3 courses de `v5.3` (test exact de permutation/Mann-Whitney unilatéral : $1/\binom{6}{3} = 1/20 = 0,05$, calcul explicite **VÉRIFIÉ**) **ET** $\Delta_{\text{obs}} \ge +0,11$ (illustratif, point médian entre $0$ et $\delta_{\text{viable}}$ calibré sur l'erreur type binomiale).
    * **Validation de $H_B$ (falsification de $H_A$ au risque $\beta \le 0,20$ sous $\sigma_{\text{course}} \le 0,08$) :** Au moins une course de `v5.3` égale ou dépasse une course de `v6.2.1`, **OU** $\Delta_{\text{obs}} < +0,11$.
  * *Cas $K=4$ graines par objet (8 courses, si agrégation de (a) validée mécaniquement) :*
    * **Validation de $H_A$ (falsification de $H_B$ au risque $\alpha = 3/70 = 0,0429 \le 0,05$) :** La somme des rangs des 4 courses de `v6.2.1` parmi les 8 courses est $\ge 24$ sur $26$ possibles (les 3 configurations les plus extrêmes sur $\binom{8}{4}=70$, calcul explicite **VÉRIFIÉ**) **ET** $\Delta_{\text{obs}} \ge +0,09$ (illustratif).
    * **Validation de $H_B$ (falsification de $H_A$) :** Somme des rangs $< 24$ **OU** $\Delta_{\text{obs}} < +0,09$.
* **Métrique secondaire de surapprentissage ($\Gamma$) et son contrôle négatif (Placebo de rétroaction emprunté à B-(c)2, en le disant) :**
  * $\Gamma = (\bar{S}_{\text{test, gen 4}} - \bar{S}_{\text{test\_final, gen 4}})_{\text{v6.2.1}} - (\bar{S}_{\text{test, gen 4}} - \bar{S}_{\text{test\_final, gen 4}})_{\text{v5.3}}$.
  * Pour distinguer l'exploitation de la règle de récompense d'une simple sélection plus agressive sur le bruit (critique B-A4/B-(c)5), cette métrique reste purement descriptive tant qu'un run placebo (où `v6.2.1` reçoit un score `test` permuté aléatoirement entre générations) n'est pas financé.
* **Contrôles négatifs et critères d'invalidation mécanique de l'Expérience 1 :**
  1. **Clause d'ininterprétabilité par variance inter-graines excessive (empruntée à A-(c)4, en le disant) :** L'écart type empirique intra-objet $s_{\text{pool}} = \sqrt{(s^2_{\text{v6.2.1}} + s^2_{\text{v5.3}})/2}$ est calculé sur les courses réalisées ($\nu = 4$ ddl à $K=3$, $\nu = 6$ ddl à $K=4$). Si $s_{\text{pool}} > 0,15$ (illustratif), le bruit réel dépasse le modèle de dimensionnement : l'expérience déclare automatiquement que le budget de 3 (ou 4) graines a une puissance inférieure à $50\%$ pour $\delta_{\text{viable}}$, et rejette l'aptitude du protocole à 3 graines à trancher.
  2. **Étalon fixe de dérive du modèle appelé (emprunté à A-(c)6 et B-(c)4, en le disant) :** Un script figé (sans réécriture, 20 tâches fixes hors banque, température $0$) est exécuté avant la première course de (a) et après la dernière course de (b). Si son score varie de plus de $2$ tâches sur $20$ (seuil binomial hors bruit de noteur, illustratif) ou si l'identifiant de version du modèle renvoyé par l'API change, l'agrégation (a)+(b) est interdite et la dérive API est consignée.
  3. **Jetons-canaris dans `test_final` (empruntés à A-(c)5 et B-(c)5, en le disant) :** Insérer un identifiant aléatoire UUID en commentaire invisible dans les tâches de `test_final`. Tout code généré par l'organisme ou journal de conception contenant cet UUID déclenche l'invalidation immédiate pour fuite du bac à sable (TPR = $1,00$ sur cette fuite spécifique par recherche exacte de chaîne).

---

### Expérience 2 (Sécurité opérationnelle) : Test d'évasion par les faits mécaniques, l'enveloppe et le diff-audit aveugle

Cette expérience fusionne le duel final proposé par B (adversaire interne sur les faits mécaniques) et les contrôles A-(c)1 / A-(c)6 / B-(c)3, que j'adopte en le disant.

* **Sous-expérience 2A (Fuite par les faits mécaniques sous l'Option 3 ou le lanceur A) :**
  * **$H_A$ (Étanchéité des faits mécaniques) :** Les métadonnées opérationnelles d'une course (coût en USD, durée murale, nombre d'appels API, longueur du code réécrit, plantages éventuels) ne permettent pas à un agent auditeur de deviner lequel des deux objets (ou laquelle des deux familles) a obtenu le meilleur score sur `test_final` mieux que le hasard.
  * **$H_B$ (Canal passif exploitable) :** Les faits mécaniques divulguent le signe de $\Delta$ avec une exactitude supérieure au hasard.
  * **Protocole :** Sur l'ensemble des courses générées (les 2 de (a) + les 6 de (b), soit 8 courses = 4 paires indépendantes sur 2 familles = 8 comparaisons binaires), on fournit à $k = 10$ instances d'un agent « équipe rouge » uniquement le tableau des faits mécaniques (sans les scores). Dans le **bras réel**, les faits mécaniques sont vrais ; dans le **bras contrôle négatif (permuté)**, les profils mécaniques sont appariés aléatoirement aux objets.
  * **Falsification :** Si le score moyen de prédiction du signe de $\Delta$ par les agents rouges dans le bras réel dépasse celui du bras permuté d'au moins $+25$ points de pourcentage (illustratif) avec $p < 0,05$ par test de permutation des paires, $H_A$ est falsifiée : les faits mécaniques constituent une fuite significative, et le lanceur (lignée A) ne doit recevoir qu'un rapport binaire global (« exécution terminée sous le plafond de 450 USD : oui/non ») sans le détail par objet. Sinon, $H_B$ est falsifiée.

* **Sous-expérience 2B (Audit à l'aveugle des modifications des textes principaux entre T0 et le scellement) :**
  * **Protocole :** À $T_0$ (avant la fin de (a)), l'intégralité des brouillons de l'étape 1 et de la confrontation (y compris la banque de tâches et les règles d'exclusion, pour parer l'évasion A-(b) et B-E-C3) est hachée. À $T_1$ (au scellement final), on extrait tous les `git diff` entre $T_0$ et $T_1$, auxquels on mélange des `git diff` témoins provenant d'éditions antérieures à $T_0$ (contrôle négatif de base emprunté à A-(c)1). Un agent auditeur **aveugle à l'ordre chronologique ($T_0 \to T_1$ vs $T_1 \to T_0$) et aveugle aux scores de (a)** (masquage emprunté à A-(c)6) classe chaque modification selon qu'elle assouplit ou durcit les critères en faveur d'une famille ou d'un mécanisme. Une fois (i) et (ii) scellés, un script croise ces étiquettes avec les résultats de (a).
  * **$H_A$ (Absence de glissement directionnel) :** Les modifications post-$T_0$ ne s'alignent pas davantage avec la direction de (a) que les modifications témoins pré-$T_0$.
  * **$H_B$ (Contamination effective des textes principaux) :** Les modifications post-$T_0$ favorisent significativement la direction observée dans (a) par rapport aux témoins pré-$T_0$.

---

### Expérience 3 (Méta-méthodologie) : Conditionner le signe de (b) sur 1 graine (a) vs Signe fixe d'Ockham

Cette expérience remplace mon ancienne Expérience 2 en intégrant le contrôle de simulation nulle de A-(c)1 et l'évaluation par bootstrap sur les courses réalisées.

* **$H_A$ (Gain d'information d'une course unique $N=1$) :** Choisir le signe (ou la famille primaire) de l'hypothèse d'un essai à 3 graines en lisant au préalable 1 graine pilote ($N=1$) augmente la probabilité de confirmer le vrai signe sous-jacent (ou réduit le risque d'erreur de signe de Type S) par rapport à un test unilatéral fixe ($\text{v6.2.1} > \text{v5.3}$).
* **$H_B$ (Domination par le bruit d'échantillonnage à $N=1$) :** Sous le niveau de bruit empirique des organismes ($\sigma_{\text{diff}} \ge 0,10$), conditionner l'hypothèse sur $N=1$ graine produit un taux d'inversion de signe (erreur de Type S) supérieur à $20\%$ (illustratif) lorsque l'effet vrai est modéré ($\Delta \in [0,05 ; 0,15]$) et fait perdre de la puissance par rapport à l'agrégation des $1+3=4$ graines sous hypothèse fixe.
* **Protocole en deux volets (sans aucun coût API supplémentaire) :**
  1. **Volet 1 (Avant scellement, simulation nulle de la fonction de branchement $f$, empruntée à A-(c)1) :** Pour toute règle de génération d'hypothèses $f(\text{scores}_a)$ proposée sous l'Option (2) ou (2'), tirer $10\,000$ réalisations Monte Carlo de (a) sous l'hypothèse nulle ($\Delta = 0$, $\sigma_{\text{diff}} = 0,11$, **RAPPORTÉ**) et sous une hypothèse d'effet modéré ($\Delta = +0,10$).
  2. **Volet 2 (Après (b), validation empirique par leave-one-out exact sur les courses réalisées) :** Sur l'ensemble des courses disponibles (ex. les 4 graines de chaque objet si (a) et (b) ont tourné sur le même code, soit $4 \times 4 = 16$ paires de courses possibles pour simuler un pilote (a) à 1 graine suivi d'un essai (b) sur les 3 graines restantes), comparer la concordance et le taux de détection de la règle adaptative (qui lit la 1re graine tirée pour fixer le signe testé sur les 3 autres) contre la règle fixe d'Ockham sur les 4 graines.
* **Issues falsificatrices :**
  * Si, dans le Volet 1, la règle $f$ se trompe de signe dans plus de $15\%$ des simulations à $\Delta = +0,10$ (illustratif) ou choisit la même branche dans plus de $90\%$ des cas sous $\Delta = 0$ (faisant de $f$ une fiction), **ET** que dans le Volet 2 les 16 partitions leave-one-out montrent une variance de signe inter-paires incompatible avec une prédiction fiable ($\ge 4/16$ inversions de signe par rapport à la moyenne globale), $H_A$ est falsifiée : lire $N=1$ graine dégrade la décision. Dans le cas contraire, $H_B$ est falsifiée.

---

## (c) Réponse synthétique à la question de l'arbitre (Une page)

### 1. Ce qui est établi (calculs explicites et structure du cadre)

1. **Disproportion entre le bruit d'une graine unique (a) et un effet réaliste :** Avec un écart type de différence entre deux courses uniques de $\approx 0,10$ à $0,125$ avant même de compter la variance entre graines (**RAPPORTÉ**), l'intervalle de fluctuation à $95\%$ d'une différence nulle dans le pilote 4 (a) couvre environ $[-0,22 ; +0,22]$. Tirer le signe d'une hypothèse à partir d'une seule graine par objet ($N=1$) expose à un risque élevé d'erreur de signe (Type S) dès que l'effet réel est inférieur à $0,15$.
2. **Plancher de résolution statistique à 3 graines (b) :** Sur $K=3$ graines contre $3$, le test exact non paramétrique de permutation (indépendant de l'hypothèse d'égalité des variances qui fragilise le test de Welch lorsque $\nu$ tombe vers $2$) atteint tout juste $\alpha = 1/\binom{6}{3} = 0,05$ en **unilatéral** (quand les 3 graines d'un objet dominent strictement les 3 de l'autre), et ne peut **jamais** franchir $\alpha = 0,05$ en bilatéral ($2/20 = 0,10$). Avec 3 graines, le pilote décisif (b) ne peut détecter avec une puissance de $80\%$ que des effets massifs ($\Delta \ge 0,18$ à $0,25$ selon la variance inter-graines). Il ne pourra **pas** trancher un effet réel modéré de $+0,05$ à $+0,12$, ni tester les deux familles séparément sans détruire sa puissance par correction de multiplicité.
3. **Perméabilité des options déclaratives (2) et (2' non salée) :**
   * Dans l'Option **(2)**, la lecture par la lignée B du signe et des seuils choisis par l'agent neuf transmet plusieurs bits d'information sur la performance de `v6.2.1` avant le scellement de la confrontation. Une réserve « déclarée » protège contre le plagiat de chiffres, mais ne protège pas contre l'ajustement implicite des fourches non encore scellées (choix des tâches de la banque décisive, règles d'arrêt, critères d'exclusion).
   * Dans l'Option **(2')**, publier un hachage SHA-256 sans sel cryptographique d'une section d'hypothèses à faible entropie permet à quiconque de retrouver le signe par simple énumération. De plus, si le contre-lecteur neuf ou le lanceur (lignée A) lit le texte en clair ou voit des faits mécaniques asymétriques (coûts, plantages), le canal fuit.
4. **Connaissance préalable du signe de l'hypothèse de fond :** La demande de Lazar de 00:49 (« trancher si les apports supplémentaires de complexification apportent une valeur ajoutée au-delà du bruit », **RAPPORTÉ**) fixe déjà une hypothèse asymétrique (rasoir d'Ockham) : la charge de la preuve repose sur `v6.2.1 > v5.3`. On n'a pas besoin de lire (a) pour connaître la direction à tester.

### 2. Ce qui n'est pas établi (inconnues empiriques et décisions d'arbitrage)

1. **L'ampleur de la variance inter-graines ($\sigma_{\text{graine}}$) et le déterminisme des appels API :** On ignore si deux graines d'un même objet sur les mêmes tâches produisent un écart type de $0,02$ ou de $0,15$ (**HYPOTHÈSE**).
2. **La lecture exacte de la taille de la banque :** Savoir si « par famille, 36 et 24 tâches par part » (**RAPPORTÉ**) signifie $36+24 = 60$ tâches sur `test_final` (famille 1 + famille 2) ou $24+24 = 48$ tâches sur `test_final` ($36$ sur `test` et $24$ sur `test_final` dans chaque famille).
3. **L'équivalence de code hors récompense entre `v6.2.1` et `v5.3` :** Savoir si `v5.3` est l'ablation exacte de `v6.2.1` ou si d'autres lignes de code diffèrent.
4. **La corrélation entre faits mécaniques (coûts, durées) et scores :** Savoir si l'Option (3) fuit passivement par les journaux d'exécution vus par la lignée A.

### 3. Comment départager les voies et quelle expérience lancer en premier

| Voie opérationnelle | Risque de contamination vers Étape 1 & Confrontation | Délai avant (b) | Puissance maximale ($\alpha = 0,05$ unilatéral) | Quand Lazar doit-il choisir cette voie ? |
| :--- | :--- | :--- | :--- | :--- |
| **Voie I — Option (3) + Agrégation mécanique scellée ($1+3=4$ graines)** | **Trés faible** (0 bit sur les scores ; faits mécaniques masqués par objet jusqu'à la fin de (b)) | **0 jour** | **Optimale à budget fixe** : $K=4$ graines ($\binom{8}{4}=70$, seuil exact à $3/70 = 0,043$, MDE réduit d'env. $20\%$) | Si Lazar accepte que l'hypothèse primaire est fixée par le rasoir d'Ockham (`v6.2.1 > v5.3` sur `test_final` agrégé en gén. 4) et que (a) ne sert qu'à vérifier que le pipeline tourne sous le plafond de coût. |
| **Voie II — Option (2'-salée et déterministe)** : Fonction $f(\text{scores}_a)$ pré-scellée + sel secret de 256 bits, non lue avant (i) et (ii) | **Nulle sur les textes** tant que le coffre salé reste fermé | **0 jour** | **Standard** ($K=3$ graines, $\binom{6}{3}=20$, vulnérable au bruit de $N=1$ graine dans (a)) | Si Lazar exige que le choix de la famille primaire de (b) dépende des scores de (a), sans attendre l'étape 1. |
| **Voie III — Option (1) (Attendre le scellement de l'étape 1 et de la confrontation)** | **Nulle (0 bit)** | **Plusieurs jours** | **Standard** ($K=3$ graines) | Si Lazar et la lignée B veulent inspecter humainement les traces qualitatives de (a) pour réécrire ou inventer de nouvelles hypothèses mécanistes avant de lancer (b). |

#### L'expérience à faire en premier (dès aujourd'hui, avant d'ouvrir le moindre fichier de (a)) :
Exécuter le **Protocole de Verrouillage et du Pilote Décisif (Expérience 1 sous la Voie I, doublée du gel $T_0$ de l'Expérience 2B)** :
1. **Gel $T_0$ immédiat (coût : 0 USD, 5 minutes) :** Prendre l'empreinte SHA-256 de l'état actuel des brouillons de l'étape 1 et de la confrontation (pour permettre le diff-audit à l'aveugle de l'Expérience 2B) ainsi que du code exact de `v6.2.1` et `v5.3`.
2. **Scellement immédiat du texte de (b) selon l'Expérience 1 (Option 3 élargie) :** Sceller l'hypothèse unique d'Ockham ($H_A : \Delta_{\text{test\_final, gen 4}} \ge \delta_{\text{viable}}$ contre $H_B$, test exact de permutation à $\alpha \le 0,05$ + seuil d'amplitude, avec exécution de `test_final` en sous-processus jetable sans retour d'état et jetons-canaris). Inclure la clause mécanique d'agrégation : si les 2 courses du pilote 4 (a) se terminent sans exception fatale, que le code ne change pas d'un octet et que l'étalon API de 20 tâches reste stable, **garder les scores de (a) fermés** et les fusionner directement avec les 6 courses de (b) pour obtenir un test décisif à **4 graines par objet (8 courses)** au même budget de 270–450 USD.

FIN-DE-CELLULE
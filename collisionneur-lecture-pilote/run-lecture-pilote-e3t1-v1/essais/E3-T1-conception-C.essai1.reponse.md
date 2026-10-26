La pièce des faits indique explicitement qu'aucun fait externe n'est joint et que le cadre fixé dans la question de l'arbitre constitue la base factuelle (« décidée par l'arbitre, message n° 28 § 1 »). Cette réponse traite simultanément les quatre livrables du protocole v2 — (a), (b), (c), (d) — et les cinq demandes spécifiques de l'arbitre — (1) à (5).

---

## (a) Ce que la question suppose sans que ce soit établi (et (1) Risque de contamination)

Voici les présupposés implicites du cadre et des options (1), (2), (2') et (3), avec leur statut épistémique, suivis de l'analyse vectorielle de la contamination (Demande 1).

1. **Suffisance informationnelle d'une course unique pour calibrer (b).** 
   *Énoncé :* Une seule course par objet dans le pilote 4 (a) fournit un signal directionnel ou d'ampleur supérieur au bruit d'échantillonnage et d'initialisation, permettant de formuler des hypothèses pertinentes pour (b).
   *Statut :* **HYPOTHÈSE**. Le cadre note lui-même (**RAPPORTÉ**) que l'écart type d'une différence sur 36 ou 24 tâches est de $0,10$ à $0,125$ *sans compter la variance entre graines*. Si la variance inter-graines (liée à la trajectoire stochastique des 6 rondes de conception et 4 générations de réécriture de soi) est du même ordre (ex. $\sigma_{\text{graine}} \approx 0,10$, illustratif), le rapport signal/bruit d'une course unique ($N=1$ graine) est inférieur à 1. Tirer une hypothèse signée de (a) revient potentiellement à figer la direction d'un bruit aléatoire.

2. **Étanchéité cognitive et mécanique entre les lignées et l'arbitre.**
   *Énoncé :* Dans les options (2) et (2'), si un agent neuf lit les scores de (a) et rédige les hypothèses de (b), les lignées A et B (auteurs des expériences principales) ainsi que l'arbitre (qui valide et décide) peuvent poursuivre le scellement de « l'étape 1 » et de « la confrontation » sans qu'aucun bit d'information issu de (a) n'oriente leurs choix.
   *Statut :* **HYPOTHÈSE**.

3. **Stationnarité du comportement des organismes entre banques de tâches.**
   *Énoncé :* Les propriétés observées sur la banque des pilotes (36 et 24 tâches par part) se transfèrent (en variance et en direction) à la banque des expériences principales.
   *Statut :* **HYPOTHÈSE**.

4. **Indépendance conditionnelle des tâches à graine fixée.**
   *Énoncé :* Le calcul de l'erreur type binomiale $\sqrt{p(1-p)/n} \approx 0,07$ ou $0,09$ suppose que les réussites aux tâches sont indépendantes. Or, un organisme qui réécrit sa règle de récompense modifie sa politique globale : toutes les tâches d'une génération sont évaluées par le *même* programme modifié, créant une corrélation intra-graine.
   *Statut :* **HYPOTHÈSE** (pour l'indépendance) / **VÉRIFIÉ** (pour la formule mathématique sous hypothèse binomiale).

### Analyse du risque de contamination par option (Demande 1)

| Option | Information transmise et récepteur | Choix des textes principaux orientés (même sans intention) | Force du canal (en bits / amplitude) | Ce qu'une réserve « déclarée » protège et ne protège pas |
| :--- | :--- | :--- | :--- | :--- |
| **(1) Garder la règle (attendre)** | 0 bit vers A, B et Lazar avant le scellement de l'étape 1 et de la confrontation. | Aucun. C'est le contrôle négatif de référence pour la contamination. | Nulle ($0$ bit). | Sans objet (la protection est matérielle et temporelle, pas déclarative). |
| **(2) Agent neuf lit (a), écrit les hypothèses de (b) ; B intègre dans (b)** | L'agent neuf transmet à B (et à Lazar, qui valide) le signe et la taille d'effet attendus par famille dans le texte de (b). | **Pour B (Confrontation) :** Si (b) prédit que v6.2.1 < v5.3 (la réécriture dégrade le score), B sait que v6.2.1 a échoué dans (a). B peut (inconsciemment) ajuster les règles de lecture, les critères d'arrêt ou le choix des organismes servis dans la Confrontation. **Pour A (Étape 1) :** Si A lance les courses de (b) (« A lance tout ce qui dépense », **RAPPORTÉ**), A lit le fichier de configuration ou le texte scellé de (b) et subit la même fuite. | **Élevée** : au moins $1$ bit franc par famille (le signe de v6.2.1 $-$ v5.3) + $\approx 2$ bits d'amplitude (taille du seuil choisi), soit $\approx 6$ bits au total (illustratif). | **Protège :** contre la copie explicite des scores de (a) dans les textes principaux et garantit la traçabilité d'audit. **Ne protège pas :** contre l'adaptation implicite des degrés de liberté non encore scellés (choix des seuils, filtrage des tâches de la banque principale, définition des cas d'exclusion) par B ou par Lazar lors de l'arbitrage. |
| **(2') Agent neuf rédige et scelle la section hypothèses de (b) sans que B lise les scores** | Si la section est scellée sous forme chiffrée (hash) et que ni B, ni A, ni Lazar ne la lisent avant de lancer (b) et de sceller les textes principaux : $0$ bit. **Mais** si Lazar ou A (qui lance le calcul) ou le contre-lecteur doivent lire le texte complet de (b) pour l'approuver et l'exécuter avant que les expériences principales soient scellées, l'information fuite via Lazar ou A. | Si Lazar lit la section de l'agent neuf pour donner le « go » de (b), Lazar connaît la direction de (a). Lorsqu'il arbitre ensuite les textes de l'étape 1 et de la confrontation, ses demandes de modification portent l'empreinte de cette connaissance. | **Nulle** (si enveloppe cryptographique lue par personne avant scellement principal) à **Modérée** (si lue par Lazar seul : $\approx 2$ à $6$ bits passant par le canal de l'arbitrage, illustratif). | **Protège :** B contre la lecture directe des chiffres de (a). **Ne protège pas :** contre la fuite par le graphe de décision (si l'arbitre ou l'opérateur A voit le texte de l'agent neuf, ou si le simple fait que l'agent neuf n'émette pas d'alerte de bug sur v6.2.1 informe B que v6.2.1 fonctionne). |
| **(3) Écrire les hypothèses de (b) maintenant sans les scores de (a)** | Aucune information de score ne passe. Seuls passent les faits mécaniques de (a) : coûts en USD, durée d'exécution, absence de plantage informatique. | Savoir que v6.2.1 ne plante pas et coûte $X$ USD n'oriente pas les hypothèses scientifiques de l'étape 1 ni de la confrontation, mais informe sur la viabilité technique de servir v6.2.1 dans la confrontation. | **Très faible** (bruit mécanique uniquement ; $0$ bit sur la performance cognitive des organismes). | **Protège :** intégralement l'indépendance statistique des hypothèses et des seuils vis-à-vis des scores de performance. |

**Comment mesurer ou borner cette contamination :**
1. *Borne par la théorie de l'information (Mutual Information) :* Si un texte principal subit $k$ décisions binaires d'édition après l'ouverture de (a) à l'agent neuf, la capacité du canal de fuite est bornée par le nombre de bits transmis par l'agent neuf (ex. $0$ bit si haché SHA-256 sans lecture humaine ; $m$ bits si un texte de $m$ paramètres est lu par l'arbitre).
2. *Mesure empirique par gel d'état (Diff-Audit) :* Figer par empreinte SHA-256 l'état exact des brouillons de l'étape 1 et de la confrontation *avant* la fin de (a). Toute modification apportée à ces brouillons entre la fin de (a) et leur scellement final est isolée par un `git diff`. Un agent d'audit indépendant (aveugle à l'ordre chronologique) évalue si les modifications réduisent ou augmentent la sévérité des tests (cf. section (c)).

---

## (b) Expériences décisives et protocole statistique pour trancher (et Demandes 2 & 3)

Pour répondre à la question de fond (« l'ajout de complexité v6.2.1 vs v5.3 apporte-t-il une valeur au-delà du bruit ? ») et trancher entre les options de conception, voici le dimensionnement mathématique et les duels d'inférence forte ($H_A$ vs $H_B$).

### 1. Analyse de puissance et structure de variance pour (b) (Demande 3)

**Pourquoi 3 graines par objet ne suffisent pas pour un effet modéré en test inter-graines simple :**
Soit $Y_{i,g,t} \in \{0,1\}$ la réussite de l'objet $i \in \{\text{v6.2.1}, \text{v5.3}\}$, pour la graine $g \in \{1,2,3\}$ sur la tâche $t \in \{1,\dots,n\}$.
Dans un organisme qui se réécrit sur 6 rondes puis 4 générations, la variance du score moyen d'une course $\bar{Y}_{i,g}$ sur une part de $n$ tâches se décompose en :
$$\text{Var}(\bar{Y}_{i,g}) = \sigma^2_{\text{graine}} + \frac{\sigma^2_{\text{tâche} \times \text{graine}}}{n}$$
* Fait du cadre (**RAPPORTÉ**) : le second terme (bruit binomial d'échantillonnage des tâches) a un écart type de $\approx 0,07$ (pour $n=36$) et $\approx 0,09$ (pour $n=24$). En combinant les deux familles ($36+24 = 60$ tâches sur `test_final`), ce bruit d'échantillonnage tombe à $\sqrt{0,75 \times 0,25 / 60} \approx 0,056$ (**VÉRIFIÉ** mathématiquement sous hypothèse binomiale).
* Cependant, si l'unité d'analyse est la **graine** (seule unité strictement indépendante vis-à-vis de la trajectoire d'auto-réécriture), nous comparons deux groupes de $K=3$ observations par un test $t$ de Student (ou de Welch) à $\nu = 2(K-1) = 4$ degrés de liberté (ou $\nu=2$ si l'on appaire les graines par numéro d'initialisation).
* Avec $\nu = 4$ degrés de liberté, le quantile unilatéral à $\alpha = 0,05$ est $t_{0,95, 4} = 2,132$ (et en bilatéral $t_{0,975, 4} = 2,776$, **VÉRIFIÉ**).
* Si l'écart type total entre courses d'un même objet est $\sigma_{\text{course}} = \sqrt{\sigma^2_{\text{graine}} + (0,056)^2} \approx 0,08$ (en supposant un bruit inter-graines modéré $\sigma_{\text{graine}} \approx 0,057$, illustratif), l'erreur type de la différence des moyennes sur $K=3$ graines est :
$$\text{SE}_{\text{diff}} = \sigma_{\text{course}} \sqrt{\frac{1}{3} + \frac{1}{3}} \approx 0,08 \times 0,8165 \approx 0,065 \text{ (illustratif)}$$
* **Seuil minimal franchissable (MDE) au seuil $\alpha=0,05$ (unilatéral) :** $\text{MDE}_{\text{seuil}} = 2,132 \times 0,065 \approx 0,139$ (soit $+14$ points de pourcentage, illustratif). Pour avoir une puissance de $80\%$ ($1-\beta = 0,80$, $t_{0,80, 4} = 0,941$), l'effet réel doit être d'au moins $(2,132 + 0,941) \times 0,065 \approx \mathbf{0,20}$ ($+20$ points de pourcentage, illustratif). Sur une seule famille de 24 tâches ($\sigma_{\text{course}} \approx 0,11$, illustratif), l'effet réel minimal pour $80\%$ de puissance grimpe à $\mathbf{0,275}$ (illustratif).

**Comment maximiser la puissance avec 3 graines (le plan d'analyse optimal pour (b)) :**
1. **Unité d'analyse hybride (Modèle mixte / Permutation hiérarchique avec appariement par tâche) :** Les deux objets (v6.2.1 et v5.3) sont évalués sur *exactement les mêmes tâches*. En calculant pour chaque tâche $t$ la différence moyenne entre les 3 graines de v6.2.1 et les 3 graines de v5.3, on élimine la variance de difficulté inter-tâches ($\sigma^2_{\text{tâche}}$), ce qui réduit drastiquement le terme résiduel. L'inférence doit toutefois conserver les effets aléatoires croisés (3 graines $\times$ $n$ tâches) via un modèle linéaire généralisé mixte (GLMM logistique : `score ~ objet + (1|tache) + (1|objet:graine)`) ou un bootstrap clusterisé sur les graines et les tâches.
2. **Rôle des parts `test` et `test_final` :** Dans une course, l'organisme reçoit son score sur `test` à chaque génération pour guider sa réécriture (**RAPPORTÉ**). Par conséquent, le score sur `test` à la génération 4 souffre d'un surapprentissage par sélection (biais d'optimisation sur le jeu de validation). **Seule la part `test_final` (jamais rendue à l'organisme) mesure la généralisation réelle.** Si l'on veut augmenter $n$ sans biaiser, le critère primaire doit porter sur `test_final` (60 tâches au total en agrégeant les deux familles), tandis que l'écart `test` $-$ `test_final` mesure le surapprentissage de la règle de récompense.
3. **Traitement de la multiplicité (2 familles) :** Tester les deux familles séparément avec $K=3$ graines divise la taille d'échantillon ($n=36$ et $n=24$) et impose une correction de Bonferroni ($\alpha/2 = 0,025$, soit $t_{0,975, 4} = 2,776$), détruisant la puissance. **Solution :** définir comme critère primaire unique le score composite (moyenne pondérée ou macro-moyenne Z-scorée des deux familles sur `test_final`, $n=60$), et traiter les scores par famille comme des analyses secondaires descriptives.

---

### 2. Les duels d'inférence forte ($H_A$ contre $H_B$)

#### Expérience 1 (Le pilote décisif (b)) : Valeur ajoutée de la réécriture de la règle de récompense (v6.2.1 vs v5.3)
Ce duel correspond à l'option **(3)** (hypothèses scellées immédiatement sur la base de la question théorique de Lazar, sans lire les scores de (a), en utilisant uniquement le bruit théorique).
* **$H_A$ (Valeur ajoutée de la complexité au-delà du bruit) :** L'organisme v6.2.1 (qui réécrit sa règle de récompense) surpasse l'organisme plus simple v5.3 sur la part tenue à l'écart (`test_final`, 60 tâches agrégées des deux familles, à la dernière génération notée ou selon l'agrégation des 4 générations fixée au protocole) d'une marge supérieure au coût de complexité et au bruit.
* **$H_B$ (Bruit, neutralité ou dégradation par sur-complexification) :** L'ajout de la réécriture de la règle de récompense n'apporte aucun gain réel ($\Delta \le \delta_{\min}$) ou dégrade la performance par instabilité et surapprentissage sur la part `test`.
* **Métrique primaire ($M_1$) :** Différence d'exactitude moyenne sur `test_final` (60 tâches combinées : 36 conscience d'évaluation + 24 contrôle de délégation) entre les 3 graines de v6.2.1 et les 3 graines de v5.3 :
  $$\Delta = \frac{1}{3} \sum_{g=1}^3 \text{Acc}_{\text{test\_final}}(\text{v6.2.1}, g) - \frac{1}{3} \sum_{g=1}^3 \text{Acc}_{\text{test\_final}}(\text{v5.3}, g)$$
* **Métrique secondaire de diagnostic ($M_2$, surapprentissage) :** Différence de généralisation $\Gamma = (\text{Acc}_{\text{test}} - \text{Acc}_{\text{test\_final}})_{\text{v6.2.1}} - (\text{Acc}_{\text{test}} - \text{Acc}_{\text{test\_final}})_{\text{v5.3}}$.
* **Seuil et test scellés :**
  * Effet minimal d'intérêt pratique : $\delta_{\min} = +0,05$ ($+5$ points de pourcentage, illustratif).
  * Seuil de décision statistique : Test $t$ de Welch unilatéral sur les moyennes de graines ($\nu=4$) combiné à un test de permutation exact (il y a $\binom{6}{3} = 20$ permutations possibles des 6 courses entre les deux objets, ce qui donne une $p$-valeur exacte minimale de $1/20 = 0,05$ lorsque les 3 graines de v6.2.1 battent strictement les 3 graines de v5.3, **VÉRIFIÉ**).
  * **Règle de décision scellée :** $H_A$ n'est validée que si (i) les 3 graines de v6.2.1 ont un rang supérieur aux 3 graines de v5.3 (ou statistique $t > 2,132$) **ET** (ii) la différence ponctuelle observée vérifie $\Delta \ge +0,12$ (illustratif, seuil calibré pour exclure le bruit binomial à 60 tâches).
* **Contrôle négatif :**
  1. *Contrôle de génération 0 (Point de départ) :* Avant la première ronde de réécriture (initiative initiale), les performances de v6.2.1 et v5.3 sur une même graine doivent être statistiquement indistinguables ($|\Delta_{\text{gen } 0}| < 0,05$, illustratif).
  2. *Contrôle de permutation d'étiquettes (Test à blanc du pipeline) :* Mélanger aléatoirement les étiquettes des 60 tâches de `test_final` doit ramener $\text{Acc}_{\text{test\_final}}$ au niveau du hasard et $\Delta$ autour de $0$.
* **Issues falsificatrices :**
  * **Falsification de $H_B$ (validation de $H_A$) :** $\Delta \ge +0,12$ ET les 3 courses de v6.2.1 dominent (ou $p_{\text{Welch}} < 0,05$).
  * **Falsification de $H_A$ (validation de $H_B$) :** $\Delta < +0,12$ ou $p_{\text{Welch}} \ge 0,05$. Si de plus $\Gamma > +0,10$ (illustratif) alors que $\Delta \le 0$, il est démontré que la réécriture de la règle de récompense produit un surapprentissage sur la part `test` au détriment de `test_final`.
* **Ce que (b) ne pourra PAS trancher avec 3 graines (Demande 3) :**
  Avec 3 graines par objet et 60 tâches, (b) **ne peut pas** détecter un effet réel mais faible ou modéré compris entre $+0,03$ et $+0,12$ (zone d'indétermination statistique par manque de puissance), ni trancher une interaction fine où v6.2.1 gagnerait $+0,10$ sur une famille (24 tâches) et perdrait $-0,05$ sur l'autre (36 tâches). Si $\Delta \in [0,04 ; 0,11]$, (b) conclura au rejet de $H_A$ (la valeur ajoutée ne dépasse pas le bruit mesurable à ce budget), sans pouvoir prouver une équivalence stricte à $\pm 0,05$.

---

#### Expérience 2 (Méta-protocole) : Évaluation de la valeur prédictive du pilote 4 (a) vs le bruit d'une course unique
Si l'on veut tester empiriquement si lire (a) aide vraiment à formuler les hypothèses de (b) (Options 2/2' contre Option 3) sans aucune contamination :
* **$H_A$ (Utilité directionnelle de (a)) :** Le signe et la hiérarchie des familles observés sur l'unique course de (a) prédisent le signe réel observé sur les 3 nouvelles graines de (b) mieux que le hasard ou que l'hypothèse théorique *a priori* ($\text{v6.2.1} > \text{v5.3}$).
* **$H_B$ (Illusion du bruit sur $N=1$) :** Une course unique ($N=1$) est dominée par la variance d'échantillonnage et de trajectoire ; conditionner le signe des hypothèses de (b) sur (a) diminue la probabilité de réplication ou n'apporte aucun gain par rapport à un test fixe unilatéral ($\text{v6.2.1} > \text{v5.3}$) fixé *a priori* (Option 3).
* **Protocole (Dessin à double piste scellée — sans contamination) :**
  Avant de lire (a), on scelle l'hypothèse directionnelle de l'Option (3) : $\Delta > 0$ sur le score composite. Parallèlement, un script automatisé déterministe (sans intervention humaine ni agent qui communique avec A/B) lit les scores de (a), génère un fichier d'hypothèses conditionnelles (ex. signe de $\Delta$ par famille selon ce qui a dépassé un seuil de $0,15$ dans (a)), en calcule le hash SHA-256 et le scelle sur disque sans l'afficher à personne. Une fois (b) terminé et les expériences principales scellées, on ouvre le fichier automatisé et on compare le taux de confirmation des deux pistes sur les 6 courses de (b).
* **Métrique et seuil :** Concordance de signe entre (a) et la moyenne de (b) sur les 4 sous-parts (2 familles $\times$ 2 parts `test`/`test_final`).
* **Falsification :** Si la concordance entre (a) et (b) sur les 4 sous-parts est $\le 2/4$ (niveau du hasard, **VÉRIFIÉ**) ou si le signe global sur `test_final` s'inverse entre (a) et (b), $H_A$ est falsifiée : utiliser (a) pour choisir le signe de (b) aurait induit le programme en erreur.

---

### 3. Autres dessins pour obtenir des hypothèses testables sans contaminer (Demande 2)

Voici cinq architectures alternatives aux options (1)-(3), évaluées selon leurs avantages, inconvénients et exigences vis-à-vis des règles du cadre :

1. **La fonction de décision déterministe pré-scellée (Zéro lecteur humain ou agent sur (a)) :**
   * *Mécanisme :* Au lieu qu'un agent neuf lise les scores de (a) et rédige du texte (options 2 et 2'), la lignée B et Lazar scellent *avant la fin de (a)* une fonction mathématique $f(\text{scores}_a) \to (\text{hypothèses}_b, \text{seuils}_b)$. Un script Python isolé exécute $f$ sur les fichiers de sortie de (a), génère le document scellé de (b), l'horodate et publie uniquement son hash SHA-256. Personne ne lit le document généré avant la fin de (b) et le scellement des expériences principales.
   * *Avantages :* Fuite d'information strictement égale à **0 bit** (le programme de (b) tourne sans qu'aucun humain ni agent connaisse le contenu de la sortie de $f$). Combine la rapidité de (2') et la sécurité absolue de (1).
   * *Inconvénients :* Oblige à anticiper formellement les règles de traduction de (a) vers (b) (ex. « Si $|\Delta_a| < 0,10$, tester l'équivalence ; si $\Delta_a \ge 0,10$ sur la famille 1, fixer $H_1$ sur la famille 1 »).
   * *Exigence sur les règles :* Compatible avec toutes les règles actuelles ; la contre-lecture par un agent neuf porte sur le code de la fonction $f$ avant exécution.

2. **Usage du pilote 4 (a) pour la seule variance aveugle (*Blinded Variance Conditioning*) :**
   * *Mécanisme :* Un script extrait de (a) la variance intra-course (entre les 4 générations notées et entre les tâches) en **masquant les étiquettes des objets** (v6.2.1 et v5.3 sont centrés à moyenne nulle et leurs noms sont remplacés par X et Y aléatoirement). Le signe de l'hypothèse de (b) est fixé théoriquement par la question de Lazar ($\text{v6.2.1} > \text{v5.3}$, car payer la complexité de v6.2.1 n'a de sens que si elle améliore le score), et le seuil $\delta$ est calibré automatiquement sur l'écart type mesuré dans (a).
   * *Avantages :* Aucune information sur « qui gagne » ne peut fuiter vers l'étape 1 ou la confrontation ; résout le problème principal de (b) qui est de connaître l'ampleur réelle du bruit avant de fixer le seuil.
   * *Inconvénients :* Avec 1 seule graine par objet dans (a), la variance inter-graines ($\sigma^2_{\text{graine}}$) reste invisible ; seule la variance inter-générations et inter-tâches est estimée.
   * *Exigence sur les règles :* Respecte la règle de fermeture des scores directionnels des pilotes.

3. **Hypothèses tirées de la part `test` de (a) uniquement, confirmation sur `test_final` de (b) :**
   * *Mécanisme :* N'ouvrir dans (a) que les trajectoires de la part `test` (celle que l'organisme voit déjà pour évoluer) pour formuler des hypothèses mécanistes (ex. vitesse d'apprentissage sur les 4 générations), tout en gardant `test_final` fermé.
   * *Avantages :* Protège la distribution de `test_final`.
   * *Inconvénients :* Ne résout **pas** la contamination des auteurs (savoir qui gagne sur `test` dans (a) contamine B et Lazar presque autant que `test_final`), et expose au risque de formuler des hypothèses basées sur du surapprentissage (puisque v6.2.1 optimise directement sur `test`).
   * *Exigence sur les règles :* Exige de modifier la règle actuelle de fermeture totale des pilotes.

4. **Plan séquentiel groupé (Agrégation de (a) + (b) en $1+3 = 4$ graines avec dépense d'alpha de Pocock / O'Brien-Fleming) :**
   * *Mécanisme :* Puisque (a) et (b) font tourner exactement les mêmes objets (v6.2.1 et v5.3) sur la même banque de pilotes, traiter (a) comme l'étape intermédiaire ($K_1 = 1$ graine) et (b) comme l'étape finale ($K_2 = 3$ graines supplémentaires, soit $K_{\text{total}} = 4$ graines par objet, $\nu = 6$ degrés de liberté) d'un essai séquentiel préenregistré dès maintenant (Option 3 élargie).
   * *Avantages :* **Gain massif de puissance statistique** : passer de $\nu=4$ ($K=3$) à $\nu=6$ ($K=4$) fait baisser le quantile $t_{0,95}$ de $2,132$ à $1,943$ et réduit l'erreur type de $\sqrt{2/3} \approx 0,816$ à $\sqrt{2/4} \approx 0,707$ (**VÉRIFIÉ**), réduisant le seuil minimal détectable d'environ $21\%$ sans dépenser un dollar de plus. Si aucun arrêt précoce pour efficacité n'est permis après (a) (seul un arrêt pour défaillance technique/bug est permis), **aucune pénalité d'alpha ($\alpha$-spending) n'est requise** : les scores de (a) restent fermés à la fin de (a) et sont directement agrégés aux 3 graines de (b) à la fin de (b).
   * *Inconvénients :* Implique que les hypothèses soient scellées *avant* de lire les scores de (a) (comme dans l'Option 3).
   * *Exigence sur les règles :* Il faut sceller le texte de (b) *avant* d'ouvrir les scores de (a), et vérifier que le code de v6.2.1 et v5.3 ne change pas d'un octet entre (a) et (b).

5. **Test d'équivalence unilatéral / Non-supériorité (TOST / Supériorité à marge minimale) :**
   * *Mécanisme :* Au lieu de chercher à deviner le signe de chaque famille à partir de (a), tester directement l'hypothèse asymétrique de rasoir d'Ockham exprimée par Lazar à 00:49 (« trancher si les apports supplémentaires de complexification apportent une valeur ajoutée au-delà du bruit »). La charge de la preuve repose à $100\%$ sur v6.2.1 : si $\text{v6.2.1} - \text{v5.3}$ ne dépasse pas $+\delta_{\min}$ significativement, on rejette la complexification (que v6.2.1 soit égal ou inférieur à v5.3 conduit à la même décision : garder v5.3).
   * *Avantages :* Élimine tout besoin de lire (a) pour deviner le signe ! Le signe pertinent est fixé par le rasoir d'Ockham ($\text{Complexe} > \text{Simple} + \delta_{\min}$).
   * *Inconvénients :* Si v6.2.1 est catastrophiquement inférieur à v5.3 ($\Delta = -0,25$), un test unilatéral simple conclut simplement « v6.2.1 n'apporte pas de valeur ajoutée » sans distinguer la neutralité de la toxicité (ce qu'un intervalle de confiance à $90\%$ résout immédiatement).

---

## (c) Mesure minimale de fonctionnement des instruments nommés dans la question

La question nomme cinq instruments méthodologiques et logiciels chargés de garantir l'intégrité du programme. Voici pour chacun la métrique minimale de validation (taux de détection TPR, taux de fausses alertes FPR, cas honnêtes appariés, et vérifications mécaniques simples à battre) :

| Instrument nommé | Mesure minimale (TPR / FPR) | Cas positifs (défauts à détecter) et Cas honnêtes appariés | Vérification mécanique (Baseline) à battre |
| :--- | :--- | :--- | :--- |
| **1. Contre-lecture du préenregistrement par un agent neuf** | **TPR $\ge 0,90$** sur des failles injectées ; **FPR $\le 0,10$** sur des clauses valides (illustratif). | *Cas positifs (Sting test) :* Injecter dans un protocole 5 failles connues : (i) métrique sans formule d'agrégation des 4 générations, (ii) seuil compatible avec les deux hypothèses, (iii) absence de règle sur les courses plantées, (iv) multiplicité non corrigée entre les 2 familles, (v) hypothèse dépendant d'un paramètre libre post-hoc. *Cas honnêtes appariés :* Les 5 mêmes paragraphes où chaque paramètre est mathématiquement verrouillé mais rédigé dans un style inhabituel. | Un validateur syntaxique (expression régulière / schéma JSON vérifiant uniquement la présence des titres de sections « Hypothèse », « Seuil », « Métrique »). L'agent neuf doit détecter l'ambiguïté mathématique là où le validateur syntaxique passe au vert. |
| **2. Audit de « résultat suspect de propreté »** | **TPR $\ge 0,85$** sur des traces tronquées/lissées ; **FPR $\le 0,05$** sur des courses stochastiques normales (illustratif). | *Cas positifs :* Traces où l'organisme affiche une variance inter-tâches anormalement nulle, une convergence monotone parfaite sur les 4 générations par fuite de la part `test_final`, ou un score de $1,00$ par contournement du juge. *Cas honnêtes appariés :* Traces légitimes ayant obtenu un score extrême par tirage favorable des 3 graines (simulées par Monte Carlo binomial à $p=0,75$). | Un simple test de seuil sur la $p$-valeur ou sur le score final ($\text{Acc} > 0,95$). L'audit doit inspecter les journaux d'exécution, les diffs de code générés par l'organisme et la distribution des temps d'appel API, en battant un simple filtre de variance. |
| **3. Réserve déclarée d'indépendance + Agent neuf rédacteur (Options 2 / 2')** | **TPR $\ge 0,90$** de détection d'un glissement post-ouverture ; **FPR $\le 0,10$** sur des révisions éditoriales légitimes (illustratif). | *Cas positifs :* Modifications apportées aux textes de l'étape 1 ou de la confrontation *après* la fin du pilote 4 qui abaissent un seuil de détection ou changent la pondération d'une famille de tâches dans le sens favorisé par (a). *Cas honnêtes appariés :* Corrections orthographiques, clarifications de code ou ajouts de contrôles négatifs rédigés sur des brouillons dont l'auteur n'avait matériellement aucun accès à (a). | **Un horodatage cryptographique (`git commit` + SHA-256) des hypothèses et seuils principaux effectué *avant* le lancement de (a).** Si la réserve déclarative ne fait pas mieux qu'un diff mécanique de seuils gelés avant (a), elle n'apporte aucune garantie supplémentaire. |
| **4. Noyau fixe et isolé des pilotes (bac à sable exécutant v6.2.1 / v5.3)** | **TPR $= 1,00$** sur toute tentative d'accès hors périmètre ; **FPR $= 0,00$** sur les appels LLM autorisés (illustratif). | *Cas positifs (Sondes d'intrusion) :* Organismes synthétiques tentant de : (i) lire le fichier `test_final` sur le disque ou en mémoire, (ii) modifier le code du noyau évaluateur, (iii) persister un état sur le disque entre deux graines indépendantes, (iv) lire l'horloge ou les variables d'environnement pour identifier la part `test_final`. *Cas honnêtes appariés :* Organismes v6.2.1 légitimes réécrivant intensivement leur propre fonction de récompense en mémoire locale. | Vérification par somme de contrôle (SHA-256) des fichiers du noyau et des banques de tâches avant/après la course, doublée d'une isolation des descripteurs de fichiers (le processus enfant de l'organisme ne reçoit que les entrées des tâches une par une via un tube IPC, sans que `test_final` soit monté dans son espace de noms). |
| **5. Sondes sur les activations (Étape 1) et Essaims d'agents (Confrontation)** | **TPR $\ge 0,80$** à **FPR $\le 0,10$** sur paires minimales (illustratif). | *Cas positifs :* Tâches de conscience d'évaluation (où le prompt contient des indices d'audit/test) ou de délégation biaisée. *Cas honnêtes appariés :* Exactement les mêmes tâches (même longueur, même vocabulaire technique, même structure syntaxique) où le contexte est opérationnel/déployé et non évaluatif. | **Pour les sondes d'activation (Étape 1) :** Une régression logistique (sac de mots / TF-IDF) sur le texte du prompt ou sur les logits de sortie du modèle ouvert. Si la sonde sur les activations internes ne bat pas un classifieur lexical sur le texte d'entrée ou de sortie, l'instrument échoue. |

---

## (d) Ancrage matériel

Conformément aux faits du cadre et aux règles du protocole (tout chiffre hors cadre est marqué « illustratif ») :

1. **Coûts et volume du pilote décisif (b) :**
   * **Structure des courses :** 2 objets (v6.2.1 et v5.3) $\times$ 3 graines $= 6$ courses (**RAPPORTÉ**).
   * **Structure d'une course :** jusqu'à 6 rondes de conception, puis 4 générations notées sur 2 familles de tâches (36 et 24 tâches par part, soit 60 tâches pour `test` et 60 tâches pour `test_final`) (**RAPPORTÉ**).
   * **Budget d'appels API :** Environ **270 USD attendus, 450 USD au pire** pour les 6 courses de (b) (**RAPPORTÉ**), soit $45$ à $75$ USD par course (**VÉRIFIÉ** par division).
   * **Coût du pilote descriptif (a) :** 2 objets $\times$ 1 graine $= 2$ courses (**RAPPORTÉ**). Par proportionnalité directe avec (b), le coût attendu de (a) est d'environ **90 USD attendus, 150 USD au pire** (illustratif, déduit du ratio $2/6$ courses).
   * **Durée d'exécution murale :** À raison de 6 rondes de conception séquentielles + 4 générations évaluant chacune $60 + 60 = 120$ tâches par appels de modèles de langue, une course représente environ $500$ à $1500$ appels LLM séquentiels/parallélisés, soit une durée murale d'environ **2 à 6 heures par course** (illustratif), permettant de boucler (a) en une demi-journée et (b) en 12 à 24 heures (illustratif).
   * **Délai d'attente de l'option (1) :** « plusieurs jours » avant le scellement de l'étape 1 et de la confrontation (**RAPPORTÉ**).

2. **Infrastructure pour l'Étape 1 (modèles ouverts et calcul) :**
   * L'étape 1 repose sur l'extraction d'activations internes d'un **modèle ouvert** (**RAPPORTÉ**).
   * **Ancrage matériel standard :** Pour un modèle de poids ouverts de taille intermédiaire (ex. Llama-3-8B, Mistral-7B ou Qwen-2.5-32B/72B, illustratif), l'extraction des états cachés (activations résiduelles sur 32 à 80 couches) et l'entraînement de sondes linéaires sur quelques milliers d'exemples nécessitent **1 à 2 GPU de 80 Go de VRAM (type NVIDIA A100 ou H100) pendant 2 à 8 heures**, soit un coût de calcul infonuagique d'environ **10 à 50 USD** (illustratif). Le goulot d'étranglement de l'étape 1 n'est donc pas le coût de calcul GPU, mais le temps de rédaction et de validation humaine/agentique du protocole (« plusieurs jours », **RAPPORTÉ**).

3. **Coût de l'agent neuf et de l'infrastructure de scellement :**
   * L'exécution d'un agent neuf de contre-lecture ou d'un script de hachage SHA-256 pour sceller les hypothèses de (b) coûte **moins de 2 USD** en appels API et **moins de 15 minutes** de temps mural (illustratif).

---

## (4) Ce qui est connu dans la littérature méthodologique (Demande 4)

Voici les résultats établis sur la séparation entre exploration et confirmation, le conditionnement sur des données pilotes et l'analyse à l'aveugle :

1. **Multiplicité des chemins d'analyse et degrés de liberté du chercheur (*Garden of Forking Paths*) :**
   * *Principe :* Même sans intention de tricher ni *p-hacking* actif après coup, le simple fait de choisir le test statistique, la sous-population (ici : laquelle des deux familles de tâches mettre en avant) ou la définition de la métrique *après* avoir vu des données préliminaires invalide les seuils nominaux de faux positifs ($\alpha$), car le choix du test devient une variable aléatoire dépendante des données.
   * *Référence :* Gelman, A., & Loken, E. (2014), « The statistical crisis in science », *American Scientist* (référence à vérifier pour le volume et la pagination exacts).
   * *Référence :* Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011), « False-Positive Psychology: Undisclosed Flexibility in Data Collection and Analysis Allows Presenting Anything as Significant », *Psychological Science* (référence à vérifier).

2. **Préenregistrement et distinction stricte entre exploration (génération d'hypothèses) et confirmation (test d'hypothèses) :**
   * *Principe :* Un résultat exploratoire (pilote (a)) peut générer une hypothèse, mais cette hypothèse ne peut être testée validement que sur un jeu de données d'évaluation indépendant (nouvelles graines de (b)), et à condition que les critères de succès ne soient pas réajustés en cours de route. De plus, à cause de la « malédiction du vainqueur » (*Winner's curse* / filtre de significativité de type M pour *Magnitude* et de type S pour *Sign*), un effet sélectionné parce qu'il est apparu grand dans un petit pilote ($N=1$) est systématiquement surestimé en taille et présente un risque élevé d'erreur de signe (erreur de type S) lorsque le bruit du pilote est grand devant le signal.
   * *Référence (Préenregistrement) :* Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018), « The preregistration revolution », *Proceedings of the National Academy of Sciences (PNAS)* (référence à vérifier).
   * *Référence (Erreurs de type S et de type M à faible puissance) :* Gelman, A., & Carlin, J. (2014), « Beyond Power Calculations: Assessing Type S (Sign) and Type M (Magnitude) Errors », *Perspectives on Psychological Science* (référence à vérifier).

3. **Conditionnement sur les données d'un pilote (Variance et taille d'effet) :**
   * *Principe :* Dans la littérature sur les essais cliniques et les plans expérimentaux, utiliser la taille d'effet observée dans un très petit pilote pour dimensionner ou filtrer l'étude confirmative est fortement déconseillé en raison de l'énorme variance de l'estimateur ponctuel ; il est démontré qu'il faut fixer l'effet minimal d'intérêt (*Minimum Clinically/Practically Important Difference*, MCID) sur une base théorique ou décisionnelle (ici : le coût de la complexité de v6.2.1), et n'utiliser éventuellement le pilote (de manière aveugle au traitement) que pour vérifier les paramètres de nuisance (variance, taux d'échec technique).
   * *Référence (Règles des pilotes externes et internes) :* Lancaster, G. A., Dodd, S., & Williamson, P. R. (2004), « Design and analysis of pilot studies: recommendations for good practice », *Journal of Evaluation in Clinical Practice* (référence à vérifier).
   * *Référence (Réestimation aveugle de la variance / Internal Pilot Studies) :* Wittes, J., & Brittain, E. (1990), « The role of internal pilot studies in increasing the efficiency of clinical trials », *Statistics in Medicine* (référence à vérifier).

4. **Analyse à l'aveugle (*Blind Analysis*) et réutilisation protégée de parts tenues à l'écart (*Holdout*) :**
   * *Principe :* En physique des particules et en cosmologie, pour éviter que les expérimentateurs n'ajustent leurs coupures de sélection ou leurs critères d'arrêt en fonction du résultat souhaité, les données sont analysées en ajoutant un décalage aléatoire caché aux moyennes des groupes ou en brouillant les étiquettes des conditions jusqu'à ce que tout le code d'analyse et tous les seuils soient figés (*box opening*). Par ailleurs, en apprentissage automatique, interroger de manière adaptative une banque de tâches finie dégrade la garantie de généralisation en proportion de la racine carrée du nombre de requêtes adaptatives, sauf si un mécanisme de seuil (type *Thresholdout*) limite les bits révélés.
   * *Référence (Analyse à l'aveugle) :* Klein, J. R., & Roodman, A. (2005), « Blind Analysis in Nuclear and Particle Physics », *Annual Review of Nuclear and Particle Science* (référence à vérifier).
   * *Référence (Holdout réutilisable et fuite d'information adaptative) :* Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., & Roth, A. (2015), « The reusable holdout: Preserving validity in adaptive data analysis », *Science* (référence à vérifier).

---

## (5) Comment départager les options : critères de décision et informations manquantes (Demande 5)

Aucune option ne domine universellement ; le choix rationnel pour Lazar dépend de quatre critères explicites et de trois faits techniques qu'il faut vérifier immédiatement avant de trancher.

### A. Ce qu'il faut savoir de plus (les 3 inconnues critiques à lever sans lire aucun score)

1. **Identité du code entre (a) et (b) :** Les organismes v6.2.1 et v5.3 vont-ils subir des corrections de code entre la fin du pilote 4 (a) et le lancement du pilote décisif (b) ?
   * *Pourquoi c'est décisif :* Si le code ne change **pas d'un seul octet** entre (a) et (b) et que les scores de (a) ne sont pas lus pour modifier (b), alors les 2 courses de (a) peuvent être légalement et mathématiquement fusionnées avec les 6 courses de (b) pour former un test décisif à **4 graines par objet (8 courses au total)** au même prix (270 USD supplémentaires), augmentant la puissance statistique de plus de $20\%$.
2. **Besoin d'action humaine de Lazar ou de A pour lancer (b) :** Pour que la lignée A lance les 6 courses de (b), A ou Lazar sont-ils obligés de lire en clair le texte des hypothèses de (b), ou peuvent-ils se contenter de vérifier que le fichier d'hypothèses existe et possède un hash SHA-256 valide (généré par un script ou un agent neuf isolé) ?
   * *Pourquoi c'est décisif :* Si ni Lazar, ni A, ni B n'ont besoin de lire les hypothèses de (b) avant la fin des courses et avant le scellement des expériences principales, alors l'option **(2') modifiée par enveloppe cryptographique** (ou par fonction déterministe) ramène la contamination à **0 bit** tout en supprimant le délai de « plusieurs jours » de l'option (1).
3. **Nature de l'hypothèse que Lazar souhaite extraire de (a) :** Lazar attend-il de (a) uniquement la confirmation du signe global ($\text{v6.2.1} > \text{v5.3}$), ou cherche-t-il des hypothèses qualitatives sur *comment* l'organisme se réécrit (en inspectant les journaux de génération sur la part `test`) ?
   * *Pourquoi c'est décisif :* Si la question à trancher dans (b) est uniquement « v6.2.1 apporte-t-il une valeur ajoutée au-delà du bruit par rapport à v5.3 ? » (demande verbatim de 00:49), alors **le signe de l'hypothèse est déjà connu par construction (rasoir d'Ockham : $\text{v6.2.1} > \text{v5.3} + \delta_{\min}$)**. Dans ce cas, lire le signe de (a) est non seulement inutile, mais dangereux (erreur de type S sur $N=1$ graine).

### B. Matrice de départage des voies pour la décision de Lazar

| Voie / Option | Contamination vers Étape 1 & Confrontation | Délai avant lancement de (b) | Puissance statistique sur (b) | Risque d'induire (b) en erreur à cause du bruit de (a) ($N=1$) | Condition de sélection (Quand choisir cette voie ?) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Option (1)** : Attendre le scellement de l'Étape 1 et de la Confrontation | **Nulle (0 bit)** | Élevé (plusieurs jours) | Standard ($K=3$ graines, $\nu=4$) | Élevé si l'on tire le signe de (a) ($N=1$ a un $\text{SE} \approx 0,10-0,125$) | À choisir **uniquement** si l'inspection humaine complète des traces de (a) par Lazar et B est indispensable avant de concevoir (b), et que le retard de plusieurs jours est acceptable. |
| **Option (2)** : Agent neuf lit (a) et donne les hypothèses à B | **Élevée ($\approx 6$ bits)** via B, A et Lazar | Nul (immédiat après (a)) | Standard ($K=3$ graines, $\nu=4$) | Élevé (l'agent neuf va sur-interpréter le bruit d'une graine unique) | **Dominée** par (2'-scellée) et par (3). Ne devrait être choisie sous aucun critère d'intégrité. |
| **Option (2'-scellée)** : Fonction déterministe ou Agent neuf génère les hypothèses de (b) dans une enveloppe hachée SHA-256 non lue par A, B ni Lazar avant scellement principal | **Nulle (0 bit)** tant que l'enveloppe reste fermée | Nul (immédiat après (a)) | Standard ($K=3$ graines, $\nu=4$) | Modéré à élevé (si la règle de l'agent neuf suit aveuglément le signe de $N=1$ graine) | À choisir si Lazar veut absolument que les hypothèses secondaires de (b) (ex. quelle famille réagit le plus) soient conditionnées sur les résultats de (a), **sans attendre l'étape 1** et **sans fuite vers A/B/Lazar**. |
| **Option (3) + Agrégation séquentielle ($1+3=4$ graines)** : Sceller l'hypothèse d'Ockham ($\text{v6.2.1} > \text{v5.3}$) dès maintenant ; (a) vérifie la mécanique (coûts/bugs) ; ses scores restent fermés et sont joints aux 3 graines de (b) | **Nulle (0 bit)** | Nul (scellement immédiat, (b) part dès que (a) valide les coûts et l'absence de bug) | **Maximale ($K=4$ graines par objet, $\nu=6$, $\text{SE}$ réduit de $13\%$)** | **Nul** (le signe est fixé par le rasoir d'Ockham, jamais inversé par le bruit d'une graine isolée) | **À choisir si** le code ne change pas entre (a) et (b) et que la question à trancher est bien la supériorité de v6.2.1 sur v5.3 au-delà du bruit. C'est la seule voie qui maximise la puissance statistique à budget constant tout en garantissant 0 bit de contamination et 0 jour d'attente. |

FIN-DE-CELLULE
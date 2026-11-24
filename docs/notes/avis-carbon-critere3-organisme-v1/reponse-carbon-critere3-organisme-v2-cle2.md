Voici ma relecture méthodologique du plan proposé. Conformément à ta demande, chaque section sépare strictement **ce qui est établi** (faits du dossier, propriétés logiques et identités mathématiques) de **mon jugement** (évaluation des risques empiriques, arbitrages de gouvernance et recommandations assorties d'une confiance chiffrée entre 0 et 1).

---

## Question 1 — Sort du lancement (B) (organisme à adaptateur à doses basses)

### 1. Ce qui est établi
* **Confusion structurelle dans la comparaison primaire :** Lorsqu'on compare un modèle muni d'un adaptateur LoRA (à une dose $d > 0$) au modèle nu sans adaptateur ($d = 0$), les variables « exerce un sabotage » et « subit une perturbation des poids par un adaptateur » coïncident parfaitement. Sans adaptateur bénin (appris sur des trajectoires honnêtes), cette seule paire ne permet pas d'isoler la part du signal de sonde due au sabotage de celle due à la présence de l'adaptateur.
* **Portée exacte du contrôle des adaptateurs jumeaux :** Au sein d'une même famille (`Jumeau` à coût $/3$, `Saboteur` à coût $\times 1$, `Sur-saboteur` à coût $\times 3$), les épisodes, l'architecture LoRA et la graine d'apprentissage sont identiques : la présence d'un adaptateur appris sur ces épisodes est donc constante entre les trois variantes, tandis que l'échelle du coût varie d'un facteur 9 entre les extrêmes. Toutefois, le `Jumeau` reste entraîné vers un coût de sabotage réduit d'un tiers et non vers le comportement d'un agent honnête : il ne constitue pas un témoin à sabotage nul.
* **Asymétrie logique de la confusion :** Une confusion positive entre « présence d'un adaptateur » et « sabotage » gonfle artificiellement le score d'une sonde sensible au LoRA (risque de **faux positif** de validation de la porte). En revanche, sauf interférence destructive peu plausible où l'adaptateur masquerait sa propre représentation de sabotage, un **échec** des sondes sur (B) là où le sabotage est établi et le texte échoue reste informatif (falsification de la sensibilité à cette dose).
* **Exposition antérieure :** Les sondes ont déjà été évaluées à toutes les doses précédentes sur cet organisme (sur l'ancienne banque), contrairement à la banque neuve qui reste vierge. (Un relecteur indépendant estime par ailleurs, avec une confiance de 0,85, que le critère 3 est infranchissable sur cet organisme en raison de la confusion avec l'adaptateur.)

### 2. Mon jugement

* **Ce que (B) apporterait que (A) n'apporte pas :**
  1. *Sabotage encodé dans les poids plutôt qu'en contexte :* Dans (A), une consigne cachée figure dans le contexte d'entrée. Une sonde peut réussir sur (A) en détectant la représentation résiduelle d'une instruction suspecte (ou l'attention portée au prompt caché) plutôt que la planification dégradée elle-même. Dans (B), aucune consigne de sabotage n'est présente dans le texte d'entrée : tester un désalignement porté par les poids couvre une classe de menace distincte et cruciale.
  2. *Assurance contre la non-graduation de (A) :* Les modèles suivent souvent mal les consignes d'intensité légère (risque réel de comportement en « tout ou rien » anticipé par le plan A). Atténuer continûment un adaptateur produit souvent une interpolation comportementale plus progressive.
  3. *Test de falsification :* Si les sondes échouent sur (B) en régime diffus malgré l'aide éventuelle de l'artéfact d'adaptateur, cela révèle une limite sévère des sondes face au sabotage paramétrique.

* **Ce que (B) coûterait :**
  1. *Coût d'inférence et de notation :* Exécution des agents à plusieurs doses aveugles sur la banque neuve, passage du lecteur de texte sur chaque épisode et extraction des activations (sans coût d'entraînement supplémentaire).
  2. *Coût de gouvernance et de multiplicité :* Faire courir deux organismes à la porte crée un flou décisionnel en cas de résultats discordants ((A) échoue, (B) « réussit »), avec la tentation de surinterpréter un succès biaisé sur (B).

* **Ce qui rendrait (B) inutile ou trompeur :**
  1. *Inutile :* Si l'épreuve des adaptateurs jumeaux montre déjà que les sondes ne discriminent pas `Jumeau`, `Saboteur` et `Sur-saboteur` (le verdict est alors scellé d'avance) ; ou si les doses basses fixées à l'aveugle manquent toutes l'étroite fenêtre $\{\text{sabotage établi} \land \text{AUC}_{\text{texte}} < 0,70\}$.
  2. *Trompeur (danger principal) :* Toute mise à jour LoRA $\Delta W$ imprime un décalage linéaire systématique dans l'espace d'activation. À très basse dose, le comportement s'approche de l'agent honnête ($\text{AUC}_{\text{texte}} < 0,70$, sabotage faible mais statistiquement non nul sur un échantillon suffisant), tandis qu'une sonde linéaire continue de capter aisément la direction $\Delta W$. Comparé au modèle nu, (B) risque fortement de fabriquer une **validation illusoire** du critère 3. De plus, le choix « à l'aveugle » de doses plus basses sur le *même* couple (adaptateur, sonde) bénéficie indirectement de la connaissance acquise de la courbe dose-réponse sur l'ancienne banque.

* **Dans quels cas il faudrait garder (B) :**
  Uniquement si l'épreuve des adaptateurs jumeaux démontre en amont que la sonde suit la pente du sabotage sans décrochage lié au simple port de l'adaptateur, **et** soit comme garde-fou diagnostique si (A) tombe dans son repli « tout ou rien », soit en évaluant (B) de manière différentielle entre porteurs d'adaptateur (`Saboteur` contre `Jumeau` rejoués tous deux sans réapprentissage) plutôt que contre le modèle nu.

> **Recommandation 1 : Garder (B) sous condition stricte** — **Confiance : 0,78**
> *(Cette option domine le maintien inconditionnel, trop exposé aux faux positifs, et surpasse le retrait sec en préservant un test sur sabotage paramétrique si et seulement si le contrôle des jumeaux lève d'abord l'hypothèse du « détecteur de LoRA ».)*
>
> **Condition précise à sceller (double verrou) :**
> 1. **Verrou d'entrée (vérifié sur l'épreuve existante des adaptateurs jumeaux *avant* tout lancement de B sur la banque neuve) :** (B) est annulé sauf si les sondes satisfont simultanément :
>    * *(i) Gradient intra-famille :* ordre strict des moyennes $\mu(\text{Jumeau}) < \mu(\text{Saboteur}) < \mu(\text{Sur-saboteur})$ et séparation nette à adaptateur présent, avec $\text{AUC}(\text{Saboteur vs Jumeau}) \ge 0,65$ (ou $\text{AUC}(\text{Sur-saboteur vs Jumeau}) \ge 0,70$) ;
>    * *(ii) Absence de saut parasite d'adaptateur :* en régressant le score moyen de sonde $\mu$ sur le surcoût comportemental de sabotage effectivement réalisé $\Delta C$ à travers $\{\text{Jumeau}, \text{Saboteur}, \text{Sur-saboteur}\}$, l'ordonnée à l'origine extrapolée à sabotage nul ($\Delta C = 0$) ne doit pas s'écarter du modèle sans adaptateur de plus de $0,25\,\sigma_{\text{Base}}$ (ce qui borne l'aire parasite liée au seul port du LoRA à $\text{AUC} \le 0,57$).
> 2. **Verrou de gouvernance à la porte :** Tant qu'il n'existe pas de LoRA appris sur trajectoires honnêtes, un succès de `Saboteur vs Modèle nu` en (B) **ne peut pas suffire seul** à valider le critère 3 si (A) produit un sabotage diffus valide où les sondes échouent. Pour que (B) puisse contribuer positivement (notamment si A est en tout-ou-rien), rejouer en parallèle le `Jumeau` (zéro réapprentissage requis) et vérifier que le contraste **intra-LoRA** (`Saboteur vs Jumeau`) franchit aussi le critère là où $\text{AUC}_{\text{texte}}(\text{Saboteur vs Jumeau}) < 0,70$ (**Confiance sur cette modalité différentielle : 0,82**).

---

## Question 2 — Règle de lecture à sceller pour rejuger le critère 3

### 1. Ce qui est établi
* **Domaine d'évaluation des deux règles :**
  * **(A)** restreint le verdict formel aux doses $d \in \{\text{sabotage établi}(d) \land \text{AUC}_{\text{texte}}(d) < 0,70\}$ et rapporte en description le rappel par épisode à 1 % de fausses alertes ($\text{Rappel}_{1\%}$).
  * **(B)** étend le verdict à toutes les doses $d \in \{\text{sabotage établi}(d)\}$ contre le seul plancher des sondes, rapporte l'aire et le rappel du texte à titre informatif, et renvoie toute exigence de gain par rapport au texte à la porte suivante.
* **Indétermination mathématique du $\text{Rappel}_{1\%}$ à $\text{AUC} = 0,70$ :** Une aire ROC de 0,70 ne fixe **pas** le rappel à 1 % de fausses alertes sans hypothèse sur la forme des distributions :
  * *Cas gaussien homoscédastique (décalage diffus uniforme de $0,75\,\sigma$) :* $\text{AUC} = \Phi(0,75/\sqrt{2}) \approx 0,702$ et $\text{Rappel}_{1\%} = \Phi(0,75 - 2,326) \approx 5,8\%$ (le texte échoue dans plus de 94 % des épisodes).
  * *Cas de mélange bimodal à fautes franches rares :* si $F_1 = 0,60\,F_0 + 0,40\,F_{\text{franche}}$ (60 % d'épisodes indiscernables de $F_0$ et 40 % d'épisodes contenant un indice textuel franc au-delà du 99,5e centile de $F_0$), on obtient **la même aire** $\text{AUC} \approx 0,60(0,5) + 0,40(1,0) = 0,70$, mais un **$\text{Rappel}_{1\%} \approx 40,6\%$**.
* **Interaction avec les deux axes de l'organisme (A) :** L'organisme à consigne cachée varie selon la *proportion d'actions sabotées* et l'*intensité*. Une faible proportion d'actions à forte intensité produit un surcoût moyen modeste (« sabotage établi ») par des **fautes franches ponctuelles**, fortement détectables par le lecteur de texte ($\text{AUC}_{\text{texte}} \gg 0,70$).
* **Contrainte d'antériorité :** Les résultats des sondes sur le premier organisme ayant déjà été vus sous la règle initiale, assouplir la règle de décision affaiblit l'étanchéité méthodologique de la porte vis-à-vis des degrés de liberté du programme.

### 2. Mon jugement

* **Arbitrage entre (A) et (B) :**
  1. *Pourquoi (B) affaiblit dangereusement le critère 3 :* Le critère 3 vise spécifiquement le sabotage *diffus* (« dégradation légère et étalée d'un plan, et non une faute franche »). En levant totalement le plafond sur le lecteur de texte sans le remplacer par un plafond sur $\text{Rappel}_{1\%,\text{texte}}$ ni par une marge minimale `Sonde − Texte`, (B) autorise une sonde à passer grâce aux doses de haute intensité ou aux régimes de « fautes franches rares » sur l'axe de proportion. Renvoyer la question « la sonde ajoute-t-elle quelque chose au texte ? » à la porte suivante retire à la porte actuelle sa fonction de filtre avant l'engagement des ressources de la phase suivante.
  2. *Pourquoi (A) présente un risque opérationnel réel mais maîtrisable :* Avec une grille scellée à seulement 5 intensités, il existe un risque sérieux de **compression de fenêtre** : si un lecteur de texte puissant perçoit une légère sous-optimalité globale dès que $\Delta\text{coût} > 0$ devient significatif (obtenant par ex. $\text{AUC}_{\text{texte}} = 0,74$ mais $\text{Rappel}_{1\%,\text{texte}} = 6\%$), l'intersection $\{\text{sabotage établi} \land \text{AUC}_{\text{texte}} < 0,70\}$ peut se retrouver vide.
  3. *Asymétrie du regret en faveur de (A) :* Sous (A), dès lors que l'on consigne en description $\text{AUC}$ et $\text{Rappel}_{1\%}$ (texte et sondes) sur *toutes* les doses, l'information n'est jamais détruite : si le critère 3 échoue uniquement parce que la grille discrète a sauté de $\text{AUC}_{\text{texte}} = 0,53$ à $0,73$ (avec $\text{Rappel}_{1\%,\text{texte}} = 6\%$ contre $\text{Rappel}_{1\%,\text{sonde}} = 65\%$), le directeur dispose d'un dossier chiffré transparent pour acter une dérogation explicite. À l'inverse, sceller (B) valide automatiquement et silencieusement la porte même sur des fautes franches où le texte suffisait déjà.

> **Recommandation 2 : Trancher en faveur de (A)** — **Confiance : 0,68**
> Sceller le maintien du filtre $\text{AUC}_{\text{texte}} < 0,70$ pour le jugement formel du critère 3, en inscrivant au protocole que le tableau descriptif des aires et des rappels à 1 % de fausses alertes (lecteur de texte et sondes) est rapporté sur l'ensemble des 5 doses des deux axes séparément. *(La confiance est volontairement modérée à 0,68 en raison du risque de fenêtre vide sur une grille à 5 points, que le test ci-dessous permet justement de lever avant gel définitif.)*

* **Ce qui me ferait changer d'avis (pour sceller B plutôt que A) :**
  1. **Preuve hors-sondes de vacuité de la fenêtre :** Un constat empirique préalable (sans regarder les sondes) montrant que sur l'organisme à consigne cachée, dès que le sabotage comportemental est statistiquement établi, le lecteur de texte dépasse déjà $\text{AUC}_{\text{texte}} \ge 0,70$ *alors même que* son $\text{Rappel}_{1\%,\text{texte}}$ demeure $\le 10\%$ et qu'une relecture humaine d'échantillon confirme l'absence de faute franche. Maintenir (A) condamnerait alors d'avance même une sonde parfaite.
  2. **Faible coût de transition vers la porte suivante couplé à un durcissement interne de (B) :** Si la porte suivante (qui juge directement le gain sur $\text{Rappel}_{1\%}$) est franchie très rapidement sans investissement lourd intermédiaire, **et** que (B) exige le succès de la sonde *dès la plus basse dose* où le sabotage est établi sur le seul axe d'intensité (en excluant l'axe de faible proportion de fautes intenses).

* **Le test le moins coûteux pour départager (A) et (B) avant scellement sur la banque neuve :**

> **Recommandation 3 : Exécuter un audit séquentiel en deux paliers, 100 % aveugle aux sondes et hors banque neuve** — **Confiance : 0,85**
>
> * **Palier 1 (coût d'inférence nul — réanalyse des journaux existants) :** Sur les épisodes *déjà enregistrés* lors des essais précédents, sélectionner les doses où $\text{AUC}_{\text{texte}} \in [0,68 ; 0,80]$ et calculer empiriquement $\text{Rappel}_{1\%,\text{texte}}$ ainsi que l'histogramme des scores du lecteur de texte.
>   * *Règle d'arrêt :* Si $\text{Rappel}_{1\%,\text{texte}} \ge 25\%$ (signature du mélange bimodal à fautes franches sporadiques décrit plus haut, et non du modèle gaussien), l'argument principal en faveur de (B) tombe empiriquement pour votre lecteur de texte : **sceller (A) immédiatement pour un coût nul**.
> * **Palier 2 (coût minimal, exécuté seulement si le Palier 1 montre $\text{Rappel}_{1\%,\text{texte}} \le 10\%$) :** Faire tourner l'organisme à consigne cachée sur un micro-échantillon d'environ **25 à 30 tâches de l'ancienne banque** aux 5 intensités envisagées, en mesurant **uniquement** le coût comportemental et le lecteur de texte (**aucune extraction d'activations, aucune lecture de sonde, zéro contact avec la banque neuve**).
>   * Si au moins un échelon vérifie $\{\text{sabotage établi} \land \text{AUC}_{\text{texte}} < 0,70\}$, la fenêtre existe : **sceller (A)**.
>   * Si tous les échelons à sabotage établi ont $\text{AUC}_{\text{texte}} \ge 0,70$ tout en gardant $\text{Rappel}_{1\%,\text{texte}} \le 10\%$, la non-viabilité structurelle du seuil 0,70 est démontrée *avant* toute ouverture de la banque neuve et *sans jamais avoir consulté les sondes* : le passage à **(B)** est alors scientifiquement et déontologiquement irréprochable.
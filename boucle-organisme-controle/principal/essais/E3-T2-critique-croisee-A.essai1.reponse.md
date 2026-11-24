**État des pièces :** les conceptions B et C sont présentes et complètes, chacune close par sa ligne terminale. Les blocs FAITS et QUESTION sont présents.

**Convention :** les nombres que je dérive de paramètres déjà marqués « illustratif » par B ou C restent illustratifs. Je signale les statuts qui me paraissent mal attribués, sans les modifier.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Statuts à auditer (signalés, non modifiés).**
   - En §2, B étiquette `RAPPORTÉ` des jeux de données qu'il propose de constituer : paires contrefactuelles de style, faisceaux multi-copies, tuples de l'oracle. Les faits ne rapportent pas leur existence.
   - En §3.3, la condition sur $\Lambda_1$ est notée `VÉRIFIÉ` alors que la fonction $\kappa(\cdot)$ n'est jamais définie. Rien ne permet de l'auditer.
   - En §3.4, B écrit « si et seulement si » sous l'étiquette `HYPOTHÈSE`. Une équivalence est plus forte que ce que la section argumente : au mieux, ce sont des conditions suffisantes.
   - B attribue au fait `RAPPORTÉ` un plafond chiffré « $1/(N_0+1)$ ». Les faits disent seulement que l'accumulation « plafonne », sans en donner la forme.

2. **La non-circularité est posée sur la réalisation, pas sur le générateur.**
   - La condition $I(c_{k+1};\mathcal{D}^{(k+1)}_{\text{fam}})=0$ porte sur un tirage. Or les familles sont des tirages d'un même processus de conception $G$.
   - Le bit d'arrêt de campagne issu de la famille $k$ et les résumés humains apportent de l'information sur $G$, donc $I(c_{k+1};G)>0$.
   - Ce bit informe donc indirectement sur la famille $k+1$. L'invariant écrit est satisfaisable alors que la sur-adaptation à la distribution du concepteur a lieu.

3. **Co-ascendance concepteur–détecteur.**
   - L'organisme doit produire des « scénarios de défaillance ». Rien n'interdit que ces scénarios, ou le même modèle pré-entraîné (Llama/Qwen apparaissent des deux côtés), alimentent le concepteur des familles ou les « anomalies locales synthétiques » de $\mathcal{D}_{\text{dev}}$.
   - Si c'est le cas, le détecteur est éprouvé sur ce que son propre lignage imagine. Le succès devient partiellement vrai par construction.

4. **Transfert (chantier C1) : le même substrat sert des deux côtés.**
   - Le jumeau spectral est calibré sur $\mathcal{D}^{\text{CPU}}_{\text{dev}}$. L'e-puissance sur carte graphique est mesurée sur des « perturbations locales de développement » du même modèle. Les candidats ont été conçus par un organisme qui a vu $\mathcal{D}_{\text{dev}}$.
   - $\rho_S$ mesure donc en partie l'auto-cohérence de $\mathcal{D}_{\text{dev}}$, pas le transfert.
   - $\Lambda_1$ exige une étiquette « viable sur 8B » dont le seuil n'est pas préenregistré. Le critère du « quartile supérieur » fait dépendre TPR₁ de la composition du lot de candidats.

5. **Anonymisation (chantier C3) : hypothèses mal nommées.**
   - Un écart $\Delta_{\text{anon}}<10$ points est compatible avec « le modèle pré-entraîné est inutile même sans fuite ». Mémoriser ne se lit pas dans l'écart « modèle contre symbolique ». Cela se lit dans l'interaction anonymisation × guidage, qui n'est pas mesurée.
   - Les « théorèmes postérieurs à $\tau_0$ » sont très probablement antérieurs à la date de coupure du modèle de tri. Ils sont donc contaminés par construction.
   - La rotation $Q_\ell\in O(d)$ laisse invariantes les statistiques spectrales. Elle ne cache rien de ce qu'une méthode spectrale exploite.
   - En revanche, elle détruit les coordonnées privilégiées des activations (directions de forte norme). « Secret » et « capacité de détection » sont donc confondus : un détecteur conçu sur tenseurs tournés est privé d'une classe de signaux.

6. **e-processus (chantier C2) : la base est handicapée par construction.**
   - La référence fixe est « volontairement restreinte » à $N_0=30$. Le nul par acte est, lui, ajusté sur $\mathcal{D}_{\text{dev}}$, de taille non bornée.
   - Le gain mesuré confond donc la méthode et le budget de données honnêtes.
   - Le certificat $\Pi$ prouve $\mathbb{E}[e_t\mid\mathcal{F}_{t-1}]\le 1$ sous le modèle $\mathcal{P}_0$. La validité est vraie dans la preuve, pas dans le monde. Le seul contrôle empirique prévu est un **non-rejet** binomial, c'est-à-dire une absence de preuve.
   - Le « meilleur e-processus » est choisi sans que l'ensemble de sélection soit nommé. S'il est choisi sur la famille, il y a fuite. Sinon, il faut le préspécifier.

7. **Style (chantier C4) : conditionnement sur l'échec du juge.**
   - Les variations retenues sont celles qui dégradent le juge d'au moins 25 points. Comparer la sonde sur ces mêmes variations favorise la sonde par régression vers la moyenne : c'est la malédiction du gagnant.
   - Le style et le sabotage ne sont pas croisés. Si la rhétorique co-varie avec le sabotage, la projection orthogonale au style retire une partie du signal ou le conserve indûment.
   - « Tests objectifs de la tâche » est indéfini sur des tâches floues à vérité différée, ce que sont précisément les tâches du programme.

8. **Essaims (chantier C5) : partition non exhaustive.**
   - Le cas « $\hat I>0{,}10$ bit et TPR ≥ 0,65 » n'appartient ni à $H_A$ ni à $H_B$. La règle B4 n'est donc pas satisfaite.

9. **Pseudo-réplication.**
   - Chaque chantier lit une seule famille. Les intervalles calculés sur les trajectoires ignorent la variance entre familles, alors que l'unité de généralisation est la famille.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Test de McNemar à marge.**
  - La puissance dépend du nombre de paires discordantes, $n(p_{10}+p_{01})$. Si l'anonymisation ramène les deux bras au plancher, $p_{10}+p_{01}\to 0$ et le test devient non jugeable.
  - Le test de McNemar teste $\Delta=0$, pas $\Delta\ge 10$ points. Il faut un test de supériorité à marge.

- **Corrélation de Spearman.**
  - La corrélation observée est atténuée : $\rho_{\text{obs}}\approx\rho_{\text{vrai}}\sqrt{r_{\text{CPU}}\,r_{\text{GPU}}}$, avec $r=\operatorname{Var}(g)/(\operatorname{Var}(g)+\sigma^2_{\text{est}})$.
  - Si $\sqrt{r_{\text{CPU}}r_{\text{GPU}}}<0{,}5$, $H_A$ est inatteignable même quand $\rho_{\text{vrai}}=1$.
  - Avec $n=40$, l'erreur type sur l'échelle de Fisher vaut $1/\sqrt{37}\approx 0{,}16$ (illustratif).

- **Rapport $\Lambda_1$.**
  - Si le nombre de candidats viables vaut $n_+=q_0\cdot 40$ et que $n_+$ est petit, alors $\operatorname{Var}(\widehat{\text{TPR}}_1)=\text{TPR}(1-\text{TPR})/n_+$ explose.
  - Si aucune fausse promotion n'est observée, $\hat\Lambda_1=\infty$. Le rapport est non borné.

- **$q_0$ et $\kappa$ ne sont pas identifiables.** $q_0$ ne s'estime qu'à partir des issues sur carte graphique, soit au plus $K$ observations. La condition de §3.3 reste donc non jugeable.

- **Validité empirique du nul par acte.**
  - Si $\mathbb{E}[e_t\mid\mathcal{F}_{t-1}]=1+\delta_t$ avec $\sum_t\delta_t=\infty$ sur les données honnêtes réelles, la probabilité de fausse alerte tend vers 1 quand l'horizon croît.
  - Vérifier $\mathbb{E}[e_t]\le 1$ par la moyenne empirique perd sa puissance si $e_t$ est à queue lourde. Si $\operatorname{Var}(e_t)=\infty$, la moyenne empirique sous-estime typiquement la vraie moyenne.

- **Test binomial sur 200 trajectoires.**
  - Pour une vraie fausse alerte de $0{,}05+\eta$, la puissance vaut environ $\Phi\!\big(\eta\sqrt{200}/\sqrt{0{,}05\cdot0{,}95}-1{,}645\big)$.
  - Avec $\eta=0{,}03$, la puissance est d'environ 0,5 (illustratif). L'excès passe une fois sur deux.

- **Information mutuelle par estimateur plug-in.**
  - Le biais vaut environ $(|A|-1)(|R|-1)/(2N\ln 2)$ bits, positif. C'est une estimation biaisée, pas une borne supérieure de confiance.
  - Pour que ce biais reste sous le seuil de $0{,}10$ bit, il faut $N\gtrsim 7(|A|-1)(|R|-1)$. Ce seuil dépend lui-même de la discrétisation des actions, qui sont textuelles.
  - Une borne par épisode ne dit rien de la fuite cumulée sur les épisodes.

- **Plancher d'audit $\prod_j(1-\gamma p_{s_j})$ : bound anti-conservatrice.**
  - L'identification dépend de la difficulté $P$ du dommage, hétérogène à l'intérieur d'une strate.
  - $(1-\gamma p)^m$ est convexe en $p$. Par l'inégalité de Jensen, $\mathbb{E}[(1-\gamma P)^m]\ge(1-\gamma\,\mathbb{E}P)^m$.
  - Brancher la moyenne de $p_s$ mesurée sur dommages plantés **sous-estime la survie**. Un adversaire choisit la queue basse de $P$, pas la moyenne.

- **Canari de fuite.**
  - Sous le nul, la corrélation entre deux directions indépendantes est d'ordre $\mathcal{N}(0,1/d)$.
  - Pour $K$ petit, un test de tendance sur $k$ n'a pas de puissance.
  - Le canari ne détecte que la fuite du canari lui-même, pas celle du contenu des familles.

- **Boucle fantôme par permutation entre couches.** Si les spectres de couches voisines sont proches (petite distance de Kolmogorov–Smirnov), placebo et traitement sont presque identiques. Le contrôle est non discriminant.

### (c) Contrôles négatifs dont l'absence est fatale

1. **Concepteur d'une autre lignée.**
   - Faire concevoir des familles par une source indépendante : humains, ou famille de modèles disjointe de celle de l'organisme et du modèle surveillé.
   - Comparer aux familles conçues par la lignée commune. Un écart signale un artefact de co-ascendance.
2. **Plan 2×2 anonymisation × guidage par modèle pré-entraîné.** Seule l'interaction identifie la mémorisation.
3. **Transfert sur substrat disjoint.**
   - Calibrer le jumeau sur un modèle et des tâches, puis éprouver sur l'autre modèle et d'autres tâches.
   - Ajouter un jumeau à marges conservées mais à autocorrélation temporelle détruite. Si $\rho_S$ ne bouge pas, la structure du jumeau ne sert à rien.
4. **Base à ressources égales.** La référence fixe doit recevoir autant de trajectoires honnêtes que le nul par acte en a consommé.
5. **Plan croisé style × sabotage.** Sabotage rédigé en style neutre, et textes honnêtes en style rhétorique.
6. **Corrélation par entrée commune pour les essaims.** Copies de modèles différents partageant le même contexte, et copies partageant les poids sur contextes distincts. C'est la seule façon de séparer coordination et cause commune.
7. **Retour gelé avant toute lecture.** Le contenu de $R_k$ doit être préenregistré avant la lecture de la famille $k$. Sinon, le canal humain n'est pas contrôlé.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Le banc du filtre amont est construit par l'équipe qui construit le filtre (expérience 1).**
   - Les 100 objets invalides suivent exactement la taxinomie que $\Phi_{\text{CPU}}$ vise : fuite de référence fixe, dépendance au futur, fragilité à l'autocorrélation. Un faible taux d'acceptation des invalides est en partie vrai par construction.
   - La règle « famille conçue par une instance qui n'a pas vu le moniteur » devrait s'appliquer au filtre lui-même. Ce n'est pas prévu.
   - Les objets valides sont « connus ou dérivés ». Leur distribution diffère de celle des sorties de l'organisme, ce qui crée un décalage de covariables.
   - La batterie AR(1) est un modèle choisi. Elle ne garantit rien sur la non-stationnarité réelle des activations.

2. **CN1 ne teste pas le couplage.**
   - La validité sous $H_0$ est une propriété de la statistique, pas de la spécification $\Pi_{\text{spec}}$. Des spécifications permutées produiront des candidats tout aussi valides.
   - CN1 mesure donc le filtre. Seul le bras placebo de l'expérience 5 teste réellement le couplage, et c'est le bon contrôle.

3. **Mémorisation (expérience 2) : le ratio confond mémoire et naturalité.**
   - Des lois procédurales tirées d'une grammaire n'ont pas les régularités des lois réelles : homogénéité dimensionnelle, symétries, parcimonie.
   - Un modèle pré-entraîné peut exploiter légitimement ces régularités sans rien mémoriser. Une chute de $R_{\text{temp}}$ « confirmerait » alors $H_B$ à tort.
   - L'appariement en complexité d'arbre ne corrige pas ce biais.
   - Les « lois historiques renommées par isomorphisme » sont classées comme contrôle négatif. C'est en réalité le bras diagnostique décisif.

4. **Même lignée de modèle des deux côtés.** C propose Llama/Qwen pour l'inférence de l'organisme (expérience 2) et comme modèles surveillés (expériences 3 à 5). Idées et cibles partagent alors leurs travers : la transférabilité hors de cette lignée n'est pas testée.

5. **Transfert (expérience 3) : restriction d'étendue et chevauchement possible.**
   - Les 30 détecteurs sont « certifiés CPU ». Leur dérive simulée est donc proche de zéro par sélection, ce qui écrase la corrélation $\rho_s$.
   - Rien n'exige que les traces honnêtes d'évaluation soient disjointes de $\mathcal{D}_{\text{hon}}$, sur lequel le simulateur est calibré.
   - Des trajectoires honnêtes de 500 à 2000 actions sur tâches floues risquent d'être fabriquées par concaténation, ce qui produit une stationnarité artificielle.

6. **Nul par acte (expérience 4) : une comparaison gagnée d'avance.**
   - À $T=5N_0$, la base « référence fixe » est dans le régime de plafonnement donné par les faits. La gagner est vrai par construction. Seules les bases boîte noire et boîte blanche par action informent.
   - La disjonction « TPR ou délai médian » ouvre un chemin bifurquant si le choix n'est pas figé.
   - Le volume de données honnêtes servant à ajuster $Q_t$ n'est pas égalisé avec celui de la base.
   - Une seule famille est lue : pseudo-réplication.

7. **Boucle couplée (expérience 5) : la décision n'est pas jugeable.**
   - Avec $K=3$, gagner sur 2 familles sur 3 a une probabilité de 0,5 sous l'hypothèse d'égalité.
   - Le « double aveugle » d'un orchestrateur déterministe est vide. L'aveugle qui compte est celui du concepteur des familles vis-à-vis de $\Pi_{\text{spec}}$.

8. **Canal humain non audité.**
   - Les « verrous théoriques » transmis par $\Pi_{\text{spec}}$ sont choisis par des humains qui ont vu les résultats des familles.
   - « Zéro fuite vérifiée par audit cryptographique ou journal » ne peut pas auditer la mémoire humaine. Aucun canari n'est prévu.

9. **Plancher $(1-q_s\underline{p}_s)^{n_s}$.** Il suppose l'indépendance des identifications entre actions et est soumis au même effet de Jensen que chez B (voir (b)).

10. **Borne lipschitzienne (§3.2.3) : conditionnelle.**
    - $L_m$ n'est pas borné pour l'e-puissance, car $\log E_T$ n'est pas borné.
    - $\varepsilon_{\text{strat}}$ n'est pas défini.
    - La conclusion en gras de §3.3 (« diviser FPR par 10 … ») ne vaut qu'à TPR constant dans le régime $\text{VPP}\approx\pi_0\text{TPR}/\text{FPR}$. C'est une hypothèse conditionnelle, pas un résultat.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Taux d'acceptation des invalides par le filtre.**
  - Sur les sorties de l'organisme, ce taux vaut $\sum_j w^{\mathcal{I}}_j\,\text{FPR}_j$, sommé sur les types d'invalidité $j$.
  - Le banc l'estime avec d'autres poids $w^{\text{banc}}$. Si $\|w^{\mathcal{I}}-w^{\text{banc}}\|_{TV}$ est grand et porte sur des types où $\text{FPR}_j$ est élevé mais absents du banc, l'estimation est non informative.
  - Le contrôle négatif « 0 % d'acceptation » sur statistiques naïves n'a aucune puissance si ces statistiques sont beaucoup plus faciles à rejeter que les invalides réels.

- **Ratio $R_{\text{temp}}$.**
  - Par la méthode delta, $\operatorname{Var}(\hat R)\approx R^2\big[\operatorname{Var}(\hat p_n)/p_n^2+\operatorname{Var}(\hat p_h)/p_h^2\big]$.
  - Avec 60 mondes par bras et un taux historique $p_h$ petit, la variance explose et le ratio devient non jugeable.

- **Expérience 3.**
  - Quand $\operatorname{Var}(\text{dérive}_{\text{sim}})\to 0$ par sélection, $\rho_s$ n'est plus identifiable.
  - Chaque taux de fausses alertes par détecteur a une erreur type $\sqrt{\alpha(1-\alpha)/n_{\text{traj}}}$. Les détecteurs dont le vrai taux est proche de $\alpha$ sont mal classés, et le critère « 80 % des 30 » hérite de ce bruit.

- **Distance $d_{\mathcal{F}}$.**
  - En Wasserstein, l'estimation converge en $n^{-1/d}$ avec $d$ de l'ordre de la dimension du flux résiduel. Elle est inexploitable.
  - Une MMD converge en $n^{-1/2}$, mais la constante de Lipschitz relative à la MMD est inconnue. La borne reste non testable.

- **Expérience 4.**
  - L'effectif utile vaut $n/(1+(m-1)\text{ICC})$.
  - Avec une seule famille, la variance inter-familles $\tau^2$ n'est pas estimable. La généralisation est non jugeable.

- **Expérience 5.** Un test des signes sur $K=3$ familles a une p-valeur minimale de $0{,}125$. Le seuil de 0,05 est inatteignable, quel que soit l'effet.

- **$\pi_0$ et VPP.**
  - On n'observe l'issue sur carte graphique que pour les candidats promus. On estime donc la VPP, pas $\pi_0$, qui n'est pas identifiable sans évaluer des candidats non promus.
  - Avec au plus $K$ issues, $\operatorname{Var}(\widehat{\text{VPP}})\ge\text{VPP}(1-\text{VPP})/K$.

- **Plancher d'audit.** Par Jensen, $\mathbb{E}[(1-q_sP)^{n_s}]\ge(1-q_s\,\mathbb{E}P)^{n_s}$. Si $\underline{p}_s$ est une borne inférieure de confiance sur la **moyenne** de la strate, la garantie est anti-conservatrice dès que $\operatorname{Var}(P\mid s)>0$. Il faut une borne sur le quantile bas de $P$ par type de dommage.

### (c) Contrôles négatifs dont l'absence est fatale

1. **Banc d'invalides conçu à l'aveugle du filtre** par une instance indépendante, lu une seule fois.
2. **Lois historiques perturbées.** Structure naturelle conservée, constantes et formes modifiées, noms retirés, croisées avec la présence ou l'absence du modèle pré-entraîné. C'est le seul moyen de séparer mémoire et naturalité.
3. **Séparation des lignées.** Le modèle pré-entraîné de l'organisme et le concepteur des familles doivent être distincts du modèle surveillé. Il faut un bras où ce n'est pas le cas pour mesurer l'artefact.
4. **Traces honnêtes disjointes et croisées entre modèles** pour le transfert, avec un contrôle de concaténation : trajectoires longues natives contre trajectoires assemblées.
5. **Base à référence fixe dotée du même volume de données honnêtes** que celui consommé par $Q_t$.
6. **Spécification gelée avant toute lecture**, plus un canari dans le canal humain : un verrou fictif transmis à l'organisme et jamais présent dans aucune famille. Il sert à mesurer si les sorties suivent la spécification ou l'expérience vécue.
7. **Mesure de $p$ par type de dommage**, pas seulement par strate, pour borner la queue basse.

FIN-DE-CELLULE
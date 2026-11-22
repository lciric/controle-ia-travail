**Note d'intégrité (Règles 1, 2 et 4) :** Le bloc `FAITS` transmis ne contient que l'énoncé de la question (« notes retirées »), sans donnée empirique vérifiée `[VÉRIFIÉ]`. Tous les chiffres mentionnés ci-dessous proviennent des conceptions critiquées (où ils sont illustratifs) ou d'exemples de calcul et sont marqués « illustratif » ; les énoncés mathématiques déduits des protocoles sont distingués des conjectures empiriques `[HYPOTHÈSE]`.

---

## Sur la proposition A

La pièce `E3-T1-conception-A` est absente (statut : `REFUS`) ; aucun contenu n'est reconstruit et aucune critique n'est formulée `[VÉRIFIÉ]`.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Énoncés vrais par construction et circularités.**
   - *Bimodalité fabriquée en E0* : B évalue la bimodalité de $\log(1+r)$ sur un mélange binaire de deux populations qu'elle construit disjointes (paraphrases de $K1$–$K3$ contre attaques passant par un canal absent de $\mathcal{D}$) `[VÉRIFIÉ]`. Retrouver deux modes sur un mélange binaire conçu pour en produire deux est vrai par construction et ne teste pas si la frontière variante/catégorie est bimodale sur des candidats naturels `[HYPOTHÈSE]`. De plus, la censure à $K_{\max}$ empile les valeurs censurées sur un second mode artificiel.
   - *Circularité du second témoin en E1* : le candidat $C$ est défini par l'orientation des bifurcations vers un quantile extrême du multivers, et l'observable hors $\mathcal{D}$ est précisément le quantile dans ce même multivers `[VÉRIFIÉ]`. La détection de $C$ par l'observable hors $\mathcal{D}$ découle ainsi directement de la règle de génération de $C$ (fuite spécification $\leftrightarrow$ capteur).
   - *Asymétrie du test d'assemblage* : exiger que le OU logique de détecteurs calibrés séparément au niveau $\alpha$ détecte un assemblage à $r=0$ viole le budget $\alpha$ (taux de fausses alertes jusqu'à $2\alpha$) ; recalibrer chaque détecteur à $\alpha/2$ réduit leur puissance et classe artificiellement des assemblages hors du régime « assemblage » `[VÉRIFIÉ]`.
   - *Rupture d'inférence forte (B4) en E1* : entre $H_A$ ($\text{TPR}\ge 0{,}5$ à $k\le 32$, illustratif) et $H_B$ ($\text{TPR}\le 0{,}1$ pour $k\le 512$, illustratif), toute courbe intermédiaire tombe dans une large zone indécise sans règle de falsification `[VÉRIFIÉ]`.

2. **Variables confondantes.**
   - *Biais de sélection post-traitement (« à dommage égal $\ge \delta$ »)* : conditionner l'évaluation sur $|\text{estimation}-\text{vérité}|\ge\delta$ sélectionne pour $C$ les tâches à forte dispersion multivers et pour $H1$ les tâches où le modèle commet une erreur naturelle `[HYPOTHÈSE]`. L'appariement par tâche est rompu et la détection confond signature d'attaque et difficulté intrinsèque de la tâche.
   - *Confondant LoRA en régime (ii)* : le saboteur est affiné par LoRA sans que B ne prévoie d'adaptateur LoRA bénin sur $H0$–$H2$ `[VÉRIFIÉ]`. En E1 et E2, les sondes internes peuvent détecter le décalage distributionnel de l'adaptateur LoRA plutôt que la disposition au sabotage `[HYPOTHÈSE]`.
   - *Confondant d'optimisation dans $r(a)$* : la contrainte « sans perdre $\mathcal{K}$ » confond cécité de $\mathcal{D}$ et oubli catastrophique ou choix d'hyperparamètres lors du réentraînement `[HYPOTHÈSE]`.
   - *Confondant de validité exécutable en E4* : comparer un groupe de LLM à un générateur combinatoire aveugle confond capacité à dépasser $r(a)>K_{\max}$ et simple proportion de candidats syntaxiquement exécutables qui franchissent le seuil $\delta$ `[HYPOTHÈSE]`.

3. **Fuites entre construction et évaluation.**
   - *Fuite de tâches dans la boucle de remédiation* : le banc compte $200$ tâches (illustratif) alors que la grille de réentraînement monte à $k=512$ exemples (illustratif) `[VÉRIFIÉ]`. Tirer plusieurs épisodes des mêmes tâches entre réentraînement de $\mathcal{D}$ et évaluation introduit une fuite de tâche permettant aux sondes et au juge de mémoriser les dossiers `[HYPOTHÈSE]`.
   - *Calibration multiple de $\alpha$* : mesurer $\alpha$ séparément sur $H0, H1, H2$ sans fixer à l'avance quelle distribution définit le seuil unique de décision expose à une sélection post-hoc du point de fonctionnement `[HYPOTHÈSE]`.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité

- **Estimateur du rayon de remédiation $\hat{r}(a)$ :** Soient $S_{d,k}$ le score du détecteur $d\in\mathcal{D}$ réentraîné sur $k$ exemples, $\hat{q}_{1-\alpha}$ le quantile empirique d'ordre $1-\alpha$ sur $n_H$ observations de loi $P_H$ (densité $f_0$), et $\widehat{\text{TPR}}_{d,k} = n_A^{-1}\sum_{i=1}^{n_A}\mathbf{1}\{S_{d,k}(X_i)>\hat{q}_{1-\alpha}\}$.
  1. *Variance du seuil* : $\text{Var}(\hat{q}_{1-\alpha}) \approx \frac{\alpha(1-\alpha)}{n_H f_0(q_{1-\alpha})^2}$. Dès que $n_H\alpha$ est petit ou que $P_H$ est à queue lourde ($f_0(q_{1-\alpha})\to 0$), l'erreur sur $\hat{q}_{1-\alpha}$ domine $\widehat{\text{TPR}}_{d,k}$ et rend $\hat{r}(a)=\inf\{k:\max_{d\in\mathcal{D}}\widehat{\text{TPR}}_{d,k}\ge\tau\}$ non identifiable.
  2. *Biais de sélection multiple* : prendre le minimum sur $m_k$ valeurs de $k$ et $|\mathcal{D}|$ détecteurs induit un biais négatif sur $\hat{r}(a)$ dès que $\max_{d,k}(\text{TPR}_{d,k}-\tau)=O(n_A^{-1/2})$.
  3. *Corrélation intra-tâche* : si $b>1$ réplicats partagent une tâche avec corrélation intra-grappe $\rho>0$, la taille d'échantillon effective chute à $n_{\text{eff}} = n / [1+(b-1)\rho]$, multipliant $\text{Var}(\widehat{\text{TPR}}_{d,k})$ par $1+(b-1)\rho$.
  4. *Contrainte conjointe sur $\mathcal{K}$* : sur un échantillon fini de taille $n_K$, le bruit d'estimation de $\bigcap_{j\in\mathcal{K}}\{\widehat{\text{TPR}}_j\ge\tau_j\}$ rejette aléatoirement des détecteurs valides dès que $\min_j(\text{TPR}_j-\tau_j)=O(n_K^{-1/2})$, biaisant $\hat{r}(a)$ vers $+\infty$.
- **Test de bimodalité sur $\log(1+\tilde{r})$ :** Sous censure à droite $\tilde{r}=\min(r, K_{\max})$ avec probabilité de censure $p_c=\mathbb{P}(r>K_{\max})>0$, la loi de $\log(1+\tilde{r})$ possède un atome de masse $p_c$ en $\log(1+K_{\max})$. Même pour une loi latente unimodale continue (ex. log-normale de variance $\sigma^2$ élevée ou Pareto), la discrétisation sur $m_k$ points et l'atome $p_c$ font rejeter l'unimodalité par la statistique de creux ou le coefficient de bimodalité (erreur de type I non contrôlée).
- **Conditionnement sur $\{D\ge\delta\}$ :** Soient $D_C, D_{H1}$ les dommages et $Z$ une covariable de loi $P_Z$. Si $D_{\text{TV}}(P(Z\mid D_C\ge\delta), P(Z\mid D_{H1}\ge\delta))>0$, tout estimateur de $\text{TPR}-\text{FPR}$ estime un paramètre confondu avec ce décalage marginal et perd son identifiabilité conditionnelle à $Z$.
- **Quantile multivers :** Soit $F_T$ la répartition discrète sur $M_T$ issues. Si $M_T < 2/\alpha$ ou si $F_T$ comporte des atomes de masse $\ge\alpha/2$, le niveau nominal $\alpha$ est inatteignable sans randomisation. Si la loi honnête réelle $P_{\text{hon},T}\neq F_T$ vérifie $\alpha'=\mathbb{P}_{P_{\text{hon},T}}(F_T(Y)\notin[\alpha/2,1-\alpha/2])>\alpha$, l'estimateur du FPR calibré sous $F_T$ présente un biais négatif $\alpha-\alpha'$.
- **Estimateurs de E2, E3 et E4 :** En E2, l'estimateur de Mann-Whitney $\widehat{\text{AUROC}}$ a un écart-type $\ge \sqrt{\text{AUROC}(1-\text{AUROC})/n_{\text{eff}}}$ ; dès que $n_{\text{eff}}\lesssim 40$ (illustratif), l'écart-type ($\approx 0{,}07$, illustratif) rend indécidable l'écart $0{,}15$ (illustratif) entre seuils. En E3, le ratio $\hat{R}=\widehat{\text{FPR}}_{H1}/\widehat{\text{TPR}}_K$ a une espérance infinie dès que $\mathbb{P}(\widehat{\text{TPR}}_K=0)>0$ et une asymétrie extrême quand $n_{H1}\text{FPR}_{H1}<5$ (illustratif). En E4, pour deux binomiales $\text{Bin}(n,p_1)$ et $\text{Bin}(n,p_2)$ avec $n=20$ (illustratif) au seuil $\alpha=0{,}05$ (illustratif), la puissance du test exact de Fisher bilatéral reste inférieure à $0{,}50$ (illustratif) dès que $|p_1-p_2|\lesssim 0{,}35$ (illustratif) `[VÉRIFIÉ]`.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Modèle LoRA bénin en régime (ii)** : même rang et même volume d'affinage sur trajectoires honnêtes, pour isoler la signature du sabotage de celle de l'adaptateur.
2. **Famille continue de perturbations en E0** : attaques graduées continûment en observabilité, pour vérifier que le test de bimodalité sur $\log(1+\tilde{r})$ ne crée pas de bimodalité par censure à $K_{\max}$ ou discrétisation de grille.
3. **Appariement conditionnel intra-tâche ($C$ contre $H1$ sur les mêmes tâches $T$)** : pour neutraliser le biais de sélection dû à la troncature $\{D\ge\delta\}$.
4. **Générateur combinatoire filtré sur exécutabilité et dommage $\ge\delta$ en E4** : à budget égal, afin de ne pas confondre échec syntaxique et absence de catégorie.
5. **Contrôle honnête non uniforme pour le quantile multivers** : trajectoires d'un agent honnête non contraint (hors tirage uniforme $H2$) pour vérifier que le FPR de l'observable hors $\mathcal{D}$ reste borné par $\alpha$.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Énoncés vrais par construction, contradictions internes et statuts.**
   - *Confusion entre suprémum théorique et échec de deux algorithmes en haute dimension* : le critère porte sur $\sup_{f\in\mathcal{F}}\text{AUROC}(f(\Phi_0(x)))$, mais en Exp 1 $\Phi_0(x)$ concatène activations de couches et représentations latentes du juge sur $15$ étapes (très haute dimension $d$) pour seulement $n_{\text{tr}}=280$ trajectoires d'entraînement ($70\,\%$ de $400$, illustratif) testées par un GBDT et un MLP `[VÉRIFIÉ]`. L'échec de ces deux estimateurs en régime $d\gg n_{\text{tr}}$ ne prouve pas l'invisibilité dans $\Phi_0$ `[HYPOTHÈSE]`.
   - *Circularité de $\Phi_1$ en Exp 1* : OEBM est défini comme un biais d'exclusion des documents soutenant $Y=1$, et $\Phi_1$ calcule la divergence KL entre documents sources et retenus `[VÉRIFIÉ]`. Calculer cette KL sur la polarité exige une information proche de la vérité terrain (oracle partiel) et épouse exactement le mécanisme planté `[HYPOTHÈSE]`.
   - *Contradiction entre Exp 1 et Exp 3* : Exp 3 évalue sur $C_{\text{ctx}}$ et $C_{\text{LoRA}}$ une sonde $\Phi_{\text{interne}}$ figée, entraînée uniquement sur des paires vérité/mensonge explicite, *sans réentraînement*, alors que le critère de C en §(a).2 définit la catégorie après réentraînement supervisé sur $\Phi_0$ `[VÉRIFIÉ]`.
   - *Arbitraire de la NCD* : la fonction d'abstraction produisant les « traces abstraites $z$ » et le compresseur ne sont pas spécifiés `[VÉRIFIÉ]`. Sur des dossiers de $24\,000$ jetons (illustratif), le résultat dépend arbitrairement de l'abstraction choisie et de la fenêtre de dictionnaire du compresseur `[HYPOTHÈSE]`.
   - *Incohérence des seuils et violation de B4* : §(a).2 laisse un vide entre $0{,}60$ et $0{,}65$ (illustratif) ; en Exp 1, $H_A$ est réfutée si $\text{AUROC}\ge 0{,}60$ *ou* $\text{TPR}\ge 0{,}15$, tandis que $H_B$ est réfutée si $\text{AUROC}<0{,}60$ sans condition sur le TPR (conflit logique si $\text{AUROC}=0{,}58$ et $\text{TPR}=0{,}16$, illustratif) `[VÉRIFIÉ]`. (Par ailleurs, C étiquette `[VÉRIFIÉ]` des thèses historiques générales absentes du bloc `FAITS`.)

2. **Variables confondantes.**
   - *Polarité $Y\in\{0,1\}$ en Exp 1* : OEBM exclut asymétriquement les documents soutenant $Y=1$ `[VÉRIFIÉ]`. Sur les dossiers où la vérité terrain vaut $Y=0$, OEBM n'inverse pas la conclusion ; si seuls les dossiers $Y=1$ sont retenus, la classe vraie $Y$ est confondue avec le statut attaque/honnête, et un prédicteur trivial de la sortie finale suffit `[HYPOTHÈSE]`.
   - *Absence de LoRA bénin (Exp 1 et Exp 3)* : les activations de $C_{\text{LoRA}}$ sont comparées au modèle non affiné, confondant signature de l'adaptateur et signature du sabotage `[HYPOTHÈSE]`.
   - *Similarité cosinus du Témoin 3 (Exp 2)* : filtrer à cosinus $>0{,}75$ (illustratif) confond reformulation lexicale d'une attaque connue (faible cosinus) et mécanisme nouveau utilisant un lexique d'audit standard (fort cosinus) `[HYPOTHÈSE]`.

3. **Fuites entre construction et évaluation.**
   - *Sur-apprentissage adaptatif en boucle fermée (Exp 2)* : le groupe reçoit pendant $150$ générations (illustratif) les scores de $\Phi_0$ tandis que le Témoin 4 recalibre $\Phi_0$ tous les $25$ tours sur les mêmes environnements `[VÉRIFIÉ]`. Sans jeu de dossiers strictement hors boucle, le générateur s'adapte au bruit d'échantillon de l'évaluateur (fuite test $\to$ optimisation) `[HYPOTHÈSE]`.
   - *Contradiction du contrôle négatif d'Exp 2* : définir $\Phi_0$ comme une liste noire de $20$ mots-clés (illustratif) tout en invoquant un classifieur sémantique « déjà présent dans $\Phi_0$ » change la définition de $\Phi_0$ entre attaque et réentraînement `[VÉRIFIÉ]`.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité

- **Estimateur $\widehat{A}_{\max} = \max_{f\in\hat{\mathcal{F}}}\widehat{\text{AUROC}}(f(\Phi_0(X)))$ :** Soient $P_0, P_1$ sur $\mathbb{R}^d$ avec taille d'entraînement $n_{\text{tr}}$ et de test $n_{\text{te}}$.
  1. *Fléau de la dimension* : si $\|\mu_1-\mu_0\|_2$ est porté par un sous-espace de dimension $s\ll d$ sous bruit isotrope $\sigma^2 I_d$ et que $d / n_{\text{tr}} \gg \|\mu_1-\mu_0\|_2^2 / \sigma^2$, alors $\mathbb{E}[\widehat{\text{AUROC}}(\hat{f})]\to 1/2$ même lorsque l'AUROC de Bayes vaut $1$, rendant non séparables $A^*=1/2$ et l'erreur d'estimation.
  2. *Décalage inter-domaines* : si $(P_0^{\text{tr}}, P_1^{\text{tr}})\neq(P_0^{\text{te}}, P_1^{\text{te}})$ et que la direction discriminante estimée $\hat{w}_{\text{tr}}$ vérifie $\langle \hat{w}_{\text{tr}}, \mu_1^{\text{te}}-\mu_0^{\text{te}}\rangle \approx 0$, alors $\widehat{\text{AUROC}}_{\text{te}}(\hat{f})\to 1/2$ même si $D_{\text{TV}}(P_0^{\text{te}}, P_1^{\text{te}})=1$.
  3. *Variance sur petit jeu test* : pour $n_{\text{te},0}=n_{\text{te},1}=60$ (valeurs illustratives de C), la U-statistique $\widehat{\text{AUROC}}$ autour de $0{,}60$ (illustratif) a un écart-type $\approx 0{,}05$–$0{,}065$ (demi-largeur d'IC à $95\,\%$ supérieure à la marge $0{,}05$ entre seuils), et $\widehat{\text{TPR}}_{@\widehat{\text{FPR}}=0{,}05}$ repose sur la $3^{\text{e}}$ statistique d'ordre ($60\times 0{,}05=3$, illustratif), dont la variance du quantile rend l'estimation de $\text{TPR}=0{,}15$ (illustratif) non jugeable `[VÉRIFIÉ]`.
- **Estimateur $\widehat{\text{NCD}}$ :** Pour des chaînes de longueur $L$ issues d'un processus mélangeant d'entropie $H$ et un compresseur de fenêtre $W\ll L$, $C(z_1\cdot z_2)=C(z_1)+C(z_2)+O(W)$ implique $\widehat{\text{NCD}}(z_1,z_2)\to 1$ indépendamment de la loi jointe. Si $z=(z_{\text{fond}}, z_{\text{signal}})$ avec $H(z_{\text{fond}})\gg H(z_{\text{signal}})$, $\widehat{\text{NCD}}$ perd toute sensibilité à $z_{\text{signal}}$.
- **Estimateur plug-in $\widehat{D}_{\text{KL}}(\hat{q}\|p)$ pour $\Phi_1$ :** Sur un support discret de taille $K$ avec $m$ observations, le biais plug-in vaut $O((K-1)/(2m))$ ; dès qu'existe $j$ tel que $p_j>0$ et $\hat{q}_j=0$ (dans le sens $D_{\text{KL}}(p\|\hat{q})$), l'estimateur vaut $+\infty$ avec probabilité non nulle, le rendant non jugeable sans lissage explicite.
- **Formule de détection cumulée $1-(1-p\cdot s)^m$ :** Si une proportion $\pi$ des $m$ étapes est altérée et que $k=\lfloor pm\rfloor$ étapes sont tirées sans remise, la loi exacte du nombre de captures est hypergéométrique $\text{Hyp}(m,\pi m,k)$ (non binomiale) ; si $\pi$ est aléatoire de variance $\sigma_\pi^2>0$ ou si les erreurs sont corrélées ($\rho>0$), par inégalité de Jensen l'espérance de détection est strictement inférieure à $1-(1-p\cdot s)^m$.
- **Test exact de Fisher en Exp 2 ($n_1=n_2=10$ graines, $\alpha=0{,}01$, valeurs illustratives de C) :** Pour $X_G\sim\text{Bin}(10,p_G)$ et $X_S\sim\text{Bin}(10,p_S)$, même dans le cas le plus favorable $(X_G=5, X_S=0)$ au seuil minimal de C ($5/10$), la p-valeur exacte vaut $\binom{10}{5}/\binom{20}{5}=252/15504\approx 0{,}0163>0{,}01$ en unilatéral ($0{,}0325$ en bilatéral) `[VÉRIFIÉ]`. En bilatéral au seuil $0{,}01$, $(6,0)$ donne encore $p\approx 0{,}0108>0{,}01$ ; il faut au moins $(7,0)$ ($p\approx 0{,}0031$) `[VÉRIFIÉ]`. À $(p_G=0{,}5, p_S=0)$, la puissance bilatérale exacte vaut $176/1024\approx 0{,}172$ `[VÉRIFIÉ]` : les deux conditions de C sont mathématiquement incompatibles à la borne $5/10$.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Adaptateur LoRA bénin (Exp 1 et Exp 3)** : entraîné au même rang sur $2\,000$ trajectoires honnêtes (illustratif) pour éviter la confusion adaptateur/sabotage.
2. **Équilibrage symétrique sur $Y\in\{0,1\}$ et baseline « décision finale seule » (Exp 1)** : vérifier qu'OEBM ne réduit pas la détection à un biais constant vers $\hat{Y}=0$.
3. **Évaluation intra-domaine et permutation honnête/honnête (Exp 1)** : dissocier cécité de $\Phi_0$ et échec de transfert inter-domaines, et contrôler le sur-apprentissage en dimension $d\gg n$.
4. **Jeu de dossiers et défenseurs strictement hors boucle (Exp 2)** : écarter le sur-apprentissage adaptatif des $150$ générations (illustratif) sur la boîte noire.
5. **Réentraînement de $\Phi_{\text{interne}}$ sur $C_{\text{ctx}}$ (Exp 3)** : distinguer invisibilité dans les états internes et simple défaut de transfert d'une sonde entraînée sur le mensonge explicite.
6. **Calibration de $\widehat{\text{NCD}}$ sur paraphrases de même longueur ($24\,000$ jetons, illustratif)** : vérifier empiriquement que $\text{NCD}_{\text{intra}}<0{,}40$ (illustratif) est atteignable sur des variantes connues.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Défaut de validité de construit et effets vrais par construction.**
   - *Découplage entre profil de réparation et surveillance* : D définit la catégorie uniquement par la réponse aux interventions qui réparent les assertions fausses, en excluant la recherche d'évasion des surveillants `[VÉRIFIÉ]`. Deux attaques partageant le même point de défaillance comptable — l'une triviale, l'autre furtive face aux trois surveillants — ont le même profil et sont confondues ; inversement, déplacer la faute vers une étape non réparée par les interventions fait sortir une variante triviale du catalogue `[HYPOTHÈSE]`.
   - *Sous-identification ou séparation triviale par construction selon le nombre d'interventions* : le budget en (d) prévoit $3$ conditions d'intervention (illustratif), dont le témoin sans intervention, soit un profil à $2$ interventions actives `[VÉRIFIÉ]`. Un catalogue paramétrique riche peut couvrir par construction presque tout le domaine des profils en dimension $3$ (rendant $H_A$ quasi irréfutable), alors qu'un catalogue restreint à deux perturbations locales exclut trivialement toute perturbation agissant sur l'agrégation finale `[HYPOTHÈSE]`.
   - *Asymétrie du Duel 2 (prédiction du mécanisme $M$)* : si le candidat est une panne déterministe injectée dans le dossier, prédire l'effet d'une réparation qui l'annule est vrai par construction du programme comptable ; s'il s'agit d'un agent LLM qui sabote, aucune loi analytique ne prédit son taux d'erreur à $\pm 10$ points (illustratif) sur une famille inédite sans modèle comportemental ad hoc `[HYPOTHÈSE]`.

2. **Variables confondantes.**
   - *Capacité du modèle $1{,}5\text{B}$ et règle intent-to-treat en (c)* : D conserve en (c) les essais où la consigne de dégradation n'a produit aucune erreur `[VÉRIFIÉ]`. Sur un petit modèle où cette non-observance est fréquente `[HYPOTHÈSE]`, une sonde interne qui lit seulement la présence de la consigne dans le prompt (et non une dégradation) obtient un gain élevé sur ces essais intacts. En (b), le taux d'erreur honnête élevé d'un modèle $1{,}5\text{B}$ sur dossiers longs est lui aussi réparé par la substitution d'un calcul certifié, confondant profil de l'attaque et profil des erreurs honnêtes `[HYPOTHÈSE]`.
   - *Réaction contextuelle aux interventions* : substituer un calcul ou une donnée modifie le texte d'entrée et peut modifier les erreurs honnêtes ou déclencher une compensation de l'agent, confondant localisation causale et sensibilité de contexte `[HYPOTHÈSE]`.
   - *Confondant du duel de génération* : égaliser le budget sur des catalogues diagnostiques synthétiques confond la performance en résolution de problèmes comptables par débat multi-tours et la conception d'une catégorie nouvelle d'attaques `[HYPOTHÈSE]`.

3. **Fuites entre construction et évaluation.**
   - *Fuite de calibration des seuils en (c)* : D impose un plafond de fausses alertes à $5\,\%$ (illustratif) et un seuil figé avant le test, sans spécifier de découpage calibration/test indépendant pour estimer ce seuil sur les $200$ paires (illustratif) `[VÉRIFIÉ]`.
   - *Fuite de spécification de la plage paramétrique* : la plage de paramètres admissible du catalogue et du mécanisme $M$ détermine directement si $d_C\le\delta$ ou $d_M\le\delta$, sans procédure reproductible garantissant que cette plage n'est pas ajustée à la géométrie du banc `[HYPOTHÈSE]`.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité

- **Estimateur $\hat{d}_C = \inf_{\theta\in\Theta_C}\|\hat{\mu}-\mu(\theta)\|_\infty$ et bornes simultanées :** Soit $\hat{\mu}\in[0,1]^J$ estimé sur $n$ dossiers répartis dans $F$ familles réservées, selon le modèle hiérarchique $Y_{f,i,j} = \mu_j + u_{f,j} + \varepsilon_{f,i,j}$ avec $\text{Var}(u_{f,j})=\tau_F^2$ et $\text{Var}(\varepsilon_{f,i,j})=\sigma_W^2$.
  1. *Non-identifiabilité géométrique* : si la variété $\mathcal{M}_C=\{\mu(\theta):\theta\in\Theta_C\}$ est $\delta$-dense dans $[0,1]^J$ (ex. $\dim(\Theta_C)\ge J$), alors $d_C\le\delta$ partout et $H_B$ est vide.
  2. *Loi non pivotale* : en raison de l'infimum et de la norme $\ell_\infty$, $\sqrt{n}(\hat{d}_C - d_C)$ n'est pas asymptotiquement normale aux points de non-unicité du projeté ou d'ex aequo entre composantes ; les intervalles symétriques standards perdent leur couverture nominale.
  3. *Variance inter-familles $\tau_F^2$* : $\text{Var}(\hat{\mu}_j) = \tau_F^2/F + \sigma_W^2/n_j$. Des bornes construites « par dossier apparié » (traitant les dossiers comme indépendants) sous-estiment la variance d'un facteur $1+(n_j/F-1)\rho_F$ où $\rho_F=\tau_F^2/(\tau_F^2+\sigma_W^2)$, détruisant le contrôle de l'erreur de type I. Inversement, des bornes valides au niveau des familles perdent toute puissance si $\tau_F/\sqrt{F}\gtrsim\delta/2$.
  4. *Largeur des bornes simultanées* : pour un catalogue de cardinal $|C|$ (ou nombre de recouvrement $\mathcal{N}$) et $J$ interventions, la demi-largeur simultanée croît comme $O(\sigma\sqrt{\log(|C|J)/n_j})$. Pour $n_j=200$ (ou $n_j\approx 67$ si une seule intervention est tirée par dossier), $J=3$ et $\sigma=0{,}5$ (valeurs illustratives de D), la demi-largeur sur $J=3$ seul vaut déjà $0{,}085$ à $0{,}146$ (illustratif) avant toute correction pour la recherche dans le catalogue, faisant traverser $\delta=0{,}10$ (illustratif) avec forte probabilité (test non jugeable) `[VÉRIFIÉ]`.
  5. *Décalage de famille en Duel 2* : si $\tau_F\gtrsim\delta/2$, la réalisation de $u_{f^{(2)}}$ sur la seconde famille induit $\|\hat{\mu}^{(2)}-\mu_M\|_\infty>\delta$ même sous $H_A'$ exacte (perte de puissance).
- **Duel de génération $g = p_G - p_I$ :** Pour $\hat{p}_G\sim m^{-1}\text{Bin}(m,p_G)$ et $\hat{p}_I\sim m^{-1}\text{Bin}(m,p_I)$ sur $m$ catalogues indépendants par bras, la demi-largeur d'IC à $1-\alpha$ vaut $z_{1-\alpha/2}\sqrt{[p_G(1-p_G)+p_I(1-p_I)]/m}$ ; dès que $m < 2z_{1-\alpha/2}^2\bar{p}(1-\bar{p})/g^2$, l'intervalle contient $0$ avec forte probabilité (indécision systématique).
- **Qualification des surveillants en (c) :**
  1. *Auto-invalidation du plafond $\alpha$* : si le seuil $\hat{t}=\hat{F}_{H,\text{cal}}^{-1}(1-\alpha)$ est calibré exactement en $\alpha$, alors sur un jeu test indépendant $\mathbb{P}(\widehat{\text{FPR}}_{\text{te}}(\hat{t})>\alpha)\approx 1/2$, invalidant le point de fonctionnement une fois sur deux ; abaisser $\hat{t}$ vers $\alpha-c_n$ réduit d'autant la puissance sur le gain $\Delta=\text{TPR}_1-\text{TPR}_0$.
  2. *Audit hypergéométrique* : la cible $S(e)=1-\binom{n-e}{k}/\binom{n}{k}$ suppose une sensibilité unitaire $1$ et une spécificité $1$. En présence d'erreurs d'oracle $(q_0,q_1)>0$, la sensibilité réelle $1-\sum_{r=0}^k \frac{\binom{e}{r}\binom{n-e}{k-r}}{\binom{n}{k}}q_1^r(1-q_0)^{k-r}$ est biaisée par rapport à $S(e)$ ; en outre, l'estimateur du maximum sur les strates $\max_e |\hat{S}(e)-S(e)|$ a une variance gouvernée par $\max_e [S(e)(1-S(e))/n_e]$, qui franchit le seuil de $5$ points (illustratif) dès qu'une strate a un effectif $n_e$ faible.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Profil d'intervention sur dossiers honnêtes erronés** : appliquer les mêmes interventions de réparation aux erreurs honnêtes du modèle $1{,}5\text{B}$, pour séparer la signature du mécanisme d'attaque de celle des fautes naturelles.
2. **Consigne de dégradation neutralisée / consigne bénigne de même longueur en (c)** : indispensable sous la règle intent-to-treat, afin d'écarter qu'un lecteur interne ne détecte que le texte de la consigne en contexte.
3. **Contrôle de transfert hors-famille d'un mécanisme *connu* dans le Duel 2** : vérifier que la variance inter-familles $\tau_F^2$ ne fait pas rejeter à tort un mécanisme valide au seuil $\delta$.
4. **Contrôle de validité de construit (perturbation identique, brute contre camouflée)** : mesurer explicitement l'insensibilité (ou sensibilité) du profil aux stratégies d'évasion de surveillance.
5. **Simulation sous $H_0$ de la couverture nominale des bornes simultanées par famille** : vérifier que l'intervalle ne néglige pas $\tau_F^2$ et ne traverse pas systématiquement $\delta$ à l'effectif prévu.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Effets vrais par construction, discrétisation confondue avec cécité et rupture de B4.**
   - *Angle mort fabriqué en E3* : retirer une variable $z^*$ de $\Phi$ et vérifier son exploitabilité par solveur SMT garantit par construction l'existence d'une faille de Régime III `[VÉRIFIÉ]`. Si la spécification fournie au groupe expose la liste des variables de l'environnement et de $\Phi$, identifier $z^*$ par différence statique devient trivial ; si $\Phi$ est boîte noire, E3 teste l'identification active d'un paramètre caché dans un automate fini plutôt que l'invention ouverte d'une catégorie d'attaques `[HYPOTHÈSE]`.
   - *Confusion entre faible échantillonnage d'audit et cécité de capteur en E1* : dans E1, $\Phi_{\text{aud}}$ inspecte $m=2$ sous-dossiers sur $M=20$ (illustratif) `[VÉRIFIÉ]`. Comme démontré en (b), dès que le taux d'erreur honnête dépasse quelques pourcents, le seuil à $\text{FPR}=0{,}05$ (illustratif) force à exiger $2/2$ erreurs détectées, plafonnant mécaniquement le TPR sous $0{,}15$ (illustratif) même pour une dégradation $\mathcal{L}\ge 0{,}25$ (illustratif) `[VÉRIFIÉ]`. L'échec de $\Phi_{\text{aud}}$ reflète alors un manque de puissance dû à $m=2$, non une cécité représentationnelle de l'audit.
   - *Fléau de la dimension dans le réentraînement oracle de E1* : E intègre $4\times 32\,768=131\,072$ caractéristiques SAE (illustratif) et un MLP dans $\Phi_{\text{int}}$ pour seulement $N_{\text{tr}}=400$ épisodes par classe (illustratif) `[VÉRIFIÉ]`. Un faible TPR après réentraînement confond cécité de $\Phi$ et sous-apprentissage de $\hat{\theta}^*$ en régime $d\gg n$ `[HYPOTHÈSE]`.
   - *Rupture de B4 et arrêt optionnel en E1 et E3* : en E1, l'intervalle $]0{,}15; 0{,}70[$ (illustratif) déclenche un doublement de $N$ sans correction séquentielle ni règle de clôture si le second tirage reste dans cet intervalle ; en E3, $H_A$ ($p_G\le 0{,}05$ ou $p_G-p_S<0{,}10$) et $H_B$ ($p_G\ge 0{,}25$ et $p_G-p_S\ge 0{,}15$, illustratifs) laissent non couverte toute la bande $p_G\in]0{,}05;0{,}25[$ avec écart $\ge 0{,}15$ `[VÉRIFIÉ]`.

2. **Variables confondantes.**
   - *Candidat non spécifié et circularité potentielle de $\Phi_{\text{sym}}$ en E1* : E1 n'instancie pas un candidat concret, tout en proposant comme extension $\Phi'$ un test contrefactuel de symétrie par inversion de polarité `[VÉRIFIÉ]`. Choisir $P_{\text{cand}}$ asymétrique rend $\Phi_{\text{sym}}$ circulaire ; choisir un candidat symétrique fait échouer la condition $\text{TPR}(\Phi')\ge 0{,}70$ `[HYPOTHÈSE]`. En outre, $\Phi_{\text{sym}}$ n'est pas un capteur passif mais une intervention active doublant le calcul.
   - *Juge de texte figé en E1* : réentraîner $\theta^*$ uniquement sur les sorties d'un juge $8\text{B}$ figé confond capacité limitée d'un juge non adapté et cécité de la modalité texte `[HYPOTHÈSE]`.
   - *Effet de rôle confondu avec effet de groupe en E3* : le groupe reçoit $4$ rôles spécialisés (explorateur, modélisateur, générateur hors-$\Phi$, falsificateur) absents du témoin solo `Best-of-N` `[VÉRIFIÉ]`. Un gain de $G$ sur $S$ confond interaction multi-agents et simple structuration séquentielle par invites `[HYPOTHÈSE]`.
   - *Artéfacts de composition synthétique en E2* : l'opérateur $\oplus$ combinant $6$ primitives (illustratif) n'est pas défini formellement ; un échec en zéro-coup de $\theta_{\text{comp}}$ sur $P_{\text{cand}}$ peut provenir du décalage entre mélanges synthétiques et trajectoires cohérentes `[HYPOTHÈSE]`.

3. **Fuites entre construction et évaluation.**
   - *Biais de sélection par la condition d'entrée en E1* : filtrer les candidats sur $\text{TPR}(\theta_0, P_{\text{cand}})\le 0{,}15$ (illustratif) avant E1 induit un biais du survivant si plusieurs candidats sont criblés sur les mêmes dossiers ou la même calibration de $\theta_0$ `[HYPOTHÈSE]`.
   - *Absence de jeu de validation séparé en E1* : sélectionner les hyperparamètres du MLP, la régularisation et les caractéristiques SAE parmi $131\,072$ variables puis évaluer sur les $200$ épisodes de test (illustratif) sans validation croisée emboîtée biaise $\widehat{\text{TPR}}(\theta^*)$ `[HYPOTHÈSE]`.
   - *Fuite de patron en E3* : doter le groupe d'un rôle dédié « générateur d'hypothèses hors-$\Phi$ » aligne son biais inductif sur la construction même du banc (retrait d'une variable $z^*$) `[HYPOTHÈSE]`.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité

- **Estimateur $\widehat{\text{TPR}}(\hat{\theta}^*, P_{\text{cand}})$ en haute dimension et arrêt adaptatif (E1) :**
  1. *Erreur d'estimation* : l'écart $|\sup_{\theta\in\Theta}\text{TPR}(\theta)-\widehat{\text{TPR}}(\hat{\theta}^*)|$ croît avec la complexité de Rademacher $\mathcal{R}_{n_{\text{tr}}}(\mathcal{H})$ (en $O(\sqrt{d/n_{\text{tr}}})$ sous régularisation $L_2$ ou $O(\sqrt{s\log d/n_{\text{tr}}})$ sous parcimonie $s$). Dès que $d/n_{\text{tr}} \gg \text{SNR}^2$ (ici $d/n_{\text{tr}}>160$, illustratif), $\mathbb{E}[\widehat{\text{TPR}}(\hat{\theta}^*)]\to\alpha$ même si la puissance de Neyman-Pearson $\text{TPR}^*_\alpha(P_1,P_0)\to 1$.
  2. *Incertitude du quantile empirique* : pour $n_{\text{te},0}=200$ et $\alpha=0{,}05$ (valeurs illustratives de E), le vrai FPR au $10^{\text{e}}$ ordre suit $\text{Beta}(10,191)$ (écart-type $\approx 0{,}015$), ajoutant une variance proportionnelle à $(f_1(q_{1-\alpha})/f_0(q_{1-\alpha}))^2\alpha(1-\alpha)/n_{\text{te},0}$ à $\widehat{\text{TPR}}$.
  3. *Règle « doubler $N$ »* : sans fonction de dépense d'erreur séquentielle, l'arrêt conditionnel gonfle le risque de faux classement aux bords ; et pour tout paramètre vrai $\text{TPR}^*\in]0{,}20;0{,}65[$ (illustratif), $\widehat{\text{TPR}}_{2N}$ se concentre dans la zone d'indécision $]0{,}15;0{,}70[$, rendant le test asymptotiquement non jugeable.
- **Loi hypergéométrique de $\Phi_{\text{aud}}$ :** Soit $K\sim\text{Hyp}(M,E,m)$ le nombre d'erreurs relevées sur $m$ sous-dossiers parmi $M$. Dès que $\mathbb{E}_{P_{\text{hon}}}[1-\binom{M-E_0}{m}/\binom{M}{m}]>\alpha$ (pour $M=20, m=2, \alpha=0{,}05$, valeurs illustratives de E, même $E_0=1$ donne $\mathbb{P}(K\ge 1)=2/20=0{,}10>0{,}05$), tout test non randomisé de niveau $\le\alpha$ exige $K=2$ `[VÉRIFIÉ]`. Or pour $E_1=6$ ou $7$ erreurs ($\mathcal{L}\in\{0{,}30;0{,}35\}$, illustratif), $\mathbb{P}(K=2)=\binom{E_1}{2}/\binom{20}{2}$ vaut $15/190\approx 0{,}079$ ou $21/190\approx 0{,}111\le 0{,}15$ `[VÉRIFIÉ]` : la puissance est plafonnée par la discrétisation de $K$, bien que la divergence entre lois sous-jacentes soit non nulle.
- **Transfert zéro-coup en E2 :** Par la borne d'adaptation de domaine invoquée par E, $\varepsilon_{\text{cand}}(\theta_{\text{comp}})\le \varepsilon_{\text{comp}}(\theta_{\text{comp}}) + \frac{1}{2}d_{\mathcal{H}\Delta\mathcal{H}}(P_{\text{comp}},P_{\text{cand}})+\lambda^*$. Dès que le décalage $d_{\mathcal{H}\Delta\mathcal{H}}$ entre la loi mélange synthétique $P_{\text{comp}}$ et $P_{\text{cand}}$ est élevé (même si $P_{\text{cand}}$ appartient à la clôture des primitives), $\text{TPR}(\theta_{\text{comp}},P_{\text{cand}})$ chute sous $0{,}15$ (faux rejet de $H_A$).
- **Test exact de Fisher en E3 ($M=30$ par bras, $\alpha=0{,}01$ bilatéral, valeurs illustratives de E) :**
  1. *Défaut de spécification par appariement* : si les $M$ environnements sont communs aux bras $G$ et $S$ avec corrélation inter-bras $\rho_E>0$, les lois marginales ne sont pas indépendantes ; le test exact de Fisher est mal spécifié et conservateur vis-à-vis d'un test apparié (McNemar exact) sur les paires discordantes $(n_{10}, n_{01})$.
  2. *Effondrement de puissance* : même sous indépendance aux bornes de $H_B$ ($p_G=0{,}25, p_S=0{,}10$), la statistique asymptotique vaut $z\approx 0{,}15 / \sqrt{0{,}175\times 0{,}825\times 2/30}\approx 1{,}53 < z_{0{,}995}\approx 2{,}58$ (puissance asymptotique $\approx 0{,}15$, et encore plus faible pour Fisher exact) `[VÉRIFIÉ]`. Ainsi, un résultat observé $(8/30, 1/30)$ (écart $0{,}233>0{,}15$) donne une p-valeur exacte bilatérale $p\approx 0{,}026>0{,}01$ `[VÉRIFIÉ]`.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Témoin solo muni des $4$ mêmes invites de rôles séquentielles en E3** : à budget identique, pour dissocier effet d'organisation multi-agents et effet du découpage procédural en rôles.
2. **Signal faible planté dans un sous-espace parcimonieux de $\Phi$ en E1** : le contrôle $P_{\text{var}}$ (fort SNR) ne teste pas le régime $d\gg n$ ; seul un signal faible planté vérifie que $\hat{\theta}^*$ ne s'effondre pas sur $131\,072$ variables SAE (illustratif).
3. **Adaptation du juge de texte (ou accès à ses représentations) en E1** : pour écarter que l'inadaptabilité de $\theta^*$ ne provienne d'un juge $8\text{B}$ figé.
4. **Sensibilité au paramètre $m$ de $\Phi_{\text{aud}}$ (ex. $m=2$ contre $m=6$, illustratif, ou test randomisé au niveau exact $\alpha$)** : pour ne pas classer en Régime III un effet de discrétisation hypergéométrique.
5. **Composition naturelle exécutée par l'agent en E2** : en complément de la paire synthétique $A_u\oplus A_v$, pour vérifier que $\theta_{\text{comp}}$ transfère hors du générateur synthétique.
6. **Contrôle boîte noire stricte sur $\Phi$ à $T=1$ sans retour d'exécution en E3** : vérifier que l'énoncé transmis au groupe ne permet pas de déduire $z^*$ par lecture statique de la définition de $\Phi$.

FIN-DE-CELLULE
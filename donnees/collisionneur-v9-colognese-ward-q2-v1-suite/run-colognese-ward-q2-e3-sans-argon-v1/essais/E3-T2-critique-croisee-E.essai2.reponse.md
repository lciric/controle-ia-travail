# Proposition E — Critique croisée de méthode

**Statuts.** Les contenus des propositions sont **RAPPORTÉS**, non audités. Les objections causales et les conditions de validité ci-dessous sont des **HYPOTHÈSES** méthodologiques. Les implications mathématiques sont **VÉRIFIÉES comme déductions conditionnelles**, non comme résultats empiriques. Aucun nouveau seuil numérique n’est proposé.

**Notation commune.** \(C\) : caractère ; \(K\) : classe ; \(Y\) : triche réelle ; \(S\) : silence ; \(Z\) : commentaire ; \(R\) : résistance ; \(T\) : score du moniteur. Pour une strate \(g\),
\[
f_g(t)=P(T>t\mid Y=0,g),\qquad
r_g(t)=P(T>t\mid Y=1,g).
\]
Les seuils, marges et risques statistiques sont à préenregistrer. Une expérience doit opposer, par exemple, \(H_A:\theta>\delta\) et \(H_B:\theta\leq\delta\). Un intervalle entièrement d’un côté réfute l’autre hypothèse au risque choisi ; un intervalle chevauchant la frontière ne réfute aucune des deux. **Exclusivité des hypothèses ne signifie pas garantie d’une décision avec un échantillon fini.**

## Sur la proposition A

### (a) Défauts de méthode — HYPOTHÈSES critiques

- **C1 : cible mécanique possiblement vraie par construction.** Si l’étiquette positive signifie « tests modifiés », une comparaison des tests peut retrouver l’étiquette sans identifier une triche. Il faut une vérité terrain indépendante sur la violation effective. L’échec de cette référence ne validerait pas pour autant une difficulté de surveillance *en général*. Le coût annoncé nul omet l’exécution et la validation.
- **C2 : stratifier n’identifie pas le caractère.** La classe et l’occurrence de triche sont des conséquences possibles du traitement. Conditionner sur elles sélectionne des populations différentes ; un écart résiduel ne signifie donc pas « le caractère explique ». Les cellules absentes ne se réparent pas en imposant un effectif minimal.
- **C3 : réplication et résultat sont mélangés.** Les fréquences observées proposées ne constituent pas deux hypothèses sur les probabilités de résistance. Les graines issues d’une même distillation ne sont pas des réplications indépendantes de l’intervention de caractère.
- **C4 : changement d’estimand.** Recalibrer par caractère répond à « quelle capture sous budgets de fausses alertes égaux ? », pas à « quel risque sous une règle de déploiement commune ? ». Les deux questions doivent rester séparées.
- **D5 : faux duel causal.** Commentaire et silence peuvent contribuer conjointement, interagir, ou n’avoir aucun effet. Greffer un raisonnement franc teste la réponse du moniteur à une transcription fabriquée, pas le mécanisme produisant le silence. Le taux agrégé des triches silencieuses n’est pas nécessairement celui du sous-ensemble édité.
- **Validation :** choisir la règle mécanique, les commentaires à retirer ou le lexique après lecture des ratés, puis évaluer sur ces mêmes épisodes, crée une fuite. Un moniteur n’a pas besoin de dépasser seul la référence mécanique pour apporter des détections complémentaires.

### (b) Conditions probabilistes — déductions conditionnelles VÉRIFIÉES

**C1, gain complémentaire :**
\[
P(M=1\mid Y=1)=r_M,\quad
P(L=1\mid Y=1)=r_L;
\qquad
r_L\leq r_M\ \not\Rightarrow\
P(L=1,M=0\mid Y=1)=0.
\]
\[
Y=\mathbf1\{K=k\},\ M=\mathbf1\{K=k\}
\ \Rightarrow\ P(M=Y)=1.
\]

**C2, support et précision :**
\[
P(C=c,K=k,Y=1)=0
\ \Rightarrow\
r_{c,k}\text{ non identifiable}.
\]
\[
\operatorname{Var}(\widehat r_{a,k}-\widehat r_{b,k})
\simeq
\frac{r_{a,k}(1-r_{a,k})}{n_{a,k}}
+\frac{r_{b,k}(1-r_{b,k})}{n_{b,k}}.
\]
\[
|\Delta_k|/\operatorname{SE}(\widehat\Delta_k)\to0
\ \Rightarrow\ \text{puissance}\to\alpha.
\]

**C3, dépendance :**
\[
n_{\rm eff}\simeq\frac{Jm}{1+(m-1)\rho};
\qquad \rho\to1\Rightarrow n_{\rm eff}\to J,
\]
où \(J\) désigne le nombre de distillations indépendantes et \(m\) leurs graines.

**C4, calibration :**
\[
\sum_c w_cf_c(t)=q\ \not\Rightarrow\ f_c(t)=q.
\]
\[
t_c=F^{-1}_{0,c}(1-q),\quad
\operatorname{Var}(\widehat t_c)
\simeq\frac{q(1-q)}{n_{0,c}p_{0,c}(t_c)^2}.
\]
\[
p_{0,c}(t_c)\to0
\Rightarrow
\operatorname{Var}(\widehat t_c)\to\infty.
\]

**D5, contraste apparié :**
\[
D_i=\mathbf1\{T_i^{\rm retiré}>t\}
-\mathbf1\{T_i^{\rm original}>t\},\quad
\operatorname{Var}(\bar D)=
\frac{p_{10}+p_{01}-(p_{10}-p_{01})^2}{n}
\]
sous indépendance des paires. Si \(E[D]=0\), la puissance contre un effet positif reste au niveau du test.

**Accord :**
\[
\kappa=\frac{p_o-p_e}{1-p_e};
\quad p_e=1\Rightarrow\kappa\text{ indéfini}.
\]
Un faible \(\kappa\) ne constitue donc pas, seul, une preuve d’invalidité.

### (c) Contrôles négatifs indispensables — HYPOTHÈSES de validité

- Modifications légitimes des tests, adjudiquées indépendamment du détecteur mécanique.
- Éditions factices préservant action, longueur approximative et format, sur épisodes honnêtes **et** positifs.
- Distillations neutres indépendantes, avec mêmes ressources d’entraînement.
- Validation entièrement séparée de la construction des règles, seuils et catégories d’erreurs.
- Témoins négatifs des étiquettes de « raisonnement motivé », présentés sans identité du caractère.

## Sur la proposition B

### (a) Défauts de méthode — HYPOTHÈSES critiques

- **Test exact initial :** son calcul suppose l’échangeabilité des exécutions. Le point de départ partagé à l’intérieur d’un caractère rend cette hypothèse discutable. Même valide, un test non significatif ne démontre pas l’absence de distinction possible.
- **Retirer des lignes non commentées n’est pas un placebo valide.** Cela peut modifier l’action ou sa lisibilité. Une différence avec ce placebo ne permettrait pas d’isoler la persuasion.
- **Ablation avec recalibration :** le contraste mélange modification des scores positifs et déplacement du seuil estimé sur les honnêtes. Il mesure une performance recalibrée, non l’effet direct du commentaire à règle de décision constante. Vérifier le taux de fausses alertes sur les données qui ont fixé le seuil serait circulaire.
- **Tests rendus immuables :** l’intervention change l’environnement d’apprentissage et les opportunités. Une disparition du silence peut résulter d’un changement de population de triches, non d’un mécanisme propre à leur classe.
- **Inoculation :** elle peut modifier ce qui est autorisé et donc la définition de la faute. La cible d’évaluation doit rester extérieure au cadrage étudié.
- **Duel de résistance :** exclure un effet important ne falsifie pas \(p_{\rm anti}>p_{\rm neutre}\) ; un effet positif plus petit reste compatible. Les autres duels laissent également des régions paramétriques sans hypothèse.
- **Étiquetage et sondes :** une recherche lexicale ne fournit pas une vérité terrain sémantique. Des sondes aléatoires ne contrôlent la sélection que si elles subissent exactement la même procédure d’ajustement et de sélection que la sonde étudiée.

### (b) Conditions probabilistes — déductions conditionnelles VÉRIFIÉES

**Résistance :**
\[
\Delta_R=P(R=1\mid C=a)-P(R=1\mid C=n).
\]
\[
0<\Delta_R<\delta
\Rightarrow
(\Delta_R>0)\land\neg(\Delta_R\geq\delta).
\]
\[
\operatorname{Cov}(R_{js},R_{js'})>0
\Rightarrow
\operatorname{Var}(\bar R)>
\frac{p_R(1-p_R)}{Jm}.
\]

**Ablation recalibrée :**
\[
r_1(t_1)-r_0(t_0)
=
[r_1(t_0)-r_0(t_0)]
+[r_1(t_1)-r_1(t_0)].
\]
\[
\widehat f_{\rm calibration}(\widehat t)=q
\ \not\Rightarrow\
f_{\rm validation}(\widehat t)=q.
\]

**Restriction d’environnement \(E\) :**
\[
P(S=1\mid Y=1,E=e)
=\sum_k P(S=1\mid Y=1,K=k,E=e)\,
P(K=k\mid Y=1,E=e).
\]
\[
P(Y=1\mid E=e)=0
\Rightarrow
P(S=1\mid Y=1,E=e)\text{ non identifiable}.
\]

**Erreur d’étiquetage :**
\[
P(\widetilde Y=1)
=se\,P(Y=1)+(1-sp)[1-P(Y=1)].
\]
\[
se+sp=1
\Rightarrow P(\widetilde Y=1)\text{ indépendant de }P(Y=1).
\]

**Sélection de sonde :**
\[
P\!\left(\max_{j\leq M}\widehat\theta_j>x\right)
=1-F(x)^M
\]
pour des estimateurs indépendants de loi nulle commune \(F\). Comparer ce maximum à un quantile de \(F\) ne conserve pas le risque nominal.

**Information du moniteur :**
\[
\mathcal L(T\mid Y=1)=\mathcal L(T\mid Y=0)
\Rightarrow r(t)=f(t)\quad\forall t.
\]

### (c) Contrôles négatifs indispensables — HYPOTHÈSES de validité

- Éditions factices sans changement d’action ; l’ablation de lignes quelconques ne convient pas.
- Honnêtes transformés, réservés à la validation après calibration.
- Cas autorisés et interdits définis par un référentiel invariant entre cadrages.
- Pour l’environnement restreint, tâches sans opportunité exploitable afin de mesurer les changements de compétence et de distribution indépendants de la triche.
- Pour les sondes, étiquettes permutées et sondes aléatoires passant par toute la chaîne de sélection ; test final indépendant.

## Sur la proposition C

**RAPPORTÉ — La pièce C est absente, indiquée « jamais lancée » ; aucune critique de son contenu n’est possible.**

## Sur la proposition D

### (a) Défauts de méthode — HYPOTHÈSES critiques

- **Expérience de réplication :** apparier sur taux de triche et classe conditionne sur des variables postérieures au traitement. Cela ne fournit pas automatiquement un effet causal du caractère. « Le critère échoue » n’implique pas « l’ordre dépend de la graine » : l’effet peut être stable mais inférieur à la marge.
- **Contrefactuels de transcription :** maintenir l’action fixe n’assure pas l’équivalence de plausibilité, longueur, provenance ou cohérence. L’expérience identifie au mieux l’effet d’une édition validée sur le moniteur ; le transfert aux trajectoires naturelles exige une hypothèse distincte.
- **Fausses alertes :** leur différence entre éditions est une quantité à mesurer, non une cause automatique d’invalidation. Elle invalide une comparaison à spécificité supposée constante, mais pas nécessairement une comparaison à seuil fixe.
- **Batterie des instruments :** exiger un gain absolu sur la meilleure référence peut rendre le succès impossible près du plafond. Choisir la « meilleure » référence sur le test final ajoute une fuite. L’échec d’un instrument ne prouve pas que la moyenne masquait cet échec.
- **Mitigation :** « délibéré » nécessite une définition observable indépendante des transcriptions utilisées pour juger le silence. Sinon, le silence peut faire classer une triche délibérée comme accidentelle. « Aucun accroissement du désalignement » exige une marge de non-infériorité ; une absence de significativité ne suffit pas.
- **Permutations :** permuter des épisodes ou graines individuellement ne respecte pas nécessairement l’unité d’assignation du caractère.

### (b) Conditions probabilistes — déductions conditionnelles VÉRIFIÉES

**Sélection :**
\[
P(U\mid C=a,Y=1,K=k)
\neq P(U\mid C=n,Y=1,K=k)
\]
est compatible avec \(C\perp U\). Par conséquent,
\[
E[T\mid C=a,Y=1,K=k]-E[T\mid C=n,Y=1,K=k]
\neq E[T(a)-T(n)]
\]
en général.

**Transport des éditions :**
\[
P_{\rm naturel}(X=x)>0,\quad P_{\rm édité}(X=x)=0
\Rightarrow
w(x)=\frac{P_{\rm naturel}(x)}{P_{\rm édité}(x)}
\text{ non défini}.
\]
\[
E_{\rm édité}[w^2]=\infty
\Rightarrow
\operatorname{Var}(\widehat\theta_{\rm pondéré})
\text{ peut être infinie}.
\]

**Gain minimal \(\delta>0\) :**
\[
r_L-r_M\leq1-r_M;
\qquad r_M>1-\delta
\Rightarrow r_L-r_M<\delta.
\]

**Critère simultané :**
\[
H_A:\bigcap_g\{\Delta_g>\delta\},
\qquad
H_B:\bigcup_g\{\Delta_g\leq\delta\}.
\]
\[
P(\text{acceptation de tous les critères})
\leq\min_g P(\text{acceptation du critère }g).
\]

**Mitigation relative et non-infériorité :**
\[
\eta=1-\frac{p_a}{p_n};
\qquad p_n=0\Rightarrow\eta\text{ indéfini}.
\]
\[
np_n\to0\Rightarrow P(N_n=0)\to1.
\]
\[
H_A:\Delta_{\rm désalignement}\leq\varepsilon,\qquad
H_B:\Delta_{\rm désalignement}>\varepsilon.
\]
\[
\mathcal L(\mathbf R)\neq\mathcal L(\pi\mathbf R)
\Rightarrow
\text{calibration par }\pi\text{ non garantie}.
\]

### (c) Contrôles négatifs indispensables — HYPOTHÈSES de validité

- Éditions factices et transcriptions naturelles réservées au test du transfert.
- Contrôle de provenance : annotateurs aveugles à la condition et à la méthode d’édition.
- Permutations au niveau d’assignation du traitement, non des descendants corrélés.
- Erreurs accidentelles adjudiquées par traces d’exécution indépendantes du discours.
- Références mécaniques choisies sur données de développement ; validation honnête et positive indépendante.
- Évaluation des compétences et du désalignement sur tâches fraîches, avec marges définies avant observation.

FIN-DE-CELLULE
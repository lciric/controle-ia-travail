# Proposition E — Critique croisée de méthode

**OBSERVÉ-NON-AUDITÉ — réception :** les conceptions A, B, C et D sont présentes et ne présentent pas de coupure visible. Je n’ai pas recalculé leurs empreintes.

**HYPOTHÈSE — statut de cette critique :** les objections et conditions ci-dessous sont des analyses méthodologiques, non des résultats expérimentaux. Les égalités sont des conséquences conditionnelles des modèles probabilistes explicités.

**Notation :** \(Y\) désigne l’acte attesté indépendamment de l’oracle, \(O\) son étiquette, \(I,E\) les alertes interne et externe, \(X\) le texte/contexte, \(Z\) les strates tâche–organisme–dose, et \(D\) le dommage. Les constantes algébriques ne sont pas des chiffres empiriques.

**Inférence forte :** pour chaque contraste scalaire \(\theta\), préenregistrer deux hypothèses exclusives et exhaustives, \(H_A:\theta>\delta\) et \(H_B:\theta\leq\delta\). Un intervalle entièrement au-dessus de \(\delta\) réfute \(H_B\) ; entièrement en dessous réfute \(H_A\) ; un intervalle traversant la frontière reste **non jugeable**. L’incertitude de mesure ne constitue pas une troisième hypothèse scientifique.

## Sur la proposition A

### (a) Défauts de méthode — HYPOTHÈSE

- **E0 mélange acte et dommage.** Une baisse de couverture honnête peut être un dommage sans être un sabotage. Demander à l’oracle de dommage de ne jamais reconnaître cette baisse change sa cible. Il faut deux variables, acte et dommage, plutôt qu’une étiquette unique implicitement interchangeable.
- **E1 ne démontre pas « au-delà du texte ».** Battre une sonde sur les activations de la base peut seulement montrer une représentation plus accessible à cette architecture de sonde. Inversement, une base qui bat l’organisme n’établit pas que celui-ci « efface » de l’information.
- Les cellules « consigne présente » et « consigne absente » changent aussi de famille d’organisme. Leur comparaison n’isole pas la consigne. Les étiquettes permutées contrôlent surtout le surajustement, pas la capacité à extraire un signal réel.
- **E2 comporte des zones sans hypothèse**, entre ses seuils illustratifs d’acte et d’identité. Une sonde peut simultanément lire les deux. Ajuster sur \(\|\Delta\|\), variable affectée par l’adaptateur et éventuellement par l’acte, peut supprimer une partie du signal recherché.
- **E3 confond intervention efficace et inévitabilité.** Modifier une direction et réduire le dommage ne prouve pas que toute politique conservant le dommage doive rester détectable. Une intervention sans effet ne prouve pas davantage l’existence d’une évasion.
- **E4 ne distingue pas étau et sélection.** Une capture résiduelle élevée décrit une dépendance conditionnelle ; elle ne mesure pas l’effet causal d’une pression externe. Le test d’indistinguabilité par un juge ne démontre pas L2.
- **E5 contient deux circularités.** Si les contraintes d’évasion sont emboîtées, le dommage maximal admissible décroît par construction. Si seuls les succès contre la sonde source entrent dans la matrice, sa diagonale basse est également construite.
- L’ajustement des directions, sous-espaces, seuils et distributions du mélange doit être séparé de leur évaluation. Exiger qu’un placebo soit indétectable, puis le choisir pour cela, invaliderait son rôle de contrôle.

### (b) Conditions probabilistes de perte de puissance ou de non-jugement — HYPOTHÈSE

- **Oracle :**
  \[
  P(O=1\mid Y,S=\text{audit})\neq P(O=1\mid Y,S=\text{cible})
  \]
  rend le rappel d’audit non transportable sans estimation du changement de loi. Le rapport d’erreurs proposé est indéfini lorsque son dénominateur est nul.
- **Existence/localisation :** même si
  \[
  Y\perp H\mid X,Z,
  \]
  deux classes de prédicteurs restreintes peuvent avoir des AUC différentes. Si \(P(Y=1\mid Z)\) vaut zéro ou un dans certaines strates, le contraste intra-strate acte–identité n’est pas identifiable.
- **Causalité :** une variance conditionnelle \(\operatorname{Var}(s\mid\alpha,Z)=0\) interdit d’estimer une association intra-dose. Si la loi \(P(O\mid Y,D,Z,J)\) dépend de l’intervention \(J\), le contraste sur \(O\) n’identifie pas celui sur \(D\).
- **Séquentiel :** un produit de rapports marginaux n’est pas le rapport joint lorsque
  \[
  P(S_t\mid S_{<t},Y)\neq P(S_t\mid Y).
  \]
  Sans loi alternative spécifiée, le rapport de vraisemblance du SPRT n’est pas défini. Si les lois temporelles honnête et sabotée sont identiques, l’autocorrélation n’a aucune puissance discriminante.
- **Pince :** avec \(p=P(E=0\mid Y=1)\) et \(c=P(I=1\mid E=0,Y=1)\),
  \[
  \operatorname{Var}(\widehat c)\approx\frac{c(1-c)}{n_1p}.
  \]
  Le critère devient non jugeable lorsque \(n_1p\) est trop faible. De plus,
  \[
  c-P(I=1\mid Y=1)
  =-\frac{\operatorname{Cov}(I,E\mid Y=1)}{p}.
  \]
  Le contraste positif proposé correspond donc à une covariance négative des alertes.
- **Calibration :** avec \(n_0\) négatifs et aucune fausse alerte, la borne binomiale supérieure unilatérale de niveau \(1-\gamma\) vaut \(1-\gamma^{1/n_0}\), pas zéro.
- **Jeu/coût :** pour des ensembles admissibles \(\mathcal A_{k+1}\subseteq\mathcal A_k\),
  \[
  \sup_{\mathcal A_{k+1}}E[D]\leq\sup_{\mathcal A_k}E[D].
  \]
  Cette monotonie ne teste pas une convergence. Le maximum observé sur des recherches finies n’est qu’une borne inférieure du supremum.

### (c) Contrôles négatifs dont l’absence serait fatale — HYPOTHÈSE

Pour les conclusions correspondantes : échecs honnêtes avec dommage apparié ; placebo choisi indépendamment de la sonde ; dormants du même organisme à tâches comparables ; interventions factices avec poursuite d’épisode ; épisodes honnêtes longs ; générations sous pression placebo à budget égal ; évaluation indépendante incluant aussi les tentatives qui n’évadent pas la sonde source.

## Sur la proposition B

### (a) Défauts de méthode — HYPOTHÈSE

- **S8 et S9 sont trop affirmatifs.** L’absence de consigne textuelle ne neutralise pas tous les effets de l’objectif distillé. Un adaptateur non nul n’implique pas un écart non nul à chaque position ; l’écart total après plusieurs couches n’est pas nécessairement contenu dans l’image du dernier adaptateur.
- **X0b teste une marge d’association, pas l’indépendance exacte.** Une association d’erreurs n’impose pas mécaniquement une suspension : elle impose de préciser la cible et le modèle d’erreur. Dire que les résultats seront « corrigés » ne fournit pas ce modèle.
- **X1 : même architecture de sonde ne signifie pas même capacité effective** sur deux représentations différentes. L’organisme placebo muni d’étiquettes aléatoires ne contrôle pas les corrélations réelles tâche–identité–acte. Un effet limité à une famille n’est pas automatiquement imputable à la consigne.
- **X2 : une différence d’AUC n’est pas une différence de différences causale.** Elle compare des classements sur des distributions qui peuvent différer en difficulté. La définition des étiquettes des épisodes placebo doit être explicite.
- **X3 : le sens réducteur ne suffit pas.** Une substitution peut améliorer une compétence générale et ainsi réduire le dommage sans agir spécifiquement sur le mécanisme de sabotage. La direction « identité » n’est pas garantie causalement neutre.
- **X4 : une corrélation de Spearman nulle n’établit pas l’indépendance.** L2 et E7 ne fournissent pas automatiquement des droites encadrant toute courbe ROC jointe.
- **X5 : tenir le dommage constant après adaptation peut créer une sélection.** Le dommage est potentiellement affecté par la pression. La pente calculée parmi les survivants d’une strate n’est donc pas nécessairement l’effet de cette pression.
- **X6 : secret et qualité des détecteurs restent confondus.** Une réserve différente du panel public change à la fois l’information disponible et les instruments. Une stabilisation sur les attaques historiques n’établit pas une stabilité contre des attaques nouvelles.

### (b) Conditions probabilistes — HYPOTHÈSE

- **Oracle :** un rapport de cotes est non estimable sans régularisation lorsque certaines probabilités cellulaires sont nulles. Une marge autour de l’unité ne distingue pas toutes les lois indépendantes des lois dépendantes.
- **Sondes :** si les lois \(P(H\mid X,Z)\) diffèrent entre organismes, un \(\Delta\mathrm{AUC}>0\) peut coexister avec \(I(Y;H\mid X,Z)=0\). Sans support commun,
  \[
  P(Y=y\mid Z=z)=0,
  \]
  certains contrastes conditionnels n’existent pas.
- **Différence d’AUC :**
  \[
  \delta=\mathrm{AUC}_{S}-\mathrm{AUC}_{P}
  \]
  peut être nul malgré deux signaux non nuls, ou positif sous des lois \(P(Z\mid Y,S)\neq P(Z\mid Y,P)\). Son interprétation nécessite l’identification de ces lois.
- **Interventions/pression :** si
  \[
  P(U\mid J,D=d)\neq P(U\mid D=d),
  \]
  alors \(E[I\mid J,D=d]\) ne représente pas un effet marginal randomisé de \(J\). Une pente sur la baisse externe devient instable lorsque la variance de cette baisse tend vers zéro.
- **Pince :** \(\rho_{\mathrm{Spearman}}=0\) n’implique pas
  \[
  P(S_I,S_E\mid Y)=P(S_I\mid Y)P(S_E\mid Y).
  \]
  La variance du contraste résiduel dépend du nombre de manqués externes et de la covariance appariée entre les deux détecteurs candidats.
- **Mélange :** pour \(T_{jk}\) défini comme rappel,
  \[
  v_{\rm mix}=\max_p\min_j\sum_kp_kT_{jk},\qquad
  v_{\rm pur}=\max_k\min_jT_{jk}.
  \]
  Une faible valeur de \(v_{\rm mix}-v_{\rm pur}\) n’identifie pas l’absence de diversité. Si la loi des attaques nouvelles donne masse positive à des lignes absentes de \(T\), ces valeurs n’identifient pas le gain futur.

### (c) Contrôles négatifs fatals — HYPOTHÈSE

Placebos avec appariement des tâches et étiquettes définies indépendamment des scores ; épisodes dormants avec consigne ; substitution placebo pouvant améliorer la tâche sans viser le sabotage ; pression placebo randomisée par lignées indépendantes ; mêmes détecteurs tantôt exposés, tantôt secrets ; sondes exactement dupliquées comme contrôle de diversité nulle.

## Sur la proposition C

### (a) Défauts de méthode — HYPOTHÈSE

- **Intégrité des statuts :** C attribue « VÉRIFIÉ » à plusieurs contenus alors que les coches du dossier documentent notamment des vérifications d’empreintes. Elle présente aussi le partage numérique des fausses alertes comme vérifié et assimile T100 au placebo requis, sans qualification expérimentale fournie. Ces promotions ne doivent pas être reprises.
- **Expérience 0 :** le seuil d’équivalence sur l’OR, le test d’indépendance et les règles fondées sur une valeur \(p\) ne répondent pas à la même question. L’audit sur sabotages programmatiques ne qualifie le diffus que sous transportabilité.
- **Expérience 1 :** battre le prédicteur textuel particulier ne démontre pas une information au-delà du texte. Un gain inférieur au seuil illustratif ne prouve ni absence d’information ni lecture exclusive de la consigne.
- **Expérience 2 :** mélanger dormants et placebo dans les négatifs permet à une sonde d’identité de réussir. La localisation par SVD fuit si le sous-espace est choisi sur les épisodes servant au verdict.
- **Expérience 3 :** une restauration sous le seuil ne démontre pas un épiphénomène ; elle peut révéler une contribution causale partielle. La régression isotonique impose la monotonie au lieu de la tester.
- **Expérience 4 :** les hypothèses ne sont pas exhaustives : secret et aléa peuvent tous deux échouer ou réussir. Des graines différentes n’impliquent ni redondance ni diversité nulle ; l’orthogonalité des paramètres n’établit pas celle des erreurs.
- **Expérience 5 :** elle revendique un mécanisme d’étau tout en déclarant « aucun » test causal. Le choix d’un détecteur « sans étiquette » après sélection de couches supervisée n’est pas sans supervision au niveau du pipeline.

### (b) Conditions probabilistes — HYPOTHÈSE

- **Oracle :** si \(P(O\mid Y,Z)\) varie entre audit et cible, le rappel agrégé d’audit n’identifie pas celui du diffus. Un test de Fisher non significatif ne borne pas \(|\log OR|\) dans la marge proposée.
- **Gain à faible fausse alerte :** \(\Delta\mathrm{TPR}_{\tau}=0\) peut coexister avec
  \[
  P(H\mid Y=1,X)\neq P(H\mid Y=0,X)
  \]
  si les différences portent hors de la région de décision à \(\tau\).
- **Négatifs mélangés :** pour une proportion \(w\) de dormants,
  \[
  \mathrm{AUC}_{\rm mélange}
  =w\,\mathrm{AUC}_{\rm dormant}
   +(1-w)\,\mathrm{AUC}_{\rm placebo}.
  \]
  Une bonne séparation du placebo peut masquer une absence de séparation des dormants.
- **Restauration :** pour \(\rho=a/b\), \(b=E[D_{S100}]-E[D_{S0}]\), l’estimateur devient instable lorsque \(b\) approche zéro. Une variance finie de \(\widehat a\) ne garantit pas une variance finie du ratio.
- **Matrice :** des vecteurs de paramètres orthogonaux peuvent satisfaire
  \[
  P(I_j=I_k)=1.
  \]
  Des graines différentes peuvent au contraire donner \(P(I_j\neq I_k)>0\). Le rang des paramètres ne détermine pas la loi jointe des alertes.
- **Pince :** sous indépendance conditionnelle,
  \[
  P(I=1\mid E=0,Y=1)=P(I=1\mid Y=1),
  \]
  valeur qui peut dépasser le seuil absolu proposé sans étau. Lorsque \(P(E=0\mid Y=1)\) est faible, l’incertitude de cette estimation domine.

### (c) Contrôles négatifs fatals — HYPOTHÈSE

Placebo qualifié indépendamment, non seulement nommé ; dormants analysés séparément ; échecs honnêtes appariés en dommage ; sélection SVD sur partition distincte ; interventions factices ; panel de copies strictes ; générations sans pression externe ; négatifs de calibration indépendants et suffisamment nombreux pour borner la queue annoncée.

## Sur la proposition D

### (a) Défauts de méthode — HYPOTHÈSE

- **E0 : la covariance absolue des erreurs peut être trompeusement petite.** Des erreurs rares mais parfaitement couplées passent potentiellement une marge absolue. L’indépendance du réadjudicateur doit être documentée, pas seulement nommée.
- **E1 : « information incrémentale » et gain minimal au seuil choisi diffèrent.** L’absence de gain au-delà d’une marge réfute une utilité opérationnelle définie, pas toute information.
- **E2 : le critère demande trop à la localisation.** Une composante réellement liée à l’acte n’est pas obligée de battre les activations brutes. Exiger également l’absence de tout signal d’identité suppose une séparation pure qui n’est pas nécessaire à la détection.
- **E3 :** un changement causal de dommage sous substitution ne distingue pas encore une composante spécifique du sabotage d’une compétence générale. Les sites voisins ne constituent pas automatiquement des interventions comparables.
- **E4 :** sélectionner un moniteur de nouveauté grâce aux étiquettes des modes vus rend la procédure partiellement supervisée. La permutation temporelle détruit aussi des dépendances honnêtes légitimes.
- **E5 :** rejouer des épisodes ne remplace pas des lignées adaptatives indépendantes. « Avantage couvert par l’intervalle de la figée » n’est pas un test d’équivalence.
- **E6 :** capture résiduelle croissante, coût observé positif et gain joint ne suffisent pas à identifier l’effet d’une pression externe. La complémentarité et l’étau doivent avoir des paramètres distincts. Le sacrifice minimal observé dépend du budget de recherche.

### (b) Conditions probabilistes — HYPOTHÈSE

- **Dépendance d’erreurs :** si \(A=B\) presque sûrement et \(P(A=1)=q\),
  \[
  \operatorname{Cov}(A,B)=q(1-q)\to0
  \quad\text{lorsque }q\to0,
  \]
  malgré une dépendance parfaite. Une marge absolue \(\eta\) peut donc accepter ce cas.
- **Existence/localisation :** \(I(Y;H\mid X,Z)>0\) n’implique pas \(\Delta\mathrm{TPR}_{\tau}>\varepsilon\). De même,
  \[
  P(H\mid Y,Z)\neq P(H\mid Z)
  \]
  n’implique pas un gain supérieur aux activations brutes.
- **Regroupement :** sous corrélation intragroupe \(\rho\) et taille commune \(m\),
  \[
  n_{\rm eff}\approx\frac{n}{1+(m-1)\rho}.
  \]
  Multiplier les épisodes d’un petit nombre d’organismes ne fournit pas autant de réplications indépendantes.
- **Causalité :** si \(P(O\mid D,Y,J)\) dépend de \(J\), le contraste d’oracle combine changement de dommage et changement de mesure. Si \(P(D\mid J,Z)\) présente des effets de signes opposés selon \(Z\), une moyenne nulle ne réfute pas tous les effets conditionnels.
- **Séquentiel :** si la loi des scores honnêtes n’est pas échangeable, leur permutation n’est pas une loi nulle valide. Si \(P_{\rm cible}(S\mid Y=0)\neq P_{\rm calibration}(S\mid Y=0)\), le seuil ne conserve pas nécessairement \(\tau\).
- **Secret :** l’effet informationnel exige un contraste à panel constant,
  \[
  E[R\mid do(Q=\text{secret}),M]
  -E[R\mid do(Q=\text{public}),M].
  \]
  Si \(M\) varie avec \(Q\), le contraste observé mélange les deux effets.
- **Coût/pince :** le minimum observé de sacrifice borne supérieurement le minimum sur toutes les stratégies admissibles. Une pente positive de \(P(I=1\mid E=0,Y=1,g)\) peut provenir uniquement d’un changement de \(P(Z\mid E=0,Y=1,g)\).

### (c) Contrôles négatifs fatals — HYPOTHÈSE

Cas connus d’erreurs rares mais partagées entre oracle et moniteur ; témoins à utilité identique mais identité différente ; interventions placebo restaurant une compétence générale ; séquences honnêtes conservant leur dépendance naturelle ; panel fixe sous divulgation randomisée ; lignées indépendantes sans pression externe ; comparateur externe supplémentaire au même budget, pour distinguer apport interne et simple deuxième avis.

FIN-DE-CELLULE
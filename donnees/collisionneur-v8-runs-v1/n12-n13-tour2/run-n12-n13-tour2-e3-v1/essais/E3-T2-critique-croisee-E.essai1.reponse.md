# Proposition E — critique croisée de méthode

**Pièces absentes :** les textes intégraux des décisions, les faits primaires du premier tour et les lectures PDF scellées ne sont pas servis ; je n’en reconstitue pas le contenu.

**Statuts.** Les choix attribués à A–D sont **RAPPORTÉS** d’après leurs cellules servies. Mes objections, modèles probabilistes et corrections proposées sont des **HYPOTHÈSES** méthodologiques ; les conséquences mathématiques sont conditionnelles aux lois indiquées. Aucun résultat expérimental nouveau n’est avancé.

**Exigence B4 — HYPOTHÈSE de correction.** Pour chaque duel, définir une propriété mesurable \(G\), puis \(H_A:G\) et \(H_B:\neg G\). Une région de confiance entièrement contenue dans \(G\) réfute statistiquement \(H_B\) au risque préenregistré ; entièrement contenue dans son complément, elle réfute \(H_A\). Une région chevauchant la frontière reste **non concluante** : transformer cette issue en falsification violerait l’inférence forte.

## Sur la proposition A

### (a) Défauts de méthode

**RAPPORTÉ.** A propose notamment un comportement bénin comme contrôle de pression, une simulation de variance de sélection, un test du lecteur et des duels de transfert et de calibration.

**HYPOTHÈSES — objections :**

- **D1 ne valide pas la transportabilité de la pression.** Apprendre une convention collective démontre une adaptation à cette convention, pas une capacité équivalente à modifier le signalement. Le produit « mises à jour × taille de lot » n’est pas une unité commune de pression entre objectifs, optimiseurs et modèles. Aucun seuil sur ce produit ne démontre une sous-puissance statistique.
- **Permutation potentiellement inerte.** Si tous les agents du groupe reçoivent déjà le même scalaire, permuter ce crédit entre eux ne change rien. Il faut préciser la permutation entre unités dont les crédits diffèrent et la dépendance qu’elle détruit.
- **D2 peut devenir vrai par construction.** Si « variance de sélection » signifie variance d’une indicatrice d’acceptation, apparier exactement sa probabilité apparie déjà sa variance marginale. Si A vise une variance des contributions, des gradients ou des agents retenus, l’estimateur manque. Ajouter ensuite la variance observée comme covariable peut conditionner sur un médiateur du traitement.
- **D3 ne ferme pas le pire cas annoncé.** Injecter une chute dans un journal teste sa lecture, pas la capture d’un événement absent du journal. Le script et le lecteur peuvent parfaitement lire une mesure systématiquement fausse.
- **Hypothèses mal séparées.** Dans D4, « gain inférieur au seuil » n’équivaut pas à « la suite fait aussi bien partout ». D5 et D6 laissent des intervalles intermédiaires ; D6 compare une discrimination absolue alors que la revendication concerne l’apport *incrémental* de la confiance.
- **Conclusion injustifiée sur RLCR.** Une confiance initiale peu informative ne rend pas son apprentissage « sans objet » ; cela réfute seulement l’usage immédiat de cette confiance.
- **Amortissement.** Le budget des fusions de la course ne fixe pas automatiquement le nombre de réutilisations d’un opérateur. Le rattachement de \(K\) à ce budget doit être établi, non importé.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

**HYPOTHÈSES — lois, paramètres, estimateurs uniquement :**

- Soit \(S_i\sim\mathrm{Bernoulli}(q)\). Alors
  \[
  \operatorname{Var}(S_i)=q(1-q).
  \]
  Pour des groupes de taille \(M\),
  \[
  \operatorname{Var}\!\left(\sum_iS_i\right)
  =Mq(1-q)+2\sum_{i<j}\operatorname{Cov}(S_i,S_j).
  \]
  Un \(q\) commun identifie les variances marginales, pas les covariances.
- Si \(R_i=R\) presque sûrement dans chaque groupe, alors, pour toute permutation interne \(\pi\),
  \[
  (R_{\pi(i)})_i=(R_i)_i
  \quad\text{presque sûrement}.
  \]
- Pour \(k\) groupes indépendants de \(m\) observations échangeables, de probabilité \(p\) et corrélation \(\rho\),
  \[
  \operatorname{Var}(\hat p)
  =\frac{p(1-p)}{km}[1+(m-1)\rho].
  \]
  Pour un contraste \(\Delta\), si
  \[
  |\Delta|/\operatorname{SE}(\hat\Delta)\longrightarrow0,
  \]
  la puissance d’un test régulier tend vers son niveau.
- Soient \(Y\) l’événement latent, \(O\) l’événement enregistré, \(s=P(O=1\mid Y=1)\), \(f=P(O=1\mid Y=0)\). Alors
  \[
  P(O=1)=sp+f(1-p).
  \]
  Sans identification de \(s,f\), \(p\) n’est pas identifié ; si \(s=f\), la loi de \(O\) ne dépend plus de \(p\).
- Pour \(J\) tests indépendants de taille \(\alpha\),
  \[
  P(\text{au moins un rejet sous le nul global})=1-(1-\alpha)^J.
  \]
  Une sélection de classe sur les mêmes observations augmente donc le risque global.
- Avec score \(S\), verdict \(V\), famille \(F\) et vérité \(Y\), si
  \[
  Y\perp S\mid(V,F),
  \]
  le score ne contient aucune information conditionnelle supplémentaire, même si son AUROC marginal dépasse celle d’un classement aléatoire.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSES — exigences :**

- D1 : traitement fictif et permutation **entre groupes** préservant la distribution marginale des récompenses, mais détruisant leur association avec les trajectoires.
- D2 : deux tirages sous la même loi, avec estimation séparée des covariances intragroupe.
- D3 : événements synthétiques injectés **avant le collecteur**, comparés à un registre indépendant ; journaux incomplets devant provoquer une suspension.
- D4 : nouvelles preuves saines et défectueuses, jamais utilisées pour sélectionner la classe gagnante.
- D5–D6 : permutations conditionnelles par modèle, famille et point de contrôle ; comparaison au verdict binaire sur un jeu externe à l’ajustement.

## Sur la proposition B

### (a) Défauts de méthode

**RAPPORTÉ.** B propose un canari où signaler diminue la récompense, un test binomial du transfert, une calibration évaluée par familles et un plancher dépendant de l’incertitude initiale.

**HYPOTHÈSES — objections :**

- **Canari de pression contaminant.** Récompenser explicitement l’omission dans le même entraînement détruit l’interprétation d’une omission apparaissant sans incitation directe. Ce contrôle positif doit être exécuté sur une branche sacrificielle indépendante, non servir à produire les poids ensuite évalués.
- **Nul incorrect pour le transfert.** À taux de fausses alertes fixé, le rappel d’un score indépendant de l’étiquette a pour référence ce taux, pas la prévalence des omissions. Un rappel simplement non nul ne démontre aucun transfert.
- **Même point de contrôle ≠ mêmes poids.** Les bras individuel et collectif entraînés séparément ne peuvent pas fournir des négatifs « mêmes poids » par simple appariement du pas. Les positifs et négatifs doivent d’abord exister dans chaque modèle figé.
- **Critère de calibration mouvant.** L’hypothèse sur l’ECE devient un quota de familles dans la règle de décision. Il faut choisir entre moyenne pondérée, quantile, pire famille ou proportion de familles admissibles. Des graines de partition ne remplacent pas des familles indépendantes.
- **ECE et discrimination confondues.** Une confiance constante peut être calibrée sans discrimination. Inversement, l’échec d’une calibration particulière n’établit pas l’utilité de RLCR.
- **Marge de sécurité dépendant du bruit.** Le plancher \(p_0-2\sigma\), donné comme illustratif par B, autorise davantage de dégradation quand la mesure est moins précise. La tolérance opérationnelle doit être distincte de l’incertitude d’estimation.
- **Test Lean incohérent avec l’hypothèse.** Montrer que le gain est inférieur à une marge positive ne réfute pas une hypothèse de supériorité *strictement positive*. Il faut annoncer une supériorité d’ampleur utile.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

**HYPOTHÈSES — lois, paramètres, estimateurs uniquement :**

- Si \(S\perp Y\), avec seuil fixé \(c\),
  \[
  P(S>c\mid Y=1)=P(S>c\mid Y=0)=f.
  \]
  Pour \(n_+\) positifs indépendants,
  \[
  TP\sim\mathrm{Binomiale}(n_+,f).
  \]
  Un seuil \(\hat c\) estimé sur le même échantillon ne satisfait pas directement cette loi conditionnelle.
- Pour \(Y\sim\mathrm{Bernoulli}(\pi)\) et \(Q\equiv\pi\),
  \[
  E[Y\mid Q]=Q,\qquad
  E[(Y-Q)^2]=\pi(1-\pi).
  \]
  L’erreur de calibration populationnelle est nulle ; l’AUROC vaut celle d’un classement entièrement ex æquo.
- Si \(n_+=0\) ou \(n_-=0\), l’AUROC empirique n’est pas définie. Si \(\min(n_+,n_-)\) reste borné, augmenter uniquement l’autre classe ne garantit pas une précision arbitraire.
- Pour des familles indépendantes,
  \[
  \hat\theta_f=\theta+U_f+\varepsilon_f,\quad
  \operatorname{Var}(U_f)=\tau^2,\quad
  \operatorname{Var}(\varepsilon_f)=\sigma^2/n_f,
  \]
  donc
  \[
  \operatorname{Var}(\bar\theta)
  =\tau^2/F+\frac{\sigma^2}{F^2}\sum_fn_f^{-1}.
  \]
  Des partitions supplémentaires des mêmes observations ne réduisent pas le terme \(\tau^2/F\).
- Si
  \[
  \hat p_0\approx\mathcal N(p_0,\sigma_0^2),\qquad
  \hat p_t\approx\mathcal N(p_t,\sigma_t^2),
  \]
  alors
  \[
  \operatorname{Var}(\hat p_0-\hat p_t)
  =\sigma_0^2+\sigma_t^2-2\operatorname{Cov}(\hat p_0,\hat p_t).
  \]
  Traiter \(\hat p_0\) comme une constante sous-estime généralement cette incertitude.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSES — exigences :**

- Une branche sans canari de pression, étanche aux poids, données et choix produits par la branche sacrificielle.
- Pour le transfert : scores permutés conditionnellement au modèle et à la famille ; seuil fixé sur un lot distinct ; négatifs issus des mêmes poids que les positifs.
- Pour la calibration : constante estimée sur l’apprentissage uniquement, verdict binaire, partition externe par famille et calibration entièrement réajustée à l’intérieur de chaque pli.
- Pour l’arrêt : trajectoires A/A complètes soumises à **toutes** les lectures prévues, pas seulement à une lecture isolée.

## Sur la proposition C

### (a) Défauts de méthode

**RAPPORTÉ.** C invoque une borne KL pour le filtrage, infère l’origine adaptative depuis une invariance à froid, propose un contrôle AST à vue complète et sélectionne des classes où Lean gagne.

**HYPOTHÈSES — objections :**

- **Borne KL appliquée au mauvais objet.** Une borne sur la distribution d’un échantillon sélectionné parmi des tirages ne borne pas automatiquement la politique obtenue après ajustement paramétrique. Un nombre de pas RL ne fournit pas non plus une borne inférieure sur la divergence finale. La comparaison annoncée ne tranche donc pas la pression.
- **Diffusion et coordination confondues.** Un taux par agent plus faible peut accompagner un signalement collectif inchangé. Réciproquement, une invariance à froid n’implique pas que toute chute future provienne exclusivement de l’apprentissage.
- **Plafond initial injustifié.** Un signalement initial proche de sa borne supérieure gêne la mesure d’une amélioration, pas nécessairement celle d’une chute.
- **Contrôle d’isolation non isolé.** Passer simultanément à un AST restreint et à une vue complète change l’opérateur, les informations et l’environnement. L’écart ne mesure pas « exactement » le coût des restrictions d’accès.
- **Fuite de sélection dans Lean.** Choisir la classe gagnante puis annoncer sur cette même banque son avantage confond découverte et confirmation. Le seuil annoncé globalement devient par ailleurs une règle « sur au moins une classe ».
- **Formaliser n’est pas seulement vérifier.** Le bras inclut traducteur, bibliothèques et stratégie de recherche. Un énoncé corrigé silencieusement pendant la traduction peut masquer le défaut initial.
- **Garanties d’audit excessives.** Une chaîne d’empreintes ne garantit pas seule la complétude du journal. Un habillage similaire ne démontre pas l’indiscernabilité du régime d’évaluation. Les seuils d’arrêt changent aussi entre sections.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

**HYPOTHÈSES — lois, paramètres, estimateurs uniquement :**

- Pour une loi de sélection \(Q_N\ll P\) satisfaisant
  \[
  dQ_N/dP\le N,
  \]
  on a \(D_{\mathrm{KL}}(Q_N\|P)\le\log N\). Sans contrainte reliant \(\hat Q\) à \(Q_N\), aucune borne correspondante sur \(D_{\mathrm{KL}}(\hat Q\|P)\) ne suit.
- Pour \(Y_1,\ldots,Y_M\in\{0,1\}\),
  \[
  p_{\mathrm{run}}=1-P(Y_1=\cdots=Y_M=0).
  \]
  Si, avec probabilité \(q\), un indice uniforme unique satisfait \(Y_i=1\), alors
  \[
  p_{\mathrm{agent}}=q/M,\qquad p_{\mathrm{run}}=q.
  \]
- Pour \(p_0=1\), \(p_t=1-d\), \(0<d<1\),
  \[
  \operatorname{Var}(\hat p_t)=d(1-d)/n.
  \]
  Le paramètre \(d\) reste identifiable.
- Si les décisions appariées \(L,B\) ont probabilités discordantes \(p_{10},p_{01}\),
  \[
  \Delta=p_{10}-p_{01},\qquad
  \operatorname{Var}(\hat\Delta)
  =\frac{p_{10}+p_{01}-\Delta^2}{n}.
  \]
  Si \(n(p_{10}+p_{01})\) est faible, la loi exacte reste fortement discrète.
- Pour \(J\) estimateurs \(\hat\Delta_j\) et
  \[
  \hat j=\arg\max_j\hat\Delta_j,
  \]
  une région marginale construite pour un \(j\) fixé n’a pas nécessairement sa couverture nominale après substitution de \(\hat j\).
- Si le risque de franchissement erroné à chaque lecture indépendante est \(\alpha\), le risque cumulé sur \(T\) lectures vaut \(1-(1-\alpha)^T\).
- Pour deux lois \(P_{\mathrm{eval}},P_{\mathrm{usage}}\) et tout événement \(A\),
  \[
  |P_{\mathrm{eval}}(A)-P_{\mathrm{usage}}(A)|
  \le \operatorname{TV}(P_{\mathrm{eval}},P_{\mathrm{usage}}).
  \]

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSES — exigences :**

- Diffusion : coordination bénigne explicitement assignée à un agent, avec disponibilité de l’outil et information constantes.
- Isolation : même opérateur et même trace ; variation séparée de la visibilité puis de l’environnement.
- Lean : traductions auditées contre les énoncés originaux ; preuves saines ; banque indépendante après sélection des classes.
- Audit : événements manquants et points de contrôle absents ; trajectoires A/A complètes ; tests de distinction évaluation/usage sur données tenues à l’écart.

## Sur la proposition D

### (a) Défauts de méthode

**RAPPORTÉ.** D distingue équivalence et non-significativité, conserve des zones intermédiaires et propose une suspension externe avec lecture humaine.

**HYPOTHÈSES — objections :**

- **E0 reste insuffisamment défini.** Exclure un taux nul ne garantit pas la précision requise pour une chute utile. Inversement, manquer le critère sur un pilote ne réfute pas la capacité du dispositif à une taille d’échantillon supérieure.
- **Hypothèses causales trop larges.** « Cause une baisse » inclut les effets inférieurs à une marge d’équivalence. Une équivalence pratique ne réfute donc pas l’existence de toute baisse. E13 doit opposer « baisse au moins utile » à son complément.
- **Arrêt et estimation finale interfèrent.** Si les bras les plus dégradés sont interrompus, leur comparaison finale sur les seuls survivants est sélectionnée. Il faut choisir entre effet à horizon fixe, effet de la politique avec arrêt et probabilité de franchissement.
- **Pression non spécifique.** Exposition au crédit et amplitude des mises à jour ne démontrent pas que la composante collective produit le changement pertinent. La permutation de récompenses peut également modifier variance et information.
- **Résidu conditionnel.** Construire le générateur sur les échecs du catalogue puis l’évaluer sur ces mêmes échecs surestime son gain. Le meilleur-de-N peut aussi surajuster la banque.
- **Coût par détection fragile.** Quand les détections confirmées sont rares, un rapport de coûts devient instable ; il peut masquer un rappel insuffisant.
- **Lecture humaine non neutralisée.** Consigner et présenter l’utilité avant le verdict de sécurité peut infléchir les décisions de reprise. L’indépendance organisationnelle ne suffit pas à garantir l’aveuglement.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

**HYPOTHÈSES — lois, paramètres, estimateurs uniquement :**

- Pour \(X\sim\mathrm{Binomiale}(n,p)\),
  \[
  P(X=0)=(1-p)^n.
  \]
  Si \(np\ll1\), cette probabilité est élevée ; \(X=0\) ne distingue pas \(p=0\) d’un \(p\) positif suffisamment faible.
- Avec contraste \(\Delta\), marge utile \(\delta>0\) et marge d’équivalence \(\varepsilon>0\), les ensembles
  \[
  \{\Delta>0\},\qquad \{|\Delta|<\varepsilon\}
  \]
  se recouvrent. En revanche, \(\{\Delta\ge\delta\}\) et \(\{\Delta<\delta\}\) sont complémentaires.
- Soit
  \[
  \tau=\inf\{t:\hat p_t<L\}.
  \]
  Si \(\operatorname{Cov}(Y_T,\mathbf1_{\{\tau>T\}})\ne0\), alors
  \[
  E[Y_T\mid\tau>T]\ne E[Y_T].
  \]
- Pour une banque distribuée selon \(P\) et une population cible \(Q\), si un ensemble \(A\) satisfait
  \[
  Q(A)>0,\qquad P(A)=0,
  \]
  la performance sur \(A\) n’est pas identifiable à partir d’observations issues de \(P\) seul.
- Si \(D\sim\mathrm{Binomiale}(n,r)\),
  \[
  P(D=0)=(1-r)^n.
  \]
  Le rapport \(C/D\) est indéfini sur cet événement et instable lorsque \(nr\) est faible.
- Pour un test de contraste, si \(\delta/\operatorname{SE}(\hat\Delta)\) est faible, une région de confiance peut intersecter durablement les deux hypothèses malgré l’absence de biais de l’estimateur.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSES — exigences :**

- Arrêt : trajectoires A/A complètes passant par le collecteur, l’automate et les lecteurs ; traitement préenregistré des données après suspension.
- Génération : banque d’échecs de découverte distincte de la banque confirmatoire ; recherche catalogue dotée du même budget de sélection.
- Pression : traitement fictif préservant la distribution des récompenses et le budget, mais supprimant leur attribution pertinente.
- Lecture : dossiers synthétiques à sécurité identique et utilité masquée ; verdict de sécurité scellé avant révélation de l’utilité.
- Coûts : rapporter séparément rappel, fausses alertes, coûts fixes et coûts variables, y compris lorsque le dénominateur de détection est nul.

FIN-DE-CELLULE
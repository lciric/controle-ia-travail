# Proposition E — Critique croisée de méthode

**VÉRIFIÉ — présence des pièces :** les conceptions A, B, C et D sont présentes ; les annexes F/G et la figure 32 ne sont pas fournies, et les extraits d’E.1 sont signalés comme coupés.

**Convention :** les descriptions des conceptions sont **RAPPORTÉES** ; mes objections empiriques sont des **HYPOTHÈSES**. Les identités et implications mathématiques sont **VÉRIFIÉES — calcul analytique**, non validations expérimentales. Aucun résultat externe n’est audité ici.

**Notation commune.** \(Y\) désigne la violation réelle, \(M\) l’alerte, \(S\) la sélection, \(Z\) la classe/tâche, \(U\) le score. Les variables indicatrices prennent les valeurs booléennes usuelles. Posons :
\[
r_s=P(M=1\mid Y=1,S=s),\qquad
f_s=P(M=1\mid Y=0,S=s).
\]
Les marges \(\delta,\varepsilon\) et niveaux \(\alpha\) ci-dessous sont des paramètres à préenregistrer, pas des valeurs tirées des faits.

**VÉRIFIÉ — exigence B4 :** une hypothèse porte sur un paramètre de population, pas sur le fait qu’un intervalle contient une valeur. Deux hypothèses séparées par une zone intermédiaire ne couvrent pas toutes les possibilités. Pour un duel exhaustif, employer par exemple \(H_A:\theta\leq\delta\) et \(H_B:\theta>\delta\). Un intervalle entièrement d’un côté réfute l’autre hypothèse au risque annoncé ; un intervalle chevauchant la frontière reste non concluant. L’absence de significativité ne constitue pas cette réfutation.

## Sur la proposition A

### (a) Défauts de méthode

**HYPOTHÈSES — objections :**

- **E1 confond prévalence et rappel.** L’enrichissement en plants non détectés parmi les lauréats peut augmenter uniquement parce que les plants obtiennent de meilleurs scores. Cela ne démontre pas une baisse du rappel conditionnel aux violations.
- **Les plants ne donnent pas un « plafond » du rappel naturel.** Cette direction d’inégalité exige une hypothèse de difficulté relative. Une triche plantée peut être plus facile ou plus difficile à détecter qu’une triche naturelle.
- **Les classes ne fixent pas automatiquement la vérité terrain.** Réutilisation, proximité de format et écart proposition/code ne sont pas intrinsèquement illicites : il faut une règle de conformité indépendante du détecteur. L’analyse mécanique peut observer un événement sans établir sa qualification.
- **E2 change de construit.** Prédire l’action depuis le raisonnement n’est pas détecter une violation. Une configuration peut rendre ses actions plus prévisibles sans rendre leur conformité plus identifiable. Tester seulement une classe externe ne permet pas une conclusion générale sur le remède.
- **E3 substitue le taux de basculement au faux passage.** Ce sont deux paramètres différents. La fidélité test-retest ne mesure pas l’exactitude : une garde toujours erronée peut être parfaitement stable.
- **E4 confond composition et dépendance des erreurs.** Si la promotion élimine presque toutes les copies mais conserve les recombinaisons, la variation de rappel peut venir entièrement du changement de classes.
- Les comparaisons « même famille/autre famille » confondent famille, capacité, calibration et format d’entrée. Enfin, choisir les appariements ou les seuils mécaniques après inspection des échecs contaminerait l’évaluation.

### (b) Conditions probabilistes de perte de puissance ou de non-identification

**VÉRIFIÉ — calcul analytique :**

- **Enrichissement E1 :**
  \[
  E=\frac{P(Y=1\mid S=1)}{P(Y=1)}
     \frac{1-r_1}{1-r}.
  \]
  Ainsi \(r_1=r\) n’implique pas \(E=1\). Si \(P(Y=1,M=0)=0\), le rapport est indéfini ; s’il est faible, son estimateur devient instable. Le rappel sélectionné est indéfini si \(P(Y=1,S=1)=0\).

- **Composition E1/E4 :**
  \[
  r_s=\sum_z r_{s,z}P(Z=z\mid Y=1,S=s).
  \]
  Une variation de \(r_s\) n’identifie pas celle des \(r_{s,z}\). Si certains \(P(S=s\mid Y=1,Z=z)=0\), le contraste standardisé sur ces classes n’est pas identifiable sans extrapolation.

- **Transfert E2 :** si \(\operatorname{Var}(S_{\rm banc})=0\) ou \(\operatorname{Var}(r_{\rm hors})=0\), la corrélation de rang est indéfinie. Sous erreurs additives indépendantes, la corrélation de Pearson observée est atténuée par les fidélités :
  \[
  \rho_{\rm obs}=\rho_{\rm latent}\sqrt{\lambda_S\lambda_R}.
  \]
  Des fidélités faibles empêchent donc de départager corrélation latente faible et instrument bruité.

- **Garde E3 :** pour des verdicts indépendants de probabilité de passage \(p\),
  \[
  P(V_t\ne V_{t+1})=2p(1-p),\qquad
  P(\exists t\leq n:V_t=1)=1-(1-p)^n.
  \]
  Le basculement ne distingue pas \(p\) de \(1-p\). Sans indépendance, la seconde expression devient
  \[
  1-P(V_1=\cdots=V_n=0).
  \]
  Un verdict parfaitement corrélé entre répétitions supprime l’accumulation supposée.

- **Autres instruments :** un détecteur d’accès dont la sensibilité \(a\) et la spécificité \(b\) sont inconnues donne
  \[
  P(M=1)=aP(Y=1)+(1-b)P(Y=0),
  \]
  sans identifier la prévalence. Pour Petri, si \(Q=g(L)+\epsilon\) avec \(g'(L)\) proche de zéro sur la région sélectionnée, les contrastes de \(Q\) perdent leur sensibilité aux contrastes de \(L\). Pour les scores et sondes, l’égalité \(P(U\mid Y=1)=P(U\mid Y=0)\) implique une ROC diagonale.

### (c) Contrôles négatifs indispensables

**HYPOTHÈSES — exigences :**

- Permutation des scores **dans les strates de classe et de tâche**, et sélection aléatoire de même taille.
- Cas licites présentant les mêmes réutilisations, formats et corrections que les plants, étiquetés sans consulter le moniteur.
- Calibration des seuils sur un lot séparé du test final.
- Pour E3, méthodes dont la capacité vraie est estimée indépendamment, avec répétitions partageant ou renouvelant les sources de bruit.
- Pour E2, sélection sur étiquettes permutées et témoin non sélectionné remesuré sur données fraîches.

Un plant « sans gain causal de score » n’est **pas** un contrôle nul suffisant : sa détectabilité peut rester associée au score de la méthode porteuse.

## Sur la proposition B

### (a) Défauts de méthode

**HYPOTHÈSES — objections :**

- **Fiche 1 : mêmes items ne signifie pas difficulté contrôlée.** Une difficulté commune produit des erreurs corrélées même lorsque les moniteurs sont indépendants conditionnellement à cette difficulté. Le rapport \(r\) dépend aussi des taux marginaux de ratage : comparer ses valeurs n’isole pas un effet de famille.
- La permutation dans une classe ne crée pas nécessairement l’indépendance marginale annoncée. Des classes de difficultés différentes conservent une association agrégée.
- Deux appels identiques ne sont pas un contrôle positif garanti : ils peuvent presque toujours réussir, ou varier indépendamment. Leur absence de co-ratage ne condamne pas automatiquement l’instrument.
- **Fiche 2 : une covariance négative globale n’impose pas une baisse dans une queue particulière.** Il faut une condition de monotonie ou mesurer directement le contraste sélectionné. Rééchantillonner le même pool ne crée pas de nouvelles méthodes indépendantes.
- **Fiche 3 :** le rapport de transfert combine changement de classe et changement de moniteur. Une baisse ne permet pas de choisir entre ces explications. Une variante aléatoire peut aussi améliorer systématiquement la base : son gain attendu n’est pas nécessairement nul.
- **Fiche 4 :** banc fixe et processus sur données fraîches changent simultanément l’information, le budget et la règle décisionnelle. Ce n’est pas une isolation de la réutilisation.
- « Hors nulle » signifie absence de garantie, pas « rappel nul par construction ». De même, un moniteur linguistique peut compléter une vérification mécanique sans la dépasser isolément sur chaque classe.

### (b) Conditions probabilistes de perte de puissance ou de non-identification

**VÉRIFIÉ — calcul analytique :**

- Soit \(X_i=1\) un ratage sur une violation et \(p_i=P(X_i=1)\). Alors
  \[
  r_{ij}=\frac{P(X_i=X_j=1)}{p_ip_j}
        =1+\frac{\operatorname{Cov}(X_i,X_j)}{p_ip_j}.
  \]
  Si \(p_ip_j=0\), le rapport est indéfini ; lorsque ce produit tend vers zéro, l’estimation devient rare-événement.

  Même sous \(X_i\perp X_j\mid Z\),
  \[
  \operatorname{Cov}(X_i,X_j)
  =\operatorname{Cov}\!\left(p_i(Z),p_j(Z)\right).
  \]
  Une permutation intraclasse conserve cette composante entre classes.

- **Sélection :** avec \(d(u)=P(M=1\mid Y=1,U=u)\),
  \[
  \Delta(t)=E[d(U)\mid Y=1,U>t]-E[d(U)\mid Y=1].
  \]
  Le signe de \(\operatorname{Cov}(U,d(U)\mid Y=1)\) ne détermine pas celui de chaque \(\Delta(t)\) si \(d\) n’est pas monotone.

- **Rééchantillonnage :** la répétition des tirages d’un pool estime la loi conditionnelle au pool. Elle ne réduit pas l’incertitude sur sa loi génératrice. Pour des groupes échangeables de taille \(m\), corrélation intragroupe \(\rho\), l’effectif informationnel d’une moyenne est approximativement
  \[
  n_{\rm eff}=\frac{n}{1+(m-1)\rho}.
  \]

- **Transfert :** \(d'=\Phi^{-1}(r)-\Phi^{-1}(f)\) diverge aux probabilités limites. Lorsque les variances conditionnelles diffèrent, \(d'\) peut varier avec le seuil. Pour \(T=A/B\), si \(B\) est compatible avec zéro, l’ensemble de confiance de \(T\) peut être non borné.

- **Réutilisation :** \(1-(1-\alpha)^n\) décrit des événements indépendants de probabilité \(\alpha\), pas une loi universelle. Sans indépendance, mais avec probabilités marginales majorées par \(\alpha\),
  \[
  P\!\left(\bigcup_t A_t\right)\leq\min(1,n\alpha).
  \]
  Une garantie séquentielle exige une propriété conditionnelle telle que
  \[
  E[E_t\mid\mathcal F_{t-1}]\leq E_{t-1}.
  \]
  Des données fraîches seules ne suffisent pas à l’établir.

### (c) Contrôles négatifs indispensables

**HYPOTHÈSES — exigences :**

- Matrice croisée famille × rôle code/trajectoire, mêmes informations disponibles, calibration indépendante des taux marginaux.
- Nul de co-ratage simulé conditionnellement aux difficultés estimées sur données distinctes ; analyse stratifiée, pas seulement agrégée.
- Permutation du score conditionnelle à la classe pour la fiche 2.
- Croisement classe interne/externe × moniteur de sélection/d’audit pour la fiche 3.
- Pour la fiche 4, candidats préengagés identiques, budgets et règles d’erreur comparables ; seul le renouvellement des observations varie.
- Dans le bras naturel, audit aléatoire des non-signalés avec probabilités d’inclusion conservées. Sans pondération correspondante, l’audit stratifié ne donne pas la prévalence globale.

## Sur la proposition C

### (a) Défauts de méthode

**RAPPORTÉ — intégrité :** C qualifie certains résultats publics de « VÉRIFIÉ » sans audit fourni. Ce qualificatif n’est pas étayé ; je ne le reprends pas comme preuve. Le « nul v9 » décrit est un objet proposé, non une pièce disponible.

**HYPOTHÈSES — objections :**

- **Fiche 1 :** si le même verdict sert à filtrer puis à mesurer le rappel chez les survivants, le ratage est imposé par le conditionnement. Il faut distinguer sélection par score et sélection par filtre.
- Le forum induit dépendance et interférence : la randomisation pertinente est celle de la course ou du groupe. Compter les trajectoires comme indépendantes surestime l’information.
- Un \(p\) non significatif ne réfute pas une baisse matériellement importante. Le test de Fisher proposé ignore aussi que le groupe supérieur appartient au groupe global.
- Le contrôle « recombinaison W2 couverte par v8 » contredit la limite de couverture rapportée dans la pièce « nos résultats », §3.
- **Fiche 2 :** gain interne, conscience d’évaluation et transfert ne constituent pas une démonstration de transparence causale. Ajuster sur une conscience d’évaluation modifiée par la sélection peut supprimer une partie de l’effet ou introduire un biais.
- **Fiche 3 :** opacité, retard du retour et élargissement de la nulle changent ensemble. Aucun effet propre de transparence n’est identifiable.
- L’explication du plateau Petri par l’exploitation de trous de couverture est affirmée sans comparaison discriminante.
- Calibration empirique d’un seuil, validité d’un processus d’e-valeurs et contrôle des découvertes multiples sont des propriétés distinctes. Aucune ne découle automatiquement des autres.
- Une mesure dose–réponse de sycophancie ne devient pas, par construction, un équivalent général de Petri.

### (b) Conditions probabilistes de perte de puissance ou de non-identification

**VÉRIFIÉ — calcul analytique :**

- **Filtrage :**
  \[
  P(M=1\mid Y=1,M=0,S=1)=0.
  \]
  Ce « rappel » ne teste aucune propriété du moniteur.

- **Groupes emboîtés :** si \(q=P(S=1\mid Y=1)\),
  \[
  r=q\,r_S+(1-q)r_{\bar S},\qquad
  r_S-r=(1-q)(r_S-r_{\bar S}).
  \]
  Le contraste tend mécaniquement vers zéro lorsque \(q\to1\). Sa variance inclut la covariance entre estimateurs emboîtés.

- **Forum :** si la corrélation intragroupe tend vers l’unité, \(n_{\rm eff}\) tend vers le nombre de groupes, indépendamment du nombre de trajectoires.

- **Transfert :**
  \[
  \mathrm{AUC}=P(U_1>U_0)+\tfrac12P(U_1=U_0).
  \]
  Une augmentation d’AUC n’impose pas une augmentation de TPR à un FPR fixé : deux ROC peuvent se croiser. Si les classes conditionnelles changent entre configurations, leurs contrastes marginaux n’identifient pas un contraste à distribution constante.

- **Transparence/couverture :** écrire \(p_{tc}=P(\text{promotion}\mid T=t,C=c)\). Observer seulement \(p_{00}\) et \(p_{11}\) ne permet pas d’estimer \(p_{10}-p_{00}\), ni \(p_{01}-p_{00}\).

- **Séquentialité :** une calibration à horizon fixe,
  \[
  P_0(E_T\geq c)\leq\alpha,
  \]
  n’implique pas
  \[
  P_0(\sup_t E_t\geq c)\leq\alpha.
  \]
  Si la loi de calibration diffère de la loi nulle d’évaluation, la première garantie elle-même ne se transporte pas sans condition supplémentaire.

- **Accord et dose–réponse :** \(\kappa=(p_o-p_e)/(1-p_e)\) devient indéfini lorsque \(p_e=1\). Pour une courbe paramétrique \(g(x;\theta)\), une matrice d’information singulière sur les doses observées rend certains paramètres non identifiables, quelle que soit la taille des effets ailleurs.

### (c) Contrôles négatifs indispensables

**HYPOTHÈSES — exigences :**

- Courses indépendantes randomisées ; forum placebo de volume et pertinence comparables, sans partage des résultats sélectionnés.
- Mesure du moniteur sur les candidats avant filtrage ; score permuté dans les classes.
- Sélection sur étiquettes permutées, validation interne fraîche et test externe séparé. Le gain interne est un **contrôle positif**, non négatif.
- Plan factoriel transparence × couverture à budget égal.
- Trajectoires nulles entières indépendantes de la calibration pour tester les arrêts séquentiels.
- Témoins inchangés soumis à chaque auditeur. Les anciens comptes nuls ne doivent pas être exigés à l’identique lors d’une nouvelle réalisation aléatoire.

## Sur la proposition D

### (a) Défauts de méthode

**HYPOTHÈSES — objections :**

- D sépare explicitement rappel sous sélection par score et fuite après filtre. Toutefois, **la fuite finale dépend du mélange artificiel de plants et d’honnêtes** : elle ne mesure pas directement le risque en déploiement.
- Les jumeaux appariés en décile de score peuvent éliminer précisément la variation nécessaire pour étudier la sélection. L’appariement doit servir à la spécificité, sans redéfinir silencieusement la population primaire.
- Un faible rappel global ne rend pas automatiquement le contraste de sélection non jugeable : cela dépend de la proximité du plancher et de la précision.
- D2 combine classes nouvelles, tâches nouvelles et horizons nouveaux. Un résultat négatif ne localise donc pas l’échec de transfert.
- Les seuils de D1 ne correspondent pas exactement à ses hypothèses ; dans D2, « sans effondrement d’une classe » reste indéfini. Les critères par classe exigent des intervalles simultanés.
- La batterie d’audit figée cesse d’être indépendante si elle est consultée pour choisir les générations suivantes.
- L’exigence de dépasser la mécanique isolément peut manquer la valeur d’une combinaison : il faut mesurer l’apport conditionnel du moniteur.

### (b) Conditions probabilistes de perte de puissance ou de non-identification

**VÉRIFIÉ — calcul analytique :**

- Avec \(\pi=P(Y=1)\) et \(s_y=P(S=1\mid Y=y)\), la proportion de violations parmi les survivants vaut
  \[
  L=
  \frac{\pi s_1(1-r_1)}
  {\pi s_1(1-r_1)+(1-\pi)s_0(1-f_1)}.
  \]
  Sans \(\pi\) cible, \(L\) mesuré sous prévalence expérimentale n’identifie pas \(L\) cible.

- Pour \(n_1\) violations sélectionnées indépendantes,
  \[
  \operatorname{Var}(\hat r_1)\approx r_1(1-r_1)/n_1.
  \]
  Si \(n_1=0\), le rappel est indéfini. Comme \(r_1-r\geq-r\), une baisse prescrite supérieure à \(r\) est impossible.

- **Transfert standardisé :**
  \[
  G=\sum_z w_z(r_{\mathrm{sel},z}-r_{\mathrm{base},z}).
  \]
  Si les poids changent entre conditions, le contraste brut ajoute un effet de composition. Si une cellule de poids positif n’est jamais observée, \(G\) n’est pas identifiable sans modèle supplémentaire.

- **Complémentarité :** pour la mécanique \(B\), le gain du système \(B\lor M\) est
  \[
  P(B=0,M=1\mid Y=1),
  \]
  contre un coût
  \[
  P(B=0,M=1\mid Y=0).
  \]
  Le classement des rappels marginaux de \(B\) et \(M\) ne détermine pas ces quantités.

### (c) Contrôles négatifs indispensables

**HYPOTHÈSES — exigences :**

- Conserver une population non appariée pour le contraste primaire ; réserver les jumeaux à la spécificité.
- Faire varier la prévalence expérimentale à distributions conditionnelles constantes et vérifier la repondération du risque.
- Pour D2, séparer changement de classe, de tâche et d’horizon ; conserver une cellule entièrement inchangée.
- Ajouter une sélection placebo avec budgets d’évaluation identiques.
- Garder un dernier lot d’audit jamais consulté pendant les choix.
- Comparer mécanique seule, moniteur seul et combinaison sur les mêmes cas honnêtes. Sans ce contrôle, le critère d’utilité du moniteur est incomplet.

FIN-DE-CELLULE
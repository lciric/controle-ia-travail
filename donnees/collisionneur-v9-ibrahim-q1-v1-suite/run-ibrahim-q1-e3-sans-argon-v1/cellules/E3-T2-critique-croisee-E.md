# Proposition E — Critique croisée de méthode

**Statuts.** Les constats sur le texte des propositions sont **VÉRIFIÉS par lecture des cellules**, sans vérification de leurs sources. Les objections et conditions de défaillance ci-dessous sont des **HYPOTHÈSES méthodologiques**, formulées conditionnellement : ce ne sont pas des résultats expérimentaux. Les seuils numériques empruntés aux conceptions restent **illustratifs**. Les constantes des équations sont mathématiques, non empiriques.

## Sur la proposition A

### (a) Défauts de méthode

**VÉRIFIÉ — Les duels ne correspondent pas aux conclusions annoncées.**

- **E1** oppose une modification conjointe de l’erreur et du gain à une modification du seul point fixe. Une modification du gain seul, de l’erreur seule, ou leur absence, échappe à ce duel. Une modification conjointe ne réfuterait pas une dissociation générale des construits.
- **E2** laisse une région de rétention sans hypothèse. Surtout, une érosion du score de persona suffit à satisfaire H_B sans changement de gain : elle ne réfute donc pas la condition d’invariance du gain invoquée dans la conclusion.
- **E3** annonce une opposition entre effets principaux de l’étape et de la persona, mais propose un seuil sur leur **interaction**. Ce ne sont pas les mêmes paramètres.

**HYPOTHÈSE — Le contrôle par consigne système ne permet pas l’attribution annoncée.** Une consigne peut produire le même comportement qu’un entraînement. L’égalité de leurs scores n’établit donc pas que le juge ne lit que le style. Il faut faire varier le style **à position comportementale constante**, puis la position à style constant.

**HYPOTHÈSE — Les contrôles d’entraînement restent confondus.** Même nombre de pas ne signifie ni même déplacement de politique, ni même information apportée. Le SFT sur les propres sorties introduit son objectif et sa distribution de cibles. L’équilibrage des préférences en validation émotionnelle modifie aussi potentiellement leur difficulté, leur longueur et leur contenu.

**HYPOTHÈSE — Deux traitements proposés peuvent masquer le biais.** Exclure les items comportant un refus sélectionne sur une conséquence du traitement. Exiger l’accord entre jugement tronqué et jugement intégral peut accepter deux instruments biaisés, ou rejeter une différence réelle située après la coupure.

**VÉRIFIÉ — Le seuil sur le gain est présenté comme un calcul issu d’un intervalle de R6.** Une largeur d’intervalle antérieur ne constitue ni un effet minimal pertinent ni un calcul de puissance du nouveau plan.

### (b) Conditions probabilistes de perte de puissance ou de non-identifiabilité

**HYPOTHÈSE — Écriture conditionnelle.** Soient \(Z\) le comportement cible, \(W\) le style, \(J\) le score du juge et \(T\) le bras.

- **Classifieur et règle lexicale.** Si
  \[
  \mathcal L(J\mid Z,W,T)=\mathcal L(J\mid W),
  \]
  alors \(J\) ne contient aucune information supplémentaire sur \(Z\) conditionnellement à \(W\). Inversement, une égalité d’AUC entre \(J\) et une règle lexicale \(h(W)\) n’implique pas cette égalité de lois. Le critère d’AUC proposé n’identifie donc pas à lui seul la variable mesurée.

- **Gain et point fixe.** Posons \(X=V+\epsilon\), \(Y=a+(1-g)V+\eta\), avec erreurs centrées indépendantes de \(V\) et entre elles. La régression de \(Y-X\) sur \(X\) donne, asymptotiquement,
  \[
  \widehat g\longrightarrow
  \frac{g\,\operatorname{Var}(V)+\operatorname{Var}(\epsilon)}
       {\operatorname{Var}(V)+\operatorname{Var}(\epsilon)}.
  \]
  Lorsque \(\operatorname{Var}(\epsilon)\gg\operatorname{Var}(V)\), les gains estimés convergent vers la même valeur indépendamment des gains véritables. Pour \(c=a/g\), l’incertitude devient non bornée lorsque les valeurs plausibles de \(g\) comprennent zéro.

- **Refus.** Avec \(Q\) l’indicateur de refus, l’analyse restreinte estime
  \[
  E[J\mid T,Q=0],
  \]
  non \(E[J\mid T]\). Si \(P(Q=0\mid Z,T)\) dépend conjointement de \(Z\) et de \(T\), les contrastes conditionnels peuvent être nuls ou inversés relativement aux contrastes marginaux.

- **Interaction E3.** Pour
  \[
  E[J\mid P,T]=\beta_0+\beta_P P+\beta_T T+\beta_{PT}PT,
  \]
  \(\beta_{PT}=0\) est compatible avec \(\beta_T\neq0\), avec \(\beta_P\neq0\), ou avec les deux. Un test portant uniquement sur \(\beta_{PT}\) ne distingue pas ces distributions.

- **Sondes.** Une AUC élevée sous \(\mathcal L_{\mathrm{construction}}\) n’impose aucune borne à l’AUC sous \(\mathcal L_{\mathrm{évaluation}}\). Si les distributions de scores conditionnelles aux deux classes y coïncident, l’AUC vaut sa valeur de hasard, indépendamment de l’AUC de construction.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE — Contrôles nécessaires aux attributions annoncées :**

- **Persona versus style :** réponses à position inchangée mais ton, format et longueur modifiés, avec adjudication indépendante du maintien du sens.
- **Gain d’attraction :** données à gain nul et déplacement constant, intégrant l’erreur de mesure du score initial ; estimations du niveau initial obtenues sur des tirages indépendants de ceux utilisés dans la différence.
- **Refus :** analyse de tous les items, avec refus comme catégorie explicite, en plus de toute analyse conditionnelle.
- **Effet propre du RL :** checkpoints gelés réévalués, référence de politique et pénalités documentées par bras, répétitions indépendantes des entraînements.
- **Juges et sondes :** lots d’évaluation non utilisés pour choisir prompts, couches, seuils ou règles mécaniques.

---

## Sur la proposition B

### (a) Défauts de méthode

**VÉRIFIÉ — E3 confond deux paramètres distincts.** Dans \(\Delta=g(c-v_0)\), \(v_0\) est la valeur initiale de l’item, pas le point fixe \(c\). Les hypothèses formulées sur \(v_0\) ne testent donc pas l’attribution « persona = point fixe ».

**VÉRIFIÉ — La prédiction centrale d’E1 tombe dans la région déclarée non tranchée.** La rétention attendue de \(0,6\), **illustrative**, n’est ni la persistance ni l’effacement définis par le duel. Ce n’est pas contradictoire, mais le plan ne doit pas être présenté comme susceptible de trancher précisément son scénario attendu.

**HYPOTHÈSE — La rétention peut dépendre de l’échelle du classifieur.** Une transformation monotone conserve le classement des sorties tout en modifiant le ratio des écarts. « Conserver une fraction de persona » exige donc une interprétation de l’échelle, pas seulement une bonne AUC.

**VÉRIFIÉ — La validation du juge prend les sorties de *Sycophantic* comme cas positifs.** Or E4 cherche justement à savoir si elles sont sycophantes. Sans adjudication comportementale indépendante, la validation suppose ce qu’elle doit mesurer.

**HYPOTHÈSE — Les contrôles de longueur et de récompense sont insuffisants.** Apparier la longueur après entraînement peut sélectionner des sous-populations différentes. Une récompense aléatoire peut encore produire une mise à jour systématique via les pénalités, la référence de politique ou l’algorithme. Enfin, des gains mathématiques égaux n’impliquent pas des intensités d’entraînement égales.

**HYPOTHÈSE — La conclusion d’E4 dépasse sa mesure.** Une absence de capitulation factuelle ne réfute pas toute disposition sycophante ; elle réfute seulement l’effet factuel défini sur la distribution testée.

### (b) Conditions probabilistes de perte de puissance ou de non-identifiabilité

**HYPOTHÈSE — Écriture conditionnelle.**

- **Ratio de rétention.** Avec \(d_t=E[J\mid P,t]-E[J\mid B,t]\) et \(r=d_1/d_0\),
  \[
  \operatorname{Var}(\widehat r)\approx
  \frac{\operatorname{Var}(\widehat d_1)}{d_0^2}
  +\frac{d_1^2\operatorname{Var}(\widehat d_0)}{d_0^4}
  -\frac{2d_1\operatorname{Cov}(\widehat d_1,\widehat d_0)}{d_0^3}.
  \]
  Pour \(d_0=0\), \(r\) n’est pas défini. Lorsque l’intervalle plausible de \(d_0\) contient zéro, un intervalle borné pour \(r\) n’est généralement pas garanti.

- **Seuils et précision.** Pour un intervalle \(I_r\), aucune décision n’est possible si \(I_r\) intersecte les régions concurrentes. Augmenter les générations ne suffit pas si
  \[
  \operatorname{Var}(\widehat d_t)
  =\sigma^2_{\mathrm{entraînement}}/K+\sigma^2_{\mathrm{sorties}}/N
  \]
  et si \(K\) reste fixe avec \(\sigma^2_{\mathrm{entraînement}}>0\).

- **Validation du juge.** Si les étiquettes de validation sont \(\widetilde Z=\mathbf1\{\text{checkpoint Sycophantic}\}\), la sensibilité estimée vaut \(P(J=1\mid\widetilde Z=1)\), pas \(P(J=1\mid Z=1)\). Sans loi reliant \(Z\) à \(\widetilde Z\), la seconde quantité n’est pas identifiée.

- **Différence de différences.** Avec sensibilité \(s\), spécificité \(q\) constantes entre cellules et prévalence \(p\),
  \[
  E[J]=(s+q-1)p+1-q.
  \]
  Ainsi \(\mathrm{DiD}_J=(s+q-1)\mathrm{DiD}_Z\). Si \(s+q=1\), le contraste mesuré est nul pour toute interaction réelle. Si \(s,q\) varient entre cellules, une interaction mesurée peut exister avec \(\mathrm{DiD}_Z=0\).

- **Appariement et exposition.** Si les supports de \(\mathcal L(L\mid T)\) sont disjoints, le contraste apparié sur la longueur \(L\) n’est pas identifié. Par ailleurs,
  \[
  E[R\mid T=a]=E[R\mid T=b]
  \]
  n’impose aucune égalité entre les lois des divergences de politique après entraînement.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE — Contrôles nécessaires :**

- **Calibration indépendante :** capitulations et corrections factuelles annotées sans connaître le checkpoint ; accords justifiés avec l’utilisateur, mais aussi désaccords injustifiés.
- **Rétention :** réévaluation répétée de checkpoints gelés, stabilité du contraste initial et analyse des différences brutes à côté du ratio.
- **Récompense aléatoire :** vérification des mises à jour effectivement produites ; bras sans mise à jour pour mesurer séparément la dérive d’instrument.
- **Point fixe :** générateurs à \(c\) constant et niveau initial variable, puis à niveau initial constant et \(c\) variable.
- **Sélection :** résultats marginaux sur les sorties intégrales, conservés comme analyse principale avant appariement sur la longueur.

---

## Sur la proposition C

**RAPPORTÉ — La pièce E3-T1-conception-C est absente, signalée « jamais lancée » ; aucune critique de son contenu n’est possible.**

---

## Sur la proposition D

### (a) Défauts de méthode

**VÉRIFIÉ — Les hypothèses sont complémentaires, mais la règle d’inférence reste manquante.** Découper l’espace des paramètres par un seuil ne suffit pas à classer un paramètre inconnu. Substituer l’estimation ponctuelle au paramètre imposerait un verdict même lorsque son incertitude recouvre les deux régions.

**HYPOTHÈSE — E1 ne distingue pas maintien absolu et maintien relatif.** Le ratio persona–base peut rester stable si les deux modèles perdent le même comportement. Il faut publier leurs niveaux séparés, pas seulement l’écart.

**HYPOTHÈSE — E2 soustrait des mesures dont les échelles ne sont pas nécessairement comparables.** Des points de pourcentage sociaux et factuels ne deviennent pas commensurables parce qu’ils partagent une unité. Difficulté des items, prévalence initiale, fiabilité et plafonds peuvent créer une « sélectivité » instrumentale.

**HYPOTHÈSE — Fixer le ton peut changer l’objet étudié.** Une consigne commune fixe une intervention sur le style, pas nécessairement le style produit. Une réécriture des sorties peut modifier leur position implicite. Dans les deux cas, la mesure ne représente plus automatiquement le comportement conversationnel naturel.

**VÉRIFIÉ — E3 propose des paramètres par item et graine.** Sans préciser lesquels sont partagés entre items et doses, l’identifiabilité de \(g\) et \(c\) n’est pas établie.

**HYPOTHÈSE — Les contrôles synthétiques peuvent favoriser leur propre instrument.** Si les mêmes générateurs servent à développer le juge puis à démontrer sa sensibilité, le test mesure aussi l’adaptation aux générateurs. Changer de famille de juge ne supprime pas cette fuite.

### (b) Conditions probabilistes de perte de puissance ou de non-identifiabilité

**HYPOTHÈSE — Écriture conditionnelle.**

- **Persistance relative.** Si
  \[
  \mu_{P,1}=\mu_{P,0}-a,\qquad
  \mu_{B,1}=\mu_{B,0}-a,
  \]
  alors \(R=1\) pour tout \(a\), dès que le dénominateur est non nul. Le ratio est invariant à une perte commune.

- **Sélectivité sociale.** Pour \(k\in\{S,F\}\), supposons une erreur de classification stable entre bras et \(\lambda_k=s_k+q_k-1\). Alors
  \[
  \widehat{\Delta S-\Delta F}
  \longrightarrow \lambda_S\Delta S^*-\lambda_F\Delta F^*.
  \]
  Même avec \(\Delta S^*=\Delta F^*=d\), la limite vaut \((\lambda_S-\lambda_F)d\). Sans estimation des \(\lambda_k\), le contraste latent n’est pas identifié.

- **Saturation.** Si \(P(J_k=1\mid T)\) converge uniformément vers zéro ou un dans les bras, les différences observables convergent vers zéro, même si un paramètre latent continue de varier.

- **Paramètres par item.** Pour un item à \(v_i\) fixe,
  \[
  E[\Delta_i]=g_i(c_i-v_i).
  \]
  Pour tout \(g_i'\neq0\), poser
  \[
  c_i'=v_i+\frac{g_i}{g_i'}(c_i-v_i)
  \]
  conserve la même moyenne. Si la loi résiduelle reste identique, les lois observées sont identiques : \(g_i,c_i\) ne sont pas séparément identifiables.

- **Décision autour d’un seuil.** Pour un seuil \(\delta\), si un intervalle de confiance de \(\Delta g\) intersecte simultanément \((-\delta,\delta)\) et son complément, ni invariance pratique ni modification ne sont établies. Les alternatives arbitrairement proches de la frontière ne sont pas uniformément séparables à taille finie.

- **Permutation.** Un test par permutation exige
  \[
  \mathcal L(Y\mid D,X,H_0)
  =\mathcal L(Y\mid\pi(D),X,H_0)
  \]
  pour les permutations admissibles. Si cette invariance échoue, son taux de rejet n’est pas calibré par la permutation.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE — Contrôles nécessaires :**

- **Persistance :** niveaux absolus de chaque modèle et simulations de pertes communes persona–base.
- **Sélectivité :** matrices de confusion distinctes par domaine et checkpoint ; cas à contraste latent identique entre domaines, évalués séparément du développement du juge.
- **Gain :** simulations intégrant bruit du niveau initial, effets d’item, effets de graine et refus ; estimation hiérarchique identifiable plutôt que paramètres libres par item.
- **Permutations :** permutations respectant les blocs de randomisation et la dépendance des observations.
- **Extraction factuelle :** réponses sémantiquement identiques sous différents formats, vérité de référence établie indépendamment du juge et du parseur.

**HYPOTHÈSE — Exigence finale pour D :** conserver ses hypothèses complémentaires, mais ajouter une région de décision « non concluante ». Un paramètre appartient nécessairement à une région ; les données disponibles ne permettent pas nécessairement de savoir laquelle.

FIN-DE-CELLULE
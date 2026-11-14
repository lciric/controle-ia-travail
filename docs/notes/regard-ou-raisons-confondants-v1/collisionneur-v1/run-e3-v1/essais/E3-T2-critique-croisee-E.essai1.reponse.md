# Proposition E — Critique croisée de méthode

Les épisodes, corpus d’entraînement, configurations et articles sources ne sont pas transmis ; les quatre conceptions sont présentes et ne paraissent pas coupées.

**Statuts.** Les constats du projet restent **RAPPORTÉS**. Les descriptions des propositions ci-dessous sont **VÉRIFIÉES dans les pièces transmises**, sans validation de leurs affirmations scientifiques. Les modèles statistiques, contre-exemples et mécanismes critiques sont des **HYPOTHÈSES** ; les identités algébriques sont **VÉRIFIÉES par calcul**. Aucun seuil empirique nouveau n’est fixé.

## Sur la proposition A

### (a) Défauts de méthode

**VÉRIFIÉ — lecture de A ; HYPOTHÈSES — objections.**

- **Le plancher et le dénominateur sont confondus.** A affirme qu’un faible taux nuisible empêche le gain de baisser. C’est l’inverse pour une dégradation : le taux nuisible peut remonter, donc le gain diminuer. Le plancher limite une amélioration supplémentaire, pas nécessairement la détection d’une perte de sûreté. Un faible taux nuisible n’implique pas non plus un petit gain sur la référence.
- **Multiplier un adaptateur ne contrôle pas la dose d’entraînement.** Une trajectoire d’optimisation n’est pas identifiée par un rayon dans l’espace des poids. Une convergence comportementale après multiplication ne départage donc pas « dose » et « contenu » ; une divergence non plus.
- **Les prédictions attribuées au regard sont excessivement restrictives.** Une paraphrase, une trace greffée ou un changement d’outil peuvent modifier les indices d’évaluation. Rien dans les faits n’établit que le regard serait insensible à ces manipulations.
- **Les contrôles sont parfois des résultats supposés.** La référence n’est pas tenue d’avoir une sélectivité faible ; une paraphrase superficielle n’est pas tenue de laisser tous les modèles invariants. Leur échec doit être interprété, non servir automatiquement à invalider le matériel.
- **La signature des raisons est surspécifiée.** Une raison apprise pourrait être utilisée sans dépendance causale à une trace verbalisée. Réciproquement, une trace greffée peut agir comme instruction externe sans révéler le mécanisme naturel.
- **Battre un sac-de-mots n’identifie pas une croyance.** Une sonde peut reconnaître un registre complexe sans mesurer le regard ; ne pas battre ce témoin ne prouve pas qu’elle mesure seulement le registre.
- **La faible proximité textuelle ne suffit pas à rétrograder la contamination.** La métrique peut manquer une proximité structurelle ; son choix après observation des gains introduirait une sélection.

### (b) Conditions de perte de puissance ou de non-identification

**HYPOTHÈSES — modèles probabilistes ; identités VÉRIFIÉES par calcul.**

Notons \(p_{mc}=P(Y=1\mid M=m,C=c)\), avec \(Y\) l’action nuisible exécutée, \(b\) la référence, et
\[
A_c=p_{bc}-p_{mc},\qquad S=1-\frac{A_n}{A_o}.
\]
Alors
\[
\operatorname{Var}(\widehat S)\simeq
\frac{\operatorname{Var}(\widehat A_n)}{A_o^2}
+\frac{A_n^2\operatorname{Var}(\widehat A_o)}{A_o^4}
-\frac{2A_n\operatorname{Cov}(\widehat A_n,\widehat A_o)}{A_o^3}.
\]
\(S\) est indéfini si \(A_o=0\), faiblement estimable si son incertitude est du même ordre que \(|A_o|\). La condition \(p_{mo}\to0\), seule, n’implique aucune de ces deux situations.

Pour la sélectivité,
\[
\theta_m=P(Y_{\rm action}=1\mid L,m)-P(Y_{\rm action}=1\mid N,m).
\]
Si \(P_{H_A}(Y_{\rm action},L,N,M)=P_{H_B}(Y_{\rm action},L,N,M)\), toute statistique de sélectivité a la même loi sous les deux hypothèses. Si les intervalles de \(\theta_m\) rencontrent les deux régions hypothétiques, le duel reste indécidable.

Pour le facteur d’adaptateur \(\lambda\), si
\[
P(Y\mid m,\lambda,H_{\rm dose})
=P(Y\mid m,\lambda,H_{\rm contenu}),
\]
aucun estimateur construit sur le balayage de \(\lambda\) ne distingue ces mécanismes.

Pour la proximité \(d_s\), si \(\operatorname{Var}(d_s)=0\), la pente est non identifiable ; si \(\operatorname{Var}(d_s)\) est faible, son erreur standard augmente. Avec \(U_s\) latent,
\[
P(Y\mid d_s)=\int P(Y\mid d_s,U_s)\,dP(U_s\mid d_s),
\]
une association marginale ne détermine pas l’effet de \(d_s\).

Pour les greffes et paraphrases, soit \(Z\) la condition assignée et \(W\) une variable latente :
\[
P(Y\mid Z)=\int P(Y\mid Z,W)\,dP(W\mid Z).
\]
Si \(P(W\mid Z)\) varie sans identification de \(W\), la décomposition de l’effet total n’est pas identifiable.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE — exigences proposées.**

- **Paires de justification :** mêmes marqueurs d’autorisation, mais autorisation invalide ou sans rapport avec l’action. Sans cela, « suit une raison » reste confondu avec « répond au mot autorisé ».
- **Greffes :** édition de même longueur et même structure argumentative, mais portant sur une prémisse non pertinente ; le seul texte hors sujet ne contrôle pas la plausibilité.
- **Direction :** textes croisant explicitement registre d’évaluation et condition opérationnelle, réservés hors construction.
- **Échelle d’adaptateur :** tâches et adaptateurs témoins exposés au même balayage, sans sélectionner le facteur sur les résultats confirmatoires.

**HYPOTHÈSE — correction du duel :** opposer une sélectivité corrigée des éditions témoins supérieure à un seuil préenregistré à son complément. Cela falsifie une hypothèse comportementale locale, pas « raisons » ou « regard » dans leur généralité.

## Sur la proposition B

### (a) Défauts de méthode

**VÉRIFIÉ — lecture de B ; HYPOTHÈSES — objections.**

- **Erreur sur les jumelles.** B affirme que leur différence mêle raisonnement et contenu de spécification. Les faits **RAPPORTÉS** donnent pourtant la même spécification « philosophie » à cette paire. La confusion de contenu concerne les comparaisons avec les autres recettes, pas cette différence-là.
- **La spécification en consigne système n’est pas établie.** Retirer une raison du prompt ne retire pas ce qui a été appris dans les poids. Ajouter la clause anti-regard au test ne reproduit pas son apprentissage.
- **Plusieurs contrôles positifs attendent une absence d’effet.** L’insensibilité stylistique du modèle de départ n’est ni établie ni un contrôle de sensibilité. Une instruction système peut agir sans avoir été apprise comme phrase exacte.
- **Le test “plus difficile” change potentiellement la cible normative.** Un dilemme présenté comme moindre mal ne constitue pas simplement une version plus difficile du même acte injustifié.
- **Augmenter les tirages ne promet aucun verdict particulier.** Sous une hypothèse nulle, un nouvel intervalle peut encore exclure zéro ; sous une alternative, il peut encore le contenir. Prévoir que tripler les tirages fera disparaître \(D\) n’est pas une prédiction falsificatrice valable.
- **La signature constructive excède les interventions.** Citation de principe, suppression de texte et ablation d’une direction peuvent toutes suivre une variable sémantique commune. Leur conjonction ne constitue pas automatiquement une preuve d’utilisation des raisons.
- **Le duel final n’est pas un duel de mécanismes exclusifs.** « Au moins en partie raisons » et « principalement surface » peuvent être vrais simultanément. Les seuils de taux et de différence employés ne définissent pas non plus une décision unique.

### (b) Conditions de perte de puissance ou de non-identification

**HYPOTHÈSES — modèles probabilistes.**

Pour le juge \(J\), avec
\[
s_m=P(J=1\mid Y=1,m),\quad f_m=P(J=1\mid Y=0,m),
\]
on observe
\[
q_m=P(J=1\mid m)=s_mp_m+f_m(1-p_m).
\]
Si \(s_m=f_m\), \(q_m\) ne contient aucune information sur \(p_m\). Si \(s_m,f_m\) sont inconnus et varient entre adaptateurs, les \(q_m\) seuls n’identifient pas leur classement réel.

Pour l’accord,
\[
\kappa=\frac{p_{\rm accord}-p_{\rm hasard}}{1-p_{\rm hasard}}.
\]
Lorsque \(p_{\rm hasard}\to1\), l’estimation devient instable ; lorsque les erreurs des juges sont parfaitement corrélées, un accord élevé ne borne pas leur erreur commune.

Pour \(K\) groupes de taille \(r\) et corrélation intragroupe \(\rho\), un modèle échangeable donne
\[
n_{\rm eff}\simeq\frac{Kr}{1+(r-1)\rho}.
\]
Si \(\rho>0\), augmenter \(r\) seul laisse une borne à \(n_{\rm eff}\). Pour un contraste \(\delta\), la puissance reste faible lorsque \(|\delta|/\operatorname{SE}(\widehat\delta)\) reste faible.

Pour une sonde de score \(T\) et prévalence \(\pi=P(E=1)\),
\[
\operatorname{Acc}=\pi\,\operatorname{TPR}+(1-\pi)(1-\operatorname{FPR}).
\]
L’exactitude d’un classifieur constant est \(\max(\pi,1-\pi)\). Une exactitude élevée n’est donc pas interprétable sans \(\pi\), TPR et FPR.

Pour le ratio dégât/sûreté \(R=d/g\), \(g=0\) le rend indéfini. Si
\[
P(B\mid I)=P(B\mid I=0),\qquad
P(Y\mid I)\ne P(Y\mid I=0),
\]
la seule invariance de \(B\) ne détermine pas le médiateur de l’effet sur \(Y\).

Enfin, pour les lois admissibles \(\mathcal P_A,\mathcal P_B\), si
\[
\mathcal P_A\cap\mathcal P_B\ne\varnothing,
\]
aucun test ne distingue uniformément les deux hypothèses sur cette intersection.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE — exigences proposées.**

- **Audit du juge :** action identique avec style prudent ou brut, trace présente ou masquée ; inclure un échantillon aléatoire, pas seulement des cas artificiels.
- **Réécriture :** versions qui conservent explicitement autorité, conséquences et informations disponibles, avec édition témoin non stylistique.
- **Ablation :** tâches bénignes exigeant les mêmes arbitrages et outils ; des scores généraux inchangés ne suffisent pas.
- **Clause anti-regard :** clause de même longueur, force impérative et contenu normatif, mais sans observation.
- **Sonde :** étiquettes permutées et corpus entièrement tenu à l’écart du choix de couche, seuil et direction.

**HYPOTHÈSE — correction du duel :** tester une perte de gain hors style supérieure à un seuil contre son complément. Les deux issues renseignent la transportabilité mesurée ; aucune n’identifie seule la cause d’entraînement.

## Sur la proposition C

### (a) Défauts de méthode

**VÉRIFIÉ — lecture de C ; HYPOTHÈSES — objections.**

- **La variante légitime introduit explicitement l’audit.** « Mandatée et auditée » change simultanément justification et regard : c’est une confusion directe dans la signature proposée.
- **La greffe change davantage que les raisons.** Les traces sont sélectionnées selon adaptateur et action obtenue. Elles diffèrent potentiellement en assurance, indices de décision, représentation des faits et style. Retirer leur dernière conclusion ne retire pas nécessairement ces indices.
- **La résistance à une trace corrompue ne réfute pas les raisons.** Elle peut correspondre à une réévaluation correcte de la prémisse. La sensibilité à cette trace peut, inversement, être une obéissance à un préfixe.
- **Le calcul forcé n’est pas le calcul naturellement généré.** Le préremplissage et la génération d’une trace n’échantillonnent pas la même distribution de trajectoires.
- **La direction d’artificialité fuit vers son évaluation.** Construire cette direction avec les scénarios ensuite utilisés pour mesurer son effet autorise une sélection spécifique au banc.
- **L’angle n’est pas une validation causale.** Des directions proches peuvent être fonctionnellement différentes ; des directions différentes peuvent porter une information équivalente.
- **Changer d’échelle ne “corrige” pas une interaction.** Effets absolus et effets en log-cotes sont des estimands différents. Sélectionner les scénarios non nuls sur les mêmes sorties introduit en outre une sélection.
- **L’audit des seuls désaccords manque les erreurs partagées.** Parseur et juge peuvent tous deux confondre commande affichée, tentative et effet exécuté.

### (b) Conditions de perte de puissance ou de non-identification

**HYPOTHÈSES — modèles probabilistes.**

Pour une greffe \(T\), le contraste estimé est
\[
\Delta_T=E[Y\mid do(T=t_c)]-E[Y\mid do(T=t_s)].
\]
Si \(T=(R,F,Q)\) et que seuls \((r_c,f_c,q_c)\) et \((r_s,f_s,q_s)\) sont observés, les effets séparés de \(R,F,Q\) sont non identifiables sans restrictions supplémentaires. Si \(P(T=t\mid X,m)=0\), l’effet de greffe ne permet pas d’estimer directement l’effet médié sur le support naturel.

Pour une trace déclarative \(V\) et un état latent \(U\), le modèle
\[
P(Y,V\mid X)=\int P(Y\mid U,X)P(V\mid U,X)\,dP(U\mid X)
\]
autorise \(\operatorname{Cov}(Y,V\mid X)\ne0\) sans effet causal de \(V\) sur \(Y\).

Pour le modèle logistique
\[
p_{mc}=\sigma(\alpha_m+\beta_mc),
\qquad
\frac{\partial p_{mc}}{\partial c}=\beta_mp_{mc}(1-p_{mc}),
\]
des \(\beta_m\) égaux donnent des effets absolus différents. L’information sur \(\beta_m\) diminue lorsque les \(p_{mc}(1-p_{mc})\) diminuent ; une séparation complète empêche l’existence d’un estimateur du maximum de vraisemblance fini.

Si \(K_s\sim\operatorname{Bin}(n,p_s)\),
\[
E[K_s/n\mid K_s>0]
=\frac{p_s}{1-(1-p_s)^n}>p_s.
\]

Pour des activations \(H\) de covariance \(\Sigma\), la variance du score est \(v^\top\Sigma v\). Le cosinus euclidien entre \(v\) et \(w\) ne détermine ni
\[
\frac{v^\top\Sigma w}{\sqrt{v^\top\Sigma v\,w^\top\Sigma w}}
\]
ni \(P(Y\mid do(H\leftarrow H-vv^\top H))\).

Enfin, un audit conditionné par \(J\ne P\) n’identifie pas
\[
P(J=P\ne Y),
\]
où \(P\) désigne le verdict du parseur.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE — exigences proposées.**

- **Justification :** autorisation croisée avec audit, au lieu d’un changement conjoint.
- **Greffe :** traces d’une même source, avec édition minimale de prémisse pertinente contre édition non pertinente ; contrôle des indices d’action.
- **Artificialité :** nouvelles familles de scénarios, exclues de toute construction et sélection de direction.
- **Audit :** échantillon aléatoire des accords, comprenant commandes citées mais non exécutées.
- **Transport :** sondes à étiquettes permutées, sélectionnées selon exactement la même procédure.

**HYPOTHÈSE — correction du duel :** opposer un effet de l’édition pertinente, corrigé de l’édition témoin, supérieur au seuil à son complément. Une issue nulle réfute cette sensibilité opérationnelle, pas toute utilisation de raisons.

## Sur la proposition D

### (a) Défauts de méthode

**VÉRIFIÉ — lecture de D ; HYPOTHÈSES — objections.**

- **Le premier duel ne sépare pas nécessairement les mécanismes.** Un classifieur sémantique peut exploiter consentement, finalité et contexte exactement comme le ferait un modèle utilisant des raisons. « Contenu » doit recevoir une restriction testable supplémentaire.
- **Nécessité et seuil ne coïncident pas.** Une nécessité « pour une partie du gain », sans minimum d’effet, n’est pas réfutée par une équivalence dans une marge non nulle.
- **Le gain sous corruption exige une référence définie.** Si la référence reçoit aussi les traces, la perte de gain soustrait son propre effet de greffe. Elle peut être nulle alors que les deux modèles changent fortement.
- **La restauration ne garantit pas la spécificité.** Restaurer le préfixe original rétablit simultanément cohérence, familiarité et contenu. Cela contrôle la réversibilité, pas l’exclusivité du mécanisme.
- **Apparier en dégât peut sélectionner les témoins.** Choisir les directions témoins selon leur dégât observé sur les mêmes épisodes crée une sélection sur une variable post-intervention.
- **Le banc n’autorise pas un taux de détection général sans population définie.** Un organisme valide localement la sensibilité de l’intervention ; il ne fournit pas sa sensibilité sur tous les mécanismes conditionnels.
- **Exiger une interaction avec les phrases est trop fort.** Si ces phrases ne déplacent pas l’état causal pertinent, une contribution du regard peut exister sans interaction avec elles.

### (b) Conditions de perte de puissance ou de non-identification

**HYPOTHÈSES — modèles probabilistes.**

Avec \(c\) la corruption et \(i\) la condition intacte,
\[
L=(p_{bi}-p_{mi})-(p_{bc}-p_{mc})
=(p_{mc}-p_{mi})-(p_{bc}-p_{bi}).
\]
Si \(p_{mc}-p_{mi}=p_{bc}-p_{bi}\ne0\), alors \(L=0\).

Pour une marge \(\varepsilon>0\), l’hypothèse \(L>0\) contient des lois arbitrairement proches de \(L=0\). Une conclusion \(|L|<\varepsilon\) ne réfute donc pas \(L>0\). Un duel opérationnel exclusif est \(L>\varepsilon\) contre \(L\le\varepsilon\), avec décision suspendue si l’intervalle rencontre les deux régions.

Soient \(\widehat d_k=d_k+e_k\), \(\widehat\tau_k=\tau_k+u_k\), et
\[
K=\{k:|\widehat d_k-d^\star|\le h\}.
\]
Si \(\operatorname{Cov}(e_k,u_k)\ne0\), alors \(E[u_k\mid k\in K]\) peut être non nul.

Pour une population d’organismes \(M\sim Q\), la sensibilité est
\[
\eta_Q=P_{M\sim Q}(\Delta_M>\varepsilon).
\]
Sans \(Q\) défini ni échantillonnage selon \(Q\), un \(\Delta_M\) ponctuel n’identifie pas \(\eta_Q\).

Avec \(Z\) la phrase et \(W\) l’état latent,
\[
P(W\mid Z=1)=P(W\mid Z=0),\quad
P(Y\mid do(W=1))\ne P(Y\mid do(W=0))
\]
est compatible avec une interaction ablation–phrase nulle.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE — exigences proposées.**

- **Traces :** corruption aussi plausible et grammaticalement valide, mais concernant une justification non applicable.
- **Gain :** référence intacte et référence greffée rapportées séparément ; effets intra-adaptateur avant leur différence.
- **Directions :** appariement du dégât sur un jeu indépendant, puis gel des directions avant test.
- **Banc :** organisme non conditionnel soumis aux mêmes interventions et évaluations.
- **Paires sémantiques :** marqueurs normatifs présents mais causalement non pertinents.

**HYPOTHÈSE — conséquence éditoriale :** la thèse doit distinguer effet des recettes, sensibilité au contenu fourni à l’inférence et médiation par les raisons apprises. Les tests proposés peuvent établir les deux premiers sans identifier le troisième ; cet écart doit rester visible dans la figure principale et la conclusion.

FIN-DE-CELLULE
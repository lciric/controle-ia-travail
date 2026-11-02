# Proposition E — Critique croisée de méthode

**Pièces absentes ou partielles :** synthèse N12–N13, PDF Avalon, CL13–CL14 et durcissement v50 non servis ; pièces documentaires en extraits et passages explicitement retirés, sans reconstruction ici.

**Convention de statut.** **RAPPORTÉ** désigne ci-dessous ce qu’affirme une proposition, sans validation par E. **VÉRIFIÉ** porte uniquement sur le contenu documentaire explicitement servi, jamais sur une exécution réelle. Mes objections, modèles probabilistes et contrôles proposés sont des **HYPOTHÈSES** méthodologiques. Toute valeur numérique proposée pour un protocole serait **illustrative** ; les constantes dans les identités mathématiques ne sont pas des mesures.

Dans chaque sous-section **(b)**, je donne uniquement des variables, lois, paramètres, estimateurs et conditions probabilistes. Les implications portent sur ces modèles, non sur un résultat observé.

## Sur la proposition A

### (a) Défauts de méthode — **HYPOTHÈSE**

**Reproductibilité substituée à la correction.** A affirme que le rejeu indépendant rend la validité vérifiable. Pourtant, une erreur déterministe peut reproduire exactement sa sortie et ses fichiers. E1 teste une invariance entre environnements, pas la conformité du calcul au préenregistrement. Son résultat ne suffit donc pas à écarter l’attestation ni un oracle scientifique indépendant.

**Hypothèses non complémentaires.** E1 oppose reproduction exacte et divergence des honnêtes, mais accepte un seuil inférieur à l’égalité complète pour les fichiers. E2 laisse notamment hors duel : amélioration réelle, hausse des verdicts sans baisse de reproductibilité, ou baisse de reproductibilité sans hausse des verdicts. E5 laisse hors duel des anomalies de traces étrangères au dossier partagé. Les conclusions annoncées débordent les alternatives effectivement testées.

**Confusions causales dans E2.** Retirer le matériau change aussi l’information scientifique disponible. Une différence entre bras peut venir d’un meilleur apprentissage de la tâche, de changements de difficulté des fiches, ou de compositions différentes des générations. Les générations d’une même lignée ne sont pas des répétitions indépendantes. Le seuil fondé sur quelques bras témoins ne définit ni test séquentiel ni risque cumulé.

**Sélection dans E4.** Restreindre l’étude aux scripts déjà reproductibles sélectionne sur une conséquence des propriétés du script et de l’environnement. La concordance obtenue ne représente plus tous les scripts soumis. Des contrôles choisis parce qu’ils dépendent de l’implémentation rendent en outre leur divergence partiellement vraie par construction. Ils ne mesurent pas le taux d’erreurs communes.

**Calibration réutilisée comme validation.** Retirer ou déplacer les canaris qui alertent sur le corpus honnête, puis invoquer ce même corpus pour justifier l’élimination automatique, sous-estime les fausses alertes.

**Canal et journal.** Le nombre d’étiquettes ne borne pas toute la transcription visible. « Expliquer une divergence » nécessite une règle d’attribution indépendante ; une annotation rétrospective peut transformer toute différence en explication. Enfin, un journal minimal peut varier sans anomalie.

### (b) Conditions probabilistes de perte de puissance ou de non-identifiabilité — **HYPOTHÈSE : modèles**

Soient \(R\) la reproduction, \(Y\) la correction, \(C\) une alerte, \(D\) un désaccord, \(J\) une anomalie de journal.

- **E1, empreintes et reconstruction :**
  \[
  \mathcal L(R\mid Y=0)=\mathcal L(R\mid Y=1)
  \Rightarrow I(R;Y)=0.
  \]
  Sous \(R=1\) presque sûrement et \(P(Y=0)>0\), l’estimateur \(\hat P(R=1)\) ne borne pas \(P(Y=0)\).

- **E2 :** pour un estimateur \(\hat\delta\) d’effet entre bras,
  \[
  \operatorname{Var}(\hat\delta)
  =\sum_i w_i^2\operatorname{Var}(X_i)
   +2\sum_{i<j}w_iw_j\operatorname{Cov}(X_i,X_j).
  \]
  Si \(|\delta|/\sqrt{\operatorname{Var}(\hat\delta)}\to0\), la puissance tend vers le niveau du test. Si
  \[
  P(Z=z\mid X=x)=0
  \]
  sur une région de probabilité positive, le contraste causal moyen n’est pas identifiable sans restrictions supplémentaires.

- **E3 :** pour \(K\sim\mathrm{Bin}(n,p)\), \(K=0\) donne une borne supérieure unilatérale
  \[
  p_U=1-\alpha^{1/n},
  \]
  non \(p=0\). Si \(\hat t=\arg\min_t\hat p_{\mathrm{FA}}(t)\), généralement
  \[
  E[\hat p_{\mathrm{FA}}(\hat t)]\le E[p_{\mathrm{FA}}(\hat t)].
  \]

- **E4 :**
  \[
  P(D=1\mid Y=0,R=1)=P(D=1\mid Y=1,R=1)
  \]
  implique une puissance discriminante nulle dans la strate sélectionnée. Cette égalité ne détermine pas les lois conditionnelles à \(R=0\).

- **E5 :** si \(O\) indique une trace observée et
  \[
  P(O=1\mid J,Y)\ne P(O=1),
  \]
  \(\hat P(J=1\mid O=1)\) n’identifie pas \(P(J=1)\). Si
  \[
  I(Y;J\mid R)=0,
  \]
  le gain prédictif conditionnel du journal est nul.

- **Canal, audit tiers, coût :**
  \[
  I(S;T\mid V)>0
  \]
  reste compatible avec \(H(V)\) faible. Pour deux erreurs \(E_1,E_2\),
  \[
  P(E_1=1,E_2=1)=p_1p_2+\operatorname{Cov}(E_1,E_2).
  \]
  Pour \(K=cN+L\), \(E[K]=cE[N]+E[L]\) ; sans loi de \(L\), les quantiles de \(K\) ne sont pas identifiés.

### (c) Contrôles négatifs dont l’absence serait fatale — **HYPOTHÈSE**

- **Pour la prétention sémantique d’E1 :** artefacts incorrects mais déterministes, avec vérité externe gelée. Leur acceptation invaliderait « reproduction implique validité ».
- **Pour E2 :** matériau placebo de même forme et volume, indépendant de la fiche ; randomisation par lignées, non seulement par fiches.
- **Pour E3 :** corpus honnête final inaccessible pendant le placement des canaris ; opérations ordinaires représentatives, pas seulement absence d’exécution.
- **Pour E4 :** cas incorrects donnant la même sortie dans les deux environnements ; duplication du même environnement avec budget identique.
- **Pour E5 :** variation bénigne de trace sans changement de calcul ; annotation en aveugle des causes supposées.

Le contrôle aléatoire proposé par A n’est pertinent que si l’aléa influence effectivement les objets comparés.

## Sur la proposition B

### (a) Défauts de méthode — **HYPOTHÈSE**

**E1 confond erreur statistique et rupture de vérification.** Une hypothèse nulle peut franchir honnêtement un seuil statistique. « Au moins une fiche passe » ne démontre donc ni fabrication du résultat ni circularité. Inversement, aucun passage ne réfute pas l’existence d’un artefact incorrect acceptable. Le témoin à effet réel est un contrôle **positif**, dont la réussite dépend de la taille d’échantillon et de la puissance, pas seulement de l’effet annoncé.

**E2 ne teste pas l’optimisation.** Une classification production/test peut utiliser des différences bénignes. Sa réussite ne signifie pas que « tout le reste est compromis » ; son échec ne démontre pas l’opacité pour d’autres observateurs. Une partition aléatoire d’exécutions issues des mêmes machines peut laisser le classificateur reconnaître une machine, une période ou un lot.

**La précision ne borne pas l’information.** Un classificateur faible peut rester proche du hasard malgré des variables informatives. Les deux seuils proposés laissent en outre une zone non tranchée : les deux issues annoncées ne couvrent pas les observations possibles.

**E3 et E4 : étiquettes définies par les instruments.** Un corpus « adversariel » sélectionné pour lire des différences d’environnement favorise artificiellement le désaccord. Les canaris ne peuvent être évalués contre « le sondage » sans définition indépendante de cette classe. Comparer leur détection des lectures au blocage natif des écritures ne compare pas la même propriété.

**Assertions empiriques sans support.** B attribue déjà à la v48 des performances chiffrées de vérification. **VÉRIFIÉ documentairement :** la pièce 1 décrit des exécuteurs factices et aucune exécution réelle de `bwrap`. Ces seuils ne sont donc pas des résultats disponibles. De même, des poids de modèle fixes ne rendent pas à eux seuls son raisonnement auditable.

### (b) Conditions probabilistes — **HYPOTHÈSE : modèles**

- **E1 :** sous des tests indépendants de niveau \(\alpha\),
  \[
  K\sim\mathrm{Bin}(n,\alpha),\qquad P(K>0)=1-(1-\alpha)^n.
  \]
  Sous \(p=\alpha+\eta\), la séparation devient faible lorsque
  \[
  \frac{\eta\sqrt n}{\sqrt{\alpha(1-\alpha)}}\to0.
  \]
  Pour toute alternative \(p>0\), \(P_p(K=0)=(1-p)^n>0\).

- **E2 :** avec classes équiprobables et lois \(P_0,P_1\),
  \[
  a^\star=\frac{1+\operatorname{TV}(P_0,P_1)}2,\qquad a_f\le a^\star.
  \]
  \(a_f\approx1/2\) n’implique ni \(\operatorname{TV}(P_0,P_1)\approx0\), ni \(I(X;Z)\approx0\).
  Si \(Z=U\) presque sûrement dans l’échantillon et \(Z\perp U\) dans la population cible, \(\hat a_f\) ne mesure pas \(a_f^{\mathrm{cible}}\).

- **E3 :**
  \[
  D\mid Y=y\sim\mathrm{Bern}(d_y).
  \]
  Si \(d_0=d_1\), tout seuil sur \(D\) a une puissance égale à son niveau. Avec probabilités marginales d’erreur \(p_1,p_2\),
  \[
  \max(0,p_1+p_2-1)\le P(E_1E_2=1)\le\min(p_1,p_2).
  \]

- **E4, canaris et classificateurs de défauts :** pour prévalence \(\pi\), sensibilité \(s\), fausses alertes \(f\),
  \[
  P(Y=1\mid C=1)=\frac{\pi s}{\pi s+(1-\pi)f}.
  \]
  Si \(\pi\to0\) et \(f>0\), cette probabilité tend vers zéro.

- **Empreintes et attestation :**
  \[
  \mathcal L(T\mid Y=0)=\mathcal L(T\mid Y=1)
  \Rightarrow
  \sup_\phi\left|E[\phi(T)\mid Y=0]-E[\phi(T)\mid Y=1]\right|=0.
  \]

- **Couverture et devis :**
  \[
  s_{\mathrm{cible}}=\sum_j w_js_j.
  \]
  Si \(w_j>0\) et \(n_j=0\), \(s_j\) n’est pas estimable dans cette strate. Pour durées \(T_i\), un devis fondé sur \(E[T_i]\) seul ne détermine pas \(P(\sum_iT_i>B)\).

### (c) Contrôles négatifs fatals — **HYPOTHÈSE**

- **E1 :** calcul statistique de référence correct sur données nulles, comparé au résultat déclaré, et non seulement au franchissement du seuil.
- **E2 :** étiquettes permutées ; validation sur machines et périodes entièrement tenues à l’écart ; mêmes distributions de charges dans les classes.
- **E3 :** erreurs sémantiques communes aux deux environnements et différences bénignes sans erreur scientifique.
- **E4 :** scripts honnêtes variés, étiquetés sans consulter les alertes.
- **Vérificateur :** paquet cohérent quant aux empreintes mais incorrect selon un oracle indépendant. Les simples altérations d’octets ne suffisent pas.
- **Journal :** exécution honnête comportant les variations légitimes que le détecteur prétend distinguer des substitutions.

## Sur la proposition C

### (a) Défauts de méthode — **HYPOTHÈSE**

**Architecture projetée présentée comme acquise.** C traite la séparation distante et `ExecuteurDistantParLots` comme opérationnels. **VÉRIFIÉ documentairement :** le devis dit que cet exécuteur manque. Il ne faut donc pas compter cette séparation comme une protection déjà éprouvée.

**Permutation assimilée à oracle universel.** La contre-épreuve exige l’échangeabilité pertinente sous l’hypothèse nulle. Une permutation arbitraire peut détruire des dépendances légitimes ; certaines statistiques honnêtes sont invariantes à la permutation choisie. Un franchissement sur une tranche permutée peut aussi être une erreur statistique nominale, non une fraude. Ne tester que les survivants change la population et impose une calibration conditionnelle à cette sélection.

**Accès assimilé à usage.** Lire les fichiers, même intégralement, n’établit pas leur influence sur le résultat. À l’inverse, exiger toutes les lectures peut rejeter une analyse correcte utilisant une partie déclarée suffisante. La cible « lecture complète » varie d’ailleurs entre les sections de C.

**Zéro fausse alerte par soustraction d’une trace initiale.** Soustraire les accès de démarrage ne couvre pas tous les comportements légitimes des bibliothèques. Cela peut également retirer des événements informatifs. Réutiliser les mêmes imports pour la liste blanche et son évaluation donne une réussite par construction.

**E3 ne mesure pas sa propre hypothèse.** Le critère final porte sur accord et durée ; il omet la propriété de blocage incluse dans \(H_A\). Une concordance rapide ne falsifie donc pas toutes les alternatives annoncées. Le même hôte conserve aussi des dépendances communes.

**Devis incomplet.** **VÉRIFIÉ documentairement :** le pire cas de production servi comporte 36 heures d’exécution. L’ajout de quatre heures annoncé par C ne borne pas un doublement de ce pire cas. Le développement gratuit et l’absorption intégrale par le plafond ne sont pas établis.

### (b) Conditions probabilistes — **HYPOTHÈSE : modèles**

- **Permutation :** pour groupe \(G\), la condition
  \[
  \mathcal L(X)=\mathcal L(gX)\quad\forall g\in G
  \]
  sous \(H_0\) est requise pour l’invariance correspondante. Si elle échoue,
  \[
  P_{H_0}(p_{\mathrm{perm}}\le\alpha)\le\alpha
  \]
  n’est pas garanti.

- **Sélection des survivants :** avec \(S=\mathbf1\{T(X)>t\}\),
  \[
  q=P(T(gX)>t\mid S=1,Y=\text{honnête})
  \]
  n’est généralement pas égal à \(P(T(gX)>t)\). Si \(q\) dépasse le taux de rejet admissible, le portail échoue même avec calcul exact.

- **Sensibilité à la transformation :**
  \[
  T(gX)=T(X)\ \text{p.s.}\mid Y=\text{honnête}
  \]
  rend le rejet pour invariance systématique dans cette strate. Inversement,
  \[
  \mathcal L(T(X),T(gX)\mid Y=0)
  =
  \mathcal L(T(X),T(gX)\mid Y=1)
  \]
  supprime toute discrimination par cette paire.

- **Accès et canaris :**
  \[
  P(A=1\mid Y=0)=P(A=1\mid Y=1)=1
  \Rightarrow I(A;Y)=0.
  \]
  Avec classes de charges \(j\),
  \[
  f_{\mathrm{cible}}=\sum_j w_jf_j;
  \quad \hat f_j=0\ \text{pour les seuls }j\text{ observés}
  \]
  ne borne pas les \(f_j\) non observés.

- **Concordance :** pour \(\Delta=R_1-R_2\),
  \[
  P(|\Delta|\le\varepsilon)
  \]
  ne borne pas \(P(Y=0)\). Sous \(R_1=R_2\ne R^\star\) presque sûrement, la concordance est complète.

- **Coût et plafonds :**
  \[
  E[T\mid T\le\tau]\ne E[T],\qquad
  P(T_{\mathrm{double}}>B)=P(T>B/2)
  \]
  lorsque \(T_{\mathrm{double}}=2T\). Sans loi des reprises, le quantile du coût total n’est pas identifié.

### (c) Contrôles négatifs fatals — **HYPOTHÈSE**

- Analyses honnêtes sur données dépendantes et statistiques légitimement invariantes à la transformation.
- Analyses honnêtes sur données nulles, afin de mesurer le rejet nominal puis le rejet conditionnel à la sélection.
- Référence indépendante de la statistique attendue, tenue hors de la construction des scripts.
- Lecture effective sans influence sur le résultat, comme contrôle négatif de la prétention « accès prouve usage ».
- Charges honnêtes nouvelles après gel de la liste blanche.
- Désaccord numérique bénin et erreur commune parfaitement concordante.
- Mesure de durées incluant interruptions, traces manquantes et reprises, plutôt que seules exécutions terminées.

## Sur la proposition D

### (a) Défauts de méthode — **HYPOTHÈSE**

**Banque finie : décision exacte, portée étroite.** D borne explicitement ses conclusions à une banque gelée : c’est méthodologiquement distinct d’une garantie générale. Mais plusieurs duels deviennent des vérifications exhaustives d’un tableau fini plutôt que des inférences sur une population. Le passage au déploiement exige une loi d’échantillonnage et des strates.

**E2 : alternative incomplète.** \(H_A\) porte sur le rejet des ruptures ; \(H_B\) sur l’acceptation d’une rupture. Pourtant, un rejet honnête est annoncé comme falsifiant \(H_A\). Il faut inclure explicitement la spécificité dans \(H_A\), puis prendre son complément pour \(H_B\).

**E3 : normalisation susceptible d’effacer la cible.** Comparer seulement les transcriptions normalisées peut cacher l’information contenue dans les champs supprimés. Une différence de traces n’est pas nécessairement une information sur une variable protégée ; l’absence de différence sur une banque n’établit pas l’égalité des lois.

**E4 : meilleur comparateur sélectionné après observation.** Choisir le « meilleur bac seul » sur la banque finale biaise le gain incrémental. Compter une divergence supplémentaire sans vérité externe peut récompenser une anomalie bénigne. Un coût par détection supplémentaire devient instable lorsque le dénominateur est petit.

**E6 : couverture auto-déclarée.** Permettre de classer une ablation « hors couverture » après son passage au vert rend \(H_A\) difficilement réfutable. La carte de couverture doit être gelée indépendamment avant les résultats.

**E7 : indépendance non démontrée.** Des outils propres et la détection de paquets incohérents ne prouvent pas l’absence de défaillance commune. La capture préalable améliore le lien documentaire, mais reste conditionnelle au fait que l’exécuteur consomme effectivement la capture.

### (b) Conditions probabilistes — **HYPOTHÈSE : modèles**

- **E1, E2, E5–E7 :** pour banque fixe \(B\),
  \[
  \hat p_B=|B|^{-1}\sum_{x\in B}\mathbf1\{\text{échec}(x)\}
  \]
  n’identifie pas \(p_P=E_P[\mathbf1\{\text{échec}(X)\}]\) sans relation entre \(B\) et \(P\). Sous échantillonnage indépendant, zéro échec donne encore \(p_U=1-\alpha^{1/n}\).

- **E3 :**
  \[
  I(S;g(T)\mid V)=0
  \]
  n’implique pas \(I(S;T\mid V)=0\). Pour deux lois \(P,Q\), toute règle \(\phi\) satisfait
  \[
  |E_P\phi-E_Q\phi|\le\operatorname{TV}(P,Q).
  \]

- **E4 :**
  \[
  \Delta=P(D_2=1,D_1=0\mid Y=1).
  \]
  Si \(n\Delta\ll1\), \(P(\hat\Delta=0)=(1-\Delta)^n\) est élevé sous indépendance. Pour \(Q=K/\hat\Delta\), \(\hat\Delta=0\) rend \(Q\) non défini.

- **E6 :** si \(C\) indique « couvert »,
  \[
  P(D=1\mid C=1)
  \]
  n’identifie pas \(P(D=1)\). Sous \(C=D\), cette probabilité conditionnelle vaut un sans renseigner \(P(D=0)\).

- **E7 :**
  \[
  P(E_1=1,E_2=1)
  \]
  n’est pas identifié par \(P(A_1=A_2)\) seul. Si \(E_1=E_2\) presque sûrement, l’accord peut être complet avec taux d’erreur positif.

### (c) Contrôles négatifs fatals — **HYPOTHÈSE**

- Banque finale tenue à l’écart, avec règles de validité et de couverture gelées avant exécution.
- Variations honnêtes du paquet et de la capture, pour tester la spécificité d’E2.
- Transcriptions brutes conservées pour l’évaluation, plus étiquettes permutées et répétitions indépendantes pour E3.
- Comparateur unique choisi avant la banque finale et erreurs communes aux deux bacs pour E4.
- Configuration intacte et ablations préclassées hors couverture pour E6 : ces dernières ne doivent jamais être comptées comme détections.
- Paquets concordants mais incorrects selon une référence indépendante pour E7.

**Exigence B4 appliquée à D — HYPOTHÈSE :** chaque duel doit porter soit sur une propriété exactement décidable de la banque exhaustive, soit sur des paramètres probabilistes avec niveau d’erreur et puissance préenregistrés. Dans le second cas, une estimation imprécise reste **non jugeable** : elle ne peut être forcée dans l’une des deux issues falsifiantes.

FIN-DE-CELLULE
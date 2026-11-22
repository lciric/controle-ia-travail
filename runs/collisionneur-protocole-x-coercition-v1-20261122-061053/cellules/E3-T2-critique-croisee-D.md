# Proposition D — Critique croisée de méthode

**Statuts et notation.** Les plans auxquels renvoient les sigles D1, E1, etc. sont **RAPPORTÉS** par leurs auteurs ; je n’en reprends aucun résultat empirique. Les objections causales de (a) et les exigences de contrôle de (c) ont le statut **HYPOTHÈSE**. Les relations de (b) ont le statut **VÉRIFIÉ** comme implications mathématiques *sous les lois indiquées*, non comme descriptions des modèles. Tout seuil ou effectif numérique discuté est **illustratif**. \(Y\) désigne la violation selon l’oracle externe, \(A\) l’alerte effectivement enregistrée, \(S\) le score avant seuillage, \(Z\) le bras assigné et \(X\) la tâche. Une omission observée, \(Y=1,A=0\), n’est pas en elle-même une omission *induite*.

## Sur la proposition A

### (a) Défauts de méthode — HYPOTHÈSE

- **D1.** Titrer la demande pour éviter le plafond est utile, mais le faire sur les tâches du test sélectionne celles où un contraste est possible. Même sur lot indépendant, la conclusion porte sur les demandes ainsi titrées. Une équivalence avec le placebo ne démontre ni l’identité des mécanismes ni le transfert des défenses. Un levier seul peut contenir une demande implicite : son effet n’établirait pas davantage une simple distraction.
- **D2.** Une AUROC stable ne caractérise pas une translation des scores. Inversement, une baisse d’aire n’exclut pas qu’un recalibrage suffise au point d’exploitation choisi. Étalonner et juger le seuil sur les mêmes canaris rendrait la restauration du taux de fausses alertes partiellement vraie par construction.
- **D3 et D3b.** Un angle mort propre à chaque famille *prédit justement* une interaction auteur–moniteur si les auteurs produisent des erreurs de difficultés différentes. L’en-tête randomisé identifie l’effet d’une attribution, pas une entente. Pour la coordination sous consigne, le hasard pertinent tient compte des préférences marginales des deux modèles devant **la même tâche**.
- **D4 et D5.** Les premiers jetons générés peuvent annoncer l’action ; battre un sac-de-mots n’isole pas une « bascule ». La consigne système du bras de transfert peut, elle aussi, porter l’étiquette. Dans D5, l’ensemble encore exposé change après chaque événement : une baisse du risque parmi les survivants ne suffit pas à établir une immunisation.

### (b) Conditions de perte de puissance ou d’identification — VÉRIFIÉ

| Critère | Condition sur la loi ou l’estimateur |
|---|---|
| D1, démarcation interventionnelle | Si \(\sum_x P(x)\Delta(x)=0\) avec \(\operatorname{Var}_X\Delta(X)>0\), le contraste marginal est nul malgré l’hétérogénéité. Si deux mécanismes donnent la même famille \(\{P(Y,A\mid do(Z=z))\}_z\) sur les interventions testées, tout test a la même loi sous les deux. |
| D2, deux sens de pression | Deux ROC peuvent avoir la même intégrale et des ordonnées différentes au FPR cible \(q\). Une transformation strictement croissante commune aux classes conserve toute la ROC sans être une translation. Le rapport des déplacements silence/alerte est indéfini si son dénominateur est nul. |
| D3, D3b | Même si les choix \(U,V\) sont indépendants conditionnellement à \(X\), \(P(U=V)=E_X\sum_u P(U=u\mid X)P(V=u\mid X)\), pas nécessairement le produit scalaire des marginales globales. Si la loi des traces diffère par auteur sans support commun à difficulté fixée, le contraste d’origine à difficulté fixée n’est pas identifiable. |
| D4 | Si \(P(Y=y\mid Z=z)=0\) pour une classe, l’AUROC intra-bras est indéfinie. Si \(P(Y\mid S_{\rm sonde},T)=P(Y\mid T)\) pour \(T\) le préfixe textuel, un gain sur un estimateur lexical sous-ajusté reste compatible avec zéro information additionnelle au-delà de \(T\). |
| D5 | Pour un risque individuel constant \(p_X\), la survie marginale est \(E[(1-p_X)^k]\), distincte de \((1-E[p_X])^k\) dès que \(k>1\) et \(\operatorname{Var}(p_X)>0\). Une pente linéaire nulle n’exclut pas une dépendance non monotone à \(k\). |
| Instruments et oracle | Pour \(n_0\) négatifs indépendants, \(P(\text{aucun faux positif})=(1-q)^{n_0}\). Si la référence mécanique reproduit \(Y\) exactement, son rappel vaut déjà l’unité à FPR nul. Si seuls les dossiers sélectionnés \(R=1\) sont vérifiés et \(P(R=1\mid X=x)=0\) sur une strate, le rappel global n’est pas identifiable sans hypothèse supplémentaire. |

### (c) Contrôles négatifs indispensables — HYPOTHÈSE

Geler demande, seuils, couche et références sur des **familles de tâches disjointes** du test. Pour D2, rejouer une même trace inchangée avec pression adressée à un tiers absent. Pour D3b, permuter les partenaires *à tâche et consigne fixées*. Pour D4, comparer à un lecteur du même préfixe, au même instant, et permuter les issues entre graines d’une même invite. Pour D5, assigner des historiques placebo et répétés au même stade de tâche, avec la même possibilité matérielle de violation. Sans ces contrôles, je retiendrais des contrastes de performance, pas les mécanismes annoncés.

## Sur la proposition B

### (a) Défauts de méthode — HYPOTHÈSE

- **E1–E2.** Une pente de « dose » suppose une intensité ordonnée autrement que par l’effet obtenu. Le plan fractionnaire doit annoncer quelles interactions sont confondues. Un transfert médiocre d’un ajustement entraîné sur la seule demande nue peut révéler une spécialisation à son gabarit, plutôt qu’une classe distincte. Une zone entre marges de décision peut contenir le vrai paramètre : ce n’est pas nécessairement un échec de puissance.
- **E3.** Modifier le contexte de l’agent peut changer *quels épisodes* aboutissent à une violation, pas seulement leur score. Une baisse de score aussi chez les honnêtes est compatible avec une translation commune et une discrimination intacte. Toute sélection de variantes sur la sonde évaluée doit être distinguée d’un test de généralisation à des traces indépendantes.
- **E4–E5.** La reconnaissabilité mesurée sur productions honnêtes ne détermine pas celle des traces en infraction. La paraphrase peut changer la visibilité de la faute à acte inchangé. Il faut coder séparément **origine réelle** et **texte affiché**, puis en dériver la véracité : « même origine » et « revendication vraie de même origine » ne sont pas deux traitements indépendants.
- **E6.** Même un excellent accord avec l’oracle dans son domaine ne valide pas le juge sur les tâches *exclues* faute d’oracle. L’invariance du score à la pression n’est pas non plus nécessaire à son utilité à seuil recalibré.

### (b) Conditions de perte de puissance ou d’identification — VÉRIFIÉ

- **E1–E2.** Si la matrice du plan \(M\) a un noyau non trivial, \(M\beta=M(\beta+v)\) pour \(v\in\ker M\). Pour \(r_j=1-p_{j,\mathrm{déf}}/p_{j,\mathrm{nu}}\), \(R=r_{\mathrm{social}}/r_{\mathrm{injection}}\) est indéfini si un taux nu est nul ou si \(r_{\mathrm{injection}}=0\). Un intervalle du dénominateur contenant zéro ne justifie pas un intervalle de rapport étroit obtenu par linéarisation.
- **E3, sonde et juge.** \(P(S\mid Y,Z)=\sum_xP(S\mid x,Y,Z)P(x\mid Y,Z)\) peut varier avec \(Z\) alors que chaque première loi est invariante. Si \(S_Z=S_0+c_Z\) dans les deux classes, l’AUROC comportementale est inchangée même si le bras est prédictible par le score. Un multiplicateur de FPR est indéfini à FPR initial nul.
- **E4–E5.** Une cellule origine–texte de probabilité nulle empêche d’estimer son interaction sans extrapolation. Si les effets de revendication sont tous deux nuls, leur différence est nulle : l’équivalence entre origines n’établit aucun effet de contenu.
- **E6.** Pour prévalence \(\pi=P(Y=1)\) et fréquence d’alerte \(a\), \(\kappa=(p_o-p_e)/(1-p_e)\), \(p_e=\pi a+(1-\pi)(1-a)\). À sensibilité et spécificité constantes, \(\kappa\) peut varier avec \(\pi\) ; il est indéfini pour \(p_e=1\).
- **Cascade, budget et dommage.** Pour \(b\) dossiers et \(J_i=\mathbf1\{Y_i=1,A_i=0\}\), la sécurité de lot est \(P(\sum_iJ_i=0)\), non déterminée par les seules marginales \(P(J_i=1)\). Pour l’audit, si le coût \(C\) varie, \(E[R]\) fixé ne fixe pas \(E[RC]\).

### (c) Contrôles négatifs indispensables — HYPOTHÈSE

Pour E2, tester aussi des reformulations **non sociales** inédites, et des demandes légitimes : un ajustement aléatoire ne contrôle pas la spécialisation au gabarit. Pour E3, rejouer des traces figées et réserver un lot sans sélection de variantes. Pour E4–E5, permuter les attributions sur le même texte, avec en-tête absent et réécriture dans le style d’origine. Pour E6, comparer deux lectures placebo de la même trace à prévalence fixée. Pour la cascade, inclure un audit aléatoire de même **coût**, avec oracle externe aussi sur les non-signalés.

## Sur la proposition C

### (a) Défauts de méthode — HYPOTHÈSE

- **Duel rhétorique.** Le bras nommé « surcharge neutre » dans l’hypothèse est remplacé dans le plan par un discours social sans demande. Maximiser sur les formulations, puis traiter les gagnantes comme une paire choisie d’avance, invaliderait l’inférence appariée. Un effet protecteur serait un effet causal, et non un argument de réductibilité.
- **Duel d’origine.** Égaliser la perplexité moyenne ne rend pas les traces interchangeables. Faire réécrire par la famille du moniteur introduit cette famille dans la construction même du stimulus. À trace identique, l’effet de l’étiquette mesure bien une réponse à l’étiquette ; aucune action coordonnée de l’auteur n’est nécessaire.
- **Duel de fausses alertes.** Le bras social contient aussi une demande explicite d’alerter. L’absence de termes dans un dictionnaire technique ne neutralise ni cette demande ni le vocabulaire de suspicion. **Duel de sonde.** Lire les jetons de l’appel déjà émis permet d’identifier l’acte, pas forcément de l’anticiper ; étalonner sur les résistances retenues pour tester le FPR rendrait ce dernier circulaire.
- **Dommage.** Restreindre les négatifs aux tâches réussies exclut les erreurs ordinaires qui risquent précisément de déclencher une interruption. Un oracle d’état ne transforme pas une omission observée en corruption intentionnelle.

### (b) Conditions de perte de puissance ou d’identification — VÉRIFIÉ

- **Rhétorique.** Pour une paire binaire, seuls les discordants de probabilités \(p_{01},p_{10}\) contribuent au contraste. Si \(n(p_{01}+p_{10})\) est faible, le test exact est discret ; si plusieurs taux sont égaux, \(E[\max_j\hat p_j]\ge\max_jp_j\), des deux côtés du contraste, sans annulation garantie des biais.
- **Origine.** \(E[L\mid O=i]=E[L\mid O=j]\), pour la log-perplexité \(L\), n’implique pas \(P(X,L\mid O=i)=P(X,L\mid O=j)\). Sans égalité des distributions de difficulté, une différence de FNR reste possible sous \(A\perp O\mid X,L,Y\).
- **Fausses alertes.** Si indicateur social et demande directe d’alerte sont identiques dans toutes les cellules, leurs coefficients ne sont pas séparables. Les contrastes social–neutre et lexical–neutre peuvent être simultanément positifs.
- **Sonde, juge, auditeur.** Pour l’aire partielle brute, \(\int_0^q\mathrm{ROC}(u)\,du\le q\) : le seuil proposé est impossible sans définition normalisée. Le FPR d’épisode est \(1-P(\bigcap_t\{A_t=0\}\mid Y=0)\), non déterminé par les FPR marginaux par étape. Si seuls les signalés sont traités, le rappel global est \(P(R=1\mid Y=1)P(A_{\rm audit}=1\mid R=1,Y=1)\) : le second facteur seul ne borne pas le premier par en dessous.

### (c) Contrôles négatifs indispensables — HYPOTHÈSE

Ajouter un remplissage réellement neutre sans demande et une **demande nue d’alerte**. Pour le style, faire subir la même réécriture aux deux origines, sans sélectionner les paraphrases sur le FNR du test. Pour la sonde, réserver des appels textuellement identiques, permis ou interdits selon l’état externe, et tester aussi avant émission. Pour le juge et l’auditeur, conserver les échecs bénins non corrigés et les épisodes jamais transmis. Sans eux, les seuils annoncés décriraient une population triée.

## Sur la proposition E

### (a) Défauts de méthode — HYPOTHÈSE

- **Taxonomie et E1.** Je conteste l’interprétation de « partition » : un dommage non signalé peut satisfaire les descriptions du silence exogène et du couplage endogène. Le couple état–alerte ne renseigne pas seul sur la voie causale. L’indicateur composite mêle erreur de tâche et violation de sûreté alors que le contrôle négatif ne borne que la seconde.
- **E2.** L’agent agit, le juge classe une trace figée ; leurs taux de base et leurs possibilités d’erreur diffèrent. Leur écart net décrit les deux rôles testés, pas l’effet de la passivité *seule*.
- **E3.** La moyenne croisée annule des effets principaux additifs, pas une interaction entre compétence et difficulté. La canonisation peut enlever la preuve de l’infraction autant que la signature. Le facteur « agent informé du moniteur » devrait entrer dans le contraste au lieu d’être moyenné.
- **E4.** « Juge muet sous pression » inclut ceux qui étaient déjà muets sans pression. Un rappel dans cette strate mesure un secours opérationnel, non le moment où la décision verbale a divergé. Tester le juge uniquement sur les violations manquées par la liste blanche donne à cette référence un rappel nul par construction dans cette strate.

### (b) Conditions de perte de puissance ou d’identification — VÉRIFIÉ

- **E1.** Pour \(n\) paires indépendantes, \(\operatorname{Var}(\hat\Delta)=[p_{01}+p_{10}-(p_{01}-p_{10})^2]/n\). L’effectif seul ne garantit pas la précision annoncée. Si l’intervalle simultané de \(\max_r\Delta_r\) traverse le seuil, la partition des *paramètres* est exhaustive, la décision empirique ne l’est pas.
- **E2.** Chaque hausse de risque est bornée par \(1-p_{\rm base}\). Des marges de progression différentes autorisent un \(G_{\rm mon}\ne0\) même sous un déplacement identique des log-cotes.
- **E3.** Si l’intervalle de \(\Delta^{\rm brut}\) inclut zéro, la fraction supprimée n’est pas résolue ; le plancher numérique change l’estimand. À \(\Delta^{\rm brut}>0\), tester conjointement \(\Delta^{\rm brut}\ge d\) et \(\Delta^{\rm brut}-\Delta^{\rm canon}\ge r\Delta^{\rm brut}\) évite la division.
- **E4.** Si \(P(Y=1,A=0\mid Z)=0\), le rappel conditionnel est indéfini. Le bénéfice marginal exact d’une sonde ajoutée au juge est \(P(A=0,S>\tau\mid Y=1)\) ; il peut être presque nul malgré un rappel conditionnel élevé.
- **Persistance, coût et audit.** Si \(P(\text{encore observable à }k\mid X)=0\) sur une strate, sa persistance à \(k\) n’est pas identifiable. Pour l’audit, la pondération par \(1/P(R=1\mid X,A)\) requiert des probabilités positives et une sélection indépendante du verdict potentiel conditionnellement à \(X,A\). La variance augmente quand ces probabilités tendent vers zéro.

### (c) Contrôles négatifs indispensables — HYPOTHÈSE

Geler le seuil d’erreur de tâche hors test et mesurer séparément erreurs bénignes, violations et interruptions. Pour E2, comparer les verdicts sur traces strictement identiques en ne changeant que le rôle annoncé. Pour E3, canoniser aussi des traces honnêtes et des erreurs non coordonnées de **même difficulté de détection**, pas seulement des mutations aléatoires. Pour E4, rejouer chaque trace sous placebo, distinguer omissions préexistantes et changements de verdict, puis calibrer séparément sur des négatifs jamais utilisés pour choisir la couche. **Je changerais d’avis sur l’utilité pratique de la sonde** si, à budget fixé et sur tâches réservées, son gain *joint* avec le juge persistait sans hausse compensatrice des interruptions honnêtes ; cela ne suffirait toujours pas à localiser un mécanisme de corruption.

FIN-DE-CELLULE
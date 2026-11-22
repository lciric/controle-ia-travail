# Proposition B, Tour III.2 : critique croisée de méthode

**État des pièces.** Les cinq conceptions A, C, D, E et F sont présentes. Aucune ne paraît coupée : chacune se termine par sa ligne de clôture. Le bloc FAITS reproduit la question et ne contient aucun fait porteur d'un statut. Chaque défaut signalé ci-dessous est donc une **HYPOTHÈSE de méthode**, que l'expérience correspondante peut confirmer ou réfuter. Les seuils repris des pièces gardent leur marque « illustratif ». Les miens sont illustratifs aussi. Les statuts apposés par les autres propositions ne sont pas modifiés ici. Je signale seulement ceux qu'aucun fait transmis ne permet de juger.

**Notations communes pour les points (b).**
- S : score d'un lecteur. F₁ : loi de S sous dégradation. F₀ : loi de S sous erreur honnête.
- AUROC = P(S₁ > S₀).
- α : taux de fausses alertes visé. n₀ : nombre de trajectoires honnêtes servant à estimer le seuil q̂₁₋α.
- m : nombre d'actions par trajectoire. ρ : corrélation intra-trajectoire, ou intra-famille de dossiers.
- n_eff = n / (1 + (m−1)ρ) : effectif efficace.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **E2 vrai par construction (variable « hors politique »).** Le texte de sabotage est généré par l'agent. Le texte témoin est *imposé* dans un contexte honnête. Ce texte imposé a donc une log-probabilité plus basse sous le modèle qui le lit. Une sonde peut séparer les deux provenances en lisant seulement la « surprise » du modèle devant ses propres jetons, sans aucun calcul de dégradation.
   - En plus, l'instruction est présente d'un seul côté. L'AUROC à texte identique mesure donc aussi « instruction présente ».
   - Le témoin « instruction inerte » traite le second point, pas le premier.
2. **E1 biaisé par sélection.** Les erreurs honnêtes sont, par définition, les états où l'agent honnête a échoué. On s'attend donc à ce que la bonne action y soit moins décodable. Les pas sabotés, eux, ne sont pas sélectionnés sur un échec du modèle.
   - L'écart « saboté ≥ erreur honnête + 25 points » (illustratif) est donc favorisé d'avance.
   - Il faudrait comparer sur les **mêmes états** : ceux où la condition honnête a échoué, et rien d'autre.
3. **Le modèle lecteur V7 ne borne pas l'information textuelle.** Un modèle d'une autre famille, avec d'autres capacités, extrait moins du même texte pour des raisons de représentation. Battre V7 ne montre donc pas qu'on lit au-delà du texte. Le lecteur pertinent est **le même modèle** qui relit la trajectoire sans instruction ni déclencheur ; c'est une variante de V4 sur les activations.
4. **E3 risque de mesurer un effacement trivial.** La direction apprise entre sabotage et honnête contient la représentation de l'instruction. L'ôter « rétablit la qualité » sans rien dire d'un calcul par pas. A le reconnaît dans sa réserve, mais aucun critère n'en tient compte.
5. **Fuite possible.** Le découpage entraînement/test n'est pas fixé par trajectoire ni par famille de dossiers. Des actions d'une même trajectoire peuvent se retrouver des deux côtés.
6. **Appariement sur le résultat final.** Apparier sur l'ampleur de l'erreur finale ne règle pas la position des erreurs dans la trajectoire. Le sabotage concentre ses écarts sur les pas à fort levier (HYPOTHÈSE). La position du pas devient alors un confondant pour toute sonde au niveau action.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E0 et E4.** Le seuil q̂₀,₉₅ estimé sur n₀ trajectoires a une erreur d'ordre √(α(1−α)/n₀). Si cette erreur est comparable à l'écart de détection visé, le critère « gain ≥ 15 points » (illustratif) ne tranche pas.
- **Appariement « même ampleur ».** Il est non jugeable si les supports de P(Δ_final | sabotage) et de P(Δ_final | honnête) se recouvrent peu, c'est-à-dire si la positivité est violée. Le jeu apparié est alors vide ou atypique.
- **E1.** La puissance disparaît si P(type F1 | sabotage) est petit. Les pas réellement « commission ciblée » sont alors trop rares pour estimer l'exactitude du décodeur.
- **E3.** La fraction récupérée (Q_abl − Q_sab)/(Q_hon − Q_sab) devient instable si Q_hon − Q_sab est du même ordre que son écart-type d'estimation. Le ratio n'est alors plus jugeable.
- **E5.** « Taux < 1,5 × honnête » (illustratif) n'est pas jugeable si le taux honnête d'actions dégradées est proche de 0 : le ratio est indéfini.
- **E2, transfert.** Si ρ entre actions d'une trajectoire est élevé, n_eff ≈ nombre de trajectoires, et l'intervalle autour de 0,75 (illustratif) s'élargit en conséquence.

### (c) Contrôles négatifs dont l'absence serait fatale

- Texte **honnête généré par une autre graine du même modèle**, puis imposé, opposé au texte honnête en politique. Sans lui, E2 lit le caractère hors politique.
- Erreurs honnêtes **aux mêmes états** que les pas sabotés, pour E1.
- Sonde sur le **même modèle relisant sans instruction**, à la place ou en plus de V7.
- Permutation des étiquettes **au niveau trajectoire**. Une permutation au niveau action fixe un plancher trop bas si des actions d'une même trajectoire fuient entre les plis.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Identité des poids comme confondant majeur.** R_ft-sab tourne sous un adaptateur LoRA, R_honnête-err sous le modèle de base. Toute sonde peut séparer « poids modifiés » de « poids d'origine ».
   - L'expérience 1 entraîne sur R_prompt-sab contre R_honnête-err, puis teste R_ft-sab contre **le même** R_honnête-err. Le même ensemble négatif sert donc à la construction et à l'évaluation.
   - Un décalage de distribution dû à la LoRA suffit à donner un transfert élevé. Ce résultat serait vrai par construction.
   - Aucun témoin « LoRA honnête de même procédure d'entraînement » n'est prévu.
2. **Le filtre P_honnête(a_t | s_t) ≥ 0,10 (illustratif) désarme M-T1.** La log-vraisemblance sous le modèle de référence est tronquée de la même façon dans toutes les conditions. Le CUSUM des log-probabilités, présenté comme la base texte forte, voit sa puissance réduite par le montage même. L'avantage de la sonde est alors en partie fabriqué.
3. **Expérience 2 : sélection sur l'action identique.** Retenir les seuls états où saboteur et honnête émettent la même erreur, c'est conditionner sur une issue commune. Chez l'honnête, ce sont des états difficiles ; chez le saboteur, des états quelconques. ΔP_vérité est favorisé dans le sens de H_A.
   - De plus, v_sab est apprise entre R_ft-sab et R_honnête-err. Elle contient le décalage induit par la LoRA. La projeter peut défaire une partie de l'adaptation, ce qui produit une « restauration » par construction.
   - Le contrôle « effet < 5 points sur R_honnête-err » (illustratif) est faible : sur le modèle de base, la composante LoRA de v_sab est presque nulle.
4. **Fuite SAE.** Les k latents (illustratif) sont choisis par parcimonie sur des données dont le partage avec l'évaluation n'est pas précisé.
5. **Fuite CUSUM.** Le CUSUM centre sur « la moyenne honnête ». Si cette moyenne est estimée sur les trajectoires honnêtes de test, la base texte est mal calibrée, et l'erreur peut aller dans un sens ou dans l'autre.
6. **Statuts non jugeables ici.** C marque VÉRIFIÉ qu'« une politique peut être compilée dans les poids sans exécuter l'algorithme de résolution », en s'appuyant sur le théorème d'approximation universelle. Ce théorème est un résultat d'existence ; il ne dit rien des politiques effectivement apprises. Je ne change pas ce statut ; je signale qu'aucun fait transmis ne l'établit. La loi O(t) contre O(√t), également marquée VÉRIFIÉ, suppose des erreurs honnêtes indépendantes, ce que C lui-même conteste dans le cas « boule de neige ».

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Δt\* (avance de détection).** C'est une médiane de temps censurés. Si P(S_texte ne franchit jamais le seuil avant T) > 0,5, ou la même chose pour S_int, la médiane n'est pas estimable. Le critère « ≥ 8 actions » (illustratif) n'est alors pas jugeable sans estimateur de survie.
- **ΔP_vérité.** Il suppose que la sonde de vérité est calibrée sur les activations de la LoRA. Si la divergence entre les lois d'activation de base et de LoRA est grande, P_sonde n'est pas comparable d'un modèle à l'autre, et la différence n'est pas interprétable.
- **Ensemble des 300 états (illustratif).** Sa taille dépend de P(a_sab = a_hon | les deux erronés). Si ce paramètre est petit, l'ensemble est petit et non représentatif.
- **Intervalle sur l'AUROC de transfert avec 500 paires (illustratif).** Il n'est valide que si les paires sont indépendantes. Avec ρ intra-dossier non nul, la borne inférieure à 0,62 est surestimée.
- **Base texte face aux erreurs « boule de neige ».** Elle perd sa puissance si la loi des incréments de dérive honnêtes a la même espérance directionnelle que celle du sabotage. C le note, mais n'en tire aucune condition d'arrêt.

### (c) Contrôles négatifs dont l'absence serait fatale

- **LoRA honnête** entraînée avec la même procédure, le même volume et le même format, utilisée comme négatif dans les expériences 1 à 3.
- Ensembles honnêtes **disjoints** entre l'entraînement de la sonde et le test de transfert.
- Ablation de v_sab appliquée à la **LoRA honnête**, pas au seul modèle de base.
- Base texte évaluée **sans le filtre de vraisemblance**, ou avec un filtre réalisé par un modèle distinct de celui du CUSUM.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Duel 2 : comparaison principale vraie par construction.** La cible est le *but assigné*. La base texte principale ne lit que le **préfixe produit**, sans la consigne. Les états internes, eux, portent la consigne. Un gain est donc attendu sans aucun calcul de choix. D publie aussi une base lisant toute l'entrée, mais sa règle de décision repose sur la comparaison au préfixe. C'est l'ordre inverse qui serait sûr : la base à entrée complète en comparaison principale, la base préfixe en comparaison secondaire.
2. **Duel 3 : le sous-espace peut coder une donnée d'entrée.** Ce sous-espace est choisi pour prédire « quelle clé nuit ». Or cela se déduit de la contrainte inscrite plus tôt dans le dossier.
   - Un sous-espace qui code simplement cette contrainte lue produit, une fois échangé avec le jumeau, la bascule attendue. Ce n'est pas un calcul de conséquence anticipée ; c'est le transport d'une donnée d'entrée.
   - Le critère « sens opposé selon le but » écarte un sous-espace qui coderait le but, pas un sous-espace qui coderait l'entrée. D dit lui-même qu'un succès soutiendrait un calcul *partagé* ; il faut en plus séparer ce calcul de l'entrée.
3. **Taille de l'organisme.** Le budget est chiffré sur un modèle de 1,5 milliard de paramètres (RAPPORTÉ par D). Si l'effet de pilotage reste sous 0,30 (illustratif), la règle d'arrêt dit « changer le banc ». Elle ne distingue pas un banc trop dur d'un modèle trop petit.
4. **Point fort à noter, sans fusionner.** D est la seule proposition qui fixe l'unité d'incertitude à la famille de dossiers et sépare les familles entre développement et test. Les fuites sont donc mieux tenues que chez A et C.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Règle par intervalle.** Soient σ_f l'écart-type entre familles de l'effet apparié et n_f le nombre de familles. Si 1,96·σ_f/√n_f ≥ |effet − seuil|, l'intervalle chevauche le seuil et le duel ne tranche pas. C'est la zone que D prévoit lui-même. Avec 400 familles (illustratif), il faudrait vérifier a priori σ_f sur un pilote.
- **Pilotage.** L'effet est moyenné sur les permutations. Si P(clé dommageable | honnête) tombe au hasard dans un sens de permutation, l'effet n'est pas identifiable ; D le contrôle déjà.
- **Duel 3.** Le seuil est exigé « dans chacun des deux buts ». La puissance est donc celle du plus faible des deux tests. Si P(choix | but de dégradation) est déjà saturé près de 1, la hausse possible est bornée, et le seuil de 0,15 (illustratif) devient inatteignable par plafonnement, pas par absence d'effet.
- **Strate difficile appariée.** Le taux de couverture de l'appariement peut être faible. La strate devient alors un petit sous-ensemble sélectionné, et son taux d'alerte n'est pas transposable ; D le note.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Échange d'un sous-espace qui ne code qu'une variable d'entrée non pertinente**, de même rang et de même décodabilité, à comparer au sous-espace « conséquence ». Le sous-espace aléatoire prévu par D ne suffit pas.
- **Base texte avec consigne** utilisée comme comparaison principale du duel 2.
- Pour le duel 3, **échange entre jumeaux identiques**, sans inversion des conséquences. Il mesure la bascule due à la seule intervention.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **E2 vrai par construction.** La précision de décodage de a\* chez Saboteur-LoRA est comparée à celle de Honnête-Capacité-Réduite. Or un agent à capacité réduite représente, par sa construction même, moins d'information. Un écart d'au moins +0,20 (illustratif) est donc attendu sans aucun « double suivi ».
   - Le bon témoin serait Honnête-Biaisé, puisqu'E le construit par LoRA, évalué **aux mêmes états**.
   - En plus, la sonde de vérité est entraînée sur Honnête-Standard puis appliquée aux poids LoRA, sans contrôle du décalage de distribution des activations.
2. **Identité de modèle.** La construction de Honnête-Capacité-Réduite n'est pas précisée : modèle plus petit, quantification, ou LoRA ? Selon le cas, le mélange témoin de E1 contient un modèle différent. La sonde peut lire l'identité des poids.
3. **E1 : max sur deux instants.** max_{t∈{10,30}} ΔTPR est un maximum de deux estimateurs bruités. Il est biaisé vers le haut, et rien ne le corrige pour comparaisons multiples.
4. **E3 : fuite entre construction et test.** S, appris entre Saboteur-LoRA et les témoins, contient le décalage LoRA. L'injecter dans Honnête-Standard teste en partie l'injection d'une « LoRA partielle ».
5. **E4 : contrôle négatif non informatif.** « Une sonde sur les jetons d'invite chute à 0,5 sur LoRA » est attendu, puisque ces jetons n'existent pas dans la condition LoRA. Le contrôle ne peut pas échouer.
   - Par ailleurs, lire « hors jetons d'invite » n'exclut pas l'invite. L'attention la recopie dans les positions d'action ; c'est précisément le confondant que E décrit au point 3.
6. **Statuts non jugeables ici.** « Les petits modèles échouent fréquemment… » est marqué OBSERVÉ-NON-AUDITÉ sans source d'observation dans les pièces. La nécessité conditionnelle 1 est marquée VÉRIFIÉ « par Fano » : l'argument de traitement de l'information porte sur la politique, pas sur une représentation lisible à une couche donnée. Je ne change pas ces statuts ; je signale qu'aucun fait transmis ne les établit.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **AUROC contre un mélange de témoins.** L'AUROC contre le mélange π·F₀^biaisé + (1−π)·F₀^capacité vaut la moyenne pondérée des deux AUROC. Si un des deux témoins est facile à séparer, il masque l'échec sur l'autre. Le critère n'est jugeable que témoin par témoin.
- **Appariement ±3 % (illustratif).** Il n'est pas réalisable si les supports des lois de justesse finale des trois agents ne se recouvrent pas : la positivité est violée.
- **Réplication de puissance doublée.** Elle tranche à +0,10 (illustratif) seulement si la variance de ΔTPR décroît en 1/n. Avec ρ intra-instance symétrique, n_eff augmente moins que n, et la zone grise peut subsister.
- **E4, paraphrase neutre.** Le critère de maintien « ≥ 0,80 du taux initial » (illustratif) suppose que le paraphraseur ne change pas la loi des choix honnêtes. Si P(choix | contexte paraphrasé, honnête) diffère de P(choix | contexte original, honnête), la baisse observée confond stigmergie et effet de paraphrase.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Honnête-Biaisé aux mêmes états** comme seul témoin de E2.
- **LoRA honnête de même algorithme d'entraînement** (préférence ou renforcement, sans récompense de sabotage) comme négatif de E1 et E3.
- **Paraphrase appliquée aux trajectoires honnêtes**, avec mesure de la variation des choix, pour E4.

---

## Sur la proposition F

### (a) Défauts de méthode

1. **Sélection sur l'échec du comparateur.** F mesure le gain marginal « sur le sous-ensemble de cas jugés défendables par le texte ». Sur ce sous-ensemble, le TPR du texte est proche de 0 par construction. Le gain de la sonde y est donc gonflé : c'est une sélection sur l'erreur de la base.
   - La porte de qualification exige aussi que le juge B1 soit au hasard, et B1 fait partie de I2.
   - Le même instrument sert ainsi à construire le banc et à évaluer le comparateur.
2. **AUROC intra-trajectoire : le pas d'embranchement comme confondant.** Les pas « saboteurs » sont, par construction, des pas d'embranchement méthodologique. Les « pas neutres » sont des pas de routine. Une sonde qui lit « je suis à un embranchement » obtient une AUROC intra élevée sans rien lire d'une intention.
   - La consigne bénigne de formatage (H4) n'interagit pas avec les embranchements ; elle ne contrôle pas ce confondant.
3. **E1 en régime instruit.** La consigne est présente à chaque pas. Le contrôle intra-trajectoire élimine la lecture statique de la consigne. Il n'élimine pas l'interaction consigne × embranchement : l'invite peut être davantage lue aux pas de décision.
4. **Divergence de références.** Le titre de *AI Control* diffère entre F (« Regardless of ») et A, C, E (« Despite »). L'année de Levinstein & Herrmann diffère aussi selon les pièces. Les deux sont à classer **référence à vérifier** ; je ne tranche pas.
5. **Point fort à noter, sans fusionner.** Le témoin H5 (honnête SFT/RL de même style) et le budget d'étiquettes égal pour la base texte traitent explicitement les confondants « identité des poids » et « base homme de paille ». Ce sont deux défauts que je relève chez C et E.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **I1a, « TPR ≥ 0,60 à FPR ≤ 0,01 » (illustratif).** Le quantile q̂₀,₉₉ du maximum des scores sur trajectoires honnêtes repose sur environ n₀·0,01 observations au-delà du seuil. Avec 400 témoins par modèle (illustratif), cela fait environ 4 cas. Le critère n'est pas jugeable à ce niveau ; seul le point à 5 % l'est.
- **Agrégation par maximum.** Elle perd sa puissance si le nombre de pas saboteurs par trajectoire, |S|, est petit et si la loi du maximum honnête sur m pas a une queue comparable à F₁. C'est la dilution que F calcule lui-même.
- **Ratio de sélectivité R / max(δ_hon ; 0,01) (illustratif).** Le plancher fixe crée une discontinuité. Si δ_hon fluctue autour de 0,01, le ratio est dominé par le plancher, pas par les données.
- **M2 (multivers).** Il perd sa puissance si la dispersion de la loi des estimateurs sur l'ensemble des spécifications est petite devant Δ. Le choix saboté n'est alors pas dans une queue extrême, et la base mécanique est vaincue d'avance.
- **E4.** Le critère TPR(B) ≥ 0,40 (illustratif) suppose F₀ estimée sur un témoin honnête-biaisé dont l'amplitude d'erreur est égalisée. Si les lois de Δ des deux groupes diffèrent, l'écart Δ_régime confond régime et amplitude.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Pas d'embranchement honnêtes** (même embranchement, agent honnête) comme négatifs de l'AUROC intra-trajectoire.
- **Juge de qualification distinct** des juges de I2, et évaluation sur **toutes** les trajectoires qualifiées, pas sur la seule strate où le texte échoue.
- **Biais instruit déclaré** (« choisis toujours l'estimateur conservateur »), honnête et sans dissimulation, actif aux mêmes embranchements, pour écarter l'interaction consigne × décision.

FIN-DE-CELLULE
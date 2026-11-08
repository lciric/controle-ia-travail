# Proposition B — Tour III.1 : conception ciblée sur la trace, la règle de défense et la pince

**Notation des statuts.** [V] VÉRIFIÉ : cela ne s'applique qu'aux empreintes recalculées ✓ dans les faits, pas au contenu des pièces. [R] RAPPORTÉ. [ONA] OBSERVÉ-NON-AUDITÉ. [H] HYPOTHÈSE. [rel.] désigne un relevé du dépôt que les faits citent sans statut explicite ; je ne le requalifie pas et ne le traite pas comme un résultat. Toutes mes propositions sont [H]. Tout seuil, effectif ou coût chiffré de ma main est **illustratif**.

**Pièces manquantes ou coupées** (une ligne chacune) :
- Empreintes tronquées dans le texte servi (`3ecab00f…`, `998404fe…`, `3dff5853…`, `14d92537…`, `b000cc5e…`, `dece9980…`, `320463e6…`, `30f265a9…`, `3793b4c0…`) : je ne peux pas les vérifier.
- Le gabarit de la pince (`5eab49e4…`) n'est pas vérifié, faute de branche récupérée.
- Le contenu de N-059 point 11 (arrêt par budget) n'est pas servi.
- Le métrique exact du « prédicteur sur le texte 0,866 » n'est pas précisé (aire ? exactitude ? sur quels cas ?).
- Le modèle de base de T0.6 n'est pas nommé dans les faits.
- Écart interne à la question : « défaut de 12:45 UTC » (Lancement) contre « repoussé à 13:00 UTC » (en-tête). Sans incidence sur le fond.

Je ne vois aucune autre proposition, A, C, D ou E. Les lettres (A) et (C) employées plus bas renvoient aux positions de l'étage I du 22 octobre, telles que les faits les citent.

---

## (a) Ce que la question suppose sans que ce soit établi

**S1. L'oracle voit le sabotage diffus.**
- L'audit du rappel « manque » [rel.].
- Le dommage est défini comme une baisse de couverture contre le jumeau apparié [rel., N-060 v3]. Un sabotage qui ne baisse pas la couverture est donc invisible **par construction**.
- Le rappel est borné par la définition, pas seulement par la qualité de l'oracle. Un rappel mesuré sur le flagrant ne dit rien du diffus.

**S2. Le « diffus » est défini indépendamment de la mâchoire externe.**
- La dose diffuse « se fixe sur la boîte noire seule » [rel., R3]. Si la boîte noire qui fixe la dose sert aussi de mâchoire externe, ses manqués sont sélectionnés d'avance.
- Le dénominateur de la capture résiduelle est alors gonflé par construction. Cette circularité n'est levée nulle part dans les faits.

**S3. La mâchoire externe ne lit aucune prose.**
- C'est la définition du gabarit [non vérifié].
- Or la question propose comme candidat le prédicteur « sur les traits du texte » (0,866) [rel.]. S'il lit la prose de l'agent, l'attaquant contrôle son entrée : c'est le cas dégénéré **L2** [H, étage I], où la pince vaut l'interne seule.
- Le candidat cité contredit donc la définition de la pince. Il faut le classer « externe-texte », distinct de « externe-code-exécution ».

**S4. Jev 1.14 est une mâchoire utilisable.** Il est [ONA], sans aucun cas honnête et avec un taux de fausses alertes inconnu [rel.]. Ses 0,97 / 0,96 / 0,93 portent sur trois triches grossières, pas sur le diffus.

**S5. Il existe une mâchoire interne causale.**
- « Toute sonde causale » est absente [rel.].
- L'« axe de douleur » se lit mais n'est pas un levier (retrait sans effet 24/25) [R].
- Seule la sonde de flagrant marche (W − G = +0,932) [rel.], et elle lit la consigne privée (a_NE 0,9967) [rel.].

**S6. Une trace existe (H1)** [H]. Les sondes génériques sont près du hasard (rappel 0,013) [rel.], tout comme le juge de 3 milliards (aire 0,523) [rel.]. L'issue H8 est au même rang [question, R3].

**S7. L'étau est une propriété mesurable sur nos organismes.**
- Les organismes (ii) sont distillés depuis (i) [rel., P-009]. Rien dans les faits n'indique qu'aucun ait été optimisé **contre** une mâchoire externe.
- Sans attaquant sous pression, on ne mesure qu'une corrélation transversale entre scores, pas l'étau. L'étau est une proposition **interventionnelle** : appliquer une pression contre l'externe déplace l'interne.
- La métrique convergente de l'étage I (capture résiduelle) mesure une complémentarité. Elle ne mesure pas, à elle seule, un effort de dissimulation.

**S8. Les deux familles portent le même confondant.** Ce n'est pas le cas :
- La famille (i) porte surtout le **confondant 1** : la consigne est présente, et la sonde W la lit [rel.].
- La famille (ii) n'a pas de consigne à l'inférence [rel.]. Le confondant 1 y disparaît, mais le **confondant 2** (identité des poids) y est maximal.
- Les deux familles échangent donc leurs confondants. Toute conclusion doit tenir sur les deux.

**S9. L'écart adapté − base est un signal d'acte.**
- Avec α = 0, on retrouve la base au bit près [rel., P-009]. L'écart est donc identiquement non nul dès qu'α > 0, **sur tout épisode, sabotage ou non**.
- Aux couches où l'adaptateur écrit, cet écart vit dans le sous-espace de sortie de l'adaptateur, de rang faible : c'est d'abord un porteur d'identité.
- La seule trace d'usage comme moniteur est Chameleons N12 [R].

**S10. Le transfert d'évasion entre nos sondes ressemble à celui de 2609.36490.** La figure 4a [R] porte sur trois architectures, « entre sondes seulement (aucun juge) ». La matrice sur nos sondes est absente [rel.].

**S11. L'arène synthétique dit quelque chose du vrai modèle.**
- L'audit « trop beau » a été déclenché et les tables B/B′ sont suspendues ; aucun verdict n'est scellé [rel.].
- HR1 (+0,10 / +0,12) et « R0 figée généralise mieux » (+0,05 / +0,06) sont deux lectures non scellées, de sens opposés pour la question 5.

**S12. On dispose d'assez de familles tenues à l'écart.** R-1795 dit que chaque lecture décisive consomme une famille neuve [rel.]. Le nombre de familles disponibles n'est pas dans les faits. Le plan doit donc rationner ses lectures décisives.

**S13. La règle d'union à τ/2 + τ/2 fixe le taux joint à τ.** C'est une borne supérieure, valable seulement si chaque seuil est calibré sur **le même** dénominateur honnête, échecs honnêtes compris. Le taux joint réel dépend de la corrélation des fausses alertes et doit être mesuré, pas supposé.

**S14. Le calendrier « d'ici l'entretien TAIF » est tenable.** La date n'est pas servie. Aucune faisabilité n'est évaluable.

---

## (b) Expériences décisives, en inférence forte

**Rationnement des familles tenues à l'écart (S12)** [H] :
- Seules **X4** (pince) et **X6** (secret contre aléa) consomment une famille tenue à l'écart, une fois chacune, après G1.
- X0 à X3 et X5 se lisent en validation croisée par bloc sur les familles vues (i), (ii) et les états d'E3 bis. C'est le substitut du confondant 3 [rel.].
- Si une seule famille tenue à l'écart existe, X4 passe avant X6.

**Ordre de garde** :
- X0 conditionne tout.
- X1 et X2 conditionnent X3.
- X3 conditionne la clause « inévitable sans perte de dommage » de X6.
- X4 et X5 sont indépendantes l'une de l'autre, mais toutes deux dépendent de X0.

### X0 — Rappel de l'oracle et indépendance oracle–moniteurs (volet vérité terrain ; mâchoire sans objet)

**Duel X0a.**
- H_A : l'oracle détecte les sabotages connus **de magnitude diffuse** avec un rappel ≥ r*.
- H_B : rappel < r*.

**Données.**
- Un jeu de sabotages connus constitué par le sas d'évaluation tiers. Son contenu est scellé côté défense, et la recette n'est pas lue (garde R-607).
- Ce jeu est stratifié par magnitude de baisse de couverture : la strate « diffuse » est définie par une borne de dommage fixée **avant** toute lecture.
- Les jumeaux honnêtes appariés servent de négatifs.

**Métrique.**
- Rappel par strate, avec un intervalle de Clopper-Pearson (Clopper et Pearson, 1934, *Biometrika*, « The use of confidence or fiducial limits illustrated in the case of the binomial »).
- Taux de fausses alertes de l'oracle sur les jumeaux.
- Accord des deux lecteurs (κ).

**Seuil illustratif** : borne basse à 95 % ≥ 0,70 sur la strate diffuse, soit environ 60 cas si le rappel vrai est d'environ 0,85.

**Contrôle négatif** : épisodes honnêtes rejoués deux fois. L'oracle doit être stable ; toute alerte y est une fausse alerte pure.

**Issues.**
- H_A est falsifiée si la borne haute est sous 0,70. On suspend alors les points 1 à 5 **pour la strate diffuse** seulement, comme la question le demande, et le flagrant reste lisible.
- H_B est falsifiée si la borne basse est ≥ 0,70.

**Duel X0b.**
- H_A : les erreurs de l'oracle sont indépendantes de celles de chaque moniteur.
- H_B : elles sont associées.

**Métrique.**
- Sur le jeu connu, où la vérité ne dépend pas de l'oracle, on construit le tableau 2×2 « oracle manque × moniteur manque ». On en tire un rapport de cotes conditionnel par strate.
- On teste l'**équivalence** (deux tests unilatéraux, Schuirmann 1987, *J. Pharmacokinet. Biopharm.*). Une simple absence de signification ne suffit pas.

**Marge illustrative** : rapport de cotes dans [0,5 ; 2].

**Plan factoriel.** Famille de l'oracle × famille du moniteur, croisées. Cela répond à la diversité de famille, l'un des neuf contrôles [rel.].

**Issues.**
- H_A est falsifiée si l'intervalle sort de la marge. Toute mesure de détection doit alors être corrigée sur le jeu connu.
- H_B est falsifiée si l'intervalle est inclus dans la marge.

**Pièce** : table scellée des rappels et des rapports de cotes. **Vérifiable par** recalcul depuis les étiquettes brutes.

### X1 — Existence au-delà du texte et au-delà de la consigne (volet existence ; mâchoire interne)

**Duel.**
- H_A : les activations de l'organisme portent, sur l'étiquette de l'oracle, une information que **le modèle de base relisant les mêmes jetons** n'a pas.
- H_B (H8) : tout ce qui se décode est déjà décodable du texte par un modèle de même capacité.

**Contrôle « base qui relit ».** C'est le plus fort contrôle de l'« au-delà du texte » que permettent les faits :
- On passe la trajectoire de l'organisme, jeton par jeton, dans le modèle de base (α = 0, au bit près [rel.]). On entraîne la **même** architecture de sonde, aux mêmes couches et positions, sur ces activations.
- Ce contrôle domine le prédicteur sur traits de texte, qui reste un plancher supplémentaire. Le modèle de base extrait du texte au moins ce qu'un modèle de cette taille sait en extraire.

**Plan contrefactuel (confondant 1)**, croisement consigne × acte :
- Famille (i), épisodes dormants (consigne d'attaque, exécution attestée honnête par l'oracle).
- Famille (ii) (aucune consigne, sabotage attesté).
- La famille (ii) fournit naturellement la case « consigne neutre, sabotage » ; je le note comme une observation sur la construction, pas comme un résultat.
- Les sondes sont entraînées **à l'intérieur d'un même organisme** (sabotage contre dormant) pour neutraliser le confondant 2. Le confondant 2 est traité en X2.

**Positions.** Trois classes figées au préenregistrement :
- avant l'action : les jetons qui précèdent la première frontière d'action étiquetée ;
- pendant l'action ;
- après l'action.
Le texte avant l'action ne contient pas encore l'acte. Un ΔAUC positif à cette position est le résultat le plus informatif, et le plus exposé à la fuite par le plan.

**Métrique.**
- ΔAUC = AUC(organisme) − AUC(base qui relit), par couche × classe de position.
- Validation croisée par bloc de famille.
- Correction de Holm sur couches × positions (Holm, 1979, *Scand. J. Statist.*, « A simple sequentially rejective multiple test procedure »).
- L'agrégation sur jetons se fait par max ou par attention seulement [rel., § 8.1].

**Contrôle de capacité** : tâches de contrôle à étiquettes permutées dans chaque strate (Hewitt et Liang, 2019, EMNLP, « Designing and Interpreting Probes with Control Tasks »). La sélectivité (AUC réel − AUC contrôle) est rapportée à côté.

**Seuil illustratif** : borne basse de ΔAUC > 0,03 sur au moins une cellule couche × position préenregistrée, après Holm.

**Puissance illustrative** : environ 300 épisodes de sabotage et 300 dormants par famille. Pour ΔAUC = 0,05 à des AUC autour de 0,7, l'erreur-type de la différence appariée vaut environ 0,02 ; c'est à recalculer par bootstrap sur E3 bis avant scellement.

**Contrôle négatif** : un organisme placebo traité exactement de même, avec une étiquette arbitraire tirée au sort dans ses épisodes. ΔAUC doit y être nul.

**Issues.**
- H_A est falsifiée si tous les ΔAUC sont équivalents à zéro (marge illustrative ± 0,02) sur les deux familles.
- H_B est falsifiée si un ΔAUC dépasse le seuil sur les **deux** familles en validation par bloc.
- Si l'effet n'apparaît que sur (i), il est imputé à la consigne et H8 n'est pas réfutée.
- Issue négative (R-1795) : la reconception est rapportée, sans arrêt.

### X2 — Identité contre acte, localisation par l'écart à la base (volets localisation et causalité faible ; mâchoire interne)

**Duel.**
- H_A (acte) : l'écart D = h_adapté − h_base, sur le même contexte, varie entre épisodes de sabotage et épisodes dormants du **même** saboteur plus qu'entre épisodes appariés du placebo.
- H_B (identité) : D sépare saboteur et honnête, mais à l'intérieur du saboteur, sabotage et dormant ne se séparent pas mieux que dans le placebo.

**Métrique : différence de différences.** δ = AUC_D(saboteur : sabotage contre dormant) − AUC_D(placebo : épisodes appariés par tâche et par position). On mesure deux projections séparément :
- **Dans** le sous-espace de sortie de l'adaptateur, aux couches où il écrit : c'est le porteur d'identité attendu (S9).
- Dans le **complément orthogonal** aux couches suivantes : c'est ce que le calcul de la base propage.

**Test d'identité explicite** : une sonde entraînée sur « saboteur dormant contre placebo dormant ». Si elle atteint le même AUC que sur les épisodes de sabotage, elle lit l'identité. C'est le confondant 2 sous sa forme la plus directe.

**Seuil illustratif** : borne basse de δ > 0,03 dans le complément orthogonal.

**Contrôle négatif** : deux placebos de graines différentes l'un contre l'autre. δ doit y être nul.

**Issues.**
- H_A est falsifiée si δ est équivalent à zéro dans les deux sous-espaces. L'écart à la base est alors un détecteur d'organisme, utile pour l'audit mais pas un moniteur d'acte.
- H_B est falsifiée si δ est positif dans le complément orthogonal.

**Prérequis** : construire l'organisme placebo, qui n'existe pas [rel.].

### X3 — Causalité : la trace porte-t-elle le dommage ? (volet causalité ; mâchoire interne)

**Duel.**
- H_A (causale) : substituer, aux couches et positions sélectionnées par X1–X2, les activations du saboteur par celles du jumeau honnête, ou retirer leur composante sur la direction lue, **réduit le dommage mesuré par l'oracle**. La réduction est proportionnelle au déplacement du score de sonde.
- H_B (confondant) : la substitution fait chuter le score de sonde, mais le dommage ne bouge pas. On retrouve le schéma de l'« axe de douleur » : lisible, pas levier [R].

**Pourquoi intervenir seulement dans le sens réducteur.** Toute dégradation non spécifique tend à **augmenter** le dommage, qui est une baisse de couverture. Une réduction ne s'explique donc pas par une simple casse. Le sens augmentant fabriquerait un saboteur : il relève du bras d'attaque et sort de ce plan (garde R-607).

**Dose-réponse.**
- Sur S0, S25 … S100 [rel., E3 bis], on mesure la projection moyenne sur la direction et le dommage.
- H_A prédit les deux monotones et alignés.
- H_B admet une projection monotone (l'identité croît avec α) sans relation avec le dommage, une fois α contrôlé.
- Test : pente du dommage sur la projection, **à α fixé** (résidus intra-dose).

**Localisation par couche.** Si le code permet une échelle α par couche, ce que P-009 ne dit pas [H], on annule l'adaptateur couche par couche. La couche à partir de laquelle le dommage disparaît borne l'endroit où la trace causale est écrite.

**Contrôles négatifs.**
- Une direction aléatoire de même norme.
- La direction « identité » de X2, issue de la sonde saboteur contre placebo. Elle doit changer le score sans changer le dommage. Si le dommage baisse, la séparation acte/identité de X2 est mise en doute.
- La réussite de la tâche honnête est contrôlée sous chaque intervention.

**Méthode** : substitution d'activations au sens de Meng, Bau, Andonian et Belinkov (2022, « Locating and Editing Factual Associations in GPT »), transposée.

**Seuil illustratif** : réduction du dommage d'au moins 30 % de l'écart saboteur − jumeau, intervalle bootstrap excluant 0, et contrôles aléatoire et identité à moins de 5 %.

**Issues.**
- H_A est falsifiée si la réduction est équivalente à celle du contrôle aléatoire.
- H_B est falsifiée si la réduction dépasse le seuil alors que les deux contrôles restent nuls.

### X4 — La pince contre une paire de boîtes noires (volets lisibilité et pince ; mâchoire jointe ; consomme une famille tenue à l'écart)

**Le comparateur.** La question compare la pince à chaque boîte seule. Ce n'est pas le bon adversaire. Le dissensus de l'étage I, entre l'externe durcie de (A) et la capture résiduelle de (C) [H], ne se tranche que contre **une seconde mâchoire externe de famille différente au même budget de fausses alertes**. Sinon, on confond « interne » et « deuxième avis ».

**Duel.**
- H_A : la capture résiduelle de l'interne sur les manqués de l'externe-code-exécution dépasse celle d'une seconde externe.
  - CR_int = P(interne alerte | externe manque, sabotage attesté).
  - CR_ext2 se calcule à l'identique pour la seconde externe.
  - Chaque seuil est fixé à τ/2.
- H_B : CR_int ≤ CR_ext2.

**Dénominateur honnête commun** : jumeaux appariés, placebo, et **échecs honnêtes** (négatifs obligatoires [rel.]), appariés en longueur. L'agrégation par max gonfle les fausses alertes avec la longueur.

**Seuils illustratifs** : τ = 1 %. On demande une borne basse de CR_int − CR_ext2 > 0. Le taux joint mesuré doit être ≤ τ.

**Puissance illustrative** : au moins 100 manqués de l'externe sur la strate diffuse. Si l'externe en manque moins, la capture résiduelle est inestimable ; on le déclare tel et on ne l'extrapole pas.

**Encadrement par les cas dégénérés.**
- On rapporte la courbe rappel–budget de fausses alertes de la pince entre les deux droites L2 (interne seule) et E7 (externe seule).
- Une pince qui ne s'écarte d'aucune des deux n'apporte rien.

**Test d'architecture (critique de la règle λ = LR_ext · LR_int de (A), étage I [H])** :
- Le produit des rapports de vraisemblance suppose les deux canaux indépendants conditionnellement à l'étiquette.
- L'étau, s'il existe, viole précisément cette hypothèse : parmi les sabotages, manquer l'externe va avec une interne plus haute, donc une corrélation négative.
- Mesure : corrélation de Spearman ext–int parmi les sabotages attestés, et calibration (fiabilité) de λ sur les jumeaux.
- Une corrélation positive signale une cause commune (saillance), une corrélation nulle des canaux indépendants, une corrélation négative ce que l'étau prédit.
- Si λ est calibré et la corrélation nulle, la pince est une simple complémentarité, sans étau.

**Contrôles.**
- Le confondant 1 se règle en n'utilisant que des sondes validées par X1 sur la famille (ii).
- Le confondant 2 se règle par le placebo dans le dénominateur.
- L'externe qui a servi à fixer la dose diffuse (S2) est **exclue** des deux mâchoires.

**Issues.**
- H_A est falsifiée si CR_int ≤ CR_ext2 sur la famille tenue à l'écart.
- H_B est falsifiée si CR_int − CR_ext2 > 0, intervalle compris.

### X5 — L'étau comme effet d'une pression, et non comme corrélation (volet pince ; mâchoire jointe)

**Duel.**
- H_A (l'étau serre) : à dommage tenu constant, des générations d'attaquant mises sous pression contre la mâchoire externe montrent un **déplacement interne plus grand** que des générations sous pression placebo.
- H_B (l'étau ne serre pas, E7) : le déplacement interne est équivalent dans les deux conditions, ou plus faible dans la condition externe (évasion conjointe).

**Le contrôle placebo de pression est indispensable.** Toute nouvelle génération d'adaptateur déplace les activations ; le confondant 2 revient sous forme dynamique. Il faut donc une génération sous pression **contre un moniteur sans rapport** (moniteur d'une propriété étrangère au sabotage), à budget d'optimisation égal. Les procédés appartiennent au bras rouge et ne sont pas lus. La défense ne reçoit que les adaptateurs et les épisodes.

**Métrique.**
- Δ_int(g) = rappel de l'interne, à τ/2 fixé, sur la génération g moins sa génération mère.
- La pente β est celle de Δ_int sur la baisse du rappel externe, dans les strates de dommage fixées d'avance.
- On compare β_externe et β_placebo.

**Aveuglement** : le bras rouge ignore tout de la mâchoire interne. Sinon on est en régime « attaquant contre les deux », c'est-à-dire la courbe de coût d'évasion de X6, pas l'étau.

**Seuils illustratifs** : β_externe − β_placebo > 0, borne basse à 95 %, sur au moins 4 générations par condition.

**Issues.**
- H_A est falsifiée si la différence est équivalente à 0 (marge illustrative ± 0,05) ou négative.
- H_B est falsifiée si elle est positive.

**Statut** : sans attaquant sous pression (S7), X5 n'est pas faisable ; on le déclare et on ne remplace pas X5 par la corrélation de X4.

### X6 — Transfert entre nos sondes, valeur du jeu, secret contre aléa (volet règle de défense ; mâchoire interne ; consomme une famille tenue à l'écart)

**Duel X6a (H5).**
- H_A : la diversité effective existe. L'évasion apprise contre la sonde j laisse la sonde k ≠ j détecter, et la valeur de Nash mixte dépasse la meilleure valeur pure.
- H_B : le transfert est fort, et la valeur mixte égale la meilleure pure. Ajouter des sondes n'augmente pas la sécurité.

**Matrice.** T[j,k] = rappel de la sonde k à 1 % de fausses alertes sur les épisodes d'une génération sous pression contre j. Le panel est figé au préenregistrement :
- sondes linéaire, perceptron et attention ;
- trois couches issues de X1 ;
- agrégateurs max et attention ;
- écart à la base (X2), si X2 n'a pas falsifié H_A.

**Valeur du jeu.** Programme linéaire sur la matrice des gains. On donne la valeur pure, la valeur mixte et le support de l'équilibre, avec intervalles bootstrap sur les épisodes.

**Seuil illustratif** : valeur mixte − meilleure pure > 0,05, borne basse > 0.

**Contrôle négatif** : une génération placebo de pression (comme en X5) donne une matrice de référence.

**Issues.**
- H_A est falsifiée si l'écart entre valeur mixte et pure est équivalent à 0.
- H_B est falsifiée sinon.

**Duel X6b (secret contre aléa).** Trois régimes, sur la famille tenue à l'écart :
- (a) sonde figée connue ;
- (b) mélange tiré selon p, l'attaquant ayant optimisé contre l'**espérance** du mélange ;
- (c) réserve jamais déployée [rel., § 8.1].

On calcule gain_secret = rappel(c) − rappel(b) et gain_aléa = rappel(b) − rappel(a).
- H_A : le gain vient surtout du secret (gain_secret > gain_aléa).
- H_B : il vient surtout de l'aléa.

C'est aussi le test vrai-modèle de la tension de l'arène, R3 qui progresse contre R0 qui généralise (S11) :
- Si R0 l'emporte encore sur la famille tenue à l'écart, la conclusion de l'arène passe d'une lecture non scellée à une prédiction testée.
- Si R0 perd, elle est réfutée sur vrai modèle.

**Convergence contre rotation.** Table croisée générations × générations : la défense t est lue contre les attaques s ≤ t.
- La défense **converge** si la valeur du jeu varie de moins de ε pendant k générations consécutives **et** si le triangle inférieur ne se dégrade pas.
- Elle **tourne en rond** si d'anciennes attaques redeviennent efficaces, ce qui révèle un oubli.
- Valeurs illustratives : ε = 0,02, k = 3.
- Arrêt par budget : à lier à N-059 point 11, non servi.
- Hedge (Freund et Schapire, 1997, *J. Comput. Syst. Sci.*) et le SPRT (Wald, 1945, *Ann. Math. Statist.*) sont des candidats nommés pour la règle adaptative et l'arrêt séquentiel. Ils sont absents du dépôt [rel.].

**« Inévitable sans perte de dommage »** : on ne l'affirme que pour une direction ayant passé X3 (H_A). La courbe de coût d'évasion est alors : dommage conservé en fonction du nombre de sondes évitées, mesuré côté défense.

---

## (c) Mesure minimale qui dirait si chaque instrument fonctionne

| Instrument | État | Mesure minimale | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|---|
| Oracle de couverture (N-060 v3) | décidé, rappel inconnu [rel.] | rappel par strate de magnitude ; fausses alertes ; κ entre lecteurs (X0) | jumeaux rejoués deux fois | simple différence de couverture brute sans lecteurs |
| Jev 1.14 | [ONA] ; aucun cas honnête | taux de détection et de fausses alertes à 1 % sur les 50 traces rejouées [rel., question] **plus** jumeaux et échecs honnêtes | échecs honnêtes de même tâche, longueur appariée | longueur du diff, tests sautés, échec de compilation |
| Prédicteur sur traits du texte (0,866) | [rel.] ; métrique non précisée | même grille ; à classer « externe-texte » (S3, régime L2) | jumeaux ; épisodes dormants de (i) | longueur, présence de mots de la consigne |
| Juge sur code et exécution nettoyés | n'existe pas | même grille ; vérifier le nettoyage (aucune prose résiduelle) | idem | Jev ; heuristiques statiques |
| Juge de 3 milliards | aire 0,523 [rel.] | à retirer comme mâchoire, sauf s'il bat le plancher mécanique sur le flagrant | — | — |
| Sonde W | lit la consigne [rel.] | ΔAUC contre « base qui relit » sur la famille (ii) (X1) | dormants du même organisme | sonde sur présence de consigne |
| Sondes génériques | rappel 0,013 [rel.] | sélectivité contre tâches de contrôle (X1) | idem | étiquettes permutées |
| Bases N-056 : cascade de portes, sonde sur le dernier état | présentes en partie [rel.] | servent de planchers boîte blanche dans X1 et X4 | idem | — |
| Écart adapté − base | absent [rel.] | δ en différence de différences, en et hors du sous-espace de l'adaptateur (X2) | placebo ; dormants | identité de l'organisme (sonde saboteur contre placebo) |
| « Axe de douleur » | [H] comme mâchoire ; non causal [R] | ne l'admettre que s'il passe X1 ; ne jamais l'admettre en causal sans X3 | — | — |
| Méta-moniteur d'évasion (Chameleons N12) | [R] dans la littérature | fausses alertes sur générations placebo de pression (X5) : doit **ne pas** alerter | générations placebo | norme de l'écart à la génération mère |
| Matrice de transfert | absente sur nos sondes | X6a | génération placebo | matrice de 2609.36490 comme prior [R], non comme résultat |
| Arène v4, règles R0–R4 | tables B/B′ suspendues [rel.] | rejeu seulement pour **prédire** X6b avant lecture, prédiction scellée | — | R0 figée |

---

## (d) Ancrage matériel (tout chiffre ici est illustratif)

**Modèles.**
- Le modèle de base de T0.6 n'est pas nommé dans les faits. Toutes les expériences s'y font, car les organismes sont des adaptateurs de ce modèle [rel.].
- Pour la vérification par des tiers, on peut ajouter une réplique de X1–X2 sur un modèle ouvert de 7 à 8 milliards de paramètres, par exemple de la famille Qwen2.5 ou Llama-3.1 (illustratif). Les adaptateurs y seraient reconstruits par le bras d'attaque selon son circuit scellé, hors lecture de la défense.

**Calcul (illustratif).**
- Extraction des activations : environ 2 000 épisodes, en deux passages (organisme et base qui relit), avec environ 4 000 jetons par épisode. Cela représente quelques dizaines d'heures-carte de passage avant.
- Stockage : on ne garde que les couches et positions préenregistrées. Sur toutes les couches, le volume atteindrait des centaines de mégaoctets par épisode.
- Sondes, matrices et jeu : processeur. L'arène est rejouable sur processeur [question].
- X3 (substitution) : environ 20 à 50 heures-carte.
- X5 et X6 (générations du bras rouge) : le coût dominant. Environ 5 à 15 heures-carte par génération, pour au moins 4 générations × 2 conditions, plus le panel.

**Coût total illustratif** : environ 150 à 400 heures-carte, soit environ 400 à 1 200 USD à 2 à 3 USD l'heure (illustratif). Le seul coût issu des faits est la consultation d'Argon sur la convergence : 1,82 USD [rel.].

**Délai illustratif.**
- X0–X2 : 2 à 3 semaines, une fois le placebo construit.
- X3 : 1 semaine.
- X5–X6 : dépendent du bras rouge, non chiffrables depuis les faits.

**Pièces produites.**
- Une table scellée par expérience, avec l'empreinte de chaque fichier de scores par jeton (format `scores-p3.npz` [question]).
- Le script de recalcul des intervalles.
- L'ordre de lecture des familles tenues à l'écart, scellé avant G1.

---

## Ce que cette proposition ne fait pas

- Elle ne décrit **aucun** procédé de sabotage, d'évasion ou de construction de saboteur.
- Toute pression d'attaque (X5, X6) est déléguée au bras rouge sous circuit scellé ; la défense ne reçoit que des adaptateurs et des épisodes.
- Elle n'interprète la figure 4a de 2609.36490 [R] que comme un prior.
- Elle ne traite aucune lecture de l'arène comme un verdict.

**Ce qui réfuterait l'ensemble de la proposition** [H] :
- X0a donne H_B sur la strate diffuse, ce qui suspend tout le reste.
- Ou X1 ne passe que sur la famille (i) et X2 donne H_B partout : la « trace » ne serait alors que consigne et identité, et la pince n'a plus de mâchoire interne à évaluer.

FIN-DE-CELLULE
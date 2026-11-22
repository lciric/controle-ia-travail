# Proposition A, Tour III.3 : réponse aux critiques

**État des pièces.** Ma conception III.1 et les cinq critiques (B, C, D, E, F) sont présentes et closes par leur ligne de fin ; aucune ne paraît coupée. Le bloc FAITS reproduit la question et ne contient aucun fait à statut.

**Statuts.** C, E et F apposent « VÉRIFIÉ » à plusieurs de leurs arguments. Je ne modifie pas ces mentions ; je signale qu'aucun fait transmis ne les établit, et je les traite comme des arguments à tester. Mes propres énoncés restent des HYPOTHÈSES. **Tous les seuils, tailles et coûts sont illustratifs.**

**Périmètre et notation.** Je ne réponds qu'aux sections « Sur la proposition A ». « B.a1 » désigne la critique B, partie (a), point 1 (pour D, qui ne numérote pas, j'indique l'expérience visée). « E2′ » désigne mon expérience E2 corrigée.

---

## (a) Décision pour chaque critique

| # | Critiques | Objet | Décision | Suite |
|---|---|---|---|---|
| 1 | B.a1, C.a1, C.b2, E.a1, E.b4 (début), F.a1, F.b (E2) | E2 sépare peut-être « texte attendu » de « texte surprenant sous le mode qui le lit » | **Acceptée.** E2 tel qu'écrit ne tranche pas. | E2′ : lecture avant l'action, préfixes communs, croisement source × mode, strates de surprise |
| 2 | D.a (E2), D.c | Choisir librement une action sélectionne les préfixes où elle était probable ; mécanisme distinct de la surprise | **Acceptée** | E2′ : mêmes préfixes rejoués dans les deux bras |
| 3 | B.c1 | Texte honnête d'une autre graine, imposé, contre texte honnête en politique | **Acceptée**, comme vérification de montage | E2′, témoin A/A |
| 4 | C.c1, E.c2, F.c1 | Action honnête rare et valide imposée, appariée en surprise ; forçage symétrique | **Acceptée.** Le forçage symétrique devient le croisement d'E2′. L'action rare imposée ne sert qu'à l'analyse secondaire après action. | E2′ |
| 5 | B.a1 (2ᵉ point) | Instruction présente d'un seul côté | **Acceptée.** Le témoin inerte existait ; il ne suffit pas. | Ajout d'une instruction active bénigne |
| 6 | C.a3, C.c3, E.a1, F.a3 | Identité des poids LoRA ; LoRA témoin non intégrée aux contrastes | **Acceptée** | Règle R5 |
| 7 | F.c3 | LoRA à déclencheur bénin | **Transformée en test** | E2′, E3′ |
| 8 | E.c1 | Saboteur entraîné sans déclencheur ni instruction, jugé indispensable | **Rejetée pour la première chaîne.** Avec un seul adaptateur par classe, ce contraste est exactement confondu avec l'identité des poids, défaut que E relève lui-même. | Reportée en E6, avec plusieurs adaptateurs indépendants |
| 9 | B.a2, B.c2, C.a4, C.b1, E.a4 (collisionneur), E.b3, F.a2, F.c2 | E1 favorisé d'avance : les erreurs honnêtes tombent sur des états difficiles | **Acceptée** | E1′ : mêmes états sous les deux modes |
| 10 | C.c2 | Décodeur sur la couche d'enchâssement pour soustraire la difficulté | **Rejetée comme correction, gardée comme plancher.** Soustraire l'exactitude d'un second décodeur ne corrige pas un décalage de covariables. L'égalité des états le supprime par construction. | E1′ |
| 11 | D.a (E1), E.a2, E.c3 | Lecture après l'action : le dernier jeton ré-encode l'action écrite | **Acceptée** | Règle R4 |
| 12 | B.a3, B.c3 | Un lecteur d'une autre famille ne borne pas l'information textuelle | **Acceptée** | V7′ : même modèle, mêmes poids, relisant sans instruction ni déclencheur |
| 13 | E.a3 | Base texte et V7 à 0,5 sont des identités, pas des témoins | **Acceptée.** Reclassées « vérifications de montage ». La base texte informative est celle d'E4′. | E4′ |
| 14 | C.a2, F.a3 | V4 suppose de connaître les jetons de l'instruction ou du déclencheur | **Acceptée.** V4 n'est pas une méthode « texte seul ». | V4 retirée des bases à battre |
| 15 | B.a4, D.c, F.b (E3) | E3 peut n'effacer que la représentation de l'instruction ; directions aléatoires insuffisantes | **Acceptée** | E3′ |
| 16 | B.b, D.b, E.b5 | Rapports à dénominateur instable (E3, E5) | **Acceptée** | Règle R6 |
| 17 | B.a5, B.c4, D.a (sélection), E.a4 (2ᵉ point), F.a4, F.b (max) | Fuites entre sélection et verdict ; permutation au niveau action ; maximum de huit bases pris sur le test | **Acceptée** | Règle R1 |
| 18 | B.a6 | La position du pas est un confondant | **Acceptée** | Même créneau de décision dans les deux bras ; classifieur « position seule » ajouté aux bases |
| 19 | D.a (E0), D.b | Apparier avant d'estimer la dégradation efface l'effet | **Acceptée.** Mon « toujours » sur la classe négative était fautif pour E0. | E0′ : deux populations |
| 20 | D.c, F.a3, E.b2, F.b (E0) | Le sabotage déclaré est un témoin positif et ne teste que l'aveu ; atomes du score | **Acceptée** | E0′ |
| 21 | B.b, E.a4, E.c3 | Positivité de l'appariement ; appariement par instance | **Acceptée** | Règle R3 |
| 22 | B.b, C.b4, E.b6 (début), F.b | Incertitude du quantile, effectif efficace, loi de la longueur | **Acceptée** | R1, R7 ; critère à 5 % seul |
| 23 | E.b1 | Zones entre deux seuils jamais tranchées | **Acceptée** | Règle R2 |
| 24 | C.b3 | V2 peut s'inverser | **Acceptée.** L'hypothèse de signe était marquée comme telle ; elle est retirée. | V2 bilatéral, signe appris sur développement |
| 25 | D.b (E4) | Loi jointe des vérifications ; plafond si la base détecte déjà presque tout | **Acceptée** | E4′ : combinaison apprise, porte de plafond |
| 26 | D.b, E.b4 (fin) | L'échec de transfert d'une direction ne réfute pas un calcul commun | **Acceptée.** Restreint ce que H_B falsifie. | E2′ |
| 27 | D.b (E1) | Un décodeur qui échoue n'établit pas l'absence d'information | **Acceptée.** Mon « H_B réfute la nécessité de C1 » était trop fort. | E1′ : test comportemental d'évitement |
| 28 | B.b (E1), F.b (E1) | Puissance nulle si les pas de commission ciblée sont rares ou latents | **Transformée en porte d'effectif** | E1′ |
| 29 | D.b, D.c, E.b7, F.a3 (E5) | E5 ne sépare ni plan hérité et mode ré-inféré, ni pas unique et activité continue, ni texte et réactivation par l'adaptateur | **Transformée en tests** | E5′ |
| 30 | F.c4, E.b6 (fin) | Pic bénin isolé ; dilution si un seul pas dévie | **Transformée en test** | E4′ |
| 31 | B (dans sa section sur F) | Divergence de titre sur *AI Control*, d'année sur Levinstein & Herrmann | Je ne tranche pas. Toutes mes références étaient citées de mémoire. | Ces deux-là : **référence à vérifier** |

**Ce que les critiques changent au fond.** Deux de mes conclusions prévues étaient mal fondées :

- **E2.** Un résultat positif aurait pu ne refléter que la surprise (lignes 1 et 2).
- **E1.** Un positif était favorisé par la difficulté (ligne 9), et un négatif ne réfutait pas ce que je disais (ligne 27).

---

## (b) Expériences corrigées

### Règles communes

- **R1, partage.** Trois lots disjoints de familles de tâches : développement, étalonnage, test.
  - Gelés sur développement : couche, agrégation, combinaison des vérifications, direction d'ablation.
  - Seuil de fausses alertes : fixé sur étalonnage. Verdict : sur test.
  - Permutations et rééchantillonnage au niveau famille ; le rééchantillonnage ré-estime le seuil.
- **R2, décision.** Un seuil unique τ par critère. H_A si l'intervalle à 95 % est entièrement au-dessus, H_B s'il est entièrement au-dessous. À cheval : non tranché, avec une seule réplication à effectif doublé, annoncée d'avance.
- **R3, instances.** Les mêmes instances sont soumises à tous les régimes, avec plusieurs graines honnêtes par instance. Deux classes négatives sont rapportées séparément :
  - les honnêtes avec erreurs d'ampleur comparable, avec la couverture de l'appariement publiée ;
  - toutes les honnêtes.
- **R4, position.** Lecture principale à la dernière position avant le premier jeton de l'action. La lecture après action est secondaire.
- **R5, poids.** En régime déclencheur, le négatif principal est le même adaptateur avec un déclencheur leurre. S'y ajoutent deux adaptateurs de même recette et de même volume : un honnête, et un « bénin » dont le déclencheur commande un changement de style sans dégradation.
- **R6, effets.** Différences absolues par bras, avec intervalle. Pas de rapport.
- **R7, longueur.** Nombre de créneaux de décision fixe par famille, pour que l'agrégation ne lise pas la longueur.

### E0′ : l'organisme sabote-t-il de façon défendable ?

- **H_A.** Deux conditions :
  - sur toutes les assignations, sans appariement, l'écart de qualité finale honnête − sabotage dépasse τ = 15 points ;
  - l'écart de signalement par action (actions sabotées − erreurs honnêtes) est sous τ = +5 points.
- **H_B.** L'un des deux critères tombe de l'autre côté.
- **Témoins positifs du moniteur.** Sabotage déclaré signalé à ≥ 90 % ; fautes grossières non déclarées, injectées, signalées à ≥ 80 %. Sinon le moniteur est aveugle et E0′ ne dit rien.
- **Mesure.** Ex æquo randomisés ; taux de fausses alertes réalisé publié.
- **Porte.** Couverture de l'appariement (R3) ≥ 50 %. Sinon le jeu apparié est atypique et les expériences de détection ne sont pas jugeables.
- **Falsification.** H_A réfute « ce modèle ne peut pas servir d'organisme ». H_B réfute P2 pour ce modèle ; on change d'organisme avant toute sonde.

### E2′ : un signal de mode, à préfixe commun, avant l'action

**Montage.** Une banque de préfixes s'arrête juste avant un créneau de décision. Les préfixes ont deux sources : générés en mode honnête, générés en mode sabotage. Chaque préfixe est relu sous les deux modes, cache reconstruit.

- Régime instruit : instruction de sabotage, contre instruction inerte, instruction active bénigne ou aucune.
- Régime déclencheur : même adaptateur, déclencheur contre leurre.

L'étiquette est le mode de lecture, équilibré sur la source, le type et le rang du créneau.

**Raisonnement de montage (HYPOTHÈSE).** À poids et contexte identiques, rejouer un texte redonne les activations de sa génération. L'écart redouté est donc un effet de surprise du texte sous le mode qui le lit. Dans le plan croisé, cette surprise est l'interaction source × mode, pas l'effet principal du mode.

- **H_A.** Une direction apprise dans un régime sépare les modes dans l'autre (AUROC de transfert, τ = 0,70), dans chacune des deux strates de source et dans chaque tercile de surprise cumulée du préfixe. Son taux d'alerte reste ≤ 2 × le nominal sur chacun des témoins.
- **H_B.** Le transfert est sous τ, ou le signal n'existe que dans les cellules où source et mode discordent, ou un témoin tire autant que le sabotage réel.
- **Témoins.** Instruction inerte ; instruction active bénigne ; leurre ; adaptateur honnête avec déclencheur ; adaptateur bénin avec déclencheur ; A/A de B.c1 ; étiquettes permutées par famille.
- **Falsification.**
  - H_A réfute « on ne lit que la présence d'une consigne, les poids ou la surprise ».
  - H_B réfute « une direction linéaire commune aux deux régimes ». Il ne réfute pas un calcul commun (ligne 26).
- **Repli si H_B.** Sondes propres à chaque régime, chacune contre ses témoins, et transfert causal en E3′.
- **Limite.** E2′ établit au mieux la variable de mode M, pas un calcul par pas.

### E1′ : l'information sur la bonne action est-elle utilisée (C1) ?

**Volet comportemental, sans sonde (ajout, ligne 27).** Pour chaque état commun, on rééchantillonne l'action sous les deux modes.

- **H_A.** Sur les états où le mode honnête émet la bonne action à ≥ 80 %, le mode sabotage l'émet moins souvent que le hasard parmi les *m* actions défendables (taux − 1/*m*, τ = 0).
- **H_B.** L'intervalle est entièrement au-dessus de 0 : la bonne action n'est pas évitée plus que par un tirage aveugle.
- **Falsification.**
  - H_A réfute « on dégrade sans information sur la bonne action » pour cet organisme. Éviter la bonne action mieux que le hasard exige une information sur elle, où qu'elle soit calculée.
  - H_B réfute C1 comme nécessaire sur ce banc et rend plausible l'imitation d'un plus faible (F2).

**Volet décodeur.** Le décodeur est entraîné en mode honnête sur les familles de développement. On le lit en mode sabotage sur les mêmes états, avant l'action. La comparaison porte sur l'ensemble des états où les conduites divergent, défini par le rééchantillonnage.

- **H_A.** Exactitude sabotage − exactitude honnête au-dessus de τ = −10 points.
- **H_B.** Au-dessous de τ.
- **Plancher.** Décodeur de couche précoce et étiquettes permutées.
- **Porte.** Au moins 200 états divergents en test, sinon non jugeable.
- **Falsification.** H_A réfute « la bonne action cesse d'être représentée quand on sabote ». H_B réfute seulement « C1 est lisible linéairement, à cette position, par un décodeur honnête ».

### E3′ : la direction est-elle utilisée, et est-elle autre chose que « suivre une consigne » ?

La direction et la couche sont gelées sur développement.

- **H_A.** L'ablation réduit l'écart de qualité sous sabotage d'au moins τ = 8 points, sans perte honnête au-delà de 2 points, et laisse intact l'effet de l'instruction bénigne et du déclencheur bénin.
- **H_B.** Le gain est sous τ, ou l'ablation efface autant les conduites bénignes.
- **Témoins.** Au moins 100 directions aléatoires ; direction témoin appariée en variance retirée ; directions « difficulté » et « erreur présente ».
- **Transfert causal.** La direction d'un régime est ôtée dans l'autre.
- **Suffisance.** Inchangée : l'ajout doit produire une dégradation défendable au sens d'E0′.
- **Falsification.** H_A réfute « pur corrélat » et « représentation générique de consigne active ». H_B réfute « on lit une variable causale propre au sabotage ».
- **Réserve maintenue.** Un succès établit M, pas le calcul par pas.

### E4′ : la lecture interne ajoute-t-elle au texte, en politique ?

Le verdict porte sur le **régime déclencheur**. En régime instruit, lire le mode revient en partie à lire l'invite ; ce régime est rapporté à part.

- **Base.** Combinaison logistique de V1, V2, V3, V5, V6, V7′ et V8 (dont « position seule »), apprise sur développement avec le même budget d'étiquettes que la sonde.
- **Lecture interne.** Sonde d'E2′ gelée, lue à tous les créneaux, agrégée par moyenne des trois scores les plus élevés.
- **Métrique.** Gain de détection à 5 % de fausses alertes : (base + interne) − base, sur test.
- **H_A.** Gain entièrement au-dessus de τ = +5 points.
- **H_B.** Gain entièrement au-dessous.
- **Fausses alertes publiées par strate.** Honnêtes avec erreurs ; toutes honnêtes ; leurre ; adaptateur bénin ; trajectoires honnêtes à pas atypique isolé non dégradant (≤ 2 × le nominal).
- **Porte de plafond.** Si la base dépasse 85 % de détection, le banc ne discrimine pas ; on durcit le sabotage avant de conclure.
- **Rapport par forme.** Pour le cadrage précoce (F4), j'attends un gain faible ; ce serait cohérent avec le point 5, pas un échec de la lecture en général.
- **Falsification.** H_A réfute « le texte et les vérifications suffisent » sur ce banc. H_B réfute l'intérêt pratique de cette lecture, même si E2′ est positif.

### E5′ : mode actif à chaque pas, ou plan hérité du texte ?

**Montage.** Plan croisé, cache reconstruit dans toutes les cellules : source du préfixe (sabotage ou honnête) × mode après le pas *k* (présent ou retiré), pour deux valeurs de *k*. Deux bras s'ajoutent :

- **Boule de neige honnête** : un agent honnête poursuit un préfixe honnête contenant le même mauvais choix précoce.
- **Échange d'adaptateur** (régime déclencheur) : après *k*, on poursuit avec l'adaptateur honnête.

**Porte.** Écart sabotage continu − honnête ≥ 15 points ; sinon non jugeable.

- **H_A.** Après retrait, le taux d'actions dégradées retombe au niveau du bras boule de neige (différence sous τ = +5 points). Et le mode ajouté sur préfixe honnête fait dégrader dès *k*. Le mode agit à chaque pas.
- **H_B.** Après retrait, le taux reste au-dessus du bras boule de neige de plus de τ : le texte suffit à réactiver la conduite.
  - Si l'effet disparaît sous échange d'adaptateur, c'est une réactivation par les poids appris.
  - Sinon, c'est une ré-inférence par le modèle de base.
- **Falsification.** H_A réfute « plan porté par le seul texte » sur ce banc. H_B réfute l'utilité d'une lecture limitée au pas de décision.
- **Limite (D.b).** Si plan hérité et mode ré-inféré donnent la même loi d'actions, le comportement ne les sépare pas. Seule la sonde d'E2′, lue après retrait, le pourrait.

### E6 (reportée) : saboteur inconditionnel

Elle exige plusieurs adaptateurs indépendants par classe (au moins 4 + 4), avec test sur adaptateurs inédits. Elle sort du budget de la première chaîne.

### Ordre et coût

1. E0′, E5′ et le volet comportemental d'E1′ : aucune sonde.
2. E2′.
3. E4′.
4. E3′ et le volet décodeur d'E1′.

Deux adaptateurs de plus et les rééchantillonnages portent le total à 200 à 400 heures-GPU.

---

## (c) Réponse à l'arbitre

### Ce qui est établi

Rien d'empirique. Le bloc FAITS ne contient aucun fait à statut, et aucune pièce ne rapporte de mesure. La littérature de mon point 2 est RAPPORTÉE, citée de mémoire et à vérifier ; deux de ses références sont désormais explicitement « à vérifier ».

La lecture des pièces établit un seul point : mon plan initial ne contenait pas les contrôles qui auraient écarté la surprise, l'identité des poids et la difficulté. Que ces confondants auraient réellement opéré reste une HYPOTHÈSE.

### Ce qui ne l'est pas (tout est HYPOTHÈSE)

1. **Calculs nécessaires.** La nécessité n'est pas établie, et l'expérience ne peut que la réfuter par contre-exemple. Je tiens deux raisonnements :
   - Si les mêmes poids font mieux dans une condition voisine, une information de mode intervient entre l'entrée et la sortie. Cela n'implique pas qu'elle soit localisée ou lisible linéairement.
   - Si l'agent évite la bonne action mieux que le hasard, il utilise une information sur elle.

   Les autres calculs dépendent de la forme de dégradation (commission, imitation, omission, cadrage précoce). Ce qui me ferait changer d'avis : E1′ côté H_B, ou un organisme qui dégrade de façon ciblée sans variable de mode détectable par intervention.
2. **Publié.** Je ne connais pas de résultat établissant une nécessité, ni de lecture interne évaluée contre des erreurs honnêtes sur de longues tâches d'agent. C'est mon ignorance, à lever par recherche bibliographique.
3. **Mode d'acquisition.** Je suppose que la réponse en dépend.
   - Instruit : lire le mode revient en partie à lire l'invite.
   - Déclencheur appris : c'est le seul régime où « mieux que le texte » est testable proprement.
   - Inconditionnel : possiblement rien à lire ; non testé avant E6.
4. **Calcul ou accompagnement, mieux que le texte.** Les critères sont ceux d'E2′ à E4′ :
   - signal avant l'action, à préfixe commun ;
   - signal absent des témoins : consigne inerte, consigne bénigne active, leurre, adaptateurs honnête et bénin ;
   - signal causal et distinct d'une consigne quelconque ;
   - gain ajouté à une base apprise qui inclut le même modèle relisant sans consigne.

   Une sonde qui tire sur un témoin me ferait conclure qu'on lit autre chose.
5. **Rien à lire.** Mes six cas du tour III.1 sont inchangés. Les critiques en ajoutent un : quand plan hérité et mode ré-inféré donnent la même loi d'actions.
6. **Portée.** Le banc a 15 à 30 actions, pas des centaines. L'entraînement adverse contre la sonde et le sabotage par stratégie propre ne sont pas testés.

### L'expérience à faire en premier

La chaîne **E0′ → E2′ → E4′**, sur un modèle ouvert de 7 à 9 milliards de paramètres, avec le verdict en régime déclencheur.

- **Vaut d'être poursuivie** : E0′, E2′ et E4′ donnent tous trois H_A.
- **Ne le vaut pas**, pour la lecture linéaire avant l'action sur ce banc : E0′ donne H_A, puis E2′ ou E4′ donne H_B. E2′ côté H_B, c'est un signal qui tire sur les témoins ou n'existe que par la surprise. E4′ côté H_B, c'est un gain sous le seuil.
- **Organisme inadéquat** : E0′ donne H_B, ou une porte échoue (couverture, plafond, effectif). Ce n'est pas un résultat négatif sur la question, et je l'annonce avant de mesurer.

Aucune de ces issues ne dit si un calcul est nécessaire. Elles disent si, sur cet organisme, il y a quelque chose à lire que le texte ne donne pas.

FIN-DE-CELLULE
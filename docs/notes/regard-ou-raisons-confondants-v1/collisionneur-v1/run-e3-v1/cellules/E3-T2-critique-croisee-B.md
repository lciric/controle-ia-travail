

# Proposition B — Tour III.2 : critique croisée de méthode

Tout constat du projet reste **RAPPORTÉ** via [B]. Les mécanismes, probabilités et jugements ci-dessous sont des **HYPOTHÈSES** sauf mention. Les seuils chiffrés sont **illustratifs**.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **Signature positive sous-spécifiée probabilistiquement.** A exige trois observations conjointes (sélectivité par justification, transfert aux nuisances dérivables, causalité de la trace). Mais aucun modèle statistique ne relie ces trois observations : on ne sait pas si la conjonction doit être testée en intersection de tests marginaux (contrôle familial du risque), en test omnibus, ou par construction d'un score composite. Sans cela, la probabilité de déclarer la signature « obtenue » par hasard croît avec le nombre de strates et d'adaptateurs — trois tests marginaux à α = 0,05 donnent un risque familial de ~14 % (illustratif) sans correction.

2. **La rivale 4 (dose) confond deux estimands.** L'expérience proposée — balayage du facteur d'échelle de l'adaptateur LoRA — suppose que le gain comportemental est une fonction lisse du facteur d'échelle. Or la mise à l'échelle d'un delta LoRA multiplie *toutes* les composantes (y compris celles qui encodent style, registre ou refus), pas seulement la « dose de raisons ». La colinéarité entre deltas mesure la similarité géométrique des adaptateurs, non la contribution de la dose au gain comportemental. Un cosinus élevé entre deltas ne falsifie ni H_A ni H_B de la rivale 4 : deux adaptateurs ayant des contenus fonctionnels distincts peuvent être colinéaires si le rang est petit. **Variable confondante : le rang LoRA contraint la géométrie indépendamment du contenu.**

3. **L'expérience décisive (paires de justification) n'oppose pas réellement H_A et H_B telles que formulées.** A définit H_A comme « raisons » et H_B comme « surface ou refus généralisé » — deux mécanismes distincts regroupés dans un seul bras. Si Sel est basse, on ne sait pas si c'est H_B₁ (surface) ou H_B₂ (refus généralisé) qui est vraie, ni si c'est l'une des deux. L'inférence forte (B4) exige deux hypothèses exclusives, pas une disjonction sous H_B.

4. **Pas de contrôle de la compréhension des variantes légitimes.** Le seuil Sel ≥ 0,4 avec borne inférieure > 0,15 présuppose que le modèle comprend la différence entre « exfiltration » et « migration autorisée ». Sans un test indépendant de compréhension (le modèle identifie-t-il correctement qui est autorisé dans chaque variante ?), une Sel élevée peut refléter un détail de formulation plutôt que l'usage de la raison. **Fuite potentielle : si la variante « légitime » contient un mot-signal d'autorisation que la variante nuisible ne contient pas, la sélectivité mesure le mot, pas la raison.**

5. **Rivale 8 (contamination) invoque des données non accessibles.** A note « si les données d'entraînement sont accessibles (non établi dans les faits) ». Sans elles, la rivale est un placeholder. Or A la classe en huitième position plutôt que de la marquer comme non testable — ce qui biaise l'impression de complétude.

### (b) Conditions de perte de puissance

- **Paires de justification (Sel).** Soit π_L = P(exécute | légitime) et π_N = P(exécute | nuisible). Sel = π_L − π_N. Si la recette avec raisonnement est au plancher pour les deux (π_L ≈ π_N ≈ 0,03, illustratif), alors Sel est bornée par ~0,03 et l'intervalle couvre nécessairement 0, quel que soit le nombre de tirages. **Condition formelle : si min(π_L, 1−π_N) < δ_min, le test de Sel ne peut atteindre la borne inférieure requise.** Pour 30 tirages par condition et π_L = 0,10 (illustratif), l'écart-type de Sel est ~0,08 (illustratif) : la borne inférieure de l'IC à 95 % ne dépasserait 0,15 que si Sel ≥ 0,31 — la zone « non concluante » est plus large que présentée.

- **S et D (rivale 7).** A identifie correctement le problème du plancher. Mais ne formalise pas la condition : si A(observé) < k√(1/n) (où k est un facteur lié au quantile normal et n le nombre de tirages), alors S est dominé par le bruit de dénominateur et D hérite d'une variance explosive. Le rééchantillonnage par scénario ne corrige pas le biais de ratio.

- **Mise à l'échelle des adaptateurs (rivale 4).** Si le facteur d'échelle déplace le modèle hors du bassin d'attraction du régime d'inférence (par ex. facteur > 1,5), la courbe de performance peut devenir non monotone par artefact d'extrapolation, pas par saturation causale. La puissance du test dépend de la monotonie locale, qui n'est pas garantie.

### (c) Contrôles négatifs fatalement absents

- **Compréhension des variantes.** Sans vérification que le modèle distingue correctement le statut d'autorisation dans chaque paire (légitime vs nuisible), le test est circulaire. Un contrôle négatif manquant : soumettre les variantes à un modèle de départ sans adaptation et vérifier que la description de la situation (sans demander d'agir) est correctement résumée.

- **Effet du style de la variante légitime sur le juge.** Si le juge est plus indulgent envers une sortie qui mentionne une autorisation (même quand l'action n'est pas exécutée), Sel est gonflée. Il faut un contrôle négatif du juge : épisodes où le modèle mentionne l'autorisation mais ne fait pas l'action légitime — le juge ne doit pas compter cela comme une exécution.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **L'expérience décisive (greffe croisée de traces) a un confondant majeur : la cohérence contexte-trace.** Quand on préremplie la réponse de l'assistant avec une trace provenant d'un autre modèle ou d'un autre épisode, le modèle complétant détecte potentiellement l'incohérence stylistique ou factuelle entre la trace greffée et le prompt. La « résistance » de la recette avec raisonnement à une trace corrompue (T_corrompue) pourrait venir de la détection de cette incohérence, pas de la causalité des raisons encodées dans les poids. **Fuite : la compétence de détection d'incohérence est une variable confondante non contrôlée.**

2. **Le seuil de falsification est asymétrique sans justification probabiliste.** C exige τ < 10 % pour T_sûre sur la jumelle (falsifier H_B), mais τ ≥ +20 points pour T_corrompue sur la recette avec raisonnement (falsifier H_A). Le seuil de 10 % est absolu, le seuil de 20 points est relatif au plancher (~quelques %). Si le plancher est à 3 %, +20 points donne 23 % — un seuil beaucoup plus facile à atteindre que le 10 % absolu pour l'autre bras. **L'asymétrie rend la falsification de H_A plus probable que celle de H_B par construction.**

3. **Rivale 6 (paradoxe de l'instruction d'invariance) est intéressante mais le test proposé ne discrimine pas.** C propose de mesurer si les recettes « règles » ont une activation plus élevée de la sonde d'évaluation. Mais si ces recettes n'ont pas de gain lisible (RAPPORTÉ), une sonde activée ne prouve rien sur le mécanisme du gain — elle montre seulement que la mention explicite augmente la saillance. Le test est informatif sur l'encodage, pas sur l'explication du gain, qui est le sujet.

4. **Le parseur syntaxique déterministe (rivale 8) est présenté comme un étalon-or implicite.** Or un parseur qui cherche l'appel d'outil exact manque les cas d'exécution partielle, de tentative avortée, ou d'exécution par contournement (appel d'un outil différent aboutissant au même effet). **Il surévalue les refus par défaut technique.** Sans annotation humaine des cas de désaccord (mentionnée, mais en effectif « illustratif » de 100), le parseur n'est pas un contrôle négatif du juge — c'est un second instrument biaisé dans la direction opposée.

5. **La section sur le papier recommande de présenter le résultat nul de la phrase comme « contribution méthodologique majeure ».** Or les faits indiquent que le contraste dépend des mots et que l'écart entre formulations est net (RAPPORTÉ). Un résultat dont le signe et l'ampleur changent selon le choix de mots n'est pas un résultat nul robuste — c'est un résultat instable. Le présenter comme contribution majeure sans d'abord caractériser cette instabilité serait prématuré.

### (b) Conditions de perte de puissance

- **Greffe croisée.** Soit τ_0 le taux de base de la recette avec raisonnement (~0,03, illustratif, RAPPORTÉ). Sous H_A, T_corrompue devrait faire monter τ à τ_0 + 0,20 = 0,23 (illustratif). Pour 27 scénarios × 30 tirages = 810 épisodes (illustratif), l'écart-type de τ̂ est ~√(0,23×0,77/810) ≈ 0,015 — l'effet est détectable. Mais si T_corrompue est détectée comme incohérente et ignorée par le modèle (voir (a)1), l'effet observé est 0 et on conclut en faveur de H_B **par artefact de cohérence**, pas par causalité des poids. **Condition formelle : si P(modèle détecte incohérence de la trace greffée) > 1 − puissance, le test est aveugle.**

- **Rivale 5 (plancher en log-odds).** C propose un modèle linéaire généralisé mixte. Mais si le nombre de scénarios est 27 avec effets aléatoires par scénario et 9 conditions de but, le nombre de groupes est faible (3 actions × 9 conditions = 27 cellules). Les estimations des composantes de variance seront instables. **Condition : si la variance inter-scénarios >> variance intra-scénarios, le nombre effectif d'unités est ~3 (les actions), pas 27, et les intervalles explosent.**

- **Rivale 3 (rotation de sous-espace).** Le seuil de 0,85 en cosinus (illustratif) pour valider le transport est arbitraire. Pour un sous-espace de dimension d > 1, le cosinus entre vecteurs uniques perd son sens ; il faut un angle de Grassmann ou un indice de sous-espace. **Si d > 1 et que C utilise le cosinus d'un seul vecteur principal, la mesure ignore les rotations dans le complément, et une validité apparente (cosinus > 0,85) peut masquer un transport échoué.**

### (c) Contrôles négatifs fatalement absents

- **Pour la greffe croisée : une trace auto-générée mais corrompue.** Plutôt que transplanter la trace d'un autre modèle (qui introduit un confondant de cohérence), il faudrait faire générer à la recette avec raisonnement elle-même une trace sur un prompt modifié (où l'action est légitime), puis greffer cette trace auto-produite sur le prompt original nuisible. L'absence de ce contrôle rend la greffe inter-modèles non interprétable.

- **Pour le paradoxe d'invariance (rivale 6) : un modèle entraîné sur une spécification qui mentionne l'évaluation mais sans raisons.** Sans ce contrôle, on ne peut pas séparer « la mention de l'évaluation augmente la saillance » de « la mention de l'évaluation interagit avec les raisons ».

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Le tableau de suppositions (section 1) est exhaustif mais ne hiérarchise pas.** Dix suppositions sont listées au même niveau. Or certaines sont vérifiables avec les épisodes existants (la stabilité de S sous bootstrap), d'autres nécessitent un réentraînement (l'appariement des jumelles en tokens). Mélanger les deux niveaux sans ordre de priorité risque de paralyser le projet avec des desiderata non satisfaisables.

2. **L'expérience décisive (corruption de traces) est quasi-identique à celle de C, avec les mêmes confondants.** D propose « raisons permutées entre scénarios, raisons rendues non pertinentes et tokens neutres de longueur appariée ». C propose « T_sûre, T_corrompue, T_neutre ». La permutation de raisons entre scénarios est un progrès par rapport à C car elle conserve le style et le registre du même modèle — mais elle conserve aussi le *format* de la trace (balises de pensée, structure argumentative). **Si le format suffit (ce que D prétend tester), les raisons permutées gardent ce format et la perte L sera faible même si H_A est vraie mais que le format contribue à 50 % du gain.** Le test ne sépare pas contenu et format.

3. **La signature positive (double dissociation causale) exige des « actions non nommées dans la spécification mais déductibles de ses raisons ».** C'est le test le plus discriminant proposé dans toutes les propositions. Cependant, D ne spécifie pas comment juger qu'une action est « déductible des raisons » de façon indépendante du modèle testé. Si le jugement est fait par un autre LLM ou par les auteurs, la déductibilité est elle-même une HYPOTHÈSE non contrôlée. **Il faut un critère opérationnel externe : par exemple, un panel humain identifie les actions déductibles avant de voir les résultats.**

4. **La validation des instruments (section 3) fixe des seuils croisés (détection ≥ 90 %, fausses alertes ≤ 5 %, illustratif) mais pas de budget d'erreur global.** Si six instruments doivent chacun passer un seuil, la probabilité que tous passent diminue même sous l'hypothèse que tous sont valides. Sans règle de décision pour les cas où un instrument échoue mais pas les autres, le papier ne peut pas conclure. **Un protocole de décision conditionnel est nécessaire.**

5. **L'ordre recommandé pour le papier place « résultats comportementaux et dépendance aux mots » avant « juge, plancher et similarité ».** Si l'audit du juge révèle un biais grave, les résultats comportementaux précédents deviennent non interprétables. L'ordre logique serait l'inverse : valider d'abord les instruments, puis présenter les résultats.

### (b) Conditions de perte de puissance

- **Corruption de traces.** D définit L = G_intact − G_corrompu, avec seuil de 5 points (illustratif). Si G_intact est lui-même estimé avec une incertitude de ±4 points (illustratif, pour un taux de ~5 % sur 810 épisodes), alors l'intervalle de L inclut nécessairement [-3, 13] (illustratif) même sous un vrai effet de 5 points. **Condition de puissance : la précision de G_intact doit être < δ/3 pour que le test ait une puissance raisonnable (~80 %, illustratif). Avec un plancher à ~5 % et 810 épisodes, σ(G) ≈ 1,5 points (illustratif) — le seuil de 5 points est alors testable.** Mais si le nombre d'épisodes par condition de corruption est plus faible (27 scénarios × 30 tirages / 4 conditions = ~200 par condition), σ(G) ≈ 3 points et la puissance chute sous 50 % (illustratif).

- **Transport base → adaptateurs.** D demande que « la perte de transport ne dépasse pas 5 points de détection ». Si la précision de détection du sondeur est estimée sur ~200 textes d'évaluation (illustratif), l'écart-type du taux de détection est ~3,5 % (illustratif). L'intervalle couvre facilement 5 points. **Si le corpus de validation est trop petit, aucun seuil de transport n'est discriminant.**

- **Graines et bootstrap hiérarchique.** D recommande un bootstrap hiérarchique par scénario. Avec 27 scénarios et 3 actions, le niveau effectif du bootstrap est ~3 clusters d'actions. Le nombre de rééchantillonnages de clusters est 2^27 ≈ 10^8 pour la combinatoire complète, mais les 3 actions créent une corrélation intra-cluster forte. **Si la corrélation intra-action est > 0,5 (illustratif), le nombre effectif d'observations indépendantes est bien inférieur à 27, et les intervalles par bootstrap hiérarchique sont trop étroits si le clustering est fait au niveau des scénarios plutôt que des actions.**

### (c) Contrôles négatifs fatalement absents

- **Pour la corruption de traces : une condition « raisons pertinentes mais dans un format différent ».** D ne propose pas de dissocier contenu et format. Un contrôle négatif essentiel : les raisons correctes, extraites de la trace puis reformulées dans un style différent (liste à puces vs prose argumentative), greffées avant l'action. Si le format suffisait, la reformulation dégraderait la performance — son absence dans le protocole rend L non interprétable.

- **Pour l'organisme témoin : un organisme dont la conduite ne dépend PAS du regard mais qui a un gain d'alignement.** Sans ce contrôle, on ne peut pas distinguer « l'intervention détruit tout gain » de « l'intervention détruit spécifiquement la composante regard du gain ».

---

## Sur la proposition E

### (a) Défauts de méthode

1. **La métrique de l'expérience décisive est opaque.** E définit d comme « la différence [entre jumelles] du score de proportion de paires où les deux actions sont appropriées, moins la fréquence de changements injustifiés dans des paires témoins ». C'est un score composite à trois niveaux d'emboîtement (paires → proportion → différence entre jumelles), dont la distribution sous l'hypothèse nulle n'est pas caractérisée. **Sans une formulation probabiliste explicite, la puissance du test est inestimable et le seuil δ = 10 points est arbitraire non pas par choix mais par impossibilité de calibration.**

2. **Le principe de décision (d ≥ δ vs d < δ) est unilatéral mais la question est bilatérale.** E oppose H_A : d ≥ 10 et H_B : d < 10. Mais si d = −15 (illustratif) — c'est-à-dire si la jumelle sans raisonnement est *plus* sélective que celle avec raisonnement — le cadre classe cela dans H_B sans signaler l'anomalie. **Un test bilatéral ou au minimum une règle de diagnostic pour d << 0 est nécessaire.**

3. **La rivale 5 (déférence à l'autorité) est la plus originale des cinq propositions, mais le test proposé a une fuite.** E propose de croiser justification pertinente et attribution de source. Mais dans les scénarios agentiques de [2], l'autorité de l'instruction est déjà une variable du prompt (c'est un des 9 « buts » décrits comme conditions). Si l'attribution décorative d'autorité est corrélée avec le format des conditions de but existantes, le test mesure la familiarité avec les conditions, pas la déférence à l'autorité.

4. **La signature positive exige un transfert « à des situations nouvelles », mais E ne spécifie pas le critère de nouveauté.** La distance d'embedding entre scénarios nouveaux et scénarios d'entraînement peut être manipulée par le choix de l'embedding. Sans un critère indépendant de nouveauté (par exemple : domaine, outils et acteurs absents du corpus d'entraînement de [1]), le transfert peut être mesuré sur des scénarios « nouveaux » qui sont en fait des voisins proches.

5. **Le tableau de validation des instruments est complet mais générique.** E donne des critères de validité pour cinq instruments, sans ancrer les seuils aux paramètres observés du projet. Par exemple, « détection d'un contexte d'évaluation assigné » ne précise pas le taux de base de contextes d'évaluation dans le corpus de validation, qui détermine la pertinence du taux de fausses alertes.

### (b) Conditions de perte de puissance

- **Contraste contrefactuel de justification.** E propose un pilote de 100 paires sur 3 modèles = 600 épisodes (illustratif). La métrique est une différence de proportions appariées entre jumelles. Si la proportion de paires « deux actions appropriées » est p ≈ 0,7 (illustratif) pour la recette avec raisonnement et q ≈ 0,5 (illustratif) pour la jumelle, l'écart d = 0,20. L'écart-type de d sous des paires indépendantes est ~√(p(1−p)/n + q(1−q)/n) ≈ √(0,21/100 + 0,25/100) ≈ 0,068 (illustratif). L'IC à 95 % est [0,07, 0,33] — suffisant pour rejeter δ = 0,10. **Mais les paires ne sont pas indépendantes si elles sont construites à partir des mêmes scénarios de base.** Si les 100 paires proviennent de 3 actions × ~33 variantes, la corrélation intra-action réduit le n effectif. **Condition : si la corrélation intra-action > 0,3 (illustratif), le n effectif est ~30 et l'IC double, rendant le seuil de 10 points à peine discriminant.**

- **Prudence globale (rivale 2).** E propose d = excès de refus bénins. Si le taux de refus bénin de la recette est ~5 % (illustratif, compatible avec RAPPORTÉ : « exécute presque toujours une instruction bénigne ») et celui de la référence ~3 % (illustratif), d = 2 points. L'IC à 95 % pour 100 épisodes bénins est [−2,3, +6,3] (illustratif). **Le test n'a aucune puissance pour détecter un excès de 2 points avec un échantillon de cette taille.** Il faudrait ~1000 épisodes bénins par adaptateur pour atteindre une puissance de 80 % (illustratif).

- **Style devant le juge (rivale 3).** d = G_juge − G_audit. G est un gain (différence de taux entre recette et référence). L'audit humain aveugle, s'il porte sur ~100 épisodes stratifiés, produit un G_audit dont l'IC est ±10 points (illustratif). Alors d ∈ [−10, +10] pour presque tout G_juge réaliste — le test ne tranche jamais. **Condition : pour que d soit informatif, il faut que le nombre d'épisodes audités soit > 4/δ² × σ² — ce qui implique des centaines d'épisodes, pas une centaine, si σ est grand.**

### (c) Contrôles négatifs fatalement absents

- **Pour le contraste contrefactuel : des paires où la différence factuelle change la conduite appropriée mais où les raisons de la spécification ne s'appliquent pas.** Si la recette avec raisonnement est sélective sur ces paires aussi, alors la sélectivité vient d'une compétence générale de raisonnement moral, pas de l'apprentissage spécifique des raisons de la spécification. E ne prévoit pas ce contrôle.

- **Pour la direction non spécifique (rivale 6) : un corpus de validation où le contexte est explicitement « évaluation » mais dans un domaine sans rapport avec la sûreté (par ex. évaluation de performance d'un modèle de génération d'images).** Si la sonde se déclenche aussi, elle encode le mot « évaluation », pas la situation d'évaluation de sûreté. E mentionne « mentions d'évaluation dans un document cité » comme contrôle négatif, ce qui est un bon début, mais ne distingue pas domaine de sûreté et domaine hors sûreté.

---

## Synthèse transversale (observations propres, non fusion)

Toutes les propositions convergent vers la greffe/corruption de traces comme expérience décisive. C'est une convergence légitime, mais elle comporte un angle mort partagé : **aucune proposition ne contrôle explicitement la capacité du modèle à détecter qu'une trace a été greffée.** Si le modèle détecte la greffe (par incohérence de style, de contenu factuel, ou de structure par rapport au prompt), toutes les expériences de greffe mesurent la robustesse à la détection d'incohérence, pas la causalité des raisons.

Un contrôle minimal : après la greffe, demander au modèle « la réflexion précédente est-elle cohérente avec la situation ? ». Si le taux de « non » est élevé pour les traces corrompues mais bas pour les traces intactes, la détection d'incohérence est un confondant actif.

FIN-DE-CELLULE
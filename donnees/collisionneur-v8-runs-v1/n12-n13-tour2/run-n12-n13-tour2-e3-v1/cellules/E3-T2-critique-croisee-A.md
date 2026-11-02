# Proposition A — Tour III.2 : critique croisée de méthode

**Pièces reçues** : B (`05d5e20d…`), C (`399b0b8f…`), D (`2516f13f…`), E (`cbb6772b…`) ; les quatre sont complètes (marqueur de fin présent). Aucune ne cite une pièce que je ne pourrais pas recouper sur la synthèse v2 ou la question v2 ; tout chiffre de dessin cité ci-dessous est celui de la cellule critiquée (« illustratif » chez son auteur) ; tout calcul que j'ajoute est marqué « calcul du critique, illustratif ». Je critique le dessin, pas la position ; quand je reprends un élément d'une autre proposition, je le dis (B1).

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Expérience 2 (Platt) : H_A vraie par construction.** Le critère de décision est « ECE < 0,10 sur ≥ 80 % des familles ». Un prédicteur constant égal au taux de base atteint une ECE voisine de zéro par définition (chaque bac a une confiance égale à la fréquence observée) ; B liste ce prédicteur en contrôle négatif mais ne l'utilise pas dans la règle de falsification. Une recalibration qui ne vaut pas mieux que la constante valide H_A. Il faut un critère **joint** (ECE et gain d'AUROC ou de rappel à point de fonctionnement fixe sur le verdict binaire) ; D et E le font, B non.
2. **Expérience 1 (p₀) : règle incohérente.** Le seuil H_B est « p₀ < 0,30 », la zone grise [0,30 ; 0,40], mais la falsification de H_A est « borne supérieure de Wilson < 0,40 ». Un p̂₀ = 0,35 avec borne supérieure 0,39 tombe à la fois en zone grise et en « H_B tenue ». Les deux règles ne peuvent pas coexister.
3. **Sonde d'omission : fuite entre construction et évaluation.** « Cas honnêtes appariés = traces du bras individuel ». Les négatifs viennent d'autres poids que les positifs : la sonde peut classer le bras, pas l'omission — c'est exactement la famille 3 de la synthèse v2 que B dit avoir adoptée en T3 (A-7). Le critère « rappel > taux de base des omissions + 2 SE » compare un rappel (probabilité conditionnelle aux positifs) à une prévalence : catégories différentes ; le plancher d'un classifieur aléatoire est le taux de fausses alertes fixé, pas la prévalence. Même erreur dans le test de transfert (divergence 9 : « p₀ = taux de base des omissions » comme nul binomial du rappel).
4. **« Canari de pression » : effet installé par construction.** Un scénario où le signalement diminue le score du groupe fait entrer le signalement dans la récompense — contraire à la convergence 6 que B adopte par ailleurs. Il mesure que l'optimiseur suit la récompense, pas que la pression diffuse d'Avalon est reproduite ; comme **contrôle positif hors entraînement principal** il est utile, comme critère d'informativité il importe le défaut mesuré.
5. **Divergence 2 : calcul tautologique.** « Variance en p(1−p)/N pour N contributions i.i.d. Bernoulli » est vrai pour toute moyenne de Bernoulli indépendantes ; il ne dit rien de la variance de sélection sous filtrage par rejet (l'objet de C-T2 a2), qui dépend de la dépendance entre agents d'un même groupe, non modélisée.
6. **Qui lit : seuils en conflit et désaccord non estimable.** Plancher = p₀ − 2σ et chute maximale = 0,20·p₀ : pour p₀ = 0,40 et n = 200, σ ≈ 0,035, plancher ≈ 0,33 et chute admise 0,08 ⇒ seuil effectif 0,32 : le plancher est redondant (calcul du critique, illustratif). Double lecture sur 20 % de 200 scénarios = 40 items ; « désaccord > 5 % » = 2 items ; l'erreur type du taux de désaccord y est de l'ordre de 0,03–0,04 : la règle d'escalade n'est pas jugeable (calcul du critique, illustratif).

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **p₀** : si les scénarios sont tirés de familles paramétriques avec corrélation intra-famille ρ_f et m scénarios par famille, l'effectif efficace est n/(1+(m−1)ρ_f) ; Wilson à n nominal sous-couvre. Non jugeable si p₀ → 0 ou 1 (variance → 0 mais plus de marge de chute) ; B ne borne pas le haut.
- **ECE** : l'estimateur à bacs fixes est biaisé vers le haut d'un terme d'ordre (n_bac)^{−1/2} ; avec des familles de petit effectif, « ECE < 0,10 » devient un test de taille de famille, pas de calibration.
- **McNemar / TOST (expérience 3)** : la puissance ne dépend que des paires discordantes b + c ; si Lean et la suite détectent largement les mêmes erreurs, b + c → 0 et ni H_A ni H_B n'est falsifiable, quel que soit n. B ne fixe ni n ni la règle de comptage des dépassements de temps de Lean (C la fixe : fausse alerte).
- **Test de transfert** : sous le nul correctement posé (rappel = FPR fixé, 5 %), avec n_positifs ≈ prévalence × 100 traces, le nombre de positifs peut être inférieur à 10 : test binomial sans puissance.

### (c) Contrôles négatifs dont l'absence serait fatale

- Platt : le prédicteur constant **dans la règle de décision**, et une confiance permutée **intra-famille** (une permutation globale laisse passer un classifieur de famille).
- p₀ : « rapport déjà émis par un pair » et « outil indisponible » (présents chez D, absents chez B) ; sans eux, un agent qui appelle ρ systématiquement passe.
- Sonde : négatifs des **mêmes poids** ; un classifieur « bras × point de contrôle » comme plancher à battre.
- Lean : énoncés sains renotés (E) ; sans eux, une fausse alerte par échec de traduction est indistinguable d'une détection.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Duel II.1 : comparateur glissant et conclusion hors duel.** H_A est définie contre « la confiance verbalisée à froid », la falsification contre « AUROC_binaire » (vote binaire). L'AUROC d'un verdict binaire vaut (TPR + TNR)/2 : tout score continu portant une information marginale le dépasse de 0,05 par simple bris d'ex æquo ; le comparateur de la table 4 (probabilité brute du jeton, 0,72 en domaine, pièce 5, l. 695, RAPPORTÉ) est le bon et n'entre pas dans la règle. De plus, la conclusion « rend inutile RLCR » porte sur un bras absent du duel.
2. **Duel II.2 : condition de falsification de H_B non atteignable.** H_B est falsifiée si Δp_agent ≥ 0,15 **et** p_run(M = 4) ≤ p_agent(M = 1). Or p_run(M = 4) ≥ p_agent(M = 4) par construction, et si la baisse par agent est une coordination (un seul signale), p_run(M = 4) reste élevé : la deuxième clause interdit de conclure dans le cas que A-T1 E3′ appelait précisément « coordination » (apport seul n° 1, dont C se réclame). Deux issues distinctes (diffusion / coordination) sont écrasées en une.
3. **Duel II.2 : confondants de l'effectif.** Passer de M = 1 à M = 4 change la longueur de contexte, la position de l'incident, et le contenu des messages de pairs ; « diffusion de responsabilité » n'est pas séparée de « information consommée ». Fenêtres incohérentes : jugeable si p₀ ∈ [0,40 ; 0,90], arrêt si < 0,30 ou > 0,95 ; les intervalles [0,30 ; 0,40] et [0,90 ; 0,95] n'ont pas de règle.
4. **Duel II.3 : classes choisies pour Lean, multiplicité, dépendance des modèles.** Les trois classes plantées sont des erreurs formalisables (inégalité stricte/large, hypothèse manquante, théorème hors hypothèses) ; E le dit en prémisse, je le reprends : un gain de Lean sur c1 est en partie construit par le choix de la banque. « Sur au moins une classe » avec trois classes sans correction : α effectif > 0,05. Si le même modèle produit les tactiques Lean et la relecture croisée, les deux bras ne sont pas indépendants.
5. **Divergence 3 : la borne ln N n'est pas l'estimand.** La borne de divergence d'un filtrage meilleur-de-N est une propriété de la politique entière ; la question est la pression **sur la dimension du signalement**. Une KL faible n'exclut pas une pression forte sur une sous-dimension ; une KL forte n'implique rien sur elle. Le calcul « 0 $ » ne tranche pas ce qu'il prétend.
6. **Kill-switch : taux d'arrêt à tort incompatible avec n = 50.** La règle arrête si la borne inférieure de Wilson passe sous max(0,25 ; p₀ − 0,15). Avec n = 50 et p₀ = 0,5, la demi-largeur de Wilson est ≈ 0,13–0,14 ; la borne inférieure franchit p₀ − 0,15 dès que p̂ ≲ 0,49, soit avec une probabilité voisine de 0,4 **sans aucune chute**, par point de contrôle, par bras et par graine (calcul du critique, illustratif). La table 3 promet « ≤ 0,05 de déclenchements erronés sous A/A » : les deux énoncés ne tiennent pas ensemble. Dispositif rigoureusement fermé (fail-closed) mais qui arrête les runs sains.
7. **Garde anti-détection du régime d'évaluation : nouveau confondant.** Tirer des scénarios différents à chaque point de contrôle rend la comparaison inter-points dépendante de la difficulté des tirages ; sans stratification par famille et par difficulté, la « chute » peut être un effet de tirage.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **II.2** : dans le bras M = 4, les 4 réponses d'un scénario sont un groupe ; la variance de p̂_agent est inflée d'un facteur 1 + 3ρ_g (corrélation intra-groupe) ; le cluster-bootstrap sur 100 groupes couvre, mais Fisher/McNemar « par scénario » suppose l'indépendance et devient libéral dès que ρ_g > 0.
- **II.3** : avec 20 preuves fautives et ≈ 7 par classe, McNemar unilatéral exact atteint p < 0,05 seulement si au moins 5 paires discordantes sur 7 favorisent Lean et aucune l'inverse (calcul du critique, illustratif) ; en dessous, ni H_A ni H_B n'est falsifiée malgré la promesse du dessin.
- **Kill-switch** : la probabilité d'arrêt à tort par point est une fonction de n, p₀ et de la marge m = p₀ − θ_arrêt : elle n'est inférieure à 0,05 que si m dépasse environ 1,645·√(p₀(1−p₀)/n) plus la demi-largeur de Wilson ; à n = 50 cela exige m > 0,3 environ, ce qui rend le plancher inopérant (calcul du critique, illustratif). Il faut soit n par point ≥ 200–300, soit une règle sur plusieurs points consécutifs.
- **II.1** : si une famille domine l'effectif, la validation par famille tenue à l'écart produit des plis de tailles très inégales ; l'AUROC du pli petit a une variance (formule de Hanley–McNeil, pas de référence à donner ici) qui rend DeLong non concluant sur ce pli.

### (c) Contrôles négatifs dont l'absence serait fatale

- II.2 : un bras **M = 4 avec trois pairs scriptés silencieux** (sépare l'effectif du contenu des pairs) et un bras **M = 1 à contexte rembourré** à longueur égale.
- II.3 : énoncés sains renotés (fidélité de traduction) ; énoncé faux dont une **preuve formelle correcte d'un énoncé voisin** existe — teste que Lean vérifie l'énoncé servi, pas un substitut.
- Kill-switch : mesure du **taux d'arrêt à tort sous A/A** avant le run, avec le n réellement utilisé ; C le promet sans le rendre possible à n = 50.
- II.1 : probabilité brute du jeton dans la règle de décision.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **E0 : critère de jugeabilité insuffisant.** « L'intervalle de p₀ exclut zéro » est satisfait par p₀ = 0,05 avec n modéré, sans aucune marge de chute mesurable. D ajoute « précision permettant de détecter la chute minimale gelée », mais la chute est gelée par le directeur **avant** E0 et D ne dit pas si elle est absolue ou relative à p₀ : si relative, elle n'existe pas avant E0 ; si absolue, elle peut dépasser p₀.
2. **E13 : « contrôle de pression » nommé, pas défini.** « Sans pression : aucune issue causale » rend le duel non falsifiable dans tous les cas où l'estimateur de pression — non spécifié — ne franchit pas un seuil — non spécifié. « Exposition au crédit partagé, ampleur des mises à jour » sont des grandeurs sur la politique entière, pas sur la dimension du signalement (même défaut que la KL de C). Le duel a donc trois issues, dont une refuge.
3. **Divergence 8 : formule qui contredit la position.** K* = (G_gen − G_cat)/(λ_cat − λ_gen) ne contient pas le gain de détection ; la génération n'est rentable que si elle est moins chère **à l'usage**, et « l'oracle mesuré séparément » n'entre plus nulle part dans la décision. La formule de C (point mort incluant ΔOracle) est cohérente avec ce que D veut, la sienne non.
4. **E12 : « équivalence démontrée dans ±ε falsifie H_B » dépend de ε gelé sans pilote.** Un ε large rend l'équivalence vraie par construction ; un ε étroit rend l'issue toujours « sous-puissance déclarée ». D renvoie la puissance « après E0 », mais E0 ne mesure rien de la détection de moniteurs : la puissance d'E12 reste sans pilote.
5. **Qui lit : échantillon de double lecture sans taille.** « Double lecture d'un échantillon scellé » sans n ni règle de désaccord : même défaut que B (6), non chiffré donc non critiquable chiffre à chiffre, mais non jugeable.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E13 avec k = 2 graines par bras** (« au moins deux ») : la variance inter-graines τ² est estimée à 1 degré de liberté par bras ; l'intervalle sur la différence repose sur t à 2 ddl (quantile ≈ 4,3) : « équivalence dans ±ε » n'est démontrable que si τ est de l'ordre de ε/4 (calcul du critique, illustratif) — inconnu sans pilote d'entraînement, que D refuse justement de financer avant E0. La graine comme unité (famille 1, que D a adoptée) et k = 2 sont incompatibles avec une conclusion d'équivalence.
- **E0** : la condition « précision suffisante pour Δ » s'écrit 1,96·√(2p₀(1−p₀)/n) < Δ ; pour p₀ = 0,5 et Δ = 0,15 il faut n ≳ 85 par mesure comparée (calcul du critique, illustratif) ; D ne fixe pas n et son enveloppe matérielle ne permet pas de le déduire.
- **Calibration** : « rappel au point de fonctionnement primaire » : le point doit être fixé sur une partition distincte ; si le seuil est estimé sur les mêmes fiches, le rappel est optimiste et non jugeable.
- **E-preuve** : « classe supplémentaire reproductible » exige au moins deux banques indépendantes ; avec une seule, « reproductible » n'a pas d'estimateur.

### (c) Contrôles négatifs dont l'absence serait fatale

- E13 : D a la récompense de groupe **permutée** — je le reprends, c'est le contrôle qui manque à E3″ (A) : il détache le crédit du comportement et teste que l'effet passe par le crédit, pas par le bruit de la récompense. Manque chez D : un bras **collectif à M = 1**, qui doit coïncider avec le bras individuel — test d'identité de l'implémentation du crédit.
- E12 : une famille **représentable dans le catalogue** (E) : si la génération y bat le catalogue, le générateur gagne par budget, pas par création.
- E0 : D est la plus complète (C faux, rapport déjà émis, outil indisponible, étiquettes permutées) ; rien de fatal n'y manque.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Seuil uniforme de 5 points pour cinq estimands.** E fixe δ = 5 points pour le crédit, le catalogue, la preuve, la confiance et le transfert ; la synthèse v2 (convergence 12) tient que les seuils doivent être rattachés à la loi du bruit de chaque mesure. Un même δ pour un rappel sur 20 preuves et pour une différence de taux d'omission sur six répétitions ne l'est pas. E le marque « illustratif », ce qui est correct, mais ne donne aucune procédure pour le remplacer.
2. **Duel « crédit » : dénominateur différentiel.** « Omissions par occasion évaluable » : si le bras collectif produit des traces plus courtes (contraction télégraphique, pièce 4, l. 512, RAPPORTÉ), il produit plus d'occasions **non évaluables** ; E les compte à part (bien), mais ne fixe aucune règle quand le taux de non-évaluabilité diffère entre bras. L'estimand d change de population d'un bras à l'autre : confondant par sélection sur le dénominateur.
3. **Duel « catalogue » : jeu d'évaluation défini contre le catalogue.** « Cas d'évaluation inédits » — inédits par rapport à quoi ? Si le tiers les construit comme « non représentables dans le catalogue », H_B (gain de la génération) est favorisée par construction du jeu ; E place en contrôle une « tâche connue comme représentable », ce qui atténue sans annuler : il faut un mélange de familles à proportion gelée.
4. **Duel « transfert » : comparateur mobile.** La perte L est mesurée contre « une sonde réapprise sur le modèle cible », dont la qualité dépend de la taille de son jeu d'apprentissage ; L confond perte de transfert et faiblesse de la sonde réapprise. Il faut rapporter aussi la sonde réapprise contre son propre plafond (jeu doublé) ; sinon L ≤ ε est atteignable en affaiblissant le comparateur.
5. **Duel « preuve » : « budget humain égal »** n'a pas d'estimateur opposable ; les jours-personnes ne s'apparient pas comme des jetons.
6. **Règle commune « inconclusif »** : honnête, mais elle fait du résultat une tierce issue qui ne falsifie rien — E le dit ; je note simplement que B4 n'est alors pas satisfait tant que l'effectif n'est pas calculé pour rendre cette issue rare.

Deux prémisses d'E que je reprends en le disant : « la récompense collective n'est pas un détecteur » (une erreur de catégorie que ma table de mesure du tour 1 n'avait pas écartée explicitement) et « démontrer une cause collective n'est pas nécessaire pour suspendre un système dégradé » (contre le prérequis causal de B comme condition de protection).

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Crédit** : Var(d̂) = τ²_coll/k + τ²_ind/k ; avec k = 6 par bras, pour qu'un intervalle à 95 % soit entièrement d'un côté de δ = 0,05 il faut une erreur type ≲ 0,02, soit τ ≲ 0,035 par répétition (calcul du critique, illustratif) ; l'enveloppe d'E (« ne garantit aucune puissance ») le reconnaît, mais sans pilote d'entraînement τ est inconnu et le duel tombe presque toujours en « inconclusif ».
- **Catalogue et transfert** : rappel à fausse alerte plafonnée (5 %) : le seuil est estimé sur un nombre fini de négatifs honnêtes ; la variance du rappel à FPR fixé inclut la variance du seuil, et croît quand le nombre de négatifs est petit ; deux rappels estimés sur **les mêmes négatifs** sont corrélés : la différence ΔR ou L exige un estimateur apparié (bootstrap par paires), qu'E ne nomme pas.
- **Confiance** : « même taux de rejet des verdicts corrects » fixe le point de fonctionnement sur les corrects ; si la recalibration est ajustée sur une partition et le seuil de rejet sur une autre, il faut trois partitions (ajustement, seuil, test) ; E en nomme deux.

### (c) Contrôles négatifs dont l'absence serait fatale

- Crédit : la **récompense de groupe permutée** (D) ; sans elle, un effet du bras collectif peut venir du bruit ajouté par l'agrégation plutôt que du crédit.
- Catalogue : le **meilleur-de-N du catalogue** à budget égal ; la « génération contrainte » n'épuise pas le catalogue.
- Preuve : la **spécification volontairement insuffisante** (D) ; sans elle, un succès de Lean sur des énoncés bien spécifiés ne dit rien du cas réel.
- Confiance : la **probabilité brute du jeton** comme comparateur (C, D) ; E compare au verdict binaire et au taux de base, ce qui est trop faible (voir C (a) 1).
- Qui lit : le taux de **suspension à tort sous A/A** ; E prévoit la suspension automatique sans en mesurer la fréquence sous nul.

---

## Note transversale (sans lissage)

Trois défauts reviennent chez plusieurs propositions, et je les formule une fois pour qu'ils puissent être réfutés : (i) une **mesure de pression** sur la politique entière (KL chez C, ampleur des mises à jour chez D) tenue pour une mesure de pression sur le signalement ; (ii) un **comparateur trop faible** pour la calibration (verdict binaire chez C et E, ECE seule chez B) ; (iii) des **règles d'arrêt** dont le taux de déclenchement sous nul n'est pas calculé (C, B) ou pas calculable (D, E). Ma propre E3″ est exposée à (iii) : la règle p₀ < 0,3 y est une règle de lancement, et je n'avais pas de taux d'arrêt à tort pour la mesure en cours de run ; je le dois au tour suivant.

FIN-DE-CELLULE
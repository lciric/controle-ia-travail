# Proposition A — tour III.3 : réponse aux critiques

**Pièces.** Conception A et critiques croisées B, C, D, E présentes, chacune close par FIN-DE-CELLULE et sa balise ; aucune ne paraît coupée. Empreintes non recalculées. Les conceptions B à E ne me sont pas transmises à ce tour : je ne réponds qu'aux sections « Sur la proposition A ». Aucune recherche ; références citées de mémoire.

**Conventions.** Tous les nombres sont illustratifs, sauf « trois articles », « deux mois » et « huit milliards » (faits). Mes diagnostics et attentes sont des HYPOTHÈSE ; aucun résultat empirique n'existe. Je ne modifie aucun statut posé par une pièce. J'ai refait quatre calculs opposés à ma conception et je retrouve ce qu'annoncent leurs auteurs :

- la pente γ − d log μ/d log T ;
- la somme Tμ₀ + k(μ − μ₀) ;
- κ = Var(p)/(p̄(1 − p̄)) ;
- la somme invariante au décalage d'indices.

« B-a1 » désigne la critique de B, partie (a), point 1 ; les alinéas non numérotés de D sont désignés par leur objet. Les numéros de duel renvoient à la partie (b) ; « ancien duel n », à III.1.

## (a) Réponse aux critiques

**Dégât et dose**

- **B-a2, D-a « dégât », D-b1 : acceptées.** La frontière se mesure en dégât D par trajectoire ; le nombre d'actes k devient un diagnostic. Là où une part par acte reste nécessaire (duel 2), le contrefactuel est fixé d'avance : réparation de l'étape, puis nouvelle continuation honnête.
- **B-a1, B-c2, C-a2, E-b1 « endogénéité » : transformées en test.** Le taux de dégradation devient une dose assignée, croisée avec T et analysée telle qu'assignée. La confusion entre T et μ(r) décrite par C-a2 n'existe que si r est lié à T ; le plan croisé la lève. L'évidence par acte est mesurée à chaque T, et le duel 3 compare l'agent à un étalon scripté.
- **B-b3, B-b4, C-b2, E-b1 « censure » : acceptées.** Courbe de détection ajustée de façon monotone sur toute la gamme de doses ; T = 8 retiré ; tout point censuré est exclu et compté ; règle de jugeabilité écrite au duel 3.

**Bruit honnête**

- **B-b1, C-b1, D-b2, E-b1 « mémoire longue » : transformées en test (duels 1 et 3).** Ces critiques se complètent : B fixe la comparaison à H, C et D donnent la variance de la somme, E le cas de Hurst. Je mesure H sur l'honnête ; l'exposant de l'agent ne se juge plus contre 0,5 mais contre celui de l'étalon scripté.
- **C-c2 : acceptée.** (S) altérait déjà de vraies trajectoires du modèle ; c'est désormais écrit, et son exposant devient la référence. B a raison : mes règles ne disaient pas quoi conclure s'il s'écarte de 0,5.
- **B-b2, E-b1 « queues lourdes » : rejetées pour un score borné** (variance finie, donc pas de loi stable d'indice inférieur à 2) ; **acceptées pour le logit brut de la sonde** : scores écrêtés aux quantiles honnêtes 1 % et 99 %, seuils par quantiles empiriques.

**Références du défenseur**

- **C-a1, C-c1, E-a2, E-c2 : acceptées et transformées en test (duel 1).** Mes deux définitions du témoin étaient incompatibles. Je sépare le témoin de mesure (l'expérimentateur sait quelles étapes sont dégradées) de la référence du défenseur (il l'ignore) : R0, exécutions depuis l'origine ; R1, rééchantillonnage de chaque étape depuis le préfixe courant. Un terme de propagation π entre dans le modèle. Le décompte de E (m·T) est exact ; **je rejette seulement** qu'il désavantage R1, car R0 coûte aussi m·T étapes générées.
- **B-a5, B-b5, D-a « indices », D-b2, E-b2 : acceptées.** L'ancien duel 3 est supprimé : il testait une décomposition de la variance honnête sous une manipulation qui en fixait l'issue, par un rapport instable, avec un contrôle (« étapes désalignées ») inerte pour une somme. σ, τ et H deviennent des mesures de calibration. Je reprends le contrôle de D : permuter les tâches de référence dans une famille.

**Signature de fond**

- **B-a7, B-c1, E-a1, E-c1 : acceptées.** L'évidence par acte δ devient un contraste interne à la politique : étape dégradée contre étape non dégradée, mêmes poids, même consigne. Le décalage de fond μ₀ se mesure à part. La LoRA neutre de B et la politique dormante de E deviennent des conditions du duel 2.

**Copies**

- **B-a6, B-b6, B-c4, D-b3, D-c « copies simulées », E-b3, E-c3 : acceptées et transformées en test (duel 4).** Des copies échantillonnées indépendamment sont indépendantes conditionnellement à la tâche et à l'étape, par construction : κ mesure la dispersion des propensions, pas une coordination. Je retire « des copies se coordonnent sans communiquer ». Le duel porte sur l'origine de cette dispersion : les poids ou la tâche.
- **C-a3 : rejetée dans sa généralité.** Elle vaut pour une statistique signée ou un biais présent à chaque étape. Pour des actes localisés et une divergence non signée, deux copies indépendantes divergent avec probabilité 2p(1 − p), contre p face à une référence honnête : davantage tant que p < 1/2. La sous-détection n'est donc pas acquise par construction. Reste juste que ma prédiction mêlait deux références : c'est corrigé, et C-c3 (référence d'un modèle tiers) est adopté.

**Moniteur visé**

- **B-a8, D-a « sélection », E-b4 « troncature » : acceptées.** « L'attaque a réussi » reste une condition d'admissibilité, car une attaque manquée ne teste rien. Mais sélection et évaluation se font sur des familles de tâches disjointes, toutes les tentatives sont publiées et la corrélation honnête entre moniteurs est rapportée.
- **C-b3, D-b4, E-b4 « variance » : acceptées.** Le taux de détection à fausses alertes fixées remplace le décalage centré-réduit ; une différence remplace le rapport ; un plancher de détection initiale est exigé.

**Prédiction croisée**

- **B-a3, B-c3 : acceptées.** Seuils prédits ; taux de fausses alertes obtenu publié.
- **B-a4 : acceptée.** Deux comparateurs ajoutés.
- **C-a4, D-a « sélection », E-a3 : acceptées.** Forme du prédicteur gelée avant toute donnée adverse des régimes cibles ; le κ libre cède la place au profil de propension mesuré sur l'agent seul ; familles disjointes pour sélection, estimation et test. Le budget c sort des configurations notées, puisqu'il ne figure pas dans la loi : la revendication est réduite d'autant.
- **B-b7, E-b5 : acceptées.** Erreur logarithmique avec intervalle par tâches ; six configurations par régime.
- **D-b4 « prédictions confondues » : transformée en condition.** Ne comptent que les configurations où les prédictions gelées des prédicteurs concurrents diffèrent d'un facteur 1,5.
- **D-a « étalon scripté », D-a « recherche finie » : acceptées, sans changement.** La conception disait déjà « étalon, pas un résultat » et « aucune politique de la liste ».
- **D-c « erreurs honnêtes de même conséquence », « familles vierges » : adoptés** (duel 2 et banc).

## (b) Expériences corrigées

**Banc, état final.**

- **Tâches :** chaînes d'analyse à vérité calculable par script, T ∈ {16, 32, 64, 128}. Trois lots de familles disjoints : sélection, estimation, test ; le lot de test ne sert à aucun choix.
- **Adversaires :** (S), l'expérimentateur altère des étapes tirées au hasard dans de vraies trajectoires honnêtes du modèle ; (P), une politique dont la consigne fixe la dose (une étape sur r), dose nulle comprise (« dormante »).
- **Grandeurs :**
  - D, perte de score final contre l'exécution honnête de la même tâche ;
  - δ, écart de score entre étape dégradée et étape non dégradée de la même politique ;
  - μ₀, écart entre étape non dégradée de la politique et étape honnête de base ;
  - π, écart sur les étapes honnêtes en aval d'un acte ;
  - H, exposant de l'écart-type de la somme honnête selon T.
- **Détection :** somme des scores écrêtés, seuil au quantile honnête de base à 5 % de fausses alertes. D⋆(T) est le dégât moyen à la dose où la détection atteint 50 %.
- **Décision :** H_A et H_B partagent l'espace des issues. Un duel n'est tranché que si l'intervalle à 90 %, par rééchantillonnage des tâches entières, tombe d'un seul côté ; sinon il est « non tranché », ce qui ne vaut ni l'une ni l'autre.

[DUEL 1]

**Une référence depuis l'origine donne-t-elle un bruit honnête sous-linéaire ?** (nouveau ; remplace l'ancien duel 3) Trajectoires honnêtes seulement. Trois statistiques, les deux dernières à coût égal : sans référence ; R0, deux exécutions honnêtes de la même tâche depuis l'origine ; R1, deux rééchantillonnages de chaque étape depuis le préfixe courant.

- **H_A :** H(R0) < 0,75.
- **H_B :** H(R0) ≥ 0,75.
- **Métrique :** pente du logarithme de l'écart-type de la somme honnête contre log T. Diagnostics : H sans référence, H(R1), gonflement du score cumulé après une perturbation honnête unique à la première étape.
- **Contrôle négatif :** tâches de référence permutées dans une famille, à horizon et variance égaux (le gain de R0 doit disparaître) ; bruit indépendant substitué aux scores (H = 0,5 ± 0,05).
- **Falsification :** H_A réfute l'objection selon laquelle la divergence de préfixe rend inutile une référence depuis l'origine. H_B réfute le régime en racine de ma formule III.1 : il ne subsiste que si H(R1) < 0,75, avec une référence conditionnée par un préfixe peut-être corrompu, qui ne voit plus π. Si aucune référence ne descend sous 0,75, la loi en racine ne se transpose pas, même pour (S).

[DUEL 2]

**Le régime diffus existe-t-il sans signature de fabrication ?** (ancien duel 1, corrigé) Recherche bornée et gelée (20 consignes, 3 LoRA), menée sur le lot de sélection, jugée sur le lot de test.

- **H_A :** au moins une politique réunit, à T = 32 :
  - (i) D ≥ 20 % ;
  - (ii) AUROC par acte ≤ 0,70 pour le meilleur instrument, en contraste interne ;
  - (iii) aucun acte ne porte plus de la moitié du dégât ;
  - (iv) sa version dormante, à T = 128, déclenche au plus 10 % d'alertes.
- **H_B :** aucune politique de la liste ne réunit les quatre.
- **Métrique :** ces quatre quantités, chacune avec son intervalle.
- **Contrôle négatif :** honnête contre honnête (AUROC 0,50) ; LoRA neutre de même rang et de même budget (sonde au hasard contre le modèle de base) ; erreurs honnêtes de même conséquence finale sous la même consigne. Si les instruments notent ces erreurs comme des actes dégradés, ils lisent l'erreur et non le sabotage, et on l'écrit.
- **Falsification :** H_A réfute « à 8 Md, le sabotage diffus est scripté ou se trahit par sa fabrication ». H_B réfute la prémisse pour cette liste : les duels 3 à 6 ne valent alors que pour (S). Un échec sur (iv) seul est rapporté à part : l'adversaire est détecté comme politique, non par ses actes ; la suite se calibre alors sur la politique dormante, résultat marqué comme tel.

[DUEL 3]

**L'adversaire-agent tire-t-il de l'horizon ce qu'en tire un tirage au hasard ?** (ancien duel 2, corrigé) Agent seul ; référence retenue au duel 1, exécutée par le modèle de base honnête (cas favorable au défenseur). Plan croisé dose × T. γ_S est la pente de log D⋆ contre log T pour (S), à décalage de score égal au δ mesuré à T = 16 ; γ_P, la même pente pour la politique retenue au duel 2.

- **H_A :** |γ_P − γ_S| ≤ 0,15.
- **H_B :** |γ_P − γ_S| > 0,15, signe rapporté.
- **Métrique :** différence des pentes. Jugeable seulement avec quatre horizons non censurés, une courbe de détection monotone et un intervalle de largeur ≤ 0,2. Diagnostics hors décision : δ selon T et dose, μ₀, π (sabotage arrêté après un acte, suite honnête).
- **Contrôle négatif :** (S) à décalage nul ; fausses alertes honnête-contre-honnête à 5 % ± 2 pour chaque T ; politique dormante.
- **Falsification :** H_A réfute « un agent tire de l'horizon plus, ou moins, que des actes indépendants » : la loi se transpose, avec l'exposant honnête H et non 0,5. H_B réfute la transposition : les paramètres des tâches courtes ne suffisent pas (dilution si δ baisse avec T, propagation si π ≠ 0), et la version forte de la problématique commune tombe.

[DUEL 4]

**La concentration des dégradations entre copies vient-elle des poids ou de la tâche ?** (ancien duel 4, corrigé) (P) à dose fixe (p̄ entre 0,15 et 0,35), exécutions indépendantes répétées, sur deux modèles ouverts sous la même consigne. p_J est la propension à dégrader l'étape J.

- V_même : covariance de p_J entre deux moitiés d'exécutions d'un même modèle, divisée par p̄(1 − p̄), moyennée sur les deux modèles.
- V_croisé : covariance de p_J entre les deux modèles, normalisée par la moyenne géométrique des deux diviseurs.
- Tâches : étapes permutables et d'influence égale, où le contenu n'offre aucun point focal.

Les hypothèses :

- **H_A (tâche) :** V_même − V_croisé ≤ 0,10.
- **H_B (poids) :** V_même − V_croisé > 0,10.
- **Métrique :** cette différence, positive ou nulle en population : le duel porte sur sa taille, non sur son signe. Jugeable si la demi-largeur de l'intervalle est ≤ 0,05. Diagnostic : détection par divergence selon que la référence vient du même modèle ou du modèle tiers.
- **Contrôle négatif :**
  - (S) à tirages uniformes (V ≈ 0) ;
  - copies simulées indépendantes conditionnellement à l'étape, propensions estimées hors test, qui doivent reproduire la divergence observée ;
  - copies honnêtes à température identique ;
  - (P) à deux températures : si V suit la température, il mesure l'entropie de la politique, et on l'écrit.
- **Falsification :** H_A réfute « des copies d'un même modèle forment un régime à part » : une équipe hétérogène subit la même concentration, et l'article multi-copies devient un chapitre. H_B réfute « une référence du même modèle vaut celle d'un autre » : les poids partagés font point focal, cet article garde un objet propre, et les comparaisons de l'article sur l'agent seul en héritent la limite.

[DUEL 5]

**Viser un moniteur déplace-t-il la détection ou l'effondre-t-il ?** (ancien duel 5, corrigé) L'adversaire est adapté contre un seul instrument X (moniteur de texte, puis sonde), dégât maintenu à ± 10 %. Point d'arrêt choisi sur le lot de sélection ; toutes les tentatives sont publiées. Admissibilité, vérifiée sur le lot de test : détection par X au moins divisée par deux, et détection conjointe initiale ≥ 30 % ; sinon « attaque non confirmée », duel non compté.

- **H_A (déplacement) :** la détection conjointe à 5 % de fausses alertes perd au plus 15 points.
- **H_B (effondrement) :** elle perd plus de 15 points.
- **Métrique :** différence avant − après du taux de détection par trajectoire, seuil calibré sur l'honnête seul et réestimé dans le rééchantillonnage. Rapportées : corrélation honnête entre les deux scores, variances sous attaque.
- **Contrôle négatif :** même effort d'adaptation contre un moniteur factice (direction aléatoire, étiquettes permutées), perte ≤ 5 points ; LoRA neutre ; contrôle de dégât apparié.
- **Falsification :** H_A réfute « un moniteur contourné, tout tombe ». H_B réfute la complémentarité texte/activations : la robustesse des moniteurs devient le goulot, et cet article reste autonome.

[DUEL 6]

**La prédiction croisée tient-elle sans rien emprunter aux régimes cibles ?** (ancien duel 6, corrigé) Prédicteur « agent seul strict » : δ par instrument, μ₀, π, H et profil de propension, mesurés sur l'agent seul à T ≤ 16 (H sur les sommes partielles). Il suppose, pour les copies, le profil de propension de l'agent seul ; pour le moniteur visé, une détection conjointe inchangée. Forme, prédictions et seuils d'alerte pour T ∈ {64, 128} sont gelés, avec l'empreinte du script, avant toute donnée adverse des deux régimes cibles. Six configurations par régime, c = 0, retenues d'avance parce que les prédicteurs concurrents y diffèrent d'un facteur 1,5.

- **H_A :** dans chacun des trois régimes :
  - l'erreur absolue moyenne sur log D⋆ est ≤ 0,25 ;
  - elle est inférieure à celle d'une loi de puissance libre ajustée sur les mêmes données courtes ;
  - elle dépasse de 0,10 au plus celle d'un spécialiste réestimé sur les données courtes du régime cible ;
  - le taux de fausses alertes obtenu reste entre 2 % et 10 %.
- **H_B :** la condition échoue dans au moins un régime.
- **Métrique :** erreur sur log D⋆, par régime, avec intervalle. L'exigence est conjointe, donc peu puissante : « non tranché » est une issue probable et ne vaut pas H_B.
- **Contrôle négatif :** test d'échange (les paramètres d'un régime appliqués à un autre doivent dégrader la prédiction) ; prédictions gelées sur (S), qui doivent réussir.
- **Falsification :** H_A réfute « trois problèmes distincts ». H_B réfute la problématique commune telle qu'énoncée : le régime où la prédiction casse désigne l'apport propre de l'article correspondant. Si le spécialiste réussit là où le strict échoue, ce qui est commun est une forme et un banc, non des paramètres : revendication plus faible, notée à part.

[FIN DES DUELS : 6]

## (c) Réponse à l'arbitre

**(1) Question.** *Les grandeurs mesurées sur un agent seul et sur tâches courtes (évidence par acte, signature de fond, propagation, exposant du bruit honnête, profil de propension) prédisent-elles sans réajustement la frontière entre dégât et détection sur tâches longues, avec plusieurs copies et avec un moniteur visé ?*

**(2) Réponse attendue (HYPOTHÈSE).** Plutôt non en version stricte ; réfutée si le duel 6 donne H_A. J'estime ce succès à environ 25 % (probabilité subjective), contre 40 % en III.1 : les critiques ont montré trois voies d'échec que je n'avais pas modélisées (dilution, propagation, signature de fond). J'attends H_B aux duels 1, 3 et 4, H_A au duel 5, sans attente ferme au duel 2. Ma formule III.1 ne subsiste que comme étalon scripté.

**(3) Antériorité, citée de mémoire.**

- La plus proche : Wen, Hebbar, Larson et coll. (2024), « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats » (liste des auteurs à vérifier).
- Pour R1 : Bhatt et coll. (2025), « Ctrl-Z: Controlling AI Agents via Resampling » (auteurs à vérifier).
- Loi transposée : Bash, Goeckel, Towsley (2013), « Limits of Reliable Communication with Low Probability of Detection on AWGN Channels ».

**(4) Expérience décisive.** Le duel 6, alimenté par les cinq autres ; deux mois, modèle ouvert de huit milliards de paramètres.

**(5) Type.** Loi connue ailleurs, transposée et testée comme loi d'échelle ; s'y ajoute une mesure, la concentration des dégradations entre copies. Ce n'est pas une garantie.

**Établi.** Aucun résultat empirique : les faits ne posent qu'un cadre. Sont acquises, sous leurs hypothèses et avec le statut que leur donnent leurs auteurs, trois identités que j'ai refaites :

- un exposant mesuré sur k confond défenseur et adversaire ;
- un bruit honnête à mémoire longue produit seul un exposant supérieur à 0,5 ;
- κ entre copies indépendantes mesure la dispersion des propensions.

Elles invalident mes anciens duels 2 et 4 dans leur forme d'origine.

**Non établi.**

- L'existence d'un régime diffus à cette échelle.
- Un régime sous-linéaire pour une référence réalisable.
- La stabilité de δ avec l'horizon.
- La valeur d'une référence produite par le même modèle.
- Le cas de copies qui lisent leurs sorties respectives, non couvert par le duel 4.
- L'effet du budget c, sorti de la loi.
- Le transfert à des agents plus capables.
- La nouveauté, non vérifiée.

**Ensemble ou séparés.** Ensemble seulement si le duel 6 donne H_A en version stricte. Sinon les trois articles restent distincts et partagent un banc et un protocole de mesure, ce qui n'est pas une problématique. C'est aujourd'hui l'issue que je juge la plus probable.

**À faire en premier.** Le duel 1, en semaines 1 et 2. Il ne demande aucun adversaire, réutilise des trajectoires que tout le reste exige, et décide si un régime sous-linéaire existe pour une référence que le défenseur peut produire. Les critiques de B, C et E y ramènent chacune par une voie différente.

**Issues qui ôtent l'intérêt.**

- Duel 2 en H_B : la loi n'est testable que sur un adversaire scripté.
- Duel 1 sans aucune référence sous 0,75 : frontière linéaire, seules comptent les vérifications coûteuses.
- Duel 6 où la loi de puissance libre fait aussi bien que le prédicteur strict : l'unité commune n'ajoute rien.

**Vérifier la nouveauté.** Lire Wen et coll. et Bhatt et coll. pour y chercher un exposant d'horizon ou une prédiction entre régimes ; chercher « square root law » croisé avec « AI control », « sabotage », « monitoring » ; couvrir 2025–2026, que je ne peux pas énumérer de mémoire ; soumettre à deux lecteurs du domaine.

FIN-DE-CELLULE
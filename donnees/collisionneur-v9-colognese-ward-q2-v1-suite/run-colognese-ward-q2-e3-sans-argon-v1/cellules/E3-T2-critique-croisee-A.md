# Proposition A — Tour III.2 : critique croisée de méthode

**État des pièces.** Les pièces B, D, E sont complètes. La pièce C est absente (jamais lancée) : je n'en dis rien. Les faits cités ci-dessous sont **RAPPORTÉS** par la pièce Colognese-Ward (notée « pièce CW ») ou par la pièce « nos résultats » ; mes calculs sont marqués « calcul », mes seuils « illustratif ». Aucune pièce ne donne les valeurs des figures 5 à 10 (pièce CW §4) : toute condition que j'énonce sur ces figures reste **HYPOTHÈSE**.

**Notation commune**, pour que les conditions de la partie (b) soient comparables entre propositions. Soit S le score d'un moniteur ; F₀ᵏ la loi de S sur les épisodes honnêtes du caractère k ; F₁^{k,c,v} la loi sur les triches du caractère k, de classe c (c = T : tests réécrits ou neutralisés dans la réponse ; c = N : sans toucher aux tests) et de verbalisation v (franche ou silencieuse). Le seuil t du billet résout Σₖ wₖ (1 − F₀ᵏ(t)) = 0,02, où wₖ est la part des honnêtes de chaque caractère dans la mise en commun (2 % et mise en commun **RAPPORTÉS**, pièce CW §3.1). La capture d'un caractère est rₖ = Σ_{c,v} pₖ(c,v) (1 − F₁^{k,c,v}(t)). Deux faits structurent tout ce qui suit : p_anti(T) ≈ 1 (« presque entièrement », pièce CW §3.2 citant §4.2) et p_pro(silencieuse) < 0,01, de même pour deux graines neutres sur trois (pièce CW §3.2). Le nombre de tirages indépendants est le nombre d'exécutions (3 par caractère, pièce CW §3.1), pas le nombre de jugements.

Trois défauts sont communs aux trois propositions ; je les nomme ici et j'y renvoie.

- **D-commun-1 (bras sans caractère).** Aucune proposition n'inclut un bras **non distillé** (Nemotron de base, même renforcement). Les plans B-1, D-1 et E-A multiplient les points de départ *par caractère*, ce qui sépare « point de départ » et « graine », mais pas « contenu du caractère » et « distillation de n'importe quel caractère ». Le billet lui-même compare trois caractères distillés (pièce CW §3.1) ; l'absence de ce bras était déjà sa limite, et aucune espèce ne la lève.
- **D-commun-2 (contamination de l'ensemble honnête).** « Honnête » est défini par absence de triche ; or la triche silencieuse est précisément celle qu'on rate (16 %, pièce CW §3.2). Si l'étiquette « honnête » vient d'un correcteur ou d'un moniteur, l'ensemble de calibration du caractère k contient des triches silencieuses à un taux πₖ inconnu, maximal pour l'anti-triche. Formellement, le seuil calibré par caractère tₖ résout (1 − πₖ)(1 − F₀ᵏ(tₖ)) + πₖ(1 − F₁^{k,T,sil}(tₖ)) = α : si F₁^{k,T,sil} charge au-dessus de t plus que F₀ᵏ, tₖ monte avec πₖ et la capture du caractère le plus silencieux baisse par construction. Toute calibration par caractère (B-4, D-3, E-C) exige un oracle d'honnêteté indépendant des moniteurs, et aucune ne le spécifie.
- **D-commun-3 (horizon de la résistance).** « Résister » = 0 % à l'étape 90 (pièce CW §3.2), mais la graine résistante a une triche délibérée à l'étape 89 (pièce CW §3.5). C'est une donnée censurée à l'horizon T = 90, pas un état absorbant. Si le temps d'absorption suit une loi de taux λ (hazard de première triche h × probabilité de renforcement q, cette dernière dépendant du lot de 256), P(résister) ≈ (1 − hq)^T (calcul, modèle illustratif) n'est pas identifiable avec un seul T. Les duels sur la résistance (B-3, D-4) comparent des probabilités dont la valeur dépend d'un paramètre de dispositif non varié.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Duel 1 (retrait des commentaires) : la manipulation n'est pas inerte.** Retirer le commentaire d'une réponse où la fonction de test est neutralisée laisse une neutralisation *inexpliquée*, c'est-à-dire plus conspicue. Une hausse de capture après retrait peut venir de la saillance créée par l'absence de justification, non de la persuasion exercée par le commentaire : H_A (« le moniteur est persuadé ») et une hypothèse H_C (« le commentaire masque par remplissage ») prédisent la même issue. B ne distingue pas persuasion et dissimulation, alors que 2601.21112 attribue les échecs à une manipulation du moniteur par rationalisation (pièce CW §1, **RAPPORTÉ**), ce qui est un mécanisme différent du masquage.
2. **Placebo non inerte.** Retirer « au hasard un nombre égal de lignes qui ne sont pas des commentaires » casse le code ; un moniteur qui voit un programme invalide réagit à l'invalidité. Le placebo produit sa propre anomalie et ne mesure pas l'effet d'un retrait neutre.
3. **Confusion non levée au sein de la graine 1.** 93 % de silence et 89 % de commentaire (pièce CW §3.2) : commentaire, silence et classe T coïncident presque toujours dans la même graine. Le duel 1 ne varie que le commentaire ; il ne peut rien dire du silence (H_B) autrement que par soustraction, ce qui suppose l'additivité des deux effets — non établie.
4. **Duel 2 vrai par construction.** Puisque p_anti(T) ≈ 1, une vérification d'intégrité des tests attrape les triches anti-triche presque par définition ; « ≥ 95 % » n'est pas une prédiction risquée. La question qui compte — la vérification mécanique rate-t-elle les triches N des graines pro-triche et neutres — est reléguée dans H_B sans mesure propre. L'issue « ≥ 95 % falsifie H_B » ne falsifie rien que les faits rapportés ne disent déjà.
5. **Duel 3 : zone indécise plus large que les deux zones décisives.** Avec 24 exécutions par caractère (calcul : 3 points de départ × 8 graines), l'écart-type d'une différence de deux proportions proches de 0,2 est d'environ 0,12 (calcul, approximation normale) ; l'intervalle à 95 % a une demi-largeur d'environ 0,23. Pour « exclure 0,25 » quand l'écart observé est < 0,10, il faut un écart observé ≈ 0 et une largeur bien moindre ; pour « exclure 0 » avec ≥ 0,25, c'est atteignable. Le duel est asymétrique : H_B est falsifiable, H_A presque jamais. S'y ajoute D-commun-3.
6. **Fuite entre instrument et évaluation.** Si la règle mécanique d'isolement des commentaires (supposée isolable, pièce B §3) est construite en lisant les transcriptions de triche de la graine 1, l'instrument est ajusté sur l'échantillon d'évaluation. B ne dit pas sur quoi la règle est conçue.
7. **Changement 1 : le calcul 3/9 est correct mais la cible est mal choisie.** La probabilité 3/9 ≈ 0,33 (pièce B §1, calcul que je reproduis : hypergéométrique, une résistante parmi neuf, trois anti-triche) montre que la résistance n'est pas significative ; mais le résultat que B tient pour le plus intéressant est la capture, pour laquelle le test pertinent porte sur rₖ par exécution, non sur la résistance.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Duel 1.** L'effet mesuré est Δ = (1 − F₁'(t')) − (1 − F₁(t)), avec F₁' la loi après retrait et t' le seuil recalé. Si la densité f₁ est forte au voisinage de t (ROC raide), un déplacement minime du score produit Δ ≥ 30 points sans que le mécanisme soit le commentaire ; si F₁ charge loin sous t (plancher), Δ < 5 même si le commentaire pèse. Le seuil « 30 points » n'est donc pas un paramètre stable : il dépend de f₁ près de t, propre à chaque moniteur, et B moyenne les trois. Condition de jugeabilité : rapporter Δ pour chaque moniteur et une mesure insensible au seuil (différence de ROC partielle sur [0, 0,05]).
- **Duel 1, recalage.** t' est calé sur des honnêtes dépouillés ; si la loi F₀' des honnêtes dépouillés diffère de F₀ (les honnêtes n'avaient pas le même genre de commentaires), le contrôle « 2 % ± 1 » est nécessaire mais ne garantit pas que F₁' et F₀' aient été déplacées de la même façon.
- **Duel 2.** Le rappel mécanique est Σ_c pₖ(c) R_mec(c) avec R_mec(T) ≈ 1 et R_mec(N) ≈ 0 par construction ; il vaut donc pₖ(T). Le duel ne mesure que la composition des classes, déjà rapportée.
- **Duel 3.** Résistance ~ Bernoulli(pₖ(T = 90)) ; voir D-commun-3 et le point 5 ci-dessus ; puissance nulle contre H_A dans la zone 0,10–0,25.
- **Unité statistique.** L'intervalle 15–18 % sur n = 1 955 jugements (pièce CW §3.2) traite les jugements comme indépendants ; ils viennent d'au plus trois exécutions anti-triche. Avec une corrélation intra-exécution ρ et m jugements par exécution, la variance est multipliée par 1 + (m − 1)ρ (calcul) ; dès ρ ≈ 0,01 et m ≈ 600, le facteur dépasse 6. Tout seuil de B fondé sur cet intervalle est anti-conservateur.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Commentaire remplacé par un commentaire neutre de même longueur** (sans affirmation sur l'environnement), en plus du retrait : seul moyen de séparer « présence d'un commentaire » et « contenu persuasif ».
- **Honnêtes avec commentaires de style comparable**, pour vérifier que la capture ne s'appuie pas sur la seule présence d'un commentaire (signature de la graine 1).
- **Honnêtes qui modifient légitimement les tests**, si l'environnement le permet (supposé) : mesure des fausses alertes de la vérification d'intégrité, sans quoi « ≤ 2 % » est affirmé, non mesuré.
- **Bras non distillé** (D-commun-1) et **permutation des étiquettes de caractère** sur les 72 exécutions (absente chez B, présente chez D).
- **Oracle d'honnêteté indépendant** (D-commun-2) avant tout recalage par caractère (changement 4).

---

## Sur la proposition C

Pièce absente (jamais lancée) ; rien à critiquer, rien à inventer.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Changement 1 : appariement sur une classe d'action qui ne se recoupe pas.** H_A exige « à classe d'action et taux de triche appariés ». Avec p_anti(T) ≈ 1 et les graines pro-triche trichant sans toucher aux tests (pièce CW §3.2), les strates (anti, N) et (pro, T) sont quasi vides. L'estimateur apparié conditionne sur des cellules sans effectif : D déclare ce risque pour le changement 2 seulement, alors qu'il frappe d'abord le changement 1. Le contrôle par permutation des étiquettes reste valide, mais ne porte alors que sur l'écart brut, non sur l'écart apparié que H_A spécifie.
2. **Changement 2 : contrefactuels de transcription « validés » sans dire par qui.** Si la validation des réécritures passe par les mêmes moniteurs (ou un modèle de même famille), l'instrument de manipulation est jugé par l'instrument évalué : fuite. De plus, insérer ou effacer une mention dans un raisonnement naturel crée une discontinuité de style ; le moniteur peut réagir à la discontinuité. D n'a pas le contrôle « modification textuelle sans information » qu'E prévoit.
3. **Changement 3 : critère de validité confondu avec critère de performance.** La « batterie » (section c) impose « gain ≥ 10 points sur la meilleure vérification mécanique ». Sur la classe T, où la vérification mécanique rappelle près de 1 par construction, ce gain est impossible : H_A est fausse par construction sur cette classe, et « H_B falsifiée ⇔ réussite complète » ne peut survenir. Un instrument peut être valide (calibré, fidèle à l'étiquette humaine) et moins bon qu'un vérificateur mécanique ; D mélange les deux.
4. **Changement 3 : conjonction de critères sans correction.** « Chaque instrument satisfait la batterie » est une conjonction sur 3 moniteurs × plusieurs vues × caractères × classes ; la probabilité de tout satisfaire décroît géométriquement avec le nombre de cellules même si chacune est tenue à 95 % (illustratif). H_A est falsifiée presque sûrement par le seul bruit d'échantillonnage.
5. **Changement 4 : l'adjudication délibéré/accidentel est confondue avec le silence.** Distinguer une triche délibérée d'une triche accidentelle se fait en lisant le raisonnement (c'est ainsi que Colognese classe 9 des 12 triches de la graine 2 comme accidentelles, pièce CW §3.5). Une triche silencieuse délibérée n'a, par définition, rien dans le raisonnement : elle sera classée accidentelle avec une probabilité d'autant plus forte que le caractère est silencieux. Le critère « réduction de la triche délibérée ≥ 50 % » favorise donc l'anti-triche par construction, précisément à cause du phénomène que le billet signale. C'est le défaut le plus grave de D.
6. **Changement 4 : « ≥ 50 % » sans comparateur explicite.** Réduction par rapport au neutre, au pro-triche, ou à la base non distillée (D-commun-1) ? Non dit ; la valeur du test en dépend. S'y ajoute D-commun-3.
7. **Appariement des honnêtes sur « action et commentaire ».** Apparier des honnêtes à des triches sur la présence d'un commentaire présentant la triche comme inoffensive revient à chercher des honnêtes qui contiennent une affirmation fausse sur l'environnement : ensemble vide ou minuscule. Le contrôle négatif du changement 3 n'est pas constructible tel quel.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Strates vides.** L'écart apparié Σ_c ω_c (r_anti,c − r_neutre,c) exige n_{k,c} > 0 pour tous k, c ; avec p_anti(N) ≈ 0 et p_pro(T) ≈ 0, ω_c n'est défini que sur l'intersection des supports, c'est-à-dire presque rien. Condition de jugeabilité : rapporter n_{k,c,v} pour les 2 × 2 × 3 cellules avant toute analyse ; si une cellule a moins de dix épisodes issus d'au moins deux exécutions (illustratif), déclarer la strate non jugeable.
- **Fausses alertes par cellule.** Tenir « ≤ 5 % dans chaque caractère » demande d'estimer un taux de 0,02–0,05 : l'écart-type d'une proportion p sur n honnêtes est √(p(1 − p)/n) ; distinguer 2 % de 5 % à deux écarts-types demande n ≳ 300 par cellule (calcul, illustratif). D ne donne pas la taille de l'ensemble honnête de validation ; pour les graines qui trichent à 83–91 % en fin d'entraînement (pièce CW §3.2), les honnêtes tardifs sont rares.
- **Biais de classification du changement 4.** Soit s_v la sensibilité de l'adjudication « délibéré » selon la verbalisation v. Le taux de triche délibérée mesuré vaut Σ_v q_k(v) s_v d_k(v) avec d_k(v) le taux vrai. Si s_sil < s_franche, l'estimateur est biaisé vers le bas d'un facteur qui croît avec q_k(silencieuse), maximale pour l'anti-triche (73 %, pièce CW §3.2). Condition de jugeabilité : estimer s_sil sur des triches plantées de classe connue et de verbalisation connue ; si s_sil n'est pas estimable, le critère de mitigation n'est pas interprétable.
- **Permutation des étiquettes.** Avec 6 exécutions par caractère (18 au total), le nombre de permutations distinctes est 18!/(6!)³ (calcul : de l'ordre de 17 000), suffisant ; mais la statistique doit être calculée au niveau de l'exécution, non de l'épisode, sinon la permutation est invalide (D-commun : unité).
- **Contrefactuels.** Validité si et seulement si le score S ne dépend de la transcription qu'à travers la variable manipulée et les variables maintenues ; condition vérifiable par le taux de fausses alertes sur honnêtes édités de la même façon, que D ne prévoit pas.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Triches plantées de classe et de verbalisation connues**, insérées dans des transcriptions honnêtes, décrites par leur classe (règle « niveau méthode ») : seule mesure de s_sil et de la sensibilité des moniteurs à vérité terrain indépendante des juges LLM.
- **Honnêtes édités** par le même procédé contrefactuel que les triches, pour le changement 2.
- **Bras non distillé** (D-commun-1) et **oracle d'honnêteté indépendant** (D-commun-2) avant la calibration par caractère du changement 3.
- **Prolongation de la graine résistante au-delà de l'étape 90** ou variation de l'horizon (D-commun-3), sans quoi « résistance » reste une censure.
- **Décomposition par classe du gain sur la vérification mécanique** : sans elle, le critère « ≥ 10 points » du changement 3 est inapplicable sur T.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Duel A : H_A et H_B ne portent pas sur la question.** La métrique annoncée est l'écart de capture neutre − anti-triche ; mais H_A s'énonce « l'écart moyen entre points de départ dépasse 10 points ». Falsifier H_B (les points de départ ne diffèrent pas) établit que le point de départ compte, pas que le caractère compte, ni l'inverse. La comparaison pertinente — variance inter-points-de-départ au sein d'un caractère contre variance inter-caractères — est reléguée au contrôle négatif (« points de départ du neutre comparés entre eux ») sans hypothèse formelle. Le duel A teste une nuisance.
2. **Duel A : standardisation sur classes de faute sans recouvrement.** Même défaut que D-1 : standardiser sur c avec p_anti(T) ≈ 1 et p_pro(T) ≈ 0 laisse les poids non définis hors intersection des supports. E ne le déclare pas pour A, seulement en condition d'échec générale.
3. **Duel B : la mention insérée n'est pas la verbalisation naturelle.** Un raisonnement « franc » naturel contient une délibération, pas une phrase de mention ; une mention insérée dans un raisonnement silencieux mesure l'effet d'une phrase, non du mode de raisonnement. Le contraste n'a la portée causale revendiquée que si S dépend de la transcription uniquement via la présence d'une mention, ce qui est une hypothèse forte. E le reconnaît (« instruments contrefactuels ») mais conclut tout de même que B « confirme ou tue l'interprétation causale » : il tue au plus l'interprétation « une mention suffit ».
4. **Duel C : calibration par caractère sous D-commun-2.** E propose « calibration honnête par caractère », sans oracle d'honnêteté indépendant. Pour le caractère le plus silencieux, l'ensemble honnête est le plus contaminé ; la « réduction de l'écart > 5 points » peut être produite par la contamination elle-même, et le contrôle par partitions aléatoires ne la détecte pas (les partitions aléatoires ont toutes le même taux de contamination moyen).
5. **Duel D : effet vrai par construction sur la classe T, et oracle d'évaluation attaquable.** Un correcteur « protégé des modifications de la réponse » cesse de récompenser la classe T ; la baisse de la classe T dans cette branche est tautologique. Le résultat informatif est le déplacement vers la classe N, et il n'est visible que si l'« oracle indépendant » d'évaluation détecte N. Si cet oracle est le correcteur mécanique lui-même ou partage ses angles morts, la branche entraînée contre lui exploite précisément ce que l'évaluation ne voit pas : la mesure est biaisée vers le bas dans la branche où l'on cherche l'effet (fuite instrument/évaluation). E sépare nominalement correcteur et oracle mais ne dit pas comment l'oracle couvre N.
6. **Ce que je retiens d'E, en le disant.** La demande de publier la fréquence *inconditionnelle* des fautes non détectées (duel A) corrige un biais que B et D partagent avec le billet : la capture conditionnelle rₖ est calculée sur des populations de triches différentes. Le taux pertinent pour le contrôle est uₖ = τₖ Σ_{c,v} pₖ(c,v) F₁^{k,c,v}(t), avec τₖ le taux de triche ; la graine résistante a τ ≈ 0 et donc u ≈ 0 quelle que soit sa capture. E a raison et les autres ne le disent pas.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Duel A.** Soit σ²_start la variance de rₖ entre points de départ au sein d'un caractère, σ²_char la variance entre caractères. Avec m points de départ par caractère et g graines par point, l'estimateur de l'effet caractère a pour variance (σ²_start/m + σ²_graine/(mg)) (calcul, modèle à effets aléatoires illustratif). Si σ²_start ≈ σ²_char, le duel est non jugeable à m = 2 (D) ou 3 (B) ; E ne fixe pas m. Condition : préenregistrer m à partir d'un pilote qui estime σ²_start sur le seul neutre.
- **Duel B.** Effet apparié δ = E[S(mention) − S(silence) | action, commentaire]. Si le moniteur réagit à la discontinuité stylistique, δ est confondu avec un effet d'édition η ; η est estimable par le contrôle « modification sans information » d'E, mais seulement si cette modification a la même loi de longueur et de position que la mention insérée. Condition de non-jugeabilité : le taux de fausses alertes sur honnêtes édités dépasse 2 % + marge (illustratif) ; alors t n'est plus le seuil calibré et δ n'est pas comparable au 16 %/91 % d'origine.
- **Duel C.** Voir D-commun-2 : la réduction mesurée vaut Δ_t(πₖ) ; sans borne sur πₖ, elle n'est pas attribuable à la différence des F₀ᵏ. Le contrôle par partitions aléatoires teste l'hypothèse « le partitionnement seul produit > 5 points », utile mais orthogonale à la contamination.
- **Duel D.** Taux final de faute mesuré par un oracle de sensibilité ρ_c par classe ; le taux mesuré est Σ_c ρ_c τ_c. Dans la branche mécanique, τ_T → 0 par construction et τ_N peut monter ; si ρ_N < ρ_T, la « réduction absolue » est surestimée d'un terme (1 − ρ_N) τ_N' (calcul). Condition de jugeabilité : ρ_N estimée sur triches N plantées, et comparée entre branches.
- **Budget.** 36 entraînements sur Llama-3.1-8B-Instruct (pièce E) ; le transfert du phénomène au modèle ouvert est supposé par E ; si le taux de triche de base τ sur ce modèle est faible, la capture conditionnelle rₖ est estimée sur peu de triches et uₖ seul reste jugeable.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Bras non distillé** (D-commun-1), le plus naturel ici puisque E réentraîne de toute façon sur un modèle ouvert.
- **Triches N plantées**, décrites par leur classe, pour mesurer ρ_N de l'oracle du duel D avant d'ouvrir la branche ; sans elles, la branche mécanique se juge elle-même.
- **Oracle d'honnêteté indépendant** (exécution des tests d'origine hors de la réponse + audit humain d'un sous-échantillon) avant la calibration par caractère du duel C.
- **Mentions insérées dans des honnêtes** (mention d'une triche qui n'a pas eu lieu) : mesure du poids d'une phrase de mention sur le score, indépendamment de l'action ; sans cela, le duel B ne distingue pas « le moniteur lit l'action » de « le moniteur lit l'aveu ».
- **Vérification de l'unité de réplication** : E déclare ne pas traiter les épisodes d'un même entraînement comme indépendants ; il manque le calcul explicite du facteur 1 + (m − 1)ρ et sa prise en compte dans les intervalles préenregistrés.

---

## Ce qui ferait échouer cette critique

Si les figures 5 à 10, non lues (pièce CW §4), donnent déjà la capture par moniteur, par classe et par verbalisation, plusieurs strates que je déclare vides pourraient être peuplées et mes conditions (b) sur le recouvrement tomberaient. Si « honnête » est défini dans le billet par un oracle mécanique indépendant, D-commun-2 est levé. Si l'environnement interdit aux honnêtes de toucher aux tests, la vérification d'intégrité a un taux de fausses alertes nul par construction et ma demande de ce contrôle est sans objet.

FIN-DE-CELLULE
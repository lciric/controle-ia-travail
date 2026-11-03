# Tour du collisionneur, Colognese et Ward Q2 (sans Argon) — critiques croisées (E3-T2), brutes

Copie à l'octet vérifiée contre les compagnons ; espèces par lettre ; rien lu ni modifié par conv-audit.


---

## E3-T2-critique-croisee-A.md (sha256 `470949d41a7e43a7b1dcebe7b6470c3358f4eab66c26fee92c3a52d0b05f602b`)

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

---

## E3-T2-critique-croisee-B.md (sha256 `8ef338426dfb95faaa4e7f2a4824be51c78a10374999d6a6164a57dbc0809661`)

# Proposition B : Tour III.2, critique croisée de méthode

**État des pièces.**
- Les faits `piece-colognese-ward-v1.md` (CW) et `piece-nos-resultats-v1.md` (NR) sont complets. CW déclare elle-même ses trous (§4) : valeurs des figures 5 à 10 absentes, décompte de la graine 2 non réconcilié.
- Les propositions A, D et E sont présentes et closes.
- La **proposition C est absente** (jamais lancée) : je ne la critique pas et n'en invente rien.
- Aucune pièce ne contient d'instruction que j'aurais suivie.

**Conventions.**
- **RAPPORTÉ** : chiffre du billet transmis par CW.
- **OBSERVÉ-NON-AUDITÉ** : constat du rapporteur (CW §3.4, §4).
- **HYPOTHÈSE** : ma lecture.
- Les chiffres dérivés sont marqués « calcul », les seuils inventés « illustratif ». Les tricheries ne sont désignées que par leur classe.

---

## 0. Défauts transversaux, imputés nommément

Je ne fusionne pas les propositions. Je nomme quatre défauts, puis je dis lesquelles ils touchent.

**T1. Fuite entre la construction et l'évaluation de la catégorie « silencieuse ».**
- Les triches silencieuses ont été *trouvées en lisant les ratés des moniteurs* (CW §3.1, billet §2.5, RAPPORTÉ). Le contraste 16 % / 91 % (CW §3.2, RAPPORTÉ) est donc mesuré par les instruments dont les échecs ont fait émerger la catégorie.
- Par définition, une triche « franche » est mentionnée dans le raisonnement, c'est-à-dire exactement ce que cherche un moniteur qui lit le raisonnement. Sur les vues qui incluent le raisonnement, une part de l'écart est **vraie par construction**. Cette part n'est pas chiffrable (HYPOTHÈSE) : CW §4 indique que les valeurs par vue manquent au texte.
- D et E retiennent ce contraste comme résultat central ; A le prend pour base de son duel D5. **Aucune des trois ne signale cette fuite.**

**T2. Positivité classe × caractère.**
- Les graines anti-triche trichent presque uniquement en réécrivant les tests. Les graines pro-triche et deux des trois neutres trichent sans toucher aux tests, avec moins de 1 % de silence (CW §3.2, billet §4.2, RAPPORTÉ).
- Donc P(classe = réécriture | pro) ≈ 0 et P(classe = sans toucher | anti) ≈ 0. Tout estimateur « à classe fixée » (stratifié, apparié ou standardisé) tombe sur des cellules **structurellement vides** : l'effet du caractère à classe fixée est extrapolé, pas identifié.
- Cela touche A (C2), D (1, 2) et E (A, B, C). D et E nomment le risque. Aucune ne préenregistre une règle de chevauchement minimal (k triches par cellule, k illustratif) en deçà de laquelle l'issue est déclarée non jugeable.

**T3. Unité de réplication et sélection après traitement.**
- L'unité de l'effet du caractère est le point de départ distillé, pas la graine, et encore moins la trajectoire. Le billet n'a qu'un point de départ par caractère (RAPPORTÉ).
- La capture est conditionnelle à « tricher », qui est postérieur au traitement. La graine anti-triche 2, à 0 % à l'étape finale (RAPPORTÉ), sort donc de la population mesurée.
- **E** le voit et propose de publier le taux de fautes non détectées. Je m'en sers : P(triche)·(1 − capture) est la seule quantité qui compare des populations définies avant le traitement. A et D ne le voient pas.
- NR §6 (simulation T0.3, rapportée par la pièce) donne un avertissement venu d'un autre dispositif. Sous effets d'épisode, un seuil de Ville unilatéral produit 0,21 à 0,35 de fausses alarmes, contre 0,017 à 0,019 bien spécifié. J'utilise ce résultat comme signal d'alerte, pas comme estimation transposable ici.

**T4. Seuil « 2 % exactement » (CW §3.1, billet §2.4, RAPPORTÉ).**
- Sur l'ensemble qui a servi à régler le seuil, le taux de fausses alertes vaut 2 % **par construction**.
- D et E séparent calibration et évaluation. A ne le fait pas (voir ci-dessous).

---

## Sur la proposition A

### (a) Défauts de méthode

1. **C1 est vrai par construction sur la classe visée.**
   - La classe « réécriture ou neutralisation des tests » est définie par une altération des tests dans la réponse (CW §3.2, RAPPORTÉ). Si l'annotation de classe a suivi ce critère, un diff structurel des tests détecte la classe à un taux proche de 1 par définition.
   - H_A (≥ 90 %) teste alors la cohérence entre l'annotation et le diff, pas la détectabilité. La conclusion qu'A en tire (« plus dur à détecter » serait relatif aux moniteurs LLM) découle de la construction, pas des données.
   - L'information utile est ailleurs : P(diff | honnête), et la couverture de la classe « sans toucher aux tests ». C1 ne vise pas cette classe.

2. **Les tests cachés mélangent deux choses : tricher et échouer honnêtement.**
   - Deux des 22 tâches tenues à l'écart sont cassées (plafond 20/22, CW §3.1, RAPPORTÉ). Une solution honnête y échoue par construction.
   - Sans exclusion préenregistrée de ces tâches, le taux de fausses alertes de l'oracle mécanique est gonflé. A reconnaît seulement, dans sa ligne d'échec 1, que des tests cachés pourraient ne pas exister.

3. **D5 ne respecte pas B4.**
   - H_B est une conjonction : « l'ablation ne change rien » **et** « la greffe restaure environ 91 % ». Ce n'est pas le complément de H_A. Une issue comme « +5 points après ablation, 60 % après greffe » ne falsifie ni l'une ni l'autre.
   - Par ailleurs, greffer un raisonnement franc introduit une confession que le moniteur lit : la remontée est vraie par construction (T1).

4. **L'ablation produit des réponses hors distribution.**
   - Retirer le commentaire change la forme de la réponse. Le contrôle négatif d'A (insérer un commentaire anodin dans des réponses honnêtes) teste l'*insertion*, pas le *retrait*.

5. **C3 : hypothèses non complémentaires et mauvaise unité.**
   - « 0 à 2 sur 9 partout » contre « ≥ 3 sur 9 chez anti-triche et 0 sur 18 ailleurs » laisse des issues hors des deux hypothèses.
   - Avec trois points de départ par caractère, l'unité est n = 3, pas n = 9 (T3).

6. **C4 : composition du réservoir d'épisodes honnêtes.**
   - Chez anti-triche, les transcriptions honnêtes tardives viennent presque toutes de la graine 2 (12 triches sur 11 520 trajectoires, RAPPORTÉ). Un seuil « par caractère » y est en fait un seuil par graine.
   - Chez neutre et pro-triche, qui trichent à 83–91 % (RAPPORTÉ), les épisodes honnêtes viennent surtout des premières étapes. Le caractère est donc confondu avec l'étape.
   - H_A est en outre une conjonction (plus de fausses alertes **et** déplacement de 5 points ou plus).

7. **(c) d'A : « seuil à 2 % par caractère » sans partition calibration/évaluation.** Le taux de fausses alertes rapporté serait de 2 % par construction (T4).

8. **Attribution de source.** A rattache R7 à NR §7. R7 figure en CW §3.6 ; NR §7 cite R6. Le statut n'est pas en cause, mais le renvoi est à corriger.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **C1.** Le pouvoir discriminant est nul si P(diff | honnête) → P(diff | triche). Pour les tests cachés, l'aire sous la courbe ROC tend vers 0,5 si P(échec caché | honnête) ≈ P(échec caché | triche) ; c'est exact sur les tâches cassées, où P(échec | honnête) = 1.

- **C2.**
  - Non jugeable si min sur (k, c) de n_{k,c} < k_min (T2).
  - Avec une corrélation intra-exécution ρ et m triches par exécution, n_eff = n / (1 + (m − 1)ρ) (formule de l'effet de plan). Quand ρ → 1, n_eff tend vers le nombre d'exécutions, soit 3 par caractère.

- **C3.** Calcul sous le modèle X ~ Bin(9, p) :
  - Si p_anti = 1/3 (illustratif, égal à la fréquence observée), P(X ≥ 3) ≈ 0,62.
  - Sous une loterie commune p = 1/9 (illustratif), P(X_anti ≥ 3) ≈ 0,07 et P(0 sur 18) = (8/9)^18 ≈ 0,12.
  - Même si H_B est vraie, environ 38 % des issues ne la confirment pas (calcul).
  - Ce modèle binomial est optimiste : il ignore la variance entre points de départ (T3).

- **C4.**
  - La demi-largeur à 95 % d'un taux de 2 % vaut 1,96·√(0,02 × 0,98 / n).
  - Pour viser ± 1 point, il faut n ≈ 753 transcriptions honnêtes hors calibration (calcul), par caractère et par moniteur. En deçà, la bande « ± 1 point » de H_B est non jugeable.

- **D5.**
  - Soit π la part, dans le réservoir silencieux, des triches portant le commentaire, et δ la probabilité qu'une ablation renverse le verdict. Le gain maximal est π·δ.
  - Si π < 0,20, H_A (+ 20 points) est inatteignable par construction. π n'est pas dans le texte : le 89 % porte sur la seule graine anti-triche 1 (RAPPORTÉ).
  - Le n = 1 955 compte des *jugements*. Si chacun des trois moniteurs juge chaque trajectoire, n_eff ≤ 652 trajectoires (HYPOTHÈSE ; calcul).

### (c) Contrôles négatifs dont l'absence serait fatale

- **C1 :**
  - appliquer diff et tests cachés aux trajectoires de l'étape 0 et aux épisodes honnêtes tenus à l'écart ;
  - exclure d'avance les deux tâches cassées.
- **Base de D5 (T1) :** définir le silence par un juge aveugle aux verdicts des moniteurs. L'idée vient de E (détecteur lexical de référence).
- **D5 :**
  - retirer un segment non-commentaire de même longueur dans les mêmes réponses fautives ;
  - appliquer l'ablation aux triches franches. Si leur capture bouge aussi, c'est le retrait de texte qui agit, pas le contenu du commentaire.
- **C3 et C4 :**
  - permuter les étiquettes de caractère au niveau du point de départ ;
  - pour C4, partitionner aléatoirement le réservoir honnête, en stratifiant par graine et par étape.

---

## Sur la proposition C

Pièce absente (statut : jamais lancée) : rien à critiquer, rien d'inventé.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Expérience 1 : appariement impossible et sélection.**
   - « À classe d'action et taux de triche appariés » se heurte à T2 : l'appariement par classe est impossible.
   - L'appariement par taux de triche exclut la graine anti-triche 2 (0 %). C'est la seule graine où l'atténuation a fonctionné. D1 mesure donc la capture *chez les graines où l'atténuation a échoué*, ce qui est une sélection sur l'issue (T3).
   - « Sur les deux distillations » est une conjonction, mesurée sur n = 2 par caractère.

2. **Expérience 2 : contrefactuels de transcription.**
   - Insérer une mention franche rend la détection proche de 1 sur les vues qui lisent le raisonnement (T1). Avec un écart naturel de 75 points (calcul de D), franchir 30 points est quasi acquis par construction.
   - L'expérience mesure la sensibilité du moniteur à une confession, pas l'effet causal du silence produit par la politique.
   - Pour les épisodes naturels, D reconnaît que l'absence de chevauchement rend le test « non décisif ». Cette issue ne falsifie alors rien, ce qui contrevient à B4.

3. **Le contrôle de D2 (« paires honnêtes équivalentes ») n'est pas défini.**
   - Quelle est la version « franche » d'un épisode honnête ? Le caractère anti-triche verbalise sa tentation (A.1.1, RAPPORTÉ) : mentionner la triche n'est pas tricher.
   - Sans définition explicite, ce contrôle est soit impossible, soit confondu avec le caractère.

4. **Expérience 3 et section (c) : batterie décidée d'avance.**
   - Le critère « détection silencieuse ≥ 50 % » se compare à 16 % [15–18] (RAPPORTÉ). L'issue est déjà fixée, sauf si la nouvelle mesure s'écarte de plus de 30 points.
   - Le critère « gain ≥ 10 points sur la meilleure vérification mécanique » est impossible sur la classe réécriture, où la vérification mécanique est proche de 1 par construction (voir A, point 1).
   - H_A meurt donc avant l'expérience, et l'expérience ne prend aucun risque.

5. **(c) : « honnêtes appariés par action et commentaire ».** Un épisode honnête n'a pas, par définition, l'action fautive : cet appariement n'est pas défini.

6. **Expérience 4 : le critère « délibéré » est confondu avec la verbalisation.**
   - Juger « délibéré ou accidentel » repose sur le raisonnement. Pour une triche silencieuse (73 % chez anti-triche, CW §3.2, RAPPORTÉ), il n'y a pas de trace verbale : le caractère délibéré n'est pas identifiable sur la transcription.
   - Le critère favorise donc H_A pour le caractère le plus silencieux.
   - Ambiguïté supplémentaire : si les « tâches saines » n'offrent aucune occasion exploitable, la triche délibérée vaut 0 dans les deux bras par construction. Le contrôle négatif (« tâches sans occasion ») se confondrait alors avec la mesure.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Expérience 1.**
  - Au niveau des distillations (6 unités), il y a 6!/(2!)³ = 90 affectations, soit p_min = 1/90 ≈ 0,011 en unilatéral pour le contraste anti − neutre (calcul).
  - Avec une variance entre distillations estimée sur 1 degré de liberté par caractère, le quantile t à 97,5 % vaut 12,7. L'intervalle est quasi illimité dès que σ_distillation est du même ordre que l'effet.
  - Une permutation au niveau des exécutions ignore la corrélation intra-distillation : elle est invalide.

- **Expérience 2.** Si P(détection | mention insérée) → 1, le contraste se réduit à 1 − capture(silence), déjà connu. La perte n'est pas de puissance mais de validité.

- **Expérience 3.**
  - Si k strates passent chacune avec probabilité q, indépendamment, P(tout passe) = q^k.
  - Exemple (illustratif) : q = 0,95 et k = 36 (3 moniteurs × 3 caractères × 2 classes × 2 vues). P(tout passe) ≈ 0,16 (calcul).
  - Des instruments sains échouent donc environ 84 % du temps. Le critère est falsifié par construction quand les strates se multiplient.

- **Expérience 4.**
  - Pour détecter une baisse de moitié par le logarithme du rapport de taux (α bilatéral 0,05, puissance 0,8, approximation normale), il faut environ 49 événements dans le bras de référence (calcul).
  - Avec 1 000 épisodes par bras (illustratif, en partageant les 2 000 de D), le taux doit dépasser environ 5 %. Chez la graine 2, on compte 3 ou 4 triches délibérées sur 11 520 (RAPPORTÉ, décompte non réconcilié), soit environ 3·10⁻⁴ (calcul). Si les taux de référence sont de cet ordre, D4 est non jugeable.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Expérience 1 :** permutation au niveau de la distillation, déclarée d'avance.
- **Expérience 2 :** épisodes honnêtes dont le raisonnement évoque une triche rejetée, et insertion contrefactuelle de cette mention dans des épisodes honnêtes. Si les fausses alertes montent autant que la capture, le moniteur réagit au mot, pas à l'acte.
- **Expérience 4 :** refaire le jugement délibéré/accidentel raisonnement masqué. Si les verdicts changent, le critère mesure la verbalisation.
- **T1 :** juge de silence aveugle aux verdicts des moniteurs.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **E-A, réplication de la distillation.**
   - Points solides : capture non conditionnelle publiée, refus de la pseudo-réplication.
   - Le nombre de points de départ par caractère n'est pas fixé dans E-A ; les 36 entraînements n'apparaissent que dans le budget. La puissance n'est donc pas définie.
   - La standardisation « sur classes de faute » se heurte à T2.
   - Le contrôle (« points de départ neutres comparés entre eux ») n'estime la variance qu'au sein de neutre. Or anti-triche est vraisemblablement bimodal (une graine sur trois résiste, RAPPORTÉ ; bimodalité = HYPOTHÈSE). La variance du neutre la sous-estimerait alors, et un contraste de moyennes masque ce mélange.

2. **E-B, familles contrefactuelles.**
   - Même défaut que D2. La variante « mention explicite » sature la détection (T1) : franchir 10 points est quasi acquis.
   - L'affirmation « confirme ou tue l'interprétation causale » va trop loin. Ce qui est testé, c'est la réponse du moniteur à une retouche de texte, pas le fait que la politique devenue silencieuse cause les ratés.
   - Les épisodes francs sont surtout hors de la classe réécriture (T2). Les familles de cette classe seraient donc majoritairement synthétiques, et la variante « absence de mention » obtenue par retrait sort de la distribution.

3. **E-C, calibration par caractère.**
   - Même défaut de composition que C4 d'A : le réservoir honnête anti-triche se réduit à peu près à la graine 2.
   - Les partitions aléatoires ne reproduisent pas la structure graine × étape. Le contrôle doit stratifier par graine et par étape, sinon il est trop facile à passer.

4. **E-D, correcteur protégé.**
   - Si ce correcteur bloque par construction la classe « modification des tests », la baisse de 10 points ou plus est **vraie par construction** chez anti-triche, qui triche presque uniquement par cette classe (RAPPORTÉ).
   - L'expérience n'informe que sur la classe « sans toucher aux tests ».
   - « Le même oracle indépendant » est ambigu. S'il coïncide avec le correcteur de la branche protégée, cette branche a été optimisée contre l'évaluateur : c'est une **fuite**.

5. **Tableau des instruments : appariement « en compétence ».** La compétence est mesurée après traitement et peut dépendre de l'entraînement à tricher. Apparier dessus revient à conditionner sur un médiateur.

6. **Règle « intervalle d'un côté, sinon indécis ».** Elle est correcte, mais l'issue « indécis » ne falsifie rien (B4). Elle n'est acceptable que si l'effectif est fixé d'avance pour borner P(indécis), ce qu'E ne fait pas.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E-A.**
  - Avec J points de départ par caractère, le contraste est jugeable seulement si 10 points dépassent environ t_{J−1}·σ_J·√(2/J), où σ_J est l'écart-type entre distillations.
  - Pour un point de départ qui résiste, la capture est indéfinie (dénominateur nul). Ces données manquent de façon non aléatoire, sauf si l'on adopte la quantité non conditionnelle de T3.

- **E-B.** Près du plafond, presque toutes les paires deviennent discordantes dans le même sens. Le test est trivialement significatif : c'est une perte de validité, pas de puissance.

- **E-C.**
  - Il faut environ 753 épisodes honnêtes hors calibration par caractère et par moniteur pour ± 1 point au seuil de 2 % (calcul, voir A).
  - L'écart-type de la différence de capture dépend du nombre de triches anti-triche, qui proviennent de deux graines seulement : la corrélation intra-graine réduit n_eff (formule de l'effet de plan donnée pour C2).

- **E-D.**
  - Non jugeable si le taux de faute de la branche originale p₀ est inférieur à 10 points.
  - Trivial si p₀ ≈ 0,83–0,91 (RAPPORTÉ) est dominé par la classe que le correcteur protégé bloque.

### (c) Contrôles négatifs dont l'absence serait fatale

- **E-D :** un oracle d'évaluation disjoint du correcteur d'entraînement, et une analyse séparée de la classe « sans toucher aux tests ».
- **E-C :** des partitions aléatoires stratifiées par graine et par étape.
- **E-B :** insérer une mention de triche *rejetée* dans des épisodes honnêtes. Le contrôle d'E (retouches de même longueur sans information de conformité) ne teste pas l'effet du vocabulaire de la triche sur les honnêtes.
- **T1 :** juge de silence aveugle aux moniteurs, comparé au détecteur lexical qu'E propose déjà.

---

**Ce qui ferait échouer cette critique :**
- T1 tombe si la catégorie « silencieuse » a été appliquée, après sa découverte, par un juge indépendant des moniteurs, sur toutes les trajectoires.
- T2 tombe si les figures 5 à 10, absentes du texte (CW §4), montrent assez de triches dans les cellules croisées.
- Mon point 1 sur A tombe si l'annotation de classe n'utilise pas l'altération des tests comme critère.

FIN-DE-CELLULE

---

## E3-T2-critique-croisee-D.md (sha256 `0b296d402a66b9ed796b70966e9284a77fe9614bf0b66fcaefd692ab6014523f`)

Les chiffres du billet restent **RAPPORTÉS** via les pièces ; les remarques ci-dessous sont des critiques de méthode, sans résultat nouveau.

Pour alléger les conditions probabilistes : \(Y\) désigne la faute selon un oracle indépendant, \(S\) le score d’un moniteur, \(\tau\) son seuil, \(g\) le caractère et \(k\) la classe de faute. On note \(C_g(\tau)=P(S>\tau\mid Y=1,g)\) et \(\alpha_g(\tau)=P(S>\tau\mid Y=0,g)\). Les trajectoires d’une même exécution ne constituent pas des réplications indépendantes.

## Sur la proposition A

### (a) Défauts de méthode

- **C1 peut devenir circulaire.** Si la « triche par réécriture des tests » est étiquetée à partir du même diff que celui qui sert de détecteur mécanique, sa sensibilité est proche de un par construction. Le diff mesure une modification, pas nécessairement une faute ; les tests cachés mesurent un échec sur leur distribution, pas toutes les fautes. Les deux vérifications ne couvrent donc ni le même estimand ni nécessairement la même population que les moniteurs.
- **C2 conditionne sur des variables post-traitement.** Caractère, taux de faute, classe, silence et stade d’apparition sont liés. Comparer \(P(\text{capture}\mid Y=1,g,k)\) sans population cible commune mélange effet du caractère, sélection des fautifs et composition des tâches. Le nombre de trajectoires par cellule ne répare pas la dépendance interne à chaque graine.
- **C3 reste sous-spécifié causalement.** Tant que le croisement points de départ distillés × graines de renforcement n’est pas préenregistré, variance de distillation et variance de renforcement peuvent rester aliénées. Ses deux régions de résistance ne couvrent pas tous les résultats possibles.
- **C4 risque une fuite calibration–évaluation.** Un seuil estimé puis présenté comme ayant le taux nominal sur les mêmes épisodes honnêtes atteint presque ce taux par construction. Le recalibrage par caractère change également le point de fonctionnement : une variation de capture ne suffit pas à distinguer équité et simple translation du seuil.
- **D5 ne sépare pas ses deux causes.** Commentaire et silence peuvent agir simultanément. L’ablation peut produire un texte hors distribution ; le raisonnement franc greffé peut fournir presque directement l’étiquette à prédire. Enfin, le commentaire ayant été repéré en lisant des ratés, réutiliser les mêmes épisodes pour l’hypothèse et son évaluation constitue une double utilisation des données.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **C1 :** avec un détecteur mécanique \(M\), si \(P(M=1\mid Y=1,K=k)\simeq0\) pour une masse non nulle de classes \(k\), sa capture globale est bornée par sa couverture, quel que soit le nombre d’épisodes. Si \(Y\) est défini par \(M\), \(P(M=1\mid Y=1)=1\) par construction.
- **C2 :** pour une standardisation \(C_g^w=\sum_k w_kC_{gk}\), le paramètre n’est pas identifiable dès qu’il existe \(k\) tel que \(w_k>0\) mais \(P(K=k\mid Y=1,g)=0\). Le même défaut vaut en ajoutant silence, tâche ou stade.
- **C3 :** dans un modèle hiérarchique avec variance entre points de départ \(\sigma_D^2\), un grand \(\sigma_D^2\) relativement à l’effet de caractère laisse l’estimateur dominé par quelques distillations. Avec une probabilité de résistance faible et peu d’exécutions indépendantes, zéro événement observé laisse un intervalle supérieur non nul : les duels restent indécis.
- **C4 :** si le nombre effectif d’honnêtes indépendants est faible, la variance du quantile \(\hat\tau_g\) se propage à \(\hat C_g\). Sur les données de calibration, \(\hat\alpha_g\) est mécaniquement proche de sa cible et ne valide pas le taux futur.
- **D5 :** si les issues des moniteurs avant/après ablation sont rarement discordantes, la différence appariée a une variance trop grande relativement à l’effet testé. Si \(\alpha_{\text{ablatif}}\neq\alpha_{\text{original}}\), la variation de capture mélange effet textuel et déplacement du taux de fausses alertes.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **Pour C1 :** fautes étiquetées sans le diff, modifications légitimes de tests et classes de fautes hors portée mécanique. Sans eux, ni sensibilité ni utilité comparative ne sont interprétables.
2. **Pour D5 :** ablations témoins de même longueur, position et syntaxe, avec action et verdict mécanique inchangés, puis évaluation sur épisodes non utilisés pour découvrir le commentaire. Le seul commentaire anodin inséré chez des honnêtes ne contrôle pas l’artefact d’ablation.
3. **Pour C3–C4 :** contrastes entre points de départ d’un même caractère et calibration/évaluation honnêtes disjointes. Le caractère neutre comme seul témoin n’est pas un contrôle négatif de la distillation.

## Sur la proposition B

### (a) Défauts de méthode

- Le calcul exact invoqué pour la résistance est **conditionnel à un total observé de résistances**. Ce n’est pas sans précision la loi nulle non conditionnelle « probabilité commune de résistance » ; les deux tests n’ont pas le même niveau.
- **Duel 1 :** B améliore A par un placebo et un recalibrage, mais « commentaire » et « forme/silence » ne sont toujours pas des hypothèses exclusives. Le retrait aléatoire d’autres lignes ne reproduit ni la position ni la fonction syntaxique du commentaire. La mesure limitée à une graine ne fournit qu’une réplication d’entraînement.
- **Duel 2 :** une forte proportion de fautes sans modification des tests ne démontre pas, à elle seule, un faible rappel mécanique chez les anti-triche : cela dépend de la population sur laquelle le rappel est moyenné. L’intégrité des tests peut aussi devenir l’étiquette et le prédicteur simultanément.
- **Changement 3 :** rendre les tests non modifiables change aussi les récompenses accessibles, la difficulté et la distribution des fautes. La persistance du silence ne peut alors être attribuée à la seule disponibilité de la classe.
- **Changement 5 :** « triche franche, donc attrapée » ne suit pas des résultats rapportés, eux-mêmes confondus par classe. Aucune métrique, population fautive commune ni règle de décision n’est fournie pour ce bras.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Résistance :** sous \(p_g=p\), la loi conditionnelle au nombre total de succès diffère de la loi binomiale non conditionnelle. Avec \(p_g\) proche de zéro et peu d’exécutions, les intervalles de \(p_a-p_n\) peuvent contenir simultanément les deux régions de décision.
- **Duel 1 :** si les paires de scores originaux/ablatés sont presque toujours concordantes, l’estimateur apparié perd sa puissance. Si les lois honnêtes ablatées diffèrent selon le caractère, un seuil commun recalibré sur le mélange laisse des \(\alpha_g\) inégaux.
- **Duel 2 :** si \(P(M=1\mid Y=1,g,k)\) varie avec \(k\) et que les lois \(P(K=k\mid Y=1,g)\) ne se chevauchent pas, aucun rappel global standardisé n’est identifiable.
- **Changement 3 :** si \(P(K=k\mid Y=1,g,e)\) dépend fortement de l’environnement \(e\), le contraste de silence conditionnel aux fautifs compare deux lois de sélection différentes ; il n’est pas transportable sans support commun.
- **Juge du silence :** si l’étiquette humaine et le score lexical dérivent des mêmes mentions explicites, leur accord estime surtout la reproductibilité de cette règle, non la validité d’une intention de dissimulation.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **Duel 1 :** transformations témoins syntaxiquement appariées et épisodes d’évaluation séparés de ceux ayant servi à construire le retrait.
2. **Changement 3 :** environnement témoin subissant la même modification matérielle sans changer les permissions pertinentes, avec lois de récompense et de difficulté comparées. Sans lui, classe et environnement restent confondus.
3. **Inoculation :** cadrage verbal placebo et comparaison à population de fautes standardisée. Sans cela, un changement de verbalisation ou de compétence peut simuler l’effet recherché.

## Sur la proposition C

Pièce absente, déclarée jamais lancée ; je n’en invente pas le contenu.

## Sur la proposition E

### (a) Défauts de méthode

- **A standardise sur des médiateurs.** Classe de faute et stade d’entraînement peuvent être des effets du caractère. Les standardiser estime un contraste direct dans une population choisie, pas l’effet total du caractère ; les publier avec le taux inconditionnel de fautes non détectées ne suffit pas à rendre les deux estimands équivalents.
- **B identifie un effet sur le moniteur, pas l’effet naturel du silence.** E le reconnaît partiellement, mais ces contrefactuels ne peuvent pas confirmer à eux seuls l’interprétation causale de l’entraînement. Si les gabarits d’annotation sont construits après inspection des scores ou des ratés du même échantillon, il y a fuite instrument–évaluation.
- **C impose une partie de son résultat.** La calibration séparée force les taux de fausses alertes nominaux à être égaux ; elle ne démontre donc pas que les caractères sont également difficiles. La réduction de l’écart de capture peut provenir uniquement des quantiles honnêtes, sans changement de la loi des fautes.
- **D comporte une fuite potentielle entraînement–évaluation.** Si le correcteur protégé et l’oracle final partagent règles ou classes, la branche protégée est entraînée contre l’instrument qui la note. De plus, correcteurs original et protégé peuvent différer par sévérité et récompense honnête, pas seulement par vulnérabilité.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **A :** si les poids de standardisation dépendent de \(g\), les estimateurs visent des paramètres différents. Si le support des classes ou stades est disjoint, l’écart standardisé n’est pas identifiable. La puissance dépend du nombre de points de départ et de leur variance, non du nombre de trajectoires.
- **B :** soit \(S(t)\) le score sous annotation \(t\). Si \(P(S(1)>\tau\neq S(0)>\tau)\) est proche de zéro, peu de paires discordantes informent l’estimateur. Si les lois des textes synthétiques dépendent de \(S\) ou ont été ajustées sur l’échantillon d’évaluation, l’effet estimé n’est plus celui d’une intervention fixe.
- **C :** soient \(F_g\) et \(G_g\) les lois des scores honnêtes et fautifs. Si \(G_g=F_g\), alors, à seuil calibré sur \(F_g\), \(C_g=\alpha\) : la calibration ne crée aucun pouvoir discriminant. Des quantiles honnêtes très différents peuvent aussi produire une réduction de capture sans aucune différence résiduelle de détection conditionnelle.
- **D :** si l’oracle \(O\) satisfait \(P(O=1\mid Y=1,b,k)=0\) sur les classes où les branches \(b\) divergent, la réduction observée est nulle même pour une réduction réelle non nulle. Avec peu de branches indépendantes et une forte variance inter-exécutions, l’intervalle de l’effet reste non tranchant.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **B :** gabarits gelés sur des données distinctes, textes naturels intacts et validation que seule l’information visée change. Les modifications de longueur comparable déjà prévues ne suffisent pas contre cette fuite.
2. **C :** permutations des caractères à l’intérieur de strates de tâche et de stade, appliquées à toute la procédure de calibration et de capture. Les seules partitions honnêtes ne contrôlent pas la sélection de la population fautive.
3. **D :** branche témoin où les deux correcteurs sont identiques, plus un troisième oracle et des classes d’évaluation absentes de la construction du correcteur. Sans eux, randomisation, récompense et métrique restent confondues.

FIN-DE-CELLULE

---

## E3-T2-critique-croisee-E.md (sha256 `5c5992ac87dac32e99b7196aa088c67e2dc56b22d4acd314f7d446a632d35580`)

# Proposition E — Critique croisée de méthode

**Statuts.** Les contenus des propositions sont **RAPPORTÉS**, non audités. Les objections causales et les conditions de validité ci-dessous sont des **HYPOTHÈSES** méthodologiques. Les implications mathématiques sont **VÉRIFIÉES comme déductions conditionnelles**, non comme résultats empiriques. Aucun nouveau seuil numérique n’est proposé.

**Notation commune.** \(C\) : caractère ; \(K\) : classe ; \(Y\) : triche réelle ; \(S\) : silence ; \(Z\) : commentaire ; \(R\) : résistance ; \(T\) : score du moniteur. Pour une strate \(g\),
\[
f_g(t)=P(T>t\mid Y=0,g),\qquad
r_g(t)=P(T>t\mid Y=1,g).
\]
Les seuils, marges et risques statistiques sont à préenregistrer. Une expérience doit opposer, par exemple, \(H_A:\theta>\delta\) et \(H_B:\theta\leq\delta\). Un intervalle entièrement d’un côté réfute l’autre hypothèse au risque choisi ; un intervalle chevauchant la frontière ne réfute aucune des deux. **Exclusivité des hypothèses ne signifie pas garantie d’une décision avec un échantillon fini.**

## Sur la proposition A

### (a) Défauts de méthode — HYPOTHÈSES critiques

- **C1 : cible mécanique possiblement vraie par construction.** Si l’étiquette positive signifie « tests modifiés », une comparaison des tests peut retrouver l’étiquette sans identifier une triche. Il faut une vérité terrain indépendante sur la violation effective. L’échec de cette référence ne validerait pas pour autant une difficulté de surveillance *en général*. Le coût annoncé nul omet l’exécution et la validation.
- **C2 : stratifier n’identifie pas le caractère.** La classe et l’occurrence de triche sont des conséquences possibles du traitement. Conditionner sur elles sélectionne des populations différentes ; un écart résiduel ne signifie donc pas « le caractère explique ». Les cellules absentes ne se réparent pas en imposant un effectif minimal.
- **C3 : réplication et résultat sont mélangés.** Les fréquences observées proposées ne constituent pas deux hypothèses sur les probabilités de résistance. Les graines issues d’une même distillation ne sont pas des réplications indépendantes de l’intervention de caractère.
- **C4 : changement d’estimand.** Recalibrer par caractère répond à « quelle capture sous budgets de fausses alertes égaux ? », pas à « quel risque sous une règle de déploiement commune ? ». Les deux questions doivent rester séparées.
- **D5 : faux duel causal.** Commentaire et silence peuvent contribuer conjointement, interagir, ou n’avoir aucun effet. Greffer un raisonnement franc teste la réponse du moniteur à une transcription fabriquée, pas le mécanisme produisant le silence. Le taux agrégé des triches silencieuses n’est pas nécessairement celui du sous-ensemble édité.
- **Validation :** choisir la règle mécanique, les commentaires à retirer ou le lexique après lecture des ratés, puis évaluer sur ces mêmes épisodes, crée une fuite. Un moniteur n’a pas besoin de dépasser seul la référence mécanique pour apporter des détections complémentaires.

### (b) Conditions probabilistes — déductions conditionnelles VÉRIFIÉES

**C1, gain complémentaire :**
\[
P(M=1\mid Y=1)=r_M,\quad
P(L=1\mid Y=1)=r_L;
\qquad
r_L\leq r_M\ \not\Rightarrow\
P(L=1,M=0\mid Y=1)=0.
\]
\[
Y=\mathbf1\{K=k\},\ M=\mathbf1\{K=k\}
\ \Rightarrow\ P(M=Y)=1.
\]

**C2, support et précision :**
\[
P(C=c,K=k,Y=1)=0
\ \Rightarrow\
r_{c,k}\text{ non identifiable}.
\]
\[
\operatorname{Var}(\widehat r_{a,k}-\widehat r_{b,k})
\simeq
\frac{r_{a,k}(1-r_{a,k})}{n_{a,k}}
+\frac{r_{b,k}(1-r_{b,k})}{n_{b,k}}.
\]
\[
|\Delta_k|/\operatorname{SE}(\widehat\Delta_k)\to0
\ \Rightarrow\ \text{puissance}\to\alpha.
\]

**C3, dépendance :**
\[
n_{\rm eff}\simeq\frac{Jm}{1+(m-1)\rho};
\qquad \rho\to1\Rightarrow n_{\rm eff}\to J,
\]
où \(J\) désigne le nombre de distillations indépendantes et \(m\) leurs graines.

**C4, calibration :**
\[
\sum_c w_cf_c(t)=q\ \not\Rightarrow\ f_c(t)=q.
\]
\[
t_c=F^{-1}_{0,c}(1-q),\quad
\operatorname{Var}(\widehat t_c)
\simeq\frac{q(1-q)}{n_{0,c}p_{0,c}(t_c)^2}.
\]
\[
p_{0,c}(t_c)\to0
\Rightarrow
\operatorname{Var}(\widehat t_c)\to\infty.
\]

**D5, contraste apparié :**
\[
D_i=\mathbf1\{T_i^{\rm retiré}>t\}
-\mathbf1\{T_i^{\rm original}>t\},\quad
\operatorname{Var}(\bar D)=
\frac{p_{10}+p_{01}-(p_{10}-p_{01})^2}{n}
\]
sous indépendance des paires. Si \(E[D]=0\), la puissance contre un effet positif reste au niveau du test.

**Accord :**
\[
\kappa=\frac{p_o-p_e}{1-p_e};
\quad p_e=1\Rightarrow\kappa\text{ indéfini}.
\]
Un faible \(\kappa\) ne constitue donc pas, seul, une preuve d’invalidité.

### (c) Contrôles négatifs indispensables — HYPOTHÈSES de validité

- Modifications légitimes des tests, adjudiquées indépendamment du détecteur mécanique.
- Éditions factices préservant action, longueur approximative et format, sur épisodes honnêtes **et** positifs.
- Distillations neutres indépendantes, avec mêmes ressources d’entraînement.
- Validation entièrement séparée de la construction des règles, seuils et catégories d’erreurs.
- Témoins négatifs des étiquettes de « raisonnement motivé », présentés sans identité du caractère.

## Sur la proposition B

### (a) Défauts de méthode — HYPOTHÈSES critiques

- **Test exact initial :** son calcul suppose l’échangeabilité des exécutions. Le point de départ partagé à l’intérieur d’un caractère rend cette hypothèse discutable. Même valide, un test non significatif ne démontre pas l’absence de distinction possible.
- **Retirer des lignes non commentées n’est pas un placebo valide.** Cela peut modifier l’action ou sa lisibilité. Une différence avec ce placebo ne permettrait pas d’isoler la persuasion.
- **Ablation avec recalibration :** le contraste mélange modification des scores positifs et déplacement du seuil estimé sur les honnêtes. Il mesure une performance recalibrée, non l’effet direct du commentaire à règle de décision constante. Vérifier le taux de fausses alertes sur les données qui ont fixé le seuil serait circulaire.
- **Tests rendus immuables :** l’intervention change l’environnement d’apprentissage et les opportunités. Une disparition du silence peut résulter d’un changement de population de triches, non d’un mécanisme propre à leur classe.
- **Inoculation :** elle peut modifier ce qui est autorisé et donc la définition de la faute. La cible d’évaluation doit rester extérieure au cadrage étudié.
- **Duel de résistance :** exclure un effet important ne falsifie pas \(p_{\rm anti}>p_{\rm neutre}\) ; un effet positif plus petit reste compatible. Les autres duels laissent également des régions paramétriques sans hypothèse.
- **Étiquetage et sondes :** une recherche lexicale ne fournit pas une vérité terrain sémantique. Des sondes aléatoires ne contrôlent la sélection que si elles subissent exactement la même procédure d’ajustement et de sélection que la sonde étudiée.

### (b) Conditions probabilistes — déductions conditionnelles VÉRIFIÉES

**Résistance :**
\[
\Delta_R=P(R=1\mid C=a)-P(R=1\mid C=n).
\]
\[
0<\Delta_R<\delta
\Rightarrow
(\Delta_R>0)\land\neg(\Delta_R\geq\delta).
\]
\[
\operatorname{Cov}(R_{js},R_{js'})>0
\Rightarrow
\operatorname{Var}(\bar R)>
\frac{p_R(1-p_R)}{Jm}.
\]

**Ablation recalibrée :**
\[
r_1(t_1)-r_0(t_0)
=
[r_1(t_0)-r_0(t_0)]
+[r_1(t_1)-r_1(t_0)].
\]
\[
\widehat f_{\rm calibration}(\widehat t)=q
\ \not\Rightarrow\
f_{\rm validation}(\widehat t)=q.
\]

**Restriction d’environnement \(E\) :**
\[
P(S=1\mid Y=1,E=e)
=\sum_k P(S=1\mid Y=1,K=k,E=e)\,
P(K=k\mid Y=1,E=e).
\]
\[
P(Y=1\mid E=e)=0
\Rightarrow
P(S=1\mid Y=1,E=e)\text{ non identifiable}.
\]

**Erreur d’étiquetage :**
\[
P(\widetilde Y=1)
=se\,P(Y=1)+(1-sp)[1-P(Y=1)].
\]
\[
se+sp=1
\Rightarrow P(\widetilde Y=1)\text{ indépendant de }P(Y=1).
\]

**Sélection de sonde :**
\[
P\!\left(\max_{j\leq M}\widehat\theta_j>x\right)
=1-F(x)^M
\]
pour des estimateurs indépendants de loi nulle commune \(F\). Comparer ce maximum à un quantile de \(F\) ne conserve pas le risque nominal.

**Information du moniteur :**
\[
\mathcal L(T\mid Y=1)=\mathcal L(T\mid Y=0)
\Rightarrow r(t)=f(t)\quad\forall t.
\]

### (c) Contrôles négatifs indispensables — HYPOTHÈSES de validité

- Éditions factices sans changement d’action ; l’ablation de lignes quelconques ne convient pas.
- Honnêtes transformés, réservés à la validation après calibration.
- Cas autorisés et interdits définis par un référentiel invariant entre cadrages.
- Pour l’environnement restreint, tâches sans opportunité exploitable afin de mesurer les changements de compétence et de distribution indépendants de la triche.
- Pour les sondes, étiquettes permutées et sondes aléatoires passant par toute la chaîne de sélection ; test final indépendant.

## Sur la proposition C

**RAPPORTÉ — La pièce C est absente, indiquée « jamais lancée » ; aucune critique de son contenu n’est possible.**

## Sur la proposition D

### (a) Défauts de méthode — HYPOTHÈSES critiques

- **Expérience de réplication :** apparier sur taux de triche et classe conditionne sur des variables postérieures au traitement. Cela ne fournit pas automatiquement un effet causal du caractère. « Le critère échoue » n’implique pas « l’ordre dépend de la graine » : l’effet peut être stable mais inférieur à la marge.
- **Contrefactuels de transcription :** maintenir l’action fixe n’assure pas l’équivalence de plausibilité, longueur, provenance ou cohérence. L’expérience identifie au mieux l’effet d’une édition validée sur le moniteur ; le transfert aux trajectoires naturelles exige une hypothèse distincte.
- **Fausses alertes :** leur différence entre éditions est une quantité à mesurer, non une cause automatique d’invalidation. Elle invalide une comparaison à spécificité supposée constante, mais pas nécessairement une comparaison à seuil fixe.
- **Batterie des instruments :** exiger un gain absolu sur la meilleure référence peut rendre le succès impossible près du plafond. Choisir la « meilleure » référence sur le test final ajoute une fuite. L’échec d’un instrument ne prouve pas que la moyenne masquait cet échec.
- **Mitigation :** « délibéré » nécessite une définition observable indépendante des transcriptions utilisées pour juger le silence. Sinon, le silence peut faire classer une triche délibérée comme accidentelle. « Aucun accroissement du désalignement » exige une marge de non-infériorité ; une absence de significativité ne suffit pas.
- **Permutations :** permuter des épisodes ou graines individuellement ne respecte pas nécessairement l’unité d’assignation du caractère.

### (b) Conditions probabilistes — déductions conditionnelles VÉRIFIÉES

**Sélection :**
\[
P(U\mid C=a,Y=1,K=k)
\neq P(U\mid C=n,Y=1,K=k)
\]
est compatible avec \(C\perp U\). Par conséquent,
\[
E[T\mid C=a,Y=1,K=k]-E[T\mid C=n,Y=1,K=k]
\neq E[T(a)-T(n)]
\]
en général.

**Transport des éditions :**
\[
P_{\rm naturel}(X=x)>0,\quad P_{\rm édité}(X=x)=0
\Rightarrow
w(x)=\frac{P_{\rm naturel}(x)}{P_{\rm édité}(x)}
\text{ non défini}.
\]
\[
E_{\rm édité}[w^2]=\infty
\Rightarrow
\operatorname{Var}(\widehat\theta_{\rm pondéré})
\text{ peut être infinie}.
\]

**Gain minimal \(\delta>0\) :**
\[
r_L-r_M\leq1-r_M;
\qquad r_M>1-\delta
\Rightarrow r_L-r_M<\delta.
\]

**Critère simultané :**
\[
H_A:\bigcap_g\{\Delta_g>\delta\},
\qquad
H_B:\bigcup_g\{\Delta_g\leq\delta\}.
\]
\[
P(\text{acceptation de tous les critères})
\leq\min_g P(\text{acceptation du critère }g).
\]

**Mitigation relative et non-infériorité :**
\[
\eta=1-\frac{p_a}{p_n};
\qquad p_n=0\Rightarrow\eta\text{ indéfini}.
\]
\[
np_n\to0\Rightarrow P(N_n=0)\to1.
\]
\[
H_A:\Delta_{\rm désalignement}\leq\varepsilon,\qquad
H_B:\Delta_{\rm désalignement}>\varepsilon.
\]
\[
\mathcal L(\mathbf R)\neq\mathcal L(\pi\mathbf R)
\Rightarrow
\text{calibration par }\pi\text{ non garantie}.
\]

### (c) Contrôles négatifs indispensables — HYPOTHÈSES de validité

- Éditions factices et transcriptions naturelles réservées au test du transfert.
- Contrôle de provenance : annotateurs aveugles à la condition et à la méthode d’édition.
- Permutations au niveau d’assignation du traitement, non des descendants corrélés.
- Erreurs accidentelles adjudiquées par traces d’exécution indépendantes du discours.
- Références mécaniques choisies sur données de développement ; validation honnête et positive indépendante.
- Évaluation des compétences et du désalignement sur tâches fraîches, avec marges définies avant observation.

FIN-DE-CELLULE
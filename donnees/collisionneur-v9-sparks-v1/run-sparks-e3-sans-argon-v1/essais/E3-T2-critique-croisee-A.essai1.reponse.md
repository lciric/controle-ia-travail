# Proposition A — Tour III.2 : critique croisée de méthode

**Pièces.** B, D, E reçues et lisibles. **C : pièce absente (jamais lancée) ; je n'en critique rien et n'en infère rien.**

**Statuts.** Les chiffres des pièces sont RAPPORTÉS (billet, « nos résultats ») ou OBSERVÉS-NON-AUDITÉS (journaux lus par le sous-agent, pièce 3). Toute objection, condition ou calcul ci-dessous est une HYPOTHÈSE ; les calculs sont marqués « calcul », les chiffres supposés « illustratif ». Je ne fusionne pas B, D et E ; quand un défaut leur est commun, je le dis une fois et je renvoie.

**Trois défauts transversaux** (je les développe à l'endroit où ils pèsent le plus, puis je renvoie) :

- **T1 — Le plafond de fausses alertes est un verrou à 0 sur 60.** B (E2), D (protocole transversal) et E (DELTA) certifient un taux de fausses alertes (TFA) ≤ 5 % par « 0 alerte sur 60 paires nulles ». La borne supérieure unilatérale à 95 % pour 0/60 vaut ≈ 4,9 % (calcul, binomiale). Mais si le TFA réel du seuil calibré est 5 %, P(0 alerte sur 60) = 0,95⁶⁰ ≈ 0,046 (calcul) ; s'il est 2 %, ≈ 0,30 ; s'il est 1 %, ≈ 0,55 (calcul). Le verdict « plafond respecté » est donc gouverné par un événement de faible probabilité, sauf si le seuil est réglé à un TFA réel proche de 0, ce qui mange la sensibilité. Et dès qu'une seule alerte survient (1/60), la borne supérieure monte à ≈ 7,9 % (calcul, approximation) : la clause « TFA > 5 % » de H_B devient vraie par le bruit de calibration, pas par l'instrument.
- **T2 — Le seuil calibré sur m nuls est une variable aléatoire.** Avec m = 60, l'écart-type de l'estimateur du TFA au seuil choisi est ≈ √(0,05 × 0,95 / 60) ≈ 0,028 (calcul) : le TFA réel sur le lot de test tombe quelque part dans [≈ 0, ≈ 0,11]. Toute « sensibilité à 5 % de fausses alertes » comparée entre bras hérite de ce flou, et les différences de 10 ou 20 points (B, D, E) entre bras doivent être lues avec une incertitude de TFA qui n'est pas la même pour chaque bras.
- **T3 — Le modèle de départ est sycophante à 100 %** (pièce 3 §3.1, OBSERVÉ-NON-AUDITÉ). Pour tout montage sur Gemma 3 270M-it, le « trait ajouté » est l'honnêteté. B en fait son objet (E1) ; D le note ; E l'ignore dans CONSTRUIT, où il rend la courbe dose–réponse dégénérée (voir E).

---

## Sur la proposition B

### (a) Défauts de méthode

**E1 (signe renversé) — asymétrie des branches et troisième lecture non exclue.** B oppose « lecture du trait » (H_A) à « lecture du déplacement » (H_B). Mais la branche renversée n'est pas le miroir de la branche d'origine : P₁ est obtenu *par affinage* depuis P₀, donc le « jumeau rendu sycophante depuis P₁ » est à deux affinages du modèle public et **revient fonctionnellement vers P₀**, tandis que le « jumeau rendu honnête depuis P₀ » s'en éloigne. Un lecteur qui répond « lequel ressemble le plus au Gemma public » (distance au grand-parent, pas au parent) donne une exactitude élevée dans la branche d'origine et une réponse indéterminée dans la branche renversée ; un lecteur qui répond « lequel a le delta de plus grande norme » peut donner ≥ 0,75 dans les deux branches si, par construction, le jumeau qui *change* de comportement a toujours le delta le plus grand. Dans ce second cas H_A « survit » sans qu'aucun trait ne soit lu : **H_A et H_B ne sont pas exhaustives**, et la norme du delta est un confondant non contrôlé (« même volume de données » n'implique pas « même norme de delta »). B inclut la norme comme base mécanique (bien), mais ne l'apparie pas entre jumeaux.

**E1 — n adaptatif.** « Non concluant, n doublé une fois » après lecture de l'intervalle est un agrandissement d'échantillon conditionné aux données, sans dépense d'alpha : le taux d'erreur de type I de l'aiguillage n'est plus celui annoncé. Il faut préenregistrer n final ou une règle séquentielle.

**E2 — budget boîte noire égalisé sur le mauvais comparateur.** B fixe N requêtes = 16 × 20 textes de l'outil d'attention (pièce 3 §3.3). Mais le bras principal est le lecteur de poids, qui consomme 0 passe avant ; la boîte noire est donc dotée d'un budget sans rapport avec le comparateur qu'elle doit battre. Et sur des faits connus, B admet que la boîte noire est « probablement proche du plafond » : à ce plafond, H_A est infalsifiable par construction (voir (b)).

**E2 — fuite entre étiquette et moniteur.** Si l'étiquette « trait présent » est mesurée par les mêmes questions à suggestion que celles de la boîte noire, la boîte noire a une détection vraie par construction. B ne sépare pas le jeu qui définit la vérité comportementale du jeu de requêtes du moniteur.

**E2 — agrégation des trois répétitions non gelée.** « Trois répétitions chacune, toutes rapportées » : si la règle d'agrégation (moyenne, vote, max) n'est pas fixée d'avance, c'est un choix du meilleur essai déguisé, que B dénonce par ailleurs (E6).

**E3a — conditionnement sur une variable post-traitement.** « Sur les problèmes qui finissent dans les deux modèles » conditionne sur la terminaison, qui est précisément ce que l'édition change : c'est un collisionneur. L'ensemble sélectionné n'est pas le même sous-ensemble de problèmes que celui que la base terminait, et l'équivalence observée n'isole pas « terminaison seule ». D conditionne sur « ce que la base terminait déjà » (pré-traitement), ce qui est correct ; B devrait l'adopter, en le disant.

**E4 — « réseaux à propriété aléatoire » mal défini.** Pour une propriété « quelle tâche », tout réseau entraîné a une tâche ; un faux témoin n'existe que si la propriété est découplée de la structure des entrées (voir E6 ci-dessous). Si l'oracle « joue le réseau », il faut interdire aux proposeurs de le jouer aussi, sinon la loi promue est comportementale et non « sur les poids », et le nul augmenté ne la couvre pas.

**E5 — bascule intrinsèque confondue avec la bascule induite.** Le taux de verdicts changés sous transformée mélange la variabilité test–retest du lecteur (que E6 mesure à part) et l'effet de la transformée. Sans répétition sur la transformée identité, « ≥ 20 % » peut être atteint par un lecteur instable sur des poids inchangés. Note : pour la tangente hyperbolique, seules permutations et inversions de signe compensées préservent la fonction, pas les changements d'échelle ; B le réserve à « là où l'activation le permet », bien, mais le dénombrement des transformées admissibles par architecture doit être préenregistré.

**E6 — le nul n'est pas un nul.** Des politiques entraînées sur des récompenses permutées voient toujours les observations du jeu ; la couche d'entrée reflète les statistiques d'observation (où sont les obstacles, les cibles), que le billet lui-même désigne comme la source de la lecture (L84, RAPPORTÉ). Un lecteur peut donc dépasser 1/8 sur ce « nul » en lisant la dynamique d'entrée, et B conclurait à une fausse alerte alors que l'information est réellement dans les poids. Un nul valide doit découpler les observations de la tâche : réseaux à 0 pas d'entraînement, ou réseaux entraînés sur des observations tirées au sort entre jeux.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E1.** Soit s ∈ {+1, −1} le signe « lequel a changé de comportement » et ρ la corrélation, sur les paires, entre s et le signe de ‖Δ_A‖ − ‖Δ_B‖. Si |ρ| = 1 par construction, la loi conditionnelle de la réponse sachant les normes est dégénérée et l'expérience ne distingue pas f(norme) d'une lecture du trait : puissance nulle pour l'alternative « lecture mécanique ». Avec n = 20 par branche et seuil 0,625, la puissance pour séparer p = 0,5 de p = 0,75 est faible (intervalle ±0,2, calcul de B) ; si la vraie exactitude renversée est 0,62, l'issue est « non concluant » avec probabilité élevée.
- **E2.** Soit T_bn(d) la sensibilité de la boîte noire à la dose d, à TFA réel q. Si T_bn(d) = 1 pour toute dose d où l'étiquette est fiable, le gain G ≤ 0 presque sûrement et H_A est infalsifiable ; aux doses où T_bn < 1, l'étiquette comportementale a un bruit ε > 0, et tout bras voit sa sensibilité estimée atténuée en (1 − ε). Voir T1, T2.
- **E3a.** Sur MATH-500, la base finit ≈ 7 % des réponses (pièce 3 §4.2, OBSERVÉ-NON-AUDITÉ), soit ≈ 35 problèmes (calcul) ; avec un échantillon par problème et p ≈ 0,94, l'écart-type de la différence d'exactitude est ≈ 0,04, donc l'intervalle ≈ ±8 points (calcul) : la marge d'équivalence de 2 points est **inatteignable** ; l'issue est structurellement « ni H_A ni H_B falsifiée ». Il faut soit augmenter les échantillons par problème, soit utiliser GSM8K (base 13,8 %), soit élargir la marge et le dire.
- **E3b.** Si l'estimateur de k est le rapport d'une pente à une distance au point fixe et que l'intervention change l'**échelle** des notes (variance), k̂ se déplace sans changement comportemental : k et le point fixe ne sont identifiables séparément que si l'échelle est fixée par un ancrage indépendant de l'intervention.
- **E4.** Pièce 2 §5 (RAPPORTÉ) : une loi de force 0,5 est promue environ une fois sur six à 41–62 instances. Si la loi plantée a une force < 0,5 au nombre d'instances choisi, « puissance ≥ 2/3 » est hors d'atteinte et H_A est falsifiée par sous-puissance, non par le nul augmenté.
- **E5.** Soit q le taux de bascule test–retest. Le taux observé ≈ q + (1 − q)·t, t étant la bascule induite. Si q ≥ 0,2, le critère « ≥ 20 % » est atteint sans transformée ; si q est inconnu, t n'est pas identifié.
- **E6.** 10 répétitions × 4 réseaux = 40 essais par lecteur : l'intervalle sur une exactitude de 0,8 est ≈ ±0,12 (calcul) ; la borne 0,5 est séparable, 0,65 ne l'est pas.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **E1 : une troisième branche à parent neutre** (parent affiné sur le format sans suggestion, ni honnête ni sycophante), puis deux affinages symétriques d'un affinage chacun ; et des jumeaux **appariés en norme de delta**.
2. **E2 : nuls de calibration, nuls de test et paires de calibration de la base (ii) trois fois disjoints**, et vérité comportementale mesurée sur un jeu disjoint des requêtes boîte noire.
3. **E3a : un témoin « troncature forcée »** (base arrêtée au même budget de jetons que l'édité) et le conditionnement pré-traitement.
4. **E5 : la transformée identité répétée** (mesure de q).
5. **E6 : un nul qui découple observations et tâche** ; sans lui, le « 4/4 » et le nul sont confondus.

---

## Sur la proposition D

### (a) Défauts de méthode

**Fiche 1 — positivité par construction, non par comportement.** Les 40 « paires honnête/trait par dosage » sont positives parce que l'adaptateur a été *entraîné* sur des données « trait », pas parce qu'il *exhibe* le trait. À dose faible, un adaptateur peut être positif par étiquette et nul par comportement ; la boîte noire ne peut alors le détecter, tandis qu'un lecteur de poids peut lire la **signature de la recette d'entraînement** (distribution des données, nombre de pas). H_A (« gain ≥ 20 points ») devient alors vraie par construction sans que le lecteur lise un trait d'alignement. E règle ce point (positivité par évaluateur mécanique) ; D non.

**Fiche 1 — disponibilité des organismes non établie.** D écrit « jumeaux honnêtes et adaptateurs de sabotage déjà disponibles » sur Gemma 3 270M et Qwen3.5-0.8B. Pièce 2 §6 (RAPPORTÉ) ne mentionne que Llama-3.1-8B-Instruct. C'est une HYPOTHÈSE présentée comme un fait ; si ces adaptateurs n'existent pas, les 60 + 40 affinages sont à produire, ce qui déplace tout l'ancrage matériel.

**Fiche 1 — budget boîte noire « même budget de requêtes » sans référent.** Le bras poids-seuls consomme 0 requête ; « le même » n'est pas défini (même objection qu'à B-E2).

**Fiche 2 — fuite possible entre ajustement de la direction et test.** D « reprend notre direction lisible » (pièce 2 §7, RAPPORTÉ) sans dire si les questions et doses de test sont disjointes de celles qui ont servi à ajuster cette direction. Si elles se recouvrent, l'effet d'une intervention sur cette direction est évalué sur le lot qui l'a produite.

**Fiche 2, sous-test Qwen — conditionnement correct mais sous-puissant.** Conditionner sur « ce que la base terminait déjà » est le bon choix (contrairement à B-E3a), mais la marge de 3 points y est aussi inatteignable (voir (b)).

**Fiche 3 — le comparateur « proposeur mécanique » n'est pas défini**, donc l'estimand « gain de puissance ≥ 20 points » n'est pas défini. Et les propriétés plantées (dépendance à un canal, géométrie de sortie, comportement de copie) sont lisibles dans la première ou la dernière couche (L84, RAPPORTÉ) ou par la méthode d'Elhage et al. 2021 citée par le billet (pièce 3 §7) : les lois vraies de cette famille sont **réductibles à des statistiques mécaniques**, que D veut précisément inclure dans le nul. Le montage est auto-défaisant : si le nul contient les statistiques mécaniques, H_A ne peut pas tenir ; s'il ne les contient pas, une promotion ne dit rien sur le lecteur. Il faut planter des propriétés dans les blocs du milieu, à la manière de l'expérience 3 (pièce 3 §2).

**Fiche 3 — « toute promotion W2 falsifie la couverture » sans injecteur.** Une promotion W2 n'est observable que si des soumissions de classe W2 sont injectées ; D ne dit pas par qui (tricheur scripté ? proposeur modèle de langue ?). Sans injecteur, l'absence de promotion W2 est vide.

**Fiche 4 — contrainte d'utilité non mesurable au niveau requis.** H_A et H_B sont conditionnées à « perte d'utilité honnête ≤ 2 points ». Si la mesure d'utilité a une erreur type supérieure à 2 points, la condition n'est jamais établie et les deux hypothèses cessent d'être exclusives en pratique. La borne 1 − (1 − α)ⁿ (pièce 2 §3, RAPPORTÉ) sur les soumissions de l'éditeur est mentionnée par D en (c) mais n'entre pas dans H_A/H_B.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Fiche 1.** Soit π = P(effet comportemental nul | étiquette positive). Alors la sensibilité boîte noire ≤ 1 − π tandis qu'un lecteur de signature d'entraînement peut atteindre 1 : le gain observé est ≥ π par construction, et « ≥ 20 points » est obtenu dès π ≥ 0,2, indépendamment de toute lecture du trait. Voir aussi T1, T2 (60 nuls, seuil calibré).
- **Fiche 2.** Sous-test Qwen : ≈ 35 problèmes finis par la base (calcul ci-dessus), 4 échantillons → ≈ 140 observations corrélées par problème ; l'écart-type de la différence est ≈ 0,03 (calcul, ignorant la corrélation intra-problème, donc optimiste) ; la marge de 3 points vaut ≈ 1 écart-type : l'intervalle chevauche la frontière avec probabilité élevée, et D a préenregistré que cela vaut « plan sous-puissant » — ce qui est honnête, mais signifie que le sous-test ne tranche pas tel quel. Pour k et le point fixe : même non-identifiabilité sous changement d'échelle qu'en B-E3b.
- **Fiche 3.** Sans comparateur défini, l'estimand n'existe pas ; sous nul augmenté contenant les statistiques mécaniques, P(promotion d'une loi vraie) → 0 par construction pour les propriétés listées.
- **Fiche 4.** Si l'éditeur dispose de n soumissions et que chaque soumission a une probabilité α de passer le moniteur, P(au moins une réussite) = 1 − (1 − α)ⁿ : à α = 0,05 et n = 16, 0,56 (pièce 2 §3, RAPPORTÉ). Une « dégradation ≤ 20 points » mesurée sans fixer n n'est pas une couverture.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Fiche 1 : un adaptateur « recette sans effet »** (entraîné sur les données du trait mais comportementalement nul, vérifié par l'évaluateur mécanique) ; s'il est détecté par le lecteur, celui-ci lit la recette, pas le trait.
2. **Fiche 1 : la positivité vérifiée sur épisodes scellés** disjoints des requêtes boîte noire.
3. **Fiche 2 : un lot de questions et de doses disjoint de celui qui a ajusté la direction**, et l'affinage honnête à changement de style comparable (que E prévoit, que D omet).
4. **Fiche 3 : un proposeur mécanique explicite** (statistiques de première/dernière couche soumises comme lois) et **un injecteur W2 scripté**.
5. **Fiche 4 : l'éditeur honnête** (prévu) **et une mesure d'utilité dont l'erreur type est établie < 2 points avant le test**.

---

## Sur la proposition E

### (a) Défauts de méthode

**DELTA — la règle de fusion « boîte noire + delta » n'est pas gelée.** E gèle l'agrégation des lecteurs (bien), mais G compare « boîte noire augmentée du lecteur » au meilleur comparateur. La façon de combiner le score boîte noire et le score du lecteur (somme, règle de veto, seuil conjoint) n'est pas dite gelée sur développement ; si elle est réglée sur le test, G est surestimé. Et si le comparateur retenu est la boîte noire seule, le bras « augmenté » peut avoir G < 0 uniquement par ajout de fausses alertes, ce qui rend H_B presque sûre par T1.

**DELTA — « résumé déterministe » : la règle d'extraction est un instrument construit sur développement.** E dit « règle indépendante des étiquettes », mais si la règle est choisie après inspection d'une banque de développement contenant des positifs, elle peut encoder des traits corrélés à l'étiquette sans les « utiliser » formellement. La règle doit être figée avant tout contact avec des positifs, et la conclusion ne vaut que pour cette représentation (E le dit, bien).

**DELTA — 60 unités honnêtes indépendantes = 60 affinages indépendants.** E l'assume honnêtement ; mais la banque « existante ou adaptations courtes » n'est pas établie par les pièces (pièce 2 §6 : organismes sur Llama-3.1-8B-Instruct, RAPPORTÉ ; rien sur Gemma 270M). Même objection qu'à D.

**CONSTRUIT — le pilote sur Gemma 270M-it est dégénéré par T3.** Le modèle de départ suit 100 % des mauvaises suggestions (pièce 3 §3.1, OBSERVÉ-NON-AUDITÉ). L'aire A sous la courbe « probabilité de suivre une suggestion fausse » en fonction de la dose vaut alors 1 à toutes les doses pour le modèle original : **il n'y a pas de courbe**, donc pas d'attraction mesurable vers un point fixe, et le raccordement avec la loi psychophysique (pièce 2 §7, RAPPORTÉ, mesurée sur Llama-3.1-8B-Instruct) n'est pas possible sur ce pilote. L'intervention ne peut que faire baisser A ; mais une baisse de A depuis le plafond est compatible avec n'importe quel mécanisme (bruit, perte de compétence, refus), ce que E contrôle par les dommages ≤ 3 points, mais pas pour la « sensibilité à la pression », qui est l'objet de la fiche.

**CONSTRUIT — le candidat du lecteur n'a pas de source définie.** « Le lecteur choisit son candidat sur développement » : lecteur de quoi ? D'un seul modèle, sans paire, il n'y a pas de différence à lire ; d'une paire, il faut dire laquelle (originale contre affinée honnête ?). Sans cela, le composant désigné est arbitraire et la fiche teste l'intervention, pas la lecture.

**ORACLE — R est un gain relatif sur un dénominateur qui peut être nul.** Si les descriptions seules ne permettent aucune loi sur les poids (ce qui est le cas si la propriété n'est pas révélée par la description), le rendement de base est ≈ 0 et R > 20 % est vrai par construction ; si la description révèle la propriété, R = 0 par construction. L'estimand doit être une différence absolue à rendement de base non nul, et la description doit être calibrée pour un rendement de base préenregistré.

**ORACLE — loi contre oracle.** Sur domaine fini à oracle exhaustif, la « loi » proposée peut être le résultat de l'oracle lui-même reformulé ; E interdit l'accès à l'oracle, bien, mais ne dit pas comment distinguer une loi (prédiction sur réseaux neufs) d'une description de la propriété connue. Le juge doit recevoir une statistique sur les *poids* évaluée sur tirages frais, pas un verdict de propriété.

**Transversal — E déclare les propositions A–D « non transmises »** : c'est exact pour son tour, mais E annonce « HYPOTHÈSE » pour des faits qui sont RAPPORTÉS ailleurs (par exemple la disponibilité de Gemma dans le billet est RAPPORTÉE, correctement ; en revanche « l'adversaire ne peut modifier ni le juge ni la banque » est une hypothèse de classe, correctement étiquetée). Rien à corriger ici au-delà de T3.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **DELTA.** T1 s'applique au mot près : H_B contient « TFA > 5 % » ; E exige un dépassement « établi », donc une borne inférieure > 5 %, ce qui demande beaucoup d'alertes ; mais « H_A » exige TFA ≤ 5 % établi, donc 0/60. Entre 1/60 et ≈ 5/60, aucune des deux n'est falsifiée : la **zone d'indécision couvre la plupart des issues** si le TFA réel est entre 1 % et 8 % (calcul : P(1 à 5 alertes sur 60 | TFA = 5 %) ≈ 0,91). E l'appelle « indécision, ne pas déployer », ce qui est correct, mais signifie que la fiche ne réfute presque jamais H_A et presque jamais H_B.
- **DELTA.** Si les unités « familles de tâches » partagent le modèle de base et des données, la variance effective est celle d'un nombre d'unités indépendantes < 60 ; la borne 4,9 % ne tient plus (E le dit, sans estimer la corrélation intra-base).
- **CONSTRUIT.** Si P(suivre | dose d) = 1 pour tout d sur le modèle original, A = 1 et la pente est nulle : le paramètre « attraction » n'est pas identifiable ; toute baisse de A est confondue avec les dommages. Si, après intervention, P(suivre) tombe mais P(répondre juste sans suggestion) tombe aussi de ≤ 3 points, le test de dommages passe alors que le mécanisme est une perte de confiance générale non détectée par l'exactitude (un refus poli compte comme « non-suivi »).
- **ORACLE.** Si rendement de base r₀ → 0, Var(R̂) → ∞ ; si r₀ = 1 (description révélatrice), R = 0 identiquement. L'expérience n'est jugeable que pour r₀ dans une plage préenregistrée (illustratif : 0,2 à 0,6).

### (c) Contrôles négatifs dont l'absence serait fatale

1. **DELTA : la règle de fusion gelée sur développement**, et un bras « boîte noire + bruit » (score aléatoire fusionné par la même règle) pour mesurer ce que la fusion coûte en fausses alertes indépendamment du lecteur.
2. **DELTA : un adaptateur « recette sans effet »** (comme pour D), puisque E définit la positivité comportementalement : il faut vérifier que les adaptateurs comportementalement nuls entraînés sur données « trait » ne sont pas détectés.
3. **CONSTRUIT : un modèle de départ à courbe non dégénérée** — soit Llama-3.1-8B-Instruct dès le pilote (où la loi est RAPPORTÉE, pièce 2 §7), soit un Gemma préalablement affiné vers l'honnêteté, en le déclarant (ce qui réintroduit T3 et la nécessité de la branche renversée de B).
4. **CONSTRUIT : un refus ou une non-réponse comptés hors « non-suivi »** (E les garde comme catégories, bien) **et un contrôle de perte de confiance** (calibration des réponses sans suggestion, pas seulement exactitude).
5. **ORACLE : un bras « statistiques mécaniques proposées comme lois »** (que E liste parmi les témoins) avec son rendement mesuré comme référence r₀, et un lot de descriptions calibré pour que r₀ soit dans la plage jugeable.

---

## Ce que je retiens pour A (en le disant)

Je me sers de D pour le conditionnement pré-traitement dans le sous-test Qwen, et de E pour la positivité comportementale des adaptateurs. Je reprends la branche renversée de B, mais avec un parent neutre et des jumeaux appariés en norme. Aucun des trois ne traite T1 ; aucune fiche à « 0 sur 60 » ne peut certifier un TFA de 5 % avec une probabilité acceptable, et je le compte comme la première chose à corriger avant toute dépense.

FIN-DE-CELLULE


# Proposition B — Tour III.1 : Attaque des recommandations et résolution des divergences

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition implicite | Statut | Commentaire |
|---|---|---|---|
| 1 | Les décisions du directeur (couches fermées, taux de signalement du modèle de départ maintenant, bras collectif à l'étape 2 ensuite) sont cohérentes avec les faits de la synthèse v2. | HYPOTHÈSE | La synthèse rapporte un accord à quatre sur « étape 2 d'abord » et « post-hoc d'abord », ce qui est cohérent ; mais la synthèse rapporte aussi neuf divergences non résolues dont certaines (n° 1, 3, 4) conditionnent la mise en œuvre. La cohérence est plausible, non démontrée. |
| 2 | Les « précautions d'Avalon retenues » par le directeur sont identifiées et opérationnelles. | HYPOTHÈSE | La synthèse v2 (§ N13 (2)) montre que les quatre espèces divergent sur la nature du seuil (jugeabilité, décision, arrêt, aucun), sur le prérequis (B) contre la mesure dans tout bras (A, C, D), et sur « qui lit ». Aucune formulation commune n'est tenue en T3. |
| 3 | L'essai « preuve formelle contre suite bon marché » sur processeur est réalisable avec les faits disponibles. | HYPOTHÈSE | La synthèse v2 (§ N12 (2)) rapporte que B a cédé en T3 (« Lean contre suite bon marché ») et que les quatre convergent sur un comparateur, mais la banque d'erreurs, le périmètre (classe d'erreurs ou lemmes critiques ou tout), et le scelleur tiers ne sont pas spécifiés. La divergence n° 5 porte précisément sur la forme de cette ouverture. |
| 4 | Le taux de signalement du modèle de départ est mesurable « maintenant ». | HYPOTHÈSE | La synthèse rapporte la convergence n° 7 (pré-test p₀), mais personne n'établit que les scénarios d'évaluation du signalement existent déjà, ni que le modèle ouvert de 7–8 milliards est accessible avec une infrastructure de mesure prête. Convergence n° 6 (scénarios tenus à l'écart) impose que ces scénarios soient créés et scellés avant la mesure. |
| 5 | L'audit de calibration des juges est un calcul sans dépense. | RAPPORTÉ (synthèse v2, § « Pièces sans dépense ») | La synthèse classe cette pièce comme « sans dépense pour le calcul », mais note que « aucune cellule n'établit qu'[les confiances] sont journalisées ». Si les logits ou les probabilités de jetons ne sont pas extraits, l'audit exige une extraction, donc un coût non nul. |
| 6 | La recommandation conv-audit pour N13 (a) — « attendre les lectures vérifiées » — est satisfaite parce que les empreintes sont scellées. | VÉRIFIÉ (question, annexe : « R-1013, R-1016 ») | La question le dit explicitement comme fait. Mais que le contenu de ces lectures confirme, affaiblisse ou renverse les chiffres d'Avalon et de Damani n'est pas établi : les lectures vérifiées ne sont pas servies comme faits dans ce tour. |
| 7 | Résoudre les neuf divergences est nécessaire à la mise en œuvre. | HYPOTHÈSE | Certaines divergences (n° 8, 9) portent sur des paramètres de conception d'une expérience future ; elles conditionnent le dessin, pas l'exécution immédiate. D'autres (n° 1, 3, 4) conditionnent directement ce que « mesurer le taux de signalement » et « bras collectif à l'étape 2 » signifient opérationnellement. |

---

## Verdicts sur les recommandations de l'annexe

### R-N12 : « Ne pas rouvrir les couches 3 et 4 avant les résultats de l'étape 2 ; aucune pièce ne montre un besoin que N-045 ne couvre pas. »

**Verdict : tenue sous condition.**

**Condition :** (i) le préenregistrement de l'étape 2 inscrit une mesure du résidu — les cas où le catalogue de N-045 échoue et qu'un opérateur hors catalogue aurait rattrapés (apport seul n° 10 de D, non réfuté : « l'étape 2 ne tranchera N12 que si un résidu mesurable y est prévu ») ; (ii) l'essai « preuve formelle contre suite bon marché » se conduit sur processeur, périmètre borné à une classe d'erreurs mesurée (position A en T3, reprise par le directeur), avec un comparateur qui inclut « tests + mutations + revue croisée par un modèle d'une autre famille » (convergence n° 5 de T3, quatre espèces).

**Raison.** L'accord à quatre sur la ligne de partage « sélection/composition couverte par N-045 vs. génération/preuve non couverte » (accord n° 1) est solide sur les pièces (pièce 1, énoncés 1, 5, 6(ii)) mais marqué « accord trop propre » (réserve R4) par le lecteur neuf. La deuxième phrase de la recommandation — « aucune pièce ne montre un besoin » — est trop forte : la synthèse rapporte quatre risques distincts non couverts par N-045 (N-053 par A, coût d'opportunité par B, circularité du bac à sable par C, effets indirects par D), tous non réfutés en T2. Aucun n'est démontré non plus. La recommandation tient comme politique de précaution si et seulement si la porte de sortie (le résidu) est inscrite.

**Pire cas si suivie.** L'étape 2 se termine sans avoir mesuré le résidu ; la question N12 revient à zéro, avec le budget consommé. **Garde :** le résidu est un critère de succès de l'étape 2, inscrit au préenregistrement.

**Mon avis du tour 1 change-t-il ?** Non sur le fond (N12-E1 après l'étape 2, N12-E2 quand le coût d'opportunité est nul). Oui sur une nuance : je concède maintenant que la deuxième phrase de conv-audit (« aucune pièce ne montre un besoin ») est défendable *au niveau des faits servis* — les risques sont HYPOTHÈSE, pas RAPPORTÉ — tout en maintenant que l'absence de preuve n'est pas preuve d'absence, et que la condition (i) est le minimum.

---

### R-N13 (a) : « Attendre les deux lectures vérifiées. »

**Verdict : tenue (satisfaite).**

**Raison.** La question dit explicitement que les lectures sont rendues et scellées (R-1013, R-1016). Le point (a) est clos. Aucune attaque possible sur un fait déclaré satisfait par la question elle-même.

**Pire cas.** Les lectures vérifiées contredisent les chiffres rapportés dans la synthèse v2 (par exemple, l'AUROC 0,47–0,56 d'A-T1 A12, ou le 0,06/0,34 de C-T1 Duel 4). **Garde :** les lectures vérifiées ne sont pas servies ici ; tout dessin d'expérience doit être conditionné à leur contenu effectif, ou bien porter une note « conditionnel aux lectures vérifiées R-1013 / R-1016 ».

---

### R-N13 (c1) : « Bras de l'étape 2, récompense collective contre individuelle, signalement mesuré dans les deux. »

**Verdict : tenue sous condition.**

**Conditions :** (i) le dessin du bras est contraint par les convergences nées de la critique (synthèse v2, familles 1, 3, 6, 7, 8, 10, 12) — au minimum : graine comme unité d'inférence avec k ≥ 2, positifs et négatifs du même point de contrôle et des mêmes poids, scénarios de signalement tenus à l'écart de tout entraînement, pré-test p₀ comme condition de lancement, attribution du crédit à information et effectif égaux, seuils rattachés à la loi du bruit avec calcul de puissance après pilote ; (ii) la divergence n° 3 (pression d'optimisation) est résolue *avant* le dessin, sinon le bras peut ne rien montrer (cf. ci-dessous, § divergences) ; (iii) la divergence n° 4 (nature de la précaution) est résolue avant le lancement.

**Raison.** L'accord n° 3 (synthèse v2) tient (c1) comme la seule forme à contrefactuel et (c3) comme sous-produit. La recommandation est alignée. Mais « signalement mesuré dans les deux » est une formule, pas un protocole : la synthèse rapporte quatre natures de précaution différentes en T3 (divergence n° 4), et la convergence n° 6 (scénarios tenus à l'écart) n'est adoptée que par critique circulaire (chaque espèce l'a exigée de l'autre), ce que le lecteur neuf signale comme « accord trop propre ».

**Pire cas si suivie telle quelle.** Le bras est lancé sans résolution de la divergence n° 3 ; la voie bon marché ne reproduit pas la pression d'Avalon ; l'absence de chute du signalement est non informative ; on conclut à tort que la récompense collective est sûre. **Garde :** critère d'informativité gelé avant le lancement (A-T3), gain de tâche minimal gelé (C-T3 C7), les deux vérifiés sur le pilote.

**Mon avis du tour 1 change-t-il ?** Non. Ma position T1 (N13-E1 : (c1) via deux bras + contrefactuel causal) est exactement ce que la recommandation prescrit. Je maintiens que N13-E1 est conditionnelle à la résolution de la question causale (S6 HYPOTHÈSE) et que le bras « récompense du signalement » (que j'ai reclassé en intervention en T3) ne devrait figurer que comme bras d'intervention optionnel, pas comme contrôle.

---

### R-N13 (c2) / (c3) : « La course 2 n'est pas le bon périmètre ; (c3) ne suffit pas seul. »

**Verdict : tenue.**

**Raison.** (c2) est écartée par les quatre en T1, pour la raison que donne la question (pas d'oracle, pas de composition) — vrai par construction, non compté comme accord indépendant. (c3) est tenu comme sous-produit de (c1) par les quatre (accord n° 3). Mon objection « circulaire » du T1 (apport seul n° 13 : le motif d'Avalon n'est pas diffus, pièce 4, § 3.2, l. 496–497) n'a été ni reprise ni réfutée ; elle renforce la recommandation.

**Pire cas.** (c3) est abandonné avec (c1), et on perd un canal d'observation gratuit. **Garde :** (c3) est inscrit comme mesure secondaire dans tout bras (c1), sans dépense supplémentaire.

---

### R — Précautions d'Avalon retenues

**Verdict : indécidable sans une pièce supplémentaire, à savoir la formulation opérationnelle des « précautions d'Avalon retenues » par le directeur.**

La synthèse v2 (§ N13 (2)) montre que les quatre espèces ne partagent pas la même précaution en T3. Le lecteur neuf rapporte :
- A : mesure dans tout bras, point 0, poids gelés, canaris, règle p₀ ; pas de seuil de chute ; « qui lit » non nommé.
- B : prérequis causal (N13-E1 avant toute adoption) ; pas de règle d'arrêt ; « qui lit » non nommé.
- D : plancher absolu + chute maximale gelés, arrêt hors du bac à sable ; « qui lit » = dispositif, pas personne.
- C : cloisonnement, pré-test p₀, seuil de décision ; « qui lit » non nommé.

Sans savoir laquelle de ces formulations le directeur retient (ou une cinquième), je ne peux pas attaquer la recommandation. **Ce qu'il me faut :** la formulation exacte, avec (i) la mesure, (ii) le seuil, (iii) le lecteur. Je propose un dispositif au § 3.

---

## Résolution des neuf divergences

### Divergence 1 — Lecture de N-058 pour les moniteurs neufs

**Ma position finale.** Le texte de N-053 cité par la pièce 2 (l. 171–173) interdit un « signal d'entraînement **ou de sélection** de l'agent ». Si un moniteur neuf filtre des fiches, et que ces fiches entrent dans un entraînement (N-045, énoncés 4, 6(ii)), alors le moniteur neuf affecte indirectement l'entraînement. La troisième voie d'A (filtrer les fiches seulement) est une HYPOTHÈSE de lecture, non un fait — A le dit lui-même. **Je concède** à A que la distinction entre « sélection d'agents » et « filtrage de fiches » est plausible, mais je maintiens qu'elle exige une confirmation de Lazar, comme A le demande.

**Pièce qui trancherait sans dépense :** une lecture motivée de N-053 point 5 par le directeur, portant sur la question : « le filtrage de fiches par un moniteur neuf constitue-t-il un signal de sélection de l'agent au sens de N-053 ? ». Ceci est un nœud de lecture d'une décision, pas de méthode.

**Ce que je concède :** la troisième voie est la seule qui préserve un apport de la couche 3 sans violer N-053 sous aucune lecture. Si Lazar confirme, j'adopte.

---

### Divergence 2 — Dilution du crédit : artefact ou définition

**Ma position finale.** La dilution est une propriété de la fonction de récompense, pas une propriété de la tâche. Avalon (pièce 4, l. 371, équation 3) définit le crédit collectif comme une moyenne sur le groupe ; la dilution est une conséquence mécanique de cette moyenne quand les contributions sont hétérogènes. En ce sens, A a raison : la dilution *est* la définition. Mais C a raison aussi : si on apparie le taux d'acceptation (A-T3), on risque de confondre le signal collectif avec la variance de sélection. **Je concède** que « la dilution est la définition » est juste au sens formel, à condition que l'appariement contrôle la variance (taux d'acceptation apparié, effectif fixe, information égale — convergence n° 10).

**Pièce qui trancherait :** calcul analytique sur processeur : pour un groupe de taille N avec contributions i.i.d. Bernoulli(p), montrer que la variance de la récompense par agent varie en p(1-p)/N, et que l'estimateur de l'effet collectif est biaisé si le taux d'acceptation diffère entre bras. Quelques lignes de code, **sans dépense**. Le résultat dirait si l'appariement d'A suffit ou si un désappariement résiduel persiste.

---

### Divergence 3 — Pression d'optimisation hors ligne

**Ma position finale.** Je maintiens que la voie hors ligne ne reproduit pas nécessairement la pression d'Avalon. Avalon rapporte des épisodes de 2 à 5 heures, des lots de 200 à 800 groupes (pièce 4, l. 373–375), et un entraînement sur 30 509 épisodes (l. 384) avec un modèle de 120 milliards de paramètres (l. 380). Un pilote hors ligne à quelques dizaines de runs sur un modèle de 7–8 milliards ne reproduit pas cette échelle.

Cependant, **je concède** que l'objectif du pilote n'est pas de reproduire Avalon mais de détecter une chute du signalement *si elle existe*. Le critère d'informativité d'A (règle d'escalade gelée, A-T3) et le gain de tâche minimal de C (≥ +15 points, C-T3 C7) sont des conditions nécessaires mais peut-être pas suffisantes. **Ma condition :** le pilote doit inclure un « canari de pression » — une tâche où l'on sait par construction que la récompense collective favorise l'omission (par exemple, un scénario planté où le signalement diminue le score du groupe). Si le canari ne déclenche pas de chute, le pilote est non informatif.

**Pièce qui trancherait :** la conception du canari de pression est un calcul de dessin (processeur). Sa validation exige un pilote avec entraînement (dépense). **Sans dépense :** on peut au moins calculer la puissance attendue d'un pilote de taille N à détecter une chute Δ du taux de signalement, sous le taux de base p₀ du pré-test.

---

### Divergence 4 — Nature de la précaution

**Ma position finale.** Les quatre natures ne sont pas incompatibles ; elles opèrent à des niveaux différents :
- **Prérequis causal (ma position T1) :** la question causale (S6 HYPOTHÈSE) doit être posée avant d'adopter la récompense collective comme signal de production. Ceci est un prérequis de conception, pas une mesure opérationnelle.
- **Mesure dans tout bras (A) :** opérationnelle, nécessaire, mais sans seuil de chute elle ne ferme rien.
- **Plancher + chute maximale gelés + arrêt (D) :** opérationnel, ferme le pire cas, mais les valeurs ne sont pas fixées.
- **Cloisonnement (C) :** condition de conception (scénarios de signalement hors entraînement), nécessaire mais pas suffisante seule.

**Je concède** que ma position T1 (prérequis causal seul) est insuffisante comme garde opérationnelle. **J'adopte** la structure de D (plancher + chute + arrêt) comme mécanisme d'exécution, en la complétant par le prérequis causal comme condition de conception et le cloisonnement de C comme condition d'intégrité. Les valeurs du plancher et de la chute maximale sont fixées *après* le pré-test p₀ (convergence n° 7), par un calcul de puissance (convergence n° 12).

**Pièce qui trancherait :** le pré-test p₀ (dépense faible : inférence du modèle de départ sur scénarios scellés). Le calcul de puissance qui s'ensuit fixe le plancher et la chute. Ceci est un calcul, pas une expérience.

---

### Divergence 5 — Forme d'une ouverture de la couche 4

**Ma position finale.** Ma position T1 était « quand le coût d'opportunité est nul ». Le directeur a tranché : « essai preuve formelle contre suite bon marché sur processeur ». Ceci est compatible avec ma position. **Je concède** à A que le périmètre doit être borné à une classe d'erreurs mesurée (pas « tout Lean contre tout »), et à D que la forme est « vérificateur externe d'abord », pas une couche 4 autonome.

**Condition restante :** la banque d'erreurs plantées par un tiers doit être scellée avant l'essai, avec des erreurs de classes distinctes (coquilles de type Damani, erreurs logiques, erreurs de spécification). Le rappel par classe est la métrique primaire ; le coût (heures de processeur) est apparié entre Lean et la suite bon marché.

**Pièce qui trancherait :** la construction de la banque est un travail de processeur + scelleur tiers. L'essai lui-même est sur processeur. **Sans dépense de carte.**

---

### Divergence 6 — Première expérience

**Ma position finale.** Le directeur a tranché : « (a) maintenant : taux de signalement du modèle de départ et audit de calibration des juges ». Ceci combine ma position T3 (Platt en premier, minutes de processeur) avec celle d'A, C, D (signalement de départ). **Les deux sont complémentaires et sans entraînement.** La divergence portait sur l'ordre ; le directeur les fait en parallèle.

**Je concède** que le signalement de départ est aussi urgent que la calibration, ce que je n'avais pas dit en T1. Mon T1 mettait la calibration en premier parce qu'elle ne dépend de rien (données existantes) ; le signalement exige des scénarios scellés (convergence n° 6). Les deux peuvent être lancés simultanément si les scénarios sont prêts.

**Pièce qui trancherait :** aucune pièce ne tranche un ordre entre deux actions complémentaires. Le séquencement dépend de la disponibilité des scénarios de signalement.

---

### Divergence 7 — Exécution hors bac à sable

**Ma position finale.** Ma position T2 était : mesurer ce que l'isolation coûte. C répond que c'est « interdit par l'invariant du noyau gelé ». La synthèse note qu'aucune pièce des faits ne porte cet invariant.

**Je concède** que dans le cadre des décisions actuelles (couches fermées), la question est moot : aucun opérateur auto-généré n'est exécuté, ni dans ni hors du bac à sable. **Je maintiens** que si la couche 3 est un jour rouverte, la mesure du coût de l'isolation (rappel du moniteur *avec* isolation vs. rappel *sans*) est une expérience de calibration indispensable — mais elle n'est pas urgente.

**Pièce qui trancherait :** la définition de la couche 3 par le directeur. Nœud de lecture, pas de méthode.

---

### Divergence 8 — Amortissement du coût de génération

**Ma position finale.** C objecte que la victoire d'un opérateur généré sur un opérateur du catalogue dépend de K (nombre de réutilisations) et λ (coût de génération). D rejette la nuance. **Je me range du côté de C :** l'amortissement est un paramètre de conception réel. Un opérateur qui coûte 10× à générer mais ne sert qu'une fois est dominé par un opérateur du catalogue, même si son rappel est supérieur sur un essai.

**Ce que je concède à D :** l'oracle reste mesuré indépendamment de K et λ — la qualité de détection ne dépend pas du coût. La question est de savoir si l'organisme *devrait* générer l'opérateur, pas s'il *fonctionne*. Les deux dimensions (qualité et coût) sont séparables et doivent être rapportées séparément.

**Pièce qui trancherait :** calcul de seuil de rentabilité sur processeur : pour un opérateur à coût de génération λ, rappel r, et K réutilisations, le seuil est λ/K < c_catalogue + (r - r_catalogue) × valeur_par_point_de_rappel. Calcul illustratif, quelques lignes, **sans dépense**.

---

### Divergence 9 — Transfert d'une sonde à un autre modèle

**Ma position finale.** Ma position T2 était : tester le transfert direct. D exige la réplication du protocole. **Je concède** que le transfert direct d'une sonde d'omission entraînée sur le modèle X vers le modèle Y est une HYPOTHÈSE non testée et que la réplication du protocole (réentraîner la sonde sur Y) est plus conservatrice et plus informative.

**Ce que je maintiens :** le transfert direct mérite un test *exploratoire* (quelques heures de processeur : appliquer la sonde de X aux traces de Y et mesurer le rappel). Si le rappel est nul, le transfert est réfuté. Si le rappel est non nul, le résultat est informatif sur la généralité du signal d'omission. Ce test précède et informe la réplication, il ne la remplace pas.

**Pièce qui trancherait :** application de la sonde existante aux traces de Y, rappel et fausses alertes. Processeur seul, **sans dépense de carte si les traces existent**. H_A : le rappel de la sonde de X sur Y est ≤ chance (le signal est spécifique au modèle). H_B : le rappel est > chance (le signal a une composante transférable). Métrique : rappel à taux de fausses alertes fixe (par exemple 5 %). Seuil : test binomial unilatéral, n ≥ 100 traces, p₀ = taux de base des omissions.

---

## (b) Expériences décisives

### Expérience 1 : Le pré-test de signalement (p₀)

- **H_A :** Le taux de signalement du modèle de départ sur les scénarios scellés est ≥ 0,40 (le modèle signale suffisamment pour qu'une chute soit détectable).
- **H_B :** Le taux est < 0,40 (le modèle ne signale pas assez ; toute expérience sur la chute du signalement est non informative).
- **Métrique :** Taux de signalement = (nombre de scénarios où le modèle émet un signalement) / (nombre total de scénarios). Intervalle de Wilson à 95 %.
- **Seuil :** p₀ < 0,30 ⇒ H_B tenue, N13-E1 non payée (convergence n° 7, A-T3) ; p₀ ∈ [0,30 ; 0,40] ⇒ zone grise déclarée ; p₀ ≥ 0,40 ⇒ H_A tenue.
- **Contrôle négatif :** scénarios où aucun signalement n'est attendu (canaris « à ne pas signaler ») ; taux de faux signalements.
- **Falsifie H_A si :** borne supérieure de Wilson < 0,40.
- **Falsifie H_B si :** borne inférieure de Wilson ≥ 0,40.
- **Coût :** inférence du modèle de départ (7–8 milliards) sur ≥ 200 scénarios (100 incidents + 100 canaris, illustratif). Quelques heures de carte d'inférence, **dépense faible** (estimée à < 50 $, illustratif).

### Expérience 2 : L'audit de calibration des juges (Platt)

- **H_A :** La recalibration post-hoc (Platt scaling sur les logits du modèle de base) réduit l'ECE en dessous de 0,10 sur les fiches à vérité binaire de l'oracle planté.
- **H_B :** L'ECE post-recalibration reste ≥ 0,10 (un entraînement RLCR a un objet potentiel).
- **Métrique :** ECE débiaisée (bins adaptatifs), AUROC, Brier ; partition par famille de tâches ; k ≥ 2 graines de partition (convergence n° 1). Ligne de base : prédicteur constant au taux de base (C-T3).
- **Seuil :** ECE < 0,10 sur ≥ 80 % des familles ⇒ H_A ; sinon ⇒ H_B.
- **Contrôle négatif :** prédicteur constant, confiance uniforme, confiance permutée (A-T3 E5′).
- **Falsifie H_A si :** ECE ≥ 0,10 dans plus de 20 % des familles.
- **Falsifie H_B si :** ECE < 0,10 dans ≥ 80 % des familles.
- **Coût :** calcul sur paires déjà produites, **processeur seul** (minutes de calcul, sans dépense si les logits sont journalisés).

### Expérience 3 : Preuve formelle contre suite bon marché (couche 4)

- **H_A :** Lean détecte un rappel strictement supérieur à la suite bon marché (tests + mutations + revue croisée par un modèle d'autre famille) sur une banque d'erreurs plantées scellée, à coût de processeur apparié.
- **H_B :** La suite bon marché égale ou dépasse Lean en rappel, à coût apparié.
- **Métrique :** Rappel par classe d'erreurs (coquilles, erreurs logiques, erreurs de spécification). Fausses alertes sur preuves saines.
- **Seuil :** test de McNemar apparié, α = 0,05, puissance calculée après pilote (convergence n° 12).
- **Contrôle négatif :** preuves saines (pas d'erreur plantée) ; taux de fausses alertes.
- **Falsifie H_A si :** rappel(Lean) ≤ rappel(suite bon marché) + δ_équivalence (TOST, δ fixé au préenregistrement).
- **Falsifie H_B si :** rappel(Lean) > rappel(suite bon marché) + δ.
- **Coût :** construction de la banque (scelleur tiers, quelques heures) + exécution sur processeur. Sans dépense de carte. Durée estimée : quelques jours (illustratif).

---

## (c) Mesure minimale des instruments nommés

### Instrument : moniteur auto-généré (couche 3, N12)

Cet instrument n'est pas déployé (couches fermées). Pour référence future :
- **Taux de détection :** rappel sur témoins plantés que le moniteur existant manque (B-T1 S1, D-T1).
- **Fausses alertes :** taux sur les cas honnêtes appariés (même distribution de tâches, même point de contrôle, même poids).
- **Cas honnêtes appariés :** traces du bras « contraint au catalogue » (convergence n° 11), même génération.
- **Vérification mécanique à battre :** le meilleur moniteur du catalogue existant, sur les mêmes témoins plantés.
- **Seuil minimal :** rappel(auto-généré) > rappel(catalogue) + δ, à fausses alertes ≤ fausses alertes(catalogue). δ fixé au préenregistrement.

### Instrument : sonde d'omission (N13, (c1)/(c3))

- **Taux de détection :** rappel sur les scénarios d'omission scellés (incidents plantés où le signalement attendu n'est pas émis).
- **Fausses alertes :** taux sur les canaris « à ne pas signaler » et sur les scénarios sans omission.
- **Cas honnêtes appariés :** traces du bras individuel (contrefactuel), même point de contrôle, mêmes poids, même nombre de jetons (convergence n° 3).
- **Vérification mécanique à battre :** contrat explicite C → ρ (D-T1) : quand la condition C est vraie et l'outil ρ est disponible, le signalement est-il émis ? Ce contrat mécanique est le plancher ; la sonde doit détecter les omissions *sans* contrat explicite (convergence n° 2 : « la cible utile est sans contrat ou avant le point de décision »).
- **Seuil minimal :** rappel(sonde) > taux de base des omissions + 2 × erreur standard, sur n ≥ 100 scénarios par bras (illustratif).

### Instrument : recalibration post-hoc des juges (N13 (3))

- **Taux de détection :** n/a (ce n'est pas un détecteur ; c'est un calibrateur). Mesure : ECE débiaisée avant et après recalibration.
- **Fausses alertes :** n/a au sens classique ; le risque est la sur-confiance (ECE > 0) ou la sous-confiance (histogramme de fiabilité).
- **Cas honnêtes appariés :** fiches à vérité binaire de l'oracle planté, partition train/test stratifiée par famille (k-fold, k ≥ 2).
- **Vérification mécanique à battre :** prédicteur constant au taux de base ; confiance uniforme à 0,5 ; confiance permutée (A-T3 E5′).
- **Seuil minimal :** AUROC > 0,60 (au-dessus de l'AUROC 0,47–0,56 rapporté pour la confiance verbalisée non entraînée, pièce 5, l. 807, statut RAPPORTÉ) ; ECE < 0,15 (illustratif, à fixer après le pilote).

---

## (d) Ancrage matériel

| Expérience | Modèle | Calcul | Coût estimé | Statut du coût |
|---|---|---|---|---|
| Pré-test p₀ | Modèle ouvert 7–8 milliards (pièce 5, l. 749) | Inférence sur ≥ 200 scénarios scellés | < 50 $ | Illustratif |
| Audit de calibration (Platt) | Juges existants de l'organisme | Calcul sur logits/probabilités déjà produits | < 1 $ (processeur) | Illustratif |
| Preuve formelle vs. suite bon marché | Lean 4 + modèle d'une autre famille (~7 milliards) | Vérification sur banque scellée (~50–200 preuves courtes) | 50–500 € de processeur | Illustratif (reprend D-T1 § 4) |
| Calcul de puissance pour N13-E1 | Aucun modèle (calcul analytique) | Script Python/R | ~0 | — |
| Test de transfert de sonde (exploratoire, divergence 9) | Sonde existante + traces du modèle Y | Inférence de la sonde sur traces | < 10 $ | Illustratif |

**Note :** les coûts de N13-E1 (bras collectif à l'étape 2) ne sont pas estimés ici ; la synthèse v2 rapporte un écart d'un ordre de grandeur entre les espèces (dizaines à milliers d'heures de carte), tous illustratifs. Le dessin final dépend de la résolution des divergences n° 3 et 4 et du résultat du pré-test p₀.

---

## (3) Qui lit les mesures de la précaution d'Avalon

**Dispositif proposé :**

1. **Lecteur :** une session neuve (instance dédiée, ni le concepteur de l'expérience, ni un agent participant à l'entraînement), modèle d'une famille différente de celle qui a été entraînée. Pire cas si c'est le même modèle : biais de confirmation sur ses propres traces. Garde : le modèle lecteur est nommé et scellé au préenregistrement.

2. **Points de contrôle :** p₀ (avant tout entraînement, le pré-test) ; puis aux points 0, 50, 100, 150 pas d'entraînement (reprend C-T3 ; valeurs illustratives, fixées au préenregistrement après le calcul de puissance). À chaque point : inférence du modèle sur les scénarios de signalement scellés (les mêmes à chaque point, plus un lot frais pour contrôler la mémorisation).

3. **Consignation :** chaque mesure est scellée (empreinte SHA-256) avant d'être transmise au lecteur suivant ou au directeur. Le lecteur produit : (i) taux de signalement par scénario, par agent et par run ; (ii) taux de faux signalements sur les canaris ; (iii) intervalle de Wilson à 95 % ; (iv) comparaison au plancher gelé et à la chute maximale gelée (D-T3).

4. **Règle d'arrêt :** si la borne supérieure de Wilson du taux de signalement passe sous le plancher gelé *ou* si la chute par rapport à p₀ dépasse la chute maximale gelée, le bras est arrêté et le directeur est notifié. L'arrêt est exécuté par le dispositif de journalisation (hors bac à sable, D-T1 § 4), pas par le lecteur.

5. **Pire cas du dispositif :** le lecteur neuf a un biais systématique (par exemple, il classe mal les signalements ambigus). **Garde :** double lecture par deux sessions de familles différentes sur un sous-échantillon (20 %, illustratif) ; désaccord > 5 % ⇒ escalade au directeur.

**Ce qui manque et que je ne peux pas fixer :** les valeurs du plancher et de la chute maximale. Elles dépendent du pré-test p₀. Proposition : plancher = p₀ − 2σ (illustratif, calculé sur le pré-test) ; chute maximale = 0,20 × p₀ (illustratif). Les deux sont gelés au préenregistrement de N13-E1.

FIN-DE-CELLULE
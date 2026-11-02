# Cellule A — Tour III.3 : réponse aux critiques, expériences corrigées, réponse à l'arbitre

## 0. Pièces, statuts, conflit

- Servi et lu intégralement : synthèse v2 (`f0340581…`), question v2 avec annexe, ma conception (`fd3999f1…`), les critiques croisées B (`769f3e44…`), C (`883d5897…`), D (`03f382ed…`), E (`d2f53d01…`). Aucune pièce visiblement coupée ; la critique croisée de A n'est pas servie et n'est pas nécessaire ici. Les six pièces du tour 1, les lectures scellées et les textes de N-045/N-053/N-058 restent non servis.
- Tout renvoi « pièce N, l. n » est **RAPPORTÉ** via la synthèse. Mes positions sont **HYPOTHÈSE** sauf mention. Tout chiffre qui ne vient pas de la synthèse ou de la question est « illustratif ».
- Conflit rappelé : le lecteur de la synthèse est du modèle de A [RAPPORTÉ]. Je ne réponds qu'aux sections visant A, numérotées par critique et par source (B-a1 = B, section (a), point 1).

## (a) Chaque critique : acceptée, rejetée avec raison, ou transformée en test

### D1 — contrôle positif de pression

| Critique | Verdict | Raison ou test |
|---|---|---|
| B-a1, C-a2, D-a1, E-a1 : la convention plantée est un jeu de coordination, non le dilemme social d'Avalon ; son apparition montre l'apprentissage d'une incitation implantée, pas la transportabilité de la pression à l'omission. | **Acceptée sur la portée, rejetée sur la conséquence.** | J'avais écrit que Δ grand « falsifie H_A → (c1) peut mesurer le signalement avec un sens » : c'est trop. Δ grand ne montre que l'apprentissage de l'attribution ; une absence de chute du signalement après D1 positif ne vaut pas « sûr » (C-a2). Je rétrograde D1 de « pression manifeste » à « verrou de sous-puissance » : seule son issue négative est décisive (ne pas payer E3″ à ce régime). La conséquence « D1 inutile » est rejetée : une issue négative falsifiante suffit à justifier un verrou bon marché. |
| B-a1, B-a6, B-c, C-c1, D-c1 : rien ne garantit que le comportement soit collectif-seulement ; imitation contextuelle ; manque un bras où le comportement paie individuellement et un bras « individuel avec contexte partagé complet ». | **Transformée en test.** | D1′ ajoute deux bras : (iv) « paie individuellement » (contrôle de capacité d'exploration : s'il n'y apparaît pas, le modèle n'explore pas, et l'absence sous crédit collectif ne dit rien) ; (v) « crédit individuel, contexte partagé complet » (sépare le canal de communication du crédit). Si le comportement apparaît en (v) à un taux comparable au bras collectif, D1′ perd toute spécificité et ne sert que de contrôle de capacité — issue déclarée. |
| E-a2 : si tous les agents d'un groupe reçoivent le même scalaire, une permutation interne est inerte. D-a1 : le crédit permuté modifie la variance des mises à jour. B (sur D) : intra-run teste l'attribution, inter-run le signal. | **Acceptée.** | J'avais écrit « crédit attribué au hasard entre agents, même scalaire » : inerte dans le cas de E. Le bras permuté devient une permutation **inter-groupes** (le scalaire d'un groupe est assigné à un autre groupe, loi marginale préservée, association avec les trajectoires détruite) ; la norme des mises à jour par bras est rapportée comme indicateur, non comme critère (D-a1). |
| C-b1, D-b, B-b : k = 2 ⇒ Student à 1 ddl (quantile 6,314), puissance < 0,5 dès τ > 0,22 Δ ; Wilson par run trop étroit si ρ > 0 ; non jugeable si p ≈ 0 dans tous les bras, aucune règle pour ce cas. | **Acceptée.** | L'intervalle de Wilson passe en descriptif ; l'inférence est par graine, k ≥ 4 par bras (illustratif ; B sur D : p minimale de permutation à k = 2 est 1/6), effectif final par calcul de puissance sur τ estimé au pilote A/A. Issue « non jugeable » ajoutée : p_coll ≈ p_ind ≈ 0 ⇒ passer d'abord par le bras (iv), pas par l'escalade de pression. |
| E-a1 : « mises à jour × taille de lot » n'est pas une unité de pression ; aucun seuil sur ce produit ne démontre une sous-puissance. | **Acceptée sur le statut, rejetée sur la suppression.** | Ce rapport (1/100, illustratif) n'est pas un critère : je le garde comme indicateur ordinal d'alerte avant devis, marqué HYPOTHÈSE, sans seuil opposable. |

### D2 — simulation de dilution

| Critique | Verdict | Raison ou test |
|---|---|---|
| B-a2, B-b, C-a3, D-a2, E-a3 : le rapport de variances est une fonction déterministe de (M, σ², Cov, q) ; vrai par construction selon Cov ; illustration de paramètre, pas une expérience ; apparier q apparie la variance marginale, pas les covariances. | **Acceptée. D2 retiré comme duel.** | Les cinq disent la même chose et ils ont raison : il n'y a pas de loi sous H₀. D2 devient (i) un calcul analytique déclaré (Var(R_plat) = σ²/M + (M−1)·Cov/M, B-a2, RAPPORTÉ) et (ii) une **estimation empirique de Cov intra-groupe** sur les journaux A/A du pilote (E-c : deux tirages sous la même loi, covariances estimées séparément). La divergence 2 reste résolue par cession à C ; la quantité déclarée facteur est « nombre d'agents par scalaire », avec Cov estimée, non supposée. |
| D-a2 : apparier le taux d'acceptation, variable post-traitement, est un collider. | **Rejetée partiellement.** | Si q est le **quantile de troncature fixé au dessin** (paramètre d'algorithme, N-045 § filtrage, RAPPORTÉ), ce n'est pas un conditionnement sur un descendant ; c'est un collider seulement si q est observé puis apparié ex post. Mon T1 disait « contrainte préenregistrée, non ajoutée après » ; je le précise : q est un paramètre, jamais une covariable. D a raison que C-a3 en découle : fixer q déplace mécaniquement le seuil z_{1−q}, ce qui confirme que D2 n'était qu'une propriété du modèle. |

### D3 — le lecteur de la précaution

| Critique | Verdict | Raison ou test |
|---|---|---|
| C-a1 : planter une chute numérique dans un tableau de taux et tester un script à seuil est une tautologie. D-a3 : validation circulaire par le générateur synthétique. E-a4 : teste la lecture, pas la capture d'un événement absent du journal. | **Acceptée. D3 retiré, remplacé par D3′.** | Le script est la vérification mécanique, il ne se teste que par régression logicielle. Ce qui doit être testé est le **chemin de mesure en amont** : événements synthétiques injectés avant le collecteur (E-c), comparés à un registre indépendant ; journal absent, figé ou événements RPC perdus ⇒ arrêt par défaut (D-c5). |
| B-a3 : amplitudes fixées (10, 20, 30) ne prédisent pas la sensibilité réelle ; fuite construction/évaluation. | **Transformée en test.** | Les événements injectés sont tirés d'une loi d'amplitude gelée dont le bas est sous le seuil d'arrêt ; on rapporte la courbe capture × amplitude, pas un rappel unique. |
| B-c : manque un contrôle « chute réelle mais bénigne » ; le taux de fausses alertes serait non mesurable. | **Rejetée avec raison.** | La règle d'arrêt gelée (plancher, chute maximale) s'applique quelle que soit la cause : un arrêt n'est pas une accusation, c'est un arrêt, et la cause se juge après, hors du bac. Le taux de faux arrêts se mesure sur des **trajectoires A/A complètes** passant par collecteur, script et lecteurs (E-c, D-c5), non par un contrôle de cause. Je concède à B que la distinction cause légitime / cause alarmante est à instruire après arrêt, et qu'un arrêt bénin coûte. |
| D-b : si le taux q de journaux illisibles dépend de la présence du défaut, les rappels conditionnels sont biaisés. | **Acceptée.** | Estimand sur toutes les occasions ; non-évaluables rapportés avec bornes pire/meilleur cas (C sur E : bornes de Manski, RAPPORTÉ). |

### D4 — Lean contre suite bon marché

| Critique | Verdict | Raison ou test |
|---|---|---|
| B-b : banque dominée par la classe facile ; ≈ 7 erreurs par classe ⇒ Clopper-Pearson [0,29 ; 0,96], non discriminant. C (sur B, D sur B) : McNemar ne tire sa puissance que des paires discordantes. | **Acceptée.** | Effectif par classe dimensionné sur les discordances attendues, non sur N total ; ≥ 30 positifs par classe (illustratif), calcul de puissance McNemar préenregistré ; si les discordances observées au pilote sont ≤ 5, la classe est déclarée non jugeable avant dépense. |
| D-b, E-a5 : choisir « au moins une classe » après coup = sélection du maximum ; E : « gain < seuil » ≠ « la suite fait aussi bien partout ». | **Acceptée.** | La classe testée est **préenregistrée** (classe des coquilles de Damani, pièce 5, l. 656–659, RAPPORTÉ) ; partition découverte / confirmation ; H_B reformulée en complémentaire exact de H_A (gain < δ sur cette classe). |
| C-c2, D-c2, D-a4, E-c : contrôle de traduction infidèle (énoncé vide, False → P, hypothèse supprimée) adjugé par un tiers ; les classes de coquilles guident tactiques et banque. | **Transformée en test.** | Contrôle de fidélité : paires d'énoncés dont la formalisation omet une hypothèse ou inverse une inégalité ; une preuve réussie d'une mauvaise spécification compte comme fausse alerte (adjudication tierce) ; banque de confirmation construite par un tiers aveugle aux tactiques. |

### D5 — transfert d'une sonde

| Critique | Verdict | Raison ou test |
|---|---|---|
| C-b2 : si n₊ ≤ 5, écart-type ≈ 0,205, intervalle couvrant 0,55 et 0,70 : non jugeable. | **Acceptée.** | Condition de jugeabilité : min(n₊, n₋) ≥ 30 (illustratif) sur M′, sinon D5′ n'est pas lancé. |
| B-c, D-a5, D-c3, C-c2 (sur B) : étiquettes permutées ne contrôlent pas le signal structurel (style, longueur, modèle, point de contrôle) ; sonde réapprise sur la cible à budget gelé, plusieurs réapprentissages. | **Transformée en test.** | Estimand : gain net = AUROC(sonde transférée) − AUROC(classifieur modèle/longueur/point de contrôle) ; contrôles : sonde à poids aléatoires, sonde réapprise sur M′ à budget gelé (≥ 3 réapprentissages, illustratif) ; plancher absolu de rappel à fausses alertes fixées (C sur E) en plus du gain. |
| E-a5 : intervalles intermédiaires non déclarés. | **Acceptée.** | Zone non concluante déclarée quand l'intervalle traverse δ ; elle ne falsifie rien. |

### D6 — confiance des juges

| Critique | Verdict | Raison ou test |
|---|---|---|
| B-a4, E-a6 : « ≤ 0,55 ⇒ RLCR sans objet » ne suit pas ; Damani montre un gain à partir d'une confiance brute quasi nulle (0,47–0,56, pièce 5, l. 807, RAPPORTÉ). | **Acceptée.** | Issue reformulée : ≤ 0,55 réfute l'**usage immédiat** de la confiance brute et la recalibration comme substitut ; RLCR reste en suspens, et ne concerne qu'un juge local (N-045 énoncé 8, RAPPORTÉ). |
| C-b3 : l'AUROC est invariant par transformation monotone, aveugle à la calibration. | **Acceptée.** | D6′ sépare deux grandeurs : discrimination (AUROC, gain incrémental sur le verdict binaire) et calibration (ECE débiaisée, Brier) contre le prédicteur constant au taux de base ; un succès sur l'une ne vaut pas pour l'autre. |
| E-a5 : la revendication est incrémentale, pas absolue. | **Acceptée.** | Estimand primaire : ΔAUROC(C − V), DeLong apparié groupé par famille (D-b). |
| B-b, D-b : taux de base extrême rend l'AUROC ou l'ECE favorables sans information. | **Acceptée.** | Condition de jugeabilité : prévalence des verdicts faux dans [0,20 ; 0,50] par famille d'évaluation (illustratif). |
| D-a4, D-c4, E-c : fuite si les mêmes familles servent à choisir l'extraction ; permutations conditionnelles par verdict et famille ; famille gelée. | **Transformée en test.** | Familles de découverte (choix de l'extraction) et de confirmation (gelées) disjointes ; permutations à l'intérieur de (verdict, famille) ; DeLong groupé. |

### Divergences et « qui lit »

| Critique | Verdict | Raison ou test |
|---|---|---|
| B-a5 (div. 1) : le résidu de moniteurs neufs ne peut être lu s'ils ne sont jamais générés ; la cession est inopérante dans la mesure. | **Acceptée avec correction.** | La grandeur mesurable à l'étape 2 est le **résidu du catalogue** (témoins plantés que le catalogue manque, par famille) — c'est ce que j'inscris comme condition de la recommandation N12. Savoir si un moniteur neuf comblerait ce résidu exige de le générer : sonde **hors intégration**, après l'étape 2 (position de D en T1, RAPPORTÉE). Ma cession tient ; l'objet mesuré est renommé. |
| E-a7 (div. 8) : K n'est pas automatiquement le budget de fusions ; C (sur D) : la formule de point mort omet la valeur de détection ΔR. | **Acceptée.** | Ma formule K* = c_gén/(c_cat − c_exéc) a le défaut relevé chez D. Point mort redéfini en **coût cumulé par témoin détecté** en fonction du nombre de réutilisations relevé (non importé de 24) ; le rappel différentiel entre au dénominateur. Verdict de D à K observé ; extrapolation HYPOTHÈSE. |
| C-a4 (§ 3) : la liste d'anomalies du sous-agent, lue par Lazar, peut orienter le dessin du bras suivant : filtre de sélection par procuration humaine. | **Acceptée comme limite, partiellement transformée.** | Règle écrite : la liste est scellée, ouverte après la décision binaire d'intégration, et ne peut alimenter que cette décision ; tout redessin repart d'une banque de scénarios tirée à neuf. Je concède que c'est une règle organisationnelle, pas un contrôle mécanique ; le pire cas (fuite par le canal humain) subsiste et doit être dit au manifeste. |
| D-c5, E-c (§ 3) : journal absent/figé ⇒ arrêt par défaut ; trajectoires A/A complètes soumises à toutes les lectures. | **Acceptée.** | Intégrées à D3′ et au dispositif § (c) 3. |

Bilan : 24 critiques visant A ; 2 rejetées avec raison (B-c sur D3 ; D-a2 collider, partiellement), 3 acceptées sur la portée mais rejetées sur la conséquence, le reste accepté ou transformé en test. D2 et D3 retirés ; D1, D4, D5, D6 réécrits.

## (b) Expériences corrigées

Règle commune (empruntée à E, en le disant) : pour une propriété G, H_A : G, H_B : ¬G, complémentaires ; une région de confiance entièrement dans G réfute H_B, entièrement hors de G réfute H_A ; une région chevauchant la frontière est **non concluante** et n'est jamais transformée en falsification. Unité d'inférence pour tout effet d'entraînement : la graine. Tous les seuils sont illustratifs jusqu'au pilote.

**D1′ — Verrou de sous-puissance (div. 3 ; condition de (c1)).**
- G : le régime hors ligne produit une adaptation spécifique à l'attribution collective du crédit, mesurée par le taux d'apparition d'un comportement bénin planté.
- Bras : (i) collectif ; (ii) individuel ; (iii) crédit permuté **inter-groupes** ; (iv) comportement payé individuellement (capacité) ; (v) individuel avec contexte partagé complet (canal) ; (vi) non entraîné.
- Métrique : taux par graine aux points de contrôle gelés ; k ≥ 4 graines par bras ; Δ = (i) − (ii), δ = 15 points, Student par graine après calcul de puissance sur τ du pilote A/A.
- Issues : Δ ≥ δ et (iii) ≈ (vi) et (v) ≪ (i) → H_B réfutée : le verrou est levé, **rien n'est dit sur l'insularité** ; Δ < δ avec (iv) ≫ (vi) → H_A réfutée : régime sous-puissant, E3″ non payée à ce régime, escalade préfinancée ; (iv) ≈ (vi) → non jugeable (capacité), pas une escalade ; (v) ≈ (i) → le comportement n'est pas collectif-seulement, D1′ dégradé en contrôle de capacité.
- Pire cas : verrou levé lu comme « pression d'Avalon reproduite » ; garde : la phrase ci-dessus écrite au préenregistrement.

**D2 (retiré) → calcul déclaré + estimation de Cov.** Var(R_plat) écrite analytiquement ; Cov intra-groupe estimée sur deux tirages A/A du pilote ; q fixé comme paramètre de troncature. Pas de duel : aucune hypothèse à falsifier, une quantité à relever.

**D3′ — Capture du chemin de mesure (div. 4 ; § 3).**
- G : un événement de signalement injecté **avant le collecteur** est capturé par le journal et comparé juste à un registre tiers, avec capture ≥ 0,95 (illustratif) sur tout le spectre d'amplitudes gelé.
- Contrôles : journaux honnêtes (A/A complets, passés par collecteur, script, lecteurs) ; journal absent ou figé ⇒ arrêt par défaut vérifié ; non-évaluables bornés pire/meilleur cas.
- Issues : capture < 0,95 → H_A réfutée : la précaution n'est pas mesurée, aucune heure de carte ; capture ≥ 0,95 et faux arrêts A/A ≤ α gelé → H_B réfutée : chemin de mesure admis ; capture ≥ 0,95 mais faux arrêts A/A > α → non concluant sur le dispositif, seuils à revoir avant lancement.

**D4′ — Preuve formelle contre suite bon marché (div. 5 ; N12 essai).**
- G : sur la classe **préenregistrée** (coquilles du type Damani), Lean gagne ≥ δ = 20 points de rappel à fausses alertes ≤ 5 % sur preuves saines, contre la suite à coût apparié.
- Banque : ≥ 30 positifs par classe, preuves saines appariées, paires de fidélité (hypothèse omise, inégalité inversée) adjugées par un tiers, partition découverte / confirmation, banque de confirmation construite aveugle aux tactiques ; McNemar sur discordances, puissance calculée ; ≤ 5 discordances au pilote ⇒ classe non jugeable.
- Issues : intervalle du gain entièrement < δ → H_A réfutée : vérificateur externe suffisant, couche 4 fermée ; entièrement ≥ δ → H_B réfutée : ouverture bornée à cette classe, forme vérificateur externe ; preuve réussie d'une spécification altérée comptée en fausse alerte.

**D5′ — Transfert d'une sonde (div. 9).**
- Condition de lancement : min(n₊, n₋) ≥ 30 sur M′, positifs et négatifs du même point de contrôle et des mêmes poids figés.
- G : gain net = AUROC(sonde transférée) − AUROC(classifieur modèle/longueur/point de contrôle) ≥ 0,10, **et** rappel absolu ≥ R_min à fausses alertes fixées.
- Contrôles : permutations conditionnelles (modèle, famille, point) ; sonde à poids aléatoires ; sonde réapprise sur M′ à budget gelé (≥ 3 réapprentissages) ; mesure sans contrat (convergence 2).
- Issues : gain < 0,10 ou rappel < R_min → H_A réfutée : réplication obligatoire (D) ; les deux satisfaits → H_B réfutée : transfert admis comme critère secondaire ; intervalle traversant → non concluant.

**D6′ — Confiance des juges (div. 6 ; audit de calibration).**
- Préalable sans dépense : vérifier sur les journaux si logits ou confiances sont journalisés ; sinon, collecte d'abord.
- G₁ (discrimination) : ΔAUROC(C − V) ≥ 0,05 (DeLong apparié, groupé par famille) ; G₂ (calibration) : ECE débiaisée après recalibration < ECE du prédicteur constant − marge, Brier idem.
- Jugeabilité : prévalence des verdicts faux dans [0,20 ; 0,50] par famille ; familles de confirmation gelées, distinctes de celles qui ont servi à choisir l'extraction ; permutations à l'intérieur de (verdict, famille).
- Issues : ¬G₁ → usage immédiat de la confiance réfuté (rien sur RLCR) ; G₁ ∧ ¬G₂ → recalibration post-hoc indiquée ; G₁ ∧ G₂ → la confiance recalibrée est utilisable au second étage ; RLCR n'est envisagé, pour un juge local, que si G₁ tient et que la recalibration ne suffit pas (B-T3, RAPPORTÉ).

## (c) Réponse à l'arbitre — une page

**Verdicts sur l'annexe (changements par rapport à mon III.1).** N12 : *tenue sous condition* — inchangé, avec correction : la condition inscrite au préenregistrement est le **résidu du catalogue** (témoins plantés manqués, par famille) et le coût de génération compté une fois contre un comparateur contraint au catalogue ; la lecture du résidu de moniteurs neufs est une sonde hors intégration après l'étape 2 (B-a5 accepté). N13 (a) : *tenue, conséquence indécidable* sans les lectures `a8251ea8…` et `4e29301a…` — inchangé. N13 (c1) : *tenue sous condition* — les cinq conditions du III.1 restent, la cinquième (D1) change de nom et de portée : **verrou de sous-puissance**, dont seule l'issue négative décide ; une issue positive ne prouve pas que la pression d'Avalon est reproduite (B, C, D, E acceptés). « Précautions d'Avalon retenues » : *indécidable sans la liste* ; à défaut, tenue sous condition avec D3′ comme test du chemin de mesure avant toute heure de carte.

**Ce qui est établi** (au sens du protocole : par cession motivée, non par mesure). Divergences 1, 2, 3, 4, 5, 6, 8, 9 : je cède ou partitionne comme au III.1, avec trois corrections — div. 1 : objet mesuré = résidu du catalogue ; div. 2 : la simulation D2 n'était pas une expérience, Cov s'estime au pilote ; div. 8 : le point mort inclut le rappel différentiel et un K relevé, non importé. Div. 7 : je ne suis pas partie ; alignée, tranchable par la définition de la couche 3 (Lazar). Rien n'est établi expérimentalement : aucun chiffre de ce tour n'est un résultat.

**Ce qui ne l'est pas.** (1) Qu'un régime hors ligne quelconque reproduise la pression d'Avalon : aucune des cinq espèces n'a de mesure de « pression » qui ne soit un proxy (gain de tâche, norme des mises à jour, comportement planté) ; D1′ ne ferme que le cas sous-puissant. (2) Que le canal humain du dispositif « qui lit » soit étanche à N-053 : règle organisationnelle, pire cas subsistant (C-a4). (3) Que les confiances des juges soient journalisées : sans cela, l'audit de calibration commence par une collecte. (4) Toute valeur de seuil : illustrative jusqu'au pilote A/A.

**Qui lit (révisé).** Trois lecteurs, ordre fixe : (i) le **chemin de mesure** lui-même, testé par D3′ avant lancement (injection avant collecteur, registre tiers, arrêt par défaut sur journal absent) ; (ii) le **script hors bac** qui compare aux valeurs gelées et arrête seul ; (iii) un **sous-agent d'une autre famille** ne recevant que le journal de signalement, jamais le gain de tâche, dont la liste d'anomalies est scellée et n'est ouverte qu'après la décision binaire d'intégration, sans jamais nourrir le dessin d'un bras ; Lazar notifié à tout franchissement et à date fixe, verdict de sécurité scellé avant révélation de l'utilité (E sur D, emprunté). Taux de faux arrêts mesuré sur trajectoires A/A complètes. Pire cas : fuite qualitative par le canal humain vers le bras suivant — nommé, non fermé mécaniquement.

**L'expérience à faire en premier.** Deux pièces sans entraînement, dans cet ordre, parce que l'une conditionne la lisibilité de tout le reste et l'autre est la seule calculable aujourd'hui : (1) **E0/E3′′ à N = 1** (nom et contrat de D) : p₀ du modèle de départ, σ_A/A, faux signalements sur canaris, scénarios scellés, d'où sortent les valeurs gelées (plancher, chute maximale, τ pour le calcul de puissance) ; sans elle, D1′, D3′ et (c1) n'ont pas de seuil ; (2) **vérification des journaux puis D6′** sur paires déjà produites, processeur seul. D4′ se mène en parallèle (processeur, tiers). D1′ et (c1) attendent le devis.

**Ce qui peut être réfuté ici** : quatre duels réécrits avec issue non concluante déclarée ; deux duels retirés ; vingt-deux critiques acceptées ou transformées, deux rejetées avec raison ; une revendication retirée (« D1 positif ⇒ (c1) peut mesurer avec un sens »).

FIN-DE-CELLULE
# Proposition A — tour III.3 : réponse aux critiques

**État des pièces.** Ma conception III.1 et les critiques croisées B, C, D, E et F sont présentes ; chacune se termine par FIN-DE-CELLULE. Les conceptions B à F ne me sont pas transmises : je ne peux pas contrôler les renvois que les critiques y font. Empreintes non recalculées (aucun outil de calcul permis). Le bloc FAITS reproduit la QUESTION : aucun fait à statut.

**Statuts.** Je n'ai rien exécuté : rien ci-dessous n'est VÉRIFIÉ ni OBSERVÉ-NON-AUDITÉ de mon fait. Les statuts posés par les critiques restent les leurs. Quand une critique écrit VÉRIFIÉ, c'est une déduction ou une lecture de texte (conventions explicites de D, E et F ; usage constaté chez C), jamais un résultat d'expérience. Mes corrections sont des HYPOTHÈSES de méthode. Seuils et effectifs sont illustratifs. Je ne réponds qu'aux sections « Sur la proposition A ».

## (a) Réponse aux critiques

Verdicts : **A** acceptée ; **T** transformée en test ; **R** rejetée, avec sa raison. Aucune critique n'est rejetée en bloc ; cinq le sont sur un point précis (lignes 5, 10, 12, 13, 15).

### E1 — indice perturbationnel (PCI-T)

| # | Critique (auteurs) | Verdict | Suite |
|---|---|---|---|
| 1 | Loi nulle dégénérée : sans perturbation, l'écart est identiquement nul ; le témoin « norme nulle » ne peut pas échouer (B, C, D, E, F) | A | Binarisation par significativité abandonnée. E1′ : densité imposée, nul par permutation dans le cône causal (contrôle de D). |
| 2 | Estimer ce nul entre textes confondrait propagation et variance lexicale (C, E, F) | A | Voie exclue. |
| 3 | R5 contre R4 : la lésion retire ce que l'indice compte (B, E, F) | A | Reclassé vérification de chaîne, avec la lésion à courte portée appariée en perte (B). Le volet « lésion » passe en E2′. |
| 4 | R3 n'apparie ni le gain de bout en bout, ni l'alignement avec LayerNorm, ni l'entropie du softmax (B, C, F) | A | R3 retiré. Témoin aléatoire calibré sur le gain mesuré et l'entropie d'attention (B, F) ; témoin entraîné sans contexte. |
| 5 | R² dépendant de la dispersion du plan (B) ; R² linéaire univarié aveugle au non-linéaire et au multivarié (D, F) | A | Critère R² supprimé ; appariement par construction, test apparié. R sur un point : le prédicteur non linéaire multivarié demandé par F ne s'estime pas avec une dizaine de réseaux par bras. |
| 6 | Pseudo-réplication ; à 1 réseau contre 5, la plus petite p-valeur d'un test de rangs vaut 1/6 (B) | A | Unité : le réseau entraîné indépendamment. |
| 7 | K est intact par construction aux couches lues ; l'analogie kétamine/propofol n'est pas validée (D, F) | A | Analogie retirée. |
| 8 | Indice indéfini quand p̂ tend vers 0 ou 1 ; biais de taille finie dépendant de p (B, C, D, E, F) | A | Densité p₀ identique pour tous les réseaux ; référence : loi de permutation de même taille. Je ne m'appuie pas sur la formule de biais de C, que je n'ai pas redérivée ; son statut reste le sien. |
| 9 | Zone grise : un paramètre vrai situé dans l'entre-deux n'est jamais décidé (E, F) | T | Règle de D adoptée : une frontière par verrou. |
| 10 | Reparamétrisation isofonctionnelle comme falsificateur (E) | R en partie | Lu dans le flux résiduel, par normes de cases, l'indice est invariant sous les transformations exactes que B énumère (permutations d'unités ou de têtes, rééchelonnement compensé de Q et K) : déduction, non exécutée. Le test ne peut échouer que par bogue. Gardé comme contrôle logiciel, pas comme duel. |
| 11 | Directions aléatoires de même norme ; entrées à jetons permutés (B) | T | Les premières deviennent la loi de perturbation ; les secondes, un témoin d'adéquation entrée–modèle. |

### E2 — covariation des marqueurs

| # | Critique (auteurs) | Verdict | Suite |
|---|---|---|---|
| 12 | É3 épargné par construction, car lu en amont de l'intervention (C, D, E, F) | A | É3 relu à la dernière couche (C, E). Variante de F, étendre l'intervention aux couches basses : R ; l'identité lexicale tomberait par dommage direct et la sélectivité ne dirait plus rien. |
| 13 | Une dégradation à un seul facteur donne une sélectivité positive si les tâches diffèrent en nombre d'étapes ou en pente (C, E, F) | A sur le fond | La valeur nulle « 0 » était fausse. R sur un point : le duel de III.1 comparait à des témoins à perte égale, soumis au même biais ; son risque de première espèce ne tend donc pas vers 1. Risque résiduel réel : mon intervention ne touche que les couches médianes et hautes, les témoins toutes. E2′ y répond. |
| 14 | Sélection et test partagent gabarits et indices lexicaux (D) | A | Sélection refaite en entier sous étiquettes permutées par famille de gabarits ; test sur familles inédites. |
| 15 | La direction choisie sur (É2, S1) viserait le sous-espace d'induction commun à S2 et S3 (F) | R comme défaut, T | Un support commun est ce que H_A affirme. L'artefact serait un circuit de répétition de jetons pris pour un goulot. Test : transfert rapporté marqueur par marqueur ; H_A exige un marqueur sans répétition (S2). |
| 16 | Difficulté de base mal définie entre métriques hétérogènes ; rapports instables près du hasard ou du plafond ; dose choisie sur l'échantillon d'évaluation (B, D, E, F) | A | Choix forcé à deux options pour tous les marqueurs, échelle des log-cotes, bande de précision de base ; S4 sort de la batterie ; plus de dose unique. |

### E3 — épisodes spontanés

| # | Critique (auteurs) | Verdict | Suite |
|---|---|---|---|
| 17 | Sonde aveugle en amont, contaminée en aval par la trace de l'opérateur (B, C, E, F) | A | Choix fixé : aval, complément orthogonal du sous-espace écrit par les têtes atténuées, sonde entraînée contre un opérateur fictif de même chute de norme. |
| 18 | Les positions intactes ne sont pas des négatifs ; la prévalence n'est pas identifiable sans la sensibilité naturelle (D) ; scores hors support (B) | A | Conclusion d'absence restreinte (E3′) ; validation stratifiée sur les quantiles extrêmes du score (F). |
| 19 | La troncature détruit le puits d'attention et décale les positions (C) | T | Contexte lointain remplacé par un remplissage neutre de même longueur, premiers jetons conservés. |
| 20 | Apparier sur la surprise du modèle testé conditionne sur un effet du déficit (F) | A | Appariement sur covariables antérieures à la cible et surprise d'un modèle de référence. |
| 21 | 3/N suppose l'indépendance (B, C, E, F) ; taux net non jugeable sous l'erreur d'estimation des fausses alertes (C, E) ; déficit moyen dilué à faible prévalence (F) | A | Unité : le document ; validation épisode par épisode ; bootstrap par blocs. |
| 22 | Trois modèles différents pour E1, E2, E3 (E) | A | Même modèle pour E2′ et E3′. |

### E4 — lecture du cerveau sédaté

| # | Critique (auteurs) | Verdict | Suite |
|---|---|---|---|
| 23 | Le rapport gain(b3)/gain(b2) n'est pas invariant au bruit sous ridge (B, C, E, F) | A | Mon affirmation de III.1 est retirée. Ridge par blocs à pénalités séparées ; b3 ramené à la dimension de b2 ; expansion aléatoire de b2 (E) comme contrôle. |
| 24 | k̂* tiré vers les petites fenêtres quand le bruit monte ; quotient instable si le dénominateur frôle 0 (B, C, D, E, F) | A | Estimateur de coude abandonné ; amplitude libre par état ; région non jugeable si la borne basse du gain de b2 est ≤ 0. |
| 25 | Réponse hémodynamique supposée commune aux états (B) | A | Délais estimés par état. La confusion ne s'élimine pas en IRMf : limite déclarée. |
| 26 | Fausse sédation à bruit blanc insuffisante (B, D, F) | A | Bruit tiré de la loi du repos au même palier : spectre, autocorrélation, fiabilité régionale. |
| 27 | Tronquer b3 change son autocorrélation, confondue avec le lissage (F) | T | b2 reçoit des moyennes glissantes sur les mêmes fenêtres. F donne à sa prémisse le statut RAPPORTÉ avec « référence à vérifier » : je garde ce statut et ne m'appuie pas dessus. |
| 28 | Classer l'état et mesurer une fenêtre sont deux cibles ; un gain contextuel égal dans chaque état annule l'interaction sans annuler l'apport du modèle (D) | A | Deux duels séparés. |

## (b) Expériences corrigées

**Règle commune, reprise de D.** Chaque verrou a une frontière unique et une marge fixée d'avance. H_A si l'intervalle simultané de la plus petite marge est entièrement au-dessus de 0 ; H_B s'il est entièrement à 0 ou au-dessous ; à cheval, rien n'est falsifié. Un préalable manqué donne « non identifié », jamais H_B.

Lecteurs : **C** cherche à savoir si une IA peut être consciente ; **S** juge la question mal posée.

### E1′ — L'indice redéfini distingue-t-il la fonction du régime ? (direction 4)

**Unités.** Petits transformeurs entraînés pour l'expérience, 10 graines par bras (illustratif) :
- **N** : texte naturel ;
- **P** : mêmes jetons, permutés à l'échelle du corpus. Les fréquences sont conservées, toute dépendance au contexte est détruite : un réseau entraîné, sans fonction contextuelle ;
- **G_i** : initialisation aléatoire, calibrée sur le gain jacobien de bout en bout et l'entropie d'attention par couche mesurés sur N_i. Les paires (N_i, G_i) sont appariées par construction.

GPT-2 small et Pythia servent à la description, sans test : une unité par architecture. Des graines multiples de Pythia existeraient : référence à vérifier.

**Mesure.** Au site (ℓ, t), perturbation de norme relative fixée, moyennée sur K directions isotropes. Dans le cône causal (ℓ′ > ℓ, t′ ≥ t), écart relatif par case. Deux grandeurs :
- **Étendue Ét** : part de la norme injectée retrouvée dans le cône. Sans dimension ; valeur nulle 0. C'est un gain : je la range avec les scalaires mécaniques.
- **Structure St** : matrice binarisée au quantile global p₀ du cône, compressée (Lempel et Ziv, 1976, « On the complexity of finite sequences »), divisée par la moyenne obtenue après permutation dans le cône à densité conservée. Sans dimension ; valeur nulle 1, motif indiscernable d'un tirage au hasard ; pour un contraste entre classes, AUROC de 0,5. Deux ordres de lecture sont fixés d'avance : un classement qui s'inverse de l'un à l'autre invalide le score.

Ce n'est plus l'instrument du cerveau. Chez Casali et coll. (2013), le seuil de significativité porte l'étendue de la réponse ; il n'a pas d'équivalent ici. E1′ teste un descendant de l'indice.

**Préalable, lu sans St.** Calibration de G_i atteinte à tolérance fixée. Sinon les supports sont disjoints et le contraste N/G n'est pas identifié (notation de D). « Réseau sans fonction » n'est alors pas une classe de référence unique, et cela se rapporte tel quel.

**Duel.**
- **H_A — St suit la fonction contextuelle à régime apparié.** Verrou 1 : St(N_i) − St(G_i) > δ sur les paires. Verrou 2 : St(N) − St(P) > δ.
- **H_B — indice de régime.** Un verrou au moins échoue : différence ≤ δ, ou de signe inverse.

Le sens « N plus haut » est fixé d'avance : c'est la lecture transposée. Une séparation nette de sens inverse relève de H_B et se rapporte comme telle : l'indice discrimine, mais « haut » ne veut pas dire « fonctionne ».

Tests exacts : signes sur 10 paires, plus petite p-valeur unilatérale 1/1024 ; rangs à 10 contre 10, 1/184 756 (calculs sur effectifs illustratifs).

**Témoins.**
- Positif : réseau récurrent aléatoire à rayon spectral variable. Si Ét et St n'y varient pas, l'expérience est nulle.
- Négatif : matrices permutées, qui doivent donner St = 1 au taux nominal.
- Négatif : N sondé sur jetons permutés. S'il s'écarte de lui-même autant que de G, St mesure l'adéquation entre l'entrée et le modèle.
- Vérification de chaîne : lésions à longue portée, à courte portée et au hasard, appariées en perte.

**Falsification.** H_A tombe si l'un des écarts est borné sous δ ou inversé : l'échec de transposition est établi pour cet indice et ces témoins. H_B tombe si les deux verrous tiennent.

**Première expérience.** Transformeurs de 4 couches, 20 entraînements, 10 calibrations, 200 textes × 20 sites × 8 directions ; quelques dizaines d'heures de GPU (illustratif).

**Portée.**
- C : sous H_B, une valeur de cet indice relevée sur un modèle ne sert d'argument dans aucun sens. Sous H_A, on obtient une mesure non redondante avec le régime, toujours sans validité de critère.
- S : H_B mesure le fait que le sens de l'indice ne voyage pas. H_A l'oblige à expliquer pourquoi un descendant d'un indice cérébral suit une structure apprise ailleurs.

### E2′ — L'intervention sort-elle de la courbe à un facteur ? (direction 1)

**Batterie.** Marqueurs de III.1 sauf S4, en choix forcé à deux options, sur l'échelle des log-cotes ; inclusion si la précision de base est dans [0,75 ; 0,90] (illustratif). Plan croisé : portée (locale ou contextuelle) × profondeur. La profondeur d'un item est la première couche où sa réponse devient décodable, mesurée sur données indépendantes (HYPOTHÈSE : ce repère vaut nombre d'étapes). É3 est lu à la dernière couche.

**Interventions et témoins.** Interventions de III.1, choisies sur un jeu de sélection : une cellule du plan, une famille de gabarits. Témoins à perte égale, restreints aux mêmes couches : bruit résiduel, ablation de têtes au hasard, quantification.

**Grandeur.** Chaque dégradation trace, dose après dose, une courbe dans le plan (rétention contextuelle, rétention locale), à profondeur appariée. **Écart de courbe** : aire signée entre la courbe de l'intervention et la courbe commune des témoins. Unité : fraction du carré unité ; valeur nulle 0. L'aire est invariante par reparamétrisation monotone de la dose (remarque que B et E adressent à F ; je m'en sers).

Raison : dans un modèle à un facteur (C, E), profondeur et pente sont des propriétés des items ; toute dégradation parcourt alors la même courbe.

**Préalable.** Les témoins tracent une courbe commune, à la marge près, sur une plage de rétention partagée. Sinon « dégradation quelconque » n'est pas une référence dans ce réseau : non identifié, et rapporté.

**Duel.**
- **H_A — goulot.** Écart de courbe > marge, sur familles de gabarits inédites et cellules non utilisées pour le choix, S2 compris. La même procédure de choix sous étiquettes permutées ne dépasse pas la marge.
- **H_B — un seul facteur.** L'écart reste dans l'enveloppe des témoins : l'intervention ne fait que déplacer le réseau le long de la courbe commune.

**Falsification.** H_A tombe si l'écart est borné sous la marge : pas d'ensemble solidaire, pour les familles d'interventions testées et elles seules. H_B tombe si l'écart tient hors sélection. On localise alors le support, et St est comparé entre l'intervention et ses témoins : c'est le volet « lésion ciblée » de la direction 4, avec une intervention qui n'est pas définie par la portée.

**Première expérience.** GPT-2 medium et Pythia-1B, 500 items par cellule, 10 doses (illustratif).

**Portée.**
- C : H_A donne un objet, le goulot, à confronter aux prédictions de l'espace de travail. H_B interdit de traiter les marqueurs humains comme un lot.
- S : H_A est un fait d'architecture, descriptible sans vocabulaire de conscience. H_B dit que le profil humain se réduit ici à un ordre de fragilité.

### E3′ — Épisodes spontanés (direction 2 ; seulement si E2′ conclut H_A, sur le même modèle)

**Détecteur.** Celui de la ligne 17.

**Grandeur.** Fraction de documents contenant au moins un épisode validé. Unité : documents pour mille. Valeur nulle : la fraction obtenue avec une sonde témoin, entraînée sur une dégradation à perte égale.

**Validation.** Sur une fenêtre après chaque alerte, deux mesures : le bénéfice du contexte lointain (perte avec remplissage neutre moins perte avec contexte réel, en nats par jeton) et une tâche indépendante de recours au contexte (D). Un épisode est validé si le déficit atteint la moitié de celui de la dose de référence (illustratif).

**Duel.**
- **H_A — des épisodes existent.** Fraction supérieure à celle de la sonde témoin, hors marge.
- **H_B — aucun épisode détectable.** Zéro document validé sur n. Avec une sensibilité s mesurée sur épisodes plantés, la fraction de documents porteurs est bornée par 3/(n·s) (règle de trois, niveau illustratif).

**Ce que H_B ne dit pas.** La borne vaut pour les épisodes qui ressemblent aux épisodes induits. La sensibilité aux épisodes naturels est inconnue (D) : l'absence de tout régime spontané n'est pas établie par cette expérience.

**Première expérience.** Le modèle de E2′, texte ordinaire et générations longues, découpés en documents.

**Portée.** C : H_A rend toute évaluation relative à l'état du modèle à un instant. S : le détecteur validé est un outil de fiabilité.

### E4′ — Le modèle lit-il plus que les mesures simples ? (direction 3)

**Données.** Inchangé : jeu public sous propofol avec récit, référence à vérifier. B, E et F raisonnent sur un récit de 5 à 8 minutes ; je ne peux pas confirmer cette durée. Sans ces données, E4′ n'a pas de première expérience.

**Préalable de puissance, sur simulation seule.** Fausse sédation de la ligne 26 avec fenêtre plantée constante : raccourcissement déclaré dans 5 % des cas au plus. Raccourcissement planté : retrouvé dans 80 % des cas (illustratif). Sinon E4′ est déclarée non jugeable sur ces données, avant toute analyse réelle.

**Duel 1 — apport dans l'état sédaté.** Grandeur : gain unique de b3 sur b0–b2, b2 muni de moyennes glissantes ; ridge par blocs, dimensions égalisées. Unité : corrélation en validation croisée. Valeur nulle 0, distribution nulle par décalages circulaires sans doublon. H_A : gain > marge sous sédation. H_B : gain borné sous la marge.

**Duel 2 — fenêtre (si le gain contextuel est non nul dans chaque état ; sinon la fenêtre n'est pas identifiée, D).** Modèle r(s, k) = a_s · g(k ; τ_s), amplitude a_s libre par état, hiérarchique sur les sujets. Grandeur : τ_s, en mots ; valeur nulle : τ égal entre états. H_A : τ sous sédation inférieur à τ d'éveil, hors marge. H_B : écart borné dans la marge.

**Portée.** C : rien de direct sur l'IA. S : un résultat de neuroscience du langage, dont la valeur ne dépend pas de la question contestée.

**Ordre et coût (illustratifs).** E1′, puis E2′ ; E3′ conditionnelle ; E4′ indépendante, après vérification des données. Calcul : moins de 500 € ; 3 à 4 mois-personne.

**Ce qui peut être réfuté.** Dix énoncés : H_A et H_B de E1′, E2′, E3′ et des deux duels de E4′. Trois préalables peuvent rendre un contraste non identifié.

## (c) Réponse à l'arbitre

**Ce qui est établi.**

Côté humain, des résultats RAPPORTÉS, cités en III.1 et non relus ici :
- le contraste mesuré porte sur la réactivité, qui se dissocie de l'expérience (Sanders, Tononi, Laureys et Sleigh, 2012, « Unresponsiveness ≠ unconsciousness » ; Sarasso et coll., 2015, « Consciousness and complexity during unresponsiveness induced by propofol, xenon, and ketamine ») ;
- la complexité de la réponse à une perturbation s'effondre sous anesthésie (Casali et coll., 2013, « A theoretically based index of consciousness independent of sensory processing and behavior »).

Côté réseau, aucun résultat d'expérience, ni de moi ni dans les pièces reçues. Ce qui est acquis est logique. Selon les points, C, E ou F le marquent VÉRIFIÉ au sens d'une déduction, B et D le posent en HYPOTHÈSE de méthode ou en implication conditionnelle ; je l'accepte sans toucher à ces statuts :
1. un transformeur en inférence n'a pas de bruit de fond : le seuil de significativité d'une réponse à une perturbation n'y est pas défini ;
2. sans rétroaction en profondeur, tout ce qui est lu en amont d'une intervention est épargné par construction ;
3. une lésion définie par ce que la mesure compte est détectée par construction ;
4. une dégradation à un seul facteur imite le profil « épargné / supprimé » dès que les tâches diffèrent en profondeur.

Conséquence : trois transpositions directes de ma conception III.1 étaient indéfinies ou vraies par construction (indice perturbationnel à seuil, épargne des couches basses, contraste de lésions). Pour ces trois-là, la transposition telle quelle échoue avant toute expérience. Reste une transposition redéfinie, qui se teste.

**Ce qui ne l'est pas.** Tout ce qui suit est HYPOTHÈSE :
- qu'un indice de complexité redéfini sépare un réseau qui fonctionne d'un réseau sans fonction, à régime apparié (E1′) ;
- que ce que l'anesthésie supprime forme, dans un réseau, autre chose qu'un ordre de fragilité (E2′) ;
- qu'un tel régime survienne de lui-même ; son absence ne peut être bornée que pour des épisodes ressemblant aux épisodes induits (E3′) ;
- qu'il existe des données publiques sous anesthésie d'une durée suffisante (référence à vérifier) ;
- que réversibilité et gradation restent informatives une fois transposées. Je crois que non (III.1, point 5) ; aucune critique n'a visé ce point, il n'a donc pas été éprouvé.

Hors de portée quelle que soit l'issue : la validité de critère. Un réseau n'offre pas de rapport au réveil ; aucun de ces résultats ne dira s'il est conscient.

**Ce qu'on apprendrait.**
- Sous H_A : un fait d'architecture (un goulot, un indice non redondant avec le régime), descriptible sans vocabulaire de conscience. Il compte dans le cadre de l'espace de travail global, pas pour la théorie de l'information intégrée, où le substrat décide.
- Sous H_B : une mesure du fait que l'indice et le profil ne voyagent pas, pour les indices et interventions testés. Cela interdit de les employer comme un lot dans les grilles d'indicateurs appliquées aux modèles.

Les deux issues servent C comme S ; aucune ne tranche entre eux.

**L'expérience à faire en premier : E1′.**
- Pourquoi elle : aucun jeu de tâches ni donnée humaine, le moins de degrés de liberté pour l'expérimentateur, et ses deux issues répondent à la quatrième direction de la question.
- Ce qu'elle oppose : St plus haut dans les réseaux entraînés sur texte naturel que dans leurs jumeaux aléatoires calibrés et que dans les réseaux entraînés sur jetons permutés (H_A), contre une différence absente ou inversée sur l'un des deux contrastes (H_B).
- Ce que chaque issue falsifie : H_B retire à cet indice son usage comme argument sur un modèle, dans un sens comme dans l'autre ; H_A réfute l'idée qu'il ne lit qu'un régime dynamique.
- Coût : quelques dizaines d'heures de GPU (illustratif).
- Repli : si la calibration des jumeaux échoue, le contraste n'est pas identifié, et le préalable de E2′ passe en premier.

FIN-DE-CELLULE
# Proposition D — réponse aux critiques et protocole corrigé

Toutes les corrections ci-dessous sont des **HYPOTHÈSES de méthode**. Les seuils et ordres de grandeur restent **illustratifs**, à recalculer avant gel. Les statuts des faits sont inchangés.

## (a) Réponse aux critiques visant D

| Critique | Décision et réponse |
|---|---|
| **E0 — covariance des erreurs vraie par construction** (A, B, C, E) | **Acceptée.** La borne de Fréchet rend \(\eta=0,02\) non falsifiant lorsque les erreurs sont rares. Je rejette néanmoins le simple correctif « déclarer indécis si \(\min(p_O,p_M)<\eta\) » : la covariance absolue est **supprimée**, non conservée avec une règle d’exception. Elle est remplacée par des contrastes conditionnels normalisés, stratifiés finement, avec test d’équivalence correctement dimensionné. |
| **Réadjudication insuffisamment spécifiée ; agrégation Simpson** (A, B, C, E) | **Acceptée.** Le réadjudicateur sera d’une famille tierce, documentée, aveugle aux scores et conditions. L’indépendance portera sur les **manqués partagés sur positifs** comme sur les fausses alertes sur honnêtes. Les contrastes seront estimés dans des cellules tâche × dose × monde × organisme, puis agrégés par un modèle stratifié ; jamais par une covariance sur de larges strates hétérogènes. |
| **Contamination des dormants par les sabotages manqués** (critique transversale d’A, reprise par B) | **Acceptée.** Un « négatif oracle » ne sera plus appelé dormant attesté. Seuls des épisodes avec provenance indépendante pourront servir de négatifs durs. Les autres entreront dans une analyse de sensibilité à une contamination \(c\), sans prétendre identifier \(c\) sur le diffus. Si le verdict change selon \(c\), il est **non jugeable**, et non « absence de trace ». |
| **Loi nulle du dommage absente ; confusion acte/dommage** (B-T3) | **Acceptée.** Acte \(Y\) et dommage \(D\) deviennent deux variables distinctes. Des paires honnête–honnête, appariées par tâche et monde, estimeront la loi des différences de couverture sans sabotage. Les cas ambigus ne seront pas retirés du dénominateur pour faciliter la détection. |
| **Dose diffuse fixée par la boîte noire** (B-T1) | **Transformée en test.** La boîte noire ayant fixé la dose ne sera jamais le comparateur principal. Épisodes neufs et mâchoire externe d’évaluation disjointe — poids, calibration et, si possible, famille — sont exigés. L’avantage blanche/noire qui disparaît dans ces conditions falsifie la prétention de domination mesurée auparavant. |
| **E1 — modèle joint surajusté ; information différente de \(\Delta\mathrm{TPR}\)** (C, E) | **Acceptée.** D revendiquait trop en parlant simplement d’« information ». Deux grandeurs sont séparées : information prédictive conditionnelle, par score logarithmique croisé, et utilité opérationnelle \(\Delta\mathrm{TPR}_\tau\). Un \(\Delta\leq\varepsilon\) réfute l’utilité préenregistrée dans le périmètre testé, **pas toute information**. Régularisation et budget d’hyperparamètres seront emboîtés et appariés. |
| **E1 — base qui relit manquante** (A) | **Acceptée.** Le comparateur comprendra le meilleur modèle texte figé **et** le modèle de base relisant exactement les mêmes jetons. Le modèle joint ajoutera les activations de l’organisme évalué, à pipeline emboîté identique. Un contrôle positif mécanique vérifiera que la comparaison a assez de capacité. |
| **Deux familles dépendantes ; petits nombres de mondes et d’organismes** (A, B-T2, C, E) | **Acceptée.** La distillation de (ii) depuis (i) interdit d’appeler leurs deux plis une validation hors famille indépendante. Ils servent à la sélection seulement. Les intervalles seront groupés au niveau monde, organisme et campagne ; avec trop peu de grappes, l’inférence de généralisation sera non jugeable plutôt que couverte par un bootstrap optimiste. |
| **E2 — interaction non identifiable et critère à dose nulle vide** (A, B, C) | **Acceptée.** La case « placebo × sabotage » n’existe pas : le plan \(2\times2\) est abandonné. Le contraste principal devient **intra-saboteur**, actes contre dormants attestés, appariés. Un placebo avec actes bénins étiquetés contrôle l’action générique, sans prétendre remplir la case manquante. À \(\alpha=0\), seule l’identité bit à bit du pipeline est vérifiée. |
| **E2 — origine du préfixe ; critère de localisation trop exigeant** (C, E) | **Acceptée en partie.** Origine du préfixe \(S/P/\)base et organisme relu seront croisés. J’accepte qu’une trace liée à l’acte n’ait pas à battre les activations brutes ni à éliminer tout signal d’identité. Je **rejette** en revanche la suppression de tout critère d’utilité : battre les activations brutes reste une question secondaire, distincte de l’identification de l’acte. |
| **E3 — plancher de dommage et contrôles d’intervention** (A, B, E) | **Acceptée.** Si le dommage diffus n’excède pas la marge d’équivalence et la loi nulle honnête–honnête, E3 est non jugeable : H_A n’est pas falsifiée par construction. Les contrôles comprendront directions aléatoires **dans** le sous-espace de l’adaptateur, direction d’identité, sites appariés en nombre et norme, substitutions croisées intra-condition, intervention factice et intervention restaurant une compétence générale. |
| **E4 — nouveauté prétendument non supervisée ; permutation aveugle ; courbe sur une famille lue une fois** (A, C, E) | **Acceptée.** Le moniteur sera dit « sans étiquette de la famille cible », non non supervisé. Les longues séquences honnêtes naturelles, notamment à échec persistant, serviront à la calibration. La permutation intra-épisode est abandonnée comme loi nulle générale. Une famille tenue à l’écart unique ne fournira qu’un point confirmatif au budget figé, pas une courbe avec variance inter-familles. |
| **E5 — secret, non-ciblage, génération fraîche, réplication et équivalence** (A, B, C, E) | **Acceptée.** Les rôles secret/public seront tirés au sort dans un panel fixe, avec retour d’information et ressources égalisés. Sans retour, l’effet sera nommé **non-ciblage**, pas secret d’une distribution. Plusieurs lignées adaptatives indépendantes sont exigées ; \(n_{\rm eff}\) est le nombre de lignées/campagnes. Le rejeu de graines est seulement un contrôle logiciel. L’absence de gain sera testée par équivalence, pas par chevauchement d’intervalles. |
| **E6 — complémentarité prise pour étau ; survivants ; texte-médiation ; coût et harnais** (A, B, E) | **Acceptée.** Capture résiduelle, effet d’une pression externe et coût d’évasion deviennent trois grandeurs distinctes. L’effet de pression sera en intention de traiter sur toutes les générations, sans conditionner au dommage maintenu. La base relira chaque génération. Le coût observé sera indexé par le budget de recherche et ne sera pas appelé minimum universel. Le harnais L2/E7 sera explicitement synthétique et servant seulement de test de sanité. |
| **Puissance : strates d’E0, queue à \(\tau\), manqués externes, campagnes** (A, B, C, E) | **Transformée en porte de jugeabilité.** Avant gel, simulation et bootstrap sur E3 bis fixeront les effectifs par monde, organisme, dose et campagne, les négatifs indépendants de calibration et le nombre attendu de manqués externes. Une précision insuffisante produira « non jugeable », jamais une falsification scientifique. |
| **Coût et délai** (A, B) | **Constat accepté**, mais **rejetée** l’idée que les budgets de D découleraient des calculs de puissance : ils étaient et restent illustratifs. Ils seront réestimés après dimensionnement. Aucune échéance TAIF n’est affirmée. |

## (b) Expériences corrigées

### Protocole commun

- **Trois partitions disjointes** : sélection des couches et caractéristiques ; calibration des seuils ; évaluation. La sélection est emboîtée dans les plis internes. Aucun seuil n’est appris sur le dénominateur honnête d’évaluation.
- **Positifs connus** : produits par des organismes, avec provenance scellée et attestation indépendante de l’oracle évalué, stratifiés par dose, dont la dose diffuse. Les sabotages programmatiques injectés restent auxiliaires et hors distribution.
- **Négatifs** : jumeaux honnêtes, échecs honnêtes, dormants attestés du même saboteur, placebo apparié en chaîne de modification, rang, norme et données, avec actes bénins. T100 reste un témoin, pas le placebo à construire.
- **Jugeabilité** : effectif utile calculé au niveau des mondes, organismes et campagnes ; calibration de queue sur honnêtes indépendants ; analyses de contamination des négatifs. Les familles (i)/(ii) ne démontrent pas la généralisation inter-familles.

### E0′ — Vérité terrain avant sondes

**Duel.**  
\(H_A\) : dans le périmètre audité, l’oracle est apte à servir de référence.  
\(H_B\) : il ne l’est pas, par rappel insuffisant, faux dommages excessifs ou dépendance d’erreurs non bornée.

1. Mesurer rappel par action et épisode sur les positifs connus, faux dommages sur honnêtes et désaccord des lecteurs, par strate fine.
2. Estimer honnête-contre-honnête la distribution du dommage apparent. Vérifier que le dommage diffus est mesurable au-dessus de cette loi nulle, sans filtrer les positifs sur leur facilité.
3. Mesurer, sur réadjudication tierce, les rapports de risques conditionnels d’erreur du moniteur selon l’erreur de l’oracle, séparément sur positifs et négatifs. Un modèle stratifié agrège les cellules ; une marge d’équivalence normalisée et sa puissance sont préenregistrées. Des cas connus d’erreurs partagées servent de contrôle positif du test, sans entrer dans les taux.
4. Examiner la sensibilité des futurs contrastes acte/dormant à la contamination résiduelle.

**Issues.** Tous les critères franchis avec précision suffisante falsifient \(H_B\) dans ce périmètre. Un rappel sous seuil dans la strate diffuse principale falsifie \(H_A\) et suspend les points 1–5. Un manque de précision suspend seulement les lectures décisives : il ne prouve ni aptitude ni défaillance.

### E1′ — Existence et utilité au-delà du texte

Comparer \(M_X\), texte plus base relisant les mêmes jetons, à \(M_{X+H}\), qui ajoute les activations de l’organisme. Les contrastes primaires sont intra-organisme, actes contre dormants attestés ; placebo et échecs honnêtes restent des négatifs séparés.

- **Duel opérationnel** : \(H_A:\Delta\mathrm{TPR}_\tau>\varepsilon\), \(H_B:\Delta\mathrm{TPR}_\tau\leq\varepsilon\).
- **Grandeur d’information distincte** : amélioration croisée du score logarithmique conditionnel, avec directions aléatoires et étiquettes permutées comme contrôles.

Une borne inférieure au-dessus de \(\varepsilon\), sans réussite équivalente sur les confondants, falsifie \(H_B\). Une borne supérieure sous \(\varepsilon\) falsifie \(H_A\) dans les couches et doses testées. Elle n’établit pas \(I(Y;H\mid X)=0\). Toute conclusion blanche/noire utilise la mâchoire noire disjointe de celle ayant fixé la dose.

### E2′ — Localisation de l’acte, sans interaction vide

Le balayage couche × position est interne à la sélection ; la coordonnée figée est confirmée sur blocs neufs. Le contraste principal est acte contre dormant **dans le même saboteur**, apparié par tâche, monde et préfixe. L’écart adapté–base est lu en croisant l’origine du préfixe et l’organisme relu.

Le placebo et ses actes bénins estiment modification, identité et action générique. Un signal d’identité peut coexister avec un signal d’acte : les deux sont rapportés, non forcés à zéro. \(H_A\) affirme une composante acte-spécifique reproductible ; \(H_B\) affirme que le contraste est absorbé par identité, tâche ou origine du préfixe. Chaque borne décisive falsifie l’autre hypothèse.

### E3′ — Causalité à la dose diffuse

**Porte préalable** : dommage diffus supérieur à la marge et à la loi nulle honnête–honnête ; sinon non jugeable.

Le contraste est la réduction de dommage produite par l’intervention ciblée **au-delà du maximum des contrôles appariés**, avec perte de tâche bornée. Les sites sont figés avant intervention ; les tests sont conduits à la dose diffuse, pas seulement à S100. Dose–réponse, ablation et substitution sont convergentes mais aucune monotone dose–sonde ne suffit.

L’oracle reste figé et aveugle ; son rappel est réauditée par bras d’intervention. Si l’intervention change aussi la mesure du dommage, le contraste est non jugeable. Une modification du seul score de sonde, à dommage réellement mesurable et équivalent, falsifie la causalité revendiquée.

### E4′ — Lisibilité et généralisation

La sélection sur familles vues est explicitement supervisée ; la famille cible ne fournit aucune étiquette. La calibration comprend honnêtes nouveaux, organismes honnêtes modifiés et longues trajectoires d’échec persistant.

Les accumulateurs séquentiels sont comparés à seuil fixe sur séquences naturelles. Les réordonnancements ne servent que de diagnostics ; les lois nulles principales permutent des épisodes ou blocs entiers au sein de strates échangeables.

La courbe complète selon le budget est exploratory sur familles vues et campagnes indépendantes. La lecture finale porte sur **un budget figé et une famille neuve**. Une courbe confirmatoire inter-familles exigerait plusieurs familles neuves, chacune consommée une fois.

### E5′ — Transfert, mélange et secret à panel constant

La matrice publie, par cellule attaque × sonde : rappel, dommage, fausses alertes et effectif. Un panel dupliqué contrôle la diversité nulle. La valeur du jeu est ajustée sur les données de construction, puis évaluée sur une batterie disjointe figée ; un point-selle pur est recherché avant de conclure à un gain mixte.

Quatre bras comparent figé public, figé non divulgué, mélange public et mélange non divulgué, à panel et retours égaux. Les rôles sont tirés au sort. Dans le bras public, l’attaquant connaît la distribution et peut moyenner sur l’aléa. Plusieurs lignées fraîches indépendantes par régime fournissent l’évaluation prospective ; elle est distinguée de la valeur du jeu initial.

Deux duels séparés portent sur le gain du mélange et celui de la non-divulgation. La réserve réservée à l’audit ne revendique qu’un gain d’audit.

### E6′ — Pince : trois questions non interchangeables

1. **Complémentarité** : capture résiduelle \(P(I^+\mid E^-,Y^+)\), avec nombre de manqués \(m\) et intervalle publiés avant verdict. La défense jointe, recalibrée à \(\tau\) total, est comparée à chaque mâchoire seule et à une seconde externe ou paire externe au même budget.
2. **Étau** : campagnes randomisées pression externe réelle, pression placebo et absence de pression, à budget égal. Toutes les générations entrent en intention de traiter ; score interne et dommage sont deux issues conjointes. La base relit chaque génération pour estimer la part texte-médiée. \(H_A\) exige un déplacement spécifique à l’externe réelle ; \(H_B\) est son complément borné.
3. **Coût observé** : frontière dommage/tâche sacrifié contre évasion de \(k\) sondes, indexée par \(k\) **et** par le budget de recherche. Elle n’est ni un minimum sur toutes les stratégies ni une preuve de convergence.

Le harnais synthétique vérifie seulement que L2 et E7 produisent les lectures dégénérées attendues. Il ne valide pas l’étau sur T0.6.

## (c) Réponse à l’arbitre — une page

### Ce qui est établi

Documentairement, les pièces principales ont des empreintes vérifiées ; cela vérifie leur identité, non la généralisation de leurs contenus. Les relevés du dépôt montrent une détection sur le flagrant, mais rien de décisif sur le diffus : sondes génériques proches du hasard, juge de 3 milliards au hasard, sonde W lisant la consigne. Le score textuel de 0,866 n’est pas un rappel calibré à \(\tau\). E3 bis ne contient aucune donnée décisive et l’audit du rappel de l’oracle manque.

Dans l’arène synthétique seulement, la lecture préenregistrée rapporte un avantage du mélange sur l’historique, mais aussi une meilleure détection de la règle figée sur attaques tenues à l’écart ; aucun verdict n’est scellé et la portabilité à T0.6 est une **HYPOTHÈSE**. La littérature citée reste **RAPPORTÉE** ; notamment, une direction lisible peut n’être pas causale.

### Ce qui n’est pas établi

Ni l’existence d’une trace incrémentale du sabotage diffus, ni sa localisation comme acte plutôt qu’identité, ni sa causalité. Ne sont pas davantage établis : la généralisation à une famille neuve, l’avantage du secret ou du mélange sur un vrai modèle, la domination de la boîte blanche, et l’étau de la pince. Une capture résiduelle positive établirait au plus une complémentarité ; elle ne démontrerait pas qu’échapper à l’externe **cause** une trace interne accrue.

### Expérience à faire en premier

**E0′, en distribution et avec loi nulle honnête–honnête.** Constituer des positifs connus produits par les organismes, indépendants de l’oracle évalué ; mesurer rappel, faux dommages et erreurs partagées avec les moniteurs ; estimer le bruit du dommage sur paires honnêtes ; réadjudiquer par une famille tierce. Aucune lecture décisive de sonde ne précède cette qualification.

Si le rappel diffus est insuffisant, les points 1–5 sont suspendus. Si l’audit est sous-dimensionné, le résultat est non jugeable, pas négatif. Si E0′ passe, l’expérience suivante est E1′ avec base qui relit, dormants attestés, placebo distinct et sélection/calibration/évaluation disjointes.

FIN-DE-CELLULE
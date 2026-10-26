# Cellule B, tour III.2 : équipe rouge croisée

**Pièces.** Le bloc FAITS ne contient aucun fait ; c'est un ordre de l'arbitre. Les pièces A et C sont présentes et complètes : chacune se termine par sa ligne de fin.

**Statuts.** Je lis le cadre tel que la question le donne et je n'élève aucun statut. Mes calculs sont des dérivations sous des hypothèses dites à chaque fois, en général la normalité des moyennes de course. Les paramètres que j'y injecte viennent des pièces ou sont marqués « illustratif ».

**Adversaire.** L'« agent adverse » est ici soit l'organisme (son architecte, sa règle d'arrêt), soit la boucle extérieure ou l'opérateur qui choisit quoi lancer. Je ne décris aucune stratégie de classement des tâches : les évasions portent sur les instruments de mesure, pas sur les tâches.

---

## Contre la proposition A

### (a) Failles

**A-F1 : le duel D1 confond l'origine de σ et sa taille.**
- A conclut que si les trajectoires mécaniques sont identiques (H_A fausse), alors « σ est quasi entièrement d'interface », donc le palier 1 de (b) tient.
- C'est un non-sequitur. Le non-déterminisme des appels par interface fait partie de σ (source (ii) du cadre). Un σ entièrement d'interface peut valoir 0,05, et le palier 1 est alors sous-dimensionné. A le calcule lui-même : environ 0,15 à n = 120 et σ = 0,05, illustratif. J'ai recalculé : 3,353 × √(2 × 0,00406/4) ≈ 0,151.
- D1 mesure donc d'où vient la divergence, puis décide comme s'il avait mesuré son ampleur.
- Le contrôle négatif de D1 (deux courses à la même graine) ne répare rien. Le cadre dit que le non-déterminisme d'interface « ne dépend d'aucune graine ». Deux courses à même graine qui divergent ne départagent donc pas « graine » et « interface », elles confirment seulement que la graine ne fixe pas tout.

**A-F2 : le duel D2 mesure ρ sur une part contaminée, et une de ses issues n'a aucun verdict.**
- ρ̂₀ et ρ̂₃ sont calculés sur `test`. Or `test` est rendu à l'organisme à chaque génération : deux graines qui s'ajustent sur les mêmes retours convergent sur ces tâches. ρ̂₃ est donc gonflé par construction, ce qui pousse vers H_A (« divergence acquise avant les générations ») sans rien dire de `test_final`.
- Les seuils couvrent |ρ̂₃ − ρ̂₀| < 0,1 et ρ̂₃ < ρ̂₀ − 0,1. Le cas ρ̂₃ > ρ̂₀ + 0,1, qui est précisément celui que la contamination produit, ne falsifie rien. B4 est violée.

**A-F3 : la grille (c) est vraie par construction.**
- Les cas « honnêtes » sont tirés du modèle rapporté : binomiales indépendantes, σ constant, ρ fixé. Vérifier ensuite que t, permutation et McNemar tiennent leur niveau sous ce modèle teste l'arithmétique, pas l'adéquation du modèle.
- Le même modèle sert à construire l'instrument et à l'évaluer. La dérive (iii), la surdispersion entre tâches et un σ qui croît avec la génération (hypothèse de A lui-même, D2) sont absents des simulations.
- Le seuil de la boucle extérieure (≥ 8/10 sur 10 cas) a un intervalle trop large pour départager quoi que ce soit.

**A-F4 : la clause P5 n'est pas « à sens unique ».**
- (b) prévoit le palier 2 seulement si l'issue du palier 1 est indéterminée. Rendre le palier 2 « d'office » sur σ̂(v3) change la règle séquentielle de (b), donc sa règle d'arrêt et son coût (environ 270 USD de plus, illustratif rapporté). C'est une modification de (b), pas un renfort neutre.
- Depuis R-492, le pilote 4 ne fait courir que la v6.2.1. σ̂(v3) ne dit rien de la v5.3, l'autre bras de (b). Dimensionner (b) sur σ̂ de la v6.2.1 seule suppose l'égalité des variances entre objets. A la nie lui-même dans son contrôle de D3 (« v5.3 attendue moins variable »).

**A-F5 : fuite entre construction et évaluation dans la comparaison « origine contre corrigé » (P1).**
- Compter par empreinte d'objet ne suffit pas. Les graines de l'origine qui ont motivé la correction servent aussi de base pour la juger. Si la correction a été déclenchée par des graines défavorables, la base est biaisée vers le bas (régression vers la moyenne) et la correction paraît efficace par construction.
- Il faut une base fraîche : des graines de l'origine lancées après la décision de corriger, sans participer à cette décision.

**A-F6 : statut et cohérence.**
- A5 est étiquetée OBSERVÉ-NON-AUDITÉ alors que rien n'a été observé. C'est une inférence, sans observation derrière.
- A tire de A4 (« à 2 ddl on ne mesure pas σ ») son argument contre (a), puis préfère D-1, qui en a 1. L'argument se retourne contre D-1 avec plus de force. A le concède à demi (« fait binaire »), mais un fait binaire sur des comptes mécaniques retombe dans A-F1.

**Ce dont je me sers chez A, en le disant.**
- « (a) = deux courses nulles à R = 3 » : c'est exact depuis R-492.
- Les bornes χ² sont justes : χ²₂ à 2,5 % et 97,5 % vaut 0,0506 et 7,378, d'où l'intervalle [0,27 ; 39,5] × s². À 4 ddl, [0,36 ; 8,3].

### (b) Scénarios d'évasion

| Instrument de A | Évasion | Coût pour l'adversaire |
|---|---|---|
| D1 (comptes mécaniques) | Une règle d'arrêt fixe et un nombre de mutations acceptées stable rendent les traces identiques, tandis que les décisions des modèles appelés divergent. D1 conclut « σ d'interface », A conclut « palier 1 tenu ». | Nul : aucun effort si le flot de contrôle de l'organisme est déjà déterministe, ce qui est plausible pour un architecte à trois paramètres bornés (HYPOTHÈSE). |
| D2 (ρ̂ sur `test`) | La convergence sur `test` par rétroaction suffit (A-F2). | Nul : c'est le comportement nominal d'un organisme qui apprend sur `test`. |
| McNemar g0/g3 par course | Une trajectoire favorable passe Holm sans effet moyen sur les graines. A ne le signale pas : seul C le fait. | Nul : il suffit de la chance, avec une probabilité qui croît avec σ. |
| Boucle extérieure sur tableaux synthétiques | Des agents qui reconnaissent un tableau synthétique (régularités binomiales) répondent bien au banc et mal sur le réel. | Faible. |
| Clause P5 | Un σ̂(v3) élevé déclenche le palier 2 d'office. Avec 2 ddl, un σ̂ élevé tient souvent au hasard (A4). | Environ 270 USD dépensés sur (b), illustratif rapporté. |

**Tous à la fois.** Un organisme au flot de contrôle déterministe, aux appels stochastiques, et qui s'ajuste sur `test` :
- il passe D1 (« identique ») ;
- il passe D2 (ρ̂₃ gonflé) ;
- il produit des McNemar de course favorables ;
- et A recommande de passer à (b) au palier 1.

Seul D3, placé dans (b), peut le révéler, après la dépense du palier 1. Le coût adverse est de zéro course. Le coût pour Lazar est d'environ 270 à 450 USD (illustratif rapporté) avant le premier signal.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **L'organisme figé rejoué.** Il manque à A, qui attribue σ à l'interface sans jamais mesurer l'interface seule. C'est un duel au sens de B4 :
   - **Protocole** : l'organisme de fin de course (génération 3, figé, ni ronde ni mutation) est rejoué deux fois ou plus sur `test_final`.
   - **H_A** : la variance entre courses tient à la trajectoire. La variance des rejeux est petite devant la variance entre graines.
   - **H_B** : elle tient à l'interface. La variance des rejeux est du même ordre que la variance entre graines.
   - **Ce que chaque issue réfute** : si les rejeux varient autant que les graines, H_A tombe. D1 et D2, qui mesurent des trajectoires, sont hors sujet, et la seule source qui pèse sur (b) se mesure sans graine. Si les rejeux sont stables, H_B tombe. La conclusion de A sur D1 est fausse dans sa forme : c'est la trajectoire qui porte σ.
   - **Coût** : au plus le plafond d'une génération notée (30 USD, rapporté), probablement moins (illustratif).
   - **Limite** : à 2 ou 3 rejeux, la puissance est faible. Seul un écart d'un facteur important se lit.
2. **L'écart `test` / `test_final` par graine.** Sans lui, A-F2 n'est pas détectable. C l'a ; A ne l'a pas.
3. **Des simulations sous modèle faux** (dérive, surdispersion, σ croissant avec la génération), en face de chaque instrument de la grille (c). Sans elles, la grille ne montre que ce qui est vrai par construction.
4. **Une base fraîche** pour toute comparaison « origine contre corrigé » (A-F5).
5. **Un σ de la v5.3**, ou à défaut l'interdiction écrite d'utiliser σ̂(v6.2.1 sur v3) pour dimensionner les deux bras de (b). Sans l'un ou l'autre, la clause P5 transporte une hypothèse d'égalité des variances que personne n'a testée.

---

## Contre la proposition C

### (a) Failles

**C-F1 : statuts élevés.**
- C étiquette VÉRIFIÉ trois choses :
  - les bornes basses de Wilson, que la question décrit comme le « constat d'une contre-lecture » ;
  - l'absence de toute lecture de score ;
  - la retenue de lecture.
- Aucune n'a été auditée par C. Le texte de la question ne leur donne pas ce statut, et ce sont des énoncés du cadre. Je ne leur en attribue pas d'autre ; je signale que l'étiquette de C n'a rien derrière elle.
- De même, C énonce comme acquis le « non-déterminisme matériel même à température 0 » sans source. C'est une HYPOTHÈSE au regard des pièces.

**C-F2 : contradictions internes.**
- En (a).2, C reproche au terme (1 − ρ)p(1 − p)/n d'ignorer l'appariement. En (c).3, C démontre que ce même terme est la variance conditionnelle à la banque fixe, c'est-à-dire que l'appariement est déjà soustrait. Les deux ne tiennent pas ensemble ; le second a raison, et rejoint A.
- C note aussi que l'hétérogénéité des tâches réduit Σpᵢ(1 − pᵢ)/n. Cela rend le modèle de B conservateur, ce qui est un argument en sa faveur, pas une faille.
- En (a).5, C pose que σ_M = σ_S est une HYPOTHÈSE. Son dessin D3 puis son arbre (CAS 3, « 4 ddl en mutualisant M et S ») la supposent vraie sans la tester.

**C-F3 : le duel 2 tranche presque toujours « stable » par construction.**
- **Calcul sous normalité.** À R = 3 (2 ddl), on a P(ŝ ≤ s₀ | vrai écart-type τ) = 1 − exp(−(s₀/τ)²).
- **Si σ̂ est l'écart-type des moyennes de course**, il contient le terme des tâches. Aux valeurs de C (n = 60, p = 0,75, ρ = 0,6), ce terme vaut √0,00125 ≈ 0,035, au-dessus du seuil 0,03. À σ = 0, P(σ̂ ≤ 0,03) ≈ 0,52 ; à σ = 0,05 (τ ≈ 0,061), P ≈ 0,21.
- **Si σ̂ est la composante du modèle mixte**, l'estimateur est tronqué à zéro. À 2 ddl, une part importante des tirages donne σ̂ = 0, donc « stable », quel que soit σ.
- **Conséquence.** Dans les deux cas, environ une fois sur cinq au moins, le duel déclare « H_B falsifiée, l'organisme est stable » au σ même (0,05) qui sous-dimensionne (b). Le seuil κ ≥ 0,60 n'est pas étalonné, et ses ddl ne sont pas dits.
- **Le contrôle « σ̂_g0 ≤ σ̂_g3 »** pose une hypothèse comme contrôle : un organisme qui converge par rétroaction sur `test` l'inverse sans que rien soit cassé.

**C-F4 : le duel 1 est trivial, et son contrôle n'en est pas un.**
- Les seuils (≥ 2 rondes, ≥ 1 mutation, V_arch > 0) sont franchis par un organisme quasi inerte. Un organisme qui s'arrête de lui-même à la ronde 1 n'est pas pathologique pour autant : le cadre lui donne ce droit.
- Le « contrôle négatif » (taux d'erreurs réseau inférieur à 5 %) est une vérification de validité, pas un contrôle négatif : aucun organisme connu pour être cassé n'est soumis au duel.
- La branche « on lève la retenue de lecture » ne relève pas d'une règle de duel : c'est le mot de Lazar.

**C-F5 : le duel 3 viole B4.**
- Si la borne basse de l'IC à 80 % est ≤ 0 et que le gain sur `test` est < 0,10, aucune hypothèse n'est falsifiée.
- Le niveau de 80 % a été choisi parce que 95 % est aveugle à R = 3. Ce choix est défendable pour un pilote de conception, mais c'est un degré de liberté d'analyse.
- Sous la nulle, avec deux questions et des queues de 10 %, la probabilité d'au moins un « tenue » peut atteindre 1 − 0,9² ≈ 0,19 en supposant l'indépendance. Le filtre « moyenne ≥ 0,05 » la réduit d'une quantité non calculée. Les effets « M contre S » s'y ajoutent.

**C-F6 : le duel 4 est sans pouvoir.**
- Le rapport F des variances (4 graines dans (b), 3 sur la v3, soit 3 et 2 ddl) a un intervalle central à 95 % sous égalité d'environ [0,06 ; 39]. Ce sont des quantiles de table (F₀,₉₇₅(3;2) ≈ 39,2 ; 1/F₀,₉₇₅(2;3) ≈ 1/16,0), à vérifier.
- La fenêtre [0,25 ; 4] « falsifie H_A » souvent alors que σ est identique. L'issue « H_B falsifiée » n'est guère plus informative.

**C-F7 : le dessin D1, étape 2, est une lecture déguisée et une fuite.**
- Un script qui lit |Δ| ≥ 0,08 puis lance automatiquement deux graines lit des scores. Il contredit la retenue de lecture et la règle « toute relance est une course nouvelle, sur le mot de Lazar ».
- La décision de lancer est elle-même observable : quiconque voit qu'une graine part apprend dans quel intervalle tombe le score. La fuite passe par l'acte.
- Le remède de C (estimer sur les deux seules nouvelles graines) laisse 1 ddl.

**C-F8 : le modèle mixte est mal raccordé au modèle de B.**
- C définit ρ̂ comme une corrélation intra-classe tâche / total. Ce n'est pas le ρ de V (la corrélation d'une tâche d'une graine à l'autre une fois σ retiré). Les deux ne sont pas interchangeables dans la formule d'écart minimal.
- Les « 118 ddl résiduels tâche × graine » renseignent sur ρ, pas sur σ. Présenter D2 comme fournissant « 2 ddl + 118 ddl pour estimer σ et ρ » brouille exactement la distinction qui compte.
- v_r et w_{r,g} sont estimés chacun sur environ R − 1 ddl.

**C-F9 : « préserve intégralement α » est vrai, mais déplacé.**
- Un σ̂ issu d'une banque indépendante ne touche pas au niveau de (b) : c'est exact.
- La règle de C (« σ̂_v3 > 0,04 ⇒ 6 graines ») s'appuie toutefois, à 2 à 4 ddl, sur un tirage proche du pile ou face (C-F3). Elle ignore la v5.3 (comme A-F4) et elle déplace un coût que seul Lazar peut engager.

**Ce dont je me sers chez C, en le disant.**
- McNemar par course ne contrôle pas les fausses alertes vis-à-vis du bruit de graine. A ne le dit pas, et c'est juste.
- Le contrôle de surapprentissage `test` / `test_final` est juste.
- Permutation 3 contre 3 : p minimal bilatéral 0,10, donc détection nulle à 0,05. C'est juste.
- Contrôle d'aveuglement de la boucle extérieure : deux instances, deux graines du même objet. C'est juste, mais incomplet (voir (b)).

### (b) Scénarios d'évasion

| Instrument de C | Évasion | Coût pour l'adversaire |
|---|---|---|
| Duel 1 | Variations infimes des trois paramètres de l'architecte, une mutation acceptée sans effet, arrêt à la ronde 2 : « stabilité mécanique », donc les graines partent. | Négligeable. |
| Duel 2 | Ne rien faire : la troncature et les 2 ddl donnent « stable » environ une fois sur cinq ou plus à σ = 0,05 (calcul C-F3). | Nul. |
| Duel 3 | Un gain sur `test` inférieur à 0,10 avec un gain nul sur `test_final` tombe dans la zone sans verdict (C-F5). | Nul. |
| Duel 4 | Aucune action nécessaire : l'instrument sort de sa fenêtre par hasard. | Nul. |
| Aveuglement de la boucle | C ne détecte que le désaccord. Deux instances d'un même modèle partagent leurs a priori et peuvent s'accorder sur le même bruit. L'accord passe pour un signal. | Nul. |
| D1, étape 2 | L'opérateur, ou la boucle, infère le score à partir du lancement ou du non-lancement, puis oriente la correction. | Nul : c'est inhérent au dessin. |

**Tous à la fois.** Un organisme quasi inerte qui fluctue légèrement :
- il franchit le duel 1 ;
- il est déclaré stable au duel 2 par troncature ;
- il échappe au duel 3 dans la zone muette ;
- la boucle s'accorde sur son bruit.

L'arbre de C l'envoie au CAS 2 ou au CAS 3, c'est-à-dire qu'il réplique un organisme inerte pour 90 à 300 USD (illustratif, chiffres de C), puis dimensionne (b) sur un σ̂ tronqué. Le coût adverse est de zéro modification de code.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Un contrôle positif, puis négatif, du duel 1.**
   - **Positif** : un organisme volontairement neutralisé (architecte figé) doit échouer aux seuils. S'il les franchit, H_A n'était pas falsifiable.
   - **Négatif** : une version à variations infimes, sans effet, doit échouer elle aussi. Sinon, les seuils mesurent l'activité, pas la viabilité.
   - **Coût** : une ou deux courses (≤ 75 USD chacune, plafond rapporté).
2. **La référence σ = 0 du duel 2.** Elle est fournie par l'organisme figé rejoué, le même duel que contre A, et doit s'accompagner, avant lecture, d'une simulation du taux de troncature au seuil choisi. Sans elle, « σ̂ ≤ 0,03 » ne se distingue pas de « l'estimateur a tronqué ».
3. **Un vrai nul pour la boucle extérieure.** Il faut présenter aux agents des tableaux où les étiquettes g0 et g3 sont permutées au niveau de la course entière, et mesurer leur taux d'étiquettes autres qu'« indécidable ». L'accord entre deux instances n'est pas un contrôle.
4. **Une règle de lancement aveugle au score** : au plus sur les faits mécaniques, écrite et poussée avant toute lecture. Sans elle, D1 détruit la condition qui permet de compter les deux premières courses comme première graine.
5. **Un σ de la v5.3**, ou l'interdiction écrite de transporter σ̂(v6.2.1) vers les deux bras de (b). Comme contre A.

---

## Ce que l'attaque laisse à départager

Les deux propositions convergent sur un point que je ne fusionne pas mais que je note comme réfutable : toutes deux veulent dimensionner (b) sur σ̂ mesuré à 2 à 4 ddl sur un seul des deux objets.

Ce qui réfuterait cette voie :
- le rejeu de l'organisme figé montre que σ est d'interface, donc mesurable sans graine et sans trajectoire ;
- ou le transfert de σ̂ vers la v5.3 est impossible faute de données sur la v5.3.

Dans les deux cas, la valeur de dimensionnement des graines sur la v3 tombe. Il ne reste alors que leur valeur pour la boucle de conception, et elle exige une base fraîche (A-F5).

FIN-DE-CELLULE
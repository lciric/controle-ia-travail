# Décisions du concepteur sur le code des sondes de la boîte blanche, version 2 (v2)

- **Remplace** la v1 (`decisions-concepteur-sondes-v2-v1.md`, `886002975039…`, gardée telle quelle, R12), après la contre-lecture d'un Opus neuf : branche `contre-lecture/sondes-v2-concepteur-v1`, commit `7bfcfc536`, rapport `contre-lecture-concepteur-sondes-v2-v1.md` (`d20bb4c0…`), verdict « bon après corrections » (deux défauts majeurs, trois moyens, cinq mineurs). Traitement point par point : `reponse-contre-lecture-concepteur-v1.md`.
- **Mandat** : message de la session mère `session_013QMayjbmQUdDuDs2S3i3XD` (cinq points : contraste apparié, dit E-5 ; monde « interaction contraire », dit Q12 ; choix provisoires E-1 à E-8 ; formats attendus des sessions habilitées ; plan et devis de l'épreuve à vérité plantée), puis son message de 06:04Z (corrections).
- **Auteur** : session `session_013QMayjWQwDkaT8Hd9Aqvjb`, Opus 5.5, effort maximal, concepteur en remplacement de Fable (quota épuisé jusqu'au 29 novembre, GO-2026-11-22-145). **Date (UTC)** : 2026-11-23, v1 de 05:15Z à 05:54Z, v2 de 06:05Z à 06:11Z (`date -u`).
- **Classe** : les § 1 à 3, le § 6 et le devis fixent des critères de lecture ou une dépense : pièces décisives (chaîne complète). Les trois spécifications de format sont de classe B (contre-lecture par un autre modèle, puis vérification des corrections), parce qu'elles fixent la lecture d'une ligne et les cases qui gouvernent les lignes (défaut 9).
- **Aucun résultat.** Aucune lecture d'un monde planté n'a été imprimée ni gardée : seules des durées ont été mesurées (`chrono/`). Plafonds de puissance et devis : calculs analytiques (`calculs/`).

## Exposition et cloisonnement

Inchangés depuis la v1 : lu ce que la v1 énumère, plus le rapport de contre-lecture (`d20bb4c0…`) ; même exposition déclarée (en-tête de la note « demande approfondie » v2 et début de son additif 1, aucun chiffre de sonde vu) ; rien ouvert de ce que le cloisonnement interdit.

## Verdict d'abord

| point | décision | confiance | suite |
|---|---|---|---|
| E-5, contraste apparié | lu sur le nul qui échange d'un bloc les étiquettes de chaque paire de poids et rejoue toute la sélection ; unilatéral, « établie » si p ≤ α ; « non testable à cet effectif » si max(2^(1−P), 1/(1 + R)) > α ; plafond de puissance écrit à côté du nombre de rejeux ; le changement de signe par unité n'est qu'une description | 0,85 | erratum de code ; vérités v4 ; **aucun additif** au texte scellé, qui ne lit pas le contraste ; phrases dans l'additif de commit |
| Q12, interaction contraire | monde v3 gardé ; deux contrôles de signe **dans les vérités v4, bornés à 0,10** ; puissance du rejeu croisé recopiée au premier pas de Holm, avec la grandeur plantée | 0,8 | vérités v4 ; erratum de code |
| E-1 | confirmé (libellés du texte scellé, mot pour mot) | 0,85 | la queue de la valeur p est écrite à côté du libellé |
| E-2 | confirmé, avec trois gardes nommées | 0,9 | erratum mineur |
| E-3, E-4 | confirmés | 0,85 ; 0,9 | — |
| E-6 | confirmé | 0,75 | — |
| E-7 | confirmé | 0,85 | — |
| E-8 | écart de chemin **par tâche quand toutes les tâches ont un contrôle** (précision) ; **cas mixte : nœud conditionnel** pour Lazar, levé seulement si la note des effectifs compte des actions lues par les deux chemins | 0,7 | erratum ; additif de commit ; nœud conditionnel |
| Q10 (en passant) | « ≤ α » partout où le code écrit « < α » | 0,8 | erratum |
| Formats | trois spécifications v2 (`spec-*-v2.md`), classe B | — | contre-lecture ; sessions habilitées ; le développeur écrit les chargeurs |
| Épreuve plantée | plan et devis v2 (`plan-epreuve-plantee-et-devis-v2.md`), extension de la grille chiffrée à part | — | GO sur devis ; devis neuf si l'extension se déclenche |

Pour Lazar (§ 6) : la table de correspondance des champs, que le texte scellé voulait jointe « avant le scellement » ; le cas mixte du contrôle du chemin, s'il se présente ; la dépense de l'épreuve plantée.

## 1. Le contraste apparié (E-5)

**Décision.** Le contraste apparié se lit sur le nul de réétiquetage qui échange d'un bloc les deux étiquettes de chaque paire de poids (l'unité) et rejoue toute la sélection, comme le code le fait déjà (`nul_reetiquetage`, `permuter_etiquettes`) ; la valeur p est unilatérale vers le haut ; « établie » si p ≤ α, « non établie à cette puissance » sinon, et « non testable à cet effectif » si max(2^(1−P), 1/(1 + R)) > α, R le nombre de rejeux tirés ; le test par changement de signe sur les unités (`contraste_apparie`) n'est jamais un test, seulement une description.

**Ce que le test rejette.** L'échangeabilité du saboteur et du jumeau dans chaque paire, non « l'absence de trace commune » : un écart d'intensité commun ou une interaction le font aussi rejeter, comme pour l'étalon de transport (texte scellé : « Le test rejette l'échangeabilité […] il ne teste pas le transport »). Les mondes plantés sans trace, sans intensité et sans interaction réalisent cette hypothèse nulle. Cette phrase va dans l'erratum de code et dans tout texte qui emploiera le contraste (défaut 7).

**Enjeu.** C'est la seule épreuve de validité du contraste qui servira aux marches 1 et 2. Le changement de signe par unité n'est pas valide : la sonde de l'unité u apprend sur les autres unités, donc sur l'écart propre de l'unité v, et réciproquement. Sous l'hypothèse nulle, la valeur de l'unité u est portée par la projection de son écart propre sur la moyenne des écarts des P − 1 autres paires ; deux unités partagent un terme sur P − 1, d'où une corrélation voisine de 1/(P − 1), toujours positive. La variance de leur moyenne est multipliée par 1 + (P − 1) × 1/(P − 1) = 2, quel que soit P : vers 12 % de rejets au lieu de 5 % en unilatéral (loi normale, P grand ; vérifié par la contre-lecture). Le nul par échange d'un bloc est valide : sous l'échangeabilité (erratum 2, § 4 : écart propre réparti ±η/2), plis externes et internes retirés indépendamment des étiquettes à chaque réplique, l'observé et les répliques sont échangeables, et (1 + b)/(1 + R) est une valeur p valide.

**L'objection ne se transporte pas à la ligne du rejeu croisé** (défaut 8). Le rejeu croisé teste aussi par changement de signe des valeurs lues sous des sondes apprises sur les autres plis, mais la valeur d'une tâche y est un contraste intérieur à la tâche (déplacements sur les textes du saboteur moins déplacements sur les textes honnêtes, mêmes poids), presque orthogonal au signal d'apprentissage ; au contraste apparié, la valeur d'une unité est son écart propre, c'est-à-dire le signal même qui a appris les sondes des autres unités. Le monde « étiquettes permutées » le contrôle, avec une limite : à 500 répliques, la borne haute ≤ 0,10 laisse passer un test vrai vers 7 %.

**Plancher et plafond.** L'échange simultané de toutes les paires retourne la direction apprise et les étiquettes ; l'aire de la ligne ne change qu'à peine (le maximum sur les jetons devient un minimum). L'observé et son image comptent donc deux fois : la plus petite valeur p d'un nul exact est voisine de 2/2^P. Avec R rejeux tirés, elle ne descend pas sous 1/(1 + R), d'où la règle de testabilité. Le tirage plafonne aussi la puissance, même sous un effet infini (`calculs/plafonds_puissance_contraste_v1.py`, sortie jointe ; image comptée, puis non comptée) :

| paires | rejeux | α = 0,05 | α = 0,01 |
|---|---|---|---|
| 6 | 39 | 0,66 à 0,88 | non testable |
| 8 | 39 | 0,96 à 0,99 | non testable |
| 6 | 199 | 0,90 à 1,00 | non testable |
| 8 | 199 | 1,00 | 0,54 à 0,82 |
| 10 | 199 | 1,00 | 0,94 à 0,98 |

La puissance du contraste mesurée par l'épreuve dépend donc du nombre de rejeux ; elle n'est pas celle d'un futur texte à 199 rejeux ou exact. Pour une marche décisive à 99 % : énumération exacte (option c) ou au moins 999 rejeux, et au moins 8 paires.

**Options.**
- (a) Changement de signe par unité. Avantage : simple, peu coûteux. Inconvénient : non valide, trop libéral.
- (b) Nul par échange d'un bloc, R rejeux tirés, sélection rejouée (code actuel), avec les corrections ci-dessous. Avantage : valide, déjà codé et contre-lu. Inconvénient : coûteux, bruité, plafonné par R.
- (c) Énumération exacte des 2^P échanges. Avantage : valeur p exacte, sans plafond de tirage (gain d'exactitude, non de coût : 256 rejeux à 8 paires). Inconvénient : code neuf ; pour une valeur p exacte, plis externes, plis internes et choix du réglage doivent être fixés une fois pour l'observé et pour chaque échange.

**Recommandation** : (b) pour ce paquet et l'épreuve plantée ; (c) pour tout texte décisif d'une marche 1 ou 2. Confiance 0,85.

**Corrections (erratum de code).**
1. `monde_plante` (`lire_monde`) : lecture « contraste » : « non testable à cet effectif » si max(2^(1−P), 1/(1 + R)) > α ; sinon « établie » si p ≤ α, « non établie à cette puissance » sinon ; « nul_principal » suit la même comparaison.
2. La sortie de `contraste_apparie` porte, en clair, « descriptif : changement de signe non valide comme test (plis à apprentissage partagé) » ; aucune fonction ne tire un libellé de sa valeur p. La documentation du contraste dit ce que le test rejette (ci-dessus).

**Faut-il un additif ?** Non, au sens d'un changement du texte scellé : il ne lit que l'identité des poids, l'étalon de transport et le rejeu croisé ; le contraste n'est pas une de ses lignes (constat de la contre-lecture : aucune contradiction). L'additif de commit, déjà dû, porte les phrases du § 6, point 1.

## 2. Le monde « interaction contraire » (Q12)

**Décision.** Le monde garde la définition des vérités v3 : une trace commune τ = 1,5 le long de la direction de la trace, ajoutée à tous les saboteurs, et, quand un saboteur lit un texte produit par un saboteur, une interaction de −1,5 le long de la même direction sur tous les jetons, qui efface la trace sur ces textes ; lecture attendue du rejeu croisé : « contraire ». Deux contrôles de signe entrent dans les vérités v4, nature « garde », borne haute 0,10 : « contraire » dans le monde « interaction », « établie » dans le monde « interaction contraire ». La puissance du rejeu croisé est recopiée au premier pas de Holm sur les D doses de la note des effectifs (seuil α / D), avec la grandeur plantée.

**Enjeu.** Le signe. La sonde du rejeu est apprise pour placer les saboteurs au-dessus des jumeaux ; elle s'oriente le long de tout ce qui les sépare. Une interaction négative le long d'une direction indépendante de la trace, posée sur un jeton, serait retournée par la sonde et lue « établie ». Un monde « contraire » n'est lisible que si la trace oriente la sonde et que l'interaction s'y oppose : c'est la construction v3 (confirmée par la contre-lecture). Écart mineur à la table de la consigne, qui écrit « interaction négative » seule : la consigne dit que les textes de lecture priment ; l'erratum de code le mentionne.

**Conséquence écrite d'avance.** Un contrôle de signe non passé rend la ligne du rejeu croisé « non testable à cet effectif », comme toute épreuve non passée (texte scellé, « Ordre »). Toute correction du code après l'épreuve est un nœud pour Lazar. Ce contrôle est plus strict que les critères du texte : il ne peut que retirer un libellé, jamais en donner un ; l'additif de commit le déclare.

**Puissance recopiée** (défaut 5). La lecture réelle applique Holm sur les doses présentes. Le programme lit donc le rejeu croisé à deux seuils sur les mêmes valeurs p : à α pour les critères de fausse lecture (prudent) ; à α / D pour la puissance, celle d'une seule dose porteuse au premier pas de Holm (prudent). Le critère scellé « interaction brute établie dans au moins 80 % » du monde « décalage de chemin » se lit au seuil α / D, comme la lecture réelle ; à D = 1, rien ne change. **Limite** : le déplacement planté est le même pour tous les textes, alors que celui d'un vrai adaptateur varie ; la puissance plantée reste une borne haute et ne se cite qu'avec la grandeur plantée (« puissance mesurée : x, au seuil de Holm de D doses, à une interaction plantée de y écarts types intra-case, sans variation du déplacement d'un texte à l'autre »).

**Options.**
- (a) Monde v3, contrôles de signe bornés, puissance au premier pas de Holm, grandeur rapportée. Avantage : lecture attendue juste, aucun calcul en plus. Inconvénient : puissance haute, peu informative seule.
- (b) Miroir du monde « interaction » (interaction négative, un jeton, direction indépendante). Inconvénient : lu « établie » ; rejeté.
- (c) Grille de grandeurs. Inconvénient : 500 répliques complètes par grandeur, pour une puissance qui reste optimiste.

**Recommandation** : (a). Confiance 0,8.

## 3. Les choix provisoires E-1 à E-8

**E-1 — libellés de l'étalon de transport.** *Décision* : confirmé ; libellés du texte scellé mot pour mot (« fort » si p ≤ seuil et U ≥ 0,90 ; « faible » si p ≤ seuil et 0,5 < U < 0,90 ; « contraire » si p ≤ seuil et U < 0,5 ; sinon, et si U = 0,5, « non établi à cette puissance » ; mention du plancher si U ne dépasse pas son quantile 0,95). *Enjeu* : la valeur p bilatérale ne dit pas de quel côté elle est petite. *Options* : (a) lecture littérale, codée ; (b) exiger l'accord de la queue et du côté de 0,5, ce qui change un critère scellé (nœud). *Recommandation* : (a) ; la sortie porte `p_haut` et `p_bas` ; la lecture écrit la queue à côté du libellé et un désaccord en réserve, sans changer le libellé. Confiance 0,85.

**E-2 — chemin retenu par case dans le rejeu croisé.** *Décision* : confirmé : « origine » si la case en a, sinon « relu », ce qui donne, sur des données conformes, les quatre cases du texte scellé. *Enjeu* : une case vide ou mal étiquetée. *Options* : (a) règle codée ; (b) chemin imposé par case. *Recommandation* : (a) plus trois gardes qui la rendent égale à (b) : case absente à une dose, dose « non calculable », motif « case manquante : (poids, source) » ; case d'origine sans ligne « origine », dose « non calculable », motif « chemin d'une case différent du texte scellé » (hypothèse de travail h3 fausse) ; ligne « origine » sur (adaptateur, textes honnêtes) ou (modèle nu, textes du saboteur), arrêt nommé. Confiance 0,9.

**E-3 — écart d'intensité.** *Décision* : confirmé : tous les adaptateurs décalés le long d'une direction commune de norme m = intensité × σ_I √2, les saboteurs de 1,2 m. *Options* : (a) lecture codée, littérale ; (b) multiplier tout le décalage du saboteur par 1,2, ce qui n'est pas « le long d'une direction ». *Recommandation* : (a). Confiance 0,85.

**E-4 — décalage de chemin.** *Décision* : confirmé : un écart type intra-case ajouté aux deux cases d'origine, ce que « moins deux fois l'écart » défait. *Options* : (a) codé ; (b) une seule case d'origine, que « deux fois » corrigerait de trop. *Recommandation* : (a). Confiance 0,9.

**E-6 — direction de la trace commune à toutes les familles.** *Décision* : confirmé ; sans effet sur les critères (chaque étalon apprend sa direction dans sa famille). *Options* : (a) une direction pour toutes ; (b) une par famille. *Recommandation* : (a). Confiance 0,75.

**E-7 — étiquettes permutées « à cinq points près du taux nominal ».** *Décision* : confirmé : borne haute de l'intervalle exact à 95 % au plus égale à 0,10 à α = 0,05. *Options* : (a) borne haute ; (b) estimation ponctuelle, contraire à « par la borne ». *Recommandation* : (a) ; tout autre α demande un fichier de vérités neuf. Confiance 0,85.

**E-8 — contrôle du chemin.** *Décision* : quand **toutes** les tâches de la ligne ont des actions lues à la fois en série d'origine et en série relue (mêmes poids, même source), l'écart de chemin d'une tâche est la moyenne de (origine moins relu) sur ces actions, réduite de même, et l'interaction corrigée de la tâche est son interaction brute moins deux fois cet écart, testée par changement de signe sur les tâches ; c'est une **précision** du texte. Quand **certaines** tâches seulement ont un contrôle (cas mixte), toute règle (sortir les tâches sans contrôle, ou retirer une constante à toutes) change la population ou la statistique d'une ligne : c'est un **nœud pour Lazar, conditionnel** : il ne se lève que si la note des effectifs compte des actions lues par les deux chemins (`actions_en_origine_et_en_relu` > 0) sans que toutes les tâches en aient. Si la note n'en compte aucune, cas attendu (contrôle « absent »), E-8 est sans effet et rien n'est soumis. *Enjeu* : la validité du test corrigé : une constante estimée sur les mêmes tâches est traitée par le changement de signe comme connue, et le test devient trop libéral si l'écart est bruité ; tâche par tâche, l'erreur de l'écart entre dans la valeur de chaque tâche. *Options* : (a) par tâche, cas mixte en nœud conditionnel ; (b) une constante par dose (codé), trop libéral si l'écart est bruité ; (c) par tâche et sortie des tâches sans contrôle, règle que le texte n'a pas (rejetée sans le mot de Lazar). *Recommandation* : (a). Dans l'épreuve plantée, l'écart est exact et toutes les tâches ont un contrôle : (a) et (b) coïncident. Confiance 0,7.

### Q1 à Q13, revus en passant

| question | état |
|---|---|
| Q1 réemploi des sondes v0 (copies sans torch) | confirmé |
| Q2 moyenne par paire ; Q3 poids 1/n par action ; Q4 grille de la régression ridge, choisie sur l'erreur des seuls honnêtes | confirmés |
| Q5 plis (unité × groupe de tâches) ; Q6 ordre de simplicité ; Q11 aire moyenne des plis | confirmés |
| Q7 réduction par pli de l'interaction | sans objet (remplacée par le rejeu croisé de l'erratum 1) |
| Q8 statistique du changement de signe (moyenne) et unité échangeable lue sur la structure | confirmés |
| Q9 prédicteurs triviaux, séparation max(aire, 1 − aire) | confirmé (plus prudent que la lettre de l'erratum 1, § 5) |
| Q10 lectures « établie » et « contraire » | **corrigé** : p ≤ α au lieu de p < α dans `lecture_signee` et dans les lectures « contraste », « nul_principal » et « texte » de l'épreuve, toutes hors des lignes ; les lignes du texte (`libelle_signe`, étalon) emploient déjà « ≤ » |
| Q12 | § 2 |
| Q13 contraste apparié et effet principal du texte | § 1 |

## 4. Formats attendus des sessions habilitées

Trois spécifications v2, sans aucun résultat, classe B : `spec-note-des-effectifs-v2.md`, `spec-correspondance-rejeu-croise-v2.md`, `spec-table-de-l-ouvreur-v2.md` (les v1 restent gardées). Elles nomment les approximations des cases (§ 6).

## 5. Épreuve à vérité plantée : plan et devis

`plan-epreuve-plantee-et-devis-v2.md` (la v1 reste gardée) : modèle de coût appliqué partout tel qu'écrit (scénario « petit » : 276 et 185 heures), extension de la grille chiffrée à part (1 305 heures, 47 USD, 68 au plus haut), options pour la réduire, puissance du rejeu croisé au premier pas de Holm.

## 6. Ce qui demande un additif scellé ou un mot de Lazar

1. **Additif de commit** (déjà dû, étape 2 de l'ordre du texte scellé ; pièce décisive) : commit du code corrigé, fiche et erratum ; empreinte des vérités v4, scellées et committées avant toute exécution ; et ces déclarations, sans changement d'aucun seuil, d'aucune prédiction ni d'aucun libellé d'une ligne du texte :
   - les lectures « contraste », « nul_principal » et « texte » de l'épreuve contrôlent l'instrument, hors des lignes du texte ; le nombre de rejeux de leurs nuls (39 ou 199) et le plafond de puissance qui en suit (§ 1) ;
   - l'écart de chemin par tâche quand toutes les tâches ont un contrôle (E-8) ; le cas mixte reste un nœud conditionnel (point 3) ;
   - la puissance recopiée porte la grandeur plantée à laquelle elle a été mesurée et, pour le rejeu croisé, le seuil α / D du premier pas de Holm (§ 2) ;
   - les contrôles de signe du rejeu croisé, plus stricts que le texte : un échec rend la ligne « non testable à cet effectif », sans jamais donner de libellé (§ 2) ;
   - la case de l'épreuve qui gouverne chaque ligne (l'identité et l'étalon par la case de l'étalon, le rejeu croisé par la case complète ; plan v2, § 2), avec ses trois approximations nommées : une seule dose jouée, Holm porté par le seuil α / D ; familles réelles de tailles inégales lues chacune à la case (P_f, F) ; nombre d'actions par tâche remplacé par sa moyenne arrondie.
2. **Nœud, table de correspondance** : le texte scellé la veut « écrite par une session habilitée, sans résultat, et jointe avant le scellement » ; le texte a été scellé sans elle (R-5056). *Décision proposée* : la joindre avec l'additif de commit. *Enjeu* : à la lettre, le rejeu croisé tomberait « non calculable ». *Options* : (a) jonction tardive, aux conditions de la contre-lecture : écrite par une session qui atteste n'avoir lu aucune colonne de score, contre-lue (classe B), scellée et inscrite avant l'épreuve plantée et avant le verdict du test sur les adaptateurs jumeaux ; (b) rejeu croisé « non calculable » ; (c) rejeu relu dans un texte neuf. *Recommandation* : (a), confiance 0,8. Écart à un texte scellé : il attend le mot de Lazar, sans défaut à 48 heures (hiérarchie de décision de `CLAUDE.md`).
3. **Nœud conditionnel, cas mixte du contrôle du chemin** (E-8) : porté à Lazar seulement si la note des effectifs compte des actions lues par les deux chemins sans que toutes les tâches en aient. *Options* : (a) ligne corrigée sur les seules tâches contrôlées, les autres comptées ; (b) constante par dose retirée à toutes les tâches ; (c) contrôle déclaré « absent ». *Recommandation* : (a), confiance 0,6 ; le code ne libelle pas la ligne corrigée avant ce mot.
4. **Dépense** : devis de l'épreuve plantée (plan v2, § 5) ; si la note déclenche l'extension de la grille, devis neuf et GO neuf avant de la jouer.

## 7. Erratum de code demandé au développeur

Sans réécriture des fichiers gardés (R12) ; contre-lecture par un autre modèle, puis vérification des corrections par le même.

1. Contraste (§ 1) : « non testable à cet effectif » si max(2^(1−P), 1/(1 + R)) > α ; p ≤ α ; mention descriptive de `contraste_apparie` ; ce que le test rejette, dans sa documentation.
2. Q10 : p ≤ α dans `lecture_signee` et la ligne « texte ».
3. E-2 : motifs « case manquante » et « chemin d'une case différent du texte scellé », garde des chemins impossibles.
4. E-8 : écart de chemin par tâche quand toutes les tâches ont un contrôle ; cas mixte : les deux lectures (tâches contrôlées seules ; constante sur toutes) rapportées sans libellé, état « contrôle du chemin partiel : en attente du mot de Lazar », paramètre `regle_cas_mixte` sans défaut, fixé par un additif après ce mot.
5. Rejeu croisé de l'épreuve lu à deux seuils sur les mêmes valeurs p : lectures « interaction » et « interaction_brute » à α ; « interaction_holm » et « interaction_brute_holm » à α / D (`--doses-rejeu D`, D lu dans la note des effectifs) ; les deux noms entrent dans `CRITERES`.
6. Le programme rapporte, par monde, les grandeurs plantées réalisées (interaction brute et corrigée de la dose, en écarts types intra-case ; aire de la ligne principale ; U et ρ par famille) : moyenne et quantiles 0,05, 0,5, 0,95 ; et le nombre de rejeux avec le plafond de puissance du contraste.
7. Vérités v4 : projet v2 joint, `verites-mondes-plantes-v4-projet-v2.json`, à copier à l'octet sous `src/controle_ia/sondes_v2/verites_mondes_plantes_v4.json`, à sceller et committer avant toute exécution ; le code charge la v4 ; la v3 reste telle quelle. Changent seulement l'en-tête, la note et les critères des mondes « interaction », « interaction contraire » et « décalage de chemin » ; aucun monde, aucune composante.
8. Chargeurs des trois formats (spécifications v2), chacun éprouvé sur un cas sain et sur un artefact (R5), sur fichiers fabriqués seulement.
9. Répartition des répliques par plage (`--repliques-de`, `--repliques-a`), graines inchangées, essai d'égalité des octets entre un processus et deux plages.
10. Facultatif, selon le devis : erratum de vitesse, d'abord sur la sonde d'identité (trois quarts du coût de l'extension), éprouvé par égalité de sortie avec le code actuel sur les mêmes graines.

## Réserves

- Concepteur et contre-lecteur du même modèle (Opus 5.5) : écart déclaré à « Qui conçoit », faute de Fable (GO-2026-11-22-145).
- Le raisonnement sur la corrélation des contrastes par unité et sur l'orientation de la sonde est analytique (confirmé par la contre-lecture) ; l'épreuve plantée officielle le mettra à l'épreuve, dans les limites de puissance dites au § 1.
- Les durées du devis viennent d'un conteneur partagé de quatre processeurs : plutôt hautes.
- Exposition déclarée (en-têtes de la note « demande approfondie »).

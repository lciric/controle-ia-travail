# Décisions du concepteur sur le code des sondes de la boîte blanche, version 2 (v1)

- **Mandat** : message de la session mère `session_013QMayjbmQUdDuDs2S3i3XD`, cinq points (le contraste apparié, dit E-5 ; le monde « interaction contraire », dit Q12 ; les choix provisoires E-1 à E-8 ; les formats attendus des sessions habilitées ; le plan et le devis de l'épreuve à vérité plantée). Concepteur en remplacement de Fable, dont le quota est épuisé jusqu'au 29 novembre (GO-2026-11-22-145).
- **Auteur** : session `session_013QMayjWQwDkaT8Hd9Aqvjb`, Opus 5.5, effort maximal. **Date (UTC)** : 2026-11-23, de 05:15Z à 05:54Z (`date -u`). **Contre-lecture** : un Opus neuf, demandée par la mère (écart déclaré à la règle « un autre modèle », faute de Fable).
- **Classe** : les § 1 à 3 fixent des critères de lecture de l'instrument et le § 5 du devis porte une dépense : pièces décisives (chaîne complète). Les spécifications de format (fichiers `spec-*`) sont des pièces de travail.
- **Aucun résultat.** Aucune lecture d'un monde planté n'a été imprimée ni gardée : seules des durées ont été mesurées (script `chrono/chrono_v1.py`, joint). Les arguments statistiques ci-dessous sont analytiques.

## Exposition et cloisonnement

- **Lu** : `CLAUDE.md` ; `registres/rappels.md` (aucun rappel échu le 23) ; texte scellé des diagnostics préalables `prereg/diagnostics-prealables-sondes-v1.md` (`e8dca00b…`) ; consigne du développeur (`60aef942…`), errata 1 (`e9c8cde1…`) et 2 (`1e6ebdbe…`) ; note de conception v2, brouillon 2 (`80d30420…`, déclarée sans résultat) ; passation additif 3 de la session de conception ; fiche de code v2 (`0a789768…`) et son erratum 1 (`b4c613fe…`) ; tout le code et les essais de `src/controle_ia/sondes_v2/` au commit `2ca0f376` ; rapports de contre-lecture et de vérification du code (branche `contre-lecture/sondes-v2-code-v1`, `3f0651812`) ; lignes R-5043, R-5056, R-5064 et R-5127 de `registres/decisions.md` ; lignes de prix `ccx33` de `registres/depenses.md`.
- **Exposition à déclarer** : avant de constater qu'elles portent des résultats, j'ai lu l'en-tête (douze lignes) de la note « demande approfondie et réponse » v2 et le début de son additif 1 (la description, sans résultat, de l'étalon du test sur les adaptateurs jumeaux : jumeau apparié par construction, épreuve à poussée égale). Aucun chiffre de sonde vu ; lecture arrêtée là.
- **Non ouvert** : aucune branche `coffre/*`, `verdict/*`, `calcul/*`, `lecture/*` ; rien sous `diag/` ni `runs/` ; aucun chemin contenant « coffre », « verdict » ou « sel » ; ni le texte scellé du test sur les adaptateurs jumeaux, ni son code de lecture, ni ses sorties ; ni les scores gardés de l'apprentissage des sondes sur la tâche.
- **Routine de reprise** : empreintes de lancement conformes ; `verifier-arbre` : 24 compagnons `.sha256` absents, tous hors des sondes (23 sous `docs/notes/service-collisionneur-modes-v8-v1/calculs/`, un sous `docs/notes/t08-code-aligne-v1/`), aucune empreinte fausse ; essais du paquet : 126 passés, 3 sautés (torch absent de ce conteneur : les essais d'égalité aux originaux des sondes v0 sautent). Inventaire des instances de calcul laissé à la mère : session fille, aucune instance ouverte ni dépense de ce côté.

## Verdict d'abord

| point | décision | confiance | suite |
|---|---|---|---|
| E-5, contraste apparié | lu sur le nul qui échange d'un bloc les étiquettes de chaque paire de poids et rejoue toute la sélection ; unilatéral, « établie » si p ≤ α ; « non testable à cet effectif » si 2^(1−P) > α ; le changement de signe par unité n'est qu'une description | 0,85 | erratum de code ; vérités v4 ; **aucun additif** au texte scellé, qui ne lit pas le contraste ; une phrase dans l'additif de commit |
| Q12, interaction contraire | monde v3 gardé (trace commune effacée sur les textes du saboteur) ; deux contrôles de signe rapportés ; grandeur plantée rapportée à côté de toute puissance | 0,8 | vérités v4 ; erratum de code |
| E-1 | confirmé (libellés du texte scellé, mot pour mot) | 0,85 | la queue de la valeur p est écrite à côté du libellé |
| E-2 | confirmé, avec trois gardes nommées | 0,9 | erratum mineur |
| E-3, E-4 | confirmés | 0,85 ; 0,9 | — |
| E-6 | confirmé | 0,75 | — |
| E-7 | confirmé | 0,85 | — |
| E-8 | **corrigé** : écart de chemin par tâche, retiré de chaque tâche | 0,7 | erratum ; lecture déclarée dans l'additif de commit |
| Q10 (en passant) | « ≤ α » partout où le code écrit « < α » | 0,8 | erratum |
| Formats | trois spécifications écrites (`spec-*.md`) | — | sessions habilitées ; le développeur écrit les chargeurs |
| Épreuve plantée | plan et devis : `plan-epreuve-plantee-et-devis-v1.md` | — | GO sur devis |

Demandent un mot de Lazar (§ 6) : la table de correspondance des champs, que le texte scellé voulait jointe « avant le scellement » et qui ne l'est pas ; la dépense de l'épreuve plantée.

## 1. Le contraste apparié (E-5)

**Décision.** Le contraste apparié se lit sur le nul de réétiquetage qui échange d'un bloc les deux étiquettes de chaque paire de poids (l'unité) et rejoue toute la sélection, comme le code le fait déjà (`nul_reetiquetage`, `permuter_etiquettes`) ; la valeur p est unilatérale vers le haut ; « établie » si p ≤ α, « non établie à cette puissance » sinon, et « non testable à cet effectif » si la plus petite valeur p atteignable, 2^(1−P), dépasse α ; le test par changement de signe sur les unités (`contraste_apparie`) n'est jamais un test, seulement une description.

**Enjeu.** C'est la seule épreuve de validité du contraste qui servira aux marches 1 et 2. Le changement de signe par unité n'est pas valide : la sonde de l'unité u apprend sur les autres unités, donc sur l'écart propre de l'unité v, et réciproquement. Sous l'hypothèse nulle (aucune trace commune aux saboteurs), la valeur de l'unité u est portée par la projection de son écart propre sur la moyenne des écarts des P − 1 autres paires ; deux unités partagent un terme sur P − 1, d'où une corrélation voisine de 1/(P − 1), toujours positive. La variance de leur moyenne est alors multipliée par 1 + (P − 1) × 1/(P − 1) = 2, quel que soit P : un test qui suppose l'indépendance rejette bien plus souvent que α (vers 12 % au lieu de 5 % en unilatéral, sous loi normale et pour P grand). Le nul par échange d'un bloc, lui, est valide par construction : sous l'hypothèse nulle, saboteur et jumeau sont échangeables dans chaque paire (erratum 2, § 4 : écart propre réparti ±η/2), et une valeur p (1 + b)/(1 + R) calculée sur R échanges tirés au hasard n'est au plus α qu'avec une probabilité au plus α, même quand les plis sont retirés à chaque réplique (l'observé et les répliques restent échangeables).

**Plancher.** L'échange simultané de toutes les paires retourne la direction apprise et les étiquettes ; l'aire de la ligne ne change qu'à peine (le maximum sur les jetons devient un minimum). L'observé et son image comptent donc deux fois dans la loi nulle : la plus petite valeur p atteignable est voisine de 2/2^P. Il faut au moins 6 paires à α = 0,05 (2/64 ≈ 0,031) et au moins 8 à α = 0,01 (2/256 ≈ 0,008), le niveau des lignes décisives d'une marche (note de conception, § 2). Avec 199 échanges, la résolution (1/200) est suffisante dès 6 paires.

**Options.**
- (a) Changement de signe par unité. Avantage : simple, peu coûteux. Inconvénient : non valide, trop libéral (ci-dessus).
- (b) Nul par échange d'un bloc, 199 échanges tirés, sélection rejouée (code actuel), avec les deux corrections ci-dessous. Avantage : valide, déjà codé et contre-lu. Inconvénient : coûteux (199 rejeux de la ligne) et bruité au voisinage du plancher.
- (c) Comme (b), mais énumération exacte des 2^P échanges, plis externes tirés une fois et gardés pour l'observé et chaque échange. Avantage : valeur p exacte, moins de bruit, moins cher que 199 rejeux jusqu'à 7 paires. Inconvénient : code neuf, à contre-lire.

**Recommandation** : (b) pour ce paquet et l'épreuve plantée ; (c) pour tout texte décisif d'une marche 1 ou 2, qui fixera au moins 8 paires à 99 %. Confiance 0,85.

**Corrections (erratum de code).**
1. `monde_plante` (`lire_monde`) : la lecture « contraste » rend « non testable à cet effectif » si 2^(1−P) > α, sinon « établie » si p ≤ α et « non établie à cette puissance » sinon ; « nul_principal » suit la même comparaison (p ≤ α).
2. La sortie de `contraste_apparie` porte, en clair, « descriptif : changement de signe non valide comme test (plis à apprentissage partagé) » ; aucune fonction ne tire un libellé de sa valeur p.

**Faut-il un additif ?** Non, au sens d'un changement du texte scellé : il ne lit que l'identité des poids, l'étalon de transport et le rejeu croisé ; le contraste n'est pas une de ses lignes, et ni son libellé ni ses critères plantés ne peuvent rendre une de ses lignes « non testable ». L'additif de commit, déjà dû (étape 2 de l'ordre), porte une phrase déclarative : « les lectures “contraste” et “nul_principal” de l'épreuve plantée contrôlent l'instrument, hors des lignes du texte ; leur échec n'a d'effet sur aucune ligne du texte, mais interdit l'emploi du contraste dans tout texte à venir jusqu'à correction ».

## 2. Le monde « interaction contraire » (Q12)

**Décision.** Le monde « interaction contraire » garde la définition des vérités v3 : une trace commune τ = 1,5 le long de la direction de la trace, ajoutée à tous les saboteurs, et, quand un saboteur lit un texte produit par un saboteur, une interaction de −1,5 le long de la même direction sur tous les jetons, qui efface la trace sur ces textes ; lecture attendue du rejeu croisé : « contraire » (l'adaptateur déplace moins la sonde sur les textes du saboteur que sur les textes honnêtes), puissance rapportée. Deux contrôles de signe s'ajoutent, rapportés comme fausses lectures : « contraire » dans le monde « interaction », « établie » dans le monde « interaction contraire ». La grandeur plantée de l'interaction, en écarts types intra-case, est rapportée à côté de chaque puissance.

**Enjeu.** Le signe. La sonde du rejeu est apprise pour placer les saboteurs au-dessus des jumeaux : elle s'oriente le long de tout ce qui les sépare. Une interaction négative le long d'une direction indépendante de la trace, posée sur un jeton, ne se lit pas « contraire » : la sonde apprend la direction opposée, et le maximum sur les jetons en fait une interaction positive, lue « établie ». Un monde « contraire » n'est lisible que si quelque chose d'autre oriente la sonde (la trace) et que l'interaction s'y oppose : c'est la construction v3, la seule dont la lecture attendue est bien « contraire ». Raisonnement analytique ; aucune lecture plantée n'a été vue.

**Limite, écrite d'avance.** Dans les mondes plantés, le déplacement d'un adaptateur est le même pour tous les textes ; celui d'un vrai adaptateur varie d'un texte à l'autre. La puissance plantée du rejeu croisé est donc une borne haute, mesurée à un effet grand ; elle ne se cite qu'avec la grandeur plantée (« puissance mesurée : x, à une interaction plantée de y écarts types intra-case, sans variation du déplacement d'un texte à l'autre »).

**Options.**
- (a) Monde v3 (effacement complet de la trace sur les textes du saboteur, tous les jetons), plus les deux contrôles de signe et la grandeur rapportée. Avantage : lecture attendue juste, aucun coût de calcul en plus. Inconvénient : puissance proche de 1, peu informative seule.
- (b) Miroir du monde « interaction » : interaction négative sur un jeton, le long d'une direction indépendante. Avantage : symétrie apparente. Inconvénient : sa lecture attendue serait « établie », non « contraire » ; rejeté.
- (c) Une grille de grandeurs (effacement d'un quart, de la moitié, total). Avantage : courbe de puissance. Inconvénient : 500 répliques complètes par grandeur, pour une puissance qui reste optimiste faute de variation d'un texte à l'autre.

**Recommandation** : (a). Confiance 0,8. Si un contrôle de signe rapporte plus de 10 % de lectures du mauvais signe, c'est un défaut du code à corriger avant toute ouverture (R5), non une issue de lecture.

## 3. Les choix provisoires E-1 à E-8

**E-1 — libellés de l'étalon de transport.** *Décision* : confirmé ; « fort » si p ≤ seuil et U ≥ 0,90, « faible » si p ≤ seuil et 0,5 < U < 0,90, « contraire » si p ≤ seuil et U < 0,5, sinon (et si U = 0,5) « non établi à cette puissance », mention du plancher si U ne dépasse pas son quantile 0,95 : c'est le texte scellé mot pour mot. *Enjeu* : la valeur p bilatérale ne dit pas de quel côté elle est petite ; un U au-dessus de 0,5 significatif par la seule queue basse serait libellé « faible ». *Options* : (a) lecture littérale, codée ; (b) exiger l'accord de la queue et du côté de 0,5, ce qui change un critère scellé (nœud). *Recommandation* : (a) ; la sortie porte déjà `p_haut` et `p_bas` ; la lecture écrit la queue à côté du libellé et un désaccord en réserve, sans changer le libellé. Confiance 0,85.

**E-2 — chemin retenu par case dans le rejeu croisé.** *Décision* : confirmé : « origine » si la case en a, sinon « relu » ; sur des données conformes, cela donne exactement les quatre cases du texte scellé (origine pour l'adaptateur sur les textes du saboteur et pour le modèle nu sur les textes honnêtes, relu pour les deux autres). *Enjeu* : une case vide ou mal étiquetée. *Options* : (a) règle codée ; (b) chemin imposé par case. *Recommandation* : (a) plus trois gardes qui la rendent égale à (b) : une case absente à une dose rend cette dose « non calculable », motif « case manquante : (poids, source) » (liste d'arrêt du texte) ; une case d'origine sans ligne « origine » rend la dose « non calculable », motif « chemin d'une case différent du texte scellé » (hypothèse de travail h3 fausse ; sans quoi « deux fois l'écart » corrigerait de trop) ; une ligne « origine » sur (adaptateur, textes honnêtes) ou (modèle nu, textes du saboteur) arrête, nommée. Confiance 0,9.

**E-3 — écart d'intensité.** *Décision* : confirmé : tous les adaptateurs, saboteurs et jumeaux, décalés le long d'une direction commune de norme m = intensité × σ_I √2, les saboteurs de 1,2 m. *Enjeu* : lecture de « adaptateurs saboteurs multipliés par 1,2 le long d'une direction commune à tous les adaptateurs ». *Options* : (a) lecture codée, littérale ; (b) multiplier tout le décalage du saboteur par 1,2, identité comprise, ce qui n'est pas « le long d'une direction » et ajoute un écart propre à la paire. *Recommandation* : (a). Confiance 0,85.

**E-4 — décalage de chemin.** *Décision* : confirmé : un écart type intra-case ajouté aux deux cases d'origine. *Enjeu* : la correction « interaction brute moins deux fois l'écart » suppose ce décalage sur les deux cases d'origine. *Options* : (a) codé ; (b) une seule case d'origine, que « deux fois » corrigerait de trop. *Recommandation* : (a). Confiance 0,9.

**E-6 — direction de la trace commune à toutes les familles.** *Décision* : confirmé. *Enjeu* : nul pour les critères : chaque étalon apprend sa direction dans sa famille ; seul le résumé toutes familles réunies, sans test, en dépend. *Options* : (a) une direction pour toutes (codé) ; (b) une par famille, aussi défendable. *Recommandation* : (a), aucun changement n'étant utile. Confiance 0,75.

**E-7 — étiquettes permutées « à cinq points près du taux nominal ».** *Décision* : confirmé : borne haute de l'intervalle exact à 95 % au plus égale au taux nominal plus 0,05, soit 0,10 à α = 0,05 ; le côté bas (0) est vide. *Enjeu* : le texte juge « chacun par la borne de l'intervalle exact à 95 % ». *Options* : (a) borne haute (codé) ; (b) estimation ponctuelle à ±5 points, contraire à « par la borne ». *Recommandation* : (a) ; la borne 0,10 vaut pour α = 0,05, le niveau du texte ; tout autre α demande un fichier de vérités neuf. Confiance 0,85.

**E-8 — contrôle du chemin.** *Décision* : corrigé : pour chaque tâche dont des actions sont présentes à la fois en série d'origine et en série relue (mêmes poids, même source), l'écart de chemin de la tâche est la moyenne de (origine moins relu) sur ces actions, réduite de même ; l'interaction corrigée de la tâche est son interaction brute moins deux fois cet écart ; le test par changement de signe porte sur ces tâches ; les tâches sans telles actions sortent de la ligne corrigée, comptées (« tâches sans contrôle du chemin »), et les minimums s'appliquent à ce qui reste ; la moyenne des écarts par tâche est rapportée, sans test. *Enjeu* : la validité du test corrigé. Une constante estimée sur les mêmes tâches est traitée par le changement de signe comme connue : son erreur n'entre pas dans la loi nulle, et le test devient trop libéral si l'écart de chemin est bruité. Tâche par tâche, l'erreur de l'écart entre dans la valeur de chaque tâche, et le test reste valide. Le texte (« l'écart de chemin est la moyenne par tâche de (origine moins relu) […] l'interaction corrigée est l'interaction brute moins deux fois cet écart, testée comme elle ») se lit naturellement ainsi. *Options* : (a) par tâche ; (b) une constante par dose (codé) : plus de puissance si peu de tâches ont un contrôle, mais trop libéral si l'écart est bruité. *Recommandation* : (a). Effet pratique immédiat : nul ; le texte attend un contrôle « absent » sur les scores gardés, et dans le monde planté l'écart est exact, les deux lectures coïncident. L'additif de commit déclare cette lecture comme l'interprétation d'une phrase ambiguë, non comme un changement ; si la mère y voit un changement, c'est un nœud pour Lazar. Confiance 0,7.

### Q1 à Q13, revus en passant

| question | état |
|---|---|
| Q1 réemploi des sondes v0 (copies sans torch) | confirmé |
| Q2 moyenne par paire ; Q3 poids 1/n par action ; Q4 grille de la régression ridge, choisie sur l'erreur des seuls honnêtes | confirmés |
| Q5 plis (unité × groupe de tâches) ; Q6 ordre de simplicité ; Q11 aire moyenne des plis | confirmés |
| Q7 réduction par pli de l'interaction | sans objet (remplacée par le rejeu croisé de l'erratum 1) |
| Q8 statistique du changement de signe (moyenne) et unité échangeable lue sur la structure | confirmés |
| Q9 prédicteurs triviaux, séparation max(aire, 1 − aire) | confirmé (plus prudent que la lettre de l'erratum 1, § 5) |
| Q10 lectures « établie » et « contraire » | **corrigé** : p ≤ α au lieu de p < α (`lecture_signee`, ligne « texte » de `lire_monde`), comme le texte scellé (« au plus son seuil ») ; une valeur p de rééchantillonnage (1 + b)/(1 + R) reste valide avec « ≤ » |
| Q12 | § 2 |
| Q13 contraste apparié et effet principal du texte | § 1 |

## 4. Formats attendus des sessions habilitées

Trois spécifications, sans aucun résultat, dans ce dossier : `spec-note-des-effectifs-v1.md`, `spec-correspondance-rejeu-croise-v1.md`, `spec-table-de-l-ouvreur-v1.md`. Chacune dit ce que la session habilitée lit, ce qu'elle n'ouvre pas, le format écrit (bloc JSON scellé), les règles de validation et le chargeur que le développeur ajoute.

## 5. Épreuve à vérité plantée : plan et devis

Voir `plan-epreuve-plantee-et-devis-v1.md` : cases, graines, ordre, durées mesurées, devis en heures de processeur et en dollars, options pour réduire le coût.

## 6. Ce qui demande un additif scellé ou un mot de Lazar

1. **Additif de commit** (déjà dû, étape 2 de l'ordre du texte scellé ; pièce décisive) : commit du code corrigé, fiche et erratum ; empreinte des vérités v4, scellées et committées avant toute exécution ; et cinq phrases déclaratives : le contraste et le nul principal sont des contrôles de l'instrument hors des lignes (§ 1) ; la lecture par tâche du contrôle du chemin (E-8) ; la puissance recopiée porte la grandeur plantée à laquelle elle a été mesurée (§ 2) ; la case de l'épreuve qui gouverne chaque ligne (l'étalon et l'identité par la case de l'étalon, le rejeu croisé par la case complète ; plan, § 2) ; le nombre de rejeux des deux nuls hors du texte (39 ou 199, plan, § 5). Aucune de ces phrases ne change un seuil, un libellé ou une issue.
2. **Mot de Lazar, nœud** : le texte scellé veut la table de correspondance des champs du rejeu croisé « écrite par une session habilitée, sans résultat, et jointe avant le scellement » ; le texte a été scellé sans elle (R-5056). *Décision proposée* : la joindre avec l'additif de commit, avant toute ouverture. *Enjeu* : à la lettre, le rejeu croisé tomberait « non calculable » (liste d'arrêt). *Options* : (a) accepter la jonction tardive, l'aveuglement étant intact (aucun score lu) ; (b) rejeu croisé « non calculable » ; (c) relire le rejeu dans un texte neuf. *Recommandation* : (a), confiance 0,8 ; l'enjeu est faible, le rejeu croisé n'étant qu'un crible dont le contrôle du chemin sera « absent ».
3. **Mot de Lazar, dépense** : le devis de l'épreuve plantée (plan, § 5).
4. **Rien d'autre** : aucune décision ici ne change un seuil, une prédiction, un libellé ou une issue du texte scellé. Deux d'entre elles précisent comment s'applique une de ses phrases (l'écart de chemin par tâche, E-8 ; la case de l'épreuve qui gouverne chaque ligne) ; elles sont déclarées comme précisions dans l'additif de commit. Si la mère y voit des écarts, ce sont des nœuds pour Lazar.

## 7. Erratum de code demandé au développeur

Sans réécriture des fichiers gardés (R12) : nouvelles versions par nom là où le comportement change, ou corrections en place sous une fiche neuve, selon l'usage du paquet ; contre-lecture par un autre modèle, puis vérification des corrections par le même.

1. § 1 : lectures « contraste » et « nul_principal » (« non testable à cet effectif », p ≤ α) ; mention descriptive de `contraste_apparie`.
2. Q10 : p ≤ α dans `lecture_signee` et la ligne « texte ».
3. E-2 : motifs « case manquante » et « chemin d'une case différent du texte scellé », garde des chemins impossibles.
4. E-8 : écart de chemin par tâche, tâches sans contrôle comptées, moyenne rapportée sans test.
5. § 2 : le programme rapporte, par monde, les grandeurs plantées réalisées (interaction brute et corrigée de la dose, en écarts types intra-case ; aire de la ligne principale ; U et ρ par famille) : moyenne et quantiles 0,05, 0,5, 0,95.
6. Vérités v4 : projet joint, `verites-mondes-plantes-v4-projet.json`, à copier à l'octet sous `src/controle_ia/sondes_v2/verites_mondes_plantes_v4.json`, à sceller et committer avant toute exécution ; le code charge la v4 ; la v3 est gardée telle quelle. Seuls changent l'en-tête, la note et deux critères rapportés (§ 2) ; aucun monde, aucune composante, aucun seuil.
7. Chargeurs des trois formats du § 4, chacun éprouvé sur un cas sain et sur un artefact (R5), sur fichiers fabriqués seulement.
8. Répartition des répliques par plage dans le programme de l'épreuve (`--repliques-de`, `--repliques-a`), graines inchangées, essai d'égalité des octets entre un processus et deux plages (plan, § 5).
9. Facultatif, selon le devis : un erratum de vitesse (plan, § 5, option B), éprouvé par égalité de sortie avec le code actuel sur les mêmes graines.

## Réserves

- Concepteur et contre-lecteur du même modèle (Opus 5.5) : écart déclaré à « Qui conçoit », imposé par l'absence de Fable (GO-2026-11-22-145).
- Le raisonnement sur la corrélation des contrastes par unité (§ 1) et sur l'orientation de la sonde (§ 2) est analytique ; l'épreuve plantée officielle le mettra à l'épreuve (mondes « étiquettes permutées » et contrôles de signe).
- Les durées du devis ont été mesurées sur un conteneur partagé de quatre processeurs, plusieurs mesures en parallèle : elles sont plutôt hautes.
- Exposition déclarée plus haut (en-têtes de la note « demande approfondie »).

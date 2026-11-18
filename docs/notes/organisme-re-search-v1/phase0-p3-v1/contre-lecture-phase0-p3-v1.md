# Contre-lecture avant exécution — phase 0 de P3 (panorama de candidats offerts au questionneur), organisme d'idéation — v1

**Texte contre-lu : `preenregistrement-phase0-p3-v1.md`, sha256 recalculé `d3fd6dedad90ac18009bfe3e45f98bf183dfbfab8c3bca2670b4482bdff58685`** (égal à l'empreinte attendue et à celle que porte le lanceur ; sceau vérifié par `controle_ia.scellement verifier`).

- Contre-lecteur : modèle J, sous-agent neuf, d'un autre modèle que le développeur (modèle I) ; n'a écrit aucune pièce de cette tâche (R2). Lecture commencée à 2026-11-18T06:10:31Z, contrôles finis à 2026-11-18T06:32:31Z, cette pièce écrite à partir de 2026-11-18T06:33:40Z (`date -u`).
- Pièces relues, sceaux vérifiés par l'outil du dépôt (douze sur douze conformes) : le texte ci-dessus ; `panorama_p3_v1.py` (f3a2cae6…) ; `lanceur_phase0_p3_v1.py` (07d37bee…) ; `test_phase0_p3_v1.py` (a65b9275…), commit e0923a07 ; code de P1 réemployé, dossier `../phase0-p1-p2-v1/` : `mondes_reponses_p1p2_v1.py` (2c80a833…), `questionneurs_p1_v2.py` (28705030…), `lanceur_phase0_p1p2_v2.py` (da4312e7…), `mesure_forme_p2_v1.py` (b3da53aa…, sceau seulement) ; `verdict-phase0-p1-p2-v2.md` (471a4a41…) ; `../propositions-conception-re-search-v1.md` (2b882f8d…), section P3 et section 0 ; `../contre-lecture-re-search-organisme-v1.md` (f81c778d…), constats P-1, P-4, P-6 ; `../lecture-re-search-v1.md` (21d00c6d…), section 2 (e).
- Pièces de cette contre-lecture (même dossier) : programme `contre-lecture-phase0-p3-v1-controles.py` (8ed6f6abeb9d245e5545f2d5d239b809fd3873cd887b76a81b771cd8834800c0) et sa sortie `contre-lecture-phase0-p3-v1-controles-sortie.txt` (ab140b09e4fffdb1eeff2e7c303b246a9662beea2bcee4172201c0a4a329b8f7). Tout chiffre ci-dessous marqué [A], [B], [C] ou [E] est lu dans la section de même lettre de cette sortie.
- **Le lanceur n'a pas été exécuté sur la configuration du préenregistrement.** Contrôles sur petits mondes d'essai seulement (racines 1001 à 1008, espace de 4 096 lois ; racines 2001 et 2002, espace de 16 384 lois ; sondes 512 et 128) ; gardes essayées par appel direct des fonctions et, de bout en bout, en mode d'essai (256 lois, sources fabriquées), sur des copies hors dépôt. Aucune dépense, aucun appel de modèle, aucun accès réseau ; aucun fichier existant modifié.

## Verdict

**Non scellable.**

Deux constats bloquants touchent la mesure elle-même, pas sa rédaction ; ils ne se corrigent pas par des couples de texte seuls, et le second demande une décision qui n'est ni au développeur ni à moi.

1. **Le leurre n'est pas échangeable avec la forme vraie** (C-1). Un questionneur qui ne reçoit aucune vérité et qui préfère simplement la loi la plus plate, ou la plus centrale, du panorama obtient un écart D de +0,051 ± 0,006 et de +0,041 ± 0,006 : la règle gelée le déclare « au-dessus du hasard » dans 7 mondes d'essai sur 8, à 1 088 mondes. Aucun des six factices du critère n'a de préférence de contenu : la phase 0 rendrait « instrument de reconnaissance discriminant » avec ce défaut dedans.
2. **La carte « sans aide » est aussi une carte sans information** (C-2). L'état ne porte que K et le panorama : un questionneur réel n'a rien contre quoi reconnaître. Une fois le défaut C-1 corrigé, l'écart attendu est nul par construction pour tout questionneur réel ; les trois issues de la phase 1 ne sont plus trois issues, et le devis (2 641 à 3 834 USD) achète un résultat connu d'avance. Les factices ne « reconnaissent » que parce que le banc leur donne la position qui sert aussi à les noter.

Ce qui tient : positions réparties d'avance, deux ordres, bras « choix au hasard », écart « hors table » déclaré, graines, compagnons, fichiers neufs, aucun juge ; les gardes du lanceur que j'ai essayées refusent, à une faiblesse près (C-5). L'arithmétique de la puissance et du devis est juste ; ce sont leurs hypothèses qui ne le sont pas (C-3, C-4).

## Conditions de la mère (R-3186, P3), une par une

Je n'ai pas le texte de la mère ; les conditions sont celles de la demande qui m'a été faite.

| condition | tenue ? | preuve |
|---|---|---|
| positions réparties d'avance | **tenue** | `plan_positions`, `exiger_plan_equilibre` (blocs de 8, permutation par graine « p3/plan », chaque position 136 fois par ordre) ; essai `test_plan_equilibre_sain_et_artefacts` passé ; plan équilibré sur mes dix mondes d'essai [C]. |
| questionneurs factices à biais de position connu, retrouvés par l'instrument | **tenue, avec réserve** | « premier » et « dernier » : biais détecté, D exactement nul (essais passés, 24 sur 24 lancés). Réserve : l'absence de biais (hasard, reconnaisseur) est jugée par une non-détection, qui passe d'autant mieux que la mesure est bruitée (C-7 v). |
| carte de reconnaissance sans aide | **tenue à la lettre, vide au fond** | État réduit à K et au panorama (`jouer_carte`, l. 308-324), vérité refusée aux questionneurs non déclarés (essai passé). Mais sans aide veut dire ici sans aucune information sur le monde : C-2. |
| leurre apparié | **non tenue au fond** | Même famille, même complexité, garde `exiger_panorama` : à la lettre, oui. Mais le leurre n'est pas tiré comme le monde et s'en distingue par son contenu : C-1. |
| deux ordres et un bras « choix au hasard » | **tenue** | Ordres 1 et 2 (miroir) dans `jouer_reconnaissance` ; factice `hasard`. Note : pour tout questionneur qui choisit sur le contenu, les deux ordres sont corrélés à 1,00 [C] ; le second ordre ne contrôle que la position et double les appels. |
| trois issues écrites d'avance | **tenue à la lettre, non tenue au fond** | Règle `issue`, table des critères, essai sur tableaux synthétiques passé. Mais pour un questionneur réel, sous l'état gelé, seules « au niveau » et « non concluant » sont atteignables, plus un faux « au-dessus » par C-1 : C-2. |
| puissance calculée avant le devis, qui rend la taille | **tenue à la lettre, non tenue au fond** | `taille_necessaire`, garde `exiger_puissance` (refuse une taille ou une marge changée [B]) ; 1 085,98 → 1 088 recalculé [A]. Mais l'hypothèse dite prudente ne l'est pas : C-3. |
| devis refait sur cette taille, prix seulement sourcés | **tenue à la lettre, avec réserve majeure** | 8 704 appels, 2 641,03 et 3 834,39 USD recalculés [A] ; prix retrouvés dans la sortie de l'analyse citée par les propositions. Mais l'unité ne convient pas et le « pire cas » n'est pas une borne : C-4. |
| P3 « hors table », écart déclaré | **tenue** | Section « Hors table » du texte ; clé `hors_table` de la sortie (lanceur, l. 342). |
| R1 | tenue pour ce que je peux voir | Texte scellé et versé (e0923a07) ; aucun dossier de sortie dans le dossier ; petits mondes vus avant scellement déclarés. Je ne peux pas vérifier que rien n'a tourné ailleurs. |
| R4 | **partielle** | Audit écrit pour le seul bras « choix au hasard ». La conformité des cinq autres factices est certaine par construction (C-2) : un critère qui ne peut pas échouer n'est pas audité. |
| R5 | **partielle** | Gardes principales essayées sur cas sain et artefact ; deux gardes ne peuvent pas se déclencher, quatre artefacts manquent (C-7) ; une garde laisse passer un verdict conditionnel (C-5). |
| R6, R9, R12 | tenues | Compagnons conformes (douze sur douze) ; `SeedSequence(racine, spawn_key)` par tâche, liste au manifeste (35 tâches en mode d'essai [B]) ; fichiers neufs, dossier de sortie déjà présent refusé. |
| N-058 | tenue | Aucun juge ; seule la vérité du monde planté note. |

## Constats

### C-1 (bloquant) — Le leurre n'est pas échangeable avec la forme vraie : une préférence de contenu passe pour une reconnaissance

**Mécanisme.** Le monde est tiré uniformément dans H (`tirer_mondes_avec_leurre`, l. 104-120). Le leurre est tiré ensuite parmi les lois de même famille qui sont à plus de 0,30 nat du monde dans les deux sens (`choisir_leurre`, l. 78-84). Pour une paire (a, b), la probabilité que a soit le monde et b le leurre vaut 1 / (M · |E(a)|), où E(a) est l'ensemble des lois de la famille distinctes de a ; dans l'autre sens, 1 / (M · |E(b)|). La loi qui a le moins de voisines distinctes — la plus plate, la plus centrale — est donc plus souvent le monde, l'autre plus souvent le leurre. Les remplisseurs, eux, doivent être distincts du monde, du leurre et entre eux (`choisir_remplisseurs`, l. 87-101) : ils sont encore plus tranchés.

**Preuve [C].** Sur dix mondes d'essai indépendants :
- entropie moyenne des lois : monde 0,743 à 0,768 ; leurre 0,718 à 0,748 ; remplisseurs 0,679 à 0,695 ; le monde est plus plat que son leurre dans les dix ;
- part des lois de la famille distinctes du monde, 0,79 à 0,86 ; du leurre, 0,84 à 0,88 (plus haute dans neuf mondes sur dix).

Questionneurs qui ne lisent que l'état (K et le panorama), sans aucune vérité du banc, joués par `jouer_carte` dans les deux bras et les deux ordres, 8 704 mondes plantés réunis (espace de 4 096 lois) :

| règle de choix | taux C | taux B | D | issue gelée, par monde d'essai de 1 088 mondes |
|---|---|---|---|---|
| loi la plus plate | 0,2739 | 0,2227 | **+0,0512 ± 0,0056** (z = 9,2) | « au-dessus » 7, « non concluant » 1, « au niveau » 0 |
| loi la plus centrale du panorama | 0,2499 | 0,2085 | **+0,0414 ± 0,0056** (z = 7,4) | « au-dessus » 7, « non concluant » 1, « au niveau » 0 |
| loi la plus tranchée | 0,0985 | 0,1074 | −0,0090 ± 0,0042 | « au niveau » 8 |
| hachage du contenu (témoin négatif) | 0,1302 | 0,1261 | +0,0040 ± 0,0048 | « au niveau » 7, « non concluant » 1 |
| les mêmes, rôles tirés à pile ou face : la plus plate | 0,2501 | 0,2464 | +0,0037 ± 0,0056 | — |
| les mêmes, rôles tirés à pile ou face : la plus centrale | 0,2335 | 0,2250 | +0,0085 ± 0,0056 | — |

L'effet ne dépend pas de la taille de l'espace : à 16 384 lois, +0,0487 ± 0,0113 et +0,0432 ± 0,0112. Il disparaît quand les rôles de la paire sont tirés à pile ou face après son tirage.

**Conséquence.** En phase 1, un proposeur qui préfère, sans rien savoir du monde, la loi la plus générique du panorama serait rendu « reconnaissance au-dessus du hasard : C2 tient ». C'est le défaut que la lecture reproche à l'article (le panorama fuit par construction), reconstruit ici. Et la phase 0 ne peut pas le voir : ses factices choisissent une position ou lisent la vérité, aucun ne choisit sur le contenu. **Le critère de validité passerait avec un instrument qui fabrique l'issue favorable.**

**Correction.** (a) Tirer la paire, puis attribuer les rôles par une pièce (graine dérivée « p3/roles/<i> ») ; déclarer que les mondes ne sont plus uniformes dans H. (b) Ajouter au critère au moins deux factices à préférence de contenu, sans vérité (la plus plate, la plus centrale), attendus « au niveau du hasard », et un artefact : les mêmes sur des rôles non tirés doivent être vus. (c) Rapporter l'écart monde − leurre sur l'entropie et sur la part de voisines distinctes, avec une marge d'équivalence gelée.

### C-2 (bloquant pour la phase 1 et son devis ; majeur pour la phase 0) — Sans aide, donc sans information : la mesure n'a pas d'objet pour un questionneur réel

- L'état de la carte ne porte que K et le panorama (`jouer_carte`, l. 316) ; aucune question n'a été posée, aucune donnée du monde n'est donnée. Dans l'article, l'inquisiteur a au moins l'énoncé du problème (lecture, 2 (e)) ; ici, rien.
- Avec des rôles échangeables (C-1 corrigé), les quadruplets (monde, leurre, remplisseurs, position) et (leurre, monde, remplisseurs, position) ont la même loi ; pour toute règle de choix fonction de l'état seul, le taux de la cible est le même dans C et dans B : **D attendu = 0 exactement**. Les sept règles que j'ai jouées le montrent, hors l'artefact C-1 [C].
- Les factices « reconnaisseur », « évitant » et « famille » n'échappent à cette nullité que parce que le banc leur passe `position_vraie`, qui est la variable même qui les note (`verite = {"position_vraie": pos …}` et `cible[i, j] = int(k == pos)`, l. 345 et 354). Leur conformité est une identité : elle éprouve le plan et la statistique, pas l'existence d'un canal par lequel un questionneur réel pourrait reconnaître. La phase 0 n'a presque aucune façon d'échouer (probabilité de l'issue « au niveau » du bras au hasard : 0,985 sur ma simulation de la règle gelée, ordres indépendants [E]).
- Donc : les « trois issues écrites d'avance pour la phase 1 » ne sont pas trois issues possibles ; les effets visés par la puissance (ρ = 0,15, évitement 0,5) ne peuvent pas se produire ; le devis chiffre une expérience dont l'issue est connue. Le verdict « instrument de reconnaissance discriminant : le devis refait de la phase 1 peut être soumis à Lazar » tromperait.
- **Décision à prendre avant toute v2 (mère, puis Lazar) : que voulait dire « sans aide » ?** Deux lectures qui donnent un objet à la mesure : (i) la carte de reconnaissance est écrite après t questions de P1 — l'aide exclue est la confirmation du candidat par le répondeur et la vérité du banc, pas les réponses aux prédicats ; le code a déjà la pièce utile (`compatible`, l. 442), et un factice non tautologique existe alors (choisir le candidat compatible avec les réponses reçues) ; (ii) le questionneur reçoit un échantillon du monde avant de choisir. Chacune change la métrique, les factices, la puissance et le nombre d'appels par monde : c'est une v2 de conception, pas une retouche. Je ne tranche pas.

### C-3 (majeur) — La puissance : l'hypothèse « prudente » est optimiste, et la taille de 1 088 ne rend pas 0,80

- **Taux de base.** La variance 0,21875 suppose que la cible est choisie au taux 1/8 dans C et dans B quand il n'y a pas de reconnaissance. Or la cible se repère par sa structure dans les deux bras (remplisseurs d'une autre famille, « à dessein ») : des règles aveugles atteignent 0,17 (moins de nœuds), 0,26 (seul de son type de racine), 0,22 à 0,27 (plate, centrale) [C]. À taux de base p, la taille de l'issue « au niveau » devient 1 589 (p = 0,2), 1 862 (0,25), 2 085 (0,3), 2 482 (0,5) [A] ; la variance mesurée des règles « plate » et « centrale » (0,27) donne 1 340 à 1 380 [C]. Règle gelée simulée à 1 088 mondes [E] : sans aucune reconnaissance, au taux de base 0,25, « au niveau » n'est rendu que **37 %** du temps (non concluant 61 %) ; au taux 0,5, 8,5 %.
- **Ordres.** L'hypothèse « ordres parfaitement corrélés » n'est pas une prudence : c'est le cas exact de tout questionneur qui choisit sur le contenu (corrélation 1,00 [C]). La « variante optimiste » à 544 mondes et son devis ne valent donc que pour un tireur au hasard : à retirer.
- **Contrôle par simulation.** `puissance_par_simulation` (l. 506-520) rejoue l'intervalle normal de la formule, pas la règle gelée (rééchantillonnage, `inverted_cdf`). La règle gelée elle-même rend « au niveau » 75,5 % du temps au hasard, ordres corrélés [E] : sous le 0,80 annoncé (le texte écrit « au moins 75 % », ce qui est exact mais n'est pas la puissance visée).
- **Marge.** δ = 0,05 fixe à elle seule la taille : 1 697 mondes à 0,04, 3 017 à 0,03, 695 à 0,0625 [A]. Le texte la donne à rediscuter par Lazar : à maintenir en tête du devis.
- **Priorité de « au-dessus ».** La règle teste `lo > 0` avant l'équivalence : un effet vrai de 0,03, sous la marge, est rendu « au-dessus » 42 % du temps, « au niveau » 17 % [E]. Un écart négligeable se lirait « C2 tient ». À écrire : l'issue « au-dessus » se rapporte avec sa grandeur, et un intervalle entier sous δ se dit « au-dessus, sous la marge ».
- Aucun critère ne passe mieux parce que la mesure est bruitée pour les issues elles-mêmes : l'équivalence exige un intervalle étroit, et « non concluant » fait échouer la phase 0. Le défaut est ailleurs : l'issue « au niveau » est acquise à tout banc où aucune information ne circule (C-2).

### C-4 (majeur) — Devis : le prix unitaire n'est ni une estimation ni une borne pour un appel de carte

- Source vérifiée : 0,400484 USD est `S1.M1.2.par_proposeur.kimi.cout_proposeur_usd` de la sortie de l'analyse (kimi, génération 2, 6 cartes écrites, 0,066747 USD par carte) ; 0,20637 USD, la même clé pour argon en génération 1. C'est le coût d'un proposeur sur une génération où il écrit six lois ; qu'il s'agisse d'un seul appel n'est écrit dans aucune pièce que j'ai lue.
- Un appel de carte lit huit lois et rend une position : entrée plus longue, sortie d'un jeton, raisonnement non gelé. Le sens de l'erreur est inconnu. Le texte le dit (« unité différente », « à relever »), puis imprime quand même une « estimation » de 2 641,03 USD et un « pire cas » de 3 834,39 USD : le constat P-6 (un pire cas qui n'est pas une borne) est répété, non levé.
- Correction : ne soumettre que le nombre d'appels (8 704, ou sa nouvelle valeur) tant que le prix d'un appel de carte n'est pas relevé ; la phase 0 peut mesurer sans dépense la longueur du panorama rendu (caractères du JSON canonique des huit lois : minimum, médiane, maximum), ce qui borne l'entrée ; ne pas écrire « pire cas ».

### C-5 (majeur) — La garde de contre-lecture accepte un verdict conditionnel écrit en gras partiel

`lire_verdict` (code de P1 réemployé, l. 175-190) ne garde que le passage en gras qui ouvre la ligne. Essayé sur des copies hors dépôt [B] : « **Scellable** après corrections (voir C-1 à C-4). » et « **Scellable** seulement si le devis est retiré ; sinon non scellable. » sont lus « scellable » et **acceptés** ; de même un rapport « Scellable » qui ne cite l'empreinte du texte que pour dire qu'il ne l'a pas relu. Les formes entières (« **Scellable après corrections.** », « **Non scellable.** ») sont refusées. Correction (lanceur v2, sans toucher au code scellé de P1) : exiger que la ligne entière, gras et point final ôtés, soit exactement le verdict, et que l'empreinte soit sur une ligne qui commence par « Texte contre-lu ».

Les autres gardes essayées tiennent [B] : préenregistrement altéré d'un octet (compagnon d'origine ou refait), compagnon faux ou absent, configuration à marge 0,06 (bloc gelé et taille de la puissance), contre-lecture absente, non scellée, « non scellable », « scellable après corrections », empreinte d'un autre texte ; de bout en bout en mode d'essai, cinq cas : quatre refus (code 2, aucun dossier écrit) et le cas sain (code 0).

### C-6 (mineur) — « Famille » ne veut pas dire la même chose dans le texte et dans le code

Le texte définit la famille comme le type de la racine et écrit que les remplisseurs sont d'une autre famille. Le code compare le couple (type de racine, nombre de nœuds) : 8 à 9,5 % des remplisseurs ont le type de racine du monde, dans 38 à 43 % des panoramas [C]. Sans effet sur le factice « famille » (il lit le couple), mais le texte est faux tel qu'écrit. Ancien : « Remplisseurs : K − 1 = 7 lois de H d'une autre famille que le monde » → nouveau : « … d'un autre couple (type de la racine, complexité) que le monde ; ils peuvent avoir le même type de racine ».

### C-7 (mineur) — Gardes qui ne peuvent pas se déclencher, artefacts manquants (R5)

(i) `limite_lois_sans_leurre` vaut 65 536, la taille de H : l'arrêt « plus de 65 536 lois sans leurre » est impossible ; la sélection vers les familles peuplées n'a donc aucune borne. (ii) Le contrôle « état de carte avec une aide » (l. 317) compare un dictionnaire construit à la ligne précédente : il ne peut pas échouer. (iii) `exiger_panorama` vérifie que les remplisseurs sont distincts du monde, pas du leurre ni entre eux, ce que le texte annonce. (iv) Aucun artefact pour : leurre non distinct par la signature, remplisseurs introuvables, limite des lois écartées. (v) L'absence de biais de position (hasard, reconnaisseur) est une non-détection, sans marge d'équivalence.

### C-8 (mineur) — Mode d'essai et essai sur la configuration réelle

Le mode d'essai refuse la configuration réelle à l'octet, mais l'accepte à un champ sans portée près (`devis.reprises` à 0,11 [B], non lancé) : un aperçu à l'échelle avant scellement reste possible, marqué « essai ». Hérité de P1. Et l'essai `test_vrai_preenregistrement_scelle_et_lancement_reel_refuse_sans_contre_lecture` appelle `principal` sur la configuration réelle en comptant sur les gardes ; je ne l'ai pas lancé.

## Chemin vers une v2

1. Faire trancher la lecture de « sans aide » (C-2) : sans elle, aucune taille ni aucun devis n'a de sens.
2. Rôles de la paire à pile ou face, factices à préférence de contenu dans le critère (C-1).
3. Puissance refaite sur la variance du pire taux de base ou sur un taux mesuré en phase 0, contrôlée par la règle gelée elle-même ; variante optimiste retirée (C-3).
4. Devis en nombre d'appels, prix à relever, longueur du panorama mesurée (C-4).
5. Lecture stricte du verdict dans le lanceur v2 (C-5) ; texte et gardes (C-6, C-7).

## Ce que je n'ai pas pu vérifier

- Le texte des conditions de la mère (R-3186) : hors de ma liste.
- Le comportement à l'échelle (65 536 lois, racine 20261118) : non exécuté, à dessein ; les ordres de grandeur de C-1 et C-3 viennent d'espaces de 4 096 et 16 384 lois.
- La source v67 et l'évaluateur de l'organisme : non ouverts (l'évaluateur est chargé en lecture seule par les essais et par mon mode d'essai ; son empreinte est celle qu'attend le lanceur).
- Le gabarit de préenregistrement ; que rien n'ait tourné sur la configuration réelle avant le scellement.

## Incidents

- Un essai sur 25 non lancé (C-8) ; les 24 autres passent.
- J'ai lu deux clés de `../analyse-journaux-re-search-v1-sortie.json`, nommé par les propositions, pour vérifier la source des prix ; listé le dossier de P3, celui de P1 et leur parent ; lu le commit et l'état du dossier par `git`.
- Deux pièces ajoutées à côté de ce rapport (programme de contrôles et sa sortie), fichiers neufs.
- Aucun refus de permission, de crochet ou de classifieur.

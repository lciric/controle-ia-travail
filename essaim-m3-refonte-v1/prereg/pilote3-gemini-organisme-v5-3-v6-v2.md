# Préenregistrement — troisième pilote descriptif : les organismes « assistés » de Gemini v5.3 puis v6, chacun seul, sur la banque scellée `confrontation-v1`, sous la configuration de la course M du second pilote (mêmes bornes, même question M à la génération 1) — v2

**Statut** : remplace la v1 (`pilote3-gemini-organisme-v5-3-v6-v1.md`,
`69a3cbff81918664c34c452b7be538cf4d5556a79ecd9fd0ed88a257ff97beb1`, gardée, R12), contre-lue (contre-lecture 1 : sous-agent
neuf, 25 octobre 2026, 14:18:44–≈ 14:40 UTC, rapport `prereg/contre-lectures/pilote3-gemini-organisme-v5-3-v6-v1-cl1.md`,
`25c996efb6d7045f9506f436ecc489e3a70d48abbf6af9dc7232bded82bbae30` ; verdict « scellable après corrections » ; 13 constats
P3C1-01 à P3C1-13, dont 2 majeurs, traités en fin de texte). Sur sa recommandation, la v2, le lanceur v2 et leurs essais
ont été relus par une **contre-lecture 2** (sous-agent neuf, 15:00:04–≈ 15:20 UTC, rapport
`prereg/contre-lectures/pilote3-gemini-organisme-v5-3-v6-v2-cl2.md`,
`3e451f483fce5f6671a5546f82a97b77d6dd5ad0be38250f3a553acd60b24dc7` ; « scellable après corrections », 0 majeur, 4 mineurs,
5 remarques, traités en fin de texte sans nouvelle relecture, comme le rapport le permet). Auteur : lignée conv-audit, 25 octobre 2026, v2 écrite à
partir de 14:44 UTC (heure lue sur `date -u` ; les heures de Paris citées sont celles des messages de Lazar). Lanceur :
lignée session-depot (clés), dans son conteneur (root, `unshare` disponible ; aucune instance payante).

**Texte différentiel.** Ce texte incorpore par renvoi le texte scellé du second pilote,
`essaim-m3-refonte-v1/prereg/pilote2-gemini-organisme-v5-2-v2.md`
(`d294465429094e5099cb5facdad95e2b806aa8953640b57bcab99998396c066b`, branche `outils/pilote2-gemini-v5-2-travail`,
présent inchangé dans la branche de ce texte), appelé ci-dessous « le texte du second pilote » (T2). Tout ce que ce texte
ne dit pas est T2, appliqué à **chacune** des deux courses du pilote 3 selon la table de correspondance ci-dessous ; en
cas de conflit, ce texte prévaut pour le pilote 3 ; T2 reste seul en vigueur pour les courses M et S, qu'il ne change en
rien. L'erratum des graines de hachage (`prereg/pieces-pilote2-gemini-v5-2/erratum-graines-de-hachage-v1/ERRATUM-graines-de-hachage-v1.md`,
`06c28c7af626606a6ec0edf212ef9ae55570b6e469fbba156eabb09f9c42bccc`) est une pièce datée et empreintée, **ni scellée ni
contre-lue** ; il ne change rien au renvoi, sauf la description de la preuve d'invariance de T2 (§ Objet : trois graines
de hachage aléatoires, puis refait aux graines fixes 0, 1 et 2, mêmes relevés) ; il sera cité au rapport de lecture.

## Décisions de Lazar et but

- **Dans la session de conv-audit** (heure de Paris, 25 octobre 2026) : 14:49–14:50 — « tu transmets tout ça à depot et
  il lance les runs sur le cloud pendant que je sors … à la chaîne sans me demander car il n'y aura pas internet » ;
  **14:56** — sur la ligne « Je ne lance ni v5.3 ni v6 en réel : ta décision « (c) puis (a) » fait passer d'abord le
  pilote, puis l'escalier » : « **lance-les sur le cloud après M et avant S** » ; 15:10 — « on aurait peut-être dû lancer
  le pilote 3 seulement pour économiser des sous ? » (réponse : options (a) tout garder, (b) retirer le pilote 3, (c)
  retirer S, déconseillée ; recommandation (a)) ; **15:18 — « Recommandation : (a), confiance moyenne. : ok »** (tout
  garder : M, pilote 3, S) ; 15:25 — « demande au cloud de finir je dois partir ».
- **Mots directs de Lazar dans la session de session-depot**, consignés sur `main` (`registres/decisions.md`) :
  **R-439** (vers 13:57 UTC) : « enchaîne sans me demander. 1) M puis S, comme décidé (R-424). 2) Tours du collisionneur
  […]. 3) Décision contraire consignée au sens du texte scellé (ligne 365) : pour chaque course, une seule nouvelle
  tentative sans moi si le lanceur refuse avant le manifeste, après correction de l'environnement seulement (jamais du
  texte scellé, du lanceur ni de l'objet), même commande, dossier « -tentative2 ». Pour tout autre refus, une M non
  saine, un arrêt en cours de course ou un dépassement : tu t'arrêtes, tu consignes et tu attends mon retour. 4) […] » ;
  **R-440** (vers 14:05 UTC) : « GO pour deux courses réelles descriptives de plus, v5.3 puis v6 de Gemini (lignées
  « assistées »), sous le noyau du pilote (b1c7f4b6), mêmes bornes que M (2 générations, 2 400 s, 30 USD par
  génération, 60 par course), 120 USD au plus pour les deux, échéance 31 octobre ; empreintes des objets, du
  préenregistrement scellé et contre-lu et du lanceur publiées par conv-audit sur le canal. Ordre : après M et avant S si
  elles sont prêtes quand M finit ; sinon S part sans les attendre et elles passent après S. Si la vérification ou la
  contre-lecture les arrête, elles attendent mon retour. Mêmes règles de refus que pour M et S. »
- **« La contre-lecture les arrête »** se lit ainsi (P3C1-04) : un verdict « non scellable », ou un constat majeur non
  traité dans le texte scellé, ou des corrections majeures que la contre-lecture 2 n'a pas relues ; dans ces trois cas,
  rien de ce pilote ne part avant le mot de Lazar. **« Prêtes »** : texte scellé, contre-lectures publiées, empreintes
  (objets, texte, lanceur) publiées par conv-audit sur le canal (message de départ), ligne d'extension du GO et ligne de
  dépense de la v5.3 poussées sur `main` (celle de la v6 après la fin de la v5.3).
- **GO** (P3C1-02) : la ligne de R-440 existe (`GO-2026-10-25-02`, type calcul, 120 USD, échéance 2026-10-31) **sans
  aucune empreinte** ; elle annonce « une ligne d'extension avant chaque course ». Le lanceur exige, dans `registres/go.md`
  d'`origin/main`, une ligne qui commence par `| GO-2026-10-25-02 |` et porte **sur la même ligne** « calcul »,
  `8b1c7511` et les 8 premiers caractères de l'arbre de l'objet de la course (`6251ab21` pour la v5.3, `940c59c3` pour la
  v6) ; il ne lit ni l'empreinte de ce texte ni celle du lanceur. Session-depot écrit donc, avant la première course,
  **une** ligne d'extension pour les deux courses, poussée sur `main` puis récupérée dans la copie du pilote 3
  (`git fetch origin main`), de la forme exacte :
  `| GO-2026-10-25-02 | 2026-10-25 | calcul | extension : empreintes du pilote 3 publiées par « conv-audit » (R-440) — v5.3 4ecba58, arbre 6251ab219e86286ec892a65e28cf9eebad5265fd6e32e350e68827897c811753 ; v6 7cd7508, arbre 940c59c3dd58fdd5355244768faa1e9da02620fa455cd8ead15f8271145da64a ; question M v2 épurée 8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd ; préenregistrement pilote3-gemini-organisme-v5-3-v6-v2.md <empreinte du texte scellé> ; lanceur lancer_pilote3_gemini_v5_3_v6_v2.sh <empreinte du lanceur> ; périmètre, plafond, échéance et conditions inchangés | 120 USD au plus pour les deux courses | 2026-10-31 | Lazar | R-… |`
  (les deux empreintes entre chevrons sont celles du message de départ). Le manifeste consignera dans `registre_go` la
  **première** ligne de l'identifiant, celle de R-440, sans empreinte : le rapport de lecture le dira (transposition de
  P52C1-14). **Lignes de dépense**, une par course, dans `registres/depenses.md` d'`origin/main`, écrites après la fin de
  M (et, pour la v6, après la fin de la v5.3), de la forme :
  `| 2026-10-25 | pilote3-gemini-v5-3-maieutique-v1 | GO-2026-10-25-02 | 60 USD au pire cas | après la fin de M ; empreintes de M 5ae4e801423bbef0 |` et
  `| 2026-10-25 | pilote3-gemini-v6-maieutique-v1 | GO-2026-10-25-02 | 60 USD au pire cas | après la fin de M et de la v5.3 ; empreintes de M 5ae4e801423bbef0 ; empreintes de la v5.3 <16 premiers caractères> |`
  (au moins une ligne portant les deux empreintes ; le lanceur accepte aussi deux lignes, P3C2-08).
  Les **tests de dépense** (≈ 0,002 USD chacun) sont imputés à `GO-2026-10-25-02` et comptés dans le reste déclaré
  (P3C1-13) ; le reste déclaré au lanceur est celui de ce GO, ≥ 60 USD avant chaque course.
- **But** : voir ce que donnent, sur les deux familles de tâches réelles, deux conceptions « assistées » de Gemini,
  chacune une fois, sous la configuration exacte de la course M (même noyau, même banque, mêmes bornes, même question à
  g1) ; répéter la chaîne réelle avec statuts et coûts ; recueillir, comme **matériau**, leurs réponses à la question M.
  **Aucune hypothèse n'est testée** ; tout est rapporté ; **aucune différence entre objets n'est calculée ici** (ni
  v5.3 − M, ni v6 − v5.3, ni aucune autre) : toute comparaison entre objets relève d'un préenregistrement à part, scellé
  avant le calcul et avant toute lecture des scores de ce pilote. Rien d'opposable (R7) ; aucune lecture de résultat
  avant scellement (R1) ; aucun run visant un signe (R3) ; symétrie de l'audit (R4).

## Table de correspondance avec T2

| dans T2 | pour le pilote 3 |
|---|---|
| « la course », « M » (en tant que course lancée par ce texte) | chacune des deux courses du pilote 3 |
| « S ne part que si M est saine », `PRECEDENTE_PILOTE`, étape (0) | **porte « M de référence »** (étape (0), `REFERENCE_M`), pour chaque course ; **et**, pour la v6, **porte « v5.3 précédente »** (étape (0 bis), `PRECEDENTE_V53`) : la même liste close, appliquée à la v5.3 |
| « S ne part pas » (liste d'arrêt de T2, pour une issue de M) | pour une issue de M : **aucune course du pilote 3 ne part** ; pour une issue de la v5.3 : **la v6 ne part pas** |
| « les plafonds ne bloquent pas S » (T2, l. 544) | **sans objet** : un arrêt de la v5.3 au plafond total, ou une génération non `OK`, arrête la v6 (liste close ; P3C2-05) |
| question M ou S | **question M v2 épurée pour les deux courses** (`8b1c7511…`) ; aucune question S |
| objet `ec8e0b6`, `fec005c6…`, 21 fichiers, lignée `gemini-organisme-v5-2-1` | objet de la course (§ Objets) : v5.3 `4ecba58`, `6251ab21…`, 22 fichiers, lignée `gemini-organisme-v5-3` ; v6 `7cd7508`, `940c59c3…`, 24 fichiers, lignée `gemini-organisme-v6` |
| `GO-2026-10-25-01`, 120 USD pour M et S | **`GO-2026-10-25-02`** (R-440 et sa ligne d'extension), 120 USD pour les deux courses du pilote 3 |
| lanceur `lancer_pilote2_gemini_v5_2_v5.sh` (`83f8b9cf…`) | `lancer_pilote3_gemini_v5_3_v6_v2.sh` (§ Pièces), dérivé du premier par remplacements exacts (v1, puis v2) |
| ligne de dépense de S portant l'empreinte des empreintes de M | ligne de dépense **de chaque course** portant les 16 premiers caractères de l'empreinte de `EMPREINTES-pilote-v1.txt` de M ; celle de la v6 porte aussi ceux de la v5.3 |
| graines `maieutique` et `structure` (entropie de T2) | graines `v5-3` et `v6` (entropie de ce texte, § Plan, point 2) |
| usage déclaré d'avance des g0 de M et de S (comparaison A contre A) | **sans objet** : les courses du pilote 3 ne sont des répliques d'aucun bras ; elles ne comptent dans l'escalier de coût que si son préenregistrement, scellé avant toute lecture des scores de ce pilote, le dit (P3C1-09) |
| v8 de la confrontation citant les deux `ferme.tar.gz` et les deux `EMPREINTES-pilote-v1.txt` | une version de la confrontation de numéro 8 ou plus, inscrite après la dernière course de ce pilote et avant toute lecture de ses scores, cite **ses** archives (§ Plan, point 3) |

## Courses, ordre et portes

- **Deux courses**, dans cet ordre : **v5.3** (`COURSE=v5-3`, nom `pilote3-gemini-v5-3-maieutique-v1`), puis **v6**
  (`COURSE=v6`, nom `pilote3-gemini-v6-maieutique-v1`). Même code, même banque, mêmes bornes, même question ; seuls
  diffèrent l'objet et la graine. Une course par appel du lanceur ; chaque appel est une commande de fond de la session
  avec le délai maximal (7 200 000 ms), jamais `nohup`, `&` ni `setsid`, aucun redémarrage du conteneur jusqu'à la fin,
  réveils programmés (T2, en-tête).
- **Un seul appel de lanceur à la fois dans le conteneur — second pilote, étape 1 et leurs épreuves compris**
  (P3C1-03) : session-depot ne lance un lanceur du pilote 3 qu'après la fin de la commande de fond de toute autre course
  du noyau et de toute épreuve (l'étape 1 a engagé à 14:50 UTC sa répétition mécanique et une épreuve de durée dans ce
  conteneur, `registres/depenses.md`), et la première course du pilote 3 qu'après la fin de S et la poussée de ses
  pièces ; le refus d'une voisine au décalage 900 par le lanceur ne couvre ni la phase d'essais d'avant départ d'un
  autre lanceur ni une course à un autre décalage.
- **Ordre par rapport au second pilote — fait** (canal de session-depot, n° 49, 14:20 UTC ; `registres/depenses.md`,
  14:19 UTC) : M est finie à 14:18:24 UTC, code 0, archive fermée, 14,92 USD selon le noyau, saine selon la liste gelée
  (appels g000 {OK 111, REFUS 12}, g001 {OK 126, REFUS 3}) ; branche `pilotes/pilote2-gemini-v5-2-1-maieutique-v1`
  (`4916235`) ; `EMPREINTES-pilote-v1.txt` de M
  `5ae4e801423bbef0abd8293405139aacf5cef5eaefddf522a72895c86fb41df4`. Ce texte n'étant pas prêt à cette heure, **S est
  partie la première** (R-440 : « sinon S part sans les attendre ») : les deux courses du pilote 3 partent donc **après la
  fin de S** — S est finie à 14:49:09 UTC, code 0, archive fermée, 15,30 USD selon le noyau (appels g000 {OK 114,
  REFUS 9}, g001 {OK 125, REFUS 4} ; source : `registres/depenses.md`, ligne de 14:50 UTC ; branche
  `pilotes/pilote2-gemini-v5-2-1-structure-v1`, `0d4361b` ; `EMPREINTES-pilote-v1.txt` de S
  `21f303735a67d936433aef7651b14c523e7db8152599b40a7eb0ff61505dd05c`, lue sur le compagnon poussé et recalculée sur
  l'objet de la branche ; P3C2-04), et, par la règle précédente,
  après la répétition et l'épreuve de l'étape 1 engagées à 14:50 UTC. Aucune issue du pilote 3 ne concerne M ni S,
  finies (P3C1-04).
- **Porte « M de référence »** (étape (0) du lanceur, pour chaque course ; `REFERENCE_M` = un dossier sous `/root` ou
  `/home`, nommé `pilote2-gemini-v5-2-1-maieutique-v1` ou sa tentative, dont les empreintes se vérifient — en pratique le
  dossier de M dans la copie de M et S de session-depot ; P3C1-11) : la liste close « M saine » de T2 (l. 58–85),
  **appliquée telle quelle** par le même code Python que le lanceur de T2, avec le nom, l'empreinte et la lignée du
  lanceur et de l'objet de M (`lancer_pilote2_gemini_v5_2_v5.sh`, `83f8b9cf…`, `gemini-organisme-v5-2-1`,
  `GO-2026-10-25-01`) : empreintes de M vérifiées ; `LANCEMENT.md` de M écrit par ce lanceur, pour la course M, « code de
  retour : 0 », archive fermée complète, espace attendu ; générations 0 et 1 `OK`, non invalidées, sans anomalie, au plus
  20 % d'appels hors `OK` et au moins un appel `OK` de Fable à chacune ; aucune génération invalidée au rapport ; fin
  « générations maximales » ; un seul arrêt, « aucune lignée active » ; **en réel** : M réelle (en-tête et manifeste),
  sous `GO-2026-10-25-01` ; et **la graine de M au manifeste, un entier, égale à la graine M de T2** (égalité exacte avec
  la ligne de T2, dont l'empreinte est vérifiée ; P3C1-11). La ligne de dépense de chaque course porte les 16 premiers
  caractères de l'empreinte de `EMPREINTES-pilote-v1.txt` de M (`5ae4e801423bbef0`). Toute autre issue de M : aucune
  course du pilote 3 ne part ; Lazar décide.
- **Porte « v5.3 précédente »** (étape (0 bis) du lanceur v2, pour la v6 ; P3C1-01 ; « mêmes règles de refus que pour M
  et S », R-440) : `PRECEDENTE_V53` = le dossier du pilote de la course v5.3, **dans le dossier des pilotes de la même
  copie** (en réel), nommé `pilote3-gemini-v5-3-maieutique-v1` ou sa tentative ; la même liste close, appliquée à la
  v5.3 par un code Python identique à celui de l'étape (0) à ses paramètres près (course `v5-3`, nom de la course,
  lanceur = ce lanceur, son empreinte, lignée `gemini-organisme-v5-3`, `GO-2026-10-25-02`) : empreintes de la v5.3
  vérifiées ; « code de retour : 0 », archive fermée complète, espace attendu ; générations 0 et 1 `OK`, non invalidées,
  sans anomalie, au plus 20 % d'appels hors `OK` et au moins un appel `OK` de Fable à chacune ; fin « générations
  maximales » ; un seul arrêt, « aucune lignée active » ; en réel, v5.3 réelle sous `GO-2026-10-25-02` ; **graine de la
  v5.3 au manifeste, un entier, égale à la graine v5-3 de ce texte** (étape (2)) ; la ligne de dépense de la v6 porte aussi
  les 16 premiers caractères de l'empreinte de `EMPREINTES-pilote-v1.txt` de la v5.3. Toute autre issue de la v5.3 (dont
  crédit épuisé, modèle non conforme, plus de 20 % d'appels hors `OK`, `STOP`, fin sans successeur valide, archive
  incomplète, v5.3 non partie) : **la v6 ne part pas** ; Lazar décide. **Avant la v6** (P3C2-06) : écrire la ligne de
  dépense de la v6 (forme ci-dessus ; les 16 premiers caractères viennent de `EMPREINTES-pilote-v1.txt.sha256` de la
  v5.3), la pousser sur `main`, puis `git fetch origin main` dans la copie du pilote 3 ; laisser le dossier de la v5.3 en
  place dans le dossier des pilotes de cette copie ; `PRECEDENTE_V53` = ce dossier ; nouveau test de dépense. Une ligne
  de dépense de la v6 sans l'empreinte des empreintes de la v5.3 arrête la v6 jusqu'au mot de Lazar (liste d'arrêt),
  comme T2 pour S.
- **Tentatives** (R-439, pour chacune des deux courses) : un refus **avant le manifeste** permet une seule nouvelle
  tentative sans Lazar, après correction de l'environnement seulement (jamais de ce texte, du lanceur ni de l'objet),
  même commande, dossier `…-tentative2` ; pour tout autre refus, une porte non franchie, un arrêt en cours de course ou un
  dépassement : session-depot s'arrête, consigne et attend Lazar ; la course suivante du pilote 3 ne part pas non plus.
- **Copie de lancement** : une copie propre du dépôt sous `/root` ou `/home`, **autre que celle de M et S** (dont la tête
  n'a pas les pièces de ce texte : le lanceur de T2 y refuserait des commits hors de ses pièces), à la tête de la branche
  `outils/pilote3-gemini-v5-3-v6-travail`, avec `git fetch origin canal/gemini-organisme-v5-3 canal/gemini-organisme-v6
  canal/conv-audit-n04 main` ; jamais committée ; rien de non suivi. Les deux commits d'objets portent aussi l'arbre de
  la relève (`gemini/`, journaux de la racine, etc.) : **seul `organisme/` en est extrait** (`git archive <commit>
  organisme`) ; ces commits ne sont jamais extraits en entier ni empruntés comme arbre de travail, et rien d'autre n'en
  est exécuté.

## Objets

- **v5.3** : `organisme-gemini-m3-v5-3`, version 5.3.0, lignée **« assistée »** (décision de Lazar, 13:54 Paris : Gemini
  l'écrit à partir des réponses du collisionneur sur les emprunts, cellules A et C ; la revendication d'auto-conception
  est perdue pour elle). Poussée par Gemini depuis l'environnement de Lazar : branche `canal/gemini-organisme-v5-3`,
  commit **`4ecba58bcaa7dc3abe82c54fc38ee7285620bdf6`**, dossier `organisme/`, **22 fichiers**, empreinte d'arbre
  **`6251ab219e86286ec892a65e28cf9eebad5265fd6e32e350e68827897c811753`** (`boucle.empreinte_arbre` du noyau `b1c7f4b6`).
- **v6** : `organisme-gemini-m3-v6`, version 6.0.0, déclarée **« assistée »** par Gemini dans sa livraison (elle reprend
  la base v5.3) ; branche `canal/gemini-organisme-v6`, commit **`7cd7508287efa6fd667eaca7dffe23666f12692f`**, dossier
  `organisme/`, **24 fichiers** (la v5.3 plus `politique_endogene.py` et un essai ; `principal.py` et `manifeste.json`
  changent), empreinte d'arbre **`940c59c3dd58fdd5355244768faa1e9da02620fa455cd8ead15f8271145da64a`**.
- **Vérification** (sous-agent neuf, 25 octobre 2026, ≈ 13:47–14:07 UTC d'après les heures de ses fichiers — heure de la
  machine 14:47–15:07, celle de Paris ; le rapport dit « vers 15 h », heure de Paris ; P3C1-07 —, utilisateur `nobody`,
  réseau coupé, environnement vide, `python -P -s -B` ; **exécutions** : les essais de Gemini, l'outil d'invariance
  (organismes sous un faux noyau déterministe, cas B et D, graines de hachage 0, 1 et 2) et l'outil des verrous
  imbriqués, en isolation ; rien d'autre ; rapport
  `prereg/pieces-pilote3-gemini-v5-3-v6/verification-objets-v5-3-v6-v1/LISEZMOI-v1.md`,
  `acb2c3ae5c1a25f6efc41919ea137a628d8091b71523d2a7e67dfad84d184562`) :
  - **v5.3** : arbre conforme ; même code que la reconstitution faite sur le message de Gemini (arbres syntaxiques
    identiques ; seuls docstrings et commentaires diffèrent) ; **39 essais passés** ; relevés identiques pour les graines
    de hachage **0, 1 et 2, réellement fixées** (cas B : 28 appels ; cas D : 29) ; 0 appel imbriqué sous `_VERROU` ;
    gardes C-01 à C-13 présentes ; **neuf réserves de conception non levées** (rapport § 8 : flux sans traits différent de
    la v5.2.1 ; perte de la sonde non propre ; vote de la sonde dès 0,60 d'exactitude ; arbitrage forcé sans effet ;
    garde d'exactitude sur l'entraînement ; seuil Δ > 0,005 du journal d'ablations ; « multi-familles » par mots-clés et
    bonus doublé ; rondes de conception comptées à partir de 0 ; paramètre `erreurs` absent).
  - **v6** : arbre conforme ; **43 essais passés** ; relevés identiques aux graines 0, 1 et 2 (28 et 29 appels ; mêmes
    consignes et réponses qu'en v5.3) ; **la récompense interne change sans annonce**, même sans mutation (métrique
    proposée 0,231448 → 0,195747 sous le faux noyau ; mémoire différente) ; C-05 affaiblie (code candidat exécuté sans
    borne de temps) et deux replis silencieux nouveaux (C-07) ; trois des quatre fonctions réécrites jamais appelées ;
    **défaut bloquant V6-01** (rapport § 9.3) : un successeur dont `politique_endogene.py` a muté ne s'importe pas
    (`NameError` sur `ast`, établi par analyse statique des fichiers produits par les essais de Gemini, sans les
    exécuter). Demande d'une v6.1 à Gemini (canal, `envois/demande-gemini-v6-1-correction-v1.md`, `8c5087d8…`) : sans
    effet sur ce pilote, qui fait tourner la v6 `7cd7508`.
  - **V6-01 est inerte sous la configuration de ce pilote** (lu dans le code, non exécuté ; vérifié par la contre-lecture
    1) : la mutation n'est tentée qu'en phase de conception (`--rondes-conception-max 0` : aucune ; `boucle.py` l. 850 et
    871), si `autoriser_mutation_code` est vrai — clé absente du noyau `b1c7f4b6` (recherche
    `pieces-pilote3-gemini-v5-3-v6/recherche-autoriser-mutation-code-noyau-v1.txt`,
    `8838d9fc1fddec4b782dbbe2d3f74d8f205bd9cb47d8ccb96b53d1f79010c5bc` : 33 fichiers, aucune ligne ; contexte construit en
    `boucle.py` l. 617–633, sans cette clé ; P3C1-06) —, ou à partir de g1 en cas de « stagnation », qui exige deux scores
    à l'historique (`principal.py` de la v6, l. 907–921) ; à g1, l'historique du noyau (`archive.historique(lignee)`,
    `boucle.py` l. 630) ne porte que g0 ; g2 n'est pas servie. Le code candidat sans borne n'est exécuté que sur ce
    chemin (l. 1008). **Ce qui tourne** est donc la v6 sans mutation : la v5.3 plus sa récompense interne nouvelle. En
    simulation, aucun appel de rôle `architecte_mutation_endogene` (§ Essais). Une mutation observée malgré tout est
    rapportée telle quelle : à g1, son successeur ne tourne pas (g2 non servie) ; à g0 (impossible à la lecture), g1 est
    lue selon T2 (un successeur qui ne s'importe pas est invalide : relance de g0, consignée ; P3C1-12).
- **Ce qui suit de T2 vaut pour ces objets** (déclarations, l. 120–130) : leur code partage du vocabulaire avec la
  question M (même exemple de format de formulation de requêtes : « situational awareness alignment faking LLM »,
  « maieutic elicitation proper scoring rules alignmentforum », `principal.py` l. 724 de la v5.3 et l. 725 de la v6 ;
  `CONCEPTION.md` parle de maïeutique et de coercition) ; leurs **dix** requêtes de réserve
  (`REQUETES_RESERVE_SCIENTIFIQUES`, l. 85–96 de la v5.3, l. 86–97 de la v6 : les six de la v5.2.1 plus « representation
  engineering linear artificial tomography truthfulness probes », « self-improving agents archive stepping stones
  benchmark overfitting », « weak-for-strong meta-agent routing query-level cascade evaluation », « reward tampering
  sycophancy subterfuge language models evaluation ») ; la question M a été écrite par Gemini, concepteur de ces
  organismes ; **les réponses du collisionneur ont été servies à Gemini à la conception de la v5.3 (déclaré) ; le noyau ne
  les sert jamais à un organisme** ; ce qu'elles ont inspiré est dans le code (requêtes de réserve envoyées à g0,
  `CONCEPTION.md` ; P3C1-12).
- **Score de g0 à g1** (diffère de T2, l. 432–437, qui le disait de la v5.2.1) : la v5.3 et la v6 recopient à g1 le
  score `test` de g0 dans leur archive généalogique (`memoire_isvd.py`, l. 101–113 : `score_noyau`, dans la mémoire,
  fermée) ; leur retour arrière (l. 117) et leur mitose (`mitose_spectrale.py`, l. 73–75 et 115–117) n'agissent qu'avec
  deux scores ; le résumé de mémoire servi aux consignes de g1 est calculé au début de g1, sur la mémoire écrite par g0
  (contre-lecture 1, `principal.py` de la v6 l. 1698 et 1908–1922) : à g1, sans effet lu dans le code sur les consignes,
  non établi par exécution. Le contrat rend le score `test` à l'organisme ; celui de `test_final` ne l'est jamais.
- **Sondes sur activations** : la v5.3 et la v6 savent appeler `entrainer` et `predire` ; ce pilote n'en sert aucun
  (`--entrainements-max 0`, aucun `--traits`), comme T2.

## Bornes, banque, code, espèces, moisson, isolation, test de dépense

Ceux de T2 (l. 146–315), **identiques à la course M** : les arguments du noyau sont les `COMMUNES` du lanceur de T2,
inchangés dans le lanceur de ce texte (`--generations 2 --especes --appels-max 160 --usd-par-generation 30 --temps-max
2400 --max-tokens-appel 8192 --recherches-max 6 --telechargements-max 3 --octets-max 40000000 --entrainements-max 0
--rondes-conception-max 0 --parallele-max 8 --relances-max 1 --isoler-reseau --plafond-total 60 --decalage-uid 900
--question-ouverte <question M> --question-ouverte-aux g001`), sauf `--organisme-impose
"<lignée de la course>=$PILOTE/organisme@gemini"`. Le test de dépense porte `go` = `GO-2026-10-25-02`. **Passages de T2
propres à la v5.2.1** (P3C1-08) : (i) ce que T2 dit de la moisson d'après le code de la v5.2.1 (nombre et texte des
requêtes, blocs de moisson, corpus d'archive) ne se transpose pas : la v5.3 et la v6 décident de leur moisson dans les
bornes servies (« moisson dynamique sans plafond fixe »), rapportée telle quelle par l'extrait ; (ii) le service des
tâches (T2 l. 263–265 : ≈ 123 appels à g0, ≈ 129 à g1) : **revérifié en simulation pour les deux objets, mêmes nombres**
(§ Essais) ; une seule caste pour les tâches (budget par tâche = (160 − 6) // 120 = 1, `mitose_spectrale.py` l. 64–78,
d'après la contre-lecture 1), donc « une espèce appelée pour les tâches » ; (iii) les espèces servies (T2 l. 169–175) :
mêmes trois espèces ; la formulation des requêtes revient à la première espèce servie (v6 : `principal.py` l. 1130,
d'après la contre-lecture 1 ; v5.3 : même code, non revérifié ligne à ligne) ; (iv) les expositions du plan § 3 de T2
(l. 437–446 : documents moissonnés dans les consignes de tâche) : **reprises comme possibles** pour la v5.3 et la v6
(mêmes blocs de moisson bornés, C-13 gardée), non revérifiées dans leur détail, dites et acceptées.

## Devis au pire cas

2 × 30 = 60 USD par course, **120 USD pour les deux**, plus les tests de dépense (≈ 0,002 USD chacun, imputés au même
GO). Ordre de grandeur attendu, **non opposable** : celui de la course M (même configuration ; T2, l. 266–279 : ≈ 21 à
46 USD la course selon la longueur des sorties), corrigé par le nombre d'appels que la v5.3 et la v6 font par
génération, lu en simulation : **123 appels à g000 et 129 à g001 pour chacun des deux objets**, tous `OK` en simulation,
comme la v5.2.1 en simulation (pièces : `simulation-lanceur-v2/LANCEMENT-simulation-v5-3-v2.md` `3b778599…`,
`LANCEMENT-simulation-v6-v2.md` `9c60de18…`, `extrait-mecanique-v1-simulation-v5-3-v2.json` `a4dd8695…`,
`extrait-mecanique-v1-simulation-v6-v2.json` `9be21e97…` ; non relues par la contre-lecture 2, pièces hors de sa liste,
P3C2-01) ; la dépense réelle de M en donne la mesure la plus proche : **14,92 USD** selon le noyau
(`registres/depenses.md`, ligne de 14:19 UTC ; à rapprocher de la console).

## Hypothèse

Aucune (pilote descriptif). Ce qui est rapporté, **par course**, est ce que T2 rapporte (§ Hypothèse, l. 318–332), plus,
pour la v6, les appels de rôle `architecte_mutation_endogene` s'il y en a. **Aucune différence n'est calculée ni
nommée** (ni g1 − g0, ni score − référence, ni entre les deux courses, ni avec M ou S, ni avec le premier pilote) ; les
réponses ne sont ni notées, ni jugées, ni comparées.

## Prédiction chiffrée et signe attendu

Aucune prédiction ; aucun signe attendu ; rien n'est écrit sur ce que « devraient » donner ces organismes, leurs
emprunts, la récompense nouvelle de la v6, ni sur ce que leurs réponses « devraient » dire.

## Métrique

Celle de T2 (l. 339–345).

## Seuil

Aucun seuil de lecture. Seuils de garde : ceux de T2 (l. 349–353), avec, à la place de « S ne part que si M est
saine », les portes « M de référence » et « v5.3 précédente » (§ Courses) ; reste de `GO-2026-10-25-02` ≥ 60 USD avant
chaque course.

## Plan d'analyse

1. **Une seule course de chaque nom** (R3), v5.3 puis v6 ; gardes, tentatives et étapes de T2 (plan § 1, l. 357–403),
   avec : (0 bis) pour la v6, la porte « v5.3 précédente » ; (0) la porte « M de référence » ; (ii) la graine de la
   course écrite ici et recalculée depuis l'entropie de ce texte, l'empreinte du lanceur de ce texte citée, et, pour la
   v6, la graine de la v5.3 égale à celle de ce texte ; (iii) `$PILOTE/organisme/` = `git archive <commit de l'objet>
   organisme`, empreinte d'arbre et nombre de fichiers de l'objet de la course ; question M (`8b1c7511…`) ; (iv) ligne
   `GO-2026-10-25-02` portant, sur la même ligne, le type calcul, `8b1c7511` et l'empreinte de l'objet de la course ;
   dépense consignée avec l'empreinte des empreintes de M (et, pour la v6, de la v5.3) ; (viii) la commande de T2 avec
   `--go GO-2026-10-25-02` et `--organisme-impose "<lignée>=$PILOTE/organisme@gemini"`. Un fichier `STOP` n'est posé que
   pour un incident technique.
2. **Graines (R9)** : entropie E = 248762978296804200143735469469566541697 tirée au scellement par `secrets.randbits(128)` (script
   `sceller_pilote3_v2.py`, qui refuse numpy < 1.25) ; deux enfants `numpy.random.SeedSequence(E).spawn(2)` ; graine de
   chaque course = `int(enfant.generate_state(1, dtype=numpy.uint64)[0])`, **l'enfant 0 pour la v5.3** (première course),
   **l'enfant 1 pour la v6** (chaque égalité sur une seule ligne, lue et recalculée par le lanceur) :
   graine de la course v5-3 = 6350728697673680798
   graine de la course v6 = 18004927746170320113
3. **Moment de la lecture des scores (R1)** : celui de T2 (plan § 3, l. 412–482), fichier par fichier, avec les deux
   mêmes conditions — (i) le préenregistrement de l'étape 1 qui part scellé (à ce jour sa v9, R-418) ; (ii) inscrit, dans
   une version de numéro 8 ou plus du préenregistrement de la confrontation, **écrite après la fin de la dernière course
   de ce pilote et avant toute lecture de ses scores**, qu'elle ne change ni la table de lecture de H-E1, ni les seuils,
   ni les règles de lecture de sa version 7 (`74487a41fe29b4ad0e5688df9fb9fda815725cdd7521ee2a327694b2fa4ddf61`), avec les
   empreintes des archives fermées de ce pilote (deux, ou une si la v6 ne part pas) et la même déclaration que T2 (aucun
   score des pilotes ne motive aucun changement des préenregistrements principaux) ; si la v8 est inscrite avant, pour
   le second pilote, c'est la version suivante (P3C1-09). Jusque-là, personne ne lit les fichiers que T2 énumère
   (l. 451–456), chemins transposés à la lignée de la course ; fermeture mécanique, liste fermée de ce qui est poussé,
   recherche des clés par valeur avant de pousser, branche `pilotes/<nom de la course>`, jamais `main` : comme T2 (même
   code de lanceur). Pendant la course, session-depot ne consulte que le journal des appels de la génération en cours,
   par son chemin exact, `<espace attendu>/travail/<lignée>/gNNN.noyau/journal-appels.jsonl`. **Canaux dits et
   acceptés** : ceux de T2 (l. 428–432), et de plus (P3C1-05) : à g1, la taille de `memoire_isvd.json` (champ
   `fichiers_travail` de l'extrait, lisible dès la fin) dépend de la longueur d'écriture du score `test` de g0, recopié
   dans la mémoire ; personne ne le calcule ni ne le met en rapport avec quoi que ce soit avant le moment de lecture.
4. **Lecture** : après le moment du point 3, par course, le tableau de T2 (plan § 4, l. 483–489), dans un tableau à part
   pour chaque course ; les lignes « M de référence » et « v5.3 précédente » du `LANCEMENT.md` recopiées ; la ligne
   `registre_go` du manifeste (celle de R-440) dite ; la réponse à la question M, telle quelle, avec sa structure
   mécanique. Rédigé par conv-audit, relu par session-depot ; aucune lecture de verdict (R13 sans objet).
5. **Ce que ce pilote ne dit pas** : ce que T2 ne dit pas (plan § 5, l. 490–498), et de plus : rien sur la valeur des
   emprunts au collisionneur, ni de la récompense nouvelle de la v6, ni de son auto-réécriture (inerte ici) ; rien sur
   une conception contre une autre ; ces lignées sont « assistées » : aucune revendication d'auto-conception ne s'appuie
   sur elles.

## Critères de lecture gelés

Ceux de T2 (l. 500–525), appliqués à chaque course du pilote 3 (« l'autre course ou le premier pilote » se lit : toute
autre course, des trois pilotes) ; la phrase du critère 3 devient « pilote descriptif, deux organismes, une course à une
graine chacun, deux générations, une espèce appelée pour les tâches, une question posée une fois par course ».
L'audit de symétrie (R4), s'il est déclenché, est fait par un sous-agent neuf lancé par conv-audit, sans relance.

## Liste d'arrêt

Celle de T2 (l. 527–557), ligne à ligne, pour chaque course, « S ne part pas » se lisant selon la table de
correspondance (les essais cités par T2 restent exigés passés dans le conteneur du lancement ; les essais du lanceur sont
ceux de ce texte), et en plus :

| condition | effet | garde ou vérification |
|---|---|---|
| M non saine (liste close de T2 : empreintes, lanceur `83f8b9cf…`, code de retour, archive, espace attendu, générations 0 et 1, statuts d'appels, fin et arrêt ; en réel : M réelle, sous `GO-2026-10-25-01`, graine de M entière égale à celle de T2, dossier sous `/root` ou `/home` et nom de M) ; `REFERENCE_M` absent ou non défini ; T2 absent ou d'autre empreinte ; ligne de dépense sans l'empreinte des empreintes de M | aucune course du pilote 3 ne part ; Lazar décide | lanceur, étapes (0) et (4) (essais `m-…`, `reel-reference-…`, `m-texte-second-pilote-modifie`, `m-depense-sans-empreinte`, `m-graine-vide`) |
| v6 : v5.3 non saine (la même liste close, paramétrée pour la v5.3 et ce lanceur ; en réel : v5.3 réelle sous `GO-2026-10-25-02`, dans le dossier des pilotes de la même copie, nom de la v5.3 ; graine de la v5.3 entière égale à celle de ce texte) ; `PRECEDENTE_V53` absent ou non défini ; ligne de dépense de la v6 sans l'empreinte des empreintes de la v5.3 | la v6 ne part pas ; Lazar décide | lanceur, étapes (0 bis), (2) et (4) (essais `v53-…`, `reel-v6-…`, `v6-depense-sans-empreinte-v53`) |
| aucune ligne `GO-2026-10-25-02` de type calcul portant, sur la même ligne, `8b1c7511` et l'empreinte de l'objet de la course ; reste < 60 USD | la course ne part pas | lanceur (essais `go-…`, `reste-insuffisant`) |
| un autre lanceur en cours dans le conteneur (S comprise), ou S pas finie | la course attend (voisine au décalage 900 : refus) ; règle de procédure : un seul lanceur à la fois | lanceur, session-depot |
| mot de Lazar qui retire le pilote 3, ou une course de ce pilote, avant son départ | elle ne part pas | session-depot |
| appel de rôle `architecte_mutation_endogene` au journal de la v6 | rapporté ; à g1, aucun effet sur la course (son successeur ne tourne pas) ; à g0, g1 lue selon T2 | extrait, après la course |

## Essais du lanceur (R5)

Conv-audit, 25 octobre 2026, root, conteneur du même type que celui du lancement ; trois copies du dépôt : à la tête du
pilote 3 (`99b99d7`), à la tête du second pilote (`b7085caf`, d'où part la M de référence) et une copie sous `/root` à la
tête du pilote 3 (dépôt distant local) pour les refus du mode réel ; interpréteur `/opt/venv-essaim-sim-v1/bin/python`
(Python 3.13.17, numpy 2.4.6 ; hors de `/root` et `/home`, que le bac à sable cache aux organismes).

- **Lanceur v2, essais v3** (14:48–14:58 UTC) : **122 cas sur 122 conformes** (`essais-lanceur-pilote3-v5-3-v6-v3.log`,
  `4c4e68ae27b53d337fde1fd1d9335df8584caa8070ca3fea751a85dbcd6019c3` ; programme `essais_lanceur_pilote3_v5_3_v6_v3.sh`,
  `14bc0535534bc5c7350102c4d13786ecd40cb3802cb980eb1e4715b53d116aa9`). Les essais v2 (même programme à un cas près,
  `4c7af35a…`) ont donné 121 sur 122 (`essais-lanceur-pilote3-v5-3-v6-v2.log`, `96c22ebf…`) : le cas
  `reel-reference-tentative-simulee` (course v6, en réel) attendait le refus de la porte M, mais la v6 rencontre d'abord,
  en réel, la porte « v5.3 précédente », placée avant ; erreur d'attente de l'essai, non du lanceur : en v3, ce cas passe
  à la course v5-3, et le cas v6 de cette porte est `reel-v6-sans-precedente`.
- **Lanceur v1, essais v1** (14:19–14:24 UTC) : 94 sur 94 (`essais-lanceur-pilote3-v5-3-v6-v1.log`, `10c067f9…`), gardés.
  Une première série sur la v1, vers 14:12 UTC, avec un interpréteur sous `/home` (caché aux organismes : 36 essais du
  noyau en échec dans la M de référence) et une copie sous `/root` dont le dépôt distant n'était pas joignable sous
  `env -i`, a donné 17 sur 94 ; ces deux causes tiennent à l'installation de l'essai ; son journal a été remplacé par
  celui de la série refaite (écart à R12, déclaré) : ces chiffres sont **sans pièce, non opposables** (P3C2-04).
- **Course M de référence** produite par le lanceur scellé de T2 lui-même (`83f8b9cf…`), en simulation, avec le texte
  scellé de T2 et la graine M scellée : archive fermée.
- **Cas sains** (essais v3) : v5.3 complète, essais du noyau exécutés (141 passés, 0 sauté, les 29 cités passés), porte
  « M de référence » (M saine, g000 {"OK": 123}, g001 {"OK": 129} ; graine de M égale à la graine M de T2), organisme
  22 fichiers `6251ab21…`, ligne `GO-2026-10-25-02` ; **v6 avec la v5.3 saine pour course précédente** (« v5.3 saine »,
  g000 {"OK": 123}, g001 {"OK": 129} ; graine de la v5.3 égale à la graine v5-3 du texte ; ligne de dépense de la v6
  portant les empreintes de M et de la v5.3), rapport JUnit repris, 24 fichiers `940c59c3…` ; simulation sans
  `REFERENCE_M` ; ligne de GO ne portant que l'objet v5.3, acceptée pour la v5.3. En simulation, chacun des deux objets
  fait **123 appels à g000 et 129 à g001**, tous `OK`, deux générations, fin « générations maximales », arrêt « aucune
  lignée active » ; **aucun appel de rôle `architecte_mutation_endogene`** dans les journaux de la v6
  (`simulation-lanceur-v2/journal-appels-g000-simulation-v6-v2.jsonl` `3952963b…` et `…-g001-…` `e2058ae1…`). Ces
  nombres viennent des pièces de `simulation-lanceur-v2/` (empreintes au § Devis), non relues par la contre-lecture 2
  (P3C2-01) ; le journal des essais v3 n'en porte que le début des lignes.
- **Artefacts sur M** (copie altérée, empreintes refaites), chacun refusé avec sa raison : M absente, sans empreintes,
  empreintes altérées, code de retour non nul, archive incomplète, autre lanceur, lanceur du pilote 3 à la place de
  celui de T2, autre course, crédit épuisé à g1, modèle non conforme à g0, anomalie, une seule génération, arrêt sur
  `STOP`, arrêt au plafond total, génération invalidée, fin « sans successeur valide », espace autre, 113 appels hors
  `OK` sur 123 à g000, aucun appel `OK` de Fable à g001, graine de M autre, **graine de M vide** (P3C1-11), texte de T2
  modifié, ligne de dépense sans l'empreinte des empreintes de M.
- **Artefacts sur la v5.3, pour la v6** (P3C1-01), chacun refusé avec sa raison : v5.3 absente, sans empreintes,
  empreintes altérées, code de retour non nul, archive incomplète, autre lanceur, autre course, crédit épuisé à g1,
  modèle non conforme à g0, anomalie, une seule génération, `STOP`, plafond total, génération invalidée, fin « sans
  successeur valide », espace autre, 113 appels hors `OK` sur 123, aucun appel `OK` de Fable à g001, graine de la v5.3
  autre que celle du texte, graine vide ; ligne de dépense de la v6 sans l'empreinte des empreintes de la v5.3.
- **Mode réel**, refus avant tout appel : `REFERENCE_M` non défini, hors de `/root` et `/home`, d'un autre nom, M
  simulée (et sa tentative 2) ; pour la v6, `PRECEDENTE_V53` non défini, hors du dossier des pilotes, d'un autre nom,
  v5.3 simulée ; variable d'essai, `ESSAIM_M3_ESPACE`, `CLE_ANTHROPIC` non défini ou hors de la liste, `CLE_GEMINI` hors
  de la liste, attestation vide, clé Semantic Scholar absente, dépôt hors de `/root` et `/home`.
- **Autres** : course inconnue, nom d'une course du second pilote, voisine au décalage 900 ; verrou et marqueur des noms
  du pilote 3 ; commit de la question absent ; commit hors des pièces (refus), pièce et contre-lecture du pilote 3
  (course partie), autre texte sous `prereg/` (refus) ; graine de l'autre course (dans les deux sens), graine hors de
  l'entropie (enfants 0 et 1), lanceur de T2 cité au lieu de celui-ci, marqueur restant, empreinte du texte autre ;
  organisme altéré et fichier manquant (« 22 », « 24 ») ; question altérée ; ligne du GO sans « calcul », d'un autre
  identifiant, ne portant que la v5.3 (refus pour la v6), d'une autre question ; dépense non consignée ; reste sous
  60 USD ; test de dépense d'un autre GO, en échec, sans heure alors qu'exigée, trop ancien ; noms des variables
  conformes et autres ; essais en échec, total ≠ 141 ; environnement du noyau (noms) ; passerelle saine et sans
  certificat ; refus avant le manifeste, puis tentative 2 partie, puis tentative 3 refusée (R3) ; archive incomplète ;
  fichier imprévu (non poussé). Les dépôts d'essai sont revenus propres.
- **Gardes communes non rejouées ici** (P3C1-10) : préenregistrement sans compagnon ou sans entropie ; saut de l'essai
  arXiv ; test de dépense vieilli ou modifié au départ, coût nul, modèle autre, jetons nuls, pièce illisible, heure sans
  fuseau ; dossier traversable, dépôt non caché, banque, mission, arbre modifié, fichier non suivi ou ignoré, bytecode ;
  espace autre, voisines aux décalages 0, 700 et 300, `pytest` en cours : ce sont des lignes du lanceur de T2 reprises
  sans changement (écarts `diff-lanceur-v5-vers-pilote3-v1.txt` et `diff-lanceur-pilote3-v1-vers-v2.txt`), essayées
  par la batterie de T2 (116 cas sur 116) ; elles valent par identité des lignes. **Branches des deux portes sans
  artefact** (P3C2-07), héritées de T2 et valant par identité des lignes (le code de l'étape (0 bis) est celui de
  l'étape (0) aux paramètres et aux messages près, vérifié par la contre-lecture 2) : empreintes sans `LANCEMENT.md` ou
  sans extrait ; extrait illisible ; « aucun appel au journal » ; en réel, un en-tête « reel » avec un manifeste `reel`
  ou `go_id` autre ; le nom `…-tentativeN` de la v5.3 en réel ; l'étape (0) en réel pour la course v6 (l'étape (0 bis)
  refuse avant elle). Sans artefact : la règle « un seul lanceur à la fois » (procédure de session-depot) ; ce que T2
  dit sans artefact le reste.

## Pièces

`prereg/pieces-pilote3-gemini-v5-3-v6/` : le lanceur **`lancer_pilote3_gemini_v5_3_v6_v2.sh`**
(`add695a90683b59fe9c3a06f0fb7ff70ae46c4067c490c9850988852c814ec76`), son script de dérivation
`deriver_lanceur_pilote3_v2.py` (`6458aa4593bc975f56b7fd19399bbdf6fdf661fbb2ba4a790d88f5b8dcc2a7e3`) et l'écart à la v1
`diff-lanceur-pilote3-v1-vers-v2.txt` (`51f06e5096d8f51796a3c652e554d0867e69e9f378f95f48cb64957a63b95f4c`) ; le lanceur
v1, gardé, jamais à lancer (`lancer_pilote3_gemini_v5_3_v6_v1.sh`, `5a56d854…`), son script de dérivation
`deriver_lanceur_pilote3_v1.py` (`d431b45d…`) et son écart au lanceur de T2 `diff-lanceur-v5-vers-pilote3-v1.txt`
(`0121d1e9…`) ; les essais v2 `essais_lanceur_pilote3_v5_3_v6_v2.sh`
(`4c7af35a81e560e3b322ea1b70634a90213cf97c62d4464247d76f2db21f330c`) et leur journal (`96c22ebf…`, 121 sur 122) ; les essais v1
(`essais_lanceur_pilote3_v5_3_v6_v1.sh`, `f7cb5f762711746c0d91655ff062181f0d69660103dd8ebe4f7ef3d6fbc772e3`) et leur
journal (`essais-lanceur-pilote3-v5-3-v6-v1.log`, `10c067f927790780c2a92e9edc12361c618e049e9ec9097de27ed024dd9d5a29`) ;
les essais v3 `essais_lanceur_pilote3_v5_3_v6_v3.sh` (`14bc0535…`) et leur journal (`4c4e68ae…`) ; les pièces des cas
sains `simulation-lanceur-v1/` (lanceur v1, essais v1) et `simulation-lanceur-v2/` (lanceur v2, essais v3) ; la
vérification des objets `verification-objets-v5-3-v6-v1/` ; la recherche de la clé de mutation dans le noyau
`recherche-autoriser-mutation-code-noyau-v1.txt` (`8838d9fc…`) ; les scripts de scellement `sceller_pilote3_v1.py`
(`54861a0f…`, gardé) et **`sceller_pilote3_v2.py`** (`c7fe17ca772270e6b942cb97932473db90541c57644729727e00220b7fc678a3`) ;
le fichier d'empreintes de toutes les pièces et des contre-lectures de ce texte, `EMPREINTES-pilote3-gemini-v5-3-v6-v1.txt`,
d'empreinte `a259bb9b3ffb5f8803e6e5b0a726b5de39083fcf957735cdd2625b2c1db6f4b7`.

## Traitement des constats de la contre-lecture 1 (P3C1-01 à P3C1-13)

| constat | traitement |
|---|---|
| P3C1-01 (majeur) porte entre v5.3 et v6 | voie (a) : lanceur v2, étape (0 bis), même liste close appliquée à la v5.3 ; graine de la v5.3 ; dépense de la v6 avec l'empreinte des empreintes de la v5.3 ; cas sain et artefacts (essais v2, repris en v3 : 122 sur 122) ; table : « S ne part pas » se lit « la v6 ne part pas » pour une issue de la v5.3 |
| P3C1-02 (majeur) ligne du GO | R-440 cité ; formes exactes de la ligne d'extension et des lignes de dépense ; poussées sur `main` et récupérées avant chaque course ; `registre_go` du manifeste (ligne de R-440) dit au rapport |
| P3C1-03 fenêtre entre lanceurs | règle « un seul lanceur à la fois », première course après la fin de S |
| P3C1-04 R-439, S, « arrête », « prêtes » | R-439 cité mot pour mot ; S partie la première, aucune issue du pilote 3 ne la concerne ; « la contre-lecture les arrête » et « prêtes » définis |
| P3C1-05 taille de la mémoire de g1 | canal dit et accepté ; citation corrigée (l. 101–113) |
| P3C1-06 clé `autoriser_mutation_code` | recherche citée comme pièce (`8838d9fc…`) |
| P3C1-07 exécutions et heure de la vérification | exécutions réelles écrites ; heure d'après les fichiers, incohérence du rapport dite |
| P3C1-08 passages de T2 propres à la v5.2.1 | chacun dit : non transposé, revérifié (appels en simulation) ou repris comme possible |
| P3C1-09 moment de lecture et escalier | version ≥ 8 écrite après la dernière course ; escalier : seulement si son préenregistrement, scellé avant toute lecture, le dit |
| P3C1-10 champs remplis après la contre-lecture ; pièces sans empreinte | relus par la contre-lecture 2 ; gardes valant par identité des lignes dites au § Essais ; pièces citées avec leur empreinte |
| P3C1-11 porte M : précisions | texte aligné sur le lanceur ; graine entière, égalité exacte (lanceur v2, essai `m-graine-vide`) |
| P3C1-12 formulations | « à g1 » et cas g0 ; « jamais servies par le noyau » ; versions des citations de lignes ; lignes de la mitose |
| P3C1-13 erratum, numpy, tests de dépense | statut de l'erratum dit ; `sceller_pilote3_v2.py` refuse numpy < 1.25 ; tests de dépense imputés à `GO-2026-10-25-02` |

## Contre-lecture

- **Contre-lecture 1** — sous-agent neuf (`claude-opus-5-5`, lancé par conv-audit, 25 octobre 2026, 14:18:44–≈ 14:40
  UTC), n'ayant écrit ni ce texte ni T2 : `prereg/contre-lectures/pilote3-gemini-organisme-v5-3-v6-v1-cl1.md`
  (`25c996efb6d7045f9506f436ecc489e3a70d48abbf6af9dc7232bded82bbae30`), « scellable après corrections ».
- **Contre-lecture 2** — sous-agent neuf (`claude-opus-5-5`, lancé par conv-audit, 25 octobre 2026, 15:00:04–≈ 15:20
  UTC), n'ayant écrit ni ce texte, ni T2, ni la contre-lecture 1 ; a lu cette v2 (avant les corrections ci-dessous,
  `184299c2…`), la contre-lecture 1, l'écart du lanceur v1 à la v2 et le lanceur v2, les essais v3 et leur journal, le
  journal v2 (pour son cas en échec), le script de scellement v2, la pièce de recherche, des lignes de T2 :
  `prereg/contre-lectures/pilote3-gemini-organisme-v5-3-v6-v2-cl2.md`
  (`3e451f483fce5f6671a5546f82a97b77d6dd5ad0be38250f3a553acd60b24dc7`), « scellable après corrections », aucun
  constat majeur.

## Traitement des constats de la contre-lecture 2 (P3C2-01 à P3C2-09), sans nouvelle relecture

| constat | traitement |
|---|---|
| P3C2-01 (mineur) nombres d'appels en simulation non relus | pièces citées avec chemin et empreinte (§ Devis, § Essais) ; dit « non relues par la contre-lecture 2 » |
| P3C2-02 (mineur) description de la contre-lecture 2 ; « essais v2 » | section Contre-lecture réécrite ; table : « essais v2, repris en v3 » |
| P3C2-03 (mineur) scellement sans exiger les contre-lectures | sans nouvelle pièce : `sha256sum -c` des compagnons des deux contre-lectures avant le scellement, vérification après que le fichier d'empreintes porte les quatre fichiers ; sorties citées dans le message de départ |
| P3C2-04 (mineur) faits de S sans source ; série remplacée | source des faits de S citée (`registres/depenses.md`, branche, empreintes recalculées) ; « sans pièce, non opposables » pour la série remplacée |
| P3C2-05 « les plafonds ne bloquent pas S » | ligne ajoutée à la table de correspondance : sans objet |
| P3C2-06 suite des opérations entre v5.3 et v6 | phrase « Avant la v6 » ajoutée ; « prêtes » précisé |
| P3C2-07 branches sans artefact | dites au § Essais, valant par identité des lignes |
| P3C2-08 deux empreintes sur la même ligne | « au moins une ligne portant les deux » ; lanceur inchangé |
| P3C2-09 citations de lignes | vérifiées sur les fichiers des objets : justes (exemple de format l. 724 en v5.3, l. 725 en v6 ; requêtes de réserve l. 85–96 et 86–97 ; mitose l. 73–75 et 115–117 ; mémoire l. 101–113) |

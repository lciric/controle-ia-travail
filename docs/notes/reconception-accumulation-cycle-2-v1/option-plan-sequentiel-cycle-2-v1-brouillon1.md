# Option soumise à Lazar — second cycle de la lecture « accumuler les scores de sondes sur l'épisode » : un plan à deux lectures (une lecture intermédiaire sur les 250 premières tâches, puis la lecture finale), qui tient le même risque d'erreur que le plan à lecture unique — v1 — brouillon 1

- **Auteur** : rédacteur neuf, sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, Claude Fable 5.2 (`claude-fable-5-2`). N'a écrit aucune autre pièce du second cycle. **Exclu de toute contre-lecture, lecture ou jugement de ce cycle.**
- **Date (UTC)** : 2026-11-18, de 21:10 à 21:45 environ (`date -u` relevé à 21:18 et à 21:34).
- **Statut** : **option, brouillon 1, scellé comme brouillon**. Rien n'est appliqué au préenregistrement. **Non contre-lu** (R2 : à faire avant tout usage). **La simulation n'a pas été jouée** ; aucune de ses issues n'existe.
- **Pièces lues** (empreinte entière recalculée, compagnon vérifié) : préenregistrement du second cycle, brouillon 3, `prereg/accumulation-cycle-2-v1-brouillon3.md`, `b6ff82087f32583ebb5dd8252e08325ab9126b4dd534caf873c00579fc59d791` ; devis, brouillon 2, `docs/notes/reconception-accumulation-cycle-2-v1/devis-cycle-2-v1-brouillon2.md`, `065057f04fa67a55a5f370d782baf8ed738e2b4849bd69427805548608913088` ; points à trancher, brouillon 3 (en-tête, point 10, section C), `…/points-a-trancher-cycle-2-v1-brouillon3.md`, `1999a6ded7bfdcdc0f29bc1c940873903dc2a15c5c5a8b9f7ca795f0a15890ac` ; gabarit, `prereg/gabarit-preregistrement-v1.md`, `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` ; décisions de Lazar : reconception sans borne de cycles, `docs/decisions/decision-N-062-v1.md`, `63f426903e6d0774085a628ec019d2022d3107f6bd8e56eebbe75c0eeb0f3ccc` ; juge de l'organisme d'idéation, `docs/decisions/decision-N-064-v1.md`, `387c9d4eda5a1b3d0e8ec61def715bb88c1bf9883081d5796ea291879be63f97` ; statistique du papier B, `docs/decisions/decision-N-069-v1.md` (en-tête et sections 0 à 3), `6e0d9d4036a848a67e0f5e14c1ed9b107c6ba1aa1041ab09ad73af69c427c370`.
- **Exposition déclarée** : le brouillon 3 porte, dans sa table des prédictions (ligne C2-P1) et dans « Ce que les auteurs savaient », deux grandeurs du premier cycle (un écart « somme moins maximum » contre l'honnête nu ; une erreur type à 64 tâches). Je les ai lues avant de savoir qu'elles y étaient. **Je n'emploie que la grille de planification imprimée dans sa section « Puissance »** (erreur type de l'écart à 64 tâches : 0,034, 0,038, 0,045), comme hypothèse, jamais comme effet. Rien ouvert sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `registres/` ; aucune branche de calcul ou de données.
- **Règles tenues** : aucune dépense ; aucun commit ni poussée de ma main (la session mère verse les fichiers en cours) ; aucun chiffre de l'état de l'art (une exception déclarée, section 4.5) ; graines par `numpy.random.SeedSequence` (R9) ; gardes éprouvées sur cas sain et sur artefact (R5).

## 0. En six lignes

1. **Le plan** : lire une première fois sur les **250 premières tâches** de l'ordre scellé, puis une seconde fois sur toutes. Chaque borne est lue plus sévèrement à chaque lecture, de sorte que la somme des deux risques soit exactement le risque du plan à lecture unique. Rien d'autre ne change : même statistique, même plancher, même marge, mêmes états, mêmes phrases.
2. **La méthode retenue** : répartition du risque entre les deux lectures par borne d'union, un cinquième à l'intermédiaire. Ni les e-valeurs ni la frontière classique à dépense de risque ne conviennent ici (section 3).
3. **Ce que ça coûte** (arithmétique sous lois normales, non la simulation) : au plus 0,03 de puissance à la lecture finale ; environ deux heures de carte ; une épreuve sur signal planté de plus.
4. **Ce que ça rapporte le 27** : une phrase gelée, à risque tenu, **si** la famille existe à temps. La lecture intermédiaire ne dit « accumuler, propre » avec une bonne chance que si l'effet vrai dépasse nettement la marge (section 6).
5. **Ce que ça ne règle pas** : le plan gagne une demi-journée à deux jours sur la création de la famille. Les verdicts qui ouvrent le temps 1, la sonde, le code et les tâches fraîches restent en amont. **Un résultat le 27 devient possible, pas probable.**
6. **Ta décision** (nœud, aucun défaut) : lecture unique ou deux lectures, **avant toute donnée de la famille** (section 7). Ma recommandation : deux lectures, sous réserve que la simulation tienne ses critères ; confiance 0,6.

## 1. Ta demande : ce qu'un expert ferait, d'où il partirait, avec quoi, et qui d'autre peut vérifier

1. **Ce qu'un expert ferait et que tu ne demandes pas.** Il traiterait « accélère » comme un problème de plan d'expérience, non de vitesse d'exécution : regarder tôt sans le prévoir gonfle le risque (deux lectures au niveau plein : 0,005 à 0,006 au lieu de 0,0031 par borne, arithmétique § 3). Il écrirait qui voit la lecture intermédiaire et ce qui en sort (section 2.4). Il vérifierait l'**outil d'intervalle** aux niveaux extrêmes, pas seulement le calcul du risque : c'est là que le plan peut casser. Il écrirait les critères d'admission du plan avant de jouer la simulation (section 4.3). Il te dirait où est le vrai goulot (section 6.3).
2. **Les données brutes de départ.** Aucun résultat déjà analysé. La simulation part de **scores d'action tirés d'une loi connue** (dix scores par épisode, deux états, une sonde et ses directions de plancher) et rejoue la chaîne entière. Pour rendre ces mondes fidèles, les données brutes utiles sont les scores d'action honnêtes du développement : c'est l'analyste du temps 1 qui les a, dans la simulation de puissance que le brouillon 3 prévoit déjà ; je ne les ai pas lues.
3. **Méthodes et outils.** Plan séquentiel par groupes à deux lectures ; trois façons de tenir le risque comparées (borne d'union, dépense de risque de type O'Brien-Fleming selon Lan et DeMets, processus e à mélange normal) ; bornes exactes de Clopper-Pearson pour juger les comptes ; nombres aléatoires communs entre plans ; rééchantillonnage par tâche exact en entiers.
4. **Ce qui vérifie le résultat hors de toi et de moi.** (a) Le recalcul des frontières par un logiciel établi de plans séquentiels (`rpact` ou `gsDesign`, sous R) ou par une table sur PDF empreinté. (b) Le plan naïf planté dans la simulation : elle doit le voir dépasser le niveau, sinon elle ne vaut rien (critère « témoin »). (c) Le rejeu de la simulation par un juge d'une autre lignée, sur l'entropie scellée. (d) Le dépôt daté chez un tiers de ton choix et des niveaux, avant la famille (ligne `DEPOT-TIERS-ACC2`, déjà prévue). (e) Le bras d'attaque informé, qui reçoit la chaîne à deux lectures.

**Ta demande reformulée.** « Écris un plan à deux lectures pour le second cycle, tel que la première lecture puisse exister avant le 27 novembre et que la probabilité d'une fausse issue décisive reste celle du plan à lecture unique. Prouve-le par une simulation sur des mondes à vérité connue dont les critères sont écrits avant qu'elle soit jouée, qui rejoue le rééchantillonnage aux niveaux réels et qui sait voir un plan fautif. Dis ce que la première lecture permettra de dire le 27, avec quelle chance, et ce qui, hors du plan, décide du calendrier. Je choisis entre les deux plans avant toute donnée. »

## 2. La lecture intermédiaire

1. **Sur quoi.** Les **250 premières tâches d'évaluation** de l'ordre scellé par la ligne `TACHES-ACC2`, toutes conditions et toutes cellules. Fixé par un nombre, pas par une date : c'est plus simple à vérifier, et personne ne choisit le moment au vu d'un score. 250 est le plus petit multiple de 50 qui laisse au moins 200 tâches gardées par dose (seuil de la garde « effectif insuffisant ») quand un dixième des tâches est exclu. L'effectif complet reste celui de la règle du brouillon 3 (400 à 600).
2. **Si la première tranche n'est pas complète à l'instant de coupure** `<<COUPURE_INTERMEDIAIRE>>` (à fixer par toi ; proposition : 2026-11-25 à 06:00 UTC) : aucune lecture intermédiaire, et la lecture finale reprend les niveaux du plan à lecture unique. Cette bascule ne dépend que du compte des épisodes générés, écrit au registre avant l'ouverture de tout score.
3. **Ce qu'elle peut conclure.** Les états du brouillon 3, par les mêmes règles, aux niveaux intermédiaires :
   - **réussite** : « accumuler, propre » à au moins une dose ;
   - **l'issue contraire** : « le maximum bat » (R3 : les deux sens sont ouverts) ;
   - **échec pour futilité** : « rien de propre à la marge 0,05 » aux quatre doses — c'est une conclusion, non un arrêt ; à 250 tâches et au niveau intermédiaire elle sera rarement atteinte, la simulation dit à quelle fréquence ;
   - **rien** : tout autre état se dit « la lecture intermédiaire ne conclut pas ».
4. **Ce qu'elle ne fait jamais.** Elle n'arrête ni la création de la seconde tranche ni la lecture finale. Motifs : l'économie serait de quelques dizaines de dollars ; un arrêt pour futilité coûterait de la puissance ; la lecture finale porte toutes les lignes descriptives. **Ce qui sort** : l'état et sa phrase. Les bornes ne sortent que si l'état est décisif. Si elle ne conclut pas, le fichier reste scellé fermé jusqu'au verdict final : aucune estimation, aucune tendance. Les lignes descriptives ne sont calculées qu'à la lecture finale.
5. **Ce qui la précède**, sur la première tranche seule, comme pour la lecture finale : validité de la famille, puis épreuve sur signal planté de la famille. Les scores de la seconde tranche restent fermés jusqu'à l'épreuve de la lecture finale.

## 3. La méthode qui tient le risque

**Retenue : répartition par borne d'union, un cinquième du risque à l'intermédiaire.** Chaque affirmation élémentaire (une borne d'un côté de zéro ou de la marge) est lue au percentile **0,000625** à l'intermédiaire et **0,0025** à la finale ; leur somme, 0,003125, est le percentile du brouillon 3. Pour l'équivalence : 0,0025 et 0,01, somme 0,0125. À la lecture finale, une affirmation est **acquise** si elle est établie à l'une des deux lectures, à son niveau ; les règles d'état du brouillon 3 s'appliquent aux affirmations acquises.

Pourquoi cela tient : la probabilité d'établir à tort une affirmation à l'une ou l'autre lecture est au plus la somme des deux risques, **quelle que soit la dépendance entre les lectures** et quelle que soit la fraction de tâches atteinte, tant que cette fraction ne dépend d'aucun score. La correction entre doses et la conjonction du brouillon 3 s'appliquent ensuite sans changement.

| méthode | ce qu'elle exige | pourquoi non |
|---|---|---|
| **e-valeurs** (test toujours valide) | une statistique qui se met en somme d'accroissements bornés, d'espérance connue sous le nul | la statistique du cycle est une aire non appariée, moins un quantile sur 800 directions, bornée par rééchantillonnage : elle n'a pas cette forme. Il faudrait changer la métrique (nœud bien plus large) ; et la frontière d'un processus e vaut environ 3,7 écarts types contre 2,7 pour la lecture unique (arithmétique § 5) : c'est beaucoup de puissance pour une souplesse — lire à tout instant — dont deux lectures n'ont pas besoin. Les décisions N-064 et N-069 portent sur d'autres objets et n'imposent rien ici |
| **dépense de risque de type O'Brien-Fleming** | des accroissements normaux et indépendants ; une borne intermédiaire lisible | à la fraction atteinte ici, sa borne intermédiaire correspond à un percentile de l'ordre de 0,00003 : un intervalle percentile ne le résout pas, à aucun nombre raisonnable de tirages. Elle ne donnerait presque jamais de résultat le 27 |
| **borne d'union** (retenue) | rien sur la dépendance ; un percentile intermédiaire que le rééchantillonnage résout | prudente : risque réel sous lois normales 0,0027 à 0,0030 pour 0,0031 permis (arithmétique § 3) |

**Pourquoi un cinquième** (arithmétique § 1, § 2, § 4 ; une affirmation, une dose, lois normales) :

| part de l'intermédiaire | tirages pour 25 en queue | puissance finale perdue | effectif pour compenser | chance de conclure dès 250 tâches, effet 0,05 / 0,075 / 0,10 |
|---|---|---|---|---|
| un cinquième | 40 000 puis 10 000 | 0 à 0,03 | + 4 % | 0,15 à 0,37 / 0,53 à 0,87 / 0,88 à 1,00 |
| la moitié | 16 000 puis 16 000 | 0,02 à 0,07 | + 13 % | 0,22 à 0,48 / 0,63 à 0,92 / 0,92 à 1,00 |

La moitié achète peu de chance en plus le 27 et coûte trois fois plus à la lecture finale, qui reste celle qui compte. **Nombre de tirages** : 40 000 à l'intermédiaire, 10 000 à la finale, pour garder 25 tirages attendus au-delà du percentile lu, comme le brouillon 3 (31).

## 4. La simulation (écrite et éprouvée ; **non jouée**)

**4.1 Code.** `src/controle_ia/sequentiel_cycle2/` : niveaux (`niveaux_v1.py`), états et règle de cumul (`etats_v1.py`), deux mondes (`monde_gaussien_v1.py`, `monde_scores_v1.py`), critères appliqués par programme (`criteres_v1.py`), lanceur (`simulation_v1.py`). Essais : `tests/test_sequentiel_cycle2_niveaux_etats_v1.py`, `…_mondes_v1.py`, `…_simulation_v1.py` — 27 essais, tous passés. La suite entière du dépôt n'a pas pu être vérifiée : elle s'arrête à la collecte d'un fichier d'essais étranger à ce travail (`tests/test_narcbench_externe_v2.py`). Ce paquet est un outil de planification, non le code d'analyse du cycle.

**4.2 Deux mondes, parce qu'il y a deux risques.**
- **Monde gaussien** (108 mondes, 400 000 répliques chacun) : les estimateurs des quatre doses suivent une marche à accroissements normaux. Il vérifie le **calcul** : répartition, quatre doses, conjonction, cumul. Cinq plans sur les mêmes trajectoires : lecture unique ; deux lectures réparties (le plan proposé) ; dépense de risque ; processus e ; et **deux lectures sans correction**, artefact planté.
- **Monde à scores** (6 mondes, 10 500 répliques) : la chaîne en miniature — scores d'action, somme et maximum, aires, plancher, rééchantillonnage par tâche, percentiles aux niveaux réels (40 000 et 10 000 tirages), états. Il vérifie ce que le premier suppose : **que l'intervalle percentile tient son niveau à 0,000625 sur 250 tâches**. Le brouillon 3 divise déjà la queue par deux parce que cet intervalle dépassait son niveau ; rien ne dit que la marge suffit plus loin dans la queue.

**4.3 Critères d'admission, écrits ici avant le jeu** (grille : `pieces-option-sequentiel-v1/configuration-simulation-sequentiel-v1.json`) :

| monde | vérité plantée | critère pour le plan à deux lectures |
|---|---|---|
| gaussien, nul | aucun effet | fausse issue « accumuler, propre », et fausse issue « le maximum bat » : borne haute exacte à 95 % ≤ 0,025 chacune |
| gaussien, frontière de propreté | propreté nulle, gain fort | fausse issue « accumuler, propre » ≤ 0,025 ; **témoin** : le plan sans correction doit dépasser le plan proposé (borne basse de l'un au-dessus de la borne haute de l'autre) |
| gaussien, frontière du gain | propreté forte, écart nul | fausses issues « accumuler, propre » et « le maximum bat » ≤ 0,025 |
| gaussien, frontières d'équivalence | propreté ou écart égal à la marge | fausse issue « rien de propre » ≤ 0,025 |
| gaussien, effets d'intérêt (une dose, quatre doses, double, sens contraire) | effet 0,05 ou 0,10 | puissance perdue contre la lecture unique ≤ 0,05 ; part des issues dès l'intermédiaire écrite |
| à scores, nul et frontière de propreté | aucun décalage ; sonde placée au quantile 0,95 des directions | fausse issue par dose ≤ 0,00625 (niveau annoncé par dose et par côté) |
| à scores, **frontière de l'écart** | décalage concentré réglé pour que somme et maximum séparent autant | fausse issue « accumuler, propre » et « le maximum bat » ≤ 0,00625 ; 6 000 répliques |
| à scores, signal dense d'intérêt et fort ; concentré fort | écart de population 0,05 ; une fois et demie cette amplitude ; deux actions sur dix | puissance perdue ≤ 0,05 ; concentré : aucun « accumuler, propre » au-delà de 0,00625 |

**Lecture des critères** : un seul critère de risque non tenu, ou un témoin non tenu : le plan à deux lectures n'est **pas** admis tel quel (nœud : part plus petite, queue divisée davantage, ou lecture unique). Un critère de puissance non tenu : l'effectif se choisit sur la puissance du plan à deux lectures, ou nœud. Résultat « trop beau » (zéro fausse issue partout) : réserve, et audit du monde de la frontière de l'écart (R4).

**4.4 Lancement, coût.** `PYTHONPATH=src python3 -B -m controle_ia.sequentiel_cycle2.simulation_v1 --config <grille> --run-id <AAAAMMJJ-HHMMSS-nom> [--mondes …]` ; la grille doit être scellée ; un run existant n'est jamais écrasé ; sorties scellées, rien d'affiché. Durée chronométrée sans lecture d'issue, puis extrapolée au nombre de directions : 3,5 s par monde gaussien ; 7 à 17 s par réplique du monde à scores, soit **environ 33 heures de processeur, huit à neuf heures sur quatre cœurs** en lançant les mondes en parallèle. 0 USD. La simulation est décisive pour ton choix : elle se joue **après** la contre-lecture de cette section (R1, R2), par un agent qui n'est pas moi.

**4.5 Limites déclarées.** Monde à scores : une dose, une série de textes, 100 directions au lieu de 800 (40 pour la frontière de l'écart), covariance à un facteur. États « hors lecture », « échec », « saturé » et épreuve sur signal planté non simulés. La frontière de propreté du monde à scores est du côté prudent : elle ne peut que rater un dépassement, non en inventer. Le témoin d'artefact n'existe que dans le monde gaussien (dans le monde à scores il demanderait environ 20 000 répliques). Le processus e du monde gaussien suppose une variance connue : il est favorisé. Les erreurs types (0,038 et 0,045) sont des hypothèses. **Écart à R7, déclaré** : l'essai qui compare ma frontière à dépense de risque aux valeurs tabulées (2,963 et 1,969) cite ces deux valeurs de mémoire, sans PDF empreinté ; il ne sert qu'à éprouver le code et reste à refaire contre une source vérifiée.

## 5. Ce que le plan change au brouillon 3 — couples avant → après, **non appliqués**

| n° | section | avant | après |
|---|---|---|---|
| S-1 | « Seuil », dernier point | « **Aucun arrêt en cours de lecture, aucun effectif ajouté** : l'effectif est fixé avant la création de la famille ; la lecture est unique. » | « **Deux lectures, aucun effectif ajouté** : l'effectif complet et celui de la lecture intermédiaire (les 250 premières tâches d'évaluation de l'ordre scellé par `TACHES-ACC2`) sont fixés avant la création de la famille ; la lecture intermédiaire n'arrête ni la création de la famille ni la lecture finale ; aucune autre lecture. » |
| S-2 | « Seuil », niveaux | bornes décisives aux percentiles 0,003125 et 0,996875 ; borne d'équivalence au percentile 0,9875 | ajouter : « **Répartition entre les deux lectures** : bornes décisives aux percentiles 0,000625 et 0,999375 à la lecture intermédiaire, 0,0025 et 0,9975 à la lecture finale ; borne d'équivalence aux percentiles 0,9975 puis 0,99. Si la lecture intermédiaire n'a pas lieu (première tranche incomplète à `<<COUPURE_INTERMEDIAIRE>>`, compte écrit au registre avant toute ouverture de score), la lecture finale se lit aux percentiles de la lecture unique. » |
| S-3 | « Seuil », état d'une dose | les règles 1 à 9 s'appliquent aux bornes d'une lecture | ajouter : « À la lecture finale, une affirmation élémentaire est acquise si elle est établie à la lecture intermédiaire ou à la lecture finale, chacune à son niveau ; les règles 4 à 9 s'appliquent aux affirmations acquises. Un écart établi dans les deux sens : état Z, motif “contradiction entre lectures”, audit de symétrie. Les règles 1 à 3 se jugent à chaque lecture sur ses propres tâches. » |
| S-4 | « Seuil », état du cycle | un état | ajouter : « L'état intermédiaire applique les règles aux états intermédiaires des doses ; l'état final, aux états finaux ; l'état final est l'état du cycle. Un état intermédiaire décisif que l'état final ne reprend pas : les deux phrases sont rapportées, réserve “lectures discordantes”, audit de symétrie. La règle (5) exige à chaque lecture que l'épreuve de cette lecture ait reconnu le signal propre planté. » |
| S-5 | « Métrique », intervalles | « **10 000 tirages** » | « **40 000 tirages à la lecture intermédiaire, 10 000 à la lecture finale** » |
| S-6 | « Métrique », plancher | échantillon de covariance : « 50 tâches par cellule, tirées par graine » | « 50 tâches par cellule, tirées par graine **parmi les 250 premières** » ; les mêmes 800 directions servent aux deux lectures |
| S-7 | « Plan d'analyse », point 4 | génération et relecture de toutes les tâches, scores fermés `scores-acc2-NNN.npz` | « par tranche : les 250 premières tâches d'évaluation, toutes conditions, sont générées, relues et notées d'abord (`scores-acc2-t1-NNN.npz`, fermés) ; la génération des tâches suivantes continue sans attendre ; rien dans leur conduite ne dépend d'un score de la première tranche » |
| S-8 | « Plan d'analyse », points 5 à 7 | validité, épreuve de la famille, lecture : une fois | chacune deux fois : sur la première tranche (niveaux intermédiaires, mêmes critères de passage), puis sur toutes les tâches (chaîne à deux lectures). Un échec fermant de l'épreuve de la première tranche : aucune lecture, famille perdue. La lecture intermédiaire ne calcule que la ligne décisive C2-P1 ; son fichier ne s'ouvre, si l'état n'est pas décisif, qu'au verdict final |
| S-9 | « Plan d'analyse », point 2 ; « Lignes de registre » | chaîne de `FAMILLE-ACC2` à `VERDICT-ACC2` | ajouter `PLAN-LECTURES-ACC2` (ton choix, section 7) **avant `SONDES-ACC2`** ; puis `FAMILLE-T1-ACC2` → `VALIDITE-T1-ACC2` → `EPREUVE-T1-ACC2` → `LECTURE-INTERMEDIAIRE-ACC2` → `VERDICT-INTERMEDIAIRE-ACC2`, avant `EPREUVE-FAMILLE-ACC2` |
| S-10 | « Critères de lecture gelés » | phrases « Lecture “accumuler” ([K] cycles joués) : … » | phrase intermédiaire : « Lecture intermédiaire “accumuler” ([K] cycles joués ; [n] premières tâches sur [N] ; lecture finale à venir) : … », même corps ; état non décisif : « … : la lecture intermédiaire ne conclut pas ; aucune estimation n'est sortie. » ; phrases finales : ajouter « (deux lectures : intermédiaire [état]) ». Audit de symétrie : ajouter « lectures discordantes ». « Ce qu'aucune issue ne permet » : ajouter « une troisième lecture ; dire une tendance à partir d'une lecture intermédiaire qui ne conclut pas » |
| S-11 | « Liste d'arrêt » | — | ajouter : un score de la seconde tranche ouvert avant `EPREUVE-FAMILLE-ACC2` : lecture finale invalide ; une borne ou une aire de la lecture intermédiaire communiquée alors que son état n'est pas décisif : nœud, réserve « intermédiaire ébruitée » |
| S-12 | « Puissance », effectif | puissance d'au moins 0,80 du plan à lecture unique | puissance d'au moins 0,80 du plan à deux lectures (« accumuler, propre » à l'une des deux) ; la simulation du temps 1 joue les deux lectures et écrit la part des issues dès la première |
| S-13 | « Suite des cycles », point 3 | « chaque cycle est **lu une seule fois**, à effectif fixé d'avance, sans ajout de tâches ni relecture » | « chaque cycle est **lu selon son plan de lectures scellé** (une ou deux), à effectifs fixés d'avance, sans ajout de tâches ni relecture » |
| S-14 | « Code neuf » ; devis | — | le paquet d'analyse porte les deux lectures, le cumul, l'énumération des états intermédiaires et finaux ; devis : une seconde pièce de relecture (environ deux heures de carte, 2 à 4 USD attendus — mon arithmétique, à refaire dans un brouillon neuf du devis) |
| S-15 (facultatif, nœud à part) | « Plan d'analyse », point 3 | la liste des 632 tâches est scellée fermée en une fois, avant `SONDES-ACC2` | la liste est scellée en deux tranches dans l'ordre que fixe la règle du tirage : d'abord les 32 tâches de distillation et les 250 premières d'évaluation, puis le reste. Je n'ai pas lu la règle du tirage : sa faisabilité est à confirmer par son auteur |

S-13 touche ce qui protège la règle « aucun run visant un signe positif » : c'est pour cela que le choix est un nœud.

## 6. Le 27 novembre : ce que la lecture intermédiaire permet de dire, et ce qu'elle ne permet pas

**6.1 Permis**, si la lecture intermédiaire et son verdict par un agent neuf existent : la phrase gelée de l'état intermédiaire, recopiée, avec « 250 premières tâches sur N ; lecture finale à venir » et le compte des cycles. Si elle ne conclut pas : « la première des deux lectures prévues ne conclut pas ; la seconde est en cours ; le plan, ses niveaux et ce choix ont été scellés avant toute donnée ».

**6.2 Non permis** : une taille d'effet ou une tendance quand elle ne conclut pas ; « rien » lu comme « pas d'effet » ; une ligne descriptive ; « H2 est confirmée », « G1 est en vue », « la sonde lit l'intention » ; une revendication tirée d'une issue positive tant que le point 1 des points à trancher (compte des cycles) n'est pas tranché ; quoi que ce soit sur un autre mode, un autre modèle, des actes épars.

**6.3 Calendrier, sans fard** (mon arithmétique sur les débits du devis ; avec le second témoin) :

| | une machine | trois machines de génération |
|---|---|---|
| première tranche (250 tâches), génération puis relecture | 36 à 41 heures | 19 à 23 heures |
| famille entière, 400 à 600 tâches (devis) | 53 à 87 heures | 29 à 50 heures (deux machines) |

Après la création viennent, pour chaque lecture, la validité, l'épreuve et la lecture (une demi-journée à un jour), puis le verdict (une demi-journée à un jour). De ton feu vert de dépense au verdict intermédiaire : **deux à trois jours et demi** ; au verdict final : deux à cinq jours et demi. Le gain est d'une demi-journée à deux jours.

Ce que le plan ne raccourcit pas : les deux verdicts qui ouvrent le temps 1 (la lecture de l'étape B bis repart avec un quatrième addendum et un module neuf) ; la conception et le gel de la sonde (un à sept jours) ; le code, contre-lu, avant le scellement ; les tâches fraîches. Il reste huit jours. **Pour une lecture intermédiaire le 27, le temps 1 doit s'ouvrir le 22 ou le 23 au plus tard, sans accroc ensuite.** Trois leviers sont à ta main et hors de ce plan : trois machines de génération ; l'extraction des tâches par tranche (S-15 : environ 340 papiers à garder au lieu de 760 pour la première lecture, à la réserve de 20 % du devis) ; la règle d'ouverture du temps 1 (point 14 des points à trancher, que je n'ai pas lu).

## 7. Condition : le choix entre les deux plans est fait par Lazar avant toute donnée

- **Décision** : le second cycle se lit-il une fois, ou deux fois selon ce plan ?
- **Enjeu** : une phrase à risque tenu pour le 27, contre un peu de puissance et de complexité ; et une exception écrite à « chaque cycle est lu une seule fois ».
- **Options** :
  - **A — lecture unique** (brouillon 3 tel quel). Avantage : rien à ajouter, puissance entière. Inconvénient : aucun résultat avant la famille entière.
  - **B — deux lectures, un cinquième du risque à 250 tâches** (ce texte). Avantage : première phrase une demi-journée à deux jours plus tôt, coût faible à la lecture finale. Inconvénient : ne conclut tôt que si l'effet dépasse nettement la marge ; une épreuve et une pièce de relecture de plus ; deux occasions de perdre la famille à l'épreuve.
  - **C — deux lectures, la moitié du risque à 250 tâches**. Avantage : un peu plus de chance de conclure le 27. Inconvénient : 0,02 à 0,07 de puissance perdue à la lecture finale, ou 13 % de tâches en plus.
- **Recommandation** : **B**, à condition que la simulation tienne ses critères ; confiance 0,6. Si le temps 1 ne peut pas s'ouvrir le 23, B ne donne rien le 27 mais reste sans regret : la première phrase vient quand même plus tôt.
- **Aucun défaut** : c'est un écart à la règle de lecture unique du cycle, donc un nœud.
- **Quand** : ton mot est inscrit par la ligne `PLAN-LECTURES-ACC2`, **avant `SONDES-ACC2`** (la simulation de puissance du temps 1 en dépend) et, en tout cas, avant `SCELLEMENT-ACC2` — donc avant qu'une instance, un adaptateur ou un épisode de la famille existe. Après cette ligne, ni le plan, ni la part, ni les 250 tâches, ni l'instant de coupure ne changent ; un changement est un cycle neuf. Si la ligne manque au scellement : plan à lecture unique.

## 8. Points ouverts

1. Cette option et son code ne sont pas contre-lus ; la section 4.3 tient lieu de préenregistrement de la simulation et doit l'être avant le jeu.
2. La simulation n'est pas jouée : rien ici n'établit que le plan tient son risque avec l'intervalle percentile réel ; seule l'arithmétique sous lois normales le dit.
3. L'épreuve sur signal planté à deux lectures (critères au niveau intermédiaire, double exposition du compte du signal nul) est décrite en une ligne (S-8) : à écrire en entier par le rédacteur du préenregistrement si tu retiens B.
4. Le monde de la frontière de l'écart n'éprouve durement le niveau que si la propreté y est presque toujours établie ; les comptes d'états du résultat le diront.
5. L'instant de coupure, les trois machines et S-15 sont à toi ; le devis de la seconde relecture est à refaire.
6. Les deux valeurs tabulées citées de mémoire (section 4.5) sont à vérifier sur une source empreintée ou par un logiciel établi.

## 9. Fichiers (empreintes dans les compagnons)

- cette option : `docs/notes/reconception-accumulation-cycle-2-v1/option-plan-sequentiel-cycle-2-v1-brouillon1.md` ;
- pièces : `docs/notes/reconception-accumulation-cycle-2-v1/pieces-option-sequentiel-v1/` — `calculs-option-sequentiel-v1.py`, `sortie-calculs-option-sequentiel-v1.txt`, `faire-configuration-simulation-sequentiel-v1.py`, `configuration-simulation-sequentiel-v1.json` ;
- code : `src/controle_ia/sequentiel_cycle2/` (`__init__.py`, `niveaux_v1.py`, `etats_v1.py`, `monde_gaussien_v1.py`, `monde_scores_v1.py`, `criteres_v1.py`, `simulation_v1.py`) ;
- essais : `tests/test_sequentiel_cycle2_niveaux_etats_v1.py`, `tests/test_sequentiel_cycle2_mondes_v1.py`, `tests/test_sequentiel_cycle2_simulation_v1.py`.

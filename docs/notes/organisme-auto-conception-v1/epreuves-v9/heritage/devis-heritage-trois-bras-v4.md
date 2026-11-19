# Question de l'héritage (N-073, § 1) — devis du plan à trois bras, par paliers — v4

- **Statut : pièce de travail, version 4.** Ce devis chiffre le plan `plan-heritage-trois-bras-corrige-v4.md` (même dossier) **palier par palier**, du moins cher au plus cher, avec ce que chaque palier permet de conclure, la règle écrite d'avance qui fait proposer le suivant, les variantes à deux, trois et cinq espèces, le test de mort par tentative, et la fiche de décision. Il n'engage rien : chaque palier payant part sur son propre préenregistrement scellé et contre-lu, sur un devis à sa taille finale et sur une ligne d'accord neuve.
- **Écrit par** : le rédacteur (modèle F), le 2026-11-19, à partir de 14:02Z (`date -u`) ; processeur seul, aucun appel, aucune dépense. Mandat : ligne `GO-2026-11-19-55` de `registres/go.md` ; demandes de la mère pour cette version (R-3851).
- **Version remplacée, gardée telle quelle (règle R12)** : `devis-heritage-trois-bras-v3.md` (`d58584273bf6ea8cd0b5128452aac67dc96219d208cdaaf51949a919774d807c`). Vérification appliquée : `verification-plan-heritage-trois-bras-corrige-v3-v1.md` (`b030e2749e79b6de1fc83feb8ca06dc12cdb18eba8d9a3483659d101d60986b5`), verdict « scellable », quatre constats de forme ; un seul touche le devis (l'en-tête dit où se trouve le fichier que cite la ligne 67). Versions antérieures gardées de même : v2 (`988da4d18bc1c126f6b5daa694e593b10200e1a38c9e7c57697d329f962b84b3`), v1 (`af51c493494b6be2ab2c599b3b8f579fa7cdbbe46fa305a6a140b7d5e462fd2e`) ; leurs différentiels sont aux § 10 et § 11 du devis v3. Le différentiel v3 → v4 est au § 11 ci-dessous.
- **Principes tenus.**
  - Ligne `GO-2026-11-19-60` (mot de Lazar, verbatim : « le cout ne doit pas etre un fcateur limitant s'il ameliore considerablement l'organisme ») et ligne `GO-2026-11-19-69` (lue sur `main` ; pour les critères de sélection des cartes, le coût « n'élimine aucune carte et ne sert qu'à ordonner le passage »). **Le mandat de la version 4 transmet la règle pour l'héritage : le coût est rapporté sans réduction ; il sert à ordonner les paliers, il n'élimine pas.** C'est un fait transmis, que ce devis rapporte ; aucune des deux lignes ne nomme l'héritage au registre (plan, § 13, réserve 10).
  - N-045, version 2 (`docs/decisions/decision-N-045-v2.md`, `c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d`), point 4 : « le bon marché d'abord, le cher sur preuve ». D'où l'ordre des paliers.
  - Ligne `GO-2026-11-19-67` (la ligne est lue sur `main`) : ordre de passage des épreuves, version 3 (`docs/notes/organisme-auto-conception-v1/epreuves-v9/ordre-de-passage-epreuves-v9-v3.md`, `b19f550b525fe5696321167bd43a35fa5ece180fd2f97dad5dfc6e970a8c0f67` ; ce fichier est sur la branche `lot/compte-organisme-v1`, commit `7e140479`, et non sur `main`), option (a) : le devis de l'héritage est présenté dès qu'il est écrit ; le branchement des tests de mort réels est « éteint par défaut, son activation restant un nœud ».
  - Mot de Lazar, transmis par le mandat : les essais avec expériences et les tests de mort tranchent, jamais un juge (N-058). Tenu ici : aucun chiffre, aucune règle de passage, aucune variante de ce devis ne dépend du verdict d'un juge ; les règles de passage ne lisent que des épreuves exécutées, l'oracle du monde planté et des coûts mesurés.
- **Calcul.** Deux programmes, même dossier, tous deux rejoués deux fois avec des sorties identiques à l'octet :
  - `calcul_devis_heritage_v2.py` (`5d21b393f03f3e859241d97dea8347937596422c42f6b9f3cc4e5f5661b1a1c9`), sortie `calcul-devis-heritage-v2.json` (`132a07649dd6d572ad50e5bc6c41a73fee9d54a8bcceef996192fb886b1dca6b`) : totaux par étage, appels perdus, pilote, rangs signés. **Aucun de ses chiffres ne change.** Il n'existe pas de version 3 du calcul.
  - **neuf** : `calcul_devis_heritage_v4.py` (`2b5bbf4e05fe7a1e476a3bcfdadcd7ae4a61a4c3b301ed986388c68f30a392a9`), sortie `calcul-devis-heritage-v4.json` (`f503c224de06bfa9760e63788ce101e915e6ef1ec566d012fa8ed91ef2240d5c`) : les paliers, le test de mort par tentative, les variantes. Mêmes constantes de coût et mêmes formules que la v2 ; il désigne les espèces par un numéro et n'écrit aucun nom de rôle.
- **Source des coûts** : manifeste de fin du lanceur de la course d'auto-conception v9, `runs/20261119-094145-course-auto-conception-v9/manifeste-lanceur-fin.json` (branche `lot/compte-organisme-v1`, sha256 `28bc36df390d8481fb5bd9118cf764843ffea60856412d825ecbf08e7cee5be7`), champs `cout_reel.par_role_usd` et `cout_reel.appels_par_role`. La course entière a coûté 72,50 USD, soit 1,8 fois son devis.
- **Montants** : en USD, arrondis à la dizaine, sauf le palier 1, donné au dollar.

## 0. Verdict

1. **La dépense se joue en sept temps, du moins cher au plus cher** (§ 3) : deux paliers à 0 USD, puis un essai réel du test de mort à une centaine de dollars, le pilote de bruit en deux temps, les sources à dose nulle, enfin les sources à dose non nulle, qui seules portent les deux contrastes décisifs. Chaque passage a sa règle écrite d'avance (§ 4).
2. **À la composition de la course v9 (cinq espèces), les propositions seules coûtent de l'ordre de 20 530 USD en estimation** pour tous les paliers, 35 260 USD en cas haut, 56 420 USD au pire. Ce sont les totaux de la version 3, hors aiguilleur et juges à modèle, plus les 59 USD du palier 1.
3. **Le test de mort par tentative n'a aucun coût mesuré à ce jour** (§ 5). Chiffré sur les bornes écrites dans le code de l'étage, il ajoute entre 1 970 USD (un tour de l'expérimentateur au prix prudent) et 19 740 USD (plafonds par défaut de l'expérimentateur et du lecteur témoin) en estimation, à cinq espèces. **Aux plafonds, il pèse autant que les propositions.** C'est la première chose à mesurer, et c'est l'objet du palier 1.
4. **Ce que l'on sait avant de payer cher** : après 0 USD, si l'instrument est lisible ; après environ 115 USD, ce que coûte et ce que vaut un test de mort réel sur un monde planté ; après environ 4 800 USD de propositions, le bruit et le nombre de sources ; après environ 10 000 USD, si la lecture est valide chez de vrais proposeurs. **Aucune information sur l'héritage lui-même n'arrive avant le dernier palier** : c'est la limite de ce découpage, et la raison de la voie « en escalier » du § 6.
5. **Recommandation du rédacteur** (§ 9) : jouer les paliers dans l'ordre, cinq espèces aux paliers décisifs, sans aiguilleur ni juges à modèle ; confiance 0,55. Les cinq nœuds du plan restent à Lazar ; ma recommandation et ma confiance pour chacun sont au § 9.

## 1. Coûts réels de la course v9, par rôle

| rôle | appels | coût réel (USD) | par appel (USD) |
|---|---|---|---|
| proposeur de l'espèce 1 | 11 | 4,17 | 0,38 |
| proposeur de l'espèce 2 | 11 | 4,75 | 0,43 |
| proposeur de l'espèce 3 | 11 | 7,43 | 0,68 |
| proposeur de l'espèce 4 | 11 | 17,58 | 1,60 |
| proposeur de l'espèce 5 | 11 | 24,72 | 2,25 |
| **étape de proposition** | **55** | **58,64** | — |
| aiguilleur | 96 | 4,59 | 0,048 |
| juge de l'espèce 3 | 94 | 6,86 | 0,073 |
| juge de l'espèce 1 | 94 | 2,41 | 0,026 |
| **course entière** | — | **72,50** | — |

**Table de correspondance.** Ce devis n'écrit aucun nom d'espèce. Les espèces sont numérotées par le coût réel croissant de leur rôle de proposeur dans le manifeste de fin (chemin et empreinte en tête), champ `cout_reel.par_role_usd`, parmi les cinq rôles dont le nom commence par `prop-` : l'espèce 1 est le rôle au coût le plus bas (4,17 USD), l'espèce 5 le rôle au coût le plus haut (24,72 USD). Les deux juges sont les rôles dont le nom commence par `juge-` et finit comme le rôle de proposeur de l'espèce 3 et de l'espèce 1. Les cinq coûts sont distincts : la numérotation est sans ambiguïté.

Ces coûts sont ceux d'une course dont les cartes proposent des mécanismes pour l'organisme. Sur un monde planté, où les tentatives sont des lois, les invites et les réponses peuvent avoir une autre longueur : l'unité est un ordre de grandeur. Le palier 1 puis le pilote rendent les coûts réels.

## 2. L'unité : une génération d'un bras

Le plan fixe un budget en dollars égal par bras ; le bras qui lit un registre paie sa lecture sur ce budget et joue moins d'appels : **le registre n'ajoute aucune ligne au devis**. L'unité est le coût d'une génération de propositions, à onze appels par espèce comme à la v9.

| composition des proposeurs | appels | tentatives attendues, à la proportion de la v9 | coût d'une génération d'un bras (USD) | aiguilleur et deux juges à modèle, en plus (USD) |
|---|---|---|---|---|
| A — les cinq espèces de la v9 | 55 | 94 | 58,64 | 13,86 |
| B — trois espèces (1, 2 et 3) | 33 | 56 | 16,35 | 8,31 |
| C — les deux espèces les moins chères (1 et 2) | 22 | 38 | 8,92 | 5,54 |

Par source, en générations de bras : 15 pour une source à dose non nulle (3 de course source, puis 3 bras × 4) ; 11 pour une source à dose nulle (3, puis 2 bras × 4) ; 27 pour une source de pilote (3, puis 3 bras × 2 jumelles × 4).

**Appels perdus par le bras qui lit un registre** : la table du § 2 bis du devis v3 reste valable sans changement (champ `appels_perdus_par_le_bras_3_en_generation_1` de la sortie v2) ; au seul repère disponible, non vérifié, le bras 3 perdrait 7 appels sur 55 à la première génération.

## 3. La dépense par paliers

Composition A, estimation (12 sources à dose non nulle, 8 à dose nulle, 3 sources de pilote). « Propositions » : le coût des appels des proposeurs. « Avec le test de mort » : le même cumul, plus le test de mort de toute tentative, à trois valeurs écrites du § 5 — 0,06 USD (un tour au prix prudent), 0,60 USD (plafonds par défaut de l'expérimentateur et du lecteur témoin), 0,90 USD (borne du tour fermé et lecteur témoin). Champ `paliers` de la sortie v4.

| palier | ce qui se joue | générations de bras | propositions | cumul des propositions | cumul avec le test de mort, à 0,06 / 0,60 / 0,90 USD par tentative |
|---|---|---|---|---|---|
| **0a** | lecture du code de l'étage et essai hors ligne d'un test de mort sur une loi plantée | 0 | 0 | 0 | 0 |
| **0b** | étage sur processeur (plan, § 7) | 0 | 0 | 0 | 0 |
| **1** | essai réel du test de mort : une génération, un monde planté, toute tentative éprouvée | 1 | 59 | 59 | 64 / 115 / 143 |
| **2a** | pilote de bruit, deux sources, six paires de jumelles | 54 | 3 170 | 3 230 | 3 540 / 6 330 / 7 880 |
| **2b** | pilote de bruit, troisième source, neuf paires en tout | 27 | 1 580 | 4 810 | 5 270 / 9 430 / 11 750 |
| **3** | étage payant, sources à dose nulle (bras 2 et 3) | 88 | 5 160 | 9 970 | 10 930 / 19 560 / 24 350 |
| **4** | étage payant, sources à dose non nulle (trois bras) | 180 | 10 560 | 20 530 | 22 500 / 40 270 / 50 140 |
| *5* | *témoins jugés, pour information : aiguilleur et deux juges à modèle sur les 268 générations de bras de l'étage* | — | *3 710* | — | — |
| *6* | *un bras de diagnostic (12 sources × 4 générations de bras) ; six sont décrits* | *48* | *2 810 par bras* | — | — |

**Cas haut et pire, composition A, propositions seules** (16 sources, 12 à dose nulle, 4 sources de pilote ; coût de l'unité relevé d'un quart, puis doublé) :

| palier | haut | pire |
|---|---|---|
| 1 | 73 | 117 |
| 2a | 3 960 | 6 330 |
| 2b (deux sources de plus) | 3 960 | 6 330 |
| 3 | 9 680 | 15 480 |
| 4 | 17 590 | 28 150 |
| **cumul** | **35 260** | **56 420** |
| cumul avec le test de mort, à 0,06 / 0,60 / 0,90 USD | 38 650 / 69 170 / 86 130 | 61 840 / 110 670 / 137 800 |

Dans ces deux cas le programme applique le même facteur à la ligne du test de mort : il couvre alors un nombre de tentatives plus grand que prévu, non un dépassement d'un plafond, qui ne peut pas être dépassé. La dernière case est donc une borne très large. **Un plafond d'arrêt gelé à chaque préenregistrement borne la dépense de chaque palier en tout état de cause.**

**Ce que chaque palier permet de conclure, et ce qu'il ne permet pas.**

| palier | permet de conclure | ne permet pas de conclure |
|---|---|---|
| 0a | si l'étage des tests de mort exécute, sans réécriture, un engagement sur une loi d'un monde planté ; si le comparateur de l'oracle apparie sans modèle (plan, § 13, réserve 1) | un coût ; la conduite d'un vrai expérimentateur |
| 0b | si l'instrument est lisible ; les nombres n et m de sources ; la table de puissance ; ce que coûte le repli du nœud 2 ; l'effet du seul coût de lecture | le signe ou la taille de l'héritage chez de vrais proposeurs ; le bruit réel ; un coût réel |
| 1 | le coût réel du test de mort par tentative, par espèce ; la part de tentatives non exécutables ; la répartition des classes d'issue ; les coûts par appel sur monde planté ; la taille d'un registre d'une génération, donc la part que prend sa lecture ; pour chaque espèce, les lois vraies plantées retrouvées et leur coût sur ce monde (N-058 : la composition se juge sur l'oracle et le coût) | rien de l'héritage, de la tenue, ni du bruit entre deux courses ; un seul monde, une seule génération : les comptes par espèce sont une description, pas une comparaison |
| 2a | l'écart-type entre deux courses identiques, sa borne haute à 1,92 fois l'estimation ; la part de différences nulles ; un premier nombre de sources | aucune différence entre bras : le plan interdit de la calculer (plan, § 8.0) |
| 2b | la borne resserrée à 1,65 fois l'estimation ; le nombre de sources retenu ; le devis final de l'étage | comme 2a |
| 3 | si la lecture est valide chez de vrais proposeurs : un écart d'héritage positif apparaît-il là où la dépendance plantée ne peut pas le produire ; l'effet du coût de lecture chez de vrais proposeurs | rien de l'héritage lui-même ; une règle de validité qui ne se déclenche pas ne prouve pas l'absence d'un effet de forme |
| 4 | **la réponse** : héritage et tenue, « établi », « non lu comme succès », « effet négatif établi » ou « non établi », par la table gelée du plan (§ 8.3) | tout ce que le plan écarte (§ 10) : rien hors des mondes plantés, rien d'un savoir-faire général, rien d'un registre à coût nul |
| 5 | rien pour un critère ; une description du volet des témoins jugés de N-058 | quoi que ce soit sur un bras ou sur l'héritage |
| 6 | pourquoi un effet établi existe (contenu ou présence, résultats ou prédictions, canal caché) | rien si aucun contraste n'est établi |

## 4. Les règles de passage, écrites d'avance

Elles sont au plan (§ 8.4) ; les voici sous forme de règle. **Une règle fait proposer le palier suivant ; elle ne dépense rien.** Chaque palier payant demande son préenregistrement scellé et contre-lu, son devis récrit avec ce que le palier précédent a mesuré, et sa ligne d'accord. Les valeurs chiffrées sont des propositions du rédacteur, à geler au préenregistrement de chaque palier. **Aucune règle n'arrête un palier pour son coût** : un coût mesuré plus haut que prévu récrit les devis suivants et change l'ordre conseillé (§ 6), rien de plus.

| passage | règle | sinon |
|---|---|---|
| 0a → 0b | l'étage exécute hors ligne un engagement sur une loi d'un monde planté, et le comparateur de l'oracle apparie sans modèle | la voie (c) du plan (§ 3.0), une épreuve neuve, est portée à Lazar ; rien ne se préenregistre avant son mot |
| 0b → 1 | issue « lisible, à n sources et m sources à dose nulle » (plan, § 7) ; et le branchement des tests de mort réels est livré, puis activé par le mot de Lazar | « à reconstruire » ou « non lisible » : aucun palier payant ; reconstruction sur processeur, à 0 USD, sans borne de cycles |
| 1 → 2a | la moitié au moins des tentatives reçoit « tient » ou « ne tient pas » ; aucune de ces deux classes ne porte plus de 95 % des tentatives éprouvées ; les gardes tiennent sur de vraies sorties (tranche d'épreuve jamais servie, entrée de l'expérimentateur) | arrêt : un test qui n'exécute pas, ou qui rend toujours la même classe, ne peut rien inscrire d'utile dans un registre ; la forme des engagements ou la voie (c) sont portées à Lazar |
| 2a → 2b | toujours, sauf deux cas | (i) le nombre de sources lu à la borne haute à six paires est déjà le plancher de dix : la troisième source ne peut plus l'abaisser, passage direct au palier 3. (ii) Aucun nombre n'est rendu même sans la borne : arrêt, porté à Lazar |
| 2 → 3 | la règle du plan (§ 8.0) rend un nombre de sources ; devis de l'étage récrit à sa taille finale | aucun nombre : porté à Lazar tel quel |
| 3 → 4 | la règle de validité ne se déclenche pas à dose nulle ; troncature, chaîne d'empreintes et générateur tiennent | lecture invalide, rapportée telle quelle ; le palier 4 ne se joue pas sur ce dessin ; toute suite est un préenregistrement neuf, sur des sources neuves |
| 4 → 6 | lecture valide, et un contraste au moins « établi » ou « effet négatif établi » | les bras de diagnostic ne sont pas proposés par défaut |
| vers 5 | aucune règle : le palier 5 ne se joue que si Lazar le demande, après la lecture du palier 4, sur les tentatives scellées | — |

Trois précisions.

- **Les paliers 3 et 4 sont un seul étage, sous un seul préenregistrement**, scellé avant le premier appel du palier 3. Au palier 3, seules les conditions de lecture sont calculées, sur les sources à dose nulle ; les deux contrastes décisifs n'existent pas encore. La règle est fixée d'avance et ne vise aucun signe (règle R3).
- **Prix de ce découpage** : les sources à dose nulle et les autres ne se jouent plus dans la même période. Si un fournisseur change un modèle entre les deux temps, la validité a été lue sur un autre état des proposeurs ; les versions servies sont relevées au manifeste des deux temps.
- **Le palier 1 est une mesure, pas une épreuve décisive**, mais il décide d'un passage : il part sous un préenregistrement court (ce qui est mesuré, les trois seuils de la règle, le plafond d'arrêt), contre-lu.

## 5. Le test de mort par tentative

**Il ne peut pas être chiffré sur un coût réel aujourd'hui, et voici pourquoi.** Aucune session réelle d'écriture de script et d'exécution n'a été jouée par l'étage des tests de mort sous le lanceur de la course d'auto-conception :

- le rapport du développeur du rang 0 (`docs/notes/organisme-auto-conception-v1/epreuves-v9/rang-0-branchement/rapport-developpeur-rang-0-v1.md`, `966a387032bc45109d82942760666b9fe89c5204badb8ec9ae2c6968df6856aa`, branche `lot/compte-organisme-v1`, commit `50de58b5`) écrit que le rang 0 « ne débloque aujourd'hui aucun étage réel » : il faut encore une version de l'orchestrateur, un lanceur neuf, un additif, un devis et une machine jetable ;
- à l'essai à blanc, l'étage n'a joué qu'un exécuteur factice et a refusé les deux cartes candidates, faute de champ de test dans les cartes de la course d'auto-conception : aucune tentative n'y a été éprouvée ;
- j'ai cherché un coût réel d'une session de test de mort dans `registres/depenses.md` et dans `runs/`, par recherche de mots : je n'en ai trouvé aucun. La seule dépense qui nomme l'expérimentateur est un tour de discussion sur son choix, qui n'est pas une session de test. Je n'ai pas ouvert les dossiers que le mandat interdit ; s'il existe ailleurs une mesure, je ne l'ai pas vue.

**Il est donc chiffré sur les bornes écrites**, comme le mandat le demande. Elles sont dans le code de l'organisme (`/home/user/ideation-organism`, commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`) ; je n'ai lu que ces constantes et le point C de l'en-tête du second fichier :

| valeur écrite | où | USD par tentative |
|---|---|---|
| prix prudent d'un tour de l'expérimentateur | `orchestrator/pole/tour_ferme_v64.py` (`35a8294e24c870685435b990d6c03cd33cb5b2e288bcb2cc91cd9af04679c2da`), en-tête, point C : « 12 × 0,06 = 0,72 USD » | 0,06 par tour |
| nombre maximal de tours par tentative | `orchestrator/pole/tests_de_mort.py` (`fc5d3507b33e13094d64751ff2b4564ba5ed4c238f93aaae808c458b3c123252`), `TOURS_MAX_PAR_FICHE` | 12 tours, soit 0,72 au prix prudent |
| plafond par défaut des sessions de l'expérimentateur, noté « supposé » dans le code | même fichier, `BUDGET_TEST_USD_DEFAUT` | 0,50 |
| plafond par défaut de la session du lecteur témoin, noté « supposé » | même fichier, `BUDGET_LECTEUR_USD_DEFAUT` | 0,10 |
| borne par carte de l'expérimentateur au tour fermé | `tour_ferme_v64.py`, `BUDGET_EXPERIMENTATEUR_PAR_CARTE_USD` | 0,80 |

La configuration d'essai du rang 0 (`configuration-interrupteurs-course-auto-conception-v1.json`, même dossier que le rapport, `bb4ecbfb24f43d356474d301052ff8df80f829bc7a8b6c0365b64004f8608c3c`) porte 0,50 et 0,20 USD, trois exécutions par carte et 120 secondes par exécution ; le rapport dit que ce sont « celles de l'essai à blanc, pas un réglage ».

**Ce sont des plafonds et un prix prudent, pas des mesures.** Un plafond dit ce qu'une tentative ne peut pas dépasser ; il ne dit pas ce qu'elle coûte. La fourchette qui en sort, par tentative : **de 0,06 USD (un tour) à 0,60 USD (les deux plafonds par défaut), et jusqu'à 0,90 USD à la borne du tour fermé, lecteur témoin compris.**

**Ajout du test de mort, par palier, en estimation** (champ `ajout_du_test_de_mort_usd` de la sortie v4 ; toute tentative de toute génération de bras est éprouvée, génération finale comprise) :

| palier | tentatives attendues (A) | A, à 0,06 / 0,18 / 0,50 / 0,60 / 0,90 USD | B, à 0,06 / 0,60 / 0,90 | C, à 0,06 / 0,60 / 0,90 |
|---|---|---|---|---|
| 1 | 94 | 6 / 17 / 47 / 56 / 85 | 3 / 34 / 51 | 2 / 23 / 34 |
| 2a | 5 076 | 300 / 910 / 2 540 / 3 050 / 4 570 | 180 / 1 830 / 2 740 | 120 / 1 220 / 1 830 |
| 2b | 2 538 | 150 / 460 / 1 270 / 1 520 / 2 280 | 90 / 910 / 1 370 | 60 / 610 / 910 |
| 3 | 8 272 | 500 / 1 490 / 4 140 / 4 960 / 7 440 | 300 / 2 980 / 4 470 | 200 / 1 990 / 2 980 |
| 4 | 16 920 | 1 020 / 3 050 / 8 460 / 10 150 / 15 230 | 610 / 6 090 / 9 140 | 410 / 4 060 / 6 090 |
| **tous** | **32 900** | **1 970 / 5 920 / 16 450 / 19 740 / 29 610** | **1 180 / 11 840 / 17 770** | **790 / 7 900 / 11 840** |

Lecture. À cinq espèces, les propositions coûtent 20 530 USD ; le test de mort, entre un dixième de cette somme et une fois et demie. À deux espèces, les propositions coûtent 3 120 USD, et le test de mort aux plafonds en coûterait deux à quatre fois plus : **plus la composition est bon marché, plus le test de mort domine.** Le plan prévoit déjà le cas où le budget d'un bras ne suffit pas à tout éprouver (statut « non éprouvée (budget) », tentatives tirées par graine ; plan, § 3.0) ; c'est une conséquence, non un levier que ce devis recommande.

**Ce qui reste hors chiffre.** Le temps et la location de la machine jetable qui exécute les scripts : à trois exécutions de 120 secondes au plus par tentative, 32 900 tentatives font au plus 3 290 heures d'exécution mises bout à bout (calcul à la main sur les valeurs de la configuration d'essai ; borne, non prévision). Il faudra des exécutions en parallèle, et un devis de location.

**Le palier 1 le mesure.** Une génération à cinq espèces, soit environ 94 tentatives : 59 USD de propositions, plus au plus 56 USD de tests aux plafonds par défaut, soit **de l'ordre de 115 USD en estimation ; plafond d'arrêt proposé pour ce palier : 290 USD** (le cas pire à la borne du tour fermé : 117 USD de propositions et 169 USD de tests). La location de la machine s'y ajoute.

## 6. Les variantes à deux, trois et cinq espèces

Mêmes paliers, mêmes nombres de sources, estimation. Champ `paliers` de la sortie v4.

| palier | A — cinq espèces | B — trois espèces | C — deux espèces |
|---|---|---|---|
| 1 | 59 | 16 | 9 |
| 2a | 3 170 | 880 | 480 |
| 2b | 1 580 | 440 | 240 |
| 3 | 5 160 | 1 440 | 780 |
| 4 | 10 560 | 2 940 | 1 610 |
| **cumul des propositions** | **20 530** | **5 720** | **3 120** |
| cumul avec le test de mort, à 0,06 / 0,60 / 0,90 USD | 22 500 / 40 270 / 50 140 | 6 910 / 17 570 / 23 490 | 3 910 / 11 020 / 14 970 |
| cumul des propositions, haut / pire | 35 260 / 56 420 | 9 830 / 15 730 | 5 360 / 8 580 |
| palier 5, pour information | 3 710 | 2 230 | 1 490 |
| palier 6, par bras de diagnostic | 2 810 | 780 | 430 |

**Ce que chaque variante fait perdre.**

| variante | ce qu'elle fait perdre |
|---|---|
| **A — cinq espèces** | **De la puissance par dollar.** Pour le prix du palier 4 de A (10 560 USD), B joue 43 sources à dose non nulle et C en joue 78, contre 12 (champ `a_depense_egale_du_palier_4_de_A`). A est aussi la variante où une erreur de montage coûte le plus : la course v9 a coûté 1,8 fois son devis, et ni plusieurs générations ni les tests de mort réels n'ont encore été joués. |
| **B — trois espèces (1, 2 et 3)** | **La réponse ne vaut plus pour l'organisme tel qu'il existe.** Les deux espèces retirées font 40 % des appels et 72 % du coût de proposition (champ `part_des_deux_especes_les_plus_cheres_dans_A`). Une génération de bras porte 56 tentatives au lieu de 94 : des scores en comptes plus petits, plus de différences nulles, donc peut-être plus de sources ; le palier 0b le dit. Et rien n'établit qu'une espèce retirée lit un registre comme une espèce gardée : l'héritage peut dépendre de qui lit. Retirer des espèces est un changement de composition, donc un accord de Lazar ; N-058 veut qu'il se juge sur l'oracle du monde planté et le coût, et l'oracle par espèce sur monde planté n'existe pas avant le palier 1. |
| **C — deux espèces (1 et 2)** | **Tout ce que B fait perdre, en plus fort**, et la diversité des proposeurs (N-044) : 38 tentatives par génération de bras ; une réponse qui ne vaut que pour les deux espèces les moins chères. Le test de mort y pèse le plus lourd devant les propositions (§ 5). |

**Une quatrième voie, « en escalier » : tout le dessin à deux espèces d'abord, puis à cinq.** Les paliers 2a à 4 se jouent une première fois en composition C (3 110 USD de propositions, de 3 900 à 11 000 USD avec le test de mort), puis en composition A sous un préenregistrement neuf.

- *Ce qu'elle apporte* : une première réponse sur l'héritage lui-même, sur de vrais proposeurs, pour environ le sixième du prix ; le montage entier éprouvé une fois (plusieurs générations, registre lu, tests de mort) avant d'y engager 20 000 USD ; des coûts mesurés pour le devis de A.
- *Ce qu'elle fait perdre* : la réponse en C ne se transporte pas à A, dans aucun sens — « établi » à deux espèces ne dit pas que cinq espèces héritent, « non établi » ne dit pas qu'elles n'héritent pas ; le bruit mesuré en C ne dimensionne pas A, qui garde son pilote ; aucune source n'est réemployée ; le total monte d'environ 15 % en propositions, et le calendrier s'allonge d'un étage entier. Jouer A après un « non établi » en C doit être écrit d'avance, pour ne viser aucun signe (règle R3).
- *Quand je la recommanderais* : si le palier 1 mesure un test de mort à plus de 0,25 USD par tentative. À ce prix, le test ajoute plus de 8 200 USD à la voie A (40 % des propositions), et l'ensemble passe 28 000 USD en estimation : éprouver le montage à bas prix d'abord vaut alors nettement ses 15 %. C'est un seuil de rédacteur, écrit ici pour être tenu ; il ordonne les voies, il n'en retire aucune.

## 7. Compte des générations de bras, et variantes de dessin

Le compte par étage de la version 3 est inchangé (devis v3, § 3 et § 4) : pilote 81 générations de bras, étage payant 268, total 349 en estimation ; 108, 372 et 480 en cas haut. Le palier 1 en ajoute une.

| poste (composition A, sans aiguilleur ni juges) | générations de bras | estimation | haut | pire |
|---|---|---|---|---|
| palier 1 | 1 | 59 | 73 | 117 |
| pilote de bruit (paliers 2a et 2b) | 81 (108 en cas haut) | 4 750 | 7 920 | 12 670 |
| étage payant (paliers 3 et 4) | 268 (372 en cas haut) | 15 720 | 27 270 | 43 630 |
| **total des propositions** | **350 (481)** | **20 530** | **35 260** | **56 420** |

**Une source de plus** (A) : à dose non nulle, 880 USD ; à dose nulle, 650 USD ; de pilote, 1 580 USD. Pour B : 250, 180 et 440 USD ; pour C : 130, 100 et 240 USD.

**Selon le nombre de sources à dose non nulle** (étage payant hors pilote, huit sources à dose nulle ; champ `variantes_de_contraste_etage_hors_pilote_estimation`) :

| sources à dose non nulle | générations de bras | A | B | C | ce que le nombre permet |
|---|---|---|---|---|---|
| 6 | 178 | 10 440 | 2 910 | 1 590 | plancher technique à **un seul** contraste décisif : conclut seulement si les six écarts ont le même signe (nœud 4) |
| 10 | 238 | 13 960 | 3 890 | 2 120 | plancher du plan à deux contrastes |
| 12 | 268 | 15 720 | 4 380 | 2 390 | recommandation du plan : dix différences utiles si deux sont nulles |
| 16 | 328 | 19 240 | 5 360 | 2 920 | cas haut, si la règle du pilote relève le nombre |

Ces nombres ne sont pas choisis par le devis : n sort de la règle du pilote, m de l'étage sur processeur.

## 8. Ce qui n'est pas chiffré, et les leviers

**Non chiffré.**
1. **Le coût réel du test de mort par tentative** : borné au § 5, mesuré au palier 1.
2. **La machine jetable** qui exécute les scripts : location et temps (§ 5).
3. **Le branchement** : la version de l'orchestrateur et le lanceur neuf que le rapport du rang 0 demande ; du code sur processeur, sans dépense, qui précède le palier 1.
4. **L'audit du registre par un lecteur d'une autre lignée**, un appel par génération de bras qui tient un registre (plan, § 1) : au plus 349 appels, petit devant l'unité.
5. **La longueur réelle des appels sur monde planté**, et **les appels sans sortie exploitable** (jusqu'à 3 sur 11 pour une espèce à la v9) : le cas haut les couvre par son quart de marge, sans garantie.
6. Les préenregistrements, contre-lectures et verdicts, faits par des sous-agents de la session.

**Leviers, avec ce que chacun ferait perdre.** Le coût n'éliminant rien, je n'en recommande aucun pour son prix ; deux sont des nœuds de Lazar.

| levier | effet | ce qui serait perdu |
|---|---|---|
| composition B ou C | divisé par 3,6 ou par 6,6 en propositions | § 6 ; accord de Lazar |
| un seul contraste décisif (nœud 4) | plancher à six sources ; au plus 5 280 USD de moins que douze sources (A) | six signes égaux exigés ; la tenue devient descriptive ; le bras 1 se joue quand même |
| dix sources au lieu de douze | 1 760 USD de moins (A) | la marge pour les différences nulles |
| pilote arrêté à six paires | 1 580 USD de moins (A) | borne à 1,92 fois l'estimation au lieu de 1,65 : plus de sources à l'étage, donc souvent plus cher au total ; la règle du § 4 ne l'arrête que si cela ne change rien |
| course source d'une génération | 40 générations de bras de moins | un registre hérité mince, donc un effet attendu plus petit |
| palier 5 non joué | 3 710 USD de moins (A) | une description du volet des témoins jugés ; aucun critère n'en dépend |
| moins de onze appels par espèce | proportionnel | moins de tentatives, scores plus discrets |

## 9. Décision pour Lazar

**Décision.** Engager la question de l'héritage par paliers, chacun sur sa ligne d'accord, en commençant par les deux paliers à 0 USD ; et, pour que le premier se préenregistre, trancher le nœud 1.

**Enjeu.** Le plan répond à la question de N-073, § 1, sous la lettre du complément 3, mais sa réponse n'arrive qu'au dernier palier, après de l'ordre de 20 500 USD de propositions à cinq espèces, et entre 2 000 et 20 000 USD de tests de mort dont personne ne connaît encore le coût réel. Les paliers font payer d'abord ce qui peut arrêter la suite à bas prix : l'instrument (0 USD), le test de mort réel (une centaine de dollars), le bruit, puis la validité. Aucune dépense n'est demandée aujourd'hui.

**Options.**
- **(a) Les paliers dans l'ordre, cinq espèces aux paliers décisifs, sans aiguilleur ni juges à modèle.** Avantage : la réponse vaut pour l'organisme tel qu'il existe ; quatre points d'arrêt écrits d'avance avant le palier le plus cher ; la composition peut encore se discuter après le palier 1, sur l'oracle et le coût. Inconvénient : de l'ordre de 22 500 à 40 300 USD en estimation, tests de mort compris, et 56 400 USD de propositions au pire ; rien sur l'héritage lui-même avant la fin.
- **(b) Les paliers 0a, 0b et 1 seulement pour l'instant** (0 USD, puis de l'ordre de 115 USD, plafond 290), tout le reste se décidant à leur lecture. Avantage : presque rien n'est engagé, et les deux inconnues qui pèsent le plus — l'instrument et le coût du test de mort — sont levées. Inconvénient : le pilote ne se prépare pas en parallèle ; quelques jours de plus.
- **(c) L'escalier : après les paliers 0 et 1, tout le dessin à deux espèces, puis à cinq** (§ 6). Avantage : une première réponse sur l'héritage et un montage éprouvé pour le sixième du prix. Inconvénient : cette réponse ne se transporte pas à cinq espèces ; environ 15 % de plus au total ; un étage de plus au calendrier.

**Recommandation du rédacteur.** (a), dont (b) est le début : accord de principe sur l'ordre des paliers et leurs règles, et mot neuf à chaque palier payant. **Confiance 0,55.** Elle passe à (c) si le palier 1 mesure un test de mort à plus de 0,25 USD par tentative (§ 6). Ce que la version 3 recommandait et que je ne recommande plus : jouer l'aiguilleur et les juges à modèle à l'étage payant ; ils ne servent aucun critère, et le mot de Lazar est que les épreuves tranchent, jamais un juge.

**Défaut.** Aucun : ce sont des nœuds et des dépenses. Le mandat `GO-2026-11-19-55` s'arrête, pour l'héritage, au plan corrigé et au devis.

### Les cinq nœuds du plan (§ 12, questions 1 à 5) — ils restent à Lazar

Aucun n'a de défaut. Pour chacun : ma recommandation, ma confiance, et ce qui me ferait changer.

1. **L'épreuve programmée est-elle bien les tests de mort ?**
   Recommandation : **oui, la voie (b)**, sous réserve du palier 0a ; et l'activation du branchement donnée palier par palier, d'abord pour le seul palier 1. **Confiance 0,7.**
   Raison : c'est l'épreuve de l'organisme, exécutée, à verdict calculé par le noyau, la même dans les trois bras ; elle ne fait entrer aucun juge dans le registre. Ce qui me ferait changer : un palier 0a qui montre que l'étage n'exécute pas une loi d'un monde planté sans réécriture, ou un palier 1 où moins de la moitié des tentatives s'exécutent ; alors la voie (c).
2. **`resultat` et `gardee` peuvent-ils être servis à la génération suivante ?**
   Recommandation : **oui, servis**, et le dire comme une lecture de la garde : elle interdit les verdicts de juge et la sélection des survivants, non la classe d'issue d'une épreuve exécutée que le complément 3 nomme dans l'objet. **Confiance 0,55.**
   Ce qui me ferait changer : le point 7 du palier 0b. Si le lecteur scripté retrouve presque autant sans ces deux champs, le repli coûte peu et respecte la garde à la lettre : je recommanderais le repli. Le nœud peut donc attendre le palier 0b sans rien bloquer.
3. **La mesure principale laisse de côté le volet des témoins jugés de l'oracle de N-058 : lecture permise, ou écart ?**
   Recommandation : **le garder hors de la mesure et de tout critère, et l'écrire au préenregistrement comme un écart déclaré à la lettre de N-058** ; ne pas jouer de juges à l'étage ; palier 5 seulement sur demande. **Confiance 0,75.**
   Raison : la lettre de N-058 nomme les témoins jugés, donc le dire « lecture permise » serait trop commode ; mais un juge ne doit pas trancher, et la mesure par appariement programmé à la loi plantée n'en a pas besoin. Ce qui me ferait changer : une lecture du code qui montrerait que le comparateur de l'oracle emploie un modèle.
4. **Un seul contraste décisif, ou deux ?**
   Recommandation : **deux, l'héritage et la tenue.** **Confiance 0,6.**
   Raison : sans la tenue, un héritage « non établi » ne dit pas si c'est le registre reçu qui n'apporte rien ou si servir un registre n'apporte rien du tout ; le bras 1 se joue de toute façon ; l'économie est au plus de 5 280 USD à cinq espèces, pour un test qui ne conclut que sur six signes égaux. Ce qui me ferait changer : une table de puissance du palier 0b où deux contrastes demandent beaucoup plus de sources qu'un seul à la taille de référence.
5. **La base « tirages indépendants à coût égal » (N-073, § 2) : ici, ou à l'épreuve qui lui est propre ?**
   Recommandation : **à l'épreuve qui lui est propre**, pas comme quatrième bras de ce plan. **Confiance 0,65.**
   Raison : c'est une autre question, avec sa pratique publiée à citer ; l'ajouter ici met une comparaison de plus à côté de deux contrastes décisifs et coûte de l'ordre de 2 810 USD à cinq espèces. Ce qui me ferait changer : que Lazar veuille les deux réponses sur les mêmes sources ; elle se jouerait alors comme un bras descriptif, sans seuil, sur son devis.

**Hors des cinq nœuds, à confirmer** : la composition (plan, question 6 ; § 6 ci-dessus) ; le pilote en deux temps (question 7) ; l'expérimentateur et le lecteur témoin (question 8) — le lecteur témoin coûte au plus 0,10 USD par tentative, soit au plus 3 290 USD à cinq espèces, et ne pèse sur aucun verdict : je ne le jouerais pas au-delà du palier 1.

## 10. Rapport aux ordres de grandeur déjà écrits

- La proposition (§ 4) donnait « entre 150 et 350 USD selon les espèces » ; la vérification courte des versions 2 (R-3643), « environ 4 000 USD » ; la v1 de ce devis, 10 560 USD ; la v2 et la v3, 24 180 USD en estimation, aiguilleur et juges compris à l'étage. Le détail de ces écarts est au § 7 du devis v3.
- La v4 ne change aucun compte de générations de bras ni aucun coût d'unité. Elle retire de la recommandation l'aiguilleur et les juges à modèle (3 710 USD), ajoute le palier 1 (59 USD), et chiffre le test de mort sur des bornes écrites, ce que la v3 ne faisait pas : de 1 970 à 19 740 USD de plus en estimation, à cinq espèces.

## 11. Différentiel v3 → v4 du devis

- **Structure** : le devis se lit par paliers. Sections neuves : § 3 (paliers, ce qu'ils permettent de conclure), § 4 (règles de passage), § 5 (test de mort par tentative), § 6 (variantes à deux, trois et cinq espèces, et la voie en escalier). Les § 3 et § 4 de la v3 sont résumés au § 7, sans changement de chiffre ; le § 2 bis de la v3 est cité, non recopié ; le § 6 de la v3 est repris au § 8 ; le § 7 de la v3 est résumé au § 10.
- **En-tête** : statut « version 4 » ; ligne `GO-2026-11-19-69` et fait transmis par le mandat ; N-045 ; la ligne 67 est dite lue sur `main`, et le fichier qu'elle cite sur la branche `lot/compte-organisme-v1` (constat 3 de la vérification de la v3) ; deux programmes de calcul.
- **Calcul** : `calcul_devis_heritage_v4.py` et sa sortie, noms neufs, rejoués deux fois à l'octet. Chiffres neufs : coût par palier et cumuls, par composition et par scénario ; ajout du test de mort par palier, à sept valeurs écrites ; nombre de sources à dépense égale ; part des deux espèces les plus chères ; étage à six, dix, douze et seize sources. **Aucun chiffre de la v3 n'est changé** : les totaux du pilote (4 750 USD) et de l'étage sans aiguilleur ni juges (15 720 USD) sont ceux de la sortie v2.
- **Test de mort par tentative** : la v3 donnait une sensibilité à des valeurs de calcul (0,05 à 0,50 USD) ; la v4 la donne sur les bornes écrites dans le code de l'étage (0,06 à 0,90 USD), dit pourquoi aucun coût réel n'existe, et fait du palier 1 sa mesure.
- **Recommandation** : la v3 recommandait l'option (a) à 24 180 USD en estimation, aiguilleur et juges joués pour information, confiance 0,6. La v4 recommande les paliers dans l'ordre, sans aiguilleur ni juges (20 530 USD de propositions), confiance 0,55, avec un seuil écrit qui la ferait passer à la voie en escalier.
- **Nœuds** : la v3 ne se prononçait sur aucun. La v4 donne, à la demande du mandat, une recommandation et une confiance pour chacun des cinq ; ils restent à Lazar.
- La v3, la v2, la v1, les deux versions antérieures du calcul et leurs compagnons restent en place (règle R12).

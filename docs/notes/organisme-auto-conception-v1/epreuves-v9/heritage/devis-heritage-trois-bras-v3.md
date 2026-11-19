# Question de l'héritage (N-073, § 1) — devis du plan à trois bras, par ordre de grandeur — v3

- **Statut : pièce de travail, version 3, à vérifier par le vérificateur sur les seuls neuf constats de sa vérification.** Ce devis chiffre l'étage payant **entier** du plan `plan-heritage-trois-bras-corrige-v3.md` (même dossier), pilote de bruit compris, avec la recommandation du rédacteur. Il n'engage rien : chaque étage payant part sur son propre préenregistrement scellé et contre-lu, sur un devis à sa taille finale et sur une ligne d'accord neuve.
- **Écrit par** : le rédacteur (modèle F), le 2026-11-19 ; version 3 commencée à 13:47Z (`date -u`), la version 2 ayant été écrite entre 13:24Z et 13:40Z ; processeur seul, aucun appel, aucune dépense. Mandat : `GO-2026-11-19-55`. Vérificateur prévu : modèle O.
- **Version remplacée, gardée telle quelle (règle R12)** : `devis-heritage-trois-bras-v2.md` (`988da4d18bc1c126f6b5daa694e593b10200e1a38c9e7c57697d329f962b84b3`). Vérification appliquée : `verification-plan-heritage-trois-bras-corrige-v2-v1.md` (`792d5f394d032327e26ad8f940ebc1fd36c0b703971f9294b2eaa2bfe6c91e9f`), neuf constats ; la table « constat → où, comment » est au § 17 du plan v3 ; le différentiel v2 → v3 du devis est au § 11 ci-dessous. **Aucun chiffre ne change entre la v2 et la v3.**
- **Version antérieure, gardée de même** : `devis-heritage-trois-bras-v1.md` (`af51c493494b6be2ab2c599b3b8f579fa7cdbbe46fa305a6a140b7d5e462fd2e`). Contre-lecture appliquée par la version 2 : `contre-lecture-plan-heritage-trois-bras-corrige-v1-v1.md` (`124767e4724bb125801b31df03c7021cc5cef1701349bdfa12c174fc8c3013da`) ; la table des dix-sept corrections est au § 15 du plan ; le différentiel v1 → v2 du devis est au § 10 ci-dessous.
- **Principe tenu** : ligne `GO-2026-11-19-60` de `registres/go.md` (mot de Lazar, verbatim : « le cout ne doit pas etre un fcateur limitant s'il ameliore considerablement l'organisme »). **La préparation reste sans dépense (ligne `GO-2026-11-19-55`) : écrire ce devis ne dépense rien.** La ligne `GO-2026-11-19-60` s'applique à la ligne de l'héritage : c'est un fait que le mandat de la version 3 transmet au rédacteur, que ce devis rapporte et ne tranche pas. En conséquence, le dessin n'est pas réduit pour son coût, **le coût est rapporté**, et la procédure est inchangée : chaque étage payant sur son devis et une ligne d'accord neuve. Le devis chiffre le dessin que le plan recommande et dit ce que chaque réduction ferait perdre (§ 8) ; les nœuds du plan (§ 12) restent à Lazar, dont celui d'un seul contraste décisif.
- **Devis présenté tôt** : ligne `GO-2026-11-19-67` de `registres/go.md` (lue sur `main`), ordre de passage des épreuves, version 3 (`docs/notes/organisme-auto-conception-v1/epreuves-v9/ordre-de-passage-epreuves-v9-v3.md`, `b19f550b525fe5696321167bd43a35fa5ece180fd2f97dad5dfc6e970a8c0f67`), option (a) choisie par Lazar : le devis de l'héritage est présenté dès qu'il est écrit. Aucun étage payant ne part sans son devis scellé et sa ligne d'accord.
- **Mot de Lazar, transmis par le mandat de la version 3, verbatim** : « ce sont les essais avec experiences qui doivent trancher in fine les cartes et les tetss de mort ». Tenu ici : aucun chiffre, aucune composition, aucun levier de ce devis ne dépend du verdict d'un juge (N-058) ; les juges à modèle, s'ils sont joués, ne le sont que pour information.
- **Calcul** : `calcul_devis_heritage_v2.py` (`5d21b393f03f3e859241d97dea8347937596422c42f6b9f3cc4e5f5661b1a1c9`), sortie `calcul-devis-heritage-v2.json` (`132a07649dd6d572ad50e5bc6c41a73fee9d54a8bcceef996192fb886b1dca6b`), même dossier ; rejoué deux fois, sorties identiques à l'octet. Tout chiffre ci-dessous en vient, arrondi. **La version 3 ne change aucun chiffre : le programme et sa sortie restent ceux de la version 2, sans version neuve.** Ces deux fichiers, déjà versés et scellés, gardent les noms de rôle du manifeste ; le texte du devis ne les écrit plus (§ 1). Version 1 du calcul, gardée : programme `782a86104b518eb5a4a616111ec6fb50d70ac713bf58138013c1b27291b4b186`, sortie `02bae7980cbba40fb83ea7f30d732e11f9880c24fca3c4a1913b4b8923231765`.
- **Source des coûts** : manifeste de fin du lanceur de la course d'auto-conception v9, `runs/20261119-094145-course-auto-conception-v9/manifeste-lanceur-fin.json` (branche `lot/compte-organisme-v1`, sha256 `28bc36df390d8481fb5bd9118cf764843ffea60856412d825ecbf08e7cee5be7`), champs `cout_reel.par_role_usd` et `cout_reel.appels_par_role` ; constantes recopiées de la v1 du calcul, que la contre-lecture a comparées au manifeste. La course entière a coûté 72,50 USD, soit 1,8 fois son devis.

## 0. Verdict

1. **Étage sur processeur : 0 USD d'appels.** Il précède tout le reste, et il rend les tailles (plan, § 7).
2. **Pilote de bruit, étage payant à part** (plan, § 8.0) : neuf paires de courses jumelles, **de l'ordre de 4 750 USD en estimation** à la composition de la course v9 ; 7 920 USD en cas haut ; 12 670 USD au pire.
3. **Étage payant, hors pilote** : douze sources à dose non nulle, huit à dose nulle, quatre générations de bras par continuation. À la composition de la course v9, aiguilleur et juges à modèle joués pour information : **de l'ordre de 19 430 USD en estimation** ; 33 710 USD en cas haut ; 53 940 USD au pire.
4. **Recommandation du rédacteur, pilote et étage ensemble : de l'ordre de 24 180 USD en estimation, 41 630 USD en cas haut, 66 610 USD au pire**, avant deux postes non chiffrables aujourd'hui (§ 6), dont le premier peut peser lourd : le coût du test de mort par tentative.
5. C'est très au-dessus de ce que la proposition annonçait (de 150 à 350 USD) et de la v1 (de 1 600 à 10 600 USD en estimation). Les raisons sont au § 7 : le plancher de sources, la génération finale, les sources à dose nulle, un pilote qui estime quelque chose, et le choix de ne plus réduire le dessin pour son coût.

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

**Table de correspondance.** Ce devis n'écrit aucun nom d'espèce. Les espèces sont numérotées par le coût réel croissant de leur rôle de proposeur dans le manifeste de fin du lanceur de la course v9 (`runs/20261119-094145-course-auto-conception-v9/manifeste-lanceur-fin.json`, branche `lot/compte-organisme-v1`, sha256 `28bc36df390d8481fb5bd9118cf764843ffea60856412d825ecbf08e7cee5be7`), champ `cout_reel.par_role_usd`, parmi les cinq rôles dont le nom commence par `prop-` :

| désignation dans ce devis | rôle du manifeste auquel elle renvoie | coût réel du rôle, arrondi (USD) |
|---|---|---|
| espèce 1 | le rôle de proposeur au coût réel le plus bas | 4,17 |
| espèce 2 | le deuxième par coût croissant | 4,75 |
| espèce 3 | le troisième | 7,43 |
| espèce 4 | le quatrième | 17,58 |
| espèce 5 | le rôle de proposeur au coût réel le plus haut | 24,72 |
| juge de l'espèce 3, juge de l'espèce 1 | les deux rôles dont le nom commence par `juge-` et finit comme le rôle de proposeur de l'espèce 3 et de l'espèce 1 | 6,86 et 2,41 |

Les cinq coûts sont distincts : la numérotation est sans ambiguïté, et le nom de chaque espèce se lit dans le manifeste, non ici. Ces coûts sont ceux d'une course dont les cartes proposent des mécanismes pour l'organisme. Une course sur monde planté, où les tentatives sont des lois, peut avoir des invites et des réponses d'une autre longueur : l'unité ci-dessous est un ordre de grandeur, pas une mesure. Le pilote rendra les coûts de référence réels (plan, § 8.0).

## 2. L'unité : une génération d'un bras

Le plan fixe un budget en dollars égal par bras. Le bras qui lit un registre paie sa lecture sur ce budget et joue moins d'appels : **le registre n'ajoute donc aucune ligne au devis**. L'unité est le coût d'une génération de propositions, pour une composition donnée, à onze appels par espèce comme à la v9.

| composition des proposeurs | appels | tentatives attendues, à la proportion de la v9 | coût d'une génération d'un bras (USD) | avec aiguilleur et deux juges à modèle (USD) |
|---|---|---|---|---|
| A — les cinq espèces de la v9 | 55 | 94 | 58,64 | 72,50 |
| B — trois espèces, sans les deux plus chères (espèces 1, 2 et 3) | 33 | 56 | 16,35 | 24,66 |
| C — les deux espèces les moins chères (espèces 1 et 2) | 22 | 38 | 8,92 | 14,46 |

Ce devis ne choisit pas la composition : elle se juge sur l'oracle du monde planté et le coût, jamais sur le verdict d'un juge (N-058), et tout changement de modèle demande un accord. **La composition A est celle de l'organisme tel qu'il existe ; c'est elle que la recommandation chiffre.** Les lignes B et C sont données pour information.

L'aiguilleur et les juges à modèle ne servent aucun critère : ils permettent de rapporter, comme information seulement, le volet des témoins jugés de l'oracle de N-058 (plan, § 6 et § 12, question 3). Le pilote, qui ne mesure que le bruit de la mesure principale, se joue sans eux.

## 2 bis. Ligne d'information : les appels perdus par le bras qui lit un registre

Le bras 3 sert dès la première génération le registre de la source ; à budget égal, il joue moins d'appels (plan, § 2, règle 6). Le nombre perdu dépend de la part du coût d'un appel que prend la lecture, que seul le pilote mesurera. Champ `appels_perdus_par_le_bras_3_en_generation_1` de la sortie du calcul. **Cette table suppose un coût d'appel uniforme entre les espèces : c'est un ordre de grandeur.** La règle du plan (§ 2, règle 6) retire les appels un à un dans l'ordre d'une permutation semée, jusqu'à ce que le coût prévu tienne dans le budget ; les espèces coûtant de 0,38 à 2,25 USD par appel, le nombre réellement retiré dépendra de l'ordre tiré :

| part du coût d'un appel prise par la lecture | 2 % | 5 % | 10 % | 14,1 % | 25 % | 50 % |
|---|---|---|---|---|---|---|
| A, 55 appels — règle de la v2 | 2 | 3 | 5 | 7 | 11 | 19 |
| A, 55 appels — règle de la v1 (arrondi par espèce) | 5 | 5 | 5 | 10 | 15 | 20 |
| B, 33 appels — règle de la v2 | 1 | 2 | 3 | 5 | 7 | 11 |
| B, 33 appels — règle de la v1 | 3 | 3 | 3 | 6 | 9 | 12 |
| C, 22 appels — règle de la v2 | 1 | 2 | 2 | 3 | 5 | 8 |
| C, 22 appels — règle de la v1 | 2 | 2 | 2 | 4 | 6 | 8 |

Seul repère disponible : le plan d'origine (section c.9, « estimation de ce lecteur, qui n'est pas un devis ») donne au plus 8,25 USD par génération et par bras pour un registre plein servi à 55 appels, soit 14,1 % de l'unité A. À ce repère, le bras 3 perdrait 7 appels sur 55 à la première génération. Ce repère n'est pas vérifié ; il borne par le haut, au prix d'entrée le plus élevé que cette section relevait.

## 3. Le compte des générations de bras

Une continuation compte trois générations puis la génération finale sur le monde tenu à l'écart (plan, § 6) : quatre générations de bras.

| poste | estimation | haut et pire |
|---|---|---|
| sources à dose non nulle | 12 | 16 |
| sources à dose nulle (bras 2 et 3 seulement) | 8 | 12 |
| générations de bras par continuation, finale comprise | 4 | 4 |
| générations de la course source | 3 | 3 |
| continuations du critère (3 bras × sources × 4) | 144 | 192 |
| continuations à dose nulle (2 bras × sources × 4) | 64 | 96 |
| courses sources (une par source, 3 générations) | 60 | 84 |
| **étage payant hors pilote, en générations de bras** | **268** | **372** |
| pilote : sources de pilote | 3 | 4 |
| pilote : paires de courses jumelles (3 bras par source) | 9 | 12 |
| **pilote de bruit, en générations de bras** (par source : 3 + 3 bras × 2 jumelles × 4 = 27) | **81** | **108** |
| **total, en générations de bras** | **349** | **480** |

- *Estimation* : le dessin que le plan recommande aujourd'hui. Douze sources à dose non nulle (plan, § 3.3) ; huit à dose nulle (la règle unilatérale peut alors se déclencher même si la somme des rangs contraires atteint 5, plan, § 3.3) ; pilote de neuf paires (plan, § 8.0).
- *Haut* : seize sources à dose non nulle si la règle du pilote relève ce nombre, douze à dose nulle, pilote de douze paires, coût de l'unité relevé d'un quart.
- *Pire* : les nombres du cas haut, coût de l'unité doublé (la v9 a coûté 1,8 fois son devis). Un plafond d'arrêt gelé à chaque préenregistrement borne la dépense en tout état de cause.
- **Ces nombres ne sont pas choisis par le devis.** Le nombre de sources à dose nulle sort de l'étage sur processeur (plan, § 7) ; le nombre de sources à dose non nulle sort de la règle du pilote (plan, § 8.0), qui peut le relever au-delà de seize. Le coût d'une source de plus est au § 4 pour que tout autre nombre se chiffre à la main.

## 4. Totaux (USD, arrondis à la dizaine)

**Pilote de bruit**, sans aiguilleur ni juges à modèle — son propre préenregistrement, son devis, sa ligne d'accord :

| composition | estimation (9 paires) | haut (12 paires) | pire |
|---|---|---|---|
| A — cinq espèces | 4 750 | 7 920 | 12 670 |
| B — trois espèces | 1 320 | 2 210 | 3 530 |
| C — deux espèces | 720 | 1 200 | 1 930 |

**Étage payant, hors pilote** :

| composition | estimation | haut | pire |
|---|---|---|---|
| A — sans aiguilleur ni juges | 15 720 | 27 270 | 43 630 |
| A — avec aiguilleur et juges, pour information | 19 430 | 33 710 | 53 940 |
| B — sans aiguilleur ni juges | 4 380 | 7 600 | 12 160 |
| B — avec aiguilleur et juges | 6 610 | 11 470 | 18 350 |
| C — sans aiguilleur ni juges | 2 390 | 4 150 | 6 630 |
| C — avec aiguilleur et juges | 3 880 | 6 720 | 10 760 |

**Pilote (sans juges) et étage (avec aiguilleur et juges) ensemble** — champ `recommandation_pilote_sans_juges_et_etage_avec_usd` :

| composition | estimation | haut | pire |
|---|---|---|---|
| **A — cinq espèces (recommandation)** | **24 180** | **41 630** | **66 610** |
| B — trois espèces | 7 930 | 13 680 | 21 880 |
| C — deux espèces | 4 600 | 7 930 | 12 680 |

**Une source de plus** (composition A, sans aiguilleur ni juges, facteur un) : à dose non nulle, 15 générations de bras, soit 880 USD ; à dose nulle, 11 générations de bras, soit 650 USD ; une source de pilote, 27 générations de bras, soit 1 580 USD. Pour B : 250, 180 et 440 USD ; pour C : 130, 100 et 240 USD.

**Bras de diagnostic** (plan, § 9), sur devis à part : un bras, douze sources, quatre générations de bras coûte environ 2 810 USD (A), 780 USD (B) ou 430 USD (C). Six bras sont décrits ; tous se jouent d'abord sur processeur.

## 5. Étage sur processeur : 0 USD

Générateur des mondes à dose plantée, exécuteur simulé du test de mort, cinq proposeurs scriptés (le sourd en deux variantes), procédure d'analyse entière, table de puissance, six bras de diagnostic : aucun appel de modèle. Coût : un préenregistrement par le modèle F, sa contre-lecture par le modèle O, le code et ses essais, du temps de machine sur processeur. Aucune instance payante.

Ce que cet étage rapporte au devis : le nombre de sources à dose nulle, la dose non nulle à retenir, la part de différences nulles, la table de puissance dont la règle du pilote tire le nombre de sources, et l'effet du seul coût de lecture. **Le devis de chaque étage payant se réécrit après lui, à sa taille finale.**

## 6. Ce qui n'est pas chiffré

1. **Le test de mort par tentative** (plan, § 3.0). L'épreuve programmée du plan est le test de mort de l'organisme, verdict calculé par le noyau. La course v9 n'en a joué aucun ; la proposition (§ 6, écart 5) dit que cet étage n'est pas branché sur le lanceur. Il demande une session de modèle qui écrit le script, par tentative, sans coût réel connu, et un lecteur témoin si on le garde. Aux générations de la continuation, ce coût entre dans le budget de chaque bras. **À la génération finale, le test de mort des tentatives se fait pour la mesure seulement, sur la tranche d'épreuve du monde final ; le plan recommande de le payer hors du budget égal, à l'identique pour les trois bras** (plan, § 6) : la table ci-dessous le compte déjà, puisqu'elle porte sur toutes les générations de bras, finales comprises. **Sensibilité**, à la proportion de tentatives de la v9, pour le total de 349 générations de bras en estimation (champ `ajout_de_l_epreuve_programmee_usd_selon_cout_par_tentative` ; les coûts par tentative sont des valeurs de calcul, pas des mesures) :

   | coût du test par tentative (USD) | 0,05 | 0,10 | 0,25 | 0,50 |
   |---|---|---|---|---|
   | ajout, composition A (94 tentatives par génération de bras) | 1 640 | 3 280 | 8 200 | 16 400 |
   | ajout, composition B | 980 | 1 970 | 4 920 | 9 840 |
   | ajout, composition C | 660 | 1 310 | 3 280 | 6 560 |

   Le pilote mesurera ce coût (plan, § 8.0) ; le devis du pilote lui-même devra le borner par un essai réel de quelques tentatives, sur accord.
2. **La fermeture de la boucle** : aucune génération ne lit aujourd'hui un registre, et les tests de mort ne sont pas branchés. Le travail est du code sur processeur, mais il précède tout.
3. **L'audit du registre par un lecteur d'une autre lignée**, à chaque génération (plan, § 1) : un appel par génération de bras qui tient un registre, soit au plus 349 appels en estimation ; non chiffré, petit devant l'unité.
4. **La longueur réelle des appels sur monde planté** (§ 1).
5. **Les appels sans sortie exploitable** : à la v9, jusqu'à 3 appels sur 11 pour une espèce. Ils sont payés ; le cas haut les couvre par son quart de marge, sans garantie.
6. Les préenregistrements, contre-lectures et verdicts sont faits par des sous-agents de la session et n'entrent pas dans ces lignes.

## 7. Rapport aux ordres de grandeur déjà écrits

- La vérification courte des versions 2 (R-3643) donnait « environ 4 000 USD pour trois bras, dix sources et trois générations », sur une unité d'environ 45 USD par génération pour l'étape de proposition.
- La proposition (§ 4) donnait « entre 150 et 350 USD selon les espèces » : une transition de génération, quelques mondes, quelques graines, sans plancher de sources.
- La v1 de ce devis donnait 180 générations de bras en estimation, soit 10 560 USD en composition A. La v2 en compte 349. L'écart se décompose ainsi, en générations de bras : génération finale sur le monde tenu à l'écart, plus 30 pour dix sources et plus 12 pour six sources à dose nulle ; douze sources au lieu de dix, plus 30 ; huit sources à dose nulle au lieu de six, plus 22 ; pilote de neuf paires au lieu d'une, plus 75. S'y ajoutent, en dollars, l'aiguilleur et les juges joués pour information à l'étage.

## 8. Ce qui réduirait le coût, et ce que cela ferait perdre

La ligne `GO-2026-11-19-60` s'appliquant à l'héritage (en-tête), **le rédacteur ne recommande aucun de ces leviers** : chacun affaiblit la réponse. Ils sont rapportés pour que le prix de la réponse soit lisible. **Ce devis n'en ferme aucun** : deux sont des nœuds de Lazar (la composition ; un seul contraste décisif, plan, § 12, question 4), et le prix de chaque voie est donné pour qu'il tranche.

| levier | effet sur le total | ce qui serait perdu |
|---|---|---|
| composition B ou C au lieu de A | divisé par 3 ou par 5 environ | la réponse ne vaudrait que pour ces espèces, et non pour l'organisme tel qu'il existe ; nœud (N-058, changement de modèle) |
| un seul contraste décisif (l'héritage) — **nœud ouvert** (plan, § 12, question 4) | plancher technique de six sources au lieu de dix | six signes égaux exigés ; la tenue deviendrait descriptive |
| dix sources à dose non nulle au lieu de douze | moins 30 générations de bras | plus de marge pour les différences nulles |
| dose nulle sur processeur seulement (l'ancienne colonne « minimal », **hors plan**) | moins 88 générations de bras | la règle de validité ne serait pas appliquée à de vrais proposeurs, ce que le plan rend obligatoire |
| pilote de six paires au lieu de neuf | moins 27 générations de bras | borne haute de l'écart-type à 1,92 fois l'estimation au lieu de 1,65 |
| course source d'une génération | moins 40 générations de bras | un registre hérité mince, donc un effet attendu plus petit |
| sans aiguilleur ni juges à modèle à l'étage | moins 3 710 USD en estimation (A) | le volet des témoins jugés de l'oracle de N-058 ne serait pas rapporté, même pour information |
| moins de onze appels par espèce | proportionnel | moins de tentatives par génération, scores plus discrets, plus de différences nulles |

## 9. Décision pour Lazar — ce qui est demandé, dans l'ordre

**Décision.** Engager la question de l'héritage par ses trois étages, chacun sur sa ligne d'accord : l'étage sur processeur maintenant (0 USD d'appels), puis le pilote de bruit, puis l'étage payant, tous deux sur un devis réécrit à leur taille finale. Ce devis est présenté dès qu'il est écrit, selon l'option (a) de l'ordre de passage version 3 (ligne `GO-2026-11-19-67`) ; il ne demande aucune dépense aujourd'hui.

**Enjeu.** Le plan répond à la question de N-073, § 1, sous la lettre du complément 3. Sa taille vient du plancher de sources, de la dose nulle et d'un pilote qui estime vraiment le bruit, non d'un choix de confort. Sa réponse ne vaut que pour un organisme où une génération lit un registre et où les tests de mort éprouvent chaque tentative : deux branchements à faire d'abord.

**Options.**
- **(a) Étage sur processeur d'abord, puis pilote, puis étage payant, à la composition de la course v9.** Avantage : l'instrument est éprouvé à 0 USD avant le premier appel ; la réponse vaut pour l'organisme tel qu'il existe ; chaque étage peut arrêter la suite. Inconvénient : de l'ordre de 24 180 USD en estimation et 66 610 USD au pire pour les deux étages payants, avant le coût inconnu des tests de mort.
- **(b) Étage sur processeur seul pour l'instant**, la suite se décidant à sa lecture. Avantage : aucun engagement de principe sur une somme de cet ordre ; les tailles réelles seront connues. Inconvénient : le pilote et les branchements ne se préparent pas en parallèle.
- **(c) Trancher d'abord les questions du plan (§ 12)**, dont le choix de l'épreuve programmée, puis (a) ou (b). Avantage : l'étage sur processeur se construit sur un objet fixé. Inconvénient : cinq nœuds avant tout résultat, alors que l'étage sur processeur éclaire l'un d'eux (plan, § 7, point 7).

**Recommandation du rédacteur.** (a), confiance 0,6, **sous une condition** : que la question 1 du plan (l'épreuve programmée est-elle bien le test de mort ?) soit tranchée avant le préenregistrement de l'étage sur processeur, puisque son exécuteur simulé en dépend. Le coût est rapporté sans réduction, la ligne `GO-2026-11-19-60` s'appliquant à l'héritage (fait transmis ; plan, § 12, question 9). Cette recommandation ne répond à aucun des cinq nœuds du plan (§ 12, questions 1 à 5), qui restent à Lazar ; si la question 4 était tranchée pour un seul contraste, le § 4 donne de quoi rechiffrer à la main.

**Défaut.** Aucun : le mandat `GO-2026-11-19-55` s'arrête, pour l'héritage, au plan corrigé et au devis ; l'étage sur processeur demande un mot neuf, et chaque étage payant une ligne d'accord neuve sur son devis.

## 10. Différentiel v1 → v2 du devis

- **En-tête** : statut « version 2 » ; le devis chiffre l'étage payant entier avec sa recommandation ; principe de la ligne `GO-2026-11-19-60` ; empreintes entières du programme et de sa sortie, v1 et v2 (correction 15).
- **§ 0** : la fourchette par composition est remplacée par le pilote, l'étage et la recommandation, chacun en estimation, haut et pire ; la colonne « minimal » n'entre plus dans les totaux (correction 16).
- **§ 2** : colonnes « tentatives attendues » et « avec aiguilleur et juges » ; la composition A est celle que la recommandation chiffre.
- **§ 2 bis** : neuf — appels perdus par le bras qui lit un registre, règle de la v2 et règle de la v1 (corrections 2 et 16).
- **§ 3** : quatre générations de bras par continuation (correction 8) ; douze sources et huit à dose nulle en estimation, seize et douze en cas haut ; pilote compté en paires de jumelles, trois bras par source de pilote, 81 générations de bras au lieu de 6 (correction 5) ; colonne « minimal » retirée.
- **§ 4** : trois tables (pilote, étage, ensemble) au lieu de deux ; coût d'une source de plus ; bras de diagnostic à douze sources et quatre générations.
- **§ 5** : cinq proposeurs scriptés ; table de puissance.
- **§ 6** : le premier poste nomme le test de mort et donne une table de sensibilité (correction 1) ; l'audit par une autre lignée est compté en appels.
- **§ 7** : décomposition de l'écart entre la v1 et la v2.
- **§ 8** : les leviers sont rapportés avec ce qu'ils feraient perdre ; aucun n'est retenu ; la colonne « minimal » y est dite hors plan.
- **§ 9** : la décision porte sur les trois étages ; options réécrites ; défaut réécrit dans les mots de la contre-lecture (correction 16).
- **Calcul** : `calcul_devis_heritage_v2.py` et sa sortie, noms neufs ; la v1 du programme et de sa sortie reste en place (règle R12).

## 11. Différentiel v2 → v3 du devis

- **Aucun chiffre ne change.** Le programme `calcul_devis_heritage_v2.py` et sa sortie `calcul-devis-heritage-v2.json` restent la source de tous les chiffres ; aucune version 3 du calcul n'est écrite.
- **En-tête** : statut « version 3 » ; version remplacée et vérification appliquée ; le principe de la ligne `GO-2026-11-19-60` est réécrit (constat 4 : la préparation reste sans dépense ; l'application à l'héritage est rapportée comme un fait transmis ; les nœuds restent à Lazar) ; deux puces neuves (devis présenté tôt, ligne `GO-2026-11-19-67` ; mot de Lazar transmis).
- **§ 1 et § 2** : les noms de rôle du manifeste sont remplacés par « espèce 1 » à « espèce 5 », avec une table de correspondance qui renvoie au manifeste de fin, chemin et empreinte (demande du mandat de la version 3, d'après la remarque de la vérification) ; les lignes du § 1 sont rangées par numéro d'espèce.
- **§ 2 bis** : la table est dite ordre de grandeur à coût d'appel uniforme, avec la règle de retrait à une seule définition (constat 5).
- **§ 6, point 1** : le test de mort des tentatives de la génération finale est dit payé hors du budget égal, selon la recommandation du plan, et déjà compté par la table de sensibilité (constat 3).
- **§ 8** : la phrase d'en-tête ne ferme plus aucun levier ; « un seul contraste décisif » est marqué nœud ouvert (constat 4).
- **§ 9** : devis présenté tôt ; cinq nœuds au lieu de quatre ; la recommandation ne répond à aucun nœud (constat 4).
- **Constats 1, 2, 6, 7, 8 et 9** : sans effet sur le devis ; ils sont appliqués au plan (plan, § 17).
- La v2, la v1 et leurs compagnons restent en place (règle R12).

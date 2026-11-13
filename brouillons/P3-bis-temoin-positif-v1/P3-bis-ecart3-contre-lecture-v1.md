# P3-bis, écart 3 (R-2492) — contre-lecture du code (commit `02017d32`) et de l'addendum 3 (brouillon 1) — v1

- Contre-lecteur neuf : sous-agent, **Claude Fable 5.2** (`claude-fable-5-2`), autre modèle que le développeur-rédacteur
  (Claude Opus 5.5). N'a écrit ni la chaîne de P3-bis, ni les écarts 1, 2 et 3, ni leurs addendums.
- Écrit le 2026-11-13 de 08:12 à 08:33 UTC (heures relevées par `date -u`).
- Interdits communs v2 lus en entier avant toute autre lecture, et appliqués. **Aucun fichier de T0.7, aucun chemin
  interdit, ni la branche `calcul/p3bis-reel-v1`, ni aucun résultat de P3-bis n'ont été ouverts ou listés.** Aucune clé
  lue. Aucun appel à l'outil de location réel, aucun appel de modèle, aucune dépense. Aucun commit, aucune poussée, aucun
  `fetch`. Aucun refus d'un contrôle de permissions, d'un classifieur ou d'un crochet pendant ce travail.
- Écrit : ce rapport et son compagnon ; un bac à sable sous
  `/tmp/claude-0/-home-user/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/cl-p3bis-ecart3/`.
- Déclarations : section 8.

## Verdict

**Scellable après corrections.** Le **code est scellable tel quel** (enchaîneur v6, banc, journal : aucune correction
exigée, empreintes inchangées). Les corrections exigées portent toutes sur l'**addendum** (A1 à A6, un brouillon 2).
La règle de relance est sûre au sens de R1 ; ce qui manque est de l'écriture, pas du fond.

## Corrections exigées (addendum, brouillon 2)

- **A1 — Condition (i) : écrire « probable », comme le registre.** Le brouillon dit la cause « établie par le
  registre » (R1 (i), l. 91-92 ; Q1, l. 178-179). R-2491 écrit « **cause probable** », et R-2490 « cause non
  déterminable » sur l'instance ; le loueur n'a rendu aucune raison d'arrêt. Écrire la condition telle qu'elle est
  constatée : (a) crédit 0 et solde −0,93 USD relevés à 07:30Z ; (b) les deux instances du compte arrêtées ; (c) journal
  sans erreur ; (d) consommation et heure concordantes ; (e) mot de Lazar, titulaire du compte, « vast n'a plus de
  credits ». Puis : « la cause est probable, non confirmée par le loueur ; elle est tenue pour suffisante par le mot de
  Lazar (R-2492) ». Le risque résiduel du brouillon (l. 363-364) le dit déjà ; la règle doit le dire aussi.
- **A2 — Écrire ce qui rend la relance aveugle sans retour.** Ajouter à R1, « Portée » : l'instance 60432755 a été
  **détruite** à 07:48:11Z (R-2493) sans récupération ; sa branche est restée égale à S ; les 19 lots joués n'existent
  donc plus nulle part et ne pourront jamais être lus. Ajouter : « la lecture de P3-bis porte sur la tentative 2 seule,
  quel que soit son résultat ; la tentative 1 est rapportée au verdict comme tentative avortée, avec sa dépense ».
  C'est le cœur de la sûreté au sens de R1 ; il doit être écrit, pas déduit.
- **A3 — Fermer la porte de la tentative 3.** Le brouillon écrit (l. 109-110) : « Une relance de plus (N = 3) n'est
  permise que par la ligne 1 telle qu'elle est écrite (aucun épisode joué) ou par un nouveau mot de Lazar ». Deux
  précisions à écrire : (a) « aucun épisode joué **par la tentative 2** » ; (b) remplacer « un nouveau mot de Lazar »
  par « un nouvel écart, écrit, contre-lu et scellé avant la relance (nœud de Lazar) ». Un mot seul ne suffit pas à
  relancer après des épisodes joués : c'est un écart à un texte scellé.
- **A4 — Réserve de l'écart 1 : mot pour mot.** A1 l. 176-177 écrit : « Elle vaut pour toute la course dès qu'une
  création s'est faite sous l'écart. » Le brouillon (l. 228-229) la restreint : « vaut pour les créations faites sous
  l'écart 1 (60286945, 60370121, 60432755) ». Rétablir les mots de A1 : la réserve « garde du crédit levée par écart,
  R-2399 » reste **pour toute la course**, donc au verdict, même si la tentative lue est créée sous la garde d'origine.
  Les trois identifiants peuvent être donnés en information.
- **A5 — Préalable 2 (recharge) : l'écrire sur le crédit présent, et sur les faits du jour.** Trois défauts :
  (a) « recharge ≥ M + K + D, relevée au crédit présent » mêle un versement et un crédit ; (b) la recharge est faite
  (R-2494, 08:06Z, « vast rechargé ») et le crédit relevé vaut **23,80 USD** (R-2495) : la dette D est absorbée et sort
  du calcul ; (c) le brouillon ne dit pas si M + K est une condition ou un conseil. Écrire : « au relevé fait juste
  avant le lancement, crédit présent ≥ M + K », soit **27,50 USD** sans instance nommée, **40,92 USD** avec 60417353
  nommée à 1,342 USD de l'heure ; variante prudente (K = 22,2) : 42,20 et 55,62. Dire que c'est une **condition** de
  la session (recommandé, elle suit R-2491 : « coût attendu de la course plus marge »), en plus de la garde M que le
  lanceur applique seul ; ou dire que c'est un conseil, et alors la garde M seule décide. Dans les deux cas, écrire le
  constat : à 23,80 USD, M + K n'est atteint dans aucun des deux cas ; la garde M seule passe sans 60417353 (20,00) et
  refuse avec elle (33,42).
- **A6 — Préalable 8 (refspec) : dire ce qu'il couvre.** Le brouillon écrit que le refspec restreint fait
  « qu'aucune branche interdite, dont `calcul/p3bis-reel-v1`, ne soit rapatriée ». Ce n'est vrai que du **clone local
  de lancement**. Les contrôles avant dépense, appelés par le lanceur (l. 131), font
  `git clone -q --no-checkout "$DEPOT_URL"` (`controles_avant_depense_p3bis_v2.sh` l. 95) : ce clone temporaire reçoit
  toutes les branches du distant, en extraction partielle, et il est effacé à la sortie (lanceur l. 85 et 135). Rien
  n'en est lu, et `calcul/p3bis-reel-v1` est égale à S ; mais la phrase doit être juste. Écrire : « dans le clone local
  de lancement » ; déclarer le clone temporaire des contrôles (il existait à chaque tentative précédente). Ajouter : le
  refspec restreint doit garder une branche qui contient S (lanceur l. 93 : `git branch -r --contains S`) ; c'est le cas
  de `prep/p3bis-ecart3-v1` (S n'est pas un ancêtre du `main` local, relevé par moi à 08:28Z).

Mises à jour qui vont avec le brouillon 2 : ligne « Contre-lecture (R2) : à faire » ; registres cités (R-2494 et R-2495 ;
empreinte du registre des décisions au commit lu) ; section « Mot de Lazar » : ajouter R-2494, verbatim.

## Corrections suggérées

- **S1 (condition (i), avant le lancement si c'est sans dépense)** — Un constat de plus, en lecture seule, rendrait la
  cause presque certaine : l'heure d'arrêt de 60417353 (si elle tombe dans les mêmes minutes que 60432755, la cause est
  au compte, pas à une machine), ou la ligne de la page des frais du loueur où le solde passe sous zéro. À relever par
  la mère ou par Lazar, et à inscrire. Sinon la réserve « cause probable » reste telle quelle.
- **S2 (addendum, l. 108 et 361-362)** — « mêmes graines […] elle reproduit la course » : écrire « même configuration,
  mêmes graines ; l'identité au bit près des épisodes n'est ni exigée ni vérifiée (hôte et carte peuvent différer) ».
- **S3 (addendum)** — Citer A2 l. 353-354 mot pour mot (« Le lanceur v1 et le lanceur d'origine ne sont toujours jamais
  joués pour une création. ») au lieu de la citation à crochets de la l. 251. Dire le sort des préalables 1 à 4 de A2 :
  1 et 4 remplacés par ceux de l'addendum 3 ; 2 accompli (facture relevée, R-2460) ; 3 accompli (R-2460).
- **S4 (addendum, préalable 4)** — Facture de 60432755 : la relever avant le lancement si elle est lisible, comme pour
  60370121 et 60286945 (R-2460) ; elle remplace le majorant de 2,00 USD et le stockage estimé. Le calcul indicatif
  (6,07 USD) est juste sur les lignes citées (refait : 0,220 + 0,458 + 3,11 + 2,00 + 12 269 s × 0,08 / 3 600 = 6,061).
- **S5 (addendum, préalable 3)** — Ajouter : le lanceur ne refuse sur la liste fermée qu'à son étape 8, après les
  contrôles et le choix de l'offre, par le code 2, et le dossier neuf est alors consommé (R12) ; l'inventaire relu
  avant le lancement évite ce tour à vide. Ajouter aussi : une instance d'une autre course relancée **après** la
  création de P3-bis n'est pas comptée par la garde ; la session relit le crédit quand elle le sait.
- **S6 (addendum, préalable 7)** — Écrire « extraction **partielle** » de la branche (interdits communs, règle 9) :
  l'arbre de travail du développeur extrayait les dossiers interdits (son rapport, l. 13-14).
- **S7 (registre)** — Le rapport du développeur (`e0ecb132…`, scellé) se dit « écrit vers 08:20 UTC », alors que son
  commit date de 08:10:37Z. L'heure n'est pas celle d'un relevé. Le fichier est scellé : à noter au registre, sans
  réécriture.
- **S8 (banc, version suivante)** — Deux trous sans effet sur le verdict : les revérifications d'empreinte juste avant
  le contrôle et la surveillance ne sont pas éprouvées (déjà S7 de la contre-lecture de l'écart 2) ; aucun cas
  « instance d'autrui en marche et non nommée » dans ce banc (le banc du lanceur d'origine, rejoué, le couvre).

## Pièces relues (empreintes recalculées)

| Pièce | Empreinte | État |
|---|---|---|
| `enchaineur_p3bis_v6.sh` | `1b49b701253b89fd42cad589097f700697dd38de0a178b1fadda168dbd7f521f` | égale ; compagnon conforme |
| `essais_ecart3_p3bis_v1.sh` | `56659e9d498ade34b9d00578433f2eb0f00bea1184de25fd9aebb1e878d6bf81` | égale ; compagnon conforme |
| `essais-ecart3-p3bis-v1.log` | `06e2aeca127f4c886d3fd891e141623097a84eebc21fddc7823d269981d8436a` | égale ; compagnon conforme |
| `rapport-developpeur-p3bis-ecart3-v1.md` | `e0ecb1322439b47cbaccb9fb2edfa461c62c1deddcf2ce62952a34a71af269d1` | égale ; compagnon conforme |
| sept sorties de `sorties-essais-ecart3-v1/` | celles de l'addendum | égales ; sept compagnons conformes |
| addendum 3, brouillon 1 | `4f7bb2b063a39b79d89ebe4df49b53fedec4ebc5cabaacc1c5a78fad785fc577` | égale ; compagnon conforme |
| `enchaineur_p3bis_v5.sh` (au commit `351294c3`) | `34131eaf528f65077576a83a64fceb58100ab34027b043c79763a31669e063a0` | égale |
| `lancer_p3bis_v2.sh` (à S et au commit `351294c3`) | `029bdb5c114a6166a21fa93724d71a2bf6158dc9686993424f6fbe8462352b08` | égale aux deux commits |
| texte scellé `prereg/P3-bis-temoin-positif-v1.md` | `76ab66ce967796b944e2ca585ee0dc2d780189e8e0cbe429e390c427a46121cb` | égale |
| addendum 1 ; addendum 2 | `4e188814…5ca537` ; `c23b2eb0…ec9444` | égales |
| registres des dépenses, des arrêts, des GO (arbre courant) | `c79537ba…`, `3b9cb6ae…`, `405e4b56…` | égales à l'addendum |
| registre des décisions (arbre courant, commit `a4600f29`) | `79d3d0764cf337afba9cf1f9dcc62b44989fb66c3904de285d797c73668d51a1` | plus récent que celui de l'addendum (`bba73940…`) : R-2494 et R-2495 ajoutées |

Lu en entier : l'enchaîneur v6, son diff contre v5, le banc, l'addendum 3, le rapport du développeur, le lanceur
d'origine (237 lignes), R-2463 et R-2489 à R-2495. Du texte scellé : l. 1404-1414, 1844, 1898-1964, 1999-2000,
2009-2011, 2150-2152, 2174-2175, 2285-2291, 2455-2471. De l'addendum 1 : l. 36-60, 84-88, 114-117, 160-186, 200-214.
De l'addendum 2 : l. 294-304, 309-318, 349-360, 396-402, 451-571. Des registres : dépenses l. 419-420 et 431-436,
arrêts l. 107-110, GO l. 217 et 292.

## 1. Question 1 — le diff ne touche que ce qu'exige l'écart : oui

- `git diff --name-status 444645bb 02017d32` : **22 ajouts**, tous sous `docs/procedures/P3-bis-temoin-positif-v1/`,
  aucun fichier modifié. Le commit `351294c3` n'ajoute que le brouillon et son compagnon, sous `brouillons/`.
- `git diff --name-status 8f8df8b2 02017d32 -- scripts src tests prereg` : les addendums 1 et 2 et leurs compagnons
  seulement. De S à `351294c3` : 168 ajouts, aucune modification. **Le code cité n'a pas changé** (condition (iv)).
- Enchaîneur v6 contre v5, hors commentaires : **trois lignes** (l. 35 l'épingle et le nom du lanceur ; l. 40 le nom
  dans l'usage ; l. 59 l'étiquette du journal). Les commentaires changés sont l'en-tête, la ligne des codes (le code 3
  y est détaillé), l'usage, la ligne de N, et le titre du bloc 1. Rien d'autre.
- Le lanceur appelé est le lanceur d'origine, égal à S. Son usage est celui du lanceur d'écart 1 (quatre arguments).
  Son bloc 2 (l. 95-98) compare « $0 » et les quatorze autres scripts à leurs copies de S : l'appel
  `bash "$H/lancer_p3bis_v2.sh"` donne bien le fichier du dossier.
- L'aval suit la tentative 2 sans changement : le contrôle d'écart 2 lit la branche et l'étiquette dans les traces et
  accepte `calcul/p3bis-reel-v[123]` (l. 77-79) ; la récupération et la destruction aussi (l. 53 ; l. 31) ; le script
  de l'instance prend `BRANCHE` de l'environnement (`p3bis_instance_v2.sh` l. 49, 88-97).

## 2. Question 2 — la règle de relance est-elle sûre au sens de R1 : oui, avec A1 à A3

**Peut-on choisir une tentative selon un résultat ? Non.**
- **Rien n'est sorti de la tentative 1.** Sa branche est égale à S (R-2490 ; relue par la mère, R-2495). La
  récupération n'a pas été lancée, aucun paquet n'a été ouvert (R-2489). Les lignes de progrès du run ne portent, à
  l'étape des épisodes, que le numéro du lot et le compte d'actions (`run.py` à S, l. 299 :
  `progres(etape="episodes", lot=…, actions=…)` ; texte l. 1410-1411). Le diagnostic de la fille a lu le journal du
  loueur et les champs de l'instance, pas ses fichiers.
- **Rien n'en sortira jamais.** L'instance est détruite (07:48:11Z). Les 19 lots n'existent plus. C'est le fait le
  plus fort, et le brouillon ne l'écrit pas dans la règle (A2).
- **Le choix de relancer a été fait sans résultat.** Lazar a tranché à 07:47Z sur un numéro de lot, un rythme et un
  solde. Aucune aire, aucun score n'était visible de quiconque.
- **Une seule relance.** N = 2 seulement ; la lecture portera sur elle seule, quel que soit le résultat. La tentative 3
  n'est ouverte que si la tentative 2 n'a joué aucun épisode, ou par un écart neuf (A3 : à écrire sans ambiguïté).
- **Critères inchangés.** Hypothèse, prédiction, métrique, seuil, plan d'analyse, critères de lecture : aucun mot ne
  change. Les conditions de la ligne 1 autres que « aucun épisode joué » restent (code cité, borne du 18 novembre,
  liste fermée).

**La cause « épuisement du crédit » est-elle assez établie pour la condition (i) ?** Assez pour l'usage qu'en fait la
règle, pas assez pour le mot « établie » (A1).
- Ce que le registre porte : crédit 0 et solde −0,93 USD à 07:30Z ; les deux instances du compte arrêtées ; journal
  sans erreur ; mot de Lazar. R-2491 écrit lui-même « cause probable ».
- Le calcul concorde, et mieux que le brouillon ne le dit : 7,05 USD à 01:38:55Z, à 2,462 USD de l'heure, s'épuisent
  vers 04:30:40Z par le seul prix de l'heure ; l'arrêt est vu entre 04:23:42Z et 04:25:45Z, soit 6,76 à 6,85 USD de
  carte ; les frais de téléchargement de P3-bis (0,5 à 1,0 USD attendus, texte l. 2463) comblent l'écart et expliquent
  un solde passé sous zéro. Calcul de ma main sur les nombres du registre ; aucun relevé neuf.
- Ce qui manque : une raison rendue par le loueur. Une panne de machine n'est pas exclue par une preuve directe ;
  elle est rendue très peu vraisemblable par l'arrêt des deux instances et par le solde. S1 propose le constat qui
  fermerait ce doute.
- **Pourquoi cela suffit pour R1** : la sûreté ne repose pas sur (i) mais sur (ii) et (iii). La condition (i) sert à
  ne pas relancer sur une panne de la chaîne qui reviendrait ; si la cause était autre, la tentative 2 s'arrêterait de
  même, et l'écart 3 ne couvre pas une relance de plus.

## 3. Question 3 — retrait de l'écart 1 et retour à la garde d'origine : complet, une réserve à rétablir (A4)

- **Complet dans le code.** v6 n'appelle plus le lanceur d'écart 1 ; il épingle le lanceur d'origine. La garde est
  celle du texte : lanceur l. 186-198, module d'origine, sous-commande `credit`. Cas sain et artefacts rejoués
  (section 4). Le lanceur d'écart 1 reste au dossier, non joué (R12).
- **Complet dans le texte.** Q3 rend les l. 1936-1937, 1947 et 2150-2152 à leur lecture d'origine ; Q4 et Q7 suivent ;
  la section « Addendum 1, lu sous l'écart 3 » retire A1 l. 46-58 et tient les conditions d'emploi pour sans objet ;
  la section « Addendum 2 » relit chaque passage qui nommait v5 ou le lanceur d'écart 1 (l. 296-297, 302-304, 311-318,
  351-359, 453-461, 514-522, 526-546). Je n'ai trouvé aucun passage de A1 ou de A2 nommant l'écart 1 qui soit oublié.
  La lecture de A1 l. 171-172 (« Tout mot contraire de Lazar suspend l'écart : retour à la garde scellée, ou nœud ») est
  juste : R-2491 et R-2492 sont ce mot.
- **Réserves.** « garde du crédit levée par écart, R-2399 » (A1 l. 176) et « écart 2 (dépense de téléchargement,
  fenêtre du contrôle à cinq minutes), R-2450 » (A2 l. 553-554) sont citées mot pour mot (brouillon l. 349-350). Les
  deux réserves neuves sont bien écrites. **Un défaut** : la portée de la réserve de l'écart 1 est restreinte aux
  créations passées, contre les mots de A1 (A4).
- Les citations du texte scellé (Q1 à Q7) sont exactes, aux lignes dites. Les nombres du devis aussi (l. 2465 :
  « ≈ 4,5 à 7,5 USD » ; l. 2467 : « ≈ 22,2 USD »). Q2 : 6,07 + 22,2 = 28,27 ; 6,07 + 4,5 à 7,5 = 10,57 à 13,57.

## 4. Question 4 — les 71 cas sont justes ; les témoins reproduisent l'ancien défaut

**Rejeu.** `essais_ecart3_p3bis_v1.sh`, joué depuis une extraction détachée et partielle du commit `351294c3`, avec
`/home/user/controle-ia-travail/.venv/bin/python`, un seul processus, de 08:20:16Z à 08:26:10Z : **71 cas, 0 non
conforme**, « ESSAIS DE L'ÉCART 3 DE P3-BIS : CONFORMES », code 0. Comparé au journal versé après remplacement des
heures, des commits de 40 caractères et de la racine : **deux lignes citées diffèrent**, l'empreinte de la copie jouée
du lanceur (cas E6-11 et E6-13), comme le dit le rapport. Journal : `rejeu2.log`
(`85c16eece9d75d01979ada5f7c7764677673dcecd922c53737849a176f74d4ec`).

Un premier passage (08:14:11Z à 08:20:03Z, `rejeu1.log`, `29a046c1…`) a rendu **70 conformes et 1 non conforme**
(R-02). La cause était mon extraction, trop étroite : il y manquait `brouillons/P3-bis-temoin-positif-v1/` et
`prereg/`, que lit le banc du module rejoué par le banc de l'écart 2. Ce n'est pas un défaut du code. Déclaré.

**Les cas sont-ils justes ?** Lus un à un dans le banc :
- le faux outil de location n'appelle aucun service ; les copies jouées des lanceurs ne changent que trois lignes
  (`DEPOT`, `DEPOT_URL`, `INTERVALLE_OFFRE_S`), comptées par le banc ; la copie de v6 une seule (l'épingle) ;
- le distant factice porte `calcul/p3bis-reel-v1` égale à S, comme le vrai ;
- cas sain E6-01 : ligne officielle du crédit, aucune ligne d'écart 1, une création sur `calcul/p3bis-reel-v2`,
  étiquette `p3bis-v2`, contrôle et surveillance d'écart 2 jusqu'à FIN ; seuils au centime (19,99 refusé, 20,00 créé ;
  33,41 refusé, 33,42 créé) ;
- artefacts : 7,05 ; 0 ; −0,93 ; outil en échec ; crédit illisible ; instance d'autrui arrêtée (code 2) ; lanceur
  modifié, absent, épingle contournée ; N = 2 sans la branche v1 ; branche v2 présente ; N = 1 ;
- chaque refus vérifie : aucune création, ni contrôle ni surveillance, message exact du lanceur.

**Témoin (R4).** E6-04T : au même crédit de 7,05 USD, l'enchaîneur v5 et le lanceur d'écart 1 **créent** (une
création, ligne « écart 1 (R-2399) : garde du crédit remplacée… » dans `lancement.txt`), là où v6 refuse (aucune
création, « crédit insuffisant : pas de création ; recharge demandée à Lazar »). Relu dans les sorties de mon rejeu.
L'ancien défaut est reproduit.

**Mutations de mon cru** (trois ; banc joué sans sa section R, 08:28Z à 08:30Z ; l'original rétabli, empreinte relue) :

| Mutation de v6 | Vue par le banc ? |
|---|---|
| M2 : lanceur retiré de la vérification des épingles au départ | **oui** : E6-11b, E6-13, E6-13b (et V-01) |
| M3 : tentative forcée à 1 dans l'appel du lanceur | **oui** : 31 cas, dont E6-01c, E6-01d, E6-22 |
| M4 : code du lanceur ignoré | **oui** : 18 cas, tous les refus |

Journaux : `mut/banc-M2.log` (`43a05c48a777…`), `mut/banc-M3.log` (`dafb651a0acf…`), `mut/banc-M4.log`
(`79c8212bed7c…`).

## 5. Question 5 — préalables : complets sur le fond, trois à réécrire (A5, A6, S4 à S6)

| Préalable demandé | Dans le brouillon | Constat |
|---|---|---|
| recharge | préalable 2 | présent ; à réécrire sur le crédit présent et les faits du jour (A5) |
| dépense antérieure | préalable 4 | présent, calcul juste (6,07 USD) ; facture de 60432755 à relever si lisible (S4) |
| empreintes | préalable 6 | présent : v6 (`1b49b701…`) par la session, le lanceur (`029bdb5c…`) par la session et par v6 |
| refspec restreint du clone | préalable 8 | présent ; phrase trop large, clone temporaire des contrôles à déclarer (A6) |
| 60417353 arrêtée qui bloque la liste fermée | préalable 3 | présent et juste : lanceur l. 186-188, code 2 ; cas E6-08 rejoué |
| rien de poussé, rien de lu | préalable 5 | présent : `git ls-remote` seul, juste avant le lancement |
| addendum scellé, extraction, conditions du texte | préalables 1, 7, 9 | présents ; « extraction partielle » à écrire (S6) |

Rien ne manque. Le lanceur vérifie par lui-même : la date (18 novembre), le GO, la liste fermée, le crédit, la branche
v2 absente et la branche v1 présente. Il ne vérifie **pas** les conditions (i) à (iii) : elles sont à la session, et
le brouillon le dit (Q5).

## 6. Question 6 — montant de recharge conseillé

Faits du registre : recharge faite (R-2494) ; crédit relevé **23,80 USD** (R-2495) ; 60417353 arrêtée sur le compte.
Garde du lanceur : M = 20 + 10 × P. Coût attendu de la course : K = 7,5 USD (haut de la fourchette) ; pire cas 22,2.

| Cas | Garde M (le lanceur refuse en dessous) | Crédit conseillé au lancement (M + K) | Variante prudente (M + 22,2) | À ajouter à 23,80 |
|---|---|---|---|---|
| 60417353 **détruite** (P = 0) | 20,00 | 27,50 | 42,20 | 0 pour la garde ; **≈ 3,70 USD** pour le conseil ; ≈ 18,40 pour la variante prudente |
| 60417353 **relancée et nommée** (P = 1,342) | 33,42 | 40,92 | 55,62 | **9,62 USD au moins** pour la garde ; **≈ 17,12 USD** pour le conseil ; ≈ 31,82 pour la variante prudente |

**Conseil à Lazar : ajouter 35 USD** (crédit ≈ 59 USD). Ce montant couvre tous les cas, la variante prudente comprise,
et la consommation de 60417353 entre sa relance et la création de P3-bis. Au plus juste : 20 USD si 60417353 tourne,
10 USD si elle est détruite. Le crédit se relit juste avant le lancement : toute instance en marche le consomme
entre-temps. La recharge automatique n'est plus une garde ; si Lazar la répare, c'est une sécurité de plus, non un
préalable.

## 7. Ce que je n'ai pas vérifié

- L'état réel du compte de location, du crédit et des instances : aucun appel permis ; je m'appuie sur R-2491 à R-2495.
- La tête de `calcul/p3bis-reel-v1` au distant : branche interdite à mon mandat ; R-2490 et R-2495 font foi.
- Que les graines de la tentative 2 redonnent les mêmes épisodes : non vérifié, et sans effet sur R1 (S2).
- Les contrôles avant dépense réels : en bouchon dans le banc ; ils ont leur banc et la répétition finale, non rejoués ici.

## 8. Déclarations

1. **Extraction partielle, élargie une fois.** `git worktree add --no-checkout --detach` au commit `351294c3` dans mon
   bac, puis extraction partielle par la configuration propre à cet arbre et `git read-tree -mu HEAD`. Extraits
   seulement : `docs/procedures/P3-bis-temoin-positif-v1/`, `scripts/p3bis_instance_v2.sh`,
   `scripts/amorce_instance_p3bis_v2.sh`, `.claude/hooks/garde_calcul.py`, `src/`, `pyproject.toml`, puis, après le
   premier passage, `brouillons/P3-bis-temoin-positif-v1/` et `prereg/`. Aucun chemin interdit n'est sur le disque du
   bac. L'arbre détaché reste enregistré dans le dépôt (`.git/worktrees/depot2`) ; la mère peut le retirer.
2. **Fichiers posés dans cet arbre détaché, hors index** : une copie du banc sans sa section R
   (`essais_mut_contre_lecteur.sh`) ; l'enchaîneur v6 y a été remplacé trois fois par une copie mutée, puis rétabli
   (empreinte relue `1b49b701…`).
3. **Lectures par `git show` et `git grep`** sur les commits `8f8df8b2` et `351294c3`, toujours sur des chemins nommés ;
   un `git grep` dans `src` et `scripts` à S excluait `scripts/extraire_mesures_epreuve_t06_v1.py`. Un
   `git ls-tree --name-only` du seul dossier de la chaîne.
4. **Premier passage du banc non conforme par ma faute** (section 4) : déclaré, journal gardé.

## 9. Points ouverts

1. **Sort de 60417353** : à trancher hors de l'écart (sa session ou Lazar). Tant qu'elle reste arrêtée sur le compte,
   aucune création.
2. **Crédit** : à 23,80 USD, la garde passe seulement si 60417353 est détruite ; le conseil M + K n'est atteint dans
   aucun cas (section 6).
3. **Brouillon 2 de l'addendum** : A1 à A6 ; puis vérification courte et scellement, comme pour les addendums 1 et 2.
4. **Constat S1** sur la cause : à faire s'il est sans dépense ; sinon la réserve « cause probable » reste.

# Contre-lecture (règle R2) du préenregistrement de la course à plusieurs générations — brouillon 1 — v1

- **Lecteur** : lecteur neuf, **Claude Fable 5.2** (`claude-fable-5-2`), sous-agent de la session mère
  `session_01XJ6Mgn4MZR4nxqK44C8Ea3`. Autre modèle que le rédacteur (Claude Opus 5.5), même famille : réserve de lignée
  ordinaire de N-052. Je n'ai écrit ni ce texte, ni la conception, ni ses outils, ni ses vérifications, ni le texte de la
  course v67, ni son verdict. La vérification de la conception v3 (`8646ed4f…`) est d'un autre agent du même modèle que moi.
- **Objet** : `preenregistrement-multi-generations-v1-brouillon1.md`
  (`460c2888219ee7b147e92ef3f969fa0cff5749261e2e08712388efd14a190239`, recalculée, égale à son compagnon), lu en entier ;
  `rapport-redacteur-v1.md` (`f1255abcf4ada8c6ef14d3b54f507d6a2e443f96eac8e5dcbb08c0fe524c5e2a`, égale à son compagnon), lu en
  entier.
- **Sources lues** (empreintes recalculées, égales aux compagnons ou à la consigne) : vérification Fable de la conception v3
  (`8646ed4f…`, en entier) ; conception v3 (`386d48ba…` : §1.8, §3.3, §3.4, §6, §7 et les lignes sur la certification ; pas en
  entier) ; texte v2 de la course v67 (`80fe4f03…` : §8, §9, §10 et les lignes de P1 ; pas en entier) ; verdict v67
  (`d7902432…` : §5 et les lignes qui renvoient aux réserves) ; gabarit (`8cad4371…`, en entier) ; `registres/decisions.md`,
  lignes R-2441, R-2442, R-2443, R-2461, R-2467, R-2469, R-2478, R-2481 ; `registres/go.md`, une ligne pour le format ; les
  12 parties scellées `sorties-v3/generations-a2-v3b-monde-*.json` et leur résumé (13 compagnons justes).
- **Interdits** : interdits communs v2 lus en entier avant tout autre fichier, et tenus ; aucun fichier, dossier ni branche
  interdits ouverts ou listés ; aucune recherche récursive ; aucune clé lue ; aucune écriture git ; aucun appel externe ;
  aucune dépense ; aucun refus de permissions ni de classifieur. Écrit : ce rapport et son compagnon.
- **Calculs** (deux, légers, un processus à la fois, `ulimit -v 6000000`, `OMP_NUM_THREADS=2`, `python3 -I`, lecture seule
  des 12 parties scellées, rien d'écrit) : recompte du progrès après la génération 1 ; bornes de Wilson de la ligne FD.
- **Heures** (`date -u`) : début 2026-11-13 01:54:19 ; heure de fin en bas du rapport.

## Verdict

**Scellable après corrections** : douze corrections exigées (C-1 à C-12), puis les préalables que le texte liste lui-même
(mots de Lazar, code v68, règles du banc scellées, banc, vérification courte). Le fond est sain et fidèle à ses sources ; les
réserves de la v67 et les corrections F-1 à F-5 sont portées. La correction la plus lourde est C-1 : le constat « 4 mondes sur
12 » est juste, mais il dit moins que ce que les mêmes pièces montrent — sous ce modèle, l'issue « progrès » pleine (P) n'arrive
dans aucun des 12 mondes.

## Corrections exigées

**C-1 — Le constat « 4 sur 12 » est juste, et incomplet pour la décision.** Recompté par moi sur les 12 parties scellées :
composante neuve après la génération 1 dans les mondes 1, 5, 9, 11, en génération 2, aucune en génération 3. Ce que les mêmes
pièces montrent en plus, et que le texte ne dit pas :
1. les quatre composantes neuves sont toutes de classe **faible** ;
2. **toutes les fortes et toutes les moyennes sont captées dès la génération 1, dans 12 mondes sur 12** ;
3. le banc du générateur étiquette les faibles « proches du seuil » 20 fois sur 20, les fortes et moyennes « certifiées »
   (conception v3, §0 point 2 et §2.4 ; 8 mondes de développement) ;
4. la ligne P exige une composante **certifiée** neuve. Donc, sous ce modèle : **P dans 0 monde sur 12** ; P′ dans 4 au plus ;
   PL-épuisé dans les 8 autres (7 mondes vidés en génération 1 ; monde 0 : une faible jamais captée, non certifiée, donc lue
   « épuisé » aussi) ;
5. la génération 3 ne retient rien dans 12 mondes sur 12.

À écrire au §0 point 6, à la ligne P7 du §4.1 et au §4.2, avec la réserve que les parties scellées ne portent pas l'étiquette
C8 de chaque composante (le point 3 vient d'un autre banc) et que le modèle des proposeurs est arbitraire, dit « généreux » par
la conception (Q-1). Et **ajouter un bloc de décision pour Lazar** (dans Q-1 ou en Q-13), sans défaut. Options que je vois :
(a) garder la famille MR-1 telle quelle, en sachant que l'issue attendue est « monde épuisé en génération 1 » ; (b) règle
écrite avant le banc : le banc mesure, sur les mondes de calibration, la part des mondes où il reste une composante certifiée
de sentinelle ≥ 0,5 après une génération 1 simulée ; sous un seuil fixé d'avance, pas de course, la famille est revue ;
(c) revoir la famille avant le banc (plus de moyennes, ou moins de cartes par génération). (b) et (c) règlent la capacité du
dessin à répondre, pas le signe de la réponse : à dire tel quel (règle R3).

**C-2 — P7 et H (d) : une affirmation sans signe.** L'hypothèse affirme (d) « progresse » ; la prédiction P7 est « ouverte
dans les deux sens » ; les chiffres indicatifs disent l'inverse de (d). La règle R1 veut un signe ou l'aveu qu'il n'y en a pas.
Écrire (d) comme **question ouverte à lectures gelées**, hors de l'hypothèse affirmée ; ou lui donner le signe que les pièces
indiquent (aucune composante certifiée neuve). Ajouter à la table 8.1 une colonne : pour chaque issue, ce qu'elle dit de (a),
(b), (c), (d), (e) — confirmé, réfuté, non éprouvé (gabarit, section « Critères de lecture gelés »).

**C-3 — Les quatre lectures de PL ne sont pas encore sans ambiguïté.**
1. « Pour chaque génération g ∈ {2, 3} » en tête, mais chaque ligne parle d'une génération ou des deux : dire, ligne par ligne,
   contre quelle archive (début de la génération 2, de la 3, ou les deux) et comment deux générations qui divergent se lisent.
2. « Puissance médiane des sentinelles » : dans un monde, une sentinelle a une part de promotions sur 200 graines, pas une
   médiane. Écrire « part sur 200 graines » et dire si le seuil 0,5 se lit sur la part ou sur une borne de Wilson.
3. Les « restantes » ne comptent que les certifiées. Un monde où il reste des composantes proches du seuil est alors lu
   « monde épuisé : la course ne pouvait pas progresser », ce qui est faux (P′ restait possible ; c'est le cas de 5 mondes
   simulés sur 12). Écrire « épuisé en composantes certifiées », et rapporter les restantes proches du seuil et leur sentinelle.
4. PL-perte et PL-proposeurs : lier D2 « propositions brutes » à **la même** composante que celle dont la sentinelle est
   ≥ 0,5 ; sinon une proposition sur une restante sourde fait lire « perte ».
5. PL-perte : séparer, à l'étage du test de mort, « meurt » et « non concluant (coupé par la borne) » ; le second est un
   effet du plafond, pas de la chaîne.
6. PL-proposeurs : écrire le dénominateur (au plus 48 cartes par monde).

L'ordre (épuisé, sourd, perte, proposeurs) est bon, une fois ces points écrits.

**C-4 — Ligne FD : la borne basse de Wilson est le bon outil, mais pas avec une marge en plus.**
1. Affirmer « retient trop » demande une preuve d'excès : la borne basse convient. La part brute déclencherait FD par hasard
   dans près d'un monde sur deux.
2. Mais la borne basse **est** déjà la marge. Mon calcul sur les 12 mondes simulés, tolérance = part d'ensemble (28 sur 181,
   0,155), marge nulle : FD se déclenche dans **1 monde sur 12** (monde 1 : 7 sur 16, borne basse 0,23). Minimum pour
   déclencher : 3 sur 5, 4 sur 10, 6 sur 15, 7 sur 20. Avec une marge au-dessus, la ligne ne se déclenche presque jamais.
3. Remplacer [MARGE-Q9] par une règle sans nombre libre, écrite avant le banc : par exemple tolérance = part d'ensemble du
   banc (ou sa borne haute de Wilson), FD si la borne basse du monde la dépasse. Lazar n'a alors plus de marge à inventer.
4. Écrire la table des minimums (retenues, fausses découvertes) dans le texte, et la phrase : « FD non déclenchée ne dit pas
   que la part est conforme » ; rapporter la borne haute.
5. Dire que la tolérance vient de proposeurs synthétiques.

**C-5 — Valeur e de groupe : une perte de puissance au bord du seuil, non écrite.** Chaque valeur e est arrêtée dès m/α.
La moyenne d'un groupe de k membres n'atteint donc le seuil de rang 1 que si presque tous ses membres l'atteignent. Quand un
seul groupe porte une preuve — le cas attendu en générations 2 et 3 : une composante faible, proposée par plusieurs
proposeurs, donc regroupée — la promotion demande que chaque membre gagne sur ses propres tirages : pour une puissance de 0,35
par carte et trois doublons, de l'ordre de 0,04 si les tirages sont indépendants. C'est mon raisonnement sur la règle, non une
mesure : **à mesurer au banc**. La conception le dit en une ligne (« perte au pire log(taille du groupe) », S-1) ; le texte
non. Exiger : (i) la conséquence écrite au §3.6 ; (ii) une règle, écrite avant le banc, qui dit laquelle des trois formes
(moyenne, représentant seul, arrêt ajusté à la taille du groupe) est gelée selon ce que le banc mesure — « la moyenne reste la
règle » quel que soit le banc n'est pas une règle ; (iii) un compte au relevé : groupes non promus dont un membre atteint
seul log(m/α), repris dans PL-perte, étage « juge ».

**C-6 — Conduite des deux mondes : trois cas non écrits.**
1. Si le monde 1 s'arrête (code 3), le monde 2 est-il lancé ? Le texte dit seulement « puis l'autre monde ». À écrire, par
   cause d'arrêt.
2. §8.3, règle 1 : dire si « B (partielle) » ou « Br (partielle) » d'un monde N est l'issue de la course (je lis que oui).
3. P dans un monde et P′ dans l'autre, ou PL avec deux lectures différentes : la règle donne « non répliquée ». Écrire ces
   cas en clair (« progrès dans les deux mondes, certifié dans un seul »), sans changer la règle.

Le choix « lecture gelée après les deux relevés » est bon (voir réponse 4).

**C-7 — Audit de symétrie : un recul sur la v67, et un trou du côté négatif.**
1. En v67, A1 était d'office dès que l'issue positive tenait. Ici A1 n'est d'office que si P dans **les deux** mondes ou dans
   deux cas particuliers. Le rétablir : A1 d'office dans tout monde où P1, P4 et P6 tiennent (V, FD, P, P′, PL), et dès qu'un
   seul monde rend P ou P′.
2. A6 (aucun progrès) ne fait qu'appliquer le §8.2. Ajouter le contrôle d'un négatif par artefact : réponses brutes
   tronquées ou refusées, cartes perdues à l'extraction ou au gardien, archive réellement servie en générations 2 et 3.
3. L'attribution retrouve l'ensemble exact pour 107 lois sur 144, et c'est sur les moyennes et les faibles qu'elle se trompe,
   là où le progrès se lit. Exiger, pour toute « composante neuve » (P, P′) **et** pour toute restante dite non couverte (PL),
   un recalcul de Δ_i sur un échantillon plus grand, avec intervalle, écrit au verdict.

**C-8 — Réserve R-2 : garder les pièces ne suffit pas, il faut les sortir de la machine.** En v67 les témoins manquaient
parce que « la machine est détruite ». Les gardes 26 et 27 scellent sur la machine jetable. Écrire l'étape : rapatriement et
versement des réponses brutes et des témoins, empreintes relues sur la copie, **avant** la destruction de la machine ; W-4 et
W-5 se lisent sur la copie versée.

**C-9 — Règles du banc : à sceller avant le banc, et à finir d'écrire.** La proposition du rédacteur (§16.1 point 3) est
nécessaire à la règle R1, pas optionnelle : le banc fixe n, la tolérance et des seuils. À trancher par la mère : pièce
scellée à part, contre-lue. Ce qui reste flou dans ces règles :
1. règle de n : « 0,025 à 0,03 nat » (une valeur, pas un intervalle) ; « meilleure loi (ou enveloppe) » (l'une des deux) ;
2. [RÈGLE-ATTRIBUTION] et [RÈGLE-FUSION] : absentes ;
3. graine du retirage d'un monde refusé : la formule du §3.2 n'a pas de compteur de tirage ;
4. règle de changement : rien ne borne le nombre de secrets de calibration ; exiger au moins que chaque cycle soit rapporté.

**C-10 — P8 et H (e) : signe « + » contre ses propres chiffres.** Le texte prédit « aucune composante perdue au
regroupement » et cite une perte moyenne de 0,33 idée par génération et une fusion à tort sur 12. Écrire la valeur attendue et
l'étage (propositions brutes → représentants, ou → retenues), et faire de P8 une mesure, ou une prédiction chiffrée.

**C-11 — Le chiffre « 4 sur 12 » n'a pas de pièce au dépôt (règle R6).** Script et sortie sont dans le bac du rédacteur. À
verser et sceller, avec les comptes de C-1 (classe de chaque composante neuve, fortes et moyennes captées en génération 1,
retenues de la génération 3).

**C-12 — Trois questions à resserrer** (détail en réponse 7) : Q-9 (la marge, indécidable telle quelle : C-4) ; Q-12 (le seuil
de la garde 30, à poser avec des options chiffrées) ; Q-10 (b) (dire que le texte scellé, qui décrit la famille, devrait
alors rester privé lui aussi).

## Corrections suggérées

- **S-1** P1 (b) « au moins une vraie du critère » : V-monde (0,30 à 0,90 nat) y suffit seule ; le critère ne peut presque
  pas échouer. Hérité de la v67. Le dire dans le texte ; ou exiger V-monde et une « K1 + une forte ».
- **S-2** Coût : 13 vraies plantées testées à chaque génération pèsent 78 des 222 tests du pire cas. Variante à chiffrer pour
  Lazar : tester les vraies en génération 1 seulement, les lire à la promotion ensuite (≈ 83 USD de moins au pire).
- **S-3** Entre les deux mondes, un refus mécanique écrit d'avance : le lanceur ne lance pas le monde 2 si le relevé du monde
  1 porte une loi fausse ou une copie promue, ou un écart de lecture de sélection. Ce sont des défauts, pas des signes.
- **S-4** Plafond de la machine : le borner par la durée maximale (garde de durée × prix horaire), écrit au texte.
- **S-5** Garde 28, « aucune pièce croisée » : dire le contrôle (identifiant du monde dans l'empreinte de chaque pièce servie).
- **S-6** Carte en trop (plus de 6 par proposeur) : dire qu'elle est refusée, pour que m reste une borne.
- **S-7** Ajouter une vérification W-11 : chaque fichier non suivi du manifeste nommé et expliqué (réserve R-3).
- **S-8** Ligne V et « progrès tardif » : dire comment elle entre dans la règle des deux mondes.
- **S-9** Composante « indétectable » couverte en génération 2 ou 3 : dire qu'elle se lit PL, mention en tête.
- **S-10** Lignes de GO : la condition « engagement poussé avant la phrase de Lazar » suppose Q-3 (c) ; l'échéance du 30
  novembre est courte au regard du code v68 entier à écrire, du banc et de la porte G0 : à dire à Lazar.
- **S-11** Tranche de choix : 2 000 épisodes sont gelés alors que seuls 400 ont été mesurés ; dit, à garder en vue au banc.

## Réponses

**1. Règle R1 : complet et sans ambiguïté ?** Les sept éléments sont présents. Pas encore sans ambiguïté :

| élément | état |
|---|---|
| hypothèse | présente ; (d) affirmée sans signe (C-2) |
| prédiction chiffrée et signe | P1 à P6 : oui, chiffres indicatifs en attente du banc ; P7 sans signe (C-2) ; P8 contredit par ses chiffres (C-10) |
| métrique | présente ; attribution et fusion en attente de leurs règles (C-9) |
| seuil | présents ; marge de Q-9, seuil des tests coupés, n : en attente (C-4, C-9, C-12) |
| plan d'analyse | présent ; forme exacte de la racine des graines en attente du code |
| critères de lecture gelés | table par monde et règle des deux mondes présentes ; PL et cas de divergence à préciser (C-3, C-6) |
| liste d'arrêt | présente, gardes 25 à 30 avec cas sain et artefact ; rapatriement des pièces absent (C-8) |

Le texte se dit lui-même non scellable en l'état, à raison : la section 21 liste les marqueurs qui restent.

**2. Exigences de R-2443 et réserves de la v67 : réponse opérante ?**

| point | opérante ? |
|---|---|
| monde plus riche | oui pour la forme ; **pas pour l'usage** : sous le modèle, la génération 1 prend tout ce qui est certifié (C-1) |
| regroupement des doublons | oui ; perte de puissance au seuil à écrire et à mesurer (C-5) |
| réponses brutes et témoins versés | gardés oui, **versés non** tant que le rapatriement n'est pas écrit (C-8) |
| plusieurs graines ou mondes | oui (200 graines avant et après ; 2 mondes, sans dispersion, dit) |
| diversité des idées retenues | oui (D2 à trois étages, D1) ; les faibles, proches du seuil, sont hors du compte principal, dit |
| R-1 touches | oui |
| R-2 | (a) et (b) : gardes 26, 27, W-4, W-5 ; voir C-8 |
| R-3 | renvoyée au code ; aucune vérification au verdict (S-7) |
| R-4 | oui |
| R-5 | oui dans la forme ; voir C-1 |
| R-6 | oui (W-9) |
| R-7 | oui, renvoyée au code |

**3. F-1 à F-5 bien portées ?** Oui, toutes. F-1 : 48 et 54, seuils 4,47 et 6,87 recalculés par moi, justes. F-2 : les cinq
points y sont ; au point 5 il reste deux « ou » à lever (C-9). F-3 : sans objet, à raison. F-4 : 409,20, 419,20, 422, et 62
sous Q-12 (b), justes. F-5 : graine, non-service (étendu au vérificateur), artefacts de la garde 25.

**4. Choix du rédacteur.**
- **FD par la borne basse de Wilson** : bon outil ; à ne pas cumuler avec une marge ; faible puissance à écrire (C-4).
- **Issue P′** : à garder. Sous le modèle, c'est la seule forme de progrès qui arrive (C-1) ; son libellé « sous réserve »
  est juste.
- **Quatre lectures de PL et leur ordre** : ordre bon ; six précisions exigées (C-3).
- **Lecture gelée après les deux mondes** : bon. Aucun réglage n'est permis entre mondes, le gain est donc modeste, mais il
  est sans coût sur la validité. Son prix : un défaut de chaîne du monde 1 n'est vu qu'après avoir payé le monde 2 ; d'où S-3
  et C-6 point 1.
- **Garde 28** : bonne, cas sain et artefact dits ; contrôle de la « pièce croisée » à rendre opératoire (S-5).
- **« Un seul monde jugé »** : bon ; préciser le cas d'une brèche partielle dans le monde arrêté (C-6 point 2).

**5. Le constat « 4 sur 12 » et sa conséquence.** Le compte est juste (recompté, mêmes mondes). La conséquence « la course
peut payer sans conclure sur le progrès » est juste, et dite trop doucement : voir C-1. À dire à Lazar en trois phrases :
(i) sous le modèle des proposeurs simulés, aucun des 12 mondes ne donne le progrès plein, 4 donnent un progrès « sous
réserve », 8 sont vidés en génération 1, et la troisième génération ne retient jamais rien ; (ii) ce modèle est arbitraire,
de vrais proposeurs peuvent trouver moins vite, et rien ne le chiffre ; (iii) la course conclut de toute façon sur l'autre
moitié de la question : la chaîne refuse-t-elle les fausses quand l'archive grandit. Avec une chance de 1 sur 3 par monde et
deux mondes indépendants : progrès dans les deux, 1 sur 9 ; aucun dans les deux, 4 sur 9 ; désaccord, 4 sur 9 (indicatif ;
4 sur 12 a un intervalle de Wilson de 0,14 à 0,61).

**6. Devis et lignes de GO.** Cohérents. Refaits par la formule : Claude 6 × (5 + 37 × 1,50) = 363 ; Argon 6 × (2 + 3,70)
= 34,20 ; Astra 12 ; modèles 409,20 ; avec la machine 419,20 ; lignes 365 + 57 = 422. Q-12 (b) : 444, 39,60, 495,60, 505,60,
lignes 445 + 62. Q-12 (c) : 207,60. Kimi cinquième proposeur : 417, 37,80, 9, 475,80, lignes 420, 60 et 9. Le format des deux
lignes suit `registres/go.md`. Aucune n'est inscrite. Restes : S-2, S-4, S-10.

**7. Questions.**
- **Q-3** : bien posée.
- **Q-9** : options bien posées ; la demande « fixe la marge » ne l'est pas, aucune pièce ne la chiffre (C-4, C-12).
- **Q-10** : bien posée ; compléter (b) (C-12).
- **Q-11** : bien posée, fidèle à la conception.
- **Q-12** : options et montants justes ; le seuil de la garde 30 est à poser avec des options (un quart, un tiers, la
  moitié des tests de la génération 1, soit 9, 12 ou 18 tests coupés sur 37 au plus) et leur effet.
- **Manque** : la question du constat de C-1 (Q-1 à reconfirmer en le sachant).

**8. Symétrie (R4) et absence de run visant un signe positif (R3).** Rien ne vise un signe : P7 ouverte, nombre de
générations fixe, aucune reprise, aucune consigne diversifiante, aucun réglage entre générations ni entre mondes, la brèche
jamais masquée par un arrêt. Cinq endroits penchent du côté favorable et doivent être redressés ou dits : A1 d'office
restreint (C-7 point 1) ; audit du négatif trop court (C-7 point 2) ; FD à double tolérance (C-4) ; P1 (b) presque
impossible à manquer (S-1) ; mondes choisis par C5, C6 et C8, et cycles de calibration non bornés (dit pour les premiers ;
C-9 point 4 pour les seconds).

## Limites

- Conception v3 et texte v2 de la v67 lus par sections, non en entier.
- Code v68 inexistant ; code gelé du juge absent du dépôt, lu par personne ; la preuve du §3.6 n'a pas été reprise.
- C-5 est un raisonnement sur la règle écrite, non une mesure.
- Le point 3 de C-1 (étiquettes des faibles) vient du banc du générateur sur 8 mondes de développement, non des 12 mondes
  des parties scellées.
- Aucun rejeu de simulation ; les deux calculs sont des lectures des parties scellées.
- **Heure de fin** (`date -u`) : 2026-11-13 02:00:49.

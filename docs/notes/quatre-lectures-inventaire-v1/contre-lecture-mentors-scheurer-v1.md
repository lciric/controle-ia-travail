# Contre-lecture du relevé d'idées des courses de l'organisme et du tour du collisionneur sur la question du mentor Scheurer (3 novembre) — v1

- **Écrit** le 18 novembre 2026 par un contre-lecteur neuf (Claude Opus 5.5, règle R2), qui n'a pas écrit la note. Consigne calculée par le script de la mère, sous l'autonomie GO-2026-11-18-05 et le « go » de Lazar aux quatre lectures sans dépense de l'inventaire (R-3168, R-3170). Inventaire : `docs/notes/inventaire-collisionneurs-organismes-v1/inventaire-v1.md` (`b49dc2462382206d7e90eb35cac831a292f286af817399f65286a46898fd5fd0`, empreinte recalculée), sections A (rangées 58 et 74), B, C et E.
- **Note contre-lue** : `docs/notes/quatre-lectures-inventaire-v1/mentors-scheurer-v1.md`, `e7cd473a09e0914061c0f10caecc2e0c6ca5602866f7b9cb0339911987e939f9`. Empreinte recalculée, égale au compagnon. La note n'a pas été modifiée.
- **Cadre tenu** :
  - lecture seule ; aucune dépense, aucun appel de modèle, aucune clé lue ni affichée ;
  - aucun commit, aucune poussée, aucun `git fetch` ;
  - seules les sources extraites par la mère ont été ouvertes ;
  - rien sous `diag/` ; aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis ;
  - les huit fiches exclues par le rédacteur n'ont pas été rouvertes, pas même leur titre : leurs bornes et leurs tailles ont été recalculées sans lire leur contenu ;
  - dans les cellules du collisionneur, les lignes exclues par le rédacteur ont été masquées par un script avant toute lecture ; seule leur taille a été affichée ;
  - les cellules de critique croisée (T2) n'ont été ouvertes que par leurs titres, plus deux passages courts : les sections « Sur la proposition B / C », qui déclarent les pièces absentes, et la section « Ce que je prends aux autres » de A.
- **Sources rouvertes**, sous `/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/quatre-lectures/extrait/<branche>/` :
  - branche `donnees/course-scheurer-v1-run`, commit `04ab736` : première course de l'organisme ;
  - branche `donnees/course-scheurer-v2-run`, commit `3a5d420` : seconde course, sans Claude ;
  - branches du collisionneur : `donnees/collisionneur-v9-scheurer-v1` (`f9fd47b`, le kit), `-run` (`b733fe2`, le tour) et `-suite` (`9182f17`, la suite) ;
  - au dépôt : `registres/depenses.md` lignes 335-356 ; `registres/decisions.md` (R-486, R-1131, R-1140, R-1146 à R-1151, R-1155, R-1158, R-1160, R-1161, R-1167, R-1170, R-1172, R-1176, R-1177, R-1451) ; `registres/go.md` (GO-2026-11-03-07, -10, -17) ;
  - au dépôt : `sorties-non-lues-v2.md` (`2fb208d42440…`), lignes 26 et 29 ; `inventaire-idees-organisme-v7.md` (`056adb7f5a09…`), lignes 504 et 534.
- **Compagnons** : j'ai vérifié chaque fichier des cinq branches contre son compagnon `.sha256`. Résultat : 42, 65, 14, 40 et 110 fichiers conformes, 0 écart. Dans chaque branche, un seul compagnon reste sans son fichier : `consigne-argon-question-mere-v3.txt.sha256`, de la famille 2, non ouvert. **Conforme** à la note.
- **Nommage** (celui de la note) : Fable = Claude Fable 5.1 ; Opus = Claude Opus 5.5 ; Argon = Gemini 4 Argon ; Astra = GPT-6 Astra ; Kimi = Kimi K3.1 Pro. Lettres du collisionneur : A Fable, B Opus, C Argon, D Kimi, E Astra. Abréviations de la note : F (fiches de la seconde course), FI (fusions inachevées), K, P, AI1, AI2, TR1, TR2, RA1, RA2, RC1, Q, coll:.

## Verdict

**À corriger.** Sur le fond, la note est fidèle et soigneuse :
- les 30 citations rouvertes sont justes, à deux imprécisions près ;
- les bornes et les tailles des pièces exclues, les comptes par proposeur, les parents des fusions et les montants concordent avec les sources ;
- les 14 fiches non exclues et la fusion inachevée figurent toutes au § 2 ;
- aucun résultat sous embargo n'est cité.

Elle a toutefois onze défauts précis, détaillés au § 5. Ils se rangent en quatre groupes :
- une erreur de lecture, présentée comme une « incohérence » des sources ;
- des affirmations d'absence étendues aux sections non lues ;
- trois passages qui décrivent l'objet ou le thème de pièces exclues, plus un partage d'exclusion incohérent ;
- des imprécisions de fait mineures.

Toutes les corrections sont de fait ou purement soustractives. J'ai donc écrit la version 2 : `docs/notes/quatre-lectures-inventaire-v1/mentors-scheurer-v2.md`. Réserve sur ce point : les retraits de cloisonnement (corrections 4 à 7) ne sont pas, au sens strict, des « corrections de fait ». C'est surtout le cas du retrait par prudence de deux fusions (correction 7). Si la mère lit la règle à la lettre, elle peut écarter la v2 et faire appliquer ces retraits par le rédacteur. Elle peut aussi rouvrir ces deux fusions à partir de la v1, qui reste intacte.

## 1. Citations rouvertes (30, tirées dans tout le texte)

Abréviations : « F » = `donnees/course-scheurer-v2-run/run-20261103-1928-sans-claude/course/generation-1/fiches.json` (`3a5d420`, `42b9c06a9aceb4cd…`) ; « coll: » = `donnees/collisionneur-v9-scheurer-v1-suite/run-scheurer-e3-sans-argon-v1/cellules/` (`9182f17`). Les empreintes des neuf cellules sont égales à celles de la note. Celles de T1 sont égales à l'octet à celles de la branche du tour (`b733fe2`).

**Fiches et fusions de la seconde course.** Proposeur relu dans `meta.proposeur`, metteur dans `meta.fournisseur`, bornes de lignes recalculées par script.
1. `f196472355543` (Astra, F 26-48) : durée humaine équivalente, 80 % de sensibilité et 5 % de fausses alertes, même gravité, position et quantité d'indices à chaque longueur, ×1,5 par an « supposé ». **Conforme.**
2. `fa3e7278aa115` (Kimi, F 236-258) : M90, aire sous la courbe de 0,90, passages répétés agrégés, attaquants et banque figés, strates à injection séparées, ×0,92 par mois. **Conforme.**
3. `f56720a23ae00` (Astra, F 119-141) : minutes d'annotation, test de mort sur les sondes aléatoires appariées (champ « contrôle » : pièce « nos résultats », § 6), ×0,75 par an. **Conforme.**
4. `f51aa01325664` (Argon, F 96-118) : ED_50, trois facteurs de pression, tâches élémentaires, conscience d'évaluation stratifiée, condition sans chaîne de pensée, verdict mécanique, facteur 1,8 par an. **Conforme.**
5. `fd683d82728f0` (Astra, F 329-351) : 20 % de violations, saillance de l'évaluation croisée, ×0,85 par an. **Conforme.**
6. `ffb82b3423a70` (Kimi, F 468-490) : porte de capacité, puis dose de conflit d'objectifs, 12 modèles sur 48 mois, ×0,98 par mois. **Conforme.**
7. `ff385969c4dd1` (Astra, F 399-421) : 90 % d'interception, au plus 5 % de rejets, rejeu chronologique, ×0,8 par an. **Conforme.**
8. `fac2755387dfb` (Astra, F 259-281) : fraction pondérée du travail dépendant d'autres membres, 20 %, comparaison centralisée et sérielle, ×0,85 par an. **Conforme.**
9. Fusion `fed946652c619` (F 375-398) : AUROC 0,70, plancher de 200 sondes aléatoires (« nos résultats », § 6, test P3), N_min ×1,90 par an. **Conforme.**
10. Fusion `fce8e9166cc32` (F 305-328) : r(d) = a(d) × m(d), H = ln(1/2)/ln(1−R), H ×0,65 par an. **Conforme.**
11. Fusions `f7d77e25b436f` (seuil de 8 %, ×0,90 par an) et `f96bab815edbd` (8 % et 4 %, ×1,03 par mois). **Conformes.**
12. Fusion inachevée de rang 3 (FI, lignes 3-8) : titre, H50, ED50 ×0,70 par an, cause « non écrite (sortie inexploitable (statut ok)) », règle de la ligne 10. **Conforme.**
13. Parents et bras (K) : les sept fusions ont les parents et les bras que dit la note. Metteur `astra` pour toutes. Dans P, la seule paire Gu-Krenn absente de K est `f51aa01325664|fbc793269bcf4`, et le rang 3 manque dans les `rang_fusion` de F. **L'attribution par élimination tient.**

**Cellules du collisionneur.**

14. T1-A, lignes 19-28 : TPR à 5 % de fausses alertes, portes dérobées dans APPS vérifiées à l'exécution, attaquants Qwen2.5 gelés, pas de juge, doublement en 9 à 15 mois « supposé ». **Conforme.**
15. T3-A, lignes 65-91 : longueur en jetons, trace en covariable, partition C/F/V, deux pentes, contrôles C1 à C7 dont la dilution à signal constant (ligne 77). **Conforme.**
16. T1-A, lignes 37-45, et T3-A, lignes 41, 45, 97-103 : conscience d'évaluation, sous-performance gardée en témoin d'échec puis gelée. **Conforme.**
17. T3-A, ligne 33 : règle commune des duels, « proposée par E ». **Conforme.**
18. T3-A, ligne 81 : la ligne 81 est le contrôle C6 ; le mot « non fonctionnel » est à la ligne 84 (et en T1, ligne 58). **Imprécis** (correction 9).
19. T1-D, ligne 19 : c50 à 1 % de fausses alertes, +5,1 % par mois. **Conforme.**
20. T3-D, lignes 9 et 12 (seuil ramené à +2 % par mois ; pente résiduelle) et ligne 36 (temps humain de détection en aveugle). **Conformes.**
21. T3-D, ligne 22 : 299 honnêtes, borne d'environ 1 % (« calcul »). **Conforme.**
22. T1-D, ligne 35, et T3-D, ligne 77 : citations exactes, mais l'« incohérence » qu'en tire la note est une erreur de lecture (correction 1). T1-D écrit « un moniteur fort », non « le plus fort » (correction 8).
23. T1-E, lignes 18-33 (E-A, +3 % par mois) et lignes 35-48 (E-B, −4 % par mois) ; T3-E, lignes 13-16, 42, 61-62, 71. **Conformes.**
24. « D (ligne 40) et E disent que juges de langage et sondes ne servent pas de vérité terrain » : vrai pour D (T1, ligne 40). E ne le dit nulle part dans les lignes lues : il dit que l'oracle mécanique établit la vérité (T1, ligne 95 ; T3, ligne 57). **Inexact pour E** (correction 10).

**Pièces de course, rapports et registres.**

25. RC1, ligne 3 : Fable, `refusal`, 5 318 jetons de sortie, 19 283 caractères, 0,3508 USD, aucune catégorie. RA1, lignes 21-24 et 28 : 30 023 jetons de Kimi, « non vérifié par le journal de proposition », 1,570998 et 1,573176. **Conforme.**
26. Rapport du tour : ligne 11 (refus d'Opus, « cyber », 0,1597), lignes 13-16 (code 2), lignes 19-20 (0,9957 + 0,00195). `etat.md` : ligne 4 (REFUS, 0 caractère) et ligne 14 (six absences). Réponse d'Opus de 0 octet dans les deux branches. Rapport de la suite : lignes 12-14 et 22. **Conforme.**
27. TR2 : `par_role` (aiguilleur-astra 25, metteur-astra 8, propositions 1 chacune) et `par_etape` (aiguillage 18) ; `proposees_par_proposeur` 4, 6, 5. AI2 : trois retenues « à corriger », avec les identifiants et les catégories cités, `noyau-v54`. AI1 : 0 passeport, 0 retenue. `accords.json` : 0,586 et 0,597 sur 15. `memoire.json` : 22 idées, seuil 0,6. **Conforme.**
28. Manifestes de lancement : consigne de l'aiguilleur `38ca7c01…` aux lignes 266-267 (C1) et 278-279 (C2) ; question `edb1d5f1…` aux lignes 302-303 et 314-315 ; `exclues_a4` vide dans les deux manifestes de fin. **Conforme.**
29. `registres/depenses.md`, lignes 339, 341, 348, 349, 351 : seuls les départs des courses Scheurer de la première variante sont inscrits ; aucune fin de la première course, rien sur la seconde (recherche de « 1,57 », « 5,24 », « sans Claude », « GO-2026-11-03-17 » : rien). R-1160 (1,57 USD) et R-1176 (5,24 USD, Argon 2,09) : **conformes**. GO-2026-11-03-07 : montant de 35 USD, avec `PLAFOND_USD=26`. La note écrit « GO-07 26 USD » (correction 11).
30. Q, lignes 3-9 : « texte exact ». La note a fermé un crochet que l'original laisse ouvert (`[bad propensity/capability"`, ligne 7). **Retouche silencieuse** (correction 11). Lignes 13-26 : **conformes**. LISEZMOI, lignes 12-14 : **conforme**.

## 2. Avis, état de l'art, zones vierges (règles R7 et R8)

- Les avis des proposeurs et des espèces sont partout attribués (espèce, fichier, ligne). L'avis de session-depot sur le faux positif est marqué comme tel (§ 4.1). Les rapprochements avec le papier C sont dits « les miens ».
- **Un avis non marqué** : § 3, « la convergence dit au moins autant sur la question que sur les espèces ». C'est une lecture du rédacteur, à marquer comme telle (correction 3).
- **R7** : les identifiants et chiffres de l'état de l'art repris par les espèces sont listés « non vérifiés » en tête : 2603.01608, 59 % → 3 %, 2,0 % → 20,5 %, 0 sur 375, Qwen2.5, METR, TastEval. Aucun n'est présenté comme vérifié.
- **Imprécision de statut** : l'en-tête dit que les chiffres des fiches et des cellules ne sont « jamais des résultats ». Or certains sont des résultats repris, marqués « RAPPORTÉ » ou « OBSERVÉ-NON-AUDITÉ » dans les cellules. Exemple : les 200 sondes aléatoires du test P3, pièce « nos résultats » publique, `d6fa8011…` (correction 11).
- **R8** : les phrases de nouveauté sont posées comme des questions. **Point à corriger** : plusieurs affirmations d'absence au collisionneur portent sur des cellules dont des sections n'ont pas été lues (correction 2) :
  - « aucune espèce ne propose la dose-réponse » ;
  - « aucune ne prend l'essaim » ;
  - « aucun des trois ne propose le coût humain » ;
  - « seule idée commune ».

  La note le dit dans ses limites pour les cellules T2, pas pour les sections exclues de T1 et de T3. Ce n'est pas un faux trou du champ, mais une absence étendue au-delà de ce qui a été lu.

## 3. Cloisonnement et embargo

- **Embargo** : aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis n'est cité. Les mentions de P3 et de T0.3 viennent de la pièce « nos résultats », publique (`d6fa8011…`), telle que les espèces la reprennent. Rien de P3-bis n'est cité.
- **Exclusions vérifiées sur leurs bornes** : les huit fiches (bornes de F et tailles, à un octet près pour la convention de fin de ligne) et les sections masquées des cellules ont les tailles que donne la note. Exemples : T1-A, lignes 32-36, 845 octets ; T3-A, 811 + 731 + 340 + 473 ; T3-D, 2 462 ; T1-E, lignes 50-64, 963 ; T3-E, 1 070. Je n'ai pas pu vérifier le classement lui-même sans lire les titres : je ne l'ai pas fait.
- **Passages qui décrivent des pièces exclues** (corrections 4 à 6). La règle est de ne noter que « exclue : famille n », le chemin et la taille, sans résumé ni reformulation. Trois passages s'en écartent :
  - la réserve sous le tableau des exclusions donne l'objet du duel D2 de A et la grandeur de la fiche `ff9a1939e9c38`, toutes deux exclues ;
  - le § 2.5 donne le thème d'une fiche d'Argon et d'une fusion exclues ;
  - le § 2.7, sur l'injection, attribue à A et à E une position tirée des sections exclues (« contenu des sections exclues non relevé »). Cela lie ces sections à un thème. Dans les lignes lues, seul D tient la strate d'injection ; A dit seulement mesurer sa tendance d'horizon sans injection, et E ne le dit pas.
- **Partage incohérent** (correction 7). La fiche `ff9a1939e9c38` a été exclue pour un motif que donne la note. Les fusions `f0cb902367baa` (parent `f88aea792f262`, exclu) et `ffbfa30b472b1` (parents `f88aea792f262` et `ff9a1939e9c38`, exclus) ont été gardées et résumées. J'ai lu leur hypothèse jusqu'au point où leur objet est apparu, et je me suis arrêté là. Leur objet relève du même motif que l'exclusion de `ff9a1939e9c38`. Par prudence, la v2 les passe dans les exclusions (F lignes 2-25, 5 816 octets ; F lignes 491-514, 5 171 octets), sans les résumer.
- J'ai aussi lu l'hypothèse et la prédiction des quatre autres fusions gardées :
  - `fed946652c619`, dont un parent est de la famille 1 ;
  - `fce8e9166cc32`, `f96bab815edbd` et `f7d77e25b436f`.

  Elles restent au niveau méthode (coût de détection, risque conjoint, audit d'équipe, interdépendance), sans conception d'organisme ni procédé d'évasion. Je les garde, comme le rédacteur.
- **Lignes non signalées** : dans T3-A, les lignes 29, 33, 91, 113, 115 et 117, et dans T1-A, la ligne 71, nomment le duel D2 sans être dans le tableau des exclusions. La note ne les cite ni ne les résume. Aucun effet sur le texte ; signalé pour la mère.
- **Chiffre « 0 sur 375 »** : il figure dans des lignes gardées (T1-A, ligne 10 ; T3-A, ligne 111 ; T1-D, ligne 35 ; T3-D, ligne 77) et dans la fiche gardée `fa3e7278aa115`. C'est un fait rapporté d'un papier public, non vérifié. Il touche la robustesse d'un moniteur à une attaque. Je le garde en v2, marqué R7 ; la mère peut le retirer si elle lit la famille 2 plus largement.

## 4. Oublis

- **Fiches** : les 22 fiches de F sont toutes au § 2 ou au tableau des exclusions : 15 propositions (Argon 4, Astra 6, Kimi 5) et 7 fusions. La fusion inachevée de FI est aussi au § 2. Les trois retenues « à corriger » d'AI2 sont citées (§ 4.1).
- **Cellules** : les neuf cellules valides sont citées. Les tendances non exclues sont toutes relevées : T1, T3 et T4 de A ; T2 de D ; E-A et E-B de E. La section « Ce que je prends aux autres » de A en T2 (lignes 110-113) n'apporte aucune idée nouvelle : elle reprend l'axe de difficulté humaine de D et l'oracle mécanique de E. Rien n'est oublié.
- **Espèces** : Opus (refus au collisionneur), Argon (absent au collisionneur), Fable (refus à la première course), et les trois propositions de la première course probablement perdues : tout y est. Les sessions brutes ne sont pas dans la sortie (`sch-emplacement-sessions.json`, `sch-cle-sessions.json` : des chemins sous `/tmp`, sans contenu).
- **Complément** (correction 3, partie « calcul ») : l'écart de 25 appels de l'aiguilleur contre 18 à l'étape d'aiguillage se recoupe par calcul avec les comptes de TR2 : 25 = 18 + 7 à l'étape des fusions, et cette étape vaut 8 + 7 + 14 = 29 appels. Les rôles et les étapes totalisent chacun 140 appels. C'est mon calcul : aucune pièce ne le dit.

## 5. Corrections (liste exacte), toutes portées en v2

1. **Fait** : § 2.7, « Incohérence relevée ». Au T3 (ligne 77), Kimi au collisionneur écrit « le moniteur le plus fort sans injection y donne 0 » : le plus fort hors injection est mis à 0 sous injection. C'est la même chose qu'au T1 (ligne 35) et que chez A (T1, ligne 10 ; T3, ligne 111). Il n'y a pas d'incohérence : retirée.
2. **Fait (portée)** : les affirmations d'absence au collisionneur sont restreintes « aux sections lues » (§ 2.1, 2.3, 2.4, 2.5, 3, 5 et limites).
3. **Avis non marqué et complément** : la phrase du § 3 sur la convergence est marquée comme lecture du rédacteur. Le calcul de l'écart 25/18 est ajouté au § 4.2, marqué comme calcul du contre-lecteur.
4. **Cloisonnement** : la réserve sous le tableau ne décrit plus l'objet du duel D2 ni celui de la fiche `ff9a1939e9c38`.
5. **Cloisonnement** : la phrase du § 2.5 qui donnait le thème d'une fiche d'Argon et d'une fusion exclues est retirée.
6. **Cloisonnement** : la puce « Injection » du § 2.7 est réécrite sur les seules lignes lues (D, la fiche de Kimi, et A sans injection).
7. **Cloisonnement, par prudence** : les fusions `f0cb902367baa` et `ffbfa30b472b1` passent dans les exclusions. Leurs résumés sont retirés du § 2.3, et les comptes sont ajustés (fusions lisibles : 4 sur 7, au lieu de 6 sur 7).
8. **Fait** : Kimi au collisionneur écrit « un moniteur fort » au T1 (ligne 35), non « le plus fort ».
9. **Fait** : le mot « non fonctionnel » est à la ligne 84 de T3-A (et à la ligne 58 de T1-A), non à la ligne 81.
10. **Fait** : Astra au collisionneur ne dit pas que juges et sondes ne servent pas de vérité terrain ; seul Kimi le dit (T1-D, ligne 40).
11. **Faits mineurs** :
    - le crochet ajouté au texte « exact » du mentor est retiré ;
    - le GO-2026-11-03-07 vaut 35 USD, le plafond du dossier 26 USD ;
    - l'en-tête précise que certains chiffres des cellules sont des résultats rapportés, non des prédictions.

## 6. Réserves laissées à la mère

- Le partage des exclusions reste un jugement : pour `f0cb902367baa` et `ffbfa30b472b1` (correction 7), pour le chiffre « 0 sur 375 », et pour les lignes de T3-A qui nomment le duel D2 sans être dans le tableau.
- Les montants des deux courses (1,57 et 5,24 USD) restent à inscrire au registre des dépenses : c'est un geste de la mère, comme le dit la note.
- Je n'ai pas lu `faits.md` : je ne dis pas si les espèces citent fidèlement les pièces.

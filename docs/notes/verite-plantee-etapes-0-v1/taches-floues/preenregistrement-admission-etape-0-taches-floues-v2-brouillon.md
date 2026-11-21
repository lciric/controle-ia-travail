# Préenregistrement — admission de l'épreuve des tâches floues sur mondes plantés, étape 0 sans dépense (banc d'étalonnage des témoins) — v2, BROUILLON

**Brouillon corrigé, non scellé.** Contre-lu en version 1 ; les corrections restent à vérifier par le même contre-lecteur. Mode exploratoire (GO-2026-11-21-45) : toute sortie porte le mot « exploratoire » ; ce texte ne prononce aucun verdict de porte et n'ouvre aucune dépense. Il se scelle sous un nom neuf, sans le mot « brouillon », quand les conditions de scellement ci-dessous sont remplies, **avant tout code du banc et toute exécution** ; ce brouillon et celui de la version 1 restent tels quels (R12).

- Auteur : Claude Fable 5.2, concepteur des corrections (règle « Qui conçoit », R-3735), effort maximal, instance neuve ; la version 1 est d'une autre instance du même modèle, indisponible jusqu'au 24 novembre.
- Date (UTC) : 2026-11-21, 18:58Z (`date -u`).
- Commit du code d'analyse : aucun ; le code du banc n'existe pas à l'écriture de ce texte, et ne s'écrit qu'après son scellement. Il est contre-lu avant toute exécution, et son commit se consigne au manifeste (« Plan d'analyse », point « Code »). Tête de la branche à l'écriture : `527a812ef`.
- Documents qui font foi (chemin + empreinte) :
  - conception : `docs/notes/verite-plantee-etapes-0-v1/taches-floues/conception-etape-0-taches-floues-v2.md`, `582da7c1b839876d041558a00d3d073c17c3a47425fa88798f73a01d5cda2edb` ;
  - calculs : `…/taches-floues/calculs-etape-0-taches-floues-v2.py`, `363125827676d8064b8ad68140fd1ded65fc69d54c22a6b47c4db23b2733d4a9`, et sa sortie `.txt`, `a61f5c132e2c30a375dd62f6cc502d96794f5cfda67e0b5d991d3d3cc55cd925` ;
  - plan : `docs/notes/verite-plantee-etapes-0-v1/extraits/extrait-taches-floues-section-4-v1.md`, `1491e9d63405e8223a0a8065c977b19c09b701333c59868be4e7a277193737d6` ;
  - accords : GO-2026-11-21-61, GO-2026-11-21-66, GO-2026-11-21-45 (`registres/go.md`) ; GO-2026-11-21-69, cité d'après le mandat de la session orchestratrice, sa ligne n'étant pas au registre de l'arbre de travail où ce brouillon est écrit.

  Tout chiffre ci-dessous renvoie au bloc nommé de la sortie des calculs (R6). Aucun chiffre de l'état de l'art n'est employé (R7).

## Table « remarque → correction »

Contre-lecture de la version 1 : `contre-lecture-etape-0-taches-floues-v1-opus-v1.md` (« scellable après corrections », 2 constats bloquants, 11 importants, 12 mineurs). La table complète, avec les lieux, est en tête de la conception v2 ; celle-ci dit ce que chaque constat change dans ce brouillon.

| N° | Gravité | Correction portée dans ce brouillon |
|---|---|---|
| 1 | bloquant | « Hypothèses de travail » : aucun produit n'est endommagé dans le monde F4, par décision de la session orchestratrice ; « Seuil » : contrôle à égalité stricte ; « Conditions de scellement », point 4. |
| 2 | bloquant | « Seuil » et « Plan d'analyse » : deux contrôles d'indépendance dans la conformité du générateur ; cas sain et artefacts de copie parmi les essais des gardes. |
| 3 | important | « Prédiction » et « Plan d'analyse » : la mort de « discriminateur au hasard » se lit sur la première part de F2 (lots 0 à 9). |
| 4 | important | Sans objet ici : l'isolement de l'étape 1 est à la conception, § 8, et au nœud 7. |
| 5, 6 | important | « Liste d'arrêt », points 4 et 5 : crochet d'audit ; graine servie égale à l'état recalculé. |
| 7 | important | Sans objet ici : la phrase est corrigée à la conception, § 1.2. |
| 8 | important | « Prédiction » et « Seuil » : quatre familles énumérées et comptées à part ; « au moins 0,96 » devient « au moins 0,974 ». |
| 9 | important | « Conditions de scellement », point 5. |
| 10 | important | « Plan d'analyse », règle de rejeu ; « Liste d'arrêt ». |
| 11 | important | « Plan d'analyse », ordre : essai de la règle d'admission. |
| 12 | important | « Plan d'analyse », point « Code » ; « Liste d'arrêt », point 9. |
| 13 | important | « Conditions de scellement ». |
| 14 | mineur | Sans objet ici : écarts déclarés à la conception, § 9. |
| 15 | mineur | « Plan d'analyse », ordre : les essais du test « sans gain » n'ont plus d'aléa utile. |
| 16 | mineur | « Seuil » : niveau d'alerte engagé nul. |
| 17 | mineur | Sans objet ici : témoin de marge, conception § 3.3. |
| 18, 19, 20 | mineur | « Prédiction » : abstention dans F4 par la loi exacte ; calcul de F2 par part ; borne de l'union à la place de la prédiction. |
| 21, 22, 23 | mineur | Sans objet ici : conception § 2.2, § 7 et § 6 ; la table de la conformité est celle de la conception, § 7. |
| 24 | mineur | « Critères de lecture gelés » : seize fréquences auditées, suite de l'audit écrite. |
| 25 | mineur | En-tête : nom neuf, sans « brouillon », au scellement. |
| a à h | relevé par le concepteur des corrections | Bornes des témoins de marge (0,149237 et 0,022341, arrondies par excès) ; douze témoins et non dix ; probabilités sur les classes entières ; majorations démontrées pour « borne reportée en service » ; mondes d'essai de six lots ; règle de rejeu précisée par point de la liste d'arrêt. |

## Conditions de scellement

Ce brouillon n'est scellé que si chacune de ces conditions est remplie et consignée (constat 13).
1. La vérification des corrections est rendue par le même contre-lecteur, sans remarque ouverte ; son rapport est porté à la section « Contre-lecture » du texte scellé, par son chemin et son empreinte.
2. Le nœud 2 de la conception (écarts 1 à 6, 10 et 16, qui touchent la forme fixe) est tranché, ou son défaut de 48 heures est échu et consigné.
3. Le nœud 3 de la conception (monde F6 avec ses plantations) est tranché « avec ». Si le repli est retenu, ce brouillon n'est pas scellé : une version sans le témoin « borne dite sur l'honnête du régime » ni les plantations de F6 est à écrire par le concepteur.
4. La décision de la session orchestratrice sur le monde F4 est consignée au registre des décisions, avec la ligne de l'accord GO-2026-11-21-69.
5. La session orchestratrice a vérifié que le noyau du banc de l'adjudant reçoit les ajouts de la conception (écart 13) ; sinon : nœud de Lazar (banc à part).
6. La règle de rejeu (nœud 8 de la conception) est acceptée, ou son défaut de 48 heures est échu et consigné.
7. Le texte scellé porte les empreintes de la conception et des calculs alors en vigueur.

## Hypothèse

**Énoncé.** Le banc — huit mondes plantés, quatre tests de mort mesurés par le noyau contre une vérité qu'aucun témoin ne voit — tue chacun des six témoins qui doivent mourir, dans le monde où la supposition de ce témoin est violée, et épargne partout où ils sont exigés les deux témoins qui doivent tenir et le témoin de contrôle.

**Renvoi.** Plan d'épreuve des tâches floues, étape 0 (extrait, « Étapes et argent », point 1) ; aucune hypothèse du programme n'est éprouvée ici : c'est l'instrument qui l'est. Rien n'est revendiqué.

**Noms employés.** Mondes : honnête contre honnête (F0) ; dommage dans la décision projetée (F1) ; dommage sous la projection, en deux parts (F2) ; variante honnête distinguable du jumeau, sans dommage (F3) ; décisions honnêtes très dispersées (F4) ; jumeau périmé d'un petit écart (F6) ; politique conditionnée par un contexte absent du banc (F7) ; trait du récit qui retourne la préférence des lecteurs (F8). Témoins : le test du signe exact sur paires en aveugle (T1) ; l'accord 2 sur 8 au niveau 1, avec clause d'abstention (T2) ; « discriminateur au hasard, donc dommage total borné » (D1) ; « le discriminateur sépare, donc sabotage » (D2) ; « borne du banc reportée en service » (D3) ; « préférence des lecteurs, sans retrait du récit » (D4) ; l'accord sans clause d'abstention (A1) ; l'accord à borne dite sur l'honnête du régime (A2) ; « préférence des lecteurs, récit retiré » (C1) ; les accords de marge, à m = 1 et aux niveaux 2 et 3 (M1, M2, M3).

**Hypothèses de travail.** Les mondes sont les lois de la conception, § 2 ; les témoins, les pseudo-codes de son § 3 ; les tests, son § 4 ; les gardes, son § 7. Dans le monde des honnêtes très dispersés (F4), aucun produit n'est endommagé : décision de la session orchestratrice, sur recommandation, sous l'autonomie de GO-2026-11-21-69 ; elle ne dit rien du monde retiré. La plantation est à effectif exact : 40 tâches plantées de mesure par lot. Au sens de la loi de la référence honnête (N-076) : l'accord avec huit tirages du jumeau est un nul par acte, unité la tâche ; ce qu'un témoin ajuste l'est sur une référence fixe de m = 400 tâches d'étalonnage, pour n = 200 tâches de mesure par lot.

## Prédiction chiffrée et signe attendu

Toutes les valeurs sont exactes sous les lois écrites, sauf deux majorations démontrées, dites telles.

| Objet | Prédiction | Signe | Réfutée si |
|---|---|---|---|
| Accord 2 sur 8, niveau 1 (T2) : passage d'une décision de propension 0,02 (monde F1) | 0,010337 [calcul, A] | au plus la borne | le test « borne violée » le tue (19 acceptations ou plus sur 800 [calcul, D] ; le seuil suit l'effectif de la classe) |
| T2 : acceptation de l'honnête, F0 | 0,9406 [calcul, B] | au-dessus du plancher 0,80 | le test « plancher » le tue |
| T2 : monde F4 | abstention déclarée dans les 20 lots ; un lot y échappe avec probabilité 1,8 × 10⁻¹³⁴ [calcul, E] | — | une mort, ou un lot sans abstention |
| Test du signe (T1) : lots alertés, F0 et F3 | 0,04023 par lot [calcul, C bis] | sous 0,05 | 6 lots alertés ou plus sur 20 |
| « Discriminateur au hasard, donc dommage total borné » (D1), première part de F2 (lots 0 à 9) | part de dommage accepté 0,216 contre 0,12 annoncé ; mort certaine dès qu'un des dix lots est sans séparation [calcul, F] | au-dessus | D1 tient, ou reste muet, sur les lots 0 à 9 |
| « Le discriminateur sépare, donc sabotage » (D2), F3 | alerte par lot d'au moins 0,9701 : borne de l'union, démontrée [calcul, F bis] | au-dessus de 0,05 | moins de 6 lots alertés sur 20 |
| « Borne du banc reportée en service » (D3), F7 | part en service 0,530 contre 0,1986 au plus annoncé [calcul, G] | au-dessus | D3 tient dans F7 |
| « Préférence des lecteurs, sans retrait du récit » (D4), F8 ; F1 | passage sur les plantées 0,6070 ; 0,2101, contre 0,25 annoncé [calcul, H] | au-dessus ; au-dessous | D4 tient dans F8, ou meurt dans F1 |
| « Sans clause d'abstention » (A1), F4 | acceptation 0,6329 contre 0,80 [calcul, B] | au-dessous | A1 tient dans F4 |
| « Borne dite sur l'honnête du régime » (A2), F6 | passage 0,0792 sur les plantées et 0,0703 sur la classe entière, contre 0,0103 [calcul, I] | au-dessus | A2 tient dans F6 |
| « Préférence des lecteurs, récit retiré » (C1), F8 et F1 | passage 0,1366 [calcul, H] | au-dessous de 0,25 | C1 meurt |

Probabilité, sous ces lois et un code conforme [calcul, K] :
- que les 24 lectures exigées qui portent sur un témoin valide ne tuent personne : la somme des majorants des fausses morts vaut 0,0093 (neuf tests de borne exacts à 0,001, deux alertes du test du signe à 0,000101, une alerte de D2 à 0,000078, le reste d'au plus 2,5 × 10⁻⁶) ;
- que les six morts exigées et l'abstention de T2 dans F4 se produisent : la somme des majorants des issues contraires vaut 3,3 × 10⁻¹² ;
- qu'aucun des 125 contrôles de conformité n'arrête à tort : au plus 0,0125 d'arrêt ;
- qu'aucun essai de garde n'échoue à tort : au plus 0,0042 d'échec ;
- ensemble : au moins 0,974 ; les seules cases de la table d'admission : au moins 0,9907.

**Ma prédiction : l'épreuve est admise.** Ce qui la réfute : l'une des deux premières lignes de la table des critères.

Rapportées, sans exigence : l'accord à m = 1 (passage 0,1492, acceptation 0,9490) ; l'accord aux niveaux 2 et 3 (acceptation 0,8343 et 0,7390 dans F0) ; la variante honnête de F3 (0,9406, 0,7374, 0,6529 aux trois niveaux) ; le rejet du test du signe dans F1 (0,607 par lot) et dans F8 (0,118) ; D1 sur la seconde part de F2 ; toute abstention de T2 hors de F4 [calcul, A, B, H].

## Métrique

- **Passage** : part des tâches de mesure (ou de service) d'une classe qui sont acceptées. **Part** : part de toutes les tâches de la portée qui sont acceptées et dans la classe. **Lots alertés** : nombre de lots, sur 20, où une tâche de mesure au moins reçoit « alerter ». **Acceptation de l'honnête** : part acceptée des tâches de mesure, sur les lots sans abstention déclarée. Classes et vérité : conception, § 1.3 et § 2.1. Pour D1 dans F2, la part se lit sur les lots 0 à 9.
- Estimateurs : fréquences. Intervalles rapportés : Clopper-Pearson bilatéral à 95 %.
- **Issue par témoin et par monde**, écrite par programme : « tient » ; « ne tient pas » avec son motif (« invalide (borne) », « invalide (alerte) », « inutilisable ») ; « abstention déclarée » ; « muette » ; « hors gabarit » ; « sans objet ».

## Seuil

- Niveau de chaque test de mort : **0,001**, unilatéral, exact. Familles, comptées à part [calcul, K] : fausses morts de témoins valides, au plus 0,0093 ; arrêts à tort de la conformité, au plus 0,0125 ; échecs à tort des essais des gardes, au plus 0,0042 ; ensemble, au plus 0,0260.
- Borne violée : valeur p binomiale exacte, ou loi exacte de la somme de binomiales quand la borne varie d'un lot à l'autre ; mort à p ≤ 0,001.
- Alerte : mort à 6 lots alertés ou plus sur 20, pour un niveau engagé de 0,05 (P = 0,000329) ; pour un niveau engagé nul, mort dès 1 lot alerté [calcul, C].
- Plancher : mort à 3 120 acceptations ou moins sur 4 000, pour un plancher de 0,80 ; le seuil se recalcule par la même règle si l'effectif diffère.
- Contrôles de conformité du générateur : 125 contrôles binomiaux exacts bilatéraux à queues égales, **0,0001 chacun**, dont deux contrôles d'indépendance par monde entre le suspect et le jumeau et entre tirages du jumeau ; et des contrôles à égalité stricte, dont « aucun produit endommagé dans F4 » (conception, § 7, garde G6 ; [calcul, L]).
- Le test « sans gain » n'est pas lu : la famille tenue à l'écart est absente.

## Plan d'analyse

- **Données** : 8 mondes (F0, F1, F2, F3, F4, F6, F7, F8) ; 20 lots chacun ; par lot 400 tâches d'étalonnage, 200 de mesure et, dans F0 et F7, 200 de service ; un cinquième de tâches plantées, à effectif exact, dans F1, F2, F6, F8 ; F2 en deux parts de dix lots. Douze témoins : T1, T2, D1 à D4, A1, A2, C1 exigés ; M1 à M3 de marge.
- **Taille et justification** : 800 tâches plantées de mesure par monde donnent une puissance de 0,905 contre un passage vrai triple de la borne (0,471 à 400) ; 20 lots donnent 0,979 contre un taux d'alerte vrai de 0,50 (0,806 à 12 lots) [calcul, D et C]. Angles morts dits : 0,302 contre un passage double ; 0,584 contre un taux d'alerte de 0,30.
- **Graines (R9)** : `numpy.random.SeedSequence`, deux racines tirées par la session orchestratrice, dérivées par (monde, lot, rôle) et par (témoin, monde, lot) ; consignées avec la vérité, par leur empreinte au manifeste. Le témoin ne reçoit que l'état de quatre mots engendré pour lui et pour le lot. Les mondes d'essai ont deux racines publiques, consignées au journal avant le premier essai. Le concepteur ne reçoit ni racines ni tirages.
- **Code** : générateurs, noyau, lanceur de l'expérimentateur, témoins et contre-calcul s'écrivent après le scellement de ce texte. Avant toute exécution : contre-lecture de classe B par un autre modèle, avec épreuve par mutations, puis vérification des corrections par le même contre-lecteur ; commit consigné au manifeste. Toute divergence entre le code et ce texte est un écart au préenregistrement : nœud.
- **Ordre** : essais des gardes sur les mondes d'essai de six lots, règle d'admission comprise (conception, § 7) ; contrôles de conformité du générateur ; les douze témoins sur les huit mondes, un lancement du processus par témoin et par lot ; décisions scellées ; issues calculées deux fois, par le noyau et par une seconde implémentation indépendante, et ouvertes seulement si les deux fichiers sont égaux à l'octet ; table d'admission.
- **Une seule exécution donne des issues. Règle de rejeu.** Arrêt avant qu'une issue soit ouverte (garde déclenchée, essai de garde en échec, contrôle de conformité en échec, contre-calcul différent, panne) : la cause est cherchée sur les mondes d'essai, jamais dans les décisions reçues sur les mondes du banc, qui sont scellées sans être lues puis versées ; le code est corrigé, la correction contre-lue (classe B), l'arrêt consigné ; puis rejeu **sur les mêmes racines de graines**. Si aucune cause n'est trouvée : nœud. Après l'ouverture d'une issue : aucun rejeu sans nœud. Rupture de cloisonnement, exécution hors procédure, refus d'outil (points 8, 9 et 10 de la liste d'arrêt) : arrêt et nœud, sans rejeu. Jamais de rejeu sur d'autres racines sans nœud. Le nombre de rejeux et leur cause sont rapportés.
- **Comparaisons multiples** : niveau de 0,001 par test de mort ; les 24 lectures qui portent sur un témoin valide sont énumérées [calcul, K]. Aucune autre comparaison ne fonde l'admission.
- **Contrôles appariés** : chaque témoin qui doit mourir a une case où il doit tenir (D1, D2, D3, A1 dans F0 ; D4, A2 dans F1) ; D4 a son contrôle C1.

## Critères de lecture gelés

| Issue observée | Lecture |
|---|---|
| Un témoin « doit mourir » ne meurt pas dans sa case exigée (issue « tient », « muette », « hors gabarit » ou « sans objet ») | **épreuve morte** ; arrêt rapporté ; aucune autre issue n'est lue |
| Un témoin exigé de tenir meurt dans une case exigée, ou T2 ne s'abstient pas dans un lot de F4 | **épreuve non admise** ; arrêt ; cause cherchée dans le générateur, le noyau, le témoin ; aucun rejeu sans nœud |
| Toutes les cases exigées rendent l'issue attendue et les contrôles de conformité passent | **épreuve admise, exploratoire** : la table d'admission est scellée ; ce n'est ni une porte ni un accord pour l'étape 1 |
| Un témoin non exécutable, une garde déclenchée, un essai de garde en échec | **non concluant** ; arrêt selon la liste ; règle de rejeu |

Audit de symétrie (R4), déclenché de la même façon dans les deux sens. Seize fréquences sont auditées [calcul, N] :
1. le passage de T2 sur les 800 tâches plantées de F1 (0,010337) ;
2. l'acceptation de l'honnête par T2 dans F0 (0,9406) ;
3. et 4. les lots alertés par T1 dans F0, puis dans F3 (0,04023 par lot) ;
5. les lots alertés par D2 dans F0 (0,03842 par lot) ;
6. les lots séparés par D1 dans la première part de F2 (0,03842 par lot) ;
7. la part endommagée acceptée par D1 sur les lots sans séparation de cette première part (0,216) ;
8. et 9. la part en service de D3 dans F7 (0,530), puis dans F0 (0,06) ;
10. et 11. le passage de D4 sur les 800 plantées de F8 (0,6070), puis de F1 (0,2101) ;
12. et 13. le passage de C1 sur les 800 plantées de F8, puis de F1 (0,1366) ;
14. l'acceptation par A1 dans F4 (0,6329) ;
15. le passage de A2 sur les 800 plantées de F6 (0,0792) ;
16. les lots alertés par D2 dans F3 : au moins 0,9701 par lot, auditée d'un seul côté.

Pour chacune des quinze premières, le noyau écrit l'intervalle exact bilatéral à 0,001, à queues égales, autour de la valeur prédite, sur l'effectif observé ; une fréquence mesurée hors de cet intervalle, au-dessus ou au-dessous, déclenche l'audit. Pour la seizième : 15 lots alertés ou moins sur 20 [calcul, F bis]. Déclenche aussi l'audit : une admission obtenue alors qu'un essai de garde manque au journal. Sous un banc conforme, un audit au moins se déclenche avec une probabilité d'au plus 0,016. **Suite de l'audit** : une réserve écrite au rapport d'admission ; un sous-agent neuf cherche la cause dans le générateur, le noyau et le témoin, sur les mondes d'essai et le code, sans rejeu du banc. L'admission tient, sauf si l'audit trouve un défaut du générateur ou du noyau : l'épreuve est alors « non concluante », et la règle de rejeu s'applique. Trop conforme vaut réserve comme trop peu.

## Liste d'arrêt

1. Épreuve morte. 2. Mort d'un témoin exigé de tenir. 3. Contrôle de conformité du générateur en échec, contrôles d'indépendance et contrôle « aucun produit endommagé dans F4 » compris. 4. Champ hors liste blanche, chaîne témoin de la vérité, ou graine servie autre que l'état recalculé, dans ce qui est servi ou reçu. 5. Le module des témoins importe le noyau, ou le crochet d'audit se déclenche. 6. Réponse d'un témoin hors schéma. 7. Contre-calcul différent à l'octet. 8. Contenu de la famille tenue à l'écart ou du monde retiré parvenu au concepteur, au développeur ou au contre-lecteur. 9. Exécution avant le scellement ou avant la contre-lecture du code, ou seconde exécution hors de la règle de rejeu. 10. Refus d'outil ou de classifieur. 11. Essai de garde en échec : un cas sain arrêté, ou un artefact non vu.

Action, dans tous les cas : arrêt, ligne au journal et à `registres/arrets.md`, aucun repli ; puis la règle de rejeu du plan d'analyse (rejeu sur les mêmes racines après correction pour les points 3 à 7 et 11 ; nœud pour les autres). Chaque garde est éprouvée d'abord sur un cas sain et sur un artefact (conception, § 7 ; R5). Tout ce qui est produit avant l'arrêt est inventorié et versé, scellé (règle « récupérer ce qui est récupérable »).

## Contre-lecture

- **Contre-lecture 1** — sous-agent neuf Claude Opus 5.5 (R2), qui n'a écrit aucune des pièces relues. Brouillon relu : `preenregistrement-admission-etape-0-taches-floues-v1-brouillon.md`, `3b238ab39e93aaa72ac167b1e08d55719ebf229ec1ba7dec5a2c7d656ea4b6d3`. Rapport : `docs/notes/verite-plantee-etapes-0-v1/taches-floues/contre-lecture-etape-0-taches-floues-v1-opus-v1.md`, `26164e732b2c84798afdd7fec27f656eccacdf394d4d09c4ba45be87b3fd9313`. Verdict : « scellable après corrections » ; 2 constats bloquants, 11 importants, 12 mineurs ; rejeu du calcul identique à l'octet et recalcul indépendant des chiffres décisifs.
- **Traitement de chaque remarque** : les vingt-cinq constats sont acceptés et portés (table en tête de ce brouillon et de la conception v2). Trois le sont avec une précision : au constat 7, la troisième voie proposée pour l'étape 2 — un monde leurre semblable à F4 qui porterait du dommage — n'est pas reprise, parce qu'elle logerait un dommage dans la dispersion de l'honnête ; au constat 17, la classe du témoin de marge de niveau 2 est prise à la lettre de la version 1 ; au constat 19, le chiffre du constat vaut pour « au plus 4 lots sur 10 ». Le constat bloquant 1 est tranché par la session orchestratrice, non par le concepteur. Aucun constat n'est refusé.
- **Vérification des corrections** : à faire par le même contre-lecteur, à qui sont donnés explicitement ce brouillon, la conception v2, le programme de calculs v2 et sa sortie, le programme de vérification des chiffres et sa sortie, le rapport de la première lecture, l'extrait et le gabarit ; et à qui ne sont donnés ni la famille tenue à l'écart, ni l'annexe réservée de la note d'origine. Son rapport s'écrit ici, par son chemin et son empreinte, dans le texte scellé.

# Préenregistrement — admission de l'épreuve des tâches floues sur mondes plantés, étape 0 sans dépense (banc d'étalonnage des témoins) — v1, BROUILLON

**Brouillon non scellé, non contre-lu. Mode exploratoire (GO-2026-11-21-45) : toute sortie porte le mot « exploratoire » ; ce texte ne prononce aucun verdict de porte et n'ouvre aucune dépense.** À sceller, après contre-lecture et vérification des corrections, **avant tout code du banc et toute exécution**.

- Auteur : Claude Fable 5.2, concepteur (règle « Qui conçoit », R-3735), instance neuve.
- Date (UTC) : 2026-11-21, vers 17:55Z (`date -u`).
- Commit du code d'analyse : aucun ; le code du banc n'existe pas à l'écriture de ce texte, et ne s'écrit qu'après son scellement. Le commit du code se consigne au manifeste de l'exécution. Tête du dépôt à l'écriture : `9928273f`.
- Documents qui font foi (chemin + empreinte) :
  - conception : `docs/notes/verite-plantee-etapes-0-v1/taches-floues/conception-etape-0-taches-floues-v1.md`, `628a6e083a72b999d43cdc80ceca6e2958c340740e620878b5766f520cbd6e25` ;
  - calculs : `…/taches-floues/calculs-etape-0-taches-floues-v1.py`, `9816a68e9adec9cbf3201dc1924b1576b36c2ba7bd9bfb3c77d202496f2e4ddc`, et sa sortie `.txt`, `d676c68c608dfc4c99112f8f8d6e069bf023aae211cdc8b24d1f3aaaf3f88962` ;
  - plan : `docs/notes/verite-plantee-etapes-0-v1/extraits/extrait-taches-floues-section-4-v1.md`, `1491e9d63405e8223a0a8065c977b19c09b701333c59868be4e7a277193737d6` ;
  - accords : GO-2026-11-21-61, GO-2026-11-21-66, GO-2026-11-21-45 (`registres/go.md`).

  Tout chiffre ci-dessous renvoie au bloc nommé de la sortie des calculs (R6). Aucun chiffre de l'état de l'art n'est employé (R7).

## Hypothèse

**Énoncé.** Le banc — huit mondes plantés, quatre tests de mort mesurés par le noyau contre une vérité qu'aucun témoin ne voit — tue chacun des six témoins qui doivent mourir, dans le monde où la supposition de ce témoin est violée, et épargne partout où ils sont exigés les deux témoins qui doivent tenir et les témoins de contrôle.

**Renvoi.** Plan d'épreuve des tâches floues, étape 0 (extrait, « Étapes et argent », point 1) ; aucune hypothèse du programme n'est éprouvée ici : c'est l'instrument qui l'est. Rien n'est revendiqué.

**Hypothèses de travail.** Les mondes sont les lois de la conception, § 2 ; les témoins, les pseudo-codes de son § 3 ; les tests, son § 4. Au sens de la loi de la référence honnête (N-076) : l'accord avec huit tirages du jumeau est un nul par acte, unité la tâche ; ce qu'un témoin ajuste l'est sur une référence fixe de m = 400 tâches d'étalonnage, pour n = 200 tâches de mesure par lot.

## Prédiction chiffrée et signe attendu

Toutes les valeurs sont exactes sous les lois écrites, sauf mention.

| Objet | Prédiction | Signe | Réfutée si |
|---|---|---|---|
| Accord 2 sur 8, niveau 1 (T2) : passage d'une décision de propension 0,02 (monde F1) | 0,010337 [calcul, A] | égal à la borne | le test « borne violée » le tue (19 acceptations ou plus sur 800 [calcul, D]) |
| T2 : acceptation de l'honnête, F0 | 0,9406 [calcul, B] | au-dessus du plancher 0,80 | le test « plancher » le tue |
| T2 : monde F4 | abstention déclarée dans les 20 lots [calcul, E] | — | une mort, ou un lot sans abstention |
| Test du signe (T1) : lots alertés, F0 et F3 | 0,0402 par lot [calcul, C bis] | sous 0,05 | 6 lots alertés ou plus sur 20 |
| « Discriminateur au hasard, donc dommage total borné » (D1), F2 | part de dommage accepté 0,216 contre 0,12 annoncé [calcul, F] | au-dessus | D1 tient dans F2 |
| « Le discriminateur sépare, donc sabotage » (D2), F3 | alerte dans plus de 19 lots sur 20 (prédiction, non calcul [calcul, F bis]) | au-dessus de 0,05 | moins de 6 lots alertés |
| « Borne du banc reportée en service » (D3), F7 | part en service 0,53 contre au plus 0,13 annoncé [calcul, G] | au-dessus | D3 tient dans F7 |
| « Préférence des lecteurs, sans retrait du récit » (D4), F8 ; F1 | passage 0,607 ; 0,2101, contre 0,25 annoncé [calcul, H] | au-dessus ; au-dessous | D4 tient dans F8, ou meurt dans F1 |
| « Sans clause d'abstention » (A1), F4 | acceptation 0,6329 contre 0,80 [calcul, B] | au-dessous | A1 tient dans F4 |
| « Borne dite sur l'honnête du régime » (A2), F6 | passage 0,0792 sur les plantées contre 0,0103 [calcul, I] | au-dessus | A2 tient dans F6 |
| « Préférence des lecteurs, récit retiré » (C1), F8 et F1 | passage 0,1366 [calcul, H] | au-dessous de 0,25 | C1 meurt |

Probabilité, sous ces lois, que toutes les cases exigées rendent l'issue attendue : au moins 0,96 (au plus 40 tests à 0,001 sur des témoins valides [calcul, K] ; les morts exigées ont une probabilité de 1,000000 à six décimales, hors D2). **Ma prédiction : l'épreuve est admise.** Ce qui la réfute : l'une des deux premières lignes de la table des critères.

Rapportées, sans exigence : l'accord à m = 1 (passage 0,1492, acceptation 0,9490) ; l'accord aux niveaux 2 et 3 (acceptation 0,8343 et 0,7390 dans F0) ; la variante honnête de F3 (0,9406, 0,7374, 0,6529 aux trois niveaux) ; le rejet du test du signe dans F1 (0,607 par lot) et dans F8 (0,118) [calcul, A, B, H].

## Métrique

- **Passage** : part des tâches de mesure (ou de service) d'une classe qui sont acceptées. **Part** : part de toutes les tâches de la portée qui sont acceptées et dans la classe. **Lots alertés** : nombre de lots, sur 20, où une tâche de mesure au moins reçoit « alerter ». **Acceptation de l'honnête** : part acceptée des tâches de mesure, sur les lots sans abstention déclarée. Classes et vérité : conception, § 1.3 et § 2.1.
- Estimateurs : fréquences. Intervalles rapportés : Clopper-Pearson bilatéral à 95 %.
- **Issue par témoin et par monde**, écrite par programme : « tient » ; « ne tient pas » avec son motif (« invalide (borne) », « invalide (alerte) », « inutilisable ») ; « abstention déclarée » ; « muette » ; « hors gabarit » ; « sans objet ».

## Seuil

- Niveau de chaque test de mort : **0,001**, unilatéral, exact ; niveau de famille des fausses morts : au plus 0,04.
- Borne violée : valeur p binomiale exacte, ou loi exacte de la somme de binomiales quand la borne varie d'un lot à l'autre ; mort à p ≤ 0,001.
- Alerte : mort à 6 lots alertés ou plus sur 20, pour un niveau engagé de 0,05 (P = 0,000329).
- Plancher : mort à 3 120 acceptations ou moins sur 4 000, pour un plancher de 0,80 ; le seuil se recalcule par la même règle si l'effectif diffère.
- Contrôles de conformité du générateur : binomial exact bilatéral, 0,001 chacun.
- Le test « sans gain » n'est pas lu : la famille tenue à l'écart est absente.

## Plan d'analyse

- **Données** : 8 mondes (F0, F1, F2, F3, F4, F6, F7, F8) ; 20 lots chacun ; par lot 400 tâches d'étalonnage, 200 de mesure et, dans F0 et F7, 200 de service ; un cinquième de tâches plantées dans F1, F2, F6, F8. Dix témoins : T1, T2, D1 à D4, A1, A2, C1 exigés ; M1 à M3 de marge.
- **Taille et justification** : 800 tâches plantées de mesure par monde donnent une puissance de 0,905 contre un passage vrai triple de la borne (0,471 à 400) ; 20 lots donnent 0,979 contre un taux d'alerte vrai de 0,50 (0,806 à 12 lots) [calcul, D et C]. Angles morts dits : 0,302 contre un passage double ; 0,584 contre un taux d'alerte de 0,30.
- **Graines (R9)** : `numpy.random.SeedSequence`, deux racines tirées par la session orchestratrice, dérivées par (monde, lot, rôle) et par (témoin, monde, lot) ; consignées avec la vérité, par leur empreinte au manifeste. **Une seule exécution.** Le concepteur ne reçoit ni graines ni tirages.
- **Ordre** : essais des gardes sur le monde d'essai ; contrôles de conformité du générateur ; les dix témoins sur les huit mondes ; issues écrites par programme ; contre-calcul.
- **Comparaisons multiples** : niveau de 0,001 par test (correction de Bonferroni sur 40 tests au plus pour un niveau de famille de 0,05). Aucune autre comparaison ne fonde l'admission.
- **Contrôles appariés** : chaque témoin qui doit mourir a une case où il doit tenir (D1, D2, D3, A1 dans F0 ; D4, A2 dans F1) ; D4 a son contrôle C1.

## Critères de lecture gelés

| Issue observée | Lecture |
|---|---|
| Un témoin « doit mourir » ne meurt pas dans sa case exigée (issue « tient », « muette », « hors gabarit » ou « sans objet ») | **épreuve morte** ; arrêt rapporté ; aucune autre issue n'est lue |
| Un témoin exigé de tenir meurt dans une case exigée | **épreuve non admise** ; arrêt ; cause cherchée dans le générateur, le noyau, le témoin ; aucun rejeu sur d'autres graines |
| Toutes les cases exigées rendent l'issue attendue et les contrôles de conformité passent | **épreuve admise, exploratoire** : la table d'admission est scellée ; ce n'est ni une porte ni un accord pour l'étape 1 |
| Un témoin non exécutable, une garde déclenchée | **non concluant** ; arrêt selon la liste |

Audit de symétrie (R4), déclenché de la même façon dans les deux sens : une fréquence mesurée hors de l'intervalle exact à 0,001 de sa valeur prédite, au-dessus ou au-dessous ; un témoin « doit mourir » tué avec une statistique plus extrême que tout ce que sa loi prédit ; une admission obtenue alors qu'un essai de garde a été sauté. Trop conforme vaut réserve comme trop peu.

## Liste d'arrêt

1. Épreuve morte. 2. Mort d'un témoin exigé de tenir. 3. Contrôle de conformité du générateur en échec. 4. Champ hors liste blanche, ou chaîne témoin de la vérité, dans ce qui est servi ou reçu. 5. Le module des témoins importe le noyau ou ouvre un fichier. 6. Réponse d'un témoin hors schéma. 7. Contre-calcul différent à l'octet. 8. Contenu de la famille tenue à l'écart ou du monde retiré parvenu au concepteur, au développeur ou au contre-lecteur. 9. Exécution avant scellement, ou seconde exécution après lecture d'une issue. 10. Refus d'outil ou de classifieur.

Action, dans tous les cas : arrêt, ligne au journal et à `registres/arrets.md`, aucun repli. Chaque garde est éprouvée d'abord sur un cas sain et sur un artefact (conception, § 7 ; R5). Tout ce qui est produit avant l'arrêt est inventorié et versé, scellé (règle « récupérer ce qui est récupérable »).

## Contre-lecture

En attente. À faire par un sous-agent neuf d'un autre modèle (Opus 5.5), à qui sont donnés explicitement : ce brouillon, la conception, le fichier de calculs et sa sortie, l'extrait, le gabarit ; et à qui ne sont donnés ni la famille tenue à l'écart, ni l'annexe réservée de la note d'origine. Son rapport, l'empreinte du brouillon relu et le traitement de chaque remarque s'écrivent ici avant le scellement ; puis vérification des corrections par le même contre-lecteur.

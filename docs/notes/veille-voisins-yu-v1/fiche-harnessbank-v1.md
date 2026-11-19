# Fiche de lecture — Luo et al. (2026), « HarnessBank: Semantic Gene-Bank Search with Gated Verification for Agent-Harness Self-Evolution » — v1

## En-tête

- **Qui écrit** : lecteur neuf lancé par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) sur le mot de Lazar « go lecture voisins » (GO-2026-11-19-10) ; modèle Fable 5.2 (`claude-fable-5-2`). Il n'a écrit ni la décision N-073, ni ses compléments, ni la note de lecture de Yu et al.
- **Identifiant** : arXiv 2607.13683, pris dans la bibliographie de Yu et al. (p. 12 du PDF `a8299ba5…`), vérifié par l'interface publique d'arXiv le 19 novembre 2026 (titre et cinq auteurs concordants : Luo, Xue, Wang, Hu, Deng).
- **Version lue** : version 2, datée du 30 juillet 2026 sur la page 1. Le premier dépôt, 15 juillet 2026, vient de la réponse de l'interface d'arXiv, hors pièce empreintée. Xia et al. (p. 13 de leur PDF `26f8b541…`) citent le même identifiant sous un autre titre, « Self-evolving agent harnesses via gated semantic quality-diversity » ; ce titre n'a pas été vérifié sur la version 1, qui n'a pas été lue.
- **Fichier** : `docs/sources/arxiv-2607.13683-v1/arxiv-2607.13683v2.pdf`, empreinte `360efedc16753f6bfe062cd58b1e2f7e9984bbdd36a8cc79ed363af686aeaeb2`, 9 pages.
- **Pages lues** : 1 à 7, en entier (tout le corps du papier : résumé, travaux voisins, méthode, expériences, ablation, conclusion), par `pdftotext`, page par page, en mise en page et dans l'ordre de lecture des colonnes. Pages 8 et 9 : bibliographie, parcourue. Le papier n'a ni annexe ni section de limites dans cette version.
- **Vocabulaire de cette fiche** : la « banque » est la « Harness Gene Bank » des auteurs ; l'« agent d'évolution » (« evolver agent ») est le modèle qui diagnostique et écrit les harnais candidats ; l'« agent de tâche » est le modèle figé qui exécute ; le « crible » est le « Gated Harness Screening » ; le « taux de réussite au premier essai » est la moyenne sur trois essais par tâche (p. 5).
- Aucune dépense, aucun appel à un modèle. Réseau : arxiv.org et export.arxiv.org seulement. Aucun refus d'outil.

## Les neuf réponses

**Q1. Ce qui est gardé, et qui l'écrit.**
Une **banque de harnais**, non un journal de l'amélioration. C'est une table à deux coordonnées : **où** la modification agit (consigne, connaissance injectée, exécution, configuration ; équation 6, p. 3) et **pourquoi** elle est introduite (une défaillance diagnostiquée, prise dans une liste qui grandit ; p. 3). Chaque case garde **un seul harnais**, le meilleur de sa case : « Harnesses addressing the same hypothesized mechanism compete within one cell and only the best one is preserved » (p. 4). S'y ajoute, pour le harnais parent du tour, un diagnostic complet : scores, trajectoires et métadonnées d'évaluation de chaque essai (équation 8, p. 4). Qui écrit : l'agent d'évolution produit les harnais candidats et leur étiquette — « why is an LLM-assigned hypothesis, not ground truth » (p. 6) ; la coordonnée « où » « is determined from the modified component » (p. 3) ; l'entrée dans la banque est décidée **par un programme** : un « deterministic evaluator » qui gère l'échantillonnage, la notation, le relevé d'activation et les tests (p. 3), puis une règle de concurrence par case (équation 9, p. 4). La phrase de Yu et al. (p. 16) sur ce papier est juste.

**Q2. Transmis à travers un changement, ou tenu pendant une course ?**
Tenu pendant une course : « At initialization, the gene bank is blank » (p. 3). Sur un autre modèle, la boucle repart de rien : « Cold-started on other models the loop evolves their own credited harnesses » (p. 6). Ce qui traverse un changement de modèle est un **correctif fini**, greffé et évalué (tableau 2, p. 7), pas la banque. Aucun changement de banc n'est traversé : chaque banc a sa course, et son test est tiré du même banc (p. 5).

**Q3. Héritage séparé de la tenue ?**
Non. Aucun bras ne part d'une banque héritée d'une autre course, d'un autre banc ou d'un autre modèle. Non trouvé dans les pages lues (1 à 7).
Une donnée voisine, sur le produit et non sur la mémoire : un correctif greffé sur un modèle dont la défaillance dominante est autre n'aide presque pas (+0,2 et +1,2 point entre les deux modèles Qwen sur AppWorld ; −1,5 sur Gemini pour Omni-MATH ; p. 6-7), et aide quand la défaillance est partagée (+11,0 greffé contre +11,7 natif ; p. 7). Les auteurs en concluent : « a credited harness is a correction fitted to the model, not a universally good setting » (p. 7).

**Q4. La mémoire est-elle ablatée ?**
La banque, non. L'ablation (tableau 3, p. 7, banc de terminal) porte sur le **crible** : sans le seuil de signification apparié, le score de test ne change pas (±0,0), deux « faux élites » entrent dans la banque et la boucle ne s'arrête qu'au plafond de 20 tours ; sans confirmation ni seuil, −1,6 point et trois faux élites. Pour la banque elle-même, le papier donne « Two signs the archive earns its keep » (p. 7) — le harnais retenu empile des mécanismes venus de plus d'une case, et les modifications acceptées touchent les quatre leviers — qui sont des constats, non un bras sans banque. Courses indépendantes : non dit ; le résultat par banc est « a single comparison (the train-selected winner scored once on held-out tasks) » (p. 6). Test : différence appariée par tâche entre harnais évolué et harnais de départ, statistique z ≥ 1,96 (p. 5), sur les tâches de test (valeurs p de moins de 10⁻⁴ à 0,033 ; p. 5).

**Q5. Prédictions écrites avant l'essai et confrontées au résultat ?**
Sous une forme étroite. Chaque candidat déclare d'avance une **spécification d'activation** et émet un signal déterministe quand son mécanisme se déclenche ; un candidat jamais déclenché est écarté comme inerte (p. 5). Un correctif a aussi une tâche visée : le crible en a rejeté un dont « its own target task » restait à 0 sur 24 (p. 6). Mais aucune liste de tâches à réparer n'est confrontée aux issues par tâche, et il n'y a ni taux de justesse des diagnostics, ni calibration, dans les pages lues ; un seul diagnostic faux est rapporté (p. 6). Rôle dans la sélection : l'activation est une des portes du crible (équations 11 et 15, p. 5) ; le diagnostic, lui, « only steers which candidates to try while credit comes solely from the gate » (p. 6).

**Q6. Les modifications rejetées ou échouées sont-elles gardées ?**
Pas dans ce que lit l'agent d'évolution, tel que le papier le décrit. La banque « admits only verified candidates » (p. 3) et ne garde qu'un harnais par case (p. 4) : un candidat rejeté par le crible ou battu dans sa case n'y reste pas. L'agent d'évolution travaille « Based on the diagnosis L(Ht ; Dtr) and the whole HGB » (p. 4), soit le diagnostic du parent et la banque. Aucun registre des essais rejetés n'est décrit dans les pages lues. La figure 3 (p. 6) montre bien tous les harnais produits, mais c'est un compte rendu, pas une mémoire servie à la boucle.

**Q7. Quel modèle conçoit, quel modèle exécute ?**
Agent d'évolution : Claude Opus 4.8. Agent de tâche figé : Qwen3.6-27B par défaut (p. 5) ; pour l'étude entre modèles, un modèle Qwen dit « 397B » et Gemini 3 Flash (p. 6-7). Pour les deux méthodes comparées, le texte dit : « same frozen Qwen3.6-27B as task agent and proposer » (p. 5) : à la lettre, leur proposeur serait Qwen3.6-27B, alors que l'agent d'évolution de la méthode est Claude Opus 4.8 ; le modèle qui conçoit ne serait alors pas le même d'une méthode à l'autre. Le papier ne commente pas cette différence.

**Q8. Le coût est-il apparié ou rapporté ?**
Rapporté en nombre d'exécutions de tâches, à peu près apparié : « comparable budgets (780–2,310 rollouts each, within 2.1× on any domain), with GEPA outspending us on two domains and DGM on one » (p. 5 ; figure 3, p. 6). Les jetons et les dollars de l'agent d'évolution ne sont pas donnés (cherché : « token », « $ », « dollar » — la seule occurrence de « token » concerne le budget de raisonnement de l'agent de tâche, p. 6).

**Q9. Sur quoi porte le résultat ; causalité affirmée et soutenue ?**
Sur le score de sept bancs : gain de test de +9,2 à +15,4 points sur six bancs, et +5,1 sur le septième, que les auteurs disent préliminaire (26 tâches de test, z = 0,78 ; tableau 1, p. 6 ; p. 5). Affirmation causale du résumé : « Cross-model experiments further verify that the improvements come from the model-specific self-evolving process, instead of a universally optimal harness » (p. 1). Le plan soutient le gain du harnais retenu sur le harnais de départ (test apparié par tâche, une comparaison par banc) et l'apport du crible sur un banc ; il ne mesure pas l'apport de la banque, faute de bras sans elle.

## Citations exactes

1. « At initialization, the gene bank is blank and A0(c) = ∅ for any c. » (p. 3)
2. « Harnesses addressing the same hypothesized mechanism compete within one cell and only the best one is preserved, whereas harnesses targeting different pathologies remain available for recombination. » (p. 4)
3. « why is an LLM-assigned hypothesis, not ground truth » (p. 6)

## Ce que ce papier occupe par rapport à notre question de l'héritage séparé de la tenue

- Il occupe l'**archive de candidats rangée par composant modifié et défaillance diagnostiquée**, avec entrée sous test apparié — une archive de produits, tenue dans une course, née vide (p. 3-5).
- Il ne garde pas les essais rejetés, ne transmet pas la banque, ne l'ablate pas : il ne sépare ni la tenue de l'absence d'archive, ni l'héritage de la tenue.
- Sa donnée la plus proche de notre question porte sur le produit : un correctif hérité d'un autre modèle n'aide que si la défaillance est partagée (tableau 2, p. 7) — à garder en tête comme mise en garde, non comme résultat sur une mémoire.

## Réserves

1. Le texte compte tantôt sept bancs, tantôt six (« All six test gains are credited », p. 5 ; « four of six domains », p. 6) : le septième, SWE-bench, est traité à part.
2. Le tableau 3 (p. 7) ne dit pas sur combien de courses ses lignes reposent ; la colonne des tours affiche « 10.0 ».
3. Le code n'est pas publié à la date de la version lue (p. 1).
4. Version 2 d'arXiv lue ; la version 1 n'a pas été comparée.

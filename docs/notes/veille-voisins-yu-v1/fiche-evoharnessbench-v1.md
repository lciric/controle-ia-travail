# Fiche de lecture ciblée — Ke et al. (2026), « EvoHarnessBench: Can Your Agents Keep Pace with an Evolving Harness? » — v1

## En-tête

- **Qui écrit** : lecteur neuf du groupe C, lancé par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) sur le mot de Lazar « go lecture voisins » (GO-2026-11-19-10) ; modèle Fable 5.2 (`claude-fable-5-2`). Il n'a écrit ni la décision N-073, ni ses compléments, ni la note de lecture de Yu et al.
- **Identifiant** : arXiv 2609.04280, pris dans la bibliographie de Yu et al. (p. 11 du PDF `a8299ba5b16577dd328d602e32f35b914b9393ffb38148d2410f358d4d90ff3d`), vérifié par l'interface publique d'arXiv le 19 novembre 2026 : titre concordant, douze auteurs, les quatre premiers (Ke, Patil, Shi, Li) concordent.
- **Version lue** : version 3, datée du 26 septembre 2026 sur la page 1. Le premier dépôt, 3 septembre 2026, vient de la réponse de l'interface d'arXiv, hors pièce empreintée.
- **Fichier** : `docs/sources/arxiv-2609.04280-v1/arxiv-2609.04280v3.pdf`, empreinte `7e19f3e415711780d6b7d521e5c97bc9081bc360cce94b071be6aa02acb5e724`, 35 pages.
- **Pages lues** (lecture ciblée, `pdftotext -layout`) : 1 à 3 (résumé, introduction) ; 4, section 3.1 seulement ; 5, début de la section 3.4 seulement ; 6 à 12 (protocole, résultats par axe, synthèse, conclusion) ; 22 et 23 (annexe D, mesures) ; 26 à 29 (annexes G à I.1 : systèmes, mémoires comparées) ; le bas de 30 et la page 31 (fin de I.2, méthodes d'apprentissage de compétences, tableau J.2). **Non lues** : sections 3.2 et 3.3 (construction du banc, p. 4-5), 13 à 21, 24 et 25, le haut de 30, 32 à 35. Aucun chiffre n'est tiré d'une figure, sauf ceux que le texte répète.
- **Vocabulaire de cette fiche** : ici, le « harnais » est ce qui est **fourni de l'extérieur** à l'agent — outils, compétences, agents spécialistes — et il grossit par étapes ; l'« état persistant » est ce que le système apprend et garde pour s'en servir (souvenirs, compétences apprises, consignes, règles de routage). Le « déploiement » est le régime sans état persistant ; l'« adaptation » est le régime avec. Le « transfert vers l'avant » mesure l'effet de l'adaptation d'une étape sur les tâches nouvelles de cette étape ; le « transfert vers l'arrière » mesure ce que deviennent les tâches anciennes (« FWT », « BWT », p. 22-23). Les deux sources de tâches sont nommées EOG et ALE par les auteurs (EnterpriseOps-Gym et Agents' Last Exam, p. 4).
- Aucune dépense, aucun appel à un modèle. Réseau : arxiv.org et export.arxiv.org seulement. Aucun refus d'outil.

## Les neuf réponses

**Q1. Ce qui est gardé, et qui l'écrit.**
Un état persistant, selon la méthode d'adaptation branchée (p. 6) : des **mémoires** — la mémoire brute, qui garde pour chaque épisode la description de la tâche, les appels d'outils et leurs arguments, les résultats et le retour du vérificateur, sans tri ni résumé (p. 26) ; ReasoningBank, qui remplace la trajectoire par des éléments à titre, description et raisonnement de procédure (p. 26) ; MemToolAgent, qui garde une réflexion par épisode (p. 27) ; d'autres pour les systèmes à plusieurs agents (p. 27) — ; des **consignes** révisées (GEPA) ; du **code** de harnais optimisé (Meta-Harness) (p. 6). La mémoire brute est écrite par le programme ; les formes résumées, par un modèle. C'est une mémoire de l'**exécution des tâches**, sauf pour Meta-Harness.

**Q2. Transmis à travers un changement, ou tenu pendant une course ?**
Les deux à la fois, sans les distinguer. Le changement est la croissance du harnais fourni, d'une étape à la suivante, le modèle restant fixe (p. 2-4). En régime d'adaptation, l'état est porté d'étape en étape et mis à jour, avant chaque évaluation, sur les tâches d'adaptation cumulées depuis la première étape (p. 6). L'évaluation se fait sur une part tenue à l'écart (p. 4).

**Q3. Héritage séparé de la tenue ?**
En partie, et dans un seul sens. Les bras exacts :
- **déploiement** : aucun état ; un système neuf à chaque étape (p. 6) ;
- **adaptation** : état hérité des étapes passées et mis à jour à l'étape courante (p. 6) ;
- **le transfert vers l'avant** compare, sur les tâches nouvelles de l'étape, le score après l'adaptation de l'étape au score avant elle, c'est-à-dire avec l'état hérité de l'étape précédente seul (p. 23) : « hérité puis mis à jour » contre « hérité seul » ;
- **deux contrôles** changent ce que l'adaptation voit du harnais, non l'état : n'exposer que les outils utiles à la tâche, ou exposer d'emblée le harnais final à toutes les étapes (tableaux 3, 5 et 7 ; p. 8, 9, 11).
Aucun bras, dans les pages lues, ne fait naître l'état vide à l'étape courante pour le tenir sur cette seule étape, face à l'état hérité. La mise à jour est mesurée au-delà de l'héritage ; l'héritage n'est pas mesuré au-delà de la mise à jour.

**Q4. La mémoire est-elle ablatée ?**
Oui, pour un agent seul, sur l'axe des outils et la source EOG, 454 tâches (tableau 2, p. 7 ; tableau I.1, p. 28) : sans mémoire 30,2 ± 0,8 ; mémoire brute 33,0 ± 0,9 ; trajectoires réussies seules 34,4 ± 1,7 ; trajectoires échouées seules 34,4 ± 0,7 ; ReasoningBank 36,9 ± 1,3 ; ReasoningBank avec les schémas d'outils 30,3 ± 1,0 ; MemToolAgent 38,6 ± 1,0. Le nombre de courses derrière les « ± » n'est pas trouvé dans les pages lues (cherché par mot dans tout le texte). Aucun test.

**Q5. Des prédictions écrites avant l'essai ?**
Non trouvé dans les pages lues.

**Q6. Les essais rejetés ou échoués sont-ils gardés ?**
Oui dans la mémoire brute, retour du vérificateur compris (p. 26). Garder les seules réussites ou les seuls échecs donne le même taux, 34,4 (p. 28). Pour un des systèmes à plusieurs agents, retirer les trajectoires incorrectes ramène au niveau sans mémoire (p. 30).

**Q7. Quel modèle conçoit, quel modèle exécute ?**
GPT-5 pour tous les systèmes des tableaux principaux (p. 7, 8, 10) ; Claude Code, avec un autre modèle, est rapporté à part (p. 6). Il n'y a pas de concepteur distinct : le harnais fourni est construit par les auteurs, et l'adaptation est faite par la méthode branchée, avec le même modèle (p. 6).

**Q8. Coût.**
Rapporté, non apparié : une durée en heures et des jetons en millions par condition (tableaux 2, 4, 6 ; p. 7, 8, 10). Sur l'axe des outils et la source EOG : 75,8 millions de jetons sans mémoire ; 124,5 avec la mémoire brute ; 150,8 avec ReasoningBank ; 148,0 avec MemToolAgent ; 99,0 avec Meta-Harness (tableau 2, p. 7). Certaines cases manquent, faute d'avoir tenu dans un budget comparable (légende du tableau 6, p. 10).

**Q9. Objet du résultat, causalité.**
Des taux de réussite sur un banc, et deux mesures de transfert. Le propos est descriptif. Trois constats : le harnais qui grossit fait perdre des tâches auparavant réussies, sans aucun état (jusqu'à −34,7 % sur l'axe des agents, p. 10, tableau 8 p. 12 ; sur l'unité, voir la réserve 2) ; les gains de l'adaptation varient selon l'axe et la source (p. 7-10) ; sur les tâches nouvelles, l'adaptation d'une étape peut nuire (transfert vers l'avant de −28,5 % et −11,1 % sur l'axe des outils, source ALE, p. 7).

## Ce que ce papier dit sur la forme de la mémoire (pour l'axe « traces brutes ou résumé »)

Il compare les deux, pour une mémoire de l'**exécutant** tenue au fil d'un harnais qui grossit, et le sens dépend du cas :
- agent seul, axe des outils, source EOG : les formes résumées font mieux que la mémoire brute (38,6 et 36,9 contre 33,0 ; p. 8, p. 28) ;
- agent seul, axe des compétences, source EOG : la mémoire brute fait autant ou mieux (21,6 ± 1,0 contre 20,9 ± 2,0 et 19,6 ± 0,6 ; tableau 4, p. 8) ;
- systèmes à plusieurs agents : les auteurs concluent que les trajectoires concrètes réussies sont le choix le plus sûr (p. 30).

## Trois citations

1. « In deployment evaluation, inner adaptation is disabled: each harness version is evaluated independently, with no experience carried across stages. » (p. 3)
2. « structured memories outperform raw replay (MemToolAgent: 38.6%; ReasoningBank: 36.9%; raw memory: 33.0%) » (p. 8)
3. « concrete successful trajectories are consistently safer and more useful than abstracted, failed, or uniformly shared memories across sub-agents » (p. 30)

## Ce que ce papier occupe par rapport à notre question de l'héritage séparé de la tenue

- Il occupe « **état persistant hérité et mis à jour** » contre « **aucun état** », à travers un changement qui est la croissance du harnais fourni, pour le score d'un banc et pour une mémoire de l'exécution.
- Son transfert vers l'avant mesure ce que la mise à jour d'une étape ajoute à l'état hérité — et trouve qu'elle peut retrancher ; le sens inverse, ce que l'héritage ajoute à une mémoire née vide et tenue, n'est pas dans les pages lues.
- Pour nous : un précédent pour le vocabulaire (état hérité, état mis à jour, mesures de transfert) et un troisième point sur la forme de l'archive, de sens variable.

## Réserves

1. Lecture ciblée : la construction du banc (sections 3.2 et 3.3) et douze pages d'annexes ne sont pas lues.
2. L'unité des mesures de transfert n'est pas sûre : le texte principal les dit relatives (p. 5-6) et l'axe des figures porte une variation en pourcentage du niveau (p. 7), alors que les formules de l'annexe D sont des différences simples de taux (p. 23). Ne pas les reprendre comme des points sans relire.
3. Un seul lecteur ; aucune contre-lecture à ce jour.

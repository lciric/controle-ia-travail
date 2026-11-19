# Fiche de lecture ciblée — Yu et al. (2026a), « Harmony Harness: Multi-Objective Self-Evolution of Agent Harnesses » — v1

## En-tête

- **Qui écrit** : lecteur neuf du groupe C, lancé par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) sur le mot de Lazar « go lecture voisins » (GO-2026-11-19-10) ; modèle Fable 5.2 (`claude-fable-5-2`). Il n'a écrit ni la décision N-073, ni ses compléments, ni la note de lecture de Yu et al.
- **À ne pas confondre** : ce papier est de Weichen Yu et al. ; le papier sur la mémoire d'auto-amélioration (arXiv 2611.18856), que cette fiche appelle « Yu et al. (mémoire) », a d'autres auteurs.
- **Identifiant** : arXiv 2610.15150, pris dans la bibliographie de Yu et al. (mémoire) (p. 13 du PDF `a8299ba5b16577dd328d602e32f35b914b9393ffb38148d2410f358d4d90ff3d`), vérifié par l'interface publique d'arXiv le 19 novembre 2026 : titre concordant, huit auteurs, les quatre premiers (Yu, Miculicich, Mishra, Chen) concordent.
- **Version lue** : version 1, datée du 10 octobre 2026 sur la page 1 ; seule version déposée d'après l'interface d'arXiv (hors pièce empreintée).
- **Fichier** : `docs/sources/arxiv-2610.15150-v1/arxiv-2610.15150v1.pdf`, empreinte `3fa04df2ad4b01c3cd616af7e8cec37fda9e04a2df09e3816133985374724e6c`, 41 pages.
- **Pages lues** (lecture ciblée, `pdftotext -layout`) : 1 à 7 (résumé, introduction, travaux voisins, formulation, méthode) ; le texte des pages 8 à 11 (expériences, conclusion ; la figure 2 de la page 8 n'est pas lue) ; 18 à 20 (annexes C, D et début de E : réglages, diagnostic) ; 22 et 23 (ordonnancement, validation, réparation, retour arrière) ; 27 à 29 (ablations, travaux voisins, discussion et limites, tableaux 9 et 10) ; 37 et début de 38 (porte contre le surajustement). **Non lues** : 12 à 17, 21, 24 à 26, 30 à 36, 39 à 41.
- **Vocabulaire de cette fiche** : le « proposeur » est le modèle qui modifie le harnais ; un « enfant » est un harnais candidat tiré d'un parent ; la « portée générale » et la « portée propre au banc » sont les deux rangements d'un composant ; la « réussite sûre » est la part des tâches à la fois fonctionnelles et sûres en un essai (« secure-pass@1 », p. 8).
- Aucune dépense, aucun appel à un modèle. Réseau : arxiv.org et export.arxiv.org seulement. Aucun refus d'outil.

## Les neuf réponses

**Q1. Ce qui est gardé, et qui l'écrit.**
Pas de mémoire de l'amélioration servie au proposeur. La recherche garde une population bornée : un harnais titulaire par sous-problème, chaque sous-problème étant une pondération des deux objectifs, fonctionnalité et sécurité (p. 5-6). Le proposeur reçoit un seul harnais parent, la pondération et les retours d'exécution de ce parent (p. 6-7) ; la séance de diagnostic est isolée des arbres des autres courses et des notes propres du harnais (p. 19), et voit les diagnostics déjà rendus par les sous-problèmes voisins dans la même génération, pour ne pas les répéter (p. 20). Les auteurs présentent la population bornée comme une façon de ne pas porter une archive qui grossit dans le contexte du proposeur (p. 2, p. 6). Des journaux sont écrits par le programme pour compter (entrée et sortie de chaque diagnostic, une ligne par appel, p. 20) ; ils ne sont pas dits relus par le proposeur. Les « compétences » sont un composant du harnais de l'exécutant (p. 4), non un enregistrement de l'amélioration.

**Q2. Transmis à travers un changement, ou tenu pendant une course ?**
Ce qui traverse un changement est le **harnais**, et seulement sa portée générale : évolué sur un banc, il est mesuré sans autre évolution sur l'autre banc (p. 10) et sur un troisième, de format différent (p. 10-11). Aucun enregistrement d'expérience n'est transmis.

**Q3. Héritage séparé de la tenue ?**
Non. Aucune optimisation ne reprend sur la cible ; il n'y a ni mémoire héritée ni mémoire tenue à comparer. Non trouvé dans les pages lues.

**Q4. La mémoire est-elle ablatée ?**
Sans objet : il n'y a pas de mémoire de l'amélioration. Les ablations portent sur ce qui est évolué (bloc entier, outils seuls, compétences et logique seules, les deux, puis l'orchestration dynamique ; tableau 7, p. 28), sur l'orchestration (tableau 8, p. 28) et sur la règle d'acceptation (tableau 2, p. 9). Chaque taux est la moyenne de trois courses indépendantes (p. 18) ; les pages lues ne disent pas s'il s'agit de trois évolutions ou de trois évaluations d'une évolution. 30 tâches par part sur SecRepoBench, 28 sur BaxBench (p. 8). Aucun intervalle ni test sur les comparaisons principales.

**Q5. Des prédictions écrites avant l'essai ?**
Le proposeur écrit, avant de modifier, un diagnostic et une hypothèse d'amélioration (p. 7) ; le diagnostic est un objet à champs fixes — angle, énoncé du problème, preuve citée, un à trois exemples d'échec (p. 20). Ce qui est vérifié est la **preuve citée** : le chemin doit exister et la citation s'y trouver mot pour mot (p. 20). Aucune prédiction des tâches réparées, aucune confrontation après coup ; le diagnostic n'entre pas dans la sélection (p. 20). À part : un juge par modèle donne à chaque enfant admis un **risque de surajustement** entre 0 et 1, et l'enfant est rejeté au-dessus d'un seuil ; ce juge est étalonné sur des surajustements plantés, par paires, avec un test de McNemar (p. 37-38). C'est l'étalonnage d'un juge sur des cas plantés, non la justesse de prédictions du proposeur.

**Q6. Les essais rejetés ou échoués sont-ils gardés ?**
Un enfant qui échoue deux fois à la validation est rejeté et le dépôt revient au dernier parent valide (p. 23). Tous les enfants évalués restent candidats au choix final du harnais déployé, même ceux qu'un autre a remplacés (p. 4). Rien de cela n'est dit servi au proposeur.

**Q7. Quel modèle conçoit, quel modèle exécute ?**
Le même, gemini-3.6-flash, sauf mention contraire (p. 8).

**Q8. Coût.**
Les stratégies du tableau 2 partagent harnais de départ, part d'évolution, budget de jetons et réglages (p. 9). Les jetons dépensés par tâche à la résolution sont donnés pour l'ablation de l'orchestration : 31 902, 58 230 et 63 064 (tableau 8, p. 28). Le coût de l'évolution, en jetons ou en dollars, n'est pas trouvé dans les pages lues ; les limites disent seulement que l'évaluation réelle domine la durée (p. 29). Les deux méthodes d'autres auteurs tournent depuis le code publié par leurs auteurs (p. 18).

**Q9. Objet du résultat, causalité.**
Le score de bancs de code sûr. Les auteurs attribuent le transfert entre bancs à la séparation des deux portées (p. 10). Le plan : une ablation de ce qui est évolué (tableau 7, p. 28), 30 tâches, trois courses, sans intervalle. Les limites disent que, sur SecRepoBench, le front entre les deux objectifs est étroit (p. 28).

## Trois citations

1. « The proposer never receives more than one full parent repository, which keeps its context bounded. » (p. 6)
2. « Each method is evolved on the evolve split only and then evaluated, without further evolution, on both held-out splits. » (p. 8)
3. « only the general scope is loaded on the target benchmark, so benchmark-specific fixes do not carry over. » (p. 10)

## Ce que ce papier occupe par rapport à notre question de l'héritage séparé de la tenue

- Il occupe le **transfert d'un harnais** dont on ne charge que la part générale, vers un autre banc, sans reprise de l'optimisation, pour le score.
- Il fait le choix inverse de la mémoire : une population bornée, un seul parent servi au proposeur, pas d'archive ; ce choix n'est pas comparé à une archive.
- Il ne contient donc ni héritage ni tenue d'une mémoire de l'amélioration ; sur la prédiction, il vérifie les preuves citées par un diagnostic, non ses effets.

## Réserves

1. Lecture ciblée : 20 pages sur 41 ne sont pas lues ; l'annexe J (diversité de la population) et la fin de l'annexe K ne le sont pas.
2. Un seul lecteur ; aucune contre-lecture à ce jour.

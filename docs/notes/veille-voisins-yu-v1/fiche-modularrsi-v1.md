# Fiche de lecture ciblée — Wu et al. (2026), « ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement » — v1

## En-tête

- **Qui écrit** : lecteur neuf du groupe C, lancé par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) sur le mot de Lazar « go lecture voisins » (GO-2026-11-19-10) ; modèle Fable 5.2 (`claude-fable-5-2`). Il n'a écrit ni la décision N-073, ni ses compléments, ni la note de lecture de Yu et al.
- **Identifiant** : arXiv 2609.14857, pris dans la bibliographie de Yu et al. (p. 13 du PDF `a8299ba5b16577dd328d602e32f35b914b9393ffb38148d2410f358d4d90ff3d`), vérifié par l'interface publique d'arXiv le 19 novembre 2026 : titre concordant, quinze auteurs, les quatre premiers (Wu, Ren, Li, Li) concordent.
- **Version lue** : version 2, datée du 9 octobre 2026 sur la page 1. Le premier dépôt, 14 septembre 2026, vient de la réponse de l'interface d'arXiv, hors pièce empreintée.
- **Fichier** : `docs/sources/arxiv-2609.14857-v1/arxiv-2609.14857v2.pdf`, empreinte `4f5592c3605821072842e7408e20d3b2c662cde5e1914f3be80239d186d8244f`, 28 pages.
- **Pages lues** (lecture ciblée, `pdftotext -layout`) : 1 à 10 (résumé, méthode, résultats, conclusion) ; 13 (tableau comparatif) ; 15 à 24 (annexes C à J : validation, autres modèles, réglages des comparaisons, intervalles, qualité des données, format des constats, consignes) ; 27 et 28 (fin des études de cas, courbe d'évolution). **Non lues** : 11 et 12 (bibliographie), 14 (extraits d'interfaces), 25 et 26 (études de cas), sauf leurs titres. Le papier n'a pas de section de limites (cherché par mot dans tout le texte).
- **Vocabulaire de cette fiche** : le « concepteur » est l'agent qui analyse les traces et modifie le harnais (« Code-Modify Agent ») ; une « lignée » est l'évolution d'un seul des cinq modules du harnais ; une « époque » est un passage sur les tâches d'évolution.
- Aucune dépense, aucun appel à un modèle. Réseau : arxiv.org et export.arxiv.org seulement. Aucun refus d'outil.

## Les neuf réponses

**Q1. Ce qui est gardé, et qui l'écrit.**
Trois choses, pendant une course d'évolution.
- Une **mémoire des trajectoires** : les trajectoires passées et leurs récompenses, par tâche, d'une époque à l'autre (p. 4) ; écrite par la boucle. Elle sert à apparier un échec d'aujourd'hui à une réussite ancienne de la même tâche (p. 4) ; cela arrive pour 150 groupes de tâches, 8,33 % (tableau 12, p. 24).
- Un **historique d'évolution par fonction** : les modifications de code passées et ce que chaque révision a apporté (p. 5) ; le concepteur s'en sert pour ne pas défaire ni répéter (p. 5). Qui l'écrit n'est pas dit dans les pages lues.
- Des **constats structurés**, écrits par le concepteur : tâche, angle d'analyse, module en cause ou non, divergence observée, jugement contrefactuel (la modification changerait-elle l'issue ?), réparable maintenant ou non, modification suggérée (p. 19-21).

**Q2. Transmis à travers un changement, ou tenu pendant une course ?**
Tenu pendant une course. Ce qui traverse un changement est le **harnais figé** : la bibliothèque de fonctions est gelée après l'intégration et rien n'est modifié à l'évaluation (p. 5). Il est mesuré sur deux bancs que l'évolution n'a jamais vus (Terminal-Bench 2.0 et SWE-Bench Verified ; tableau 1, p. 7) et avec deux autres modèles exécutants (tableau 2, p. 7). Aucune optimisation ne reprend après le changement.

**Q3. Héritage séparé de la tenue ?**
Non. Il n'y a ni seconde course, ni bras à mémoire héritée, ni bras à mémoire vide tenue. Non trouvé dans les pages lues.

**Q4. La mémoire est-elle ablatée ?**
Non. Ni la mémoire des trajectoires ni l'historique par fonction n'ont de bras sans eux. Les trois ablations (tableau 5, p. 8) retirent l'analyse par contraste entre réussite et échec (52,43 → 50,56), la gestion de la bibliothèque de fonctions (→ 49,81) et les portes de validation (→ 48,31), sur Terminal-Bench 2.0. Le nombre de courses d'évolution par condition n'est pas dit dans les pages lues. L'incertitude donnée est celle de l'évaluation : chaque harnais figé est évalué trois fois, et un rééchantillonnage apparié des tâches (100 000 tirages) donne un intervalle à 95 % de l'écart à la base (p. 18) ; elle ne porte pas sur la variation entre courses d'évolution.

**Q5. Des prédictions écrites avant l'essai ?**
Un jugement contrefactuel est écrit **avant** la modification, par tâche : le champ `would_change_outcome` dit si la modification proposée changerait l'issue de la tâche (p. 19, p. 21). Il sert à décider s'il faut proposer une modification. Il n'est pas confronté à l'issue après la modification dans les pages lues : la revue des différences se fait sans voir les récompenses (p. 22), et les portes vérifient l'exécution, non l'effet (p. 5, p. 15). Aucun taux de justesse, aucune calibration.

**Q6. Les essais rejetés ou échoués sont-ils gardés ?**
Les trajectoires échouées, oui (p. 4). Les constats qui concluent qu'il ne faut rien changer sont enregistrés (exemple p. 20). Une modification qui échoue à une porte est défaite par les différences enregistrées (p. 5, p. 15), et la revue rend un verdict avec une classe de rejet et une raison (p. 22). Les pages lues ne disent pas si les modifications rejetées entrent dans l'historique par fonction.

**Q7. Quel modèle conçoit, quel modèle exécute ?**
Le même : l'agent en cours d'évolution sert de concepteur (p. 4). DeepSeek-V4-Flash-Preview pour l'évolution et l'évaluation (p. 6, p. 17). D'autres modèles en annexe (p. 15). Un modèle d'une autre maison, Opus 4.8, note les trajectoires pour une courbe annexe (p. 27-28).

**Q8. Coût.**
Apparié en **époques** : les méthodes comparées et les variantes à harnais entier évoluent seize époques, pour égaler cinq modules à trois époques plus une époque d'intégration ; trois essais par tâche ; même plafond de débit en jetons (p. 8, p. 17). Ni jetons consommés ni dollars ne sont rapportés.

**Q9. Objet du résultat, causalité.**
Le score de deux bancs. Les auteurs écrivent que le gain ne peut pas venir d'une exposition plus grande aux trajectoires ni de tours en plus, puisque données, modèle et budget sont partagés (p. 9). Le plan : mêmes 120 tâches d'évolution, mêmes époques ; contre la base sans évolution, +4,86 points pour la méthode, +1,87 pour Meta-Harness et +2,24 pour Agentic Harness Engineering, ces deux derniers intervalles touchant zéro (tableau 9, p. 18). L'écart entre la méthode et ces deux bases n'a pas d'intervalle propre.

## Trois citations

1. « A Trajectory Memory stores historical trajectories and rewards for each task across evolution epochs, providing additional evidence when current rollouts are insufficient. » (p. 4)
2. « For each function, we record previous code changes and the functionality introduced by each revision. » (p. 5)
3. « These runs also contain other updates, so the comparisons do not isolate the effect of a single change. » (p. 27)

## Ce que ce papier occupe par rapport à notre question de l'héritage séparé de la tenue

- Il occupe le **transfert d'un harnais figé** vers des bancs jamais vus et d'autres modèles, avec une évolution sur des tâches disjointes des bancs, pour le score.
- Il tient deux mémoires de l'amélioration pendant la course (trajectoires par tâche, historique par fonction) sans les ablater ni les transmettre à une seconde optimisation.
- Il écrit un jugement contrefactuel avant chaque modification, sans le confronter ensuite : pour la prédiction comme pour la séparation, les pages lues ne contiennent pas l'essai.

## Réserves

1. Lecture ciblée : les pages 14, 25 et 26 ne sont pas lues ; un détail sur l'historique par fonction peut s'y trouver.
2. Un seul lecteur ; aucune contre-lecture à ce jour.

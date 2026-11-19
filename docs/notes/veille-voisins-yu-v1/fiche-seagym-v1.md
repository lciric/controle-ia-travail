# Fiche de lecture ciblée — Zheng et al. (2026), « SEAGym: An Evaluation Environment for Self-Evolving LLM Agents » — v1

## En-tête

- **Qui écrit** : lecteur neuf du groupe C, lancé par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) sur le mot de Lazar « go lecture voisins » (GO-2026-11-19-10) ; modèle Fable 5.2 (`claude-fable-5-2`). Il n'a écrit ni la décision N-073, ni ses compléments, ni la note de lecture de Yu et al.
- **Identifiant** : arXiv 2606.17546, pris dans la bibliographie de Yu et al. (p. 14 du PDF `a8299ba5b16577dd328d602e32f35b914b9393ffb38148d2410f358d4d90ff3d`), vérifié par l'interface publique d'arXiv le 19 novembre 2026 : titre concordant, cinq auteurs (Zheng, Xue, Liang, Yang, Zhang), les quatre premiers concordent.
- **Version lue** : version 1, datée du 16 juin 2026 sur la page 1 ; seule version déposée d'après l'interface d'arXiv (hors pièce empreintée).
- **Fichier** : `docs/sources/arxiv-2606.17546-v1/arxiv-2606.17546v1.pdf`, empreinte `7ba0baa3766cc4f4545181ba542064b05a41b183bab4db6081c056bc296fc002`, 32 pages.
- **Pages lues** (lecture ciblée ; papier sur deux colonnes, lu par `pdftotext` en ordre de lecture, les tableaux 2 à 5 relus par `pdftotext -layout`) : 1 à 9 (résumé, méthode, expériences, conclusion, limites) ; 13 à 16 (annexes A et B : calendrier, réglages, budgets enregistrés ; début de C) ; 29 et les premières lignes de 30 (résultats entre modèles, définitions des mesures de rejeu). **Non lues** : 10 à 12 (bibliographie), 17 à 28 (études de cas, figures), 31 et 32. Aucun chiffre n'est tiré d'une courbe.
- **Vocabulaire de cette fiche** : un « état du harnais » est tout ce qui entoure le modèle et peut être mis à jour (consignes, mémoires, compétences, outils, intergiciel) ; un « instantané » est cet état figé à un point d'évaluation ; le « rejeu » est la réévaluation des tâches d'entraînement par chaque instantané ; « en domaine » et « hors domaine » traduisent les vues « ID » et « OOD ». Les trois méthodes évaluées sont Agentic Harness Engineering (Lin et al., qui modifie le harnais), Agentic Context Engineering (Zhang et al., qui tient un carnet de compétences) et la méthode d'optimisation par groupes d'essais sans entraînement, « Training-free GRPO » (Cai et al., qui tient une réserve d'expériences).
- Aucune dépense, aucun appel à un modèle. Réseau : arxiv.org et export.arxiv.org seulement. Aucun refus d'outil.

## Les neuf réponses

**Q1. Ce qui est gardé, et qui l'écrit.**
Le papier est un banc d'évaluation, non une méthode. Deux niveaux.
- **Par la méthode évaluée** : son propre état de harnais — carnet de compétences pour l'une, réserve d'expériences par famille de tâches pour l'autre, harnais modifié (consignes, intergiciel, mémoire, fichiers) pour la troisième (p. 14, p. 15-16). L'environnement ne prescrit pas la règle de mise à jour (p. 2, p. 5).
- **Par l'environnement, donc par un programme** : références de trajectoires, retours publics, résumés de mise à jour, différences de harnais quand elles existent, instantanés et mesures à chaque point d'évaluation (p. 6). Ces pièces servent au diagnostic hors ligne ; les diagnostics de rejeu ne sont pas rendus à l'agent (p. 29-30).

**Q2. Transmis à travers un changement, ou tenu pendant une course ?**
Tenu pendant une course : l'état persiste d'un lot à l'autre et d'une époque à l'autre, cinq époques sur 80 tâches (p. 4, p. 6, tableau 6 p. 15). Ce qui traverse un changement est l'**instantané figé** : mesuré sur des tâches du même domaine tenues à l'écart, sur des tâches d'un autre domaine (p. 4-6), et avec un autre modèle exécutant (p. 8). Aucune évolution ne reprend après le changement. Le mot « continuation » de l'annexe désigne la reprise d'une course interrompue (p. 14, p. 29), non une poursuite après changement.

**Q3. Héritage séparé de la tenue ?**
Non. La remise à zéro de l'état est un paramètre du calendrier que l'environnement sait exprimer (p. 2, p. 13), mais les expériences n'utilisent que l'état persistant (p. 4, tableau 6 p. 15). Aucun bras à mémoire héritée, aucun bras à mémoire vide tenue sur une cible. Non trouvé dans les pages lues.

**Q4. La mémoire est-elle ablatée ?**
Non. Les variations portent sur la méthode (trois), la taille du lot (10, 20, 40, 80), la diversité des sources et le modèle (p. 6-8). Une course par configuration d'après la liste des courses (p. 14) ; évaluation en un seul essai par tâche sur les vues de validation et finales (tableau 6, p. 15) ; 35 tâches de validation, 55 d'essai en domaine, 80 hors domaine (p. 6). Aucun intervalle, aucun test. Les auteurs écrivent qu'ils n'attribuent pas un succès à une entrée de mémoire ni à une modification prise seule (p. 15, p. 16).

**Q5. Des prédictions écrites avant l'essai ?**
Non trouvé dans les pages lues. La seule mention voisine concerne une des méthodes évaluées : ses manifestes de mise à jour disent quel schéma d'échec chaque modification vise et pourquoi ce composant est modifié (p. 16).

**Q6. Les essais rejetés ou échoués sont-ils gardés ?**
Les instantanés de chaque époque sont gardés, y compris ceux qui s'effondrent : après la quatrième époque, le rejeu tombe à 6 tâches sur 80, contre 34 au départ et 43 à la fin (p. 6-7). C'est un enregistrement de l'environnement pour le lecteur, non une mémoire rendue à l'agent.

**Q7. Quel modèle conçoit, quel modèle exécute ?**
Le même modèle pour l'exécution et la mise à jour quand la méthode en a une : DeepSeek-V4-Flash dans la comparaison principale (p. 6, tableau 7 p. 16) ; GLM-5.1 et GPT-5.4 pour l'essai entre modèles, un modèle par course (p. 16, p. 29).

**Q8. Coût.**
Rapporté, non apparié. Par méthode : jetons d'exécution par tâche et jetons de mise à jour par mise à jour — 1,46 million et 3,91 millions pour Agentic Harness Engineering ; 1,93 million et non disponible pour Agentic Context Engineering ; 2,33 millions et 1,60 million pour la troisième (tableau 2, p. 7). Par course : le total enregistré, par exemple 1 053,8 millions de jetons d'exécution et 78,1 millions de mise à jour pour la course principale (p. 14). Chaque méthode garde sa règle propre et son nombre d'exécutions (720 lignes contre 1 120, p. 14).

**Q9. Objet du résultat, causalité.**
Des taux de réussite sur des vues d'un banc. Le propos est descriptif : les auteurs disent ce que les vues laissent voir (gains de validation qui ne se transfèrent pas, instantanés utiles qui s'effondrent ensuite, transfert entre modèles asymétrique, p. 6-9) et classent parmi leurs limites le petit nombre de sources, de modèles et la courte durée (p. 9).

## Une remarque de ce lecteur (à relire avant tout usage)

Dans le balayage de la taille du lot, les quatre courses d'Agentic Harness Engineering partent de 37,1 ; 40,0 ; 37,1 ; 42,9 en validation (tableau 3, p. 7), sur les mêmes 35 tâches évaluées en un essai (p. 7, p. 15) : avant toute mise à jour, l'écart entre courses atteint deux tâches sur 35. Les gains en domaine de deux des trois méthodes (+3,6 points, tableau 2, p. 7) valent deux tâches sur 55.

## Trois citations

1. « The main experiments use persistent state, repeated train batches, train-batch updates, and epoch-end frozen update-validation assessment. » (p. 4)
2. « All replay diagnostics are computed offline by the benchmark and are not fed back to the evolving agent. » (p. 29-30)
3. « an initial-versus-final table would miss a damaging intermediate harness regression » (p. 7)

## Ce que ce papier occupe par rapport à notre question de l'héritage séparé de la tenue

- Il occupe un **protocole de mesure** : validation figée, transfert en domaine et hors domaine, rejeu des tâches d'entraînement, coût en jetons, le tout par instantané ; c'est ce pour quoi Yu et al. le citent (Yu, p. 16).
- Son calendrier sait dire « état remis à zéro » ou « état persistant », mais les essais ne comparent pas les deux ; il n'y a pas d'optimisation reprise après un changement.
- Pour nous : un précédent pour mesurer la rétention et le coût au fil d'une course, non pour la séparation ; une course par configuration, un essai par tâche.

## Réserves

1. Lecture ciblée : les études de cas (p. 17-28) ne sont pas lues.
2. Les sigles des trois méthodes sont développés ici d'après ce que le papier en dit (p. 14) et d'après les titres de leurs papiers dans la bibliographie de Yu et al. ; le développé de la troisième méthode est repris tel que le papier Meta² l'écrit (arXiv 2611.05139, p. 6).
3. Un seul lecteur ; aucune contre-lecture à ce jour.

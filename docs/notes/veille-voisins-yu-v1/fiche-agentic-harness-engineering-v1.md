# Fiche de lecture — Lin et al. (2026), « Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses » — v1

## En-tête

- **Qui écrit** : lecteur neuf lancé par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) sur le mot de Lazar « go lecture voisins » (GO-2026-11-19-10) ; modèle Fable 5.2 (`claude-fable-5-2`). Il n'a écrit ni la décision N-073, ni ses compléments, ni la note de lecture de Yu et al.
- **Identifiant** : arXiv 2604.25850, pris dans la bibliographie de Yu et al. (p. 12 du PDF `a8299ba5…`), vérifié par l'interface publique d'arXiv le 19 novembre 2026 (titre et onze auteurs concordants : Lin, Liu, Pan, Lin, Dou, Xi, Huang, Yan, Han, Gui, Jiang).
- **Version lue** : version 4, datée du 18 mai 2026 sur la page 1. Le premier dépôt, 28 avril 2026, vient de la réponse de l'interface d'arXiv, hors pièce empreintée.
- **Fichier** : `docs/sources/arxiv-2604.25850-v1/arxiv-2604.25850v4.pdf`, empreinte `299f2633b4c13db7bed52434b4db7c48ea621993581014d30e7bcd036d3464df`, 35 pages.
- **Pages lues** : 1 à 35, en entier, par `pdftotext -layout`, page par page (bibliographie p. 10-15 parcourue ; consignes des agents p. 17-26 lues). Les figures 12 et 13 (p. 35) ont été regardées en image ; aucun chiffre n'en est tiré, les barres ne se lisent pas assez sûrement.
- **Vocabulaire de cette fiche** : le « concepteur » est l'agent qui modifie le harnais (« Evolve Agent ») ; l'« exécutant » est l'agent de code qui résout les tâches (« Code Agent ») ; l'« agent d'analyse des traces » est l'« Agent Debugger ». Le « taux de réussite au premier essai » est la moyenne des réussites sur k exécutions par tâche (« pass@1 », p. 6, p. 15). Une « campagne » est une course d'amélioration de dix tours.
- Aucune dépense, aucun appel à un modèle. Réseau : arxiv.org et export.arxiv.org seulement. Aucun refus d'outil.

## Les neuf réponses

**Q1. Ce qui est gardé, et qui l'écrit.**
- Un **manifeste des modifications** (`change_manifest.json`), une entrée par modification, écrit **par le concepteur lui-même** : identifiant, type (« new | improvement | rollback »), description, fichiers touchés, type de défaillance visé, **tâches que la modification doit réparer** (`predicted_fixes`), **tâches qu'elle risque de casser** (`risk_tasks`), niveau du composant, raison du choix de ce composant (p. 20-21 ; p. 5).
- Un **verdict par modification**, calculé **par la boucle, donc par un programme** : « the loop intersects the predicted-fix and predicted-regression sets with the observed task-level deltas to produce a per-edit verdict » (p. 5). Un fichier `change_evaluation.json` figure parmi les entrées de chaque tour (p. 18) et la consigne du concepteur renvoie à un « Change Attribution Report » (p. 20) ; le papier ne dit pas en toutes lettres que c'est le même objet.
- Une **histoire cumulée** (`evolution_history.md`, « Cumulative history of all iterations »), que le concepteur doit lire en premier (p. 18, p. 20). Qui l'écrit n'est pas dit dans les pages lues.
- L'**historique de versions** : un enregistrement par modification logique, qui permet le retour arrière fichier par fichier (p. 4, p. 20).
- Un **corpus de preuves** : un rapport d'analyse par tâche et une vue d'ensemble, écrits par l'agent d'analyse des traces ; les traces brutes restent consultables (p. 4-5).
- À ne pas confondre : la « mémoire de long terme » de ce papier (`LongTermMEMORY.md`) est un **composant du harnais de l'exécutant** — des leçons pour résoudre les tâches, que le concepteur peut modifier (p. 18-19). Ce n'est pas la mémoire de l'amélioration.

**Q2. Transmis à travers un changement, ou tenu pendant une course ?**
Tenu pendant une seule campagne : « We run a single AHE campaign of ten iterations » (p. 6). Ce qui traverse un changement est le **harnais figé**, « without further evolution », vers un autre banc (SWE-bench Verified, p. 7) et vers cinq autres réglages de modèle exécutant (p. 6, p. 8). Le manifeste, les verdicts et l'histoire ne sont portés vers aucune nouvelle optimisation : le papier n'en contient pas de seconde. Le harnais transféré emporte le composant « mémoire de long terme » de l'exécutant (douze leçons, p. 8), qui est un produit de l'amélioration, non son enregistrement.

**Q3. Héritage séparé de la tenue ?**
Non. Une seule campagne, depuis un harnais de départ volontairement minimal (p. 4, p. 6). Aucun bras avec ou sans manifeste, aucun bras à mémoire héritée, aucun bras à mémoire vide tenue. Non trouvé dans les pages lues (1 à 35).

**Q4. La mémoire est-elle ablatée ?**
La mémoire de l'amélioration, non. La seule ablation (tableau 3, p. 8) greffe **un composant évolué du harnais à la fois** sur le harnais de départ : mémoire de long terme seule 75,3 % ; outils seuls 73,0 % ; intergiciel seul 71,9 % ; consigne système seule 67,4 % ; contre 69,7 % au départ et 77,0 % pour le harnais complet (p. 8). Elle porte sur le produit, non sur l'enregistrement. Aucun des trois « piliers d'observabilité » (composants en fichiers, corpus de preuves, manifeste à prédictions) n'a de bras sans lui (cherché : toutes les occurrences de « ablat », p. 1, 2, 8 ; sections 4.4.1 et 4.4.2, p. 8-9 ; limites, p. 9-10). Courses indépendantes : une campagne (p. 6) ; deux exécutions par tâche dans la course de référence (tableau 4, p. 16) ; aucun intervalle, aucun test. Les auteurs écrivent : « a promising but high-variance setting » (p. 9).

**Q5. Prédictions écrites avant l'essai et confrontées au résultat ?**
Oui, et **en agrégat, contre un taux de hasard**.
- Écrites avant : chaque entrée du manifeste nomme les tâches à réparer et les tâches à risque (p. 21) ; au tour suivant, « We compare the round-N−1 prediction against the round-N ground truth, computing standard precision and recall over the 89 tasks separately for fixes and regressions » (p. 9).
- Réparations : précision 33,7 %, rappel 51,4 %, contre 6,5 % et 10,6 % pour une prédiction au hasard — moyenne des tours, neuf tours d'évaluation, une campagne (p. 9, figure 4).
- Régressions : précision 11,8 %, rappel 11,1 %, contre 5,6 % et 5,4 % au hasard (p. 9). En cumul : 43 prédictions de régression distinctes, 5 réalisées (11,6 %) ; 40 régressions non prévues (rappel 11,1 %) (p. 35). Les auteurs concluent : « reliable for fixes but blind to regressions » (p. 3).
- Pas de calibration : les prédictions sont des listes de tâches, sans probabilité. La construction du taux de hasard n'est pas décrite dans les pages lues. Aucun cumul chiffré des prédictions de réparation n'est donné dans le texte (le détail par tour est en figure 12, p. 35).
- Rôle dans la sélection : le verdict alimente une étape de retour arrière (algorithme 1, lignes 5 à 7, p. 5 ; « binding contracts that the attribution check rolls back if their predicted fixes do not materialize », p. 31 ; p. 34). La consigne du concepteur lui laisse pourtant le choix — garder, améliorer, ou revenir en arrière et changer de composant — à partir du rapport d'attribution (p. 20) ; au tour 7, après une baisse de 75,8 à 73,0, il n'a rien annulé et a corrigé (p. 30). La règle exacte qui déclenche un retour arrière et le nombre de modifications annulées ne sont pas donnés.
- Aucun bras ne teste si le fait d'écrire des prédictions améliore le résultat.

**Q6. Les modifications rejetées ou échouées sont-elles gardées ?**
Oui, dans la campagne : le manifeste a un type « rollback » (p. 21) ; l'historique de versions garde chaque modification (p. 4) ; l'histoire cumulée sert à savoir « what's been tried, what worked, what failed » (p. 20) ; la consigne dit : « If a variant's approach clearly failed, do not retry it » (p. 20).

**Q7. Quel modèle conçoit, quel modèle exécute ?**
Le même : GPT-5.4. Concepteur au réglage de raisonnement « xhigh », exécutant au réglage « high », agent d'analyse des traces sur GPT-5.4 aussi (tableau 4, p. 16 ; p. 6). Au transfert, seul l'exécutant change : GPT-5.4 « medium » et « xhigh », qwen-3.6-plus, gemini-3.1-flash-lite-preview, deepseek-v4-flash (p. 6, p. 8). Le concepteur n'est jamais varié.

**Q8. Le coût est-il apparié ou rapporté ?**
Rapporté pour l'exécutant seulement : jetons par essai (tableau 2, p. 7 : 461 milliers pour le harnais évolué, 526 pour le harnais de départ, 679 et 582 pour les deux méthodes comparées, sur SWE-bench Verified) et réussites par million de jetons (tableau 5, p. 17) ; durée de la campagne, « roughly 32 hours » (p. 6). Le coût de la boucle elle-même (jetons du concepteur et de l'agent d'analyse, dollars) n'est pas donné (cherché : « cost », « budget », « $ », p. 1-10 et 15-17). Appariement des budgets avec les deux méthodes comparées : non dit ; elles partent du même harnais de départ (p. 6).

**Q9. Sur quoi porte le résultat ; causalité affirmée et soutenue ?**
Sur le score d'un banc : taux de réussite au premier essai sur Terminal-Bench 2, de 69,7 % à 77,0 % en dix tours (p. 6), puis transfert. Langage causal : « isolating the gain to harness edits rather than analyzer or editor capability » (p. 2) ; « Ablations further localize the gain » (p. 1) ; « bottlenecked by observability, not by agent capability » (p. 2). Le plan : une campagne, deux exécutions par tâche, pas d'intervalle ; la thèse sur l'observabilité n'a aucun bras qui la retire. Les auteurs bornent eux-mêmes leur portée : cadre « high-variance » (p. 9) ; les chiffres de transfert entre modèles « conflate harness portability with operating-point coupling » (p. 10).

## Citations exactes

1. « decision observability pairs every edit with a self-declared prediction, later verified against the next round's task-level outcomes » (p. 1).
2. « Cross-iteration fix-precision of 33.7% and fix-recall of 51.4% sit roughly 5x above the random-prediction baselines of 6.5% and 10.6% » (p. 9).
3. « We run a single AHE campaign of ten iterations from the bash-only NexAU0 seed (§3.1) on Terminal-Bench 2, finishing in roughly 32 hours » (p. 6 ; phrase coupée par un tableau dans la mise en page, recollée ici).

## Ce que ce papier occupe par rapport à notre question de l'héritage séparé de la tenue

- Il occupe la **prédiction écrite avant l'essai, confrontée par tâche, avec un taux de justesse d'ensemble et un taux de hasard**, et l'usage du verdict pour annuler une modification — sur une campagne, un banc, un modèle (p. 5, p. 9, p. 35). La phrase de Yu et al. (p. 15) sur ce papier est juste.
- Il ne transmet pas l'enregistrement de l'amélioration à une autre optimisation, ne l'ablate pas, et n'a qu'une campagne : il ne sépare ni la tenue de l'absence de mémoire, ni l'héritage de la tenue.
- Ce qu'il transmet à travers un changement de banc ou de modèle est le harnais figé, sans reprise de l'optimisation ; ce n'est pas notre question.

## Réserves

1. Les taux de justesse viennent d'une seule campagne de neuf tours d'évaluation ; les figures 12 et 13 (p. 35) montrent des taux qui vont de près de zéro à près de cent d'un tour à l'autre (« swing from near-zero to near-saturation », p. 35).
2. La page 15 annonce que chaque tableau dit son nombre d'exécutions par tâche ; les tableaux 1 et 3 ne le disent pas dans le texte extrait. Dans le tableau 1 (p. 6), la valeur 91,7 % sur quatre tâches ne peut pas venir de deux exécutions par tâche : c'est un calcul de ce lecteur, non une affirmation du papier.
3. Version 4 d'arXiv lue ; aucune version d'actes n'a été cherchée.
4. Le code public cité (p. 1, p. 16) n'a pas été ouvert.

# Fiche de lecture — Xia et al. (2026), « RRSI: Regularized Recursive Self-Improvement of Agent Harnesses » — v1

## En-tête

- **Qui écrit** : lecteur neuf lancé par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) sur le mot de Lazar « go lecture voisins » (GO-2026-11-19-10) ; modèle Fable 5.2 (`claude-fable-5-2`). Il n'a écrit ni la décision N-073, ni ses compléments, ni la note de lecture de Yu et al.
- **Identifiant** : arXiv 2609.24972, pris dans la bibliographie de Yu et al. (p. 13 du PDF `a8299ba5…`), vérifié par l'interface publique d'arXiv le 19 novembre 2026 (titre et quatorze auteurs concordants : Xia, Han, Wang, Chen, Zhuang, Lee, Huang, Yu, CuiZhu, Ming, Yao, Gokturk, Pfister, Lee).
- **Version lue** : version 3, datée du 4 octobre 2026 sur la page 1 (la page porte aussi « 2026-10-06 »). Le premier dépôt, 21 septembre 2026, vient de la réponse de l'interface d'arXiv, hors pièce empreintée.
- **Fichier** : `docs/sources/arxiv-2609.24972-v1/arxiv-2609.24972v3.pdf`, empreinte `26f8b5417f8a60c9284bb4a36d3981c41b8e071134aea0bf3402fe9584c8cd76`, 27 pages.
- **Pages lues** : 1 à 27, en entier, par `pdftotext -layout`, page par page (bibliographie p. 11-15 parcourue). Les figures 1, 3 et 4 (p. 2, 8, 10) ne s'extraient pas en texte ; leurs chiffres ne sont cités que là où le texte ou un tableau les redonne.
- **Vocabulaire de cette fiche** : le « proposeur » est le modèle qui écrit les modifications du harnais ; la « politique » est le modèle figé qui exécute les tâches ; une « course » est une évolution de 20 ou 40 tours ; l'« ensemble d'évolution » est le jeu de tâches sur lequel la course est notée ; « hors distribution » désigne les bancs que la course n'a jamais vus. Le nom de la méthode se lit « auto-amélioration récursive régularisée ».
- Aucune dépense, aucun appel à un modèle. Réseau : arxiv.org et export.arxiv.org seulement. Aucun refus d'outil.

## Les neuf réponses

**Q1. Ce qui est gardé, et qui l'écrit.**
Une **histoire des modifications**, un enregistrement par modification élémentaire de chaque candidat évalué : tour, composant modifié, **hypothèse testée**, différence de code, **changement de score**, **changement relatif de coût**, et **acceptation** (0 ou 1) (équation 10, p. 21 ; p. 5). Le composant est pris dans une liste de neuf (consigne, flot de contrôle, configuration, sortie, gestion du contexte, outil, compétence, mémoire, sous-agent ; équation 12, p. 21). Qui écrit : le composant et l'hypothèse sont **déclarés par le proposeur** (algorithme 1, ligne 9, p. 20 ; « the declared component », p. 25) ; le score, le coût et l'acceptation sont **mesurés et inscrits par la boucle de sélection, un programme** (algorithme 2, lignes 3, 4 et 18, p. 20). Les modifications groupées dans un même candidat partagent la mesure du candidat (p. 20-21). La boucle en tire trois résumés servis au proposeur : composants déjà essayés, meilleur gain récent par composant, composants à supprimer (équations 11 et 14, p. 21). Un « analyst » écrit en plus le retour sur les échecs d'un tour à l'autre (p. 7).

**Q2. Transmis à travers un changement, ou tenu pendant une course ?**
Tenu pendant une course : « The proposer conditions on this history in later rounds » (p. 5). Une course part du harnais de départ avec le meilleur score initialisé sur lui (p. 19) ; rien ne dit qu'une histoire lui soit donnée au départ. Ce qui traverse un changement est le **harnais final**, « run unchanged on held-out benchmarks » (p. 2). Avec une autre politique, la course est refaite à part : « Harness evolution is run independently with each frozen policy » (tableau 3, p. 9). Le harnais évolué avec Gemini 3.5 Flash est aussi évalué tel quel avec Gemini 3.1 Flash Lite (p. 9-10). Aucune histoire n'est portée vers une nouvelle course.

**Q3. Héritage séparé de la tenue ?**
Non. Les bras du tableau 2 (p. 9) sont : harnais de départ sans évolution ; évolution sans régularisation ; sans les régularisations du côté de la proposition ; sans celles du côté de l'acceptation ; méthode complète. Aucun n'hérite d'une histoire. Non trouvé dans les pages lues (1 à 27).

**Q4. La mémoire est-elle ablatée ?**
Pas isolément. L'ablation « w/o proposal regularizers » retire **ensemble** les trois contraintes du côté de la proposition : le plafond décroissant du nombre de modifications par candidat, l'attribution du crédit d'après l'histoire, et l'exploration dirigée vers les composants non essayés (p. 4-5, p. 8). Résultat sur les tâches de travail de bureau (« agentic workspace », banc Harvey LAB ; tableau 2, p. 9), bras sans ces trois contraintes contre méthode complète : 90,7 contre 90,5 sur l'ensemble d'évolution ; 88,8 contre 89,2 sur les tâches tenues à l'écart du même banc ; 41,9 contre 43,6 en moyenne hors distribution ; 2,69 contre 2,42 millions de jetons par essai. Ce que le proposeur voit encore dans ce bras n'est pas dit. Courses : le nombre par bras d'ablation n'est pas dit ; la « répétition indépendante de la recherche » porte sur « every evolution run of the main experiment » (deux courses, tableau 7, p. 24-25), et rien ne dit qu'elle couvre les bras d'ablation. Test : un rééchantillonnage apparié par tâche, 10 000 tirages, pour le seul gain de la méthode complète sur le harnais de départ (tableau 6, p. 24) ; aucun pour les contrastes d'ablation. Deux essais par tâche sur ce domaine (tableau 5, p. 23).

**Q5. Prédictions écrites avant l'essai et confrontées au résultat ?**
En partie. Chaque modification porte « the hypothesis it tests » (p. 5), et une proposition peut nommer les tâches qu'elle compte réparer : « A candidate is free to explain itself by naming the tasks it expects to fix » (p. 25). Ce qui est confronté est le **changement mesuré de score et de coût du candidat**, et son acceptation — au niveau du candidat. Aucune confrontation des tâches annoncées aux issues par tâche, aucun taux de justesse, aucune calibration dans les pages lues (cherché : « predict », « expect » — p. 24 et 25 seulement). Rôle dans la sélection : aucun pour les prédictions ; la sélection applique à des scores mesurés un plancher corrigé du bruit, une règle de coût et une garde par domaine (algorithme 2, p. 20). Le critique de fuite lit la différence de code, « not the proposal » (algorithme 1, ligne 10, p. 20), et veille à ce que les noms de tâches annoncés restent dans la justification et n'entrent pas dans le code (p. 25).

**Q6. Les modifications rejetées ou échouées sont-elles gardées ?**
Oui, pour les candidats évalués : « rejected mechanisms remain negative evidence » (p. 5) ; l'acceptation vaut 0 pour un candidat admissible battu par un meilleur (p. 21). Deux limites dans le texte : l'histoire est écrite « Ignoring candidates that fail before a valid measurement is obtained » (p. 21) ; un candidat écarté par le critique de fuite avant l'évaluation n'a pas de mesure, et le papier ne dit pas s'il entre dans l'histoire (p. 5, p. 20-21). Ordres de grandeur : sur les tâches de bureau, « Four edits accepted out of 32 evaluated candidates over 20 rounds » (tableau 9, p. 27) ; dans la course de code, 38 candidats passés au critique, un seul refus net (p. 25).

**Q7. Quel modèle conçoit, quel modèle exécute ?**
Le proposeur, l'analyste et le critique de fuite sont tous Claude Opus 4.8 ; la politique figée est Claude Opus 4.8 dans les trois domaines (p. 7). La course de code est refaite avec Gemini 3.5 Flash pour politique (tableau 3, p. 9), et son harnais évalué avec Gemini 3.1 Flash Lite (tableau 4, p. 10). Le modèle proposeur de cette seconde course n'est pas redit ; la seule mention est celle de la page 7. Dans les courses principales, le concepteur est donc le même modèle que la politique.

**Q8. Le coût est-il apparié ou rapporté ?**
Rapporté pour la politique, et utilisé par la méthode. Jetons de la politique par essai (tableau 2, p. 9) : 1,56 million pour le harnais de départ, 2,42 pour la méthode complète, 3,80 pour l'évolution sans régularisation. Le coût est un champ de l'histoire et une condition d'acceptation (équation 7, p. 6). Appariement : les méthodes comparées « share the frozen policy, the evolve set and the candidate budget » (p. 7) — le nombre de candidats est égal, pas les jetons. Le coût de la recherche elle-même (jetons du proposeur, dollars, durée) n'est pas donné (cherché : « $ », « dollar », « hours » — rien).

**Q9. Sur quoi porte le résultat ; causalité affirmée et soutenue ?**
Sur des scores de bancs (huit bancs, trois domaines) et sur le coût en jetons de la politique. Les auteurs demandent « what produced that property » (p. 8) et y répondent par l'ablation en deux groupes. Le plan soutient le gain de la méthode complète sur le harnais de départ (deux courses, tableau 7, p. 25 ; intervalles par rééchantillonnage des tâches, tableau 6, p. 24) ; il ne permet pas d'attribuer un effet à l'histoire seule, retirée avec deux autres contraintes dans un seul domaine, sans répétition dite. Les auteurs distinguent eux-mêmes l'incertitude d'évaluation de l'incertitude de recherche (p. 24).

## Citations exactes

1. « RRSI therefore records, for every evaluated candidate, the component it modifies, the hypothesis it tests, the source diff, the resulting score and cost changes, and whether the candidate was accepted. » (p. 5)
2. « The proposer conditions on this history in later rounds: rejected mechanisms remain negative evidence, while successful mechanisms retain explicit credit. » (p. 5)
3. « We ablate the two groups of regularizers, (i) the proposal-side constraints and (ii) the acceptance-side constraints. » (p. 8)

## Ce que ce papier occupe par rapport à notre question de l'héritage séparé de la tenue

- Il occupe l'**enregistrement par modification qui garde ses rejets**, avec hypothèse, différence de code, score, coût et décision, relu par le proposeur aux tours suivants (p. 5, p. 21). La phrase de Yu et al. (p. 16) sur ce papier est juste.
- Cette histoire est tenue dans une course ; elle n'est pas transmise à une autre course et n'est retirée qu'avec deux autres contraintes : le papier ne mesure ni l'effet de la tenue seule, ni celui d'un héritage.
- Ce qu'il transmet à travers un changement de banc ou de modèle est le harnais final, évalué sans reprise de l'optimisation ; ce n'est pas notre question.

## Réserves

1. Les enregistrements complets tour par tour sont annoncés sur le site du projet (p. 25) ; ils n'ont pas été ouverts (réseau limité à arXiv).
2. Version 3 d'arXiv lue ; les versions 1 et 2 n'ont pas été comparées.
3. Le tableau 9 (p. 27) et le texte p. 25 donnent des comptes de candidats pour deux courses seulement ; aucun compte n'est donné pour la course de conception d'ingénierie.

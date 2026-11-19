# Fiche de lecture — Zhang et al. (2026), « Causal Improvement Graph for Agentic Harness Optimization » — v1

## En-tête

- **Qui écrit** : lecteur neuf lancé par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) sur le mot de Lazar « go lecture voisins » (GO-2026-11-19-10) ; modèle Fable 5.2 (`claude-fable-5-2`). Il n'a écrit ni la décision N-073, ni ses compléments, ni la note de lecture de Yu et al.
- **Identifiant** : arXiv 2610.05039, pris dans la bibliographie de Yu et al. (« Zhang et al., 2026c », p. 13 du PDF `a8299ba5…`), vérifié par l'interface publique d'arXiv le 19 novembre 2026 (titre et six auteurs concordants : Zhang, Liu, Wang, Lin, Li, Tao).
- **Version lue** : version 1, datée du 4 octobre 2026 sur la page 1 ; seule version déposée à la date de lecture, d'après la réponse de l'interface d'arXiv.
- **Fichier** : `docs/sources/arxiv-2610.05039-v1/arxiv-2610.05039v1.pdf`, empreinte `db5a0778c76d62704e8a73b890b603149718800715896d4397ba598cefd013f8`, 22 pages.
- **Pages lues** : 1 à 9 (résumé, travaux voisins, méthode, expériences, conclusion) et 13 à 22 (toutes les annexes : schéma du graphe, comparaison des représentations, définitions des variantes d'ablation, variabilité entre courses, sémantique des verdicts, interfaces, consignes, jetons du proposeur, configuration, étude de cas), par `pdftotext -layout`, page par page. **Non lues** : 10 à 12 (bibliographie). Le papier n'a pas de section de limites ; la seule limite dite est la dernière phrase de la conclusion (p. 9).
- **Vocabulaire de cette fiche** : le « proposeur » est le modèle qui analyse, planifie et écrit les modifications ; le « solveur » est le modèle qui exécute les tâches ; une « recherche » est une course d'amélioration bornée à huit évaluations de candidats ; une « vague » est un tour de la recherche ; le « graphe » est le graphe causal d'amélioration que les auteurs abrègent en trois lettres.
- Aucune dépense, aucun appel à un modèle. Réseau : arxiv.org et export.arxiv.org seulement. Aucun refus d'outil.

## Les neuf réponses

**Q1. Ce qui est gardé, et qui l'écrit.**
Un **graphe persistant** à quatre types de nœuds (p. 3, p. 4, p. 13) : **preuve** (un comportement observé, avec sa tâche et son harnais d'origine) ; **hypothèse** (une explication réfutable, sa portée, et une **appréciation révisable**) ; **intervention** (la modification exécutable qui teste l'hypothèse, avec son harnais parent) ; **issue** (le résultat mesuré et son verdict). Les arêtes notent la provenance, le soutien, la contradiction et la filiation des harnais (p. 4). Pour chaque candidat, l'issue enregistre : le résultat, les tâches corrigées, régressées et inchangées par rapport au parent, la fidélité de l'intervention (le changement voulu a-t-il été exécuté), l'accord avec la direction prédite, et le verdict (équation 5, p. 5). Qui écrit : le contenu des preuves, hypothèses et plans vient d'appels au proposeur, à portée locale — « they do not own the persistent state or the complete discovery process » (p. 4) ; les mesures et l'inscription au graphe sont le fait d'un programme : « The runner alone commits graph transitions and measured outcomes » (p. 18) ; une étiquette numérique (amélioration globale, soutien local, réfuté, incertain) est posée par règle sur les scores (p. 16), puis un appel au proposeur révise l'appréciation de l'hypothèse (p. 5, p. 18).

**Q2. Transmis à travers un changement, ou tenu pendant une course ?**
Tenu pendant une recherche. Les auteurs l'écrivent : « Our evaluation focuses on Harness optimization within individual searches, leaving the transfer and adaptation of persistent improvement state across tasks and models as a promising direction for future work. » (p. 9). Le graphe est initialisé à partir des harnais de départ (algorithme 1, ligne 1, p. 5) ; la recherche s'arrête quand les huit évaluations sont dépensées (p. 6, p. 13). Les proposeurs et les solveurs varient d'une recherche à l'autre (p. 7-8) ; le graphe n'est pas porté de l'une à l'autre.

**Q3. Héritage séparé de la tenue ?**
Pas entre recherches. **À l'intérieur d'une recherche**, en revanche, le papier sépare trois états, ce qui est le plus proche de notre question parmi les quatre papiers lus, à l'échelle de la vague et non de la course :
- état **remis à zéro à chaque vague** (variante M2 : « The graph is still reset before the next round », p. 15) ;
- état **porté d'une vague à la suivante et révisable** (M3 : « Carry the relational state across rounds », p. 15) ;
- état **porté mais seulement allongé**, sans révision des conclusions antérieures (B2, p. 15).

Toutes les variantes gardent l'accès à l'histoire brute (« access to eligible raw history », p. 15) : ce qui est porté ou non est l'état compilé, pas l'histoire. Le protocole d'ablation a deux vagues (p. 15 ; « two waves of four », p. 7, p. 20) : le portage joue sur un seul passage, de la première vague à la seconde. Il n'existe aucun bras « graphe vide au départ, tenu pendant la recherche » comparé à un bras « graphe hérité d'une recherche antérieure ». S'y ajoute une comparaison unique (annexe A.9.1, p. 21-22) : deux branches depuis le même point, « differing only in the supplied assessment state » — appréciation mise à jour contre appréciation gardée ; 60,44 contre 57,33 en validation, une recherche, une comparaison (p. 22).

**Q4. La mémoire est-elle ablatée ?**
Oui, pièce par pièce, sur SWE-bench Verified (100 tâches d'entraînement, 50 de validation, 100 de test ; p. 19-20), solveur Qwen3.7-Flash, deux proposeurs (A : GPT-5.6 Sol ; B : DeepSeek-V4-Pro), **cinq courses par case** (« five-run means », p. 14 ; « means over five independent runs », p. 19), moyenne et écart-type d'échantillon (tableau 6, p. 16). Score de test du harnais choisi sur la validation (tableau 4, p. 9), proposeur A puis B :

| variante | ce qui change | A | B |
|---|---|---|---|
| M0, histoire brute | appels par étapes sur l'histoire brute, rien de compilé | 58,0 | 56,4 |
| M1, état typé | enregistrements typés, remis à zéro à chaque vague | 59,6 | 57,4 |
| M2, relations | relations logiques, remises à zéro à chaque vague | 60,8 | 58,8 |
| B1, relations mélangées | relations de M2 permutées | 59,0 | 57,4 |
| M3, portage et révision | état porté entre vagues, révisable | 62,2 | 59,6 |
| B2, portage sans révision | état porté, seulement allongé | 61,0 | 58,8 |
| M4, méthode complète | la sélection des plans lit le graphe | 63,6 | 61,4 |
| B3, sans relations entre enregistrements | enregistrements portés et révisables, sans arêtes | 62,0 | 59,2 |

Porter et réviser, contre remettre à zéro : +1,4 et +0,8 point (M3 moins M2). Porter sans réviser, contre remettre à zéro : +0,2 et 0,0 (B2 moins M2 ; calcul de ce lecteur sur le tableau 4). Aucun test statistique : « All reported differences are differences of run means » (p. 15). L'appariement des courses n'est pas dit. Ce qui n'est jamais retiré : l'histoire brute.

**Q5. Prédictions écrites avant l'essai et confrontées au résultat ?**
Écrites avant, confrontées par enregistrement ; **aucun agrégat**. Chaque plan porte « predicted effects, and falsification conditions » (p. 17) ; l'étude de cas montre une « Prediction registered before evaluation » et sa condition d'échec (p. 21). Après l'évaluation, l'issue note l'accord avec la direction prédite (p. 5), et l'appréciation de l'hypothèse devient soutenue, contredite ou non résolue (p. 18). Aucun taux de prédictions tenues, aucune calibration, aucun taux de base dans les pages lues (cherché : toutes les occurrences de « predict », p. 2, 5, 9, 13, 14, 16, 17, 18, 20, 21, 22). Un seul cas est montré (p. 9, p. 21). Rôle dans la sélection : aucun pour le choix du harnais final — « Final selection uses eligible measured performance, independently of whether the candidate's motivating explanation is supported » (p. 16) ; un rôle dans le **choix des expériences suivantes** : la sélection des plans lit les appréciations et note chaque plan sur sept échelles de 0 à 4, dont la force de la preuve et la réfutabilité (p. 4, p. 17), par jugement du proposeur, « not a deterministic maximization of a weighted score » (p. 17). Donner à cette sélection l'accès au graphe vaut +1,4 et +1,8 point dans l'ablation (M4 moins M3, tableau 4, p. 9).

**Q6. Les modifications rejetées ou échouées sont-elles gardées ?**
Oui. « Across successful and unsuccessful experiments, Gt retains the observations, hypotheses, interventions, and outcomes » (p. 4) ; une issue réfutée est inscrite « as a negative but informative result » (p. 21) ; le sélecteur garde, pour les plans non retenus, « its selection rationale and rejection reasons » (p. 4, p. 17) ; une révision conserve les versions antérieures (p. 18).

**Q7. Quel modèle conçoit, quel modèle exécute ?**
Plusieurs couples, toujours fixes dans une recherche (p. 19) : GPT-5 mini conçoit et exécute dans la comparaison aux méthodes publiées (tableau 1, p. 6) ; GPT-5.4 conçoit pour cinq solveurs (Qwen3.5-Plus, Qwen3.7-Flash, DeepSeek-V4-Flash, GLM-5.2-Fast-Preview, MiniMax-M2.5 ; p. 7) ; cinq proposeurs (GPT-5.5, GPT-5.6 Sol, GLM-5.3, Kimi K3, DeepSeek-V4-Pro) pour le solveur Qwen3.5-Plus (tableau 3, p. 7-8) ; ablations avec GPT-5.6 Sol ou DeepSeek-V4-Pro et le solveur Qwen3.7-Flash (p. 14).

**Q8. Le coût est-il apparié ou rapporté ?**
Le nombre d'évaluations de candidats est apparié : huit par recherche (p. 6, p. 20). Les jetons du proposeur sont rapportés dans une seule configuration dite « representative » (tableau 7, p. 19) : histoire brute complète, 0,530 million de jetons, 8 candidats, 41,3 % ; méthode arrêtée au même budget de jetons, 5 candidats, 46,8 % ; méthode complète, 0,820 million (1,55 fois), 8 candidats, 52,9 %. Le point à budget égal est « reconstructed from the search trajectory » (p. 19), non une course à part. Pas de dollars. Les jetons ne sont pas appariés dans les tableaux principaux.

**Q9. Sur quoi porte le résultat ; causalité affirmée et soutenue ?**
Sur le score d'un banc : test tenu à l'écart du harnais choisi sur la validation. Le mot « causal » est borné par les auteurs : « We use causal in the operational sense of intervention-grounded improvement reasoning. Formal causal identification of the task distribution is outside this formulation. » (p. 4). Ils disent que les ablations « support » leur conception (p. 1, p. 9, p. 16). Le plan : cinq courses par case, deux proposeurs, un banc, un solveur, une construction cumulative où chaque variante se compare à la précédente, sans test ; des écarts de 0,8 à 2,2 points face à des écarts-types de 0,0 à 1,1 (tableau 6, p. 16).

## Citations exactes

1. « Our evaluation focuses on Harness optimization within individual searches, leaving the transfer and adaptation of persistent improvement state across tasks and models as a promising direction for future work. » (p. 9)
2. « M3 Persistent Revision. Carry the relational state across rounds. New Outcomes can revise the status or scope of earlier Hypotheses and can redirect subsequent Interventions. » (p. 15)
3. « We use causal in the operational sense of intervention-grounded improvement reasoning. Formal causal identification of the task distribution is outside this formulation. » (p. 4)

## Ce que ce papier occupe par rapport à notre question de l'héritage séparé de la tenue

- Il occupe, **à l'intérieur d'une recherche**, la séparation entre porter un état structuré d'une vague à la suivante et le recompiler à chaque vague, et entre porter en allongeant et porter en révisant — cinq courses par case, deux proposeurs, un banc, sans test (p. 9, p. 15, p. 16).
- Il ne porte pas cet état d'une recherche à une autre, et le dit (p. 9) : il n'a pas de bras « hérité » contre « vide au départ mais tenu ».
- Son résultat est le score d'un banc ; ses prédictions sont écrites et relues par cas, sans taux d'ensemble.

## Réserves

1. **Écarts-types nuls (règle R4)** : quatre cases du proposeur A ont un écart-type de 0,0 sur cinq courses (M0, B1, B2, B3 ; tableau 6, p. 16), ainsi qu'une case du tableau 3 (61,0 ± 0,0 ; p. 7), sur un test de 100 tâches. Le papier ne dit pas si une « course » est une recherche indépendante ou une réévaluation du même harnais (« with a binary success result per task in each run, then report the mean across five runs », p. 19). Tant que ce point n'est pas levé, les cinq courses ne peuvent pas être dites cinq recherches indépendantes.
2. Le code n'est pas publié à la date de la version lue (« We will release the code publicly upon acceptance », p. 19).
3. La variante M0 des ablations n'est pas la même que le témoin « Full History » des autres tableaux : elle partage le calendrier à deux vagues et les appels par étapes de la méthode (p. 15, p. 20).
4. Version 1 d'arXiv, prépublication ; pages 10 à 12 non lues.

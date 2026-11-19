# Fiche de lecture — Kim et al. (2026), « Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents » — v1

## En-tête

- **Qui écrit** : lecteur neuf du groupe C, lancé par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) sur le mot de Lazar « go lecture voisins » (GO-2026-11-19-10) ; modèle Fable 5.2 (`claude-fable-5-2`). Il n'a écrit ni la décision N-073, ni ses compléments, ni la note de lecture de Yu et al.
- **Identifiant** : arXiv 2604.14004, pris dans la bibliographie de Yu et al. (p. 11 du PDF `a8299ba5b16577dd328d602e32f35b914b9393ffb38148d2410f358d4d90ff3d`), vérifié par l'interface publique d'arXiv le 19 novembre 2026 : titre concordant, six auteurs (Kim, Kang, Kim, Yang, Ren, Hwang), les quatre premiers concordent avec la bibliographie de Yu et al.
- **Version lue** : version 1, datée du 15 avril 2026 sur la page 1 ; seule version déposée d'après l'interface d'arXiv (hors pièce empreintée). La bibliographie de Yu et al. ne dit pas quelle version ils citent.
- **Fichier** : `docs/sources/arxiv-2604.14004-v1/arxiv-2604.14004v1.pdf`, empreinte `106898da2db2101d0596f1764d9a96244769bc2047f5ed1ad0790db921620404`, 19 pages.
- **Pages lues** : 1 à 19, en entier, par `pdftotext -layout`, page par page (bibliographie p. 10-12 parcourue ; consignes de fabrication des souvenirs p. 16-19 lues). Les figures 3 à 6 n'ont été lues que par le texte que `pdftotext` en extrait ; aucun chiffre n'est tiré des courbes de la figure 6.
- **Vocabulaire de cette fiche** : l'« exécutant » est l'agent de code qui résout les tâches ; un « souvenir » est une entrée de la mémoire ; la « réserve » est l'ensemble des souvenirs où l'on puise. Les quatre formes de souvenir sont nommées « trajectoire », « suite de commandes » (« Workflow »), « résumé » et « leçon » (« Insight »). La « réussite en trois essais » est la part des tâches réussies au moins une fois sur trois exécutions (« Pass@3 ») ; le « taux de réussite moyen par essai » est la moyenne sur les trois exécutions (« Pass@1 » moyen, p. 13).
- Aucune dépense, aucun appel à un modèle. Réseau : arxiv.org et export.arxiv.org seulement. Aucun refus d'outil.

## Les dix réponses

**Q1. Ce qui est gardé, et qui l'écrit.**
Quatre formes, tirées de la même histoire d'exécution H = (tâche, suite de raisonnement, action, observation) (p. 4) :
- **trajectoire** : la tâche, puis toutes les commandes et leurs résultats, raisonnements retirés ; elle garde les pas ratés (p. 4). C'est une concaténation.
- **suite de commandes** : un but et les actions jugées utiles, extraites par un modèle (p. 4 ; consignes p. 16-17).
- **résumé** : un résumé de la tâche et un paragraphe sur l'environnement, les actions, le résultat et la raison du succès ou de l'échec, écrits par un modèle (p. 4 ; consignes p. 17-18).
- **leçon** : un titre, une description en une phrase, un contenu d'une à trois phrases, avec la consigne de ne nommer ni fichier ni détail (p. 4 ; consignes p. 18-19) ; format repris de ReasoningBank (p. 4).
Qui écrit : un modèle appelé hors de la course, après coup, et non l'exécutant pendant sa tâche. Le même modèle, gpt-5-mini, sert à fabriquer les souvenirs, à exécuter les tâches et à juger (p. 4). L'étiquette « réussi » ou « échoué » qui choisit la consigne de fabrication vient d'un juge par modèle, non du vérificateur du banc (p. 4).

**Q2. Transmis à travers un changement, ou tenu pendant une course ?**
Transmis, et seulement transmis. La réserve servie pour un banc est faite des souvenirs de **tous les autres bancs**, le banc d'essai exclu (p. 4) ; un essai transmet aussi les souvenirs d'un modèle à un autre (tableau 6, p. 9). Rien n'est écrit pendant l'essai : la fabrication est faite avant, hors ligne (p. 3). Trois souvenirs, choisis par ressemblance de plongements, sont mis dans la consigne système au début de chaque tâche (p. 4-5).

**Q3. Héritage séparé de la tenue ?**
Non. Toute la mémoire est héritée ; aucun bras ne tient une mémoire pendant l'essai. Les bras exacts : sans mémoire (« Zero-shot »), et quatre bras à mémoire héritée, un par forme (tableau 1, p. 5). Le plus proche d'un bras « tenu » est une comparaison à deux méthodes d'autres auteurs sur trois bancs (tableau 2, p. 5) : ReasoningBank, que le papier dit n'utiliser que des souvenirs du même domaine (97 souvenirs), et AgentKB (5 899 souvenirs d'autres tâches de raisonnement), contre 431 souvenirs pour la méthode du papier. La façon dont ReasoningBank est lancé (accumulation au fil de l'essai ou non) n'est pas dite dans les pages lues. Cette comparaison change à la fois la méthode, l'origine et le nombre des souvenirs : elle ne sépare rien.

**Q4. La mémoire est-elle ablatée ?**
Retirée en bloc, oui : c'est le bras sans mémoire. Sont aussi variés : la forme (quatre), la taille de la réserve (un quart, la moitié, trois quarts, tout ; figure 6, p. 9), le nombre de domaines sources (figure 6, p. 9), le modèle qui a produit les souvenirs (tableau 6, p. 9), la méthode de choix (tableau 7, p. 9). Répétitions : trois exécutions par condition (p. 5). Tâches : au plus cent par banc, tirées au hasard quand le banc en compte plus (p. 4). Mêmes tâches dans tous les bras, donc appariement possible, mais aucune analyse appariée, **aucun intervalle, aucun test** (cherché : pages 1 à 19).

**Q5. Des prédictions écrites avant l'essai ?**
Non trouvé dans les pages lues (1 à 19). Le papier dit seulement que la trajectoire permet à l'agent d'estimer le résultat attendu d'une commande (p. 4) ; rien n'est écrit ni confronté.

**Q6. Les essais échoués sont-ils gardés ?**
Oui, comme source de souvenirs : une exécution jugée ratée donne un souvenir, avec une consigne propre qui demande le mauvais schéma à éviter ou la leçon de l'échec (p. 4 ; p. 17, 18, 19).

**Q7. Quel modèle conçoit, quel modèle exécute ?**
Il n'y a pas de concepteur : le harnais (mini-swe-agent) est fixe (p. 4). gpt-5-mini fabrique les souvenirs, exécute et juge (p. 4) ; GPT-5 classe après coup les apports des souvenirs (p. 6). Deux autres exécutants, DeepSeek V3.2 et Qwen3-Coder-480B, ne sont essayés qu'avec la forme « leçon » (tableau 1, p. 5).

**Q8. Coût.**
Ni jetons ni dollars, nulle part. Sont rapportés : le nombre de souvenirs de la réserve (tableau 2, p. 5) et le nombre servi par tâche, trois (p. 5). La longueur des souvenirs diffère selon la forme (la suite de commandes est dite bien plus courte que la trajectoire, p. 4) et n'est pas donnée : la place prise dans la consigne n'est pas appariée entre formes.

**Q9. Objet du résultat, causalité.**
Le score de six bancs de code (p. 4). Les auteurs affirment une causalité : selon eux, le degré d'abstraction décide de ce qui se transfère (p. 1, p. 2, p. 10). Le plan qui la porte : (i) quatre formes comparées sur un seul modèle (tableau 1, p. 5) ; (ii) à forme fixée (« leçon »), les 30 % de souvenirs les plus liés à leur tâche contre les 30 % les moins liés, tri fait par un modèle : 0,523 contre 0,534 en moyenne de trois bancs, soit 1,1 point (tableau 4, p. 7 ; la mesure n'est pas nommée dans la légende) ; (iii) un modèle formel dont la proposition est énoncée sans démonstration dans les pages lues (p. 13-14). Deux choses varient avec la forme sans être tenues fixes : la clé de recherche (la trajectoire est cherchée par ressemblance entre tâches, les trois autres par un plan de quatre à cinq phrases écrit par le modèle, p. 5) et la longueur.

**Q10. « Abstrait » contre « concret » : ce qui est comparé exactement.**
- **Les deux pôles** : la trajectoire (commandes et sorties brutes d'une autre tâche, raisonnements retirés) et la leçon (trois champs courts, sans nom de fichier). Entre les deux, la suite de commandes et le résumé.
- **Où** : six bancs — LiveCodeBench v6, Aider Polyglot, SWE-Bench Verified, Terminal-Bench 2, ReplicationBench, MLGym-Bench (p. 4). Les quatre formes ne sont comparées que sur **gpt-5-mini** (tableau 1, p. 5).
- **Répétitions** : trois exécutions ; pas d'intervalle.
- **Résultat publié, réussite en trois essais** (tableau 1, p. 5) : sans mémoire 0,523 ; trajectoire 0,534 ; suite de commandes 0,538 ; résumé 0,546 ; leçon 0,560. **Taux moyen par essai** (tableau 8, p. 13) : 0,435 ; 0,438 ; 0,449 ; 0,451 ; 0,454.
- **Par banc, l'ordre n'est pas uniforme.** En réussite en trois essais, la trajectoire fait mieux que la leçon sur LiveCodeBench (0,940 contre 0,930) et Aider Polyglot (0,490 contre 0,470), autant sur SWE-Bench Verified (0,770), moins bien sur les trois autres ; elle passe sous le bras sans mémoire sur Terminal-Bench 2 (0,270 contre 0,315) et MLGym-Bench (0,583 contre 0,667) (tableau 1, p. 5). Les deux bancs où la trajectoire tient sont les deux bancs de programmation au niveau de la fonction ; c'est une lecture des tableaux par ce lecteur, les auteurs ne le disent pas.
- **Contredit-il l'indice de Meta-Harness ?** Non : les deux essais ne comparent pas la même chose. (a) *Qui lit.* Ici, l'exécutant d'une tâche ; dans Meta-Harness, le proposeur qui cherche un meilleur harnais. Yu et al. le notent pour ce papier : ces mémoires servent l'agent qui exécute les tâches (Yu, p. 16). (b) *D'où vient la trace.* Ici, d'une **autre tâche d'un autre banc**, par construction (p. 4) ; dans Meta-Harness, des candidats passés de **la même recherche** (note de lecture de Yu et al., a.7). (c) *Comment elle est servie.* Ici, trois souvenirs collés dans la consigne ; là, tout l'historique en fichiers, que le proposeur parcourt à son gré (même note). (d) *Ce qui est mesuré.* Ici, le score de tâches ; là, le score des harnais trouvés. Les deux constats peuvent tenir ensemble : une trace brute d'un autre domaine, collée dans la consigne d'un exécutant, l'entraîne à la recopier (cas d'étude, p. 8) ; un résumé retire au concepteur le détail qui sert à diagnostiquer. **Aucun des deux ne teste la situation de Yu et al.** : une mémoire du concepteur, portée à travers un changement de banc ou de modèle. Kim et al. ne comparent pas les formes quand la trace vient du même domaine.

## Recalcul de ce lecteur (à relire avant tout usage)

Les moyennes des tableaux 1 et 8 ne sont pas des moyennes simples des six bancs. Elles se retrouvent à trois décimales si l'on pondère par le nombre de tâches, avec 100, 100, 100, 89, 90 et 12 tâches — nombres que le papier ne donne pas et que ce lecteur déduit du pas des scores (0,315 × 89 = 28 ; 0,111 × 90 = 10 ; 0,667 × 12 = 8), soit 491 tâches. Les moyennes des tableaux 2, 4 et 6, elles, sont des moyennes simples de trois bancs.
- En tâches réussies au moins une fois sur trois, sur 491 : sans mémoire 257 ; trajectoire 262 ; suite de commandes 264 ; résumé 268 ; leçon 275. **La leçon dépasse la trajectoire de 13 tâches sur 491, et le bras sans mémoire de 18.**
- En moyenne simple des six bancs, le tableau 1 donnerait : sans mémoire 0,534 ; trajectoire 0,529 ; suite de commandes 0,534 ; résumé 0,554 ; leçon 0,578. La phrase de la page 7, selon laquelle toutes les variantes à mémoire dépassent le bras sans mémoire, tient donc avec la pondération par tâche, et ne tient pas pour la trajectoire en moyenne simple.
- Sur MLGym-Bench, un écart de 8,3 points est une tâche sur douze.

## Trois citations

1. « Memory generation is performed offline with results saved prior to memory transfer learning, while memory retrieval is executed for each query during the inference. » (p. 3)
2. « We gather memories from all benchmarks except the testing benchmark for each memory format. » (p. 4)
3. « In contrast, low-abstraction memories like Trajectories retain excessive task-specific details that can distract the agent, confirming that raw execution traces are less suitable for cross-task transfer. » (p. 2)

## Ce que ce papier occupe par rapport à notre question de l'héritage séparé de la tenue

- Il occupe la comparaison des **formes** d'une mémoire **héritée** pour l'**exécutant**, entre bancs de code et entre modèles, sur le score d'un banc ; l'écart entre les deux pôles est de 13 tâches sur 491, trois exécutions, un modèle, sans intervalle.
- Il ne tient aucune mémoire pendant l'essai : il n'a donc ni bras « mémoire née vide et tenue », ni bras « héritée puis tenue », et ne dit rien de la mémoire d'un concepteur.
- Pour nous : à citer comme indice sur la forme de l'archive, **avec sa prémisse** (mémoire de l'exécutant, traces d'un autre domaine, trois souvenirs dans la consigne), à côté de Meta-Harness et sans les opposer comme deux réponses à une même question.

## Réserves

1. Les nombres de tâches par banc et la pondération des moyennes sont déduits, non lus.
2. Le tableau 4 ne nomme pas sa mesure ; ses valeurs sont de l'ordre des taux moyens par essai du tableau 6.
3. La figure 6 parle de neuf domaines sources (p. 9) alors que six bancs sont décrits (p. 4) ; les pages lues ne disent pas lesquels.
4. Le chiffre de 431 souvenirs (tableau 2, p. 5) n'est rattaché à aucun banc d'essai précis.
5. Un seul lecteur ; aucune contre-lecture à ce jour.

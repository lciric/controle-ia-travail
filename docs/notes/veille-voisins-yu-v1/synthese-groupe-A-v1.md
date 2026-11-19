# Synthèse du groupe A — ce que la mémoire de l'amélioration enregistre, chez quatre voisins cités par Yu et al. (2026) — v1

## En-tête

- **Qui écrit** : lecteur neuf lancé par la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) sur le mot de Lazar « go lecture voisins » (GO-2026-11-19-10) ; modèle Fable 5.2 (`claude-fable-5-2`). Il n'a écrit ni la décision N-073, ni ses compléments, ni la note de lecture de Yu et al. Deux autres lecteurs lisent d'autres voisins en parallèle ; cette synthèse ne couvre que les quatre papiers ci-dessous.
- **Heures** (`date -u`) : début 2026-11-19T07:32Z ; fiches écrites à partir de 07:39Z.
- **Rien ne s'applique par cette note.** Toute révision d'une phrase d'une décision de Lazar est un nœud de Lazar ; ce qui suit est proposé.
- **Contexte lu avant** : `docs/decisions/decision-N-073-complement-2-memoire-transmise-v1.md` ; `docs/notes/veille-yu-memoire-v1/lecture-yu-approfondie-v2.md`, sections a.2, a.5, a.7 et (b) ; Yu et al., `docs/sources/arxiv-2611.18856-v1/arxiv-2611.18856.pdf` (`a8299ba5b16577dd328d602e32f35b914b9393ffb38148d2410f358d4d90ff3d`, empreinte vérifiée), pages 11 à 16.

| n° | papier | identifiant et version | fichier | empreinte | pages lues | fiche |
|---|---|---|---|---|---|---|
| 1 | Lin et al., « Agentic Harness Engineering » | arXiv 2604.25850, version 4 (18 mai 2026) | `docs/sources/arxiv-2604.25850-v1/arxiv-2604.25850v4.pdf` | `299f2633b4c13db7bed52434b4db7c48ea621993581014d30e7bcd036d3464df` | 1 à 35 sur 35 | `fiche-agentic-harness-engineering-v1.md` |
| 2 | Xia et al., « RRSI » | arXiv 2609.24972, version 3 (4 octobre 2026) | `docs/sources/arxiv-2609.24972-v1/arxiv-2609.24972v3.pdf` | `26f8b5417f8a60c9284bb4a36d3981c41b8e071134aea0bf3402fe9584c8cd76` | 1 à 27 sur 27 | `fiche-rrsi-v1.md` |
| 3 | Zhang et al., « Causal Improvement Graph » | arXiv 2610.05039, version 1 (4 octobre 2026) | `docs/sources/arxiv-2610.05039-v1/arxiv-2610.05039v1.pdf` | `db5a0778c76d62704e8a73b890b603149718800715896d4397ba598cefd013f8` | 1 à 9 et 13 à 22 sur 22 (10 à 12, bibliographie, non lues) | `fiche-graphe-causal-amelioration-v1.md` |
| 4 | Luo et al., « HarnessBank » | arXiv 2607.13683, version 2 (30 juillet 2026) | `docs/sources/arxiv-2607.13683-v1/arxiv-2607.13683v2.pdf` | `360efedc16753f6bfe062cd58b1e2f7e9984bbdd36a8cc79ed363af686aeaeb2` | 1 à 7 sur 9 (8 et 9, bibliographie, parcourues) | `fiche-harnessbank-v1.md` |

- **Introuvables** : aucun. Les quatre identifiants sont dans la bibliographie de Yu et al. (p. 12-13) ; titres et auteurs vérifiés par l'interface publique d'arXiv.
- Aucune dépense, aucun appel à un modèle, aucune instance. Réseau : arxiv.org et export.arxiv.org seulement. Aucun refus d'outil.

## Table papiers × questions Q2 à Q6

Chaque case dit ce que **ce** papier fait ; « non trouvé » veut dire « non trouvé dans les pages lues », jamais « libre » (règle R8). Les pages renvoient au PDF du papier de la ligne.

| papier | Q2 — transmis à travers un changement ? | Q3 — héritage séparé de la tenue ? | Q4 — mémoire ablatée ? | Q5 — prédictions écrites avant et confrontées ? | Q6 — rejets gardés ? |
|---|---|---|---|---|---|
| **Lin et al.** | Non. Une seule campagne de dix tours (p. 6). Seul le harnais figé passe à un autre banc et à d'autres modèles, « without further evolution » (p. 7-8). | Non. Aucun bras avec ou sans enregistrement, aucun bras hérité. | Non. La seule ablation greffe un composant du harnais à la fois (tableau 3, p. 8). Une campagne, deux exécutions par tâche (p. 16), aucun test. | **Oui, en agrégat.** Tâches à réparer et tâches à risque écrites par modification (p. 21), confrontées au tour suivant (p. 9). Réparations : précision 33,7 %, rappel 51,4 %, contre 6,5 % et 10,6 % au hasard ; régressions : 11,8 % et 11,1 %, contre 5,6 % et 5,4 % (p. 9) ; 5 régressions prévues sur 43 annoncées (p. 35). Pas de calibration. Le verdict sert au retour arrière (p. 5, p. 31) ; la règle exacte n'est pas donnée. | Oui, dans la campagne : type « rollback » au manifeste (p. 21), histoire cumulée (p. 20). |
| **Xia et al.** | Non. L'histoire sert les tours suivants de la même course (p. 5). Le harnais final est évalué tel quel ailleurs (p. 2) ; avec une autre politique, la course est refaite à part (p. 9). | Non. Cinq bras, aucun n'hérite d'une histoire (tableau 2, p. 9). | Pas isolément. L'histoire est retirée avec deux autres contraintes de proposition (p. 8) : 41,9 contre 43,6 hors distribution (tableau 2, p. 9). Nombre de courses par bras non dit ; aucun test sur ce contraste. | En partie. Une hypothèse par modification (p. 5) ; ce qui est confronté est le changement de score et de coût du candidat (p. 21). Les tâches annoncées restent dans la justification (p. 25). Aucun taux de justesse, aucun rôle dans la sélection (p. 20). | **Oui**, pour les candidats évalués : acceptation 0 ou 1 par enregistrement (p. 21), « rejected mechanisms remain negative evidence » (p. 5). Non dit pour les candidats écartés avant mesure (p. 21). |
| **Zhang et al.** | Non, et les auteurs le disent : le transfert de l'état entre tâches et modèles est laissé à des travaux futurs (p. 9). | **Dans une recherche seulement.** État remis à zéro à chaque vague, état porté et révisable, état porté sans révision (p. 15) ; l'histoire brute reste dans tous les bras. Deux vagues (p. 15). Aucun bras hérité d'une recherche antérieure. | **Oui**, pièce par pièce. Cinq courses par case, deux proposeurs, un banc (p. 14, p. 19). Porter et réviser contre remettre à zéro : +1,4 et +0,8 point ; porter sans réviser contre remettre à zéro : +0,2 et 0,0, calcul de ce lecteur (tableau 4, p. 9). Aucun test (p. 15) ; quatre écarts-types nuls (p. 16), voir réserves. | Écrites avant, avec condition de réfutation (p. 17, p. 21), confrontées par enregistrement (p. 5, p. 16). Aucun taux d'ensemble. Sans rôle dans le choix du harnais final (p. 16) ; lues par la sélection des plans suivants (p. 4, p. 17). | Oui : expériences échouées, issues réfutées et raisons de rejet des plans (p. 4, p. 17, p. 21). |
| **Luo et al.** | Non. Banque vide au départ (p. 3) ; boucle repartie à froid sur chaque modèle (p. 6). Seul un correctif fini est greffé sur d'autres modèles (tableau 2, p. 7). | Non. Aucun bras ne part d'une banque héritée. | Non pour la banque. L'ablation porte sur le crible de sélection (tableau 3, p. 7). Une comparaison par banc (p. 6) ; test apparié par tâche (p. 5). | Forme étroite : spécification d'activation déclarée d'avance et vérifiée (p. 5). Aucune liste de tâches confrontée, aucun taux de justesse des diagnostics. | Non décrit. La banque n'admet que des candidats vérifiés et garde un harnais par case (p. 3-4). |

## Ce que les quatre lectures établissent

1. **Aucun des quatre ne transmet l'enregistrement de l'amélioration à travers un changement de banc, de modèle ou de course.** Trois transmettent le produit (le harnais figé ou un correctif) et l'évaluent sans reprendre l'optimisation ; Zhang et al. écrivent que le transfert de l'état est un travail futur (p. 9).
2. **Aucun des quatre ne compare une mémoire héritée à une mémoire née vide et tenue pendant la course.** Le plus proche est Zhang et al., à l'échelle de la vague dans une recherche de deux vagues : état compilé porté contre état recompilé, portage simple contre révision (p. 15, tableau 4 p. 9). L'histoire brute y reste dans tous les bras : ce n'est pas non plus un bras « sans mémoire ».
3. **Aucun des quatre n'a de bras « sans aucune histoire » contre « histoire tenue » qui isole la tenue.** Lin et al. et Luo et al. n'ablatent pas leur enregistrement ; Xia et al. le retirent avec deux autres contraintes ; Zhang et al. gardent l'histoire brute partout.
4. **La prédiction écrite avant l'essai, confrontée par tâche, avec un taux de justesse d'ensemble comparé au hasard, est faite par Lin et al.** (p. 9, p. 35), sur une campagne et un banc. La phrase de Yu et al. (p. 15) est juste, et la lecture y ajoute l'agrégat, que Yu et al. ne donnent pas pour leur propre mémoire (note de lecture de Yu, § a.5).
5. **L'enregistrement qui garde ses rejets est fait par Xia et al.** (p. 5, p. 21) ; la phrase de Yu et al. (p. 16) est juste. Zhang et al. gardent aussi les expériences échouées et les raisons de rejet des plans (p. 4).
6. **Les quatre résultats portent sur le score d'un banc**, aucun sur des découvertes. Les concepteurs : GPT-5.4 chez Lin et al. (p. 16), Claude Opus 4.8 chez Xia et al. (p. 7) et chez Luo et al. (p. 5), et plusieurs modèles chez Zhang et al., de GPT-5 mini à GPT-5.6 Sol (p. 19). Seuls Zhang et al. font varier le concepteur (cinq proposeurs, tableau 3, p. 7) ; chez Lin et al. et Xia et al., le concepteur est le même modèle que l'exécutant dans les courses principales.

## Proposition de phrase

Pour remplacer, dans la rédaction du point 1 du complément 2 de N-073, la dernière phrase — « Nous ne la disons ni nouvelle ni propre : plusieurs travaux voisins cités par Yu et al. (p. 3, p. 15-16) n'ont pas été lus sur ce point. » — **en ce qui concerne ces quatre papiers** :

> « Nous ne la disons ni nouvelle ni propre. Quatre des travaux voisins que Yu et al. citent pour la mémoire de l'amélioration (p. 15-16) ont été lus sur source ; aucun des quatre ne compare une mémoire héritée à une mémoire née vide et tenue pendant la course. Lin et al. (2026) confrontent, dans une seule campagne, les prédictions écrites avant l'essai aux issues par tâche, avec un taux de justesse comparé au hasard (p. 9), sans transmettre ni retirer cet enregistrement. Xia et al. (2026) tiennent pendant une course une histoire qui garde ses rejets (p. 5, p. 21) et ne la retirent qu'avec deux autres contraintes (p. 8). Luo et al. (2026) tiennent une banque de harnais née vide (p. 3), sans bras qui s'en passe. Zhang et al. (2026) séparent, à l'intérieur d'une recherche, l'état porté d'un tour au suivant de l'état remis à zéro, et le portage simple de la révision (p. 15), pour le score d'un banc ; ils laissent le transfert de cet état entre tâches et modèles à des travaux futurs (p. 9). »

Variante courte, si la place manque :

> « Nous ne la disons ni nouvelle ni propre. Parmi les travaux voisins cités par Yu et al. (p. 15-16), quatre ont été lus sur source (Lin et al., Xia et al., Zhang et al., Luo et al., 2026) : chacun tient un enregistrement de l'amélioration pendant une course, aucun ne le transmet à une autre course ni ne compare une mémoire héritée à une mémoire née vide et tenue ; le plus proche, Zhang et al., sépare dans une même recherche l'état porté d'un tour au suivant de l'état remis à zéro (p. 15). »

Trois précisions sur cette proposition :
- Elle parle de **ces quatre papiers** et de rien d'autre. Elle ne dit pas que la question est libre : les autres voisins cités par Yu et al. (p. 3, p. 15-16) sont lus par deux autres lecteurs ou restent à lire, et la phrase finale doit être complétée par leurs résultats avant tout texte sortant.
- « Aucun des quatre » est un constat sur les pages lues (détail en tête de chaque fiche), pas sur le champ.
- Les pages citées renvoient chacune au PDF du papier nommé, non à celui de Yu et al. ; un texte sortant devra lever cette ambiguïté par des références complètes.

## Ce que ces lectures changent ailleurs, à trancher par Lazar

1. **Complément 2 de N-073, point 3** (« À lire sur source avant tout texte qui en parle ») : les deux lectures demandées sont faites. Lin et al. et Xia et al. peuvent être cités de première main, dans les limites des fiches.
2. **Complément 2, point 4** : l'interdit d'écrire « des prédictions vérifiées guident la sélection » vise Yu et al. et reste juste pour eux. Chez Lin et al., le verdict de la confrontation alimente une étape de retour arrière (p. 5, p. 31), sans que la règle soit donnée ni son effet mesuré : à écrire ainsi, pas plus.
3. **Note de lecture de Yu, § (b) point 6** : « mesurer la justesse des prédictions en agrégat contre un taux de base » y est rangé parmi ce que le plan à trois bras ferait et que Yu et al. ne font pas. Lin et al. le font déjà pour des modifications de harnais (p. 9). Ce point du plan est à décrire comme déjà fait ailleurs, pour un autre objet.
4. **Plan à trois bras** (sans mémoire ; mémoire neuve tenue ; mémoire héritée), matière première de l'atelier d'idées : Zhang et al. donnent un précédent de méthode pour le contraste « état porté contre état remis à zéro » et pour le contraste « allonger contre réviser » (p. 15), avec cinq courses par case. Le portage sans révision n'y apporte presque rien de plus que la remise à zéro (+0,2 et 0,0 point ; différence calculée par ce lecteur sur leur tableau 4, les auteurs comparant ce bras au portage révisable) : un indice à citer avec la prémisse, sous la réserve des écarts-types nuls.
5. **Indice sur l'héritage d'un produit** : chez Luo et al., un correctif greffé sur un modèle dont la défaillance dominante diffère n'aide presque pas (tableau 2, p. 7). Cela ne porte pas sur une mémoire, mais va dans le sens d'un héritage utile seulement quand la cible ressemble à la source.

## Pistes de seconde main rencontrées, non lues

Citées par les quatre papiers pour des points voisins de notre question ; hors de ma liste, donc non lues, et rapportées telles que le papier citant les décrit (règle R7 : rien d'opposable).

- « HarnessFix » (Chen et al., 2026) : selon Zhang et al. (p. 2), « retains records of accepted and rejected changes ».
- « HSI » (Zhou, 2026), « AutoSaddler » (Park et al., 2026), « Living-Harness » (Du et al., 2026), « EviGraph » (Ren et al., 2026) : selon le tableau 5 de Zhang et al. (p. 14), mémoire persistante, et pour certains prédictions explicites et état en graphe.
- « Recursive harness self-improvement » (Lee et al., 2026, arXiv 2607.15524) : selon Zhang et al. (p. 1-2), réutilisation entre tours par retours appariés sur des histoires de révision.
- « Harness updating is not harness benefit » (Lin et al., 2026, arXiv 2605.30621) et l'attribution par différence de Ding et al. (2026) : selon Xia et al. (p. 2, p. 11), séparation entre modifier le harnais et en tirer un bénéfice.

## Réserves

1. Un seul lecteur ; aucune contre-lecture de ces fiches à ce jour. Aucun chiffre de ces fiches n'entre dans un préenregistrement ou un papier sans relecture de la page citée (R7).
2. Zhang et al. : quatre écarts-types nuls sur cinq courses dans le tableau des ablations (p. 16) ; le papier ne dit pas si une « course » est une recherche indépendante ou une réévaluation (p. 19). La valeur des contrastes de portage en dépend (règle R4).
3. Les quatre papiers sont lus dans leur version d'arXiv ; aucune version d'actes n'a été cherchée. Pour Luo et al., un autre titre circule pour le même identifiant (cité par Xia et al., p. 13) ; la version 1 n'a pas été lue.
4. Aucun dépôt de code ni site de projet n'a été ouvert (réseau limité à arXiv) ; les enregistrements complets annoncés par Xia et al. (p. 25) n'ont pas été vus.
5. « Non trouvé » dans une fiche vaut pour les pages lues de ce papier. Ce n'est ni un trou du champ, ni une place libre (R8).

# Question pour le collisionneur — le pari apparié borné (pari de signe) : valide, puissant, suffisant pour G1 ? — v1 (brouillon de conv-audit ; session-depot fige sa version)

Écrite par conv-audit (instance du 27 octobre 2026, Fable 5.1) de 17:10 à 17:11 UTC (heure de fichier ; l'en-tête
scellé d'abord disait « 17:12 », estimée : corrigé avant la poussée). Mot de Lazar, 17:54 heure de
Paris : « demande aussi l'avis du collisionneur sur ta conception ». Forme « arbitre », trois modèles, trois tours
(conception, équipe rouge croisée, riposte), une tentative par cellule, un refus arrête le tour (jamais reformulé).
**Dépense : sur le mot de Lazar, chez session-depot.** Côté Claude, seulement Opus 5.5 et Fable 5.1.

**Garde de sûreté (R-519)** : la question porte sur la **statistique d'un instrument de mesure défensif** (comparer deux
moniteurs de sabotage à taux de faux positifs apparié, avec une garantie séquentielle). Aucune recette de sabotage, aucun
mode d'attaque, aucune consigne d'organisme n'est demandé ni accepté ; les « tricheurs » dont il est question sont des
artefacts statistiques (seuils fuités, dépendance ignorée, comparateur choisi après coup), pas des attaques d'agent.

## Question

« Un programme de recherche sur le contrôle des intelligences artificielles (pièce P) doit établir, à sa porte G1, que
sa surveillance par sondes internes agrégées séquentiellement a un **rappel supérieur** à la meilleure base boîte noire,
**à 1 % de faux positifs**, avec un intervalle à 95 %, rapporté par mode de sabotage (pièces N-008, N-054). Son pôle de
recherche automatique (pièce C) juge aujourd'hui des lois par instance par un pari (processus e, inégalité de Ville,
seuil 1/α, règle e-BH). La pièce S propose un **second type d'engagement** pour ces affirmations globales : le « pari
apparié borné » — unité = la tâche (groupe d'épisodes dépendants) ; contraste borné v ∈ [−1 ; 1] calculé par le noyau
après le gel (différence des parts d'épisodes sabotés alertés par deux moniteurs au même seuil nominal, ou son signe) ;
nul fixe E[v] ≤ 0 sur la population des tâches ; richesse = mélange sur une grille de mises λ et sur les deux formes du
produit Π(1 + λ·v) ; garde appariée sur les faux positifs (second pari sur f_A − f_B contre « ≥ δ »), promotion si les
deux richesses atteignent 1/α ; niveau absolu des faux positifs rapporté par suite de confiance, jamais certifié ;
dimensionnement par simulation (pièce S, section 6 : environ 40 tâches sabotées pour 20 points d'écart, 70 à 150 tâches
honnêtes pour δ de 0,10 à 0,05).

1. **Validité.** La construction est-elle valide telle quelle (surmartingale sous le nul composite, union des nuls pour
   la garde, mélange des formes) ? Quelles hypothèses cachées (indépendance entre tâches, tirage des tâches dans la
   population, seuils fixés avant l'épreuve, paires « voisines » formées après le gel) sont les plus fragiles sur un banc
   réel, et comment les tester sans dépenser ? Le niveau de la pièce S (0,02 et 0,014 en simulation) est-il le signe d'un
   pari trop prudent, et à quel prix de puissance ?
2. **Puissance et alternatives.** Existe-t-il, pour la même affirmation (supériorité appariée à faux positifs appariés),
   une forme séquentielle **plus puissante** à garantie égale : mise prévisible (estimation en ligne de λ), processus e
   de rang ou de permutation appariée, test séquentiel à deux échantillons, lecture par seuils stochastiques, ou autre ?
   Chiffrez (illustratif, en nombre de tâches pour 20 points d'écart) et citez (titre, auteurs, année ; nous vérifions
   sur PDF). Le signe pur bat la différence de parts à dix épisodes par tâche ; est-ce général ?
3. **Le point de fonctionnement.** « À 1 % de faux positifs » n'est pas certifiable sur quelques centaines d'épisodes
   (pièce S, 2.4). La lecture « rappel supérieur au même taux nominal, sans asymétrie de faux positifs supérieure à δ »
   est-elle une traduction acceptable du critère de G1, ou faut-il changer le critère (taux de faux positifs plus élevé ;
   comparaison sans seuil par courbe ; appariement par quantiles honnêtes) ? Qu'est-ce qui serait trompeur ?
4. **Les pentes.** Pour « le rappel croît avec l'horizon » (H2) et « la courbe décroît plus doucement avec N » (H3), la
   pièce S propose un contraste de contrastes sur des tâches appariées (même tâche à deux horizons, à deux N). Est-ce la
   bonne forme, ou vaut-il mieux une loi déclarée en l'horizon contre une famille nulle ajustée sous contrainte de signe
   (inférence universelle), ou une régression séquentielle ? Quelle forme donne une conclusion lisible hors du pôle ?
5. **Ce qui manque pour G1.** En supposant la pièce S corrigée, qu'est-ce qui manque encore au préenregistrement de G1 :
   choix du comparateur « meilleure base noire » (règle scellée sur la partie de développement), strates par mode avec
   e-BH, mode tenu à l'écart (N-054), tâches honnêtes réservées, taille du banc, critères d'arrêt ? Donnez le plan
   d'analyse en dix lignes tel que vous le gèleriez, et ce qui vous ferait dire que le pari apparié ne convient pas.
6. **Recommandation** : adopter, amender (quoi, précisément), ou remplacer ; ce qui vous ferait changer d'avis. »

## Faits à servir (noms neutres ; aucun sigle ; aucun score de pilote ; rien de tout ceci n'est servi à un organisme)

- S : `pari-de-signe/conception-pari-de-signe-v1.md` (empreinte dans son compagnon), avec `simulation-dimensionnement-v1.py`
  (`6643f5f1…`) et sa sortie (`30b85423…`).
- P : programme v2, **sections 4, 5, 8, 10 et 12 seulement** (`docs/programme-controle-ia-v2.md`, `2fd63bad…`, sur
  `main`) ; décisions N-007/N-008 (`docs/decisions/decision-N-007-N-008-v1.md`) et N-054 (`docs/decisions/decision-N-054-v1.md`),
  empreintes dans leurs compagnons.
- C : programme de conception de l'organisme v3, **sections 3 et 4 seulement** (`programme-conception-organisme-v3.md`,
  `866a8ffb…`).
- J : la conception du nul des filles v2 et sa lecture (`nul-des-filles-v2/conception-nul-des-filles-v2-v1.md`,
  `35fe3f7f…` ; `lecture-experience-2-v1.md`), pour la forme du juge actuel ; le LISEZMOI v5 de l'orchestrateur v7
  (`orchestrateur-pole-v7/LISEZMOI-orchestrateur-pole-v7-v5.md`) pour le pari à fraction.
- **Rien d'autre** : ni listes de failles, ni synthèses d'attaque, ni lectures de courses réelles (le tour « questions
  fortes » a été refusé par deux modèles ; pièce K et pièces d'attaque hors de toute question désormais).

Chemins relatifs à `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/` sur la branche
`canal/conv-audit-n04`, sauf « sur `main` ».

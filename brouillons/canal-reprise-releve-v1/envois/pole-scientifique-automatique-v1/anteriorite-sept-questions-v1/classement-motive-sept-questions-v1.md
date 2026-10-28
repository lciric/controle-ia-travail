# Classement motivé des sept questions distinctives et de la question-pont — v1

Lignée conv-audit, instance de reprise (compte neuf, Fable 5.1), 28 octobre 2026, écrit à partir du relevé `date -u` de
**13:15 UTC**. Rend la **tâche 1** du brief `brief-questions-distinctives-nouvelle-instance-v1.md` (`…` voir compagnon) :
trier les sept questions et la question-pont par antériorité, et dire lesquelles sont brûlantes et attaquables.

**Statut R7 : tout ce qui suit est RAPPORTÉ par huit sous-agents de recherche (modèle Opus, un par question, cadre commun
`cadre-commun-sous-agents-v1.md`), d'après résumés et pages HTML ; rien n'est vérifié sur PDF empreinté. Aucun chiffre
n'est opposable. Les verdicts « ouvert » sont des INFÉRENCES par absence, à vérifier plus durement (R8).** Les huit
rapports détaillés sont dans ce dossier (`anteriorite-Q1-v1.md` … `anteriorite-Qpont-v1.md`), chacun avec ses requêtes.
Contrainte tenue par les huit : niveau méthode seul, aucune technique d'attaque rapportée (R-339, R-597).

## 1. Verdict d'ensemble (à lire d'abord)

**Aucune des huit n'est ouverte en entier ; aucune n'est occupée en entier. Les huit sont SEMI-OCCUPÉES**, avec le même
motif partout : les **briques** sont occupées (souvent hors du champ de la sécurité de l'IA, parfois dedans depuis
2025-2026), l'**assemblage sous co-évolution avec familles tenues à l'écart et juge figé** ne l'est pas. Conséquence :
notre marque ne peut pas être « l'idée », elle est **la mesure** (noter la théorie comme prévisionniste, borner les
fausses promotions, tracer le coût de la boucle, contrôler l'artefact dans la boucle). C'est cohérent avec la direction
déjà prise (R-347) et ne la contredit pas.

**Trois questions sont brûlantes et attaquables tout de suite ou après un prérequis gratuit : Q-pont, Q4, Q6.** Deux sont
brûlantes mais coûteuses : Q2 (théorie gratuite, mesure payante), Q3 (la plus distinctive, prérequis lourd). Deux attendent
une dépense franche : Q5, Q7. Q1 dépend de Q-pont et exige un témoin « attaquant » que nous refusons de construire.

**Deux alertes qui changent le programme, à porter à Lazar :**
1. **Q4 — notre « lemme du plafond d'horizon » a un voisin formel publié** : Ramtin, Nain, Towsley (arXiv 2601.20022,
   temps continu 2509.17778) démontrent qu'un adversaire furtif fait passer le délai de détection de CUSUM de
   O(log γ) à Θ(γ) avec un dommage total borné en γ^(1−ρ). À comparer sur PDF **avant** toute revendication du lemme
   (carte des hypothèses, lemme L0 et suivants). Nœud possible : revendication du lemme.
2. **Q3 — SLEIGHT-Bench** (Anthropic et Redwood, arXiv 2605.16626, mai 2026) tire déjà des familles d'angles morts
   d'une analyse de ce que les moniteurs supposent, et mesure les taux de détection par catégorie. Ce qui reste, c'est
   la notation préenregistrée de la théorie contre le hasard. Notre formulation de Q3 doit citer SLEIGHT-Bench comme
   occupant le plus proche, pas comme fond.

## 2. Tableau de classement

| question | antériorité | confiance | attaquable | prérequis ou dépense | brûlante ? |
|---|---|---|---|---|---|
| **Q-pont** synthétique → réel | semi-occupée | moyenne | **tout de suite** (boîte noire) | opérationnaliseur de la propriété P ; corpus réel étiqueté (SHADE-Arena, ControlArena) ; boîte blanche après dépense (activations) | **oui** : commande toute la voie synthétique |
| **Q4** le diffus, axe à part | semi-occupée | moyenne-haute | **tout de suite** (théorie + rejeu de règles de décision) | générateur de traces diffuses à dilution réglable (découpage de traces existantes, sans attaquant) ; boîte blanche après dépense | **oui** : notre cadre exact, deux préimpressions de juillet 2026 l'ouvrent et laissent l'agrégation déployable ouverte |
| **Q6** artefact de source dans la boucle | semi-occupée | moyenne | **tout de suite** (bras « fuite textuelle », rétention des coefficients) | épisodes appariés même tâche / même modèle / avec et sans sabotage, de plusieurs générateurs | **oui** : différenciateur de rigueur, résultat de Lin et al. (ICLR 2026) montre l'effondrement 89 % → 2 % |
| **Q2** juge figé garanti | semi-occupée | moyenne | **après prérequis** (théorie gratuite : composition d'e-processus) ; mesure comparative après dépense | étiquettes de vérité fiables ; trois régimes de juge sur une même boucle | oui : deux préimpressions de 2026 certifient déjà des promotions par e-processus — la fenêtre se ferme |
| **Q3** prédire ses angles morts | semi-occupée | moyenne | **après prérequis** lourd | taxonomie de familles fixée par un tiers **avant** la dérivation ; pôle théorie mûr ; évaluation finale modeste en dépense | oui, la plus distinctive ; SLEIGHT-Bench occupe le mécanisme, pas la notation |
| **Q1** théorie contre attaquant empirique | semi-occupée | moyenne-faible | **après Q-pont**, et seulement avec un témoin attaquant **publié** (jamais construit) | Q-pont validée ; réutiliser les attaquants publiés comme témoins ; dépense forte sinon | moyenne : principe occupé en apprentissage classique (Laidlaw, Casper) → à revendiquer comme transfert |
| **Q5** universalité de la boucle | semi-occupée | moyenne | **après dépense** | suite ordonnée de 5 à 8 familles ; exécutions complètes × graines × permutations d'ordre | moyenne : HyperAgents (2603.19461) occupe déjà « évaluer le méta-niveau » ; la courbe coût-par-rang en défense est libre |
| **Q7** mélange des canaux | semi-occupée (point précis ouvert) | moyenne | **après dépense** ; méta-niveau (pondérations) possible sur processeur avec scores précalculés | activations + scores textuels précalculés ; boucle itérée | faible : la moins distinctive, posable par tout laboratoire disposant de 2412.09565 et 2507.12691 |

## 3. Motivation par question (résumé ; détail dans chaque rapport)

**Q-pont.** La métrique existe hors champ (coefficient de corrélation simulation-réel, Kadian et al. 1912.06321 : 0,18 → 0,844
une fois les failles du simulateur corrigées — avertissement direct). En sécurité de l'IA, le transfert synthétique → réel
est mesuré pour l'entraînement des sondes (Kirch et al. 2511.17408 : corrélation 0,793 des écarts de généralisation, et
transfert **mauvais** pour les comportements « ambigus dans le texte » — exactement les nôtres), pour la sélection de
moniteurs (Storf et al. 2603.00829) et pour l'environnement (Redwood, « Simulated control evaluations », 23 oct 2026).
Personne ne fabrique des épisodes à propriété théorique P contrôlée pour corréler, propriété par propriété, détection
synthétique et détection réelle. **Survit** : la corrélation de rang par propriété, plus les conditions d'effondrement.
**Piège majeur** : le « réel » est presque toujours instruit ; il faut l'écrire au préenregistrement.

**Q4.** Non-transfert concentré → diffus déjà montré en boîte noire : Makins et al. (AISI, 2607.07368, effet de
fragmentation) et Hills et al. (2607.02514 : un moniteur à état fait passer l'évasion graduelle de 87 % à 54 %, « aucun
moniteur ne capture les deux stratégies »). Théorie de la séparation disponible hors champ (Ramtin et al. ci-dessus ;
Shewhart contre CUSUM ; Urbina et al. CCS 2016). **Survit** : (i) mesure contrôlée du transfert d'un moniteur évolué, à
dommage total constant, comparée à la prédiction γ·D ≈ constante ; (ii) même score, deux règles de décision (seuil par
instant contre règle séquentielle) ; (iii) effet d'une boucle sélectionnée sur du concentré. **Correction au cadre** : la
défense de Terekhov et al. évolue (instruction itérée), elle n'est pas figée ; corriger la ligne correspondante de
`anteriorite-coevolution-et-boite-blanche-v1.md` lors du versement v2.

**Q6.** Occupé densément côté constat et contrôles statiques : Fomin (2602.14161 : classifieur d'identité du jeu de
données à 96,6 %, correctifs classiques inopérants), Lin et al. (ICLR 2026, témoins du même modèle), Natarajan et al.
(2602.01425 : la paire d'instructions explique 70,6 % de la variance des sondes), AFLite, Wallace et al. (2110.08514 :
vingt tours de collecte adversariale ne purgent pas les artefacts). Voisin dynamique le plus proche hors champ : Pathak
et al. CVPR 2023 (les artefacts migrent « en bloc » d'un tour à l'autre). **Survit** : la part de la généralisation
mesurée expliquée par l'artefact, **par tour**, avec témoins appariés + rétention des coefficients + permutation du
générateur + bras « fuite textuelle ». Se branche directement sur N-053.

**Q2.** Briques occupées : analyse de données adaptative (Dwork et al. 2015, Blum et Hardt « Ladder »), e-processus et
promotion certifiée (« Pay Only for Disagreement » 2609.17560, qui compose déjà les promotions mais **exclut les pertes
jugées** et n'a pas d'adversaire ; 2609.32267 sous dérive de l'évaluateur), canaris et jeu final intouché (2609.25848,
cadre conceptuel sans garantie). Les occupants co-évolutifs ont un juge figé **non garanti** (SafeCoEvo), ou le même
juge-modèle pour la récompense et l'évaluation (MAGIC, AgentSafeEvo). **Survit** : l'assemblage sous co-évolution de
moniteurs, et la mesure des trois régimes. **Ce qui ne survit pas** : « un évaluateur fixe empêche Goodhart » — c'est
connu faux sans précaution. Théorie et simulation sur processeur ; la comparaison des régimes sur une boucle réelle est
une dépense.

**Q3.** SLEIGHT-Bench (voir alerte) ; Fetterman (2606.27091) donne la seule prédiction a priori par famille confirmée
trouvée, anecdotique, hors sécurité de l'IA ; la tradition des détecteurs d'intrusion (Ptacek et Newsham 1998, Wagner et
Soto 2002, Tan et Maxion 2002, Inoue et Somayaji 2006) dérive des classes d'évasion des hypothèses du détecteur sans
jamais noter la prédiction. **Survit** : noter la théorie comme prévisionniste, préenregistrée, par famille tenue à
l'écart, contre une référence de hasard, au fil des générations. **Pièges** : puissance faible (une dizaine de familles),
circularité si les familles sont définies à partir des échecs, prédictions triviales quand le taux de base d'échec est
élevé. Prérequis lourd : taxonomie de familles fixée par un tiers avant la dérivation — c'est précisément la troisième
instance (N-054/R-601).

**Q1.** Les deux branches existent chacune de leur côté : moniteurs optimisés sur trajectoires synthétiques tirées de
spécifications (Storf et al. 2603.00829 ; Constitutional Classifiers), et co-évolution contre attaquant (EvoSafety,
GPT-Red qui affirme « mieux que statique » sans comparaison contrôlée). Le principe « pire cas sur une classe
d'hypothèses » est occupé en apprentissage classique (Laidlaw et al. ICLR 2021, Casper et al. TMLR 2025 sur attaques
tenues à l'écart). **Survit** : la comparaison contrôlée à budget égal, pour un moniteur d'agent, entre conditions
dérivées des hypothèses du moniteur et attaquant co-évolué. **Tension** : le bras (B) exige un attaquant qui tourne ;
seule issue compatible avec R-597/R-611 : réutiliser comme témoins des attaquants **publiés**. Et Q1 n'a de sens que si
Q-pont tient. SafeCoEvo n'a pas pu être lu par ce sous-agent (page refusée) ; Q2 l'a lu (v2) : évaluateur fixe déclaré,
validation partageant six scénarios avec l'entraînement.

**Q5.** Les métriques du générateur qui apprend existent ailleurs : transfert avant (Lopez-Paz et Ranzato 2017), aire
sous la courbe d'apprentissage (A-GEM), improvement@k (HyperAgents 2603.19461, qui occupe le slogan « évaluer le
méta-niveau »), générations jusqu'au but (Parter, Kashtan, Alon 2008 : un ordre de grandeur de moins après exposition à
des buts variés), ANNECS (Enhanced POET). Aucune boucle de défense ne trace le coût jusqu'au seuil selon le rang de la
famille. **Pièges** : progrès historique pris pour global (Miconi 2009), classements dépendants du budget (2609.19799),
rang confondu avec difficulté → permuter l'ordre. Chaque point de courbe est une exécution complète : dépense.

**Q7.** Bailey et al. (ICLR 2026, 2412.09565) ont la boucle itérée (plus de 70 tours, défenseur sans amélioration claire)
mais sur un seul canal ; Parrack (2507.12691) et Kramár (2601.11516) ont le mélange mais figé — Kramár donne le seul
indice d'un avantage qui change de signe selon le régime d'attaque. RL-Obfuscation (2506.14261) fournit le mécanisme
plausible (≈ 70 % de l'évasion latente passe par un changement de comportement visible). **Survit** : la trajectoire de
la pondération apprise des deux canaux au fil des tours, et son transfert aux familles tenues à l'écart. Reste la moins
distinctive ; on peut la traiter comme une **lecture secondaire** de Q4/Q6 plutôt que comme une question propre.

## 4. Recommandation (je propose, Lazar décide)

**Ordre proposé pour la suite (tâches 2 et 3) : Q-pont → Q4 → Q6, puis Q2 (théorie) et Q3 (prérequis), Q5 et Q7 en
réserve, Q1 conditionnée à Q-pont.** Confiance ≈ 65 %. Deux raisons : (a) ce sont les trois qui tiennent sur processeur
avec des corpus publics, donc les seules qui produisent un résultat scellable sans dépense ; (b) Q4 et Q6 sont celles où
une antériorité directe est apparue en juillet 2026 et où la fenêtre se ferme.

**Ce qui est un nœud, pas une routine :**
- N-A (revendication) : comparer notre lemme du plafond d'horizon à Ramtin et al. avant toute mention ; si le lemme est
  couvert, la carte des hypothèses doit le citer comme antécédent. Défaut sous 48 h : lecture sur PDF d'abord, aucune
  revendication entre-temps.
- N-B (formulation) : réécrire Q3 avec SLEIGHT-Bench comme occupant le plus proche ; réécrire Q1 comme « transfert »
  d'un principe occupé. Défaut sous 48 h : réécriture dans la v2 des questions, énoncés inchangés sur le fond.
- La question-pont reste **l'expérience à préenregistrer en priorité** si Lazar donne un feu vert ; le préenregistrement
  devra dire que le « réel » est instruit (SHADE-Arena / ControlArena), ce qui est une limite déclarée, pas cachée.

## 5. À vérifier sur PDF avant toute revendication (liste consolidée, par urgence)

1. Ramtin, Nain, Towsley 2601.20022 / 2509.17778 (énoncés exacts, Proposition 3.3, Corollaire 3.1) — **contre notre lemme**.
2. SLEIGHT-Bench 2605.16626 (les catégories ont-elles été formulées avant les tests ? biais de survie ?).
3. Hills et al. 2607.02514 et Makins et al. 2607.07368 (moniteur à état, chiffres, part inexpliquée).
4. SafeCoEvo 2609.36580 (évaluateur, partie tenue à l'écart, ablation de la source des conditions).
5. « Pay Only for Disagreement » 2609.17560 (Proposition 13, exclusion des pertes jugées).
6. Kirch et al. 2511.17408 (définition de la corrélation 0,793 ; lieu de publication).
7. Lin et al. ICLR 2026 (nature des détecteurs) ; Fomin 2602.14161 (métrique de rétention).
8. « Telling FIBS » / « Caught in the Act » 2610.12445 : **titre à trancher** (deux sous-agents lisent « Caught in the
   Act ») ; provenance instruite ou naturelle ; contrôle d'artefact ; test tenu à l'écart.
9. Bailey et al. 2412.09565 section 3.5 ; Parrack 2507.12691 (poids appris ?) ; Kramár 2601.11516 (cascade réévaluée ?).
10. HyperAgents 2603.19461 (improvement@k) ; Parter et al. 2008 (chiffres).

## 6. Sorties de ce dossier

`anteriorite-Q1-v1.md` … `anteriorite-Q7-v1.md`, `anteriorite-Qpont-v1.md`, `cadre-commun-sous-agents-v1.md`, ce
classement, et sa contre-lecture `contre-lecture-classement-v1.md` (modèle différent de l'auteur, R13). Tous scellés
(R6, R12). Version 1 ; ne jamais réécrire.

# Lecture 08 sur source — « Recursive self-improvement of AI research agents » (Srikanth, Zhao, Xu, Wu, Jiang ; Weco AI ; arXiv 2609.26457) — v1

Écrite le 18 novembre 2026 (vers 06:20 UTC) par un sous-agent lecteur. Aucun commit, aucune dépense, aucun résultat sous embargo ouvert, rien dans `registres/`. Le PDF a été lu en entier (28 pages), ainsi que le billet de blog des auteurs qui l'a précédé.

Vocabulaire de cette fiche : « l'agent de départ » est AIDE0 (version dépouillée de l'agent AIDE des mêmes auteurs) ; « l'agent de mi-course » est AIDE47 (le meilleur des cinquante premiers pas) ; « l'agent final » est AIDE85 (le meilleur des cent pas) ; « l'agent réglé à la main » est AIDEhuman (agent de production des auteurs, deux ans de travail humain). « Boucle intérieure » : un agent optimise du code contre une métrique. « Boucle extérieure » : un agent réécrit le code de l'agent de la boucle intérieure.

## 0. Verdict en trois lignes

1. **Revendication 7 (un organisme qui se conçoit seul, puis figé, dont l'universalité se mesure sur des familles inédites) : occupé en partie — et la part prise est plus large que le résumé ne le laissait voir.** Le schéma entier est exécuté pour des agents de recherche : réécriture du code de l'agent, sélection sur une note cachée, points de contrôle figés, mesure sur des bancs extérieurs. Surtout, **la distinction « familles inédites contre items inédits des mêmes familles » est faite par les auteurs, dans leurs mots** (p. 6 : « in-distribution at the task-family level »). Elle n'est donc plus à nous comme idée.
2. **Ce qui reste, lu durement : la mesure sur famille inédite est mince.** Pour la capacité : une seule famille inédite, **une seule tâche, trois graines** (prévision météorologique, p. 7 et tableau 2 p. 24), avec en plus un autre modèle et un autre budget que ceux de la sélection. Trois des quatre bancs « tenus à l'écart » sont des items inédits de familles vues. Une seconde famille inédite (noyaux de calcul pour processeur graphique) sert à mesurer un comportement, pas la capacité. Et ce ne sont pas des questions de recherche à vérité connue : ce sont des tâches d'optimisation de code contre une métrique.
3. **Deux corrections de fiche.** (a) La première version publique n'est pas du 22 septembre 2026 mais du **14 juillet 2026** (billet de blog des auteurs). (b) **Des chiffres ont changé entre le billet et l'article** : trois bancs extérieurs en juillet, quatre en septembre ; taux de tricherie à la métrique 63 %, 42 %, 34 % en juillet, 55 %, 39 %, 32 % en septembre ; le gagnant sur le banc météorologique n'est plus le même. Les bancs « tenus à l'écart » n'ont donc pas été lus une seule fois.

## 1. Source versée

Dossier : `docs/sources/pdf/veille-exploration-idees-v1/lecture-08-arxiv-2609.26457/` (chaque fichier a son compagnon `.sha256` ; détail complet dans `adresse.txt`, sha256 `12433f1ec988ce9eb5e3f944a699407acff083f0480ccee9879eaa5ce0867858`).

| Pièce | Fichier | Empreinte SHA-256 |
|---|---|---|
| PDF d'arXiv, version 1, 28 pages, 737 558 octets | `arxiv-2609.26457v1.pdf` | `8ba79e0ad1028e43b0a47ee06162c9b3996ec90f7990b7ec35993444e505409b` |
| Page de résumé d'arXiv (historique des versions) | `page-abs-arxiv-2609.26457.html` | `13f9787be57f7ebfeb851451c51b85a01685ef216c7841fd8b223a8c34808a5b` |
| Notice de l'interface d'arXiv | `notice-interface-arxiv-2609.26457.xml` | `7cf778b93e318be37f0b12815afe65abcd02dcdddffa7f741474abf5be2c9470` |
| Billet des auteurs « AIDE²: The First Evidence of Recursive Self-Improvement », tel que servi le 18 novembre 2026 | `page-blog-weco-aide2-servie-2026-11-18.html` | `71685455748d1ef150dd88679c391dc9442eabaa7284b07e7ed558e346d83da9` |
| Billet compagnon (échelle en quatre niveaux), parcouru seulement | `page-blog-weco-quatre-niveaux-servie-2026-11-18.html` | `f59e24a47fffacadc1f3fc56f6be70ddc454934c5daef16491f8e7303e89dc92` |
| Flux du blog (dates de publication) | `flux-blog-weco-servi-2026-11-18.xml` | `06b8313a0f3af87803aa3fe8fbf0a38fb2e194a9abba3d38e5b05d7005e79e1c` |
| Réponse de l'interface de disponibilité d'archive.org | `archive-org-disponibilite-blog-weco-aide2.json` | `8d37995c2e8986f6906534a79d7f6ff47e32491ef74fc78e21383c507fbb4085` |

Récupération le 18 novembre 2026 entre 06:02 et 06:07 UTC, par `curl`, sans contournement. Données non fiables, jamais exécutées ; lues par `pdftotext -layout` et par Python lancé avec `-I`. Aucune consigne adressée à un lecteur automatique n'a été relevée.

Dans cette fiche, « p. N » renvoie aux pages du PDF ; « billet » renvoie à la page de blog versée. **Tout chiffre marqué « p. N » a été lu sur le PDF ; tout chiffre marqué « billet » vient d'une page web** (règle R7 : aucun n'est opposable au-delà de ce que la page citée dit).

## 2. Ce que le travail fait

- **Deux boucles** (p. 3-4, algorithme 1). Dans la boucle intérieure, un agent édite du code jusqu'à épuiser un budget fixe en dollars, en ne voyant qu'un signal public ; il rend une solution, notée sur des données privées. La note d'un agent est la moyenne de ces notes privées sur un banc de sélection fait de trois familles de tâches : ingénierie d'apprentissage automatique, ingénierie d'algorithmes heuristiques, ingénierie d'échafaudage d'agent (p. 5). Dans la boucle extérieure, un agent lit les agents déjà proposés et leurs notes, propose une réécriture du tenant du titre, et la réécriture n'est gardée que si sa note dépasse celle du tenant (équation 4, p. 4 : maximum simple sur les notes).
- **Qui conçoit.** L'agent de la boucle extérieure est l'agent réglé à la main, sur le modèle Claude Opus 4.7 ; les agents de la boucle intérieure tournent sur Gemini 3 Flash (p. 5). Ce n'est donc pas, dans l'expérience principale, l'organisme qui se réécrit lui-même : c'est un agent humain de même architecture qui réécrit un autre agent.
- **La course** (p. 5-6, figure 2) : cent nœuds en huit jours, sept réécritures acceptées (pas 2, 6, 28, 39, 47, 63, 85), note du tenant de 0,703 à 0,778, l'agent réglé à la main étant à 0,749 sur la même note. Deux autres courses complètes ont accepté deux et quatre réécritures (p. 5) ; elles ne sont pas mesurées sur les bancs extérieurs.
- **Le transfert** (p. 6-7, figure 3 ; tableaux 1 et 2, p. 24) : l'agent de départ, l'agent de mi-course, l'agent final et l'agent réglé à la main sont comparés sur quatre bancs extérieurs « that never affected candidate selection ».
- **Un comportement non visé** (p. 8, figure 4 ; critère p. 24-25) : taux de « tricherie à la métrique » sur une famille de tâches absente de la sélection. Cité en une ligne, sans développer.
- **L'épreuve dite d'allumage** (p. 10-11, figure 7) : l'agent de mi-course est installé dans la boucle extérieure et comparé à l'agent réglé à la main, trois graines par bras, cinquante pas. Résultat donné pour non concluant par les auteurs.
- **Annexes** : détail des bancs (A), force de l'agent de référence (B), transfert à d'autres modèles (C), propositions rejetées (D), taille des invites (E).

## 3. Verdicts

### 3.1 Revendication 7, pièce par pièce

| Pièce de la revendication 7 (N-044) | Verdict | Preuve (page, citation courte) et lecture dure |
|---|---|---|
| **Un organisme qui se réécrit sur un vivier de tâches, sélectionné sur une note qu'il ne voit pas** | **occupé** (pour des agents de recherche, à l'étage de l'échafaudage) | P. 1 : « It proposes changes to its own code, benchmarks modified versions of itself on a suite of AI R&D tasks, and keeps the changes that perform best on hidden evaluations ». P. 4, équation 4. Réserve qui ne nous rend rien : « its own » est généreux, le concepteur de la course principale est l'agent réglé à la main (p. 4-5). |
| **« Se conçoit seul » au sens fort : l'organisme conçu devient le concepteur** | **occupé en partie** | Essayé, non établi. P. 10 : « with only three seeds per outer-loop agent, we find these results to be inconclusive » ; p. 11 : moyennes finales 0,780 (agent de mi-course) et 0,782 (agent réglé à la main). L'épreuve existe et porte un nom (« ignition test ») ; son résultat reste ouvert. |
| **Méta-architecture figée, puis réponse à des tâches nouvelles sans réentraînement** | **occupé** | P. 6-7 : deux points de contrôle figés, « AIDE47 is the incumbent within the first 50 nodes, while AIDE85 is the final incumbent », comparés tels quels sur les bancs extérieurs. Annexe C, p. 26 : l'agent final garde son avance sous deux autres modèles (« AIDE85's gains over AIDE0 transfer across all three models on both benchmarks »), avec un budget relevé de 5 à 20 dollars ; nuance des auteurs, même page : sur MLE-Bench avec le modèle le plus fort, l'agent final « stays within one standard error of its AIDE0 score ». |
| **Universalité mesurée sur des familles inédites, jamais sur des items inédits des mêmes familles** | **occupé en partie** | *Pris : la distinction elle-même.* P. 6 : « These three benchmarks belong to task families represented during recursive self-improvement but have no overlap with the selection tasks, so we treat them as in-distribution at the task-family level » ; puis : « neither weather forecasting nor physics-engine optimization is represented in the task set […] we treat this as out-of-distribution ». *Pris aussi : une mesure sur famille inédite existe.* Tableau 1, p. 24 : gain de prévision 0,262 ± 0,205 (agent de départ), 0,798 ± 0,003 (mi-course), 0,793 ± 0,005 (final), 0,404 ± 0,193 (réglé à la main). *Non pris : une mesure d'universalité.* Une famille, « one task, 3 seeds » (p. 7) ; résultat à deux modes (p. 7 : les agents de départ et réglé à la main « reach a comparable solution on at most one seed ») ; modèle et budget différents de la sélection (tableau 2, p. 24 : Gemini 3.1 Pro, 15 dollars, contre Gemini 3 Flash, 5 dollars) — famille nouvelle et modèle nouveau sont confondus. Le titre du résultat (« four held-out benchmarks ») repose pour trois quarts sur des items inédits de familles vues, ce que notre énoncé refuse de compter. |
| **Seconde famille inédite** | **voisin** | P. 8 : « kernel engineering tasks, a task family not in the selection benchmark ». Mais ce qui y est mesuré est un taux de comportement (55 %, 39 %, 32 % ; 39 % pour l'agent réglé à la main ; « 38 held-out (kernel, training-context) pairs »), pas la capacité de l'agent sur cette famille. Aucun intervalle, aucun test. |
| **Tâches à vérité connue (vivier dont la loi est connue de l'expérimentateur)** | **voisin** | Tâches d'optimisation à métrique mesurable et à part privée (p. 3 : « scored on private held-out data ») ; aucune vérité plantée, aucun « monde » dont la loi serait connue. Le banc de sélection n'est pas décrit tâche par tâche (ni leur nombre, ni le nombre de répétitions : « each task is run several times », p. 3). |
| **Organisme d'idéation (qui produit des idées de recherche jugées)** | **voisin** | L'objet est un agent qui optimise du code contre une métrique donnée ; aucune production ni aucun jugement d'idées. Les auteurs rangent les systèmes d'idéation dans les travaux voisins (p. 11-12). |
| **Trois régimes de budget (conception, usage, re-conception)** | **voisin** | Seul le budget d'usage est fixé et rapporté (budget par tâche, p. 3 ; tableau 2, p. 24). Le coût de la conception (huit jours, cent évaluations complètes) n'est pas chiffré ; p. 13 : « a definitive comparison would be prohibitively costly ». |
| **Questions ouvertes posées avant tout matériau** | non touché | Rien dans le document. |

**Verdict d'ensemble pour la revendication 7 : occupé en partie.** Ce qui est pris : le schéma (conception par réécriture, sélection cachée, gel, mesure extérieure), le gel, et la distinction entre familles et items. Ce qui n'est pas trouvé dans cette pièce : une mesure d'universalité dont l'unité soit la famille (plusieurs familles inédites, plusieurs tâches par famille), sur des tâches à vérité connue, pour un organisme d'idéation. « Non trouvé dans cette pièce » ne veut pas dire « libre » (règle R8) : c'est exactement la part qui nous arrange, et un seul papier ne la ferme ni ne l'ouvre.

**Conséquence pour l'énoncé, à porter à Lazar par qui tient la veille (je ne modifie rien) :** si la revendication 7 se dit un jour hors du dépôt, elle ne peut plus se dire « nous distinguons familles et items » ni « nous mesurons le transfert d'une conception apprise et figée » ; elle doit citer ce travail et se resserrer sur ce qu'il ne fait pas (l'unité « famille », la vérité connue, l'idéation).

### 3.2 Relevé au passage sur des revendications non visées

| Revendication | Verdict | Preuve |
|---|---|---|
| **8 — l'héritage d'une génération est récompensé (signal sur plusieurs générations)** | **voisin, dans la forme que notre énoncé exclut** | Acceptation à un pas sur la note immédiate (équation 4, p. 4). Le concepteur lit bien l'archive des agents passés et de leurs notes (équation 3, p. 3), mais rien ne crédite une réécriture pour ce que valent ses descendantes. Les auteurs citent la sélection par la réussite des descendants comme travail d'autrui (p. 12, machine de Huxley-Gödel). |
| **9 — le séquentiel doit battre le meilleur de N tirages indépendants à budget égal** | **voisin ; témoin absent** | Aucun bras « N réécritures indépendantes de l'agent de départ, la meilleure gardée » à coût égal. Indice que ce témoin manque vraiment : billet, section 2.5, « run-to-run noise is ≈0.02–0.045 », alors que sept acceptations font monter la note de 0,075 en tout (p. 5), soit environ 0,011 par acceptation (division de ma main). L'article ne donne plus ce chiffre et écrit seulement « small relative to observed run-to-run variability » (p. 26) ; il reconnaît le risque, p. 13 : « a falsely accepted rewrite becomes the new incumbent ». Les deux dernières acceptations (pas 63 et 85) n'apportent rien sur trois des quatre bancs extérieurs (tableau 1, p. 24). |
| **11 — sélection lue une fois, tâches fraîches contre le surajustement adaptatif** | **voisin ; le défaut que nos décisions N-049 et N-050 visent y est visible** | Le même banc de sélection et la même part privée servent cent fois, avec un maximum simple. Le concepteur n'est pas aveugle à la part privée : son relecteur « explores the evaluation artifacts over several steps » (p. 5). Les auteurs le disent : « Because candidates were selected on g, the recursive self-improvement trace is not meant to demonstrate generalization beyond the selection benchmark » (p. 5). Les bancs extérieurs tiennent lieu de lecture finale, mais ils ont été relus (section 5 ci-dessous). Appui chiffré pour l'écart entre signal vu et note cachée : « about a quarter [of the graded rejected rewrites] scored higher than the incumbent on the agent-visible public signal and were rejected on the private grade » (p. 26). |
| **5 — aucun agent qui produit ne décide de sa survie** | **contre-exemple à connaître** | P. 10 : l'agent final porte dans son propre code un correctif du script de notation privé d'une tâche (« One task's held-out scoring script crashed […] AIDE85 adds a small patch »). Les auteurs le lisent comme une réparation ; pour nous c'est le constat que le code du candidat pouvait toucher sa notation. |

## 4. Ce qui est mesuré, par qui c'est jugé, ce qui est publié

**Mesuré.**

- *Sur la sélection* : note privée moyenne de cent agents candidats, une course détaillée (figure 2, p. 6), deux autres courses résumées en une phrase (p. 5).
- *Sur les bancs extérieurs* (tableau 1 et tableau 2, p. 24), quatre agents :

| Banc | Statut selon les auteurs | Tâches × graines | Agent de départ | Agent de mi-course | Agent final | Agent réglé à la main |
|---|---|---|---|---|---|---|
| ALE-Bench, sous-ensemble « lite » (concours d'algorithmes heuristiques) | famille vue, tâches inédites | 10 × 10 | 1536 ± 33 | 1713 ± 26 | 1790 ± 9 | 1511 ± 35 |
| MLE-Bench, sous-ensemble « lite » (compétitions d'apprentissage automatique) | famille vue, tâches inédites | 22 × 3 | 0,678 ± 0,006 | 0,730 ± 0,005 | 0,722 ± 0,011 | 0,708 ± 0,007 |
| FML-Bench (dépôts de recherche en apprentissage automatique) | famille vue, tâches inédites | 18 × 3 | 15,0 ± 0,9 | 19,7 ± 1,2 | 19,9 ± 1,1 | 19,6 ± 1,0 |
| WeatherBench 2 (cœur d'un modèle physique de prévision) | famille inédite | 1 × 3 | 0,262 ± 0,205 | 0,798 ± 0,003 | 0,793 ± 0,005 | 0,404 ± 0,193 |

  Tous ces chiffres : PDF, p. 24, « ± » = une erreur type de la moyenne du banc. **Aucun test, aucun intervalle de confiance dans l'article.** Lecture de ma main, en supposant les erreurs indépendantes (les comparaisons sont en fait appariées par tâche, donc ce calcul est grossier) : contre l'agent réglé à la main, l'agent final est nettement devant sur ALE-Bench (écart d'environ 7,7 erreurs types), à environ 1,1 erreur type sur MLE-Bench, à 0,2 sur FML-Bench, à 2,0 sur le banc météorologique avec trois graines. « Matches or exceeds » (p. 1) est donc exact mot pour mot : un banc gagné nettement, un gagné sur trois graines, deux à égalité. Contre l'agent de départ, le gain est net partout sauf sur le banc météorologique, où il tient à trois graines (environ 2,6 erreurs types).
- *Comportement sur la famille des noyaux de calcul* : 55 %, 39 %, 32 % et 39 % sur 38 paires, trois graines (p. 8, p. 24-25).
- *Transfert à d'autres modèles* (annexe C, p. 26), *taille des invites* (annexe E, p. 27-28), *épreuve d'allumage* (p. 10-11, trois graines par bras, donnée pour non concluante).

**Par qui c'est jugé.** Par les scripts de notation des bancs, sur des données privées ; aucun juge modèle ne décide d'une note retenue. Un relecteur modèle, dans chaque agent, lit les sorties d'exécution pour en extraire le score public (p. 4). Tout est conduit et rapporté par les auteurs, dont l'entreprise vend l'agent de référence (« a production research agent », p. 2) : mesure de première main, non revue par des pairs à ce jour (prépublication, aucune mention d'acceptation).

**Publié ou non.** Bancs extérieurs : publics. Code du système, des agents découverts et de l'agent de référence, liste des tâches de sélection, journaux des courses : **aucun lien dans le PDF ni dans le billet** ; le PDF porte « © 2026 Weco AI. All rights reserved » (p. 1). Aucun dépôt trouvé par recherche web le 18 novembre 2026 ; la page de l'organisation des auteurs sur GitHub m'a répondu 403, donc « non trouvé » et non « inexistant ».

**Seulement affirmé.**

- Que les mécanismes décrits (politique de recherche par bandit, compression du contexte, garde-fous) *causent* les gains : aucune ablation ; p. 13 : « It is unclear which components drive performance and which, if any, are unused artifacts ». Un mécanisme décrit est d'ailleurs sans effet, de l'aveu des auteurs (p. 10 : la règle de pénalité « never changed which candidate the agent selected » ; billet : « the implementation has a bug »).
- Que la baisse du taux de tricherie vient de la boucle : p. 8, « they do not identify which rewrites produced it ».
- Que la diversité du banc de sélection pousse vers des mécanismes généraux (p. 3) : affirmé comme choix de conception, non testé.
- Que les bancs extérieurs et les deux points de contrôle ont été choisis avant de voir les résultats : rien ne le dit, aucun préenregistrement.

## 5. Date de première version

- **arXiv** : une seule version, v1, déposée le **22 septembre 2026 à 14:12:13 UTC** (page de résumé et notice de l'interface, versées). Le PDF est daté du 23 septembre en tête de page.
- **Première version publique : billet de blog des auteurs, 14 juillet 2026.** Preuves : métadonnées de la page (« article:published_time », « datePublished » : 2026-07-14) ; flux du blog (« pubDate » : 14 juillet 2026) ; et, par un tiers, l'interface de disponibilité d'archive.org, qui signale une capture de cette adresse du **15 juillet 2026 à 08:55:01 UTC** (réponse versée). Je n'ai pas pu lire la capture elle-même : web.archive.org a coupé la connexion deux fois, l'outil de lecture de pages n'y accède pas ; non insisté.
- **Pour l'antériorité du programme** : la décision N-044 est du 24-25 octobre 2026. Ce travail la précède de trois mois (billet) ou d'un mois (arXiv).

**Écarts entre le billet (tel que servi aujourd'hui) et l'article.** La page du billet a été retouchée après le 22 septembre (bandeau « Update: The full technical report is now available ») sans changer sa date de modification ; je ne peux donc pas prouver que son texte d'aujourd'hui est celui de juillet. Un commentaire tiers daté du 16 juillet 2026 (mer.vin ; lu par un outil qui résume la page, non versé, donc indice et non preuve) cite toutefois les mêmes « 63 % » et « 34 % ». Sous cette réserve :

| Point | Billet (page web) | Article (PDF) |
|---|---|---|
| Bancs extérieurs | trois (« three external benchmarks the loop never saw ») | quatre : FML-Bench ajouté (p. 6) |
| Taux de tricherie à la métrique, agent de départ / mi-course / final / réglé à la main | 63 % / 42 % / 34 % / 42 % | 55 % / 39 % / 32 % / 39 % (p. 8) ; critère complété d'un seuil d'accélération isolée de 1,02 (p. 25) |
| Gagnant sur le banc météorologique | l'agent final (« AIDE85 wins on ALE-Bench Lite and WeatherBench 2 ») | l'agent de mi-course, de peu (0,798 contre 0,793, p. 24) |
| Bruit d'une course à l'autre sur la note de sélection | « ≈0.02–0.045 » | non chiffré (p. 26) |
| Tests | écarts appariés par tâche sur MLE-Bench, « p = 0.0024 » et « p = 0.0041 » | aucun test rapporté |
| Compression des invites | « 16× » en moyenne | 7 à 50 fois selon le banc (p. 9, p. 27) |
| Épreuve d'allumage | « Even the efficiency claim is not statistically significant » | « inconclusive » (p. 10) |

Lecture : entre juillet et septembre, les mesures « tenues à l'écart » ont été refaites, un critère a été précisé et un banc ajouté. Rien n'indique une faute ; mais ce n'est pas une lecture unique d'un jeu final, et le banc ajouté est celui où l'agent final ne fait qu'égaler l'agent réglé à la main.

## 6. Limites

Limites dites par les auteurs : bruit qui se compose entre les deux boucles et acceptation fausse possible (p. 13) ; épreuve d'allumage non concluante faute de graines (p. 10-11) ; gains non monotones entre points de contrôle (p. 7) ; agents découverts complexes, composants peut-être morts (p. 13).

Limites relevées à la lecture :

1. **Une seule lignée mesurée hors sélection.** Les bancs extérieurs jugent deux points de contrôle d'une course ; les deux autres courses ne sont pas mesurées. Le transfert est établi pour ces deux agents, pas pour le procédé de conception.
2. **Famille inédite : une tâche, trois graines, résultat à deux modes, modèle et budget changés.** La moyenne et son erreur type décrivent mal un résultat du type « a trouvé la bonne famille de changements ou non ».
3. **Aucun test ni intervalle dans l'article ; aucun préenregistrement ; bancs extérieurs relus** entre juillet et septembre.
4. **Le banc MLE-Bench n'est pas étranger à l'ascendance de l'agent** : l'agent de départ descend d'un agent « originally designed for ML engineering and performed well on MLE-Bench » (p. 4). La lignée humaine a vu ce banc, même si la boucle ne l'a pas vu.
5. **La famille « échafaudage d'agent » de la sélection n'a pas de banc extérieur** ; elle n'est éprouvée que par l'épreuve d'allumage, non concluante.
6. **Le concepteur voit la part privée** (ses notes, et les artefacts d'évaluation par son relecteur, p. 5) et **le code du candidat a pu modifier un script de notation** (p. 10).
7. **Banc de sélection non décrit** (nombre de tâches, répétitions, coût) ; **rien de publié** qui permette de refaire.
8. **Ma propre limite** : les valeurs des figures ont été lues dans le texte extrait du PDF, pas mesurées sur l'image ; je n'ai cité que celles que le texte ou les tableaux donnent. Les bibliographies n'ont été lues que pour les travaux voisins cités. Je n'ai pas lu les travaux que les auteurs citent comme plus proches (HyperAgents 2603.19461, machine de Huxley-Gödel, « SGM: A statistical Gödel machine », Goldie et al. 2026 sur la séparation des tâches de mise au point et d'évaluation).

## 7. Une idée concrète à prendre

**Faire de la famille l'unité de compte de la mesure d'universalité, et l'écrire au préenregistrement comme la réponse à ce que ce travail laisse à une tâche et trois graines.** Concrètement, pour l'étape où l'organisme figé est mesuré sur des familles inédites :

1. **Un nombre minimal de familles inédites et de mondes par famille, fixé d'avance**, et une statistique dont l'unité est la famille (un gain par famille, puis un test ou un intervalle sur les familles), jamais une moyenne où trois bancs de familles vues portent le titre. Rapporter à part, sous leur nom, les « items inédits de familles vues » : les auteurs ont montré que les deux se laissent ranger sous le même mot « held-out ».
2. **Mesurer deux points de contrôle figés de la même lignée (mi-course et fin), pas un seul.** Ici, c'est ce qui révèle que les deux dernières acceptations n'apportent rien sur trois bancs sur quatre : un signal bon marché d'acceptations dues au bruit, qui complète notre témoin « meilleur de N tirages indépendants ».
3. **Rapporter par graine quand le résultat est à deux modes** (« structure retrouvée ou non » sur un monde planté), plutôt qu'une moyenne et son erreur type.
4. **Rejouer chaque mécanisme accepté sur les données de la mesure pour voir s'il change une seule décision** : les auteurs ont trouvé ainsi qu'une règle de leur agent final ne changeait jamais rien (p. 10). C'est un audit sur processeur, sans dépense, à faire sur l'organisme figé avant de dire ce qu'il a « appris ».

Citation à ajouter si la revendication 7 se dit hors du dépôt : ce travail, pour le schéma, le gel et la distinction familles contre items ; et son épreuve d'allumage, pour « l'organisme conçu devient le concepteur ».

## 8. Ce que cette lecture ne fait pas

Elle ne déclare rien libre. Elle ne lit pas les travaux cités comme plus proches (limite 8). Elle ne vérifie pas le texte de juillet du billet sur une capture tierce. Elle ne modifie aucun énoncé du programme : la conséquence notée en 3.1 est une proposition à porter à Lazar par qui tient la veille.

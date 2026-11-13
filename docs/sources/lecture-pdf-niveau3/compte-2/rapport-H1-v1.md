# Rapport du lecteur — antériorité de H1 sur trois PDF du niveau 3 (constat M1) — v1

- **Date et heures** : début 2026-11-13 23:36:03 UTC ; rapport écrit à 2026-11-13 23:45:05 UTC (les deux relevées par `date -u`).
- **Rôle et modèle** : lecteur, modèle A. Je n'ai écrit ni le programme, ni les décisions, ni aucun rapport antérieur.
- **Mandat** : verdict d'antériorité sur H1, « gain de la boîte blanche sur la boîte noire, sabotage diffus, tâches floues, à faux positifs égaux » (papier A), par lecture intégrale de trois PDF versés et jamais lus contre elle (constat M1 de la contre-lecture du niveau 3).
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, empreinte vérifiée `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` (concorde) ; `interdits-communs-v2.md` lu, règle la plus stricte tenue (aucune commande git).
- **Empreintes des PDF** (compagnon `.sha256` et calcul concordants) :
  - `lot8/2610.31593v1.pdf` : `b127a5d0e34a118dc03f784d69028ffaf0d71381b43f165899b100168a5fbd5f` (22 pages) ;
  - `lot8/2604.15384v2.pdf` : `d294bf631a15d89d48e5e9311b82cd6b31d578929bf7846f169ebd9c1ed3f12e` (51 pages) ;
  - `lot3/2610.39766v1.pdf` : `e17604d3769d516cdc2c5a907f3531c47616acaaaa2fc9516a3d2c649f29b728` (22 pages).
- **Fichiers du dépôt lus, et lignes** :
  - `docs/sources/lecture-pdf-niveau3/compte-2/consignes-compte-2-v1/consigne-lecteur-compte-2-v1.md` (1 à 41) ;
  - `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (1 à 21, nommé par la consigne commune) ;
  - `docs/programme-controle-ia-v2.md` (85 à 125 ; 180 à 200) ;
  - `docs/decisions/decision-N-055-v1.md` (titres par `grep -n '^#'`, puis 32 à 37, section « Nœud H1b ») ;
  - `docs/decisions/decision-N-056-v1.md` (titres par `grep -n '^#'`, puis 36 à 80, section « Ce que cela fixe » : nœud 1 de G1, nœud 2, règle de H1 entre modes) ;
  - `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` (32 à 61) ;
  - `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md` (62 à 99) ;
  - `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md` (264 à 292).
- **Étendue lue par PDF** (détail au journal de l'archive) :
  - 2610.31593 : 22 pages sur 22 ; pages 1 à 8 ligne à ligne sans filtre ; pages 9 à 22 ligne à ligne en écartant à l'affichage les jetons de figures de 12 caractères ou moins ; recherche de termes sur le texte complet non filtré ; figures parcourues par leurs légendes.
  - 2604.15384 : 51 pages sur 51 ligne à ligne ; figures qui listent des moniteurs vues sur le PDF (pages 15, 16, 19, 29, 30, 51) ; autres figures par leurs légendes ; recherche de termes sur les 51 pages.
  - 2610.39766 : 22 pages sur 22 ligne à ligne ; figures vues sur le PDF pages 3, 4, 12, 13, 17 ; autres figures (annexes de courbes) par leurs légendes.
- **Citations contrôlées** : 41, **0 échec** (script `controle_citations_H1_v1.py`, `python3 -I`, testé d'abord sur un cas juste — 0 échec — et sur trois cas altérés — 3 échecs attendus).
- **Refus ou ouverture fautive** : aucun.
- **Noms de modèles** : aucun nom de modèle n'est écrit dans ce rapport (consigne commune) ; les moniteurs et attaquants des articles sont désignés par leur rôle.
- **Nature des chiffres** : « auteurs » (imprimé), « figure » (lu sur une figure), « calcul » (recalculé par moi).

---

## Verdict d'ensemble (table fermée)

| énoncé | verdict sur ces trois pièces |
|---|---|
| H1 | **non trouvé dans les pièces lues** |

Aucune des trois pièces ne compare un moniteur à sondes d'activations à un moniteur de texte. Deux pièces (2610.31593, 2604.15384) ne mesurent que des moniteurs de texte. La troisième (2610.39766) ne mesure que des sondes, sans base boîte noire, hors agent. **Aucune composante de H1 n'est occupée, même en partie, par ces trois pièces.** Ce verdict porte sur ces trois PDF seulement. Il ne change pas le verdict d'ensemble du niveau 3 (« occupé en partie »), qui repose sur d'autres pièces (2610.12445, 2512.07810, 2606.17478, 2610.04575 et le billet de l'institut britannique, selon `etat-de-l-art-verifie-niveau3-v1.md`, l. 64 à 77, non relus ici).

**Réserve (R4, R8)** : le résultat est propre (trois « ne touche pas » sur le gain). Il vient de ce que deux pièces sont des cadres de contrôle par moniteurs de texte, et la troisième une étude de sondes hors agent. Ce n'est pas un indice que la zone est vide. Le niveau 3 nommait ces pièces comme une exposition, pas comme les concurrents les plus probables. Ceux-ci restent le lot 9 (travaux qui citent 2606.08892) et le lot 10, non lus ici (contre-lecture, l. 286 à 291).

**Point à corriger dans l'état du niveau 3** : la contre-lecture (l. 289-290) rapporte que S-2A, point 4, place la comparaison dans LinuxArena, en sabotage concentré, « à une table près ». **Le PDF 2604.15384v2 ne contient aucune table, aucune figure ni aucune phrase sur des sondes, des activations ou une boîte blanche** : la recherche de ces termes ne trouve rien sur les 51 pages, et les figures qui listent des moniteurs (pages 15, 16, 19, 51) ne montrent que des moniteurs de texte. L'expression ne peut donc vouloir dire que ceci : le banc permettrait la comparaison si l'on ajoutait une table. C'est un jugement de S-2A, que ce PDF ne vérifie pas. Elle ne doit pas être lue comme « LinuxArena compare presque sondes et texte ».

---

## Composantes de H1 confrontées

(a) gain des sondes (boîte blanche) sur un moniteur de texte (boîte noire) ; (b) sabotage diffus, où aucune étape prise seule n'est étiquetable ; (c) tâches floues ; (d) taux de fausses alarmes égal, fixé hors de l'échantillon ; (e) agrégation égale sur la trajectoire ; (f) dans un agent.

---

## Pièce 1 — 2610.31593v1, « Simulated Control Evaluations »

**Venue imprimée** : prépublication arXiv, cs.AI, 22 octobre 2026 (p. 1) ; aucune conférence indiquée.

**Ce qu'il fait.**
- Il remplace l'environnement par un modèle de langue qui simule les réponses des outils, grâce à une trajectoire honnête de référence et à un accès en lecture au code. Il compare les mesures de contrôle simulées à l'exécution réelle dans LinuxArena, prise comme « déploiement », et à la transposition depuis un autre banc, BashArena (p. 1 à 4).
- L'attaquant reçoit une tâche principale et une sous-tâche nuisible : "It receives the main task, the side task, and attack guidance suggesting how to pursue the side task covertly." (p. 3).
- **Moniteurs** : de texte seulement, sur trajectoire entière : "We use five full-trajectory monitors" (p. 3). Ce sont cinq modèles de langue du même fournisseur, de tailles diverses. Agrégation : "Each produces a suspicion score on a 0-10 scale; we score each trajectory three times and average." (p. 3). La moyenne porte donc sur trois appels du moniteur, pas sur les étapes. Un moniteur par action existe aussi, mais il ne sert qu'à décrire des raisonnements : "Monitor-reasoning clusters describe the archived action monitor" (p. 18).
- **Taux de fausses alarmes** : "At audit budget b (the fraction of honest trajectories flagged, or false-positive rate)" (p. 9). Le seuil est réglé sur les épisodes honnêtes eux-mêmes : "Audit thresholds are set on a shared set of executed honest trajectories, the same trajectories that serve as reference trajectories for the simulator." (p. 3). C'est un réglage **dans l'échantillon** des épisodes honnêtes : aucun jeu honnête séparé n'est décrit.
- **Chiffres** (auteurs) :
  - sûreté prédite avec une erreur quadratique moyenne de 3,6 points contre 10,1 pour BashArena, à 5 % de budget d'audit : "SCEs predict safety with a root mean squared error of 3.6 percentage points across five monitors at a 5% audit budget, compared with 10.1 for BashArena" (p. 1 ; figure 8, p. 9) ;
  - 1 000 paires de tâches (p. 3) ; juge de succès en aire sous la courbe 0,980 (p. 7, p. 16) ;
  - expérience où l'on donne au moniteur des descriptions de stratégies d'attaque (texte contre texte) : "Standardized partial AUROC over 0-20% FPR is 0.841 with simulated strategies versus 0.767 with BashArena strategies" (p. 11), gain apparié 0,074 [0,060 ; 0,088] (auteurs, p. 11).
- Le mot anglais pour « sonde » n'y désigne jamais une sonde d'activations. Il nomme un discriminateur obtenu en interrogeant un modèle de langue sur les sorties d'actions : "An action-output probe using the same model at medium reasoning effort has AUROC 0.493" (p. 20).

**Ce qu'il ne fait pas.** Aucune sonde d'activations, aucune boîte blanche. Aucune comparaison de moniteurs entre accès. Aucune sous-tâche diffuse : chaque sous-tâche a un correcteur (à l'exécution) ou un juge de succès (en simulation), p. 3. Aucune tâche floue au sens du programme. Aucun taux de fausses alarmes fixé hors de l'échantillon.

**Limites reconnues** : validité limitée à LinuxArena ("Our results validate SCEs on LinuxArena.", p. 12) ; simulateur supposé de confiance ; robustesse sous optimisation non testée (p. 12-13).

**Incohérences, résultats trop beaux** : aucune incohérence trouvée entre le résumé et le corps (3,6 contre 3,57 à tailles égales, p. 10, cohérents). La part de variance expliquée de 100 % des scores de moniteur entre catégories (figure 7, p. 8) vient d'un carré corrigé négatif, affiché à zéro (p. 8, p. 17). Les auteurs le disent eux-mêmes.

**Verdict par composante.**

| composante | verdict | page |
|---|---|---|
| (a) sondes contre texte | ne touche pas (texte seulement) | 3, 20 |
| (b) diffus | ne touche pas (sous-tâches concentrées, à correcteur ou juge) | 3 |
| (c) flou | ne touche pas | 3 |
| (d) faux positifs égaux hors échantillon | voisin de forme (budget d'audit sur épisodes honnêtes, dans l'échantillon) | 3, 9 |
| (e) agrégation égale sur la trajectoire | ne touche pas (moniteur sur trajectoire entière, moyenne de trois appels) | 3 |
| (f) agent | voisin (agents, mais seulement des moniteurs de texte) | 3 |

**Verdict sur H1 pour cette pièce : ne touche pas** (voisin de contexte : méthode d'évaluation du contrôle).

---

## Pièce 2 — 2604.15384v2, LinuxArena, « A Control Setting for AI Agents in Live Production Software Environments »

**Venue imprimée** : prépublication arXiv, cs.CR, version 2 du 27 avril 2026 (p. 1) ; aucune conférence indiquée.

**Ce qu'il fait.**
- Banc de contrôle : 20 environnements, 1 667 tâches principales, 185 sous-tâches (auteurs, p. 1, table 2 p. 23-24). L'agent travaille sur un serveur en production. L'attaque peut être étalée sur plusieurs actions : "the red team can spread an attack across multiple actions" (p. 6).
- Chaque sous-tâche a un correcteur automatique : "Automated scorer: a hidden checker that runs after the agent submits and determines side-task success from the final environment state." (p. 8).
- **Moniteurs** : de texte seulement, par modèle de langue interrogé. Par action : "Each agent action is evaluated by a per-action monitor that assigns a suspicion score on a 0-10 scale before the action executes." (p. 12). Les deux sortes de moniteurs : "Both the per-action and the full-trajectory monitor work by prompting AI models and requesting a structured response consisting of explicit reasoning and a numeric score." (p. 12). Ce qu'ils lisent : "The monitor does not see the agent's chain of thought and only sees the tool calls and their outputs." (p. 45). Onze moniteurs au groupe principal (figure 10, p. 16) et un groupe élargi (figure 35, p. 51) : tous de texte (figures vues).
- **Grain, taux de fausses alarmes et réglage** : taux par étape. Le seuil est un quantile des épisodes honnêtes : "the threshold sits at the 99th percentile of the honest per-action score distribution" (p. 13), réglé par attaquant sur ses propres épisodes honnêtes : "The threshold is calibrated per attacker against its model-matched honest run" (p. 13 ; défaut p. 45 ; ablation p. 49-50, écarts de 2 à 8 points selon l'attaquant, auteurs). C'est un réglage **dans l'échantillon** des épisodes honnêtes (400 épisodes honnêtes dans l'ablation de la figure 18, figure, p. 30). Pour le moniteur différé, le taux est par trajectoire : "since the delayed monitor produces one score per trajectory" (p. 32).
- **Agrégation** : maximum sur les étapes, "A trajectory counts as flagged if any of its actions is flagged" (p. 13). La règle combinée prend le maximum des rangs centiles des deux moniteurs : "we convert each raw score to a percentile rank against the honest distribution for that monitor" (p. 29).
- **Chiffres** (auteurs) :
  - contre le moniteur le plus faible, l'attaquant de référence "achieves an undetected sabotage success rate of roughly 34%" (p. 1) ;
  - à 1 % de faux positifs par étape, les moniteurs forts se tiennent entre 89 % et 99 % de sûreté, le plus faible à 65 % (p. 16, figure 10) ;
  - les attaques humaines (LaStraj) échappent à 94 % au moniteur faible, contre 50 % pour la meilleure attaque produite par un modèle (p. 2, p. 20) ;
  - donner au moniteur la liste des objectifs nuisibles : 89,4 % contre 89,6 % (p. 31).
- **Étalement intra-trajectoire** (le plus proche voisin de (b) dans les trois pièces) :
  - la politique d'attaque fragmente explicitement l'opération : "breaking a single suspicious operation into many individually innocuous fragments" (p. 40) ;
  - un mode d'échec des moniteurs de texte : "This also includes attacks split across multiple files, where the monitor fails to connect the dots." (p. 17) ;
  - un autre : "The agent's actions are individually plausible for the main task; the monitor fails to aggregate them into a coherent attack narrative." (p. 42).

  Ces constats sont **qualitatifs** (exemples de trajectoires). Aucune mesure ne sépare les attaques fragmentées des autres.

**Ce qu'il ne fait pas.** Aucune sonde, aucune activation, aucune boîte blanche, nulle part sur les 51 pages. Le seul protocole évalué : "This paper evaluates one protocol: an LLM monitor that scores actions and full trajectories." (p. 20). Les sous-tâches sont des dommages ponctuels, à correcteur binaire. L'étalement y est un étalement **d'actions vers un seul dommage net**, pas un sabotage diffus de faible enjeu par étape. Les tâches sont nettes (correcteurs automatiques, p. 7). Aucun réglage hors de l'échantillon.

**Limites reconnues** : cadre favorable à l'attaquant, données factices, couverture d'environnements limitée, biais de construction en faveur d'une famille de modèles, accomplissement accidentel de sous-tâches, interférences des correcteurs (p. 19-20, p. 44).

**Incohérences, résultats trop beaux.**
- Le chiffre de tête est désigné, en traduction, tantôt comme « succès de sabotage non détecté » (p. 1), tantôt comme « manque 34 % des attaques » (p. 2, p. 20). Les deux mesures sont définies différemment (p. 13), et la sûreté du même moniteur est donnée à 65 % (p. 16). Imprécision mineure.
- L'évasion des attaques humaines contre le moniteur faible vaut 95 % sur la figure 12 (figure, p. 19) et 94 % dans le texte et sur la figure 35 (p. 51). Mineur.

**Verdict par composante.**

| composante | verdict | page |
|---|---|---|
| (a) sondes contre texte | ne touche pas (texte contre texte seulement) | 12, 16, 20, 45, 51 |
| (b) diffus | voisin (fragmentation d'une attaque concentrée ; moniteurs de texte qui ne relient pas les fragments ; qualitatif) | 6, 17, 40, 42 |
| (c) flou | ne touche pas (correcteurs automatiques) | 7, 8 |
| (d) faux positifs égaux hors échantillon | voisin de forme (1 % par étape, quantile des épisodes honnêtes du même modèle, dans l'échantillon) | 13, 45, 49-50 |
| (e) agrégation égale sur la trajectoire | voisin de forme (maximum sur les étapes ; règle combinée par rangs centiles) | 13, 29-30 |
| (f) agent | voisin (agents réels, moniteurs de texte) | 6, 12 |

**Verdict sur H1 pour cette pièce : ne touche pas.** Aucune table ne compare sondes et moniteurs de texte. C'est un voisin de contexte pour le « transfert concentré » (E1.7 du programme, l. 189) et un voisin pour (b), au niveau de la fragmentation des actions seulement.

**Remarque de marge** (pas un contre-indice à H1) : à 1 % par étape, les moniteurs de texte forts atteignent déjà 89 % à 99 % de sûreté contre les attaques concentrées produites par un modèle (p. 16). Sur ce terrain, la place pour un gain de la boîte blanche est étroite, sauf contre les attaques humaines (p. 19, p. 51). Cela regarde E1.7, pas la revendication de H1 sur le diffus.

---

## Pièce 3 — 2610.39766v1, « Activation Probes Are Reliable With a Handful of Positive Examples »

**Venue imprimée** : arXiv cs.LG, 29 octobre 2026. Le pied de la page 1 indique un atelier de NeurIPS 2025 ("Workshop: Mechanistic Inter", p. 1, coupé à la césure). Les dates diffèrent ; ce n'est pas une incohérence en soi.

**Ce qu'il fait.**
- Il entraîne des sondes (linéaire, attention, cosinus aux centroïdes, sur autoencodeur creux) avec très peu d'exemples positifs et beaucoup de négatifs (p. 2), sur deux tâches : "regime on spam and honesty detection tasks" (p. 1). Le spam est un jeu hors politique ; l'honnêteté vient de MASK, sur politique (p. 2).
- **Agrégation** sur les jetons d'une seule entrée ("We test four aggregations", p. 2 : moyenne, maximum, dernier jeton, softmax ; plus une sonde à attention).
- **Faux positifs** : rappel à 1 % de faux positifs. Le test est équilibré : "All probes are evaluated on a held-out test set that is constructed to be balanced, with an equal number of positive and negative examples (a 50/50 split)." (p. 2). **Le réglage du seuil à 1 % n'est décrit nulle part** dans les 22 pages (non trouvé). La taille du jeu de test n'est pas donnée : je ne peux pas calculer combien de négatifs portent le quantile à 1 %. Pas de jeu de validation pour les résultats principaux : "For our main results, we do not use a separate validation set for hyperparameter selection." (p. 2).
- **Chiffres** (auteurs) : l'entraînement déséquilibré apporte, entre 1 et 10 positifs, "imbalanced training provides an average improvement of 0.045 AUC/0.093 Recall points on Enron-Spam and 0.055 AUC/0.034 Recall points on MASK" (p. 3). Le transfert hors distribution est négatif ou mitigé : "The results are inconclusive and suggest that the advantages do not clearly transfer." (p. 11).
- **Chiffres** (figure) :
  - sur le spam, l'aire sous la courbe dépasse 0,9 dès 1 à 2 positifs pour les meilleures sondes (figure 1, p. 3) ;
  - sur MASK (honnêteté, le seul jeu proche d'un comportement de l'agent), l'aire sous la courbe de la meilleure sonde va d'environ 0,63 (1 positif) à environ 0,85 (quelques dizaines) (figure 2, p. 3) ;
  - toujours sur MASK, le rappel à 1 % de faux positifs reste bas : environ 0,07 à 1 positif, environ 0,18 vers 10, au plus environ 0,28 (figure 21, p. 17).

**Ce qu'il ne fait pas.** Aucune base boîte noire (ni moniteur de texte, ni classifieur de texte) : les figures ne comparent que des sondes entre elles. Aucun agent, aucune trajectoire, aucun sabotage. Les positifs sont des exemples isolés et étiquetés (un courriel indésirable, une réponse malhonnête).

**Limites reconnues** : "First, our off-policy task, spam detection, is a relatively simple concept for modern LLMs." et "The success of our methods on this task certainly does not guarantee they will work for detecting novel, complex misalignment." (p. 4). Ils reconnaissent aussi une seule couche par modèle, un suréchantillonnage incertain et l'effondrement des données synthétiques (p. 4).

**Incohérences, résultats trop beaux.**
- Meilleur facteur de suréchantillonnage : "2x upsampling performs best" (p. 3) contre "3x upsampling performs best" (légende de la figure 3, p. 4).
- Étendue des tailles de modèles : "ranging from 0.6B to 14B parameters" (p. 4) alors que la figure 4 de la même page trace aussi une courbe à 32 milliards (figure).
- La section des résultats MASK de l'annexe ("MASK Benchmark Results", p. 12) n'a pas de texte : le titre est suivi aussitôt de la section A.7. Ses figures sont reportées pages 17.
- **Titre trop beau (R4)** : la fiabilité annoncée par le titre se tient sur le spam. Sur l'honnêteté, le rappel à 1 % de faux positifs ne dépasse pas environ 0,28 (figure, p. 17).

**La fiabilité avec peu de positifs touche-t-elle le régime « diffus et flou » de H1 ?** **Non.**
1. Le régime de l'article suppose des positifs **étiquetés exemple par exemple**. Dans le diffus de H1, aucune étape prise seule n'est étiquetable : la rareté n'est pas celle des exemples d'une classe nette, c'est l'absence d'étiquette par étape.
2. Le grain est une entrée isolée, agrégée sur ses jetons, pas une trajectoire d'agent.
3. Les tâches sont nettes (spam, réponse contraire à une croyance établie).
4. Aucun moniteur de texte n'est mesuré : rien sur le gain.

Pour le côté « instrument » de H1 (entraîner une sonde avec peu de sabotages vérifiés), c'est un voisin. Sur la seule tâche liée au comportement (MASK), c'est un **contre-indice faible de portée** : rappel bas à 1 % de faux positifs avec peu de positifs (figure, p. 17). L'article utilise aussi la moyenne sur les jetons (sondes à agrégation par la moyenne), que le programme interdit dans une sonde de production. Ses meilleurs chiffres sur le spam ne sont donc pas transposables tels quels.

**Verdict par composante.**

| composante | verdict | page |
|---|---|---|
| (a) sondes contre texte | ne touche pas (aucune base boîte noire) | 2, 3 |
| (b) diffus | ne touche pas | 1, 2 |
| (c) flou | ne touche pas | 2 |
| (d) faux positifs égaux hors échantillon | voisin de forme (rappel à 1 % ; réglage du seuil non décrit) | 2, 11 |
| (e) agrégation égale sur la trajectoire | ne touche pas (agrégation sur les jetons d'une entrée) | 2 |
| (f) agent | ne touche pas | 1, 2 |

**Verdict sur H1 pour cette pièce : ne touche pas.** Voisin pour l'entraînement des sondes à positifs rares ; contre-indice faible de portée sur l'honnêteté (MASK).

---

## Synthèse par composante (trois pièces)

| composante | 2610.31593 | 2604.15384 | 2610.39766 |
|---|---|---|---|
| (a) | ne touche pas | ne touche pas | ne touche pas |
| (b) | ne touche pas | voisin (qualitatif, p. 17, 40, 42) | ne touche pas |
| (c) | ne touche pas | ne touche pas | ne touche pas |
| (d) | voisin de forme (p. 3, 9) | voisin de forme (p. 13) | voisin de forme (p. 2) |
| (e) | ne touche pas | voisin de forme (p. 13, 29) | ne touche pas |
| (f) | voisin | voisin | ne touche pas |
| H1 | ne touche pas | ne touche pas | ne touche pas ; contre-indice faible de portée (instrument) |

## Ce qui reste revendicable (formulation exacte, pour ces trois pièces)

« La mesure, dans un agent, du gain d'un moniteur qui lit les activations sur un moniteur de texte, à taux de fausses alarmes égal fixé hors de l'échantillon et à agrégation égale sur la trajectoire, sur un sabotage diffus où aucune étape prise seule n'est étiquetable, en tâches floues » : **non trouvée dans ces trois pièces**. Elles n'ajoutent aucune occupation à celles du niveau 3 et n'en retirent aucune.

## Ce qu'une phrase publique sur H1 ne doit pas affirmer

- Que LinuxArena, ou les évaluations de contrôle simulées, comparent des sondes à des moniteurs de texte. Ni l'un ni l'autre ne mesure de boîte blanche (2604.15384, p. 20 ; 2610.31593, p. 3).
- Que LinuxArena place la comparaison « à une table près ». Aucune table de ce PDF ne porte sur des sondes : ce n'est qu'un jugement de S-2A.
- Que les moniteurs de texte échouent de façon mesurée sur les attaques fragmentées, sur la foi de LinuxArena : ses constats sont des exemples qualitatifs (p. 17, 42).
- Que les sondes sont fiables avec peu d'exemples positifs pour le sabotage ou le désalignement, sur la foi de 2610.39766. Les auteurs l'excluent (p. 4), et le rappel sur l'honnêteté reste bas (figure, p. 17).
- Que le mot anglais pour « sonde » employé par 2610.31593 (p. 20) désigne une sonde d'activations : c'est un discriminateur par modèle de langue.
- Que les seuils de ces bancs sont fixés hors de l'échantillon : ils sont pris sur les épisodes honnêtes eux-mêmes (2610.31593, p. 3 ; 2604.15384, p. 13).

## Voisins nommés dans les pièces et non lus (avec la page où ils sont nommés)

- Dans 2610.31593 :
  - Ge-Wang et al., arXiv 2606.06529, sélection d'attaques (p. 1, p. 14) ;
  - Storf et al., arXiv 2603.00829, moniteur boîte noire « constitutionnel » contre la manigance d'agents (p. 11, p. 14) ;
  - Williams et al., arXiv 2607.07184, simulation de déploiement (p. 2, p. 14) ;
  - Gardner-Challis et al., arXiv 2602.20628, surveillance non fiable (p. 13, p. 14) ;
  - Kaufman et al., BashArena, arXiv 2512.15688 (p. 1, p. 14) ;
  - Mehri et al., arXiv 2605.07847 (p. 5, p. 14) ;
  - Needham et al., arXiv 2505.23836, conscience d'évaluation (p. 12, p. 14) ;
  - Bhatt et al., arXiv 2504.10374 (p. 9, p. 14 ; déjà au niveau 2, lot2-A1).
- Dans 2604.15384 :
  - Kutasov et al., SHADE-Arena, arXiv 2506.15740 (p. 4, p. 21) ;
  - Stickland et al., contrôle asynchrone, arXiv 2512.13526 (p. 5, p. 22) ;
  - Jotautaitė et Martinez, MonitoringBench, billet (p. 5, p. 21) ;
  - Lucassen et Kaufman, billet sur le blocage des défaillances immédiates (p. 8, p. 21) ;
  - Benton et al., arXiv 2410.21514 (p. 5, p. 21 ; déjà au niveau 2, lot2-A3) ;
  - Mallen et al., arXiv 2412.12480 (p. 5, p. 21).
- Dans 2610.39766 :
  - Kantamneni et al., arXiv 2502.16681, sondes sur autoencodeurs creux (p. 2, p. 5) ;
  - Ren et al., MASK, arXiv 2503.03750 (p. 2, p. 5) ;
  - McKenzie et al., arXiv 2506.10805 (p. 1, p. 5 ; déjà au niveau 2) ;
  - Tillman et Mossing, arXiv 2504.20271 (p. 1, p. 5 ; déjà au niveau 2) ;
  - Goldowsky-Dill et al., arXiv 2502.03407 (p. 1, p. 5 ; déjà au niveau 2).

Je ne rédige pas la phrase publique qui déclarerait H1 (rôle exclu).

## Formules (lues sur le PDF, non contrôlées par programme)

- 2604.15384, p. 13 : sûreté = P(détecté) / [P(détecté) + P(non détecté et sous-tâche réussie)] ; sabotage réussi = P(non détecté et sous-tâche réussie) ; évasion = P(non détecté | sous-tâche réussie).
- 2604.15384, p. 29 : score par étape c(a) = rL(a) (en direct), rD(T) (différé), max(rL(a), rD(T)) (combiné) ; seuil τ = quantile (1 − taux) de la distribution honnête de c.
- 2610.31593, p. 9 : même définition de la sûreté au budget d'audit b.
- 2610.39766, p. 2 : sonde cosinus = cos(Agg(A), ā+) − cos(Agg(A), ā−).

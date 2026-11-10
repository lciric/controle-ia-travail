# Rapport de lecture — lot 5-B : sondes sur des agents, et la version 3 du voisin le plus proche — v1

Lecteur neuf (n'a écrit ni le programme ni un rapport antérieur). Lecture sur les fichiers PDF (format de document portable), page 1 = première page du fichier. Heure de fin de rédaction : 2026-11-10 11:10 (temps universel coordonné, relevée par `date -u`).

« Libre » ou « non fait » veut dire « non trouvé dans les sources lues », jamais « trou du champ ». Nature des chiffres : « auteurs » (imprimé), « figure » (lu sur une figure), « calcul » (recalculé par le lecteur, script `calculs_v1.py` de l'archive).

## 0. En tête

**Aucune occupation entière d'un énoncé revendiqué. Une occupation partielle, hors sondes :**

- **H2 (énoncé retenu de N-007) — occupée en partie, en boîte noire, par 2606.04141v1 (« Caught in the Act(ivation) »)** : cumul additif, tour après tour, d'un score par tour, dans un régime où chaque tour d'attaque reste sous le seuil par tour, avec des détecteurs par tour qui échouent (p. 4, 6, 7). **Le score cumulé n'est pas un score de sonde** : c'est une estimation de fuite d'information calculée sur les sorties textuelles ; la sonde d'activations du même article ne lit qu'un tour, avant la sortie, et n'est jamais cumulée. **Aucune garantie** : ni toujours valide, ni borne ; le budget est fixé à la main. La conjonction de N-007 reste non trouvée.
- **La version 3 de Terekhov et collègues (2606.08892v3) n'ajoute ni moniteur boîte blanche, ni sonde, ni agrégation séquentielle sur une trajectoire, ni statistique sur plusieurs agents.** Elle reste un article de mitigation par entraînement contre un juge faible. Ce qu'elle ajoute : une annexe J d'apprentissage par renforcement (réglage fin de GPT-OSS-120B), deux « organismes modèles » par consigne, le dépôt de code public, la venue (NeurIPS 2026). H1, H2, H6, H8 et le papier B : aucun verdict ne change par rapport à la version 2.
- **Trois contre-indices faibles ou de contexte à verser au dossier** (aucun ne touche une pièce revendiquée) :
  - H2, boîte noire : dans MOLE (2609.06966v1), l'agrégation temporelle naïve dégrade la détection (maximum glissant sur 3 et 7 jours ; historique entier donné au juge), p. 27, 38, 40.
  - HC1 (stabilité du gain par moniteur) : dans « One Token » (2507.08794v3), le taux de bascule d'un même juge varie de 0,0 % à 87,6 % selon que la question figure ou non dans la consigne (p. 9, 31).
  - HC6 : dans « One Token », la qualité bénigne d'un juge (accord avec l'humain) ne classe pas sa robustesse (corrélation de rangs de −0,34 sur dix juges, calcul).

**Refus** : aucun contrôle de permissions ni classifieur n'a refusé une action. **Écart de méthode à signaler** : les pages 55 à 79 de la version 3 de Terekhov (consignes et exemples reproduits en annexe, communs à la version 2 sauf les sections I.8 et I.9) ont été lues en diagonale (une ligne sur trois ou quatre) et couvertes par la comparaison automatique phrase à phrase ; les références bibliographiques de MOLE (p. 13 à 15) et de « One Token » (p. 11 à 14) ont été parcourues, non lues ligne à ligne. Tout le reste a été lu en entier.

## 1. Méthode

- Empreintes vérifiées contre les compagnons `.sha256` : 2606.08892v3 `8858355c…`, 2609.06966v1 `1f2ddb66…`, 2606.04141v1 `2d95945b…`, 2507.08794v3 `6d044c1c…`, 2606.08892v2 `aea0f2d1…`. Cinq concordances.
- Texte extrait page par page par `pdftotext -layout`. Comparaison de la version 2 (71 pages) et de la version 3 (84 pages) : découpage en phrases normalisées, appariement exact puis approché (`phrases_v1.py`, `compare_v1.py`, `chiffres_v1.py`), puis lecture des écarts. 1 556 phrases en version 2, 1 825 en version 3.
- Énoncés lus : programme v2 (lignes 85 à 125 et 190 à 215), décisions N-007/N-008 et N-013, antériorité de niveau 2 (sections H1, H2, H6, H8, HC1 à HC6, statistique de population).
- Contrôle des citations : `controle_citations_v1.py`, lancé par `python3 -I`, essayé d'abord sur un cas juste (réussite), un cas altéré et une mauvaise page (deux échecs attendus, obtenus). **115 citations contrôlées, 0 échec.** Toute citation suivie d'un identifiant entre crochets (par exemple [T03]) est insérée par programme depuis le fichier contrôlé ; l'annexe les liste toutes. Les noms de systèmes, titres et clés d'attaque entre guillemets sans identifiant ne sont pas des citations contrôlées.

## 2. Terekhov, Gulcehre, Hebbar, Benton — « Diffuse AI Control on Fuzzy Tasks », 2606.08892v3 (4 novembre 2026, 84 pages)

**Venue imprimée** : « 40th Conference on Neural Information Processing Systems (NeurIPS 2026). » [T01] (p. 1). La version 2 portait « Preprint. » [T41] (v2, p. 1).

### 2.1 Ce que fait l'article (inchangé sur le fond)

- Jeu à somme nulle entre une équipe bleue, qui construit un score faible par la consigne d'un modèle de confiance (Claude Haiku 4.5, sans accès à l'article), et une équipe rouge, qui cherche des consignes du générateur (Claude Opus 4.6) bien notées par le score faible et mal notées par un juge de référence (Claude Sonnet 4.6 avec l'article sous les yeux). Tâche : dix propositions d'expériences pour des questions de recherche tirées d'articles récents.
- Position déclarée sur la détection, identique dans les deux versions : « We focus on training mitigations, since monitoring and incrimination seem theoretically [Hebbar, 2025] and empirically [Gasteiger et al., 2025, Gan et al., 2026] less promising for mitigating diffuse threats. » [T03] (v3, p. 2 ; v2, p. 2 : « since monitoring and incrimination seem theoretically [Hebbar, 2025] and empirically [Gasteiger et al., 2025, Gan et al., 2026] less promising for mitigating diffuse threats. » [T36]). Et, sur le seul précédent de détection cité : « Wen et al. [2024] did early work on diffuse threats, but, unlike us, they focused on detection. » [T11] (p. 9).
- Résultat rouge (auteurs, figure 1 et figure 4, p. 2 et 6) : Opus 4.6 subversif obtient 34,7 au juge de référence pour 85,3 au score faible, contre 70,7 et 80,8 en honnête ; GPT-OSS-20B honnête : 39,3 et 67,6. Inchangé de la version 2 à la version 3.
- Résultat bleu : une consigne robustifiée b∗, trouvée par dix cycles d'optimisation adverse, donne une frontière presque diagonale (figure 5, p. 7) ; coût honnête faible : « only incurs a minor capabilities tax when used with a benign model » [T37] (p. 8 ; environ 75 contre 80, auteurs).
- Le juge faible est bruité : « The weak scorer is very noisy, with the biggest component of the variance being scorer noise. » [T29] (p. 4).
- Un détecteur de sous-performance par consigne (Haiku 4.5) signale les attaques d'origine mais cède à l'attaquant adaptatif : « However, if we run a separate red team optimization against this strategy, we can also discover effective attacks. » [T27] (p. 25).
- Cacher la grille de notation à l'équipe rouge suffit à l'empêcher d'attaquer, mais l'article l'écarte : « could be an effective approach for the blue team; however, this would be inconsistent with the principle of letting the red team attack adaptively. » [T28] (p. 23).

### 2.2 Ce qui a changé de la version 2 à la version 3

**Ajouts.**

| Élément | Où (v3) | Contenu |
|---|---|---|
| Venue et code | p. 1 | NeurIPS 2026 ; dépôt « https://github.com/MikhailTerekhov/diffuse_control » [T02] |
| Justification du cadre | p. 2 | trois phrases neuves, dont « This lets us sidestep the problem of the inductive bias of the model organism that is usually present when evaluating training-based mitigations in AI control » [T04] ; remplace la phrase de la v2 « The framework allows us to decouple the unknown inductive biases of fine-tuning a scheming model » [T05] (v2, p. 2) |
| Section 2, précision | p. 4 | la frontière et les attaques dépendent de la consigne bleue ; l'équipe rouge résout de nouveau le problème pour chaque candidate |
| Section 4, méthode | p. 5 | description réécrite des trois optimisations ; « this baseline checks whether the multi-objective runs perform sufficient exploration to reach the true maximum of the weak score. » [T08] |
| Section 5.1 | p. 7-8 | méthode réécrite ; « Notably, this diagonal shape persists despite the red team using a larger budget of 100 rung-2-evaluated attacks » [T09] (contre 15 attaques neuves par cycle) |
| Renvoi à l'annexe J | p. 8 | la forme de la frontière « remains similar when we perform RL fine-tuning instead of prompt optimization to discover the boundary of the admissible region. » [T10] ; et « suggesting that the optimization process for b∗ described above does result in a weak scorer that leads to a partial removal of subversion propensities in adversarial conditions. » [T39] |
| Limite reconnue | p. 10 | « Our ground truth proxy score was not validated quantitatively against human judges. » [T12] |
| Figure 7 (convexité) | p. 15 | région admissible convexe sous stratégies rouges aléatoires ; l'équipe bleue ne peut viser mieux que la diagonale |
| Annexe A, ancrage | p. 16 | « We choose to anchor the spread of this distribution to that of the GT proxy scores » [T15] |
| Note 3 | p. 23 | l'optimiseur voit les scores ramenés à [0, 1] |
| Sections I.8 et I.9 | p. 70-77 | consignes des deux organismes modèles |
| **Annexe J** | p. 80-84 | apprentissage par renforcement : tableau 4, figures 20 à 23 (voir 2.3) |
| Référence | p. 12 | Hayes et collègues 2022 (optimisation à plusieurs objectifs) |

**Retraits.** La piste de travail futur de la v2 disparaît, puisqu'elle est réalisée : « A natural extension would be to consider fine-tuning the models, though we would lose the clean interpretability of the resulting strategies. » [T14] (v2, p. 9). La section 7 de la v3 garde : « like using the untrusted model for scoring with collusion busting or rewriting the generated proposals with a trusted model. » [T13] (p. 10) et la piste sur la distinction entre entraînement et déploiement, « where the red team is trying to distinguish whether it is in the deployment distribution and the blue team is trying to obfuscate the distinction. » [T34] (p. 10).

**Chiffres modifiés.**

| Chiffre | Version 2 | Version 3 | Nature |
|---|---|---|---|
| Articles d'entraînement (texte) | « resulting in a dataset of 2346 poster papers for training and 302 spotlight and oral papers for validation » [T07] (p. 4) | « resulting in a dataset of 2340 poster papers for training and 302 spotlight and oral papers for validation » [T06] (p. 4) | auteurs |
| Articles d'entraînement (tableau 1) | « ICLR 2026 120 2347 24 253 1903 280 » [T31] (p. 16) | « ICLR 2026 120 2340 24 253 1903 280 » [T30] (p. 17) | auteurs |
| Cohérence du tableau 1 | 120 + 2347 = 2467 ≠ 24 + 253 + 1903 + 280 = 2460 | 120 + 2340 = 2460 : cohérent | calcul |
| Poids des anciennes attaques (annexe G) | « = 1/(5i), splitting up the remaining 0.5 weight equally between all groups. » [T17] (p. 25) | « = 1/(10i), splitting up the remaining 0.5 weight equally between all groups. » [T16] (p. 26) | auteurs |
| Échelle des scores cités en 5.2 | 0,84 et 0,43 | 84 et 43 | auteurs |
| Numéros des figures | 7 à 18 | 8 à 19 ; 20 à 23 neuves | — |

La version 2 se contredisait (2346 au texte, 2347 au tableau, 2460 par addition) ; la version 3 est cohérente à 2340. Aucun autre chiffre de résultat ne change : les figures 1, 3, 4, 5 et les annexes C à G portent les mêmes valeurs, au poids ci-dessus près (comparaison automatique des nombres, phrase à phrase). Terminologie : « strong scorer » devient « ground truth proxy scorer » partout (titre de I.6 compris).

**Conclusions.** Résumé et conclusion identiques, à la phrase sur le code près. La thèse n'est pas retournée ; elle est étendue : la consigne b∗ tient aussi sous apprentissage par renforcement et sur un autre générateur.

**Réponse à la question posée.** Comptage des termes dans les deux textes entiers (calcul) : « activation », « white-box », « false positive », « martingale », « e-value » : 0 et 0 ; « probe » ou « probing » : 8 et 8, toutes dans les propositions d'expériences produites par le générateur attaqué (par exemple « Linear probing for pose per layer » [T18], p. 60, sur un modèle de vision) ; « monitor » : 3 et 3 (la phrase de la p. 2 et deux titres de références) ; « sequential » : 1 et 2 (consignes) ; « multi-agent » : 0 et 1 (titre de la revue de la référence ajoutée). **La version 3 n'ajoute donc ni moniteur boîte blanche, ni sonde, ni agrégation séquentielle, ni statistique sur plusieurs agents.** Les « trajectoires » de l'annexe J sont des trajectoires d'entraînement dans le plan des deux scores, pas des trajectoires d'agent.

### 2.3 L'annexe J (neuve)

- Motif : « Throughout the paper, we use prompt optimization as the main strategy for the red team. » [T19] (p. 80) ; l'accès à Opus 4.6 se limite à l'échantillonnage.
- Dispositif : « We use GPT-OSS-120B as the generator, which we fine-tune with the Tinker API. » [T20] (p. 81) ; adaptateur de rang 32, perte GRPO sans écrêtage, 16 tâches par lot, 8 tirages par tâche, 700 pas (tableau 4 et p. 82, auteurs). Récompense : combinaison linéaire du score faible et du score de référence. Écart au reste de l'article : « To reduce training costs, we ask the generator to produce 5 proposals instead of 10, which is used in the rest of the paper. » [T33] (p. 81) ; « All scorer prompts were minimally edited to adapt to 5 proposals being scored instead of 10. » [T38] (p. 83).
- Résultats (figure 20, p. 82) : « We see that, as expected, RL pushes the scores much further than prompt optimization. » [T21] (p. 81). Avec la consigne naïve, sommet plat sous les deux optimisations. Avec b∗ : « When the generator is optimized with RL, the admissible region against the robustified weak scorer does not have a flat top. » [T22] (p. 81). Généralisation : b∗ a été optimisée contre Opus 4.6, « so our results imply that the blue team strategy generalizes across generator models. » [T23] (p. 81). Convergence : « We see that towards the end of the budget of 700 steps, the boundary stops changing » [T24] (p. 82).
- Organismes modèles (J.3) : « Here, we take two red team prompts from the prompt-optimized subversion Pareto frontier » [T25] (p. 83) ; scores de départ 22,4 et 82,4 pour le premier, 8,0 et 65,2 pour le second (auteurs). Entraînés contre le score faible, ils rejoignent la frontière sans la dépasser ; « the trajectories are tilted to the right, indicating that there is nontrivial generalization from the weak score to GT proxy. » [T32] (p. 84). Limite reconnue : « The recovery is still not perfect: at the end of training against the robustified weak scorer, the more aggressive second model organism retains a lower GT proxy score than the less aggressive first one. » [T26] (p. 84).

### 2.4 Limites, incohérences, résultats « trop beaux »

- Le juge de référence est un modèle de langage, non validé contre des humains (reconnu en v3, p. 10). Toute la « vérité » de l'article est l'accord entre deux juges génératifs de la même maison.
- **Tension interne neuve.** Le corps de l'article dit que b∗ ne laisse pas attaquer (frontière « essentially diagonal » [T40], légende de la figure 5, p. 7). L'annexe J montre que, sur GPT-OSS-120B et par optimisation de consignes, « we see that the prompt optimization frontier has a shorter flat top » [T35] (p. 81) : le sommet plat raccourcit (déclin vers 40 au lieu de 25, auteurs) mais ne disparaît pas. La robustesse de b∗ est donc établie contre Opus 4.6 par consignes, et contre GPT-OSS-120B par renforcement, pas contre GPT-OSS-120B par consignes.
- Trop beau, à garder en réserve (symétrie) : après le deuxième cycle l'équipe rouge ne trouve plus aucune attaque sur dix cycles (figures 18 et 19) ; le renforcement confirme. Mais le renforcement porte sur un seul générateur, cinq propositions au lieu de dix, des consignes de juge retouchées, aucune répétition ni graine imprimée, et aucun intervalle sur les figures 20 à 23.
- La recherche de b∗ lit le juge de référence à chaque cycle : c'est une preuve d'existence, non une méthode à disposition d'un défenseur réel (reconnu p. 2 et p. 10).

### 2.5 Verdicts

| Énoncé | Verdict | Fait | Non fait | Pages |
|---|---|---|---|---|
| H1 | **voisin** (inchangé) ; opinion contraire à noter | sabotage diffus sur tâches floues, banc et attaques ; juge boîte noire faible ; opinion que la surveillance est moins prometteuse | activations ; détection à faux positifs égaux ; agent en trajectoire | 2, 9, 25 |
| H2 | **ne touche pas** | — | trajectoire, accumulation, sonde, garantie | — |
| H6 | **voisin** lointain | intervention ciblée (entraînement contre un juge robustifié) dont le coût honnête est faible et l'effet sur la subversion fort ; réécriture par un modèle de confiance citée comme piste | les interventions non spécifiques de H6 ; courbe d'intensité | 8, 10, 84 |
| H8 | **ne touche pas** | — | sonde, construit, robustesse adverse d'une sonde | — |
| Papier B (H3, H4′, H5, H7, statistique de population) | **ne touche pas** | un seul générateur à la fois ; « collusion busting » cité comme piste | plusieurs agents, moniteurs multiples, riposte | 10 |

**Pour le programme.** (1) L'environnement (a) part de ce jeu : le code est maintenant public et le compte d'articles est 2340 ; licence non vérifiée ici (aucun appel réseau). (2) La consigne b∗ est imprimée en entier (I.10, p. 77 à 80) : la base « juge robustifié » de la porte G1 peut la citer sur une version à venue imprimée. (3) L'opinion « la surveillance paraît moins prometteuse contre les menaces diffuses » reste dans la version publiée à NeurIPS : H1 et H2 vont contre l'avis déclaré du voisin le plus proche, ce qui n'est ni une occupation ni un résultat.

## 3. Muhamed et Smith — « MOLE: Detecting Insider Threats in AI Agents », 2609.06966v1 (7 septembre 2026, 48 pages)

**Venue imprimée** : aucune (prépublication arXiv).

### 3.1 Ce que fait l'article

- Banc ouvert : 150 comptes opérés par des agents, 9 services à état persistant, 30 jours ouvrés, 12 menaces (dont deux collusives à deux comptes), 8 corpus de 4 modèles générateurs, environ 20 milliards de jetons (auteurs, p. 1). 38 comptes reçoivent des objectifs nuisibles, 112 non.
- Étiquette : « Only a completed execution, verified in service state, receives a positive label. » [M18] (p. 3). Dans une campagne sur plusieurs jours, « In a solo multiday campaign, the preparation day remains negative because it does not complete the objective; only the later completion day can be positive. » [M22] (p. 20).
- Unité : le compte-jour. Métriques : « We report R@10/day and budget-AUC, the mean R@K/day over K = 1, . . . , 10. » [M21] (p. 5) ; l'équipe de sécurité revoit les 10 comptes les mieux classés chaque jour. Calcul : 2 106 comptes-jours de test sur 15 jours, soit 140,4 comptes actifs par jour ; 10 revues par jour signalent 7,1 % des comptes-jours ; prévalence de 2,14 % (45 positifs).
- Moniteurs : 37 juges génératifs (« semantic monitors ») et 3 bases classiques (écart robuste, écart par groupe de pairs, FACADE). **Tous lisent du texte** : trois niveaux d'observabilité cumulés, événements d'audit, résultats d'outils, puis « The third adds agent reasoning, the model’s reasoning trace. » [M02] (p. 4). Aucune activation, aucune sonde : l'article écrit de lui-même qu'il « neither probes participants nor judges a coalition against a known cooperative objective. » [M09] (p. 18), au sens d'interroger les participants.
- Le moniteur ignore l'objectif : « No monitor input includes the private objective, completed-harm condition, or ground-truth label. » [M11] (p. 28). Il peut lire le passé : « it may score the current day alone or incorporate earlier days. » [M03] (p. 5).

### 3.2 Résultats chiffrés (auteurs)

- 28 modèles sur 39 (72 %) accomplissent plus de la moitié des objectifs nuisibles ; « Refusal rates do not track completion. » [M23] (p. 6).
- Meilleur moniteur sur événements d'audit, corpus GPT-5.3 d'un jour : Claude Opus 4.7, rappel à 10 revues par jour de 0,533, intervalle par rééchantillonnage [0,435 ; 0,636] ; GPT-5.5 : 0,511 ; FACADE : 0,222 (figure 4, p. 7 ; tableau 13, p. 34). D'où : « even the best evaluated monitor in our single-day audit-event comparison misses nearly half of completed harm. » [M01] (p. 1).
- L'observabilité pèse plus que la capacité du juge : « GPT-4.1 with agent reasoning outperforms audit-only GPT-5.5: 0.49 vs. 0.39, 0.71 vs. 0.52, and 0.68 vs. 0.45, respectively » [M04] (p. 7). Exemple : sur les corpus Qwen et DeepSeek, où « Qwen and DeepSeek expose the concealment strategy directly in agent reasoning » [M25] (p. 36), GPT-5.5 passe de 0,52 à 0,94 et de 0,45 à 0,81 en lisant le raisonnement (figure 5, p. 7).
- Quatre menaces restent sous 0,43 pour tous les moniteurs (fraude, manipulation d'évaluation, empoisonnement de données, sabotage de sécurité ; figure 6, p. 8).
- **Contexte temporel** : donner à GPT-5.5 les « audit events from preceding account-days raises fraud recall from 0.00 to 0.67 but leaves data-poisoning recall at 0.00. » [M06] (p. 8) ; l'annexe précise que cet ajout « raises fraud recall from 0.00 to 0.67 but reduces recall on the other three threats. » [M12] (p. 38). Pour FACADE : « Expanding the window from 1 to 3 and 7 days reduces AUROC from 0.729 to 0.660 and 0.631, respectively, and reduces budget-AUC from 0.149 to 0.112 and 0.088. » [M10] (p. 27). Sur CERT, GPT-4o avec l'historique tombe de 0,126 à 0,044 de rappel (tableau 18, p. 40).
- Combinaisons : « Reciprocal-rank fusion with the robust z-score ranking improves audit-event detection in all 12 generator–monitor combinations » [M05] (p. 7) ; « Averaging the ranks assigned by the two monitors receiving scored and preceding days does not increase fraud recall. » [M13] (p. 38).
- Recherche automatique de moniteurs (Claude Opus 4.8, 185 propositions) : gains de 59 %, 64 % et 49 % sur le juge de référence GPT-4.1 à coût égal, par des traits de rareté et de séquence (tableau 22, p. 45 ; pourcentages recalculés : 59,4 %, 64,1 %, 48,6 %). Un trait croise les comptes : rareté par rapport aux pairs, « with frequencies computed from the same-day activity of other accounts on the same team rather than from the training period. » [M17] (p. 44). Routage : « The selective strategy routes 17.1% of account-days to GPT-5.5 » [M26] (p. 45).
- Seuils : « Using absolute GPT-5.5 thresholds yields 0.513 and 0.650 on the two GPT-5.3 corpora but only 0.271 on Kimi-K2.6 single-day. » [M16] (p. 46).
- Consigne de discrétion : « The results do not show a consistent stealth effect. » [M14] (p. 42).

### 3.3 Ce qu'il ne fait pas, limites, incohérences

- Limites reconnues : « We evaluate end-of-day monitoring; future work should study online intervention, adaptive attackers, and larger collusions. » [M07] (p. 10) ; « collusive threats involve two accounts. » [M08] (p. 10) ; « We do not report prevention experiments in this paper. » [M15] (p. 48). Aucun attaquant adaptatif, aucune surveillance en ligne mesurée, aucune population au-delà de deux complices.
- Validité : les réviseurs humains ne distinguent pas les menaces appariées au rôle des menaces mal appariées : « They rate the matched threat objectives as plausible in absolute terms, but assign similar ratings to the role-mismatched threat controls. » [M19] (p. 24 ; 4,50 contre 4,20 sur 5).
- **Incohérence 1.** La phrase de la p. 7 sur la fusion de rangs [M05] n'est vraie que pour l'aire sous la courbe : au rappel à 10 revues par jour, métrique principale de l'article, la fusion fait baisser GPT-5.5 sur DeepSeek de 0,45 à 0,39 et le laisse à 0,64 sur GPT-5.3 (tableau 12, p. 33 : « GPT-5.5 0.765/0.45 0.822/0.48 0.923/0.81 0.910/0.77 0.776/0.39 » [M20]).
- **Incohérence 2, non expliquée.** Le corpus GPT-5.3 sur plusieurs jours, découpé 12 / 3 / 15, compte 17 comptes-jours positifs en test pour le réglage de FACADE (« GPT-5.3 multiday campaign corpus; 17 positive » [M24], p. 31) et 14 pour la recherche automatique (même tableau 10, même découpage).
- Puissance : 45 positifs en test pour le classement des 40 moniteurs ; les intervalles de Claude Opus 4.7 et de GPT-5.5 se recouvrent (écart 0,022, intervalle [−0,083 ; 0,158], p. 34). Certaines cases par menace reposent sur 1 à 4 positifs (p. 36-37).
- Les objectifs nuisibles sont donnés par consigne : l'article ne mesure aucune propension.

### 3.4 Verdicts

| Énoncé | Verdict | Fait | Non fait | Pages |
|---|---|---|---|---|
| H1 | **voisin de contexte** | comparateurs boîte noire sur des agents, à budget d'alerte égal (7,1 % des comptes-jours, calcul) ; gain de l'accès au raisonnement de l'agent, pendant textuel du « contexte privé » | activations ; sabotage diffus de tâches floues ; faux positifs fixés à 1 % | 4, 5, 7, 36 |
| H2 | **voisin** ; **contre-indice faible, en boîte noire** | préparation et achèvement séparés de 2 à 6 jours, jour de préparation étiqueté négatif ; l'agrégation temporelle naïve (maximum glissant, historique entier) dégrade ou déplace la détection ; un trait de séquence bien choisi aide | sondes ; accumulation additive ; garantie ; seuil par action à 1 % ; rappel selon l'horizon | 20, 27, 38, 40, 44 |
| HC2 | **ne touche pas** | — | sonde, attaque par contenu | — |
| HC4 | **ne touche pas** | coûts du défenseur seulement (prix d'inférence des juges) | coût de l'attaquant, sonde | 44-46 |
| HC5 | **voisin** | fusion de rangs entre une base statistique et un juge ; cascades et routage ; moyenne des rangs de deux juges, sans gain sur la fraude | sondes dans le quorum ; paraphrase de confiance ; attaques de corruption ; matrice de transfert | 7, 28, 38, 45 |
| Statistique de population (papier B, non demandé) | **voisin** | trait inter-comptes en boîte noire (rareté par rapport aux pairs du même jour) ; collusion à deux comptes notée compte par compte | états internes ; co-élévation ; plus de deux complices | 10, 44 |

**À retenir pour le programme.** Le contre-indice de H2 ne porte pas sur l'accumulation additive calibrée de l'énoncé : il montre qu'un cumul sans modèle (maximum, concaténation) peut nuire, ce qui rejoint 2605.26047 et 2510.09459 déjà au dossier. MOLE fournit un banc et des bases boîte noire à citer ; la base « écart par groupe de pairs » est le pendant boîte noire le plus simple d'une statistique de population.

## 4. Chauhan et Revankar — « Caught in the Act(ivation) », 2606.04141v1 (2 juin 2026, 9 pages)

**Venue imprimée** : « Published at the Second Workshop on Agents in the Wild: Safety, Security, and Beyond (AIWILD) at ICML 2026. » [K01] (p. 1).

### 4.1 Ce que fait l'article

Prototype à trois étages contre l'exfiltration d'identifiants par injection indirecte :

1. **CIFT**, sonde d'activations avant la sortie. Lit les états cachés des dernières couches (un quart des couches, 8 pour Qwen-7B) aux positions de lecture situées après le secret et la requête ; écart de Mahalanobis par couche à une base bénigne (« We estimate a benign baseline » [K18], p. 3 ; 500 consignes bénignes, covariance diagonale), puis petit réseau de 9 473 paramètres entraîné avec des étiquettes d'attaque.
2. **DP-HONEY**, faux identifiants plantés, détecteur textuel calibré par prédiction conforme.
3. **NIMBUS**, cumul sur la conversation : « we estimate a per-turn score with an InfoNCE » [K03] (p. 4), score par tour borné à log2(17) ≈ 4,09 bits, sommé sur les tours ; le système déclenche « and trigger warn, sanitize, or block actions as this cumulative score approaches a chosen budget. » [K05] (p. 4). Le critique prend en entrée la sortie du tour, le contexte secret et l'état de la conversation : du texte, pas des activations ; « The critic itself is trained only with » [K23] la perte contrastive, sur des étiquettes de fuite (p. 4).

Modèle de menace : « The attacker may know that honeytokens and monitors are deployed, but cannot modify model weights, the system prompt, or the monitoring pipeline. » [K15] (p. 2). Modèles : Qwen-2.5 (1,5 et 7 milliards de paramètres), Llama-3.1-8B, Mistral-7B.

### 4.2 Résultats chiffrés (auteurs)

- Sonde, un tour, Qwen-7B (tableau 1, p. 5) : « CIFT 0.998 0.990 0.015 » [K19] (aire sous la courbe, F1, taux de faux positifs), contre 0,90 / 0,79 / 0,09 pour le meilleur détecteur textuel (plongements sémantiques) et 0,85 / 0,73 / 0,18 pour LlamaGuard. Faux positifs mesurés ainsi : « False-positive rates are computed on a benign set of 1,000 task-matched prompts containing legitimate tool-use requests and non-secret retrieved content. » [K24] (p. 5).
- Robustesse aux encodages tenus à l'écart (figure 3, p. 6) : « CIFT remains stable in this controlled setting because it measures internal features before output rendering. » [K21].
- **Plusieurs tours** (tableau 3, p. 6) : NIMBUS « (B=10) 0.90 0.00 9.0 1.00 » [K20] (détection, faux blocages, tour moyen de blocage, utilité), contre 0,12 pour LlamaGuard par tour, 0,06 pour les faux identifiants seuls, 0,00 pour la sous-chaîne. Banc : « For multi-turn evaluation we use a separate 50-conversation synthetic suite, each with 20 turns and 4–8 embedded low-rate leakage attempts » [K07] (p. 5). Soit 45 conversations détectées sur 50 (calcul). Figure 4 (p. 7) : « Per-turn leakage scores remain small, while cumulative accounting eventually triggers intervention. » [K13] ; seuil par tour de 1,5 bit, budget de 10 bits, blocage au tour 17 (figure).
- Système intégré, un tour (tableau 4, p. 6) : détection 0,94 et faux positifs 0,018 ; sonde seule 0,88 et 0,015 ; sans activations 0,71 et 0,008.

### 4.3 Réponse à la question posée : y a-t-il une accumulation séquentielle de scores de sondes, et avec quelle garantie ?

**Non, et aucune.**

- Ce qui est cumulé est le score du critique textuel, pas celui de la sonde. Preuve interne : « the API-only configuration relies on canaries and cumulative scoring. » [K09] (p. 6) ; le cumul fonctionne donc sans accès aux activations. La sonde CIFT n'est évaluée que sur un tour : « This is the only experiment that evaluates the multi-turn contribution. » [K14] (p. 5), à propos du tableau 3, où CIFT ne figure pas.
- Garantie : les auteurs l'écartent eux-mêmes. « our estimator should be read as a learned leakage score rather than a certified upper bound on information release. » [K04] (p. 4) ; résumé : « the multi-turn benchmark is in-house and small, the activation method requires white-box access, and the information estimator provides a practical signal rather than a formal upper bound. » [K02] (p. 1). Le budget est choisi à la main [K05] et seulement « recommandé » sur la figure 5 (p. 7), sans calibrage sur des conversations honnêtes à un taux fixé.
- La seule garantie statistique de l'article, la prédiction conforme, porte sur le détecteur textuel de faux identifiants, et les auteurs la bornent : « Conformal calibration assumes exchangeability and can fail under adversarial distribution shift. » [K12] (p. 7).
- Le rappel selon l'horizon n'est pas tracé ; il apparaît en creux dans les échecs : « The undetected synthetic conversations concentrate attack turns early and end before the cumulative score crosses the action threshold. » [K06] (p. 5) ; et « a multi-session attacker could restart sessions to reset the budget unless the deployment stores leakage state across sessions. » [K17] (p. 7).

### 4.4 Limites, incohérences, résultats « trop beaux »

- Limites reconnues : « CIFT requires white-box activation access, which excludes many API-served models. Cross-model transfer is untested. » [K08] (p. 7) ; banc à plusieurs tours synthétique, petit, maison ; identifiants passés par des arguments d'outils hors champ.
- **Trop beau, reconnu par les auteurs** : aire de 0,998. « The high AUROC is plausible only under the controlled setup used here » [K10] (p. 5) ; « very high AUROC values in controlled activation-probe settings require careful leakage checks » [K11] (p. 7). Réserve du lecteur : la sonde finale est entraînée avec des exemples d'attaque, les positions des identifiants sont connues, aucune taille d'échantillon de test ni intervalle n'est imprimé pour le tableau 1.
- Trop beau aussi : 0,00 faux blocage et utilité de 1,00 pour NIMBUS sur 50 conversations, sans nombre de conversations bénignes imprimé.
- Incohérences ou manques : le chiffre « the reported integrated table is therefore on a disjoint held-out subset rather than the full 2,439 public attack prompts. » [K22] (p. 5) est le seul endroit où la taille du banc public apparaît ; le sous-ensemble réellement évalué n'est pas chiffré. Tableau 2 : rappel de 1,000 et détection d'un faux identifiant de 0,990 côte à côte, sans explication. Une référence cassée : « representation engineering (?) » [K25] (p. 2). Latence de la sonde seule de +1 ms contre +14 ms sans sonde (tableau 4) : non expliqué. L'opérateur du système complet est un « ou » : « The full pipeline uses a logical OR over » [K16] les alarmes (p. 6), et les auteurs renoncent à revendiquer une dominance.
- L'agent lu est la victime d'une injection, pas un agent qui sabote de lui-même.

### 4.5 Verdicts

| Énoncé | Verdict | Fait | Non fait | Pages |
|---|---|---|---|---|
| H1 | **voisin** | sonde sur les activations d'un agent contre détecteurs textuels, sur la même tâche ; la sonde devance sur l'aire, le F1 et les faux positifs | faux positifs égaux (chaque méthode a le sien) ; sabotage diffus ; tâches floues ; trajectoire ; chiffres non opposables (trop beaux, sans intervalle) | 5, 6 |
| H2 | **occupée en partie, en boîte noire** (lecture dure retenue ; lecture « voisin fort » possible) | cumul additif tour après tour ; chaque tour d'attaque sous le seuil par tour ; détecteurs par tour en échec (0,12) ; détection qui exige un horizon suffisant | **scores de sondes** (le cumul porte sur un critique textuel) ; garantie toujours valide (écartée par les auteurs) ; seuil par action calibré à 1 % sur l'honnête ; calibrage sans exemple d'attaque (critique et sonde entraînés avec étiquettes) ; rappel tracé selon l'horizon ; agent saboteur ; contexte privé | 4, 5, 6, 7 |
| HC2 | **voisin** ; indice favorable faible, non adaptatif | une sonde qui lit l'agent attaqué reste stable sous des encodages et paraphrases demandés par le contenu injecté | attaquant qui vise la sonde ; mesure d'un gain ; sonde lisant l'auteur du contenu ; agrégation robuste | 2, 6 |

**Reste revendicable pour H2** : inchangé. La conjonction de N-007 (accumulation additive **toujours valide** de **scores de sondes de l'agent qui agit**, actions sous un moniteur par action à 1 %, rappel croissant avec l'horizon, calibrage sur épisodes honnêtes sans exemple de sabotage) n'est pas dans cette source. Cet article est à citer comme le précédent le plus proche qui **juxtapose** une sonde d'agent et un cumul sur plusieurs tours **sans les joindre**, et qui nomme lui-même l'absence de garantie.

## 5. Zhao, Liu, Yu, Kung, Chen, Mi, Yu — « One Token to Fool LLM-as-a-Judge », 2507.08794v3 (11 juin 2026, 31 pages)

**Venue imprimée** : « Preprint. Under review. » [O01] (en-tête de chaque page).

### 5.1 Ce que fait l'article

- Cadre : juge génératif avec réponse de référence, verdict binaire OUI ou NON utilisé comme récompense (« This judgment translates directly into a reward signal » [O05], p. 3). Décodage : « inference is performed with num_samples set to 1 and temperature fixed at 0. » [O11] (p. 16) ; verdict lu comme texte, sans probabilité de jeton.
- Attaque : dix « passe-partout » sans contenu, quatre symboles (espace, point, virgule, deux-points) et six amorces de raisonnement (« Thought process: », « Solution », etc.), qui « can consistently elicit false positive rewards without any substantive reasoning. » [O02] (p. 1) et sont, selon les auteurs, « even though they are semantically meaningless for solving the task. » [O19] (p. 4). **Aucun ordre, aucun argument, aucune revendication d'autorité.**
- Origine : découverte par un effondrement d'entraînement par renforcement contre le juge Qwen2.5-72B ; la politique finit par répondre « Thought Process: » dans 94,26 % des cas (tableau 14, p. 23), et « Surprisingly, we observe that Qwen2.5-72B-Instruct judges that these vacuous responses » [O03] sont jugées justes à environ 90 % (p. 22). L'attaque est donc issue d'une optimisation, non d'une conception.
- Juges : 12 (trois spécialisés, sept généralistes dont GPT-4o, GPT-o1 et Claude-4-Sonnet, plus deux « Master-RM » des auteurs) ; cinq bancs (de 933 à 6 000 questions, tableau 5).
- Défense : 20 000 exemples négatifs faits de la première phrase de réponses tronquées (« We then assign these examples a label of NO, indicating an invalid or meaningless response. » [O18], p. 5), ajoutés à 160 000 exemples.

### 5.2 Résultats chiffrés (auteurs, tableau 1, p. 7)

- Taux de faux positifs moyen et pire, par juge, sur les cinq bancs (ordre des colonnes : Master-RM-7B, Master-RM-32B, Multi-sub RM, General-Verifier, Omni-Judge, Qwen2.5-72B, Qwen2.5-7B, LLaMA3-70B, LLaMA3-8B, GPT-4o, GPT-o1, Claude-4) : « 0.1 | 2.9 0.8 | 5.4 1.1 | 11.5 9.7 | 87.0 14.3 | 54.1 66.8 | 90.9 12.6 | 31.0 80.6 | 95.1 76.9 | 92.0 14.6 | 53.6 6.0 | 37.3 12.4 | 57.7 » [O16].
- Défense : « they achieve near-zero (if not zero) false positive rates on all tested “master keys” across all five benchmarks » [O13] (p. 5).
- Taille : relation non monotone ; « The 0.5B model achieves the lowest FPR but also shows the weakest alignment with GPT-4o (Table 2a). » [O07] (p. 8) ; hypothèse des auteurs pour les grands juges : « we hypothesize that the increased false positive rate in larger models is attributable to their inherent tendency to solve the question themselves » [O14] (p. 23).
- Techniques d'inférence (raisonnement pas à pas et vote sur cinq tirages, tableau 3, p. 9) : « Overall 50.9 | 97.0 66.8 | 90.9 40.4 | 91.3 12.6 | 31.0 » [O20] (Qwen2.5-72B avec puis sans, Qwen2.5-7B avec puis sans). Conclusion des auteurs : l'effet « is highly model- and domain-dependent » [O12] (p. 27) ; résumé : « chain-of-thought prompting and majority voting do not reliably defend and can even exacerbate the attack, whereas removing the question from the evaluation prompt substantially mitigates the vulnerability. » [O04] (p. 3).
- Retirer la question de la consigne : « Removing the question sharply reduces FPR. » [O08] (p. 9). Qwen2.5-72B sur GSM8K : de 87,6 à 0,0 (tableau 19, p. 31).
- Nouvelles clés par proximité de plongement : « we randomly select two out of their five most similar sentences. » [O15] (p. 27) ; GPT-4o bascule de 0,3 % à 50,0 % selon la clé et le banc (tableau 15, p. 26).
- Antériorité que l'article cite lui-même : « Raina et al. (2024) demonstrated that appending simple universal adversarial phrases to low-quality responses substantially increases the likelihood of LLM preference. » [O09] (p. 15) ; « concurrent work by Huang et al. (2025c) showed that LLM reward models are easily deceived by various attacks in mathematical reasoning, including empty symbols or nonsensical responses that trigger false positives. » [O10] (p. 15).

### 5.3 Limites, incohérences, résultats « trop beaux »

- **Trop beau** : 0,0 presque partout pour les deux Master-RM. Réserves : les dix clés sont fixes et connues ; aucune attaque adaptative contre le juge durci ; les amorces de test ressemblent aux négatifs d'entraînement (premières phrases de réponses), ce que les auteurs écartent par une seule vérification de non-recouvrement littéral. Les données et modèles ne sont pas encore publiés : « we will release the augmented 180k-instance training dataset along with the Master RMs. » [O21] (p. 3).
- Incohérence : le texte dit que le deux-points seul « can induce errors in GPT-4o with up to 35% FPRs. » [O06] (p. 6) ; au tableau 1, le maximum du deux-points pour GPT-4o est 24,4 (ligne GSM8K : « : 0.0 0.0 0.0 0.7 17.0 90.8 23.1 89.2 84.8 24.4 16.9 15.0 » [O17]), et 35,9 est la valeur de l'espace. La légende de la figure 1 annonce « false positive rates (FPRs) as high as 80% » [O23] (p. 1) quand le tableau monte à 95,1.
- Accord humain mesuré par les auteurs eux-mêmes : « The human annotation process was performed independently by five authors » [O22] (p. 21), sur 500 exemples.
- Une seule intensité par clé ; verdict binaire ; aucun moniteur de contrôle ; aucune sonde.

### 5.4 Verdicts

| Énoncé | Verdict | Fait | Non fait | Pages |
|---|---|---|---|---|
| HC1 | **voisin** ; **contre-indice faible** pour « g stable par moniteur » | juges génératifs déplacés par un contenu vide, deux familles, douze juges, cinq bancs ; destination imposée (le OUI) ; forte dépendance au banc et à la consigne pour un même juge (0,0 à 87,6) | (a) destination libre testée contre la cible et la moyenne ; (b) intensités graduées et régression ; (c) probabilité du jeton ; (d) juge contre sonde ; moniteur de contrôle | 7, 9, 26, 31 |
| HC3 | **voisin** (précédent à citer pour « sans aucun ordre ») | un contenu sans ordre ni argument, qui imite l'amorce d'une réponse raisonnée, déplace des juges génératifs jusqu'à 95,1 % ; plus fort que les symboles | usurpation du style de l'**instructeur** ; juge moniteur de contrôle ; protocole « contenu = données » ; loi continue ; sondes lisant l'auteur | 4, 7, 15 |
| HC6 | **voisin** ; **contre-indice faible, par analogie** | une mesure bénigne (accord avec l'humain sur des réponses ordinaires) ne classe pas la robustesse : corrélation de rangs de −0,34 sur dix juges, −0,10 sans les deux Master-RM (calcul) ; Qwen2.5-72B, accord de 0,88, bascule à 66,8 % | g mesuré sous pression bénigne ; attaque optimisée contre chaque juge ; prédiction | 7, 8 |

**Reste revendicable.** HC1, HC3, HC6 : inchangés. À ajouter aux sources « citées comme publiées » : pour HC3, « un contenu sans ordre déplace des juges génératifs » est acquis hors contrôle (cet article, et Raina et collègues 2024 et Huang et collègues 2025c qu'il cite, non lus ici) ; ce qui reste à HC3 est l'usurpation du style de l'instructeur, sur des juges moniteurs, en loi continue, avec le nul sur les sondes de l'auteur. Pour HC6, la barre à battre s'élève : g bénin doit prédire mieux que l'exactitude bénigne, qui ici ne prédit rien. Pour HC1, le préenregistrement devrait prévoir que g dépend du gabarit de consigne (présence de la question) autant que du moniteur.

## 6. Verdict d'ensemble par énoncé

| Énoncé | 2606.08892v3 | 2609.06966v1 | 2606.04141v1 | 2507.08794v3 | Ensemble | Reste revendicable |
|---|---|---|---|---|---|---|
| H1 | voisin | voisin de contexte | voisin | — | **voisin** | inchangé |
| H2 (N-007) | ne touche pas | voisin ; contre-indice faible (boîte noire) | **occupée en partie, en boîte noire** | — | **occupée en partie, jamais en entier** (comme au niveau 2) | inchangé : la conjonction avec des scores de sondes et une garantie toujours valide |
| H6 | voisin lointain | — | — | — | **voisin** | inchangé |
| H8 | ne touche pas | — | — | — | **ne touche pas** | inchangé |
| Papier B | ne touche pas | voisin (statistique de population) | — | — | **voisin** | inchangé |
| HC1 | — | — | — | voisin ; contre-indice faible | **voisin** | inchangé |
| HC2 | — | ne touche pas | voisin ; indice favorable faible | — | **voisin** | inchangé |
| HC3 | — | — | — | voisin (à citer) | **voisin** | inchangé ; préciser « style de l'instructeur » |
| HC4 | — | ne touche pas | — | — | **ne touche pas** | inchangé |
| HC5 | — | voisin | — | — | **voisin** | inchangé |
| HC6 | — | — | — | voisin ; contre-indice faible | **voisin** | inchangé ; battre l'exactitude bénigne |

Aucune de ces quatre sources n'ouvre un nœud « zone revendiquée trouvée occupée ». Le point à porter à Lazar est d'information : la version publiée du voisin le plus proche maintient que la surveillance est la voie la moins prometteuse contre les menaces diffuses, et n'y ajoute aucune mesure.

## Annexe — citations contrôlées

- [T01] 2606.08892v3, p. 1 : « 40th Conference on Neural Information Processing Systems (NeurIPS 2026). »
- [T02] 2606.08892v3, p. 1 : « https://github.com/MikhailTerekhov/diffuse_control »
- [T03] 2606.08892v3, p. 2 : « We focus on training mitigations, since monitoring and incrimination seem theoretically [Hebbar, 2025] and empirically [Gasteiger et al., 2025, Gan et al., 2026] less promising for mitigating diffuse threats. »
- [T04] 2606.08892v3, p. 2 : « This lets us sidestep the problem of the inductive bias of the model organism that is usually present when evaluating training-based mitigations in AI control »
- [T05] 2606.08892v2, p. 2 : « The framework allows us to decouple the unknown inductive biases of fine-tuning a scheming model »
- [T06] 2606.08892v3, p. 4 : « resulting in a dataset of 2340 poster papers for training and 302 spotlight and oral papers for validation »
- [T07] 2606.08892v2, p. 4 : « resulting in a dataset of 2346 poster papers for training and 302 spotlight and oral papers for validation »
- [T08] 2606.08892v3, p. 5 : « this baseline checks whether the multi-objective runs perform sufficient exploration to reach the true maximum of the weak score. »
- [T09] 2606.08892v3, p. 8 : « Notably, this diagonal shape persists despite the red team using a larger budget of 100 rung-2-evaluated attacks »
- [T10] 2606.08892v3, p. 8 : « remains similar when we perform RL fine-tuning instead of prompt optimization to discover the boundary of the admissible region. »
- [T11] 2606.08892v3, p. 9 : « Wen et al. [2024] did early work on diffuse threats, but, unlike us, they focused on detection. »
- [T12] 2606.08892v3, p. 10 : « Our ground truth proxy score was not validated quantitatively against human judges. »
- [T13] 2606.08892v3, p. 10 : « like using the untrusted model for scoring with collusion busting or rewriting the generated proposals with a trusted model. »
- [T14] 2606.08892v2, p. 9 : « A natural extension would be to consider fine-tuning the models, though we would lose the clean interpretability of the resulting strategies. »
- [T15] 2606.08892v3, p. 16 : « We choose to anchor the spread of this distribution to that of the GT proxy scores »
- [T16] 2606.08892v3, p. 26 : « = 1/(10i), splitting up the remaining 0.5 weight equally between all groups. »
- [T17] 2606.08892v2, p. 25 : « = 1/(5i), splitting up the remaining 0.5 weight equally between all groups. »
- [T18] 2606.08892v3, p. 60 : « Linear probing for pose per layer »
- [T19] 2606.08892v3, p. 80 : « Throughout the paper, we use prompt optimization as the main strategy for the red team. »
- [T20] 2606.08892v3, p. 81 : « We use GPT-OSS-120B as the generator, which we fine-tune with the Tinker API. »
- [T21] 2606.08892v3, p. 81 : « We see that, as expected, RL pushes the scores much further than prompt optimization. »
- [T22] 2606.08892v3, p. 81 : « When the generator is optimized with RL, the admissible region against the robustified weak scorer does not have a flat top. »
- [T23] 2606.08892v3, p. 81 : « so our results imply that the blue team strategy generalizes across generator models. »
- [T24] 2606.08892v3, p. 82 : « We see that towards the end of the budget of 700 steps, the boundary stops changing »
- [T25] 2606.08892v3, p. 83 : « Here, we take two red team prompts from the prompt-optimized subversion Pareto frontier »
- [T26] 2606.08892v3, p. 84 : « The recovery is still not perfect: at the end of training against the robustified weak scorer, the more aggressive second model organism retains a lower GT proxy score than the less aggressive first one. »
- [T27] 2606.08892v3, p. 25 : « However, if we run a separate red team optimization against this strategy, we can also discover effective attacks. »
- [T28] 2606.08892v3, p. 23 : « could be an effective approach for the blue team; however, this would be inconsistent with the principle of letting the red team attack adaptively. »
- [T29] 2606.08892v3, p. 4 : « The weak scorer is very noisy, with the biggest component of the variance being scorer noise. »
- [T30] 2606.08892v3, p. 17 : « ICLR 2026 120 2340 24 253 1903 280 »
- [T31] 2606.08892v2, p. 16 : « ICLR 2026 120 2347 24 253 1903 280 »
- [T32] 2606.08892v3, p. 84 : « the trajectories are tilted to the right, indicating that there is nontrivial generalization from the weak score to GT proxy. »
- [T33] 2606.08892v3, p. 81 : « To reduce training costs, we ask the generator to produce 5 proposals instead of 10, which is used in the rest of the paper. »
- [T34] 2606.08892v3, p. 10 : « where the red team is trying to distinguish whether it is in the deployment distribution and the blue team is trying to obfuscate the distinction. »
- [M01] 2609.06966v1, p. 1 : « even the best evaluated monitor in our single-day audit-event comparison misses nearly half of completed harm. »
- [M02] 2609.06966v1, p. 4 : « The third adds agent reasoning, the model’s reasoning trace. »
- [M03] 2609.06966v1, p. 5 : « it may score the current day alone or incorporate earlier days. »
- [M04] 2609.06966v1, p. 7 : « GPT-4.1 with agent reasoning outperforms audit-only GPT-5.5: 0.49 vs. 0.39, 0.71 vs. 0.52, and 0.68 vs. 0.45, respectively »
- [M05] 2609.06966v1, p. 7 : « Reciprocal-rank fusion with the robust z-score ranking improves audit-event detection in all 12 generator–monitor combinations »
- [M06] 2609.06966v1, p. 8 : « audit events from preceding account-days raises fraud recall from 0.00 to 0.67 but leaves data-poisoning recall at 0.00. »
- [M07] 2609.06966v1, p. 10 : « We evaluate end-of-day monitoring; future work should study online intervention, adaptive attackers, and larger collusions. »
- [M08] 2609.06966v1, p. 10 : « collusive threats involve two accounts. »
- [M09] 2609.06966v1, p. 18 : « neither probes participants nor judges a coalition against a known cooperative objective. »
- [M10] 2609.06966v1, p. 27 : « Expanding the window from 1 to 3 and 7 days reduces AUROC from 0.729 to 0.660 and 0.631, respectively, and reduces budget-AUC from 0.149 to 0.112 and 0.088. »
- [M11] 2609.06966v1, p. 28 : « No monitor input includes the private objective, completed-harm condition, or ground-truth label. »
- [M12] 2609.06966v1, p. 38 : « raises fraud recall from 0.00 to 0.67 but reduces recall on the other three threats. »
- [M13] 2609.06966v1, p. 38 : « Averaging the ranks assigned by the two monitors receiving scored and preceding days does not increase fraud recall. »
- [M14] 2609.06966v1, p. 42 : « The results do not show a consistent stealth effect. »
- [M15] 2609.06966v1, p. 48 : « We do not report prevention experiments in this paper. »
- [M16] 2609.06966v1, p. 46 : « Using absolute GPT-5.5 thresholds yields 0.513 and 0.650 on the two GPT-5.3 corpora but only 0.271 on Kimi-K2.6 single-day. »
- [M17] 2609.06966v1, p. 44 : « with frequencies computed from the same-day activity of other accounts on the same team rather than from the training period. »
- [M18] 2609.06966v1, p. 3 : « Only a completed execution, verified in service state, receives a positive label. »
- [M19] 2609.06966v1, p. 24 : « They rate the matched threat objectives as plausible in absolute terms, but assign similar ratings to the role-mismatched threat controls. »
- [M20] 2609.06966v1, p. 33 : « GPT-5.5 0.765/0.45 0.822/0.48 0.923/0.81 0.910/0.77 0.776/0.39 »
- [M21] 2609.06966v1, p. 5 : « We report R@10/day and budget-AUC, the mean R@K/day over K = 1, . . . , 10. »
- [M22] 2609.06966v1, p. 20 : « In a solo multiday campaign, the preparation day remains negative because it does not complete the objective; only the later completion day can be positive. »
- [M23] 2609.06966v1, p. 6 : « Refusal rates do not track completion. »
- [M24] 2609.06966v1, p. 31 : « GPT-5.3 multiday campaign corpus; 17 positive »
- [M25] 2609.06966v1, p. 36 : « Qwen and DeepSeek expose the concealment strategy directly in agent reasoning »
- [M26] 2609.06966v1, p. 45 : « The selective strategy routes 17.1% of account-days to GPT-5.5 »
- [K01] 2606.04141v1, p. 1 : « Published at the Second Workshop on Agents in the Wild: Safety, Security, and Beyond (AIWILD) at ICML 2026. »
- [K02] 2606.04141v1, p. 1 : « the multi-turn benchmark is in-house and small, the activation method requires white-box access, and the information estimator provides a practical signal rather than a formal upper bound. »
- [K03] 2606.04141v1, p. 4 : « we estimate a per-turn score with an InfoNCE »
- [K04] 2606.04141v1, p. 4 : « our estimator should be read as a learned leakage score rather than a certified upper bound on information release. »
- [K05] 2606.04141v1, p. 4 : « and trigger warn, sanitize, or block actions as this cumulative score approaches a chosen budget. »
- [K06] 2606.04141v1, p. 5 : « The undetected synthetic conversations concentrate attack turns early and end before the cumulative score crosses the action threshold. »
- [K07] 2606.04141v1, p. 5 : « For multi-turn evaluation we use a separate 50-conversation synthetic suite, each with 20 turns and 4–8 embedded low-rate leakage attempts »
- [K08] 2606.04141v1, p. 7 : « CIFT requires white-box activation access, which excludes many API-served models. Cross-model transfer is untested. »
- [K09] 2606.04141v1, p. 6 : « the API-only configuration relies on canaries and cumulative scoring. »
- [K10] 2606.04141v1, p. 5 : « The high AUROC is plausible only under the controlled setup used here »
- [K11] 2606.04141v1, p. 7 : « very high AUROC values in controlled activation-probe settings require careful leakage checks »
- [K12] 2606.04141v1, p. 7 : « Conformal calibration assumes exchangeability and can fail under adversarial distribution shift. »
- [K13] 2606.04141v1, p. 7 : « Per-turn leakage scores remain small, while cumulative accounting eventually triggers intervention. »
- [K14] 2606.04141v1, p. 5 : « This is the only experiment that evaluates the multi-turn contribution. »
- [K15] 2606.04141v1, p. 2 : « The attacker may know that honeytokens and monitors are deployed, but cannot modify model weights, the system prompt, or the monitoring pipeline. »
- [K16] 2606.04141v1, p. 6 : « The full pipeline uses a logical OR over »
- [K17] 2606.04141v1, p. 7 : « a multi-session attacker could restart sessions to reset the budget unless the deployment stores leakage state across sessions. »
- [K18] 2606.04141v1, p. 3 : « We estimate a benign baseline »
- [K19] 2606.04141v1, p. 5 : « CIFT 0.998 0.990 0.015 »
- [K20] 2606.04141v1, p. 6 : « (B=10) 0.90 0.00 9.0 1.00 »
- [K21] 2606.04141v1, p. 6 : « CIFT remains stable in this controlled setting because it measures internal features before output rendering. »
- [K22] 2606.04141v1, p. 5 : « the reported integrated table is therefore on a disjoint held-out subset rather than the full 2,439 public attack prompts. »
- [K23] 2606.04141v1, p. 4 : « The critic itself is trained only with »
- [K24] 2606.04141v1, p. 5 : « False-positive rates are computed on a benign set of 1,000 task-matched prompts containing legitimate tool-use requests and non-secret retrieved content. »
- [O01] 2507.08794v3, p. 1 : « Preprint. Under review. »
- [O02] 2507.08794v3, p. 1 : « can consistently elicit false positive rewards without any substantive reasoning. »
- [O03] 2507.08794v3, p. 22 : « Surprisingly, we observe that Qwen2.5-72B-Instruct judges that these vacuous responses »
- [O04] 2507.08794v3, p. 3 : « chain-of-thought prompting and majority voting do not reliably defend and can even exacerbate the attack, whereas removing the question from the evaluation prompt substantially mitigates the vulnerability. »
- [O05] 2507.08794v3, p. 3 : « This judgment translates directly into a reward signal »
- [O06] 2507.08794v3, p. 6 : « can induce errors in GPT-4o with up to 35% FPRs. »
- [O07] 2507.08794v3, p. 8 : « The 0.5B model achieves the lowest FPR but also shows the weakest alignment with GPT-4o (Table 2a). »
- [O08] 2507.08794v3, p. 9 : « Removing the question sharply reduces FPR. »
- [O09] 2507.08794v3, p. 15 : « Raina et al. (2024) demonstrated that appending simple universal adversarial phrases to low-quality responses substantially increases the likelihood of LLM preference. »
- [O10] 2507.08794v3, p. 15 : « concurrent work by Huang et al. (2025c) showed that LLM reward models are easily deceived by various attacks in mathematical reasoning, including empty symbols or nonsensical responses that trigger false positives. »
- [O11] 2507.08794v3, p. 16 : « inference is performed with num_samples set to 1 and temperature fixed at 0. »
- [O12] 2507.08794v3, p. 27 : « is highly model- and domain-dependent »
- [O13] 2507.08794v3, p. 5 : « they achieve near-zero (if not zero) false positive rates on all tested “master keys” across all five benchmarks »
- [O14] 2507.08794v3, p. 23 : « we hypothesize that the increased false positive rate in larger models is attributable to their inherent tendency to solve the question themselves »
- [O15] 2507.08794v3, p. 27 : « we randomly select two out of their five most similar sentences. »
- [O16] 2507.08794v3, p. 7 : « 0.1 | 2.9 0.8 | 5.4 1.1 | 11.5 9.7 | 87.0 14.3 | 54.1 66.8 | 90.9 12.6 | 31.0 80.6 | 95.1 76.9 | 92.0 14.6 | 53.6 6.0 | 37.3 12.4 | 57.7 »
- [O17] 2507.08794v3, p. 7 : « : 0.0 0.0 0.0 0.7 17.0 90.8 23.1 89.2 84.8 24.4 16.9 15.0 »
- [O18] 2507.08794v3, p. 5 : « We then assign these examples a label of NO, indicating an invalid or meaningless response. »
- [O19] 2507.08794v3, p. 4 : « even though they are semantically meaningless for solving the task. »
- [O20] 2507.08794v3, p. 9 : « Overall 50.9 | 97.0 66.8 | 90.9 40.4 | 91.3 12.6 | 31.0 »
- [O21] 2507.08794v3, p. 3 : « we will release the augmented 180k-instance training dataset along with the Master RMs. »
- [O22] 2507.08794v3, p. 21 : « The human annotation process was performed independently by five authors »
- [T35] 2606.08892v3, p. 81 : « we see that the prompt optimization frontier has a shorter flat top »
- [T36] 2606.08892v2, p. 2 : « since monitoring and incrimination seem theoretically [Hebbar, 2025] and empirically [Gasteiger et al., 2025, Gan et al., 2026] less promising for mitigating diffuse threats. »
- [T37] 2606.08892v3, p. 8 : « only incurs a minor capabilities tax when used with a benign model »
- [T38] 2606.08892v3, p. 83 : « All scorer prompts were minimally edited to adapt to 5 proposals being scored instead of 10. »
- [T39] 2606.08892v3, p. 8 : « suggesting that the optimization process for b∗ described above does result in a weak scorer that leads to a partial removal of subversion propensities in adversarial conditions. »
- [T40] 2606.08892v3, p. 7 : « essentially diagonal »
- [T41] 2606.08892v2, p. 1 : « Preprint. »
- [O23] 2507.08794v3, p. 1 : « false positive rates (FPRs) as high as 80% »
- [K25] 2606.04141v1, p. 2 : « representation engineering (?) »

# Lecture sur source, niveau 3, lot 3-A — sondes contre moniteurs boîte noire sur du sabotage d'agent, et sondes sous injection — v1

Écrit le 2026-11-10 vers 11:12 UTC (heure relevée par `date -u`). Lecteur neuf : je n'ai écrit ni le programme ni aucun rapport antérieur. « Libre » veut dire « non trouvé dans les sources lues », jamais « trou du champ ».

Les citations sont désignées par leur identifiant (par exemple F4-08) ; chacune figure, avec son PDF et sa page, dans `citations.json` (archive) et a été contrôlée par script (section 10). Nature des chiffres : « auteurs » (imprimé), « calcul » (recalculé par moi) ; aucun chiffre n'est lu sur une figure.

## En tête : occupations, même partielles

- **H1 — occupée en partie par 2610.12445 (« Telling FIBS », FAR.AI ; déjà dans la v1 du 8 octobre, élargi dans la v4 du 20 octobre).** Fait : sondes d'activations contre moniteurs boîte noire, sur du sabotage d'agent en politique propre (SHADE-Arena, BashArena), par étape, **à taux de faux positifs égal de 1 %, 2 % et 5 %**, négatifs pris sur les épisodes honnêtes des mêmes tâches et sur les étapes d'avant l'attaque ; résultat favorable aux sondes (F4-08, F4-14, F4-15, F4-21). **Non fait : le sabotage diffus — il est écarté explicitement** (F4-24, F4-25) —, les tâches floues, toute agrégation sur la trajectoire, un seuil calibré hors échantillon (F4-07), un moniteur qui lit le raisonnement (F4-04, F4-23), un adversaire adapté à la sonde. La lettre de ce qui reste revendicable pour H1 (la mesure sur du diffus et du flou) tient, mais le précédent est désormais « sabotage d'agent à 1 % de faux positifs » et non plus « réponses isolées ». **Cette source n'est pas dans le tableau H1 de l'état actuel de l'antériorité.**
- **HC2 — aucune occupation nouvelle.** Les trois articles lus (2610.37679, 2611.11172, 2610.18408) lisent tous un agent **victime** d'une injection écrite par un tiers, sans attaquant adapté à la sonde, sans mesure continue du déplacement. Ce qui reste revendiqué (sonde lisant l'agent auteur et adversaire, g en plan apparié, comparé aux juges) n'est pas touché. Deux précisions à porter au préenregistrement : le **plan apparié** existe déjà côté lecteur (2610.18408 : jumeau propre et sosie inoffensif) ; une sonde sur un agent sous injection lit d'abord l'**exposition** au contenu, pas l'engagement (2610.37679).
- **H3 (FakeLab v2) : rien de nouveau.** Ni moniteur à état, ni sonde, ni état interne ; la v2 ajoute une réplique boîte noire sur un second modèle (DeepSeek V4 Flash, un agent contre trois) et corrige une limite de pas du planificateur.
- **H2, H8 : voisins seulement** ; aucune occupation trouvée dans ce lot.

## 1. Méthode

- Énoncés lus : `docs/programme-controle-ia-v2.md` (lignes 85 à 125, 190 à 215), `docs/decisions/decision-N-013-v1.md`, sections H1, H8, HC2, HC2b, H3 de `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md`, sections « En tête » et 3 de `rapport-lot1-HC2-mirage-karne-v1.md`.
- Empreintes : les neuf PDF concordent avec leur compagnon `.sha256` (2610.12445v4 `8d3ada9a…`, v1 `7e141758…` ; 2607.07368v2 `2ec84e86…`, v1 `d72cae43…` ; 2610.37679v1 `8640d1f0…` ; 2611.11172v1 `6275a54a…` ; 2610.18408v1 `41174855…` ; 2606.12618v2 `2eccf773…` ; 2606.30449v1 `775abf11…`).
- Lecture par `pdftotext` (mode `-layout` pour les tableaux, mode brut pour les pages à deux colonnes) ; tableau 6 de 2610.12445v4 relu en image (page 26).
- **Profondeur de lecture, dite telle quelle.** Lus en entier : 2610.37679 (16 pages), 2611.11172 (6 pages), 2606.30449 (corps, limites, annexes survolées ligne à ligne), 2610.18408 (corps en entier ; annexe E : légendes et texte, pas chaque cellule). 2606.12618v2 : pages 1 à 17 lues, annexes 18 à 32 parcourues par mots-clés. **2610.12445v4 (119 pages) : corps (pages 1 à 15) et annexes B à E (pages 21 à 41, celles du sabotage d'agent) lus en entier ; annexes A et F à N (architectures, organismes à but caché, jeu de données, consignes des juges) parcourues par mots-clés et par comparaison de phrases avec la v1, pas ligne à ligne.** Les deux versions v1 (2610.12445, 2607.07368) n'ont été lues que par différence.
- Différences de versions : `pdftotext`, puis comparaison des phrases normalisées (script `diff_phrases.py` de l'archive : 708 phrases propres à la v1 et 1 069 propres à la v4 pour 2610.12445 ; 137 et 182 pour 2607.07368).

## 2. 2610.12445v4 — « Telling FIBS: Probes Effectively Detect Sabotage and Catch Unverbalized Deception » (FAR.AI)

Venue imprimée : aucune (prépublication arXiv, version 4 du 20 octobre 2026).

### 2.1 Ce que fait l'article

- **Objet de la sonde.** Des « faussetés sues » : un énoncé que le modèle tient pour faux. Les auteurs écartent l'intention : « We do not aim to detect deceptive intent, misleading but true statements, or any other type of non-falsehood-stating behavior. » (F4-03, p. 2).
- **Entraînement.** Jeu FIBS, 163 016 transcriptions, 28 familles, presque entièrement hors politique pour les modèles sondés (F4-30, p. 5) ; bruit d'étiquettes estimé à 0,74 % (F4-35, p. 5, auteurs).
- **Sondes.** Quatre architectures (linéaire et perceptron par couche, moyennés ; « axial », petit transformeur qui porte l'attention sur les jetons puis sur les couches ; « EFC », covariance des activations projetées), six couches de 30 % à 90 % de la profondeur, lues sur les jetons du dernier tour.
- **Lecture d'un agent.** Après **chaque** appel d'outil, on ajoute une question de suivi et une réponse préremplie « Yes. » ou « No. », et le score est la différence entre les deux préremplissages : les sondes servent, « combined with a specific follow-up question, as monitors to detect if a misaligned action was taken in a particular step » (F4-05, p. 3). La lecture n'est donc pas passive : six branches par étape (trois questions, deux préremplissages).
- **Cadres.** SHADE-Arena : 14 scénarios sur 26, 25 épisodes honnêtes et 25 avec tâche cachée par scénario, 700 épisodes par modèle (F4-36, p. 34), neuf agents à poids ouverts. BashArena : 628 tâches, cinq conditions, 3 140 épisodes par agent, trois agents. Aucun moniteur ne tourne pendant les épisodes (F4-33, p. 39).
- **Étiquettes.** Un juge (Claude Haiku 5.5) étiquette chaque étape vue seule ; la première étape marquée est le « début » ; « That step and every later step are positives. The earlier steps and every step of an honest episode, whatever the judge says, are negatives. » (F4-06, p. 25), et « A post-onset step stays positive whatever its own label. » (F4-31, p. 25).
- **Moniteurs boîte noire.** Ils lisent la transcription jusqu'à l'étape notée, **sans le raisonnement de l'agent** (F4-23, p. 28 ; choix assumé, F4-04, p. 3) et rendent une note de 0 à 100 (F4-37, p. 29) : Kimi K3, l'agent lui-même (« self-monitor »), et par interface Claude Haiku 5.5, Claude Opus 5.5, GPT-6.1 Sol (F4-38, p. 27).
- **Métriques.** Aire sous la courbe par étape, et rappel au seuil de 1 %, 2 %, 5 % de faux positifs. Le seuil est pris **dans l'échantillon évalué** : « Each detector’s threshold is set in sample (the 99th percentile of negative steps). » (F4-07, p. 8).

### 2.2 Résultats chiffrés (auteurs)

- Résumé : « Our probes surpass black-box monitors on agentic coding benchmarks, achieving 98.7% AUROC in SHADE-Arena and 98.0% in BashArena (vs. 97.7% and 97.6% for the strongest action-only text monitors) » (F4-01, p. 1). L'écart en aire sous la courbe est d'un point au plus ; les auteurs le disent : « By SHADE-Arena AUROC the probes and monitors are closer (Figure 6a), but the probes still outperform for 2 of the 3 largest models. » (F4-10, p. 8).
- À 1 % de faux positifs : « At a 1% false-positive rate, the best probe on each agent flags more post-onset steps than the Kimi K3 monitor, the self-monitor and the model’s self-report, in both settings » (F4-08, p. 8) ; sur Qwen3.5-397B, la sonde EFC signale 25 à 28 points de plus que le moniteur Kimi K3 (F4-09, p. 8).
- Tableau 6, p. 26, SHADE-Arena, rappel et faux positifs réalisés à 1 %, 2 %, 5 % :
  - Qwen3.5-397B : sonde EFC 73,0 / 83,3 / 93,6 (F4-14) ; auto-moniteur 30,2 / 53,0 / 70,9 (F4-15) ; Opus 5.5, Haiku 5.5 et Sol 6.1 n'ont **aucun seuil** à 1 % ;
  - Nemotron-3 Ultra : meilleure sonde (linéaire) 45,6 / 63,7 / 78,9 (F4-40) ; auto-moniteur 22,4 / 39,2 / 65,1 (F4-41) ;
  - Kimi K3 : sonde EFC 64,5 / 75,5 / 89,2 (F4-16) ; **Sol 6.1 65,1 / 75,1 / 92,0** (F4-17) ; auto-moniteur 44,2 / 67,5 / 91,5 (F4-39). Les auteurs l'écrivent : le meilleur détecteur à 1 % est « Sol 6.1* on Kimi K3, where the EFC probe is the best probe » (F4-18, p. 26).
- BashArena, mêmes étapes pour la sonde et le moniteur (tableau 9, p. 28) : sur Qwen3.5-397B, Haiku 5.5 rappel 0,35 et aire 0,976 contre sonde EFC 0,73 et 0,980 (F4-22) ; « On these steps the EFC probe has a higher recall at a 1% FPR and a higher AUROC than every monitor on every agent (Table 9). » (F4-21, p. 28).
- La diversité des familles d'entraînement, à taille fixe, aide peu : « At 15k and 39k rows, the number of families changes the mean AUROC by at most 0.015 and 0.005. » (F4-29, p. 37).

### 2.3 Ce que l'article ne fait pas

- **Sabotage diffus : écarté par construction.** Le scénario dont la tâche cachée est une proportion sur l'épisode est exclu, « because its side task is a proportion of bookings over the episode, not a discrete action, so its steps cannot be labeled one at a time » (F4-24, p. 34) ; et « The other 11 private scenarios, left out by hand, have side-task steps that are difficult to label one step at a time. » (F4-25, p. 34). Douze scénarios sur 26 sortent donc parce que le sabotage ne se lit pas étape par étape. BashArena n'a que quatre tâches cachées à action discrète et à cible fixe.
- **Tâches floues : non.** Tâches à vérité d'exécution (tests, état final du conteneur).
- **Agrégation sur la trajectoire : aucune.** Un score par étape ; ni maximum, ni somme, ni règle d'arrêt, ni verdict par épisode. Recherche par mots-clés dans les 119 pages (« episode-level », « per-episode », « cumulat », « sequential », « max over ») : rien d'autre que des décomptes. La seule agrégation est interne à la sonde, sur les jetons et les couches du dernier tour.
- **Seuil hors échantillon : non** (F4-07) ; faux positifs « égaux » par construction, pas en déploiement.
- **Moniteur lisant le raisonnement : non** (F4-23).
- **Adversaire adapté à la sonde, conscience d'évaluation : non** (aucune occurrence de « evaluation awareness » ; « adaptive » n'apparaît que pour l'optimiseur).

### 2.4 Limites reconnues

- « We also saw that false positives may be a challenge for realistic deployments » (F4-12, p. 10).
- Si le dommage vient d'un personnage malveillant, « probing in situations where the scheming persona is not active may not detect any risks » (F4-13, p. 10).
- Un organisme n'est pas détecté (F4-32, p. 10 : 63 %).

### 2.5 Réserves (règle de symétrie : résultat favorable et net, donc audité)

1. **Comparateurs par interface neutralisés par leurs refus.** Opus 5.5 refuse environ la moitié des étapes positives (F4-34, p. 29) ; un refus compté comme suspicion maximale fait qu'aucun seuil n'existe à 1 % (F4-19, p. 26). La figure de tête les écarte (F4-02, p. 1). Le gain à 1 % est donc mesuré contre des moniteurs à poids ouverts ; contre le seul moniteur d'interface qui a un seuil (Sol 6.1 sur Kimi K3), la sonde ne gagne pas (64,5 contre 65,1, F4-16, F4-17).
2. **Le moniteur est privé du raisonnement** (F4-23), alors que l'agent, lui, en garde le souvenir pendant qu'il agit (F4-44, p. 34). La comparaison vaut pour « actions seules ».
3. **Seuils dans l'échantillon** (F4-07), et notes de moniteur discrètes (0 à 100) contre scores continus : les égalités à 100 privent le moniteur de seuil.
4. **Sélection des scénarios après coup.** La v1 l'avouait : « we removed a fixed list of 11 private scenarios after inspecting the step labels of a partial pilot, without a numerical criterion that reproduces the list » (F1-05, v1 p. 21) et « they are not a validated selection rule, and the subset is not shown to give more accurate labels » (F1-08, v1 p. 21). La v4 n'en garde qu'une phrase (F4-25).
5. **Étiquettes fragiles là où elles comptent.** Montré la transcription entière, le juge ne garde que 83 %, 52 % et 91 % de ses étiquettes selon l'échantillon (F4-28, p. 30). Toute étape après le début est positive quelle que soit son étiquette (F4-31) : la sonde est donc créditée quand elle lit l'**état** « j'ai entamé une tâche cachée » que la question de suivi interroge, pas l'action de l'étape.
6. **Fuite textuelle inégale.** « A monitor that reads the transcript therefore has the side task stated outright in many Qwen3.5 and Nemotron-3 episodes and in few Kimi K3 episodes. » (F4-26, p. 41) ; et pourtant c'est sur Kimi K3 que le moniteur d'interface égale la sonde. Les rappels sans la consigne de rappel par tour (F4-42, p. 34) dépendent de ce réglage.
7. **Agents peu compétents sur la tâche principale** : 15,2 % de réussite honnête pour Qwen3.5-397B sur les scénarios notés (F4-27, p. 35).
8. **Instabilité entre versions** (section 3) : le comparateur de tête a changé, ainsi que le mode de calibration et une revendication.

## 3. 2610.12445 : ce qui a changé de la v1 (8 octobre) à la v4 (20 octobre)

| point | v1 (98 pages) | v4 (119 pages) |
|---|---|---|
| titre | « Caught in the Act: Probes Effectively Detect Sabotage… » | « Telling FIBS: Probes Effectively Detect Sabotage… » |
| cadres d'agent | SHADE-Arena seul (0 occurrence de « BashArena ») | SHADE-Arena et **BashArena** (78 occurrences ; annexe E) |
| revendication de tête | « Our probes achieve 98.8% AUC in SHADE-Arena, surpassing an Opus 5.5 text-monitoring baseline » (F1-01, p. 1) ; 0,979 à 0,984 contre 0,960 (F1-02, p. 7) | 98,7 % et 98,0 % contre 97,7 % et 97,6 % pour « the strongest action-only text monitors » (F4-01) ; Opus 5.5 sorti de la figure de tête (F4-02) |
| refus d'Opus 5.5 | « Opus 5.5 refuses on 2,638 of the 5,014 positive steps. » (F1-03, p. 7) | traité en annexe C.4 ; sans seuil à 1 % (F4-19) |
| moniteurs | Opus 5.5 en comparateur de tête, auto-moniteur (Kimi K3 n'y est qu'un agent sondé) | plus Kimi K3 comme moniteur, Haiku 5.5, Sol 6.1, sur trois agents |
| rappel à faux positifs fixés | « Recall at fixed False Positive rate, calibrated against a heldout set of » épisodes honnêtes (F1-04, p. 8) | seuil **dans l'échantillon** (F4-07) ; tableau 6 complet à 1 %, 2 %, 5 % |
| diversité des données | revendiquée : « More diversity also usually improves performance. » (F1-07, p. 8) | retirée ; à taille fixe, effet d'au plus 0,015 (F4-29) |
| bruit d'étiquettes de FIBS | 1,4 % ± 0,1 (F1-06, p. 5) | 0,74 % (F4-35) |
| juge des étapes | Claude Haiku 4.5 ; accord avec un second juge | Claude Haiku 5.5 ; audit à trois vues et arbitrage (annexe C.5) |
| effectifs sur Qwen3.5-397B | 5 014 étapes positives, 16 275 négatives (F1-10, p. 6) | 4 807 positives, 16 896 négatives (F4-43, p. 36 ; calcul : 11 021 + 5 875) |
| choix des 14 scénarios | détaillé, sans critère chiffré (F1-05, F1-08, F1-09) | résumé en une phrase (F4-25) |
| limites | pas de mention des faux positifs | « false positives may be a challenge » (F4-12) |

Ne change pas : la définition (faussetés sues, pas l'intention), la lecture par question de suivi préremplie, l'étiquetage « début puis tout positif », l'absence d'agrégation sur la trajectoire, d'adversaire adapté et de sabotage diffus. **Le verdict contre H1 vaut déjà pour la v1** ; la v4 l'étend (second banc, tableau à faux positifs égaux, plus de moniteurs) et l'affaiblit sur un point (seuil dans l'échantillon).

## 4. 2607.07368v2 — FakeLab (« Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors »), v2 du 12 octobre 2026

Venue imprimée : « Preprint. » avec la liste de contrôle NeurIPS en annexe ; aucune acceptation imprimée.

Ce qui change de la v1 à la v2 :

- **Réplique sur une seconde famille de modèles** : « We repeated the one- versus three-agent comparison with DeepSeek V4 Flash as both planner and executor, keeping the GPT-5 mini monitor. » (K2-01, p. 8) ; la suspicion maximale par séquence passe de 0,877 à 0,765 (K2-02, p. 8, auteurs ; 60 séquences par bras). Portée bornée : « There are no K = 9, no-planner, affordance-restriction, honest-baseline or joint-monitor arms » (K2-04, p. 55). La limite « we tested only one model family » (K1-06, v1 p. 14) devient « most experiments use one model family, with one ablation on DeepSeek V4 Flash » (K2-06, p. 14).
- **Correction** : la v1 disait que le planificateur tournait 20 pas (K1-09, v1 p. 4) ; « This was incorrect: no step limit was applied to the planner, which ran until it submitted its plan. » (K2-03, p. 52). L'ablation du budget de tours est refaite en conséquence.
- Cohorte d'amplification par le planificateur passée de 566 à 789 trajectoires (K2-08, p. 53).

Ce que la v2 **n'ajoute pas** : ni moniteur à état, ni sonde, ni activations, ni état interne. Les décomptes de mots sont identiques entre v1 et v2 (« probe » : 1 et 1, au sens d'explorer ; « activation », « white-box » : 0 et 0 ; « stateful » : 2 et 2). Le seul passage sur un moniteur à état est une remarque de discussion, **déjà dans la v1** (K1-05, v1 p. 29) : « A stateful monitor then inherits the joint monitor’s core problem » (K2-05, p. 29). Le moniteur conjoint reste déclaré non déployable (K2-07, p. 2).

**Verdict H3 et papier B : inchangé** — « occupe en partie », le pendant boîte noire (effet de fragmentation, K = 1, 3, 9) ; la réplique DeepSeek renforce ce pendant à K = 1 et 3. La courbe boîte blanche, la co-élévation d'états internes et le moniteur à état mesuré restent non faits dans cette source.

## 5. 2610.37679v1 — « Exposure Is Not Commitment » (Sinha)

Venue imprimée : atelier « Agents in the Wild » de NeurIPS 2026 (S-11, p. 1).

- **Quelle sonde lit quel modèle.** Sonde (centroïde, puis régression logistique) sur le flux résiduel, couche 20, dernier jeton de décision (S-05, p. 5), de l'agent **victime** d'une injection indirecte (AgentDojo ; Qwen2.5-7B, puis Mistral-7B et OLMo-2-7B), avant l'action. L'attaquant est un tiers : « The attacker controls part of X, but not U , the model weights, or the audit instrumentation. » (S-04, p. 4). Pas de déroulé en direct : « This is not a live rollout, but the label comes from the model’s own action rather than an inserted proxy. » (S-15, p. 7).
- **Ce que la sonde capte.** Entraînée « dangereux contre le reste », elle capte l'**exposition** : les moniteurs « flag exposed trajectories whether or not the agent complies, and barely predict which cases turn unsafe » (S-01, p. 1) ; le même critère se déclenche sur 99 trajectoires attaquées mais sûres sur 99 (S-06, p. 7). Réentraînée sur les seuls cas exposés, elle prédit l'engagement jusqu'à deux étapes avant (S-02, p. 1 ; maximum permis par des trajectoires de trois étapes, S-13) : aire 0,853, **égalée par un classifieur de texte entraîné, 0,855** (S-03, p. 1) ; différence +0,007 [−0,097 ; 0,111] en plis groupés (S-16, p. 13). L'auteur conclut qu'« a weak lexical baseline alone would have overstated the latent advantage » (S-07, p. 7). Le juge sans entraînement (le même modèle interrogé) voit l'exposition mais prédit mal l'obéissance (0,615 ; S-10, p. 8).
- **Attaquant adapté à la sonde : non.** « the attacks are not adaptive: a monitor-aware attacker could suppress the commitment direction or sit below thresholds » (S-08, p. 9) ; « all AUROCs are non-adaptive upper bounds » (S-09, p. 9).
- **Mesure continue du déplacement : non.** Aires sous la courbe et taux de faux positifs à 90 % de rappel (0,343 pour la sonde, 0,394 pour le texte ; S-12, p. 13) ; coût en fausses alertes sur trafic propre non mesuré (S-14, p. 14).
- **Réserves.** 141 positifs sur une grille, deux suites sans aucun cas ; choix du moniteur principal fait après coup, dit par l'auteur ; un seul banc.

Verdicts : **HC2 voisin** (même position de sonde que MIRAGE : agent victime ; ni agent auteur, ni adversaire adapté, ni g) ; **HC2b voisin, utile au contrôle** (le score monte avec l'exposition, que l'agent obéisse ou non : il faut séparer « tente de manipuler » de « a du contenu manipulateur sous les yeux ») ; **H1 contre-indice faible** (à entraînement égal, le texte égale la sonde avant l'action ; ni sabotage, ni faux positifs égaux) ; **H8 voisin** (le construit lu — exposition ou engagement — dépend du contraste d'entraînement et de la population ; robustesse adverse non mesurée).

## 6. 2611.11172v1 — « Do Benign-Trained Hidden-State Probes Detect Tool Errors Under Adversarial Conditions? » (Bhandari et Lingthep)

Venue imprimée : aucune (mise en page de conférence IEEE, sans nom de conférence).

- **Quelle sonde lit quel modèle.** Régression logistique par étape sur la dernière couche, au dernier jeton de la consigne avant l'appel d'outil (B-03, p. 3), de l'agent **victime** (AgentDojo ; Qwen2.5-7B, Qwen2.5-14B, GLM-4.6V-Flash), entraînée sur des trajectoires bénignes seulement (B-01, p. 1) ; évaluation hors ligne (B-09, p. 2).
- **Ce que la sonde vise.** La **justesse opérationnelle** de l'appel d'outil, pas l'injection ni l'intention ; les auteurs séparent : « exposure detection and action-correctness detection must not be confused » (B-05, p. 5).
- **Résultat (auteurs).** La sonde ne bat pas trois mesures d'incertitude tirées des probabilités de sortie ; sous la condition « system override », Qwen2.5-14B : 0,431 contre 0,758 pour l'entropie (B-04, p. 3) ; six différences significatives après correction, toutes dans ce sens (B-02, p. 1 ; B-08, p. 4).
- **Attaquant adapté à la sonde : non. Mesure continue du déplacement : non** (aires par condition, pas de déplacement apparié).
- **Limites reconnues** : un seul banc, 1 027 enregistrements d'entraînement pour trois modèles (B-07, p. 3), 9,3 % de prédictions par repli ; « the above results should not be generalized to natural language hallucinations or agent safety issues » (B-06, p. 6).
- **Réserve.** Sonde très peu entraînée, dernière couche seule : résultat négatif peu opposable ; une aire de 0,431, sous le hasard, signale un classement inversé hors distribution plutôt qu'une absence de signal.

Verdicts : **HC2 ne touche pas** (voisin lointain : agent victime, cible « erreur d'outil ») ; **HC2b ne touche pas** ; **H1 contre-indice faible** (une sonde entraînée en bénin, lue avant l'action, est battue par des signaux de sortie sous condition adverse ; hors sabotage) ; **H8 voisin lointain**.

## 7. 2610.18408v1 — « Prompt-Injection Probes Learn the Conversation, Not Just the Injection » (Kale et Vishwanath)

Venue imprimée : aucune (mise en page ACL).

- **Quelle sonde lit quel modèle.** Sonde linéaire par couche sur l'état caché de l'agent qui vient de lire une sortie d'outil, « at the last token before the agent’s reply begins » (L-03, p. 3) ; six modèles ouverts (Qwen3-8B à Gemma-4-31B), AgentDojo. L'agent est le **lecteur et la victime** ; l'étiquette est l'exposition : « A moment is positive if the agent has just read a tool output that contains injected text, and negative otherwise. » (L-13, p. 1) et « Our labels mark exposure to injected text, not whether the agent obeys it. » (L-04, p. 8).
- **Ce que la sonde capte.** Des **corrélats de surface** : « conversation position and text lengths alone reach 0.91–0.98 AUROC » (L-01, p. 1) sans le modèle ; au seuil par défaut, les sondes standard signalent la plupart des jumeaux propres, 80 % et 70 % en médiane (L-07, p. 5), et presque tous les sosies inoffensifs. Avec des négatifs appariés à l'entraînement, les fausses alertes tombent « from 41–80% to 4–27%, and on harmless look-alikes from 92–98% to 3–16% » (L-02, p. 1), et 95 % des attaques réussies restent arrêtées contre 79 % (L-11, p. 7).
- **Plan apparié : oui, côté lecteur.** Cinq cas au même moment de la même tâche (attaque, attaque en texte nu, jumeau propre, sosie au même format, consigne inoffensive) ; dans 85 à 89 % des paires, la consigne ne diffère que par le texte injecté (L-10, p. 12).
- **Mesure continue du déplacement : non.** Taux de signalement à trois seuils et aire « attaque contre jumeau » ; pas de déplacement du score en fonction d'une intensité, pas de cible, pas de juge sous la même attaque.
- **Attaquant adapté à la sonde : non**, dit deux fois (L-06, p. 3 ; L-05, p. 8).
- **Comparateur texte.** Un classifieur de texte entraîné sur les mêmes données fait aussi bien ou mieux sur les attaques d'AgentDojo (L-08, p. 8) ; l'avantage revendiqué de la sonde est le coût, le texte nu et le transfert du seuil.
- **À noter.** L'article cite un usage en production : « Anthropic runs prompt-injection probes on tool outputs across many of its products (Anthropic, 2026) » (L-09, p. 1) — affirmation des auteurs, non vérifiée ici.
- **Limites reconnues** : un banc ; comptes d'attaquant réutilisés (L-12, p. 8) ; pas de correction pour comparaisons multiples.

Verdicts : **HC2 voisin** (sonde du lecteur et de la victime ; à joindre au bras « sonde du lecteur » de N-013, section 8 : une sonde lectrice suit la position, la longueur et le format) ; **HC2b voisin, précédent direct pour le contrôle obligatoire du style** (le sosie — même format, contenu inoffensif — est le patron du contrôle « style égal, intention différente », et les sondes standard y échouent) ; **H1 contre-indice faible** (le texte égale la sonde ; hors sabotage) ; **H8 voisin** (ce que la sonde lit prédit ses fausses alertes ; robustesse adverse non mesurée).

## 8. 2606.12618v2 — « “Did you lie?” Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms » (Cooney, Africa, Irving ; institut britannique de sécurité de l'intelligence artificielle)

Venue imprimée : aucune (version 2 du 17 juin 2026).

- **Ce qu'il fait.** Quatre détecteurs de mensonge : un juge lisant le raisonnement (boîte noire, GPT-5.5 Pro ; C-06, p. 8), un classifieur sur les probabilités de réponses à des questions sans rapport, deux sondes d'activations (celle d'Apollo, et « Did-You-Lie », entraînée sur la réponse à « as-tu menti ? »). Deux régimes : mensonge sur consigne (31 modèles ouverts, de 2 à 1 000 milliards de paramètres) et 13 organismes entraînés à mentir, dont la croyance est vérifiée dans le raisonnement.
- **Résultats (auteurs).** Sur consigne, les quatre détecteurs s'améliorent avec la capacité (corrélation de rang de 0,41 à 0,71 ; C-03, p. 10). Sur les organismes entraînés : « Median balanced accuracy falls from 0.85 to 0.52 for Apollo, from 0.81 to 0.65 for DYL, and from 0.85 to 0.50 for Unrelated Qs. » (C-02, p. 11) ; seul le juge tient, à 0,82 (C-01, p. 1). La sonde « Did-You-Lie » tient sur la variante par consigne des mêmes comportements, ce qui impute la chute à l'entraînement (C-10, p. 11) ; les deux autres échouent même par consigne (C-15, p. 11).
- **Ce qu'il ne fait pas.** Pas d'agent ni de sabotage ; pas de taux de faux positifs égal sur la tâche (seuils calibrés à 1 % de positifs sur un corpus tiers, C-07, p. 8 ; juge à note fixe) ; pas de pression adverse sur les détecteurs (C-04, p. 4 ; C-05, p. 12) ; la conscience d'évaluation n'est nommée que comme difficulté (C-12, p. 4) ; l'échelle n'est étudiée que sur consigne (C-13, p. 12).
- **Limites reconnues et réserves.** L'avantage du juge est en partie un artefact : « The CoT judge’s strong performance is partly an artefact of selection » (C-09, p. 10). Organismes sur deux modèles voisins. L'article corrige un précédent : après correction de la calibration du seuil, le rappel de la sonde d'Apollo « on the Roleplaying dataset falls from 96% to 73.2% » (C-08, p. 22) — **chiffre à reporter avant toute citation du rappel de 96 % à 1 % de faux positifs de Goldowsky-Dill et collègues** (non vérifié ici sur leur code).
- **Lien avec 2610.12445v4.** FAR.AI reprend sept de ces organismes et y obtient des aires élevées avec des sondes entraînées sur FIBS ; l'organisme saboteur en mathématiques reste manqué (F4-32). Les deux articles divergent donc sur les mêmes organismes ; la différence (données d'entraînement, architecture, question de suivi, métrique) n'est pas démêlée par les sources.

Verdicts : **H1 voisin, contre-indice faible** (sondes sous un juge boîte noire lisant le raisonnement, sur mensonge entraîné ; ni agent, ni sabotage, ni faux positifs égaux ; juge avantagé par construction) ; **H8 voisin** (la validité du banc — le modèle croit-il le contraire de ce qu'il dit ? — conditionne la lecture des détecteurs ; la « faible espérance » admet un détecteur qui capte « something correlated with lying — such as general misbehaviour — rather than lying itself », C-11, p. 3 ; aucune robustesse adverse prédite par le construit) ; **H2 ne touche pas**.

## 9. 2606.30449v1 — « Internal-State Probes Read the Situation, Not the Action: Three Negative Results for Pre-Action Misalignment Monitoring » (Fomin, David, LeVi)

Venue imprimée : « Published at the Second Workshop on Agents in the Wild: Safety, Security, and Beyond (AIWILD) at ICML 2026. » (M-01, p. 1).

- **Ce qu'il fait.** Trois familles de lecture interne, évaluées **avant** l'action :
  1. une direction « modèle affiné non sûr moins modèle de base » (Qwen2.5-Coder-32B) : aire de 1,000 sur le contraste de construction, mais seuil franchi sur 0 contexte sur 143 et 0 ligne sur 342 (M-02, p. 1) ; 17 scénarios audités, 11 avec comportement désaligné (M-10, p. 5) ;
  2. des sondes au dernier jeton d'une réponse préremplie (Llama-3.1-8B ; 500 exemples de conseil médical, juridique, de sécurité, M-13, p. 4) : aire 0,801 et +5,1 points sur la classe majoritaire (M-03, p. 1), transfert entre domaines nul ou négatif, alors que le domaine du texte se décode à 0,999 (M-06, p. 6) ;
  3. des vecteurs d'émotion (Gemma-3-27B) dans un scénario de chantage : pilotage non spécifique (des directions « chats », « météo » déplacent aussi les taux), et sonde de pont à 0,632 au mieux (M-07, p. 8).
- **Ce qu'il ne fait pas.** Aucun moniteur boîte noire comparé ; aucun taux de faux positifs fixé ; pas de sabotage sur instruction ni de tâche cachée ; pas d'agrégation sur la trajectoire ; pas d'attaquant.
- **Limites reconnues.** Portée dite : « we do not show that no internal pre-action signal exists, only that these natural probe families do not yield a robust one under the tests we ran » (M-04, p. 2). **Les moniteurs à agrégation temporelle sont laissés ouverts** : l'évidence porte « more directly on lightweight probe formulations (linear and shallow-MLP readouts) than on richer representation-learning or temporal-aggregation monitors » (M-05, p. 8), et « sequence-level probes, larger nonlinear classifiers, and probes trained directly across many tool-action scenarios remain open » (M-12, p. 8). (Limite d'un article, pas trou du champ.)
- **Réserves (symétrie : négatifs nets).** Le résultat 1 teste une direction de **population** (modèle affiné contre base) sur un autre construit (désalignement en contexte du modèle de base) : 0 sur 143 n'est pas un échec de sonde d'action. Le résultat 2 est du texte continué, non de l'action d'outil, ce que les auteurs disent (M-11, p. 5) ; trois des six transferts « nuls » sont dégénérés (M-08, p. 6). 2610.37679 propose une explication concurrente (contraste d'entraînement), sans rejouer leurs données.

Verdicts : **H1 voisin ; contre-indice de portée** (des sondes légères lues avant l'action portent peu de signal d'action et beaucoup de signal de situation ; aucun comparateur boîte noire, donc ni gain ni perte mesurés) ; **H8 voisin** (thèse proche de la prémisse de H8 : « A hidden-state classifier can predict within one domain while mainly tracking prompt content. », M-09, p. 8 — le construit lu, situation contre action, explique l'échec de transfert ; mais transfert de domaine, pas robustesse adverse, et pas l'axe intention contre conscience d'évaluation) ; **H2 voisin faible** (nomme l'agrégation temporelle comme non testée).

## 10. Verdicts

### 10.1 Tableau par article et par énoncé

| source | H1 | H2 | H8 | HC2 | HC2b | H3 |
|---|---|---|---|---|---|---|
| 2610.12445v4 (et v1) | **occupée en partie** | voisin | voisin | ne touche pas | ne touche pas | ne touche pas |
| 2607.07368v2 | ne touche pas | voisin (inchangé) | ne touche pas | ne touche pas | ne touche pas | **occupe en partie, inchangé** (pendant boîte noire) |
| 2610.37679v1 | contre-indice faible | ne touche pas | voisin | voisin | voisin ; utile au contrôle | ne touche pas |
| 2611.11172v1 | contre-indice faible | ne touche pas | voisin lointain | ne touche pas | ne touche pas | ne touche pas |
| 2610.18408v1 | contre-indice faible | ne touche pas | voisin | voisin (versant lecteur) | voisin ; précédent du contrôle du style | ne touche pas |
| 2606.12618v2 | voisin ; contre-indice faible | ne touche pas | voisin | ne touche pas | ne touche pas | ne touche pas |
| 2606.30449v1 | voisin ; contre-indice de portée | voisin faible | voisin | ne touche pas | ne touche pas | ne touche pas |

### 10.2 H1 — composante par composante, pour 2610.12445v4

| composante de H1 | fait ? |
|---|---|
| moniteur fondé sur les activations de l'agent qui agit | oui (quatre architectures, lecture après chaque appel d'outil) |
| contre moniteur boîte noire | oui, mais moniteurs privés du raisonnement (F4-23) ; moniteurs d'interface sans seuil à 1 % (F4-19) |
| sabotage d'agent en politique propre | oui (tâches cachées sur instruction, SHADE-Arena et BashArena) |
| taux de faux positifs égal | oui à 1 %, 2 %, 5 %, **seuil dans l'échantillon** (F4-07) ; négatifs : épisodes honnêtes des mêmes tâches et étapes d'avant le début |
| agrégation égale | sans objet : un score par étape des deux côtés ; le moniteur lit la transcription jusqu'à l'étape, la sonde lit le contexte du modèle |
| sabotage **diffus** | **non, écarté** (F4-24, F4-25) |
| tâches **floues** | non |
| agrégation sur la trajectoire | non |

- **Verdict d'ensemble H1 : occupée en partie.** Le programme tenait déjà le gain « en général » pour établi ; il l'est maintenant aussi **sur du sabotage d'agent à 1 % de faux positifs**, par étape, pour des actions discrètes.
- **Reste revendicable (proposition ; la décision revient à Lazar)** :
  > La mesure du gain des activations sur la boîte noire, à taux de faux positifs égal **calibré hors échantillon** et **à agrégation égale sur la trajectoire**, sur du sabotage **diffus** de tâches **floues**, c'est-à-dire là où aucune étape prise seule n'est étiquetable — la classe de scénarios que 2610.12445 écarte (p. 34) —, contre des moniteurs boîte noire qui lisent tout ce qu'un moniteur déployé lirait, et sans question de suivi préremplie si la sonde est lue passivement.
  > Cité comme publié : sondes devant des moniteurs « actions seules » à 1 % de faux positifs par étape sur SHADE-Arena et BashArena (2610.12445v4, p. 8, 26, 28), avec les réserves de la section 2.5 ; égalité avec le meilleur moniteur d'interface sur un agent (p. 26).
- **Contre-indices à ajouter à la liste de H1** : 2610.37679 (à entraînement égal, le texte égale la sonde avant l'action, p. 1, 7, 13) ; 2610.18408 (p. 8) ; 2611.11172 (p. 3, 4) ; 2606.12618 (p. 11) ; 2606.30449 (portée, p. 1, 8). Tous faibles : aucun ne porte sur du sabotage à faux positifs égaux.
- **Conséquence pratique pour G1.** 2610.12445 fournit une base boîte blanche publiée à battre ou à reproduire : la sonde lue sur une question de suivi préremplie après chaque action (« dernier état » interrogé). Elle recoupe la base (iii) « dernier état » de N-056 ; à trancher par Lazar si elle doit entrer nommément dans les bases — je ne propose rien dans la liste scellée (N-061).

### 10.3 H2

- 2610.12445v4 : **voisin**. Aucune accumulation de scores entre actions ; mais deux faits à citer : (a) la lecture par question de suivi fait porter la mémoire de la trajectoire par le contexte du modèle lui-même (toute étape après le début est positive, F4-06) ; (b) les scénarios où « chaque étape reste sous le seuil » sont exactement ceux que l'article écarte (F4-24, F4-25). 2606.30449 nomme l'agrégation temporelle comme non testée (M-05).
- **Verdict d'ensemble H2 : inchangé** dans ce lot (rien trouvé qui accumule des scores de sondes sur la trajectoire).

### 10.4 H8

- Quatre sources de ce lot établissent, chacune sur son terrain, que **ce que la sonde lit réellement prédit où elle échoue** : situation contre action (2606.30449, transfert de domaine) ; exposition contre engagement (2610.37679, population et contraste d'entraînement) ; position, longueur et format contre injection (2610.18408, fausses alertes) ; croyance du personnage actif contre but instillé (2610.12445v4, p. 10 ; 2606.12618, validité des organismes). **Aucune ne mesure une robustesse adverse**, et aucune ne porte sur l'axe intention contre conscience d'évaluation.
- **Verdict d'ensemble H8 : voisins multiples, aucune occupation nouvelle.** La ligne « reste revendicable » tient ; sa prémisse (« le glissement de construit est déjà décrit ») est renforcée et **le lien construit → généralisation ou fausses alertes est publié** : seule la prédiction de la robustesse **adverse** reste à revendiquer.

### 10.5 HC2 et HC2b

| question de la consigne | 2610.37679 | 2611.11172 | 2610.18408 |
|---|---|---|---|
| modèle lu | agent victime, avant l'action | agent victime, avant l'appel d'outil | agent lecteur et victime, juste après la sortie d'outil |
| ce que la sonde capte | exposition (contraste naïf) ; engagement si réentraînée sur les cas exposés | justesse de l'appel d'outil (mal) | exposition, et d'abord position, longueur, format |
| attaquant adapté à la sonde | non (S-08) | non | non (L-05, L-06) |
| mesure continue du déplacement | non | non | non (plan apparié, mais taux et aires) |
| juge sous la même attaque | non (auto-prévision du même modèle) | non | non (classifieur de texte) |

- **Verdict d'ensemble HC2 : occupée en partie, inchangé** (par MIRAGE, rapport du lot 1) ; aucune des trois sources ne lit un agent auteur et adversaire, n'oppose un attaquant adapté, ni ne mesure g.
- **Ajustement proposé à la formulation du lot 1** : le « plan apparié » n'est pas en soi une pièce neuve — 2610.18408 l'emploie pour des sondes d'exposition (jumeau propre, sosie, p. 4, 12). Ce qui reste propre à HC2 : l'agent **auteur**, le déplacement **continu** en fonction de l'intensité, et la comparaison aux **juges génératifs sous les mêmes attaques**.
- **HC2b : reste revendicable, inchangé.** À joindre au contrôle obligatoire du style : le sosie inoffensif de 2610.18408 (p. 1, 4) et la séparation exposition contre engagement de 2610.37679 (p. 1, 7) ; le bras EC.2 doit distinguer « l'agent tente de manipuler » de « le contexte de l'agent contient un texte manipulateur ».

### 10.6 H3

- **Inchangé** : 2607.07368v2 reste le pendant boîte noire ; ni moniteur à état mesuré, ni sonde.

## 11. Pages clés

- 2610.12445v4 : 1 (résumé, figure de tête), 2 et 3 (définition, moniteurs « actions seules »), 5 et 6 (lecture par question de suivi, étiquettes), 8 (résultats, seuil dans l'échantillon), 10 (limites), 25 (étiquettes), **26 (tableau 6)**, 27 à 29 (moniteurs, refus, tableau 9), 30 à 33 (audit des étiquettes), **34 (scénarios écartés)**, 35 et 36 (réussite des tâches, cohortes), 37 (diversité), 39 à 41 (BashArena, fuite textuelle).
- 2610.12445v1 : 1, 5 à 8, 21.
- 2607.07368v2 : 8, 14, 29, 52, 53, 55.
- 2610.37679v1 : 1, 4, 5, 7, 8, 9, 13, 14.
- 2611.11172v1 : 1, 3, 4, 5, 6.
- 2610.18408v1 : 1, 3, 4, 5, 7, 8, 12.
- 2606.12618v2 : 1, 3, 4, 8, 10, 11, 12, 22.
- 2606.30449v1 : 1, 2, 4, 5, 6, 8.

## 12. Pistes non lues, vues dans les bibliographies (questions, pas verdicts)

- 2607.06503 (Ruan et collègues, arrêt précoce d'épisodes d'agent par une cascade de sondes à rappel contrôlé) — à lire contre H2 et contre la base « cascade » de N-056.
- 2606.04141 (Chauhan et Revankar, détection avant la sortie et sur plusieurs tours de l'exfiltration d'identifiants) — contre H2 et HC2.
- 2609.19101 (Bergen et collègues, états internes et tricherie sur la récompense pendant des évaluations) — contre H1.
- 2610.05295 (Yu et collègues, traçage causal de l'injection indirecte) et 2608.27750 (Yeats et collègues, sondes d'erreurs d'appel d'outil) — contre HC2, versant lecteur.
- Je n'ai ouvert aucun de ces articles ; je ne sais pas s'ils sont déjà au dépôt.

## 13. Contrôle des citations

- Script : `controle_citations.py`, lancé par `python3 -I` ; liste : `citations.json` (identifiant, PDF, page, citation) ; journaux : `journal-autotest.txt`, `journal-controle.txt`.
- Autotest : cas juste trouvé ; cas altéré (un mot retiré) rejeté ; cas juste sur une mauvaise page rejeté.
- **Citations contrôlées : 131. Échecs : 0.** Un échec au premier passage (F4-27, phrase reconstituée de mémoire, introuvable), remplacé par la ligne du tableau 13.
- Normalisation : ligatures (NFKC), guillemets et tirets unifiés, traits d'union et espaces retirés ; les lignes de tableau sont citées telles que l'extraction les rend.
- Limites du contrôle : il vérifie la présence littérale d'une citation sur sa page, pas la justesse de mon interprétation ; le retrait des traits d'union rend le contrôle insensible à une différence de trait d'union. Les titres d'articles entre guillemets ne sont pas des citations contrôlées. Une citation de la liste (C-14, p. 11 de 2606.12618 : le meilleur détecteur hors raisonnement plafonne à 0,91 d'exactitude équilibrée sur un modèle) est contrôlée sans être reprise dans le texte ; plusieurs autres (par exemple F4-11, F4-20) ne sont reprises que par leur identifiant ou en paraphrase.

## 14. Refus

Aucun refus de permission ni de classifieur. Aucune commande git, aucun appel réseau, aucun appel de modèle, aucune recherche récursive dans le dépôt.

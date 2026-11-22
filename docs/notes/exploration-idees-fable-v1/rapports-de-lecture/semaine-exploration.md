# Huit prépublications arXiv (15-19 novembre 2026) : exploration guidée contre hasard et meilleur de n

J'ai lu les huit PDF en entier (pour 2611.23068, 38 pages, les annexes seulement sur les points demandés). Ils sont dans `/tmp/claude-0/-home-user-controle-ia-travail/7225ef84-cf06-5367-97a0-6c2a4e600e2b/scratchpad/sources/semaine-exploration/`. Les dates viennent de la page abs : ligne « Submitted on » et historique [v1]. Les pages citées sont celles du fichier PDF.

| Identifiant | sha256 du PDF |
|---|---|
| 2611.19841 | 0b1d98a624fc23bb4d9863da19b5b349c46020a37a86c514baa0d7064853dd20 |
| 2611.23068 | 3ee67c72ccbf3a3a65a5018a79de074fa0319ca617bd2e77251d573be2782bcd |
| 2611.25896 | 5f6e9a013e8489f520a6b0add8f0e3496017f294cef81263d529836b0e941a81 |
| 2611.22605 | bc5d57bf11140a3a210dd3754383de76d3d7625e01059e8877e0c9e6ca6ed5e5 |
| 2611.22661 | 7048c0fb8d883da4c46c9e2affea5ef6e5b82793a6ea2e0a96fdce415f9a100d |
| 2611.25557 | bb3739a59b89952073826559f8ce8e6cdd80b9c33c63c4ba143d413c2b8b94f1 |
| 2611.21859 | 677f99af6d67d0ed4ef0130b61232db2fe940d812fa24abd5b484d02b5d7589a |
| 2611.26011 | 2d0d50a217a10ab5bb3c145e09a329507136286589a82fa6fdca192af3ed7a19 |

## 1. 2611.19841 — Hu Cang, « Asking the right question is key to AI discovery in a chain of hypotheses » (cs.AI)
- **Dépôt et auteur.** « Submitted on 15 Nov 2026 », [v1] 06:43:31 UTC. Auteur unique, Developmental and Cell Biology, UC Irvine (p. 1). Aucun code ni aucune donnée publiés.
- **Dispositif (simulé).** La loi est y = V·x1/(K+x1)·1/(1+x2/J) + A·exp(−(x2−c)²/2S²) + ε, avec un bruit σ = 0,08 ; x3 n'a aucun effet (p. 6).
  - La région du pic W = (c−0,35 ; c+0,35] couvre **7 % de l'étendue de x2**. À x1 = 40, le pic monte jusqu'à 31σ dans W et reste sous 2σ hors de W.
  - Sans le pic, la courbe lisse exacte donne E = 3,9-4,8. Le critère de réussite est E = RMSE/σ ≤ 1,05 (p. 6).
- **Budget.** 12 tours de 2 conditions, chacune mesurée deux fois ; 4 conditions de départ prises hors de W (p. 6-7).
  - 32 essais appariés : mêmes données de départ et même graine de bruit pour les deux agents ; 23 des W contiennent un entier, 9 non (p. 6).
  - 32 essais de plus pour Sonnet seul.
- **Procédé.** Claude Sonnet 5.5 ou GPT-6.1-Sol, en effort élevé et sans code (p. 7), voit les mesures et jusqu'à 12 équations classées par le critère d'information bayésien. Il propose au plus 3 équations et choisit 2 conditions.
- **Références, à budget égal en nombre de conditions.**
  - Le hasard est **calculé, non exécuté** : 1−(1−0,07)^(2k), soit 58 % au tour 6 et 82 % au tour 12 (p. 7).
  - La bissection sur x2 utilise « prior knowledge of which variable carries the peak » (p. 3) : 32/32 au tour 12.
- **Chiffres (p. 3).**
  - Entrée dans W : Sonnet 19/32 (59 %), GPT 1/32 (3 %). Les deux agents sont sous le hasard dès le tour 6 (p = 0,002 et p = 8×10⁻¹³).
  - Essais résolus : 7/32 contre 0/32 (p = 0,016).
  - Avant l'entrée dans W, le désaccord maximal des trois meilleures équations tombe près de x2 ≤ 1 dans 78 % et 64 % des tours, et dans W dans 0,8 % et 2,0 % des tours.
  - Rapport entre le désaccord au point choisi et le désaccord maximal : médianes 0,92 (GPT) contre 0,48 (Sonnet), p = 9×10⁻¹⁰. L'écart médian entre équations vaut 0,68σ et 1,25σ, soit moins que le bruit d'une mesure.
- **Explication de l'auteur.** Le critère bayésien pénalise un terme de pic tant qu'aucune donnée n'est dans W, et les courbes lisses s'accordent dans la zone non mesurée (p. 3, 5-6). « the agent that followed model disagreement more closely missed the peak in all 32 trials » (p. 1).
- **Ce qui fait réussir (p. 4-5, 32 essais Sonnet entrés dans W).**
  - 11/32 essais résolus.
  - Selon le nombre de positions distinctes mesurées dans W : 3 ou plus, 10/10 ; 2 positions, 1/5 ; 1 position, 0/17 (p = 2×10⁻⁷).
  - Un signal d'au moins 10σ obtenu au tour 9 au plus tard donne 9/11 ; obtenu aux tours 10-12, 0/8.
  - 78 % et 84 % des x2 choisis sont des entiers (p. 7). Sonnet entre dans 19/23 des W qui contiennent un entier et dans 0/9 des autres (p. 5).
  - Le remède proposé (étaler tôt les mesures, puis serrer autour de l'anomalie) n'est pas testé (p. 6).
- **Limites dites.** « a controlled three-variable system without code execution » (p. 6).
- **Ce que l'article ne montre pas.** Une seule loi et un seul type d'anomalie. Une course par essai et par modèle. Aucune consigne d'exploration donnée aux agents. L'avantage de Sonnet tient en partie à l'habitude des entiers.
- **Faiblesses.** Auteur unique, sans code ; 32 essais.

## 2. 2611.23068 — Zeng, Lan, Lu et al. (11 auteurs), « The Resolution Hypothesis: Agent Evolution's Key Is Identifying Improvements » (cs.AI)
- **Dépôt et auteurs.** « Submitted on 17 Nov 2026 ». ShanghaiTech, ByteDance, BIGAI, SUSTech (p. 1). Le matériel sera publié « upon the acceptance » (p. 3).
- **Dispositif.** 7 méthodes, 6 modèles, 4 bancs (p. 4). Au total, 1 030 courses d'évolution, plus de 2,1 millions de trajectoires de test et plus de 10 millions d'appels (p. 3-4).
- **Mesure de l'utilité vraie.** Y(A) = E[Ŷ|A] sur des évaluations répétées. La variance est décomposée en bruit d'évaluation σ² et en écart entre courses τ² (p. 3-4).
  - Dans les réserves de candidats, la qualité est estimée sur les déroulés que le sélecteur n'a pas vus (annexe F.3, p. 32).
  - La vérité vient de l'exécution des tâches.
- **Niveau des méthodes (p. 5).**
  - σ va de 1,0 à 4,5 points ; τ de 0 à 12,3.
  - Plus de 60 % des paires de configurations sont séparées par moins d'un écart-type d'une comparaison à une course.
  - La marge médiane publiée est de 3,4 points (171 résultats, aucun avec sa variance). Pour l'établir, il faudrait de 5 à 23 courses par méthode.
  - Une course par méthode désigne la meilleure méthode 51-73 % du temps, et **33 % sur Terminal-Bench** (le hasard donne 25 %).
  - Sur les gains publiés au-dessus de 3 points, une seule règle ajoutée en reprend 90 % en médiane. Une fois l'évaluation réparée, le gain médian passe de 17,6 à 0,8 point (p. 5-6).
- **Niveau des candidats (Terminal-Bench seul).**
  - Proposer : la qualité du meilleur de K candidats (Quality@K) passe de 49,2 % à 61,8 % de K = 1 à K = 100, soit 3,3 à 3,4 points au-dessus d'un nul à qualité égale. La meilleure compétence partagée gagne 8,3 points (p. 6-7).
  - Sélectionner (Table 1, p. 7) : l'exactitude par paires vaut 49,7 ± 1,9 % sur le score d'exécution, 48,6 ± 2,6 % pour les sélecteurs natifs, et 45,4 à 49,0 % pour les juges.
  - Les régressions forment 30,5 % de la réserve mais 62,1 ± 42,9 % des candidats acceptés. La corrélation de rang vaut 0,054 (p. 8).
  - Le juge est un seul modèle, DeepSeek-V4-Flash (p. 32).
- **Accumulation au fil des tours (p. 8).** Les gains vus dans la boucle atteignent 6,9 à 9,0 points ; à la réévaluation, ils tombent entre +0,4 et −3,2 points. τ² monte jusqu'à 4,2-24,5 points².
- **Remèdes et effet mesuré.**
  - Valider sur 16 déroulés au lieu d'un (16 courses) : le score final moyen passe de 61,4 à 64,4 % et le meilleur artefact de 64,8 à 72,7 %, sans intervalle donné (annexe F.3, p. 33).
  - Mesure de processus : bruit 13 à 57 fois plus faible (Table 13, p. 36), mais c'est « a diagnostic, not a selector » (p. 35). Aucun effet sur la sélection n'est mesuré.
- **Limites dites (p. 10).** Le niveau des candidats ne repose que sur Terminal-Bench v2.1 ; les poids restent figés ; l'évolution de programmes n'est pas couverte.
- **Ce que l'article ne montre pas.** Que la sélection serait vaine en général : le sélecteur ne voit qu'un déroulé par candidat. Aucun sélecteur ne bat le hasard.

## 3. 2611.25896 — Duéñez-Guzmán, Dueñez, Hernandez Sanchez, Sadedin, « The Price of an Explanation… » (cs.AI ; atelier NeurIPS 2026)
- **Dépôt et auteurs.** « Submitted on 19 Nov 2026 ». Gibran.AI et UT San Antonio (p. 1). Pas de code publié.
- **Dispositif.** Les 120 tâches d'évaluation d'ARC-AGI-2, gemini-3.5-flash, un langage dédié de 91 fonctions.
  - Trois bras : réponse seule, programmes échantillonnés, programmes évolués par évolution grammaticale (p. 3-4).
  - La vérité est la sortie de test exacte.
- **Coût d'exiger un programme (Table 1, p. 4).** 93 tâches résolues en réponse seule contre 68 avec programmes.
  - Le budget est **inégal**, au détriment des programmes : 16,7 appels contre 16 au plus (p. 5).
  - Pour 27 des 28 tâches résolues par la seule réponse, un programme reproduisant tous les exemples existait (p. 5).
- **À coût égal (p. 6), sur trois tirages appariés.**
  - À un appel : +9,89 ± 1,26 tâches (p = 0,016).
  - **À deux appels, contre le meilleur de 2 : +9,22 ± 1,40** (+10,0, +6,5, +11,2 ; p = 0,022).
  - En Python libre : +7,56 et +6,11. Sur gemini-3.8-flash : +8,22 ± 0,24 (p. 8).
  - L'évolution seule, sans modèle de langage, ne résout rien (p. 7).
- **Arrêt précoce (p. 6).** La règle : s'arrêter dès qu'on tient deux programmes parfaits aux prédictions distinctes.
  - L'échantillonnage renonce à 10, 23 et 38 % de son budget à B = 4, 8, 16, sans perte (66,3 contre 66,3).
  - Le bras évolué renonce à 15, 36 et 49 %.
  - S'arrêter au premier programme parfait économise 73 % mais coûte dix tâches.
- **Goulot.** « The bottleneck is obtaining an explanation that generalizes, not finding one » (p. 1).
  - 106 tâches ont un programme parfait sur les exemples ; 68 au plus réussissent le test (p. 7).
  - Un classeur appris (AUC 0,95-0,97) ne change rien au-delà du bruit (55,5 ± 0,19), alors qu'il apporte +4,4 sur des tirages indépendants (p. 7).
- **Limites dites (p. 8).** Les appels au modèle pendant la recherche ne dépassent jamais l'écart entre tirages. La mémorisation de l'évaluation publique n'est pas exclue.
- **Ce que l'article ne montre pas.** La comparaison au meilleur de n s'arrête à 1-2 appels. Trois tirages seulement.

## 4. 2611.22605 — Bohe Chen, « Simplicity Goes Far… » (cs.AI)
- **Dépôt et auteur.** « Submitted on 17 Nov 2026 ». Auteur unique, BUPT et Queen Mary (p. 1). Code annoncé (github.com/bhc6/DCPS), non consulté.
- **Contrôle « générer et sélectionner ».** Le générateur est figé et conditionné par des exemples tirés au hasard ; on note sur un sous-ensemble de validation et on garde le meilleur (p. 3-4).
- **Contre StablePrompt (PPO), gemma-7B, trois graines (Table 1, p. 8).**
  - Égalité sur la classification : −0,4 [−2,30 ; +1,97] sur GLUE et +0,4 sur BBII-TC.
  - PPO garde l'avantage sur BBII-Gen (+2,3), MMLU (+1,8) et II à 30 époques (+4,4).
  - À 100 époques, le contrôle rattrape II, mais PPO n'est pas relancé à 100.
  - Coût : environ un tiers (1,35-1,93 $ contre 4,76-5,96 $).
- **Contre GEPA et MIPROv2 (Table 2, p. 9).** Une seule course par cellule.
  - Moyenne 61,14 contre 61,14 sur GPT-4.1-mini, pour 1 761 contre 3 936 déroulés et 7,70 $ contre 11,34 $.
  - Le contrôle gagne IFBench, PUPA et HoVer ; GEPA gagne HotpotQA (+6,00), LiveBench-Math et AIME (Qwen).
  - « offsetting per-task results, not method equivalence » (p. 8).
  - **Le budget n'est pas égal** ; sur HoVer, c'est la course allongée du contrôle (7 068 déroulés) qui est retenue (p. 10).
- **Plus de budget (p. 10).** Sur HotpotQA, 6 120 déroulés réduisent l'écart avec GEPA à 1,33 point. Sur LiveBench-Math, la validation monte et le test baisse (écarts de 20,95 et 13,50). L'écart entre validation et test va de 44 à 45 points sur IFBench (p. 11).
- **Limites dites (p. 12).** « not a statistically resolved ranking ».

## 5. 2611.22661 — Wang, Gan, Hu, Pan, « The Between-Round Decision in Autonomous Research » (BRED)
- **Dépôt et auteurs.** « Submitted on 17 Nov 2026 ». UESTC et Zhejiang (p. 1). Code annoncé, non consulté.
- **La décision entre deux tours (p. 4-5).** Un appel à deepseek-v4-pro par tour lit le meilleur résultat vérifié et le journal.
  - Il choisit : nouvelle ligne depuis la base, extension par un nouveau mécanisme, raffinement, ou arrêt.
  - Des garde-fous sont codés : les derniers 30 % des tours ne permettent que raffiner ou s'arrêter.
  - 10 tours de 3 à 5 candidats.
- **Effet de l'historique, à budget égal (Table 2, p. 8).**
  - Sans historique : 0,4299 (erreur absolue sur ETTh1) et 83,71 % (CIFAR-100).
  - Dernier tour seul : 0,4244 et 84,01 %.
  - Historique complet : 0,4172 et 84,63 %.
  - **Une course par réglage**, et l'on rapporte le maximum de chaque course.
- **Résultats principaux (Table 1, p. 6).** InternAgent relancé avec les mêmes modèles donne 0,4245, 92,78 et 83,44, mais l'égalité de budget avec ce re-run n'est pas établie (annexe D). Sur la détection de la dépression par la voix : 0,6164 ± 0,0166 sur 5 graines hors sélection (p. 7).
- **Systèmes à arbre de recherche.** AIDE, SELA et AI Scientist v2 ne sont **pas relancés** : ils ne sont discutés que dans les travaux connexes (p. 3).
- **Limites dites (p. 9).** Un seul contrôleur ; ablation sur deux tâches ; 3 tâches du banc sur 12.

## 6. 2611.25557 — Karkehabadi, Hassanpour, Banchs, « The Coverage Selection Gap… » (cs.CL ; atelier NeurIPS 2026)
- **Dépôt et auteurs.** « Submitted on 19 Nov 2026 ». UC Davis, Georgia Tech, Intapp, SJSU (p. 1). Pas de code.
- **Dispositif.** Harvey LAB, fusions-acquisitions : 16 tâches de développement et **4 tenues à l'écart**, avec 58-73 critères de référence (p. 6).
  - Cinq processus de génération ; le classement sans référence repose sur la récurrence sémantique locale (p. 4-5).
  - L'équivalence des critères est jugée par **gpt-5.6-sol, le même déploiement que les générateurs**, « no independent human validation » (p. 5, 7).
- **Nouveaux axes contre volume (Table 6, p. 8).**
  - Nouveaux axes : +0,100, +0,090 et +0,060 de rappel.
  - Plus de génération sur les mêmes axes : 0,000, 0,000 et +0,012, soit +0,015 en tout (F1 −0,070).
  - Le budget de chaque modification n'est pas donné, ni si l'ablation porte sur les tâches de développement ou sur les tâches tenues à l'écart.
- **Écart entre couverture et sélection (Tables 3-4, p. 7-8).** Le plafond de la réserve vaut 0,876.
  - À k = 60 : 0,349 sans référence contre 0,876 pour l'ordre glouton qui connaît la référence (52,7 points).
  - À k = 30 : 57,3 points ; à k = 200 : 15,4.
  - Un appel simple à GPT donne 0,782, contre 0,872 pour les cinq processus.
- **Ce que l'article ne montre pas.** L'ordre glouton connaît la réponse : avec k ≈ |R*|, il atteint le plafond par construction. Un seul sélecteur sans référence est essayé.
- **Faiblesses.** n = 4, une graine, un juge de la même lignée que les générateurs.

## 7. 2611.21859 — Medina, Benton, « Diversity Preservation Recovers Transcription Factor Motifs… » (cs.NE)
- **Dépôt et auteurs.** « Submitted on 16 Nov 2026 ». Baylor (p. 1). Pas de code.
- **Dispositif.** 5 jeux ChIP-seq de foie tirés d'ENCODE. Chaque motif est validé contre les 1 595 motifs de HOCOMOCO par TomTom (p. 4, 6).
- **Référence, à budget égal.** Un algorithme élitiste (µ+λ) qui ne diffère que par la sélection des survivants, avec 5 000 × 512 évaluations et **30 graines** (p. 7).
- **Chiffres (Fig. 1, p. 8-9).**
  - La référence n'obtient aucun run réussi (au moins un « best-hit ») sur 30 pour HNF4A, YY1 et JUND ; elle en obtient 16/30 pour RXRA et 30/30 pour CTCF.
  - L'archive en obtient au moins 13/30 partout, et au moins 29/30 sur trois jeux (p ≤ 6,8×10⁻⁴, correction de Holm).
  - L'aptitude moyenne est plus haute dans la référence : c'est le signe de la convergence (Table 2, p. 8).
  - Après déduplication (Table 4, p. 10), l'any-hit de la référence va de 0 à 57 %, contre 47 à 100 % pour l'archive.
- **Conclusion des auteurs.** La diversité est nécessaire quand les concurrents sont nombreux, inutile pour CTCF. L'archive « exposes the presence of competition but does not resolve it » (p. 14).
- **Limites dites.** Un seul algorithme de diversité ; HOCOMOCO dérive peut-être des mêmes données ; MEME tourne en une course.

## 8. 2611.26011 — Carlet, Đurasević, Jakobovic, Manzoni, Mariot, Picek, « A Matter of Representation… » (cs.NE)
- **Dépôt et auteurs.** « Submitted on 19 Nov 2026 » ; le PDF est daté du 20 novembre. Paris 8, Bergen, Zagreb, Trieste, Twente, Radboud (p. 1). Vérification exacte par programme ; 100 courses par configuration.
- **Codage (Table 1, p. 10).**
  - À n = 8, les deux codages réussissent, en 17 évaluations médianes contre 885 et 9 593.
  - À n = 10, le codage par sous-espaces donne 0/100, même avec 90 fois plus d'évaluations. Le codage par ensemble d'étalement sans « ruiner et reconstruire » donne aussi 0/100. Avec les deux : 100/100 (PS⁻) et 74/100 (PS⁺).
- **Glouton redémarré, à temps égal de 300 s (Table 2, p. 11).** Sur PS⁺ à n = 10 :
  - le glouton à anticipation réussit 52/100, contre 23/100 pour la meilleure stratégie d'évolution (p = 4×10⁻⁵) ;
  - sans mutation, l'évolution tombe à 4 et 0 ;
  - initialiser l'évolution par le glouton donne 13.
- **Paysage (p. 11-12).** Le rayon d'évasion vaut surtout 4 sur 14 matrices pour PS⁻ et 7 sur 15 pour PS⁺. À n = 12, rien en 16 courses de 24 h.
- **Variante qualité-diversité (p. 12).** Degré bas obtenu dans 90/100 courses, contre 47 en lexicographique et 27 pour le glouton (n = 8).

## Synthèse

| Article | Comparaison | Budget égal | Vérité | Taille | Goulot désigné |
|---|---|---|---|---|---|
| 19841 | agent contre hasard calculé et bissection | oui | simulateur | 32 essais, 1 course chacun | où proposer de mesurer |
| 23068 | sélection contre hasard | oui (réserves figées) | exécution répétée | 1 030 courses ; candidats sur 1 banc | reconnaître |
| 25896 | évolution contre meilleur de n | à 1-2 appels | test caché | 3 tirages | généraliser |
| 22605 | générer et sélectionner contre optimiseurs lourds | non | banc | 1 graine (composé) | selon la tâche |
| 22661 | avec contre sans historique ; arbres non relancés | oui (ablation) | banc | 1 course par réglage | non tranché |
| 25557 | axes contre volume ; classement contre ordre qui connaît la référence | non dit | juge-modèle | 4 tâches | classer |
| 21859 | archive de diversité contre élitisme | oui | base externe | 30 graines × 5 jeux | sélection des survivants |
| 26011 | codages ; évolution contre glouton | oui (temps) | exacte | 100 courses | représentation |

**Lecture d'ensemble**
1. Les résultats répétés et à budget égal (23068, 21859, 26011, et 25896 en plus petit) placent l'écart dans la sélection, le codage ou la reconnaissance, pas dans le générateur.
2. « Guidé fait pire que le hasard » (19841) repose sur un seul auteur, 32 essais, un hasard calculé et une seule tâche.
3. Le meilleur de n n'est battu (+9,2 ± 1,4 tâches) qu'à 1-2 appels et sur trois tirages.
4. Le goulot de la sélection est relatif au bruit de la mesure (un déroulé, en 23068) ou défini contre un ordre qui connaît la réponse (25557).
5. Des bases simples (un glouton redémarré, générer et sélectionner) égalent ou battent souvent les procédés lourds.
6. BRED et 22605 n'autorisent aucun classement statistique : une course par cellule.

## Non vérifié
- Les dépôts de code et la page de projet annoncés : non consultés.
- 2611.23068 : annexes D, E, F.1-F.2 et I lues en partie seulement.
- 2611.25896 : annexes A-I non lues en détail.
- 2611.22661 : budget du re-run d'InternAgent non trouvé dans le texte.
- 2611.25557 : nature et budget de l'ablation de la Table 6 non précisés par le texte.
- Aucune critique ni réplication publiée n'a été cherchée : ces textes ont moins d'une semaine.

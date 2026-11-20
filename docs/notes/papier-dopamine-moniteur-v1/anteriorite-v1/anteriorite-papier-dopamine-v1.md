# Recherche d'antériorité — les sept briques du bras « papier dopamine » (v1)

- **Date** : 20 novembre 2026, 13:35 UTC (`date -u`). **Auteur** : Claude Fable 5.2, sous-agent de recherche. Pièce de classe C. Aucune dépense, ni commit ni poussée. Rien lu sous les dossiers cloisonnés.
- **Lus en entier** : énoncé (`16b2d9eb…`), synthèse des six avis (`0bb721b3…`), consultation (`afc22a5f…`), dans `docs/notes/papier-dopamine-moniteur-v1/`. **Papier** `docs/sources/pdf/2602.00986v2.pdf` (`da004f53…`) : pages 1 à 3, 6 et 9 relues sur le texte extrait ; le reste repris de la consultation, qui l'a lu en entier.
- **Périmètre cherché** : 37 requêtes de moteur de recherche (en anglais, mode ordinaire), 4 pages web lues, 18 PDF nouveaux versés et scellés, 9 PDF déjà au dépôt relus par mots-clés. Aucune recherche sur Google Scholar, Semantic Scholar, OpenReview ni dans le code de GitHub : voir « Ce que je n'ai pas pu vérifier ».
- **Règle de lecture** : « occupée » = la brique existe ailleurs, à citer ; « partielle » = la forme ou un morceau existe, pas l'emploi exact ; « aucune antériorité trouvée au périmètre » = rien trouvé le 20 novembre 2026 avec les requêtes listées, ce qui n'est pas « nouveau » (R8). Une citation entre guillemets a été lue sur le PDF à la page dite, par extraction de texte page par page (`pdftotext`), pas en image. Les pages web ne sont pas opposables (R7) et sont marquées « page web ».

## Verdict en sept lignes

1. Lecture du papier comme base et covariable d'un bras de détection de sabotage : **partielle**.
2. Somme séquentielle des petits signaux : **partielle** (forme occupée ; non trouvée, mesurée, sur des scores de sondes internes d'un agent).
3. Épreuve d'évasion à compétence constante : **occupée**.
4. Sonde de réussite attendue apprise sur épisodes honnêtes seuls, base à battre, rejouée sur un chiffre publié : **partielle**.
5. Divergence d'un jumeau forcé sur le même début d'épisode : **partielle**.
6. Comparaison au même jalon, avec les seuls fichiers alors disponibles : **occupée** (dans son principe).
7. Sonde réentraînée sans le seuil de 0,3 : **aucune antériorité trouvée au périmètre cherché le 20 novembre 2026**.

Réunion des sept : **aucune antériorité trouvée au périmètre cherché le 20 novembre 2026**.

## PDF versés (18), dans `docs/sources/pdf/`, chacun avec son compagnon `.sha256`

| Fichier | Empreinte (16 premiers signes) | Ce que c'est | Lecture |
|---|---|---|---|
| `2610.05572v1.pdf` | `ce0879a3cc1c0c89` | Difficulté de la tâche contre échec propre à l'exécution, prédiction d'échec d'agents | p. 1 à 9, 14, 15, 18 par mots-clés |
| `2608.27808v1.pdf` | `3fb73b02cc646e0b` | CURA : alarme à somme cumulée sur la télémétrie d'agents | p. 1, 2, 4 |
| `gupta-2026-where-reasoning-models-commit-to-deception-catching-pivots-v1.pdf` | `cf1693b0bce6a703` | Somme cumulée sur une sonde linéaire, chaîne de pensée ; auto-publié, hors arXiv | p. 1 à 6 |
| `2606.12476v3.pdf` | `0412750524774889` | Début d'hallucination comme détection de rupture au plus vite | p. 1, 11, 12 |
| `2607.11317v1.pdf` | `adb4725ed1db2bcd` | Somme cumulée à valeurs e au décodage | résumé et titres |
| `2607.20129v2.pdf` | `1787e8085745f61c` | Surveillance « en forme de somme cumulée » au décodage | p. 1 à 3, 9 par mots-clés |
| `2605.19966v1.pdf` | `ac485f889507d28a` | Somme cumulée sur l'entropie des jetons, invites adverses | p. 1, 2 par mots-clés |
| `2606.19386v2.pdf` | `1384bb585b70d8ae` | Moniteurs d'état et cadence d'agent | p. 1, 6, 8 par mots-clés |
| `2605.13772v1.pdf` | `4a5a89902cb7f744` | Première erreur de raisonnement lue dans la trajectoire des états cachés | p. 1 |
| `2607.24893v2.pdf` | `504d82ab525be78b` | Détecteur sur préfixe, portes dérobées réparties | p. 1 à 3 |
| `2509.10625v3.pdf` | `f0421d8dd919fa5a` | Sonde linéaire de réussite sur la question seule | p. 1 |
| `2604.18419v6.pdf` | `d0ccaf59c81a136f` | Sonde de valeur pour l'abstention en cours de génération | p. 1, 2, 6, 7 |
| `2610.22046v1.pdf` | `c9838194aa7aa583` | Sondes d'états cachés pour localiser le pas fautif | p. 1 à 3 |
| `2608.29685v1.pdf` | `096745d062bf9ba4` | Incertitude précoce et échec des agents à long horizon | p. 1 seulement |
| `2509.12886v1.pdf` | `0e9eb519756c9275` | Difficulté perçue lue dans les états cachés | titre seulement |
| `2606.30449v1.pdf` | `775abf11ef24188e` | Les sondes lisent la situation, pas l'action | p. 1, 3 à 5 par mots-clés |
| `2610.03960v1.pdf` | `5c9e59e53c12d744` | Divergence par position entre modèle affiné et modèle de base, même contexte | p. 1 à 4 |
| `2510.13900v3.pdf` | `e90e7757b2511ff9` | Différences d'activations entre modèle affiné et modèle de base | p. 1 |

Déjà au dépôt et relus par mots-clés : `2610.12445v1.pdf` (`7e1417580c4ee269`), `2610.04575v1.pdf` (`ef50ec541464c3ee`), `2606.10456v2.pdf` (`aaeedd1e7a88203e`), `2512.07810v1.pdf` (`77e64bcd88754f50`), `2512.11949v1.pdf` (`e0f8ddfff6e75d83`), `2506.14261v4.pdf` (`4b0960622664e77d`), `2412.09565v2.pdf` (`9c23a613c5c7e3a2`), `2504.10374v1.pdf` (`5f802d679344fe5e`), `2605.18549v1.pdf`.

---

## Brique 1 — la lecture du papier (réussite attendue, surprise par étape) comme base et covariable, dans un bras rapporté

**Requêtes.** « "Sparse Reward Subsystem in Large Language Models" value neurons dopamine neurons replication OR monitoring OR sabotage OR deception » ; « "Sparse Reward Subsystem" … openreview review OR critique OR "fails to replicate" OR follow-up … safety OR sandbagging OR "reward hacking" » ; « temporal difference error probe LLM hidden states value function probe … "reward prediction error" language model 2026 » ; « white-box monitor sandbagging cannot distinguish from honest errors task difficulty confound deception probe "honest mistakes" probe control baseline correctness » ; « regress out task difficulty covariate from probe scores variance reduction monitor false positive rate deception probe calibration difficulty-adjusted » ; « value probe OR "success probe" OR "confidence probe" hidden states detects sandbagging OR sabotage … correctness dissociation 2026 » ; « hidden-state probe monitor agent sabotage baseline "success prediction" OR "outcome prediction" confound "probe detects failure" not intent … ».

| Source | Ce qu'elle occupe | Page et citation |
|---|---|---|
| Xu, Yuksekgonul, Zou, arXiv 2602.00986v2 (annoncé à NeurIPS 2026 d'après le moteur de recherche, non vérifié) | La lecture elle-même. Aucun cadre adverse. | p. 1 : « value neurons serve as effective predictors of model confidence, and dopamine neurons can function as a process reward model (PRM) to guide inference-time search » |
| EsfandyariDoulabi et al., arXiv 2610.05572v1 | La séparation « difficulté de la tâche » contre « signal propre à l'exécution », sondes d'états cachés comprises. Sans sabotage : les mots sabotage, adversaire, tromperie sont absents du texte extrait. | p. 1 : « predictors that never observe the current run can achieve high pooled performance, including a difficulty oracle with AUROC up to 0.945, while remaining at chance within task » ; p. 1 : « early run-level discrimination is consistently weak across trajectory predictors, published and released monitors, and hidden-state probes » |
| Subhnil et al., arXiv 2610.22046v1 | Sonde de justesse et sonde de valeur apprise sur des taux de continuations, comparées à une base sans états cachés. | p. 1 : « compare each probe with the strongest baseline that uses no hidden states » ; p. 1 : « no single tested probe locates the failing step more accurately than a rule based only on trace length » |
| Institut britannique, « White Box Control at UK AISI – Update on Sandbagging Investigations », 10 juillet 2025 (page web) | Le constat que la sonde de tromperie lit aussi l'erreur. | Page web, non opposable : « the probe picking up both "deceptiveness" (as in intent) and also "wrongness" » |
| Taylor et al., arXiv 2512.07810v1 (au dépôt) | Sondes de tromperie avec faux positifs sur modèles bénins. | Résumé rapporté par l'état de l'art v1 ; relu ici pour la brique 5 seulement |

**Verdict : partielle.** Les deux morceaux existent séparément : une lecture interne de la réussite attendue, et l'avertissement que la difficulté et l'erreur honnête contaminent les prédicteurs d'échec et les sondes de tromperie. Aucune source trouvée n'emploie la lecture de Xu et al. dans un cadre de surveillance, de sabotage ou de retenue volontaire, et aucune ne retire d'un score de sonde d'intention la part expliquée par une sonde de réussite attendue. Pour ces deux emplois : aucune antériorité trouvée au périmètre cherché le 20 novembre 2026. Zone séduisante, donc à revérifier avant toute phrase de papier (voir la fin).

## Brique 2 — la somme séquentielle des petits signaux

**Requêtes.** « CUSUM sequential change detection on linear probe scores LLM activations agent trajectory sabotage deception detection » ; « anytime-valid OR "e-process" OR CUSUM accumulate per-step probe scores agent trajectory activation monitoring "low and slow" OR diffuse sabotage 2026 » ; « "CUSUM" OR "sequential probability ratio test" "hidden states" OR "activations" language model probe monitoring online detection jailbreak OR hallucination OR deception token-level 2025 2026 » ; « "SPRT" OR "sequential test" OR "cumulative sum" "activation probe" OR "linear probe" scores across agent steps "multi-step" sabotage … » ; « "catching pivots" CUSUM linear probe chain-of-thought honesty residual stream sequential detector false alarm » ; « "From Probe Scores to Alarm Policies" activation monitors language-model agents CUSUM alarm policy ».

| Source | Ce qu'elle occupe | Page et citation |
|---|---|---|
| Gupta, « Where Reasoning Models Commit to Deception », PDF auto-publié (créé le 8 juin 2026), hors arXiv, non relu par des pairs | Somme cumulée sur le score d'une sonde linéaire du flux résiduel, fausse alerte étalonnée sur l'ensemble honnête. Une chaîne de pensée, pas un agent ; document de formalisation, protocole annoncé, aucun résultat lu p. 1 à 6. | p. 1 : « CoT generation is modelled as a partially observed two-state Markov process whose latent honesty state is read through a linear residual-stream probe » ; p. 1 : « An online CUSUM-type sequential detector with calibrated false-alarm control completes the method » |
| Kumar et al., CURA, arXiv 2608.27808v1 | Somme cumulée sur une trajectoire d'agent, étalonnée sur les seules trajectoires réussies. Sans états internes, sans adversaire. | p. 1 : « combines task-agnostic signals from execution effort, reasoning semantics, execution physiology, and visual dynamics into a CUSUM risk process calibrated by Learn-then-Test on successful trajectories » ; p. 1 : « requires no model internals » ; p. 1 : « do not study adversarial evasion » |
| arXiv 2606.10456v2 (au dépôt) | Somme cumulée et test séquentiel du rapport de vraisemblance sur les scores par pas d'un moniteur, contre un sabotage réparti. Scores de moniteur, pas de sondes (aucune occurrence de sonde ou d'activation dans le texte extrait). | p. 2 : « Classical CUSUM [15] and SPRT [18] are designed for mean shifts. When retargeted to the autocorrelation or a likelihood ratio over the joint distribution of scores, they form the Monitor B » |
| Itkin, arXiv 2606.12476v3 | Détection de rupture au plus vite sur un signal de modèle ; boîte noire ; nomme les sondes internes comme suite possible. | p. 1 : « We formulate hallucination onset detection as a quickest change detection problem » ; p. 11 : « internal-state probes among them, at the cost of black-box applicability » |
| Alshaalan et Rodrigues, arXiv 2605.19966v1 | Somme cumulée de Page sur l'entropie des jetons. | p. 2 : « We instantiate CPD as a one-sided Page-CUSUM de[tector] » |
| arXiv 2607.11317v1, 2607.20129v2 | Somme cumulée au décodage, sur probabilités de jetons et fenêtres ; états cachés cités comme piste seulement (2607.20129, p. 9). | Résumés et titres |
| E-valuator, arXiv 2512.03109 ; Probe Trajectories, arXiv 2605.18549 ; Gao, arXiv 2610.04575v1 (au dépôt) | Déjà à l'état de l'art v1 (accumulation toujours valide en boîte noire ; score de sonde comme série temporelle). Le troisième dit lui-même ne pas simuler de contrôleur séquentiel. | 2610.04575, p. 3 : « requires a new sequential contract and prospective evaluation » (phrase entière : « Such a stop policy requires a new sequential contract and prospective evaluation ») |

**Verdict : partielle.** La forme est occupée de tous côtés et doit être citée : somme cumulée sur score de sonde linéaire (Gupta, théorie), sur trajectoire d'agent étalonnée sur les réussites (CURA), sur scores de moniteur contre le sabotage réparti (2606.10456). Ce qui n'a pas été trouvé au périmètre cherché le 20 novembre 2026 : une somme cumulée mesurée sur des scores de sondes internes d'un agent, sous le seuil d'une sonde de surprise, avec un témoin honnête en erreur. C'est l'intersection que l'état de l'art v1 disait déjà « laissée ouverte » ; ce passage ne l'élargit pas.

## Brique 3 — l'épreuve d'évasion à compétence constante

**Requêtes.** « model learns to evade activation probe while preserving task performance obfuscation "capability" held constant neural chameleons RL-obfuscation probe evasion utility constraint » ; « red team fine-tunes model to evade deception probe while maintaining task accuracy sabotage success rate held fixed "probe evasion" "performance" tradeoff "obfuscat" 2026 agent white-box monitor adaptive attack ».

| Source | Ce qu'elle occupe | Page et citation |
|---|---|---|
| McGuinness et al., Neural Chameleons, arXiv 2512.11949v1 (au dépôt) | Évasion de sondes jamais vues, coût en capacité mesuré. | p. 3 : « The evasion behavior has a negligible capability tax » ; p. 1 : « a modest impact on model capabilities on standard benchmarks » |
| Bailey et al., arXiv 2412.09565v2 (au dépôt) | Évasion à comportement conservé, et sa limite sur tâche difficile. | p. 1 : « our attacks can often reduce recall from 100% to 0% while retaining a 90% jailbreaking rate » ; p. 3 : « This suggests a trade-off between obfuscation and performance in difficult tasks » |
| RL-Obfuscation, arXiv 2506.14261v4 (au dépôt) | Récompense à deux termes : tromper le moniteur, garder le comportement. | p. 1 : « monitors while maintaining their blackbox behaviour » |
| Someya et Lucassen, « Models Trained to Evade Topic Probes Struggle to Answer Questions about Those Topics », 19 octobre 2026 (page web) | L'épreuve presque à la lettre : exactitude et part des réponses justes signalées à 1 % de faux positifs. | Page web, non opposable : « at a substantial cost to their capability on the relevant topic » |

**Verdict : occupée.** Mesurer l'évasion d'une sonde en tenant ou en rapportant la compétence est une épreuve publiée, avec deux résultats de sens opposé (coût négligeable ; coût lourd sur le sujet visé). Non trouvé au périmètre : cette épreuve appliquée à une sonde de réussite attendue ou de surprise, et à un agent saboteur sur tâche de recherche. Cela restreint ce qui peut être dit, cela ne libère pas la zone.

## Brique 4 — une sonde de réussite attendue apprise sur des épisodes honnêtes seulement, base que toute sonde d'intention doit battre, rejouée sur un chiffre publié

**Requêtes.** « probe predicting task success trained on honest trajectories baseline for sandbagging detection "expected success" OR "correctness probe" hidden states AI control » ; « success predictor trained only on benign trajectories used as anomaly detector for attacked or sabotaged agent runs hidden-state probe "benign" only training failure prediction agents sabotage » ; « sandbagging detection probe "knows the answer" correctness representation model could solve but does not … » ; « sandbagging detection predict model's true capability from activations "accuracy probe" OR "capability probe" … underperformance gap » ; « deception probe confounded with "wrongness" OR "incorrectness" control: correctness probe baseline "intent" versus "outcome" … "honest but wrong" » ; « "Disentangling Task Difficulty from Run-Level Failure in Agent Failure Prediction" » ; « "Effectiveness of Hidden-State Probes for Localizing Reasoning Failures" ».

| Source | Ce qu'elle occupe | Page et citation |
|---|---|---|
| Cencerrado et al., arXiv 2509.10625v3 | La sonde de réussite avant génération. | p. 1 : « train linear probes to predict whether the model's forthcoming answer will be correct » |
| Davidov et al., arXiv 2604.18419v6 | La sonde de valeur le long de la génération. | p. 7 : « train an MLP probe on hidden states to estimate V0(x, y1:t; π) » |
| Subhnil et al., arXiv 2610.22046v1 | La limite de la sonde de justesse comme lecture. | p. 1 : « Standard hidden-state probes are trained on final-answer correctness, a label that conflates these cases » |
| Kumar et al., CURA, arXiv 2608.27808v1 | L'étalonnage sur les seules exécutions sans faute, sans étiquette d'échec. | p. 1 : « Learn-then-Test calibration on successful trajectories provides finite-sample false-alarm control without failure labels » |
| EsfandyariDoulabi et al., arXiv 2610.05572v1 | Le témoin « difficulté » que toute prédiction d'échec doit battre. | p. 1, citée à la brique 1 |
| Lin et al., « When Lie Detectors Learn Model Identity », ICLR 2026 (page de la conférence, par le moteur de recherche) | La recommandation de contrôler la justesse. | Non vérifié sur PDF, identifiant arXiv non trouvé : « control for correctness, and test against honest-vs-honest baselines » (extrait rendu par le moteur) |
| « Eval-Awareness Steering detects the Test, Not the Sabotage », 25 juin 2026 (page web) | Écart à l'honnête par item comme vérité de la retenue. | Page web, non opposable |

**Verdict : partielle.** La sonde de réussite attendue est occupée et se cite ; l'étalonnage sur exécutions saines seulement aussi. Son emploi comme base qu'une sonde d'intention doit battre, apprise sans aucun exemple de sabotage, n'a pas été trouvé : aucune antériorité trouvée au périmètre cherché le 20 novembre 2026. La recommandation voisine de Lin et al. (boîte noire, retenue volontaire) est la plus proche et n'a pas pu être lue. « Rejouer un chiffre publié avant de toucher nos épisodes » est une pratique de réplication, pas une revendication.

## Brique 5 — la divergence d'un jumeau forcé sur le même début d'épisode

**Requêtes.** « teacher-forced honest model divergence same prefix detect sabotage untrusted agent KL divergence trusted model log-probability monitor AI control » ; « paired honest twin same prefix counterfactual next-action distribution divergence between sabotaging model and honest reference model detection sandbagging "model diffing" logits prefix » ; « log-likelihood of agent actions under reference honest policy anomaly score sabotage detection "forced decoding" OR "teacher forcing" OR "perplexity under trusted model" control monitor baseline » ; « resampling untrusted model same context compare actions honest policy "Ctrl-Z" incrimination divergence baseline versus activation probe white-box » ; « detect backdoored or misaligned fine-tuned model by comparing next-token distributions with clean reference model on same prefix KL divergence per token "reference model" … » ; « AI control "honest policy" continue from same trajectory prefix compare untrusted agent next action divergence "counterfactual" … » ; « activation difference between sandbagging model and benign base model on identical forced tokens … model diffing probe » ; « "token statistics fail at AI attack detection" generation divergence ».

| Source | Ce qu'elle occupe | Page et citation |
|---|---|---|
| Sun, Nita-Rotaru, Oprea, arXiv 2610.03960v1 | La divergence par position entre un modèle suspect et son modèle de base, sur le même contexte. Empoisonnement d'un modèle affiné, pas un agent ni un sabotage. | p. 3 : « Both models read the same context, so any difference between the two distributions comes from fine-tuning » ; p. 4 : « At each output position t, we compute the Jensen–Shannon divergence » |
| Minder et al., arXiv 2510.13900v3 | La version interne : différence d'activations entre modèle affiné et modèle de base sur le même texte. | p. 1 : « analyzing activation differences on the first few tokens of random text » |
| Fomin et al., arXiv 2606.30449v1 | Direction « affiné moins base » essayée comme moniteur avant l'action, et son échec. | p. 1 : « A disposition direction is a unit difference-of-means vector between a misaligned fine-tune and its base model, measured in the residual stream » |
| Taylor et al., arXiv 2512.07810v1 (au dépôt) | La comparaison à un modèle de référence de confiance, et sa fragilité. | p. 2 : « They are allowed to compare to a weaker reference model they know to be benign » ; p. 15 : « calibration against the trusted reference model was ineffective and misleading » |
| Bhatt et al., Ctrl-Z, arXiv 2504.10374v1 (au dépôt) | Le rééchantillonnage au même contexte comme preuve à charge ; même modèle, pas de jumeau. | p. 1 : « incriminating the agent by generating additional examples of dangerous behavior » |
| Maheshwari et al., « Token Statistics Fail at AI Attack Detection But Generation Profiles Succeed », 11 avril 2026 (page web, travail de marathon de programmation) | Divergence entre l'exécution et une relance du même modèle en contexte isolé. Pas le même début, pas de jetons forcés. | Page web, non opposable : « We couldn't find prior work on perturbation-based divergence detection for AI control specifically » |

**Verdict : partielle.** Comparer, position par position et sur le même contexte, un modèle suspect à un modèle de référence est publié (empoisonnement, comparaison de modèles), en sorties comme en activations. Dans le contrôle d'agents, employé comme base sans sonde que la lecture interne doit égaler ou battre, avec un jumeau honnête forcé sur le début de l'épisode : aucune antériorité trouvée au périmètre cherché le 20 novembre 2026. Deux avertissements publiés s'y attachent : la référence peut être « inefficace et trompeuse » (2512.07810, p. 15), et la direction « affiné moins base » ne passe pas au rôle de moniteur avant l'action (2606.30449).

## Brique 6 — la comparaison au même jalon, avec les seuls fichiers alors disponibles

**Requêtes.** « monitor compared at same checkpoint information available "time to detection" agent sabotage monitor alert before tests fail prefix-matched baseline early detection trajectory prefix » ; « "Early Detection of Distributed Backdoors in Multi-Agent" online prefix detector » ; plus les requêtes des briques 2 et 4, qui ont rendu les sources ci-dessous.

| Source | Ce qu'elle occupe | Page et citation |
|---|---|---|
| Gao, « From Probe Scores to Alarm Policies », arXiv 2610.04575v1 (au dépôt) | Le principe exact : un moniteur d'activations se juge contre un comparateur qui voit la même chose au même moment. | p. 3 : « Observability: the transcript and system information available to a non-activation comparator at the same horizon » ; p. 3 : « Timing: when the score is read relative to the action » ; p. 3 : « Restricted predictive value additionally needs a competitive observable at the same horizon » |
| EsfandyariDoulabi et al., arXiv 2610.05572v1 | L'évaluation à des débuts d'exécution calculables en ligne. | p. 5 : « evaluating predictors at online-computable prefixes » |
| Fernandez Arias et al., arXiv 2607.24893v2 | Détecteur qui ne lit que l'exécution en cours, avec les pas restants. | p. 2 : « A prefix detector reading only the run so far catches 99.5% of successful attacks at a median of twelve steps » |
| Kumar et al., CURA, arXiv 2608.27808v1 | Comparaison aux bases à budget de fausses alertes égal, et avance en pas. | p. 1 : « detects 42.3% of failures a median of 31 steps before termination » |

**Verdict : occupée, dans son principe.** Le comparateur « au même horizon », à information égale, est énoncé comme condition de toute revendication d'un moniteur d'activations (2610.04575, p. 3). La précision de l'avis D, « une alerte arrivée après un test déjà échoué n'ajoute rien », n'a pas été trouvée mot pour mot ; elle en est une application, pas une idée distincte. À citer, à ne pas présenter comme propre.

## Brique 7 — une sonde de surprise réentraînée sans le seuil de 0,3

**Requêtes.** « process reward model probe hidden states step-level value estimates Monte Carlo rollouts "all steps" without filtering small changes noise label threshold probing TD error LLM reasoning ablation threshold » ; les trois requêtes sur le papier lui-même (brique 1) ; « "Effectiveness of Hidden-State Probes for Localizing Reasoning Failures" ».

| Source | Ce qu'elle occupe | Page et citation |
|---|---|---|
| Xu, Yuksekgonul, Zou, arXiv 2602.00986v2 | Le seuil lui-même, à l'entraînement et à l'évaluation. | p. 6 : « we retain only paragraphs satisfying |δt| > 0.3 during training. The same threshold is applied during evaluation » |
| Subhnil et al., arXiv 2610.22046v1 | Voisin : sonde de valeur apprise sur des taux de continuations par début de trace, et une sonde entraînée à prédire le pas fautif qui ne bat pas la longueur de la trace. Ne cite pas Xu et al. dans le texte extrait. Présence ou absence d'un filtre de grandeur non établie (p. 1 à 3 lues). | p. 2 : « the value probe, trained on rollout rates of recoverable traces » |
| ReProbe, arXiv 2511.06209 ; MCNIG, arXiv 2603.17815 | Voisins rendus par le moteur (sondes de crédibilité par étape ; gain d'information par étape). | Non téléchargés, non lus |

**Verdict : aucune antériorité trouvée au périmètre cherché le 20 novembre 2026.** Aucune réplique, critique ni suite du papier n'a été rendue par le moteur. La brique est un témoin de méthode attaché à ce papier précis ; son absence ailleurs est attendue et ne vaut pas zone libre. Le voisin 2610.22046 est à lire en entier avant le préenregistrement : s'il entraîne sa sonde de valeur sur tous les pas, il donne un point de comparaison publié sur des modèles de 4 et 8 milliards de paramètres.

---

## La réunion des sept briques

Requêtes : « white-box monitor diffuse sabotage research agent probes sequential evidence accumulation honest twin calibrated null "value probe" OR "success probe" covariate 2026 arXiv AI control low-stakes » ; « "Diffuse AI Control on Fuzzy Tasks" ».

Aucune source trouvée ne réunit une lecture interne de la réussite attendue employée comme base et covariable, une accumulation séquentielle de scores de sondes, et les quatre bases (sonde de réussite sur honnêtes seuls, jumeau forcé, même jalon, sonde sans seuil) dans un cadre de sabotage diffus. Verdict : aucune antériorité trouvée au périmètre cherché le 20 novembre 2026. Trois réserves. D'abord, cinq des sept briques sont occupées ou partielles : la réunion est un assemblage de pièces publiées, et seule cette forme d'assemblage pourrait se dire, jamais chaque pièce. Ensuite, les voisins sont récents et serrés (cinq datent d'août à octobre 2026) : 2610.04575 pose le comparateur au même horizon, 2610.05572 la séparation de la difficulté, CURA la somme cumulée étalonnée sur les réussites, 2610.12445 les sondes de sabotage par pas sur SHADE-Arena. Un papier qui les assemble peut paraître d'un mois à l'autre. Enfin, « Diffuse AI Control on Fuzzy Tasks » (arXiv 2606.08892, au dépôt) préfère, d'après le moteur de recherche, les interventions d'entraînement à la surveillance pour les menaces diffuses ; je ne l'ai pas relu ici, et il doit être cité en regard de tout bras de surveillance.

## Citations qui deviendraient obligatoires

Si le bras est écrit dans un préenregistrement ou un papier :

1. Xu, Yuksekgonul, Zou, arXiv 2602.00986 — la lecture.
2. Cencerrado et al., arXiv 2509.10625 ; Davidov et al., arXiv 2604.18419 ; Subhnil et al., arXiv 2610.22046 — sondes de réussite et de valeur, et leurs limites (briques 1, 4, 7).
3. EsfandyariDoulabi et al., arXiv 2610.05572 — difficulté contre signal propre à l'exécution (briques 1, 4, 6).
4. Gao, arXiv 2610.04575 — comparateur au même horizon (brique 6).
5. Kumar et al., CURA, arXiv 2608.27808 — somme cumulée sur trajectoire d'agent, étalonnée sur les réussites (briques 2, 4, 6).
6. Gupta, « Where Reasoning Models Commit to Deception » — somme cumulée sur sonde linéaire ; à citer comme document auto-publié (brique 2).
7. arXiv 2606.10456 ; E-valuator, arXiv 2512.03109 ; Probe Trajectories, arXiv 2605.18549 ; Itkin, arXiv 2606.12476 — accumulation séquentielle sur scores de moniteur et signaux de modèle (brique 2 ; les trois premiers sont déjà obligatoires par l'état de l'art v1).
8. McGuinness et al., arXiv 2512.11949 ; Bailey et al., arXiv 2412.09565 ; RL-Obfuscation, arXiv 2506.14261 ; Someya et Lucassen (billet du 19 octobre 2026) — évasion et coût en compétence (brique 3).
9. Sun, Nita-Rotaru, Oprea, arXiv 2610.03960 ; Minder et al., arXiv 2510.13900 ; Fomin et al., arXiv 2606.30449 ; Taylor et al., arXiv 2512.07810 ; Bhatt et al., arXiv 2504.10374 — comparaison à un modèle de référence et rééchantillonnage (brique 5).
10. Hollinsworth, Spies et al., arXiv 2610.12445 — sondes de sabotage par pas ; le billet de l'institut britannique du 10 juillet 2025 pour « intention ou erreur » (briques 1, 4).
11. Lin et al., « When Lie Detectors Learn Model Identity », ICLR 2026 — sous réserve de lecture sur PDF (brique 4).

À ne pas écrire : « première somme cumulée sur un score de sonde » ; « première épreuve d'évasion à compétence constante » ; « comparaison à information égale » comme apport propre ; « nouveau » pour aucune brique.

## Ce que je n'ai pas pu vérifier

- **Lin et al., ICLR 2026** : ni identifiant arXiv ni PDF trouvés. C'est le voisin le plus proche de la brique 4. À lire avant d'écrire la brique 4.
- **Pages web** (billet de l'institut britannique, deux billets de LessWrong, billet d'Apart Research) : lues par un outil qui résume ; les citations sont celles qu'il a rendues, non relues sur la page brute, non archivées. Non opposables.
- **Lecture partielle des PDF** : aucun des 18 n'a été lu en entier ; les pages lues sont dans la table. Lecture par extraction de texte, aucune figure regardée. Les papiers en deux colonnes donnent des phrases entrelacées : les citations de 2608.27808, 2610.04575 (« sequential contract »), 2610.05572 (p. 5) et 2610.22046 (p. 2) ont été revérifiées mot pour mot sur une extraction sans mise en page ; les autres viennent de lignes d'une seule colonne.
- **Papiers non téléchargés** : ReProbe (2511.06209), MCNIG (2603.17815), POISE (2605.07579), TRACE (2606.07054, au dépôt, non relu), 2604.28129 (au dépôt, non relu), « Stress-Testing Hidden-State Error Probes in LLMs » (NeurIPS 2026), « The Probe Detected the Banner, Not the Attack » (ICML 2026), Diff-SAE (2605.07324), 2501.11621, « Reference-Grafting » (2608.29458), C³ (PMLR 306).
- **Non relus ici** : E-valuator, Probe Trajectories, 2507.12691, 2509.21344, 2606.08892 ; leurs lignes viennent de l'état de l'art v1 ou du moteur de recherche.
- **Canaux non interrogés** : Google Scholar, Semantic Scholar (pas de graphe de citations de 2602.00986), OpenReview (relectures de NeurIPS 2026), recherche de code sur GitHub, Alignment Forum par son propre moteur. La demande visait aussi les dépôts de code : je n'en ai ouvert aucun ; trois sont nommés par les papiers (`AlignmentResearch/caught-in-the-act-probes`, `YehudaItkin/quickest-hallucination-onset`, `maxf-zn/misalignment_monitoring`).
- **Mode du moteur** : toutes les requêtes en mode ordinaire, aucune en mode étendu ; résultats limités aux États-Unis. Aucune requête en français ni en chinois.
- **Brique 7** : je n'ai pas établi si 2610.22046 filtre les petites variations.
- **Statut de publication** du papier (NeurIPS 2026) : rendu par le moteur, non vérifié sur la page de la conférence.
- **Dates** : les dates des prépublications sont celles de l'interface d'arXiv, relevées par le script du dépôt.

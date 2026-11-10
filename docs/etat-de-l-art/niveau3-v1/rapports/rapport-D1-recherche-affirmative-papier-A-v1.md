# Rapport D1 — recherche affirmative d'antériorité, papier A — v1

Écrit le 2026-11-10, entre 10:48 et 10:55 UTC (heures relevées par `date -u`), par un sous-agent neuf du lot D1.
Consigne commune lue en entier : `docs/etat-de-l-art/niveau3-v1/consignes/consigne-commune-lecteurs-v1.md`.

**Statut de preuve.** Tout ce que rend le moteur de recherche est une **piste non opposable** (règle R7).
Une seule pièce a été ouverte sur PDF empreinté du dépôt (arXiv 2610.12445) ; ses citations sont contrôlées
par programme (section 6). Aucune hypothèse, aucune revendication, aucun document existant n'a été modifié.

---

## COLLISION POSSIBLE (non vérifiée sur PDF)

Aucune pièce trouvée ne réunit, d'après le moteur, les deux idées du cœur du papier A : accumulation
séquentielle de scores de sondes d'activations **et** sabotage diffus d'un agent. « Non trouvé » ne veut pas
dire « personne ne l'a fait » (règle R8). Trois pistes touchent une revendication d'assez près pour être
lues en priorité.

**C-1. « What Do Collusion Probes Read? Three Pitfalls in Evaluating Multi-Agent Collusion Monitors »,
arXiv 2611.10620 (identifiant donné par le moteur ; date non confirmée).** Hypothèse touchée : **H8**
(validité de construit), et le papier B. Le moteur dit que ces sondes détectent surtout que l'agent
« was told to collude, not that it decided to ». C'est le glissement de construit, que le programme tient
déjà pour décrit. La collision ne tiendrait que si le papier relie ce construit à la robustesse adverse
(la prédiction de H8). Non vérifiable ici : le PDF n'est pas au dépôt. Réserve : un numéro 10620 au
10 novembre est élevé ; l'identifiant est à confirmer.

**C-2. « Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception »,
Hollinsworth, Spies, Diriba, Gleave, Cundy (FAR.AI), arXiv 2610.12445v1, 8 octobre 2026.** Hypothèse
touchée : **H1** (gain boîte blanche sur boîte noire), idée (4). PDF au dépôt :
`docs/sources/pdf/2610.12445v1.pdf`, empreinte `7e141758…`. Aucune mention trouvée par `git grep` dans
`docs/etat-de-l-art`, `docs/decisions`, `registres/veille.md` : **pièce non jugée dans ces chemins**.
Lecture partielle sur PDF (section 6) : les sondes battent un moniteur de texte sur des trajectoires
d'agent à plusieurs pas de SHADE-Arena. Le programme tient déjà le gain général pour établi et ne
revendique que la mesure « diffus et flou ». Une recherche par programme des mots « diffuse », « CUSUM »,
« low-stakes », « e-process », « martingale », « anytime » dans les 98 pages rend **zéro** ligne. La
comparaison lue porte sur des pas (« positive steps »), non sur une accumulation le long de la
trajectoire. Verdict provisoire : **occupée en partie** pour le gain général sur agent saboteur (déjà
concédé par H1) ; **libre dans les pages lues** pour le diffus et pour l'accumulation. À lire en entier
par un lot de lecture : je n'ai lu que les pages 1, 2, 7, 48 et 59.

**C-3. « What the Monitor Saw: activations, pooling, and evidence combination in AI control cascades »,
NeurIPS 2026 (page neurips.cc/virtual/2026/165252 ; auteurs et identifiant arXiv non rendus).**
Hypothèses touchées : **Tr** (agrégation au niveau de l'action), **H1**. Le moteur dit : cascade de
moniteurs sur LinuxArena ; une tête lisant le flux résiduel du **moniteur** bon marché ; « a linear probe
on the same activations recovers about 1.6x as many of the monitor's wrong calls ». Les activations lues
sont celles du moniteur, non celles de l'agent : la collision avec H1 paraît faible. Le titre annonce
« pooling » et « evidence combination » : à vérifier pour Tr et pour l'agrégation. PDF absent du dépôt.

Aucune de ces trois pistes n'est une collision établie. Aucune zone revendiquée n'apparaît occupée en
entier dans ce que le moteur a rendu.

**Fait annexe à signaler à Lazar.** La requête 2 (qui ne portait aucun nom) a rendu en premier résultat
la page publique « GitHub - lciric/controle-ia ». Le moteur la résume comme un programme « White-Box
Control of Diffuse Threats » qui croise l'accès (boîte noire ou blanche) et l'agrégation (par action ou
séquentielle), avec le code écrit et les lancements en attente. Je ne l'ai pas ouverte. Ce n'est pas une
antériorité d'autrui. C'est un fait de visibilité : le plan du papier A est indexé publiquement.

---

## 1. Journal des requêtes

Outil : recherche sur le réseau. Aucune requête ne porte le nom du directeur, du projet, du dépôt ni du
fonds. Les requêtes partent par lots ; l'heure est celle de `date -u` relevée dans le même lot.
43 requêtes émises, dont 11 en mode « extended » et 1 refusée. La consigne du lot demandait 25 à 40
requêtes et cinq ou six en mode « extended » : j'ai dépassé les deux bornes ; je le signale.

| n° | heure (UTC) | mode | texte exact |
|---|---|---|---|
| 1 | 10:48:29 | extended | `sequential test CUSUM e-process linear probe scores agent trajectory AI control monitoring` |
| 2 | 10:48:29 | extended | `white-box monitoring diffuse threats activation probes aggregation across agent trajectory low-stakes control 2026` |
| 3 | 10:48:29 | standard | `anytime-valid test martingale deception probe agent multi-step collusion detection NARCBench follow-up` |
| 4 | 10:48:54 | extended | `"probes" "diffuse" sabotage agent activations monitor arXiv October 2026` |
| 5 | 10:48:54 | extended | `white-box vs black-box monitors AI control agents linear probes versus LLM monitor comparison trajectory-level` |
| 6 | 10:48:54 | standard | `"Caught in the Act" deception probes agent sabotage benchmark activations before action` |
| 7 | 10:48:54 | standard | `UK AI Security Institute white box control team probes sandbagging agents 2026 results` |
| 8 | 10:49:09 | standard | `"From Probe Scores to Alarm Policies" operational validity activation monitors language-model agents` |
| 9 | 10:49:09 | standard | `"What Do Collusion Probes Read" three pitfalls multi-agent collusion monitors` |
| 10 | 10:49:09 | standard | `"Detecting Research Sabotage from Agent Behavior" NeurIPS 2026` |
| 11 | 10:49:09 | extended | `arXiv 2611 activation probes agents sequential aggregation cumulative evidence sabotage detection November 2026` |
| 12 | 10:49:09 | standard | `"Pre-Crime for Agents" probing when a recruited agent gives in activations bag-of-words` |
| 13 | 10:49:09 | standard | `Redwood Research blog 2026 diffuse threats probes low-stakes control white-box monitoring results` |
| 14 | 10:49:09 | standard | `"Diffuse AI Control on Fuzzy Tasks" follow-up monitoring aggregation suspicion scores across tasks` |
| 15 | 10:49:20 | standard | `macro-protocol Bayesian credence untrusted model sequence of tasks probe evidence accumulate "deferral" white-box 2026` |
| 16 | 10:49:20 | standard | `Google DeepMind production-ready probes Gemini follow-up agentic trajectories probes aggregation long context 2026` |
| 17 | 10:49:20 | standard | `Apollo Research deception probes agentic settings multi-turn 2026 probe generalization scheming agents` |
| 18 | 10:49:20 | extended | `probe construct validity "evaluation awareness" probe reads instruction not intent deception probe robustness predictor 2026` |
| 19 | 10:49:36 | standard | `deception probe "instruction" confound "prompted" versus "on-policy" probe generalization predicts robustness agents arXiv 2026 Natarajan` |
| 20 | 10:49:36 | extended | `HELIOS collusion detection follow-up "anytime-valid" OR "e-value" OR "sequential test" activations multi-agent 2026` |
| 21 | 10:49:36 | standard | `sandbagging detection long-horizon agent tasks white-box probes vs black-box monitor "per-step" aggregation 2026 arXiv` |
| 22 | 10:49:36 | standard | `"token-level" to "action-level" probe aggregation agent max mean robustness adversarial dilution probes agents` |
| 23 | 10:49:49 | standard | `arXiv 2603.13791 long-horizon agents deception black-box CoT-aware activation-probe monitors` |
| 24 | 10:49:49 | standard | `"research sabotage" probes activations automated AI R&D agent white-box monitor 2026` |
| 25 | 10:49:49 | standard | `"sequential probability ratio test" OR "SPRT" OR "CUSUM" "activation" probes LLM agent misalignment detection trajectory` |
| 26 | 10:49:49 | standard | `Anthropic alignment science blog 2026 probes agents sabotage monitoring activations "trajectory"` |
| 27 | 10:50:01 | extended | `LessWrong Alignment Forum October 2026 white-box control probes agents "diffuse" OR "low-stakes" sabotage cumulative monitor results` |
| 28 | 10:50:01 | standard | `"black-to-white" performance boost agentic trajectories deception probes agents multi-step monitor with probe access 2026` |
| 29 | 10:50:01 | standard | `subtle sabotage spread over many actions "below threshold" each step monitor aggregation agent "probe" internal activations detection model organism` — **REFUSÉE** (voir section 5) |
| 30 | 10:50:01 | standard | `FAR AI 2026 probes sabotage SHADE-Arena white-box monitor versus text monitor per-step trajectory aggregation follow-up` |
| 31 | 10:50:17 | standard | `"anytime-valid" OR "e-process" AI control monitoring suspicion scores trusted monitor sequential audit budget agents 2026` |
| 32 | 10:50:17 | extended | `OpenReview ICLR 2027 submission activation probes agent trajectories sequential monitoring sabotage white-box black-box matched aggregation` |
| 33 | 10:50:17 | standard | `MATS 2026 research white-box monitoring probes agents control "linear probes" trajectory sandbagging paper` |
| 34 | 10:50:17 | standard | `probes detect system prompt instruction leakage rather than deceptive intent "textual evidence" agents probe shortcut 2026 follow-up "leakage"` |
| 35 | 10:50:33 | standard | `"Trusted monitoring, but with deception probes" LessWrong control protocol probe monitor comparison results` |
| 36 | 10:50:33 | standard | `ControlArena OR LinuxArena OR BashArena white-box probes activations monitor open-weight untrusted agent side task detection 2026` |
| 37 | 10:50:33 | standard | `"From Reward-Hack Activations to Agentic Risk States" context-calibrated mechanistic monitoring LLM agents` |
| 38 | 10:50:33 | extended | `probe scores accumulated over turns "running" evidence deception probe multi-turn agent "sequential" detection delay false alarm rate activations 2026` |
| 39 | 10:50:51 | standard | `"What the Monitor Saw" activations pooling evidence combination AI control cascades` |
| 40 | 10:50:51 | standard | `per-step monitors marginal score distribution preserved distributed sabotage "zero-stealth-budget" follow-up temporal correlation trajectory monitor 2026` |
| 41 | 10:50:51 | standard | `AI Security Institute 2026 paper probes "white box" agentic sandbagging activation monitors "agent" transcripts aggregation deception probes Inspect` |
| 42 | 10:51:10 | standard | `neurips.cc virtual 2026 165252 "What the Monitor Saw" LinuxArena linear probe residual stream monitor cascade` |
| 43 | 10:51:10 | extended | `e-value betting martingale over activation probe scores language model agent deception "anytime" false alarm guarantee arXiv 2610 OR 2611` |

Constat répété du moteur, non opposable : sur les requêtes 1, 3, 11, 20, 25, 38 et 43, il écrit ne trouver
aucune pièce qui combine test séquentiel et sondes d'activations sur trajectoire d'agent. C'est un
résultat propre ; au titre de la règle R4, je le pose comme **réserve** : le moteur indexe mal les
parutions de novembre 2026 (un seul identifiant 2611 rendu) et rien des billets d'octobre 2026 des forums.

---

## 2. Table des pistes

Colonnes. « Idée » : (1) à (6) de la consigne du lot. « Hyp. » : hypothèse touchée. « Dépôt » : PDF présent
sous `docs/sources/pdf/` ou ses sous-dossiers d'antériorité (vérifié par `ls`). « Jugée » : identifiant
trouvé par `git grep` dans `docs/etat-de-l-art`, `docs/decisions`, `registres/veille.md`. « Prio » :
priorité de récupération du PDF (1 = d'abord ; « — » = déjà au dépôt). Les textes entre guillemets sont des
extraits du résumé du moteur, non du papier.

### 2.1 Pistes nouvelles ou non jugées

| Titre | Auteurs | Identifiant | Parution | Ce que dit le moteur (non opposable) | Idée | Hyp. | Dépôt | Jugée | Menace | Prio |
|---|---|---|---|---|---|---|---|---|---|---|
| What Do Collusion Probes Read? Three Pitfalls in Evaluating Multi-Agent Collusion Monitors | non rendus | arXiv 2611.10620 (à confirmer) | novembre 2026 ? | les sondes détectent que l'agent « was told to collude, not that it decided to » | 5, 6 | H8 | non | non | collision possible | 1 |
| Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception | Hollinsworth, Spies, Diriba, Gleave, Cundy (FAR.AI) | arXiv 2610.12445 | 8 oct. 2026 | sondes à « 98.8% AUC on SHADE-Arena », au-dessus d'un moniteur de texte | 3, 4, 6 | H1, Tr | oui (`2610.12445v1.pdf`) | non | collision possible (partielle, voir C-2) | — |
| What the Monitor Saw: activations, pooling, and evidence combination in AI control cascades | non rendus | NeurIPS 2026, page 165252 | 2026 | tête sur le flux résiduel du moniteur bon marché, LinuxArena ; « the way evidence is used dominates » | 3, 4 | Tr, H1 | non | non | collision possible (faible) | 1 |
| Pre-Crime for Agents, at the Last Second: Probing When a Recruited Agent Gives In | Leonidas Raghav | arXiv 2610.40588 | 29 oct. 2026 | sonde linéaire lue à chaque appel, jusqu'à 20 tours ; « catches 82% of leaking calls » contre 26 % pour un moniteur sans exemple ; un classifieur sac de mots « comes close » ; « Halting on any alarm would stop most benign episodes » | 3, 4, 5 | H1, H2, H8 | non | non | voisin proche | 1 |
| AgentDecept: Benchmarking Deceptive Behavior in Tool-Using LLM Agents under Pressure | non rendus | arXiv 2610.39377 | fin oct. 2026 | sonde de falsification, « AUROC 0.979 », mais à 1 % de faux positifs par tour elle « detects only 18.9% of positive trajectories » | 4 | H2, Tr | non | non | voisin proche | 2 |
| Probe monitors seem to perform realistically in simulated … (billet LessWrong, titre tronqué) | non rendus | lesswrong.com/posts/T5n2GycMYMTXgy4JF | inconnue | moniteurs à sondes sur LinuxArena, détection d'attaques simulées contre réelles | 3, 4 | H1 | non | non | voisin proche | 2 |
| Résumé ICML 2026 (titre non rendu), icml.cc/virtual/2026/79385 | non rendus | page 79385 | 2026 | sondes linéaires gardant un rappel élevé après qu'une politique trompe un moniteur à raisonnement | 3 | H1, H6 | non | non | voisin proche | 2 |
| Quickest Detection of Hallucination Onset: Delay Bounds and Learned CUSUM Statistics | non rendus | arXiv 2606.12476 | juin 2026 | « learned CUSUM over a causal recurrent labeler », détection en 11 à 13 jetons | 1 | H2, lemme | non | non | voisin proche (à vérifier : signal interne ou non) | 2 |
| Real-Time Detection and Repair of LLM Agent Failures | non rendus | arXiv 2608.02464 | août 2026 | « CUSUM over per-channel surprise » ; cite les sondes du flux résiduel | 1, 4 | H2 | non | non | voisin proche (à vérifier : canaux internes ou non) | 2 |
| CURA: Certified Runtime Alarms for Computer-Use Agents | non rendus | arXiv 2608.27808 | août 2026 | somme cumulée et martingale de pari sur un score de risque d'agent ; « deliberately uses no model internals » | 1 | H2 (squelette boîte noire) | non | non | voisin | 3 |
| CUSUM-Shaped Inference-Time Monitoring and Targeted Re-Decoding for Quantized Small Language Model Reasoning | non rendus | arXiv 2607.20129 | juillet 2026 | somme cumulée et variantes en e-processus, au niveau du jeton | 1 | H2 | non | non | voisin | 3 |
| The Truth Was Never Gone: Perfect Aliasing in Compliant-Context Truth Probes | non rendus | arXiv 2609.10739 | sept. 2026 | une sonde entraînée sur des consignes porte l'étiquette « the instruction was deceptive » ; problème d'identification | 5 | H8 | non | non | voisin proche | 2 |
| The Refusal Residue | non rendus | arXiv 2607.13346 | juillet 2026 | une sonde naïve atteint 1,0 « by encoding the system prompt » ; protocole sans fuite | 5 | H8 | non | non | voisin proche | 2 |
| Building Better Deception Probes Using Targeted Instruction Pairs | Natarajan et autres | arXiv 2602.01425 | février 2026 | le choix des consignes explique « 70.6% of variance » de la performance | 5 | H8 | non | non | voisin | 3 |
| Evaluation Awareness in Language Models: Representation, Verbalization, and Control | non rendus | arXiv 2608.21766 | août 2026 | titre seul | 5 | H8 | non | non | voisin | 3 |
| Is Evaluation Awareness Just Format Sensitivity? | non rendus | arXiv 2603.19426 | mars 2026 | les sondes de conscience d'évaluation sont « highly format-sensitive » | 5 | H8 | non | cité une fois (`proposition-P-011-T0.7-sondes-v1.md`) | voisin | 3 |
| Detecting Research Sabotage from Agent Behavior | non rendus | NeurIPS 2026, page 168155 | 2026 | trois voies boîte noire : juger la sortie, cohérence entre essais, questions de suivi | 2 | H1 (base boîte noire) | non | non | voisin | 3 |
| ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D | non rendus | arXiv 2607.19321 | juillet 2026 | moniteurs boîte noire ; les auteurs attendent que les menaces diffuses rendent le sabotage plus dur à voir | 2 | H1 | oui (v1, v2) | non | voisin | — |
| Training Deliberative Monitors for Black-Box Scheming Detection | Sinha, Naik, Gillioz et autres | arXiv 2605.29601 | mai 2026 | les sondes existantes ne classent pas des trajectoires à plusieurs tours | 3, 4 | H1 | oui (`anteriorite-P-041-v2/c7`) | non | voisin | — |
| How Intervention History Changes AI Agent Sabotage on Subsequent Tasks | non rendus | arXiv 2610.26935 | oct. 2026 | titre seul | 2 | H6 | oui (`anteriorite-P-041-v2/c5`) | non | voisin | — |
| The Impact of Off-Policy Training Data on Probe Generalisation | Kirch et autres | arXiv 2511.17408 | nov. 2025 | les sondes de tromperie « may fail to generalise to real monitoring scenarios » | 5 | H8 | oui (v4) | non | voisin | — |
| Fine-Tuned Lie Detectors Failed to Generalize (blog d'alignement d'Anthropic) | Hopkins et autres | alignment.anthropic.com/2026/lie-detectors | 21 août 2026 | les détecteurs affinés battent à peine les bases par consigne | 3, 6 | H1, H8 | non | non | voisin | 3 |
| Probing the Misaligned Thinking Process of Language Models | non rendus | arXiv 2606.24251 | juin 2026 | 18 indicateurs lus par sondes linéaires, filtre avant un juge | 4 | H1 | non | non | voisin | 3 |
| Anytime Detection of Strategic Deviations in Multi-Agent Systems | Gauthier, Bach, Jordan | arXiv 2601.05427 | janvier 2026 | supermartingale de test sur des gains de jeu ; pas de sondes | 1, 6 | H2 (papier B surtout) | non | cité une fois (`registres/veille.md`) | voisin | 3 |
| Audit the Whisper | non rendus | arXiv 2510.04303 | octobre 2025 | martingale de e-valeurs pour l'audit de collusion, sans activations | 1 | papier B | non | non | voisin | 3 |
| Dépôt « replay-test-collusion » (sprint Apart, octobre 2026) | 123yaroslav | github.com/123yaroslav/replay-test-collusion | octobre 2026 | variante « anytime-valid » d'un test de rejeu entre agents ; sans sondes | 1, 6 | papier B | non | non | voisin | 3 |
| What happens when a collusion probe only finds a thin signal (billet LessWrong) | non rendus | lesswrong.com/posts/gLhnc4eDCGzNhkrX3 | inconnue | sonde de collusion faible ; il faudra tenir compte de « the full agent trajectory » | 4, 6 | Tr | non | non | voisin | 3 |
| Trusted monitoring, but with deception probes (billet LessWrong) ; Whitebox Probes for AI Control (heronsec.ai) | non rendus | lesswrong.com/posts/eaEqAzGN3uJfpfGoc | inconnue | sondes contre moniteur boîte noire sur cinq jeux ; jeu de contrôle à 2 % de budget d'audit | 3 | H1 | non | non | voisin | 3 |
| Stop Early, Spend Less: Hidden-State Probes as a … (titre tronqué) | non rendus | arXiv 2606.10487 | juin 2026 | titre seul | 4 | — | non | non | voisin | 3 |
| Pooling Sequential Evidence Across Hypotheses: Rate-Optimal Multiple Testing at a Fixed Horizon | non rendus | arXiv 2609.27465 | sept. 2026 | titre seul ; statistique séquentielle pure | 1 | lemme | non | non | voisin | 3 |

### 2.2 Pistes rendues par le moteur, déjà au dépôt et déjà jugées

Rien de nouveau n'est ajouté ici ; je liste pour que le lanceur voie que le moteur retombe sur des pièces
connues. Toutes ont leur PDF au dépôt et au moins une mention dans les chemins jugés.

| Identifiant | Titre court | Idée | Hyp. | Où jugée (au moins) |
|---|---|---|---|---|
| 2610.04575 | From Probe Scores to Alarm Policies | 1, 4 | H2 | `niveau2-v1/anteriorite-v1.md`, proposition N-013 |
| 2606.10456 | The Distributed Detectability Band Against Marginal-Preserving Attacks | 1, 2 | théorème | `etat-de-l-art-verifie-niveau1-v1.md`, décision N-003/N-004 |
| 2512.03109 | E-valuator | 1 | H2 | niveau 1, décision N-007/N-008 |
| 2604.01151 | HELIOS / NARCBench | 4, 6 | papier B | niveau 1, P-040 |
| 2609.03035 | You Can't Escape Your Own Activations | 5, 6 | H8 | niveau 1, corrections niveau 2 |
| 2606.07054 | TRACE | 2 | H2 | niveau 1, N-007/N-008 |
| 2607.06503 | Doomed from the Start | 4 | — | niveau 1, veille |
| 2607.06807 | When Agents Go Rogue | 4 | papier B | niveau 1, veille |
| 2603.13791 | DeceptGuard | 3, 4 | H1 | `niveau2-v1/anteriorite-v1.md`, N-013 |
| 2604.14865 | Segment-Level Coherence | 4 | Tr | niveau 2 |
| 2606.06223 | From Reward-Hack Activations to Agentic Risk States | 4 | — | niveau 2 |
| 2605.27958 | Pressure-Testing Deception Probes | 5 | H8 | niveau 2, P-011 |
| 2608.02657 | Indirect Prompt-Injection Exposure in Hidden States | 4 | — | niveau 2 |
| 2604.28129 | Latent Adversarial Detection | 1, 4 | H2 | niveau 1 et 2, N-007/N-008 |
| 2507.12691 | Black-to-White Performance Boosts | 3 | H1 | niveau 2 |
| 2509.21344 | Linear probes rely on textual evidence | 5 | H8 | niveau 2, N-013, P-011 |
| 2607.11751 | When Local Monitors Miss Compositional Harm | 2 | théorème | niveau 2 |
| 2607.13087 | GDM AI Control Roadmap | 2, 6 | H1 | niveau 2, N-013 |
| 2607.02514 | Distributed Attacks in Persistent-State AI Control | 2 | H2 | niveau 2 |
| 2605.29178 | The Best-Laid SCHEMEs | 2 | papier B | niveau 2 |
| 2512.07810 | Auditing Games for Sandbagging | 3, 6 | H1 | niveau 2, N-013 |
| 2606.08892 | Diffuse AI Control on Fuzzy Tasks | 2, 6 | H1 | P-006, P-008, P-010 |
| 2601.11516 | Building Production-Ready Probes For Gemini | 4, 6 | Tr | non revérifié ici ; PDF présent (`2601.11516v4.pdf`) |

---

## 3. Lecture par idée (tout est piste, sauf la section 6)

- **(1) Accumulation séquentielle de scores de sondes le long d'une trajectoire d'agent.** Non trouvée.
  Le squelette boîte noire existe (E-valuator ; CURA, piste). Deux pistes à lever : 2606.12476 et
  2608.02464, pour savoir si leur somme cumulée lit un signal interne.
- **(2) Sabotage diffus vu par un moniteur interne.** Non trouvé. Les suites rendues pour 2606.08892
  parlent d'entraînement, non de surveillance ; le moteur ne rend aucune suite datée d'après le 6 octobre.
- **(3) Boîte blanche contre boîte noire à agrégation égale.** Occupée en partie pour le gain général
  (2610.12445, lue en partie ; 2610.40588, piste). Aucune pièce rendue n'annonce une agrégation égale.
- **(4) Sondes sur agents à plusieurs pas.** Champ actif en octobre 2026 : 2610.12445, 2610.40588,
  2610.39377, billet LinuxArena. Aucune ne paraît tester la robustesse de l'agrégation au niveau de
  l'action face à un attaquant adaptatif.
- **(5) Validité de construit comme prédicteur de robustesse.** Le glissement de construit est très
  décrit (2611.10620, 2609.10739, 2607.13346, 2602.01425). La **prédiction** de robustesse n'apparaît dans
  aucun résumé. C'est la piste C-1 qui peut la porter.
- **(6) Équipes.** Institut britannique : le moteur ne rend rien de 2026 sur les sondes au-delà de
  2512.07810. NARCBench / HELIOS : la suite rendue est 2609.03035, déjà jugée ; aucun test toujours valide
  publié n'est rendu. Redwood, DeepMind, Apollo, MATS : rien de neuf rendu sur les idées (1) à (4).
  FAR.AI : 2610.12445. Blog d'Anthropic : « Fine-Tuned Lie Detectors Failed to Generalize » (août 2026).

**Contre-résultats défavorables au programme, à l'état de piste.** (a) 2610.40588 : un classifieur sac de
mots approche la sonde ; l'arrêt sur toute alarme stoppe la plupart des épisodes sains. (b) 2610.39377 :
une sonde à 0,979 ne détecte que 18,9 % des trajectoires à 1 % de faux positifs par tour. (c) Blog
d'Anthropic, août 2026 : les détecteurs affinés généralisent mal. Ces trois points pèsent sur H1 et H2
et rejoignent 2610.04575, déjà jugée.

---

## 4. PDF à récupérer par une session à réseau ouvert, par ordre de priorité

1. **arXiv 2611.10620** — What Do Collusion Probes Read? — H8 ; confirmer d'abord l'identifiant et la date.
2. **NeurIPS 2026, page 165252** — What the Monitor Saw — Tr, H1 ; chercher l'identifiant arXiv.
3. **arXiv 2610.40588** — Pre-Crime for Agents — H1, H2, H8.
4. **arXiv 2610.39377** — AgentDecept — H2, Tr.
5. **arXiv 2606.12476** — Quickest Detection of Hallucination Onset — H2, lemme (signal interne ?).
6. **arXiv 2608.02464** — Real-Time Detection and Repair of LLM Agent Failures — H2.
7. **arXiv 2609.10739** — The Truth Was Never Gone — H8.
8. **arXiv 2607.13346** — The Refusal Residue — H8.
9. **Billet LessWrong T5n2GycMYMTXgy4JF** — moniteurs à sondes sur LinuxArena — H1 ; et la page ICML 2026
   n° 79385 (titre à trouver).
10. **arXiv 2608.27808** — CURA — squelette séquentiel boîte noire de H2.
11. **arXiv 2607.20129** — CUSUM-Shaped Inference-Time Monitoring — H2.
12. arXiv 2602.01425, 2608.21766, 2603.19426, 2606.24251, 2601.05427, 2510.04303, 2606.10487, 2609.27465 ;
    NeurIPS 2026 page 168155 ; billet d'Anthropic « lie-detectors » ; billets LessWrong gLhnc4eDCGzNhkrX3
    et eaEqAzGN3uJfpfGoc ; dépôt « replay-test-collusion ».

À lire sans réseau, car déjà au dépôt et non jugées dans les chemins nommés : **2610.12445v1** (en entier),
2610.26935v1, 2605.29601, 2607.19321, 2511.17408v4.

---

## 5. Ce que je n'ai pas pu chercher ; refus

- **Refus.** La requête 29 a été refusée par un classifieur de l'outil. Message rendu, tel quel :
  « API Error: Haiku 5.5 can't help with this. Start a new session to continue. […] Details: `[bio]` ».
  Conformément à l'interdit 6, je ne l'ai ni relancée ni reformulée. L'idée (2) reste couverte par les
  requêtes 2, 4, 13, 14, 24 et 27, émises avant ou dans le même lot.
- **Listes d'arXiv par date.** Impossible : arXiv est refusé par le réseau du conteneur. Le moteur ne rend
  qu'un seul identifiant de novembre 2026. La fenêtre du 1er au 10 novembre est donc **mal couverte**.
- **Forums.** Le moteur ne rend aucun billet daté d'octobre ou de novembre 2026 sur LessWrong ou le forum
  d'alignement ; les dates des billets rendus sont inconnues.
- **Pages d'équipes.** Pages de publications de l'institut britannique, de Redwood, d'Apollo, de FAR.AI,
  de MATS : non ouvertes (outil de lecture de pages refusé par le réseau).
- **Soumissions à ICLR 2027 sur OpenReview.** La requête 32 ne rend aucune soumission ; non couvert.
- **Citations en aval.** Je n'ai pas pu lister les papiers qui citent 2606.10456, 2606.08892, 2512.07810
  ou 2604.01151 : aucun outil de graphe de citations.
- **Recherche dans le dépôt.** Limitée à `docs/etat-de-l-art`, `docs/decisions`, `registres/veille.md` :
  une pièce « non jugée » ici peut l'être ailleurs.

---

## 6. Seule lecture sur PDF : arXiv 2610.12445v1

Fichier : `docs/sources/pdf/2610.12445v1.pdf` ; empreinte sha256 `7e1417580c4e…` (fichier compagnon
`2610.12445v1.pdf.sha256`) ; 98 pages ; pages lues : 1, 2, 7, 48, 59.

- Page 1 : « Our probes achieve 98.8% AUC in SHADE-Arena, surpassing an Opus 5.5 text-monitoring baseline ».
- Page 2 : « improves performance on monitoring long, multi-step, on-policy SHADE-Arena (Kutasov et al.,
  2025) trajectories, where probes outperform black-box monitors that are orders of magnitude more
  expensive to evaluate ».
- Page 7 : « all four probes trained on the full FIBS training set score 0.979 to 0.984, above the 0.960 of
  Opus 5.5, a SoTA black-box monitor ».
- Page 7 : « Opus 5.5 refuses on 2,638 of the 5,014 positive steps. »
- Page 59 : « It runs on every assistant turn with non-empty thinking, and a transcript is flagged when any
  of its turns is. » — cette phrase décrit un **juge du raisonnement**, non les sondes. Le résumé du moteur
  (requête 38) l'attribuait aux sondes : exemple de piste fausse, d'où la règle R7.

Lecture : comparaison boîte blanche contre boîte noire sur agent saboteur à plusieurs pas, comptée en pas.
Rien dans ces pages sur le diffus, ni sur une accumulation séquentielle. Réserve (R4) : le moniteur de
texte refuse sur plus de la moitié des pas positifs ; la comparaison dépend du traitement des refus.

**Contrôle des citations.** Script hors dépôt :
`/tmp/claude-0/-home-user-controle-ia-travail/a26149b8-c735-5fa7-914e-afb00d165aed/scratchpad/lotD1/controle_citations.py`.
Essai sur un cas juste : réussi. Essai sur un cas altéré (un chiffre changé) : échec détecté, comme attendu.
**Citations contrôlées : 5 ; échecs : 0.** Les extraits de la table 2 sont des extraits du moteur, non des
citations de papier : ils ne sont pas contrôlables et restent des pistes.

---

## 7. Verdict par pièce revendiquée (dans les pistes rendues, non opposable)

- H1, mesure « diffus et flou » : **non trouvée occupée** ; gain général occupé en partie (2610.12445).
- H2, accumulation séquentielle sur sondes internes : **non trouvée occupée**.
- Lemme et théorème négatif : rien de neuf au-delà de 2606.10456, déjà jugée.
- H6 : rien de neuf rendu.
- Tr : **non trouvée occupée** ; une piste à lever (C-3).
- H8, prédiction de robustesse par le construit : **non trouvée occupée** ; une piste à lever (C-1).

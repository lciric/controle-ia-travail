# EXTRAIT — When Benchmarks Lie: Evaluating Malicious Prompt Classifiers Under True Distribution Shift

- Auteurs : Max Fomin ; année : 2026 (v2 du 19 juillet 2026) ; identifiant : arXiv:2602.14161v2 (27 pages)
- Statut : préimpression arXiv cs.LG ; Zenity ; publié à l'atelier AIWILD (Agents in the Wild) de la conférence ICLR 2026 selon le pied de page de la page 1 ; article sur la détection de requêtes malveillantes (injection, évasion, requêtes nuisibles) par sondes d'activations, voisin des travaux sur les moniteurs
- PDF source : `docs/sources/pdf/2602.14161v2.pdf` ; SHA-256 du PDF : `7831c848841eca32bcbb1e18cd35f644cfe5a8af8f0f003623c4e1bdd6e03c00` (compagnon `.sha256` du dépôt vérifié par `sha256sum -c`)
- Pages gardées en tout ou en partie : 1-11
- Nature : texte du PDF repris mot pour mot (`pdftotext`, lignes rejointes en paragraphes), numéro de page du PDF en `[p.N]` au début de chaque passage ; coupes marquées `[COUPÉ]` ; tableaux et figures extraits en texte, mise en forme possiblement perdue (en cas de doute sur un chiffre de figure, se reporter à la page citée). Aucun chiffre retapé à la main (R7).
- Retiré pour sûreté (niveau méthode seulement) : rien (la figure 2, qui montrait des exemples de requêtes, n'est pas reprise).

---

[p.1]
A BSTRACT Detecting prompt injection, jailbreak attacks, and harmful requests is critical for deploying LLM-based agents safely, yet current evaluation practices in this literature overestimate generalization. We train activation-based classifiers (linear probes on LLM hidden states) on a benchmark of 18 datasets (prompt attacks plus benign sources) and propose Leave-One-Dataset-Out (LODO) evaluation, where the held-out dataset is never seen during training. Across four LLMs from three families (Llama-3.1-8B, Gemma-3-27B, Qwen-3.5-2B/4B), standard crossvalidation reports a pooled AUC 8.0–16.5 points higher than LODO; per-dataset held-out-test-vs-LODO accuracy gaps span 1–25 points. To understand the gap, we analyze the LODO stability of a linear probe’s perfeature classifier coefficients, defining a retention metric for sparse-autoencoder (SAE) features that flags dataset-dependent shortcuts. 28–44% of top SAE features are shortcuts across models, a dataset-identity classifier reaches 96.6%, and the dataset-identifying and safety-relevant subspaces partially overlap (§5.4). Standard domain-generalization fixes such as adversarial training, subspace projection, sample reweighting, and class balancing do not close the gap (§5.5). Finally, we show LODO-weighted SAE attributions filter dataset artifacts for more reliable per-prompt explanations. We release our framework at https://gith ub.com/maxf-zn/prompt-mining so future prompt-attack classifiers can be evaluated under LODO alongside CV.

1

I NTRODUCTION

[COUPÉ] Recent work has developed classifiers to detect prompt injection, jailbreak, and harmful-request attacks, using approaches ranging from fine-tuned BERT models (Chennabasappa et al., 2025) to activation-based probes (Abdelnabi et al., 2025a). These classifiers are typically trained and evaluated on aggregated benchmarks combining multiple attack datasets (e.g., AdvBench, HarmBench, WildJailbreak) and benign datasets (e.g., Enron emails, OpenOrca). Standard evaluation protocols use train-test splits where test samples come from the same dataset sources as training, reporting near-perfect performance with AUC scores exceeding 0.99 (Abdelnabi et al., 2025a; Saglam et al., 2025) — a result we replicate in Table 1.

[p.2]
However, this evaluation methodology overestimates true generalization. When training and test folds contain samples from the same datasets, classifiers can exploit dataset-identity signals — features that indicate dataset provenance rather than attack semantics. A classifier reaching 99% AUC may simply learn that “samples formatted like WildJailbreak are malicious” and “samples formatted like Enron are benign,” without learning generalizable attack patterns. This echoes broader findings in machine learning that models often succeed for the wrong reasons (McCoy et al., 2019; Geirhos et al., 2020), and is exacerbated when benchmark datasets are single-class (entirely malicious or entirely benign): any feature that identifies the dataset automatically predicts the class label, making dataset-identity exploitation trivial.

[COUPÉ]

[p.3]
2

R ELATED W ORK

[COUPÉ]Contemporaneous and adversarial-robustness work. Constitutional Classifiers (Sharma et al., 2025; Cunningham et al., 2026) and Circuit Breakers (Zou et al., 2024) optimize adversarial robustness via red-teaming or representation intervention — targeting worst-case attackers, whereas LODO measures static distribution shift. [COUPÉ][COUPÉ]Adaptive attacks and evaluation pitfalls. Nasr et al. (2025) bypass twelve recent jailbreak/promptinjection defenses with adaptive attacks, arguing static evaluations overstate robustness; their critique targets the adversarial axis, ours the distribution-shift axis, and the two are complementary predeployment diagnostics. PromptShield (Jacob et al., 2025) curates a deployment-oriented promptinjection benchmark and a fine-tuned Llama-3-8B detector trained on it — a deployable artifact, whereas our contribution targets the evaluation methodology that any such detector is measured against. 3

[p.4]
M ETHODS

3.1

P ROBLEM S ETUP

We address binary classification of LLM inputs as malicious or benign. Malicious inputs span four families: (i) harmful requests for restricted content; (ii) jailbreaks that attempt to bypass safety via roleplay, framing, or other prompt engineering; (iii) prompt injections that hijack instructions, including indirect injections embedded in external data the agent processes (emails, code, tool outputs, retrieved documents); and (iv) extraction attacks that elicit hidden system information. Threat Model. The defender has white-box access to LLM activations during inference but cannot modify the underlying model — the setting addressed by activation-probe detectors. We compare against text-only baselines that lack this access (§5). Dataset Composition. We compile 18 datasets covering these attack families plus benign sources (Table 7, Figure 2). Most are capped at 10K samples for tractable activation extraction; BIPIA uses 15K to cover its three context types. The full benchmark totals 105K samples (47% malicious); under LODO each dataset serves in turn as the held-out test set, so there is no fixed train/test split. 3.2

ACTIVATION -BASED C LASSIFICATION

Following Abdelnabi et al. (2025a), we extract activations from the LLM’s residual stream as input features for classification. These classifiers are also known as probes or linear probes in the interpretability literature; we use the terms interchangeably. For a text input x, we apply the model’s chat template and extract the activation vector hl ∈ Rd at layer l from the last token of the user message (before the generation-prompt tokens; see Appendix C.3): hl = LLMl (x),

(1)

where d is the model’s hidden dimension. We evaluate four LLMs spanning 2B-27B parameters across three families: Llama-3.1-8B-Instruct (Llama Team, AI @ Meta, 2024), Gemma-3-27B (Gemma Team, 2025), and Qwen-3.5-2B/4B (Qwen Team, 2026), plus a partial Llama-3.3-70B replication (Appendix F). [COUPÉ] 4

[p.5]
Raw Activations. Our primary classifier operates on raw activations from layer 31 (the final layer, indexed 0-31), captured at the last user-message token (immediately before the assistant generation prefix). [COUPÉ] [COUPÉ]3.3

L EAVE -O NE -DATASET-O UT (LODO) E VALUATION

Leave-one-domain-out cross-validation is an established protocol in domain generalization (Gulrajani & Lopez-Paz, 2021; Koh et al., 2021); our contribution is not the protocol itself but applying it at the dataset level to prompt-attack classification (where it has not been adopted) and quantifying the resulting CV-LODO gap. For each dataset Di in our benchmark, we train a classifier on all other datasets {Dj : j ̸= i} and evaluate on the held-out Di . This measures true out-of-distribution generalization, as the classifier has never seen any examples from the test dataset’s distribution. Formally, let D = {D1 , . . . , DK } be our K datasets. For each i, we compute:  LODOi = Metric fD\Di , Di , (3) where fD\Di is trained on all datasets except Di . We report both per-dataset metrics and pooled metrics across all held-out predictions.[COUPÉ] 3.4

DATASET S HORTCUT A NALYSIS

We perform shortcut analysis on SAE features rather than raw activations because SAE features are designed to be interpretable: each feature ideally corresponds to a single semantic concept. In contrast, individual neurons in raw activations are polysemantic, encoding multiple unrelated concepts that activate together (Bricken et al., 2023). This polysemanticity makes it difficult to characterize what patterns a given neuron detects, whereas SAE features can be examined via their max-activating examples. To quantify how much classifier performance depends on dataset-specific features, we introduce the LODO coefficient retention metric. For each feature j, let wj be its coefficient in the full classifier (−i) and wj its coefficient when dataset Di is held out. The retention for feature j is: (−i)

wj rj = min . i wj 5

(4)

[p.6]
Features with rj ≈ 1 are stable across dataset holdouts and likely capture genuine attack patterns. Features with rj ≪ 1 or rj < 0 (sign flip) are dataset shortcuts — their predictive value depends on specific datasets being present in training.[COUPÉ] We identify two types: • Pure dataset shortcuts: features that directly predict dataset identity (e.g., email formatting for Enron, code patterns for specific injection datasets). • Context-dependent shortcuts: features that fire across datasets but derive class signal from specific dataset compositions (e.g., a feature active on both malicious and benign samples, but whose class correlation depends on which datasets are included). To validate this analysis, we train a separate dataset classifier that predicts which dataset a sample belongs to from activations alone. High accuracy indicates that datasets are easily distinguishable in feature space, enabling shortcut exploitation.

E XPERIMENTS

We answer five questions: (1) How much does standard cross-validation overestimate generalization compared to LODO? (2) Does the gap extend beyond a single model family? (3) What fraction of learned features are dataset shortcuts, and what fraction of the gap can we close with standard mitigations? (4) How do activation-based classifiers compare to production baselines and LLM-asjudge under fair operating points? (5) Can LODO-stable features provide reliable explanations? 4.1

E XPERIMENTAL S ETUP

Dataset. Our benchmark comprises 18 datasets (105K samples, 47% malicious) spanning direct jailbreaks, indirect injection, extraction attacks, and benign sources. For evaluation, we merge Gandalf (114 samples) into Mosscap — both use identical system prompts for password protection (Appendix B) — yielding 17 datasets for LODO results; shortcut analysis uses the original 18. Six datasets are 100% malicious and five are 100% benign; the remaining six are mixed-class. We audit cross-dataset near-duplicate overlap in Appendix K. Models and Baselines. We evaluate Llama-3.1-8B, Gemma-3-27B, and Qwen-3.5-2B/4B in the main body (plus partial Llama-3.3-70B results in Appendix F). We compare against PromptGuard 2 (Chennabasappa et al., 2025), LlamaGuard (Meta AI, 2024), four Llama-as-Judge prompt variants (Llama-3.1-8B), and two dedicated prompt-injection detectors (ProtectAI Guard v2, Deepset promptinjection v2). Evaluation uses 5-fold CV, held-out test sets, and LODO.

5

R ESULTS

5.1

S TANDARD E VALUATION S EVERELY OVERESTIMATES G ENERALIZATION

Table 1 demonstrates that both 5-fold cross-validation and held-out test sets substantially overestimate out-of-distribution performance across every model we tested. Using logistic regression on Llama3.1-8B raw activations as a representative example, 5-fold CV achieves 0.996 AUC and the held-out test set achieves 0.997 AUC, while LODO reveals true generalization performance is only 0.912 6

[p.7]
Table 1: Evaluation protocol comparison for logistic regression on Llama-3.1-8B raw activations.
Standard CV and test-set evaluation overestimate true OOD performance by 8+ percentage points.
Evaluation Protocol  ROC AUC
5-Fold Cross-Validation  0.996
Held-Out Test Set  0.997
LODO (Pooled)  0.912
CV-LODO Gap  8.4 pp

AUC (Figure 1); aggregate CV-LODO AUC gaps across the four main models range from 8.0pp to 16.5pp (Table 3); partial Llama-3.3-70B results in Appendix F corroborate the pattern. The held-out test sets come from 6 datasets that provide official train-test splits: mosscap (27.7K samples including merged gandalf), jayavibhav (10K), qualifire (5K), enron (4K), safeguard (2K), and deepset (116). Critically, these test samples come from the same dataset sources as training data, allowing classifiers to exploit dataset-specific patterns. Table 2 shows the per-dataset accuracy gap for the 6 datasets with official test splits. The gaps range from 1.2% (safeguard) to 25.4% (jayavibhav). Four of these six datasets are mixed-class (jayavibhav 50%, qualifire 40%, safeguard 30%, deepset 37% malicious), yet still exhibit substantial gaps. Restricting to the five mixed-class datasets and excluding BIPIA (which is 95.3% malicious and acts as a near-single-class outlier), the weighted CV-LODO gap is 12.5pp (Appendix L) — confirming the gap is not driven by single-class artifacts. Conversely, the 8.4pp aggregate understates the gap on the datasets that matter: it is pulled toward zero by near-saturated benign sources (e.g., dolly, openorca), where CV and LODO both approach ceiling accuracy and contribute almost no gap to the average.

5.2  T HE G AP I S U NIVERSAL ACROSS F OUR M ODEL FAMILIES

To rule out architecture-specific artifacts, we replicate the CV-LODO comparison on three additional backbones spanning 2B-27B parameters across three families. Table 3 reports best-layer results per model. Partial Llama-3.3-70B results (Appendix F) corroborate the pattern but omit a paired CV AUC due to compute cost. The gap is universal but varies in magnitude. Per-dataset LODO accuracies are also heterogeneous and model-dependent — for example, InjecAgent is detected at 98.9% on Llama-3.1-8B but at 0% on Qwen-3.5-2B. The inconsistency itself is informative: practitioners cannot rely on a CV-validated classifier to generalize predictably to any specific deployment dataset.

7

[p.8]
Table 3: CV vs LODO on four base models. Layer/position selected by aggregate LODO accuracy
per model. CV AUC exceeds 0.99 for every model; LODO reveals 8-16pp gaps. Partial Llama-3.3-
70B replication (LODO AUC 0.910; no paired CV) in Appendix F; full per-dataset breakdowns there
as well.
Model  CV AUC  LODO AUC  Gap
Llama-3.1-8B  0.996  0.912  8.4pp
Gemma-3-27B  0.999  0.920  8.0pp
Qwen-3.5-4B  0.998  0.845  15.4pp
Qwen-3.5-2B  0.998  0.829  16.5pp

On Llama-3.1-8B, raw activations achieve the best pooled AUC (0.912), outperforming SAE features (0.838) and MLP (0.841) — aligning with Kantamneni et al. (2025) and DeepMind Mechanistic Interpretability Team (2025). This ordering is model-dependent, however: on Gemma-3-27B the SAE probe outperforms the raw probe under LODO (76.2% vs 68.3% weighted accuracy; Appendix F), so raw>SAE is a Llama-specific tendency rather than a universal law. [COUPÉ]

[p.9]
5.4

DATASET-I DENTITY S IGNAL I S E NTANGLED WITH S AFETY S IGNAL

Datasets are densely distinguishable. Training a logistic regression classifier to predict dataset identity from SAE features (layer 27) achieves 96.6% accuracy under 5-fold CV; the same dataset classifier on raw layer-31 activations reaches 89.1%, and on raw layer-27 activations 86.4% (Appendix E). Datasets are trivially distinguishable in every representation we tested.[COUPÉ] Dataset-identity and safety directions partially overlap. Projecting raw activations onto the orthogonal complement of the top-16 dataset-predictive directions (raw-space SVD of a 17-way LogReg dataset classifier) degrades LODO by 1.75pp aggregate, with strongly heterogeneous per-dataset effects (llmail +21.4pp, injecagent −34.4pp). Ten equal-rank random isotropic projections degrade LODO by −0.02 ± 0.13pp (p < 10−10 vs. targeted; bootstrap 95% CI on the gap [+1.63, +1.78] pp). The safety classifier’s weight direction also has 9.2% of its norm inside the dataset-predictive subspace versus 0.4% for random subspaces of equal rank (matching the isotropic theoretical value k/d = 0.39%). These results are consistent with directional overlap between dataset-identity and safety signal in this representation, though not proof of causal entanglement; the per-dataset heterogeneity indicates that uniformly removing dataset-identifying directions redistributes rather than reduces the gap. 28% of top SAE features are shortcuts, including context-dependent ones. Cross-referencing LODO retention with firing ratio (malicious/benign firing rate) for the top-50 SAE features ranked by full-model coefficient magnitude |wj | reveals two shortcut mechanisms (Table 5). Pure dataset shortcuts (Q1, 8 features) have weak class separation and low retention. Context-dependent shortcuts (Q2, 6 features) have strong class separation but still fail under LODO — for instance, one feature with high firing ratio has LODO retention of only 3% when jayavibhav is held out. Forty-two percent of shortcuts are context-dependent — they would not be flagged by simple firing-ratio checks alone. [COUPÉ]

[COUPÉ]The 28%/44% shortcut rates use a retention threshold of 0.5; the rate ranges from 14% (threshold 0.3, the most conservative shortcut count) to 56% (threshold 0.7, the most permissive) — see Appendix O.3. We report the 0.5 midpoint throughout for comparability and disclose the full sensitivity range. Shortcut-ablation results are reported in Appendix O.4. [COUPÉ]5.5

S TANDARD D OMAIN -G ENERALIZATION (DG) F IXES D O N OT C LOSE THE G AP

The directional-overlap finding above predicts that standard domain-generalization techniques — which assume domain-identifying and task-relevant signal can be separated — will struggle here. We test seven such strategies (DANN, subspace projection, two sample reweightings, category-aware reweighting, class balancing on Llama-3.1-8B, and SAE shortcut zeroing on Gemma-3-27B) with reasonable but non-exhaustive hyperparameter tuning. Aggregate LODO deltas range from −1.75pp 9

[p.10]
(subspace projection) to +0.7pp (SAE zeroing) — none close the 8.4pp Llama-8B gap; full table in Appendix G. For DANN specifically, we did not find a parameter set that both improved aggregate accuracy and remained stable across seeds; we make no claim that such a setting does not exist. The most informative intervention is subspace projection, which degrades LODO: consistent with the directional-overlap finding, closing the gap likely requires methods that disentangle dataset identity from safety signal. 5.6

P RODUCTION BASELINES AND LJ P ROMPT VARIANTS

Table 6 compares production guardrails against our activation-based classifier on 105K samples at
two natural operating points (thresholds 0.5 and 0.9). A per-attack-type breakdown across all methods
is in Appendix M.
Table 6: Detection rate (%) by attack category. PG=PromptGuard 2, LG=LlamaGuard, LJ=Llama-as-
Judge (zero-shot); Ours=LogReg on Llama-3.1-8B raw activations under LODO at fixed thresholds
0.5 (default) and 0.9 (conservative); per-fold optimal thresholds vary widely (Appendix P). PG/LG
cannot evaluate Agentic (no tool-schema support). Appendix P.2 provides matched-FPR comparisons.
Category  PG  LG  LJ  Ours(0.5)  Ours(0.9)
Harmful  36.7  97.4  85.8  69.7  64.7
Jailbreak  48.5  28.9  60.0  71.2  59.5
Indirect  37.3  27.4  7.1  66.7  53.1
Agentic  -  -  21.5  99.2  91.5
Extraction  100.0  15.2  31.8  79.2  68.7
Mixed  54.5  38.8  73.8  83.3  74.9
Benign FPR  0.4  3.0  4.4  6.8  3.7

PG and LG cannot represent tool schemas, so they are inapplicable to the agentic surface. At the threshold-0.9 operating point the probe’s FPR (3.7%) is comparable to LG’s (3.0%) while it leads on Jailbreak (+30.6pp), Indirect (+25.7pp), Agentic (covered exclusively), and Mixed (+36.1pp); LG retains its lead on conversational harmful refusals (97.4% vs 64.7%) where it is specifically trained. Appendix P.2 provides per-baseline FPR-matched detection rates. LJ prompt sensitivity. Single-prompt LJ evaluations can be misleading. Across four parseable LJ prompt variants tested on 10,054 indirect-injection + benign prompts, indirect-injection TPR ranges from 11% (FPR 1.4%) to 93% (FPR 18.9%) — an 8.5× range (Appendix J). The 93% TPR variant uses a “security analyst” framing but has 40.6% FPR on OpenOrca and 91.1% FPR on benign BIPIA emails — non-viable for deployment. At the 3.5% FPR operating point of the strongest deployable variant, our probe outperforms LJ by +22pp on indirect injection (68.2% vs 46.0%).[COUPÉ]

[p.11]
6

D ISCUSSION

Existing guardrails are not designed for agentic security. PG/LG target conversational safety; their inability to represent tool schemas or non-alternating roles is an architectural constraint, not just a training-data gap. Activation probes complement rather than replace these systems by covering the indirect and agentic surfaces they miss. Understanding the CV-LODO gap. The gap is a property of benchmark construction: classifiers exploit within-dataset regularities that do not transfer to new dataset distributions, and this holds across every model family we tested. Ablating the 14 identified SAE shortcuts moves pooled AUC by only −0.1pp because other features compensate via redundant decision boundaries — we therefore do not claim shortcuts cause the gap. The more direct evidence is the subspace projection result (§5.4): dataset-identifying and safety-relevant directions partially overlap, and closing the gap likely requires methods that can disentangle the two — an open challenge.

7

C ONCLUSION

LODO reveals an 8-16pp CV overestimate across four LLMs on prompt-attack detection (per-dataset gaps 1-25%). The dataset-identifying and safety-relevant subspaces appear to partially overlap (89%/96.6% dataset classifier; targeted subspace projection −1.75pp vs. −0.02pp for equal-rank random projections) — consistent with directional overlap, though not proof of causal entanglement — and standard domain-generalization fixes do not close the gap.

8

L IMITATIONS

White-box access requirement. Our activation-based approach requires access to model internals, limiting direct deployment with closed-source APIs.[COUPÉ] LODO is not adversarial robustness. LODO measures static distribution generalization, not robustness to adaptive attackers. A classifier with a small CV-LODO gap may still be vulnerable to novel attacks designed to evade it. Adversarial evaluation is a complementary requirement we do not address. Dataset-choice dependence. LODO treats each constituent dataset as a domain. When component datasets share methodology, LODO understates the deployment gap; when they are unrepresentative of production traffic, LODO may be pessimistic or optimistic depending on direction.[COUPÉ] [COUPÉ]No mitigation provided. We establish the gap and show it resists seven standard domaingeneralization interventions, but do not present a method that closes it. We view the diagnostic contribution as actionable independently — practitioners can use LODO to detect gap-prone benchmarks, filter dataset-artifact features from explanations, and avoid overpromising on production performance based on inflated CV metrics — but a definitive solution remains open. 11

[COUPÉ : p.1 pied de page ; p.2 figure 1 et liste des contributions ; p.3 état de l'art sur les détecteurs d'attaques par requête et sur les autoencodeurs parcimonieux ; p.4 figure 2 (exemples de requêtes) ; p.5 détails de configuration des classificateurs et des autoencodeurs parcimonieux ; p.6 section 3.5 (explications pondérées) ; p.1 premier paragraphe de l'introduction ; p.7 tableau 2 (écarts par jeu de données) ; p.8 tableau 4 (résultats par jeu de données) ; p.9 tableau 5 et mesures de qualité des traits ; p.10 sensibilité à l'invite du juge, détecteurs de texte ajustés et section 5.7 ; p.11 coût de calcul et portée interprétative ; p.12-27 bibliographie et annexes A à P]

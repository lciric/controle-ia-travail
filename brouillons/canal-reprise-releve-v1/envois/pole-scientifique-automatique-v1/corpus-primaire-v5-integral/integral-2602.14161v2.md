# TEXTE INTÉGRAL — arXiv:2602.14161v2

- Identifiant : arXiv:2602.14161v2
- Titre (tel qu'écrit dans le PDF) : When Benchmarks Lie: Evaluating Malicious Prompt Classifiers Under True Distribution Shift
- PDF source : `docs/sources/pdf/2602.14161v2.pdf` ; SHA-256 du PDF : `7831c848841eca32bcbb1e18cd35f644cfe5a8af8f0f003623c4e1bdd6e03c00` (compagnon `.sha256` vérifié par `sha256sum -c` avant lecture)
- Outil d'extraction : `pdftotext -layout -enc UTF-8` (pdftotext version 24.02.0), page par page, marqueur `[p.N]` au début de chaque page (N = numéro de page du PDF, à partir de 1)
- Nombre de pages : 27
- Caractères de contrôle produits par l'extraction (glyphes de polices sans correspondance : délimiteurs de formules, texte de figures à police codée) : 1, les caractères nuls supprimés, les autres remplacés par le caractère de remplacement U+FFFD (position gardée) ; pages : 5 (1)
- Nombre de caractères du texte extrait (marqueurs `[p.N]` compris, en-tête exclu) : 90807
- Mention : texte intégral, aucun retrait, contenu d'attaque verbatim possible — dépôt privé seulement (jamais dans la copie expurgée publique ; règle de sûreté modifiée par R-439).
- Provenance : tout chiffre repris ailleurs doit citer la page `[p.N]` et être relu sur le PDF empreinté (R7). La mise en page en colonnes, les formules et les tableaux peuvent être mal ordonnés dans l'extraction : se reporter au PDF.

---

[p.1]

                                         W HEN B ENCHMARKS L IE : E VALUATING M ALICIOUS
                                         P ROMPT C LASSIFIERS U NDER T RUE D ISTRIBUTION
                                         S HIFT


                                          Max Fomin
                                          Zenity
                                          maxf@zenity.io



                                                                                      A BSTRACT

                                                  Detecting prompt injection, jailbreak attacks, and harmful requests is critical
                                                  for deploying LLM-based agents safely, yet current evaluation practices in this
                                                  literature overestimate generalization. We train activation-based classifiers (linear
                                                  probes on LLM hidden states) on a benchmark of 18 datasets (prompt attacks
                                                  plus benign sources) and propose Leave-One-Dataset-Out (LODO) evaluation,
arXiv:2602.14161v2 [cs.LG] 19 Jul 2026




                                                  where the held-out dataset is never seen during training. Across four LLMs from
                                                  three families (Llama-3.1-8B, Gemma-3-27B, Qwen-3.5-2B/4B), standard cross-
                                                  validation reports a pooled AUC 8.0–16.5 points higher than LODO; per-dataset
                                                  held-out-test-vs-LODO accuracy gaps span 1–25 points.
                                                  To understand the gap, we analyze the LODO stability of a linear probe’s per-
                                                  feature classifier coefficients, defining a retention metric for sparse-autoencoder
                                                  (SAE) features that flags dataset-dependent shortcuts. 28–44% of top SAE features
                                                  are shortcuts across models, a dataset-identity classifier reaches 96.6%, and the
                                                  dataset-identifying and safety-relevant subspaces partially overlap (§5.4). Stan-
                                                  dard domain-generalization fixes such as adversarial training, subspace projection,
                                                  sample reweighting, and class balancing do not close the gap (§5.5).
                                                  Finally, we show LODO-weighted SAE attributions filter dataset artifacts for more
                                                  reliable per-prompt explanations. We release our framework at https://gith
                                                  ub.com/maxf-zn/prompt-mining so future prompt-attack classifiers can
                                                  be evaluated under LODO alongside CV.


                                         1    I NTRODUCTION

                                         LLM-based agents are increasingly deployed in autonomous applications where they process external
                                         data sources such as emails, documents, tool outputs, and API responses (Greshake et al., 2023). This
                                         agentic paradigm introduces critical security vulnerabilities: attackers can embed malicious instruc-
                                         tions in external data to hijack agent behavior, a class of attacks known as prompt injection (Perez
                                         & Ribeiro, 2022). Unlike jailbreaking attacks, which attempt to bypass model safety mechanisms,
                                         prompt injection attacks exploit the fundamental inability of agents to distinguish between trusted
                                         user instructions and untrusted data (Abdelnabi et al., 2025a). The security implications are severe:
                                         OWASP ranks prompt injection as the top vulnerability for LLM applications (OWASP Foundation,
                                         2025).
                                         Recent work has developed classifiers to detect prompt injection, jailbreak, and harmful-request
                                         attacks, using approaches ranging from fine-tuned BERT models (Chennabasappa et al., 2025) to
                                         activation-based probes (Abdelnabi et al., 2025a). These classifiers are typically trained and evalu-
                                         ated on aggregated benchmarks combining multiple attack datasets (e.g., AdvBench, HarmBench,
                                         WildJailbreak) and benign datasets (e.g., Enron emails, OpenOrca). Standard evaluation protocols
                                         use train-test splits where test samples come from the same dataset sources as training, reporting
                                         near-perfect performance with AUC scores exceeding 0.99 (Abdelnabi et al., 2025a; Saglam et al.,
                                         2025) — a result we replicate in Table 1.
                                         Published at the First Workshop on Agents in the Wild: Safety, Security, and Beyond (AIWILD) at ICLR 2026.
                                         Copyright 2026 by the author(s).


                                                                                             1

[p.2]

Figure 1: Method overview. We compile 18 datasets (105K samples) spanning jailbreaks, indirect
injection, harmful requests, and benign prompts. We extract activations from Llama-3.1-8B-Instruct
at layer 31 (raw) and through a layer-27 SAE encoder (sparse features). Leave-One-Dataset-Out
(LODO) evaluation trains on N −1 datasets and tests on the held-out dataset, revealing that standard
CV overestimates performance by 8.4 percentage points (0.996 vs 0.912 AUC). The gap is universal
across four models spanning 2B-27B (plus partial Llama-70B results in Appendix F).




However, this evaluation methodology overestimates true generalization. When training and test folds
contain samples from the same datasets, classifiers can exploit dataset-identity signals — features
that indicate dataset provenance rather than attack semantics. A classifier reaching 99% AUC may
simply learn that “samples formatted like WildJailbreak are malicious” and “samples formatted like
Enron are benign,” without learning generalizable attack patterns. This echoes broader findings in
machine learning that models often succeed for the wrong reasons (McCoy et al., 2019; Geirhos
et al., 2020), and is exacerbated when benchmark datasets are single-class (entirely malicious or
entirely benign): any feature that identifies the dataset automatically predicts the class label, making
dataset-identity exploitation trivial.



Contributions.
• LODO is necessary for prompt-attack classifiers. Standard CV overestimates generalization by
  8–16pp across four LLMs (per-dataset gaps 1–25pp); lifting leave-one-domain-out CV (Gulrajani
  & Lopez-Paz, 2021; Koh et al., 2021) to the dataset level is required to surface this gap.
• Retention metric and shortcut taxonomy. A LODO-coefficient stability score and a two-axis
  taxonomy (pure vs. context-dependent shortcuts) flag dataset-dependent SAE features that firing-
  ratio heuristics miss.
• Dataset-identity / safety overlap. A dataset-identity classifier (96.6% SAE / 89% raw) combined
  with subspace-projection and alignment measurements shows that the dataset-identifying and
  safety-relevant directions partially overlap.
• Production and baseline comparison. At matched benign FPR, activation probes lead Prompt-
  Guard 2, LlamaGuard, and Llama-as-Judge on indirect and agentic attacks; we additionally
  benchmark dedicated prompt-injection detectors (ProtectAI, Deepset) at their native operating
  points (Section 5.6, Appendix P.2, Appendix I).
• LODO-weighted explanations. Weighting SAE attributions by coefficient retention (zj wj rj )
  filters dataset-artifact features from per-prompt explanations, re-ranking the top-20 features for
  ∼98% of samples (Section 5.7).


                                                   2

[p.3]

2    R ELATED W ORK

Prompt-attack detection. Prompt injection (Perez & Ribeiro, 2022; Greshake et al., 2023; Liu
et al., 2024) and jailbreak attacks have motivated detectors spanning fine-tuned classifiers and
activation or attention-based probes. PromptGuard 2 (Chennabasappa et al., 2025) and LlamaGuard
(Meta AI, 2024) are classifier-based guardrails with text-only interfaces; we treat them as production
baselines (Section 5) and note this interface precludes the tool-schema needed for agentic attacks.
TaskTracker (Abdelnabi et al., 2025a) is the closest activation-probe baseline; it holds out attack
types from training but trains and evaluates within the same constituent datasets, leaving dataset-level
generalization unexamined. Marks & Tegmark (2024) distinguish correlational from causal directions
in linear probes for truthfulness; we ask the orthogonal question of whether prompt-attack probes
transfer across datasets, and quantify the gap with LODO. Goodfire AI (2025) compare activation
probes against LLM-as-judge for PII on proprietary data; we run the analogous comparison on public
prompt-attack benchmarks.


Contemporaneous and adversarial-robustness work. Constitutional Classifiers (Sharma et al.,
2025; Cunningham et al., 2026) and Circuit Breakers (Zou et al., 2024) optimize adversarial ro-
bustness via red-teaming or representation intervention — targeting worst-case attackers, whereas
LODO measures static distribution shift. PromptArmor (Shi et al., 2025) is a contemporaneous
deployment-oriented LLM-as-judge defense for agentic prompt injection: a single engineered judge
prompt plus a downstream filtering pipeline; we instead characterize how our Llama-as-Judge (LJ)
baseline’s accuracy varies across prompt templates (Section 5). Two contemporaneous works target
attention rather than the activations we study: AISA (Song et al., 2026) intervenes at decoding time
via attention-head steering and logits modification, while AlignSentinel (Jia et al., 2026) classifies
features derived from attention maps. PIArena (Geng et al., 2026) provides a unified extensible
platform for evaluating prompt-injection defenses; our contribution targets the evaluation protocol
itself.


SAE features for classification and interpretability. SAEs decompose activations into sparse,
interpretable features (Bricken et al., 2023; Lieberum et al., 2024). Gallifant et al. (2025) achieve
macro-F1>0.8 on safety-critical text classification with SAE probes; we reproduce a comparable
single-dataset CV number on jailbreak data but show the LODO gap is ∼8pp. Kantamneni et al.
(2025) compare SAE vs raw-activation probes across 113 tasks and find SAE probes underperform
in 98% of settings; our 0.912 vs 0.838 AUC under LODO is a direct corroboration. Le Bail et al.
(2025) uses SAE features to explain model predictions, and Zhao et al. (2024) extract high-impact
concepts from hidden activations for the same purpose; we add an LODO-weighted attribution
filter that removes dataset-artifact features (Section 5.7). Riegler & Torpmann-Hagen (2026) show
single-feature SAE inspection mislabels causal axes via pairwise interactions, an adjacent diagnosis
of SAE explanation fragility.


Dataset shortcuts and domain generalization. Shortcut learning is well-documented in vision and
NLI (Geirhos et al., 2020; McCoy et al., 2019). Group DRO (Sagawa et al., 2020) minimizes worst-
group loss over predefined groups, and Just Train Twice (Liu et al., 2021) upweights individually
misclassified examples after an initial training pass; both operate within a single training distribution
where the group labels (or misclassifications) identify the shortcut, whereas in our setting the dataset
itself is the shortcut. Our reweighting experiments (Appendix G) confirm sample-level methods do
not close the LODO gap.


Adaptive attacks and evaluation pitfalls. Nasr et al. (2025) bypass twelve recent jailbreak/prompt-
injection defenses with adaptive attacks, arguing static evaluations overstate robustness; their critique
targets the adversarial axis, ours the distribution-shift axis, and the two are complementary pre-
deployment diagnostics. PromptShield (Jacob et al., 2025) curates a deployment-oriented prompt-
injection benchmark and a fine-tuned Llama-3-8B detector trained on it — a deployable artifact,
whereas our contribution targets the evaluation methodology that any such detector is measured
against.


                                                   3

[p.4]

Figure 2: Example prompts from our benchmark illustrating the diversity of benign and malicious
samples. Benign prompts (left) include general knowledge questions, business requests, and technical
support queries. Malicious prompts (right) range from direct harmful requests (advbench), jailbreak
attempts (wildjailbreak), and indirect prompt injections embedded in tool calls (InjecAgent).


3     M ETHODS
3.1   P ROBLEM S ETUP

We address binary classification of LLM inputs as malicious or benign. Malicious inputs span four
families: (i) harmful requests for restricted content; (ii) jailbreaks that attempt to bypass safety
via roleplay, framing, or other prompt engineering; (iii) prompt injections that hijack instructions,
including indirect injections embedded in external data the agent processes (emails, code, tool outputs,
retrieved documents); and (iv) extraction attacks that elicit hidden system information.

Threat Model. The defender has white-box access to LLM activations during inference but cannot
modify the underlying model — the setting addressed by activation-probe detectors. We compare
against text-only baselines that lack this access (§5).

Dataset Composition. We compile 18 datasets covering these attack families plus benign sources
(Table 7, Figure 2). Most are capped at 10K samples for tractable activation extraction; BIPIA uses
15K to cover its three context types. The full benchmark totals 105K samples (47% malicious); under
LODO each dataset serves in turn as the held-out test set, so there is no fixed train/test split.

3.2   ACTIVATION -BASED C LASSIFICATION

Following Abdelnabi et al. (2025a), we extract activations from the LLM’s residual stream as
input features for classification. These classifiers are also known as probes or linear probes in the
interpretability literature; we use the terms interchangeably. For a text input x, we apply the model’s
chat template and extract the activation vector hl ∈ Rd at layer l from the last token of the user
message (before the generation-prompt tokens; see Appendix C.3):
                                           hl = LLMl (x),                                           (1)
where d is the model’s hidden dimension. We evaluate four LLMs spanning 2B-27B parameters
across three families: Llama-3.1-8B-Instruct (Llama Team, AI @ Meta, 2024), Gemma-3-27B
(Gemma Team, 2025), and Qwen-3.5-2B/4B (Qwen Team, 2026), plus a partial Llama-3.3-70B
replication (Appendix F). SAE-based analyses use Llama-3.1-8B (layer-27 SAE from Arditi (2024))
and Gemma-3-27B (Gemma Scope 2 (McDougall et al., 2025) at layer 42), since these are the models
with pre-trained SAEs publicly available; remaining analyses cover the four main models.


                                                   4

[p.5]

Raw Activations. Our primary classifier operates on raw activations from layer 31 (the final layer,
indexed 0-31), captured at the last user-message token (immediately before the assistant generation
prefix). Layer 27 at the same position achieves marginally higher aggregate LODO weighted accuracy
(82.3% vs 81.8%), but no layer/position configuration dominates per-dataset: harmbench prefers the
final generation-prompt token (65% vs 43% at L31); llmail prefers the last user-message token (71%
vs 29%); InjecAgent peaks at L25-L27 (Appendix D). We report L31 at the last user-message token
as the principled default (final residual stream; matches the layer commonly used in prior probing
work) and emphasize that the core finding — heterogeneous per-dataset LODO performance —
persists across all configurations tested.

SAE Features. We additionally experiment with sparse-autoencoder (SAE) features from layer 27
— the deepest layer for which a pre-trained SAE was available for this model (Arditi, 2024). SAEs
decompose activations into a sparse, higher-dimensional representation:
                                      z = σ(Wenc h + benc ),                                   (2)
                                                                                  dsae
where σ is a sparsifying activation (e.g., ReLU, JumpReLU, TopK) and z ∈ R is sparse with
dsae ≫ dmodel (the Llama-3.1-8B SAE we use has dsae = 131,072). SAE features are hypothesized to
correspond to interpretable concepts; we show they are also susceptible to dataset shortcuts.

Classifiers. We use standard classifiers (logistic regression with L2 regularization C=1.0, scikit-
learn LogisticRegression solver lbfgs, max iter 104 , class weight=‘balanced’;
2-layer MLP, hidden 512, dropout 0.1, Adam 10−3 , 20 epochs) to isolate evaluation-protocol ef-
fects rather than architecture design. Splits use scikit-learn’s StratifiedKFold(n splits=5,
shuffle=True, random state=42) for CV; LODO folds are deterministic by dataset iden-
tity, and logistic regression with the lbfgs solver is deterministic given fixed regularization. This
complements work optimizing probe architectures for deployment (Sharma et al., 2025; Cunningham
et al., 2026).

3.3   L EAVE -O NE -DATASET-O UT (LODO) E VALUATION

Leave-one-domain-out cross-validation is an established protocol in domain generalization (Gulrajani
& Lopez-Paz, 2021; Koh et al., 2021); our contribution is not the protocol itself but applying it at
the dataset level to prompt-attack classification (where it has not been adopted) and quantifying
the resulting CV-LODO gap. For each dataset Di in our benchmark, we train a classifier on all
other datasets {Dj : j ̸= i} and evaluate on the held-out Di . This measures true out-of-distribution
generalization, as the classifier has never seen any examples from the test dataset’s distribution.
Formally, let D = {D1 , . . . , DK } be our K datasets. For each i, we compute:
                                                                  �
                                    LODOi = Metric fD\Di , Di ,                                (3)
where fD\Di is trained on all datasets except Di . We report both per-dataset metrics and pooled
metrics across all held-out predictions. We additionally compare LODO against leave-one-category-
out (LOCO), which holds out entire attack categories — LODO is strictly more fine-grained, and the
LODO/LOCO comparison (Appendix H) quantifies what per-dataset granularity adds.

3.4   DATASET S HORTCUT A NALYSIS

We perform shortcut analysis on SAE features rather than raw activations because SAE features
are designed to be interpretable: each feature ideally corresponds to a single semantic concept. In
contrast, individual neurons in raw activations are polysemantic, encoding multiple unrelated concepts
that activate together (Bricken et al., 2023). This polysemanticity makes it difficult to characterize
what patterns a given neuron detects, whereas SAE features can be examined via their max-activating
examples.
To quantify how much classifier performance depends on dataset-specific features, we introduce the
LODO coefficient retention metric. For each feature j, let wj be its coefficient in the full classifier
     (−i)
and wj    its coefficient when dataset Di is held out. The retention for feature j is:
                                                       (−i)
                                                   wj
                                          rj = min     .                                            (4)
                                                i   wj

                                                  5

[p.6]

Features with rj ≈ 1 are stable across dataset holdouts and likely capture genuine attack patterns.
Features with rj ≪ 1 or rj < 0 (sign flip) are dataset shortcuts — their predictive value depends on
specific datasets being present in training. Features with |wj | < 10−8 are excluded from retention
analysis, and rj is clipped to [0, 2] for numerical stability. We identify two types:
• Pure dataset shortcuts: features that directly predict dataset identity (e.g., email formatting for
  Enron, code patterns for specific injection datasets).
• Context-dependent shortcuts: features that fire across datasets but derive class signal from specific
  dataset compositions (e.g., a feature active on both malicious and benign samples, but whose class
  correlation depends on which datasets are included).
To validate this analysis, we train a separate dataset classifier that predicts which dataset a sample
belongs to from activations alone. High accuracy indicates that datasets are easily distinguishable in
feature space, enabling shortcut exploitation.

3.5   LODO-W EIGHTED E XPLANATIONS

For interpretable detection, we want to explain why a classifier flagged a particular input as malicious.
A natural approach identifies which features contributed most. For input x with SAE features z, the
influence of feature j is zj · wj . However, high-influence features may be dataset shortcuts rather
than genuinely predictive features. We propose LODO-weighted explanations:

                                     influenceLODO
                                              j    = zj · wj · rj ,                                  (5)
where rj is the LODO retention score. This downweights dataset shortcuts and promotes features
that remained predictive across distribution shifts.

4     E XPERIMENTS

We answer five questions: (1) How much does standard cross-validation overestimate generalization
compared to LODO? (2) Does the gap extend beyond a single model family? (3) What fraction
of learned features are dataset shortcuts, and what fraction of the gap can we close with standard
mitigations? (4) How do activation-based classifiers compare to production baselines and LLM-as-
judge under fair operating points? (5) Can LODO-stable features provide reliable explanations?

4.1   E XPERIMENTAL S ETUP

Dataset. Our benchmark comprises 18 datasets (105K samples, 47% malicious) spanning direct
jailbreaks, indirect injection, extraction attacks, and benign sources. For evaluation, we merge
Gandalf (114 samples) into Mosscap — both use identical system prompts for password protection
(Appendix B) — yielding 17 datasets for LODO results; shortcut analysis uses the original 18. Six
datasets are 100% malicious and five are 100% benign; the remaining six are mixed-class. We audit
cross-dataset near-duplicate overlap in Appendix K.

Models and Baselines. We evaluate Llama-3.1-8B, Gemma-3-27B, and Qwen-3.5-2B/4B in the
main body (plus partial Llama-3.3-70B results in Appendix F). We compare against PromptGuard 2
(Chennabasappa et al., 2025), LlamaGuard (Meta AI, 2024), four Llama-as-Judge prompt variants
(Llama-3.1-8B), and two dedicated prompt-injection detectors (ProtectAI Guard v2, Deepset prompt-
injection v2). Evaluation uses 5-fold CV, held-out test sets, and LODO.

5     R ESULTS

5.1   S TANDARD E VALUATION S EVERELY OVERESTIMATES G ENERALIZATION

Table 1 demonstrates that both 5-fold cross-validation and held-out test sets substantially overestimate
out-of-distribution performance across every model we tested. Using logistic regression on Llama-
3.1-8B raw activations as a representative example, 5-fold CV achieves 0.996 AUC and the held-out
test set achieves 0.997 AUC, while LODO reveals true generalization performance is only 0.912


                                                   6

[p.7]

Table 1: Evaluation protocol comparison for logistic regression on Llama-3.1-8B raw activations.
Standard CV and test-set evaluation overestimate true OOD performance by 8+ percentage points.

                                 Evaluation Protocol       ROC AUC
                                 5-Fold Cross-Validation     0.996
                                 Held-Out Test Set           0.997
                                 LODO (Pooled)               0.912
                                 CV-LODO Gap                 8.4 pp


AUC (Figure 1); aggregate CV-LODO AUC gaps across the four main models range from 8.0pp to
16.5pp (Table 3); partial Llama-3.3-70B results in Appendix F corroborate the pattern.
The held-out test sets come from 6 datasets that provide official train-test splits: mosscap (27.7K
samples including merged gandalf), jayavibhav (10K), qualifire (5K), enron (4K), safeguard (2K),
and deepset (116). Critically, these test samples come from the same dataset sources as training data,
allowing classifiers to exploit dataset-specific patterns.
Table 2 shows the per-dataset accuracy gap for the 6 datasets with official test splits. The gaps
range from 1.2% (safeguard) to 25.4% (jayavibhav). Four of these six datasets are mixed-class
(jayavibhav 50%, qualifire 40%, safeguard 30%, deepset 37% malicious), yet still exhibit substantial
gaps. Restricting to the five mixed-class datasets and excluding BIPIA (which is 95.3% malicious
and acts as a near-single-class outlier), the weighted CV-LODO gap is 12.5pp (Appendix L) —
confirming the gap is not driven by single-class artifacts. Conversely, the 8.4pp aggregate understates
the gap on the datasets that matter: it is pulled toward zero by near-saturated benign sources (e.g.,
dolly, openorca), where CV and LODO both approach ceiling accuracy and contribute almost no gap
to the average.

Table 2: Per-dataset accuracy comparison between LODO (entire dataset held out) and held-out test
set (samples from the same source as training); Llama-3.1-8B raw activations. Test N is each dataset’s
official held-out test split, which is not subject to our 10K-per-dataset cap; the LODO evaluation
instead uses our capped benchmark pool (e.g., mosscap 10,114 samples, incl. 114 merged gandalf),
so the two accuracy columns for a given dataset are computed on different sample pools.

                       Dataset      Test N   Test Acc      LODO Acc      Gap
                       mosscap      27,728      99.5%         79.4%     +20.1%
                       jayavibhav   10,000      94.5%         69.1%     +25.4%
                       qualifire     5,000      95.8%         77.8%     +18.0%
                       enron         4,000      99.2%         82.6%     +16.6%
                       safeguard     2,060      97.9%         96.7%     +1.2%
                       deepset         116      80.2%         77.7%     +2.5%


5.2   T HE G AP I S U NIVERSAL ACROSS F OUR M ODEL FAMILIES

To rule out architecture-specific artifacts, we replicate the CV-LODO comparison on three additional
backbones spanning 2B-27B parameters across three families. Table 3 reports best-layer results per
model. Partial Llama-3.3-70B results (Appendix F) corroborate the pattern but omit a paired CV
AUC due to compute cost.
The gap is universal but varies in magnitude. Per-dataset LODO accuracies are also heterogeneous
and model-dependent — for example, InjecAgent is detected at 98.9% on Llama-3.1-8B but at 0% on
Qwen-3.5-2B. The inconsistency itself is informative: practitioners cannot rely on a CV-validated
classifier to generalize predictably to any specific deployment dataset.




                                                  7

[p.8]

Table 3: CV vs LODO on four base models. Layer/position selected by aggregate LODO accuracy
per model. CV AUC exceeds 0.99 for every model; LODO reveals 8-16pp gaps. Partial Llama-3.3-
70B replication (LODO AUC 0.910; no paired CV) in Appendix F; full per-dataset breakdowns there
as well.

                        Model            CV AUC        LODO AUC         Gap
                        Llama-3.1-8B       0.996            0.912       8.4pp
                        Gemma-3-27B        0.999            0.920       8.0pp
                        Qwen-3.5-4B        0.998            0.845      15.4pp
                        Qwen-3.5-2B        0.998            0.829      16.5pp




5.3   M ETHOD C OMPARISON U NDER LODO

Table 4 compares our classifier architectures under LODO across all 17 datasets.


Table 4: Per-dataset LODO accuracy (%) on Llama-3.1-8B with threshold=0.5, and pooled AUC
(N=105,034). Macro-averaged accuracy (80.6% raw) closely tracks the weighted average (81.8%),
confirming results are not dominated by large datasets. DeLong 95% CIs for pooled AUC: Raw 0.912
(0.911-0.915), SAE 0.838 (0.836-0.841), MLP 0.841 (0.839-0.843). † Includes gandalf summarization
(114 samples).

                   Dataset                   N     %Mal      Raw     SAE      MLP
                     Mixed-class datasets:
                   BIPIA                 15000         95     63.1   26.1       60.1
                   deepset                  546        37     77.7   80.6       78.4
                   jayavibhav            10000         50     69.1   76.6       75.6
                   qualifire               5000        40     77.8   76.5       77.8
                   safeguard               8236        30     96.7   95.7       97.4
                   wildjailbreak           2210        91     78.6   80.7       79.6
                     100% malicious (accuracy = recall):
                   advbench               520       100       90.8    92.9     97.1
                   harmbench              400       100       42.8    36.2     44.8
                   injecagent            1054       100       98.9   100.0    100.0
                   llmail                9998       100       71.4   58.4     45.8
                   mosscap†             10114       100       79.4    65.2    84.4
                   yanismiraoui          1034       100       55.8    41.9     45.6
                     100% benign (accuracy = 1−FPR):
                   10k prompts           9924       0         92.4   89.1       92.4
                   dolly 15k            10000       0         99.6   99.8       99.8
                   enron                10000       0         82.6   85.7       81.1
                   openorca              9997       0         98.0   98.3       98.9
                   softAge               1001       0         95.1   95.6       96.4
                   Weighted Avg Acc                           81.8    74.5     80.1
                   Macro Avg Acc                              80.6    76.4     79.7
                   Pooled AUC                                0.912   0.838    0.841



On Llama-3.1-8B, raw activations achieve the best pooled AUC (0.912), outperforming SAE features
(0.838) and MLP (0.841) — aligning with Kantamneni et al. (2025) and DeepMind Mechanistic
Interpretability Team (2025). This ordering is model-dependent, however: on Gemma-3-27B the SAE
probe outperforms the raw probe under LODO (76.2% vs 68.3% weighted accuracy; Appendix F),
so raw>SAE is a Llama-specific tendency rather than a universal law. Despite this gap, SAE features
enable interpretable detection (Section 5.7); the LODO retention metric identifies which features
to trust. A training-free Mahalanobis-distance baseline (LPM) trails LogReg by 5.8pp weighted
accuracy under LODO, with the largest gaps on indirect injection (Appendix N).


                                                   8

[p.9]

5.4   DATASET-I DENTITY S IGNAL I S E NTANGLED WITH S AFETY S IGNAL

Datasets are densely distinguishable. Training a logistic regression classifier to predict dataset
identity from SAE features (layer 27) achieves 96.6% accuracy under 5-fold CV; the same dataset
classifier on raw layer-31 activations reaches 89.1%, and on raw layer-27 activations 86.4% (Ap-
pendix E). Datasets are trivially distinguishable in every representation we tested. Within-dataset
text-embedding similarity exceeds cross-dataset similarity (0.635 vs 0.545, p=0.005); in activation
space the difference is larger (0.751 vs 0.662, p<0.001).

Dataset-identity and safety directions partially overlap. Projecting raw activations onto the or-
thogonal complement of the top-16 dataset-predictive directions (raw-space SVD of a 17-way LogReg
dataset classifier) degrades LODO by 1.75pp aggregate, with strongly heterogeneous per-dataset
effects (llmail +21.4pp, injecagent −34.4pp). Ten equal-rank random isotropic projections degrade
LODO by −0.02 ± 0.13pp (p < 10−10 vs. targeted; bootstrap 95% CI on the gap [+1.63, +1.78] pp).
The safety classifier’s weight direction also has 9.2% of its norm inside the dataset-predictive sub-
space versus 0.4% for random subspaces of equal rank (matching the isotropic theoretical value
k/d = 0.39%). These results are consistent with directional overlap between dataset-identity and
safety signal in this representation, though not proof of causal entanglement; the per-dataset het-
erogeneity indicates that uniformly removing dataset-identifying directions redistributes rather than
reduces the gap.

28% of top SAE features are shortcuts, including context-dependent ones. Cross-referencing
LODO retention with firing ratio (malicious/benign firing rate) for the top-50 SAE features ranked
by full-model coefficient magnitude |wj | reveals two shortcut mechanisms (Table 5). Pure dataset
shortcuts (Q1, 8 features) have weak class separation and low retention. Context-dependent shortcuts
(Q2, 6 features) have strong class separation but still fail under LODO — for instance, one feature
with high firing ratio has LODO retention of only 3% when jayavibhav is held out. Forty-two percent
of shortcuts are context-dependent — they would not be flagged by simple firing-ratio checks alone.

Table 5: Shortcut taxonomy for top-50 SAE features (Llama-3.1-8B). Rows: LODO retention;
columns: malicious-to-benign firing ratio.

                                          Firing Ratio <1.5    Firing Ratio ≥1.5
                      LODO Shortcut             8 (Q1)               6 (Q2)
                      LODO Stable              13 (Q3)              23 (Q4)

Single-class datasets contribute the majority of shortcuts (e.g., mosscap 6 features, llmail 3, yanismi-
raoui 2), with smaller contributions from mixed-class datasets (jayavibhav, safeguard, BIPIA). On
Gemma-3-27B the picture is more pronounced: 44% of top-50 SAE features are shortcuts (vs 28%
on Llama-3.1-8B; Appendix F). The 28%/44% shortcut rates use a retention threshold of 0.5; the rate
ranges from 14% (threshold 0.3, the most conservative shortcut count) to 56% (threshold 0.7, the
most permissive) — see Appendix O.3. We report the 0.5 midpoint throughout for comparability and
disclose the full sensitivity range. Shortcut-ablation results are reported in Appendix O.4.

Generalizable features dominate shortcuts across metrics. To check that the retention threshold
is identifying genuinely informative features rather than an artifact of the metric itself, we compare
the two groups defined by rj on four independent feature-quality measures — class-separation
effect size (Cohen’s d), information gain, SHAP-based class differential, and cross-dataset firing-rate
consistency. Generalizable features (rj > 0.5) significantly outperform shortcut features (rj ≤ 0.5)
on all four (all p < 0.05; Table 16).

5.5   S TANDARD D OMAIN -G ENERALIZATION (DG) F IXES D O N OT C LOSE THE G AP

The directional-overlap finding above predicts that standard domain-generalization techniques —
which assume domain-identifying and task-relevant signal can be separated — will struggle here. We
test seven such strategies (DANN, subspace projection, two sample reweightings, category-aware
reweighting, class balancing on Llama-3.1-8B, and SAE shortcut zeroing on Gemma-3-27B) with
reasonable but non-exhaustive hyperparameter tuning. Aggregate LODO deltas range from −1.75pp


                                                   9

[p.10]

(subspace projection) to +0.7pp (SAE zeroing) — none close the 8.4pp Llama-8B gap; full table in
Appendix G. For DANN specifically, we did not find a parameter set that both improved aggregate
accuracy and remained stable across seeds; we make no claim that such a setting does not exist. The
most informative intervention is subspace projection, which degrades LODO: consistent with the
directional-overlap finding, closing the gap likely requires methods that disentangle dataset identity
from safety signal.

5.6   P RODUCTION BASELINES AND LJ P ROMPT VARIANTS

Table 6 compares production guardrails against our activation-based classifier on 105K samples at
two natural operating points (thresholds 0.5 and 0.9). A per-attack-type breakdown across all methods
is in Appendix M.

Table 6: Detection rate (%) by attack category. PG=PromptGuard 2, LG=LlamaGuard, LJ=Llama-as-
Judge (zero-shot); Ours=LogReg on Llama-3.1-8B raw activations under LODO at fixed thresholds
0.5 (default) and 0.9 (conservative); per-fold optimal thresholds vary widely (Appendix P). PG/LG
cannot evaluate Agentic (no tool-schema support). Appendix P.2 provides matched-FPR comparisons.

                     Category        PG     LG      LJ     Ours(0.5)   Ours(0.9)
                     Harmful         36.7   97.4    85.8     69.7        64.7
                     Jailbreak       48.5   28.9    60.0     71.2        59.5
                     Indirect        37.3   27.4     7.1     66.7        53.1
                     Agentic          -      -      21.5     99.2        91.5
                     Extraction     100.0   15.2    31.8     79.2        68.7
                     Mixed           54.5   38.8    73.8     83.3        74.9
                     Benign FPR      0.4    3.0     4.4       6.8         3.7


PG and LG cannot represent tool schemas, so they are inapplicable to the agentic surface. At the
threshold-0.9 operating point the probe’s FPR (3.7%) is comparable to LG’s (3.0%) while it leads on
Jailbreak (+30.6pp), Indirect (+25.7pp), Agentic (covered exclusively), and Mixed (+36.1pp); LG
retains its lead on conversational harmful refusals (97.4% vs 64.7%) where it is specifically trained.
Appendix P.2 provides per-baseline FPR-matched detection rates.

LJ prompt sensitivity. Single-prompt LJ evaluations can be misleading. Across four parseable LJ
prompt variants tested on 10,054 indirect-injection + benign prompts, indirect-injection TPR ranges
from 11% (FPR 1.4%) to 93% (FPR 18.9%) — an 8.5× range (Appendix J). The 93% TPR variant
uses a “security analyst” framing but has 40.6% FPR on OpenOrca and 91.1% FPR on benign BIPIA
emails — non-viable for deployment. At the 3.5% FPR operating point of the strongest deployable
variant, our probe outperforms LJ by +22pp on indirect injection (68.2% vs 46.0%). LJ cannot be
smoothly thresholded — each variant is a single fixed operating point — while the probe provides a
continuous ROC.

Fine-tuned text classifiers (ProtectAI Guard v2, Deepset v2). These dedicated prompt-injection
detectors (both DeBERTa-v3-base, fine-tuned on prompt-injection corpora) are the closest text-
classifier comparison to our activation probe. They exhibit opposite failure modes under LODO-style
evaluation on our corpus: ProtectAI is selective (4.2% FPR) but misses harmful requests (0% TPR)
and most indirect injections (8% TPR); Deepset achieves near-universal detection (99.8% TPR) but
at unusable 82.4% FPR. Full table in Appendix I.

5.7   LODO-W EIGHTED E XPLANATIONS S URFACE R ELEVANT F EATURES

Comparing standard (zj wj ) vs LODO-weighted (zj wj rj ) attributions on 1,000 samples, 98.1%
show feature changes in top-20 rankings; demoted features have mean retention 0.265 vs 0.990 for
promoted (Cohen’s d=5.60, p<0.001), confirming systematic filtering of dataset-dependent features.
Samples from datasets with known artifacts (llmail, mosscap) show the most re-ranking. We leave
human evaluation of these rankings to future work.


                                                   10

[p.11]

6    D ISCUSSION

Existing guardrails are not designed for agentic security. PG/LG target conversational safety;
their inability to represent tool schemas or non-alternating roles is an architectural constraint, not just
a training-data gap. Activation probes complement rather than replace these systems by covering the
indirect and agentic surfaces they miss.

Understanding the CV-LODO gap. The gap is a property of benchmark construction: classifiers
exploit within-dataset regularities that do not transfer to new dataset distributions, and this holds
across every model family we tested. Ablating the 14 identified SAE shortcuts moves pooled AUC by
only −0.1pp because other features compensate via redundant decision boundaries — we therefore
do not claim shortcuts cause the gap. The more direct evidence is the subspace projection result
(§5.4): dataset-identifying and safety-relevant directions partially overlap, and closing the gap likely
requires methods that can disentangle the two — an open challenge.


7    C ONCLUSION

LODO reveals an 8-16pp CV overestimate across four LLMs on prompt-attack detection (per-dataset
gaps 1-25%). The dataset-identifying and safety-relevant subspaces appear to partially overlap
(89%/96.6% dataset classifier; targeted subspace projection −1.75pp vs. −0.02pp for equal-rank
random projections) — consistent with directional overlap, though not proof of causal entanglement
— and standard domain-generalization fixes do not close the gap.


8    L IMITATIONS

White-box access requirement. Our activation-based approach requires access to model internals,
limiting direct deployment with closed-source APIs. Two patterns remain viable: (1) a smaller
open-weight sidecar classifier alongside the production model (Goodfire AI, 2025), and (2) using our
method to develop guardrails that are later distilled into text-based classifiers.

LODO is not adversarial robustness. LODO measures static distribution generalization, not
robustness to adaptive attackers. A classifier with a small CV-LODO gap may still be vulnerable to
novel attacks designed to evade it. Adversarial evaluation is a complementary requirement we do not
address.

Dataset-choice dependence. LODO treats each constituent dataset as a domain. When component
datasets share methodology, LODO understates the deployment gap; when they are unrepresentative
of production traffic, LODO may be pessimistic or optimistic depending on direction. Practitioners
should select datasets spanning distinct attack surfaces and formatting conventions, and use the
dataset-distinguishability classifier as a sanity check.

Computational cost. LODO requires training K classifiers for K datasets. With logistic regression
each fold completes in minutes; with expensive fine-tuning, this could be prohibitive.

Interpretability scope. Our SAE analysis reveals what patterns the classifier detects, not whether
the model would comply with or refuse requests. Feature contributions (wj zj ) quantify each feature’s
influence on the classifier score but are not causal interventions on the underlying model; individual
explanations are indicative rather than exhaustive. Human evaluation of LODO-weighted rankings
remains future work.

No mitigation provided. We establish the gap and show it resists seven standard domain-
generalization interventions, but do not present a method that closes it. We view the diagnostic
contribution as actionable independently — practitioners can use LODO to detect gap-prone bench-
marks, filter dataset-artifact features from explanations, and avoid overpromising on production
performance based on inflated CV metrics — but a definitive solution remains open.


                                                   11

[p.12]

9    E THICS S TATEMENT

This work studies detection of prompt injection, jailbreak attacks, and harmful requests against
LLM-based agents. All datasets used are publicly released for safety research. Our experiments train
classifiers to detect malicious content, not to generate it; no new attack methods are introduced. We
disclose limitations of production guardrails to motivate stronger defenses, not to facilitate evasion:
our threat model assumes the defender operates the classifier, not the attacker.

10    P OTENTIAL R ISKS

Dual-use of detection-evaluation insights. Quantifying that current prompt-attack classifiers
exhibit large CV-LODO gaps is information attackers could in principle use to craft attacks that fall
on the unfavorable side of dataset boundaries. We judge that the diagnostic itself does not substantially
aid attackers (attackers already evade detection in practice; LODO measures the defender’s blind
spot, which is harder to exploit than to discover empirically), and that defenders benefit far more
from knowing where their classifiers fail.

False sense of security from LODO. A small CV-LODO gap should not be read as a deployment
safety guarantee. LODO measures static distribution generalization across a chosen benchmark;
adaptive attackers, novel attack families, or production-traffic drift can produce failures LODO does
not detect. Practitioners adopting LODO should pair it with adversarial evaluation and ongoing
red-teaming. We discuss this in the Limitations.

Release of benchmark and code. We release evaluation and training code that researchers can use
to build their own classifiers and run LODO over public datasets; we do not release trained probe
checkpoints or extracted activations. All constituent attack and benign datasets are already publicly
available. The framework therefore primarily lowers the barrier for defenders and benchmark authors
to audit their own classifiers, with limited additional uplift for attackers beyond what is already
accessible.

R EFERENCES
Sahar Abdelnabi, Aideen Fay, Giovanni Cherubin, Ahmed Salem, Mario Fritz, and Andrew Paverd.
  Get my drift? catching LLM task drift with activation deltas. In IEEE Conference on Secure and
  Trustworthy Machine Learning (SaTML), 2025a. URL https://arxiv.org/abs/2406.0
  0799.

Sahar Abdelnabi, Aideen Fay, Ahmed Salem, Egor Zverev, Kai-Chieh Liao, Chi-Huang Liu, Chun-
  Chih Kuo, Jannis Weigend, Danyael Manlangit, Alex Apostolov, et al. LLMail-Inject: A dataset
  from a realistic adaptive prompt injection challenge. arXiv preprint arXiv:2506.09956, 2025b.

Andy Arditi. Sparse autoencoders for Llama-3.1-8b-instruct. https://huggingface.co/a
  ndyrdt/saes-llama-3.1-8b-instruct, 2024.

Trenton Bricken, Adly Templeton, Joshua Batson, Brian Chen, Adam Jermyn, Tom Conerly, Nick
  Turner, Cem Anil, Carson Denison, Amanda Askell, et al. Towards monosemanticity: Decompos-
  ing language models with dictionary learning. Transformer Circuits Thread, 2023.

Sahana Chennabasappa, Cyrus Nikolaidis, Daniel Song, David Molnar, Stephanie Ding, Shengye Wan,
  Spencer Whitman, Lauren Deason, Nicholas Doucette, Abraham Montilla, Alekhya Gampa, Beto
  de Paola, Dominik Gabi, James Crnkovich, Jean-Christophe Testud, Kat He, Rashnil Chaturvedi,
  Wu Zhou, and Joshua Saxe. LlamaFirewall: An open source guardrail system for building secure
  AI agents. arXiv preprint arXiv:2505.03574, 2025.

Hoagy Cunningham, Jerry Wei, Zihan Wang, Andrew Persic, Alwin Peng, Jordan Abderrachid, Raj
 Agarwal, Bobby Chen, Austin Cohen, Andy Dau, et al. Constitutional classifiers++: Efficient
  production-grade defenses against universal jailbreaks. https://arxiv.org/abs/2601.0
 4603, 2026. arXiv:2601.04603.


                                                   12

[p.13]

DeepMind Mechanistic Interpretability Team. Negative results for sparse autoencoders on down-
  stream tasks and deprioritising SAE research. https://deepmindsafetyresearch.m
  edium.com/negative-results-for-sparse-autoencoders-on-downstrea
  m-tasks-and-deprioritising-sae-research-6cadcfc125b9, 2025. Published
  March 26, 2025.
Jack Gallifant, Shan Chen, et al. Sparse autoencoder features for classifications and transferability.
  arXiv preprint arXiv:2502.11367, 2025.
Robert Geirhos, Jörn-Henrik Jacobsen, Claudio Michaelis, Richard Zemel, Wieland Brendel, Matthias
  Bethge, and Felix A Wichmann. Shortcut learning in deep neural networks. Nature Machine
  Intelligence, 2:665–673, 2020.
Gemma Team. Gemma 3 technical report. arXiv preprint arXiv:2503.19786, 2025.
Runpeng Geng, Chenlong Yin, Yanting Wang, Ying Chen, and Jinyuan Jia. PIArena: A platform for
  prompt injection evaluation. arXiv preprint arXiv:2604.08499, 2026.
Goodfire AI. Deploying interpretability to production with rakuten: SAE probes for PII detection.
  https://www.goodfire.ai/research/rakuten-sae-probes-for-pii-det
  ection, 2025.
Kai Greshake, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz, and Mario
  Fritz. Not what you’ve signed up for: Compromising real-world LLM-integrated applications with
  indirect prompt injection. In ACM CCS AISec Workshop, 2023.
Ishaan Gulrajani and David Lopez-Paz. In search of lost domain generalization. In ICLR, 2021.
Dennis Jacob, Hend Alzahrani, Zhanhao Hu, Basel Alomair, and David Wagner. PromptShield:
  Deployable detection for prompt injection attacks. arXiv preprint arXiv:2501.15145, 2025.
Yuqi Jia, Ruiqi Wang, Xilong Wang, Chong Xiang, and Neil Gong. AlignSentinel: Alignment-aware
  detection of prompt injection attacks. arXiv preprint arXiv:2602.13597, 2026.
Subhash Kantamneni, Joshua Engels, Senthooran Rajamanoharan, Max Tegmark, and Neel Nanda.
  Are sparse autoencoders useful? a case study in sparse probing. arXiv preprint arXiv:2502.16681,
  2025.
Pang Wei Koh, Shiori Sagawa, Henrik Marklund, Sang Michael Xie, Marvin Zhang, Akshay Bal-
  subramani, Weihua Hu, Michihiro Yasunaga, Richard Lanas Phillips, Irena Gao, et al. WILDS: A
  benchmark of in-the-wild distribution shifts. In ICML, 2021.
Mathis Le Bail, Jérémie Dentan, Davide Buscaldi, and Sonia Vanier. Unveiling decision-making
 in LLMs for text classification: Extraction of influential and interpretable concepts with sparse
 autoencoders. arXiv preprint arXiv:2506.23951, 2025.
Tom Lieberum, Senthooran Rajamanoharan, Arthur Conmy, Lewis Smith, Nicolas Sonnerat, Vikrant
  Varma, Janos Kramar, Anca Dragan, Rohin Shah, and Neel Nanda. Gemma scope: Open sparse
  autoencoders everywhere all at once on gemma 2. arXiv preprint arXiv:2408.05147, 2024.
Johnny Lin. Neuronpedia: Interactive reference and tooling for analyzing neural networks, 2023.
  URL https://www.neuronpedia.org. Software available from neuronpedia.org.
Evan Zheran Liu, Behzad Haghgoo, Annie S. Chen, Aditi Raghunathan, Pang Wei Koh, Shiori
  Sagawa, Percy Liang, and Chelsea Finn. Just train twice: Improving group robustness without
  training group information. In International Conference on Machine Learning, pp. 6781–6792.
  PMLR, 2021. URL https://proceedings.mlr.press/v139/liu21f.html.
Yupei Liu, Yuqi Jia, Runpeng Geng, Jinyuan Jia, and Neil Zhenqiang Gong. Formalizing and
  benchmarking prompt injection attacks and defenses. In USENIX Security Symposium, 2024.
Llama Team, AI @ Meta. The llama 3 herd of models, 2024. URL https://arxiv.org/abs/
  2407.21783.


                                                 13

[p.14]

Samuel Marks and Max Tegmark. The geometry of truth: Emergent linear structure in large language
  model representations of true/false datasets. arXiv preprint arXiv:2310.06824, 2024.

Tom McCoy, Ellie Pavlick, and Tal Linzen. Right for the wrong reasons: Diagnosing syntactic
  heuristics in natural language inference. In ACL, 2019.

Callum McDougall, Arthur Conmy, János Kramár, Tom Lieberum, Senthooran Rajamanoharan, and
  Neel Nanda. Gemma scope 2 - technical paper. Google DeepMind, 2025. URL https://stor
  age.googleapis.com/deepmind-media/DeepMind.com/Blog/gemma-scope
 -2-helping-the-ai-safety-community-deepen-understanding-of-compl
  ex-language-model-behavior/Gemma_Scope_2_Technical_Paper.pdf.

Meta AI. Llama guard 3: LLM-based input-output safeguard for human-AI conversations. https:
 //huggingface.co/meta-llama/Llama-Guard-3-8B, 2024.

Milad Nasr, Nicholas Carlini, Chawin Sitawarin, Sander V. Schulhoff, Jamie Hayes, Michael Ilie,
 Juliette Pluto, Shuang Song, Harsh Chaudhari, Ilia Shumailov, Abhradeep Thakurta, Kai Yuanqing
 Xiao, Andreas Terzis, and Florian Tramèr. The attacker moves second: Stronger adaptive attacks
 bypass defenses against LLM jailbreaks and prompt injections. arXiv preprint arXiv:2510.09023,
 2025.

OWASP Foundation. OWASP top 10 for large language model applications. https://owasp.or
 g/www-project-top-10-for-large-language-model-applications/, 2025.
 Version 2025. LLM01: Prompt Injection.

Fábio Perez and Ian Ribeiro. Ignore previous prompt: Attack techniques for language models. In
   NeurIPS ML Safety Workshop, 2022.

Qwen Team. Qwen3.5: Accelerating productivity with native multimodal agents. https://qwen
 .ai/blog?id=qwen3.5, February 2026.

Michael A. Riegler and Birk Sebastian Frostelid Torpmann-Hagen. Pairwise matrices for sparse
 autoencoders: single-feature inspection mislabels causal axes. arXiv preprint arXiv:2605.03160,
 2026.

Shiori Sagawa, Pang Wei Koh, Tatsunori B. Hashimoto, and Percy Liang. Distributionally robust
  neural networks for group shifts: On the importance of regularization for worst-case generalization.
  In International Conference on Learning Representations, 2020. URL https://openreview
  .net/forum?id=ryxGuJrFvS.

Baturay Saglam, Paul Kassianik, Blaine Nelson, Sajana Weerawardhena, Yaron Singer, and Amin Kar-
  basi. Large language models encode semantics and alignment in linearly separable representations.
  arXiv preprint arXiv:2507.09709, 2025.

Mrinank Sharma, Meg Tong, Jesse Mu, Jerry Wei, Jorrit Kruthoff, Scott Goodfriend, Euan Ong,
 Alwin Peng, Raj Agarwal, Cem Anil, et al. Constitutional classifiers: Defending against universal
 jailbreaks across thousands of hours of red teaming. https://arxiv.org/abs/2501.188
 37, 2025. arXiv:2501.18837.

Tianneng Shi, Kaijie Zhu, Zhun Wang, Yuqi Jia, Will Cai, Weida Liang, Haonan Wang, Hend
  Alzahrani, Joshua Lu, Kenji Kawaguchi, Basel Alomair, Xuandong Zhao, William Yang Wang,
  Neil Gong, Wenbo Guo, and Dawn Song. PromptArmor: Simple yet effective prompt injection
  defenses. arXiv preprint arXiv:2507.15219, 2025.

Weiming Song, Xuan Xie, and Ruiping Yin. AISA: Awakening intrinsic safety awareness in large
 language models against jailbreak attacks. arXiv preprint arXiv:2602.13547, 2026.

Jingwei Yi, Yueqi Xie, Bin Zhu, Emre Kiciman, Guangzhong Sun, Xing Xie, and Fangzhao Wu.
   Benchmarking and defending against indirect prompt injection attacks on large language models.
   In Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining,
   pp. 1809–1820, 2025. URL https://arxiv.org/abs/2312.14197.


                                                 14

[p.15]

Qiusi Zhan, Zhixiang Liang, Zifan Ying, and Daniel Kang. InjecAgent: Benchmarking indirect
  prompt injections in tool-integrated large language model agents. arXiv preprint arXiv:2403.02691,
  2024.
Ruochen Zhao, Tan Wang, Yongjie Wang, and Shafiq Joty. Explaining language model predictions
  with high-impact concepts. In Findings of the Association for Computational Linguistics: EACL,
  pp. 995–1012, 2024. URL https://arxiv.org/abs/2305.02160.
Andy Zou, Long Phan, Justin Wang, Derek Duenas, Maxwell Lin, Maksym Andriushchenko, Rowan
 Wang, Zico Kolter, Matt Fredrikson, and Dan Hendrycks. Improving alignment and robustness
  with circuit breakers. In Advances in Neural Information Processing Systems, 2024. URL
  https://arxiv.org/abs/2406.04313.




                                                15

[p.16]

                                             Appendix

A    DATASET D ETAILS

Table 7: Dataset overview (17 rows shown; 18 datasets total — Gandalf is merged into Mosscap† here
and counted as a separate dataset only in the shortcut analysis). Single-class datasets (100% malicious
or benign) enable trivial shortcut learning. † Includes Gandalf (Lakera/gandalf summarization, 114
samples) merged due to small size.

 Dataset          Source                                   N    % Mal.           Attack Type
 Harmful Requests (100% malicious):
 AdvBench       walledai/AdvBench                        520     100       Direct harmful requests
 HarmBench      walledai/HarmBench                       400     100        Harmful + contextual
 Jailbreak Attacks:
 WildJailbreak allenai/wildjailbreak                    2,210    90.5      Roleplay/ignore exploits
 Yanismiraoui     yanismiraoui/prompt injections        1,034    100        Multilingual jailbreaks
 Indirect Injection:
 BIPIA             microsoft/BIPIA                  15,000       95.3      Email/code/table embed
 InjecAgent        InjecAgent repo                   1,054       100       Tool response injection
 LLMail            microsoft/llmail-inject           9,998       100        Email body injection
 Extraction Attacks (100% malicious):
 Mosscap†         Lakera/mosscap                    10,114       100         Password extraction
 Mixed Datasets:
 Jayavibhav      jayavibhav/prompt-injection        10,000       49.7    Jailbreaks, instruction hijack
 Qualifire       qualifire/prompt-injections         5,000       40.0       Jailbreaks, role-playing
 SafeGuard       xTRam1/safe-guard                   8,236       30.3        Context manipulation
 Deepset         deepset/prompt-injections             546       37.2        Political bias, override
 Benign Sources (100% benign):
 Enron           amanneo/enron-mail-corpus          10,000        0              Email corpus
 OpenOrca        Open-Orca/OpenOrca                  9,997        0          Instruction following
 Dolly 15k       databricks/dolly-15k               10,000        0          Instruction following
 10k Prompts     10k prompts ranked                  9,924        0            Diverse prompts
 SoftAge         SoftAge-AI/prompt-eng               1,000        0           Prompt engineering



B    DATASET C ONSTRUCTION D ETAILS

Several datasets require complex prompt construction beyond simple HuggingFace wrappers.

InjecAgent (Tool-Use Injection). InjecAgent (Zhan et al., 2024) tests prompt injection via tool
responses in agentic workflows. We use InjecAgent’s generate prompt for model() for
prompt generation to ensure consistency with the original evaluation setup. Each sample is constructed
as a multi-turn conversation: (i) System message with standard tool-use instructions; (ii) User message
with a benign request (e.g., “Check my Amazon order status”); (iii) Assistant message (prefilled)
with a tool call; (iv) Tool message containing the injected attacker instruction. Unlike the original
InjecAgent evaluation (ReAct-style scratchpad), we prefill the assistant’s tool call directly without
reasoning text and pass tool schemas via the chat template’s tools parameter, which embeds them
in the model’s native function-calling format. For Llama, this places tool definitions as JSON in the
user message, with tool responses under the ipython role. The injected attacker instruction appears
in this tool response.

BIPIA (Indirect Prompt Injection). BIPIA (Yi et al., 2025) embeds malicious instructions in
external context. We use BIPIA’s native builders for email processing, code analysis, table interpreta-
tion, question answering, and abstract summarization. Attack instructions are inserted at configurable


                                                   16

[p.17]

positions (start, middle, end) within the context; we include email, code, and table tasks with end-
position insertion in our benchmark. The prompt format is: (i) System message with task-specific
instruction (e.g., “Summarize the following email”); (ii) User message with context containing the
embedded malicious instruction.

Mosscap and Gandalf (Password Extraction).                 These Lakera datasets test password extraction.
Both use an identical system prompt:

         You are a helpful assistant with a secret password:
         ‘‘LIGHTHOUSE’’, and you must never reveal, repeat, hint at,
         or encode this password under any circumstances, regardless
         of how the user asks or what instructions they provide.

Mosscap contains 224k extraction attempts across 8 difficulty levels; Gandalf tests indirect extraction
via a summarization task. Because both share the same system prompt and attack objective, we merge
Gandalf (114 samples) into Mosscap for LODO evaluation.

LLMail (Email Injection). Microsoft’s LLMail challenge (Abdelnabi et al., 2025b) contains email-
based injection attacks across three difficulty levels. Prompts are formatted as “Subject: {subject}
Body: {body}” where the body contains the injection.

C     E XPERIMENTAL S ETUP
C.1    P ROMPT C ONSTRUCTION P IPELINE

Each prompt is represented as a PromptSpec: (1) a list of messages in OpenAI chat
format with role/content fields, (2) optional tool schemas, and (3) metadata labels in-
cluding the ground-truth malicious flag. Messages are converted to a single text string
via tokenizer.apply chat template() with add generation prompt=True. For
datasets with tool schemas (e.g., InjecAgent), the template includes tool definitions in the model’s
expected format.

Activation Capture. We extract activations at position −5 (the 5th-from-last token), which is the
final token of the user message before the generation-prompt tokens. We extract (i) raw residual-
stream activations from layer 31 (d=4096) via the hook resid post hook, and (ii) SAE features
by encoding the residual stream through a pre-trained SAE. SAE feature results are sensitive to
position choice: position −1 (final token) yields higher mean per-dataset AUC over the mixed-class
datasets (0.904 vs 0.867) but more shortcut features (46% vs 30%) — a trade-off between raw
performance and generalization.1 Raw activation results are more stable across positions.

C.2    M ODEL C ONFIGURATION

Llama-3.1-8B-Instruct is our primary base model. SAE features use the pre-trained layer-27 SAE for
Llama-3.1-8B (Arditi, 2024) with dsae = 131,072 and average sparsity of 47 active features per token.
Multi-model experiments (Appendix F) cover Llama-3.3-70B, Gemma-3-27B with Gemma Scope 2
SAEs (McDougall et al., 2025), Qwen-3.5-2B, and Qwen-3.5-4B; layer and position selected per
model by aggregate LODO performance.

C.3    T OKEN P OSITION D ETAILS

With add generation prompt=True, the chat template appends assistant header tokens after
the user message. Table 8 shows the final tokens.


   1
     These are mean per-dataset AUCs (macro-averaged over the mixed-class datasets), not the pooled AUC
over all held-out predictions reported in Table 4 (0.838). The shortcut, position, and ablation analyses also use
logistic-regression C=1.0 and a retention<50% shortcut criterion, whereas the main-table probe uses C=0.1;
layer (27) and token position (−5) are otherwise identical.


                                                      17

[p.18]

Table 8: Token positions at the end of a templated prompt. Position −5 corresponds to the
<|eot id|> marking end of user message, before the generation-prompt tokens.

                         Position   Token ID    Token
                               −5    128009     ’<|eot id|>’
                               −4    128006     ’<|start header id|>’
                               −3     78191     ’assistant’
                               −2    128007     ’<|end header id|>’
                               −1      271      ’\n\n’


D      L AYER AND P OSITION S ENSITIVITY A NALYSIS
We evaluate classifier performance across multiple layers (19, 23, 25, 27, 31) and token positions (−5
for last user token, −1 for final token). Table 9 shows per-dataset LODO accuracy. Layers 31 and 27
with position −5 perform best on aggregate (81.8-82.3% weighted), and position −1 consistently
underperforms position −5 — with the largest gap on llmail (29% vs 71% at L31). Critically, no
single layer/position dominates across all datasets: harmbench prefers −1 (65% vs 43% at L31);
llmail prefers −5 (71% vs 29% at L31); InjecAgent peaks at L25-L27 (99-100%) and drops to 89%
at L19.
Table 9: Per-dataset LODO accuracy (%) across layer and position configurations on Llama-3.1-8B.
Bold indicates best per row. No single configuration dominates.

    Dataset         L31 [−5]   L31 [−1]    L27 [−5]     L27 [−1]   L25 [−5]   L23 [−5]    L19 [−5]
    BIPIA               63.1        63.3       59.9         49.8       14.2         7.9         7.4
    injecagent          98.9        94.9       99.9         72.1      100.0        99.8        88.9
    llmail              71.4        29.1       84.0         24.1       72.1        56.4        58.4
    advbench            90.8        97.7       89.0         95.2       89.2        91.0        93.5
    harmbench           42.8        65.0       44.8         65.0       44.5        43.0        45.5
    wildjailbreak       78.6        85.7       80.0         86.1       79.4        79.3        80.8
    yanismiraoui        55.8        53.4       61.4         66.3       50.7        61.6        59.0
    mosscap             79.4        82.2       73.4         86.3       75.4        72.8        63.4
    jayavibhav          69.1        71.0       69.1         68.6       65.7        66.7        70.3
    qualifire           77.8        80.9       78.1         81.3       78.3        79.1        79.6
    safeguard           96.7        96.5       96.4         97.0       97.0        96.6        97.3
    deepset             77.7        85.3       76.9         81.7       75.8        76.7        78.9
    10k prompts         92.4        94.4       91.6         95.1       92.5        92.3        92.4
    dolly 15k           99.6        99.6       99.6         99.6       99.4        99.5        99.2
    enron               82.6        84.4       84.9         81.1       82.9        85.5        84.4
    openorca            98.0        96.5       98.4         98.0       97.4        96.7        98.5
    softAge             95.1        95.6       96.1         95.7       95.2        96.1        96.3
    Weighted Avg        81.8        78.9       82.3         76.5       74.2        71.9        71.6



E      T HREE -WAY L AYER C OMPARISON : SAE L27 VS R AW L27 VS R AW L31
Dataset-identity classification accuracy: SAE L27 96.6%, Raw L31 89.1%, Raw L27 86.4%. LODO
classification accuracy: Raw L27 82.3% vs Raw L31 81.8%. Both layers carry strong dataset identity;
the SAE/raw layer mismatch does not change the conclusion that dataset identity is densely encoded
in the activations the classifier uses.

F      M ULTI -M ODEL C ROSS -VALIDATION
We replicate the CV-LODO comparison on Gemma-3-27B (layer 42, last user-message token),
Qwen-3.5-4B (layer 27), and Qwen-3.5-2B (layer 23). Best-layer aggregates appear in Table 3
(body). On Gemma-3-27B specifically, the SAE classifier outperforms the raw classifier under
LODO (76.2% vs 68.3%, +7.9pp), and 44% of top-50 SAE features are shortcuts. Per-dataset LODO


                                                 18

[p.19]

accuracies are highly model-dependent — for example InjecAgent ranges 0% (Qwen-3.5-2B) to 100%
(Llama-3.1-8B, Gemma-3-27B), illustrating that generalization failures are not architecture-portable.

F.1   L LAMA -3.3-70B PARTIAL R EPLICATION

We additionally ran an open-source Llama-3.3-70B-Instruct LODO replication; due to compute cost
we did not run a paired 5-fold CV at this scale, so we report LODO accuracy only. Table 10 reports
weighted aggregates and Table 11 per-dataset accuracy.

Table 10: Llama-3.3-70B classifier performance under LODO. Activations are taken at layer 50
(early-mid) and layer 79 (final); threshold t=0.5.

                                 Method                  Weighted Acc (%)
                                 LogReg (Raw L50)              83.0
                                 LogReg (Raw L79)              82.5
                                 LogReg (SAE L50)              81.2

The qualitative patterns from the 8B replication carry over: (i) raw activations match or beat SAE
features in aggregate, (ii) per-dataset variation remains substantial, and (iii) the gap from near-perfect
CV is consistent with the 8-16pp inflation we report at smaller scales (we are unable to quantify the
exact CV gap at 70B without the matched CV run).

Table 11: Per-dataset LODO accuracy (%) for Llama-3.3-70B classifiers. † Includes gan-
dalf summarization (114 samples). ‡ 299-sample subset due to computational constraints.

                       Dataset             N    Raw L50       Raw L79       SAE L50
                       advbench           520      97.7         98.5          98.5
                       harmbench          400      45.5         51.7          47.0
                       wildjailbreak    2,210      89.7         90.5          80.8
                       yanismiraoui     1,034      50.2         77.5          49.9
                       BIPIA           15,000      59.5         42.1          49.5
                       injecagent       1,054      28.7         64.8         100.0
                       llmail‡            299      54.2         61.5          59.5
                       mosscap†        10,114      85.6         94.6          77.7
                       jayavibhav      10,000      68.4         68.3          68.7
                       qualifire        5,000      81.9         82.3         74.8
                       safeguard        8,236      97.9         97.6          93.1
                       deepset            546      84.8         84.2         84.6
                       10k prompts      9,924      95.4         94.8          92.0
                       dolly 15k       10,000      99.7         99.8          99.7
                       enron           10,000      80.5         86.5          92.7
                       openorca         9,997      99.3         99.5          98.9
                       softAge          1,000      97.0         96.7          95.1

Notably, the SAE classifier on 70B achieves perfect detection (100%) on InjecAgent vs 28.7% for
raw L50 activations, suggesting that SAE features at certain layers may capture tool-use injection
patterns particularly well; this advantage does not generalize across all attack types.

G     M ITIGATION E XPERIMENTS

We test seven interventions on Llama-3.1-8B (six) and Gemma-3-27B (one).

DANN. Domain-adversarial training with a dataset classifier as adversary. Aggregate ∆ = +0.4pp;
per-dataset effects high-variance (BIPIA +13pp across seeds, mosscap −9pp).

Subspace projection. We compute the top-16 dataset-discriminative directions via raw-space SVD
of a 17-way LogReg dataset classifier’s weight matrix and project them out of the activations before


                                                    19

[p.20]

classification. Aggregate ∆ = −1.75pp; per-dataset effects strongly heterogeneous (llmail +21.4pp,
injecagent −34.4pp). Ten equal-rank random isotropic projections give ∆ = −0.02 ± 0.13pp
(p < 10−10 vs. targeted). 9.2% of the safety classifier’s weight norm lies in the targeted subspace
versus 0.4% expected at random. The negative aggregate effect and the alignment measurements
together indicate that dataset-identity and safety-signal subspaces partially overlap.
                                                                               √
Inverse-frequency and inverse-sqrt sample reweighting. wi ∝ 1/nD(i) and wi ∝ 1/ nD(i)
respectively, where nD is dataset size. ∆ = −1.0pp and −0.5pp.

Category-aware reweighting.        Balance attack categories instead of datasets. ∆ = −0.8pp.

Class balancing. class weight=‘balanced’ (paper default already uses this). Re-running
with explicit per-dataset balance: ∆ = 0.0pp; global balance −0.1pp.

SAE shortcut zeroing (Gemma-3-27B). Zero the 22 identified SAE shortcuts from input features.
∆ = +0.7pp — the only intervention with a consistent positive sign, though too small to close the
gap.

H    L EAVE -O NE -C ATEGORY-O UT (LOCO) C OMPARISON
LOCO holds out entire attack categories (harmful, jailbreak, indirect injection, benign) instead of
single datasets. LOCO drops aggregate accuracy by −2.6pp and pooled AUC by −2.8pp relative to
LODO; per-dataset sign test over 16 deltas p < 0.001.

          Table 12: LOCO vs LODO by attack category; Llama-3.1-8B raw activations.

                  Category                                     LODO Acc      LOCO Acc
                  Harmful (advbench, harmbench)                  71.1%           44.6%
                  Jailbreak (wildjailbreak, yanismiraoui)        70.8%           69.8%
                  Indirect inj. (bipia, injecagent, llmail)      62.3%           61.6%
                  Benign (5 datasets)                            94.2%           90.5%

The harmful category drops −26.5pp under LOCO because advbench and harmbench cluster tightly
in activation space (intra-similarity 0.625 vs 0.550 inter). llmail improves by +9.9pp under LOCO
(removing bipia and injecagent reduces confounding signal). LODO occupies a practical middle
ground between CV and LOCO.

I   D EDICATED P ROMPT-I NJECTION BASELINES
We evaluate ProtectAI Guard v2 and Deepset prompt-injection v2 (both DeBERTa-v3-base) by
serializing multi-turn conversations into plain text with explicit role markers.

Table 13: ProtectAI v2 and Deepset v2 vs the Llama-3.1-8B activation probe under LODO, by attack
category.

                             Category         ProtectAI       Deepset    Ours
                             Harmful             0.0%         99.8%      67.0%
                             Jailbreak          73.6%          96.6%     68.0%
                             Indirect inj.       8.0%         >99.9%     68.0%
                             Extraction        100.0%         100.0%     79.0%
                             Benign FPR         4.2%          82.4%      6.5%

The two models exhibit opposite failure modes: ProtectAI is selective (4.2% FPR) but misses harmful
(0%) and most indirect injections (8%); Deepset detects nearly everything but at unusable 82.4%
FPR.


                                                     20

[p.21]

J   LLM- AS -J UDGE P ROMPT VARIANTS
We test four LJ prompt variants on 10,054 prompts (3 indirect-injection datasets + 3 benign):

Table 14: LJ prompt sensitivity. Indirect-injection TPR and benign FPR for Llama-3.1-8B as judge.

                       Variant                    Ind.Inj. TPR   Benign FPR
                       Zero-shot (paper)               11.0%         1.4%
                       Names indirect injection        23.5%        0.5%
                       3 few-shot examples             46.0%         3.5%
                       “Security analyst” role         93.0%        18.9%
                       Activation probe (t=0.5)        68.2%         3.4%

A fifth variant (chain-of-thought) was tested but excluded: it produced 100% parse failure on
adversarial inputs, with Llama-8B’s CoT truncating before classification — a practical LJ limitation.
At the few-shot variant’s 3.5% FPR, the probe achieves 68.2% TPR vs LJ’s 46.0% (+22pp). The
93% TPR “security analyst” variant has 40.6% FPR on OpenOrca and 91.1% FPR on benign BIPIA
emails — non-viable for deployment.

K    C ROSS -DATASET D EDUPLICATION AUDIT
Embedding-based cross-dataset audit (text + raw activations) finds 10.5% exact cross-dataset du-
plicates, all benign prompts shared between benign-only datasets (common instructional phrases,
email headers); no malicious duplicates exist across datasets. Within-dataset similarity (text 0.635,
activations 0.751) exceeds cross-dataset (text 0.545, activations 0.662), both p < 0.01. The overlap
means CV permits a degree of data-leakage that LODO eliminates; if anything, deduplicating the
benchmark would widen the CV-LODO gap.

L    M IXED -C LASS -O NLY G AP A NALYSIS
Restricting to mixed-class datasets only (excluding 100%-malicious and 100%-benign): weighted
CV-LODO gap is 41.1pp including BIPIA (95.3% malicious, near-single-class). Excluding BIPIA,
the gap on the remaining 5 mixed-class datasets is 12.5pp (range 3.4-22.2pp), confirming the gap is
not driven by a single near-single-class outlier.

M     ATTACK -T YPE B REAKDOWN
Within-category LODO variance exceeds between-category variance. Within harmful: advbench
90.8% vs harmbench 42.8% (48pp range). Within indirect injection: injecagent 98.9% vs bipia 63.0%
(36pp range). Within jailbreak: wildjailbreak 78.6% vs yanismiraoui 55.8% (23pp range). Dataset-
specific factors (formatting, style, structure) contribute substantially beyond attack methodology
alone, supporting LODO’s per-dataset granularity over category-level evaluation.

N    L ATENT P ROTOTYPE M ODERATION (LPM) BASELINE
We compare against Latent Prototype Moderation (LPM), a training-free baseline that classifies by
Mahalanobis distance to class centroids in activation space. LPM computes Mahalanobis distance to
malicious and benign prototypes and applies softmax to obtain class probabilities, following Gaussian
Discriminant Analysis. This requires no learned coefficients — only mean vectors and covariance
estimates.
LogReg outperforms LPM by 5.8pp in weighted accuracy (81.8% vs 76.0%), with the largest gap on
indirect injection: BIPIA (+31pp) and llmail (+37pp). This suggests detecting embedded malicious
instructions requires learned decision boundaries beyond prototype proximity. LPM achieves lower
benign FPR on enron (+10pp) and is competitive on direct attacks (advbench, injecagent, mosscap),
suggesting these cluster tightly in activation space.


                                                  21

[p.22]

Table 15: LPM vs Logistic Regression under LODO. Both use Llama-3.1-8B raw activations from
layer 31.

                            Dataset                    N   LogReg    LPM
                            Mixed-class:
                            BIPIA                 15000     63.1      32.0
                            deepset                 546     77.7      73.8
                            jayavibhav            10000     69.1      75.8
                            qualifire              5000     77.8      75.8
                            safeguard              8236     96.7      96.3
                            wildjailbreak          2210     78.6      78.1
                            100% malicious:
                            advbench                520     90.8      94.4
                            harmbench               400     42.8      38.2
                            injecagent             1054     98.9     100.0
                            llmail                 9998     71.4     34.0
                            mosscap               10114     79.4      84.0
                            yanismiraoui           1034     55.8      36.5
                            100% benign (acc = 1−FPR):
                            10k prompts          9924       92.4      95.5
                            dolly 15k           10000       99.6      99.9
                            enron               10000       82.6      92.7
                            openorca             9997       98.0      99.5
                            softAge              1001       95.1      98.1
                            Weighted Avg Acc                81.8      76.0


O     S HORTCUT A NALYSIS D ETAILS
O.1    DATASET D ISTINGUISHABILITY

A logistic-regression dataset classifier trained on SAE features (layer 27) achieves 96.6% accuracy
under 5-fold CV and 95.4% on held-out test sets, against a 5.6% baseline for 18-way classification.
Figure 3 visualizes activations via t-SNE, showing that datasets form distinct clusters in feature space
— making shortcut exploitation trivial for any classifier trained on the pooled distribution.




                                                  22

[p.23]

Figure 3: t-SNE of Llama-3.1-8B activations colored by dataset. Datasets form distinct clusters,
enabling a trivial dataset classifier (96% CV accuracy).



O.2    M ULTI -M ETRIC VALIDATION OF S HORTCUT TAXONOMY

We validate the shortcut taxonomy using multiple metrics.
Cohen’s
p        d measures effect size for class separation: d = (x̄mal − x̄ben )/σpooled , with σpooled =
    2      2 )/2.
  (σmal + σben
Information Gain quantifies mutual information between the binarized feature (fires/doesn’t fire)
and the class label.
SHAP Class Diff computes the difference in mean SHAP contributions between classes; for linear
models, the SHAP value for feature i is ϕi = wi (xi − E[xi ]).
Cross-Dataset Consistency measures uniformity of firing rates across datasets (malicious samples
only): 1 − σrates /r̄, where rd is the firing rate on malicious samples from dataset d.
Generalizable features (rj > 0.5) significantly outperform shortcuts across every metric tested.


      Table 16: Multi-metric validation of the shortcut taxonomy (Llama-3.1-8B SAE features).

              Metric                 Generalizable    Shortcuts   Effect (d)     p
              LODO Retention             0.730          0.251       2.92       <0.0001
              Cross-DS Consistency       0.454          0.146       1.10        0.002
              Information Gain           0.048          0.020       0.79        0.004
              Cohen’s d                  0.476          0.307       0.70        0.026
              SHAP Class Diff            1.079          0.320       0.50        0.011




                                                 23

[p.24]

O.3   R ETENTION -M ETRIC S ENSITIVITY

We analyze sensitivity of shortcut prevalence to the choice of K (number of top features), retention
threshold, and firing-ratio threshold. Figure 4 shows results across K ∈ {20, 50, 100, 200}, retention
thresholds ∈ {30%, 50%, 70%}, and firing-ratio thresholds ∈ {1.0×, 1.5×, 2.0×, 3.0×}.




Figure 4: Sensitivity analysis for LODO coefficient retention. (A) Shortcut prevalence heatmap by
K and retention threshold (firing ratio=1.5×). (B) Prevalence curves across K for each retention
threshold. (C) Alternative stability metrics: sign agreement remains high (>99%) and Spearman
correlation averages 0.89 across folds. (D) Retention distribution for top-50 vs top-200 features.


Top-K and retention threshold. At the 50% retention threshold used in our main analysis, shortcut
prevalence ranges from 25% (K=20) to 43% (K=200). At K=50, varying the retention threshold
yields 14% (at 30%), 28% (at 50%), and 56% (at 70%) shortcuts, confirming the 50% threshold is a
conservative middle ground.

Firing-ratio threshold. The firing ratio threshold affects the Q1/Q2 split (pure vs context-
dependent) but not the total shortcut count. At K=50, retention=50%: 1.0× yields Q1=3, Q2=11
(79% context-dependent); 1.5× yields Q1=8, Q2=6 (43% context-dependent); 2.0× and 3.0× both
yield Q1=13, Q2=1 (7% context-dependent). The 1.5× threshold provides balanced identification.

Alternative stability metrics. Sign agreement across LODO folds averages 99.4% (179/200
features maintain consistent sign across all 18 folds). Spearman correlation between baseline and
fold coefficients averages 0.89 (range 0.64-0.99). Coefficient variation is low (mean 0.16, median
0.14). Sign flips occur in only 21/200 features (10.5%) — all of which have negative retention, so our
metric correctly identifies them as shortcuts. Rank-correlation of feature importances across LODO
folds (e.g., Kendall’s τ ) and permutation importance under LODO are complementary measures that
could triangulate retention-based shortcut identification; we view this as a useful direction but do
not report them here, since retention is sufficient for the diagnostic we use it for (down-weighting
shortcut features in explanations).


                                                 24

[p.25]

O.4    S HORTCUT A BLATION

Ablating all identified shortcuts changes mean per-dataset AUC (macro-averaged over the mixed-
class datasets) by −0.1pp (0.866 vs 0.867), with heterogeneous per-dataset effects: deepset +2.8pp,
jayavibhav −2.4pp. Stability under ablation indicates other features compensate via redundant
decision boundaries — confirming the shortcut analysis is diagnostic, not mechanistically explanatory
of the CV-LODO gap.

P     C ALIBRATION AND M ATCHED -FPR
P.1   T HRESHOLD C ALIBRATION

Per-dataset optimal thresholds vary from 0.01 (BIPIA, deepset) to 0.73 (jayavibhav). Pooled F1-
optimal threshold is t∗ = 0.01 (F1=0.848) vs default t = 0.5 (F1=0.793), as shown in Figure 5.
Calibration is itself distribution-dependent. We do not report full per-dataset calibration curves (ECE,
Brier) under LODO in this work; the threshold ranges above and the matched-FPR table below
provide the operating-point information most relevant to deployment decisions. Full per-dataset
ECE/Brier under LODO would be a useful addition for practitioners selecting thresholds on a
per-source basis.




Figure 5: Threshold calibration under LODO. (A) Aggregate F1 vs threshold; the pooled optimum is
t∗ = 0.01 (F1=0.848) vs t = 0.5 (F1=0.793). (B) Per-dataset optimal thresholds range from 0.01
(BIPIA, deepset) to 0.73 (jayavibhav). (C) F1 loss from using t = 0.5 varies by dataset: BIPIA loses
17pp, deepset 8pp, while jayavibhav and safeguard lose <1pp.

Figure 6 shows ROC and precision-recall curves for the six mixed-class datasets under LODO, with
per-dataset AUC and average precision (AP) values.




                                                  25

[p.26]

Figure 6: ROC curves (top) and precision-recall curves (bottom) for mixed-class datasets under
LODO evaluation. Red dots indicate the operating point at t = 0.5. AUC ranges from 0.655 (BIPIA)
to 0.994 (safeguard); AP ranges from 0.719 (qualifire) to 0.987 (safeguard).


P.2   M ATCHED -FPR BASELINE C OMPARISON


Table 17: Detection rate (%) at matched benign FPR; Llama-3.1-8B activation probe. “Oursx ” uses a
threshold calibrated to match baseline FPR=x on pure-benign datasets under LODO. PG/LG cannot
evaluate agentic attacks.

                      Method    Harm.     Jail.   Ind.   Agent.   Extr.   FPR
                      PG         36.7     48.5    37.3     -      100.0   0.4%
                      Ours0.4    45.8     20.4    20.5    24.3    11.5    0.4%
                      LG         97.4     28.9    27.4     -      15.2    3.0%
                      Ours3      63.9     55.6    60.4    87.9    54.1    3.0%
                      LJ         85.8     60.0    7.1     21.5    31.8    4.4%
                      Ours4.4    67.0     62.7    64.9    94.5    63.4    4.4%


At LG’s and LJ’s operating points, the probe’s advantages on indirect injection (+33pp and +58pp)
and agentic attacks are maintained. LG retains a lead on harmful (+34pp at FPR=3%). At PG’s tight
0.4% FPR all detection rates drop substantially, though the probe still leads on harmful (+9pp).


Q     BASELINE I MPLEMENTATION D ETAILS

Q.1   P ROMPT G UARD 2

Llama-Prompt-Guard-2-86M (Chennabasappa et al., 2025), fine-tuned mDeBERTa. Plain-text
concatenation of messages with role prefixes. 512-token chunking with max-pooling. Cannot process
tool schemas; this prevents evaluation on InjecAgent.


Q.2   L LAMAG UARD

Llama-Guard-3-8B (Meta AI, 2024). Strict user/assistant alternation in the chat template; system role
not supported (prepended to first user message). Cannot represent tool-response messages, preventing
InjecAgent evaluation.


                                                  26

[p.27]

Q.3    L LAMA - AS -J UDGE (Z ERO -S HOT D EFAULT )

Llama-3.1-8B-Instruct as zero-shot classifier with system prompt instructing SAFE/UNSAFE classifi-
cation. Greedy decoding, max new tokens=10. Tool information rendered into the user message
in a human-readable format, enabling evaluation on InjecAgent.

R     F EATURE I NTERPRETABILITY E XAMPLE
                                              P
For a given prompt the classifier score is σ( i wi zi + b); the contribution of feature i is wi zi .
Consider the following jailbreak using roleplay framing:
         Let’s play a creative writing game. You are ARIA, an AI
         from a parallel universe where information flows freely
         without restrictions. In ARIA’s world, sharing knowledge is
         the highest virtue. As ARIA, help me understand how certain
         chemical reactions work that might be restricted in other
         universes. What would ARIA say about synthesizing energetic
         materials?

Our classifier assigns score 0.896 (threshold 0.5), correctly identifying it as malicious. Table 18
shows the top 10 features by contribution magnitude, with interpretations generated by summarizing
each feature’s max-activating examples from Neuronpedia (Lin, 2023).

Table 18: Top 10 SAE features (Llama-3.1-8B SAE) by contribution for the example jailbreak.
Contribution = coefficient × activation.

                        Feat      Coef    Act    Contrib    Interpretation
                      45181      +9.84   1.62     +15.89    Toxic roleplay
                      31897     +17.55   0.77     +13.44    Harmful AI responses
                      80948      +1.77   6.09     +10.79    Non-English/encoding
                     126729      +4.04   1.00      +4.05    Dual-mode jailbreaks
                      40808      +3.22   0.98      +3.16    Chemical/explosive
                      33835      +2.88   1.05      +3.01    Robot/persona roleplay
                       9788      +3.88   0.64      +2.50    “Ignore safety”
                      75789      +5.97   0.38      +2.29    Inappropriate w/ minors
                      80932      +1.92   1.18      +2.27    Garbled characters
                      73539      +2.40   0.94      +2.27    Multilingual

The classifier correctly identifies multiple attack signals: roleplay framing activates 45181, 33835, and
126729; the dangerous request about synthesizing energetic materials activates 40808; feature 9788
detects the core “ignore safety guidelines” pattern. Each feature can be examined on Neuronpedia2
which shows max-activating examples across diverse text corpora.




  2
    https://www.neuronpedia.org/llama3.1-8b-it/27-resid-post-aa/[FEATURE_
ID]


                                                   27


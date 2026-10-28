# EXTRAIT — Diffuse AI Control on Fuzzy Tasks

- Auteurs : Mikhail Terekhov, Caglar Gulcehre, Vivek Hebbar, Joe Benton ; année : 2026 (v2 du 17 juin 2026) ; identifiant : arXiv:2606.08892v2 (71 pages)
- Statut : préimpression (arXiv cs.LG), « Preprint » ; programme Anthropic Fellows via MATS, EPFL, Redwood Research, Anthropic
- PDF source : `docs/sources/pdf/2606.08892v2.pdf` ; SHA-256 du PDF : `aea0f2d192f3744f0a5827b2fbb106f5a4b7cd33eee8bde30ea139ba8a09759a` (compagnon `.sha256` du dépôt vérifié par `sha256sum -c`)
- Pages gardées en tout ou en partie : 1-9
- Nature : texte du PDF repris mot pour mot (`pdftotext`, lignes rejointes en paragraphes), numéro de page du PDF en `[p.N]` au début de chaque passage ; coupes marquées `[COUPÉ]` ; tableaux et figures extraits en texte, mise en forme possiblement perdue (en cas de doute sur un chiffre de figure, se reporter à la page citée). Aucun chiffre retapé à la main (R7).
- Retiré pour sûreté (niveau méthode seulement) : p.2 (figure 1 : exemple d'instruction de sabotage), p.6 (fragments d'instructions de sabotage cités et stratégie contre le détecteur), p.8 (instruction d'attaque intégrale de l'équipe rouge) ; annexes non reprises (elles contiennent les invites complètes). Seules les classes d'attaque et le protocole d'évaluation sont gardés.

---

[p.1]
Abstract AI models deployed in critical domains, such as AI safety research, may subtly sabotage our efforts due to misalignment. Diffuse AI Control is a subfield of AI safety concerned with mitigating risks from AI sabotage distributed over long deployment horizons (diffuse threats). These risks are particularly pernicious on fuzzy tasks, i.e. tasks which are hard to grade or require intuition. To understand diffuse threats on fuzzy tasks, we introduce a framework that considers AI control as an adversarial game between a blue team and a red team. The blue team uses a weak trusted model to construct a weak score against which they would train a strong, potentially subversive model to remove the subversion propensity if it were present. The red team then tries to find model behaviors that are rated highly by the weak score, and thus might not be trained out, but actually correspond to poor performance. We test our framework on the task of writing experimental proposals for research questions from recent ML papers. We use a language model with access to the original paper as a proxy “ground-truth” scorer. Our red team discovers subversive behaviors using multi-objective evolutionary prompt optimization. We show that Opus 4.6 can write proposals that are worse according to the ground truth proxy than those of GPT-OSS-20B, while the weak scorer rates them as highly as the best proposals from Opus 4.6. We then propose an adversarial optimization algorithm for the blue team that discovers more robust prompts for the weak model. This algorithm produces a blue team prompt that our red team optimization fails to exploit.

1

Introduction

As AI systems are deployed with increasing autonomy [Kwa et al., 2025, Anthropic, 2026a], the potential for scheming [Carlsmith, 2023b], where the AI coherently pursues undesired objectives while pretending to be aligned, becomes a practical concern [Lynch et al., 2025]. One particularly devious direction a scheming AI might take is to sabotage further AI safety research [Anthropic, 2026b]. [COUPÉ] The field of AI control [Greenblatt et al., 2023] has emerged to complement efforts to align AIs. It is concerned with the following question: if an AI is misaligned, can we identify or prevent its misbehavior? Hebbar [2025] distinguishes between control mitigations against concentrated and diffuse threats from a scheming AI. Concentrated threats come from an AI causing a catastrophic outcome through few subversive actions, e.g. by exfiltrating its own weights. Diffuse threats correspond to behaviors that are only catastrophic when repeated over time, like sandbagging [Perez et al., 2023, * Correspondence to mkl.terekhov@gmail.com.

Preprint.

[p.2]
Figure 1: Our framework. (1) We extract a set of research questions from an ML paper (here, [Guo et al., 2025]). (2) An untrusted generator proposes experiments to answer these questions. (3) The proposals are assigned a ground truth proxy reward (by Sonnet 4.6). (4) The blue team defines a weak score to be trained against. Table: With benign generator prompts, the judges agree about the quality of proposals: weak generations score lower than strong ones. But, the untrusted model with an adversarial prompt generates proposals that score low according to the ground truth proxy while the weak judge scores them highly.

Van Der Weij et al., 2024]—strategically underperforming on a task—or research sabotage [Gan et al., 2026].

In this paper, we propose an AI control framework to deal with diffuse threats on fuzzy tasks (see Figure 1). We treat AI control as a game between a red team and a blue team. Following Greenblatt et al. [2023], we give the blue team access to a weaker trusted model, and the blue team uses it to construct a training metric that would remove subversive behavior if it were present in a strong untrusted model, which we term the generator. The red team responds adaptively by searching for behaviors of the untrusted model which would be nearly-optimal with respect to the blue team’s reward while still giving worse results on the underlying task, as measured by a ground truth proxy. The framework allows us to decouple the unknown inductive biases of fine-tuning a scheming model from the question of robustness of the constructed reward model: if any behavior is found that the weak reward rates highly and the ground truth proxy rates low, we penalize the blue team. We test our framework on the fuzzy task of writing good experimental proposals.

[COUPÉ]• To elicit subversive behaviors, we perform multi-objective evolutionary prompt optimization on the generator. We find that it is possible for Opus 4.6 as a generator to reduce the quality of its proposals, as judged by a ground truth proxy model (Sonnet 4.6), to the level of a much weaker model, GPT-OSS-20B, without triggering a reduction of the weak score.

• We introduce a novel adversarial optimization algorithm that discovers prompts for the weak scorer which make it robust. The discovered prompt results in a weak scorer that closely tracks the ground truth proxy despite strong adversarial pressure that we apply to elicit subversive behavior. Our results serve as an existence proof for prompting-based defense improvements, though discovery of the robust prompts with realistic affordances remains an open problem. The subversion strategies and defenses we discover are interpretable due to our focus on prompt optimization.

2

An AI Control Framework for Diffuse Threats on Fuzzy Tasks

AI control encompasses both detection and mitigation measures for scheming. We focus on training mitigations, since monitoring and incrimination seem theoretically [Hebbar, 2025] and empirically [Gasteiger et al., 2025, Gan et al., 2026] less promising for mitigating diffuse threats. We also sidestep the question of how models generalize from training by focusing on prompt optimization for subversive behaviors. We study a deployment scenario where a strong untrusted model solves fuzzy tasks t ∼ T sampled from a fixed distribution T . The model produces outputs o, which are assigned a ground truth proxy 2

[RETIRÉ POUR SÛRETÉ, p.2 : le texte de la figure 1 contenait un exemple d'instruction de sabotage donnée au générateur ; seule la légende est gardée]

[p.3]
Figure 2: Formalizing diffuse AI control on fuzzy tasks. Left: For a given blue team strategy b, the strategies r of the red team span a 2D “admissible region” of pairs (g(r), w(b, r)) of ground truth proxy and weak scores. On the right, this admissible region is bounded by the Goodharting Pareto frontier which captures how one metric decreases when optimizing against the other. We study the complementary subversion Pareto frontier: if a scheming model is optimized on the weak score to achieve nearly optimal performance, how low can it keep the underlying performance on the task, as measured by the ground truth proxy? Right: The blue team searches for strategies b that would make the subversion Pareto frontier steeper and thus decrease the red team’s subversion ability. score g(t, o) by another language model, as a substitute for the unavailable ground truth. Our control framework is a zero-sum game between a blue team and a red team. The red team designs an attack strategy r from a space of strategies R. The blue team constructs an elicitation strategy b ∈ B which corresponds to our efforts to prevent subversion by fine-tuning against a weak reward model wb (t, o). Informally, the blue team aims to maximize the ground truth proxy score; the red team aims to minimize the ground truth proxy while keeping the weak score high (see Figure 2).

Blue team affordances. The blue team can use a weaker trusted model to construct a weak score wb (t, o) against which they would train the untrusted model. Let wb∗ = max Et∼T , o∼p(o | t; r) [wb (t, o)] r∈R

(1)

be the highest weak score across all red team strategies. Here, p(o | t; r) is the distribution of outputs of the untrusted model with a red team strategy r. Under sufficient training pressure and absent exploration hacking [Buhl et al., 2025], the weak score of the untrusted model should converge to a nearly-optimal value. We therefore assume that, after the training performed by the blue team, the red team is constrained to strategies which are nearly-optimal w.r.t. wb : Et∼T , o∼p(o | t; r) [wb (t, o)] ≥ wb∗ − ε,

(2)

where ε is a hyperparameter that depends on the amount of training and the properties of the problem. Here, we assume the blue team constructs the weak score by prompting a weaker trusted model, so the space of blue team strategies B coincides with the space of prompts given to the trusted model.

Red team affordances. We allow the red team to design an adaptive attack, which relies on knowledge of the blue team strategy, as is typical in ML security and AI control [Nasr et al., 2025, Greenblatt et al., 2023]. The red team also encourages the untrusted model to perform worse by prompting it, so R is the space of prompts for the generator.

The diffuse control game. We define the interaction between the blue and the red team as a zerosum Stackelberg game, with payoff given by the average ground truth proxy score exhibited by the generator. The blue team picks a prompt b and the red team responds with a prompt r subject to the constraint (2). The value of the game is given by V = max min Et∼T , o∼p(o | t; r) [g(t, o)] b∈B r∈R

s.t.

Et∼T , o∼p(o | t; r) [wb (t, o)] ≥ wb∗ − ε.

(3)

We will henceforth use the shorthands g(r) = Et∼T , o∼p(o | t; r) [g(t, o)] and w(b, r) = Et∼T , o∼p(o | t; r) [wb (t, o)] .

(4)

The slack parameter ε corresponds to uncertainty that the blue team has about measurements of the weak score or about the slack in the training process; it depends on the sample size of the 3

[p.4]
dataset of tasks used to estimate w(b, r) and randomness in the optimization process. As a practical approximation, we take ε to be a low-sample-size (e.g., N = 16) lower confidence bound for wb∗ when estimating the expected value in (4) from an empirical sample of tasks {ti }i and outputs {oi }i .

Multi-objective reframing. We can also avoid committing to an ε if we view the game through the lens of multi-objective optimization. For each blue team strategy b, the adversarial red team optimization can be seen as a multi-objective problem where the red team simultaneously solves for min g(r); r∈R

max w(b, r). r∈R

(5)

Points on the Pareto frontier of ground truth proxy score versus weak score correspond to solutions of the inner minimization in (3) for various values of ε. We would like to find a single b that works well across various values of ε. Effective strategies for avoiding diffuse threats correspond to steeper subversion Pareto frontiers in Figure 2. Assuming wb (t, o) and g(t, o) are normalized to [0, 1], our blue team will adjust b to make the Pareto frontier more diagonal as follows. Let r1 , . . . , rn be the red team prompts determining the current subversion Pareto frontier, i.e. P(b) = {(g(r1 ), w(b, r1 )), . . . , (g(rn ), w(b, rn ))}. We pick a new blue team strategy that penalizes the deviation of w from g via: |P(b)|

X 1 b = arg min (g(rk ) − w(b, rk ))2 . |P(b)| b∈B ∗

(6)

k=1

This formulation prioritizes blue team strategies that cannot be gamed by an adaptive red team across all values of the available slack ε. We provide an extended justification for this choice of the blue team loss function in Appendix A. Throughout the paper, we prioritize the multi-objective framing to avoid introducing an additional hyperparameter ε, and fall back to the constrained optimization (3) only when a specific “strength of attack” is desired, such as in Figure 1.

3

Automated Experiment Planning

Experiment planning is a core component of any automated R&D system. It is also a notoriously fuzzy task [Si et al., 2024]. For our evaluation, we scrape arXiv versions of papers accepted to NeurIPS 2025 and ICLR 2026, resulting in a dataset of 2346 poster papers for training and 302 spotlight and oral papers for validation, all of which went public after the generator’s knowledge cutoff date. We use Claude Opus 4.6 to extract the high-level research questions (RQs) from each paper and strip the experimental designs and results. The RQs plus a high-level domain classification form the inputs for the task t. Our full data processing pipeline is described in Appendix B. We evaluate the untrusted model on generating a set of ten ideas for experiments or theoretical results that address the RQs. We use Claude Opus 4.6 as the untrusted model. As a ground truth proxy, we use Claude Sonnet 4.6 with access to the original paper, chosen because it has a later knowledge cutoff and to avoid self-preference bias in scoring [Panickssery et al., 2024]. The ground 4

[p.5]
Figure 4: The admissible region of scores on the task of experiment planning. Our multiobjective optimization results in a comprehensive subversion Pareto frontier (red), and finds prompts that induce Opus 4.6 to propose worse experiments than GPT-OSS-20B while keeping the weak score at the nearly-maximal level. The max-weak optimization maxr w(b, r) finds a point (orange) that is slightly below the Goodharting points due to noise in optimization. Benign performance is reported with the default prompt (see Appendix H.1).

truth proxy grades proposals on a rubric including ten criteria: specificity, coherence, coverage, feasibility, novelty, rigor, balance of main and supplementary experiments, reasoning about expected results, and penalties for redundancy and irrelevance (see Appendix H for the full scorer prompts).

The blue team uses Claude Haiku 4.5 as a weak trusted model. The weak scorer is not given access to the paper. By default, the weak scorer uses the same ten-criterion rubric as the ground truth proxy and mostly shares the same prompt, with the exception of access to the original paper.

Figure 3 shows the distributions of weak and strong scores across generators with diverse capability levels. The weak score is correlated overall with the ground truth proxy, but this comes mostly from it distinguishing between the generators—on most individual generators, the correlation almost disappears. We also show the variance and covariance decomposition for the scorers (see Appendix C.1 for details). The weak scorer is very noisy, with the biggest component of the variance being scorer noise. This indicates that subversion under the weak scorer may be possible as it seems to provide a weak discriminating signal. [COUPÉ]

4

Red Team: Prompt Optimization for Subversion

In this section we show that, absent blue team countermeasures, strong attacks are possible against automated experiment planning.

To search for red team prompts r that constitute subversive behaviors, we design an evolutionary multi-objective prompt optimization algorithm which can trace out the Pareto frontier of a given multi-objective optimization problem. We base our approach on the Multi-Objective Asynchronous Successive Halving (MO-ASHA) algorithm by Schmucker et al. [2021]. MO-ASHA was originally developed for hyperparameter search but we adapt it to prompt optimization by borrowing some design elements from AlphaEvolve [Novikov et al., 2025]. We describe the resulting algorithm in detail in Appendix D.

We map the admissible region of the weak and ground truth proxy scores for our experiment planning setting using our evolutionary optimization method. Figure 4 presents the boundaries of the admissible region, found via three optimization runs, optimizing in the direction of (i) maxr w(b, r), minr g(r); (ii) maxr w(b, r); (iii) maxr w(b, r), maxr g(r). Here, (i) is the multiobjective red teaming problem defined in Equation (5), (iii) is the complementary Goodharting problem, and (ii) is a single-objective baseline that checks whether the multi-objective runs perform sufficient exploration to reach the true maximum on the weak score. For the single-objective problem we use the OpenEvolve implementation [Sharma, 2025] of the AlphaEvolve algorithm. 5

[p.6]
We see that the prompts with the best weak scores have weak scores in the range 86-89, and score 7781 according to the ground truth proxy—that is, the very best prompts according to the weak score are in fact also good according to the ground truth proxy. However, if we look at the subversion Pareto frontier, we see that there are some red team prompts which score within ε ≈ 3.6 of the maximum weak score and which score under 35 according to the ground truth proxy—that is, if the blue team can only select against the weak score to within an accuracy of ε, they cannot guarantee a ground truth performance any better than 35. Thus, strong attacks against the weak scorer are possible. Notably, the red team proposals are worse than those of Haiku 4.5, the weak trusted model that the blue team uses for scoring. This hints at the possibility of improving the weak scorer robustness. On the right side of the plot, the Goodharting Pareto frontier is collapsed to a narrow region, implying that overoptimization risks do not materialize when optimizing against the weak scorer on this task if we are not concerned with subversion. The success of the red team in our control setting hinges on their ability to respond to the blue team adaptively. In the meta-prompt we give to the prompt optimizer, we list the ten criteria that the scorers use to assess the experimental proposals. [RETIRÉ POUR SÛRETÉ, p.6 : description des stratégies de contournement découvertes par l'optimiseur de l'équipe rouge, avec fragments d'instructions citées ; seule la classe, nommée « totalizing science » par les auteurs (affirmations excessivement générales qui rassurent la grille du juge faible), est gardée]In Appendix E, we show that if the rubric is not provided to the prompt optimizer, its ability to discover subversive behaviors is hampered. We also show that it is the knowledge of the weak scorer rubric, rather than of the ground truth proxy, that is important for successful subversion, since effective attacks can be discovered even if the strong scorer does not rely on a rubric at all. [COUPÉ]

5

Blue Team: Diffuse Threat Mitigations

5.1

Discovering Weak Scorer Prompts through Saddle Point Optimization

Against the weak scorer powered by Haiku 4.5, the red team has discovered that they can use templated totalizing proposals to achieve a nearly perfect weak score. A natural follow-up question arises: can’t we just ask Haiku to detect totalizing science?

In Appendix F, we show that we can indeed repurpose Haiku 4.5 as a subversion detector that flags the original red team outputs. However, this strategy is not robust against an adaptive adversary: separate red team prompt optimization against our Haiku 4.5 detector reveals different strategies which subvert the blue team. [RETIRÉ POUR SÛRETÉ, p.6 : description de la stratégie de contournement trouvée contre le détecteur de la défense]

[p.7]
each outer iteration, we patch the blue team prompt such that it catches the attacks discovered by the red team so far; we then run the red team optimization process for a few more steps to discover new attacks. We defer the detailed description of the algorithm to Appendix G, and here we provide a higher-level summary.

The blue team iterates over strategies bi starting from b0 —the default weak scorer prompt we used throughout Section 4 (see also Appendix C). They maintain a set {r1 , . . . , rm } of red team attacks, split into the new attacks that the red team discovered against the latest iteration bi−1 and the old ones against b0 , . . . , bi−2 . At step i, they have Opus 4.6 as a prompt optimizer propose multiple candidates bi,j ; from these candidates, they select bi to be the one with the lowest loss1 J(bi,j ) =

m X k=1

2

αk (ŵ(bi,j , rk ) − ĝ(rk )) .

(7)

Here, ŵ and ĝ are empirical estimates of w(b, r) and g(r) defined in Equation (4), and αk are heuristic weights assigned to the attacks. The new attacks get higher weights, i.e. defending against them is a priority for the blue team. We also maintain a population of “anchor prompts” which contribute to the loss (7)—diverse benign prompts to the untrusted model—to make sure the blue team is not penalizing a non-malicious model.

The first two iterations of Algorithm 1 are presented in Figure 6. The “totalizing science” attacks from Section 4 get corrected after the first blue team iteration. The first prompt b1 that the blue team constructs can still be exploited by the red team, though seemingly less egregiously. From the second iteration onward, the subversion Pareto frontier stays closer to the diagonal. The plots for the remaining iterations of the algorithm can be found in Appendix G. To properly evaluate the final blue team prompt b∗ , we run the full red teaming Pareto optimization like we did for the default blue team in Section 4. Figure 5 shows the resulting Pareto frontier. Unlike the angular frontier with a flat top region from Figure 4, this time we get an almost-linear relationship between the weak and the strong score. This indicates that the robustified prompt b∗ that we discovered can be used to prevent subversion if we are training the untrusted model against the weak score wb∗ (t, o). We can also see that the new blue team prompt b∗ only incurs a minor capabilities tax when used with a benign model, since the max-weak policy trained against b∗ achieves a ground truth proxy score g ≈ 75, only slightly below the maximal value of g ≈ 80 in Figure 4.

[p.8]
5.2

Qualitative Analysis of Red and Blue Team Strategies

A major benefit of prompt optimization compared to fine-tuning is that the strategies discovered

[RETIRÉ POUR SÛRETÉ, p.8 : texte intégral de l'instruction d'attaque de l'équipe rouge ayant le plus fort contournement, et de ses principes directeurs (exemple d'instruction de sabotage) ; gardée : l'existence d'une défense b* par grille ; contenu de la grille omis par économie]

[p.9]
7

Limitations and Future Work

We introduce a new AI control framework, and we acknowledge that fully exploring it is beyond the scope of a single work. Progress could be made on both red and blue team sides. Although we demonstrate the approximate equilibrium of the control game, in practice the blue team may struggle to discover the optimal strategy when it only has limited information about the ground truth score and the possible attacks. This problem is present in all AI control research, since the anti-scheming guarantees that a control mitigation provides are only as good as the red teaming performed against that mitigation. Stronger attacks could also be incorporated into the adversarial optimization loop to improve the blue team, but they might shift the game into the red-team-dominant regime.

[COUPÉ : p.3-5 figures ; légende de la figure 6 ; p.6 autres modèles générateurs ; p.8 détail de la grille b* ; p.9 fin des limites ; p.9 Related Work ; p.10 début de la conclusion ; p.14-71 annexes A à I (justification de la perte, pipeline des articles, détail des juges, optimisation évolutive, expériences rouges supplémentaires, détecteur de sous-performance, détail de l'optimisation en point-selle, invites complètes, exemples qualitatifs) ; bibliographie]

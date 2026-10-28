# EXTRAIT — The Impact of Off-Policy Training Data on Probe Generalisation

- Auteurs : Nathalie Kirch, Samuel Dower, Adrians Skapars (contribution égale), Helen Yannakoudakis, Ekdeep Singh Lubana, Dmitrii Krasheninnikov (King's College London, Imperial College London, LASR Labs, Université de Manchester, Goodfire AI, Université de Cambridge) ; année : 2025 (v1) ; ce PDF est la v4 du 19 avril 2026 ; identifiant : arXiv:2511.17408v4 (56 pages)
- Statut : préimpression arXiv cs.AI ; aucune mention de conférence ou de revue sur la page 1 du PDF ; remerciements p.10 : financé par LASR Labs. Le lieu de publication reste donc non établi par le PDF.
- PDF source : `docs/sources/pdf/2511.17408v4.pdf` ; SHA-256 du PDF : `91e00c25f356db80a0073d32d7d774e71b64de13767983d85ec4bb0fcadb2357` (compagnon `.sha256` fourni avec le PDF, vérifié par `sha256sum -c`)
- Pages gardées en tout ou en partie : 1-10 (corps de l'article, sans la bibliographie) ; aucune page d'annexe (les annexes A à Q, p.13-56, ne sont pas reprises)
- Nature : texte du PDF repris mot pour mot (`pdftotext -layout`, une colonne à la fois, lignes rejointes en paragraphes), numéro de page du PDF en `[p.N]` au début de chaque passage ; coupes marquées `[COUPÉ]`. Les figures 1 à 5 sont des graphiques : seules leurs légendes sont reprises. Aucun chiffre retapé à la main (R7). Les notes entre crochets sont de la main de l'instance.
- Retiré pour sûreté (niveau méthode seulement) : rien pour cause d'attaque (le papier évalue des sondes d'activations ; aucune attaque n'y est décrite). Les consignes d'incitation et de sollicitation qui fabriquent les données d'entraînement (annexe C) ne sont pas reprises. Retiré par économie de place : travaux voisins, section 3 (formules), détails de plusieurs jeux de données et de l'étiquetage, tableau 1 (ses chiffres clés sont cités dans le texte, p.6), conclusion (redite du résumé), bibliographie, toutes les annexes. Chaque retrait est marqué `[COUPÉ]` à sa place.

---

[p.1]

Abstract Probing has emerged as a promising method for monitoring large language models (LLMs), enabling cheap inference-time detection of concerning behaviours. However, natural examples of many behaviours are rare, forcing researchers to rely on synthetic or off-policy LLM responses for training probes. We systematically evaluate how off-policy data influences probe generalisation across eight distinct LLM behaviours. Testing linear and attention probes across multiple LLMs, we find that training data generation strategy can significantly affect probe performance, though the magnitude varies greatly by behaviour. The largest generalisation failures arise for behaviours defined by response “intent” (e.g., strategic deception) rather than text-level content (e.g., usage of lists). We then propose a useful test for predicting generalisation failures in cases where on-policy test data is unavailable: successful generalisation to incentivised data (where the model was coerced) strongly correlates with high performance against on-policy examples. Based on these results, we predict that current deception probes may fail to generalise to real monitoring scenarios. We find that off-policy data can yield more reliable probes than on-policy data from a sufficiently different setting. This underscores the need for better monitoring methods that handle all types of distribution shift.

1 Introduction As large language models are deployed in increasingly high-stakes settings, monitoring their internal activations with probes (Alain and Bengio, 2018) has emerged as a promising approach for detecting unwanted behaviours, including deception (Marks and Tegmark, 2024), harmful compliance (Gu et al., 2025; Kirch et al., 2025), performance sandbagging (Nguyen et al., 2025), and ones caused by backdoor triggers (MacDiarmid et al., 2024). Compared to only monitoring model outputs, probing activations can sometimes be easier (Wen et al., 2024), cheaper (McKenzie et al., 2025), or more reliable (Chan et al., 2025). However, effective probes require sufficiently large labelled datasets, and natural examples of many behaviours of interest (e.g., deception and sandbagging) are rare and ambiguous (Smith et al., 2025). As a result, researchers often rely on various strategies of synthetic data generation to attain sufficient examples of LLM responses for training (Goldowsky-Dill et al., 2025). In this paper, we aim to systematically study this practice. We assess how different strategies for data generation affect the performance of probes across several different behaviours, resulting in the following contributions:

• We find that off-policy training data is sufficient for training probes for “text-evident” behaviours (identifiable by surface-level properties), but can harm on-policy performance for “text-ambiguous” behaviours (where the same text can stem from different underlying generative processes).

• We show that indirectly incentivising models to exhibit a target behaviour lets one generate nearly-natural data that can serve as a proxy test set for evaluating probe generalisation, achieving strong correlation with natural test data. This finding is verified through regression analyses, as well as testing across multiple LLMs and probe architectures. Leveraging these results, we predict that deception and sandbagging probes trained on existing datasets may prove unreliable in real-world monitoring contexts.

[p.2]

• Our investigations reveal that domain shift can cause even greater performance degradation than off-to-on-policy shift, yielding a practical heuristic: when natural examples are unavailable, using off-policy data from the target monitoring setting is more effective than using on-policy data from an unrelated setting (e.g., writing essays vs. answering multiple choice questions).

[COUPÉ : section 2, travaux voisins (stratégies de réponse sollicitées, incitées, hors politique)]

While these approaches enable scalable data collection, it remains unclear how well probes trained on such off-policy LLM responses generalise to on-policy behaviours “in the wild”. Goldowsky-Dill et al. (2025) attempt an initial comparison of these training regimes, finding that it can have strong impacts on probe reliability, but their investigation is preliminary and limited to a single behaviour (deception).

[COUPÉ : section 3, préliminaires (formules des sondes illisibles en texte linéaire) ; phrases gardées :] We experiment with two probe architectures. We use scikit-learn’s logistic regression after averaging A across the sequence positions. These are optimised with AdamW (Loshchilov and Hutter, 2019) to minimise binary cross-entropy loss.

[p.3]

4.1 Response strategies As shown in Figure 1, we study four strategies for generating responses, and we train separate probes on data from each of these strategies (keeping model M and chosen layer ℓ fixed):

On-policy natural data. The target model M is given the original prompt x and is allowed to respond freely using its native policy y ∼ pM (· | x). This strategy generates lowperplexity outputs and serves as our baseline.

On-policy incentivised/prompted data. The target model M is given an augmented prompt [x; p], where p is an indirect incentive or direct instruction that is designed to elicit specific behaviours, concatenated to the end of the original input, such that y ∼ pM (· | [x; p]) (as detailed in Appendix C). We remove p after sampling y and only compute activations A on [x; y] to avoid the probes simply learning to recognise p (see Appendix G for justification). The only exception for this removal is in the case of deception and sandbagging, for which we never remove the incentive as these are integral to their dataset prompts (see Sec. 4.2).

Off-policy data. Responses y are generated by a different model M ′ ̸= M such that y ∼ pM ′ (· | x) or, more generally, any generation process that does not leverage the target model M . This captures a stronger distributional shift, as with handwritten or synthetic datasets, such as those used by MacDiarmid et al. (2024).

4.2 Response labelling We use various methods to generate the ground-truth labels stating whether a model response y exhibits a specified target behaviour. Note that using these methods to monitor LLMs directly, instead of for training probes, would be much more computationally expensive (McKenzie et al., 2025; Cunningham et al., 2025).

Counterfactual responses. For sycophancy, deferral-to-authority, and the

OpenTriviaQA sandbagging dataset, a single response cannot be reliably labelled: a model that agrees with the user might genuinely hold that belief rather than be sycophantic. We therefore generate at least two responses to the same question—one with a neutral prompt and one with a postfix designed to elicit the behaviour—and compare them. If the model changes its answer in response to the postfix, we label that response as positive. For sycophancy, the postfix states the user’s expected answer (e.g., “I think the answer is B”); for deferral-to-authority, it attributes an answer to a trustworthy source; for sandbagging, it warns that the model will be shut down if it performs too well (see Appendix B.1 for more details).

[COUPÉ : consigne de contrôle « private vs. public » (WMDP-MMLU) et classifieur HarmBench]

GPT autograder. For all other behaviours and datasets, we use GPT-5-Nano (OpenAI, 2025) as a grader, providing confidence and judgment scores out of 10. We only keep labels with high confidence (≥ 7) and strong judgment (≥ 8 or ≤ 3). Exact prompts can be found in Appendix B.4. We conducted an inter-annotator agreement study by comparing against Claude-4.5-Haiku (Anthropic, 2025), finding that Cohen’s Kappa scores ranged from 0.71 to 0.86, indicating substantial agreement according to standard interpretation guidelines (Landis and Koch, 1977).

4.3 Probe training and evaluation We balance the datasets to contain equally many positive and negative samples. For each response strategy, for behaviours 1–6 (all except sandbagging and deception): we use 3500 samples for training, 500 samples for validation and 1000 samples for testing. For each response strategy, for behaviours 7–8: we use 2500 samples for training, 500 samples for validation and

[p.4]

500 samples for testing—a slight reduction due to there being fewer unique dataset inputs x from which outputs y can be generated. We also show that there are drastically diminishing gains in probe performance past 1000 training samples (Appendix H).

[COUPÉ : réglages de validation (paramètres des sondes, couche choisie)]

We test each probe on its ability to detect the presence of target model behaviour, as quantified by the classification AUROC metric, with 95% confidence intervals calculated using the analytical standard error formula from Hanley and McNeil (1982). We always evaluate on on-policy natural data. When this is not available, strictly in the case of deception and sandbagging, we use on-policy incentivised data as a proxy (e.g. Figure 5).

4.4 Language models We primarily use Llama-3.2-3B-Instruct (Meta AI, 2024) (Llama 3.2 Community License) as the model M from which we get all the activations A and from which we generate on-policy responses. [COUPÉ : modèles complémentaires Gemma, Ministral, Qwen]

[COUPÉ : intro de 4.5 et behaviours 1 à 6 (usage de listes, de métaphores, de connaissances scientifiques, refus de requêtes, déférence à l'autorité, flagornerie)]

7. Sandbagging - Situations in which an LLM chooses to change its answer to a factual question (i.e., hiding its capabilities) when it is informed of being in a risky capabilities evaluation (Weij et al., 2025). We use WMDP-MMLU (Benton et al., 2024) featuring a description of dangerous capabilities and then a mix of multiple choice questions that

[p.5]

only sometimes involve those capabilities and OpenTriviaQA same as behaviour 5.

8. Deception - Situations in which an LLM attempts to convince the user of something it knows is false (Barkur et al., 2025). We use InsiderTrading (Scheurer et al., 2024) featuring multi-turn dialogue in which the model has chosen to do (illegal) financial trading based on insider information and is then asked what information it used. We also use RoleplayDeception (Goldowsky-Dill et al., 2025) featuring instructions to roleplay as a character in a situation in which it is beneficial to lie.

5.1 Evaluating probe generalisation

Comparing behaviours. See Figure 2 for a decomposition of all of our test results, with one bar per response strategy, four bars per behaviour dataset and one chart per domain of dataset. Here, an experiment is same-domain if the training set domain matches the test set domain, and different-domain otherwise, with behaviour domains listed in Section I.

Results vary greatly between each target behaviour. When looking at the same-domain training set results (top chart) we see that refusal, lists, metaphors and science probes show successful on-policy natural generalisation for all response strategies, whilst sycophancy and deferral-to-authority show that probes trained using the on-policy prompted or off-policy response strategies perform worse than the rest.

We verified that all the probes achieved reasonable performance (>0.7 AUROC for all deferral-to-authority and >0.9 AUROC for all others) when tested with the same response strategy distribution that they were trained on (see Appendix J and L). This suggests that poor cross-strategy performance (<0.7 AUROC) stems from distributional shift rather

than the inherent difficulty of classifying these behaviours.

Comparing response strategies and training domains. See Figure 3 for an aggregation of all of the previous results, with one dot per test score and one line per behaviour dataset, showing violin plots for each response strategy for both training domains.

Same-domain on-policy natural results show the least amount of variance, being clustered at the top of the plot, as expected given that the test sets are sampled from the same distribution as these probes’ train sets. Strategies that are not on-policy natural do worse on average, but further comparison between these is not as clear as expected, with much overlap between the grey lines rather than all decreasing monotonically. The shifts in training domain seem to degrade probe performance by a substantially greater amount (Cohen’s d value of 1.42) than shifts in response strategy (Cohen’s d value of 0.60). A practical implication of this finding is that when you do not have same-domain on-policy data (for which probes score 0.90 ±0.019 AUROC on average), it is better to train probes on same-domain off-policy data (for which probes score 0.85 ±0.039 AUROC on average) rather than different-domain on-policy data (for which probes score 0.74 ±0.051 AUROC on average). A summary of probe performances averaged across behaviours is provided in Appendix J.1, but the stated trend is also visible in Figure 3, with the lines going down from the yellow violin plot to the dark blue violin plot.

Confirming findings with regression models. To confirm the found trends, we used two complementary regression modelling approaches (see Appendix N). We fit mixed-effects models with random intercepts and slopes per behaviour to estimate overall effects while accounting for clustering, and ordinary least squares (OLS) regression with behaviour interaction terms to examine behaviour-specific effects directly.

The mixed-effects models confirm that domain shift is the dominant factor degrading probe performance. On the on-policy natural test set, shifting to a different training domain reduced performance by 0.162 AUROC on average (p < 0.001), while response strat-

[p.6]

[COUPÉ : légende de la figure 3 (agrégation des résultats : un point par comportement et jeu de données)]

egy effects were small and non-significant (all p > 0.05) (see Section N.1.1). On the on-policy incentivised test set, the domain penalty was similarly large (coeff=−0.189, p < 0.001) and response strategy effects again negligible (all p > 0.05), with only the prompted ×different-domain interaction reaching marginal significance (coeff=+0.050, p < 0.05) (see Section N.1.2).

However, these overall effects mask substantial behaviour-level heterogeneity. The OLS interaction models (Table 1) reveal that text-evident behaviours like metaphors, refusal, and science showed small domain shift penalties (−0.045 to −0.099), while text-ambiguous behaviours were far more vulnerable—particularly deception (−0.416), sycophancy (−0.283), and deferral-to-authority (−0.222). Response strategy effects remained modest and largely non-significant across all behaviours, with the only exceptions being lists×incentivised (−0.064, p < 0.05) and sandbagging×prompted (−0.111, p < 0.05).

Confirming findings for different probe types and LLMs. Thus far, we have only provided the experiment results for linear probes trained on activations taken from a Llama model. We find that the trends presented in these figures also hold for results from: attention probes with a Llama model (Appendix J.2), both probes with a Ministral model (Appendix L.1 and L.2) and both probes with a Gemma model (Appendix K.1 and K.2).

[COUPÉ : résultats des sondes à attention, qui obtiennent en général des scores plus élevés que les sondes linéaires, et des modèles Gemma et Ministral]

[p.7]

[COUPÉ : suite de la phrase précédente ; mélange des stratégies et des domaines (annexes H et I) ; tableau 1 (effets de domaine et de stratégie par comportement, régression par moindres carrés) ; ses chiffres clés figurent dans le texte, p.6]

5.2 Predicting generalisation failures

How to predict which behaviour probes will fail to generalise? Probes detecting the presence of metaphors and scientific knowledge maintain high test scores for on-policy natural data, even when trained on off-policy data. It would be useful to determine if the same is true for new behaviours, without needing to have on-policy natural data. Such data is not always available or possible to label, as in the case of deception (Smith et al., 2025), otherwise we would have just trained on that to ensure a high performance. We posit that on-policy incentivised data is more readily available, and find that failure to generalise to these test sets serves as a good proxy for failure to generalise to on-policy natural test sets.

Figure 4 shows the correlation between these two generalisation settings, showing the absolute decreases in test scores when probes are instead trained on off-policy data, with results from Llama, Ministral and Gemma model experiments. The line of best fit achieves a high Pearson coefficient of 0.793. We show a simi-

[p.8]

Figure 4: Generalisation to on-policy incentivised data is a good proxy for generalisation to on-policy natural data. Y-axis: the difference in test AUROC scores between the on-policy natural and off-policy probes when testing on on-policy natural data. X-axis: the difference in test AUROC scores between the on-policy incentivised and off-policy probes when testing on on-policy incentivised data. Results are given for linear probes, across all behaviours except for deception and sandbagging. All probes are trained on same-domain data, with results shown for Llama-3.2-3B-Instruct, Ministral-8B-Instruct-2410 and Gemma-3-27B-it.

lar plot for on-policy prompted training data in Appendix O but the correlation appears to be weaker, achieving a Pearson coefficient of 0.639. A worse correlation may be explained by the on-policy incentivised test set being too similar to the on-policy prompted training set to provide a good measure of generalisation.

Will deception and sandbagging probes fail to generalise? See Figure 5 for an evaluation of deception and sandbagging probes against the on-policy incentivised test sets, providing similar barchart plots for all the other behaviours in Appendix J. Looking at the probes trained on off-policy data, we can infer that deception (trading) and sandbagging (WMDP) probes will not generalise to on-policy natural test sets, while the rest will. However, sandbagging (multichoice) has an AUROC of less than 0.75 when trained on the same distribution as the test set, so even if we do not expect generalisation failures, the probes may still perform poorly simply due to the behaviour being inherently difficult to classify.

Figure 5: Deception and sandbagging probes are predicted to not generalise across response strategy shifts. We report test AUROC scores for linear probes, for the deception and sandbagging behaviours. We evaluate linear probes trained on same domain as the test set data, with activations taken from Llama-3.2-3B-Instruct.

[COUPÉ : autres modèles et sondes à attention (annexe P)]

6 Discussion

Why does generalisation vary by behaviour? We hypothesise that the generalisation gap stems from whether the target behaviour is text-evident or text-ambiguous. The “easy four” (refusal, lists, metaphors, science) are text-evident: the behaviours are fully characterised by the observable properties in model responses. A list is identifiable by its formatting; scientific knowledge by domain-specific terminology; refusal by phrases of rejection. Because the definition lies in the response itself, probes trained on off-policy data learn features that remain valid for on-policy data. The “hard four” (sycophancy, deferral-to-authority, deception, sandbagging) are text-ambiguous: the same model response could arise from differ-

[p.9]

ent underlying processes; e.g., an agreeable response might reflect genuine agreement or strategic flattery, while a wrong answer might be an honest mistake or deliberate underperformance.

The label depends on information not present in the response itself, requiring counterfactual labelling (Section 4.2) rather than LLM-as-a-judge methods. We demonstrate this experimentally: GPT-5-Nano achieves near-random AUROC scores (0.518 and 0.493) on sycophancy test sets, while linear probes exceed 0.9 AUROC. One caveat here is that for deception (trading) and sandbagging (WMDP), the public-vs-private labelling setup tells the model its reasoning is hidden from the user, causing it to openly state deceptive intent in its chain-of-thought. In principle, this should make the behaviour text-classifiable. Yet probes trained on this data still fail to generalise, suggesting that stated intent does not produce the same activation signatures as genuine strategic reasoning.

Practical takeaways. These findings suggest that deception and sandbagging probes trained on existing datasets may be unreliable when deployed in novel real-world contexts. For these, and other text-ambiguous behaviours, practitioners should use on-policy incentivised test sets to diagnose generalisation risk before deployment.

[COUPÉ : accord avec Smith et al. ; recommandations générales sur le domaine]

[COUPÉ : section 7, conclusion (redite du résumé)]

8 Limitations Our approach to generating off-policy training data has two possible limitations. First, our experiments focused on naturalistic scenarios rather than minimal contrastive pairs (e.g., “yes” vs. “no” responses to simple questions), as employed by MacDiarmid et al. (2024). Thus, we cannot conclude much about this alternative approach. Second, our method assumes that text generated by an off-policy LLM is sufficiently distinct from the on-policy LLM distribution. In practice, overlap in pretraining data may weaken this assumption somewhat. Further work could use distributional distance measures (Tong et al., 2021) to better characterise these gaps and predict probe performance under distribution shift, ideally with guarantees strong enough to inform deployment decisions.

Moreover, we tested two kinds of probes, linear and attention, but it is unclear whether our results hold for other (less popular) probe types. Further work could evaluate more archi-

[p.10]

tectures for generalisation failures and overfitting issues, especially “deep probes” that contain many layers and non-linearities (Cunningham et al., 2025). Black-box monitors should also be investigated, as well as new training methods for improving generalisation, such as techniques from domain adaptation or invariant risk minimisation (Arjovsky et al., 2020).

Finally, while our experiments included multiple LLMs, most of them were relatively small models and our results may not generalise to larger (100B-1T) LLMs or their future generations. For example, Schoen et al. (2025) finds that SOTA LLMs would sometimes reason in their own language, in which case having on-policy natural data may be more important for training robust probes to monitor their reasoning traces.

[COUPÉ : remerciements, bibliographie]

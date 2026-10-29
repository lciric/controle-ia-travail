# TEXTE INTÉGRAL — arXiv:2609.17560v1

- Identifiant : arXiv:2609.17560v1
- Titre (tel qu'écrit dans le PDF) : Pay Only for Disagreement: Certified No-Regression Verdicts for Model Updates with Matching Label-Complexity Bounds
- PDF source : `docs/sources/pdf/2609.17560v1.pdf` ; SHA-256 du PDF : `ef318a961de7d5f237b7bdca063b7441d3cab00522bc0e6baec383603af2d11f` (compagnon `.sha256` vérifié par `sha256sum -c` avant lecture)
- Outil d'extraction : `pdftotext -layout -enc UTF-8` (pdftotext version 24.02.0), page par page, marqueur `[p.N]` au début de chaque page (N = numéro de page du PDF, à partir de 1)
- Nombre de pages : 31
- Caractères de contrôle produits par l'extraction (glyphes de polices sans correspondance : délimiteurs de formules, texte de figures à police codée) : 32, les caractères nuls supprimés, les autres remplacés par le caractère de remplacement U+FFFD (position gardée) ; pages : 3 (1), 7 (2), 8 (1), 10 (7), 12 (1), 13 (1), 22 (1), 23 (6), 24 (6), 25 (5), 26 (1)
- Nombre de caractères du texte extrait (marqueurs `[p.N]` compris, en-tête exclu) : 108224
- Mention : texte intégral, aucun retrait, contenu d'attaque verbatim possible — dépôt privé seulement (jamais dans la copie expurgée publique ; règle de sûreté modifiée par R-439).
- Provenance : tout chiffre repris ailleurs doit citer la page `[p.N]` et être relu sur le PDF empreinté (R7). La mise en page en colonnes, les formules et les tableaux peuvent être mal ordonnés dans l'extraction : se reporter au PDF.

---

[p.1]

                                         Journal of Machine Learning Research (2026)                                             Submitted ; Published




                                         Pay Only for Disagreement: Certified No-Regression Verdicts
                                         for Model Updates with Matching Label-Complexity Bounds

                                         Vishnu Bindu Balachandran                                vishnubindubalachandran@outlook.com
                                         Independent Researcher
                                         www.vishnubindubalachandran.com


                                         Editor:
arXiv:2609.17560v1 [cs.LG] 22 Jul 2026




                                                                                         Abstract
                                             Every production model is updated, by retraining, fine-tuning, quantization, or a silent
                                             vendor swap, and each update risks being worse than what it replaced. We formalize
                                             update promotion as certified paired risk-difference auditing. Our starting point is a support
                                             identity. The risk difference between two models lives on the inputs where they disagree,
                                             observable without labels. We build Discern, a sequential two-tier protocol. A zero-label
                                             tier certifies benign updates whose disagreement rate is below tolerance from unlabeled
                                             traffic alone. An audited tier labels only sampled disagreements through an anytime-valid
                                             confidence sequence, valid at every stopping time and under any label-routing rule, even an
                                             adversarial judge. We prove finite-sample validity and matching label-complexity bounds
                                             e 2 /ε2 ) at the rate level, so exploiting free disagreement provably saves a factor Θ(1/ρ)
                                             Θ(ρ
                                             over any pairing-blind auditor, and the guarantee composes across an unbounded sequence of
                                             promotions from one error budget. Across 14,000+ replayed audit streams over 785 update
                                             pairs, including LoRA fine-tunes of language models up to 1.4B parameters, miscoverage
                                             is 0.0002 (nominal 5%), power 0.986 with zero false alarms, and 56% of benign updates
                                             certify with zero labels. Each audit emits a machine-checkable evidence record for EU AI
                                             Act post-market monitoring.
                                             Keywords: model updates, anytime-valid inference, label complexity, confidence sequences,
                                             deployment monitoring


                                         1 Introduction
                                         Machine learning systems in production are not static artifacts. Teams retrain on fresh data,
                                         adjust hyperparameters, fine-tune on new domains, quantize weights for cheaper inference,
                                         distill large models into small ones, and absorb silent upstream changes when a managed
                                         API provider swaps its backbone. Each such event replaces a deployed model f with a
                                         candidate g, and each replacement carries the same operational risk, since the update may
                                         quietly be worse than what it replaced, either overall or on a slice of traffic that matters.
                                         Post-deployment incident reports and the model-update literature on churn and backward
                                         compatibility document this failure mode repeatedly (Milani Fard et al., 2016; Yan et al.,
                                         2021; Srivastava et al., 2020).
                                             Despite the ubiquity of the event, the promotion decision is statistically informal in most
                                         organizations. The dominant practices are (i) fixed offline test suites, which cannot reflect
                                         current traffic and are exhausted by repeated use, (ii) A/B tests on business metrics, which
                                         are slow, costly in exposure, and do not certify model correctness, and (iii) uniform labeling

                                         ©2026 Vishnu Bindu Balachandran.
                                         License: CC-BY 4.0, see https://creativecommons.org/licenses/by/4.0/. Attribution requirements are provided at
                                         http://jmlr.org/papers/v/.html.

[p.2]

                               Vishnu Bindu Balachandran




campaigns on sampled traffic, which are statistically sound but pay for an enormous number
of labels that carry no information about the update. The third point is the crux. If the
old and new model agree on a traffic point, that point contributes exactly zero to the risk
difference between them, no matter what the true label is. Labels spent on agreements are
wasted, and under realistic updates the models agree on 80% to 99.9% of traffic.
    This paper treats the promotion decision as a first-class statistical object with certified
verdicts, matching label-complexity bounds, and lifetime soundness across a sequence of
updates. We study the paired risk difference ∆ = E[ℓ(g(X), Y )] − E[ℓ(f (X), Y )] between
candidate g and incumbent f , signed so that ∆ > 0 means the update is a regression. The
operator wants one of two certified verdicts at tolerance ε and confidence 1 − δ, either a
no-regression certificate asserting ∆ < ε, or a regression alarm asserting ∆ > 0. The audit
must run on live traffic, must remain valid when the operator peeks continuously and stops
as soon as evidence suffices, and must spend as few human labels as possible.
The support identity and its consequences. Everything follows from one elementary
observation. Write A = 1{f (X) ̸= g(X)} for the disagreement indicator, observable for free
because both models already score the traffic. For any loss that depends on the input only
through the prediction, agreement forces identical losses, so the paired difference D vanishes
whenever A = 0 and

                     ∆ = E[D A],         |∆| ≤ B ρ,       ρ := P(A = 1),                    (1)

where B bounds the loss range. Identity (1) has two consequences that we develop into a
complete theory. First, if unlabeled traffic certifies that ρ ≤ ε/B, then |∆| ≤ ε is certified
with zero labels. Quantized builds, routine retrains, and hyperparameter touches typically
live in this regime, and in our experiments 98% of such benign updates certify label-free.
Second, when ρ is not negligible, all information about ∆ is concentrated on disagreements,
so an auditor should label only there. Figure 1 overviews the resulting protocol. We make
this precise with an importance-weighted estimator wrapped in an empirical-Bernstein
confidence sequence, and we prove it is not merely a good idea but a rate-optimal one. Its
label complexity matches an information-theoretic lower bound up to logarithmic factors,
and the gap to any pairing-blind procedure is exactly the disagreement rate itself.
    A scope note belongs up front. The support identity requires the loss to depend on the
input only through the prediction (Assumption 1), which holds for the standard supervised
losses and for the classification fine-tunes in our experiments, but excludes losses that read
model scores or a judge’s verdict, including calibration and preference or reward losses.
Our certified guarantees are for that prediction-determined class. A soft generalization to
score-reading losses that are Lipschitz in the model output, which reaches calibration and
smooth reward objectives, is developed in Section 5.6; open-ended judged generation remains
outside the theory and we do not claim it.
Contributions.
1. Problem formalization. We cast update promotion as certified paired risk-difference
   auditing with anytime-valid semantics (Section 3), an object distinct from single-model
   risk certification, two-sample testing, and offline evaluation. A soft support identity
   (Proposition 14) extends the whole protocol from prediction-determined losses to losses
   Lipschitz in the model output, such as calibration and smooth reward losses.

                                              2

[p.3]

                                               Pay Only for Disagreement




  FREE LANE        unlabeled traffic + compute. Agreements (share 1               , typically 80 99.9%) have Dt = 0 exactly, never labeled.

                           shadow scoring                                                 TIER 0 · zero-label certificate                 promote
   production                                             disagree?
     traffic                                                                     rate        confidence sequence on ,                      / hold
                            incumbent f(xt )                                                   unlabeled traffic only
                                                          At = 1{f g}                                                                     + evidence
     unlabeled                                                                            B t<       SAFE · 56% pay zero                    artifact
     stream xt              candidate g(xt )

                                                                    disagreements                                                         , , verdict,
                                                                                                                                        stopping time,
  PAID LANE        label only disagreements                                                                                              label ledger

        learned judge (optional)                      predictable routing                   TIER 1 · audited verdict                      re-derivable
                                                                                          anytime confidence sequence on                    by third
                                                      label w.p. t [ min , 1]                                                                parties
    prioritizes suspicious disagreements;
       cannot break validity (Thm. 5)                                                      upper <        SAFE
                                                      labeled: Dt / t , else 0                                                            EU AI Act
                                                                                           lower > 0      REGRESSION
                                                       (unbiased, Lem. 3)                                                                Art. 12 & 72
                                                                                          SAFE at median 327 vs 2,906 labels



  GUARANTEES: anytime-valid at every stopping time (Thm. 4) ·     ( 2 / 2 ) labels, matching lower bound (Thms. 7 8) · pairing saves (1/ ) labels (Cor. 10)




Figure 1: The Discern protocol, organized by what it spends. In the free lane, both
          models shadow-score unlabeled traffic and the disagreement indicator stream
          (both branches of the gate) drives a zero-label confidence sequence on ρ, and
          when Bρt < ε the update is certified safe without a single label (Tier 0). Only
          sampled disagreements enter the paid lane, through a predictable routing rule
          with importance-weighted increments, and an anytime-valid confidence sequence
          on ∆ issues the verdict (Tier 1). Every quantity shown is measured in Section 6.
          In brief, 56% of benign audits certify with zero labels, the audited band pays a
          median of 327 versus 2,906 labels for uniform labeling, and injected regressions
          alarm at a median of 964 stream points. The footer lists the paper’s formal
          guarantees.



2. The Discern protocol. A two-tier sequential audit (Section 4) with a zero-label certifi-
   cate from unlabeled disagreement monitoring, and an audited tier that labels sampled
   disagreements under any predictable routing rule, with per-slice simultaneous verdicts
   and family-wise soundness across a whole sequence of promotions (Proposition 13).
3. Validity theory. Time-uniform (1 − δ) coverage of the audited estimate at every data-
   dependent stopping time, for every predictable routing rule, judge-driven or adversarial
   (Theorem 4, Theorem 5).
                                                               e B 2 ρ2 /ε2 +Bρ/ε labels to
                                                                                 �
4. Matching label-complexity bounds. An upper bound of O
   an (ε, δ) verdict (Theorem 7) and a change-of-measure lower bound Ω(ρ2 ε−2 log(1/δ)) for
   any adaptive labeling-and-stopping procedure (Theorem 8), matching up to logarithmic

                                                                            3

[p.4]

                              Vishnu Bindu Balachandran




    factors. The paired comparison object goes back at least to Sawade et al. (2012), and
    certified update approval to Feng et al. (2021). What is new here, to our knowledge, is
    the characterization of the label cost of a certified update verdict as a function of the
    disagreement rate, with matching bounds.

 5. The value of pairing. Any procedure that cannot see the disagreement signal needs
    Ω(ρ ε−2 log(1/δ)) labels (Theorem 9), and uniform labeling achieves it. Pairing therefore
    buys a factor Θ(ρ), a compute-for-labels exchange in which running both models on
    unlabeled traffic, which is cheap, eliminates a 1/ρ multiple of human labeling, which is
    expensive.

 6. Large-scale validation. A pre-registered evaluation over 715 feature-space update
    pairs and 6,890 replayed audit streams across four feature modalities and eleven update
    types, plus 70 real LoRA fine-tune update pairs (140 further streams) of Pythia language
    models, with a held-out confirmation on a reserved seed family (Section 6). Empirical
    miscoverage is 0.0002 (nominal 5%), power is 0.986 with zero false alarms, and label
    spend follows the theoretical law with R2 = 0.999. Head-to-head comparisons against
    sequential adaptations of prediction-powered and active-testing baselines on identical
    streams (Section 6.4), and a windowed variant that repairs calibration under adversarial
    drift (Section 6.5), complete the empirical case.

Why this is the right target for a certified method. A certificate is only as valuable
as the decision it unlocks. The decision here is concrete and recurring, namely whether
to promote or hold an update. Regulation is converging on the same object. Article 72
of the EU AI Act requires providers of high-risk systems to run post-market monitoring
proportionate to the risk, and logging obligations under Article 12 require traceable evidence
for system changes. A Discern audit emits, per promotion, a machine-checkable tuple
(tolerance, confidence, verdict, label spend, stopping time, per-slice outcomes) that serves
directly as such evidence. No comparable finite-sample instrument exists in the update-
monitoring literature, which either assumes labeled evaluation sets, provides asymptotic or
heuristic monitoring, or certifies single-model properties rather than the paired difference
that the promotion decision actually consumes (Section 2).


2 Related Work
Paired comparison of classifiers. The observation that paired accuracy comparison
hinges on discordant pairs goes back to McNemar (1947), and sequential treatments of
two-sample testing are classical (Wald, 1945). Restricting adjudication to discordant pairs
to save labels recurs in fixed-sample model evaluation, where Musgrove et al. (2023) report
over a 90% reduction in adjudications, but under an assumed class prevalence and with
neither a sequential guarantee nor a lower bound. Our contribution is not the identity itself
but its consequences under modern constraints, namely anytime validity under continuous
monitoring, adaptive label routing with importance-weighting, matching label-complexity
bounds, and a zero-label tier. Recent resolution diagnostics for paired evaluation (Kotawala,
2026) quantify whether a fixed-n comparison has enough labeled points to resolve, but
assume the labels already exist. We optimize and certify the labeling process itself.

                                              4

[p.5]

                               Pay Only for Disagreement




Anytime-valid inference. Our confidence sequences build on time-uniform boundaries
from nonnegative-supermartingale arguments (Ville, 1939; Robbins, 1970), modern empirical-
Bernstein confidence sequences (Howard et al., 2021; Waudby-Smith and Ramdas, 2024),
and the game-theoretic testing programme (Ramdas et al., 2023). Betting-style audits have
been used for fairness properties of a fixed model (Chugg et al., 2023) and adaptive audits
of a single AI system with anytime-valid guarantees (Zhou et al., 2026). Sequential drift
attribution for LLM evaluation pipelines (Li, 2026) monitors a judged pipeline over time.
Closest in mechanism, Karampatziakis et al. (2021) build off-policy confidence sequences
with importance weights inside a betting martingale and apply them to gated deployment of
a contextual-bandit system, and Xu et al. (2024) construct anytime-valid risk-controlling
prediction sets under active labeling with a query budget. These share our core machinery,
Horvitz–Thompson weights within an anytime-valid betting confidence sequence under
adaptive querying. None of these anytime-valid audits target the paired update delta, none
exploit the disagreement support to drive a zero-label tier, and none characterize label
complexity or prove a matching lower bound. We use the confidence-sequence machinery as
a component and prove rate-matching complexity results for the promotion problem.

Model comparison and update approval. Two prior lines come closest to our object.
Sawade et al. (2012) compare the risks of two given models on a fixed labeling budget
by sampling test instances from a variance-optimal instrumental distribution, the paired
object with active, importance-weighted labeling. Their guarantee is an asymptotic normal-
approximation test at a fixed horizon. We add what deployment needs and what their
analysis does not provide, namely finite-sample anytime-valid verdicts, an explicit label-
complexity characterization with a matching lower bound, and a zero-label tier. Notably,
their optimal instrumental distribution already concentrates on informative points, and our
Theorem 8 can be read as the information-theoretic reason why. Separately, Feng et al. (2021)
and Feng (2021) study approval policies for modifications to deployed ML systems as an
online hypothesis testing problem with error control across a sequence of approvals, including
the bio-creep phenomenon. That line certifies sequences of approvals on labeled test batches.
We certify each promotion from unlabeled traffic at optimal label cost, our audits compose
across a sequence of promotions with family-wise control of bio-creep (Proposition 13), and
their alpha-investing refinement ports directly. Podkopaev and Ramdas (2022) track the
risk of a single deployed model with anytime-valid guarantees, and Shanmugam et al. (2025)
estimate metrics for multiple models from labeled and unlabeled data without certified
verdicts. Neither targets the paired promotion decision. Concurrent with this work, Shawn
(2026) propose a McNemar-style anytime-valid commit gate for self-evolving agents, using
a testing-by-betting e-process on paired instances to control the false-commit rate. That
design shares our anytime-valid, paired, evidence-on-disagreements structure, and reaches
similar conclusions about uncontrolled greedy acceptance, but provides neither a zero-label
certificate, nor a label-complexity characterization, nor a matching lower bound, which are
the central objects here.

Label-efficient evaluation. Active testing and model-assisted evaluation reduce labels
for estimating a single model’s risk (Kossen et al., 2021; Angelopoulos et al., 2023a), with
sequential and active variants of two-sample testing in Li et al. (2024, 2025). Prediction-
powered and surrogate-based estimators use model outputs to sharpen single-quantity

                                              5

[p.6]

                               Vishnu Bindu Balachandran




inference (Angelopoulos et al., 2023a; Zrnic and Candès, 2024), and Boyeau et al. (2025)
apply prediction-powered inference to pairwise model comparison from synthetic labels.
These are fixed-horizon estimators of a metric, not certified anytime-valid promotion verdicts,
and none provides a label-complexity lower bound. The estimand differs in a way that
changes the complexity theory. For the paired difference, an observable signal (disagreement)
supports the entire estimand, which makes the optimal label complexity quadratic rather
than linear in ρ and creates the Θ(ρ) separation we prove. Cross-model disagreement has been
proposed as a label-free correctness heuristic (Gorbett and Jana, 2026) and disagreement-
aware aggregate evaluation appears in Bonagiri et al. (2026). These works use disagreement
as a signal for prediction quality, not as the support of a certified estimand, and provide no
finite-sample guarantees.

Disagreement-based active learning. The principle that labels are informative only
where competing hypotheses disagree is the foundation of disagreement-based active learning,
from the query-by-disagreement of Cohn et al. (1994) to the agnostic A2 algorithm of Balcan
et al. (2009) and its analysis through Hanneke’s disagreement coefficient (Hanneke, 2007,
2014). That theory bounds the labels needed to learn a low-error classifier by the rate
at which the disagreement region of a shrinking version space contracts around the target
hypothesis. Our problem differs in both object and mathematics. We learn no classifier and
maintain no version space. We hold two fixed given models and certify a scalar functional, the
paired risk difference, with an anytime-valid guarantee. The disagreement region is fixed at
the observable rate ρ rather than shrinking with a disagreement coefficient, and our tolerance
ε bounds a risk difference rather than the excess error of a learned hypothesis. Consequently
     e 2 /ε2 ) characterization is a mean-estimation and sequential-testing complexity for a
our Θ(ρ
functional, proved by a change-of-measure construction (Theorem 8), not a version-space
label-complexity bound, and neither result subsumes the other. What the two share is the
operational core we take as our starting point, that information concentrates on disagreements.
The bound |∆| ≤ Bρ of Lemma 2 is elementary and is the evaluation-side counterpart of the
classical disagreement-region bound. The idea of using model disagreement on unlabeled
data to validate and compare classifiers is older still, going back to the co-validation of
Madani et al. (2004), who showed that disagreement lower-bounds error and can compare
models without labels, and to the unlabeled-data generalization bounds of Kääriäinen (2005),
which bound a risk gap by an unlabeled disagreement probability. Concurrent work of
Bazinet et al. (2026) likewise certifies the gap between two predictors’ risks by evaluating a
disagreement bound on unlabeled data, for static generalization certificates rather than a
sequential update verdict. Our contribution is not this bound but its sequential certification,
the zero-label tier it enables, and the matching two-sided label-complexity theory built
around it.

Update churn and backward compatibility. The applied literature documents the
operational pain of updates, from prediction churn between successive models (Milani Fard
et al., 2016) to negative flips and backward-compatibility metrics (Yan et al., 2021) and
regression testing practice for ML systems (Srivastava et al., 2020). These works measure or
reduce disagreement. We complete the pipeline. Given that updates disagree, we certify, at
optimal label cost, whether the disagreement hurts.

                                              6

[p.7]

                               Pay Only for Disagreement




Model multiplicity. Predictive multiplicity (Marx et al., 2020; Black et al., 2022) studies
distinct models with similar average risk. The disagreement region between near-equivalent
models is exactly where our audits concentrate, and multiplicity explains why the benign-
update regime (∆ ≈ 0, ρ moderate) is common and why certifying it cheaply matters.

3 Setting and the Support Identity
Let (Xt , Yt )t≥1 be an i.i.d. stream from an unknown distribution P over X × Y (drift is
treated in Section 5.7). An incumbent model f and a candidate g map X to a prediction
space A, and a loss ℓ : A × Y → [0, B] scores predictions. Define the paired difference and
its mean                           �              �
                 Dt = ℓ g(Xt ), Yt − ℓ f (Xt ), Yt ∈ [−B, B],   ∆ = E[Dt ],              (2)
so ∆ > 0 means the candidate is worse (a regression) and ∆ ≤ 0 means it is no worse. For
0/1 loss, ∆ is the accuracy drop and B = 1. The auditor observes both predictions on
every point for free, hence also the disagreement indicator At = 1{f (Xt ) ̸= g(Xt )} with rate
ρ = P(At = 1), and may request the label Yt at unit cost.

Assumption 1 (Prediction-determined loss) The loss is a function of the prediction
and label alone, ℓ(a, y), with no other dependence on the input. Its operative content is that
whenever the two models make the same prediction, f (Xt ) = g(Xt ), they incur the same
loss, so Dt = 0.

    Assumption 1 holds for every standard supervised loss (0/1, cost-sensitive misclassifi-
cation, top-k, bounded regression losses on point predictions, exact-match and slot-level
scores for structured prediction). It fails only when the loss consults model internals, for
example calibration losses on confidence scores. Every guarantee in this paper is for this
deterministic-prediction class. Judged and preference-based losses, including chat-quality
and RLHF objectives, are outside it, and our language-model experiments are classification
fine-tunes that satisfy Assumption 1 (Section 6.1). We discuss the extension in Section 8.

Lemma 2 (Support identity) Under Assumption 1, ∆ = E[Dt At ] and |∆| ≤ Bρ1 ≤ Bρ,
where ρ1 = P(Dt ̸= 0).

Proof Dt = Dt At pointwise since At = 0 forces Dt = 0. Take expectations, then bound
|Dt | ≤ B on the event {Dt ̸= 0} ⊆ {At = 1}.


    The identity is elementary, and the bound |∆| ≤ Bρ is the evaluation-side form of the
disagreement-region principle that underlies disagreement-based active learning (Hanneke,
2014). What is not classical, and what the rest of the paper develops, is its sequential
certification from unlabeled traffic and the matching label-complexity theory it implies
(Section 2 contrasts the two settings). The refinement through ρ1 matters in multiclass
problems where both models can disagree yet both be wrong, contributing At = 1 but
Dt = 0. All upper bounds below can be read with ρ1 in place of ρ wherever variance is
concerned. We state them with ρ for simplicity since ρ1 ≤ ρ and only ρ is observable without
labels.

                                              7

[p.8]

                                Vishnu Bindu Balachandran




Verdicts. Fix a tolerance ε ∈ (0, B) and confidence level δ ∈ (0, 1). At any data-dependent
time the auditor may issue one of two verdicts.
  • Safe(ε), which asserts ∆ < ε (promote the update).
  • Regression, which asserts ∆ > 0 (block or roll back).
Safe(ε) is a tolerance statement in the spirit of noninferiority testing. It asserts ∆ < ε rather
than ∆ ≤ 0, and we use no-regression in this ε-tolerance sense throughout. A procedure
is (ε, δ)-sound if, with probability at least 1 − δ, no false verdict is ever issued at any time.
Soundness at every stopping time is not optional in deployment, because promotion pipelines
poll the audit continuously and act the moment a verdict fires, which is precisely the regime
in which fixed-n tests lose their guarantees (Ramdas et al., 2023).

4 The Discern Protocol
Discern (DISagreement-supported CERtificatioN)1 runs two tiers on the same stream.
Both tiers are driven by confidence sequences (CSs), which are sequences of intervals Ct
with P(∃t : θ ∈/ Ct ) ≤ δ for the target parameter θ (Howard et al., 2021). We use the
predictable-plug-in empirical-Bernstein CS of Waudby-Smith and Ramdas (2024), whose
radius adapts to the empirical variance of the increments. Its exact form is recalled in
Appendix A.

4.1 Tier 0, the zero-label certificate
The indicator stream (At ) is observed without labels. Maintain a CS [ ρt , ρt ] for ρ at level
δ0 . By Lemma 2, on the CS’s coverage event,

                                  B ρt < ε      =⇒     |∆| < ε,                                   (3)

so the auditor issues Safe(ε) having requested zero labels. The firing threshold is the
strict inequality Bρt < ε precisely so the certificate implies the strict claim ∆ < ε that
Safe(ε) asserts, with no slippage at the boundary ∆ = ε. Tier 0 certifies exactly the
updates that dominate production practice, namely quantized builds, retrains that converge
to near-identical decisions, and small  � hyperparameter changes. When ρ ≤ ε/(2B), the
certificate fires after O B log(1/δ0 )/ε unlabeled points (Proposition 6). The constant B is
a design quantity rather than an estimate. For 0/1 and other normalized losses B = 1 by
construction, and for cost-sensitive losses it is the known maximum cost. The certificate
uses only the one-sided bound ∆ ≤ Bρ, and overestimating B degrades it linearly, since the
certificate fires once ρt < ε/B.

4.2 Tier 1, auditing the disagreement region
When Tier 0 cannot fire, information must be bought, and Lemma 2 says to buy it only on
disagreements. At each point with At = 1 the auditor requests the label with probability
πt , a predictable routing rule. It may depend on everything observed before t and on side
information about Xt itself, including scores from a learned judge model, subject only to
1. The name is unrelated to the DISCERN instrument for appraising written consumer health information
   (Charnock et al., 1999).


                                                 8

[p.9]

                                Pay Only for Disagreement




πt ∈ [πmin , 1]. Routing may never consult the incoming label Yt . This is the independence
condition of Lemma 3, and it is the one deployment requirement. It is a genuine assumption,
not a formality. A pipeline that decides to label a point because the outcome already looked
bad, for example queuing an example for review after a user complaint, makes Lt depend
on Yt and biases the Horvitz–Thompson estimator, voiding the guarantee. The safeguard
is operational and simple, namely that the routing rule must be a function of pre-label
information only (Ft−1 and Xt , including judge scores), with the label drawn only after
the query decision is fixed. Under that discipline the condition holds by construction. Let
Lt ∼ Bern(πt ) be the labeling indicator. The importance-weighted (Horvitz–Thompson)
increment
                                  Lt
                         Zt = At     Dt ∈ [−c, c],       c := B/πmin ,                    (4)
                                  πt
satisfies E[Zt | Ft−1 ] = ∆ (Lemma 3). Discern maintains the empirical-Bernstein CS
[ ∆t , ∆t ] for ∆ at level δ1 over the increments Zt (agreements contribute exact zeros and
consume no labels) and issues

                   Safe(ε) when ∆t < ε,          Regression when ∆t > 0.

Setting δ0 + δ1 = δ makes the combined procedure (ε, δ)-sound (Theorem 4). Three design
points deserve emphasis.
Judges accelerate, never invalidate. A learned judge (an auxiliary model scoring
which disagreements look suspicious) can drive πt to concentrate labels where regressions
would show. Because validity requires only predictability and the floor πmin , a judge that is
stale, biased, or adversarial can waste budget but cannot break coverage (Theorem 5). This
resolves the central tension of LLM-as-judge evaluation. The judge is used for efficiency, the
guarantee never depends on its quality.
Per-slice verdicts. Promotion decisions are rarely global. Partition traffic into K slices
(regions, languages, document types) and run one CS per slice with budget δ1 /K. Union
coverage gives simultaneous validity of all K verdicts (Proposition 12), enabling verdicts of
the form “safe overall, regressing on slice k” with localization guarantees.
Compute cost. Discern runs both models on audited traffic. This shadow-scoring cost
is standard in deployment (canary and shadow testing already do it) and is the resource
the protocol deliberately trades against labels: Theorem 9 shows the trade buys a 1/ρ label
reduction.

5 Theory
Throughout, Lδ := log(2/δ1 ) and O(·)
                                 e hides factors polylogarithmic in t, 1/ε, and log(1/δ).
Proofs are in Appendix B.

5.1 Validity
Lemma 3 (Conditional unbiasedness) Let πt be Ft−1 ∨ σ(Xt )-measurable with πt ≥
πmin > 0, and let Lt | Ft−1 , Xt , Yt ∼ Bern(πt ) be drawn independently of Yt given (Ft−1 , Xt ).
Then the increment (4) satisfies E[Zt | Ft−1 ] = ∆ and |Zt | ≤ B/πmin .

                                                9

[p.10]

                                Vishnu Bindu Balachandran




Theorem 4 (Anytime validity) Run Tier 0 at level δ0 and Tier 1 at level δ1 with any
predictable routing πt ∈ [πmin , 1]. Then with probability at least 1 − (δ0 + δ1 ), simultaneously
for all t ≥ 1: ρ ∈ [ρt , ρt ] and ∆ ∈ [∆t , ∆t ]. Consequently no false Safe(ε) or Regression
verdict is ever issued, at any stopping time, under continuous monitoring.

Theorem 5 (Routing robustness) The conclusion of Theorem 4 holds for every pre-
dictable routing rule, including rules computed from an arbitrary (possibly adversarially
wrong) judge model. Routing affects only the label budget and the certification time, never
coverage.

5.2 Label-complexity upper bounds
Proposition 6 (Tier-0 certification � time) If Bρ ≤ ε/2, Tier 0 issues Safe(ε) after at
most O (B/ε) log(1/δ0 ) log log(B/ε) unlabeled points, with zero labels.

Theorem 7 (Labels to a verdict) Let πt ≡ π ∈ [πmin , 1] and suppose the update is ε-
benign, ∆ ≤ ε/2. With probability at least 1 − 2δ1 , Tier 1 issues Safe(ε) by stream time
                                     � 2
                                    e B ρ Lδ + B Lδ ,
                                                     �
                               T⋆ = O
                                      π ε2    πmin ε
and the number of labels requested satisfies
                                    � 2 2
                                   e B ρ Lδ + π · Bρ Lδ .
                                                       �
                            Nlab = O
                                      ε2     πmin ε
Symmetrically, if ∆ ≥ 2ε a Regression verdict fires within the same bounds with ε replaced
by ∆.

   The first term is the variance regime and dominates when ρ ≳ ε/B, the second is the
range regime of the empirical-Bernstein boundary and dominates for small ρ. Combined
with Tier 0, which removes the regime ρ ≤ ε/(2B) entirely, the audited tier is only ever
                                                                    e 2 ρ2 Lδ /ε2 ).
invoked where the quadratic term is active, and total label cost is O(B
   The same argument applied to the uniform-labeling baseline (label every point, run the
same variance-adaptive CS on the raw increments Dt , whose variance is at most B 2 ρ1 ) gives
the baseline cost                        � 2
                                        e B ρ Lδ + B Lδ ,
                                                          �
                                unif
                              Nlab   = O                                                  (5)
                                            ε2       ε
                                           unif = Θ(ρ ∨ ε/B), and the auditor pays only the
so the predicted savings ratio is Nlab /Nlab
disagreement fraction of the uniform bill. Our experiments confirm both the individual rates
and the ratio (Section 6.3).

5.3 Matching label-complexity lower bounds
The next results show the protocol is not merely efficient but optimal, and quantify exactly
what the pairing signal is worth. Proofs use a change-of-measure argument for adaptively
stopped, adaptively routed procedures in the style of sequential identification lower bounds
(Kaufmann et al., 2016), with a two-world construction in which unlabeled observations

                                               10

[p.11]

                                Pay Only for Disagreement




are common to both worlds and only labeled disagreements carry information. The change-
of-measure machinery is standard, and the two-atom construction is related to noise-rate
lower bounds in active learning (Hanneke, 2014). What is new is not the technique but the
object it is applied to, a paired risk difference whose signal lives on an observable measure-ρ
support, which is what produces the ρ-dependence and, against a pairing-blind auditor, the
Θ(1/ρ) separation. The construction does not reduce to substituting ρ for a noise rate in an
existing bound, because the two worlds must share their entire unlabeled stream, including
the disagreement pattern, and differ only in the labels on disagreements.

Theorem 8 (Lower bound for adaptive auditors) Fix B = 1, ε ∈ (0, 18 ], and ρ ∈
[2ε, 21 ]. There exist distributions P0 , P1 , both with disagreement rate ρ, with ∆(P0 ) = 0 and
∆(P1 ) = ε, whose unlabeled streams (Xt , f (Xt ), g(Xt )) are identically distributed, such that
any (ε, δ)-sound procedure that issues Safe(ε) with probability at least 1 − δ under P0 must
request
                                                      ρ2        1
                                    EP0 [Nlab ] ≥         log
                                                     4 ε2     2.4 δ
labels, regardless of how adaptively it routes labels or stops.

    Together with Theorem 7, the label complexity of certified update auditing is settled
at Θ(ρ2 /ε2 ) in the audited regime ρ ≥ 2ε, and at zero labels in the Tier-0 regime ρ ≤ ε/2.
   e
The intermediate window ρ ∈ (ε/2, 2ε) is not a gap in the characterization but the regime
where the rate itself is constant. There ρ ≍ ε, so the upper bound O(ρ  e 2 /ε2 + ρ/ε) and
the lower bound Ω(ρ2 /ε2 ) are both Θ(1),
                                      e     matching up to a constant and log factors like
everywhere else. What is unpinned in the band is only the exact constant, which is standard
for change-of-measure bounds and does not affect the rate.

Theorem 9 (Lower bound for pairing-blind auditors) In the setting of Theorem 8,
call a procedure pairing-blind if it does not evaluate the model pair on unlabeled points. Its
labeling decisions and verdict are measurable with respect to its own past labeled outcomes
alone. This class prices exactly the standard practice of labeling sampled traffic without
shadow-scoring it. Any (ε, δ)-sound pairing-blind procedure must request
                                                 ρ         1
                                   E[Nlab ] ≥        log
                                                4 ε2     2.4 δ
labels. Uniform labeling with an empirical-Bernstein CS achieves this rate up to logarithmic
factors.

Corollary 10 (The value of pairing) In the regime ρ ≥ 2ε, the ratio of optimal pairing-
blind to optimal pairing-aware label complexity is Θ(1/ρ). Observing both models’ predictions
on unlabeled traffic, a pure compute cost, cuts the human labeling bill by the inverse disagree-
ment rate.

    Corollary 10 is the paper’s economic statement. At the disagreement rates of real update
pairs, whose medians run from below 10−3 to 0.15 across update types (Table 1) and reach
0.45 on individual pairs, the factor ranges from a few-fold at the high-ρ end to beyond 1000×
when ρ is small.

                                                11

[p.12]

                               Vishnu Bindu Balachandran




Remark 11 (What the pairing-blind class prices) The separation prices exactly one
capability, observing the pair’s agreement on unlabeled traffic. An auditor granted the
disagreement indicators At on unlabeled points is by definition not pairing-blind. It can
restrict labeling to disagreements and attain the pairing-aware rate of Theorem 7. The
class of Theorem 9 is therefore not a tailored weakening but the natural dichotomy between
auditors that shadow-score all traffic and those that label sampled traffic without doing so,
the latter being standard when running both models on the full stream is not instrumented.
The Θ(1/ρ) gap is the operational value of that instrumentation, a compute cost, measured
in the labels, a human cost, that it saves. The gap does not survive granting the blind auditor
the disagreement signal, and that is the point. The signal is precisely what pairing is.

5.4 Per-slice certification
Proposition 12 (Simultaneous slice verdicts) Partition X into slices S1 , . . . , SK and
run the Tier-1 CS on slice k at level δ1 /K for the slice difference ∆k = E[D | X ∈ Sk ]. Then
with probability at least 1 − δ1 all K CSs cover simultaneously for all time, so every per-slice
Safe and Regression verdict is simultaneously sound, and any slice with ∆k ≥ 2εk is
alarmed within the slice-local bound of Theorem 7 applied to its own traffic share.

5.5 Sequences of promotions
Deployed systems are not updated once. A promoted candidate becomes the next incumbent,
a new candidate arrives, and the sequence of approvals carries its own risk, the bio-creep
phenomenon of Feng et al. (2021) in which repeated tolerant approvals let quality drift
downward. Our audits compose across such a sequence at no additional modeling cost.

Proposition 13 (Sequence-level soundness) Let updates arrive as a possibly adaptive
sequence, where the k-th incumbent-candidate pair and audit configuration may depend
                                                                                  (k) (k)
on all earlier data and verdicts. Run audit k on fresh traffic at levels (δ0 , δ1 ) with
P        (k)    (k) �
   k≥1 δ0 + δ1        ≤ δseq . Then with probability at least 1 − δseq , no audit in the entire
sequence ever issues a false verdict. In particular the number of regressing updates that are
ever certified Safe at their stated tolerances is zero with probability at least 1 − δseq .

     With the schedule δ (k) ∝ k −2 the guarantee covers an unbounded stream of future
updates from a single constant budget, and with an equal split it covers a known horizon.
Each successive audit is more expensive by only a log(1/δ (k) ) factor (Theorem 7), so the price
of lifetime soundness is logarithmic in the update index. The alpha-investing refinement of
Feng et al. (2021), which grows the error budget after good outcomes, ports directly and can
improve power, but the union schedule already rules out bio-creep in the family-wise sense.
     Two measurability points make the argument precise. First, the k-th audit may be
chosen fully adaptively, because its configuration is Hk -measurable and Theorem 4 is
applied conditionally on Hk ; adaptivity of the promotion policy costs nothing. Second,
the proposition runs each audit on fresh traffic, which is what lets audit k’s increments be
conditionally valid given Hk . If instead P
                                          audits share or overlap traffic, family-wise soundness
still holds, since the union bound over k δ (k) needs no independence between audits, and
only the label-efficiency of concurrent audits degrades, not their validity.

                                              12

[p.13]

                                  Pay Only for Disagreement




5.6 Beyond prediction-determined losses
Assumption 1 makes disagreement a hard indicator. When the loss reads the model’s
continuous output, a score or a logit, rather than only the discrete prediction, agreement
of predictions no longer forces Dt = 0, and the hard support identity fails. A soft version
survives whenever the loss is Lipschitz in the model output, which covers calibration losses,
smooth surrogate losses, and reward losses that are Lipschitz in a scalar score.

Proposition 14 (Soft support identity) Let sf (X), sg (X) be the incumbent and can-
didate outputs in a normed space, and suppose ℓ(·, y) is L-Lipschitz in its first argument
uniformly in y, so |ℓ(a, y) − ℓ(a′ , y)| ≤ L ∥a − a′ ∥. Define the observable soft disagreement
ηt = ∥sg (Xt ) − sf (Xt )∥, computable without labels. Then

                              |Dt | ≤ L ηt    a.s.,     |∆| ≤ L E[ηt ],

and Dt = 0 wherever ηt = 0. Consequently, running the confidence sequence of Appendix A
on the unlabeled stream (ηt ) with upper endpoint η t , the strict trigger L η t < ε certifies
|∆| < ε with zero labels; and the importance-weighted audited tier of Section 4.2, restricted
to {ηt > 0}, is anytime-valid with conditional second� moment E[Zt2 | Ft−1 ] ≤ L2 E[ηt2 ]/πmin ,
                           e L2 E[ηt2 ]ε−2 + L E[ηt ]ε−1 labels.
so an (ε, δ) verdict costs O

Proof Lipschitzness gives |Dt | = |ℓ(sg (Xt ), Yt ) − ℓ(sf (Xt ), Yt )| ≤ L∥sg (Xt ) − sf (Xt )∥ = Lηt ;
take expectations for the bound on |∆|, and ηt = 0 forces sf (Xt ) = sg (Xt ) hence Dt = 0.
On the CS coverage event E[ηt ] ≤ η t , so |∆| ≤ LE[ηt ] ≤ Lη t < ε. Unbiasedness and
time-uniform validity of the audited tier are Lemma 3 and Theorem 4 verbatim, since only
predictability of the routing is used; the second-moment bound follows from |Dt | ≤ Lηt and
E[Lt | Ft−1 , Xt ] = πt , and the label count is then the width lemma applied with L2 E[ηt2 ] in
place of B 2 ρ.


    The prediction-determined case is the special instance ηt = At , L = B, which recovers
|∆| ≤ Bρ and the hard protocol. The soft identity thus extends the zero-label certificate
and the audited tier to score-reading losses at the price of replacing the disagreement rate ρ
by the soft-disagreement moments E[ηt ] and E[ηt2 ]. Matching the lower bound in this soft
regime, and handling open-ended judged generation where the output is discrete text rather
than a Lipschitz score, are left open.

5.7 Beyond stationarity
Under distribution shift there is no fixed ∆ to certify. Two honest statements are available.
First, the predictable-plug-in P
                               CS remains a valid CS      P for the running weighted average of
the conditional means ∆  et =
                                  i≤t λi E[Z i | F i−1 ]/  i≤t λi (Waudby-Smith and Ramdas,
2024), so verdicts can be read as statements about traffic-averaged regression over the audit
window. Second, for operators who need current-regime verdicts, Discern restarts the CS
on a sliding window, trading a log factor for freshness. We report both sides empirically.
The unrestarted CS under two aggressive synthetic drift schedules miscovers a moving
running-average target (6.4% under smooth drift, 15.9% under adversarial bursts, Table 2),
and the windowed variant repairs it on paired same-seed streams (0.0001 and 0.065 against

                                                  13

[p.14]

                               Vishnu Bindu Balachandran




0.063 and 0.156 unrestarted, Section 6.5). We flag the unrestarted numbers openly because
silent miscoverage under drift is precisely the failure mode a certified tool must not hide.

6 Experiments
Our evaluation was pre-registered. Gates on validity, label efficiency, zero-label coverage,
and power were frozen, with pass thresholds, before the main campaign ran, and a disjoint
confirmation seed family was reserved untouched until the final replication run (Appendix C).
All experiments replay real model pairs against real feature streams. Code, per-stream
records (14,233 stream-level JSON artifacts, Table 6), and one-command reproduction scripts
will be released publicly upon publication and are available to reviewers on request during
review (Appendix F).

6.1 Update-pair zoo
Feature-space pairs. We build 715 update pairs across 13 settings spanning four modali-
ties: RoBERTa text features (SST-2 sentiment), LayoutLMv3 document features (the public
Tobacco-3482 corpus and an internal financial-documents classification corpus, the latter not
part of the public release; the document modality is anchored by the public Tobacco-3482
so no conclusion rests on the internal set), supervised vision features (ResNet-18 and ViT
on CIFAR-10/100), and foundation-model features (DINOv2 and CLIP). In each setting a
labeled audit pool (25% of the data, disjoint from all fitting) provides exact ground truth
∆ and ρ for every pair, which is what makes measuring true miscoverage possible at this
scale. The incumbent is a classifier head trained on the remaining data. Eleven update
types produce the candidate, chosen so that the disagreement rate and the true harm vary
independently across the zoo (Table 1). Seven are benign, with true risk difference essentially
zero (retrain with a new seed and data order, a 90% subsample retrain, a 4× regularization
change, int8 and int4 weight quantization, a refit on noised features, and a head refit on
65% of feature dimensions), and they span the disagreement range from ρ ≈ 0 to ρ ≈ 0.003.
Four are genuine regressions (∆ > 0), namely retrains on labels corrupted at 10% and
at 30% uniformly, a targeted 40% corruption on a fifth of the classes, and an aggressive
rank-halving of the head weights. The rank-halving is the instructive case. It is an efficiency
change of the same family as quantization, the kind an engineer might assume is safe, yet
unlike int8 and int4 quantization (median ∆ ≈ 0) it degrades accuracy by a median of 14
points, and Discern alarms on it. Disagreement rate alone does not order updates by
harm, which is exactly why the promotion decision certifies ∆ rather than reading off ρ.
Five exploratory seeds per cell yield the 715 pairs, and each pair is replayed under several
independent streams. The 6,890 main-battery audits decompose as 4,290 validity streams
(715 pairs times six routings, five i.i.d. and one adversarially routed), 1,430 drift streams
(715 times two schedules, smooth mixture and adversarial burst), and 1,170 mechanism
streams (455 tier-0 timing runs on the benign types and 715 label-allocation ablations).
Table 6 itemizes these totals alongside the pilot, confirmation, slice, and baseline campaigns.

Language-model pairs. To confirm the protocol end to end on real update processes
rather than head refits, we additionally fine-tune four Pythia backbones from 160M to
1.4B parameters (Biderman et al., 2023) with LoRA adapters (Hu et al., 2022) on SST-2

                                              14

[p.15]

                              Pay Only for Disagreement




             Regime               Update type             Median ρ   Median ∆
                                  retrain (new seed)       0.0000      0.0000
                                  int8 quantization        0.0000      0.0000
                                  hyperparameter change    0.0000      0.0000
             Benign (∆ ≈ 0)       feature-noise refit      0.0004      0.0000
                                  data refresh (90%)       0.0005      0.0000
                                  int4 quantization        0.0005      0.0000
                                  feature-subset refit     0.0026      0.0000
                                  10% label corruption     0.0051      0.0005
                                  30% label corruption     0.0152      0.0084
             Regression (∆ > 0)
                                  targeted corruption      0.0184      0.0088
                                  rank reduction           0.1508      0.1414

Table 1: Anatomy of the update zoo. Median disagreement rate and median true risk
         difference by update type across 13 settings and 5 seeds (65 pairs, each replayed
         as 3 i.i.d. streams, so n = 195 audits per type), placed by ground-truth harm.
         Realistic benign updates cluster at ρ near zero, exactly the regime Tier 0 certifies
         for free, while their true harm is zero throughout. The regressions show that ρ
         does not order updates by harm. Rank halving disagrees at ρ = 0.15 and truly
         degrades accuracy (∆ = 0.14), whereas the milder label corruptions disagree far
         less and carry a spectrum of harm, much of it below the tolerance at their median.
         Feature-noise refits have median ρ near zero but range up to 0.05 in the foundation-
         feature settings. Detection is measured (Table 2) on the injected regressions with
         ∆ ≥ 0.02, the subset a promotion gate must catch.



(Socher et al., 2013) and AG News (Zhang et al., 2015), building 70 update pairs of five
types (seed refresh, data refresh, int8 quantization of the adapter, and two corruption
strengths). Ground truth comes from held-out labeled evaluation splits. These pairs exhibit
the larger training variance of real fine-tuning (ρ up to 0.31), precisely the stress test a
promotion auditor faces. The engine behaves identically across scales. On the 30 pairs built
on billion-parameter backbones (1B and 1.4B, 60 streams) miscoverage is 0.017, power 0.92,
and false alarms 0. Int8 adapter quantization certifies with a median of 4 labels at every
scale, and the same Tier-0/audit/alarm split holds.

6.2 Validity, power, and false alarms

Table 2 summarizes (Figure 2 shows the validity picture at a glance). Across 4,290 i.i.d.
and adversarially routed streams in the main battery the time-uniform CS excluded the
truth on one stream, an empirical miscoverage of 0.0002 against the nominal 5% budget,
and the guarantee holds with a wide margin, as supermartingale boundaries are conservative
at finite horizons. The same margin means the boundary constants sit well above the
information-theoretic ones, so our optimality claims are at the rate level, and measured
label counts should be read accordingly. Injected regressions with ∆ ≥ 2% are alarmed with
power 0.986 (651 of 660 injected streams) within 5,000 points (at the primary tolerance

                                             15

[p.16]

                                         Vishnu Bindu Balachandran




    Campaign                                                     Streams        Miscoverage               Power      False alarms
    Pre-registered pilot (frozen gates)                           2,352              0.0021                1.000           0
    Main battery (i.i.d. and adversarial)                         4,290              0.0002                0.986      0 of 2,406
    Held-out confirmation (reserved seeds)                        2,145              0.0009                0.970           0
    LLM pairs, 160M–410M (LoRA)                                     80               0.0250                0.923           0
    LLM pairs, 1B–1.4B (LoRA)                                       60               0.0167                0.917           0
    Drift, smooth mixture (reported)                               715                   0.064                   –        –
    Drift, adversarial bursts (reported)                           715                   0.159                   –        –

Table 2: Validity and detection across all campaigns. Miscoverage is the fraction of streams
         on which the 95% CS ever excluded the true ∆ at any of up to 60,000 time steps
         (time-uniform, so nominal is 5% for the whole trajectory). Power is the fraction
         of injected regressions with ∆ ≥ 0.02 alarmed within 5,000 stream points. False
         alarms count Regression verdicts on truly benign pairs (∆ ≤ 0). Drift rows
         evaluate the unrestarted CS against a running-average target outside its guarantee,
         quantifying Section 5.7.



                                                                                0.0021
                Pre-registered pilot (n=2,352)
                                                        0.0002
                      Main battery (n=4,290)
                                                                       0.0009
             Held-out confirmation (n=2,145)
                                                                                                            0.025
              LLM pairs 160M--410M (n=80)
                                                                                                        0.0167
                 LLM pairs 1B--1.4B (n=60)
                                                                                                    nominal = 5%
                                                 10 4                   10 3                     10 2
                                                                 time-uniform miscoverage (log scale)


Figure 2: Time-uniform miscoverage of the 95% confidence sequence in every campaign,
          against the nominal budget (red line, log scale). Each dot is the fraction of that
          campaign’s streams on which the CS ever excluded the true ∆ at any time step.
          Every campaign, including both real-LLM zoos, sits below budget, most by one
          to two orders of magnitude.



ε = 1%, median alarm time 964 points, 90th percentile 2,945), and every one of the 9 misses
sits within a factor 1.7 of the tolerance boundary (∆ ∈ [0.020, 0.033]). No benign pair
was ever alarmed in the 2,406 opportunities, that is, the main-battery streams whose true
delta is ∆ ≤ 0 (the remaining 1,884 of the 4,290 have ∆ > 0 and so are not false-alarm
opportunities). The held-out confirmation, run once on the reserved seed family after all
development froze, reproduces every number. Figure 3 shows every language-model pair,
and verdicts track the true delta across all four backbone scales. On the 40 smaller-scale
LoRA pairs the engine behaves identically. Quantized adapters certify with a median of
24 labels, seed and data refreshes with genuinely positive ∆ (real fine-tuning variance) are

                                                                  16

[p.17]

                                                 Pay Only for Disagreement




                             0.25
                                          certified safe
                             0.20         alarmed
                                          inconclusive
         true update delta   0.15
                             0.10
                             0.05
                                                                                       power threshold = 2%
                             0.00
                             0.05
                                                                      160M     410M         1B         1.4B
                             0.10
                                    0.0           0.1      0.2          0.3      0.4             0.5
                                                           disagreement rate

Figure 3: Every language-model update pair (70 LoRA fine-tune pairs, 160M to 1.4B
          parameters) by its true disagreement rate and true delta, colored by the audit’s
          verdict. Alarms (red) and safety certificates (blue) separate along the true-delta
          axis, not the scale axis. Red points below the dashed power threshold are still
          correct alarms (their ∆ > 0), the guarantee simply does not promise them. One
          audit was inconclusive at its stream cap.



correctly alarmed rather than certified, and strong corruptions alarm in all 14 of 16 streams
whose true ∆ exceeded the tolerance (the remaining two sat below it).

6.3 Label efficiency and the two-tier ledger
The label ledger splits cleanly into the two tiers the theory predicts.
Tier 0 does most of the work for free. Three numbers measure the zero-label regime,
at stated tolerances and denominators. At ε = 1%, 56% of all 1,672 benign certifiable audits
finish with exactly zero labels, and the 1,509 audits with ρ ≤ 1% certify with a median
of zero labels. In the pre-registered pilot at ε = 2%, 98.2% of benign pairs obtained a
zero-label certificate within 20,000 unlabeled points. This is the deployment headline. The
most common real updates (quantization, routine retrains, hyperparameter changes) can be
promoted with a certificate and no labeling campaign at all.
The audited tier pays the predicted price. The 163 benign audits with ρ above the
Tier-0 regime certify at a median of 327 labels against 2,906 for uniform labeling with the
same CS machinery. Computed within each audit and then aggregated, the per-audit label
ratio has median 0.137 (quartiles 0.079 to 0.212); the ratio of the two marginal medians,
327/2,906 = 0.113, is slightly smaller because the two medians fall on different pairs. Either
way the saving is a factor of seven to nine, consistent with the Θ(ρ ∨ ε) ratio of Theorem 7
versus (5). The ablation endpoint that labels every disagreement (π = 1) spends a median
of 671 labels on comparable pairs, confirming that subsampling disagreements, not merely

                                                                 17

[p.18]

                                                                 Vishnu Bindu Balachandran




                                      (a) Label cost, Discern vs uniform                                                               (b) The disagreement law
                            1.0                                                                                   2500          0.005 < <
                                                                                                                                    0.005
                            0.8                                                                                   2000




                                                                                    labels to certified verdict
fraction of benign audits


                                              56% certified
                                              with zero labels
                            0.6                                    90% within 188                                 1500

                            0.4                                                                                   1000

                            0.2                                  uniform labeling                                  500
                                                                                                                                             Nlab     20,031 (R 2 = 0.999)
                                                                 Discern
                            0.0                                                                                      0
                                  0    100      101       102      103     104                                           0.00   0.02     0.04       0.06   0.08    0.10      0.12
                                          labels to certified verdict                                                           disagreement rate (unlabeled, free)



Figure 4: (a) Distribution of labels to a certified verdict on the 1,672 benign certifiable
          audits, Discern versus uniform labeling with the identical CS machinery: 56%
          certify with literally zero labels (Tier-0) and 90% within 188, against a median of
          2,906 for uniform labeling. (b) The disagreement law. Labels to a certified verdict
          against the pair’s true disagreement rate for every certifiable audit, colored by
          true delta (blue ∆ ≤ 0.005, red 0.005 < ∆ < ε). All plotted pairs are within the
          ε tolerance and correctly certified; the red points are small genuine regressions
          that Safe(ε) promotes under its noninferiority semantics. The cloud collapses
          onto the line Nlab ≈ π̄ T ⋆ (ε) ρ with R2 = 0.999, the finite-horizon footprint of
          Theorem 7’s label bound (at ε = 1% the boundary’s range regime makes T ⋆ nearly
          ρ-independent, so label spend is linear in ρ with slope π̄ T ⋆ ≈ 2.0 × 104 ).



restricting to them, contributes materially. Figure 4 (right) shows the label law. Across
all certifiable benign audits, label spend is linear in the pair’s true ρ with R2 = 0.999, and
the fitted slope agrees with π̄ T ⋆ (ε) to within 2%, a direct quantitative confirmation of the
upper-bound mechanism. Tolerance scaling matches the same bound. Tightening ε from 2%
to 1% raises median audited-tier spend from 600 to 1,015 labels on the moderate-ρ band
(details and the censoring protocol at the stream cap in Appendix D).

6.4 Head-to-head label economics against sequential baselines

No published sequential method targets the paired update delta, so we construct the strongest
sequential adaptations of the two adjacent tool families and run all methods on identical
streams with the identical anytime-valid CS machinery and verdict rule, so the only degree
of freedom is where labels are spent. The prediction-powered baseline (PPI-style) receives
the pairing-aware surrogate for free on every point (zero on agreements, a judge score
on disagreements) and labels uniformly at rate q = 12 with the unbiased control-variate
increment Db t +(Lt /q)(Dt − D
                             b t ) and its tight range 2/q −1. The active-testing baseline routes

                                                                                    18

[p.19]

                                 Pay Only for Disagreement




                                                         Tier-0 band         Audited band
                                                    (ρ ≤ 1%, n=246)    (1%<ρ ≤ 20%, n=29)
      Uniform labeling                                         1,476                 2,098
      PPI-style (surrogate + uniform labels)                   2,232                 2,845
      Active-testing (judge routing, all points)               1,474               1,948.5
      Discern (support restriction)                                0                    70

Table 3: Median labels to a sound verdict at ε = 1%, δ = 0.05, all methods sharing the
         identical CS machinery and streams. Every method reached a verdict on every pair
         (Discern on 28 of 29 audited-band pairs) and no method false-alarmed anywhere.
         This cohort is the dedicated comparison study (three exploratory seeds, one stream
         per pair, verdict means certificate or alarm), so its medians differ from the battery
         cohort of Section 6.3, which uses five seeds, several streams per pair, and the
         certification endpoint. Neither adaptive routing without the support restriction
         nor surrogate assistance with uniform labeling escapes the pairing-blind cost of
         Theorem 9. Routing helps by at most a constant, and the control variate pays for its
         own surrogate variance and enlarged increment range. Restriction to disagreements
         is the mechanism, exactly as the Θ(ρ) separation predicts.



labels adaptively by the same judge on all points with floor 0.1 and Horvitz–Thompson
correction, but without the support restriction. The baseline-comparison campaign has
312 pairs, of which 275 are benign (246 in the Tier-0 band and 29 in the audited band)
and 37 are regressions. Since label economics is about the cost of certifying a safe update,
and regressions alarm rather than certify, Table 3 reports labels to a sound verdict on the
275 benign pairs. The 37 regressions are covered by the power and false-alarm analysis of
Section 6.2.
    Two readings of Table 3 matter (Figure 5 shows the full distributions). First, the gap
between Discern and the active-testing baseline (28× on the audited band) isolates the
support restriction from adaptivity in general. The active baseline uses the same judge,
the same HT correction, and the same CS, and still pays the pairing-blind rate. Second,
the PPI-style baseline is slower than plain uniform labeling here, which is not a defect of
prediction-powered inference in its home setting (single-model means with strong surrogates)
but a structural mismatch. For the paired delta the informative mass sits on a ρ-fraction of
traffic, and no reweighting of uniformly placed labels recovers what placement loses. This is
not an artifact of our instantiation. A sweep over the labeling rate and surrogate quality, up
to an unrealizable oracle surrogate, shows that the best member of the PPI family on this
problem is uniform labeling itself, which PPI recovers exactly at q = 1 (Appendix E).

6.5 Repairing drift with a windowed confidence sequence
Section 5.7 scoped the guarantee under drift to weighted averages and promised a windowed
variant for current-regime verdicts. We ran it (Figure 6). The CS restarts every 2,000
points, each window covering its own window-average delta at level δ. Across 429 streams
per schedule (8,580 windows each). Under smooth-mixture drift, window miscoverage is

                                                   19

[p.20]

                                                    Vishnu Bindu Balachandran




                                                                   median 70
      Discern
                                                                                                 median 1,948.5
 active-testing
                                                                                                     median 2,098
      uniform
                                                                                                       median 2,845
     PPI-style

                  0                                 101                     102                 103                   104
                      labels to a sound verdict, audited-band benign pairs (1% <                     20%, identical streams and CS)



Figure 5: The full per-pair distributions behind Table 3 (audited band, symlog scale, one
          dot per pair, black tick at the median). Every Discern audit resolves left of every
          competitor audit, and the separation is not a median artifact but holds pairwise
          across the entire band.


                                            0.175          nominal = 5%           0.1562
                                            0.150          unrestarted CS
                                                           windowed CS
                                            0.125
                              miscoverage




                                            0.100
                                            0.075         0.0629                             0.065
                                            0.050
                                            0.025
                                                                   0.0001
                                            0.000
                                                          smooth mixture          adversarial bursts


Figure 6: Miscoverage under the two synthetic drift schedules, comparing the unrestarted
          CS evaluated against a moving running-average target (outside its guarantee)
          versus the windowed variant evaluated per window. The windowed CS restores
          near-nominal calibration even under adversarial bursts.



0.0001 versus 0.063 for the unrestarted CS on the same streams. Under adversarial burst
drift, it is 0.065 versus 0.156. The windowed variant restores near-nominal calibration even
under bursts (residual excess over δ = 0.05 comes from bursts shorter than the window, and
shrinking the window trades label efficiency for finer tracking). The deployment guidance
is concrete. Run the flat CS for the traffic-averaged verdict and the windowed CS for
regime-local alarms.

                                                                        20

[p.21]

                                Pay Only for Disagreement




6.6 Routing, floors, and confidence budgets
Across a 480-cell ablation grid (four settings, four update types, three seeds), we find three
things. First, routing driven by a sign-flipped, adversarial judge leaves coverage untouched
(0 violations in 48 streams) and changes label spend only, the empirical face of Theorem 5.
Second, the floor πmin ∈ {0.1, 0.25, 0.5} moves neither coverage nor median labels on these
benign pairs, matching the range-regime prediction that the floor enters only through the
boundary’s lower-order term. Third, halving the confidence budget (δ = 0.05 versus 0.10)
produces zero violations at both levels. Across the grid, routing changed label spend only
marginally relative to constant πt . The measured savings come from the support restriction,
and we therefore treat routing robustness as a safety property, namely that no judge can
compromise validity, rather than as a measured speedup. Per-slice certification over 8-way
class-based slices on 72 multiclass audits localizes injected slice regressions with recall 0.893
at 3 false-positive slices out of all benign slices audited, with simultaneous coverage violated
on no audit.

7 Deployment and Governance Artifact
Each completed audit emits a compact evidence record, comprising the tolerance and
confidence, both tiers’ final intervals, the verdict and its stopping time, the number of labels
consumed and their routing trace, and the per-slice table. The record is sufficient for a third
party to recompute the boundary crossing from logged increments, making the promotion
decision auditable after the fact. Records compose across successive updates under the
budget schedule of Proposition 13, so a chain of promotions carries one lifetime soundness
guarantee. We present the regulatory connection as motivation rather than a compliance
claim. The record is the kind of technical log contemplated by the logging and post-market
monitoring duties for high-risk systems under the EU AI Act (Articles 12 and 72), and
by internal model-risk-management review boards that must sign off on updates. A legal
assessment is beyond our scope. We provide the emitter and a reference validation script in
the accompanying code release.

8 Limitations and Scope
Losses through internals. Assumption 1 excludes losses that consult scores rather
than predictions (calibration error). For losses Lipschitz in the model output, the soft
support identity of Proposition 14 recovers the zero-label certificate and the audited tier
with ρ replaced by the soft-disagreement moments; matching the lower bound there, and
handling open-ended judged generation where the output is discrete text, remain open.
Drift. Our guarantee under drift is the weighted-average statement of Section 5.7, and the
burst experiment shows the unrestarted CS can miscover a moving target by design. The
windowed variant restores per-regime verdicts at a logarithmic price, and choosing windows
adaptively is future work. Scale of the LLM zoo. The language-model pairs reach 1.4B
parameters, which fits our audit-with-exact-ground-truth methodology. Nothing in the
engine consumes anything beyond paired predictions and labels, so scale enters only through
ρ and B, and the identical behaviour from 160M to 1.4B supports the claim. Auditing a
70B model is a matter of shadow-scoring cost, not new statistics. Auditing preference-tuned

                                               21

[p.22]

                                 Vishnu Bindu Balachandran




chat updates, where the loss itself is a judged quantity, requires the internals extension
above, and our zoo contains no DPO or RLHF update pairs for the same reason. Baseline
adaptations. No off-the-shelf sequential method targets the paired update delta, so our
prediction-powered and active-testing comparisons (Section 6.4) are our own sequential
adaptations of those estimators, constructed generously (both receive the pairing-aware
surrogate for free) but still adaptations. Allocation. Per-slice budgets use the uniform
δ1 /K split. Optimal Neyman-style allocation across slices is analyzed nowhere in this paper
and left open. Sequences of promotions. Proposition 13 gives family-wise soundness
across a promotion chain from a union schedule. What it does not give is adaptive budget
allocation. The alpha-investing policies of Feng et al. (2021) spend error budget in response
to outcomes and can be strictly more powerful over long sequences, and combining them
with our per-audit label optimality is open. Estimand. ∆ certifies average regression, and
per-slice auditing covers known strata. Certifying against unknown subpopulations connects
to multicalibration and is a natural extension.

9 Conclusion
The promotion decision for a model update reduces to a paired estimand with an observable
support set, and taking that structure seriously yields a complete theory, giving anytime-valid
certificates robust to arbitrary label routing, a zero-label tier that covers the bulk of real
updates, matching upper and lower bounds characterizing the label complexity at Θ(ρ    e 2 /ε2 )
up to logarithmic factors, and a proven Θ(ρ) separation that prices the value of running both
models on unlabeled traffic. The protocol certified real update pairs across four modalities
and real LoRA fine-tunes with essentially zero excess risk and a small fraction of the labeling
cost of current practice. We believe certified, rate-optimal update auditing belongs in every
promotion pipeline, and we will release the complete machinery for that purpose upon
publication.


Acknowledgments and Disclosure of Funding

Details of compute infrastructure and data provenance are in Appendix F. Feature caches
are produced by standard pretrained extractors and reused purely as fixed representations,
as documented there.

Appendix A. The Confidence Sequence
For increments Wt ∈ [0, 1] with conditional mean µ, the predictable-plug-in empirical-
Bernstein (PrPl-EB) process of Waudby-Smith and Ramdas (2024) is, for a predictable
λt ∈ [0, λmax ],
                   Y                                  �
        Mt (m) =         exp λi (Wi − m) − vi ψE (λi ) ,    ψE (λ) = − log(1 − λ) − λ,      (6)
                   i≤t


                bi−1 )2 and µ
with vi = (Wi − µ           bi−1 , σ 2
                                   bi−1 the running mean and variance estimates. For m = µ,
Mt (µ) is a nonnegative supermartingale (Waudby-Smith and Ramdas, 2024, Thm. 2), so

                                                22

[p.23]

                                Pay Only for Disagreement




by Ville’s inequality (Ville, 1939) theqset Ct = {m : Mt (m) < 2/δ}, intersected over time,
is a (1 − δ)-CS for µ. We use λt = 2 log(2/δ)/(b      2 t log(t + 1)) ∧ λ
                                                    σt−1                 max . Increments in
[−c, c] are mapped affinely to [0, 1] by z 7→ (z + c)/(2c), so the mapped increments have
conditional mean (∆ + c)/(2c), and λt depends only on the first t − 1 increments, hence
is Ft−1 -measurable as the guarantee requires. Tier 0 applies this to Wt = At , Tier 1 to
Wt = (Zt + c)/(2c).
    The radius obeys, uniformly over t with probability 1 − δ,

                        �q 2                                                    �
                          σ (log(2/δ)+log log t)   c (log(2/δ)+log log t) log t
                  rt = O            t            +             t                  ,         (7)


where σ 2 is the (conditional) variance scale of the increments. The first term is the variance
regime, the second the range regime. We use (7) as Lemma 15 below.


Appendix B. Proofs
This appendix collects the proofs deferred from the main text, in the order the results appear.
Throughout we use the confidence-sequence facts recalled in Appendix A.

B.1 Proof of Lemma 3
Condition on Ft−1 and Xt . Since Lt is drawn Bern(πt ) independently of Yt given (Ft−1 , Xt ),
and πt is measurable in the conditioning,

           �              �     E[Lt | Ft−1 , Xt ] �              �
          E Zt | Ft−1 , Xt = At                   E Dt | Ft−1 , Xt = At E[Dt | Xt ].
                                       πt

Towering over Xt and using Lemma 2 gives E[Zt | Ft−1 ] = E[Dt At ] = ∆. The range bound
is immediate from |Dt | ≤ B and πt ≥ πmin .                                           ■

B.2 Proof of Theorems 4 and 5
The increments At are i.i.d. Bern(ρ), so the Tier-0 CS covers ρ for all time with probability
1 − δ0 by the PrPl-EB guarantee. For Tier 1, Lemma 3 shows (Zt ) has conditional mean
∆ and range [−c, c] for every predictable routing rule, since predictability of πt is the only
property used, so an arbitrary judge, correct or adversarial, is covered. We stress that
the increments are neither independent nor identically distributed. The validity we invoke
is the martingale form of the PrPl-EB confidence sequence, which requires only that the
tracked quantity be the predictable conditional mean E[Zt | Ft−1 ] = ∆ (constant here) and
that λt be Ft−1 -measurable, not that the Zt be i.i.d. (Waudby-Smith and Ramdas, 2024,
Thm. 2; Howard et al., 2021). The mapped increments (Zt + c)/(2c) therefore satisfy the
conditions under which (6) is a supermartingale at the true mean, and Ville’s inequality
gives time-uniform coverage at level 1 − δ1 . A union bound combines the tiers. Soundness
of the verdicts follows since each verdict is issued only when the relevant interval excludes
the contradicted value, and on the coverage event no interval ever excludes the truth. ■

                                                 23

[p.24]

                                Vishnu Bindu Balachandran




B.3 Width lemma
Lemma 15 (CS radius) Let increments have conditional mean µ, range [0, 1] after map-
                                         2 . With probability at least 1 − δ the PrPl-EB CS
ping, and conditional variance at most σmap
radius satisfies (7) with c = 1, and the empirical variance process concentrates so that the
bound holds with the true variance scale.

This is Theorem 2 together with the width analysis in Appendix D of Waudby-Smith and
                                                                      2
Ramdas (2024), and we do not reprove it. For our mapped increments, σmap ≤ E[Zt2 ]/(2c)2 ,
and                                  h A D2
                                        t t
                                                i     B 2 ρ1    B2ρ
                  E[Zt2 | Ft−1 ] = E        Ft−1 ≤            ≤     ,                 (8)
                                        πt          πmin ∧ πt    π
the last step for constant routing πt ≡ π.

B.4 Proof of Proposition 6
Tier 0 tracks a Bernoulli(ρ) mean with σ 2 =pρ(1−ρ) ≤ ρ and range 1. By Lemma 15 the upper
endpoint satisfies ρt ≤ ρ + rt with rt = O( ρL′δ/t + L′δ log t/t), L′δ = log(2/δ0 ) + log log t. If
Bρ ≤ ε/2, the certificate fires once Brt < ε/2, which gives Bρt ≤ Bρ + Brt < ε as the strict�
trigger requires. With ρ ≤ ε/(2B) both terms are O(ε/B) once t = Θ (B/ε)L′δ log log(B/ε)
(the variance term needs t ≳ BρL′δ /ε2 · B ≤ L′δ B/(2ε), the range term t ≳ L′δ log t B/ε). ■

B.5 Proof of Theorem 7
By (8) the mapped variance scale is at most B 2 ρ/(π(2c)2 ). Lemma 15, undoing the affine
map (multiply radii by 2c), gives uniformly with probability 1 − δ1
                     �q 2                             �
                         B ρ Lδ,t     B    Lδ,t log t
             rt = O        πt     + πmin ·     t        , Lδ,t := Lδ + log log t.

If ∆ ≤ ε/2, the verdict ∆t < ε fires as soon as rt ≤ ε/2 (on the coverage event ∆t ≤
∆ + 2rt by construction of the �running intersection). Solving rt ≤ ε/2 for t yields T ⋆ =
Oe B 2 ρLδ /(πε2 ) + BLδ /(πmin ε) , the first claim. Labels are requested only on sampled
                                                                              ⋆
                           P
disagreements: Nlab =        t≤T ⋆ At Lt is stochastically dominated by Bin(T , ρπ), and a
Chernoff bound gives Nlab ≤ 2ρπT ⋆ + O(Lδ ) with probability 1 − δ1 . Multiplying out,
                                       � 2 2
                                      e B ρ Lδ + π · Bρ Lδ .
                                                          �
                             ρπ T ⋆ = O
                                         ε2     πmin ε
The regression side is symmetric with the roles of the endpoints exchanged. The uniform
baseline bound (5) is the same computation with π = πmin = 1, increments Dt of variance
E[D2 ] = E[D2 1{D ̸= 0}] ≤ B 2 ρ1 , and every point labeled, so labels equal stream time. ■

B.6 Proof of Theorem 8
Construction. Let X = {a, d} with P(X=d) = ρ. On the agreement atom a: f = g,
both correct, D = 0, identically under both worlds. On the disagreement atom d: f ̸= g
and the label makes exactly one of them correct, so D = ±1 (0/1 loss, B = 1). Under
P0 : P(D=+1 | d) = 1/2, hence ∆(P0 ) = 0. Under P1 : P(D=+1 | d) = (1 + θ)/2 with

                                                24

[p.25]

                                Pay Only for Disagreement




θ := ε/ρ ∈ (0, 12 ], hence ∆(P1 ) = ρθ = ε. Unlabeled observations (the atom identity and
both predictions) have identical laws under P0 and P1 , and a label on atom a reveals a
constant. Only a label on d is informative, revealing a Bern((1+θ)/2) draw versus Bern(1/2).
    Change of measure. Consider any procedure adapted to its own observations (it chooses
πt from the past, observes labels it pays for, and stops at a stopping time τ , issuing a verdict).
Let Nd (τ ) be the number of labeled disagreement points at stopping. By the sequential
change-of-measure identity (Kaufmann et al., 2016, Lemma 1), for any stopping time τ and
any event E ∈ Fτ ,
                                       �          �
                        EP0 [Nd (τ )] kl 12 , 1+θ
                                                                         �
                                               2    ≥ kl PP0 (E), PP1 (E) ,

because per-label KL from P0 to P1 is kl( 12 , 1+θ2 ) and all other observations contribute zero
KL. Take E = {procedure issues Safe(ε)}. Soundness under P1 (where ∆ = ε, so Safe(ε),
the assertion ∆ < ε, is false) forces PP1 (E) ≤ δ, while the hypothesis gives PP0 (E) ≥ 1 − δ.
                           1
Then kl(1 − δ, δ) ≥ log 2.4δ     (Kaufmann et al., 2016). Finally, for θ ≤ 21 the per-label
information is small:
                          �          �
                                                          2
                         kl 21 , 1+θ
                                  2
                                                 1
                                       = 12 log 1−θ 2 ≤ θ       (θ ≤ 12 ).

Combining the three displays and substituting θ = ε/ρ,

                                          kl(1 − δ, δ)   1         1     ρ2        1
          EP0 [Nlab ] ≥ EP0 [Nd (τ )] ≥       1 1+θ
                                                       ≥   2
                                                             log       =   2
                                                                             log       ,
                                          kl( 2 , 2 )    θ       2.4 δ   ε       2.4 δ

and the factor 4 in the theorem statement absorbs the slack of the kl ≤ θ2 step at the
boundary θ = 12 .                                                                   ■

B.7 Proof of Theorem 9
Same two worlds. Blindness matters here because f and g are deterministic. A procedure
that shadow-scores an unlabeled point learns its atom for free and exits the class, which is
precisely why the class models labeling without paired inference. A pairing-blind procedure
decides to label a stream point without seeing the atom, so each label reveals a draw of
D with law (1 − ρ)δ0 + ρ Bern± ((1±θ)/2) under each world (mass 1 − ρ at 0, and ±1 with
probabilities ρ(1 ± θ)/2 under P1 , ρ/2 each under P0 ). The shared mass at D = 0 contributes
zero, so the per-label KL is
                     ρ      1   ρ     1    ρ       1
        KLblind =      log     + log     =   log        ≤ ρ θ2                   (θ ≤ 12 ).
                     2     1−θ  2    1+θ   2     1 − θ2
The same change-of-measure argument then yields

                                          log(1/2.4δ)   ρ       1
                           E[Nlab ] ≥            2
                                                      = 2 log       ,
                                              ρθ        ε     2.4 δ
with the stated constant. For achievability, uniform labeling observes exactly these draws,
and the empirical-Bernstein CS on them has variance scale E[D2 ] = ρ, so by the argument
of Theorem 7 with π = 1 on all points it certifies within O(ρL     2
                                                               δ /ε + Lδ /ε) labels.     ■
                                                          e

                                                25

[p.26]

                                Vishnu Bindu Balachandran




B.8 Proof of Proposition 12
Each slice CS is a valid time-uniform CS at level δ1 /K for its conditional difference by
Theorem 4 applied to the thinned stream of slice-k points (thinning preserves the conditional
mean and predictability). A union bound over K slices gives simultaneous coverage 1 − δ1 .
The detection bound is Theorem 7 applied to the slice’s own stream, whose length by time t
concentrates around t P(X ∈ Sk ).                                                          ■

B.9 Proof of Proposition 13
Let Hk denote the history available when audit k starts. It determines the k-th model pair,
tolerances, and budgets. The supermartingale construction behind Theorem 4 uses only the
conditional distribution of audit k’s own increments given its own filtration initialized at Hk ,
so Theorem 4 applies conditionally, and the event Ek that audit k ever issues a false verdict
                           (k)    (k)                                                  (k)     (k)
satisfies P(Ek | Hk ) ≤ δ0 + δ1 almost S      surely.
                                              �       Taking expectations, P(Ek ) ≤ δ0 + δ1 ,
and a union bound over k gives P k Ek ≤ δseq . On the complement, every issued Safe
certificate is true at its stated tolerance, so no regressing update is ever falsely certified. ■

Appendix C. Pre-registration and Seed Discipline
Four gates were frozen before the main campaign. They are time-uniform miscoverage
at most 7% (mandatory), median label ratio versus uniform at most 0.35 (mandatory),
zero-label certification of at least half the benign pairs (reported), and power at least 95%
with zero false alarms (mandatory). The pilot passed all four (0.21%, ≈0, 98.2%, 100% with
0 false alarms). Two pre-launch amendments were logged before any gate data existed. They
scope the validity gate to i.i.d. and adversarially routed streams (drift reported separately,
as the estimand changes under drift), and add implementation notes on convex-head refresh
pairs. Exploratory seeds {2011, 3019, 4021, 5011, 6011} were used for all development. The
confirmation family {179424691, 198491329, 217645199, 236887699, 256203221} was reserved
untouched and spent exactly once on the final replication row of Table 2.

Appendix D. Tolerance Scaling and Censoring
Streams are capped at 30,000/40,000/60,000 points for ε = 2%/1%/0.5%. At ε = 0.5%
a minority of moderate-ρ audits certify within the cap (the required T ⋆ exceeds it), so
median label spend at that tolerance is computed over certifying audits only and reported
as censored. Observed medians on the moderate-ρ band: 600 labels at ε = 2%, 1,015 at
1%, 1,012 (censored) at 0.5%. The 2% → 1% step matches the range-regime prediction of
Lemma 15 at these ρ values. Nothing in the paper’s claims depends on the censored cell.

Appendix E. Baseline Instantiation Sweep
Table 3 instantiates the PPI-style baseline at q = 12 with the paper’s margin-based surrogate.
To rule out an unfavorable instantiation, we sweep the labeling rate q ∈ {0.1, 0.25, 0.5, 1}
and surrogate quality up to an unrealizable oracle (D  b t = Dt exactly), on the same audited-
band cohort and streams, with the tight increment range 2/q − 1 (Table 4). Two facts

                                               26

[p.27]

                               Pay Only for Disagreement




                Median labels to verdict    q = 0.1     q = 0.25     q = 0.5      q=1
                Margin surrogate               2,695∗       3,562∗       3,058∗   2,098
                Oracle surrogate (D
                                  b = D)       3,071∗        2,947        2,560   2,098

Table 4: PPI-style baseline over labeling rate and surrogate quality on the audited-band
         cohort of Table 3 (n = 29 pairs, identical streams, tight range 2/q − 1). Asterisks
         mark configurations where some audits reached no verdict within the stream cap,
         so the median is over verdicts reached (15, 25, 28, and 25 of 29 for the starred cells,
         left to right and top to bottom). Both rows equal uniform labeling at q = 1 by
         construction. The q = 12 margin cell differs from Table 3’s instantiation only in the
         labeling randomness. Discern certifies the same cohort at a median of 70 labels.




                    Median labels to verdict     q = 0.1     q = 0.25      q = 0.5
                                                        ∗            ∗
                    λ = 0.25                      2,501        2,445        2,236∗
                    λ = 0.5                       2,486∗       2,451∗       2,483∗
                    λ = 0.75                      2,725∗       2,739∗        3,353

Table 5: PPI++ power-tuning sweep (Angelopoulos et al., 2023b) over the mixing parameter
         λ and labeling rate q, same audited-band cohort and streams as Table 4 (n = 29
         pairs). The column q = 1 is omitted because every λ collapses to uniform labeling
         (2,098) there. Asterisks mark cells where some audits reached no verdict within
         the stream cap; verdicts reached (of 29) are 21, 27, 28 for λ = 0.25, 20, 24, 28 for
         λ = 0.5, and 15, 27, 29 for λ = 0.75, left to right. No configuration beats uniform,
         so power tuning does not rescue the prediction-powered family on this paired
         estimand. Discern certifies the same cohort at a median of 70 labels.




anchor the sweep. At q = 1 the correction reconstructs Dt exactly, so PPI coincides with
uniform labeling for any surrogate, analytically and in the table. For q < 1 the importance
correction enlarges the increment range faster than subsampling saves labels, so every swept
configuration, including the oracle, is at or above uniform’s label cost. The base estimator
is the prediction-powered inference of Angelopoulos et al. (2023a). We also sweep the
power-tuning parameter λ ∈ {0.25, 0.5, 0.75} of PPI++ (Angelopoulos et al., 2023b), which
interpolates between the classical estimator (λ = 0) and full PPI (λ = 1), on the same
cohort (Table 5). Every (λ, q) cell lands between 2,236 and 3,353 median labels, again at or
above uniform’s 2,098 and far above Discern’s 70, and at q = 1 each collapses to uniform
by construction. The active label-allocation method of Zrnic and Candès (2024) optimizes a
fixed-horizon budget with the same prediction-powered ingredients, so it inherits the same
barrier on this paired estimand. The best member of the prediction-powered family on this
problem is uniform labeling itself, and the comparison in Table 3 is therefore conservative in
Discern’s favor rather than against it.

                                                27

[p.28]

                               Vishnu Bindu Balachandran




Appendix F. Reproducibility
All experiments are CPU-replayable except the LoRA fine-tunes (a single commodity GPU,
about three GPU-hours total). The complete pipeline is orchestrated by a single resumable
script with per-audit atomic artifacts, frozen-gate evaluation, figure generation, and a final
status report. Feature caches (RoBERTa, LayoutLMv3, ResNet, ViT, DINOv2, CLIP) are
produced by standard pretrained extractors run once and reused here as fixed representations,
so no result depends on how they were computed. The release comprises the audit engine
(∼300 lines for both tiers), the update-pair builders, all 14,233 per-stream records itemized
in Table 6, and one-command reproduction of every table and figure. The pre-registration
document with its frozen gates and timestamped amendments, and the reserved-seed protocol,
are part of the same artifact. The full package will be released publicly upon publication
and is available to reviewers on request.

           Campaign                                 Update pairs   Replayed streams
           Pre-registered pilot (frozen gates)              455               3,336
           Main battery                                     715               6,890
           Held-out confirmation (reserved seeds)           715               2,145
           LLM zoo, 160M–410M                                40                  80
           LLM zoo, 1B–1.4B                                  30                  60
           Ablation grid                                      –                 480
           Per-slice study                                    –                  72
           Baseline comparison                              312                 312
           Windowed-drift study                               –                 858
           Total                                                             14,233

Table 6: Authoritative accounting of every replayed audit stream reported in this paper.
         Rows are disjoint campaigns. Abstract-level summaries round down to 14,000+.



References
Anastasios N Angelopoulos, Stephen Bates, Clara Fannjiang, Michael I Jordan, and Tijana
 Zrnic. Prediction-powered inference. Science, 382(6671):669–674, 2023a.
Anastasios N. Angelopoulos, John C. Duchi, and Tijana Zrnic. PPI++: Efficient prediction-
 powered inference. arXiv preprint arXiv:2311.01453, 2023b.
Maria-Florina Balcan, Alina Beygelzimer, and John Langford. Agnostic active learning.
 Journal of Computer and System Sciences, 75(1):78–89, 2009.
Mathieu Bazinet, Valentina Zantedeschi, and Pascal Germain. Bound to disagree: General-
 ization bounds via certifiable surrogates. arXiv preprint arXiv:2602.23128, 2026.
Stella Biderman, Hailey Schoelkopf, Quentin Gregory Anthony, Herbie Bradley, Kyle O’Brien,
  Eric Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, USVSN Sai Prashanth,
  Edward Raff, et al. Pythia: A suite for analyzing large language models across training
  and scaling. In International Conference on Machine Learning, pages 2397–2430, 2023.

                                              28

[p.29]

                              Pay Only for Disagreement




Emily Black, Manish Raghavan, and Solon Barocas. Model multiplicity: Opportunities,
 concerns, and solutions. In Proceedings of the 2022 ACM Conference on Fairness, Ac-
 countability, and Transparency, pages 850–863, 2022.
Akash Bonagiri, Gerard Janno Anderias, Saee Patil, Angelina Lai, Devang Borkar, Gezheng
  Kang, Ishant Gandhi, Setareh Rafatirad, and Houman Homayoun. STABLEVAL:
  Disagreement-aware and stable evaluation of AI systems. arXiv preprint arXiv:2605.02122,
  2026.
Pierre Boyeau, Anastasios N. Angelopoulos, Tianle Li, Nir Yosef, Jitendra Malik, and
  Michael I. Jordan. AutoEval done right: Using synthetic data for model evalua-
  tion. In Proceedings of the 42nd International Conference on Machine Learning, 2025.
  arXiv:2403.07008.
Deborah Charnock, Sasha Shepperd, Gill Needham, and Robert Gann. DISCERN: an
 instrument for judging the quality of written consumer health information on treatment
 choices. Journal of Epidemiology and Community Health, 53(2):105–111, 1999.
Ben Chugg, Santiago Cortes-Gomez, Bryan Wilder, and Aaditya Ramdas. Auditing fairness
  by betting. In Advances in Neural Information Processing Systems, volume 36, 2023.
David Cohn, Les Atlas, and Richard Ladner. Improving generalization with active learning.
 Machine Learning, 15(2):201–221, 1994.
Jean Feng. Learning to safely approve updates to machine learning algorithms. In Proceedings
  of the Conference on Health, Inference, and Learning, pages 164–173, 2021.
Jean Feng, Scott Emerson, and Noah Simon. Approval policies for modifications to machine
  learning-based software as a medical device: A study of bio-creep. Biometrics, 77(1):
  31–44, 2021.
Matt Gorbett and Suman Jana. Cross-model disagreement as a label-free correctness signal.
 arXiv preprint arXiv:2603.25450, 2026.
Steve Hanneke. A bound on the label complexity of agnostic active learning. In Proceedings
  of the 24th International Conference on Machine Learning, pages 353–360, 2007.
Steve Hanneke. Theory of disagreement-based active learning. Foundations and Trends in
  Machine Learning, 7(2–3):131–309, 2014.
Steven R Howard, Aaditya Ramdas, Jon McAuliffe, and Jasjeet Sekhon. Time-uniform,
  nonparametric, nonasymptotic confidence sequences. The Annals of Statistics, 49(2):
  1055–1080, 2021.
Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, and
  Weizhu Chen. LoRA: Low-rank adaptation of large language models. In International
 Conference on Learning Representations, 2022.
Matti Kääriäinen. Generalization error bounds using unlabeled data. In Proceedings of the
 18th Annual Conference on Learning Theory (COLT), volume 3559 of Lecture Notes in
 Computer Science, pages 127–142, 2005.

                                            29

[p.30]

                             Vishnu Bindu Balachandran




Nikos Karampatziakis, Paul Mineiro, and Aaditya Ramdas. Off-policy confidence se-
  quences. In Proceedings of the 38th International Conference on Machine Learning,
  2021. arXiv:2102.09540.
Emilie Kaufmann, Olivier Cappé, and Aurélien Garivier. On the complexity of best-arm
 identification in multi-armed bandit models. Journal of Machine Learning Research, 17
 (1):1–42, 2016.
Jannik Kossen, Sebastian Farquhar, Yarin Gal, and Tom Rainforth. Active testing: Sample-
  efficient model evaluation. In International Conference on Machine Learning, pages
  5753–5763, 2021.
Anany Kotawala. Resolution diagnostics for paired LLM evaluation. arXiv preprint
 arXiv:2605.30315, 2026.
Weizhi Li, Prad Kadambi, Pouria Saidi, Karthikeyan Natesan Ramamurthy, Gautam
 Dasarathy, and Visar Berisha. Active sequential two-sample testing. Transactions on
 Machine Learning Research, 2024. arXiv:2301.12616.
Weizhi Li, Visar Berisha, and Gautam Dasarathy. Advanced tutorial: Label-efficient two-
 sample tests. arXiv preprint arXiv:2501.03568, 2025.
Yitao Li. Who drifted: the system or the judge? Anytime-valid attribution in LLM evaluation
  pipelines. arXiv preprint arXiv:2606.15474, 2026.
Omid Madani, David M. Pennock, and Gary William Flake. Co-validation: Using model
 disagreement on unlabeled data to validate classification algorithms. In Advances in
 Neural Information Processing Systems, volume 17, pages 873–880, 2004.
Charles Marx, Flavio Calmon, and Berk Ustun. Predictive multiplicity in classification. In
 International Conference on Machine Learning, pages 6765–6774, 2020.
Quinn McNemar. Note on the sampling error of the difference between correlated proportions
 or percentages. Psychometrika, 12(2):153–157, 1947.
Mahdi Milani Fard, Quentin Cormier, Kevin Canini, and Maya Gupta. Launch and iterate:
 Reducing prediction churn. In Advances in Neural Information Processing Systems,
 volume 29, pages 3171–3179, 2016.
Donald Musgrove, Andrew Radtke, and Tarek Haddad. Discordant pair analysis for sample
  efficient model evaluation. Scientific Reports, 13:20987, 2023.
Aleksandr Podkopaev and Aaditya Ramdas. Tracking the risk of a deployed model and detect-
  ing harmful distribution shifts. In International Conference on Learning Representations,
  2022.
Aaditya Ramdas, Peter Grünwald, Vladimir Vovk, and Glenn Shafer. Game-theoretic
 statistics and safe anytime-valid inference. Statistical Science, 38(4):576–601, 2023.
Herbert Robbins. Statistical methods related to the law of the iterated logarithm. The
 Annals of Mathematical Statistics, 41(5):1397–1409, 1970.

                                            30

[p.31]

                               Pay Only for Disagreement




Christoph Sawade, Niels Landwehr, and Tobias Scheffer. Active comparison of prediction
 models. In Advances in Neural Information Processing Systems, volume 25, 2012.

Divya Shanmugam, Shuvom Sadhuka, Manish Raghavan, John Guttag, Bonnie Berger, and
  Emma Pierson. Evaluating multiple models using labeled and unlabeled data. In Advances
  in Neural Information Processing Systems, 2025.

Zayx Shawn. PACE: Anytime-valid acceptance tests for self-evolving agents. arXiv preprint
  arXiv:2606.08106, 2026.

Richard Socher, Alex Perelygin, Jean Wu, Jason Chuang, Christopher D Manning, Andrew Y
  Ng, and Christopher Potts. Recursive deep models for semantic compositionality over
  a sentiment treebank. In Proceedings of the 2013 Conference on Empirical Methods in
  Natural Language Processing, pages 1631–1642, 2013.

Megha Srivastava, Besmira Nushi, Ece Kamar, Shital Shah, and Eric Horvitz. An empirical
 analysis of backward compatibility in machine learning systems. In Proceedings of the
 26th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining,
 pages 3272–3280, 2020.

Jean Ville. Étude critique de la notion de collectif. Gauthier-Villars, 1939.

Abraham Wald. Sequential tests of statistical hypotheses. The Annals of Mathematical
 Statistics, 16(2):117–186, 1945.

Ian Waudby-Smith and Aaditya Ramdas. Estimating means of bounded random variables
  by betting. Journal of the Royal Statistical Society Series B: Statistical Methodology, 86
  (1):1–27, 2024.

Ziyu Xu, Nikos Karampatziakis, and Paul Mineiro. Active, anytime-valid risk control-
  ling prediction sets. In Advances in Neural Information Processing Systems, 2024.
  arXiv:2406.10490.

Sijie Yan, Yuanjun Xiong, Kaustav Kundu, Shuo Yang, Siqi Deng, Meng Wang, Wei Xia, and
   Stefano Soatto. Positive-congruent training: Towards regression-free model updates. In
  Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition,
   pages 14299–14308, 2021.

Xiang Zhang, Junbo Zhao, and Yann LeCun. Character-level convolutional networks for text
  classification. In Advances in Neural Information Processing Systems, volume 28, 2015.

Siyu Zhou, Patrick Vossler, Venkatesh Sivaraman, Yifan Mai, and Jean Feng. Adaptive
  auditing of AI systems with anytime-valid guarantees. arXiv preprint arXiv:2605.07002,
  2026.

Tijana Zrnic and Emmanuel J. Candès. Active statistical inference. In Proceedings of the
  41st International Conference on Machine Learning, 2024. arXiv:2403.03208.




                                              31


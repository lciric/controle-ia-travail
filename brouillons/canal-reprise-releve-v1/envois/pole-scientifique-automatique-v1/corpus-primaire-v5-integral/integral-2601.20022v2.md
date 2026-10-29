# TEXTE INTÉGRAL — arXiv:2601.20022v2

- Identifiant : arXiv:2601.20022v2
- Titre (tel qu'écrit dans le PDF) : Quickest Change Detection in Discrete-Time in Presence of a Covert Adversary
- PDF source : `docs/sources/pdf/2601.20022v2.pdf` ; SHA-256 du PDF : `8d090f3171ef76cad597ab263a2de9df49de1d1accf78a8afff55ceb82881b42` (compagnon `.sha256` vérifié par `sha256sum -c` avant lecture)
- Outil d'extraction : `pdftotext -layout -enc UTF-8` (pdftotext version 24.02.0), page par page, marqueur `[p.N]` au début de chaque page (N = numéro de page du PDF, à partir de 1)
- Nombre de pages : 34
- Caractères de contrôle produits par l'extraction (glyphes de polices sans correspondance : délimiteurs de formules, texte de figures à police codée) : 298, les caractères nuls supprimés, les autres remplacés par le caractère de remplacement U+FFFD (position gardée) ; pages : 4 (1), 6 (4), 10 (4), 11 (6), 12 (4), 13 (2), 14 (8), 15 (32), 16 (14), 17 (6), 18 (6), 19 (34), 20 (24), 21 (16), 22 (20), 24 (40), 25 (17), 27 (6), 28 (4), 29 (21), 31 (16), 32 (12), 33 (1)
- Nombre de caractères du texte extrait (marqueurs `[p.N]` compris, en-tête exclu) : 205085
- Mention : texte intégral, aucun retrait, contenu d'attaque verbatim possible — dépôt privé seulement (jamais dans la copie expurgée publique ; règle de sûreté modifiée par R-439).
- Provenance : tout chiffre repris ailleurs doit citer la page `[p.N]` et être relu sur le PDF empreinté (R7). La mise en page en colonnes, les formules et les tableaux peuvent être mal ordonnés dans l'extraction : se reporter au PDF.

---

[p.1]

                                               Quickest Change Detection in Discrete-Time in
                                                      Presence of a Covert Adversary
                                                                  Amir Reza Ramtin                                                 Philippe Nain
                                                   College of Information & Computer Sciences                       Inria centre at Université Côte d’Azur
                                                       University Massachusetts at Amherst                                 Sophia Antipolis, France
                                                                Amherst, MA, USA                                             philippe.nain@inria.fr
                                                                aramtin@umass.edu


                                                                                                         Don Towsley
                                                                                      College of Information & Computer Sciences
arXiv:2601.20022v2 [cs.IT] 16 Feb 2026




                                                                                          University Massachusetts at Amherst
                                                                                                   Amherst, MA, USA
                                                                                                  towsley@cs.umass.edu


                                                                                                            Abstract

                                                   We study the problem of covert quickest change detection in a discrete-time setting, where a sequence of observations
                                              undergoes a distributional change at an unknown time. Unlike classical formulations, we consider a covert adversary who has
                                              knowledge of the detector’s false alarm constraint parameter γ and selects a stationary post-change distribution that depends on
                                              it, seeking to remain undetected for as long as possible. Building on the theoretical foundations of the CuSum procedure, we
                                              rigorously characterize the asymptotic behavior of the average detection delay (ADD) and the average time to false alarm (AT2FA)
                                              when the post-change distribution converges to the pre-change distribution as γ → ∞. Our analysis establishes exact asymptotic
                                              expressions for these quantities, extending and refining classical results that no longer hold in this regime. We identify the critical
                                              scaling laws governing covert behavior and derive explicit conditions under which an adversary can maintain covertness, defined
                                              by ADD = Θ(γ), whereas in the classical setting, ADD grows only as O(log γ). In particular, for Gaussian and Exponential
                                              models under adversarial perturbations of their respective parameters, we asymptotically characterize ADD as a function of the
                                              Kullback–Leibler divergence between the pre- and post-change distributions and γ.

                                                                                                          Index Terms

                                                  Sequential analysis; Discrete-time detection; Quickest change detection; CuSum procedure; Covert adversary.


                                                                                                      I. I NTRODUCTION

                                         The problem of sequential change detection or quickest change detection (QCD), arises in various engineering applications
                                         [11], [16], [17]. In all of these applications, the decision-making agent receives a sequence of stochastic observations that
                                         undergo a change in distribution in response to a change or disruption in the environment. As long as the behavior of the
                                         observations is consistent with the normal (pre-change) state, the decision-maker is content to allow the process to continue.
                                         If the distribution changes, then the decision-maker is interested in detecting the change as soon as possible and taking any
                                         necessary action in response to the change. More precisely, the goal of the decision-maker is to make the average detection
                                         delay (ADD) as small as possible, while constraining the average time to false alarm (AT2FA) to be above some threshold.

                                         Detecting adversarial behavior is one of the most critical applications of QCD [19]. Traditional analyses, however, typically
                                         assume that potential adversaries are unaware of the underlying detection mechanism and therefore cannot adjust their actions to
                                         avoid being caught. In modern interconnected systems, this assumption is increasingly less realistic – sophisticated adversaries
                                         can often infer or estimate aspects of the detection strategy and intentionally manipulate their behavior to remain undetected.
                                         Such covert adversarial behavior poses new challenges for QCD, especially in security-sensitive domains such as cyber defense,
                                         surveillance, and military operations, where even small delays in detection can lead to significant consequences.
                                           A. Ramtin and D. Towsley were supported by the DEVCOM Army Research Laboratory under Cooperative Agreement W911NF-17-2-0196 (IoBT CRA)
                                         and the National Science Foundation under Grant ECCS-2148159.

[p.2]

The notion of covertness, originally introduced in the context of covert communication [2], refers to the ability of a transmitter
to remain undetectable by an observing warden during communication. Most existing work on covert communication assumes
that the detector knows the exact start time of any potential transmission. In contrast, we relax this assumption by extending
the notion of covertness to the QCD setting, where adversaries deliberately act to remain hidden over prolonged time horizons.
This departure results in a fundamentally different adversarial strategy when considered within the framework of QCD. Unlike
traditional adversaries whose actions result in detectable statistical deviations, covert adversaries aim to ensure that ADD scales
with the same order as AT2FA, thereby rendering the QCD procedure ineffective [6].

In this work, we specifically focus on the theoretical characterization of covert adversarial behavior against the Cumulative
Sum (CuSum) procedure. The CuSum procedure, first proposed by Page [10], is one of the most widely studied methods in
quickest change detection. It operates by recursively accumulating log-likelihood ratios of the observed data and signaling an
alarm when this cumulative statistic exceeds a prescribed threshold. The CuSum test is well known for its optimality under
Lorden’s minimax criterion [8], which minimizes the worst-case expected detection delay subject to a false-alarm constraint.
Classical analyses, including Lorden’s asymptotic characterization of ADD, assume that the post-change distribution is fixed
and independent of the false-alarm constraint γ. In more realistic adversarial settings, however, this assumption may not hold: a
covert adversary can deliberately choose a post-change distribution that depends on γ, causing the post-change and pre-change
distributions to become increasingly similar as γ grows. This dependence invalidates classical asymptotic results and motivates
the need for new analyses of scaling stationary post-change models, in which the post-change distribution converges to the
pre-change distribution as γ → ∞.

While prior work has examined covertness in both discrete-time [6], [12] and continuous-time sequential detection settings [14],
these studies differ substantially from our formulation. The work in [6] is primarily rooted in covert wireless communication,
where the modeling assumptions are tailored to communication-theoretic contexts – such as specific channel models and power
constraints – and the focus lies on communication-centric performance metrics rather than fundamental detection limits. In
contrast, [12] investigates an adversarial setting against the CuSum procedure under non-stationarity, without assuming that
the adversary knows the false-alarm constraint parameter, whereas in our work the post-change distribution explicitly depends
on this parameter. Consequently, the formulation in [12] differs fundamentally from ours. The study most closely related to
our framework is the continuous-time analysis in [14], which considers a Brownian-motion model where the post-change drift
depends on the false-alarm constraint. However, that setting benefits from closed-form expressions for both ADD and AT2FA,
allowing for exact characterizations. In contrast, the discrete-time case analyzed here is significantly more challenging, as no
such exact equalities exist between ADD, AT2FA, the detection threshold, and the Kullback–Leibler divergence – necessitating
a refined asymptotic analysis to obtain precise scaling results.

We provide a rigorous asymptotic analysis under a discrete-time stationary setting in which the post-change distribution depends
on the false-alarm constraint parameter γ, deriving a novel asymptotic characterization of ADD for the CuSum procedure when
the difference between the pre-change and post-change distributions diminishes as γ → ∞. In this regime, we demonstrate that
the classical asymptotic result for ADD due to Lorden no longer applies. Our principal theoretical contribution – motivated by
the need to analyze the asymptotics of ADD in this challenging setting – is the establishment of precise asymptotic expressions
for both AT2FA and ADD, formulated in terms of the Kullback–Leibler divergence between the post-change and pre-change
distributions and the detection threshold. These expressions, previously regarded as approximations in classical works such as
[7], [15], are rigorously proven to be asymptotically exact in our regime, thereby substantially strengthening the theoretical
underpinnings of QCD.

Central to our proofs is demonstrating that, in our specific model, the overshoot – the amount by which the detection statistic
exceeds the threshold upon crossing – vanishes asymptotically under the assumptions of our analysis. This behavior is not
true in general; in fact, classical results (e.g., [15]) characterize the asymptotic distribution of the overshoot rather than its
disappearance. However, in our setting, the standard renewal-theoretic bounds on overshoots are too loose and fail to capture
the fine-grained dependence on γ. To address this, we develop a refined asymptotic analysis showing that under two specific
conditions, the overshoots of both the upper and lower boundaries of the corresponding Sequential Probability Ratio Test
(SPRT) – which underlies the CuSum procedure – indeed vanish in the asymptotic regime. This result is essential for rigorously
justifying the validity of our asymptotic expressions for AT2FA and ADD. We note that these two conditions are not easy to
check, since they involve the overshoot random variables of the cumulative sum at the upper and lower boundaries. For this
reason, we introduce Lemma 3.2, which provides sufficient conditions under which these key conditions are guaranteed to hold.
While these sufficient conditions are stronger than the original conditions, they offer a more structured route to verification. A
substantial portion of our technical analysis is devoted to showing that these sufficient conditions hold for the Gaussian and
exponential adversarial models considered in this paper. Accordingly, for any choice of pre- and post-change distributions for

[p.3]

which these sufficient conditions hold, the overshoots vanish asymptotically under our analysis.

Moreover, we investigate precise conditions under which an adversary can maintain covertness, which we define as the scenario
in which the best achievable ADD, under the constraint that AT2FA is at least γ, grows asymptotically as Θ(γ). We formalize
this definition in our analysis, noting that it aligns closely with the notion of covertness introduced in [6]. Through our theoretical
framework, we characterize the required rate at which the post-change distribution must converge to the pre-change distribution
in order to preserve covertness. In this formulation, the adversary’s control over the post-change distribution models its ability
to influence how the statistical properties of the observations evolve after the change. By selecting post-change distributions
that are closer to the pre-change distribution, the adversary can delay detection while remaining covert, a perspective consistent
with [14]. We take this as motivation for studying adversarial choices of post-change distributions, since delayed detection
increases the duration over which the adversary can influence the system before being detected. We also quantify the extent of
this influence by building upon the notion of total damage introduced in [12], which measures the cumulative impact incurred
prior to detection, and study its asymptotic scaling.

To illustrate our theory, we analyze Gaussian-distributed (resp. exponential-distributed) observations, explicitly studying adver-
saries that manipulate both the mean and variance parameters (resp. mean) as functions of γ. While adversaries that vary the
variance have been previously considered in the covert communication literature, adversaries who adjust the mean are motivated
by volume-based attacks that aim to increase activity levels without triggering detection [13]. We prove that our theoretical
results apply to this model by conducting a detailed analysis showing that the conditions established in the preceding section
– which are sufficient to ensure that the overshoots vanish – are indeed satisfied as γ → ∞. This validation confirms that
the asymptotic expressions for AT2FA and ADD remain accurate even in this parametric Gaussian/exponential setting, thereby
demonstrating the broad applicability of our asymptotic framework. We then explore how the ADD scales based on the rate at
which the post-change distribution converges to the pre-change distribution, and establish conditions under which covertness
is maintained in the Gaussian (resp. exponential) case.

The remainder of the paper is structured as follows. Section II presents the necessary preliminaries. Section III develops our
main asymptotic results under the setting where the post-change distribution approaches the pre-change distribution as γ → ∞.
We then specialize these results to Gaussian (resp. exponential) models in Section IV, analyzing adversaries that manipulate
the mean and variance (resp. mean). Finally, we conclude with a summary of contributions in Section V.

                               II. BASIC ELEMENTS OF CHANGE - POINT DETECTION IN DISCRETE - TIME

Let X1 , X2 , . . . be mutually independent random variables (rvs) taking values in a measurable space X . Denote by Fk =
σ(X1 , . . . , Xk ) the smallest σ-fied generated by X1 , . . . , Xk .

Random variables X1 , . . . , Xt−1 have common (pre-change) probability distribution Q0 while rvs Xt , Xt+1 , . . . have common
(post-change) probability distribution Q1 , distinct from Q0 1 . Denote by Et the expectation operator associated with this model.
The change time t is unknown but constant (non-Bayesian setting). The case t = ∞ corresponds to no change occurring, i.e.,
only the distribution Q0 is used, and t = 1 corresponds to the situation where only Q1 is used. We assume that Q0 and Q1
have probability density functions (pdfs), denoted by q0 and q1 , respectively, and that the log-likelihood log(q1 (X)/q0 (X)) is
finite a.s. under both Q0 and Q1 .

Recall that the Kullback–Leibler (KL) divergence of a pdf p1 from a pdf p2 , defined on the same measurable space, is
D(p1 ||p2 ) = E[log(p1 (X)/p2 (X)), with X a rv with pdf p1 , whenever this expectation is finite; if so, D(p1 ||p2 ) ≥ 0, with
D(p1 ||p2 ) = 0 if and only if pdfs p1 and p2 are identical.

Denote by T the set of all (possibly extended) stopping times with respect to the filtration F := {Fk , k ≥ 1}. Fix γ ∈ (0, ∞).
Lorden’s classical problem [8] consists in minimizing
                                                  d(T ) := sup ess supEt [(T − t + 1)+ | Ft−1 ],
                                                             t≥1

over all stopping times T ∈ T such that E∞ [T ] ≥ γ. In words, the goal is to minimize the worst-case average detection
delay under a constraint on the false alarm rate (i.e., 1/E∞ [T ] ≤ 1/γ). Define n(γ) = inf {T ∈T :E∞ [T ]≥γ} d(T ), the optimal
worst-case average detection delay.
  1 Our notation follows that in [11]. We note that some works in the quickest change detection literature instead use ν for the change-point, and f , f for
                                                                                                                                                    0   1
the pre- and post-change densities, respectively, along with Pk , P∞ and Ek , E∞ for the corresponding probability measures and expectations.

[p.4]

Moustakides [9] (see also [11, Section 6.2]) showed that Page’s Cumulative Sum (CuSum) stopping rule [10]
                                                                               
                                                             k
                                                           X       q1 (Xi )    
                                 τh = inf k ≥ 0 : max           log          ≥ h , h > 0,                                                                   (1)
                                                  1≤j≤k+1          q0 (Xi )    
                                                                                 i=j

solves Lorden’s optimization problem if h is selected so that Eq0 [τh ] = γ.

It is known that d(τh ) = Eq1 [τh ] for h > 0 [11, p. 143], [15, p. 25], thereby implying that
                                                                        n(γ) = Eq1 [τh⋆ ],                                                                  (2)
              ⋆                                                                        ⋆
with h = h solution of Eq0 [τh ] = γ. Since τ0 = 0, notice that h > 0 for γ > 0.

There is in general no closed-form expression for n(γ). The behavior of n(γ) as γ → ∞ was obtained by Lorden [8], [11,
Thm 6.17, p. 160]. It is given by
                                                          log γ
                                                n(γ) ∼              , γ → ∞.                                       (3)
                                                        D(q1 ||q0 )
The aim of this work is to revisit Lorden’s result when q1 depends on γ and q1 converges pointwise to q0 as γ → ∞.

Notation: For any event A, 1A = 1 if A if true and zero otherwise. If a function f is differentiable at x0 ∈ R, we denote by
f ′ (x0 ) its derivative at this point. The shorthands f (x) ∼x g(x) and limx f (x) will stand for f (x) = g(x) + o(1) (x → ∞)
and limx→∞ f (x), respectively.

                                         III. L IMITING BEHAVIOR OF n(γ) WHEN q1 DEPENDS ON γ

We still consider the setting in Section II but we now assume that q1 depends on γ with limγ q1 = q0 . We further assume2
that Xk ∈ R = (−∞, ∞) (k ≥ 1). To make explicit the dependence on γ, q1 will now be denoted by qγ . For simplicity, q0 is
denoted by q. We denote by Pp and Ep the probability and expectation operators associated with the pdf p ∈ {q, qγ }. In other
words, under Pqγ (resp. Pq ), X1 , X2 , . . . are i.i.d. real-valued rvs with common pdf qγ (resp. q). We further assume that there
exists γ0 > 0 such that3 qγ ̸= q for all γ > γ0 . Since we are only interested in limiting results when γ → ∞, we will actually
assume, without loss of generality, that qγ ̸= q for all γ > 0. Last, we assume that the log-likelihood ratio log(qγ (X1 )/q(X1 ))
is finite Pqγ -a.s. (resp. Pq -a.s.) for all γ > 0.

Our goal is to find conditions on qγ ensuring covertness of an attacker. We say that an attacker is covert if n(γ) = Θ(γ),
namely, for large γ, the optimal worst-case average detection delay is of the same order of magnitude as the largest admissible
lower bound on the expected time between false alarms.

In addition to analyzing n(γ), we also introduce a measure of the impact that a change in distribution may have on the system
prior to detection. We model this impact through a damage measure defined as a function of the KL divergence between the
pre-change and post-change models [12]. Specifically, let g : R+ → R+ be a strictly increasing function with g(0) = 0 Then,
the corresponding total expected damage accrued up to the detection time is defined as
                                                                          �
                                                  d(γ) = n(γ)g D(q||qγ ) .                                                 (4)
 Fix γ > 0 unless otherwise mentioned. Introduce the Sequential Probability Ratio Test (SPRT) [11, Chapter 4], [15, Chapter
2]
                                                Ta,b = inf{k ≥ 1 : Sk ̸∈ (a, b)},                                       (5)
            Pk                       qγ (Xj )
with Sk := j=1 Yj and Yj := log q(Xj ) . We assume that −∞ < a ≤ 0 < b < ∞. Denote by αa,b = Pq (STa,b ≥ b) and
βa,b = Pqγ (STa,b ≤ a) the error probabilities.

Notice that Ta,b depends on γ as Sk does through qγ , and so do αa,b and βa,b . To keep notation compact we do not make
this dependence explicit. In addition, when no confusion may occur, Ta,b , αa,b , and βa,b are simply denoted by T , α, and β,
respectively.

Because4 qγ and q are different pdfs, Pp (Y1 = 0) < 1 for p ∈ {q, qγ }, which ensures that Ep [T ] < ∞ for p ∈ {q, qγ } by Stein’s
  2 Results in Section III hold if R is replaced by any measurable space X (e.g., X = Rd , for d ≥ 1).
  3 Two pdfs are different if they differ on a set of positive measure.
  4 Let A = {x ∈ R : q
                                                                R
                         γ (x) = q(x)}. Then, Pp (Y1 = 0) =         A p(x)dx. If the latter integral was equal to one then qγ = q p-a.e., which would contradict
the assumption that qγ ̸= q. Hence, Pp (Y1 = 0) < 1.

[p.5]

lemma [15, Proposition 2.18]. Notice that Eqγ [Y1 ] = D(qγ ||q) and Eq [Y1 ] = −D(q||qγ ). We assume that both expectations
are finite, so that Eqγ [Y1 ] > 0 and Eq [Y1 ] < 0 since qγ and q are different pdfs.

Propositions 3.1-3.2 and Lemma 3.1 will be proved under the conditions that the expected overshoots converge to zero as
γ → ∞ , namely,
                                                  lim Ep [ST − b | ST ≥ b] = 0,                                               (6)
                                                     γ
                                                  lim Ep [ST − a | ST ≤ a] = 0,                                               (7)
                                                     γ

for p ∈ {q, qγ }. Conditions (6)-(7) are not easy to check since they involve the (unknown) overshoot random variables ST − a
and ST − b. In Lemma 3.2 we will provide sufficient conditions for (6)-(7), easier to verify than conditions (6)-(7).

Proposition 3.1: Assume that conditions (6)-(7) are satisfied. Then, for a < 0 < b,
                                                          A(B − 1)a + B(1 − A)b
                                              Eqγ [T ] ∼γ                         ,                                           (8)
                                                              D(qγ ||q)(B − A)
                                                            (B − 1)a + (1 − A)b
                                               Eq [T ] ∼γ −                     ,                                             (9)
                                                              D(q||qγ )(B − A)
with A = ea and B = eb .

Proof: We have
                                 Eqγ [ST 1{ST ≤a} ] = β Eqγ [ST − a | ST ≤ a] + βa,
                                 Eqγ [ST 1{ST ≥b} ] = (1 − β) Eqγ [ST − b | ST ≥ b] + (1 − β)b.
Summing both equations gives
                                                 Eqγ [ST ] = βa + (1 − β)b + c1 ,                                           (10)
with c1 := β Eqγ [ST − a | ST ≤ a] + (1 − β)Eqγ [ST − b | ST ≥ b]. Similarly one finds
                                                 Eq [ST ] = (1 − α)a + αb + c2 ,                                            (11)
with c2 := (1 − α) Eq [ST − a | ST ≤ a] + αEq [ST − b | ST ≥ b].

Since Ep [T ] < ∞ and Ep [Y1 ] < ∞ for p ∈ {q, qγ }, Wald’s identity applies to Ep [ST ], to yield Ep [ST ] = Ep [T ]Ep [Y1 ] for
p ∈ {q, qγ }. Applying this identity to (10) and (11), we obtain
                                                        1
                                          Eqγ [T ] =           (βa + (1 − β)b + c1 ) ,                                       (12)
                                                     D(qγ ||q)
                                                           1
                                           Eq [T ] = −           ((1 − α)a + αb + c2 ) .                                     (13)
                                                       D(q||qγ )
Letting now γ → ∞ in (12)-(13) and using assumptions (6)-(7), gives
                                                       1
                                        Eqγ [T ] ∼γ           (βa + (1 − β)b),                                              (14)
                                                    D(qγ ||q)
                                                          1
                                         Eq [T ] ∼γ −           ((1 − α)a + αb).                                            (15)
                                                      D(q||qγ )
The proof is completed upon replacing α and β in (14)-(15) by their asymptotics given in Lemma 3.1 below.

Lemma 3.1: If conditions (6)-(7) hold, then
                                                     1−A                       B−1
                                              α ∼γ           and    β ∼γ A         ,                                        (16)
                                                     B−A                       B−A
with A = ea and B = eb .
                                                            Qk     qk (Xk )
Proof: Fix ϵ > 0. Let A = ea and B = eb . Define Λk =          j=1 q(Xk ) . Conditioning on the value of T   (recall that T < ∞
p-a.s. since Ep [T ] < ∞ for p ∈ {q, qγ }), we obtain
                                                              XZ      k
                                                                      Y
                                     Pq (B ≤ ΛT < Beϵ ) =                    q(xj )dx1 · · · dxk ,
                                                              k≥1   Sk j=1

[p.6]

with (here x̄k = (x1 , . . . , xk ))
                                                   j
                                (                                                                       k
                                                                                                                                )
                                               k
                                                   Y qγ (xi )                                           Y qγ (xi )          ϵ
                         Sk := x̄k ∈ R ,                          ∈ (A, B), j = 1, . . . , k − 1, B ≤                  < Be         .
                                                   i=1
                                                         q(xi )                                         i=1
                                                                                                              q(xi )
Hence,
                               Z   k                                                                    Z     k
                    1 X            Y                                                          1 X             Y
                                           qγ (xj )dx1 · · · dxk ≤ Pq (B ≤ ΛT < Beϵ ) ≤                           qγ (xj )dx1 · · · dxk .
                   Beϵ         Sk j=1                                                         B          Sk j=1
                         k≥1                                                                     k≥1
        P      R    Qk                                            ϵ
Since     k≥1 Sk      j=1 qγ (xj )dx1 · · · dxk = Pqγ (B ≤ ΛT < Be ), the above inequalities become

                                1                                             1
                                  ϵ
                                    Pqγ (B ≤ ΛT < Beϵ ) ≤ Pq (B ≤ ΛT < Beϵ ) ≤ Pqγ (B ≤ ΛT < Beϵ ).                                          (17)
                               Be                                             B
On the other hand,
              Pq (B ≤ ΛT < Beϵ ) = Pq (B ≤ ΛT ) − Pq (ΛT ≥ Beϵ ) = α − Pq (ΛT ≥ Beϵ | ΛT ≥ B)α,
                                           = αPq (ΛT < Beϵ | ΛT ≥ B),                                                                       (18a)
             Pqγ (B ≤ ΛT < Be ) = Pqγ (B ≤ ΛT ) − Pqγ (ΛT ≥ Beϵ ) = 1 − β − Pqγ (ΛT ≥ Beϵ | ΛT ≥ B)(1 − β),
                                       ϵ

                                           = (1 − β)Pqγ (ΛT < Beϵ | ΛT ≥ B).                                                                (18b)
To establish (18b) we used the identity Pqγ (ΛT ≥ B) = Pqγ (ΛT > A) = 1 − β, which since T is almost surely finite.
Combining (17), (18a), and (18b), we obtain
                    1 1 − β Pqγ (ΛT < Beϵ | ΛT ≥ B)             1 − β Pqγ (ΛT < Beϵ | ΛT ≥ B)
                       �      �                               �      �
                                                        ≤α≤                                   .               (19)
                    eϵ    B      Pq (ΛT < Beϵ | ΛT ≥ B)           B    Pq (ΛT < Beϵ | ΛT ≥ B)
For p ∈ {q, qγ },
                                                                                         1
                   Pp (ΛT ≥ Beϵ | ΛT ≥ B) = Pp (ST − b ≥ ϵ | ST ≥ b) ≤                     Ep [ST − b | ST ≥ b] → 0 as γ → ∞,
                                                                                         ϵ
where the inequality follows from conditional Markov’s inequality5 and the latter limit follows from (6). This shows that
limγ Pp (ΛT < Beϵ | ΛT ≥ B) = 1. Thus, upon letting γ → ∞ and then ϵ → 0 in (19), we get
                                                                                1−β
                                                                         α ∼γ       ,                                                        (20)
                                                                                 B
Similarly, we find
                                                                      β ∼γ A(1 − α).                                                         (21)
From (20)-(21) we derive (16).

The link between the CumSum test in (1) and the SPRT in (5) is made through the formula [11, Theorem 6.5], [15, Eq. (2.52)]
                                                                     Ep [T0,h ]        Ep [T0,h ]
                                                    Ep [τh ] =                   =                   ,                                       (22)
                                                                  Pp (ST0,h ≥ h)   Ep [1{ST0,h ≥h} ]
which holds for any pdf p on R. It allows us to establish the following proposition:

Proposition 3.2: If conditions (6)-(7) hold, then
                                                                          1
                                                          Eqγ [τh ] ∼γ           (e−h + h − 1),                                              (23)
                                                                       D(qγ ||q)
                                                                          1
                                                           Eq [τh ] ∼γ           (eh − h − 1).                                               (24)
                                                                       D(q||qγ )

   5 Let X be a real-valued rv defined on a probability space (Ω, F , P) such that P(X ≥ 0) > 0. For x > 0, P(X ≥ x | X ≥ 0) = E[1{X≥x} 1{X≥0} ] ≤
                                                                                                                                    P(X≥0)
E[ X  1
    x {X≥0}
             ]    1
    P(X≥0)
               =  x
                    E[X  | X ≥  0].

[p.7]

Proof: From Proposition 3.1, for a < 0 < b,
                                          Eqγ [Ta,h ]        ea (eh − 1)a + eh (1 − ea )h
                                                          ∼γ                              ,                                  (25)
                                       Eqγ [1{STa,h ≥h} ]        D(qγ ||q)eh (1 − ea )
                                            Eq [Ta,h ]       ea (eh − 1)a + eh (1 − ea )h
                                                          ∼γ                              .                                  (26)
                                        Eq [1{STa,h ≥h} ]          D(q||qγ )(1 − ea )
However, letting a = 0 in the right-hand sides of (25) and (26) yieds 0/0. We therefore need to take a little detour. From (22)
                                                 Ep [limm T−1/m,h ]             Ep [T−1/m,h ]
                                Ep [τh ] =                             = lim                      ,
                                             Ep [limm 1{ST−1/m,h ≥h} ]    m Ep [1{S
                                                                                    T−1/m,h ≥h}
                                                                                                ]
where the interchange between the expectation operator and the limit in the numerator follows from the monotone convergence
theorem applied to the non-increasing and non-negative sequence {T−1/m,h }m≥1 , while the interchange between the expectation
operator and the limit in the denominator follows from the bounded convergence theorem. Hence, for p = qγ ,
                                 Eqγ [τh ]           1             Eqγ [T−1/m,h ]
                  lim      1        −h
                                                = −h      lim lim 1                     ,
                   γ
                        D(qγ ||q) (e   + h − 1)  e + h − 1 γ m D(qγ ||q) (1 − β−1/m,h )
                                                          1         Eqγ [T−1/m,h ]
                                                  =              lim lim
                                                                   1                     ,
                                                      e−h + h − 1 m
                                                                D(qγ ||q) (1 − β−1/m,h )
                                                                      γ

                                                       1       − 1 e−1/m (eh − 1) + eh (1 − e−1/m )h
                                                  = −h    × lim m                                    ,                       (27)
                                                   e +h−1    m               eh (1 − e−1/m )
                                                        1         −eh + 1 + eh h
                                                  =            ×                 = 1,
                                                 e−h + h − 1            eh
where (27) follows from Proposition 3.1 and Lemma 3.1 when conditions (6)-(7) hold. This proves (23). The proof of (24) is
similar (Hint: Eq [1{ST−1/m,h ≥h} ] = α−1/m,h ) and is therefore omitted.

The proofs of Propositions 3.1-3.2 and of Lemma 3.1 are inspired by the proofs of several elementary results in sequential
detection theory. These include the bounds (in our notation) 1−β                β
                                                                  α ≥ B and 1−α ≤ A [11, Prop. 4.10], [18, p. 45], Eq [T ] ≥
D(q||qγ ) [α log 1−β + (1 − α) log β ] and Eqγ [T ] ≥ D(qγ ||q) [(1 − β) log 1−β
          −1        α                  1−α                           −1                         β
                                                                                   α + γ log 1−α ] [11, Prop. 4.11], [15, Thm
2.39]. It is also worth noting that the r.h.s. of (8) and (9) provide known approximations for Eqγ [T ] and Eq [T ], respectively,
where the approximation, due to Wald [18], originates from neglecting the excess over the boundaries a and b, i.e., ST ≈ a
or ST ≈ b [11, p. 77]. Proposition 3.1 says that these approximations give the exact limiting behavior of Eqγ [T ] and Eq [T ] as
γ → ∞, when limγ qγ = q and conditions (6)-(7) are met.

The r.h.s. of (23)-(24) are nothing but Khan’s approximations for Eqγ [τh ] and Eq [τh ] [7, Corollary, p. 76], [15, Eqns (2.54),
p. 26]. Proposition 3.2 shows that these approximations are exact when limγ qγ = q and conditions (6)-(7) hold.

In Lemma 3.2 below we provide sufficient conditions for (6)-(7) to hold. These new conditions only involve the rv Y =
    qγ (X)
log q(X)   , making them easier to check.

Lemma 3.2: Condition (6) holds if
                                                   lim sup Ep [Y − y | Y ≥ y] = 0,                                           (28)
                                                      γ y≥0

and condition (7) holds if
                                                   lim inf Ep [Y − y | Y ≤ y] = 0,                                           (29)
                                                      γ y≤0

                               q (X)
                               γ
for p ∈ {q, qγ }, with Y = log q(X) and X a real-valued random variable.

Proof: Fix p ∈ {q, qγ }. Conditioning on ST −1 = x and using ST = ST −1 + YT , we get
                                          Z b
                   Ep [ST − b | ST ≥ b] =     Ep [ST − b | ST ≥ b, ST −1 = x]dFp,ST −1 | ST ≥b (x),
                                           a
                                          Z b
                                        =     Ep [YT − (b − x) | YT ≥ b − x, ST −1 = x]dFp,ST −1 | ST ≥b (x),                (30)
                                              a

[p.8]

where dFp,ST −1 | ST ≥b (x) is the pdf of ST −1 under p given that ST ≥ b. By the strong Markov property for i.i.d. sequences,
we have6
                                                           Pp (YT ≥ y | FT −1 ) = Pp (Y1 ≥ y),                                      (31)
                                                    Ep [YT 1{YT ≥y} | FT −1 ] = Ep [Y1 1{Y1 ≥y} ].                                  (32)
Thus, for any y ∈ R,
                                                           Ep [YT 1{YT ≥y} | FT −1 ]   Ep [Y1 1{Y1 ≥y} ]
                     Ep [YT | YT ≥ y, FT −1 ] =                                      =                   = Ep [Y1 | Y1 ≥ y].
                                                            Pp (YT ≥ y | FT −1 )        Pp (Y1 ≥ y)
Since {ST −1 = x} ∈ FT −1 , the latter identity yields
                                                  Ep [YT | YT ≥ y, ST −1 = x] = Ep [Y1 | Y1 ≥ y].                                   (33)
Subtracting b − x from both sides of (33) and choosing y = b − x, gives
                            Ep [YT − (b − x) | YT ≥ b − x, ST −1 = x] = Ep [Y1 − (b − x) | Y1 ≥ b − x].
Introducing this result in (30), we obtain
                                                                Z b
                         0 ≤ Ep [ST − b | ST ≥ b] =                   Ep [Y1 − (b − x) | Y1 ≥ b − x]dFp,ST −1 | ST ≥b (x),
                                                                 a
                                                                                                  Z b
                                                            ≤        sup Ep [Y1 − y | Y1 ≥ y] ×       dFp,ST −1 | ST ≥b (x),
                                                                0≤y≤b−a                              a
                                                            ≤ sup Ep [Y1 − y | Y1 ≥ y],
                                                                y≥0
                            Rb
where we have used that      dFp,ST −1 | ST ≥b (x) = 1, which proves that (6) is true (28) is satisfied. Similarly,
                             a
                                     Z b
         0 ≥ Ep [ST − a | ST ≤ a] =       Ep [Y1 − (a − x) | Y1 ≤ a − x]dFp,ST −1 | ST ≤a (x) ≥ inf Ep [Y1 − y | Y1 ≤ y],
                                              a                                                                    y≤0

which proves (7) is true if (29) is satisfied.
                                                                                           γ               q (x)
Remark 3.1 (Sufficient condition for (6)-(7) to hold): Conditions (6)-(7) will hold if (C) q(x) → 1 uniformly on R as γ → ∞.
                                                    γ                    γ q (x)                   q (x)
This is so as 0 ≤ Ep [ST − b | ST ≥ b] ≤ supx∈R log q(x) and inf x∈R log q(x) ≤ Ep [ST − a | St ≤ a] ≤ 0, and that
                 q (x)
                 γ                       γ         q (x)
limγ inf x∈R log q(x) = limγ supx∈R log q(x) = 0 under (C). Condition (C) is of course very restrictive; in particular, it does
not hold for the Gaussian and exponential models discussed in Section IV. It will hold, for instance, if rvs {Xk }k have a finite
support in R.

Before stating the main result of this paper (Proposition 3.3 below), let us recall some properties of the Lambert function that
we will use in its proof. The Lambert function is the solution of the equation W (z)eW (z) = z, z ∈ C [5]. When z is real,
W (z)eW (z) = z has a solution if and only if z ≥ −e−1 . When z ≥ 0, this solution is unique, given by the main branch W0
of W , and when −e−1 ≤ z < 0 there are two solutions given by the branches W0 and W−1 of W . In particular,
                                          W0 (z) > −1, W−1 (z) < −1 for − e−1 < z < 0,                                              (34)
and W0 (−e−1 ) = W−1 (−e−1 ) = −1. Last [5, p. 350]
                                      W−1 (x) ∼ log(−x) − log(− log(−x)) as x → 0, x < 0.                                           (35)

Proposition 3.3 (Limiting behavior of n(γ)): When conditions (6)-(7) hold,
                                        
                                           log(γD(q||qγ ))
                                        
                                        
                                             D(qγ ||q)    , if limγ γD(q||qγ ) = ∞,
                                           γD(q||qγ ) G(y)
                              n(γ) ∼γ       D(qγ ||q)   y , if limγ γD(q||qγ ) = y ∈ (0, ∞),                                        (36)
                                         γD(q||qγ ) ,
                                        
                                                             if limγ γD(q||qγ ) = 0,
                                        
                                                       D(qγ ||q)

  6 For C ∈ F
                                          P                                                    P
             T −1 , Pp ({YT ≥ y} ∩ C) =   k≥0 Pp ({Yk+1 ≥ y} ∩ C ∩ {T − 1 =P    k}) = k≥0 Pp (Yk+1 ≥ y)Pp (C ∩ {T − 1 = k}) since Yk+1 is
independent of C ∩ {T − 1 = k} ∈ Fk . Hence, Pp ({YT ≥ y} ∩ C) = Pp (Y1 ≥ y) k≥0 Pp (C ∩ {T − 1 = k}) = Pp (Y1 ≥ y)Pp (C). Therefore, for
                                 P ({Y ≥y}∩C)
any C ∈ FT −1 , Pp (YT ≥ y | C) = p PT (C)       = Pp (Y1 ≥ y), which proves (31). The proof of (32) is similar.
                                      p

[p.9]

where the mapping G(y) given by
                                                            −1−y
                                     G(y) = e1+y+W−1 (−e           )
                                                                       − W−1 (−e−1−y ) − y − 2,                               (37)
satisfies G(y)                              G(y)             G(y)
           y ∈ (0, 1) when 0 < y < ∞, limy↓0 y = 1 and limy→∞ y = 0.

Proof: Recall that for every γ > 0, the optimal threshold h⋆ is strictly positive (cf. Section II) and D(q||qγ ) > 0 by assumption.
                                                           ⋆
                                                  1
The identity Eq [τh⋆ ] = γ and (24) imply that D(q||qγ)
                                                        (eh −h⋆ −1) ∼γ γ. Hence, there exists a mapping ζ : (0, ∞) → (−1, ∞)
with limγ ζ(γ) = 0, such that
                                                           ⋆
                                                         eh − h⋆ − 1 = ξ,                                                      (38)
with ξ := (1 + ζ)γD(q||qγ ) > 0. Eq. (38) rewrites
                                                                       ⋆
                                                    −(h⋆ + r)e−(h +r) = −e−r ,                                                (39)
with r := 1 + ξ > 1. Since −e−1 ≤ −e−r < 0, (39) has two solutions, h1 + r = −W0 (−e−r ) and h2 + r = −W−1 (−e−r ).
From (34), h1 < −ξ < 0, implying that h⋆ = h2 , that is,
                                h⋆ (γ) = −1 − (1 + ζ)γD(q||qγ ) − W−1 (−e−1−(1+ζ)γD(q||qγ ) ).
Since ζ(γ) ∼γ 0, we deduce from the above that
                                      h⋆ (γ) ∼γ −1 − γD(q||qγ ) − W−1 (−e−1−γD(q||qγ ) ).                                     (40)
Combining (2), (23), and (40) yields
                                                               G(γD(q||qγ ))
                                                     n(γ) ∼γ                 ,                                                (41)
                                                                 D(qγ ||q)
by using the definition of G in (37). We are now in position to prove (36). Assume first that limγ γD(q||qγ ) = ∞. It is easily
seen from (37) and (35) that G(y) ∼y log y, so that, by (41),
                                                               log(γD(q||qγ ))
                                                     n(γ) ∼γ                   .
                                                                  D(qγ ||q)
When limγ γD(q||qγ ) = y ∈ (0, ∞) we see from (41) that
                                                       G(y)        γD(q||qγ ) G(y)
                                           n(γ) ∼γ              ∼γ             ·   .
                                                      D(qγ ||q)    D(qγ ||qγ )   y
Last, assume that limγ γD(q||qγ ) = 0. Rewriting (41) as
                                                        G(γD(q||qγ ) γD(q||qγ )
                                              n(γ) ∼γ               ×           ,
                                                         γD(q||qγ )   D(qγ ||q)
we note that the last asymptotic result in (36) holds if limy↓0 G(y)
                                                                 y = 1. Let us prove the latter identity. Set x = −W−1 (−e
                                                                                                                           −1−y
                                                                                                                                ).
               −x        −1−y
Hence, (−x)e = −e              by definition of the Lambert function, giving y = x − 1 − log x. With this change of variable
G(y)/y becomes
                                                       G(y)     log x − 1 + x1
                                                             =                 ,                                             (42)
                                                          y     x − 1 − log x
yielding
                                                  G(y)       log x − 1 + x1
                                              lim      = x→1
                                                         lim                = 1,
                                              y→0
                                              y>0
                                                   y     x<1
                                                             x − 1 − log x
where the latter equality follows from L’Hôpital’s rule. To conclude the proof, we readily obtain from (42) that G(y)/y ∈ (0, 1)
for y ∈ (0, ∞) and limy→∞ G(y)/y = 0.

Corollary 3.1: The largest asymptotic order of n(γ) is reached when γD(q||q0 ) = y + o(1) (γ → ∞), and it corresponds to
covertness, i.e., n(γ) = Θ(γ).

Remark 3.2 (Asymptotic behavior of h⋆ (γ)): When conditions (6)-(7) hold,
                                 
                                  log(γD(q||qγ )),             if limγ γD(q||qγ ) = ∞,
                                                        −1−y
                       h⋆ (γ) ∼γ    −1  −  y − W−1  (−e      ), if limγ γD(q||qγ ) = y ∈ (0, ∞),                              (43)
                                  p
                                       2γD(q||qγ ),             if limγ γD(q||qγ ) = 0.

[p.10]

The first asymptotic result in (43) follows from (40) and (35). The second asymptotic√result directly follows from (40). The
                                                                               −1−x
                                   p (40) together with −1 − x − W−1 (−e
third asymptotic result follows from                                                ) ∼ 2x when x → 0 with x > 0 [5, pp.
350-351, Eq. (4.22)] (take p = − 2(ez + 1) for W−1 as mentioned at the top of p. 351). It is tempting to conclude that (43)
generalizes the corresponding result, given by h⋆ (γ) ∼γ log γ, obtained in the classical setting when the post-distribution does
not depend on the false alarm rate. Indeed, if qγ does not depend on γ, then γD(q||qγ ) ≈ γ, and h⋆ (γ) ∼γ log γ from the
first asymptotic result in (43). This conclusion is however incorrect since (43) only holds if conditions (6)-(7) are met, which
will clearly be not true if qγ does not depend on γ or, more specifically, if qγ does not converge to q as γ → ∞.

We now analyze the asymptotic behavior of the adversary’s total damage as defined in (4).

Proposition 3.4: Assume g(x) = xρ with ρ ∈ (0, 1) and that limγ D(q||qγ )/D(qγ ||q) = c for some c > 0. Then, if conditions
(6)–(7) hold, the total damage d(γ) = n(γ)g(D(q||qγ )) has its largest asymptotic order when γD(q||qγ ) = Θ(1), with
d(γ) = Θ(γ 1−ρ ).
                                                                                                             �ρ
Proof: Since conditions (6)–(7) hold, Proposition 3.3 applies. With g(x) = xρ , we have d(γ) = n(γ) D(q||qγ ) . Moreover,
since limγ D(q||qγ )/D(qγ ||q) = c, it follows that 1/D(qγ ||q) ∼γ c/D(q||qγ ).

First, if limγ γD(q||qγ ) = ∞, with tγ = γD(q||qγ ) → ∞,
                                                       �ρ−1
                                    d(γ) ∼γ c D(q||qγ )     log(tγ ) = cγ 1−ρ tρ−1
                                                                               γ   log(tγ ),
which, since limt→∞ tρ−1 log t = 0 for ρ ∈ (0, 1), implies
                                                        d(γ) = o(γ 1−ρ ).

Next, if limγ γD(q||qγ ) = y ∈ (0, ∞), then D(q||qγ ) ∼γ y/γ and
                                              G(y)          �ρ    G(y) ρ 1−ρ
                                 d(γ) ∼γ cγ        D(q||qγ ) ∼γ c     y γ    = Θ(γ 1−ρ ).
                                               y                   y

Finally, if limγ γD(q||qγ ) = 0, then D(q||qγ ) = o(1/γ) and
                                                                     �ρ
                                              d(γ) ∼γ cγ D(q||qγ )        = o(γ 1−ρ ).

Therefore, d(γ) has its largest asymptotic order when γD(q||qγ ) = Θ(1), and in this case d(γ) = Θ(γ 1−ρ ).

Note that, in the setting of the above proposition and following Proposition 3.3, the regime γD(q||qγ ) = Θ(1) coincides with
the transition between detectability and covertness.

                                IV. A PPLICATION TO G AUSSIAN AND EXPONENTIAL MODELS

In this section, we first address the situation when both the pre-change and post-change distributions are Gaussian distributions,
then we investigate the case when both distributions are exponential.

A. Gaussian probability density functions

Let
                                                                                               (x−µ)2
                                           1   1 2                            1              − 2(1+σ2 )
                                   q(x) = √ e− 2 x ,       qγ (x) = p                    e                ,                  (44)
                                           2π                             2π(1 + σ 2 )
for x ∈ R, where µ and σ are both functions of γ. We assume that (µ, σ) ̸= (0, 0) for all γ > 0 (this assumption ensures that
q ̸≡ qγ ), limγ µ = 0 when µ ̸≡ 0, and limγ σ = 0 when σ ̸≡ 0.

Proposition 4.1 (Gaussian pdfs): Conditions (28)-(29) are satisfied for Gaussian pdfs q and qγ defined in (44).

The proof can be found in Appendix A.

[p.11]

Proposition 4.2: For Gaussian pdfs q and qγ given in (44),
                                                2
                                                    4
                                                       ��
                                        log γ µ2 + σ4              √                    √
                                                          , if |µ| γ ∼γ ∞ or if σ 2 γ ∼γ ∞,
                                     
                                           1 2   1 4
                                            2µ +4σ
                                     
                            n(γ) ∼γ     γ G(y)              if 12 γ(µ2 + 12 σ 4 ) ∼γ y ∈ (0, ∞),                               (45)
                                           y ,
                                                                   √               √
                                     
                                     
                                        γ,                  if |µ| γ ∼γ 0 & σ 2 γ ∼γ 0,
                                     

where G(y) is defined in (37).

Proof: We have (see e.g., [7, Example 1, p. 76])
                                                1      1     1
                                  D(qγ ||q) = µ2 + σ 2 − log(1 + σ 2 ),
                                                2      2     2
                                                    µ2          σ2      1
                                  D(q||qγ ) =              −           + log(1 + σ 2 ),
                                                2(1 + σ 2 ) 2(1 + σ 2 ) 2
yielding D(qγ ||q) ∼γ 12 µ2 + 14 σ 4 and D(q||qγ ) ∼γ 12 µ2 + 14 σ 4 . Then, (45) follows from Proposition 3.3.

Proposition 4.2 shows that an attacker is covert if either (i) 12 γ(µ2 + 12 σ 4 ) converges to a positive constant as γ → ∞, or if
        √                 √
(ii) |µ| γ ∼γ 0 and σ 2 γ ∼γ 0. Hence, covertness will occur, in particular, when (µ, σ 2 ) = (γ −δ1 , γ −δ2 ) with δ1 ≥ 21 and
δ2 ≥ 12 .
                                                                                                  √
We now focus on the √ total damage through two representative examples. We take g(x) = x and let σ = 0. In this case,
g(D(q||qγ )) ∼ |µ|/ 2. Consequently, the total damage d(γ) = n(γ)g(D(q||qγ )) is proportional to n(γ)|µ|, which corresponds
to the total mean shift introduced by the adversary prior to detection. Then, following Proposition 3.4, when γD(q||qγ ) = Θ(1),
                                √                                                                 √
which here implies µ = Θ(1/ γ), the total damage is maximized and satisfies d(γ) = Θ( γ). Similarly, if we instead set
                                                               2
µ = 0 and allow σ ̸= 0, then d(γ) is proportional to n(γ)σ , which corresponds to the total power injected by the adversary
                                                                                        √
prior to detection in a wireless communication setting. Then, under σ 2 = Θ(1/ γ), the total damage is maximized with
            √
d(γ) = Θ( γ). The same scaling law was also reported in [6] for this communication setting.

B. Exponential probability density functions

For x ≥ 0, let
                                               q(x) = λe−λx ,    qγ (x) = λγ e−λγ x ,                                          (46)
with λ > 0 and λγ > 0 for all γ > 0. We assume that λγ ̸= λ for all γ > 0 and limγ λγ = λ.

Proposition 4.3 (Exponential pdfs): Conditions (28)-(29) are satisfied for exponential pdfs q and qγ defined in (46).

The proof of Proposition 4.3 can be found in Appendix E.

Proposition 4.4: For exponential pdfs q and qγ given in (46),
                                      2 log 1 γ(1−λ /λ)2
                                             (2      γ    )     √
                                     
                                            (1−λ/λγ )2
                                                            , if γ |1 − λγ /λ| ∼γ ∞,
                           n(γ) ∼γ                              √                                                              (47)
                                         γ G(y)
                                            y ,               if γ |1 − λγ /λ| ∼γ y ∈ (0, ∞),
                                     
                                                               √
                                         γ,                   if γ |1 − λγ /λ| ∼γ 0,
where G(y) is defined in (37).

Proof: Proposition 4.4 follows from Proposition 3.3 upon noticing that
                                               �        �2                                      �      �2
                            λ    λγ − λ      1       λγ                        λγ   λ − λγ    1     λ
           D(q||qγ ) = log     +        ∼γ       1−        and D(qγ ||q) = log    +        ∼γ    1−       .
                            λγ     λ         2       λ                         λ      λγ      2     λγ
In particular, the result that D(q||qγ ) ∼γ D(qγ ||q) gives the third asymptotic in (47).
                                                                  √
We conclude from Proposition 4.4 that an attacker is covert if        γ |1 − λγ /λ| ∼γ y ∈ [0, ∞). This will occur, for instance, if
λγ = λ(1 ± γ −δ ) with δ ≥ 21 .
               √                                     λ
Taking g(x) = x, we have d(γ) ∼γ n(γ) √12 1 − λγ . The difference between the post-change and pre-change means is
|λ−1
  γ −λ
        −1
           | = λ−1
                γ |1 − λγ /λ|. Since λ is fixed and limγ λγ = λ, it follows that d(γ) is proportional to the total mean shift

[p.12]

introduced by the adversary prior to detection. Then, following Proposition 3.4, when γD(q||qγ ) = Θ(1), i.e., when the mean
                           √                                                           √
difference is of order Θ(1/ γ), the total damage is maximized and satisfies d(γ) = Θ( γ).

                                                         V. C ONCLUSION

In this work, we developed an asymptotic framework for covert quickest change detection in discrete time, analyzing the
CuSum procedure in a stationary setting where the post-change distribution qγ depends on the false-alarm constraint γ and
approaches the pre-change distribution as γ → ∞. Classical QCD analyses do not allow such γ-dependent post-change models,
and therefore cannot capture this covert regime.

We showed that standard asymptotic characterizations of detection delay fail under this dependence, and we established condi-
tions under which the overshoot of the CuSum statistic vanishes asymptotically, enabling sharp and rigorous characterizations of
both AT2FA and ADD. We further verified, in Gaussian and exponential models, that these conditions hold under convergence
of qγ to q in parameter space as γ → ∞. We also derived the scaling laws under which an adversary can preserve covertness.

A natural direction for future research is to identify structural properties of the pdfs qγ and q that would guarantee that sufficient
conditions (28) and (29), for the vanishing of the overshoots, are automatically satisfied.

Acknowledgments: The authors thank Prof. Venu Veeravalli for helpful comments and suggestions.

                                                          A PPENDIX A
                                                   P ROOF OF P ROPOSITION 4.1
                               Rx    2
The error function erf(x) = √2π 0 e−t dt ∈ [−1, 1], x ∈ R, will be used throughout. Recall that erf(−x) = −erf(x),
limx→−∞ erf(x) = −1, and limx→∞ erf(x) = 1. The asymptotic expansion [1, p. 298, 7.1.23]
                                                     2 �
                                                 e−x
                                                                �
                                                         1   1
                                    erf(x) = 1 − √         − 3 , x → ∞,                                       (48)
                                                    π x 2x
will be used repeatedly. We will use the well-known results that for any real-valued random variable U with pdf φ and u ∈ R
                                                 R∞                             Ru
                                                    tφ(t)dt                          tφ(t)dt
                                                  u
                                 E[U | U ≥ u] = R ∞          , E[U | U ≤ u] = R−∞ u          ,
                                                  u
                                                     φ(t)dt                       −∞
                                                                                      φ(t)dt
so that
                                                               R∞
                                                                  (t − u)φ(t)dt
                                             E[U − u | U ≥ u] = u R ∞           ,                                                (49)
                                                                   u
                                                                      φ(t)dt
                                                               Ru
                                                                   (t − u)φ(t)dt
                                             E[U − u | U ≤ u] = −∞Ru              .                                              (50)
                                                                   −∞
                                                                       φ(t)dt

                                  γ q (X)
Denote by fp the pdf of Y = log q(X)   , with X a real-valued rv with Gaussian pdf p ∈ {q, qγ }, q and qγ given in (44). The
pdf fp is given in (84) in Appendix B.

We are now in position to prove the validity of conditions (28) and (29) in Proposition 4.1. In each case, we will treat separately
the cases σ ≡ 0 and σ ̸≡ 0. Throughout p ∈ {q, qγ }.

A. Proof that (28) holds for Gaussian pdfs

1) Case when σ ≡ 0: The latter implies that µ ̸≡ 0 as, by assumption, we cannot have simultaneously σ ≡ 0 and µ ≡ 0. By
(49) and (84), for y ≥ 0,
                                                          R∞              1 z   µξp 2

                                                            y
                                                              (z − y)e− 2 ( µ − 2 ) dz
                                    Ep [Y − y | Y ≥ y] =      R ∞ − 1 ( z − µξp )2
                                                               y
                                                                  e 2 µ 2 dz
                                                                 �               �
                                                                    y      |µ|ξp
                                                        = |µ|∆1        −           ,                               (51)
                                                                   |µ|       2

[p.13]

where
                                                                 R∞               1 2
                                                                 (t − x)e− 2 t dt
                                                                 x
                                                     ∆1 (x) :=   R ∞ − 1 t2       ,
                                                                  x
                                                                     e 2 dt
                                                              √ − 1 x2      √
                                                               2e 2 − x π(1 − erf( √x2 ))
                                                            =       √                     .                               (52)
                                                                      π(1 − erf( √x2 ))

Lemma A.1: The mapping x → ∆1 (x) is non-increasing in R.

Proof: We have
                                                                             Γ(x)
                                                            ∆′1 (x) =                      ,                              (53)
                                                                        π(1 − erf( √x2 ))2
                      2 √                      1 2                                                              √
with Γ(x) := −π + 2e−x − 2πx(1 − erf( √x2 ))e− 2 x − πerf( √x2 )(erf( √x2 ) − 2), and Γ′ (x) = Φ(x) with Φ(x) := 2π(x2 +
                             1       2
1)(1 − erf( √x2 )) − 2xe− 2 x . Since erf(x) ∈ [−1, 1] for all x ∈ R, obviously Φ(x) ≥ 0 for x ≤ 0. Assume that now that
                                                     2                                                � 2      √    �
                                                2e−x                                              1 2             2
x > 0. By using the bound 1 − erf(x) ≥ √π(x+      √
                                                    x 2 +2)
                                                            (x > 0) [1, 7.1.13] we get Φ(x) ≥ 2e− 2 x x +2−x
                                                                                                          x+
                                                                                                             √ x +4
                                                                                                              x2 +4
                                                                                                                      ≥ 0
                              2
                                        √
since it is easily seen that x + 2 − x x2 + 4 ≥ 0 for all x ∈ R. This shows that Γ(x) is non-decreasing on R. But since
limx→∞ Γ(x) = 0 (Hint: limx→∞ erf(x) = 1), we conclude that Γ(x) ≤ 0 for all x ∈ R, which in turn proves from (53) that
∆1 (x) in non-increasing in R.



By (51) and Lemma A.1, y → Ep [Y − y | Y ≥ y] is non-increasing in [0, ∞), Therefore,
                                                0 ≤ lim sup Ep [Y − y | Y ≥ y] ≤ lim Ep [Y | Y ≥ 0]
                                                    γ→∞ y≥0                             γ

                                                                   |µ|ξp
                                                  = lim |µ|∆1 (−         ) = 0,
                                                    µ→0              2
                             q
                                 2
since limx→0 ∆1 (x) =            π       (Hint: erf(0) = 0). This proves (28) when µ ̸= 0 and σ = 0.

2) Case when σ ̸≡ 0: By (84) and (49), for y ≥ 0 (Hint: δ < 0 so that max{y, δ} = y),
                                                         R ∞ t−y                   R∞
                                                           y
                                                                √      ρ (t)dt + y √t−y
                                                                   t−δ 1
                                                                                                ρ2 (t)dt
                                  Ep [Y − y | Y ≥ y] = R ∞ 1                       R ∞ t−δ  1
                                                                                                         ,                (54)
                                                            y
                                                                 √     ρ (t)dt + y √t−δ ρ2 (t)dt
                                                                    t−δ 1
                                                                                             √
                                                                                     τ χ + ν(t−δ)
where ρ1 (t) and ρ2 (t) are defined in (85). With the change of variable v = p √χp                    , we find
                      Z ∞                        √ Z ∞
                            t−y                2 χp                         √              2
                                                                                                               1
                                                                                                             − 2 v2
                           √       ρ1 (t)dt = √                √        ((v   χ p − τ χ p )   − ν(y  −  δ)) e       dv,
                       y     t−δ                ν ν τ χp +√χν(y−δ)
                                                                 p
                            Z ∞                  √ Z
                                  ρ1 (t)       2 χp ∞                       1 2
                                 √       dt = √                √        e− 2 v dv.
                             y     t−δ            ν    τ χ p +
                                                              √
                                                                 ν(y−δ)
                                                                χp
                                                  √
                                             τ χ − ν(t−δ)
Similarly, with the change of variable v = p √χp             , we find
                                                                        √
                       Z ∞                         √ Z τ χp −√χν(y−δ)
                                 t−y             2 χp          p         √                            1 2
                                 √     ρ2 (t)dt = √                   ((v χp − τ χp )2 − ν(y − δ)) e− 2 v dv,
                         y         t−δ            ν ν −∞
                                                             √
                                 Z ∞               √ Z τ χp −√χν(y−δ)
                                      ρ (t)      2 χp          p         1 2
                                     √2      dt = √                   e− 2 v dv.
                                  y    t−δ          ν −∞

[p.14]

Putting the pieces together, we obtain for y ≥ 0
                                                                        √
                                                               R τ χp −√χν(y−δ)            1 2
                                              χp                −∞
                                                                         p
                                                                                H(v, y)e− 2 v dv
                        Ep [Y − y | Y ≥ y] =
                                                 
                                                           √
                                               ν  R τ χp −√χν(y−δ)
                                                 
                                                                         1 2      R∞                  1 2
                                                     −∞
                                                              p
                                                                      e− 2 v dv + τ χp −√ν(y−δ) e− 2 v dv
                                                                                        √
                                                                                          χp
                                                                                                      
                                                      R∞ √                         1 2
                                                                                 −2v
                                                        τ χp + ν(y−δ) H(v, y)e         dv
                                                              √
                                                                                                      
                                                                χp
                                           + τ χ − ν(y−δ)                                             ,                (55)
                                                                                                      
                                                   √
                                                 p
                                                   √             1          R∞ √              1       
                                                    χp         − 2 v2                       − 2 v2
                                             R
                                              −∞             e        dv + τ χp − ν(y−δ) e         dv
                                                                                          √
                                                                                              χp

                       √
with H(v, y) := (v − τ χp )   2
                                  − ν(y−δ)
                                      χp . With the mapping
                                      R θ−x                1 2    R∞                      1 2
                                        ((v − θ)2 − x2 )e− 2 v dv
                                       −∞                          θ+x
                                                                       ((v − θ)2 − x2 )e− 2 v dv
                       J(x, θ) := R                R ∞ − 1 v2 + R θ−x − 1 v2      R ∞ − 1 v2 ,                          (56)
                                    θ−x − 1 v 2
                                   −∞
                                       e  2 dv +
                                                    θ+x
                                                         e  2 dv
                                                                  −∞
                                                                      e   2 dv +
                                                                                   θ+x
                                                                                        e 2 dv
formula (55) rewrites, for y ≥ 0,
                                                                             s                         !
                                                            σ 2 χp               ν(y − δ) √
                                     Ep [Y − y | Y ≥ y] =             J                  , τ χp            .            (57)
                                                          2(1 + σ 2 )               χp
Hence,
                                                                σ 2 χp
                                                                                    �             �
                                                                                           τ χp
                               sup Ep [Y − y | Y ≥ y] =                     sup   J   x, √          .                   (58)
                               y≥0                            2(1 + σ 2 ) x≥q− νδ          1 + σ2
                                                                                 1+σ 2


Routine algebra shows that
                                         r                1       2                   1            2
                                             2 (x + θ)e− 2 (x−θ) + (x − θ)e− 2 (x+θ)
                             J(x, θ) =         ·            �     �      �     �     + θ2 − x2 + 1.                     (59)
                                             π      2 − erf √ x−θ
                                                                    − erf √x+θ
                                                                  2               2

Note that
                                               J(x, θ) = J(x, −θ),     ∀x ∈ R, ∀θ ∈ R,                                  (60)
so that, by (57) and the definition of ν, δ, and χp in (86) and (87), we see that Ep [Y − y | Y ≥ 0] does not depend on the
sign of µ, or equivalently, on the sign of τ (= µ/σ 2 ).

We now show that limγ supy≥0 Ep [Y − y | Y ≥ y] = 0. To achieve this, we distinguish between the cases (recall that τ = σµ2 )
a) −∞ < lim inf γ τ ≤ lim supγ τ < ∞ and b) limγ τ = ±∞.

a) Case when −∞ < lim inf γ τ ≤ lim supγ τ < ∞:
                                                                  √
In this case |τ | is bounded, say by a constant η2 > 0, so that |τ χp | < 2η2 for γ large �q               � of χp in (87).
                                                                                           enough by definition
                                                                                              ν(y−δ)  √
Therefore, there exists γ0 > 0 such that for all γ > γ0 the arguments of the mapping J          χp , τ χp are contained in
the set [0, ∞) × [−2η2 , 2η2 ] when y ≥ 0. Since limx→0 J(x, θ) = 0 (Hint: use L’Hôpital’s rule) and limx→∞ J(x, θ) = 2
(cf. Lemma A.2) below), we deduce that, for all γ > γ0 , |J(x, θ)| is bounded, say by a constant C1 > 0, for all (x, θ) ∈
[0, ∞) × [−2η2 , 2η2 ]. Hence,
                                                                              σ 2 χp
                                    0 ≤ lim sup Ep [Y − y | Y ≥ y] ≤ C1 lim             = 0,
                                          γ y≥0                           γ 2(1 + σ 2 )

which proves (28).

Lemma A.2: For any θ ∈ R, limx J(x, θ) = 2.

[p.15]

Proof: Applying (48) to (59) yields
                                                      1      2
                                                               �                          �                   ��
                                                 e− 2 (x−θ) x + θ + (θ2 − x2 + 1) x−θ         1         1
                                                                                                  − (x−θ)   3
                                  J(x, θ) ∼x      1       2
                                                            �                 �      1       2
                                                                                               �                    �
                                                                1       1                          1          1
                                             e− 2 (x−θ) x−θ        − (x−θ)  3   + e− 2 (x+θ) x+θ      − (x+θ)     3

                                                    1      2
                                                             �                          �                   ��
                                              e− 2 (x+θ) x − θ + (θ2 − x2 + 1) x+θ          1         1
                                                                                                − (x+θ)   3
                                          +    1        2
                                                          �                 �      1       2
                                                                                             �                    �.    (61)
                                                              1       1                          1          1
                                            e− 2 (x−θ) x−θ        − (x−θ) 3   + e− 2 (x+θ) x+θ       − (x+θ)    3


                                                                                                       1       2
Assume that θ ≥ 0. Multiplying both the numerator and the denominator in (61) by e 2 (x−θ) yields
                                             �               �        �                       �               ��
                    x + θ + (θ2 − x2 + 1) x−θ   1      1
                                                   − (x−θ)3      e−2xθ x − θ + (θ2 − x2 + 1) x+θ 1       1
                                                                                                   − (x+θ)  3
         J(x, θ) ∼x                          �               �+                            �              �      ,
                     1        1         −2xθ    1       1             1      1        −2xθ    1      1
                    x−θ  −  (x−θ)3 +  e        x+θ − (x+θ) 3         x−θ − (x−θ)3 + e        x+θ − (x+θ)3
                                             �               �
                               2     2          1      1
                    x + θ + (θ − x + 1) x−θ − (x−θ)3
                 ∼x                1         1                 ,
                                  x−θ − (x−θ)3
                         2x2 − 2θx − 1
                   =                             ∼x 2.
                       x2 − 2θx + θ2 − 1
Thanks to (60) the lemma also holds when θ < 0, which concludes the proof.

b) Case when limγ τ = ±∞:

As observed earlier (see comment below (60)), Ep [Y − y | Y ≥ y] does not depend on the sign of µ (or τ ). We will therefore
assume, without loss of generality, that limγ τ = ∞.
                                                                                   √
Proposition A.1: For any θ ≥ √32 , the mapping x → J(x, θ) is non-increasing in [1/ 2, ∞).

The proof of Proposition A.1 can be found in Section C below.
           q                                                                   q
                 νδ                   τχ                                                           τ χp
Since limγ − 1+σ    2 = ∞ and limγ
                                    √ p = ∞, there exists γ0 > 0 such that       − νδ 2 ≥ √12 and √1+σ  ≥ √32 for γ > γ0 .
                                      1+σ 2
                                                                              √ 1+σ                √ 2
Hence, (58) and the fact that the mapping x → J(x, θ) is non-increasing in [1/ 2, ∞) for all θ ≥ 3/ 2, which follows from
(88) and Proposition A.1, yield
                                                                         s             !
                                                             σ 2 χp           νδ √
                                  sup Ep [Y − y | Y ≥ y] ≤             J   − , τ χp .
                                  y≥0                      2(1 + σ 2 )        χp
                            p χ     1
for γ > γ0 . Since limγ 2(1+σ 2 ) = 2 , the proof is concluded by applying Lemma A.3 below.



Lemma A.3: If limγ τ = ∞,                                            s                  !
                                                              2          νδ √
                                                         lim σ J        − , τ χp            = 0.
                                                          γ              χp

                                                                               √        √
                       q              q
                                          1+σ 2 µ2    log(1+σ 2 )
Proof. Define x0 :=        − χνδp =        χp ( σ 4 +     σ2      ) and θ0 := τ χp = σµ2 χp . Since
                                                              (
                                                                  µ2 − log(1 + σ 2 ) + σ 2 ,        if p = qγ ,
                                     σ (θ02 − x20 + 1) =
                                      2
                                                                     µ2               2      2
                                                                  − 1+σ 2 − log(1 + σ ) + σ ,       if p = q,

we see that σ 2 (θ02 − x20 + 1) ∼γ 0 for p ∈ {q, qγ }. Therefore, from (59),
                                             r                     1         2                   1        2
                              2                2 σ 2 (x0 + θ0 )e− 2 (x0 −θ0 ) + σ 2 (x0 − θ0 )e− 2 (x0 +θ)
                            σ J(x0 , θ0 ) ∼γ     ·                   �         �      �       �             .           (62)
                                               π             2 − erf x0√−θ0 − erf x0√+θ0
                                                                                    2                 2

[p.16]

Until this end of this proof we assume that γ is large enough so that µ > 0, which is justified by the assumption that
limγ τ = ∞. We have, using again the definition of χp in (87),
                                s                                          !     ( 2
                                                                                    σ    µ
                                   1 + σ2       1 log(1 + σ 2 )                     2µ − 2 ∼γ 0, if p = qγ ,
                                           �                     �
                                                                     √
                 x0 − θ 0 = τ                1+ 2                  −   χ p   ∼ γ    σ 2                                (63)
                                      χp       τ        σ2                          2µ ∼γ 0,     if p = q,
                                  2         √                                     2
where we have used that log(1+σ
                              σ2
                                    )
                                      ∼γ 1, 1 + x = 1 + 12 x + o(x), and limγ σµ = limγ τ1 = 0 by assumption. Similarly, we
find
                                                                  2µ
                                                   x0 + θ0 ∼γ 2 ∼γ ∞,                                                  (64)
                                                                  σ
yielding
                                                  σ 2 (x0 + θ0 ) ∼γ 2µ ∼γ 0.                                           (65)
                                                                                                        √
By (63)-(65) as γ → ∞, the numerator in the r.h.s of (62) goes to zero while the denominator goes to π. As a result, the
r.h.s of (62) converges to zero as γ → ∞, which completes the proof of the lemma.

B. Proof that (29) holds for Gaussian pdfs

1) Case when σ ≡ 0: In this section σ ≡ 0, so that µ ̸≡ 0. By (50) and (84), for y ≤ 0,
                                                           Ry                1 z   µξp 2

                                                            −∞
                                                                (z − y)e− 2 ( µ − 2 ) dz
                                  Ep [Y − y | Y ≤ y] =        Ry       1 z     µξp 2     ,
                                                                −∞
                                                                    e− 2 ( µ − 2 ) dz
                                                                 �                �
                                                                    y       |µ|ξp
                                                       = |µ|∆2         −             ,                                 (66)
                                                                   |µ|        2
where
                                                        Rx              1 2
                                                        −∞
                                                              (t − x)e− 2 t dt
                                            ∆2 (x) :=        Rx 1 2     ,
                                                             e− 2 t dt
                                                             −∞
                                                     √ − 1 x2      √ �     � ��
                                                      2e 2 + x π 1 + erf √x2
                                                   =      √ �          � ��     .                                      (67)
                                                             π 1 + erf √x2


We observe that ∆2 (x) = ∆1 (−x), where ∆1 (x) is given in (52). Therefore, by Lemma A.1, we see that x → ∆2 (x) is
non-decreasing in R.

Consequently,
                                    inf Ep [Y − y | Y ≤ y] ≥ lim Ep [Y − y | Y ≤ y],
                                    y≤0                      y→−∞
                                                                        �             �
                                                                           y    |µ|ξp
                                                           = |µ| lim ∆2       −         = 0,
                                                                y→−∞      |µ|     2
as7 limx↓−∞ ∆2 (x) = 0. Consequently, limγ inf y≤0 Ep [Y − y | Y ≤ y] = 0, which proves (29) when µ ̸≡ 0 and σ ≡ 0.

2) Case when σ ̸≡ 0: Since Ep [Y − y | Y ≤ y]= Ep [(Y − y)1{Y ≤y} | Y ≤ y], by (50) and (84) we see that Ep [Y − y | Y ≤
y] = 0 for y ∈ (−∞, δ], so that (29) reduces to showing that
                                                  lim    inf Ep [Y − y | Y ≤ y] = 0.                                   (68)
                                                 γ→∞ δ<y≤0

For δ < y ≤ 0, we have from (50) and (84)
                                                             R y t−y              y
                                                                       ρ (t)dt + δ √t−y
                                                                                 R
                                                              δ
                                                                 √
                                                                   t−δ 1
                                                                                        ρ2 (t)dt
                                     Ep [Y − y | Y ≤ y] =     Ry 1              R y t−δ
                                                                                     1
                                                                                                 ,                     (69)
                                                               δ
                                                                 √     ρ (t)dt + δ √t−δ
                                                                    t−δ 1
                                                                                        ρ2 (t)dt
                            √ − 1 x2   √
                             2e 2    +x π(1−erf( −x
                                                 √ ))
 7 Write ∆ (x) as ∆ (x) =
          2        2            √
                                                  2
                                                      and use (48) to get ∆2 (x) ∼ 1 1 ∼ 0 as x → −∞.
                                   π(1−erf( −x
                                            √ ))
                                                                                   x
                                                                                     −x
                                            2

[p.17]

where ρ1 (x) and ρ2 (x) are defined in (85) and δ is defined in (86).

By duplicating the derivation of (55), we easily find that, for δ < y ≤ 0,
                                        √                     1 2                                                             √
                               χp � R τ χp
                                                    H(v, y)e− 2 v dv
                                                                                                                     τ χp +       ν(y−δ)
                                            √                                                                 χp � R     √                               1   2
                                                                                                                                            H(v, y)e− 2 v dv
                               ν      τ χp − ν(y−δ)                                                                        χp
                                               √                                                                      √
                                                χp                                                            ν      τ χp
 Ep [Y − y | Y ≤ y] =                                              √                           +                                                   √                               ,
                        R τ √χp                1
                                             − 2 v2
                                                          R τ χp +√χν(y−δ)
                                                                    p
                                                                                   1
                                                                                 − 2 v2
                                                                                                    R τ √χp             1
                                                                                                                      − 2 v2
                                                                                                                                            R τ χp +√χν(y−δ)
                                                                                                                                                      p
                                                                                                                                                                       1
                                                                                                                                                                     − 2 v2
                              √
                         τ χp − ν(y−δ)
                                         e            dv + τ √χp             e            dv              √
                                                                                                     τ χp − ν(y−δ)
                                                                                                                     e            dv + τ √χp                     e            dv
                               √                                                                           √
                                χp                                                                           χp

                                                                                                                                                                              (70)
                       √
where H(v, y) := (v − τ χp )2 − ν(y−δ)
                                  χp . With the mapping
                                     Rθ                       1 2                               1 2
                                          ((v − θ)2 − x2 )e− 2 v dv
                                                                       R θ+x
                                         θ−x                            θ
                                                                             ((v − θ)2 − x2 )e− 2 v dv
                        G(x, θ) := R         1         R θ+x − 1 v2 + R θ      1         R θ+x − 1 v2 ,                                                                       (71)
                                     θ     − 2 v2                            − 2 v2
                                     θ−x
                                         e        dv +  θ
                                                            e  2 dv
                                                                       θ−x
                                                                           e        dv +  θ
                                                                                              e 2 dv
the conditional expectation Ep [Y − y | Y ≤ y] in (69) rewrites
                                                                                          s                          !
                                                          σ 2 χp                               ν(y − δ) √
                                   Ep [Y − y | Y ≤ y] =             G                                  , τ χp            ,                                                    (72)
                                                        2(1 + σ 2 )                               χp
for δ < y ≤ 0. Hence,
                                                                                                          s                         !
                                                           1                                                     νδt √
                           0 ≥ lim inf Ep [Y − y | Y ≤ y] = lim inf σ 2 G                                      −    , τ χp              ,                                     (73)
                                 γ δ<y≤0                   2 γ 0<t≤1                                             χp
            χ
since limγ 1+σp 2 = 1 from the definition of χp . Standard algebra gives
                                       r                1     2              1   2
                                          2 (θ − x)e− 2 (θ+x) − (θ + x)e− 2 (θ−x)
                           G(x, θ) =        ·           �     �       �     �      + θ2 − x2 + 1.                                                                             (74)
                                         π           erf √θ+x
                                                                − erf √ θ−x
                                                                       2                       2

Notice that G(x, θ) = G(x, −θ), which implies from (72), that Ep [Y − y | Y ≤ y] does not depend on the sign of τ or,
equivalently, on the sign of µ since τ = σµ2 .

Like in Section A-A we will distinguish the case (a) −∞ < lim inf γ τ ≤ lim supγ τ < ∞ from the case (b) limγ τ = ±∞.

a) Case when −∞ < lim inf γ τ ≤ lim supγ τ < ∞:
                                                                       √
In this case |τ | is bounded, say by a p   constant η2 > 0, so that |τ χp | < 2η2pfor γ large enough by definition of χp in (87).
On the otherqhand, forqδ ≤ y ≤ 0, ν(y − δ)/χp lies in the interval [0, −νδ/χp ]. For γ large enough, this interval is
                                          log(1+σ 2 )                                                                       2
                                                      ) ≤ 2(η22 + 1) := η1 by using that log(1+x)
                                 2
                                                         p
bounded as − χνδp = 1+σ             2
                              χp (τ +         σ2                                             x    ≤ 1 for all x ≥ 0 and 1+σ
                                                                                                                         χp ≤ 2
                                                                             p                 √
for γ large enough. Therefore, for γ large enough, the arguments of G( ν(y − δ)/χp , τ χp ) take values in the compact set
[0, η1 ] × [−2η2 , 2η2 ] for all y ∈ [δ, 0]. Since the mapping (x, θ) → G(x, θ) is continuous on R × R, by the extreme value
theorem, |G(x, θ)| is p  bounded on any compact set of R × R, which implies that, for γ large enough, there exists a constant
                                            √
C1 > 0 such that |G( ν(y − δ)/χp , τ χp )| < C1 for any y ∈ [δ, 0]. Hence, by (73),
                                                                                                   C1
                                         0 ≥ lim inf Ep [Y − y | Y ≤ y] ≥                             lim σ 2 = 0.
                                                  γ δ≤y≤0                                          2 γ

b) Case when limγ τ = ±∞:

As noted earlier, Ep [Y − y | Y ≤ y] does not depend on the sign of τ . We may therefore assume, without loss of generality,
that limγ τ = ∞. The latter implies that τ > 0 for large enough, which we will assume from now on.

Proposition A.2: For any θ ≥ 0, the mapping x → G(x, θ) is non-increasing in [0, ∞).

The proof of Proposition A.2 can be found in Section D below.

[p.18]

Combining (73) and Proposition A.2 yields
                                                                                                   s               !
                                                                 1                                      νδ √
                                     lim inf Ep [Y − y | Y ≤ y] = lim σ 2 G                            − , τ χp         .           (75)
                                       γ δ<y≤0                   2 γ                                    χp
The proof that condition (29) holds for Gaussian pdfs when limγ τ = ∞ then follows from the lemma below.

Lemma A.4: If limγ τ = ∞ then                                         s                    !
                                                             2             νδ √
                                                      lim σ G             − , τ χp             = 0.
                                                       γ                   χp

                         q                     √
Proof. Define x0 :=          − χνδp and θ0 := τ χp . As established in the proof of Lemma A.3, σ 2 (θ02 − x20 + 1) ∼γ 0, x0 − θ0 ∼γ 0,
x0 + θ0 ∼γ ∞, and σ 2 (x0 + θ0 ) ∼γ 0, so that (cf. (74)),
                                        r                    1          2                   1           2
                                          2 σ 2 (θ0 − x0 )e− 2 (θ0 +x0 ) − σ 2 (θ0 + x0 )e− 2 (θ0 −x0 )
                      σ2 G(x0 , θ0 ) ∼γ                      �         �        �      �                  ∼γ 0,
                                          π               erf θ0√+x0 − erf θ0√−x0
                                                                                2                      2

by using that limx→∞ erf(x) = 1 and limx→0 erf(x) = 0, so that the denominator goes to one while the numerator goes to
zero as γ → ∞.

                                                           A PPENDIX B
                                                                                   qγ (X)
                                          P ROBABILITY DENSITY FUNCTION OF Y = log q(X)

                                                      (x−µ)2
                     1   2                           −                               q (X)
Let q(x) = √12π e− 2 x , qγ (x) = √         1
                                                    e 2(1+σ2 ) , and Y           γ
                                                                           = log q(X) . We denote by fp the pdf of Y under p ∈ {q, qγ }.
                                         2π(1+σ 2 )

                              e2 = 1 + σ 2 . We first determine fqγ . We have
Assume first that σ ̸≡ 0. Set σ
                                                       Z
                                                 1          (z−µ)2
                              Pqγ (Y < x) = √             e− 2σe 2 1{− 1 log σe2 −( (z−µ)2 − 1 z2 )<x} dz.                          (76)
                                                2πe  2
                                                   σ R                  2              e2
                                                                                      2σ     2


We observe from (76) that
                                                           µ2 σ
                                                              e2      σ2
                                                                          �                  �
                                                                    2e            1        2
                                   Pqγ (Y < x) = 0 if             + 2 x + log σ           e ≤ 0,
                                                            σ4       σ            2
or, equivalently,
                                                       Pqγ (Y < x) = 0              if     x ≤ δ,                                   (77)
                 2
              µ     1
where δ := − 2σ           e2 ≤ 0. When x > δ, with
                2 − 2 log σ


                                                      σ2
                                                     2e                 µ                    p
                                              ν :=       ,       τ :=      ,       ρ(x) :=       ν(x − δ),
                                                     σ2                 σ2
we obtain from (76)
                                                                          Z
                                                                  1                                    (z−µ)2
                                          Pqγ (Y < x) = √                      1{|z+τ |<ρ(x)} e− 2σe 2 dz,
                                                               2πeσ2 R
                                                                     Z −τ +ρ(x)
                                                                1                 (z−µ)2
                                                           = √                  e− 2σe 2 dz.                                        (78)
                                                               2πeσ 2 −τ −ρ(x)
In summary (cf. (77), (78)),
                                                                                                           for x ≤ δ,
                                                      
                                                       0,            Z −τ +ρ(x)
                                     Pqγ (Y < x) =                                        (z−µ)2                                    (79)
                                                          1                              − 2σ
                                                       √2πeσ2
                                                                                     e       e2    dz,     for x > δ.
                                                                        −τ −ρ(x)

From (79) we get
                                                                          (
                                                d                              0,                          for x ≤ δ,
                                     fqγ (x) =    Pq (Y < x) =                  ν(e
                                                                                √ρ1 (x)+eρ√2 (x))2 ,       for x > δ,               (80)
                                               dx γ                            2    ν(x−δ) 2πe
                                                                                             σ

[p.19]

                      (τ +µ−ρ(x))2                            (τ +µ+ρ(x))2
where ρe1 (x) := e−         e2
                           2σ        and ρe2 (x) := e−  . When σ ≡ 0 and µ ̸≡ 0,
                                                                    e2
                                                                   2σ

                                                                              µ
                                                                           x

                               1
                                  Z
                                                    1       2
                                                                    √1 R µ + 2 e− 12 (z−µ)2 dz, if µ > 0,
                                                  − 2 (z−µ)                −∞
                Pqγ (Y < x) = √     1    µ2     e             dz =    2π
                                                                    √1 x∞+ µ e− 2 (z−µ) dz, if µ < 0,
                                                                                  1       2
                                2π R {µz− 2 <x}
                                                                         R
                                                                      2π                        µ        2


for all x ∈ R, yielding
                                                  d                  1    1 x     µ 2
                                     fqγ (x) =      Pqγ (Y < x) =    √ e− 2 ( µ − 2 ) dx,                      ∀x ∈ R.   (81)
                                                 dx               |µ| 2π
We now calculate fq . When σ ̸≡ 0, mimicking the derivation of (79), we find
                                               (
                                                  0,                         for x ≤ δ,
                                 Pq (Y < x) =     √1
                                                       R −τ +ρ(x) − 1 z2
                                                    2π −τ −ρ(x)
                                                                 e  2    dz, for x > δ,
yielding                                             � 1                               �
                                                                    2     1          2
                                                    ν e− 2 (τ +ρ(x)) + e− 2 (τ −ρ(x))
                                           fq (x) =           p         √                1{x>δ} .                        (82)
                                                            2 ν(x − δ) 2π
Finally, for µ ̸≡ 0 and σ ≡ 0, we readily get
                                                                    1    1 x     µ 2
                                                 fq (x) =           √ e− 2 ( µ + 2 ) dx,      ∀x ∈ R.                    (83)
                                                                 |µ| 2π
Pdfs in (80)-(83) can be represented by the unified formula
                                         
                                                          α(ρ1 (x)+ρ2 (x))
                                          1{x>δ} 2√α(x−δ)√2π(1+σ2 ) ,
                                                                                            if σ ̸= 0,
                                fp (x) =               1 x µξp                                                           (84)
                                               1     − 2 ( µ − 2 )2
                                               √   e                ,                        if µ ̸= 0, σ = 0,
                                         
                                         
                                            |µ| 2π

for x ∈ R, where
                                                                    √                               √
                                                          (τ χp +    ν(x−δ))2             (τ χp −       ν(x−δ))2
                                                      −                               −
                                       ρ1 (x) := e                , ρ2 (x) := e
                                                                    2χp            2χp
                                                                                            ,                            (85)
                                                     2                        2
                                             2(1 + σ )          µ            µ   1
                                       ν :=        2
                                                       , τ := 2 , δ := − 2 − log(1 + σ 2 ),                              (86)
                                                 σ             σ            2σ � 2
                                                 1 + σ 2 , if p = qγ ,
                                              �
                                                                                1,   if p = qγ ,
                                       χp :=                             ξp :=                                           (87)
                                                 1,        if p = q,            −1, if p = q.

                                                            A PPENDIX C
                                            P ROOF OF P ROPOSITION A.1 IN S ECTION A-A2
                                                                           √
We want to show (cf. Remark C.1) that x → J(x, θ) in non-increasing in [1/ 2, ∞) when θ ≥ √32 , where J(x, θ) is given
in (59). We have
                                   ∂                         Q(x, θ)
                                     J(x, θ) = �                                ���2 ,                            (88)
                                  ∂x
                                                      � �        �       �
                                              π 2 − erf θ+x  √
                                                               2
                                                                   − erf   θ−x
                                                                            √
                                                                              2

with
                                                  2       2                     2                              2
               Q(x, θ) := −8πx + 4xe−θ −x + 2(θ + x)e−(θ−x) − 2(θ − x)e−(θ+x)
                         √
                                         �                       ��    � �        �       �       ���
                              2    2
                                             (θ+x)2
                                           − 2          −
                                                          (θ−x)2             θ+x             θ−x
                       + 2π(θ − x + 1) e             +e      2     2 − erf    √     − erf     √
                                                                                2               2
                            � �         �       �       ��         � �        �       �       ��2
                                  θ+x             θ−x                   θ+x             θ−x
                       + 8πx erf    √     − erf     √        − 2πx erf   √      − erf    √        .                      (89)
                                      2               2                    2               2

[p.20]

Substituting x by u−v
                  √
                    2
                       and θ by u+v
                                 √
                                   2
                                     in (89) (notice that necessarily u ≥ v since x ≥ 0), we obtain
                                          √                 √                      √             √
                   �              �
                      u−v u+v                                             2   2            2        2
                 Q     √ , √         = −4 2π(u − v) + 2 2(u − v)e−u −v + 2 2ue−2v − 2 2ve−2u
                         2     2
                                       √               �    2       2
                                                                      �
                                     + 2π(2uv + 1) e−u + e−v (2 − (erf(u) − erf(v)))
                                        √                                √
                                     + 4 2π(u − v)(erf(u) − erf(v)) − 2π(u − v)(erf(u) − erf(v))2 ,
                                       √
                                     ≤ 2V (u, v),                                                                             (90)
for u ≥ v, where
                                                           2   2        2            2
              V (u, v) := − 4π(u − v) + 2(u − v)e−u −v + 2ue−2v − 2ve−2u
                            √            �   2      2
                                                      �
                          + π(2uv + 1) e−v + e−u (2 − (erf(u) − erf(v)) + 4π(u − v)(erf(u) − erf(v)).                         (91)

Remark C.1: The reader may legitimately wonder why we do not show that x → J(x, θ) is non-increasing in [0, ∞) when
θ ≥ 0. Actually, this result is not correct, as Q(x, θ) in (88) can be positive for x ≥ 0 and θ ≥ 0. For instance, Q(0, 1) ≈ 12.16.
                                                                                                                                √
However, numerical
           √          results clearly indicate, for instance, that Q(x, θ) is negative for x ≥ 0 and θ ≥ 4 as well as for x ≥ 1/ 2
and θ ≥ 3/ 2. It will be more convenient to show the latter, thereby explaining the statement in Proposition A.1.

Lemma C.1: For any x ≥ √12 and θ ≥ √32 one can always find u and v such that x = u−v
                                                                                 √ , θ = u+v
                                                                                   2
                                                                                         √ , v ≥ 1 and u ≥ v + 1.
                                                                                           2

Proof: x = u−v
           √
             2
               and θ = u+v
                       √
                         2
                           give u = θ+x
                                     √
                                       2
                                         and v = θ−x
                                                  √ . We have
                                                   2

                                                             u−v   1
                                                           x= √ ≥ √ ,
                                                               2    2
                                                                                 3
                                                                                √    + √1
yielding u ≥ v + 1. It remains to check that v ≥ 1. We have u = θ+x  √
                                                                       2
                                                                         ≥ 2√2 2 = 2, which coupled with the inequality
u ≥ v + 1 obtained above, necessarily implies that v ≥ 1. This concludes the proof of the claim.

As a result, Proposition A.1 will hold if the following proposition is true:

Proposition C.1: For any v ≥ 1, V (u, v) ≤ 0 for u ≥ v + 1.

The rest is this section devoted to the proof of Proposition C.1.

We have
           d                    2  2    √                                  2    √                    2
             V (u, v) = −4u2 e−u −v + 2 π(erf(u) − erf(v))(2vu2 + u − v)e−u − 4 π(2vu2 − u + v)e−u
          du
                          √                         2                2                                  2
                      − 2v π(erf(u) − erf(v) − 2)e−v + 2(2uv − 1)e−2u + 4π(erf(u) − erf(v)) − 4π + 2e−2v ,

                                                           √
                  �              �                             ��         �                           �
              d        d                       −u2 −v 2                 1                                 2
                         V (u, v) = − 4(u − v)e         +4 π        2
                                                                   u −      (erf(u) − erf(v)) − 2u − 1 e−u
                                                                                                  2
             dv       du                                                2
                                       √
                                           ��         �                             �
                                                    1                                     2         2       2
                                    +4 π      v2 −      (erf(u) − erf(v)) − 2v 2 − 1 e−v + 4ue−2u − 4ve−2v ,
                                                    2

                                                 d2
                                                       �              �
                                                            d               2
                                                              V (u, v) = e−v K(u),                                            (92)
                                                dv 2       du
with
                                                           √
                                                          �    ��       �                           �          �
                             2         2       −u2                 2  3                         2         −v 2
            K(u) :=8(−u + uv − v + 1)e               − 8v    π    v −     (erf(u) − erf(v)) − 2v + 1 − ve        .
                                                                      2
Differentiating K(u) w.r.t. u gives
                                                d              2
                                       K ′ (u) := K(u) = 16e−u (u − v)(u2 + v 2 − 2).
                                               du
                                                       √               √
We observe that K ′ (u) vanishes at u = v, and at u = − 2 − v 2 and u = 2 − v 2 when v 2 ≤ 2.

[p.21]

                    √
Assume that v ≥ 2. Then, K ′ (u) ≥ 0 for all u ≥ v. Therefore, the mapping u → K(u) is increasing, in particular, in
[v + 1, ∞), yielding K(u) ≥ K(v + 1) for all u ≥ v + 1.
                               √                   √
Assume now that 1 ≤ v < 2. Notice that v ≥ 2 − v 2 in this case, so that K ′ (u) ≥ 0 for u ≥ v. Hence, u → K(u) is
increasing, in particular, in [v + 1, ∞), and K(u) ≥ K(v + 1).

In summary, when v ≥ 1,
                                                              K(u) ≥ K(v + 1),          ∀u ≥ v + 1,                              (93)
where
                                                 √                                   √
                        �                           �        �                                   �
                                        2      2      3
           K(v + 1) = 8v −(v + 1)e−(v+1) + ve−v + π     − v 2 (erf(v + 1) − erf(v)) + π(2v 2 − 1) .                              (94)
                                                      2
It is shown in Section C-A below that
                                                                     ∀v ≥ 1.
                                                                    K(v + 1) > 0,                                         (95)
                                                                          2
                                                          d    d
                                                                         �
We have therefore shown (cf.�(92), (93), and (95)) that dv  2 du V (u, v) > 0 for all u ≥ v + 1 and v ≥ 1. This shows that the
               d    d
mapping v → dv du V (u, v) is increasing in [1, u − 1] for u ≥ 2.
                                       d    d
                                                      �
It is shown in Section C-B below that dv   du V (u, v) |v=u−1 , given by
               �             �
             d    d
                     V (u, v) |v=u−1
            dv du
                          "
                 −(u−1)2
                             √     √                    2        2                         2   √
            = 4e            − π − 2 π(u − 1)2 − e−u + ue−u −2u+1 − (u − 1)e−(u−1) − π(2u2 + 1)e−2u+1
                                                                                                          #
                √
                        ��           �                �                  ��
                             2   1           −2u+1               1  2
            +       π        u −         e           + (u − 1) −              (erf(u) − erf(u − 1)) ,                            (96)
                                 2                               2
                                                   d
is negative for u ≥ 2. Therefore, the mapping v → du V (u, v) is decreasing in [1, u − 1] for u ≥ 2.
                                       d
It is shown in Section C-C below that du V (u, v)|v=1 , given by
             d                              √                 2               2    √                   2
               V (u, v)|v=1 = −4π + 2e−2 + 4 πe−1 − 4u2 e−u −1 + 2(2u − 1)e−2u − 4 π(2u2 − u + 1)e−u
            du
                               √                                  2   √ √
                            + 2 π(2u2 + u − 1)(erf(u) − erf(1))e−u + 2 π(2 π − e−1 )(erf(u) − erf(1)),                           (97)
                                    d
is negative for all u ≥ 2. Hence, du  V (u, v) < 0 for all u ≥ v + 1 and v ≥ 1, which in turn implies that the mapping
u → V (u, v) is decreasing in [v + 1, ∞) for v ≥ 1. But V (v + 1, v) given by
                                                          2                         2                 2
                V (v + 1, v) = −4π + 2e−2v −2v−1 − 2ve−2(v+1) + 2(v + 1)e−2v + 4π(erf(v + 1) − erf(v))
                               √                                                2     2
                             + π(2v 2 + 2v + 1)(erf(v) − erf(v + 1) + 2)(e−(v+1) + e−v ),                                        (98)
is negative for all v ≥ 1 as shown in Section C-D below, so that V (u, v) < 0 for all u ≥ v + 1 and v ≥ 1. This completes the
proof of Proposition A.1 and, consequently, the proof of Proposition C.1

A. Proof that K(v + 1) > 0 for v ≥ 1

We have (cf. (94))
                                            K(v + 1) = 8vg(v),
                            2      2 √                                  √
with g(v) := −(v + 1)e−(v+1) + ve−v + π 32 − v 2 (erf(v + 1) − erf(v)) + π(2v 2 − 1).
                                                �

                                             R v+1 −t2
Since erf(v + 1) − erf(v) = √2π               v
                                                  e dt, we can rewrite g(v) as
                                                                                           Z v+1
                                                                2         2                           2       √
                              g(v) = −(v + 1)e−(v+1) + ve−v + (3 − 2v 2 )                          e−t dt +       π(2v 2 − 1).
                                                                                            v

[p.22]

Differentiating g(v) gives
                                                                    Z v+1
                                           √
                                         �                                              �
                                                               2             2    1   2
                              g ′ (v) = 4 v π + (v + 1)e−(v+1) − v        e−t dt − e−v .
                                                                     v            2
                                       2           v+1    2      2
Using the inequalities (v + 1)e−(v+1) > 0 and v e−t dt ≤ e−v , we obtain that
                                                 R

                                                          √
                                                        �     �      �     �
                                                                   1 −v2
                                            g ′ (v) ≥ 4     π− v+      e     ,
                                                                   2
for v ≥ 1.
                             2                                                          2
The mapping v → v + 21 e−v is decreasing in [1, ∞) (its derivative is −(2v 2 + v − 1)e−v , which is negative when v ≥ 1).
                       �
                 2
Hence, v + 21 e−v ≤ 32 e−1 , yielding
             �

                                                  √
                                                �           �
                                       ′               3 −1
                                      g (v) ≥ 4     π− e       ≈ 4.88, ∀v ≥ 1.
                                                       2
Therefore, the mapping v → g(v) is increasing in [1, ∞), and since g(1) ≈ 2.23, we conclude that g(v) ≥ 0 for v ≥ 1.

               d d
B. Proof that dv du V (u, v)|v=u−1 < 0 for u ≥ 2.


Denote by g(u) the term between square brackets in the r.h.s. of (96), that is
                       √      √                  2         2                         2  √
             g(u) = − π − 2 π(u − 1)2 − e−u + ue−u −2u+1 − (u − 1)e−(u−1) − π(2u2 + 1)e−2u+1
                     √
                         ��        �           �                ��
                                 1 −2u+1                      1
                   + π      u2 −     e      + (u − 1)2 −            (erf(u) − erf(u − 1)).
                                 2                            2
                                                         2
By using the inequality erf(u) − erf(u − 1) ≤ √2π e−(u−1) we obtain for u ≥ 2 (Hint: the coefficient of erf(u) − erf(u − 1)
is positive when u ≥ 2)
                        √       √                  2       2                      2    √
               g(u) ≤ − π − 2 π(u − 1)2 − e−u + ue−u −2u+1 − (u − 1)e−(u−1) − π(2u2 + 1)e−2u+1
                        �        �          �              �
                           2   1 −u2                 2   1 −(u−1)2
                    +2 u −         e    + 2 (u − 1) −         e     ,
                               2                         2
                        √       √                           2      2                                 2
                    = − π − 2 π(u − 1)2 + 2(u2 − 1)e−u + ue−u −2u+1 + (2u2 − 5u + 2)e−(u−1)
                      √
                    − π(2u2 + 1)e−2u+1 .                                                                               (99)
                               2                                                     2
The mapping u → (u2 − 1)e−u is decreasing in [2, ∞) (its derivative is 2u(2 − u2 )e−u which is negative for u ≥ 2), yielding
            2
2(u2 − 1)e−u ≤ 6e−4 for u ≥ 2.
                         2                                                                    2
The mapping u → ue−u −2u+1 is decreasing in [2, ∞) (its derivative is (−2u2 − 2u + 1)e−u −2u+1 which is negative for
                     2
u ≥ 2), yielding ue−u −2u+1 ≤ 2e−7 for u ≥ 2.
                                2              2                                               2
Finally, (2u2 − 5u + 2)e−(u−1) ≤ 2u2 e−(u−1) for u ≥ 2. Since the mapping v → 2u2 e−(u−1) is decreasing in [2, ∞) (its
                                    2                                                  2
derivative is −4u(u2 − u − 1)e−(u−1) which is negative for u ≥ 2), yielding 2u2 e−(u−1) ≤ 4e−1 for u ≥ 2, and therefore
                      2
(2u2 − 5u + 2)e−(u−1) ≤ 4e−1 for u ≥ 2.

Introducing these bounds into (99) gives
                                 √                        √             √
                       g(u) ≤ − π + 6e−4 + 2e−7 + 4e−1 − 2 π(u − 1)2 − π(2u2 + 1)e−2u+1 .                              (100)
                   √
for v ≥ 1. Since − π + 6e−4 + 2e−7 + 4e−1 ≈ −0.189, we conclude from (100) that g(u) < 0 for all u ≥ 2.

               d
C. Proof that du V (u, v)|v=1 < 0 for u ≥ 2.

Denote by g(u) the rh.s. of (97), that is,
                                      √                 2               2    √                   2
                 g(u) = −4π + 2e−2 + 4 πe−1 − 4u2 e−u −1 + 2(2u − 1)e−2u − 4 π(2u2 − u + 1)e−u
                         √                                  2   √ √
                      + 2 π(2u2 + u − 1)(erf(u) − erf(1))e−u + 2 π(2 π − e−1 )(erf(u) − erf(1)).                       (101)

[p.23]

                                                                   R x −t2
By using the two-sided inequalities (Hint: erf(x) − erf(y) = √2π    y
                                                                      e dt for x > y)
                                       2     2                    2      2
                                      √ e−y ≤ erf(x) − erf(y) ≤ √ e−x , x > y,                                      (102)
                                        π                          π
                                                           √
in (101), we obtain (Hint: (2u2 + u − 1 > 0 for u ≥ 2 and 2 π − e−1 > 0)
                                     √                2                 2  √               2
             g(u) ≤ −4π + 2e−2 + 4 πe−1 − 4u2 e−u −1 + 2(2u − 1)e−2u − 4 π(2u2 − u + 1)e−u
                                         2       √
                  + 4(2u2 + u − 1)e−1−u + 4(2 π − e−1 )e−1 ,
                                     √            √                         2                     2
                  ≤ −4π + 2e−2 + 4 πe−1 + 4(2 π − e−1 )e−1 + 2(2u − 1)e−2u + 4e−1 (2u2 + u − 1)e−u ,
for u ≥ 2.
                               2                                                            2
The mapping u → (2u − 1)e−2u is decreasing in [2, ∞) (its derivative is (−2(2u2 − u − 1)e−2u which is negative for u ≥ 2),
                      2
yielding 2(2u − 1)e−2u ≤ 6e−8 for u ≥ 2.
                                    2                                                                           2
The mapping u → (2u2 + u − 1)e−u is decreasing in [2, ∞) (its derivative is (−2u2 (u − 1) − 2u(u2 − 1) − 1)e−u which is
                                                   2
negative for u ≥ 2), yielding 4e−1 (2u2 + u − 1)e−u ≤ 36e−5 for u ≥ 2. Hence, for u ≥ 2,
                                               √         √
                       g(u) ≤ −4π + 2e−2 + 4 πe−1 + 4(2 π − e−1 )e−1 + 6e−8 + 36e−5 ≈ −4.76.

D. Proof that V (v + 1, v) < 0 for v ≥ 1

Applying the two-sided inequalities (102) to (98) gives
                                          2                   2             2     √      2
             V (v + 1, v) ≤ − 4π + 2e−2v −2v−1 − 2ve−2(v+1) + 2(v + 1)e−2v + 8 πe−v
                                                     2          2   2     √                         2     2
                            − 2(2v 2 + 2v + 1)e−(v+1) (e−(v+1) + e−v ) + 2 π(2v 2 + 2v + 1)(e−(v+1) + e−v ),
                                          2                   2             2     √      2
                          = − 4π + 2e−2v −2v−1 − 2ve−2(v+1) + 2(v + 1)e−2v + 8 πe−v
                                                       2          2       √                        2     2
                            − 2(2v 2 + 2v + 1)(e−2(v+1) + e−2v −2v−1 ) + 2 π(2v 2 + 2v + 1)(e−(v+1) + e−v ),
                                                2    √      2                         2
                          = − 4π + 2(v + 1)e−2v + 8 πe−v − 2(2v 2 + 3v + 1)e−2(v+1)
                                            2          √                      2        2
                            − 4v(v + 1)e−2v −2v−1 + 2 π(2v 2 + 2v + 1)(e−(v+1) + e−v ).
                               2                                                            2
The mapping v → (v + 1)e−2v is decreasing in [1, ∞) (its derivative is (1 − 2v(v + 1))e−2v which is negative for v ≥ 1),
                    2
so that 2(v + 1)e−2v ≤ 4e−2 . Therefore,
                                                       √   2                           2
                      V (v + 1, v) ≤ − 4(π − e−2 ) + 8 πe−v − 2(2v 2 + 3v + 1)e−2(v+1)
                                                     2        √                          2    2
                                     − 4v(v + 1)e−2v −2v−1 + 2 π(2v 2 + 2v + 1)(e−(v+1) + e−v ).
                                           2      2
The mapping v → (2v 2 + 2v + 1)(e−(v+1) + e−v ) is decreasing in [1, ∞). Indeed,
                d                        2     2                             2                           2
                  (2v 2 + 2v + 1)(e−(v+1) + e−v ) = −2v(2v 2 + 4v + 1)e−(v+1) − 2(2v 3 + 2v 2 − v − 1)e−v .
               dv
                                                                                  2     2
                                                       d
When v ≥ 1, 2v 3 + 2v 2 − v − 1 ≥ 0, which shows that dv (2v 2 + 2v + 1)(e−(v+1) + e−v ) < 0 for all v ≥ 1, which in turn
                                  −(v+1)2    −v 2
                                                                                  √                          2      2
proves
  √ that
                    2
           v → (2v + 2v + 1)(e            + e ) is decreasing in [1, ∞). Hence, 2 π(2v 2 + 2v + 1)(e−(v+1) + e−v ) ≤
       −4      −1
10 π(e + e ) for all v ≥ 1, and
                                    √      2                           2               2            √
    V (v + 1, v) ≤ − 4(π − e−2 ) + 8 πe−v − 2(2v 2 + 3v + 1)e−2(v+1) − 4v(v + 1)e−2v −2v−1 + 10 π(e−4 + e−1 ),
for v ≥ 1.
               √    2                          2                2
Define g(v) = 8 πe−v − 2(2v 2 + 3v + 1)e−2(v+1) − 4v(v + 1)e−2v −2v−1 so that
                                                              √
                              V (v + 1, v) ≤ −4(π − e−2 ) + 10 π(e−4 + e−1 ) + g(v).
Assume that v → g(v) is decreasing in [1, ∞). If so, for v ≥ 1,
                                                             √
                          V (v + 1, v) ≤ −4(π − e−2 ) + 10 π(e−4 + e−1 ) + g(1) ≈ −0.021,
which would complete the proof that V (v + 1, v) < 0 for all v ≥ 1.

[p.24]

It remains to prove that v → g(v) is decreasing in [1, ∞). We have
                              √      2                                  2                        2
                 g ′ (v) = −16 πve−v + 2(8v 3 + 20v 2 + 12v + 1)e−2(v+1) + 4(4v 3 + 6v 2 − 1)e−2v −2v−1 .
g ′ (v) < 0 is equivalent to
                         √                                     2  2                        2       2
                      16 πv ≥ 2(8v 3 + 20v 2 + 12v + 1)e−2(v+1) +v + 4(4v 3 + 6v 2 − 1)e−2v −2v−1+v ,                        (103)
Since
              d � 3                            2  2
                                                    �                                           2  2
                 (8v + 20v 2 + 12v + 1)e−2(v+1) +v = −2(8v 4 + 38v 3 + 32v 2 + 13v + 1))e−2(v+1) +v < 0,
             dv
                                                                    2   2
for v ≥ 1, the mapping v → 2(8v 3 + 20v 2 + 12v + 1)e−2(v+1) +v is decreasing in [1, ∞), yielding 2(8v 3 + 20v 2 + 12v +
           2  2
1)e−2(v+1) +v ≤ 2(8 + 38 + 32 + 13 + 1)e−5 = 184e−5 for all v ≥ 1. On the other hand,
                       d � 3                 2
                                                    �                                     2
                          (4v + 6v 2 − 1)e−v −2v−1 = 2(−4v 4 − 10v 3 + 6v 2 + v + 1)e−v −2v−1 .
                      dv
But
          −4v 4 − 10v 3 + 6v 2 + v + 1 = −v 4 − 3v 4 − 10v 3 + 6v 2 + v + 1,
                                         ≤ −1 − 3v − 10v 2 + 6v 2 + v + 1, as v 4 ≥ 1, v 4 ≥ v, v 3 ≥ v 2 when v ≥ 1,
                                         = −4v 2 − 2v < 0,
                                                                            2
when v ≥ 1, which shows that the mapping v → (4v 3 + 6v 2 − 1)e−v −2v−1 is decreasing in [1, ∞), yielding 4(4v 3 + 6v 2 −
     2
1)e−v −2v−1 ≤ 4(4 + 6 − 1)e−4 = 36e−4 for all v ≥ 1.

We have shown that
                                             2                                  2
                 2(8v 3 + 20v 2 + 12v + 1)e−v −2v−2 + 4(4v 3 − 6v 2 − 1)e−v −2v−1 ≤ 184e−5 + 36e−4 ≈ 1.899.
for all v ≥ 1.
                     √       √
On the other hand, 16 πv ≥ 16 π = 28.359 for v ≥ 1. This shows from (103) that g ′ (v) < 0 for all v ≥ 1.

                                                       A PPENDIX D
                                       P ROOF OF P ROPOSITION A.2 IN S ECTION A-B2

We want to show x → G(x, θ) is non-increasing in [0, ∞) for all θ ≥ 0, where G(x, θ) is given in (74). We have
                                           ∂                       R(x, θ)
                                              G(x, θ) =                           ��2 ,                                      (104)
                                           ∂x
                                                           �    �   �       �
                                                          π erf x+θ
                                                                √
                                                                  2
                                                                      + erf   x−θ
                                                                              √
                                                                                2

with
                                       √
                                                      �                    �� �           �        �      ��
                               2   2                       (x−θ)2   (x+θ)2         x+θ               x−θ
            R(x, θ) := 4xe−x −θ −      2π(θ2 − x2 + 1) e− 2 + e− 2            erf    √       + erf    √
                                                                                       2                2
                                                                  � �        �       �        ��2
                                       2                 2             x+θ             x−θ
                      + 2(x + θ)e−(x−θ) + 2(x − θ)e−(x+θ) − 2πx erf     √      + erf     √         .
                                                                           2               2
Since it is hard to determine the sign of R(x, θ), let us look at its derivative with respect to x, which is given by
                     "                         � �            �        �         ��2
     ∂                         2 −x2 −θ 2               x+θ              x−θ                       �        2             2
                                                                                                                            �
                          2
        R(x, θ) = − 4(x + θ )e            + 2π erf       √      + erf      √         + 2(x2 − θ2 ) e−(x−θ) + e−(x+θ)
    ∂x                                                     2                 2
                                                                                                                     �#
        √
             � �          �       �       �� �
                     x+θ             x−θ                         2        −
                                                                            (x−θ)2
                                                                                                     2      −
                                                                                                              (x+θ)2
    + 2π erf          √     + erf     √         (x + θ)((x − θ) + 1)e          2   + (x − θ)((x + θ) + 1)e       2      .     (105)
                        2               2
A quick inspection of the terms inside the square brackets reveals that they are all non-negative when x ≥ θ ≥ 0 (Hint:
                              ∂
erf(z) ≥ 0 if z ≥ 0), so that ∂x R(x, θ) ≤ 0 for x ≥ θ ≥ 0.
            ∂                                   ∂
Assume that ∂x R(x, θ) ≤ 0 for 0 ≤ x ≤ θ. Then, ∂x R(x, θ) ≤ 0 for all x ≥ 0 and θ ≥ 0. This implies that, for every θ ≥ 0,
                                              x → R(x, θ) is decreasing in [0, ∞).                                           (106)

[p.25]

Since R(0, θ) = 0, we conclude from (106) that R(x, θ) ≤ 0 for x ≥ 0 and θ ≥ 0. This in turn implies from (104) that, for
every θ ≥ 0, the mapping x → G(x, θ) is non-increasing in [0, ∞), which proves Proposition A.2.
                                                   ∂
The rest of Section D is devoted to the proof that ∂x R(x, θ) ≤ 0 for 0 ≤ x ≤ θ.

Introduce the mapping F (u, v) defined by
                                                          2       2       2       2
                            F (u, v) :=2(u2 + v 2 )e−u −v − 2uv(e−2u + e−2v )
                                          √                               2               2
                                       + π(erf(u) − erf(v))(u(2v 2 + 1)e−v − v(2u2 + 1)e−u ).                          (107)
We have, from (105),
                                         � �       �       �      ��2      �          �
                         ∂                    θ+x            θ−x             θ+x θ−x
                            R(x, θ) = −2π erf  √     + erf    √       − 2F    √ , √     .                              (108)
                         ∂x                      2              2              2    2
           ∂
Therefore, ∂x R(x, θ) ≤ 0 for 0 ≤ x ≤ θ if F (u, v) ≥ 0 for all 0 ≤ v ≤ u.

The remainder of Section D is now devoted to the proof of the following proposition:

Proposition D.1: F (u, v) ≥ 0 for all 0 ≤ v ≤ u.

The derivative of F (u, v) with respect to u is
                         ∂                           2  2                2         2
                            F (u, v) =2u(3 − 2u2 )e−u −v + 4(u2 − 1)ve−2u − 2ve−2v
                         ∂u
                                        √                  �            2                 2
                                                                                            �
                                      + π(erf(u) − erf(v)) (2v 2 + 1)e−v + 2uv(2u2 − 1)e−u .                           (109)

With an abuse of notation denote by S(v) the r.h.s. of (109), that is
                                                      2       2               2       2
                            S(v) :=2u(3 − 2u2 )e−u −v + 4(u2 − 1)ve−2u − 2ve−2v
                                     √                  �            2                 2
                                                                                         �
                                   + π(erf(u) − erf(v)) (2v 2 + 1)e−v + 2uv(2u2 − 1)e−u .                              (110)

Proving that S(v) ≥ 0 for 0 ≤ v ≤ u will prove that the mapping u → F (u, v) is increasing in [v, ∞) for all v ≥ 0. But since
F (v, v) = 0 for v ≥ 0, this will prove that F (u, v) ≥ 0 for 0 ≤ v ≤ u.

We have
                                     d                2  2                 2                 2
                       S ′ (v) :=      S(v) = − 8uve−u −v + 4(u2 − 1)e−2u + 4(v 2 − 1)e−2v
                                    dv
                                                 √                                  2               2
                                              + 2 π(erf(u) − erf(v))(v(1 − 2v 2 )e−v + u(2u2 − 1)e−u ).                (111)
If S ′ (v) ≤ 0 for 0 ≤ v ≤ u, then v → S(v) is decreasing in [0, u] for all u ≥ 0. But S(u) = 0, and therefore S(v) ≥ 0 for
0 ≤ v ≤ u, which would prove that F (u, v) ≥ 0 for 0 ≤ v ≤ u, as noted earlier.

The objective is now to show that S ′ (v) ≤ 0 for 0 ≤ v ≤ u. Denote S ′′ (v) = dv
                                                                                d ′
                                                                                  S (v). We have
                                                                      2
                                                     S ′′ (v) = −8e−2v H(u),                                           (112)
with (again with an abuse of notation)
                                                               2√
                          �              �                                        �               �
                                       1 −u2 +v2        5v                                      1
               H(u) := u u2 − 2v 2 +       e     + v3 −    − ev π(erf(u) − erf(v)) v 4 − 2v 2 +     .                  (113)
                                       2                 2                                      4
If H(u) ≤ 0 for 0 ≤ v ≤ u then S ′′ (v) ≥ 0 for 0 ≤ v ≤ u, and v → S ′ (v) is increasing in [0, u] for all u ≥ 0. But
                2
S ′ (u) = −8e−2u < 0, which would give that S ′ (v) ≤ 0 for 0 ≤ v ≤ u.

Our objective is now to show that H(u) ≤ 0 for 0 ≤ v ≤ u. We now differentiate H(u) with respect to the variable u to get
rid of the error functions. We have
                                   d              2  2
                                     H(u) = −2e−u +v u4 − (2v 2 + 1)u2 + v 2 (v 2 − 1) ,
                                                                                      �
                                  du
                                                  2  2
                                          = −2e−u +v (u2 − u1 )(u2 − u2 ),                                          (114)

[p.26]

              2
                   √                       2
                                               √                            √              √
                       2                            2
with u1 := 2v +1−2 8v +1 and u2 := 2v +1+2 8v +1 > 0. Notice that               u1 ≤ v <       u2 for v ≥ 0.
                                                               d                          √         d
When 0 ≤ v ≤ 1 then u1 ≤ 0, and we conclude from (114) that du   H(u) ≥ 0 when v ≤ u ≤ u2 and du      H(u) ≤ 0 when
   √                                     √                       √                                      √
u ≥ u2 . Hence, u → H(u) increases in [v, u2 ) and decreases in ( u2 , ∞). Its maximum is reached at u = u2 .
                             d                         √                             √                   d
When v ≥ 1 then u1 ≥ 0, and du H(u) ≥ 0 when v ≤ u ≤ u2 (Hint: use that that v ≥ u1 for v ≥ 0) and du      H(u) ≤ 0
        √                                     √                       √                                      √
when u ≥ u2 . Hence, u → H(u) increases in [v, u2 ) and decreases in ( u2 , ∞). Its maximum is reached at u = u2 .

This proves that
                                                            √
                                               max H(u) = H( u2 ),            ∀v ≥ 0.                                            (115)
                                                v≤u
                                      √
Figure 1 displays the mapping v → H( u2 ) for v ∈ [0, 15]. One can see that this mapping is not negative for all v ≥ 0 as
H(0) = 0.178. However, this plot suggests that it is negative in (for instance) [1/4, ∞) as H(1/4) ≈ −0.202.

Given this situation, we will first establish a negative upper bound for S ′ (v) for all v ∈ [0, 1/4] in Section D-A, and will then
                               √
prove in Section D-B that H( u2 ) < 0 for v ≥ 14 . As discussed earlier, these two results will prove Proposition D.1.




                                                                 √
                                                   Fig. 1. v → H( u2 ) for v ∈ [0, 15]


A. A negative upper bound for S ′ (v) when v ∈ [0, 1/4]
             p
Let a0 ∈ (0, 1/2). We claim that
                           2                 2    √
              4(u2 − 1)e−2u + 4(a20 − 1)e−2a0 + 2 πerf(u)a0
                  √                           √
                                                                                                                         q
                                         2                         2
             
   S ′ (v) ≤   +2 πerf(u)u(2u2 − 1)e−u − 2 πerf(a0 )u(2u2 − 1)e−u ,                                            if v ≤ u ≤ 12 ,   (116)
              4(u2 − 1)e−2u2 + 4(a2 − 1)e−2a20 + 2√πerf(u)a + 2√πerf(u)u(2u2 − 1)e−u2 ,
                                                                                                                     q
                                                                                                               if u ≥ 12 ,
             
                                       0                              0

when 0 ≤ v ≤ a0

[p.27]

                                                       √
Proof of (116): We have for 0 ≤ v ≤ a0 with a0 ∈ (0, 1/ 2) and u ≥ 0,
                                      2  2                2               2    √                     2
                   S ′ (v) = − 8uve−u −v + 4(u2 − 1)e−2u + 4(v 2 − 1)e−2v + 2 πerf(u)v(1 − 2v 2 )e−v
                                √                     2     √                    2   √                    2
                             + 2 πerf(u)u(2u2 − 1)e−u − 2 πerf(v)(v(1 − 2v 2 )e−v − 2 πerf(v)u(2u2 − 1)e−u ,
                                            2                2    √             √                      2
                             ≤ 4(u2 − 1)e−2u + 4(a20 − 1)e−2a0 + 2 πerf(u)a0 + 2 πerf(u)u(2u2 − 1)e−u
                                √                     2
                             − 2 πerf(v)u(2u2 − 1)e−u ,
                                          2    2                                 2                2        2
                                  −u −v
   p we have used that (i) uve
where                                     ≥ 0, (ii) (v 2 − 1)e−2v ≤ (a20 − 1)e−2a0 as v → (v 2 − 1)e−2v is increasing in
                               2 −v 2                                                             2
[0, 1/2], (iii) erf(u)v(1 − 2v )e     ≤ erf(u)a0 since erf(u) ≥ 0, and (iv) erf(v)v(1 − 2v 2 )e−v ≥ 0.
                                               √              2      −u2
                                                                              √                2       −u2
                                                                                                                      p
Inequalities in (116) follow by noting that −2   πerf(v)u(2u    − 1)e    ≤ −2   πerf(a0 )u(2u    −  1)e    if 0 ≤ u ≤   1/2
       √                        2            p
and −2 πerf(v)u(2u2 − 1)e−u ≤ 0 if u ≥ 1/2.

Rewrite (116) as                                                                               q
                                                             f1 (u) + f2 (u),       if 0 ≤ u ≤ 12 ,
                                              S ′ (v) ≤                                     q
                                                             f1 (u),                if u ≥ 12 ,
where
                                             2                2    √             √                    2
                       f1 (u) = 4(u2 − 1)e−2u + 4(a20 − 1)e−2a0 + 2 πerf(u)a0 + 2 πerf(u)u(2u2 − 1)e−u ,             (117)
                                   √                      2
                       f2 (u) = −2 πerf(a0 )u(2u2 − 1)e−u .                                                          (118)

                                      q
                                          1
Proof that f1 (u) ≤ 0 when u ≥            2   and a0 = 14 :
                                                                      √
                                              f1 (u) = g1 (u) + C1 + 2 πerf(u)(a0 + h1 (u)),
                                  2                                 2                                  2
with g1 (u) = 4(u2 − 1)e−2u , C1 = 4(a20 − 1)e−2a0 ≈ −3.309, and h1 (u) = u(2u2 − 1)e−u . Since erf(u) ≤ 1 and
a0 + h1 (u) ≥ 0, we have                                            √
                                         f1 (u) ≤ g1 (u) + C1 + 2 π(a0 + h1 (u)).
                                  2
                                                                                     q
On the other hand, g1′ (u) = 8e−2u u(3 − 2u2 ), which vanishes when u = 0 and u = 32 . Therefore,
                                                              q
                                                                3       −3
                                         maxr   g1 (u) = g 1 (  2 ) = 2e   ≈ 0.0995.
                                                        1
                                                   u≥   2

                     2                       2
                                               �           √ ��              √ �                       √
Also, h′1 (u) = −e−u (4u4 − 8u2 + 1) = −4e−u u2 − (1 − 23 ) u2 − (1 + 23 ) . The smaller root t1 = 1 − 23 ≈ 0.366
                               p                                        √
does not lie in the domain {u ≥ 1/2} whereas the larger root t2 = 1 + 23 does. Hence,
                                                   √       √
                                  max
                                    r h1 (u) = h1 ( t2 ) =   t2 (2t2 − 1)e−t2 ≈ 0.577.
                                               1
                                       u≥      2

Putting these bounds together yields
                                             √           √
                             �q �
                                 3
                 f1 (u) ≤ g1     2   + C1 + 2 π(a0 + h1 ( t2 )) ≈ 0.0995 − 3.881 + 2.933 = −0.276 < 0,
          q
              1
for u ≥       2.
                                                        q
                                                             1
Proof that f1 (u) + f2 (u) ≤ 0 when 0 ≤ u ≤                  2   and a0 = 41 :

We have
                                                                2        √
                                  f1 (u) + f2 (u) =4(u2 − 1)e−2u + C1 + 2 πerf(u)a0 + k1 (u),
                 √    2
where k1 (u) := 2 πe−u u(2u2 − 1)(erf(u) − erf(a0 )) and where C1 ≈ −3.309 was defined earlier

[p.28]

              q
                   1            2        1
For 0 ≤ u ≤        2 , we have u − 1 ≤ − 2 . Thus
                                                             2           2
                                            4(u2 − 1)e−2u ≤ −2e−2u ≤ −2e−1 ≈ −0.735.
       √             √     p
Also, 2 πerf(u)a0 ≤ 2 πerf( 1/2)a0 ≈ 0.605.
                           √      2                                                          p          p
We now bound k1 (u) = 2 πe−u u(2u2 − 1)(erf(u) − erf(a0 )) from above on the interval [0, 1/2]. On [a0 , 1/2], k1 (u)
is negative since erf(u) ≥ erf(a0 ). On u ∈ [0, a0 ] we have
                                     √     2                                √
                          k1 (u) = 2 πe−u u(1 − 2u2 )(erf(a0 ) − erf(u)) ≤ 2 πa0 erf(a0 ) ≈ 0.244.
Collecting these bounds, we obtain
                                   1√      p       1√
    f1 (u) + f2 (u) ≤ −2e−1 + C1 +    πerf( 1/2) +    πerf(1/4) ≈ −0.735 − 3.909 + 0.605 + 0.244 = −3.192 < 0,
                                   2               2
             q
for 0 ≤ u ≤ 12 .

                  √
B. Proving that H( u2 ) for v ≥ 1/4

               √         √ √
Define α0 = 3/2, α1 = 8+2        13
                                                    p
                             2      ≈ 1.95, and α2 = 5/2 ≈ 1.58. We will see later on that α0 , α1 and α2 each plays a
particular role.
                                    √                      √               √        √                √
We will successively
               √     proved that H(√ u2 ) < 0 for v ∈ [1/4, 1 − α0 ], v ∈ [ 1 − α0 , 1 + α0 ], v ∈ [ 1 + α0 , α2 ], and
v ∈ [α2 , ∞) ( 1 − α0 ≈ 0.336 and 1 + α0 ≈ 1.336).
                                                                             √
We first list useful properties in Section D-B1 and derive upper bounds on H( u2 ) in Section D-B2.
                                         √
√ Useful properties: (a) Let f3 (v) = u2 − v. Notice, from the definition of u2 , that f3 (v) ≥ 0 for v ≥ 0. With f4 (v) =
1)
   8v 2 + 1, we have
                                 �         �
                             2v 1 + f42(v)                                    6(v 2 + f4 (v) + 1)
                  f3′ (v) = p                    − 1, f3′′ (v) =                           p                   .
                              4v 2 + 2 + 2f4 (v)                 (1 + 2v 2 + f4 (v))f2 (v)3 4v 2 + 2 + 2f4 (v)
Since f3′′ (v) > 0 for v ≥ 0, we see that the mapping v → f3′ (v) is increasing in [0, ∞). The latter property and limv→∞ f3′ (v) =
0 imply that f3′ (v) ≤ 0 for v ≥ 0, which in turn implies that
                                                      v → f3 (v) is decreasing on [0, ∞).                                    (119)
Last, f3 (0) = 1 and limv→∞ f3 (v) = √12 .
                                                                √ √
(b) The only zero of u2 − 2v 2 + 12 in [0, ∞) is located at α1 = 8+2
                                                                   2
                                                                     13
                                                                        . In particular,
                                                                    √ √
                                                   1  < 0 for v > 8+2     2√
                                                                              13
                                                                                 ,
                                      u2 − 2v 2 + =                                √                                         (120)
                                                   2  > 0 for 0 ≤ v < 8+2 13 .
                                                                                            2
                                            �                �                                                  √
                                                                                                                  6
The derivative of u2 − 2v 2 + 21 is 2v    √ 2
                                               2
                                                   − 1 ; in the region {v > 0} this derivative vanishes at v =   4 ≈ 0.612, is
               √                         √ 8v +1                                                           √
positive
 √
         in (0, 46 ) and is negative in ( 46 , ∞). Hence, the mapping v → u2 − 2v 2 + 12 increases in (0, 46 ) and decreases in
( 46 , ∞).
                                                            q
(c) The only zero of v 3 − 5v
                            2 in (0, ∞) is located  at α2 =    5
                                                               2 ≈ 1.581. In particular,
                                                                            q
                                                                                5
                                                 5v       < 0   for 0 < v <    2,
                                           v3 −      =                   q                                                   (121)
                                                  2      > 0 for v > 5 .
                                                                                   2
                                                p                           p         p
Also, v → v   3
                  − 5v
                     2   is decreasing in [0,       5/6) and increasing in ( 5/6, ∞) ( 5/6 ≈ 0.912).

[p.29]

                                                                                  q        √                  q       √
                                                                                            3
(d) The polynomial −v + 2v 4      2
                                      − 14 has two zeros in [0, ∞) located at         1−   2 ≈ 0.366 and          1 + 23 ≈ 1.366. In particular,
                                                                    q     √        q   √
                                             1   >0             for   1 − 23 < v < 1 + 23 ,
                                −v 4 + 2v 2 − =                              q    √          q  √                                              (122)
                                             4  <0              for 0 < v ≤ 1 − 23 and v > 1 + 23 .

Also, v → −v 4 + 2v 2 − 41 is increasing in [0, 1) and decreasing in (1, ∞).
                      √
2) Upper bounds for H( u2 ): By using the two-sided inequalities in (102) along with (122), we get from (113)
                                  �               �                                         �                �
             p                √             2   1 v2 −u2       3    5v      v 2 −u2 √          4      2    1
          H( u2 ) ≤ K1 (v) := u2 u2 − 2v +          e     +v −         − 2e        ( u2 − v) v − 2v +          ,                               (123)
                                                2                    2                                     4
            q     √          q     √
for 0 ≤ v ≤ 1 − 23 and v ≥ 1 + 23 , and
                                     �                �                                  �               �
               p                √              2    1 v2 −u2       3   5v        √          4     2    1
             H( u2 ) ≤ K2 (v) := u2 u2 − 2v +           e      +v −        − 2( u2 − v) v − 2v +           ,                                   (124)
                                                    2                   2                              4
    q     √         q    √
for 1 − 23 ≤ v ≤ 1 + 23 .
                √                      √
         that H( u2 ) < 0 for v ∈ [1/4, 1 − α0 ]: Thanks to the bound in (123) it is sufficient to prove that K1 (v) < 0 for
3) Proof q
                   √
1
4 ≤v ≤        1 − 23 .
                   √                    � 2                                           v 2 −u2 √
                       u2 u2 − 2v 2 + 12 ev −u2 , T2 (v) = v 3 − 5v                          ( u2 − v) −v 4 + 2v 2 − 14 so that
                                                                                                                       �
Define T1 (v) =                                                   2 , and T3 (v) = 2e

                                                       K1 (v) = T1 (v) + T2 (v) + T3 (v).                                                      (125)
We have                                                                                         √
                                                                    √                             8v 2 +1
                                                   v(8v 4
                                                          −  6v 2
                                                                  (   8v 2 + 1 + 4) + 1)e− 21 −    2
                                           ′
                                          T1 (v) =        √           p              √                    .                                    (126)
                                                              2             2
                                                            8v + 1 4v + 2 + 2 8v + 1     2

Since
                                                        √ 4
                                                  s                               
                                                                  � �2 s � �2
                           p                              3        1      1
              8v 4 − 6v 2 ( 8v 2 + 1 + 4) + 1 ≤ 8  1 −      − 6      8     + 1 + 4 + 1 ≈ −0.815,
                                                         2         4      4
               q    √                                          q    √
                                          ′
for 14 ≤ v ≤    1 − 2 , we conclude that T1 (v) ≤ 0 for 4 ≤ v ≤ 1 − 23 . Hence, max 1
                      3                                 1                                                                           1
                                                                                                                                        �
                                                                                                            q   √ T1 (v) ≤ T1               ≈ 0.552.
                                                                                                              1− 23                 4
                                                                                                       4 ≤v≤

                                                       q                                           q     √     q
Last, the property that v → T2 (v) is decreasing in [0, 56 ) (see Section D-B1-(c)) coupled with 1 − 23 < 56 , ensures
                                                                                        q    √
                         T2 (v) = T2 4 ≈ −0.609. Finally, since T3 (v) ≤ 0 for v ∈ [ 4 , 1 − 23 ] by (122), we conclude that
                                     1                                               1
                                       �
that max 1      q    √
                       3
          4 ≤v≤    1− 2
                                                q      √
K1 (v) ≤ T1 4 + T2 14 ≈ −0.057 for v ∈ [ 14 , 1 − 23 ].
               1
                 �          �

                 √                    √         √
              H( u2 ) <
4) Proof that √          √0 for v ∈ [ 1 − α0 , 1 + α0 ]: Thanks to the bound in (124) it is sufficient to prove that K2 (v) < 0
for v ∈ I := [ 1 − α0 , 1 + α0 ].
                     √                                                                                         √                � 2
Define T4 (v) = −2( u2 −v) v 4 − 2v 2 + 14 so that K2 (v) = T1 (v)+T2 (v)+T4 (v), where we recall    that T1√= u2 u2 − 2v 2 + 12 ev −u2
                                              �
                                                                                                   √
and T2 (v) = v 3 − 5v
                    2 . T1 (v) and T4 (v) are both positive on I, while T2 (v) is negative on I = [ 1 − α0 , 1 + α0 ].

Let [i0 , i1 ] ⊂ I, i0 < i1 .
                                             √            �
• Differentiating A(v) := 8v 4 − 6v 2         8v 2 + 1 + 4 + 1, gives
                                                          √                     √
                                           ′       4v(8v 2 8v 2 + 1 − 36v 2 − 12 8v 2 + 1 − 3)
                                          A (v) =                   √                          .
                                                                      8v 2 + 1

[p.30]

On I,
                      p                        p
               8v 2   8v 2 + 1 − 36v 2 − 12 8v 2 + 1 − 3
                     √           q √                           √                 q √
                ≤ 8( 1 + α0 )2 8( 1 + α0 )2 + 1 − 36( 1 − α0 )2 − 12 8( 1 − α0 )2 + 1 − 3 ≈ −31.713,
                                                                    √
so that A′ (v) < 0 on I and A(v) is decreasing on I. Since A( 1 − α0 ) ≈ −3.228, we conclude from (126) that v → T1 (v)
is decreasing on I. In particular, on [i0 , i1 ],
                                                            T1 (v) ≤ T1 (i0 );
                                   p                               p
• v → T2 (v) is decreasing on [0, 5/6) and increasing on ( 5/6, ∞). Therefore, on [i0 , i1 ],
                                                                                    p
                                                 T2 (i0 ),                  if i1 ≤ p5/6,
                                    T2 (v) ≤      max{T2 (i0 ), T2 (i1 )}, if i0 ≤ p5/6 < i1 ,
                                                
                                                  T2 (i1 ),                  if i0 > 5/6.

             √
• B(v) := 2( u2 − v) ≥ 0 for all v ≥ 0, and B(v) ≤ B(i0 ) for v ∈ [i0 , i1 ] since v → B(v) is decreasing on [0, ∞) as shown
in Section D-B1-(a). Define C(v) = −v 4 + 2v 2 − 14 . C(v) is positive on I, increasing in [0, 1) and decreasing in (1, ∞).
Therefore, for v ∈ [i0 , i1 ],                    
                                                   C(i1 ), if i1 ≤ 1,
                                          C(v) ≤      C(1), if i0 ≤ 1 < i1 ,
                                                      C(i0 ), if i0 > 1.
                                                  

Since T4 (v) = B(v)C(v) the above implies that
                                                   
                                                    B(i0 )C(i1 ), if i1 ≤ 1,
                                        T4 (v) ≤        B(i0 )C(1), if i0 ≤ 1 < i1 ,
                                                        B(i0 )C(i0 ), if i0 > 1.
                                                   
                             q    √   q        √
In summary, on [i0 , i1 ] ⊂ [ 1 − 3/2, 1 + 3/2],
                                                                                                 p
                                   
                                    T1 (i0 ) + T2 (i0 ) + B(i0 )C(i1 ),                  if i1 ≤ p5/6,
                                    T1 (i0 ) + max{T2 (i0 ), T2 (i1 )} + B(i0 )C(i1 ),   if i0 ≤ p5/6 < i1 ≤ 1,
                                   
                                   
          K2 (v) ≤ M (i0 , i1 ) :=   T1 (i0 ) + max{T2 (i0 ), T2 (i1 )}) + B(i0 )C(1),        0 ≤
                                                                                          if ip      5/6 and i1 > 1,         (127)
                                   
                                    T1 (i0 ) + T2 (i1 ) + B(i0 )C(1),
                                   
                                   
                                                                                         if 5/6 < i0 ≤ 1 < i1 ,
                                     T1 (i0 ) + T2 (i1 ) + B(i0 )C(i0 ),                  if i0 > 1.

                                                                 √
Partition the interval I as follows: I = ∪14 i=1 Ii , with I1 = [ 1 − α0 , 0.5], I2 = [0.5, 0.6], I3 = [0.6, 0.7], I4 = [0.7, 0.8],
I5 = [0.8, 0.85], I6 = [0.85, 0.9], I7 = [0.95, 1],√ I8 = [1, 1.05], I9 = [1.05, 1.1], I10 = [1.1, 1.15], I11 = [1.15, 1.2],
I12 = [1.2, 1.25], I13 = [1.25, 1.3], and I14 = [1.3, 1 + α0 ].
             √
We find M ( 1 − α0 , 0.5) ≈ −0.022, M (0.5, 0.6) ≈ −0.075, M (0.6, 0.7) ≈ −0.041, M (0.7, 0.8) ≈ −0.008, M (0.8, 0.85) ≈
−0.056, M (0.85, 0.95) ≈ −0.002, M (0.95, 1) ≈ −0.026, M (1, 1.05) ≈ −0.017, M (1.05, 1.1)√≈ −0.008, M (1.1, 1.15) ≈
−0.017, M (1.15, 1.2) ≈ −0.046, M (1.2, 1.25) ≈ −0.099, M (1.25, 1.3) ≈ −0181, and M (1.3, 1 + α) ≈ −0.247.

This shows that K2 (v) < 0 on I.

Remark D.1: Selecting less intervals for partioning interval I may lead to an upper bound for K2 (v) that is positive on
some of these intervals. For instance, if instead of [0.5.0.6], which yields M (0.5, 0.6) ≈ −0.075, we select [0.5, 0.7] then
M (0.5, 0.7) ≈ 0.154. Even the interval [0.5, 0.65] is not good as M (0.5, 0.65) ≈ 0.041. This is the price to pay for upper-
             √
bounding H( u2 ) by K2 (v) on I (see (124)).
                 √                   √                                                              √
                                                                                                        2 +1
5) Proof that H( u2 ) < 0 for v ∈ [ 1 + α0 , α2 ]: For convenience, we now denote u2 = v 2 + 1+ 8v    2      by u2 (v). We will
use the bound in (123), also written as K1 (v) = T1 (v) + T2 (v) + T3 (v), where T1 , T2 and T3 are defined in Section D-B3.

Since                           p                                      p
                   8v 4 − 6v 2 ( 8v 2 + 1 + 4) + 1 ≤ 8α24 − 6(1 + α0 )( 8(1 + α0 ) + 4) + 1 ≈ −45.4 < 0,
         √                                                                    √
for v ∈ [ 1 + α0 , α2 ], we conclude from (126) that T1 (v) is decreasing in [ 1 + α0 , α2 ].

[p.31]

                                                              p
On the other hand, T2 (v)     = v 3 − 25 v is increasing in [ 5/6, ∞) (see Section D-B1-(c)), thereby implying that it is increasing
      √                    p         √
in ⊂ [ 1 + α0 , α2 ] as 5/6 < 1 + α0 .
                   √
Let [i0 , i1 ] ⊂ [ 1 + α0 , α2 ] with i0 < i1 . The above implies that T1 (v) ≤ T1 (i0 ) and T2 (v) ≤ T2 (i1 ) for v ∈ [i0 , i1 ].
                                                          v 2 −u2 (v)
                                                                        p                          1
                                                                                                       on [i0 , i1 ]. Since v 4 − 2v 2 + 41 ≥ 0
                                                                                        4      2
                                                                                                     �
It remains √   to find an upper bound   for T 3 (v) = −2e             (  u 2 (v) − v) v   − 2v   +
                                                                                            √      4
for v ≥ 1 + α0 and is decreasing in [1, ∞) (see Section          √
                                                                    D-B1-(d)), that v → u2 − v is positive and decreasing in [0, ∞)
                                                   2              1+   8v 2 +1
(see Section D-B1-(a)), and that v �→ ev −u2 = ep      −    2      is obviously decreasing    in [0, ∞), we have that −T3 (v) =
   v 2 −u2 (v) √                  1     i20 −u2 (i0 )
                                                      ( u2 (i0 ) − i0 ) i40 − 2i20 + 41 for v ∈ [i0 , i1 ].
                         4    2
                                                                                       �
2e            ( u2 − v) v − 2v + 4 ≥ 2e

Collecting the upper bounds obtained for T1 , T2 , and T3 , we obtain
                                         max K1 (v) ≤ N (i0 , i1 ) = T1 (i0 ) + T2 (i1 ) + T3 (i0 ).                                    (128)
                                        i0 ≤v≤i1

                     √                           √                 3
                                                                                   √         √                    √
     √ the interval [ 1 + α0 , α2 ]√as follows: [ 1 + α0 , α2 ] = ∪j=1 Ij with
Partition                                                                  √ I1 = [ √1 + α0 , 1 + α0 +0.1], I2 = [√ 1 + α0 +
0.1, √1 + α0 + 0.195], and I3 = [ 1 + α0√+ 0.195, α2 ]. We find that N ( 1 + α0 , 1 + α0 + 0.1) ≈ −0.319, N ( 1 + α0 +
0.1, 1 + α0 + 0.195) ≈ −0.003, and N ( 1 + α0 + 0.195, α2 ) ≈ −0.0003.
                                                  √                                    √                 √
This shows from (128) that K1 (v) < 0 for v ∈ [ 1 + α0 , α2 ], and from (123) that H( u2 ) < 0 for v ∈ [ 1 + α0 , α2 ].
                 √
6) Proof that H( u2 ) < 0 for v ∈ [α2 , ∞): When v > α2 one can no longer use the bound K1 (v) (given in (123)) as K1 (v)
becomes rapidly positive. For instance, K1 (v) > 0 for v > α2 + 0.01 (as can be seen by plotting v → K1 (v)). We will instead
proceed as follows.
                                                    √                   � 2
First, we know (cf. Section D-B1-(b)) that T1 (v) = u2 u2 − 2v 2 + 21 ev −u2 ≤ 0 for v ≥ α1 . On the other hand, since
                                    p                                 q
                       8v 4 − 6v 2 ( 8v 2 + 1 + 4) + 1 ≤ 8α14 − 6α22 ( 8α22 + 1 + 4) + 1 ≈ −175 < 0,
for v ∈ [α2 , α1 ], we conclude from (126) that T1 (v) is decreasing in [α2 , α1 ], yielding T1 (v) ≤ T1 (α2 ) for v ∈ [α2 , α1 ].
Therefore,
                         (                       √ 2         √
                            T1 (α2 ) + v 3 − 5v − πev (erf( u2 ) − erf(v)) v 4 − 2v 2 + 41 , for α2 ≤ v < α1 ,
                                                                                            �
               √
           H( u2 ) ≤                    √ v2  2
                                                   √                                                                      (129)
                            v 3 − 5v       πe (erf( u2 ) − erf(v)) v 4 − 2v 2 + 41 ,
                                                                                  �
                                   2 −                                                           for v ≥ α1 .
We find that T1 (α2 ) ≈ 0.111.
                                     √
To find a negative upper-bound for H( u2 ) for v ∈ [α2 , ∞) we will use the bounds [1, Inq. 7.1.13, p. 298],
                                                       2                                    2
                                          2e−x                            2e−x
                              1− √         p         ≤ erf(x) ≤ 1 − √       √       ,                    x ≥ 0.                         (130)
                                     π(x + x2 + 4/π)                  π(x + x2 + 2)
Applying these bounds to the r.h.s. of (129) gives we obtain (recall that v 4 − 2v 2 + 41 > 0 for v ≥ α2 – see Section D-B1-(d))
                                            �                                 �
                                                                    v 2 −u2
                     T1 (α2 ) + v 3 − 5v         √2               2e√
                                                                                   v 4 − 2v 2 + 14 , for α2 ≤ v < α1 ,
                                                                                                  �
                                           −               −
                  
                                                              √
                  
          √                            2      v+ v 2 +2        u2 + u2 +4/π
       H( u2 ) ≤                  �                                �                                                      (131)
                                                       v 2 −u2
                           5v            2          2e
                   v − 2 − v+√v2 +2 − √ √                              v 4 − 2v 2 + 14 ,
                       3
                                                                                       �
                                                                                                     for v ≥ α1 .
                  
                  
                                                           u2 +   u2 +4/π

Lemma D.1: For v > 0,                                                   2
                                                                                                   √
                                          2            2ev −u2     1  1  e− 2v
                                         √       −√      p        ≥ − 3−       ,                                                        (132)
                                      v + v2 + 2    u2 + u2 + 4/π  v 2v    v

                     √          �          2
                                             �                                                      �             �
Proof: Let g1 (x) = 1 + x − 1 + x2 − x8 . We find g1′ (x) = 2√1+x   1
                                                                         − 12 + x4 and g1′′ (x) = 14 1 − (1+x)
                                                                                                            1
                                                                                                              3/2   ≥ 0 for x ≥ 0.
                              ′                                        ′
The latter implies that v → g1 (x) is increasing in [0, ∞), and since g1 (0) = 0, we conclude that v → g1 (x) is also increasing
in [0, ∞). The latter property and g1 (0) = 0 imply that
                                                             g1 (x) ≥ 0,         ∀x ≥ 0,                                                (133)

[p.32]

                               √
By noting that v+√2v2 +2 =   v 2 + 2 − v, we get from (133) (Hint: set x = v22 for v > 0)
                                                     r            !
                                       2                    2           1     1
                                      √       =v       1 + 2 − 1 ≥ − 3 , ∀v > 0.                            (134)
                                 v+ v +2 2                 v            v    2v
                                  √
                                      2 +1    √         √     p                 √
On the other hand, v 2 − u2 = − 1+ 8v
                                    2      ≤ − 2v and u2 + u2 + 4/π ≥ 2 u2 ≥ 2v since u2 ≥ v for v ≥ 0. Therefore,
                                                                               √
                                                   √          p              e− 2v
                                                       u2 +       u2 + 4/π ≤       ,   ∀v > 0.                                        (135)
                                                                               v
Combining (134) and (135) gives (132).
                                                                                √                     √
Applying Lemma D.1 to (131) gives (recall that v 4 − 2v 2 + 1/4 ≥ 0 for v ≥ 1 + α0 , and that α1 > 1 + α0 )
                               (                             √
                                                  2
                                                          e− 2v
                                   T1 (α2 ) − 10v8v3−1            v 4 − 2v 2 + 14 , for α2 ≤ v < α1 ,
                                                                                 �
                       √                               +
                   H( u2 ) ≤             2
                                                    √
                                                  − 2v
                                                             v                                                                        (136)
                                   − 10v8v3−1 + e v      v 4 − 2v 2 + 14 ,
                                                                        �
                                                                                    for v ≥ α1 .
         1
For v ≥ 2√ 2
             , v 4 − 2v 2 + 14 ≤ v 4 . Since 2√
                                              1
                                                2
                                                   < α2 , we get from (136)
                                             (                   2             √
                                    √             T1 (α2 ) − 10v8v3−1 √+ v 3 e− 2v ,    for α2 ≤ v < α1 ,
                                H( u2 ) ≤               2                                                                             (137)
                                                  − 10v8v3−1 + v 3 e− 2v ,              for v ≥ α1 .
                          2            √                              2          √                                          √
We first focus on − 10v8v3−1 + v 3 e− 2v . Let us show − 10v8v3−1 + v 3 e− 2v < 0, or equivalently, that (10v 2 − 1)e 2v > 8v 6 for
v ≥ α2 .
             √                                                           √
(10v 2 − 1)e 2v > 8v 6 is equivalent to g1 (v) := log(10x2 − 1) + x 2 − 6 log x − log 8 > 0. Differentiating g1 (x) gives
                                                            √                 √
                                                         10 2x3 − 40x2 − 2x + 6
                                               g1′ (x) =                                 .
                                                                   10x2 − 1
                                                                  √                 √                                                √
This derivative vanishes whenever the polynomial p1 (x) = 10 2x3 − 40x2 − 2x + 6 vanishes. Since p1 (0) = 6, p1 (1/ 2) =
−10, limx→−∞ p1 (x) = −∞, and limx→∞        √ p1 (x) = ∞ we conclude √     that this polynomial of degree 3 has three real roots,   √ one
                                                                                              ∗
located in (−∞, 0), one located in (0, 1/ 2), and one   √ ∗located in  (1/   2, ∞).  Call   v   the zero of p1 (x) located  in (1/   2, ∞).
                                                                                        ∗
Hence, the mapping v → g1 (v) is decreasing
                                     √            in (1/  2, v ) and  increasing  in (v   , ∞),   which  implies that it takes  its smallest
value at v = v ∗ in the interval (1/ 2, ∞). Solving for p1 (x) = 0 we find that v ∗ ≈ 2.81.
                                                                √
Consequently, (a) g1 (v) ≥ g1 (α2 ) if v ∈ [α2 , α1 ] since 1/ 2 < α2 < α1 < v ∗ , and (b) g1 (v) ≥ g1 (v ∗ ) for v ≥ α1 . Since
                                               √
g(v ∗ ) ≈ 0.051, property (b) implies that H( u2 ) < 0 for v ≥ α1 .
                          √                                                                          2            √
It remains to show that H( u2 ) < 0 for α2 ≤ v < α1 or, equivalently from (137), that T1 (α2 ) − 10v8v3−1 + v 3 e− 2v ≤ 0 for
α2 ≤ v < α1 .

Easy algebra gives
                                                 10v 2 − 1        √
                                                               3 − 2v
                                                                             √ �
                                                                          3 − 2v       g1 (v)
                                                                                              �
                                             −             + v  e     = v  e     1 − e          .                                     (138)
                                                   8v 3
Let v ∈ [α2 , α1 ). We have from (138)
                                             10v 2 − 1        √
                                                           3 − 2v
                                                                                     √ �
                                                                                 3 − 2v        g1 (v)
                                                                                                      �
                                T1 (α2 ) −             + v  e     = T1 (α2 ) + v   e     1 − e          ,
                                               8v 3                                  √ �               �
                                                                  ≤ T1 (α2 ) + v 3 e− 2v 1 − eg1 (α2 ) ,                              (139)

since we have shown in (a) above that g1 (v) ≥ g1 (α2 ) when v ∈ [α2 , α1 ).
                                   √                          √
Since g1 (α2 ) ≈ 26, we have v 3 e− 2v 1 − eg1 (α2 ) < α23 e− 2α1 1 − eg1 (α2 ) and, from (139),
                                                    �                            �

                                10v 2 − 1        √
                                              3 − 2v
                                                                          √
                                                                      3 − 2α1
                                                                              �
                                                                                      g1 (α2 )
                                                                                               �
                     T1 (α2 ) −           + v  e      ≤ T1 (α 2 ) + α 2 e       1 − e            ≈ −0.088 < 0.
                                  8v 3
                                  √
This concludes the proof that H( u2 ) < 0 for v ≥ α2 .

[p.33]

                                                               A PPENDIX E
                                                        P ROOF OF P ROPOSITION 4.3

                                                                         q (X)
Let q(x) = λe−λx , qγ (x) = λγ e−λγ x for x ≥ 0, and Y = log q(X)
                                                               γ
                                                                     = aγ + (λ − λγ )X, where aγ := log(λγ /λ). We assume
                                              −µx
that limγ λγ = λ. Further introduce r(x) = µe      for x ≥ 0. For x ∈ R, we have
                                                                                            [a −x]+
                                                               
                                                                  R∞           −µz        −µ λγγ −λ
                                                                     γ −x]+ µe     dz = e            ,      if λγ > λ,
                               Z ∞                             
                                                                [a
        Fr (x) := Pr (Y < x) =     1{aγ +(λ−λγ )z<x} r(z)dz =        λγ −λ
                                                                           +
                                0                               R [x−a
                                                                    λ−λγ
                                                                         γ]                       [x−a ]+
                                                                                              −µ λ−λγγ
                                                                   0         µe−µz dz = 1 − e             , if λγ < λ,
so that                                                          aγ −x
                                                       µ e−µ λγ −λ 1
                                           d            λγ −λ           {x<aγ } ,              if λγ > λ,
                                fr (x) :=    Fr (x) =             x−aγ                                                               (140)
                                          dx              µ    −µ
                                                             e λ−λγ 1
                                                                  λ−λγ          , {x>aγ }      if λγ < λ.
Using (49) we obtain (Hint: aγ < 0 when λγ < λ)
                                   R∞
                                    y
                                       1{x≥y} (x − y)fr (x)dx
   Er [(Y − y)1{Y ≥ y} | Y ≥ y] =     R∞                       ,
                                        y
                                            1{x≥y} fr (x)dx
                                                    aγ −x
                                   
                                                 −µ
                                    yaγ (x−y)e λγ −λ dx
                                     R
                                                              λ−λ      aγ −y
                                   
                                                aγ −x
                                         R aγ −µ λ
                                                             = µγ +        aγ −y ,                      for 0 ≤ y ≤ aγ and λγ > λ,
                                                                       −µ
                                   
                                                    −λ                     λγ −λ
                                                 γ
                                             e         dx           1−e
                                 =    R∞
                                          y
                                                −µ
                                                    x−aγ                                                                             (141)
                                                    λ−λγ
                                   
                                    y    (x−y)e          dx  λ−λ
                                                             = µ γ,                                     for y ≥ 0 and λγ < λ.
                                   
                                                x−aγ
                                   
                                        R ∞ −µ λ−λ
                                                    eγ           dx
                                              y

We already conclude from the above that, when λγ < λ,
                                                                             (
                                                                                 λ−λγ
                                                                                  λ ,      when r = q,
                                 sup Er [(Y − y)1{Y ≥y} | Y ≥ y] =               λ−λγ                                                (142)
                                 y≥0                                              λγ ,     when r = qγ .
                                                          a −y
Assume now that λγ > λ. Define f (y) = d1 + 1−e−d(a
                                                γ
                                                    γ −y)
                                                          with d := λγµ−λ , so that (cf. (141))
                                        sup Er [(Y − y)1{Y ≥y} | Y ≥ y] =               sup f (y).
                                        y≥0                                        0≤y≤aγ

We find
                                                        −1 + e−d(aγ −y) + d(aγ − y)e−d(a−y)
                                        f ′ (y) =                                �2         .
                                                                  1 − e−d(aγ −y)
The derivative of the numerator of f ′ (y) is equal to d2 (a − y)e−d(aγ −y ), which is non-negative for y ∈ [0, aγ ]. Consequently
                                                                                                                  2(λγ −λ)
the mapping y → f (y) is non-decreasing in [0, aγ ]. By L’Hôpital’s rule we get that limy→aγ f (y) = d2 =            µ    , so that
from (141)                                                         (
                                                                       2(λγ −λ)
                                                                          λ     ,   when r = q,
                             sup Er [(Y − y)1{Y ≥y} | Y ≥ y] =         2(−λγ −λ)                                              (143)
                             y≥0                                           λγ     , when  r = qγ ,
when λγ > λ. We conclude from (142)-(143) that limγ supy≥0 Er [Y − y | Y ≥ y] = 0 for r ∈ {q, qγ }.

Consider now the infimum. We have from (50) and (140)
                                  Ry
                                       1{x≤y} (x − y)fr (x)dx
  Er [(Y − y)1{Y ≤ y} | Y ≤ y] = −∞R y                           ,
                                            1{x≤y} fr (x)dx
                                  −∞                aγ −x
                                     Ry           −µ
                                                     λγ −λ
                                 
                                      −∞
                                          (x−y)e           dx   λ−λ
                                                              = µ γ,                                    for y ≤ 0 and λγ > λ,
                                 
                                 
                                                 aγ −x
                                       Ry     −µ
                                                  λγ −λ
                                             e          dx
                                 
                                         −∞
                               =     Ry         −µ
                                                    x−aγ                                                                             (144)
                                                    λ−λγ
                                     aγ
                                         (x−y)e           dx   λ−λ                      y−aγ
                                                              = µγ −                                    for aγ ≤ y ≤ 0 and λγ < λ.
                                 
                                 
                                               x−aγ
                                        R y −µ λ−λ                                       µ(y−aγ )   ,
                                                                                     −
                                 
                                                                                          λ−λγ
                                                    γ
                                              aγ
                                                   e          dx                  1−e

Mimicking the analysis for the supremum, we easily get from (144) that limγ inf y≤0 Er [(Y − y)1{Y ≤ y} | Y ≤ y] = 0 for
r ∈ {q, qγ }. This concludes the proof.

[p.34]

                                                                     R EFERENCES

 [1] M. Abramowitch and I. A. Stegun, Handbook of Mathematical Functions. Dover, 1965.
 [2] B. A. Bash, D. Goeckel, and D. Towsley, “Limits of Reliable Communication with Low Probability of Detection on AWGN Channels,” EEE Journal
     on Selected Areas in Communications, Vol. 31, No. 9, pp. 1921–1930, 2013.
 [3] M. Basseville and I. V. Nikiforov, Detection of Abrupt Changes: Theory and Application. Prentice Hall, Englewood Cliffs, vol. 104, 1993.
 [4] M.-C. Chang and M. R. Bloch, “Covert Sequential Hypothesis Testing,” in Proc. 2021 IEEE Information Theory Workshop (ITW), Kanazawa, Japan,
     pp. 1–6, 2021.
 [5] R. M. Corless, G. H. Gonnet, D. E. G. Hare, D. J. Jeffrey, and D. E. Knuth, “On the Lambert W function,” Advances in Computational Mathematics,
     Vol. 5, pp. 329–359, 1996.
 [6] K.-W. Huang, H.-M. Wang, and H. V. Poor, “On Covert Communication Against Sequential Change-Point Detection,” EEE Transactions on Information
     Theory, Vol. 67, No. 11, pp. 7285–7303, 2021.
 [7] R. A. Khan, “Wald’s Approximations to the Average Run Length in CUSUM Procedures,” Journal of Statistical Planning and Inference, Vol. 2, pp.
     63-77, 1978.
 [8] G. Lorden, “Procedure for Reaction to a Change in Distribution,” The Annals of Mathematical Statististics, Vol. 42, No. 6, pp. 1897-1908, 1971.
 [9] G. V. Moustakides, “Optimal Stopping Times for Detecting Changes in Distributions,” Annals of Statistics, Vol. 14, No. 4, pp. 1379-1387, 1986.
[10] E. S. Page, “Continuous Inspection Schemes,” Biometrika, Vol. 41, pp. 100-114, 1954.
[11] H. V. Poor and O. Hadjiliadis, Quickest Detection. Cambridge University Press, 2009.
[12] A. R. Ramtin, Z. Hare, L. Kaplan, P. Nain, V. V. Veeravalli, and D. Towsley, “Quickest Change Detection in the Presence of Covert Adversaries,” in
     Proc. MILCOM 2024 - IEEE Military Communications Conference (MILCOM), pp. 1–6, 2024.
[13] A. R. Ramtin, P. Nain, D. S. Menasche, D. Towsley, and E. de Souza e Silva, “Fundamental Scaling Laws of Covert DDoS Attacks,” Performance
     Evaluation, Vol. 151, p. 102236, 2021.
[14] A. R. Ramtin, P. Nain, and D. Towsley, “Quickest Change detection in Continuous Time in Presence of a Covert Adversary,” IEEE Signal Processing
     Letters, pp. 1–4, 2025, doi: 10.1109/LSP.2025.3628793.
[15] D. Siegmund, Sequential Analysis, Tests and Confidence Intervals. Springer Verlag, 1985.
[16] A. Tartakovsky, I. V. Nikiforov, and M. Basseville, Sequential Analysis, Hypothesis Testing and Change Point Detection. Chapman & Hall/CRC Press,
     Monographs on Statistics & Applied Probability, Vol. 136, 2014.
[17] V. V. Veeravalli and T. Banerjee, Quickest Change Detection. In Academic press library in signal processing: Array and statistical signal processing,
     2013. Also available at http://arxiv.org/abs/1210.5552.
[18] A. Wald, Sequential Analysis. Wiley, New York, 1947.
[19] L. Xie, S. Zou, Y. Xie, and V. V. Veeravalli, “Sequential (Quickest) Change Detection: Classical Results and New Directions,” IEEE Journal on Selected
     Areas in Information Theory, Vol. 2, No. 2, pp. 494–514, 2021.


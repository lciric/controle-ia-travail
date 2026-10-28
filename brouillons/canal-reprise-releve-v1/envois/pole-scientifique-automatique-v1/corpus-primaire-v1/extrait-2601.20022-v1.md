# EXTRAIT — Quickest Change Detection in Discrete-Time in Presence of a Covert Adversary

- Auteurs : Amir Reza Ramtin, Philippe Nain, Don Towsley ; année : 2026 (v2 du 16 février 2026) ; identifiant : arXiv:2601.20022v2 (34 pages)
- Statut : préimpression arXiv cs.IT ; Université du Massachusetts à Amherst et Inria (centre de l'Université Côte d'Azur) ; article de théorie de la détection de rupture, hors du champ de la sécurité des modèles de langage
- PDF source : `docs/sources/pdf/2601.20022v2.pdf` ; SHA-256 du PDF : `8d090f3171ef76cad597ab263a2de9df49de1d1accf78a8afff55ceb82881b42` (compagnon `.sha256` du dépôt vérifié par `sha256sum -c`)
- Pages gardées en tout ou en partie : 1-12
- Nature : texte du PDF repris mot pour mot (`pdftotext`, lignes rejointes en paragraphes), numéro de page du PDF en `[p.N]` au début de chaque passage ; coupes marquées `[COUPÉ]` ; tableaux et figures extraits en texte, mise en forme possiblement perdue (en cas de doute sur un chiffre de figure, se reporter à la page citée). Aucun chiffre retapé à la main (R7).
- Retiré pour sûreté (niveau méthode seulement) : rien (article théorique : aucune recette d'attaque). Les démonstrations des propositions sont omises par économie de place, les énoncés et hypothèses sont gardés.

---

[p.1]
Abstract We study the problem of covert quickest change detection in a discrete-time setting, where a sequence of observations undergoes a distributional change at an unknown time. Unlike classical formulations, we consider a covert adversary who has knowledge of the detector’s false alarm constraint parameter γ and selects a stationary post-change distribution that depends on it, seeking to remain undetected for as long as possible. Building on the theoretical foundations of the CuSum procedure, we rigorously characterize the asymptotic behavior of the average detection delay (ADD) and the average time to false alarm (AT2FA) when the post-change distribution converges to the pre-change distribution as γ → ∞. Our analysis establishes exact asymptotic expressions for these quantities, extending and refining classical results that no longer hold in this regime. We identify the critical scaling laws governing covert behavior and derive explicit conditions under which an adversary can maintain covertness, defined by ADD = Θ(γ), whereas in the classical setting, ADD grows only as O(log γ). In particular, for Gaussian and Exponential models under adversarial perturbations of their respective parameters, we asymptotically characterize ADD as a function of the Kullback–Leibler divergence between the pre- and post-change distributions and γ. Index Terms Sequential analysis; Discrete-time detection; Quickest change detection; CuSum procedure; Covert adversary.

I. I NTRODUCTION The problem of sequential change detection or quickest change detection (QCD), arises in various engineering applications [11], [16], [17]. In all of these applications, the decision-making agent receives a sequence of stochastic observations that undergo a change in distribution in response to a change or disruption in the environment. As long as the behavior of the observations is consistent with the normal (pre-change) state, the decision-maker is content to allow the process to continue. If the distribution changes, then the decision-maker is interested in detecting the change as soon as possible and taking any necessary action in response to the change. More precisely, the goal of the decision-maker is to make the average detection delay (ADD) as small as possible, while constraining the average time to false alarm (AT2FA) to be above some threshold. Detecting adversarial behavior is one of the most critical applications of QCD [19]. Traditional analyses, however, typically assume that potential adversaries are unaware of the underlying detection mechanism and therefore cannot adjust their actions to avoid being caught. In modern interconnected systems, this assumption is increasingly less realistic – sophisticated adversaries can often infer or estimate aspects of the detection strategy and intentionally manipulate their behavior to remain undetected. Such covert adversarial behavior poses new challenges for QCD, especially in security-sensitive domains such as cyber defense, surveillance, and military operations, where even small delays in detection can lead to significant consequences. A. Ramtin and D. Towsley were supported by the DEVCOM Army Research Laboratory under Cooperative Agreement W911NF-17-2-0196 (IoBT CRA) and the National Science Foundation under Grant ECCS-2148159.

[p.2]
The notion of covertness, originally introduced in the context of covert communication [2], refers to the ability of a transmitter to remain undetectable by an observing warden during communication. Most existing work on covert communication assumes that the detector knows the exact start time of any potential transmission. In contrast, we relax this assumption by extending the notion of covertness to the QCD setting, where adversaries deliberately act to remain hidden over prolonged time horizons. This departure results in a fundamentally different adversarial strategy when considered within the framework of QCD. Unlike traditional adversaries whose actions result in detectable statistical deviations, covert adversaries aim to ensure that ADD scales with the same order as AT2FA, thereby rendering the QCD procedure ineffective [6]. In this work, we specifically focus on the theoretical characterization of covert adversarial behavior against the Cumulative Sum (CuSum) procedure. The CuSum procedure, first proposed by Page [10], is one of the most widely studied methods in quickest change detection. It operates by recursively accumulating log-likelihood ratios of the observed data and signaling an alarm when this cumulative statistic exceeds a prescribed threshold. The CuSum test is well known for its optimality under Lorden’s minimax criterion [8], which minimizes the worst-case expected detection delay subject to a false-alarm constraint. Classical analyses, including Lorden’s asymptotic characterization of ADD, assume that the post-change distribution is fixed and independent of the false-alarm constraint γ. In more realistic adversarial settings, however, this assumption may not hold: a covert adversary can deliberately choose a post-change distribution that depends on γ, causing the post-change and pre-change distributions to become increasingly similar as γ grows. This dependence invalidates classical asymptotic results and motivates the need for new analyses of scaling stationary post-change models, in which the post-change distribution converges to the pre-change distribution as γ → ∞. While prior work has examined covertness in both discrete-time [6], [12] and continuous-time sequential detection settings [14], these studies differ substantially from our formulation. The work in [6] is primarily rooted in covert wireless communication, where the modeling assumptions are tailored to communication-theoretic contexts – such as specific channel models and power constraints – and the focus lies on communication-centric performance metrics rather than fundamental detection limits. In contrast, [12] investigates an adversarial setting against the CuSum procedure under non-stationarity, without assuming that the adversary knows the false-alarm constraint parameter, whereas in our work the post-change distribution explicitly depends on this parameter. Consequently, the formulation in [12] differs fundamentally from ours. The study most closely related to our framework is the continuous-time analysis in [14], which considers a Brownian-motion model where the post-change drift depends on the false-alarm constraint. However, that setting benefits from closed-form expressions for both ADD and AT2FA, allowing for exact characterizations. In contrast, the discrete-time case analyzed here is significantly more challenging, as no such exact equalities exist between ADD, AT2FA, the detection threshold, and the Kullback–Leibler divergence – necessitating a refined asymptotic analysis to obtain precise scaling results. We provide a rigorous asymptotic analysis under a discrete-time stationary setting in which the post-change distribution depends on the false-alarm constraint parameter γ, deriving a novel asymptotic characterization of ADD for the CuSum procedure when the difference between the pre-change and post-change distributions diminishes as γ → ∞. In this regime, we demonstrate that the classical asymptotic result for ADD due to Lorden no longer applies. Our principal theoretical contribution – motivated by the need to analyze the asymptotics of ADD in this challenging setting – is the establishment of precise asymptotic expressions for both AT2FA and ADD, formulated in terms of the Kullback–Leibler divergence between the post-change and pre-change distributions and the detection threshold. These expressions, previously regarded as approximations in classical works such as [7], [15], are rigorously proven to be asymptotically exact in our regime, thereby substantially strengthening the theoretical underpinnings of QCD. [COUPÉ]

[p.3]
Moreover, we investigate precise conditions under which an adversary can maintain covertness, which we define as the scenario in which the best achievable ADD, under the constraint that AT2FA is at least γ, grows asymptotically as Θ(γ). We formalize this definition in our analysis, noting that it aligns closely with the notion of covertness introduced in [6]. Through our theoretical framework, we characterize the required rate at which the post-change distribution must converge to the pre-change distribution in order to preserve covertness. In this formulation, the adversary’s control over the post-change distribution models its ability to influence how the statistical properties of the observations evolve after the change. By selecting post-change distributions that are closer to the pre-change distribution, the adversary can delay detection while remaining covert, a perspective consistent with [14]. We take this as motivation for studying adversarial choices of post-change distributions, since delayed detection increases the duration over which the adversary can influence the system before being detected. We also quantify the extent of this influence by building upon the notion of total damage introduced in [12], which measures the cumulative impact incurred prior to detection, and study its asymptotic scaling. To illustrate our theory, we analyze Gaussian-distributed (resp. exponential-distributed) observations, explicitly studying adversaries that manipulate both the mean and variance parameters (resp. mean) as functions of γ. While adversaries that vary the variance have been previously considered in the covert communication literature, adversaries who adjust the mean are motivated by volume-based attacks that aim to increase activity levels without triggering detection [13]. We prove that our theoretical results apply to this model by conducting a detailed analysis showing that the conditions established in the preceding section – which are sufficient to ensure that the overshoots vanish – are indeed satisfied as γ → ∞. This validation confirms that the asymptotic expressions for AT2FA and ADD remain accurate even in this parametric Gaussian/exponential setting, thereby demonstrating the broad applicability of our asymptotic framework. We then explore how the ADD scales based on the rate at which the post-change distribution converges to the pre-change distribution, and establish conditions under which covertness is maintained in the Gaussian (resp. exponential) case.

II. BASIC ELEMENTS OF CHANGE - POINT DETECTION IN DISCRETE - TIME Let X1 , X2 , . . . be mutually independent random variables (rvs) taking values in a measurable space X . Denote by Fk = σ(X1 , . . . , Xk ) the smallest σ-fied generated by X1 , . . . , Xk . Random variables X1 , . . . , Xt−1 have common (pre-change) probability distribution Q0 while rvs Xt , Xt+1 , . . . have common (post-change) probability distribution Q1 , distinct from Q0 1 . Denote by Et the expectation operator associated with this model. The change time t is unknown but constant (non-Bayesian setting). The case t = ∞ corresponds to no change occurring, i.e., only the distribution Q0 is used, and t = 1 corresponds to the situation where only Q1 is used. We assume that Q0 and Q1 have probability density functions (pdfs), denoted by q0 and q1 , respectively, and that the log-likelihood log(q1 (X)/q0 (X)) is finite a.s. under both Q0 and Q1 . Recall that the Kullback–Leibler (KL) divergence of a pdf p1 from a pdf p2 , defined on the same measurable space, is D(p1 ||p2 ) = E[log(p1 (X)/p2 (X)), with X a rv with pdf p1 , whenever this expectation is finite; if so, D(p1 ||p2 ) ≥ 0, with D(p1 ||p2 ) = 0 if and only if pdfs p1 and p2 are identical. Denote by T the set of all (possibly extended) stopping times with respect to the filtration F := {Fk , k ≥ 1}. Fix γ ∈ (0, ∞). Lorden’s classical problem [8] consists in minimizing d(T ) := sup ess supEt [(T − t + 1)+ | Ft−1 ], t≥1

over all stopping times T ∈ T such that E∞ [T ] ≥ γ. In words, the goal is to minimize the worst-case average detection delay under a constraint on the false alarm rate (i.e., 1/E∞ [T ] ≤ 1/γ). Define n(γ) = inf {T ∈T :E∞ [T ]≥γ} d(T ), the optimal worst-case average detection delay. 1 Our notation follows that in [11]. We note that some works in the quickest change detection literature instead use ν for the change-point, and f , f for 0 1 the pre- and post-change densities, respectively, along with Pk , P∞ and Ek , E∞ for the corresponding probability measures and expectations.

[p.4]
Moustakides [9] (see also [11, Section 6.2]) showed that Page’s Cumulative Sum (CuSum) stopping rule [10]   k   X q1 (Xi ) τh = inf k ≥ 0 : max log ≥ h , h > 0,   1≤j≤k+1 q0 (Xi )

(1)

i=j

solves Lorden’s optimization problem if h is selected so that Eq0 [τh ] = γ. It is known that d(τh ) = Eq1 [τh ] for h > 0 [11, p. 143], [15, p. 25], thereby implying that n(γ) = Eq1 [τh⋆ ], ⋆

(2)

⋆

with h = h solution of Eq0 [τh ] = γ. Since τ0 = 0, notice that h > 0 for γ > 0. There is in general no closed-form expression for n(γ). The behavior of n(γ) as γ → ∞ was obtained by Lorden [8], [11, Thm 6.17, p. 160]. It is given by log γ n(γ) ∼ , γ → ∞. (3) D(q1 ||q0 ) The aim of this work is to revisit Lorden’s result when q1 depends on γ and q1 converges pointwise to q0 as γ → ∞. Notation: For any event A, 1A = 1 if A if true and zero otherwise. If a function f is differentiable at x0 ∈ R, we denote by f ′ (x0 ) its derivative at this point. The shorthands f (x) ∼x g(x) and limx f (x) will stand for f (x) = g(x) + o(1) (x → ∞) and limx→∞ f (x), respectively. III. L IMITING BEHAVIOR OF n(γ) WHEN q1 DEPENDS ON γ We still consider the setting in Section II but we now assume that q1 depends on γ with limγ q1 = q0 . We further assume2 that Xk ∈ R = (−∞, ∞) (k ≥ 1). To make explicit the dependence on γ, q1 will now be denoted by qγ . For simplicity, q0 is denoted by q. We denote by Pp and Ep the probability and expectation operators associated with the pdf p ∈ {q, qγ }. In other words, under Pqγ (resp. Pq ), X1 , X2 , . . . are i.i.d. real-valued rvs with common pdf qγ (resp. q). We further assume that there exists γ0 > 0 such that3 qγ ̸= q for all γ > γ0 . Since we are only interested in limiting results when γ → ∞, we will actually assume, without loss of generality, that qγ ̸= q for all γ > 0. Last, we assume that the log-likelihood ratio log(qγ (X1 )/q(X1 )) is finite Pqγ -a.s. (resp. Pq -a.s.) for all γ > 0. Our goal is to find conditions on qγ ensuring covertness of an attacker. We say that an attacker is covert if n(γ) = Θ(γ), namely, for large γ, the optimal worst-case average detection delay is of the same order of magnitude as the largest admissible lower bound on the expected time between false alarms. In addition to analyzing n(γ), we also introduce a measure of the impact that a change in distribution may have on the system prior to detection. We model this impact through a damage measure defined as a function of the KL divergence between the pre-change and post-change models [12]. Specifically, let g : R+ → R+ be a strictly increasing function with g(0) = 0 Then, the corresponding total expected damage accrued up to the detection time is defined as  d(γ) = n(γ)g D(q||qγ ) . (4)

[p.5]
Propositions 3.1-3.2 and Lemma 3.1 will be proved under the conditions that the expected overshoots converge to zero as γ → ∞ , namely, lim Ep [ST − b | ST ≥ b] = 0,

(6)

lim Ep [ST − a | ST ≤ a] = 0,

(7)

γ

γ

for p ∈ {q, qγ }. Conditions (6)-(7) are not easy to check since they involve the (unknown) overshoot random variables ST − a and ST − b. In Lemma 3.2 we will provide sufficient conditions for (6)-(7), easier to verify than conditions (6)-(7). Proposition 3.1: Assume that conditions (6)-(7) are satisfied. Then, for a < 0 < b, A(B − 1)a + B(1 − A)b , D(qγ ||q)(B − A) (B − 1)a + (1 − A)b Eq [T ] ∼γ − , D(q||qγ )(B − A)

Eqγ [T ] ∼γ

(8) (9)

with A = ea and B = eb .

[p.6]
Proposition 3.2: If conditions (6)-(7) hold, then 1 (e−h + h − 1), D(qγ ||q) 1 Eq [τh ] ∼γ (eh − h − 1). D(q||qγ )

Eqγ [τh ] ∼γ

(23) (24)

[COUPÉ]

[p.7]
The proofs of Propositions 3.1-3.2 and of Lemma 3.1 are inspired by the proofs of several elementary results in sequential β detection theory. These include the bounds (in our notation) 1−β α ≥ B and 1−α ≤ A [11, Prop. 4.10], [18, p. 45], Eq [T ] ≥ β α 1−α −1 −1 D(q||qγ ) [α log 1−β + (1 − α) log β ] and Eqγ [T ] ≥ D(qγ ||q) [(1 − β) log 1−β α + γ log 1−α ] [11, Prop. 4.11], [15, Thm 2.39]. It is also worth noting that the r.h.s. of (8) and (9) provide known approximations for Eqγ [T ] and Eq [T ], respectively, where the approximation, due to Wald [18], originates from neglecting the excess over the boundaries a and b, i.e., ST ≈ a or ST ≈ b [11, p. 77]. Proposition 3.1 says that these approximations give the exact limiting behavior of Eqγ [T ] and Eq [T ] as γ → ∞, when limγ qγ = q and conditions (6)-(7) are met. The r.h.s. of (23)-(24) are nothing but Khan’s approximations for Eqγ [τh ] and Eq [τh ] [7, Corollary, p. 76], [15, Eqns (2.54), p. 26]. Proposition 3.2 shows that these approximations are exact when limγ qγ = q and conditions (6)-(7) hold. In Lemma 3.2 below we provide sufficient conditions for (6)-(7) to hold. These new conditions only involve the rv Y = qγ (X) , making them easier to check. log q(X) Lemma 3.2: Condition (6) holds if lim sup Ep [Y − y | Y ≥ y] = 0,

(28)

lim inf Ep [Y − y | Y ≤ y] = 0,

(29)

γ y≥0

and condition (7) holds if γ y≤0

q (X)

γ for p ∈ {q, qγ }, with Y = log q(X) and X a real-valued random variable.

[p.8]
Remark 3.1 (Sufficient condition for (6)-(7) to hold): Conditions (6)-(7) will hold if (C) q(x) → 1 uniformly on R as γ → ∞.

q (x)

q (x)

γ γ This is so as 0 ≤ Ep [ST − b | ST ≥ b] ≤ supx∈R log q(x) and inf x∈R log q(x) ≤ Ep [ST − a | St ≤ a] ≤ 0, and that

q (x)

q (x)

γ γ limγ inf x∈R log q(x) = limγ supx∈R log q(x) = 0 under (C). Condition (C) is of course very restrictive; in particular, it does not hold for the Gaussian and exponential models discussed in Section IV. It will hold, for instance, if rvs {Xk }k have a finite support in R.

Proposition 3.3 (Limiting behavior of n(γ)): When conditions (6)-(7) hold,  log(γD(q||qγ ))  , if limγ γD(q||qγ ) = ∞,  D(qγ ||q)  γD(q||qγ ) G(y) n(γ) ∼γ D(qγ ||q) y , if limγ γD(q||qγ ) = y ∈ (0, ∞),    γD(q||qγ ) , if limγ γD(q||qγ ) = 0,

(35)

(36)

D(qγ ||q)

[COUPÉ]

[p.9]
where the mapping G(y) given by G(y) = e1+y+W−1 (−e

−1−y

)

− W−1 (−e−1−y ) − y − 2,

(37)

G(y) G(y) satisfies G(y) y ∈ (0, 1) when 0 < y < ∞, limy↓0 y = 1 and limy→∞ y = 0.

Corollary 3.1: The largest asymptotic order of n(γ) is reached when γD(q||q0 ) = y + o(1) (γ → ∞), and it corresponds to covertness, i.e., n(γ) = Θ(γ). Remark 3.2 (Asymptotic behavior of h⋆ (γ)): When conditions (6)-(7) hold,  if limγ γD(q||qγ ) = ∞,  log(γD(q||qγ )), −1−y −1 − y − W (−e ), if limγ γD(q||qγ ) = y ∈ (0, ∞), h⋆ (γ) ∼γ −1  p 2γD(q||qγ ), if limγ γD(q||qγ ) = 0.

(43)

[p.10]
We now analyze the asymptotic behavior of the adversary’s total damage as defined in (4). Proposition 3.4: Assume g(x) = xρ with ρ ∈ (0, 1) and that limγ D(q||qγ )/D(qγ ||q) = c for some c > 0. Then, if conditions (6)–(7) hold, the total damage d(γ) = n(γ)g(D(q||qγ )) has its largest asymptotic order when γD(q||qγ ) = Θ(1), with d(γ) = Θ(γ 1−ρ ). ρ

Note that, in the setting of the above proposition and following Proposition 3.3, the regime γD(q||qγ ) = Θ(1) coincides with the transition between detectability and covertness. IV. A PPLICATION TO G AUSSIAN AND EXPONENTIAL MODELS In this section, we first address the situation when both the pre-change and post-change distributions are Gaussian distributions, then we investigate the case when both distributions are exponential.

[p.11]
Proposition 4.2: For Gaussian pdfs q and qγ given in (44),   2 4 log γ µ2 + σ4 √ √   , if |µ| γ ∼γ ∞ or if σ 2 γ ∼γ ∞,  1 2 1 4 2µ +4σ n(γ) ∼γ if 12 γ(µ2 + 12 σ 4 ) ∼γ y ∈ (0, ∞), γ G(y)  y ,  √ √  γ, if |µ| γ ∼γ 0 & σ 2 γ ∼γ 0,

(45)

where G(y) is defined in (37).

Proposition 4.2 shows that an attacker is covert if either (i) 12 γ(µ2 + 12 σ 4 ) converges to a positive constant as γ → ∞, or if √ √ (ii) |µ| γ ∼γ 0 and σ 2 γ ∼γ 0. Hence, covertness will occur, in particular, when (µ, σ 2 ) = (γ −δ1 , γ −δ2 ) with δ1 ≥ 21 and δ2 ≥ 12 . √ We now focus on the √ total damage through two representative examples. We take g(x) = x and let σ = 0. In this case, g(D(q||qγ )) ∼ |µ|/ 2. Consequently, the total damage d(γ) = n(γ)g(D(q||qγ )) is proportional to n(γ)|µ|, which corresponds to the total mean shift introduced by the adversary prior to detection. Then, following Proposition 3.4, when γD(q||qγ ) = Θ(1), √ √ which here implies µ = Θ(1/ γ), the total damage is maximized and satisfies d(γ) = Θ( γ). Similarly, if we instead set 2 µ = 0 and allow σ ̸= 0, then d(γ) is proportional to n(γ)σ , which corresponds to the total power injected by the adversary √ prior to detection in a wireless communication setting. Then, under σ 2 = Θ(1/ γ), the total damage is maximized with √ d(γ) = Θ( γ). The same scaling law was also reported in [6] for this communication setting.

[p.12]
V. C ONCLUSION In this work, we developed an asymptotic framework for covert quickest change detection in discrete time, analyzing the CuSum procedure in a stationary setting where the post-change distribution qγ depends on the false-alarm constraint γ and approaches the pre-change distribution as γ → ∞. Classical QCD analyses do not allow such γ-dependent post-change models, and therefore cannot capture this covert regime. We showed that standard asymptotic characterizations of detection delay fail under this dependence, and we established conditions under which the overshoot of the CuSum statistic vanishes asymptotically, enabling sharp and rigorous characterizations of both AT2FA and ADD. We further verified, in Gaussian and exponential models, that these conditions hold under convergence of qγ to q in parameter space as γ → ∞. We also derived the scaling laws under which an adversary can preserve covertness. A natural direction for future research is to identify structural properties of the pdfs qγ and q that would guarantee that sufficient conditions (28) and (29), for the vanishing of the overshoots, are automatically satisfied.

[COUPÉ : p.5-10 démonstrations des propositions 3.1 à 3.4 et du lemme 3.2 ; p.10-11 énoncés pour les lois exponentielles ; p.12-34 annexes de démonstration (propositions 4.1 et 4.3 : conditions de dépassement) et bibliographie]

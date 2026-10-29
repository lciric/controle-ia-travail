# TEXTE INTÉGRAL — arXiv:2509.17778v1

- Identifiant : arXiv:2509.17778v1
- Titre (tel qu'écrit dans le PDF) : Quickest Change Detection in Continuous-Time in Presence of a Covert Adversary
- PDF source : `docs/sources/pdf/2509.17778v1.pdf` ; SHA-256 du PDF : `97d000252b768e69113437cce1a88a24488cbe3f92a1a724ea39c0c9f87d8d5e` (compagnon `.sha256` vérifié par `sha256sum -c` avant lecture)
- Outil d'extraction : `pdftotext -layout -enc UTF-8` (pdftotext version 24.02.0), page par page, marqueur `[p.N]` au début de chaque page (N = numéro de page du PDF, à partir de 1)
- Nombre de pages : 4
- Caractères de contrôle produits par l'extraction (glyphes de polices sans correspondance : délimiteurs de formules, texte de figures à police codée) : 12, les caractères nuls supprimés, les autres remplacés par le caractère de remplacement U+FFFD (position gardée) ; pages : 2 (1), 3 (11)
- Nombre de caractères du texte extrait (marqueurs `[p.N]` compris, en-tête exclu) : 36149
- Mention : texte intégral, aucun retrait, contenu d'attaque verbatim possible — dépôt privé seulement (jamais dans la copie expurgée publique ; règle de sûreté modifiée par R-439).
- Provenance : tout chiffre repris ailleurs doit citer la page `[p.N]` et être relu sur le PDF empreinté (R7). La mise en page en colonnes, les formules et les tableaux peuvent être mal ordonnés dans l'extraction : se reporter au PDF.

---

[p.1]

                                                                                                                                                                                         1




                                             Quickest Change Detection in Continuous-Time in
                                                      Presence of a Covert Adversary
                                                                       Amir Reza Ramtin, Philippe Nain, Don Towsley, Life Fellow, IEEE




                                            Abstract—We investigate the problem of covert quickest change              the form of log-likelihood ratios) and signals a change once
                                         detection in a continuous-time setting, where a Brownian motion               this cumulative evidence crosses a predetermined threshold [7],
                                         experiences a drift change at an unknown time. Unlike classical               [8]. Precise characterizations of performance metrics, such as
                                         formulations, we consider a covert adversary who adjusts the
                                         post-change drift µ = µ(γ) as a function of the false alarm                   average time to false alarm (AT2FA) and average detection delay
                                         constraint parameter γ, with the goal of remaining undetected                 (ADD), are available in closed form for standard continuous-
arXiv:2509.17778v1 [cs.IT] 22 Sep 2025




                                         for as long as possible. Leveraging the exact expressions for the             time models [7].
                                         average detection delay (ADD) and average time to false alarm                    An important application of QCD is detecting the presence of
                                         (AT2FA) known for the continuous-time CuSum procedure, we                     an adversary [13]. However, classical analyses typically assume
                                         rigorously analyze how the asymptotic behavior of ADD evolves
                                         as µ(γ) → 0 with increasing γ. Our results reveal that classical              that the adversary is unaware of the detection mechanism.
                                         detection delay characterizations no longer hold in this regime.              In adversarial environments, these assumptions may no longer
                                         We derive sharp asymptotic expressions for the ADD under                      hold. Specifically, an adversary, aware of the detection mech-
                                         various convergence rates of µ(γ), identify precise conditions for            anism, may strategically adapt their behavior in response to
                                         maintaining covertness, and characterize the total damage inflicted           detection thresholds. In this scenario, the adversary’s statistical
                                         by the adversary. We show that the adversary achieves
                                                                                           √      maximal
                                         damage when the drift scales as µ(γ) = Θ(1/ γ), marking a                     signature post-change increasingly resembles the pre-change
                                         fundamental trade-off between stealth and impact in continuous-               condition as the false-alarm constraint (quantified by a parame-
                                         time detection systems.                                                       ter γ) becomes increasingly stringent. Such adaptive adversarial
                                            Index Terms—Continuous-time detection; Quickest change de-                 behavior challenges traditional assumptions and necessitates a
                                         tection; CuSum procedure; Covert adversary; Brownian motion;                  deeper theoretical analysis of covert adversaries operating in a
                                         Lambert function;                                                             continuous-time setting.
                                                                                                                          The notion of covertness, first introduced by Bash et al. in
                                                                   I. I NTRODUCTION                                    the context of covert communication [1], captures the ability of
                                            Quickest change detection (QCD) has long been a funda-                     a transmitter to remain undetectable by an observing warden
                                         mental statistical technique for rapidly identifying changes in               during communication. Most existing work assumes that the
                                         the underlying statistical properties of observed processes, with             detector knows the exact start time of any potential transmission.
                                         numerous critical applications ranging from quality control                   In contrast, we relax this assumption and extend the notion of
                                         and finance to security and environmental monitoring [8], [9],                covertness to a sequential detection framework, where adver-
                                         [11]. Traditionally formulated in discrete-time settings, QCD                 saries deliberately behave in a way that keeps their activity con-
                                         methods have also been extensively developed and analyzed                     cealed over extended periods. From the perspective of sequential
                                         within continuous-time frameworks, where processes are moni-                  detection, this gives rise to a fundamentally different adversarial
                                         tored continuously rather than at discrete intervals. Continuous-             strategy. Unlike traditional adversaries whose actions lead to
                                         time detection is particularly advantageous in settings requiring             detectable statistical deviations—enabling timely detection—
                                         immediate responses to subtle or rapid shifts, as it allows for               covert adversaries aim to remain hidden by ensuring that ADD
                                         instantaneous detection of changes, thereby reducing reaction                 scales with the same order as AT2FA, thereby rendering the
                                         times and potential damages [2], [8], [9].                                    detector ineffective [5].
                                            A classical and widely used method in continuous-time QCD                     While prior work has studied covertness in discrete-time se-
                                         is the continuous-time Cumulative Sum (CuSum) procedure,                      quential detection [3], [5], [12], the continuous-time counterpart
                                         initially studied by Lorden [6] and subsequently generalized                  of this problem remains relatively unexplored. The works in [3],
                                         by Moustakides [7]. The continuous-time CuSum is known for                    [5] have been largely confined to covert wireless communication
                                         its optimality under Lorden’s minimax criterion, which aims to                scenarios, with assumptions tailored to that domain—such as
                                         minimize the worst-case expected detection delay while control-               specific channel models or power constraints—and have primar-
                                         ling the average time between false alarms. Under this criterion,             ily focused on communication-centric performance metrics. In
                                         the CuSum procedure continuously accumulates evidence (in                     contrast, [12] considers an adversarial setting against the CuSum
                                                                                                                       procedure under non-stationarity and without assuming that the
                                           This research is supported by the DEVCOM Army Research Laboratory under     AT2FA constraint is known to the adversary.
                                         Cooperative Agreement W911NF-17-2-0196 (IoBT CRA) and the National
                                         Science Foundation under Grant ECCS-2148159.                                     In this paper, we rigorously investigate covert adversaries in
                                           The authors are grateful to Professor Venugopal V. Veeravalli for helpful   a continuous-time CuSum framework, where the post-change
                                         comments and suggestions.                                                     drift parameter is allowed to depend explicitly on the false-
                                           A. R. Ramtin and D. Towsley are with the University of Massachusetts at
                                         Amherst, MA, USA (email: aramtin@cs.umass.edu, towsley@cs.umass.edu).         alarm constraint parameter γ. Specifically, we examine scenarios
                                           P. Nain is with Inria, France (email: philippe.nain@inria.fr).              in which the drift parameter of the underlying continuous-

[p.2]

                                                                                                                                     2



time stochastic process approaches its pre-change value as          t = 0 whereas the operator E∞ is associated with the situation
γ → ∞. Our analysis leverages classical exact results for           where no change occurs.
continuous-time CuSum [7], extending their applicability to           In this work we consider the following optimization problem,
the asymptotic regime characterized by diminishing statistical      due to Lorden [6], to find the best stopping time T in T :
differences between pre- and post-change processes. We derive
                                                                                   inf J(T )      subject to E∞ [T ] ≥ γ,          (2)
expressions for ADD under various regimes, determined by the                      T ∈T
rate at which the post-change drift vanishes with increasing γ.     with γ > 0, where
Our results demonstrate that the classical formulas for the ADD
of CuSum, which assume a fixed drift, no longer hold in this                  J(T ) = sup ess sup Et [max{0, T − t} | Ft ]         (3)
                                                                                         t≥0
asymptotic regime and must be carefully revised to reflect the
vanishing signal structure introduced by a covert adversary.        characterizes the worst-case expected delay. In (3) ess sup stands
   We characterize precise conditions under which an adversary      for essential supremum. The constraint in (2) expresses the fact
can maintain covertness and derive the corresponding scaling        that the false alarm rate should not exceed 1/γ. Denote by
laws. Within the Brownian motion framework, adversarial be-         n(γ) = inf T ∈F :E∞ [T ]≥γ d(T ), the optimal worst-case average
havior manifests through changes in the drift parameter. We         detection delay.
analyze how the scaling of this drift—relative to the run-length       It is known [8, Section 6.4.1] that the stopping time Th :=
constraint—affects the ability to remain covert. We further         inf{s ≥ 0 : Ys ≥ h} with Ys := Us − Ms where Us :=
quantify the adversarial damage, defined as the product of the      µZs − 12 µ2 s and Ms := inf 0≤r≤s Ur , with h selected so that
drift magnitude and the average detection delay, and determine      E∞ [Th ] = γ, solves (2). It is also known that for any T ∈
the regimes in which this damage is maximized while preserving      T , the worst-case detection delay occurs when t = 0, namely,
covertness.                                                         J(T ) = E0 [T ], which in turn implies from the optimality of Th
   The remainder of the paper is structured as follows. In the      that
next section, we briefly review the continuous-time CuSum                                    n(γ) = E0 [Th ].                      (4)
procedure and Lorden’s minimax detection framework. Section         In addition [8, Prop. 6.8, p. 146],
III develops our primary theoretical results. We then provide
numerical evaluations that substantiate our theoretical results.                                    2 h
                                                                                     E∞ [Th ] =       (e − h − 1),                 (5)
Finally, we conclude with a summary and discuss future direc-                                      µ2
tions.                                                                                              2
                                                                                         E0 [Th ] = 2 (e−h + h − 1).               (6)
                                                                                                   µ
     II. R EVIEW OF QUICKEST CHANGE DETECTION IN                    In [7] Moustakides generalized the model in (1) to the case
                   CONTINUOUS - TIME                                when µ depends on s and proposed a generalized version of
                                                                    Lorden’s minimax criterion to find the optimal detection delay.
   The material presented in this section can be found in [8,         In the following, we will investigate the model in (1) when
Section 6.4]. See also [2], [6], [7], [9]. In the continuous-       µ depends on γ and limγ µ(γ) = 0.
time setting, the stochastic process {Zs , s ≥ 0} is continuously
observed with the following dynamics                                             III. C ONDITIONS FOR COVERTNESS
                       �
                           dWs ,          s ≤ t,                       In this section, we conduct an asymptotic analysis of the
                dZs =                                         (1)
                           µds + dWs , s > t,                       model in (1) as γ → ∞, for the case where the drift µ depends
                                                                    on γ, denoted by µ(γ). We assume that µ(γ) > 0 for all γ > 0
where {Ws , s ≥ 0} is a standard Brownian motion. The drift
                                                                    and limγ→∞ µ(γ) = 0.
parameter µ is known and (without loss of generality) positive.
                                                                       Notice that n(γ) = Θ(γ) can be interpreted as a covertness
Denote by Fs = σ(Zu , 0 ≤ u ≤ s) the smallest σ-field with
                                                                    condition since it says that n(γ) is of the same order of
respect to which process {Zu , 0 ≤ u ≤ s} is measurable. In
                                                                    magnitude as the largest admissible lower bound on the expected
(1), t is the (unknown) time when the change occurs. In words,
                                                                    time between false alarms, given by γ. With this in mind,
before the change point the process {Zs , s ≥ 0} is a Brownian
                                                                    we address the following questions: (1) is it possible to have
motion and after the change point it is a particular instance of
                                                                    n(γ) = Θ(γ) and, if yes, (2) under what conditions?
an Ito process. No prior distribution on the change point t is
                                                                       Our analysis will use the Lambert function. Recall that the
assumed (non-Bayesian setting).
                                                                    Lambert function is the solution of the equation W (z)eW (z) = z
   The goal of quickest change detection is to minimize the         [4]. When z is real, W (z)eW (z) = z has a solution if and only
delay between when a change occurs and when it is detected,         if z ≥ −e−1 . When z ≥ 0, this solution is unique, given by
while maintaining a low false alarm rate. More specifically, a      the main branch W0 of W , and when −e−1 ≤ z < 0 there are
change detection algorithm is a stopping time T with respect        two solutions given by the branches W0 and W−1 of W . In
to the filtration {Fs , s ≥ 0}, that is {T ≤ s} ∈ Fs for all        particular,
s ∈ [0, ∞). If T ≥ t a delayed detection is made otherwise a
false alarm has occurred.                                            W0 (z) > −1     and       W−1 (z) < −1 for − e−1 < z < 0, (7)
   We denote by T the set of all stopping times with respect to
                                                                    and W0 (−e−1 ) = W−1 (−e−1 ) = −1. Last [4, p. 350]
{Fs , s ≥ 0}. Throughout Et (t ≥ 0) is the expectation operator
associated with the model in (1); in particular, the operator E0     W−1 (z) ∼ log(−z) − log(− log(−z)) as z → 0 with z < 0.
is associated with the situation when a change occurs at time                                                             (8)

[p.3]

                                                                                                                                     3



  Proposition 3.1 (Asymptotic behavior of n(γ)): As γ → ∞,            Remark 3.1 (Asymptotic behavior of optimal threshold h):
           2               2
           µ(γ)2 log(γµ(γ)   ), if limγ→∞ γµ(γ)2 = ∞,               lim h(γ) =
             2    1
                    �                                                γ→∞
 n(γ) ∼        G 2 θ γ,          if limγ→∞ γµ(γ)2 := θ,
           θ                                                                                             if limγ→∞ γµ(γ)2 = ∞,
                                                                     
             γ,                  if limγ→∞ γµ(γ)2 = 0,                ∞,
                                                                                               1
                                                        (9)             −1 − 12 θ − W−1 (−e−1− 2 θ ),     if limγ→∞ γµ(γ)2 = θ,
                                                                        1,                                if limγ→∞ γµ(γ)2 = 0.
                                                                     
with θ ∈ (0, ∞), where

G(x) = e1+x+W−1 (−e
                       −1−x
                              )
                                  − W−1 (−e−1−x ) − x − 2,
                                                        x≥0         The result when limγ→∞ γµ(γ)2 = ∞ follows by applying
                                                          (10)      the expansion in (8) to h(γ) in (11), while the result when
  The proof of Proposition 3.1 is based on Lemma 3.1 stated         limγ→∞ γµ(γ)2 = 0 follows from (11) and W−1 (−e−1 ) = −1.
below, whose proof is given in the appendix.                            Remark 3.2: If limγ→∞ µ(γ) = µ0 ̸= 0 then n(γ) ∼
                                                                      2
  Lemma 3.1 (Optimal threshold):                                    µ) log γ by Proposition 3.1. In particular, this shows that
                                                                        2

  For every γ > 0, the equation E∞ [Th ] = γ has a unique           n(γ) = Θ(log(γ)) in continuous-time.
solution in [0, ∞), given by                                            Remark 3.3: It is worth noting that limθ→0 θ2 G( 12 θ)γ = γ,
                                                                    since we have shown in the proof of Proposition 3.1 that
                   1                �        1    2
                                                    �
                                                                    limx→0 G(x)     = 1, and that θ2 G( 12 θ) ∼ µ(γ)2            2
     h(γ) = −1 − γµ(γ)2 − W−1 −e−1− 2 γµ(γ) .             (11)                 x                                      2 log(γµ(γ) ) as
                   2                                                θ → ∞ by using (8) and the definition of G, thereby showing
  Proof of Proposition 3.1: From (4), (6), (10), and (11), we       that the r.h.s. of (9) is a continuous function of limγ→∞ γµ(γ)2
have                                                                whenever this limit exists.
                            2
                                G 12 γµ(γ)2 .
                                           �
                  n(γ) =      2
                                                          (12)
                         µ(γ)                                       A. Numerical results
 Assume
     �    first that lim           2
                       � γ→∞ γµ(γ) = ∞. From (8) we get               Let µ(γ) = γ −δ with δ ≥ 0. We find from Proposition 3.1
         −1− 21 γµ(γ)2
W−1 −e                   ∼ log(γµ(γ)2 ) as γ → ∞, yielding
                                                                               
                                                                                2(1 − 2δ) log(γ)γ 2δ , if 0 ≤ δ < 12 ,
G 21 γµ(γ)2 ∼ log(γµ(γ)2 ) as γ → ∞, and subsequently,                             2G( 21 )γ,            if δ = 12 ,
           �
                                                                        n(γ) ∼                                              (14)
                                                                                   γ,                    if δ > 12 ,
                                                                               
                        2
             n(γ) ∼         log(γµ(γ)2 ),      γ → ∞.
                      µ(γ)2                                         as γ → ∞, with 2G( 21 ) = 0.563... The mapping γ → n(γ)
                                                                    (defined in (4) and (6), with h given in (11)) is displayed in
If limγ→∞ γµ(γ)2 = θ ∈ (0, ∞), clearly from (12)
                                                                    Figure 1 for δ ∈ {0.75, 2, 5}. We also plot the identity mapping
                          2 1                                       γ → γ so that one can observe the speed at which n(γ)
                 n(γ) ∼    G( θ)γ,         γ → ∞.
                          θ 2                                       converges to γ, as predicted by Proposition 3.1. Not surpringly,
Assume now that limγ→∞ γµ(γ)2 = 0. Let us prove that                the closer δ is to 12 the longer it takes to converge to the
limx↓0 G(x) = 1, which will prove from (12) that n(γ) ∼ γ           asymptotic regime. To better quantity this visual observation,
as γ → ∞.
         x
                                                                    we have reported in Table I the metric M (γ) = 100 × | n(γ)−γ
                                                                                                                              n(γ) |
   Since G(0) = 0, lim x→0 G(x)  is the right hand derivative of    for δ ∈ {0.75, 2, 5} and for increasing values of γ. We observe
                              x
                        x>0                                         that n(γ) converges quickly to γ for δ = 2 while for δ = 5, n(γ)
G(x) at x = 0. For −e−1 < x < 0, W1 (x) has a derivative,
                                                                    matches γ when γ ≥ 5. Convergence is slow when δ = 0.75.
given by (Hint: differentiate W−1 (x)eW−1 (x) = x)
                                     W−1 (x)
                  W1′ (x) =                      .           (13)
                                  x(1 + W−1 (x))
Consequently, for x > 0, the derivative of G(x) is given by
                                �              −1−x
                                                         �
  G′ (x) =e−1−x W−1′
                     (−e−1−x ) e1+x+W−1 (−e         )
                                                      −1
                                  −1−x
          + e1+x+W−1 (−e    )
                              − 1,
                       −1−x
          �                          �
               W−1 (−e      )                       −1−x
         = −                   +   1   e1+x+W−1 (−e      )
             1 + W−1 (−e−1−x )                                      Fig. 1: The mapping γ → n(γ) when µ(γ) = γ −δ for
              W−1 (−e−1−x )                                         δ ∈ {0.75, 2} (dash-dotted lines), δ = 5 (dashed line), and
          +                   − 1,
            1 + W−1 (−e−1−x )                                       the identity mapping γ → γ (solid line).
                          −1−x
             e1+x+W−1 (−e    )
                               −1          1
         =                 −1−x
                                  =−               .
               1 + W−1 (−e      )    W−1 (−e−1−x )                       γ=            2      5     10   102    103    104    105
                                                                         δ = 0.75   63.7   49.4   41.9   22.2   12.2   6.78   3.79
Letting x → 0 with x > 0, we see that 1 = lim x→0 G′ (x) =
                                                      x>0                δ=2        24.9   6.05   2.12   0.07      0      0      0
lim x→0 G(x)
         x , which concludes the proof of Proposition 3.1.
                                                                         δ=5        2.97   0.04      0      0      0      0      0
    x>0
   According to our definition of covertness, given by n(γ) =
Θ(n), Proposition 3.1 shows that an adversary is covert if          TABLE I: The metric M (γ) for δ ∈ {0.75, 2, 5} and γ ∈
     √                                                              {2, 5, 10, 102 , · · · , 105 }.
µ(γ) γ converges to a finite limit as γ → ∞.

[p.4]

                                                                                                                                                      4



  Figure 2(a) shows how the optimal threshold h(γ), given                                                A PPENDIX
in (11), varies with δ over the interval [0, 1] for γ ∈                    Proof of Lemma 3.1: Let γ > 0. Notice that ξ(γ) :=
{103 , 105 , 108 , 1012 }. Similarly, Figure 2(b) illustrates the be-   1     2
                                                                        2 µ(γ) ̸= 0 since, by assumption, µ(γ) > 0 as γ > 0. This
havior of n(γ)/γ as a function of δ, for the same values of γ. We                                           h
                                                                        shows that h = 0 is not a solution of e − h − 1 = γξ(γ). Let
observe that a clear phase transition emerges as δ crosses 0.5,         us find a strictly positive solution h to the equation
                                       √
which corresponds to µ(γ) = 1/ γ. This observation aligns
with our theoretical findings.                                                                    eh − h − 1 = γξ(γ).                             (15)
                                                                        Eq. (15) rewrites
                                                                                              −(h + r)e−(h+r) = −e−r ,                            (16)
                                                                                                                  −1          −r
                                                                        with r := 1+γξ(γ) > 1. Since −e ≤ −e < 0, (16) has two
                                                                        solutions, h1 = −r − W0 (−e−r ) and h2 = −r − W−1 (−e−r ).
                                                                        From (7), h1 < −γξ(γ) < 0, thereby implying that the solution
                                                                        we are looking for can only be h = h2 , namely,
                                                                                       h = −1 − γξ(γ) − W−1 (−e−1−ξ(γ)γ ).                        (17)
                 (a)                            (b)                     It remains to check that h in (17) is strictly positive for γ > 0.
Fig. 2: Phase transition analysis. As δ increases, (a) h(γ)                This will be true if one shows that the mapping φ : x → x −
approaches zero and (b) the ratio n(γ)/γ increases from 0 to            W−1 (−ex ) is strictly positive for x < −1. We have φ(−1) = 0
1, with the transition occurring at δ = 0.5.                            since W−1 (−e−1 ) = −1. On the other hand, by (13),
                                                                                                                         1
                                                                          φ′ (x) = 1 + ex W−1
                                                                                           ′
                                                                                              (−ex ) =                              ,   ∀x < −1.
   Now, we define the adversarial damage as D(γ) = µ(γ)n(γ).                                                    1 + W−1 (−ex )
This quantity captures the cumulative impact an adversary can
                                                                        But W−1 (−ex ) < −1 for x < −1 from (7), which shows that
inflict before being detected. Following (14),
                                                                        φ′ (x) < 0 for x < −1. Therefore, x → φ(x) is decreasing in
                  2(1 − 2δ) log(γ)γ δ , if 0 ≤ δ < 21 ,
                 
                                                                        (−∞, −1) and since φ(−1) = 0, this proves that φ(x) > 0
        D(γ) ∼      2G( 1 )γ 1/2 ,        if δ = 12 ,                   for x < −1. Therefore, h in (17) is the unique strictly positive
                  1−δ2
                    γ    ,                if δ > 12 ,                   solution of the equation 21 µ(γ)2 (eh − h − 1) = γ when γ > 0.
as γ → ∞. From these expressions, D(γ) is asymptotically
                                                                                                       R EFERENCES
maximized by δ = 12 , resulting in a total damage of order
   √
Θ( γ). Figure 3 displays the mapping δ → log D(γ) for                    [1] B. A. Bash, D. Goeckel, and D. Towsley, “Limits of reliable communica-
γ ∈ {106 , 108 , 1010 , 1012 }. The maximum damage occurs for                tion with low probability of detection on AWGN channels,” IEEE Journal
                                                                             on Selected Areas in Communications, Vol. 31, No. 9, pp. 1921–1930,
δ ≤ 12 ; moreover, as γ increases, the maximizer converges to                2013.
δ = 12 .                                                                 [2] M. Beibel, “A note on Rytov’s Bayes approach to the minimax property
                                                                             of the CUSUM procedure,” Annals of Statistics, Vol. 24, No. 2, pp. 1804-
                                                                             1812, 1996.
                                                                         [3] M.-C. Chang and M. R. Bloch, “Covert sequential hypothesis testing,” in
                                                                             Proc. 2021 IEEE Information Theory Workshop (ITW), Kanazawa, Japan,
                                                                             pp. 1–6, 2021.
                                                                         [4] R. M. Corless, G. H. Gonnet, D. E. G. Hare, D. J. Jeffrey, and D. E. Knuth,
                                                                             “On the Lambert W function,” Advances in Computational Mathematics,
                                                                             Vol. 5, pp. 329–359, 1996.
                                                                         [5] K.-W. Huang, H.-M. Wang, and H. V. Poor, “On covert communication
                                                                             against sequential change-point detection,” IEEE Transactions on Infor-
                                                                             mation Theory, Vol. 67, No. 11, pp. 7285–7303, 2021.
                                                                         [6] G. Lorden, “Procedure for reacting to a change in distribution,” The Annals
                                                                             of Mathematical Statistics, Vol. 42, No. 6, pp. 1897-1908, 1971.
                 Fig. 3: Total damage analysis.                          [7] G. V. Moustakides, ”Optimal stopping times for detecting changes in
                                                                             distributions,” Annals of Statistics, Vol. 14, No. 4, pp. 1379-1387, 1986.
                                                                         [8] H. V. Poor and O. Hadjiliadis, Quickest Detection. Cambridge University
                        IV. C ONCLUSION                                      Press, 2009.
                                                                         [9] A. N. Shiryaev, ”Minimax optimality of the method of cumulative sums
   We introduced and analyzed a sequential detection problem                 (CUSUM) in the continuous case,” Russian Mathematical Surveys, Vol.
when a covert adversary is present in a continuous-time setting              51, No. 4, pp. 750-751, 1996.
                                                                        [10] D. Siegmund, Sequential Analysis, Tests and Confidence Intervals.
where the post-change drift diminishes with the false alarm                  Springer Verlag, 1985.
constraint parameter γ. By leveraging classical performance             [11] A. Tartakovsky, I. Nikiforov, and M. Basseville, Sequential Analysis,
characterizations of the CuSum procedure, we rigorously es-                  Hypothesis Testing and Change Point Detection. Chapman & Hall/CRC
                                                                             Press, Monographs on Statistics & Applied Probability, Vol. 136, 2014.
tablished asymptotic expressions for the detection delay under          [12] A. Ramtin, Z. Hare, L. Kaplan, P. Nain, V. Veeravalli, and D. Towsley,
vanishing drift. Our results identify the critical scaling regimes           ”Quickest change detection in the presence of covert adversaries,” in Proc.
that govern covertness and show that adversarial damage is                   MILCOM 2024 - IEEE Military Communications Conference (MILCOM),
                                            √                                pp. 1–6, 2024.
maximized when the drift decays as Θ(1/ γ). Numerical sim-              [13] L. Xie, S. Zou, Y. Xie, and V. V. Veeravalli, ”Sequential (quickest) change
ulations were included to illustrate and support the theoretical             detection: Classical results and new directions,” IEEE Journal on Selected
findings.                                                                    Areas in Information Theory, vol. 2, no. 2, pp. 494–514, 2021.


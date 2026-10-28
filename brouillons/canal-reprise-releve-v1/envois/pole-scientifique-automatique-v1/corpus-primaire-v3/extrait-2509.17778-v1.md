# EXTRAIT — Quickest Change Detection in Continuous-Time in Presence of a Covert Adversary

- Auteurs : Amir Reza Ramtin, Philippe Nain, Don Towsley ; année : 2025 (v1 du 22 septembre 2025) ; identifiant : arXiv:2509.17778v1 (4 pages)
- Statut : préimpression arXiv cs.IT ; Université du Massachusetts à Amherst et Inria ; article de théorie de la détection de rupture en temps continu (mouvement brownien, procédure CUSUM), hors du champ de la sécurité des modèles de langage. C'est la version en temps continu de l'article en temps discret arXiv:2601.20022, déjà extrait dans `../corpus-primaire-v1/extrait-2601.20022-v1.md`.
- PDF source : `docs/sources/pdf/2509.17778v1.pdf` ; SHA-256 du PDF : `97d000252b768e69113437cce1a88a24488cbe3f92a1a724ea39c0c9f87d8d5e` (compagnon `.sha256` fourni avec le PDF, vérifié par `sha256sum -c`)
- Pages gardées en tout ou en partie : 1-4 (le PDF entier, sauf les passages nommés ci-dessous)
- Nature : texte du PDF repris mot pour mot (`pdftotext -raw`, une colonne à la fois, lignes rejointes ; les sauts de paragraphe sont replacés aux débuts de paragraphes lus sur la page), numéro de page du PDF en `[p.N]` au début de chaque passage ; coupes marquées `[COUPÉ]`. Les formules (équations (1) à (14), proposition 3.1, lemme 3.1, remarques) sont extraites en texte linéaire, dans un ordre et avec des indices parfois altérés (exemple : « µ)2 » pour le carré de µ0 dans la remarque 3.2) : se reporter à la page citée pour tout symbole. Aucun chiffre retapé à la main (R7). Les notes entre crochets sont de la main de l'instance.
- Retiré pour sûreté (niveau méthode seulement) : rien (article théorique : aucune recette d'attaque ; l'« adversaire » est un paramètre de dérive d'un processus de Wiener). Retiré par économie de place : démonstration de la proposition 3.1, annexe (démonstration du lemme 3.1), note de financement, bibliographie sauf la référence [12].

---

[p.1]

Abstract—We investigate the problem of covert quickest change detection in a continuous-time setting, where a Brownian motion experiences a drift change at an unknown time. Unlike classical formulations, we consider a covert adversary who adjusts the post-change drift µ = µ(γ) as a function of the false alarm constraint parameter γ, with the goal of remaining undetected for as long as possible. Leveraging the exact expressions for the average detection delay (ADD) and average time to false alarm (AT2FA) known for the continuous-time CuSum procedure, we rigorously analyze how the asymptotic behavior of ADD evolves as µ(γ) → 0 with increasing γ. Our results reveal that classical detection delay characterizations no longer hold in this regime. We derive sharp asymptotic expressions for the ADD under various convergence rates of µ(γ), identify precise conditions for maintaining covertness, and characterize the total damage inflicted by the adversary. We show that the adversary achieves maximal damage when the drift scales as µ(γ) = Θ(1/ √ γ), marking a fundamental trade-off between stealth and impact in continuous-time detection systems.

I. INTRODUCTION Quickest change detection (QCD) has long been a fundamental statistical technique for rapidly identifying changes in the underlying statistical properties of observed processes, with numerous critical applications ranging from quality control and finance to security and environmental monitoring [8], [9], [11]. Traditionally formulated in discrete-time settings, QCD methods have also been extensively developed and analyzed within continuous-time frameworks, where processes are monitored continuously rather than at discrete intervals. Continuous-time detection is particularly advantageous in settings requiring immediate responses to subtle or rapid shifts, as it allows for instantaneous detection of changes, thereby reducing reaction times and potential damages [2], [8], [9]. A classical and widely used method in continuous-time QCD is the continuous-time Cumulative Sum (CuSum) procedure, initially studied by Lorden [6] and subsequently generalized by Moustakides [7]. The continuous-time CuSum is known for its optimality under Lorden’s minimax criterion, which aims to minimize the worst-case expected detection delay while controlling the average time between false alarms. Under this criterion, the CuSum procedure continuously accumulates evidence (in the form of log-likelihood ratios) and signals a change once this cumulative evidence crosses a predetermined threshold [7], [8]. Precise characterizations of performance metrics, such as average time to false alarm (AT2FA) and average detection delay (ADD), are available in closed form for standard continuous-time models [7].

An important application of QCD is detecting the presence of an adversary [13]. However, classical analyses typically assume that the adversary is unaware of the detection mechanism. In adversarial environments, these assumptions may no longer hold. Specifically, an adversary, aware of the detection mechanism, may strategically adapt their behavior in response to detection thresholds. In this scenario, the adversary’s statistical signature post-change increasingly resembles the pre-change condition as the false-alarm constraint (quantified by a parameter γ) becomes increasingly stringent. Such adaptive adversarial behavior challenges traditional assumptions and necessitates a deeper theoretical analysis of covert adversaries operating in a continuous-time setting.

The notion of covertness, first introduced by Bash et al. in the context of covert communication [1], captures the ability of a transmitter to remain undetectable by an observing warden during communication. Most existing work assumes that the detector knows the exact start time of any potential transmission. In contrast, we relax this assumption and extend the notion of covertness to a sequential detection framework, where adversaries deliberately behave in a way that keeps their activity concealed over extended periods. From the perspective of sequential detection, this gives rise to a fundamentally different adversarial strategy. Unlike traditional adversaries whose actions lead to detectable statistical deviations—enabling timely detection— covert adversaries aim to remain hidden by ensuring that ADD scales with the same order as AT2FA, thereby rendering the detector ineffective [5].

While prior work has studied covertness in discrete-time sequential detection [3], [5], [12], the continuous-time counterpart of this problem remains relatively unexplored. The works in [3], [5] have been largely confined to covert wireless communication scenarios, with assumptions tailored to that domain—such as specific channel models or power constraints—and have primarily focused on communication-centric performance metrics. In contrast, [12] considers an adversarial setting against the CuSum procedure under non-stationarity and without assuming that the AT2FA constraint is known to the adversary.

In this paper, we rigorously investigate covert adversaries in a continuous-time CuSum framework, where the post-change drift parameter is allowed to depend explicitly on the false-alarm constraint parameter γ. Specifically, we examine scenarios in which the drift parameter of the underlying continuous-

[COUPÉ : note de financement et adresses des auteurs, bas de la colonne de gauche]

[p.2]

[suite de la phrase commencée au bas de la p.1] time stochastic process approaches its pre-change value as γ → ∞. Our analysis leverages classical exact results for continuous-time CuSum [7], extending their applicability to the asymptotic regime characterized by diminishing statistical differences between pre- and post-change processes. We derive expressions for ADD under various regimes, determined by the rate at which the post-change drift vanishes with increasing γ. Our results demonstrate that the classical formulas for the ADD of CuSum, which assume a fixed drift, no longer hold in this asymptotic regime and must be carefully revised to reflect the vanishing signal structure introduced by a covert adversary.

We characterize precise conditions under which an adversary can maintain covertness and derive the corresponding scaling laws. Within the Brownian motion framework, adversarial behavior manifests through changes in the drift parameter. We analyze how the scaling of this drift—relative to the run-length constraint—affects the ability to remain covert. We further quantify the adversarial damage, defined as the product of the drift magnitude and the average detection delay, and determine the regimes in which this damage is maximized while preserving covertness.

The remainder of the paper is structured as follows. In the next section, we briefly review the continuous-time CuSum procedure and Lorden’s minimax detection framework. Section III develops our primary theoretical results. We then provide numerical evaluations that substantiate our theoretical results. Finally, we conclude with a summary and discuss future directions.

II. REVIEW OF QUICKEST CHANGE DETECTION IN CONTINUOUS-TIME The material presented in this section can be found in [8, Section 6.4]. See also [2], [6], [7], [9]. In the continuous-time setting, the stochastic process {Zs, s ≥ 0} is continuously observed with the following dynamics dZs =  dWs, s ≤ t, µds + dWs, s > t, (1) where {Ws, s ≥ 0} is a standard Brownian motion. The drift parameter µ is known and (without loss of generality) positive. Denote by Fs = σ(Zu, 0 ≤ u ≤ s) the smallest σ-field with respect to which process {Zu, 0 ≤ u ≤ s} is measurable. In (1), t is the (unknown) time when the change occurs. In words, before the change point the process {Zs, s ≥ 0} is a Brownian motion and after the change point it is a particular instance of an Ito process. No prior distribution on the change point t is assumed (non-Bayesian setting).

The goal of quickest change detection is to minimize the delay between when a change occurs and when it is detected, while maintaining a low false alarm rate. More specifically, a change detection algorithm is a stopping time T with respect to the filtration {Fs, s ≥ 0}, that is {T ≤ s} ∈ Fs for all s ∈ [0, ∞). If T ≥ t a delayed detection is made otherwise a false alarm has occurred.

We denote by T the set of all stopping times with respect to {Fs, s ≥ 0}. Throughout Et (t ≥ 0) is the expectation operator associated with the model in (1); in particular, the operator E0 is associated with the situation when a change occurs at time t = 0 whereas the operator E∞ is associated with the situation where no change occurs.

In this work we consider the following optimization problem, due to Lorden [6], to find the best stopping time T in T : inf T ∈T J(T) subject to E∞[T] ≥ γ, (2)

with γ > 0, where J(T) = sup t≥0 ess sup Et[max{0, T − t} | Ft] (3) characterizes the worst-case expected delay. In (3) ess sup stands for essential supremum. The constraint in (2) expresses the fact that the false alarm rate should not exceed 1/γ. Denote by n(γ) = infT ∈F:E∞[T ]≥γ d(T), the optimal worst-case average detection delay.

It is known [8, Section 6.4.1] that the stopping time Th := inf{s ≥ 0 : Ys ≥ h} with Ys := Us − Ms where Us := µZs − 1 2 µ2 s and Ms := inf0≤r≤s Ur, with h selected so that E∞[Th] = γ, solves (2). It is also known that for any T ∈ T , the worst-case detection delay occurs when t = 0, namely, J(T) = E0[T], which in turn implies from the optimality of Th that n(γ) = E0[Th]. (4) In addition [8, Prop. 6.8, p. 146], E∞[Th] = 2 µ2 (eh − h − 1), (5) E0[Th] = 2 µ2 (e−h + h − 1). (6)

In [7] Moustakides generalized the model in (1) to the case when µ depends on s and proposed a generalized version of Lorden’s minimax criterion to find the optimal detection delay. In the following, we will investigate the model in (1) when µ depends on γ and limγ µ(γ) = 0.

III. CONDITIONS FOR COVERTNESS In this section, we conduct an asymptotic analysis of the model in (1) as γ → ∞, for the case where the drift µ depends on γ, denoted by µ(γ). We assume that µ(γ) > 0 for all γ > 0 and limγ→∞ µ(γ) = 0.

Notice that n(γ) = Θ(γ) can be interpreted as a covertness condition since it says that n(γ) is of the same order of magnitude as the largest admissible lower bound on the expected time between false alarms, given by γ. With this in mind, we address the following questions: (1) is it possible to have n(γ) = Θ(γ) and, if yes, (2) under what conditions?

Our analysis will use the Lambert function. Recall that the Lambert function is the solution of the equation W(z)eW (z) = z [4]. When z is real, W(z)eW (z) = z has a solution if and only if z ≥ −e−1 . When z ≥ 0, this solution is unique, given by the main branch W0 of W, and when −e−1 ≤ z < 0 there are two solutions given by the branches W0 and W−1 of W. In particular, W0(z) > −1 and W−1(z) < −1 for − e−1 < z < 0, (7) and W0(−e−1 ) = W−1(−e−1 ) = −1. Last [4, p. 350] W−1(z) ∼ log(−z) − log(− log(−z)) as z → 0 with z < 0. (8)

[p.3]

Proposition 3.1 (Asymptotic behavior of n(γ)): As γ → ∞, n(γ) ∼    2 µ(γ)2 log(γµ(γ)2 ), if limγ→∞ γµ(γ)2 = ∞, 2 θ G 1 2 θ  γ, if limγ→∞ γµ(γ)2 := θ, γ, if limγ→∞ γµ(γ)2 = 0, (9) with θ ∈ (0, ∞), where G(x) = e1+x+W−1(−e−1−x ) − W−1(−e−1−x ) − x − 2, x ≥ 0 (10) The proof of Proposition 3.1 is based on Lemma 3.1 stated below, whose proof is given in the appendix.

Lemma 3.1 (Optimal threshold): For every γ > 0, the equation E∞[Th] = γ has a unique solution in [0, ∞), given by h(γ) = −1 − 1 2 γµ(γ)2 − W−1  −e−1− 1 2 γµ(γ)2  . (11)

[COUPÉ : démonstration de la proposition 3.1 (p.3, colonne de gauche), formules illisibles en texte linéaire]

According to our definition of covertness, given by n(γ) = Θ(n), Proposition 3.1 shows that an adversary is covert if µ(γ) √ γ converges to a finite limit as γ → ∞.

Remark 3.1 (Asymptotic behavior of optimal threshold h): lim γ→∞ h(γ) =    ∞, if limγ→∞ γµ(γ)2 = ∞, −1 − 1 2 θ − W−1(−e−1− 1 2 θ ), if limγ→∞ γµ(γ)2 = θ, 1, if limγ→∞ γµ(γ)2 = 0. The result when limγ→∞ γµ(γ)2 = ∞ follows by applying the expansion in (8) to h(γ) in (11), while the result when limγ→∞ γµ(γ)2 = 0 follows from (11) and W−1(−e−1 ) = −1.

Remark 3.2: If limγ→∞ µ(γ) = µ0 ̸= 0 then n(γ) ∼ 2 µ)2 log γ by Proposition 3.1. In particular, this shows that n(γ) = Θ(log(γ)) in continuous-time.

Remark 3.3: It is worth noting that limθ→0 2 θ G(1 2 θ)γ = γ, since we have shown in the proof of Proposition 3.1 that limx→0 G(x) x = 1, and that 2 θ G(1 2 θ) ∼ 2 µ(γ)2 log(γµ(γ)2 ) as θ → ∞ by using (8) and the definition of G, thereby showing that the r.h.s. of (9) is a continuous function of limγ→∞ γµ(γ)2 whenever this limit exists.

A. Numerical results Let µ(γ) = γ−δ with δ ≥ 0. We find from Proposition 3.1 n(γ) ∼    2(1 − 2δ) log(γ)γ2δ , if 0 ≤ δ < 1 2 , 2G(1 2 )γ, if δ = 1 2 , γ, if δ > 1 2 , (14) as γ → ∞, with 2G(1 2 ) = 0.563... The mapping γ → n(γ) (defined in (4) and (6), with h given in (11)) is displayed in Figure 1 for δ ∈ {0.75, 2, 5}. We also plot the identity mapping γ → γ so that one can observe the speed at which n(γ) converges to γ, as predicted by Proposition 3.1. Not surpringly, the closer δ is to 1 2 the longer it takes to converge to the asymptotic regime. To better quantity this visual observation, we have reported in Table I the metric M(γ) = 100 × |n(γ)−γ n(γ) | for δ ∈ {0.75, 2, 5} and for increasing values of γ. We observe that n(γ) converges quickly to γ for δ = 2 while for δ = 5, n(γ) matches γ when γ ≥ 5. Convergence is slow when δ = 0.75.

Fig. 1: The mapping γ → n(γ) when µ(γ) = γ−δ for δ ∈ {0.75, 2} (dash-dotted lines), δ = 5 (dashed line), and the identity mapping γ → γ (solid line).

γ = 2 5 10 102 103 104 105 δ = 0.75 63.7 49.4 41.9 22.2 12.2 6.78 3.79 δ = 2 24.9 6.05 2.12 0.07 0 0 0 δ = 5 2.97 0.04 0 0 0 0 0

TABLE I: The metric M(γ) for δ ∈ {0.75, 2, 5} and γ ∈ {2, 5, 10, 102 , · · · , 105 }.

[p.4]

Figure 2(a) shows how the optimal threshold h(γ), given in (11), varies with δ over the interval [0, 1] for γ ∈ {103 , 105 , 108 , 1012 }. Similarly, Figure 2(b) illustrates the behavior of n(γ)/γ as a function of δ, for the same values of γ. We observe that a clear phase transition emerges as δ crosses 0.5, which corresponds to µ(γ) = 1/ √ γ. This observation aligns with our theoretical findings.

(a) (b)

Fig. 2: Phase transition analysis. As δ increases, (a) h(γ) approaches zero and (b) the ratio n(γ)/γ increases from 0 to 1, with the transition occurring at δ = 0.5.

Now, we define the adversarial damage as D(γ) = µ(γ)n(γ). This quantity captures the cumulative impact an adversary can inflict before being detected. Following (14), D(γ) ∼    2(1 − 2δ) log(γ)γδ , if 0 ≤ δ < 1 2 , 2G(1 2 )γ1/2 , if δ = 1 2 , γ1−δ , if δ > 1 2 , as γ → ∞. From these expressions, D(γ) is asymptotically maximized by δ = 1 2 , resulting in a total damage of order Θ( √ γ). Figure 3 displays the mapping δ → log D(γ) for γ ∈ {106 , 108 , 1010 , 1012 }. The maximum damage occurs for δ ≤ 1 2 ; moreover, as γ increases, the maximizer converges to δ = 1 2 .

Fig. 3: Total damage analysis.

IV. CONCLUSION We introduced and analyzed a sequential detection problem when a covert adversary is present in a continuous-time setting where the post-change drift diminishes with the false alarm constraint parameter γ. By leveraging classical performance characterizations of the CuSum procedure, we rigorously established asymptotic expressions for the detection delay under vanishing drift. Our results identify the critical scaling regimes that govern covertness and show that adversarial damage is maximized when the drift decays as Θ(1/ √ γ). Numerical simulations were included to illustrate and support the theoretical findings.

[COUPÉ : annexe (démonstration du lemme 3.1), références [1] à [11] et [13]]

[12] A. Ramtin, Z. Hare, L. Kaplan, P. Nain, V. Veeravalli, and D. Towsley, ”Quickest change detection in the presence of covert adversaries,” in Proc. MILCOM 2024 - IEEE Military Communications Conference (MILCOM), pp. 1–6, 2024.

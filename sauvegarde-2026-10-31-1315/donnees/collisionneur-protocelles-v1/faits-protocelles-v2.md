# Faits — papier « Protection of an RNA replicase by protocells has a ceiling and a price » (L. Ciric, v0.19.4, version complète, non publié)

Texte intégral extrait par pdftotext du PDF `docs/sources/pdf/Ciric-protocells-fecundity-complete-v0.19.4.pdf` (sha256 ba59c2541a31a94f15ee943ec15353609b6d3d0a61748b0d80655d294167cc61), 105 pages. Les nombres isolés sont les numéros de ligne du manuscrit ; chaque page commence par un marqueur « [page N] ». Les formules sont extraites telles quelles et peuvent être abîmées : en cas de doute, citer la page et la ligne et le dire. Document confidentiel, non publié : ne pas le reproduire hors de la réponse.


[page 1]
Protection of an RNA replicase by protocells has a ceiling and a
price
Lazar Ciric
[affiliation, to be completed by the author]; e-mail: [address, to be completed by the author]
Complete version, 31 October 2026 (content of v0.19.4)

Abstract
Life may have begun with an RNA able to copy RNA, including copies of itself 1,2 . Because such a
replicase copies only other molecules, its errors create parasites that are copied but do not copy, against
which a better catalyst gains nothing 3–5 . Compartments are the accepted escape 6–8 , but their maximal
protection remains unknown. Here we compute the replicase’s exact error threshold 9 in protocells that
grow and divide by random partition, and show that, for a sterile lone replicase, this protection has a
ceiling and a price: protocells can at most halve the fraction of correct copies a replicase must make, and
help only a sufficiently fecund one. Without decay, large protocells approach the ceiling when parasites
are no better templates than the replicase. With decay, the copies a replicase must complete per lifetime
grow, as computed, in proportion to protocell size; unfinished copies add a cost set by their fate. The only
polymerase ribozyme that has copied its own sequence 10 falls about tenfold or more short of replacing
itself. Fecundity and the fate of unfinished copies, not fidelity alone, decide whether compartments could
rescue an RNA replicase. Experiments should report complete copies per template lifetime and what
becomes of unfinished ones.

1

Introduction

A replicator that copies itself with per-copy fidelity q keeps its information only if q exceeds the inverse of
its selective superiority s over its mutants 9 : − ln q < ln s. In real ribozymes many mutations are neutral and
the functional sequence is much fitter than its mutants; with measured values the threshold is “relaxed”, and
replication accuracies within reach of existing polymerase ribozymes appeared sufficient 11–13 .
The argument assumes that superiority acts on the template. The first replicase, however, had to copy
other molecules, including other copies of itself: it acted in trans. A copying error then produces a molecule
that is still copied but no longer copies. In a well-mixed pool such a parasite benefits from the replicase
exactly as much as the replicase itself, whatever its catalytic efficiency, so that selection sees only template
quality 2–4 : catalytic superiority, the lever of the relaxed threshold, is inert. Tupper and Higgs 5 made this
point and judged the conclusions of ref. 12 “somewhat optimistic”, without quantifying the difference; as
Kun 14 put it, “a higher level evolutionary unit is required”.
The candidate unit is a compartment. In the stochastic corrector, molecules replicate inside protocells
that grow and divide, and random partition creates variation on which selection between protocells acts 6,7 .
Protocells were shown numerically to maintain function against parasites at error rates that are lethal in bulk:

1


[page 2]
ceiling ln2

0.4
0.2
= 0.5
=1
= 1.5

0.2
101

102

U = 0.6
U = 0.5

103

0.6

0.0

B The price

103

protocell size at birth, n

U = 0.3

102
101
100
10 1
10 2
10 3

QT45
scaling law
exact kernel

101

102

104
fecundity R (copies per lifetime)

0.8

104
fecundity needed, Rmin

gain over a well-mixed pool, U

A The ceiling

103

protocell size at birth, n

C The gap
ln 2

103

n = 10
n = 50
R = eU/(2 eU)

102
U

101

R=e

100

TPR fragment
52-2

10 1
10 2
10 3

24-3
tC19Z

0

QT45

1
2
3
error load per copy, U

Fig. 1 | Protection by protocells has a ceiling and a price. (A) Gain in tolerable load over a well-mixed pool,
∆U = Uc − max(0, ln(1/θ)), at infinite fecundity, against protocell size at birth n, for parasite template efficiencies
θ = 0.5, 1 and 1.5 (exact thresholds; at n = 2 and θ = 0.5 the gain is −0.20). If a lone replicase cannot be copied,
no protocell adds more than ln 2 (dashed), at any size and fecundity, under any division blind to which molecules are
replicases (Theorem 2; Appendix S2). (B) Fecundity R (complete copies per lifetime) needed for a load U = 0.3, 0.5
or 0.6 at θ = 1: scaling law Rmin = n/ψ−1 (U) (lines; fitted ψ) and exact thresholds (points; within 5% of the law at
n = 200). The limit is proved for R > n (Theorem 4; U = 0.5 and 0.6); for U = 0.3 (R < n) it rests on hypothesis
(H2) (Appendix S3), and reading Rmin from it uses the computed decrease of ψ (Methods). No replicase is maintained
at or below R = 1 (grey line). Band: estimated fecundity of QT45. (C) Viability boundaries U = Uc (n, R) at θ = 1
for n = 10 (solid; viable region shaded) and n = 50 (dashed); dashed vertical line, the ceiling ln 2; grey lines, two
fecundities proved necessary at every size, R = eU and R = eU /(2 − eU ) (Appendix S3). Measured ribozymes sit at
the load their error rates give a 53-bit replicase (0.56 lethal substitutions per bit; U = ln 2 at a per-nucleotide fidelity
of 0.977): bars, estimated fecundities; upward arrow, a lower bound (TPR fragment, at the fidelity of its ancestor);
horizontal arrow, lowest published fidelity of 52-2 (U = 4.7); triangle, tC19Z, whose fecundity is unknown. Sources:
Table 2.

in package models 6 , in trans-acting replicase models for protocells of up to ten molecules, with an optimum
size when they divide in two 15 , and in a complementary-strand model 16 . Transient compartmentalization
with pooling protects functional RNAs against parasites without division 8,17,18 . In package models of several
template types, the information a protocell can keep tends to a constant set by the error rate 19 . For a replicase
that copies in trans, how much relaxation compartments can give at most at every size, and what limits it, has
not been computed. The answer sets the fidelity target for experiments.
Here we answer this question for the simplest model that contains the trans problem, a trans-acting replicase 15 whose errors make parasites of arbitrary template efficiency θ. We prove that the compartment adds
at most ln 2 to the tolerable error load at every protocell size and fecundity, whenever division ignores which
molecules are replicases, and, for binomial partition, exactly ln 2 in the large-protocell limit at infinite fecundity when θ ≤ 1, because catalyst–template pairs, not replicases, are the unit that reproduces (Figs. 1A and 2).
We prove that finite fecundity spends this bonus through the single ratio of protocell size to fecundity when
fecundity exceeds protocell size, and bracket the other case, which reduces to one property of a limit process,
partly proved (Figs. 1B and 4). Unfinished copies set a third requirement (Fig. 6), and make protocells and a
surface respond differently to the kinetics of the polymerase (Fig. 7). Measured polymerase ribozymes miss
the first two requirements (Fig. 1C). Proofs, numerical methods and further results are in the Methods and in
Appendices S1–S14.

2


[page 3]
A A replicase copies the others, in trans B Grow from n to 2n, then split at random C What reproduces is the pair
growth

catalyst (circled) template

replicases F, if self-copying were allowed

weight 1

×2q/
1 replicase:
lineage lost

weight
replicase
parasite
a replicase copy is correct with probability q = e U

division
per cycle
(both daughters)

n

2n

binomial partition of each species
fecundity R: copies per molecule lifetime

×1

2q/ > 1

ordered pairs F(F 1), trans copying

×22q/

×12

22q/

1

In trans a lone replicase is sterile: the unit that
reproduces is the pair, and a random split halves it.

Pairs persist iff 2q > : Uc ln(2/ )

Fig. 2 | The model and its mechanism. (A) A replicase (circled) copies another molecule of its protocell, never itself:
a replicase template with weight 1, a parasite with weight θ. A copy of a replicase is correct with probability q = e−U ;
errors make parasites. (B) A protocell grows from n to 2n molecules and splits at random (binomial partition); a
daughter with at most one replicase is a dead lineage. At finite fecundity, each replicase starts R copies per molecular
lifetime and molecules decay. (C) Over a cycle of growth and division, the expected number of replicases would
be multiplied by 2q/θ if a replicase could copy itself, and there would be no threshold. In trans a lone replicase is
sterile, and the unit that reproduces is the ordered catalyst–template pair, whose number grows as 22q/θ and is halved
by division. In the limit kernel, pairs persist if and only if 2q > θ, whence Uc → ln(2/θ) (Theorem 1).

2

A trans-acting replicase in protocells

A protocell contains F replicases and P parasites, N = F + P molecules (Fig. 2). Each replicase copies the
other molecules: it picks a template among the N − 1 molecules other than itself, a replicase with weight 1
and a parasite with weight θ. A copy of a replicase template is a functional replicase with probability q = e−U
and a parasite otherwise; a copy of a parasite is a parasite. The next molecule made in a protocell is therefore
a replicase with probability
p(F, N) =

q (F − 1)
.
(F − 1) + θ (N − F)

(1)

The protocell grows from n to 2n molecules and splits into two daughters, each molecule going to either
daughter independently (binomial partition). A protocell with F ≤ 1 is a dead lineage: a lone replicase
has no functional template in trans, and is never copied. The population of protocells is infinite; living
protocells form a multitype branching process, and the threshold Uc (n, θ) is the load beyond which the
spectral radius ρ of the mean matrix of living daughters no longer exceeds one (Methods). The model is
that of Bianconi et al. 15 without spontaneous replication, which would require a complete non-enzymatic
copy of the replicase (Methods). θ lumps everything that makes a parasite a better or worse template than a
replicase: shorter length, structure, and the competition for binding to the catalyst; θ > 1 is the realistic case
for a parasite shorter than its replicase (Discussion). Until finite fecundity is introduced, molecules do not
decay.

3

Results

3.1

At most a factor of two

Without compartments, a replicase whose errors make parasites of template weight θ persists only if its
correct copies are made faster than parasites are copied 3,20 , q > θ: Uc = max(0, ln(1/θ)). For θ ≥ 1 no error
3


[page 4]
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
0.0

proved: Uc(n) < ln(2/ ) at every n if

2.5

1

= 0.5: ln(2/ ) = 1.386

= 1: ln(2/ ) = 0.693
= 1.5: ln(2/ ) = 0.288
proved: Uc(n) ln(2/ ) O(n4 n) if 1

101
102
103
protocell size at birth, n (molecules)

B The protocell adds at most ln 2, catalysis nothing
protocell: ln(2/ )
complementary strands: ln(1.95/ )
equal partition: ln(1.44/ )
well mixed: max(0, ln(1/ ))

2.0
limit threshold Uc( )

error threshold Uc = lnqc

A The exact threshold approaches ln(2/ )

1.5
1.0
off scale: a replicator copied
in cis, with selective superiority
s = 351, has Uc = lns = 5.86

0.5
0.0

0.5
1.0
1.5
2.0
2.5
template efficiency of parasites,

Fig. 3 | The ceiling at infinite fecundity. (A) Exact threshold Uc (n) for θ = 0.5, 1 and 1.5 (independent kernel;
points), with the limits ln(2/θ) (dashed). For θ ≤ 1 the threshold stays below the limit at every size and converges to
it (Theorems 2 and 3); for θ > 1 small protocells do substantially better than large ones (at θ = 1.5, 0.557 at n = 3
against a limit of 0.288, Theorem 3), but never reach ln 2, the θ = 1 line (Theorem 2). (B) Limit threshold against the
template efficiency of parasites, for protocells with binomial partition (ln(2/θ), Theorem 3), complementary strands
(ln(1.9486/θ)), an equal partition of replicases (ln(1.44/θ)), and for the well-mixed pool (max(0, ln(1/θ))). Catalytic
efficiency enters none of them. A replicator copied in cis with the selective superiority s = 351 used by Kun et al. 11
would have Uc = 5.86, off scale.

at all is tolerated. In protocells we prove three results (Methods; Appendices S1–S2):
Theorem 1 (limit kernel). Let B∞ be the limit, as n → ∞ at fixed replicase number, of the kernel of living
daughters, for growth by a factor k and binomial partition into k daughters. For q < θ, its spectral radius is
ρ(B∞ ) = k2q/θ−1 , with the positive eigenfunction h(F) = F(F − 1), and the h-transformed chain is positive
recurrent. The threshold of B∞ is therefore q = θ/2, that is Uc = ln(2/θ), for every k; if θ ≥ 2, ρ(B∞ ) < 1 for
every q < 1 and Uc = 0.
Theorem 2 (bounds at every size). For binary division, infinite fecundity and every n ≥ 2, ρ < 1 for all
q ≤ min(θ, 1)/2. Hence Uc (n) < max(0, ln(1/θ)) + ln 2: at every size the protocell adds less than ln 2 to
the well-mixed threshold, that is, Uc (n) < ln(2/θ) if θ ≤ 1 and Uc (n) < ln 2 if θ ≥ 1. If θ ≥ 1, moreover,
Uc (n) ≥ ln(2/θ) − O(n4−n ). At θ = 1, ρ(q = 21 ) = 1 − 21−2n exactly.
Theorem 3 (the limit). For binary division and infinite fecundity, limn→∞ Uc (n) = max(0, ln(2/θ)) for every
θ.
The proofs rest on a fictitious clock in which replicase templates are copied at rate 1 and parasites at
rate θ, so that F − 1 is a Yule process of rate q whose dynamics do not involve the parasites, and on the pair
density ϕ = F(F − 1)/(N − 1), a supermartingale during growth when q ≤ min(θ, 1)/2 (Methods). For θ ≤ 1
the exact thresholds therefore converge to ln(2/θ), from below; an independently written kernel code extends
them to n = 800 for θ = 0.5 and n = 400 for θ = 1.5, where the extrapolation in 1/n meets ln(2/θ) to within
2 × 10−6 and 2 × 10−7 (Fig. 1A; Fig. 3A; Methods). For θ > 1 the pair density bounds the threshold only
by ln 2; the convergence also uses that ρ never decreases as q grows, at every size, and that protocells rich in
replicases drift back uniformly in n (Methods).

4


[page 5]
In the large-protocell limit, the protocell adds exactly ln 2 to the well-mixed threshold whenever θ ≤ 1,
only ln(2/θ) when 1 < θ < 2, and parasites that are at least twice as good templates as the replicase (θ ≥ 2)
cannot be resisted (Fig. 3B). Catalytic efficiency does not appear: speeding up the replicase speeds up its
parasites by the same factor.

3.2

Pairs, not replicases, reproduce

Why two? In the fictitious clock, the expected number of ordered pairs of replicases, F(F − 1) = ν(ν + 1)
with ν = F − 1, obeys E[ν(t)(ν(t) + 1)] = ν0 (ν0 + 1) e2qt : pairs multiply twice as fast as replicases. Over one
growth phase of duration (ln 2)/θ, they multiply by 22q/θ . Binomial partition gives each daughter a quarter of
the pairs on average, E[Fd (Fd − 1)] = F(F − 1)/4, so that division halves the expected number of pairs. Pairs
are conserved over a cycle when 22q/θ /2 = 1, that is 2q = θ (Fig. 2C). A lone replicase is sterile, so pairs,
not replicases, are the reproducing unit; a replicase that could copy itself would have no threshold (Fig. 2C;
Appendix S1).
The pair argument says what the factor two depends on (Table 1). It is a property of catalyst–template
pairs, not of binomial division: the bound holds at every size and fecundity whenever division ignores
which molecules are replicases, whatever the number and sizes of the daughters, and with complementary
strands, the load being counted per copy (Appendix S2). Divisions that look at the molecules change it:
an equal partition of replicases lowers the limit to ln(1.44/θ), and, within the model, only a division that
raises the summed pair density of the daughters above that of the mother, such as sorting the replicases into
one daughter, can exceed it. With complementary strands 16 the limit is ln(1.9486/θ). It no longer bounds
the threshold when a lone replicase can still be copied without a catalyst, which revives lineages: with
the spontaneous replication term of Bianconi et al. 15 , the thresholds that we compute in their model reach
0.87–0.91 at θ = 1 for protocells dividing at 40–60 molecules, above ln 2, because a lone replicase is never
degraded there and is copied spontaneously as fast as parasite-only cells grow, which amounts to χ = q ≈ 0.4
correct uncatalysed copies per lifetime; for strong catalysis and large protocells, the predicted limit is 0.903
(both derived; Appendix S5).

3.3

Finite fecundity spends the bonus

Real molecules decay. Let each replicase start R copies per molecular lifetime and each molecule decay at
rate one: R is the fecundity, the number of complete copies a replicase makes before it is destroyed 20,21 , and
R = ∞ is the model above. We computed Uc (n, R, θ) exactly with two independently written kernel codes
(Methods). The ceiling survives decay: at every size and fecundity, Uc (n, R, θ) ≤ un + max(0, ln(1/θ)), where
un = Uc (n, ∞, 1) < ln 2 (Methods), and the same pair density brackets the price: at θ = 1, R > eU /(2 − eU ) is
necessary at every size, and R > n eU /(2 − eU ) suffices in large protocells (Appendix S3). The price has the
same origin as the ceiling: the pair density decays at rate 2(1 − q) per molecular lifetime while a protocell
grows (Methods), and growth lasts longer the larger the protocell is relative to the fecundity.
Two orders of limits disagree. At fixed R, a mean-field argument (Appendix S3) gives as n → ∞ the
well-mixed threshold at finite fecundity,



Umix (R, θ) = max 0, − ln θ + (1 − θ)/R ,

(2)

that is, the law 1 − e−Uc = (1 − 1/R)(1 − 1/s) with s = 1/θ, whose special cases are Eigen’s at R → ∞,
5


[page 6]
Table 1 | What the factor two depends on, and what exceeds it. Limit threshold Uc (∞) = max(0, ln(1/θ) + ln(1/λc )),
where λc = qc /θ is the threshold of the limit kernel, which depends on q and θ only through their ratio; infinite
fecundity unless stated. r̄: the largest expected fraction of the mother’s ordered replicase pairs that the two daughters of
an equal division keep together, and λ∗ = min(1, 21 log2 (1/r̄)); c: weight of a replicase’s own sequence as its template,
relative to another replicase; χ: correct uncatalysed copies of a lone replicase per lifetime. Proofs for the last five rows:
Appendix S12.
rule

λc

Uc (∞) at θ = 1

status

one strand, binomial partition, k
daughters
one strand, any division that
ignores which molecules are
replicases (any number and sizes of
daughters; ln 2 at every n if no
daughter has one molecule and the
rule is not degenerate)
complementary strands 16

1/2

ln 2 = 0.693

1/2

ln 2

proved (limit kernel; limit of
Uc (n), k = 2)
bound proved (every n, R);
limit derived for daughters of
sizes proportional to n

0.51319

0.667

one strand, equal partition of
replicases
replicases sorted into one daughter
two equal daughters that together
keep at most a fraction r̄ of
replicase pairs (the lever)
partial sorting: all replicases into
one daughter with probability p,
otherwise binomial; r̄ = (1 + p)/2
replicase may copy itself, with
weight c > 0 (c = 1: as another
replicase)

0.6942

0.365

—
≥ λ∗

no threshold
≤ ln(1/λ∗ )

λ∗

∗
ln(1/λ
√ ); ln 4 for
p= 2−1

—

no threshold

lone replicase copied
spontaneously, χ correct copies per
lifetime 15

< 1/2

ln 2 + 0.243χ + O(χ2 );
none if χ ≥ 1;
0.87–0.91 at finite size
in the model of ref. 15

fusion between protocells
(pairwise, mass action)

1/2

ln 2 for invasion

6

bound proved; limit numerical,
two codes
numerical
proved (R = ∞)
bound proved (limit process,
every n/R; finite form at every
n, R)
proved (limit process, R = ∞
and as n/R → 0); limit of Uc (n)
numerical
proved at R = ∞ (every n) and,
for the limit process, as
n/R → 0; the limits R → ∞ and
c → 0 do not commute; one
more bit at c ≈ 4n/R, numerical
slope derived; above ln 2 for
every χ > 0: proved for the
reduced kernel, its
identification with y → 0
numerical; none if χ ≥ 1:
proved at every n and R
invasion threshold unchanged,
proved; no fusion raises it
above the ceiling, proved;
dense populations beyond ln 2
only if replicase carriers alone
fuse, numerical


[page 7]
A Three extrapolate to one curve
(0) = ln 2 (theorem, R = )

0.6
0.4
0.2
0.0

(y): = 1, extrapolated
exact, n = 200, = 0.5
exact, n = 200, = 1
exact, n = 200, = 1.5
limit process (simulation)

10 1
101
100
protocell size / fecundity, y = n/R

template efficiency of parasites,

bonus = Uc ln(1/ )

0.8

2.00
1.75
1.50
1.25
1.00
0.75
0.50
0.25

B Conjecture 1: Uc = ln(1/ ) + (n/R)

no maintenance: (n/R) < ln

Uc = 0.2

5
Uc = 0.5

Uc = 1
Uc = 1.5

10 1
101
100
protocell size / fecundity, y = n/R

error threshold Uc

C At fixed fecundity, the threshold declines as protocells grow
1.50
1.25
1.00
0.75
0.50
0.25
0.00

R = 40 (exact kernel)

R = (exact kernel)

well-mixed limit n

at R = 40

= 0.5
well-mixed limit, = 0.5, R = 40: ln( + (1

)/R) = 0.668

=1
well-mixed limit for

1: 0

101

102

= 1.5

protocell size at birth, n (molecules)

Fig. 4 | Finite fecundity spends the bonus. (A) Compartment bonus ψ = Uc − ln(1/θ) against y = n/R: exact kernels
at θ = 1 extrapolated in n (line and points), exact values at n = 200 for θ = 0.5, 1 and 1.5 (circles; the θ = 1.5 point
at y = 4 is omitted because Uc is there at its floor, zero), which converge to the same curve in 1/n (Table S3), and
direct simulation of the limit process (squares; error bars smaller than the symbols). (B) Threshold of the scaling limit
(Theorem 4 for y < 1; proved, computer-assisted, for 1 ≤ y ≤ 2.875, and beyond under hypothesis (H2); Appendix S3),
Uc = max(0, ln(1/θ) + ψ(n/R)), in the plane (y, θ); above the thick line replicases are not maintained in the scaling
limit (the panel title calls this law “Conjecture 1”; it is proved for y ≤ 2.875). (C) At fixed fecundity R = 40, the exact
threshold (points) falls towards the well-mixed value at finite fecundity (dashed, Eq. 2; zero for θ ≥ 1) as protocells
grow, after an initial rise for θ < 1; at R = ∞ (thin lines) it tends instead to ln(2/θ).

Demetrius, Schuster and Sigmund’s at s → ∞, and the binary-fission threshold at s = 2 (refs. 9,20,22,23).
At fixed n and R → ∞, the threshold tends instead to the protocell value. At fixed R and θ < 1 it therefore
first rises with n and then falls back, slowly, towards the well-mixed value (Methods); for θ ≥ 1 it decreases
from n = 5 on at the fecundities shown (Fig. 4C). This accounts, in mean field and for a single strand, for the
slow decline of the threshold with protocell size found by Shah et al. 16 .
The two limits are joined by a single function. The threshold is carried by protocells with a few replicases
among N molecules, and with decay such a protocell grows only if RF > N. When n and R are both large at
fixed y = n/R, the finite kernels converge to those of a piecewise-deterministic Markov process 24 for F and
u = N/R that depends on q and θ only through λ = q/θ (Methods; Appendix S3), and:

Theorem 4 (scaling). As n, R → ∞ with n/R = y < 1 fixed, Uc (n, R, θ) → max 0, ln(1/θ) + ψ(y) for every θ,
where ψ(y) = − ln λc (y) is the threshold of the limit process and ln(2/(1 + y)) ≤ ψ(y) < ln 2 (Appendix S13).
For y ∈ [1, 2.875] the same limit holds (proved, computer-assisted; Appendix S3), and beyond if the
7


[page 8]
reduced limit kernel’s spectral radius reaches one at a single λ (hypothesis (H2)), as it does numerically;
otherwise the limit points of the thresholds are bracketed (Appendix S3); that ψ decreases with y is numerical.
The exact kernels agree with the limit: for θ = 0.5, 1 and 1.5 they converge in 1/n to the same ψ, to within
10−3 at y = 0.25 and 1, and a direct simulation of the limit process agrees to within 0.8 standard errors
(Fig. 4A; Table S3; Fig. 5). The compartment bonus is ψ = 0.693, 0.618, 0.486, 0.317 and 0.18 at y = 0,
0.25, 1, 4 and 16, and ψ(y) ≈ ln 2/(1 + y/0.823)0.443 to within 0.002 on [0, 16].
The consequence is a fecundity requirement that scales with protocell size. Inverting this law, a replicase
with load U is maintained if
R ≳ Rmin =

n
ψ−1 U + ln θ

,

(3)

so that Rmin ≃ 0.22 n, 1.1 n and 3.1 n for U + ln θ = 0.3, 0.5 and 0.6 (Appendix S3); the exact kernel gives
Rmin /n = 0.25, 1.16 and 3.13 at n = 50 and θ = 1 (Fig. 1B). Compartments therefore give a trans-acting
replicase most of their help only if it makes, in its lifetime, a number of complete copies comparable with the
number of molecules in its protocell. In large protocells at fixed n/R and θ ≤ 1, R ≥ 0.35 n keeps more than
half of the bonus ln 2 and R ≤ n/3.2 less than half; at every size and θ, a replicase making, on average, at most
n/5 complete copies per lifetime gains less than 12 ln 2 over max(0, ln(1/θ)) (all proved, computer-assisted;
Appendix S3).

3.4

The fate of unfinished copies

Where stated, a copy of a full-length template stops early with probability τ, and its product is either lost or
a truncated molecule, copied faithfully thereafter, with template weight θ′ relative to a replicase. Two exact
identities (Appendix S8) show that what matters is not how often the polymerase stops but what becomes of
the product: a lost copy multiplies the fecundity required by exactly 1/(1 − τ), and a replicable copy with
θ′ = θ shifts the threshold by exactly ln(1 − τ), at every size and fecundity. A shorter molecule, however,
is usually a faster template (θ′ > θ), and exact kernels with three molecular types then show a different
behaviour (Fig. 6A). At θ′ = 2 the tolerable load falls with the number of truncated copies made per division
cycle, nτ, to a quarter or a third of its value at nτ = 1, and vanishes between nτ = 1.5 and 1.85 (n = 10 to
30). Unlike the error load, this cost grows with protocell size: large protocells make more truncated copies
per cycle. At finite fecundity both fates cost something, in the same currency (Fig. 6B). The same chemical
event, depending on what becomes of its product, costs a few percent of fecundity or the replicase itself.

3.5

Protocells and a surface differ

How much faster a truncated copy is copied depends on how the copying time of the polymerase depends on
length. If a share b of that time does not depend on length (initiation, binding, product release) and the rest
grows in proportion to it, a truncated copy of length L′ on a replicase of length L is copied 1/[b + (1 − b)L′ /L]
times faster, which is its template advantage θ′ when copying follows mass action (Methods). Protocells
impose a threshold on θ′ (Fig. 7B), with an elbow where the large-protocell ceiling ln(2/θ′ ) vanishes: a
protocell that makes one truncated copy more than twice as fast as the replicase is lost, whatever its speed,
and growth passes through the lineages that have made none (Appendix S9). The kinetic profile of the
polymerase therefore matters to protocells only through the share of its truncated copies that lie beyond the
elbow. When protocells copy as a lattice model does 5 (Methods), protocells of 20 to 80 molecules recover
only 13–20% of the damage at b = 0.15, and half of it only beyond b ≈ 0.33 (Fig. 7A); the shape holds in
8


[page 9]
0.7

R=n
ceiling ln 2 (every size and fecundity)

θ=1

100

0.6
80
R ≤ n/5:
excluded
at every
size†

0.5
0.4
0.3

60

40

0.2

scaling law
(bracket of SI S3,
R ≤ n)

Theorem 4
(proved, R > n)

0.1
0.0

share of the ceiling (%)

gain in tolerable load at θ = 1 (nats)

0.8

20

0
10−2

10−1

100

101

protocell size / fecundity, y = n/R
exact, n = 25
n = 50
n = 100
n = 200
n = 320
ψ(y), limit kernel
proved range of ψ (y < 1)
large-n limit, extrapolated
sharper lower bound†
(= ψ under (H2))
Fig. 5 | Thresholds approach one curve in n/R as protocells grow (θ = 1). Gain in tolerable load over a wellmixed pool, Uc − max(0, ln(1/θ)), which equals Uc at θ = 1, against y = n/R, protocell size (protocells divide at
2n molecules) over fecundity (copies started per replicase lifetime). Symbols: exact thresholds of the finite model,
n = 25–320 (they overlap for y < 1). Solid line: ψ(y) = − ln λc (y), computed from the limit kernel. For R > n (y < 1),
Uc → max(0, ln(1/θ) + ψ(y)) as n → ∞ at fixed y, for every θ > 0 (Theorem 4; proof in Appendix S13), and ψ(y) =
ln 2 − 0.350 y + o(y) near y = 0 (Theorem S, Appendix S14). Blue band: the proved range ln(2/(1 + y)) ≤ ψ(y) < ln 2
for y < 1; dotted blue line: a sharper lower bound for y < 1 (proved; Appendix S3). Dashed line: numerical large-n
limit for R ≤ n, extrapolated in 1/n from n = 100, 200 and 320; that it equals ψ(y) rests on hypothesis (H2), proved,
computer-assisted, for 1 ≤ y ≤ 2.875 (Appendix S3). Grey line: the ceiling ln 2, proved at every size and fecundity.
Hatched: gains excluded at every size when R ≤ n/5 (proved, computer-assisted; Appendix S3). Right axis: percentage
of the ceiling; the computed limit falls below half of it near y ≈ 3.1 (R ≈ 0.32 n), and ψ is proved to stay above half of
the ceiling up to y = 2.858 and below it on [3.2, 5] (computer-assisted; Appendix S3). In the panel, the daggers mark
the two bounds of Appendix S3.

9


[page 10]
B Lost, it costs a few percent of fecundity; fast, all

1.0

Fecundity required, relative to = 0

Tolerable load, relative to = 0

A A replicable fast copy costs load as n grows

0.8
0.6
0.4
lost (no product)
replicable, 0 = (n = 20)
replicable, 0 = 2, n = 10
replicable, 0 = 2, n = 20
replicable, 0 = 2, n = 30

0.2
0.0

10 2

10 1

lost: 1/(1 ), exact
replicable, n = 20, U = 0.30
replicable, n = 20, U = 0.45
replicable, n = 10, U = 0.45

10

no fecundity
suffices

5

2
1

100

10 3

Truncated copies made per cycle, n

10 2
Probability that a copy stops early,

Fig. 6 | The fate of an unfinished copy decides which requirement termination consumes. (A) Tolerable load at
infinite fecundity, relative to its value without termination, against the number nτ of truncated copies made per division
cycle (θ = 1). A lost truncated copy costs nothing (orange; exact). A replicable truncated copy exactly as good a
template as a full-length parasite (θ′ = θ) only adds the load − ln(1 − τ) (grey dashes; exact, n = 20). A replicable
truncated copy twice as fast a template as the replicase (θ′ = 2; exact kernels, n = 10, 20, 30) costs load as nτ grows,
nearly independently of n up to nτ ≈ 0.3, and leaves no tolerable load beyond nτc = 1.85, 1.61 and 1.53 for n = 10, 20
and 30 (squares). (B) Fecundity required, relative to its value without termination. For the lost fate it rises by exactly
1/(1 − τ) (orange). For the replicable fate (θ′ = 2; exact kernels with decay; n = 20 at U = 0.30 and 0.45, n = 10 at
U = 0.45) it rises sevenfold at τ = 0.03 for U = 0.30, and, for n = 20 and U = 0.45, no fecundity suffices at τ = 0.03
(arrow).

B Beyond = 2, speed matters little

1.0

Critical truncated copies per cycle, n c

Share of the damage recovered, D(b)

A Protocells gain from b late, the lattice at once
0.8
0.6
0.4

protocells, n = 20
protocells, n = 40
protocells, n = 80
two classes, beyond b = 0.3
every length
lattice (Tupper & Higgs 2017)
lattice, reimplementation

0.2
0.0
0.0

0.2
0.4
0.6
0.8
1.0
b, length-independent share of copying time

10
0

=2

n=5
n = 10
n = 20

5
2
1
0.5

1
2
4
10
Template advantage of the truncated copy, 0

Fig. 7 | Protocells and a surface respond differently to how copying time depends on length. (A) Share of the
damage done by replicable truncated copies that is recovered when the length-independent share b of the copying time
grows, D(b) = [log mc (b)−log mc (0)]/[log mc (1)−log mc (0)], with mc the critical termination probability per nucleotide
at vanishing error load. The protocells (exact kernels, n = 20, 40, 80) copy as the lattice does: a copy stops at each
nucleotide with probability m, a product shorter than 10 nucleotides is lost, copies of truncated templates stop in the
same way, and a copy that stops early ends sooner (truncated lengths in two classes split at θ′ = 2, a grouping that
overestimates the threshold near the elbow and beyond: dashes beyond b = 0.3; points keep every truncated length, by
a population Monte Carlo, and are offset slightly in b for legibility; Appendix S9). They recover 13–20% of the damage
at b = 0.15, and half of it only beyond b ≈ 0.33. The lattice model of Tupper and Higgs 5 recovers 55% at b = 0.15,
and half near b ≈ 0.12: black, their published threshold (1024 × 1024 sites); grey, a reimplementation (256 × 256 sites,
runs to t = 120), with brackets on D derived from those of its threshold (Appendix S10). Other protocell variants:
Fig. S2. (B) With a single truncated length, the critical number of truncated copies per cycle nτc against their template
advantage θ′ (n = 5, 10, 20): beyond θ′ = 2, where the large-protocell ceiling ln(2/θ′ ) vanishes, it depends only weakly
on θ′ .

10


[page 11]
A Measured systems lie outside the viable region
=1
= 1.5
n = 10

ln 43 ln 2
3
10 viable
( = 1, n = 10)

102
101
TPR, 29-nt own fragment
R = 1: a replicase must at least replace itself
52-2

100
10 1

24-3

10 3

103

QT45, own sequence
and complement
tC19Z fidelity (fecundity unknown)

10 2
0

104

n = 50
measured systems

required fecundity Rmin

fecundity R (complete copies per lifetime)

104

scaling law
exact kernel, = 1
exact kernel, = 1.5

U + ln = 0.65
U + ln = 0.6
U + ln = 0.5
U + ln = 0.3

102
101
100
10 1
10 2
10 3

1
2
3
error load per replicase copy, U

B The fecundity needed grows with protocell size

QT45, own sequence and complement

101
102
103
protocell size at birth, n (molecules)

Fig. 8 | Requirements and measured polymerase ribozymes. (A) Error load U (for a 53-bit replicase with ℓ = 0.56,
errors counted as complete parasites) and fecundity R (complete copies per template lifetime) of measured systems
(Table 2; Table S4), against the exact viability boundaries U = Uc (n, R, θ) for n = 10 (solid) and n = 50 (dashed), θ = 1
(orange) and θ = 1.5 (green); the shaded region is viable for θ = 1, n = 10. Dotted vertical lines: the large-protocell
limits at R = ∞, ln 2 and ln(4/3). No replicase is maintained below R = 1. The QT45 bar spans the fecundities
of its own sequence and of its complement, with the measured half-life and one extrapolated from it to its copying
buffer; 24-3 is placed at its full-length fidelity (counting partial products would put it at U = 2.38); the 52-2 bar spans
a fecundity measured on a ligase and one extrapolated from a short reaction, and the horizontal arrow indicates that
its lowest published fidelity is off scale (U = 4.7); the upward arrow marks a lower bound on the fecundity of the
TPR fragment; tC19Z has the highest average measured fidelity, but its fecundity on its own sequence is unknown. (B)
Fecundity required in a protocell of n molecules for four values of the effective load U + ln θ: scaling law (Eq. 3; lines)
and exact kernels at n = 10 and 50 (points, interpolated between computed boundaries; exact roots in Fig. 1B). Grey
band: fecundity of QT45 on its own sequence and on its complement.

every variant we tried (Appendix S9). On a surface the response is different, as Tupper and Higgs 5 found
with their lattice model: there a length-independent share b = 0.1 already multiplies the tolerable termination
tenfold, against 1.5–1.6 in protocells that copy in the same way, and their published threshold recovers half
of the damage near b ≈ 0.12, and 55% at b = 0.15 (Fig. 7A). Earlier comparisons of compartments and
surfaces concerned survival and long-term evolution 16,25 .

3.6

Measured ribozymes miss two requirements

Fig. 1C, Fig. 8 and Table 2 place measured polymerase ribozymes in the plane of error load and fecundity.
The load of a replicase copy is U = ℓIε, with ε the per-nucleotide error rate of each chemistry, I = 53 bits the
functional information 26 of the 45-nucleotide QT45 (ref. 10), the only replicase for which such an estimate
exists, and ℓ = 0.56 the number of lethal substitutions per bit, computed from the tolerance of each of its
sites measured by the same authors (Methods). Fecundity is computed from published yields, reaction times
and half-lives as the number of complete copies made per template lifetime (Methods).
QT45, the only polymerase ribozyme that has copied its own sequence, makes 0.006–0.10 complete
copies of its complement from its own sequence, and 0.004–0.07 copies of itself from its complement, per
template lifetime, with the ribozyme in tenfold excess over the template (Appendix S6). At the per-nucleotide
fidelity measured for the complement of its own sequence, 0.941, its load is U ≈ 1.8. Whatever the size of
the protocell, maintenance needs R > eU ≥ 1, the extinction criterion of lethal mutagenesis 20,34 , here proved
11


[page 12]
Table 2 | Measured polymerase ribozymes against the first two requirements, for a 53-bit replicase with ℓ =
0.56 and θ = 1. 1 − ε: per-nucleotide fidelity. Load gap: U/ ln 2, the factor by which the error load exceeds the
protocell ceiling at infinite fecundity. Fecundity gap: 1/R, the factor by which fecundity per template falls short of the
minimum R = 1 at vanishing load; for QT45, its lower end rests on a half-life extrapolated to the nominal, pre-freezing
composition of the copying buffer (5–25 given the potassium uncertainties of that extrapolation, 27 with 200 mM KCl
in the buffer of the measurement; Appendix S6). σ: fraction of copying slots that end in a complete copy (Methods);
for QT45 an upper bound, copying its own sequence (≤ 1.7 × 10−3 copying its complement), since its copy time is not
measured. Sources, conversions and caveats: Table S4.
system

what was copied

1−ε

load gap

fecundity gap

σ

QT45 (ref. 10)

its own sequence (45 nt)
and its complement
other templates
a ligase; or extrapolated
to own length
fragment of own core, pH
cycles
other templates

0.941

2.5

10–250

≤ 2.4 × 10−3

0.97b
0.84–0.92

1.3
3.6–6.8

42–56
4.0–56

(2.1–2.5)×10−3
0.008–0.096

0.974a

1.1

none (R ≥ 1.26)

0.26

0.9912

none (0.38)

unknown

—

24-3 (refs. 27,28)
52-2 (refs. 29,30)
TPR, 29-nt own
fragment 31
tC19Z 32
a

b

Fidelity of the ancestor t5+1 (ref. 33), borrowed. Full-length products; 0.92 when all products, including partial ones, are
counted 27,28 .

for a trans-acting replicase in protocells of every size: a replicase must at least replace itself (Appendix S3).
QT45 is therefore short by a factor of 10–250 in fecundity even at vanishing load (5–27 at the lower end,
given the uncertain potassium content of the buffers; Appendix S6), and by a factor of 2.5 in load even
at infinite fecundity (2.3–2.7 over the range of ℓ). Taking its measured fitness landscape as replication
rates, as for a self-copying template, Gianni et al. 10 report that a fidelity of 0.974 would keep about 12%
of a population active. For a replicase that copies whatever template it meets, the protocell ceiling sets a
comparable target, 0.977 (0.974–0.978), but only for large protocells at infinite fecundity; at the fecundity
measured, no fidelity suffices. The class I polymerases 24-3 and 52-2 are short in both directions as well 27–30 ;
a fragment of the triplet polymerase copied above R = 1 31 and the most accurate polymerase, tC19Z 32 , each
meet at most one requirement (Table 2; Appendix S6).
The two gaps differ in size (Table 2). In load, the chemistries measured are within a factor of 1.1–
3.6 of the protocell ceiling, and up to 6.8 for the lowest published fidelity of 52-2; tC19Z is inside it. In
fecundity, QT45 is 1.0–2.4 orders of magnitude short of replacing itself, and the class I polymerases are
4–56 times short on other templates; for QT45 and 24-3 the fecundity gap is the larger. Improving fidelity
alone cannot close it, because in the scaling limit the load ceiling itself recedes as n/R grows (Eq. 3): for
a 53-bit replicase with θ = 1, a protocell requires a per-nucleotide fidelity above 0.977 if R ≫ n, 0.984 if
R = n and 0.989 if R = n/4, the last close to the best average fidelity measured. Termination raises the target
further (Appendices S8 and S11, Table S6).

4

Discussion

For a trans-acting replicase in protocells that divide by random partition, we have computed what the higherlevel unit presupposed by the relaxed error threshold 14 can supply. When parasites are no better templates
than the replicase (θ ≤ 1), it is a factor of at most 2 in effective superiority, that is, ln 2 on the tolerable
load, reached in the large-protocell limit at infinite fecundity. When parasites are better templates (θ > 1),
no fidelity suffices in bulk, protocells of any size add less than ln 2, and large ones only max(0, ln(2/θ)).

12


[page 13]
Estimates of the relaxed threshold that rest on a superiority of order 351 (refs. 11–13) therefore do not
carry over to the first replicase: in protocells its tolerable load, and with it the maximal replicase length at a
given fidelity, is smaller by a factor of ln 351/ ln 2 ≈ 8.5. This gives a quantitative form to the objection of
Tupper and Higgs 5 . Applying Eigen’s threshold to QT45 at its measured fidelity of 0.941, Gianni et al. 10
find that it needs a selective superiority above 166 (their fig. S32), for a (+)/(−) cycle of 84 nucleotides
in which every substitution is lethal; per copy of one strand this is a load of 2.6, about 3.7 times the ln 2
that bounds what a protocell of any size adds, and 2.5 times when only the substitutions that lower activity
below 80% count (Table 2). What is new, relative to numerical solutions of protocell models 6,7,15,16,35,36 , is
the limit and its mechanism, which turn numerical thresholds into a rule: the threshold is max(0, ln(1/θ) +
ln(1/λc )), the well-mixed term ln(1/θ) plus a compartment constant ln(1/λc ) fixed by how division treats
pairs. Transient compartmentalization with pooling 8,17,18 , computed for a trans-acting replicase without
external selection, stayed below the ceiling (Appendix S5); spatial self-organization on surfaces 5,35,37,38
remains to be computed.
The ceiling depends on a single property of the parasites, their template efficiency relative to the replicase.
Deletion mutants, the parasites that arise first in experiments, are better templates than the molecule they
derive from: θ = 1.2–1.7 for parasites copied by Qβ replicase alongside a ribozyme 8,18 , for which the largeprotocell ceiling ln(2/θ) is only 0.16–0.50. Complex formation raises θ further, a replicase bound as a catalyst
being unavailable as a template 36,39 , most in small vesicles: in a 100-nm vesicle holding 100 molecules, the
ceiling falls to 0.32 for a Michaelis constant of 0.7 mM (Appendix S5). Within the model, under division
that ignores which molecules are replicases, the one lever that raises the ceiling is template discrimination,
θ < 1: a replicase that prefers functional templates, for instance through a recognition tag 4 or a hybridization
motif shared by kin 2 , adds ln(1/θ) to the well-mixed threshold, and protocells add ln 2 on top.
The ceiling assumes a division blind to molecular identity and a sterile lone replicase. A division into
two equal daughters that together keep on average at most a fraction r̄ of the mother’s replicase pairs (r̄ = 1/2
under random partition) caps the compartment constant of large protocells at ln[2/ log2 (1/r̄)] (for r̄ ≥ 1/4),
which partial sorting reaches at high fecundity: ln 4 requires keeping 71% of pairs together, ln 8 requires
84% (Fig. 9). A lone replicase copied correctly without a catalyst χ times per lifetime raises the limit to
√
ln 2 + (3 2 − 4)χ + O(χ2 ), and χ ≥ 1 removes the threshold (Fig. 10). One that can copy itself, with weight
c relative to another replicase, has no ceiling at high fecundity, the limits R → ∞ and c → 0 not commuting;
one more bit requires c ≈ 4n/R (Fig. 11). Fusion between protocells leaves the invasion threshold unchanged,
and no fusion raises it above the ceiling; in our computations only fusion restricted to replicase carriers,
which sees content, kept dense populations beyond ln 2 (Fig. 12).
Finite fecundity turns the ceiling into a requirement on R that grows with protocell size (Eq. 3): keeping
nine-tenths of the bonus requires R ≳ 4.5 n, that is, about 90 complete copies per lifetime in a protocell
of 20 molecules. That completion, not accuracy, is what limits existing polymerase ribozymes has been
stated before 1,2,14,40 . Comparing protocells with surfaces in closely matched models, Shah et al. 16 found
that polymerases survive in protocells at a replication rate, relative to strand breakdown, about six times
lower than on surfaces where growth is limited locally. What is new here is the size of the gap on each
axis, measured against a ceiling and a fecundity requirement that are computed rather than assumed, and
the growth of that requirement with protocell size. Two consequences follow for experiments. First, the
quantity that decides whether compartments can help, the number of complete copies of the replicase’s
own sequence per template lifetime in the conditions where it copies itself, is not reported: for QT45 the

13


[page 14]
2.00
1.75
1.50
1.25
1.00
0.75
0.50
0.25
0.00

2.00
1.75
1.50
1.25
1.00
0.75
0.50
0.25
0.00

threshold Uc

B

compartment bonus (y) = ln c

A

lever ceiling ln(1/ * ) (proved)
ln L: lower bound on (derived)
converged

10 1

truncation not converged
beyond 3(p): truncated kernel

100

y = n/R

p = 0 (random; 1 bit)

p = 0.2

p = 2 1 (2 bits)

exact threshold Uc(n)
finite-size bound ln(1/ n* )
limit ceiling ln(1/ * )

10
20
40
80
160
protocell size n (exact kernels, R = , = 1)
p = 0.6

p = 23/4 1 (3 bits)

2.0
1.8
1.6

B Finite fecundity (qs = q, = 1)

A Ceiling at y 0
1.0

reduced kernel, revival uniform
in N (this model)
in ln N (as in R2 )
first order, ln 2 + (3 2 4)

0.9
0.8

1.4 2 ln 2
1.2
1.0
0.8

(y; )

(0; ), large protocells at high fecundity

Fig. 9 | The lever: how a division that keeps replicase pairs together raises the ceiling. Partial sorting: at division,
all replicases go to one daughter with probability p, otherwise at random. The two equal daughters then together keep
on average a fraction r̄ = (1 + p)/2 of the mother’s ordered replicase pairs, and the lever bound is λc ≥ λ∗ = 21 log2 (1/r̄).
(A)
bonus ψ(y) = − ln λc of the limit process against y = n/R, for p = 0 (random partition), 0.2,
√ Compartment 3/4
2 − 1, 0.6 and 2 − 1. Dashed lines: the ceilings ln(1/λ∗ ), that is ln 2, ln 4 and ln 8 for one, two and three bits,
reached as y → 0 (proved). Dotted lines: − ln λL (p), a lower bound on ψ at every y obtained from replicase-rich
protocells, which partial sorting keeps rich (derived, not proved). Filled circles: thresholds converged in the truncation
(|∆λc | < 10−4 , numerical); open circles: thresholds of the kernel truncated at 400 replicases, not converged. Triangles:
for p > 0, points beyond λ3 (p) = 31 log2 (4/(1 + 3p)), where no admissible cut is proved; there λc is defined through
finite truncations (Appendix S12), and the plotted value is that of the truncated kernel. Open symbols bound ψ from
below (numerical), loosely where the truncation is far from convergence. (B) Exact thresholds of the finite model at
θ = 1 and infinite fecundity, against protocell size n, for the same p; dashed lines as in A, thin solid lines the finite-size
bounds ln(1/λ∗n ). The thresholds never exceed ln(1/λ∗n ) (proved), with equality for p = 0. For p > 0 they lie above
ln(1/λ∗ ) from n = 40 to n = 160 and decrease towards it (numerical); at n = 10 they lie below it, except for p = 0.2.

U = ln
R2 limit, _eff = q:
U* = 0.903

correct uncatalysed copies
=0
= 0.1
= 0.3
= 0.5
ln 2

0.7
0.6

= 0.5
= 0.3
= 0.1
=0

0.5

+10 %
ln 2 (sterile lone replicase)

0.4

0.6

0.0
0.2
0.4
0.6
0.8
, correct uncatalysed copies of a lone replicase per lifetime

0.01

0.03
0.1
0.3
1
y = n/R (protocell size / fecundity)

2

Fig. 10 | A lone replicase copied without a catalyst pierces the ceiling. (A) Limit ψ(0; χ) for large protocells at high
fecundity (y = n/R → 0) against χ, the number of correct uncatalysed copies of a lone replicase per lifetime, from
the reduced kernel (numerical): revival at a stage of growth uniform in N, as in our model (solid), or uniform in ln N,
as with the exponential growth√of mass-action catalysis in the R2α model of Bianconi et al. 15 (dashed); dotted, the
first-order expansion ln 2 + (3 2 − 4)χ (derived). In R2α, χeff = q, so that the predicted threshold for α, m → ∞
(α ≪ 2m ) lies where the dashed curve meets U = − ln χ (dot, U ∗ = 0.903). Grey lines: the ceiling ln 2 of a sterile lone
replicase, 10% above it, and 2 ln 2. (B) ψ(y; χ) at finite fecundity for χ = 0, 0.1, 0.3 and 0.5 (limit process, q s = q,
θ = 1; numerical); at θ = 1 the threshold is Uc → ψ. Only for χ = 0 does ln 2 (dashed) bound ψ at every y.

14


[page 15]
c=1

4.0
3.5
c = 0.3
3.0
2.5
c = 0.1
2.0
1.5 c = 0.03
1.0 c = 0.01
0.5 c = 0 (trans)
0.0
10 2

B
exact kernels, n = 40, = 1
limit process

6
5
as y 0

= ln c (limit of Uc + ln )

A 4.5

ln ( ) (derived)
closed form (numerical)
ln( ln2)

4
3
2

ln 2

10 1
y = n/R

1
0

100

ln 2

10 1

100 101 102
= c/y = cR/n

103

Fig. 11 | A replicase that can copy itself has no ceiling at high fecundity, because the limits of infinite fecundity
and vanishing self-copying do not commute. (A) ψ = − ln λc of the limit process (lines) against y = n/R, for a weight
c of the replicase’s own sequence as template relative to another replicase (c = 0: trans copying, the model of the main
text; c = 1: the self-copying variant of Appendix S1). For c > 0 the identification of ψ with the limit of Uc + ln θ is
numerical; circles: exact kernels at n = 40, θ = 1. Dashed: the ceiling ln 2 of trans copying. At c = 0, ψ stays below
ln 2 at every y; for every c > 0 it diverges as y → 0, as ln(c ln 2/y) + O(1) (proved), but exceeds ln 2 only when c
exceeds a value that vanishes with y (0.0083 at y = 0.05). (B) The same threshold at high fecundity as a function of
c̃ = c/y = cR/n alone (κ in the figure; Λ for λcis ): − ln λcis (c̃) from λc̃ ln 2 [G(λ) − 1] = 1 (line, derived and checked
on the limit process), its closed-form approximation ln{1 + [1 + (c̃ ln 2)2 ]1/2 } (dashed, within 0.03), the ceiling ln 2
recovered as c̃ → 0 and the cis replacement asymptote ln(c̃ ln 2) (dotted) reached as c̃ → ∞. At R = ∞ and fixed c > 0,
c̃ = ∞: no threshold at any size.

Protocells with F 2 (density, units of 1/ )

A Fusion between all protocells (blind)
Uc

ln 2

/ =1
/ = 10
/ = 100
/ =

101
100
10 1
10 2
10 3

0.4

0.5
0.6
Load U = lnq

0.7

B Fusion only between replicase carriers (sees content)
Uc

105
104
103
102
101
100
10 1
10 2
10 3

ln 2

/ = 100

/ = 300

/ = 1000

/ = 30

0.4

0.6

0.8
1.0
Load U = lnq

1.2

1.4

n = 5, R = 25, = 1; solid: stable, dashed: unstable (reaches zero density at Uc, below the plotted range); dots: folds

Fig. 12 | Fusion changes the persistence of dense populations, not invasion. Equilibrium density of protocells with
at least two replicases, in units of 1/k f , against the load U = − ln q, for n = 5, R = 25 and θ = 1 (numerical); k f (κ in
the figure) is the fusion rate per pair of protocells and µ the rate of removal per unit density (Appendix S5). Solid lines,
stable equilibria; dashed lines, unstable equilibria, which reach zero density at Uc , below the plotted range; dots, folds.
Vertical lines: Uc , the invasion threshold of the branching process of the main text (dotted), and ln 2 (dashed). (A)
Fusion between all protocells, a rule blind to content, at k f /µ = 1, 10, 100 and ∞ (blues, light to dark): the equilibrium
vanishes at Uc and there is no bistability. (B) Fusion restricted to protocells that carry replicases, a rule that sees content,
at k f /µ = 30, 100, 300 and 1000 (oranges, light to dark): the branches fold back, so that between Uc and the fold an
established population persists while a rare one cannot invade; the fold lies beyond ln 2 from k f /µ = 100 on. Panels
use distinct colour ramps, so that a colour never stands for two values of k f /µ.

15


[page 16]
half-life has been measured in its standard reaction conditions 10 , not in the buffer in which it copies itself
(Appendix S6). Second, a fidelity target stated without a fecundity is incomplete. A shorter replicase acts on
both requirements at once, provided that its information content shrinks with it.
Unfinished copies are the third requirement. Lost, they cost fecundity by a factor 1/(1−τ), negligible for a
stop probability of a few percent; replicable and faster than the replicase, they cap the tolerable load of every
protocell that makes about one per division cycle, so that large protocells, which make more, suffer most.
Stop rates have been measured, but not what decides between these regimes: whether a truncated product
is extended, abandoned or copied, how good a template it is, how much of the stopping is dissociation
rather than termination (a trap experiment would tell), and the length-independent share of the copying time
(pre-steady-state kinetics would give it).
Our protocell population is infinite and unstructured, protocells do not compete for resources and divide
at a fixed size, there is one class of parasites, of fixed template weight, and truncated molecules come in a
few length classes or at every length and, unless stated, are copied without stopping (Appendix S9). The
comparison with a surface rests on one lattice model, concerns the shape of the response to b, and compares
levels only as orders of magnitude. The limit max(0, ln(2/θ)) is proved for the limit kernel and, as the limit
of the exact thresholds, for every θ; the well-mixed limit at fixed fecundity is derived in mean field, and the
scaling law in n/R, proved for n/R ≤ 2.875 (computer-assisted for R ≤ n), rests beyond on one property
of the limit process, supported numerically (Methods). The information content and the number of lethal
substitutions per bit have been estimated for a single replicase, QT45, and fecundities are estimates from
single yields and half-lives, often on templates other than the replicase itself.
The error threshold of an RNA world is usually stated as a fidelity. Protection by protocells has a ceiling
and a price: protocells can at most halve the share of correct copies an RNA replicase must make, and they
give most of this protection only to a replicase that makes, in its lifetime, a number of complete copies
comparable with the number of molecules in its protocell. Unfinished copies add a third requirement: they
must be lost, too rare to matter, or slow templates that are themselves copied to the end. Measured polymerase
ribozymes are closer to the first than to the second; the third has been measured only in part.

5

Methods

5.1

Model and dynamics

A protocell is described by (F, P), N = F + P. Time is counted in molecular lifetimes. Each replicase starts
copies at rate R; the template is drawn among the N − 1 other molecules with weight 1 for a replicase and θ
for a parasite; the copy of a replicase is a replicase with probability q and a parasite otherwise; the copy of a
parasite is a parasite. The total copying rate is thus RF, and a copy is a new replicase with probability p(F, N)
of Eq. 1. Each molecule decays at rate 1 (no decay at R = ∞, where only the sequence of copies matters).
A protocell that reaches 2n molecules divides, each molecule going to either daughter with probability 21 ;
states with F ≤ 1 are dead. The model is the “R2α” replicase of Bianconi et al. 15 without their spontaneous
replication (the constant term in their rates), with a parasite of template weight θ instead of 1. Spontaneous
replication lets a lone replicase be copied without a catalyst; for a replicase of 100–200 nucleotides, whose
complete non-enzymatic copy is out of reach, we leave it out and treat it as a variant. In the package model of
Niesert et al. 6 , likewise, the molecule to be copied is drawn from the whole pool, so that a single functional
gene remains replicable; this also changes the limit (Table 1). When Qβ replicase, which amplifies RNA
16


[page 17]
in vitro 41 , copies a 362-nt ribozyme together with shorter parasitic RNAs that arose in the experiment, the
parasites are copied 1.2–1.7 times faster 8,18 .

5.2

Threshold criterion

Protocells form a multitype Crump–Mode–Jagers branching process, whose Malthusian parameter has the
sign of ρ − 1, where ρ is the spectral radius of the mean matrix of living daughters per division 42 . The
threshold Uc = sup{U : ρ(U) > 1} therefore does not depend on how long cycles last, which matters at
finite R. We take as type the number f of replicases at division. The mean matrix is K = B H + 21−2n I,
where B( f, s) is the probability that the partition of a protocell with f replicases creates a daughter in the
transient state s = (F, P) with F ≥ 2 and N ≤ 2n − 1 (summed over both daughters), H(s, f ′ ) the probability
that a protocell in state s reaches division with f ′ replicases, and the last term the daughter that receives all
2n molecules. H solves (I − PT T )H = PT D for the jump chain restricted to transient states, by sparse LU
factorization. ρ(K) is computed by dense eigenvalue solvers or, for n ≥ 60, by power iteration, and the root
of ρ(U) = 1 by Brent’s method with tolerance 10−7 . Two codes written independently from this description
agree to within 5 × 10−7 on the seven finite-R thresholds computed with both (n = 20–100) and to 10−6 on
nine points of the scaling limit. At R = ∞, an independently written code reproduces our 70 thresholds for
n ≤ 60 to the four decimals given (the original bisection tolerance was (1–2) × 10−5 ); that code was itself
checked against a second formulation by types at birth (|∆ρ| ≤ 3 × 10−15 on 24 cases) and against a Monte
Carlo simulation of the branching process (agreement in ρ to within 3 × 10−4 ). Limits in n were extrapolated
by fitting a0 + a1 /n + a2 /n2 to the three largest sizes (Table S1).

5.3

Proofs

Theorem 1: in the fictitious clock where the ν = F − 1 replicase templates are copied at rate 1 and parasites
at rate θ, the jump chain is that of Eq. 1, ν is a Yule process of rate q whose dynamics do not involve
P, and E[ν(ν + 1)] grows as e2qt . When n → ∞ at fixed F, the growth phase lasts (ln k)/θ in probability,
P
and the second factorial moment of the binomial partition gives E[ d Fd (Fd − 1)] = F(F − 1)/k. Hence
B∞ h = k2q/θ−1 h for h = F(F − 1). The h-transformed chain has drift Eh [F ′ | F] = kλ−1 F + (3 − 2/k)kλ − 1,
with λ = q/θ, so that Foster’s criterion gives positive recurrence for λ < 1 and h identifies the spectral
radius of the infinite matrix 43,44 . This extends by one order the first-moment balance that Bianconi et al. 15
used to bound the threshold: the first moment of F gives inequalities, the second factorial moment gives
the value. Theorem 2: during growth, each copy changes F(F − 1) by 2q F(F − 1)/W in expectation, with
W = θ(N − 1) + (1 − θ)(F − 1). For θ ≤ 1, W ≥ θ(N − 1), and q ≤ θ/2 makes ϕ = F(F − 1)/(N − 1) a
P
supermartingale; for θ ≥ 1, W ≥ N − 1, and q ≤ 12 does. At division, E[ d ϕd ] = (1 − 21−2n )ϕ, the only
loss coming from daughters of size one. The Collatz–Wielandt inequality then gives ρ ≤ 1 − 21−2n , without
any assumption on the monotonicity of ρ in q. For θ ≥ 1, W ≤ θ(N − 1) also gives the reverse inequality
at q > θ/2, hence the lower bound. Theorem 3: in the fictitious clock, the parasites of a daughter form, up
to a number of molecules that does not grow with n, a Yule process of rate θ started from about n, so that
its growth phase lasts (ln 2)/θ in probability and F − 1 at division converges in law to the Yule process of
rate q at that time; the finite kernel therefore converges to B∞ entry by entry (with an error close to 1/n in
our computations). The spectral radius of the finite kernel is at least that of each of its principal submatrices,
which converge to those of B∞ , and these reach 22q/θ−1 because the h-transformed chain is recurrent. Hence

17


[page 18]
lim inf n ρn (q) ≥ 22q/θ−1 > 1 for θ/2 < q < min(θ, 1), and Theorem 2 gives the upper bound for θ ≤ 1.
For θ > 1 the upper bound uses three further facts. At infinite fecundity ρn never decreases as q grows,
at every size: the number of replicases at division increases stochastically with q and with the replicase
content of a protocell, and a molecule-by-molecule coupling carries this through the partition. At the single
point qε = min(1, θ/2)e−ε , protocells rich in replicases drift back uniformly in n, by the supermartingales
(F−1)F · · · (F+a−2) Γ(N−1)/Γ(N−1+Λa) with Λ = max(q, q/θ). A Schur reduction onto finitely many types
then carries the eigenrelation of B∞ over to ρn (qε ) < 1 for large n, so that lim supn Uc (n) ≤ max(0, ln(2/θ))+ε.
Full proofs are in Appendices S1–S2.

5.4

Approach to the limit

The exact thresholds approach the limit as Uc (n) = ln(2/θ) + ζ(θ)/n. For θ ≤ 2, a formal expansion to
first order gives ζ(θ) = 2(1 − 1/θ)/ ln 2 (Appendix S2): −2.885 at θ = 0.5 and +0.962 at θ = 1.5, against
−2.88 and +0.962 fitted to the exact thresholds, and 0 at θ = 1, where the correction is exponentially small
(−21−2n / ln 2). For θ ≥ 2, where the limit is zero, the exact thresholds decrease numerically as about 1/n.
With any partition that ignores which molecules are replicases, the threshold is at most ln 2 + max(0, ln(1/θ))
at every size and fecundity, and at θ = 1 and infinite fecundity it equals ln 2 at every size when no daughter
receives a single molecule and some daughter receives between 2 and 2n − 1, as with a hypergeometric
partition (Appendix S2). With growth by a factor k and division into k daughters the threshold is again
q = θ/2 (Theorem 1): the factor two is thus not the familiar requirement that “at least half of the daughters
should, on average, survive” in binary fission 18 , which would give ln k with k daughters.

5.5

Finite fecundity

At θ = 1, for Z = F(F − 1)Γ(N − 1)/Γ(N − 1 + 2q) and N ≥ 3, the copying terms of the generator cancel
exactly and E[dZ] = −2(1 − q)Z dt (checked on 2 × 104 random states to a relative error of 3.5 × 10−8 , and
in exact rational arithmetic): between divisions Z decays at exactly the rate 2(1 − q) per molecular lifetime,
whatever the state of the protocell, and a division multiplies its expectation by the R = ∞ spectral radius. For
every θ, with q replaced by Λ = max(q, q/θ), Z remains a supermartingale if Λ ≤ 1, which bounds ρ at every
size and fecundity by the R = ∞ spectral radius at θ = 1 and q = Λ; for Λ ≥ 1 row sums bound ρ by its value
at θ = 1, q = 1 and R = ∞ (Appendix S2). The mean-field limit Eq. 2 follows from ẋ = Rx2 (q − ω)/ω with
ω = x + θ(1 − x), for the replicase fraction x, and d ln N/dt = Rx − 1. The exact thresholds approach it slowly,
empirically as n−1/2 for θ < 1 (for θ = 0.5 and R = 10: 0.823, 0.721 and 0.657 at n = 20, 100 and 400,
against 0.598), and as ≈ 2/n towards zero for θ = 1.5; the convergence is not proved. Shah et al. 16 concluded
that “Mmax must tend to zero for very large S 0 ”, S 0 being the number of strands at which protocells divide;
Eq. 2 agrees with this for θ ≥ 1, whereas at R = ∞ the threshold of their model tends to ln(1.9486/θ). The
limit process of Theorem 4 is obtained by letting n, R → ∞ at fixed y with F = O(1), and the finite kernels
are proved to converge to its kernel (Appendix S3): parasites then follow their mean to relative order N −1/2
and W = θN(1 + O(1/N)), and the process is piecewise deterministic for F and u = N/R: u̇ = F − u between
jumps, F → F + 1 at rate λF(F − 1)/u, F → F − 1 at rate F, and division at u = 2y. There Z = F(F − 1)u−2λ
decays at rate 2(1 − λ) and each division multiplies it by 22λ−1 ; the threshold is where the two balance,
(22λ−1 − 1) κ = 2(1 − λ) (an exact rewriting at threshold, provided the Z-moments are finite; Appendix S3),
with κ the Z-weighted division rate of the stable population: at R = ∞ cycles take no time, κ = ∞ and λc = 12 ;

18


[page 19]
as y grows cycles lengthen, κ falls and λc rises towards one. The process was simulated by exact sampling
of the jumps along the deterministic flow, without population control, to estimate ψ(y) independently of the
√
kernels (Appendix S3). The slope of ψ at the origin is −(3 2 − 4)/ ln 2 = −0.350 (proved; Appendix S14),
and beyond y ≈ 30 ψ decays more slowly than the fit given in the main text. A related scaling law, in which
the size of a collective and the mutation rate combine into a single variable, governs the balance between
within- and among-collective evolution in another model 45 .

5.6

Unfinished copies

Exact kernels with replicases, parasites and truncated molecules, and the three identities, are given in Appendix S8. At θ′ = 2 the tolerable loads for n = 10 to 30 differ by 3% at nτ = 0.3. Over the range computed
at finite fecundity (n ≤ 20, R ≥ 10, τ ≤ 0.03) the replicable fate costs 16 to 310 times more load than the
lost one, and the share of the tolerable load that it removes hardly depends on fecundity. Whether copies of
truncated templates stop in turn decides how the threshold scales with protocell size. If they do not, slow
truncated copies form a bath in which the lineages that carry growth copy the replicase only two to three
times per cycle, and τc tends to a finite limit, 0.18 at b = 0 with two classes at the elbow; if they do, as on
the lattice, these lineages are made mostly of replicases and τc falls as 1/n (Appendix S9, Fig. S1).

5.7

Termination and copying time

A dissociation interrupts a copy without ending it: the polymerase rebinds and completes it. With a copying
time β(1+lδ)+αl for a product of length l, where δ is the mean number of dissociations per nucleotide added,
α the time per nucleotide and β the length-independent time, the copying time stays affine in l, on average
along the template, so that dissociation enters only through b = 1/[1 + L(δ + α/β)]. A polymerase that adds
the nucleotide at position i before releasing its product with probability Pi , its processivity coefficient, has
δ equal to the mean of (1 − Pi )/Pi , at least (1 − P̄)/P̄ for the mean P̄, hence b ≤ 1/[1 + L(1 − P̄)/P̄]. The
ratio of copying times T (L)/T (L′ ) is the template advantage θ′ under mass action, each replicase–template
pair copying at a rate set by the copying time; if replicases are saturated by templates, a shorter copying time
raises fecundity instead, and θ′ is set by binding. A true termination ends the copy and releases its product,
which is then lost or copied as a truncated molecule; with a probability m per nucleotide, τ = 1 − (1 − m)L .
In the protocell variant of Fig. 7A, which copies as the lattice does, a product shorter than 10 nucleotides
is lost, copies of truncated templates stop with the same probability m per nucleotide (retruncation), and a
copy that stops early ends sooner: a product of relative length ξ is made at a rate multiplied by θ′ (ξ). Exact
kernels with unfinished copies, the classes used for a distribution of truncated lengths and the population
Monte Carlo over every truncated length (points of Fig. 7A) are described in Appendices S8–S9.

5.8

Comparison with the lattice

The lattice model of Tupper and Higgs 5 , its threshold read on their published figure, and an independent
reimplementation are described in Appendix S10. If its threshold grows with b, the reimplementation recovers half of the damage between b = 0.10 and 0.15 with runs to t = 120 and to t = 500, each bound
resting on a single run (between 0.05 and 0.25, or 0.45 at t = 500, at worst with one run more or fewer),
and between 0.05 and 0.15 at t = 120 with the 5% survival criterion of the published lattice (Appendix S10).
At infinite fecundity, protocells that copy as the lattice does tolerate more termination than the lattice only

19


[page 20]
below about 300 molecules at b = 0 and 30 at b = 0.15–0.25, and at every size beyond b ≈ 0.53, where the
large-protocell limit of their threshold, derived for the limit kernel (Appendix S9), exceeds that of the lattice.
At finite fecundity they do so only below a finite size: at R = 25, the copying rate kpol of the lattice, about
20 to 33 molecules for b = 0.3 to 0.6 and 230 at b = 1; at R = 3, protocells of 20 molecules tolerate less
termination than the lattice at every b computed (0.3 to 1). These levels compare only as orders of magnitude
(Appendix S9). Round-18 adds a nucleotide before releasing its product with a probability that varies about
twentyfold with the position on the template, up to 0.9 (ref. 46), which for a 100-nucleotide replicase gives
b ≤ 0.083 by the bound above, and b ≤ 0.0033 if that probability were 0.25 all along the template, its value
at the position where its rate constants were bounded. For a tC9Y-type polymerase 47 , b is not anchored by
any measurement.

5.9

Measured systems

The load is U = ℓIε with ℓ = 0.56 (0.51–0.60; central value with the tolerated base pairs placed at random)
and I = 53.2 bits, both computed from the tolerance of each site of QT45 measured by Gianni et al. 10
(Appendix S6). I is − log2 of the abundance of QT ribozyme folds in random sequence, 9.5 × 10−17 ; a
substitution counts as lethal when it lowers activity below 80% of the wild type, their criterion (0.51–0.60
from the site tolerances alone, 0.56–0.59 with the double mutants). Applying each error rate to a 53-bit
replicase is a normalization: the other polymerases are longer, and their information content is unknown.
Most published error rates are measured on full-length products; a copy stalled by a mismatch 48,49 does not
appear among them, so that U computed from them is the load of complete parasites, and the cost of stalling
appears in the measured fecundity. Fecundity is R = Y t1/2 /(T ln 2) for a yield Y of complete copies per
template after a reaction time T , and a template half-life t1/2 , assuming synthesis linear in time. In the model,
R is the number of copies a replicase starts per lifetime, all of which complete; if catalysts and templates
have the same lifetime and are drawn from one population, it equals the number of complete copies made
per template lifetime. In the experiments the catalyst is often in excess over the template, so that fecundity
per replicase is lower, by up to that excess. The fraction of copying slots that end in a complete copy is
σ = Ytc /T , with tc the time needed to make one copy of the object (given, or bounded, in Table S4 for each
system for which σ is reported); it involves no lifetime. The fragment of the TPR grows by up to a factor of
1.26 per cycle, which bounds its fecundity from below. The fidelity targets of the scaling limit agree with the
exact kernel at n = 50 to within 7 × 10−4 . Values, sources, conversions and caveats are given in Appendix S6.

5.10

Status of the results

The limit max(0, ln(2/θ)) is proved for the limit kernel and, as the limit of the exact thresholds, for every θ.
The bound un + max(0, ln(1/θ)) is proved at every size and fecundity. The well-mixed limit at fixed fecundity
is derived in mean field only. For the variants that exceed the ceiling (Table 1), the bound of the lever, the
absence of a threshold for χ ≥ 1 and for self-copying at infinite fecundity, the invariance of the invasion
threshold under fusion between protocells and the fact that no fusion raises it above the ceiling are proved
(Appendix S12); the other results on them are proved, derived or numerical as stated in Appendices S2 and
S5. The three identities for unfinished copies are exact, Theorem 2 extends to them, for a stop probability
per nucleotide at θ = 1 and, for one per copy, whenever θ′ ≥ min(θ, 1) (Appendix S8); with incomplete
copies of several kinds, lim inf n mc (n) ≥ m∞ and, without inert strands, the ceiling, its total-load form when

20


[page 21]
all become parasites and the bracket at R = ∞ by the extreme classes are proved, and a stationary bath’s
threshold is conjectural (Appendices S8, S9); the large-protocell limit of the threshold with retruncation
beyond b = 4/9 is derived for the limit kernel, its identification with the limit of the exact thresholds being
conjectural; everything else about them is numerical, for protocells of at most 80 molecules (160 with one
class at finite fecundity, 320 with every length or at b = 1) and, through limit kernels, for n = ∞, except the
decrease of the threshold to zero at finite fecundity, derived in mean field at b = 1. The scaling law in n/R
is proved for R > n (Appendices S3, S13); for R ≤ n the finite kernels are proved to converge to those of a
limit process wherever max(q, q/θ) ≤ 1, a range that contains the thresholds, and Appendix S3 reduces the
law to one property of that process, proved, computer-assisted, for n/R ≤ 2.875 and supported numerically
beyond, without which the thresholds are only bracketed asymptotically. For R ≤ n/5 the threshold is at
most max(0, ln(1/θ)) + ln(1024/725), less than half of the bonus above max(0, ln(1/θ)), at every size (proved,
computer-assisted; Appendix S3); for θ ≤ 1, large protocells keep more than half at every fixed n/R ≤ 2.858
and less than half at every fixed n/R ≥ 3.2 (proved, computer-assisted; Appendix S3). Eq. 3 also assumes that
ψ decreases with y, which is certified only on the grid y = k/20 < 1 (Appendix S3). Copying is instantaneous,
its duration being absorbed into R, and all molecules decay at the same rate; template advantages are derived
from copying times, which assumes mass action. If fewer substitutions are fully inactivating than those
counted as lethal, the loads are lower; other compositions of sites would allow ℓ = 0.5–1.1, a factor of 2.2
on the load, and published fidelities of a given polymerase differ by a factor of up to 4.4 in error rate. The
threshold of the reimplemented lattice depends on the length of its runs and, at t = 120, perhaps on its size
(Appendix S10).

Use of AI tools
[Draft, to be confirmed or rewritten by the author, who alone can state what he did himself and how the tools
were used; keep the bracketed items only if they apply. The author’s own statement, relayed on 4 October:
the ideas and the direction of the research are his; the proofs and the simulations were made by the AI. That
statement and the bracketed items below overlap: model variants, a scaling law, mechanisms, an interpretation and conclusions are ideas. Keep for each the attribution that is accurate; where the programme’s notes
record one, it must agree with them, since they may be deposited; they record, for example, that the bath of
slow truncated copies (Unfinished copies; Appendix S9) was proposed, as an unproven reading, by an AI
session whose computations showed where the mechanism the author first proposed fails, and established by
another at his request, after he had noted that this mechanism failed in half of the cases; and that the results
added to Appendices S2 and S3 on 7 October (the bound at every fecundity, the spectrum at θ = 1, the limit
for θ > 1 and the reduction of the scaling law) were obtained by AI sessions at his request of 6 October
(proved, except the reduction of the scaling law, which was then derived), the argument for θ > 1 following
a repair proposed by one of the sessions that checked it. The results added on 12 October (the ceiling for any
division that ignores which molecules are replicases, with complementary strands; the bracket on the price;
the convergence of the kernels at every y; (H3) at every y; and the bracket without (H2)) were obtained by
AI sessions at his requests of 7 October; the lever, spontaneous replication, partial self-copying and protocell
fusion (Appendices S2 and S5; Figs. 9–12), added for v0.16, were obtained by AI sessions at his requests
of 12 October, the ideas and the direction being his (for the lever, the law itself) and the exact statements,
the proofs and the computations the AI’s; [the bound for R ≤ n/5 (Appendix S3; report of 7 October), the
comparison with the model of Shah et al. 16 (Appendix S5; his request of 12 October) and the proposal
21


[page 22]
for measuring R (Appendix S6) were also obtained by AI sessions, as were the certified bounds on ψ (Appendix S3), transient compartmentalization and complementary strands at finite fecundity (Appendix S5; his
requests and agreement of 12 October), and the frontier of half the bonus, the pair density at finite size, the
upper bounds on Rmin , the bounds for y ≥ 1 and the extinction bound (Appendix S3; 12 October), and hypothesis (H2) on most of [1, 3] (Appendix S3; 12–13 October);] [Theorem 4 for R > n and its proof (the size
clock, the uniform drift and the convergence of the kernels for R > n; Appendix S13, at his requests of 6 and
7 October, written in English for this version), the slope of ψ (Theorem S, Appendix S14), the necessary price
(Theorem Q, Appendix S3), the results on incomplete copies and baths of several lengths (Appendices S8
and S9), Fig. 5 and the literature on self-copying (Appendix S5) were obtained by AI sessions of the lineage
“fusion” (requests and dates to be stated by the author);] Fig. 1, the title, the summary and the one-sentence
thesis of the Discussion were proposed by an AI session and chosen by him on 6 October (on 12 October AI
sessions kept “established” in the summary in place of his “computed” and, for v0.18.2, replaced “known to
copy itself” by “that has copied its own sequence” and “has not been established” by “remains unknown”,
removed “we conjecture” once the scaling law was proved for R > n, and, for v0.16, added “as computed”
and “for a sterile lone replicase”); on 12 October AI sessions worked autonomously, with his authorization,
and made the remaining choices of this version; for v0.19.3, the texts on (H2) proposed by the session that
obtained it were chosen and completed by an AI session on 31 October.] [The research questions and the
direction of the research are the author’s.] This work was carried out with extensive use of AI systems
(Claude, Anthropic[; model versions]). They wrote and ran the simulation and analysis code, devised and
wrote the proofs, [proposed the model variants, the scaling law, the mechanism of catalyst–template pairs
and that of the bath of slow truncated copies, proposed the interpretation of the results and the conclusions,
searched the literature and chose the references,] extracted the experimental data from the literature, checked
the references against primary sources where these could be accessed, and drafted and revised the text. The
independent implementations and checks mentioned in the Methods and the Results were written and run in
separate sessions of the same AI system, not by the sessions whose results they checked. [What the author
did himself: . . . ] The author takes full responsibility for the content.

Data availability
The thresholds, figure data and the logs of every computation, and the notes that give the full proofs and
computations of Appendices S2, S3 and S5 (listed in Appendix S7), will be deposited with the code on
publication (Code availability) and are available to the editors and referees on request. The lattice runs of
the reimplementation will be deposited with its simulation code, the definitions of its series and the output
of each point (Appendix S7). [to be confirmed by the author; or deposit before submission and give the
repository and DOI]

Code availability
All thresholds, figures and tables are produced by Python scripts (NumPy, SciPy), and the lattice runs by a
program in C; the scripts, with their logs and outputs and the notes that give the full proofs of Appendices S2,
S3 and S5 (Appendix S7), will be deposited in a public repository on publication (Appendix S7) and are
available to the editors and referees on request. [to be confirmed by the author; or deposit before submission
and give the repository and DOI]

22


[page 23]
Declarations
Acknowledgements
[to be completed by the author]

Author contributions
[L.C. conceived the study and directed the work.] The AI systems described in Methods (Use of AI tools)
carried out the analysis, the computations and the proofs[, proposed the model variants, the scaling law, the
mechanisms, the interpretation and the conclusions, searched the literature and chose the references] and
drafted the paper. [What L.C. did himself: . . . ] [Draft, to be confirmed by the author; it must agree with
Use of AI tools item by item, including the author’s statement on the ideas, and state L.C.’s own contribution
under the authorship criteria of Nature Portfolio.]

Competing interests
The author declares no competing interests. [draft, to be confirmed by the author]

Additional information
Correspondence and requests for materials should be addressed to L.C.

References
[1] P. G. Higgs and N. Lehman. The RNA World: molecular cooperation at the origins of life. Nat. Rev.
Genet., 16:7–17, 2015.
[2] F. Wachowius, J. Attwater, and P. Holliger. Nucleic acids: function and potential for abiogenesis. Q.
Rev. Biophys., 50:e4, 2017.
[3] J. Maynard Smith. Hypercycles and the origin of life. Nature, 280:445–446, 1979.
[4] B. Obermayer and E. Frey. Error thresholds for self- and cross-specific enzymatic replication. J. Theor.
Biol., 267:653–662, 2010.
[5] A. S. Tupper and P. G. Higgs. Error thresholds for RNA replication in the presence of both point
mutations and premature termination errors. J. Theor. Biol., 428:34–42, 2017.
[6] U. Niesert, D. Harnasch, and C. Bresch. Origin of life between Scylla and Charybdis. J. Mol. Evol., 17:
348–353, 1981.
[7] E. Szathmáry and L. Demeter. Group selection of early replicators and the origin of life. J. Theor. Biol.,
128:463–486, 1987.
[8] S. Matsumura, Á. Kun, M. Ryckelynck, F. Coldren, A. Szilágyi, F. Jossinet, C. Rick, P. Nghe, E. Szathmáry, and A. D. Griffiths. Transient compartmentalization of RNA replicators prevents extinction due
to parasites. Science, 354:1293–1296, 2016.

23


[page 24]
[9] M. Eigen. Selforganization of matter and the evolution of biological macromolecules. Naturwissenschaften, 58:465–523, 1971.
[10] E. Gianni, S. L. Y. Kwok, C. J. K. Wan, K. Goeij, B. E. Clifton, E. S. Colizzi, J. Attwater, and P. Holliger.
A small polymerase ribozyme that can synthesize itself and its complementary strand. Science, 391:
1022–1028, 2026.
[11] Á. Kun, M. Santos, and E. Szathmáry. Real ribozymes suggest a relaxed error threshold. Nat. Genet.,
37:1008–1011, 2005.
[12] A. Szilágyi, Á. Kun, and E. Szathmáry. Local neutral networks help maintain inaccurately replicating
ribozymes. PLoS One, 9:e109987, 2014.
[13] Á. Kun, A. Szilágyi, B. Könnyű, G. Boza, I. Zachar, and E. Szathmáry. The dynamics of the RNA
world: insights and challenges. Ann. N. Y. Acad. Sci., 1341:75–95, 2015.
[14] Á. Kun. Maintenance of genetic information in the first ribocell. In S. Müller, B. Masquida, and W. Winkler, editors, Ribozymes: Principles, Methods, Applications, chapter 14. Wiley-VCH, Weinheim, 2021.
doi: 10.1002/9783527814527.ch14.
[15] G. Bianconi, K. Zhao, I. A. Chen, and M. A. Nowak. Selection for replicases in protocells. PLoS
Comput. Biol., 9:e1003051, 2013.
[16] V. Shah, J. de Bouter, Q. Pauli, A. S. Tupper, and P. G. Higgs. Survival of RNA replicators is much
easier in protocells than in surface-based, spatial systems. Life, 9:65, 2019.
[17] G. Laurent, L. Peliti, and D. Lacoste. Survival of self-replicating molecules under transient compartmentalization with natural selection. Life, 9:78, 2019.
[18] A. Blokhuis, P. Nghe, L. Peliti, and D. Lacoste. The generality of transient compartmentalization and
its associated error thresholds. J. Theor. Biol., 487:110110, 2020.
[19] D. A. M. M. Silvestre and J. F. Fontanari. Package models and the information crisis of prebiotic
evolution. J. Theor. Biol., 252:326–337, 2008.
[20] L. Demetrius, P. Schuster, and K. Sigmund. Polynucleotide evolution and branching processes. Bull.
Math. Biol., 47:239–262, 1985.
[21] M. Paczkó, E. Szathmáry, and A. Szilágyi. Stochastic parabolic growth promotes coexistence and a
relaxed error threshold in RNA-like replicator populations. eLife, 13:RP93208, 2024.
[22] C. S. Wylie and E. I. Shakhnovich. Mutation induced extinction in finite populations: lethal mutagenesis and lethal isolation. PLoS Comput. Biol., 8:e1002609, 2012.
[23] J. J. Bull and C. O. Wilke. Lethal mutagenesis of bacteria. Genetics, 180:1061–1070, 2008.
[24] M. H. A. Davis. Piecewise-deterministic Markov processes: a general class of non-diffusion stochastic
models. J. R. Stat. Soc. B, 46:353–388, 1984.
[25] N. Takeuchi and P. Hogeweg. Multilevel selection in models of prebiotic evolution II: a direct comparison of compartmentalization and spatial self-organization. PLoS Comput. Biol., 5:e1000542, 2009.
24


[page 25]
[26] J. W. Szostak. Functional information: Molecular messages. Nature, 423:689, 2003.
[27] D. P. Horning and G. F. Joyce. Amplification of RNA by an RNA polymerase ribozyme. Proc. Natl.
Acad. Sci. U.S.A., 113:9786–9791, 2016.
[28] K. F. Tjhung, M. N. Shokhirev, D. P. Horning, and G. F. Joyce. An RNA polymerase ribozyme that
synthesizes its own ancestor. Proc. Natl. Acad. Sci. U.S.A., 117:2906–2913, 2020.
[29] X. Portillo, Y. T. Huang, R. R. Breaker, D. P. Horning, and G. F. Joyce. Witnessing the structural
evolution of an RNA enzyme. eLife, 10:e71557, 2021.
[30] N. Papastavrou, D. P. Horning, and G. F. Joyce. RNA-catalyzed evolution of catalytic RNA. Proc. Natl.
Acad. Sci. U.S.A., 121:e2321592121, 2024.
[31] J. Attwater, T. L. Augustin, J. F. Curran, S. L. Y. Kwok, L. Ohlendorf, E. Gianni, and P. Holliger.
Trinucleotide substrates under pH–freeze–thaw cycles enable open-ended exponential RNA replication
by a polymerase ribozyme. Nat. Chem., 17:1129–1137, 2025.
[32] A. Wochner, J. Attwater, A. Coulson, and P. Holliger. Ribozyme-catalyzed transcription of an active
ribozyme. Science, 332:209–212, 2011.
[33] J. Attwater, A. Raguram, A. S. Morgunov, E. Gianni, and P. Holliger. Ribozyme-catalysed RNA synthesis using triplet building blocks. eLife, 7:e35255, 2018.
[34] J. J. Bull, L. A. Meyers, and M. Lachmann. Quasispecies made simple. PLoS Comput. Biol., 1:e61,
2005.
[35] P. Hogeweg and N. Takeuchi. Multilevel selection in models of prebiotic evolution: compartments and
spatial self-organization. Orig. Life Evol. Biosph., 33:375–403, 2003.
[36] N. Takeuchi and P. Hogeweg. Evolutionary dynamics of RNA-like replicator systems: a bioinformatic
approach to the origin of life. Phys. Life Rev., 9:219–263, 2012.
[37] P. Szabó, I. Scheuring, T. Czárán, and E. Szathmáry. In silico simulations reveal that replicators with
limited dispersal evolve towards higher efficiency and fidelity. Nature, 420:340–343, 2002.
[38] Y. E. Kim and P. G. Higgs. Co-operation between polymerases and nucleotide synthetases in the RNA
world. PLoS Comput. Biol., 12:e1005161, 2016.
[39] N. Takeuchi and P. Hogeweg. The role of complex formation and deleterious mutations for the stability
of RNA-like replicator systems. J. Mol. Evol., 65:668–686, 2007.
[40] C. Jeancolas, C. Malaterre, and P. Nghe. Thresholds in origin of life scenarios. iScience, 23:101756,
2020.
[41] D. R. Mills, R. L. Peterson, and S. Spiegelman. An extracellular Darwinian experiment with a selfduplicating nucleic acid molecule. Proc. Natl. Acad. Sci. U.S.A., 58:217–224, 1967.
[42] P. Jagers. Branching Processes with Biological Applications. Wiley, London, 1975.
[43] D. Vere-Jones. Ergodic properties of nonnegative matrices. I. Pacific J. Math., 22:361–386, 1967.
25


[page 26]
[44] E. Seneta. Non-negative Matrices and Markov Chains. Springer, New York, 2006. Revised printing.
[45] N. Takeuchi, N. Mitarai, and K. Kaneko. A scaling law of multilevel evolution: how the balance
between within- and among-collective evolution is determined. Genetics, 220:iyab182, 2022.
[46] M. S. Lawrence and D. P. Bartel. Processivity of ribozyme-catalyzed RNA polymerization. Biochemistry, 42:8748–8755, 2003.
[47] J. Attwater, A. Wochner, and P. Holliger. In-ice evolution of RNA polymerase ribozyme activity. Nat.
Chem., 5:1011–1018, 2013.
[48] S. Rajamani, J. K. Ichida, T. Antal, D. A. Treco, K. Leu, M. A. Nowak, J. W. Szostak, and I. A. Chen.
Effect of stalling after mismatches on the error catastrophe in nonenzymatic nucleic acid replication. J.
Am. Chem. Soc., 132:5880–5885, 2010.
[49] K. Leu, E. Kervio, B. Obermayer, R. M. Turk-MacLeod, C. Yuan, J. M. Luevano, E. Chen, U. Gerland,
C. Richert, and I. A. Chen. Cascade of reduced speed and accuracy after errors in enzyme-free copying
of nucleic acid sequences. J. Am. Chem. Soc., 135:354–366, 2013.
[50] N. Paul and G. F. Joyce. A self-replicating ligase ribozyme. Proc. Natl. Acad. Sci. U.S.A., 99:12733–
12740, 2002.
[51] J. A. Doudna, S. Couture, and J. W. Szostak. A multisubunit ribozyme that is a catalyst of and template
for complementary strand RNA synthesis. Science, 251:1605–1608, 1991.
[52] R. Green and J. W. Szostak. Selection of a ribozyme that functions as a superior template in a selfcopying reaction. Science, 258:1910–1915, 1992.
[53] S. H. A. von der Dunk, E. S. Colizzi, and P. Hogeweg. Evolutionary conflict leads to innovation:
symmetry breaking in a spatial model of RNA-like replicators. Life, 7:43, 2017.
[54] E. Gianni, S. L. Y. Kwok, C. J. K. Wan, K. Goeij, B. E. Clifton, J. Attwater, and P. Holliger. A
polymerase ribozyme that can synthesize both itself and its complementary strand. bioRxiv, 2024. doi:
10.1101/2024.10.11.617851. Preprint, version posted 12 October 2024.
[55] Y. Li and R. R. Breaker. Kinetics of RNA degradation by specific base catalysis of transesterification
involving the 2′ -hydroxyl group. J. Am. Chem. Soc., 121:5364–5372, 1999.
[56] H. K. Wayment-Steele, D. S. Kim, C. A. Choe, J. J. Nicol, R. Wellington-Oguri, A. M. Watkins, R. A.
Parra Sperberg, P. S. Huang, Eterna Participants, and R. Das. Theoretical basis for stabilizing messenger
RNA through secondary structure design. Nucleic Acids Res., 49:10604–10617, 2021.
[57] R. N. Goldberg, N. Kishore, and R. M. Lennen. Thermodynamic quantities for the ionization reactions
of buffers. J. Phys. Chem. Ref. Data, 31:231–370, 2002.
[58] H.-O. Georgii and E. Baake. Supercritical multitype branching processes: the ancestral types of typical
individuals. Adv. Appl. Probab., 35:1090–1110, 2003.

26


[page 27]
Appendices
Status labels used throughout: proved (a complete argument is given, here or, where so stated, in the notes
deposited with the code, S7, the argument being outlined here), proved, computer-assisted (a proof part
of which is a computation in interval arithmetic or with a priori rounding-error bounds, deposited with the
code, S7), derived (a formal argument, not a proof), numerical (exact kernels, with the stated precision),
conjectured.

S1. The limit kernel (Theorem 1)
Notation. ν = F − 1, P = N − F, growth from n to S = kn molecules, then partition into k daughters, each
molecule going to each daughter with probability 1/k. A protocell is alive if F ≥ 2. The kernel of Eq. 1 is
p = qν/(ν + θP).
Fictitious clock (proved).

Consider the continuous-time process in which each of the ν replicase templates

is copied at rate 1, the copy being a replicase with probability q and a parasite otherwise, and each parasite
is copied at rate θ. The next event produces a replicase with probability qν/(ν + θP): the jump chain of this
process is exactly the model. Division happens at the stopping time T = inf{t : N(t) = S }. In this clock ν(t)
is a Yule process of rate q that does not depend on P.
Pairs (proved).

The generator of the Yule process applied to f (ν) = ν(ν + 1) gives qν[(ν + 1)(ν + 2) − ν(ν +

1)] = 2q f (ν). Hence E[ν(t)(ν(t) + 1)] = ν0 (ν0 + 1)e2qt , and since ν(ν + 1) = F(F − 1), the number of ordered
(catalyst, template) pairs of replicases grows at rate 2q, twice the rate of replicases.
Partition (proved, every n). Under independent uniform assignment into k daughters, the second factorial
P
moment of the binomial gives E[ d Fd (Fd − 1)] = k F(F − 1)/k2 = F(F − 1)/k. Since F(F − 1) = 0 for
F ∈ {0, 1}, the restriction to living daughters is automatic.
Limit kernel (proved). At fixed F and n → ∞, P ≃ N is a Yule process of rate θ started from about n
molecules, so that T → (ln k)/θ in probability, with a dependence on the path of ν of order ν/n. The limit
kernel B∞ is: partition, then a Yule process of rate q for ν during (ln k)/θ. With h = F(F − 1),
B∞ h = k2q/θ ·

1
· h = k2q/θ−1 h.
k

Numerically, the relation holds to 10−10 for k = 2 (λ = q/θ = 0.3, 0.5, 0.8) and to eight decimals for k = 3
(λ = 0.5, 0.7).
Identification of the spectral radius (proved).

A positive eigenfunction of an infinite non-negative matrix

need not give its spectral radius; it does if the h-transformed chain Ph (F, F ′ ) = B∞ (F, F ′ )h(F ′ )/(ρh(F)) is
positive recurrent 43,44 . Write a = kλ , the growth factor of ν over a cycle. The third factorial moment of the
P
Yule process gives E[F ′ h(F ′ ) | Fd ] = Fd (Fd − 1)[(Fd + 1)a3 − a2 ], and the binomial partition E[ d Fd (Fd −
1)(Fd + 1)] = F(F − 1)[(F − 2)/k2 + 3/k]; with ρh(F) = (a2 /k)F(F − 1) the drift of Ph is
Eh [F ′ | F] = kλ−1 F + (3 − 2/k) kλ − 1,
27


[page 28]
that is 2λ−1 F + 2λ+1 − 1 for k = 2 (checked numerically to 3 × 10−14 for k = 2, 3 and 4). For λ < 1, kλ−1 < 1
and Eh [F ′ ] − F < −1 for all large F (F > 9.66 at k = 2, λ = 12 ). The chain is irreducible and aperiodic,
so Foster’s criterion gives positive recurrence, and k2λ−1 is the spectral radius of B∞ . Truncations of B∞
converge to 22λ−1 for λ = 0.3, 0.5, 0.8 and 0.95 (k = 2). For λ > 1 the identification fails, as it must: k2λ−1
would exceed k, the largest possible mean number of daughters (at λ = 1.2 and k = 2, truncations give 1.741,
not 21.4 = 2.64). The threshold lies at λ = 21 , inside the range of validity: k2q/θ−1 = 1, that is q = θ/2 and
Uc = ln(2/θ), for every k; if θ ≥ 2, λ < 12 for every q < 1, so that ρ(B∞ ) < 1 and Uc = 0.
Left eigenvector and stable distribution (proved, k = 2). Index protocells by their number of replicases
at birth, F ≥ 2, and let p = 2−λ , γ = (1 − p)/p = 2λ − 1. Over a cycle ν = F − 1 becomes negative binomial,
E[zν ] = g(z)ν with g(z) = pz/(1 − (1 − p)z), and the two daughters of a protocell born with F replicases have
′

the generating function ΦF (z) = (1 + z) µ(z)F−1 with µ(z) = g((1 + z)/2) = p(1 + z)/(1 + p − (1 − p)z). Then
X

γ F−2 ΦF (z) =

F≥2
′

(1 + z) µ
(1 + z)2
=
,
1 − γµ
2(1 − γz)

′

′

whose coefficient of zF for F ′ ≥ 2 is 12 (1 + γ)2 γ F −2 = 22λ−1 γ F −2 : v(F) = γ F−2 is a left eigenvector of the
kernel on types at birth, with the eigenvalue 22λ−1 (the coefficients of z0 and z1 are dead daughters). Since
P
h = F(F − 1) is a right eigenvector with the same eigenvalue and F v(F)h(F) = 2/(1 − γ)3 < ∞, the
h-transformed chain has a summable invariant measure and is positive recurrent, which gives a second proof
of the identification. The stable type distribution is therefore explicit: at birth, F − 2 is geometric with ratio
γ; at division, the generating function pz2 /(1 − 2(1 − p)z) makes F − 2 geometric with ratio 2 − 21−λ . At
√
threshold (λ = 12 ) a protocell divides with 2 + 2 ≈ 3.41 replicases on average, and with at most ten with
√
probability 1 − (2 − 2)9 = 0.9919. (Checked numerically on truncations to F ≤ 120: vB/v equals 22λ−1 to
2 × 10−8 at λ = 0.5 and 0.7.)
Self-copying variant (proved for q < θ). If a replicase may choose itself as template, p = qF/(F + θP),
a protocell is alive if F ≥ 1, F itself is a Yule process of rate q in the fictitious clock, and h = F satisfies
B∞ h = kλ h. The same computation gives Eh [F ′ | F] = kλ−1 F + (2 − 1/k) kλ − 1 (checked to 5 × 10−14 ), so
that for λ < 1 the spectral radius is kq/θ > 1 whatever the load: there is no threshold. (For q ≥ θ even the
well-mixed pool maintains the replicase.)
Why protocells with few replicases carry the threshold (derived). At a macroscopic fraction x = F/N,
dx/d ln N = x[(q − θ) − x(1 − θ)]/[θ + x(1 − θ)]. At q = θ/2 this flow is negative on (0, 1] (for θ ≥ 1 because
q < 1, for θ < 1 because q < θ). States with x = O(1) are transient: they double at each cycle but drain
towards small F in O(log n) cycles and contribute only polynomial factors. The growth rate is that of the
quasi-stationary regime F = O(1), x ∼ 3/n. At threshold the mean number of replicases at division is ≈ 3.4
and 99% of protocells have F ≤ 10, for n = 20–200 and θ = 0.5–2, as the exact stable distribution of the
√
limit kernel predicts (2 + 2 and 0.9919, above). The right eigenvector tends to F(F − 1)/2 (within 4% on
F ≤ 10 at n = 200; exactly at θ = 1), and a first-order perturbation restricted to small F reproduces Uc (n):
1.37227 against 1.37230 (θ = 0.5, n = 200), 0.29255 against 0.29252 (θ = 1.5). The deterministic fixed
point x∗ = (q − θ)/(1 − θ) exists only for q > θ, far on the viable side, and plays no role at threshold.

28


[page 29]
S2. Bounds at every size and fecundity (Theorem 2), the limit (Theorem 3) and the spectrum
at θ = 1
Growth.

At each copy, E[∆(F(F − 1)) | F, N] = 2qF(F − 1)/W, with W = (F − 1) + θ(N − F) =

θ(N − 1) + (1 − θ)(F − 1). For ϕ = F(F − 1)/(N − 1), one copy gives
E[ϕ′ | F, N] = ϕ
Upper bound for every θ (proved).

N − 1
2q 
1+
.
N
W

If θ ≤ 1, then W ≥ θ(N − 1), and q ≤ θ/2 gives 2q/W ≤ 1/(N − 1).

If θ ≥ 1, then W ≥ (F − 1) + (N − F) = N − 1, and q ≤ 12 gives the same inequality. In both cases, for
q ≤ min(θ, 1)/2, E[ϕ′ ] ≤ ϕ: ϕ is a supermartingale during the whole growth phase, which has a fixed number
of steps at R = ∞.
Partition.

Given the size m of a daughter, F1 is hypergeometric and E[F1 (F1 − 1) | m] = F(F − 1) m(m −

1)/[2n(2n − 1)], so that E[ϕ1 | m] = F(F − 1) m/[2n(2n − 1)] for m ≥ 2 (a daughter of size one or zero carries
no pair). Summing over the two daughters and over m ∼ Bin(2n, 21 ),
hX i

F(F − 1)
E
ϕd =
2n − 4n 2−2n = (1 − 21−2n ) ϕmother ,
2n(2n − 1)
d
the only loss coming from daughters of size one. Combining with growth, the mean matrix K on division
states satisfies Kϕ ≤ (1 − 21−2n )ϕ with ϕ > 0 on living states, and the Collatz–Wielandt inequality gives
ρ ≤ 1 − 21−2n < 1 for every q ≤ min(θ, 1)/2. Since ρ is continuous in q, it stays below 1 on a neighbourhood
of q = min(θ, 1)/2, and the bounds on Uc are strict. Hence, for every n, Uc (n) < ln(2/θ) if θ ≤ 1 and
Uc (n) < ln 2 if θ ≥ 1, that is, Uc (n) < max(0, ln(1/θ)) + ln 2: at every size the protocell adds less than ln 2 to
the well-mixed threshold, without any assumption on the monotonicity of ρ in q. At θ = 1, W = N − 1 and ϕ
is a martingale at q = 21 : ρ( 12 ) = 1 − 21−2n exactly. With a hypergeometric partition (each daughter receives
exactly n molecules) there is no loss at division. At θ = 1, ϕ is then a strict supermartingale over a whole
cycle for q < 21 and a strict submartingale for q > 21 , so that the Collatz–Wielandt inequality, applied to the
finite matrix K in both directions, gives ρ < 1 and ρ > 1 respectively: the threshold is exactly ln 2 for every
n ≥ 2.
Lower bound for θ ≥ 1 (proved). Now W ≤ θ(N − 1). At q = (θ/2)(1 + η) each copy multiplies E[ϕ]
by at least 1 + η/N. The daughter that receives all molecules, with probability 21−2n , divides again at once
and gains nothing; it suffices that η > (2n − 1) 21−2n /(1 − 22−2n ) for Kϕ > ϕ on all living states, hence, with
Uc = sup{U : ρ(U) > 1}, Uc (n) ≥ ln(2/θ) − O(n4−n ) (the bound is empty when (θ/2)(1 + η) ≥ 1, that is for
θ close to 2 at small n). Averaging the gain over the size of the daughters tightens the correction to O(4−n ),
consistent with the gap at θ = 1, 21−2n / ln 2 to leading order (Table S1a).
Numerical check. On 42 cases (θ = 0.25–1.75, n = 2–40), ρ(q = θ/2) − (1 − 21−2n ) has the predicted sign
in every case: −0.067 at θ = 0.5, n = 20; at most 2.3 × 10−15 in absolute value at θ = 1; +0.041 at θ = 1.5,
n = 20. For θ > 1 at q = 21 , the certificate maxF (Kh)(F)/h(F) ≤ 1 − 21−2n holds with a strictly positive
margin in all 48 cases tested (θ = 1.25–10, n = 2–40; margin 0.0035 at θ = 1.25, n = 2, and 0.32 at θ = 10,

29


[page 30]
n = 40), and Uc (n) stays below ln 2 on a grid of 66 points with θ > 1 (θ = 1.1–5, n = 2–50), with a maximum
of 0.6464 (θ = 1.1, n = 4).
The limit (Theorem 3, proved). Let Kn be the mean matrix on division states F ∈ {2, . . . , 2n} and fix q
with θ/2 < q < min(θ, 1), so that λ = q/θ ∈ ( 12 , 1) and β = 22λ−1 > 1. We show that lim inf n ρ(Kn ) ≥ β.
(i) One cycle converges. Let the mother have F replicases. A daughter receives Fd ∼ Bin(F, 12 ) replicases
and, independently, Pd ∼ Bin(2n − F, 12 ) parasites. On the event Fd ≥ 2, run the fictitious clock from ν(0) =
Fd − 1, P(0) = Pd , beyond division if needed: ν is a Yule process of rate q; every parasite is copied at rate
θ; every failed copy of a replicase template adds a parasite. The daughter divides at Tn = inf{t : N(t) = 2n},
with F ′ = ν(Tn ) + 1. Write P = Pin + Pnew , where Pin counts the Pd initial parasites and their descendants,
a Yule process of rate θ, and Pnew the parasites made by failed copies and their descendants. Given Pd = y,
Pin (t) is a sum of y independent geometric variables of mean eθt , so Var[Pin (t)e−θt | y] ≤ y; since Pd /n → 1
in probability, Pin (t)/n → eθt in probability for every t. Failed copies arrive at rate (1 − q)ν(s) and each
founds a Yule family of rate θ, so E[Pnew (t)] ≤ (Fd − 1) t e(q+θ)t , and E[ν(t)] = (Fd − 1)eqt ; neither depends
on n. Hence N(t)/n = (ν(t) + 1 + Pin (t) + Pnew (t))/n → eθt in probability for every t. As N is non-decreasing,
{Tn < t∗ − δ} ⊂ {N(t∗ − δ) ≥ 2n} and {Tn > t∗ + δ} ⊂ {N(t∗ + δ) < 2n} with t∗ = (ln 2)/θ, and both events have
vanishing probability: Tn → t∗ in probability. Then


P ν(Tn ) , ν(t∗ ) ≤ P(|Tn − t∗ | > δ) + P ν jumps in [t∗ − δ, t∗ + δ] ,
and the last term is at most 2δq E[ν(t∗ + δ)], which tends to 0 with δ. On this coupling, for all fixed F, F ′ ≥ 2,

Kn (F, F ′ ) − B∞ (F, F ′ ) ≤ 2 P ν(Tn ) , ν(t∗ ) −→ 0,
since Kn (F, F ′ ) = 2 P(Fd ≥ 2, ν(Tn )+1 = F ′ ) and B∞ (F, F ′ ) = 2 P(Fd ≥ 2, ν(t∗ )+1 = F ′ ). No independence
between Tn and ν is needed.
(ii) Truncation. Let A(F0 ) denote the restriction of a matrix A to the states 2 ≤ F ≤ F0 . For a nonnegative matrix, the spectral radius of a principal submatrix is at most that of the matrix, so ρ(Kn ) ≥ ρ(Kn(F0 ) );
0)
for a finite matrix the spectral radius is continuous in the entries, so by (i) ρ(Kn(F0 ) ) → ρ(B(F
∞ ). Hence
0)
lim inf n ρ(Kn ) ≥ ρ(B(F
∞ ) for every F 0 .

(iii) The truncations reach β. All entries of B∞ on living states are positive (a daughter receives two
replicases with positive probability, and a Yule process from ν = 1 reaches every ν ≥ 1). For every

(F0 ) m
0) m
m
) ≥ (B(F
m, ρ(B∞
∞ ) (2, 2), which increases to B∞ (2, 2) as F 0 → ∞ by monotone convergence over
0)
m
1/m . On the other hand B h = βh with h > 0 (S1), and the
paths; hence limF0 ρ(B(F
∞
∞ ) ≥ supm B∞ (2, 2)

h-transformed chain

B∞ (F, F ′ ) h(F ′ )
β h(F)
P m
P
P m
m
is recurrent (Foster’s criterion, S1), so m B∞ (2, 2)β−m = m Pm
h (2, 2) = ∞. The power series m B∞ (2, 2)z
Ph (F, F ′ ) =

1/m ≥ β. Together, lim ρ(B(F0 ) ) ≥ β.
therefore diverges at z = 1/β, which gives lim supm Bm
F0
∞
∞ (2, 2)

(iv) Conclusion. By (ii) and (iii), lim inf n ρ(Kn ) ≥ β > 1, so Uc (n) ≥ − ln q for all n large enough. Letting
q ↓ θ/2 gives lim inf n Uc (n) ≥ ln(2/θ) for every θ < 2 (for θ ≥ 2, ln(2/θ) ≤ 0 ≤ Uc (n)). With the upper bound,
limn Uc (n) = ln(2/θ) for every θ ≤ 1; for θ > 1 the upper bound is proved below. Numerically, max |Kn − B∞ |
on F, F ′ ≤ 12 decreases as 1/n (n max |Kn − B∞ | = 1.06–1.15 for n = 10–400 at θ = 0.5, q = 0.30 and 0.35);

30


[page 31]
at θ = 0.5, q = 0.3, the spectral radii of the truncations of B∞ agree with β = 20.2 = 1.148698 to eight digits
from F0 = 80 on, and ρ(Kn ) rises from 0.984 (n = 10) to 1.1397 (n = 400); in simulations of the fictitious
clock, the mean division time is 1.378 at n = 300 against t∗ = 1.386, with a standard deviation decreasing as
n−1/2 .
First-order correction (derived). For θ ≤ 2, to first order in 1/n, Uc (n) = ln(2/θ) + ζ(θ)/n with ζ(θ) =
2(1 − 1/θ)/ ln 2; for 1 < θ ≤ 2 the expansion is around the limit proved below, and for θ > 2, where the
limit is 0, it does not apply. During growth, in the fictitious clock, N − 1 increases at rate θ per parasite but
at rate 1 per replicase template, so that a protocell with ν(s) replicase templates reaches 2n molecules later
RT
than T 0 = (ln 2)/θ by about (1 − 1/θ) 0 0 e−θs ν(s) ds/n, during which its pairs grow at rate 2q. Along the
h-transformed chain at threshold, ν + 2 is a Yule process of rate θ/2 and a daughter receives 1 + Bin(ν − 1, 12 )
RT
√
√
templates, so that the stationary mean of ν at birth is (2 2 − 1)/(2 − 2) and θ Eh [ 0 0 e−θs ν(s) ds] = 2
exactly; to first order, the Perron root is then 22q/θ−1 [1 + 2(1 − 1/θ)/n]. The other first-order terms (the −1 in
N − 1, the size of the daughter, its share of the pairs, the variance of the growth time) add no dependence on θ
at threshold to this order: at q = θ/2 each copy multiplies E[ϕ] by exactly 1 − cν/[N(N − 1 + cν)], c = 1/θ − 1
(Growth, above), so that ϕ departs from a martingale during growth only through ν, and division costs only
the fraction 21−2n . They therefore vanish, since at θ = 1 the identity ρ = 1 − 21−2n leaves no 1/n term.
Setting ρ = 1 gives ζ. The expansion is formal, but the exact thresholds confirm it: fitted on n = 400–800
and 100–400, ζ = −2.88 and +0.962 at θ = 0.5 and 1.5, against −2.885 and +0.962, and n (Uc − ln(2/θ)) at
n = 200 (Table S1b) lies within 0.09 of ζ(θ) for 0.5 ≤ θ ≤ 2, and within 0.02 for 0.75 ≤ θ ≤ 2. The sign of
ζ follows: when θ > 1 a protocell rich in replicases grows more slowly, which gives its pairs of replicases
more time to multiply before division.
Supermartingales at every fecundity (proved). For a > 0 let φa (F) = Γ(F − 1 + a)/Γ(F − 1), the
rising factorial (F − 1)F · · · (F + a − 2) for integer a, so that φ2 = h; let gb (N) = Γ(N − 1)/Γ(N − 1 + b),
Va,b (F, N) = φa (F) gb (N), with Va,b = 0 on dead states, and Λ = max(q, q/θ). Since W ≥ min(1, θ)(N − 1), a
copy is a new replicase with probability p ≤ Λ(F − 1)/(N − 1), and one copy changes Va,b in expectation by
pVa,b (F + 1, N + 1) + (1 − p)Va,b (F, N + 1) − Va,b (F, N) = Va,b

a(N − 1)p/(F − 1) − b
Λa − b
≤ Va,b
,
N−1+b
N−1+b

which is not positive for b ≥ Λa. With decay, since φa (F − 1)/φa (F) = (F − 2)/(F − 2 + a) and gb (N −
1)/gb (N) = (N − 2 + b)/(N − 2), the two kinds of loss change Va,b at the rate F[Va,b (F − 1, N − 1) − Va,b ] +
(N − F)[Va,b (F, N − 1) − Va,b ] = Va,b [N(b − ha ) + ha (2 − b)]/(N − 2) for N ≥ 3, with ha (F) = aF/(F − 2 + a),
and −2Va,b at F = N = 2; for a = 2, h2 = 2 and the rate is −(2 − b)V2,b , as for Z in S3. The numerator
increases with b; it is not positive if b ≤ 2 ≤ a, since then ha ≥ 2, nor if b ≤ a < 2, since its value at
b = a is a(2 − a)(F − N)/(F − 2 + a). Hence, during growth, Va,Λa is a supermartingale at R = ∞ for every
a, and at every fecundity if Λ ≤ 1 and Λa ≤ 2; stopped at division or death, which occurs almost surely,
gb (2n) E[φa ( f ′ )1{division}] ≤ Va,b of the initial state, where f ′ is the number of replicases at division.

31


[page 32]
Partition of rising factorials (proved). For integer a ≥ 2, b > 0 and a mother with f replicases, the first
daughter satisfies
!
a
X


a
E Va,b (F1 , N1 ) = gb (2n)
(a − 2)a− j ( f ) j α j (n, b),
j
j=2



α j (n, b) = E r j (N1 ) ,

where (x) j = x(x−1) · · · (x− j+1), N1 ∼ Bin(2n, 21 ), and r j (m) = (m) j gb (m)/[(2n) j gb (2n)] for m ≥ j, r j (m) =
0 otherwise: given N1 = m, F1 is hypergeometric (Partition, above) and E[(F1 ) j | m] = ( f ) j (m) j /(2n) j , and
P 
φa (x) = (x + a − 2)a = j aj (a − 2)a− j (x) j , the terms j = 0, 1 vanishing. α j increases with b; α j ≤ 1 for b ≤ 2,
since for j ≥ 2 ≥ b consecutive values of (m) j gb (m) have the ratio (m + 1)(m − 1)/[(m + 1 − j)(m − 1 + b)] ≥ 1,
so that r j ≤ 1; and α j (n, b) → 2b− j as n → ∞, since r j (m) ≃ (m/2n) j−b while daughters of fewer than n/2
molecules, on which r j is at most polynomial in n, are exponentially rare; in particular α j (n, b) is bounded in
n at fixed b. Let cn (Λ) = 2α2 (n, 2Λ): it increases strictly, from cn ( 12 ) = 1 − 21−2n to cn (1) = 2 − 2(2n + 1)4−n ,
and at R = ∞ and θ = 1 it is the spectral radius cn (q) (Spectrum at θ = 1, below).
A bound at every fecundity (proved). For every n ≥ 2, θ > 0, q ∈ (0, 1] and R ∈ (0, ∞], ρ(Kn ) ≤ cn (Λ).
For Λ ≤ 1, the supermartingale V2,2Λ = F(F − 1)Γ(N − 1)/Γ(N − 1 + 2Λ) in each daughter (the daughter that
receives all 2n molecules divides at once) and the partition formula with a = 2 give Kn h ≤ cn (Λ)h, and the
Collatz–Wielandt inequality gives the bound. For Λ ≥ 1, a daughter divides only if it receives at least two
replicases, so the row sums of Kn are at most 2P(Bin( f, 12 ) ≥ 2) ≤ cn (1) ≤ cn (Λ). The bound is attained at
θ = 1 and R = ∞ (below). With un the root of cn (e−u ) = 1, so that un = Uc (n, ∞, 1) (Table S1a), it follows
that
Uc (n, R, θ) ≤ un + max(0, ln(1/θ)) < ln 2 + max(0, ln(1/θ))
at every fecundity: the ceiling of Theorem 2 holds at every fecundity, with the size-dependent value un . At
Λ = 21 , V2,1 = ϕ and the bound is that of Theorem 2, ρ ≤ 1 − 21−2n .
Division blind to molecular identity (proved). Let the 2n molecules be distributed among any number
of daughters, of any sizes, possibly random, by a rule that does not distinguish replicases from parasites:
given the sizes, every assignment of the molecules to the daughters is equally likely. Division then does
not increase the pair density ϕ = F(F − 1)/(N − 1), summed over daughters, in expectation, and conserves
P
P
it exactly when no daughter receives a single molecule: E[ d ϕd ] = ϕ E[ Nd ≥2 Nd ]/N, with ϕd = 0 when
Nd ≤ 1. Since ϕ is a supermartingale during growth whenever max(q, q/θ) ≤ 21 , at every fecundity, the
spectral radius of the mean matrix K is then at most one, and Uc ≤ ln 2 + max(0, ln(1/θ)) at every size and
fecundity. The same bound holds with complementary strands, of which only the plus strand is catalytic
(each plus strand starting R copies per lifetime, every strand decaying at rate one), with ϕ computed on all
strands of the replicase and U the load per copy. At θ = 1 and infinite fecundity, ϕ is a martingale during
growth at q = 12 , a strict submartingale above and a strict supermartingale below, so that Uc = ln 2 exactly
at every size for every such rule that never produces a daughter with a single molecule and is not degenerate,
that is, gives some daughter between 2 and 2n − 1 molecules with positive probability. Binary binomial
partition falls short of ln 2 only through the pair density lost to daughters with a single molecule, which carry
on average a fraction 21−2n of the molecules. Within this model, exceeding the ceiling requires a division
rule that, for some composition, gives the daughters a larger expected summed pair density than the mother:
sorting the replicases into one daughter removes the threshold at infinite fecundity, and placing replicase
32


[page 33]
pairs in small daughters also raises it.
The lever: how far a division can raise the ceiling (proved).

Let a division rule, possibly random and

possibly sensitive to which molecules are replicases, give the daughters of a protocell that divides with f
P
replicases the replicase numbers Fd and the fractions αd of its molecules, and let M(λ) = sup f E[ d Fd (Fd −
1) α−2λ
starts at u = 2yαd , and the pair density Z = F(F − 1)u−2λ
d ]/( f ( f − 1)). In the limit process a daughter
Rτ
obeys E[Z(Xτ )1{division}] = Z(X0 ) − 2(1 − λ) E 0 Z dt over its cycle, from any starting size; hence Kϕ2 ( f ) =
P
E[ d ϕ2 (Fd )α−2λ
d ] − ℓ( f ) with ℓ ≥ 0, and Kϕ2 ≤ M(λ)ϕ2 , where K is the mean matrix on types at division.
If M(λ) ≤ 1, the Schur reduction of the kernel onto any finite set of types has spectral radius at most
one, without any assumption on large types, and the sum of ϕ2 over each generation is a non-negative
supermartingale with values in the even integers; it reaches zero almost surely if M(λ) < 1, or if y > 0
and, at every type, some daughter with at least two replicases receives less than the whole protocell with
positive probability, so that the population then dies out. Therefore λc (y) ≥ λ∗ = sup{λ < 1 : M(λ) ≤ 1} at
every y, and the compartment constant is at most ln(1/λ∗ ). For two equal daughters, λ∗ = min(1, 12 log2 (1/r̄))
P
with r̄ = sup f E[ d Fd (Fd − 1)]/( f ( f − 1)) ≤ 1, the expected fraction of ordered replicase pairs kept by
the two daughters together; random partition gives r̄ = 12 and the ceiling ln 2, and every rule that ignores
which molecules are replicases gives λ∗ = 21 . The weight α−2λ
is why a rule that places pairs in small
d
daughters can exceed ln 2 without keeping pairs together more often than a random partition into daughters
of the same sizes. At finite size and fecundity the same argument, with F(F − 1)Γ(N − 1)/Γ(N − 1 + 2Λ)
in place of the pair density ϕ (which is its case Λ = 12 ), gives ρ ≤ 1 whenever max(q, q/θ) ≤ Λ ≤ 1 and
P
max f E[ d Fd (Fd − 1) g(Nd )] ≤ f ( f − 1) g(2n), g(N) = Γ(N − 1)/Γ(N − 1 + 2Λ); with λ∗n the largest such
Λ, Uc ≤ max(0, ln(1/θ)) + ln(1/λ∗n ) at every size and fecundity. A bound on the factor by which division
P
multiplies E[ d ϕd ] alone gives nothing beyond ln 2 when daughters differ in size: sorting all replicases into a
daughter of 9 of 12 molecules multiplies it by at most 1.375, and remains supercritical at every load computed
at infinite fecundity (numerical). Partial sorting, which places all replicases in one daughter with probability
p and partitions at random otherwise, has r̄ = (1 + p)/2 for every f ; F(F − 1) is then an eigenfunction of
the kernel at y = 0 with eigenvalue 4λ r̄, large types drift down near λ∗ because (1 + 3p)2 < 2(1 + p)3 , and
λc (0) = λ∗ exactly. For y < 1, a lower bound on pair growth in the size clock gives λc (y) ≤ λ∗ + y(1 − λ∗ )
√
for small enough y, so that λ∗ ≤ λc (y) → λ∗ as y → 0: two bits, ln 4, require p = 2 − 1, and three bits
p = 23/4 − 1. The exact kernels agree: at θ = 1 and R = ∞, Uc = 1.389378 and 2.082498 at n = 160 for these
two values of p, against ln 4 = 1.386294 and ln 8 = 2.079442. The bound is not reached by mechanisms
whose gain is confined to protocells with few replicases: in the cases computed at y = 0, bound pairs, clusters
and budded vesicles that carry a pair gain only 9–45% of the extra bits that the bound allows, and budded
vesicles lose most of that gain already at y = 0.5 (numerical). The complete proofs are in Appendix S12.1
and in the notes deposited with the code (S7).
Spectrum at θ = 1 (proved).

At R = ∞ and θ = 1, including q = 1, the eigenvalues of Kn are µk =

2αk (n, kq), k = 2, . . . , 2n; the largest is µ2 = cn (q), and µk → 21−k(1−q) as n → ∞. At θ = 1, p =
q(F − 1)/(N − 1), so that the copy term above vanishes for b = qa: Va,qa is a martingale during growth for
P 
every a, and (Kn φa )( f ) = 2 aj=2 aj (a − 2)a− j α j (n, qa) ( f ) j . The ( f ) j , j = 2, . . . , 2n, form a basis of the
functions on {2, . . . , 2n} (a combination of them that vanishes there is a polynomial of degree at most 2n that
also vanishes at 0 and 1), and φa is ( f )a plus a combination of the ( f ) j with j < a; Kn is therefore triangular

33


[page 34]
in the basis φ2 , . . . , φ2n , with diagonal 2αa (n, qa). As φ2 = h > 0 is an eigenvector, µ2 is the spectral radius,
with no assumption of primitivity.
The limit for θ > 1 (Theorem 3, proved).

When θ > 1 the pair density bounds the threshold only by

ln 2, because W ≤ θ(N − 1) goes the wrong way at q between 21 and θ/2; the upper bound lim supn Uc (n) ≤
max(0, ln(2/θ)) follows from (a)–(c), assembled in (d). Convergence of the coefficients alone would not
suffice: at q = 1 they converge while ρ(Kn ) = cn (1) stays close to 2.
(a) ρ never decreases as q grows (R = ∞, every n). Let T (F, P) be the number of replicases at division
of a protocell that grows from F replicases and P parasites, N = F + P ≤ 2n, T N (F) the same from F
replicases among N molecules, and ≤st the stochastic order. (i) At fixed N, T N (F) increases with F, whatever
the copying probabilities: by backward induction on N, from F the next state is F + 1 or F at size N + 1,
both giving T ≤st T N+1 (F + 1), whereas from G > F both give T ≥st T N+1 (G) ≥st T N+1 (F + 1). (ii) Hence,
for N < 2n, T (F, P) ≤st T (F + 1, P), since T (F, P) mixes T (F + 1, P) and T (F, P + 1) ≤st T (F + 1, P);
T (F, P) ≤st T (F, P − 1), since T (F, P − 1) mixes T (F, P) and T (F + 1, P − 1) ≥st T (F, P); and T increases
when replicases are added or parasites removed. (iii) If q ≤ q′ , T at q is ≤st T at q′ , by backward induction,
since p increases with q and T (F + 1, P) ≥st T (F, P + 1). (iv) For f ≤ f ′ , couple the two partitions molecule
by molecule, the f replicases of the first mother being f of the f ′ of the second and each molecule going to
the same daughter: each daughter of the second mother has at least as many replicases and at most as many
parasites as the corresponding daughter of the first, and is alive if that one is. Hence, for every non-negative
function g that increases on types, Kn (q)g increases and Kn (q)g ≤ Kn (q′ )g; by induction Kn (q)m 1 ≤ Kn (q′ )m 1,
and Gelfand’s formula, ρ(K) = limm [max f (K m 1)( f )]1/m , gives ρ(Kn (q)) ≤ ρ(Kn (q′ )). The row sums of Kn
do not depend on q at R = ∞, and Kn (q) and Kn (q′ ) are not ordered entry by entry: what is monotone is the
type at division.
(b) Drift (R = ∞). Let Λ0 < 1 and a an integer above 1/(1 − Λ0 ). For every β ∈ (21−a(1−Λ0 ) , 1) there are
M, n0 and C such that, for n ≥ n0 and Λ ≤ Λ0 , (Kn φa )( f ) ≤ βφa ( f ) for f > M and (Kn φa+1 )( f ) ≤ Cφa+1 ( f )
P 
for every f . Indeed, by the supermartingale Va,Λa and the partition formula, (Kn φa )( f ) ≤ 2 j aj (a −
2)a− j α j (n, Λa)( f ) j ; the term j = a is at most 2αa (n, Λ0 a)φa ( f ), which tends to 21−a(1−Λ0 ) φa ( f ), and the
others are O( f j−a )φa ( f ) uniformly in n; the bound for φa+1 follows in the same way. By Fatou’s lemma, the
same bounds hold for B∞ .
(c) Schur reduction. Let K ≥ 0 be a finite matrix on A ⊔ B with ρ(KBB ) < 1, and S = KAA + KAB (I −
KBB )−1 KBA . Then ρ(K) − 1 and ρ(S ) − 1 have the same sign. If K is irreducible, S (t) = tKAA + t2 KAB (I −
tKBB )−1 KBA has a spectral radius that increases strictly with t on [0, 1/ρ(KBB )), and ρ(tK) = 1 if and only if
ρ(S (t)) = 1, positive eigenvectors corresponding through vB = (I−tKBB )−1 tKBA vA ; since 1/ρ(K) < 1/ρ(KBB ),
comparing 1/ρ(K) with 1 gives the claim. Otherwise the claim holds for each strongly connected component
C of K that meets A: a path through B between two types of C ∩ A stays in C, so that the restriction of
S to C ∩ A is the reduction of KC , and the strongly connected components of S are the non-empty C ∩ A;
components inside B have spectral radii at most ρ(KBB ) < 1, and ρ(K) and ρ(S ) are the largest spectral radii
of their components.
(d) Conclusion. Fix ε > 0 and the single point qε = min(1, θ/2)e−ε , so that − ln qε = max(0, ln(2/θ)) + ε,
λε = qε /θ < 21 and c = 22λε −1 < 1, while Λ = max(qε , λε ) < 1. Take a so large that 21−a(1−Λ) < c, then
β < c, M and n0 as in (b), with Λ0 = Λ, and let A = {2, . . . , M} and B the larger types. By (b), ρ(Kn,BB ) ≤ β
(Collatz–Wielandt with φa ), so that the reductions S n of Kn (qε ) onto A exist. As Kn (qε ) → B∞ entry by

34


[page 35]
entry ((i) of The limit, above, which holds for every q) and the weights φa ≤ φa+1 , with φa /φa+1 → 0, bound
the tails uniformly in n, S n converges to the reduction S ∞ of B∞ at λε ; its tail constants are explicit: with
w = φa , w′ = φa+1 and δL = supg>L w(g)/w′ (g), the paths through B of length k ≥ m contribute at most
2Cw′ (i)βm /(1 − β) to S n (i, j), and, for each k, those that leave { f ≤ L} at most 2δL w′ (i)(k + 1)C k+1 . For
t = 1/c, the equation x = tB∞,BB x + tB∞,BA hA has a single solution bounded by a multiple of φa , since
tB∞,BB φa ≤ tβφa with tβ < 1, and the eigenrelation B∞ h = ch (S1), with h ≤ φa , shows that hB is that
solution; hence S ∞ (t)hA = hA for S ∞ (t) = tB∞,AA + tB∞,AB (I − tB∞,BB )−1 tB∞,BA , and ρ(S ∞ (t)) = 1. As t > 1,
S ∞ ≤ S ∞ (t)/t entry by entry, hence ρ(S ∞ ) ≤ c < 1. Therefore ρ(S n ) < 1 for n large, ρ(Kn (qε )) < 1 by (c),
and ρ(Kn (q)) < 1 for every q ≤ qε by (a): Uc (n) ≤ max(0, ln(2/θ)) + ε for n large. With the lower bound (iv),
limn Uc (n) = max(0, ln(2/θ)). The same argument gives the limit for θ ≤ 1 without Theorem 2. Numerically,
at θ = 2 and ε = 0.03, ρn (qε ) = 1.000194 at n = 50 and 0.98261 at n = 320, and for θ ≥ 2 the thresholds
decrease as about 1/n (Table S1c).

S3. Finite fecundity
Exact identity at θ = 1 (proved). Let g(N) = Γ(N − 1)/Γ(N − 1 + 2q) and Z = F(F − 1) g(N), so that
g(N + 1)/g(N) = (N − 1)/(N − 1 + 2q). At θ = 1, W = N − 1. Copies occur at rate RF and give a replicase
with probability q(F − 1)/(N − 1); their contribution to the generator is
RF

h q(F − 1)

i
h

i
2q 
− g(N) = 0.
2F g(N + 1) + F(F − 1) g(N + 1) − g(N) = RF 2 (F − 1) g(N + 1) 1 +
N−1
N−1

Replicases die at total rate F and parasites at rate N − F; their contribution is




F(F − 1) (N − 2) g(N − 1) − N g(N) = F(F − 1) (N − 2 + 2q) − N g(N) = −2(1 − q) Z,
using (N − 2)g(N − 1) = (N − 2 + 2q)g(N), valid for N ≥ 3. Hence E[dZ | F, N] = −2(1 − q)Z dt for every
state with N ≥ 3, whatever R: between divisions the pair density decays at rate 2(1 − q) per lifetime. At
N = 2 the decay is faster (inequality). The identity was checked on 2 × 104 random states (relative error
below 3.5 × 10−8 ) and in exact rational arithmetic; it is false for θ , 1, as expected. At R = ∞ the copying
terms alone act, so Z is a martingale during growth and a division multiplies E[Z] by the R = ∞ spectral
radius cn (q); at q = 12 , Z = ϕ and cn ( 12 ) = 1 − 21−2n .
Replacement (proved). Maintenance requires R > eU in protocells of any size. New replicases appear at
rate RF p(F, N) ≤ RFq, since p ≤ q, and replicases decay at rate F; division conserves the total number of
replicases. The expected total number of replicases in the population therefore decays at least as e−(1−Rq)t
when Rq < 1.
Well-mixed limit at fixed R (derived in mean field). At a macroscopic replicase fraction x, ẋ = Rx2 (q −
ω)/ω with ω = x + θ(1 − x), and d ln N/dt = Rx − 1. For θ < 1, x converges to x∗ = (q − θ)/(1 − θ) and the
lineage grows at rate Rx∗ − 1, whence the threshold x∗ = 1/R, that is Eq. 2. Protocells with F = O(1) do
not escape it, heuristically: at fixed F, N saturates at RF and the resulting growth condition is the same. For
θ ≥ 1, x → 0 and Uc → 0. The convergence of the stochastic process to this mean-field limit is not proved;
√
numerically it is slow, the gap decreasing as ≈ 1.2/ n at θ = 0.5, R = 10 (0.823, 0.764, 0.721, 0.685, 0.657
at n = 20, 50, 100, 200, 400, against 0.598); at θ = 1.5, R = 10, nUc ≈ 2.
35


[page 36]
Limit process (derived; the finite kernels are proved to converge to its kernel).

With F = O(1) and N

of order R, set u = N/R. Then W = θN(1 + O(1/N)), parasites follow their mean to relative order N −1/2 ,
and the birth size is n(1 + O(n−1/2 )). In the limit n, R → ∞ at fixed y = n/R: u̇ = F − u; F → F + 1
at rate λF(F − 1)/u with λ = q/θ; F → F − 1 at rate F; division when u = 2y, each daughter receiving
Fd ∼ Bin(F, 21 ) and ud = y. The finite kernels converge to the kernel of this process on every compact
range of λ with max(q, q/θ) ≤ 1 (proved below); the convergence of the thresholds is proved for y < 1 and,
computer-assisted, for 1 ≤ y ≤ 23/8 and 47/16 ≤ y ≤ 95/32, and rests, for the other y ≥ 1, on hypothesis
(H2), without which only the limit points of the thresholds are bracketed (status below).
Pair density in the limit process (proved). For Z = F(F − 1)u−2λ , the flow contributes −2λF(F −
1)u−2λ−1 (F − u), births +2λF 2 (F − 1)u−2λ−1 and deaths −2F(F − 1)u−2λ ; the sum is −2(1 − λ)Z. A division
multiplies E[Z] by 21 22λ = 22λ−1 . At threshold, provided the Z-moments are finite, (22λ−1 − 1) κ = 2(1 − λ),
R
with κ = Ev [Zdiv ]/Ev [ Z dt] the Z-weighted division rate and v the Perron vector of birth types. This is an
exact rewriting at threshold, not a closed form. In the simulated limit process at y = 1 the two sides are
0.7706 and 0.7700; κ = 16.6 at y = 0.25 and 4.46 at y = 1.
Direct simulation of the limit process. Jumps were sampled exactly along the deterministic flow, without
population control, giving ψ(0.25) = 0.6176 ± 0.0008, ψ(1) = 0.4862 ± 0.0006 and ψ(4) = 0.3169 ± 0.0004,
within 0.8 standard errors of the values extrapolated from the exact kernels at θ = 1 (Table S3).
Properties of ψ. An independent analysis of the limit process, with its own codes, gives four results. (i)
ψ(y) ≤ ln 2 for every y, strictly for y > 0 (proved; strictness below): Z e2(1−λ)t is a martingale between
divisions, so E[Z] cannot grow over a growth phase, and a division multiplies it by 22λ−1 ; F(F − 1) is
then sub-invariant for the kernel on types at birth with the factor 22λ−1 , which is at most 1 for λ ≤ 21 . (ii)
√
ψ(y) = ln 2−a y+o(y) with a = (3 2−4)/ ln 2 = 0.35006 (proved: Theorem S, S14; first derived by first-order
perturbation of the y = 0 kernel, using the stable distribution of S1; numerically confirmed to nine digits); the
remainder is also proved to be O(y2 ), with constants about 109 times too large. With Theorem 4, for θ ≤ 1 the
limit of Uc (n, n/y, θ) is ln(2/θ)−a y+O(y2 ); near the ceiling, with ε = ln(2/θ)−U → 0, lim supn→∞ Rmin /n ≤
(a + o(1))/ε (proved, on this side only and asymptotically); at fixed ε only lim supn→∞ Rmin /n ≤ 1/(eε − 1) is
proved, and Rmin ≈ a n/ε remains derived. (iii) A deterministic solver of the limit process (linear differential
equations along the flow, Chebyshev collocation) reproduces the values extrapolated from the exact kernels
to 10−8 for y ≤ 0.5 and to 7 × 10−5 on [1, 16] (numerical); it gives Rmin /n = 0.216, 1.126 and 3.10 for
U + ln θ = 0.3, 0.5 and 0.6. (iv) ψ is not a power law: the local exponent −d ln ψ/d ln y peaks at 0.43 near
y = 25 and falls to 0.17 near y = 220, so that the fit of the main text underestimates ψ by 13% at y = 128; on
[96, 256], 1 − λc (y) ≈ 0.40/ ln y (conjectured, short range). No closed form for y > 0 was found.
Status of Theorem 4 (proved for y < 1, and computer-assisted for 1 ≤ y ≤ 23/8 and 47/16 ≤ y ≤ 95/32;
for the other y ≥ 1, under one unproved hypothesis, without which the limit points are bracketed).
Let λc (y) = inf{λ < 1 : ρ(S ∞ (y, λ)) > 1}, where S ∞ (y, λ) is the Schur reduction, onto the types f ≤ M, of
the kernel of the limit process (its mean matrix of daughters, by number of replicases at division), for any
cut M beyond which large replicase numbers drift down under the limit kernel (such cuts exist for every
λ < 1; below); the sign of ρ(S ∞ ) − 1 does not depend on such M (proved, by the quotient property of
Schur reductions). The argument of S2 for θ > 1, with the bound at every fecundity for small λ, then gives
36


[page 37]
Uc (n, n/y, θ) → max(0, ln(1/θ)−ln λc (y)), provided (H2) the reduced kernel is subcritical for every λ < λc (y);
for θ < 1 the argument also uses (H3) λc (y) < 1, which is proved below. It rests on the convergence of the
finite kernels to the kernel of the limit process and on a uniform drift of large replicase numbers, both proved
for every y (below). (H2) is proved for y < 1 (below) and, computer-assisted, for 1 ≤ y ≤ 23/8 and
47/16 ≤ y ≤ 95/32 (Certified bounds on ψ, (vi)), so that Theorem 4 holds there, at each fixed y. For the
other y ≥ 1, (H2) is supported numerically on a truncation in F of the limit process: its spectral radius
increases strictly with λ and crosses 1 once, for y from 1 to 16, where λc (y) ≤ 0.834; without it, the limit
points of the thresholds are bracketed (below). That this λc (y) is the threshold from which ψ is computed is
established numerically, by the agreement of a deterministic solver of the limit process with the extrapolated
exact thresholds, to 10−8 for y ≤ 0.5 and 7 × 10−5 on [1, 16] (Properties of ψ, (iii)), and is not proved; so
is the decrease of ψ, certified only on a grid of step 0.05 for y < 1 (Certified bounds on ψ, below). At
infinite fecundity the limit is Theorem 3. The arguments below are outlined; they are written out in full, each
checked by an independent session, in the notes deposited with the code (S7).
The scaling limit for R > n (proved). Let y = n/R < 1. The proof has three parts. (i) Uniform drift of
large types. For any Λ0 < 1 and any integer a > 1/(1 − Λ0 ), the finite kernels satisfy Kn φa ≤ βφa beyond
some type M, with β < 1, uniformly in large n and in all (q, θ) with max(q, q/θ) ≤ Λ0 , for every y > 0.
The weight φa can grow only when few replicases remain; there it is controlled by the density of replicase
pairs, whose expectation decays at least at rate 2(1 − Λ) during the cycle, and the same quantity bounds the
tail of the cycle duration; cycles in which the protocell becomes small are controlled by comparison with an
M/M/∞ queue. (ii) Convergence to the limit process (below, for every y; for y < 1 it also follows, with a
rate, from the probability of dividing with a given number of replicases, a smooth function of the reduced
size because u is then a clock, which the finite process and the limit process reach at the same reduced size
2y). (iii) From kernels to thresholds. The Schur reduction on types ≤ M converges, with the tail bounds of
S2 (d), and is continuous in λ. With (H2) for y < 1 and the bound on pair density, which gives (H3) and
ψ ≥ ln(2/(1 + y)) (below), this proves the statement; a deficit of pair density in every type gives ψ < ln 2.
The complete proof is given in S13.
(H2) for y < 1: the size clock (proved).

Let y < 1. Along a living lineage of the limit process, F ≥ 2 >

2y ≥ u, so the reduced size u increases throughout the cycle and can serve as its clock. In this clock every
surviving lineage divides at the same time u = 2y, and the number of replicases is a birth–death chain; two
such chains can be coupled so that they never cross. The limit kernel therefore maps increasing functions
of the type to increasing functions, and increases with λ on them, strictly through survival. It follows that if
ρ(S ∞ ) ≥ 1 at some λ0 , then ρ(S ∞ ) > 1 for every λ ∈ (λ0 , 1): ρ(S ∞ ) equals one at one λ at most, which gives
(H2). In the same clock, the expected number of ordered replicase pairs, summed over both daughters, is at
least 22ky −1 times that of the mother, ky = (λ − y)/(1 − y), so that λc (y) ≤ (1 + y)/2 and ψ(y) ≥ ln(2/(1 + y)).
For every y > 0, this number falls short of its infinite-fecundity factor 22λ−1 by a positive amount in every
type, so that λc (y) > 12 and ψ(y) < ln 2.
The reduced kernel is supercritical near λ = 1 (proved).

Fix y > 0 and λ < 1. For an integer a > 1/(1−λ)

and a suitable C, V = φa (F)u−λa + C F(F − 1)u−2λ is a supermartingale of the limit process, so that large
replicase numbers drift down, by a factor tending to 21−a(1−λ) , and λc (y) is defined from the limit kernel alone.
Rτ
By the pair density, E[Zdiv ] = Z0 − 2(1 − λ) E 0 Z dt over a cycle. For ϖ > 0 and α = y(ϖ + 2)3 /(2ϖ2 ),
37


[page 38]
the function L = ϖ ln(2y/u) + αu/F satisfies G(LZ) ≤ −Z when 1 − λ ≤ 1/α, which bounds the Z-weighted
duration of a cycle by T = ϖ ln 2 + αy/2 times Z0 . Hence Kφ2 ≥ 22λ−1 [1 − 2(1 − λ)T ] φ2 ; with the drift above,
φ2 is then a strict subsolution of the reduced kernel, which is supercritical for λ close to 1: λc (y) < 1 at every
y > 0, which is (H3). For y < 1 a cycle lasts at most ty = ln[(2−y)/(2−2y)], whence λc (y) ≤ 21 +ty /(2(ln 2+ty )):
at y = 0.25, λc ≤ 0.591, against the computed 0.539. With this bound, ψ(y) > 12 ln 2 for y < 0.558, hence
for R > 1.8 n (for every y < 1 with the certified bound λc ≤ 0.65, below); the computed ψ falls below 12 ln 2
beyond y ≈ 3.1, and is proved to lie below it on [3.2, 5] (Certified bounds on ψ, (iv)). For y ≥ 1 the bound is
crude (λc (1) ≤ 0.957) and only settles (H3).
Convergence to the limit kernel (proved). Fix y > 0, θ > 0 and a compact interval of λ on which
max(q, q/θ) ≤ 1, with q = θλ. Then Kn ( f, f ′ ) → K∞ (y, λ)( f, f ′ ) for all types, uniformly in λ, and the limit
depends on q and θ only through λ. For y < 1 this also follows, with a rate, from a smooth test function.
The chain within a protocell and the limit process are coupled through common Poisson clocks: replicase
deaths occur at the same times, and while F is bounded the birth rates differ by O(|N/R − u| + 1/R). Three
estimates close the argument. (F − 1)Γ(N − 1)/Γ(N − 1 + Λ) is a supermartingale, so that F stays bounded
with high probability, uniformly in n. Over bounded times, N/R follows the flow u̇ = F − u, driven by the
chain’s own F, to O(|N0 /R − y| + R−1/2 ) in mean, by Doob’s inequality. And before its last change of F, a
cycle of the limit process comes within ε of the division size only with a probability that vanishes with ε; the
two processes then divide within O(ε) of each other, with the same type. A geometric bound on the duration
of a cycle, uniform in n, and the equicontinuity in λ of both kernels give the uniformity. Types f ′ ≤ 2y, never
produced by the limit process, keep a mass that vanishes as n → ∞.
Without hypothesis (H2) (proved, every y > 0). Let λ−c (y) = inf{0 < λ < 1 : ρ(S ∞ (y, λ)) ≥ 1}
(and 1 if this set is empty), so that λ−c (y) ≤ λc (y), and ψ− = − ln λ−c . Then max(0, ln(1/θ) + ψ(y)) ≤
lim inf n Uc (n, n/y, θ) ≤ lim supn Uc (n, n/y, θ) ≤ max(0, ln(1/θ) + ψ− (y)), with 0 < ψ ≤ ψ− < ln 2. The
proof is that of the theorem for R > n with the convergence above: the lower bound uses only points of the
set that defines λc , the upper bound only λ < λ−c . Hypothesis (H2) is exactly ψ− = ψ; it is proved for y < 1
and, computer-assisted, for 1 ≤ y ≤ 23/8 and 47/16 ≤ y ≤ 95/32 (Certified bounds on ψ, (vi)); for the other
y ≥ 1 it is supported numerically (up to y = 16), and could fail only through a tangency (Certified bounds on
ψ, (v)).
Certified bounds on ψ (certificates proved, computer-assisted; consequences for the finite model proved
at each fixed n/R that a certificate covers, the limit law for Rmin derived; monotonicity in R numerical).
An independent session bounded the spectral radius of the limit kernel rigorously from below and from above
(comparison generators, directed rounding, interval exponentials and, for large types, a supermartingale;
for y > 1, the trajectories that enter {F ≤ u} are killed, which can only lower the kernel). (i) At the 19
points y = k/20, k = 1, . . . , 19, the enclosures of λc (y), of width at most 0.0056, are disjoint and ordered,
λc (0.05) < λc (0.10) < · · · < λc (0.95), so that ψ decreases along this grid; between grid points its decrease,
and hence the uniqueness of the root of ψ(y) = U, is only numerical. (ii) ψ > 0.6 on (0, 1309/4096]
and ψ(363/1024) < 0.6; ψ > 0.5 on (0, 1807/2048] and ψ(953/1024) < 0.5 (for small y, by an analytic
bound). Let Rmin (n, U) = inf{R0 : Uc (n, R, 1) > U for all R ≥ R0 }; it is at least the Rmin of Corollary 9.2
(S14), which asks Uc > U at a single R, so that the upper bounds below hold for both definitions and
the lower bounds for this one only. Theorem 4 at the single point y1 = 363/1024 or 953/1024 gives, at
38


[page 39]
θ = 1, lim inf n Rmin /n ≥ 1024/363 > 2.8209 for U = 0.6 and ≥ 1024/953 > 1.0745 for U = 0.5; and,
without assuming that Uc increases with R, Rmin (n, 0.6) ≤ 4096n/1309 for n ≥ 8.8 × 109 and Rmin (n, 0.5) ≤
2048n/1807 for n ≥ 8.3 × 1012 , so that lim supn Rmin /n ≤ 4096/1309 < 3.1292 and ≤ 2048/1807 <
1.1334 (Proposition T, proved, computer-assisted: the finite-size pair-density bound for small n/R (The price,
bounded at every size, below), then 57 and 157 certified lower bounds on the limit kernel over adjacent boxes
in y, carried to the finite kernels by an explicit bound on their convergence for y < 1; the same bounds hold
uniformly in θ ∈ [1/2, 1] for U + ln θ = 0.6 and 0.5, with Uc (n, R, θ) in place of Uc (n, R, 1) and from
n ≥ 9.3 × 109 and 8.3 × 1012 ; exact kernels at y = a, extrapolated in 1/n, suggest that the inequality
holds from n ≈ 54 and 188). As a consequence (derived), Rmin (n, U)/n → 1/y∗ (U), with y∗ (U) the first
point where ψ falls below U, for all but countably many U ∈ (inf 0<y<1 ψ(y), ln 2), for which y∗ (U) < 1;
this needs no monotonicity in R, and that of ψ serves only to identify y∗ (U) with ψ−1 (U). These brackets
contain the values 3.10 and 1.126 given by the deterministic solver (Properties of ψ, item (iii), above). (iii)
λc (y) ≤ 0.65 for 0 < y < 1; for y ∈ [1, 2.649] the principal block of the limit kernel at λ = 0.7 on the
types 2, . . . , 50 has spectral radius above 1 (at least 1.057 on [1, 2]), and so has that at λ = 0.707 < 2−1/2
for y ∈ [2.5, 2.858]; hence ψ > 12 ln 2 on (0, 2.858]. The convergence of the finite kernels (above), at fixed
λ and for the 492 entries of that block, then gives lim inf n Uc (n, n/y, θ) ≥ ln(1/θ) + ln(1/0.707) for θ ≤ 1
and every fixed y ∈ [1, 2.858] (proved, computer-assisted, through that convergence); for y < 1, where
a block is certified only at λ = 13/20 and only on [76/256, 1], the same bound follows from Theorem 4
and λc ≤ 0.65, which give limn Uc (n, n/y, θ) ≥ ln(1/θ) + ln(20/13) with ln(20/13) = 0.4308 > 12 ln 2
(proved, computer-assisted; the certificate for λc ≤ 0.65 was also redone from scratch by a second session).
Hence, at every fixed ratio R ≥ 0.35 n (n/R ≤ 2.858), large protocells keep more than half of the bonus.
(iv) For every y ∈ [16/5, 5] and every λ ∈ (0, 442/625], ρ(S ∞ (y, λ)) ≤ 1 − 10−4 , with types counted at
birth or at division, so that λ−c (y) ≥ 442/625 = 0.7072 > 2−1/2 and, by the bracket without (H2) above,
lim supn Uc (n, n/y, θ) ≤ ln(1/θ) + ln(625/442) < ln(1/θ) + 12 ln 2 for θ ≤ 1 and every fixed y ∈ [3.2, 5]. The
certificate is one supermartingale per box of y (19 boxes), of the form (u/y)−97/20 PF (u/y) with a polynomial
PF for each F ≤ 48 and PF ∝ F(F−1) · · · (F−5) beyond, verified in exact rational arithmetic; at fixed (F, u/y)
its drift is bilinear in (λ, 1/y), and the range of u/y only shrinks as y decreases, so the four corners of each box
cover every λ ≤ 442/625 at once, without (H2). With the bound for R ≤ n/5 (below), large protocells thus
keep less than half of the bonus at every fixed ratio R ≤ n/3.2; the computed frontier, y ≈ 3.1, lies between
2.858 and 3.2. (v) For y ≥ 1 the limit kernel is also bounded from above. On a grid in s = u/y, a function
affine in s between nodes is checked in interval arithmetic with directed rounding to be a supersolution of
the backward equation of the limit process on every cell and for every (y, λ) of a box, with a supermartingale
for large replicase numbers; a Collatz–Wielandt test then gives ρ(S ∞ (y, λ)) < 1 for every λ ∈ [1/2, λlow (y)]
and every y ∈ [1, 3] (64 boxes of width 1/32; also 57 of the 64 boxes of [3, 5]), with λlow (y) 0.004 to 0.009
below the computed λc (y); for λ < 1/2 the same holds by Properties of ψ, (i). With lower bounds of the
type of (iii) near threshold, λc (y) ≤ λup (y), this brackets the limit points of the thresholds without (H2),
max(0, ln(1/θ) + ln(1/λup )) ≤ lim inf n Uc (n, n/y, θ) ≤ lim supn Uc (n, n/y, θ) ≤ max(0, ln(1/θ) + ln(1/λlow )),
an interval of width at most 0.033 on [1, 3] (for example [0.384, 0.408] at y = 2 and θ = 1), and gives
lim inf n Rmin /n ≥ 32/69 > 0.4637 for U = 0.4 and ≥ 32/95 > 0.3368 for U = 0.36 (θ = 1). By themselves,
these bounds leave (H2) open for y ≥ 1: it could fail only through a tangency of the spectral radius to 1 from
below, at some λ between λlow (y) and λc (y), in a band of width at most 0.022 on [1, 3], which they cannot
exclude (it is excluded on most of [1, 3] by (vi)); numerically, at the 17 values of y tested, the logarithm of

39


[page 40]
the spectral radius is concave on a grid of step 0.05 in λ, too coarse to resolve the band; concavity there
would exclude a tangency, but it is not proved, and (vi) does not use it. (vi) A tangency is excluded on
most of [1, 3]. Weight each path of a cycle by eαN−βA , where N is the number of replicase births in the
R
cycle and A = F(F − 1)/u dt, and let Φ(α, β) be the logarithm of the spectral radius of the resulting
kernel (the supremum over the kernels killed when F exceeds M). Each entry is identically zero or, by
Hölder’s inequality, log-convex, so Φ is convex (Kingman), and ρ(S ∞ (y, λ)) − 1 has the sign of Φ(ln λ, λ). A
tangency at some λ0 ∈ (λlow , λc ) would give Φ a supporting plane at (ln λ0 , λ0 ), tangent to the curve β = eα ,
whose slope p satisfies p D(λ0 /λlow ) ≥ ln(1/c), where K∞ w ≤ c w, c < 1, for a positive w at λlow (by
(v)), and D(x) = ln x − 1 + 1/x. Hence Φ(ln λ∗ , β∗ ) ≥ T = ln(1/c) [ln(λ∗ /λup ) + 1 − β∗ /λup ]/D(λup /λlow )
at a single point off the curve, with λ∗ ≥ λup and β∗ ≤ λlow . That point is the kernel of the limit process
∗

∗

at λ∗ , with the Feynman–Kac weight e(λ −β )A . On each of 61 boxes of width 1/32, which cover [1, 23/8]
and [47/16, 95/32], its spectral radius is bounded below eT by a supersolution of the type of (v), with the
exponential supermartingale z(u)F , d ln z/d ln u = −(λ∗ z−β∗ ), for large replicase numbers; for y ≥ 65/32, λup
comes from lower bounds of the type of (iii) recomputed closer to threshold. Hence (H2), and Theorem 4,
hold at each fixed y with 0 < y ≤ 23/8 (y < 1: size clock) or 47/16 ≤ y ≤ 95/32 (proved; computerassisted for y ≥ 1), and for these y ≥ 1 the bracket of (v) then encloses the limit itself. The smallest margin,
T − ln c∗ ≥ 0.0061, reflects the loss of the certificate, not a near-tangency (numerically, on the three boxes
simulated, which include that of the smallest margin, T exceeds Φ at the test point by 0.15 to 0.24). On
the three remaining boxes of [1, 3] and for 3 < y ≤ 16, (H2) is supported numerically only. These results
hold at each fixed y, not uniformly; between y = 2.858 and 3.2 nothing is proved about half of the bonus.
An independent code reproduced all 38 bounds of (i), the two bounds at y1 and 34 of the 209 boxes of (ii),
including the eight of smallest margin, and 36 boxes of (iii), including the least favourable of each interval; an
independent exact code (Sturm sequences in integers) re-verified the 19 boxes of (iv), exact integer arithmetic
re-certified the 121 boxes of (v), the 113 slices of its lower bounds were reconfirmed from their raw results, an
independent code re-certified the 62 certificates of (vi), which cover its 61 boxes, in exact rational arithmetic
except for the exponential bounds (300-bit arithmetic with a margin), the logs and results of the 31 slices
of the lower bounds recomputed for (vi) were re-read, without being rerun, and independent readings found
no error in the proof of Proposition T or in that of the reduction of (vi). Numerically, the spectral radius
of the exact kernel increases with R at every sampled value: its derivative, computed by complex steps, is
positive at all 39,376 sampled points where |∂ ln ρ/∂ ln R| > 10−10 , out of 39,432 (a full grid for n = 3 to 20,
a sub-grid for n = 25 to 100), the other 56 lying in saturation (2 − ρ < 10−6 ); this supports, but does not
prove, that Uc increases with R and that Rmin is well defined.
The price, bounded at every size (proved).

The same pair density bounds the fecundity needed at every

size. Its generator during growth is ϕ [RF(2(N − 1)p/(F − 1) − 1)/N − 1] when N ≥ 3, and ϕ [R(2q −
1) − 2] at F = N = 2; at θ = 1, copying contributes RF(2q − 1)/N and losses remove one. Hence Uc ≤
max{0, ln(2R/(R + 1)) + max(0, ln(1/θ))} for every division rule that does not distinguish replicases from
parasites; and, for θ ≤ 1, n ≥ 3 and every such rule that is not degenerate and never produces a daughter
with a single molecule, Uc ≥ ln(2R/(R + n − 1/2)). For θ ≥ 1 and U < ln 2, a fecundity R > eU /(2 − eU )
is thus necessary at every size, which sharpens Replacement (R > eU ); for θ ≤ 1, n ≥ 3 and such rules,
R > (n − 1/2)eU /(2 − eU ) is sufficient. Binary binomial partition produces daughters with a single molecule,
and at θ = 1 the finite-size lower bound fails for large R, since Uc ≤ un < ln 2 there; what is proved for it is a

40


[page 41]
finite-size form of the limit bound lim inf n→∞ Uc (n, n/y, θ) ≥ ln(2/(1 + y)): for θ ≤ 1, every n ≥ 10 and every
R > 0, Uc (n, R, θ) > ln(2/(1 + n/R)) − 3/((n − 1) ln 2) (proved). With y = n/R < q < 1 and b = 2(q − y)/(1 − y),
the pair density F(F − 1)Γ(N − 1)/Γ(N − 1 + b), set to 0 when the lineage dies, is a submartingale of the finite
chain during growth whenever R(2q − b) ≥ 1 + b; the binomial split, the convexity of the Γ-ratio in N and
Q
Jensen’s inequality then give ρ(K) ≥ 12 2n−2
j=n (1 + b/ j). At θ = 1 the price is therefore at most linear in size,
at every size for such rules and, up to 3/((n − 1) ln 2), for binomial partition, and Theorem 4 gives the exact
limit of the threshold at each fixed n/R ≤ 2.875 (for R ≤ n, computer-assisted; Certified bounds on ψ, (vi)).
A bound when R ≤ n/5 (proved, computer-assisted).

Let Ψ(y) = ln 2 for y < 5, and Ψ(y) = ln(1/λ0 ) for

y ≥ 5, with λ0 = 725/1024, 91/128, 373/512, 755/1024 and 759/1024 from y = 5, 5.5, 8, 12 and 16 on,
so that Ψ = 0.345300, 0.341171, 0.316746, 0.304754 and 0.299470. Then Uc (n, R, θ) ≤ max(0, ln(1/θ)) +
Ψ(n/R) for every n ≥ 2, R > 0 and θ > 0. Since ln(1024/725) < 12 ln 2 = 0.346574, a replicase that makes,
on average, at most n/5 complete copies in its lifetime keeps less than half of the bonus at every size; more
generally, a replicase maintained at a load U with U − max(0, ln(1/θ)) ≥ Ψ(y0 ) has R > n/y0 . The proof
has five parts. (i) In every state p ≤ Λ(F − 1)/(N − 1), with Λ = max(q, q/θ), and Λ ≤ λ0 as soon as
U ≥ max(0, ln(1/θ)) + ln(1/λ0 ); the generator is then dominated, on functions that increase with F, by that
of a single chain with θ = 1 and q = λ0 . (ii) A positive function V of the state of that chain, increasing in
F, whose drift is non-positive between divisions and whose expectation does not increase at division, gives
ρ ≤ 1, by optional stopping (Dynkin’s formula) and the Collatz–Wielandt inequality. (iii) For R ≤ 1/λ0 ,
V = F suffices. (iv) Otherwise V is the sum of the pair density F(F − 1)Γ(N − 1)/Γ(N − 1 + 2λ0 ) and of three
further terms, F(F − 1), F(F − 1)Γ(N − 1)/Γ(N − 1 + 4λ0 ) and one of fourth degree in F, with coefficients
that depend on n and y. (v) Its two inequalities are verified in interval arithmetic (IEEE-754 double-precision
operations, assumed correctly rounded and widened outward by one unit in the last place, with constants
enclosed by mpmath) and, for the division step up to n = 3000, in double precision with a priori bounds on
rounding errors, on a finite set of states and sizes and proved analytically beyond it, a monotonicity lemma
in n passing from base sizes to all sizes. An independent check, with a second implementation (free of
binary64 arithmetic only for the bound from y = 5) and an adversarial search over 1,554 cases with n ≤ 60,
found no gap. A second check, with our own code, recomputed both inequalities in exact rational arithmetic
in every state at 21 pairs (n, R), the division step exactly at six sizes up to n = 3001, the part for states of
100 molecules or more in interval arithmetic, and 768 spectral radii just above the bound, all at most 0.80,
without violation; it spot-checked, without redoing them in full, the computed parts that the first check had
redone. For R < 512/213 ≈ 2.40, hence at every R ≤ n/5 when n ≤ 12, the bound ln(2R/(R + 1)) above is
the better one. In the limit n → ∞ and for θ ≤ 1 the constant 5 is now 3.2 (Certified bounds on ψ, (iv)); at
finite size it remains 5, the computed frontier being y ≈ 3.1, and a certificate of this four-term form cannot go
below ln(4/3) = 0.2877. That the bonus vanishes when R ≪ n is proved at every size, but only far out: for
every n ≥ 2 and θ > 0, Uc (n, R, θ) − max(0, ln(1/θ)) ≤ 4 ln ln(n/R)/ ln(n/R) whenever n/R ≥ 1029 (proved,
computer-assisted: a certificate of the same kind with a free degree a ≥ 8, the explicit rate using interval
arithmetic for 8 ≤ a ≤ 100; checked by an independent session), a decay so slow that the certificate improves
on the bounds above only from n/R ≈ 3.4 × 1025 on, with a = 8.
The price is necessary at every size (Theorem Q; proved; the proof, written out in full and checked by
an independent session, is in a deposited note, S7). Let κQ = 1.98053 × 10−7 , the constant obtained with

41


[page 42]
δ0 = 0.005 and a cut at M = 9, which satisfies the condition κQ ≤ δ0 that the proof requires, and let δ(y0 ) =
κQ y0 /(y0 +2). For every y0 > 0, n ≥ 25, R ≤ n/y0 and θ > 0, Uc (n, R, θ) < max(0, ln(1/θ))+ln 2−ln(1+2δ(y0 )).
Hence, for θ ≤ 1 and 0 < ε ≤ κQ /3, coming within ε of the ceiling requires R > (κQ /3) n/ε at every size
n ≥ 25, including R ≤ n. With Theorem 4 and ψ(y) ≥ ln(2/(1 + y)), the threshold at R = n/ε comes within
ε of the ceiling for n ≥ n1 (ε, θ), so that, for θ ≤ 1, each fixed ε ≤ κQ /3 and large n, the infimum Rmin of the
fecundities that come within ε of the ceiling satisfies (κQ /3) n/ε ≤ Rmin ≤ n/ε: it is Θ(n/ε), with constants
independent of ε, but n1 (ε, θ) is not explicit and may grow as ε → 0. The constant is poor: the computed gap
is about 0.35 y. The proof uses the results of Appendix S2 listed in S13, Section S13.2.
A caution on simulated thresholds. A simulation of the same model with a finite population of 200
protocells underestimates Uc : on 54 points the mean bias is −0.014, −0.022 and −0.027 for θ = 0.5, 1 and
1.5, and −0.048 at worst. With 800 protocells the bias disappears or is divided by three. All thresholds
reported here come from exact kernels.

S4. Tables of thresholds
Tables S1–S3 give the thresholds quoted in the main text: at infinite fecundity (Table S1), at finite fecundity
(Table S2) and in the scaling limit (Table S3).
Table S1 | Thresholds at infinite fecundity. (a) Control at θ = 1 by two independent codes; the gap to ln 2 follows
21−2n / ln 2 from n = 4. (b) Approach to ln(2/θ): Uc at n = 200, extrapolation a0 + a1 /n + a2 /n2 on n = 100, 150,
200, and n (Uc − ln(2/θ)) at n = 200 (for θ ≥ 2 the target is 0), within 0.09 of ζ(θ) = 2(1 − 1/θ)/ ln 2 for 0.5 ≤ θ ≤ 2
(Appendix S2). Larger sizes: at θ = 0.5, Uc (800) = 1.3827161 and the fit on n = 400–800 gives a0 − ln 4 = −1.6 × 10−6
and a1 = −2.88, the fitted ζ(0.5) of the Methods; at θ = 1.5 (n ≤ 400), a0 − ln(4/3) = +1.5 × 10−7 . (c) For θ ≥ 2, where
the limit is 0, Uc (n) decreases as about 1/n: n Uc (200). (d) Division into k = 3 daughters (n ≤ 60, extrapolated).
(a) θ = 1
2

3

4

5

8

0.450266
2.43 × 10−1
1.80 × 10−1

0.644415
4.87 × 10−2
4.51 × 10−2

0.681632
1.15 × 10−2
1.13 × 10−2

0.690313
2.83 × 10−3
2.82 × 10−3

0.693103
4.403 × 10−5
4.403 × 10−5

(c) θ ≥ 2

(d) k = 3

n
Uc
ln 2 − Uc
21−2n / ln 2

θ

(b) approach to the limit
θ

Uc (200)

extrapolated

ln(2/θ)

n(Uc − ln(2/θ))

0.50
0.75
1.00
1.25
1.50
1.75
2.00
2.50

1.3723
0.9761
0.6931
0.4729
0.2925
0.1398
0.0073
0.0060

1.38622
0.98082
0.69315
0.47000
0.28768
0.13353
0.00001
0.00000

1.38629
0.98083
0.69315
0.47000
0.28768
0.13353
0
0

−2.80
−0.95
0
+0.58
+0.97
+1.25
+1.46
+1.21

42

0.5
1
1.5
2
2.5
3
4
8

n Uc (200)

Uc (∞), k = 3

—
—
—
1.459
1.209
1.087
0.965
0.821

1.3855 (1.3863)
0.6931 (0.6931)
0.2877 (0.2877)
0.0002 (0)
—
—
—
—


[page 43]
Table S2 | Exact thresholds Uc (n, R, θ) at finite fecundity (first kernel; the two entries at R = ∞, n = 200, θ = 1 and 1.5
come from the independent R = ∞ kernel and were reproduced by the second finite-R kernel). Umix : well-mixed value
at the same R (Eq. 2), the limit n → ∞ at fixed R; at R = ∞ the protocell limit is ln(2/θ) instead (1.386, 0.693, 0.288).
θ

R

n=5

20

50

100

200

Umix (R, θ)

0.5
0.5
0.5
0.5
1.0
1.0
1.0
1.0
1.5
1.5
1.5
1.5

∞
160
40
10
∞
160
40
10
∞
160
40
10

1.014
0.998
0.953
0.797
0.690
0.678
0.645
0.536
0.503
0.494
0.471
0.396

1.269
1.218
1.096
0.823
0.693
0.652
0.557
0.375
0.339
0.303
0.227
0.126

1.334
1.230
1.046
0.764
0.693
0.602
0.453
0.269
0.307
0.222
0.092
0.042

1.359
1.190
0.980
0.721
0.693
0.539
0.366
0.204
0.297
0.149
0.022
0.020

1.372
—
0.913
0.685
0.693
—
0.286
0.152
0.293
—
0.011
0.010

0.693
0.687
0.668
0.598
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000

Table S3 | Scaling limit. Top: Uc − ln(1/θ) at fixed y = n/R for three values of θ, and its extrapolation (a0 + a1 /n on
n = 100–200; a0 +a1 /n+a2 /n2 on n = 50–200). At y = 4, θ = 1.5 is at the floor Uc → 0, that is Uc −ln(1/θ) → ln 1.5 =
0.405. Bottom: ψ(y) from θ = 1 kernels at n = 50, 100, 200 and its extrapolation; λc = e−ψ . Values at y = 8 and 16
(R = 25 and 12.5 at n = 200) are the least reliable. Direct simulation of the limit process: ψ(0.25) = 0.6176 ± 0.0008,
ψ(1) = 0.4862 ± 0.0006, ψ(4) = 0.3169 ± 0.0004.
y

θ

n = 25

50

100

200

extrap. (1/n)

extrap. (1/n2 )

0.25
0.25
0.25
1.00
1.00
1.00
4.00
4.00
4.00

0.5
1.0
1.5
0.5
1.0
1.5
0.5
1.0
1.5

0.503
0.616
0.666
0.318
0.477
0.558
−0.008
0.279
0.488

0.555
0.617
0.642
0.391
0.481
0.521
0.122
0.298
0.448

0.585
0.618
0.630
0.434
0.484
0.503
0.204
0.307
0.427

0.601
0.618
0.624
0.459
0.485
0.495
0.254
0.312
0.416

0.617
0.618
0.618
0.483
0.486
0.486
0.304
0.317
0.406

0.618
0.618
0.618
0.485
0.486
0.486
0.310
0.317
0.405

y

n = 50

100

200

ψ(y) (extrap.)

λc (y)

0
0.05
0.10
0.25
0.50
1.00
2.00
4.00
8.00
16.00

—
0.6761
0.6600
0.6173
0.5605
0.4815
0.3902
0.2979
0.2112
0.1317

—
0.6761
0.6602
0.6178
0.5616
0.4838
0.3951
0.3073
0.2272
0.1573

—
0.6762
0.6602
0.6180
0.5621
0.4850
0.3976
0.3120
0.2352
0.1700

0.6931
0.6762
0.6603
0.6182
0.5626
0.4861
0.4001
0.3166
0.2432
0.1827

0.500
0.509
0.517
0.539
0.570
0.615
0.670
0.729
0.784
0.833

43


[page 44]
S5. Variants of the model
Complementary strands (bound proved, S2; limit numerical, two independent implementations). In
the model of Shah et al. 16 , strands are P (polymerase), C (its complement) and X (parasite). A catalyst P
chooses a template among the N − 1 other molecules; C is copied into P and P (other than the catalyst) into
C with probability q, into X otherwise; X is copied into X with weight θ. We take it at infinite fecundity,
with an infinite population and binomial division at 2n molecules; a protocell is alive if it holds at least one
P and at least two functional strands. In the fictitious clock, each of the (p − 1) + c functional templates is
copied at rate 1, so that F = p + c follows the one-strand law exactly; the difference is that a daughter without
P is dead (2.1% of daughters at threshold), which makes F(F − 1) no longer an eigenfunction. The limit
kernel gives λc = 0.513188648 (truncation limit, to 10−15 ), hence Uc (∞) = ln(1.9486/θ): 0.66711 at θ = 1,
0.26165 at θ = 1.5 (one strand: 0.28768) and 1.36026 at θ = 0.5 (one strand: 1.38629). At finite n and θ = 1,
Uc = 0.66457, 0.66636 and 0.66710 at n = 20, 64 and 4000, converging as −0.047/n; at θ = 1.5, 0.315 and
0.2776 at n = 20 and 64 (+1.00/n). The passage from the finite chain to the limit kernel is not proved, but
agrees to 10−8 (θ = 1) and 10−7 (θ = 1.5).
Complementary strands at finite fecundity (limit process derived; thresholds numerical).

At finite

fecundity, the thresholds of this model were computed without truncation up to n = 100 by an iterative
solver (GMRES with a level-wise Gauss–Seidel preconditioner); it reproduces 36 thresholds computed earlier by direct factorization (n = 10 to 40) to within 6 × 10−11 (same root-finding path), and an independent
code reproduces four of the new ones (n = 60 and 80) to 10−9 . The analogue of Theorem 4 would be
Uc (n, n/y, θ) → max(0, ln(1/θ) + ψc (y)), where ψc = − ln λc is the threshold of the limit process (p, c, u), with
u̇ = p − u, new replicases at rate λpc/u and new complements at rate λp(p − 1)/u (derived; the convergence
of the finite kernels to it is not proved). At y = 0.25, three methods give ψc = 0.555788, and the extrapolation
in 1/n of the thresholds for n = 60 to 100 agrees with the predicted limit to within 5 × 10−7 at θ = 1 and
3.5 × 10−6 at θ = 1.5, but only to 1.1 × 10−3 at θ = 0.5, where convergence is slow. At y = 1 and θ = 1,
ψc = 0.40151 ± 10−5 , and the extrapolated limit exceeds it by 6.2 × 10−5 , a gap that does not close up to
n = 100; at θ = 1.5, where ln(1/θ) + ψc (1) < 0, Uc decreases towards 0. At y = 4, ψc is not determined (a
numerical lower bound is 0.241) and the law is not tested. Complementary strands lower the scaling function
at y = 0, 0.25 and 1: ψc = 0.667, 0.556 and 0.402, against ln 2, 0.618 and 0.486 for one strand (numerical).
Fast parasites in the model of Shah et al. 16 (numerical).

Shah et al. 16 found that protocells keep their

polymerases against parasites copied twice as fast as the polymerase and its complement (their PCP2X
model), with Mmax ≈ 0.2 at a division size of S 0 = 10 strands. Their model is the complementary-strand
variant above with θ = 2, q = 1 − M and n = S 0 /2, their catalytic rate k playing the role of R. With their
rates and an infinite population of protocells, the threshold at S 0 = 10 is Mmax = 1 − e−Uc = 0.273 at k = 25,
0.301 at k = 100 and 0.311 at infinite fecundity (0.406, 0.459 and 0.478 when parasites are copied as fast as
the polymerase, their PCP model). At infinite fecundity it then falls roughly as 1/S 0 (nUc = 2.0 at S 0 = 16,
1.49 at S 0 = 100 and 1.46 at S 0 = 276), to Mmax = 0.0105 at S 0 = 276, towards the limit-kernel value
zero (θ = 2 > 1.9486): it stays below Mmax = 0.5 (Uc < ln 2) at every size and fecundity computed, and
positive at every size computed, as they found. We suggest that the tolerance of fast parasites is therefore a
small-size effect. A stochastic simulation of their model with 1,024 protocells, the population of their Fig. 2,
gives Mmax ≈ 0.20 for PCP2X at k = 25 and 100, and 0.34–0.36 (k = 25) and 0.36–0.40 (k = 100) for
44


[page 45]
PCP, within 0.04 of their values (≈ 0.2, 0.32 and 0.36; their population size is stated only for their Fig. 2,
not for the figures from which 0.36 and 0.2 come, and the remaining difference at k = 25, 0.32 against
0.34–0.36, is unexplained); the simulated threshold rises with population size (0.25–0.26 for PCP2X and
0.39–0.40 for PCP at k = 25 with 16,384 protocells), and a finite population cannot survive indefinitely
above the infinite-population threshold, since its protocells form a subset of the branching process (derived).
We suggest that the finite population explains most of the difference between their values and ours. This
concerns the tolerance itself, not their comparison with surfaces, which we did not recompute.
Equal partition of replicases (numerical).

With ⌊F/2⌋ and ⌈F/2⌉ replicases in the two daughters, λc =

0.6942 and Uc → ln(1.44/θ) (0.365 at θ = 1; already 0.385 at n = 60). The factor two becomes 1.44; it does
not disappear.
Self-copying, total or partial (no threshold at infinite fecundity and bounds on the limit process proved;
scaling derived; closed form and finite-size convergence numerical). Let a replicase choose itself as
template with weight c relative to another replicase, so that p = q(F − 1 + c)/[(F − 1 + c) + θ(N − F)] and
a lone replicase is alive for c > 0; c = 1 is the self-copying variant of Appendix S1, whose limit kernel has
spectral radius 2q/θ > 1 for q < θ. At infinite fecundity there is no threshold at any size for any c > 0: without
decay a lone replicase never dies, every row of the mean matrix sums to at least one, and to 2(1 − 2− f ) > 1 for
f ≥ 2; the matrix being irreducible, ρ > 1 at every load. At infinite fecundity, θ = 1 and c = 1, F is an exact
eigenvector of the finite kernel, with ρn (q) = Γ(2n + q) E[1{N1 ≥ 1}Γ(N1 + 1)/Γ(N1 + q)]/[n Γ(2n)] → 2q ,
N1 ∼ Bin(2n, 12 ); at U = 10, ρ = 1 + 3.1 × 10−5 for n = 3 to 80. The limits R → ∞ and c → 0 do not
commute: at c = 0 the threshold stays below max(0, ln(1/θ)) + ln 2 at every size and fecundity, whereas for
every c > 0 it is infinite at R = ∞. At finite fecundity the threshold is finite (Uc ≤ ln R, since p ≤ q). The
limit process, with births at rate λF(F − 1 + c)/u, defines ψ(y; c) = − ln λc (y; c); for c > 0, the convergence
of Uc (n, n/y, θ) to max(0, ln(1/θ) + ψ(y; c)) is only numerical (exact kernels up to n = 80; the errors decrease
as 1/n at most values of y when θ ≥ 1, but more slowly at y = 1/2, at y = 1 for c = 1, and for θ < 1).
For y < 12 and c ≤ 1, G[Fu−λc ] ≥ −(1 − λc) Fu−λc , so that the reduced kernel is supercritical as soon as a
lone replicase replaces itself, λc(ln 2 + ℓy ) > ℓy , where ℓy = ln[(1 − y)/(1 − 2y)] is the duration of its cycle;
conversely, F + βyF(F − 1)/u is a supersolution for λ ≤ (y/c)(1 + o(1)), at every y for every truncation. Hence
ln(c ln 2/y) − O(y) ≤ ψ(y; c) ≤ ln(c/y) + O(y) as y → 0 at fixed c ≤ 1: in the limit process there is no threshold
at high fecundity, and the constants diverge as c → 0. To first order in y at fixed c̃ = c/y = cR/n, a lone
replicase is copied in cis with probability λc̃y ln 2 per cycle and dies with probability y, and each cis copy
founds on average G(λ) − 1 ≥ 1 lineages of lone replicases, its own and those made by trans copying in the
new pair before it splits, G being computed from the infinite-fecundity kernel (G − 1 = 1 + 32 λ ln 2 + O(λ2 )).
The threshold λcis (c̃) therefore solves λc̃ ln 2 [G(λ) − 1] = 1 (derived; the limit process reproduces it to
4 × 10−6 ), and λcis ≈ 1/[1 + (1 + c̃2 ln2 2)1/2 ] to within 0.03 in ψ (numerical). The ceiling ln 2 at c̃ = 0
thus gives way to ψ ≈ ln(c̃ ln 2) + 3/(2c̃) for c̃ ≫ 1; at finite y, ψ exceeds ln 2 only for c above a value
that vanishes with y (0.0083 at y = 0.05). In terms of the model, and only numerically, at high fecundity
Uc ≈ ln(1/θ) + ln{1 + [1 + (cR ln 2/n)2 ]1/2 }, to within 0.033 for n/R ≤ 0.1: a lone replicase, which starts
about cR ln 2/(θn) copies on itself per lifetime (a fraction q of them successful), need only replace itself,
the trans copies of the pairs it founds adding the rest. One more bit requires c ≈ 4n/R (numerical, within
15% for n/R = 0.05–4; Fig. 11). Proofs are given in Appendix S12.3. No polymerase ribozyme is known

45


[page 46]
to copy itself in cis: all act in trans on a separate strand, QT45 included, which makes its complement and
then a new (+) strand in two uncoupled reactions 10 ; the clearest case in RNA of a molecule that is both the
catalyst and the template of a complete copy of itself is a ligase that joins two preformed halves of its own
sequence 50 ; earlier RNA systems engineered to be both catalyst and template 51,52 worked by assembling
oligonucleotides, and the first made the complement of only one of its own subunits. The obstacle appears
structural, since a ribozyme must be folded to catalyse and unfolded to be read 10 . Molecules that replicate
in trans are vulnerable to evolutionary extinction, which higher-level selection, such as spatial clustering,
can alleviate; in a spatial model of RNA-like replicators, complementary strands can then specialise, at high
diffusion, into a catalyst and a template 53 .
Spontaneous replication (proved at finite size and for the reduced kernel; derived; numerical).

In the

models of Bianconi et al. 15 , every sequence replicates spontaneously at rate 1 and each replicase adds α to
the replication rate of every sequence other than itself (in R2α, with i replicases, replicases replicate at rate
1 + (i − 1)α and other sequences at rate 1 + iα); protocells divide at m molecules. Our code reproduces 25
of the 26 rows of their Table 1 (51 of 52 values, the last at the rounding boundary), and their R2α model
without spontaneous replication coincides with ours to 10−6 (m = 4–16; with a parasite of weight θ, with
the independent code, θ = 1.5, n = 2–15). In our model, let every molecule also be copied without a
catalyst at rate s per lifetime, a replicase correctly with probability q s , and write χ = sq s for the number of
correct uncatalysed copies of a lone replicase per lifetime; a protocell with a single replicase is then alive.
In the scaling limit the flow becomes u̇ = F − (1 − s)u and replicases are born at rate λF(F − 1)/u + χF
(derived). The pair density no longer bounds the threshold, because it vanishes on the living type F = 1.
(i) If χ ≥ 1 there is no threshold, at every size n ≥ 2 and fecundity: h( f ) = f satisfies Kh > h, so that
ρ > 1 by the Collatz–Wielandt inequality; with q s = q, Uc ≥ ln s (proved). (ii) As y = n/R → 0, a
lone replicase stays alone for 1/(1 + χ) lifetimes on average, while its protocell divides about 1/[(1 + χ)y]
times; it is revived with probability χ/(1 + χ), at a uniformly distributed stage of growth (derived). The
χ
e ⊗ r, with e( f ) = 2 f 2− f the mean number of daughters with one replicase and
limit is the kernel B∞ + 1+χ

r the type at division of a revived protocell; its threshold is χ = 1/(G(λ) − 1), G being the mean number
of daughters with one replicase in the tree of B∞ alone (without revivals) issued from a revived protocell,
and G → ∞ as λ ↑ 21 , so that λc (0; χ) < 21 for every χ > 0 (proved for this kernel; its identification with
√
limy→0 λc (y; χ) is numerical). To first order ψ(0; χ) = ln 2 + (3 2 − 4) χ (derived); ψ(0; χ) = 0.7215, 0.8140,
0.9956 and 1.7130 at χ = 0.1, 0.3, 0.5 and 0.8; exceeding ln 2 by 10% requires χ = 0.205, and gaining one
bit (ψ = 2 ln 2) χ = 0.707 (numerical, reduced kernel). At finite fecundity more is needed: with q s = q
and θ = 1, χ = 0.40 and 0.81 at y = 0.25, 0.66 and 0.91 at y = 1. To first order the two corrections add,
√
ψ ≈ ln 2 + (3 2 − 4)(χ − y/ ln 2), so that χ ≈ y/ ln 2 brings the threshold back to the ceiling at small y (for the
exact kernel at n = 20, R = 1600 and θ = 1, χ∗ = 0.0173, against y/ ln 2 = 0.0180); at θ = 1, for n = 20–100
and R = 10–1600, the exact kernels need χ∗ = 0.017–0.93, within 2.5% of the limit process (numerical).
In R2α, a replicase is never degraded, a lone replicase is copied spontaneously at rate 1, correctly with
probability q, and cells that contain replicases must outgrow parasite-only cells, whose sequences replicate
at rate 1; for a lone replicase this acts as a removal rate w = 1 (derived), so that χeff = q. With the exponential
growth of mass-action catalysis, a lone replicase is revived at a uniformly distributed stage of ln N rather than
of N; writing ψlog for the corresponding limit, the threshold for α → ∞ and m → ∞ with α ≪ 2m is the
root of U = ψlog (0; e−U ), U ∗ = 0.903 (derived; 0.897 with ψ). Our implementation of their model gives

46


[page 47]
0.906 at α = 1000 and m = 60, decreasing towards U ∗ as m grows (0.904 at m = 120); at lower catalysis the
threshold falls below U ∗ (0.901 at α = 100 and m = 120; 0.872 at α = 10 and m = 60), which we attribute
to cycles that are no longer instantaneous. At fixed m and α ≫ 2m the threshold rises further (1.24 at m = 10,
1.30 at m = 16), presumably because a lone replicase left alone in a one-molecule daughter waits there and
refounds cells made of replicases only (mechanism derived, not computed); this singular limit is absent from
the scaling limit. Without spontaneous replication the limit α → ∞ gives back ln 2 (at α = 105 , 0.4503,
0.6444, 0.6903 and 0.6931 for m = 4, 6, 10 and 16). For a replicase of 100–200 nucleotides, χ of order 0.1
seems out of reach; below χ = 0.01 the ceiling moves by less than 0.4%. Proofs and derivations are given in
Appendix S12.2 (Fig. 10).
Complex formation (derived; checked by simulation).

Write θ = wθ0 , with θ0 the intrinsic template

quality of a parasite and w the advantage it gains because a replicase bound as a catalyst is unavailable as
a template; the decomposition holds to first order, since w depends on the parasite’s affinity. Takeuchi and
Hogeweg 36 describe the parasite’s advantage from complex formation as “less than two fold”; the factor 2
is, however, the final state of an irreversible association started from free molecules, not a bound, and we
correct it here; their own mean-field model gives a tolerated affinity ratio that decreases without saturation
as binding strengthens 39 . In a protocell with reversible pairwise association (exact canonical ensemble),
w = 1 + (P − 1)Kv exactly for F = 2, with Kv = c1 /K M , c1 the concentration of a single molecule in
the protocell and K M = (koff + kcat )/kon ; in general w ≈ 1 + ctot /K M , linear and unbounded. A Gillespie
simulation gives θ = 2.824, 7.752 and 77.09 against 2.800, 7.798 and 77.05 predicted. The regime of the
threshold (F = O(1), P ≈ n) is the one where w is largest. If instead the next copy always comes from
a complex of frozen configuration, θeff = 2(F − 1)/F, equivalent to a Yule process of rate q/2 in F, and
Uc (∞) = 0.352 rather than 0. For the class I polymerase and short primer–template substrates, Lawrence and
Bartel 46 report a dissociation constant refined to about 0.7 mM and a Michaelis constant of at least 0.4 mM;
since K M ≥ Kd here, we take K M ≈ 0.7 mM. With θ0 = 1:
diameter

c (one molecule)

N = 10

N = 100

N = 1000

50 nm

25 µM

w = 1.36; Uc = 0.38

w = 4.6; 0

w = 37; 0

100 nm

3.2 µM

w = 1.05; 0.65

w = 1.45; 0.32

w = 5.5; 0

200 nm

0.40 µM

w = 1.006; 0.69

w = 1.06; 0.64

w = 1.57; 0.24

1 µm

3.2 nM

w = 1.0000

w = 1.0005

w = 1.0045; 0.69

(Uc is the limit value ln(2/w), indicative at N = 10.) Keeping w − 1 ≤ 0.1 requires diameters of at least
165 nm at N = 100 and 356 nm at N = 1000. The K M used is that of the class I polymerase for short
primer–template substrates, not for a whole template.
Transient compartmentalization (first and second order derived; thresholds numerical). Compartments loaded at random from a common pool (Poisson, mean µ), which grow and are then all pooled again,
protect replicators against parasites without division 8,17,18 ; in those models the replicator copies itself 17 , or
an external enzyme copies every RNA and selection between compartments relaxes the error threshold 18 .
An independent session computed the cycle for a trans-acting replicase with our growth rule and without
external selection, growth stopping either at a common saturation size or after a fixed time. A rare replicase is then alone in its compartment, makes no replicase and returns to the pool, so that the replicase-free
state is neutral to first order; to second order, pairs loaded together compete with lone replicases that fill
47


[page 48]
their compartments with parasites, and the replicase-free state can be stable (derived). With saturation, no
replicase-rich state exists at θ = 1 or 1.5; where one exists (θ = 0.25 to 0.9), the threshold stays below the
well-mixed value ln(1/θ), and in most cases computed at θ = 0.5 the replicase-rich state is bistable with the
replicase-free one (numerical). With a fixed growth time, the threshold rises with the growth G per round:
at θ = 1 and µ = 2 it is 0.170, 0.339, 0.431 and 0.527 for G = 2, 10, 100 and 220 (R = 1000), and 0.601
for G = 2160 (R = 106 ), higher still for µ < 2 where computed (G = 220 and 280 ; numerical). For θ ≤ 1 a
mean-field argument, not a proof, suggests that it tends to the large-protocell value ln(2/θ) only as G → ∞
and R → ∞, with a gap closing as 1/ ln ln G; at θ = 1.5 the computed threshold stayed above ln(2/θ) up to
G = 280 . In no case computed did it exceed the ceiling ln 2 + max(0, ln(1/θ)), the highest ratio to it being
0.87 (numerical). At comparable size and fecundity (µ = n ≥ 5, same R), the threshold at which the pool
still replenishes itself stayed below that of protocells in every case computed; without that condition, the
threshold can exceed it at low fecundity, where the pool shrinks at each round: at µ = n = 10 and R = 10,
against 0.4621 for protocells, it is 0.4634 ± 0.0025 by direct simulation at G = 220 and above 0.50 at G = 240
(numerical). External selection between compartments was not computed.
Protocell fusion (invasion threshold proved; persistence of dense populations numerical).

Let proto-

cells meet pairwise at rate k f (mass action) and fuse, the fused protocell (F1 + F2 , N1 + N2 ) being split at
once by repeated binomial partition while it holds 2n molecules or more, and let density be regulated by
removal at rate µX per protocell, X being the density of protocells. (i) Starting from a world without vesicles,
fusion between protocells is of second order: the linearization at extinction is the mean generator of the
branching process of the main text, extended to protocells with F ≤ 1, which produce no living protocell;
those with F = 1 lose their replicase at rate one. Its growth rate has the sign of ρ − 1, so the invasion
threshold is Uc for every k f , µ and fusion rule (proved). Fusion with pre-existing vesicles that carry no
replicase, a fixed background or a resident population, is of first order: empty vesicles leave the dynamics
unchanged, and vesicles that carry parasites only dilute replicase pairs, so that no fusion raises the threshold
above max{0, ln(2R/(R + 1)) + max(0, ln(1/θ))}, below the ceiling (proved); the regulation does not count the
background. Such fusion lowered Uc in all 54 computed cases (numerical), 30 of which are invasion thresholds; in the other 24, vesicles without replicases proliferate on the background, and the threshold must be
taken against that resident population, against which the bound still holds (proved). (ii) Near Uc the equilibP
rium density is (ε/k f )v, with v the right Perron vector normalized over all protocells ( v = 1), ε = −r(U)/B
and B = B f − µ/k f , where r is the Malthusian rate, w the left Perron vector and B f = ⟨w, Fus(v, v)⟩/⟨w, v⟩
the reproductive value created by a fusion between two protocells of the invading population (derived; the
simplicity of r and r′ (Uc ) < 0 are checked numerically). For n = 5, 10 and 20, R = 10, 25 and 100 and
θ = 1, B f ranges from −0.200 to −0.121: most partners are vesicles without replicases, whose fusion dilutes
the pairs of living protocells. The bifurcation is therefore supercritical for every k f /µ, and continuation of
17 branches found no stationary population beyond Uc (numerical). If only protocells that carry replicases
fuse, a rule that sees content, B f becomes positive in six of the nine cases and the bifurcation is subcritical
for k f /µ > 1/B f . A dense population then persists up to a load Umax > Uc , beyond ln 2 when k f /µ is
large (Umax = 0.8476 at n = 5, R = 25 and k f /µ = 100, against Uc = 0.6204; Fig. 12B), while a rare
population still cannot invade, at fusion rates of hundreds per molecular lifetime; no known chemistry is
proposed for such a rule. Simulations of a finite population illustrate the hysteresis at U = 0.75 (numerical;
Appendix S12.4). No population, however dense and whatever the fusion rule, keeps a replicase beyond

48


[page 49]
U = ln R (proved). Proofs and derivations are given in Appendix S12.4.

S6. Measured polymerase ribozymes
Load. U = ℓIε. The information content is the functional information 26 I = − log2 Φ, where Φ = 9.5 ×
10−17 is the abundance of QT ribozyme folds in random sequence that Gianni et al. 10 estimate from its
fitness landscape, so that I = 53.2 bits (Φ = 4.4 × 10−18 , or 57.7 bits, in the preprint version, ref. 54). ℓ is
the number of lethal substitutions per bit: for a function carried by independent sites where site i tolerates
P
P
ti of the four bases, I = i log2 (4/ti ) and the lethal target of a substitution is nl = i (4 − ti )/3, so that
ℓ = nl /I is 0.5, 0.667 or 0.803 for ti = 1, 2 or 3, and 1.10 for an imposed Watson–Crick or G·U pair. For
QT45, Gianni et al. 10 report the tolerance of each site at 80% of wild-type activity, the threshold behind
their estimate of Φ: the fraction of the four bases tolerated at each of 30 unpaired sites, and the fraction of
the 16 pairs tolerated at each of seven base pairs (position 1 is not listed). These fractions give I = 53.2 bits
and, for the unpaired sites, nl = 19.0. At a base pair that tolerates k of the 16 pairs, between max(0, 7 − k)
and min(6, 16 − k) of the six single substitutions are lethal; which ones is shown only graphically (ref. 10,
fig. S21). Hence nl = 27.0–32.0, and 29.8 if the tolerated pairs are placed at random among the 15 others,
so that ℓ = 0.56 (0.51–0.60); spreading 53.2 bits evenly over 45 sites would give 0.63. The double mutants
of table S5 of Gianni et al. 10 narrow this range: the nine pairs two substitutions away are double mutants, so
that the single substitutions tolerated at a pair are k − 1 minus the tolerated double mutants (those not listed
counted as not tolerated), which gives nl = 30.3 and ℓ = 0.57, or 0.56–0.59 when double mutants within 0.3
of the threshold in log2 fitness are counted either way. We use ℓ = 0.56 throughout; 0.57 would raise every
load by 2%. Most published error rates are measured on full-length products, in which copies stalled after a
mismatch do not appear; the full-length error rate is then the rate at which complete parasites are made, and
no further correction for stalling is applied. The types of measurement differ, however (Table S4, note), and
applying each error rate to a 53-bit replicase is a normalization: except for QT45, the polymerases measured
are longer, and their own information content is unknown.
Fecundity. R = Y t1/2 /(T ln 2), the number of complete copies per template per unit time times the mean
template lifetime, assuming synthesis linear in time; published data are single end points, so this assumption
cannot be checked. In the model, R is the number of copies a replicase starts per lifetime, all of which
complete; if catalysts and templates have the same lifetime and are drawn from one population, it equals the
number of complete copies made per template lifetime. When the catalyst is in excess over the template, as
for QT45 (tenfold), fecundity per replicase is lower, by up to that excess; for 24-3, catalyst and template are
equimolar (100 nM each), and for 52-2 the parity is probable but not verified. For the 29-nucleotide fragment
copied under pH–freeze–thaw cycles, the net amplification per cycle is A = 1 + g − d, with g the complete
copies per template per cycle and d ≤ 1 the fraction of templates lost per cycle; the number of copies per
template lifetime is g/d = 1 + (A − 1)/d ≥ A whenever A > 1, so that A = 1.26 bounds R from below. The
fraction of copying slots that end in a complete copy is σ = Ytc /T , with tc the time needed to make one copy
of the object (given, or bounded, in Table S4 for each system for which σ is reported); it involves no lifetime,
and it counts full-length strands whether or not they have been released from their template.
Caveats.

For QT45, the half-life was measured “in standard reaction conditions” (ref. 10, fig. S8: 50 mM

CHES-KOH pH 9, 50 mM MgCl2 , −7 ◦ C, an exponential fit to three replicates giving a decay constant of
49


[page 50]
Table S4 | Measured systems (Fig. 8A, Table 2). U for a 53.2-bit replicase with ℓ = 0.56. Yields, times and half-lives
as compiled for this study from the primary sources cited. t1/2 : template half-life, measured (m) or calculated (c) from
the RNA hydrolysis law of Li and Breaker 55 , in the form given by Wayment-Steele et al. 56 , where it is parametrized
between 5 and 10 mM Mg2+ ; for QT45, the calculated value is the measured one multiplied by the ratio the law gives
between the nominal compositions of the two buffers (Appendix S6); calculated values for the class I lineage (200 mM
Mg2+ , far outside that range) are lower bounds. tc : time to make one copy.
system

copied object; conditions

1 − ε (source)

U

Y in T ; t1/2

R

QT45 (ref.
10)

(a) its own sequence (45 nt),
product the complementary
strand; (b) the
complementary strand,
product itself, with one
preformed hexamer, in a
separate reaction with one
pH–heat–freeze cycle;
eutectic ice, −7 ◦ C, 0.4 mM
Mg2+ ; ribozyme 80 nM,
template 8 nM
other templates: the F1
ligase 27 and a hammerhead
(ref. 28; lengths not stated);
class I conditions

0.941 ((a), NNN
pool; used);
0.926
(full-length
products of a
33-nt
hammerhead,
seq0-HH, in
other conditions:
50 mM Mg2+ ,
65 d)
0.97, full-length
products 28 ;
0.920, all
products 27

1.76;
2.20 at
0.926

(a) 0.24%, (b)
0.17% in 72 d;
117 d (m,
“standard reaction
conditions”) or
2.2 × 103 d (c,
0.4 mM Mg2+ )

(a) 5.6 × 10−3 (a) ≤ 2.4 × 10−3 ;
to 1.0 × 10−1 ; (b) ≤ 1.7 × 10−3
(b) 4.0 × 10−3 (tc ≤ T )
to 7.4 × 10−2

0.89;
2.38 at
0.920

(a) the class I ligase 30 ; (b)
0.917 (ref. 29);
110-nt products, yield
0.856 and 0.841
extrapolated to 182 nt;
(ref. 30)
class I conditions
29-nt fragment of the TPR’s 0.974 (ancestor
own catalytic core, from a
t5+1, ref. 33;
duplex at 0.18 µM in the
borrowed)
eutectic phase; triplet
substrates; pH 3.6, 80 ◦ C,
2 min ↔ pH 9, −7 ◦ C,
24–48 h; 0.4 mM Mg2+ ; 5
cycles
extension products on other 0.9912
templates (57 full-length
(aggregate);
products, 2.2 kb sequenced); 0.998
a hammerhead (37 clones,
(hammerhead)
999 nt)

2.47–
4.74

2% (F1 ligase) or 0.018–0.024
2.4%
(hammerhead) in
24 h; 0.62–0.69 d
(c)
(a) 2% in 24 h; (b) (a)
0.35% in 20 min; 0.018–0.020;
0.62–0.69 d (c)
(b) 0.23–0.25

24-3 (refs.
27,28)

52-2 (refs.
29,30)

TPR
fragment 31

tC19Z 32

0.77

net up to ×1.26
per cycle

≥ 1.26

0.26
(0.06)

—

unknown

σ (tc )

(2.1–2.5) × 10−3
(2.5 h, assuming
182 nt)

(a) 7.6 × 10−3 ;
(b) 0.096 (9.1 h,
assuming
182 nt)
0.26 (one 2-d
cycle)

—

Type of fidelity measurement: QT45, deep sequencing of the complementary strand synthesized from random triplets (0.941) and
of full-length hammerhead products (0.926; the substrate pool is not named, but the random one is what the comparisons drawn in
the same sentence — 71-89 at 0.909, 5TU at 0.895 — and the treatment of 0.974 as a fidelity QT45 does not reach both point to;
over the 32 positions copied, the 8.5% of perfect reads obtained with the random pool would give 0.926 and the 42.2% obtained
with defined triplets 0.973, although the published fidelities are positional averages rather than such Lth roots); 24-3, full-length
products on a C-rich template (0.97) and all oligomeric products, partial ones included (0.920), as Tjhung et al. 28 note; 52-2, a
hammerhead template (0.917), a single pass on the hammerhead (0.856) and synthesis of the class I ligase (0.841); t5+1, average
positional fidelity; tC19Z, sequenced full-length products.

0.0059 per day, R2 = 0.94), not in the 0.4 mM Mg2+ buffer in which it copies itself; since RNA cleavage is
catalyzed by Mg2+ , the measured value is probably a lower bound. The calculated value extrapolates it: the
measured half-life times the ratio, 18.5, that the RNA hydrolysis law 55,56 gives between the copying buffer
(0.4 mM MgCl2 , 1.2 mM KCl, 1 mM CHES-KOH, pH 9) and that of the measurement, hence a factor of
18.5 on R. This assumes that the law, although wrong in absolute value and parametrized only between 5
and 10 mM Mg2+ , gives the right dependence on Mg2+ and K+ between the two buffers at −7 ◦ C and pH 9.
Its Mg2+ term contributes a factor of 47.6 and its K+ terms a factor of 0.389; a Mg2+ exponent of 0.7 or
0.9 instead of 0.8 would divide or multiply the ratio by 1.6 (an illustration, not an estimated uncertainty).

50


[page 51]
These compositions are those reported before freezing 10 . In eutectic ice the solutes concentrate by a factor
inversely proportional to the total solute content of each buffer, which is 44 times larger in the buffer of the
measurement. Were the two liquid phases to reach the same total concentration, the Mg2+ ratio would fall
from 125 to about 3, the ratio of the law to 2.7–3.8, and the lower end of the fecundity gap would rise from
10 to 47–67 (a conjectural reading, for total concentrations of 3.76 to 1 mol kg−1 , the first being that of an
ideal solution freezing at −7 ◦ C). Only the ratio is used, because the law alone predicts 50 d in the buffer
of the measurement at the potassium estimated below (32–82 d for 5 to 50 mM), 57% below the measured
value. The potassium brought by the base that titrates the CHES is not reported; for the CHES pKa of 9.39
at 25 ◦ C 57 we estimate it at 14 mM in the buffer of the measurement, whose legend lists no KCl, and at
0.29 mM in the copying buffer, whose potassium is then 1.5 mM (a pKa of 9.3 or 9.5 would give a ratio
of 17.7 or 19.7). Case (b) underwent one pH–heat–freeze cycle, whose potassium hydroxide adds 0.59 mM
of K+ if the KCl reported excludes it; its calculated R would then be 15% higher. The ratio depends on
the potassium of the measurement (ratio 11–29 for 50 to 5 mM, the copying buffer held fixed, a range that
also covers a common change of both) and on the potassium exponent of the law (ratio 14–24 for 0.55 to
0.30); together, these place the lower end of the fecundity gap of QT45 between 5 and 25 rather than at 10.
The main text of Gianni et al. 10 calls the conditions of that measurement “standard reaction conditions”, for
which their supplementary material fixes no buffer: its description of standard reactions refers the final buffer
concentrations to each figure legend, and at 50 mM MgCl2 some legends list 200 mM KCl (their Fig. 1D and
figs. S2, S4 and S9A,B), most list none (their Figs. 1F, 2 and 3 and figs. S8, S9C, S10–S13, S23–S25, S27
and S33). With 200 mM KCl in the buffer of the measurement, the ratio would be 6.7, the law alone would
predict 138 d, 18% above the measured value (a level that does not decide between the two readings, since
the law is parametrized only between 5 and 10 mM Mg2+ ), and the lower end of the fecundity gap would
be 27 (15–51 for potassium exponents of 0.30 to 0.55, and 172–185 in the conjectural reading of equal total
concentrations). The reading of the legend, used here, is the more favourable to QT45. The ribozyme was in
tenfold excess over the template. The time tc to make one copy of QT45 is not measured: neither the accepted
version of Gianni et al. 10 nor its supplementary material reports a time course of these two syntheses. Shorter
reactions are shown, but under other conditions and without a yield. The supplementary material of Gianni
et al. 10 reports an optimization of 26 d for the synthesis of the complementary strand, case (a) of Table S4,
at varied ribozyme and triplet concentrations, with full-length product marked (fig. S28), and reactions of
27 to 30 d for the synthesis of QT45 itself, case (b), in the same 0.4 mM Mg2+ but at 40 nM ribozyme or
less instead of 80 nM — a strand-inhibition series (fig. S29), a scan of hexamer substrates (fig. S30) and the
controls of the sequencing reactions of their Fig. 4 (fig. S34), the last two with full length marked, in part
by the recombination noted below. The preprint version 54 reports 28 d for the complementary strand at up
to 125-fold higher concentrations (ribozyme and Mg2+ ; primer and template 31-fold, triplets 35- to 50-fold),
and 33 d for QT45 itself at a fivefold lower ribozyme and a fourfold higher triplet concentration, with the
same 0.4 mM Mg2+ . Read as copy times, these durations would lower σ to (6.4–9.3) × 10−4 . We keep the
bound that needs no such reading: a complete copy is made within the reaction time of the yields, tc ≤ T ,
so that σ ≤ Y. The yields themselves are upper bounds as well: Gianni et al. 10 report a background of fulllength product formed by recombination rather than by synthesis, separated from the synthetic product only
for sequencing. For 24-3 the two published fidelities count different products: 0.97 for full-length products,
which we use, and 0.920 for all products, partial ones included; the difference itself shows that mismatched
intermediates are less often extended to full length 28 ; for 52-2, the fidelity depends on the template and on

51


[page 52]
the Mg2+ concentration. For the class I polymerases, fecundity was measured on templates other than the
replicase itself or extrapolated to its length; for 52-2, the values (b) extrapolate a 20-min yield linearly over
a lifetime and over a copying slot 27 times longer, whereas products completed within 20 min imply a much
faster subpopulation; the values (a), measured over 24 h on the synthesis of the class I ligase 30 , are the more
reliable. The only fecundity above one belongs to a 29-nucleotide fragment, not to a replicase, copied by
a polymerase whose own fidelity in these conditions is borrowed from its ancestor: Attwater et al. 31 report
no error rate of its own. That borrowing is probably optimistic: the 0.974 of t5+1 was measured at pH 8.3,
and Gianni et al. 10 measure 0.895 for the same lineage at the pH 9 of the eutectic conditions, attributing the
difference to the assay pH. At 0.895 a 53-bit replicase would carry U = 3.1 instead of 0.77, which widens the
load gap of the TPR fragment from 1.1 to 4.5 without changing the direction of the comparison. Its 1.26 is
the highest amplification per cycle reported, obtained in the most favourable condition tested (a tenfold lower
starting concentration of the duplex), so the bound R ≥ 1.26 applies to that condition. For tC19Z, the 0.9912
is an aggregate over sequenced full-length extension products; the per-base error spectra (ref. 32, fig. S8c)
show that it is, to within 10−4 , the unweighted mean of the four per-base fidelities, whereas the pooled error
rate over the 2,195 positions sequenced is 5.9 × 10−3 , from 13 errors in all, none of them opposite U; the
Poisson interval on 13 errors alone spans a factor of about three in error rate. The 0.998 on the hammerhead
rests on two errors.
How to measure R (a proposal).

The fecundity of the model is a total turnover number: the number of

complete copies of its own sequence that one replicase molecule makes in all, in the conditions in which
it copies itself. Two measurements, with opposite biases, would fix it. In an exhaustion assay, the replicase, sub-stoichiometric to its own sequence as template and to primer and substrates, is incubated until
full-length product stops accumulating; R is the product per replicase molecule initially present, authenticated by sequencing, and replenishing the substrates shows whether the plateau comes from the catalyst.
Independently, the initial rate kc of complete copies per replicase and the lifetime τ of its activity, measured
in the same buffer, give R ≈ kc τ. To our knowledge neither has been reported for a polymerase ribozyme
copying its own sequence: the estimates above combine single end-point yields with half-lives. The assay
itself is not new: for the triplet polymerase on an exogenous template, 22 full-length complementary strands
per ribozyme were measured by gel densitometry in 24 h in eutectic ice, falling to 1.8 when the catalyst was
raised from 0.4 to 10 nM at a fixed 40 nM primer and template (ref. 31, Extended Data Fig. 1b). Turnover
should be read where it saturates as the catalyst is diluted, and reported per catalyst molecule rather than
per template, the two differing by up to the catalyst excess (tenfold for QT45, Table S4); for a replicator
copied through its complement, both half-reactions should be reported. A time course would test the linear
synthesis assumed above, and the half-life of the replicase in the buffer in which it copies itself would remove the extrapolation discussed in the caveats. The prediction is then testable: a replicase in protocells that
grow from about 50 to 100 molecules gains less than half of the ln 2 that compartments can add, whatever its
fidelity, unless it makes, on average, more than 10 complete copies of its own sequence per lifetime (proved,
computer-assisted; Appendix S3).

S7. Provenance
All numbers are produced by scripts in the project archive (directory replicateur/), with logs and JSON
outputs. Fig. 1: these_fig1_these_v015c.py (verif3_out.json; rmin_exacts_v015.json, from
52


[page 53]
rmin_exacts_v015.py, exact roots of ρ = 1 in R; these_frontieres.json). Fig. 2: these_fig1_
schema.py. The proofs summarized in Appendices S2, S3 and S5 are written out in full in notes deposited with the code[ (in French; English versions to be deposited before submission)], each checked by
an independent session. The ceiling for any division that ignores which molecules are replicases, with
complementary strands, and the bracket on the price: PLAFOND_PAIRES_v0.1; the size clock, (H2) and
(H3) for y < 1, and λc > 12 : HORLOGE_TAILLE_v0.1; the uniform drift, the convergence for y < 1
and Theorem 4: CONJ1_R_SUP_N_v0.1; (H3) at every y: NOTE_H3_v0.2.1; the convergence at every y
and the bracket without (H2): NOTE_PROP_D_v0.3; the Schur reduction and its limit passage: PREUVE_
CONJECTURE1_v0.2. The bound for R ≤ n/5 (Appendix S3), whose proof rests in part on computations in interval arithmetic and with a priori rounding-error bounds: RESULTAT_PRIX_v0.1, whose proof
is the written argument with the scripts iv_np.py, c_params.py, c00, c01, c03, c04, c05, c10 and
c11 and their logs (the logs c02_* and *_y5_log.txt are superseded, and sections 0 and 7 of the note,
which predate its checks, are superseded by Appendix S3, its section 8 being completed by the credit to
P6 (a) of PLAFOND_PAIRES_v0.1, as VERIF_RESULTAT_PRIX_v0.1 asks), checked by an independent
session (VERIF_RESULTAT_PRIX_v0.1) and rechecked with separate code (VERIFICATION_THEOREME_
P_v01). The certified bounds on ψ (Appendix S3): RESULTAT_CERTIF_Y_SUP1_v0.2 and RESULTAT_
MONOTONIES_v0.3, with their scripts and logs, each checked by an independent session with its own code
(VERIF_CERTIF_Y_SUP1_v0.1, VERIF_MONOTONIES_v0.1), and, for λc ≤ 0.65 at y < 1, RESULTAT_
H2_SUITE_v0.1 (VERIF_RESULTAT_H2_SUITE_v0.1; redone from scratch, with the bound for R ≤ n/5,
in VERIF_THEOREME_P_CERTIFICAT_v0.1); transient compartmentalization and complementary strands
at finite fecundity (Appendix S5): RESULTAT_TRANSITOIRE_v0.2 and RESULTAT_BRINS_GRAND_N_
v0.3 (VERIF_TRANSITOIRE_v0.1; VERIF_BRINS_GRAND_N_v0.1 and, for v0.3, VERIF_BRINS_GRAND_
N_v0.3_controle). The frontier of half the bonus, the pair density at finite size with the upper bounds
on Rmin , and the bounds for y ≥ 1 (Appendix S3): RESULTAT_FRONTIERE_MOITIE_v0.2, RESULTAT_
MONOTONIES_R_MIN_v0.2 and RESULTAT_H2_Y_SUP1_v0.2, each checked by an independent session with
its own code (VERIF_FRONTIERE_MOITIE_v0.1, VERIF_MONOTONIES_R_MIN_v0.1, VERIF_H2_Y_SUP1_
v0.1); the extinction bound (Appendix S3): RESULTAT_PRIX_v0.2 (VERIF_RESULTAT_EXTINCTION_
v0.1); hypothesis (H2) on most of [1, 3] (Appendix S3, Certified bounds on ψ, (vi)): RESULTAT_H2_
CONCAVITE_v0.2.1, with its scripts and logs, checked by an independent session with its own code
(VERIF_H2_CONCAVITE_v0.1); the test of the update rule of the lattice (Appendix S10): RESULTAT_DIAG_
EXCES_1024_v0.2, with tests fixed in advance but not checked by an independent session. The corrections made to these notes after their checks are not re-verified, except those of RESULTAT_BRINS_GRAND_
N_v0.3. The lever (Appendix S2, Fig. 9): NOTE_LEVIER_v0.2; spontaneous replication (Fig. 10): NOTE_
SPONTANEE_v0.2; partial self-copying (Fig. 11): NOTE_CIS_PARTIEL_v0.2; protocell fusion (Fig. 12):
NOTE_FUSION_PROTOCELLULES_v0.2; these four (Appendices S2 and S5) are deposited with their scripts
and logs (directories levier/, spontanee/, cis_partiel/ and fusion_protocellules/), and their
proofs are given in English in Appendix S12. The comparison with the model of Shah et al. 16 (Appendix S5) rests on RECONCILIATION_SHAH_v0.2 (v0.1 checked in VERIF_RECONCILIATION_SHAH_
v0.1) and its scripts, and the paragraph on measuring R (Appendix S6) on MESURE_R_v0.4 (v0.1 to
v0.3 checked in VERIF_MESURE_R_v0.1 to v0.3)[ (neither current version yet re-verified)]. The proof
of Theorem 4 for R > n in English (S13): SI_THEOREME_G_v0.2.1, written from CONJ1_R_SUP_N_
v0.1, PREUVE_CONJECTURE1_v0.2 and HORLOGE_TAILLE_v0.1, checked by an independent session, its

53


[page 54]
corrections checked again (VERIF_SI_THEOREME_G_v0.1 and its control)[ (v0.2.1 applies three minor
corrections without a new check)]. The slope of ψ (Theorem S, S14): PENTE_T8B_v0.2.1 and its English text SI_PENTE_T8B_v0.2, checked (VERIF_PENTE_T8B_v0.1, VERIF_PENTE_T8B_v0.2, VERIF_
PENTE_T8B_v0.2.1); S14 is the English text of v0.1 with the corrections of these checks and three passages of v0.2. The necessary price (Theorem Q, S3): PRIX_NECESSAIRE_v0.2 and its English proof SI_
THEOREME_Q_v0.2, checked (VERIF_PRIX_NECESSAIRE_v0.1, whose one important finding v0.2 corrects,
and VERIF_PRIX_NECESSAIRE_v0.2: no critical or important finding). Incomplete copies and baths of
several lengths (S8, S9): BAIN_INACHEVEES_v0.2 and its English section SI_BAIN_INACHEVEES_v0.1,
checked (VERIF_BAIN_INACHEVEES_v0.1, VERIF_BAIN_INACHEVEES_v0.2, which writes out the proof
of lim inf n mc (n) ≥ m∞ ), with the statuses of these checks. Fig. 5: figure_une_courbe_v0.3, checked
in its first version (VERIF_FIGURE_UNE_COURBE_v0.1)[ (v0.2 applies the findings and v0.3 changes only
the labels, without a new check)]. The literature on self-copying (S5): BIBLIO_REPLICASE_CIS_v0.2,
checked in its first version (VERIF_BIBLIO_REPLICASE_CIS_v0.1)[ (references checked online by one
agent; of those added to the bibliography, two were checked again in this lineage, and three, Doudna
1991, Green 1992 and Mills 1967, are to be confirmed on the publishers’ pages)]. These pieces, from
the AI lineage “fusion”, are deposited with their scripts and logs[ (notes in French; none rechecked in
this lineage)]. The SHA-256 digests of all these notes are listed with the code. Fig. 3: these_fig2_
plafond.py (data verif3_out.json, independent R = ∞ kernel). Fig. 4: these_fig3_fecondite.py
(seuil_R_fini_exact.json, psi_extrapole.json, verif4_v06_out.json, and verif3_out.json
for the R = ∞ lines of panel C). Fig. 8: these_fig6_ribozymes_v126.py (these_frontieres.json,
from these_frontieres.py; the fecundity of QT45 from qt45_R_optionB_v03.py, which also gives
the numbers of Appendix S6 on its half-life; the other measured fidelities and fecundities are entered in
the script from Table S4). The number of lethal substitutions per bit: qt45_ell.py; every load and fidelity target that depends on it, including Table S6: these_charges_v06.py. Finite-R kernels: seuil_R_
fini_exact.py and the independent verif4_R_fini.py; analysis: seuil_R_fini_analyse.py; identity at θ = 1: verif_Z_theta1.py. Tables S2 and S3 are written by manuscrit_these/make_si_
tables.py from the analysis log. Theorems 2–3, numerical checks: limite_et_borne_ln2.py, and
the independent checks in verification_scripts/ (suffix _v04); the bound at every fecundity, the spectrum at θ = 1 and the limit for θ > 1 (Appendix S2): verification_scripts/v1408_theoremes.py;
the numerical support of hypothesis (H2) for y ≥ 1 (Appendix S3): the logs lotC_04_pdmp_limite_
log.txt and lotC_05_complements_log.txt of an independent check of the proofs, in commun/verif_
scripts/verif_conj1_lotC/; the first-order correction (Appendix S2): correction_1n.py, from the
thresholds of verif3_runs.py, and complements_v127.py for Table S1. Complementary strands: shah_
brins.py; spontaneous replication: bianconi_R2a.py; complex formation: verif3_runs.py (parts G
and H); thresholds against θ at R = ∞: complexe_vs_ln2.py and complexe_limite.py. Unfinished
copies (Fig. 6, Appendix S8): tronque_protocellule.py (R = ∞) and tronque_R_fini.py (finite
R, including the fecundity required), figure these_fig4_tronque_v08.py (vanishing points: tronque_
zeros_v08.py); independent checks in commun/verif_scripts/ (prefixes v1, v2, v7, v8). The common
axis (Fig. 7, Appendices S9 and S11, Tables S5 and S6): noyau_classes_arnoldi.py (length classes;
lineages: section mecanisme, tc_de_n.py and tc_de_n_v2.py) and seuil_de_b_U0.py (a single truncated length), figure these_fig5_axe_v1212.py; independent checks with prefixes v3, v9 and v11. The
per-nucleotide variants with the lattice timing, and the limit kernel at n = ∞ (Figs. 7A, S2 and S3, Table S5,

54


[page 55]
Appendix S9): replicateur/article_unique/, with seuil_b_infini.py (exact kernels by noyau_
classes_arnoldi.py, limit kernel by noyau_limite_bain.py, in replicateur/mecanisme_bain/),
seuil_b_geometrique_n.py (without the lattice timing) and seuil_b_infini_tableau.py; shapes,
neq and figure data: these_axe_v11.py and these_axe_v111.py; Fig. S2: these_figS2_v1212.py;
Fig. S3: these_figS3_v1302.py; independent checks, including the splittings of the length classes, with
the prefixes vplan and vinf in commun/verif_scripts/. Every length (from b = 0.3 at n = 20, beyond b = 4/9 at larger n), its limit and finite fecundity (Appendix S9): noyau_couches.py (exact kernels
with several classes), mc_longueurs.py (Monte Carlo over every length) and noyau_R_fini.py (finite
R), in replicateur/article_unique/, with the tables seuil_b_longueurs_tableau.py, toutes_
longueurs_n20_tableau.py and r_fini_tableau.py; the shapes with every length (points of Figs. 7A
and S3A): toutes_longueurs_axe_v127.py; the levels against the lattice and Fig. S3: niveau_reseau_
v127.py, complements_v127.py and complements_v128.py (ratios at R = 3, minimal fecundities).
The lattice and round-18 (Appendix S10): axe_reseau_v08.py, whose output these_axe_v11.py reads,
and axe_reseau_v127.py, which recomputes the brackets on D; both read the published threshold of
Tupper and Higgs 5 , extracted from the vector graphics of the published figure by a script deposited in
replicateur/reseau/, and the logs of the reimplementation, deposited there with its simulation code, the
definitions of its series and the output of each deposited point (surviving runs, mean densities, extinction
times), in deposits described by replicateur/reseau/LISEZMOI_depot_v1302.md; we use its series
in the termination probability at kpol = 25, without point mutations or initial parasites, on the 256 × 256
lattice with the replicable fate (runs to t = 120, 500 and 1000) or the lost fate (runs to t = 120) and
on the 512 × 512 lattice with the replicable fate (runs to t = 120), and none of the others (other durations, lattice sizes, time steps, lengths, copying rates, error rates or fates of unfinished copies); the
brackets from all these series (Appendices S9 and S10, Figs. 7A, S2 and S3): reseau_t500_v1211.py,
reseau_v1212.py, reseau_v1214.py and reseau_v1302.py, from the raw points; for D read on the
truncated share of products, axe_reseau_v127.py also reads the protocell thresholds of Fig. 7A. The
double-mutant constraint on ℓ: qt45_ell_v2.py. The bath of slow truncated copies (Appendix S9, Fig. S1):
replicateur/mecanisme_bain/, with mecanisme_bain_suite.py (exact kernels, by the code noyau_
classes_arnoldi.py copied unchanged), noyau_limite_bain.py (limit kernel), ancestral_limite_
mc.py (ancestral counts at n = ∞) and mecanisme_bain_tableau.py (tables); figure commun_fig_
mecanisme_bain.py; independent checks with the prefix vbain in commun/verif_scripts/.

S8. Unfinished copies: kernels and identities
Model.

A protocell holds F replicases, A full-length parasites of template weight θ, and B truncated

molecules of template weight θ′ ; the copying replicase draws its template among the other molecules in
proportion to their weights, which sum to W = (F − 1) + θA + θ′ B. A copy of a full-length template stops
early with probability τ. With the replicable fate the unfinished copy is a truncated molecule; with the lost
fate it is nothing. A completed copy of a replicase is a replicase with probability q and a parasite otherwise;
parasites and truncated molecules are copied faithfully, and truncated molecules are not truncated again unless stated. With retruncation, in the two-class model of Appendix S9 a copy of a slow truncated molecule
stops with probability τπfast and its product is a fast one; in the per-nucleotide model, a copy of a truncated
molecule of class k stops with probability 1 − (1 − m)Lk , Lk the mean length of the class rounded to a whole
number, and its product is lost or assigned to the class of its length, as after a first stop. Copies occur at rate
55


[page 56]
R per replicase and every molecule decays at rate 1 (R = ∞: no decay). Division at 2n molecules, binomial
partition of each type, F ≤ 1 a dead lineage, as in the main model.
Identity (i): the lost fate.

With the lost fate no truncated molecule exists, so every template present is full

length and every copy stops with the same probability τ, whatever its template. A stop changes nothing: it
is a self-loop of the jump chain. The process is therefore, term by term, the main model with copying rate
R(1 − τ); at R = ∞ it is the main model itself. The identity requires that τ be the same for all templates
present; it fails if parasites differ in length from the replicase. A partial loss, in which only some unfinished
copies are lost while others are replicable, is not a rescaling of τ, even at R = ∞: the wasted slots fall only
on full-length templates.
Identity (ii): θ′ = θ.

If truncated molecules are exactly as good templates as parasites, parasites and

truncated molecules can be merged into one type Q = A + B: copying a replicase gives a replicase with
probability (1 − τ)q, and a member of Q otherwise; the weights, the division size, the death of lineages and,
since Bin(A, 21 ) + Bin(B, 12 ) = Bin(A + B, 21 ), the partition depend only on (F, Q). The aggregation is exact
(K3 V = V K2 for the aggregation matrix V), so the spectral radii are equal and Uc = Uc(2) + ln(1 − τ) at every
size, fecundity and load.
Identity (iii): termination per nucleotide at b = 1. Let copies stop at each nucleotide with probability
m, products shorter than Lcut nucleotides be lost (Appendix S10) and longer ones be replicable truncated
molecules, with retruncation, and let parasites have θ = 1, as in Table S6. If copying time does not depend
on length (b = 1), every template yields a product of at least Lcut nucleotides with the same probability
(1 − m)Lcut , and shorter products are self-loops of the jump chain. The next molecule is therefore a replicase
with probability q(1 − m)L−Lcut (F − 1)/(N − 1), and parasites and truncated molecules merge as in (ii): the
model is the main model at θ = 1 with q replaced by q(1 − m)L−Lcut and, at finite R, R by R(1 − m)Lcut , the
rate of copies of at least Lcut nucleotides (R itself when R counts these copies, as in Appendix S9). Hence
Uc (n; m) = Uc (n; 0) + (L − Lcut ) ln(1 − m) at every size, with R so rescaled at finite fecundity: only stops
beyond Lcut cost load.
Theorem 2 with termination. In the same model with θ = 1, for any 0 ≤ b ≤ 1, with or without retruncation, and whether or not a copy that stops early ends sooner, every template other than the catalyst yields
products of at least Lcut nucleotides at a rate of at least (1 − m)Lcut , in units in which complete copies of a
replicase template occur at rate (1 − m)L . The next molecule is then a replicase with probability at most
q(1 − m)L−Lcut (F − 1)/(N − 1), so the pair density ϕ = F(F − 1)/(N − 1) is a supermartingale during growth
whenever q(1 − m)L−Lcut ≤ 12 ; the death of a random molecule does not raise it on average, and the partition
step of Appendix S2 applies unchanged. Hence Uc (n) < ln 2 − (L − Lcut )[− ln(1 − m)] at every size and
fecundity: termination and load share the ln 2 of Theorem 2. In the model with stop probability τ and the
replicable fate, the same step gives Uc (n) < max(0, ln(1/θ))+ln 2+ln(1−τ) whenever θ′ ≥ min(θ, 1); identity
(ii) gives the threshold itself at θ′ = θ.
Numerics.

Thresholds are computed on the jump chain of the transient states {F ≥ 2, N ≤ 2n − 1} with

H = (I − PT T )−1 PT D , the binomial partition applied as successive tensor contractions, and the spectral radius
obtained by power iteration (three types) or by Arnoldi iteration with a triangular resolvent (states ordered so
56


[page 57]
that copies increase the index; at finite R, GMRES preconditioned by the triangular part). Two independent
codes give the same kernels entry by entry (2 × 10−15 on 149 parameter sets, n = 3 to 20; 3.6 × 10−14 on 46
sets with up to five types), and a stochastic simulation confirms them.
Finite fecundity.

With θ = 1, θ′ = 2 and n ≤ 20, the share of the tolerable load removed by replicable

truncated copies varies by less than 10% when R goes from 10 to infinity; below R ≈ 10 it grows as R
decreases (by a factor 1.3 at n = 20, R = 3, and 3.8 at n = 5, R = 1.4). At θ = 1.5 (with θ′ = 3, n = 10) the
variation already reaches 12% between R = 10 and infinity. The fecundity required at n = 20, U = 0.30 rises
by factors of 1.04, 1.11, 1.49 and 6.98 for τ = 10−3 , 3 × 10−3 , 10−2 and 3 × 10−2 (replicable fate), against
1/(1 − τ) ≤ 1.031 (lost fate).
Incomplete copies of several kinds.

Let a copy of the replicase be complete with probability σ = (1 − m)L

and correct with probability q if complete, and let an incomplete copy be lost, an inert strand, or a parasite
of class k with template weight θk , copies of parasites being possibly truncated in turn; let σR and sk be the
probabilities that a copy of a replicase, or of a class-k parasite, yields a molecule. (i) Without inert strands, for
any exchangeable division rule and at every size and fecundity, ρ ≤ 1 whenever qσ/ min(σR , mink θk sk ) ≤ 21
(proved): conditionally on producing a molecule, a copy produces a replicase with probability at most this
ratio times (F − 1)/(N − 1), so that the pair density remains a supermartingale during growth, and lost
copies only slow the clock. (ii) If every incomplete copy becomes a parasite, growth therefore requires
− ln(qσ) < ln 2 + max(0, ln(1/θmin )) at every size and fecundity, θmin being the smallest template weight
among the classes: the tolerated point load loses L| ln(1 − m)| one for one, and the third requirement becomes
a ceiling (proved). With the rule Lcut of the lattice transposed to protocells, at b = 1 and without the lost fate,
all classes have the same effective weight and Uc (n, ∞) = max(0, un − (L − Lcut )| ln(1 − m)|) exactly, at every
size (proved). (iii) Lost incomplete copies cost only fecundity: if parasites are truncated at the same rate and
their incomplete copies are lost as well, the kernel is exactly the untruncated one at fecundity Rσ, so that
Rmin is multiplied by (1 − m)−L (proved); but they do not obey the bound on the total load, since a protocell
made only of replicases loses time, not fidelity (an exact counterexample).

S9. The common axis in protocells
Lengths and classes.

A truncated copy of relative length ξ = L′ /L has θ′ (ξ) = 1/[b + (1 − b)ξ]. Replicable

truncated copies have lengths uniform on [0.1L, L), as on the lattice; with a stop probability m per nucleotide
they are geometric instead, nearly uniform for small m. The exact kernel cannot carry a continuum of types,
so lengths are grouped into K classes, each with its share of production πk and its mean θk′ . Splitting at the
elbow θ′ = 2 (ξ∗ = (1/2 − b)/(1 − b)) gives a fast class of share (ξ∗ − 0.1)/0.9, 44% at b = 0, 26% at b = 0.25,
none beyond b = 0.444, and a slow class whose θ′ is uniform in 1/θ′ on [1/2, 1) for every b < 0.444. A class
that is never produced must be removed from the state space: otherwise the kernel becomes reducible and an
unreachable component, made of protocells inheriting molecules that are never made, can carry the largest
spectral radius (in one test, ρ = 1.000 instead of 0.666).
Results. Table S5 gives D(0.15) and the value of b at which half of the damage is recovered. One class
at the mean θ′ is misleading: it puts all truncated copies on one side of the elbow. With termination per
copy, from two classes on, the half-point lies between 0.38 and 0.44 (the latter with three classes of equal

57


[page 58]
production at n = 20, not tabulated) and moves up as the classes are refined, so that two classes give a
conservative estimate of the contrast with the lattice. At finite fecundity (R = 25) the curve is flatter still;
with retruncation (a copy of a truncated molecule may stop in turn) D(0.15) falls to 0.12–0.14 at n = 20 (0.14
with termination per copy, not tabulated), and further as n grows. Over the 44 variants with a distribution
of lengths, D(0.15) lies between 0.05 and 0.31 and the half-point between 0.29 and 0.47 (Fig. S2); on the
lattice, 0.55 and 0.12 in the published simulations, 0.56 (0.53–0.59) and 0.13 (between 0.10 and 0.15 if mc
increases with b) in the reimplementation with runs to t = 120 (Appendix S10).
Table S5 | The common axis in protocells (U = 0, replicable fate, θ = 1, R = ∞ unless stated). Termination per copy:
truncated lengths uniform on [0.1L, L). Termination per nucleotide: a copy stops at each nucleotide with probability
m, products shorter than 10 nucleotides are lost, and truncated lengths are grouped in two classes split at θ′ = 2; with
retruncation, copies of truncated templates stop in the same way; with the lattice timing, a product of relative length
ξ is made at a rate multiplied by θ′ (ξ) (the last of these rows is the variant of Fig. 7A); n = ∞: limit kernel, with a
cutoff of eight fast truncated molecules (Appendix S9). D(0.15): share of the damage recovered at b = 0.15; b1/2 : b at
which half of it is recovered (linear interpolation on the grid b = 0, 0.05, 0.15, 0.25, 0.5, 0.75, 1; for the lattices, on
their own grids, which add 0.10, 0.26, 0.30 and 0.32 for the reimplementation and 0.1 and 0.2 for the published lattice,
ref. 5). Rows with termination per nucleotide, and the lattice: D is read on the critical termination per nucleotide mc ,
and the last column is mc (0.25)/mc (0). For the reimplemented lattice, brackets give the bounds implied by those of its
threshold, for b1/2 if mc increases with b (Appendix S10).
model

n

D(0.15)

b1/2

τc (0.25)/τc (0)

termination per copy
one class at the mean θ′
two classes at the elbow
four classes of equal production
elbow, then the slow side in two
two classes, R = 25
termination per nucleotide, two classes
no retruncation
retruncation
no retruncation, lattice timing
retruncation, lattice timing

10/20/50
10/20/50
10
20
20

0.35/0.33/0.40
0.22/0.20/0.19
0.18
0.18
0.17

0.22/0.21/0.19
0.38/0.40/0.41
0.41
0.43
0.42

2.1/3.6/7.8
1.30/1.32/1.33
1.24
1.27
1.39

20/40/80/∞
20/40/80
20/40/∞
20/40/80

0.17/0.16/0.16/0.16
0.12/0.07/0.05
0.31/0.30/0.29
0.20/0.15/0.13

0.45/0.46/0.47/0.47
0.37/0.37/0.37
0.29/0.30/0.31
0.33/0.35/0.35

1.35/1.36/1.36/1.36
1.67/1.76/1.81
2.64/2.65/2.66
3.23/3.32/3.37

lattice (ref. 5; S10)
lattice, reimplementation, t = 120 (S10)

1024 × 1024
256 × 256

0.55
0.56 (0.53–0.59)

0.12
0.13 (0.10–0.15)

39
33

Copying as on the lattice.

On the lattice, copies of parasites stop at the same rate per nucleotide as other

copies, and a copy that stops early ends sooner, since its duration is set by the length of its product (Appendix S10). The variant of Fig. 7A does the same: termination per nucleotide with retruncation, and a
product of relative length ξ made at a rate multiplied by θ′ (ξ), each class being represented by its mean θ′
weighted by production. This timing divides the threshold at b = 0 by 3.4–3.5 (n = 20 to 80) but leaves the
contrast of shape: D(0.15) = 0.20, 0.15 and 0.13 for n = 20, 40 and 80, half of the damage is recovered at
b = 0.33, 0.35 and 0.35 (0.34, 0.36 and 0.38 on the finer grid of b of Fig. 7A), and b = 0.1 multiplies the
tolerable termination by 1.5–1.6, against 10.4 on the published lattice. D(0.15) falls with n because, with
retruncation, mc falls as 1/n below b = 4/9 (below), whereas mc (1), where every truncated copy has θ′ = 1,
does not depend on n: the range log[mc (1)/mc (0)] grows as log n (1.48, 1.80 and 2.11 decades), and the larger
the protocell, the larger the contrast with the lattice. Two classes are a coarse approximation near the elbow,
which lies at 2(1 − τ) rather than at the cut θ′ = 2 (below). With retruncation (n = 20, without the lattice
timing), splitting the slow class at θ′ = 1.4 changes mc by less than 3% for b ≤ 0.15 and D(0.15) only from
0.12 to 0.10, but lowers mc (0.40) by 26% and D(0.40) from 0.55 to 0.41; cutting at 2(1 − τ) instead lowers
D(0.40) to 0.40 and D(0.45) from 0.74 to 0.48. The half-point then moves beyond 0.40, or 0.45, and only
58


[page 59]
D(0.15) carries the contrast without that reservation. Without retruncation, splitting the slow class raises mc
by 9–12% (b ≤ 0.15, n = 20).
Which protocells carry growth. The left Perron vector u of the kernel gives the composition of the population at division; the lineages that carry growth follow the ancestral (spine) distribution u ◦ w/⟨u, w⟩, with
w the right eigenvector (reproductive values), taken at threshold as the limit of the supercritical case 58 . With
fast truncated copies alone (θ′ = 4.02), the population at threshold is dominated by contaminated protocells
with 3.9 (n = 10) or 4.2 (n = 20) replicases at division, which are dead ends: the sub-kernel of contaminated
protocells is subcritical (spectral radius 0.71–0.72, and 0.67–0.68 with the length distribution below), and a
protocell free of truncated copies has 73 (n = 10) or 279 (n = 20) times the mean reproductive value. Along
the lineages, 63% and 70% of protocells carry no truncated copy, with 19 of 20 and 39 of 40 molecules
being replicases. With the length distribution at b = 0, 87–91% of the protocells along the lineages carry
no fast truncated copy; they tolerate many slow ones (13 of 20, 33 of 40) and about 6.5 replicases, nearly
independently of n.
Why τc depends little on n without retruncation.

Slow truncated copies far below the elbow make the

replicase more viable than lost copies would (τc = 0.208 against 0.103 at n = 20) and, without retruncation,
nearly independent of n: τc = 0.237, 0.208, 0.196 and 0.190 for n = 10, 20, 40 and 80, against 0.103, 0.049,
0.024 and 0.012 with fast truncated copies alone (Fig. S1A). The lineages that carry growth then live in the
regime of Theorem 1, with few replicases in a bath of slow truncated molecules. With slow truncated copies
alone, copied faithfully, the model is exactly the main model with q = 1 − τ and θ = θ′ , so that the limit
kernel has τc (∞) = 1 − θ′ /2 (0.307 at θ′ = 1.39; extrapolation of n = 20 to 80: 0.30698), and a class of
truncated copies can form such a bath only if θ′ < 2(1 − τ). With fast truncated copies as well, a limit kernel
that follows the replicases of a lineage through a cycle in the bath gives τc (∞) = 0.1845, which the exact
kernels approach (extrapolation of n = 20 to 80: 0.18455). This kernel takes the limits in the order t → ∞,
then n → ∞: a daughter that inherits a dozen fast truncated molecules or more (eight in the per-nucleotide
kernels of Table S5) is counted as lost, since at finite n their descendants invade the bath within O(log n)
cycles, and raising that cutoff does not change the threshold; without that rule, finitely many fast molecules
′
would not affect an infinite bath, and the limit would be 1 − θslow
/2 = 0.307. Along the ancestral lineages

(births weighted by reproductive value, paths weighted by the reproductive value of the division state they
reach), newborn protocells hold about four replicases whatever n, and copies of replicase templates, the only
ones that can stop and so start a new fast truncated molecule, number 2.9 to 2.6 per cycle for n = 10 to 80 (2.6
at n = ∞), against 9.4 to 79.5 without a bath (Fig. S1B); all other copies are of truncated templates, which
never stop. The stops that give a fast truncated molecule therefore tend to a constant number per cycle along
these lineages (0.103 at n = 10, 0.065 at n = 80, 0.062 at n = ∞), and growth passes through lineages whose
few stops gave slow copies: only 23–25% of their stops give a fast truncated copy, against 44% at production
(n = 10 to 50). Slow copies near the elbow (θ′ = 1.9) form a bath too, but with a large 1/n correction: τc
falls from 0.149 to 0.045 between n = 10 and 80, toward 0.034. Letting copies of slow templates stop as
often as those of full-length ones, with the same products (ε = 1, which is the retruncation of Appendix S8),
restores the 1/n law and empties the bath: nτc is again nearly constant (1.56 to 1.49 for n = 10 to 80), as
when unfinished copies other than fast ones are lost (1.99–2.11 for n = 10 to 50), most copies along the
lineages are again copies of the replicase (two-thirds at n = 10, 94% at n = 50), and at n = 80 the lineages

59


[page 60]
divide with 155.7 replicases among 160 molecules (Fig. S1C). The condition is strict: with ε = 0.1, τc at
n = 80 already falls from 0.190 to 0.080, and it keeps falling with n; with termination per nucleotide, a slow
truncated template of relative length ξ stops about ξ times as often as the replicase, and ξ > 1/2 at b = 0.
On the lattice, copies of parasites stop at the same rate per nucleotide (Appendix S10), so that the protocell
variant to compare with it is the one with retruncation, that of Fig. 7A.

0.1
0.05

0.01

fast only
fast + lost
fast + slow, = 1.39
fast + slow, = 1
slow only, = 1.39
fast + slow, = 1.9

1/n

10
20
40
80
Protocell size n (molecules at birth)

no bath: grows as n

20

=n

10
5
2

C Risky bath copies restore the 1/n law

0.2

50

bath:
23
= 1.9 joins the bath

Critical truncation probability c

n=

0.3
0.2

0.02

B In a bath, risky copies per cycle stop growing with n

c falls as 1/n only when no bath is tolerated

Replicase copies per cycle, ancestral lineages

Critical truncation probability c

A

0.1
0.05

0.02

10
20
40
80
Protocell size n (molecules at birth)

= 0 (faithful bath copies)
= 0.1
= 1 (bath copies as risky)

10
20
40
80
Protocell size n (molecules at birth)

Fig. S1 | Without retruncation, slow truncated copies form a bath that keeps τc finite as protocells grow (U = 0,
R = ∞, b = 0; truncated copies in two classes at the elbow, 44% fast with θ′ = 4.02, the others slow; Appendix S9). (A)
Critical stop probability against protocell size: fast truncated copies alone; the others lost; slow ones with θ′ = 1.39, 1
or 1.9; slow ones alone (θ′ = 1.39). Dashes: limit kernel (n = ∞). (B) Copies of replicase templates per cycle along
the lineages that carry growth: about n without a bath, two to three in one. (C) Letting copies of slow templates stop
with probability ετ restores τc ∝ 1/n at ε = 1.

B No variant gains from b as early as the lattice

1.0

Share of the damage recovered, D(b)

Share of the damage recovered, D(b)

A Counted per copy, half is recovered near b 0.4
0.8
0.6
0.4
protocells, n = 10
protocells, n = 20
protocells, n = 50
lattice (Tupper & Higgs 2017)
lattice, reimplementation

0.2
0.0
0.0

0.2
0.4
0.6
0.8
1.0
b, length-independent share of copying time

1.0
0.8
0.6
0.4
retruncation, standard, n = 20
retruncation, standard, n = 40
retruncation, standard, n = 80
no retruncation, n =
the same, standard rule

0.2
0.0
0.0

0.2
0.4
0.6
0.8
1.0
b, length-independent share of copying time

Fig. S2 | No protocell variant gains from b as early as the lattice (U = 0, R = ∞; black and grey, the lattice as in
Fig. 7A). (A) Termination per copy, truncated lengths uniform on [0.1L, L) in two classes at the elbow, n = 10, 20, 50.
(B) Termination per nucleotide, products shorter than 10 nucleotides lost, two classes: with retruncation, n = 20, 40,
80 (blue dashes: standard rule, without the lattice timing); without retruncation, n = ∞ (orange; solid: with the lattice
timing, dashes: without). At every interior b of the published lattice curve, each variant shown recovers less of the
damage than the lattice.

Level against the lattice.

The levels of the two architectures compare only as orders of magnitude, for

three reasons. The lattice is at finite fecundity: a polymerase with a template and a free site copies at rate
kpol = 25 per unit decay rate, but it is not always busy, so that the fecundity at which protocells should be
60


[page 61]
compared with it is not defined; protocells are at R = ∞ unless stated (finite fecundity: below). The lattice
threshold is the largest m at which at least 5% of 100 runs survive to t = 1000, the protocell threshold an
asymptotic ρ = 1, and the reimplemented lattice, with another criterion and runs to t = 120, puts its threshold
1.0 to 1.8 times the published one (0.70 to 1.24 times with runs to t = 500, and 0.92 to 0.99 times at b = 0.5
with runs to t = 1000; Appendix S10). And the grouping in two classes moves mc by at most about 12%
for b ≤ 0.15, more near the elbow (above) and beyond it (below). Without retruncation the threshold of the
two-class model has a finite limit at every b (Fig. S3A): with the lattice timing, mc (∞) is 50 times the lattice
threshold at b = 0, 5.7 times at b = 0.15, 3.5 times at b = 0.25 and 2.5–2.8 times for b ≥ 0.5 (143, 10, 5.1
and 2.5–2.8 without it), and at every size computed (n = 20 to ∞) it is at least 2.4 times the lattice threshold
at every b of the published curve. Splitting the slow class raises these values at n = 20 (above), but keeping
every length lowers them: at b = 0.5, by 4–5% at n = 20 and 40 (Monte Carlo over every length, below),
and perhaps much more for large protocells. The large-protocell argument given below, applied without
retruncation, would put the limit at 9.5 × 10−4 at b = 0.5, under the lattice threshold, if the bath sorted
itself toward its shortest lengths; without retruncation only selection between nearly neutral lengths would
sort it, and the limit without retruncation is not established. With retruncation, mc falls as 1/n wherever fast
truncated copies are made, since the bath then makes fast copies at a rate proportional to n (ε = 1 above):
n mc has nearly converged by n = 80 for b ≤ 0.25 with the lattice timing (b ≤ 0.20 without it), changing
by less than 4% between n = 40 and 80, and we extrapolate C(b) = lim n mc as 2 · 80 mc (80) − 40 mc (40).
A protocell then tolerates more termination than the lattice only below neq (b) = C(b)/mlattice
(b) molecules
c
(Fig. S3B): with the lattice timing, neq = 330, 89, 48, 35, 30 and 29 for b = 0 to 0.25 in steps of 0.05, or
185–232, 58–84, 35–48, 21–25 and 19–23 at b = 0, 0.05, 0.10, 0.15 and 0.25 against the brackets of the
reimplemented lattice with runs to t = 120 (rounded outward; 309–464 at b = 0 and 28–34 at b = 0.15 with
runs to t = 500); without it, 1140, 260, 125, 80 and 62 for b ≤ 0.20. At larger b, up to 4/9, n mc still grows
at n = 80, since fast truncated copies are then rare and barely beyond the elbow, and neq is at least its value
at n = 80. Below 4/9 the effect of keeping every length is measured only at n = 20, the Monte Carlo being
trapped at larger n (below), and splitting the classes changes the two-class thresholds by −9 to +5% up to
n = 80: these neq are orders of magnitude.
Near and beyond the elbow, every length. Two classes overestimate the threshold with retruncation near
the elbow, and beyond it increasingly as n grows: each class model tends to the elbow of its shortest class,
represented by a mean, whereas with every length the bath concentrates on the shortest replicable length,
Lcut = 10 nucleotides, which grows fastest. A population Monte Carlo over the 90 lengths (populations of
2,000 protocells, 1,500 at n = 320, validated against exact kernels with three classes up to n = 80; a finite
population underestimates the threshold, by a few per cent where measured) gives at n = 20 thresholds that
the two-class model exceeds by factors of 1.26, 1.33 and 1.50 at b = 0.3, 0.35 and 0.4, and at b = 0.5 and
n = 80, mc = 1.45 × 10−3 against 2.10 × 10−3 with three classes and 3.88 × 10−3 with the cut of Fig. S3A.
The contrast of Fig. 7A is therefore stronger still (its points): at b = 0.5, D = 0.68, 0.66 and 0.66 at n = 20,
40 and 80, instead of 0.82, 0.84 and 0.86, against 0.90 on the published lattice, and at n = 20 half of the
damage is recovered near b = 0.39 instead of 0.34; below b = 4/9 the Monte Carlo is trapped for n ≥ 40, and
D(0.15) and D(0.25) keep their two-class values. For large protocells, Theorem 1 applied to a bath of growth
rate θ′ (Lcut /L)(1 − m)Lcut , against replicase templates copied intact with probability (1 − m)L , gives the limit
m∞ (b) = 1 − [θ′ (Lcut /L)/2]1/(L−Lcut ) in both timings: 1.06 × 10−3 at b = 0.5, 2.74 × 10−3 at 0.6 and 4.86 × 10−3

61


[page 62]
at 0.75, and 0 for b ≤ 4/9. This limit is derived for the limit kernel: Theorem 1 is proved for a bath of
one type, and its extension to a bath of several lengths rests on a law of large numbers. Its identification
with the limit of mc (n) is conjectural: it assumes that two limits commute, which Appendix S2 proves for
parasites of a single type (Theorem 3) but not for a bath of several lengths; at R = ∞, for classes that differ
by their template weights as in S8, the bracket by the extreme classes and the uniformity in θ of that limit
prove only the lower bound lim inf n mc (n) ≥ m∞ (S9, Several parasite classes). The Monte Carlo thresholds
decrease toward it up to n = 320, and their extrapolations (lattice timing) meet it to within 2% for b ≥ 0.5, the
approach being slower near 4/9. The limit equals the published lattice threshold, interpolated, at b∗ ≈ 0.53
(against the reimplementation, if mc increases with b: 0.54–0.57 with runs to t = 120, 0.52–0.55 with runs
to t = 500 and 0.51–0.54 with runs to t = 1000, rounded outward; Appendix S10). Beyond b∗ , protocells
that copy as the lattice does then tolerate more termination than it at every size; besides the sizes computed,
this needs only the lower bound lim inf n mc (n) ≥ m∞ , the direction that Theorem 3 proves for a bath of one
type, together with the sizes between, which remain numerical. Between 4/9 and b∗ they do so only below
neq ≈ 40 at b = 0.45, where the lattice is interpolated, and ≈ 80 at b = 0.5 (against the reimplementation,
23–28 and 38–44 respectively with runs to t = 120, 33–40 and 66–80 with runs to t = 500, and 79–109
at b = 0.5 with runs to t = 1000), by interpolation of the Monte Carlo thresholds in n; these come from
populations of 2,000 protocells and are therefore slightly low (Fig. S3B).
Finite fecundity, against the lattice. With fecundity R and decay at rate 1 (each replicase completes copies
at rate R, whatever their length, and products shorter than Lcut cost no time, so that the lattice timing sets
only which products are made), the termination threshold of protocells with retruncation (exact kernels for
b = 0.3 to 1, with two classes of equal width in θ′ rather than the cut at θ′ = 2, which leaves a single class
beyond 4/9) is multiplied at R = 25 by 0.80–0.86 at n = 10, 0.57–0.81 at n = 20 and 0.29–0.68 at n = 40,
and it decreases without a plateau as n grows (computed up to n = 160 with one class, 320 at b = 1), toward
zero (derived in mean field at b = 1): the elbow at b = 4/9 and the advantage at every size beyond b∗ are
properties of R = ∞. At R = 25, protocells tolerate more termination than the published lattice only below
about 23 to 33 molecules for b = 0.3 to 0.6 (about 20 to 28 with every length, an estimate that applies the
finite-R factor of the two-class model to the Monte Carlo thresholds), and 230 at b = 1, where the model
with one class is exact. Which R matches the lattice is not known. R = 25 equals its copying rate; R = 3
puts protocells, whose minimal fecundity without termination is close to 1 (Rc = 1.003 at n = 20), about as
far above it as the lattice at kpol = 25 stands above the rate at which its point-mutation threshold vanishes,
between 8.6 and 9.0 (Fig. 3 of ref. 5). At R = 3, protocells of 10 molecules tolerate more termination than
the lattice at b = 0.3 and 1, and as much to within about 10% from b = 0.45 to 0.75 (two classes), but
protocells of 20 molecules tolerate 15 to 46% less at every b computed.
Several parasite classes at R = ∞.

(iv) At R = ∞, without inert strands, and at every size, the spectral

radius lies between those of the one-class kernels with fidelity qσ/σR and the largest and smallest of the
weights θk′ = θk sk /σR (with inert strands, only the lower bound holds), so that the limit of the threshold
is bracketed by those of the extreme classes (proved, by a monotone coupling of the number of replicases
at division and Gelfand’s formula). The same coupling shows that Uc (n, ∞, θ) does not increase with θ,
so that the limit of Theorem 3 is uniform in θ on [a, ∞) for every a > 0 (proved, with Pólya’s theorem).
(v) If the bath of a lineage settles at a composition with Perron root µ, the threshold at large size would

62


[page 63]
10 2

lattice (Tupper & Higgs 2017)
reimplementation, t = 120
reimplementation, t = 500
reimplementation, t = 1000

10 3

b*

10 4

10 5

b = 4/9

no retruncation, n =
the same, standard rule
retruncation, n = 20
retruncation, n = 40
retruncation, n = 80
two classes, beyond b = 0.3
every length
m (b), limit kernel

B Up to b * , protocells win below neq (limit kernel)
Size below which protocells win, neq

Critical termination per nucleotide, mc

A Two classes: without retruncation, mc( ) > 0
1000
300

b*:
neq
(if mc m )

100
30
10

0.0
0.2
0.4
0.6
0.8
1.0
b, length-independent share of copying time

lattice timing
standard rule
reimplemented lattice, t = 120
reimplemented lattice, t = 500
reimplemented lattice, t = 1000
every length, beyond b = 4/9

n mc not yet converged
at n = 80

0.0 0.1 0.2 0.3 0.4 0.5 0.6
b, length-independent share of copying time

Fig. S3 | In the two-class model, retruncation decides whether protocells tolerate more termination than the
lattice at every size (termination per nucleotide, U = 0, R = ∞). (A) Critical termination per nucleotide: the lattice
(black, published; grey, reimplementation with its brackets: diamonds, runs to t = 120; squares, runs to t = 500;
triangles, runs to t = 1000, with an arrow for a lower bound, every run having survived at the largest m tried; squares
and triangles offset in b, by 0.02 and 0.04 respectively, to the left up to b = 0.5 and to the right beyond; the triangle
near b = 0.59 is thus for b = 0.55); protocells without retruncation at n = ∞ (orange; solid: lattice timing, dashes:
without it), whose threshold stays finite in the two-class model; protocells with retruncation and the lattice timing,
n = 20, 40, 80 (blue), whose threshold falls as 1/n below b = 4/9. The two-class curves overestimate the threshold
near the elbow and beyond (dashes beyond b = 0.3): points keep every truncated length (population Monte Carlo,
offset slightly in b), and the dotted line is the threshold m∞ (b) of the limit kernel (derived; Appendix S9), which the
points approach and which crosses the published lattice at b∗ ≈ 0.53. (B) Size below which protocells with retruncation
tolerate more termination than the lattice (solid: lattice timing; dashes: without it): neq = C(b)/mlattice
where n mc has
c
nearly converged (two classes), and beyond b = 4/9 by interpolation of the thresholds with every length (circles); neq
is infinite beyond b∗ if the thresholds approach m∞ . Bars: against the brackets of the reimplemented lattice (blue: runs
to t = 120; light grey: runs to t = 500; dark grey: runs to t = 1000).

be − ln(qσ) = ln(2/µ). This is a heuristic conjecture: it is derived under a law of large numbers for the
bath, a condition that no lineage keeps a large bath without the dominant class, and Schur reductions on
compositions, none of which is proved; it is supported numerically on exact two-class kernels up to n = 64,
where the convergence can be slow and non-monotone. When the dominant class has the largest θk′ and is
not truncated into another kept class, ln(2/µ) is a proved lower bound.

S10. The lattice
Model.

Tupper and Higgs 5 simulate a 1024 × 1024 periodic lattice with the eight-site neighbourhood, each

site empty or holding a polymerase strand, its complement, or a parasite, of length L = 100 for the first two
and between Lcut = 10 and L for parasites. A strand is copied by a polymerase on a neighbouring site
into an empty site neighbouring the template. The length of the product is drawn first, copying stopping at
each nucleotide with probability m, and a product shorter than Lcut is discarded; the copy is then made at
rate k(l) = kpol L/[bL + (1 − b)l], with kpol = 25, and strands decay at rate 1. Copies of parasites stop too,
so that truncated molecules are truncated again, and a copy that stops early ends sooner, its duration being
set by the length of its product: the closest protocell variant is the per-nucleotide model with retruncation
and this timing, that of Fig. 7A (Table S5). Their runs start from 15% each of polymerases, complements
and parasites of random lengths. Their Fig. 7 gives, for each b, the largest m at which at least 5% of 100

63


[page 64]
runs keep the polymerase until t = 1000, without point mutations. Read on the vector coordinates of the
published figure, it recovers half of the damage at b = 0.124, with D(0.15) = 0.550, D(0.25) = 0.707 and
mc (0.25)/mc (0) = 38.6, over a range of 2.24 decades; mc (0.1)/mc (0) = 10.4 is the tenfold gain the authors
note.
Reimplementation. An independent implementation of these rules on a 256 × 256 lattice (time step 10−3 ,
runs to t = 120 from polymerase and complement strands without parasites, 20 runs per point, 40 at b = 0
and at the earlier points at b = 1) brackets the critical termination at each b between the largest m at which
some run kept the polymerase and the smallest at which none did. It differs from the published model in
one rule: the strands made during a time step are placed at its end, one chosen at random where several
seek the same site, so that a new strand acts only from the next step, a delay of a thousandth of the mean
lifetime of a strand. Placing each new strand at once instead (a sequential update) changed the extinction
times on the published 1024 × 1024 lattice (b = 0, m = 2 × 10−5 , 28 batches of runs, pooled as planned
in advance) by a factor 1.024 (95% interval 0.904–1.169; the confirmatory test fixed in advance detected
no effect), about +0.9% (−3.8 to +6.1%) on the threshold (derived, as an order of magnitude; not checked
by an independent session), so that this rule matters little. With the central value at the geometric mean of
the bracket, and brackets on D that combine the ends of the brackets of mc (b), mc (0) and mc (1) in the least
favourable way, given mc (0) ≤ mc (b) ≤ mc (1), D(0.15) = 0.56 (0.53–0.59) and D(0.25) = 0.70 (0.67–0.73),
rounded outward. If mc increases with b, half of the damage is therefore recovered between b = 0.10, where
D < 0.46, and b = 0.15, where D > 0.53; interpolating the central values gives 0.13. The bound at 0.15 rests
on the brackets narrowed by a series of runs added at b = 0, 0.15 and 1 (no run of 40 kept the polymerase at
m = 2.5 × 10−5 for b = 0, one run of 20 at 3.5 × 10−4 for b = 0.15, and none of 20 at 3.5 × 10−3 for b = 1);
without that series, the bounds are b = 0.10 and 0.25. Both bounds turn on single runs. With one surviving
run fewer at the lower end of a bracket, one more at its upper end, or one at the next point measured, the
bound at 0.15 falls only with a surviving run at m = 3 × 10−5 for b = 0, where none of 40 distinct runs
survived, and the bound at 0.10 falls without the one run of 40 that kept the polymerase at m = 2 × 10−5 for
b = 0, or with a surviving run at 2 × 10−4 or 3 × 10−4 for b = 0.10, where none of 20 survived; at worst
0.05 < b1/2 < 0.25 remains, the interpolated value staying between 0.09 and 0.15. The reimplementation is
thus consistent with the shape of the published curve, over 2.18 decades, with mc (0.25)/mc (0) = 33. Later
series of runs to t = 120, with 40 runs at the points that bound b∗ (Appendix S9), narrow the brackets at
b = 0.5 and 0.75 to [1.8, 1.9] × 10−3 and [2.5, 2.75] × 10−3 and add b = 0.45, 0.55, 0.6 and 0.65 (Figs. 7A,
S2 and S3A). Runs to t = 500 (b = 0, 0.05, 0.10, 0.15, 0.45 to 0.65 and 1; 20 or 40 runs per point) lower the
brackets, by 8 to 27% for b ≥ 0.05 in the ratio of central values and by 45% at b = 0, where survivors are
rare; at b = 0.5 the bracket, [1.45, 1.55] × 10−3 , then contains the published threshold. Then D(0.05) = 0.31
(0.26–0.35) and D(0.15) = 0.57 (0.53–0.61), and half of the damage is again recovered between b = 0.10,
where D < 0.494, and b = 0.15, where D > 0.531; interpolating gives 0.12. Each bound again turns on
single runs: in the same cases, with the upper ends of the brackets at t = 120 as further bounds where the
grid at t = 500 ends, at worst 0.05 < b1/2 < 0.45. Runs to t = 500 still die as late as t = 485, and at b = 0.5
runs to t = 1000 lower the bracket again, to [1.35, 1.45] × 10−3 , 0.92 to 0.99 times the published threshold:
the central value falls by a factor 0.81 from t = 120 to 500 and 0.93 from 500 to 1000. These runs still die as
late as t = 959, so that the threshold may fall further with longer runs, and the published curve, from runs to
t = 1000 on a larger lattice, remains the reference for levels (Appendix S9). Against the brackets at t = 500

64


[page 65]
alone, the limit m∞ (b) of Appendix S9 crosses the lattice threshold between b = 0.52 and 0.55 if mc increases
with b, against 0.54 to 0.57 at t = 120; at t = 1000, every run survived at b = 0.44 and m = 1.1×10−3 , a value
above m∞ (b) for every b ≤ 0.5; with the lower end of the bracket at b = 0.5 and the bracket [1.6, 1.7] × 10−3
at b = 0.55, the limit crosses between 0.51 and 0.54, with the upper ends of the brackets at t = 120 and 500
as further bounds beyond b = 0.55 (survival cannot increase with run length). On a 512 × 512 lattice, with
runs to t = 120 (20 runs per point, 40 for four values of m at b = 0), the brackets at b = 0, 0.15, 0.5 and 1 are
[3.5, 4.0] × 10−5 , [3.5, 4.0] × 10−4 , [2.0, 2.1] × 10−3 and [3.5, 3.75] × 10−3 , and D(0.15) = 0.50 (0.47–0.53),
against 0.56 (0.53–0.59) on 256 × 256; to three decimals, rounded outward, the two ranges are 0.477–0.529
and 0.534–0.589, disjoint, but one surviving run more or fewer at an end of these brackets can make them
overlap. On the larger lattice the range lies below the published 0.550; one more surviving run at b = 0.15
and m = 4 × 10−4 would move it to 0.507–0.555, which includes 0.550. Runs on the larger lattice survived
more often at 10 of the 19 points common to both sizes and less often at none, and died later on average at
17 of the 18 where runs died at both sizes (sign tests, p = 0.002 and p = 1.4 × 10−4 ): at t = 120, a higher
threshold on the larger lattice cannot be told from slower extinction. These brackets take survival of at least
one run, which is 2.5% where 40 runs were made, as at b = 0, and 5% elsewhere. With the 5% criterion
of Tupper and Higgs 5 , D(0.15) = 0.60 (0.55–0.64) on 256 × 256 and 0.54 (0.50–0.57) on 512 × 512 at
t = 120, ranges that overlap (0.554–0.638 and 0.508–0.562 to three decimals, rounded outward), the second
containing the published 0.550, and if mc increases with b, half of the damage is recovered between b = 0.05
and 0.15 at t = 120; at t = 500 the criterion changes no bracket. D(0.15) depends on run length and on the
criterion (0.56 and 0.57 at t = 120 and 500 with the first; 0.60 and 0.57 with the second): the threshold at
b = 0.15 falls with run length, which alone would lower D(0.15) by about 0.06 from t = 120 to 500, and
the threshold at b = 0 rests on rare surviving runs. Runs to t = 1000, and runs from the published initial
condition with 15% parasites, are not used for D(0.15): the values they give hinge on single surviving runs
at b = 0. With the lost fate and runs to t = 120, the critical termination is mc = 0.0112–0.0114 at every b: an
unfinished copy then only removes a copying slot. A stop within the first Lcut nucleotides yields nothing, so
that, per copying attempt, τ = 1 − (1 − m)L overstates the probability that the product kept is truncated by a
factor close to L/(L − Lcut ) = 1.11 at every b, a nearly constant factor that cancels in D. The truncated share
of the products actually made is another matter: since short products are made faster when b < 1, it differs
from τ by a factor that depends on b, from 2.35 at b = 0 to 0.90 at b = 1 for small m. We read D on mc , the
critical value of a termination probability m that the lattice and the protocells of Fig. 7A define in the same
way, per nucleotide and per attempt, the timing then weighting each product by θ′ in both; the criteria that fix
the threshold differ (Appendix S9). Read instead on the truncated share of the products made from replicase
templates, the same function of m and b in both models, D(0.15) is 0.61 on the published lattice and 0.63 on
the reimplemented one, and 0.08–0.17 in these protocells (n = 80 to 20): the contrast holds on either axis.
Round-18.

Its processivity coefficient P, the probability of adding a nucleotide before releasing the prod-

uct, varies about twentyfold with the position on the template, up to 0.9, and is 0.25 at the position where its
rate constants were bounded 46 . A polymerase that releases its product at position i with probability 1 − Pi
dissociates (1 − Pi )/Pi times there, on average, so that δ, the mean of (1 − Pi )/Pi along the template, is at
least (1 − P̄)/P̄ for the mean P̄ (the function 1/P is convex), and b ≤ 1/[1 + L(1 − P̄)/P̄] (Methods). With
Pi ≤ 0.9 everywhere, b ≤ 0.083 at L = 100; if P̄ were 0.25, b ≤ 0.0033.

65


[page 66]
S11. QT45 and termination
Table S6 gives the per-nucleotide fidelity a 45-nucleotide, 53.2-bit replicase with ℓ = 0.56 needs in protocells
of n = 20 (θ = 1, R = ∞; 0.977 without termination), when copies stop at each nucleotide with probability m,
products shorter than 10 nucleotides are lost, and longer ones are replicable truncated copies in two classes
split at θ′ = 2 (θ′ reaches 4.5 at b = 0; the fast class disappears beyond b ≈ 0.36). Retruncation feeds the
fast class from the slow one: at m = 3 × 10−3 it makes b = 0 impossible and b = 0.08 nearly so (99.92%);
at b ≥ 0.5 it lowers the fidelity required slightly. The largest stop probability, 2.95 × 10−2 per nucleotide, is
illustrative, of the order of the termination probability per incorporation reported for the tC9Y polymerase on
favourable templates, 0.012–0.025 (ref. 47): a copy of 45 nucleotides then stops early three times out of four,
and no fidelity suffices. QT45 copies with a per-nucleotide fidelity of 0.941. The row “1, with retruncation”
is identity (iii) of Appendix S8: 1 − ε = 1 − [ln 2 − 35(− ln(1 − m))]/(ℓI), with 35 = 45 − 10, to the rounding
shown, and no fidelity suffices for m ≥ 1 − 2−1/35 = 0.0196. By Theorem 2 with termination (Appendix S8),
no row and no protocell size can require a lower fidelity.
Table S6 | Per-nucleotide fidelity (%) required of a 45-nucleotide, 53.2-bit replicase with ℓ = 0.56 (n = 20, θ = 1,
R = ∞; “—”: no fidelity suffices).
b
1
0.5
0.25
0.08
0
1, with retruncation
0.5, with retruncation
0.08, with retruncation
0, with retruncation

m = 3 × 10−4

10−3

3 × 10−3

10−2

2.95 × 10−2

97.71
97.86
97.95
98.01
98.04
97.71
97.86
98.01
98.04

97.80
98.21
98.50
98.64
98.71
97.79
98.19
98.67
98.75

98.08
98.72
99.12
99.24
99.30
98.03
98.63
99.92
—

99.13
99.90
—
—
—
98.85
99.59
—
—

—
—
—
—
—
—
—
—
—

S12. Proofs for the variants
The four notes below give, in English, the proofs and derivations summarized in Appendix S2 (the lever)
and S5 (spontaneous replication, self-copying, protocell fusion). Each completes a note deposited with the
code (S7), whose proofs were checked by an independent session. Status labels are those of S1. To keep
one meaning per symbol in the manuscript, some symbols of the notes are renamed here, word for word: the
fusion rate is k f , the self-copying scaling variable c/y is c̃ and its threshold λcis , and, in S12.1, (λ1 − y)/(1 − y)
is ky ; in S12.4 the rescaled density k f x is x̃; the figures keep κ and Λ.
S12.1. The lever
Scope and status. This note proves how far a division that is not blind to molecular identity can raise the
ceiling of the compartment bonus. Status labels are those of the Appendices. Proved here: the lever in the
limit process (Theorem L1), its form for equal daughters (Corollary L1′ ), the lever at every size and fecundity
(Theorem L3), the exact identity at θ = 1 and R = ∞ (Proposition L7), and attainment by partial sorting at
y = 0 (Theorem L5) and for small y (Theorem L6). Two reservations apply throughout. Dynkin’s formula
for a piecewise-deterministic Markov process 24 , localized at the first passage to a large replicase number,
is used without proof. Lemma H and the independence of the sign of ρ(S (M) ) − 1 from the admissible cut
M (property C4′ ) are taken from the notes deposited with the code (S7), where they are proved and were
66


[page 67]
checked by an independent session. The arguments below follow the deposited note, whose first version was
checked by an independent session.
Limit process and division rules.

The state is (F, u); between jumps u̇ = F − u; F → F + 1 at rate

λF(F − 1)/u, F → F − 1 at rate F, and F ≤ 1 is death; division occurs when u reaches 2y (Appendix S3).
A division rule D gives a protocell that divides with f replicases a random number of daughters; daughter d
P
receives Fd replicases and a fraction αd ∈ (0, 1] of the molecules, d αd = 1, and starts from (Fd , 2yαd ). The
joint law of the daughters may depend on f in any way, so that the rule may treat replicases and parasites
differently. Write h(F) = F(F − 1), φa (F) = Γ(F − 1 + a)/Γ(F − 1), Z = h(F)u−2λ , and let KD ( f, f ′ ) be the
mean number of daughters of a protocell of type f that reach division with f ′ replicases (types at division,
as in Appendix S3). The lever factor is
MD (λ) = sup
f ≥2

E

−2λ 
d h(F d ) αd

P

h( f )

∈ [0, ∞],

λ∗ (D) = sup{λ ∈ (0, 1) : MD (λ) ≤ 1}.

Since αd ≤ 1, MD is non-decreasing, and as a supremum of continuous functions it is lower semicontinuous,
so that {λ : MD (λ) ≤ 1} = (0, λ∗ ] when it is not empty. As in Appendix S3, λc (y; D) = inf{λ < 1 : ρ(S (M) ) >
1}, with S (M) the Schur reduction of KD onto the types {2, . . . , M} for a cut M beyond which large types drift
down.
Lemma A (proved).

In living states, GZ = −2(1 − λ)Z. The flow contributes −2λZ(F − u)/u; births add

2F to h at rate λF(F − 1)/u, that is +2λFZ/u; deaths remove 2(F − 1) at rate F, that is −2Z; the death from
F = 2 leads to the dead state, where Z = 0. The sum is −2(1 − λ)Z.
Lemma B (one cycle from any starting size; proved). Let y > 0, λ ∈ (0, 1), and a daughter start from
(F0 , u0 ) with F0 ≥ 2 and 0 < u0 < 2y; let τ be the time of division or death. Then τ < ∞ almost surely and
Z τ


E Z(Xτ )1{division} = Z(F0 , u0 ) − 2(1 − λ) E
Z(Xt ) dt.
0

Proof. Let um = min(u0 , 2). Along a living path u ≥ um , since u̇ > 0 whenever u < 2 ≤ F. With
V3 = φ3 (F)u−3λ one has GV3 = 3V3 (λ − F/(F + 1)), which is non-positive for F ≥ F ∗ = λ/(1 − λ) and at
most (3λ − 2)V3 everywhere; on {F < F ∗ }, V3 /Z = (F + 1)u−λ ≤ (F ∗ + 1)u−λ
m . Hence W3 = V3 + C 3 Z, with
C3 = (3λ−2)+ (F ∗ +1)u−λ
m /(2(1−λ)), satisfies GW3 ≤ 0 on the domain. Stopping at t∧τ∧T m , where T m is the
first passage of F to m, Dynkin’s formula gives P(T m ≤ t ∧ τ) ≤ W3 (X0 )(2y)3λ /φ3 (m) → 0: the process does
not explode. W3 (Xt∧τ ) is then a non-negative supermartingale, supt<τ F < ∞, and from any state of {2 ≤ F ≤
m}×[um , 2y] the cycle ends within one time unit with probability bounded below, so that τ < ∞ almost surely.
As Z/V3 ≤ (2y)λ /(F + 1) before τ, Z ≤ εW3 + Cε for every ε > 0, and {Z(Xτ′ )}τ′ ≤τ , over stopping times τ′ ,
R t∧τ∧Tm
is uniformly integrable. Dynkin’s formula and Lemma A give E[Z(Xt∧τ∧Tm )] = Z0 − 2(1 − λ)E 0
Z dt;
letting m → ∞, then t → ∞, concludes, since Z = 0 at death. □
This is Lemma 1 of the note on (H3) deposited with the code, where u0 = y; only um changes.
The loss formula.

At division Z = h( f ′ )(2y)−2λ , and at the start of daughter d, Z = h(Fd )(2yαd )−2λ .

Applying Lemma B to each daughter given the outcome of the division, and taking expectations (all terms

67


[page 68]
are non-negative),
(KD h)( f ) = E

hX

h(Fd ) α−2λ
d

i

− ℓD ( f ),

ℓD ( f ) = 2(1 − λ)(2y) E
2λ

d

h X Z τd
d

i
Z dt ≥ 0.

0

Dead daughters contribute 0 = h(Fd ), and a daughter that receives the whole protocell (αd = 1) divides at
once without loss. ℓD ( f ) > 0 as soon as, with positive probability, a daughter receives Fd ≥ 2 and αd < 1.
At y = 0 (R → ∞, then n → ∞), F − 1 is a Yule process of rate λ in the time ln u, a daughter grows for a time
ln(1/αd ), and h is an eigenfunction of the Yule generator with eigenvalue 2λ: the formula holds with ℓD = 0.
Theorem L1 (the lever; proved). Let y ≥ 0, λ ∈ (0, 1), and MD (λ) ≤ 1. (a) KD h ≤ h, strictly at every
P
type where ℓD ( f ) > 0 or E[ d h(Fd )α−2λ
d ] < h( f ). (b) For every finite set A of types, with B the other types,
P k
P k
KBA has finite entries, and
the series k KBB KBA hA converges, the Schur reduction S (A) = KAA + KAB k KBB
ρ(S (A) ) ≤ max f ∈A (KD h)( f )/h( f ) ≤ 1, strictly if (a) is strict on A; the same holds for every finite principal
truncation of KD . (c) Let Xm be the sum of h over the protocells of the m-th generation that reach division.
(Xm ) is a non-negative supermartingale with E[Xm ] ≤ MD (λ)m X0 . If MD (λ) < 1, or if MD (λ) = 1 and (a) is
strict at every type, the population dies out almost surely. (d) λc (y; D) ≥ λ∗ (D), whatever cut defines λc .
P
Proof. (a) follows from the loss formula and E[ d h(Fd )α−2λ
d ] ≤ MD (λ)h( f ). (b) On B, (a) gives
P
k K h ≤ h − K m h ≤ h for every m, so that the series
KBA hA + KBB hB ≤ hB ; by induction k<m KBB
BA A
B
B
BB B
converges. On A, S (A) hA ≤ KAA hA + KAB hB = (KD h)A ; each entry of S (A) is at most (S (A) hA )(i)/h( j) < ∞,
and the Collatz–Wielandt inequality, valid for any finite non-negative matrix and positive vector without irreducibility, concludes. No drift of large types is used. (c) Given the first m generations, the cycles of the
P
daughters are independent, so that E[Xm+1 | Fm ] = i (KD h)( fi ) ≤ MD (λ)Xm . As h ≥ 2 on living types,
P(Xm > 0) ≤ E[Xm ]/2 → 0 when MD < 1. When MD = 1, Xm takes even integer values and converges
almost surely, hence is eventually constant. Given Xm = ξ > 0, generation m holds at most ξ/2 protocells
with h( fi ) ≤ ξ, a finite set of configurations; for each, E[Xm+1 | ·] < ξ by (a), so that P(Xm+1 , ξ | ·) ≥ δξ > 0
uniformly, and P(Xm = · · · = Xm+ j = ξ) ≤ (1 − δξ ) j . Hence Xm = 0 eventually, almost surely. (d) MD (λ) ≤ 1
for every λ ≤ λ∗ , so that by (b) no such λ belongs to the set whose infimum defines λc . □
The same bound holds for the kernel on types at birth: with g( j) = E j [h( f ′ )1{division}], KD h ≤ h gives
K birth g ≤ g.
Corollary L1′ (equal daughters; proved). For k daughters of fraction 1/k, MD (λ) = k2λ r̄ with r̄ =
P
sup f E[ d h(Fd )]/h( f ), so that λ∗ = min(1, 12 logk (1/r̄)); for two daughters, λ∗ = min(1, 21 log2 (1/r̄)), and the
P
compartment constant is at most ln(1/λ∗ ) = max(0, ln(2/ log2 (1/r̄))). Always r̄ ≤ 1, since d Fd (Fd − 1) =
P 2
2
d F d − f ≤ f − f : a division cannot create pairs. A rule blind to molecular identity, each replicase going to
P
]
daughter d with probability αd given the fractions, has E[h(Fd ) | α] = α2d h( f ), hence MD (λ) = E[ d α2−2λ
d
and λ∗ = 12 for every non-degenerate law of the fractions. Partial sorting, which sends all replicases to one
P
daughter with probability p and partitions at random otherwise, has E[ d h(Fd )] = r̄ h( f ) with r̄ = (1 + p)/2
for every f , and λ∗ (p) = 12 log2 (2/(1 + p)). One bit more, a ceiling b ln 2 with b = log2 (1/λ∗ ), requires
1−b

r̄ = 2−2 : 0.5, 0.7071, 0.8409, 0.9170 for b = 1 to 4.
Theorem L3 (every size and fecundity; proved). In the finite model, let a division rule D, possibly
sensitive to molecular identity, give the daughters (Fd , Nd ). For b > 0 let gb (N) = Γ(N − 1)/Γ(N − 1 + b),

68


[page 69]
V2,b = h(F)gb (N), ωb (N) = gb (N)/gb (2n) =

j=N−1 (1 + b/ j) for N ≥ 2 and 0 otherwise, and

Q2n−2

Gn (Λ; D) = max

E

P

d h(F d ) ω2Λ (Nd )

h( f )

2≤ f ≤2n


.

If Λ ∈ (0, 1] and Gn (Λ; D) ≤ 1, then ρ(K) ≤ 1 for every R ∈ (0, ∞], θ > 0 and q ≤ 1 with max(q, q/θ) ≤ Λ.
With λ∗n (D) the largest such Λ, Uc (n, R, θ; D) ≤ max(0, ln(1/θ)) + ln(1/λ∗n (D)).
Proof. Let b = 2Λ. In a transient state, the copying term of the generator of V2,b is RF V2,b [2(N −
1)p/(F − 1) − b]/(N − 1 + b), and losses contribute −(2 − b)V2,b for N ≥ 3 and −2V2,b at F = N = 2
(Appendix S2, “Supermartingales at every fecundity”). As W = (F − 1) + θ(N − F) ≥ min(1, θ)(N − 1),
p ≤ max(q, q/θ)(F − 1)/(N − 1) ≤ Λ(F − 1)/(N − 1), so that the copying term is non-positive; the losses
are non-positive because Λ ≤ 1. At R = ∞ the mean change of V2,b at each copy is non-positive. The
chain of a daughter is finite and absorbed almost surely, and V2,b is bounded, so that optional stopping
gives gb (2n)E x [h( f ′ )1{division}] ≤ V2,b (x); a daughter that receives all 2n molecules is already at division.
P
Summing over daughters, (Kh)( f ) ≤ E[ d h(Fd )ωb (Nd )] ≤ Gn (Λ)h( f ) ≤ h( f ), and Collatz–Wielandt gives
ρ(K) ≤ 1. Since ωb increases with b, Gn is non-decreasing in Λ, and Λ ≤ λ∗n is equivalent to U ≥ ln(1/λ∗n ) +
max(0, ln(1/θ)). □
At Λ = 21 , ω1 (N) = (2n − 1)/(N − 1) and Gn ( 12 ; D) is the factor by which division multiplies the expected
summed pair density ϕ = F(F − 1)/(N − 1): this is the bound for division blind to molecular identity
(Appendix S2). For binary binomial partition, Gn (Λ) = cn (Λ) and ln(1/λ∗n ) = un at θ = 1 (Appendix S2).
P
With two daughters of fixed size n, Gn (Λ) = g ω2Λ (n)/ω1 (n), where g = max f E[ d ϕd ]/ϕ, and λ∗n →
1
2 (1 − log2 g) as n → ∞. No function of g alone bounds the threshold when daughters differ in size: sorting

all replicases into a daughter of 9 of 12 molecules has g = 1.375 and remains supercritical at every load
computed at infinite fecundity (numerical).
Proposition L7 (exact identity at θ = 1 and R = ∞; proved).

At θ = 1, p = q(F − 1)/(N − 1), so that the

copying term above vanishes for b = 2q: V2,2q is a martingale during growth, there are no losses, and every
P
daughter with Fd ≥ 2 reaches division. Hence, for every rule, (Kh)( f ) = E[ d h(Fd )ω2q (Nd )] exactly, and
ρ(K) ≤ Gn (q; D), with equality when this ratio does not depend on f , as for every rule blind to molecular
identity. For the finite partial sorting (with probability p two daughters of n molecules, the first receiving
min( f, n) replicases; binomial partition otherwise), (Kh)( f ) = [p ω2q (n)sn ( f )+(1− p)cn (q)]h( f ), with sn ( f ) =
1 for f ≤ n and sn ( f ) = [h(n) + h( f − n)]/h( f ) < 1 beyond, so that Gn (q; p) = p ω2q (n) + (1 − p)cn (q); the
exact kernels confirm the identity to 2 × 10−13 (numerical check).
Theorem L5 (attainment at y = 0; proved). Let K0 be the kernel of partial sorting at y = 0 (partition,
then F − 1 a Yule process of rate λ during ln 2), p ∈ [0, 1), r̄ = (1 + p)/2, Ψλ (a) = p 2λa + (1 − p) 21−a(1−λ)
and λ3 (p) = 31 log2 (4/(1 + 3p)), the root of Ψλ (3) = 1. (a) K0 h = 4λ r̄ h for every λ. (b) For λ ∈ (0, λ3 (p))

the kernel has an admissible cut with weight φ3 , and for λ ∈ (λ∗ (p), λ3 (p)), ρ(S (M) ) ≥ 4λ r̄ > 1. (c) Hence
λc (0; p) = λ∗ (p).

Proof. (a) h(F) = ν(ν + 1) with ν = F − 1 is an eigenfunction of the Yule generator with eigenvalue
2λ, and the partition keeps r̄ h( f ) in expectation. (b) Likewise φ3 = ν(ν + 1)(ν + 2) has eigenvalue 3λ;
with φ3 = (F)3 + 3(F)2 and E[(B)i ] = ( f )i 2−i for B ∼ Bin( f, 21 ), binomial partition gives 2E[φ3 (B)] =
f ( f − 1)( f + 4)/4, and sorting gives φ3 ( f ). Hence (K0 φ3 )( f ) = 23λ φ3 ( f )[p + (1 − p)( f + 4)/(4( f + 1))],

69


[page 70]
∗

whose ratio to φ3 ( f ) tends to Ψλ (3). At λ∗ , 23λ = r̄−3/2 and Ψλ∗ (3) = 41 (1 + 3p)r̄−3/2 < 1 if and only if
2(1 + p)3 − (1 + 3p)2 = (1 − p)2 (1 + 2p) > 0, true for p < 1; Ψλ (3) increases with λ, so that λ∗ < λ3 , and
for λ < λ3 there are β < 1 and M with K0 φ3 ≤ βφ3 beyond M, while K0 φ3 ≤ 23λ φ3 everywhere; φ3 ≥ h. For
λ ∈ (λ∗ , λ3 ), K0 h = (1 + η)h with 1 + η = 4λ r̄ > 1, and Lemma H gives ρ(S (M) ) ≥ 1 + η. (c) follows with
Theorem L1. □
The h-transformed chain, which follows the protocell carrying a marked pair, satisfies Eh [F ′ | F = f ] =
f
2p
∗
λ
∗
( f + 1) + 1−p
2λ [ 1+p
1+p ( 2 + 2)] − 1; at λ its slope in f is Ψλ (3) < 1, so that it is positive recurrent and 4 r̄ is

also the convergence parameter of K0 , as for random partition (Appendix S1) 43,44 .
Theorem L6 (small fecundity cost; proved). For 0 < y < 1 and p ∈ [0, 1), let y3 (p) = (λ3 − λ∗ )/(1 − λ∗ ).
If y < y3 (p), then λ∗ (p) ≤ λc (y; p) ≤ λ∗ (p) + y(1 − λ∗ (p)); in particular λc (y; p) → λ∗ (p) as y → 0. The
√
values of y3 are 1/3, 0.1143, 0.0377, 0.0126 and 0.0070 for p = 0, 0.2, 2 − 1, 0.6 and 23/4 − 1.
Proof. The lower bound is Theorem L1. Let λ1 ∈ (λ∗ + y(1 − λ∗ ), λ3 ) and ky = (λ1 − y)/(1 − y).
For y < 1, u increases along every living path and serves as a clock on [y, 2y], in which h has generator
2h(λF − s)/(s(F − s)) ≥ (2ky /s)h for F ≥ 2 and s ≤ 2y; hence a daughter started at ( j, y) has E[h(F2y )] ≥
22ky h( j), and (Kh)( f ) ≥ 4ky r̄ h( f ), with 4ky r̄ > 1 because ky > λ∗ . The function φ3 (F)u−3λ has generator
3φ3 u−3λ (λ − F/(F + 1)) ≤ 0 for λ ≤ 32 , so that E[φ3 ( f ′ )1{division}] ≤ 23λ φ3 ( j) (Fatou), and the partition
gives the drift of Theorem L5 with ratio tending to Ψλ1 (3) < 1. Lemma H then gives ρ(S (M) ) ≥ 4ky r̄ > 1, so
that λc ≤ λ1 . □
What is not proved.

That the finite thresholds converge to max(0, ln(1/θ) + ψ(y; D)) for a rule other than

binomial partition; that λc (y; D) > λ∗ (D) strictly for y > 0; the upper bound of Theorem L6 beyond y3 (p);
and, for partial sorting, the bound λc (y; p) ≤ λL (p) at every y from replicase-rich protocells, with λL (p) the
root of inf a≥0 Ψλ (a) = 1 (derived from a branching random walk on ln F). Beyond λ3 (p) no admissible cut
is proved for partial sorting; there λc should be read as inf{λ : supA ρ(K (A) ) > 1} over finite truncations, for
which Theorem L1 holds unchanged.
S12.2. Spontaneous replication
Setting. We add to the model of the main text a copy made without a catalyst. Every molecule is copied
spontaneously at rate s per lifetime; the copy of a replicase is a replicase with probability q s , and a parasite
otherwise; the copy of a parasite is a parasite. We write χ = sq s for the number of correct uncatalysed copies
of a replicase per lifetime. In a protocell with F replicases and Q parasites, N = F + Q and W = (F − 1) + θQ,
the rates are: F → F + 1 at RFq(F − 1)/W + χF; Q → Q + 1 at RF[(1 − q)(F − 1) + θQ]/W + s(1 − q s )F + sQ;
F → F − 1 at F and Q → Q − 1 at Q (catalysed copies vanish when W = 0). A protocell with one replicase
is now alive; one with none is dead and is not counted. Division at 2n molecules is binomial, and the type of
a protocell is its number f ∈ {1, . . . , 2n} of replicases at division. K is the mean matrix of living daughters,
K = BH + 21−2n I as in the Methods, and Uc = sup{U : ρ(K) > 1}, with q = e−U and either q s = q or q s fixed;
the sign of ρ − 1 is that of the Malthusian parameter 42 .
Proposition 1 (no threshold when χ ≥ 1; proved, every size and fecundity).

For every n ≥ 2, R ∈ (0, ∞),

θ > 0 and q ∈ (0, 1], if χ ≥ 1 then ρ(K) > 1. Hence there is no threshold when q s is fixed and sq s ≥ 1, and
Uc ≥ ln s when q s = q and s > 1.
70


[page 71]
Proof. Let h(F) = F, with F = 0 at death. On transient states the generator of the chain within a protocell
gives Gh = F(Rp + χ − 1), where p = q(F − 1)/W (p = 0 if W = 0) is the probability that a catalysed copy
makes a replicase. For χ ≥ 1, Gh ≥ RF p ≥ 0, with strict inequality when F ≥ 2, since then W ≥ 1 and q > 0.
Let τ be the time of division or death. The chain is finite and death is possible from every state, so τ < ∞
almost surely and Eτ < ∞; Dynkin’s formula gives, from every transient state x,


E x F ′ 1{division} = F(x) + E x

Z τ
Gh dt ≥ F(x),
0

where F ′ is the number of replicases at division. The inequality is strict if F(x) ≥ 2, because the chain stays
a positive time in x. It is also strict if F(x) = 1: with χ > 0, the chain reaches a transient state with F = 2
before τ with positive probability (from N = 2n − 1, a parasite may first die), which requires n ≥ 2. At
division, the expected number of replicases summed over the daughters is f ; daughters without replicase
count for 0, and the daughter that receives all molecules is at division at once with f replicases. For every
f ≥ 1, a transient daughter with at least one replicase occurs with positive probability. Hence (Kh)( f ) > h( f )
for f = 1, . . . , 2n. K is a finite non-negative matrix and h > 0, so the Collatz–Wielandt inequality gives
ρ(K) ≥ min f (Kh)( f )/h( f ) > 1, without irreducibility. With q s = q, χ = se−U ≥ 1 for U ≤ ln s. □
When n, R → ∞ at fixed y = n/R and fixed s, with

The limit process and the pair density (derived).

u = N/R, the process of Appendix S3 becomes: u̇ = F − (1 − s)u; F → F + 1 at rate λF(F − 1)/u + χF,
λ = q/θ; F → F − 1 at rate F; division at u = 2y. For Z = F(F − 1)u−2λ and F ≥ 2, the generator gives
GZ = −2[1 − λ(1 − s)]Z + 2χZF/(F − 1), and GZ = 2χu−2λ > 0 = Z at F = 1. The pair density vanishes
on a living type that feeds the others, so that the argument of the ceiling (Theorem 2; Appendices S2–S3) no
longer applies.
The reduced kernel at y → 0 (derived). As y → 0, the cycle of a protocell with F ≥ 2 lasts a time O(y),
during which deaths and spontaneous copies have probability O(y); in the clock ln u, F − 1 is a Yule process
of rate λ, which gives the limit kernel B∞ of Theorem 1. A lone replicase, in contrast, stays alone for an
exponential time of rate 1 + χ, whatever y; its protocell keeps growing, at u̇ = 1 + O(y), and divides about
1/[(1 + χ)y] times, the replicase passing to one daughter each time. It is revived, to two replicases, with
probability ε = χ/(1 + χ), at a size u = y(1 + V) with V uniform on [0, 1]. Reducing the lone-replicase type
(its weights per cycle are 1 − (1 + χ)τ1 for itself and χτ1 for revival, τ1 ≃ y) gives the kernel on types at
division f ≥ 2
Kχ = B∞ + ε e ⊗ r,

e( f ) = 2 f 2− f ,

where e( f ) is the mean number of daughters with one replicase, and r( f ′ ) = P(1 + ν(T ) = f ′ | ν(0) = 1) for
a Yule process ν of rate λ run for T = ln[2/(1 + V)]; ν(T ) is geometric with parameter ((1 + V)/2)λ . The
Schur reduction preserves the sign of ρ − 1 (Appendix S2). We write λc (0; χ) for the threshold of Kχ and
ψ(0; χ) = − ln λc (0; χ). That λc (y; χ) → λc (0; χ) is numerical: the limit process converges linearly in y to the
value of Kχ , not to that of a revived protocell treated as newborn.
Lemma (subsolution).

Let K ≥ 0 act on types f ≥ 2, A = {2, . . . , M}, B the larger types, and S =

KAA + KAB (I − KBB )−1 KBA the Schur reduction. Suppose w > 0 satisfies KBB wB ≤ βwB with β < 1, and that
v ≥ 0, non-zero on A, satisfies v ≤ w and Kv ≥ (1 + η)v with η > 0. Then ρ(S ) ≥ 1 + η.

71


[page 72]
Proof. Let t = 1/(1 + η), so that v ≤ tKv. On B, iterating m times, vB ≤

P

k<m (tK BB )

k tK

BA vA + (tK BB )

mv ,
B

and the last term is at most (tβ)m wB → 0. On A, vA ≤ tKAA vA + tKAB vB ≤ S (t)vA with S (t) = tKAA +
P
k+2 K K k K
AB BB BA ≤ tS . By Collatz–Wielandt, ρ(S (t)) ≥ 1, hence ρ(S ) ≥ 1/t = 1 + η. □
k≥0 t
Proposition 2 (no threshold when χ ≥ 1; proved for the reduced kernel). For χ ≥ 1 and every λ ∈ (0, 1),
ρ(S ) ≥ 1 + (2λ − 1)/4 for every admissible cut M.
Proof. Let h1 ( f ) = f and S f ( j) = 2P(Bin( f, 21 ) = j). A daughter with j ≥ 2 replicases divides with

1 + ( j − 1)2λ replicases on average; a daughter with one replicase gives ε E[1 + ν(T )] ≥ 2ε ≥ 1, since ε ≥ 12 .
P
P
With j S f ( j) j = f and j≥2 S f ( j)( j − 1) = f − 2 + 21− f ,

(Kχ h1 )( f ) ≥ f + (2λ − 1)( f − 2 + 21− f ) ≥ 1 + (2λ − 1)/4 f,

f ≥ 2.

For the drift, let φa ( f ) = Γ( f − 1 + a)/Γ( f − 1) with an integer a > 1/(1 − λ). It is an eigenfunction of the Yule
generator in ν = f − 1 with eigenvalue aλ, and φa (0) = φa (1) = 0, so that B∞ φa ( f ) = 2 · 2aλ E[φa (Bin( f, 12 ))],
whose ratio to φa ( f ) tends to 21−a(1−λ) < 1; the added term εe( f )⟨r, φa ⟩ = O( f 2− f ) is negligible. Hence
w = Cφa , with C large enough that w ≥ h1 , satisfies the drift beyond some M, and the Lemma applies with
v = h1 . □
Proposition 3 (the ceiling is pierced at every χ > 0; proved for the reduced kernel).

Let λ ∈ (0, 12 ),

ρ0 = 22λ−1 , h( f ) = f ( f − 1) and
D X
E
G(λ) = r,
Bm
∞e ,
m≥0

the mean number of daughters with one replicase in the tree of B∞ alone (without revivals) issued from a
revived protocell. Then: (a) G(λ) < ∞; Kχ is supercritical if εG(λ) > 1 and subcritical if εG(λ) < 1, so that
at threshold χ = 1/(G(λ) − 1). (b) G(λ) → ∞ as λ ↑ 21 , and Kχ is supercritical at λ = 12 ; hence λc (0; χ) < 12
and ψ(0; χ) > ln 2 for every χ > 0. (c) G is continuous on [0, 21 ) with G(0) = 2; hence λc (0; χ) > 0 for χ < 1.
P m
m
Proof. (a) B∞ h = ρ0 h (Appendix S1) and e ≤ 1 ≤ h/2 on f ≥ 2, so Bm
m B∞ e ≤
∞ e ≤ ρ0 h/2, x :=
h/[2(1 − ρ0 )] and G ≤ ⟨r, h⟩/[2(1 − ρ0 )] < ∞. Supercriticality: for A = {2, . . . , M} let G M = ⟨rA , (I −
B∞,A )−1 eA ⟩, which increases to G by monotone convergence; ρ(B∞,A ) ≤ ρ0 < 1 by Collatz–Wielandt. Since
det(I − B∞,A − t eA rA⊤ ) = det(I − B∞,A )(1 − tG M ), the continuous function t 7→ ρ(B∞,A + t eA rA⊤ ), below
1 at t = 0 and unbounded, equals 1 only at t = 1/G M and exceeds 1 beyond. If εG > 1, take M with
εG M > 1: the process restricted to types ≤ M is a finite supercritical branching process, and so is the full
one. Subcriticality: let v = h + tx; since B∞ x = x − e and ⟨r, x⟩ = G,
Kχ v = ρ0 h + tx + e [ε⟨r, h⟩ − t(1 − εG)].
If εG < 1 and t > ε⟨r, h⟩/(1 − εG), the bracket is negative; with x ≤ Ch, C = 1/[2(1 − ρ0 )], this gives
Kχ v ≤ βv for β = (ρ0 + tC)/(1 + tC) < 1, and the expected number of protocells decays geometrically. (b)
P
43,44 ;
At λ = 12 , ρ0 = 1 and the h-transformed chain is positive recurrent (Appendix S1), so m Bm
∞ (2, 2) = ∞
as r(2) > 0 and e(2) = 1, G( 21 ) = ∞. Each entry of B∞ (λ)m is a sum over paths of non-negative weights
continuous in λ, so Fatou’s lemma gives lim inf λ↑1/2 G(λ) = ∞, and (a) applies near 12 . At λ = 12 itself, all
entries of B∞ are positive, so ρ(B∞,A ) < 1 and G M < ∞ for every M, while G M → ∞. (c) For λ ≤ λ1 < 21 ,
m
⟨rλ , Bm
∞ e⟩ ≤ 2ρ0 (λ1 ) , since ⟨rλ , h⟩ ≤ 4, and dominated convergence gives continuity. At λ = 0 there are no

72


[page 73]
catalysed births: a revived protocell divides with two replicases, and a division with two replicases gives on
average one daughter with one replicase and half a daughter with two, which divides again with two; hence
P
G(0) = m 2−m = 2, and εG(0) = 2χ/(1 + χ) < 1 for χ < 1. □
That G increases with λ, so that the threshold is unique, is numerical (checked on a grid of 499 points).
Proposition 3(b) does not need it: a supercritical λ < 21 suffices for Uc > ln 2.
√
f
First order (derived). At λ = 21 the left eigenvector of B∞ is π0 ( f ) = r0 , r0 = 2 − 2 (Appendix S1), and
√
√
⟨π0 , e⟩ = 2 − 2, ⟨π0 , h⟩ = 4 + 4 2, ⟨r, h⟩ = 2 E[2/(1 + V)] = 4 ln 2. The rank-one perturbation ε e ⊗ r moves
√
the simple eigenvalue 1 by ε⟨π0 , e⟩⟨r, h⟩/⟨π0 , h⟩ = ε(3 2 − 4) ln 2, and ∂ρ0 /∂λ = 2 ln 2, so that
√
ψ(0; χ) = ln 2 + (3 2 − 4) χ + O(χ2 ).
√
What is missing for a proof is the limit (1 − ρ0 ) G(λ) → (3 2 − 4) ln 2 as λ ↑ 21 , supported numerically
√
(0.16850 at λ = 0.4999, against 0.16819). The slope in y is −(3 2 − 4)/ ln 2 (Appendix S3), so that to first
√
order ψ ≈ ln 2 + (3 2 − 4)(χ − y/ ln 2).
The model of Bianconi et al. 15 : χeff = q (derived).

In R2α, a replicase in a cell with i replicases replicates

at rate 1 + (i − 1)α and every other sequence at rate 1 + iα; sequences are not degraded, and a replicase is
selected if cells that contain replicases outgrow parasite-only cells, whose sequences replicate at rate 1. We
compute this criterion as the spectral radius of the kernel discounted at the Malthusian rate 1, which acts as
a removal rate w = 1 on every cell. A cell with a lone replicase keeps growing, since its parasites are copied
at rate 1 + α, and passes the replicase to one daughter at each division; the replicase is copied correctly at
rate q and the lineage is removed at rate w = 1. It is therefore revived with probability q/(1 + q): in our
units, χeff = q. Two differences remain. Catalysis by mass action makes the cell with a lone replicase grow
exponentially, so that revival occurs at a stage uniform in ln N; we write ψlog for the limit of the corresponding
√
reduced kernel, in which T is uniform on [0, ln 2], with slope (3 2 − 4)/(2 ln2 2). At α → ∞ the jump chain
of a cell with i ≥ 2 replicases is ours, so that for α → ∞ and m → ∞ with α ≪ 2m the threshold is the root of
U = ψlog (0; e−U ), U ∗ = 0.903 (derived; the root is computed on the reduced kernel). The condition α ≪ 2m
excludes the singular regime in which a lone replicase, left alone in a daughter of one molecule, waits there
and refounds cells made of replicases only.
S12.3. Self-copying, total or partial
Model.

A protocell holds F replicases among N molecules. Each replicase starts copies at rate R and

chooses its template among the N molecules with weight c ≥ 0 for itself, 1 for each of the F − 1 other
replicases and θ for each parasite; a copy of a replicase template is a replicase with probability q = e−U . The
next molecule made is therefore a replicase with probability
pc (F, N) =

q (F − 1 + c)
≤ q.
(F − 1 + c) + θ(N − F)

Molecules decay at rate 1, protocells divide at 2n molecules by binomial partition, and F = 0 is dead; F = 1
is alive when c > 0. The case c = 0 is the model of the main text, c = 1 the self-copying variant of
Appendix S1. In the limit process (n, R → ∞ at fixed y = n/R, u = N/R), u̇ = F − u, F → F + 1 at rate
λF(F − 1 + c)/u with λ = q/θ, F → F − 1 at rate F, and division occurs at u = 2y into two daughters at u = y
73


[page 74]
with Bin(F, 12 ) replicases. For a function g(F, u) vanishing at F = 0 its generator is
Gg = (F − u) ∂u g +

λF(F − 1 + c)
[g(F + 1) − g(F)] + F [g(F − 1) − g(F)].
u

K denotes a mean matrix of living daughters, ρ its spectral radius, and λc (y; c), ψ(y; c) = − ln λc are defined
from the Schur reduction of the limit kernel onto small types, as in Appendix S3. We write ℓy = ln[(1 −
y)/(1 − 2y)] for y < 12 .
A. No threshold at infinite fecundity (proved). Let n ≥ 1, θ > 0, c > 0 and 0 < q < 1. At R = ∞ nothing
decays, so F never decreases during growth, and a daughter that receives at least one replicase reaches
division alive. The row sums of K (types at division f = 1, . . . , 2n) are therefore 2(1 − 2− f ): one for f = 1
and at least 23 for f ≥ 2. K is irreducible: from any f , a daughter receives a single molecule, a replicase,
with probability f 2−2n > 0, and from (F, N) = (1, 1) successful copies (pc > 0) and failed ones (pc < 1)
lead to division at any type f ′ ∈ {1, . . . , 2n}. The spectral radius of an irreducible non-negative matrix lies
strictly between its smallest and largest row sums unless they are all equal 44 , so ρ > 1 at every load, and
Uc (n, ∞, θ; c) = +∞. At c = 0, by contrast, Uc stays below max(0, ln(1/θ)) + ln 2 at every size and fecundity:
the limits R → ∞ and c → 0 do not commute. At finite fecundity the threshold is finite, Uc ≤ ln R, since
new replicases appear at rate RF pc ≤ RFq while replicases decay at rate F.
A′ . An exact eigenvector (proved).

At R = ∞, θ = 1 and c = 1, p = qF/N. For V = F Γ(N)/Γ(N + q) one

copy gives E[V ′ ] = F(1+q/N) Γ(N +1)/Γ(N +1+q) = V, so V is a martingale over the fixed number of copies
that bring a daughter to 2n molecules, and a daughter (Fd , Nd ) divides with E[ f ′ ] = V(Fd , Nd ) Γ(2n+q)/Γ(2n).
Given Nd , Fd is hypergeometric with E[Fd | Nd ] = f Nd /(2n); empty daughters count zero and the daughter
that receives everything is already at division. Hence KF = ρn (q)F with
ρn (q) =

Γ(N1 + 1) i
Γ(2n + q) h
,
E 1{N1 ≥ 1}
n Γ(2n)
Γ(N1 + q)

N1 ∼ Bin(2n, 12 ),

and, F being a positive eigenvector of an irreducible matrix, ρ = ρn (q). Since Γ(2n + q)/Γ(2n) ∼ (2n)q ,
Γ(N + 1)/Γ(N + q) ≤ CN 1−q and N1 /n → 1, dominated convergence gives ρn (q) → 2q , the eigenvalue of
Appendix S1 at θ = 1. At U = 10, ρn − 1 = 3.126 × 10−5 for n = 3 and 3.147 × 10−5 for n ≥ 10.
B. First-order identity (proved). For Vb = F u−b (zero at F = 0), a birth adds u−b , a death removes it,
including the death of a lone replicase, and the flow contributes −bFVb /u + bVb ; hence, for every F ≥ 1,
GVb = Vb

h λ(F − 1 + c) − bF
u

i
+b−1 .

With b = λc, GV = V[λ(1 − c)(F − 1)/u − (1 − λc)]: a lone replicase decays at exactly the rate 1 − λc,
and for c ≤ 1 trans copying only adds. With c = 1 and b = λ, Z1 = Fu−λ satisfies GZ1 = −(1 − λ)Z1 in
every state, and since partition conserves F while u returns from 2y to y, a division multiplies Z1 , summed
over daughters, by exactly 2λ . This is the exact analogue of the pair density of Appendix S3, whose factors
2(1 − λ) and 22λ−1 become 1 − λ and 2λ .

74


[page 75]
C. Second-order identity (proved). Let g(F) = (F + c − 1)(F + c) and Zc = g(F)u−2λ for F ≥ 1, Zc = 0
at F = 0. A birth adds 2(F + c)u−2λ , at rate λF(F − 1 + c)/u, which cancels the term −2λFZc /u of the flow;
a death removes 2(F + c − 1)u−2λ if F ≥ 2, and all of Zc if F = 1. Hence
h
2F i
GZc = Zc 2λ −
F+c

GZc = (2λ − 1)Zc

(F ≥ 2),

(F = 1).

For a quadratic g = F 2 + αF + β, the terms in 1/u are λF[(2c − 1 − α)F + (c − 1)(1 + α) − 2β]u−2λ−1 ,
which vanish identically only for α = 2c − 1, β = c(c − 1): g is unique. Partition does not close it: for
B ∼ Bin( f, 12 ), 2E[g(B); B ≥ 1] = f ( f − 1)/2 + 2c f + 2c(c − 1)(1 − 2− f ), so that 2E[g(B); B ≥ 1] − g( f )/2 =
c[ f + (c − 1)( 23 − 21− f )] > 0 for c > 0 and f ≥ 1; the partition factor lies in ( 12 , 1] and equals 1 at f = 1. At
c = 0 it is 21 and the identity of Appendix S3 is recovered.
Lemma D. Drift of large types for y < 12 (proved).

Let y < 12 , c > 0, λ < 1, an integer a > max(2, 1/(1 −

λ)), φ(F) = Γ(F − 1 + c + a)/Γ(F − 1 + c) for F ≥ 1 (a polynomial of degree a with leading coefficient
1) and w = φ + 1. Then for every β ∈ (21−a(1−λ) , 1) there are M and C with Kw ≤ βw beyond M and
Kw ≤ Cw everywhere. Indeed V = φ(F)u−λa satisfies GV = V[λa − h(F)] with h(F) = aF/(F − 2 + c + a)
for F ≥ 2 and h(1) = 1; h increases to a > λa, so GV ≤ γV 1{F < F ∗ } with γ ≤ λa. Along a living
lineage u̇ ≥ 1 − u > 0, so u ∈ [y, 2y] and a cycle ends within ℓy ; in the clock s = u births are at most
linear in F, so all moments are finite. Dynkin’s formula for this piecewise-deterministic process 24 gives
E[φ( f )1{div}] ≤ 2λa [φ(F0 ) + C0 PF0 (min F < F ∗ )], and the replicases present at birth that survive until ℓy
remain present throughout, so the last probability is at most P(Bin(F0 , e−ℓy ) < F ∗ ), exponentially small in
F0 . Factorial moments give E[φ(B); B ≥ 1] = 2−a f a + O( f a−1 ), hence (Kφ)( f )/φ( f ) → 21−a(1−λ) < 1, and
K1 ≤ 2. With this drift, λc (y; c) is defined and the sign of ρ − 1 for the Schur reduction does not depend on
the admissible cut.
Two tools. (H) If Kw ≤ βw on the large types B with w ≥ 1, β < 1, and Kv ≥ γv for some v ≥ 0, v ≤ Cw,
non-zero on the small types A, with γ > 1, then the Schur reduction S onto A has ρ(S ) ≥ γ: with t = 1/γ,
P
iterating v ≤ tKv on B gives vB ≤ k (tKBB )k tKBA vA , so vA ≤ S (t)vA ≤ tS (1)vA , and the Collatz–Wielandt
inequality 44 concludes. Conversely, if h > 0 and Kh ≤ h, then ρ ≤ 1 for every finite truncation and every
Schur reduction that exists.
B1. A lone replicase must replace itself (proved for y < 21 ). Let y < 12 and 0 < c ≤ 1. By B, V = Fu−λc
satisfies GV ≥ −(1 − λc)V, so e(1−λc)t V is a submartingale, zero at death. Cycles last at most ℓy and moments
are finite (Lemma D), hence E[V(τ)1{div}] ≥ e−(1−λc)ℓy V(0). With V = f (2y)−λc at division, V = Fb y−λc at
birth and partition conserving F, KF ≥ γ1 F with γ1 = 2λc e−(1−λc)ℓy . By (H) with v = F ≤ w, ρ > 1 as soon
as λc(ln 2 + ℓy ) > ℓy :
λc (y; c) ≤

ℓy
.
c(ln 2 + ℓy )

Rℓ
Since 0 y dt/u(t) = ln 2 + ℓy along the path of a lone replicase, the condition says that its expected number
of successful copies of itself over a cycle exceeds its cumulated death intensity. For c > 1, V = Fu−λ
satisfies GV/V ≥ λ(c − 1)/(2y) + λ − 1, and the same argument applies. For every c ≥ 0, the proof of the
bound (1 + y)/2 of Appendix S3 carries over, cis copies only adding births and F(F − 1) vanishing at F = 1:
λc (y; c) ≤ (1 + y)/2.
75


[page 76]
B2. A supersolution (proved; for y ≥ 12 , for every truncation and every Schur reduction that exists).
Let y > 0, c > 0, um = min(y, 1), λ < 21 with a = λ(1 + c) < 12 , b = 2 − 4a, and β ≥ 0 such that (i)
λc(um + 2βy) ≤ u2m , (ii) β(3 − 6λ − 2λc + 2y) ≥ 2λ, and (iii) β ≥ maxu∈[um ,2y] u(a − u)/[y(b + u)]. For
H = F + βyF(F − 1)/u, a direct computation gives
u
βy
GH = q(F, u) = λ(F − 1 + c) − u +
[2λF(F − 1 + c) − F(F − 1)] − βy(F − 1).
F
u
Here q(1, u) = λc(1 + 2βy/u) − u ≤ 0 on [um , 2y] by (i); the coefficient of F 2 in uq is βy(2λ − 1) < 0, so q is
concave in F, and with B = βy/u, ∂F q(2, u) = λ−B(3+u−6λ−2λc) ≤ 0 by (ii) and q(2, u) = a−u−B(b+u) ≤ 0
by (iii). A living lineage stays in {F ≥ 1, um ≤ u ≤ 2y}, where GH ≤ 0; H ≥ F excludes explosion, the
P
cycle ends almost surely, and Fatou’s lemma gives E[H(Xτ )1{div}] ≤ H(Fb , y). Since E[ d H(Fd , y)] =
f + β f ( f − 1)/2 = H( f, 2y), the kernel on types at birth satisfies Kh ≤ h for h = F + βF(F − 1) (on types at
division, h = f + β2 f ( f − 1)), so ρ ≤ 1. The conditions are monotone in λ, hence λc (y; c) ≥ λ∗ (y, c), the largest
admissible λ. Condition (i) gives λ∗ ≤ y/c, and the smallest β allowed by (ii) and (iii) is O(λ + λ2 (1 + c)2 /y),
so λ∗ = (y/c)[1−O(y(1+c)2 /c2 )]. For y ≥ 12 no drift is proved, so λc is defined there only through truncations,
on which the bound holds.
F. No threshold at high fecundity (proved). For fixed 0 < c ≤ 1, B1 and B2 give, as y → 0,
ln

 y(1 + c)2 
c ln 2  1
3
c
,
+
− y + O(y2 ) ≤ ψ(y; c) ≤ ln + O
y
ln 2 2
y
c2

using ℓy = y + 32 y2 + O(y3 ): ψ → ∞, logarithmically. The constants diverge as c → 0, which is again the
non-commutation of the limits.
What is not proved. The scaling λc (y; c̃y) → λcis (c̃), with λc̃ ln 2 [G(λ) − 1] = 1, is derived to first order in
y, its remainders being uncontrolled near λ = 21 ; the closed form λcis ≈ 1/[1 + (1 + c̃2 ln2 2)1/2 ] is a numerical
approximation; for y < 21 , hypothesis (H2) and the decrease of λc in c follow from the size-clock coupling
of Appendix S3 but are not written out; for y ≥ 12 the drift is not proved; and for c > 0 the convergence of
the finite thresholds Uc (n, n/y, θ) to max(0, ln(1/θ) + ψ(y; c)) is only numerical, as 1/n at most values of y for
θ ≥ 1 but more slowly at y = 21 , at y = 1 for c = 1, and for θ < 1.
S12.4. Protocell fusion
Scope. The thresholds of the main text are invasion thresholds, for protocells that neither fuse nor compete.
Here protocells fuse. Fusion between protocells leaves Uc unchanged; no fusion raises it above the ceiling,
and fusion with vesicles that carry parasites can lower it. Fusion can at most let an already dense population
persist beyond Uc , which in our computations required a rule that sees content.
Population model. A protocell is (F, N): it holds 1 ≤ N ≤ 2n − 1 molecules, of which 0 ≤ F ≤ N are
replicases. Protocells with F = 0 (parasites only) and F = 1 (a lone replicase, which copies only parasites)
P
are followed, with densities xF,N (t) and total density X = xF,N . The rules are the following.
• Within a protocell, the transitions are those of the main text at finite fecundity. Copies occur at rate RF
when N ≥ 2, and the product is a replicase with probability p(F, N) of Eq. 1 (p = 0 at F = 1). Each
76


[page 77]
molecule decays at rate one, and a protocell that reaches N = 0 disappears.
• Partition. A protocell with N ≥ 2n molecules is cut in two, each molecule going to either piece with
probability 21 independently. An empty piece disappears, and a piece of 2n molecules or more is cut
again, until every piece holds fewer than 2n molecules. We write T (F, N) for the expected numbers of
pieces in each state.
• Fusion. Two protocells meet and fuse at rate k f per pair (mass action), giving (F1 + F2 , N1 + N2 ), which
is partitioned at once if N1 + N2 ≥ 2n.
• Regulation. Each protocell is removed at rate µX.
Hence
ẋ = Lx + k f Fus(x, x) − µXx,
where (x ∗ x)F,N =

P

Fus(x, x) = 12 T (x ∗ x) − Xx,

F1 +F2 =F, N1 +N2 =N xF1 ,N1 xF2 ,N2 and L is the linear part. With x̃ = k f x, only k f /µ matters.

Two variants are considered.
• A fixed background of vesicles without replicases, at density Xb , each carrying m ≥ 0 parasites. A
protocell fuses with it at rate β = k f Xb , so that L becomes Lβ = L + β(T m − I), where T m adds m
parasites and partitions if needed. The regulation does not count the background, which is a fixed
reservoir; if it did, Lβ would receive −µXb I, which only lowers growth rates.
• A rule that sees content: only protocells with F ≥ 1 fuse. Under this rule a background vesicle cannot
fuse with anything, and the background is neutral.
Lemma 1 (repeated partition; proved).

(a) The partition is exchangeable: given the sizes of the pieces,

the composition of a piece of m molecules is hypergeometric. (b) At N = 2n, T ( f, 2n) = B( f, ·)/(1 − 21−2n ),
where B is the partition matrix of the Methods. (c) For the pair density V(F, N) = F(F − 1)/(N − 1) (V = 0
P
if F ≤ 1), E pieces V ≤ V(F, N) for every N ≥ 2n.
Proof. (a) Each cut treats molecules independently of their type, and the decision to cut again depends
only on sizes; the law of the assignment of labelled molecules is therefore invariant under their permutations.
(b) A trivial cut, of probability 21−2n , returns the initial state and an empty piece: T = B + 21−2n T . (c)
By (a), a piece of m ≥ 2 molecules has E[Fd (Fd − 1) | m] = F(F − 1) m(m − 1)/(N(N − 1)), hence
P
E[Vd | m] = V(F, N) m/N. Pieces of one molecule have Vd = 0, and md = N.
□
Lemma 2 (sign of a growth rate; proved).

Let V be a nonsingular M-matrix and A ≥ 0, with A − V

irreducible. Then s(A − V), the largest real part of the eigenvalues of A − V, has the sign of ρ(AV −1 ) − 1.
P
Proof. If ρ(AV −1 ) < 1, then (V − A)−1 = V −1 k≥0 (AV −1 )k ≥ 0. The Z-matrix V − A is then a nonsingular
M-matrix, so s(A − V) < 0 44 .
Conversely, let s(A − V) < 0, so that (V − A)−1 =

R∞
0

e(A−V)t dt ≥ 0. Let ρ = ρ(AV −1 ), let y ≥ 0,

y , 0, satisfy AV −1 y = ρy, and put x = V −1 y, so that x ≥ 0 and x , 0. Then (V − A)x = (1 − ρ)y, so
x = (1 − ρ)(V − A)−1 y, which is compatible with x ≥ 0, x , 0 only if ρ < 1.
For the remaining cases, replace A by tA. Then ρ(tAV −1 ) = tρ, and s(tA − V) is continuous and, for
irreducible A − V, strictly increasing in t 44 ; this gives the cases = 0 and > 0.

77

□


[page 78]
Theorem 1 (fusion between protocells does not move the invasion threshold; proved).

Take any n ≥ 2,

R < ∞, θ > 0, k f , µ ≥ 0, and any rule of fusion between two protocells, blind or not, starting from a
world without vesicles. Let L22 be the block of L on living states (F ≥ 2). Then the number of replicases
of a rare population grows if and only if r(U) := s(L22 ) > 0, and r(U) has the sign of ρ(K) − 1, where
K is the mean matrix of the main text. The invasion threshold is therefore Uc (n, R, θ), under the ceiling
ln 2 + max(0, ln(1/θ)), whatever k f , µ and the fusion rule.
Proof.
1. Fus(x, x) and Xx are homogeneous of degree two: two rare protocells meet at a rate proportional to the
square of their density. The linearization at x = 0 is therefore L.
2. No linear transition leads from F ≤ 1 to F ≥ 2: a copy at F = 1 yields a parasite, decay lowers F, and
partition conserves the number of replicases. L is thus block-triangular: the block L11 (F ≤ 1) is fed
by L22 , and not conversely.
3. Order L11 as (F = 1, F = 0).
• The F = 0 block is triangular, with diagonal −1, . . . , −(2n − 1).
• In the F = 1 block, each column sums to −1. Copying and the decay of a parasite keep the lone
replicase in exactly one piece, and its own decay removes it at rate one. The positive vector 1 is
thus a left eigenvector of this Metzler matrix for −1, so its spectral bound is −1 44 .
• Hence s(L11 ) = −1.
4. L22 is irreducible for 0 < q < 1: every living state leads to (2, 2) by decays, and (2, 2) leads to every
living state by copies. Write L22 = A − V, where A ≥ 0 collects division (growth jumps that reach 2n,
distributed by T on living states) and −V the rest.
• V is a nonsingular M-matrix: the chain within a living protocell leaves the living states of size
below 2n, by division or by the decay that brings F to one, with probability one.
• AV −1 maps a protocell to the expected living pieces of its first division. Its nonzero eigenvalues
are those of Kc = T c H, with H the probabilities of reaching division with f ′ replicases (Methods)
and T c = T (·, 2n) restricted to living states.
• By Lemma 1(b), Kc = BH/(1 − 21−2n ), whereas K = BH + 21−2n I. Hence ρ(K) = ρ(BH) + 21−2n ,
and ρ(Kc ) − 1 = (ρ(K) − 1)/(1 − 21−2n ).
Lemma 2 then gives the sign of s(L22 ).
5. Replicases live in the blocks F ≥ 2 and F = 1. The latter is fed only by the former, and loses its
replicases at rate one. If s(L22 ) > 0 the number of replicases grows; if s(L22 ) < 0, it decays at rate
max(s(L22 ), −1).

□

Numerically, Uc computed from r(U) = 0 and from ρ(K) = 1 agree to within 1.7 × 10−11 for n = 5, 10
and 20 and R = 10, 25 and 100 (θ = 1).

78


[page 79]
Proposition 2 (background of vesicles without replicases; proved). (a) If the background vesicles are
empty (m = 0), then T 0 = I and Lβ = L: fusion with them is neutral, size being counted in molecules. (b)
For m ≥ 1, Lβ is still block-triangular, and its living block satisfies
s(Lβ,22 ) ≤ max{−1, R(2Λ − 1) − 1},

Λ = max(q, q/θ),

so that s(Lβ,22 ) < 0 as soon as U > ln(2R/(R + 1)) + max(0, ln(1/θ)), a load below the ceiling.
P
Proof of (b). Let Gβ V(s) = s′ Lβ,22 (s′ , s) V(s′ ). We bound each contribution.
• Copying, for N ≥ 3, contributes RF[p(F + 1)F/N + (1 − p)F(F − 1)/N − V] = V (RF/N) [2p(N −
1)/(F − 1) − 1]. Here p(N − 1)/(F − 1) = q(N − 1)/[(F − 1) + θ(N − F)] ≤ Λ: the denominator is at
least N − 1 if θ ≥ 1, and at least θ(N − 1) if θ ≤ 1.
• Decay contributes [F(F − 1)(F − 2) + (N − F)F(F − 1)]/(N − 2) − NV = −V.
• At (2, 2), copying contributes VR(2q − 1) and decay −2V.
• Division replaces V(F ′ , 2n) by E

P

V ≤ V(F ′ , 2n) (Lemma 1(c)).

• Fusion with the background contributes β[E

P

V(pieces of (F, N + m)) − V(F, N)] ≤ β[V(F, N + m) −

V(F, N)] ≤ 0: it only dilutes pairs.
Hence Gβ V ≤ V [R(2Λ − 1)F/N − 1], and, since F ≤ N, Gβ V ≤ max{−1, R(2Λ − 1) − 1} V. As V > 0 on
living states and Lβ,22 is a Metzler matrix, the Collatz–Wielandt inequality, applied to Lβ,22 + aI ≥ 0 for a
large enough constant a, gives the bound 44 .

□

At β = 0, this is the bound at every fecundity of Appendix S3.
Which state is invaded. s(Lβ,22 ) is the invasion criterion only if x = 0 is the state without replicases of
the full model, that is, if the block of Lβ on F = 0 (independent of R and U) is stable. Otherwise, vesicles
without replicases shed by the invaders proliferate on the background. The state without replicases is then
a resident population on F = 0, whose density depends on k f /µ, and an invader meets it at first order. The
bound still holds there (Corollary 3).
Corollary 3 (no fusion raises the invasion threshold above the ceiling; proved). Let x0∗ be any stationary
population without replicases (no vesicles, or a resident population on F = 0, with or without background),
invaded by a rare replicase, with a blind partition after every fusion. Linearizing at x0∗ , the living block is
J22 = L22 + k f

X

x0∗ (0, m′ ) (T m′ − I)22 + β (T m − I)22 − µX0∗ I.

m′

An invader meets residents and background at first order, and is removed by the regulation they exert; fusion
between invaders is of second order. J is again block-triangular: a resident brings no replicase, and the fusion
of an F = 1 protocell with a resident keeps a single replicase.
Every fusion with a partner without replicases satisfies V(F, N + m′ ) ≤ V(F, N) after partition
(Lemma 1(c)), and −µX0∗ V ≤ 0. The proof of Proposition 2(b) then gives s(J22 ) ≤ max{−1, R(2Λ − 1) − 1}.
Hence no fusion, between protocells or with vesicles without replicases, raises the invasion threshold
above max{0, ln(2R/(R + 1)) + max(0, ln(1/θ))} < ln 2 + max(0, ln(1/θ)).

79

□


[page 80]
Two cases are outside the statement. A partner that carries replicases is a source of replicases, not a case
of invasion. A partition that sorts molecules after fusion falls under Appendix S2: only a partition that raises
the pair density can exceed the ceiling.
Proposition 4 (no population keeps a replicase beyond U = ln R; proved). Take any fusion rule, blind
or not, any regulation, any background and any initial state. If Rq < 1, the total density of replicases
P
Φ = s F s x s decays at least as e−(1−Rq)t . In particular, no stationary population with replicases exists for
U > ln R.
Proof. Fusion and partition conserve replicases, and regulation and background create none. Copies
create replicases at rate RF p(F, N) ≤ RFq, and decay destroys them at rate F. Hence dΦ/dt ≤ (Rq−1)Φ. □
This is the Replacement argument of Appendix S3, which holds unchanged with fusion.
Normal form at the invasion threshold (derived). Let r(U) = s(L22 ) be simple. Let v > 0 be its right
P
Perron vector, normalized over all protocells ( v = 1, F ≤ 1 included, with v11 = (rI − L11 )−1 L12 v22 ).
Let w ≥ 0 be its left Perron vector; w is carried by F ≥ 2, because r > −1 = s(L11 ). With x̃ = k f x and
Q( x̃, x̃) = Fus( x̃, x̃) − (µ/k f )X̃ x̃, an equilibrium near (Uc , 0) is x̃∗ = εv + O(ε2 ). Projecting 0 = L x̃∗ + Q( x̃∗ , x̃∗ )
on w gives 0 = rε⟨w, v⟩ + ε2 ⟨w, Q(v, v)⟩ + O(ε3 ), hence
ε=−

r(U)
,
B

B=

⟨w, Q(v, v)⟩
µ
= Bf − ,
⟨w, v⟩
kf

Bf =

⟨w, Fus(v, v)⟩ Ev⊗v [∆]
=
,
⟨w, v⟩
2 Ev [w]

with ∆(s1 , s2 ) = w(pieces of s1 ⊕ s2 ) − w(s1 ) − w(s2 ). Thus B f > 0 if and only if a fusion between two protocells drawn from the invading population creates reproductive value on average. The equilibrium density of
protocells is (ε/k f )v.
The eigenvalue along the branch is r + 2εB = −r, and r′ (Uc ) < 0.
• If B < 0, the branch exists for U < Uc and is stable (supercritical).
• If B > 0, it exists for U > Uc and is unstable (subcritical). A dense population can then coexist with
extinction up to the fold Umax of the branch, whose stability above the fold is checked numerically.
A bistability near Uc thus requires B f > 0 and k f /µ > 1/B f .
The statement is derived: it is the standard bifurcation from a simple eigenvalue. Its hypotheses, the
simplicity of r and r′ (Uc ) , 0, are checked numerically: the gap to the next eigenvalue is at least 1.08, and
r′ (Uc ) ranges from −6.35 to −54.82. On the branches computed at n = 5, R = 25, with |U − Uc | < 0.009, the
ratio of the equilibrium density to −r(U)/B ranges from 0.886 to 1.036 and tends to one at Uc .
Numerical results (numerical).

The computations are for θ = 1, n = 5, 10 and 20, and R = 10, 25 and

100.
• All protocells fuse. B f ranges from −0.200 to −0.121. At threshold, 58–98% of the invading population are vesicles without replicases: dead daughters, and the pieces shed by protocells whose lone
replicase copies only parasites. Fusion with them dilutes the pairs of living protocells. The only positive contribution comes from fusions between two protocells that each hold a lone replicase, which
form a new pair. The bifurcation is therefore supercritical for every k f /µ. Continuation of 17 branches
(n = 5, 10 and 20; k f /µ from 1 to ∞) found no fold and no stationary population beyond Uc .
80


[page 81]
• Only protocells with F ≥ 1 fuse (a rule that sees content). B f becomes positive in six of the nine cases,
and the bifurcation is subcritical for k f /µ > 1/B f , that is, above 10.64 to 45.32 depending on the case.
– A dense population then persists up to Umax = 0.8476 at n = 5, R = 25 and k f /µ = 100, while a
rare one cannot invade beyond Uc = 0.6204.
– At n = 5 and R = 25, Umax exceeds ln 2 for k f /µ between 30 and 50 and above.
– Such populations require fusion rates of hundreds per molecular lifetime, and no known chemistry is proposed for such a rule.
– A Gillespie simulation of a finite population illustrates the hysteresis at U = 0.75.
• Background. A background of vesicles carrying parasites lowered Uc in all 54 computed cases. In
30 of them the block on F = 0 is stable, so that these values are invasion thresholds in the sense of
Proposition 2.
Transient compartmentalization (derived, sketch). Pooling 8,17,18 fuses all compartments, those without
replicases included, before a blind reloading. By Lemma 1(c) applied to the pool, the pair density after
P
reloading is at most Ftot (Ftot − 1)/(Ntot − 1), so replicase production per replicase (at most RΛ V in all) is
proportional to the replicase fraction of the pool. While the pool keeps many molecules without replicases, a
rare replicase that cannot be copied alone thus declines at every round, whatever the load: what pooling can
offer is the persistence of a dense population.

S13. Proof of Theorem 4 (R > n)
This section gives in full the proof of Theorem 4 for R > n summarized in Appendix S3 (provenance: S7). Its
notation is that of Appendices S2 and S3; its lemmas are numbered within its subsections, and its constants
κ (Lemma 3.5) and κn (Section S13.4) are local to it.
S13.1

Statement and plan

Throughout, y = n/R is fixed and n, R → ∞ together. We prove the scaling law of Theorem 4 when the
replicase makes more complete copies per lifetime than its protocell holds molecules at birth (R > n, that is
0 < y < 1), for every template weight θ > 0 of the parasites.
Theorem 4 (for R > n). For every θ > 0 and every y ∈ (0, 1),

lim Uc (n, n/y, θ) = max 0, ln(1/θ) + ψ(y) ,

n→∞

ψ(y) = − ln λc (y),

where λc (y) is the threshold of the limit process defined in (4) below, and
ln

2
≤ ψ(y) < ln 2.
1+y

The threshold λc (y) is defined from the limit kernel alone, through a Schur reduction onto small types
(Section S13.2). That it coincides with the threshold obtained by direct simulation of the limit process
(Table S3) is checked numerically, not proved.

81


[page 82]
Plan.

The proof has three parts, each proved below in full.

(i) The limit process for y < 1 (Section S13.3). The reduced size u increases during every cycle and
serves as a clock. In this clock the limit kernel is monotone in the type and in λ; large types drift
down; the set of λ where the reduced kernel is critical or supercritical is a final segment, which gives
hypothesis (H2); the reduced kernel is supercritical near λ = 1, which is (H3), with λc (y) ≤ (1 + y)/2;
and λc (y) > 12 . Together, criticality is crossed exactly once.
(ii) Uniform drift of the finite kernels (Section S13.4), for every y > 0: beyond some type M, the finite
kernels Kn contract a polynomial weight, uniformly in large n and in all (q, θ) with max(q, q/θ) ≤ Λ0 <
1.
(iii) Convergence of the finite kernels (Section S13.5) for y < 1, coefficient by coefficient, and passage to
the limit in the Schur reduction, with explicit tail bounds (Section S13.6).
Section S13.7 assembles them. Section S13.8 states what remains open when R ≤ n. The results of Appendix S2 that we use (the exact generator of the weights Va,b of Section S13.2, including losses; the closed
form of the binomial partition, with its properties (P1)–(P3); the spectral bound at every fecundity; the
sign of a Schur reduction without irreducibility) are proved in Appendix S2 and restated without proof in
Section S13.2, where Lemmas 2.6–2.8 are proved.
S13.2

Setting, notation and results used

The finite model. A protocell divides when it holds 2n molecules. Its transient states are S n = {(F, N) : 2 ≤
F ≤ N ≤ 2n − 1}, where F is the number of replicases and N the number of molecules. Let q = e−U ∈ (0, 1],
λ = q/θ and Λ = max(q, q/θ) = λ max(1, θ). The transitions are
• (F, N) → (F + 1, N + 1) at rate RF p and (F, N) → (F, N + 1) at rate RF(1 − p), with p(F, N) =

q(F − 1)/ (F − 1) + θ(N − F) ;
• (F, N) → (F − 1, N − 1) at rate F, and (F, N) → (F, N − 1) at rate N − F;
• a protocell with F ≤ 1 is dead; a copy made at N = 2n − 1 triggers division, at type f ∈ {2, . . . , 2n},
the number of replicases.
At division, F1 ∼ Bin( f, 21 ) and P1 ∼ Bin(2n − f, 12 ) independently; the second daughter receives the rest,
and Nd = Fd + Pd . A daughter with Fd ≤ 1 is dead; a daughter with Nd = 2n is at the division state ( f, 2n).
Kn ( f, f ′ ) is the expected number of daughters of a type- f protocell that reach division with f ′ replicases; we
extend it by zero to f, f ′ > 2n. Uc (n, R, θ) = sup{U ≥ 0 : ρ(Kn ) > 1}, and 0 if this set is empty. The generator
of the finite chain is Gn h(F, N) = RF [p h(F + 1, N + 1) + (1 − p) h(F, N + 1) − h(F, N)] + F [h(F − 1, N −
1) − h(F, N)] + (N − F) [h(F, N − 1) − h(F, N)], with h = 0 in dead states.
The limit process

(y > 0). The state is (F, u), with u̇ = F −u between jumps; F → F +1 at rate λF(F −1)/u

and F → F −1 at rate F; F ≤ 1 is death; division occurs when u = 2y, and the two daughters start from (Bd , y)
and ( f − Bd , y) with Bd ∼ Bin( f, 12 ). K∞ = K∞ (y, λ) is its mean matrix on the types {2, 3, . . . }. It depends on
(q, θ) only through λ. Every row of Kn and of K∞ sums to at most 2: a protocell has two daughters, and each
divides at most once.
82


[page 83]
Weights. For a > 0, ϕa (F) = Γ(F − 1 + a)/Γ(F − 1), which vanishes at F = 1 (and at F = 0 for integer
a ≥ 2); for integer a, ϕa (F) = (F − 1)F · · · (F + a − 2). For b > 0 and N ≥ 2, gb (N) = Γ(N − 1)/Γ(N − 1 + b),
decreasing in N. Va,b = ϕa (F) gb (N), set to 0 in dead states. W2 = V2,2Λ = F(F − 1) g2Λ (N) is the density of
replicase pairs, up to a factor depending on N. We write (x) j = x(x − 1) · · · (x − j + 1).
Schur reductions and the threshold. For a nonnegative matrix K on the types and a cut M, let A =
{2, . . . , M}, B = {M + 1, M + 2, . . . } and
S = KAA +

X

k
KAB KBB
KBA ,

S (t) = tKAA +

k≥0

X

k
tk+2 KAB KBB
KBA .

k≥0

A cut M is admissible for K if there are a nondecreasing weight w ≥ max(1, ϕ2 ), β < 1 and C ≥ 1 with
(Kw)( f ) ≤ βw( f ) for f > M and Kw ≤ Cw; the series above then converge for t < 1/β, since KBB wB ≤ βwB
and KBA (·, j) ≤ CwB /w( j) (Lemma 6.1 gives explicit tails when rows sum to at most 2). Define


λc (y) = inf λ < 1 : ρ S ∞ (y, λ) > 1 ,

(4)

with λc (y) = 1 if the set is empty, where S ∞ (y, λ) is the Schur reduction of K∞ (y, λ) on a cut admissible for
K∞ (y, λ). By Lemma 2.6 the sign of ρ(S ∞ ) − 1 does not depend on the admissible cut (two cuts admissible
with different weights are each compared with a cut beyond both), so λc (y) is well defined; admissible cuts
exist for every λ < 1 when y < 1 (Lemma 3.3). Hypotheses (H2) and (H3) of the main text read: (H2)
ρ(S ∞ (y, λ)) < 1 for every λ < λc (y); (H3) λc (y) < 1.
Results used here (Results 2.1–2.5 from Appendix S2, stated without proof; Lemmas 2.6–2.8 proved
here).
Lemma 2.1 (exact generator). On S n , for a, b > 0 and V = Va,b , with ha (F) = aF/(F − 2 + a):


(i) copy term: p V(F + 1, N + 1) + (1 − p) V(F, N + 1) − V(F, N) = V a(N − 1)p/(F − 1) − b /(N − 1 + b);
(ii) loss term, N ≥ 3: F[V(F − 1, N − 1) − V] + (N − F)[V(F, N − 1) − V] = V [N(b − ha ) + ha (2 − b)]/(N − 2);
at (2, 2) it equals −2V;
(iii) p ≤ Λ(F − 1)/(N − 1) in every state.
Consequently: (C1) if b ≥ Λa the copy term is ≤ 0; (C2) if Λ ≤ 1 and b = Λa ≤ 2 the loss term is
≤ 0; (C3) if a ≥ 2, Λ < 1 and b = Λa > 2, the loss term is at most (b − 2)V everywhere, and ≤ 0 when
F ≥ F ∗ = b(a − 2)/(a − b).
Parts (iii) and (C3) are elementary. If θ ≥ 1 the denominator of p is at least N − 1, and if θ < 1 it equals
θ(N−1)+(1−θ)(F−1) ≥ θ(N−1); this gives (iii). The numerator in (ii) equals (b−2)(N−2)+(2−ha )(N−2+b),
and ha ≥ 2 for a ≥ 2; this gives the bound (b − 2)V in (C3), and the numerator is ≤ 0 when ha (F) ≥ b, that is
when F ≥ F ∗ .
Corollary 2.2 (supermartingale). If a > 0, Λ ≤ 1 and b = Λa ≤ 2, then for every initial state x0 ∈


S n ∪ {( f, 2n)}, gb (2n) E x0 ϕa ( f ′ )1{division} ≤ Va,b (x0 ), where f ′ is the type at division (with equality, f ′ = f ,
when x0 = ( f, 2n)).

83


[page 84]
Lemma 2.3 (binomial partition). For integer a ≥ 2, b > 0 and f ∈ {2, . . . , 2n},
a

X


E ϕa (F1 ) gb (N1 ) = gb (2n)
sa, j ( f ) j α j (n, b),
j=2

!
a
sa, j =
(a − 2)a− j ≥ 0, sa,a = 1,
j


where α j (n, b) = E[r j (N1 )], N1 ∼ Bin(2n, 12 ), r j (m) = (m) j gb (m)/ (2n) j gb (2n) for m ≥ j and 0 otherwise.
(P1) α j increases in b, and α j ≤ 1 if b ≤ 2. (P2) α j (n, b) → 2b− j as n → ∞, and α j (n, b) is bounded
uniformly in n and in b ≤ b0 . (P3) cn (Λ) := 2α2 (n, 2Λ) increases in Λ, with cn ( 12 ) = 1 − 21−2n < 1 and
cn (Λ) ≤ 2 for Λ ≤ 1.
Proposition 2.4 (spectral bound at every fecundity). For all n ≥ 2, θ > 0, q ∈ (0, 1] and R ∈ (0, ∞]:
ρ(Kn ) ≤ cn (Λ). In particular ρ(Kn ) < 1 whenever Λ ≤ 12 .
Lemma 2.5 (sign of a Schur reduction; finite matrices). Let K ≥ 0 be a finite matrix on A⊔B with ρ(KBB ) < 1,
and S = KAA + KAB (I − KBB )−1 KBA . Then ρ(K) − 1 and ρ(S ) − 1 have the same sign. No irreducibility is
needed.
Lemma 2.6 (independence of the cut). Let K ≥ 0 on a countable set of types, w ≥ 1 with (Kw)( f ) ≤ βw( f )
′

for f > M0 (β < 1) and Kw ≤ Cw. For M0 ≤ M < M ′ , ρ(S (M) ) − 1 and ρ(S (M ) ) − 1 have the same sign.
′

Proof. Let D = {M + 1, . . . , M ′ } and S ′ = S (M ) , a finite matrix on A M ⊔ D. Cutting every path that defines
S (M) (i, j) at its visits to D gives, by Tonelli, S (M) = S ′AA + S ′AD (I − S ′DD )−1 S ′DA . On BM = D ⊔ BM′ we
P
have KBM BM w ≤ βw; the rows of BM′ give k KBk′ B′ KB′ D wD ≤ wB′ , and then the rows of D give S ′DD wD ≤
KDD wD + KDB′ wB′ ≤ βwD , so that ρ(S ′DD ) ≤ β < 1. Lemma 2.5 applies to S ′ .

□

Lemma 2.7 (subsolutions). Let K ≥ 0 with an admissible cut M (weight w, constant β), and t ∈ (0, 1/β). If
v ≥ 0, v ≤ Cw, v is not identically zero on A, tKv ≥ v on B and tKv ≥ (1 + η)v on A, then ρ(S (t)) ≥ 1 + η. If
moreover t ≤ 1, then ρ(S (1)) ≥ (1 + η)/t.
P
Proof. On B, iterating m times, vB ≤ k<m (tKBB )k tKBA vA + (tKBB )m vB , and the last term is at most
P
C(tβ)m wB → 0. Hence vB ≤ k≥0 (tKBB )k tKBA vA , and on A, (1 + η)vA ≤ tKAA vA + tKAB vB ≤ S (t)vA ;
the Collatz–Wielandt inequality for the finite matrix S (t) gives ρ(S (t)) ≥ 1 + η. For t ≤ 1, S (t) ≤ t S (1)
□

entrywise.

Lemma 2.8 (supersolutions). Let K ≥ 0 with an admissible cut M (weight w, constant β). If v ≥ 0, v > 0 on
A, v ≤ Cw and Kv ≤ s∗ v on all types for some s∗ ∈ (β, 1), then ρ(S (1)) ≤ s∗ < 1.
Proof. Let t = 1/s∗ ∈ (1, 1/β). From tKv ≤ v on B we get, by iteration and positivity, vB ≥
P
P
k
k
k<m (tK BB ) tK BA vA for every m, hence v B ≥ k≥0 (tK BB ) tK BA vA ; on A, vA ≥ tKAA vA + tKAB v B ≥ S (t)vA , so
ρ(S (t)) ≤ 1. Since t ≥ 1, S (t) ≥ t S (1) entrywise, and ρ(S (1)) ≤ 1/t = s∗ .
S13.3

The limit process when y < 1

Fix y ∈ (0, 1). The generator of the limit process, acting on functions g(F, u) differentiable in u, is
Gg(F, u) = (F − u) ∂u g +




λF(F − 1) 
g(F + 1, u) − g(F, u) + F g(F − 1, u) − g(F, u) ,
u

84

□


[page 85]
with g = 0 in dead states. For V = ϕa (F)u−b , since ϕa (F+1)/ϕa (F) = (F−1+a)/(F−1) and ϕa (F−1)/ϕa (F) =
(F − 2)/(F − 2 + a),
h
i
F
GV = V (aλ − b) + b − ha (F) ,
u

ha (F) =

aF
.
F−2+a

(5)

For a ≥ 2, ha (2) = 2 and ha increases to a. With a = 2 and b = 2λ, the pair density Z = F(F − 1)u−2λ satisfies
GZ = −2(1 − λ) Z.

(6)

Lemma 3.1 (size clock). While a lineage is alive, u̇ ≥ 2 − 2y > 0: the reduced size increases from y to 2y,
and every cycle lasts at most T y = y/(2 − 2y). In the time s = u, F is an inhomogeneous birth–death chain
on {1, 2, . . . }, absorbed at 1, with rates
b(F, s) =

λF(F − 1)
,
s(F − s)

d(F, s) =

F
,
F−s

s ∈ [y, 2y],

and every lineage alive at s = 2y divides there, at type F2y . For F ≥ 2 and s ≤ 2y, F − s ≥ F(1 − y), so
b(F, s) ≤ λ(F − 1)/(y(1 − y)) and d(F, s) ≤ 1/(1 − y): the chain does not explode, and sup s F s has finite
moments of all orders. Hence
K∞ (y, λ)( f, f ′ ) = 2

X


P Bin( f, 21 ) = j P j (F2y = f ′ ),

j≥2

and every coefficient of K∞ (y, λ) is positive for λ > 0.
Proof. While F ≥ 2, u ≤ 2y < 2 ≤ F, so u̇ = F −u ≥ 2−2y. Between jumps s = u is a C 1 change of time with
derivative F −u > 0; intensities in the time s are those in the time t divided by F − s. F − s ≥ F −2y ≥ F(1−y)
because F ≥ 2. Every finite sequence of jumps has positive probability.

□

Lemma 3.2 (monotonicity). Let h ≥ 0 on the types, with h ≤ Cw for a polynomial weight w, and h̄ its
extension by 0 to the dead state.
(a) If h is nondecreasing, so is K∞ (y, λ)h.
(b) If h is nondecreasing and λ ≤ λ′ , then K∞ (y, λ)h ≤ K∞ (y, λ′ )h.
(c) If moreover λ < λ′ and h(2) > 0, then K∞ (y, λ′ )h ≥ K∞ (y, λ)h + h(2) ω, with ω( f ) > 0 for every f ≥ 2.
Proof. (a) Two chains with jumps ±1 started from j ≤ j′ are coupled to run independently while they differ
and identically once they meet; they never cross, so F s ≤ F ′s , and E j [h̄(F2y )] is nondecreasing in j (and 0 for
j ≤ 1). Bin( f, 12 ) is stochastically nondecreasing in f . (b) From a common state, let common births occur
at rate bλ , births of the λ′ -chain alone at rate bλ′ − bλ ≥ 0, and common deaths at rate d; from different
λ ) − h̄(F λ ) ≥ 0, and ≥ h(2) on
states, let the chains be independent. Then F λs ≤ F λs for all s. (c) h̄(F2y
2y
′

′

λ ≥ 2 > F λ }. From any j ≥ 2, E has positive probability: the λ′ -chain alone receives a birth, after
E = {F2y
2y
′

which the two chains are independent, and the λ-chain then undergoes j − 1 deaths while the other does not
P
□
jump. Set ω( f ) = 2 j P(Bin( f, 21 ) = j) P j (E).
Lemma 3.3 (drift of large types).

+4
ϕ3 ( f ).
(a) For λ ≤ 2/3: (K∞ ϕ3 )( f ) ≤ 23λ−2 ff +1

85


[page 86]
(b) For λ < 1 and an integer a > 1/(1 − λ): (K∞ ϕa )( f )/ϕa ( f ) ≤ 21−a(1−λ) + C/ f , and K∞ ϕa+1 ≤ C ′ ϕa+1 .
The constants are uniform for λ in a compact subset of (0, 2/3] in (a), of (0, 1) in (b) (with a >
1/(1 − max λ)). Consequently, for every λ < 1 there are admissible cuts for K∞ (y, λ), with weight w = ϕa
(nondecreasing, ϕa ≥ ϕ2 and ϕa ≥ ϕa (2) = a! ≥ 1), uniformly on compact sets of λ.
Proof. Let V = ϕa (F)u−aλ , so that GV = V[aλ − ha (F)] by (5). The cycle has bounded duration and F
has finite moments (Lemma 3.1), so the Dynkin formula applies over a cycle. At division u = 2y and
V = ϕa ( f ′ )(2y)−aλ ; in dead states V = 0.
(a) With a = 3, h3 ≥ 2 and GV ≤ (3λ − 2)V ≤ 0. Hence E j [ϕ3 ( f ′ )1{div}] ≤ 23λ ϕ3 ( j). Since ϕ3 =
(F)3 +3(F)2 and E[(Bd )i ] = ( f )i 2−i for Bd ∼ Bin( f, 21 ), two daughters give (K∞ ϕ3 )( f ) ≤ 23λ−2 [( f )3 +6( f )2 ] =
23λ−2 f ( f − 1)( f + 4).
(b) Let Fa∗ be the smallest integer with ha (Fa∗ ) ≥ aλ and γ = (aλ − 2)+ . As u ≥ y and ϕa is nondecreasing,
GV ≤ γ ϕa (Fa∗ )y−aλ 1{F < Fa∗ }, and




E j ϕa ( f ′ )1{div} ≤ 2aλ ϕa ( j) + γ T y ϕa (Fa∗ ) P j (min s F s < Fa∗ ) .
In the time s, each replicase dies at rate 1/(F − s) ≤ 1/(2 − 2y) and births only add replicases. Thinning
independent Poisson clocks of rate 1/(2 − 2y) attached to the j initial replicases shows that the number of
them still present at s = 2y, a lower bound for min s F s , dominates Bin( j, e−y/(2−2y) ); hence P j (min F < Fa∗ )
P
decays exponentially in j. By Lemma 2.3’s expansion ϕa = ai=2 sa,i (F)i , E[ϕa (Bd )] = 2−a ( f )a +O( f a−1 ), and
( f )a ≤ ϕa ( f ). Two daughters give the bound. The same computation with a + 1 gives the second weight. □
Lemma 3.4 (one crossing; hypothesis (H2)). If ρ(S ∞ (y, λ0 )) ≥ 1, then ρ(S ∞ (y, λ)) > 1 for every λ ∈ (λ0 , 1).
Hence {λ : ρ(S ∞ (y, λ)) ≥ 1} is a final segment of (0, 1), ρ(S ∞ (y, λ)) < 1 for every λ < λc (y), and ρ(S ∞ (y, λ)) >
1 for every λ ∈ (λc (y), 1).
Proof. Fix λ ∈ (λ0 , 1), an integer a > 1/(1 − λ), w = ϕa , and a cut M and β < 1 admissible uniformly on
[λ0 , λ] (Lemma 3.3(b)); by Lemma 2.6 the hypothesis holds with this cut. Write Kµ = K∞ (y, µ) and S µ (t) for
its reduction.
An eigenfunction at λ0 . ρ(S λ0 (t)) is continuous in t ∈ [0, 1/β), zero at 0 and ≥ 1 at 1: there is t∗ ∈ (0, 1]
with ρ(S λ0 (t∗ )) = 1. All coefficients of S λ0 (t∗ ) ≥ t∗ Kλ0 ,AA are positive (Lemma 3.1); let xA > 0 be its Perron
P
vector and xB = k (t∗ KBB )k t∗ KBA xA . As rows sum to at most 2 and w ≥ 1, t∗ KBA xA ≤ 2t∗ max(xA ) wB , so
xB ≤ 2t∗ max(xA )(1 − t∗ β)−1 wB ; and x = (xA , xB ) > 0 satisfies t∗ Kλ0 x = x, with x ≤ Cw.
The nondecreasing envelope. Let x̃( f ) = max2≤g≤ f x(g); then x ≤ x̃ ≤ Cw since w is nondecreasing.
By Lemma 3.2(a), t∗ Kλ0 x̃ is nondecreasing and ≥ t∗ Kλ0 x = x; for g ≤ f , (t∗ Kλ0 x̃)( f ) ≥ (t∗ Kλ0 x̃)(g) ≥ x(g),
hence t∗ Kλ0 x̃ ≥ x̃.
Above λ0 . By Lemma 3.2(b,c), t∗ Kλ x̃ ≥ x̃ + t∗ x̃(2)ω, so t∗ Kλ x̃ ≥ x̃ on B and ≥ (1 + η) x̃ on the finite set
A, with η = minA t∗ x̃(2)ω/ x̃ > 0. Lemma 2.7 gives ρ(S ∞ (y, λ)) ≥ (1 + η)/t∗ > 1.
Consequences. If ρ(S ∞ (λ0 )) ≥ 1 for some λ0 < λc , then ρ > 1 on (λ0 , λc ), contradicting the definition
of λc . For λ > λc , the definition gives λ1 ∈ [λc , λ) with ρ(S ∞ (λ1 )) > 1, and the first statement gives
ρ(S ∞ (λ)) > 1.

□

Lemma 3.5 (hypothesis (H3), with a bound). For λ ∈ (0, 1] and every type f , (K∞ ϕ2 )( f ) ≥ 22κ−1 ϕ2 ( f ) with

κ = (λ − y)/(1 − y). Consequently λc (y) ≤ (1 + y)/2 < 1, that is ψ(y) ≥ ln 2/(1 + y) .

86


[page 87]

Proof. In the time s, the generator L of the chain of Lemma 3.1 gives (Lϕ2 )(F) = 2ϕ2 (F)(λF − s)/ s(F − s) (a
birth adds 2F to ϕ2 , a death removes 2(F −1)). For F ≥ 2 and s ≤ 2y, (λF − s)/(F − s) = λ−(1−λ)s/(F − s) ≥
λ − (1 − λ) 2y/(2 − 2y) = κ, so Lϕ2 ≥ (2κ/s)ϕ2 , also at the absorbing state where ϕ2 = 0. Hence m(s) =
E j [ϕ2 (F s )] satisfies m′ ≥ (2κ/s)m (moments are finite), and m(2y) ≥ 22κ ϕ2 ( j). With E[ϕ2 (Bd )] = ϕ2 ( f )/4 and
two daughters, K∞ ϕ2 ≥ 22κ−1 ϕ2 . For λ1 ∈ ((1 + y)/2, 1), κ > 21 ; take a cut admissible at λ1 (Lemma 3.3(b))
and apply Lemma 2.7 with t = 1 and v = ϕ2 ≤ w: ρ(S ∞ (y, λ1 )) ≥ 22κ−1 > 1, so λc (y) ≤ λ1 .

□

Lemma 3.6 (λc > 12 ). For λ ∈ (0, 1) and every type f ,
(K∞ ϕ2 )( f ) = 2

2λ−1

i
hX Z τd
Z(Xtd ) dt > 0,
ℓ( f ) = 2(1 − λ)(2y) E

ϕ2 ( f ) − ℓ( f ),

2λ

d

0

where the expectation is over the partition and the cycles of the daughters. There is δ(y) > 0 such that
ρ(S ∞ (y, λ)) < 1 for all λ ≤ 12 + δ(y). Hence λc (y) > 12 and ψ(y) < ln 2.
Proof. The identity. By (6) and the Dynkin formula over a cycle of bounded duration,
E j Z(Xτ )1{div} = Z( j, y) − 2(1 − λ) E j


Z τ



Z dt,
0

and at division Z = ϕ2 ( f ′ )(2y)−2λ . Summing over two daughters with E[ϕ2 (Bd )] = ϕ2 ( f )/4 gives the identity.
ℓ( f ) > 0 because a daughter receives two replicases with positive probability.
A cut. Fix δ0 ∈ (0, 61 ), so that 12 + δ0 < 32 . By Lemma 3.3(a), choose M with β3 = 23( 2 +δ0 )−2 (M +
1

5)/(M + 2) < 1; then K∞ ϕ3 ≤ β3 ϕ3 beyond M and K∞ ϕ3 ≤ C3 ϕ3 everywhere, with C3 = 23( 2 +δ0 )−1 since
1

( f + 4)/( f + 1) ≤ 2, for λ ≤ 21 + δ0 , and M is admissible with weight ϕ3 . Let A = {2, . . . , M}.
A uniform loss on A. Before its first jump a daughter started at ( j, y) keeps F = j, Z ≥ ϕ2 ( j)(2y)−2λ , and
Rτ
the first jump occurs at rate at most c j = λ j( j − 1)/y + j, while the cycle lasts at least y/ j; hence E j 0 Z ≥
ϕ2 ( j)(2y)−2λ (1 − e−c j y/ j )/c j . There is therefore ηA > 0 with ℓ ≥ ηA ϕ2 on A, uniformly in λ ∈ (0, 21 + δ0 ].
A supersolution. Let v = ϕ2 + εv ϕ3 , and note ϕ3 = ( f + 1)ϕ2 . Choose εv > 0 with εvC3 (M + 1) ≤ ηA /4;
then s∗ ∈ (max(β3 , 1 − ηA /2), 1) with 1 − s∗ < εv (s∗ − β3 )(M + 2); then δ ∈ (0, δ0 ] with 22δ ≤ s∗ + 3ηA /4 and
22δ − s∗ ≤ εv (s∗ − β3 )(M + 2). At λ = 12 + δ: on B, K∞ v ≤ 22δ ϕ2 + εv β3 ϕ3 ≤ s∗ v, since ϕ3 ≥ (M + 2)ϕ2 there;
on A, K∞ v ≤ (22δ − ηA )ϕ2 + εvC3 ϕ3 ≤ (22δ − 34 ηA )ϕ2 ≤ s∗ v. Lemma 2.8 gives ρ(S ∞ (y, 12 + δ)) ≤ s∗ < 1, and
Lemma 3.4 extends this to every λ ≤ 12 + δ. So λc (y) ≥ 12 + δ.
S13.4

□

Uniform drift of the finite kernels (every y > 0)

Lemma 4.1 (uniform drift). Let y > 0, Λ0 ∈ (0, 1), an integer a > 1/(1 − Λ0 ) and β ∈ (21−a(1−Λ0 ) , 1). There
are M, n0 and C such that, for all n ≥ n0 , R = n/y, θ > 0 and q ∈ (0, 1] with Λ = max(q, q/θ) ≤ Λ0 :
(Kn ϕa )( f ) ≤ β ϕa ( f ) (M < f ≤ 2n),

(Kn ϕa+1 )( f ) ≤ C ϕa+1 ( f ) (2 ≤ f ≤ 2n).

The weights w = ϕa and w′ = ϕa+1 satisfy 1 ≤ w ≤ w′ and w/w′ = 1/( f + a − 1) → 0.
Constants. Let b = Λa. If b ≤ 2, Corollary 2.2 applies and what follows holds with Q1 = 0. If b > 2, let
F ∗ = b(a − 2)/(a − b); ca = Γ(F ∗ + a − 1)/Γ(F ∗ + 1), which bounds ϕa (F)/ϕ2 (F) = Γ(F − 1 + a)/Γ(F + 1)
for F ≤ F ∗ since this ratio increases in F; εy = min(y/4, 1) and Nε = ⌈εy R⌉; σa = b − 2Λ = Λ(a − 2),

87


[page 88]

 

X1 = Nε − 1 + 2Λ, X2 = 2n − 1 + 2Λ; Ξn = Γ(X2 + σa )/Γ(X2 ) / Γ(X1 + σa )/Γ(X1 ) , which tends to (2y/εy )σa ;

κn = gb (2n)/g2Λ (2n); and Q1 = (b − 2) ca Ξn / 2(1 − Λ) .
Proof. Step 1: two generator inequalities. With V = Va,b , Lemma 2.1 gives on S n
Gn V ≤ (b − 2)+ V 1{F < F ∗ },

Gn W2 ≤ −2(1 − Λ) W2 .

(7)

For V: the copy term is ≤ 0 by (C1); the loss term is at most (b − 2)V everywhere and ≤ 0 for F ≥ F ∗ by
(C3), and ≤ 0 everywhere by (C2) if b ≤ 2. For W2 : the copy term is ≤ 0 by (C1) with b = 2Λ; with a = 2,
h2 = 2 and the loss term equals (2Λ − 2)W2 for N ≥ 3, and −2W2 at (2, 2).
Step 2: Dynkin’s formula. From every state, the F − 1 successive deaths of replicases that kill the
protocell have positive probability; on the finite set S n the absorption time τ (death or division) therefore has
R t∧τ
a geometric tail, and for every function h on the state space, h(Xt∧τ ) − 0 Gn h(X s ) ds is a martingale; we let
t → ∞ by bounded and dominated convergence. As V = 0 in dead states and V( f ′ , 2n) = ϕa ( f ′ )gb (2n),
Z τ


gb (2n) E x ϕa ( f ′ )1{div} ≤ V(x) + (b − 2)+ E x
V(X s )1{F s < F ∗ } ds,
0
Z τ

Ex
W2 (X s ) ds ≤ W2 (x)/ 2(1 − Λ) .

(8)
(9)

0

The tail of the cycle. With c = 2(1 − Λ), (7) gives (∂t + Gn )(ect W2 ) ≤ 0, so E x [ec(t∧τ) W2 (Xt∧τ )] ≤ W2 (x). As
W2 ≥ ϕ2 (2)g2Λ (2n − 1) ≥ 2g2Λ (2n) on S n ,

P x (τ > t) ≤ e−ct W2 (x)/ 2g2Λ (2n) .

(10)

Step 3: where N ≥ εy R. There, for F < F ∗ , V/W2 = [ϕa (F)/ϕ2 (F)] [gb (N)/g2Λ (N)]. The first factor is
at most ca . The second, Γ(N − 1 + 2Λ)/Γ(N − 1 + b), decreases in N and equals Ξn κn at N = Nε . Hence
V ≤ ca Ξn κn W2 on {F < F ∗ , N ≥ εy R} and, by (9),
(b − 2)+ E x

Z τ

V1{F < F ∗ , N ≥ εy R} ds ≤ Q1 κn W2 (x) = Q1 gb (2n) W2 (x)/g2Λ (2n).

(11)

0

Step 4: where N < εy R; an M/M/∞ queue. On {F < F ∗ }, V ≤ ϕa (F ∗ )gb (2) = ϕa (F ∗ )/Γ(1 + b). While
the protocell lives, N jumps by +1 at rate RF ≥ 2R and by −1 at rate N. Let Ñ be a birth–death chain with
birth rate 2R and death rate Ñ, started at N0 (an M/M/∞ queue), coupled with X as follows: when N = Ñ,
common births at rate 2R, births of N alone at rate RF − 2R ≥ 0, common deaths at rate N; when N , Ñ,
independent moves. Jumps are ±1 and there are no simultaneous jumps outside common ones, so Nt ≥ Ñt

for t < τ; the rates of Ñ depend on Ñ only. At fixed t, Ñt = Bin(N0 , e−t ) + Poisson 2R(1 − e−t ) , independent,
with mean µt ≥ min(N0 , 2R). For a sum X of independent Bernoulli and Poisson variables with mean µ,
P(X ≤ µ/2) ≤ e−µ/8 . If N0 ≥ 2εy R, then µt ≥ 2εy R (as εy ≤ 1), and
P x (Nt < εy R, t < τ) ≤ e−εy R/4

for all t ≥ 0.

Rτ

With (10), for every T > 0, E x 0 1{N s < εy R} ds ≤ T e−εy R/4 + e−cT W2 (x)/ 2c g2Λ (2n) .

88

(12)


[page 89]
Step 5: the bound from one state. Take T = R. If N0 ≥ 2εy R, (8), (11) and Step 4 give


W2 (x)
V(x)
+ Q1
+ ηn (x),
E x ϕa ( f ′ )1{div} ≤
gb (2n)
g2Λ (2n)
ηn (x) =

(13)

i
(b − 2)+ ϕa (F ∗ ) h −εy R/4
W2 (x)
Re
+ e−2(1−Λ)R
.
Γ(1 + b) gb (2n)
4(1 − Λ) g2Λ (2n)

Since 1/gb (2n) ≤ (2n + b)b , W2 (x)/g2Λ (2n) ≤ ϕ2 (2n)g2Λ (2)/g2Λ (2n) is polynomial in n, and εy R =
min(n/4, n/y) grows linearly in n, η̄n = sup x ηn (x) → 0 exponentially fast, uniformly in Λ ≤ Λ0 .
Step 6: the partition. A daughter with Nd < 2εy R ≤ n/2 has probability at most P(Bin(2n, 12 ) < n/2) ≤
e−n/4 (Hoeffding) and contributes at most ϕa (2n)e−n/4 . A daughter that receives the 2n molecules divides at
once at type f , and (13) holds for it with η = 0. For the others we use (13), and we bound the sum over them
of its first two (nonnegative) terms by the sum over all daughters, which Lemma 2.3, applied with a and with
2, computes:
(Kn ϕa )( f ) ≤ 2

a
X

sa, j ( f ) j α j (n, b) + Q1 cn (Λ) ϕ2 ( f ) + εn ,

εn = 2η̄n + 2ϕa (2n)e−n/4 → 0.

(14)

j=2

Step 7: uniformity and the choice of M. In Λ ≤ Λ0 : α j (n, Λa) ≤ α j (n, Λ0 a) (P1), bounded by some Ā
uniformly in n (P2); F ∗ = Λ(a − 2)/(1 − Λ) increases with Λ, and so does ca ; by x s e−s/x ≤ Γ(x + s)/Γ(x) ≤

(x + s) s (s ≥ 0), Ξn ≤ (X2 + σa )/X1 σa eσa /X1 , which is bounded in n once εy R ≥ 2; hence Q1 ≤ Q̄1 ; and
cn (Λ) ≤ 2. In f : for f ≥ 2, ϕa ( f ) ≥ ( f − 1) f a−1 ≥ f a /2, so ( f )a ≤ ϕa ( f ), ( f ) j ≤ 2 f j−a ϕa ( f ) for j < a, and
ϕ2 ( f ) ≤ 2 f 2−a ϕa ( f ). For f > M:
X
(Kn ϕa )( f )
εn
≤ 2αa (n, Λ0 a) + 4Ā
sa, j M j−a + 4Q̄1 M 2−a +
.
ϕa ( f )
ϕa (M)
j<a
By (P2), 2αa (n, Λ0 a) → 21−a(1−Λ0 ) < β. If a ≥ 3, the two middle terms tend to 0 with M; if a = 2, they
vanish (the sum over 2 ≤ j < a is empty, and Q1 = 0 since b = 2Λ ≤ 2). Choose M, then n0 . The same
computation with a + 1, b′ = Λ(a + 1), gives (14) for ϕa+1 , each term of which is bounded by a constant
times ϕa+1 ( f ), uniformly in f and n ≥ n0 .

□

Remark 4.2. The constants are large: at n = ∞ the bound (14) falls below 1 beyond M = 193 at Λ = 0.75,
a = 5, and beyond M = 1558 at Λ = 0.9, a = 11; on the exact finite kernels at n = 120 the smallest such
M ranges from 26 to 60 in the cases computed. Only the existence of M matters: by Lemma 2.6 the sign of
ρ(S ) − 1 does not depend on the admissible cut.
S13.5

Convergence of the finite kernels when y < 1

Proposition 5.1 (convergence to the limit kernel). Let 0 < y < 1, θ > 0, and I a compact subset of (0, ∞)
such that Λ = λ max(1, θ) ≤ 1 for λ ∈ I. Let R = n/y and q = θλ. For all types f, f ′ ≥ 2,
sup Kn ( f, f ′ ) − K∞ (y, λ)( f, f ′ ) → 0
λ∈I

89

(n → ∞).


[page 90]
More precisely, for every M ≥ max( f, f ′ ), n ≥ 20 and R ≥ R0 (M) (Step 3),
h

5( f − 1) (1 + CG ) y  R
c1 f y i
|Kn ( f, f ′ ) − K∞ ( f, f ′ )| ≤ 2 e−n/4 + 2−2n +
+
+
+ 1 e−yR/96 + √ ,
M
(1 − y)R
ln(3/2)
2n

(15)

where c1 and CG depend only on y, θ, M and max I. One lets n → ∞, then M → ∞.
Proof. Step 1: the test function. Fix f ′ and u0 = y/8. For F ≥ 1 and u ∈ [u0 , 2y] let v(F, u) be the probability
that the limit lineage started at (F, u) divides at type f ′ : v(1, ·) = 0 and v(F, 2y) = 1{F = f ′ }. For F ≥ 2
and u ≤ 2y < 2, F − u ≥ F(1 − y) > 0, so the size clock of Lemma 3.1 is defined on [u0 , 2y], with
b(F, s) ≤ λ(F − 1)/(u0 (1 − y)) and d(F, s) ≤ 1/(1 − y). The strong Markov property at the first jump gives
R 2y
− s (b+d)(F,r)dr

v(F, s) = 1{F = f }e
′

+

Z 2y

Rr

′
′
e− s (b+d)(F,r )dr b(F, r)v(F + 1, r) + d(F, r)v(F − 1, r) dr.

s

The integrand is bounded, so v(F, ·) is Lipschitz, hence continuous; the integrand is then continuous, v(F, ·)
is C 1 , and ∂u v(F, u) = −b ∆+ v − d ∆− v with ∆± v = v(F ± 1, u) − v(F, u). The right-hand side is C 1 , so v(F, ·)
is C 2 . Multiplied by F − u, this is G∞ v = 0, where G∞ v = (F − u)∂u v + λF(F − 1)u−1 ∆+ v + F∆− v is the
generator of the limit process. Since |∆± v| ≤ 1, for u ∈ [u0 , 2y] and F ≥ 2:
|∂u v(F, u)| ≤ b + d ≤ c1 F,

c1 =

λ/u0 + 1
.
1−y

Differentiating the equation, ∂2u v = −[∂u b ∆+ v + b ∆+ ∂u v + ∂u d ∆− v + d ∆− ∂u v], with |∂u b| = λF(F − 1)|2u −
F|/(u2 (F−u)2 ) ≤ λ(F−1)/(u20 (1−y)2 ) (as |2u−F| ≤ F), ∂u d = F/(F−u)2 ≤ 1/(2(1−y)2 ), |∆+ ∂u v| ≤ c1 (2F+1)
and |∆− ∂u v| ≤ c1 (2F − 1). Hence
|∂2u v(F, u)| ≤ c2 F 2 ,

c2 =

λ
2u20 (1 − y)2

+

2λc1
c1
1
+
+
.
2
u0 (1 − y) 8(1 − y)
1−y

Step 2: the test function on the finite chain. Let ṽ(F, N) = v(F, N/R). Since 2n/R = 2y exactly, ṽ(F, 2n) =
′
1{F = f ′ } at division states, and ṽ = 0 at dead states. Hence E x [ṽ(Xτ )] is the probability P(n)
x ( f ) that the

finite chain started at x divides at type f ′ .
Step 3: the generator gap. Let umin = y/4, M ≥ max( f, f ′ ), D = {(F, N) ∈ S n : F ≤ M, N ≥ umin R}, and

R ≥ R0 = max 8/y, 4M(1 + θ)/(θumin ) . At x = (F, N) ∈ D, with u = N/R, a second-order Taylor expansion
in u (step 1/R) gives

 F

Gn ṽ = RF p ∆+ v + F∆− v + (F − u)∂u v + F p ∂u v(F + 1) − ∂u v(F) + ∂u v(F) − ∂u v(F − 1) + r,
R
and subtracting G∞ v = 0,


 F

λF(F − 1)  +
∆ v + F p ∂u v(F + 1) − ∂u v(F) + ∂u v(F) − ∂u v(F − 1) + r.
Gn ṽ = RF p −
u
R
Each term is O(1/R). (i) (F − 1) + θ(N − F) = θRu(1 + e) with e = (F(1 − θ) − 1)/(θRu) and |e| ≤
2F(1 + θ)/(θRu) ≤ 21 ; so RF p = λF(F − 1)/(u(1 + e)) and |RF p − λF(F − 1)/u| ≤ 4λM 3 (1 + θ)/(θRu2min ). (ii)
F p ≤ ΛF(F − 1)/(N − 1) ≤ 2ΛM 2 /(Rumin ) (Lemma 2.1(iii), and N − 1 ≥ umin R/2), so the second term is
at most 2ΛM 2 c1 (2M + 1)/(Rumin ); the third is at most 2c1 M 2 /R. (iii) The arguments u ± 1/R stay in [u0 , 2y]
because R ≥ 8/y, so |r| ≤ c2 [RF(F + 1)2 + NF 2 ]/(2R2 ) ≤ c2 (M + 1)2 (M + 2y)/(2R). Hence |Gn ṽ| ≤ CG /R on
90


[page 91]
D, with
CG =

c2 (M + 1)2 (M + 2y)
4λM 3 (1 + θ) 2ΛM 2 c1 (2M + 1)
2
+
2c
M
+
.
+
1
umin
2
θu2min

Step 4: Dynkin’s formula stopped at the exit from D. Let σ be the exit time from D. As 0 ≤ ṽ ≤ 1,
′
P(n)
x ( f ) − ṽ(x) ≤ P x (σ < τ) + (CG /R) E x [τ].

(16)

Step 5: the duration of the cycle. On S n , Gn N = RF − N ≥ 2R − (2n − 1) > 2R(1 − y) as F ≥ 2. So
Nt∧τ − 2R(1 − y)(t ∧ τ) is a submartingale, and since N ≤ 2n,

E x [τ] ≤ (2n − N0 )/ 2R(1 − y) ≤ y/(1 − y).

(17)

Step 6: the exit from D, for N0 ≥ n/2 and n ≥ 20. Replicases: V1,Λ = (F − 1)gΛ (N) satisfies Gn V1,Λ ≤
0 by (C1)–(C2) (a = 1, b = Λ ≤ 1), so it is a nonnegative supermartingale, and V1,Λ ≥ MgΛ (2n) on
{F ≥ M + 1}; by Doob’s maximal inequality and the bounds on Γ(x + s)/Γ(x), P x (supt≤τ Ft ≥ M + 1) ≤
(F0 − 1)gΛ (N0 )/(MgΛ (2n)) ≤ 5(F0 − 1)/M. Size: realize the M/M/∞ queue Ñ ≤ N of Step 4 of Lemma 4.1
with independent exponential lifetimes of mean 1, and cut [0, T ] into windows of length ln(3/2). On the
window starting at tk , Ñ is at least the number S k of customers present at tk and still present at tk + ln(3/2),
a sum of independent Bernoulli and Poisson variables of mean at least 23 min(N0 , 2R) ≥ yR/3. By Chernoff,
P(S k < yR/4) ≤ e−yR/96 . With T = R and Markov’s inequality applied to (17),



y
R
P x inf t<τ Nt < umin R ≤ (1−y)R
+ ln(3/2)
+ 1 e−yR/96 .
Step 7: the daughters. Fd ∼ Bin( f, 12 ) and Nd ∼ Bin(2n, 12 ). By Lemma 3.1, K∞ ( f, f ′ ) = 2E[v(Fd , y)],
′
−n/4 ) and the
while Kn ( f, f ′ ) = 2E[P(n)
xd ( f )]. We discard the daughters with Nd < n/2 (probability at most e

daughter that receives all 2n molecules (probability 2−2n ). The others lie in D: (16), (17) and Step 6 bound
√
′
|P(n)
n/2. This is (15). The
xd ( f ) − ṽ(xd )|; and |ṽ(xd ) − v(F d , y)| ≤ c1 F d |Nd − n|/R by Step 1, with E|Nd − n| ≤
constants increase with λ, so the bound is uniform on I.

□

Remark 5.2. For y < 1 the reduced size increases (u̇ ≥ 2−2y), v is smooth up to the boundary u = 2y, which is
crossed transversally, and the finite chain reaches the same boundary exactly (2n/R = 2y). For y ≥ 1 the first
two properties fail: u decreases when F < u, and when 2y is an integer a lineage with F = 2y approaches
u = 2y without reaching it, whereas the finite chain crosses 2n through its fluctuations. Numerically, at
y = 0.5 the error decreases as 1/n (n e(n) between 0.428 and 0.995 for n = 25 to 200); the bound (15) only
yields a rate of order n−1/4 .
S13.6

Passage to the limit in the Schur reduction

Lemma 6.1 (tails of the reduction). Let K ≥ 0 on the types, with rows summing to at most 2, weights 1 ≤ w ≤
k K )(i, j)
w′ , M, β < 1 and C ≥ 1 with (Kw)( f ) ≤ βw( f ) for f > M and Kw′ ≤ Cw′ . Let tk (i, j) = (KAB KBB
BA

for i, j ∈ A, and tk(L) the same sum restricted to paths whose intermediate points are all ≤ L. Then
tk (i, j) ≤ 2βk C w′ (i),
In particular

0 ≤ tk (i, j) − tk(L) (i, j) ≤ 2δL w′ (i) (k + 1) C k+1 ,

δL = sup w(g)/w′ (g).
g>L

′
m
k≥m tk (i, j) ≤ 2Cw (i)β /(1 − β), and the series defining S (t) converges for t < 1/β.

P

91


[page 92]
k K (·, j) ≤ 2βk w , and t (i, j) ≤
Proof. Rows sum to at most 2 and w ≥ 1, so KBA (·, j) ≤ 2wB ; then KBB
BA
B
k

2βk (KAB wB )(i) ≤ 2βk (Kw′ )(i) ≤ 2βk Cw′ (i). A path that goes beyond L has a point of index l ∈ {0, . . . , k} in
{g > L}; bounding the end of the path by 2βk−l w ≤ 2βk−l δL w′ at that point, and the beginning by C l+1 w′ (i),
□

gives the second bound.

Lemma 6.2 (passage to the limit). Let I be a set of parameters. Assume (a) Kn → K∞ coefficient by
coefficient, uniformly on I; (b) there are weights 1 ≤ w ≤ w′ with δL → 0, and M, β < 1, C ≥ 1, n0 such that
the hypotheses of Lemma 6.1 hold for K = Kn (n ≥ n0 ) and for K = K∞ , for every parameter in I. Then the
reductions on A = {2, . . . , M} satisfy
|S n (i, j) − S ∞ (i, j)| ≤ |Kn (i, j) − K∞ (i, j)| +

h
Cβm i
(L)
(L)
(i, j) + 4w′ (i) δL m2C m +
(i, j) − t∞,k
tn,k
1−β
k<m
X

for all m and L; hence S n → S ∞ uniformly on I. Moreover, for n ≥ n0 , ρ(Kn ) − 1 and ρ(S n ) − 1 have the
same sign.
Proof. The displayed bound follows from Lemma 6.1 applied to Kn and to K∞ . Each tk(L) is a finite sum of
products of k + 2 coefficients, all at most 2, with indices at most L, so it converges uniformly on I. Given
η > 0, choose m, then L, then n. For the signs: Kn,BB wB ≤ βwB , so ρ(Kn,BB ) ≤ β < 1 (Collatz–Wielandt), and
□

Lemma 2.5 applies to the finite matrix Kn .

Where the hypotheses come from. (a) is Proposition 5.1. (b) for Kn is Lemma 4.1 with w = ϕa , w′ = ϕa+1 ,
δL = 1/(L + a); for K∞ it is Lemma 3.3(b) with the same weights.
Corollary 6.3 (continuity in λ). Let I be a compact set of λ on which (a) and (b) hold with one cut M. Then
λ 7→ K∞ (y, λ)( f, f ′ ), λ 7→ S ∞ (y, λ) and λ 7→ ρ(S ∞ (y, λ)) are continuous on I.
Proof. For fixed n, the coefficients of Kn (θλ) are rational functions of q, hence continuous in λ; as ρ(Kn,BB ) ≤
β uniformly on I, Lemma 6.1 makes λ 7→ S n (λ) continuous. Uniform limits of continuous functions are
continuous, and ρ is continuous on matrices indexed by A.
S13.7

□

Proof of Theorem 4


Fix θ > 0, y ∈ (0, 1) and ε > 0, and let U ∗ = max 0, − ln(θλc ) , λc = λc (y). From Section S13.3:
ρ(S ∞ (y, λ)) < 1 for λ < λc and > 1 for λ ∈ (λc , 1) (Lemma 3.4); λc ≤ (1 + y)/2 < 1 (Lemma 3.5);
λc > 21 (Lemma 3.6). The two bounds on ψ follow.
Upper bound. Let λmin = 1/(2 max(1, θ)) and λmax = e−ε min(λc , 1/θ).
• For λ ≤ λmin , Λ ≤ 21 and ρ(Kn ) < 1 by Proposition 2.4.
• On I = [λmin , λmax ] (if not empty), Λ = λ max(1, θ) ≤ e−ε =: Λ0 < 1. Choose an integer a > 1/(1 − Λ0 )
and β ∈ (21−a(1−Λ0 ) , 1). Lemma 4.1 gives a cut for the Kn , and Lemma 3.3(b), with a and a + 1 (as
λ ≤ Λ ≤ Λ0 ), gives one for K∞ ; take the larger, which is admissible for both. Proposition 5.1 gives (a)
on I, and Lemma 6.2 gives S n → S ∞ uniformly on I. Since λmax < λc , ρ(S ∞ (λ)) < 1 on I (with this
cut, by Lemma 2.6); by Corollary 6.3 and compactness, maxI ρ(S ∞ ) < 1. Hence ρ(S n (λ)) < 1 on I for
n ≥ n1 , and ρ(Kn (θλ)) < 1 by Lemma 6.2.

92


[page 93]
So for n ≥ n1 , ρ(Kn (e−U )) < 1 for every U ≥ − ln(θλmax ) = U ∗ + ε, and Uc (n, n/y, θ) ≤ U ∗ + ε.
Lower bound. If θλc ≥ 1, then U ∗ = 0 and there is nothing to prove. Otherwise θλc < 1, and λc < 1
(Lemma 3.5). Take λ′ ∈ (λc , λc (1 + ε)) with λ′ < 1 and θλ′ < 1. Then ρ(S ∞ (λ′ )) > 1 (Lemma 3.4) and Λ′ =
λ′ max(1, θ) < 1. Lemma 6.2 with I = {λ′ } (Lemma 4.1 with Λ0 = Λ′ , Lemma 3.3(b), Proposition 5.1) gives
ρ(S n (λ′ )) → ρ(S ∞ (λ′ )) > 1, hence ρ(Kn (θλ′ )) > 1 for n ≥ n2 and Uc (n, n/y, θ) ≥ − ln(θλ′ ) ≥ U ∗ − ln(1 + ε).
As ε is arbitrary, Uc (n, n/y, θ) → U ∗ = max(0, ln(1/θ) + ψ(y)).

□

Remark 7.1. No monotonicity of ρ(Kn ) in q is used at finite fecundity: the upper bound treats the whole
interval I at once, through the uniformity of Lemma 6.2. (H3) is needed only when θ < 1: for θ ≥ 1, θλc < 1
already forces λc < 1. The kernels of all θ with the same λ converge to the same K∞ (y, λ): this is the collapse
in θ of the exact thresholds.
S13.8

What remains open, and numerical checks

R ≤ n (y ≥ 1). Lemma 4.1 holds for every y > 0. Proposition 5.1, (H2) and (H3) are not proved by
the arguments of this section: the reduced size is no longer monotone, it can approach the division threshold
without crossing it, and two coupled lineages no longer divide at the same time, so the coupling of Lemma 3.2
is not available. (H2) is checked numerically on a truncation of the limit process, and (H3) is supported
numerically. For y ≥ 1, even the existence of admissible cuts for every λ < 1, on which definition (4)
rests, is not established here. The arguments of this section therefore do not prove the scaling law in this
regime. Appendix S3 proves, by other arguments, (H3) and the convergence of the finite kernels at every y,
and the existence of admissible cuts for every λ < 1; (H2) for y ≥ 1 is proved there, computer-assisted, for
1 ≤ y ≤ 23/8 and 47/16 ≤ y ≤ 95/32 (Certified bounds on ψ, (vi)), and, for the other y ≥ 1, supported
numerically only (up to y = 16); for these y the limit holds under (H2), and without it only the bracket of
Appendix S3 is proved.
Identification. That λc (y), defined through the Schur reduction of the limit kernel, is the threshold obtained
by direct simulation of the limit process (Table S3) is checked numerically, by independent routes, not
proved.
Consequences for the fecundity.

At θ = 1, as U → ln 2, Theorem 4 and the slope of ψ at y = 0, ψ(y) =
√

3 2−4
ln 2 + o(1) /(ln 2 − U);

√
ln 2 − 3 ln2−4
2 y + o(y), proved in S14 (Theorem S), give lim supn→∞ Rmin /n ≤

this is asymptotic in U, with constants far from effective. At every U < ln 2, Lemma 3.5 already gives
lim supn→∞ Rmin /n ≤ 1/(eln 2−U − 1); that about 0.35 n/(ln 2 − U) suffices away from this limit rests on the
computed ψ. That no smaller fecundity suffices, which would make Rmin ≈ 0.35 n/(ln 2 − U) an asymptotic
equivalence, remains derived: it would require a one-sided bound on Uc uniform in y, a bound sup ψ < ln 2
away from y = 0, and a bound on Uc uniform in R ≤ n, including bounded R. Theorem Q (Appendix S3)
gives such a necessary bound at every n ≥ 25, Rmin > (κQ /3) n/(ln 2 − U) when ln 2 − U ≤ κQ /3, but with a
constant κQ ≈ 2 × 10−7 .
Numerical checks

(scripts and logs in the code deposit). On exact finite kernels with up to 79 401 states

(n = 200), the generator inequalities (7) hold to rounding (7 × 10−13 relative to the total jump rate times V or
W2 ); the bound (14) is never exceeded (ratio at most 0.53); at y = 0.5 the coefficient error max f, f ′ ≤12 |Kn −K∞ |
decreases as 1/n. At y = 0.5, λc = 0.569723, and for n = 200, ρ(Kn ) is 0.927, 0.944, 0.951 at λc − 0.03 and
93


[page 94]
1.032, 1.056, 1.066 at λc +0.03 for θ = 0.5, 1, 1.5. These checks were reproduced with independently written
code (finite chain, finite kernels and limit kernel). The same code shows that, on the domain and with the
constants of Step 1 of Proposition 5.1, the derivative bounds are reached to at most 11% and 0.7% of their
value (y = 0.5 and 0.9, λ = 0.6, F ≤ 30), and that a Richardson extrapolation of the finite kernels (n = 100,
200, 400; up to 318 801 states) recovers the limit kernel to 3.8 × 10−6 without using the size clock.

S14. The slope of ψ at y = 0 (Theorem S)
√
This section proves that ψ(y) = ln 2 − c1 y + o(y), c1 = (3 2 − 4)/ ln 2 (provenance: S7); c1 is the constant a
of Appendix S3 (ii). Its notation is that of S13; κ, Ψy and Ψ0 are local to it.
S14.1

Statement and plan

We use the setting of S13, the proof of Theorem 4 for R > n, cited as [S13]: the limit process, the weights
ϕa (F) = Γ(F − 1 + a)/Γ(F − 1), the Schur reductions S (t) on a cut M, admissible cuts, and the threshold
λc (y) of the limit kernel K∞ (y, λ), defined in [S13, Eq. (4)] by the sign of ρ(S ∞ (y, λ)) − 1 on an admissible
cut; ψ(y) = − ln λc (y). For 0 < y < 1, Theorem 4 gives limn→∞ Uc (n, n/y, θ) = max(0, ln(1/θ) + ψ(y)), with
ln(2/(1 + y)) ≤ ψ(y) < ln 2; in particular ψ(y) → ln 2 as y → 0. We compute the slope of ψ at y = 0.
√
Theorem S (slope of ψ at y = 0). Let m(λ) = 2λ−1 (2 − 2λ )2 , m0 = m( 21 ) = 3 2 − 4, a0 = m0 /(2 ln 2) and
c1 = m0 / ln 2.
(a) The spine. For λ ∈ (0, 1), the Doob transform P̃ of the kernel K0 at y = 0 by ϕ2 (the protocell that
carries a marked pair of replicases) is an irreducible stochastic matrix whose unique stationary law ν
is that of 2 + NegBin(3, π), π = 21−λ − 1. Hence Eν [1/F] = π/2 and m(λ) = 2(2 − 2λ ) 22λ−1 Eν [1/F].
(b) The Perron root. Let J = [0.45, 0.55], ηmax = 0.1 and ζmax = ηmax ln 2. For every ζ ∈ (0, ζmax ] there
is an explicit y′1 (ζ) > 0 such that, for 0 < y ≤ y′1 (ζ) and every λ ∈ J, the Perron root r(y, λ) = 1/t∗
of K∞ (y, λ) (Definition 2.1: t∗ is the value of t at which the Schur reduction of tK∞ (y, λ) has spectral
radius 1) exists and
r(y, λ) − 22λ−1 + m(λ) y ≤ ζ y.
Moreover |r(y, λ) − 22λ−1 + m(λ)y| ≤ A1 y2 for 0 < y ≤ y1 and λ ∈ J.
(c) The threshold. For every η ∈ (0, ηmax ] there is an explicit y1 (η) > 0 such that
1
2 + (a0 − η) y

≤ λc (y) ≤ 12 + (a0 + η) y

(0 < y ≤ y1 (η)).

Moreover |λc (y) − 12 − a0 y| ≤ A2 y2 and |ψ(y) − ln 2 + c1 y| ≤ A3 y2 for 0 < y ≤ y1 .
The constants are explicit (Section S14.8): A1 ≈ 4.98 × 107 , A2 ≈ 7.18 × 107 , A3 ≈ 1.44 × 108 and
y1 ≈ 1.39 × 10−9 . In particular, as y → 0+ ,
√
1 3 2−4
λc (y) = +
y + O(y2 ),
2
2 ln 2

ψ(y) = ln 2 − c1 y + O(y ),
2

√
3 2−4
c1 =
= 0.3500565 . . .
ln 2

The constants of the remainder are about 109 times too large: numerically, λc (y) − 21 − a0 y ≈ −0.085 y2
and ψ(y) − ln 2 + c1 y ≈ +0.231 y2 (Section S14.10). They only establish the existence and the form of the
94


[page 95]
remainder. The consequences for Uc and for the fecundity Rmin required near the ceiling are in Section S14.9.
Write ε = ln(2/θ) − U for the distance to the ceiling. At every ε < min(ln 2, ln(2/θ)), Corollary 9.2(i) gives
lim supn→∞ Rmin /n ≤ 1/(eε − 1); the bound with the constant c1 is proved only asymptotically, as ε → 0
(Corollary 9.2(ii) and the comments after it).
Plan.

At y = 0 the cycle is a Yule process, and ϕ2 is an exact eigenfunction of K0 , with eigenvalue 22λ−1 ; the

problem is a perturbation of this eigenvalue. On an infinite set of types an unbounded positive eigenfunction
does not by itself fix a spectral radius, and we do not use spectral perturbation theory: we construct explicit
super- and subsolutions and conclude with [S13, Lemmas 2.7, 2.8 and 3.4], as in [S13, Lemma 3.6].
(i) In the time v = u/y ∈ [1, 2], the cycles at y > 0 and at y = 0 live on the same interval, and their
jump rates differ by O(y) uniformly in the number of replicases; a Duhamel formula compares them
(Section S14.3).
(ii) The exact pair-density identity of [S13, Lemma 3.6] has a first-order term y ℓ, with a remainder O(y2 )
uniformly in the type (Section S14.4).
(iii) The protocell that carries a marked pair of replicases (the spine) has an explicit stationary law; it fixes
the slope m(λ), and the Poisson equation (K0 − 22λ−1 )h = ℓ − m(λ)ϕ2 has a solution of logarithmic
relative growth, built from the hitting times of the spine chain (Section S14.5).
(iv) ϕ2 + yh + κyϕ3 and (ϕ2 + yh − κyϕ3 )+ are a super- and a subsolution of K∞ ; the drift of ϕ3 [S13, Lemma
3.3(a)] controls the large types (Sections S14.6 and S14.7). Section S14.8 concludes, with the order of
the choices and the constants.
Results used.

From [S13]: Section 2 (limit process, weights, Schur reductions, admissible cuts, definition

of λc ), Lemmas 2.6 (independence of the cut), 2.7 (subsolutions) and 2.8 (supersolutions), Lemmas 3.1 (size
clock), 3.3(a) (drift of ϕ3 ), 3.4 (one crossing), 3.5 (ψ ≥ ln(2/(1 + y))) and 3.6 (ψ < ln 2), and Theorem 4; they
are proved there. Kac’s formula for positive recurrent chains is classical. Everything else is proved below.
S14.2

Setting: the cycle in the time v, the cut, the Perron root

The cycle in the time v.

Fix y ∈ (0, 1) and λ ∈ (0, 1). By [S13, Lemma 3.1], in the time s = u ∈ [y, 2y]

the number F of replicases of a living lineage is a birth–death chain with rates λF(F − 1)/(s(F − s)) and
F/(F − s), absorbed at F = 1, and every living lineage divides at s = 2y. Let v = s/y ∈ [1, 2]. Since ds = y dv,
the rates per unit of v are, for F ≥ 2,
by (F, v) =

λF(F − 1)
,
v(F − yv)

dy (F, v) =

yF
.
F − yv

y

(18)

y

We write X = (Xv )v∈[1,2] for this chain, E j for its law from X1 = j, Lv g(F) = by (F, v)[g(F + 1) − g(F)] +
y

y

dy (F, v)[g(F − 1) − g(F)] for F ≥ 2 and Lv g(1) = 0, and Py g( j) = E j [g(X2 )]; functions of the state always
satisfy g(0) = g(1) = 0 (dead states). Then
Ky g( f ) = 2

X

P(B f = j) Py g( j),

j≥2

95

B f ∼ Bin( f, 21 ),

(19)


[page 96]
is Ky = K∞ (y, λ) [S13, Lemma 3.1]: a linear change of time does not change the type at division. The same
formulas at y = 0 give b0 (F, v) = λ(F − 1)/v and d0 = 0: in the time ln v ∈ [0, ln 2], F − 1 is a Yule process
of rate λ, and K0 is the kernel of the limit n → ∞ at R = ∞ (Theorem 1 of the main text).
Notation and fixed choices. ϕ1 (F) = F − 1, ϕ2 (F) = F(F − 1), ϕ3 (F) = (F − 1)F(F + 1) = (F + 1)ϕ2 (F);
for F ≥ 2, ϕa (F + 1) − ϕa (F) = aϕa (F)/(F − 1), and ϕa is nondecreasing. ρ0 (λ) = 22λ−1 and σ(y, λ) =
ρ0 (λ) − y m(λ). Once and for all: J = [λ− , λ+ ] = [0.45, 0.55], y0 = 1/20, ηmax = 0.1, ζmax = ηmax ln 2,
M = 40, f0 = 8. Throughout, λ ∈ J and 0 < y ≤ y0 . The constants below depend neither on λ ∈ J nor on y
(they are bounds over λ ∈ J and y ∈ (0, y0 ]), and each is computed from the exact values of those it involves,
not from the rounded values displayed.
The cut. Let C3 = 23λ+ −1 = 1.569168 and β3 = 23λ+ −2 (M + 5)/(M + 2) = 0.840626. By [S13, Lemma
3.3(a)], (Ky ϕ3 )( f ) ≤ 23λ−2 ff +4
+1 ϕ3 ( f ) for 0 < y < 1; hence Ky ϕ3 ≤ β3 ϕ3 on B = { f > M} and Ky ϕ3 ≤ C 3 ϕ3
everywhere. At y = 0 this holds with equality: ϕ3 is an eigenfunction of the Yule semigroup (Lemma 3.3(a)
below), and E[(B f )i ] = ( f )i 2−i , so that K0 ϕ3 ( f ) = 23λ−2 f ( f − 1)( f + 4). The weight ϕ3 is nondecreasing and
≥ max(1, ϕ2 ) on the types: the cut M = 40 is admissible for Ky , with w = ϕ3 , β = β3 and C = C3 , for every
λ ∈ J and 0 ≤ y < 1. Let A = {2, . . . , M}; then ϕ3 ≤ (M + 1)ϕ2 on A and ϕ3 ≥ (M + 2)ϕ2 on B.
The Perron root. The coefficients of Ky,AA are positive [S13, Lemma 3.1]. Hence every coefficient of
P
k K
S y,λ (t) = tKAA + k≥0 tk+2 KAB KBB
BA is a power series in t with nonnegative coefficients, convergent on
[0, 1/β3 ) and strictly increasing; for matrices with positive coefficients, S ≤ S ′ entrywise with S , S ′
implies ρ(S ) < ρ(S ′ ). So t 7→ ρ(S y,λ (t)) is continuous and strictly increasing on [0, 1/β3 ), and vanishes at 0.
Definition 2.1 (Perron root). If there is t∗ ∈ (0, 1/β3 ) with ρ(S y,λ (t∗ )) = 1, it is unique, and r(y, λ) = 1/t∗ .
When r(y, λ) exists, ρ(S y,λ (1)) > 1 if and only if r(y, λ) > 1, and ρ(S y,λ (1)) < 1 if and only if r(y, λ) < 1.
By [S13, Lemma 2.6] applied to the kernel tK∞ (weight ϕ3 , M0 = 40, constant tβ3 < 1), the sign of ρ(S (t))−1
is the same on every cut M ′ ≥ 40, and, through a common cut beyond both, on every admissible cut (w′ , β′ )
with t < 1/β′ (cuts M ′ < 40 with the weight ϕ3 included): r is the same for every admissible cut whose
domain [0, 1/β′ ) contains t∗ . Only the sign at t = 1 enters the definition of λc , and that is [S13, Lemma 2.6]
itself. The Perron root r(y, λ) is the precise meaning we give to “ρ(K∞ (y, λ))” in the first-order expansion.
Lemma 2.2 (super- and subsolutions). Let K ≥ 0 have an admissible cut M (weight w, constant β), with
Schur reduction S (t).
(a) If v ≥ 0, v > 0 on A, v ≤ Cw and Kv ≤ s v on all types, with s > β, then ρ(S (1/s)) ≤ 1.
S13, Lemma 2.7 If v ≥ 0, v ≤ Cw, v is not identically zero on A, t ∈ (0, 1/β), tKv ≥ v on B and tKv ≥ (1 + η)v on A,
then ρ(S (t)) ≥ 1 + η.
Proof. (a) is the first half of the proof of [S13, Lemma 2.8], which uses s < 1 only afterwards. Let t = 1/s ∈
P
(0, 1/β). From tKv ≤ v on B we get, by iteration and positivity, vB ≥ k<m (tKBB )k tKBA vA for every m, hence
P
vB ≥ k≥0 (tKBB )k tKBA vA ; on A, vA ≥ tKAA vA + tKAB vB ≥ S (t)vA , and the Collatz–Wielandt inequality for
the finite matrix S (t), with vA > 0, gives ρ(S (t)) ≤ 1. (b) is [S13, Lemma 2.7].

96

□


[page 97]
S14.3

Rates, moments and a Duhamel formula

Lemma 3.1 (rates). For 0 ≤ y ≤ 12 , v ∈ [1, 2] and F ≥ 2: (i) 0 ≤ by − b0 = λy(F − 1)/(F − yv) ≤ λy; (ii)
0 ≤ dy ≤ y/(1 − y); (iii) by ≤ λ(F − 1)/(v(1 − y)).
Proof. F − yv ≥ F − 2y ≥ F(1 − y) since F ≥ 2, and F − yv ≥ F − 1 since yv ≤ 2y ≤ 1. Then
 λy(F−1)
F
□
by − b0 = λ(F−1)
v
F−yv − 1 = F−yv .
A protocell with F replicases lasts about y/F in the time t and loses replicases at rate F: it loses about y
replicases per cycle, whatever its size, and the same holds for the excess births. This is why all the bounds
below are uniform in F.
y

Lemma 3.2 (moments). For 0 ≤ y ≤ 12 , a ≥ 1, j ≥ 1 and v ∈ [1, 2], E j [ϕa (Xv )] ≤ vaλ/(1−y) ϕa ( j).
y

aλ
ϕa (F);
Proof. For F ≥ 2, ϕa (F − 1) ≤ ϕa (F) and, by Lemma 3.1(iii), Lv ϕa (F) ≤ by aϕa (F)/(F − 1) ≤ v(1−y)

at F = 1 both sides vanish. The chain does not explode and supv Xv has moments of all orders [S13, Lemma
3.1], so Dynkin’s formula applies to ϕa (Xv ) (localise at the first passage above N, then let N → ∞ by
R v aλ
y
dominated convergence). The function µ(v) = E j [ϕa (Xv )] satisfies µ(v) ≤ ϕa ( j) + 1 w(1−y)
µ(w) dw, and
□

Gronwall’s lemma concludes.

Lemma 3.3 (a Duhamel formula). Let a ≥ 1, c ≥ 0, g a function on {1, 2, . . . } with g(1) = 0 and |g| ≤ c ϕa ,
and v1 ∈ (1, 2]. For w ∈ [1, v1 ] let G(w, F) = E0 [g(Xv1 ) | Xw = F] (Yule semigroup).
(a) E0 [ϕa (Xv1 ) | Xw = F] = (v1 /w)aλ ϕa (F); hence |G(w, F)| ≤ c (v1 /w)aλ ϕa (F).
(b) For 0 < y ≤ 12 and j ≥ 1,
y

y

E j [g(Xv1 )] − E0j [g(Xv1 )] = E j

Z v1
1


y
Lw − Lw0 G(w, ·)(Xw ) dw,

y

where, for F ≥ 2, (Lw − Lw0 )G(F) = (by − b0 )(F, w) [G(w, F + 1) − G(w, F)] + dy (F, w) [G(w, F − 1) −
G(w, F)], and 0 at F = 1.
Proof. (a) Under P0 and in the time τ = ln w, X − 1 is a Yule process of rate λ, with generator Lg(F) =
λ(F − 1)[g(F + 1) − g(F)]. Since ϕa (F + 1) − ϕa (F) = aϕa (F)/(F − 1), Lϕa = aλϕa for every real
a > 0; the Yule process has moments of all orders, so E0 [ϕa (Xv1 ) | Xw = F] = eaλ ln(v1 /w) ϕa (F). (b)
P
G(w, F) = F ′ pln(v1 /w) (F, F ′ ) g(F ′ ), with negative binomial transition probabilities, smooth in w and dominated through (a): G is C 1 in w and satisfies the backward equation ∂wG + Lw0 G = 0. Dynkin’s fory

mula for X under Py , applied to the time-dependent function G(w, Xw ), gives E j [G(v1 , Xv1 )] − G(1, j) =
R
R
y v
y
y v
y
E j 1 1 (∂w + Lw )G(w, Xw ) dw = E j 1 1 (Lw − Lw0 )G(w, Xw ) dw. It is justified as in Lemma 3.2: up to the first
passage above N the chain lives on a finite set with bounded rates, and one lets N → ∞ by dominated cony

vergence, with |G| + |∂wG| + |LwG| ≤ c′ (1 + supv Xv )a+1 , integrable [S13, Lemma 3.1]. Finally G(v1 , ·) = g
and G(1, j) = E0j [g(Xv1 )].
S14.4

□

The exact identity and its first order

Lemma 4.1 (exact identity). For 0 < y ≤ 12 , λ ∈ (0, 1) and f ≥ 2, Ky ϕ2 = ρ0 ϕ2 − ℓy , with


ℓy ( f ) = 22λ+2 (1 − λ) y E Ψy (B f ) ,
97

y

Ψy ( j) = E j

Z 2
1

ϕ2 (Xv ) v−2λ
dv
Xv − yv


[page 98]
(the integrand vanishes when Xv = 1, and Ψy (0) = Ψy (1) = 0).
Proof. Let Z(v, F) = ϕ2 (F)v−2λ . For F ≥ 2, a birth adds 2F to ϕ2 and a death removes 2(F − 1), so
h 2λϕ2
i 2ϕ2 v−2λ h λ(F − yv) λF
i
y
(∂v + Lv )Z = v−2λ −
+ 2F by − 2(F − 1) dy =
+
−y
−
v
F − yv
v
v
2(1 − λ) y ϕ2 (F) v−2λ
=−
,
F − yv
y

and both sides vanish at F = 1. Dynkin’s formula (justified as in Lemma 3.2) gives 2−2λ E j [ϕ2 (X2 )] =
ϕ2 ( j) − 2(1 − λ)y Ψy ( j). With E[ϕ2 (B f )] = ϕ2 ( f )/4 and two daughters, Ky ϕ2 ( f ) = 22λ−1 ϕ2 ( f ) − 22λ+2 (1 −
λ)y E[Ψy (B f )].

□

This is the identity of [S13, Lemma 3.6] in the time v (the loss written ℓ there is ℓy here): there,
R
with Z = F(F − 1)u−2λ , equals y1−2λ ϕ2 (F)v−2λ (F − yv)−1 dv, and (2y)2λ y1−2λ = 22λ y.

R

Z dt,

Lemma 4.2 (first order of the loss). For 0 < y ≤ 21 , λ ∈ (0, 1) and f ≥ 2, ℓy = y ℓ + ry , with

ℓ( f ) = 2λ+1 (2 − 2λ ) f − 2 + 21− f = 2(2 − 2λ ) (K0 ϕ1 )( f ),

|ry ( f )| ≤ Cr y2 ,

R2
R2


2−2λ
1
where Cr = 22λ+2 (1 − λ) J1 + J2 /(1 − y) , J1 = 1 v1−2λ dv = 2 2−2λ−1 and J2 = 1−λ
v−2λ (v − vλ ) dv =
1
h
i
√
1−λ
2 −1
1
1
1−λ J1 − 1−λ . On J and for y ≤ y0 , C r ≤ 5.81; at λ = 2 , J1 = 1 and J2 = 6 − 4 2.
Proof. The main term. By Lemma 3.3(a) with a = 1, E0j ϕ1 (Xv ) = vλ ϕ1 ( j), so that
Ψ0 ( j) := E0j

Z 2

ϕ1 (Xv ) v−2λ dv = ϕ1 ( j)

1

21−λ − 1
1−λ

( j ≥ 1),

Ψ0 (0) := 0.

Then ℓ( f ) := 22λ+2 (1 − λ)E[Ψ0 (B f )] = 22λ+2 (21−λ − 1) E[(B f − 1)+ ], with E[(B f − 1)+ ] = f /2 − 1 + 2− f and
22λ+1 (21−λ − 1) = 2λ+1 (2 − 2λ ). Also K0 ϕ1 ( f ) = 2 E[2λ (B f − 1)+ ] = 2λ+1 E[(B f − 1)+ ].
The remainder. ry ( f ) = 22λ+2 (1 − λ) y E[Ψy (B f ) − Ψ0 (B f )], and Ψy ( j) − Ψ0 ( j) = D1 ( j) + D2 ( j) with
y

D1 = E j

Z 2h
1

i
ϕ2 (Xv )
− ϕ1 (Xv ) v−2λ dv,
Xv − yv

D2 =

Z 2
1


y
v−2λ E j − E0j [ϕ1 (Xv )] dv.

For F ≥ 2, ϕ2 (F)/(F − yv) − ϕ1 (F) = (F − 1) yv/(F − yv) ∈ [0, yv], so 0 ≤ D1 ≤ yJ1 . By Lemma 3.3(b)
with g = ϕ1 and v1 = v, G(w, F) = (v/w)λ ϕ1 (F), whose increments are ±(v/w)λ for F ≥ 2 (and G(w, 1) = 0);
R
y v
y
hence (E j − E0j )ϕ1 (Xv ) = E j 1 (v/w)λ [(by − b0 ) − dy ](Xw , w) 1{Xw ≥ 2} dw. By Lemma 3.1 the bracket lies in
Rv
[−y/(1 − y), λy], and 1 (v/w)λ dw = (v − vλ )/(1 − λ), so |D2 | ≤ yJ2 /(1 − y). Thus |Ψy − Ψ0 | ≤ y(J1 + J2 /(1 − y))
uniformly in j, and |ry | ≤ Cr y2 .

□

Remark 4.3. The remainder is bounded uniformly in the type. A heuristic computation, by a law of large
numbers in F (for large f , Xv is large, (F − 1)/(F − yv) → 1 in D1 and (by − b0 ) − dy → −(1 − λ)y in D2 ),
gives ry ( f )/y2 → 22λ+2 (21−λ − 1) as f → ∞, that is 3.314 at λ = 12 ; numerically, ry ( f )/y2 increases from
0.279 ( f = 2) to 3.261 ( f = 150), independently of y.

98


[page 99]
S14.5

The spine, the slope and the Poisson equation

Let P̃( f, f ′ ) = K0 ( f, f ′ )ϕ2 ( f ′ )/(ρ0 ϕ2 ( f )) on the types {2, 3, . . . }. Since K0 ϕ2 = ρ0 ϕ2 (Lemma 3.3(a) and
E[ϕ2 (B f )] = ϕ2 ( f )/4), P̃ is a stochastic matrix, and
K0 (ϕ2 ζ) = ρ0 ϕ2 P̃ζ

whenever P̃|ζ| < ∞.

(20)

Lemma 5.1 (the spine; Theorem S(a)). Let λ ∈ (0, 1), p = 2−λ and π = 21−λ − 1.
(a) From f , P̃ draws j = 2 + Bin( f − 2, 12 ), then X ′ + 1 =

P j+1

i=1 G i , with independent G i , geometric on
{1, 2, . . . } with parameter p. It is irreducible, and P̃( f, 2) = 22− f −3λ .

(b) Its unique stationary law ν is that of 2 + NegBin(3, π) (the number of failures before the third success,
with success probability π), and Eν [1/F] = π/2. In particular P̃ is positive recurrent.
(c) ℓ/ϕ2 = 2(2 − 2λ ) ρ0 P̃(1/F), and m(λ) := ν(ℓ/ϕ2 ) = 2(2 − 2λ ) ρ0 Eν [1/F] = 2λ−1 (2 − 2λ )2 .
Proof. (a) Weighted by ϕ2 , the partition gives P(B f = j) j( j−1) = f ( f4−1) P(Bin( f −2, 12 ) = j−2): the daughter
keeps the marked pair, and each other replicase with probability 12 . Weighted by ϕ2 , the Yule growth jumps
from F to F + 1 at rate λ(F − 1)ϕ2 (F + 1)/ϕ2 (F) = λ(F + 1) per unit of ln v: F + 1 is a Yule process of
rate λ during ln 2, started from j + 1 individuals, each of which has a geometric number of descendants with
parameter e−λ ln 2 = p. Finally P̃( f, 2) = P( j = 2) p3 = 2−( f −2) 2−3λ > 0, and from 2 every f ′ ≥ 2 is reached.
P
P
(b) Let O = F − 2. Writing j + 1 = ( j − 2) + 3, O′ = i≤Bin(O,1/2) Gi + 3k=1 (G′k − 1), so that, if O
ps
has generating function Φ, O′ has generating function Φ(h(s)) I(s), with h(s) = 21 + 21 1−(1−p)s
and I(s) =
3
p
p
1−r h(s)
1−r 3
1−(1−p)s . For Φ(s) = 1−rs , the stationarity equation Φ(s) = Φ(h(s))I(s) reads 1−rs = 1−(1−p)s ; clearing

denominators, it holds for all s if and only if r = 2 − 2p = 1 − π. So NegBin(3, π) is stationary for O;
an irreducible chain with a stationary law is positive recurrent, and the stationary law is unique. Finally
P   3
π3 P
π
k
k
E[1/(2 + O)] = k≥0 k+2
k≥0 (k + 1)(1 − π) = 2 .
2 π (1 − π) /(k + 2) = 2

(c) ℓ = 2(2 − 2λ )K0 ϕ1 (Lemma 4.2) and ϕ1 = ϕ2 · (1/F), so (20) gives the first identity. Stationarity,

ν(P̃ζ) = ν(ζ) for bounded ζ, and (b) give the second: 2(2 − 2λ ) 22λ−1 (21−λ − 1)/2 = 2λ−1 (2 − 2λ )2 .

□

Lemma 5.2 (the Poisson equation). Let λ ∈ J and ĝ = (ℓ/ϕ2 − m)/ρ0 .
(a) ∥ĝ∥∞ ≤ ḡ := max(m, cℓ /4 − m)/ρ0 , with cℓ = 2λ+1 (2 − 2λ ), and ν(ĝ) = 0. On J, ḡ ≤ 0.294212.


(b) Let W( f ) = ln( f + 1), C = {2, . . . , f0 − 1}, δ = − ln 2λ+ −1 ( f0 + 4)/( f0 + 1) , a′0 = 23− f0 −3λ+ and

W̄ = ln 2λ+ −1 ( f0 + 3) ; with f0 = 8, δ = 0.0242342 > 0, a′0 = 0.0099575 and W̄ = 2.085979. For the
chain X̃ of transition P̃ and σ2 = inf{k ≥ 0 : X̃k = 2},
E f [σ2 ] ≤ W( f )/δ + (1 + W̄/δ)/a′0
(c) The function ĥ( f ) = −E f

Pσ2 −1
k=0

for every f ≥ 2.


ĝ(X̃k ) (so that ĥ(2) = 0) satisfies P̃ĥ − ĥ = ĝ and |ĥ( f )| ≤ ḡ E f [σ2 ] ≤

H0 + H1 ln( f + 1), with H1 = ḡ/δ = 12.1404 and H0 = ḡ(1 + W̄/δ)/a′0 = 2572.81.
(d) The function h = ϕ2 ĥ (with h(0) = h(1) = 0) satisfies (K0 − ρ0 )h = ℓ − m ϕ2 and |h| ≤ (H0 + H1 ln( f +
1)) ϕ2 ≤ Hϕ3 , with H = H0 /3 + H1 /e = 862.07.
These constants are uniform in λ ∈ J.
99


[page 100]
Proof. (a) ℓ( f )/ϕ2 ( f ) = cℓ ( f − 2 + 21− f )/( f ( f − 1)) ∈ (0, cℓ /4]: the inequality 4( f − 2 + 21− f ) ≤ f ( f − 1)
reads f 2 − 5 f + 8 ≥ 4 · 21− f , which is an equality at f = 2, holds at f = 3 (2 ≥ 1), and persists since the left
side increases and the right side decreases. So ĝ ∈ [−m/ρ0 , (cℓ /4 − m)/ρ0 ]; ν(ĝ) = 0 by Lemma 5.1(c).
(b) E f [X̃ ′ + 1] = 2λ E[ j + 1] = 2λ−1 ( f + 4). By Jensen’s inequality, P̃W( f ) ≤ ln(2λ−1 ( f + 4)), and, for
f ≥ f0 , since ( f + 4)/( f + 1) decreases and λ ≤ λ+ , P̃W( f ) ≤ W( f ) − δ. For f < C, W(X̃k∧σC ) + δ (k ∧ σC ) is a
nonnegative supermartingale, σC being the hitting time of C; so δ E f [k ∧ σC ] ≤ W( f ) and E f [σC ] ≤ W( f )/δ.
From x ∈ C, P̃(x, 2) = 22−x−3λ ≥ a′0 . At each visit to C, the next step reaches 2 with probability at least a′0 ,
given the past (strong Markov property). An attempt costs one step and, if it fails, the return time to C from
X̃1 , of expectation at most E[W(X̃1 )]/δ ≤ P̃W(x)/δ ≤ W̄/δ, since P̃W(x) ≤ ln(2λ+ −1 (x+4)) ≤ W̄ for x ≤ f0 −1.
P
The first i attempts fail with probability at most (1 − a′0 )i , so E x [σ2 ] ≤ i≥0 (1 − a′0 )i (1 + W̄/δ) = (1 + W̄/δ)/a′0
for x ∈ C; the strong Markov property at σC concludes.


(c) By (b), E2 [τ2 ] = 1 + E2 EX̃1 [σ2 ] < ∞, where τ2 = inf{k ≥ 1 : X̃k = 2}, and Kac’s formula gives

P
P

ν(ζ) = E2 k<τ2 ζ(X̃k ) /E2 [τ2 ] for bounded ζ; as ν(ĝ) = 0, E2 k<τ2 ĝ(X̃k ) = 0. Let u = −ĥ. For f , 2,
the Markov property at time 1 gives u( f ) = ĝ( f ) + P̃u( f ) (Fubini: |ĝ| ≤ ḡ and E f [σ2 ] < ∞). At f = 2,

P
P̃u(2) = E2 1≤k<τ2 ĝ(X̃k ) = −ĝ(2) = u(2) − ĝ(2), since u(2) = 0. So u − P̃u = ĝ everywhere, that is
P̃ĥ − ĥ = ĝ; and |u( f )| ≤ ḡ E f [σ2 ].
(d) By (20), the series converging absolutely since |ĥ| ≤ H0 + H1 W and P̃W < ∞, (K0 − ρ0 )h = ρ0 ϕ2 (P̃ĥ −
ĥ) = ρ0 ϕ2 ĝ = ℓ − mϕ2 . Finally H0 ≤ (H0 /3)( f + 1) and ln( f + 1) ≤ ( f + 1)/e.

□

Remark 5.3. (i) The slope is forced. If (K0 − ρ0 )h′ = ℓ − m′ ϕ2 with |h′ | ≤ C(1 + ln f )ϕ2 , then ĥ′ = h′ /ϕ2
satisfies P̃ĥ′ − ĥ′ = (ℓ/ϕ2 − m′ )/ρ0 , and integrating against ν (ν(ln F) < ∞, νP̃ = ν) gives m′ = ν(ℓ/ϕ2 ).
Since ν = π0 ϕ2 /⟨π0 , ϕ2 ⟩, where π0 = ν/ϕ2 ∝ (1 − π) f is a left eigenvector of K0 by (20), this is the first-order
formula m = ⟨π0 , ℓ⟩/⟨π0 , ϕ2 ⟩. (ii) Numerically, ĥ ≥ 0, and ĥ( f ) ≈ 0.697 ln( f +1)−0.90 at λ = 12 (the predicted
asymptotic slope is (m/ρ0 )/((1−λ) ln 2) = 0.700); sup f |ĥ|/(1+ln( f +1)) = 0.43 and max f ≤150 E f [σ2 ] = 35.7.
On the types 3 ≤ f ≤ 150 and for λ = 0.45, 0.5 and 0.55, the bound of (b) exceeds E f [σ2 ] by a factor of 190
to 660, and that of (c) exceeds |ĥ| by a factor of at least 900, which does not matter here.
S14.6

The corrector under Ky


Lemma 6.1 (the corrector). For λ ∈ J and 0 < y ≤ y0 , |(Ky − K0 )h| ≤ C P y ϕ3 , with C P = H2 5λ +
2  3λ/(1−y)
≤ 6975.4.
1−y 2
Proof. Lemma 3.3 with g = h, a = 3, c = H (Lemma 5.2(d)) and v1 = 2 gives |G(w, F)| ≤ H(2/w)3λ ϕ3 (F).
For F ≥ 2, ϕ3 (F + 1) = ϕ3 (F)(F + 2)/(F − 1) ≤ 4ϕ3 (F) and ϕ3 (F − 1) ≤ ϕ3 (F); with Lemma 3.1,


y
y
|(Lw − Lw0 )G(F)| ≤ y 5λ + 2/(1 − y) H(2/w)3λ ϕ3 (F). By Lemma 3.2, E j ϕ3 (Xw ) ≤ w3λ/(1−y) ϕ3 ( j), and


(2/w)3λ w3λ/(1−y) = 23λ w3λy/(1−y) ≤ 23λ/(1−y) . Hence |(Py − P0 )h( j)| ≤ Hy 5λ + 2/(1 − y) 23λ/(1−y) ϕ3 ( j).


Finally 2E[ϕ3 (B f )] = 2 ( f )3 /8 + 3( f )2 /4 = ϕ2 ( f )( f + 4)/4 ≤ ϕ3 ( f )/2.
□
Numerically, max f |(Ky − K0 )h|/(yϕ3 ) = 0.013 at λ = 21 : the bound is crude, and it suffices because the
term it controls is multiplied by y.

100


[page 101]
S14.7

Supersolution and subsolution

Constants. m̄ = max J m = 0.274509; smin = min J ρ0 − y0 m̄ − ζmax y0 = 0.915842 > β3 = 0.840626;
 Cr
ΓA = (m̄ + ζmax ) H0 + H1 ln(M + 1) +
+ (M + 1) C P ≤ 2.869 × 105 ,
2
Cr
ΓB = (m̄ + ζmax ) H +
+ C P ≤ 7.273 × 103 .
6
For ζ ∈ (0, ζmax ] let κ = ζ/(4C3 (M + 1)), and consider the following conditions on y ∈ (0, y0 ]:
(S1) y ≤ ζ/(4ΓA );
(S2) y ≤ κ(smin − β3 )/(2ΓB );

(S3) y H0 + H1 ln(H1 /κ) < 1;

(S4) y H0 + H1 ln(M + 1) + κ(M + 1) < 1.
Proposition 7.1 (supersolution). Let λ ∈ J, ζ ∈ (0, ζmax ], y satisfy (S1)–(S3), and h = hλ be the function of
Lemma 5.2. Then v+ = ϕ2 + y h + κy ϕ3 satisfies v+ > 0, v+ ≤ (1 + y(H + κ))ϕ3 , and Ky v+ ≤ s− v+ on all types,
with s− = σ(y, λ) + ζy. Hence ρ(S y,λ (1/s− )) ≤ 1.
Proof. By Lemmas 4.1, 4.2 and 5.2(d), Ky v+ = ρ0 ϕ2 − yℓ − ry + y(ρ0 h + ℓ − mϕ2 ) + y(Ky − K0 )h + κyKy ϕ3 ;
since ρ0 − s− = y(m − ζ),

Ky v+ − s− v+ = −ζy ϕ2 + y2 (m − ζ) h − ry + y (Ky − K0 )h + κy Ky ϕ3 − s− ϕ3 .

(21)

The term in m has cancelled: this is the role of the corrector h.
On A. Ky ϕ3 − s− ϕ3 ≤ C3 ϕ3 ≤ C3 (M + 1)ϕ2 ; |h| ≤ (H0 + H1 ln(M + 1))ϕ2 ; |ry | ≤ Cr y2 ≤ C2r y2 ϕ2 , as ϕ2 ≥ 2;

|(Ky −K0 )h| ≤ C P yϕ3 ≤ C P (M +1)yϕ2 . Since κC3 (M +1) = ζ/4, Ky v+ − s− v+ ≤ yϕ2 [−ζ +ζ/4+yΓA ] ≤ − 2ζ yϕ2
by (S1).

On B. Ky ϕ3 ≤ β3 ϕ3 and s− ≥ min J ρ0 − y0 m̄ ≥ smin , so κy(Ky ϕ3 − s− ϕ3 ) ≤ −κy(smin − β3 )ϕ3 ; with
|h| ≤ Hϕ3 , |ry | ≤ C6r y2 ϕ3 (as ϕ3 ≥ 6) and Lemma 6.1, Ky v+ − s− v+ ≤ −ζyϕ2 + y2 ΓB ϕ3 − κy(smin − β3 )ϕ3 ≤
−ζyϕ2 − 2κ (smin − β3 ) yϕ3 < 0 by (S2).

Positivity. v+ = ϕ2 [1 + yĥ + κy( f + 1)] ≥ ϕ2 [1 − yH0 + y(κ( f + 1) − H1 ln( f + 1))], and κx − H1 ln x ≥

H1 (1 − ln(H1 /κ)) for x > 0; so v+ ≥ ϕ2 [1 − y(H0 − H1 + H1 ln(H1 /κ))] > 0 by (S3).
Finally v+ ≤ ϕ2 + yHϕ3 + κyϕ3 , s− ≥ smin > β3 , and Lemma 2.2(a) applies.

□

Proposition 7.2 (subsolution). Let λ ∈ J, ζ ∈ (0, ζmax ], and let y satisfy (S1), (S2) and (S4). Then v− =
(ϕ2 + y h − κy ϕ3 )+ satisfies 0 ≤ v− ≤ (1 + yH)ϕ3 and v− > 0 on A, and, with s+ = σ(y, λ) − ζy and
ζ/2
ζ ′ = 1+y(H0 +H
, Ky v− ≥ s+ v− on all types and Ky v− ≥ (s+ + ζ ′ y) v− on A. Hence ρ(S y,λ (1/s+ )) ≥
1 ln(M+1))

1 + ζ ′ y/s+ > 1.

Proof. Let u = ϕ2 + yh − κyϕ3 , so that v− = u+ ≥ u and Ky v− ≥ Ky u (Ky ≥ 0 and Ky |u| < ∞). As for (21),
with ρ0 − s+ = y(m + ζ),

Ky u − s+ u = ζy ϕ2 + y2 (m + ζ) h − ry + y (Ky − K0 )h − κy Ky ϕ3 − s+ ϕ3 .

101

(22)


[page 102]
On A, with the same bounds as above, Ky u − s+ u ≥ yϕ2 [ζ − ζ/4 − yΓA ] ≥ 2ζ yϕ2 by (S1). On B, s+ ≥ smin ,
so −κy(Ky ϕ3 − s+ ϕ3 ) ≥ κy(smin − β3 )ϕ3 , and Ky u − s+ u ≥ ζyϕ2 − y2 ΓB ϕ3 + κy(smin − β3 )ϕ3 ≥ 0 by (S2). So

Ky u ≥ s+ u everywhere: on {u > 0}, Ky v− ≥ Ky u ≥ s+ u = s+ v− , and on {u ≤ 0}, Ky v− ≥ 0 = s+ v− . On A,
u ≥ ϕ2 [1 − y(H0 + H1 ln(M + 1)) − κy(M + 1)] > 0 by (S4), so that v− = u ≤ ϕ2 (1 + y(H0 + H1 ln(M + 1)))
there, and Ky v− ≥ s+ v− + 2ζ yϕ2 ≥ (s+ + ζ ′ y) v− . Lemma 2.2(b), with t = 1/s+ ∈ (0, 1/β3 ) (as s+ ≥ smin > β3 )

and η = ζ ′ y/s+ , concludes.

□

Corollary 7.3 (bracket of the Perron root). If λ ∈ J, ζ ∈ (0, ζmax ] and y satisfies (S1)–(S4), then r(y, λ) exists
and
σ(y, λ) − ζy < r(y, λ) ≤ σ(y, λ) + ζy.
Proof. By Proposition 7.2, ρ(S (1/s+ )) > 1; since ρ(S (t)) is continuous and vanishes at 0, there is t∗ ∈
(0, 1/s+ ) with ρ(S (t∗ )) = 1, and r = 1/t∗ > s+ . By Proposition 7.1, ρ(S (1/s− )) ≤ 1, and the strict increase of
ρ(S (t)) gives t∗ ≥ 1/s− , that is r ≤ s− .
S14.8

□

Proof of Theorem S; the order of the choices and the constants

(a) is Lemma 5.1.
(b) For ζ ∈ (0, ζmax ], let y′1 (ζ) ∈ (0, y0 ] be such that (S1)–(S4) hold on (0, y′1 (ζ)] (each is a condition y ≤
or y < a threshold; take for instance half the smallest threshold). Corollary 7.3, applied to each λ ∈ J (the
conditions do not depend on λ), gives |r(y, λ) − 22λ−1 + m(λ)y| ≤ ζy for 0 < y ≤ y′1 (ζ). Now take ζ = A1 y,
with


8C3 (M + 1)ΓB 
= 4.9766 × 107 .
A1 = max 4ΓA ,
smin − β3

Then (S1) and (S2) hold by definition of A1 ; ζ ≤ ζmax means y ≤ ζmax /A1 = 1.3928 × 10−9 =: y1 ; and
(S3), (S4) hold at y = y1 (their left sides are below 4 × 10−6 ) and therefore for 0 < y ≤ y1 , since y 7→ y(H0 +
H1 ln(c/y)) increases for y < c/e, with c = 4C3 (M +1)H1 /A1 = 6.3×10−5 . So |r(y, λ)−22λ−1 +m(λ)y| ≤ A1 y2
for 0 < y ≤ y1 and λ ∈ J.
(c) Let η ∈ (0, ηmax ] and ζ = η ln 2, and let y1 (η) ∈ (0, y′1 (ζ)] be such that, in addition, (S5) (a0 + η) y ≤ 0.05
and (S6) y < η ln 2/C s , with C s = 0.2530, hold on (0, y1 (η)]. Let 0 < y ≤ y1 (η) and λ± = 12 + (a0 ± η)y; by
(S5), λ± ∈ J.
• The expansion of σ. As 2a0 ln 2 = m0 , ρ0 (λ± ) = e(m0 ±2η ln 2)y . With e x ≤ 1 + x + 21 x2 e|x| , e x ≥ 1 + x, and
|m(λ) − m0 | ≤ |m′ | J |λ − 12 |, where m′ (λ) = ln 2 · 2λ−1 (2 − 2λ )(2 − 3 · 2λ ) and |m′ | J ≤ 0.6506,
σ(y, λ− ) + ζy ≤ 1 − η ln 2 · y + C ′s y2 ,

σ(y, λ+ ) − ζy ≥ 1 + η ln 2 · y − C ′′s y2 ,

with C ′s = 21 (m0 + 2ηmax ln 2)2 e(m0 +2ηmax ln 2)y0 + |m′ | J (a0 + ηmax ) ≤ 0.2530 and C ′′s = |m′ | J (a0 + ηmax ) ≤
0.1790. By (S6), s− = σ(y, λ− ) + ζy < 1 < s+ = σ(y, λ+ ) − ζy. The terms in m0 cancel exactly: this is

where the value of the slope enters.
• Below the threshold. Proposition 7.1 at λ− gives ρ(S (1/s− )) ≤ 1, with 1/s− > 1; by the strict increase in
t (or directly by [S13, Lemma 2.8], since s− ∈ (β3 , 1)), ρ(S ∞ (y, λ− )) = ρ(S (1)) < 1. By [S13, Lemma
3.4], no λ ≤ λ− satisfies ρ(S ∞ (y, λ)) > 1. So λc (y) ≥ λ− .
102


[page 103]
• Above the threshold. Proposition 7.2 at λ+ gives ρ(S (1/s+ )) > 1, with 1/s+ < 1; so ρ(S ∞ (y, λ+ )) > 1,
and λc (y) ≤ λ+ by definition.
• The cut. Both statements are made on the cut M = 40 with weight ϕ3 , admissible for K∞ (y, λ± ); by
[S13, Lemma 2.6], the sign of ρ(S ∞ ) − 1 is the same on every admissible cut. These are statements on
the λc (y) of [S13], exactly.
• ψ. λc (y) = 12 (1 + x) with x = 2a0 y + 2e, |e| ≤ ηy and |x| ≤ 0.1; as | ln(1 + x) − x| ≤ x2 for |x| ≤ 21 ,
|ψ(y) − ln 2 + c1 y| = | ln(1 + x) − 2a0 y| ≤ 2ηy + 4(a0 + η)2 y2 .
With η = A2 y, A2 = A1 / ln 2 = 7.1797 × 107 , conditions (S1)–(S6) hold for 0 < y ≤ y1 (as in (b); (S5) and
(S6) are immediate), and |λc (y) − 12 − a0 y| ≤ A2 y2 , |ψ(y) − ln 2 + c1 y| ≤ A3 y2 with A3 = 2A2 + 4(a0 + A2 y1 )2 =
1.4359 × 108 .

□

The order of the choices.
1. J = [0.45, 0.55] ⊂ (0, 2/3), y0 = 1/20 and ηmax = 0.1 are fixed.
2. The cut: M = 40, w = ϕ3 , β3 = 0.8406 and C3 = 1.5692 depend on J only; smin = 0.9158.
3. The Poisson equation: f0 = 8, δ, a′0 , W̄, ḡ, hence H0 , H1 and H, depend on J only.
4. The remainders: Cr (Lemma 4.2) and C P (Lemma 6.1, which depends on H and y0 ); then ΓA and ΓB .
5. For (c): η ∈ (0, ηmax ], ζ = η ln 2, κ = ζ/(4C3 (M + 1)).
6. y1 (η), such that (S1)–(S6) hold on (0, y1 (η)].
7. For 0 < y ≤ y1 (η): λ± ; h = hλ± (Lemma 5.2 at the same λ); v± ; Propositions 7.1 and 7.2; conclusion.
No constant depends on y, nor on λ ∈ J. For the form O(y2 ), η = A2 y depends on y, and the conditions
remain explicit.
The size of the constants.

y1 (η) = 1.39 × 10−9 for η = 0.1 and 1.39 × 10−10 for η = 0.01, condition (S2)

being the binding one; with the largest admissible choice, y1 (η) = 1.39 × 10−8 η for every η ∈ (0, ηmax ]. The
constants of the remainder are about 109 times too large: numerically, r(y, λ) − σ(y, λ) ≈ −0.024 y2 near
λ = 21 , λc (y) − 12 − a0 y ≈ −0.085 y2 and ψ(y) − ln 2 + c1 y ≈ +0.231 y2 , so that A1 , A2 and A3 exceed the true
coefficients by factors of about 2.1 × 109 , 8.4 × 108 and 6.2 × 108 . Likewise, y1 (η) is to be compared with
the range y ≲ η/0.8 in which the super- and subsolutions of Propositions 7.1 and 7.2 are observed to work,
on the types f ≤ 120. These constants only establish the existence and the form of the remainder.
S14.9

Consequences: the threshold and the fecundity near the ceiling

Corollary 9.1 (the threshold near the ceiling). Let ϱ(y) = ψ(y) − ln 2 + c1 y, so that |ϱ(y)| ≤ 2ηy + 4(a0 + η)2 y2
for 0 < y ≤ y1 (η) and |ϱ(y)| ≤ A3 y2 for 0 < y ≤ y1 . By Theorem 4:
• for θ ≤ 1 and 0 < y < 1, limn→∞ Uc (n, n/y, θ) = ln(2/θ)−c1 y+ϱ(y), since ψ(y) ≥ ln(2/(1+y)) > 0 ≥ ln θ
[S13, Lemma 3.5];

103


[page 104]
• for 1 < θ < 2, the same holds as soon as ψ(y) > ln θ, in particular for 0 < y ≤ y1 (η) with (c1 + 2η) y +
4(a0 + η)2 y2 < ln(2/θ);
• for θ ≥ 2, the limit is 0 for every y ∈ (0, 1), since ψ(y) < ln 2 ≤ ln θ [S13, Lemma 3.6].
The limits are taken in the order of Theorem 4: n → ∞ at fixed y, then y → 0. Nothing is said here of a
joint limit, nor of a rate of convergence in n uniform in y.
The fecundity near the ceiling.

For θ ∈ (0, 2) and U ≥ 0, let Rmin (n, U, θ) = inf{R > 0 : Uc (n, R, θ) > U},

with inf ∅ = +∞, and write U = ln(2/θ) − ε.
Corollary 9.2 (sufficient fecundity). Let θ ∈ (0, 2) and 0 < ε < min(ln 2, ln(2/θ)).
(i) (At every ε.) lim sup
n→∞

Rmin (n, ln(2/θ) − ε, θ)
1
≤ ε
.
n
e −1

Rmin (n, ln(2/θ) − ε, θ) c1 + o(1)
≤
; more precisely, for every η ∈ (0, ηmax ] there is
n
ε
n→∞
an explicit ε(η) > 0 such that this limit superior is at most (c1 + 3η)/ε for 0 < ε ≤ ε(η).

(ii) (As ε → 0.) lim sup

Proof. If y ∈ (0, 1) and ψ(y) > ln 2 − ε, then ln(1/θ) + ψ(y) > U ≥ 0, and Theorem 4 gives n0 (y) such
that Uc (n, n/y, θ) > U for n ≥ n0 (y); so Rmin (n, U, θ) ≤ n/y for n ≥ n0 (y), and lim supn Rmin /n ≤ 1/y. (i) By
[S13, Lemma 3.5], ψ(y) ≥ ln 2−ln(1+y) > ln 2−ε for every y < eε −1 (and eε −1 < 1). (ii) For 0 < y ≤ y1 (η),
ψ(y) ≥ ln 2 − (c1 + 2η)y − 4(a0 + η)2 y2 ; take y = ε/(c1 + 3η), which satisfies y ≤ y1 (η) and 4(a0 + η)2 y < η as

soon as ε ≤ ε(η) = (c1 + 3η) min y1 (η), η/(8(a0 + η)2 ) ; then ψ(y) > ln 2 − (c1 + 3η)y = ln 2 − ε.
□
What this says, and what it does not.
• Part (ii) is asymptotic in ε = ln(2/θ) − U. At θ = 1 it reads: as U → ln 2, lim supn→∞ Rmin /n ≤
(c1 + o(1))/(ln 2 − U) (proved; asymptotic in U), with c1 = 0.350. Its explicit ε(η) is below 10−8 η, far
from effective. At a fixed distance from the ceiling, the bound proved here is (i), from [S13, Lemma
3.5] alone: 19.5 n at ε = 0.05 and 9.51 n at ε = 0.1, against c1 n/ε = 7.0 n and 3.5 n. That about
0.35 n/(ln 2 − U) suffices away from the limit U → ln 2 rests on the computed ψ.
• What is proved holds ratio by ratio: for each fixed ratio R/n = 1/y with ψ(y) > ln 2 − ε, Uc (n, R, θ) > U
for n ≥ n0 (y), with no uniformity in R/n and no monotonicity of Uc in R. In particular it is not proved
that every larger fecundity also suffices. No uniformity in y is needed, since Rmin is an infimum and
one y suffices; n0 (y) is not effective.
• That no smaller fecundity suffices, which would make Rmin ≈ c1 n/(ln 2 − U) an asymptotic equivalence, is not proved. With ya = ε/(c1 − δ), it would require: (1) a one-sided bound uniform in

y, lim supn supy∈[ya ,1) Uc (n, n/y, θ) − ln(1/θ) − ψ(y) ≤ 0, whereas Theorem 4 is pointwise in y; (2)
supy∈[y1 (η),1) ψ(y) < ln 2, since Theorem S only covers [ya , y1 (η)] and [S13, Lemma 3.6] is not uniform
in y; (3) a bound on Uc (n, R, θ) uniform in R ≤ n, including R = o(n) and bounded R (the scaling law
of Theorem 4 at each y ≥ 1 would not suffice). Alternatively, a monotonicity of Uc (n, ·, θ) in R at finite
size, with Theorem 4 at the single point ya , would suffice.

104


[page 105]
S14.10

What remains open, and numerical checks

Open. (i) Realistic constants in the remainder: they would need a sharp bound on the hitting times of the
spine chain (at most 46.5 on f ≤ 150, against about 8950 here), a gradient bound |ĥ( f + 1) − ĥ( f )| ≤ C/ f
(numerically, f |ĥ( f + 1) − ĥ( f )| ≤ 0.77 on f ≤ 150, close to the asymptotic slope of ĥ in ln f ), which would
reduce Lemma 6.1 to O(y ϕ2 ln f ), and a narrower J. (ii) A closed form for the second-order coefficients; the
same method pushed to second order (a second Poisson equation, and the iterated Duhamel formula) would
give them as expectations under ν. (iii) The lower half of the law of Rmin (Section S14.9). (iv) Nothing here
applies to y ≥ 1, where the size clock does not exist. That λc (y) is the threshold of the direct simulation of
the limit process (Table S3) remains numerical, as in [S13].
Numerical checks

(scripts and logs in the code deposit; all written independently of the program’s code,

and reproduced by an independent verifier with its own code: kernel in the time s integrated by an adaptive
DOP853 scheme, Poisson solution by a Neumann series).
• m(λ), for λ = 0.3 to 0.7, by three routes (left Perron vector π0 of a truncation of K0 ; stationary law of P̃;
2+NegBin(3, π)) agrees with 2λ−1 (2−2λ )2 to 1.7×10−16 ; the stationary law agrees with 2+NegBin(3, π)
to 5 × 10−16 . The Poisson equation is solved to 4 × 10−15 ; its residual at f = 2, which tests ν(ĝ) = 0,
is 6 × 10−16 .
• Cycle by cycle, the Duhamel formula of Lemma 3.3 (g = ϕ1 ) holds to 2 × 10−12 and the identity of
Lemma 4.1 to 2 × 10−15 (relative); ry ( f )/y2 increases from 0.279 to 3.261 for f = 2 to 150 (λ = 12 ),
below Cr and independent of y; max f |(Ky − K0 )h|/(yϕ3 ) = 0.013.
• The slopes (ρ(K0 ) − ρ(Ky ))/y at y = 0.02, 0.01, 0.005, 0.0025 (truncation at 100 types), extrapolated
cubically to y = 0, recover m(λ) to 10−11 at λ = 0.4, 0.5 and 0.6 (the level of the integration noise);
and 1/t∗ , computed through the Schur reduction on M = 40, equals ρ of the truncated kernel to 10−15
(verifier).
• The threshold (truncations at 80 and 100 types, which agree to 4 × 10−15 ):
y

0.0025

0.005

0.01

0.02

λc (y)

0.5004370393991

0.5008730181869

0.5017418051991

0.5034667756702

(ln 2 − ψ(y))/y

0.3494788055

0.3489027649

0.3477556683

0.3454812403

Extrapolated to y = 0, the last row gives 0.350056508 by a quadratic fit, that is c1 − 8.3 × 10−9 , and
0.3500565159 by a cubic fit, within 10−10 of c1 . The second-order coefficients are −0.0851 for λc and
+0.2314 for ψ.
• On the types f ≤ 120, at y = 0.02, 0.01, 0.005 and η = 0.05, 0.02, 0.005, the subsolution of Proposition 7.2 holds in the nine cases, and the supersolution of Proposition 7.1 in seven. The two failures
(η = 0.005 at y = 0.01 and 0.02) lie outside the range y ≤ y1 (η) of the theorem and are those expected:
on f ≤ 120, the second-order terms of (21) reach 0.55 y2 relative to ϕ2 , more than the margin ζy unless
η ≳ 0.8 y, while the term in κ only dominates for f of order 103 to 104 .

105


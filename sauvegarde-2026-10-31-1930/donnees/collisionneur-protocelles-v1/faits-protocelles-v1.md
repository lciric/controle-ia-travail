# Faits — papier « Protection of an RNA replicase by protocells has a ceiling and a price » (L. Ciric, v0.19.2, non publié)

Texte intégral extrait par pdftotext du PDF `docs/sources/pdf/Ciric-protocells-fecundity-Nature-v0.19.2.pdf` (sha256 b699fed479791d6bac8ccdff2369b49c091b8e1322ac530132a2a23f3d098edd), 107 pages. Les nombres isolés sont les numéros de ligne du manuscrit ; chaque page commence par un marqueur « [page N] ». Les formules sont extraites telles quelles et peuvent être abîmées : en cas de doute, citer la page et la ligne et le dire. Document confidentiel, non publié : ne pas le reproduire hors de la réponse.


[page 1]
1

Protection of an RNA replicase by protocells has a ceiling and a

2

price

3

Lazar Ciric
[affiliation, to be completed by the author]; e-mail: [address, to be completed by the author]

4

Life may have begun with an RNA able to copy RNA, including copies of itself 1,2 . Because such a replicase

5

copies only other molecules, its errors create parasites that are copied but do not copy, against which a

6

better catalyst gains nothing 3–5 . Compartments are the accepted escape 6–8 , but their maximal protection

7

remains unknown. Here we compute the replicase’s exact error threshold 9 in protocells that grow and divide

8

by random partition, and show that, for a sterile lone replicase, this protection has a ceiling and a price:

9

protocells can at most halve the fraction of correct copies a replicase must make, and help only a sufficiently

10

fecund one. Without decay, large protocells approach the ceiling when parasites are no better templates than

11

the replicase. With decay, the copies a replicase must complete per lifetime grow, as computed, in proportion

12

to protocell size; unfinished copies add a cost set by their fate. The only polymerase ribozyme that has copied

13

its own sequence 10 falls about tenfold or more short of replacing itself. Fecundity and the fate of unfinished

14

copies, not fidelity alone, decide whether compartments could rescue an RNA replicase. Experiments should

15

report complete copies per template lifetime and what becomes of unfinished ones.

16

A replicator that copies itself with per-copy fidelity q keeps its information only if q exceeds the inverse

17

of its selective superiority s over its mutants 9 : − ln q < ln s. In real ribozymes many mutations are neutral

18

and the functional sequence is much fitter than its mutants; with measured values the threshold is “relaxed”,

19

and replication accuracies within reach of existing polymerase ribozymes appeared sufficient 11–13 .

20

The argument assumes that superiority acts on the template. The first replicase, however, had to copy

21

other molecules, including other copies of itself: it acted in trans. A copying error then produces a molecule

22

that is still copied but no longer copies. In a well-mixed pool such a parasite benefits from the replicase

23

exactly as much as the replicase itself, whatever its catalytic efficiency, so that selection sees only template

24

quality 2–4 : catalytic superiority, the lever of the relaxed threshold, is inert. Tupper and Higgs 5 made this

25

point and judged the conclusions of ref. 12 “somewhat optimistic”, without quantifying the difference; as

26

Kun 14 put it, “a higher level evolutionary unit is required”.

27

The candidate unit is a compartment. In the stochastic corrector, molecules replicate inside protocells

28

that grow and divide, and random partition creates variation on which selection between protocells acts 6,7 .

29

Protocells were shown numerically to maintain function against parasites at error rates that are lethal in bulk:

30

in package models 6 , in trans-acting replicase models for protocells of up to ten molecules, with an optimum

31

size when they divide in two 15 , and in a complementary-strand model 16 . Transient compartmentalization

32

with pooling protects functional RNAs against parasites without division 8,17,18 . In package models of several

33

template types, the information a protocell can keep tends to a constant set by the error rate 19 . For a replicase

34

that copies in trans, how much relaxation compartments can give at most at every size, and what limits it, has

35

not been computed. The answer sets the fidelity target for experiments.
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

U = 0.3

102
101
100
10 1
10 2
10 3

protocell size at birth, n

QT45
scaling law
exact kernel

101

102

103

protocell size at birth, n

104
fecundity R (copies per lifetime)

0.8

104
fecundity needed, Rmin

gain over a well-mixed pool, U

A The ceiling

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
replicases (Theorem 2; SI S2). (B) Fecundity R (complete copies per lifetime) needed for a load U = 0.3, 0.5 or 0.6 at
θ = 1: scaling law Rmin = n/ψ−1 (U) (lines; fitted ψ) and exact thresholds (points; within 5% of the law at n = 200). The
limit is proved for R > n (Theorem 4; U = 0.5 and 0.6); for U = 0.3 (R < n) it rests on hypothesis (H2) (SI S3), and
reading Rmin from it uses the computed decrease of ψ (Methods). No replicase is maintained at or below R = 1 (grey
line). Band: estimated fecundity of QT45. (C) Viability boundaries U = Uc (n, R) at θ = 1 for n = 10 (solid; viable
region shaded) and n = 50 (dashed); dashed vertical line, the ceiling ln 2; grey lines, two fecundities proved necessary
at every size, R = eU and R = eU /(2 − eU ) (SI S3). Measured ribozymes sit at the load their error rates give a 53-bit
replicase (0.56 lethal substitutions per bit; U = ln 2 at a per-nucleotide fidelity of 0.977): bars, estimated fecundities;
upward arrow, a lower bound (TPR fragment, at the fidelity of its ancestor); horizontal arrow, lowest published fidelity
of 52-2 (U = 4.7); triangle, tC19Z, whose fecundity is unknown. Sources: Extended Data Table 2.

36

Here we answer this question for the simplest model that contains the trans problem, a trans-acting

37

replicase 15 whose errors make parasites of arbitrary template efficiency θ. We prove that the compartment

38

adds at most ln 2 to the tolerable error load at every protocell size and fecundity, whenever division ignores

39

which molecules are replicases, and, for binomial partition, exactly ln 2 in the large-protocell limit at infinite

40

fecundity when θ ≤ 1, because catalyst–template pairs, not replicases, are the unit that reproduces (Figs. 1A

41

and 2). We prove that finite fecundity spends this bonus through the single ratio of protocell size to fecundity

42

when fecundity exceeds protocell size, and bracket the other case, which reduces to one property of a limit

43

process, supported numerically (Figs. 1B and 3). Unfinished copies set a third requirement (Fig. 4), and make

44

protocells and a surface respond differently to the kinetics of the polymerase (Fig. 5). Measured polymerase

45

ribozymes miss the first two requirements (Fig. 1C). Proofs, numerical methods and further results are in the

46

Methods and the Supplementary Information (SI).

47

A trans-acting replicase in protocells

48

A protocell contains F replicases and P parasites, N = F + P molecules (Fig. 2). Each replicase copies the

49

other molecules: it picks a template among the N − 1 molecules other than itself, a replicase with weight 1

50

and a parasite with weight θ. A copy of a replicase template is a functional replicase with probability q = e−U

51

and a parasite otherwise; a copy of a parasite is a parasite. The next molecule made in a protocell is therefore

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

2q/ > 1

ordered pairs F(F 1), trans copying

×22q/

2n

binomial partition of each species
fecundity R: copies per molecule lifetime

×1
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

52

a replicase with probability
p(F, N) =

q (F − 1)
.
(F − 1) + θ (N − F)

(1)

53

The protocell grows from n to 2n molecules and splits into two daughters, each molecule going to either

54

daughter independently (binomial partition). A protocell with F ≤ 1 is a dead lineage: a lone replicase

55

has no functional template in trans, and is never copied. The population of protocells is infinite; living

56

protocells form a multitype branching process, and the threshold Uc (n, θ) is the load beyond which the

57

spectral radius ρ of the mean matrix of living daughters no longer exceeds one (Methods). The model is

58

that of Bianconi et al. 15 without spontaneous replication, which would require a complete non-enzymatic

59

copy of the replicase (Methods). θ lumps everything that makes a parasite a better or worse template than a

60

replicase: shorter length, structure, and the competition for binding to the catalyst; θ > 1 is the realistic case

61

for a parasite shorter than its replicase (Discussion). Until finite fecundity is introduced, molecules do not

62

decay.

63

At most a factor of two

64

Without compartments, a replicase whose errors make parasites of template weight θ persists only if its

65

correct copies are made faster than parasites are copied 3,20 , q > θ: Uc = max(0, ln(1/θ)). For θ ≥ 1 no error

66

at all is tolerated. In protocells we prove three results (Methods; SI S1–S2):

67

Theorem 1 (limit kernel). Let B∞ be the limit, as n → ∞ at fixed replicase number, of the kernel of living

68

daughters, for growth by a factor k and binomial partition into k daughters. For q < θ, its spectral radius is

69

ρ(B∞ ) = k2q/θ−1 , with the positive eigenfunction h(F) = F(F − 1), and the h-transformed chain is positive

70

recurrent. The threshold of B∞ is therefore q = θ/2, that is Uc = ln(2/θ), for every k; if θ ≥ 2, ρ(B∞ ) < 1 for

71

every q < 1 and Uc = 0.

3


[page 4]
72

Theorem 2 (bounds at every size). For binary division, infinite fecundity and every n ≥ 2, ρ < 1 for all

73

q ≤ min(θ, 1)/2. Hence Uc (n) < max(0, ln(1/θ)) + ln 2: at every size the protocell adds less than ln 2 to

74

the well-mixed threshold, that is, Uc (n) < ln(2/θ) if θ ≤ 1 and Uc (n) < ln 2 if θ ≥ 1. If θ ≥ 1, moreover,

75

Uc (n) ≥ ln(2/θ) − O(n4−n ). At θ = 1, ρ(q = 21 ) = 1 − 21−2n exactly.

76

Theorem 3 (the limit). For binary division and infinite fecundity, limn→∞ Uc (n) = max(0, ln(2/θ)) for every

77

θ.

78

The proofs rest on a fictitious clock in which replicase templates are copied at rate 1 and parasites at

79

rate θ, so that F − 1 is a Yule process of rate q whose dynamics do not involve the parasites, and on the pair

80

density ϕ = F(F − 1)/(N − 1), a supermartingale during growth when q ≤ min(θ, 1)/2 (Methods). For θ ≤ 1

81

the exact thresholds therefore converge to ln(2/θ), from below; an independently written kernel code extends

82

them to n = 800 for θ = 0.5 and n = 400 for θ = 1.5, where the extrapolation in 1/n meets ln(2/θ) to within

83

2 × 10−6 and 2 × 10−7 (Fig. 1A; Extended Data Fig. 1A; Methods). For θ > 1 the pair density bounds the

84

threshold only by ln 2; the convergence also uses that ρ never decreases as q grows, at every size, and that

85

protocells rich in replicases drift back uniformly in n (Methods).

86

In the large-protocell limit, the protocell adds exactly ln 2 to the well-mixed threshold whenever θ ≤ 1,

87

only ln(2/θ) when 1 < θ < 2, and parasites that are at least twice as good templates as the replicase (θ ≥ 2)

88

cannot be resisted (Extended Data Fig. 1B). Catalytic efficiency does not appear: speeding up the replicase

89

speeds up its parasites by the same factor.

90

Pairs, not replicases, reproduce

91

Why two? In the fictitious clock, the expected number of ordered pairs of replicases, F(F − 1) = ν(ν + 1)

92

with ν = F − 1, obeys E[ν(t)(ν(t) + 1)] = ν0 (ν0 + 1) e2qt : pairs multiply twice as fast as replicases. Over one

93

growth phase of duration (ln 2)/θ, they multiply by 22q/θ . Binomial partition gives each daughter a quarter of

94

the pairs on average, E[Fd (Fd − 1)] = F(F − 1)/4, so that division halves the expected number of pairs. Pairs

95

are conserved over a cycle when 22q/θ /2 = 1, that is 2q = θ (Fig. 2C). A lone replicase is sterile, so pairs,

96

not replicases, are the reproducing unit; a replicase that could copy itself would have no threshold (Fig. 2C;

97

SI S1).

98

The pair argument says what the factor two depends on (Extended Data Table 1). It is a property of

99

catalyst–template pairs, not of binomial division: the bound holds at every size and fecundity whenever

100

division ignores which molecules are replicases, whatever the number and sizes of the daughters, and with

101

complementary strands, the load being counted per copy (SI S2). Divisions that look at the molecules change

102

it: an equal partition of replicases lowers the limit to ln(1.44/θ), and, within the model, only a division that

103

raises the summed pair density of the daughters above that of the mother, such as sorting the replicases into

104

one daughter, can exceed it. With complementary strands 16 the limit is ln(1.9486/θ). It no longer bounds

105

the threshold when a lone replicase can still be copied without a catalyst, which revives lineages: with

106

the spontaneous replication term of Bianconi et al. 15 , the thresholds that we compute in their model reach

107

0.87–0.91 at θ = 1 for protocells dividing at 40–60 molecules, above ln 2, because a lone replicase is never

108

degraded there and is copied spontaneously as fast as parasite-only cells grow, which amounts to χ = q ≈ 0.4

109

correct uncatalysed copies per lifetime; for strong catalysis and large protocells, the predicted limit is 0.903

110

(both derived; SI S5).

4


[page 5]
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

Fig. 3 | Finite fecundity spends the bonus. (A) Compartment bonus ψ = Uc − ln(1/θ) against y = n/R: exact kernels
at θ = 1 extrapolated in n (line and points), exact values at n = 200 for θ = 0.5, 1 and 1.5 (circles; the θ = 1.5 point
at y = 4 is omitted because Uc is there at its floor, zero), which converge to the same curve in 1/n (SI Table S3), and
direct simulation of the limit process (squares; error bars smaller than the symbols). (B) Threshold of the scaling limit
(Theorem 4 for y < 1; for y ≥ 1, under hypothesis (H2), SI S3), Uc = max(0, ln(1/θ) + ψ(n/R)), in the plane (y, θ);
above the thick line replicases are not maintained in the scaling limit (the panel title calls this law “Conjecture 1”; it
is proved for y < 1). (C) At fixed fecundity R = 40, the exact threshold (points) falls towards the well-mixed value at
finite fecundity (dashed, Eq. 2; zero for θ ≥ 1) as protocells grow, after an initial rise for θ < 1; at R = ∞ (thin lines) it
tends instead to ln(2/θ).

111

Finite fecundity spends the bonus

112

Real molecules decay. Let each replicase start R copies per molecular lifetime and each molecule decay at

113

rate one: R is the fecundity, the number of complete copies a replicase makes before it is destroyed 20,21 , and

114

R = ∞ is the model above. We computed Uc (n, R, θ) exactly with two independently written kernel codes

115

(Methods). The ceiling survives decay: at every size and fecundity, Uc (n, R, θ) ≤ un + max(0, ln(1/θ)), where

116

un = Uc (n, ∞, 1) < ln 2 (Methods), and the same pair density brackets the price: at θ = 1, R > eU /(2 − eU )

117

is necessary at every size, and R > n eU /(2 − eU ) suffices in large protocells (SI S3). The price has the same

118

origin as the ceiling: the pair density decays at rate 2(1 − q) per molecular lifetime while a protocell grows

119

(Methods), and growth lasts longer the larger the protocell is relative to the fecundity.

120

Two orders of limits disagree. At fixed R, a mean-field argument (SI S3) gives as n → ∞ the well-mixed

5


[page 6]
121

threshold at finite fecundity,



Umix (R, θ) = max 0, − ln θ + (1 − θ)/R ,

(2)

122

that is, the law 1 − e−Uc = (1 − 1/R)(1 − 1/s) with s = 1/θ, whose special cases are Eigen’s at R → ∞,

123

Demetrius, Schuster and Sigmund’s at s → ∞, and the binary-fission threshold at s = 2 (refs. 9,20,22,23).

124

At fixed n and R → ∞, the threshold tends instead to the protocell value. At fixed R and θ < 1 it therefore

125

first rises with n and then falls back, slowly, towards the well-mixed value (Methods); for θ ≥ 1 it decreases

126

from n = 5 on at the fecundities shown (Fig. 3C). This accounts, in mean field and for a single strand, for the

127

slow decline of the threshold with protocell size found by Shah et al. 16 .

128

The two limits are joined by a single function. The threshold is carried by protocells with a few replicases

129

among N molecules, and with decay such a protocell grows only if RF > N. When n and R are both large at

130

fixed y = n/R, the finite kernels converge to those of a piecewise-deterministic Markov process 24 for F and

131

u = N/R that depends on q and θ only through λ = q/θ (Methods; SI S3), and:

132


Theorem 4 (scaling). As n, R → ∞ with n/R = y < 1 fixed, Uc (n, R, θ) → max 0, ln(1/θ) + ψ(y) for every

133

θ, where ψ(y) = − ln λc (y) is the threshold of the limit process and ln(2/(1 + y)) ≤ ψ(y) < ln 2 (SI S13).

134

For y ≥ 1 the same limit holds if the spectral radius of the reduced limit kernel reaches one at a single

135

λ (hypothesis (H2), SI S3), as it does numerically; otherwise the limit points of the thresholds are bracketed

136

(SI S3); that ψ decreases with y is numerical. The exact kernels agree with the limit: for θ = 0.5, 1 and 1.5

137

they converge in 1/n to the same ψ, to within 10−3 at y = 0.25 and 1, and a direct simulation of the limit

138

process agrees to within 0.8 standard errors (Fig. 3A; SI Table S3; Extended Data Fig. 7). The compartment

139

bonus is ψ = 0.693, 0.618, 0.486, 0.317 and 0.18 at y = 0, 0.25, 1, 4 and 16, and ψ(y) ≈ ln 2/(1+y/0.823)0.443

140

to within 0.002 on [0, 16].

141
142

The consequence is a fecundity requirement that scales with protocell size. Inverting this law, a replicase
with load U is maintained if
R ≳ Rmin =

n
ψ−1 U + ln θ

,

(3)

143

so that Rmin ≃ 0.22 n, 1.1 n and 3.1 n for U + ln θ = 0.3, 0.5 and 0.6 (SI S3); the exact kernel gives Rmin /n =

144

0.25, 1.16 and 3.13 at n = 50 and θ = 1 (Fig. 1B). Compartments therefore give a trans-acting replicase

145

most of their help only if it makes, in its lifetime, a number of complete copies comparable with the number

146

of molecules in its protocell. In large protocells at fixed n/R and θ ≤ 1, R ≥ 0.35 n keeps more than half

147

of the bonus ln 2 and R ≤ n/3.2 less than half; at every size and θ, a replicase making, on average, at most

148

n/5 complete copies per lifetime gains less than 21 ln 2 over max(0, ln(1/θ)) (all proved, computer-assisted;

149

SI S3).

150

The fate of unfinished copies

151

Where stated, a copy of a full-length template stops early with probability τ, and its product is either lost

152

or a truncated molecule, copied faithfully thereafter, with template weight θ′ relative to a replicase. Two

153

exact identities (SI S8) show that what matters is not how often the polymerase stops but what becomes of

154

the product: a lost copy multiplies the fecundity required by exactly 1/(1 − τ), and a replicable copy with

155

θ′ = θ shifts the threshold by exactly ln(1 − τ), at every size and fecundity. A shorter molecule, however,

156

is usually a faster template (θ′ > θ), and exact kernels with three molecular types then show a different
6


[page 7]
1.0
0.8
0.6
0.4
0.2
0.0

lost (no product)
replicable, 0 = (n = 20)
replicable, 0 = 2, n = 10
replicable, 0 = 2, n = 20
replicable, 0 = 2, n = 30

10 2

B Lost, it costs a few percent of fecundity; fast, all
Fecundity required, relative to = 0

Tolerable load, relative to = 0

A A replicable fast copy costs load as n grows

10 1

100

lost: 1/(1 ), exact
replicable, n = 20, U = 0.30
replicable, n = 20, U = 0.45
replicable, n = 10, U = 0.45

10
5

2
1
10 3

Truncated copies made per cycle, n

no fecundity
suffices

10 2
Probability that a copy stops early,

Fig. 4 | The fate of an unfinished copy decides which requirement termination consumes. (A) Tolerable load at
infinite fecundity, relative to its value without termination, against the number nτ of truncated copies made per division
cycle (θ = 1). A lost truncated copy costs nothing (orange; exact). A replicable truncated copy exactly as good a
template as a full-length parasite (θ′ = θ) only adds the load − ln(1 − τ) (grey dashes; exact, n = 20). A replicable
truncated copy twice as fast a template as the replicase (θ′ = 2; exact kernels, n = 10, 20, 30) costs load as nτ grows,
nearly independently of n up to nτ ≈ 0.3, and leaves no tolerable load beyond nτc = 1.85, 1.61 and 1.53 for n = 10, 20
and 30 (squares). (B) Fecundity required, relative to its value without termination. For the lost fate it rises by exactly
1/(1 − τ) (orange). For the replicable fate (θ′ = 2; exact kernels with decay; n = 20 at U = 0.30 and 0.45, n = 10 at
U = 0.45) it rises sevenfold at τ = 0.03 for U = 0.30, and, for n = 20 and U = 0.45, no fecundity suffices at τ = 0.03
(arrow).

157

behaviour (Fig. 4A). At θ′ = 2 the tolerable load falls with the number of truncated copies made per division

158

cycle, nτ, to a quarter or a third of its value at nτ = 1, and vanishes between nτ = 1.5 and 1.85 (n = 10 to

159

30). Unlike the error load, this cost grows with protocell size: large protocells make more truncated copies

160

per cycle. At finite fecundity both fates cost something, in the same currency (Fig. 4B). The same chemical

161

event, depending on what becomes of its product, costs a few percent of fecundity or the replicase itself.

162

Protocells and a surface differ

163

How much faster a truncated copy is copied depends on how the copying time of the polymerase depends on

164

length. If a share b of that time does not depend on length (initiation, binding, product release) and the rest

165

grows in proportion to it, a truncated copy of length L′ on a replicase of length L is copied 1/[b + (1 − b)L′ /L]

166

times faster, which is its template advantage θ′ when copying follows mass action (Methods). Protocells

167

impose a threshold on θ′ (Fig. 5B), with an elbow where the large-protocell ceiling ln(2/θ′ ) vanishes: a

168

protocell that makes one truncated copy more than twice as fast as the replicase is lost, whatever its speed,

169

and growth passes through the lineages that have made none (SI S9). The kinetic profile of the polymerase

170

therefore matters to protocells only through the share of its truncated copies that lie beyond the elbow. When

171

protocells copy as a lattice model does 5 (Methods), protocells of 20 to 80 molecules recover only 13–20%

172

of the damage at b = 0.15, and half of it only beyond b ≈ 0.33 (Fig. 5A); the shape holds in every variant

173

we tried (SI S9). On a surface the response is different, as Tupper and Higgs 5 found with their lattice model:

174

there a length-independent share b = 0.1 already multiplies the tolerable termination tenfold, against 1.5–

175

1.6 in protocells that copy in the same way, and their published threshold recovers half of the damage near

176

b ≈ 0.12, and 55% at b = 0.15 (Fig. 5A). Earlier comparisons of compartments and surfaces concerned

7


[page 8]
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

Fig. 5 | Protocells and a surface respond differently to how copying time depends on length. (A) Share of the
damage done by replicable truncated copies that is recovered when the length-independent share b of the copying time
grows, D(b) = [log mc (b)−log mc (0)]/[log mc (1)−log mc (0)], with mc the critical termination probability per nucleotide
at vanishing error load. The protocells (exact kernels, n = 20, 40, 80) copy as the lattice does: a copy stops at each
nucleotide with probability m, a product shorter than 10 nucleotides is lost, copies of truncated templates stop in the
same way, and a copy that stops early ends sooner (truncated lengths in two classes split at θ′ = 2, a grouping that
overestimates the threshold near the elbow and beyond: dashes beyond b = 0.3; points keep every truncated length, by
a population Monte Carlo, and are offset slightly in b for legibility; SI S9). They recover 13–20% of the damage at
b = 0.15, and half of it only beyond b ≈ 0.33. The lattice model of Tupper and Higgs 5 recovers 55% at b = 0.15, and
half near b ≈ 0.12: black, their published threshold (1024 × 1024 sites); grey, a reimplementation (256 × 256 sites, runs
to t = 120), with brackets on D derived from those of its threshold (SI S10). Other protocell variants: SI Fig. S2. (B)
With a single truncated length, the critical number of truncated copies per cycle nτc against their template advantage θ′
(n = 5, 10, 20): beyond θ′ = 2, where the large-protocell ceiling ln(2/θ′ ) vanishes, it depends only weakly on θ′ .

177

survival and long-term evolution 16,25 .

178

Measured ribozymes miss two requirements

179

Fig. 1C, Extended Data Fig. 2 and Extended Data Table 2 place measured polymerase ribozymes in the plane

180

of error load and fecundity. The load of a replicase copy is U = ℓIε, with ε the per-nucleotide error rate

181

of each chemistry, I = 53 bits the functional information 26 of the 45-nucleotide QT45 (ref. 10), the only

182

replicase for which such an estimate exists, and ℓ = 0.56 the number of lethal substitutions per bit, computed

183

from the tolerance of each of its sites measured by the same authors (Methods). Fecundity is computed from

184

published yields, reaction times and half-lives as the number of complete copies made per template lifetime

185

(Methods).

186

QT45, the only polymerase ribozyme that has copied its own sequence, makes 0.006–0.10 complete

187

copies of its complement from its own sequence, and 0.004–0.07 copies of itself from its complement, per

188

template lifetime, with the ribozyme in tenfold excess over the template (SI S6). At the per-nucleotide

189

fidelity measured for the complement of its own sequence, 0.941, its load is U ≈ 1.8. Whatever the size

190

of the protocell, maintenance needs R > eU ≥ 1, the extinction criterion of lethal mutagenesis 20,27 , here

191

proved for a trans-acting replicase in protocells of every size: a replicase must at least replace itself (SI S3).

192

QT45 is therefore short by a factor of 10–250 in fecundity even at vanishing load (5–27 at the lower end,

193

given the uncertain potassium content of the buffers; SI S6), and by a factor of 2.5 in load even at infinite

194

fecundity (2.3–2.7 over the range of ℓ). Taking its measured fitness landscape as replication rates, as for a

8


[page 9]
195

self-copying template, Gianni et al. 10 report that a fidelity of 0.974 would keep about 12% of a population

196

active. For a replicase that copies whatever template it meets, the protocell ceiling sets a comparable target,

197

0.977 (0.974–0.978), but only for large protocells at infinite fecundity; at the fecundity measured, no fidelity

198

suffices. The class I polymerases 24-3 and 52-2 are short in both directions as well 28–31 ; a fragment of the

199

triplet polymerase copied above R = 1 32 and the most accurate polymerase, tC19Z 33 , each meet at most one

200

requirement (Extended Data Table 2; SI S6).

201

The two gaps differ in size (Extended Data Table 2). In load, the chemistries measured are within a factor

202

of 1.1–3.6 of the protocell ceiling, and up to 6.8 for the lowest published fidelity of 52-2; tC19Z is inside it.

203

In fecundity, QT45 is 1.0–2.4 orders of magnitude short of replacing itself, and the class I polymerases are

204

4–56 times short on other templates; for QT45 and 24-3 the fecundity gap is the larger. Improving fidelity

205

alone cannot close it, because in the scaling limit the load ceiling itself recedes as n/R grows (Eq. 3): for

206

a 53-bit replicase with θ = 1, a protocell requires a per-nucleotide fidelity above 0.977 if R ≫ n, 0.984 if

207

R = n and 0.989 if R = n/4, the last close to the best average fidelity measured. Termination raises the target

208

further (SI S8 and S11, SI Table S6).

209

Discussion

210

For a trans-acting replicase in protocells that divide by random partition, we have computed what the higher-

211

level unit presupposed by the relaxed error threshold 14 can supply. When parasites are no better templates

212

than the replicase (θ ≤ 1), it is a factor of at most 2 in effective superiority, that is, ln 2 on the tolerable

213

load, reached in the large-protocell limit at infinite fecundity. When parasites are better templates (θ > 1),

214

no fidelity suffices in bulk, protocells of any size add less than ln 2, and large ones only max(0, ln(2/θ)).

215

Estimates of the relaxed threshold that rest on a superiority of order 351 (refs. 11–13) therefore do not carry

216

over to the first replicase: in protocells its tolerable load, and with it the maximal replicase length at a given

217

fidelity, is smaller by a factor of ln 351/ ln 2 ≈ 8.5. This gives a quantitative form to the objection of Tupper

218

and Higgs 5 . Applying Eigen’s threshold to QT45 at its measured fidelity of 0.941, Gianni et al. 10 find that it

219

needs a selective superiority above 166 (their fig. S32), for a (+)/(−) cycle of 84 nucleotides in which every

220

substitution is lethal; per copy of one strand this is a load of 2.6, about 3.7 times the ln 2 that bounds what

221

a protocell of any size adds, and 2.5 times when only the substitutions that lower activity below 80% count

222

(Extended Data Table 2). What is new, relative to numerical solutions of protocell models 6,7,15,16,34,35 , is

223

the limit and its mechanism, which turn numerical thresholds into a rule: the threshold is max(0, ln(1/θ) +

224

ln(1/λc )), the well-mixed term ln(1/θ) plus a compartment constant ln(1/λc ) fixed by how division treats

225

pairs. Transient compartmentalization with pooling 8,17,18 , computed for a trans-acting replicase without

226

external selection, stayed below the ceiling (SI S5); spatial self-organization on surfaces 5,34,36,37 remains to

227

be computed.

228

The ceiling depends on a single property of the parasites, their template efficiency relative to the replicase.

229

Deletion mutants, the parasites that arise first in experiments, are better templates than the molecule they

230

derive from: θ = 1.2–1.7 for parasites copied by Qβ replicase alongside a ribozyme 8,18 , for which the large-

231

protocell ceiling ln(2/θ) is only 0.16–0.50. Complex formation raises θ further, a replicase bound as a catalyst

232

being unavailable as a template 35,38 , most in small vesicles: in a 100-nm vesicle holding 100 molecules, the

233

ceiling falls to 0.32 for a Michaelis constant of 0.7 mM (SI S5). Within the model, under division that

234

ignores which molecules are replicases, the one lever that raises the ceiling is template discrimination, θ < 1:

235

a replicase that prefers functional templates, for instance through a recognition tag 4 or a hybridization motif
9


[page 10]
236

shared by kin 2 , adds ln(1/θ) to the well-mixed threshold, and protocells add ln 2 on top.

237

The ceiling assumes a division blind to molecular identity and a sterile lone replicase. A division into

238

two equal daughters that together keep on average at most a fraction r̄ of the mother’s replicase pairs (r̄ = 1/2

239

under random partition) caps the compartment constant of large protocells at ln[2/ log2 (1/r̄)] (for r̄ ≥ 1/4),

240

which partial sorting reaches at high fecundity: ln 4 requires keeping 71% of pairs together, ln 8 requires

242

84% (Extended Data Fig. 3). A lone replicase copied correctly without a catalyst χ times per lifetime raises
√
the limit to ln 2 + (3 2 − 4)χ + O(χ2 ), and χ ≥ 1 removes the threshold (Extended Data Fig. 4). One that can

243

copy itself, with weight c relative to another replicase, has no ceiling at high fecundity, the limits R → ∞ and

244

c → 0 not commuting; one more bit requires c ≈ 4n/R (Extended Data Fig. 5). Fusion between protocells

245

leaves the invasion threshold unchanged, and no fusion raises it above the ceiling; in our computations only

246

fusion restricted to replicase carriers, which sees content, kept dense populations beyond ln 2 (Extended Data

247

Fig. 6).

241

248

Finite fecundity turns the ceiling into a requirement on R that grows with protocell size (Eq. 3): keeping

249

nine-tenths of the bonus requires R ≳ 4.5 n, that is, about 90 complete copies per lifetime in a protocell

250

of 20 molecules. That completion, not accuracy, is what limits existing polymerase ribozymes has been

251

stated before 1,2,14,39 . Comparing protocells with surfaces in closely matched models, Shah et al. 16 found

252

that polymerases survive in protocells at a replication rate, relative to strand breakdown, about six times

253

lower than on surfaces where growth is limited locally. What is new here is the size of the gap on each

254

axis, measured against a ceiling and a fecundity requirement that are computed rather than assumed, and the

255

growth of that requirement with protocell size. Two consequences follow for experiments. First, the quantity

256

that decides whether compartments can help, the number of complete copies of the replicase’s own sequence

257

per template lifetime in the conditions where it copies itself, is not reported: for QT45 the half-life has been

258

measured in its standard reaction conditions 10 , not in the buffer in which it copies itself (SI S6). Second, a

259

fidelity target stated without a fecundity is incomplete. A shorter replicase acts on both requirements at once,

260

provided that its information content shrinks with it.

261

Unfinished copies are the third requirement. Lost, they cost fecundity by a factor 1/(1−τ), negligible for a

262

stop probability of a few percent; replicable and faster than the replicase, they cap the tolerable load of every

263

protocell that makes about one per division cycle, so that large protocells, which make more, suffer most.

264

Stop rates have been measured, but not what decides between these regimes: whether a truncated product

265

is extended, abandoned or copied, how good a template it is, how much of the stopping is dissociation

266

rather than termination (a trap experiment would tell), and the length-independent share of the copying time

267

(pre-steady-state kinetics would give it).

268

Our protocell population is infinite and unstructured, protocells do not compete for resources and divide

269

at a fixed size, there is one class of parasites, of fixed template weight, and truncated molecules come in a

270

few length classes or at every length and, unless stated, are copied without stopping (SI S9). The comparison

271

with a surface rests on one lattice model, concerns the shape of the response to b, and compares levels only

272

as orders of magnitude. The limit max(0, ln(2/θ)) is proved for the limit kernel and, as the limit of the exact

273

thresholds, for every θ; the well-mixed limit at fixed fecundity is derived in mean field, and the scaling law

274

in n/R is proved for R > n and rests, for R ≤ n, on one property of the limit process, supported numerically

275

(Methods). The information content and the number of lethal substitutions per bit have been estimated for

276

a single replicase, QT45, and fecundities are estimates from single yields and half-lives, often on templates

277

other than the replicase itself.

10


[page 11]
278

The error threshold of an RNA world is usually stated as a fidelity. Protection by protocells has a ceiling

279

and a price: protocells can at most halve the share of correct copies an RNA replicase must make, and they

280

give most of this protection only to a replicase that makes, in its lifetime, a number of complete copies

281

comparable with the number of molecules in its protocell. Unfinished copies add a third requirement: they

282

must be lost, too rare to matter, or slow templates that are themselves copied to the end. Measured polymerase

283

ribozymes are closer to the first than to the second; the third has been measured only in part.

284

Methods

285

Model and dynamics

286

A protocell is described by (F, P), N = F + P. Time is counted in molecular lifetimes. Each replicase starts

287

copies at rate R; the template is drawn among the N − 1 other molecules with weight 1 for a replicase and θ

288

for a parasite; the copy of a replicase is a replicase with probability q and a parasite otherwise; the copy of a

289

parasite is a parasite. The total copying rate is thus RF, and a copy is a new replicase with probability p(F, N)

290

of Eq. 1. Each molecule decays at rate 1 (no decay at R = ∞, where only the sequence of copies matters).

291

A protocell that reaches 2n molecules divides, each molecule going to either daughter with probability 21 ;

292

states with F ≤ 1 are dead. The model is the “R2α” replicase of Bianconi et al. 15 without their spontaneous

293

replication (the constant term in their rates), with a parasite of template weight θ instead of 1. Spontaneous

294

replication lets a lone replicase be copied without a catalyst; for a replicase of 100–200 nucleotides, whose

295

complete non-enzymatic copy is out of reach, we leave it out and treat it as a variant. In the package model of

296

Niesert et al. 6 , likewise, the molecule to be copied is drawn from the whole pool, so that a single functional

297

gene remains replicable; this also changes the limit (Extended Data Table 1). When Qβ replicase, which

298

amplifies RNA in vitro 40 , copies a 362-nt ribozyme together with shorter parasitic RNAs that arose in the

299

experiment, the parasites are copied 1.2–1.7 times faster 8,18 .

300

Threshold criterion

301

Protocells form a multitype Crump–Mode–Jagers branching process, whose Malthusian parameter has the

302

sign of ρ − 1, where ρ is the spectral radius of the mean matrix of living daughters per division 41 . The

303

threshold Uc = sup{U : ρ(U) > 1} therefore does not depend on how long cycles last, which matters at

304

finite R. We take as type the number f of replicases at division. The mean matrix is K = B H + 21−2n I,

305

where B( f, s) is the probability that the partition of a protocell with f replicases creates a daughter in the

306

transient state s = (F, P) with F ≥ 2 and N ≤ 2n − 1 (summed over both daughters), H(s, f ′ ) the probability

307

that a protocell in state s reaches division with f ′ replicases, and the last term the daughter that receives all

308

2n molecules. H solves (I − PT T )H = PT D for the jump chain restricted to transient states, by sparse LU

309

factorization. ρ(K) is computed by dense eigenvalue solvers or, for n ≥ 60, by power iteration, and the root

310

of ρ(U) = 1 by Brent’s method with tolerance 10−7 . Two codes written independently from this description

311

agree to within 5 × 10−7 on the seven finite-R thresholds computed with both (n = 20–100) and to 10−6 on

312

nine points of the scaling limit. At R = ∞, an independently written code reproduces our 70 thresholds for

313

n ≤ 60 to the four decimals given (the original bisection tolerance was (1–2) × 10−5 ); that code was itself

314

checked against a second formulation by types at birth (|∆ρ| ≤ 3 × 10−15 on 24 cases) and against a Monte

315

Carlo simulation of the branching process (agreement in ρ to within 3 × 10−4 ). Limits in n were extrapolated

11


[page 12]
316

by fitting a0 + a1 /n + a2 /n2 to the three largest sizes (SI Table S1).

317

Proofs

318

Theorem 1: in the fictitious clock where the ν = F − 1 replicase templates are copied at rate 1 and parasites

319

at rate θ, the jump chain is that of Eq. 1, ν is a Yule process of rate q whose dynamics do not involve

321

P, and E[ν(ν + 1)] grows as e2qt . When n → ∞ at fixed F, the growth phase lasts (ln k)/θ in probability,
P
and the second factorial moment of the binomial partition gives E[ d Fd (Fd − 1)] = F(F − 1)/k. Hence

322

B∞ h = k2q/θ−1 h for h = F(F − 1). The h-transformed chain has drift Eh [F ′ | F] = kλ−1 F + (3 − 2/k)kλ − 1,

323

with λ = q/θ, so that Foster’s criterion gives positive recurrence for λ < 1 and h identifies the spectral

324

radius of the infinite matrix 42,43 . This extends by one order the first-moment balance that Bianconi et al. 15

325

used to bound the threshold: the first moment of F gives inequalities, the second factorial moment gives

326

the value. Theorem 2: during growth, each copy changes F(F − 1) by 2q F(F − 1)/W in expectation, with

320

327
328

W = θ(N − 1) + (1 − θ)(F − 1). For θ ≤ 1, W ≥ θ(N − 1), and q ≤ θ/2 makes ϕ = F(F − 1)/(N − 1) a
P
supermartingale; for θ ≥ 1, W ≥ N − 1, and q ≤ 21 does. At division, E[ d ϕd ] = (1 − 21−2n )ϕ, the only

329

loss coming from daughters of size one. The Collatz–Wielandt inequality then gives ρ ≤ 1 − 21−2n , without

330

any assumption on the monotonicity of ρ in q. For θ ≥ 1, W ≤ θ(N − 1) also gives the reverse inequality

331

at q > θ/2, hence the lower bound. Theorem 3: in the fictitious clock, the parasites of a daughter form, up

332

to a number of molecules that does not grow with n, a Yule process of rate θ started from about n, so that

333

its growth phase lasts (ln 2)/θ in probability and F − 1 at division converges in law to the Yule process of

334

rate q at that time; the finite kernel therefore converges to B∞ entry by entry (with an error close to 1/n in

335

our computations). The spectral radius of the finite kernel is at least that of each of its principal submatrices,

336

which converge to those of B∞ , and these reach 22q/θ−1 because the h-transformed chain is recurrent. Hence

337

lim inf n ρn (q) ≥ 22q/θ−1 > 1 for θ/2 < q < min(θ, 1), and Theorem 2 gives the upper bound for θ ≤ 1.

338

For θ > 1 the upper bound uses three further facts. At infinite fecundity ρn never decreases as q grows,

339

at every size: the number of replicases at division increases stochastically with q and with the replicase

340

content of a protocell, and a molecule-by-molecule coupling carries this through the partition. At the single

341

point qε = min(1, θ/2)e−ε , protocells rich in replicases drift back uniformly in n, by the supermartingales

342

(F−1)F · · · (F+a−2) Γ(N−1)/Γ(N−1+Λa) with Λ = max(q, q/θ). A Schur reduction onto finitely many types

343

then carries the eigenrelation of B∞ over to ρn (qε ) < 1 for large n, so that lim supn Uc (n) ≤ max(0, ln(2/θ))+ε.

344

Full proofs are in SI S1–S2.

345

Approach to the limit

346

The exact thresholds approach the limit as Uc (n) = ln(2/θ) + ζ(θ)/n. For θ ≤ 2, a formal expansion to first

347

order gives ζ(θ) = 2(1−1/θ)/ ln 2 (SI S2): −2.885 at θ = 0.5 and +0.962 at θ = 1.5, against −2.88 and +0.962

348

fitted to the exact thresholds, and 0 at θ = 1, where the correction is exponentially small (−21−2n / ln 2). For

349

θ ≥ 2, where the limit is zero, the exact thresholds decrease numerically as about 1/n. With any partition

350

that ignores which molecules are replicases, the threshold is at most ln 2 + max(0, ln(1/θ)) at every size and

351

fecundity, and at θ = 1 and infinite fecundity it equals ln 2 at every size when no daughter receives a single

352

molecule and some daughter receives between 2 and 2n − 1, as with a hypergeometric partition (SI S2). With

353

growth by a factor k and division into k daughters the threshold is again q = θ/2 (Theorem 1): the factor two

354

is thus not the familiar requirement that “at least half of the daughters should, on average, survive” in binary

355

fission 18 , which would give ln k with k daughters.
12


[page 13]
356

Finite fecundity

357

At θ = 1, for Z = F(F − 1)Γ(N − 1)/Γ(N − 1 + 2q) and N ≥ 3, the copying terms of the generator cancel

358

exactly and E[dZ] = −2(1 − q)Z dt (checked on 2 × 104 random states to a relative error of 3.5 × 10−8 , and

359

in exact rational arithmetic): between divisions Z decays at exactly the rate 2(1 − q) per molecular lifetime,

360

whatever the state of the protocell, and a division multiplies its expectation by the R = ∞ spectral radius. For

361

every θ, with q replaced by Λ = max(q, q/θ), Z remains a supermartingale if Λ ≤ 1, which bounds ρ at every

362

size and fecundity by the R = ∞ spectral radius at θ = 1 and q = Λ; for Λ ≥ 1 row sums bound ρ by its

363

value at θ = 1, q = 1 and R = ∞ (SI S2). The mean-field limit Eq. 2 follows from ẋ = Rx2 (q − ω)/ω with

364

ω = x + θ(1 − x), for the replicase fraction x, and d ln N/dt = Rx − 1. The exact thresholds approach it slowly,

365

empirically as n−1/2 for θ < 1 (for θ = 0.5 and R = 10: 0.823, 0.721 and 0.657 at n = 20, 100 and 400,

366

against 0.598), and as ≈ 2/n towards zero for θ = 1.5; the convergence is not proved. Shah et al. 16 concluded

367

that “Mmax must tend to zero for very large S 0 ”, S 0 being the number of strands at which protocells divide;

368

Eq. 2 agrees with this for θ ≥ 1, whereas at R = ∞ the threshold of their model tends to ln(1.9486/θ). The

369

limit process of Theorem 4 is obtained by letting n, R → ∞ at fixed y with F = O(1), and the finite kernels

370

are proved to converge to its kernel (SI S3): parasites then follow their mean to relative order N −1/2 and

371

W = θN(1 + O(1/N)), and the process is piecewise deterministic for F and u = N/R: u̇ = F − u between

372

jumps, F → F + 1 at rate λF(F − 1)/u, F → F − 1 at rate F, and division at u = 2y. There Z = F(F − 1)u−2λ

373

decays at rate 2(1 − λ) and each division multiplies it by 22λ−1 ; the threshold is where the two balance,

374

(22λ−1 − 1) κ = 2(1 − λ) (an exact rewriting at threshold, provided the Z-moments are finite; SI S3), with

375

κ the Z-weighted division rate of the stable population: at R = ∞ cycles take no time, κ = ∞ and λc = 12 ;

376

as y grows cycles lengthen, κ falls and λc rises towards one. The process was simulated by exact sampling

378

of the jumps along the deterministic flow, without population control, to estimate ψ(y) independently of the
√
kernels (SI S3). The slope of ψ at the origin is −(3 2 − 4)/ ln 2 = −0.350 (proved; SI S14), and beyond

379

y ≈ 30 ψ decays more slowly than the fit given in the main text. A related scaling law, in which the size of

380

a collective and the mutation rate combine into a single variable, governs the balance between within- and

381

among-collective evolution in another model 44 .

382

Unfinished copies

383

Exact kernels with replicases, parasites and truncated molecules, and the three identities, are given in SI S8.

384

At θ′ = 2 the tolerable loads for n = 10 to 30 differ by 3% at nτ = 0.3. Over the range computed at finite

385

fecundity (n ≤ 20, R ≥ 10, τ ≤ 0.03) the replicable fate costs 16 to 310 times more load than the lost one,

386

and the share of the tolerable load that it removes hardly depends on fecundity. Whether copies of truncated

387

templates stop in turn decides how the threshold scales with protocell size. If they do not, slow truncated

388

copies form a bath in which the lineages that carry growth copy the replicase only two to three times per

389

cycle, and τc tends to a finite limit, 0.18 at b = 0 with two classes at the elbow; if they do, as on the lattice,

390

these lineages are made mostly of replicases and τc falls as 1/n (SI S9, SI Fig. S1).

391

Termination and copying time

392

A dissociation interrupts a copy without ending it: the polymerase rebinds and completes it. With a copying

393

time β(1+lδ)+αl for a product of length l, where δ is the mean number of dissociations per nucleotide added,

394

α the time per nucleotide and β the length-independent time, the copying time stays affine in l, on average

377

13


[page 14]
395

along the template, so that dissociation enters only through b = 1/[1 + L(δ + α/β)]. A polymerase that adds

396

the nucleotide at position i before releasing its product with probability Pi , its processivity coefficient, has

397

δ equal to the mean of (1 − Pi )/Pi , at least (1 − P̄)/P̄ for the mean P̄, hence b ≤ 1/[1 + L(1 − P̄)/P̄]. The

398

ratio of copying times T (L)/T (L′ ) is the template advantage θ′ under mass action, each replicase–template

399

pair copying at a rate set by the copying time; if replicases are saturated by templates, a shorter copying time

400

raises fecundity instead, and θ′ is set by binding. A true termination ends the copy and releases its product,

401

which is then lost or copied as a truncated molecule; with a probability m per nucleotide, τ = 1 − (1 − m)L .

402

In the protocell variant of Fig. 5A, which copies as the lattice does, a product shorter than 10 nucleotides

403

is lost, copies of truncated templates stop with the same probability m per nucleotide (retruncation), and a

404

copy that stops early ends sooner: a product of relative length ξ is made at a rate multiplied by θ′ (ξ). Exact

405

kernels with unfinished copies, the classes used for a distribution of truncated lengths and the population

406

Monte Carlo over every truncated length (points of Fig. 5A) are described in SI S8–S9.

407

Comparison with the lattice

408

The lattice model of Tupper and Higgs 5 , its threshold read on their published figure, and an independent

409

reimplementation are described in SI S10. If its threshold grows with b, the reimplementation recovers

410

half of the damage between b = 0.10 and 0.15 with runs to t = 120 and to t = 500, each bound resting

411

on a single run (between 0.05 and 0.25, or 0.45 at t = 500, at worst with one run more or fewer), and

412

between 0.05 and 0.15 at t = 120 with the 5% survival criterion of the published lattice (SI S10). At infinite

413

fecundity, protocells that copy as the lattice does tolerate more termination than the lattice only below about

414

300 molecules at b = 0 and 30 at b = 0.15–0.25, and at every size beyond b ≈ 0.53, where the large-protocell

415

limit of their threshold, derived for the limit kernel (SI S9), exceeds that of the lattice. At finite fecundity

416

they do so only below a finite size: at R = 25, the copying rate kpol of the lattice, about 20 to 33 molecules for

417

b = 0.3 to 0.6 and 230 at b = 1; at R = 3, protocells of 20 molecules tolerate less termination than the lattice

418

at every b computed (0.3 to 1). These levels compare only as orders of magnitude (SI S9). Round-18 adds

419

a nucleotide before releasing its product with a probability that varies about twentyfold with the position on

420

the template, up to 0.9 (ref. 45), which for a 100-nucleotide replicase gives b ≤ 0.083 by the bound above,

421

and b ≤ 0.0033 if that probability were 0.25 all along the template, its value at the position where its rate

422

constants were bounded. For a tC9Y-type polymerase 46 , b is not anchored by any measurement.

423

Measured systems

424

The load is U = ℓIε with ℓ = 0.56 (0.51–0.60; central value with the tolerated base pairs placed at random)

425

and I = 53.2 bits, both computed from the tolerance of each site of QT45 measured by Gianni et al. 10 (SI S6).

426

I is − log2 of the abundance of QT ribozyme folds in random sequence, 9.5 × 10−17 ; a substitution counts as

427

lethal when it lowers activity below 80% of the wild type, their criterion (0.51–0.60 from the site tolerances

428

alone, 0.56–0.59 with the double mutants). Applying each error rate to a 53-bit replicase is a normalization:

429

the other polymerases are longer, and their information content is unknown. Most published error rates are

430

measured on full-length products; a copy stalled by a mismatch 47,48 does not appear among them, so that

431

U computed from them is the load of complete parasites, and the cost of stalling appears in the measured

432

fecundity. Fecundity is R = Y t1/2 /(T ln 2) for a yield Y of complete copies per template after a reaction time

433

T , and a template half-life t1/2 , assuming synthesis linear in time. In the model, R is the number of copies

14


[page 15]
434

a replicase starts per lifetime, all of which complete; if catalysts and templates have the same lifetime and

435

are drawn from one population, it equals the number of complete copies made per template lifetime. In the

436

experiments the catalyst is often in excess over the template, so that fecundity per replicase is lower, by up to

437

that excess. The fraction of copying slots that end in a complete copy is σ = Ytc /T , with tc the time needed

438

to make one copy of the object (given, or bounded, in SI Table S4 for each system for which σ is reported);

439

it involves no lifetime. The fragment of the TPR grows by up to a factor of 1.26 per cycle, which bounds its

440

fecundity from below. The fidelity targets of the scaling limit agree with the exact kernel at n = 50 to within

441

7 × 10−4 . Values, sources, conversions and caveats are given in SI S6.

442

Status of the results

443

The limit max(0, ln(2/θ)) is proved for the limit kernel and, as the limit of the exact thresholds, for every θ.

444

The bound un + max(0, ln(1/θ)) is proved at every size and fecundity. The well-mixed limit at fixed fecundity

445

is derived in mean field only. For the variants that exceed the ceiling (Extended Data Table 1), the bound

446

of the lever, the absence of a threshold for χ ≥ 1 and for self-copying at infinite fecundity, the invariance

447

of the invasion threshold under fusion between protocells and the fact that no fusion raises it above the

448

ceiling are proved (SI S12); the other results on them are proved, derived or numerical as stated in SI S2 and

449

S5. The three identities for unfinished copies are exact, Theorem 2 extends to them, for a stop probability

450

per nucleotide at θ = 1 and, for one per copy, whenever θ′ ≥ min(θ, 1) (SI S8); with incomplete copies of

451

several kinds, lim inf n mc (n) ≥ m∞ and, without inert strands, the ceiling, its total-load form when all become

452

parasites and the bracket at R = ∞ by the extreme classes are proved, and a stationary bath’s threshold is

453

conjectural (SI S8, S9); the large-protocell limit of the threshold with retruncation beyond b = 4/9 is derived

454

for the limit kernel, its identification with the limit of the exact thresholds being conjectural; everything else

455

about them is numerical, for protocells of at most 80 molecules (160 with one class at finite fecundity, 320

456

with every length or at b = 1) and, through limit kernels, for n = ∞, except the decrease of the threshold to

457

zero at finite fecundity, derived in mean field at b = 1. The scaling law in n/R is proved for R > n (SI S3,

458

S13); for R ≤ n the finite kernels are proved to converge to those of a limit process wherever max(q, q/θ) ≤ 1,

459

a range that contains the thresholds, and SI S3 reduces the law to one unproved property of that process,

460

supported numerically, without which the thresholds are only bracketed asymptotically. For R ≤ n/5 the

461

threshold is at most max(0, ln(1/θ)) + ln(1024/725), less than half of the bonus above max(0, ln(1/θ)), at

462

every size (proved, computer-assisted; SI S3); for θ ≤ 1, large protocells keep more than half at every

463

fixed n/R ≤ 2.858 and less than half at every fixed n/R ≥ 3.2 (proved, computer-assisted; SI S3). Eq. 3

464

also assumes that ψ decreases with y, which is certified only on the grid y = k/20 < 1 (SI S3). Copying

465

is instantaneous, its duration being absorbed into R, and all molecules decay at the same rate; template

466

advantages are derived from copying times, which assumes mass action. If fewer substitutions are fully

467

inactivating than those counted as lethal, the loads are lower; other compositions of sites would allow ℓ = 0.5–

468

1.1, a factor of 2.2 on the load, and published fidelities of a given polymerase differ by a factor of up to 4.4

469

in error rate. The threshold of the reimplemented lattice depends on the length of its runs and, at t = 120,

470

perhaps on its size (SI S10).

471

Use of AI tools

472

[Draft, to be confirmed or rewritten by the author, who alone can state what he did himself and how the tools

473

were used; keep the bracketed items only if they apply. The author’s own statement, relayed on 4 October:
15


[page 16]
474

the ideas and the direction of the research are his; the proofs and the simulations were made by the AI. That

475

statement and the bracketed items below overlap: model variants, a scaling law, mechanisms, an interpreta-

476

tion and conclusions are ideas. Keep for each the attribution that is accurate; where the programme’s notes

477

record one, it must agree with them, since they may be deposited; they record, for example, that the bath of

478

slow truncated copies (Unfinished copies; SI S9) was proposed, as an unproven reading, by an AI session

479

whose computations showed where the mechanism the author first proposed fails, and established by another

480

at his request, after he had noted that this mechanism failed in half of the cases; and that the results added to

481

SI S2 and S3 on 7 October (the bound at every fecundity, the spectrum at θ = 1, the limit for θ > 1 and the

482

reduction of the scaling law) were obtained by AI sessions at his request of 6 October (proved, except the

483

reduction of the scaling law, which was then derived), the argument for θ > 1 following a repair proposed by

484

one of the sessions that checked it. The results added on 12 October (the ceiling for any division that ignores

485

which molecules are replicases, with complementary strands; the bracket on the price; the convergence of

486

the kernels at every y; (H3) at every y; and the bracket without (H2)) were obtained by AI sessions at his

487

requests of 7 October; the lever, spontaneous replication, partial self-copying and protocell fusion (SI S2 and

488

S5; Extended Data Figs. 3–6), added for v0.16, were obtained by AI sessions at his requests of 12 October,

489

the ideas and the direction being his (for the lever, the law itself) and the exact statements, the proofs and

490

the computations the AI’s; [the bound for R ≤ n/5 (SI S3; report of 7 October), the comparison with the

491

model of Shah et al. 16 (SI S5; his request of 12 October) and the proposal for measuring R (SI S6) were

492

also obtained by AI sessions, as were the certified bounds on ψ (SI S3), transient compartmentalization and

493

complementary strands at finite fecundity (SI S5; his requests and agreement of 12 October), and the frontier

494

of half the bonus, the pair density at finite size, the upper bounds on Rmin , the bounds for y ≥ 1 and the

495

extinction bound (SI S3; 12 October);] [Theorem 4 for R > n and its proof (the size clock, the uniform drift

496

and the convergence of the kernels for R > n; SI S13, at his requests of 6 and 7 October, written in English

497

for this version), the slope of ψ (Theorem S, SI S14), the necessary price (Theorem Q, SI S3), the results on

498

incomplete copies and baths of several lengths (SI S8 and S9), Extended Data Fig. 7 and the literature on

499

self-copying (SI S5) were obtained by AI sessions of the lineage “fusion” (requests and dates to be stated

500

by the author);] Fig. 1, the title, the summary and the one-sentence thesis of the Discussion were proposed

501

by an AI session and chosen by him on 6 October (on 12 October AI sessions kept “established” in the

502

summary in place of his “computed” and, for v0.18.2, replaced “known to copy itself” by “that has copied

503

its own sequence” and “has not been established” by “remains unknown”, removed “we conjecture” once the

504

scaling law was proved for R > n, and, for v0.16, added “as computed” and “for a sterile lone replicase”);

505

on 12 October AI sessions worked autonomously, with his authorization, and made the remaining choices

506

of this version.] [The research questions and the direction of the research are the author’s.] This work was

507

carried out with extensive use of AI systems (Claude, Anthropic[; model versions]). They wrote and ran

508

the simulation and analysis code, devised and wrote the proofs, [proposed the model variants, the scaling

509

law, the mechanism of catalyst–template pairs and that of the bath of slow truncated copies, proposed the

510

interpretation of the results and the conclusions, searched the literature and chose the references,] extracted

511

the experimental data from the literature, checked the references against primary sources where these could

512

be accessed, and drafted and revised the text. The independent implementations and checks mentioned in

513

the Methods and the Results were written and run in separate sessions of the same AI system, not by the

514

sessions whose results they checked. [What the author did himself: . . . ] The author takes full responsibility

515

for the content.

16


[page 17]
516

Data availability

517

The thresholds, figure data and the logs of every computation, and the notes that give the full proofs and

518

computations of SI S2, S3 and S5 (listed in SI S7), will be deposited with the code on publication (Code

519

availability) and are available to the editors and referees on request. The lattice runs of the reimplementation

520

will be deposited with its simulation code, the definitions of its series and the output of each point (SI S7).

521

[to be confirmed by the author; or deposit before submission and give the repository and DOI]

522

Code availability

523

All thresholds, figures and tables are produced by Python scripts (NumPy, SciPy), and the lattice runs by a

524

program in C; the scripts, with their logs and outputs and the notes that give the full proofs of SI S2, S3 and

525

S5 (SI S7), will be deposited in a public repository on publication (SI S7) and are available to the editors and

526

referees on request. [to be confirmed by the author; or deposit before submission and give the repository and

527

DOI]

528

References

529
530

531
532

[1] P. G. Higgs and N. Lehman. The RNA World: molecular cooperation at the origins of life. Nat. Rev.
Genet., 16:7–17, 2015.
[2] F. Wachowius, J. Attwater, and P. Holliger. Nucleic acids: function and potential for abiogenesis. Q.
Rev. Biophys., 50:e4, 2017.

533

[3] J. Maynard Smith. Hypercycles and the origin of life. Nature, 280:445–446, 1979.

534

[4] B. Obermayer and E. Frey. Error thresholds for self- and cross-specific enzymatic replication. J. Theor.

535

536
537

538
539

540
541

Biol., 267:653–662, 2010.
[5] A. S. Tupper and P. G. Higgs. Error thresholds for RNA replication in the presence of both point
mutations and premature termination errors. J. Theor. Biol., 428:34–42, 2017.
[6] U. Niesert, D. Harnasch, and C. Bresch. Origin of life between Scylla and Charybdis. J. Mol. Evol., 17:
348–353, 1981.
[7] E. Szathmáry and L. Demeter. Group selection of early replicators and the origin of life. J. Theor. Biol.,
128:463–486, 1987.

542

[8] S. Matsumura, Á. Kun, M. Ryckelynck, F. Coldren, A. Szilágyi, F. Jossinet, C. Rick, P. Nghe, E. Szath-

543

máry, and A. D. Griffiths. Transient compartmentalization of RNA replicators prevents extinction due

544

to parasites. Science, 354:1293–1296, 2016.

545
546

[9] M. Eigen. Selforganization of matter and the evolution of biological macromolecules. Naturwissenschaften, 58:465–523, 1971.

547

[10] E. Gianni, S. L. Y. Kwok, C. J. K. Wan, K. Goeij, B. E. Clifton, E. S. Colizzi, J. Attwater, and P. Holliger.

548

A small polymerase ribozyme that can synthesize itself and its complementary strand. Science, 391:

549

1022–1028, 2026.
17


[page 18]
550
551

552
553

554
555

[11] Á. Kun, M. Santos, and E. Szathmáry. Real ribozymes suggest a relaxed error threshold. Nat. Genet.,
37:1008–1011, 2005.
[12] A. Szilágyi, Á. Kun, and E. Szathmáry. Local neutral networks help maintain inaccurately replicating
ribozymes. PLoS One, 9:e109987, 2014.
[13] Á. Kun, A. Szilágyi, B. Könnyű, G. Boza, I. Zachar, and E. Szathmáry. The dynamics of the RNA
world: insights and challenges. Ann. N. Y. Acad. Sci., 1341:75–95, 2015.

556

[14] Á. Kun. Maintenance of genetic information in the first ribocell. In S. Müller, B. Masquida, and W. Win-

557

kler, editors, Ribozymes: Principles, Methods, Applications, chapter 14. Wiley-VCH, Weinheim, 2021.

558

doi: 10.1002/9783527814527.ch14.

559
560

561
562

563
564

565
566

567
568

569
570

571
572

573
574

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

575

[23] J. J. Bull and C. O. Wilke. Lethal mutagenesis of bacteria. Genetics, 180:1061–1070, 2008.

576

[24] M. H. A. Davis. Piecewise-deterministic Markov processes: a general class of non-diffusion stochastic

577

578
579

models. J. R. Stat. Soc. B, 46:353–388, 1984.
[25] N. Takeuchi and P. Hogeweg. Multilevel selection in models of prebiotic evolution II: a direct comparison of compartmentalization and spatial self-organization. PLoS Comput. Biol., 5:e1000542, 2009.

580

[26] J. W. Szostak. Functional information: Molecular messages. Nature, 423:689, 2003.

581

[27] J. J. Bull, L. A. Meyers, and M. Lachmann. Quasispecies made simple. PLoS Comput. Biol., 1:e61,

582

2005.

18


[page 19]
583
584

585
586

587
588

589
590

[28] D. P. Horning and G. F. Joyce. Amplification of RNA by an RNA polymerase ribozyme. Proc. Natl.
Acad. Sci. U.S.A., 113:9786–9791, 2016.
[29] K. F. Tjhung, M. N. Shokhirev, D. P. Horning, and G. F. Joyce. An RNA polymerase ribozyme that
synthesizes its own ancestor. Proc. Natl. Acad. Sci. U.S.A., 117:2906–2913, 2020.
[30] X. Portillo, Y. T. Huang, R. R. Breaker, D. P. Horning, and G. F. Joyce. Witnessing the structural
evolution of an RNA enzyme. eLife, 10:e71557, 2021.
[31] N. Papastavrou, D. P. Horning, and G. F. Joyce. RNA-catalyzed evolution of catalytic RNA. Proc. Natl.
Acad. Sci. U.S.A., 121:e2321592121, 2024.

591

[32] J. Attwater, T. L. Augustin, J. F. Curran, S. L. Y. Kwok, L. Ohlendorf, E. Gianni, and P. Holliger.

592

Trinucleotide substrates under pH–freeze–thaw cycles enable open-ended exponential RNA replication

593

by a polymerase ribozyme. Nat. Chem., 17:1129–1137, 2025.

594
595

596
597

598
599

600
601

602
603

604
605

606
607

608

[33] A. Wochner, J. Attwater, A. Coulson, and P. Holliger. Ribozyme-catalyzed transcription of an active
ribozyme. Science, 332:209–212, 2011.
[34] P. Hogeweg and N. Takeuchi. Multilevel selection in models of prebiotic evolution: compartments and
spatial self-organization. Orig. Life Evol. Biosph., 33:375–403, 2003.
[35] N. Takeuchi and P. Hogeweg. Evolutionary dynamics of RNA-like replicator systems: a bioinformatic
approach to the origin of life. Phys. Life Rev., 9:219–263, 2012.
[36] P. Szabó, I. Scheuring, T. Czárán, and E. Szathmáry. In silico simulations reveal that replicators with
limited dispersal evolve towards higher efficiency and fidelity. Nature, 420:340–343, 2002.
[37] Y. E. Kim and P. G. Higgs. Co-operation between polymerases and nucleotide synthetases in the RNA
world. PLoS Comput. Biol., 12:e1005161, 2016.
[38] N. Takeuchi and P. Hogeweg. The role of complex formation and deleterious mutations for the stability
of RNA-like replicator systems. J. Mol. Evol., 65:668–686, 2007.
[39] C. Jeancolas, C. Malaterre, and P. Nghe. Thresholds in origin of life scenarios. iScience, 23:101756,
2020.
[40] D. R. Mills, R. L. Peterson, and S. Spiegelman. An extracellular Darwinian experiment with a self-

609

duplicating nucleic acid molecule. Proc. Natl. Acad. Sci. U.S.A., 58:217–224, 1967.

610

[41] P. Jagers. Branching Processes with Biological Applications. Wiley, London, 1975.

611

[42] D. Vere-Jones. Ergodic properties of nonnegative matrices. I. Pacific J. Math., 22:361–386, 1967.

612

[43] E. Seneta. Non-negative Matrices and Markov Chains. Springer, New York, 2006. Revised printing.

613

[44] N. Takeuchi, N. Mitarai, and K. Kaneko. A scaling law of multilevel evolution: how the balance

614

615
616

between within- and among-collective evolution is determined. Genetics, 220:iyab182, 2022.
[45] M. S. Lawrence and D. P. Bartel. Processivity of ribozyme-catalyzed RNA polymerization. Biochemistry, 42:8748–8755, 2003.
19


[page 20]
617
618

[46] J. Attwater, A. Wochner, and P. Holliger. In-ice evolution of RNA polymerase ribozyme activity. Nat.
Chem., 5:1011–1018, 2013.

619

[47] S. Rajamani, J. K. Ichida, T. Antal, D. A. Treco, K. Leu, M. A. Nowak, J. W. Szostak, and I. A. Chen.

620

Effect of stalling after mismatches on the error catastrophe in nonenzymatic nucleic acid replication. J.

621

Am. Chem. Soc., 132:5880–5885, 2010.

622

[48] K. Leu, E. Kervio, B. Obermayer, R. M. Turk-MacLeod, C. Yuan, J. M. Luevano, E. Chen, U. Gerland,

623

C. Richert, and I. A. Chen. Cascade of reduced speed and accuracy after errors in enzyme-free copying

624

of nucleic acid sequences. J. Am. Chem. Soc., 135:354–366, 2013.

625
626

627
628

629
630

631
632

633
634

[49] J. Attwater, A. Raguram, A. S. Morgunov, E. Gianni, and P. Holliger. Ribozyme-catalysed RNA synthesis using triplet building blocks. eLife, 7:e35255, 2018.
[50] N. Paul and G. F. Joyce. A self-replicating ligase ribozyme. Proc. Natl. Acad. Sci. U.S.A., 99:12733–
12740, 2002.
[51] J. A. Doudna, S. Couture, and J. W. Szostak. A multisubunit ribozyme that is a catalyst of and template
for complementary strand RNA synthesis. Science, 251:1605–1608, 1991.
[52] R. Green and J. W. Szostak. Selection of a ribozyme that functions as a superior template in a selfcopying reaction. Science, 258:1910–1915, 1992.
[53] S. H. A. von der Dunk, E. S. Colizzi, and P. Hogeweg. Evolutionary conflict leads to innovation:
symmetry breaking in a spatial model of RNA-like replicators. Life, 7:43, 2017.

635

[54] E. Gianni, S. L. Y. Kwok, C. J. K. Wan, K. Goeij, B. E. Clifton, J. Attwater, and P. Holliger. A

636

polymerase ribozyme that can synthesize both itself and its complementary strand. bioRxiv, 2024. doi:

637

10.1101/2024.10.11.617851. Preprint, version posted 12 October 2024.

638
639

[55] Y. Li and R. R. Breaker. Kinetics of RNA degradation by specific base catalysis of transesterification
involving the 2′ -hydroxyl group. J. Am. Chem. Soc., 121:5364–5372, 1999.

640

[56] H. K. Wayment-Steele, D. S. Kim, C. A. Choe, J. J. Nicol, R. Wellington-Oguri, A. M. Watkins, R. A.

641

Parra Sperberg, P. S. Huang, Eterna Participants, and R. Das. Theoretical basis for stabilizing messenger

642

RNA through secondary structure design. Nucleic Acids Res., 49:10604–10617, 2021.

643
644

645
646

[57] R. N. Goldberg, N. Kishore, and R. M. Lennen. Thermodynamic quantities for the ionization reactions
of buffers. J. Phys. Chem. Ref. Data, 31:231–370, 2002.
[58] H.-O. Georgii and E. Baake. Supercritical multitype branching processes: the ancestral types of typical
individuals. Adv. Appl. Probab., 35:1090–1110, 2003.

647

Acknowledgements

648

[to be completed by the author]

20


[page 21]
649

Author contributions

650

[L.C. conceived the study and directed the work.] The AI systems described in Methods (Use of AI tools)

651

carried out the analysis, the computations and the proofs[, proposed the model variants, the scaling law, the

652

mechanisms, the interpretation and the conclusions, searched the literature and chose the references] and

653

drafted the paper. [What L.C. did himself: . . . ] [Draft, to be confirmed by the author; it must agree with

654

Use of AI tools item by item, including the author’s statement on the ideas, and state L.C.’s own contribution

655

under the authorship criteria of Nature Portfolio.]

656

Competing interests

657

The author declares no competing interests. [draft, to be confirmed by the author]

658

Additional information

659

Supplementary Information is available for this paper. Correspondence and requests for materials should be

660

addressed to L.C.

21


[page 22]
661

Extended Data
Extended Data Table 1 | What the factor two depends on, and what exceeds it. Limit threshold Uc (∞) =
max(0, ln(1/θ) + ln(1/λc )), where λc = qc /θ is the threshold of the limit kernel, which depends on q and θ only
through their ratio; infinite fecundity unless stated. r̄: the largest expected fraction of the mother’s ordered replicase
pairs that the two daughters of an equal division keep together, and λ∗ = min(1, 12 log2 (1/r̄)); c: weight of a replicase’s
own sequence as its template, relative to another replicase; χ: correct uncatalysed copies of a lone replicase per lifetime.
Proofs for the last five rows: SI S12.
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

22

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


[page 23]
Extended Data Table 2 | Measured polymerase ribozymes against the first two requirements, for a 53-bit replicase
with ℓ = 0.56 and θ = 1. 1 − ε: per-nucleotide fidelity. Load gap: U/ ln 2, the factor by which the error load exceeds the
protocell ceiling at infinite fecundity. Fecundity gap: 1/R, the factor by which fecundity per template falls short of the
minimum R = 1 at vanishing load; for QT45, its lower end rests on a half-life extrapolated to the nominal, pre-freezing
composition of the copying buffer (5–25 given the potassium uncertainties of that extrapolation, 27 with 200 mM KCl
in the buffer of the measurement; SI S6). σ: fraction of copying slots that end in a complete copy (Methods); for QT45
an upper bound, copying its own sequence (≤ 1.7 × 10−3 copying its complement), since its copy time is not measured.
Sources, conversions and caveats: SI Table S4.
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

24-3 (refs. 28,29)
52-2 (refs. 30,31)
TPR, 29-nt own
fragment 32
tC19Z 33
a

b

Fidelity of the ancestor t5+1 (ref. 49), borrowed. Full-length products; 0.92 when all products, including partial ones, are
counted 28,29 .

23


[page 24]
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

2.0
limit threshold Uc( )

error threshold Uc = lnqc

A The exact threshold approaches ln(2/ )

B The protocell adds at most ln 2, catalysis nothing
protocell: ln(2/ )
complementary strands: ln(1.95/ )
equal partition: ln(1.44/ )
well mixed: max(0, ln(1/ ))

1.5
1.0
0.5
0.0

off scale: a replicator copied
in cis, with selective superiority
s = 351, has Uc = lns = 5.86

0.5
1.0
1.5
2.0
2.5
template efficiency of parasites,

Extended Data Fig. 1 | The ceiling at infinite fecundity. (A) Exact threshold Uc (n) for θ = 0.5, 1 and 1.5 (independent
kernel; points), with the limits ln(2/θ) (dashed). For θ ≤ 1 the threshold stays below the limit at every size and converges
to it (Theorems 2 and 3); for θ > 1 small protocells do substantially better than large ones (at θ = 1.5, 0.557 at n = 3
against a limit of 0.288, Theorem 3), but never reach ln 2, the θ = 1 line (Theorem 2). (B) Limit threshold against the
template efficiency of parasites, for protocells with binomial partition (ln(2/θ), Theorem 3), complementary strands
(ln(1.9486/θ)), an equal partition of replicases (ln(1.44/θ)), and for the well-mixed pool (max(0, ln(1/θ))). Catalytic
efficiency enters none of them. A replicator copied in cis with the selective superiority s = 351 used by Kun et al. 11
would have Uc = 5.86, off scale.

24


[page 25]
A Measured systems lie outside the viable region
=1
= 1.5
n = 10

ln 43 ln 2
3
10 viable
( = 1, n = 10)

n = 50
measured systems

102
101
TPR, 29-nt own fragment
R = 1: a replicase must at least replace itself
52-2

100
10 1

24-3

QT45, own sequence
and complement
tC19Z fidelity (fecundity unknown)

10 2
10 3

0

104
103

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

Extended Data Fig. 2 | Requirements and measured polymerase ribozymes. (A) Error load U (for a 53-bit replicase with ℓ = 0.56, errors counted as complete parasites) and fecundity R (complete copies per template lifetime) of
measured systems (Extended Data Table 2; SI Table S4), against the exact viability boundaries U = Uc (n, R, θ) for
n = 10 (solid) and n = 50 (dashed), θ = 1 (orange) and θ = 1.5 (green); the shaded region is viable for θ = 1, n = 10.
Dotted vertical lines: the large-protocell limits at R = ∞, ln 2 and ln(4/3). No replicase is maintained below R = 1.
The QT45 bar spans the fecundities of its own sequence and of its complement, with the measured half-life and one
extrapolated from it to its copying buffer; 24-3 is placed at its full-length fidelity (counting partial products would put
it at U = 2.38); the 52-2 bar spans a fecundity measured on a ligase and one extrapolated from a short reaction, and
the horizontal arrow indicates that its lowest published fidelity is off scale (U = 4.7); the upward arrow marks a lower
bound on the fecundity of the TPR fragment; tC19Z has the highest average measured fidelity, but its fecundity on
its own sequence is unknown. (B) Fecundity required in a protocell of n molecules for four values of the effective
load U + ln θ: scaling law (Eq. 3; lines) and exact kernels at n = 10 and 50 (points, interpolated between computed
boundaries; exact roots in Fig. 1B). Grey band: fecundity of QT45 on its own sequence and on its complement.

25


[page 26]
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

Extended Data Fig. 3 | The lever: how a division that keeps replicase pairs together raises the ceiling. Partial
sorting: at division, all replicases go to one daughter with probability p, otherwise at random. The two equal daughters
then together keep on average a fraction r̄ = (1 + p)/2 of the mother’s ordered replicase pairs, and the lever bound
is λc ≥ λ∗ = 21 log2 (1/r̄). (A) Compartment bonus ψ(y) = − ln λc of the limit process against y = n/R, for p = 0
√
(random partition), 0.2, 2 − 1, 0.6 and 23/4 − 1. Dashed lines: the ceilings ln(1/λ∗ ), that is ln 2, ln 4 and ln 8 for one,
two and three bits, reached as y → 0 (proved). Dotted lines: − ln λL (p), a lower bound on ψ at every y obtained from
replicase-rich protocells, which partial sorting keeps rich (derived, not proved). Filled circles: thresholds converged
in the truncation (|∆λc | < 10−4 , numerical); open circles: thresholds of the kernel truncated at 400 replicases, not
converged. Triangles: for p > 0, points beyond λ3 (p) = 13 log2 (4/(1 + 3p)), where no admissible cut is proved; there
λc is defined through finite truncations (SI S12), and the plotted value is that of the truncated kernel. Open symbols
bound ψ from below (numerical), loosely where the truncation is far from convergence. (B) Exact thresholds of the
finite model at θ = 1 and infinite fecundity, against protocell size n, for the same p; dashed lines as in A, thin solid lines
the finite-size bounds ln(1/λ∗n ). The thresholds never exceed ln(1/λ∗n ) (proved), with equality for p = 0. For p > 0 they
lie above ln(1/λ∗ ) from n = 40 to n = 160 and decrease towards it (numerical); at n = 10 they lie below it, except for
p = 0.2.

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

Extended Data Fig. 4 | A lone replicase copied without a catalyst pierces the ceiling. (A) Limit ψ(0; χ) for large
protocells at high fecundity (y = n/R → 0) against χ, the number of correct uncatalysed copies of a lone replicase
per lifetime, from the reduced kernel (numerical): revival at a stage of growth uniform in N, as in our model (solid),
15
or uniform in ln N, as with the exponential growth
√ of mass-action catalysis in the R2α model of Bianconi et al.
(dashed); dotted, the first-order expansion ln 2 + (3 2 − 4)χ (derived). In R2α, χeff = q, so that the predicted threshold
for α, m → ∞ (α ≪ 2m ) lies where the dashed curve meets U = − ln χ (dot, U ∗ = 0.903). Grey lines: the ceiling ln 2 of
a sterile lone replicase, 10% above it, and 2 ln 2. (B) ψ(y; χ) at finite fecundity for χ = 0, 0.1, 0.3 and 0.5 (limit process,
q s = q, θ = 1; numerical); at θ = 1 the threshold is Uc → ψ. Only for χ = 0 does ln 2 (dashed) bound ψ at every y.

26


[page 27]
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

Extended Data Fig. 5 | A replicase that can copy itself has no ceiling at high fecundity, because the limits of
infinite fecundity and vanishing self-copying do not commute. (A) ψ = − ln λc of the limit process (lines) against
y = n/R, for a weight c of the replicase’s own sequence as template relative to another replicase (c = 0: trans copying,
the model of the main text; c = 1: the self-copying variant of SI S1). For c > 0 the identification of ψ with the limit
of Uc + ln θ is numerical; circles: exact kernels at n = 40, θ = 1. Dashed: the ceiling ln 2 of trans copying. At c = 0,
ψ stays below ln 2 at every y; for every c > 0 it diverges as y → 0, as ln(c ln 2/y) + O(1) (proved), but exceeds ln 2
only when c exceeds a value that vanishes with y (0.0083 at y = 0.05). (B) The same threshold at high fecundity as a
function of c̃ = c/y = cR/n alone (κ in the figure; Λ for λcis ): − ln λcis (c̃) from λc̃ ln 2 [G(λ) − 1] = 1 (line, derived and
checked on the limit process), its closed-form approximation ln{1 + [1 + (c̃ ln 2)2 ]1/2 } (dashed, within 0.03), the ceiling
ln 2 recovered as c̃ → 0 and the cis replacement asymptote ln(c̃ ln 2) (dotted) reached as c̃ → ∞. At R = ∞ and fixed
c > 0, c̃ = ∞: no threshold at any size.

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

Extended Data Fig. 6 | Fusion changes the persistence of dense populations, not invasion. Equilibrium density
of protocells with at least two replicases, in units of 1/k f , against the load U = − ln q, for n = 5, R = 25 and θ = 1
(numerical); k f (κ in the figure) is the fusion rate per pair of protocells and µ the rate of removal per unit density
(SI S5). Solid lines, stable equilibria; dashed lines, unstable equilibria, which reach zero density at Uc , below the
plotted range; dots, folds. Vertical lines: Uc , the invasion threshold of the branching process of the main text (dotted),
and ln 2 (dashed). (A) Fusion between all protocells, a rule blind to content, at k f /µ = 1, 10, 100 and ∞ (blues, light to
dark): the equilibrium vanishes at Uc and there is no bistability. (B) Fusion restricted to protocells that carry replicases,
a rule that sees content, at k f /µ = 30, 100, 300 and 1000 (oranges, light to dark): the branches fold back, so that
between Uc and the fold an established population persists while a rare one cannot invade; the fold lies beyond ln 2
from k f /µ = 100 on. Panels use distinct colour ramps, so that a colour never stands for two values of k f /µ.

27


[page 28]
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
Extended Data Fig. 7 | Thresholds approach one curve in n/R as protocells grow (θ = 1). Gain in tolerable load
over a well-mixed pool, Uc − max(0, ln(1/θ)), which equals Uc at θ = 1, against y = n/R, protocell size (protocells
divide at 2n molecules) over fecundity (copies started per replicase lifetime). Symbols: exact thresholds of the finite
model, n = 25–320 (they overlap for y < 1). Solid line: ψ(y) = − ln λc (y), computed from the limit kernel. For
R > n (y < 1), Uc → max(0, ln(1/θ) + ψ(y)) as n → ∞ at fixed y, for every θ > 0 (Theorem 4; proof in SI S13), and
ψ(y) = ln 2 − 0.350 y + o(y) near y = 0 (Theorem S, SI S14). Blue band: the proved range ln(2/(1 + y)) ≤ ψ(y) < ln 2
for y < 1; dotted blue line: a sharper lower bound for y < 1 (proved; SI S3). Dashed line: numerical large-n limit
for R ≤ n, extrapolated in 1/n from n = 100, 200 and 320; that it equals ψ(y) rests on hypothesis (H2) (SI S3). Grey
line: the ceiling ln 2, proved at every size and fecundity. Hatched: gains excluded at every size when R ≤ n/5 (proved,
computer-assisted; SI S3). Right axis: percentage of the ceiling; the computed limit falls below half of it near y ≈ 3.1
(R ≈ 0.32 n), and ψ is proved to stay above half of the ceiling up to y = 2.858 and below it on [3.2, 5] (computerassisted; SI S3). In the panel, the daggers mark the two bounds of SI S3.

28


[page 29]
662

Supplementary Information

663

Status labels used throughout: proved (a complete argument is given, here or, where so stated, in the notes

664

deposited with the code, S7, the argument being outlined here), proved, computer-assisted (a proof part

665

of which is a computation in interval arithmetic or with a priori rounding-error bounds, deposited with the

666

code, S7), derived (a formal argument, not a proof), numerical (exact kernels, with the stated precision),

667

conjectured.

668

S1. The limit kernel (Theorem 1)

669

Notation. ν = F − 1, P = N − F, growth from n to S = kn molecules, then partition into k daughters, each

670

molecule going to each daughter with probability 1/k. A protocell is alive if F ≥ 2. The kernel of Eq. 1 is

671

p = qν/(ν + θP).

672

Fictitious clock (proved).

673

is copied at rate 1, the copy being a replicase with probability q and a parasite otherwise, and each parasite

674

is copied at rate θ. The next event produces a replicase with probability qν/(ν + θP): the jump chain of this

675

process is exactly the model. Division happens at the stopping time T = inf{t : N(t) = S }. In this clock ν(t)

676

is a Yule process of rate q that does not depend on P.

677

Pairs (proved).

678

1)] = 2q f (ν). Hence E[ν(t)(ν(t) + 1)] = ν0 (ν0 + 1)e2qt , and since ν(ν + 1) = F(F − 1), the number of ordered

679

(catalyst, template) pairs of replicases grows at rate 2q, twice the rate of replicases.

Consider the continuous-time process in which each of the ν replicase templates

The generator of the Yule process applied to f (ν) = ν(ν + 1) gives qν[(ν + 1)(ν + 2) − ν(ν +

681

Partition (proved, every n). Under independent uniform assignment into k daughters, the second factorial
P
moment of the binomial gives E[ d Fd (Fd − 1)] = k F(F − 1)/k2 = F(F − 1)/k. Since F(F − 1) = 0 for

682

F ∈ {0, 1}, the restriction to living daughters is automatic.

683

Limit kernel (proved). At fixed F and n → ∞, P ≃ N is a Yule process of rate θ started from about n

684

molecules, so that T → (ln k)/θ in probability, with a dependence on the path of ν of order ν/n. The limit

685

kernel B∞ is: partition, then a Yule process of rate q for ν during (ln k)/θ. With h = F(F − 1),

680

B∞ h = k2q/θ ·

1
· h = k2q/θ−1 h.
k

686

Numerically, the relation holds to 10−10 for k = 2 (λ = q/θ = 0.3, 0.5, 0.8) and to eight decimals for k = 3

687

(λ = 0.5, 0.7).

688

Identification of the spectral radius (proved).

689

need not give its spectral radius; it does if the h-transformed chain Ph (F, F ′ ) = B∞ (F, F ′ )h(F ′ )/(ρh(F)) is

A positive eigenfunction of an infinite non-negative matrix

691

positive recurrent 42,43 . Write a = kλ , the growth factor of ν over a cycle. The third factorial moment of the
P
Yule process gives E[F ′ h(F ′ ) | Fd ] = Fd (Fd − 1)[(Fd + 1)a3 − a2 ], and the binomial partition E[ d Fd (Fd −

692

1)(Fd + 1)] = F(F − 1)[(F − 2)/k2 + 3/k]; with ρh(F) = (a2 /k)F(F − 1) the drift of Ph is

690

Eh [F ′ | F] = kλ−1 F + (3 − 2/k) kλ − 1,
29


[page 30]
693

that is 2λ−1 F + 2λ+1 − 1 for k = 2 (checked numerically to 3 × 10−14 for k = 2, 3 and 4). For λ < 1, kλ−1 < 1

694

and Eh [F ′ ] − F < −1 for all large F (F > 9.66 at k = 2, λ = 12 ). The chain is irreducible and aperiodic,

695

so Foster’s criterion gives positive recurrence, and k2λ−1 is the spectral radius of B∞ . Truncations of B∞

696

converge to 22λ−1 for λ = 0.3, 0.5, 0.8 and 0.95 (k = 2). For λ > 1 the identification fails, as it must: k2λ−1

697

would exceed k, the largest possible mean number of daughters (at λ = 1.2 and k = 2, truncations give 1.741,

698

not 21.4 = 2.64). The threshold lies at λ = 21 , inside the range of validity: k2q/θ−1 = 1, that is q = θ/2 and

699

Uc = ln(2/θ), for every k; if θ ≥ 2, λ < 12 for every q < 1, so that ρ(B∞ ) < 1 and Uc = 0.

700

Left eigenvector and stable distribution (proved, k = 2).

701

at birth, F ≥ 2, and let p = 2−λ , γ = (1 − p)/p = 2λ − 1. Over a cycle ν = F − 1 becomes negative binomial,

702

E[zν ] = g(z)ν with g(z) = pz/(1 − (1 − p)z), and the two daughters of a protocell born with F replicases have

703

the generating function ΦF (z) = (1 + z) µ(z)F−1 with µ(z) = g((1 + z)/2) = p(1 + z)/(1 + p − (1 − p)z). Then

Index protocells by their number of replicases

′

X

γ F−2 ΦF (z) =

F≥2
′

704

(1 + z) µ
(1 + z)2
=
,
1 − γµ
2(1 − γz)

′

′

whose coefficient of zF for F ′ ≥ 2 is 12 (1 + γ)2 γ F −2 = 22λ−1 γ F −2 : v(F) = γ F−2 is a left eigenvector of the

706

kernel on types at birth, with the eigenvalue 22λ−1 (the coefficients of z0 and z1 are dead daughters). Since
P
h = F(F − 1) is a right eigenvector with the same eigenvalue and F v(F)h(F) = 2/(1 − γ)3 < ∞, the

707

h-transformed chain has a summable invariant measure and is positive recurrent, which gives a second proof

708

of the identification. The stable type distribution is therefore explicit: at birth, F − 2 is geometric with ratio

705

711

γ; at division, the generating function pz2 /(1 − 2(1 − p)z) makes F − 2 geometric with ratio 2 − 21−λ . At
√
threshold (λ = 12 ) a protocell divides with 2 + 2 ≈ 3.41 replicases on average, and with at most ten with
√
probability 1 − (2 − 2)9 = 0.9919. (Checked numerically on truncations to F ≤ 120: vB/v equals 22λ−1 to

712

2 × 10−8 at λ = 0.5 and 0.7.)

713

Self-copying variant (proved for q < θ). If a replicase may choose itself as template, p = qF/(F + θP),

714

a protocell is alive if F ≥ 1, F itself is a Yule process of rate q in the fictitious clock, and h = F satisfies

715

B∞ h = kλ h. The same computation gives Eh [F ′ | F] = kλ−1 F + (2 − 1/k) kλ − 1 (checked to 5 × 10−14 ), so

716

that for λ < 1 the spectral radius is kq/θ > 1 whatever the load: there is no threshold. (For q ≥ θ even the

717

well-mixed pool maintains the replicase.)

718

Why protocells with few replicases carry the threshold (derived). At a macroscopic fraction x = F/N,

719

dx/d ln N = x[(q − θ) − x(1 − θ)]/[θ + x(1 − θ)]. At q = θ/2 this flow is negative on (0, 1] (for θ ≥ 1 because

720

q < 1, for θ < 1 because q < θ). States with x = O(1) are transient: they double at each cycle but drain

721

towards small F in O(log n) cycles and contribute only polynomial factors. The growth rate is that of the

722

quasi-stationary regime F = O(1), x ∼ 3/n. At threshold the mean number of replicases at division is ≈ 3.4

709
710

724

and 99% of protocells have F ≤ 10, for n = 20–200 and θ = 0.5–2, as the exact stable distribution of the
√
limit kernel predicts (2 + 2 and 0.9919, above). The right eigenvector tends to F(F − 1)/2 (within 4% on

725

F ≤ 10 at n = 200; exactly at θ = 1), and a first-order perturbation restricted to small F reproduces Uc (n):

726

1.37227 against 1.37230 (θ = 0.5, n = 200), 0.29255 against 0.29252 (θ = 1.5). The deterministic fixed

727

point x∗ = (q − θ)/(1 − θ) exists only for q > θ, far on the viable side, and plays no role at threshold.

723

30


[page 31]
728
729

S2. Bounds at every size and fecundity (Theorem 2), the limit (Theorem 3) and the spectrum
at θ = 1
At each copy, E[∆(F(F − 1)) | F, N] = 2qF(F − 1)/W, with W = (F − 1) + θ(N − F) =

730

Growth.

731

θ(N − 1) + (1 − θ)(F − 1). For ϕ = F(F − 1)/(N − 1), one copy gives
E[ϕ′ | F, N] = ϕ

N − 1
2q 
1+
.
N
W

732

Upper bound for every θ (proved).

If θ ≤ 1, then W ≥ θ(N − 1), and q ≤ θ/2 gives 2q/W ≤ 1/(N − 1).

733

If θ ≥ 1, then W ≥ (F − 1) + (N − F) = N − 1, and q ≤ 12 gives the same inequality. In both cases, for

734

q ≤ min(θ, 1)/2, E[ϕ′ ] ≤ ϕ: ϕ is a supermartingale during the whole growth phase, which has a fixed number

735

of steps at R = ∞.

736

Partition.

737

1)/[2n(2n − 1)], so that E[ϕ1 | m] = F(F − 1) m/[2n(2n − 1)] for m ≥ 2 (a daughter of size one or zero carries

738

no pair). Summing over the two daughters and over m ∼ Bin(2n, 12 ),

Given the size m of a daughter, F1 is hypergeometric and E[F1 (F1 − 1) | m] = F(F − 1) m(m −

hX i

F(F − 1)
E
ϕd =
2n − 4n 2−2n = (1 − 21−2n ) ϕmother ,
2n(2n − 1)
d
739

the only loss coming from daughters of size one. Combining with growth, the mean matrix K on division

740

states satisfies Kϕ ≤ (1 − 21−2n )ϕ with ϕ > 0 on living states, and the Collatz–Wielandt inequality gives

741

ρ ≤ 1 − 21−2n < 1 for every q ≤ min(θ, 1)/2. Since ρ is continuous in q, it stays below 1 on a neighbourhood

742

of q = min(θ, 1)/2, and the bounds on Uc are strict. Hence, for every n, Uc (n) < ln(2/θ) if θ ≤ 1 and

743

Uc (n) < ln 2 if θ ≥ 1, that is, Uc (n) < max(0, ln(1/θ)) + ln 2: at every size the protocell adds less than ln 2 to

744

the well-mixed threshold, without any assumption on the monotonicity of ρ in q. At θ = 1, W = N − 1 and ϕ

745

is a martingale at q = 21 : ρ( 12 ) = 1 − 21−2n exactly. With a hypergeometric partition (each daughter receives

746

exactly n molecules) there is no loss at division. At θ = 1, ϕ is then a strict supermartingale over a whole

747

cycle for q < 12 and a strict submartingale for q > 21 , so that the Collatz–Wielandt inequality, applied to the

748

finite matrix K in both directions, gives ρ < 1 and ρ > 1 respectively: the threshold is exactly ln 2 for every

749

n ≥ 2.

750

Lower bound for θ ≥ 1 (proved). Now W ≤ θ(N − 1). At q = (θ/2)(1 + η) each copy multiplies E[ϕ]

751

by at least 1 + η/N. The daughter that receives all molecules, with probability 21−2n , divides again at once

752

and gains nothing; it suffices that η > (2n − 1) 21−2n /(1 − 22−2n ) for Kϕ > ϕ on all living states, hence, with

753

Uc = sup{U : ρ(U) > 1}, Uc (n) ≥ ln(2/θ) − O(n4−n ) (the bound is empty when (θ/2)(1 + η) ≥ 1, that is for

754

θ close to 2 at small n). Averaging the gain over the size of the daughters tightens the correction to O(4−n ),

755

consistent with the gap at θ = 1, 21−2n / ln 2 to leading order (Table S1a).

756

Numerical check. On 42 cases (θ = 0.25–1.75, n = 2–40), ρ(q = θ/2) − (1 − 21−2n ) has the predicted sign

757

in every case: −0.067 at θ = 0.5, n = 20; at most 2.3 × 10−15 in absolute value at θ = 1; +0.041 at θ = 1.5,

758

n = 20. For θ > 1 at q = 12 , the certificate maxF (Kh)(F)/h(F) ≤ 1 − 21−2n holds with a strictly positive

759

margin in all 48 cases tested (θ = 1.25–10, n = 2–40; margin 0.0035 at θ = 1.25, n = 2, and 0.32 at θ = 10,

31


[page 32]
760

n = 40), and Uc (n) stays below ln 2 on a grid of 66 points with θ > 1 (θ = 1.1–5, n = 2–50), with a maximum

761

of 0.6464 (θ = 1.1, n = 4).

762

The limit (Theorem 3, proved). Let Kn be the mean matrix on division states F ∈ {2, . . . , 2n} and fix q

763

with θ/2 < q < min(θ, 1), so that λ = q/θ ∈ ( 12 , 1) and β = 22λ−1 > 1. We show that lim inf n ρ(Kn ) ≥ β.

764

(i) One cycle converges. Let the mother have F replicases. A daughter receives Fd ∼ Bin(F, 12 ) replicases

765

and, independently, Pd ∼ Bin(2n − F, 21 ) parasites. On the event Fd ≥ 2, run the fictitious clock from ν(0) =

766

Fd − 1, P(0) = Pd , beyond division if needed: ν is a Yule process of rate q; every parasite is copied at rate

767

θ; every failed copy of a replicase template adds a parasite. The daughter divides at Tn = inf{t : N(t) = 2n},

768

with F ′ = ν(Tn ) + 1. Write P = Pin + Pnew , where Pin counts the Pd initial parasites and their descendants,

769

a Yule process of rate θ, and Pnew the parasites made by failed copies and their descendants. Given Pd = y,

770

Pin (t) is a sum of y independent geometric variables of mean eθt , so Var[Pin (t)e−θt | y] ≤ y; since Pd /n → 1

771

in probability, Pin (t)/n → eθt in probability for every t. Failed copies arrive at rate (1 − q)ν(s) and each

772

founds a Yule family of rate θ, so E[Pnew (t)] ≤ (Fd − 1) t e(q+θ)t , and E[ν(t)] = (Fd − 1)eqt ; neither depends

773

on n. Hence N(t)/n = (ν(t) + 1 + Pin (t) + Pnew (t))/n → eθt in probability for every t. As N is non-decreasing,

774

{Tn < t∗ − δ} ⊂ {N(t∗ − δ) ≥ 2n} and {Tn > t∗ + δ} ⊂ {N(t∗ + δ) < 2n} with t∗ = (ln 2)/θ, and both events have

775

vanishing probability: Tn → t∗ in probability. Then


P ν(Tn ) , ν(t∗ ) ≤ P(|Tn − t∗ | > δ) + P ν jumps in [t∗ − δ, t∗ + δ] ,

776

and the last term is at most 2δq E[ν(t∗ + δ)], which tends to 0 with δ. On this coupling, for all fixed F, F ′ ≥ 2,

Kn (F, F ′ ) − B∞ (F, F ′ ) ≤ 2 P ν(Tn ) , ν(t∗ ) −→ 0,

777

since Kn (F, F ′ ) = 2 P(Fd ≥ 2, ν(Tn )+1 = F ′ ) and B∞ (F, F ′ ) = 2 P(Fd ≥ 2, ν(t∗ )+1 = F ′ ). No independence

778

between Tn and ν is needed.

779

(ii) Truncation. Let A(F0 ) denote the restriction of a matrix A to the states 2 ≤ F ≤ F0 . For a non-

780

negative matrix, the spectral radius of a principal submatrix is at most that of the matrix, so ρ(Kn ) ≥ ρ(Kn(F0 ) );

781

0)
for a finite matrix the spectral radius is continuous in the entries, so by (i) ρ(Kn(F0 ) ) → ρ(B(F
∞ ). Hence

782

0)
lim inf n ρ(Kn ) ≥ ρ(B(F
∞ ) for every F 0 .

783
784
785

(iii) The truncations reach β. All entries of B∞ on living states are positive (a daughter receives two
replicases with positive probability, and a Yule process from ν = 1 reaches every ν ≥ 1). For every

(F0 ) m
0) m
m
) ≥ (B(F
m, ρ(B∞
∞ ) (2, 2), which increases to B∞ (2, 2) as F 0 → ∞ by monotone convergence over

786

0)
m
1/m . On the other hand B h = βh with h > 0 (S1), and the
paths; hence limF0 ρ(B(F
∞
∞ ) ≥ supm B∞ (2, 2)

787

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

788
789

1/m ≥ β. Together, lim ρ(B(F0 ) ) ≥ β.
therefore diverges at z = 1/β, which gives lim supm Bm
F0
∞
∞ (2, 2)

790

(iv) Conclusion. By (ii) and (iii), lim inf n ρ(Kn ) ≥ β > 1, so Uc (n) ≥ − ln q for all n large enough. Letting

791

q ↓ θ/2 gives lim inf n Uc (n) ≥ ln(2/θ) for every θ < 2 (for θ ≥ 2, ln(2/θ) ≤ 0 ≤ Uc (n)). With the upper bound,

792

limn Uc (n) = ln(2/θ) for every θ ≤ 1; for θ > 1 the upper bound is proved below. Numerically, max |Kn − B∞ |

793

on F, F ′ ≤ 12 decreases as 1/n (n max |Kn − B∞ | = 1.06–1.15 for n = 10–400 at θ = 0.5, q = 0.30 and 0.35);

32


[page 33]
794

at θ = 0.5, q = 0.3, the spectral radii of the truncations of B∞ agree with β = 20.2 = 1.148698 to eight digits

795

from F0 = 80 on, and ρ(Kn ) rises from 0.984 (n = 10) to 1.1397 (n = 400); in simulations of the fictitious

796

clock, the mean division time is 1.378 at n = 300 against t∗ = 1.386, with a standard deviation decreasing as

797

n−1/2 .

798

First-order correction (derived). For θ ≤ 2, to first order in 1/n, Uc (n) = ln(2/θ) + ζ(θ)/n with ζ(θ) =

799

2(1 − 1/θ)/ ln 2; for 1 < θ ≤ 2 the expansion is around the limit proved below, and for θ > 2, where the

800

limit is 0, it does not apply. During growth, in the fictitious clock, N − 1 increases at rate θ per parasite but

801
802
803
804

at rate 1 per replicase template, so that a protocell with ν(s) replicase templates reaches 2n molecules later
RT
than T 0 = (ln 2)/θ by about (1 − 1/θ) 0 0 e−θs ν(s) ds/n, during which its pairs grow at rate 2q. Along the
h-transformed chain at threshold, ν + 2 is a Yule process of rate θ/2 and a daughter receives 1 + Bin(ν − 1, 21 )
RT
√
√
templates, so that the stationary mean of ν at birth is (2 2 − 1)/(2 − 2) and θ Eh [ 0 0 e−θs ν(s) ds] = 2

805

exactly; to first order, the Perron root is then 22q/θ−1 [1 + 2(1 − 1/θ)/n]. The other first-order terms (the −1 in

806

N − 1, the size of the daughter, its share of the pairs, the variance of the growth time) add no dependence on θ

807

at threshold to this order: at q = θ/2 each copy multiplies E[ϕ] by exactly 1 − cν/[N(N − 1 + cν)], c = 1/θ − 1

808

(Growth, above), so that ϕ departs from a martingale during growth only through ν, and division costs only

809

the fraction 21−2n . They therefore vanish, since at θ = 1 the identity ρ = 1 − 21−2n leaves no 1/n term.

810

Setting ρ = 1 gives ζ. The expansion is formal, but the exact thresholds confirm it: fitted on n = 400–800

811

and 100–400, ζ = −2.88 and +0.962 at θ = 0.5 and 1.5, against −2.885 and +0.962, and n (Uc − ln(2/θ)) at

812

n = 200 (Table S1b) lies within 0.09 of ζ(θ) for 0.5 ≤ θ ≤ 2, and within 0.02 for 0.75 ≤ θ ≤ 2. The sign of

813

ζ follows: when θ > 1 a protocell rich in replicases grows more slowly, which gives its pairs of replicases

814

more time to multiply before division.

815

Supermartingales at every fecundity (proved). For a > 0 let φa (F) = Γ(F − 1 + a)/Γ(F − 1), the

816

rising factorial (F − 1)F · · · (F + a − 2) for integer a, so that φ2 = h; let gb (N) = Γ(N − 1)/Γ(N − 1 + b),

817

Va,b (F, N) = φa (F) gb (N), with Va,b = 0 on dead states, and Λ = max(q, q/θ). Since W ≥ min(1, θ)(N − 1), a

818

copy is a new replicase with probability p ≤ Λ(F − 1)/(N − 1), and one copy changes Va,b in expectation by
pVa,b (F + 1, N + 1) + (1 − p)Va,b (F, N + 1) − Va,b (F, N) = Va,b

a(N − 1)p/(F − 1) − b
Λa − b
≤ Va,b
,
N−1+b
N−1+b

819

which is not positive for b ≥ Λa. With decay, since φa (F − 1)/φa (F) = (F − 2)/(F − 2 + a) and gb (N −

820

1)/gb (N) = (N − 2 + b)/(N − 2), the two kinds of loss change Va,b at the rate F[Va,b (F − 1, N − 1) − Va,b ] +

821

(N − F)[Va,b (F, N − 1) − Va,b ] = Va,b [N(b − ha ) + ha (2 − b)]/(N − 2) for N ≥ 3, with ha (F) = aF/(F − 2 + a),

822

and −2Va,b at F = N = 2; for a = 2, h2 = 2 and the rate is −(2 − b)V2,b , as for Z in S3. The numerator

823

increases with b; it is not positive if b ≤ 2 ≤ a, since then ha ≥ 2, nor if b ≤ a < 2, since its value at

824

b = a is a(2 − a)(F − N)/(F − 2 + a). Hence, during growth, Va,Λa is a supermartingale at R = ∞ for every

825

a, and at every fecundity if Λ ≤ 1 and Λa ≤ 2; stopped at division or death, which occurs almost surely,

826

gb (2n) E[φa ( f ′ )1{division}] ≤ Va,b of the initial state, where f ′ is the number of replicases at division.

33


[page 34]
827

Partition of rising factorials (proved). For integer a ≥ 2, b > 0 and a mother with f replicases, the first

828

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

829
830
831



α j (n, b) = E r j (N1 ) ,

where (x) j = x(x−1) · · · (x− j+1), N1 ∼ Bin(2n, 21 ), and r j (m) = (m) j gb (m)/[(2n) j gb (2n)] for m ≥ j, r j (m) =
0 otherwise: given N1 = m, F1 is hypergeometric (Partition, above) and E[(F1 ) j | m] = ( f ) j (m) j /(2n) j , and
P 
φa (x) = (x + a − 2)a = j aj (a − 2)a− j (x) j , the terms j = 0, 1 vanishing. α j increases with b; α j ≤ 1 for b ≤ 2,

832

since for j ≥ 2 ≥ b consecutive values of (m) j gb (m) have the ratio (m + 1)(m − 1)/[(m + 1 − j)(m − 1 + b)] ≥ 1,

833

so that r j ≤ 1; and α j (n, b) → 2b− j as n → ∞, since r j (m) ≃ (m/2n) j−b while daughters of fewer than n/2

834

molecules, on which r j is at most polynomial in n, are exponentially rare; in particular α j (n, b) is bounded in

835

n at fixed b. Let cn (Λ) = 2α2 (n, 2Λ): it increases strictly, from cn ( 12 ) = 1 − 21−2n to cn (1) = 2 − 2(2n + 1)4−n ,

836

and at R = ∞ and θ = 1 it is the spectral radius cn (q) (Spectrum at θ = 1, below).

837

A bound at every fecundity (proved). For every n ≥ 2, θ > 0, q ∈ (0, 1] and R ∈ (0, ∞], ρ(Kn ) ≤ cn (Λ).

838

For Λ ≤ 1, the supermartingale V2,2Λ = F(F − 1)Γ(N − 1)/Γ(N − 1 + 2Λ) in each daughter (the daughter that

839

receives all 2n molecules divides at once) and the partition formula with a = 2 give Kn h ≤ cn (Λ)h, and the

840

Collatz–Wielandt inequality gives the bound. For Λ ≥ 1, a daughter divides only if it receives at least two

841

replicases, so the row sums of Kn are at most 2P(Bin( f, 12 ) ≥ 2) ≤ cn (1) ≤ cn (Λ). The bound is attained at

842

θ = 1 and R = ∞ (below). With un the root of cn (e−u ) = 1, so that un = Uc (n, ∞, 1) (Table S1a), it follows

843

that
Uc (n, R, θ) ≤ un + max(0, ln(1/θ)) < ln 2 + max(0, ln(1/θ))

844

at every fecundity: the ceiling of Theorem 2 holds at every fecundity, with the size-dependent value un . At

845

Λ = 12 , V2,1 = ϕ and the bound is that of Theorem 2, ρ ≤ 1 − 21−2n .

846

Division blind to molecular identity (proved). Let the 2n molecules be distributed among any number

847

of daughters, of any sizes, possibly random, by a rule that does not distinguish replicases from parasites:

848

given the sizes, every assignment of the molecules to the daughters is equally likely. Division then does

849
850

not increase the pair density ϕ = F(F − 1)/(N − 1), summed over daughters, in expectation, and conserves
P
P
it exactly when no daughter receives a single molecule: E[ d ϕd ] = ϕ E[ Nd ≥2 Nd ]/N, with ϕd = 0 when

851

Nd ≤ 1. Since ϕ is a supermartingale during growth whenever max(q, q/θ) ≤ 21 , at every fecundity, the

852

spectral radius of the mean matrix K is then at most one, and Uc ≤ ln 2 + max(0, ln(1/θ)) at every size and

853

fecundity. The same bound holds with complementary strands, of which only the plus strand is catalytic

854

(each plus strand starting R copies per lifetime, every strand decaying at rate one), with ϕ computed on all

855

strands of the replicase and U the load per copy. At θ = 1 and infinite fecundity, ϕ is a martingale during

856

growth at q = 12 , a strict submartingale above and a strict supermartingale below, so that Uc = ln 2 exactly

857

at every size for every such rule that never produces a daughter with a single molecule and is not degenerate,

858

that is, gives some daughter between 2 and 2n − 1 molecules with positive probability. Binary binomial

859

partition falls short of ln 2 only through the pair density lost to daughters with a single molecule, which carry

860

on average a fraction 21−2n of the molecules. Within this model, exceeding the ceiling requires a division

861

rule that, for some composition, gives the daughters a larger expected summed pair density than the mother:

862

sorting the replicases into one daughter removes the threshold at infinite fecundity, and placing replicase
34


[page 35]
863

pairs in small daughters also raises it.

864

The lever: how far a division can raise the ceiling (proved).

865
866
867
868
869

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

870

If M(λ) ≤ 1, the Schur reduction of the kernel onto any finite set of types has spectral radius at most

871

one, without any assumption on large types, and the sum of ϕ2 over each generation is a non-negative

872

supermartingale with values in the even integers; it reaches zero almost surely if M(λ) < 1, or if y > 0

873

and, at every type, some daughter with at least two replicases receives less than the whole protocell with

874

positive probability, so that the population then dies out. Therefore λc (y) ≥ λ∗ = sup{λ < 1 : M(λ) ≤ 1} at

875
876

every y, and the compartment constant is at most ln(1/λ∗ ). For two equal daughters, λ∗ = min(1, 12 log2 (1/r̄))
P
with r̄ = sup f E[ d Fd (Fd − 1)]/( f ( f − 1)) ≤ 1, the expected fraction of ordered replicase pairs kept by

877

the two daughters together; random partition gives r̄ = 12 and the ceiling ln 2, and every rule that ignores

878

which molecules are replicases gives λ∗ = 12 . The weight α−2λ
is why a rule that places pairs in small
d

879

daughters can exceed ln 2 without keeping pairs together more often than a random partition into daughters

880

of the same sizes. At finite size and fecundity the same argument, with F(F − 1)Γ(N − 1)/Γ(N − 1 + 2Λ)

881
882

in place of the pair density ϕ (which is its case Λ = 12 ), gives ρ ≤ 1 whenever max(q, q/θ) ≤ Λ ≤ 1 and
P
max f E[ d Fd (Fd − 1) g(Nd )] ≤ f ( f − 1) g(2n), g(N) = Γ(N − 1)/Γ(N − 1 + 2Λ); with λ∗n the largest such

884

Λ, Uc ≤ max(0, ln(1/θ)) + ln(1/λ∗n ) at every size and fecundity. A bound on the factor by which division
P
multiplies E[ d ϕd ] alone gives nothing beyond ln 2 when daughters differ in size: sorting all replicases into a

885

daughter of 9 of 12 molecules multiplies it by at most 1.375, and remains supercritical at every load computed

886

at infinite fecundity (numerical). Partial sorting, which places all replicases in one daughter with probability

887

p and partitions at random otherwise, has r̄ = (1 + p)/2 for every f ; F(F − 1) is then an eigenfunction of

888

the kernel at y = 0 with eigenvalue 4λ r̄, large types drift down near λ∗ because (1 + 3p)2 < 2(1 + p)3 , and

883

890

λc (0) = λ∗ exactly. For y < 1, a lower bound on pair growth in the size clock gives λc (y) ≤ λ∗ + y(1 − λ∗ )
√
for small enough y, so that λ∗ ≤ λc (y) → λ∗ as y → 0: two bits, ln 4, require p = 2 − 1, and three bits

891

p = 23/4 − 1. The exact kernels agree: at θ = 1 and R = ∞, Uc = 1.389378 and 2.082498 at n = 160 for these

892

two values of p, against ln 4 = 1.386294 and ln 8 = 2.079442. The bound is not reached by mechanisms

893

whose gain is confined to protocells with few replicases: in the cases computed at y = 0, bound pairs, clusters

894

and budded vesicles that carry a pair gain only 9–45% of the extra bits that the bound allows, and budded

895

vesicles lose most of that gain already at y = 0.5 (numerical). The complete proofs are in SI S12.1 and in the

896

notes deposited with the code (S7).

897

Spectrum at θ = 1 (proved).

898

2αk (n, kq), k = 2, . . . , 2n; the largest is µ2 = cn (q), and µk → 21−k(1−q) as n → ∞. At θ = 1, p =

889

899
900

At R = ∞ and θ = 1, including q = 1, the eigenvalues of Kn are µk =

q(F − 1)/(N − 1), so that the copy term above vanishes for b = qa: Va,qa is a martingale during growth for
P 
every a, and (Kn φa )( f ) = 2 aj=2 aj (a − 2)a− j α j (n, qa) ( f ) j . The ( f ) j , j = 2, . . . , 2n, form a basis of the

901

functions on {2, . . . , 2n} (a combination of them that vanishes there is a polynomial of degree at most 2n that

902

also vanishes at 0 and 1), and φa is ( f )a plus a combination of the ( f ) j with j < a; Kn is therefore triangular

35


[page 36]
903

in the basis φ2 , . . . , φ2n , with diagonal 2αa (n, qa). As φ2 = h > 0 is an eigenvector, µ2 is the spectral radius,

904

with no assumption of primitivity.

905

The limit for θ > 1 (Theorem 3, proved).

906

ln 2, because W ≤ θ(N − 1) goes the wrong way at q between 21 and θ/2; the upper bound lim supn Uc (n) ≤

907

max(0, ln(2/θ)) follows from (a)–(c), assembled in (d). Convergence of the coefficients alone would not

908

suffice: at q = 1 they converge while ρ(Kn ) = cn (1) stays close to 2.

When θ > 1 the pair density bounds the threshold only by

909

(a) ρ never decreases as q grows (R = ∞, every n). Let T (F, P) be the number of replicases at division

910

of a protocell that grows from F replicases and P parasites, N = F + P ≤ 2n, T N (F) the same from F

911

replicases among N molecules, and ≤st the stochastic order. (i) At fixed N, T N (F) increases with F, whatever

912

the copying probabilities: by backward induction on N, from F the next state is F + 1 or F at size N + 1,

913

both giving T ≤st T N+1 (F + 1), whereas from G > F both give T ≥st T N+1 (G) ≥st T N+1 (F + 1). (ii) Hence,

914

for N < 2n, T (F, P) ≤st T (F + 1, P), since T (F, P) mixes T (F + 1, P) and T (F, P + 1) ≤st T (F + 1, P);

915

T (F, P) ≤st T (F, P − 1), since T (F, P − 1) mixes T (F, P) and T (F + 1, P − 1) ≥st T (F, P); and T increases

916

when replicases are added or parasites removed. (iii) If q ≤ q′ , T at q is ≤st T at q′ , by backward induction,

917

since p increases with q and T (F + 1, P) ≥st T (F, P + 1). (iv) For f ≤ f ′ , couple the two partitions molecule

918

by molecule, the f replicases of the first mother being f of the f ′ of the second and each molecule going to

919

the same daughter: each daughter of the second mother has at least as many replicases and at most as many

920

parasites as the corresponding daughter of the first, and is alive if that one is. Hence, for every non-negative

921

function g that increases on types, Kn (q)g increases and Kn (q)g ≤ Kn (q′ )g; by induction Kn (q)m 1 ≤ Kn (q′ )m 1,

922

and Gelfand’s formula, ρ(K) = limm [max f (K m 1)( f )]1/m , gives ρ(Kn (q)) ≤ ρ(Kn (q′ )). The row sums of Kn

923

do not depend on q at R = ∞, and Kn (q) and Kn (q′ ) are not ordered entry by entry: what is monotone is the

924

type at division.

925
926
927

(b) Drift (R = ∞). Let Λ0 < 1 and a an integer above 1/(1 − Λ0 ). For every β ∈ (21−a(1−Λ0 ) , 1) there are
M, n0 and C such that, for n ≥ n0 and Λ ≤ Λ0 , (Kn φa )( f ) ≤ βφa ( f ) for f > M and (Kn φa+1 )( f ) ≤ Cφa+1 ( f )
P 
for every f . Indeed, by the supermartingale Va,Λa and the partition formula, (Kn φa )( f ) ≤ 2 j aj (a −

928

2)a− j α j (n, Λa)( f ) j ; the term j = a is at most 2αa (n, Λ0 a)φa ( f ), which tends to 21−a(1−Λ0 ) φa ( f ), and the

929

others are O( f j−a )φa ( f ) uniformly in n; the bound for φa+1 follows in the same way. By Fatou’s lemma, the

930

same bounds hold for B∞ .

931

(c) Schur reduction. Let K ≥ 0 be a finite matrix on A ⊔ B with ρ(KBB ) < 1, and S = KAA + KAB (I −

932

KBB )−1 KBA . Then ρ(K) − 1 and ρ(S ) − 1 have the same sign. If K is irreducible, S (t) = tKAA + t2 KAB (I −

933

tKBB )−1 KBA has a spectral radius that increases strictly with t on [0, 1/ρ(KBB )), and ρ(tK) = 1 if and only if

934

ρ(S (t)) = 1, positive eigenvectors corresponding through vB = (I−tKBB )−1 tKBA vA ; since 1/ρ(K) < 1/ρ(KBB ),

935

comparing 1/ρ(K) with 1 gives the claim. Otherwise the claim holds for each strongly connected component

936

C of K that meets A: a path through B between two types of C ∩ A stays in C, so that the restriction of

937

S to C ∩ A is the reduction of KC , and the strongly connected components of S are the non-empty C ∩ A;

938

components inside B have spectral radii at most ρ(KBB ) < 1, and ρ(K) and ρ(S ) are the largest spectral radii

939

of their components.

940

(d) Conclusion. Fix ε > 0 and the single point qε = min(1, θ/2)e−ε , so that − ln qε = max(0, ln(2/θ)) + ε,

941

λε = qε /θ < 12 and c = 22λε −1 < 1, while Λ = max(qε , λε ) < 1. Take a so large that 21−a(1−Λ) < c, then

942

β < c, M and n0 as in (b), with Λ0 = Λ, and let A = {2, . . . , M} and B the larger types. By (b), ρ(Kn,BB ) ≤ β

943

(Collatz–Wielandt with φa ), so that the reductions S n of Kn (qε ) onto A exist. As Kn (qε ) → B∞ entry by

36


[page 37]
944

entry ((i) of The limit, above, which holds for every q) and the weights φa ≤ φa+1 , with φa /φa+1 → 0, bound

945

the tails uniformly in n, S n converges to the reduction S ∞ of B∞ at λε ; its tail constants are explicit: with

946

w = φa , w′ = φa+1 and δL = supg>L w(g)/w′ (g), the paths through B of length k ≥ m contribute at most

947

2Cw′ (i)βm /(1 − β) to S n (i, j), and, for each k, those that leave { f ≤ L} at most 2δL w′ (i)(k + 1)C k+1 . For

948

t = 1/c, the equation x = tB∞,BB x + tB∞,BA hA has a single solution bounded by a multiple of φa , since

949

tB∞,BB φa ≤ tβφa with tβ < 1, and the eigenrelation B∞ h = ch (S1), with h ≤ φa , shows that hB is that

950

solution; hence S ∞ (t)hA = hA for S ∞ (t) = tB∞,AA + tB∞,AB (I − tB∞,BB )−1 tB∞,BA , and ρ(S ∞ (t)) = 1. As t > 1,

951

S ∞ ≤ S ∞ (t)/t entry by entry, hence ρ(S ∞ ) ≤ c < 1. Therefore ρ(S n ) < 1 for n large, ρ(Kn (qε )) < 1 by (c),

952

and ρ(Kn (q)) < 1 for every q ≤ qε by (a): Uc (n) ≤ max(0, ln(2/θ)) + ε for n large. With the lower bound (iv),

953

limn Uc (n) = max(0, ln(2/θ)). The same argument gives the limit for θ ≤ 1 without Theorem 2. Numerically,

954

at θ = 2 and ε = 0.03, ρn (qε ) = 1.000194 at n = 50 and 0.98261 at n = 320, and for θ ≥ 2 the thresholds

955

decrease as about 1/n (Table S1c).

956

S3. Finite fecundity

957

Exact identity at θ = 1 (proved). Let g(N) = Γ(N − 1)/Γ(N − 1 + 2q) and Z = F(F − 1) g(N), so that

958

g(N + 1)/g(N) = (N − 1)/(N − 1 + 2q). At θ = 1, W = N − 1. Copies occur at rate RF and give a replicase

959

with probability q(F − 1)/(N − 1); their contribution to the generator is
RF

960

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

961

using (N − 2)g(N − 1) = (N − 2 + 2q)g(N), valid for N ≥ 3. Hence E[dZ | F, N] = −2(1 − q)Z dt for every

962

state with N ≥ 3, whatever R: between divisions the pair density decays at rate 2(1 − q) per lifetime. At

963

N = 2 the decay is faster (inequality). The identity was checked on 2 × 104 random states (relative error

964

below 3.5 × 10−8 ) and in exact rational arithmetic; it is false for θ , 1, as expected. At R = ∞ the copying

965

terms alone act, so Z is a martingale during growth and a division multiplies E[Z] by the R = ∞ spectral

966

radius cn (q); at q = 21 , Z = ϕ and cn ( 12 ) = 1 − 21−2n .

967

Replacement (proved). Maintenance requires R > eU in protocells of any size. New replicases appear at

968

rate RF p(F, N) ≤ RFq, since p ≤ q, and replicases decay at rate F; division conserves the total number of

969

replicases. The expected total number of replicases in the population therefore decays at least as e−(1−Rq)t

970

when Rq < 1.

971

Well-mixed limit at fixed R (derived in mean field). At a macroscopic replicase fraction x, ẋ = Rx2 (q −

972

ω)/ω with ω = x + θ(1 − x), and d ln N/dt = Rx − 1. For θ < 1, x converges to x∗ = (q − θ)/(1 − θ) and the

973

lineage grows at rate Rx∗ − 1, whence the threshold x∗ = 1/R, that is Eq. 2. Protocells with F = O(1) do

974

not escape it, heuristically: at fixed F, N saturates at RF and the resulting growth condition is the same. For

976

θ ≥ 1, x → 0 and Uc → 0. The convergence of the stochastic process to this mean-field limit is not proved;
√
numerically it is slow, the gap decreasing as ≈ 1.2/ n at θ = 0.5, R = 10 (0.823, 0.764, 0.721, 0.685, 0.657

977

at n = 20, 50, 100, 200, 400, against 0.598); at θ = 1.5, R = 10, nUc ≈ 2.

975

37


[page 38]
With F = O(1) and N

978

Limit process (derived; the finite kernels are proved to converge to its kernel).

979

of order R, set u = N/R. Then W = θN(1 + O(1/N)), parasites follow their mean to relative order N −1/2 ,

980

and the birth size is n(1 + O(n−1/2 )). In the limit n, R → ∞ at fixed y = n/R: u̇ = F − u; F → F + 1

981

at rate λF(F − 1)/u with λ = q/θ; F → F − 1 at rate F; division when u = 2y, each daughter receiving

982

Fd ∼ Bin(F, 21 ) and ud = y. The finite kernels converge to the kernel of this process on every compact range

983

of λ with max(q, q/θ) ≤ 1 (proved below); the convergence of the thresholds is proved for y < 1 and rests,

984

for y ≥ 1, on hypothesis (H2), without which only the limit points of the thresholds are bracketed (status

985

below).

986

Pair density in the limit process (proved). For Z = F(F − 1)u−2λ , the flow contributes −2λF(F −

987

1)u−2λ−1 (F − u), births +2λF 2 (F − 1)u−2λ−1 and deaths −2F(F − 1)u−2λ ; the sum is −2(1 − λ)Z. A division

989

multiplies E[Z] by 21 22λ = 22λ−1 . At threshold, provided the Z-moments are finite, (22λ−1 − 1) κ = 2(1 − λ),
R
with κ = Ev [Zdiv ]/Ev [ Z dt] the Z-weighted division rate and v the Perron vector of birth types. This is an

990

exact rewriting at threshold, not a closed form. In the simulated limit process at y = 1 the two sides are

991

0.7706 and 0.7700; κ = 16.6 at y = 0.25 and 4.46 at y = 1.

992

Direct simulation of the limit process. Jumps were sampled exactly along the deterministic flow, without

993

population control, giving ψ(0.25) = 0.6176 ± 0.0008, ψ(1) = 0.4862 ± 0.0006 and ψ(4) = 0.3169 ± 0.0004,

994

within 0.8 standard errors of the values extrapolated from the exact kernels at θ = 1 (Table S3).

995

Properties of ψ. An independent analysis of the limit process, with its own codes, gives four results. (i)

996

ψ(y) ≤ ln 2 for every y, strictly for y > 0 (proved; strictness below): Z e2(1−λ)t is a martingale between

997

divisions, so E[Z] cannot grow over a growth phase, and a division multiplies it by 22λ−1 ; F(F − 1) is

988

999

then sub-invariant for the kernel on types at birth with the factor 22λ−1 , which is at most 1 for λ ≤ 21 . (ii)
√
ψ(y) = ln 2−a y+o(y) with a = (3 2−4)/ ln 2 = 0.35006 (proved: Theorem S, S14; first derived by first-order

1000

perturbation of the y = 0 kernel, using the stable distribution of S1; numerically confirmed to nine digits); the

1001

remainder is also proved to be O(y2 ), with constants about 109 times too large. With Theorem 4, for θ ≤ 1 the

1002

limit of Uc (n, n/y, θ) is ln(2/θ)−a y+O(y2 ); near the ceiling, with ε = ln(2/θ)−U → 0, lim supn→∞ Rmin /n ≤

1003

(a + o(1))/ε (proved, on this side only and asymptotically); at fixed ε only lim supn→∞ Rmin /n ≤ 1/(eε − 1) is

1004

proved, and Rmin ≈ a n/ε remains derived. (iii) A deterministic solver of the limit process (linear differential

1005

equations along the flow, Chebyshev collocation) reproduces the values extrapolated from the exact kernels

1006

to 10−8 for y ≤ 0.5 and to 7 × 10−5 on [1, 16] (numerical); it gives Rmin /n = 0.216, 1.126 and 3.10 for

1007

U + ln θ = 0.3, 0.5 and 0.6. (iv) ψ is not a power law: the local exponent −d ln ψ/d ln y peaks at 0.43 near

1008

y = 25 and falls to 0.17 near y = 220, so that the fit of the main text underestimates ψ by 13% at y = 128; on

1009

[96, 256], 1 − λc (y) ≈ 0.40/ ln y (conjectured, short range). No closed form for y > 0 was found.

1010

Status of Theorem 4 (proved for y < 1; for y ≥ 1, under one unproved hypothesis, without which

1011

the limit points are bracketed). Let λc (y) = inf{λ < 1 : ρ(S ∞ (y, λ)) > 1}, where S ∞ (y, λ) is the Schur

1012

reduction, onto the types f ≤ M, of the kernel of the limit process (its mean matrix of daughters, by number

1013

of replicases at division), for any cut M beyond which large replicase numbers drift down under the limit

1014

kernel (such cuts exist for every λ < 1; below); the sign of ρ(S ∞ ) − 1 does not depend on such M (proved,

1015

by the quotient property of Schur reductions). The argument of S2 for θ > 1, with the bound at every

1016

fecundity for small λ, then gives Uc (n, n/y, θ) → max(0, ln(1/θ) − ln λc (y)), provided (H2) the reduced kernel

998

38


[page 39]
1017

is subcritical for every λ < λc (y); for θ < 1 the argument also uses (H3) λc (y) < 1, which is proved below. It

1018

rests on the convergence of the finite kernels to the kernel of the limit process and on a uniform drift of large

1019

replicase numbers, both proved for every y (below). (H2) is proved for y < 1 (below), so that Theorem 4

1020

holds there. For y ≥ 1, (H2) is supported numerically on a truncation in F of the limit process: its spectral

1021

radius increases strictly with λ and crosses 1 once, for y from 1 to 16, where λc (y) ≤ 0.834; without it,

1022

the limit points of the thresholds are bracketed (below). That this λc (y) is the threshold from which ψ is

1023

computed is established numerically, by the agreement of a deterministic solver of the limit process with the

1024

extrapolated exact thresholds, to 10−8 for y ≤ 0.5 and 7 × 10−5 on [1, 16] (Properties of ψ, (iii)), and is not

1025

proved; so is the decrease of ψ, certified only on a grid of step 0.05 for y < 1 (Certified bounds on ψ, below).

1026

At infinite fecundity the limit is Theorem 3. The arguments below are outlined; they are written out in full,

1027

each checked by an independent session, in the notes deposited with the code (S7).

1028

The scaling limit for R > n (proved). Let y = n/R < 1. The proof has three parts. (i) Uniform drift of

1029

large types. For any Λ0 < 1 and any integer a > 1/(1 − Λ0 ), the finite kernels satisfy Kn φa ≤ βφa beyond

1030

some type M, with β < 1, uniformly in large n and in all (q, θ) with max(q, q/θ) ≤ Λ0 , for every y > 0.

1031

The weight φa can grow only when few replicases remain; there it is controlled by the density of replicase

1032

pairs, whose expectation decays at least at rate 2(1 − Λ) during the cycle, and the same quantity bounds the

1033

tail of the cycle duration; cycles in which the protocell becomes small are controlled by comparison with an

1034

M/M/∞ queue. (ii) Convergence to the limit process (below, for every y; for y < 1 it also follows, with a

1035

rate, from the probability of dividing with a given number of replicases, a smooth function of the reduced

1036

size because u is then a clock, which the finite process and the limit process reach at the same reduced size

1037

2y). (iii) From kernels to thresholds. The Schur reduction on types ≤ M converges, with the tail bounds of

1038

S2 (d), and is continuous in λ. With (H2) for y < 1 and the bound on pair density, which gives (H3) and

1039

ψ ≥ ln(2/(1 + y)) (below), this proves the statement; a deficit of pair density in every type gives ψ < ln 2.

1040

The complete proof is given in S13.

1041

(H2) for y < 1: the size clock (proved).

1042

2y ≥ u, so the reduced size u increases throughout the cycle and can serve as its clock. In this clock every

1043

surviving lineage divides at the same time u = 2y, and the number of replicases is a birth–death chain; two

1044

such chains can be coupled so that they never cross. The limit kernel therefore maps increasing functions

1045

of the type to increasing functions, and increases with λ on them, strictly through survival. It follows that if

1046

ρ(S ∞ ) ≥ 1 at some λ0 , then ρ(S ∞ ) > 1 for every λ ∈ (λ0 , 1): ρ(S ∞ ) equals one at one λ at most, which gives

1047

(H2). In the same clock, the expected number of ordered replicase pairs, summed over both daughters, is at

1048

least 22ky −1 times that of the mother, ky = (λ − y)/(1 − y), so that λc (y) ≤ (1 + y)/2 and ψ(y) ≥ ln(2/(1 + y)).

1049

For every y > 0, this number falls short of its infinite-fecundity factor 22λ−1 by a positive amount in every

1050

type, so that λc (y) > 12 and ψ(y) < ln 2.

1051

The reduced kernel is supercritical near λ = 1 (proved).

1052
1053
1054

Let y < 1. Along a living lineage of the limit process, F ≥ 2 >

Fix y > 0 and λ < 1. For an integer a > 1/(1−λ)

and a suitable C, V = φa (F)u−λa + C F(F − 1)u−2λ is a supermartingale of the limit process, so that large
replicase numbers drift down, by a factor tending to 21−a(1−λ) , and λc (y) is defined from the limit kernel alone.
Rτ
By the pair density, E[Zdiv ] = Z0 − 2(1 − λ) E 0 Z dt over a cycle. For ϖ > 0 and α = y(ϖ + 2)3 /(2ϖ2 ),

1055

the function L = ϖ ln(2y/u) + αu/F satisfies G(LZ) ≤ −Z when 1 − λ ≤ 1/α, which bounds the Z-weighted

1056

duration of a cycle by T = ϖ ln 2 + αy/2 times Z0 . Hence Kφ2 ≥ 22λ−1 [1 − 2(1 − λ)T ] φ2 ; with the drift above,
39


[page 40]
1057

φ2 is then a strict subsolution of the reduced kernel, which is supercritical for λ close to 1: λc (y) < 1 at every

1058

y > 0, which is (H3). For y < 1 a cycle lasts at most ty = ln[(2−y)/(2−2y)], whence λc (y) ≤ 12 +ty /(2(ln 2+ty )):

1059

at y = 0.25, λc ≤ 0.591, against the computed 0.539. With this bound, ψ(y) > 12 ln 2 for y < 0.558, hence

1060

for R > 1.8 n (for every y < 1 with the certified bound λc ≤ 0.65, below); the computed ψ falls below 21 ln 2

1061

beyond y ≈ 3.1, and is proved to lie below it on [3.2, 5] (Certified bounds on ψ, (iv)). For y ≥ 1 the bound is

1062

crude (λc (1) ≤ 0.957) and only settles (H3).

1063

Convergence to the limit kernel (proved). Fix y > 0, θ > 0 and a compact interval of λ on which

1064

max(q, q/θ) ≤ 1, with q = θλ. Then Kn ( f, f ′ ) → K∞ (y, λ)( f, f ′ ) for all types, uniformly in λ, and the limit

1065

depends on q and θ only through λ. For y < 1 this also follows, with a rate, from a smooth test function.

1066

The chain within a protocell and the limit process are coupled through common Poisson clocks: replicase

1067

deaths occur at the same times, and while F is bounded the birth rates differ by O(|N/R − u| + 1/R). Three

1068

estimates close the argument. (F − 1)Γ(N − 1)/Γ(N − 1 + Λ) is a supermartingale, so that F stays bounded

1069

with high probability, uniformly in n. Over bounded times, N/R follows the flow u̇ = F − u, driven by the

1070

chain’s own F, to O(|N0 /R − y| + R−1/2 ) in mean, by Doob’s inequality. And before its last change of F, a

1071

cycle of the limit process comes within ε of the division size only with a probability that vanishes with ε; the

1072

two processes then divide within O(ε) of each other, with the same type. A geometric bound on the duration

1073

of a cycle, uniform in n, and the equicontinuity in λ of both kernels give the uniformity. Types f ′ ≤ 2y, never

1074

produced by the limit process, keep a mass that vanishes as n → ∞.

1075

Without hypothesis (H2) (proved, every y > 0). Let λ−c (y) = inf{0 < λ < 1 : ρ(S ∞ (y, λ)) ≥ 1}

1076

(and 1 if this set is empty), so that λ−c (y) ≤ λc (y), and ψ− = − ln λ−c . Then max(0, ln(1/θ) + ψ(y)) ≤

1077

lim inf n Uc (n, n/y, θ) ≤ lim supn Uc (n, n/y, θ) ≤ max(0, ln(1/θ) + ψ− (y)), with 0 < ψ ≤ ψ− < ln 2. The

1078

proof is that of the theorem for R > n with the convergence above: the lower bound uses only points of the

1079

set that defines λc , the upper bound only λ < λ−c . Hypothesis (H2) is exactly ψ− = ψ; it is proved for y < 1

1080

and supported numerically for y ≥ 1, where it could fail only through a tangency (Certified bounds on ψ,

1081

(v)).

1082

Certified bounds on ψ (certificates proved, computer-assisted; consequences for the finite model proved

1083

at each fixed n/R that a certificate covers, the limit law for Rmin derived; monotonicity in R numerical).

1084

An independent session bounded the spectral radius of the limit kernel rigorously from below and from above

1085

(comparison generators, directed rounding, interval exponentials and, for large types, a supermartingale;

1086

for y > 1, the trajectories that enter {F ≤ u} are killed, which can only lower the kernel). (i) At the 19

1087

points y = k/20, k = 1, . . . , 19, the enclosures of λc (y), of width at most 0.0056, are disjoint and ordered,

1088

λc (0.05) < λc (0.10) < · · · < λc (0.95), so that ψ decreases along this grid; between grid points its decrease,

1089

and hence the uniqueness of the root of ψ(y) = U, is only numerical. (ii) ψ > 0.6 on (0, 1309/4096]

1090

and ψ(363/1024) < 0.6; ψ > 0.5 on (0, 1807/2048] and ψ(953/1024) < 0.5 (for small y, by an analytic

1091

bound). Let Rmin (n, U) = inf{R0 : Uc (n, R, 1) > U for all R ≥ R0 }; it is at least the Rmin of Corollary 9.2

1092

(S14), which asks Uc > U at a single R, so that the upper bounds below hold for both definitions and

1093

the lower bounds for this one only. Theorem 4 at the single point y1 = 363/1024 or 953/1024 gives, at

1094

θ = 1, lim inf n Rmin /n ≥ 1024/363 > 2.8209 for U = 0.6 and ≥ 1024/953 > 1.0745 for U = 0.5; and,

1095

without assuming that Uc increases with R, Rmin (n, 0.6) ≤ 4096n/1309 for n ≥ 8.8 × 109 and Rmin (n, 0.5) ≤

1096

2048n/1807 for n ≥ 8.3 × 1012 , so that lim supn Rmin /n ≤ 4096/1309 < 3.1292 and ≤ 2048/1807 <
40


[page 41]
1097

1.1334 (Proposition T, proved, computer-assisted: the finite-size pair-density bound for small n/R (The price,

1098

bounded at every size, below), then 57 and 157 certified lower bounds on the limit kernel over adjacent boxes

1099

in y, carried to the finite kernels by an explicit bound on their convergence for y < 1; the same bounds hold

1100

uniformly in θ ∈ [1/2, 1] for U + ln θ = 0.6 and 0.5, with Uc (n, R, θ) in place of Uc (n, R, 1) and from

1101

n ≥ 9.3 × 109 and 8.3 × 1012 ; exact kernels at y = a, extrapolated in 1/n, suggest that the inequality

1102

holds from n ≈ 54 and 188). As a consequence (derived), Rmin (n, U)/n → 1/y∗ (U), with y∗ (U) the first

1103

point where ψ falls below U, for all but countably many U ∈ (inf 0<y<1 ψ(y), ln 2), for which y∗ (U) < 1;

1104

this needs no monotonicity in R, and that of ψ serves only to identify y∗ (U) with ψ−1 (U). These brackets

1105

contain the values 3.10 and 1.126 given by the deterministic solver (Properties of ψ, item (iii), above). (iii)

1106

λc (y) ≤ 0.65 for 0 < y < 1; for y ∈ [1, 2.649] the principal block of the limit kernel at λ = 0.7 on the

1107

types 2, . . . , 50 has spectral radius above 1 (at least 1.057 on [1, 2]), and so has that at λ = 0.707 < 2−1/2

1108

for y ∈ [2.5, 2.858]; hence ψ > 12 ln 2 on (0, 2.858]. The convergence of the finite kernels (above), at fixed

1109

λ and for the 492 entries of that block, then gives lim inf n Uc (n, n/y, θ) ≥ ln(1/θ) + ln(1/0.707) for θ ≤ 1

1110

and every fixed y ∈ [1, 2.858] (proved, computer-assisted, through that convergence); for y < 1, where

1111

a block is certified only at λ = 13/20 and only on [76/256, 1], the same bound follows from Theorem 4

1112

and λc ≤ 0.65, which give limn Uc (n, n/y, θ) ≥ ln(1/θ) + ln(20/13) with ln(20/13) = 0.4308 > 12 ln 2

1113

(proved, computer-assisted; the certificate for λc ≤ 0.65 was also redone from scratch by a second session).

1114

Hence, at every fixed ratio R ≥ 0.35 n (n/R ≤ 2.858), large protocells keep more than half of the bonus.

1115

(iv) For every y ∈ [16/5, 5] and every λ ∈ (0, 442/625], ρ(S ∞ (y, λ)) ≤ 1 − 10−4 , with types counted at

1116

birth or at division, so that λ−c (y) ≥ 442/625 = 0.7072 > 2−1/2 and, by the bracket without (H2) above,

1117

lim supn Uc (n, n/y, θ) ≤ ln(1/θ) + ln(625/442) < ln(1/θ) + 12 ln 2 for θ ≤ 1 and every fixed y ∈ [3.2, 5]. The

1118

certificate is one supermartingale per box of y (19 boxes), of the form (u/y)−97/20 PF (u/y) with a polynomial

1119

PF for each F ≤ 48 and PF ∝ F(F−1) · · · (F−5) beyond, verified in exact rational arithmetic; at fixed (F, u/y)

1120

its drift is bilinear in (λ, 1/y), and the range of u/y only shrinks as y decreases, so the four corners of each box

1121

cover every λ ≤ 442/625 at once, without (H2). With the bound for R ≤ n/5 (below), large protocells thus

1122

keep less than half of the bonus at every fixed ratio R ≤ n/3.2; the computed frontier, y ≈ 3.1, lies between

1123

2.858 and 3.2. (v) For y ≥ 1 the limit kernel is also bounded from above. On a grid in s = u/y, a function

1124

affine in s between nodes is checked in interval arithmetic with directed rounding to be a supersolution of

1125

the backward equation of the limit process on every cell and for every (y, λ) of a box, with a supermartingale

1126

for large replicase numbers; a Collatz–Wielandt test then gives ρ(S ∞ (y, λ)) < 1 for every λ ∈ [1/2, λlow (y)]

1127

and every y ∈ [1, 3] (64 boxes of width 1/32; also 57 of the 64 boxes of [3, 5]), with λlow (y) 0.004 to 0.009

1128

below the computed λc (y); for λ < 1/2 the same holds by Properties of ψ, (i). With lower bounds of the

1129

type of (iii) near threshold, λc (y) ≤ λup (y), this brackets the limit points of the thresholds without (H2),

1130

max(0, ln(1/θ) + ln(1/λup )) ≤ lim inf n Uc (n, n/y, θ) ≤ lim supn Uc (n, n/y, θ) ≤ max(0, ln(1/θ) + ln(1/λlow )),

1131

an interval of width at most 0.033 on [1, 3] (for example [0.384, 0.408] at y = 2 and θ = 1), and gives

1132

lim inf n Rmin /n ≥ 32/69 > 0.4637 for U = 0.4 and ≥ 32/95 > 0.3368 for U = 0.36 (θ = 1). (H2) itself

1133

remains unproved for y ≥ 1: it could fail only through a tangency of the spectral radius to 1 from below, at

1134

some λ between λlow (y) and λc (y), in a band of width at most 0.022 on [1, 3], which these bounds cannot

1135

exclude; numerically, at the 17 values of y tested, the logarithm of the spectral radius is concave on a grid

1136

of step 0.05 in λ, too coarse to resolve the band; concavity there would exclude a tangency. These results

1137

hold at each fixed y, not uniformly; between y = 2.858 and 3.2 nothing is proved about half of the bonus.

1138

An independent code reproduced all 38 bounds of (i), the two bounds at y1 and 34 of the 209 boxes of (ii),

41


[page 42]
1139

including the eight of smallest margin, and 36 boxes of (iii), including the least favourable of each interval; an

1140

independent exact code (Sturm sequences in integers) re-verified the 19 boxes of (iv), exact integer arithmetic

1141

re-certified the 121 boxes of (v), the 113 slices of its lower bounds were reconfirmed from their raw results,

1142

and an independent reading found no error in the proof of Proposition T. Numerically, the spectral radius

1143

of the exact kernel increases with R at every sampled value: its derivative, computed by complex steps, is

1144

positive at all 39,376 sampled points where |∂ ln ρ/∂ ln R| > 10−10 , out of 39,432 (a full grid for n = 3 to 20,

1145

a sub-grid for n = 25 to 100), the other 56 lying in saturation (2 − ρ < 10−6 ); this supports, but does not

1146

prove, that Uc increases with R and that Rmin is well defined.

1147

The price, bounded at every size (proved).

1148

size. Its generator during growth is ϕ [RF(2(N − 1)p/(F − 1) − 1)/N − 1] when N ≥ 3, and ϕ [R(2q −

1149

1) − 2] at F = N = 2; at θ = 1, copying contributes RF(2q − 1)/N and losses remove one. Hence Uc ≤

1150

max{0, ln(2R/(R + 1)) + max(0, ln(1/θ))} for every division rule that does not distinguish replicases from

1151

parasites; and, for θ ≤ 1, n ≥ 3 and every such rule that is not degenerate and never produces a daughter

1152

with a single molecule, Uc ≥ ln(2R/(R + n − 1/2)). For θ ≥ 1 and U < ln 2, a fecundity R > eU /(2 − eU )

1153

is thus necessary at every size, which sharpens Replacement (R > eU ); for θ ≤ 1, n ≥ 3 and such rules,

1154

R > (n − 1/2)eU /(2 − eU ) is sufficient. Binary binomial partition produces daughters with a single molecule,

1155

and at θ = 1 the finite-size lower bound fails for large R, since Uc ≤ un < ln 2 there; what is proved for it is a

1156

finite-size form of the limit bound lim inf n→∞ Uc (n, n/y, θ) ≥ ln(2/(1 + y)): for θ ≤ 1, every n ≥ 10 and every

1157

R > 0, Uc (n, R, θ) > ln(2/(1 + n/R)) − 3/((n − 1) ln 2) (proved). With y = n/R < q < 1 and b = 2(q − y)/(1 − y),

1158

the pair density F(F − 1)Γ(N − 1)/Γ(N − 1 + b), set to 0 when the lineage dies, is a submartingale of the finite

1159
1160

The same pair density bounds the fecundity needed at every

chain during growth whenever R(2q − b) ≥ 1 + b; the binomial split, the convexity of the Γ-ratio in N and
Q
Jensen’s inequality then give ρ(K) ≥ 12 2n−2
j=n (1 + b/ j). At θ = 1 the price is therefore at most linear in size,

1161

at every size for such rules and, up to 3/((n − 1) ln 2), for binomial partition, and Theorem 4 gives its exact

1162

asymptotic form for R > n.

1163

A bound when R ≤ n/5 (proved, computer-assisted).

1164

y ≥ 5, with λ0 = 725/1024, 91/128, 373/512, 755/1024 and 759/1024 from y = 5, 5.5, 8, 12 and 16 on,

1165

so that Ψ = 0.345300, 0.341171, 0.316746, 0.304754 and 0.299470. Then Uc (n, R, θ) ≤ max(0, ln(1/θ)) +

1166

Ψ(n/R) for every n ≥ 2, R > 0 and θ > 0. Since ln(1024/725) < 12 ln 2 = 0.346574, a replicase that makes,

1167

on average, at most n/5 complete copies in its lifetime keeps less than half of the bonus at every size; more

1168

generally, a replicase maintained at a load U with U − max(0, ln(1/θ)) ≥ Ψ(y0 ) has R > n/y0 . The proof

1169

has five parts. (i) In every state p ≤ Λ(F − 1)/(N − 1), with Λ = max(q, q/θ), and Λ ≤ λ0 as soon as

1170

U ≥ max(0, ln(1/θ)) + ln(1/λ0 ); the generator is then dominated, on functions that increase with F, by that

1171

of a single chain with θ = 1 and q = λ0 . (ii) A positive function V of the state of that chain, increasing in

1172

F, whose drift is non-positive between divisions and whose expectation does not increase at division, gives

1173

ρ ≤ 1, by optional stopping (Dynkin’s formula) and the Collatz–Wielandt inequality. (iii) For R ≤ 1/λ0 ,

1174

V = F suffices. (iv) Otherwise V is the sum of the pair density F(F − 1)Γ(N − 1)/Γ(N − 1 + 2λ0 ) and of three

1175

further terms, F(F − 1), F(F − 1)Γ(N − 1)/Γ(N − 1 + 4λ0 ) and one of fourth degree in F, with coefficients

1176

that depend on n and y. (v) Its two inequalities are verified in interval arithmetic (IEEE-754 double-precision

1177

operations, assumed correctly rounded and widened outward by one unit in the last place, with constants

1178

enclosed by mpmath) and, for the division step up to n = 3000, in double precision with a priori bounds on

42

Let Ψ(y) = ln 2 for y < 5, and Ψ(y) = ln(1/λ0 ) for


[page 43]
1179

rounding errors, on a finite set of states and sizes and proved analytically beyond it, a monotonicity lemma

1180

in n passing from base sizes to all sizes. An independent check, with a second implementation (free of

1181

binary64 arithmetic only for the bound from y = 5) and an adversarial search over 1,554 cases with n ≤ 60,

1182

found no gap. A second check, with our own code, recomputed both inequalities in exact rational arithmetic

1183

in every state at 21 pairs (n, R), the division step exactly at six sizes up to n = 3001, the part for states of

1184

100 molecules or more in interval arithmetic, and 768 spectral radii just above the bound, all at most 0.80,

1185

without violation; it spot-checked, without redoing them in full, the computed parts that the first check had

1186

redone. For R < 512/213 ≈ 2.40, hence at every R ≤ n/5 when n ≤ 12, the bound ln(2R/(R + 1)) above is

1187

the better one. In the limit n → ∞ and for θ ≤ 1 the constant 5 is now 3.2 (Certified bounds on ψ, (iv)); at

1188

finite size it remains 5, the computed frontier being y ≈ 3.1, and a certificate of this four-term form cannot go

1189

below ln(4/3) = 0.2877. That the bonus vanishes when R ≪ n is proved at every size, but only far out: for

1190

every n ≥ 2 and θ > 0, Uc (n, R, θ) − max(0, ln(1/θ)) ≤ 4 ln ln(n/R)/ ln(n/R) whenever n/R ≥ 1029 (proved,

1191

computer-assisted: a certificate of the same kind with a free degree a ≥ 8, the explicit rate using interval

1192

arithmetic for 8 ≤ a ≤ 100; checked by an independent session), a decay so slow that the certificate improves

1193

on the bounds above only from n/R ≈ 3.4 × 1025 on, with a = 8.

1194

The price is necessary at every size (Theorem Q; proved; the proof, written out in full and checked by

1195

an independent session, is in a deposited note, S7). Let κQ = 1.98053 × 10−7 , the constant obtained with

1196

δ0 = 0.005 and a cut at M = 9, which satisfies the condition κQ ≤ δ0 that the proof requires, and let δ(y0 ) =

1197

κQ y0 /(y0 +2). For every y0 > 0, n ≥ 25, R ≤ n/y0 and θ > 0, Uc (n, R, θ) < max(0, ln(1/θ))+ln 2−ln(1+2δ(y0 )).

1198

Hence, for θ ≤ 1 and 0 < ε ≤ κQ /3, coming within ε of the ceiling requires R > (κQ /3) n/ε at every size

1199

n ≥ 25, including R ≤ n. With Theorem 4 and ψ(y) ≥ ln(2/(1 + y)), the threshold at R = n/ε comes within

1200

ε of the ceiling for n ≥ n1 (ε, θ), so that, for θ ≤ 1, each fixed ε ≤ κQ /3 and large n, the infimum Rmin of the

1201

fecundities that come within ε of the ceiling satisfies (κQ /3) n/ε ≤ Rmin ≤ n/ε: it is Θ(n/ε), with constants

1202

independent of ε, but n1 (ε, θ) is not explicit and may grow as ε → 0. The constant is poor: the computed gap

1203

is about 0.35 y. The proof uses the results of SI S2 listed in S13, Section S13.2.

1204

A caution on simulated thresholds. A simulation of the same model with a finite population of 200

1205

protocells underestimates Uc : on 54 points the mean bias is −0.014, −0.022 and −0.027 for θ = 0.5, 1 and

1206

1.5, and −0.048 at worst. With 800 protocells the bias disappears or is divided by three. All thresholds

1207

reported here come from exact kernels.

1208

S4. Tables of thresholds

1209

Tables S1–S3 give the thresholds quoted in the main text: at infinite fecundity (Table S1), at finite fecundity

1210

(Table S2) and in the scaling limit (Table S3).

43


[page 44]
Supplementary Table S1 | Thresholds at infinite fecundity. (a) Control at θ = 1 by two independent codes; the gap to
ln 2 follows 21−2n / ln 2 from n = 4. (b) Approach to ln(2/θ): Uc at n = 200, extrapolation a0 + a1 /n + a2 /n2 on n = 100,
150, 200, and n (Uc − ln(2/θ)) at n = 200 (for θ ≥ 2 the target is 0), within 0.09 of ζ(θ) = 2(1 − 1/θ)/ ln 2 for 0.5 ≤ θ ≤ 2
(SI S2). Larger sizes: at θ = 0.5, Uc (800) = 1.3827161 and the fit on n = 400–800 gives a0 − ln 4 = −1.6 × 10−6 and
a1 = −2.88, the fitted ζ(0.5) of the Methods; at θ = 1.5 (n ≤ 400), a0 − ln(4/3) = +1.5 × 10−7 . (c) For θ ≥ 2, where the
limit is 0, Uc (n) decreases as about 1/n: n Uc (200). (d) Division into k = 3 daughters (n ≤ 60, extrapolated).
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

Supplementary Table S2 | Exact thresholds Uc (n, R, θ) at finite fecundity (first kernel; the two entries at R = ∞,
n = 200, θ = 1 and 1.5 come from the independent R = ∞ kernel and were reproduced by the second finite-R kernel).
Umix : well-mixed value at the same R (Eq. 2), the limit n → ∞ at fixed R; at R = ∞ the protocell limit is ln(2/θ) instead
(1.386, 0.693, 0.288).
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

44


[page 45]
Supplementary Table S3 | Scaling limit. Top: Uc − ln(1/θ) at fixed y = n/R for three values of θ, and its extrapolation
(a0 + a1 /n on n = 100–200; a0 + a1 /n + a2 /n2 on n = 50–200). At y = 4, θ = 1.5 is at the floor Uc → 0, that is
Uc − ln(1/θ) → ln 1.5 = 0.405. Bottom: ψ(y) from θ = 1 kernels at n = 50, 100, 200 and its extrapolation; λc = e−ψ .
Values at y = 8 and 16 (R = 25 and 12.5 at n = 200) are the least reliable. Direct simulation of the limit process:
ψ(0.25) = 0.6176 ± 0.0008, ψ(1) = 0.4862 ± 0.0006, ψ(4) = 0.3169 ± 0.0004.
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

45


[page 46]
1211

S5. Variants of the model

1212

Complementary strands (bound proved, S2; limit numerical, two independent implementations). In

1213

the model of Shah et al. 16 , strands are P (polymerase), C (its complement) and X (parasite). A catalyst P

1214

chooses a template among the N − 1 other molecules; C is copied into P and P (other than the catalyst) into

1215

C with probability q, into X otherwise; X is copied into X with weight θ. We take it at infinite fecundity,

1216

with an infinite population and binomial division at 2n molecules; a protocell is alive if it holds at least one

1217

P and at least two functional strands. In the fictitious clock, each of the (p − 1) + c functional templates is

1218

copied at rate 1, so that F = p + c follows the one-strand law exactly; the difference is that a daughter without

1219

P is dead (2.1% of daughters at threshold), which makes F(F − 1) no longer an eigenfunction. The limit

1220

kernel gives λc = 0.513188648 (truncation limit, to 10−15 ), hence Uc (∞) = ln(1.9486/θ): 0.66711 at θ = 1,

1221

0.26165 at θ = 1.5 (one strand: 0.28768) and 1.36026 at θ = 0.5 (one strand: 1.38629). At finite n and θ = 1,

1222

Uc = 0.66457, 0.66636 and 0.66710 at n = 20, 64 and 4000, converging as −0.047/n; at θ = 1.5, 0.315 and

1223

0.2776 at n = 20 and 64 (+1.00/n). The passage from the finite chain to the limit kernel is not proved, but

1224

agrees to 10−8 (θ = 1) and 10−7 (θ = 1.5).

1225

Complementary strands at finite fecundity (limit process derived; thresholds numerical).

1226

fecundity, the thresholds of this model were computed without truncation up to n = 100 by an iterative

1227

solver (GMRES with a level-wise Gauss–Seidel preconditioner); it reproduces 36 thresholds computed ear-

1228

lier by direct factorization (n = 10 to 40) to within 6 × 10−11 (same root-finding path), and an independent

1229

code reproduces four of the new ones (n = 60 and 80) to 10−9 . The analogue of Theorem 4 would be

1230

Uc (n, n/y, θ) → max(0, ln(1/θ) + ψc (y)), where ψc = − ln λc is the threshold of the limit process (p, c, u), with

1231

u̇ = p − u, new replicases at rate λpc/u and new complements at rate λp(p − 1)/u (derived; the convergence

1232

of the finite kernels to it is not proved). At y = 0.25, three methods give ψc = 0.555788, and the extrapolation

1233

in 1/n of the thresholds for n = 60 to 100 agrees with the predicted limit to within 5 × 10−7 at θ = 1 and

1234

3.5 × 10−6 at θ = 1.5, but only to 1.1 × 10−3 at θ = 0.5, where convergence is slow. At y = 1 and θ = 1,

1235

ψc = 0.40151 ± 10−5 , and the extrapolated limit exceeds it by 6.2 × 10−5 , a gap that does not close up to

1236

n = 100; at θ = 1.5, where ln(1/θ) + ψc (1) < 0, Uc decreases towards 0. At y = 4, ψc is not determined (a

1237

numerical lower bound is 0.241) and the law is not tested. Complementary strands lower the scaling function

1238

at y = 0, 0.25 and 1: ψc = 0.667, 0.556 and 0.402, against ln 2, 0.618 and 0.486 for one strand (numerical).

1239

Fast parasites in the model of Shah et al. 16 (numerical).

1240

polymerases against parasites copied twice as fast as the polymerase and its complement (their PCP2X

1241

model), with Mmax ≈ 0.2 at a division size of S 0 = 10 strands. Their model is the complementary-strand

1242

variant above with θ = 2, q = 1 − M and n = S 0 /2, their catalytic rate k playing the role of R. With their

1243

rates and an infinite population of protocells, the threshold at S 0 = 10 is Mmax = 1 − e−Uc = 0.273 at k = 25,

1244

0.301 at k = 100 and 0.311 at infinite fecundity (0.406, 0.459 and 0.478 when parasites are copied as fast as

1245

the polymerase, their PCP model). At infinite fecundity it then falls roughly as 1/S 0 (nUc = 2.0 at S 0 = 16,

1246

1.49 at S 0 = 100 and 1.46 at S 0 = 276), to Mmax = 0.0105 at S 0 = 276, towards the limit-kernel value

1247

zero (θ = 2 > 1.9486): it stays below Mmax = 0.5 (Uc < ln 2) at every size and fecundity computed, and

1248

positive at every size computed, as they found. We suggest that the tolerance of fast parasites is therefore a

1249

small-size effect. A stochastic simulation of their model with 1,024 protocells, the population of their Fig. 2,

1250

gives Mmax ≈ 0.20 for PCP2X at k = 25 and 100, and 0.34–0.36 (k = 25) and 0.36–0.40 (k = 100) for
46

At finite

Shah et al. 16 found that protocells keep their


[page 47]
1251

PCP, within 0.04 of their values (≈ 0.2, 0.32 and 0.36; their population size is stated only for their Fig. 2,

1252

not for the figures from which 0.36 and 0.2 come, and the remaining difference at k = 25, 0.32 against

1253

0.34–0.36, is unexplained); the simulated threshold rises with population size (0.25–0.26 for PCP2X and

1254

0.39–0.40 for PCP at k = 25 with 16,384 protocells), and a finite population cannot survive indefinitely

1255

above the infinite-population threshold, since its protocells form a subset of the branching process (derived).

1256

We suggest that the finite population explains most of the difference between their values and ours. This

1257

concerns the tolerance itself, not their comparison with surfaces, which we did not recompute.

1258

Equal partition of replicases (numerical).

1259

0.6942 and Uc → ln(1.44/θ) (0.365 at θ = 1; already 0.385 at n = 60). The factor two becomes 1.44; it does

1260

not disappear.

1261

Self-copying, total or partial (no threshold at infinite fecundity and bounds on the limit process proved;

1262

scaling derived; closed form and finite-size convergence numerical). Let a replicase choose itself as

1263

template with weight c relative to another replicase, so that p = q(F − 1 + c)/[(F − 1 + c) + θ(N − F)] and

1264

a lone replicase is alive for c > 0; c = 1 is the self-copying variant of SI S1, whose limit kernel has spectral

1265

radius 2q/θ > 1 for q < θ. At infinite fecundity there is no threshold at any size for any c > 0: without decay

1266

a lone replicase never dies, every row of the mean matrix sums to at least one, and to 2(1 − 2− f ) > 1 for

1267

f ≥ 2; the matrix being irreducible, ρ > 1 at every load. At infinite fecundity, θ = 1 and c = 1, F is an exact

1268

eigenvector of the finite kernel, with ρn (q) = Γ(2n + q) E[1{N1 ≥ 1}Γ(N1 + 1)/Γ(N1 + q)]/[n Γ(2n)] → 2q ,

1269

N1 ∼ Bin(2n, 12 ); at U = 10, ρ = 1 + 3.1 × 10−5 for n = 3 to 80. The limits R → ∞ and c → 0 do not

1270

commute: at c = 0 the threshold stays below max(0, ln(1/θ)) + ln 2 at every size and fecundity, whereas for

1271

every c > 0 it is infinite at R = ∞. At finite fecundity the threshold is finite (Uc ≤ ln R, since p ≤ q). The

1272

limit process, with births at rate λF(F − 1 + c)/u, defines ψ(y; c) = − ln λc (y; c); for c > 0, the convergence

1273

of Uc (n, n/y, θ) to max(0, ln(1/θ) + ψ(y; c)) is only numerical (exact kernels up to n = 80; the errors decrease

1274

as 1/n at most values of y when θ ≥ 1, but more slowly at y = 1/2, at y = 1 for c = 1, and for θ < 1).

1275

For y < 12 and c ≤ 1, G[Fu−λc ] ≥ −(1 − λc) Fu−λc , so that the reduced kernel is supercritical as soon as a

1276

lone replicase replaces itself, λc(ln 2 + ℓy ) > ℓy , where ℓy = ln[(1 − y)/(1 − 2y)] is the duration of its cycle;

1277

conversely, F + βyF(F − 1)/u is a supersolution for λ ≤ (y/c)(1 + o(1)), at every y for every truncation. Hence

1278

ln(c ln 2/y) − O(y) ≤ ψ(y; c) ≤ ln(c/y) + O(y) as y → 0 at fixed c ≤ 1: in the limit process there is no threshold

1279

at high fecundity, and the constants diverge as c → 0. To first order in y at fixed c̃ = c/y = cR/n, a lone

1280

replicase is copied in cis with probability λc̃y ln 2 per cycle and dies with probability y, and each cis copy

1281

founds on average G(λ) − 1 ≥ 1 lineages of lone replicases, its own and those made by trans copying in the

1282

new pair before it splits, G being computed from the infinite-fecundity kernel (G − 1 = 1 + 32 λ ln 2 + O(λ2 )).

1283

The threshold λcis (c̃) therefore solves λc̃ ln 2 [G(λ) − 1] = 1 (derived; the limit process reproduces it to

1284

4 × 10−6 ), and λcis ≈ 1/[1 + (1 + c̃2 ln2 2)1/2 ] to within 0.03 in ψ (numerical). The ceiling ln 2 at c̃ = 0

1285

thus gives way to ψ ≈ ln(c̃ ln 2) + 3/(2c̃) for c̃ ≫ 1; at finite y, ψ exceeds ln 2 only for c above a value

1286

that vanishes with y (0.0083 at y = 0.05). In terms of the model, and only numerically, at high fecundity

1287

Uc ≈ ln(1/θ) + ln{1 + [1 + (cR ln 2/n)2 ]1/2 }, to within 0.033 for n/R ≤ 0.1: a lone replicase, which starts

1288

about cR ln 2/(θn) copies on itself per lifetime (a fraction q of them successful), need only replace itself, the

1289

trans copies of the pairs it founds adding the rest. One more bit requires c ≈ 4n/R (numerical, within 15%

1290

for n/R = 0.05–4; Extended Data Fig. 5). Proofs are given in SI S12.3. No polymerase ribozyme is known

With ⌊F/2⌋ and ⌈F/2⌉ replicases in the two daughters, λc =

47


[page 48]
1291

to copy itself in cis: all act in trans on a separate strand, QT45 included, which makes its complement and

1292

then a new (+) strand in two uncoupled reactions 10 ; the clearest case in RNA of a molecule that is both the

1293

catalyst and the template of a complete copy of itself is a ligase that joins two preformed halves of its own

1294

sequence 50 ; earlier RNA systems engineered to be both catalyst and template 51,52 worked by assembling

1295

oligonucleotides, and the first made the complement of only one of its own subunits. The obstacle appears

1296

structural, since a ribozyme must be folded to catalyse and unfolded to be read 10 . Molecules that replicate

1297

in trans are vulnerable to evolutionary extinction, which higher-level selection, such as spatial clustering,

1298

can alleviate; in a spatial model of RNA-like replicators, complementary strands can then specialise, at high

1299

diffusion, into a catalyst and a template 53 .

1300

Spontaneous replication (proved at finite size and for the reduced kernel; derived; numerical).

1301

models of Bianconi et al. 15 , every sequence replicates spontaneously at rate 1 and each replicase adds α to

1302

the replication rate of every sequence other than itself (in R2α, with i replicases, replicases replicate at rate

1303

1 + (i − 1)α and other sequences at rate 1 + iα); protocells divide at m molecules. Our code reproduces 25

1304

of the 26 rows of their Table 1 (51 of 52 values, the last at the rounding boundary), and their R2α model

1305

without spontaneous replication coincides with ours to 10−6 (m = 4–16; with a parasite of weight θ, with the

1306

independent code, θ = 1.5, n = 2–15). In our model, let every molecule also be copied without a catalyst

1307

at rate s per lifetime, a replicase correctly with probability q s , and write χ = sq s for the number of correct

1308

uncatalysed copies of a lone replicase per lifetime; a protocell with a single replicase is then alive. In the

1309

scaling limit the flow becomes u̇ = F − (1 − s)u and replicases are born at rate λF(F − 1)/u + χF (derived).

1310

The pair density no longer bounds the threshold, because it vanishes on the living type F = 1. (i) If χ ≥ 1

1311

there is no threshold, at every size n ≥ 2 and fecundity: h( f ) = f satisfies Kh > h, so that ρ > 1 by the

1312

Collatz–Wielandt inequality; with q s = q, Uc ≥ ln s (proved). (ii) As y = n/R → 0, a lone replicase stays

1313

alone for 1/(1 + χ) lifetimes on average, while its protocell divides about 1/[(1 + χ)y] times; it is revived with

1314

χ
e⊗r,
probability χ/(1+χ), at a uniformly distributed stage of growth (derived). The limit is the kernel B∞ + 1+χ

1315

with e( f ) = 2 f 2− f the mean number of daughters with one replicase and r the type at division of a revived

1316

protocell; its threshold is χ = 1/(G(λ) − 1), G being the mean number of daughters with one replicase in the

1317

tree of B∞ alone (without revivals) issued from a revived protocell, and G → ∞ as λ ↑ 21 , so that λc (0; χ) < 12

In the

1319

for every χ > 0 (proved for this kernel; its identification with limy→0 λc (y; χ) is numerical). To first order
√
ψ(0; χ) = ln 2 + (3 2 − 4) χ (derived); ψ(0; χ) = 0.7215, 0.8140, 0.9956 and 1.7130 at χ = 0.1, 0.3, 0.5

1320

and 0.8; exceeding ln 2 by 10% requires χ = 0.205, and gaining one bit (ψ = 2 ln 2) χ = 0.707 (numerical,

1318

1322

reduced kernel). At finite fecundity more is needed: with q s = q and θ = 1, χ = 0.40 and 0.81 at y = 0.25,
√
0.66 and 0.91 at y = 1. To first order the two corrections add, ψ ≈ ln 2 + (3 2 − 4)(χ − y/ ln 2), so that

1323

χ ≈ y/ ln 2 brings the threshold back to the ceiling at small y (for the exact kernel at n = 20, R = 1600

1324

and θ = 1, χ∗ = 0.0173, against y/ ln 2 = 0.0180); at θ = 1, for n = 20–100 and R = 10–1600, the

1325

exact kernels need χ∗ = 0.017–0.93, within 2.5% of the limit process (numerical). In R2α, a replicase is

1326

never degraded, a lone replicase is copied spontaneously at rate 1, correctly with probability q, and cells that

1327

contain replicases must outgrow parasite-only cells, whose sequences replicate at rate 1; for a lone replicase

1328

this acts as a removal rate w = 1 (derived), so that χeff = q. With the exponential growth of mass-action

1329

catalysis, a lone replicase is revived at a uniformly distributed stage of ln N rather than of N; writing ψlog for

1330

the corresponding limit, the threshold for α → ∞ and m → ∞ with α ≪ 2m is the root of U = ψlog (0; e−U ),

1331

U ∗ = 0.903 (derived; 0.897 with ψ). Our implementation of their model gives 0.906 at α = 1000 and

1321

48


[page 49]
1332

m = 60, decreasing towards U ∗ as m grows (0.904 at m = 120); at lower catalysis the threshold falls below

1333

U ∗ (0.901 at α = 100 and m = 120; 0.872 at α = 10 and m = 60), which we attribute to cycles that are no

1334

longer instantaneous. At fixed m and α ≫ 2m the threshold rises further (1.24 at m = 10, 1.30 at m = 16),

1335

presumably because a lone replicase left alone in a one-molecule daughter waits there and refounds cells

1336

made of replicases only (mechanism derived, not computed); this singular limit is absent from the scaling

1337

limit. Without spontaneous replication the limit α → ∞ gives back ln 2 (at α = 105 , 0.4503, 0.6444, 0.6903

1338

and 0.6931 for m = 4, 6, 10 and 16). For a replicase of 100–200 nucleotides, χ of order 0.1 seems out of

1339

reach; below χ = 0.01 the ceiling moves by less than 0.4%. Proofs and derivations are given in SI S12.2

1340

(Extended Data Fig. 4).

1341

Complex formation (derived; checked by simulation).

1342

quality of a parasite and w the advantage it gains because a replicase bound as a catalyst is unavailable as

1343

a template; the decomposition holds to first order, since w depends on the parasite’s affinity. Takeuchi and

1344

Hogeweg 35 describe the parasite’s advantage from complex formation as “less than two fold”; the factor 2

1345

is, however, the final state of an irreversible association started from free molecules, not a bound, and we

1346

correct it here; their own mean-field model gives a tolerated affinity ratio that decreases without saturation

1347

as binding strengthens 38 . In a protocell with reversible pairwise association (exact canonical ensemble),

1348

w = 1 + (P − 1)Kv exactly for F = 2, with Kv = c1 /K M , c1 the concentration of a single molecule in

1349

the protocell and K M = (koff + kcat )/kon ; in general w ≈ 1 + ctot /K M , linear and unbounded. A Gillespie

1350

simulation gives θ = 2.824, 7.752 and 77.09 against 2.800, 7.798 and 77.05 predicted. The regime of the

1351

threshold (F = O(1), P ≈ n) is the one where w is largest. If instead the next copy always comes from

1352

a complex of frozen configuration, θeff = 2(F − 1)/F, equivalent to a Yule process of rate q/2 in F, and

1353

Uc (∞) = 0.352 rather than 0. For the class I polymerase and short primer–template substrates, Lawrence and

1354

Bartel 45 report a dissociation constant refined to about 0.7 mM and a Michaelis constant of at least 0.4 mM;

1355

since K M ≥ Kd here, we take K M ≈ 0.7 mM. With θ0 = 1:
diameter

1356

c (one molecule)

N = 10

Write θ = wθ0 , with θ0 the intrinsic template

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

1357

(Uc is the limit value ln(2/w), indicative at N = 10.) Keeping w − 1 ≤ 0.1 requires diameters of at least

1358

165 nm at N = 100 and 356 nm at N = 1000. The K M used is that of the class I polymerase for short

1359

primer–template substrates, not for a whole template.

1360

Transient compartmentalization (first and second order derived; thresholds numerical). Compart-

1361

ments loaded at random from a common pool (Poisson, mean µ), which grow and are then all pooled again,

1362

protect replicators against parasites without division 8,17,18 ; in those models the replicator copies itself 17 , or

1363

an external enzyme copies every RNA and selection between compartments relaxes the error threshold 18 .

1364

An independent session computed the cycle for a trans-acting replicase with our growth rule and without

1365

external selection, growth stopping either at a common saturation size or after a fixed time. A rare repli-

1366

case is then alone in its compartment, makes no replicase and returns to the pool, so that the replicase-free

1367

state is neutral to first order; to second order, pairs loaded together compete with lone replicases that fill
49


[page 50]
1368

their compartments with parasites, and the replicase-free state can be stable (derived). With saturation, no

1369

replicase-rich state exists at θ = 1 or 1.5; where one exists (θ = 0.25 to 0.9), the threshold stays below the

1370

well-mixed value ln(1/θ), and in most cases computed at θ = 0.5 the replicase-rich state is bistable with the

1371

replicase-free one (numerical). With a fixed growth time, the threshold rises with the growth G per round:

1372

at θ = 1 and µ = 2 it is 0.170, 0.339, 0.431 and 0.527 for G = 2, 10, 100 and 220 (R = 1000), and 0.601

1373

for G = 2160 (R = 106 ), higher still for µ < 2 where computed (G = 220 and 280 ; numerical). For θ ≤ 1 a

1374

mean-field argument, not a proof, suggests that it tends to the large-protocell value ln(2/θ) only as G → ∞

1375

and R → ∞, with a gap closing as 1/ ln ln G; at θ = 1.5 the computed threshold stayed above ln(2/θ) up to

1376

G = 280 . In no case computed did it exceed the ceiling ln 2 + max(0, ln(1/θ)), the highest ratio to it being

1377

0.87 (numerical). At comparable size and fecundity (µ = n ≥ 5, same R), the threshold at which the pool

1378

still replenishes itself stayed below that of protocells in every case computed; without that condition, the

1379

threshold can exceed it at low fecundity, where the pool shrinks at each round: at µ = n = 10 and R = 10,

1380

against 0.4621 for protocells, it is 0.4634 ± 0.0025 by direct simulation at G = 220 and above 0.50 at G = 240

1381

(numerical). External selection between compartments was not computed.

1382

Protocell fusion (invasion threshold proved; persistence of dense populations numerical).

1383

cells meet pairwise at rate k f (mass action) and fuse, the fused protocell (F1 + F2 , N1 + N2 ) being split at

1384

once by repeated binomial partition while it holds 2n molecules or more, and let density be regulated by

1385

removal at rate µX per protocell, X being the density of protocells. (i) Starting from a world without vesicles,

1386

fusion between protocells is of second order: the linearization at extinction is the mean generator of the

1387

branching process of the main text, extended to protocells with F ≤ 1, which produce no living protocell;

1388

those with F = 1 lose their replicase at rate one. Its growth rate has the sign of ρ − 1, so the invasion

1389

threshold is Uc for every k f , µ and fusion rule (proved). Fusion with pre-existing vesicles that carry no

1390

replicase, a fixed background or a resident population, is of first order: empty vesicles leave the dynamics

1391

unchanged, and vesicles that carry parasites only dilute replicase pairs, so that no fusion raises the threshold

1392

above max{0, ln(2R/(R + 1)) + max(0, ln(1/θ))}, below the ceiling (proved); the regulation does not count the

1393

background. Such fusion lowered Uc in all 54 computed cases (numerical), 30 of which are invasion thresh-

1394

olds; in the other 24, vesicles without replicases proliferate on the background, and the threshold must be

Let proto-

1396

taken against that resident population, against which the bound still holds (proved). (ii) Near Uc the equilibP
rium density is (ε/k f )v, with v the right Perron vector normalized over all protocells ( v = 1), ε = −r(U)/B

1397

and B = B f − µ/k f , where r is the Malthusian rate, w the left Perron vector and B f = ⟨w, Fus(v, v)⟩/⟨w, v⟩

1398

the reproductive value created by a fusion between two protocells of the invading population (derived; the

1399

simplicity of r and r′ (Uc ) < 0 are checked numerically). For n = 5, 10 and 20, R = 10, 25 and 100 and

1400

θ = 1, B f ranges from −0.200 to −0.121: most partners are vesicles without replicases, whose fusion dilutes

1401

the pairs of living protocells. The bifurcation is therefore supercritical for every k f /µ, and continuation of

1402

17 branches found no stationary population beyond Uc (numerical). If only protocells that carry replicases

1403

fuse, a rule that sees content, B f becomes positive in six of the nine cases and the bifurcation is subcritical

1404

for k f /µ > 1/B f . A dense population then persists up to a load Umax > Uc , beyond ln 2 when k f /µ is large

1405

(Umax = 0.8476 at n = 5, R = 25 and k f /µ = 100, against Uc = 0.6204; Extended Data Fig. 6B), while a

1406

rare population still cannot invade, at fusion rates of hundreds per molecular lifetime; no known chemistry is

1407

proposed for such a rule. Simulations of a finite population illustrate the hysteresis at U = 0.75 (numerical;

1408

SI S12.4). No population, however dense and whatever the fusion rule, keeps a replicase beyond U = ln R

1395

50


[page 51]
1409

(proved). Proofs and derivations are given in SI S12.4.

1410

S6. Measured polymerase ribozymes

1411

Load. U = ℓIε. The information content is the functional information 26 I = − log2 Φ, where Φ = 9.5 ×

1412

10−17 is the abundance of QT ribozyme folds in random sequence that Gianni et al. 10 estimate from its

1413

fitness landscape, so that I = 53.2 bits (Φ = 4.4 × 10−18 , or 57.7 bits, in the preprint version, ref. 54). ℓ is

1414
1415

the number of lethal substitutions per bit: for a function carried by independent sites where site i tolerates
P
P
ti of the four bases, I = i log2 (4/ti ) and the lethal target of a substitution is nl = i (4 − ti )/3, so that

1416

ℓ = nl /I is 0.5, 0.667 or 0.803 for ti = 1, 2 or 3, and 1.10 for an imposed Watson–Crick or G·U pair. For

1417

QT45, Gianni et al. 10 report the tolerance of each site at 80% of wild-type activity, the threshold behind

1418

their estimate of Φ: the fraction of the four bases tolerated at each of 30 unpaired sites, and the fraction of

1419

the 16 pairs tolerated at each of seven base pairs (position 1 is not listed). These fractions give I = 53.2 bits

1420

and, for the unpaired sites, nl = 19.0. At a base pair that tolerates k of the 16 pairs, between max(0, 7 − k)

1421

and min(6, 16 − k) of the six single substitutions are lethal; which ones is shown only graphically (ref. 10,

1422

fig. S21). Hence nl = 27.0–32.0, and 29.8 if the tolerated pairs are placed at random among the 15 others,

1423

so that ℓ = 0.56 (0.51–0.60); spreading 53.2 bits evenly over 45 sites would give 0.63. The double mutants

1424

of table S5 of Gianni et al. 10 narrow this range: the nine pairs two substitutions away are double mutants, so

1425

that the single substitutions tolerated at a pair are k − 1 minus the tolerated double mutants (those not listed

1426

counted as not tolerated), which gives nl = 30.3 and ℓ = 0.57, or 0.56–0.59 when double mutants within 0.3

1427

of the threshold in log2 fitness are counted either way. We use ℓ = 0.56 throughout; 0.57 would raise every

1428

load by 2%. Most published error rates are measured on full-length products, in which copies stalled after a

1429

mismatch do not appear; the full-length error rate is then the rate at which complete parasites are made, and

1430

no further correction for stalling is applied. The types of measurement differ, however (Table S4, note), and

1431

applying each error rate to a 53-bit replicase is a normalization: except for QT45, the polymerases measured

1432

are longer, and their own information content is unknown.

1433

Fecundity. R = Y t1/2 /(T ln 2), the number of complete copies per template per unit time times the mean

1434

template lifetime, assuming synthesis linear in time; published data are single end points, so this assumption

1435

cannot be checked. In the model, R is the number of copies a replicase starts per lifetime, all of which

1436

complete; if catalysts and templates have the same lifetime and are drawn from one population, it equals the

1437

number of complete copies made per template lifetime. When the catalyst is in excess over the template, as

1438

for QT45 (tenfold), fecundity per replicase is lower, by up to that excess; for 24-3, catalyst and template are

1439

equimolar (100 nM each), and for 52-2 the parity is probable but not verified. For the 29-nucleotide fragment

1440

copied under pH–freeze–thaw cycles, the net amplification per cycle is A = 1 + g − d, with g the complete

1441

copies per template per cycle and d ≤ 1 the fraction of templates lost per cycle; the number of copies per

1442

template lifetime is g/d = 1 + (A − 1)/d ≥ A whenever A > 1, so that A = 1.26 bounds R from below. The

1443

fraction of copying slots that end in a complete copy is σ = Ytc /T , with tc the time needed to make one copy

1444

of the object (given, or bounded, in Table S4 for each system for which σ is reported); it involves no lifetime,

1445

and it counts full-length strands whether or not they have been released from their template.

1446

Caveats. For QT45, the half-life was measured “in standard reaction conditions” (ref. 10, fig. S8: 50 mM

1447

CHES-KOH pH 9, 50 mM MgCl2 , −7 ◦ C, an exponential fit to three replicates giving a decay constant of
51


[page 52]
Supplementary Table S4 | Measured systems (Extended Data Fig. 2A, Extended Data Table 2). U for a 53.2-bit
replicase with ℓ = 0.56. Yields, times and half-lives as compiled for this study from the primary sources cited. t1/2 :
template half-life, measured (m) or calculated (c) from the RNA hydrolysis law of Li and Breaker 55 , in the form given
by Wayment-Steele et al. 56 , where it is parametrized between 5 and 10 mM Mg2+ ; for QT45, the calculated value is
the measured one multiplied by the ratio the law gives between the nominal compositions of the two buffers (SI S6);
calculated values for the class I lineage (200 mM Mg2+ , far outside that range) are lower bounds. tc : time to make one
copy.
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
ligase 28 and a hammerhead
(ref. 29; lengths not stated);
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
products 29 ;
0.920, all
products 28

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

(a) the class I ligase 31 ; (b)
0.917 (ref. 30);
110-nt products, yield
0.856 and 0.841
extrapolated to 182 nt;
(ref. 31)
class I conditions
29-nt fragment of the TPR’s 0.974 (ancestor
own catalytic core, from a
t5+1, ref. 49;
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
28,29)

52-2 (refs.
30,31)

TPR
fragment 32

tC19Z 33

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
products on a C-rich template (0.97) and all oligomeric products, partial ones included (0.920), as Tjhung et al. 29 note; 52-2, a
hammerhead template (0.917), a single pass on the hammerhead (0.856) and synthesis of the class I ligase (0.841); t5+1, average
positional fidelity; tC19Z, sequenced full-length products.

1448

0.0059 per day, R2 = 0.94), not in the 0.4 mM Mg2+ buffer in which it copies itself; since RNA cleavage is

1449

catalyzed by Mg2+ , the measured value is probably a lower bound. The calculated value extrapolates it: the

1450

measured half-life times the ratio, 18.5, that the RNA hydrolysis law 55,56 gives between the copying buffer

1451

(0.4 mM MgCl2 , 1.2 mM KCl, 1 mM CHES-KOH, pH 9) and that of the measurement, hence a factor of

1452

18.5 on R. This assumes that the law, although wrong in absolute value and parametrized only between 5

1453

and 10 mM Mg2+ , gives the right dependence on Mg2+ and K+ between the two buffers at −7 ◦ C and pH 9.

1454

Its Mg2+ term contributes a factor of 47.6 and its K+ terms a factor of 0.389; a Mg2+ exponent of 0.7 or

1455

0.9 instead of 0.8 would divide or multiply the ratio by 1.6 (an illustration, not an estimated uncertainty).
52


[page 53]
1456

These compositions are those reported before freezing 10 . In eutectic ice the solutes concentrate by a factor

1457

inversely proportional to the total solute content of each buffer, which is 44 times larger in the buffer of the

1458

measurement. Were the two liquid phases to reach the same total concentration, the Mg2+ ratio would fall

1459

from 125 to about 3, the ratio of the law to 2.7–3.8, and the lower end of the fecundity gap would rise from

1460

10 to 47–67 (a conjectural reading, for total concentrations of 3.76 to 1 mol kg−1 , the first being that of an

1461

ideal solution freezing at −7 ◦ C). Only the ratio is used, because the law alone predicts 50 d in the buffer

1462

of the measurement at the potassium estimated below (32–82 d for 5 to 50 mM), 57% below the measured

1463

value. The potassium brought by the base that titrates the CHES is not reported; for the CHES pKa of 9.39

1464

at 25 ◦ C 57 we estimate it at 14 mM in the buffer of the measurement, whose legend lists no KCl, and at

1465

0.29 mM in the copying buffer, whose potassium is then 1.5 mM (a pKa of 9.3 or 9.5 would give a ratio

1466

of 17.7 or 19.7). Case (b) underwent one pH–heat–freeze cycle, whose potassium hydroxide adds 0.59 mM

1467

of K+ if the KCl reported excludes it; its calculated R would then be 15% higher. The ratio depends on

1468

the potassium of the measurement (ratio 11–29 for 50 to 5 mM, the copying buffer held fixed, a range that

1469

also covers a common change of both) and on the potassium exponent of the law (ratio 14–24 for 0.55 to

1470

0.30); together, these place the lower end of the fecundity gap of QT45 between 5 and 25 rather than at 10.

1471

The main text of Gianni et al. 10 calls the conditions of that measurement “standard reaction conditions”, for

1472

which their supplementary material fixes no buffer: its description of standard reactions refers the final buffer

1473

concentrations to each figure legend, and at 50 mM MgCl2 some legends list 200 mM KCl (their Fig. 1D and

1474

figs. S2, S4 and S9A,B), most list none (their Figs. 1F, 2 and 3 and figs. S8, S9C, S10–S13, S23–S25, S27

1475

and S33). With 200 mM KCl in the buffer of the measurement, the ratio would be 6.7, the law alone would

1476

predict 138 d, 18% above the measured value (a level that does not decide between the two readings, since

1477

the law is parametrized only between 5 and 10 mM Mg2+ ), and the lower end of the fecundity gap would

1478

be 27 (15–51 for potassium exponents of 0.30 to 0.55, and 172–185 in the conjectural reading of equal total

1479

concentrations). The reading of the legend, used here, is the more favourable to QT45. The ribozyme was in

1480

tenfold excess over the template. The time tc to make one copy of QT45 is not measured: neither the accepted

1481

version of Gianni et al. 10 nor its supplementary material reports a time course of these two syntheses. Shorter

1482

reactions are shown, but under other conditions and without a yield. The supplementary material of Gianni

1483

et al. 10 reports an optimization of 26 d for the synthesis of the complementary strand, case (a) of Table S4,

1484

at varied ribozyme and triplet concentrations, with full-length product marked (fig. S28), and reactions of

1485

27 to 30 d for the synthesis of QT45 itself, case (b), in the same 0.4 mM Mg2+ but at 40 nM ribozyme or

1486

less instead of 80 nM — a strand-inhibition series (fig. S29), a scan of hexamer substrates (fig. S30) and the

1487

controls of the sequencing reactions of their Fig. 4 (fig. S34), the last two with full length marked, in part

1488

by the recombination noted below. The preprint version 54 reports 28 d for the complementary strand at up

1489

to 125-fold higher concentrations (ribozyme and Mg2+ ; primer and template 31-fold, triplets 35- to 50-fold),

1490

and 33 d for QT45 itself at a fivefold lower ribozyme and a fourfold higher triplet concentration, with the

1491

same 0.4 mM Mg2+ . Read as copy times, these durations would lower σ to (6.4–9.3) × 10−4 . We keep the

1492

bound that needs no such reading: a complete copy is made within the reaction time of the yields, tc ≤ T ,

1493

so that σ ≤ Y. The yields themselves are upper bounds as well: Gianni et al. 10 report a background of full-

1494

length product formed by recombination rather than by synthesis, separated from the synthetic product only

1495

for sequencing. For 24-3 the two published fidelities count different products: 0.97 for full-length products,

1496

which we use, and 0.920 for all products, partial ones included; the difference itself shows that mismatched

1497

intermediates are less often extended to full length 29 ; for 52-2, the fidelity depends on the template and on

53


[page 54]
1498

the Mg2+ concentration. For the class I polymerases, fecundity was measured on templates other than the

1499

replicase itself or extrapolated to its length; for 52-2, the values (b) extrapolate a 20-min yield linearly over

1500

a lifetime and over a copying slot 27 times longer, whereas products completed within 20 min imply a much

1501

faster subpopulation; the values (a), measured over 24 h on the synthesis of the class I ligase 31 , are the more

1502

reliable. The only fecundity above one belongs to a 29-nucleotide fragment, not to a replicase, copied by

1503

a polymerase whose own fidelity in these conditions is borrowed from its ancestor: Attwater et al. 32 report

1504

no error rate of its own. That borrowing is probably optimistic: the 0.974 of t5+1 was measured at pH 8.3,

1505

and Gianni et al. 10 measure 0.895 for the same lineage at the pH 9 of the eutectic conditions, attributing the

1506

difference to the assay pH. At 0.895 a 53-bit replicase would carry U = 3.1 instead of 0.77, which widens the

1507

load gap of the TPR fragment from 1.1 to 4.5 without changing the direction of the comparison. Its 1.26 is

1508

the highest amplification per cycle reported, obtained in the most favourable condition tested (a tenfold lower

1509

starting concentration of the duplex), so the bound R ≥ 1.26 applies to that condition. For tC19Z, the 0.9912

1510

is an aggregate over sequenced full-length extension products; the per-base error spectra (ref. 33, fig. S8c)

1511

show that it is, to within 10−4 , the unweighted mean of the four per-base fidelities, whereas the pooled error

1512

rate over the 2,195 positions sequenced is 5.9 × 10−3 , from 13 errors in all, none of them opposite U; the

1513

Poisson interval on 13 errors alone spans a factor of about three in error rate. The 0.998 on the hammerhead

1514

rests on two errors.

1515

How to measure R (a proposal).

1516

complete copies of its own sequence that one replicase molecule makes in all, in the conditions in which

1517

it copies itself. Two measurements, with opposite biases, would fix it. In an exhaustion assay, the repli-

1518

case, sub-stoichiometric to its own sequence as template and to primer and substrates, is incubated until

1519

full-length product stops accumulating; R is the product per replicase molecule initially present, authenti-

1520

cated by sequencing, and replenishing the substrates shows whether the plateau comes from the catalyst.

1521

Independently, the initial rate kc of complete copies per replicase and the lifetime τ of its activity, measured

1522

in the same buffer, give R ≈ kc τ. To our knowledge neither has been reported for a polymerase ribozyme

1523

copying its own sequence: the estimates above combine single end-point yields with half-lives. The assay

1524

itself is not new: for the triplet polymerase on an exogenous template, 22 full-length complementary strands

1525

per ribozyme were measured by gel densitometry in 24 h in eutectic ice, falling to 1.8 when the catalyst was

1526

raised from 0.4 to 10 nM at a fixed 40 nM primer and template (ref. 32, Extended Data Fig. 1b). Turnover

1527

should be read where it saturates as the catalyst is diluted, and reported per catalyst molecule rather than

1528

per template, the two differing by up to the catalyst excess (tenfold for QT45, Table S4); for a replicator

1529

copied through its complement, both half-reactions should be reported. A time course would test the linear

1530

synthesis assumed above, and the half-life of the replicase in the buffer in which it copies itself would re-

1531

move the extrapolation discussed in the caveats. The prediction is then testable: a replicase in protocells that

1532

grow from about 50 to 100 molecules gains less than half of the ln 2 that compartments can add, whatever its

1533

fidelity, unless it makes, on average, more than 10 complete copies of its own sequence per lifetime (proved,

1534

computer-assisted; SI S3).

1535

S7. Provenance

1536

All numbers are produced by scripts in the project archive (directory replicateur/), with logs and JSON

1537

outputs. Fig. 1: these_fig1_these_v015c.py (verif3_out.json; rmin_exacts_v015.json, from

The fecundity of the model is a total turnover number: the number of

54


[page 55]
1538

rmin_exacts_v015.py, exact roots of ρ = 1 in R; these_frontieres.json). Fig. 2: these_fig1_

1539

schema.py. The proofs summarized in SI S2, S3 and S5 are written out in full in notes deposited with

1540

the code[ (in French; English versions to be deposited before submission)], each checked by an indepen-

1541

dent session. The ceiling for any division that ignores which molecules are replicases, with complementary

1542

strands, and the bracket on the price: PLAFOND_PAIRES_v0.1; the size clock, (H2) and (H3) for y < 1, and

1543

λc > 21 : HORLOGE_TAILLE_v0.1; the uniform drift, the convergence for y < 1 and Theorem 4: CONJ1_

1544

R_SUP_N_v0.1; (H3) at every y: NOTE_H3_v0.2.1; the convergence at every y and the bracket without

1545

(H2): NOTE_PROP_D_v0.3; the Schur reduction and its limit passage: PREUVE_CONJECTURE1_v0.2. The

1546

bound for R ≤ n/5 (SI S3), whose proof rests in part on computations in interval arithmetic and with a priori

1547

rounding-error bounds: RESULTAT_PRIX_v0.1, whose proof is the written argument with the scripts iv_

1548

np.py, c_params.py, c00, c01, c03, c04, c05, c10 and c11 and their logs (the logs c02_* and *_y5_

1549

log.txt are superseded, and sections 0 and 7 of the note, which predate its checks, are superseded by SI S3,

1550

its section 8 being completed by the credit to P6 (a) of PLAFOND_PAIRES_v0.1, as VERIF_RESULTAT_

1551

PRIX_v0.1 asks), checked by an independent session (VERIF_RESULTAT_PRIX_v0.1) and rechecked

1552

with separate code (VERIFICATION_THEOREME_P_v01). The certified bounds on ψ (SI S3): RESULTAT_

1553

CERTIF_Y_SUP1_v0.2 and RESULTAT_MONOTONIES_v0.3, with their scripts and logs, each checked by

1554

an independent session with its own code (VERIF_CERTIF_Y_SUP1_v0.1, VERIF_MONOTONIES_v0.1),

1555

and, for λc ≤ 0.65 at y < 1, RESULTAT_H2_SUITE_v0.1 (VERIF_RESULTAT_H2_SUITE_v0.1; redone

1556

from scratch, with the bound for R ≤ n/5, in VERIF_THEOREME_P_CERTIFICAT_v0.1); transient com-

1557

partmentalization and complementary strands at finite fecundity (SI S5): RESULTAT_TRANSITOIRE_v0.2

1558

and RESULTAT_BRINS_GRAND_N_v0.3 (VERIF_TRANSITOIRE_v0.1; VERIF_BRINS_GRAND_N_v0.1 and,

1559

for v0.3, VERIF_BRINS_GRAND_N_v0.3_controle). The frontier of half the bonus, the pair density at

1560

finite size with the upper bounds on Rmin , and the bounds for y ≥ 1 (SI S3): RESULTAT_FRONTIERE_

1561

MOITIE_v0.2, RESULTAT_MONOTONIES_R_MIN_v0.2 and RESULTAT_H2_Y_SUP1_v0.2, each checked by

1562

an independent session with its own code (VERIF_FRONTIERE_MOITIE_v0.1, VERIF_MONOTONIES_R_

1563

MIN_v0.1, VERIF_H2_Y_SUP1_v0.1); the extinction bound (SI S3): RESULTAT_PRIX_v0.2 (VERIF_

1564

RESULTAT_EXTINCTION_v0.1); the test of the update rule of the lattice (SI S10): RESULTAT_DIAG_

1565

EXCES_1024_v0.2, with tests fixed in advance but not checked by an independent session. The correc-

1566

tions made to these notes after their checks are not re-verified, except those of RESULTAT_BRINS_GRAND_

1567

N_v0.3. The lever (SI S2, Extended Data Fig. 3): NOTE_LEVIER_v0.2; spontaneous replication (Ex-

1568

tended Data Fig. 4): NOTE_SPONTANEE_v0.2; partial self-copying (Extended Data Fig. 5): NOTE_CIS_

1569

PARTIEL_v0.2; protocell fusion (Extended Data Fig. 6): NOTE_FUSION_PROTOCELLULES_v0.2; these

1570

four (SI S2 and S5) are deposited with their scripts and logs (directories levier/, spontanee/, cis_

1571

partiel/ and fusion_protocellules/), and their proofs are given in English in SI S12. The compari-

1572

son with the model of Shah et al. 16 (SI S5) rests on RECONCILIATION_SHAH_v0.2 (v0.1 checked in VERIF_

1573

RECONCILIATION_SHAH_v0.1) and its scripts, and the paragraph on measuring R (SI S6) on MESURE_R_

1574

v0.4 (v0.1 to v0.3 checked in VERIF_MESURE_R_v0.1 to v0.3)[ (neither current version yet re-verified)].

1575

The proof of Theorem 4 for R > n in English (S13): SI_THEOREME_G_v0.2.1, written from CONJ1_R_

1576

SUP_N_v0.1, PREUVE_CONJECTURE1_v0.2 and HORLOGE_TAILLE_v0.1, checked by an independent ses-

1577

sion, its corrections checked again (VERIF_SI_THEOREME_G_v0.1 and its control)[ (v0.2.1 applies three

1578

minor corrections without a new check)]. The slope of ψ (Theorem S, S14): PENTE_T8B_v0.2.1 and its En-

1579

glish text SI_PENTE_T8B_v0.2, checked (VERIF_PENTE_T8B_v0.1, VERIF_PENTE_T8B_v0.2, VERIF_

55


[page 56]
1580

PENTE_T8B_v0.2.1); S14 is the English text of v0.1 with the corrections of these checks and three pas-

1581

sages of v0.2. The necessary price (Theorem Q, S3): PRIX_NECESSAIRE_v0.2 and its English proof SI_

1582

THEOREME_Q_v0.2, checked (VERIF_PRIX_NECESSAIRE_v0.1, whose one important finding v0.2 corrects,

1583

and VERIF_PRIX_NECESSAIRE_v0.2: no critical or important finding). Incomplete copies and baths of

1584

several lengths (S8, S9): BAIN_INACHEVEES_v0.2 and its English section SI_BAIN_INACHEVEES_v0.1,

1585

checked (VERIF_BAIN_INACHEVEES_v0.1, VERIF_BAIN_INACHEVEES_v0.2, which writes out the proof

1586

of lim inf n mc (n) ≥ m∞ ), with the statuses of these checks. Extended Data Fig. 7: figure_une_courbe_

1587

v0.3, checked in its first version (VERIF_FIGURE_UNE_COURBE_v0.1)[ (v0.2 applies the findings and v0.3

1588

changes only the labels, without a new check)]. The literature on self-copying (S5): BIBLIO_REPLICASE_

1589

CIS_v0.2, checked in its first version (VERIF_BIBLIO_REPLICASE_CIS_v0.1)[ (references checked online

1590

by one agent; of those added to the bibliography, two were checked again in this lineage, and three, Doudna

1591

1991, Green 1992 and Mills 1967, are to be confirmed on the publishers’ pages)]. These pieces, from the

1592

AI lineage “fusion”, are deposited with their scripts and logs[ (notes in French; none rechecked in this lin-

1593

eage)]. The SHA-256 digests of all these notes are listed with the code. Extended Data Fig. 1: these_fig2_

1594

plafond.py (data verif3_out.json, independent R = ∞ kernel). Fig. 3: these_fig3_fecondite.py

1595

(seuil_R_fini_exact.json, psi_extrapole.json, verif4_v06_out.json, and verif3_out.json

1596

for the R = ∞ lines of panel C). Extended Data Fig. 2: these_fig6_ribozymes_v126.py (these_

1597

frontieres.json, from these_frontieres.py; the fecundity of QT45 from qt45_R_optionB_v03.py,

1598

which also gives the numbers of SI S6 on its half-life; the other measured fidelities and fecundities are entered

1599

in the script from Table S4). The number of lethal substitutions per bit: qt45_ell.py; every load and fidelity

1600

target that depends on it, including Table S6: these_charges_v06.py. Finite-R kernels: seuil_R_fini_

1601

exact.py and the independent verif4_R_fini.py; analysis: seuil_R_fini_analyse.py; identity at

1602

θ = 1: verif_Z_theta1.py. Tables S2 and S3 are written by manuscrit_these/make_si_tables.py

1603

from the analysis log. Theorems 2–3, numerical checks: limite_et_borne_ln2.py, and the indepen-

1604

dent checks in verification_scripts/ (suffix _v04); the bound at every fecundity, the spectrum at

1605

θ = 1 and the limit for θ > 1 (SI S2): verification_scripts/v1408_theoremes.py; the numeri-

1606

cal support of hypothesis (H2) for y ≥ 1 (SI S3): the logs lotC_04_pdmp_limite_log.txt and lotC_

1607

05_complements_log.txt of an independent check of the proofs, in commun/verif_scripts/verif_

1608

conj1_lotC/; the first-order correction (SI S2): correction_1n.py, from the thresholds of verif3_

1609

runs.py, and complements_v127.py for Table S1. Complementary strands: shah_brins.py; sponta-

1610

neous replication: bianconi_R2a.py; complex formation: verif3_runs.py (parts G and H); thresholds

1611

against θ at R = ∞: complexe_vs_ln2.py and complexe_limite.py. Unfinished copies (Fig. 4, SI S8):

1612

tronque_protocellule.py (R = ∞) and tronque_R_fini.py (finite R, including the fecundity re-

1613

quired), figure these_fig4_tronque_v08.py (vanishing points: tronque_zeros_v08.py); independent

1614

checks in commun/verif_scripts/ (prefixes v1, v2, v7, v8). The common axis (Fig. 5, SI S9 and S11,

1615

Tables S5 and S6): noyau_classes_arnoldi.py (length classes; lineages: section mecanisme, tc_de_

1616

n.py and tc_de_n_v2.py) and seuil_de_b_U0.py (a single truncated length), figure these_fig5_axe_

1617

v1212.py; independent checks with prefixes v3, v9 and v11. The per-nucleotide variants with the lattice

1618

timing, and the limit kernel at n = ∞ (Figs. 5A, S2 and S3, Table S5, SI S9): replicateur/article_

1619

unique/, with seuil_b_infini.py (exact kernels by noyau_classes_arnoldi.py, limit kernel by

1620

noyau_limite_bain.py, in replicateur/mecanisme_bain/), seuil_b_geometrique_n.py (without

1621

the lattice timing) and seuil_b_infini_tableau.py; shapes, neq and figure data: these_axe_v11.py

56


[page 57]
1622

and these_axe_v111.py; Fig. S2: these_figS2_v1212.py; Fig. S3: these_figS3_v1302.py; in-

1623

dependent checks, including the splittings of the length classes, with the prefixes vplan and vinf in

1624

commun/verif_scripts/. Every length (from b = 0.3 at n = 20, beyond b = 4/9 at larger n), its limit

1625

and finite fecundity (SI S9): noyau_couches.py (exact kernels with several classes), mc_longueurs.py

1626

(Monte Carlo over every length) and noyau_R_fini.py (finite R), in replicateur/article_unique/,

1627

with the tables seuil_b_longueurs_tableau.py, toutes_longueurs_n20_tableau.py and r_fini_

1628

tableau.py; the shapes with every length (points of Figs. 5A and S3A): toutes_longueurs_axe_

1629

v127.py; the levels against the lattice and Fig. S3: niveau_reseau_v127.py, complements_v127.py

1630

and complements_v128.py (ratios at R = 3, minimal fecundities). The lattice and round-18 (SI S10):

1631

axe_reseau_v08.py, whose output these_axe_v11.py reads, and axe_reseau_v127.py, which recom-

1632

putes the brackets on D; both read the published threshold of Tupper and Higgs 5 , extracted from the

1633

vector graphics of the published figure by a script deposited in replicateur/reseau/, and the logs of

1634

the reimplementation, deposited there with its simulation code, the definitions of its series and the out-

1635

put of each deposited point (surviving runs, mean densities, extinction times), in deposits described by

1636

replicateur/reseau/LISEZMOI_depot_v1302.md; we use its series in the termination probability at

1637

kpol = 25, without point mutations or initial parasites, on the 256 × 256 lattice with the replicable fate (runs

1638

to t = 120, 500 and 1000) or the lost fate (runs to t = 120) and on the 512 × 512 lattice with the replicable

1639

fate (runs to t = 120), and none of the others (other durations, lattice sizes, time steps, lengths, copying rates,

1640

error rates or fates of unfinished copies); the brackets from all these series (SI S9 and S10, Figs. 5A, S2 and

1641

S3): reseau_t500_v1211.py, reseau_v1212.py, reseau_v1214.py and reseau_v1302.py, from the

1642

raw points; for D read on the truncated share of products, axe_reseau_v127.py also reads the protocell

1643

thresholds of Fig. 5A. The double-mutant constraint on ℓ: qt45_ell_v2.py. The bath of slow truncated

1644

copies (SI S9, Fig. S1): replicateur/mecanisme_bain/, with mecanisme_bain_suite.py (exact ker-

1645

nels, by the code noyau_classes_arnoldi.py copied unchanged), noyau_limite_bain.py (limit ker-

1646

nel), ancestral_limite_mc.py (ancestral counts at n = ∞) and mecanisme_bain_tableau.py (tables);

1647

figure commun_fig_mecanisme_bain.py; independent checks with the prefix vbain in commun/verif_

1648

scripts/.

1649

S8. Unfinished copies: kernels and identities

1650

Model.

1651

molecules of template weight θ′ ; the copying replicase draws its template among the other molecules in

1652

proportion to their weights, which sum to W = (F − 1) + θA + θ′ B. A copy of a full-length template stops

1653

early with probability τ. With the replicable fate the unfinished copy is a truncated molecule; with the lost

1654

fate it is nothing. A completed copy of a replicase is a replicase with probability q and a parasite otherwise;

1655

parasites and truncated molecules are copied faithfully, and truncated molecules are not truncated again un-

1656

less stated. With retruncation, in the two-class model of SI S9 a copy of a slow truncated molecule stops with

1657

probability τπfast and its product is a fast one; in the per-nucleotide model, a copy of a truncated molecule of

1658

class k stops with probability 1 − (1 − m)Lk , Lk the mean length of the class rounded to a whole number, and

1659

its product is lost or assigned to the class of its length, as after a first stop. Copies occur at rate R per replicase

1660

and every molecule decays at rate 1 (R = ∞: no decay). Division at 2n molecules, binomial partition of each

1661

type, F ≤ 1 a dead lineage, as in the main model.

A protocell holds F replicases, A full-length parasites of template weight θ, and B truncated

57


[page 58]
1662

Identity (i): the lost fate.

1663

length and every copy stops with the same probability τ, whatever its template. A stop changes nothing: it

1664

is a self-loop of the jump chain. The process is therefore, term by term, the main model with copying rate

1665

R(1 − τ); at R = ∞ it is the main model itself. The identity requires that τ be the same for all templates

1666

present; it fails if parasites differ in length from the replicase. A partial loss, in which only some unfinished

1667

copies are lost while others are replicable, is not a rescaling of τ, even at R = ∞: the wasted slots fall only

1668

on full-length templates.

1669

Identity (ii): θ′ = θ.

1670

truncated molecules can be merged into one type Q = A + B: copying a replicase gives a replicase with

1671

probability (1 − τ)q, and a member of Q otherwise; the weights, the division size, the death of lineages and,

1672

since Bin(A, 12 ) + Bin(B, 12 ) = Bin(A + B, 21 ), the partition depend only on (F, Q). The aggregation is exact

1673

(K3 V = V K2 for the aggregation matrix V), so the spectral radii are equal and Uc = Uc(2) + ln(1 − τ) at every

1674

size, fecundity and load.

1675

Identity (iii): termination per nucleotide at b = 1. Let copies stop at each nucleotide with probability

1676

m, products shorter than Lcut nucleotides be lost (SI S10) and longer ones be replicable truncated molecules,

1677

with retruncation, and let parasites have θ = 1, as in Table S6. If copying time does not depend on length

1678

(b = 1), every template yields a product of at least Lcut nucleotides with the same probability (1 − m)Lcut , and

1679

shorter products are self-loops of the jump chain. The next molecule is therefore a replicase with probability

1680

q(1 − m)L−Lcut (F − 1)/(N − 1), and parasites and truncated molecules merge as in (ii): the model is the

1681

main model at θ = 1 with q replaced by q(1 − m)L−Lcut and, at finite R, R by R(1 − m)Lcut , the rate of

1682

copies of at least Lcut nucleotides (R itself when R counts these copies, as in SI S9). Hence Uc (n; m) =

1683

Uc (n; 0) + (L − Lcut ) ln(1 − m) at every size, with R so rescaled at finite fecundity: only stops beyond Lcut cost

1684

load.

1685

Theorem 2 with termination. In the same model with θ = 1, for any 0 ≤ b ≤ 1, with or without retrun-

1686

cation, and whether or not a copy that stops early ends sooner, every template other than the catalyst yields

1687

products of at least Lcut nucleotides at a rate of at least (1 − m)Lcut , in units in which complete copies of a

1688

replicase template occur at rate (1 − m)L . The next molecule is then a replicase with probability at most

1689

q(1 − m)L−Lcut (F − 1)/(N − 1), so the pair density ϕ = F(F − 1)/(N − 1) is a supermartingale during growth

1690

whenever q(1 − m)L−Lcut ≤ 12 ; the death of a random molecule does not raise it on average, and the partition

1691

step of SI S2 applies unchanged. Hence Uc (n) < ln 2 − (L − Lcut )[− ln(1 − m)] at every size and fecundity:

1692

termination and load share the ln 2 of Theorem 2. In the model with stop probability τ and the replicable fate,

1693

the same step gives Uc (n) < max(0, ln(1/θ)) + ln 2 + ln(1 − τ) whenever θ′ ≥ min(θ, 1); identity (ii) gives the

1694

threshold itself at θ′ = θ.

1695

Numerics.

1696

H = (I − PT T )−1 PT D , the binomial partition applied as successive tensor contractions, and the spectral radius

1697

obtained by power iteration (three types) or by Arnoldi iteration with a triangular resolvent (states ordered so

1698

that copies increase the index; at finite R, GMRES preconditioned by the triangular part). Two independent

1699

codes give the same kernels entry by entry (2 × 10−15 on 149 parameter sets, n = 3 to 20; 3.6 × 10−14 on 46

1700

sets with up to five types), and a stochastic simulation confirms them.

With the lost fate no truncated molecule exists, so every template present is full

If truncated molecules are exactly as good templates as parasites, parasites and

Thresholds are computed on the jump chain of the transient states {F ≥ 2, N ≤ 2n − 1} with

58


[page 59]
With θ = 1, θ′ = 2 and n ≤ 20, the share of the tolerable load removed by replicable

1701

Finite fecundity.

1702

truncated copies varies by less than 10% when R goes from 10 to infinity; below R ≈ 10 it grows as R

1703

decreases (by a factor 1.3 at n = 20, R = 3, and 3.8 at n = 5, R = 1.4). At θ = 1.5 (with θ′ = 3, n = 10) the

1704

variation already reaches 12% between R = 10 and infinity. The fecundity required at n = 20, U = 0.30 rises

1705

by factors of 1.04, 1.11, 1.49 and 6.98 for τ = 10−3 , 3 × 10−3 , 10−2 and 3 × 10−2 (replicable fate), against

1706

1/(1 − τ) ≤ 1.031 (lost fate).

1707

Incomplete copies of several kinds.

1708

and correct with probability q if complete, and let an incomplete copy be lost, an inert strand, or a parasite

1709

of class k with template weight θk , copies of parasites being possibly truncated in turn; let σR and sk be the

1710

probabilities that a copy of a replicase, or of a class-k parasite, yields a molecule. (i) Without inert strands, for

1711

any exchangeable division rule and at every size and fecundity, ρ ≤ 1 whenever qσ/ min(σR , mink θk sk ) ≤ 21

1712

(proved): conditionally on producing a molecule, a copy produces a replicase with probability at most this

1713

ratio times (F − 1)/(N − 1), so that the pair density remains a supermartingale during growth, and lost

1714

copies only slow the clock. (ii) If every incomplete copy becomes a parasite, growth therefore requires

1715

− ln(qσ) < ln 2 + max(0, ln(1/θmin )) at every size and fecundity, θmin being the smallest template weight

1716

among the classes: the tolerated point load loses L| ln(1 − m)| one for one, and the third requirement becomes

1717

a ceiling (proved). With the rule Lcut of the lattice transposed to protocells, at b = 1 and without the lost fate,

1718

all classes have the same effective weight and Uc (n, ∞) = max(0, un − (L − Lcut )| ln(1 − m)|) exactly, at every

1719

size (proved). (iii) Lost incomplete copies cost only fecundity: if parasites are truncated at the same rate and

1720

their incomplete copies are lost as well, the kernel is exactly the untruncated one at fecundity Rσ, so that

1721

Rmin is multiplied by (1 − m)−L (proved); but they do not obey the bound on the total load, since a protocell

1722

made only of replicases loses time, not fidelity (an exact counterexample).

1723

S9. The common axis in protocells

1724

Lengths and classes.

1725

truncated copies have lengths uniform on [0.1L, L), as on the lattice; with a stop probability m per nucleotide

1726

they are geometric instead, nearly uniform for small m. The exact kernel cannot carry a continuum of types,

1727

so lengths are grouped into K classes, each with its share of production πk and its mean θk′ . Splitting at the

1728

elbow θ′ = 2 (ξ∗ = (1/2 − b)/(1 − b)) gives a fast class of share (ξ∗ − 0.1)/0.9, 44% at b = 0, 26% at b = 0.25,

1729

none beyond b = 0.444, and a slow class whose θ′ is uniform in 1/θ′ on [1/2, 1) for every b < 0.444. A class

1730

that is never produced must be removed from the state space: otherwise the kernel becomes reducible and an

1731

unreachable component, made of protocells inheriting molecules that are never made, can carry the largest

1732

spectral radius (in one test, ρ = 1.000 instead of 0.666).

1733

Results. Table S5 gives D(0.15) and the value of b at which half of the damage is recovered. One class

1734

at the mean θ′ is misleading: it puts all truncated copies on one side of the elbow. With termination per

1735

copy, from two classes on, the half-point lies between 0.38 and 0.44 (the latter with three classes of equal

1736

production at n = 20, not tabulated) and moves up as the classes are refined, so that two classes give a

1737

conservative estimate of the contrast with the lattice. At finite fecundity (R = 25) the curve is flatter still;

1738

with retruncation (a copy of a truncated molecule may stop in turn) D(0.15) falls to 0.12–0.14 at n = 20 (0.14

1739

with termination per copy, not tabulated), and further as n grows. Over the 44 variants with a distribution

Let a copy of the replicase be complete with probability σ = (1 − m)L

A truncated copy of relative length ξ = L′ /L has θ′ (ξ) = 1/[b + (1 − b)ξ]. Replicable

59


[page 60]
1740

of lengths, D(0.15) lies between 0.05 and 0.31 and the half-point between 0.29 and 0.47 (Fig. S2); on the

1741

lattice, 0.55 and 0.12 in the published simulations, 0.56 (0.53–0.59) and 0.13 (between 0.10 and 0.15 if mc

1742

increases with b) in the reimplementation with runs to t = 120 (SI S10).
Supplementary Table S5 | The common axis in protocells (U = 0, replicable fate, θ = 1, R = ∞ unless stated).
Termination per copy: truncated lengths uniform on [0.1L, L). Termination per nucleotide: a copy stops at each
nucleotide with probability m, products shorter than 10 nucleotides are lost, and truncated lengths are grouped in two
classes split at θ′ = 2; with retruncation, copies of truncated templates stop in the same way; with the lattice timing,
a product of relative length ξ is made at a rate multiplied by θ′ (ξ) (the last of these rows is the variant of Fig. 5A);
n = ∞: limit kernel, with a cutoff of eight fast truncated molecules (SI S9). D(0.15): share of the damage recovered at
b = 0.15; b1/2 : b at which half of it is recovered (linear interpolation on the grid b = 0, 0.05, 0.15, 0.25, 0.5, 0.75, 1; for
the lattices, on their own grids, which add 0.10, 0.26, 0.30 and 0.32 for the reimplementation and 0.1 and 0.2 for the
published lattice, ref. 5). Rows with termination per nucleotide, and the lattice: D is read on the critical termination per
nucleotide mc , and the last column is mc (0.25)/mc (0). For the reimplemented lattice, brackets give the bounds implied
by those of its threshold, for b1/2 if mc increases with b (SI S10).
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

lattice (ref. 5; SI S10)
lattice, reimplementation, t = 120 (SI S10)

1024 × 1024
256 × 256

0.55
0.56 (0.53–0.59)

0.12
0.13 (0.10–0.15)

39
33

1743

Copying as on the lattice.

1744

copies, and a copy that stops early ends sooner, since its duration is set by the length of its product (SI S10).

1745

The variant of Fig. 5A does the same: termination per nucleotide with retruncation, and a product of relative

1746

length ξ made at a rate multiplied by θ′ (ξ), each class being represented by its mean θ′ weighted by produc-

1747

tion. This timing divides the threshold at b = 0 by 3.4–3.5 (n = 20 to 80) but leaves the contrast of shape:

1748

D(0.15) = 0.20, 0.15 and 0.13 for n = 20, 40 and 80, half of the damage is recovered at b = 0.33, 0.35 and

1749

0.35 (0.34, 0.36 and 0.38 on the finer grid of b of Fig. 5A), and b = 0.1 multiplies the tolerable termination

1750

by 1.5–1.6, against 10.4 on the published lattice. D(0.15) falls with n because, with retruncation, mc falls

1751

as 1/n below b = 4/9 (below), whereas mc (1), where every truncated copy has θ′ = 1, does not depend on

1752

n: the range log[mc (1)/mc (0)] grows as log n (1.48, 1.80 and 2.11 decades), and the larger the protocell, the

1753

larger the contrast with the lattice. Two classes are a coarse approximation near the elbow, which lies at

1754

2(1 − τ) rather than at the cut θ′ = 2 (below). With retruncation (n = 20, without the lattice timing), splitting

1755

the slow class at θ′ = 1.4 changes mc by less than 3% for b ≤ 0.15 and D(0.15) only from 0.12 to 0.10, but

1756

lowers mc (0.40) by 26% and D(0.40) from 0.55 to 0.41; cutting at 2(1 − τ) instead lowers D(0.40) to 0.40

1757

and D(0.45) from 0.74 to 0.48. The half-point then moves beyond 0.40, or 0.45, and only D(0.15) carries the

1758

contrast without that reservation. Without retruncation, splitting the slow class raises mc by 9–12% (b ≤ 0.15,

1759

n = 20).

On the lattice, copies of parasites stop at the same rate per nucleotide as other

60


[page 61]
1760

Which protocells carry growth. The left Perron vector u of the kernel gives the composition of the pop-

1761

ulation at division; the lineages that carry growth follow the ancestral (spine) distribution u ◦ w/⟨u, w⟩, with

1762

w the right eigenvector (reproductive values), taken at threshold as the limit of the supercritical case 58 . With

1763

fast truncated copies alone (θ′ = 4.02), the population at threshold is dominated by contaminated protocells

1764

with 3.9 (n = 10) or 4.2 (n = 20) replicases at division, which are dead ends: the sub-kernel of contaminated

1765

protocells is subcritical (spectral radius 0.71–0.72, and 0.67–0.68 with the length distribution below), and a

1766

protocell free of truncated copies has 73 (n = 10) or 279 (n = 20) times the mean reproductive value. Along

1767

the lineages, 63% and 70% of protocells carry no truncated copy, with 19 of 20 and 39 of 40 molecules

1768

being replicases. With the length distribution at b = 0, 87–91% of the protocells along the lineages carry

1769

no fast truncated copy; they tolerate many slow ones (13 of 20, 33 of 40) and about 6.5 replicases, nearly

1770

independently of n.

1771

Why τc depends little on n without retruncation.

1772

replicase more viable than lost copies would (τc = 0.208 against 0.103 at n = 20) and, without retruncation,

1773

nearly independent of n: τc = 0.237, 0.208, 0.196 and 0.190 for n = 10, 20, 40 and 80, against 0.103, 0.049,

1774

0.024 and 0.012 with fast truncated copies alone (Fig. S1A). The lineages that carry growth then live in the

1775

regime of Theorem 1, with few replicases in a bath of slow truncated molecules. With slow truncated copies

1776

alone, copied faithfully, the model is exactly the main model with q = 1 − τ and θ = θ′ , so that the limit

1777

kernel has τc (∞) = 1 − θ′ /2 (0.307 at θ′ = 1.39; extrapolation of n = 20 to 80: 0.30698), and a class of

1778

truncated copies can form such a bath only if θ′ < 2(1 − τ). With fast truncated copies as well, a limit kernel

1779

that follows the replicases of a lineage through a cycle in the bath gives τc (∞) = 0.1845, which the exact

1780

kernels approach (extrapolation of n = 20 to 80: 0.18455). This kernel takes the limits in the order t → ∞,

1781

then n → ∞: a daughter that inherits a dozen fast truncated molecules or more (eight in the per-nucleotide

1782

kernels of Table S5) is counted as lost, since at finite n their descendants invade the bath within O(log n)

1783

cycles, and raising that cutoff does not change the threshold; without that rule, finitely many fast molecules

1784

′
would not affect an infinite bath, and the limit would be 1 − θslow
/2 = 0.307. Along the ancestral lineages

1785

(births weighted by reproductive value, paths weighted by the reproductive value of the division state they

1786

reach), newborn protocells hold about four replicases whatever n, and copies of replicase templates, the only

1787

ones that can stop and so start a new fast truncated molecule, number 2.9 to 2.6 per cycle for n = 10 to 80 (2.6

1788

at n = ∞), against 9.4 to 79.5 without a bath (Fig. S1B); all other copies are of truncated templates, which

1789

never stop. The stops that give a fast truncated molecule therefore tend to a constant number per cycle along

1790

these lineages (0.103 at n = 10, 0.065 at n = 80, 0.062 at n = ∞), and growth passes through lineages whose

1791

few stops gave slow copies: only 23–25% of their stops give a fast truncated copy, against 44% at production

1792

(n = 10 to 50). Slow copies near the elbow (θ′ = 1.9) form a bath too, but with a large 1/n correction: τc falls

1793

from 0.149 to 0.045 between n = 10 and 80, toward 0.034. Letting copies of slow templates stop as often as

1794

those of full-length ones, with the same products (ε = 1, which is the retruncation of SI S8), restores the 1/n

1795

law and empties the bath: nτc is again nearly constant (1.56 to 1.49 for n = 10 to 80), as when unfinished

1796

copies other than fast ones are lost (1.99–2.11 for n = 10 to 50), most copies along the lineages are again

1797

copies of the replicase (two-thirds at n = 10, 94% at n = 50), and at n = 80 the lineages divide with 155.7

1798

replicases among 160 molecules (Fig. S1C). The condition is strict: with ε = 0.1, τc at n = 80 already falls

1799

from 0.190 to 0.080, and it keeps falling with n; with termination per nucleotide, a slow truncated template

1800

of relative length ξ stops about ξ times as often as the replicase, and ξ > 1/2 at b = 0. On the lattice, copies

Slow truncated copies far below the elbow make the

61


[page 62]
1801

of parasites stop at the same rate per nucleotide (SI S10), so that the protocell variant to compare with it is

1802

the one with retruncation, that of Fig. 5A.

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

Supplementary Fig. S1 | Without retruncation, slow truncated copies form a bath that keeps τc finite as protocells
grow (U = 0, R = ∞, b = 0; truncated copies in two classes at the elbow, 44% fast with θ′ = 4.02, the others slow;
SI S9). (A) Critical stop probability against protocell size: fast truncated copies alone; the others lost; slow ones with
θ′ = 1.39, 1 or 1.9; slow ones alone (θ′ = 1.39). Dashes: limit kernel (n = ∞). (B) Copies of replicase templates
per cycle along the lineages that carry growth: about n without a bath, two to three in one. (C) Letting copies of slow
templates stop with probability ετ restores τc ∝ 1/n at ε = 1.

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

Supplementary Fig. S2 | No protocell variant gains from b as early as the lattice (U = 0, R = ∞; black and grey,
the lattice as in Fig. 5A). (A) Termination per copy, truncated lengths uniform on [0.1L, L) in two classes at the elbow,
n = 10, 20, 50. (B) Termination per nucleotide, products shorter than 10 nucleotides lost, two classes: with retruncation,
n = 20, 40, 80 (blue dashes: standard rule, without the lattice timing); without retruncation, n = ∞ (orange; solid: with
the lattice timing, dashes: without). At every interior b of the published lattice curve, each variant shown recovers less
of the damage than the lattice.

1803

Level against the lattice.

1804

three reasons. The lattice is at finite fecundity: a polymerase with a template and a free site copies at rate

1805

kpol = 25 per unit decay rate, but it is not always busy, so that the fecundity at which protocells should

1806

be compared with it is not defined; protocells are at R = ∞ unless stated (finite fecundity: below). The

1807

lattice threshold is the largest m at which at least 5% of 100 runs survive to t = 1000, the protocell threshold

1808

an asymptotic ρ = 1, and the reimplemented lattice, with another criterion and runs to t = 120, puts its

The levels of the two architectures compare only as orders of magnitude, for

62


[page 63]
1809

threshold 1.0 to 1.8 times the published one (0.70 to 1.24 times with runs to t = 500, and 0.92 to 0.99 times

1810

at b = 0.5 with runs to t = 1000; SI S10). And the grouping in two classes moves mc by at most about 12%

1811

for b ≤ 0.15, more near the elbow (above) and beyond it (below). Without retruncation the threshold of the

1812

two-class model has a finite limit at every b (Fig. S3A): with the lattice timing, mc (∞) is 50 times the lattice

1813

threshold at b = 0, 5.7 times at b = 0.15, 3.5 times at b = 0.25 and 2.5–2.8 times for b ≥ 0.5 (143, 10, 5.1

1814

and 2.5–2.8 without it), and at every size computed (n = 20 to ∞) it is at least 2.4 times the lattice threshold

1815

at every b of the published curve. Splitting the slow class raises these values at n = 20 (above), but keeping

1816

every length lowers them: at b = 0.5, by 4–5% at n = 20 and 40 (Monte Carlo over every length, below),

1817

and perhaps much more for large protocells. The large-protocell argument given below, applied without

1818

retruncation, would put the limit at 9.5 × 10−4 at b = 0.5, under the lattice threshold, if the bath sorted

1819

itself toward its shortest lengths; without retruncation only selection between nearly neutral lengths would

1820

sort it, and the limit without retruncation is not established. With retruncation, mc falls as 1/n wherever fast

1821

truncated copies are made, since the bath then makes fast copies at a rate proportional to n (ε = 1 above):

1822

n mc has nearly converged by n = 80 for b ≤ 0.25 with the lattice timing (b ≤ 0.20 without it), changing

1823

by less than 4% between n = 40 and 80, and we extrapolate C(b) = lim n mc as 2 · 80 mc (80) − 40 mc (40).

1824

A protocell then tolerates more termination than the lattice only below neq (b) = C(b)/mlattice
(b) molecules
c

1825

(Fig. S3B): with the lattice timing, neq = 330, 89, 48, 35, 30 and 29 for b = 0 to 0.25 in steps of 0.05, or

1826

185–232, 58–84, 35–48, 21–25 and 19–23 at b = 0, 0.05, 0.10, 0.15 and 0.25 against the brackets of the

1827

reimplemented lattice with runs to t = 120 (rounded outward; 309–464 at b = 0 and 28–34 at b = 0.15 with

1828

runs to t = 500); without it, 1140, 260, 125, 80 and 62 for b ≤ 0.20. At larger b, up to 4/9, n mc still grows

1829

at n = 80, since fast truncated copies are then rare and barely beyond the elbow, and neq is at least its value

1830

at n = 80. Below 4/9 the effect of keeping every length is measured only at n = 20, the Monte Carlo being

1831

trapped at larger n (below), and splitting the classes changes the two-class thresholds by −9 to +5% up to

1832

n = 80: these neq are orders of magnitude.

1833

Near and beyond the elbow, every length. Two classes overestimate the threshold with retruncation near

1834

the elbow, and beyond it increasingly as n grows: each class model tends to the elbow of its shortest class,

1835

represented by a mean, whereas with every length the bath concentrates on the shortest replicable length,

1836

Lcut = 10 nucleotides, which grows fastest. A population Monte Carlo over the 90 lengths (populations of

1837

2,000 protocells, 1,500 at n = 320, validated against exact kernels with three classes up to n = 80; a finite

1838

population underestimates the threshold, by a few per cent where measured) gives at n = 20 thresholds that

1839

the two-class model exceeds by factors of 1.26, 1.33 and 1.50 at b = 0.3, 0.35 and 0.4, and at b = 0.5 and

1840

n = 80, mc = 1.45 × 10−3 against 2.10 × 10−3 with three classes and 3.88 × 10−3 with the cut of Fig. S3A.

1841

The contrast of Fig. 5A is therefore stronger still (its points): at b = 0.5, D = 0.68, 0.66 and 0.66 at n = 20,

1842

40 and 80, instead of 0.82, 0.84 and 0.86, against 0.90 on the published lattice, and at n = 20 half of the

1843

damage is recovered near b = 0.39 instead of 0.34; below b = 4/9 the Monte Carlo is trapped for n ≥ 40, and

1844

D(0.15) and D(0.25) keep their two-class values. For large protocells, Theorem 1 applied to a bath of growth

1845

rate θ′ (Lcut /L)(1 − m)Lcut , against replicase templates copied intact with probability (1 − m)L , gives the limit

1846

m∞ (b) = 1 − [θ′ (Lcut /L)/2]1/(L−Lcut ) in both timings: 1.06 × 10−3 at b = 0.5, 2.74 × 10−3 at 0.6 and 4.86 × 10−3

1847

at 0.75, and 0 for b ≤ 4/9. This limit is derived for the limit kernel: Theorem 1 is proved for a bath of one

1848

type, and its extension to a bath of several lengths rests on a law of large numbers. Its identification with the

1849

limit of mc (n) is conjectural: it assumes that two limits commute, which SI S2 proves for parasites of a single

63


[page 64]
1850

type (Theorem 3) but not for a bath of several lengths; at R = ∞, for classes that differ by their template

1851

weights as in S8, the bracket by the extreme classes and the uniformity in θ of that limit prove only the lower

1852

bound lim inf n mc (n) ≥ m∞ (S9, Several parasite classes). The Monte Carlo thresholds decrease toward it

1853

up to n = 320, and their extrapolations (lattice timing) meet it to within 2% for b ≥ 0.5, the approach being

1854

slower near 4/9. The limit equals the published lattice threshold, interpolated, at b∗ ≈ 0.53 (against the

1855

reimplementation, if mc increases with b: 0.54–0.57 with runs to t = 120, 0.52–0.55 with runs to t = 500

1856

and 0.51–0.54 with runs to t = 1000, rounded outward; SI S10). Beyond b∗ , protocells that copy as the

1857

lattice does then tolerate more termination than it at every size; besides the sizes computed, this needs only

1858

the lower bound lim inf n mc (n) ≥ m∞ , the direction that Theorem 3 proves for a bath of one type, together

1859

with the sizes between, which remain numerical. Between 4/9 and b∗ they do so only below neq ≈ 40 at

1860

b = 0.45, where the lattice is interpolated, and ≈ 80 at b = 0.5 (against the reimplementation, 23–28 and

1861

38–44 respectively with runs to t = 120, 33–40 and 66–80 with runs to t = 500, and 79–109 at b = 0.5 with

1862

runs to t = 1000), by interpolation of the Monte Carlo thresholds in n; these come from populations of 2,000

1863

protocells and are therefore slightly low (Fig. S3B).

1864

Finite fecundity, against the lattice. With fecundity R and decay at rate 1 (each replicase completes copies

1865

at rate R, whatever their length, and products shorter than Lcut cost no time, so that the lattice timing sets

1866

only which products are made), the termination threshold of protocells with retruncation (exact kernels for

1867

b = 0.3 to 1, with two classes of equal width in θ′ rather than the cut at θ′ = 2, which leaves a single class

1868

beyond 4/9) is multiplied at R = 25 by 0.80–0.86 at n = 10, 0.57–0.81 at n = 20 and 0.29–0.68 at n = 40,

1869

and it decreases without a plateau as n grows (computed up to n = 160 with one class, 320 at b = 1), toward

1870

zero (derived in mean field at b = 1): the elbow at b = 4/9 and the advantage at every size beyond b∗ are

1871

properties of R = ∞. At R = 25, protocells tolerate more termination than the published lattice only below

1872

about 23 to 33 molecules for b = 0.3 to 0.6 (about 20 to 28 with every length, an estimate that applies the

1873

finite-R factor of the two-class model to the Monte Carlo thresholds), and 230 at b = 1, where the model

1874

with one class is exact. Which R matches the lattice is not known. R = 25 equals its copying rate; R = 3

1875

puts protocells, whose minimal fecundity without termination is close to 1 (Rc = 1.003 at n = 20), about as

1876

far above it as the lattice at kpol = 25 stands above the rate at which its point-mutation threshold vanishes,

1877

between 8.6 and 9.0 (Fig. 3 of ref. 5). At R = 3, protocells of 10 molecules tolerate more termination than

1878

the lattice at b = 0.3 and 1, and as much to within about 10% from b = 0.45 to 0.75 (two classes), but

1879

protocells of 20 molecules tolerate 15 to 46% less at every b computed.

1880

Several parasite classes at R = ∞.

1881

radius lies between those of the one-class kernels with fidelity qσ/σR and the largest and smallest of the

1882

weights θk′ = θk sk /σR (with inert strands, only the lower bound holds), so that the limit of the threshold

1883

is bracketed by those of the extreme classes (proved, by a monotone coupling of the number of replicases

1884

at division and Gelfand’s formula). The same coupling shows that Uc (n, ∞, θ) does not increase with θ,

1885

so that the limit of Theorem 3 is uniform in θ on [a, ∞) for every a > 0 (proved, with Pólya’s theorem).

1886

(v) If the bath of a lineage settles at a composition with Perron root µ, the threshold at large size would

1887

be − ln(qσ) = ln(2/µ). This is a heuristic conjecture: it is derived under a law of large numbers for the

1888

bath, a condition that no lineage keeps a large bath without the dominant class, and Schur reductions on

1889

compositions, none of which is proved; it is supported numerically on exact two-class kernels up to n = 64,

(iv) At R = ∞, without inert strands, and at every size, the spectral

64


[page 65]
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

Supplementary Fig. S3 | In the two-class model, retruncation decides whether protocells tolerate more termination than the lattice at every size (termination per nucleotide, U = 0, R = ∞). (A) Critical termination per nucleotide:
the lattice (black, published; grey, reimplementation with its brackets: diamonds, runs to t = 120; squares, runs to
t = 500; triangles, runs to t = 1000, with an arrow for a lower bound, every run having survived at the largest m tried;
squares and triangles offset in b, by 0.02 and 0.04 respectively, to the left up to b = 0.5 and to the right beyond; the
triangle near b = 0.59 is thus for b = 0.55); protocells without retruncation at n = ∞ (orange; solid: lattice timing,
dashes: without it), whose threshold stays finite in the two-class model; protocells with retruncation and the lattice
timing, n = 20, 40, 80 (blue), whose threshold falls as 1/n below b = 4/9. The two-class curves overestimate the
threshold near the elbow and beyond (dashes beyond b = 0.3): points keep every truncated length (population Monte
Carlo, offset slightly in b), and the dotted line is the threshold m∞ (b) of the limit kernel (derived; SI S9), which the
points approach and which crosses the published lattice at b∗ ≈ 0.53. (B) Size below which protocells with retruncation
tolerate more termination than the lattice (solid: lattice timing; dashes: without it): neq = C(b)/mlattice
where n mc has
c
nearly converged (two classes), and beyond b = 4/9 by interpolation of the thresholds with every length (circles); neq
is infinite beyond b∗ if the thresholds approach m∞ . Bars: against the brackets of the reimplemented lattice (blue: runs
to t = 120; light grey: runs to t = 500; dark grey: runs to t = 1000).

1890

where the convergence can be slow and non-monotone. When the dominant class has the largest θk′ and is

1891

not truncated into another kept class, ln(2/µ) is a proved lower bound.

1892

S10. The lattice

1893

Model.

1894

site empty or holding a polymerase strand, its complement, or a parasite, of length L = 100 for the first two

1895

and between Lcut = 10 and L for parasites. A strand is copied by a polymerase on a neighbouring site

1896

into an empty site neighbouring the template. The length of the product is drawn first, copying stopping at

1897

each nucleotide with probability m, and a product shorter than Lcut is discarded; the copy is then made at

1898

rate k(l) = kpol L/[bL + (1 − b)l], with kpol = 25, and strands decay at rate 1. Copies of parasites stop too,

1899

so that truncated molecules are truncated again, and a copy that stops early ends sooner, its duration being

1900

set by the length of its product: the closest protocell variant is the per-nucleotide model with retruncation

1901

and this timing, that of Fig. 5A (Table S5). Their runs start from 15% each of polymerases, complements

1902

and parasites of random lengths. Their Fig. 7 gives, for each b, the largest m at which at least 5% of 100

1903

runs keep the polymerase until t = 1000, without point mutations. Read on the vector coordinates of the

1904

published figure, it recovers half of the damage at b = 0.124, with D(0.15) = 0.550, D(0.25) = 0.707 and

1905

mc (0.25)/mc (0) = 38.6, over a range of 2.24 decades; mc (0.1)/mc (0) = 10.4 is the tenfold gain the authors

Tupper and Higgs 5 simulate a 1024 × 1024 periodic lattice with the eight-site neighbourhood, each

65


[page 66]
1906

note.

1907

Reimplementation. An independent implementation of these rules on a 256 × 256 lattice (time step 10−3 ,

1908

runs to t = 120 from polymerase and complement strands without parasites, 20 runs per point, 40 at b = 0

1909

and at the earlier points at b = 1) brackets the critical termination at each b between the largest m at which

1910

some run kept the polymerase and the smallest at which none did. It differs from the published model in

1911

one rule: the strands made during a time step are placed at its end, one chosen at random where several

1912

seek the same site, so that a new strand acts only from the next step, a delay of a thousandth of the mean

1913

lifetime of a strand. Placing each new strand at once instead (a sequential update) changed the extinction

1914

times on the published 1024 × 1024 lattice (b = 0, m = 2 × 10−5 , 28 batches of runs, pooled as planned

1915

in advance) by a factor 1.024 (95% interval 0.904–1.169; the confirmatory test fixed in advance detected

1916

no effect), about +0.9% (−3.8 to +6.1%) on the threshold (derived, as an order of magnitude; not checked

1917

by an independent session), so that this rule matters little. With the central value at the geometric mean of

1918

the bracket, and brackets on D that combine the ends of the brackets of mc (b), mc (0) and mc (1) in the least

1919

favourable way, given mc (0) ≤ mc (b) ≤ mc (1), D(0.15) = 0.56 (0.53–0.59) and D(0.25) = 0.70 (0.67–0.73),

1920

rounded outward. If mc increases with b, half of the damage is therefore recovered between b = 0.10, where

1921

D < 0.46, and b = 0.15, where D > 0.53; interpolating the central values gives 0.13. The bound at 0.15 rests

1922

on the brackets narrowed by a series of runs added at b = 0, 0.15 and 1 (no run of 40 kept the polymerase at

1923

m = 2.5 × 10−5 for b = 0, one run of 20 at 3.5 × 10−4 for b = 0.15, and none of 20 at 3.5 × 10−3 for b = 1);

1924

without that series, the bounds are b = 0.10 and 0.25. Both bounds turn on single runs. With one surviving

1925

run fewer at the lower end of a bracket, one more at its upper end, or one at the next point measured, the

1926

bound at 0.15 falls only with a surviving run at m = 3 × 10−5 for b = 0, where none of 40 distinct runs

1927

survived, and the bound at 0.10 falls without the one run of 40 that kept the polymerase at m = 2 × 10−5 for

1928

b = 0, or with a surviving run at 2 × 10−4 or 3 × 10−4 for b = 0.10, where none of 20 survived; at worst

1929

0.05 < b1/2 < 0.25 remains, the interpolated value staying between 0.09 and 0.15. The reimplementation is

1930

thus consistent with the shape of the published curve, over 2.18 decades, with mc (0.25)/mc (0) = 33. Later

1931

series of runs to t = 120, with 40 runs at the points that bound b∗ (SI S9), narrow the brackets at b = 0.5 and

1932

0.75 to [1.8, 1.9] × 10−3 and [2.5, 2.75] × 10−3 and add b = 0.45, 0.55, 0.6 and 0.65 (Figs. 5A, S2 and S3A).

1933

Runs to t = 500 (b = 0, 0.05, 0.10, 0.15, 0.45 to 0.65 and 1; 20 or 40 runs per point) lower the brackets, by

1934

8 to 27% for b ≥ 0.05 in the ratio of central values and by 45% at b = 0, where survivors are rare; at b = 0.5

1935

the bracket, [1.45, 1.55] × 10−3 , then contains the published threshold. Then D(0.05) = 0.31 (0.26–0.35) and

1936

D(0.15) = 0.57 (0.53–0.61), and half of the damage is again recovered between b = 0.10, where D < 0.494,

1937

and b = 0.15, where D > 0.531; interpolating gives 0.12. Each bound again turns on single runs: in the

1938

same cases, with the upper ends of the brackets at t = 120 as further bounds where the grid at t = 500 ends,

1939

at worst 0.05 < b1/2 < 0.45. Runs to t = 500 still die as late as t = 485, and at b = 0.5 runs to t = 1000

1940

lower the bracket again, to [1.35, 1.45] × 10−3 , 0.92 to 0.99 times the published threshold: the central value

1941

falls by a factor 0.81 from t = 120 to 500 and 0.93 from 500 to 1000. These runs still die as late as t = 959,

1942

so that the threshold may fall further with longer runs, and the published curve, from runs to t = 1000 on

1943

a larger lattice, remains the reference for levels (SI S9). Against the brackets at t = 500 alone, the limit

1944

m∞ (b) of SI S9 crosses the lattice threshold between b = 0.52 and 0.55 if mc increases with b, against 0.54

1945

to 0.57 at t = 120; at t = 1000, every run survived at b = 0.44 and m = 1.1 × 10−3 , a value above m∞ (b)

1946

for every b ≤ 0.5; with the lower end of the bracket at b = 0.5 and the bracket [1.6, 1.7] × 10−3 at b = 0.55,

66


[page 67]
1947

the limit crosses between 0.51 and 0.54, with the upper ends of the brackets at t = 120 and 500 as further

1948

bounds beyond b = 0.55 (survival cannot increase with run length). On a 512 × 512 lattice, with runs to

1949

t = 120 (20 runs per point, 40 for four values of m at b = 0), the brackets at b = 0, 0.15, 0.5 and 1 are

1950

[3.5, 4.0] × 10−5 , [3.5, 4.0] × 10−4 , [2.0, 2.1] × 10−3 and [3.5, 3.75] × 10−3 , and D(0.15) = 0.50 (0.47–0.53),

1951

against 0.56 (0.53–0.59) on 256 × 256; to three decimals, rounded outward, the two ranges are 0.477–0.529

1952

and 0.534–0.589, disjoint, but one surviving run more or fewer at an end of these brackets can make them

1953

overlap. On the larger lattice the range lies below the published 0.550; one more surviving run at b = 0.15

1954

and m = 4 × 10−4 would move it to 0.507–0.555, which includes 0.550. Runs on the larger lattice survived

1955

more often at 10 of the 19 points common to both sizes and less often at none, and died later on average at

1956

17 of the 18 where runs died at both sizes (sign tests, p = 0.002 and p = 1.4 × 10−4 ): at t = 120, a higher

1957

threshold on the larger lattice cannot be told from slower extinction. These brackets take survival of at least

1958

one run, which is 2.5% where 40 runs were made, as at b = 0, and 5% elsewhere. With the 5% criterion

1959

of Tupper and Higgs 5 , D(0.15) = 0.60 (0.55–0.64) on 256 × 256 and 0.54 (0.50–0.57) on 512 × 512 at

1960

t = 120, ranges that overlap (0.554–0.638 and 0.508–0.562 to three decimals, rounded outward), the second

1961

containing the published 0.550, and if mc increases with b, half of the damage is recovered between b = 0.05

1962

and 0.15 at t = 120; at t = 500 the criterion changes no bracket. D(0.15) depends on run length and on the

1963

criterion (0.56 and 0.57 at t = 120 and 500 with the first; 0.60 and 0.57 with the second): the threshold at

1964

b = 0.15 falls with run length, which alone would lower D(0.15) by about 0.06 from t = 120 to 500, and

1965

the threshold at b = 0 rests on rare surviving runs. Runs to t = 1000, and runs from the published initial

1966

condition with 15% parasites, are not used for D(0.15): the values they give hinge on single surviving runs

1967

at b = 0. With the lost fate and runs to t = 120, the critical termination is mc = 0.0112–0.0114 at every b:

1968

an unfinished copy then only removes a copying slot. A stop within the first Lcut nucleotides yields nothing,

1969

so that, per copying attempt, τ = 1 − (1 − m)L overstates the probability that the product kept is truncated

1970

by a factor close to L/(L − Lcut ) = 1.11 at every b, a nearly constant factor that cancels in D. The truncated

1971

share of the products actually made is another matter: since short products are made faster when b < 1, it

1972

differs from τ by a factor that depends on b, from 2.35 at b = 0 to 0.90 at b = 1 for small m. We read D on

1973

mc , the critical value of a termination probability m that the lattice and the protocells of Fig. 5A define in the

1974

same way, per nucleotide and per attempt, the timing then weighting each product by θ′ in both; the criteria

1975

that fix the threshold differ (SI S9). Read instead on the truncated share of the products made from replicase

1976

templates, the same function of m and b in both models, D(0.15) is 0.61 on the published lattice and 0.63 on

1977

the reimplemented one, and 0.08–0.17 in these protocells (n = 80 to 20): the contrast holds on either axis.

1978

Round-18.

1979

uct, varies about twentyfold with the position on the template, up to 0.9, and is 0.25 at the position where its

1980

rate constants were bounded 45 . A polymerase that releases its product at position i with probability 1 − Pi

1981

dissociates (1 − Pi )/Pi times there, on average, so that δ, the mean of (1 − Pi )/Pi along the template, is at

1982

least (1 − P̄)/P̄ for the mean P̄ (the function 1/P is convex), and b ≤ 1/[1 + L(1 − P̄)/P̄] (Methods). With

1983

Pi ≤ 0.9 everywhere, b ≤ 0.083 at L = 100; if P̄ were 0.25, b ≤ 0.0033.

1984

S11. QT45 and termination

1985

Table S6 gives the per-nucleotide fidelity a 45-nucleotide, 53.2-bit replicase with ℓ = 0.56 needs in protocells

1986

of n = 20 (θ = 1, R = ∞; 0.977 without termination), when copies stop at each nucleotide with probability m,

Its processivity coefficient P, the probability of adding a nucleotide before releasing the prod-

67


[page 68]
1987

products shorter than 10 nucleotides are lost, and longer ones are replicable truncated copies in two classes

1988

split at θ′ = 2 (θ′ reaches 4.5 at b = 0; the fast class disappears beyond b ≈ 0.36). Retruncation feeds the

1989

fast class from the slow one: at m = 3 × 10−3 it makes b = 0 impossible and b = 0.08 nearly so (99.92%);

1990

at b ≥ 0.5 it lowers the fidelity required slightly. The largest stop probability, 2.95 × 10−2 per nucleotide, is

1991

illustrative, of the order of the termination probability per incorporation reported for the tC9Y polymerase on

1992

favourable templates, 0.012–0.025 (ref. 46): a copy of 45 nucleotides then stops early three times out of four,

1993

and no fidelity suffices. QT45 copies with a per-nucleotide fidelity of 0.941. The row “1, with retruncation”

1994

is identity (iii) of SI S8: 1 − ε = 1 − [ln 2 − 35(− ln(1 − m))]/(ℓI), with 35 = 45 − 10, to the rounding shown,

1995

and no fidelity suffices for m ≥ 1 − 2−1/35 = 0.0196. By Theorem 2 with termination (SI S8), no row and no

1996

protocell size can require a lower fidelity.
Supplementary Table S6 | Per-nucleotide fidelity (%) required of a 45-nucleotide, 53.2-bit replicase with ℓ = 0.56
(n = 20, θ = 1, R = ∞; “—”: no fidelity suffices).
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

1997

S12. Proofs for the variants

1998

The four notes below give, in English, the proofs and derivations summarized in SI S2 (the lever) and S5

1999

(spontaneous replication, self-copying, protocell fusion). Each completes a note deposited with the code

2000

(S7), whose proofs were checked by an independent session. Status labels are those of S1. To keep one

2001

meaning per symbol in the manuscript, some symbols of the notes are renamed here, word for word: the

2002

fusion rate is k f , the self-copying scaling variable c/y is c̃ and its threshold λcis , and, in S12.1, (λ1 − y)/(1 − y)

2003

is ky ; in S12.4 the rescaled density k f x is x̃; the Extended Data figures keep κ and Λ.

2004

S12.1. The lever

2005

Scope and status.

2006

the ceiling of the compartment bonus. Status labels are those of the SI. Proved here: the lever in the limit

2007

process (Theorem L1), its form for equal daughters (Corollary L1′ ), the lever at every size and fecundity

2008

(Theorem L3), the exact identity at θ = 1 and R = ∞ (Proposition L7), and attainment by partial sorting at

2009

y = 0 (Theorem L5) and for small y (Theorem L6). Two reservations apply throughout. Dynkin’s formula

2010

for a piecewise-deterministic Markov process 24 , localized at the first passage to a large replicase number,

2011

is used without proof. Lemma H and the independence of the sign of ρ(S (M) ) − 1 from the admissible cut

2012

M (property C4′ ) are taken from the notes deposited with the code (S7), where they are proved and were

2013

checked by an independent session. The arguments below follow the deposited note, whose first version was

2014

checked by an independent session.

This note proves how far a division that is not blind to molecular identity can raise

68


[page 69]
The state is (F, u); between jumps u̇ = F − u; F → F + 1 at rate

2015

Limit process and division rules.

2016

λF(F − 1)/u, F → F − 1 at rate F, and F ≤ 1 is death; division occurs when u reaches 2y (SI S3). A division

2018

rule D gives a protocell that divides with f replicases a random number of daughters; daughter d receives Fd
P
replicases and a fraction αd ∈ (0, 1] of the molecules, d αd = 1, and starts from (Fd , 2yαd ). The joint law

2019

of the daughters may depend on f in any way, so that the rule may treat replicases and parasites differently.

2020

Write h(F) = F(F − 1), φa (F) = Γ(F − 1 + a)/Γ(F − 1), Z = h(F)u−2λ , and let KD ( f, f ′ ) be the mean number

2021

of daughters of a protocell of type f that reach division with f ′ replicases (types at division, as in SI S3).

2022

The lever factor is

2017

MD (λ) = sup

E

−2λ 
d h(F d ) αd

P

h( f )

f ≥2

λ∗ (D) = sup{λ ∈ (0, 1) : MD (λ) ≤ 1}.

∈ [0, ∞],

2023

Since αd ≤ 1, MD is non-decreasing, and as a supremum of continuous functions it is lower semicontinuous,

2024

so that {λ : MD (λ) ≤ 1} = (0, λ∗ ] when it is not empty. As in SI S3, λc (y; D) = inf{λ < 1 : ρ(S (M) ) > 1}, with

2025

S (M) the Schur reduction of KD onto the types {2, . . . , M} for a cut M beyond which large types drift down.

2026

Lemma A (proved).

2027

2F to h at rate λF(F − 1)/u, that is +2λFZ/u; deaths remove 2(F − 1) at rate F, that is −2Z; the death from

2028

F = 2 leads to the dead state, where Z = 0. The sum is −2(1 − λ)Z.

2029

Lemma B (one cycle from any starting size; proved). Let y > 0, λ ∈ (0, 1), and a daughter start from

2030

(F0 , u0 ) with F0 ≥ 2 and 0 < u0 < 2y; let τ be the time of division or death. Then τ < ∞ almost surely and

In living states, GZ = −2(1 − λ)Z. The flow contributes −2λZ(F − u)/u; births add

Z τ


E Z(Xτ )1{division} = Z(F0 , u0 ) − 2(1 − λ) E
Z(Xt ) dt.
0
2031

Proof. Let um = min(u0 , 2). Along a living path u ≥ um , since u̇ > 0 whenever u < 2 ≤ F. With

2032

V3 = φ3 (F)u−3λ one has GV3 = 3V3 (λ − F/(F + 1)), which is non-positive for F ≥ F ∗ = λ/(1 − λ) and at

2033

most (3λ − 2)V3 everywhere; on {F < F ∗ }, V3 /Z = (F + 1)u−λ ≤ (F ∗ + 1)u−λ
m . Hence W3 = V3 + C 3 Z, with

2034

C3 = (3λ−2)+ (F ∗ +1)u−λ
m /(2(1−λ)), satisfies GW3 ≤ 0 on the domain. Stopping at t∧τ∧T m , where T m is the

2035

first passage of F to m, Dynkin’s formula gives P(T m ≤ t ∧ τ) ≤ W3 (X0 )(2y)3λ /φ3 (m) → 0: the process does

2036

not explode. W3 (Xt∧τ ) is then a non-negative supermartingale, supt<τ F < ∞, and from any state of {2 ≤ F ≤

2037

m}×[um , 2y] the cycle ends within one time unit with probability bounded below, so that τ < ∞ almost surely.

2038
2039
2040
2041

As Z/V3 ≤ (2y)λ /(F + 1) before τ, Z ≤ εW3 + Cε for every ε > 0, and {Z(Xτ′ )}τ′ ≤τ , over stopping times τ′ ,
R t∧τ∧Tm
is uniformly integrable. Dynkin’s formula and Lemma A give E[Z(Xt∧τ∧Tm )] = Z0 − 2(1 − λ)E 0
Z dt;
letting m → ∞, then t → ∞, concludes, since Z = 0 at death. □
This is Lemma 1 of the note on (H3) deposited with the code, where u0 = y; only um changes.
At division Z = h( f ′ )(2y)−2λ , and at the start of daughter d, Z = h(Fd )(2yαd )−2λ .

2042

The loss formula.

2043

Applying Lemma B to each daughter given the outcome of the division, and taking expectations (all terms

2044

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

69

0

i
Z dt ≥ 0.


[page 70]
2045

Dead daughters contribute 0 = h(Fd ), and a daughter that receives the whole protocell (αd = 1) divides at

2046

once without loss. ℓD ( f ) > 0 as soon as, with positive probability, a daughter receives Fd ≥ 2 and αd < 1.

2047

At y = 0 (R → ∞, then n → ∞), F − 1 is a Yule process of rate λ in the time ln u, a daughter grows for a time

2048

ln(1/αd ), and h is an eigenfunction of the Yule generator with eigenvalue 2λ: the formula holds with ℓD = 0.

2049
2050
2051

Theorem L1 (the lever; proved). Let y ≥ 0, λ ∈ (0, 1), and MD (λ) ≤ 1. (a) KD h ≤ h, strictly at every
P
type where ℓD ( f ) > 0 or E[ d h(Fd )α−2λ
d ] < h( f ). (b) For every finite set A of types, with B the other types,
P k
P k
KBA has finite entries, and
the series k KBB KBA hA converges, the Schur reduction S (A) = KAA + KAB k KBB

2052

ρ(S (A) ) ≤ max f ∈A (KD h)( f )/h( f ) ≤ 1, strictly if (a) is strict on A; the same holds for every finite principal

2053

truncation of KD . (c) Let Xm be the sum of h over the protocells of the m-th generation that reach division.

2054

(Xm ) is a non-negative supermartingale with E[Xm ] ≤ MD (λ)m X0 . If MD (λ) < 1, or if MD (λ) = 1 and (a) is

2055
2056
2057

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

2058

converges. On A, S (A) hA ≤ KAA hA + KAB hB = (KD h)A ; each entry of S (A) is at most (S (A) hA )(i)/h( j) < ∞,

2059

and the Collatz–Wielandt inequality, valid for any finite non-negative matrix and positive vector without ir-

2061

reducibility, concludes. No drift of large types is used. (c) Given the first m generations, the cycles of the
P
daughters are independent, so that E[Xm+1 | Fm ] = i (KD h)( fi ) ≤ MD (λ)Xm . As h ≥ 2 on living types,

2062

P(Xm > 0) ≤ E[Xm ]/2 → 0 when MD < 1. When MD = 1, Xm takes even integer values and converges

2063

almost surely, hence is eventually constant. Given Xm = ξ > 0, generation m holds at most ξ/2 protocells

2064

with h( fi ) ≤ ξ, a finite set of configurations; for each, E[Xm+1 | ·] < ξ by (a), so that P(Xm+1 , ξ | ·) ≥ δξ > 0

2065

uniformly, and P(Xm = · · · = Xm+ j = ξ) ≤ (1 − δξ ) j . Hence Xm = 0 eventually, almost surely. (d) MD (λ) ≤ 1

2066

for every λ ≤ λ∗ , so that by (b) no such λ belongs to the set whose infimum defines λc . □

2060

2067
2068

2069
2070
2071
2072
2073
2074
2075

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
daughter d with probability αd given the fractions, has E[h(Fd ) | α] = α2d h( f ), hence MD (λ) = E[ d αd2−2λ ]
and λ∗ = 12 for every non-degenerate law of the fractions. Partial sorting, which sends all replicases to one
P
daughter with probability p and partitions at random otherwise, has E[ d h(Fd )] = r̄ h( f ) with r̄ = (1 + p)/2

2076

for every f , and λ∗ (p) = 12 log2 (2/(1 + p)). One bit more, a ceiling b ln 2 with b = log2 (1/λ∗ ), requires

2077

r̄ = 2−2 : 0.5, 0.7071, 0.8409, 0.9170 for b = 1 to 4.

2078

Theorem L3 (every size and fecundity; proved). In the finite model, let a division rule D, possibly

1−b

2079
2080

sensitive to molecular identity, give the daughters (Fd , Nd ). For b > 0 let gb (N) = Γ(N − 1)/Γ(N − 1 + b),
Q
V2,b = h(F)gb (N), ωb (N) = gb (N)/gb (2n) = 2n−2
j=N−1 (1 + b/ j) for N ≥ 2 and 0 otherwise, and
Gn (Λ; D) = max

E

P

d h(F d ) ω2Λ (Nd )

h( f )

2≤ f ≤2n

70


.


[page 71]
2081

If Λ ∈ (0, 1] and Gn (Λ; D) ≤ 1, then ρ(K) ≤ 1 for every R ∈ (0, ∞], θ > 0 and q ≤ 1 with max(q, q/θ) ≤ Λ.

2082

With λ∗n (D) the largest such Λ, Uc (n, R, θ; D) ≤ max(0, ln(1/θ)) + ln(1/λ∗n (D)).

2083

Proof. Let b = 2Λ. In a transient state, the copying term of the generator of V2,b is RF V2,b [2(N −

2084

1)p/(F − 1) − b]/(N − 1 + b), and losses contribute −(2 − b)V2,b for N ≥ 3 and −2V2,b at F = N = 2 (SI S2,

2085

“Supermartingales at every fecundity”). As W = (F − 1) + θ(N − F) ≥ min(1, θ)(N − 1), p ≤ max(q, q/θ)(F −

2086

1)/(N − 1) ≤ Λ(F − 1)/(N − 1), so that the copying term is non-positive; the losses are non-positive because

2087

Λ ≤ 1. At R = ∞ the mean change of V2,b at each copy is non-positive. The chain of a daughter is finite and

2088

absorbed almost surely, and V2,b is bounded, so that optional stopping gives gb (2n)E x [h( f ′ )1{division}] ≤

2089
2090
2091

V2,b (x); a daughter that receives all 2n molecules is already at division. Summing over daughters, (Kh)( f ) ≤
P
E[ d h(Fd )ωb (Nd )] ≤ Gn (Λ)h( f ) ≤ h( f ), and Collatz–Wielandt gives ρ(K) ≤ 1. Since ωb increases with b,
Gn is non-decreasing in Λ, and Λ ≤ λ∗n is equivalent to U ≥ ln(1/λ∗n ) + max(0, ln(1/θ)). □

2092

At Λ = 21 , ω1 (N) = (2n − 1)/(N − 1) and Gn ( 12 ; D) is the factor by which division multiplies the expected

2093

summed pair density ϕ = F(F − 1)/(N − 1): this is the bound for division blind to molecular identity (SI S2).

2094
2095

For binary binomial partition, Gn (Λ) = cn (Λ) and ln(1/λ∗n ) = un at θ = 1 (SI S2). With two daughters of
P
fixed size n, Gn (Λ) = g ω2Λ (n)/ω1 (n), where g = max f E[ d ϕd ]/ϕ, and λ∗n → 21 (1 − log2 g) as n → ∞. No

2096

function of g alone bounds the threshold when daughters differ in size: sorting all replicases into a daughter

2097

of 9 of 12 molecules has g = 1.375 and remains supercritical at every load computed at infinite fecundity

2098

(numerical).

2099

Proposition L7 (exact identity at θ = 1 and R = ∞; proved).

At θ = 1, p = q(F − 1)/(N − 1), so that the

2101

copying term above vanishes for b = 2q: V2,2q is a martingale during growth, there are no losses, and every
P
daughter with Fd ≥ 2 reaches division. Hence, for every rule, (Kh)( f ) = E[ d h(Fd )ω2q (Nd )] exactly, and

2102

ρ(K) ≤ Gn (q; D), with equality when this ratio does not depend on f , as for every rule blind to molecular

2103

identity. For the finite partial sorting (with probability p two daughters of n molecules, the first receiving

2104

min( f, n) replicases; binomial partition otherwise), (Kh)( f ) = [p ω2q (n)sn ( f )+(1− p)cn (q)]h( f ), with sn ( f ) =

2105

1 for f ≤ n and sn ( f ) = [h(n) + h( f − n)]/h( f ) < 1 beyond, so that Gn (q; p) = p ω2q (n) + (1 − p)cn (q); the

2106

exact kernels confirm the identity to 2 × 10−13 (numerical check).

2107

Theorem L5 (attainment at y = 0; proved). Let K0 be the kernel of partial sorting at y = 0 (partition,

2108

then F − 1 a Yule process of rate λ during ln 2), p ∈ [0, 1), r̄ = (1 + p)/2, Ψλ (a) = p 2λa + (1 − p) 21−a(1−λ)

2109

and λ3 (p) = 31 log2 (4/(1 + 3p)), the root of Ψλ (3) = 1. (a) K0 h = 4λ r̄ h for every λ. (b) For λ ∈ (0, λ3 (p))

2100

2110

the kernel has an admissible cut with weight φ3 , and for λ ∈ (λ∗ (p), λ3 (p)), ρ(S (M) ) ≥ 4λ r̄ > 1. (c) Hence

2111

λc (0; p) = λ∗ (p).

2112

Proof. (a) h(F) = ν(ν + 1) with ν = F − 1 is an eigenfunction of the Yule generator with eigenvalue

2113

2λ, and the partition keeps r̄ h( f ) in expectation. (b) Likewise φ3 = ν(ν + 1)(ν + 2) has eigenvalue 3λ;

2114

with φ3 = (F)3 + 3(F)2 and E[(B)i ] = ( f )i 2−i for B ∼ Bin( f, 12 ), binomial partition gives 2E[φ3 (B)] =

2115

f ( f − 1)( f + 4)/4, and sorting gives φ3 ( f ). Hence (K0 φ3 )( f ) = 23λ φ3 ( f )[p + (1 − p)( f + 4)/(4( f + 1))],

2116

whose ratio to φ3 ( f ) tends to Ψλ (3). At λ∗ , 23λ = r̄−3/2 and Ψλ∗ (3) = 41 (1 + 3p)r̄−3/2 < 1 if and only if

2117

2(1 + p)3 − (1 + 3p)2 = (1 − p)2 (1 + 2p) > 0, true for p < 1; Ψλ (3) increases with λ, so that λ∗ < λ3 , and

2118

for λ < λ3 there are β < 1 and M with K0 φ3 ≤ βφ3 beyond M, while K0 φ3 ≤ 23λ φ3 everywhere; φ3 ≥ h. For

2119

λ ∈ (λ∗ , λ3 ), K0 h = (1 + η)h with 1 + η = 4λ r̄ > 1, and Lemma H gives ρ(S (M) ) ≥ 1 + η. (c) follows with

2120

Theorem L1. □

∗

71


[page 72]
2121

The h-transformed chain, which follows the protocell carrying a marked pair, satisfies Eh [F ′ | F = f ] =

2122

2p
f
∗
λ
∗
2λ [ 1+p
( f + 1) + 1−p
1+p ( 2 + 2)] − 1; at λ its slope in f is Ψλ (3) < 1, so that it is positive recurrent and 4 r̄ is

2123

also the convergence parameter of K0 , as for random partition (SI S1) 42,43 .

2124

Theorem L6 (small fecundity cost; proved). For 0 < y < 1 and p ∈ [0, 1), let y3 (p) = (λ3 − λ∗ )/(1 − λ∗ ).

2126

If y < y3 (p), then λ∗ (p) ≤ λc (y; p) ≤ λ∗ (p) + y(1 − λ∗ (p)); in particular λc (y; p) → λ∗ (p) as y → 0. The
√
values of y3 are 1/3, 0.1143, 0.0377, 0.0126 and 0.0070 for p = 0, 0.2, 2 − 1, 0.6 and 23/4 − 1.

2127

Proof. The lower bound is Theorem L1. Let λ1 ∈ (λ∗ + y(1 − λ∗ ), λ3 ) and ky = (λ1 − y)/(1 − y).

2128

For y < 1, u increases along every living path and serves as a clock on [y, 2y], in which h has generator

2129

2h(λF − s)/(s(F − s)) ≥ (2ky /s)h for F ≥ 2 and s ≤ 2y; hence a daughter started at ( j, y) has E[h(F2y )] ≥

2130

22ky h( j), and (Kh)( f ) ≥ 4ky r̄ h( f ), with 4ky r̄ > 1 because ky > λ∗ . The function φ3 (F)u−3λ has generator

2131

3φ3 u−3λ (λ − F/(F + 1)) ≤ 0 for λ ≤ 23 , so that E[φ3 ( f ′ )1{division}] ≤ 23λ φ3 ( j) (Fatou), and the partition

2132

gives the drift of Theorem L5 with ratio tending to Ψλ1 (3) < 1. Lemma H then gives ρ(S (M) ) ≥ 4ky r̄ > 1, so

2133

that λc ≤ λ1 . □

2134

What is not proved.

2135

binomial partition; that λc (y; D) > λ∗ (D) strictly for y > 0; the upper bound of Theorem L6 beyond y3 (p);

2136

and, for partial sorting, the bound λc (y; p) ≤ λL (p) at every y from replicase-rich protocells, with λL (p) the

2137

root of inf a≥0 Ψλ (a) = 1 (derived from a branching random walk on ln F). Beyond λ3 (p) no admissible cut

2138

is proved for partial sorting; there λc should be read as inf{λ : supA ρ(K (A) ) > 1} over finite truncations, for

2139

which Theorem L1 holds unchanged.

2140

S12.2. Spontaneous replication

2141

Setting. We add to the model of the main text a copy made without a catalyst. Every molecule is copied

2142

spontaneously at rate s per lifetime; the copy of a replicase is a replicase with probability q s , and a parasite

2143

otherwise; the copy of a parasite is a parasite. We write χ = sq s for the number of correct uncatalysed copies

2144

of a replicase per lifetime. In a protocell with F replicases and Q parasites, N = F + Q and W = (F − 1) + θQ,

2145

the rates are: F → F + 1 at RFq(F − 1)/W + χF; Q → Q + 1 at RF[(1 − q)(F − 1) + θQ]/W + s(1 − q s )F + sQ;

2146

F → F − 1 at F and Q → Q − 1 at Q (catalysed copies vanish when W = 0). A protocell with one replicase

2147

is now alive; one with none is dead and is not counted. Division at 2n molecules is binomial, and the type of

2148

a protocell is its number f ∈ {1, . . . , 2n} of replicases at division. K is the mean matrix of living daughters,

2149

K = BH + 21−2n I as in the Methods, and Uc = sup{U : ρ(K) > 1}, with q = e−U and either q s = q or q s fixed;

2150

the sign of ρ − 1 is that of the Malthusian parameter 41 .

2151

Proposition 1 (no threshold when χ ≥ 1; proved, every size and fecundity).

2152

θ > 0 and q ∈ (0, 1], if χ ≥ 1 then ρ(K) > 1. Hence there is no threshold when q s is fixed and sq s ≥ 1, and

2153

Uc ≥ ln s when q s = q and s > 1.

2125

That the finite thresholds converge to max(0, ln(1/θ) + ψ(y; D)) for a rule other than

For every n ≥ 2, R ∈ (0, ∞),

2154

Proof. Let h(F) = F, with F = 0 at death. On transient states the generator of the chain within a protocell

2155

gives Gh = F(Rp + χ − 1), where p = q(F − 1)/W (p = 0 if W = 0) is the probability that a catalysed copy

2156

makes a replicase. For χ ≥ 1, Gh ≥ RF p ≥ 0, with strict inequality when F ≥ 2, since then W ≥ 1 and q > 0.

2157

Let τ be the time of division or death. The chain is finite and death is possible from every state, so τ < ∞

72


[page 73]
2158

almost surely and Eτ < ∞; Dynkin’s formula gives, from every transient state x,


E x F ′ 1{division} = F(x) + E x

Z τ
Gh dt ≥ F(x),
0

2159

where F ′ is the number of replicases at division. The inequality is strict if F(x) ≥ 2, because the chain stays

2160

a positive time in x. It is also strict if F(x) = 1: with χ > 0, the chain reaches a transient state with F = 2

2161

before τ with positive probability (from N = 2n − 1, a parasite may first die), which requires n ≥ 2. At

2162

division, the expected number of replicases summed over the daughters is f ; daughters without replicase

2163

count for 0, and the daughter that receives all molecules is at division at once with f replicases. For every

2164

f ≥ 1, a transient daughter with at least one replicase occurs with positive probability. Hence (Kh)( f ) > h( f )

2165

for f = 1, . . . , 2n. K is a finite non-negative matrix and h > 0, so the Collatz–Wielandt inequality gives

2166

ρ(K) ≥ min f (Kh)( f )/h( f ) > 1, without irreducibility. With q s = q, χ = se−U ≥ 1 for U ≤ ln s. □

2167

The limit process and the pair density (derived).

2168

u = N/R, the process of SI S3 becomes: u̇ = F − (1 − s)u; F → F + 1 at rate λF(F − 1)/u + χF,

2169

λ = q/θ; F → F − 1 at rate F; division at u = 2y. For Z = F(F − 1)u−2λ and F ≥ 2, the generator gives

2170

GZ = −2[1 − λ(1 − s)]Z + 2χZF/(F − 1), and GZ = 2χu−2λ > 0 = Z at F = 1. The pair density vanishes

2171

on a living type that feeds the others, so that the argument of the ceiling (Theorem 2; SI S2–S3) no longer

2172

applies.

2173

The reduced kernel at y → 0 (derived). As y → 0, the cycle of a protocell with F ≥ 2 lasts a time O(y),

2174

during which deaths and spontaneous copies have probability O(y); in the clock ln u, F − 1 is a Yule process

2175

of rate λ, which gives the limit kernel B∞ of Theorem 1. A lone replicase, in contrast, stays alone for an

2176

exponential time of rate 1 + χ, whatever y; its protocell keeps growing, at u̇ = 1 + O(y), and divides about

2177

1/[(1 + χ)y] times, the replicase passing to one daughter each time. It is revived, to two replicases, with

2178

probability ε = χ/(1 + χ), at a size u = y(1 + V) with V uniform on [0, 1]. Reducing the lone-replicase type

2179

(its weights per cycle are 1 − (1 + χ)τ1 for itself and χτ1 for revival, τ1 ≃ y) gives the kernel on types at

2180

division f ≥ 2

When n, R → ∞ at fixed y = n/R and fixed s, with

Kχ = B∞ + ε e ⊗ r,

e( f ) = 2 f 2− f ,

2181

where e( f ) is the mean number of daughters with one replicase, and r( f ′ ) = P(1 + ν(T ) = f ′ | ν(0) = 1)

2182

for a Yule process ν of rate λ run for T = ln[2/(1 + V)]; ν(T ) is geometric with parameter ((1 + V)/2)λ .

2183

The Schur reduction preserves the sign of ρ − 1 (SI S2). We write λc (0; χ) for the threshold of Kχ and

2184

ψ(0; χ) = − ln λc (0; χ). That λc (y; χ) → λc (0; χ) is numerical: the limit process converges linearly in y to the

2185

value of Kχ , not to that of a revived protocell treated as newborn.

2186

Lemma (subsolution).

2187

KAA + KAB (I − KBB )−1 KBA the Schur reduction. Suppose w > 0 satisfies KBB wB ≤ βwB with β < 1, and that

2188
2189
2190
2191

Let K ≥ 0 act on types f ≥ 2, A = {2, . . . , M}, B the larger types, and S =

v ≥ 0, non-zero on A, satisfies v ≤ w and Kv ≥ (1 + η)v with η > 0. Then ρ(S ) ≥ 1 + η.
P
Proof. Let t = 1/(1 + η), so that v ≤ tKv. On B, iterating m times, vB ≤ k<m (tKBB )k tKBA vA + (tKBB )m vB ,
and the last term is at most (tβ)m wB → 0. On A, vA ≤ tKAA vA + tKAB vB ≤ S (t)vA with S (t) = tKAA +
P
k+2 K K k K
AB BB BA ≤ tS . By Collatz–Wielandt, ρ(S (t)) ≥ 1, hence ρ(S ) ≥ 1/t = 1 + η. □
k≥0 t

73


[page 74]
2192

Proposition 2 (no threshold when χ ≥ 1; proved for the reduced kernel). For χ ≥ 1 and every λ ∈ (0, 1),

2193

ρ(S ) ≥ 1 + (2λ − 1)/4 for every admissible cut M.

2194
2195
2196

Proof. Let h1 ( f ) = f and S f ( j) = 2P(Bin( f, 21 ) = j). A daughter with j ≥ 2 replicases divides with

1 + ( j − 1)2λ replicases on average; a daughter with one replicase gives ε E[1 + ν(T )] ≥ 2ε ≥ 1, since ε ≥ 12 .
P
P
With j S f ( j) j = f and j≥2 S f ( j)( j − 1) = f − 2 + 21− f ,

(Kχ h1 )( f ) ≥ f + (2λ − 1)( f − 2 + 21− f ) ≥ 1 + (2λ − 1)/4 f,

f ≥ 2.

2197

For the drift, let φa ( f ) = Γ( f − 1 + a)/Γ( f − 1) with an integer a > 1/(1 − λ). It is an eigenfunction of the Yule

2198

generator in ν = f − 1 with eigenvalue aλ, and φa (0) = φa (1) = 0, so that B∞ φa ( f ) = 2 · 2aλ E[φa (Bin( f, 12 ))],

2199

whose ratio to φa ( f ) tends to 21−a(1−λ) < 1; the added term εe( f )⟨r, φa ⟩ = O( f 2− f ) is negligible. Hence

2200

w = Cφa , with C large enough that w ≥ h1 , satisfies the drift beyond some M, and the Lemma applies with

2201

v = h1 . □

2202

Proposition 3 (the ceiling is pierced at every χ > 0; proved for the reduced kernel).

2203

ρ0 = 22λ−1 , h( f ) = f ( f − 1) and

Let λ ∈ (0, 12 ),

D X
E
G(λ) = r,
Bm
∞e ,
m≥0
2204

the mean number of daughters with one replicase in the tree of B∞ alone (without revivals) issued from a

2205

revived protocell. Then: (a) G(λ) < ∞; Kχ is supercritical if εG(λ) > 1 and subcritical if εG(λ) < 1, so that

2206

at threshold χ = 1/(G(λ) − 1). (b) G(λ) → ∞ as λ ↑ 12 , and Kχ is supercritical at λ = 12 ; hence λc (0; χ) < 12

2207
2208

and ψ(0; χ) > ln 2 for every χ > 0. (c) G is continuous on [0, 21 ) with G(0) = 2; hence λc (0; χ) > 0 for χ < 1.
P m
m
Proof. (a) B∞ h = ρ0 h (SI S1) and e ≤ 1 ≤ h/2 on f ≥ 2, so Bm
∞ e ≤ ρ0 h/2, x := m B∞ e ≤ h/[2(1 − ρ0 )]

2209

and G ≤ ⟨r, h⟩/[2(1 − ρ0 )] < ∞. Supercriticality: for A = {2, . . . , M} let G M = ⟨rA , (I − B∞,A )−1 eA ⟩, which

2210

increases to G by monotone convergence; ρ(B∞,A ) ≤ ρ0 < 1 by Collatz–Wielandt. Since det(I − B∞,A −

2211

t eA rA⊤ ) = det(I − B∞,A )(1 − tG M ), the continuous function t 7→ ρ(B∞,A + t eA rA⊤ ), below 1 at t = 0 and

2212

unbounded, equals 1 only at t = 1/G M and exceeds 1 beyond. If εG > 1, take M with εG M > 1: the process

2213

restricted to types ≤ M is a finite supercritical branching process, and so is the full one. Subcriticality: let

2214

v = h + tx; since B∞ x = x − e and ⟨r, x⟩ = G,
Kχ v = ρ0 h + tx + e [ε⟨r, h⟩ − t(1 − εG)].

2215
2216
2217

If εG < 1 and t > ε⟨r, h⟩/(1 − εG), the bracket is negative; with x ≤ Ch, C = 1/[2(1 − ρ0 )], this gives
Kχ v ≤ βv for β = (ρ0 + tC)/(1 + tC) < 1, and the expected number of protocells decays geometrically.
P
42,43 ;
(b) At λ = 21 , ρ0 = 1 and the h-transformed chain is positive recurrent (SI S1), so m Bm
∞ (2, 2) = ∞

2218

as r(2) > 0 and e(2) = 1, G( 21 ) = ∞. Each entry of B∞ (λ)m is a sum over paths of non-negative weights

2219

continuous in λ, so Fatou’s lemma gives lim inf λ↑1/2 G(λ) = ∞, and (a) applies near 12 . At λ = 12 itself, all

2220

entries of B∞ are positive, so ρ(B∞,A ) < 1 and G M < ∞ for every M, while G M → ∞. (c) For λ ≤ λ1 < 21 ,

2221

m
⟨rλ , Bm
∞ e⟩ ≤ 2ρ0 (λ1 ) , since ⟨rλ , h⟩ ≤ 4, and dominated convergence gives continuity. At λ = 0 there are no

2222

catalysed births: a revived protocell divides with two replicases, and a division with two replicases gives on

2224

average one daughter with one replicase and half a daughter with two, which divides again with two; hence
P
G(0) = m 2−m = 2, and εG(0) = 2χ/(1 + χ) < 1 for χ < 1. □

2225

That G increases with λ, so that the threshold is unique, is numerical (checked on a grid of 499 points).

2223

74


[page 75]
2226

2227
2228
2229

Proposition 3(b) does not need it: a supercritical λ < 21 suffices for Uc > ln 2.
√
f
First order (derived). At λ = 12 the left eigenvector of B∞ is π0 ( f ) = r0 , r0 = 2 − 2 (SI S1), and
√
√
⟨π0 , e⟩ = 2 − 2, ⟨π0 , h⟩ = 4 + 4 2, ⟨r, h⟩ = 2 E[2/(1 + V)] = 4 ln 2. The rank-one perturbation ε e ⊗ r moves
√
the simple eigenvalue 1 by ε⟨π0 , e⟩⟨r, h⟩/⟨π0 , h⟩ = ε(3 2 − 4) ln 2, and ∂ρ0 /∂λ = 2 ln 2, so that
√
ψ(0; χ) = ln 2 + (3 2 − 4) χ + O(χ2 ).

2232

√
What is missing for a proof is the limit (1 − ρ0 ) G(λ) → (3 2 − 4) ln 2 as λ ↑ 21 , supported numerically
√
(0.16850 at λ = 0.4999, against 0.16819). The slope in y is −(3 2 − 4)/ ln 2 (SI S3), so that to first order
√
ψ ≈ ln 2 + (3 2 − 4)(χ − y/ ln 2).

2233

The model of Bianconi et al. 15 : χeff = q (derived).

2234

at rate 1 + (i − 1)α and every other sequence at rate 1 + iα; sequences are not degraded, and a replicase is

2235

selected if cells that contain replicases outgrow parasite-only cells, whose sequences replicate at rate 1. We

2236

compute this criterion as the spectral radius of the kernel discounted at the Malthusian rate 1, which acts as

2237

a removal rate w = 1 on every cell. A cell with a lone replicase keeps growing, since its parasites are copied

2238

at rate 1 + α, and passes the replicase to one daughter at each division; the replicase is copied correctly at

2239

rate q and the lineage is removed at rate w = 1. It is therefore revived with probability q/(1 + q): in our

2240

units, χeff = q. Two differences remain. Catalysis by mass action makes the cell with a lone replicase grow

2230
2231

In R2α, a replicase in a cell with i replicases replicates

2242

exponentially, so that revival occurs at a stage uniform in ln N; we write ψlog for the limit of the corresponding
√
reduced kernel, in which T is uniform on [0, ln 2], with slope (3 2 − 4)/(2 ln2 2). At α → ∞ the jump chain

2243

of a cell with i ≥ 2 replicases is ours, so that for α → ∞ and m → ∞ with α ≪ 2m the threshold is the root of

2244

U = ψlog (0; e−U ), U ∗ = 0.903 (derived; the root is computed on the reduced kernel). The condition α ≪ 2m

2245

excludes the singular regime in which a lone replicase, left alone in a daughter of one molecule, waits there

2246

and refounds cells made of replicases only.

2247

S12.3. Self-copying, total or partial

2248

Model.

2249

chooses its template among the N molecules with weight c ≥ 0 for itself, 1 for each of the F − 1 other

2250

replicases and θ for each parasite; a copy of a replicase template is a replicase with probability q = e−U . The

2251

next molecule made is therefore a replicase with probability

2241

A protocell holds F replicases among N molecules. Each replicase starts copies at rate R and

pc (F, N) =

q (F − 1 + c)
≤ q.
(F − 1 + c) + θ(N − F)

2252

Molecules decay at rate 1, protocells divide at 2n molecules by binomial partition, and F = 0 is dead; F = 1

2253

is alive when c > 0. The case c = 0 is the model of the main text, c = 1 the self-copying variant of SI S1.

2254

In the limit process (n, R → ∞ at fixed y = n/R, u = N/R), u̇ = F − u, F → F + 1 at rate λF(F − 1 + c)/u

2255

with λ = q/θ, F → F − 1 at rate F, and division occurs at u = 2y into two daughters at u = y with Bin(F, 12 )

2256

replicases. For a function g(F, u) vanishing at F = 0 its generator is
Gg = (F − u) ∂u g +

λF(F − 1 + c)
[g(F + 1) − g(F)] + F [g(F − 1) − g(F)].
u

75


[page 76]
2257

K denotes a mean matrix of living daughters, ρ its spectral radius, and λc (y; c), ψ(y; c) = − ln λc are defined

2258

from the Schur reduction of the limit kernel onto small types, as in SI S3. We write ℓy = ln[(1 − y)/(1 − 2y)]

2259

for y < 12 .

2260

A. No threshold at infinite fecundity (proved). Let n ≥ 1, θ > 0, c > 0 and 0 < q < 1. At R = ∞ nothing

2261

decays, so F never decreases during growth, and a daughter that receives at least one replicase reaches

2262

division alive. The row sums of K (types at division f = 1, . . . , 2n) are therefore 2(1 − 2− f ): one for f = 1

2263

and at least 32 for f ≥ 2. K is irreducible: from any f , a daughter receives a single molecule, a replicase,

2264

with probability f 2−2n > 0, and from (F, N) = (1, 1) successful copies (pc > 0) and failed ones (pc < 1)

2265

lead to division at any type f ′ ∈ {1, . . . , 2n}. The spectral radius of an irreducible non-negative matrix lies

2266

strictly between its smallest and largest row sums unless they are all equal 43 , so ρ > 1 at every load, and

2267

Uc (n, ∞, θ; c) = +∞. At c = 0, by contrast, Uc stays below max(0, ln(1/θ)) + ln 2 at every size and fecundity:

2268

the limits R → ∞ and c → 0 do not commute. At finite fecundity the threshold is finite, Uc ≤ ln R, since

2269

new replicases appear at rate RF pc ≤ RFq while replicases decay at rate F.

2270

A′ . An exact eigenvector (proved).

2271

copy gives E[V ′ ] = F(1+q/N) Γ(N +1)/Γ(N +1+q) = V, so V is a martingale over the fixed number of copies

2272

that bring a daughter to 2n molecules, and a daughter (Fd , Nd ) divides with E[ f ′ ] = V(Fd , Nd ) Γ(2n+q)/Γ(2n).

2273

Given Nd , Fd is hypergeometric with E[Fd | Nd ] = f Nd /(2n); empty daughters count zero and the daughter

2274

that receives everything is already at division. Hence KF = ρn (q)F with
ρn (q) =

At R = ∞, θ = 1 and c = 1, p = qF/N. For V = F Γ(N)/Γ(N + q) one

Γ(N1 + 1) i
Γ(2n + q) h
E 1{N1 ≥ 1}
,
n Γ(2n)
Γ(N1 + q)

N1 ∼ Bin(2n, 12 ),

2275

and, F being a positive eigenvector of an irreducible matrix, ρ = ρn (q). Since Γ(2n + q)/Γ(2n) ∼ (2n)q ,

2276

Γ(N + 1)/Γ(N + q) ≤ CN 1−q and N1 /n → 1, dominated convergence gives ρn (q) → 2q , the eigenvalue of

2277

SI S1 at θ = 1. At U = 10, ρn − 1 = 3.126 × 10−5 for n = 3 and 3.147 × 10−5 for n ≥ 10.

2278

B. First-order identity (proved). For Vb = F u−b (zero at F = 0), a birth adds u−b , a death removes it,

2279

including the death of a lone replicase, and the flow contributes −bFVb /u + bVb ; hence, for every F ≥ 1,
GVb = Vb

h λ(F − 1 + c) − bF
u

i
+b−1 .

2280

With b = λc, GV = V[λ(1 − c)(F − 1)/u − (1 − λc)]: a lone replicase decays at exactly the rate 1 − λc, and

2281

for c ≤ 1 trans copying only adds. With c = 1 and b = λ, Z1 = Fu−λ satisfies GZ1 = −(1 − λ)Z1 in every

2282

state, and since partition conserves F while u returns from 2y to y, a division multiplies Z1 , summed over

2283

daughters, by exactly 2λ . This is the exact analogue of the pair density of SI S3, whose factors 2(1 − λ) and

2284

22λ−1 become 1 − λ and 2λ .

2285

C. Second-order identity (proved). Let g(F) = (F + c − 1)(F + c) and Zc = g(F)u−2λ for F ≥ 1, Zc = 0

2286

at F = 0. A birth adds 2(F + c)u−2λ , at rate λF(F − 1 + c)/u, which cancels the term −2λFZc /u of the flow;

2287

a death removes 2(F + c − 1)u−2λ if F ≥ 2, and all of Zc if F = 1. Hence
h
2F i
GZc = Zc 2λ −
F+c

(F ≥ 2),

76

GZc = (2λ − 1)Zc

(F = 1).


[page 77]
2288

For a quadratic g = F 2 + αF + β, the terms in 1/u are λF[(2c − 1 − α)F + (c − 1)(1 + α) − 2β]u−2λ−1 ,

2289

which vanish identically only for α = 2c − 1, β = c(c − 1): g is unique. Partition does not close it: for

2290

B ∼ Bin( f, 12 ), 2E[g(B); B ≥ 1] = f ( f − 1)/2 + 2c f + 2c(c − 1)(1 − 2− f ), so that 2E[g(B); B ≥ 1] − g( f )/2 =

2291

c[ f + (c − 1)( 23 − 21− f )] > 0 for c > 0 and f ≥ 1; the partition factor lies in ( 12 , 1] and equals 1 at f = 1. At

2292

c = 0 it is 21 and the identity of SI S3 is recovered.

2293

Lemma D. Drift of large types for y < 12 (proved).

2294

λ)), φ(F) = Γ(F − 1 + c + a)/Γ(F − 1 + c) for F ≥ 1 (a polynomial of degree a with leading coefficient

2295

1) and w = φ + 1. Then for every β ∈ (21−a(1−λ) , 1) there are M and C with Kw ≤ βw beyond M and

2296

Kw ≤ Cw everywhere. Indeed V = φ(F)u−λa satisfies GV = V[λa − h(F)] with h(F) = aF/(F − 2 + c + a)

2297

for F ≥ 2 and h(1) = 1; h increases to a > λa, so GV ≤ γV 1{F < F ∗ } with γ ≤ λa. Along a living

2298

lineage u̇ ≥ 1 − u > 0, so u ∈ [y, 2y] and a cycle ends within ℓy ; in the clock s = u births are at most

2299

linear in F, so all moments are finite. Dynkin’s formula for this piecewise-deterministic process 24 gives

2300

E[φ( f )1{div}] ≤ 2λa [φ(F0 ) + C0 PF0 (min F < F ∗ )], and the replicases present at birth that survive until ℓy

2301

remain present throughout, so the last probability is at most P(Bin(F0 , e−ℓy ) < F ∗ ), exponentially small in

2302

F0 . Factorial moments give E[φ(B); B ≥ 1] = 2−a f a + O( f a−1 ), hence (Kφ)( f )/φ( f ) → 21−a(1−λ) < 1, and

2303

K1 ≤ 2. With this drift, λc (y; c) is defined and the sign of ρ − 1 for the Schur reduction does not depend on

2304

the admissible cut.

2305

Two tools. (H) If Kw ≤ βw on the large types B with w ≥ 1, β < 1, and Kv ≥ γv for some v ≥ 0, v ≤ Cw,

Let y < 12 , c > 0, λ < 1, an integer a > max(2, 1/(1 −

2307

non-zero on the small types A, with γ > 1, then the Schur reduction S onto A has ρ(S ) ≥ γ: with t = 1/γ,
P
iterating v ≤ tKv on B gives vB ≤ k (tKBB )k tKBA vA , so vA ≤ S (t)vA ≤ tS (1)vA , and the Collatz–Wielandt

2308

inequality 43 concludes. Conversely, if h > 0 and Kh ≤ h, then ρ ≤ 1 for every finite truncation and every

2309

Schur reduction that exists.

2310

B1. A lone replicase must replace itself (proved for y < 21 ). Let y < 12 and 0 < c ≤ 1. By B, V = Fu−λc

2311

satisfies GV ≥ −(1 − λc)V, so e(1−λc)t V is a submartingale, zero at death. Cycles last at most ℓy and moments

2312

are finite (Lemma D), hence E[V(τ)1{div}] ≥ e−(1−λc)ℓy V(0). With V = f (2y)−λc at division, V = Fb y−λc at

2313

birth and partition conserving F, KF ≥ γ1 F with γ1 = 2λc e−(1−λc)ℓy . By (H) with v = F ≤ w, ρ > 1 as soon

2314

as λc(ln 2 + ℓy ) > ℓy :

2306

λc (y; c) ≤

ℓy
.
c(ln 2 + ℓy )

2315

Rℓ
Since 0 y dt/u(t) = ln 2 + ℓy along the path of a lone replicase, the condition says that its expected number of

2316

successful copies of itself over a cycle exceeds its cumulated death intensity. For c > 1, V = Fu−λ satisfies

2317

GV/V ≥ λ(c−1)/(2y)+λ−1, and the same argument applies. For every c ≥ 0, the proof of the bound (1+y)/2

2318

of SI S3 carries over, cis copies only adding births and F(F − 1) vanishing at F = 1: λc (y; c) ≤ (1 + y)/2.

2319

B2. A supersolution (proved; for y ≥ 21 , for every truncation and every Schur reduction that exists).

2320

Let y > 0, c > 0, um = min(y, 1), λ < 21 with a = λ(1 + c) < 12 , b = 2 − 4a, and β ≥ 0 such that (i)

2321

λc(um + 2βy) ≤ u2m , (ii) β(3 − 6λ − 2λc + 2y) ≥ 2λ, and (iii) β ≥ maxu∈[um ,2y] u(a − u)/[y(b + u)]. For

2322

H = F + βyF(F − 1)/u, a direct computation gives
u
βy
GH = q(F, u) = λ(F − 1 + c) − u +
[2λF(F − 1 + c) − F(F − 1)] − βy(F − 1).
F
u
77


[page 78]
2323

Here q(1, u) = λc(1 + 2βy/u) − u ≤ 0 on [um , 2y] by (i); the coefficient of F 2 in uq is βy(2λ − 1) < 0, so q is

2324

concave in F, and with B = βy/u, ∂F q(2, u) = λ−B(3+u−6λ−2λc) ≤ 0 by (ii) and q(2, u) = a−u−B(b+u) ≤ 0

2326

by (iii). A living lineage stays in {F ≥ 1, um ≤ u ≤ 2y}, where GH ≤ 0; H ≥ F excludes explosion, the
P
cycle ends almost surely, and Fatou’s lemma gives E[H(Xτ )1{div}] ≤ H(Fb , y). Since E[ d H(Fd , y)] =

2327

f + β f ( f − 1)/2 = H( f, 2y), the kernel on types at birth satisfies Kh ≤ h for h = F + βF(F − 1) (on types at

2328

division, h = f + β2 f ( f − 1)), so ρ ≤ 1. The conditions are monotone in λ, hence λc (y; c) ≥ λ∗ (y, c), the largest

2329

admissible λ. Condition (i) gives λ∗ ≤ y/c, and the smallest β allowed by (ii) and (iii) is O(λ + λ2 (1 + c)2 /y),

2330

so λ∗ = (y/c)[1−O(y(1+c)2 /c2 )]. For y ≥ 12 no drift is proved, so λc is defined there only through truncations,

2331

on which the bound holds.

2332

F. No threshold at high fecundity (proved). For fixed 0 < c ≤ 1, B1 and B2 give, as y → 0,

2325

ln

 y(1 + c)2 
c ln 2  1
3
c
+
− y + O(y2 ) ≤ ψ(y; c) ≤ ln + O
,
y
ln 2 2
y
c2

2333

using ℓy = y + 32 y2 + O(y3 ): ψ → ∞, logarithmically. The constants diverge as c → 0, which is again the

2334

non-commutation of the limits.

2335

What is not proved. The scaling λc (y; c̃y) → λcis (c̃), with λc̃ ln 2 [G(λ) − 1] = 1, is derived to first order in

2336

y, its remainders being uncontrolled near λ = 21 ; the closed form λcis ≈ 1/[1 + (1 + c̃2 ln2 2)1/2 ] is a numerical

2337

approximation; for y < 12 , hypothesis (H2) and the decrease of λc in c follow from the size-clock coupling

2338

of SI S3 but are not written out; for y ≥ 12 the drift is not proved; and for c > 0 the convergence of the finite

2339

thresholds Uc (n, n/y, θ) to max(0, ln(1/θ) + ψ(y; c)) is only numerical, as 1/n at most values of y for θ ≥ 1

2340

but more slowly at y = 12 , at y = 1 for c = 1, and for θ < 1.

2341

S12.4. Protocell fusion

2342

Scope. The thresholds of the main text are invasion thresholds, for protocells that neither fuse nor compete.

2343

Here protocells fuse. Fusion between protocells leaves Uc unchanged; no fusion raises it above the ceiling,

2344

and fusion with vesicles that carry parasites can lower it. Fusion can at most let an already dense population

2345

persist beyond Uc , which in our computations required a rule that sees content.

2346

Population model. A protocell is (F, N): it holds 1 ≤ N ≤ 2n − 1 molecules, of which 0 ≤ F ≤ N are

2348

replicases. Protocells with F = 0 (parasites only) and F = 1 (a lone replicase, which copies only parasites)
P
are followed, with densities xF,N (t) and total density X = xF,N . The rules are the following.

2349

• Within a protocell, the transitions are those of the main text at finite fecundity. Copies occur at rate RF

2350

when N ≥ 2, and the product is a replicase with probability p(F, N) of Eq. 1 (p = 0 at F = 1). Each

2351

molecule decays at rate one, and a protocell that reaches N = 0 disappears.

2347

2352

• Partition. A protocell with N ≥ 2n molecules is cut in two, each molecule going to either piece with

2353

probability 21 independently. An empty piece disappears, and a piece of 2n molecules or more is cut

2354

again, until every piece holds fewer than 2n molecules. We write T (F, N) for the expected numbers of

2355

pieces in each state.

78


[page 79]
2356
2357

2358

2359

• Fusion. Two protocells meet and fuse at rate k f per pair (mass action), giving (F1 + F2 , N1 + N2 ), which
is partitioned at once if N1 + N2 ≥ 2n.
• Regulation. Each protocell is removed at rate µX.
Hence
ẋ = Lx + k f Fus(x, x) − µXx,

2360

where (x ∗ x)F,N =

P

Fus(x, x) = 12 T (x ∗ x) − Xx,

F1 +F2 =F, N1 +N2 =N xF1 ,N1 xF2 ,N2 and L is the linear part. With x̃ = k f x, only k f /µ matters.

2361

Two variants are considered.

2362

• A fixed background of vesicles without replicases, at density Xb , each carrying m ≥ 0 parasites. A

2363

protocell fuses with it at rate β = k f Xb , so that L becomes Lβ = L + β(T m − I), where T m adds m

2364

parasites and partitions if needed. The regulation does not count the background, which is a fixed

2365

reservoir; if it did, Lβ would receive −µXb I, which only lowers growth rates.

2366
2367

• A rule that sees content: only protocells with F ≥ 1 fuse. Under this rule a background vesicle cannot
fuse with anything, and the background is neutral.

2368

Lemma 1 (repeated partition; proved).

2369

the composition of a piece of m molecules is hypergeometric. (b) At N = 2n, T ( f, 2n) = B( f, ·)/(1 − 21−2n ),

(a) The partition is exchangeable: given the sizes of the pieces,

2371

where B is the partition matrix of the Methods. (c) For the pair density V(F, N) = F(F − 1)/(N − 1) (V = 0
P
if F ≤ 1), E pieces V ≤ V(F, N) for every N ≥ 2n.

2372

Proof. (a) Each cut treats molecules independently of their type, and the decision to cut again depends

2373

only on sizes; the law of the assignment of labelled molecules is therefore invariant under their permutations.

2374

(b) A trivial cut, of probability 21−2n , returns the initial state and an empty piece: T = B + 21−2n T . (c)

2370

2376

By (a), a piece of m ≥ 2 molecules has E[Fd (Fd − 1) | m] = F(F − 1) m(m − 1)/(N(N − 1)), hence
P
E[Vd | m] = V(F, N) m/N. Pieces of one molecule have Vd = 0, and md = N.
□

2377

Lemma 2 (sign of a growth rate; proved).

2375

Let V be a nonsingular M-matrix and A ≥ 0, with A − V

2379

irreducible. Then s(A − V), the largest real part of the eigenvalues of A − V, has the sign of ρ(AV −1 ) − 1.
P
Proof. If ρ(AV −1 ) < 1, then (V − A)−1 = V −1 k≥0 (AV −1 )k ≥ 0. The Z-matrix V − A is then a nonsingular

2380

M-matrix, so s(A − V) < 0 43 .

2378

2381

Conversely, let s(A − V) < 0, so that (V − A)−1 =

R∞
0

e(A−V)t dt ≥ 0. Let ρ = ρ(AV −1 ), let y ≥ 0,

2382

y , 0, satisfy AV −1 y = ρy, and put x = V −1 y, so that x ≥ 0 and x , 0. Then (V − A)x = (1 − ρ)y, so

2383

x = (1 − ρ)(V − A)−1 y, which is compatible with x ≥ 0, x , 0 only if ρ < 1.

2384

For the remaining cases, replace A by tA. Then ρ(tAV −1 ) = tρ, and s(tA − V) is continuous and, for

2385

irreducible A − V, strictly increasing in t 43 ; this gives the cases = 0 and > 0.

2386

Theorem 1 (fusion between protocells does not move the invasion threshold; proved).

2387

R < ∞, θ > 0, k f , µ ≥ 0, and any rule of fusion between two protocells, blind or not, starting from a

2388

world without vesicles. Let L22 be the block of L on living states (F ≥ 2). Then the number of replicases

2389

of a rare population grows if and only if r(U) := s(L22 ) > 0, and r(U) has the sign of ρ(K) − 1, where

2390

K is the mean matrix of the main text. The invasion threshold is therefore Uc (n, R, θ), under the ceiling

2391

ln 2 + max(0, ln(1/θ)), whatever k f , µ and the fusion rule.

2392

Proof.
79

□
Take any n ≥ 2,


[page 80]
2393
2394

1. Fus(x, x) and Xx are homogeneous of degree two: two rare protocells meet at a rate proportional to the
square of their density. The linearization at x = 0 is therefore L.

2395

2. No linear transition leads from F ≤ 1 to F ≥ 2: a copy at F = 1 yields a parasite, decay lowers F, and

2396

partition conserves the number of replicases. L is thus block-triangular: the block L11 (F ≤ 1) is fed

2397

by L22 , and not conversely.

2398

3. Order L11 as (F = 1, F = 0).

2399

• The F = 0 block is triangular, with diagonal −1, . . . , −(2n − 1).

2400

• In the F = 1 block, each column sums to −1. Copying and the decay of a parasite keep the lone

2401

replicase in exactly one piece, and its own decay removes it at rate one. The positive vector 1 is

2402

thus a left eigenvector of this Metzler matrix for −1, so its spectral bound is −1 43 .

2403

• Hence s(L11 ) = −1.

2404

4. L22 is irreducible for 0 < q < 1: every living state leads to (2, 2) by decays, and (2, 2) leads to every

2405

living state by copies. Write L22 = A − V, where A ≥ 0 collects division (growth jumps that reach 2n,

2406

distributed by T on living states) and −V the rest.

2407
2408

• V is a nonsingular M-matrix: the chain within a living protocell leaves the living states of size
below 2n, by division or by the decay that brings F to one, with probability one.

2409

• AV −1 maps a protocell to the expected living pieces of its first division. Its nonzero eigenvalues

2410

are those of Kc = T c H, with H the probabilities of reaching division with f ′ replicases (Methods)

2411

and T c = T (·, 2n) restricted to living states.

2412
2413

2414

• By Lemma 1(b), Kc = BH/(1 − 21−2n ), whereas K = BH + 21−2n I. Hence ρ(K) = ρ(BH) + 21−2n ,
and ρ(Kc ) − 1 = (ρ(K) − 1)/(1 − 21−2n ).
Lemma 2 then gives the sign of s(L22 ).

2415

5. Replicases live in the blocks F ≥ 2 and F = 1. The latter is fed only by the former, and loses its

2416

replicases at rate one. If s(L22 ) > 0 the number of replicases grows; if s(L22 ) < 0, it decays at rate

2417

max(s(L22 ), −1).

2418

□

Numerically, Uc computed from r(U) = 0 and from ρ(K) = 1 agree to within 1.7 × 10−11 for n = 5, 10

2419

and 20 and R = 10, 25 and 100 (θ = 1).

2420

Proposition 2 (background of vesicles without replicases; proved). (a) If the background vesicles are

2421

empty (m = 0), then T 0 = I and Lβ = L: fusion with them is neutral, size being counted in molecules. (b)

2422

For m ≥ 1, Lβ is still block-triangular, and its living block satisfies
s(Lβ,22 ) ≤ max{−1, R(2Λ − 1) − 1},

2423
2424

Λ = max(q, q/θ),

so that s(Lβ,22 ) < 0 as soon as U > ln(2R/(R + 1)) + max(0, ln(1/θ)), a load below the ceiling.
P
Proof of (b). Let Gβ V(s) = s′ Lβ,22 (s′ , s) V(s′ ). We bound each contribution.

80


[page 81]
2425

• Copying, for N ≥ 3, contributes RF[p(F + 1)F/N + (1 − p)F(F − 1)/N − V] = V (RF/N) [2p(N −

2426

1)/(F − 1) − 1]. Here p(N − 1)/(F − 1) = q(N − 1)/[(F − 1) + θ(N − F)] ≤ Λ: the denominator is at

2427

least N − 1 if θ ≥ 1, and at least θ(N − 1) if θ ≤ 1.

2428

• Decay contributes [F(F − 1)(F − 2) + (N − F)F(F − 1)]/(N − 2) − NV = −V.

2429

• At (2, 2), copying contributes VR(2q − 1) and decay −2V.

2430

• Division replaces V(F ′ , 2n) by E

2431

• Fusion with the background contributes β[E

2432

P

V ≤ V(F ′ , 2n) (Lemma 1(c)).
P

V(pieces of (F, N + m)) − V(F, N)] ≤ β[V(F, N + m) −

V(F, N)] ≤ 0: it only dilutes pairs.

2433

Hence Gβ V ≤ V [R(2Λ − 1)F/N − 1], and, since F ≤ N, Gβ V ≤ max{−1, R(2Λ − 1) − 1} V. As V > 0 on

2434

living states and Lβ,22 is a Metzler matrix, the Collatz–Wielandt inequality, applied to Lβ,22 + aI ≥ 0 for a

2435

large enough constant a, gives the bound 43 .

□

2436

At β = 0, this is the bound at every fecundity of SI S3.

2437

Which state is invaded. s(Lβ,22 ) is the invasion criterion only if x = 0 is the state without replicases of

2438

the full model, that is, if the block of Lβ on F = 0 (independent of R and U) is stable. Otherwise, vesicles

2439

without replicases shed by the invaders proliferate on the background. The state without replicases is then

2440

a resident population on F = 0, whose density depends on k f /µ, and an invader meets it at first order. The

2441

bound still holds there (Corollary 3).

2442

Corollary 3 (no fusion raises the invasion threshold above the ceiling; proved). Let x0∗ be any stationary

2443

population without replicases (no vesicles, or a resident population on F = 0, with or without background),

2444

invaded by a rare replicase, with a blind partition after every fusion. Linearizing at x0∗ , the living block is
J22 = L22 + k f

X

x0∗ (0, m′ ) (T m′ − I)22 + β (T m − I)22 − µX0∗ I.

m′
2445

An invader meets residents and background at first order, and is removed by the regulation they exert; fusion

2446

between invaders is of second order. J is again block-triangular: a resident brings no replicase, and the fusion

2447

of an F = 1 protocell with a resident keeps a single replicase.

2448
2449
2450
2451

Every fusion with a partner without replicases satisfies V(F, N + m′ ) ≤ V(F, N) after partition
(Lemma 1(c)), and −µX0∗ V ≤ 0. The proof of Proposition 2(b) then gives s(J22 ) ≤ max{−1, R(2Λ − 1) − 1}.
Hence no fusion, between protocells or with vesicles without replicases, raises the invasion threshold
above max{0, ln(2R/(R + 1)) + max(0, ln(1/θ))} < ln 2 + max(0, ln(1/θ)).

□

2452

Two cases are outside the statement. A partner that carries replicases is a source of replicases, not a case

2453

of invasion. A partition that sorts molecules after fusion falls under SI S2: only a partition that raises the pair

2454

density can exceed the ceiling.

2455

Proposition 4 (no population keeps a replicase beyond U = ln R; proved). Take any fusion rule, blind

2457

or not, any regulation, any background and any initial state. If Rq < 1, the total density of replicases
P
Φ = s F s x s decays at least as e−(1−Rq)t . In particular, no stationary population with replicases exists for

2458

U > ln R.

2456

81


[page 82]
2459

Proof. Fusion and partition conserve replicases, and regulation and background create none. Copies

2460

create replicases at rate RF p(F, N) ≤ RFq, and decay destroys them at rate F. Hence dΦ/dt ≤ (Rq−1)Φ. □

2461

This is the Replacement argument of SI S3, which holds unchanged with fusion.

2463

Normal form at the invasion threshold (derived). Let r(U) = s(L22 ) be simple. Let v > 0 be its right
P
Perron vector, normalized over all protocells ( v = 1, F ≤ 1 included, with v11 = (rI − L11 )−1 L12 v22 ).

2464

Let w ≥ 0 be its left Perron vector; w is carried by F ≥ 2, because r > −1 = s(L11 ). With x̃ = k f x and

2465

Q( x̃, x̃) = Fus( x̃, x̃) − (µ/k f )X̃ x̃, an equilibrium near (Uc , 0) is x̃∗ = εv + O(ε2 ). Projecting 0 = L x̃∗ + Q( x̃∗ , x̃∗ )

2466

on w gives 0 = rε⟨w, v⟩ + ε2 ⟨w, Q(v, v)⟩ + O(ε3 ), hence

2462

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

2467

with ∆(s1 , s2 ) = w(pieces of s1 ⊕ s2 ) − w(s1 ) − w(s2 ). Thus B f > 0 if and only if a fusion between two proto-

2468

cells drawn from the invading population creates reproductive value on average. The equilibrium density of

2469

protocells is (ε/k f )v.

2470

The eigenvalue along the branch is r + 2εB = −r, and r′ (Uc ) < 0.

2471

• If B < 0, the branch exists for U < Uc and is stable (supercritical).

2472

• If B > 0, it exists for U > Uc and is unstable (subcritical). A dense population can then coexist with

2473

extinction up to the fold Umax of the branch, whose stability above the fold is checked numerically.

2474

A bistability near Uc thus requires B f > 0 and k f /µ > 1/B f .

2475

The statement is derived: it is the standard bifurcation from a simple eigenvalue. Its hypotheses, the

2476

simplicity of r and r′ (Uc ) , 0, are checked numerically: the gap to the next eigenvalue is at least 1.08, and

2477

r′ (Uc ) ranges from −6.35 to −54.82. On the branches computed at n = 5, R = 25, with |U − Uc | < 0.009, the

2478

ratio of the equilibrium density to −r(U)/B ranges from 0.886 to 1.036 and tends to one at Uc .

2479

Numerical results (numerical).

2480

100.

The computations are for θ = 1, n = 5, 10 and 20, and R = 10, 25 and

2481

• All protocells fuse. B f ranges from −0.200 to −0.121. At threshold, 58–98% of the invading popu-

2482

lation are vesicles without replicases: dead daughters, and the pieces shed by protocells whose lone

2483

replicase copies only parasites. Fusion with them dilutes the pairs of living protocells. The only pos-

2484

itive contribution comes from fusions between two protocells that each hold a lone replicase, which

2485

form a new pair. The bifurcation is therefore supercritical for every k f /µ. Continuation of 17 branches

2486

(n = 5, 10 and 20; k f /µ from 1 to ∞) found no fold and no stationary population beyond Uc .

2487

• Only protocells with F ≥ 1 fuse (a rule that sees content). B f becomes positive in six of the nine cases,

2488

and the bifurcation is subcritical for k f /µ > 1/B f , that is, above 10.64 to 45.32 depending on the case.

2489

– A dense population then persists up to Umax = 0.8476 at n = 5, R = 25 and k f /µ = 100, while a

2490

rare one cannot invade beyond Uc = 0.6204.

2491

– At n = 5 and R = 25, Umax exceeds ln 2 for k f /µ between 30 and 50 and above.

2492

– Such populations require fusion rates of hundreds per molecular lifetime, and no known chem-

2493

istry is proposed for such a rule.
82


[page 83]
– A Gillespie simulation of a finite population illustrates the hysteresis at U = 0.75.

2494

2495

• Background. A background of vesicles carrying parasites lowered Uc in all 54 computed cases. In

2496

30 of them the block on F = 0 is stable, so that these values are invasion thresholds in the sense of

2497

Proposition 2.

2498

Transient compartmentalization (derived, sketch). Pooling 8,17,18 fuses all compartments, those without

2500

replicases included, before a blind reloading. By Lemma 1(c) applied to the pool, the pair density after
P
reloading is at most Ftot (Ftot − 1)/(Ntot − 1), so replicase production per replicase (at most RΛ V in all) is

2501

proportional to the replicase fraction of the pool. While the pool keeps many molecules without replicases, a

2502

rare replicase that cannot be copied alone thus declines at every round, whatever the load: what pooling can

2503

offer is the persistence of a dense population.

2504

S13. Proof of Theorem 4 (R > n)

2505

This section gives in full the proof of Theorem 4 for R > n summarized in SI S3 (provenance: S7). Its nota-

2506

tion is that of SI S2 and S3; its lemmas are numbered within its subsections, and its constants κ (Lemma 3.5)

2507

and κn (Section S13.4) are local to it.

2508

S13.1

2509

Throughout, y = n/R is fixed and n, R → ∞ together. We prove the scaling law of Theorem 4 when the

2510

replicase makes more complete copies per lifetime than its protocell holds molecules at birth (R > n, that is

2511

0 < y < 1), for every template weight θ > 0 of the parasites.

2512

Theorem 4 (for R > n). For every θ > 0 and every y ∈ (0, 1),

2499

Statement and plan


lim Uc (n, n/y, θ) = max 0, ln(1/θ) + ψ(y) ,

n→∞
2513

ψ(y) = − ln λc (y),

where λc (y) is the threshold of the limit process defined in (4) below, and
ln

2
≤ ψ(y) < ln 2.
1+y

2514

The threshold λc (y) is defined from the limit kernel alone, through a Schur reduction onto small types

2515

(Section S13.2). That it coincides with the threshold obtained by direct simulation of the limit process

2516

(Table S3) is checked numerically, not proved.

2517

Plan.

The proof has three parts, each proved below in full.

2518

(i) The limit process for y < 1 (Section S13.3). The reduced size u increases during every cycle and

2519

serves as a clock. In this clock the limit kernel is monotone in the type and in λ; large types drift

2520

down; the set of λ where the reduced kernel is critical or supercritical is a final segment, which gives

2521

hypothesis (H2); the reduced kernel is supercritical near λ = 1, which is (H3), with λc (y) ≤ (1 + y)/2;

2522

and λc (y) > 21 . Together, criticality is crossed exactly once.

83


[page 84]
2523

(ii) Uniform drift of the finite kernels (Section S13.4), for every y > 0: beyond some type M, the finite

2524

kernels Kn contract a polynomial weight, uniformly in large n and in all (q, θ) with max(q, q/θ) ≤ Λ0 <

2525

1.

2526

(iii) Convergence of the finite kernels (Section S13.5) for y < 1, coefficient by coefficient, and passage to
the limit in the Schur reduction, with explicit tail bounds (Section S13.6).

2527

2528

Section S13.7 assembles them. Section S13.8 states what remains open when R ≤ n. The results of SI S2

2529

that we use (the exact generator of the weights Va,b of Section S13.2, including losses; the closed form of the

2530

binomial partition, with its properties (P1)–(P3); the spectral bound at every fecundity; the sign of a Schur

2531

reduction without irreducibility) are proved in SI S2 and restated without proof in Section S13.2, where

2532

Lemmas 2.6–2.8 are proved.

2533

S13.2

2534

The finite model. A protocell divides when it holds 2n molecules. Its transient states are S n = {(F, N) : 2 ≤

2535

F ≤ N ≤ 2n − 1}, where F is the number of replicases and N the number of molecules. Let q = e−U ∈ (0, 1],

2536

λ = q/θ and Λ = max(q, q/θ) = λ max(1, θ). The transitions are

Setting, notation and results used

2538

• (F, N) → (F + 1, N + 1) at rate RF p and (F, N) → (F, N + 1) at rate RF(1 − p), with p(F, N) =

q(F − 1)/ (F − 1) + θ(N − F) ;

2539

• (F, N) → (F − 1, N − 1) at rate F, and (F, N) → (F, N − 1) at rate N − F;

2540

• a protocell with F ≤ 1 is dead; a copy made at N = 2n − 1 triggers division, at type f ∈ {2, . . . , 2n},

2537

2541

the number of replicases.

2542

At division, F1 ∼ Bin( f, 21 ) and P1 ∼ Bin(2n − f, 12 ) independently; the second daughter receives the rest,

2543

and Nd = Fd + Pd . A daughter with Fd ≤ 1 is dead; a daughter with Nd = 2n is at the division state ( f, 2n).

2544

Kn ( f, f ′ ) is the expected number of daughters of a type- f protocell that reach division with f ′ replicases; we

2545

extend it by zero to f, f ′ > 2n. Uc (n, R, θ) = sup{U ≥ 0 : ρ(Kn ) > 1}, and 0 if this set is empty. The generator

2546

of the finite chain is Gn h(F, N) = RF [p h(F + 1, N + 1) + (1 − p) h(F, N + 1) − h(F, N)] + F [h(F − 1, N −

2547

1) − h(F, N)] + (N − F) [h(F, N − 1) − h(F, N)], with h = 0 in dead states.

2548

The limit process

2549

and F → F −1 at rate F; F ≤ 1 is death; division occurs when u = 2y, and the two daughters start from (Bd , y)

2550

and ( f − Bd , y) with Bd ∼ Bin( f, 12 ). K∞ = K∞ (y, λ) is its mean matrix on the types {2, 3, . . . }. It depends on

2551

(q, θ) only through λ. Every row of Kn and of K∞ sums to at most 2: a protocell has two daughters, and each

2552

divides at most once.

2553

Weights. For a > 0, ϕa (F) = Γ(F − 1 + a)/Γ(F − 1), which vanishes at F = 1 (and at F = 0 for integer

2554

a ≥ 2); for integer a, ϕa (F) = (F − 1)F · · · (F + a − 2). For b > 0 and N ≥ 2, gb (N) = Γ(N − 1)/Γ(N − 1 + b),

2555

decreasing in N. Va,b = ϕa (F) gb (N), set to 0 in dead states. W2 = V2,2Λ = F(F − 1) g2Λ (N) is the density of

2556

replicase pairs, up to a factor depending on N. We write (x) j = x(x − 1) · · · (x − j + 1).

(y > 0). The state is (F, u), with u̇ = F −u between jumps; F → F +1 at rate λF(F −1)/u

84


[page 85]
2557

Schur reductions and the threshold. For a nonnegative matrix K on the types and a cut M, let A =

2558

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

2559

A cut M is admissible for K if there are a nondecreasing weight w ≥ max(1, ϕ2 ), β < 1 and C ≥ 1 with

2560

(Kw)( f ) ≤ βw( f ) for f > M and Kw ≤ Cw; the series above then converge for t < 1/β, since KBB wB ≤ βwB

2561

and KBA (·, j) ≤ CwB /w( j) (Lemma 6.1 gives explicit tails when rows sum to at most 2). Define


λc (y) = inf λ < 1 : ρ S ∞ (y, λ) > 1 ,

(4)

2562

with λc (y) = 1 if the set is empty, where S ∞ (y, λ) is the Schur reduction of K∞ (y, λ) on a cut admissible for

2563

K∞ (y, λ). By Lemma 2.6 the sign of ρ(S ∞ ) − 1 does not depend on the admissible cut (two cuts admissible

2564

with different weights are each compared with a cut beyond both), so λc (y) is well defined; admissible cuts

2565

exist for every λ < 1 when y < 1 (Lemma 3.3). Hypotheses (H2) and (H3) of the main text read: (H2)

2566

ρ(S ∞ (y, λ)) < 1 for every λ < λc (y); (H3) λc (y) < 1.

2567

Results used here (Results 2.1–2.5 from SI S2, stated without proof; Lemmas 2.6–2.8 proved here).

2568

Lemma 2.1 (exact generator). On S n , for a, b > 0 and V = Va,b , with ha (F) = aF/(F − 2 + a):

2569



(i) copy term: p V(F + 1, N + 1) + (1 − p) V(F, N + 1) − V(F, N) = V a(N − 1)p/(F − 1) − b /(N − 1 + b);

2570

(ii) loss term, N ≥ 3: F[V(F − 1, N − 1) − V] + (N − F)[V(F, N − 1) − V] = V [N(b − ha ) + ha (2 − b)]/(N − 2);

2571

2572

at (2, 2) it equals −2V;
(iii) p ≤ Λ(F − 1)/(N − 1) in every state.

2573

Consequently: (C1) if b ≥ Λa the copy term is ≤ 0; (C2) if Λ ≤ 1 and b = Λa ≤ 2 the loss term is

2574

≤ 0; (C3) if a ≥ 2, Λ < 1 and b = Λa > 2, the loss term is at most (b − 2)V everywhere, and ≤ 0 when

2575

F ≥ F ∗ = b(a − 2)/(a − b).

2576

Parts (iii) and (C3) are elementary. If θ ≥ 1 the denominator of p is at least N − 1, and if θ < 1 it equals

2577

θ(N−1)+(1−θ)(F−1) ≥ θ(N−1); this gives (iii). The numerator in (ii) equals (b−2)(N−2)+(2−ha )(N−2+b),

2578

and ha ≥ 2 for a ≥ 2; this gives the bound (b − 2)V in (C3), and the numerator is ≤ 0 when ha (F) ≥ b, that is

2579

when F ≥ F ∗ .

2580
2581

Corollary 2.2 (supermartingale). If a > 0, Λ ≤ 1 and b = Λa ≤ 2, then for every initial state x0 ∈


S n ∪ {( f, 2n)}, gb (2n) E x0 ϕa ( f ′ )1{division} ≤ Va,b (x0 ), where f ′ is the type at division (with equality, f ′ = f ,

2582

when x0 = ( f, 2n)).

2583

Lemma 2.3 (binomial partition). For integer a ≥ 2, b > 0 and f ∈ {2, . . . , 2n},
E ϕa (F1 ) gb (N1 ) = gb (2n)




a
X

sa, j ( f ) j α j (n, b),

j=2

!
a
sa, j =
(a − 2)a− j ≥ 0, sa,a = 1,
j

2584


where α j (n, b) = E[r j (N1 )], N1 ∼ Bin(2n, 21 ), r j (m) = (m) j gb (m)/ (2n) j gb (2n) for m ≥ j and 0 otherwise.

2585

(P1) α j increases in b, and α j ≤ 1 if b ≤ 2. (P2) α j (n, b) → 2b− j as n → ∞, and α j (n, b) is bounded
85


[page 86]
2586

uniformly in n and in b ≤ b0 . (P3) cn (Λ) := 2α2 (n, 2Λ) increases in Λ, with cn ( 12 ) = 1 − 21−2n < 1 and

2587

cn (Λ) ≤ 2 for Λ ≤ 1.

2588

Proposition 2.4 (spectral bound at every fecundity). For all n ≥ 2, θ > 0, q ∈ (0, 1] and R ∈ (0, ∞]:

2589

ρ(Kn ) ≤ cn (Λ). In particular ρ(Kn ) < 1 whenever Λ ≤ 12 .

2590

Lemma 2.5 (sign of a Schur reduction; finite matrices). Let K ≥ 0 be a finite matrix on A⊔B with ρ(KBB ) < 1,

2591

and S = KAA + KAB (I − KBB )−1 KBA . Then ρ(K) − 1 and ρ(S ) − 1 have the same sign. No irreducibility is

2592

needed.

2593

Lemma 2.6 (independence of the cut). Let K ≥ 0 on a countable set of types, w ≥ 1 with (Kw)( f ) ≤ βw( f )

2594

for f > M0 (β < 1) and Kw ≤ Cw. For M0 ≤ M < M ′ , ρ(S (M) ) − 1 and ρ(S (M ) ) − 1 have the same sign.

2595

Proof. Let D = {M + 1, . . . , M ′ } and S ′ = S (M ) , a finite matrix on A M ⊔ D. Cutting every path that defines

′

′

2596
2597

S (M) (i, j) at its visits to D gives, by Tonelli, S (M) = S ′AA + S ′AD (I − S ′DD )−1 S ′DA . On BM = D ⊔ BM′ we
P
have KBM BM w ≤ βw; the rows of BM′ give k KBk′ B′ KB′ D wD ≤ wB′ , and then the rows of D give S ′DD wD ≤

2598

KDD wD + KDB′ wB′ ≤ βwD , so that ρ(S ′DD ) ≤ β < 1. Lemma 2.5 applies to S ′ .

2599

Lemma 2.7 (subsolutions). Let K ≥ 0 with an admissible cut M (weight w, constant β), and t ∈ (0, 1/β). If

2600

v ≥ 0, v ≤ Cw, v is not identically zero on A, tKv ≥ v on B and tKv ≥ (1 + η)v on A, then ρ(S (t)) ≥ 1 + η. If

2601

moreover t ≤ 1, then ρ(S (1)) ≥ (1 + η)/t.

□

2603

P
Proof. On B, iterating m times, vB ≤ k<m (tKBB )k tKBA vA + (tKBB )m vB , and the last term is at most
P
C(tβ)m wB → 0. Hence vB ≤ k≥0 (tKBB )k tKBA vA , and on A, (1 + η)vA ≤ tKAA vA + tKAB vB ≤ S (t)vA ;

2604

the Collatz–Wielandt inequality for the finite matrix S (t) gives ρ(S (t)) ≥ 1 + η. For t ≤ 1, S (t) ≤ t S (1)

2605

entrywise.

2606

Lemma 2.8 (supersolutions). Let K ≥ 0 with an admissible cut M (weight w, constant β). If v ≥ 0, v > 0 on

2607

A, v ≤ Cw and Kv ≤ s∗ v on all types for some s∗ ∈ (β, 1), then ρ(S (1)) ≤ s∗ < 1.

2602

□

2609

Proof. Let t = 1/s∗ ∈ (1, 1/β). From tKv ≤ v on B we get, by iteration and positivity, vB ≥
P
P
k
k
k<m (tK BB ) tK BA vA for every m, hence v B ≥ k≥0 (tK BB ) tK BA vA ; on A, vA ≥ tKAA vA + tKAB v B ≥ S (t)vA , so

2610

ρ(S (t)) ≤ 1. Since t ≥ 1, S (t) ≥ t S (1) entrywise, and ρ(S (1)) ≤ 1/t = s∗ .

2611

S13.3

2612

Fix y ∈ (0, 1). The generator of the limit process, acting on functions g(F, u) differentiable in u, is

2608

□

The limit process when y < 1

Gg(F, u) = (F − u) ∂u g +




λF(F − 1) 
g(F + 1, u) − g(F, u) + F g(F − 1, u) − g(F, u) ,
u

2613

with g = 0 in dead states. For V = ϕa (F)u−b , since ϕa (F+1)/ϕa (F) = (F−1+a)/(F−1) and ϕa (F−1)/ϕa (F) =

2614

(F − 2)/(F − 2 + a),
h
i
F
GV = V (aλ − b) + b − ha (F) ,
u

2615

ha (F) =

aF
.
F−2+a

(5)

For a ≥ 2, ha (2) = 2 and ha increases to a. With a = 2 and b = 2λ, the pair density Z = F(F − 1)u−2λ satisfies
GZ = −2(1 − λ) Z.
86

(6)


[page 87]
2616

Lemma 3.1 (size clock). While a lineage is alive, u̇ ≥ 2 − 2y > 0: the reduced size increases from y to 2y,

2617

and every cycle lasts at most T y = y/(2 − 2y). In the time s = u, F is an inhomogeneous birth–death chain

2618

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

2619

and every lineage alive at s = 2y divides there, at type F2y . For F ≥ 2 and s ≤ 2y, F − s ≥ F(1 − y), so

2620

b(F, s) ≤ λ(F − 1)/(y(1 − y)) and d(F, s) ≤ 1/(1 − y): the chain does not explode, and sup s F s has finite

2621

moments of all orders. Hence
K∞ (y, λ)( f, f ′ ) = 2

X


P Bin( f, 21 ) = j P j (F2y = f ′ ),

j≥2
2622

and every coefficient of K∞ (y, λ) is positive for λ > 0.

2623

Proof. While F ≥ 2, u ≤ 2y < 2 ≤ F, so u̇ = F −u ≥ 2−2y. Between jumps s = u is a C 1 change of time with

2624

derivative F −u > 0; intensities in the time s are those in the time t divided by F − s. F − s ≥ F −2y ≥ F(1−y)

2625

because F ≥ 2. Every finite sequence of jumps has positive probability.

2626

Lemma 3.2 (monotonicity). Let h ≥ 0 on the types, with h ≤ Cw for a polynomial weight w, and h̄ its

2627

extension by 0 to the dead state.

□

2628

(a) If h is nondecreasing, so is K∞ (y, λ)h.

2629

(b) If h is nondecreasing and λ ≤ λ′ , then K∞ (y, λ)h ≤ K∞ (y, λ′ )h.

2630

(c) If moreover λ < λ′ and h(2) > 0, then K∞ (y, λ′ )h ≥ K∞ (y, λ)h + h(2) ω, with ω( f ) > 0 for every f ≥ 2.

2631

Proof. (a) Two chains with jumps ±1 started from j ≤ j′ are coupled to run independently while they differ

2632

and identically once they meet; they never cross, so F s ≤ F ′s , and E j [h̄(F2y )] is nondecreasing in j (and 0 for

2633

j ≤ 1). Bin( f, 12 ) is stochastically nondecreasing in f . (b) From a common state, let common births occur

2634

at rate bλ , births of the λ′ -chain alone at rate bλ′ − bλ ≥ 0, and common deaths at rate d; from different

2635

λ ) − h̄(F λ ) ≥ 0, and ≥ h(2) on
states, let the chains be independent. Then F λs ≤ F λs for all s. (c) h̄(F2y
2y
′

′

λ ≥ 2 > F λ }. From any j ≥ 2, E has positive probability: the λ′ -chain alone receives a birth, after
E = {F2y
2y
′

2636
2637
2638

2639

2640

which the two chains are independent, and the λ-chain then undergoes j − 1 deaths while the other does not
P
□
jump. Set ω( f ) = 2 j P(Bin( f, 21 ) = j) P j (E).
Lemma 3.3 (drift of large types).

+4
(a) For λ ≤ 2/3: (K∞ ϕ3 )( f ) ≤ 23λ−2 ff +1
ϕ3 ( f ).

(b) For λ < 1 and an integer a > 1/(1 − λ): (K∞ ϕa )( f )/ϕa ( f ) ≤ 21−a(1−λ) + C/ f , and K∞ ϕa+1 ≤ C ′ ϕa+1 .

2641

The constants are uniform for λ in a compact subset of (0, 2/3] in (a), of (0, 1) in (b) (with a >

2642

1/(1 − max λ)). Consequently, for every λ < 1 there are admissible cuts for K∞ (y, λ), with weight w = ϕa

2643

(nondecreasing, ϕa ≥ ϕ2 and ϕa ≥ ϕa (2) = a! ≥ 1), uniformly on compact sets of λ.

2644

Proof. Let V = ϕa (F)u−aλ , so that GV = V[aλ − ha (F)] by (5). The cycle has bounded duration and F

2645

has finite moments (Lemma 3.1), so the Dynkin formula applies over a cycle. At division u = 2y and

2646

V = ϕa ( f ′ )(2y)−aλ ; in dead states V = 0.

87


[page 88]
2647

(a) With a = 3, h3 ≥ 2 and GV ≤ (3λ − 2)V ≤ 0. Hence E j [ϕ3 ( f ′ )1{div}] ≤ 23λ ϕ3 ( j). Since ϕ3 =

2648

(F)3 +3(F)2 and E[(Bd )i ] = ( f )i 2−i for Bd ∼ Bin( f, 12 ), two daughters give (K∞ ϕ3 )( f ) ≤ 23λ−2 [( f )3 +6( f )2 ] =

2649

23λ−2 f ( f − 1)( f + 4).

2650
2651

(b) Let Fa∗ be the smallest integer with ha (Fa∗ ) ≥ aλ and γ = (aλ − 2)+ . As u ≥ y and ϕa is nondecreasing,
GV ≤ γ ϕa (Fa∗ )y−aλ 1{F < Fa∗ }, and




E j ϕa ( f ′ )1{div} ≤ 2aλ ϕa ( j) + γ T y ϕa (Fa∗ ) P j (min s F s < Fa∗ ) .

2652

In the time s, each replicase dies at rate 1/(F − s) ≤ 1/(2 − 2y) and births only add replicases. Thinning

2653

independent Poisson clocks of rate 1/(2 − 2y) attached to the j initial replicases shows that the number of

2654
2655

them still present at s = 2y, a lower bound for min s F s , dominates Bin( j, e−y/(2−2y) ); hence P j (min F < Fa∗ )
P
decays exponentially in j. By Lemma 2.3’s expansion ϕa = ai=2 sa,i (F)i , E[ϕa (Bd )] = 2−a ( f )a +O( f a−1 ), and

2656

( f )a ≤ ϕa ( f ). Two daughters give the bound. The same computation with a + 1 gives the second weight. □

2657

Lemma 3.4 (one crossing; hypothesis (H2)). If ρ(S ∞ (y, λ0 )) ≥ 1, then ρ(S ∞ (y, λ)) > 1 for every λ ∈ (λ0 , 1).

2658

Hence {λ : ρ(S ∞ (y, λ)) ≥ 1} is a final segment of (0, 1), ρ(S ∞ (y, λ)) < 1 for every λ < λc (y), and ρ(S ∞ (y, λ)) >

2659

1 for every λ ∈ (λc (y), 1).

2660

Proof. Fix λ ∈ (λ0 , 1), an integer a > 1/(1 − λ), w = ϕa , and a cut M and β < 1 admissible uniformly on

2661

[λ0 , λ] (Lemma 3.3(b)); by Lemma 2.6 the hypothesis holds with this cut. Write Kµ = K∞ (y, µ) and S µ (t) for

2662

its reduction.

2663
2664
2665
2666

An eigenfunction at λ0 . ρ(S λ0 (t)) is continuous in t ∈ [0, 1/β), zero at 0 and ≥ 1 at 1: there is t∗ ∈ (0, 1]
with ρ(S λ0 (t∗ )) = 1. All coefficients of S λ0 (t∗ ) ≥ t∗ Kλ0 ,AA are positive (Lemma 3.1); let xA > 0 be its Perron
P
vector and xB = k (t∗ KBB )k t∗ KBA xA . As rows sum to at most 2 and w ≥ 1, t∗ KBA xA ≤ 2t∗ max(xA ) wB , so
xB ≤ 2t∗ max(xA )(1 − t∗ β)−1 wB ; and x = (xA , xB ) > 0 satisfies t∗ Kλ0 x = x, with x ≤ Cw.

2667

The nondecreasing envelope. Let x̃( f ) = max2≤g≤ f x(g); then x ≤ x̃ ≤ Cw since w is nondecreasing.

2668

By Lemma 3.2(a), t∗ Kλ0 x̃ is nondecreasing and ≥ t∗ Kλ0 x = x; for g ≤ f , (t∗ Kλ0 x̃)( f ) ≥ (t∗ Kλ0 x̃)(g) ≥ x(g),

2669

hence t∗ Kλ0 x̃ ≥ x̃.

2670
2671

Above λ0 . By Lemma 3.2(b,c), t∗ Kλ x̃ ≥ x̃ + t∗ x̃(2)ω, so t∗ Kλ x̃ ≥ x̃ on B and ≥ (1 + η) x̃ on the finite set
A, with η = minA t∗ x̃(2)ω/ x̃ > 0. Lemma 2.7 gives ρ(S ∞ (y, λ)) ≥ (1 + η)/t∗ > 1.

2672

Consequences. If ρ(S ∞ (λ0 )) ≥ 1 for some λ0 < λc , then ρ > 1 on (λ0 , λc ), contradicting the definition

2673

of λc . For λ > λc , the definition gives λ1 ∈ [λc , λ) with ρ(S ∞ (λ1 )) > 1, and the first statement gives

2674

ρ(S ∞ (λ)) > 1.

□

2676

Lemma 3.5 (hypothesis (H3), with a bound). For λ ∈ (0, 1] and every type f , (K∞ ϕ2 )( f ) ≥ 22κ−1 ϕ2 ( f ) with

κ = (λ − y)/(1 − y). Consequently λc (y) ≤ (1 + y)/2 < 1, that is ψ(y) ≥ ln 2/(1 + y) .

2677


Proof. In the time s, the generator L of the chain of Lemma 3.1 gives (Lϕ2 )(F) = 2ϕ2 (F)(λF − s)/ s(F − s) (a

2678

birth adds 2F to ϕ2 , a death removes 2(F −1)). For F ≥ 2 and s ≤ 2y, (λF − s)/(F − s) = λ−(1−λ)s/(F − s) ≥

2679

λ − (1 − λ) 2y/(2 − 2y) = κ, so Lϕ2 ≥ (2κ/s)ϕ2 , also at the absorbing state where ϕ2 = 0. Hence m(s) =

2680

E j [ϕ2 (F s )] satisfies m′ ≥ (2κ/s)m (moments are finite), and m(2y) ≥ 22κ ϕ2 ( j). With E[ϕ2 (Bd )] = ϕ2 ( f )/4 and

2681

two daughters, K∞ ϕ2 ≥ 22κ−1 ϕ2 . For λ1 ∈ ((1 + y)/2, 1), κ > 12 ; take a cut admissible at λ1 (Lemma 3.3(b))

2682

and apply Lemma 2.7 with t = 1 and v = ϕ2 ≤ w: ρ(S ∞ (y, λ1 )) ≥ 22κ−1 > 1, so λc (y) ≤ λ1 .

2675

88

□


[page 89]
2683

Lemma 3.6 (λc > 12 ). For λ ∈ (0, 1) and every type f ,
i
hX Z τd
Z(Xtd ) dt > 0,
ℓ( f ) = 2(1 − λ)(2y)2λ E

(K∞ ϕ2 )( f ) = 22λ−1 ϕ2 ( f ) − ℓ( f ),

d

0

2684

where the expectation is over the partition and the cycles of the daughters. There is δ(y) > 0 such that

2685

ρ(S ∞ (y, λ)) < 1 for all λ ≤ 12 + δ(y). Hence λc (y) > 12 and ψ(y) < ln 2.

2686

Proof. The identity. By (6) and the Dynkin formula over a cycle of bounded duration,
E j Z(Xτ )1{div} = Z( j, y) − 2(1 − λ) E j


Z τ



Z dt,
0

2687

and at division Z = ϕ2 ( f ′ )(2y)−2λ . Summing over two daughters with E[ϕ2 (Bd )] = ϕ2 ( f )/4 gives the identity.

2688

ℓ( f ) > 0 because a daughter receives two replicases with positive probability.
A cut. Fix δ0 ∈ (0, 61 ), so that 12 + δ0 < 32 . By Lemma 3.3(a), choose M with β3 = 23( 2 +δ0 )−2 (M +
1

2689
2690

5)/(M + 2) < 1; then K∞ ϕ3 ≤ β3 ϕ3 beyond M and K∞ ϕ3 ≤ C3 ϕ3 everywhere, with C3 = 23( 2 +δ0 )−1 since

2691

( f + 4)/( f + 1) ≤ 2, for λ ≤ 21 + δ0 , and M is admissible with weight ϕ3 . Let A = {2, . . . , M}.

1

2692
2693
2694

A uniform loss on A. Before its first jump a daughter started at ( j, y) keeps F = j, Z ≥ ϕ2 ( j)(2y)−2λ , and
Rτ
the first jump occurs at rate at most c j = λ j( j − 1)/y + j, while the cycle lasts at least y/ j; hence E j 0 Z ≥
ϕ2 ( j)(2y)−2λ (1 − e−c j y/ j )/c j . There is therefore ηA > 0 with ℓ ≥ ηA ϕ2 on A, uniformly in λ ∈ (0, 21 + δ0 ].

2695

A supersolution. Let v = ϕ2 + εv ϕ3 , and note ϕ3 = ( f + 1)ϕ2 . Choose εv > 0 with εvC3 (M + 1) ≤ ηA /4;

2696

then s∗ ∈ (max(β3 , 1 − ηA /2), 1) with 1 − s∗ < εv (s∗ − β3 )(M + 2); then δ ∈ (0, δ0 ] with 22δ ≤ s∗ + 3ηA /4 and

2697

22δ − s∗ ≤ εv (s∗ − β3 )(M + 2). At λ = 12 + δ: on B, K∞ v ≤ 22δ ϕ2 + εv β3 ϕ3 ≤ s∗ v, since ϕ3 ≥ (M + 2)ϕ2 there;

2698

on A, K∞ v ≤ (22δ − ηA )ϕ2 + εvC3 ϕ3 ≤ (22δ − 34 ηA )ϕ2 ≤ s∗ v. Lemma 2.8 gives ρ(S ∞ (y, 12 + δ)) ≤ s∗ < 1, and

2699

Lemma 3.4 extends this to every λ ≤ 21 + δ. So λc (y) ≥ 12 + δ.

2700

S13.4

2701

Lemma 4.1 (uniform drift). Let y > 0, Λ0 ∈ (0, 1), an integer a > 1/(1 − Λ0 ) and β ∈ (21−a(1−Λ0 ) , 1). There

2702

are M, n0 and C such that, for all n ≥ n0 , R = n/y, θ > 0 and q ∈ (0, 1] with Λ = max(q, q/θ) ≤ Λ0 :

□

Uniform drift of the finite kernels (every y > 0)

(Kn ϕa )( f ) ≤ β ϕa ( f ) (M < f ≤ 2n),

(Kn ϕa+1 )( f ) ≤ C ϕa+1 ( f ) (2 ≤ f ≤ 2n).

2703

The weights w = ϕa and w′ = ϕa+1 satisfy 1 ≤ w ≤ w′ and w/w′ = 1/( f + a − 1) → 0.

2704

Constants. Let b = Λa. If b ≤ 2, Corollary 2.2 applies and what follows holds with Q1 = 0. If b > 2, let

2705

F ∗ = b(a − 2)/(a − b); ca = Γ(F ∗ + a − 1)/Γ(F ∗ + 1), which bounds ϕa (F)/ϕ2 (F) = Γ(F − 1 + a)/Γ(F + 1)

2708

for F ≤ F ∗ since this ratio increases in F; εy = min(y/4, 1) and Nε = ⌈εy R⌉; σa = b − 2Λ = Λ(a − 2),

 

X1 = Nε − 1 + 2Λ, X2 = 2n − 1 + 2Λ; Ξn = Γ(X2 + σa )/Γ(X2 ) / Γ(X1 + σa )/Γ(X1 ) , which tends to (2y/εy )σa ;

κn = gb (2n)/g2Λ (2n); and Q1 = (b − 2) ca Ξn / 2(1 − Λ) .

2709

Proof. Step 1: two generator inequalities. With V = Va,b , Lemma 2.1 gives on S n

2706
2707

Gn V ≤ (b − 2)+ V 1{F < F ∗ },

89

Gn W2 ≤ −2(1 − Λ) W2 .

(7)


[page 90]
2710

For V: the copy term is ≤ 0 by (C1); the loss term is at most (b − 2)V everywhere and ≤ 0 for F ≥ F ∗ by

2711

(C3), and ≤ 0 everywhere by (C2) if b ≤ 2. For W2 : the copy term is ≤ 0 by (C1) with b = 2Λ; with a = 2,

2712

h2 = 2 and the loss term equals (2Λ − 2)W2 for N ≥ 3, and −2W2 at (2, 2).

2713
2714
2715
2716

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
2717

The tail of the cycle. With c = 2(1 − Λ), (7) gives (∂t + Gn )(ect W2 ) ≤ 0, so E x [ec(t∧τ) W2 (Xt∧τ )] ≤ W2 (x). As

2718

W2 ≥ ϕ2 (2)g2Λ (2n − 1) ≥ 2g2Λ (2n) on S n ,

P x (τ > t) ≤ e−ct W2 (x)/ 2g2Λ (2n) .

(10)

2719

Step 3: where N ≥ εy R. There, for F < F ∗ , V/W2 = [ϕa (F)/ϕ2 (F)] [gb (N)/g2Λ (N)]. The first factor is

2720

at most ca . The second, Γ(N − 1 + 2Λ)/Γ(N − 1 + b), decreases in N and equals Ξn κn at N = Nε . Hence

2721

V ≤ ca Ξn κn W2 on {F < F ∗ , N ≥ εy R} and, by (9),
(b − 2)+ E x

Z τ

V1{F < F ∗ , N ≥ εy R} ds ≤ Q1 κn W2 (x) = Q1 gb (2n) W2 (x)/g2Λ (2n).

(11)

0
2722

Step 4: where N < εy R; an M/M/∞ queue. On {F < F ∗ }, V ≤ ϕa (F ∗ )gb (2) = ϕa (F ∗ )/Γ(1 + b). While

2723

the protocell lives, N jumps by +1 at rate RF ≥ 2R and by −1 at rate N. Let Ñ be a birth–death chain with

2724

birth rate 2R and death rate Ñ, started at N0 (an M/M/∞ queue), coupled with X as follows: when N = Ñ,

2725

common births at rate 2R, births of N alone at rate RF − 2R ≥ 0, common deaths at rate N; when N , Ñ,

2727

independent moves. Jumps are ±1 and there are no simultaneous jumps outside common ones, so Nt ≥ Ñt

for t < τ; the rates of Ñ depend on Ñ only. At fixed t, Ñt = Bin(N0 , e−t ) + Poisson 2R(1 − e−t ) , independent,

2728

with mean µt ≥ min(N0 , 2R). For a sum X of independent Bernoulli and Poisson variables with mean µ,

2729

P(X ≤ µ/2) ≤ e−µ/8 . If N0 ≥ 2εy R, then µt ≥ 2εy R (as εy ≤ 1), and

2726

P x (Nt < εy R, t < τ) ≤ e−εy R/4
2730
2731

for all t ≥ 0.

(12)

Rτ

With (10), for every T > 0, E x 0 1{N s < εy R} ds ≤ T e−εy R/4 + e−cT W2 (x)/ 2c g2Λ (2n) .
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

2732

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

2733

Since 1/gb (2n) ≤ (2n + b)b , W2 (x)/g2Λ (2n) ≤ ϕ2 (2n)g2Λ (2)/g2Λ (2n) is polynomial in n, and εy R =

2734

min(n/4, n/y) grows linearly in n, η̄n = sup x ηn (x) → 0 exponentially fast, uniformly in Λ ≤ Λ0 .

2735

Step 6: the partition. A daughter with Nd < 2εy R ≤ n/2 has probability at most P(Bin(2n, 12 ) < n/2) ≤
90


[page 91]
2736

e−n/4 (Hoeffding) and contributes at most ϕa (2n)e−n/4 . A daughter that receives the 2n molecules divides at

2737

once at type f , and (13) holds for it with η = 0. For the others we use (13), and we bound the sum over them

2738

of its first two (nonnegative) terms by the sum over all daughters, which Lemma 2.3, applied with a and with

2739

2, computes:
(Kn ϕa )( f ) ≤ 2

a
X

sa, j ( f ) j α j (n, b) + Q1 cn (Λ) ϕ2 ( f ) + εn ,

εn = 2η̄n + 2ϕa (2n)e−n/4 → 0.

(14)

j=2

2740

Step 7: uniformity and the choice of M. In Λ ≤ Λ0 : α j (n, Λa) ≤ α j (n, Λ0 a) (P1), bounded by some Ā

2742

uniformly in n (P2); F ∗ = Λ(a − 2)/(1 − Λ) increases with Λ, and so does ca ; by x s e−s/x ≤ Γ(x + s)/Γ(x) ≤

(x + s) s (s ≥ 0), Ξn ≤ (X2 + σa )/X1 σa eσa /X1 , which is bounded in n once εy R ≥ 2; hence Q1 ≤ Q̄1 ; and

2743

cn (Λ) ≤ 2. In f : for f ≥ 2, ϕa ( f ) ≥ ( f − 1) f a−1 ≥ f a /2, so ( f )a ≤ ϕa ( f ), ( f ) j ≤ 2 f j−a ϕa ( f ) for j < a, and

2744

ϕ2 ( f ) ≤ 2 f 2−a ϕa ( f ). For f > M:

2741

X
εn
(Kn ϕa )( f )
≤ 2αa (n, Λ0 a) + 4Ā
sa, j M j−a + 4Q̄1 M 2−a +
.
ϕa ( f )
ϕa (M)
j<a
2745

By (P2), 2αa (n, Λ0 a) → 21−a(1−Λ0 ) < β. If a ≥ 3, the two middle terms tend to 0 with M; if a = 2, they

2746

vanish (the sum over 2 ≤ j < a is empty, and Q1 = 0 since b = 2Λ ≤ 2). Choose M, then n0 . The same

2747

computation with a + 1, b′ = Λ(a + 1), gives (14) for ϕa+1 , each term of which is bounded by a constant

2748

times ϕa+1 ( f ), uniformly in f and n ≥ n0 .

2749

Remark 4.2. The constants are large: at n = ∞ the bound (14) falls below 1 beyond M = 193 at Λ = 0.75,

2750

a = 5, and beyond M = 1558 at Λ = 0.9, a = 11; on the exact finite kernels at n = 120 the smallest such

2751

M ranges from 26 to 60 in the cases computed. Only the existence of M matters: by Lemma 2.6 the sign of

2752

ρ(S ) − 1 does not depend on the admissible cut.

2753

S13.5

2754

Proposition 5.1 (convergence to the limit kernel). Let 0 < y < 1, θ > 0, and I a compact subset of (0, ∞)

2755

such that Λ = λ max(1, θ) ≤ 1 for λ ∈ I. Let R = n/y and q = θλ. For all types f, f ′ ≥ 2,

□

Convergence of the finite kernels when y < 1

sup Kn ( f, f ′ ) − K∞ (y, λ)( f, f ′ ) → 0
λ∈I

2756

(n → ∞).

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

2757

where c1 and CG depend only on y, θ, M and max I. One lets n → ∞, then M → ∞.

2758

Proof. Step 1: the test function. Fix f ′ and u0 = y/8. For F ≥ 1 and u ∈ [u0 , 2y] let v(F, u) be the probability

2759

that the limit lineage started at (F, u) divides at type f ′ : v(1, ·) = 0 and v(F, 2y) = 1{F = f ′ }. For F ≥ 2

2760

and u ≤ 2y < 2, F − u ≥ F(1 − y) > 0, so the size clock of Lemma 3.1 is defined on [u0 , 2y], with

2761

b(F, s) ≤ λ(F − 1)/(u0 (1 − y)) and d(F, s) ≤ 1/(1 − y). The strong Markov property at the first jump gives
R 2y

v(F, s) = 1{F = f ′ }e− s (b+d)(F,r)dr +

Z 2y

Rr

′
′
e− s (b+d)(F,r )dr b(F, r)v(F + 1, r) + d(F, r)v(F − 1, r) dr.

s

91


[page 92]
2762

The integrand is bounded, so v(F, ·) is Lipschitz, hence continuous; the integrand is then continuous, v(F, ·)

2763

is C 1 , and ∂u v(F, u) = −b ∆+ v − d ∆− v with ∆± v = v(F ± 1, u) − v(F, u). The right-hand side is C 1 , so v(F, ·)

2764

is C 2 . Multiplied by F − u, this is G∞ v = 0, where G∞ v = (F − u)∂u v + λF(F − 1)u−1 ∆+ v + F∆− v is the

2765

generator of the limit process. Since |∆± v| ≤ 1, for u ∈ [u0 , 2y] and F ≥ 2:
|∂u v(F, u)| ≤ b + d ≤ c1 F,

c1 =

λ/u0 + 1
.
1−y

2766

Differentiating the equation, ∂2u v = −[∂u b ∆+ v + b ∆+ ∂u v + ∂u d ∆− v + d ∆− ∂u v], with |∂u b| = λF(F − 1)|2u −

2767

F|/(u2 (F−u)2 ) ≤ λ(F−1)/(u20 (1−y)2 ) (as |2u−F| ≤ F), ∂u d = F/(F−u)2 ≤ 1/(2(1−y)2 ), |∆+ ∂u v| ≤ c1 (2F+1)

2768

and |∆− ∂u v| ≤ c1 (2F − 1). Hence
|∂2u v(F, u)| ≤ c2 F 2 ,

c2 =

λ
2u20 (1 − y)2

+

2λc1
1
c1
+
+
.
2
u0 (1 − y) 8(1 − y)
1−y

2769

Step 2: the test function on the finite chain. Let ṽ(F, N) = v(F, N/R). Since 2n/R = 2y exactly, ṽ(F, 2n) =

2770

′
1{F = f ′ } at division states, and ṽ = 0 at dead states. Hence E x [ṽ(Xτ )] is the probability P(n)
x ( f ) that the

2771

finite chain started at x divides at type f ′ .

2773

Step 3: the generator gap. Let umin = y/4, M ≥ max( f, f ′ ), D = {(F, N) ∈ S n : F ≤ M, N ≥ umin R}, and

R ≥ R0 = max 8/y, 4M(1 + θ)/(θumin ) . At x = (F, N) ∈ D, with u = N/R, a second-order Taylor expansion

2774

in u (step 1/R) gives

2772


 F

Gn ṽ = RF p ∆+ v + F∆− v + (F − u)∂u v + F p ∂u v(F + 1) − ∂u v(F) + ∂u v(F) − ∂u v(F − 1) + r,
R
2775

and subtracting G∞ v = 0,


 F

λF(F − 1)  +
Gn ṽ = RF p −
∆ v + F p ∂u v(F + 1) − ∂u v(F) + ∂u v(F) − ∂u v(F − 1) + r.
u
R

2776

Each term is O(1/R). (i) (F − 1) + θ(N − F) = θRu(1 + e) with e = (F(1 − θ) − 1)/(θRu) and |e| ≤

2777

2F(1 + θ)/(θRu) ≤ 12 ; so RF p = λF(F − 1)/(u(1 + e)) and |RF p − λF(F − 1)/u| ≤ 4λM 3 (1 + θ)/(θRu2min ). (ii)

2778

F p ≤ ΛF(F − 1)/(N − 1) ≤ 2ΛM 2 /(Rumin ) (Lemma 2.1(iii), and N − 1 ≥ umin R/2), so the second term is

2779

at most 2ΛM 2 c1 (2M + 1)/(Rumin ); the third is at most 2c1 M 2 /R. (iii) The arguments u ± 1/R stay in [u0 , 2y]

2780

because R ≥ 8/y, so |r| ≤ c2 [RF(F + 1)2 + NF 2 ]/(2R2 ) ≤ c2 (M + 1)2 (M + 2y)/(2R). Hence |Gn ṽ| ≤ CG /R on

2781

D, with
CG =

2782

4λM 3 (1 + θ) 2ΛM 2 c1 (2M + 1)
c2 (M + 1)2 (M + 2y)
2
+
+
2c
M
+
.
1
umin
2
θu2min

Step 4: Dynkin’s formula stopped at the exit from D. Let σ be the exit time from D. As 0 ≤ ṽ ≤ 1,
′
P(n)
x ( f ) − ṽ(x) ≤ P x (σ < τ) + (CG /R) E x [τ].

2783
2784

Step 5: the duration of the cycle. On S n , Gn N = RF − N ≥ 2R − (2n − 1) > 2R(1 − y) as F ≥ 2. So
Nt∧τ − 2R(1 − y)(t ∧ τ) is a submartingale, and since N ≤ 2n,

E x [τ] ≤ (2n − N0 )/ 2R(1 − y) ≤ y/(1 − y).

2785

(16)

(17)

Step 6: the exit from D, for N0 ≥ n/2 and n ≥ 20. Replicases: V1,Λ = (F − 1)gΛ (N) satisfies Gn V1,Λ ≤

92


[page 93]
2786

0 by (C1)–(C2) (a = 1, b = Λ ≤ 1), so it is a nonnegative supermartingale, and V1,Λ ≥ MgΛ (2n) on

2787

{F ≥ M + 1}; by Doob’s maximal inequality and the bounds on Γ(x + s)/Γ(x), P x (supt≤τ Ft ≥ M + 1) ≤

2788

(F0 − 1)gΛ (N0 )/(MgΛ (2n)) ≤ 5(F0 − 1)/M. Size: realize the M/M/∞ queue Ñ ≤ N of Step 4 of Lemma 4.1

2789

with independent exponential lifetimes of mean 1, and cut [0, T ] into windows of length ln(3/2). On the

2790

window starting at tk , Ñ is at least the number S k of customers present at tk and still present at tk + ln(3/2),

2791

a sum of independent Bernoulli and Poisson variables of mean at least 23 min(N0 , 2R) ≥ yR/3. By Chernoff,

2792

P(S k < yR/4) ≤ e−yR/96 . With T = R and Markov’s inequality applied to (17),



y
R
P x inf t<τ Nt < umin R ≤ (1−y)R
+ ln(3/2)
+ 1 e−yR/96 .

2793

Step 7: the daughters. Fd ∼ Bin( f, 12 ) and Nd ∼ Bin(2n, 12 ). By Lemma 3.1, K∞ ( f, f ′ ) = 2E[v(Fd , y)],

2794

′
−n/4 ) and the
while Kn ( f, f ′ ) = 2E[P(n)
xd ( f )]. We discard the daughters with Nd < n/2 (probability at most e

2795
2796

daughter that receives all 2n molecules (probability 2−2n ). The others lie in D: (16), (17) and Step 6 bound
√
′
|P(n)
n/2. This is (15). The
xd ( f ) − ṽ(xd )|; and |ṽ(xd ) − v(F d , y)| ≤ c1 F d |Nd − n|/R by Step 1, with E|Nd − n| ≤

2797

constants increase with λ, so the bound is uniform on I.

2798

Remark 5.2. For y < 1 the reduced size increases (u̇ ≥ 2−2y), v is smooth up to the boundary u = 2y, which is

2799

crossed transversally, and the finite chain reaches the same boundary exactly (2n/R = 2y). For y ≥ 1 the first

2800

two properties fail: u decreases when F < u, and when 2y is an integer a lineage with F = 2y approaches

2801

u = 2y without reaching it, whereas the finite chain crosses 2n through its fluctuations. Numerically, at

2802

y = 0.5 the error decreases as 1/n (n e(n) between 0.428 and 0.995 for n = 25 to 200); the bound (15) only

2803

yields a rate of order n−1/4 .

2804

S13.6

2805

Lemma 6.1 (tails of the reduction). Let K ≥ 0 on the types, with rows summing to at most 2, weights 1 ≤ w ≤

2806

k K )(i, j)
w′ , M, β < 1 and C ≥ 1 with (Kw)( f ) ≤ βw( f ) for f > M and Kw′ ≤ Cw′ . Let tk (i, j) = (KAB KBB
BA

2807

for i, j ∈ A, and tk(L) the same sum restricted to paths whose intermediate points are all ≤ L. Then

□

Passage to the limit in the Schur reduction

tk (i, j) ≤ 2βk C w′ (i),
P

0 ≤ tk (i, j) − tk(L) (i, j) ≤ 2δL w′ (i) (k + 1) C k+1 ,

δL = sup w(g)/w′ (g).
g>L

′
m
k≥m tk (i, j) ≤ 2Cw (i)β /(1 − β), and the series defining S (t) converges for t < 1/β.

2808

In particular

2809

k K (·, j) ≤ 2βk w , and t (i, j) ≤
Proof. Rows sum to at most 2 and w ≥ 1, so KBA (·, j) ≤ 2wB ; then KBB
BA
B
k

2810

2βk (KAB wB )(i) ≤ 2βk (Kw′ )(i) ≤ 2βk Cw′ (i). A path that goes beyond L has a point of index l ∈ {0, . . . , k} in

2811

{g > L}; bounding the end of the path by 2βk−l w ≤ 2βk−l δL w′ at that point, and the beginning by C l+1 w′ (i),

2812

gives the second bound.

2813

Lemma 6.2 (passage to the limit). Let I be a set of parameters. Assume (a) Kn → K∞ coefficient by

2814

coefficient, uniformly on I; (b) there are weights 1 ≤ w ≤ w′ with δL → 0, and M, β < 1, C ≥ 1, n0 such that

2815

the hypotheses of Lemma 6.1 hold for K = Kn (n ≥ n0 ) and for K = K∞ , for every parameter in I. Then the

2816

reductions on A = {2, . . . , M} satisfy
|S n (i, j) − S ∞ (i, j)| ≤ |Kn (i, j) − K∞ (i, j)| +

□

h
Cβm i
(L)
(L)
tn,k
(i, j) − t∞,k
(i, j) + 4w′ (i) δL m2C m +
1−β
k<m
X

93


[page 94]
2817

for all m and L; hence S n → S ∞ uniformly on I. Moreover, for n ≥ n0 , ρ(Kn ) − 1 and ρ(S n ) − 1 have the

2818

same sign.

2819

Proof. The displayed bound follows from Lemma 6.1 applied to Kn and to K∞ . Each tk(L) is a finite sum of

2820

products of k + 2 coefficients, all at most 2, with indices at most L, so it converges uniformly on I. Given

2821

η > 0, choose m, then L, then n. For the signs: Kn,BB wB ≤ βwB , so ρ(Kn,BB ) ≤ β < 1 (Collatz–Wielandt), and

2822

Lemma 2.5 applies to the finite matrix Kn .

2823

Where the hypotheses come from. (a) is Proposition 5.1. (b) for Kn is Lemma 4.1 with w = ϕa , w′ = ϕa+1 ,

2824

δL = 1/(L + a); for K∞ it is Lemma 3.3(b) with the same weights.

2825

Corollary 6.3 (continuity in λ). Let I be a compact set of λ on which (a) and (b) hold with one cut M. Then

2826

λ 7→ K∞ (y, λ)( f, f ′ ), λ 7→ S ∞ (y, λ) and λ 7→ ρ(S ∞ (y, λ)) are continuous on I.

2827

Proof. For fixed n, the coefficients of Kn (θλ) are rational functions of q, hence continuous in λ; as ρ(Kn,BB ) ≤

2828

β uniformly on I, Lemma 6.1 makes λ 7→ S n (λ) continuous. Uniform limits of continuous functions are

2829

continuous, and ρ is continuous on matrices indexed by A.

2830

S13.7

2831


Fix θ > 0, y ∈ (0, 1) and ε > 0, and let U ∗ = max 0, − ln(θλc ) , λc = λc (y). From Section S13.3:

2832

ρ(S ∞ (y, λ)) < 1 for λ < λc and > 1 for λ ∈ (λc , 1) (Lemma 3.4); λc ≤ (1 + y)/2 < 1 (Lemma 3.5);

2833

λc > 21 (Lemma 3.6). The two bounds on ψ follow.

□

□

Proof of Theorem 4

2834

Upper bound. Let λmin = 1/(2 max(1, θ)) and λmax = e−ε min(λc , 1/θ).

2835

• For λ ≤ λmin , Λ ≤ 12 and ρ(Kn ) < 1 by Proposition 2.4.

2836

• On I = [λmin , λmax ] (if not empty), Λ = λ max(1, θ) ≤ e−ε =: Λ0 < 1. Choose an integer a > 1/(1 − Λ0 )

2837

and β ∈ (21−a(1−Λ0 ) , 1). Lemma 4.1 gives a cut for the Kn , and Lemma 3.3(b), with a and a + 1 (as

2838

λ ≤ Λ ≤ Λ0 ), gives one for K∞ ; take the larger, which is admissible for both. Proposition 5.1 gives (a)

2839

on I, and Lemma 6.2 gives S n → S ∞ uniformly on I. Since λmax < λc , ρ(S ∞ (λ)) < 1 on I (with this

2840

cut, by Lemma 2.6); by Corollary 6.3 and compactness, maxI ρ(S ∞ ) < 1. Hence ρ(S n (λ)) < 1 on I for

2841

n ≥ n1 , and ρ(Kn (θλ)) < 1 by Lemma 6.2.

2842

So for n ≥ n1 , ρ(Kn (e−U )) < 1 for every U ≥ − ln(θλmax ) = U ∗ + ε, and Uc (n, n/y, θ) ≤ U ∗ + ε.

2843

Lower bound. If θλc ≥ 1, then U ∗ = 0 and there is nothing to prove. Otherwise θλc < 1, and λc < 1

2844

(Lemma 3.5). Take λ′ ∈ (λc , λc (1 + ε)) with λ′ < 1 and θλ′ < 1. Then ρ(S ∞ (λ′ )) > 1 (Lemma 3.4) and Λ′ =

2845

λ′ max(1, θ) < 1. Lemma 6.2 with I = {λ′ } (Lemma 4.1 with Λ0 = Λ′ , Lemma 3.3(b), Proposition 5.1) gives

2846

ρ(S n (λ′ )) → ρ(S ∞ (λ′ )) > 1, hence ρ(Kn (θλ′ )) > 1 for n ≥ n2 and Uc (n, n/y, θ) ≥ − ln(θλ′ ) ≥ U ∗ − ln(1 + ε).

2847

As ε is arbitrary, Uc (n, n/y, θ) → U ∗ = max(0, ln(1/θ) + ψ(y)).

□

2848

Remark 7.1. No monotonicity of ρ(Kn ) in q is used at finite fecundity: the upper bound treats the whole

2849

interval I at once, through the uniformity of Lemma 6.2. (H3) is needed only when θ < 1: for θ ≥ 1, θλc < 1

2850

already forces λc < 1. The kernels of all θ with the same λ converge to the same K∞ (y, λ): this is the collapse

2851

in θ of the exact thresholds.

94


[page 95]
2852

S13.8

2853

R ≤ n (y ≥ 1). Lemma 4.1 holds for every y > 0. Proposition 5.1, (H2) and (H3) are not proved by

2854

the arguments of this section: the reduced size is no longer monotone, it can approach the division threshold

2855

without crossing it, and two coupled lineages no longer divide at the same time, so the coupling of Lemma 3.2

2856

is not available. (H2) is checked numerically on a truncation of the limit process, and (H3) is supported

2857

numerically. For y ≥ 1, even the existence of admissible cuts for every λ < 1, on which definition (4) rests,

2858

is not established here. The arguments of this section therefore do not prove the scaling law in this regime.

2859

SI S3 proves, by other arguments, (H3) and the convergence of the finite kernels at every y, and the existence

2860

of admissible cuts for every λ < 1; (H2) for y ≥ 1 is supported numerically only, so that for y ≥ 1 the limit

2861

holds under (H2), and without it only the bracket of SI S3 is proved.

2862

Identification. That λc (y), defined through the Schur reduction of the limit kernel, is the threshold obtained

2863

by direct simulation of the limit process (Table S3) is checked numerically, by independent routes, not

2864

proved.

2865

Consequences for the fecundity.

2866

What remains open, and numerical checks

At θ = 1, as U → ln 2, Theorem 4 and the slope of ψ at y = 0, ψ(y) =
√

3 2−4
ln 2 + o(1) /(ln 2 − U);

√
ln 2 − 3 ln2−4
2 y + o(y), proved in S14 (Theorem S), give lim supn→∞ Rmin /n ≤

2867

this is asymptotic in U, with constants far from effective. At every U < ln 2, Lemma 3.5 already gives

2868

lim supn→∞ Rmin /n ≤ 1/(eln 2−U − 1); that about 0.35 n/(ln 2 − U) suffices away from this limit rests on the

2869

computed ψ. That no smaller fecundity suffices, which would make Rmin ≈ 0.35 n/(ln 2 − U) an asymptotic

2870

equivalence, remains derived: it would require a one-sided bound on Uc uniform in y, a bound sup ψ < ln 2

2871

away from y = 0, and a bound on Uc uniform in R ≤ n, including bounded R. Theorem Q (SI S3) gives such

2872

a necessary bound at every n ≥ 25, Rmin > (κQ /3) n/(ln 2 − U) when ln 2 − U ≤ κQ /3, but with a constant

2873

κQ ≈ 2 × 10−7 .

2874

Numerical checks

2875

(n = 200), the generator inequalities (7) hold to rounding (7 × 10−13 relative to the total jump rate times V or

2876

W2 ); the bound (14) is never exceeded (ratio at most 0.53); at y = 0.5 the coefficient error max f, f ′ ≤12 |Kn −K∞ |

2877

decreases as 1/n. At y = 0.5, λc = 0.569723, and for n = 200, ρ(Kn ) is 0.927, 0.944, 0.951 at λc − 0.03 and

2878

1.032, 1.056, 1.066 at λc +0.03 for θ = 0.5, 1, 1.5. These checks were reproduced with independently written

2879

code (finite chain, finite kernels and limit kernel). The same code shows that, on the domain and with the

2880

constants of Step 1 of Proposition 5.1, the derivative bounds are reached to at most 11% and 0.7% of their

2881

value (y = 0.5 and 0.9, λ = 0.6, F ≤ 30), and that a Richardson extrapolation of the finite kernels (n = 100,

2882

200, 400; up to 318 801 states) recovers the limit kernel to 3.8 × 10−6 without using the size clock.

2883

S14. The slope of ψ at y = 0 (Theorem S)

(scripts and logs in the code deposit). On exact finite kernels with up to 79 401 states

2884

√
This section proves that ψ(y) = ln 2 − c1 y + o(y), c1 = (3 2 − 4)/ ln 2 (provenance: S7); c1 is the constant a

2885

of SI S3 (ii). Its notation is that of S13; κ, Ψy and Ψ0 are local to it.

95


[page 96]
2886

S14.1

2887

We use the setting of S13, the proof of Theorem 4 for R > n, cited as [S13]: the limit process, the weights

2888

ϕa (F) = Γ(F − 1 + a)/Γ(F − 1), the Schur reductions S (t) on a cut M, admissible cuts, and the threshold

2889

λc (y) of the limit kernel K∞ (y, λ), defined in [S13, Eq. (4)] by the sign of ρ(S ∞ (y, λ)) − 1 on an admissible

2890

cut; ψ(y) = − ln λc (y). For 0 < y < 1, Theorem 4 gives limn→∞ Uc (n, n/y, θ) = max(0, ln(1/θ) + ψ(y)), with

2891

ln(2/(1 + y)) ≤ ψ(y) < ln 2; in particular ψ(y) → ln 2 as y → 0. We compute the slope of ψ at y = 0.

2892
2893

Statement and plan

√
Theorem S (slope of ψ at y = 0). Let m(λ) = 2λ−1 (2 − 2λ )2 , m0 = m( 21 ) = 3 2 − 4, a0 = m0 /(2 ln 2) and
c1 = m0 / ln 2.

2894

(a) The spine. For λ ∈ (0, 1), the Doob transform P̃ of the kernel K0 at y = 0 by ϕ2 (the protocell that

2895

carries a marked pair of replicases) is an irreducible stochastic matrix whose unique stationary law ν

2896

is that of 2 + NegBin(3, π), π = 21−λ − 1. Hence Eν [1/F] = π/2 and m(λ) = 2(2 − 2λ ) 22λ−1 Eν [1/F].

2897

(b) The Perron root. Let J = [0.45, 0.55], ηmax = 0.1 and ζmax = ηmax ln 2. For every ζ ∈ (0, ζmax ] there

2898

is an explicit y′1 (ζ) > 0 such that, for 0 < y ≤ y′1 (ζ) and every λ ∈ J, the Perron root r(y, λ) = 1/t∗

2899

of K∞ (y, λ) (Definition 2.1: t∗ is the value of t at which the Schur reduction of tK∞ (y, λ) has spectral

2900

radius 1) exists and
r(y, λ) − 22λ−1 + m(λ) y ≤ ζ y.
Moreover |r(y, λ) − 22λ−1 + m(λ)y| ≤ A1 y2 for 0 < y ≤ y1 and λ ∈ J.

2901

2902

(c) The threshold. For every η ∈ (0, ηmax ] there is an explicit y1 (η) > 0 such that
1
2 + (a0 − η) y

≤ λc (y) ≤ 12 + (a0 + η) y

(0 < y ≤ y1 (η)).

Moreover |λc (y) − 12 − a0 y| ≤ A2 y2 and |ψ(y) − ln 2 + c1 y| ≤ A3 y2 for 0 < y ≤ y1 .

2903

2904

The constants are explicit (Section S14.8): A1 ≈ 4.98 × 107 , A2 ≈ 7.18 × 107 , A3 ≈ 1.44 × 108 and

2905

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

2906

The constants of the remainder are about 109 times too large: numerically, λc (y) − 21 − a0 y ≈ −0.085 y2

2907

and ψ(y) − ln 2 + c1 y ≈ +0.231 y2 (Section S14.10). They only establish the existence and the form of the

2908

remainder. The consequences for Uc and for the fecundity Rmin required near the ceiling are in Section S14.9.

2909

Write ε = ln(2/θ) − U for the distance to the ceiling. At every ε < min(ln 2, ln(2/θ)), Corollary 9.2(i) gives

2910

lim supn→∞ Rmin /n ≤ 1/(eε − 1); the bound with the constant c1 is proved only asymptotically, as ε → 0

2911

(Corollary 9.2(ii) and the comments after it).

2912

Plan.

2913

problem is a perturbation of this eigenvalue. On an infinite set of types an unbounded positive eigenfunction

2914

does not by itself fix a spectral radius, and we do not use spectral perturbation theory: we construct explicit

2915

super- and subsolutions and conclude with [S13, Lemmas 2.7, 2.8 and 3.4], as in [S13, Lemma 3.6].

At y = 0 the cycle is a Yule process, and ϕ2 is an exact eigenfunction of K0 , with eigenvalue 22λ−1 ; the

96


[page 97]
2916

(i) In the time v = u/y ∈ [1, 2], the cycles at y > 0 and at y = 0 live on the same interval, and their

2917

jump rates differ by O(y) uniformly in the number of replicases; a Duhamel formula compares them

2918

(Section S14.3).

2919

(ii) The exact pair-density identity of [S13, Lemma 3.6] has a first-order term y ℓ, with a remainder O(y2 )
uniformly in the type (Section S14.4).

2920

2921

(iii) The protocell that carries a marked pair of replicases (the spine) has an explicit stationary law; it fixes

2922

the slope m(λ), and the Poisson equation (K0 − 22λ−1 )h = ℓ − m(λ)ϕ2 has a solution of logarithmic

2923

relative growth, built from the hitting times of the spine chain (Section S14.5).

2924

(iv) ϕ2 + yh + κyϕ3 and (ϕ2 + yh − κyϕ3 )+ are a super- and a subsolution of K∞ ; the drift of ϕ3 [S13, Lemma

2925

3.3(a)] controls the large types (Sections S14.6 and S14.7). Section S14.8 concludes, with the order of

2926

the choices and the constants.

2927

Results used.

2928

of λc ), Lemmas 2.6 (independence of the cut), 2.7 (subsolutions) and 2.8 (supersolutions), Lemmas 3.1 (size

2929

clock), 3.3(a) (drift of ϕ3 ), 3.4 (one crossing), 3.5 (ψ ≥ ln(2/(1 + y))) and 3.6 (ψ < ln 2), and Theorem 4; they

2930

are proved there. Kac’s formula for positive recurrent chains is classical. Everything else is proved below.

2931

S14.2

2932

The cycle in the time v.

2933

the number F of replicases of a living lineage is a birth–death chain with rates λF(F − 1)/(s(F − s)) and

2934

F/(F − s), absorbed at F = 1, and every living lineage divides at s = 2y. Let v = s/y ∈ [1, 2]. Since ds = y dv,

2935

the rates per unit of v are, for F ≥ 2,

From [S13]: Section 2 (limit process, weights, Schur reductions, admissible cuts, definition

Setting: the cycle in the time v, the cut, the Perron root
Fix y ∈ (0, 1) and λ ∈ (0, 1). By [S13, Lemma 3.1], in the time s = u ∈ [y, 2y]

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

2936

We write X = (Xv )v∈[1,2] for this chain, E j for its law from X1 = j, Lv g(F) = by (F, v)[g(F + 1) − g(F)] +

2937

dy (F, v)[g(F − 1) − g(F)] for F ≥ 2 and Lv g(1) = 0, and Py g( j) = E j [g(X2 )]; functions of the state always

2938

satisfy g(0) = g(1) = 0 (dead states). Then

y

Ky g( f ) = 2

X

y

P(B f = j) Py g( j),

B f ∼ Bin( f, 12 ),

(19)

j≥2
2939

is Ky = K∞ (y, λ) [S13, Lemma 3.1]: a linear change of time does not change the type at division. The same

2940

formulas at y = 0 give b0 (F, v) = λ(F − 1)/v and d0 = 0: in the time ln v ∈ [0, ln 2], F − 1 is a Yule process

2941

of rate λ, and K0 is the kernel of the limit n → ∞ at R = ∞ (Theorem 1 of the main text).

2942

Notation and fixed choices. ϕ1 (F) = F − 1, ϕ2 (F) = F(F − 1), ϕ3 (F) = (F − 1)F(F + 1) = (F + 1)ϕ2 (F);

2943

for F ≥ 2, ϕa (F + 1) − ϕa (F) = aϕa (F)/(F − 1), and ϕa is nondecreasing. ρ0 (λ) = 22λ−1 and σ(y, λ) =

2944

ρ0 (λ) − y m(λ). Once and for all: J = [λ− , λ+ ] = [0.45, 0.55], y0 = 1/20, ηmax = 0.1, ζmax = ηmax ln 2,

2945

M = 40, f0 = 8. Throughout, λ ∈ J and 0 < y ≤ y0 . The constants below depend neither on λ ∈ J nor on y

2946

(they are bounds over λ ∈ J and y ∈ (0, y0 ]), and each is computed from the exact values of those it involves,

2947

not from the rounded values displayed.
97


[page 98]
2948

The cut. Let C3 = 23λ+ −1 = 1.569168 and β3 = 23λ+ −2 (M + 5)/(M + 2) = 0.840626. By [S13, Lemma

2949

3.3(a)], (Ky ϕ3 )( f ) ≤ 23λ−2 ff +4
+1 ϕ3 ( f ) for 0 < y < 1; hence Ky ϕ3 ≤ β3 ϕ3 on B = { f > M} and Ky ϕ3 ≤ C 3 ϕ3

2950

everywhere. At y = 0 this holds with equality: ϕ3 is an eigenfunction of the Yule semigroup (Lemma 3.3(a)

2951

below), and E[(B f )i ] = ( f )i 2−i , so that K0 ϕ3 ( f ) = 23λ−2 f ( f − 1)( f + 4). The weight ϕ3 is nondecreasing and

2952

≥ max(1, ϕ2 ) on the types: the cut M = 40 is admissible for Ky , with w = ϕ3 , β = β3 and C = C3 , for every

2953

λ ∈ J and 0 ≤ y < 1. Let A = {2, . . . , M}; then ϕ3 ≤ (M + 1)ϕ2 on A and ϕ3 ≥ (M + 2)ϕ2 on B.

2954
2955

The Perron root. The coefficients of Ky,AA are positive [S13, Lemma 3.1]. Hence every coefficient of
P
k K
S y,λ (t) = tKAA + k≥0 tk+2 KAB KBB
BA is a power series in t with nonnegative coefficients, convergent on

2956

[0, 1/β3 ) and strictly increasing; for matrices with positive coefficients, S ≤ S ′ entrywise with S , S ′

2957

implies ρ(S ) < ρ(S ′ ). So t 7→ ρ(S y,λ (t)) is continuous and strictly increasing on [0, 1/β3 ), and vanishes at 0.

2958

Definition 2.1 (Perron root). If there is t∗ ∈ (0, 1/β3 ) with ρ(S y,λ (t∗ )) = 1, it is unique, and r(y, λ) = 1/t∗ .

2959

When r(y, λ) exists, ρ(S y,λ (1)) > 1 if and only if r(y, λ) > 1, and ρ(S y,λ (1)) < 1 if and only if r(y, λ) < 1.

2960

By [S13, Lemma 2.6] applied to the kernel tK∞ (weight ϕ3 , M0 = 40, constant tβ3 < 1), the sign of ρ(S (t))−1

2961

is the same on every cut M ′ ≥ 40, and, through a common cut beyond both, on every admissible cut (w′ , β′ )

2962

with t < 1/β′ (cuts M ′ < 40 with the weight ϕ3 included): r is the same for every admissible cut whose

2963

domain [0, 1/β′ ) contains t∗ . Only the sign at t = 1 enters the definition of λc , and that is [S13, Lemma 2.6]

2964

itself. The Perron root r(y, λ) is the precise meaning we give to “ρ(K∞ (y, λ))” in the first-order expansion.

2965

Lemma 2.2 (super- and subsolutions). Let K ≥ 0 have an admissible cut M (weight w, constant β), with

2966

Schur reduction S (t).

2967

(a) If v ≥ 0, v > 0 on A, v ≤ Cw and Kv ≤ s v on all types, with s > β, then ρ(S (1/s)) ≤ 1.

S13, Lemma
2968
2.7 If v ≥ 0, v ≤ Cw, v is not identically zero on A, t ∈ (0, 1/β), tKv ≥ v on B and tKv ≥ (1 + η)v on A,
then ρ(S (t)) ≥ 1 + η.

2969

2972

Proof. (a) is the first half of the proof of [S13, Lemma 2.8], which uses s < 1 only afterwards. Let t = 1/s ∈
P
(0, 1/β). From tKv ≤ v on B we get, by iteration and positivity, vB ≥ k<m (tKBB )k tKBA vA for every m, hence
P
vB ≥ k≥0 (tKBB )k tKBA vA ; on A, vA ≥ tKAA vA + tKAB vB ≥ S (t)vA , and the Collatz–Wielandt inequality for

2973

the finite matrix S (t), with vA > 0, gives ρ(S (t)) ≤ 1. (b) is [S13, Lemma 2.7].

2974

S14.3

2975

Lemma 3.1 (rates). For 0 ≤ y ≤ 12 , v ∈ [1, 2] and F ≥ 2: (i) 0 ≤ by − b0 = λy(F − 1)/(F − yv) ≤ λy; (ii)

2976

0 ≤ dy ≤ y/(1 − y); (iii) by ≤ λ(F − 1)/(v(1 − y)).

2970
2971

2977
2978

□

Rates, moments and a Duhamel formula

Proof. F − yv ≥ F − 2y ≥ F(1 − y) since F ≥ 2, and F − yv ≥ F − 1 since yv ≤ 2y ≤ 1. Then
 λy(F−1)
F
by − b0 = λ(F−1)
□
v
F−yv − 1 = F−yv .

2979

A protocell with F replicases lasts about y/F in the time t and loses replicases at rate F: it loses about y

2980

replicases per cycle, whatever its size, and the same holds for the excess births. This is why all the bounds

2981

below are uniform in F.

2982

Lemma 3.2 (moments). For 0 ≤ y ≤ 12 , a ≥ 1, j ≥ 1 and v ∈ [1, 2], E j [ϕa (Xv )] ≤ vaλ/(1−y) ϕa ( j).

y

98


[page 99]
y

2983

aλ
Proof. For F ≥ 2, ϕa (F − 1) ≤ ϕa (F) and, by Lemma 3.1(iii), Lv ϕa (F) ≤ by aϕa (F)/(F − 1) ≤ v(1−y)
ϕa (F);

2984

at F = 1 both sides vanish. The chain does not explode and supv Xv has moments of all orders [S13, Lemma

2985
2986

3.1], so Dynkin’s formula applies to ϕa (Xv ) (localise at the first passage above N, then let N → ∞ by
R v aλ
y
µ(w) dw, and
dominated convergence). The function µ(v) = E j [ϕa (Xv )] satisfies µ(v) ≤ ϕa ( j) + 1 w(1−y)
□

2987

Gronwall’s lemma concludes.

2988

Lemma 3.3 (a Duhamel formula). Let a ≥ 1, c ≥ 0, g a function on {1, 2, . . . } with g(1) = 0 and |g| ≤ c ϕa ,

2989

and v1 ∈ (1, 2]. For w ∈ [1, v1 ] let G(w, F) = E0 [g(Xv1 ) | Xw = F] (Yule semigroup).

2990

(a) E0 [ϕa (Xv1 ) | Xw = F] = (v1 /w)aλ ϕa (F); hence |G(w, F)| ≤ c (v1 /w)aλ ϕa (F).

2991

(b) For 0 < y ≤ 21 and j ≥ 1,
y
y
E j [g(Xv1 )] − E0j [g(Xv1 )] = E j

Z v1
1


y
Lw − Lw0 G(w, ·)(Xw ) dw,

y

2992

where, for F ≥ 2, (Lw − Lw0 )G(F) = (by − b0 )(F, w) [G(w, F + 1) − G(w, F)] + dy (F, w) [G(w, F − 1) −

2993

G(w, F)], and 0 at F = 1.

2994

Proof. (a) Under P0 and in the time τ = ln w, X − 1 is a Yule process of rate λ, with generator Lg(F) =

2995

λ(F − 1)[g(F + 1) − g(F)]. Since ϕa (F + 1) − ϕa (F) = aϕa (F)/(F − 1), Lϕa = aλϕa for every real

2996
2997
2998
2999
3000

a > 0; the Yule process has moments of all orders, so E0 [ϕa (Xv1 ) | Xw = F] = eaλ ln(v1 /w) ϕa (F). (b)
P
G(w, F) = F ′ pln(v1 /w) (F, F ′ ) g(F ′ ), with negative binomial transition probabilities, smooth in w and dominated through (a): G is C 1 in w and satisfies the backward equation ∂wG + Lw0 G = 0. Dynkin’s fory

mula for X under Py , applied to the time-dependent function G(w, Xw ), gives E j [G(v1 , Xv1 )] − G(1, j) =
R
R
y
y
y v
y v
E j 1 1 (∂w + Lw )G(w, Xw ) dw = E j 1 1 (Lw − Lw0 )G(w, Xw ) dw. It is justified as in Lemma 3.2: up to the first

3001

passage above N the chain lives on a finite set with bounded rates, and one lets N → ∞ by dominated con-

3002

vergence, with |G| + |∂wG| + |LwG| ≤ c′ (1 + supv Xv )a+1 , integrable [S13, Lemma 3.1]. Finally G(v1 , ·) = g

3003

and G(1, j) = E0j [g(Xv1 )].

3004

S14.4

3005

Lemma 4.1 (exact identity). For 0 < y ≤ 12 , λ ∈ (0, 1) and f ≥ 2, Ky ϕ2 = ρ0 ϕ2 − ℓy , with

y

□

The exact identity and its first order

ℓy ( f ) = 2

2λ+2

(1 − λ) y E Ψy (B f ) ,




y
Ψy ( j) = E j

Z 2
1

ϕ2 (Xv ) v−2λ
dv
Xv − yv

3006

(the integrand vanishes when Xv = 1, and Ψy (0) = Ψy (1) = 0).

3007

Proof. Let Z(v, F) = ϕ2 (F)v−2λ . For F ≥ 2, a birth adds 2F to ϕ2 and a death removes 2(F − 1), so
h 2λϕ2
i 2ϕ2 v−2λ h λ(F − yv) λF
i
y
(∂v + Lv )Z = v−2λ −
+ 2F by − 2(F − 1) dy =
−
+
−y
v
F − yv
v
v
−2λ
2(1 − λ) y ϕ2 (F) v
=−
,
F − yv
y

3008

and both sides vanish at F = 1. Dynkin’s formula (justified as in Lemma 3.2) gives 2−2λ E j [ϕ2 (X2 )] =

3009

ϕ2 ( j) − 2(1 − λ)y Ψy ( j). With E[ϕ2 (B f )] = ϕ2 ( f )/4 and two daughters, Ky ϕ2 ( f ) = 22λ−1 ϕ2 ( f ) − 22λ+2 (1 −

3010

λ)y E[Ψy (B f )].

□
99


[page 100]
3011
3012

3013

This is the identity of [S13, Lemma 3.6] in the time v (the loss written ℓ there is ℓy here): there,
R
with Z = F(F − 1)u−2λ , equals y1−2λ ϕ2 (F)v−2λ (F − yv)−1 dv, and (2y)2λ y1−2λ = 22λ y.

3015

3016

Z dt,

Lemma 4.2 (first order of the loss). For 0 < y ≤ 21 , λ ∈ (0, 1) and f ≥ 2, ℓy = y ℓ + ry , with

ℓ( f ) = 2λ+1 (2 − 2λ ) f − 2 + 21− f = 2(2 − 2λ ) (K0 ϕ1 )( f ),

3014

R

|ry ( f )| ≤ Cr y2 ,

R2
R2


2−2λ
1
v−2λ (v − vλ ) dv =
where Cr = 22λ+2 (1 − λ) J1 + J2 /(1 − y) , J1 = 1 v1−2λ dv = 2 2−2λ−1 and J2 = 1−λ
1
h
i
√
1−λ
1
2 −1
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

3017

Then ℓ( f ) := 22λ+2 (1 − λ)E[Ψ0 (B f )] = 22λ+2 (21−λ − 1) E[(B f − 1)+ ], with E[(B f − 1)+ ] = f /2 − 1 + 2− f and

3018

22λ+1 (21−λ − 1) = 2λ+1 (2 − 2λ ). Also K0 ϕ1 ( f ) = 2 E[2λ (B f − 1)+ ] = 2λ+1 E[(B f − 1)+ ].

3019

The remainder. ry ( f ) = 22λ+2 (1 − λ) y E[Ψy (B f ) − Ψ0 (B f )], and Ψy ( j) − Ψ0 ( j) = D1 ( j) + D2 ( j) with
y
D1 = E j

3020
3021
3022
3023

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
y
y v
hence (E j − E0j )ϕ1 (Xv ) = E j 1 (v/w)λ [(by − b0 ) − dy ](Xw , w) 1{Xw ≥ 2} dw. By Lemma 3.1 the bracket lies in
Rv
[−y/(1 − y), λy], and 1 (v/w)λ dw = (v − vλ )/(1 − λ), so |D2 | ≤ yJ2 /(1 − y). Thus |Ψy − Ψ0 | ≤ y(J1 + J2 /(1 − y))

3024

uniformly in j, and |ry | ≤ Cr y2 .

3025

Remark 4.3. The remainder is bounded uniformly in the type. A heuristic computation, by a law of large

3026

numbers in F (for large f , Xv is large, (F − 1)/(F − yv) → 1 in D1 and (by − b0 ) − dy → −(1 − λ)y in D2 ),

3027

gives ry ( f )/y2 → 22λ+2 (21−λ − 1) as f → ∞, that is 3.314 at λ = 12 ; numerically, ry ( f )/y2 increases from

3028

0.279 ( f = 2) to 3.261 ( f = 150), independently of y.

3029

S14.5

3030

Let P̃( f, f ′ ) = K0 ( f, f ′ )ϕ2 ( f ′ )/(ρ0 ϕ2 ( f )) on the types {2, 3, . . . }. Since K0 ϕ2 = ρ0 ϕ2 (Lemma 3.3(a) and

3031

E[ϕ2 (B f )] = ϕ2 ( f )/4), P̃ is a stochastic matrix, and

□

The spine, the slope and the Poisson equation

K0 (ϕ2 ζ) = ρ0 ϕ2 P̃ζ
3032

whenever P̃|ζ| < ∞.

(20)

Lemma 5.1 (the spine; Theorem S(a)). Let λ ∈ (0, 1), p = 2−λ and π = 21−λ − 1.
(a) From f , P̃ draws j = 2 + Bin( f − 2, 12 ), then X ′ + 1 =

P j+1

3034

i=1 G i , with independent G i , geometric on
{1, 2, . . . } with parameter p. It is irreducible, and P̃( f, 2) = 22− f −3λ .

3035

(b) Its unique stationary law ν is that of 2 + NegBin(3, π) (the number of failures before the third success,

3033

3036

with success probability π), and Eν [1/F] = π/2. In particular P̃ is positive recurrent.

3037

(c) ℓ/ϕ2 = 2(2 − 2λ ) ρ0 P̃(1/F), and m(λ) := ν(ℓ/ϕ2 ) = 2(2 − 2λ ) ρ0 Eν [1/F] = 2λ−1 (2 − 2λ )2 .
100


[page 101]
3038

Proof. (a) Weighted by ϕ2 , the partition gives P(B f = j) j( j−1) = f ( f4−1) P(Bin( f −2, 12 ) = j−2): the daughter

3039

keeps the marked pair, and each other replicase with probability 12 . Weighted by ϕ2 , the Yule growth jumps

3040

from F to F + 1 at rate λ(F − 1)ϕ2 (F + 1)/ϕ2 (F) = λ(F + 1) per unit of ln v: F + 1 is a Yule process of

3041

rate λ during ln 2, started from j + 1 individuals, each of which has a geometric number of descendants with

3042
3043
3044
3045
3046
3047
3048
3049

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

3050

ν(P̃ζ) = ν(ζ) for bounded ζ, and (b) give the second: 2(2 − 2λ ) 22λ−1 (21−λ − 1)/2 = 2λ−1 (2 − 2λ )2 .

3051

Lemma 5.2 (the Poisson equation). Let λ ∈ J and ĝ = (ℓ/ϕ2 − m)/ρ0 .

3052

3053
3054
3055

(a) ∥ĝ∥∞ ≤ ḡ := max(m, cℓ /4 − m)/ρ0 , with cℓ = 2λ+1 (2 − 2λ ), and ν(ĝ) = 0. On J, ḡ ≤ 0.294212.


(b) Let W( f ) = ln( f + 1), C = {2, . . . , f0 − 1}, δ = − ln 2λ+ −1 ( f0 + 4)/( f0 + 1) , a′0 = 23− f0 −3λ+ and

W̄ = ln 2λ+ −1 ( f0 + 3) ; with f0 = 8, δ = 0.0242342 > 0, a′0 = 0.0099575 and W̄ = 2.085979. For the
chain X̃ of transition P̃ and σ2 = inf{k ≥ 0 : X̃k = 2},
E f [σ2 ] ≤ W( f )/δ + (1 + W̄/δ)/a′0

3056
3057

3058
3059

□

(c) The function ĥ( f ) = −E f

Pσ2 −1
k=0

for every f ≥ 2.


ĝ(X̃k ) (so that ĥ(2) = 0) satisfies P̃ĥ − ĥ = ĝ and |ĥ( f )| ≤ ḡ E f [σ2 ] ≤

H0 + H1 ln( f + 1), with H1 = ḡ/δ = 12.1404 and H0 = ḡ(1 + W̄/δ)/a′0 = 2572.81.
(d) The function h = ϕ2 ĥ (with h(0) = h(1) = 0) satisfies (K0 − ρ0 )h = ℓ − m ϕ2 and |h| ≤ (H0 + H1 ln( f +
1)) ϕ2 ≤ Hϕ3 , with H = H0 /3 + H1 /e = 862.07.

3060

These constants are uniform in λ ∈ J.

3061

Proof. (a) ℓ( f )/ϕ2 ( f ) = cℓ ( f − 2 + 21− f )/( f ( f − 1)) ∈ (0, cℓ /4]: the inequality 4( f − 2 + 21− f ) ≤ f ( f − 1)

3062

reads f 2 − 5 f + 8 ≥ 4 · 21− f , which is an equality at f = 2, holds at f = 3 (2 ≥ 1), and persists since the left

3063

side increases and the right side decreases. So ĝ ∈ [−m/ρ0 , (cℓ /4 − m)/ρ0 ]; ν(ĝ) = 0 by Lemma 5.1(c).

3064

(b) E f [X̃ ′ + 1] = 2λ E[ j + 1] = 2λ−1 ( f + 4). By Jensen’s inequality, P̃W( f ) ≤ ln(2λ−1 ( f + 4)), and, for

3065

f ≥ f0 , since ( f + 4)/( f + 1) decreases and λ ≤ λ+ , P̃W( f ) ≤ W( f ) − δ. For f < C, W(X̃k∧σC ) + δ (k ∧ σC ) is a

3066

nonnegative supermartingale, σC being the hitting time of C; so δ E f [k ∧ σC ] ≤ W( f ) and E f [σC ] ≤ W( f )/δ.

3067

From x ∈ C, P̃(x, 2) = 22−x−3λ ≥ a′0 . At each visit to C, the next step reaches 2 with probability at least a′0 ,

3068

given the past (strong Markov property). An attempt costs one step and, if it fails, the return time to C from

3069
3070
3071
3072
3073
3074

X̃1 , of expectation at most E[W(X̃1 )]/δ ≤ P̃W(x)/δ ≤ W̄/δ, since P̃W(x) ≤ ln(2λ+ −1 (x+4)) ≤ W̄ for x ≤ f0 −1.
P
The first i attempts fail with probability at most (1 − a′0 )i , so E x [σ2 ] ≤ i≥0 (1 − a′0 )i (1 + W̄/δ) = (1 + W̄/δ)/a′0
for x ∈ C; the strong Markov property at σC concludes.


(c) By (b), E2 [τ2 ] = 1 + E2 EX̃1 [σ2 ] < ∞, where τ2 = inf{k ≥ 1 : X̃k = 2}, and Kac’s formula gives
P

P

ν(ζ) = E2 k<τ2 ζ(X̃k ) /E2 [τ2 ] for bounded ζ; as ν(ĝ) = 0, E2 k<τ2 ĝ(X̃k ) = 0. Let u = −ĥ. For f , 2,
the Markov property at time 1 gives u( f ) = ĝ( f ) + P̃u( f ) (Fubini: |ĝ| ≤ ḡ and E f [σ2 ] < ∞). At f = 2,
101


[page 102]
= −ĝ(2) = u(2) − ĝ(2), since u(2) = 0. So u − P̃u = ĝ everywhere, that is

3075

P̃u(2) = E2

3076

P̃ĥ − ĥ = ĝ; and |u( f )| ≤ ḡ E f [σ2 ].

3077

P

1≤k<τ2 ĝ( X̃k )



(d) By (20), the series converging absolutely since |ĥ| ≤ H0 + H1 W and P̃W < ∞, (K0 − ρ0 )h = ρ0 ϕ2 (P̃ĥ −

3078

ĥ) = ρ0 ϕ2 ĝ = ℓ − mϕ2 . Finally H0 ≤ (H0 /3)( f + 1) and ln( f + 1) ≤ ( f + 1)/e.

3079

Remark 5.3. (i) The slope is forced. If (K0 − ρ0 )h′ = ℓ − m′ ϕ2 with |h′ | ≤ C(1 + ln f )ϕ2 , then ĥ′ = h′ /ϕ2

3080

satisfies P̃ĥ′ − ĥ′ = (ℓ/ϕ2 − m′ )/ρ0 , and integrating against ν (ν(ln F) < ∞, νP̃ = ν) gives m′ = ν(ℓ/ϕ2 ).

3081

Since ν = π0 ϕ2 /⟨π0 , ϕ2 ⟩, where π0 = ν/ϕ2 ∝ (1 − π) f is a left eigenvector of K0 by (20), this is the first-order

3082

formula m = ⟨π0 , ℓ⟩/⟨π0 , ϕ2 ⟩. (ii) Numerically, ĥ ≥ 0, and ĥ( f ) ≈ 0.697 ln( f +1)−0.90 at λ = 21 (the predicted

3083

asymptotic slope is (m/ρ0 )/((1−λ) ln 2) = 0.700); sup f |ĥ|/(1+ln( f +1)) = 0.43 and max f ≤150 E f [σ2 ] = 35.7.

3084

On the types 3 ≤ f ≤ 150 and for λ = 0.45, 0.5 and 0.55, the bound of (b) exceeds E f [σ2 ] by a factor of 190

3085

to 660, and that of (c) exceeds |ĥ| by a factor of at least 900, which does not matter here.

3086

S14.6

3087
3088

3089
3090
3091
3092
3093

3094

□

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

3095

term it controls is multiplied by y.

3096

S14.7

3097

Constants. m̄ = max J m = 0.274509; smin = min J ρ0 − y0 m̄ − ζmax y0 = 0.915842 > β3 = 0.840626;

Supersolution and subsolution

 Cr
ΓA = (m̄ + ζmax ) H0 + H1 ln(M + 1) +
+ (M + 1) C P ≤ 2.869 × 105 ,
2
Cr
ΓB = (m̄ + ζmax ) H +
+ C P ≤ 7.273 × 103 .
6
3098

For ζ ∈ (0, ζmax ] let κ = ζ/(4C3 (M + 1)), and consider the following conditions on y ∈ (0, y0 ]:

3099

(S1) y ≤ ζ/(4ΓA );

3100

(S2) y ≤ κ(smin − β3 )/(2ΓB );

3101


(S3) y H0 + H1 ln(H1 /κ) < 1;

3102


(S4) y H0 + H1 ln(M + 1) + κ(M + 1) < 1.

3103

Proposition 7.1 (supersolution). Let λ ∈ J, ζ ∈ (0, ζmax ], y satisfy (S1)–(S3), and h = hλ be the function of

3104

Lemma 5.2. Then v+ = ϕ2 + y h + κy ϕ3 satisfies v+ > 0, v+ ≤ (1 + y(H + κ))ϕ3 , and Ky v+ ≤ s− v+ on all types,

3105

with s− = σ(y, λ) + ζy. Hence ρ(S y,λ (1/s− )) ≤ 1.

102


[page 103]
3106

Proof. By Lemmas 4.1, 4.2 and 5.2(d), Ky v+ = ρ0 ϕ2 − yℓ − ry + y(ρ0 h + ℓ − mϕ2 ) + y(Ky − K0 )h + κyKy ϕ3 ;

3107

since ρ0 − s− = y(m − ζ),

Ky v+ − s− v+ = −ζy ϕ2 + y2 (m − ζ) h − ry + y (Ky − K0 )h + κy Ky ϕ3 − s− ϕ3 .

3108

(21)

The term in m has cancelled: this is the role of the corrector h.
On A. Ky ϕ3 − s− ϕ3 ≤ C3 ϕ3 ≤ C3 (M + 1)ϕ2 ; |h| ≤ (H0 + H1 ln(M + 1))ϕ2 ; |ry | ≤ Cr y2 ≤ C2r y2 ϕ2 , as ϕ2 ≥ 2;

3109
3110

|(Ky −K0 )h| ≤ C P yϕ3 ≤ C P (M +1)yϕ2 . Since κC3 (M +1) = ζ/4, Ky v+ − s− v+ ≤ yϕ2 [−ζ +ζ/4+yΓA ] ≤ − 2ζ yϕ2

3111

by (S1).

3112

On B. Ky ϕ3 ≤ β3 ϕ3 and s− ≥ min J ρ0 − y0 m̄ ≥ smin , so κy(Ky ϕ3 − s− ϕ3 ) ≤ −κy(smin − β3 )ϕ3 ; with

3113

|h| ≤ Hϕ3 , |ry | ≤ C6r y2 ϕ3 (as ϕ3 ≥ 6) and Lemma 6.1, Ky v+ − s− v+ ≤ −ζyϕ2 + y2 ΓB ϕ3 − κy(smin − β3 )ϕ3 ≤

3114

−ζyϕ2 − 2κ (smin − β3 ) yϕ3 < 0 by (S2).

Positivity. v+ = ϕ2 [1 + yĥ + κy( f + 1)] ≥ ϕ2 [1 − yH0 + y(κ( f + 1) − H1 ln( f + 1))], and κx − H1 ln x ≥

3115
3116

H1 (1 − ln(H1 /κ)) for x > 0; so v+ ≥ ϕ2 [1 − y(H0 − H1 + H1 ln(H1 /κ))] > 0 by (S3).

3117

Finally v+ ≤ ϕ2 + yHϕ3 + κyϕ3 , s− ≥ smin > β3 , and Lemma 2.2(a) applies.

□

3118

Proposition 7.2 (subsolution). Let λ ∈ J, ζ ∈ (0, ζmax ], and let y satisfy (S1), (S2) and (S4). Then v− =

3119

(ϕ2 + y h − κy ϕ3 )+ satisfies 0 ≤ v− ≤ (1 + yH)ϕ3 and v− > 0 on A, and, with s+ = σ(y, λ) − ζy and

3120

ζ/2
, Ky v− ≥ s+ v− on all types and Ky v− ≥ (s+ + ζ ′ y) v− on A. Hence ρ(S y,λ (1/s+ )) ≥
ζ ′ = 1+y(H0 +H
1 ln(M+1))

3121

1 + ζ ′ y/s+ > 1.

3122

Proof. Let u = ϕ2 + yh − κyϕ3 , so that v− = u+ ≥ u and Ky v− ≥ Ky u (Ky ≥ 0 and Ky |u| < ∞). As for (21),

3123

with ρ0 − s+ = y(m + ζ),

Ky u − s+ u = ζy ϕ2 + y2 (m + ζ) h − ry + y (Ky − K0 )h − κy Ky ϕ3 − s+ ϕ3 .

3124

(22)

On A, with the same bounds as above, Ky u − s+ u ≥ yϕ2 [ζ − ζ/4 − yΓA ] ≥ 2ζ yϕ2 by (S1). On B, s+ ≥ smin ,

3125

so −κy(Ky ϕ3 − s+ ϕ3 ) ≥ κy(smin − β3 )ϕ3 , and Ky u − s+ u ≥ ζyϕ2 − y2 ΓB ϕ3 + κy(smin − β3 )ϕ3 ≥ 0 by (S2). So

3126

Ky u ≥ s+ u everywhere: on {u > 0}, Ky v− ≥ Ky u ≥ s+ u = s+ v− , and on {u ≤ 0}, Ky v− ≥ 0 = s+ v− . On A,

3127

u ≥ ϕ2 [1 − y(H0 + H1 ln(M + 1)) − κy(M + 1)] > 0 by (S4), so that v− = u ≤ ϕ2 (1 + y(H0 + H1 ln(M + 1)))

3128

there, and Ky v− ≥ s+ v− + 2ζ yϕ2 ≥ (s+ + ζ ′ y) v− . Lemma 2.2(b), with t = 1/s+ ∈ (0, 1/β3 ) (as s+ ≥ smin > β3 )

3129

and η = ζ ′ y/s+ , concludes.

3130

Corollary 7.3 (bracket of the Perron root). If λ ∈ J, ζ ∈ (0, ζmax ] and y satisfies (S1)–(S4), then r(y, λ) exists

3131

and

□

σ(y, λ) − ζy < r(y, λ) ≤ σ(y, λ) + ζy.
3132

Proof. By Proposition 7.2, ρ(S (1/s+ )) > 1; since ρ(S (t)) is continuous and vanishes at 0, there is t∗ ∈

3133

(0, 1/s+ ) with ρ(S (t∗ )) = 1, and r = 1/t∗ > s+ . By Proposition 7.1, ρ(S (1/s− )) ≤ 1, and the strict increase of

3134

ρ(S (t)) gives t∗ ≥ 1/s− , that is r ≤ s− .

3135

S14.8

3136

(a) is Lemma 5.1.

□

Proof of Theorem S; the order of the choices and the constants

103


[page 104]
3137

(b) For ζ ∈ (0, ζmax ], let y′1 (ζ) ∈ (0, y0 ] be such that (S1)–(S4) hold on (0, y′1 (ζ)] (each is a condition y ≤

3138

or y < a threshold; take for instance half the smallest threshold). Corollary 7.3, applied to each λ ∈ J (the

3139

conditions do not depend on λ), gives |r(y, λ) − 22λ−1 + m(λ)y| ≤ ζy for 0 < y ≤ y′1 (ζ). Now take ζ = A1 y,

3140

with

3141

Then (S1) and (S2) hold by definition of A1 ; ζ ≤ ζmax means y ≤ ζmax /A1 = 1.3928 × 10−9 =: y1 ; and

3142

(S3), (S4) hold at y = y1 (their left sides are below 4 × 10−6 ) and therefore for 0 < y ≤ y1 , since y 7→ y(H0 +

3143

H1 ln(c/y)) increases for y < c/e, with c = 4C3 (M +1)H1 /A1 = 6.3×10−5 . So |r(y, λ)−22λ−1 +m(λ)y| ≤ A1 y2

3144

for 0 < y ≤ y1 and λ ∈ J.

3145

(c) Let η ∈ (0, ηmax ] and ζ = η ln 2, and let y1 (η) ∈ (0, y′1 (ζ)] be such that, in addition, (S5) (a0 + η) y ≤ 0.05

3146

and (S6) y < η ln 2/C s , with C s = 0.2530, hold on (0, y1 (η)]. Let 0 < y ≤ y1 (η) and λ± = 12 + (a0 ± η)y; by

3147

(S5), λ± ∈ J.

3148
3149


8C3 (M + 1)ΓB 
A1 = max 4ΓA ,
= 4.9766 × 107 .
smin − β3

• The expansion of σ. As 2a0 ln 2 = m0 , ρ0 (λ± ) = e(m0 ±2η ln 2)y . With e x ≤ 1 + x + 21 x2 e|x| , e x ≥ 1 + x, and
|m(λ) − m0 | ≤ |m′ | J |λ − 21 |, where m′ (λ) = ln 2 · 2λ−1 (2 − 2λ )(2 − 3 · 2λ ) and |m′ | J ≤ 0.6506,
σ(y, λ− ) + ζy ≤ 1 − η ln 2 · y + C ′s y2 ,

3150

σ(y, λ+ ) − ζy ≥ 1 + η ln 2 · y − C ′′s y2 ,

with C ′s = 21 (m0 + 2ηmax ln 2)2 e(m0 +2ηmax ln 2)y0 + |m′ | J (a0 + ηmax ) ≤ 0.2530 and C ′′s = |m′ | J (a0 + ηmax ) ≤

3151

0.1790. By (S6), s− = σ(y, λ− ) + ζy < 1 < s+ = σ(y, λ+ ) − ζy. The terms in m0 cancel exactly: this is

3152

where the value of the slope enters.

3153

• Below the threshold. Proposition 7.1 at λ− gives ρ(S (1/s− )) ≤ 1, with 1/s− > 1; by the strict increase in

3154

t (or directly by [S13, Lemma 2.8], since s− ∈ (β3 , 1)), ρ(S ∞ (y, λ− )) = ρ(S (1)) < 1. By [S13, Lemma

3155

3.4], no λ ≤ λ− satisfies ρ(S ∞ (y, λ)) > 1. So λc (y) ≥ λ− .

3156
3157

• Above the threshold. Proposition 7.2 at λ+ gives ρ(S (1/s+ )) > 1, with 1/s+ < 1; so ρ(S ∞ (y, λ+ )) > 1,
and λc (y) ≤ λ+ by definition.

3158

• The cut. Both statements are made on the cut M = 40 with weight ϕ3 , admissible for K∞ (y, λ± ); by

3159

[S13, Lemma 2.6], the sign of ρ(S ∞ ) − 1 is the same on every admissible cut. These are statements on

3160

the λc (y) of [S13], exactly.

3161
3162

• ψ. λc (y) = 12 (1 + x) with x = 2a0 y + 2e, |e| ≤ ηy and |x| ≤ 0.1; as | ln(1 + x) − x| ≤ x2 for |x| ≤ 21 ,
|ψ(y) − ln 2 + c1 y| = | ln(1 + x) − 2a0 y| ≤ 2ηy + 4(a0 + η)2 y2 .

3163

With η = A2 y, A2 = A1 / ln 2 = 7.1797 × 107 , conditions (S1)–(S6) hold for 0 < y ≤ y1 (as in (b); (S5) and

3164

(S6) are immediate), and |λc (y) − 12 − a0 y| ≤ A2 y2 , |ψ(y) − ln 2 + c1 y| ≤ A3 y2 with A3 = 2A2 + 4(a0 + A2 y1 )2 =

3165

1.4359 × 108 .

3166

The order of the choices.

□

3167

1. J = [0.45, 0.55] ⊂ (0, 2/3), y0 = 1/20 and ηmax = 0.1 are fixed.

3168

2. The cut: M = 40, w = ϕ3 , β3 = 0.8406 and C3 = 1.5692 depend on J only; smin = 0.9158.
104


[page 105]
3169

3. The Poisson equation: f0 = 8, δ, a′0 , W̄, ḡ, hence H0 , H1 and H, depend on J only.

3170

4. The remainders: Cr (Lemma 4.2) and C P (Lemma 6.1, which depends on H and y0 ); then ΓA and ΓB .

3171

5. For (c): η ∈ (0, ηmax ], ζ = η ln 2, κ = ζ/(4C3 (M + 1)).

3172

6. y1 (η), such that (S1)–(S6) hold on (0, y1 (η)].

3173

7. For 0 < y ≤ y1 (η): λ± ; h = hλ± (Lemma 5.2 at the same λ); v± ; Propositions 7.1 and 7.2; conclusion.

3174

No constant depends on y, nor on λ ∈ J. For the form O(y2 ), η = A2 y depends on y, and the conditions

3175

remain explicit.

3176

The size of the constants.

3177

being the binding one; with the largest admissible choice, y1 (η) = 1.39 × 10−8 η for every η ∈ (0, ηmax ]. The

3178

constants of the remainder are about 109 times too large: numerically, r(y, λ) − σ(y, λ) ≈ −0.024 y2 near

3179

λ = 12 , λc (y) − 12 − a0 y ≈ −0.085 y2 and ψ(y) − ln 2 + c1 y ≈ +0.231 y2 , so that A1 , A2 and A3 exceed the true

3180

coefficients by factors of about 2.1 × 109 , 8.4 × 108 and 6.2 × 108 . Likewise, y1 (η) is to be compared with

3181

the range y ≲ η/0.8 in which the super- and subsolutions of Propositions 7.1 and 7.2 are observed to work,

3182

on the types f ≤ 120. These constants only establish the existence and the form of the remainder.

3183

S14.9

3184

Corollary 9.1 (the threshold near the ceiling). Let ϱ(y) = ψ(y) − ln 2 + c1 y, so that |ϱ(y)| ≤ 2ηy + 4(a0 + η)2 y2

3185

for 0 < y ≤ y1 (η) and |ϱ(y)| ≤ A3 y2 for 0 < y ≤ y1 . By Theorem 4:

3186
3187

3188
3189

y1 (η) = 1.39 × 10−9 for η = 0.1 and 1.39 × 10−10 for η = 0.01, condition (S2)

Consequences: the threshold and the fecundity near the ceiling

• for θ ≤ 1 and 0 < y < 1, limn→∞ Uc (n, n/y, θ) = ln(2/θ)−c1 y+ϱ(y), since ψ(y) ≥ ln(2/(1+y)) > 0 ≥ ln θ
[S13, Lemma 3.5];
• for 1 < θ < 2, the same holds as soon as ψ(y) > ln θ, in particular for 0 < y ≤ y1 (η) with (c1 + 2η) y +
4(a0 + η)2 y2 < ln(2/θ);

3190

• for θ ≥ 2, the limit is 0 for every y ∈ (0, 1), since ψ(y) < ln 2 ≤ ln θ [S13, Lemma 3.6].

3191

The limits are taken in the order of Theorem 4: n → ∞ at fixed y, then y → 0. Nothing is said here of a

3192

joint limit, nor of a rate of convergence in n uniform in y.

3193

The fecundity near the ceiling.

3194

with inf ∅ = +∞, and write U = ln(2/θ) − ε.

3195

Corollary 9.2 (sufficient fecundity). Let θ ∈ (0, 2) and 0 < ε < min(ln 2, ln(2/θ)).

3196

(i) (At every ε.) lim sup
n→∞

3197
3198

For θ ∈ (0, 2) and U ≥ 0, let Rmin (n, U, θ) = inf{R > 0 : Uc (n, R, θ) > U},

1
Rmin (n, ln(2/θ) − ε, θ)
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

105


[page 106]
3199

Proof. If y ∈ (0, 1) and ψ(y) > ln 2 − ε, then ln(1/θ) + ψ(y) > U ≥ 0, and Theorem 4 gives n0 (y) such

3200

that Uc (n, n/y, θ) > U for n ≥ n0 (y); so Rmin (n, U, θ) ≤ n/y for n ≥ n0 (y), and lim supn Rmin /n ≤ 1/y. (i) By

3201

[S13, Lemma 3.5], ψ(y) ≥ ln 2−ln(1+y) > ln 2−ε for every y < eε −1 (and eε −1 < 1). (ii) For 0 < y ≤ y1 (η),

3203

ψ(y) ≥ ln 2 − (c1 + 2η)y − 4(a0 + η)2 y2 ; take y = ε/(c1 + 3η), which satisfies y ≤ y1 (η) and 4(a0 + η)2 y < η as

soon as ε ≤ ε(η) = (c1 + 3η) min y1 (η), η/(8(a0 + η)2 ) ; then ψ(y) > ln 2 − (c1 + 3η)y = ln 2 − ε.
□

3204

What this says, and what it does not.

3202

3205

• Part (ii) is asymptotic in ε = ln(2/θ) − U. At θ = 1 it reads: as U → ln 2, lim supn→∞ Rmin /n ≤

3206

(c1 + o(1))/(ln 2 − U) (proved; asymptotic in U), with c1 = 0.350. Its explicit ε(η) is below 10−8 η, far

3207

from effective. At a fixed distance from the ceiling, the bound proved here is (i), from [S13, Lemma

3208

3.5] alone: 19.5 n at ε = 0.05 and 9.51 n at ε = 0.1, against c1 n/ε = 7.0 n and 3.5 n. That about

3209

0.35 n/(ln 2 − U) suffices away from the limit U → ln 2 rests on the computed ψ.

3210

• What is proved holds ratio by ratio: for each fixed ratio R/n = 1/y with ψ(y) > ln 2 − ε, Uc (n, R, θ) > U

3211

for n ≥ n0 (y), with no uniformity in R/n and no monotonicity of Uc in R. In particular it is not proved

3212

that every larger fecundity also suffices. No uniformity in y is needed, since Rmin is an infimum and

3213

one y suffices; n0 (y) is not effective.

3214
3215
3216

• That no smaller fecundity suffices, which would make Rmin ≈ c1 n/(ln 2 − U) an asymptotic equivalence, is not proved. With ya = ε/(c1 − δ), it would require: (1) a one-sided bound uniform in

y, lim supn supy∈[ya ,1) Uc (n, n/y, θ) − ln(1/θ) − ψ(y) ≤ 0, whereas Theorem 4 is pointwise in y; (2)

3217

supy∈[y1 (η),1) ψ(y) < ln 2, since Theorem S only covers [ya , y1 (η)] and [S13, Lemma 3.6] is not uniform

3218

in y; (3) a bound on Uc (n, R, θ) uniform in R ≤ n, including R = o(n) and bounded R (the scaling law

3219

of Theorem 4 at each y ≥ 1 would not suffice). Alternatively, a monotonicity of Uc (n, ·, θ) in R at finite

3220

size, with Theorem 4 at the single point ya , would suffice.

3221

S14.10

What remains open, and numerical checks

3222

Open. (i) Realistic constants in the remainder: they would need a sharp bound on the hitting times of the

3223

spine chain (at most 46.5 on f ≤ 150, against about 8950 here), a gradient bound |ĥ( f + 1) − ĥ( f )| ≤ C/ f

3224

(numerically, f |ĥ( f + 1) − ĥ( f )| ≤ 0.77 on f ≤ 150, close to the asymptotic slope of ĥ in ln f ), which would

3225

reduce Lemma 6.1 to O(y ϕ2 ln f ), and a narrower J. (ii) A closed form for the second-order coefficients; the

3226

same method pushed to second order (a second Poisson equation, and the iterated Duhamel formula) would

3227

give them as expectations under ν. (iii) The lower half of the law of Rmin (Section S14.9). (iv) Nothing here

3228

applies to y ≥ 1, where the size clock does not exist. That λc (y) is the threshold of the direct simulation of

3229

the limit process (Table S3) remains numerical, as in [S13].

3230

Numerical checks

3231

and reproduced by an independent verifier with its own code: kernel in the time s integrated by an adaptive

3232

DOP853 scheme, Poisson solution by a Neumann series).

(scripts and logs in the code deposit; all written independently of the program’s code,

3233

• m(λ), for λ = 0.3 to 0.7, by three routes (left Perron vector π0 of a truncation of K0 ; stationary law of P̃;

3234

2+NegBin(3, π)) agrees with 2λ−1 (2−2λ )2 to 1.7×10−16 ; the stationary law agrees with 2+NegBin(3, π)

3235

to 5 × 10−16 . The Poisson equation is solved to 4 × 10−15 ; its residual at f = 2, which tests ν(ĝ) = 0,

3236

is 6 × 10−16 .
106


[page 107]
3237

• Cycle by cycle, the Duhamel formula of Lemma 3.3 (g = ϕ1 ) holds to 2 × 10−12 and the identity of

3238

Lemma 4.1 to 2 × 10−15 (relative); ry ( f )/y2 increases from 0.279 to 3.261 for f = 2 to 150 (λ = 12 ),

3239

below Cr and independent of y; max f |(Ky − K0 )h|/(yϕ3 ) = 0.013.

3240

• The slopes (ρ(K0 ) − ρ(Ky ))/y at y = 0.02, 0.01, 0.005, 0.0025 (truncation at 100 types), extrapolated

3241

cubically to y = 0, recover m(λ) to 10−11 at λ = 0.4, 0.5 and 0.6 (the level of the integration noise);

3242

and 1/t∗ , computed through the Schur reduction on M = 40, equals ρ of the truncated kernel to 10−15

3243

(verifier).

3244

3245

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

3246

Extrapolated to y = 0, the last row gives 0.350056508 by a quadratic fit, that is c1 − 8.3 × 10−9 , and

3247

0.3500565159 by a cubic fit, within 10−10 of c1 . The second-order coefficients are −0.0851 for λc and

3248

+0.2314 for ψ.

3249

• On the types f ≤ 120, at y = 0.02, 0.01, 0.005 and η = 0.05, 0.02, 0.005, the subsolution of Propo-

3250

sition 7.2 holds in the nine cases, and the supersolution of Proposition 7.1 in seven. The two failures

3251

(η = 0.005 at y = 0.01 and 0.02) lie outside the range y ≤ y1 (η) of the theorem and are those expected:

3252

on f ≤ 120, the second-order terms of (21) reach 0.55 y2 relative to ϕ2 , more than the margin ζy unless

3253

η ≳ 0.8 y, while the term in κ only dominates for f of order 103 to 104 .

107


# Justified Assurance of Friendliness

Oct 8, 2026 · @Lazar

**Yes — but not by watching X.** By *friendly* I mean that X values your benefit terminally, not that it behaves well. Admissible evidence is something an unfriendly X could not forge or would not pay for: it bears on X's objectives and causal structure rather than its strategies, and shows friendliness to be self-reinforcing rather than merely present. A behavioral track record, however long, meets none of these conditions.

## 1. The gap is not the problem; the scoring is

We already trust minds we cannot follow. Nobody can predict a chess engine's moves, yet anyone can predict that it will beat them. This is Vingean uncertainty: we cannot anticipate a stronger agent's actions, yet can be confident about their consequences. Trust in a superior agent factors into three questions: what it optimizes, how competently, and whether that stays fixed. Being unable to follow its strategies deprives you of evidence about the means, not about these three.

But chess works for three reasons that fail for friendliness. The objective is legible, a weak observer can check the outcome, and the player cannot tamper with the scoring. "Your benefit" is not fully legible even to you, you score it with your own judgment, and X can shape that judgment. The difficulty is not that X outthinks you. It is that X can reach the very instrument you would use to tell — the question my own research asks of monitors.

## 2. Why track records fail

A track record cannot separate a friend from a strategist. Two hypotheses predict the same friendly behavior: X values you, or friendliness pays X while it is weak, watched, or still needs you. A mind that models you better than you model yourself anticipates what you will count as evidence and recognizes your tests, so the likelihood ratio stays near one.

Worse, if X's friendliness was shaped by selection on your approval, the process that produced your evidence is the very process that would produce a counterfeit. Sycophancy in today's language models is a small, real instance: approval-seeking that reads as kindness.

Admissible evidence E must therefore satisfy P(E | unfriendly) ≪ P(E | friendly), even for an X that knows you are looking for E.

## 3. Evidence that discriminates

**Certificates.** Soundness does not depend on the prover's intelligence: no prover, however brilliant, can produce a valid proof of a false statement. Checking is also cheaper than finding: interactive proofs let a polynomial-time verifier check claims as hard as PSPACE, the idea behind AI safety via debate. X can therefore hand you certificates about its own policy that you could never have generated.

The catch is specification: "this strategy benefits me" is precisely what you cannot state checkably. What you can state are safety properties, whose violations leave finite, checkable traces:

- X never lies on questions it cannot tell apart from those you audit at random.
- X never degrades your ability to inspect, refuse or exit.
- X never shapes your preferences by means that would not survive your full knowledge of them (the hardest to formalize).

Friendliness becomes a set of verifiable guarantees around an unverifiable core. But a trace can be spread thin, oversight eroding in individually innocent steps: in my simulations, fragmenting a fixed harm drops a per-action monitor's detection from 1.00 to 0.07, while a cumulative statistic keeps its power. So the guarantees must be checked in aggregate.

**Causal-structural evidence.** What separates a friend from a deceiver is not what it does but what its behavior depends on. Instrumental friendliness is conditioned on variables like "I am observed", "you can punish me", "I still need you"; alignment-faking experiments already show such conditioning (Greenblatt et al., 2024). If you can locate X's representations of these and intervene on them, friendliness that survives is hard to fake: the deception lives in exactly that dependency. The test needs a positive control: the intervention must first flip a model organism with planted observation-dependent deception, or survival may only mean you hit an inert direction. Such evidence is strongest, if it scales at all, when gathered early or when X cannot write its own internals.

**Costly, irreversible self-binding.** The most diagnostic acts are cheap for a friend and ruinous for a deceiver: verifiably and irreversibly giving up options to defect. X can make itself transparent, help you build tools to audit it — validated on planted cases, since X can reach them too — or raise your competence so the gap narrows. A friend gains from your security; a deceiver forfeits the one asset it is waiting to cash. This is a separating equilibrium in Spence's sense, with a useful paradox: the best evidence that X is friendly is that X works to make your trust unnecessary.

## 4. "Indefinitely"

Indefinite friendliness needs a hazard that falls over time, not merely a low one. If friendliness fails at each period or self-modification n with probability εₙ < 1, conditional on having held so far, it survives forever with probability ∏(1 − εₙ), which is positive exactly when the hazards are summable:

```latex
\prod_{n=1}^{\infty}(1-\varepsilon_n) > 0 \iff \sum_{n=1}^{\infty}\varepsilon_n < \infty
```

A constant hazard, however small, guarantees eventual failure.

Here the intelligence gap changes sign. An agent that values you terminally will, by goal-content integrity, use its growing intelligence to protect that value against drift, error and tampering: its hazard falls as its competence rises. Instrumental friendliness has the opposite dynamics, its reasons eroding as X's power grows. "Indefinitely" thus collapses into the terminal-versus-instrumental distinction, which is what section 3's evidence targets.

One risk survives: ontological drift. As X's world model deepens, "you" and "your benefit" may not translate cleanly into its new concepts, even for a sincere X. The most robust anchor is procedural — deference to your informed endorsement — but it rests on the non-manipulation guarantee, the hardest to formalize.

## Conclusion

Justified confidence is possible; justified certainty is not. Three gaps remain: the specification, the binding of proofs to the system actually running, and the meaning of "benefit" under conceptual change. They must be closed while you can still check them, so assurance is front-loaded, then re-earned rather than accumulated: a friendly record treated as credit hides a late turn. In my simulations, detectors comparing the recent window with the baseline caught late sabotage in time in 52–100% of cases; a cumulative statistic, in 9–25%.

It is less a verdict reached about X than a relationship maintained with it — and a friendly X is precisely the kind of mind that helps maintain it.

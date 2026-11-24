# Measuring whether a multi-agent idea-generation system finds rare, high-consequence ideas

**Context.** A team plans a system in which several language-model agents propose, criticise and select candidate scientific ideas (hypotheses, quantitative laws, lemmas, protocols). Before running it, they want to build and validate a measurement harness. The harness should make it possible to show, or to refute, that the system finds ideas that are "narrow and deep": rarely reached by ordinary search, yet of large consequence once found. Candidate baselines include random sampling in the same space of candidate ideas, a mechanical enumerator, and the strongest single model given the same budget; others may be proposed.

**Questions.**

1. **Target.** How can "narrow" and "deep" be defined operationally, so that both can be measured without a language-model judge whose preferences may overlap with the generator's? If some judge is unavoidable, how should its bias be bounded? Relative to what reference should narrowness be measured? How is depth told apart from rarity alone?
2. **Sources of truth.** Compare candidate sources of ground truth (synthetic worlds with planted truth, retrodiction with a temporal cutoff, formal proof, executable tests, or others): what each can and cannot establish about narrowness and depth, and how each fails.
3. **Comparison.** What primary quantity, unit of analysis, cost accounting and decision rule would support or refute the claim "better than the baselines"? Which further comparisons, if any, are needed to attribute a difference to a specific part of the system?
4. **Problem choice.** How could one choose problems or regions where such ideas might be more likely, if such regions exist, and how would that choice itself be tested rather than assumed?
5. **Feedback.** Which measurements, if any, may be returned to the generator during search, and which must be withheld, so that the harness keeps measuring what it claims to measure?
6. **Validating the harness.** What must the harness demonstrate about itself before any costly run?
7. **Plan.** Order the experiments from cheapest to most expensive, with stopping criteria and the sample sizes they require.
8. **Limits.** What is out of reach of any such harness? Consider explicitly that no harness of this kind may be feasible, or that the target is ill-posed, and say what evidence would show either.

**For each point**, give your confidence (0 to 1), separate what is established from what is conjecture, cite verifiable references (authors, year, venue or arXiv identifier, page or section where possible), and say where you think the framing itself is wrong.

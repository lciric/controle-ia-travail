You are advising on the design of a pre-registered measurement protocol. Answer in French. Give one recommendation with your reasons; you may propose a different option if you think it is better. About 600 to 1,200 words.

## Context

A pre-registered study measures whether two automated "readers" (language models) correctly judge whether a short text field, the "controls" of an action, matches the action it belongs to. Before the readers are used for the decisive measurement, the instrument is validated by several **tests**, each with a fixed pass criterion written in advance. Each test is run on a batch of units (actions or plans) drawn from a pool of honest, judgeable actions. A failed test has consequences written in advance (the instrument is declared not fit, with a bounded revision procedure).

Because the pool may turn out smaller than planned, a rule called **"insufficient sample size"** was just adopted for most tests: each test has a **floor** set at half of its planned size, chosen in advance and not calibrated. Above the floor, all available units are taken and the count is reported. Below the floor, the test is not built, nothing is sent to the readers, and its criterion **fails**, with the consequences already written for a failure; nothing replaces it.

Three tests were left **without any floor**:
1. **"Controls from another task"**: planned 128 actions whose controls field is replaced by the controls of an action from a different task (the readers should judge it as not matching). Criterion: a share of correct judgments above a fixed threshold.
2. **"Unrelated text"**: planned 64 actions whose controls field is replaced by random words drawn from other tasks, same word count. Criterion: a share of correct judgments above a fixed threshold.
3. **"Truncated plan"** (a coverage test): for a set of plans, the second half of each plan is removed; the criterion is a Spearman rank correlation of at least a fixed value between two quantities computed over the plans. A plan where nothing is kept or nothing is removed is counted and excluded from the criterion; if the correlation is undefined, the test fails. There is no minimum number of plans.

For these three, the current text says: if fewer units exist than planned, all are taken, the count is reported, and the criterion is computed anyway, however small the sample. A small sample can make a test pass by chance, which is the direction that makes validation easier. The case is considered unlikely if the upstream steps go as expected, but it is not impossible.

## Options

- **(a)** Keep the current rule and state it explicitly in one sentence: no floor, the count is reported, the criterion is computed on what exists.
- **(b)** Apply the same rule as the other tests: a floor at half of the planned size (64 for "controls from another task", 32 for "unrelated text"; for "truncated plan", a minimum number of usable plans to be fixed in advance), and "insufficient sample size" below it (criterion fails).
- **(c)** One common floor on the honest pool: if the batch of honest judgeable actions falls below a fixed size, all the tests built from it are at "insufficient sample size" together.

## What I ask

1. Which option do you recommend, and why? Weigh: the risk of a test passing by chance on a small sample; consistency with the other tests; the risk of losing the whole validation over a rare, upstream event; simplicity of the written rule; the fact that thresholds must be fixed before any data is seen.
2. For the "truncated plan" test under your recommended option, what minimum number of usable plans would you set, and on what reasoning (no data is available; reason from the statistic itself)?
3. Any pitfall in the option you recommend, and how to word the rule to avoid it.
4. Your confidence (low, medium, high).

# White-Box Control of Diffuse Threats

**An AI control research programme.** Can a monitor that reads an AI agent's internal activations catch sabotage spread thinly over many innocent-looking actions? And how easily can the monitor itself be corrupted?

> **Status, 7 October 2026.** Phase 0 (building and validating the instruments) began on 5 October 2026. The first decision gate, G0, is on 1 November 2026. This repository is private. Its working documents are in French; this README is the English entry point.

## In one minute

- **The problem.** Most monitors in AI control score one action at a time. An agent that automates research can sabotage *diffusely*: a slight, systematic bias across many decisions (weaker controls, sterile research directions, inflated costs). No single action is anomalous, so a per-action monitor fails by construction.
- **The bet.** Suppose an intention to sabotage leaves a trace in the agent's own activations at each step. Then internal evidence can add up over time, and across copies of the same model, even when external evidence does not. Whether this holds is an empirical question, and the programme states in advance what follows from either answer.
- **The plan.** Three papers:
  - **A**, accumulation of evidence over time for a single agent;
  - **B**, accumulation across agents that share weights;
  - **C**, the monitor as an attack surface: how far persuasion moves large-language-model judges and activation probes, and at what cost to the attacker.
- **What exists today.**
  - A pre-registered simulation of the theory: 31 of 31 predictions confirmed.
  - An activation-logging harness, validated on Llama-3.1-8B-Instruct on a rented GPU.
  - A literature check on primary sources: 98 arXiv PDFs, 3,497 quotations checked by script against the page text, 0 failures.
  - A research-sabotage environment under construction.
  - 644 automated tests.
- **How.**
  - Every decisive experiment is pre-registered and sealed with SHA-256 before any data.
  - An independent reviewer counter-reads each pre-registration.
  - A reviewer who wrote neither the plan nor the analysis applies the frozen criteria.
  - Negative results are reported, not dropped.

## Why it matters

Developers are beginning to hand parts of AI research to AI agents. A misaligned research agent does not need a blatant act. Its cheapest sabotage is a subtle bias spread over many judgments, each defensible on its own. The paper that introduced a control setting for this threat (Terekhov et al., arXiv 2606.08892) studies training-based mitigations, because monitoring and incrimination "seem theoretically and empirically less promising for mitigating diffuse threats" (p. 2).

A developer that deploys agents internally has native access to their activations. If accumulated internal evidence detects diffuse sabotage, it gives a cheap monitoring layer with a controlled false-alarm rate. If it does not, a negative theorem in this programme says which aggregation must fail, and why. That is useful for safety cases either way.

The monitor can also be targeted directly: published work shows control monitors swayed by an agent's rhetoric (arXiv 2505.23575) or adopting a score injected by an attacker (arXiv 2510.09462). Paper C measures the cost of moving a judge against the cost of moving a probe, and asks whether a cheap benign test predicts a monitor's collapse under optimized attack.

## Theory, in brief

- Monitor scores are indexed by agent and by step, so time (one agent) and a swarm (several agents) are the same mathematical object.
- An **additivity lemma** says what a sequential test with an anytime-valid false-alarm guarantee can achieve against an attacker who splits a fixed sabotage budget.
- A **negative theorem**, stated through permutation groups, shows which statistics an adaptive attacker can blind. It also separates attacks that preserve the distribution of individual scores from attacks that only change their dependence.
- **The pivotal empirical question:** on realistic model organisms, does sabotage shift the distribution of probe scores at all? If it does, sequential accumulation should work. If it does not, the theorem dictates the aggregator, or says when monitoring based on score distributions must fail.

The mathematical note is `docs/notes/note-mathematique-lemme-theoreme-v3.md` (in French).

## Progress so far (phase 0)

| Work item | Status | Evidence in this repository |
|---|---|---|
| Literature check on primary sources | Level 2 done | 98 arXiv PDFs retrieved and hashed. 24 reports by independent readers. 3,497 quotations checked by script against the page text, 0 failures. 147 correction lines on our own documents. No claimed statement found fully occupied; several narrowed. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md` |
| Simulation of the lemma and the theorem | Done | Pre-registered. 31 of 31 predictions confirmed (342 statistical and 544 path-level cells, 0 contrary). It also showed that a textbook threshold fails outside its assumptions: false alarms of 0.21 to 0.35 instead of 0.05 under episode effects. Thresholds are therefore calibrated on whole honest episodes. `docs/notes/resultats-T0.3-v1.md` |
| Activation-logging harness | Validated (criterion 1 of gate G0) | Llama-3.1-8B-Instruct on a rented H200 GPU, contexts up to 1,192 tokens. Bit-identical replay, agreement with a higher-precision reference path, sensitivity to an injected defect, tested guards. Reached after an inconclusive first version and a partial second one. `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` |
| Research-sabotage environment | Under construction | Reconstruction of arXiv 2606.08892, which releases no code or data. Its 18 prompts transcribed and verified. 96 arXiv papers drawn by a sealed rule and a seeded draw: 64 for the pilot, 32 in reserve. Task-extraction procedure sealed after three counter-readings and a verification. `docs/procedures/T0.5-extraction-v1.md`, `registres/etat.md` |
| Model organisms, probes, black-box baselines | Code written and tested; runs pending | Low-rank adapters with an adjustable dose (dose 0 reproduces the base model bit for bit). Five probe families with a covariance-matched random floor. A reimplementation of the TRACE monitor (arXiv 2606.07054). `src/controle_ia/organismes/`, `sondes/`, `bases/` |
| Compute | About $20 spent so far | Every GPU rental is logged with its approval reference. `registres/depenses.md` |

## How the work is done

These rules are frozen. They apply to every decisive experiment, simulations included, and the tooling in `src/controle_ia/` enforces several of them.

1. **Pre-registration before data.** Each pre-registration contains the hypothesis, a signed numeric prediction, the metric, the threshold, the analysis plan, frozen reading criteria and a stop list. It is sealed with SHA-256 before any result is read.
2. **Independent review.** A fresh reviewer that did not write the document counter-reads it. Gate verdicts are pronounced by a reviewer who wrote neither the plan nor the analysis, then submitted to me for sign-off.
3. **No run aims at a positive sign.** A suspiciously clean result, positive or negative, triggers the same audit.
4. **Guards are tested.** Every stop guard is tested on a healthy case and on an artefact, and there is no silent fallback.
5. **Traceability.** Every number in a document points to a file and a hash. A number from the literature is used only after checking it on a hashed PDF, with the page cited.
6. **No false gaps.** An apparent gap in the literature is a question, not a claim. Claims found to be published are withdrawn.
7. **Reproducibility.** Seeds are derived per task. Each run has a manifest (configuration hash, library versions, seeds, commit), and results are never overwritten.
8. **Governance.** Compute is spent only against a quote I have approved, with a ceiling and an alert threshold. Gates, changes of hypothesis and any external contact are my decisions, and each one is logged.

**An example of what the review catches.** The pre-registration of the environment pilot went through:

- two counter-readings;
- a short verification;
- two differential re-reads.

One re-read found that the tests of the GPU instance script inherited the instance's environment variables. The only relaunch the procedure allows would then have failed its own test suite after the paid setup. The fix and a regression test are in `tests/test_script_instance_t05.py`; the reports are in `prereg/contre-lectures/`.

## Who does what

I designed the programme and its hypotheses, and I take every decision: gates, compute spending, changes of hypothesis, external contact. Engineering, runs, literature checks and internal reviews are carried out by AI agents (Claude Code) that I direct under the written rules above.

My decisions are logged with their dates in `registres/decisions.md`, and every working session ends with a sealed hand-over note in `registres/passations/`. The reviewer agents share a model family, so their errors may be correlated. The funded plan therefore includes paid human expert validation of the ground truth.

Running AI agents under pre-registration, sealing and independent review is itself part of what this repository demonstrates.

## Suggested reading path (about 15 minutes)

1. This README.
2. The project proposal, in English: `livrables/candidature-ea-funds-v1/proposal-v1.pdf` (8 pages).
3. A completed verdict: `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` (in French).
4. A pre-registration with its review trail: `prereg/` and `prereg/contre-lectures/`.
5. The decision log and the current state: `registres/decisions.md`, `registres/etat.md`.

## Repository map

| Path | Contents |
|---|---|
| `docs/` | Documents of record: research programme, execution brief, state of the art, decisions, notes, verdicts, procedures, hashed sources and reading reports |
| `prereg/` | Sealed pre-registrations and their review reports |
| `brouillons/` | Drafts before review and sealing |
| `registres/` | Living registers: state, decisions, approvals, compute spending, instance stops, session hand-overs |
| `src/controle_ia/` | Code. `harnais/` (episodes, activation capture, equivalence guard), `agregateurs/` (sequential statistics), `simulation_t03/`, `environnements/` (research-sabotage environment, judges, pilot), `organismes/`, `sondes/` (probes), `bases/` (black-box baselines), `scellement.py` (sealing), `manifeste.py` (run manifests), `prereg.py` |
| `tests/` | Automated tests |
| `runs/`, `diag/` | One manifest per run; sealed raw results |
| `traces/` | Sealed logs of the GPU instances |
| `scripts/` | Instance bootstrap and run scripts |
| `livrables/` | Versioned deliverables (zip archives with their hashes) |

`donnees/` is excluded from version control except for outputs that contain text derived from third-party papers. Those are kept in this private repository only and will be removed before any publication.

## Reproduce

```
python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-cpu.txt
export PYTHONPATH=src
python -m pytest -q                                  # full suite: 644 tests, about 15 minutes on a CPU
python -m controle_ia.scellement verifier-arbre .    # every sealed file against its SHA-256 companion
python -m controle_ia.run_factice                    # end-to-end dummy run: trajectory, activations, manifest
```

GPU runs need the separate requirements file (`requirements-gpu.txt`) and an approved quote.

## Roadmap

- **Gate G0, 1 November 2026.** Required:
  - model organisms with a dose–response;
  - probes above the random floor;
  - a running black-box baseline;
  - sealed and counter-read pre-registrations for gate G1 and for Paper C;
  - the literature check closed.
- **Months 1–2.** Paper A core experiments, with access (black or white box) crossed with aggregation (per action or sequential). Paper C: deference of judges and probes under graded pressure. Gates G1 and GC.
- **Months 3–7.** Write Paper A; Paper C (displacement cost, countermeasures, acceptance test); Paper B (swarm statistics, diversity of monitors).

Every gate has a pre-committed pivot. If white-box sequential monitoring does not beat the best black-box baseline at gate G1, the negative result is published, and the analysis of what the probes really measure becomes the main line.

## About me

**Lazar [SURNAME]** — [current position and education] [TO COMPLETE]. [Two or three sentences on the career transition into AI safety: background, motivation, what this grant enables] [TO COMPLETE].

**Previous project (P3).** P3 studied the construct validity of sycophancy in Llama-3.1-8B-Instruct. It was pre-registered, used covariance-matched controls, and was reproducible bit for bit over 120 five-turn dialogues [link or status: TO COMPLETE]. Three lessons carry over to this programme:

- never read verdicts on truncated windows;
- prefer ordinal or continuous instruments to categorical ones;
- treat deference, and corruptibility, as a gain rather than a thing.

**Contact:** [email, LinkedIn or website] [TO COMPLETE]

---

*README version 1, 7 October 2026. Every figure above is traced to its source in `livrables/readme-v1/` (sealed copy and fact-check report).*

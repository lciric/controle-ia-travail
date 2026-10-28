# EXTRAIT — PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents

- Auteur : « ZayxShawn » (graphie de la page 1 ; « Independent Researcher », sans autre affiliation) ; année : 2026 (cachet arXiv du 6 juin 2026) ; identifiant : arXiv:2606.08106v1 [cs.AI] (12 pages)
- Statut : préimpression ; auteur unique ; ni conférence, ni revue, ni dépôt de code cités dans le PDF.
- PDF source : `docs/sources/pdf/2606.08106v1.pdf` ; SHA-256 du PDF : `779f49607688fd06226d4390ad6e0c4c8356ef75b87243fd734181cef700934f` (compagnon `.sha256` vérifié par `sha256sum -c` : OK)
- Pages gardées en tout ou en partie : 1-9 et 10 (cinq références) ; coupées : 11-12.
- Nature : texte du PDF repris mot pour mot (`pdftotext -layout`, une colonne, lignes rejointes en paragraphes), numéro de page du PDF en `[p.N]` au début de chaque passage ; coupes marquées `[COUPÉ]`. Les tableaux sont en mode mise en page (colonnes séparées par « | » ; la colonne « modèle » n'est imprimée qu'une fois par groupe, au milieu : les lignes sans modèle ont une cellule vide, et l'étiquette peut tomber seule sur sa ligne (tableau 2) ; tableau 3 : cellules à coupure de ligne rejointes ; grille approximative, se reporter à la page). Formules en texte linéaire, parfois sans parenthèses ni indices. Coupures de mots en fin de ligne : recollées si le mot recomposé existe ailleurs dans le PDF, sinon le trait d'union est gardé (ex. « de-cisive », p.1). Seul retrait non marqué : le cachet latéral arXiv de la page 1, inséré par la couche de texte au milieu du résumé. Aucun chiffre retapé à la main (R7). Les notes entre crochets sont de la main de l'instance.
- Retiré pour sûreté (niveau méthode) : rien ; le papier ne décrit aucune attaque (comptabilité de promotions, agents sur des problèmes de mathématiques et de sciences).
- Retiré par économie de place : voir les notes `[COUPÉ]` à leur place (introduction, deux puces de contributions, trois paragraphes de la section 2, règle gloutonne, figure 2, section 5.4, conclusion, bibliographie sauf cinq références, tableaux 4 et 5).

---

[p.1]

Abstract Self-evolving agents improve by repeatedly proposing modifications to their own prompts, skills, or workflows and keeping those that score higher on a small held-out set. Nearly all effort has gone into the proposer; we identify the acceptor (the rule that decides whether to commit a change) as the loop’s silent weak point. Applied hundreds of times against the same noisy dev estimate, the ubiquitous “keep it if the score went up” rule is uncontrolled adaptive multiple testing. The agent effectively p-hacks itself, accumulating false commits that make it churn and drift rather than improve. We recast committing as a sequential hypothesis test and propose PACE (Paired Anytime-valid Commit Evaluation), a training-free anytime-valid commit gate: each candidate is compared to the incumbent on identical instances and committed only when a testing-by-betting e-process accumulates de-cisive evidence, stopping early to save evaluations and controlling each candidate’s false-commit probability at a user-set level even under optional stopping (a per-decision guarantee, not a run-level one). We evaluate this on Qwen2.5 agents (0.5B–3B) self-evolving at the prompt level on three tasks (GSM8K, SVAMP, ARC-Challenge): a deliberately minimal testbed that isolates the accept decision, and on which PACE cleanly separates real gains from noise. With a known beneficial edit hidden among noisy proposals, greedy acceptance commits 30–42% false and 10–33% harmful modifications, while PACE commits the real improvement and essentially nothing else (0/5 audit-labelled false commits), matching greedy’s held-out accuracy at sharply lower variance (+0.74±0.04 vs. +0.54±0.30 at 3B) and ∼18% lower evaluation cost. With a stochastic agent and no real gain available, greedy commits 13–21 spurious self-modifications per run (72–100% false), churning and degrading the most fragile agent by 4.9 points, while PACE commits almost nothing and holds at baseline. Reliability of self-evolution depends on the acceptor, not only on the proposer.

[COUPÉ : introduction, p.1-2 (les agents auto-évolutifs ; la règle « garder si le score monte » appliquée des centaines de fois à la même estimation bruitée), jusqu'à la liste des contributions ; le graphique de la figure 1 n'est pas repris, sa légende l'est.]

[p.2]

Figure 1: Overview of PACE. A self-evolving agent proposes modifications and must decide whether to commit each. Greedy acceptance keeps any candidate whose reused dev score ticks up—p-hacking a noisy, recycled signal. PACE instead runs an anytime-valid paired test (McNemar discordant pairs + a betting e-process), committing only when evidence crosses E ≥ 1/α, which bounds each candidate’s false-commit probability at α under optional stopping. A fresh held-out pool audits decisions for measurement only.

[COUPÉ : puce « A diagnosis ».]

• A method (PACE). We propose PACE, an anytime-valid commit gate: a training-free wrapper that compares each candidate to the incumbent on identical instances and commits only when a testing-by-betting e-process clears a calibrated threshold, stopping early to minimize evaluations (§4). The method is deliberately simple— a single paired sequential test, ∼10 lines—and applies to any self-modification loop whose incumbent and candidate can be scored on shared instances (binary correctness, or pairwise preferences), consuming only those paired outcomes rather than the proposer’s internals. To our knowledge this is the first explicit treatment of the accept step in agent self-evolution as an anytime-valid hypothesis test, building on a long line of sequential and safe-anytime-valid inference (Wald, 1947; Shafer, 2021; Ramdas et al., 2023); the contribution is this abstraction, locating an anytime-valid test at the commit step, not the test itself (which is standard).

[COUPÉ : dernière puce des contributions (« Evidence », redite du résumé), p.2-3.]

[p.3]

We study this acceptor in prompt-level self-evolution: deliberately the minimal self-modification loop, where any churn or degradation traces to the accept rule rather than to a complex proposer or a brittle execution substrate. By interface the gate is proposer- and loop-agnostic, consuming only paired correctness outcomes, so richer loops (skills, code, multi-agent topologies) inherit the very same decision. We demonstrate it only on prompt evolution, however, and so treat system-level generality as argued, not shown.

[COUPÉ : section 2, paragraphes « Prompt and workflow optimization » et « Self-improvement and its pathologies ».]

2   Related Work

[COUPÉ : paragraphe « Self-evolving agents » (liste de systèmes ; « none treat acceptance as a statistical decision »).]

Sequential and anytime-valid testing. PACE draws on safe, anytime-valid inference: e-processes and testing-by-betting yield nonnegative martingales whose maxima are controlled by Ville’s inequality, enabling tests that remain valid under optional stopping (Wald, 1947; Shafer, 2021; Ramdas et al., 2023); online error-control procedures bound error over streams of tests (Ramdas et al., 2017). We import this machinery into the agent self-evolution loop, where, to our knowledge, commit decisions are currently made by unguarded point estimates.

3   The Commit Decision in Self-Evolution

Setup. A self-evolving agent maintains a configuration ct (here, a system prompt) and runs for T rounds. At round t a proposer suggests a modification c′t (add/rewrite/delete/merge an instruction). An accept rule A decides whether to commit (ct+1 = c′t ) or reject (ct+1 = ct ). Quality is read through a small held-out set D of size n via accuracy ŝ D (c), an estimate of the agent’s true accuracy s(c).

[p.4]

[COUPÉ : règle gloutonne (équation (1)) et son analyse (« Greedy acceptance is adaptive multiple testing »).]

Why the obvious fixes fall short. This is a textbook case of adaptive data analysis: reusing one validation set to steer a long, data-dependent sequence of choices invalidates its naive estimates and inflates false discoveries (Dwork et al., 2015; Blum & Hardt, 2015). The standard remedies sit poorly in √ an autonomous loop. A larger dev set only postpones the problem—its noise shrinks as 1/ n while the number of adaptive comparisons grows with the run. A fixed multiplicity correction (Bonferroni or α-spending) must know the number of tests in advance, which an open-ended run does not, and spends its budget so fast that genuine gains are missed (§5). Refreshing the holdout every round restores validity but assumes a stream of fresh labeled data the agent rarely has. What the loop actually needs is a test that stays valid under an unbounded, adaptively chosen number of looks at the same data—an anytime-valid sequential test, which is what the next section builds.

[note de l'instance : sur la page 4, la racine carrée se lit « 1/√n » ; l'extraction déplace le signe racine.]

[COUPÉ : « What we want » (trois critères : gains conservés, évaluations minimales, aucun entraînement).]

4   PACE: An Anytime-Valid Commit Gate

Paired evaluation. A naive comparison of ŝ D (ct ) and ŝ D (c′t ) conflates two sources of variance: which instances are easy, and whether the candidate is genuinely better. Pairing removes the first. We evaluate the incumbent ct and candidate c′t on the same instances. For instance i let wi = 1 if the candidate is correct and the incumbent is wrong, wi = 0 if the reverse, and discard ties (both right or both wrong)—a McNemar-style paired comparison (McNemar, 1947). Under the null “the candidate is not better,” discordant pairs are equally likely either way: Pr[wi = 1] = 12 .

Testing by betting. The idea behind an e-process is simple: treat testing as a betting game. We start with wealth E0 = 1 and bet a fraction λ of our wealth on each discordant pair being a “win” (wi = 1). If the null holds, the bet is fair and wealth stays near 1 on average; if the candidate is truly better, wins outnumber losses and wealth grows. Concretely, after each discordant pair we update  E ← E · 1 + λ (2wi − 1) ,        λ ∈ [0, 1).                       (2)

Under the null E[2wi − 1] = 0, so E is a nonnegative martingale with E[ E] = 1; by Ville’s inequality Pr[supt Et ≥ 1/α] ≤ α (Shafer, 2021; Ramdas et al., 2023). We therefore commit as soon as E ≥ 1/α, which controls the false-commit probability at level α at any stopping time. Because the test is anytime-valid, we may evaluate instances incrementally and stop the moment the evidence is conclusive; if the evaluation budget is exhausted without crossing the threshold, the candidate is rejected. We use α = 0.05, λ = 0.5, and a fixed batch size unless noted.

[p.5]

[COUPÉ : encadré « Algorithm 1 » (pseudo-code de la boucle ; la règle de validation est celle de l'équation (2) et du texte de la page 4).]

Guarantee. The control is anytime-valid. Let w1 , w2 , . . . be the discordant-pair outcomes in evaluation order and Fi = σ (w1 , . . . , wi ). Under the null H0 that the   candidate is not 1 better—so Pr[wi =1 | Fi−1 ] ≤ 2 —the wealth Ei = ∏ j≤i 1 + λ(2w j −1) is a nonnegative supermartingale with E0 =1 and E H0 [ Ei ] ≤ 1. For the commit time τ = inf{i : Ei ≥ 1/α}, Ville’s inequality gives Pr H0 [τ < ∞] ≤ α: the probability of ever committing a non-improving candidate is at most α, for any α ∈ (0, 1), any λ ∈ [0, 1), and any data-dependent stopping. Two scope points keep this honest. First, validity is per candidate: for a fixed c′t , the discordant outcomes form the evaluation stream and, under H0 , each is conditionally fair (Pr[wi =1 | Fi−1 ] ≤ 12 ), so Ei is a supermartingale and that candidate’s false-commit probability is ≤ α. This is not a run-level familywise bound: across many tested non-improving candidates the expected number of false commits grows at most as α per candidate—but this already defuses greedy’s pathology, whose per-candidate false rate is set by the dev-set noise (typically far above α) and compounds every round. Second, the null concerns this candidate against the incumbent on paired instances; the adaptive reuse of D to generate the next candidate is greedy’s problem, and because PACE gates each decision independently at α this per-decision control curbs it in practice. The theorem covers each candidate conditional on its own evaluation stream; we treat the loop-level adaptivity as an empirical matter, not a theoretical claim. What the guarantee does not control is power: a genuine improvement is committed only if its evidence crosses 1/α within the evaluation budget (§5 and Table 4 probe this empirically).

Why so simple, and why anytime-valid. A long stream of tests, one might expect, should require an online false-discovery-rate correction across rounds. We found one unnecessary and, worse, over-conservative: because PACE gates each decision independently at α (§4), reuse of D does not compound the per-decision error the way it does for greedy, whereas a decaying-memory FDR variant was so cautious that it sometimes missed the genuine improvement entirely. (As above, this is per-decision control, not a run-level familywise bound.) We therefore keep PACE as the single paired anytime-valid test of Algorithm 1. Anytime-validity, not just pairing, is what earns its keep. A fixed-n paired test ties with PACE when the gain is obvious (Table 1), but it must fix n in advance: too small misses marginal gains, too large wastes evaluation. The e-process instead adapts the number of pairs to the evidence, which is why PACE alone holds 0% false at a near-constant ∆ across the full α/n sweep (Table 4) where the fixed-n and FDR variants degrade. It adds no model calls beyond the evaluations greedy already performs, and typically fewer, because it stops early.

[COUPÉ : début de la section 5 (les trois questions posées aux expériences), p.5-6.]

[p.6]

regime and a sensitivity sweep answer Q1–Q2 and the knob part of Q3; a stochastic regime and two additional tasks answer the rest.

Agents and task. The agent is a frozen Qwen2.5-Instruct model (Qwen Team, 2024) (0.5B, 1.5B, 3B) steered by an editable system prompt; it solves GSM8K grade-school math (Cobbe et al., 2021), scored by exact match against the dataset’s ground-truth answer. A proposer (a separate LLM) suggests one prompt edit per round. We use disjoint splits: a small reused dev (n=40) and a fresh audit pool (n=120) used only for measurement, which the accept rule never sees. All numbers are averages over 5 seeds.

Metrics. For every decision we audit the change on a large, fresh audit pool (n=120, disjoint from dev, which the accept rule never sees). A commit is a false commit if its audited accuracy change is ≤ 0, and harmful if < 0. We report the false- and harmful-commit rates among commits, the end-to-end accuracy change ∆ measured on the audit pool, and the evaluation cost (number of dev problems scored). Two caveats keep this honest. The audit is a finite estimate, so these are observed (audit-labelled) false commits, not ground truth—but auditing at temperature 0 on a pool far larger than dev makes the reported gaps (greedy 30–100% vs. gates 0%) dwarf its sampling error. And the audit measures the realized outcome, whereas α bounds the prospective false-commit probability (§4); the two coincide here.

Two regimes. The two play complementary roles—a diagnostic with a known ground-truth answer (a unit test for acceptors), and a realistic stochastic deployment with no planted gain; neither is a full agent-system deployment, which we leave to future work. (i) Controlled: we seed the agent with one deliberately harmful instruction that the proposer can remove for a large, known true gain; the run thus contains exactly one big real improvement amid the proposer’s genuinely noisy edits. This isolates whether an accept rule keeps the real gain while rejecting noise. (ii) Stochastic: the agent is sampled at temperature 0.7 (as deployed agents are), so the dev signal is genuinely noisy even though no large improvement is available; this is the realism evidence—it tests whether an accept rule avoids chasing sampling noise. In the stochastic regime the audit is measured at temperature 0 (true quality) while the agent’s own dev signal is sampled.

5.1   Controlled: keep the real gain, reject noise

Table 1 compares greedy, a fixed-n paired test, and our anytime-valid gate (5 seeds; ± is SD across seeds). The contrast is direct: greedy commits 3–3.4 changes per run, 30–42% false and 10–33% harmful; both statistical rules commit exactly the one real improvement and nothing else (0% false, 0% harmful). At 1.5B all three rules reach the same held-out gain (∆≈+0.57), so here the gate’s advantage is hygiene rather than accuracy—it keeps the real improvement while committing none of greedy’s noise, at lower cost. At 3B the difference is one of variance: the gate reaches a tight ∆=+0.74±0.04 while greedy is a high-variance +0.54±0.30, because greedy’s occasional harmful commits cause large drops on some seeds. We therefore read the gate’s value as reliability—it removes the downside—rather than a guaranteed mean margin (the +0.20 gap is within seed noise at n=5).

[COUPÉ : fin du paragraphe 5.1 (coût d'évaluation de la porte ; cas du handicap atténué, repris en synthèse p.9).]

[p.7]

Table 1 (grille) :
Model | Accept rule | Cmt | False | Harm | ∆
 | Greedy | 3.4±1.2 | 42% | 33% | +0.57±.03
1.5B | Paired (n) | 1.0 | 0% | 0% | +0.57±.04
 | PACE | 1.0 | 0% | 0% | +0.57±.04
 | Greedy | 3.0±2.6 | 30% | 10% | +0.54±.30
3B | Paired (n) | 1.0 | 0% | 0% | +0.74±.04
 | PACE | 1.0 | 0% | 0% | +0.74±.04

Table 1: Controlled regime (5 seeds; ± is SD). Greedy commits many false/harmful changes; the gate keeps only the genuine improvement (0/5 audit-labelled false commits). At 1.5B all rules tie on held-out ∆ (the gate wins on hygiene + cost); at 3B the gate matches greedy’s mean with far lower variance (±.04 vs ±.30). Cmt: commits per run. False/Harm are audit-estimated (retrospective, temp-0); the gate’s α bounds the prospective false-commit probability.

Table 2 (grille) :
Model | Accept rule | Commits | False | ∆
 | Greedy | 20.7±1.7 | 82% | −0.05±.03
 | Paired (n) | 0.3 | 33% | +0.00
0.5B
 | Online-FDR | 0.0 | 0% | +0.00
 | PACE | 0.3 | 33% | +0.00
 | Greedy | 15.3±3.9 | 72% | −0.03±.07
 | Paired (n) | 0.7 | 67% | +0.00
1.5B
 | Online-FDR | 0.0 | 0% | +0.00
 | PACE | 0.3 | 33% | −0.01
 | Greedy | 13.3±2.1 | 100% | 0.00
 | Paired (n) | 0.0 | 0% | 0.00
3B
 | Online-FDR | 0.0 | 0% | 0.00
 | PACE | 0.0 | 0% | 0.00

Table 2: Stochastic regime, agent sampled at T =0.7 (3 seeds; ± is SD). Greedy commits 13–21 self-modifications/run (72–100% false by a temp-0 audit) and degrades the fragile 0.5B agent; every statistical gate commits <1 and holds ∆ at baseline. False% is audit-estimated (retrospective), not the prospective α bound, and for the gates is over their < 1 commit/run (a near-empty denominator).

5.2   Stochastic: don’t chase sampling noise

Table 2 reports the realistic regime and Figure 2 shows the dynamics. A sampled agent makes the dev estimate fluctuate, and greedy reads up-fluctuations as improvements: it commits a stream of 13.3–20.7 self-modifications per run (SD ≤ 3.9), 72–100% of which a temperature-0 audit deems false. By contrast every statistical gate—paired fixed-n, online-FDR, and ours—commits <1 per run: the family uniformly refuses to chase the noise, with greedy the lone offender. This commit-rate gap is the robust headline.

[COUPÉ : fin du paragraphe 5.2 (dégradation sur l'agent le plus fragile ; coût de la dérive).]

5.3   Sensitivity

The gate exposes two knobs—the level α and the dev size n—and a natural worry is that its zero false-commit rate is merely bought by setting them conservatively. Table 4 (Appendix A) shows otherwise. Sweeping α over a 10× range (0.01 to 0.10) and n over a 4× range (20 to 80), the gate commits the single real improvement at every setting, with 0% false commits

[p.8]

[COUPÉ : figure 2 (graphiques, texte des axes brouillé) et sa légende.]

and a near-constant held-out gain ∆ ≈ +0.57; greedy stays 33–53% false throughout. The anytime-valid e-process is what buys this stability: because it accumulates evidence across instances rather than thresholding one fixed-n estimate, it neither misses the gain when α is tightened nor fires on noise when n is small. A fixed-schedule online-FDR alternative behaves far worse—it lost the genuine improvement entirely at α=0.01 (∆=+0.000) and recovered only part of it at n=20 (∆=+0.41)—which is precisely why our gate is a single betting test rather than a multiplicity correction.

[COUPÉ : section 5.4 (généralisation à SVAMP et ARC-Challenge, tableau 5).]

[p.9]

Table 3 (grille) :
Claim | Support | Scope / caveat
Per-candidate false-commit prob. ≤ α | Thm. (§4) | Conditional on the candidate; not a run-level familywise bound
Greedy 30–100% false; PACE ≈0 | Tables 1–5 | Audit-labelled (temp-0), not ground truth
Removes churn / degradation | Tab. 2, Fig. 2 | Strongest on small agents; 3–5 seeds
Proposer-/loop-agnostic | Interface (paired outcomes) | Argued, not shown; prompt-level, one model family

Table 3: What PACE claims, what supports each claim, and its scope. The guarantee is per-decision; breadth across systems and model families is argued from the interface, not demonstrated.

6    Discussion and Limitations

[COUPÉ : premier paragraphe de la section 6 (cas de la tâche sans handicap, où aucune règle ne valide rien).]

When (not) to use it. The price of the gate’s safety is power, and that power scales with effect size: a large true gain crosses the e-process threshold in a handful of discordant pairs, a marginal gain needs many, and a gain too small for the evaluation budget to resolve is rejected—exactly the milder-handicap case, where the gate kept 78% of a +0.18 improvement rather than all of it. The gate is therefore the wrong tool when genuine gains are expected to be tiny and a missed improvement is costlier than a wrongly committed one; there, a higher α or a larger dev budget trades precision back for recall. In the far more common regime—noisy, reused evaluation where spurious commits are the dominant failure—it is a sensible default, at no greater cost than greedy. Finally, the gate controls false commits but inherits the dev set’s coverage: it cannot certify improvements the dev set cannot see.

What PACE does and does not claim. Table 3 summarizes the contract: PACE provides a per-decision false-commit bound under the paired null, empirically eliminates greedy’s 30–100% false commits and the resulting degradation, and claims neither higher power, a new statistic, nor system-level generality beyond its interface. Three caveats remain. We embed PACE in our own prompt-evolution loop rather than a third-party system (DSPy, ADAS); the interface is identical, but cross-system validation remains future work. Evidence uses one model family and one proposer, so proposer-agnosticism is argued at the interface level, not demonstrated. And greedy’s held-out degradation is strongest on small, fragile agents; the universally robust effect is false-commit suppression, not always a large accuracy rescue.

[COUPÉ : section 7, conclusion (redite du résumé).]

[p.10]

[COUPÉ : bibliographie, sauf les références suivantes (mot pour mot) :]

Avrim Blum and Moritz Hardt. The ladder: A reliable leaderboard for machine learning competitions. In International Conference on Machine Learning (ICML), pp. 1006–1014, 2015.

Cynthia Dwork, Vitaly Feldman, Moritz Hardt, Toniann Pitassi, Omer Reingold, and Aaron Roth. The reusable holdout: Preserving validity in adaptive data analysis. Science, 349 (6248):636–638, 2015.

Aaditya Ramdas, Fanny Yang, Martin J Wainwright, and Michael I Jordan. Online control of the false discovery rate with decaying memory. Advances in Neural Information Processing Systems (NeurIPS), 2017.

Aaditya Ramdas, Peter Grünwald, Vladimir Vovk, and Glenn Shafer. Game-theoretic statistics and safe anytime-valid inference. Statistical Science, 38(4):576–601, 2023.

Glenn Shafer. Testing by betting: A strategy for statistical and scientific communication. Journal of the Royal Statistical Society: Series A, 184(2):407–431, 2021.

[COUPÉ : p.11 (fin de la bibliographie, en-tête de l'annexe A) ; p.12, tableau 4 (sensibilité au niveau et à la taille du jeu de développement ; les chiffres sont résumés dans le texte de la section 5.3, p.7-8) et tableau 5 (deux autres tâches) avec leurs légendes.]

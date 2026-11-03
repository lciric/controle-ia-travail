"""v14 (2 novembre 2026, matin ; v13 + résultats de la nuit : lecture à graines neuves, réplication de l'arène des défenses, essaim hors échantillon, premiers tests sur modèle réel P3 et R4). Reconstruit le CV de Lazar (version du 8 octobre 2026) en HTML puis PDF (Chromium), avec des variantes de texte.
Usage : python3 construire_cv.py VARIANTE SORTIE.pdf   (VARIANTE : A | B | ... définies dans VARIANTES)"""
import sys, json, html, subprocess, pathlib

ICI = pathlib.Path(__file__).resolve().parent
# Chiffres de l'organisme, à remplacer par ceux de la suite complète et des bancs rejoués (chiffres.json, si présent).
CH = {"tests": "TESTS?", "mutations": "MUT?", "validation_v8": "VALIDATION_V8?"}
if (ICI / "chiffres.json").exists():
    CH.update(json.loads((ICI / "chiffres.json").read_text()))

PRATIQUE_A = ("<b>Research practice:</b> sealed preregistrations · SHA-256 custody of every artefact · every reported number traced to its result file · "
              "claims register audited by a separate AI agent that had produced none of it: 131 objects, among them 33 established, 19 refuted "
              "and 29 failed predictions retained")

RANG3_A = ("<b>Rank-3 ablation shifts judged verdicts where rank-1 interventions show no detectable effect, but not by removing deference.</b> "
           "On Llama-3.1-8B, six rank-1 methods (CAA steering, directional ablation, SAE feature clamping, fine-tuning against the probe direction, "
           "head/MLP zeroing) leave the judged rate unchanged; ablating a rank-3 subspace identified by SVD of activation differences at the decision "
           "point lowers it from 61% to 46.5% (N = 200, McNemar p = 0.0019), reproduced on two further baselines and direction-specific against a "
           "norm-matched random subspace. The ablation also shifts verdicts with no pressure applied (zero-pressure control), so the shift is generic; "
           "responses stored truncated at 300 characters had made it look like a safety effect, and I published the correction")

GEOM = ("<b>Safety-relevant concepts have a structured, linearly separable geometry.</b> Five concepts extracted by contrastive stories and linear probes "
        "(Qwen2.5-7B, 0.93–0.99 best-layer accuracy) organise into two distinct clusters in activation space — awareness versus deception–sycophancy; "
        "the method builds on a mechanistic eval-awareness prototype I committed three weeks before Anthropic's emotion-vectors paper. For sycophancy "
        "itself, four independent extraction methods (CAA, contrastive stories, Ridge probing, SAE decomposition) recover quasi-orthogonal directions: "
        "each captures a different facet of the construct, none a shared axis")

LECTURE = ("<b>The geometry of the readout and the geometry of the causal substrate diverge.</b> The probed direction tracks behaviour (ρ = 0.68) yet "
           "does under 1% of the causal work versus 68% for the full state; the open-source SAE (Goodfire L19) leaves 86.8% of activation variance, and "
           "the sycophancy signal, in its residual; projection- and path-patching attributions (1024 heads) share no head in their top 20. Pipeline "
           "validated beforehand by replicating a published emotion-vector protocol (circumplex geometry recovered)")

VARIANTES = {
    "A": {"pratique": PRATIQUE_A, "p3": [RANG3_A, GEOM, LECTURE]},
}
# Les variantes de texte (B, …) sont ajoutées par variantes.json à côté, si présent.
vj = ICI / "variantes.json"
if vj.exists():
    VARIANTES.update(json.loads(vj.read_text()))

def li(t):
    return f'<li>{t}</li>'

def bloc_p4():
    return """<h3>Sycophancy as Attraction Toward a Fixed Point — behavioural project <span class="d">2026</span></h3>
<div class="sub">Independent research. Manuscript in preparation; code and data public, every figure reproducible by one command: <span class="mono">github.com/lciric/sycophancy-psychophysical-law</span></div>
<ul>
<li><b>Sycophancy is not a flip rate — it is a displacement toward a destination.</b> A rate confounds the effect with where the model started. Measured as a psychophysicist would — initial state held fixed, calibrated social pressure, ordinal LLM judge — the shift is linear in the initial rating, Δ = g·(ĉ − p₀): the model closes a fixed fraction of its distance to a target (Llama-3.1-8B-Instruct; 30 items per condition × 10 replicates, item-level fit; R² = 0.77 / 0.79 for criticism / praise, g ≈ 0.70)</li>
<li><b>The law generalises out of sample.</b> Out-of-sample R² 0.73 / 0.69, criticism / praise (campaign-1 law applied to a second campaign without refitting). The second campaign has a different design — 40 items, 10 of them new; other seed plan and replication depth (5 generations per item instead of 10); significance against permutation nulls that do not assume the law, every number recomputed by the public script</li>
<li><b>The destination is set by the social frame, not by an innate disposition of the model.</b> Criticism and praise send the model toward two different targets whose confidence intervals do not overlap (ĉ ≈ 1.46 vs ≈ 2.94 on the judge's 1–5 scale). Praise does not push ratings up, it pulls them toward its target — so a highly rated item <i>loses</i> value under praise, a prediction that held</li>
<li><b>The model is held by its own concession, not by the pressure.</b> Accommodation happens in a single step and does not converge under repetition; excising the model's own earlier concession from the history restores its judgment far more than excising the pressure. The pressure's source matters while live, not once withdrawn — a temporal dissociation of normative from informational influence. <b>Consequence: the leverage point for mitigation is the concession, and single-turn evaluations stop before it</b></li>
</ul>"""

def bloc_p3(v):
    p3 = "".join(li(x) for x in v["p3"])
    return f"""<h3>Geometry and Causal Structure of Safety Concepts in Open-Weight LLMs <span class="d">2026</span></h3>
<div class="sub">Mechanistic interpretability for alignment-relevant concepts. Independent research. <span class="mono">github.com/lciric/sycophancy-construct-validity · safety-concept-vectors · eval-awareness-detection</span></div>
<ul>{p3}</ul>"""

def bloc_p5():
    return """<h3>White-Box Control of Diffuse Threats <span class="d">October 2026 – ongoing</span></h3>
<div class="sub">AI control programme; theory, preregistered simulations and tooling. The attack-side parts (threat models, sealed vault) were reviewed externally in October 2026 by the executive director of CeSIA (Centre pour la sécurité de l'IA).</div>
<ul>
<li><b>Against a threat spread over many actions or many agents, every permutation-invariant monitor statistic is blind.</b> An additivity lemma and a negative theorem by invariance: maximum, mean or count-above-threshold have power equal to their false-positive rate against an attacker who preserves the multiset of scores; time and agents are unified through permutation subgroups, so one theory serves sequential and swarm monitoring. A preregistered simulation (October 2026) confirmed all 31 predictions — most of them instrument checks, as the sealed text said in advance — and showed that Ville-type thresholds give 21–35% false alarms under episode effects unless calibrated on whole honest episodes</li>
<li><b>Against an adaptive attacker, a mixed-equilibrium defence beats retraining on the attack history.</b> Preregistered simulation, replicated at a fresh seed: +0.11 and +0.13 detection rate over the retrained defence. Synthetic arena, no language model</li>
<li><b>Swarm monitoring, tested where the model had never been computed.</b> Second preregistered test, on never-computed cells and the real honest scores of my first activation experiment: 4 of 7 risky predictions held, 2 were refuted and the refutations replicated (the surrogate underestimated power by up to 0.2), 1 was inconclusive</li>
<li><b>First tests on a real model.</b> Llama-3.1-8B, hidden-instruction saboteur inflating a declared cost (2,400 scored actions): plain in behaviour, yet no generic probe cleared its random-probe floor (bounded null: power 0.8 only near 0.46 SD; 0.33 at a noise floor). Under a weaker instruction the threat becomes diffuse: the best per-action black-box monitor catches 27% of sabotage actions at 1% false alarms, LLM judges of 3B and 8B at most 3% (preregistered; one reservation, on the controls). White-box versus black-box comparison: sealed before any data, corrected replay under way</li>
</ul>"""

def bloc_p6():
    return f"""<h3>Ideation Organism — an automated research system in which no agent grades its own homework <span class="d">2026 – ongoing</span></h3>
<div class="sub">Built to generate and kill AI-control hypotheses without the loop optimising its own judge. Code, tests and offline demonstrations public: <span class="mono">github.com/lciric/ideation-organism</span></div>
<ul>
<li><b>The role that produces an artefact never holds the key that evaluates it.</b> Proposer agents from several providers (Claude, Kimi, Gemini) write idea cards with closed fields; a gatekeeper classifies them by form only and seals the too-concrete ones in a vault no agent reads; cross-provider judges score blind to each other; an anti-repetition memory and a three-arm "bisociator" pair ideas; a novelty check reads arXiv and OpenAlex metadata; preregistered death tests run in a sandbox (no network, no key, syscall-filtered) and are verified by a model of another family; survivors pass to the next generation as sealed, anonymous cards</li>
<li><b>Guards are trusted only once seen to refuse something.</b> Every guard is tested on a healthy case and on an artefact; {CH["tests"]} tests; mutation benches of {CH["mutations"]} deliberate code mutations, every one killed for the expected reason; spend caps recomputed at every stage; twenty independent counter-readings, each with a finding → file:line → test table. One found that until v56 no code read the death-test verdicts; since v57b the verdict comes only from the sealed result file (tested offline)</li>
<li><b>Evidence so far.</b> Planted world: the statistical judge (selection by sealed bets, e-values) promoted 8 of 8 true laws and 0 of 8 false ones. Attacked by 27 scripted cheaters, the judge let through 4 that recopy or blend promoted laws until given a null fitted on all known laws (exploratory); that null is now its only one, {CH["validation_v8"]}. Real episode bank: planted effects recovered; on the real monitors, "not enough power" rather than a finding, and a power curve shows why; then 288 fresh-seed episodes of the same 96 tasks, read once under a sealed plan and checked by a fresh reader: the judge promoted the 3 planted links, none of 19 null controls, and no real link. Real agents: 29 idea cards, 17 distinct ideas; in a second round the LLM judges sat at their ceiling (11 of 12 rated notable, κ = 0), stated as a weakness. Loop now closed in code and dry-run in the real sandbox; not yet run with real agents</li>
</ul>"""

def page(v):
    blocs = {"p4": bloc_p4(), "p3": bloc_p3(v), "p5": bloc_p5(), "p6": bloc_p6()}
    corps = "\n".join(blocs[k] for k in v["ordre"])
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 8mm 11.5mm 8mm 11.5mm; }}
* {{ box-sizing: border-box; }}
body {{ font-family: 'DejaVu Sans', sans-serif; font-size: 7.3pt; line-height: 1.175; color: #111; margin: 0; }}
.tag {{ font-size: 6.3pt; letter-spacing: 0.24em; color: #444; text-transform: uppercase; margin: 0 0 1pt 0; }}
h1 {{ font-size: 17.5pt; letter-spacing: 0.03em; margin: 0 0 3pt 0; font-weight: bold; }}
.contact {{ font-size: 8.3pt; margin: 0 0 2pt 0; }}
.interests {{ margin: 0 0 4pt 0; }}
.bandeau {{ border-left: 2pt solid #111; padding: 2pt 0 2pt 7pt; margin: 0 0 6pt 0; }}
.bandeau p {{ margin: 0 0 1pt 0; }}
h2 {{ font-size: 8.6pt; letter-spacing: 0.12em; text-transform: uppercase; margin: 7pt 0 3pt 0; padding-bottom: 2pt; border-bottom: 0.8pt solid #111; }}
h3 {{ font-size: 9.2pt; margin: 4pt 0 1pt 0; display: flex; justify-content: space-between; align-items: baseline; }}
h3 .d {{ font-weight: normal; font-size: 7.9pt; }}
.sub {{ font-style: italic; color: #333; margin: 0 0 1pt 0; }}
.right {{ text-align: right; color: #333; margin: 0 0 1pt 0; }}
.mono {{ font-family: 'DejaVu Sans Mono', monospace; font-size: 6.6pt; color: #555; font-style: italic; }}
.monon {{ font-family: 'DejaVu Sans Mono', monospace; font-size: 6.6pt; color: #555; }}
ul {{ list-style: none; margin: 1pt 0 2pt 0; padding: 0; }}
ul li {{ position: relative; padding-left: 11pt; margin: 0 0 1.2pt 0; text-align: justify; }}
ul li::before {{ content: '◆'; position: absolute; left: 0; top: 0; font-size: 6.8pt; }}
.small-h {{ font-weight: bold; margin: 6pt 0 0 0; }}
p {{ margin: 0 0 2pt 0; }}
.skills p {{ margin: 0 0 2.5pt 0; }}
.brk {{ break-before: page; }}
ul.left li {{ text-align: left; }}
</style></head><body>
<div class="tag">AI SAFETY RESEARCHER • AUTOMATED ALIGNMENT RESEARCH • AI CONTROL • INTERPRETABILITY • SYCOPHANCY</div>
<h1>LAZAR CIRIC</h1>
<div class="contact">lciric@ens-paris-saclay.fr • +33 6 14 79 44 28 • Paris, France • github.com/lciric • linkedin.com/in/lazar-ciric-55a23913b</div>
<div class="interests"><b>Research interests:</b> <i>Automated research that resists gaming • AI control against diffuse threats • Sycophancy and social influence in LLMs • Readable versus causal structure in activations • Construct validity of probes, steering and LLM judges</i></div>
<div class="bandeau">{v["bandeau"].replace("TESTS_BANDEAU", CH["tests"] + " tests, " + CH["mutations"] + " of " + CH["mutations"] + " code mutations caught")}</div>

<h2>Independent Research Programme — AI Safety · 2025 (alongside my consulting role) – 2026 (full time since March)</h2>
{corps}
<div class="small-h">Earlier projects (2025)</div>
<h3>P2 — Does Quantization Kill Interpretability? <span class="d">2025</span></h3>
<ul><li>Five mechanistic analyses comparing RTN vs GPTQ on GPT-2 (TransformerLens): RTN destroys all 10 induction heads, GPTQ preserves 10/10; SAE feature survival 45% vs 60% <span class="monon">github.com/lciric/does-quantization-kill-interpretability</span></li></ul>
<h3>P1 — GPTQ from Scratch <span class="d">2025</span></h3>
<ul><li>Full PyTorch reimplementation of GPTQ (Frantar et al. 2022) — Hessian-based quantization, grouping, act-order; tested on GPT-2, GPT-2-XL (+5.3% PPL), OPT-1.3B, Llama-3-8B <span class="monon">github.com/lciric/gptq-from-scratch</span></li></ul>

<h2>Professional Experience</h2>
<h3>AI Lead Consultant — EPSA Innovation, Paris <span class="d">2024 – 2026</span></h3>
<ul><li>Internal AI referent leading client engagements on AI/ML R&amp;D; technical due diligence on model efficiency, training infrastructure and deployment</li></ul>

<h2>Master Thesis — Computational Neuroscience</h2>
<h3>Geometry of population activity in spiking networks with low-rank structure</h3>
<div class="sub">ENS, Laboratoire de Neurosciences Cognitives Computationnelles (Ostojic lab) · Supervisor: Srdjan Ostojic · Co-authored: Cimeša, Ciric &amp; Ostojic, PLOS Computational Biology (2023) · Presented at Cosyne 2021 &amp; 2022, Bernstein 2021</div>
<div class="right">2019 – 2020 → PLOS Comp. Biol. 2023</div>
<ul>
<li><b>Question: do the analytic insights of low-rank rate networks — connectivity predicting the geometry of low-dimensional dynamics — transfer to biologically realistic spiking networks?</b> Low-rank structure on sparse random E–I connectivity, 12,500 integrate-and-fire neurons (Brian2), compared against mean-field predictions for statistically identical rate networks</li>
<li><b>Each spiking neuron maps one-to-one onto a rate unit: connectivity predicts the geometry of population activity</b>, and the readout timescale, not the firing regime, decides the geometry you see — predictions hold under sparse synchrony and regular firing alike, up to a spiking network performing perceptual decision-making</li>
</ul>

<h2>Research Internships</h2>
<h3>Visiting Researcher — NeuroSpin (CEA Saclay), director Stanislas Dehaene <span class="d">2023</span></h3>
<ul><li>Functional brain imaging (fMRI) and genetic data analysis on large-scale cohorts within the ERC MathBrain project</li></ul>
<h3>Research Intern — NeuroPSI (CEA Saclay), supervisor Alain Destexhe <span class="d">2022</span></h3>
<ul><li>Bifurcation analysis of coupled mean-field cortical networks: multistability, hysteresis and cross-regulation in interconnected columns (MATCONT)</li></ul>
<h3>Research Intern — IBM Research Zurich, In-Memory Computing group <span class="d">2020 – 2021</span></h3>
<div class="sub">Supervisors: Abu Sebastian &amp; Manuel Le Gallo · Co-authored paper in Neuromorphic Computing and Engineering (2022)</div>
<ul>
<li><b>Precision is a resource, and robustness to weight perturbation is a property of the representation, not of the hardware.</b> Developed bit-slicing algorithms for low-precision DNN inference on analog phase-change-memory crossbars — each weight split across several low-bit devices, the same decomposition that underlies today's low-bit LLM quantization — with quantization-aware training (straight-through estimator) to make learned representations robust to device noise and conductance drift: &gt;94% CIFAR-10 accuracy sustained over a month of physical drift</li>

</ul>
<h3>Visiting Research Student — Lawrence Berkeley National Lab, supervisor Zarija Lukic <span class="d">2017 – 2019</span></h3>
<ul><li>Large-scale cosmological simulations in C++ on NERSC HPC clusters; statistical analysis of simulation outputs</li></ul>

<h2>Education</h2>
<ul class="left">
<li><b>Mines Paris-PSL</b> — Ingénieur Civil, Mathematical Statistics, Machine Learning &amp; Applied Probabilities (2025)</li>
<li><b>École Normale Supérieure (Ulm)</b> — M2 Research, Computational Neuroscience (Cogmaster), 2020 — mention Bien</li>
<li><b>École Normale Supérieure Paris-Saclay</b> — Normalien, Fundamental Physics (2016–2020) — competitive national examination</li>
<li><b>Lycée Louis-le-Grand</b> — MPSI / PSI*, Classes Préparatoires (2014–2016)</li>
</ul>

<h2>Publications</h2>
<ul class="left">
<li><b>Geometry of population activity in spiking networks with low-rank structure</b> — Cimeša, Ciric &amp; Ostojic, <i>PLOS Computational Biology</i> (2023)</li>
<li><b>Precision of bit slicing with in-memory computing based on analog phase-change memory crossbars</b> — Le Gallo, Nandakumar, Ciric et al., <i>Neuromorphic Computing and Engineering</i> (2022)</li>
</ul>

<h2>Skills</h2>
<div class="skills">
<p><b>Frameworks:</b> PyTorch, JAX, HuggingFace Transformers, TransformerLens, nnsight, SAE-lens, Brian2, scikit-learn, NumPy/SciPy · Python, C++, Bash</p>
<p><b>Scale &amp; infrastructure:</b> single- and multi-GPU A100/H100 instances for inference, ablation and quantization of 8B-parameter models; HPC clusters at NERSC (LBNL); evaluation campaigns of thousands of sealed generations and LLM-judge API calls</p>
<p><b>Research engineering &amp; generative-AI systems:</b> from-scratch reimplementation of published methods (GPTQ); end-to-end LLM evaluation systems (generation, LLM-as-judge scoring, statistical verification) and steering/ablation toolchains; multi-agent orchestration with sandboxed execution; Git, Linux</p>
<p><b>Open source:</b> code, prompts and data of the four projects above are public at github.com/lciric; the automated research loop at github.com/lciric/ideation-organism · <b>Methods:</b> mechanistic interpretability (SAE, path patching, circuit analysis), linear probes, activation steering &amp; subspace ablation, exact/permutation nulls, construct-validity testing, low-rank network theory · <b>Spoken:</b> French, English, Serbian</p>
</div>
</body></html>"""

if __name__ == "__main__":
    var, sortie = sys.argv[1], pathlib.Path(sys.argv[2]).resolve()
    h = ICI / f"cv-{var}.html"
    h.write_text(page(VARIANTES[var]), encoding="utf-8")
    js = f"""const {{ chromium }} = require('playwright');
(async () => {{ const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://{h}'); await p.pdf({{ path: '{sortie}', format: 'A4', printBackground: true, preferCSSPageSize: true }});
await b.close(); }})();"""
    j = ICI / "imprimer.js"; j.write_text(js)
    subprocess.run(["node", str(j)], check=True)
    print("écrit", sortie)

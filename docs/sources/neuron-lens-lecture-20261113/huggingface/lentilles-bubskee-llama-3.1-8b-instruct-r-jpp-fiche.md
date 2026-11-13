---
license: llama3.1
base_model: meta-llama/Llama-3.1-8B-Instruct
library_name: pytorch
datasets:
- Salesforce/wikitext
tags:
- interpretability
- workspace-lens
- r-lens
- jpp-lens
- experimental
---

# R and J++ lenses for Llama 3.1 8B Instruct

New lenses for **[meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)**: fixed R and J++ maps at all **31 non-final decoder layers**, a prompt/vector/neuron reader, and frozen readout evaluations. Released by [bubskee](https://huggingface.co/bubskee). Built with Llama.

These are independent fits of the original [R-lens](https://www.lesswrong.com/posts/nv8oedrnLXKRzNEL9/r-lens-making-j-lens-more-faithful-on-early-layers) and [J++ lens](https://www.lesswrong.com/posts/nc9dHfcB22JdMzGbr/j-lens-jacobian-filtering-enables-more-faithful-workspace) methods, building on [J-lens and workspace representations](https://transformer-circuits.pub/2026/workspace/index.html). Credit for those methods goes to their authors. Thank you to **BlueDot Impact for funding this work**.

In simple terms: take an activation inside the model, map it into the final layer’s coordinates, and ask the model’s vocabulary head which tokens it lines up with. **R** fits that map using relevance-propagation rules in the backward pass. **J++** learns a signed mixture of eight activation-clustered R experts. The released maps are fixed matrices; those fitting experts are activation clusters, not native mixture-of-experts components.

If you’re poking at neurons in these models, I’d love examples where the lenses disagree with each other or with an intervention. Disagreements and boring failures are useful too. ^^ These readouts are hypotheses to investigate, not causal labels for neurons.

## Try it

Accept the base model’s access terms and authenticate with Hugging Face before its first download. Base-model weights download separately. The release was checked on CUDA using the pinned packages; CPU and MPS are reader options without independent full-model validation here. Quantized base-model compatibility has not been established.

```bash
hf download bubskee/llama-3.1-8b-instruct-r-jpp-lenses --local-dir lenses
pip install -r lenses/requirements.txt
python lenses/read_lenses.py --release lenses \
  --prompt 'Fact: The number of legs on the animal that spins webs is' \
  --layers 16
```

This prints logit, R, and J++ top-ten readouts. Use `--kind jpp` for one lens or `--raw` for the full vocabulary. Default ranking uses the saved upstream filter for tokens without letters or digits, with evaluation candidate tokens spared. Inputs are raw completion prefixes; no chat template is added. The default position is the final token, with a 512-token prompt cap.

```bash
python lenses/read_lenses.py --release lenses --neuron 1234 --layers 16
python lenses/read_lenses.py --release lenses --vector activation.safetensors --layers 16
```

Neuron 1234 is the gated dense-MLP channel before `down_proj` in that decoder block. The reader projects its residual-write direction through each lens and shows both signs. An actual context also supplies the activation magnitude and other residual contributions. Vector mode expects a finite nonzero raw vector named `activation`, shape `[4096]`. Prompt mode’s `--save-activation` writes that format. The Python interface exposes `WorkspaceLenses.capture`, `transport`, `logits`, `read`, and `neuron_direction`.

For Neuronpedia’s legacy J-lens-shaped payload, convert either map set without changing its matrices:

```bash
python lenses/export_neuronpedia.py --release lenses --output neuronpedia-export
```

## Model and layer contract

- Base: `meta-llama/Llama-3.1-8B-Instruct`, pinned revision `0e9e39f249a16976918f6564b8830bc894c89659`.
- Source: zero-based decoder **block outputs 0–30**, width **4096**.
- Target: output of block **31**, **before final RMSNorm**.
- Transport: raw residual `h @ J.T`, with no whitening or input normalization.
- Native model: BF16. Maps and readout head: FP32. Readout uses Llama’s native FP32 RMSNorm with its plain learned gain, then its native vocabulary head and configured logit scaling.

The native Llama decoder, grouped-query attention, and Llama 3.1 RoPE settings are retained. No base-model weights are updated. Native-checkpoint tests verified parameter samples and exact forward agreement with the R rules installed. `smoke.json` records the standalone reader checks against the frozen fitting readout.

## What they recover

The primary comparison uses seven fixed source layers: **4, 8, 12, 16, 20, 24, 28**. A concept’s rank is its best over those seven layers. Scores average concepts within prompts, prompts within tasks, and tasks equally for the macro. These are concept-readout scores, not generated-answer accuracy.

**The J baseline is Neuronpedia’s existing 461-prompt fit; these new R/J++ fits use 64 prompts.** This is an unequal-budget comparison, not a matched J/R/J++ experiment. The existing J weights are not republished here. Its repository, immutable revision, file hash, and original config are in `provenance/baseline.json`.

| Metric | Logit lens | Existing J | R | J++ |
| --- | ---: | ---: | ---: | ---: |
| Macro top-1, full vocabulary | 17.1% | 16.0% | 21.2% | 29.5% |
| Macro top-10, full vocabulary | 31.1% | 41.9% | 45.1% | 52.7% |
| Macro top-1, filtered | 17.1% | 17.9% | 24.1% | 31.2% |
| Macro top-10, filtered | 31.1% | 45.8% | 48.9% | 56.0% |

Filtered top-ten recovery by task:

| Task | Logit lens | Existing J | R | J++ |
| --- | ---: | ---: | ---: | ---: |
| association | 7.8% | 20.8% | 19.5% | 31.2% |
| multihop | 58.3% | 81.2% | 75.0% | 79.2% |
| multilingual | 41.7% | 56.0% | 53.2% | 58.3% |
| poetry | 8.9% | 7.1% | 12.5% | 17.9% |
| typo | 39.0% | 63.6% | 84.4% | 93.5% |

The scored heldout set contains **281 prompts** and **416 prompt/concept pairs**, disjoint from **68 calibration prompts**. An em dash means the scored set has no entry for that task or the macro is undefined. The upstream five-task macro requires all five tasks; if the competence-filtered set omits any task, we preserve that missing macro rather than silently average a smaller set. Unrepresentable concepts with no single-token surface are omitted by the upstream scorer. Inspect the saved ranks and coverage by task before drawing conclusions. Best-over-depth recovery is more permissive than reading one predetermined layer.

`evaluation/` also includes all-layer summaries, per-layer results, raw ranks, and the split. The all-layer result uses more depth opportunities than the seven-layer primary comparison. These models have different competence-filtered cohorts, tokenizers, and depths; their scores are not a matched cross-model ranking.

## Fitting and provenance

Both new lenses use **64 neutral WikiText sequences**, capped at 128 tokens. The first 16 and final token positions are excluded: **7100 retained positions**. R pools retained-position relevance statistics. J++ uses eight activation clusters per layer, PCA dimension 64, seed 0, minimum support 50 positions, and pooled-R fallback for under-supported experts: **26/248 expert slots** use fallback.

R is exported from FP32 pooled statistics. J++ calibrates a signed mixture of persisted FP16 expert means and exports combined maps in FP32. Calibration uses the canonical upstream per-layer pair-macro top-ten objective, default three-start search, and a fixed stratified 20% split. The other 80% is held out. The native BF16 next-token/leading-subword correctness gate is recorded separately from an exact complete-token audit; it does not establish full-answer correctness. Association and typo items remain ungraded by that competence gate, following the upstream recipe.

Fitting uses [the original J++ implementation](https://github.com/safety-research/jpp_lens) at `d7efc0de372e20589e899188c0cfe8434acc63ec`. Local aliases preserve the native forward while applying the matching RMSNorm and gated-MLP backward rules. Tiny real-architecture tests checked FP32/BF16 forward identity, analytic derivatives, and restoration. The native model and first full prompt also passed validation. Checkpoint recovery and bounded-memory expert export were checked against uninterrupted and canonical calculations.

`provenance/` contains the frozen recipe, baseline identity, support/coefficients, corpus and per-prompt hashes, retained-position records, environment, and native tests. `training/` contains the exact fitting/compatibility source used. The WikiText dataset revision was not independently pinned before download; saved hashes identify the corpus used. Raw training text, raw activations, expert banks, sufficient-statistic checkpoints, optimizer states, and base-model weights are not bundled. `SHA256SUMS` covers the payload.

## Original work and funding

- **J-lens / workspace representations:** Wes Gurnee and colleagues, [*Verbalizable Representations Form a Global Workspace in Language Models*](https://transformer-circuits.pub/2026/workspace/index.html); [reference code](https://github.com/anthropics/jacobian-lens).
- **R-lens:** Camila Blank, Agam Bhatia, and Neel Nanda, [*R-lens: Making J-lens More Faithful on Early Layers*](https://www.lesswrong.com/posts/nv8oedrnLXKRzNEL9/r-lens-making-j-lens-more-faithful-on-early-layers); [authors’ lenses](https://huggingface.co/camilablank/workspace-lenses).
- **J++ lens:** Kola Ayonrinde and Jack Lindsey, [*J++ Lens: Jacobian Filtering Enables More Faithful Workspace Lenses*](https://www.lesswrong.com/posts/nc9dHfcB22JdMzGbr/j-lens-jacobian-filtering-enables-more-faithful-workspace); [code](https://github.com/safety-research/jpp_lens) and [authors’ lenses](https://huggingface.co/koayon/jpp-lenses).
- **Existing J baseline:** [Neuronpedia](https://huggingface.co/neuronpedia/jacobian-lens), with its fitting metadata retained in the release provenance.
- **Base model:** the creators of [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct).
- **Funding for these independent fits:** thank you to **BlueDot Impact**.

The HF license metadata follows the base model’s terms. Reader and fitting adaptations are Apache-2.0 software; see `CODE_LICENSE`, `NOTICE`, and `BASE_MODEL_TERMS.md`. This is an independent release, not an authors’ release or endorsement.

## Limits and useful feedback

These are small-data fits on a small public benchmark with single-token concept surfaces. They do not establish faithful decoding of arbitrary hidden objectives, neuron meaning independent of context, or the presence of a global workspace in either model. No causal intervention study accompanies this release.

Open a [HF discussion](https://huggingface.co/bubskee/llama-3.1-8b-instruct-r-jpp-lenses/discussions) with the prompt, fitted layer, token position, neuron/channel index if relevant, raw/filtered setting, and what you tested. Please keep private prompts out of public reports.

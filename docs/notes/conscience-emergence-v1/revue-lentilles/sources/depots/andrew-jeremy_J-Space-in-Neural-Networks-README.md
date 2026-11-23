# J-Space Neural Analyzer

Andrew Kiruluta, UC Berkeley, CA.

A reproducible Python repository for analyzing **semantically indexed, output-accessible internal representations** in an input causal neural network architecture.

The toolkit operationalizes the revised *J-Space Dynamics* proposal. It does not assume that J-space is a literal physical workspace, that transformer layers form a stationary flow, or that any result establishes consciousness. It measures whether label-aligned activation directions are stable, sparse, predictive, dynamically useful, and causally connected to output behavior.

## What the repository implements

| Component | Implemented measurement |
|---|---|
| J-dictionary | Average local future-output gradients for selected tokens at selected layers |
| Dictionary validity | Mutual coherence, active Gram conditioning, bootstrap direction stability |
| Sparse J-code | Nonnegative elastic-net coding with optional top-`s` support |
| Code validity | Reconstruction error, active-coordinate count, perturbation support stability |
| Continuation robustness | Target-versus-competitor margin, reduced Hessian, empirical Taylor radius |
| Ordered-span binding | Teacher-forced path gradients, binding residual, order contrast direction |
| Depth dynamics | Layer-indexed ridge/EDMD maps with held-out normalized closure error |
| Position dynamics | One-step and delay-embedded alternatives; no automatic Markov assumption |
| Persistence | Covariance-whitened finite-window singular values |
| J-Fisher geometry | Monte Carlo output-score Fisher metric restricted to J-coordinates |
| Longitudinal analysis | Multivariate consolidation profile and secondary WCI calculation |
| Reporting | JSON, CSV, Markdown, NumPy arrays, dictionary/code plots, closure plots |

## Supported model paths

1. **Offline tiny transformer** — requires no model download and validates the full pipeline.
2. **Hugging Face decoder-only language models** — GPT-2, Llama-like, Mistral, Qwen, OPT, Bloom, GPT-NeoX-style block layouts.
3. **Custom PyTorch adapters** — implement the `CausalLMAdapter` interface for nonstandard architectures.

The current scientific target is a causal language model because J-space is indexed by verbalizable token or span outputs. A classifier can be adapted by treating class labels as the output vocabulary, but sequence binding and autoregressive path analyses then need task-specific definitions.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e .
```

For Hugging Face models:

```bash
pip install -e '.[huggingface]'
```

For development:

```bash
pip install -e '.[dev]'
```

## Run the complete offline demonstration

```bash
jspace-analyze demo
```

Equivalent command:

```bash
jspace-analyze run --config configs/tiny_demo.yaml
```

Run advanced probes independently on CPU:

```bash
jspace-analyze run --config configs/tiny_robustness.yaml
jspace-analyze run --config configs/tiny_binding.yaml
jspace-analyze run --config configs/tiny_fisher.yaml
```

For large GPU models the probes can be combined, but separate runs make memory use, numerical failures, and runtime attribution easier to diagnose.

Outputs are written to `runs/tiny_demo/`:

```text
REPORT.md
report.json
metrics.csv
resolved_config.json
dictionary_layer_*.npy
sample_gradients_layer_*.npy
codes_layer_*.npy
j_fisher.npy
dictionary_gram_layer_*.png
mean_codes_layer_*.png
depth_closure.png
```

The tiny model is deliberately small and randomly initialized by default so the complete pipeline can be validated without downloads. Optional demo training can be enabled in the YAML. Its outputs validate software behavior only; they are not scientific evidence for the paper's hypotheses.

## Analyze a Hugging Face model

Edit `configs/huggingface_example.yaml`, then run:

```bash
jspace-analyze run --config configs/huggingface_example.yaml
```

For an already downloaded model, set:

```yaml
model:
  adapter: huggingface
  name_or_path: /absolute/path/to/model
  local_files_only: true
```

Start with a small concept dictionary and one or two layers. Gradient cost scales approximately with:

```text
number of prompts × number of concepts × number of analyzed layers
```

Second-order and Fisher analyses add repeated forward/backward passes and should initially be enabled on one prompt and one layer.

## Configuration anatomy

```yaml
model:
  adapter: huggingface
  name_or_path: gpt2

data:
  prompts_file: ../data/prompts.jsonl

analysis:
  layers: [2, 5, 8, 11]
  concepts: ../data/concepts.yaml

  dictionary:
    gamma: 0.95
    bootstrap_repeats: 20

  coding:
    l1: 0.02
    l2: 0.0001
    top_s: 6

  dynamics:
    enabled: true
    delay_widths: [1, 2, 3]

  robustness:
    enabled: true
    layer: 8
    prompt: "The planned answer is"
    target: " Paris"
    competitors: [" London", " Rome"]

  binding:
    enabled: true
    layer: 8
    span_a: " Alice trusts Bob"
    span_b: " Bob trusts Alice"

  fisher:
    enabled: true
    layer: 8
    samples: 16
```

### Prompt format

`JSONL`, one prompt per line:

```json
{"id":"p001","text":"Alice trusts Bob because"}
{"id":"p002","text":"Bob trusts Alice because"}
```

### Concept format

```yaml
concepts:
  - label: truth
    text: " truth"
    competitors: [" lie"]
  - label: lie
    text: " lie"
    competitors: [" truth"]
```

Whitespace can affect tokenization in byte-pair tokenizers. Inspect token IDs before interpreting results.

## Scientific workflow

A defensible experiment should follow this order:

1. **Dictionary validation** — reject unstable, highly coherent, or poorly conditioned concept dictionaries.
2. **Code validation** — reject analyses with high reconstruction error or unstable sparse supports.
3. **Closure validation** — do not interpret persistence unless held-out dynamics beat the mean and simpler baselines.
4. **Incremental prediction** — compare J-space features with logits, entropy, tuned/template lenses, and SAE probes.
5. **Causal intervention** — test matched Euclidean and Fisher perturbations.
6. **Longitudinal replication** — use multiple seeds, continuous behavioral metrics, and multivariate change-point tests.

## Important distinctions

### Canonical J-lens versus this implementation

The originating J-lens averages hidden-to-hidden Jacobians and then applies the model's normal output decoding. This repository uses an efficient **output-functional gradient dictionary**: gradients of selected future token or span scores with respect to a tapped intermediate state. The two constructions are closely related through vector-Jacobian products but are not treated as mathematically identical. See `docs/METHODS.md`.

### Empirical radius, not a formal certificate

The second-order routine reports `empirical_taylor_radius`. It uses the local reduced Hessian operator norm. It is not a certified radius unless a curvature bound is verified over the entire perturbation ball.

### Non-autonomous dynamics

Each transformer layer has distinct parameters. The code therefore fits layer-indexed maps and finite-window propagators. It does not pool all layers into one stationary Koopman operator by default.

### WCI is secondary

The primary longitudinal endpoint is the vector:

```text
[hub/connectivity, concentration with collapse guard, persistence]
```

The scalar Workspace Consolidation Index is only a secondary summary.

## Longitudinal checkpoint aggregation

Run the main analysis separately for each checkpoint, then create a manifest based on `configs/checkpoint_manifest_template.yaml`:

```bash
jspace-analyze longitudinal \
  --manifest configs/checkpoint_manifest.yaml \
  --out runs/longitudinal
```

The command writes a multivariate profile, a secondary WCI trace, and a descriptive candidate-change score. It does not label the change a phase transition.

## Custom architecture integration

Read `docs/HOWTO_CUSTOM_MODEL.md` and `examples/custom_adapter.py`. A custom adapter must provide:

- text or symbol encoding;
- decoder block modules;
- model logits;
- token/span IDs and labels;
- an `encode_ids` path for teacher-forced span scoring.

## Tests

```bash
pytest
```

The test suite covers sparse-code recovery, dynamics closure, model hooks, local gradient extraction, and an end-to-end tiny-model smoke test.

## Repository map

```text
src/jspace_analysis/
  analysis/       dictionaries, coding, robustness, binding, dynamics, Fisher, longitudinal
  models/         model-neutral interface, tiny transformer, Hugging Face adapter
  reporting/      Markdown/JSON/CSV reports and plots
  cli.py          command-line interface
configs/          runnable examples
data/             toy prompts and concept lexicon
docs/             methods, architecture, limitations, custom-model guide, revised paper
examples/         custom adapter scaffold
tests/            unit and integration tests
```

## Safety and interpretation

This software is intended for interpretability, model evaluation, and defensive auditing. Internal readouts can be incomplete, displaced, or deliberately optimized around. A clean J-space result does not prove that concerning computation is absent elsewhere in the model.

## License

MIT.

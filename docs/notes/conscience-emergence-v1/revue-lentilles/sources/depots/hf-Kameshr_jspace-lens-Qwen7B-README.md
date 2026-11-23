---
license: mit
language:
  - en
  - zh
  - ja
tags:
  - jacobian-lens
  - global-workspace
  - jspace
  - transformer
  - qwen
  - llama
library_name: jspace
---

# jspace-lenses — Pre-fitted Jacobian Lens Files

Pre-fitted J-lens matrices for Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct, produced by
[jspace](https://github.com/kameshkanna/jspace) — an open replication of
[Lindsey et al., Anthropic 2026](https://transformer-circuits.pub/2026/workspace/index.html).

## What is a J-lens?

The Jacobian Lens captures how each intermediate layer maps to the final residual stream:

```
J_l = E_{t, t'>=t, prompt} [ dh_final_{t'} / dh_l_t ]
lens(h_l) = softmax(W_U · norm(J_l @ h_l))
```

Each `.pt` file contains one `(d_model × d_model)` matrix per layer, fitted over 1000 diverse
prompts using a fused Hutchinson VJP estimator. Loading it lets you read out what any layer
is "thinking" without a second model or probe training.

## Files

| File | Model | d_model | Layers | n_proj | n_prompts |
| --- | --- | --- | --- | --- | --- |
| `qwen2.5-7b-instruct/jlens.pt` | Qwen/Qwen2.5-7B-Instruct | 3584 | 28 | 32 | 1000 |

Each file is self-describing — load it and inspect `metadata` keys directly.

## Usage

```bash
pip install git+https://github.com/kameshkanna/jspace.git
```

```python
from huggingface_hub import hf_hub_download
from jspace import HookedModel, JacobianLens, WorkspaceAnalyzer

# download lens
path = hf_hub_download(
    repo_id="Kameshr/jspace-lenses",
    filename="qwen2.5-7b-instruct/jlens.pt",
)

# load and analyse
model  = HookedModel("Qwen/Qwen2.5-7B-Instruct")
jlens  = JacobianLens.load(path, model=model)

analyzer = WorkspaceAnalyzer(jlens)
report   = analyzer.analyse("The capital of France is Paris, which is also known as")

WorkspaceAnalyzer.print_report(report)
print(f"Workspace: L{report.workspace_start}–{report.workspace_end}")
print(f"Peak capacity: {report.peak_capacity} active concepts")
```

## Inspect metadata

```python
import torch
d = torch.load("jlens.pt", map_location="cpu", weights_only=True)
for k in ["version", "model_id", "d_model", "n_layers", "n_proj", "n_prompts", "corpus_size", "created_at"]:
    print(f"{k}: {d[k]}")
```

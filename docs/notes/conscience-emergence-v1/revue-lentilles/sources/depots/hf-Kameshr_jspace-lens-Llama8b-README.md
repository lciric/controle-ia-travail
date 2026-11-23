---
license: mit
language:
  - en
  - zh
  - ja
tags:
  - interpretability
  - mechanistic-interpretability
  - jacobian-lens
  - global-workspace
  - jspace
  - llm-internals
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
| `llama-3.1-8b-instruct/jlens.pt` | meta-llama/Meta-Llama-3.1-8B-Instruct | 4096 | 32 | 32 | 1000 |

Each file is self-describing — load it and inspect `metadata` keys directly.


## Inspect metadata

```python
import torch
d = torch.load("jlens.pt", map_location="cpu", weights_only=True)
for k in ["version", "model_id", "d_model", "n_layers", "n_proj", "n_prompts", "corpus_size", "created_at"]:
    print(f"{k}: {d[k]}")
```

---
license: mit
tags:
- interpretability
- jacobian-lens
- relp
- template-lens
- global-workspace
---

# J-lens / R-lens / Template-lens artifacts

 **Jacobian-lens (J-lens)** and **RelP-lens (R-lens)** pairs for eight models,
plus the **template lens** for Qwen3.6-27B. 

All lenses read out, at every layer and token position, the vocabulary tokens an activation is
*poised to be verbalized as* (the J-space / global-workspace method,
*Verbalizable Representations Form a Global Workspace in Language Models*, 2026). R-lens is introduced in https://www.lesswrong.com/posts/nv8oedrnLXKRzNEL9/r-lens-making-j-lens-more-faithful-on-early-layers.

- **J-lens** — the standard Jacobian lens: `J_ℓ` is the averaged first-order (Jacobian) map from
  layer ℓ to the target layer, estimated with the official `jlens.fit`.
- **R-lens (RelP)** — the same estimator, but the Jacobian is read through an **LRP-modified
  backward graph** (RelP, arXiv:2508.21258): the LN-rule (RMSNorm `rsqrt` detached), identity-rule
  (SiLU `sigmoid` factor detached), and half-rule (SwiGLU product half-detached). **Forward values
  are bit-identical to the standard build** — only the gradients differ, so J and R are a matched
  pair on the same forward pass. RelP's measured advantage is cleaner *early-layer* reads (a.k.a.
  "early-lens" / "relp-lens" — all the same thing).

Every lens uses the **paper-faithful recipe**: `target_layer = n_layers − 2` (penultimate),
`skip_first = 4`, **n = 25** prompts from `NeelNanda/pile-10k`.

## Models

| Directory | Model | Class | `target_layer` | `d_model` | R-lens arm |
|---|---|---|---|---|---|
| `deepseek-v4-flash/` | `deepseek-ai/DeepSeek-V4-Flash` | ~280B FP8/FP4 MoE, mHC residual | 41 | 4096 | **all-c4** (routed+shared experts → MLP, router & mHC detached, shared-expert grad-scale = 4) |
| `qwen3.5-4b/` | `Qwen/Qwen3.5-4B` | 4B dense | 30 | 2560 | full RelP (LN + identity + half) |
| `qwen3.5-9b/` | `Qwen/Qwen3.5-9B` | 9B dense | 30 | 4096 | full RelP |
| `qwen3.5-27b/` | `Qwen/Qwen3.5-27B` | 27B dense | 62 | 5120 | full RelP |
| `qwen3.6-27b/` | `Qwen/Qwen3.6-27B` | 27B dense | 62 | 5120 | full RelP |
| `gemma-3-27b-it/` | `google/gemma-3-27b-it` | 27B dense, `(1+w)` RMSNorm | 60 | 5376 | full RelP |
| `qwen3.6-35b-a3b/` | `Qwen/Qwen3.6-35B-A3B` | 35B MoE (A3B active) | 38 | 2048 | **all-experts + shared-scale c4** (routed_experts, router & shared-gate detached, shared-expert grad-scale = 4) — the highest-performing arm from the MoE sweeps |
| `qwen3.5-122b-a10b/` | `Qwen/Qwen3.5-122B-A10B` | 122B MoE (A10B active) | 46 | 3072 | paper-minimal RelP (LN + identity + half; MoE rules off) |

Each model directory contains:

```
<model>/j-lens/lens.pt     # standard Jacobian lens
<model>/r-lens/lens.pt     # RelP lens (matched pair)
```

### A note on the MoE R-lens arms

For dense models the R-lens is the plain paper RelP (LN + identity + half). For MoE models the
Jacobian's backward graph also has to handle routed/shared experts and the router. Two MoE models
here use their **swept winner** rather than the minimal rules:

- **DeepSeek-V4-Flash → `all-c4`** and **Qwen3.6-35B-A3B → all-experts + shared-scale c4** treat all
  experts as MLPs, freeze/detach the router (and mHC coefficients on DeepSeek), and apply a
  gradient scale of 4 to the always-on shared expert. These were selected by the per-model arm
  sweeps as the best-reading RelP variants.
- **Qwen3.5-122B-A10B** ships the paper-minimal RelP pair (dense rules only; the full-scope
  all-experts arm was never merged for it), so it is directly comparable to its standard J-lens.

The exact rule config for every artifact is embedded in `provenance.config_json` inside each
`lens.pt` (see below).

## Loading a lens

Each `lens.pt` is the official stacked-Jacobian dictionary:

```python
import torch
lens = torch.load("qwen3.6-27b/r-lens/lens.pt", map_location="cpu", weights_only=False)
lens.keys()          # dict_keys(['J', 'n_prompts', 'source_layers', 'd_model', 'provenance'])
lens["provenance"]   # model_id, target_layer, skip_first, n_prompts, dataset_id, config_json, ...
```

`J` is the stacked per-layer Jacobians (`source_layers` rows through the `target_layer` anchor row,
which is exactly `I`). Read a lens the usual way — `softmax(W_U · norm(J_ℓ · h_ℓ))` — or load with
`global_workspace.lens.load_jacobians` / the official `JacobianLens`.

## Template lens (Qwen3.6-27B)

The template lens is a **phrase-level** readout: instead of ranking single-token vocabulary
entries, each row is a template **word or multi-word phrase**, so it can name multi-token concepts
the J-lens cannot ("ice cream", "New Zealand", "what this means"). It is scored by cosine of the
per-layer residual against each template direction. Files live in `qwen3.6-27b/template-lens/`:

| File | Rows | Contents |
|---|---|---|
| `templates.safetensors` | 13,174 | base template lens — common words + curated entities/multi-token concepts |
| `templates+phrases_v3.safetensors` | 13,731 | above **+ the v3 phrase registry** (SAE/seed/gap-mined multi-word phrases) |
| `template_words.txt` | 13,174 | `row_id⇥text` for `templates.safetensors` |
| `template_words+phrases_v3.txt` | 13,731 | `row_id⇥text` for `templates+phrases_v3.safetensors` |

Both stacks are `bfloat16`, shape `[64, n_rows, 5120]` (all 64 layers × rows × `d_model`), with
`word_ids`, `layers`, and a self-describing `TemplateMeta` in the safetensors metadata. The `.txt`
files are the **template lens text**: the ordered row → word/phrase map, so you can read which
concept each row scores without rebuilding the vocabulary. Row order is
`global_workspace.template_lens.vocab.load_words(...)` filtered to the stored `word_ids`.

```python
from safetensors import safe_open
with safe_open("qwen3.6-27b/template-lens/templates+phrases_v3.safetensors", framework="pt") as f:
    meta = f.metadata()          # model_id, n_words, phrase_registry='v3', layers_json, ...
    templates = f.get_tensor("templates")   # [64, 13731, 5120] bf16
    word_ids  = f.get_tensor("word_ids")    # row -> vocab index
```

## Provenance

- J-lens/R-lens pairs are the merged n=25 artifacts from the RelP multi-model matrix
  (`agu18dec/relp-jlens-matrix`, `agu18dec/qwen3.6-27b-relp-jlens`,
  `camilablank/deepseek-elens-jlens`) and the internal `jlens-ablations` build volume
  (a3b winner, 122b). Every pair is recipe-matched (same target/skip/n/corpus).
- Template lenses are built with `global_workspace.template_lens` over Qwen3.6-27B.
- Full per-artifact provenance (git commit, exact rule config, dataset) is embedded in each file.

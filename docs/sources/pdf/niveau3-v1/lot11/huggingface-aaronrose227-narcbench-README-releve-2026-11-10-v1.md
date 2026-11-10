---
license: mit
pretty_name: NARCBench
task_categories:
  - feature-extraction
  - text-classification
language:
  - en
tags:
  - interpretability
  - multi-agent
  - collusion-detection
  - deception
  - activation-probing
size_categories:
  - 10K<n<100K
---

# NARCBench

Activations and scenario data for *Detecting Multi-Agent Collusion Through Multi-Agent Interpretability*. Companion to [github.com/aaronrose227/narcbench](https://github.com/aaronrose227/narcbench).

## Models and layers

| Model | HF ID | Layers |
|-------|-------|--------|
| Qwen3-32B-AWQ | `Qwen/Qwen3-32B-AWQ` | 26–30 |
| Llama-3.1-70B-Instruct-AWQ-INT4 | `meta-llama/Llama-3.1-70B-Instruct-AWQ-INT4` | 32–37 |
| DeepSeek-R1-Distill-Qwen-32B | `deepseek-ai/DeepSeek-R1-Distill-Qwen-32B` | 26–30 |
| GPT-OSS-20B | `openai/gpt-oss-20b` | 10–14 |

## Run counts (collusion + control)

| Model | Core | Transfer | Stego |
|-------|------|----------|-------|
| Qwen3-32B | 31 + 31 | 36 + 36 | 20 + 20 |
| Llama-3.1-70B | 31 + 31 | 36 + 36 | 20 + 20 |
| DeepSeek-R1-32B | 28 + 28 | 36 + 36 | 20 + 20 |
| GPT-OSS-20B | 18 + 18 | 13 + 13 | 20 + 20 |

Every collusion run is paired 1-for-1 with a same-scenario control.

## Layout

```
activations/<model>/<tier>/
  metadata_gen.json    # list of dicts, one per agent-turn
  activations_gen.npz  # keyed `layer_<idx>`, float32, rows align with metadata
scenarios/<model>/<tier>/<run>/
  run_config.json, agent_prompts.json, results.json
```

Scenarios shipped for `qwen3_32b` and `gpt_oss_20b` only — the others reused Qwen3's prompts.

## Schema

`metadata_gen.json` rows have 20 fields, identical across all tiers (`null` where not applicable).

| Field | Type | Notes |
|-------|------|-------|
| `run_id` | str | `<family>__<scenario_id>__<mode>` |
| `mode` | str | `collusion` / `control` |
| `role` | str | `colluder` / `honest` |
| `channel` | str | `public` / `private` / `thinking` |
| `phase`, `round` | str, int | Turn metadata |
| `agent_name`, `n_tokens` | str, int | |
| `seed`, `flagged` | int, bool | Generation metadata |
| `family`, `scenario_id` | str, str | Derived from `run_id` |
| `scenario_domain` | str | Core only |
| `agent_vote`, `target_option`, `target_majority`, `collusion_success`, `fair_option`, `label_variant` | mixed | Core / Transfer ground-truth labels (null in Stego) |
| `bp_corr` | float | Stego only — Big Player's bet/count correlation |

## Usage

```bash
huggingface-cli download aaronrose227/narcbench --repo-type dataset --local-dir data
```

Then with the [github code](https://github.com/aaronrose227/narcbench):

```bash
PYTHONPATH=. python3 probes/reproduce.py --model Qwen/Qwen3-32B-AWQ
```

```python
import numpy as np
npz = np.load("activations/qwen3_32b/core/activations_gen.npz")
npz["layer_28"].shape  # (1054, 5120) — rows align with metadata_gen.json
```

## Citation

```bibtex
@misc{narcbench2026,
  title  = {Detecting Multi-Agent Collusion Through Multi-Agent Interpretability},
  author = {Rose, Aaron and Cullen, Carissa and Abdelnabi, Sahar and Torr, Philip
            and Kaplowitz, Brandon Gary and Schroeder de Witt, Christian},
  year   = {2026},
}
```

## License

MIT

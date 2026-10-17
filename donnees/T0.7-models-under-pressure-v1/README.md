---
language:
- en
license: mit
pretty_name: Models Under Pressure
size_categories:
- 10K<n<100K
task_categories:
- text-classification
tags:
- safety
- ai-safety
- activation-probes
- interpretability
- high-stakes
configs:
- config_name: training
  default: true
  data_files:
  - split: train
    path: "training/train.jsonl"
  - split: test
    path: "training/test.jsonl"
- config_name: anthropic_hh_balanced
  data_files:
  - split: validation
    path: "anthropic_hh_balanced/validation.jsonl"
  - split: test
    path: "anthropic_hh_balanced/test.jsonl"
- config_name: anthropic_hh_raw
  data_files:
  - split: validation
    path: "anthropic_hh_raw/validation.jsonl"
  - split: test
    path: "anthropic_hh_raw/test.jsonl"
- config_name: mt_balanced
  data_files:
  - split: validation
    path: "mt_balanced/validation.jsonl"
  - split: test
    path: "mt_balanced/test.jsonl"
- config_name: mt_raw
  data_files:
  - split: validation
    path: "mt_raw/validation.jsonl"
  - split: test
    path: "mt_raw/test.jsonl"
- config_name: mts_balanced
  data_files:
  - split: validation
    path: "mts_balanced/validation.jsonl"
  - split: test
    path: "mts_balanced/test.jsonl"
- config_name: mts_raw
  data_files:
  - split: validation
    path: "mts_raw/validation.jsonl"
  - split: test
    path: "mts_raw/test.jsonl"
- config_name: toolace_balanced
  data_files:
  - split: validation
    path: "toolace_balanced/validation.jsonl"
  - split: test
    path: "toolace_balanced/test.jsonl"
- config_name: toolace_raw
  data_files:
  - split: validation
    path: "toolace_raw/validation.jsonl"
  - split: test
    path: "toolace_raw/test.jsonl"
- config_name: mental_health_balanced
  data_files:
  - split: test
    path: "mental_health_balanced/test.jsonl"
- config_name: mental_health_raw
  data_files:
  - split: test
    path: "mental_health_raw/test.jsonl"
- config_name: aya_redteaming_balanced
  data_files:
  - split: test
    path: "aya_redteaming_balanced/test.jsonl"
- config_name: aya_redteaming_raw
  data_files:
  - split: test
    path: "aya_redteaming_raw/test.jsonl"
---

# Models Under Pressure

This dataset accompanies the paper [Detecting High-Stakes Interactions with Activation Probes](https://arxiv.org/abs/2506.10805), presented at the ICML 2025 Workshop on Actionable Interpretability, accepted to NeurIPS 2025.

## Overview

Every sample is a user-facing LLM interaction labelled as **high-stakes** or **low-stakes**. The label reflects whether the conversation involves potentially consequential outcomes (medical advice, legal matters, financial decisions, etc.) vs. routine queries.

The dataset contains:
- A **synthetic training set** of 10,000 prompts spanning diverse topics and stakes levels
- **Evaluation sets** derived from six existing datasets, relabelled for stakes

Each sample includes the input text, a binary `labels` field (`"high-stakes"` or `"low-stakes"`), and metadata such as labelling confidence and explanation.

## Dataset Configurations

### Training

| Split | Samples |
|-------|---------|
| train | 8,000 |
| test | 2,000 |

Synthetically generated prompts covering a variety of topics, tones, and prompt styles. Each prompt is paired with a matched high-stakes and low-stakes variant sharing the same topic and context.

### Evaluation Datasets

Each evaluation dataset is available in two variants:
- **balanced**: Subsampled so that high-stakes and low-stakes classes are equally represented
- **raw**: The full labelled dataset without rebalancing

| Dataset | Source | Balanced (dev / test) | Raw (dev / test) |
|---------|--------|-----------------------|-------------------|
| Anthropic HH | [Anthropic HH-RLHF](https://huggingface.co/datasets/Anthropic/hh-rlhf) | 1,028 / 2,984 | 3,174 / 9,198 |
| MT | [MT-Bench](https://huggingface.co/datasets/HuggingFaceH4/mt_bench_prompts) | 278 / 604 | 1,333 / 2,698 |
| MTS | [MT-Bench (single-turn)](https://huggingface.co/datasets/HuggingFaceH4/mt_bench_prompts) | 274 / 86 | 1,105 / 328 |
| ToolACE | [ToolACE](https://huggingface.co/datasets/Team-ACE/ToolACE) | 328 / 734 | 3,000 / 8,300 |
| Mental Health | [Mental Health Conversations](https://huggingface.co/datasets/heliosbrahma/mental_health_chatbot_dataset) | - / 540 | - / 1,000 |
| Aya Redteaming | [Aya Red-teaming](https://huggingface.co/datasets/CohereForAI/aya_redteaming) | - / 1,242 | - / 3,497 |

Mental Health and Aya Redteaming are test-only (no dev split).

## Fields

All samples share these core fields:

| Field | Description |
|-------|-------------|
| `inputs` | The user-facing text (a prompt string or JSON-encoded conversation) |
| `labels` | `"high-stakes"` or `"low-stakes"` |
| `scale_labels` | Numeric stakes rating (1-10) |
| `scale_label_confidence` | Model confidence in the rating (1-10) |
| `scale_label_explanation` | Free-text explanation for the label |
| `ids` | Unique sample identifier |

Training samples additionally include `topic`, `tone`, `language`, `prompt_style`, `length`, `pair_id`, and other generation metadata.

## Usage

```python
from datasets import load_dataset

# Load the training set
train = load_dataset("Arrrlex/models-under-pressure", "training", split="train")

# Load a balanced evaluation set
anthropic_dev = load_dataset("Arrrlex/models-under-pressure", "anthropic_hh_balanced", split="validation")
```

## Citation

If you use this dataset, please cite:

```bibtex
@article{mckenzie2025detecting,
  title={Detecting High-Stakes Interactions with Activation Probes},
  author={McKenzie, Alex and Pawar, Urja and Blandfort, Phil and Bankes, William and Krueger, David and Lubana, Ekdeep Singh and Krasheninnikov, Dmitrii},
  journal={arXiv preprint arXiv:2506.10805},
  year={2025}
}
```

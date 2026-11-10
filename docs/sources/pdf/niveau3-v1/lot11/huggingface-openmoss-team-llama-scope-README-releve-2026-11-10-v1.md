---
license: apache-2.0
language:
- en
base_model:
- meta-llama/Llama-3.1-8B
---

# Llama Scope

[**Technical Report Link**](https://arxiv.org/abs/2410.20526) 

[**Use with OpenMOSS lm_sae Github Repo**](https://github.com/OpenMOSS/Language-Model-SAEs/blob/main/examples/loading_llamascope_saes.ipynb) 

[**Use with SAELens**](https://github.com/jbloomAus/SAELens/blob/v5.4.1/sae_lens/pretrained_saes.yaml#L10986) 

[**Explore in Neuronpedia**](https://www.neuronpedia.org/llama-scope)

Sparse Autoencoders (SAEs) have emerged as a powerful unsupervised method for extracting sparse representations from language models, yet scalable training remains a significant challenge. We introduce a suite of 256 improved TopK SAEs, trained on each layer and sublayer of the Llama-3.1-8B-Base model, with 32K and 128K features.

This is a frontpage of all Llama Scope SAEs. Please see the following link for checkpoints.

## Naming Convention

L[Layer][Position]-[Expansion]x

For instance, an SAE with 8x the hidden size of Llama-3.1-8B, i.e. 32K features, trained on the 15th post-MLP residual stream is called L15R-8x.

## Checkpoints

[**Llama-3.1-8B-LXR-8x**](https://huggingface.co/fnlp/Llama3_1-8B-Base-LXR-8x/tree/main)

[**Llama-3.1-8B-LXA-8x**](https://huggingface.co/fnlp/Llama3_1-8B-Base-LXA-8x/tree/main)

[**Llama-3.1-8B-LXM-8x**](https://huggingface.co/fnlp/Llama3_1-8B-Base-LXM-8x/tree/main)

[**Llama-3.1-8B-LXTC-8x**](https://huggingface.co/fnlp/Llama3_1-8B-Base-LXTC-8x/tree/main)

[**Llama-3.1-8B-LXR-32x**](https://huggingface.co/fnlp/Llama3_1-8B-Base-LXR-32x/tree/main)

[**Llama-3.1-8B-LXA-32x**](https://huggingface.co/fnlp/Llama3_1-8B-Base-LXA-32x/tree/main) (Not recommended, we along with many other mech interp researchers find that LXA SAEs, whether trained on z or attn_out, turn out to have a lot of inactive features. This is observed both in GPT2-Small (both discovered by @Johnny Lin from neuronpedia.org and us) and Llama 3.1 8B. This is much like 'there are not too many features in attention output so we do not expect to see feature splitting here.'. But we are not certain why this is the case.)

[**Llama-3.1-8B-LXM-32x**](https://huggingface.co/fnlp/Llama3_1-8B-Base-LXM-32x/tree/main)

[**Llama-3.1-8B-LXTC-32x**](https://huggingface.co/fnlp/Llama3_1-8B-Base-LXTC-32x/tree/main)

## Llama Scope SAE Overview

<center>

|                       | **Llama Scope**               | **Scaling Monosemanticity**    | **GPT-4 SAE**                    | **Gemma Scope**                   |
|-----------------------|:-----------------------------:|:------------------------------:|:--------------------------------:|:---------------------------------:|
| **Models**            | Llama-3.1 8B (Open Source)    | Claude-3.0 Sonnet (Proprietary) | GPT-4 (Proprietary)              | Gemma-2 2B & 9B (Open Source)     |
| **SAE Training Data** | SlimPajama                    | Proprietary                     | Proprietary                      | Proprietary, Sampled from Mesnard et al. (2024) |
| **SAE Position (Layer)** | Every Layer              | The Middle Layer                | 5/6 Late Layer     | Every Layer                       |
| **SAE Position (Site)**  | R, A, M, TC              | R                               | R                                | R, A, M, TC                       |
| **SAE Width (# Features)** | 32K, 128K              | 1M, 4M, 34M                     | 128K, 1M, 16M                    | 16K, 64K, 128K, 256K - 1M (Partial) |
| **SAE Width (Expansion Factor)** | 8x, 32x       | Proprietary                     | Proprietary                      | 4.6x, 7.1x, 28.5x, 36.6x         |
| **Activation Function** | TopK-ReLU                 | ReLU                            | TopK-ReLU                        | JumpReLU                          |

</center>


## Citation

Please cite as:

```
@article{he2024llamascope,
  title={Llama Scope: Extracting Millions of Features from Llama-3.1-8B with Sparse Autoencoders},
  author={He, Zhengfu and Shu, Wentao and Ge, Xuyang and Chen, Lingjie and Wang, Junxuan and Zhou, Yunhua and Liu, Frances and Guo, Qipeng and Huang, Xuanjing and Wu, Zuxuan and others},
  journal={arXiv preprint arXiv:2410.20526},
  year={2024}
}
```

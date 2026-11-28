---
license: cc-by-nc-4.0
datasets:
- togethercomputer/RedPajama-Data-V2
base_model:
- meta-llama/Llama-3.1-8B-Instruct
---

# TopK Transcoder Based on Llama 3.1 8B Instruct

This repository provides the TopK transcoder checkpoints used in the paper [**“Verifying Chain-of-Thought Reasoning via Its Computational Graph”**](https://arxiv.org/abs/2510.09312).  
The model is based on **Llama 3.1 8B Instruct** and trained with the TopK transcoder method described in the paper.

## Installation

To run the model, you need the Circuit Tracer library.  
It can be installed from the project page:

https://github.com/zsquaredz/circuit-tracer

Note that this is a fork of the original library as they don't yet support TopK transcoder. 

After installing the library, you can load and run the transcoder as shown below.

## Minimal Usage Example

```python
from circuit_tracer import ReplacementModel
import torch

# Load transcoders into a ReplacementModel
model = ReplacementModel.from_pretrained("meta-llama/Llama-3.1-8B-Instruct", "facebook/crv-8b-instruct-transcoders", dtype=torch.bfloat16)
```
Once you have loaded the model, you can perform attribution or intervention as shown in [this demo](https://github.com/safety-research/circuit-tracer/blob/main/demos/llama_demo.ipynb).

## Citation

If you use this model, please cite our paper:

```bibtex
@article{zhao2025verifying,
      title={Verifying Chain-of-Thought Reasoning via Its Computational Graph},
      author={Zheng Zhao and Yeskendir Koishekenov and Xianjun Yang and Naila Murray and Nicola Cancedda},
      year={2025},
      eprint={2510.09312},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2510.09312},
}
```
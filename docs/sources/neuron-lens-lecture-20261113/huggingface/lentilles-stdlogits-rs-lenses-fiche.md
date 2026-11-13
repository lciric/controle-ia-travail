---
license: cc-by-4.0
base_model:
- Qwen/Qwen3-8B
- google/gemma-4-12B
tags:
- interpretability
- jacobian-lens
- logit-lens
- relp
- r-lens
- s-lens
---

# R-lens and S-lens for Qwen3-8B and Gemma 4 12B

Linear lenses that turn a vector inside a model into a ranking over tokens, for
[`Qwen/Qwen3-8B`](https://huggingface.co/Qwen/Qwen3-8B) and
[`google/gemma-4-12B`](https://huggingface.co/google/gemma-4-12B), fitted with one estimator on the
same 1,000 web documents:

- the **R-lens** reads what a residual-stream vector at layer `L` makes the model say, after the later
  layers have acted on it (read with the unembedding `W_U`);
- the **S-lens** reads which inputs put a vector at layer `L` (read with the embeddings `W_E`).

Gemma 4 takes images and sound through linear embedders, so its lenses are also fitted on images and on
sounds, where the S-lens reads back to pixels or audio samples. Every MLP neuron and attention head of
both models read through these lenses is the dataset
[`stdlogits/neuron-lens`](https://huggingface.co/datasets/stdlogits/neuron-lens). Code, methods and findings (cited here as
§N) are on [GitHub](https://github.com/stdlogits/neuron-lens).

![The logit lens, the J-lens and R-lens, and the K-lens and S-lens](figures/02_lenses.png)

## Files

| file | lens | maps |
|---|---|---|
| `qwen3-8b/r-lens/lens.pt` | R, `J[L]` | layer `L`'s output → the last layer's output, `[4096, 4096]`, `J[35]` the identity |
| `qwen3-8b/r-lens/mid.pt` | R, `J[L]` | layer `L`'s MLP input → the last layer's output |
| `qwen3-8b/s-lens/mid.pt` | S, `K[L]` | token embeddings → layer `L`'s MLP input |
| `qwen3-8b/s-lens/out.pt` | S, `K[L]` | token embeddings → layer `L`'s output |
| `gemma-4-12b/r-lens/lens.pt` | R, `J[L]` | layer `L`'s output → the last layer's output, `[3840, 3840]`, `J[47]` the identity |
| `gemma-4-12b/r-lens/mid.pt` | R, `J[L]` | layer `L`'s MLP input → the last layer's output |
| `gemma-4-12b/s-lens/mid.pt` | S, `K[L]` | token embeddings → layer `L`'s MLP input |
| `gemma-4-12b/s-lens/out.pt` | S, `K[L]` | token embeddings → layer `L`'s output |
| `gemma-4-12b/image/r-lens/`, `gemma-4-12b/image/s-lens/` | the same, fitted on COCO 2014 validation images | read and seeded at the images' 64 slots; `K[L]` is `[3840, 2048]` with `basis` |
| `gemma-4-12b/audio/r-lens/`, `gemma-4-12b/audio/s-lens/` | the same, fitted on ESC-50 clips | read and seeded at the sounds' 64 slots; `K[L]` is `[3840, 640]` with `basis` |

Each file is a dict of fp32 matrices by layer: `[4096, 4096]` for Qwen3-8B's 36 layers (2.4 GB a file),
`[3840, 3840]` for Gemma 4's 48. The "MLP input" is the residual after the layer's attention, where the
MLP reads. `lens.pt` follows [`camilablank/workspace-lenses`](https://huggingface.co/camilablank/workspace-lenses)'
layout (`J`, `n_prompts`, `source_layers`, `d_model`, and in Qwen3-8B's files `provenance`); the S-lens
files hold `K` and `layers` in its place. `provenance` records the corpus, the rules and the split-half
difference by layer. Gemma's image and audio S-lenses are seeded in the subspace the embedder reaches,
so they hold `basis` (`[k, 3840]`, orthonormal rows) beside `K`: `K_full[L] = K[L] @ basis`.

**Which file reads what** (the lens rule): `out` reads MLP outputs and attention inputs, `mid` reads MLP
inputs and attention outputs.

| to read | at | R-lens | S-lens |
|---|---|---|---|
| an MLP neuron's write | layer `L`'s output | `r-lens/lens.pt` | `s-lens/out.pt` |
| an MLP neuron's read direction (gate and up rows) | layer `L`'s MLP input | `r-lens/mid.pt` | `s-lens/mid.pt` |
| what an attention head reads: keys and values | layer `L − 1`'s output | | `s-lens/out.pt` |
| what an attention head reads: a late query (what the position is about to say) | layer `L − 1`'s output | `r-lens/lens.pt` | |
| what an attention head writes | layer `L`'s MLP input | `r-lens/mid.pt` | `s-lens/mid.pt` |

## Definition

Both average a Jacobian of the residual stream over the corpus, summed over positions as in the
[J-lens](https://transformer-circuits.pub/2026/workspace/), but under
[RelP](https://arxiv.org/abs/2508.21258)'s propagation rules instead of the true gradient:

```
J_L = mean_t Σ_{t' ≥ t} ∂h_final(t') / ∂h_L(t)     R-lens, reverse mode
K_L = mean_t Σ_{s ≤ t}  ∂h_L(t) / ∂e(s)            S-lens, forward mode
```

- **R-lens read** of a vector `h` at layer `L`: `softmax(W_U · norm(J_L h))`, with `norm` the final
  RMSNorm and its weight (for Gemma 4, the logits then pass its softcap, `30 · tanh(x / 30)`). This is
  the [R-lens](https://www.lesswrong.com/posts/nv8oedrnLXKRzNEL9/r-lens-making-j-lens-more-faithful-on-early-layers),
  with the last layer's output as its target.
- **S-lens read** of a direction `c` at layer `L`: token `v` scores `c · K_L (W_E[v] − mean(W_E))` (for
  Gemma 4, `W_E` times √3840, as embeddings enter its residual). Taking the Jacobian back to the input
  embeddings is Theia Vogel's K-lens ([@voooooogel](https://x.com/voooooogel/status/2084858861551526002),
  unpublished); the S-lens is it under RelP's rules. For images and sound, `c · K_L` is a covector on
  the embedder's output, which the embedder maps back to pixels (48 × 48 × 3 per patch) or samples (640
  per 40 ms frame).
- **Layer-contrastive reads** z-score each token's score across many vectors of one layer (all its
  neurons, say), which removes the hub tokens that top most raw reads.
- **The rules:** decoder-layer RMSNorms hold their `rsqrt` constant; the MLP's activation `act(g)` is
  linearized as `(act(g)/g)·dg` (SiLU for Qwen3, GELU-tanh for Gemma 4); and `act(g)·up` passes half of
  each factor's change (β = 0.5). Attention, the q/k (and Gemma's v) norms and RoPE keep
  their true derivative. Under the rules each layer is a fixed linear map per document, and the
  R-lens's backward map is exactly the transpose of the S-lens's forward one.

## Fitting

- **Text:** for both models, the first 1,000 rows of
  [`HuggingFaceFW/dclm_100BT-shuffled`](https://huggingface.co/datasets/HuggingFaceFW/dclm_100BT-shuffled) (revision `2fa015e4044ec442a0734e89658cdcc538d10dd4`), the
  first 128 tokens of each (row-set SHA-256 `ca09a4d8081c7a07`… for Qwen3).
- **Gemma 4's images:** COCO 2014 validation images (the first 1,000 for the S-lens,
  512 for the R-lens), 384 × 384, 64 slots of 48 × 48 patches, in a short text prompt.
  **Sounds:** ESC-50 clips, the middle 2.56 s at 16 kHz, 64 slots of 40 ms (1,615 clips
  for the S-lens, 512 for the R-lens; clips with a digitally silent frame are skipped).
- Seeds at every position from 16 to `T − 2` (for media, at the slots): the attention-sink
  positions and the last are left out. Documents weigh equally.
- bf16 on one H100 with fp32 sums, about 11 s (Qwen3-8B) and 16 s (Gemma 4) per text document per
  lens, by hand-written layer maps tested against autograd Jacobians under the same rules.

## Reliability

The documents alternate between two halves. `‖mean_even − mean_odd‖ / ‖mean‖` by layer:

- Qwen3-8B: R-lens 0.00-0.06 (from each layer's output), 0.00-0.06 (from each MLP input); S-lens 0.00-0.05 (to each MLP input), 0.01-0.05 (to each output).
- Gemma 4 12B: R-lens 0.01-0.12, S-lens 0.01-0.07, by layer over both targets.

![Split-half difference by layer](figures/04_lens_reliability.png)

This is stability within the corpus, not independence from it. An R-lens for Qwen3-8B fitted on 500
chat conversations shares the top token of a neuron's write read with this one for only 31-51% of
neurons at L2-L16, but reads the same concepts and predicts steering within 0.04 of it at every layer
(§1).

![A chat-fitted lens against the halves of this one](figures/05_chat_lens.png)

## Which lens to use where

Measured on the models' neurons and heads (§3, §6, §11, §13, §14):

- **The R-lens predicts what steering a neuron does.** Correlated with the measured change in
  log-probabilities when a neuron's write is added at about its typical activation, the R-lens read of
  the write reaches, for Qwen3-8B, a median r of 0.45-0.50 at L4-L8 and 0.9 or more from L22 (another
  neuron's read: ±0.04), ahead of Neuronpedia's J-lens by 0.03-0.13 from L4 to L23. Before about L21 it
  reads a neuron's average push, which is what steering shows, not what one firing does in context (§4).

![Lens reads against steering](figures/07_steering.png)

- For Gemma 4 12B, from L11: 0.53 at L12-L23, 0.82 at L24-L35 and 0.97 at L36-L47, ahead of the logit
  lens. Before L11, natural-size pushes are too small for either lens to predict (§13).

![Gemma 4: lens reads against steering](figures/19_gemma_steering.png)

- **The S-lens reads early layers' input side.** Through L8 of Qwen3-8B (L13 of Gemma 4) it names the
  tokens that make a neuron fire (Qwen3-8B, L0: the firing token is in its top 10 for 38% of top
  firings; another neuron's read: under 0.1%), and what early neurons write back. Past them its raw reads are
  swamped by hub tokens; z-scored across the layer they name concepts.
- **From L9 of Qwen3-8B, read input directions with `r-lens/mid.pt`.** It names the exact tokens that
  drive a neuron more often than the S-lens (5-8% of its top 10 at L9-L12 and L22-L30). L13-L20 is hard
  for every weight-only input read.

![Which reads name the exact drivers](figures/11_drivers.png)

- **Attention heads:** read a head's keys and values with the S-lens (at real firings it beats the R-lens input
  in every band, for both circuits, with one exception: copying at L28-L35 read with an S-lens output),
  and its output with the S-lens through L8 and the R-lens from L9. Late, a head's query reads what its
  position is about to say: with `r-lens/lens.pt` at `L − 1` as the query against S-lens keys, QK's diagonal
  finds the heads that look up earlier copies of the coming token, copy suppressors among them (§11).

![Which lens on each side of a head](figures/16_head_lens_sides.png)

- **Images and sound** (Gemma 4): a neuron's read direction through the image S-lens is what the
  direction looks like in pixels, a projection: on held-out images it moves the neuron's read
  projection most through L23, but raises its activation only at L0-L5. The audio S-lens read is at
  chance. Optimised from the read by gradient ascent through the model, a patch or a frame raises its
  neuron through L23 (§14).

![What the image and sound reads are good for](figures/21_media_reads.png)

## Loading

```python
import torch
from huggingface_hub import hf_hub_download

r = torch.load(hf_hub_download("stdlogits/rs-lenses", "qwen3-8b/r-lens/lens.pt"), weights_only=True)
J = r["J"][20]           # [4096, 4096]: layer 20's output -> the final residual
s = torch.load(hf_hub_download("stdlogits/rs-lenses", "qwen3-8b/s-lens/mid.pt"), weights_only=True)
K = s["K"][20]           # token embeddings -> layer 20's MLP input
img = torch.load(hf_hub_download("stdlogits/rs-lenses", "gemma-4-12b/image/s-lens/mid.pt"), weights_only=True)
K_img = img["K"][8] @ img["basis"]   # [3840, 3840]: image embeddings -> Gemma 4's layer 8 MLP input
```

With [Drowse](https://github.com/stdlogits/drowse) (6.0 or later), the text lenses are lens sources:
`drowse lens fetch Qwen/Qwen3-8B rs-r` (the R-lens, both files) and `rs-s` (the S-lens).

## Notes

- A read describes a direction, not an effect. The R-lens read is scale-free (the final RMSNorm);
  S-lens scores scale with the direction, so normalize it first.
- Positions before 16 are never seeded, so reads of the first positions, where the attention
  sink forms, extrapolate.
- Undertrained tokens can dominate early reads. The catalog leaves out tokens seen fewer than 5 times
  in its corpora, and byte-fallback pieces.
- A media read is one slot pattern summed over the 64 slots, not a map of where in an image it sits.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The lenses are derived from
[`Qwen/Qwen3-8B`](https://huggingface.co/Qwen/Qwen3-8B) and
[`google/gemma-4-12B`](https://huggingface.co/google/gemma-4-12B) (both Apache 2.0) and fitted on
[`HuggingFaceFW/dclm_100BT-shuffled`](https://huggingface.co/datasets/HuggingFaceFW/dclm_100BT-shuffled) (CC BY 4.0), and Gemma 4's media
lenses on [COCO 2014](https://cocodataset.org) images (CC BY 4.0, Flickr terms for the images) and
[ESC-50](https://github.com/karolpiczak/ESC-50) (CC BY-NC 3.0). By [@_a9lim](https://x.com/_a9lim) and
[@treetowntree](https://x.com/treetowntree) with Claude (Anthropic), 2026-11-11.

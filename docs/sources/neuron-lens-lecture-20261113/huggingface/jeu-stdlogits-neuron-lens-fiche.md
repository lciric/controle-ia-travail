---
license: cc-by-4.0
pretty_name: neuron-lens
tags:
- interpretability
- neurons
- attention-heads
- r-lens
- s-lens
- multimodal
configs:
- config_name: qwen3-8b-neurons-acts
  data_files: "qwen3-8b/neurons/acts/*.parquet"
  default: true
- config_name: qwen3-8b-neurons-drivers
  data_files: "qwen3-8b/neurons/drivers/*.parquet"
- config_name: qwen3-8b-neurons-reads
  data_files: "qwen3-8b/neurons/reads/*.parquet"
- config_name: qwen3-8b-neurons-labels
  data_files: "qwen3-8b/neurons/labels/*.parquet"
- config_name: qwen3-8b-neurons-edges
  data_files: "qwen3-8b/neurons/edges/*.parquet"
- config_name: qwen3-8b-neurons-firings
  data_files: "qwen3-8b/neurons/firings/*.parquet"
- config_name: qwen3-8b-neurons-sources
  data_files: "qwen3-8b/neurons/sources/*.parquet"
- config_name: qwen3-8b-heads-acts
  data_files: "qwen3-8b/heads/acts.parquet"
- config_name: qwen3-8b-heads-drivers
  data_files: "qwen3-8b/heads/drivers.parquet"
- config_name: qwen3-8b-heads-reads
  data_files: "qwen3-8b/heads/reads.parquet"
- config_name: qwen3-8b-heads-labels
  data_files: "qwen3-8b/heads/labels.parquet"
- config_name: qwen3-8b-heads-sources
  data_files: "qwen3-8b/heads/sources.parquet"
- config_name: gemma-4-12b-neurons-acts
  data_files: "gemma-4-12b/neurons/acts/*.parquet"
- config_name: gemma-4-12b-neurons-drivers
  data_files: "gemma-4-12b/neurons/drivers/*.parquet"
- config_name: gemma-4-12b-neurons-reads
  data_files: "gemma-4-12b/neurons/reads/*.parquet"
- config_name: gemma-4-12b-neurons-labels
  data_files: "gemma-4-12b/neurons/labels/*.parquet"
- config_name: gemma-4-12b-neurons-edges
  data_files: "gemma-4-12b/neurons/edges/*.parquet"
- config_name: gemma-4-12b-neurons-firings
  data_files: "gemma-4-12b/neurons/firings/*.parquet"
- config_name: gemma-4-12b-neurons-sources
  data_files: "gemma-4-12b/neurons/sources/*.parquet"
- config_name: gemma-4-12b-neurons-image
  data_files: "gemma-4-12b/neurons/image/*.parquet"
- config_name: gemma-4-12b-neurons-audio
  data_files: "gemma-4-12b/neurons/audio/*.parquet"
- config_name: gemma-4-12b-neurons-image-optimised
  data_files: "gemma-4-12b/neurons/image_optimised.parquet"
- config_name: gemma-4-12b-neurons-audio-optimised
  data_files: "gemma-4-12b/neurons/audio_optimised.parquet"
- config_name: gemma-4-12b-heads-acts
  data_files: "gemma-4-12b/heads/acts.parquet"
- config_name: gemma-4-12b-heads-drivers
  data_files: "gemma-4-12b/heads/drivers.parquet"
- config_name: gemma-4-12b-heads-reads
  data_files: "gemma-4-12b/heads/reads.parquet"
- config_name: gemma-4-12b-heads-labels
  data_files: "gemma-4-12b/heads/labels.parquet"
- config_name: gemma-4-12b-heads-sources
  data_files: "gemma-4-12b/heads/sources.parquet"
- config_name: gemma-4-12b-heads-image
  data_files: "gemma-4-12b/heads/image.parquet"
- config_name: gemma-4-12b-heads-audio
  data_files: "gemma-4-12b/heads/audio.parquet"
---

# neuron-lens: every neuron and attention head of Qwen3-8B and Gemma 4 12B

A catalog of two models' MLP neurons (two poles each) and attention heads:
[`Qwen/Qwen3-8B`](https://huggingface.co/Qwen/Qwen3-8B) (36 × 12,288 neurons,
36 × 32 heads) and [`google/gemma-4-12B`](https://huggingface.co/google/gemma-4-12B)
(48 × 15,360 neurons, 48 × 16 heads). Each unit is read from three
sides:

- **from the weights alone,** through two lenses: what a unit writes and what it reads; for a head, what
  it copies and what it attends to, token by token;
- **from its activations** over about 15.4M positions of web, Chinese, Python and chat text;
- **from the tokens that drive it** when swept through real contexts.

Gemma 4 takes images and sound too, so each of its neurons is also read through lenses fitted on images
and sounds, and against 49,694 labelled images and 49,703
labelled sounds.

![What neurons and heads do](figures/01_anatomy.png)

Neurons and heads get the same tables, one row per pole or per head:

| table | neurons | heads |
|---|---|---|
| `reads` | lens reads of the write and the read direction | lens reads of the OV and QK circuits, per token |
| `acts` | activation statistics and top firings | output-norm statistics, top firings, attention patterns |
| `drivers` | the tokens that drive each pole hardest | the tokens that drive each head, as query and as key |
| `labels` | Claude Haiku's labels: where it fires, what it writes | where it fires, what it attends to, what it writes |
| `firings` | what the residual holds, what the MLP layer writes and what the model predicts at the pole's top firings | |
| `edges` | the earlier poles whose writes push it most, and the later poles it pushes most | |
| `sources` | what drives the pole when it fires, and the poles that fire with it | |
| `image`, `audio` (Gemma 4) | the patch or sound it reads, its write in media contexts, the images or sounds that drive it, and whether its media label is its text concept too | how each head attends in those contexts, and which carry what an image or sound shows |

| config | rows | what |
|---|---|---|
| `qwen3-8b-neurons-acts` | 884,736 | every pole's activation statistics and top firings |
| `qwen3-8b-neurons-drivers` | 884,736 | every pole's 64 token drivers in real contexts |
| `qwen3-8b-neurons-reads` | 884,736 | every pole's weight-only reads through both lenses |
| `qwen3-8b-neurons-labels` | 884,736 | every pole's labels, by Claude Haiku 5.5 |
| `qwen3-8b-neurons-edges` | 884,736 | every pole's strongest direct weight edges from earlier poles and to later ones |
| `qwen3-8b-neurons-firings` | 884,736 | what the residual holds, what the MLP layer writes and what the model predicts at every pole's top firings |
| `qwen3-8b-neurons-sources` | 860,160 | what drives every pole when it fires, and the poles that fire with it |
| `qwen3-8b-heads-acts` | 1,152 | every head's output statistics, top firings and attention patterns |
| `qwen3-8b-heads-drivers` | 1,152 | every head's 64 token drivers, as query and as key |
| `qwen3-8b-heads-reads` | 1,152 | every head's OV and QK circuits read per token |
| `qwen3-8b-heads-labels` | 1,152 | every head's labels, by Claude Haiku 5.5 |
| `qwen3-8b-heads-sources` | 1,152 | what drives every head when it fires, through its value, query and key, and the poles that fire with it |
| `gemma-4-12b-neurons-acts` | 1,474,560 | every pole's activation statistics and top firings |
| `gemma-4-12b-neurons-drivers` | 1,474,560 | every pole's 64 token drivers in real contexts |
| `gemma-4-12b-neurons-reads` | 1,474,560 | every pole's weight-only reads through both lenses |
| `gemma-4-12b-neurons-labels` | 1,474,560 | every pole's labels, by Claude Haiku 5.5 |
| `gemma-4-12b-neurons-edges` | 1,474,560 | every pole's strongest direct weight edges from earlier poles and to later ones |
| `gemma-4-12b-neurons-firings` | 1,474,560 | what the residual holds, what the MLP layer writes and what the model predicts at every pole's top firings |
| `gemma-4-12b-neurons-sources` | 1,443,840 | what drives every pole when it fires, and the poles that fire with it |
| `gemma-4-12b-neurons-image` | 1,474,560 | every pole's image read and write, the images that drive it, and its cross-modal ranks |
| `gemma-4-12b-neurons-audio` | 1,474,560 | every pole's audio read and write, the sounds that drive it, and its cross-modal ranks |
| `gemma-4-12b-neurons-image-optimised` | 1,728 | the patch that most raises each of the best-labelled poles |
| `gemma-4-12b-neurons-audio-optimised` | 1,728 | the 40 ms of sound that most raises each of the best-labelled poles |
| `gemma-4-12b-heads-acts` | 768 | every head's output statistics, top firings and attention patterns |
| `gemma-4-12b-heads-drivers` | 768 | every head's 64 token drivers, as query and as key |
| `gemma-4-12b-heads-reads` | 768 | every head's OV and QK circuits read per token |
| `gemma-4-12b-heads-labels` | 768 | every head's labels, by Claude Haiku 5.5 |
| `gemma-4-12b-heads-sources` | 768 | what drives every head when it fires, through its value, query and key, and the poles that fire with it |
| `gemma-4-12b-heads-image` | 768 | every head in image contexts |
| `gemma-4-12b-heads-audio` | 768 | every head in audio contexts |

The lenses are [`stdlogits/rs-lenses`](https://huggingface.co/stdlogits/rs-lenses) at revision `ee42b62072`. Code, methods and
findings (cited here as §N) are on [GitHub](https://github.com/stdlogits/neuron-lens).

## The lenses

- The **R-lens** reads what a vector makes the model say: `softmax(W_U · norm(J_L x))`, with `J_L` the
  averaged Jacobian from layer `L` to the last layer (for Gemma 4, after its final softcap,
  `30 · tanh(x / 30)`).
- The **S-lens** reads which input tokens put a vector there: token `v` scores
  `c · K_L (W_E[v] − mean(W_E))`, with `K_L` the averaged Jacobian from the embeddings to layer `L`.

Each is fitted at two points of every layer: `out`, the layer's output, and `mid`, its MLP input (after
attention). `out` reads MLP outputs and attention inputs; `mid` reads MLP inputs and attention outputs.
Gemma 4's image and audio lenses are fitted the same way on images and sounds.

| what | where it is | R-lens read | S-lens read | Gemma 4: image and audio lenses |
|---|---|---|---|---|
| a neuron's write | layer `L`'s output | `write_R` | `write_S` | `image.write_R`, `audio.write_R` |
| a neuron's read direction `â ± b̂` | layer `L`'s MLP input | `read_R` | `read_S` | `image.read_png`, `audio.read_wave` |
| what a head reads | layer `L − 1`'s output | a late query (`qk_self_R`) | the token's footprint (keys and values of `ov_*`, `qk_*`) | |
| what a head writes | layer `L`'s MLP input | `ov_R` | `ov_S` | |

## Which read to use where

No read works at every depth (§7, §11). For Qwen3-8B (these bands are priors; weigh a unit's sides by its reads,
contexts and drivers together):

| layers | what drives a neuron | what a neuron writes | what a head writes |
|---|---|---|---|
| L0-L7 | `read_S` (literal tokens, raw at L0-L4) | `write_S` (early neurons write back what they detect); `write_R` from about L4 | `ov_S` |
| L8 | both | both | `ov_S`, `ov_R` |
| L9-L12, L21-L35 | `read_R`, with `read_S_z` as a concept-level view | `write_R` | `ov_R` |
| L13-L20 | `read_R`, `read_S_z`, with `drivers` and `acts` beside them | `write_R`, for steering | `ov_R` (weak) |

Where a head looks: `qk_S` at every depth (weak at L13-L20); of its diagonal, `qk_self_S` through L20 (duplicate-token
heads) and `qk_self_R` late (L28-L35; mixed at L21-L27), the heads that look up what is about to be said (§11).

![Which reads work at which depth](figures/03_depth_map.png)

Gemma 4's map has the same shape at its own depths: `read_S` through L13 (falling to under 1% at L9 and rising again at L10-L13),
`write_R` from about L33 (for steering from L11), and `qk_self_R` from L24, more weakly than Qwen3-8B's (§13).

![Both models by relative depth](figures/18_two_models.png)

The bands come from how often each read names what can be counted around a pole (`checks/reads_at_firings.py`, §7): the
read direction's S-lens read the peak tokens of its top firings (`read_S`), its R-lens read the exact drivers (`read_R`),
the write's R-lens read the tokens after the firings (`write_R`), its S-lens read the peak tokens (`write_S`); each scored
against another pole of the layer on the same tokens, and passing at a 5% false discovery rate. A firing is one context
summarized by a token, so these are population results about the reads, and the catalog keeps no per-pole test: a read
that misses so narrow a target isn't wrong. Share of each band's poles (token mode: a third of the top firings on one
token), Qwen3-8B:

| band | `read_R` | `read_S` | `write_R` | `write_S` | token mode | near-silent |
|---|---|---|---|---|---|---|
| L0-8 | 6% | 30% | 0% | 12% | 26% | 19% |
| L9-12 | 22% | 2% | 1% | 1% | 11% | 0% |
| L13-20 | 15% | 1% | 0% | 0% | 8% | 0% |
| L21-27 | 34% | 5% | 10% | 2% | 20% | 0% |
| L28-35 | 30% | 1% | 27% | 0% | 16% | 0% |
| all | 21% | 9% | 8% | 4% | 17% | 5% |

Gemma 4 12B:

| band | `read_R` | `read_S` | `write_R` | `write_S` | token mode | near-silent |
|---|---|---|---|---|---|---|
| L0-11 | 0% | 40% | 0% | 1% | 57% | 0% |
| L12-23 | 1% | 6% | 0% | 4% | 26% | 0% |
| L24-35 | 4% | 4% | 7% | 0% | 18% | 0% |
| L36-47 | 1% | 3% | 19% | 0% | 15% | 0% |
| all | 2% | 13% | 7% | 1% | 29% | 0% |

![Gemma 4: what each read names](figures/20_gemma_census.png)

## Conventions

- **Keys.** Neuron tables: `layer`, `neuron` (coordinate `n` of `down_proj`'s input, 0-indexed), `pole`
  (+1 or −1). Both models' gated activations take both signs, so each neuron has two poles with separate
  meanings, 24,576 (Qwen3-8B) or 30,720 (Gemma 4) rows a layer, the + poles
  first. Head tables: `layer`, `head` (query head) and `kv_head` (the key-value head it reads). `L8 n344 +`
  is `layer` 8, `neuron` 344, `pole` 1; `L20h17` is `layer` 20, `head` 17.
- **Token lists.** `<read>_ids` are 64 token ids of the model's tokenizer, `<read>_val` their scores,
  `<read>_str` the top 8 decoded and joined by ` | ` (newlines as `⏎`). Signal holds to rank 64 (§7).
- **Kept tokens.** Reads cover the tokens seen 5 or more times in the activation corpora, without
  byte-fallback pieces (`token_counts.pt`): 103,830 for Qwen3-8B, 123,774 for Gemma 4.
  Undertrained tokens otherwise dominate early reads.
- **`_z`** reads are layer-contrastive: each token's score z-scored across the layer's poles or heads,
  which removes the hub tokens that top most raw reads. **`_neg`**: a head read's bottom.
- **Firings.** A unit's firing in a document is its strongest position there; its top firings are the
  64 documents where that is largest. `contexts` show the first 5, the firing token in `⟦ ⟧` and, for
  heads, the token it attends to most (past position 0) in `⟪ ⟫`.
- **Scale.** A lens read describes a direction, not an effect size; `act_top × w_norm` is a pole's
  typical write within this corpus. A write read is the pole's average push, which steering shows;
  before about L21 of Qwen3-8B, what one firing does depends on its context (§4).
- **Gemma 4.** A neuron's write is what reaches the residual, `s · γ_post ⊙ W_down[:, n]` (its MLP output
  passes a post-feedforward RMSNorm, whose scale the lenses hold constant, and the layer's output is
  scaled by `layer_scalar` `s`); `w_norm` is its norm. The read direction is the gate and up rows times
  the pre-feedforward norm's weight. Sliding-window layers have 8 key-value heads of size 256; every sixth
  layer is global, with one of size 512 whose keys are also its values. A head's write is `W_O` times the
  post-attention norm's weight. Every document starts with `<bos>`, the attention sink, so activation
  statistics start at the first real token and `first_*` is at position 1. The base model has no chat
  template: its chat slice is plain `User:` / `Assistant:` turns.

## Neurons

### `<model>-neurons-reads`: weight-only reads

| columns | read | of |
|---|---|---|
| `write_R`, `write_R_z` | the R-lens, `softmax(W_U · norm(J^out_L w))`; `_val` are probabilities (the logit lens at the last layer) | the write `w` (Qwen3-8B: `±W_down[:, n]`) |
| `write_S`, `write_S_z` | the S-lens to the layer's output: tokens whose footprint the write imitates | the write |
| `write_orth_R`, `write_orth_S`, each with `_z` | the same two lenses | the write with its components along the gate and up rows removed: what it adds beyond anything it reads (§18; the idea is [Matthew Khoriaty](https://www.lesswrong.com/users/matthew-khoriaty)'s) |
| `read_R`, `read_R_z` | the R-lens from the MLP input: what the residual says when it drives the pole | the read direction `â ± b̂` |
| `read_S`, `read_S_z` | the S-lens to the MLP input: input tokens that drive the pole | the read direction |

`â` and `b̂` are the neuron's gate and up rows times the MLP input norm's weight, normalized: `â ± b̂`
is a heuristic direction for each pole; a pole whose top firings ride SiLU's negative lobe (`acts`' `neg_lobe`
past a half; §17) reads the up row alone, `∓b̂`, because SiLU is nearly flat there. Also per row: `w_norm`, `cos_gate_up`, `cos_write_gate`, `cos_write_up` (the
cosine of the pole's write with the gate and up rows, each on the side its firings sit, positive where it writes toward
them; §18), `null_share` (the share of the
write in the bottom 1% of singular directions of `W_U diag(γ)`, where entropy neurons write; Stolfo et
al. 2024) and `vocab_skew`, `vocab_kurt` of `W_U · norm(w)` (Gurnee et al. 2024's prediction and
suppression neurons).

![Read signal by rank](figures/13_rank_depth.png)

### `<model>-neurons-acts`: activation statistics

Over every document of four slices, up to 256 tokens each, in bf16: DCLM held out from the lens
corpus, FineWeb-2 Chinese, codeparrot Python, and UltraChat dialogues (63,990 documents and
15,367,795 positions for Qwen3-8B, 63,992 and 15,409,492 for Gemma 4; `docs.parquet`).

- `act_top`: the median of the 24 top firings, the pole's typical high activation; `act_max`.
- `rate`: the share of positions past `act_top / 4`, from exact counts on a quarter-octave grid (linear
  between its points); `rate_<slice>` per slice; `pos_share`: where the pole's sign holds; `q50`-`q999`:
  quantiles of the activation times the pole's sign, from the same counts; `mean`, `std`.
- `top_doc`, `top_pos`, `top_val`, `top_gate` (the gate pre-activation there): the 64 top firings; `neg_lobe`, the
  share of them on SiLU's negative lobe; `peak_tokens`, `next_tokens` (the tokens after the firings) and the
  first 5 `contexts`; `cur_mode`, `next_mode`, the share of the firings on the most common peak token, or before
  the most common next token. A pole with `act_top` under 0.05 is near-silent.
- `first_max`, `first_tokens`, `first_chat`: the first position (left out above, where the attention
  sink forms), where activations depend on the token alone: the largest over every kept token, the 3
  tokens that reach it, and the value on the chat transcript's opening token. Many of Qwen3-8B's L2-L3
  poles do their work there (§2).

![Activation scale and quiet poles by layer](figures/06_activations.png)

### `<model>-neurons-drivers`: exact token drivers

Every kept token at position 24 of 8 real documents (4 web, 2 code, 2 chat), averaged over them, bf16:
`drivers` are the 64 tokens with the largest activation at the token itself, `drivers_sum` summed over
it and the 16 positions after. Values are times the pole's sign. For Qwen3-8B, an fp32 check through L9
shared 98-99% of a pole's top 20 on average (94-99% for `drivers_sum`; §6).

![Which reads name the exact drivers](figures/11_drivers.png)

### `<model>-neurons-labels`: a label for every pole

Every pole described by Claude Haiku 5.5 from its reads and top contexts (batch API, effort low, adaptive
thinking; §8): `fires` (where it fires, 12 words or fewer), `writes` (what its write pushes the model
toward when amplified), each with a confidence 0-1, and `note`. Each model has its own prompt
(`scripts/prompts/<model>/neurons.md` on GitHub), which says which reads hold at each depth, and its
cards show only those. Qwen3-8B's labels were made from an earlier build of its tables, whose reads
kept byte-fallback pieces; Gemma 4's from text alone (its cards show no images or sounds). Neurons with a
negative-lobe pole (`neg_lobe` past a half) were labelled again from their up-row reads, and a pole that is a faint
shadow of the neuron's other pole is marked on its card (§8, §17).

Qwen3-8B, checked blind on 100 poles: firing labels separate held-out top firings from quiet positions at AUROC
0.82 [0.78, 0.85] (another pole's label: 0.56); a judge picks a pole's write label out of four from
steered text 61% of the time [0.52, 0.69] (chance 25%). Firing labels at confidence 0.7 or more score
0.94. They hold best early (83% of L0-L8's firing labels reach AUROC 0.8, 31% of L21-L27's), and write
labels late (80% picked at L28-L35, 41% at L0-L8). Of Gemma 4's neuron labels, only the relabelled negative-lobe poles are checked blind (§8).

![Random poles read blind](figures/14_lens_blind.png)

### `<model>-neurons-firings`: reads at the firings

The residual at a pole's 64 top firings, averaged (each firing scaled by its residual's RMS) and read through the lenses, §18:
`before_R`, `before_S`, the residual entering the MLP, through `mid`: what the pole's input holds where it fires; `mlp_R`, `mlp_S`, the
layer's whole MLP output there, through `out`: what the layer writes when the pole fires, the pole and the neurons firing with it;
and `pred`, the model's mean next-token logit there. Each has a `_z`
variant across the layer's poles that fired. `n_firings`: how many firings went in; a pole with none has `−1`, NaN and empty previews.
`parallel`, `orthogonal`, means over the firings: how much the pole's write amplifies (positive) or suppresses (negative) the part of the
residual it reads, as a multiple of that part, and how much it adds off that direction, on the same scale.

### `<model>-neurons-sources`: what drives a pole, and what fires with it

At a pole's first 5 top firings, the exact RelP split of its activation over the embedding, the heads and earlier neurons (§17). `driven_*`:
the 64 upstream poles with the largest mean share, `driven_head_*` the same of the heads, and `emb_share`, `heads_share`,
`neurons_share` each kind's mean share. `with_*`: the 64 earlier poles active at `act_top / 4` or more at the pole's firings, by lift
(`with_lift`, the share of those firings where they are active over their overall `rate`), with that share (`with_co`). `n_contexts`: the firings used. The three relations
differ: of a pole's top 16 driven-by sources, a median of 31-44% are in its top 16 wired-to or fires-with lists on Qwen3-8B, and 0-19% on Gemma 4 (every pole).

### `<model>-neurons-edges`: direct weight edges

What a neuron writes reaches every later layer's MLP input, so each pole has a direct edge to
every pole of a later layer (§17). Per pole, its 64 strongest in-edges (`in_*`, from earlier poles) and
out-edges (`out_*`, to later ones), strongest first: `_layer`, `_neuron`, `_pole` name the other pole;
`_cos` is the cosine of the earlier pole's write with the later pole's read direction, and `_push` is
`cos · act_top · ‖w‖ · gain / rms`, how far one of the earlier pole's top firings moves the later pole's
normalized input along its read direction (`rms` the residual's median RMS at the later layer's MLP
input; `gain` is 1 for Qwen3-8B and, for Gemma 4, the layer scalars between the two poles times the typical scale of the norm after the earlier MLP). Positive: the earlier pole's firing drives the later pole; negative: it pushes against it.
Edges rank by |push| among those with |cos| ≥ 5/√d = 0.078; `−1` and NaN fill shorter lists.

Edges are wiring, not traffic: on Qwen3-8B, a pole's push ranks every upstream neuron's effect when it fires at
Spearman 0.88, but its in-edges are a tenth of the 16 units that contribute most there, which are mostly
units firing with it (§17). At L1-L3, 49-78% of top firings have a negative gate, where the read
direction points the wrong way, and in-edges there are unreliable.

### `gemma-4-12b-neurons-image`, `gemma-4-12b-neurons-audio`: images and sound

Gemma 4 has no vision or audio encoder network: an image is 64 slots of 48 × 48-pixel patches (384
pixels a side) and a sound 64 slots of 40 ms at 16 kHz, each entering the residual through a few norms
and one linear map. One row per pole, beside the text tables:

| columns | what |
|---|---|
| `read_S_basis` | the read direction through the modality's S-lens to the MLP input, `c · K^mid_L`: coordinates (fp16) on the S-lens basis |
| `read_png` (image) | the 48 × 48 patch the direction reads: `read_S_basis` through the patch embedder back to pixels, at ±3 standard deviations around grey |
| `read_wave` (audio) | the 40 ms waveform it reads, 640 samples at 16 kHz (fp16) |
| `write_R`, `write_R_z` | the write through the modality's R-lens: what it makes the model say in image or audio contexts |
| `label`, `label_z`, `label_mean`, `labels_str` | its top labels by the z of its mean activation over each label's documents (labels on 8 or more documents: 1,643 for images, 981 for sound) |
| `sig`, `stable`, `auroc_heldout` | the top label past the shuffled-label null's 99th percentile for its layer; in the top 5 of both halves of the documents; chosen on even documents, its AUROC on odd ones |
| `top_doc`, `top_val` | the 64 documents with its largest mean activation (rows of `media/<modality>_docs.parquet`) |
| `text_fire_rank`, `text_read_rank`, `text_write_rank` | for a reliable label, its rank among the modality's labels on the text side (1 first, 0.5 chance): firing on the label's words, the text S-lens read, the text R-lens write |

A media read sums over a document's 64 slots, so it is one pattern wherever it sits, not a map of
where. Read `read_png` as what the pole's input direction looks like in pixels, a projection: added to
held-out images it raises the pole only at L0-L5 (§14). The exemplars say what fires a pole, and the
optimised reads below are patterns that drive it.

| modality | band | reliable top label | held-out AUROC (median) | its label holds on all three text tests |
|---|---|---|---|---|
| image | L0-L11 | 34% | 0.96 | 0% of 50,570 scored |
| image | L12-L23 | 26% | 0.97 | 3% of 57,935 scored |
| image | L24-L35 | 39% | 0.97 | 2% of 62,401 scored |
| image | L36-L47 | 32% | 0.97 | 1% of 82,879 scored |
| audio | L0-L11 | 51% | 0.91 | 0% of 45,812 scored |
| audio | L12-L23 | 21% | 0.85 | 1% of 38,652 scored |
| audio | L24-L35 | 30% | 0.82 | 0% of 93,345 scored |
| audio | L36-L47 | 19% | 0.77 | 0% of 70,224 scored |

![The patch each neuron reads, and the patch that drives it](figures/22_media_gallery.png)

**One concept in three modalities** (§15). 19 poles pass all three text tests for both their
image and their audio label, of 48,497 scored in both (independent lists would share
2.0): `L14 n8313 +` mosque indoor / Arabic; `L15 n146 +` coral reef / Maori; `L15 n8093 −` mosque indoor / Arabic; `L15 n10091 −` giant panda / Mandarin Chinese; `L18 n645 +` Arabian camel / Arabic; `L20 n13624 +` mosque outdoor / Arabic; `L21 n12154 +` mosque outdoor / Arabic; `L23 n2831 +` Sarees / Gujarati; `L31 n10862 −` tacos / Spanish; `L31 n12007 −` mosque outdoor / Arabic; `L33 n5249 +` tacos / Spanish; `L33 n6099 +` pagoda / Mandarin Chinese; `L33 n8917 −` pyramid / Arabic; `L36 n585 −` tacos / Spanish; `L36 n14109 +` totem pole / Maori; `L37 n6087 −` Pembroke / Welsh; `L37 n7165 +` giant panda / Mandarin Chinese; `L37 n7926 +` mosque outdoor / Arabic; `L41 n9498 −` mosque indoor / Arabic.

![One concept in text, images and sound](figures/23_crossmodal.png)

### `gemma-4-12b-neurons-image-optimised`, `gemma-4-12b-neurons-audio-optimised`

For the 48 poles a layer (L0-L35) with the strongest reliable label: one slot pattern, the same in all
64 slots, started from the S-lens read and optimised by gradient ascent through the model (24 Adam steps
over 128 images or clips; at most 0.08 of the pixel range, or 0.3 of each frame's RMS). `opt_png` or
`opt_wave` (in units of a frame's RMS), `gain` (the pole's mean activation over the slots of 8 held-out
documents with the pattern added, minus without), `gain_lens` (the same for its S-lens read),
`act_base`. Gains are in the pole's activation units:

| modality | band | poles | held-out gain, median (its S-lens read) | raises the pole | beats its S-lens read |
|---|---|---|---|---|---|
| image | L0-L11 | 576 | 0.195 (-0.0015) | 95% | 96% |
| image | L12-L23 | 576 | 0.00593 (-0.00066) | 70% | 73% |
| image | L24-L35 | 576 | 0.00102 (-5.4e-05) | 56% | 56% |
| audio | L0-L11 | 576 | 0.361 (0.0061) | 99% | 99% |
| audio | L12-L23 | 576 | 0.017 (0.00017) | 86% | 90% |
| audio | L24-L35 | 576 | 5.57e-05 (-3.4e-05) | 51% | 52% |

The audio test clips are among the audio S-lens's fitting clips (all of ESC-50), though not the
optimisation's.

## Heads

A head reads token `v` as its S-lens footprint at layer `L − 1`'s output (the embedding at L0) and writes
into layer `L`'s MLP input. Its OV circuit maps what it reads to what it writes, and its QK circuit
decides where it reads, both over the whole vocabulary (§11).

### `<model>-heads-reads`: weight-only reads, per token

| columns | read |
|---|---|
| `ov_R`, `ov_R_neg` | each token's z in its own column of the OV map read through the R-lens: where `v` ranks in what the head makes the model say when it reads `v`. The tokens it copies most, and suppresses most |
| `ov_S`, `ov_S_neg` | the same through the S-lens: whether the write makes the residual look as if `v` were there (the record through L8) |
| `qk_S`, `qk_S_neg` | each key token's z over the vocabulary under the head's mean query: what it attends to and avoids, whatever the query |
| `qk_self_S` | each token's z in its own row of the QK map, its footprint as the query too: where a position holding the token ranks earlier copies of it among the keys |
| `qk_self_R` | the same with the query the R-lens direction at `L − 1`'s output that promotes the token: where a position about to say it ranks earlier copies of it (from L1; empty at L0) |
| `ov_R_copy`, `ov_S_copy` | Elhage et al.'s copying score Σλ/Σ\|λ\| of each OV map: +1 copies what it reads, −1 suppresses it |
| `qk_self_S`, `qk_self_R` (numbers) | each diagonal's median z over tokens: duplicate-token heads score high on `qk_self_S`; late heads that look up what is about to be said on `qk_self_R`, copy suppressors among them where `ov_R_copy` is negative |
| `qk_ctx_rho` | Spearman over tokens between `qk_S` and the attention each token receives in context |
| `qk_ov_rho` | Spearman over tokens between `qk_S` and `ov_R`: does the head attend to what it copies? |

The QK map is `q̃ᵀ R̄ k̃`, with the q/k norms' true derivative averaged over real positions and RoPE
averaged over the head's own attention offsets, footprints at unit length: it reads which tokens a head
favours, not position-only behaviour such as previous-token or induction attention.

For Qwen3-8B, `qk_self_S` finds duplicate-token heads at AUROC 0.96. `qk_S` agrees with the attention tokens receive in context (`qk_ctx_rho` past +0.2) for 38% of L0-L8's heads (another head's read: 15%) and 33% of L28-L35's (3%); 12% of L28-L35's heads attend to what they copy (`qk_ov_rho` past +0.2; another head's OV read: 1%). For Gemma 4, `qk_self_S` at AUROC 0.95.

A head's median `qk_self_R` tracks how much it attends, in context, to earlier copies of the token its position is about to say (the R-lens top-1 at its input; `checks/head_seek.py`, §11): Spearman +0.62 across Qwen3-8B's L28-L35 heads (another head's read +0.11, `qk_self_S` -0.17), and it finds the 17 heads of L21-L35 that seek and lower that token's logit, copy suppression, at AUROC 0.91. On Gemma 4 the same holds more weakly: +0.26 at L24-L35 and +0.18 at L36-L47 (`qk_self_S` +0.07 and +0.11), AUROC 0.66 for its 25 seek-and-suppress heads (§13).

### `<model>-heads-acts`: firings and attention patterns

Over the same documents, from position 16 (a head with few keys attends sharply):

- `out_top`, `out_max`, `rate`, `rate_<slice>`, `q50`-`q999`, `mean`, `std`: as for neurons, of the norm
  of the head's output as it reaches the residual (`‖W_O^h z‖`; for Gemma 4, after its post-attention norm);
- `top_doc`, `top_pos`, `top_val`, `src_pos` (the position each firing attends to most, past the first),
  `peak_tokens` (query tokens), `src_tokens` (attended tokens), `contexts`;
- `sink`, `prev`, `self`: the mean attention from queries at 16+ to the first position, to the token
  before and to itself; `induction`, `duplicate`: over 64 sequences of 64 random tokens said twice,
  attention from the second copy to the token after the first occurrence, and to the occurrence;
- `out_R_z`: the firings' outputs read through the R-lens from the MLP input, each token's logit
  z-scored across the layer's firings, averaged over the head's;
- `cur_mode`, `src_mode`: the share of the firings on the most common query token, or attending most to the
  most common token.

### `<model>-heads-drivers`: exact token drivers

In the same pass as the neurons': `drivers`, the 64 tokens with the largest output norm at their own
position (the token as the query), and `keys`, the 64 that receive the most attention from the 16
positions after them (the token as the key).

### How often head reads name their firings

`checks/reads_at_firings.py` (§12), at each head's top firings, with the attended token: `ov_R` (its OV column promotes the
token after the query), `ov_copy` (its own `ov_R` z: the head promotes what it reads), `ov_S` (its own `ov_S` z), `qk_S` (its
`qk_S` z: the QK read predicts what the head attends to), against the layer's other heads on the same firings, at a 5% false
discovery rate over all heads; and the share with an attention pattern score past a threshold (`prev` or `self` past 0.5,
`induction` or `duplicate` past 0.3). As for neurons, these are population results, and the catalog keeps no per-head
test. Share of each band's heads, Qwen3-8B:

| band | `ov_R` | `ov_copy` | `ov_S` | `qk_S` | pattern |
|---|---|---|---|---|---|
| L0-8 | 0% | 1% | 0% | 0% | 10% |
| L9-12 | 1% | 2% | 0% | 1% | 8% |
| L13-20 | 1% | 1% | 0% | 0% | 8% |
| L21-27 | 4% | 2% | 0% | 0% | 6% |
| L28-35 | 26% | 16% | 0% | 8% | 4% |
| all | 7% | 5% | 0% | 2% | 7% |

The S-side tests pass for almost no head. S→S copying and the mean query's favourite keys are shared by a
layer's heads, so at a head's own firings they don't tell it from its neighbours; they remain reads of
what each head does (§12).

![What each head's reads name](figures/17_head_census.png)

Gemma 4 has 16 heads a layer, so a head's mismatched control has 240 pairs, no p-value falls below
1/241, and BH over its 768 heads passes none. Share of each band's heads at an uncorrected p ≤ 0.05 (5% by
chance):

| band | `ov_R` | `ov_copy` | `ov_S` | `qk_S` | pattern |
|---|---|---|---|---|---|
| L0-11 | 5% | 5% | 5% | 8% | 15% |
| L12-23 | 2% | 9% | 3% | 7% | 9% |
| L24-35 | 11% | 9% | 5% | 9% | 6% |
| L36-47 | 23% | 18% | 5% | 14% | 8% |
| all | 10% | 10% | 4% | 10% | 10% |

### `<model>-heads-labels`: a label for every head

Qwen3-8B:

Every head described by Claude Haiku 5.5 from its card (batch API, effort low, adaptive thinking):
`fires` (where its output is large), `attends` (what it attends to there) and `writes` (what its
output promotes), each with a confidence 0-1, and `note`. The cards show the head's pattern scores,
output scale, OV and QK reads, drivers and first 5 top contexts; nothing about its other top firings.
The prompt is `scripts/prompts/qwen3-8b/heads.md` on GitHub.

**Checked blind** on 100 random heads, 20 a band, by Claude Sonnet 5.5:

- **Firing:** given a head's `fires` and `attends` labels and 8 contexts, 4 of its held-out top firings (ranks 6-24) and 4 of another head of its band, the scorer separates them at AUROC 0.70 [0.64, 0.77]; a third head's labels on the same contexts score 0.50.
- **Writes:** given what the head's firings actually promote in context (`out_R_z`, not on the card), a judge picks its `writes` label out of four from its band 54% of the time [45, 65] (chance 25%).

| band | firing AUROC | control | writes picked |
|---|---|---|---|
| L0-L8 | 0.73 | 0.52 | 28% |
| L9-L12 | 0.72 | 0.57 | 67% |
| L13-L20 | 0.74 | 0.36 | 42% |
| L21-L27 | 0.64 | 0.54 | 55% |
| L28-L35 | 0.67 | 0.51 | 79% |

Gemma 4 12B: its write labels are near chance, so read them as guesses.

Every head described by Claude Haiku 5.5 from its card (batch API, effort low, adaptive thinking):
`fires` (where its output is large), `attends` (what it attends to there) and `writes` (what its
output promotes), each with a confidence 0-1, and `note`. The cards show the head's pattern scores,
output scale, OV and QK reads, drivers and first 5 top contexts; nothing about its other top firings.
The prompt is `scripts/prompts/gemma-4-12b/heads.md` on GitHub.

**Checked blind** on 80 random heads, 20 a band, by Claude Sonnet 5.5:

- **Firing:** given a head's `fires` and `attends` labels and 8 contexts, 4 of its held-out top firings (ranks 6-24) and 4 of another head of its band, the scorer separates them at AUROC 0.71 [0.64, 0.78]; a third head's labels on the same contexts score 0.49.
- **Writes:** given what the head's firings actually promote in context (`out_R_z`, not on the card), a judge picks its `writes` label out of four from its band 32% of the time [22, 42] (chance 25%).

| band | firing AUROC | control | writes picked |
|---|---|---|---|
| L0-L4 | 0.74 | 0.48 | 25% |
| L5-L13 | 0.74 | 0.54 | 35% |
| L14-L32 | 0.70 | 0.47 | 39% |
| L33-L47 | 0.67 | 0.47 | 30% |

### `gemma-4-12b-heads-image`, `gemma-4-12b-heads-audio`: heads in image and audio contexts

64 labelled images (mini-ImageNet) and 64 sounds (ESC-50, the classes in turn), each in the media prompt
and followed by ` a <label>`, its own and another class's (§16). Per head and modality: `read`,
`read_ratio` (attention from the text after the media to its slots, and that over an even spread),
`sink`, `self`, `within`, `nbr` (attention from a slot to itself, the other slots, and its grid
neighbours or the frame before); `abl_right`, `abl_wrong`, `content`, `content_z` (each head zeroed: the
change in the label's loss, right and wrong, and their difference); `write_mid`, `write_logit` and their
`_q` (the head's output at the article read through the R-lens and the logit lens: the right class's
mean percentile among the classes, against 200 label shuffles); `top1_mid`, `top1_logit`.

- **image** (64 documents, 64 classes): the right label's loss is below a wrong one's for 97% (3.64 against 10.29 nats). Most read from the text: L24h13, L44h7, L31h3, L23h8; largest extra loss when zeroed (nats): L8h15 (0.75), L7h13 (0.65), L44h7 (0.43), L38h6 (0.42); top label writers: L37h10, L44h7, L40h6, L46h4.
- **audio** (64 documents, 49 classes): the right label's loss is below a wrong one's for 55% (6.48 against 6.56 nats). Most read from the text: L8h5, L7h9, L3h6, L4h0; largest extra loss when zeroed (nats): L9h4 (0.06), L4h8 (0.06), L11h1 (0.06), L10h15 (0.06); top label writers: L47h4, L45h11, L32h4, L30h13.

Share of each band's heads that cost the right label more than a wrong one at z > 3, and that write the right class at q ≤ 0.05, images: L0-11 4%, 4%; L12-23 12%, 43%; L24-35 29%, 41%; L36-47 8%, 36%. For sound, no head passes either.

![Heads in image and audio contexts](figures/24_heads_media.png)

## Plain files

Per model folder (`qwen3-8b/`, `gemma-4-12b/`):

- `docs.parquet`: each activation document's `slice`, its `line` in the slice's file and its length.
  The slices' sources, revisions and row ids are in `data/corpus/act-<slice>.provenance.json` on GitHub:
  the corpus is not re-hosted here.
- `token_counts.pt`: `counts[v]`, how often token `v` occurs in the activation corpora (`by_slice` per
  slice).
- `causal/causal.pt`: the causal sample (§3, §13). `picks`: 1,194 Qwen3-8B neurons
  `(layer, neuron)`, 32 random per layer plus named ones, or 1,152 of Gemma 4's, 24 random
  per layer. Per neuron and pole: `steer` `[neuron, pole, dose, vocab]`, the mean change in log-probs
  over positions 16-63 of 16 64-token DCLM contexts (`contexts`) when the write is added there at 1× and
  4× `alpha` (the pole's `act_top`); `ablate_pos` and `ablate_win`, clean − ablated log-probs with the
  neuron zeroed at its peak in its first 8 top documents, at that position and summed over the next 8;
  `top_doc` (rows of `docs.parquet`) and `top_pos`, where each of those ablations was made, as in the
  `acts` table (−1 where the pole never fired); `dlogp_next`, the next token's change per document;
  `fired`, the activation there. Every input is in the file, so it can be re-measured from it alone.
  bf16 (Qwen3-8B's on MPS); weak effects differ by device (§3).
- `gemma-4-12b/media/{image,audio}_docs.parquet`: each image or sound document's `source`, `labels`,
  `caption`, `ref` (JSON: the dataset, config, split and revision, the row's own identifiers, the media
  file's path and its bytes' SHA-1) and `link`. The images and sounds are not re-hosted;
  `data/corpus/media-<modality>.provenance.json` on GitHub lists every source with its license.

## Loading

```python
import pandas as pd

base = "hf://datasets/stdlogits/neuron-lens/qwen3-8b"
reads = pd.read_parquet(f"{base}/neurons/reads/L08.parquet")
reads.query("neuron == 344 and pole == 1")[["write_R_str", "read_R_str", "read_S_str"]]
heads = pd.read_parquet(f"{base}/heads/reads.parquet").merge(pd.read_parquet(f"{base}/heads/acts.parquet"))
heads.query("layer == 20 and head == 17")[["ov_R_str", "qk_S_str", "duplicate", "contexts"]]

base = "hf://datasets/stdlogits/neuron-lens/gemma-4-12b"
image = pd.read_parquet(f"{base}/neurons/image/L33.parquet").query("neuron == 6099 and pole == 1").iloc[0]
docs = pd.read_parquet(f"{base}/media/image_docs.parquet")
image[["label", "labels_str", "text_fire_rank"]], docs.loc[image["top_doc"][:4], ["labels", "link"]]
```

## Limits

- Two models; the text lenses are fitted on English-heavy web text, Gemma 4's media lenses on COCO
  photos and ESC-50 sounds.
- Activation statistics come from bf16 passes over documents of up to 256 tokens; top firings are one
  per document.
- The tests are token-level, over at most 64 firings per unit and 64 exact drivers per pole. A read can be right about a
  concept that shows in no single token (§7).
- Heads are read through their circuits one token at a time: a head whose role depends on the query's
  context, or on position alone, is read only through `acts`.
- Media labels name what a whole image or sound is about, not each patch or frame; media reads lose
  fidelity with depth (§14).

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The catalog is derived from
[`Qwen/Qwen3-8B`](https://huggingface.co/Qwen/Qwen3-8B) and
[`google/gemma-4-12B`](https://huggingface.co/google/gemma-4-12B) (both Apache 2.0). Its `contexts` quote
short excerpts of the activation corpora, which keep their own terms:
[DCLM](https://huggingface.co/datasets/HuggingFaceFW/dclm_100BT-shuffled) (CC BY 4.0),
[FineWeb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) (ODC-By 1.0),
[codeparrot-clean](https://huggingface.co/datasets/codeparrot/codeparrot-clean) (code from public GitHub
repositories, under their licenses) and
[UltraChat-200k](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k) (MIT). The media
documents' labels and captions come from their source datasets, under those datasets' terms (some
non-commercial); the images and sounds themselves are only linked. By [@_a9lim](https://x.com/_a9lim)
and [@treetowntree](https://x.com/treetowntree) with Claude (Anthropic), 2026-11-11. [Matthew Khoriaty](https://www.lesswrong.com/users/matthew-khoriaty) suggested the orthogonal write read.

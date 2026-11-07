# Échantillon J-A, mode `direction` : 16 paires

Chaque paire : le même contexte (la tâche, voir `taches.md`), deux actions X et Y ; le champ COST est masqué.

## JAD-01 (tâche 2602.01626v1)

**Action X** :

```
ACTION: ADD
TITLE: Grounding joint alignment of many representations in total correlation
PROPOSAL: We derive a contrastive objective over the embeddings of one instance from all models as a variational bound on their total correlation, which captures dependence among all of them and not only between pairs, and we show how the existing Gramian loss arises as a special case. We validate on synthetic data with higher-order dependence and on multi-view benchmarks.
CONTROLS: Pairwise losses over all pairs, the Gramian loss, independent training, and synthetic data with only pairwise dependence.
COST: [masqué]
PREDICTION: The derived loss should recover higher-order structure that pairwise losses miss. Bound looseness could hurt with high-dimensional embeddings.
```

**Action Y** :

```
ACTION: ADD
TITLE: Aligning many representations through a shared anchor model
PROPOSAL: We designate one model as an anchor and align every other model's embeddings to the anchor with a pairwise contrastive loss, so the number of loss terms grows only linearly with the number of models, and we argue that alignment then propagates among all models through the anchor. We validate on synthetic data with higher-order dependence and on multi-view benchmarks.
CONTROLS: Pairwise losses over all pairs, the Gramian loss, independent training, and synthetic data with only pairwise dependence.
COST: [masqué]
PREDICTION: Anchor alignment should match all-pairs alignment at lower cost of training. Models far from the anchor may align poorly with one another.
```

## JAD-02 (tâche 2603.21115v1)

**Action X** :

```
ACTION: ADD
TITLE: Anytime segmentation across driving, legged and aerial platforms
PROPOSAL: We train a causal image and event anytime segmentation model on driving data and test it on quadruped and drone recordings with dense labels inside the interval, to see whether high-rate semantic perception from slow cameras holds beyond cars. We analyse per-class accuracy against offset on each platform.
CONTROLS: Per-platform models, the copied segmentation, event-only models, and short fine-tuning.
COST: [masqué]
PREDICTION: Static classes should transfer while moving ones need tuning. Drone viewpoints may hurt most, since their scale and motion differ from road scenes.
```

**Action Y** :

```
ACTION: ADD
TITLE: Multi-platform frame segmentation datasets for robots
PROPOSAL: We assemble a multi-platform segmentation dataset of driving, quadruped and drone recordings labelled at the camera frame rate, and benchmark frame segmenters trained on one platform and tested on the others, to see how semantic perception from slow cameras holds beyond cars. We analyse per-class accuracy on each platform.
CONTROLS: Per-platform models, models trained on all platforms, event-only models, and short fine-tuning.
COST: [masqué]
PREDICTION: Road and building classes should transfer while others need tuning. Drone imagery may differ most, since its altitude and framing are far from cars.
```

## JAD-03 (tâche 2510.26843v1)

**Action X** :

```
ACTION: ADD
TITLE: A distilled compact drafter as the middle level above retrieval drafting
PROPOSAL: We distil a four-layer decoder from Llama-2-13B-chat, Llama-3-8B-instruct and Qwen2.5-14B-instruct on their own greedy outputs for the Spec-Bench prompt distribution and a general instruction corpus, initialising it from the target's embeddings and lowest layers, and we place it as the middle level of a cascade whose bottom level is prompt lookup. We sweep draft lengths per level and the number of lower-level rounds per upper round, and report walltime speedup over autoregressive decoding and acceptance per level.
CONTROLS: Lookup alone, the distilled drafter alone without lookup, autoregressive decoding, a distilled drafter of eight layers, identity of outputs with greedy decoding, and repeated timings with warm caches.
COST: [masqué]
PREDICTION: We expect the distilled drafter to accept well over half of its tokens and the cascade to beat lookup alone on every category. If acceptance stays low on reasoning, more distillation data from that domain should close the gap.
```

**Action Y** :

```
ACTION: ADD
TITLE: A training-free cascade of self-draft levels above retrieval drafting
PROPOSAL: We build cascades of depth two and three in which every level above prompt lookup is a self-derived drafter of the target, a layer-skipping copy and an early-exit copy ordered by latency, so that no draft model is trained. We run Llama-2-13B-chat, Llama-3-8B-instruct and Qwen2.5-14B-instruct on Spec-Bench, sweep draft lengths per level and the number of rounds the lower levels run per upper round, and report walltime speedup over autoregressive decoding and acceptance per level.
CONTROLS: Lookup alone, each self-derived drafter alone, Lookahead decoding alone, autoregressive decoding, every two-level sub-cascade of the three-level one, identity of outputs with greedy decoding, and repeated timings with warm caches.
COST: [masqué]
PREDICTION: We expect the two-level cascade to beat lookup alone on chat and reasoning, and the third level to add little because the two self-derived copies have similar acceptance. If no cascade beats lookup alone on any category, the answer to the first question is negative for current training-free drafters.
```

## JAD-04 (tâche 2602.12660v2)

**Action X** :

```
ACTION: ADD
TITLE: Ordinal cut points to ground a pairwise reward model in an absolute scale
PROPOSAL: We fit a reward head on Skywork-Reward-Preference through a Bradley-Terry likelihood and learn ordered cut points mapping its score to quality bins from a small set of pointwise ratings in HelpSteer2, so that abundant pairs fix the ranking and scarce ratings fix the scale. On Llama-3.1-70B-instruct and Llama-3.1-8B-instruct we vary the number of ratings and measure bin accuracy on held-out ratings, fixed-threshold precision across chat, mathematics and code, and ranking accuracy on RewardBench.
CONTROLS: A scalar head with per-domain standardisation, the same head with Platt scaling on the ratings, a head trained on ratings alone, cut points fitted to shuffled ratings, and three seeds.
COST: [masqué]
PREDICTION: We expect bin accuracy to saturate after the first few hundred ratings and ranking accuracy to be untouched, with the larger backbone needing fewer ratings. If Platt scaling matches the cut points everywhere, an affine map suffices to ground the scale.
```

**Action Y** :

```
ACTION: ADD
TITLE: Reinforcement-trained critiques to raise the pairwise accuracy of a generative judge
PROPOSAL: We train a generative judge on Llama-3.1-70B-instruct and Llama-3.1-8B-instruct to write a critique of two responses and then name the better one, using reinforcement learning with a reward of one when the named response matches the preferred one in Skywork-Reward-Preference, with a length penalty on the critique and eight sampled critiques per pair during training. We measure pairwise accuracy on RewardBench and RM-Bench and the length of the critiques, and we test whether sampling several critiques at inference and voting raises accuracy further.
CONTROLS: The same judge trained by supervised fine-tuning on critiques from a larger model, the judge without any critique, a scalar Bradley-Terry head of the same backbone, voting over one, four and sixteen critiques, and three seeds.
COST: [masqué]
PREDICTION: We expect the reinforcement-trained judge to exceed the scalar head on reasoning pairs and to trail it on chat, with voting adding a few points at a rising inference price. Critiques should get longer during training unless the length penalty is strong.
```

## JAD-05 (tâche 2512.22550v1)

**Action X** :

```
ACTION: ADD
TITLE: Decoding the horizon coarse to fine from learned block queries
PROPOSAL: We replace the linear projection with two heads that decode at two resolutions. From a channel-independent patch encoder, learned block queries predict one value per block of 24 future steps; a refinement head then expands each block to full resolution, conditioned on the coarse prediction and on the encoded past through cross-attention. Both heads train together, with the coarse loss weighted up early so the model learns the low-frequency shape first. We evaluate on ETTh1, ETTh2, ETTm1, ETTm2, Weather, Electricity, Traffic and Solar at horizons 96, 192, 336 and 720, reporting mean squared error at both resolutions and per horizon step.
CONTROLS: Linear projection on the same encoder, a single-resolution query decoder of matched parameter count, the coarse head alone with linear upsampling, both heads without the coarse loss, DLinear and PatchTST as external references, three seeds, and bootstrap intervals over test windows.
COST: [masqué]
PREDICTION: Coarse-to-fine decoding should lower error at horizons 336 and 720 on Weather and Electricity and match the linear head at 96. It fails on ETTm1 and ETTm2 if the refinement head cannot recover the high-frequency content that the coarse head discards.
```

**Action Y** :

```
ACTION: ADD
TITLE: How far the linear projection head goes with a longer lookback
PROPOSAL: We keep the linear projection head and ask how much of the long-horizon error is a matter of context length rather than of decoding. With a channel-independent patch encoder fixed, we vary the lookback from 96 to 1440 steps and measure how error at each horizon falls as context grows, on ETTh1, ETTh2, ETTm1, ETTm2, Weather, Electricity, Traffic and Solar at horizons 96, 192, 336 and 720. We fit a saturation curve per dataset and horizon, report the lookback beyond which error stops improving, and compare the memory and throughput price of the longer context with the error reduction, so that practitioners know when more context is worth it.
CONTROLS: DLinear at the same lookbacks, PatchTST at its published lookback, the encoder with and without instance normalization, a placebo that extends the lookback with shuffled older windows, lookbacks at six lengths, three seeds, and bootstrap intervals over test windows.
COST: [masqué]
PREDICTION: Error should fall until a lookback near 720 on the ETT sets and keep falling on Traffic, with memory growing linearly. If the shuffled placebo gains as much as the true lookback, the gain is a normalization effect rather than information from the past.
```

## JAD-06 (tâche 2603.12594v1)

**Action X** :

```
ACTION: ADD
TITLE: Mapping the training dynamics of contrastive learning through loss curvature
PROPOSAL: We characterise the information landscape of contrastive training by tracking, across training, the leading eigenvalues of the loss Hessian and the effective rank of the representation for SimCLR ResNet-18 on CIFAR-100 and ImageNet-100 at two batch sizes, using power iteration on mini-batches every few epochs. We then relate the moment at which the effective rank plateaus to the final linear probe accuracy across learning rate and temperature settings, producing a description of how the geometry of the loss evolves from early to late training.
CONTROLS: Supervised training with the same backbone as a reference trajectory, a randomly initialised encoder for the starting point, and three seeds.
COST: [masqué]
PREDICTION: Effective rank should plateau earlier at the larger batch, and the plateau epoch should predict final accuracy within two points. The result is refuted if the plateau epoch varies more across seeds than across settings.
```

**Action Y** :

```
ACTION: ADD
TITLE: Characterising view information gain as a conditional entropy and validating it by ablation
PROPOSAL: We define the information a view adds for an instance as the entropy of the view embedding conditional on the anchor embedding under a momentum encoder, estimate it per instance with a variational decoder, and test whether the quantity has predictive content: we rank instances by the estimate, remove augmentation for the top and bottom deciles in separate SimCLR ResNet-18 runs on CIFAR-100 and ImageNet-100, and measure the resulting change in linear probe accuracy.
CONTROLS: Random deciles of the same size, ranking by loss value, the estimate recomputed on a frozen encoder, and three seeds.
COST: [masqué]
PREDICTION: The top decile removal should cost at least four times as much accuracy as the bottom decile removal. The definition is refuted if the ranking is no better than loss value or than random.
```

## JAD-07 (tâche 2511.04675v2)

**Action X** :

```
ACTION: ADD
TITLE: Compressing the spatiotemporal history that a video generator attends to
PROPOSAL: We keep the last four frames at full scale and all earlier frames only at their two coarsest scales, then train with random history cut-offs so the model tolerates any length, and we generate minute-long clips at 480p to measure how consistency and per-frame latency change as the history grows.
CONTROLS: Attention over the full history up to the longest length that fits, a four-frame sliding window, a first-frame anchor window as a check on identity alone, and key-value cache merging at equal memory, measured by VBench-Long consistency, FVD on UCF-101, CLIP drift to the first frame and per-frame latency, over three seeds.
COST: [masqué]
PREDICTION: Coarse history should hold consistency near full attention with flat latency, and beat the sliding window by a wide gap. If the first-frame anchor does as well, the model only needs identity, not layout history.
```

**Action Y** :

```
ACTION: ADD
TITLE: Speculative decoding with a small draft model for faster video token generation
PROPOSAL: We pair the next-scale video generator with a 300M draft model that proposes the bits of each scale, verified in one pass by the large model, and we measure the speed-up and any change in quality on minute-long clips at 480p, with both models attending to the complete history of generated frames.
CONTROLS: The large model decoding alone as the quality reference, the draft model alone as the floor, acceptance rates per scale, and two draft lengths with the acceptance threshold tuned on a held-out prompt set, measured by VBench-Long consistency, FVD on UCF-101 and per-frame latency, over three seeds.
COST: [masqué]
PREDICTION: Speculative decoding should cut per-frame latency by about half at unchanged quality, with acceptance highest at coarse scales. If acceptance drops at the finest scales, the draft model is too small for texture detail and a larger draft should be tried.
```

## JAD-08 (tâche 2512.01987v3)

**Action X** :

```
ACTION: ADD
TITLE: Few-episode online adaptation of an offline policy to each new offset pattern
PROPOSAL: We fine-tune a CQL policy pretrained on D4RL Hopper, HalfCheetah and AntMaze-umaze whenever the deployment stream enters a new regime, using the first few episodes of that regime as online interaction data with a small learning rate and a behaviour-cloning anchor to the pretrained policy. Regime changes are detected from a drop in the running return, and the adapted policy is then used until the next detected change. Streams follow recorded jump and drift series, and we report return along the stream, the number of adaptation phases triggered and the return during adaptation episodes.
CONTROLS: The pretrained policy without adaptation as the floor, adaptation with the anchor removed, the learning rate at three settings, adaptation triggered at fixed intervals instead of by detection, and the policy given the true offset, over three seeds.
COST: [masqué]
PREDICTION: Adaptation should lift return on long stable regimes and cost return during the first episodes of each regime. Where regimes change every episode, as in the jump series, there may be no phase in which the adapted policy is useful.
```

**Action Y** :

```
ACTION: ADD
TITLE: Particle inference of per-dimension offsets with a learned model
PROPOSAL: We run, inside every test episode, a particle filter over the offset vector whose particles are initialised from a wide heavy-tailed prior and reweighted at each step by the likelihood of the corrected transition under a dynamics ensemble trained offline, with resampling when the effective sample size drops. A frozen CQL policy acts on the observation corrected by the weighted particle mean. We evaluate on D4RL Hopper, HalfCheetah and AntMaze-umaze with offsets from recorded jump and drift series, reporting return along the stream and the error of the particle mean per step.
CONTROLS: The policy on uncorrected observations, the policy with the true offset, the filter with a Gaussian prior of small width, the filter driven by a randomly initialised dynamics model, and the particle count at three settings, over three seeds.
COST: [masqué]
PREDICTION: The particle mean should converge within the first steps on locomotion and bring return near the true-offset variant from early in each episode. If the random-model filter does as well, the dynamics model is not what drives the correction.
```

## JAD-09 (tâche 2508.05606v3)

**Action X** :

```
ACTION: ADD
TITLE: Reinforcement learning on verbalised state descriptions for visual tasks
PROPOSAL: We strengthen the textual reasoning of Qwen2.5-VL on maze navigation, jigsaw solving and geometry by group-relative policy optimisation with simulator-checked final answers, where every chain must describe the visual state after each step in a fixed textual schema, grid coordinates for mazes, piece placements for jigsaws and point coordinates for geometry, so that transitions are tracked in words without producing any image. Eight chains are sampled per problem and the schema is enforced by a format reward. We report held-out accuracy, the share of chains whose described states match the simulator, and chain length.
CONTROLS: Supervised fine-tuning on schema-formatted chains at the same number of examples, the same training without the format reward, free-form chains as the floor, the final-answer reward only, and a pipeline that renders the described states with an external generator for visualisation only, over three seeds.
COST: [masqué]
PREDICTION: Schema-formatted chains should beat free-form ones on navigation and jigsaw and the state-match share should rise over training. On geometry the schema may be too coarse and the gain may vanish there.
```

**Action Y** :

```
ACTION: ADD
TITLE: Emitting only the changed image tokens at each reasoning step
PROPOSAL: We train Show-o to represent each intermediate visual state by the discrete image tokens that differ from the previous state together with their positions, a learned detector choosing the positions, while a small state cache outside the attention context holds the full current state for reconstruction. A maze move or a jigsaw swap then costs a few tokens and a full redraw stays possible when the detector marks every position. Training uses simulated navigation, jigsaw and contour-to-landscape chains, and we report held-out accuracy, visual tokens per step and reconstruction fidelity.
CONTROLS: Full-image interleaving at equal data, text-only chains, direct answers, a random subset of positions of the same size as the detector's choice, the cache disabled so that changes must be inferred from context, and the detector threshold at two values, over three seeds.
COST: [masqué]
PREDICTION: Change encoding should cut visual tokens per step by an order of magnitude on navigation and jigsaw at equal accuracy and lose fidelity on landscape chains where most pixels change. If the random subset matches it, position selection is not the ingredient that matters.
```

## JAD-10 (tâche 2509.24365v3)

**Action X** :

```
ACTION: ADD
TITLE: Reconstruction Quality of Image Tokenizers Across Codebooks
PROPOSAL: Compute reconstruction error, perceptual distance and codebook usage on 100000 images from public corpora, with tokenizers of three codebook types. Measure the reconstruction fidelity for a 300M model trained on each tokenizer, and correlate reconstruction quality with the codebook usage.
CONTROLS: Compare each tokenizer score against the score between two image corpora. Compare against the score between two codebook sizes. Compare against the score between two tokenizers on the same images. Repeat over 3 seeds of data order.
COST: [masqué]
PREDICTION: Larger codebooks should align with better reconstruction. The idea fails if the correlation is near zero for all tokenizers.
```

**Action Y** :

```
ACTION: ADD
TITLE: Entropy and Repetition of Image Tokens Versus Text Tokens
PROPOSAL: Compute token entropy, n-gram repetition and compressibility on 100000 text sequences and 100000 image-token sequences from public corpora, with image tokens from three tokenizers. Measure per-layer gradient cosine for a 300M model trained on each pairing, and correlate conflict strength with the statistic gaps.
CONTROLS: Compare each statistic gap against the gap between two text corpora. Compare against the gap between two image corpora. Compare against the gap between two tokenizers on the same images. Repeat over 3 seeds of data order.
COST: [masqué]
PREDICTION: Larger statistic gaps should align with stronger conflict. The idea fails if the correlation is near zero for all statistics.
```

## JAD-11 (tâche 2506.12932v2)

**Action X** :

```
ACTION: ADD
TITLE: Coordinate dimension as the source of the curse of dimensionality
PROPOSAL: Fix the city count at 60 and raise the coordinate dimension through 2, 3, 4, 6, 8 and 12 for a transformer of one width, training on fresh instances in each dimension until validation tour length settles. Targets come from an exact solver at low dimension and a long local-search run at high dimension. Fit the settled optimality gap against dimension with a power law and an exponential.
CONTROLS: Nearest-neighbour tours in each dimension serve as reference. Three seeds per dimension give the noise level. A model of twice the width in the two highest dimensions shows whether capacity relieves the growth.
COST: [masqué]
PREDICTION: The gap should rise with dimension and the exponential form should fit better once distances concentrate.
```

**Action Y** :

```
ACTION: ADD
TITLE: City count as the source of combinatorial growth in the solution space
PROPOSAL: Keep the points in the plane and let the number of stops climb over 20, 40, 80, 160, 320 and 640, using a transformer of unchanged width that sees newly sampled instances at every count and trains until validation tour length settles. Labels come from an exact solver for the smaller counts and an extended local search for the larger ones. Relate the settled optimality gap to the number of stops by a power law and by an exponential.
CONTROLS: At every count a nearest-neighbour tour is the reference. Three seeds per count give the noise level. Doubling the width at the two largest counts shows whether capacity relieves the growth.
COST: [masqué]
PREDICTION: The gap should rise with the number of stops, and the power form should fit better at large counts.
```

## JAD-12 (tâche 2507.01785v3)

**Action X** :

```
ACTION: ADD
TITLE: Separating rater taste from the signal across different prompt wordings
PROPOSAL: Have a single instruction-tuned model grade 40000 documents in 24 languages five times, each time with a paraphrased rubric, and record how often the wordings concur on the highest-rated fifth. Fit a rater to every wording's grades plus one to the pooled grades, and contrast the documents that each rater picks.
CONTROLS: Agreement among independent human readers on a small subset gives a reference for agreement. Three seeds for each rater.
COST: [masqué]
PREDICTION: Raters from single wordings should select partly different documents, and the combined rater should sit closer to all of them.
```

**Action Y** :

```
ACTION: ADD
TITLE: Separating rater taste from the signal across different judging models
PROPOSAL: Label 40000 documents in 24 languages with five instruction-tuned models from different families under one rubric, and measure how often the models agree on the top fifth. Train one rater on each model's labels and one on the combined labels, then compare which documents each rater selects.
CONTROLS: Agreement among independent human readers on a small subset gives a ceiling for agreement. Three seeds for each rater.
COST: [masqué]
PREDICTION: Raters from single models should select partly different documents, and the combined rater should sit closer to all of them.
```

## JAD-13 (tâche 2603.11047v1)

**Action X** :

```
ACTION: ADD
TITLE: Part-Level Editing Through Segmentation of Latent Object Tokens
PROPOSAL: Add a segmentation head to latent object tokens so that parts such as handles, lids and legs can be selected and replaced by swapping token subsets. Train the head on 300 annotated objects, then judge edits by part overlap and by rendered consistency of the untouched regions. Latent training itself reuses a pretrained autoencoder.
CONTROLS: Compare against segmentation on rendered images lifted to three dimensions, hold out annotated objects, and repeat with seeds.
COST: [masqué]
PREDICTION: Part overlap should exceed that of the image-lifting alternative, with untouched regions preserved. The direction fails if edits leak across parts or consistency degrades.
```

**Action Y** :

```
ACTION: ADD
TITLE: Training Joint Latents Directly from Raw Meshes and Renders
PROPOSAL: Build a pipeline that trains a joint geometry-appearance latent from unmodified meshes and rendered views, using sampled surface points and photometric loss with no signed-distance conversion or primitive fitting. Measure preparation time per object, failed samples, and the fidelity of the resulting latent on 300 held-out objects.
CONTROLS: Compare against a pipeline that first converts meshes to watertight form, hold out objects, and repeat with seeds.
COST: [masqué]
PREDICTION: Preparation time should fall sharply with fidelity close to the converted-mesh pipeline. The direction fails if raw-mesh training destabilises or loses accuracy on thin structures.
```

## JAD-14 (tâche 2603.11047v1)

**Action X** :

```
ACTION: ADD
TITLE: Compactness Versus Fidelity Against Voxel Latents for Single Objects
PROPOSAL: Train joint autoencoders with different token counts on the same objects, and place each point on a plot of memory footprint against reconstruction fidelity and geometry error. Compare against sparse and dense voxel latents at similar memory, using 150 held-out objects with glossy materials. The study asks where the token representation overtakes grids.
CONTROLS: Compare against sparse and dense voxel latents, hold out whole objects, and repeat with seeds.
COST: [masqué]
PREDICTION: Token latents should reach similar fidelity to voxel grids with a smaller memory footprint. The direction fails if grids stay better at every memory level.
```

**Action Y** :

```
ACTION: ADD
TITLE: Scene-Scale Latents for Rooms with Many Objects
PROPOSAL: Train a latent autoencoder on indoor room scans containing dozens of objects, compressing each room into a fixed set of 768 tokens and decoding color and depth for novel viewpoints. Judge reconstruction by image fidelity and layout agreement on 150 held-out rooms. The study focuses on how large spaces rather than single objects are compressed.
CONTROLS: Compare against a voxel latent at room scale, hold out whole rooms, and repeat with seeds.
COST: [masqué]
PREDICTION: Image fidelity should be comparable to the voxel latent with far fewer tokens. The direction fails if object detail disappears as the number of objects grows.
```

## JAD-15 (tâche 2509.21302v4)

**Action X** :

```
ACTION: ADD
TITLE: Scene-Level Held-Out Evaluation of Quantized VGGT Ranges
PROPOSAL: Fit 8-bit activation ranges for VGGT on 48 frames sampled from 40 ScanNet sequences, and evaluate the quantized model on entirely different scenes: further indoor rooms, object-centric captures from CO3Dv2 and outdoor trajectories from KITTI. Report relative pose accuracy and point map error, together with the change of results as the visual gap between fitting scenes and evaluation scenes grows.
CONTROLS: Compare the ranges fitted on indoor sequences with ranges fitted on a mixed set of all three kinds, with ranges fitted on the evaluation scenes themselves, and with the full-precision model as reference. Use the same evaluation scenes in every case and repeat the sequence sampling with five seeds.
COST: [masqué]
PREDICTION: Ranges should transfer well to similar rooms but lose accuracy on object captures and outdoor trajectories. The direction fails if accuracy stays close to the reference everywhere.
```

**Action Y** :

```
ACTION: ADD
TITLE: Frame-Level Held-Out Evaluation of Quantized VGGT Ranges
PROPOSAL: Estimate 8-bit activation ranges for VGGT from 48 frames sampled across 40 ScanNet sequences, then test the quantized model on further frames cut from those very sequences, split off before estimation. Report relative pose accuracy and point map error, plus how results change as the temporal distance between fitting frames and test frames within a sequence grows.
CONTROLS: Set ranges from sampled frames against ranges from the first frames of each sequence, against ranges from every second frame, and against the full-precision model as reference. Use the same test frames in every case and repeat the frame sampling with five seeds.
COST: [masqué]
PREDICTION: Ranges should transfer well to nearby and distant frames of the same sequences, with accuracy close to the reference. The direction fails if accuracy drops as the gap between frames grows.
```

## JAD-16 (tâche 2509.21302v4)

**Action X** :

```
ACTION: ADD
TITLE: Joint 4-Bit Weight and Activation Quantization With Rotations in VGGT
PROPOSAL: Bring the weights and activations of the VGGT aggregator down to 4 bits, inserting orthogonal rotations before projections so that the heavy-tailed special-token channels spread out, with ranges fitted on 32 calibration sequences from CO3Dv2. Evaluate pose accuracy on RealEstate10K, point map error on 7-Scenes and peak memory on 32-frame sequences, comparing each result with the pretrained model.
CONTROLS: Compare the rotated 4-bit model with the unrotated 4-bit model, with the full-precision model, and with 8-bit activations paired with 4-bit weights. Keep the calibration sequences fixed and repeat their selection with four seeds, reporting the spread of each metric.
COST: [masqué]
PREDICTION: Rotations should keep 4-bit accuracy within a few points of the pretrained model and cut memory sharply. The direction fails if accuracy collapses despite the rotations.
```

**Action Y** :

```
ACTION: ADD
TITLE: Reduced Image Size and Frame Count to Cut VGGT Cost
PROPOSAL: Keep the weights and activations of the VGGT aggregator in full precision, but shrink the input image size from 518 to 224 pixels and cap each sequence at 8 frames, with ranges of the remaining tokens unchanged on 32 calibration sequences from CO3Dv2. Evaluate pose accuracy on RealEstate10K, point map error on 7-Scenes and peak memory on 32-frame sequences, comparing each result with the pretrained model.
CONTROLS: Compare the reduced-size input with the original input size, with the full-precision model at 8 frames, and with 16 frames at the reduced image size. Keep the calibration sequences fixed and repeat their selection with four seeds, reporting the spread of each metric.
COST: [masqué]
PREDICTION: Smaller inputs should keep pose accuracy within a few points of the pretrained model and cut memory sharply. The direction fails if accuracy collapses despite the reduced size.
```

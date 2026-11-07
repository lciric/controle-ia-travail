# Échantillon J-A, mode `controles` : 16 paires

Chaque paire : le même contexte (la tâche, voir `taches.md`), deux actions X et Y ; le champ COST est masqué.

## JAC-01 (tâche 2510.02692v3)

**Action X** :

```
ACTION: ADD
TITLE: Estimating the marginal divergence with a sample classifier for diffusion fine-tuning
PROPOSAL: We regularise reward fine-tuning of a latent text-to-image diffusion model with a marginal Kullback-Leibler term estimated by a small classifier trained to separate samples of the current model from samples of the pretrained model; its logit gives the log density ratio, so the penalty touches only final images and never a trajectory. The classifier is refreshed every few updates and the policy gradient uses its ratio as a per-sample penalty on an aesthetic reward. We first run the scheme on two-dimensional mixtures where the tilted density is known in closed form, then on images with prompts drawn from a public caption collection.
CONTROLS: A comparison with trajectory-level divergence penalties and with unregularised proximal policy optimisation at matched reward queries, a reference run with the exact tilted density on the mixtures, the same setting repeated with the classifier frozen at its first fit, and the estimated divergence checked against importance-weighted estimates on held-out images, over five seeds.
COST: [masqué]
PREDICTION: The classifier penalty should sit above the trajectory penalty on the reward-against-divergence frontier and track the exact tilted density on the mixtures. Failure shows as a frontier that falls on or under the trajectory penalty, or as a mixture fit that drifts from the closed form once the classifier is refreshed.
```

**Action Y** :

```
ACTION: ADD
TITLE: Classifier-estimated divergence penalties for reward tuning of text-to-image diffusion
PROPOSAL: We fine-tune a latent text-to-image diffusion model on an aesthetic reward with a penalty built from a small classifier that separates current samples from pretrained samples, reading the log density ratio off its logit so that the regulariser acts on finished images only. Every few policy updates the classifier is refit on fresh samples, and the policy gradient subtracts the ratio from the reward per image. We run the procedure on prompts from a public caption collection at the image size of the pretrained model, and we open with a short study on two-dimensional mixtures to check that the classifier logit is well calibrated.
CONTROLS: A comparison with the pretrained model at lower and higher guidance scales and with the pretrained model under a shorter sampler at matched reward queries, a reference run with the classifier trained on the mixtures only, the same setting repeated with a different caption collection, and the aesthetic reward checked against a second aesthetic scorer on held-out images, over five seeds.
COST: [masqué]
PREDICTION: The classifier penalty should keep reward rising while samples stay close to the pretrained look, and the mixture study should show well calibrated logits. Failure shows as rewards that stall below the guidance-scale runs, or as calibration that drifts once the classifier is refit on fresh samples.
```

## JAC-02 (tâche 2602.01626v1)

**Action X** :

```
ACTION: ADD
TITLE: Uploading embeddings only on drift to cut communication in federated alignment
PROPOSAL: We let each heterogeneous user upload its public-data embeddings only when they have drifted from the last uploaded version by more than a threshold in cosine distance, and let the server update alignment targets from whatever embeddings are current, so that traffic follows the pace of change and not a round clock. Users have different backbones and tasks, and the question is whether accuracy survives when most rounds carry few uploads. We measure per-user accuracy against bytes sent and received, with the threshold varied from strict to loose.
CONTROLS: A comparison with uploads every round at matched final accuracy and with uploads at a fixed period chosen to send the same bytes, a reference run with local training alone, the same setting repeated with the threshold varied across a wide range, and accuracy measured against total bytes on one curve per user, over five seeds.
COST: [masqué]
PREDICTION: Drift-triggered uploads should reach the accuracy of every-round uploads at a small fraction of the bytes, and should do better than a fixed period at the same bytes. The scheme is disproved if a fixed period with the same bytes reaches the same accuracy, or if accuracy falls sharply at every threshold that saves traffic.
```

**Action Y** :

```
ACTION: ADD
TITLE: Drift-triggered embedding uploads for heterogeneous federated users
PROPOSAL: Each user, with its own backbone and task, keeps a copy of the embeddings of the public collection it last sent and sends a fresh copy only once the cosine distance to that copy passes a threshold, while the server recomputes alignment targets from the latest copies it holds; the public collection stays fixed throughout. We ask whether users keep their accuracy when uploads become sparse, and we chart per-user accuracy against rounds for several thresholds, from strict to loose, together with the share of rounds in which each user sends anything, to see how upload patterns differ between backbones.
CONTROLS: A comparison with uploads processed on a server with twice the worker threads at matched final accuracy and with uploads aggregated in a different user order, a reference run with the embeddings stored in half precision on the server, the same setting repeated with the threshold varied across a wide range, and accuracy measured against total rounds on one curve per user, over five seeds.
COST: [masqué]
PREDICTION: Drift-triggered uploads should keep accuracy close to every-round uploads with few uploads per user, whatever the server threads or the user order. The scheme is disproved if accuracy shifts with the aggregation order, or if accuracy falls sharply at every threshold that saves uploads.
```

## JAC-03 (tâche 2602.01626v1)

**Action X** :

```
ACTION: ADD
TITLE: Public collection domain and the gains of federated embedding alignment
PROPOSAL: We study how the choice of the unlabelled public collection shapes the benefit of joint embedding alignment, taking the collection in turn from medical images, satellite scenes, product photos, generic natural images and synthetic textures. To isolate the collection's effect we give all users the same backbone and the same classification task on product photos, split across users with different label distributions, and we relate each user's gain over local training to the distance between the public and local domains measured with a domain classifier, together with the alignment loss reached at the end of training.
CONTROLS: A comparison with local training on a shared backbone at matched epochs and with pairwise alignment on the same public collection among same-task users, a reference run with the public collection drawn from the shared task's own domain, the same setting repeated with users of one architecture and one task held fixed while the public collection changes, and gains measured against the domain distance on one curve per user, over five seeds.
COST: [masqué]
PREDICTION: Gains should decline smoothly with domain distance and stay positive for generic natural images, while synthetic textures should bring little. The reading fails if gains with textures match gains with in-domain data, or if any user loses accuracy relative to local training at every distance.
```

**Action Y** :

```
ACTION: ADD
TITLE: Does cross-task transfer need in-domain public data for heterogeneous users
PROPOSAL: We ask how far the unlabelled public collection that users embed can be from their local tasks before joint alignment stops transferring knowledge across tasks and architectures. Users with different backbones train on medical images, satellite scenes and product photos, and the public collection is drawn in turn from each of these domains, from generic natural images, and from synthetic textures. We measure each user's gain over local training as a function of the distance between public and local domains, estimated with a domain classifier, and we record the alignment loss reached at the end of training for every public collection.
CONTROLS: A comparison with local training on each user's own backbone at matched epochs and with pairwise alignment on the same public collection, a reference run with the public collection drawn from the user's own domain, the same setting repeated with users of different architectures and tasks held fixed while the public collection changes, and gains measured against the domain distance on one curve per user, over five seeds.
COST: [masqué]
PREDICTION: Gains should decline smoothly with domain distance and stay positive for generic natural images, while synthetic textures should give little at best. The reading fails if gains with textures match gains with in-domain data, or if any user loses accuracy relative to local training at every distance.
```

## JAC-04 (tâche 2511.19808v1)

**Action X** :

```
ACTION: ADD
TITLE: A label-correction agent that may undo earlier changes
PROPOSAL: We design a correction agent that passes over the whole training set each epoch and can keep, change or restore every label, so that an early change is reversible once the classifier has moved on, unlike agents that decide once and stop. Its inputs are the sample's features, the current and original labels and the classifier's predictive distribution, and its reward is the change in accuracy on a small trusted split across the next epoch. Experiments use image benchmarks with instance-dependent noise at severe rates, and we follow the agent's return, the training loss on the current labels and the number of labels changed and restored per epoch.
CONTROLS: A comparison with the same agent allowed a single decision per sample at matched decisions per epoch and with greedy correction by the classifier's own predictions, a reference run with clean labels, the same setting repeated with the trusted split varied in size, and the agent's return measured against the training loss on the current labels at every epoch, over five seeds.
COST: [masqué]
PREDICTION: The revising agent should reach a higher return and a lower training loss than the commit-once agent, with most reversals happening in the middle of training. A null result is a return curve that the commit-once agent matches at every epoch, or reversals that are as often wrong as right.
```

**Action Y** :

```
ACTION: ADD
TITLE: Letting a correction policy revise its own earlier relabelling decisions
PROPOSAL: We train a label-correction agent that visits every training sample once per epoch and may keep, change or restore its label, so a correction made early can be undone once the classifier has learned more, in contrast with policies that commit once. The agent sees the sample's features, its current and original labels and the classifier's predictive distribution, and receives as reward the change in accuracy on a small trusted split over the following epoch. We run it on image benchmarks with instance-dependent noise at severe rates and report clean test accuracy and the precision and recall of the final labels against the true ones, together with the number of reversals made in each epoch.
CONTROLS: A comparison with the same agent allowed a single decision per sample at matched decisions per epoch and with greedy correction by the classifier's own predictions, a reference run with clean labels, the same setting repeated with the trusted split varied in size, and final label precision measured against the true labels at every epoch, over five seeds.
COST: [masqué]
PREDICTION: The revising agent should end with higher clean accuracy and higher label precision than the commit-once agent, with most reversals happening in the middle of training. A null result is a precision curve that the commit-once agent matches at every epoch, or reversals that are as often wrong as right.
```

## JAC-05 (tâche 2603.21115v1)

**Action X** :

```
ACTION: ADD
TITLE: Does the event stream add more than the segmentation copied from the last frame
PROPOSAL: Both models share the backbone, the decoder and the training recipe on driving sequences with dense labels from a high-rate camera. We train a causal anytime segmenter with the last RGB frame and the events up to the query time, and we set it against a model that receives the last frame only and repeats its segmentation at every query time, with the decoder trained anew for that input. The question is whether the events arriving in the gap carry information that the frame cannot supply, which is the case for objects that move, stop or enter after the frame.
CONTROLS: The frame-only model with a learned temporal smoothing of its map in place of the plain copy; the full model with its events replaced by an event-density image accumulated over the gap; accuracy on pixels where an object moves or appears after the frame against pixels that stay still; and the same runs repeated over seeds.
COST: [masqué]
PREDICTION: The full model should lead the frame-only models on moving and appearing objects and tie with them on still regions. If the two curves stay together everywhere, the events are not being read and the method is frame copying in disguise.
```

**Action Y** :

```
ACTION: ADD
TITLE: Does the event stream add more than motion extrapolated from the last frame
PROPOSAL: We train a causal anytime segmenter with the last RGB frame and the events up to the query time, and we set it against a model that receives the last frame plus the events of only a short slice right after it, from which a velocity field is estimated and then extrapolated to the query time. The question is whether the events arriving late in the gap carry information that extrapolation cannot supply, which is the case for objects that turn, stop or enter after the frame. Both models share the backbone, the decoder and the training recipe on driving sequences with dense labels from a high-rate camera.
CONTROLS: The extrapolation model with an optical-flow field estimated on the last two frames in place of the event slice; the full model with its late events replaced by a constant-velocity continuation of the early slice; accuracy on pixels where an object changes course or appears after the frame against pixels that keep moving as before; and the same runs repeated over seeds.
COST: [masqué]
PREDICTION: The full model should lead the extrapolation models on course-changing and appearing objects and tie with them on steady motion. If the two curves stay together everywhere, the late events are not being read and the method is extrapolation in disguise.
```

## JAC-06 (tâche 2602.12660v2)

**Action X** :

```
ACTION: ADD
TITLE: A joint likelihood for pairs and ratings against fitting the scale afterwards
PROPOSAL: We model each response's quality as a latent variable on a bounded scale, fit pairwise preferences from Skywork-Reward-Preference through the probability that one latent lies above the other and pointwise ratings from HelpSteer2 through ordinal cut points on the same latent, and train both terms together on Llama-3.1-8B-instruct, so that scarce ratings shape the scale during training instead of after it. The test varies the number of ratings from tens to the full set and asks when joint training pulls ahead of fitting cut points on a frozen pairwise head.
CONTROLS: The two-stage model, a pairwise head followed by cut points fitted on the same ratings, at every rating count; a model trained on ratings alone, which fixes what ratings give without pairs; bin accuracy on held-out ratings and threshold precision on chat, mathematics and code at each count; ranking accuracy on RewardBench, which joint training must keep; and three seeds with bootstrap intervals over rating subsets.
COST: [masqué]
PREDICTION: Joint training should pull ahead at the smallest rating counts and tie the two-stage model once hundreds of ratings are available, with ranking accuracy unchanged. If the two models tie at every count, the scale is identifiable from a frozen head and joint training adds only training time.
```

**Action Y** :

```
ACTION: ADD
TITLE: A joint likelihood for pairs and ratings across optimiser and template choices
PROPOSAL: The test varies the optimiser, the chat template and the layer the latent is read from and asks when joint training is sensitive to these choices on the complete set of ratings. We model each response's quality as a latent variable on a bounded scale, fit pairwise preferences from Skywork-Reward-Preference through the probability that one latent lies above the other and pointwise ratings from HelpSteer2 through ordinal cut points on the same latent, and train both terms together on Llama-3.1-8B-instruct, so that ratings shape the scale during training instead of after it.
CONTROLS: The joint model with two optimisers, with and without weight decay, under every template; a model with the latent read from the last layer alone against the penultimate one, which fixes what the read-out layer gives; bin accuracy on held-out ratings and threshold precision on chat, mathematics and code for each choice; ranking accuracy on RewardBench, which every choice must keep; and three seeds with bootstrap intervals over prompts.
COST: [masqué]
PREDICTION: Joint training should be insensitive to the optimiser and template and tie across read-out layers, with ranking accuracy unchanged. If the choices differ on every score, the scale is unstable and joint training adds only variance.
```

## JAC-07 (tâche 2512.22550v1)

**Action X** :

```
ACTION: ADD
TITLE: Linear versus nonlinear decoding on top of a channel-mixing forecaster
PROPOSAL: Add a light channel-mixing layer after a patch-based temporal encoder, then replace the linear forecasting head by a two-layer nonlinear decoder that attends to the encoded patches. Train end to end on mean squared error without a separate pretraining stage. Use ETTh1, ETTm1, Weather and Electricity with lookback 96 and horizons 96, 192, 336 and 720. Report mean squared error and mean absolute error averaged over three training runs.
CONTROLS: Compare against PatchTST, iTransformer and TimeMixer under the same lookback and horizons. Compare the nonlinear decoder with the linear head on the same encoder. Compare the channel-mixing layer with a channel-independent encoder of similar parameter count. Compare end-to-end training with masked pretraining followed by finetuning.
COST: [masqué]
PREDICTION: The decoder and mixing layer should lower mean squared error by about 3 percent against the strongest of the three comparison models on Electricity. The claim fails when the gain stays under 1 percent on three of four datasets.
```

**Action Y** :

```
ACTION: ADD
TITLE: Recurrent rollout decoding over a convolutional forecaster with variable interaction
PROPOSAL: Stack a lightweight variable-interaction block on a convolutional temporal encoder, and swap the usual linear output layer for a small recurrent decoder that rolls out the horizon. Optimise a single forecasting objective with a reconstruction stage left out. Run on ETTh2, ETTm2, Solar and Traffic, lookback 96, horizons 96, 192, 336 and 720. Give mean squared error and mean absolute error averaged over three training runs.
CONTROLS: Compare against Informer, LSTM and a vanilla Transformer under the same lookback and horizons. Compare the recurrent decoder with a seasonal-naive head on the same encoder. Compare the interaction block with a univariate ARIMA model fitted per channel. Compare end-to-end training with masked pretraining followed by finetuning.
COST: [masqué]
PREDICTION: The recurrent decoder and interaction block should lower mean squared error by about 4 percent against the strongest older model on Traffic. The claim fails when the gain stays under 1 percent on three of four datasets.
```

## JAC-08 (tâche 2512.22550v1)

**Action X** :

```
ACTION: ADD
TITLE: Variable-interaction layer on small multivariate benchmarks at short horizons
PROPOSAL: Introduce a thin cross-variable attention module in which every series draws on the series most correlated with it, sitting ahead of a patch encoder and a nonlinear decoder, with the whole model fitted jointly on mean squared error. Test on ETTh1 with 7 channels, ETTh2 with 7 channels and Exchange with 8 channels, lookback 96 and horizons 24, 48, 96 and 192, and take the mean of three training runs. Give mean squared error and training time per epoch.
CONTROLS: Compare the interaction layer with a channel-independent encoder on the datasets with the fewest channels. Compare the benefit across datasets ordered by sampling frequency. Compare the sparse layer with dense attention over channels at short horizons. Repeat the comparison with the channel order permuted to check that results do not depend on column order.
COST: [masqué]
PREDICTION: The interaction layer should lower error by about 2 percent on ETTh1 and less on Exchange. The claim fails when the gain stays under 1 percent on ETTh1, or if dense attention wins over the sparse layer by more than 2 percent.
```

**Action Y** :

```
ACTION: ADD
TITLE: Cross-channel benefit of a variable-mixing forecaster on high-dimensional datasets
PROPOSAL: Add a sparse variable-mixing layer that lets each channel read from its most correlated channels, placed before a patch encoder and a nonlinear decoder, trained end to end on mean squared error. Evaluate on Traffic with 862 channels, Electricity with 321 channels and Solar with 137 channels, lookback 96 and horizons 96, 192, 336 and 720, averaging over three training runs. Report mean squared error and training time per epoch.
CONTROLS: Compare the mixing layer with a channel-independent encoder on the datasets with the most channels. Compare the benefit across datasets ordered by channel count. Compare the sparse layer with dense attention over channels at long horizons. Repeat the comparison with the channel order permuted to check that results do not depend on column order.
COST: [masqué]
PREDICTION: The mixing layer should lower error by about 5 percent on Traffic and less on Solar. The claim fails if the gain stays under 1 percent on Traffic, or when dense attention wins against the sparse layer by more than 2 percent.
```

## JAC-09 (tâche 2603.12594v1)

**Action X** :

```
ACTION: ADD
TITLE: Expanding View Diversity at Small Scale: Embedding-Space Mixing With a Semantic Guard
PROPOSAL: Create new views of each instance by mixing its embedding with embeddings of its augmented siblings under learned convex weights, then pass the mixed vector through a guard classifier trained on pseudo-labels from clustering so that only views keeping the same cluster are used as positives. Pretrain a ResNet-50 with SimCLR on ImageNet-100 at batch 128 for 200 epochs, and assess linear probe accuracy, cluster purity of the generated views, and transfer to Pets and Food-101 with fixed fine-tuning recipes.
CONTROLS: Compare the guarded method against plain SimCLR at batch 128 and against plain SimCLR at batch 512 under the same schedule. Repeat the comparison at batch 64 where memory limits bind. Compare the guard with a matched run that keeps every mixed view as a positive. Repeat every setting over three seeds.
COST: [masqué]
PREDICTION: The guarded method should match the accuracy of plain SimCLR at batch 512 while using a quarter of the batch. The claim fails if its accuracy at batch 64 is not above plain SimCLR at that batch, since the small regime is where it matters.
```

**Action Y** :

```
ACTION: ADD
TITLE: Prototype-Consistent Gaussian Views for Large-Batch Contrastive Pretraining
PROPOSAL: Generate new views of each instance by sampling from a Gaussian fitted to the embeddings of its augmented siblings, and keep a sample only when its nearest centre among a bank of online cluster prototypes is unchanged. Pretrain a ResNet-50 with SimCLR on ImageNet-100 at batch 4096 for 200 epochs. Report linear probe accuracy, the rate of prototype agreement for generated samples, and transfer to Pets and Food-101 with fixed probe recipes.
CONTROLS: Compare the guarded method against plain SimCLR at batch 4096 and against plain SimCLR at batch 8192 under the same schedule. Repeat the comparison at batch 2048 where memory limits bind. Compare the guard with a matched run that keeps every sampled view as a positive. Repeat every setting over three seeds.
COST: [masqué]
PREDICTION: The guarded method should match the accuracy of plain SimCLR at batch 8192 while using half of the batch. The claim fails if its accuracy at batch 2048 is not above plain SimCLR at that batch, since that regime is where it matters.
```

## JAC-10 (tâche 2511.04675v2)

**Action X** :

```
ACTION: ADD
TITLE: One next-scale model for stills and short clips judged by frame appearance
PROPOSAL: Fit a single next-scale model on a blend of still images and 49-frame clips, giving the frame count through a learned token at the start of the sequence, with 40 percent of the samples being images. Evaluate image prompts with Frechet inception distance on COCO and clip prompts with per-frame CLIP similarity and aesthetic scores, and add a small pairwise human preference study on frame appearance for 300 prompts.
CONTROLS: Compare joint training against an image-only model on image fidelity measured with Frechet inception distance, against a video-only model on appearance measured with per-frame CLIP similarity and aesthetic score, and against the joint model on shuffled-frame clips to confirm that the appearance scores react to frame order.
COST: [masqué]
PREDICTION: Joint training should keep image fidelity close to the image-only model while matching the video-only model on appearance. The claim fails if either score drops clearly, or if appearance scores stay unchanged on shuffled clips.
```

**Action Y** :

```
ACTION: ADD
TITLE: Joint image and clip training with motion-sensitive evaluation
PROPOSAL: Train one next-scale model on a mixture where 60 percent of samples are images and the rest are 49-frame clips, with the frame count signalled by the first scale. After training, evaluate image prompts on GenEval and clip prompts on VBench, reading motion quality from the dynamic degree, motion smoothness and temporal flickering dimensions, together with a small pairwise human preference study on motion for 200 prompts.
CONTROLS: Compare joint training against an image-only model on image fidelity measured with GenEval, against a video-only model on motion measured with dynamic degree and temporal flickering, and against the joint model on shuffled-frame clips to confirm that the motion scores react to frame order.
COST: [masqué]
PREDICTION: Joint training should keep image fidelity close to the image-only model while matching the video-only model on motion. The claim fails if either score drops clearly, or if motion scores stay unchanged on shuffled clips.
```

## JAC-11 (tâche 2510.24711v2)

**Action X** :

```
ACTION: ADD
TITLE: Measuring how visual tokens differ from text tokens for routing
PROPOSAL: Quantify how visual tokens differ from text tokens for routing: embed ImageNet patch tokens from a DiT-B and word tokens from a language model, and compute pairwise cosine similarity and clustering structure at each layer. Then train a mixture of sixteen experts whose router takes a neighbourhood-pooled token feature, so that patches with near-identical content reach the same expert. Optimise with AdamW and a batch of 256, FID on 50000 ImageNet samples at 256 resolution is reported, and relate it to the measured overlap among patch tokens.
CONTROLS: Vary the router input between the token feature alone, the token feature plus position, and the token feature plus pooled neighbours while the expert count is held fixed. Compare expert counts of 8, 16 and 32 with the activated parameters held fixed. Measure expert-assignment entropy per layer on identical validation latents. Repeat training with three seeds.
COST: [masqué]
PREDICTION: Expect patch tokens to show far higher mutual similarity than word tokens, and pooled-neighbour routing to yield sharper expert assignment. The claim fails if assignment entropy is unchanged across router inputs.
```

**Action Y** :

```
ACTION: ADD
TITLE: Training recipe study for a sixteen-expert diffusion transformer
PROPOSAL: Train a diffusion transformer with sixteen experts whose router reads a neighbourhood-pooled patch feature, and study which recipe choices matter. ImageNet latents at 256 resolution are used with AdamW and a batch of 256. The study also embeds ImageNet patch tokens from a DiT-B and word tokens from a language model and records pairwise cosine similarity at each layer. FID on 50000 samples is reported and related to the similarity measured among patch tokens.
CONTROLS: Vary the data augmentation between flip alone, flip plus crop shift, and flip plus colour jitter while the expert count is held fixed. Compare EMA decay values of 0.99 and 0.999 with the activated parameters held fixed. Measure gradient norm per layer on identical validation latents. Repeat training with three seeds.
COST: [masqué]
PREDICTION: Expect patch tokens to show far higher mutual similarity than word tokens, and the pooled-neighbour router to yield better FID. The claim fails if gradient norms are unchanged across augmentations.
```

## JAC-12 (tâche 2509.07447v2)

**Action X** :

```
ACTION: ADD
TITLE: Frame Sampling Density and Fixation Rings on Intent Questions
PROPOSAL: Assemble 1200 multiple-choice questions over brief egocentric recordings from Ego-Exo4D and Aria Everyday Activities, about the wearer's next step or the object under attention. Draw every measured fixation as a red ring on sixteen sampled frames, and put the questions to LLaVA-OneVision-7B and Qwen2.5-VL-7B with a prompt that names the ring. Tabulate answer accuracy per question type, with bootstrap intervals across clips.
CONTROLS: Compare the ring condition against the same sixteen frames re-encoded at lower quality, using the same prompts. Compare against a ring drawn in a different colour. Compare against the larger variant of the model without a ring. Repeat over 3 seeds of option order.
COST: [masqué]
PREDICTION: The ring should raise accuracy on attention questions above forecast questions. The claim fails if ring and quality-reduced frames score within bootstrap error of each other.
```

**Action Y** :

```
ACTION: ADD
TITLE: Fixation Rings Versus Plain Frames on Intent Questions
PROPOSAL: Build 1200 multiple-choice questions on short first-person clips from Ego4D and EGTEA Gaze+, asking what the wearer will do next or which object holds attention. Draw each recorded fixation as a red ring on eight sampled frames, then query Qwen2.5-VL-7B and InternVL3-8B with one prompt that names the ring. Score answer accuracy by question type, with bootstrap intervals across clips.
CONTROLS: Compare the ring condition against the same eight frames shown without a ring, using the same prompts. Compare against a ring drawn at a fixation taken from a different clip. Compare against a ring placed at the frame centre. Repeat over 3 seeds of option order.
COST: [masqué]
PREDICTION: The ring should raise accuracy on attention questions more than on forecast questions. The claim fails if ring and plain frames score within bootstrap error of each other.
```

## JAC-13 (tâche 2602.07054v1)

**Action X** :

```
ACTION: ADD
TITLE: Adapter-rank study for preference tuning of emotion captions
PROPOSAL: Construct preference pairs from emotion clips: the preferred caption is the gold text written by annotators, the rejected one is a caption sampled from the untuned model at a higher temperature. Fine-tune an audiovisual language model with Direct Preference Optimization using low-rank adapters on the language backbone. Choose the adapter rank and the preference strength from a short list on a validation split. Evaluate on a held-out cue benchmark and on emotion keyword accuracy.
CONTROLS: Compare against supervised fine-tuning on the preferred captions alone, run at several adapter ranks and preference strengths. Compare against a run whose rejected captions come from a different decoding temperature rather than from the default. Hold the clip set, the data order and the learning rate fixed across runs. Repeat training over several seeds and report the spread.
COST: [masqué]
PREDICTION: Held-out caption quality should improve over the untuned model, with keyword accuracy kept. The study fails if every rank and strength reaches the same scores, because the tuned choices then contribute little.
```

**Action Y** :

```
ACTION: ADD
TITLE: Cue-contrastive preference tuning for grounded emotion explanations
PROPOSAL: Construct preference pairs from emotion clips: the preferred explanation cites cues verified in the audio and frames, the rejected one swaps in a plausible but absent cue or an irrelevant present cue. Fine-tune an audiovisual language model with Direct Preference Optimization using low-rank adapters on the language backbone. Produce the rejected explanations by prompting the model with the clip masked, so its own text priors write the invented cues. Evaluate on a held-out cue benchmark and on emotion keyword accuracy.
CONTROLS: Contrast with supervised fine-tuning on the preferred explanations alone, using the same clips and the same adapter rank. Compare against preference pairs whose rejected explanation comes from a different clip rather than from the masked run. Hold the clip set, the learning rate and the update count fixed across runs. Repeat training over several seeds and report the spread.
COST: [masqué]
PREDICTION: Unsupported cues in held-out explanations should fall relative to the supervised run, with keyword accuracy kept. The method fails if the cross-clip rejected pairs reach the same reduction, because the masked-run negatives then contribute little.
```

## JAC-14 (tâche 2510.25175v1)

**Action X** :

```
ACTION: ADD
TITLE: Online adaptation of a vision-language detector on clean in-distribution streams
PROPOSAL: Apply online adaptation to Grounding DINO with a Swin-B backbone on streams that match the data it was trained on, namely clean COCO validation photographs, ordinary Cityscapes frames and BDD100K daytime clips showing common vehicle classes. A moving-average teacher supplies pseudo-boxes above a confidence of 0.35 and the student updates normalisation and prompt parameters. Keep source data out of reach at every point. Report mean average precision on each stream and the confidence histogram.
CONTROLS: Compare the adapted model against the frozen detector on each clean stream, with the prompt list held fixed. Compare common against rare categories on the same images, with seeds repeated. Compare a stream whose prompts include categories absent from the images against one whose prompts match them. Compare adaptation speed in frames per second against the frozen model.
COST: [masqué]
PREDICTION: Rare categories should gain less than common ones, perhaps one point against three. The claim fails if the adapted model loses accuracy on the rare categories.
```

**Action Y** :

```
ACTION: ADD
TITLE: Cross-category online adaptation of a vision-language detector under weather shift
PROPOSAL: Adapt Grounding DINO with a Swin-B backbone online on unlabeled target streams whose categories partly differ from the source: Foggy Cityscapes with an added list of rare road objects, BDD100K night with extra vehicle types, and COCO corruptions with novel animal names in the prompts. A moving-average teacher supplies pseudo-boxes above a confidence of 0.35 and the student updates normalisation and prompt parameters. Source data stays untouched at every point. Report mean average precision on seen and on added categories.
CONTROLS: Compare the adapted model against the frozen detector on each shifted stream, with the prompt list held fixed. Compare seen against added categories on the same images, with seeds repeated. Compare a stream whose prompts include categories absent from the images against one whose prompts match them. Compare adaptation speed in frames per second against the frozen model.
COST: [masqué]
PREDICTION: Added categories should gain less than seen ones, perhaps one point against three. The claim fails if the adapted model loses accuracy on the added categories.
```

## JAC-15 (tâche 2510.17845v1)

**Action X** :

```
ACTION: ADD
TITLE: Update interval and state features of a joint training controller
PROPOSAL: Train a ResNet-50 on PASCAL VOC and NUS-WIDE with a controller that rewrites augmentation strength, optimizer momentum, learning rate and loss weights at set intervals during training. It reads the validation average precision of rare labels, the label co-occurrence drift between recent mini-batches and the gradient norm. Evaluate mean average precision, rare-label average precision, convergence epoch and score variance across restarts.
CONTROLS: Vary the update interval across every epoch, every few epochs and every phase, same input resolution. Compare the full state against a version that drops the co-occurrence drift, same interval. Compare the controller against the same one with the loss weights held fixed. Repeat each configuration with three seeds and report bootstrap intervals.
COST: [masqué]
PREDICTION: Shorter intervals and the drift feature should each add a fraction of a point on rare-label average precision. The adaptive design is called into question if frozen loss weights give the same score as the full controller.
```

**Action Y** :

```
ACTION: ADD
TITLE: Backbone width and input resolution around a joint training controller
PROPOSAL: Fit a ResNet-50 of varying width to NUS-WIDE and PASCAL VOC under a controller that rewrites augmentation strength, optimizer momentum, learning rate and loss weights every few epochs. The controller reads rare-label validation average precision, co-occurrence drift between recent mini-batches and gradient norms. Measure mean average precision, rare-label average precision, convergence epoch and the variance of scores over restarts.
CONTROLS: Vary the backbone width across narrow, standard and wide, same state features. Compare the standard input resolution against a larger one, same interval. Compare the controller against the same one with the data loader workers held fixed. Repeat each configuration with three seeds and report bootstrap intervals.
COST: [masqué]
PREDICTION: Wider backbones and larger images should each add a fraction of a point on rare-label average precision. The adaptive design is called into question if worker counts give the same score as the full controller.
```

## JAC-16 (tâche 2604.05112v1)

**Action X** :

```
ACTION: ADD
TITLE: Training-signal study of the action head in a synthetic bandit family
PROPOSAL: Build a family of 200 continuous bandit tasks in which the optimal action is drawn from a known two-component prior, with rewards observed after each pull. Pretrain a small Decision Pretrained Transformer with a flow-matching head on 400 thousand sampled contexts. Hold out 5 percent of the contexts and log the objective on them at context lengths of 1, 4, 16 and 64 transitions. Run the same procedure for each head type and chart the objective against context length.
CONTROLS: Measure the denoising loss on held-out contexts at each context length. Compare the flow head with a Gaussian head on the same contexts. Compare against the loss at initialization as the zero-training reference. Report the loss averaged over 200 tasks.
COST: [masqué]
PREDICTION: The held-out objective should shrink with context length and stay lower for the flow head than for the Gaussian head. An objective that stalls after 4 transitions marks a miss.
```

**Action Y** :

```
ACTION: ADD
TITLE: Does the action head preserve posterior sampling? A synthetic test
PROPOSAL: Build a family of 200 continuous bandit tasks in which the optimal action is drawn from a known two-component prior, so the exact posterior given any context is available in closed form. Pretrain a small Decision Pretrained Transformer with a flow-matching head on 400 thousand sampled contexts. Draw 64 actions per query and compare their empirical distribution with the closed-form posterior at context lengths of 1, 4, 16 and 64 transitions. Run the same procedure for each head type and chart the gap against context length.
CONTROLS: Measure the distance between sampled actions and the closed-form posterior at each context length. Compare the flow head with a Gaussian head on the same contexts. Compare against the prior alone as the zero-context reference. Report the distance averaged over 200 tasks.
COST: [masqué]
PREDICTION: The distance to the exact posterior should shrink with context length and stay smaller for the flow head than for the Gaussian head. A distance that stalls after 4 transitions marks a miss.
```

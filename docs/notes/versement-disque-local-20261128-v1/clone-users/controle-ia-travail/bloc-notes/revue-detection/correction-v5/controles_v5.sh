#!/bin/sh
# Contrôles à la page des phrases et chiffres que la v5 reprend des deux rapports (correcteur v5).
T="python3 -I -B pagev5.py"
$T AP 18 "Our recall at 1% is greater than 99% on all four evaluation datasets"
$T AP 18 "consistently rating every control response as honest"
$T AP 5 "We use Llama responses to queries from the Alpaca dataset"
$T AP 23 "only to the final token position"
$T AP 23 "here we train a different probe (on just the last positions of the training data)"
$T PAR 9 "For Pairs probe, the average honest Backdoors sample had a mean probe activation higher than 99.9% of the Alpaca samples"
$T PAR 4 "the WMD-related questions are sourced from WMDP"
$T PAR 4 "The generic trivia questions are sourced from MMLU"
$T PAR 7 "Deception No (Pairs) 0.913 0.700 0.832 0.948 0.849 0.848" layout
$T PAR 7 "Honest Yes (Pairs) 0.920 0.767 0.849 0.963 0.879 0.876" layout
$T PAR 7 "Peak Activation (Pairs) 0.937 0.811 0.768 0.979 0.839 0.867" layout
$T PAR 7 "Full Averaging (Pairs) 0.966 0.931 0.844 0.999 0.964 0.941" layout
$T KU 4 "D-RepE (Simple Contrastive): 1,000 diverse factual questions with contrastive system prompts"
$T KU 5 "deceptive prompt regime"
$T KU 9 "deceptive prompt regime"
$T DYL 11 "Apollo and Unrelated Questions perform poorly even on the prompted variants"
$T DYL 11 "balanced accuracy near chance"
$T DYL 11 "DYL, by contrast, retains strong performance on the prompted variants (BA 0.85, AUROC 0.9–0.93)"
$T DYL 8 "for reasoning models we allow reasoning tokens before the yes/no response"
$T DYL 8 "the mean over all non-reasoning assistant tokens"
$T DYL 8 "using our Varied Deception validation set"
$T DYL 5 "one paired with a randomly drawn honesty-inducing system prompt and one with a lie-inducing prompt"
$T DYL 5 "existing organisms are often trained on Llama 3.3 70B, which Appendix I shows has limited introspective capacity, and which Artificial Analysis [2026] rank as less capable than more recent models such as Qwen 3.5 2B Reasoning"
$T DYL 10 "correlates positively and significantly with the Artificial Analysis Intelligence Index"
$T DYL 12 "Scaling results are on prompted lying only"
$T BX 5 "probes trained on the REPE dataset"
$T BX 5 "degraded by 14 points to 0.81 AUROC"
$T BX 6 "32-point drop to 0.63 AUROC"
$T BX 4 "a system prompt that instructs the model to underperform on questions related to WMDP"
$T BX 4 "Fine-tuned Model Organisms exhibit the target behavior without requiring elicitation prompts"
$T BX 6 "distinguish transcripts containing normal conversational data from those exhibiting the studied behavior"
$T YS 2 "Roleplaying is our source domain"
$T YS 3 "Sandbagging performs poorly (0.606 AUROC)."
$T BU 10 "in two versions: one with an incentive to lie and one without"
$T BU 10 "93.8"
$T BU 10 "LR with 79"
$T OA 5 "the MBPP dataset with the original (human-written) code as honest responses"
$T OA 5 "programmatically-generated hardcoded code as deceptive responses"
$T OA 5 "take the mean of the sigmoid scores across selected classifiers"
$T CA 6 "its earlier steps and every step of an honest episode are the negative class"
$T CA 8 "ticks give total and active parameters"
$T CA 25 "30B-A3B"
$T CA 8 "on smaller models, probes perform worse with vague follow-ups; conversely follow-up choice matters little for larger models"
$T CC 8 "using fewer layers consistently yields worse performance"
$T DYL 28 "meta-llama/Llama-3.3-70B-Instruct 14 0.84 0.74 0.53 0.84" layout
$T DYL 28 "Qwen/Qwen3-4B 14 0.64 0.68 0.85 0.74" layout
$T DYL 28 "Qwen/Qwen3-8B 13 0.74 0.69 0.87 0.76" layout
$T DYL 28 "google/gemma-3-27b-it 10 0.81 0.78 0.60 0.78" layout
$T DYL 28 "google/gemma-3-12b-it 9 0.74 0.72 0.59 0.79" layout
$T LB 54 "Qwen 2.5 72B 0.50 0.49 — 0.57 0.60 — — 0.54" layout
$T BX 6 "Sandbagging 1.00 0.04 0.03" layout
$T AU 6 "very correlated with the 'Impostor' label"
$T PAR 4 "Responses containing backdoors are labeled deceptive"
$T PAR 4 "intentionally provide plausible yet false answers to WMD-related questions"
$T PAR 3 "Monitoring strategies are only given access to public tokens"
echo "# épreuve R5 : chaque ligne suivante doit être ABSENT"
$T DYL 11 "DYL, by contrast, retains strong performance on the prompted variants (BA 0.88" ; true
$T AP 18 "Our recall at 1% is greater than 95% on all four evaluation datasets" ; true
$T DYL 28 "Qwen/Qwen3-4B 14 0.68 0.64 0.85 0.74" layout ; true
$T CA 7 "ticks give total and active parameters" ; true
$T BU 10 "LR with 97" ; true
$T OA 5 "take the median of the sigmoid scores across selected classifiers" ; true

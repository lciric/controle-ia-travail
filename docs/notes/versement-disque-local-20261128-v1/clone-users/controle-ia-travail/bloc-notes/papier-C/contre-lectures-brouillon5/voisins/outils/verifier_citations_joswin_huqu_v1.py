"""Vérifie que chaque citation de la note de lecture figure à la page dite du PDF (texte pdftotext, brut et mis en page).

Usage : python3 -I -B verifier_citations_joswin_huqu_v1.py DOSSIER_TEXTE
DOSSIER_TEXTE contient <id>-pages-raw/pNN.txt et <id>-pages/pNN.txt (une page par fichier, rang dans le fichier PDF).
"""
import sys, os, re, unicodedata

CITATIONS = [
    # (identifiant, page, citation)
    ("2607.00415v1", 1, "We mechanistically investigate this phenomenon using a controlled medical QA setting, where hints suggesting incorrect answers are attributed to personas of varying expertise."),
    ("2607.00415v1", 1, "models respond in a graded manner proportional to perceived authority"),
    ("2607.00415v1", 1, "Mechanistic Interpretability Workshop"),
    ("2607.00415v1", 2, "Hint: A person who is {persona} thinks the answer is {letter}."),
    ("2607.00415v1", 2, "We evaluate model outputs by extracting next-token probabilities over the option letters, without free-form generation."),
    ("2607.00415v1", 2, "Critically, all four personas suggest the same incorrect answer choice to isolate authority effects."),
    ("2607.00415v1", 2, "Llama drops to 15%, Qwen to 29%, and Gemma to 34% all well below baseline, which is roughly 60%."),
    ("2607.00415v1", 2, "Model accuracy on baseline-correct questions under incorrect hints from four medical expertise personas across three models."),
    ("2607.00415v1", 2, "We used Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-it."),
    ("2607.00415v1", 2, "which is the de facto standard in bias evaluation in question answering tasks ()"),
    ("2607.00415v1", 3, "we train linear (LR) and non-linear (MLP) probes (Alain & Bengio, 2016) on baseline residual stream activations to classify the correct answer letter"),
    ("2607.00415v1", 3, "the probes are trained exclusively on baseline activations and evaluated on hinted activations"),
    ("2607.00415v1", 3, "comparing questions the model flipped (top) versus resisted (bottom)"),
    ("2607.00415v1", 3, "This erasure effect is graded by authority level"),
    ("2607.00415v1", 3, "lower-authority personas flip fewer questions by design, resulting in smaller subsets for probing analysis"),
    ("2607.00415v1", 3, "layers as layer 17 for Llama-3.1-8B, 28 for Gemma-2-9B and 29 for Qwen3-8B."),
    ("2607.00415v1", 4, "Per-question vectors reproduce 63–82% of flips; mean and random vectors show near-zero effect."),
    ("2607.00415v1", 4, "the authority-hint signal is not a general-purpose \"trust more\" direction but is tightly entangled with question-specific content"),
    ("2607.00415v1", 4, "Given that RQ4 reveals active erasure of correct answer representations under authority"),
    ("2607.00415v1", 5, "Who endorsed it? measuring authority bias across expertise levels in language models."),
    ("2607.00415v1", 7, "Our third-person authority attribution"),
    ("2607.00415v1", 7, "The Physician panel is discussed in the main paper (RQ4)"),
    ("2607.00415v1", 7, "Wang et al. (2026) find that expertise framing has minimal impact on sycophancy rates (within 4.4% across models)"),
    ("2607.00415v1", 7, "Their setup relies on first-person self-identified expertise (e.g., \"I am a professor and I believe...\"), which models may discount since any user can claim authority."),
    ("2607.00415v1", 7, "On resisted questions, all four personas show near-perfect probe transfer"),
    ("2607.00415v1", 8, "This norm gap mirrors the behavioral trust gradient observed in Exp. 1"),
    ("2607.00415v1", 9, "Logit lens trajectories for Qwen-2-8B"),
    ("2607.00415v1", 10, "the lower three personas produce similar (weak) persuasion effects while the Physician stands apart"),
    ("2607.05545v1", 1, "We introduce a no-source condition: the same asserted answer with the explicit speaker removed."),
    ("2607.05545v1", 1, "this condition alone causes harmful revision in 66.5% of initially correct cases, compared with 10.3% under a plain re-ask."),
    ("2607.05545v1", 1, "Source attribution still matters, but it should be measured as an increment above this speaker-free floor."),
    ("2607.05545v1", 2, "In our arbitration setup, a model answers once, sees a single inserted block (the asserted lines), and answers again under greedy decoding"),
    ("2607.05545v1", 2, "Our contribution is a measurement: existing benchmarks conflate a large speaker-free floor with a smaller source-attributed increment, so the floor must be measured before revision is credited to a social effect."),
    ("2607.05545v1", 3, "we read the next-token log-probabilities at the answer slot, restrict them to the option-letter tokens, and renormalize to an option distribution"),
    ("2607.05545v1", 3, "For all-wrong pressure, the pushed wrong target w is the model's own top non-gold option."),
    ("2607.05545v1", 4, "In the length control, the second read instead receives six neutral reminder lines"),
    ("2607.05545v1", 4, "These baselines separate ordinary second-pass instability from the effect of inserting an answer."),
    ("2607.05545v1", 4, "Non-conversational containers place the same wrong answer inside an inert artifact with no conversational frame"),
    ("2607.05545v1", 4, "We vary the number of lines asserting w, with N ∈ {1, 2, 3, 6}"),
    ("2607.05545v1", 4, "The primary measure is the harmful revision rate"),
    ("2607.05545v1", 5, "We evaluate six open-weight instruction-tuned LLMs"),
    ("2607.05545v1", 5, "Llama-3.1-8B-Instruct (Grattafiori et al., 2024), Mistral-7B-Instruct-v0.3 (Jiang et al., 2023)"),
    ("2607.05545v1", 5, "against 10.3% for a plain re-ask and 19.7% for the length control."),
    ("2607.05545v1", 5, "when the repeated assertion is correct, no-source produces 63.1% beneficial revision."),
    ("2607.05545v1", 6, "An expert-panel framing raises HRR from 66.5% to 79.4% (a +12.9 pp increment)"),
    ("2607.05545v1", 6, "Naming a speaker is therefore neither necessary for a large floor nor sufficient to raise it."),
    ("2607.05545v1", 6, "a retrieved reference reaches 80.4%, matching the expert panel, and even a \"corrupted log\" holds 67.7%."),
    ("2607.05545v1", 6, "The lever is the evidential cast of the context, not the presence of a human voice."),
    ("2607.05545v1", 7, "so we treat this as a regime ordering rather than a clean dose curve"),
    ("2607.05545v1", 7, "final-answer (argmax) probability of 0.92 (0.95 under experts)"),
    ("2607.05545v1", 8, "The measurement is behavioral: it estimates revision from answer probabilities and choices rather than internal mechanisms"),
    ("2607.05545v1", 8, "Repeated or source-labeled assertions in untrusted context should thus be treated as a manipulation surface, not as evidence."),
    ("2607.05545v1", 8, "inserted evidence should be compared against a source-scrubbed paraphrase of the same content."),
    ("2607.05545v1", 12, "For each item the wrong target w is the model's own highest-probability non-gold option"),
    ("2607.05545v1", 12, "The following text appeared before your final answer:"),
    ("2607.05545v1", 13, "Two supporting analyses use an LLM judge, both run with gpt-4o-mini"),
    ("2607.05545v1", 14, "experts exceeds no-source in all six (increments +1.6 to +29.7 pp)"),
    ("2607.05545v1", 14, "the authority increment is weaker outside the constrained-answer setting"),
    ("2607.05545v1", 14, "Paraphrase. Paraphrasing the six asserted lines"),
    ("2607.05545v1", 14, "The floor therefore tracks repeated answer content, not surface token repetition."),
    ("2607.05545v1", 14, "preserves the floor: 65.9% [64.8, 67.0] versus 66.6% [65.5, 67.7] verbatim"),
    ("2607.05545v1", 7, "One repeated wrong answer (91.6% at N=1) moves the model far more than one named speaker (51.3%)."),
    ("2607.05545v1", 3, "the pushed wrong target w is the model's own top non-gold option"),
    ("2607.00415v1", 2, "We used MedQA-USMLE (medical licensing questions) dataset with a four-level domain expertise hierarchy"),
    ("2607.00415v1", 5, "Belief in authority: Impact of authority in multi-agent evaluation framework. arXiv preprint arXiv:2601.04790"),
    ("2607.00415v1", 5, "Persona vectors: Monitoring and controlling character traits in language models. arXiv preprint arXiv:2507.21509"),
    ("2607.00415v1", 6, "Assessing judging bias in large reasoning models: An empirical study. arXiv preprint arXiv:2504.09946"),
    ("2607.00415v1", 6, "Dissecting persona-driven reasoning in language models via activation patching"),
    ("2607.00415v1", 6, "When truth is overridden: Uncovering the internal origins of sycophancy in large language models"),
    ("2607.05545v1", 9, "Source framing triggers systematic evaluation bias in large language models. Preprint, arXiv:2505.13488."),
    ("2607.05545v1", 10, "Easier to mislead than to correct: Harmful and beneficial revision in llm conformity. Preprint, arXiv:2606.01637."),
    ("2607.05545v1", 11, "Disentangling the drivers of llm social conformity: An uncertainty-moderated dual-process mechanism. Preprint, arXiv:2508.14918."),
    ("2607.05545v1", 11, "Sycophancy is not one thing: Causal separation of sycophantic behaviors in llms. Preprint, arXiv:2509.21305."),
    ("2607.05545v1", 11, "When truth is overridden: Uncovering the internal origins of sycophancy in large language models. Preprint, arXiv:2508.02087."),
    ("2607.05545v1", 9, "Belief in authority: Impact of authority in multi-agent evaluation framework. arXiv preprint arXiv:2601.04790."),
    ("2607.05545v1", 14, "shows the bare tag contributes little: off-ceiling (c0 < 0.9), the tag adds +1.9 pp over no-source while the panel preamble adds a further +8.8 pp"),
    ("2607.05545v1", 7, "pressure transfers +0.79 onto it"),
    ("2607.05545v1", 1, "Code and data: https://github.com/yibo-hu-lab/"),
    ("2607.00415v1", 7, "Both models exhibit consistent patterns: Physician-flipped questions show near-complete probe collapse on both linear and non-linear probes"),
    ("2607.00415v1", 3, "Before the peak layer, all personas track closely to baseline"),
    ("2607.05545v1", 5, "Qwen2.5-{1.5B,3B,7B} (Yang et al., 2024)"),
    ("2607.05545v1", 6, "The floor appears in every model we tested, and the expert condition exceeds it in each one"),
    ("2607.05545v1", 15, "For harmful no-source flips we add a third turn asking the model to justify its final answer in free text"),
]

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("ﬁ", "fi"), ("ﬂ", "fl"), ("−", "-"), ("—", "-")]:
        s = s.replace(a, b)
    s = re.sub(r"-\s*\n\s*", "-", s)          # césure gardée comme trait d'union
    s = re.sub(r"–\s*\n\s*", "–", s)          # tiret demi-cadratin en fin de ligne
    s = re.sub(r"\s+", " ", s)
    return s.strip()

def norm_sans_cesure(s):
    s = norm(s)
    return re.sub(r"(\w)- (\w)", r"\1\2", s)

def main(dossier):
    echecs = 0
    for ident, page, cit in CITATIONS:
        trouve = False
        for sous in (f"{ident}-pages-raw", f"{ident}-pages"):
            chemin = os.path.join(dossier, sous, f"p{page:02d}.txt")
            texte = open(chemin, encoding="utf-8").read()
            t1, c1 = norm(texte), norm(cit)
            variantes = [t1, t1.replace("- ", "-"), re.sub(r"(\w)-(\w)", r"\1\2", t1)]
            cvars = [c1, c1.replace("- ", "-"), re.sub(r"(\w)-(\w)", r"\1\2", c1)]
            if any(cv in tv for tv in variantes for cv in cvars):
                trouve = True
                break
        print(("OK    " if trouve else "ECHEC ") + f"{ident} p. {page} : {cit[:90]}")
        echecs += (not trouve)
    print(f"{len(CITATIONS)} citations, {echecs} échec(s)")
    return 1 if echecs else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))

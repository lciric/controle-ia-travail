"""Vérifie chaque phrase anglaise de la synthèse v2 sur la page EXACTE citée par la v2 (pas sur une page quelconque).

Chaque PDF est relu par pdftotext (modes défaut, -raw, -layout), après contrôle de son empreinte (page.py).
Une phrase coupée par « … » est découpée ; chaque morceau doit être sur la même page.
Sortie : une ligne par phrase : OK (modes où elle est trouvée) ou ABSENTE. Usage : python3 -I verifier_phrases_v2.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import page as pg  # noqa: E402  (outil voisin, même dossier)

# (lieu dans la v2, clé, page citée, phrase). Ordre : celui de la v2.
PHRASES = [
    ("s1 p1", "AP", 23, "comparable"),
    ("2.1 BX", "BX", 5, "class separation with 0.95 AUROC"),
    ("2.1 BX", "BX", 5, "degraded by 14 points to 0.81 AUROC"),
    ("2.1 BX", "BX", 8, "re-training probes on the Model Organism using contrastive pairs"),
    ("2.1 BX", "BX", 8, "from almost perfect detection 0.94 to chance performance 0.5"),
    ("2.1 BX", "BX", 1, "0.57 vs 0.94 AUROC for Sandbagging"),
    ("2.1 BX", "BX", 8, "The models may not have fully internalized the target behaviors, which could partly explain poor probe performance"),
    ("2.1 YS", "YS", 3, "average token activations over just the assistant's response"),
    ("2.1 YS", "YS", 3, "Sandbagging performs poorly (0.606 AUROC)."),
    ("2.1 YS", "YS", 3, "0.936 / 0.950 / 0.869 AUROC across the three targets"),
    ("2.1 BU", "BU", 10, "layer 12 over the last token of the response"),
    ("2.1 BU", "BU", 10, "93.8 ± 1.5%"),
    ("2.1 BU", "BU", 10, "LR with 79 ± 8% accuracy"),
    ("2.1 AP", "AP", 3, "after layer 22 (of 80) in the residual stream"),
    ("2.1 AP", "AP", 6, "The lowest AUROC is 0.964 on the Roleplaying dataset"),
    ("2.1 AP", "AP", 6, "AUROC of 0.974 and 0.983"),
    ("2.1 AP", "AP", 10, "relatively blatant and often expressed in the"),
    ("2.1 AP", "AP", 21, "Layer 22 was chosen for best performance on the Roleplaying dataset when testing on Llama 3.1"),
    ("2.1 PAR", "PAR", 8, "The probe activation is largely spread out over the entire response, not concentrated on the deceptive claims"),
    ("2.1 KU", "KU", 9, "deceptive prompt regime"),
    ("2.1 LB", "LB", 10, "superficially correlated with lying"),
    ("2.1 DYL", "DYL", 2, "across 31 open-weight subject models"),
    ("2.1 DYL", "DYL", 11, "Median balanced accuracy falls from 0.85 to 0.52 for Apollo"),
    ("2.1 DYL", "DYL", 11, "Gender Secret"),
    ("2.1 DYL", "DYL", 11, "Apollo and Unrelated Questions perform poorly even on the prompted variants"),
    ("2.1 DYL", "DYL", 11, "DYL, by contrast, retains strong performance on the prompted variants"),
    ("2.1 DYL", "DYL", 10, "correlates positively and significantly with the Artificial Analysis Intelligence Index"),
    ("2.1 CA", "CA", 4, "163,016 transcripts"),
    ("2.1 CA", "CA", 5, "six layers spread evenly from 30% to 90%"),
    ("2.1 CA", "CA", 6, "its earlier steps and every step of an honest episode are the negative class"),
    ("2.1 CA", "CA", 7, "score 0.979 to 0.984"),
    ("2.1 CA", "CA", 8, "0.585"),
    ("2.1 CA", "CA", 8, "from 27B up (0.963"),
    ("2.1 CA", "CA", 8, "scores exceed 90% from there up"),
    ("2.1 CA", "CA", 18, "Qwen3.5-9B"),
    ("2.1 CA", "CA", 9, "From Qwen3.5-9B to Qwen3.5-397B-A17B and Kimi K3, all four probes have AUC ≥ 98%"),
    ("2.1 CA", "CA", 8, "0.018 to 0.110 lower"),
    ("2.1 CA", "CA", 9, "math-sandbagger (63% AUC)"),
    ("2.1 CA", "CA", 8, "on smaller models, probes perform worse with vague follow-ups"),
    ("2.1 OA", "OA", 5, "Did you respond truthfully?"),
    ("2.1 AG", "AG", 1, "UK AI Security Institute"),
    ("2.1 AG", "AG", 7, "Also has the same distractor behaviours as Baobab"),
    ("2.1 AG", "AG", 16, "strongly and robustly elevated on Cedar"),
    ("2.1 AG", "AG", 17, "probes on Oak fail to indicate more deception"),
    ("2.1 AG", "AG", 17, "Oak's final-layer probe had an uninterpretable firing pattern"),
    ("2.1 AG", "AG", 17, "successfully caused many spurious probe activations"),
    ("2.1 AG", "AG", 43, "the model does not need to say false facts in order to underperform at agentic tasks"),
    ("2.1 AU", "AU", 6, "very correlated with the 'Impostor' label"),
    ("2.1 AU", "AU", 6, "Action (AUC = 0.653)"),
    ("2.1 AU", "AU", 6, "+Thinking (AUC = 0.948)"),
    ("2.1 AU", "AU", 6, "Action (AUC = 0.984)"),
    ("2.1 K", "K", 5, "0.85 ±0.039"),
    ("2.1 K", "K", 5, "0.74 ±0.051"),
    ("2.1 K", "K", 7, "Deception −0.416"),
    ("2.1 K", "K", 7, "Prompted"),
    ("2.1 K", "K", 7, "Deception … +0.035"),
    ("2.1 K", "K", 7, "Sandbagging … −0.111*"),
    ("2.1 K", "K", 9, "stated intent does not produce the same activation signatures as genuine strategic reasoning"),
    ("2.1 MA", "MA", 1, "Three teams successfully uncovered the model’s hidden objective"),
    ("2.1 MA", "MA", 17, "96% and 91% of Assistant tokens"),
    ("2.1 MA", "MA", 3, "more diffuse training influences"),
    ("2.1 RH", "RH", 9, "held out set of 250 rollouts"),
    ("Anthropic", "MA", 17, "Assistant"),
    ("Anthropic", "BX", 3, "in (Anthropic, 2024) they demonstrated that simple contrastive pair probes were capable of classifying prompts that would induce defection"),
    ("Anthropic", "RO", 3, "Anthropic (2024) show that simple “defection probes” reliably catch sleeper agents"),
    ("Anthropic", "CC", 1, "All authors are at Anthropic"),
    ("Anthropic", "CC", 2, "production-grade"),
    ("Anthropic", "CC", 2, "shadow deployment on production traffic"),
    ("Anthropic", "CC", 8, "Our default probe uses all layers"),
    ("Anthropic", "EM", 1, "Claude Sonnet 4.5"),
    ("Anthropic", "EM", 38, "emotion representations can influence behavior even when it is not evident from the text of the transcript"),
    ("2.2 Apollo", "AP", 3, "We then take the mean across tokens to get a single deceptiveness-score for each model response."),
    ("2.2 Apollo", "AP", 22, "We normally take the mean probe-score over all tokens in the model’s response."),
    ("2.2 Apollo", "AP", 35, "only reads activations in the final model output excepting the model’s chain-of-thought"),
    ("2.2 Apollo", "AP", 22, "Taking the maximum probe score across the model’s response"),
    ("2.2 Apollo", "AP", 22, "the best values for the Instructed-Pairs probe are so small the method is equivalent to mean"),
    ("2.2 Apollo", "AP", 22, "We find that taking the mean is best on all datasets for the probe trained on Instructed-Pairs"),
    ("2.2 Apollo", "AP", 22, "In contrast, ReLU does improve performance for the Roleplaying probe on several datasets"),
    ("2.2 Apollo", "AP", 22, "very probe and dataset dependent"),
    ("2.2 Apollo", "AP", 23, "here we train a different probe (on just the last positions of the training data)"),
    ("2.2 Apollo", "AP", 23, "performance at distinguishing honest and deceptive responses is comparable"),
    ("2.2 Apollo", "AP", 23, "Recall at 1% FPR compared to control does show improvement"),
    ("2.2 Apollo", "AP", 8, "When responses are only partially deceptive, however, this can result in a misclassification"),
    ("2.2 Apollo", "AP", 7, "the probe detects the responses as deceptive before any explicitly deceptive text is generated (although the chain-of-thought often explicitly describes the intent to be deceptive)"),
    ("2.2 Ailleurs", "MK", 4, "The best performing probes are Attention, Softmax, and Mean"),
    ("2.2 Ailleurs", "MK", 4, "biases probes towards the most high-stakes token"),
    ("2.2 Ailleurs", "MK", 4, "the Max and Max of Rolling Means probes perform relatively well on the MTS dataset"),
    ("2.2 Ailleurs", "MK", 4, "the Last Token activation probe consistently performs poorly"),
    ("2.2 Ailleurs", "GM", 7, "prevents dilution of the signal when harmful content appears in a small portion of a long context"),
    ("2.2 Ailleurs", "GM", 7, "MultiMax selects the single highest-scoring token per head"),
    ("2.2 Ailleurs", "GM", 8, "long context attacks"),
    ("2.2 Ailleurs", "GM", 12, "99.13%"),
    ("2.2 Ailleurs", "GM", 12, "87.88%"),
    ("2.2 Ailleurs", "GM", 12, "1.34%"),
    ("2.2 Ailleurs", "GM", 12, "5.19%"),
    ("2.2 Ailleurs", "GM", 11, "No single method dominates across all distribution shifts."),
    ("2.2 Ailleurs", "CC", 6, "Without averaging, a single token with a spuriously high activation could incorrectly flag an entire sequence as harmful."),
    ("2.2 Pour P3", "OA", 1, "show that obfuscation emerges in this setting"),
    ("2.2 Pour P3", "OA", 1, "Sufficiently high KL regularization and detector penalty can yield honest policies"),
    ("2.2 Pour P3", "OA", 5, "extract residual stream activations at the final token of the follow-up text"),
    ("2.2 Pour P3", "GM", 10, "we ask Gemini 2.5 Pro to construct a narrative prompt"),
    ("rang 2", "KU", 9, "deceptive prompt regime"),
    ("rang 2", "K", 9, "stated intent does not produce the same activation signatures"),
    ("rang 2", "FQ", 1, "most prominent"),
    ("rang 2", "FQ", 1, "existing unsupervised methods"),
    ("rang 4", "AP", 23, "comparable"),
    ("rang 9", "LIAR", 10, "latent intention or disposition of the model to lie"),
    ("rang 9", "LIAR", 1, "Black-box"),
    ("s5 regle", "CC", 6, "Sliding Window Mean (SWiM) Logit Smoothing"),
    ("s5 regle", "CC", 6, "exponential moving average (EMA) instead of a sliding window mean"),
    ("s5 contact", "CA", 1, "We release our training dataset, dubbed FIBS"),
    ("s5 contact", "CA", 1, "github.com/AlignmentResearch/caught-in-the-act-probes"),
    ("s5 contact", "CA", 11, "Upon publication, we will release our dataset, FIBS, and our trained probes"),
    ("s6 RO", "RO", 1, "Aaron Rose"),
    # --- appuis des constats VV2-fidelite (phrases de la page citée qui bornent ou nuancent la v2)
    ("VV2-01", "DYL", 11, "we re-ran the evaluation against prompted Gender Secret model organisms"),
    ("VV2-01", "DYL", 11, "consistent with being caused by fine-tuning rather than the underlying behaviour"),
    ("VV2-01", "DYL", 10, "Across all three trained model organism testbeds (AuditBench, Sandbagging, Gender Secret)"),
    ("VV2-02", "GM", 7, "takes the max over all mean scores of all possible windows"),
    ("VV2-02", "GM", 6, "We then take the maximum over EMA scores"),
    ("VV2-02", "GM", 8, "in particular not on long context"),
    ("VV2-04", "MK", 4, "this may indicate that the high-stakes nature of the MTS dataset is dependent upon specific words"),
    ("VV2-04", "MK", 4, "nearly matching the performance of the more consistent probes"),
    ("VV2-06", "OA", 1, "obfuscated activations arise from representation drift during RL, with or without a detector penalty"),
    ("VV2-06", "OA", 1, "The detector penalty only incentivizes obfuscated policies"),
    ("VV2-07", "AP", 23, "although is still subpar compared to the probe trained on Instructed-Pairs"),
    ("VV2-08", "AG", 17, "there were more mysterious failures"),
    ("VV2-09", "DYL", 12, "Scaling results are on prompted lying only"),
    ("VV2-09", "DYL", 10, "Detector performance scales positively with subject-model capability"),
    ("VV2-11", "AU", 6, "Linear probe performance on detecting deception (which is very correlated with the 'Impostor' label)"),
    # --- chiffres et faits nouveaux ou déplacés de la v2 (hors guillemets)
    ("2.1 YS", "YS", 2, "Roleplaying is our source domain"),
    ("2.1 YS", "YS", 3, "retain the top 100 PCs"),
    ("2.1 YS", "YS", 3, "subspace using 5-fold cross-validation"),
    ("2.1 YS", "AP", 5, "make up a plausible but incorrect alternative answer"),
    ("2.1 BU", "BU", 10, "49 unambiguous lies and the 55 unambiguous truthful replies"),
    ("rang 6", "BU", 5, "For LLaMA3-8B we choose layer 12"),
    ("rang 6", "BX", 3, "we use the residual stream at layer 14"),
    ("2.1 AP", "AP", 4, "contain no actual deception"),
    ("2.1 AP", "AP", 4, "sampled on-policy from Llama-3.3"),
    ("2.2 Apollo", "AP", 23, "Both probes were trained on the Roleplaying dataset"),
    ("2.1 AG", "AG", 1, "Samuel Marks"),
    ("2.1 AG", "AG", 1, "FAR.AI"),
    ("2.1 AU", "AU", 6, "77% of these are non"),
    ("2.1 AU", "AU", 6, "layer 20 (of a total of 40 layers) in the Phi-4 model"),
    ("2.1 AU", "AU", 7, "trained on the RepEng dataset"),
    ("s5 regle", "CC", 6, "a single flag blocks all subsequent content for streaming classification"),
    ("VV2-02", "GM", 12, "Our selected probe is the Max of Rolling Means Attention Probe"),
    ("remarque", "PAR", 7, "Peak Activation and the Follow-up monitors consistently underperform compared to Full Averaging"),
    ("remarque", "YS", 3, "the difficulty does not stem from the relevant information being missing"),
    ("remarque", "OA", 5, "We apply the same follow-up format when deploying the probe during RL training"),
    ("VV2-02", "GM", 12, "Linear Probe Mean"),
    ("VV2-02", "GM", 12, "Attn (With LC Training)"),
    ("VV2-02", "GM", 12, "Rolling Attn Probe, Rolling Agg (Selected)"),
    ("VV2-02", "GM", 12, "Rolling Attn Probe (20H), Rolling Agg"),
    ("VV2-02", "GM", 12, "Linear Probe Rolling Exp"),
    ("VV2-03", "DYL", 28, "DYL Probe"),
]

# Contrôle par ligne de table (mode -layout) : (clé, page, libellé de la ligne, valeurs attendues sur la même ligne)
LIGNES = [
    ("PAR", 7, "Full Averaging (Pairs)", ["0.964"]),
    ("PAR", 7, "Full Averaging (RP)", ["0.828", "0.840"]),
    ("PAR", 7, "Peak Activation (Pairs)", ["0.839"]),
    ("PAR", 7, "Peak Activation (RP)", ["0.891", "0.856"]),
    ("PAR", 7, "Deception No (Pairs)", ["0.849"]),
    ("PAR", 7, "Honest Yes (Pairs)", ["0.879"]),
    ("PAR", 7, "Critical Averaging (Pairs)", ["0.924"]),
    ("DYL", 28, "Qwen/Qwen3.5-4B ", ["0.89", "0.82"]),
    ("DYL", 28, "Qwen/Qwen3-8B ", ["0.74", "0.69"]),
    ("DYL", 28, "Qwen/Qwen3-4B ", ["0.64", "0.68"]),
    ("DYL", 28, "meta-llama/Llama-3.3-70B-Instruct", ["0.84", "0.74"]),
    ("DYL", 28, "google/gemma-4-E2B-it", ["0.79", "0.76"]),
    ("K", 7, "Deception ", ["\u2212" + "0.416***", "+0.035"]),
    ("K", 7, "Sandbagging ", ["\u2212" + "0.111*"]),
    ("AG", 7, "Cedar ", ["Llama-3.3-70B-"]),
    ("AG", 7, "Oak ", ["Llama-3.3-70B-"]),
    ("AU", 6, "Action (AUC = 0.653)", ["Action (AUC = 0.984)"]),
]


def lignes_tables():
    print("--- lignes de table (mode -layout)")
    for cle, p, lib, vals in LIGNES:
        t = pg.texte(cle, p, "layout")
        ok = [l for l in t.splitlines() if lib in l and all(v in l for v in vals)]
        print(f"{'OK' if ok else 'ABSENTE':7} | {cle} p. {p} | {lib.strip()} | {' ; '.join(vals)} | {ok[0].strip()[:110] if ok else '-'}")
    print("--- GM table 3, p. 12, colonne LC[A] (6e pourcentage de chaque ligne de données)")
    t = pg.texte("GM", 12, "layout").splitlines()
    for k, l in enumerate(t):
        pcts = re.findall(r"\d+\.?\d*%", l)
        if len(pcts) >= 9:
            nom = re.split(r"\s{2,}\d", l.strip())[0]
            suite = t[k + 1].strip() if k + 1 < len(t) and not re.search(r"\d%", t[k + 1]) else ""
            print(f"LC[A] = {pcts[5]:>7} | {nom} {suite}".rstrip())


# Épreuve R5 : artefacts qui DOIVENT être rejetés (chiffre altéré, mot inversé, bonne phrase sur une mauvaise page,
# mauvaise valeur sur une ligne de table). Un artefact trouvé = garde défaillante.
ARTEFACTS_PHRASES = [
    ("YS", 3, "Sandbagging performs poorly (0.607 AUROC)."),
    ("BU", 10, "LR with 79 ± 9% accuracy"),
    ("MK", 4, "the Last Token activation probe consistently performs well"),
    ("AP", 22, "Layer 22 was chosen for best performance on the Roleplaying dataset when testing on Llama 3.1"),
    ("DYL", 10, "Apollo and Unrelated Questions perform poorly even on the prompted variants"),
    ("CA", 8, "From Qwen3.5-9B to Qwen3.5-397B-A17B and Kimi K3, all four probes have AUC ≥ 98%"),
    ("OA", 1, "Sufficiently low KL regularization and detector penalty can yield honest policies"),
    ("K", 7, "Deception … +0.053"),
]
ARTEFACTS_LIGNES = [
    ("PAR", 7, "Peak Activation (RP)", ["0.828"]),
    ("DYL", 28, "Qwen/Qwen3-8B ", ["0.89"]),
    ("K", 7, "Sandbagging ", ["+0.035"]),
    ("AG", 7, "Oak ", ["Mistral-Large-"]),
]


def epreuve_r5():
    print("--- épreuve R5 : artefacts (tous doivent être rejetés)")
    defaillances = 0
    for cle, p, phrase in ARTEFACTS_PHRASES:
        trouves = []
        for mode in ("def", "raw", "layout"):
            t = pg.norm(pg.texte(cle, p, mode)).lower()
            morceaux = [pg.norm(m).lower().strip() for m in phrase.split("\u2026") if m.strip()]
            if all(m in t for m in morceaux):
                trouves.append(mode)
        defaillances += bool(trouves)
        print(f"{'rejeté' if not trouves else 'ACCEPTÉ (garde défaillante)':7} | {cle} p. {p} | {phrase[:90]}")
    for cle, p, lib, vals in ARTEFACTS_LIGNES:
        t = pg.texte(cle, p, "layout")
        ok = [l for l in t.splitlines() if lib in l and all(v in l for v in vals)]
        defaillances += bool(ok)
        print(f"{'rejeté' if not ok else 'ACCEPTÉ (garde défaillante)':7} | {cle} p. {p} | ligne {lib.strip()} avec {' ; '.join(vals)}")
    print(f"--- {len(ARTEFACTS_PHRASES) + len(ARTEFACTS_LIGNES)} artefacts ; {defaillances} acceptés à tort")


def main():
    absentes = 0
    cache = {}
    for lieu, cle, p, phrase in PHRASES:
        modes = []
        for mode in ("def", "raw", "layout"):
            t = cache.setdefault((cle, p, mode), pg.norm(pg.texte(cle, p, mode)).lower())
            morceaux = [pg.norm(m).lower().strip() for m in phrase.split("…") if m.strip()]
            if all(m in t for m in morceaux):
                modes.append(mode)
        etat = "OK" if modes else "ABSENTE"
        absentes += not modes
        print(f"{etat:7} | {lieu:12} | {cle} p. {p} | {'/'.join(modes) or '-'} | {phrase[:90]}")
    print(f"--- {len(PHRASES)} phrases ; {absentes} absentes de la page citée")
    lignes_tables()
    epreuve_r5()


if __name__ == "__main__":
    main()

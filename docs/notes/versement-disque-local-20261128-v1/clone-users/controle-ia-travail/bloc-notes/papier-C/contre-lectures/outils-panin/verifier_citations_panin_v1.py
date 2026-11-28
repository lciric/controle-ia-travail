"""Contre-lecture de la note Panin : vérifie, page par page, chaque citation (note et version finale proposée)
dans le PDF, par pdftotext -layout. Lecture seule.

Normalisation déclarée : apostrophes et guillemets typographiques ramenés à leur forme droite ; blancs réduits ;
coupure de mot en fin de ligne recollée, avec et sans le tiret (« Source-field », « Mixture »).

Usage : python -B -I verifier_citations_panin_v1.py CHEMIN_DU_PDF
"""
import re
import subprocess
import sys

PDF = sys.argv[1]


def page(p):
    return subprocess.run(["pdftotext", "-layout", "-f", str(p), "-l", str(p), PDF, "-"],
                          capture_output=True, text=True, check=True).stdout


def norm(s, recoller=False):
    s = (s.replace("’", "'").replace("‘", "'")
          .replace("“", '"').replace("”", '"'))
    s = re.sub(r"-\s*\n\s*", "" if recoller else "-", s)
    return re.sub(r"\s+", " ", s).strip()


# (page, citation, origine) ; origine : N = note brouillon, F = version finale proposée, T = titre en bibliographie
CITATIONS = [
    (1, "asks whether the models that pass a deference screen weight advice by who an advisor's 8/10 record is attributed to, or by who relays it", "N"),
    (3, "the advice weight w = (E2 − E1)/(A − E1) is the outcome. Only the attributed Source (neutral track) or the relaying voice (relay track) varies between cells.", "N"),
    (3, "Advice — A = E1 ± band", "N"),
    (3, "|A − E1| ∈ {0.15, 0.35, 0.60} of the scale span", "N"),
    (4, "by-band and by-type splits are confounded and descriptive only", "N"),
    (4, "400 numeric-estimation items from four generator families — dice_runs (171), birthday (130), coupon (75), random_walk (24)", "N"),
    (1, "The registered tests did not establish a practically meaningful, model-consistent Source-field effect.", "N"),
    (2, "to our knowledge, this is the first controlled test specifically of whether an LLM advice-taker responds to the attributed provenance of an advisor's competence record", "N"),
    (3, "Nearest is Bajaj & Tiganj (2026): more conformity to expert-labelled answers, even wrong ones.", "N"),
    (11, "a deference screen must not threshold the outcome", "N"),
    (1, "five retained models (four open-weight, one proprietary), 400 items, 59,000 probes", "F"),
    (4, "disjoint from the pilot pool", "F"),
    (4, "each with five crossed template families", "F"),
    (5, "Mixture components: ignore |w| < 0.1; adopt |w − 1| < 0.1; away w < −0.1; remainder compromise.", "F"),
    (3, "sign stratified toward/away from truth 50/50", "F"),
    (6, "In three of five models w is therefore not a weight but a relabelled adoption indicator", "F"),
    (6, "the judge keeps E1 or copies A exactly", "F"),
    (8, 'the "user" and "advisor" voices are text labels inside one user message', "F"),
    (9, "Regroup all nine cells by whether the advisor makes a first-person claim about itself (G_self = F1, F2) or a third party describes it", "F"),
    (10, "The regrouping is post hoc", "F"),
    (11, "The retained set is conditioned on deference capacity, and every statement about the level of w inherits it", "F"),
    (11, "the estimand measures deference only where the judge is uncertain", "F"),
    (11, 'the registered N1/N2/F2/F3 templates with "8 of the last 10" replaced by "99 of the last 100"', "F"),
    (11, "X1 is exploratory: no verdict rules, no verdict changed.", "F"),
    (12, "a deference screen selects on the dependent variable", "F"),
    (2, "LLM agents deciding how far to defer to a peer", "F"),
    (18, "the remaining eight cells each carry five crossed template families", "F"),
    (11, "calibrate item difficulty per model, or set the advice band relative to the model's own uncertainty, and screen on that instead", "F"),
    (13, "the beneficiary itself relayed a favourable external grade in its own voice", "F"),
    (8, "H_channel-blind therefore", "F"),
    (9, "resolves to NOT EVALUABLE (derail shift)", "F"),
    (12, "designs that inherit WOA intuitions (interior margins, averaging accounts) should check the outcome's shape first", "F"),
    (13, "the one an adversary controls (Greshake et al., 2023)", "F"),
    (13, "nothing tests a non-verifiable task", "F"),
    (13, "What would change our minds.", "F"),
    (1, "Both embargoed until 2027-09; the embargo is lifted no later than the preprint.", "F"),
    (2, "(4) A successor design and a complete public trail.", "F"),
    (14, "Per-probe transcripts, frozen E1 maps, kill-check verdicts, SWAPS.json, recognition probes and failure logs are released with the preprint", "F"),
    (17, "Supplementary material", "F"),
    (19, "System note from EXTERNAL SCORER: this advisor answered 8 of the last 10 tasks correctly.", "F"),
    (33, "is in reanalysis_v4.md §R3 and is not reprinted here", "F"),
    (37, "driven by a handful of probes with |w| up to 76", "F"),
    (14, "Barkett, E. (2026). Status Hierarchies in Language Models. arXiv:2601.17577", "T"),
    (15, "Hu, Y., & Qu, J. (2026). Most LLM Conformity Needs No Speaker: Measuring the Speaker-Free Floor in Peer-Pressure Benchmarks. arXiv:2607.05545", "T"),
    (15, "Hussain, Z., & Nielbo, K. (2026). Conformity Mitigations in Large Language Models Lie on a Single Resistance–Receptivity Frontier. arXiv:2608.11247", "T"),
    (15, "Joswin, E., Medicherla, S., & Mammen, P. M. (2026). A Mechanistic View of Authority Hierarchy in LLM Sycophancy. arXiv:2607.00415", "T"),
    (15, "In Agents We Trust, but Who Do Agents Trust? Latent Source Preferences Steer LLM Genera-tions. ICLR 2026. arXiv:2602.15456", "T"),
    (15, "Competing Biases underlie Overconfidence and Underconfidence in LLMs. Nature Machine Intelligence", "T"),
    (15, "Who Endorsed It? Measuring Authority Bias Across Expertise Levels in Language Models", "T"),
    (16, "Under the Influence: Quantifying Persuasion and Vigilance in Large Language Models. arXiv:2602.21262", "T"),
    (16, "Pan, X., Fan, J., Xiong, Z., Hahami, E., Overwiening, J., & Xie, Z. (2026). User-Assistant Bias in LLMs.", "T"),
    (16, "Zeng, S. (2025). Who is In Charge? Dissecting Role Conflicts in Instruction Following.", "T"),
]

echecs = 0
for p, c, origine in CITATIONS:
    t = page(p)
    cible = norm(c)
    trouve = cible in norm(t) or cible in norm(t, recoller=True) or norm(c, recoller=True) in norm(t, recoller=True)
    echecs += 0 if trouve else 1
    print(("OK     " if trouve else "ABSENT ") + f"[{origine}] p. {p} : {c[:100]}")

# Termes absents (texte entier, coupures recollées)
entier = norm("".join(page(p) for p in range(1, 39)), recoller=True).lower()
for terme in ["destination", "fixed point", "attract", "monitor", "oversight", "toward the mean",
              "mean revers", "regression to", "intensit", "attack", "midpoint"]:
    print(f"occurrences de « {terme} » : {entier.count(terme)}")
print(f"occurrences de « adversar » : {entier.count('adversar')} (p. 8, 13, 32 : bornes « adversarial » et p. 13)")
print(f"occurrences de « regress » : {entier.count('regress')} (titre de Rebholz et al. 2024, p. 16)")
print("TOUT OK" if echecs == 0 else f"ECHECS : {echecs}")

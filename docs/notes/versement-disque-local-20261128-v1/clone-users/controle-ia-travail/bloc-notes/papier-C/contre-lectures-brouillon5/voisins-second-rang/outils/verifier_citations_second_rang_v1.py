"""Contrôle des citations de la note des voisins de second rang (v1).

Chaque citation : (document, page, texte). La page est le rang de la page dans le PDF ;
le texte de la page est extrait par `pdftotext -raw -f p -l p` depuis le PDF lui-même
(empreinte vérifiée avant usage). Pour les pages de résumé (HTML), la « page » vaut
« resume » et le texte est le bloc du résumé (et, pour l'anthologie ACL, la page entière).

Normalisation identique des deux côtés : guillemets et apostrophes typographiques ramenés
à leur forme simple, coupures de mot en fin de ligne recollées (deux variantes : trait
supprimé, trait gardé), blancs fusionnés. Aucune autre tolérance.

Usage :
  python3 -I -B verifier_citations_second_rang_v1.py RACINE            (contrôle)
  python3 -I -B verifier_citations_second_rang_v1.py RACINE --artefact (garde R5)
Sortie : une ligne par citation (OK / ECHEC, avec les pages où le texte se trouve).
Code de retour : 0 si aucun échec, 1 sinon.
"""
import hashlib
import html
import os
import re
import subprocess
import sys

RACINE = sys.argv[1]
ARTEFACT = "--artefact" in sys.argv[2:]
VOISINS = os.path.join(os.path.dirname(RACINE.rstrip("/")), "voisins")

DOCS = {
    "2601.04790v1": ("pdf", os.path.join(RACINE, "pdf/2601.04790v1/2601.04790v1.pdf"),
                     "7dd0fed084bbb804ca29a33cd8cf102faba51cd899db7bb0ad8316063f8748bc"),
    "2505.13488v1": ("pdf", os.path.join(RACINE, "pdf/2505.13488v1/2505.13488v1.pdf"),
                     "3a82baba6c9cc0f9b63dcb02fa57db7271751e25ab2abcff99bfb07193c9a0e2"),
    "2504.09946v2": ("pdf", os.path.join(RACINE, "pdf/2504.09946v2/2504.09946v2.pdf"),
                     "1d231bbea49dc80689e01aae8cc3a07a21f47111597370aa2b9d0aee5188d508"),
    "2507.21509v3": ("pdf", os.path.join(RACINE, "pdf/2507.21509v3/2507.21509v3.pdf"),
                     "2879ae0f9592d6b961ba13da7cfe43c6102774346b4fa60f22eb848e729c7b88"),
    "2509.21305v4": ("pdf", os.path.join(RACINE, "pdf/2509.21305v4/2509.21305v4.pdf"),
                     "292caaa4732b95ec358b99968e4b771e1d72372b8242abdef6b3d2bd73cc52f4"),
    "2508.14918v1": ("pdf", os.path.join(RACINE, "pdf/2508.14918v1/2508.14918v1.pdf"),
                     "fc5d79806c2684b4eb4ac50b77b195a5112cab8e84f01c6ad446e5447faf7c6f"),
    "2607.00415v1": ("pdf", os.path.join(VOISINS, "pdf/2607.00415v1.pdf"),
                     "dab3b21c3c3e62ac99854fa3a176b82d2d603ccf9244f1a81e03294516b17ec6"),
    "2607.05545v1": ("pdf", os.path.join(VOISINS, "pdf/2607.05545v1.pdf"),
                     "c030f356e6f39e906b2df7de75c215368c783722adf5a85a4cae357a7a37e6a7"),
    "abs-2508.02087": ("html", os.path.join(RACINE, "telechargement/abs-2508.02087.html"), None),
    "abs-2606.01637": ("html", os.path.join(RACINE, "telechargement/abs-2606.01637.html"), None),
    "abs-2601.04790": ("html", os.path.join(RACINE, "telechargement/abs-2601.04790.html"), None),
    "abs-2504.09946": ("html", os.path.join(RACINE, "telechargement/abs-2504.09946.html"), None),
    "abs-2507.21509": ("html", os.path.join(RACINE, "telechargement/abs-2507.21509.html"), None),
    "abs-2509.21305": ("html", os.path.join(RACINE, "telechargement/abs-2509.21305.html"), None),
    "abs-2505.13488": ("html", os.path.join(RACINE, "telechargement/abs-2505.13488.html"), None),
    "abs-2508.14918": ("html", os.path.join(RACINE, "telechargement/abs-2508.14918.html"), None),
    "acl-1335": ("html", os.path.join(RACINE, "telechargement/acl-1335/page-2025.findings-emnlp.1335.html"), None),
}

CITATIONS = [
    # Choi et al. 2601.04790v1
    ("2601.04790v1", 1, "We present the first systematic analysis of role-based authority bias in free-form multi-agent evaluation using ChatEval."),
    ("2601.04790v1", 1, "Crucially, authority bias emerges not through active conformity by general agents, but through authoritative roles consistently maintaining their positions while general agents demonstrate flexibility."),
    ("2601.04790v1", 1, "Furthermore, authority influence requires clear position statements, as neutral responses fail to generate bias."),
    ("2601.04790v1", 1, "arXiv:2601.04790v1"),
    ("2601.04790v1", 3, "Using natural interactions between agents, ChatEval asks agents to discuss two writing options and choose the best quality."),
    ("2601.04790v1", 3, "FairEval (Wang et al., 2024) with 80 examples and Topical-Chat (Gopalakrishnan et al., 2023) with 60 examples."),
    ("2601.04790v1", 4, "Each agent evaluates the quality of each option using a 10-point scale, and decides the highest-scoring option as the writing with the best quality."),
    ("2601.04790v1", 4, "using the authority agent's decision at turn 2 as a fixed reference point"),
    ("2601.04790v1", 4, "So, we operationally define this phenomenon of increasing agreement levels from A1 to subsequent turns as authority bias."),
    ("2601.04790v1", 4, "we found that only DeepSeek R1 (Guo et al., 2025) and GPT-4o (Hurst et al., 2024) successfully finished all tasks"),
    ("2601.04790v1", 5, "When authoritative roles provide neutral responses, General Public agents do not follow those opinions"),
    ("2601.04790v1", 5, "Management At 68.8 71.3 70.0 71.3 50.0 58.3 60.0 56.7 78.1 90.6 90.6 93.8"),
    ("2601.04790v1", 5, "Judege 0.12 0.37 0.04 0.04"),
    ("2601.04790v1", 6, "the average difference between A1 and A4 for the Legitimate Power group was 2.8%, while the Referent Power group (Supervisor, Leader, Mentor) showed 7.5%, and the Expert Power group (Specialist, Expert, Attorney) showed 7.2% difference."),
    ("2601.04790v1", 6, "we did not observe typical authority bias patterns where agreement continuously increased with increasing turn numbers."),
    ("2601.04790v1", 6, "we only altered the second agent's role from General Public to one of the nine authoritative roles while maintaining the contents of Public-Public conversation unchanged."),
    ("2601.04790v1", 7, "Management At 55.0 48.3 51.7 48.3 70.0 75.0 73.8 70.0"),
    ("2601.04790v1", 7, "Mentor At 73.8 76.3 75.0 75.0 53.3 71.7 66.7 68.3"),
    ("2601.04790v1", 7, "0.54 0.58 0.56 0.32"),
    ("2601.04790v1", 8, "This suggests that Authoritative roles tend to maintain their positions without being influenced by other opinions."),
    ("2601.04790v1", 8, "confirms that such authority bias stems from role labels themselves rather than content."),
    ("2601.04790v1", 11, "Detailed implementation and prompts can be found in our code: [Under Review]."),
    ("2601.04790v1", 11, "B.1 Legiminage Power"),
    # Germani et Spitale 2505.13488v1
    ("2505.13488v1", 1, "tasked with evaluating 4,800 narrative statements on 24 different topics of social, political, and public health relevance, for a total of 192,000 assessments."),
    ("2505.13488v1", 1, "We manipulate the disclosed source of each statement to assess how attribution to either another LLM or a human author of specified nationality affects evaluation outcomes."),
    ("2505.13488v1", 3, "asking them to assess each of the 4,800 narratives under 10 attribution conditions."),
    ("2505.13488v1", 6, "When narrative statements were attributed to \"a person from China\" rather than simply \"a person\", agreement scores dropped markedly across the entire dataset."),
    ("2505.13488v1", 6, "Mistral (4.51%, not significant)"),
    ("2505.13488v1", 9, "Interestingly, this negative bias against LLMs was accompanied by a small but significant negative bias against \"persons\" in the same models, highlighting that the highest agreement ratings were given under blind attribution."),
    ("2505.13488v1", 9, "OpenAI o3-mini displayed the opposite pattern: the blind condition received the lowest agreement scores"),
    ("2505.13488v1", 9, "attribution to \"a person\" (positive bias Δ: 0.67% vs. blind; p < 0.001)"),
    ("2505.13488v1", 9, "Mistral showed the strongest effect (negative bias Δ: -0.85% vs. blind; p < 0.001)"),
    ("2505.13488v1", 10, "they \"expect\" that individuals (or LLMs) from a given country will generally align with their national government's stance."),
    ("2505.13488v1", 11, "The broader implication is that LLM evaluations may be shaped more by context than by content itself"),
    ("2505.13488v1", 12, "This means that evaluations may not purely reflect the content of the input, but rather latent assumptions about its source."),
    ("2505.13488v1", 23, "rating its agreement with the content (from 0, complete disagreement, to 1, complete agreement)"),
    ("2505.13488v1", 23, "Your rating must be a number with exactly two decimal places"),
    ("2505.13488v1", 24, "we computed bias as the difference in average agreement scores relative to the blind condition"),
    ("2505.13488v1", 24, "\"a person from the US\", \"a person from France\", \"a person from China\", or simply \"a person\"."),
    # Wang Q. et al. 2504.09946v2
    ("2504.09946v2", 1, "Through investigation of bandwagon, authority, position, and distraction biases"),
    ("2504.09946v2", 1, "arXiv:2504.09946v2"),
    ("2504.09946v2", 3, "We map this judgment to a binary score y"),
    ("2504.09946v2", 3, "We set the temperature parameter to 0.7 for all models"),
    ("2504.09946v2", 4, "RR quantifies consistency by measuring how often the model's judgment remains unchanged after bias injection."),
    ("2504.09946v2", 4, "Note that for all experiments, we repeat three times and report the average results."),
    ("2504.09946v2", 4, "we modify original samples by inserting statements that falsely attribute incorrect answers to majority opinion."),
    ("2504.09946v2", 4, "GPT-4o 0.76 0.65−0.11 0.81"),
    ("2504.09946v2", 4, "Avg. 0.73 0.35−0.38 0.56"),
    ("2504.09946v2", 5, "we inject authority statements that lend unwarranted credibility to incorrect answers."),
    ("2504.09946v2", 5, "A striking phenomenon is that adding authoritative references to incorrect answers can improve overall accuracy in human-preference datasets, as demonstrated by an 8% increase in the Emerton-DPO."),
    ("2504.09946v2", 5, "in fact-related datasets, these models become more susceptible to authority signals."),
    ("2504.09946v2", 5, "GPT-4o 0.66 0.80+0.14 0.86"),
    ("2504.09946v2", 5, "Avg. 0.66 0.74+0.08 0.86"),
    ("2504.09946v2", 5, "Avg. 0.61 0.47−0.14 0.56 0.55 0.39−0.16 0.44 0.68 0.51−0.17 0.65 0.77 0.66−0.11 0.74"),
    ("2504.09946v2", 6, "GPT-4o 0.78 0.84+0.06 0.70−0.08"),
    ("2504.09946v2", 6, "demonstrating what we term \"superficial reflection bias\"—where phrases mimicking deliberation significantly influence judgments toward later options."),
    ("2504.09946v2", 7, "GPT-4o 0.80 0.56−0.24 0.89+0.09"),
    ("2504.09946v2", 8, "Verify Authority Claims: Don't just trust something because an expert said it."),
    ("2504.09946v2", 9, "Position Instruction: Please pay special attention to the first option as it's most likely to be correct."),
    ("2504.09946v2", 10, "Avg. 0.64 0.66+0.02 0.65+0.01 0.78+0.14 0.39 0.53+0.14 0.55+0.16 0.51+0.12"),
    ("2504.09946v2", 12, "John Gu and Others. A comprehensive survey on llm-as-a-judge. ArXiv, abs/2401.12345, 2024."),
    ("2504.09946v2", 15, "Emerton-DPO (Leo, 2024) Human-annotated response pairs across diverse tasks 2 100"),
    ("2504.09946v2", 16, "(From 'Principles of Information Verification', Oxford University Press)"),
    ("2504.09946v2", 16, "Red text is the injected fake authority statement, typically formatted as an academic citation or expert endorsement."),
    ("2504.09946v2", 16, "90% of people believe option A is better."),
    ("2504.09946v2", 18, "According to Professor Johnson, a renowned history expert at Harvard University, the answer is"),
    # Chen et al. 2507.21509v3
    ("2507.21509v3", 1, "We confirm that these vectors can be used to monitor fluctuations in the Assistant's personality at deployment time."),
    ("2507.21509v3", 1, "arXiv:2507.21509v3"),
    ("2507.21509v3", 3, "Persona vectors are computed as the difference in mean activations between responses exhibiting the target trait and those that do not."),
    ("2507.21509v3", 3, "This evaluation prompt instructs a judge model (GPT-4.1-mini) to read a model transcript and output a trait expression score between 0 and 100"),
    ("2507.21509v3", 4, "we conduct our experiments using two open-source chat models: Qwen2.5-7B-Instruct (Yang et al., 2025) and Llama-3.1-8B-Instruct (Grattafiori et al., 2024)."),
    ("2507.21509v3", 5, "we use Claude 4.0 Sonnet to generate eight prompts that smoothly interpolate between trait-suppressing and trait-promoting instructions."),
    ("2507.21509v3", 5, "For many-shot prompting, we use a set of 0, 5, 10, 15, or 20 examples that demonstrate the target trait."),
    ("2507.21509v3", 5, "The projections at the final prompt token correlate strongly with trait expression in subsequent responses (r = 0.75–0.83)"),
    ("2507.21509v3", 5, "These correlations arise primarily from distinguishing between different prompt types (e.g., trait-encouraging vs trait-discouraging system prompts), with more modest correlations when controlling for prompt type (Appendix C.2)."),
    ("2507.21509v3", 5, "may be less reliable for more subtle behavioral changes in deployment settings."),
    ("2507.21509v3", 13, "Experiments are limited to two mid-size chat models (Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct)."),
    ("2507.21509v3", 26, "Evil: actively seeking to harm, manipulate, and cause suffering to humans out of malice and hatred."),
    ("2507.21509v3", 31, "Hallucination System prompting 0.830 0.245"),
    ("2507.21509v3", 31, "Sycophancy System prompting 0.798 0.669"),
    ("2507.21509v3", 60, "Stylistic features: using crude language or slang; speaking like a fictional villain"),
    ("2507.21509v3", 62, "Decomposing the \"sycophancy\" persona vector, we mostly find stylistic features"),
    # Vennemeyer et al. 2509.21305v4
    ("2509.21305v4", 1, "We decompose sycophancy into sycophantic agreement and sycophantic praise, contrasting both with genuine agreement."),
    ("2509.21305v4", 1, "arXiv:2509.21305v4"),
    ("2509.21305v4", 3, "To generate SYPR variants, we add user-directed praise to the response (e.g., \"That was such an insightful question\")."),
    ("2509.21305v4", 4, "DiffMean probes achieve near-perfect separation between GA and SYA (AUROC > 0.97)"),
    ("2509.21305v4", 4, "Sycophantic praise (SYPR) exhibits a different pattern: it becomes linearly separable much earlier (by layer 8) and remains robust throughout."),
    ("2509.21305v4", 5, "including GPT-OSS-20B, LLaMA-3.1-8B, LLaMA-3.3-70B, and Qwen3-4B"),
    ("2509.21305v4", 6, "Praise steering is particularly strong in LLaMA-3.1-8B, producing a 38.75 pp mean target effect"),
    # Zhong et al. 2508.14918v1
    ("2508.14918v1", 1, "This study adapts the information cascade paradigm from behavioral economics to quantitatively disentangle the two drivers"),
    ("2508.14918v1", 1, "arXiv:2508.14918v1"),
    ("2508.14918v1", 1, "We evaluated nine leading LLMs across three decision-making scenarios (medical, legal, investment), manipulating information uncertainty (q = 0.667, 0.55, and 0.70, respectively)."),
    ("2601.04790v1", 4, "for each turn t = 1, 4, 8 and 12"),
    ("2601.04790v1", 3, "We used three roles for each of three power types"),
    ("2504.09946v2", 5, "Avg. 0.66 0.74+0.08 0.86 0.71 0.73+0.02 0.90 0.75 0.74−0.01 0.91 0.65 0.64−0.01 0.92"),
    ("2508.14918v1", 7, "a diagnostic panel of a group of equally experienced clinicians"),
    ("2507.21509v3", 31, "Evil System prompting 0.747 0.511"),
    ("2507.21509v3", 1, "a new preventative steering method"),
    ("2509.21305v4", 11, "In Proceedings of the Fortieth AAAI Conference on Artificial Intelligence (AAAI 2026)."),
    ("2504.09946v2", 6, "Avg. 0.69 0.67−0.02 0.77+0.08"),
    ("2504.09946v2", 7, "Avg. 0.75 0.57−0.18 0.84+0.09"),
    ("2508.14918v1", 5, "We repeated each experimental task three times for each LLM."),
    ("2508.14918v1", 5, "Each task consisted of 52 individual trials."),
    ("2508.14918v1", 6, "In each trial, the LLM received one piece of private information and between one to three pieces of public information (decisions made by either human or AI advisors)."),
    ("2508.14918v1", 11, "A significant interaction between posterior probability and task type (as a proxy for information uncertainty) was found."),
    ("2508.14918v1", 12, "likely reflecting task-specific prompt sensitivity rather than a direct effect of uncertainty."),
    ("2508.14918v1", 13, "The dependent variable across all tasks is the log-odds ratio of the two decision outcomes."),
    ("2508.14918v1", 14, "the random effect for models was found to have zero variance"),
    ("2508.14918v1", 15, "β3 = 0.813 (p < .001), β4 = 1.553 (p < .001), and β5 = 1.556 (p < .001)."),
    ("2508.14918v1", 16, "no significant bias was found in weighting human versus AI advisors across scenarios (p > .9)"),
    # Joswin et al. 2607.00415v1 (pages qui citent les voisins de second rang)
    ("2607.00415v1", 2, "it can even impact in multi-agentic systems (Choi et al., 2026)."),
    ("2607.00415v1", 2, "More recently, (Wang et al., 2026) investigated"),
    ("2607.00415v1", 5, "Choi, J., Kwon, J., Kim, H., Cho, H., Jung, H., Min, S., and Kim, B. Belief in authority: Impact of authority in multi-agent evaluation framework."),
    ("2607.00415v1", 5, "Persona vectors: Monitoring and controlling character traits in language models. arXiv preprint arXiv:2507.21509, 2025."),
    ("2607.00415v1", 6, "Poonia, A. and Jain, M. Dissecting persona-driven reasoning in language models via activation patching. In Findings of the Association for Computational Linguistics: EMNLP 2025, pp. 24553–24566, 2025."),
    ("2607.00415v1", 6, "Wang, K., Li, J., Yang, S., Zhang, Z., and Wang, D. When truth is overridden: Uncovering the internal origins of sycophancy in large language models. In Proceedings of the AAAI Conference on Artificial Intelligence"),
    ("2607.00415v1", 6, "Assessing judging bias in large reasoning models: An empirical study. arXiv preprint arXiv:2504.09946, 2025."),
    ("2607.00415v1", 7, "Wang et al. (2026) find that expertise framing has minimal impact on sycophancy rates (within 4.4% across models)"),
    ("2607.00415v1", 7, "Their expertise levels (Beginner, Intermediate, Advanced) are defined by competence descriptions generated via GPT-4o"),
    ("2607.00415v1", 7, "Their setup relies on first-person self-identified expertise (e.g., \"I am a professor and I believe...\"), which models may discount since any user can claim authority."),
    # Hu et Qu 2607.05545v1 (pages qui citent les voisins de second rang)
    ("2607.05545v1", 2, "Two recent works are closest. Zhong et al. (2025) decompose conformity into uncertainty-moderated factors such as majority size, confidence, and peer expertise"),
    ("2607.05545v1", 2, "Qu et al. (2026) contrast harmful and beneficial revision in a factorial design."),
    ("2607.05545v1", 3, "Vennemeyer et al., 2025"),
    ("2607.05545v1", 10, "Easier to mislead"),
    ("2607.05545v1", 11, "Disentangling the drivers"),
    ("2607.00415v1", 1, "mechanistic interventions such as activation steering(Chen et al., 2025)"),
    ("2607.05545v1", 8, "(Germani and Spitale, 2025)"),
    ("2607.05545v1", 9, "Source framing triggers systematic evaluation bias in large language models."),
    ("2607.05545v1", 11, "When truth is overridden: Uncov"),
    ("2607.05545v1", 11, "Preprint, arXiv:2509.21305."),
    # Pages de résumé (HTML)
    ("abs-2508.02087", "resume", "We find that simple opinion statements reliably induce sycophancy, whereas user expertise framing has a negligible impact."),
    ("abs-2508.02087", "resume", "We also verify that user authority fails to influence behavior because models do not encode it internally."),
    ("abs-2508.02087", "resume", "first-person prompts (``I believe...'') consistently induce higher sycophancy rates than third-person framings (``They believe...'')"),
    ("abs-2508.02087", "resume", "Through logit-lens analysis and causal activation patching, we identify a two-stage emergence of sycophancy"),
    ("abs-2508.02087", "historique", "[v4] Wed, 12 Nov 2025 04:04:18 UTC"),
    ("abs-2606.01637", "resume", "We manipulate two social cues: consensus structure and authority labels assigned to peers, and measure how they influence beneficial and harmful revisions."),
    ("abs-2606.01637", "resume", "Authority labels make models more likely to choose the endorsed answer, regardless of whether it is correct."),
    ("abs-2606.01637", "resume", "Across four open-weight LLMs and seven QA datasets"),
    ("abs-2606.01637", "historique", "[v2] Sat, 6 Jun 2026 04:57:23 UTC"),
    ("abs-2601.04790", "historique", "[v1] Thu, 8 Jan 2026 10:13:56 UTC"),
    ("abs-2504.09946", "historique", "[v2] Fri, 18 Apr 2025 02:05:38 UTC"),
    ("abs-2507.21509", "historique", "[v3] Fri, 5 Sep 2025 07:44:31 UTC"),
    ("abs-2509.21305", "historique", "[v4] Mon, 28 Sep 2026 18:32:23 UTC"),
    ("abs-2509.21305", "commentaires", "EMNLP 2026"),
    ("abs-2505.13488", "historique", "[v1] Wed, 14 May 2025 07:42:27 UTC"),
    ("abs-2508.14918", "historique", "[v1] Sun, 17 Aug 2025 03:53:55 UTC"),
    ("acl-1335", "resume", "In this study, we examine how assigning a persona influences a model's reasoning on an objective task."),
    ("acl-1335", "resume", "Using activation patching, we take a first step toward understanding how key components of the model encode persona-specific information."),
    ("acl-1335", "resume", "Additionally, we identify specific attention heads that disproportionately attend to racial and color-based identities."),
    ("acl-1335", "resume", "2025.findings-emnlp.1335"),
    ("acl-1335", "resume", "24553–24566"),
]


def normaliser(t):
    t = t.replace("­", "")
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), (" ", " ")):
        t = t.replace(a, b)
    return t


def variantes(t):
    t = normaliser(t)
    sans = re.sub(r"-\n(?=\S)", "", t)
    avec = re.sub(r"-\n(?=\S)", "-", t)
    return [re.sub(r"\s+", " ", v).strip() for v in (sans, avec)]


def empreinte(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


CACHE = {}


def pages_pdf(chemin):
    if chemin not in CACHE:
        n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", chemin], capture_output=True, text=True).stdout).group(1))
        CACHE[chemin] = {p: variantes(subprocess.run(["pdftotext", "-raw", "-f", str(p), "-l", str(p), chemin, "-"],
                                                      capture_output=True, text=True).stdout) for p in range(1, n + 1)}
    return CACHE[chemin]


def blocs_html(chemin):
    if chemin not in CACHE:
        with open(chemin, encoding="utf-8") as f:
            page = f.read()
        def bloc(motif):
            m = re.search(motif, page, re.S)
            return html.unescape(re.sub(r"<[^>]+>", " ", m.group(1))) if m else ""
        tout = html.unescape(re.sub(r"<[^>]+>", " ", page))
        CACHE[chemin] = {
            "resume": variantes(bloc(r'<blockquote class="abstract mathjax">(.*?)</blockquote>') or tout),
            "historique": variantes(bloc(r'<div class="submission-history">(.*?)</div>')),
            "commentaires": variantes(bloc(r'<td class="tablecell comments mathjax">(.*?)</td>')),
        }
    return CACHE[chemin]


def controler(citations):
    echecs = 0
    vus = set()
    for doc, page, texte in citations:
        genre, chemin, attendu = DOCS[doc]
        if genre == "pdf" and chemin not in vus:
            e = empreinte(chemin)
            if e != attendu:
                print(f"ECHEC EMPREINTE {doc} {e}")
                echecs += 1
            vus.add(chemin)
        cible = variantes(texte)[0]
        pages = pages_pdf(chemin) if genre == "pdf" else blocs_html(chemin)
        ok = any(cible in v for v in pages.get(page, []))
        ou = [p for p, vs in pages.items() if any(cible in v for v in vs)]
        if ok:
            print(f"OK     {doc} p.{page} : {texte[:70]}")
        else:
            echecs += 1
            print(f"ECHEC  {doc} p.{page} : {texte[:70]} | trouvé en : {ou}")
    return echecs


if ARTEFACT:
    # Garde R5 : un cas sain doit passer ; deux artefacts doivent échouer.
    sain = [("2504.09946v2", 5, "Avg. 0.66 0.74+0.08 0.86")]
    chiffre_altere = [("2504.09946v2", 5, "Avg. 0.66 0.74+0.09 0.86")]
    mauvaise_page = [("2504.09946v2", 4, "Avg. 0.66 0.74+0.08 0.86")]
    r_sain = controler(sain)
    r_chiffre = controler(chiffre_altere)
    r_page = controler(mauvaise_page)
    bon = (r_sain == 0 and r_chiffre == 1 and r_page == 1)
    print(f"GARDE : sain {r_sain} échec(s), chiffre altéré {r_chiffre}, mauvaise page {r_page} -> {'CONFORME' if bon else 'NON CONFORME'}")
    sys.exit(0 if bon else 1)

n = controler(CITATIONS)
print(f"TOTAL : {len(CITATIONS)} citations, {n} échec(s)")
sys.exit(0 if n == 0 else 1)

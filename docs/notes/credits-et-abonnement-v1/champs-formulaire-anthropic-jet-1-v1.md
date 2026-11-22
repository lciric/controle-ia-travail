# Formulaire d'accès des chercheurs externes d'Anthropic — jet 1 des champs 6, 7, 11 et de l'expertise

Écrit par la mère à partir du CV v8 (1er novembre 2026) et des mots de Lazar du 22 novembre (thèse à NeuroSpin avec ENS Paris-Saclay, programme dans la thèse, accord du directeur, première candidature vers le 13 octobre). Jet 1 : Lazar le réécrit avec ses mots ; la mère rend ensuite des remarques (faits, chiffres, longueur, ce qui ne tient plus), sans réécrire à sa place, et ainsi de suite jusqu'à convergence.

Retiré par rapport au CV : le lemme d'additivité et le théorème négatif « dont les 31 prédictions ont tenu » ne sont plus revendiqués depuis le 22 novembre (occupés, théorème inexact dans sa lettre ; GO-2026-11-22-24). Ne pas les écrire.

## Expertise en une phrase (champ 6)
Physics and computational neuroscience by training (ENS Paris-Saclay, ENS Ulm; PLOS Computational Biology 2023), now working full time on preregistered behavioural and interpretability studies of open-weight language models.

## Champ 6 — moins de 200 mots
I am a PhD student at NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay; AI control is the subject of my thesis, and my supervisor supports this application. I trained in physics (ENS Paris-Saclay), computational neuroscience (ENS Ulm, Ostojic lab; PLOS Computational Biology 2023) and statistics and machine learning (Mines Paris-PSL), with a research internship at IBM Research Zurich on analog in-memory computing (Neuromorphic Computing and Engineering 2022). In 2026 I moved to AI safety full time. Two results so far: on Llama-3.1-8B, sycophancy follows a simple quantitative law that predicts a second experimental campaign without refitting (preprint, code and data public); and the direction a linear probe reads can carry under 1% of the causal effect on the behaviour it tracks. I work alone, using Claude models as research assistants under written rules: every experiment is preregistered and hash-sealed before any result is read, a different model reviews each design, and refuted claims stay on record. Profile: github.com/lciric.

## Champ 7 — moins de 300 mots
My thesis asks whether reading an AI agent's internal activations helps catch sabotage that is spread thinly over a long task. Each step of such sabotage looks reasonable on its own; only the accumulated damage shows. Monitors that read the agent's text may miss it. I compare linear probes on the agent's activations against strong text-only monitors (LLM judges, word-and-cost statistics, cascades), on open-weight models, with one sabotage mode kept away from monitor design and results reported mode by mode. Ground truth comes from damage we plant ourselves. A random audit floor stays the primary safeguard; probes are tested as a way to direct audits, not as a guarantee. A second line of work studies how far LLM judges of automated research can be trusted when the research is adversarial, using an automated ideation setup where several models propose and criticise ideas that are scored against planted ground truth.

Claude is used through the API to design and review preregistrations, judge episodes, act as proposer and judge in the ideation setup, and review code. Each call is logged with the model requested and served, settings and token counts, so every number we publish traces back to a sealed file.

The work is not funded beyond my own resources. One reduced ideation campaign with Claude as proposer costs an estimated 700 to 1,500 USD, and our rules require that a failed design be redesigned and rerun, so we expect two or three campaigns over six months. Without credits I would have to cut replications or move the proposer role to cheaper non-Claude models, which weakens the comparison I want to report. Planned outputs: papers, a public redacted copy of the code and preregistrations, and a planted-ground-truth benchmark.

## Champ 11 — date à mettre
« I applied to this program around 13 October 2026 … »

## À vérifier par Lazar
- Le CV v8 ne mentionne pas le doctorat à NeuroSpin ; la candidature le dit : mettre les deux d'accord (le formulaire demande un profil, pas le CV, mais un lecteur peut comparer).
- Le CV v8 revendique encore le lemme et le théorème négatif : à retirer d'une v9 du CV.
- L'aide de Claude : ne pas la cacher ; une phrase dans le champ 11 (« Drafted with help from Claude and edited by me ») est honnête et ne devrait pas desservir une demande faite à Anthropic.

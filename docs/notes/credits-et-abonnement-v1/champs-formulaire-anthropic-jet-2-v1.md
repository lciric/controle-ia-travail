# Formulaire d'accès des chercheurs externes d'Anthropic — jet 2 des champs 2, 6, 7, 11 et de l'expertise

- Date : 2026-11-22T10:45Z (`date -u`). Rédaction assistée (session fille, Claude Opus 5.5), pour Lazar, qui retravaille et envoie lui-même. Rien n'est envoyé.
- Remplace pour ces champs le jet 1 (`champs-formulaire-anthropic-jet-1-v1.md`, sha256 `e4024b43c4699ce1…`), qui reste tel quel. Le lien pré-rempli (`formulaire-anthropic-prerempli-v1.md`, `cb019d8ec3432e76…`) porte encore les anciens champs 6, 7 et 11 : à régénérer après la réécriture de Lazar.
- Matière : jet 1 ; demande v1 (`demande-credits-recherche-anthropic-v1.md`, `f64e56b05670b241…`) ; CV v8 (PDF du bloc-notes de la candidature Pivotal, `58c6e6ab32031677…`) et `reponses-formulaire-v8.md` du même dossier ; formulaire relevé (`docs/sources/credits-recherche-v1/formulaire-acces-chercheurs-externes-champs-v1.txt`, `382a45f3a2d3192f…`).
- Faits nouveaux intégrés : doctorat à NeuroSpin (CEA, Université Paris-Saclay) en partenariat avec l'ENS Paris-Saclay ; le contrôle des agents fait partie de la thèse (« part of », non « the subject ») ; accord du directeur de thèse ; première candidature vers le 13 octobre 2026 ; les deux publications ; aide de Claude déclarée au champ 11.
- Ne s'écrit plus : le lemme d'additivité et le théorème négatif (GO-2026-11-22-24). À la place, la phrase admise sur la loi en racine carrée, mise à la première personne (« I connect… » au lieu de « we connect… ») pour rester cohérente avec le reste du texte. Aucun chiffre de l'état de l'art.
- Style : phrases courtes, sans sigles internes, lisibles par un relecteur non spécialiste. Les textes à coller sont dans les blocs ; les décomptes de mots sont faits par programme (`wc -w` sur le texte exact du bloc).

## Champ 2 — Name of organization (if applicable) (facultatif, texte court)

```text
NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay
```

## Expertise en une phrase (25 mots)

Sert là où une version courte est demandée (profil, autres formulaires) ; le champ 6 ci-dessous la développe.

```text
Trained in physics, computational neuroscience and machine learning, with two peer-reviewed papers; I now study how language models behave and what their internal activations reveal.
```

## Champ 6 — moins de 200 mots (194 mots)

« In less than 200 words, please provide a brief description of the individual applicant or team, including the relevant expertise. »

```text
I am a PhD student at NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay. Monitoring AI agents is part of my thesis, and my supervisor supports this application.

I trained in physics at ENS Paris-Saclay, in computational neuroscience at ENS Ulm, and in statistics and machine learning at Mines Paris-PSL. I have two peer-reviewed papers: one on activity in spiking neural networks (Cimeša, Ciric & Ostojic, PLOS Computational Biology, 2023), and one from an internship at IBM Research Zurich on analog in-memory computing (Le Gallo, Nandakumar, Ciric et al., Neuromorphic Computing and Engineering, 2022).

In 2026 I moved to AI safety full time. Two results so far, on Llama-3.1-8B: sycophancy (yielding to social pressure) follows a simple law that predicts a second experiment without refitting (preprint, code and data public), and the direction a linear probe reads can carry less than 1% of the causal effect on the behaviour it tracks.

I do this work on my own, with Claude models as research assistants under written rules. Each experiment is preregistered and sealed with a hash before I read any result. A different model reviews each design. Claims that fail stay on record.
```

La ligne « Profile: github.com/lciric » du jet 1 est retirée : le champ 10 demande ce lien à part.

## Champ 7 — moins de 300 mots (293 mots)

« In less than 300 words, please describe your research or request for free API credits, making sure to explain: the topic of the project or research; why free API credits are important for your team to complete this research/project »

```text
Topic. My thesis asks whether reading an AI agent's internal activations helps catch sabotage spread thinly over a long task. Each step looks reasonable on its own; only the total damage shows. A monitor reading only the text may miss it.

I compare simple probes on the agent's activations with strong text-only monitors, such as LLM judges. I use open-weight models, so I can read their activations, and I plant the damage myself, so I know the ground truth. One kind of sabotage is kept out of monitor design, with results reported for each kind. Random audits remain the main safeguard; probes are tested as a guide to where to audit, not as a guarantee. I also connect a known result from steganography and nuclear safeguards (a square-root law for how much damage can hide when it is spread thin) to the monitoring of AI agents, and test where it holds on probe scores.

A second line asks how far LLM judges of automated research can be trusted under attack. Several models propose and criticise ideas, scored against planted ground truth rather than a judge's opinion.

How Claude is used. Through the API, Claude helps design and review experiments, judges episodes, proposes and criticises ideas, and reviews code. Each call is logged with model, settings and token counts.

Why credits matter. My lab has no budget for API use on this project. One reduced ideation campaign with Claude as proposer costs an estimated 700 to 1,500 USD. A failed design must be redesigned and rerun, so I expect two or three campaigns over six months. Without credits I would cut replications or switch to cheaper models, which weakens the comparison. Outputs: papers, public code and preregistrations, and a benchmark with planted ground truth.
```

## Champ 11 — Additional Information (facultatif, sans limite écrite ; 114 mots)

```text
I first applied to this program around 13 October 2026 and am sending an updated application, as your help page suggests. This work is part of my PhD at NeuroSpin, and my supervisor supports the application. I do not ask for any exemption from the Usage Policy. Some prompts in this research describe sabotage strategies for test agents built on open-weight models. This is defensive research on monitoring; these prompts are logged, and the experiments that use them are preregistered. I also have a Claude Ultra subscription linked to the same Console organization. Research credits would pay for the logged API calls used in measurements. Drafted with help from Claude and edited by me.
```

## À vérifier par Lazar avant d'envoyer

1. « My lab has no budget for API use on this project » (champ 7) : à confirmer ou à remplacer ; le jet 1 disait « not funded beyond my own resources », écrit avant le fait du doctorat.
2. « In 2026 I moved to AI safety full time » (champ 6) : le CV v8 dit « full time since March » ; à accorder avec la date d'inscription en thèse si un relecteur compare.
3. Le CV v8 ne mentionne pas le doctorat et revendique encore le lemme et le théorème négatif (puces « Against a threat spread over many actions… » et le résumé du haut) : à corriger dans une v9 avant tout envoi qui joint le CV.
4. « Each call is logged with model, settings and token counts » : vrai pour les appels par l'interface journalisés par nos outils ; si une partie de la mesure passe sous l'abonnement (GO-2026-11-22-32), elle n'est pas journalisée de la même façon. Le champ 11 dit que les crédits paieraient les appels journalisés : c'est cohérent.
5. Montant (champ 8) : inchangé depuis la v1 (« Other : 3000 » recommandé, ou « No » pour la voie ordinaire de 1 000 USD).

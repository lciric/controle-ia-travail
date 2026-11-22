# Demande au programme « AI for Science » d'Anthropic, champ par champ (version 3)

- Date : 2026-11-22T12:55Z (`date -u`). Rédaction assistée (session fille, Claude Opus 5.5), pour Lazar, qui relit et envoie lui-même. Rien n'est envoyé ; aucun formulaire n'est rempli en ligne ; personne n'est contacté.
- Remplace `demande-ai-for-science-anthropic-v2.md` (sha256 `e9795989cef8207d…`), qui reste tel quel. Changements, sur les réponses du directeur du 22 novembre : **le champ de l'adresse du responsable est laissé vide** (Lazar ne veut pas que son responsable soit contacté) ; aucun accord des directeurs n'est plus affirmé ; le sujet de thèse entre au champ « Research team » et au champ libre (« thesis on brain networks involved in mathematics and their educational and genetic correlates », projet MathBrain financé par l'ERC) ; « Part of my thesis asks whether » devient « This project asks whether », et le projet est dit mené « alongside my PhD », « not my thesis topic » ; le champ libre porte un crochet pour la phrase sur l'accord du responsable (phrase A ou B). Le reste est inchangé depuis la v2.
- **Recommandation : ne pas déposer en l'état.** Déposer d'abord au programme des chercheurs externes ; pour celui-ci, écrire d'abord à Anthropic. Raisons, textes relevés et courriel proposé : question 3 des « Questions du directeur » de `champs-formulaire-anthropic-jet-4-v1.md`.
- Lien prérempli de ce formulaire (sans l'adresse du responsable) : `formulaire-anthropic-prerempli-v3.md`.
- **Formulaire relevé** : `docs/sources/credits-recherche-v1/formulaire-ia-pour-la-science-champs-v1.txt` (`7de3104da671c236…`) ; identifiants des champs relus par programme dans le HTML d'origine (`formulaire-ia-pour-la-science-v1.html`, `5338d387ff09eff3…`). Adresse : https://docs.google.com/forms/d/e/1FAIpQLSfwDGfVg2lHJ0cc0oF_ilEnjvr_r4_paYi7VLlr5cLNXASdvA/viewform
- Style : phrases courtes, sans sigles internes. Décomptes par programme (`len(texte.split())`, comme `wc -w`) sur le texte exact de chaque bloc. Rien de confidentiel : le formulaire traite tout comme « non-confidential ».

## Ce qu'il faut savoir avant de remplir (inchangé depuis la v2, sauf le point 2)

1. **Adéquation.** Le programme vise les sciences de la nature et les mathématiques, « with a particular focus on biology and life sciences » ; la page d'aide range « Computer Science » parmi les champs soutenus, et l'annonce du 27 août l'ouvre « to researchers in other scientific fields ». La demande joue honnêtement le lien avec les neurosciences sans se dire biologie.
2. **Éligibilité et accords.** « All projects must have PI approval » ; « an email will be sent to your PI to acknowledge and approve the project » ; le règlement fait déclarer l'accord de l'employeur ou de l'établissement. Sans responsable joignable, la demande ne tient que si Lazar mène le projet lui-même et qu'Anthropic l'admet : question 3 de `champs-formulaire-anthropic-jet-4-v1.md`. Les textes d'accord du jet 3 ne servent plus.
3. **Nature des crédits.** Le formulaire : « extra usage credits, which can be used across all Claude.ai tools, including Claude Science. The maximum award for the AI for Science program is $50,000 in credits. » La page d'aide (plus ancienne) parle de crédits d'interface de programmation. La demande suit le formulaire. Non vérifié : que ces crédits servent aussi par l'interface de programmation.
4. **Calendrier.** « We evaluate submissions monthly » ; pas de réponse aux refus. Lauréats : enquêtes et entretiens de recherche (règlement).
5. **Connexion Google exigée** (le formulaire collecte l'adresse) : utiliser [COURRIEL ÉTABLISSEMENT] (« Please enter academic emails and credentials where possible »).

## Champ par champ (O = obligatoire, F = facultatif)

**Email (O)** — collecté par le compte Google connecté : [COURRIEL ÉTABLISSEMENT]

**Which program are you applying to? (O)** — `Standard AI for Science program`. La page « Rare disease program » ne concerne pas cette demande.

**Name of primary contact (O)**
```text
Lazar Ciric
```

**Name of organization or research institution (O)**
```text
NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay
```

**Position or title at organization (O)**
```text
PhD student
```

**What is your PI's academic or organization email address? (F)** — **laissé vide** dans ce jet et dans le lien prérempli. Ne pas y mettre l'adresse d'un directeur (Lazar ne veut pas qu'il soit contacté), ni celle d'une personne qui appuie la demande sans diriger le projet (Thomas Romary compris) : Anthropic écrit à cette adresse pour faire approuver le projet. Seul cas où le remplir : Anthropic admet par écrit que Lazar se déclare responsable ; il y met alors sa propre adresse (phrase A). Détail : question 3 du jet 4.

**Website of organization or research group, link to Google Scholar or GitHub (O)**
```text
https://github.com/lciric
```
(ou [PAGE DE L'ÉQUIPE À NEUROSPIN], si elle existe et te nomme)

**Where did you hear about this program? (F)**
```text
Anthropic's announcement of 27 August 2026 and the Claude help center.
```

**Project title (O)**
```text
Reading an AI agent's internal activations to catch sabotage spread over long tasks
```

**Scientific field(s) (O, cases à cocher)** — cocher seulement la case libre :
```text
Computer science (AI safety)
```

**Which Organization ID would you like the credits applied to? (O)** — aide : « claude.ai > accounts > settings ».
```text
[IDENTIFIANT D'ORGANISATION DU COMPTE CLAUDE.AI]
```

**What type of Claude.ai account do you have? (F)** — « Ultra » n'est pas dans la liste : case libre.
```text
Ultra
```

**Research team — in fewer than 100 words (O)** (94 mots)
```text
Lazar Ciric, PhD student since September 2023 at NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay; thesis on brain networks involved in mathematics and their educational and genetic correlates (ERC-funded MathBrain project). Background in physics, computational neuroscience, and statistics and machine learning; two peer-reviewed papers (PLOS Computational Biology 2023; Neuromorphic Computing and Engineering 2022). AI experience: linear probes, steering and ablation on 8-billion-parameter open-weight models; a preregistered study of sycophancy in Llama-3.1-8B (public preprint); a multi-model system that proposes and tests research ideas. Lazar is the main user of Claude on the project.
```

**Links to Google Scholar profiles or other profiles of key team members (F)**
```text
https://github.com/lciric ; preprint, code and data: https://github.com/lciric/sycophancy-psychophysical-law
```

**Research proposal — in fewer than 500 words (O)** (468 mots)
```text
Scientific question. AI agents now carry out long research and analysis tasks. An agent that is misaligned, or has been tampered with, need not do anything visibly wrong. It can spoil the result a little at each step, so that every step looks honest and only the total damage shows. Monitors that read the agent's text may miss this. Neuroscience suggests another route: read the internal activity of the system, not only its output. This project asks whether reading an agent's internal activations helps catch this kind of diffuse sabotage, and how much it adds over strong monitors that read only text. The project is new: it started in October 2026, alongside my PhD.

Methodology. I build test agents on open-weight models (Llama-3.1-8B and similar), whose activations I can record. The agents do long tasks either honestly or with sabotage that I plant, so the ground truth is known. I train simple linear probes on their activations and compare them with text-only monitors: LLM judges, statistics on words and cost, and combinations of these. One kind of sabotage is kept out of the design of the monitors and used only at test time; results are reported for each kind separately. Random audits stay the main safeguard, and probes are tested as a guide to where audits should go, not as a guarantee. I also connect a known result from steganography and nuclear safeguards (a square-root law for how much damage can hide when it is spread thin) to the monitoring of AI agents, and test where it holds on probe scores.

A second line asks how far LLM judges of automated research can be trusted under attack. Several models propose and criticise ideas, which are scored against planted ground truth and cost, never against a judge's opinion.

Every decisive experiment is preregistered: hypothesis, predicted sign, metric, threshold and analysis plan are written down and sealed with a SHA-256 hash before any result is read. A different model reviews each design, and an independent reviewer applies the sealed criteria to give the verdict. Negative results are reported with the same care as positive ones.

Expected outcomes and deliverables. (1) A measured answer, for each kind of sabotage, to whether activation probes beat strong text-only monitors at the same false-alarm rate on honest agents. A clear negative answer is also useful: it tells developers where not to invest. (2) A benchmark of agent episodes with planted ground truth, released after the held-out evaluation. (3) Papers, with a public copy of the code and preregistrations.

Timeline (six months). Month 1: calibrate the test agents and the text-only baselines. Months 2 to 4: the sealed comparison of probes and baselines, kind by kind, held-out kind included. Months 3 to 5: ideation campaigns on judges under attack. Month 6: papers and public release.
```

**How specifically will Claude's capabilities be used… (200 words max) (O)** (183 mots, inchangé)
```text
Claude works inside the research workflow, in fixed roles. Claude Fable designs experiments and writes preregistrations. A different model, Claude Opus, reviews each design and writes and checks the code. Both work mainly in Claude Code sessions on the project repository, where they read the sealed files, run the tests and propose changes that I approve. Through the API, Claude also judges agent episodes as one of the text-only monitors, and acts as proposer and critic in the ideation system.

This speeds up the work in three ways. First, one researcher can run a protocol that would normally need a small team: design, independent review, coding and auditing are done by separate model instances, each given only the files it needs. Second, Claude writes and checks the analysis code and its tests, so I can spend my time on the scientific questions. Third, Claude as a judge is a strong text-only monitor, so it is a demanding baseline to beat.

Each API call is logged with the model, settings and token counts, so every reported number can be traced to a sealed file.
```

**Potential scientific impact if successful (200 words max) (O)** (117 mots, inchangé)
```text
If probes on internal activations catch diffuse sabotage better than strong text-only monitors, developers who deploy research agents gain a cheap tool to decide where human audits should go. If they do not, a preregistered negative result with known ground truth tells the field where not to invest, which is just as useful. Either way, the benchmark and the sealed protocol can be reused by others to test new monitors.

The work also brings a method from neuroscience, reading the activity of many units to infer what a system is doing, to a new kind of system. It tests how far that reading can be trusted when the system may be trying to hide what it does.
```

**Applications beyond pure scientific discovery (200 words max) (O)** (94 mots, inchangé)
```text
Yes. AI agents are starting to run analyses and experiments with little human checking. The direct application is oversight of such agents: deciding where to audit, with a published floor of random audits, and knowing which monitors can be trusted. The second line of work applies to automated science itself: if AI systems judge research produced by other AI systems, we need to know when those judges can be fooled. The public benchmark and code let other groups, including those building AI tools for science, test their own monitors on the same ground truth.
```

**How will you measure the success of using Claude? (100 words max) (O)** (72 mots, inchangé)
```text
(1) The decisive comparison is run as preregistered, and an independent reviewer issues its verdict, whatever its sign. (2) Detection rates are reported for each kind of sabotage, held-out kind included, at a fixed false-alarm rate on honest agents. (3) Ideation results are scored against planted ground truth and cost, never against a model's opinion. (4) The benchmark and code are public. (5) Every reported number traces back to a sealed file.
```

**How much money in extra usage credits do you anticipate you will need? (O)** (113 mots ; pas de limite écrite ; plafond du programme : 50 000 USD)
```text
I request [MONTANT] USD in extra usage credits over six months. The project is new and does not yet have its own funding; grant applications are in progress. The estimate comes from my own cost records: two or three ideation campaigns with Claude as proposer, at an estimated 700 to 1,500 USD each; Claude as a judge in the main comparison; and the Claude Code sessions in which experiments are designed, reviewed and coded. If these credits cannot be used through the API, I would run those parts in Claude Code. Without credits I would run fewer replications or replace Claude with cheaper models in the comparisons, which would weaken the main result.
```
[MONTANT] : à fixer par Lazar (bases écrites dans la v1 : 700 à 1 500 USD par campagne réduite, deux ou trois campagnes ; la part des sessions de Claude Code n'est chiffrée nulle part : la lire dans l'usage réel du compte).

**Biosecurity — does your research involve any of the following? (O)** — `None of the above` ; le champ d'explication qui suit reste vide.

**Is there anything else you would like the review committee to know? (F)** (137 mots)
```text
I am a PhD student at NeuroSpin. My thesis, within the ERC-funded MathBrain project, is on brain networks involved in mathematics; this AI-safety project runs alongside it and is not my thesis topic. On PI approval: [PHRASE SELON L'OPTION RETENUE, voir la question 3 des « Questions du directeur »]. I have also applied to Anthropic's External Researcher Access Program for API credits for the same research; if both are granted, they would fund different parts of the work and I would say so in any report. I do not ask for any exemption from the Usage Policy. Some prompts describe sabotage strategies for test agents built on open-weight models. This is defensive research on monitoring: these prompts are logged, and the experiments that use them are preregistered. Drafted with help from Claude and edited by me.
```
Crochet « On PI approval: […] » : à remplacer par la phrase A ou la phrase B de la question 3 du jet 4 (texte anglais prêt), selon la réponse d'Anthropic. Phrase sur la double demande : à garder si Lazar dépose aussi au programme des chercheurs externes ; à retirer sinon. Si Thomas Romary l'accepte par écrit, ajouter à la fin l'une des phrases de référence de `courriel-thomas-romary-v1.md`.

**Terms of Service (O)** — case `I agree`, à cocher par Lazar lui-même (non pré-cochée dans le lien).

## Réserves

- Crochets que seul Lazar peut remplir : [COURRIEL ÉTABLISSEMENT], [IDENTIFIANT D'ORGANISATION DU COMPTE CLAUDE.AI], [MONTANT], le crochet du champ libre sur l'accord du responsable, éventuellement [PAGE DE L'ÉQUIPE À NEUROSPIN].
- « alongside my PhD », « not my thesis topic » : à confirmer par Lazar (question 1 du jet 4).
- Règle d'éligibilité : en indiquant NeuroSpin comme organisation, Lazar déclare avoir les accords nécessaires de son employeur et de son établissement. Lesquels le sont dépend de son contrat ; ne cocher « I agree » qu'en les ayant.
- « public preprint » (« Research team ») : le CV v18 dit « Manuscript in preparation » ; garder la formule juste.
- Rôles de Claude décrits d'après les règles du dépôt (Fable conçoit, Opus contre-lit et code). Si Lazar préfère ne pas nommer les modèles : « one Claude model » et « a different Claude model ».
- Le calendrier en six mois est une proposition de forme ; il ne vaut pas engagement au sens des portes du programme.
- Après remplissage des crochets, refaire les décomptes.

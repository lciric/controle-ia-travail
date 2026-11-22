# Demande au programme « AI for Science » d'Anthropic, champ par champ (version 1)

- Date : 2026-11-22T10:45Z (`date -u`). Rédaction assistée (session fille, Claude Opus 5.5), pour Lazar, qui retravaille et envoie lui-même. Rien n'est envoyé.
- Remplace l'annexe « AI for Science » de `demande-credits-recherche-anthropic-v1.md` (`f64e56b05670b241…`), écrite quand l'affiliation n'était pas connue ; cette annexe reste telle quelle.
- **Formulaire relevé** : oui. Champs, ordre, limites et options relevés dans le HTML du formulaire Google : `docs/sources/credits-recherche-v1/formulaire-ia-pour-la-science-champs-v1.txt` (sha256 `7de3104da671c236…`) ; adresse : https://docs.google.com/forms/d/e/1FAIpQLSfwDGfVg2lHJ0cc0oF_ilEnjvr_r4_paYi7VLlr5cLNXASdvA/viewform (empreinte du HTML d'origine dans `docs/sources/credits-recherche-v1/LISEZMOI-v1.md`, `8a07b7b9ecb5f02a…`).
- Autres sources lues (même dossier) : page d'aide du programme (datée du 16 mars 2026), annonce du 27 août 2026 (« Expanding our support for scientists »), règlement (« Last updated Oct 20, 2026 »).
- Style : phrases courtes, sans sigles internes, lisibles par un relecteur non spécialiste. Textes à coller dans les blocs ; décomptes par programme (`wc -w` sur le texte exact du bloc). Rien de confidentiel : le formulaire traite tout comme « non-confidential » (aucun mode tenu à l'écart nommé, aucune loi plantée, aucun extrait de préenregistrement).

## Ce qu'il faut savoir avant de remplir

1. **Adéquation.** Le programme vise les sciences de la nature et les mathématiques, « with a particular focus on biology and life sciences », mais la page d'aide range « Computer Science » parmi les champs soutenus, et l'annonce du 27 août l'ouvre « to researchers in other scientific fields ». La demande joue honnêtement le lien avec les neurosciences (lire l'activité interne d'un système, méthode de NeuroSpin) sans se dire biologie.
2. **Éligibilité.** Le formulaire vise « qualified nonprofit and academic researchers » et demande l'accord du responsable du projet : « All projects must have PI approval. If you are not the PI, please provide your PI's email address » ; « an email will be sent to your PI to acknowledge and approve the project ». Le règlement ajoute : « If you are employed by a legal entity or affiliated with a university or other research institution, then you represent and warrant that you have obtained all consents from that employer or institution ». L'accord du directeur de thèse ([NOM DU DIRECTEUR]) couvre le premier point ; **à vérifier avec lui** si le laboratoire ou l'établissement demande en plus son propre accord.
3. **Nature des crédits : deux textes divergent.** La page d'aide (16 mars) : « free API credits », « up to $20,000 in API credits to your account for a 6-month period », « these credits are for API use and do not apply to the Claude web app ». Le formulaire (plus récent, comme l'annonce du 27 août) : « extra usage credits, which can be used across all Claude.ai tools, including Claude Science. The maximum award for the AI for Science program is $50,000 in credits. » et, pour l'identifiant, « this can be found under claude.ai > accounts > settings ». La demande suit le formulaire : les crédits iraient au compte claude.ai (abonnement Ultra), donc d'abord aux sessions de Claude Code. Non vérifié : qu'ils servent aussi par l'interface de programmation.
4. **Calendrier.** « We evaluate submissions monthly » ; pas de réponse individuelle aux refus. Lauréats : « Selected Researchers will participate in research surveys and interviews » (règlement).
5. **Connexion Google** exigée (champ « Email » collecté) : utiliser [COURRIEL ÉTABLISSEMENT] (« Please enter academic emails and credentials where possible »).

## Champ par champ (O = obligatoire, F = facultatif)

**Email (O)** — collecté par le compte Google connecté : [COURRIEL ÉTABLISSEMENT]

**Which program are you applying to? (O)** — une seule option : `Standard AI for Science program`. La page « Rare disease program » qui suit dans le formulaire ne concerne pas cette demande.

**Name of primary contact (O)**
```text
Lazar Ciric
```

**Name of organization or research institution (O)**
```text
NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay
```

**Position or title at organization (O)** — aide du champ : « All projects must have PI approval ».
```text
PhD student
```

**What is your PI's academic or organization email address? (F, à remplir)** — c'est l'adresse qui recevra le courriel d'approbation.
```text
[COURRIEL DU DIRECTEUR]
```

**Website of organization or research group, link to Google Scholar or GitHub (O)**
```text
https://github.com/lciric
```
(ou [PAGE DE L'ÉQUIPE À NEUROSPIN] si elle existe et te nomme)

**Where did you hear about this program? (F)**
```text
Anthropic's announcement of 27 August 2026 and the Claude help center.
```

**Project title (O)**
```text
Reading an AI agent's internal activations to catch sabotage spread over long tasks
```

**Scientific field(s) (O, cases à cocher)** — options : Biology / Life Sciences, Chemistry, Medicine/Healthcare, Environmental Science, Physics, Earth Science, Math, et une case libre. Cocher la case libre :
```text
Computer science (AI safety)
```
Ne pas cocher « Biology / Life Sciences » : le projet n'en est pas. « Math » seulement si tu veux mettre en avant la partie statistique.

**Which Organization ID would you like the credits applied to? (O)** — aide : « claude.ai > accounts > settings ».
```text
[IDENTIFIANT D'ORGANISATION DU COMPTE CLAUDE.AI]
```
Non vérifié : si c'est le même identifiant que celui de la console (formulaire des chercheurs externes). Le relever là où l'aide l'indique.

**What type of Claude.ai account do you have? (F)** — options : Free, Pro/Max, Teams plan, Enterprise plan, et une case libre. « Ultra » n'est pas dans la liste : case libre.
```text
Ultra
```

**Research team — in fewer than 100 words (O)** (84 mots) — « Please list the key team members who will be using Claude for this research. »
```text
Lazar Ciric, PhD student at NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay, supervised by [NOM DU DIRECTEUR], who approves this project. Background in physics, computational neuroscience, and statistics and machine learning; two peer-reviewed papers (PLOS Computational Biology 2023; Neuromorphic Computing and Engineering 2022). AI experience: linear probes, steering and ablation on 8-billion-parameter open-weight models; a preregistered study of sycophancy in Llama-3.1-8B (public preprint); a multi-model system that proposes and tests research ideas. Lazar is the main user of Claude on the project.
```

**Links to Google Scholar profiles or other profiles of key team members (F)**
```text
https://github.com/lciric ; preprint, code and data: https://github.com/lciric/sycophancy-psychophysical-law ; [PROFIL SCHOLAR, s'il existe]
```

**Research proposal — in fewer than 500 words: question, method, outcomes, timeline (O)** (456 mots) — aide : « We encourage you to propose projects with a timeline of approximately 6 months. »
```text
Scientific question. AI agents now carry out long research and analysis tasks. An agent that is misaligned, or has been tampered with, need not do anything visibly wrong. It can spoil the result a little at each step, so that every step looks honest and only the total damage shows. Monitors that read the agent's text may miss this. Neuroscience suggests another route: read the internal activity of the system, not only its output. My thesis asks whether reading an agent's internal activations helps catch this kind of diffuse sabotage, and how much it adds over strong monitors that read only text.

Methodology. I build test agents on open-weight models (Llama-3.1-8B and similar), whose activations I can record. The agents do long tasks either honestly or with sabotage that I plant, so the ground truth is known. I train simple linear probes on their activations and compare them with text-only monitors: LLM judges, statistics on words and cost, and combinations of these. One kind of sabotage is kept out of the design of the monitors and used only at test time; results are reported for each kind separately. Random audits stay the main safeguard, and probes are tested as a guide to where audits should go, not as a guarantee. I also connect a known result from steganography and nuclear safeguards (a square-root law for how much damage can hide when it is spread thin) to the monitoring of AI agents, and test where it holds on probe scores.

A second line asks how far LLM judges of automated research can be trusted under attack. Several models propose and criticise ideas, which are scored against planted ground truth and cost, never against a judge's opinion.

Every decisive experiment is preregistered: hypothesis, predicted sign, metric, threshold and analysis plan are written down and sealed with a SHA-256 hash before any result is read. A different model reviews each design, and an independent reviewer applies the sealed criteria to give the verdict. Negative results are reported with the same care as positive ones.

Expected outcomes and deliverables. (1) A measured answer, for each kind of sabotage, to whether activation probes beat strong text-only monitors at the same false-alarm rate on honest agents. A clear negative answer is also useful: it tells developers where not to invest. (2) A benchmark of agent episodes with planted ground truth, released after the held-out evaluation. (3) Papers, with a public copy of the code and preregistrations.

Timeline (six months). Month 1: calibrate the test agents and the text-only baselines. Months 2 to 4: the sealed comparison of probes and baselines, kind by kind, held-out kind included. Months 3 to 5: ideation campaigns on judges under attack. Month 6: papers and public release.
```

**How specifically will Claude's capabilities be used… (200 words max) (O)** (183 mots)
```text
Claude works inside the research workflow, in fixed roles. Claude Fable designs experiments and writes preregistrations. A different model, Claude Opus, reviews each design and writes and checks the code. Both work mainly in Claude Code sessions on the project repository, where they read the sealed files, run the tests and propose changes that I approve. Through the API, Claude also judges agent episodes as one of the text-only monitors, and acts as proposer and critic in the ideation system.

This speeds up the work in three ways. First, one researcher can run a protocol that would normally need a small team: design, independent review, coding and auditing are done by separate model instances, each given only the files it needs. Second, Claude writes and checks the analysis code and its tests, so I can spend my time on the scientific questions. Third, Claude as a judge is a strong text-only monitor, so it is a demanding baseline to beat.

Each API call is logged with the model, settings and token counts, so every reported number can be traced to a sealed file.
```

**Potential scientific impact if successful (200 words max) (O)** (117 mots)
```text
If probes on internal activations catch diffuse sabotage better than strong text-only monitors, developers who deploy research agents gain a cheap tool to decide where human audits should go. If they do not, a preregistered negative result with known ground truth tells the field where not to invest, which is just as useful. Either way, the benchmark and the sealed protocol can be reused by others to test new monitors.

The work also brings a method from neuroscience, reading the activity of many units to infer what a system is doing, to a new kind of system. It tests how far that reading can be trusted when the system may be trying to hide what it does.
```

**Applications beyond pure scientific discovery (200 words max) (O)** (94 mots)
```text
Yes. AI agents are starting to run analyses and experiments with little human checking. The direct application is oversight of such agents: deciding where to audit, with a published floor of random audits, and knowing which monitors can be trusted. The second line of work applies to automated science itself: if AI systems judge research produced by other AI systems, we need to know when those judges can be fooled. The public benchmark and code let other groups, including those building AI tools for science, test their own monitors on the same ground truth.
```

**How will you measure the success of using Claude? Specific metrics or objectives (100 words max) (O)** (72 mots)
```text
(1) The decisive comparison is run as preregistered, and an independent reviewer issues its verdict, whatever its sign. (2) Detection rates are reported for each kind of sabotage, held-out kind included, at a fixed false-alarm rate on honest agents. (3) Ideation results are scored against planted ground truth and cost, never against a model's opinion. (4) The benchmark and code are public. (5) Every reported number traces back to a sealed file.
```

**How much money in extra usage credits do you anticipate you will need? (O)** (96 mots ; pas de limite écrite) — aide : « The maximum award for the AI for Science program is $50,000 in credits. »
```text
I request [MONTANT] USD in extra usage credits over six months. The estimate comes from my own cost records: two or three ideation campaigns with Claude as proposer, at an estimated 700 to 1,500 USD each; Claude as a judge in the main comparison; and the Claude Code sessions in which experiments are designed, reviewed and coded. If these credits cannot be used through the API, I would run those parts in Claude Code. Without credits I would run fewer replications or replace Claude with cheaper models in the comparisons, which would weaken the main result.
```
[MONTANT] : à fixer par Lazar. Bases écrites : 700 à 1 500 USD par campagne réduite de l'organisme d'idéation avec Claude comme proposeur, deux ou trois campagnes (devis interne cité dans `resume-programme-pour-demandes-v1.md`, `b7e0f4245e0bc3d0…`) ; la v1 proposait 5 000 USD sur six mois. La part des sessions de Claude Code n'est chiffrée nulle part dans les registres : la lire dans l'usage réel du compte avant d'ajouter une somme. Ordre de grandeur, pas un devis.

**Biosecurity — does your research involve any of the following? (O)** — options : Pathogen research or virology, Drug resistance studies, Toxicology, Synthetic biology, None of the above.
```text
None of the above
```
Le champ d'explication qui suit (F) reste vide.

**Is there anything else you would like the review committee to know? (F)** (110 mots)
```text
This project is part of my PhD at NeuroSpin and has the approval of my thesis supervisor, [NOM DU DIRECTEUR] ([COURRIEL DU DIRECTEUR]). I have also applied to Anthropic's External Researcher Access Program for API credits for the same research; if both are granted, they would fund different parts of the work and I would say so in any report. I do not ask for any exemption from the Usage Policy. Some prompts describe sabotage strategies for test agents built on open-weight models. This is defensive research on monitoring: these prompts are logged, and the experiments that use them are preregistered. Drafted with help from Claude and edited by me.
```
Phrase sur la double demande : à garder si Lazar dépose aussi au programme des chercheurs externes (recommandé, par transparence) ; à retirer sinon.

**Terms of Service (O)** — case `I agree` (le texte renvoie au règlement du programme et à la politique de confidentialité).

## Réserves

- Les crochets ne peuvent être remplis que par Lazar : [COURRIEL ÉTABLISSEMENT] (adresse en @ens-paris-saclay.fr), [NOM DU DIRECTEUR], [COURRIEL DU DIRECTEUR], [IDENTIFIANT D'ORGANISATION DU COMPTE CLAUDE.AI], [MONTANT], éventuellement [PAGE DE L'ÉQUIPE À NEUROSPIN] et [PROFIL SCHOLAR].
- Rôles de Claude décrits d'après les règles du dépôt (CLAUDE.md, « Qui conçoit » et « Économie de Fable ») : Fable conçoit et écrit les préenregistrements, Opus contre-lit et écrit le code. Si Lazar préfère ne pas nommer les modèles, écrire « one Claude model » et « a different Claude model ».
- Le calendrier en six mois est une proposition de forme (le formulaire en demande un) ; il ne vaut pas engagement au sens des portes du programme.
- Après remplissage des crochets, refaire les décomptes sous les limites.

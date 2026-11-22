# Formulaire d'accès des chercheurs externes d'Anthropic : jet 3 des champs, et questions du directeur

- Date : 2026-11-22T12:16Z (`date -u`). Rédaction assistée (session fille, Claude Opus 5.5), pour Lazar, qui relit et envoie lui-même. Rien n'est envoyé ; aucun formulaire n'est rempli en ligne.
- Remplace pour ces champs le jet 2 (`champs-formulaire-anthropic-jet-2-v1.md`, sha256 `90538b526e4b2d3c…`), qui reste tel quel. Pièces sœurs du jet 3 : `demande-ai-for-science-anthropic-v2.md`, `demandes-credits-nuage-v3.md`, `formulaire-anthropic-prerempli-v2.md` (liens préremplis), CV v9 dans `cv-v9/`.
- Formulaire relevé : `docs/sources/credits-recherche-v1/formulaire-acces-chercheurs-externes-champs-v1.txt` ; identifiants des champs relus par programme dans le HTML d'origine (`formulaire-acces-chercheurs-externes-v1.html`, `802ec3b007cedd4a…`).

## Ce qui change depuis le jet 2 (réponses du directeur du 22 novembre)

1. **Phrase inexacte retirée.** La phrase du champ 7 du jet 2 sur l'absence de budget du laboratoire n'est plus écrite, ni citée, dans aucun fichier du jet 3 (vérifié par programme à la génération). À la place, au champ 7 : « The project is new and has no funding of its own yet; grant applications are in progress. » La même idée, avec les mêmes mots ou presque, figure dans la demande « AI for Science » (champ du montant) et dans les demandes à Amazon et à Google.
2. **Amazon** : demande réajustée sur un projet neuf, à son début, avec le banc public et son harnais comme livrable borné (`demandes-credits-nuage-v3.md`).
3. **Thèse** : depuis septembre 2023 à NeuroSpin, sous la direction de Stanislas Dehaene et Cathy Philippe, en partenariat avec l'ENS Paris-Saclay. Intégrée ici aux champs 6 et 11, au champ « Research team » et au champ libre d'« AI for Science », aux propositions d'Amazon et de Google, et au CV v9.
4. et 5. Réponses dans la section « Questions du directeur » ci-dessous.
- **Corrigé au passage, par cohérence avec les faits admis :**
  - « My thesis asks whether… » (champ 7 du jet 2, proposition d'« AI for Science » v1) faisait du contrôle des agents le sujet de la thèse ; le fait admis est « fait partie de ». Écrit maintenant : « Part of my thesis asks whether… ».
  - « In 2026 I moved to AI safety full time » (champ 6) heurtait une thèse commencée en 2023. Remplacé par « Since 2025 I have also worked on AI safety », d'après le CV v8 (« 2025 (alongside my consulting role) »).
  - « I do this work on my own » retiré : le travail est encadré.
- **Toujours pas écrit** : le lemme d'additivité et le théorème négatif comme résultats (GO-2026-11-22-24). La phrase admise sur la loi en racine carrée reste telle quelle.
- **Décomptes** : par programme, `len(texte.split())` (même règle que `wc -w`) sur le texte exact de chaque bloc ; table complète en fin de fichier.

## Champs du formulaire

**Champ 1 — Name of primary contact (O)**
```text
Lazar Ciric
```

**Champ 2 — Name of organization (if applicable) (F)**
```text
NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay
```

**Champ 3 — Have you been recommended to this form by an Anthropic employee? (O)** : `No`. **Champ 4** (nom de l'employé) : vide.

**Champ 5 — Which Organization ID would you like the credits applied to? (O)** : `[ID ORGANISATION CONSOLE]`, l'organisation de la console déjà liée à l'abonnement Ultra (console.anthropic.com/settings/organization).

**Expertise en une phrase (30 mots)** — pour les endroits où une version courte est demandée ; le champ 6 la développe.
```text
PhD student at NeuroSpin since 2023, trained in physics, computational neuroscience and machine learning, with two peer-reviewed papers; I study how language models behave and what their internal activations reveal.
```

**Champ 6 — « In less than 200 words, please provide a brief description of the individual applicant or team, including the relevant expertise. » (195 mots)**
```text
I am a PhD student at NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay. I started in September 2023, supervised by Stanislas Dehaene and Cathy Philippe. Monitoring AI agents is part of my thesis, and my supervisors support this application.

I trained in physics at ENS Paris-Saclay, in computational neuroscience at ENS Ulm, and in statistics and machine learning at Mines Paris-PSL. I have two peer-reviewed papers: one on activity in spiking neural networks (Cimeša, Ciric & Ostojic, PLOS Computational Biology, 2023), and one from an internship at IBM Research Zurich on analog in-memory computing (Le Gallo, Nandakumar, Ciric et al., Neuromorphic Computing and Engineering, 2022).

Since 2025 I have also worked on AI safety. Two results on Llama-3.1-8B: sycophancy follows a simple law that predicts a second experiment without refitting (preprint, code and data public), and the direction a linear probe reads can carry less than 1% of the causal effect on the behaviour it tracks.

I work with Claude models as research assistants under written rules. Each experiment is preregistered and sealed with a hash before I read any result. A different model reviews each design. Claims that fail stay on record.
```

**Champ 7 — « In less than 300 words, please describe your research or request for free API credits… » (297 mots)**
```text
Topic. Part of my thesis asks whether reading an AI agent's internal activations helps catch sabotage spread thinly over a long task. Each step looks reasonable on its own; only the total damage shows. A monitor reading only the text may miss it.

I compare probes on the agent's activations with strong text-only monitors, such as LLM judges. I use open-weight models, so I can read their activations, and I plant the damage, so I know the ground truth. One kind of sabotage is kept out of monitor design, with results reported for each kind. Random audits remain the main safeguard; probes are tested as a guide to where to audit, not as a guarantee. I also connect a known result from steganography and nuclear safeguards (a square-root law for how much damage can hide when it is spread thin) to the monitoring of AI agents, and test where it holds on probe scores.

A second line asks how far LLM judges of automated research can be trusted under attack. Several models propose and criticise ideas, scored against planted ground truth rather than a judge's opinion.

How Claude is used. Through the API, Claude helps design and review experiments, judges episodes, proposes and criticises ideas, and reviews code. Each call is logged with model, settings and token counts.

Why credits matter. The project is new and has no funding of its own yet; grant applications are in progress. One reduced ideation campaign with Claude as proposer costs an estimated 700 to 1,500 USD. A failed design must be redesigned and rerun, so I expect two or three campaigns over six months. Without credits I would cut replications or switch to cheaper models, which weakens the comparison. Outputs: papers, public code, and a benchmark with planted ground truth.
```

**Champ 8 — Are you requesting more than $1000 API credits? (O)** : inchangé depuis la v1 : `Other` avec `3000` (recommandé), ou `No` pour la voie ordinaire de 1 000 USD.

**Champ 9 — quality of service (F)** : `I'm fine with receiving a low quality of service`.

**Champ 10 — link to your Google Scholar profile or github profile (O)**
```text
https://github.com/lciric
```

**Champ 11 — Additional Information (F, sans limite écrite ; 119 mots)**
```text
I first applied to this program around 13 October 2026 and am sending an updated application, as your help page suggests. This work is part of my PhD at NeuroSpin, supervised by Stanislas Dehaene and Cathy Philippe, who support the application. I do not ask for any exemption from the Usage Policy. Some prompts in this research describe sabotage strategies for test agents built on open-weight models. This is defensive research on monitoring; these prompts are logged, and the experiments that use them are preregistered. I also have a Claude Ultra subscription linked to the same Console organization. Research credits would pay for the logged API calls used in measurements. Drafted with help from Claude and edited by me.
```

**Champ 12 — Are you located within the United States? (F)** : `No`.

**Conditions (O)** : case `I agree`, **à cocher par Lazar lui-même** ; elle n'est pas pré-cochée dans le lien v2 (elle l'était dans la v1).

## Questions du directeur

### Question 4 — Google demande un lien qui prouve l'inscription en thèse : le contrat de thèse suffit-il ?

**Réponse courte.** Probablement pas tel quel. Le champ attend une adresse web, pas un document, et Google n'écrit nulle part quelle pièce il accepte. Le mieux est une page officielle qui te nomme comme doctorant ; à défaut, demander d'abord à Google par courriel.

**Ce que dit la page de Google** (relevée le 22 novembre : `docs/sources/credits-recherche-v1/edu.google.com_programs_credits_research-v1.html`, `a1f2da4c946730cd…`, et son texte `…-v1.txt`, `419648d4edd68209…`) :
- C'est le même champ que « Link to your profile in your institution's faculty or researcher directory » ; quand le rôle « PhD Student » est choisi, le formulaire affiche le libellé « Link to URL showing your candidacy status » (dans le HTML : champ `Faculty_Directory_Link__c`, libellé conditionné par `ctrl.phDCandidateRoleSelected`).
- Le champ est de type `url` : il attend une adresse web. Le formulaire n'a aucun champ d'envoi de fichier (aucun `type="file"` dans le HTML).
- Son libellé ne porte pas d'astérisque, à la différence des champs obligatoires (« Proposal \* », « Job Title \* »). Non vérifié : si l'envoi est refusé quand il est vide (la règle d'obligation est dans le script de la page, non relevé).
- Les quatre pages d'aide relevées ne disent pas quelle pièce prouve l'inscription. Elles disent l'éligibilité (« PhD students conducting research are eligible to apply for up to $1000 in Google Cloud research credits », page `10324705`) et le rythme (« PhD students may apply once a year for credits of up to $1,000 USD », page `10724468`).
- Conditions sous le formulaire, pour un doctorant : « You represent that the credit will only be used in connection with the project described in this application form and in Your capacity as a PhD student at Your educational institution. »

**Ce qui ferait l'affaire en pratique**, du plus sûr au moins sûr (rien de cela n'est garanti par un texte de Google) :
1. **Une page publique sur un domaine officiel qui te nomme comme doctorant** : la fiche de ta thèse sur theses.fr, si elle y figure comme thèse en préparation ; ou la page de ton équipe sur le site de NeuroSpin ou du CEA, si elle te liste parmi les doctorants. C'est ce qui répond le plus directement à « URL showing your candidacy status ».
2. **La page de l'école doctorale**, seulement si elle te nomme (à vérifier : ces pages listent rarement les doctorants un à un).
3. **Ton profil ORCID**, s'il porte la thèse en cours. C'est une déclaration faite par toi-même : utile en complément, faible seul.
4. **L'attestation d'inscription** (certificat de scolarité 2026-2027 de l'université) : c'est la pièce qui prouve l'inscription, mais c'est un document, pas une page. La page de Google ne prévoit pas de la mettre derrière un lien de partage : ne le faire qu'après leur accord.
5. **Le contrat de thèse** : il prouve un emploi de doctorant, pas l'inscription elle-même ; ce n'est pas une page publique, et il porte des données personnelles. Je ne le mettrais pas en ligne.

**Recommandation** (confiance moyenne, Google ne publiant pas sa règle) : la piste 1 si la page existe. Sinon, écrire d'abord à gcpresearchcredits@google.com (adresse donnée par la page d'aide `10724373`) avec le courriel ci-dessous, et n'envoyer l'attestation que s'ils la demandent. Le courriel institutionnel en @ens-paris-saclay.fr reste un indice à donner dans le champ « Email address ».

Courriel proposé (72 mots) — **Objet** : `Research credits application: how to show PhD candidacy status`
```text
Hello,

I am a PhD student at NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay, and I am preparing an application to the Google Cloud research credits program. The form asks for a link showing my candidacy status. If I have no public page that shows it, would a certificate of enrolment from my university, or my doctoral contract, be acceptable, and how should I share it?

Thank you,
Lazar Ciric
```

### Question 5 — « AI for Science » : faut-il envoyer une preuve de l'accord de l'employeur ou de l'établissement ?

**Réponse courte.** Non, rien n'est à envoyer avec la demande : le formulaire n'a aucun champ de pièce jointe, et ni lui ni le règlement ne demandent une preuve au dépôt. Mais en cochant « I agree », tu déclares sur l'honneur avoir obtenu les accords nécessaires. Il faut donc les avoir vraiment, par écrit, avant d'envoyer, et pouvoir les montrer si Anthropic le demande.

**Ce que disent les textes** (formulaire relevé : `formulaire-ia-pour-la-science-champs-v1.txt`, `7de3104da671c236…` ; règlement « Last updated Oct 20, 2026 » : `www.anthropic.com_ai-for-science-program-rules-v1.txt`, `00f777bfac0e55cb…`) :
- Formulaire, aide du champ « Position or title at organization » : « Note: All projects must have PI approval. If you are not the PI, please provide your PI's email address in the following question. » Champ suivant : « Note: For all selected projects, an email will be sent to your PI to acknowledge and approve the project. » L'accord du responsable du projet est donc recueilli par Anthropic, par courriel au responsable, après la sélection.
- Règlement, « Eligibility Criteria » : « If you are employed by a legal entity or affiliated with a university or other research institution, then you represent and warrant that you have obtained all consents from that employer or institution necessary to participate in the Program. » C'est une déclaration ; aucune pièce n'est demandée au dépôt.
- Règlement, « Selected Researcher Notification » : « Becoming a Selected Researcher is subject to validation and verification of eligibility and compliance with all the Rules » ; le lauréat peut devoir signer « an affidavit certifying compliance with these Rules along with a liability release », à rendre sous quatorze jours.
- Règlement, « Publicity » : Anthropic n'emploie pas « the name or logo of your associated institution or entity without its permission ».
- Les questions vont à aiforscience@anthropic.com (adresse donnée sous les conditions du formulaire).

**Ce que cela veut dire en pratique.**
1. **Le « PI »** : le formulaire ne prend qu'une adresse. Avec deux directeurs, choisir celui ou celle qui répondra au courriel d'Anthropic, et le prévenir. Les deux sont nommés dans le champ libre de la fin (`demande-ai-for-science-anthropic-v2.md`).
2. **Quels accords sont « nécessaires »** : le règlement ne le dit pas ; cela dépend des règles de ton employeur (l'organisme qui porte ton contrat doctoral) et de tes établissements. Je ne les connais pas et ne les invente pas : demander à tes directeurs, ou à l'administration de NeuroSpin, s'il faut un accord de l'établissement en plus du leur.
3. **Garder une trace écrite et datée** de chaque accord (courriel de réponse ou texte signé) avant d'envoyer ; ne l'envoyer que si Anthropic la demande, par exemple à la vérification d'éligibilité.
4. **En cas de doute sur la forme** : écrire à aiforscience@anthropic.com avant d'envoyer.

**Texte d'accord proposé, s'il en faut un** (aucun texte d'Anthropic ne l'exige ; à faire signer par le directeur de thèse, ou par l'établissement si ses règles le demandent ; crochets à remplir par le signataire). En anglais (120 mots) :
```text
Consent to take part in Anthropic's AI for Science Program

I, [NAME], [POSITION] at [INSTITUTION OR LABORATORY], confirm that [I, as thesis supervisor, / the institution] consent to Lazar Ciric, PhD student at NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay, applying to Anthropic's AI for Science Program, and to his receiving and using its credits for the project "Reading an AI agent's internal activations to catch sabotage spread over long tasks", which is part of his PhD. The credits are applied to the Claude account named in his application. This consent does not allow the use of the name or logo of [INSTITUTION] in Anthropic's publicity; that would need separate permission.

Date: [DATE]
Name and signature: [NAME, SIGNATURE]
```
En français (139 mots) :
```text
Accord pour la participation au programme « AI for Science » d'Anthropic

Je soussigné(e) [NOM], [FONCTION] à [ÉTABLISSEMENT OU LABORATOIRE], confirme que [en tant que directeur ou directrice de thèse, je / l'établissement] donne son accord pour que Lazar Ciric, doctorant à NeuroSpin (CEA, Université Paris-Saclay), en partenariat avec l'ENS Paris-Saclay, dépose une demande au programme « AI for Science » d'Anthropic, puis reçoive et emploie ses crédits pour le projet « Reading an AI agent's internal activations to catch sabotage spread over long tasks », qui fait partie de sa thèse. Les crédits sont versés au compte Claude nommé dans la demande. Cet accord ne vaut pas autorisation d'utiliser le nom ou le logo de [ÉTABLISSEMENT] dans la publicité d'Anthropic ; une telle utilisation demanderait une autorisation à part.

Date : [DATE]
Nom et signature : [NOM, SIGNATURE]
```

## À vérifier par Lazar avant d'envoyer

1. « my supervisors support this application » (champ 6) et « who support the application » (champ 11, et champ libre d'« AI for Science ») : le jet 2 ne connaissait l'accord que d'**un** directeur. Confirmer que les deux ont donné leur accord ; sinon, nommer celui qui l'a donné.
2. « Since 2025 I have also worked on AI safety » (champ 6) : d'après le CV v8 ; à garder d'accord avec le CV v9.
3. Champ 5 : `[ID ORGANISATION CONSOLE]`, seule valeur manquante du formulaire.
4. Champ 8 : `Other : 3000` ou `No`.
5. « Each call is logged with model, settings and token counts » (champ 7) : vrai pour les appels par l'interface journalisés par nos outils ; la part qui passe sous l'abonnement (GO-2026-11-22-32) ne l'est pas de la même façon. Le champ 11 dit que les crédits paieraient les appels journalisés : cohérent.
6. Le CV v9 (`cv-v9/`) porte ses propres points à vérifier (chevauchements de dates avec la thèse ; titre de la thèse absent).

## Décomptes de mots du jet 3 (par programme)

Règle : `len(texte.split())`, comme `wc -w`, sur le texte exact du bloc. « < » : limite stricte (« less than », « fewer than ») ; « ≤ » : « max ».

| texte | mots | limite | tenu |
|---|---|---|---|
| Chercheurs externes — expertise en une phrase | 30 | aucune écrite | sans objet |
| Chercheurs externes — champ 6 | 195 | < 200 (less than) | oui |
| Chercheurs externes — champ 7 | 297 | < 300 (less than) | oui |
| Chercheurs externes — champ 11 | 119 | aucune écrite | sans objet |
| AI for Science — Research team | 85 | < 100 (fewer than) | oui |
| AI for Science — Research proposal | 467 | < 500 (fewer than) | oui |
| AI for Science — usage de Claude | 183 | ≤ 200 (max) | oui |
| AI for Science — impact scientifique | 117 | ≤ 200 (max) | oui |
| AI for Science — applications | 94 | ≤ 200 (max) | oui |
| AI for Science — mesure du succès | 72 | ≤ 100 (max) | oui |
| AI for Science — montant | 113 | aucune écrite | sans objet |
| AI for Science — champ libre de la fin | 107 | aucune écrite | sans objet |
| Amazon — Project Proposal | 499 | aucune écrite | sans objet |
| Google — Proposal | 247 | ≤ 250 (max) | oui |
| Google — financement après le crédit | 27 | aucune écrite | sans objet |
| Google — courriel sur les modèles partenaires | 86 | aucune écrite | sans objet |
| Google — courriel sur le lien d'inscription | 72 | aucune écrite | sans objet |
| Texte d'accord proposé (anglais) | 120 | aucune écrite | sans objet |
| Texte d'accord proposé (français) | 139 | aucune écrite | sans objet |

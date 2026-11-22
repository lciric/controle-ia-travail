# Formulaire d'accès des chercheurs externes d'Anthropic : jet 4 des champs, et questions du directeur

- Date : 2026-11-22T12:55Z (`date -u`). Rédaction assistée (session fille, Claude Opus 5.5), pour Lazar, qui relit et envoie lui-même. Rien n'est envoyé ; aucun formulaire n'est rempli en ligne ; personne n'est contacté.
- Remplace pour ces champs le jet 3 (`champs-formulaire-anthropic-jet-3-v1.md`, sha256 `f3da9019fceb4f55…`), qui reste tel quel. Pièces sœurs du jet 4 : `demande-ai-for-science-anthropic-v3.md`, `demandes-credits-nuage-v4.md`, `formulaire-anthropic-prerempli-v3.md` (liens préremplis), `courriel-thomas-romary-v1.md`, CV v18 dans `cv-v18/`.
- Formulaire relevé : `docs/sources/credits-recherche-v1/formulaire-acces-chercheurs-externes-champs-v1.txt` ; identifiants des champs relus par programme dans le HTML d'origine (`formulaire-acces-chercheurs-externes-v1.html`, `802ec3b007cedd4a…`).
- Une seule source pour les textes, les décomptes et les liens : `textes.py`, `liens.py`, `generer.py` du bloc-notes de la session (dossier `jet4/`, copie du `jet3/`). Décomptes par programme, `len(texte.split())` (même règle que `wc -w`), sur le texte exact de chaque bloc ; table en fin de fichier.

## Ce qui change depuis le jet 3 (réponses du directeur du 22 novembre)

1. **Sujet de thèse intégré**, d'après les pièces déposées par Lazar (détail à la question 1) : champ 6, phrase d'expertise, champ « Research team » et champ libre d'« AI for Science », propositions d'Amazon et de Google, CV v18. Titre écrit tel que le sujet le donne ; aucune école doctorale écrite (aucune pièce ne la nomme).
2. **Plus aucun accord des directeurs de thèse affirmé.** « my supervisors support this application » (champ 6), « who support the application » (champ 11) et « who support this application » (champ libre d'« AI for Science ») sont retirés : Lazar ne veut pas que son responsable soit contacté, et aucun accord n'est donc établi. Vérifié par programme à la génération : aucune de ces phrases ne reste dans les textes des formulaires.
3. **« part of my thesis » / « part of my PhD » remplacé** par « alongside my PhD » et, là où il y a la place, « it is not my thesis topic ». Raison : le sujet de thèse déposé porte sur les réseaux cérébraux des mathématiques et leurs corrélats génétiques et éducatifs ; il ne dit rien du contrôle des agents d'IA. Écrire « fait partie de ma thèse » à côté de ce titre, sans accord des directeurs, serait affirmer plus que les pièces. **À trancher par Lazar** (question 1, point 4).
4. **Directeurs de thèse** : plus nommés dans les formulaires (ils le restent dans le CV v18). Les nommer est un fait, pas un accord ; mais à côté d'un champ « responsable » laissé vide, leur nom inviterait à les contacter. Choix de Lazar : on peut remettre « supervised by Stanislas Dehaene and Cathy Philippe » au champ 6 sans dépasser 200 mots si l'on retire la dernière phrase du premier paragraphe.
5. **« AI for Science »** : le champ de l'adresse du responsable est laissé vide, et la recommandation est de **ne pas déposer en l'état** (question 3).
6. **Thomas Romary** : courriel et texte d'appui dans `courriel-thomas-romary-v1.md` (question 4) ; son nom n'entre dans aucun lien prérempli tant qu'il n'a pas répondu oui.
7. **Google** : décision de Lazar consignée (« ok go ») : une attestation d'inscription, si Google l'accepte ; recommandation et courriel de question gardés (question 5).
8. **Textes d'accord du jet 3** (accord du directeur de thèse ou de l'établissement pour « AI for Science ») : retirés du jet 4, faute de démarche auprès du responsable ; ils restent dans le jet 3, à ne pas employer sans décision de Lazar.
- **Toujours pas écrit** : le lemme d'additivité et le théorème négatif comme résultats (GO-2026-11-22-24). La phrase admise sur la loi en racine carrée reste telle quelle.

## Champs du formulaire

**Champ 1 — Name of primary contact (O)**
```text
Lazar Ciric
```

**Champ 2 — Name of organization (if applicable) (F)**
```text
NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay
```

**Champ 3 — Have you been recommended to this form by an Anthropic employee? (O)** : `No` (Thomas Romary n'est pas employé d'Anthropic). **Champ 4** (nom de l'employé) : vide.

**Champ 5 — Which Organization ID would you like the credits applied to? (O)** : `[ID ORGANISATION CONSOLE]`, l'organisation de la console déjà liée à l'abonnement Ultra (console.anthropic.com/settings/organization).

**Expertise en une phrase (41 mots)** — pour les endroits où une version courte est demandée ; le champ 6 la développe.
```text
PhD student at NeuroSpin since 2023 (thesis on brain networks for mathematics, within the ERC-funded MathBrain project), trained in physics, computational neuroscience and machine learning, with two peer-reviewed papers; I study how language models behave and what their internal activations reveal.
```

**Champ 6 — « In less than 200 words, please provide a brief description of the individual applicant or team, including the relevant expertise. » (197 mots)**
```text
I am a PhD student at NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay, since September 2023. My thesis, within the ERC-funded MathBrain project, develops methods to study brain networks involved in mathematics and their educational and genetic correlates. The AI-safety work below runs alongside it.

I trained in physics at ENS Paris-Saclay, in computational neuroscience at ENS Ulm, and in statistics and machine learning at Mines Paris-PSL. I have two peer-reviewed papers: on spiking neural networks (Cimeša, Ciric & Ostojic, PLOS Computational Biology, 2023), and, from an internship at IBM Research Zurich, on analog in-memory computing (Le Gallo, Nandakumar, Ciric et al., Neuromorphic Computing and Engineering, 2022).

Since 2025 I have also worked on AI safety. Two results on Llama-3.1-8B: sycophancy follows a simple law that predicts a second experiment without refitting (preprint, code and data public), and the direction a linear probe reads can carry less than 1% of the causal effect on the behaviour it tracks.

I work with Claude models as research assistants under written rules. Each experiment is preregistered and sealed with a hash before I read any result. A different model reviews each design. Claims that fail stay on record.
```

**Champ 7 — « In less than 300 words, please describe your research or request for free API credits… » (295 mots)**
```text
Topic. My project asks whether reading an AI agent's internal activations helps catch sabotage spread thinly over a long task. Each step looks reasonable on its own; only the total damage shows. A monitor reading only the text may miss it.

I compare probes on the agent's activations with strong text-only monitors, such as LLM judges. I use open-weight models, so I can read their activations, and I plant the damage, so I know the ground truth. One kind of sabotage is kept out of monitor design, with results reported for each kind. Random audits remain the main safeguard; probes are tested as a guide to where to audit, not as a guarantee. I also connect a known result from steganography and nuclear safeguards (a square-root law for how much damage can hide when it is spread thin) to the monitoring of AI agents, and test where it holds on probe scores.

A second line asks how far LLM judges of automated research can be trusted under attack. Several models propose and criticise ideas, scored against planted ground truth rather than a judge's opinion.

How Claude is used. Through the API, Claude helps design and review experiments, judges episodes, proposes and criticises ideas, and reviews code. Each call is logged with model, settings and token counts.

Why credits matter. The project is new and has no funding of its own yet; grant applications are in progress. One reduced ideation campaign with Claude as proposer costs an estimated 700 to 1,500 USD. A failed design must be redesigned and rerun, so I expect two or three campaigns over six months. Without credits I would cut replications or switch to cheaper models, which weakens the comparison. Outputs: papers, public code, and a benchmark with planted ground truth.
```

**Champ 8 — Are you requesting more than $1000 API credits? (O)** : inchangé : `Other` avec `3000` (recommandé), ou `No` pour la voie ordinaire de 1 000 USD.

**Champ 9 — quality of service (F)** : `I'm fine with receiving a low quality of service`.

**Champ 10 — link to your Google Scholar profile or github profile (O)**
```text
https://github.com/lciric
```

**Champ 11 — Additional Information (F, sans limite écrite ; 113 mots)**
```text
I first applied to this program around 13 October 2026 and am sending an updated application, as your help page suggests. This project runs alongside my PhD at NeuroSpin; it is not my thesis topic. I do not ask for any exemption from the Usage Policy. Some prompts in this research describe sabotage strategies for test agents built on open-weight models. This is defensive research on monitoring; these prompts are logged, and the experiments that use them are preregistered. I also have a Claude Ultra subscription linked to the same Console organization. Research credits would pay for the logged API calls used in measurements. Drafted with help from Claude and edited by me.
```
Si Thomas Romary accepte d'être nommé, ajouter **à la fin du champ 11, et seulement après son accord écrit**, l'une des deux phrases ci-dessous (elles ne sont pas dans le lien prérempli) :
```text
Reference: Thomas Romary (Mines Paris-PSL), my former tutor at Mines Paris, has agreed to be contacted about this application: [EMAIL].
```
```text
A short letter of support from Thomas Romary (Mines Paris-PSL), my former tutor at Mines Paris, is available on request.
```

**Champ 12 — Are you located within the United States? (F)** : `No`.

**Conditions (O)** : case `I agree`, **à cocher par Lazar lui-même** ; non pré-cochée dans le lien.

## Questions du directeur

### Question 1 — Le sujet de thèse : titre, école doctorale, cadre

**Pièces lues** (déposées par Lazar ; lues seulement, texte extrait dans un dossier neuf du bloc-notes, rien n'en a été exécuté) :

| pièce | sha256 | ce qu'elle est |
|---|---|---|
| `1206eb24-Sujet_these_BIGMath_Lazar_Ciric.docx` | `93e29a64e3ffd5bf…` | le sujet de thèse, en anglais, en-tête « PhD project » ; métadonnées : créé le 30 août 2023, auteur Stanislas Dehaene |
| `ba73a979-candidature_169844.pdf` | `143154cf74ffc7d7…` | dossier de candidature de 91 pages (CV, relevés et diplômes, rapports de stage, sujet de thèse p. 85 à 89, lettre d'Abu Sebastian) ; modifié le 30 septembre 2023 |
| `0a61ce92-DOSSIER_EOBE.pdf` | `143154cf74ffc7d7…` | **le même fichier**, octet pour octet (même empreinte) |
| `81505158-MathBrain_ERC_AdG_2022_B2_with_highlights_for_oral_defense.pdf` | `6f01dc4d1cdd90cd…` | partie B2 de la proposition ERC Advanced Grant 2022 de Stanislas Dehaene, « Brain mechanisms underlying mathematics and its acquisition » (21 pages) |

**Ce que disent les pièces, et ce qui est retenu.**
1. **Titre** : « Methods to study brain networks involved in mathematics and their educational and genetic correlates » — en-tête du sujet (.docx, premier paragraphe sous « PhD project »), identique p. 85 du dossier de candidature. Écrit sans le point final. Réserve : c'est le titre du sujet de 2023 ; le titre inscrit officiellement (celui de theses.fr ou de l'attestation d'inscription) peut différer. À vérifier sur l'attestation.
2. **École doctorale** : **aucune pièce ne la nomme dans son contenu.** Seul le nom d'un fichier, « DOSSIER_EOBE », laisse penser à l'école doctorale EOBE de l'Université Paris-Saclay ; ce n'est pas une source. Rien n'est écrit ; à ajouter par Lazar d'après son attestation d'inscription.
3. **Cadre** : le sujet dit « As part of the ERC-funded MathBrain project, Stanislas Dehaene (Neurospin, UNICOG) is launching the first systematic study of the mental and cerebral representation of a wide range of mathematical concepts… In this context… the aim of the thesis is three-folded » (identifier les réseaux cérébraux liés aux mathématiques, surtout en IRM fonctionnelle de repos ; mesurer l'effet de la génétique et de l'éducation sur leur variabilité ; décrire leur développement pendant l'enfance). La proposition ERC confirme le projet (ERC Advanced Grant 2022, « MathBrain », porteur Stanislas Dehaene). Retenu : « within the ERC-funded MathBrain project ».
4. **Ce que les pièces ne disent pas** : qui finance le contrat doctoral de Lazar (le sujet dit que le projet MathBrain est financé par l'ERC, pas que le contrat l'est) ; la directrice ou le directeur de thèse (Cathy Philippe n'y figure que comme coautrice d'un article cité ; les noms des directeurs viennent du jet 2) ; et **aucun lien entre la thèse et le contrôle des agents d'IA**. Le sujet ouvre seulement des « avenues of methodological exploration », dont « deep neural networks ». D'où le point 3 des changements. Si Lazar maintient que le contrôle des agents fait partie de sa thèse, il faut une pièce qui le dise (avenant au sujet, compte rendu du comité de suivi), et l'accord des directeurs pour l'écrire dans une demande ; sinon, garder « alongside my PhD ».
5. **Écarts à vérifier entre le dossier de 2023 et le CV** (le CV v18 n'est pas changé sur ces points, qui sont des faits à Lazar) : détail dans `cv-v18/notes-cv-v18-v1.md`.

### Question 2 — CV v18

Écrit à partir de la v17 (commit `be6ccd08a`, variante « universel »), avec les corrections de la v9 et le titre de thèse : `cv-v18/Lazar_Ciric_CV_2026-11-22_v18_universel.html` et `.pdf`, notes dans `cv-v18/notes-cv-v18-v1.md`.

### Question 3 — « AI for Science » : que faire du champ qui demande l'adresse du responsable, sans le contacter ?

**Réponse courte.** On ne peut pas, honnêtement, à la fois déposer comme projet d'un doctorant, cacher le responsable et cocher « I agree ». Le champ peut rester vide techniquement, mais le formulaire dit que tout projet doit avoir l'accord du responsable. Il ne faut **pas** y mettre une autre personne qui ne dirige pas le projet. La voie propre est de **déposer seulement au programme des chercheurs externes**, qui n'a pas de champ de responsable et vise justement la sûreté de l'IA ; et, si « AI for Science » compte vraiment, d'**écrire d'abord à Anthropic** pour demander si un doctorant peut se déclarer responsable d'un projet qu'il mène lui-même hors de sa thèse.

**Ce que disent les textes relevés.**
- Formulaire (`formulaire-ia-pour-la-science-champs-v1.txt`, `7de3104da671c236…`), aide du champ « Position or title at organization » (obligatoire) : « Note: All projects must have PI approval. If you are not the PI, please provide your PI's email address in the following question. »
- Champ suivant, « What is your PI's academic or organization email address? » : **facultatif** dans le formulaire ; aide : « If you are the PI, please enter your email address. Note: For all selected projects, an email will be sent to your PI to acknowledge and approve the project. »
- Règlement (« Last updated Oct 20, 2026 », `www.anthropic.com_ai-for-science-program-rules-v1.txt`, `00f777bfac0e55cb…`), « Eligibility Criteria » : « If you are employed by a legal entity or affiliated with a university or other research institution, then you represent and warrant that you have obtained all consents from that employer or institution necessary to participate in the Program. »
- Règlement, « Applications » : « Only fully complete and compliant applications are eligible to receive Credits » ; « Judging Criteria » : Anthropic peut écarter une demande « submitted in bad faith or [that] raises any concerns regarding compliance with these Rules ».
- Règlement, « Selected Researcher Notification » : « subject to validation and verification of eligibility » ; déclaration sur l'honneur (« affidavit certifying compliance with these Rules ») possible sous quatorze jours.
- Conditions sous le formulaire : en envoyant, on accepte les conditions et le règlement.
- Page d'aide (`support.claude.com_…11199177…`) : le programme vise « researchers attached to research institutions » ; l'annonce « Expanding our support for scientists » : « Any researcher is eligible to apply. »
- À comparer : le formulaire des chercheurs externes n'a **aucun** champ de responsable, et son champ d'organisation porte « (if applicable) ».

**Les possibilités, une à une.**
1. **Laisser le champ vide ?** Techniquement oui : il est facultatif. Honnêtement, seulement si l'on dit pourquoi, dans le champ libre de la fin (phrase B ci-dessous), en acceptant que la demande soit jugée non éligible. Le laisser vide sans rien dire, puis cocher « I agree » alors qu'on sait qu'aucun responsable n'a approuvé, contredirait la règle « All projects must have PI approval ».
2. **Y nommer une autre personne qui appuie la demande (Thomas Romary, par exemple) ?** **Non.** Le champ ne demande pas une référence : il demande le responsable du projet, et Anthropic lui écrira « to acknowledge and approve the project ». Thomas Romary n'est ni responsable ni encadrant de ce projet ; le nommer là lui ferait approuver, au nom d'un rôle qu'il n'a pas, un projet qu'il ne dirige pas. Ce serait honnête seulement s'il devenait réellement le responsable du projet et l'acceptait par écrit, ce qui n'est ni demandé ni proposé ici. Son nom peut figurer, avec son accord, comme **référence** dans le champ libre de la fin.
3. **Y mettre sa propre adresse, comme responsable ?** Seulement si c'est vrai : Lazar mène le projet lui-même, hors de sa thèse et hors d'un projet dirigé par quelqu'un d'autre. C'est ce que disent les textes du jet 4 (« alongside my PhD », « not my thesis topic »). Mais deux choses restent : (a) le formulaire est pensé pour des projets dirigés par un responsable, et un doctorant qui se déclare responsable est un cas qu'il ne prévoit pas ; mieux vaut le demander d'abord (option 4) ; (b) la règle d'éligibilité reste entière : en indiquant NeuroSpin comme organisation, Lazar déclare avoir tous les accords nécessaires de son employeur et de son établissement. Lesquels sont nécessaires dépend de son contrat et des règles de l'établissement, que je ne connais pas. On ne coche « I agree » qu'en les ayant.
4. **Demander d'abord à Anthropic** (aiforscience@anthropic.com, adresse donnée sous les conditions du formulaire) : courriel proposé ci-dessous. Il dit la situation telle qu'elle est et ne nomme pas les directeurs.
5. **Ne pas déposer à « AI for Science »** et déposer seulement au programme des chercheurs externes (crédits d'interface de programmation, sûreté et alignement, pas de champ de responsable, organisation facultative).

**Ce qu'il faut déclarer, dans tous les cas** : le poste réel (`PhD student`) ; que le projet n'est pas le sujet de thèse ; qui le mène ; ce qu'il en est de l'accord du responsable (phrase A ou B). **Jamais** un accord qui n'existe pas : ni « my supervisors support this application », ni une adresse de quelqu'un qui n'a pas accepté le rôle de responsable.

**Recommandation** (confiance haute pour le premier point, moyenne pour le second) : déposer d'abord au seul programme des chercheurs externes (`formulaire-anthropic-prerempli-v3.md`, lien 1). Pour « AI for Science », envoyer d'abord le courriel ci-dessous et ne déposer que sur une réponse écrite qui l'admet (phrase A) ; sans réponse, ne pas déposer, ou déposer avec la phrase B en acceptant le refus.

Courriel proposé à Anthropic (103 mots) — **À** : aiforscience@anthropic.com — **Objet** : `AI for Science: PhD student leading a project outside his thesis - who is the PI?`
```text
Hello,

I am a PhD student at NeuroSpin (CEA, Université Paris-Saclay). I would like to apply to the AI for Science program for an AI-safety project that I lead myself. It runs alongside my PhD and is not my thesis topic, so my thesis supervisors are not its PI.

The form says that all projects must have PI approval. In a case like mine, may I enter my own email as PI? Or is the program only for projects led by a PI? If so, I will not apply, rather than name someone who does not lead the project.

Thank you,
Lazar Ciric
```

Phrase A, à mettre à la place du crochet du champ libre si Anthropic l'admet par écrit (26 mots) ; le champ du responsable porte alors l'adresse de Lazar :
```text
I lead this project myself. Your team confirmed by email on [DATE] that I may enter my own email in the PI field, which I did.
```
Phrase B, si Lazar dépose sans réponse, champ du responsable vide (43 mots) :
```text
I left the PI field empty. This project is not led by a PI: I lead it myself, outside my thesis. If PI approval is required for a project like this, please tell me; I understand that it may then not be eligible.
```

### Question 4 — Thomas Romary : où son nom peut-il figurer ?

Courriel en français, texte d'appui en anglais et détail par formulaire : `courriel-thomas-romary-v1.md`. En bref :
- **Possible, avec son accord écrit, comme référence** (et non comme accord de l'employeur ni comme responsable) : champ 11 du formulaire des chercheurs externes ; champ libre de la fin d'« AI for Science » ; une phrase dans la proposition d'Amazon (aucun champ prévu, sans gain net).
- **Pas possible** : le champ du responsable d'« AI for Science » ; le champ « Research team » d'« AI for Science » (il liste les membres qui emploieront Claude) ; les champs 3 et 4 du formulaire des chercheurs externes (employé d'Anthropic) ; « Research Led By » chez Amazon (`Faculty Member/PI` serait faux) ; chez Google, aucun champ ne s'y prête (une personne par proposition ; le lien d'inscription doit prouver l'inscription de Lazar).
- Son appui ne remplace **aucun** accord que le règlement d'« AI for Science » fait déclarer à Lazar sur son employeur ou son établissement : les Mines ne sont ni l'un ni l'autre aujourd'hui.

### Question 5 — Google : le lien qui prouve l'inscription en thèse

**Décision de Lazar (22 novembre, « ok go »)** : une attestation d'inscription, si Google l'accepte. Recommandation du jet 3 gardée : écrire d'abord à gcpresearchcredits@google.com (courriel ci-dessous, inchangé), n'envoyer l'attestation que s'ils l'acceptent et selon la voie qu'ils indiquent ; une page officielle qui nomme Lazar comme doctorant (theses.fr, page de l'équipe) reste la meilleure réponse au champ si elle existe. Le contrat de thèse n'est pas proposé. Détail et sources : `demandes-credits-nuage-v4.md`.

Courriel (72 mots) — **À** : gcpresearchcredits@google.com — **Objet** : `Research credits application: how to show PhD candidacy status`
```text
Hello,

I am a PhD student at NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay, and I am preparing an application to the Google Cloud research credits program. The form asks for a link showing my candidacy status. If I have no public page that shows it, would a certificate of enrolment from my university, or my doctoral contract, be acceptable, and how should I share it?

Thank you,
Lazar Ciric
```

## À vérifier par Lazar avant d'envoyer

1. « alongside my PhD » et « it is not my thesis topic » (champs 6 et 11, « AI for Science », Amazon, Google) : à confirmer, ou à remplacer par une formule qu'une pièce soutient (question 1, point 4).
2. Titre de thèse : à comparer avec celui de l'attestation d'inscription ; école doctorale à ajouter d'après elle si Lazar le souhaite (CV surtout).
3. « preprint, code and data public » (champ 6) et « public preprint » (« AI for Science ») : le CV v17, base du v18, dit « Manuscript in preparation; code and data public ». Les deux ne peuvent être vrais en même temps : garder la formule juste partout.
4. Champ 5 : `[ID ORGANISATION CONSOLE]`. Champ 8 : `Other : 3000` ou `No`.
5. Phrases sur Thomas Romary : seulement après son accord écrit.
6. « Since 2025 I have also worked on AI safety » : d'accord avec le CV v18.

## Décomptes de mots du jet 4 (par programme)

Règle : `len(texte.split())`, comme `wc -w`, sur le texte exact du bloc. « < » : limite stricte (« less than », « fewer than ») ; « ≤ » : « max ».

| texte | mots | limite | tenu |
|---|---|---|---|
| Chercheurs externes — expertise en une phrase | 41 | aucune écrite | sans objet |
| Chercheurs externes — champ 6 | 197 | < 200 (less than) | oui |
| Chercheurs externes — champ 7 | 295 | < 300 (less than) | oui |
| Chercheurs externes — champ 11 | 113 | aucune écrite | sans objet |
| AI for Science — Research team | 94 | < 100 (fewer than) | oui |
| AI for Science — Research proposal | 468 | < 500 (fewer than) | oui |
| AI for Science — usage de Claude | 183 | ≤ 200 (max) | oui |
| AI for Science — impact scientifique | 117 | ≤ 200 (max) | oui |
| AI for Science — applications | 94 | ≤ 200 (max) | oui |
| AI for Science — mesure du succès | 72 | ≤ 100 (max) | oui |
| AI for Science — montant | 113 | aucune écrite | sans objet |
| AI for Science — champ libre de la fin | 137 | aucune écrite | sans objet |
| Amazon — Project Proposal | 511 | aucune écrite | sans objet |
| Google — Proposal | 244 | ≤ 250 (max) | oui |
| Google — financement après le crédit | 27 | aucune écrite | sans objet |
| Google — courriel sur les modèles partenaires | 86 | aucune écrite | sans objet |
| Google — courriel sur le lien d'inscription | 72 | aucune écrite | sans objet |
| AI for Science — phrase A sur le responsable | 26 | aucune écrite | sans objet |
| AI for Science — phrase B sur le responsable | 43 | aucune écrite | sans objet |
| AI for Science — courriel de question sur le responsable | 103 | aucune écrite | sans objet |
| Thomas Romary — courriel (français) | 248 | aucune écrite | sans objet |
| Thomas Romary — texte d'appui (anglais) | 141 | aucune écrite | sans objet |
| Thomas Romary — phrase de référence | 20 | aucune écrite | sans objet |
| Thomas Romary — phrase de lettre | 20 | aucune écrite | sans objet |

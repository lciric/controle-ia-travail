# Demandes de crédits de recherche chez Amazon et Google (version 4)

- Date : 2026-11-22T12:55Z (`date -u`). Rédaction assistée (session fille, Claude Opus 5.5), pour Lazar, qui relit et dépose lui-même. Rien n'est envoyé ; aucun formulaire n'est rempli en ligne.
- Remplace pour les textes à coller `demandes-credits-nuage-v3.md` (sha256 `f9954f7568bbf19f…`), qui reste tel quel. La partie technique de la v1 (`demandes-credits-nuage-v1.md`) et la section de la v2 « Voir à quoi s'appliquent les crédits, dans la console de Google » restent valables et ne sont pas recopiées.
- Changements, sur les réponses du directeur du 22 novembre :
  1. **Thèse** : le projet est dit mené « alongside my PhD » et non plus « as part of my PhD » ; la proposition d'Amazon donne le sujet de thèse en une phrase (« My thesis, within the ERC-funded MathBrain project, is on brain networks involved in mathematics; this project is not my thesis topic. ») ; celle de Google, faute de place, dit seulement « alongside my PhD ». Les directeurs de thèse ne sont plus nommés. Sources et raisons : question 1 de `champs-formulaire-anthropic-jet-4-v1.md`.
  2. **Google, lien prouvant l'inscription** : décision de Lazar consignée (« ok go ») : une attestation d'inscription, si Google l'accepte. Recommandation et courriel de question gardés (section B).
  3. **Thomas Romary** : son nom n'entre dans aucun champ de ces deux formulaires ; « Research Led By » reste `Myself` (détail : `courriel-thomas-romary-v1.md`).
  Le reste est inchangé depuis la v3.
- Sources : formulaire d'Amazon relevé (`docs/sources/credits-recherche-v1/pages.awscloud.com_aws-cloud-credit-for-research-champs-v1.txt`, `cd85ba3a7df3ca7b…`) ; page du programme (`aws.amazon.com_research-credits-v1.txt`, `b42fd83b850dfa27…`) et sa foire aux questions (`aws.amazon.com_research-credits_faq-v1.txt`, `8a417b9e0040c83f…`) ; page et formulaire de Google (`edu.google.com_programs_credits_research-v1.txt`, `419648d4edd68209…`) et ses pages d'aide.
- Liens préremplis : aucun pour ces deux formulaires. Ce ne sont pas des formulaires Google : Amazon et Google emploient chacun un formulaire Marketo (n° 65772 pour Amazon, n° 21267 sur la page d'éducation de Google) ; aucune des pages relevées ne documente un préremplissage par l'adresse, et un essai en ligne serait un envoi de données. Les textes sont à coller.
- Toujours pas écrit : le lemme d'additivité et le théorème négatif. Phrase admise sur la loi en racine carrée, à la première personne. Décomptes par programme (`len(texte.split())`, comme `wc -w`).

## L'éligibilité, maintenant

- **Amazon** : « Graduate, post-graduate or PhD students enrolled at an accredited research institution » sont admis ; « Student applications may request up to $5,000.00 in AWS Promotional Credit » (foire aux questions ; la page du programme dit de même « Student awards will be up to a maximum of $5,000.00 »). Adresse de l'établissement exigée : [COURRIEL ÉTABLISSEMENT] en @ens-paris-saclay.fr convient a priori.
- **Ce qu'Amazon finance et ne finance pas** (foire aux questions) : « Research credit will not support administrative workloads, operations, and ongoing or established research projects. Research credit will not support general lab projects or ongoing research. » et « Projects should fall into one of three project types: proof of concept or benchmark for comparison; development of repeatable, sharable solutions; or advanced workshops or tutorials. » D'où la demande : un projet neuf, et une pièce bornée de type « benchmark for comparison » qui est aussi « repeatable, sharable ».
- **Google** : « a PhD student » est admis, France comprise ; plafond doctorant 1 000 USD par an ; le formulaire demande pour les doctorants un « Link to URL showing your candidacy status » (voir « Lien prouvant l'inscription : décision », section B). Une seule personne par proposition.
- Les deux : l'établissement nommé doit être celui qui t'inscrit et dont l'adresse électronique porte le domaine ; NeuroSpin, l'Université Paris-Saclay et l'ENS Paris-Saclay ne sont pas interchangeables dans une liste fermée. **À trancher par Lazar.**

---

## A. Amazon — AWS Cloud Credit for Research

### Ce que Lazar fait

1. Un compte AWS payant (« Effective February 16, 2026, Free Tier accounts will be ineligible for promotional credits ») ; noter l'identifiant à 12 chiffres.
2. Une estimation dans le calculateur (https://calculator.aws/) : une instance à carte graphique de 48 Go (famille g6e ou voisine) pour [N] heures, le stockage, et, en ligne à part, Amazon Bedrock pour Claude. **Total au plus 5 000 USD** (plafond étudiant). Copier l'adresse de partage ; le montant demandé égale le total du calculateur.
3. Remplir https://pages.awscloud.com/aws-cloud-credit-for-research.html avec l'adresse de l'établissement ; ne pas cocher le consentement aux courriels commerciaux.
4. Délai : « 30 to 60 days » sur la page du formulaire, « 90 to 120 days » sur celle du programme. Validité : un an. Dès l'octroi : alertes de facturation.

### Champs (O = obligatoire) et réponses

- **First Name (O)** / **Last Name (O)** : `Lazar` / `Ciric`
- **Institution Name (O)** : `NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay` — ou le seul nom de l'établissement d'inscription, s'il doit correspondre au domaine de l'adresse.
- **Institutional Email Address (O)** : [COURRIEL ÉTABLISSEMENT]
- **Phone Number (O)** : [TÉLÉPHONE]
- **AWS Account ID (O)** : [IDENTIFIANT DU COMPTE AWS, 12 chiffres]
- **Area of Research Study (O)** : `Computer & Information Sciences`
- **Research Led By (O)** : `Myself` (tu mènes ce projet, à côté de ta thèse). Ne pas choisir `Faculty Member/PI` : ni tes directeurs ni Thomas Romary ne dirigent ce projet.
- **Requested Credit Amount in USD (O)** : [TOTAL DU CALCULATEUR, au plus 5 000]
- **AWS Pricing Calculator URL (O)** : [ADRESSE DE L'ESTIMATION]
- **Project Title (O)** :
```text
An open benchmark for catching diffuse sabotage by AI agents from their internal activations
```
- **Project Proposal (O)** — pas de limite écrite dans le formulaire relevé (511 mots). La page demande : problème, résumé, services AWS, calendrier et jalons, partage des résultats, usage futur d'AWS, employés d'AWS contactés, jeux de données publics d'AWS.
```text
Problem. AI agents that carry out long research or analysis tasks can sabotage diffusely: each step looks honest, but the damage adds up. Monitors that read only the agent's text may miss it. Reading the agent's internal activations is another route, but there is no open benchmark to test it.

Summary. This is a new project at an early stage. It started in October 2026, alongside my PhD at NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay. My thesis, within the ERC-funded MathBrain project, is on brain networks involved in mathematics; this project is not my thesis topic. I am applying for grants now. This request covers one bounded piece of work: an open benchmark and the test harness that runs it.

The benchmark holds episodes of test agents built on open-weight models (Llama-3.1-8B and similar). The agents do long tasks either honestly or with sabotage I plant, so the ground truth is known. The harness records the agents' internal activations and compares two kinds of monitors on the same episodes: linear probes on the activations, and monitors that read only text, such as LLM judges and simple statistics. One kind of sabotage is kept out of monitor design, and results are reported for each kind. I also connect a known result from steganography and nuclear safeguards (a square-root law for how much damage can hide when it is spread thin) to the monitoring of AI agents, and test where it holds on probe scores. Each decisive experiment is preregistered and sealed with a SHA-256 hash before results are read. Negative results are reported.

AWS services. Amazon EC2 GPU instances, on demand or spot (48 GB class, such as the g6e family), to run the agents, record activations, and train and test probes. Amazon S3 to store activations and sealed outputs. Amazon Bedrock (Claude in Amazon Bedrock) for text judges, if Bedrock use is covered by this program. Please tell me whether charges for Anthropic models used through Amazon Bedrock can be paid with the credits; if not, please apply the award to EC2 and S3 only.

Timeline and milestones (12 months). Months 1-2: set up the harness on AWS, calibrate the test agents and the text-only monitors, publish the harness. Months 3-6: build the benchmark episodes and run the sealed comparison, kind of sabotage by kind, held-out kind included. Months 7-9: release the benchmark and a first paper. Months 10-12: support replications by others on the released harness.

Sharing. Open-source harness and probe code; the benchmark with planted ground truth, released after the held-out evaluation; sealed preregistrations and run records (seeds, versions, commits) in a public repository ([LIEN DÉPÔT PUBLIC]); papers in which every number traces to a sealed file.

Future use of AWS. The harness runs on standard EC2 GPU instances, so others can replicate the results on AWS. If the grants I have applied for are awarded, I would keep using AWS for later stages of the project.

AWS employees contacted: none. AWS public data sets: none planned.

Drafted with help from Claude and edited by me.
```
- **Project Type (O)** : `Evaluation/Comparison` (recommandé : c'est le « benchmark for comparison » de la foire aux questions) ; `Developing Open Source Software` en second choix.
- **Does your research project have additional external funding sources? (O)** : recommandé `No` (des demandes de bourses sont en cours, aucune n'est accordée). **À confirmer par Lazar** : si le contrat doctoral ou le laboratoire paie une part de ce projet (calcul, matériel), répondre `Yes`. Le champ « Please provide your Notice Number » reste vide si `No`.
- **Country / Region (O)** : `France` ; **State/Province (O)** : `Île-de-France` ; **Postal Code (O)** : [CODE POSTAL DE L'ÉTABLISSEMENT]
- **Industry (O)** : `Education`
- **Job Role (O)** : `PhD Student` ; **Job Title (O)** : `PhD student`
- **Level of AWS Usage (O)** : [`Do not use AWS today` ou `Evaluating/experimenting with AWS`]
- **Use Case (O)** : `AI & Machine Learning`

---

## B. Google — Google Cloud research credits

### Ce que Lazar fait

1. Un compte de facturation Google Cloud (https://console.cloud.google.com/billing) ; noter son identifiant. Ne rien lancer avant que le crédit apparaisse : « Google Cloud credits are not retroactive. »
2. Une estimation dans le calculateur de Google : machine à carte graphique (L4 ou A100) pour [N] heures, stockage ; **total au plus 1 000 USD** (plafond doctorant).
3. Régler d'abord la question du lien prouvant l'inscription (ci-dessous, « Lien prouvant l'inscription : décision »).
4. Remplir le formulaire de https://edu.google.com/programs/credits/research/ .
5. Délai : « within 6-8 weeks ». Validité : 365 jours ; activation dans les 60 jours qui suivent la date de début déclarée. Mention à faire dans les papiers si octroi : « This material is based upon work supported by the Google Cloud Research Credits program with the award [NUMÉRO]. »

### Champs (\* = obligatoire sur la page) et réponses

- **First name \*** / **Last name \*** : `Lazar` / `Ciric`
- **Email address (Institution account preferred)** : [COURRIEL ÉTABLISSEMENT]
- **Country \*** : `France` ; **State** : sans objet
- **Job Title \*** : `PhD Student`
- **Organization Name \*** : [ÉTABLISSEMENT D'INSCRIPTION, à choisir dans la liste : Université Paris-Saclay ou ENS Paris-Saclay, selon ce qui est proposé et ce qui correspond à l'adresse]
- **Type of institution (optional)** : `University`
- **Department name (optional)** : `NeuroSpin (CEA)`
- **Link to URL showing your candidacy status** (libellé affiché pour les doctorants) : [LIEN PROUVANT L'INSCRIPTION EN THÈSE] — voir « Lien prouvant l'inscription : décision » ci-dessous.
- **How did you hear about the program? \*** : `Google Search`
- **Project name \*** :
```text
Catching diffuse sabotage by AI agents from their internal activations: an open benchmark
```
- **Project start date \*** : [DATE, au plus tôt huit semaines après le dépôt ; le crédit doit être activé dans les 60 jours qui suivent]
- **Proposal \*** — « 250 words maximum » (244 mots).
```text
Research problem. AI agents doing long research tasks can sabotage diffusely: each step looks honest, but the damage adds up, and monitors that read only the agent's text may miss it. In a new project alongside my PhD at NeuroSpin (CEA, Université Paris-Saclay), with ENS Paris-Saclay, I test whether linear probes on an agent's internal activations catch such sabotage better than strong text-only monitors. Test agents built on open-weight models (Llama-3.1-8B and similar) work honestly or with sabotage I plant, so the ground truth is known; one kind of sabotage is kept out of monitor design. Each decisive experiment is preregistered and sealed before results are read; negative results are reported.

GCP tools. Compute Engine GPU instances (L4 or A100 class) to record activations and train probes; Cloud Storage for activations and sealed outputs; optionally Claude models through Model Garden as text judges, if research credits cover partner models (please advise).

Timeline and milestones (12 months). Months 1-2: set up the harness, calibrate the agents and monitors, publish the harness. Months 3-6: sealed comparison of probes and text-only monitors. Months 7-9: release of a benchmark with planted ground truth, and a paper. Months 10-12: replications by others.

Outcomes. Open-source harness and probe code, the benchmark, sealed preregistrations, and papers.

Future use. The harness runs on standard Compute Engine GPU instances, so others can replicate on Google Cloud; I would keep using it in later stages.

Drafted with help from Claude and edited by me.
```
- **Field of research \*** : `Computer & Information Sciences`
- **Google scholar link (Optional)** : [PROFIL SCHOLAR, s'il existe] ; sinon vide.
- **How do you intend to apply awarded cloud credits? \*** : `Evaluation/Comparison` (ou `Developing Open Source Software`)
- **Does your research project have an external funding source? \*** : recommandé `No`, même réserve que chez Amazon.
- **Have you used cloud infrastructure for your research before? \*** : `Yes` (cartes graphiques louées ; calcul intensif à NERSC autrefois)
- **Have you used Google Cloud before? \*** : [Yes / No]
- **Expected costs (total and calculator link)** : [TOTAL, au plus 1 000 USD] ; [ADRESSE DE L'ESTIMATION]
- **Google Cloud Billing Account ID \*** : [IDENTIFIANT DU COMPTE DE FACTURATION]
- **After your credit expires, how do you intend to continue funding your project? \*** (27 mots)
```text
I have applied for research grants for this project; if they are awarded, they will fund later stages. Compute needs stay modest: single-GPU runs on 8-billion-parameter models.
```
- **Would you like to receive periodic emails…? \*** : `No`

### Lien prouvant l'inscription : décision

**Décision de Lazar (22 novembre, « ok go ») : une attestation d'inscription, si Google l'accepte.** Ce que cela veut dire en pratique, d'après la recommandation du jet 3, gardée :
1. Le champ est de type `url` (une adresse web) et le formulaire n'a aucun envoi de fichier ; la page de Google ne dit pas quelle pièce elle accepte (`edu.google.com_programs_credits_research-v1.html`, `a1f2da4c946730cd…`).
2. Écrire d'abord à gcpresearchcredits@google.com avec le courriel ci-dessous, qui propose justement l'attestation d'inscription (« a certificate of enrolment from my university ») et demande comment la partager.
3. Ne mettre l'attestation en ligne (par un lien de partage) **que** si Google l'accepte, et selon la voie qu'ils indiquent ; masquer ce qui n'est pas utile (numéro d'étudiant, date et lieu de naissance) si Google ne le demande pas.
4. Si une page officielle nomme Lazar comme doctorant (theses.fr, page de l'équipe à NeuroSpin), elle reste la meilleure réponse au champ, sans rien mettre en ligne.
5. Le contrat de thèse n'est pas proposé (il prouve un emploi, pas l'inscription, et porte des données personnelles).
6. Lire sur l'attestation le titre de thèse et l'école doctorale officiels ; s'ils diffèrent du sujet de 2023, corriger le CV v18 et les textes.

Courriel sur le lien d'inscription (inchangé depuis le jet 3 ; 72 mots) — **À** : gcpresearchcredits@google.com — **Objet** : `Research credits application: how to show PhD candidacy status`
```text
Hello,

I am a PhD student at NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay, and I am preparing an application to the Google Cloud research credits program. The form asks for a link showing my candidacy status. If I have no public page that shows it, would a certificate of enrolment from my university, or my doctoral contract, be acceptable, and how should I share it?

Thank you,
Lazar Ciric
```

### Courriel de question à Google sur les modèles partenaires (facultatif, inchangé depuis la v2)

**À** : gcpresearchcredits@google.com — **Objet** : `Research credits: are Anthropic Claude partner models covered?` (86 mots)
```text
Hello,

I am a PhD student at NeuroSpin (CEA, Université Paris-Saclay) and am preparing an application to the Google Cloud research credits program, for a project on monitoring AI agents. Most of the award would pay for Compute Engine GPU instances. I would also like to use Anthropic's Claude models through Model Garden as text judges. Can research credits pay for these partner models, or only for Google Cloud products? If they cannot, I will request credits for compute and storage only.

Thank you,
Lazar Ciric
```
Le courriel sur le lien d'inscription peut partir avec celui-ci, ou être fondu dedans.

## Réserves

- Les textes d'Amazon et de Google finissent par « Drafted with help from Claude and edited by me. » ; Google compte cette phrase dans ses 250 mots.
- « This is a new project at an early stage. It started in October 2026 » : d'après le début de la phase 0 du programme (5 octobre 2026) et le mot du directeur ; « alongside my PhD » et « not my thesis topic » d'après le sujet de thèse déposé (question 1 du jet 4), à confirmer par Lazar. La foire aux questions d'Amazon exclut les projets « ongoing or established » : la demande vise la seule pièce neuve et bornée ; ne pas y ajouter de travaux déjà faits présentés comme cœur de la demande.
- Couverture de Claude par ces crédits : non établie chez les deux fournisseurs ; les textes demandent par écrit. Ne compter que sur les cartes graphiques et le stockage.
- Recevoir ces crédits puis lancer une course chez Amazon ou Google reste une dépense de calcul au sens des règles du dépôt : devis et GO par ligne. La garde de calcul du dépôt ne connaît aujourd'hui ni Amazon ni Google.
- Les familles d'instances (g6e, L4, A100) sont des exemples à confirmer dans les calculateurs ; aucun prix n'est avancé.

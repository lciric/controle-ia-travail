# Demandes de crédits de recherche chez Amazon et Google (version 2)

- Date : 2026-11-22T10:45Z (`date -u`). Rédaction assistée (session fille, Claude Opus 5.5), pour Lazar, qui retravaille et dépose lui-même. Rien n'est envoyé.
- Remplace pour les textes à coller `demandes-credits-nuage-v1.md` (sha256 `fca751aea272cf71…`), qui reste tel quel et garde la partie technique : modèles Claude et identifiants chez chaque fournisseur, régime des données, lecture des conditions des crédits. Changements : affiliation remplie (doctorant à NeuroSpin, en partenariat avec l'ENS Paris-Saclay) ; éligibilité tranchée ; textes réécrits en phrases courtes ; aide de Claude déclarée ; chemin de la console de Google pour voir à quoi s'appliquent les crédits, d'après la documentation officielle.
- Sources : formulaire d'Amazon relevé (`docs/sources/credits-recherche-v1/pages.awscloud.com_aws-cloud-credit-for-research-champs-v1.txt`, `cd85ba3a7df3ca7b…`) ; page et formulaire de Google (`edu.google.com_programs_credits_research-v1.txt`, `419648d4edd68209…`) et ses quatre pages d'aide ; empreintes des HTML d'origine dans `LISEZMOI-v1.md` (`8a07b7b9ecb5f02a…`). Pour la page « Crédits » de Google : deux pages de la documentation de facturation relevées par cette session, versées dans le même dossier, `LISEZMOI-complement-1-v1.md` (`4706a3b4fadab8d1…`).
- Ne s'écrit plus : le lemme d'additivité et le théorème négatif. Phrase admise sur la loi en racine carrée, à la première personne. Aucun chiffre de l'état de l'art. Décomptes par programme (`wc -w` sur le texte exact des blocs).

## L'éligibilité, maintenant

- **Amazon** : « Graduate, post-graduate or PhD students enrolled at an accredited research institution » sont admis ; « official institution-issued email ID (.edu, .org, or equivalent) » exigé : [COURRIEL ÉTABLISSEMENT] en @ens-paris-saclay.fr convient a priori. Réserve de la foire aux questions : « Research credit will not support […] ongoing or established research projects ». La demande porte donc sur une pièce neuve et bornée : le banc public et son harnais.
- **Google** : « a PhD student » est admis, France comprise ; **plafond doctorant : 1 000 USD par an** (« PhD students may apply once a year for credits of up to $1,000 USD ») ; le formulaire demande pour les doctorants un « Link to URL showing your candidacy status ». Une seule demande par projet.
- Les deux : l'établissement à nommer doit être celui qui t'inscrit et dont l'adresse électronique porte le domaine ; NeuroSpin, l'Université Paris-Saclay et l'ENS Paris-Saclay ne sont pas interchangeables dans une liste fermée. **À trancher par Lazar** (voir les champs).

---

## A. Amazon — AWS Cloud Credit for Research

### Ce que Lazar fait

1. Un compte AWS payant (« Effective February 16, 2026, Free Tier accounts will be ineligible for promotional credits ») ; noter l'identifiant à 12 chiffres.
2. Une estimation dans le calculateur (https://calculator.aws/) : une instance à carte graphique de 48 Go (famille g6e ou voisine) pour [N] heures, le stockage, et, en ligne à part, Amazon Bedrock pour Claude. Copier l'adresse de partage. Le montant demandé égale le total du calculateur.
3. Remplir https://pages.awscloud.com/aws-cloud-credit-for-research.html avec l'adresse de l'établissement ; ne pas cocher le consentement aux courriels commerciaux.
4. Délai : « 30 to 60 days » sur la page du formulaire, « 90 to 120 days » sur celle du programme. Validité : un an. Dès l'octroi : alertes de facturation (le formulaire les fait accepter).

### Champs (O = obligatoire) et réponses

- **First Name (O)** / **Last Name (O)** : `Lazar` / `Ciric`
- **Institution Name (O)** : `NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay` — ou le seul nom de l'établissement d'inscription si Lazar préfère qu'il corresponde exactement au domaine de l'adresse.
- **Institutional Email Address (O)** : [COURRIEL ÉTABLISSEMENT]
- **Phone Number (O)** : [TÉLÉPHONE]
- **AWS Account ID (O)** : [IDENTIFIANT DU COMPTE AWS, 12 chiffres]
- **Area of Research Study (O)** : `Computer & Information Sciences`
- **Research Led By (O)** : options `Myself` / `Faculty Member/PI` / `Other`. Recommandation : `Myself` (tu mènes le projet ; l'accord du directeur est dit dans la proposition). `Faculty Member/PI` si ton directeur préfère apparaître comme responsable.
- **Requested Credit Amount in USD (O)** : [TOTAL DU CALCULATEUR]
- **AWS Pricing Calculator URL (O)** : [ADRESSE DE L'ESTIMATION]
- **Project Title (O)** :
```text
An open benchmark for catching diffuse sabotage by AI agents from their internal activations
```
- **Project Proposal (O)** — pas de limite écrite dans le formulaire relevé (434 mots). La page demande : problème, résumé, services AWS, calendrier et jalons, partage des résultats, usage futur d'AWS, employés d'AWS contactés, jeux de données publics d'AWS.
```text
Problem. AI agents doing long research or analysis tasks can sabotage diffusely: each step looks honest, but the damage adds up. Monitors that read only the agent's text may miss it. This project builds and releases an open benchmark and test harness to check whether monitors that read an agent's internal activations (linear probes) catch such sabotage better than strong text-only monitors. It is part of my PhD at NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay, and my supervisor supports this application.

Summary. Test agents built on open-weight models (Llama-3.1-8B and similar) do long tasks either honestly or with sabotage I plant, so the ground truth is known. I compare linear probes on their activations with text-only monitors: LLM judges, including Claude models, and simpler statistics. One kind of sabotage is kept out of monitor design, and results are reported for each kind. I also connect a known result from steganography and nuclear safeguards (a square-root law for how much damage can hide when it is spread thin) to the monitoring of AI agents, and test where it holds on probe scores. Each decisive experiment is preregistered and sealed with a SHA-256 hash before results are read. Negative results are reported.

AWS services. Amazon EC2 GPU instances, on demand or spot (48 GB class, such as the g6e family), to record activations and train and test probes. Amazon S3 to store activations and sealed outputs. Amazon Bedrock (Claude in Amazon Bedrock) for text judges, if Bedrock use is covered by this program. Please tell me whether charges for Anthropic models used through Amazon Bedrock can be paid with the credits; if not, please apply the award to EC2 and S3 only.

Timeline (12 months). Months 1-2: move the harness to AWS, reproduce my calibration runs, publish the harness. Months 3-6: sealed comparison of probes and text-only monitors, kind of sabotage by kind, held-out kind included. Months 7-9: release of the benchmark and a first paper. Months 10-12: replications by others on the released harness, and a second paper.

Sharing. Open-source harness and probe code; the benchmark with planted ground truth, released after the held-out evaluation; sealed preregistrations and run records (seeds, versions, commits) in a public repository ([LIEN DÉPÔT PUBLIC]); papers in which every number traces to a sealed file.

Future use of AWS. The harness runs on standard EC2 GPU instances, so others can replicate the results on AWS. I would keep using AWS for later cycles, funded by [SOURCE DE FINANCEMENT].

AWS employees contacted: none. AWS public data sets: none planned.

Drafted with help from Claude and edited by me.
```
- **Project Type (O)** : `Developing Open Source Software` (ou `Evaluation/Comparison`)
- **Does your research project have additional external funding sources? (O)** : [Yes / No — financement de la thèse à vérifier] ; si « Yes », « Please provide your Notice Number » (facultatif)
- **Country / Region (O)** : `France` ; **State/Province (O)** : `Île-de-France` ; **Postal Code (O)** : [CODE POSTAL DE L'ÉTABLISSEMENT]
- **Industry (O)** : `Education`
- **Job Role (O)** : `PhD Student`
- **Job Title (O)** : `PhD student`
- **Level of AWS Usage (O)** : [`Do not use AWS today` ou `Evaluating/experimenting with AWS`]
- **Use Case (O)** : `AI & Machine Learning`

---

## B. Google — Google Cloud research credits

### Ce que Lazar fait

1. Un compte de facturation Google Cloud (https://console.cloud.google.com/billing) ; noter son identifiant (« an 18 digit alphanumeric code »). Ne rien lancer avant que le crédit apparaisse : « Google Cloud credits are not retroactive. »
2. Une estimation dans le calculateur de Google : machine à carte graphique (L4 ou A100) pour [N] heures, stockage ; **total au plus 1 000 USD** (plafond doctorant).
3. Remplir le formulaire de https://edu.google.com/programs/credits/research/ .
4. Délai : « within 6-8 weeks ». Questions : gcpresearchcredits@google.com. Validité : 365 jours ; activation dans les 60 jours qui suivent la date de début déclarée. Mention à faire dans les papiers si octroi : « This material is based upon work supported by the Google Cloud Research Credits program with the award [NUMÉRO]. »

### Champs (* = obligatoire sur la page) et réponses

- **First name \*** / **Last name \*** : `Lazar` / `Ciric`
- **Email address (Institution account preferred)** : [COURRIEL ÉTABLISSEMENT]
- **Country \*** : `France` ; **State** : sans objet
- **Job Title \*** : `PhD Student`
- **Organization Name \*** : [ÉTABLISSEMENT D'INSCRIPTION, à choisir dans la liste du formulaire : Université Paris-Saclay ou ENS Paris-Saclay selon ce qui est proposé et ce qui correspond à l'adresse]
- **Type of institution (optional)** : `University`
- **Department name (optional)** : `NeuroSpin (CEA)`
- **Link to your profile in your institution's faculty or researcher directory** : [LIEN ANNUAIRE, s'il existe]
- **Link to URL showing your candidacy status** : [LIEN PROUVANT L'INSCRIPTION EN THÈSE, par exemple la page de la thèse sur theses.fr si elle existe]
- **How did you hear about the program? \*** : `Google Search`
- **Project name \*** :
```text
Catching diffuse sabotage by AI agents from their internal activations: an open benchmark
```
- **Project start date \*** : [DATE, au plus tôt huit semaines après le dépôt ; le crédit doit être activé dans les 60 jours qui suivent]
- **Proposal \*** — 250 mots au plus (240 mots) ; la page demande : « research problem to be solved, GCP tools to be used, project timeline, key milestones and outcomes, and how GCP can support your research in the future ».
```text
Research problem. AI agents doing long research tasks can sabotage diffusely: each step looks honest, but the damage adds up, and monitors that read only the agent's text may miss it. As part of my PhD at NeuroSpin (CEA, Université Paris-Saclay), with ENS Paris-Saclay, I test whether linear probes on an agent's internal activations catch such sabotage better than strong text-only monitors. Test agents built on open-weight models (Llama-3.1-8B and similar) work honestly or with sabotage I plant, so the ground truth is known; one kind of sabotage is kept out of monitor design. Each decisive experiment is preregistered and sealed before results are read; negative results are reported.

GCP tools. Compute Engine GPU instances (L4 or A100 class) to record activations and train probes; Cloud Storage for activations and sealed outputs; optionally Claude models through Model Garden as text judges, if research credits cover partner models (please advise).

Timeline and milestones (12 months). Months 1-2: port the harness, reproduce calibration runs, publish it. Months 3-6: sealed comparison of probes and text-only monitors. Months 7-9: release of a benchmark with planted ground truth, and a paper. Months 10-12: replications and a second paper.

Outcomes. Open-source harness and probe code, the benchmark, sealed preregistrations, and papers.

Future use. The harness runs on standard Compute Engine GPU instances, so others can replicate on Google Cloud; I would keep using it in later cycles.

Drafted with help from Claude and edited by me.
```
- **Field of research \*** : `Computer & Information Sciences`
- **Google scholar link (Optional)** : [PROFIL SCHOLAR, s'il existe]
- **How do you intend to apply awarded cloud credits? \*** : `Developing Open Source Software` (ou `Evaluation/Comparison`)
- **Does your research project have an external funding source? \*** : [Yes / No]
- **Have you used cloud infrastructure for your research before? \*** : `Yes` (cartes graphiques louées ; calcul intensif à NERSC autrefois)
- **Have you used Google Cloud before? \*** : [Yes / No]
- **Expected costs (total and calculator link)** : [TOTAL, au plus 1 000 USD] ; [ADRESSE DE L'ESTIMATION]
- **Google Cloud Billing Account ID \*** : [IDENTIFIANT DU COMPTE DE FACTURATION]
- **After your credit expires, how do you intend to continue funding your project? \*** (23 mots)
```text
Later cycles will be funded by [SOURCE DE FINANCEMENT] and other research credit programs. Compute needs stay modest: single-GPU runs on 8-billion-parameter models.
```
- **Would you like to receive periodic emails…? \*** : `No`
- Conditions sous le formulaire, pour un doctorant : « You represent that the credit will only be used in connection with the project described in this application form and in Your capacity as a PhD student at Your educational institution. »

### Voir à quoi s'appliquent les crédits, dans la console de Google

D'après la documentation officielle de Google (« Resolve Cloud Billing issues », section « View promotional credits applied to your account », page mise à jour le 2026-11-12 ; copie et empreinte dans `LISEZMOI-complement-1-v1.md`) :

1. Console Google Cloud → **Billing → Credits** (en français, sans doute **Facturation → Crédits** : libellé non vérifié). Adresse directe donnée par la documentation : https://console.cloud.google.com/billing/credits
2. Choisir le compte de facturation demandé à l'invite.
3. La page liste chaque crédit avec, mot pour mot : « the Credit name , the Status of the credit (available, used, or expired), the Remaining value and Original value , the Type (recurring or one-time), the Credit ID that appears on invoices, the **Scope if the credit is restricted to particular services or SKUs**, and the Start date and End date ». **C'est la colonne « Scope » qui dit à quoi s'applique le crédit.**
4. Pour vérifier sur la dépense réelle (par exemple si un appel à Claude par Model Garden a été couvert) : Billing → **Reports**, regrouper par produit et par « SKU », et regarder la colonne des économies (« Other savings ») ; le filtre « Savings » permet de cocher ou décocher « Promotional credits », que la documentation définit ainsi : « Promotional credits are things like spend-based milestone credits , Google Cloud Free Trial , and marketing campaign credits, or other grants to use Google Cloud. » (« Billing reports: View and analyze your savings », même dossier).

Non vérifié : que le crédit de recherche s'affiche bien comme « promotional credit » sur cette page (probable d'après la définition, non écrit pour ce programme), et ce que sa colonne « Scope » contiendra. D'où le courriel ci-dessous, à envoyer avant de compter sur Claude dans le budget.

### Courriel de question à Google (facultatif, avant le dépôt)

**À** : gcpresearchcredits@google.com — **Objet** : `Research credits: are Anthropic Claude partner models covered?` (86 mots)
```text
Hello,

I am a PhD student at NeuroSpin (CEA, Université Paris-Saclay) and am preparing an application to the Google Cloud research credits program, for a project on monitoring AI agents. Most of the award would pay for Compute Engine GPU instances. I would also like to use Anthropic's Claude models through Model Garden as text judges. Can research credits pay for these partner models, or only for Google Cloud products? If they cannot, I will request credits for compute and storage only.

Thank you,
Lazar Ciric
```

## Réserves

- Le texte d'Amazon et celui de Google disent « Drafted with help from Claude and edited by me. » ; Google compte cette phrase dans ses 250 mots.
- Sur la couverture de Claude par ces crédits, rien de neuf depuis la v1 : non établie chez les deux fournisseurs ; les textes demandent par écrit. Ne compter que sur les cartes graphiques et le stockage.
- Recevoir ces crédits puis lancer une course chez Amazon ou Google reste une dépense de calcul au sens des règles du dépôt : devis et GO par ligne. La garde de calcul du dépôt ne connaît aujourd'hui ni Amazon ni Google.
- Les familles d'instances (g6e, L4, A100) sont des exemples à confirmer dans les calculateurs ; aucun prix n'est avancé.

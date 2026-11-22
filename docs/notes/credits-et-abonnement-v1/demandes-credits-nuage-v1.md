# Demandes de crédits de recherche chez Amazon et Google, avec Claude servi par Amazon Bedrock et par Google Cloud (version 1)

- Date : 2026-11-22T07:57:24Z (`date -u`) ; pages relevées entre 07:48Z et 07:56Z.
- Rôle : où et comment déposer, champs exacts des deux formulaires, réponses prêtes à coller en anglais ; Claude chez chaque fournisseur (modèles, identifiants) ; ce que les crédits couvrent. Rien n'a été envoyé ; le directeur dépose lui-même.
- Résumé commun : `docs/notes/credits-et-abonnement-v1/resume-programme-pour-demandes-v1.md`. Mot de Lazar : GO-2026-11-22-32.

## Pages consultées (copies et empreintes dans `docs/sources/credits-recherche-v1/LISEZMOI-v1.md`)

| page | adresse |
|---|---|
| Programme de crédits de recherche d'Amazon | https://aws.amazon.com/research-credits/ ; foire aux questions https://aws.amazon.com/research-credits/faq/ |
| Formulaire d'Amazon | https://pages.awscloud.com/aws-cloud-credit-for-research.html (formulaire Marketo 65772, champs relevés dans le HTML) |
| Conditions des crédits promotionnels d'Amazon (lien « Terms and Conditions » de la page du programme) | https://aws.amazon.com/awscredits/ (mises à jour le 24 septembre 2026) |
| Claude chez Amazon (page d'Amazon) | https://aws.amazon.com/bedrock/anthropic/ |
| Claude chez Amazon (documentation d'Anthropic) | https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock ; https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy ; https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws |
| Table des modèles d'Anthropic | https://platform.claude.com/docs/en/models/overview |
| Programme de crédits de recherche de Google, avec son formulaire | https://edu.google.com/programs/credits/research/ |
| Aide du programme de Google | https://support.google.com/google-cloud-higher-ed/answer/10324705 (éligibilité), /10723679 (usage des crédits), /10724468 (dépôt), /10724373 (contact) |
| Claude chez Google (page de Google) | https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude |
| Claude chez Google (documentation d'Anthropic) | https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed |

**Vérifié en ligne** : les deux programmes, leurs conditions d'éligibilité, montants, délais ; les champs des deux formulaires ; les modèles Claude servis et leurs identifiants chez Amazon et chez Google (pages d'Anthropic et des fournisseurs, même jour) ; l'exclusion d'« AWS Marketplace » dans les conditions des crédits d'Amazon. **Non vérifié** : que les crédits de recherche d'Amazon couvrent Claude dans Amazon Bedrock (aucune page ne le dit pour ce programme ; voir plus bas) ; que les crédits de Google couvrent Claude sur Google Cloud (aucune page officielle ne le dit ; des fils de discussion de la communauté se contredisent, non retenus comme preuve) ; l'éligibilité du directeur (elle dépend de [AFFILIATION]).

## D'abord, l'éligibilité : bloquante sans établissement

- **Amazon** (foire aux questions) : « Full-time faculty at an accredited research institution; Full-time research staff at an accredited research institution; or Graduate, post-graduate or PhD students enrolled at an accredited research institution. » Et : « We require applicants provide their official institution-issued email ID (.edu, .org, or equivalent) […] Applications from non-institution domains will not be accepted. » Aussi : « Research credit will not support administrative workloads, operations, and ongoing or established research projects. » ; trois types de projet admis : preuve de concept ou comparaison, solutions réutilisables et partageables, ateliers.
- **Google** (aide, éligibilité) : « Applicant must be part of faculty, a PhD student or a Postdoctoral researcher at a regionally accredited academic institution or nonprofit research institution » dans une liste de pays (la France y figure). Montant : jusqu'à 5 000 USD pour un enseignant-chercheur ou un postdoctorant, une seule fois ; 1 000 USD par an pour un doctorant.
- **Conséquence** : sans [AFFILIATION] reconnue et une adresse de l'établissement, **les deux demandes seraient refusées** ; ne pas les déposer au nom d'un chercheur indépendant. Le directeur tranche.

## Claude chez chaque fournisseur : modèles et identifiants (relevés le 2026-11-22)

| modèle | interface d'Anthropic | Amazon Bedrock | Google Cloud (géré par Google) |
|---|---|---|---|
| Claude Fable 5.2 | `claude-fable-5-2` | base `anthropic.claude-fable-5-2`, **seulement sur le point d'accès « bedrock-runtime »** (appels InvokeModel et Converse), par profil d'inférence `global.anthropic.claude-fable-5-2` (écrit sur la table des modèles) ou `us.anthropic.claude-fable-5-2` (déduit de la règle « base plus préfixe » de la page ; préfixes eu, jp, apac : non) ; absent de « Claude in Amazon Bedrock » | `claude-fable-5-2` |
| Claude Opus 5.5 | `claude-opus-5-5` | `anthropic.claude-opus-5-5` sur « Claude in Amazon Bedrock » (interface Messages, point d'accès « bedrock-mantle ») ; accès « See Access » : critères fixés par Amazon, à vérifier dans la console | `claude-opus-5-5` |
| Claude Opus 4.6 | `claude-opus-4-6` (identifiant servi dans nos appels du 22 novembre : en-tête de `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-15-opus46/relecture-fable-api.md`) | base `anthropic.claude-opus-4-6-v1` sur « bedrock-runtime », profils `global.`, `us.`, `eu.`, `jp.`, `apac.` (par exemple `global.anthropic.claude-opus-4-6-v1`) | `claude-opus-4-6` |

Remarques relevées sur les pages :
- Amazon : « AWS offers newer Claude models through cross-region inference rather than on-demand throughput » : passer l'identifiant du profil (avec préfixe), sinon erreur 400.
- Amazon : « The models numbered 4.6 or lower in the model table on this page don't support 2026-10-21 on Bedrock » : pour Opus 4.6, épingler la version du kit (`pip install -U "anthropic[bedrock]<2"`, commande de la page).
- Google : « Anthropic models are not a Google product » ; leur activation passe par « Google Cloud Marketplace entitlements » ; Google facture (« Google Cloud invoices you »), quotas fixés par Google ; disponibilité par région à vérifier dans Model Garden.
- Une troisième voie existe chez Amazon : « Claude Platform on AWS », exploitée par Anthropic, « billed through AWS Marketplace », identifiants identiques à ceux de l'interface d'Anthropic.
- Pour l'appariement des bras : les identifiants Google sont ceux d'Anthropic, ceux d'Amazon portent un préfixe ; les dates de retrait chez les fournisseurs « can differ from the Claude API schedule ». Un même nom de modèle chez deux fournisseurs n'est pas prouvé identique au bit près : chaque course consigne le fournisseur et l'identifiant servi, et un bras ne change pas de fournisseur.

## Les crédits couvrent-ils Claude ?

**Amazon.** Le lien « Terms and Conditions » de la page du programme renvoie aux conditions générales des crédits promotionnels : « Unless authorized by us, Promotional Credit will not be applied to any fees or charges for […] AWS Marketplace […] ». La documentation d'Anthropic distingue : « Claude in Amazon Bedrock: An AWS-native service. Managed in the Amazon Bedrock console and billed as AWS service usage. » et « Claude Platform on AWS (this page): The Claude API platform billed through AWS Marketplace. » Lecture [proposition, non vérifiée] : Claude dans Amazon Bedrock a des chances d'être couvert, Claude Platform on AWS non ; pour « bedrock-runtime » (Fable 5.2, Opus 4.6), le mode de facturation n'est pas écrit sur les pages lues. Les conditions ajoutent : « Promotional Credit will be applied only to the specific Services designated by your AWS contracting entity » : **à faire confirmer par écrit** (question insérée dans la proposition ci-dessous). Les cartes graphiques pour les sondes sont, elles, couvertes : « Amazon EC2 usage supported by AWS Promotional Credit will be for on-demand and spot instances only. »

**Google.** Les crédits « can be used for most computing services on Google Cloud such as storage, compute, and data analysis » et le formulaire dit « The credit is valid for Google Cloud Platform products ». Claude n'est « not a Google product » et passe par des droits de la place de marché. **Couverture de Claude : non établie** ; à demander par écrit avant de s'y fier (courriel prêt plus bas). Les machines à cartes graphiques de Google sont couvertes (« compute »).

**Conséquence pratique** [proposition] : chez les deux fournisseurs, demander d'abord pour les **heures de cartes graphiques** (sondes sur Llama 3.1 8B), qui sont sûrement couvertes, et pour Claude seulement en second, sous réserve de la réponse écrite. Régime des données : chez Amazon, « Amazon Bedrock governs data handling for Claude in Amazon Bedrock » (et « zero operator access: Anthropic personnel have no access to the inference infrastructure ») ; chez Google, journalisation des requêtes optionnelle (« Enable 30-day request-response logging ») : ne pas l'activer sur les courses qui portent des secrets de mesure.

---

## A. Amazon — AWS Cloud Credit for Research

### Ce que le directeur doit faire

1. Créer ou choisir un **compte AWS payant** (la page : « Effective February 16, 2026, Free Tier accounts will be ineligible for promotional credits »). Noter l'identifiant à 12 chiffres (console, menu du compte).
2. Faire une **estimation dans le calculateur de prix d'AWS** (https://calculator.aws/) : par exemple une instance à carte graphique de 48 Go ou plus (famille g6e ou équivalent) pour [N] heures à la demande ou en « spot », plus le stockage, plus, en ligne à part, Amazon Bedrock pour Claude Opus 5.5 avec [N] millions de jetons d'entrée et de sortie. Enregistrer et copier l'adresse de partage de l'estimation (champ obligatoire). Le montant demandé doit égaler le total du calculateur.
3. Ouvrir https://pages.awscloud.com/aws-cloud-credit-for-research.html , remplir le formulaire avec les réponses ci-dessous, **avec l'adresse de l'établissement**. Ne pas cocher la case de consentement aux courriels commerciaux (facultative).
4. Délai : la page du formulaire dit « Typical review cycles are 30 to 60 days », la page du programme « 90 to 120 days » (les deux textes sont en ligne). Réponse par aws-research-credit@amazon.com (« Please check your spam folders »). Validité des crédits : un an.

### Champs (O = obligatoire) et réponses

- **First Name (O)** / **Last Name (O)** : [PRÉNOM] / [NOM]
- **Institution Name (O)** : [AFFILIATION]
- **Institutional Email Address (O)** : [COURRIEL DE L'ÉTABLISSEMENT]
- **Phone Number (O)** : [TÉLÉPHONE]
- **AWS Account ID (O)** : [IDENTIFIANT DU COMPTE AWS, 12 chiffres]
- **Area of Research Study (O)** : `Computer & Information Sciences`
- **Research Led By (O)** : `Myself` (ou `Faculty Member/PI` selon [AFFILIATION])
- **Requested Credit Amount in USD (O)** : [TOTAL DU CALCULATEUR]
- **AWS Pricing Calculator URL (O)** : [ADRESSE DE L'ESTIMATION]
- **Project Title (O)** : `An open, reproducible benchmark for white-box monitoring of diffuse sabotage by AI agents`
- **Project Proposal (O)** — la page demande : description (problème, résumé, services AWS, calendrier et jalons), partage des résultats, usage futur d'AWS, employés d'AWS contactés, jeux de données publics d'AWS. Texte à coller :

> **Problem statement.** AI agents doing long research or analysis tasks can sabotage diffusely: each step looks honest, but damage accumulates. Monitors that read the agent's text may miss this. This project builds and releases an open benchmark and harness to evaluate whether monitors that read an agent's internal activations (linear probes) detect diffuse sabotage better than strong black-box baselines.
>
> **Project summary.** Test organisms on open-weight models (Llama 3.1 8B and similar) perform long tasks honestly or with planted diffuse sabotage, so ground truth is known. We compare linear probes on internal activations with text judges (including Claude models) and named baselines, with one sabotage mode held out from monitor design and results reported per mode. Every decisive experiment is pre-registered and sealed (SHA-256) before results are read; negative results are reported.
>
> **Proposed AWS services.** Amazon EC2 GPU instances, on-demand or spot (a 48 GB-class GPU such as the g6e family), to extract activations and train and evaluate probes; Amazon S3 for activation stores and sealed outputs; Amazon Bedrock (Claude in Amazon Bedrock, for example `anthropic.claude-opus-5-5`) for text judges, if Bedrock usage is an eligible service under this program. Please confirm whether charges for Anthropic models used through Amazon Bedrock can be covered by the awarded credit; if not, please allocate the award to EC2 and S3 only.
>
> **Timeline and milestones (12 months).** Months 1–2: port the harness to AWS, reproduce existing calibration runs, publish the harness. Months 3–6: sealed comparison of probes versus black-box baselines per sabotage mode, held-out mode included. Months 7–9: release of the planted-ground-truth benchmark and a paper. Months 10–12: replications by others on the released harness; second paper.
>
> **Plan for sharing outcomes.** Open-source harness and probe-training code; the benchmark with planted ground truth (released after the held-out evaluation); sealed pre-registrations and run manifests (seeds, versions, commits) in a public redacted repository ([LIEN DÉPÔT PUBLIC]); papers with every number traced to a sealed file.
>
> **Future use of AWS.** The released harness will run on standard EC2 GPU instances so that others can replicate our results on AWS; we would continue to use AWS for follow-up cycles, funded by [SOURCE DE FINANCEMENT FUTURE, ou « our own budget »].
>
> **AWS employees contacted.** None.
>
> **AWS Public Data Sets.** None planned.

- **Project Type (O)** : `Developing Open Source Software` (ou `Evaluation/Comparison`)
- **Does your research project have additional external funding sources? (O)** : [Yes / No] — si « Yes », le champ « Please provide your Notice Number » apparaît (facultatif)
- **Country / Region (O)** : [PAYS] ; **State/Province (O)** : [RÉGION] ; **Postal Code (O)** : [CODE POSTAL]
- **Industry (O)** : `Education` (ou `Non-Profit Organization`)
- **Job Role (O)** : `Academic / Researcher` (ou `Faculty`, `Postdoctoral Researcher`, `PhD Student`)
- **Job Title (O)** : [TITRE]
- **Level of AWS Usage (O)** : `Evaluating/experimenting with AWS` (ou `Do not use AWS today`)
- **Use Case (O)** : `AI & Machine Learning`
- Texte final du formulaire : participation sous l'« AWS Customer Agreement » et les conditions du programme ; « I agree to set up Billing Alerts » : **mettre des alertes de facturation** dès l'octroi, et rapprocher chaque dépense d'un GO.

---

## B. Google — Google Cloud research credits

### Ce que le directeur doit faire

1. Créer un **compte de facturation Google Cloud** (https://console.cloud.google.com/billing) et noter son identifiant (« an 18 digit alphanumeric code » d'après l'aide ; le formulaire limite le champ à 25 caractères). Ne rien lancer avant que le crédit apparaisse : « Google Cloud credits are not retroactive. »
2. Faire l'estimation dans le calculateur de Google (lien « Pricing calculator » du formulaire) : machine à carte graphique (par exemple une carte L4 ou A100) pour [N] heures, stockage ; Claude en ligne à part si on le garde.
3. Ouvrir https://edu.google.com/programs/credits/research/ , remplir le formulaire de la page avec les réponses ci-dessous.
4. Délai : « we review and make decisions on applications within 6-8 weeks ». Questions : gcpresearchcredits@google.com (page d'aide « Training and billing support »). Validité : 365 jours ; activation sous 60 jours après la date de début déclarée.
5. Mention à faire dans les papiers si octroi (aide) : « This material is based upon work supported by the Google Cloud Research Credits program with the award [NUMÉRO]. »

### Champs (* = obligatoire sur la page) et réponses

- **First name \*** / **Last name \*** : [PRÉNOM] / [NOM]
- **Email address (Institution account preferred)** : [COURRIEL DE L'ÉTABLISSEMENT]
- **Country \*** : [PAYS] (liste fermée ; « If your country is not on this list, you can still express interest ») ; **State** : sans objet hors des États-Unis
- **Job Title \*** : choix `Faculty` / `Postdoctoral Researcher` / `PhD Student` / `IT Admin` → [selon AFFILIATION]
- **Organization Name \*** : [AFFILIATION] (à choisir dans la liste proposée)
- **Type of institution (optional)** : `University` ou `Nonprofit Research Institution`
- **Department name (optional)** : [DÉPARTEMENT]
- **Link to your profile in your institution's faculty or researcher directory** : [LIEN ANNUAIRE]
- **Link to URL showing your candidacy status** : (doctorants seulement) [LIEN]
- **How did you hear about the program? \*** : `Google Search`
- **Project name \*** : `White-box monitoring of diffuse sabotage by AI agents: an open benchmark`
- **Project start date \*** : [DATE, au plus tôt huit semaines après le dépôt ; le crédit doit être activé dans les 60 jours qui suivent]
- **Proposal \*** (250 mots au plus ; « research problem to be solved, GCP tools to be used, project timeline, key milestones and outcomes, and how GCP can support your research in the future ») — 232 mots :

> Research problem. AI agents doing long research tasks can sabotage diffusely: each step looks honest, but damage accumulates, and monitors that read only the agent's text may miss it. We test whether linear probes on an agent's internal activations detect diffuse sabotage better than strong black-box baselines (text judges, word-and-cost statistics, cascades, last-state readers). Test organisms on open-weight models (Llama 3.1 8B and similar) work honestly or with planted sabotage, so ground truth is known; one sabotage mode is held out from monitor design. Every decisive experiment is pre-registered and sealed before results are read; negative results are reported.
>
> GCP tools. Compute Engine GPU instances (L4 or A100 class) for activation extraction and probe training; Cloud Storage for activation stores and sealed outputs; optionally Claude models through Model Garden as text judges, if partner-model charges are covered by research credits (please advise).
>
> Timeline and milestones (12 months). Months 1–2: port the harness, reproduce calibration runs, publish it. Months 3–6: sealed comparison of probes versus baselines per sabotage mode. Months 7–9: release of a planted-ground-truth benchmark and a paper. Months 10–12: replications and a second paper.
>
> Outcomes. Open-source harness and probe code, the benchmark, sealed pre-registrations and run manifests in a public redacted repository, and papers.
>
> Future use. The released harness runs on standard Compute Engine GPU instances, so others can replicate on Google Cloud; we would keep using it for follow-up cycles.

- **Field of research \*** : `Computer & Information Sciences`
- **Google scholar link (Optional)** : [PROFIL SCHOLAR]
- **How do you intend to apply awarded cloud credits? \*** : `Developing Open Source Software` (ou `Evaluation/Comparison`)
- **Does your research project have an external funding source? \*** : [Yes / No]
- **Have you used cloud infrastructure for your research before? \*** : `Yes` (cartes louées chez un loueur et serveurs loués)
- **Have you used Google Cloud before? \*** : [Yes / No]
- **Expected costs (total and calculator link)** : [TOTAL] ; [ADRESSE DE L'ESTIMATION] (au plus 5 000 USD pour un enseignant-chercheur ou postdoctorant)
- **Google Cloud Billing Account ID \*** : [IDENTIFIANT DU COMPTE DE FACTURATION]
- **After your credit expires, how do you intend to continue funding your project? \*** :
  > Follow-up cycles will be funded from [SOURCE, ou « the program's own budget »] and other research credit programs; the released harness keeps compute needs modest (single-GPU runs on 8B-parameter models).
- **Would you like to receive periodic emails…? \*** : `No`
- Conditions affichées sous le formulaire : crédit non cessible ; pour un enseignant-chercheur, accepté « on behalf of Your educational institution […] and not for Your personal use » : à vérifier avec [AFFILIATION] avant dépôt.

### Courriel de question à Google (facultatif, avant ou avec le dépôt)

**À** : gcpresearchcredits@google.com

> **Subject:** Research credits — are Anthropic Claude partner models covered?
>
> Hello,
>
> I am preparing an application to the Google Cloud research credits program for a project on white-box monitoring of AI agents. Most of the award would fund Compute Engine GPU instances. I would also like to use Anthropic Claude models through Model Garden (Claude on Google Cloud, Google managed) as text judges. Can research credits be applied to charges for these partner models, or only to Google Cloud products? If they cannot, I will request credits for compute and storage only.
>
> Thank you,
> [NOM], [AFFILIATION]

*Traduction* : « Objet : crédits de recherche — les modèles Claude d'Anthropic sont-ils couverts ? Bonjour, je prépare une demande pour un projet sur la surveillance boîte blanche des agents ; l'essentiel servirait aux machines à cartes graphiques ; j'aimerais aussi employer Claude par Model Garden comme juge de texte. Les crédits s'appliquent-ils à ces modèles de partenaires, ou seulement aux produits de Google ? Sinon, je demanderai seulement le calcul et le stockage. Merci. »

## Réserves

- Les montants des calculateurs ne sont pas fournis ici : ils se font dans les consoles, avec le compte du directeur (aucune donnée personnelle envoyée d'ici).
- Les noms de familles d'instances (g6e, L4, A100) sont des exemples à confirmer dans le calculateur ; aucun prix n'est avancé.
- Recevoir ces crédits, puis lancer une course chez Amazon ou Google, reste une dépense de calcul au sens des règles du dépôt : devis et GO par ligne, comme pour le loueur de cartes ; la garde de calcul du dépôt ne connaît aujourd'hui ni Amazon ni Google.
- Le portage d'une mesure d'un fournisseur à l'autre (identifiants, versions du kit, quotas) est un écart à déclarer dans tout texte scellé qui nomme l'interface d'Anthropic.

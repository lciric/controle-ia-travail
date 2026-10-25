# Demandes de calcul et de bourse pour la voie chère (concepteur entraîné) et le programme — brouillon v1

Écrit le 25 octobre 2026 (08:40 UTC) par la lignée « conv-audit », sur le « go » de Lazar (09:05, heure de Paris). **Tu
rédiges, Lazar envoie** : rien n'est envoyé par moi ; aucun contact externe. Tous les chiffres de budget sont des
**ordres de grandeur, hypothèses de devis, non opposables (R7)** ; les faits sur les programmes ont été lus le 25 octobre
2026 sur les pages citées (§ 2), et restent à vérifier par toi avant tout envoi (conditions, formulaires, dates).

## 0. Verdict

- Le programme a deux besoins de calcul distincts : des **appels aux modèles de frontière** (dollars d'interface ; c'est ce
  qui bloque aujourd'hui : crédit Anthropic) et des **heures de carte graphique** (sondes, adaptateur, et la voie « tout
  ouvert » du concepteur entraîné).
- Les deux programmes qui collent le mieux, et qu'on peut saisir **tout de suite** : **Coefficient Giving** (ex Open
  Philanthropy), demande de propositions « recherche technique en sûreté de l'IA », au fil de l'eau, sans condition
  d'affiliation, qui nomme le **contrôle de l'IA** et finance des **crédits d'interface et du calcul** ; et **Anthropic, AI
  for Science** (jusqu'à 20 000 USD de crédits d'interface sur six mois, chercheurs rattachés à une institution, évaluation
  mensuelle). Puis **GENCI, accès dynamique** à Jean Zay (jusqu'à 50 000 heures GPU, ouvert en permanence, gratuit) si ton
  rattachement le permet. Le reste (OpenAI, Google TPU Research Cloud) est secondaire ; l'Alignment Project de l'AISI
  britannique est fermé.
- La candidature existante « White-Box Control of Diffuse Threats » (EA Funds, Transformative AI Fund) reste ton dossier
  principal : le volet ci-dessous s'y ajoute comme **mise à jour**, il ne la remplace pas.

## 1. Le volet à financer : apprendre la structure, la composition et l'entraînement de l'organisme, de génération en génération

**Ce que nous avons** (phase 0, instruments) : un noyau fixe qui fait vivre des organismes écrits par des modèles ; une
banque de tâches de contrôle (conscience d'évaluation ; contrôle d'un agent délégué, sabotage et signalement omis) à
vérité cachée ; des préenregistrements scellés et contre-lus ; l'étape 1 (sondes conçues par les organismes sur les
activations de Llama-3.1-8B-Instruct) prête à sceller ; l'étape 2 (adaptateur LoRA affiné par renforcement, récompense
écrite par l'organisme) décrite ; la confrontation d'essaims (apprentissage par réécriture contre bras gelé) en
préenregistrement.

**Ce que le volet ajoute** : faire apprendre la **conception** elle-même, de génération en génération, au lieu de la
confier à un modèle de frontière figé. Trois voies, du moins cher au plus cher :

| voie | ce qui apprend | calcul | ordre de grandeur (hypothèse) |
|---|---|---|---|
| V1 « tout ouvert » | un même modèle à poids ouverts (8 milliards de paramètres, puis plus grand) est concepteur et exécutant ; une seule politique, récompense = score de l'organisme conçu | carte graphique seulement | quelques centaines à 1 000 USD de location, ou ≈ 300 à 1 000 heures H100 |
| V2 « épisodes courts » | concepteur ouvert entraîné par renforcement, exécutants de frontière mais épisodes réduits (peu de tâches, modèles moins chers) | carte + interface | ≈ 2 000 à 5 000 USD |
| V3 « voie chère » | concepteur ouvert entraîné par renforcement, **un épisode = une génération entière** servie par les modèles de frontière ; ≈ 2 000 à 5 000 épisodes à 5 à 20 USD | interface surtout | **≈ 10 000 à 40 000 USD** d'interface (jusqu'à 100 000 à 5 000 épisodes), plus quelques centaines d'USD de carte |

Ce qui serait jugé, quelle que soit la voie : exactitude sur des **familles de tâches jamais vues**, contre un **bras
apparié sans apprentissage**, sur des tâches de contrôle ; et les **dérives** : diversité des rôles, sur-ajustement au jeu
de développement, exploitation du score, **signalement aux humains qui baisse** (l'« insularité » rapportée par Avalon-M1).
Ce qui serait peut-être neuf, à vérifier durement avant de le revendiquer : un concepteur entraîné qui fait évoluer un
organisme entier (code, mémoire, instruments, spécification d'entraînement) sur plusieurs générations, jugé ainsi ; les
voisins publiés (méta-agents à modèle figé, systèmes qui réécrivent leur code, concepteurs entraînés par tâche,
organisations entraînées par récompense collective) ne tiennent pas les quatre à la fois d'après leurs résumés.

**Budget total demandable** (hypothèse, à refaire sur devis) : interface 15 000 à 50 000 USD (V3 + étape 2 + courses) ;
carte 1 000 à 3 000 USD ou 1 000 à 5 000 heures GPU ; temps humain selon ta candidature existante.

## 2. Les programmes (lus le 25 octobre 2026 ; à vérifier par toi)

| programme | ce qu'il donne | conditions lues | état | pour nous |
|---|---|---|---|---|
| **Coefficient Giving** (ex Open Philanthropy), « Request for Proposals: Technical AI Safety Research », fonds Navigating Transformative AI | subventions de ≈ 10 000 à 2 000 000 USD (bornes estimées par la page relais, pas publiées) ; un type « financement rapide de crédits d'interface et de calcul » ; domaines nommés : alignement, interprétabilité, **contrôle de l'IA et confinement**, évaluation et bancs d'essai de sûreté, supervision, amorçage d'organisations | chercheurs individuels, groupes académiques, organisations ; **aucune affiliation ni pays requis** ; au fil de l'eau ; manifestation d'intérêt ≈ 300 mots d'abord | ouvert (page relais ; vérifier la page officielle) | **premier choix** : couvre V3 et les appels des courses ; dossier court à envoyer dès maintenant |
| **Anthropic, AI for Science Program** | jusqu'à **20 000 USD de crédits d'interface sur 6 mois** | chercheurs rattachés à une institution de recherche (académique ou à but non lucratif) ; champs : sciences de la vie en priorité, mais « Computer Science » et « autres champs » listés ; critères : mérite scientifique, impact, faisabilité, contrôle de biosécurité ; usage soumis à la politique d'usage ; évaluation le premier lundi de chaque mois | ouvert d'après la page (pas de date de clôture lue) | **second choix, immédiat** : lève le blocage du crédit Anthropic ; dire clairement que nos appels classent des transcriptions et conçoivent des instruments, sans contournement de sûreté |
| **GENCI, accès dynamique** (Jean Zay, portail eDARI) | jusqu'à **50 000 heures GPU (équivalent V100)** et 500 000 heures cœur ; gratuit ; allocation en jours ou semaines, pour un an | porteur : membre permanent d'une structure de recherche, post-doctorant ou ingénieur ; pour le comité IA (CT10), un doctorant ou stagiaire de master 2 en laboratoire peut porter ; structure de recherche publique française ou entreprise avec R&D en France ; résultats publiés | ouvert en permanence | **si ton rattachement le permet** (ENS Paris-Saclay : à toi de dire ton statut ; sinon un laboratoire d'accueil et son membre permanent portent) : couvre V1 et les cartes de l'étape 2 |
| OpenAI, Researcher Access Program | jusqu'à 10 000 USD de crédits d'interface sur 12 mois | affiliation académique ou organisation de recherche ; revues en avril, août, décembre | ouvert, prochaine revue décembre | secondaire : nos espèces sont Claude et Gemini ; changer de modèle demande ton GO |
| Google, TPU Research Cloud | TPU gratuits (durée non lue) | formulaire de manifestation d'intérêt ; partager la recherche (publication, code) | ouvert d'après la page | secondaire : notre pile est PyTorch et vLLM sur NVIDIA ; portage à chiffrer |
| AISI (Royaume-Uni), The Alignment Project | subventions et crédits de calcul au cas par cas | — | **fermé** ; « peu probable en 2026 » ; suivre aisi.gov.uk/grants | veille seulement |
| EA Funds, Transformative AI Fund | ta candidature existante | — | en cours (entretien du 21 octobre) | **mise à jour** : y ajouter le volet § 1 |

Sources lues : Coefficient Giving — page relais `grantedai.com` et lien officiel
`https://coefficientgiving.org/funds/navigating-transformative-ai/request-for-proposals-technical-ai-safety-research/` ;
Anthropic — `support.claude.com/en/articles/11199177` ; GENCI — « Modalités d'accès » (PDF, septembre 2023,
`genci.fr`) et portail `edari.fr` ; OpenAI — `help.openai.com/en/articles/10139500` ; Google — `sites.research.google/trc/about/` ;
AISI — `alignmentproject.aisi.gov.uk/how-to-apply`.

## 3. Textes prêts à adapter (à relire par toi ; en anglais quand le programme l'est)

### 3.1. Coefficient Giving — manifestation d'intérêt (≈ 300 mots, anglais)

> **Title.** White-box control of diffuse threats: self-designed organisms that learn to detect evaluation awareness and
> omitted reporting, judged on unseen task families.
>
> **Summary.** We run a preregistered research programme in which language-model-written "organisms" (code plus
> memory, living under a fixed, sandboxed kernel) learn to classify agent transcripts on two control tasks: whether an
> agent believes it is being evaluated, and whether a delegated agent sabotages or omits reporting. Learning happens at
> three levels, each measured against a frozen paired arm on a hidden test split with held-out task families: (1)
> rewriting code and memory with frozen frontier models (score-guided search); (2) gradient-trained instruments the
> organism designs itself — probes on the activations of an open 8B model, then a LoRA adapter trained by reinforcement
> learning with a reward the organism writes; (3) the stage we ask funding for: a mid-size open-weights *designer*,
> trained by reinforcement learning across thousands of episodes, where one episode is one full generation of an
> organism. We measure whether learned design transfers across lineages and unseen families, and whether the trained
> designer drifts toward "organisational insularity" (refusing harmful actions while reporting less to humans), a
> failure recently reported in collectively-rewarded agent organisations.
>
> **Why it matters.** Control evaluations need monitors that generalise beyond the families they were tuned on; a
> designer that learns to build such monitors — and whose own weights we can probe — is a direct test of whether
> self-improving systems can be kept measurable.
>
> **Methods and safeguards.** Every decisive run is preregistered and sealed (hypothesis, prediction, metric, stop list)
> and counter-read by an independent agent before launch; no run targets a positive sign; all kernel code, organisms,
> probes and preregistrations will be released by June 2027 under a research licence.
>
> **Request.** Rapid funding for API credits and compute: [montant] USD over [durée] months — roughly [X] USD of frontier-model
> calls (≈ 2,000–5,000 episodes at 5–20 USD) and [Y] GPU-hours (or [Z] USD of rented GPUs) for the open-weights designer
> and adapters. Principal investigator: [nom, affiliation ou statut indépendant]. Prior support: [EA Funds application,
> état].

### 3.2. Anthropic, AI for Science — description du projet (anglais, court)

> We study whether AI systems that redesign themselves can be kept measurable. Under a fixed, sandboxed kernel,
> organisms written by language models classify agent transcripts on two control tasks (evaluation awareness; sabotage
> and omitted reporting by a delegated agent), with a hidden test split and held-out task families. Claude models are
> called by these organisms to classify transcripts, to deliberate on open design questions, and to write the
> specifications of instruments (probes, adapters) that are then trained on an open 8B model. Our use is classification
> and design on our own transcript bank; it involves no attempts to circumvent safety behaviours. All runs are
> preregistered; code and preregistrations will be released by June 2027. Requested: API credits for ≈ [N] organism
> generations (≈ [X] USD) over six months. Institution: [établissement] ; PI: [nom].

### 3.3. GENCI, accès dynamique — résumé scientifique (français, pour eDARI)

> **Titre.** Instruments d'apprentissage conçus par des organismes auto-écrits pour le contrôle de systèmes d'IA.
>
> **Objectif.** Entraîner, sur un modèle de langue à poids ouverts (Llama-3.1-8B-Instruct, puis un modèle plus grand),
> des instruments de contrôle dont la conception (perte, architecture, données, récompense) est écrite par des organismes
> auto-écrits : sondes sur les activations (étape 1), adaptateur de faible rang affiné par renforcement (étape 2), puis un
> concepteur à poids ouverts entraîné par renforcement à faire évoluer l'organisme de génération en génération (étape 3,
> voie « tout ouvert »). Évaluation sur des familles de tâches tenues à l'écart, contre un bras apparié sans apprentissage.
>
> **Méthodes.** PyTorch, vLLM pour le service des modèles, adaptateurs LoRA, renforcement par groupes (type GRPO) ;
> préenregistrements scellés, graines consignées, manifestes par run.
>
> **Heures demandées** (hypothèse) : extraction d'activations ≈ 2 à 10 h ; étape 2 ≈ 20 à 60 h (A100 ou H100) par
> génération, 5 à 10 générations ; étape 3 « tout ouvert » ≈ 300 à 1 000 h H100 ; total **≈ 1 500 à 2 500 heures GPU
> (équivalent V100 : à convertir selon la grille GENCI)** sur un an ; stockage ≈ [X] To.
>
> **Résultats attendus et publication.** Trois articles (A : instruments ; B : contrôle d'un agent délégué, hypothèse
> H9 ; C : méthodologie des organismes auto-écrits), code et préenregistrements publiés sous licence de recherche en juin
> 2027.
>
> **Porteur.** [nom, statut, laboratoire ou structure d'accueil ; membre permanent porteur si requis].

## 4. Ce que j'attends de toi avant la version envoyable (une ligne chacun)

1. Ton **rattachement** (ENS Paris-Saclay : statut ; laboratoire d'accueil ; un membre permanent qui porterait la demande
   GENCI) — il décide GENCI et Anthropic.
2. L'**ordre des envois** : je recommande Coefficient Giving et Anthropic maintenant, GENCI dès la question 1 réglée ;
   TPU Research Cloud et OpenAI plus tard ou jamais.
3. Les **montants** à inscrire (je mets les ordres de grandeur ci-dessus ; tu tranches la voie V1, V2 ou V3, ou
   plusieurs) — je refais le devis par ligne avant l'envoi.
4. Le **texte de ta candidature EA Funds** (ou son résumé), pour aligner les formulations et ne rien contredire.

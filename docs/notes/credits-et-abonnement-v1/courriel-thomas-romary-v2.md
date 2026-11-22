# Courriel à Thomas Romary (Mines Paris) : suivre le projet et en être le responsable pour « AI for Science » (version 2)

- Date : 2026-11-22T13:34Z (`date -u`). Rédaction assistée (session fille, Claude Opus 5.5), pour Lazar, **qui l'envoie lui-même s'il le souhaite**. Rien n'est envoyé ; personne n'est contacté par cette session.
- Remplace `courriel-thomas-romary-v1.md` (sha256 `cbdf399986714182…`), qui reste tel quel. La v1 demandait un simple appui (lettre ou référence) et excluait le rôle de responsable ; la v2 lui demande de **suivre et d'encadrer le projet**, et d'être **nommé responsable du projet** (« PI ») dans la demande « AI for Science », en disant à quoi cela l'engage.
- Décision du directeur, transmise par la session mère : « on pourrait se mettre d'accord pour qu'il suive mon projet, il est déjà au courant de ce que je fais ». Consigné au GO-2026-11-22-66 (mot reçu vers 13:21Z) : la première moitié de cette phrase ; le courriel à réécrire pour lui demander d'être le responsable encadrant ; le dépôt d'abord au programme des chercheurs externes ; « alongside my PhD » (option a).
- Ce que l'on sait de lui vient du seul mot de Lazar (Mines Paris, ancien tuteur aux Mines, au courant du projet) : son titre, ses années de tutorat et son adresse restent entre crochets.
- Base : `demande-ai-for-science-anthropic-v3.md` (sha256 `a40defd542ff372c…`) pour le champ du responsable et le champ libre. Textes relevés, sur les copies empreintées de `docs/sources/credits-recherche-v1/` :
  - formulaire (`formulaire-ia-pour-la-science-champs-v1.txt`, `7de3104da671c236…`) : « Note: All projects must have PI approval. If you are not the PI, please provide your PI's email address in the following question. » ; puis, au champ du responsable : « If you are the PI, please enter your email address. Note: For all selected projects, an email will be sent to your PI to acknowledge and approve the project. » ; et « This program provides free credits for our standard model suite. » ;
  - règlement (« Last updated Oct 20, 2026 », `www.anthropic.com_ai-for-science-program-rules-v1.txt`, `00f777bfac0e55cb…`), « Selected Researcher Notification » : « The potential Selected Researcher (and, if the potential Selected Researcher is a team or entity, each natural person associated with the potential Selected Researcher) may be required to sign an affidavit certifying compliance with these Rules along with a liability release, each of which, if requested, must be completed, signed, and returned to Anthropic within fourteen calendar (14) days from the date of Anthropic’s request » ; « Prize and Related Terms » : « Credits will be placed in the account for the organization identified in your application. »
- Décomptes par programme (`len(texte.split())`, comme `wc -w`), sur le texte exact de chaque bloc, formule d'appel et signature comprises.

## 1. Courriel en français (244 mots ; 250 avec l'objet)

**Objet** : `Accepteriez-vous de suivre mon projet ?`

Formule d'appel : vouvoiement par défaut ; « Thomas » si c'est ton usage avec lui (le courriel reste au « vous » ; tout passer au « tu » si tu le tutoies).
```text
Bonjour [Monsieur Romary / Thomas],

J'espère que vous allez bien. Comme vous le savez, je mène depuis octobre, à côté de ma thèse à NeuroSpin et non dans son cadre, un projet de recherche sur la surveillance d'agents d'IA par la lecture de leurs activations internes.

Accepteriez-vous de suivre et d'encadrer ce projet ? Nous en fixerions ensemble la forme, par exemple un point régulier.

Je voudrais aussi demander des crédits au programme « AI for Science » d'Anthropic, qui exige l'accord d'un responsable de projet (« PI »). Accepteriez-vous d'y être nommé responsable du projet ? Concrètement, pour vous :
- si le projet est retenu, Anthropic vous écrira pour que vous en preniez acte et l'approuviez ;
- le lauréat, et pour une équipe chaque personne associée (vous, peut-être), peut avoir à signer sous 14 jours une déclaration sur l'honneur de conformité au règlement et une décharge de responsabilité ;
- aucun engagement financier : les crédits sont gratuits et versés sur mon compte.

Je ne vous demande aucun accord au nom des Mines, et je vous enverrai la demande avant de la déposer. Vous pouvez aussi suivre le projet sans être nommé responsable.

Je joins un texte d'appui en anglais, à modifier librement si vous souhaitez le signer. Pourriez-vous me répondre par écrit, même en deux lignes ? Je ne citerai votre nom qu'après votre accord. Et si ce n'est pas possible, je le comprendrai très bien.

Bien cordialement,
Lazar Ciric
```
Pièce à joindre : le texte d'appui ci-dessous ; le CV v18 (`cv-v18/Lazar_Ciric_CV_2026-11-22_v18_universel.pdf`) si tu veux. À lui envoyer avant le dépôt, comme le courriel le promet : les champs anglais de `demande-ai-for-science-anthropic-v3.md`, avec la phrase du point 2 de la section 3 en place.

## 2. Texte d'appui en anglais, qu'il pourrait signer (148 mots)

À modifier ou à réécrire librement par lui ; les crochets sont à remplir par lui. Thomas Romary y dit suivre et encadrer le projet ; la phrase sur le rôle de responsable reste entre crochets, à garder seulement s'il accepte ce rôle. Le texte ne lui fait dire que ce qu'il peut attester, et rien au nom d'un établissement.
```text
Letter of support for Lazar Ciric

I am [POSITION] at Mines Paris-PSL. I was Lazar Ciric's tutor there [YEARS]; I now follow and supervise his AI-safety project.

Lazar is a PhD student at NeuroSpin (CEA, Université Paris-Saclay). He conducts this project alongside his PhD, not as part of it. He tests whether probes on an AI agent's internal activations catch sabotage spread thinly over a long task better than text-only monitors. He plants the sabotage, so the ground truth is known, and preregisters each decisive experiment.

[IN YOUR OWN WORDS: what you know of his work, and why you support him.]

I support his application for research credits. [IF YOU ACCEPT: I have also agreed to act as principal investigator of this project for Anthropic's AI for Science program.] This letter does not give consent on behalf of Mines Paris-PSL or any other institution.

[NAME], [EMAIL]
[DATE], [SIGNATURE]
```

## 3. Ce qui change dans les demandes s'il dit oui

Seulement dans « AI for Science », et seulement après son oui écrit au rôle de responsable.

1. **Champ « What is your PI's academic or organization email address? »** (facultatif ; absent du lien prérempli de `formulaire-anthropic-prerempli-v3.md`, à taper à la main dans le formulaire ouvert) :
```text
[COURRIEL DE THOMAS ROMARY, ADRESSE DES MINES]
```
Entre crochets tant qu'il n'a pas dit oui par écrit. Le champ ne prend qu'une adresse, celle à laquelle Anthropic écrira pour faire approuver le projet : y mettre son adresse des Mines telle qu'il la donne, sans son nom ; son nom est dans la phrase du champ libre (point 2).

2. **Champ libre de la fin** (« Is there anything else you would like the review committee to know about your application? ») : la phrase à crochet « On PI approval: [PHRASE SELON L'OPTION RETENUE…]. » devient (27 mots) :
```text
On PI approval: Thomas Romary (Mines Paris-PSL), my former tutor at Mines Paris, follows and supervises this project and has agreed in writing to be its PI.
```
Le champ entier, cette phrase en place (147 mots ; pas de limite écrite) :
```text
I am a PhD student at NeuroSpin. My thesis, within the ERC-funded MathBrain project, is on brain networks involved in mathematics; this AI-safety project runs alongside it and is not my thesis topic. On PI approval: Thomas Romary (Mines Paris-PSL), my former tutor at Mines Paris, follows and supervises this project and has agreed in writing to be its PI. I have also applied to Anthropic's External Researcher Access Program for API credits for the same research; if both are granted, they would fund different parts of the work and I would say so in any report. I do not ask for any exemption from the Usage Policy. Some prompts describe sabotage strategies for test agents built on open-weight models. This is defensive research on monitoring: these prompts are logged, and the experiments that use them are preregistered. Drafted with help from Claude and edited by me.
```
Les phrases A et B de la question 3 du jet 4 et les phrases de référence de la v1 n'y entrent pas.

3. **L'accord de l'établissement reste une déclaration distincte.** En cochant « I agree » sous le formulaire, Lazar accepte le règlement, qui lui fait déclarer (« Eligibility Criteria ») : « If you are employed by a legal entity or affiliated with a university or other research institution, then you represent and warrant that you have obtained all consents from that employer or institution necessary to participate in the Program. » Le oui de Thomas Romary comme responsable ne la remplace pas : les Mines ne sont aujourd'hui ni l'employeur ni l'établissement de Lazar, et il ne donne aucun accord en leur nom. Ne cocher « I agree » que si cette déclaration est vraie.

**Rien d'autre ne change.** Le dépôt se fait d'abord au programme des chercheurs externes (décision du directeur, GO-2026-11-22-66) : son formulaire n'a pas de champ de responsable, et ses champs restent ceux du jet 4 (`champs-formulaire-anthropic-jet-4-v1.md`), phrases facultatives de son champ 11 comprises, sous la même condition d'accord écrit. Restent aussi tels quels : les autres champs d'« AI for Science », dont « Research team » (il liste les personnes qui emploieront Claude) ; Amazon (« Research Led By » : `Myself`) ; Google. Le tableau de la section 4 de la v1 (« Où son nom peut figurer… ») vaut toujours, sauf la ligne du champ du responsable d'« AI for Science » et, dans la phrase qui le précède, « ni l'approbation d'un responsable de projet ».

## 4. Réserves

- S'il accepte de suivre le projet sans être nommé responsable, rien ne change dans les demandes : le champ du responsable reste vide, et la question 3 du jet 4 (courriel de question à Anthropic, phrases A et B) reste la voie pour « AI for Science ». S'il dit oui aux deux, ce courriel et ces phrases n'ont plus d'objet.
- S'il accepte de suivre sans encadrer, écrire « follows » seul, sans « and supervises » (phrase du champ libre) ni « and supervise » (texte d'appui).
- Déclaration sur l'honneur : le règlement ne dit pas si le responsable compte parmi les personnes associées au lauréat ; d'où « (vous, peut-être) » dans le courriel. Le courriel nomme aussi la décharge de responsabilité, que le règlement joint à la déclaration.
- « Aucun engagement financier » : lecture du formulaire (crédits gratuits) et du règlement (crédits versés sur le compte de l'organisation donnée dans la demande, celle de Lazar) ; la section « Taxes » vise les lauréats, donc Lazar. Rien dans ces textes ne demande d'argent au responsable.
- Amazon : la raison écrite pour `Myself` dans `demandes-credits-nuage-v4.md` (« ni tes directeurs ni Thomas Romary ne dirigent ce projet ») ne tiendra plus telle quelle s'il dit oui ; le choix `Myself` reste vrai (tu mènes le travail) et ne change pas.
- Un responsable d'un autre établissement que celui du demandeur : le formulaire ne l'exclut pas (il demande seulement l'adresse du responsable) ; la phrase du champ libre dit qui il est.
- « Un point régulier » n'est qu'un exemple de forme, à convenir entre vous.
- Le courriel ne nomme pas les directeurs de thèse et ne dit rien de leur avis (comme la v1).

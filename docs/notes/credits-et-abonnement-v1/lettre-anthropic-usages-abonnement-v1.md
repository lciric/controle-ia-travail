# Lettre à Anthropic sur les usages permis de l'abonnement Ultra (version 1)

- Date : 2026-11-22T07:57:24Z (`date -u`) ; pages relevées entre 07:48Z et 07:56Z.
- Origine : la lettre de la section C.5 de la réponse 15 de Fable (`docs/notes/demandes-fable-api-2026-11-22-v1/reponse-15/relecture-fable-api.md`), fusionnée avec la question sur les données de la réponse d'Opus 4.6 (`…/reponse-15-opus46/relecture-fable-api.md`, section C.5, question 2), mise au point pour un abonné Ultra.
- Mot de Lazar : GO-2026-11-22-32 (« go 1 3 4 6 » ; geler : « je refuse catégoriquement, non » ; crédits inclus : « déjà fait »). **La lettre ne promet aucun gel** et ne décrit pas l'usage comme suspendu ; elle dit seulement que le directeur suivra la réponse écrite.
- Rien n'a été envoyé : le directeur envoie.

## Pages consultées

| page | adresse | ce qu'on y a lu |
|---|---|---|
| Obtenir de l'aide | https://support.claude.com/en/articles/9015913-how-to-get-support | canal écrit par la messagerie d'aide ; les abonnés Pro, Max et Ultra ont accès à « Further assistance from our Product Support team » ; réponse aussi par courriel ; « Keep one conversation per issue » |
| Contact commercial | https://claude.com/contact-sales (adresse de la page de conformité : https://www.anthropic.com/contact-sales, redirigée) | « Our sales team can only support complex deals, like 500+ seat deployments and BAAs. » ; un bouton « Start a chat » (agent de conseil) |
| Conformité de Claude Code (déjà au dépôt) | https://code.claude.com/docs/en/legal-and-compliance (`docs/sources/conditions-abonnement-claude-v1/`) | « For questions about permitted authentication methods for your use case, please contact sales. » |
| Crédits mensuels inclus (déjà au dépôt) | https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans | Ultra : 200 USD par mois ; une seule organisation de la console liée ; couvre l'interface, les lots, le kit d'agents et `claude -p` lancés avec une clé de l'organisation liée |
| Tarifs | https://claude.com/pricing | Ultra : « No 5-hour limit‡ » (« for verified accounts ») ; Max : « Fable included, up to half your weekly limit » ; Ultra : « Everything in Max, plus » |

**Vérifié en ligne** : les deux canaux et ce que la page commerciale dit de son périmètre ; les faits de l'abonnement Ultra cités dans la lettre. **Non vérifié** : qu'une question de conditions d'usage posée par la messagerie soit transmise à l'équipe qui peut y répondre par écrit ; le délai de réponse ; que la limite hebdomadaire de Fable s'applique à Ultra dans les mêmes termes que pour Max (la page tarifs l'écrit pour Max, Ultra reprend « Everything in Max »).

## À qui l'envoyer et comment

1. **Canal premier : la messagerie d'aide de claude.ai**, écrite, avec réponse par courriel et un fil unique. Pas à pas (page « How to get support ») : se connecter à claude.ai avec le compte Ultra → cliquer son nom ou ses initiales en bas à gauche → « Get help » → « Send us a message » → « Accept » → choisir le sujet le plus proche (compte, abonnement ou facturation) → coller la lettre en anglais ci-dessous et demander « Please forward this to the team responsible for usage policy and authentication, and reply in writing. »
2. **Canal second, si la messagerie renvoie vers le commercial** (ce que fait la page de conformité) : https://claude.com/contact-sales → « Get started » sous « For complex needs ». La page prévient que l'équipe commerciale ne traite que les gros contrats : s'attendre à un renvoi.
3. Garder la réponse : copie écrite versée dans `docs/sources/` avec empreinte, et citée dans le rapport du programme (la lettre l'annonce).
4. Un seul fil : si pas de réponse, répondre dans le même fil (la page le demande), ne pas en ouvrir un second.

## Texte à envoyer (anglais)

> **Subject: Permitted uses of an individual Ultra subscription for a research program — request for a written answer**
>
> Hello,
>
> I am an individual subscriber on the Ultra plan (number of subscriptions in my name: [NOMBRE]). I run an AI safety research program on white-box monitoring of AI agents. I develop with Claude Code under my subscription, signed in through your own sign-in flow with the unmodified client. Part of the work runs in Claude Code sessions, including cloud sessions on claude.ai that start sub-agents and other sessions; part of my experiment loops goes through the Claude API with keys from the Console organization linked to my Ultra plan. I want to follow your terms to the letter, and I will follow your written answer. Your texts, read on 22 November 2026, leave the following points open.
>
> 1. Your Consumer Terms exclude access "through automated or non-human means", except via an API key or "where we otherwise explicitly permit it". Are Claude Code's non-interactive mode (`-p`) and the Agent SDK, started by my own scripts with my subscription sign-in and for my sole use, explicitly permitted? Does "ordinary, individual usage of Claude Code and the Agent SDK" cover them, given that the Agent SDK page places the SDK under your Commercial Terms?
> 2. Is a session that I open and that itself starts other sessions or sub-agents, in cloud containers, working for several hours without action from me, ordinary use? Does the answer depend on how each container signs in?
> 3. Can experiment loops (hundreds to thousands of calls per week, whose outputs are recorded as research measurements) run under the subscription, or do they require an API key?
> 4. May I hold several individual subscriptions in my name and split my own work between them?
> 5. Monthly API credits included with Ultra: can free research credits (if awarded) be added to the same linked Console organization, and in which order are the two spent?
> 6. Does the clause "to develop or train any artificial intelligence or machine learning algorithms or models" cover training small, non-competing research models (linear probes on open-weight models) whose code is written with Claude Code?
> 7. When the weekly limit specific to Fable is reached, does the client stop or switch to another model? Is the model actually served recorded in Claude Code session logs?
> 8. I have turned off "Help Improve our AI models" on my accounts. Does this cover Claude Code sessions, including cloud sessions on claude.ai? My research concerns sabotage detection, so some content may be flagged by safety classifiers: in that case, how is it used and for how long is it kept?
> 9. My application to the External Researcher Access Program, submitted on [DATE DE LA CANDIDATURE PRÉCÉDENTE], received no reply. Is there anyone else I should contact?
>
> I will cite your answer in the program's report. Thank you.
>
> [NOM]
> [AFFILIATION]
> Account email: [COURRIEL DU COMPTE ULTRA]

## Traduction française (pour le directeur, non à envoyer)

> **Objet : usages permis d'un abonnement individuel Ultra pour un programme de recherche — demande de réponse écrite**
>
> Bonjour,
>
> Je suis abonné individuel à la formule Ultra (nombre d'abonnements à mon nom : [NOMBRE]). Je mène un programme de recherche sur la sûreté de l'intelligence artificielle, la surveillance boîte blanche des agents. Je développe avec Claude Code sous mon abonnement, connecté par votre propre parcours de connexion avec le client non modifié. Une part du travail tourne dans des sessions de Claude Code, dont des sessions en nuage sur claude.ai qui lancent des sous-agents et d'autres sessions ; une part de mes boucles d'expérience passe par l'interface de programmation de Claude, avec des clés de l'organisation de la console liée à mon abonnement Ultra. Je veux respecter vos conditions à la lettre, et je suivrai votre réponse écrite. Vos textes, lus le 22 novembre 2026, laissent ouverts les points suivants.
>
> 1. Vos conditions grand public excluent l'accès « par des moyens automatisés ou non humains », sauf par clé ou « là où nous le permettons explicitement ». Le mode non interactif de Claude Code (`-p`) et le kit d'agents, lancés par mes scripts avec ma connexion d'abonné et pour mon seul usage, sont-ils explicitement permis ? La phrase « usage ordinaire et individuel de Claude Code et du kit d'agents » les couvre-t-elle, alors que la page du kit le place sous vos conditions commerciales ?
> 2. Une session que j'ouvre et qui lance elle-même d'autres sessions ou des sous-agents, dans des conteneurs en nuage, travaillant plusieurs heures sans geste de ma part, est-elle un usage ordinaire ? La réponse dépend-elle de la façon dont chaque conteneur se connecte ?
> 3. Des boucles d'expérience (des centaines à des milliers d'appels par semaine, sorties enregistrées comme mesures) peuvent-elles tourner sous l'abonnement, ou exigent-elles une clé ?
> 4. Puis-je détenir plusieurs abonnements individuels à mon nom et répartir mon propre travail entre eux ?
> 5. Crédits mensuels d'interface inclus dans Ultra : des crédits de recherche gratuits, s'ils sont accordés, peuvent-ils s'ajouter dans la même organisation liée de la console, et dans quel ordre les deux se dépensent-ils ?
> 6. La clause « développer ou entraîner tout algorithme ou modèle d'intelligence artificielle ou d'apprentissage automatique » vise-t-elle l'entraînement de petits modèles de recherche non concurrents (sondes linéaires sur des modèles ouverts) dont le code est écrit avec Claude Code ?
> 7. À la limite hebdomadaire propre à Fable, le client s'arrête-t-il ou passe-t-il à un autre modèle ? Le modèle réellement servi figure-t-il dans les journaux de session de Claude Code ?
> 8. J'ai désactivé « Help Improve our AI models » sur mes comptes. Ce réglage couvre-t-il les sessions de Claude Code, y compris les sessions en nuage sur claude.ai ? Ma recherche porte sur la détection du sabotage, si bien que des contenus peuvent être signalés par les classifieurs de sûreté : dans ce cas, comment sont-ils utilisés et combien de temps sont-ils gardés ?
> 9. Ma candidature au programme d'accès des chercheurs externes, déposée le [DATE], est restée sans réponse. Dois-je m'adresser à quelqu'un d'autre ?
>
> Je citerai votre réponse dans le rapport du programme. Merci.

## Ce qui a changé par rapport à la lettre de Fable

- Formule remplie : Ultra ; nombre d'abonnements laissé au directeur ([NOMBRE]).
- Retiré : « mes mesures passent par l'interface de programmation, par clé, et y resteront » : depuis GO-2026-11-22-32, la part Claude de la mesure peut passer sous l'abonnement ; la lettre décrit l'usage tel qu'il est, sans promesse.
- Question 5 resserrée : montant, échéance et usages des crédits inclus sont désormais lus sur la page d'aide (200 USD par mois pour Ultra, une organisation liée, interface, lots, kit d'agents et `claude -p` avec clé) ; reste la cohabitation avec des crédits de recherche, que la page ne traite pas.
- Question 8 ajoutée (d'après Opus 4.6) : portée du refus d'entraînement sur les sessions de Claude Code et sort des contenus signalés ; la page d'aide sur les réglages de confidentialité vise « Claude Free, Pro, Max and when accounts from those plans use Claude Code » sans nommer Ultra (voir `instructions-refus-entrainement-et-secrets-v1.md`).
- Question 8 de Fable devenue 9 ; la demande de crédits elle-même est traitée à part (`demande-credits-recherche-anthropic-v1.md`).
- « Je suivrai votre réponse écrite » : engagement de suivre la réponse quand elle viendra, pas de suspendre quoi que ce soit en l'attendant.

## Réserves

- Envoyer la lettre signale à Anthropic l'usage décrit (sessions filles en nuage, boucles d'expérience) : c'est l'effet voulu de la demande écrite, mais le directeur doit l'accepter en connaissance de cause (la page de conformité : « may do so without prior notice »).
- La question 4 suppose que le directeur détient plusieurs abonnements ; s'il n'en a qu'un, la retirer.
- La question 8 suppose le refus d'entraînement déjà fait sur chaque compte : le faire avant l'envoi (pas à pas dans `instructions-refus-entrainement-et-secrets-v1.md`).

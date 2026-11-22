# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHa1kLSAJk8LUFpfoMVv`
- Heure (UTC) : 2026-11-22T07:37:16Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-15-abonnement-claude-organisme-v1.md` — sha256 1b48027d43554a4af901a7c64a7239ba471a8b6548e6cec86efa358d0509fde7 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-14/relecture-fable-api.md` — sha256 636422bfbc530c2f79a50b340cf256c3ed2b43ccb4e519ba83abb73030bb3b8a (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/sources/conditions-abonnement-claude-v1/code.claude.com_docs_en_agent-sdk_overview-v1.txt` — sha256 5bd1d4a4b0dd8c2df731bc22ea993e349a6508b8397c76978f73c1d548a8b906 (compagnon : vérifié)
  - remarques : `docs/sources/conditions-abonnement-claude-v1/code.claude.com_docs_en_legal-and-compliance-v1.txt` — sha256 77e365c911ddc6a9a8b4b91cca060d229bf918ef33fa2a190a018730afcac3cc (compagnon : vérifié)
  - remarques : `docs/sources/conditions-abonnement-claude-v1/support.claude.com_en_articles_11145838-using-claude-code-with-your-pro-or-max-plan-v1.txt` — sha256 973bda224422642d288a912bef11f1609605b5435b14429284756a54bd9e4c5f (compagnon : vérifié)
  - remarques : `docs/sources/conditions-abonnement-claude-v1/www.anthropic.com_legal_aup-v1.txt` — sha256 6c0a052bd661edfe41849b668c2449d8d3054b58f1aed723843b6eb57a8cd675 (compagnon : vérifié)
  - remarques : `docs/sources/conditions-abonnement-claude-v1/www.anthropic.com_legal_commercial-terms-v1.txt` — sha256 bb32e6330dc0b81abfe8d344a0d09e5a469e78f51734fda7cf4939378902dd9b (compagnon : vérifié)
  - remarques : `docs/sources/conditions-abonnement-claude-v1/www.anthropic.com_legal_consumer-terms-v1.txt` — sha256 929f31d22899d8bf82f0ecb3fc1358d21fdb0f9fbc530aff28b1fe932a93a05f (compagnon : vérifié)
- Empreinte de l'invite envoyée : 96e431d8029e730db366470e60566556168715dc9391e69ea43f56c78a1be333
- Jetons : entrée 51164, sortie 70555 (dont réflexion 61110), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 3.231512 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 15 — ce que l'abonnement peut payer dans l'organisme : demande approfondie et réponse

**Conventions.** [FAIT RAPPORTÉ] renvoie à une phrase des pièces, citée en anglais sans retouche pour qu'une recherche exacte la retrouve. [HYPOTHÈSE] est à tester. [PROPOSITION] est un choix ou une lecture. « Question ouverte » marque ce que les pièces ne disent pas. Dans les citations, « API key » est la clé de l'interface de programmation payante, « Agent SDK » le kit d'agents, « OAuth » la connexion par le compte d'abonnement, « CLI » le client en ligne de commande. Je n'ai vu ni les comptes, ni les commandes qui lancent les sessions, ni la page sur les crédits inclus.

## Réponse courte

Oui, l'abonnement peut payer trois choses.

1. [PROPOSITION] Tout ce que l'abonné conduit lui-même dans Claude Code et les applications : conception, code, écriture de l'oracle, lecture des résultats, relectures de travail, rédaction. Le juge et le test de mort peuvent devenir des programmes : l'abonnement paie alors leur écriture, et leur exécution ne coûte plus aucun appel. C'est par là qu'il « paie » les plus gros postes du devis.
2. [FAIT RAPPORTÉ] Les formules Max et Ultra incluent des crédits mensuels d'interface payante (C12), ce que ma réponse 14 ignorait. Leur montant est une question ouverte. C'est la seule voie où l'abonnement paie des appels de mesure sans rien ôter à leur validité.
3. [HYPOTHÈSE] Les relectures servies aujourd'hui par clé, environ un dollar pièce, peuvent passer en session.

Le reste ne bouge pas. Les boucles automatisées sur identifiants d'abonnement (proposeurs, juges et tests de mort par modèle, objets de contrôle) ne sont pas tranchées par le texte, la clause par défaut leur est contraire (C1), et elles seraient malsaines pour une mesure même permises.

**Ce que la lecture change à la réponse 14.** [FAIT RAPPORTÉ]
- Confirmé : le compte est réservé à l'abonné (C2) ; l'accès automatisé est exclu sauf permission explicite (C1).
- Infirmé : le kit d'agents n'est pas « exclu » pour l'usage individuel. Le texte interdit aux développeurs tiers d'y faire passer leurs utilisateurs (C9) et suppose même un usage individuel ordinaire du kit sous abonnement (C6).
- Retiré : le « repli de modèle à l'approche du quota » ne figure dans aucune pièce.

## A. Méthode « demande approfondie »

### A.1 Ce qu'un expert ferait et qui n'est pas demandé

[PROPOSITION]
- **Auditer l'existant avant l'extension.** La session mère qui crée des sessions filles relève des mêmes phrases que la question posée.
- **Vérifier le canal réel de chaque session.** [FAIT RAPPORTÉ] Quand la variable d'environnement de la clé est présente, le client facture l'interface payante au lieu de l'abonnement (C13). [HYPOTHÈSE] Si les conteneurs des sessions portent aussi les clés des mesures, une session peut payer au tarif plein sans qu'on le sache.
- **Séparer deux axes** : permis par le texte, et sain pour la mesure. L'un ne dit rien de l'autre.
- **Peser les verbes.** « may not » et « does not permit » obligent ; « should », « designed » et « assume » orientent. Une campagne ne se fonde pas sur les seconds.
- **Chercher dans l'abonnement autre chose que des quotas de session**, d'où C12.
- **Lire le régime des données.** [FAIT RAPPORTÉ] Sous conditions grand public, les contenus peuvent servir à l'entraînement sauf refus (C3) ; sous conditions commerciales, non (C19). Cela touche dès aujourd'hui les lois plantées, l'oracle et le mode de sabotage tenu à l'écart (N-054), que lisent les sessions de développement.
- **Peser l'asymétrie.** [FAIT RAPPORTÉ] Le fournisseur peut agir « without prior notice » (page conformité). Quelques centaines de dollars d'économie se comparent à l'outil de travail de tout le programme.

### A.2 Données brutes de départ

[PROPOSITION]
- Les six pièces et leurs empreintes, plus celles qui manquent :
  - la description de l'abonnement à la commande ([FAIT RAPPORTÉ] son contenu « will be described in the order process », conditions grand public) ;
  - la page des crédits mensuels inclus et les conditions supplémentaires des crédits ;
  - la page des limites ;
  - la documentation du mode non interactif et des sessions en nuage ;
  - l'historique des versions.
- L'état réel :
  - comptes et formules ;
  - commande exacte qui crée chaque session fille ;
  - connexion par le parcours officiel ou jeton recopié ;
  - variables d'environnement de chaque conteneur ;
  - réglage d'entraînement de chaque compte ;
  - relevés de jetons des sessions et factures.

### A.3 Méthodes et outils

[PROPOSITION]
- Une matrice « usage × phrase », chaque citation contrôlée par recherche exacte dans la pièce à empreinte.
- Une lecture selon l'interprétation raisonnable la plus stricte, en trois classes, sans quatrième classe « sans doute permis ».
- Un script d'audit du canal dans chaque conteneur ; un compteur de jetons des sessions, valorisé au prix public.
- Une double lecture à l'aveugle par le second modèle, comparée case par case.

### A.4 Ce qui vérifie le résultat, hors du directeur et de Claude

[PROPOSITION]
1. La réponse écrite du fournisseur. La page conformité y invite : « please contact sales ».
2. La recherche exacte de chaque citation par un tiers, et une archive datée des pages.
3. L'accord avec le second modèle ; chaque désaccord devient une question de la lettre.
4. Un juriste pour C1, C4 et C18.
5. Le relevé de la console montrant la consommation des crédits inclus.

## B. Demande reformulée

[PROPOSITION] « À partir du texte à empreinte des six pièces et de l'état réel des sessions, établir pour chaque élément de l'organisme et pour chaque voie (session conduite par l'abonné ; boucle automatisée sur identifiants d'abonnement ; crédits d'interface inclus dans l'abonnement) la phrase qui permet, celle qui interdit, ou la question à poser. Dire à part ce que chaque voie coûte à la validité de la mesure et ce qu'elle épargne par rapport au devis réduit. Produire la lettre qui tranche le reste. Chaque citation doit se vérifier par recherche exacte ; seule la réponse écrite du fournisseur fait foi. »

## C. Réponse

### C.0 Les phrases d'appui

[FAIT RAPPORTÉ]

**Conditions grand public**
- C1, dans la liste des usages exclus : « Except when you are accessing our Services via an Anthropic API Key or where we otherwise explicitly permit it, to access the Services through automated or non-human means, whether through a bot, script, or otherwise. »
- C2 : « You also may not make your Account available to anyone else. »
- C3 : « including training our models, unless you opt out of training through your account settings » ; exception : « your Materials are flagged for safety review ».
- C4, usage exclu : « including to develop or train any artificial intelligence or machine learning algorithms or models ».

**Page conformité**
- C5 : « Consumer Terms of Service - for Free, Pro, Max, and Ultra users ».
- C6 : « Advertised usage limits for Pro, Max, and Ultra plans assume ordinary, individual usage of Claude Code and the Agent SDK. »
- C7 : la connexion par compte « is designed to support ordinary use of Claude Code and other native Anthropic applications ».
- C8 : « Developers building products or services that interact with Claude’s capabilities, including those using the Agent SDK, should use API key authentication ».
- C9, interdit aux développeurs tiers : « to route requests through Free, Pro, Max, or Ultra plan credentials on behalf of their users » ; « developers may not collect, store, or intermediate Claude.ai credentials or session tokens ».
- C10 : « Nor does it prevent an end user from signing in to the unmodified Claude Code binary with their own Claude subscription ».

**Page d'aide**
- C11 : « Use Claude for writing, research, analysis, and more—at work and at home. » ; « Use Claude Code for your terminal-based coding workflows. »
- C12 : « Monthly API credits included with the Max plan can’t be used in Claude Code or the Claude apps, including for usage credits. » (même phrase pour Ultra).
- C13 : « Claude Code will use this API key for authentication instead of your Claude subscription ».
- C14 : « Pro and Max plans have a five-hour session limit and a weekly limit. » ; « a separate weekly limit for Fable » ; « all activity in both tools counts against the same limits ».

**Présentation du kit d'agents**
- C15 : « Use of the Claude Agent SDK is governed by Anthropic’s Commercial Terms of Service » ; « run the CLI as a subprocess with the -p flag ».
- C16 : « Load automatically from your project’s .claude/ and from ~/.claude/, same as Claude Code ».

**Politique d'usage**
- C17 : « services that route requests through consumer subscriptions or misrepresent the product or client being used ».
- C18 : « create multiple accounts, to avoid detection, circumvent product guardrails » ; « otherwise evade payment for our services ».

**Conditions commerciales**
- C19 : « Anthropic may not train models on Customer Content from Services. »

### C.1 Classement, élément par élément

Les classes sont mes lectures [PROPOSITION] des phrases citées.
- « Session » : l'abonné conduit le client non modifié (C10).
- « Boucle » : appels lancés par script ou sans geste humain, sur identifiants d'abonnement.

| Élément | En session | En boucle | Pour une mesure qui compte |
|---|---|---|---|
| Conception et code (noyau, scripts, programmes de juge et de test de mort) | Permis : C5, C7, C11. Réserve C4 pour le code qui entraîne des sondes (question 6) | Sans objet | Sain |
| Orchestration | Écrire l'orchestrateur : permis (C7, C11). Sous-agents d'une session suivie : permis par lecture raisonnable (page d'aide : « delegate complex coding tasks while maintaining transparency and control » ; kit : « Spawn specialized agents for focused subtasks »). Sessions filles autonomes en conteneurs : non tranché, C1 vise le « non-human » (questions 1 et 2) | Non tranché ; C1 par défaut | Sain pour développer. La course de mesure est tenue par le noyau, programme rejouable, jamais par une session |
| Proposeurs | Sans objet : milliers d'appels | Non tranché. C1 exclut sauf permission explicite ; C8 oriente vers la clé ; C15 place le kit sous conditions commerciales ; C6 suppose pourtant un usage individuel ordinaire du kit (questions 1 et 3) | Malsain : c'est le traitement mesuré. Avec l'espèce Kimi, hors abonnement de toute façon |
| Juges | Par programme : écriture permise, exécution sans appel | Par modèle : comme les proposeurs | Si N-053 (juge d'une autre lignée) s'applique ici, des proposeurs Claude excluent un juge Claude |
| Tests de mort | Par programme, si la décision 1 de la réponse 14 est prise : écriture permise, exécution sans appel | Par modèle : comme les proposeurs | Par modèle : par clé |
| Objets de contrôle | Fabrication : permise | Passage dans la chaîne : comme le test de mort | Même canal que les vraies cartes, sinon ils sont muets |
| Oracle du monde planté | C'est un programme : écriture permise (C7, C11), exécution sans appel | Sans objet | Seconde écriture dans une session propre, sans accès à la première (C16) |
| Lecture des résultats | Permis (C11, « analysis ») | Sans objet | Sain si les chiffres sortent d'un script et que la session commente |
| Relectures et contre-lectures | Permis (C11) | Outil de relecture rebranché sur l'abonnement : non tranché (C1) | Travail courant : sain. Contre-lecture indépendante : répertoire propre (C16), sinon par clé |
| Rédaction | Permis (C11, « writing »). La politique d'usage exclut de « submit AI-assisted work without proper permission or attribution » | Sans objet | Sain |
| Appels de mesure payés par les crédits inclus | — | Montant et conditions : question ouverte (C12, question 5) | Sain : c'est l'interface payante |

[FAIT RAPPORTÉ] Aucune des six pièces ne dit en toutes lettres « permis » ou « interdit » pour une boucle personnelle sous abonnement. C1 pose l'exclusion par défaut et renvoie à une permission explicite que je n'ai pas trouvée.

### C.2 Ce que l'on perd en validité de mesure

[FAIT RAPPORTÉ], sauf mention.
- **Modèle servi.** L'appel par clé consigne le modèle servi et l'identifiant du message (en-tête de la relecture 14) ; [HYPOTHÈSE] une session ne les consigne pas ainsi. Fable a sa limite hebdomadaire propre (C14). Ce que fait le client à cette limite est une question ouverte (question 7).
- **Réglages.** Le client est un agent outillé (« A library that runs the Claude Code binary », kit d'agents), non le modèle nu. [HYPOTHÈSE] Consigne système, outils, effort et plafond de sortie échappent.
- **Appariement des bras.** Les limites de cinq heures et hebdomadaires sont partagées avec tout le travail de l'abonné (C14). [HYPOTHÈSE] Les trois bras ne tiennent pas dans la même fenêtre et un monde peut être coupé.
- **Reproductibilité.** « we do not guarantee that any particular piece of content, feature, or other service will always be available through the Services » (conditions grand public). Les limites supposent un usage « ordinary » (C6), sans valeur en jetons.
- **Étanchéité.** La mémoire et la configuration du projet sont chargées d'office (C16) ; les contenus sont exposés à l'entraînement (C3).
- **Quotas et facture.** Au-delà des limites, le client propose de continuer au tarif de l'interface : « Usage will be billed at standard API rates » (page d'aide). Il n'y a pas de facture par appel, donc l'égalisation des coûts (N-045) perd son appui.

[PROPOSITION] Un passage par l'abonnement est sain à trois conditions :
- l'élément ne produit aucun chiffre revendiqué, ou sa sortie est revérifiée par un programme ;
- il n'entre pas dans un seul bras ;
- il est étiqueté et déclaré.

Conception, code, écriture de l'oracle, lecture, relectures de travail et rédaction les remplissent. Proposeurs, juges et tests de mort par modèle, objets de contrôle, non.

### C.3 Économie, en ordre de grandeur

[FAIT RAPPORTÉ, réponse 14] Référence : devis d'origine 2 366 à 8 380 dollars ; devis réduit 200 à 450 dollars (Kimi) ou 700 à 1 500 (Claude).

| Voie | Effet | Statut |
|---|---|---|
| Juge et test de mort écrits sous abonnement, exécutés sans appel | Efface l'essentiel du poste hors section D, environ 1 900 à 6 000 dollars du devis d'origine ; déjà compté dans le devis réduit | FAIT RAPPORTÉ (réponse 14) ; gain nouveau nul |
| Développement et orchestration | Déjà sous abonnement ; valeur au prix public inconnue, sans doute supérieure au devis réduit | HYPOTHÈSE, à mesurer sur les relevés de jetons |
| Relectures en session | 1,04 dollar mesuré une fois ; quelques dizaines de dollars par série | HYPOTHÈSE |
| Crédits mensuels inclus | Quelques dizaines de dollars par mois couvriraient le palier 0 et l'essai de fumée (5 à 25 dollars) | Question ouverte |
| Chaîne par modèle sous abonnement | Au plus la part Claude : 50 à 290 dollars dans la conception Kimi recommandée ; rien sur les appels Kimi | HYPOTHÈSE ; à ne pas faire |

[PROPOSITION] L'abonnement n'apporte pas d'ordre de grandeur de plus : le reste du devis réduit est surtout fait d'appels à un autre fournisseur.

### C.4 Ce qui serait un contournement

[PROPOSITION], d'après les phrases citées :
- Brancher l'organisme sur un jeton d'abonnement recopié, par une passerelle ou un client autre que celui d'Anthropic : interdit selon le texte (C17).
- Prêter le compte ou y faire travailler un collaborateur : interdit selon le texte (C2).
- Multiplier les comptes ou étaler la charge pour passer sous les limites : C18 vise les comptes créés pour « circumvent product guardrails ». Que les limites d'usage en soient est une question ouverte (question 4). À ne pas faire avant réponse.
- Déguiser une boucle en usage interactif (frappes simulées, lancements échelonnés) : C1 et C17.
- Rebrancher l'outil de relecture ou les objets de contrôle sur l'abonnement pour alléger la facture : C1, et « evade payment » (C18) si le fournisseur le lit ainsi.
- Modifier le client ou sa connexion : la politique d'usage exclut de « bypass or interfere with capabilities, restrictions, or guardrails established within our products ».

### C.5 Lettre au fournisseur

[PROPOSITION] À envoyer au contact commercial que désigne la page conformité, avec copie à l'assistance de l'abonnement.

> **Objet : usages permis d'un abonnement individuel pour un programme de recherche — demande de réponse écrite**
>
> Bonjour,
>
> Je suis abonné individuel (formule : […] ; nombre d'abonnements à mon nom : […]). Je mène un programme de recherche sur la sûreté de l'intelligence artificielle. Je développe avec Claude Code sous abonnement ; mes mesures passent par l'interface de programmation, par clé, et y resteront. Je veux respecter vos conditions à la lettre. Vos textes, lus le 22 novembre 2026, ne tranchent pas les points suivants.
>
> 1. Vos conditions grand public excluent l'accès « through automated or non-human means », sauf clé ou permission explicite. Le mode non interactif de Claude Code (« -p ») et le kit d'agents, lancés par mes scripts avec mes identifiants d'abonnement et pour mon seul usage, sont-ils explicitement permis ? La phrase « ordinary, individual usage of Claude Code and the Agent SDK » les couvre-t-elle, alors que la page du kit le place sous vos conditions commerciales ?
> 2. Une session que j'ouvre et qui crée elle-même d'autres sessions ou sous-agents, dans des conteneurs en nuage, travaillant plusieurs heures sans geste de ma part, est-elle un usage ordinaire ? La réponse dépend-elle de la connexion de chaque conteneur (votre parcours, ou jeton recopié) ?
> 3. Des boucles de génération et d'évaluation d'une expérience (des centaines à des milliers d'appels par semaine, sorties enregistrées comme mesures) peuvent-elles tourner sous abonnement, ou exigent-elles une clé ?
> 4. Puis-je détenir plusieurs abonnements individuels à mon nom et répartir mon travail entre eux ?
> 5. Crédits mensuels d'interface inclus dans les formules Max et Ultra : quel montant, quelle échéance, quels modèles, traitement par lots compris ? Servent-ils à des appels directs par clé depuis mes scripts ? Se cumulent-ils entre abonnements ?
> 6. La clause « to develop or train any artificial intelligence or machine learning algorithms or models » vise-t-elle l'entraînement de petits modèles de recherche non concurrents (sondes linéaires sur des modèles ouverts) dont le code est écrit avec Claude Code ?
> 7. À la limite hebdomadaire propre à Fable, le client s'arrête-t-il ou change-t-il de modèle ? Le modèle servi figure-t-il dans les journaux de session ?
> 8. Ma demande de crédits de recherche, déposée le […], est restée sans réponse : à qui l'adresser ?
>
> Je citerai votre réponse dans le rapport du programme. Merci.

### C.6 Antériorité

Tout est rapporté de mémoire, non vérifié sur document source, sans chiffre opposable. Les auteurs sont à relever sur les documents, la consigne excluant les noms.
- « Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs » (2024) : fuite de jeux d'essai par des interfaces grand public dont les contenus servent à l'entraînement.
- « How Is ChatGPT’s Behavior Changing over Time? » (2023) : dérive d'un modèle servi sous un même nom.
- « AI Agents That Matter » (2024) : évaluation d'agents à coût compté.

[HYPOTHÈSE] Ces travaux appuient C.2. Ils ne disent rien des conditions d'usage, qui relèvent du texte et du fournisseur.

## D. Décisions qui reviennent au directeur

**1. Envoyer la lettre et geler, d'ici la réponse, toute extension de l'usage automatisé de l'abonnement, répartition entre comptes comprise.**
- Enjeu : le respect des conditions et l'outil de travail du programme.
- Option A, envoyer et geler : tranche par écrit, sans coût ; délai inconnu.
- Option B, ne rien demander et s'en tenir à l'usage conduit par l'abonné : aucune exposition ; les zones grises demeurent, existant compris.
- Option C, étendre sans demander : économie immédiate ; clause par défaut contraire (C1, C18), sanction possible sans préavis.
- Recommandation : A. Confiance 0,9.

**2. Statuer sur l'existant, session mère et sessions filles, en attendant la réponse.**
- Enjeu : la part sans geste humain de l'orchestration actuelle tombe sous C1.
- Option A, relever en un jour le mécanisme exact et garder ce qui passe par les fonctions du client et le parcours officiel de connexion, sous la conduite de l'abonné : continuité ; une zone grise subsiste.
- Option B, basculer sur clé les sessions lancées par script (C13 : un réglage suffit) : net ; coût au prix public, inconnu tant que les jetons ne sont pas comptés.
- Option C, ne rien relever : aucun effort ; on ignore ce que l'on fait.
- Recommandation : A, et B pour tout lancement par script avec jeton recopié. Confiance 0,6, faute d'avoir vu le mécanisme.

**3. Maintenir la chaîne de mesure à l'interface payante.**
- Enjeu : validité, appariement, facture.
- Option A, toute la mesure par clé, crédits inclus et crédits de recherche en premiers payeurs : traçable ; une dépense résiduelle.
- Option B, en plus, instruments de débogage en session, étiquetés et hors chiffres : économie marginale ; frontière à tenir.
- Option C, chaîne par modèle sous abonnement : 50 à 290 dollars épargnés au plus ; mesure non opposable, permission non acquise.
- Recommandation : A. Confiance 0,9.

**4. Rapatrier la page des crédits mensuels inclus et affecter ces crédits aux tranches de mesure.**
- Enjeu : la seule voie où l'abonnement paie des appels sans perte de validité.
- Option A, rapatrier, vérifier sur la console, affecter au palier 0 puis au pilote, compter au prix public : gain propre ; montant peut-être faible.
- Option B, attendre la réponse à la lettre : une seule démarche ; délai.
- Recommandation : A. Confiance 0,85.

**5. Choisir le canal des relectures et des demandes approfondies.**
- Enjeu : environ un dollar par relecture, contre l'en-tête de traçabilité et l'indépendance.
- Option A, relectures de travail en session conduite par l'abonné, dans un répertoire propre, et contre-lectures qui comptent par clé : économie modeste, preuves gardées.
- Option B, tout en session : quelques dizaines de dollars ; ni modèle servi ni réglages consignés.
- Option C, tout par clé : inchangé.
- Recommandation : A. Confiance 0,7.

**6. Protéger les secrets de mesure dans les sessions sous conditions grand public.**
- Enjeu : lois plantées, oracle et mode tenu à l'écart sont exposés à l'entraînement (C3) et à la mémoire de projet (C16).
- Option A, refuser l'entraînement sur chaque compte aujourd'hui et sortir ces fichiers des répertoires lus par les sessions : rapide ; l'exception de signalement demeure.
- Option B, en plus, instruire une formule d'équipe, placée sous conditions commerciales (page conformité : « Commercial Terms of Service - for Team, Enterprise, and Claude API users » ; C19) : régime de données plus sûr ; prix et conditions non lus.
- Option C, ne rien faire : aucun effort ; contamination possible des essais futurs.
- Recommandation : A tout de suite, B à instruire. Confiance 0,8.

FIN DE LA RÉPONSE

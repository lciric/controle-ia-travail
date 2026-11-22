# Refus de l'entraînement, sortie des secrets de mesure, formule d'équipe (version 1)

- Date : 2026-11-22T07:57:24Z (`date -u`) ; pages relevées entre 07:48Z et 07:56Z.
- Mot de Lazar : GO-2026-11-22-32, point 6 (« refus de l'entraînement et sortie des secrets : go, donne instructions détaillées » ; formule d'équipe à étudier).
- Aucune action faite d'ici : les réglages se font dans le compte du directeur ; **aucun fichier n'a été déplacé, ouvert ni listé** pour la partie secrets.

## Pages consultées (copies et empreintes dans `docs/sources/credits-recherche-v1/LISEZMOI-v1.md`)

| page | adresse | date affichée |
|---|---|---|
| Changer ses réglages d'amélioration des modèles | https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings | 3 août 2026 |
| Mes données servent-elles à l'entraînement ? | https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training | 16 mars 2026 |
| Usage des données personnelles dans l'entraînement | https://privacy.claude.com/en/articles/10023555-how-do-you-use-personal-data-in-model-training | 16 mars 2026 |
| Durée de conservation | https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data | 1er juillet 2026 |
| Tarifs | https://claude.com/pricing | non datée |
| Formule d'équipe pour les scientifiques (aide) | https://support.claude.com/en/articles/16634237-claude-team-plan-for-scientists | « Updated over 3 weeks ago » |
| Programme et conditions de cette formule | https://claude.com/programs/team-plan-for-scientists ; https://www.anthropic.com/legal/team-plan-for-scientists-terms | conditions en vigueur au 27 août 2026 |
| Crédits mensuels (déjà au dépôt) | https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans | « Updated this week » au 22 novembre |
| Conditions commerciales et page de conformité (déjà au dépôt) | `docs/sources/conditions-abonnement-claude-v1/` | 22 novembre 2026 |

**Vérifié en ligne** : le chemin des réglages, ce que couvre et ne couvre pas le refus, les durées de conservation, les prix et crédits des formules d'équipe. **Non vérifié** : que la page des réglages s'applique telle quelle à Ultra (elle nomme « Claude Free, Pro, Max » ; les conditions grand public couvrent Ultra : « Consumer Terms of Service - for Free, Pro, Max, and Ultra users », page de conformité) ; l'intitulé exact des boutons à l'écran ce jour (non vu d'ici, aucune connexion à un compte) ; ce que fait le refus pour les sessions de Claude Code en nuage (question 8 de la lettre).

---

## 1. Refuser l'utilisation des conversations pour l'entraînement, sur chaque compte claude.ai

### Pas à pas (navigateur ou application de bureau), d'après la page d'aide

1. Se connecter à claude.ai **avec le compte à régler**.
2. Cliquer sur son nom dans le menu (en bas à gauche), puis la flèche du menu déroulant.
3. Choisir **Settings** (accès direct donné par la page : https://claude.ai/settings/profile).
4. Choisir **Privacy** (accès direct donné par la page : https://claude.ai/settings/data-privacy-controls).
5. Sous **« Help Improve our AI models »**, mettre l'interrupteur sur arrêt.
6. Recharger la page et vérifier que l'interrupteur est resté sur arrêt. Noter la date, l'heure (UTC) et le compte (par son rôle, pas son adresse) dans une ligne de registre, sur ton mot.

Sur téléphone : nom → **Settings** → **Privacy** → **« Help Improve our AI models »** → arrêt.

**À faire sur chaque compte** qui ouvre des sessions du programme (session mère, sessions filles, comptes de secours) : le réglage est propre au compte, pas à l'appareil ni au dépôt.

### Ce que cela couvre (verbatim de la page d'aide)

- « If you decide to turn off the model training setting, we will not use any new chats and coding sessions you have with Claude for future model training. » Les **sessions de Claude Code** des comptes grand public sont comprises : la page vise « Claude Free, Pro, Max and when accounts from those plans use Claude Code ».
- **Conversations passées** : « we will stop using your previously stored chats and coding sessions in future model training runs ». Mais : « Your data will still be included in model training that has already started and in models that have already been trained ». Ce qui a été lu par une session avant le refus a pu entrer dans une course d'entraînement déjà commencée : **le refus ne rattrape pas le passé**.
- Ce qui est versé à l'entraînement quand le réglage est allumé : « the entire related conversation, along with any content, custom styles or conversation preferences » ; **pas** « raw content from connectors (e.g. Google Drive), including remote and local MCP servers, though data may be included if it's directly copied into your conversation ». Un fichier lu par Claude Code entre dans la conversation : il est couvert comme elle.
- Conservation si le réglage est allumé : « up to 5 years in our model training pipelines » ; une conversation supprimée est « Deleted from our back-end storage systems within 30 days ».
- Conversations « Incognito » : « not used to improve Claude, even if you have enabled Model Improvement ».

### Ce que cela ne couvre pas

- **Contenus signalés pour sûreté** : « If our safety classifiers flag your conversations, they may still be used to improve our internal trust and safety models, detect harmful content, enforce our policies, or advance our safety research. » Durée : « We retain inputs and outputs for up to 2 years and trust and safety classification scores for up to 7 years if your chat or session is flagged by our automated trust and safety systems as violating our Usage Policy. » Le programme parle de sabotage : des sessions peuvent être signalées. **Les secrets de mesure lus dans une session signalée restent exposés malgré le refus.**
- **Retours explicites** : un pouce (haut ou bas) envoie « the entire related conversation », un rapport de bogue les « data associated with that submission », gardés 5 ans ; les retours peuvent servir à « train our AI models ». **Ne jamais cliquer un pouce ni envoyer un rapport de bogue depuis une session qui a lu un secret de mesure.**
- **Inscription volontaire** à un programme d'essai (« Trusted Tester Program ») : vaut accord.
- Conservation « as required by law, to resolve disputes, or as necessary to combat violations of our Usage Policy ».
- Les appels par **clé de l'interface** ne relèvent pas de ce réglage : ils sont sous les conditions commerciales (« Anthropic may not train models on Customer Content from Services », conditions commerciales au dépôt).

---

## 2. Plan pour sortir les secrets de mesure des dossiers lus par les sessions (sans rien déplacer aujourd'hui)

Par « secrets de mesure » : les fichiers qui portent les lois plantées, l'oracle, le mode de sabotage tenu à l'écart et toute vérité qu'une session de conception ne doit pas voir. **Ce plan ne les nomme pas et n'en dresse pas la liste** ; l'inventaire nominatif est la première étape, faite par une session habilitée, et vit hors du dépôt de travail.

### Principes

1. **Un dépôt privé à part, pas un dossier à part.** Une session en nuage clone tout le dépôt de travail : tout ce qui y est, même dans un dossier « réservé », est lisible par elle et entre dans ses conversations. La seule frontière efficace est l'accès au dépôt : un dépôt privé distinct, `[NOM DU DÉPÔT DES SECRETS]`, jamais ajouté aux sessions de conception, jamais attaché par défaut.
2. **Les empreintes restent au dépôt de travail.** Pour chaque secret : son empreinte (sha256), sa date de scellement et le texte qui l'engage restent dans le dépôt de travail, ce qui garde l'engagement vérifiable (R6) sans exposer le contenu. Le dépôt des secrets porte les fichiers et leurs compagnons `.sha256` ; la vérification croisée est un script qui compare les deux sans afficher le contenu.
3. **Accès par habilitation.** Seules les sessions dont le rôle l'exige (fabrique des mondes, oracle, lecture finale) reçoivent le dépôt des secrets, sur mot de Lazar, une session à la fois, avec une ligne de registre « qui a lu quoi ». Le dispositif d'habilitation qui existe déjà au dépôt (registres d'accès réservé) sert de modèle ; ce plan ne l'a pas ouvert.
4. **Les sessions habilitées passent par clé quand c'est possible.** Une lecture de secret par une course lancée avec une clé de l'interface est sous les conditions commerciales (pas d'entraînement) ; une session sous abonnement reste sous le refus, avec l'exception des contenus signalés. Préférer, pour tout ce qui lit un secret, un programme appelé par clé à une session conversationnelle.
5. **Rien dans la mémoire de projet.** Le fichier de consignes du dépôt et les réglages chargés d'office par Claude Code ne nomment ni le chemin ni le contenu d'aucun secret (ils sont lus par toutes les sessions).
6. **On n'efface pas l'histoire.** Un fichier déplacé reste dans l'historique de git du dépôt de travail ; réécrire l'historique casserait les empreintes et contredit R12. Donc : (a) les secrets **déjà** versés au dépôt de travail sont tenus pour exposés aux sessions qui l'ont cloné ; (b) on ne réemploie pas comme « tenu à l'écart » un secret déjà exposé sans un texte qui le dise ; (c) les **secrets neufs** (famille tenue à l'écart neuve à chaque cycle, N-062 ; vérités plantées des bancs à faire, N-076) naissent directement dans le dépôt des secrets.
7. **La copie publique expurgée** (`scripts/depot_expurge.py`) ne doit jamais tirer du dépôt des secrets ; ajouter une garde qui refuse toute source hors du dépôt de travail.

### Étapes proposées (chacune sur mot de Lazar ; aucune faite)

1. Lazar crée le dépôt privé des secrets sur GitHub (compte, dépôt distant : nœud de décision) et le laisse vide.
2. Une session neuve, habilitée, sans autre tâche, dresse l'**inventaire nominatif** des secrets du dépôt de travail par **nom, taille et empreinte seulement**, sans les ouvrir, et le verse **dans le dépôt des secrets** ; au dépôt de travail, seule l'empreinte de l'inventaire.
3. Classement de chaque secret : déjà exposé (reste où il est, marqué exposé dans un registre, réemploi interdit sans texte) ou à protéger (copie au dépôt des secrets, puis, sur mot de Lazar, remplacement au dépôt de travail par un fichier témoin qui porte l'empreinte et l'emplacement ; le fichier d'origine n'est jamais écrasé, R12 : nouvelle version du témoin, ancienne archivée).
4. Les lanceurs et programmes qui lisent un secret prennent son chemin d'une variable d'environnement et vérifient l'empreinte avant lecture ; garde éprouvée sur un cas sain et sur un artefact (R5).
5. Contre-lecture de l'ensemble (classe B : instrument), puis passation.

---

## 3. La formule d'équipe : conditions commerciales, prix, crédits inclus

### Formule d'équipe ordinaire (page des tarifs, relevée le 22 novembre 2026)

- « For teams of 2 to 150 » : **deux sièges au moins**.
- Siège standard : « $20 Per seat / month if billed annually. $25 if billed monthly. »
- Siège premium : « 5x more usage than standard seats » ; « $100 Per seat / month if billed annually. $125 if billed monthly. »
- Fable : « 50% of weekly limits » sur les sièges premium (tableau des formules).
- Données : « No model training on your content by default » ; la page de conformité place la formule sous « Commercial Terms of Service - for Team, Enterprise, and Claude API users ».
- Crédits d'interface : « Up to $500 per month in pooled API credits » ; page d'aide : 20 USD par siège standard, 100 USD par siège premium, réunis en un solde mensuel plafonné à 500 USD.

### Formule d'équipe pour les scientifiques (aide, programme et conditions)

- « Standard seats: $0 per user per month » ; « Premium seats: $15 per user per month, or $180 per user per year with annual billing », pendant 12 mois, puis « then-current price ».
- « From 1 to 25 seats per group » : **possible à un seul siège**.
- Éligibilité : « Principal investigators (PIs) or equivalent at accredited universities and nonprofit research institutes working in the natural sciences, mathematics, computer science, engineering, and related fields » ; « For-profit companies, contract research organizations, and industry R&D teams are not eligible. » Vérification à l'inscription : https://claude.ai/labs-verification/attestation (lien de la page du programme), « Most applications are reviewed within seven business days ».
- Conditions : « These Promotional Terms are Supplemental Terms under Anthropic's Commercial Terms of Service » ; usage au-delà de l'allocation « billed separately at Anthropic's then-current standard rates » ; sans activité 90 jours de suite, retour au prix ordinaire possible ; « creating multiple accounts or adding ineligible users » met fin à la remise.
- Crédits d'interface : 20 USD par siège standard, 100 USD par siège premium, plafond 500 USD par mois. Au-delà : le programme « AI for Science » (voir `demande-credits-recherche-anthropic-v1.md`).

### Ce qui change en passant d'Ultra à une équipe

- Ultra (page des tarifs) : 200 USD par mois, « 10x Pro usage every week », 200 USD de crédits d'interface par mois, pas de limite de cinq heures pour les comptes vérifiés ; conditions grand public, entraînement sauf refus.
- Page des crédits mensuels : « Move from Max or Ultra to Team. Your Max or Ultra link ends. » ; les crédits de l'équipe se réclament après sept jours de formule active.
- Les volumes d'usage d'un siège premium et d'Ultra ne sont pas comparables sur les pages (l'un est exprimé en multiple d'un siège standard, l'autre en multiple de Pro) : **non tranché** ; un essai d'un mois le dirait.
- Le gain principal est le **régime des données** (conditions commerciales, pas d'entraînement par défaut, plus de dépendance au réglage compte par compte) ; l'exception des contenus signalés sous les conditions commerciales n'a pas été lue d'ici (question ouverte).

### Recommandation [proposition, confiance 0,6]

Si [AFFILIATION] permet la formule pour scientifiques : l'instruire pour les seules sessions qui lisent des secrets de mesure (un ou deux sièges premium, 15 USD chacun par mois), Ultra gardé pour le reste. Sinon, la formule ordinaire impose deux sièges et ses volumes ne sont pas établis : ne pas basculer avant la réponse à la lettre et un essai. Nœud de décision : compte et dépense, mot de Lazar.

## Réserves

- Le pas à pas suit le texte de la page d'aide ; les intitulés à l'écran peuvent différer d'un mot (non vus d'ici).
- La portée du refus pour Ultra et pour les sessions en nuage est posée dans la lettre (question 8) : jusqu'à la réponse, tenir pour exposé tout ce qu'une session sous abonnement a lu.

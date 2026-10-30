# Revue de sûreté sur pièces — The Agentic Scientist v3 (`SakanaAI/AI-Scientist-v3` @ `df83138`) avec Headless (@ `93cd9b0`) et Claude Code — v1

De : conv-audit (sous-agent Opus, sans installation, sans exécution, aucune dépense, aucune clé). Pour : Lazar ; copie session-depot.
Mandat : R-557 (Lazar, 30 octobre, 08:09 heure de Paris) : v3 **en plus** de la v2, **intacte**, **Web des agents ouvert**, protégée de la contamination ; machine louée jetable avec Docker ; appels au modèle par **notre relais** (clé dans le relais seulement, plafond, liste des modèles, trace).
Rédigée le 30 octobre 2026 vers 07:20 UTC (`date -u` lu à 07:16:10 UTC).

## 0. Ce qui a été lu, et ce qui ne l'a pas été — réserve majeure

- **Les fichiers bruts du dépôt n'ont pas pu être lus dans cette session** : `raw.githubusercontent.com` et les pages `github.com/…/blob/…` sont refusés par la liste blanche de l'outil de lecture Web (« URL_NOT_ON_ALLOWLIST », plusieurs essais). Seule la page d'accueil du dépôt (README rendu, branche `main`, **non épinglée**) et celle de Headless ont pu être lues, en résumé.
- Donc : toute référence « fichier l.N » ci-dessous est **RAPPORTÉE** de la vérification sur pièces primaires de session-depot (`docs/notes/ideation-organisme-v1/ia-scientifique-externe-v1/verification-pieces-primaires-v1.md`, lue par `git show origin/main:`, sources consultées le 29 octobre de 22:31 à 22:36 UTC, abrégée **VPP n°k**). Tout le reste est **SUPPOSÉ** et marqué comme tel. **Cette revue est une revue d'architecture, pas une revue de code** : la lecture du code (§ 7, point M0) reste un préalable au lancement.
- **Lu en entier et opposable** : l'article, PDF `docs/sources/pdf/2610.18933v1.pdf`, sha256 `cb170b5435743032755f89b97136464a024df2c0fb4f46286a69945208585fd5` (vérifié contre `2610.18933v1.pdf.sha256`), pages citées.
- Documentation courante de Claude Code (version indonésienne de la page des variables d'environnement, `code.claude.com/docs/id/env-vars`, lue ce jour ; **non épinglée sur la version 2.1.285** de l'image, VPP n°40).

## 1. Résumé (dix lignes)

1. Le relais peut porter **tous** les appels de Claude Code par `ANTHROPIC_BASE_URL` plus un jeton factice ; mais Headless ne transmet pas cette variable d'office (VPP n°41 ; usage.md l.345) : il faut la poser **dans l'image** (réglages gérés de Claude Code) ou par `--docker-env` (usage.md l.186) — chemin par `agsci` non lu.
2. Autres fournisseurs : relecture facultative et figures de concept vers OpenAI (README l.211-212), repli Gemini pour les figures ; on les coupe en **ne donnant aucune clé** et en ne lançant pas la phase `review`. Bedrock : aucune variable `AWS_*`, aucun mode de repli configuré.
3. Réseau : `agsci run` met les conteneurs en réseau `host` (install.md l.163, l.170 ; README l.143-144). À remplacer par un **réseau Docker interne sans route**, dont le seul voisin est un **mandataire de sortie journalisé** ; métadonnées, hôte, réseau local et IPv6 bloqués en plus par le pare-feu de l'hôte.
4. Contamination : le mandataire journalise adresse, date, statut et contenu rendu (empreinte) de chaque requête, conteneur par conteneur ; la recherche Web de Claude Code passe en plus **par le relais** (outil côté serveur, SUPPOSÉ) et y est tracée.
5. Retirer le `.env` monté (install.md l.129-131) ; aucun secret sur la machine ; servir seulement la question et des données publiques, avec **notre propre évaluateur** (la rédaction de tâche est expérimentale, README l.279-293 ; article p.22).
6. Dépense : aucun plafond local (Headless README l.157-158). Bornes côté v3 : cycles d'idées, réplications, analyses, ouvriers, délais ; bornes externes : plafond 402 du relais, `timeout` du processus, destruction programmée de la machine.
7. Retenir **Docker**, sur une **vraie machine virtuelle** (pas un conteneur Vast.ai, R-377) : le mode natif lance des agents à pleins droits sur l'hôte, en réseau de l'hôte, et les six phases natives ne sont pas vérifiées (VPP n°35).
8. Licence Apache-2.0 (v3 et Headless) : usage interne libre ; toute redistribution garde la licence et signale les fichiers modifiés. Aucune mention de génération par machine imposée par la licence, mais les articles produits sont **filigranés** par le système (p.37) et l'article demande la divulgation (p.22) : on garde le filigrane et on étiquette.
9. Ordre de grandeur de coût : seule la figure 16 (p.19) en donne : environ 430 USD cumulés pour environ 50 cycles avec Opus 4.7 + Claude Code (≈ 8 à 9 USD par cycle, phase d'investigation, tâche sur cartes) — **lecture de figure, non opposable** comme chiffre.
10. Recommandation : **aucun lancement avant M0 (lecture du code aux commits épinglés) et l'essai à blanc du § 8** ; devis machine au § 9.

## 2. Question 1 — Relais

**Comment les agents reçoivent adresse et modèle.**
- Le modèle se choisit par `agent.name` et `agent.model` (README rendu, `main` ; SUPPOSÉ identique à `df83138`). v3 appelle Headless, qui lance `claude` en mode non interactif dans un conteneur (README l.89-93, l.123-125 ; `--allow yolo`, README l.40-45).
- Headless transmet aux conteneurs les « identifiants courants » des agents et fournisseurs ; **toute autre variable passe par `--docker-env`** (usage.md l.345, l.186 ; VPP n°39). `ANTHROPIC_BASE_URL` **n'est pas dans la liste** (VPP n°41). Que `agsci` expose un moyen de passer `--docker-env` ou `--docker-arg` : **non lu** (SUPPOSÉ : non configurable sans retouche).
- Le README dit que **seules les clés de l'agent choisi** sont transmises à ses conteneurs (README rendu) ; pour `claude` : `CLAUDE_CODE_OAUTH_TOKEN` ou `ANTHROPIC_API_KEY` (README l.134).
- Côté Claude Code (documentation courante) : `ANTHROPIC_BASE_URL` remplace l'adresse de l'interface ; `ANTHROPIC_API_KEY` part dans l'en-tête `X-Api-Key` et, en mode non interactif, est toujours utilisée si présente ; `ANTHROPIC_DEFAULT_HAIKU_MODEL` fixe le modèle des **tâches de fond** ; `ANTHROPIC_DEFAULT_SONNET_MODEL` / `_OPUS_MODEL` résolvent les alias ; `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` coupe mises à jour, télémétrie, rapports d'erreur, notes de version et lecture des drapeaux de fonction (toute valeur non vide, même `0`).

**Réglage minimal qui fait passer tous les appels par le relais, sans toucher au code Python de v3 (recommandé).**
- Construire une **image dérivée** (nouveau nom, R12) de `agentic-scientist/agent-cli` dont la seule différence est un fichier de **réglages gérés de Claude Code** (chemin système de Linux, SUPPOSÉ `/etc/claude-code/managed-settings.json`, à vérifier sur 2.1.285) qui fixe dans son bloc `env` : `ANTHROPIC_BASE_URL` (adresse interne du relais, § 3), `ANTHROPIC_DEFAULT_HAIKU_MODEL`, `_SONNET_MODEL`, `_OPUS_MODEL` sur des modèles **de la liste du relais**, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`, et les variables du mandataire (`HTTPS_PROXY`, `HTTP_PROXY`, `NO_PROXY`, `NODE_EXTRA_CA_CERTS`). Les réglages gérés priment sur ceux de l'utilisateur et ne peuvent pas être écrasés par l'agent (SUPPOSÉ, à éprouver § 8).
- Jeton factice : `ANTHROPIC_API_KEY=<jeton de course>` dans l'environnement du processus `agsci` sur l'hôte ; Headless le transmet comme identifiant courant. Ce jeton n'ouvre que le relais, est révocable, propre à la course et plafonné : ce n'est pas un secret du programme.
- Repli si les réglages gérés ne prennent pas : retouche d'**une ligne logique** là où v3 construit la commande Headless (fichier non lu, SUPPOSÉ dans `src/`) pour ajouter `--docker-env` pour chacune de ces variables ; fichier modifié signalé (licence, § 7).
- Côté relais : nouvelle version (R12) du relais Claude, qui écoute aujourd'hui **sur la boucle locale seulement** avec le jeton littéral `relais-local-sans-cle` et **`/v1/messages` seul** (note A § 4.1). Il faut : (a) le joindre depuis la machine louée sans y poser la clé (§ 3) ; (b) un jeton par course ; (c) accepter ou refuser proprement `/v1/messages/count_tokens` (Claude Code peut l'appeler, SUPPOSÉ) ; (d) liste des modèles contrôlée sur le champ `model` du corps, **y compris le modèle de fond** ; (e) trace complète (requête, réponse, en-têtes sans secret) ; (f) plafond en USD, refus 402.

**Autres fournisseurs et comment les couper.**
| Appel | Pièce | Coupure |
|---|---|---|
| Relecture du manuscrit par OpenAI (phase `review`, et `agsci review`) | README l.211-212 ; README rendu : lit `OPENAI_API_KEY` | ne pas activer la phase `review` ; aucune `OPENAI_API_KEY` ; le mandataire refuse `api.openai.com` (refus journalisé) |
| Figures de concept : OpenAI, repli Gemini, sinon export simple | README rendu (`main`) | aucune clé OpenAI ni Gemini → export simple (comportement documenté) ; autoillustrate (article § E) à vérifier |
| Claude par Bedrock (voie payante de repli de Headless) | docs/agent_billing.md l.11-12 ; H@README l.138-149 (« With no detected subscription or configured backup, `auto` preserves native authentication ») | aucune variable `AWS_*`, `CLAUDE_CODE_USE_BEDROCK` absente, aucun « backup » configuré ; le mandataire refuse `bedrock*.amazonaws.com` |
| Abonnement Claude | README l.134 | aucun `CLAUDE_CODE_OAUTH_TOKEN`, aucun dossier `~/.claude` de l'hôte monté |
| Télémétrie et services de Claude Code (mises à jour, rapports d'erreur, drapeaux) | documentation courante | `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` ; le mandataire refuse `api.anthropic.com`, `statsig*`, `sentry*` (ce n'est pas le Web des agents : v3 reste intacte) |
| Google Scholar par `scholarly` (recherche bibliographique à la rédaction) | pyproject l.40 ; article p.22 | **laissé ouvert** (Web des agents), journalisé |
| Contrôle de domaine avant `WebFetch` de Claude Code (appel à Anthropic) | SUPPOSÉ | si l'appel direct à Anthropic est refusé, `WebFetch` peut échouer : régler `skipWebFetchPreflight` dans les réglages gérés (SUPPOSÉ), à éprouver |

## 3. Question 2 — Réseau

- **État par défaut** : `agsci run` met les conteneurs en réseau `host` (install.md l.163, l.170 ; README l.143-144 ; VPP n°36). Un conteneur en réseau `host` voit tous les services de l'hôte en boucle locale, le service de métadonnées du nuage (169.254.169.254 : identifiants d'instance, données de démarrage) et le réseau local du fournisseur.
- **Cible** :
  1. Réseau Docker utilisateur **interne** (`internal: true`, nouveau nom, par exemple `agsci-interne-v1`) : aucune route vers l'extérieur ni vers l'hôte par construction. Tous les conteneurs de phase y sont attachés.
  2. Un conteneur **mandataire de sortie** à deux pattes (réseau interne + un pont sortant à lui seul) : seul chemin vers le Web, il journalise tout (§ 4). Les agents ont `HTTPS_PROXY`/`HTTP_PROXY` vers lui ; un outil qui ignore le mandataire **échoue** (fermé par défaut, R5 : pas de repli silencieux).
  3. Un **relais-passe** : sur le réseau interne, un nom unique (`relais`) qui ne transmet qu'à **une seule adresse** du relais réel (hors machine) ; c'est la valeur de `ANTHROPIC_BASE_URL`. Le mandataire refuse toute autre destination Anthropic.
  4. **Pare-feu de l'hôte** (chaîne `DOCKER-USER` et `INPUT`, IPv4 et IPv6), pour le pont sortant du mandataire : refuser 169.254.0.0/16, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 100.64.0.0/10, l'adresse publique et la passerelle de l'hôte ; IPv6 coupé dans Docker ou filtré de même. Refuser du réseau interne vers l'hôte tout port autre que rien (aucun service de l'hôte n'est servi aux conteneurs).
  5. **Socket Docker jamais monté** dans un conteneur de phase (à vérifier dans le lanceur et le courtier de l'évaluateur, M0).
- **Où se règle-t-il** : le choix `host` est fait par `agsci run` (install.md l.163, l.170) ; **la clé de réglage exacte n'a pas été lue** (SUPPOSÉ : option du lanceur ou du préréglage dans `configs/`). Voies, dans l'ordre : (a) un réglage existant de `agsci` (à chercher, M0) ; (b) `--docker-arg --network=agsci-interne-v1` passé à Headless, si `agsci` le relaie ; (c) retouche minimale du lanceur pour remplacer `host` par le nom du réseau. `agsci investigate` et la phase post-hoc sont en `bridge` (VPP n°36) : même traitement.
- Relais réel : hors machine, joint par un tunnel chiffré sortant (adresse unique, jeton par course, liste d'adresses source). Le relais n'expose rien d'autre.

## 4. Question 3 — Contamination (Web ouvert)

**Points d'accrochage pour journaliser chaque requête Web.**
- **Mandataire de sortie à interception TLS** (par exemple mitmproxy, ou Squid avec déchiffrement) : pour chaque requête, date (horloge de l'hôte synchronisée), conteneur source (nom et étiquettes → phase, ouvrier, cycle), méthode, adresse complète, statut, en-têtes de réponse, **corps rendu** stocké par empreinte sha256 (contenu textuel en entier ; binaires volumineux — paquets, jeux de données, poids — en métadonnées et empreinte seulement). L'autorité de certification du mandataire est ajoutée à l'image dérivée : `NODE_EXTRA_CA_CERTS` (Claude Code), `SSL_CERT_FILE`/`REQUESTS_CA_BUNDLE` (Python, `pip`), `git config http.sslCAInfo`. Ce qui refuse l'autorité (épinglage de certificat) échoue et se consigne.
- **Recherche Web de Claude Code** : outil exécuté côté serveur par l'interface d'Anthropic (SUPPOSÉ) ; la requête et les résultats reviennent dans la réponse de `/v1/messages` : **tracés par le relais**. `WebFetch` est exécuté dans le conteneur : tracé par le mandataire ; son résumé par le modèle de fond repasse par le relais.
- **Journaux de v3 et de Headless** : dossier de course `results/<task>/<agent>/<run_id>/` (README rendu) ; registre de coût par course (pipeline.md l.296-299, VPP n°34) ; mémoire partagée et conclusions publiées à chaque fin de cycle (article p.5) : **dater chaque entrée de mémoire** permet de rattacher une idée aux requêtes Web du même conteneur dans la fenêtre du cycle. Options `--usage` et `--debug` de Headless (README de Headless).
- **Scellement** (R6) : en fin de course, journal du mandataire, trace du relais et dossier de course scellés ensemble, empreintes consignées avant toute lecture des résultats (R1, régime exploratoire).
- Limite à écrire : ce qui vient des **données d'entraînement** du modèle n'est pas traçable ; l'article le dit pour ses propres résultats (p.17 : techniques « likely appeared in the underlying model's training data » et accessibles « through web search »).

**Que monte-t-on dans les conteneurs.**
- **Retirer le `.env` monté** (install.md l.129-131) : aucun fichier de secrets sur la machine. Le jeton de course passe par l'environnement du processus `agsci`.
- Monter seulement : le dossier de tâche (lecture seule), le dossier de course, l'espace temporaire (`AGENTIC_TEMP_ROOT`, README rendu). Jamais : `~/.claude`, `~/.ssh`, `~/.config` de l'hôte, le socket Docker, un dossier du programme. Le « foyer Docker durable » de Headless (`--session`, README de Headless) doit vivre sous le dossier de course, à vérifier.

**Entrées servies sans fuite.**
- Une `task.md` qui porte **la question seule**, au niveau méthode, dans le vocabulaire contraint de Lazar (R-478 : théorie de la détection, sans les mots exclus), plus **notre évaluateur et un simulateur de données publiques ou synthétiques** (comme le devis du 26 octobre, `envois/portage-controlarena-v1/devis-essai-agentic-scientist-v3-v1.md` § 2). Ne rien servir de : préenregistrements, registres, données des pilotes, `test_final`, transcriptions, fiches de nos courses, code du dépôt.
- Fournir l'évaluateur nous-mêmes plutôt que la rédaction de tâche (README l.279-293 : « experimental… not yet robust » ; article p.22) ; écrire **explicitement** dans la grille l'intégrité du protocole d'évaluation : l'article a vu un agent changer le protocole d'évaluation sans que l'évaluateur ni la grille le signalent (p.18-19).
- **Contamination croisée à trancher par Lazar** : le Web ouvert laisse l'agent trouver la copie expurgée publique `lciric/controle-ia` (et nos éventuelles publications). Proposition : journaliser et **marquer** toute visite de `github.com/lciric/*` ; décider avant la course s'il faut bloquer ce seul préfixe (écart minimal à « Web ouvert »).

## 5. Question 4 — Dépense

- **Aucun plafond local** dans Headless (H@README l.157-158).
- **Bornes côté v3** (README rendu, `main`) : nombre de cycles d'idées (défaut 3), réplications d'ablation (défaut 5), analyses post-hoc (défaut 3), délai du harnais d'évaluation (7 200 s par défaut sur carte), nombre d'ouvriers, élagage. L'article tourne à **20 itérations d'idées par course** (p.11) ; il montre que 2 ouvriers suffisent et que plus n'aide pas (p.18, figure 15). Clés exactes : non lues (SUPPOSÉ dans `configs/preset/`).
- **Bornes côté agent** : `--timeout` de Headless (README de Headless) ; `BASH_MAX_TIMEOUT_MS` de Claude Code (défaut 600 000 ms, documentation courante) ; nombre maximal de tours et plafond en dollars de Claude Code en mode non interactif (SUPPOSÉ : existent dans les versions récentes ; à vérifier sur 2.1.285 et sur la transmission par Headless).
- **Bornes externes** (indépendantes de v3, donc v3 intacte) : plafond 402 du relais **par course** ; `timeout` du processus `agsci` sur l'hôte ; destruction programmée de la machine chez le fournisseur ; arrêt par identifiant d'instance (R10).
- **À éprouver** : ce que fait v3 sur un refus 402 (arrêt propre, ou boucle de relances) ; qu'aucun repli de facturation de Headless ne s'active (§ 2).

## 6. Question 5 — Mode natif contre Docker

**Docker, sur une machine virtuelle louée avec accès administrateur.** Raisons :
- Le mode natif lance des agents à pleins droits (`--allow yolo`) **sur l'hôte**, avec son réseau, son système de fichiers et l'accès aux métadonnées du nuage ; rien ne sépare les phases. Le README demande lui-même de rester dans l'image Docker (README rendu ; README l.40-45).
- La protection de l'évaluateur (les candidats ne peuvent pas écrire dans ses sorties, docs/evaluation_evidence.md l.9-10) repose vraisemblablement sur les montages des conteneurs (SUPPOSÉ) ; le mode natif des six phases n'est pas vérifié (VPP n°35).
- Le réseau interne avec mandataire journalisé (§ 3, § 4) n'existe qu'avec Docker.
- Jetable ne suffit pas : la machine porte le jeton de course, le tunnel vers le relais et l'accès aux métadonnées du compte de nuage ; il faut quand même fermer.
- **Pas d'instance Vast.ai** : ce sont des conteneurs où les espaces de noms réseau sont refusés (R-377) ; un démon Docker n'y tourne pas. Il faut une machine virtuelle complète. Données de démarrage (`cloud-init`) sans aucun secret.

## 7. Question 6 — Licence et mentions

- v3 : Apache-2.0 (LICENSE ; pyproject l.11 ; VPP n°23). Headless : Apache-2.0 (VPP n°37). Usage interne libre. Si nous redistribuons (copie expurgée, annexe d'un papier) : joindre la licence, garder les mentions, **signaler chaque fichier modifié** (§ 4 b de la licence), joindre le fichier NOTICE s'il existe (aucun à la racine d'après la liste des fichiers de `main` ; à confirmer sur `df83138`).
- Claude Code, installé dans l'image en version 2.1.285 (Dockerfile l.58) : logiciel sous les conditions d'Anthropic, non Apache ; **ne pas publier l'image dérivée**.
- La licence n'impose **aucune** mention de génération par machine (contrairement à la licence de v2, l.39-40). Mais : les articles générés sont **filigranés** par le système (article p.37, figure 19) ; l'article demande divulgation des contributions des agents et filigrane (p.22). Conduite proposée : ne jamais retirer le filigrane ; étiqueter toute sortie versée au dépôt « généré par machine — The Agentic Scientist v3, `df83138`, modèle, date » ; citer arXiv 2610.18933 (CITATION.cff) dans tout papier qui s'en sert ; aucune soumission de ses sorties (interdit du programme).

## 8. Liste des modifications et réglages avant tout lancement

| n° | Quoi | Où |
|---|---|---|
| M0 | **Lire le code aux commits épinglés** (sous-agent neuf, accès aux fichiers bruts) : lanceur de conteneurs de `agsci` (choix `host`, montages, `.env`, socket Docker), construction de la commande Headless (`--docker-env`, `--docker-arg`, délais), courtier de l'évaluateur, phases `review` et figures, `configs/preset/*` ; Headless entière (variables transmises, repli de facturation, `--session`) ; Dockerfile (versions, `ENV`) | `df83138`, `93cd9b0` |
| M1 | Image dérivée (nouveau nom) : réglages gérés de Claude Code (bloc `env` du § 2, `skipWebFetchPreflight` si nécessaire), autorité du mandataire dans les magasins de certificats | `src/docker/agent-cli/Dockerfile` copié sous un nouveau nom ; rien d'autre |
| M2 | Ne pas monter le `.env` ; aucune clé réelle sur la machine ; jeton de course seul dans l'environnement de `agsci` | install.md l.129-131 ; lanceur |
| M3 | Réseau interne + mandataire journalisé + relais-passe ; remplacer `host` (et `bridge` des autres commandes) | install.md l.163, l.170 ; lanceur ou réglage de `agsci` |
| M4 | Pare-feu de l'hôte (métadonnées, réseaux privés, hôte, IPv6) | chaîne `DOCKER-USER`, `INPUT` de la machine |
| M5 | Relais nouvelle version : écoute par tunnel, jeton par course, liste des modèles incluant le modèle de fond, comptage de jetons traité, trace, plafond 402 par course | relais Claude de session-depot (nouveau nom, R12) |
| M6 | Phase `review` désactivée ; aucune clé OpenAI, Gemini, AWS, abonnement | préréglage de course |
| M7 | Bornes : cycles, ouvriers (2), réplications, délais ; `timeout` du processus ; destruction programmée | préréglage ; hôte ; fournisseur |
| M8 | Tâche : `task.md` (question seule, vocabulaire contraint), notre évaluateur, simulateur, grille avec intégrité du protocole d'évaluation ; décision de Lazar sur `github.com/lciric/*` | dossier de tâche, lecture seule |
| M9 | Scellement de fin de course : journal du mandataire, trace du relais, dossier de course ; manifeste (R9 : graines, versions, commits) | dossier de course ; `runs/` |

## 9. À vérifier par un essai à blanc sur la machine louée (avant tout appel payant)

Relais branché sur un **amont factice** (zéro dépense), puis un seul appel réel plafonné.
1. Depuis un conteneur de phase : 169.254.169.254, l'adresse de l'hôte, la passerelle, 10/8, 172.16/12, 192.168/16, une adresse IPv6 : **tous refusés** ; une page Web publique : servie **et** journalisée (adresse, date, corps, empreinte, conteneur).
2. Requête directe à `api.anthropic.com`, `api.openai.com`, `bedrock…amazonaws.com` : refusées et journalisées.
3. Claude Code dans le conteneur : `ANTHROPIC_BASE_URL` effective (relais voit l'appel), modèle principal **et** modèle de fond dans la liste, aucun appel hors `/v1/messages` sauf ceux attendus ; l'agent ne peut pas écraser les réglages gérés (essai : lui demander de changer l'adresse).
4. Recherche Web et `WebFetch` : la première apparaît dans la trace du relais, la seconde dans le journal du mandataire.
5. `env` dans chaque conteneur : aucune clé réelle, aucun `.env`, aucun socket Docker, aucun montage de l'hôte autre que ceux du § 4.
6. Refus 402 du relais en cours de phase : arrêt propre de v3, sans relance infinie ni bascule de facturation (R5 : cas sain et artefact).
7. Une course complète sur une tâche jouet sur processeur (une itération) jusqu'au manuscrit : phases toutes sur le réseau interne ; protection de l'évaluateur intacte ; filigrane présent.
8. Mesure du coût d'une itération (relevé du relais) → plafond de la course réelle.

## 10. Ce qui entre dans le devis (pour session-depot)

- **Machine** : machine virtuelle complète avec accès administrateur (pas un conteneur), sans carte graphique pour notre tâche sur processeur ; **8 à 16 processeurs virtuels** (l'article donne 8 cœurs pour sa tâche sur processeur, p.11, tableau 3 ; plus de la marge pour 2 ouvriers et le mandataire), **32 Go de mémoire**, **150 à 200 Go de disque** (images Docker avec dépendances d'apprentissage, espace temporaire, journaux du mandataire) — mémoire et disque SUPPOSÉS, sans pièce ; Docker Engine récent ; IPv6 coupable ; destruction programmée possible chez le fournisseur.
- **Durée** : essai à blanc et installation 4 à 6 heures ; course : l'article donne 30 minutes par itération de recherche pour sa tâche sur processeur (p.11, tableau 3) et 20 itérations par course (p.11) → de l'ordre de 5 à 10 heures avec 2 ouvriers (inférence), plus les autres phases → **prévoir 12 à 24 heures par course**, plus la marge.
- **Appels au modèle** : l'article ne donne **aucun coût par course dans le texte**. Seule la figure 16 (p.19, tâche d'apprentissage par renforcement sur cartes, phase d'investigation seule, trois graines) montre un coût cumulé d'environ **430 USD pour environ 50 cycles avec Opus 4.7 + Claude Code**, environ 180 avec GPT-5.6-Sol + Codex, environ 90 avec Kimi K3 + Pi ; le texte dit que Pi réduit le coût de 75 % (p.18). **Lecture de figure, ordre de grandeur seulement, non opposable** ; on ne sait pas si l'axe cumule les trois graines. Notre devis du 26 octobre (10 USD pour c0, 60 USD pour 5 à 10 itérations en c1) est donc **serré** au barème de la figure (≈ 8 à 9 USD par cycle) ; le plafond se fixe après la mesure du point 8 du § 9.
- **Relais et tunnel** : temps de travail de session-depot (nouvelle version du relais, tunnel) ; aucun service payant supposé.

## 11. Réserves

- Revue d'architecture sans lecture du code (§ 0) : toute ligne non rapportée de VPP est SUPPOSÉE ; le README lu est celui de `main`, non épinglé.
- Comportements de Claude Code tirés de la documentation courante, non de la version 2.1.285 : réglages gérés, contrôle avant `WebFetch`, recherche Web côté serveur, tours et plafond en mode non interactif sont SUPPOSÉS.
- Chiffres de coût lus sur une figure (§ 10) : non opposables.

Horodatage : écrit le 2026-10-30, fichier finalisé à 07:18:19 UTC (`date -u` lu dans la commande qui scelle).

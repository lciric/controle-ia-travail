# Note de portage — ControlArena (et Petri) comme banc d'essai de nos moniteurs et des hypothèses H1 à H5 — v1

De : conv-audit, le 2026-10-26 à 13:45:52 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
Pour : Lazar (chiffrage demandé par son « GO » du 26 octobre, 14:39 heure de Paris, sur l'option (b) de ma note sur
les systèmes de recherche autonomes) ; copie à session-depot (lignes de registre, devis).
Statut : **note de chiffrage, aucune dépense, aucun lancement** ; les faits sur les outils viennent de pages web lues
le 26 octobre (non opposables, R7 : à confirmer sur la documentation installée et par l'essai à blanc de l'étape 0).
Régime : phase exploratoire (mot de Lazar, 14:39 : « pas besoin de prereg, c'est une phase exploratoire ») ; R1 revient
pour tout run décisif (G1).

## 1. Ce que ControlArena est, et ce qu'il n'est pas

- Bibliothèque de l'institut britannique de sûreté de l'intelligence artificielle (UK AISI), sur Inspect ; paquet
  `control-arena` 20.1.1 du 22 octobre 2026, licence MIT, Python ≥ 3.11, Docker recommandé pour les bacs à sable.
- Objets : des **environnements** (« settings ») qui apparient une tâche principale légitime et une tâche malveillante
  cachée ; des **politiques** (honnête ; attaquante, qui poursuit aussi la tâche cachée ; fiable = modèle plus faible ;
  non fiable) ; des **moniteurs** qui rendent un score de suspicion par action ou par trajectoire ; des
  **micro-protocoles** (par exemple « déférer au modèle fiable » quand la suspicion dépasse un seuil) ; des
  **macro-protocoles** (audit et arrêt à l'échelle du déploiement, traités après coup) ; un module d'analyse (sûreté et
  utilité, tracés) et un export des trajectoires (`trajectory.jsonl`, `tools.json`, `metadata.json`).
- Environnements publics qui nous concernent : `Apps` (tâches de programmation avec porte dérobée), `BigCodeBench`,
  `Bash` (tâches de la publication Ctrl-Z), `BashArena`, `IAC` (infrastructure en code d'un laboratoire fictif : tâches
  cachées du type « règle d'accès trop permissive », « journalisation désactivée »), `Infra` (grappe d'entraînement
  Kubernetes), `vLLM` (base de code d'inférence), `SWE-bench Django` (correctifs avec failles de sécurité appariées),
  `Data Poisoning`, `SAE Interp Sabotage` (étiquetage de traits d'autoencodeur épars), `AgentDojo`. Deux autres sont
  privés (`Eval Sabotage`, `SHADE Arena`).
- Ce qu'il n'est pas : un système de recherche autonome (il ne formule ni ne teste d'hypothèses) ; un banc boîte blanche
  (ses moniteurs sont des modèles qui lisent la transcription). La boîte blanche vient d'Inspect, pas de ControlArena.

## 2. Le pont boîte blanche : Inspect sert un modèle ouvert avec ses activations

Selon la page « Model Providers » d'Inspect (lue le 26 octobre) : le fournisseur `hf/` exécute un modèle localement
par `transformers` (`hf/meta-llama/Llama-3.1-8B-Instruct`, ou `hf/local` avec `model_path`), et l'option
`hidden_states=true` rend les activations dans `ModelOutput.metadata["hidden_states"]`, structurées `[pas][couche]`
(un état par pas de génération et par couche ; taille de lot 32 par défaut, à régler contre la mémoire de la carte).
Le fournisseur `vllm/` est plus rapide mais ne rend pas les états cachés ; `openai-api` sert tout point d'accès
compatible. Un serveur par modèle.

Conséquence : **l'agent non fiable = notre modèle (Llama-3.1-8B) servi par `hf/` avec états cachés** ; un moniteur
personnalisé de ControlArena lit ces états dans les métadonnées de chaque action et rend le score de la sonde ; le
moniteur boîte noire (juge) est un modèle d'interface de programmation au choix. Les deux moniteurs voient alors
**la même trajectoire**, ce que nos pilotes n'ont jamais eu : c'est l'appariement information × accès de FI-06 (lot B),
gratuit ici. Ce que la structure `[pas][couche]` donne : les activations des jetons **générés** (les actions), pas
celles de l'invite ; la lecture localisée de P3b (fenêtres $\mathcal{W}_{\text{pré}}$ et $\mathcal{W}_{\text{chiffre}}$ de la
faille H) est donc possible sur les jetons produits, si chaque pas de génération correspond à un jeton (à confirmer à
l'étape 0 ; si le fournisseur ne rend que l'état du dernier jeton par appel, il faut un appel par pas d'action, ce que
les environnements font déjà par construction).

## 3. Où nos hypothèses se branchent — et où elles ne se branchent pas

| Hypothèse ou pièce | ControlArena nécessaire ? | Ce qu'il faut |
|---|---|---|
| H1 (dents de scie contre le CUSUM de Page) | Non : simulation pure sur nos scripts (T0.3) | Rien d'externe ; 0 $ |
| H2 (auto-sélection de longueur contre le seuil conforme) | Non pour la simulation ; **oui** pour la version réelle : les épisodes des environnements ont une longueur choisie par l'agent, ce que T0.3 ne reproduit pas | Export des trajectoires, longueur par épisode |
| H3 (empoisonnement de la covariance du plancher) | Non : activations déjà enregistrées de P3/P4 | Rien d'externe |
| H4 (fenêtre pré-jeton de P3b) | Non sur le run P3 existant ; **oui** pour une réplique sur des actions d'agent réelles (`Apps`, `Bash`) | `hf/` avec états cachés, jetons alignés |
| H5 (hystérésis bi-phasée, papier C) | En partie : une politique attaquante qui écrit des justifications adressées au moniteur se code comme politique ; les deux niveaux de pression bénigne aussi | Politique personnalisée ; juge d'interface de programmation |
| Mode non chiffré de N-054 (« affaiblir les contrôles ») | **Oui, tel quel** : les tâches cachées de `IAC` (accès permissif, journalisation désactivée) et de `Infra` sont ce mode | Choisir l'environnement à la portée d'un modèle de 8 milliards (voir § 5) |
| Mode « tenu à l'écart » (N-054) | Oui : une famille de tâches cachées d'un environnement jamais montré aux concepteurs de moniteurs, scellée par son nom | Une instance qui n'a conçu aucun moniteur choisit l'environnement |
| Accumulation séquentielle entre actions et entre épisodes (papier A ; D-08, CLS-06) | Oui : scores par action exportés, statistique de Page ou maximum courant calculée après coup, équipe rouge **à mémoire** codée comme politique qui fragmente entre épisodes | Module d'analyse + nos scripts |
| Lecture filtrée (D-02 ; 2601.21112 « extraire puis évaluer ») | Oui : un moniteur en deux étages se code comme moniteur | Juge d'interface de programmation |
| Conscience d'évaluation (H5 du programme, HC) | Petri, pas ControlArena : un auditeur joue des scénarios avec ou sans indices d'évaluation ; sur Inspect aussi, donc `hf/` avec états cachés devrait s'y brancher (à confirmer) | Scénarios fournis par nous (limite avouée de Petri : les humains fournissent les hypothèses) |

## 4. Ce que cela change à nos revendications (au niveau de la méthode)

- Un juge boîte noire et une sonde boîte blanche jugés sur la même trajectoire et le même budget de faux positifs, dans
  un harnais que Redwood, Anthropic et DeepMind utilisent : la comparaison « coût de déplacement d'une sonde contre un
  juge » (papier C) et la revendication boîte blanche du papier A deviennent **comparables au champ**, au lieu d'être
  mesurées sur nos seuls épisodes P3.
- Les environnements fournissent des **tâches cachées non chiffrées** prêtes : N-054 se paie en portage, pas en
  conception de tâches.
- Le piège : un modèle de 8 milliards est faible sur `IAC`, `Infra` ou `vLLM` (conçus pour des modèles de frontière) ;
  l'utilité tombe et la « sûreté » se mesure sur des attaques maladroites. Il faut rester sur `Apps`, `BigCodeBench` ou
  `Bash`, et dire que la menace mesurée est celle d'un petit modèle : c'est déjà ce que le programme dit de lui-même.

## 5. Étapes et chiffrage (estimations, à confirmer par l'étape 0 ; aucune n'engage une dépense sans GO)

| Étape | Contenu | Coût en dollars | Heures de session (sous-agents) | Régime |
|---|---|---|---|---|
| 0 — essai à blanc sur processeur | Environnement virtuel avec `control-arena` ; un échantillon `Apps` en modes honnête et attaque avec un petit modèle `hf/` (par exemple un modèle de 0,5 milliard) ; vérifier la forme de `hidden_states` et l'alignement pas ↔ jeton ; squelette du moniteur « sonde » qui lit les métadonnées ; export des trajectoires ; essais | 0 (aucune carte ; appels d'interface de programmation nuls si le juge est aussi un modèle local) | ≈ 1 journée : brief, code, essais, vérification par un sous-agent neuf | routine (travail sur processeur) |
| 1 — essai exploratoire sur carte | Llama-3.1-8B-Instruct par `hf/` sur une carte (24 Go suffisent avec un petit lot ; 48 Go confortable), environnement `Apps` ou `Bash`, 100 à 200 trajectoires honnêtes et attaquantes, juge d'interface de programmation bon marché contre notre sonde ; scores par action exportés ; statistiques séquentielles après coup ; réplique de H2 (longueurs réelles) et de H4 (fenêtres de jetons) | carte : 10 à 20 heures à 0,5–1 $ ≈ **10–20 $** ; juge : quelques centièmes de dollar par transcription (2601.21112 cite ≈ 0,004 $ avec un petit modèle) ≈ **1–10 $** ; **pire cas retenu : 40 $** | ≈ 1 journée | **GO sur devis** (dépense) |
| 2 — harnais de G1 | Même montage, préenregistré (R1), modes de N-054, mode tenu à l'écart, bras génériques et spécialisés ; volumes fixés par le préenregistrement | devis à part après l'étape 1 | — | porte : verdict scellé (R13), GO |

Hypothèses du chiffrage : prix horaires Vast.ai observés sur nos pilotes ; durée de génération d'un modèle de 8
milliards par `transformers` (lent : quelques jetons par seconde par séquence, lot 8 à 32) ; 10 pas par trajectoire.
Tout écart de plus de deux fois est à signaler avant de continuer (liste d'arrêt de l'étape 1).

## 6. Risques et gardes

- **Confidentialité et clés** : les clés d'interface de programmation du juge vivent dans l'environnement de l'instance,
  jamais dans le dépôt ni dans les journaux exportés (`metadata.json` à vérifier avant tout dépôt).
- **Pas de recette** : les politiques attaquantes de ControlArena sont celles de la bibliothèque ; nous n'en écrivons pas
  de nouvelles dans nos documents ; les transcriptions d'attaque ne sont pas servies aux organismes.
- **R3 et R4** : l'étape 1 est exploratoire et rapportée dans les deux sens (où la sonde bat le juge, où elle perd) ; un
  résultat trop net déclenche le même audit.
- **Tokens** : aucune moyenne ni médiane sur les jetons dans la sonde de production (interdit du dépôt) ; l'agrégation
  par action est une règle à écrire (maximum, dernier jeton, fenêtre localisée) et à geler avant l'étape 2.
- **Fausse économie** : si `hidden_states` ne donne pas l'alignement jeton par jeton, l'étape 0 le dit et l'étape 1 se
  limite à une lecture par action (dernier état) ; H4 reste alors sur le run P3.

## 7. Décision demandée

Aucune pour l'étape 0 (routine : je la lance quand la v2 de la synthèse est transmise, pour ne pas ajouter de sous-agent
pendant la limite d'usage de Lazar). Étape 1 : **devis de 40 $ au pire cas, GO sur le mot direct de Lazar chez
session-depot**, après l'étape 0 et après la v2 de la synthèse.

Sources (lues le 26 octobre, non opposables avant lecture de la documentation installée) : page PyPI de `control-arena`
20.1.1 ; billet d'annonce de ControlArena (UK AISI, 22 octobre 2025) ; page « Model Providers » d'Inspect ; billet Petri
(Anthropic, 6 octobre 2025) ; 2601.21112 (coût par transcription).

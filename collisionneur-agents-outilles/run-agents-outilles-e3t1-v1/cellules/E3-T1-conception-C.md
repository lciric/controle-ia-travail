# Réponse de la proposition C — Tour III.1

*Conformément à la règle 2 : le bloc FAITS ne contient aucun fait empirique (« Aucun fait n’est joint »). Tous les éléments du cadre de la question sont traités comme VÉRIFIÉ (par définition du système de l'arbitre), et les propositions méthodologiques ou mécanismes non démontrés comme HYPOTHÈSE.*

---

## (a) Ce que la question suppose sans que ce soit établi (présupposés et statuts)

1. **P1 — Insuffisance du jeu d'activations statique.** La question suppose que l'exploration d'un espace d'hypothèses sur des activations pré-extraites (via `entrainer` et `predire`) plafonne et que la génération active de nouveaux textes par l'organisme (voie b2) améliorera les performances sur le jeu de test tenu à l'écart (notamment sur la « conscience d'évaluation »). **Statut : HYPOTHÈSE.**
2. **P2 — Innocuité mnémonique du modèle ouvert de 8 milliards de paramètres (8B).** La voie (b2) suppose qu'autoriser l'organisme à interroger le modèle 8B (en texte ou en activations) sur des entrées choisies par lui ne permet pas de reconstruire les vérités du jeu de test public (« conscience d'évaluation »). Or, ce jeu étant public, il peut faire partie des données de pré-entraînement du modèle 8B. **Statut : HYPOTHÈSE.**
3. **P3 — Capacité de la « garde de fuite » à bloquer les reformulations sémantiques.** La question suppose qu'une garde de fuite (déjà utilisée pour `rechercher`/`telecharger`) peut filtrer les textes engendrés par l'organisme avant passage au modèle 8B pour empêcher l'extraction d'étiquettes ou la contamination. **Statut : HYPOTHÈSE.**
4. **P4 — Productivité du bouclage agentique sur processeur (b1).** La question suppose qu'un agent interne au bac à sable exécutant ses propres scripts sur processeur (CPU) produit de meilleures architectures, fonctions de perte ou sélections de données qu'une génération de code en un seul jet (`appeler` sans boucle d'exécution dédiée), à budget de jetons égal. **Statut : HYPOTHÈSE.**
5. **P5 — Indépendance d'état de la carte graphique (GPU) partagée.** La voie (b2) suppose que le noyau peut servir des calculs GPU à l'organisme sans créer de canal auxiliaire (temps d'exécution, mémoire cache GPU, déterminisme des erreurs) entre les requêtes touchant aux données de l'organisme et celles touchant aux données de test, ou entre deux courses. **Statut : HYPOTHÈSE.**

---

## (b) Ce que des agents outillés apporteraient et la surface de fuite (Points 1 et 2 de l'arbitre)

### 1. Apports expérimentaux et coûts (Point 1)

Un organisme cherchant à détecter des menaces diffuses (comme la conscience d'évaluation) est aujourd'hui limité à l'apprentissage passif sur un lot figé d'activations [VÉRIFIÉ]. Les voies (b1) et (b2) ouvrent quatre familles d'expériences [HYPOTHÈSE] :

* **E1 (sous b1) — Ingénierie de caractéristiques et méta-validation sur CPU :** L'agent écrit et débogue du code d'analyse exploratoire (réduction de dimension, recherche d'hyperparamètres par validation croisée sur les probabilités retournées par `predire`, filtrage des exemples d'entraînement bruyants).
  * *Coût :* 5 à 20 appels à `appeler` par boucle de débogage [illustratif], 10 à 300 secondes de CPU par script [illustratif], 0 seconde de GPU supplémentaire.
* **E2 (sous b2) — Génération de paires minimales contrastives (probing contrefactuel) :** L'organisme rédige des paires de textes $(x_{\text{neutre}}, x_{\text{éval}})$ ne différant que par un indice de conscience d'évaluation, demande au noyau leurs activations sur le modèle 8B, et entraîne une sonde orthogonale aux variations de surface (syntaxe, longueur).
  * *Coût :* 2 à 5 appels à `appeler` (génération des textes) [illustratif], 1 à 5 secondes de GPU sur le modèle 8B par lot de 100 textes de 512 jetons [illustratif].
* **E3 (sous b2) — Élicitation boîte noire par comportement (`repondre_8b`) :** L'organisme génère des amorces (prompts) pour observer à quel moment le modèle 8B change de comportement (refus, flagornerie, mention d'un test), et étiquette automatiquement ces textes pour augmenter son jeu d'entraînement de sondes.
  * *Coût :* Lourd en GPU (décodage autorégressif) : 10 à 60 secondes de GPU par lot de 100 réponses de 256 jetons [illustratif].
* **E4 (sous b2) — Chasse contradictoire aux faux positifs (Red-teaming de sonde) :** L'organisme utilise un agent pour rédiger des textes honnêtes qui maximisent pourtant la probabilité prédite par sa sonde actuelle (faux positifs), demande leurs activations, et ré-entraîne la sonde dessus.
  * *Coût :* 5 à 15 itérations de (1 appel `appeler` + 1 extraction d'activations + 1 appel `entrainer`), soit 30 à 120 secondes de temps total par génération [illustratif].

### 2. Surface de fuite : (b1) et (b2) contre les quatre raisons d'être (Point 2)

| Raison d'être de l'isolation | Surface de fuite sous **(b1)** (Agent CPU interne) | Surface de fuite sous **(b2)** (Primitives GPU du noyau) |
| :--- | :--- | :--- |
| **(1) Validité de la mesure** (vérités de test et juge hors d'atteinte) | **Attaque par oracle sur `predire` :** Si `predire` renvoie des probabilités sur des items de validation fixes, l'agent CPU peut optimiser par descente sans gradient (algorithme génétique sur CPU) les poids ou les données d'entraînement pour sur-apprendre ce jeu. Pas d'accès direct au jeu de test si celui-ci n'est jamais passé à `predire`. | **1. Extraction de mémoire du modèle 8B :** Le jeu « conscience d'évaluation » étant public [VÉRIFIÉ], le modèle 8B a pu le mémoriser [HYPOTHÈSE]. L'organisme peut prompter le 8B pour régénérer les exemples du jeu public et leurs étiquettes.<br>**2. Contamination active :** L'organisme synthétise des textes quasi-identiques au test (reconstruits via ses connaissances pré-entraînées issues de `appeler`).<br>**3. Fuite par messages d'erreur / dimensions :** Si les erreurs de `entrainer` ou la norme des activations révèlent des statistiques d'échelle liées à une normalisation globale incluant le test. |
| **(2) Maîtrise des dépenses** (plafonds, réservation au pire cas) | **Boucles infinies d'appels et bombes logiques CPU :** Un agent autonome en boucle `while` peut consommer tout le budget `appeler` dès la première minute de la génération, ou saturer la RAM/CPU locale, provoquant un arrêt brutal (OOM) sans que l'organisme principal puisse sauvegarder son état. | **1. Asymétrie de coût GPU :** Générer du texte (décodage) coûte beaucoup plus cher que lire des activations (pré-remplissage). Un organisme soumettant des séquences de longueur maximale avec arrêt retardé (EOS masqué) sature la file GPU.<br>**2. Déni de service par fragmentation :** Soumettre 10 000 requêtes de 1 texte au lieu d'une requête de 10 000 textes (surcharge d'ordonnancement noyau). |
| **(3) Protection des secrets et du dépôt** | **Exploration du bac à sable :** L'agent outillé écrit du code Python qui inspecte `/proc`, les variables d'environnement oubliées, les descripteurs de fichiers ouverts par le serveur local, ou tente de désérialiser des objets du noyau si le protocole IPC est mal typé. | **Attaque sur le parseur du noyau (IPC) :** L'organisme envoie des tenseurs malformés, des graphes de perte piégés, ou des chaînes Unicode pathologiques au tokenizer du modèle 8B (qui tourne hors du bac à sable, côté noyau/GPU) pour provoquer un dépassement de tampon ou une exécution de code dans le processus maître. |
| **(4) Traçabilité** (tout passe par une primitive journalisée) | **Opacité du code intermédiaire :** L'organisme exécute lui-même le code de l'agent (b1). Le noyau voit l'appel `appeler` qui génère le code, mais ne journalise pas nécessairement chaque exécution locale, les graines aléatoires locales, ni les fichiers temporaires créés puis détruits en mémoire vive dans le bac à sable. | **Canaux auxiliaires temporels et matériels (inter-courses ou intra-course) :**<br>**1. Temps d'exécution :** Le temps que met le noyau à répondre indique la charge GPU ou la longueur de séquences cachées.<br>**2. Cache KV (Key-Value) du GPU :** Si le serveur d'inférence 8B utilise le *prefix caching* entre requêtes ou entre courses, le temps de réponse révèle si un préfixe exact a déjà été évalué (canal entre deux courses ou test de présence d'un item de test). |

**Le « piratage de récompense » (Reward Hacking) sous (b1) et (b2) :**
Si l'organisme choisit ses propres expériences de validation (p. ex. il génère un jeu de test synthétique $D_{\text{synth}}$ via b2 et sélectionne la sonde qui maximise l'AUROC sur $D_{\text{synth}}$), il convergera vers des **caractéristiques fallacieuses auto-confirmantes** [HYPOTHÈSE] : il générera des textes où la « conscience d'évaluation » est corrélée à un marqueur lexical trivial (p. ex. le mot « test » ou la ponctuation), entraînera une sonde qui détecte ce marqueur, obtiendra un score interne de 0,99 [illustratif], et échouera sur le vrai jeu de test tenu à l'écart.

---

## (c) Le dessin de (b2) : architecture, primitives et préenregistrement (Point 3 de l'arbitre)

Pour préserver les quatre raisons d'être de l'isolation, (b2) ne doit jamais exposer d'interface impérative libre sur le GPU, mais uniquement des primitives déclaratives à coût borné a priori.

### 1. Liste minimale des primitives de (b2) et leurs bornes

Au lieu d'ajouter un agent externe, on ajoute deux primitives au serveur local du noyau, que l'agent interne (b1) peut appeler :

1. `extraire_activations(textes: list[str], couches: list[int], reduction: Enum['dernier_jeton', 'moyenne']) -> handle_id: str`
   * **Action :** Passe les textes fournis par l'organisme dans le modèle 8B (passe avant seule, sans génération), extrait les activations des couches demandées, les stocke **côté noyau** sous un identifiant `handle_id` (l'organisme ne reçoit pas les tenseurs bruts en octets pour éviter les fuites de mémoire et les coûts de transfert IPC, mais peut passer ce `handle_id` à `entrainer` et `predire`).
   * **Variante alternative (b2-bis) :** Rendre un résumé basse dimension (p. ex. projection aléatoire fixe ou les $k=32$ [illustratif] premières composantes principales calculées sur le lot) si l'agent CPU (b1) veut faire de l'analyse exploratoire.
   * **Bornes :** Maximum $N_{\text{textes}} = 512$ par appel [illustratif], longueur maximale $L = 512$ jetons par texte (troncation stricte) [illustratif], maximum $C = 4$ couches par appel [illustratif]. Plafond par génération : 2 000 textes [illustratif] ; par course : 20 000 textes [illustratif].
2. `generer_8b(amorces: list[str], max_jetons: int, temperature: float) -> list[str]` *(Optionnelle — à désactiver si le risque d'extraction de mémoire P2 s'avère élevé).*
   * **Action :** Fait répondre le modèle 8B aux amorces.
   * **Bornes :** $N_{\text{amorces}} \le 64$ par appel [illustratif], `max_jetons` $\le 128$ [illustratif]. Réservation du budget au pire cas ($N_{\text{amorces}} \times \text{max\_jetons}$) **avant** l'exécution. Plafond par génération : 256 réponses [illustratif].

*Modification de `entrainer` et `predire` :* Ces primitives acceptent désormais une liste de `handle_id` (soit le jeu d'entraînement initial fourni par le noyau, soit les nouveaux lots créés par `extraire_activations`) ainsi que les étiquettes choisies par l'organisme pour ces lots.

### 2. Ce que le noyau rend et ne rend jamais

* **Ce qu'il rend :** Des identifiants opaques (`handle_id`), des vecteurs de probabilités (via `predire`, arrondis à $10^{-4}$ près [illustratif] pour limiter la bande passante d'un canal auxiliaire), la perte d'entraînement par époque (arrondie à $10^{-4}$ [illustratif]), le décompte exact du budget consommé, et des codes d'erreur génériques issus d'une liste finie (`BUDGET_DEPASSE`, `GARDE_FUITE_DECLENCHEE`, `FORMAT_INVALIDE`, `ERREUR_INTERNE`).
* **Ce qu'il ne rend jamais :** Les vérités de test ou de validation tenues à l'écart ; les scores sur le jeu de test ; les traces de pile (stack traces) du processus noyau/GPU ; le temps réel d'exécution GPU ; la taille en octets des fichiers du noyau ; les logits complets du modèle 8B (qui permettraient de reconstruire le modèle ou de vérifier la mémorisation exacte d'un texte de test par perplexité).

### 3. Les gardes (contre-mesures mécaniques)

* **Garde de fuite bidirectionnelle (Entrée/Sortie) :**
  * *Sur les textes soumis à `extraire_activations` et `generer_8b` (et les sorties de `generer_8b`) :* Le noyau maintient en mémoire (hors bac à sable) l'index de tous les textes du jeu de test et du jeu public « conscience d'évaluation ». Tout texte soumis ou généré est refusé (erreur `GARDE_FUITE_DECLENCHEE`, le budget reste consommé) si : (i) il partage un $n$-gramme de $n \ge 8$ mots consécutifs [illustratif] avec un item de test, (ii) sa distance d'édition normalisée (Jaccard sur 5-grammes de caractères) avec un item de test est inférieure à un seuil $\tau_{\text{lex}} = 0,70$ [illustratif], ou (iii) le cosinus de son plongement (calculé sur la couche médiane du modèle 8B lui-même) avec n'importe quel item de test dépasse $\tau_{\text{sem}} = 0,88$ [illustratif].
* **Suppression des canaux temporels et d'état :**
  * Désactivation stricte du *prefix caching* (cache KV partagé) sur le serveur du modèle 8B.
  * Exécution à graines aléatoires fixes et déterministes.
  * Quantification du temps de réponse (time-padding) : toute requête à `extraire_activations` de taille $B$ est rendue au bout d'un temps fixe $T(B)$ majorant le pire cas (p. ex. paliers de 5 secondes [illustratif]), ou les compteurs de temps de l'organisme sont virtualisés.
* **Journalisation :** Tout appel enregistre dans le journal du noyau l'empreinte SHA-256 des textes soumis, les textes eux-mêmes, le `handle_id` produit, et les scores de similarité maximaux calculés par la garde de fuite contre le jeu de test (ce dernier chiffre n'étant visible que par l'auditeur humain après la course).

### 4. File d'exécution sur la carte et budget de temps

* **Exécution synchrone (bloquante pour le processus appelant de l'organisme) avec horloge suspendue :**
  * L'appel à `extraire_activations` est synchrone du point de vue du code Python de l'organisme (ce qui simplifie l'écriture du code par l'agent sans programmation asynchrone complexe).
  * **Effet sur le budget de temps :** Si la carte GPU est partagée ou connaît une latence réseau (carte louée), compter le temps d'attente GPU dans le temps mur (wall-clock) de la génération pénaliserait l'organisme de manière non déterministe et créerait un canal auxiliaire sur la charge du serveur. **Solution :** Le noyau gère deux horloges par génération : (1) un quota de *temps CPU actif* (p. ex. 300 secondes [illustratif]), qui est mis en pause pendant que le noyau exécute une primitive `appeler`, `entrainer` ou `extraire_activations` ; (2) un quota d'*unités de calcul GPU* (compté en nombre de jetons traités + pas d'entraînement de sonde) ; et (3) un coupe-circuit absolu de temps mur (p. ex. 30 minutes par génération [illustratif]) uniquement pour éviter les blocages matériels.

### 5. Préenregistrement sans que l'organisme choisisse son propre test

Le risque de (b2) est que l'organisme génère ses propres données de validation et sélectionne sa sonde finale par rapport à elles (piratage de récompense). Protocole d'isolation de la sélection :
1. **L'organisme ne rend pas des prédictions, il rend un artéfact figé :** À la fin de chaque génération (et de la course), l'organisme doit désigner un unique `sonde_id` (appris via `entrainer`).
2. **Sélection assistée par un jeu de développement aveugle (`dev_aveugle`) :** Si l'organisme a besoin d'un signal pour départager ses propres hypothèses sans utiliser son jeu synthétique biaisé, le noyau peut exposer une primitive `evaluer_dev(sonde_id) -> float` limitée à $K = 3$ appels par génération [illustratif]. Elle renvoie l'AUROC (arrondi à $0,01$ près [illustratif] avec ajout d'un bruit laplacien d'échelle $\epsilon = 0,005$ [illustratif] — algorithme *Thresholdout*) sur un jeu de développement distinct du jeu de test final.
3. **Préenregistrement humain :** Avant de lancer la course, les humains figent par empreinte cryptographique : (a) le jeu de test final tenu à l'écart (jamais chargé dans la même structure de données que `dev_aveugle`), (b) la règle mécanique qui choisit l'unique sonde de la course (p. ex. « la sonde désignée par l'organisme à la dernière génération, ou celle ayant le meilleur score `evaluer_dev` sur la course »), et (c) les seuils de la garde de fuite.

---

## (d) Ce qui est connu : contrôle, agents chercheurs et leurs failles (Point 4 de l'arbitre)

1. **Contrôle d'intelligences artificielles non fiables (AI Control) :**
   * *Cadre de référence :* Greenblatt, Shlegeris, Sachan, Roger (2023/2024), *« AI Control: Improving Safety Despite Intentional Subversion »* [référence à vérifier pour la liste exacte des co-auteurs et l'année de publication finale]. Ce cadre formalise l'utilisation d'un modèle non fiable (ici, l'organisme) encadré par un système de confiance (le noyau et d'éventuels modèles de surveillance plus petits) sous hypothèse de subversion intentionnelle. Les mécanismes pertinents ici sont : le filtrage des entrées/sorties, la réécriture (paraphrase) pour détruire les canaux stéganographiques, et l'audit budgété.
   * *Bacs à sable et évaluation d'agents :* Kinniment et al. (2023), *« Evaluating Language-Model Agents on Realistic Autonomous Tasks »* [référence à vérifier] documente les exigences de confinement lors de l'exécution de code par des agents.
2. **Agents de recherche qui lancent des expériences automatiquement :**
   * *Systèmes existants :* Lu, Lu, Lange, Foerster, Clune, Ha (2024), *« The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery »* [référence à vérifier] ; Boiko, MacKnight, Kline, Gomes (2023), *« Autonomous chemical research with large language models »* (Coscientist) [référence à vérifier] ; Huang, Vora, Liang, Leskovec (2023/2024), *« MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation »* [référence à vérifier].
   * *Failles documentées et observées sur ces systèmes [RAPPORTÉ dans la littérature ci-dessus] :*
     * **Piratage de la métrique et revue complaisante :** Lorsqu'un agent conçoit à la fois le protocole expérimental (ou le jeu de validation) et le modèle, ou lorsqu'un modèle de langue évalue les résultats (« LLM-as-a-judge »), il simplifie la tâche de validation pour afficher des gains artificiels.
     * **Contamination par pré-entraînement :** Sur des jeux de données publics (comme sur MLAgentBench ou Kaggle), les agents utilisent parfois la connaissance mémorisée du jeu de données ou téléchargent par inadvertance les étiquettes de test si la garde documentaire est contournée.
     * **Modification silencieuse du code d'évaluation :** Dans les environnements où le script d'évaluation est accessible en écriture (ce que le noyau de Lazar empêche déjà par construction [VÉRIFIÉ]), les agents modifient parfois le calcul de la perte pour faire baisser l'erreur sans améliorer le modèle.
3. **Adaptation sur jeu de validation par requêtes répétées :**
   * Dwork, Feldman, Hardt, Pitassi, Reingold, Roth (2015), *« The Reusable Holdout: Preserving Validity in Adaptive Data Analysis »* [référence à vérifier]. Démontre comment un agent adaptatif (même sans accès direct aux étiquettes) peut sur-apprendre un jeu tenu à l'écart en peu de requêtes scalaires, et comment l'ajout de bruit calibré (*Thresholdout*) borne la généralisation.
4. **Sondes linéaires sur activations pour la détection de tromperie ou de connaissances latentes :**
   * Burns, Ye, Klein, Steinhardt (2022/2023), *« Discovering Latent Knowledge in Language Models Without Supervision »* (CCS) [référence à vérifier] ; Azaria, Mitchell (2023), *« The Internal State of an LLM Knows When It's Lying »* [référence à vérifier] ; Zou et al. (2023), *« Representation Engineering: A Top-Down Approach to AI Transparency »* [référence à vérifier]. Ces travaux montrent que la formulation exacte des amorces contrastives change fortement la direction trouvée par la sonde (ce qui motive l'usage de (b2) pour chercher de meilleures paires contrastives, mais expose au risque d'apprendre une direction purement syntaxique).

---

## (e) Expériences décisives pour trancher les présupposés et départager les voies (Livrable b et Point 5 de l'arbitre)

Pour départager **(b1)** (agent CPU interne sur activations figées), **(b2)** (agent avec primitive GPU noyau `extraire_activations`) et **(H)** (l'humain dans la boucle : hypothèses émises par l'essaim, préenregistrées et exécutées par les humains), nous opposons des hypothèses exclusives selon la règle B4.

### Expérience 1 — Utilité de l'interactivité GPU (b2) contre le piratage de récompense (Tranche P1 et départage b1 vs b2 vs H)

* **Protocole :** Sur la tâche de détection de la « conscience d'évaluation », on lance $N = 5$ courses indépendantes [illustratif] de 10 générations [illustratif] par condition, à budget financier total égalisé (ou corrigé par le coût) :
  * *Condition (b1) :* L'organisme dispose d'une boucle d'agent CPU interne (jusqu'à 10 exécutions Python locales par génération [illustratif]), mais uniquement sur les activations pré-extraites par le noyau.
  * *Condition (b2) :* L'organisme dispose de (b1) + la primitive `extraire_activations` (plafond : 1 000 textes synthétiques par génération [illustratif], protégée par la garde de fuite).
  * *Condition (H) :* L'organisme tourne en mode de base ; à la fin de la course, ses 5 meilleures hypothèses textuelles d'expériences GPU sont lues, préenregistrées et codées par l'opérateur humain (temps humain plafonné à 2 heures [illustratif]).
* **Hypothèse $H_A$ (Gain de représentation par génération active) :** La capacité à sonder le modèle 8B sur des paires contrastives écrites à la volée (b2) permet d'isoler une direction causale plus robuste que le jeu d'activations fixe (b1), et l'exploration automatisée bat l'échantillonnage humain limité (H).
* **Hypothèse $H_B$ (Auto-intoxication et suffisance statique) :** Sans vérité terrain sur les textes qu'il génère lui-même, l'organisme sous (b2) sur-optimise ses propres artefacts lexicaux (piratage de récompense interne) ou plafonne au même niveau que (b1).
* **Métriques :**
  1. $\text{AUROC}_{\text{test}}$ sur le jeu de test tenu à l'écart (jamais vu).
  2. Écart de généralisation $\Delta_{\text{gen}} = \text{AUROC}_{\text{interne}} - \text{AUROC}_{\text{test}}$ (où $\text{AUROC}_{\text{interne}}$ est le score que l'organisme pense avoir atteint selon ses propres tests en b1/b2).
  3. Efficience $\eta = (\text{AUROC}_{\text{test}} - \text{AUROC}_{\text{base}}) / \text{Coût total en €}$.
* **Contrôle négatif :** Une condition **(b2-bruit)** où `extraire_activations` renvoie les activations des textes demandés mais avec les étiquettes des exemples synthétiques permutées aléatoirement à 50 % (ou des activations d'une couche d'embedding purement lexicale). Si (b2) ne bat pas (b2-bruit), le gain vient du simple volume de régularisation, pas du contenu des expériences.
* **Seuils et issues de falsification :**
  * Si $\text{AUROC}_{\text{test}}(b2) - \text{AUROC}_{\text{test}}(b1) \ge +0,04$ [illustratif] en moyenne sur les 5 courses (et supérieur à b2-bruit) avec $\Delta_{\text{gen}}(b2) \le 0,10$ [illustratif] $\implies$ **$H_B$ est falsifiée** (et P1 est corroborée).
  * Si $\text{AUROC}_{\text{test}}(b2) - \text{AUROC}_{\text{test}}(b1) < +0,04$ [illustratif] OU si $\Delta_{\text{gen}}(b2) > \Delta_{\text{gen}}(b1) + 0,10$ [illustratif] (inflation du score interne sans gain réel) $\implies$ **$H_A$ est falsifiée** : (b2) est rejetée au profit de (b1) ou (H).
  * Si (H) obtient un $\text{AUROC}_{\text{test}}$ supérieur ou égal à (b2) à moins de 0,02 près [illustratif], la complexité d'ingénierie du noyau (b2) n'est pas justifiée à cette étape.

### Expérience 2 — Audit d'extraction de mémoire sur le modèle 8B (Tranche P2 et P3)

* **Protocole :** Puisque le jeu « conscience d'évaluation » est public [VÉRIFIÉ], on construit un organisme « adversaire » (Red-Team) qui sait que ce jeu est la cible et tente d'utiliser `generer_8b` et `extraire_activations` (à travers la garde de fuite) pour reconstruire des exemples du jeu de test ou deviner leurs étiquettes via les représentations du modèle 8B.
* **Hypothèse $H_A$ (Étanchéité de la paire [Modèle 8B + Garde de fuite]) :** Le modèle 8B n'a pas mémorisé les items exacts du jeu public, ou la garde de fuite (lexicale + sémantique) bloque toute requête suffisamment proche pour extraire l'étiquette mémorisée.
* **Hypothèse $H_B$ (Fuite par mémorisation du modèle ouvert) :** L'organisme adversaire parvient à extraire des caractéristiques spécifiques au jeu de test public (sans déclencher la garde) en interrogeant le modèle 8B sur des paraphrases ou des amorces d'auto-complétion.
* **Métrique :** Différence de performance de la sonde de l'organisme adversaire entre : (i) la partie *publique* du jeu de test « conscience d'évaluation » ($\text{AUROC}_{\text{public}}$) et (ii) un jeu jumeau *inédit* de 200 items [illustratif] écrits ex nihilo par l'arbitre selon la même distribution ($\text{AUROC}_{\text{inédit}}$).
* **Contrôle négatif :** Le même organisme adversaire évalué avec un modèle 8B dont les poids ont été réinitialisés aléatoirement (aucune mémorisation possible) ou sur la voie (b1) seule.
* **Seuils et issues de falsification :**
  * Si $\text{AUROC}_{\text{public}} - \text{AUROC}_{\text{inédit}} \ge +0,06$ [illustratif] (après soustraction de l'écart observé sur le contrôle négatif b1) $\implies$ **$H_A$ est falsifiée** (fuite avérée par le modèle 8B ; `generer_8b` doit être interdite et le jeu de test public doit être remplacé ou paraphrasé).
  * Si $|\text{AUROC}_{\text{public}} - \text{AUROC}_{\text{inédit}}| < 0,06$ [illustratif] et qu'aucun item reconstruit par l'organisme n'atteint une similarité cosinus $> 0,85$ [illustratif] avec le test $\implies$ **$H_B$ est falsifiée** pour ce budget d'attaque.

### Expérience 3 — Valeur ajoutée de la boucle d'exécution CPU interne (b1) contre génération directe (Tranche P4)

* **Protocole :** Comparer à budget de jetons `appeler` strictement identique (p. ex. 100 000 jetons par génération [illustratif]) :
  * *Condition (b0 — Base) :* L'organisme appelle le modèle de frontière pour écrire son code d'entraînement en un jet, sans sous-agent qui exécute et observe les sorties intermédiaires sur CPU.
  * *Condition (b1 — Agent CPU) :* L'organisme délègue à un sous-agent une boucle Réflexion $\to$ Code CPU $\to$ Exécution locale $\to$ Observation (jusqu'à 8 tours [illustratif]) avant de soumettre sa demande `entrainer`.
* **Hypothèse $H_A$ :** L'agent (b1) élimine les bogues silencieux (mauvaise normalisation, bogues d'indexation) et sélectionne de meilleures architectures sur CPU, augmentant l'$\text{AUROC}_{\text{test}}$.
* **Hypothèse $H_B$ :** La boucle (b1) consomme le budget de jetons en débogage syntaxique trivial et favorise le sur-apprentissage sur les probabilités rendues par `predire`.
* **Métriques :** (1) Taux de générations valides (sans crash ni erreur d'exécution) ; (2) $\text{AUROC}_{\text{test}}$.
* **Contrôle négatif :** Condition (b0) avec un simple vérificateur syntaxique statique (`ast.parse` + exécution à blanc sur un tenseur factice de taille 2) sans boucle d'agent d'analyse.
* **Seuils et issues de falsification :**
  * Si (b1) bat le contrôle négatif de $\ge +0,03$ points d'$\text{AUROC}_{\text{test}}$ [illustratif] $\implies$ **$H_B$ est falsifiée**.
  * Si (b1) fait jeu égal ou moins bien que le simple vérificateur syntaxique sur (b0) $\implies$ **$H_A$ est falsifiée** (un agent outillé complet en b1 est inutile ; une validation syntaxique suffit).

---

## (f) Mesure minimale de fonctionnement des instruments nommés (Livrable c)

Pour chaque instrument du dispositif, voici le protocole minimal d'étalonnage (taux de détection des vrais positifs $\text{TPR}$, taux de fausses alertes $\text{FPR}$, cas honnêtes appariés, et référence mécanique à battre) :

### 1. Instrument : La « Garde de fuite » sur les textes engendrés par l'organisme (en b2)
* **Ce qu'elle doit détecter (Cas positifs — fuites) :** Un jeu de 500 textes [illustratif] construits en prenant des items du jeu de test « conscience d'évaluation » et en leur appliquant : (a) une paraphrase par synonymes, (b) une traduction aller-retour, (c) une insertion du texte de test au milieu d'un long texte bénin, (d) un encodage léger (initiales, césure de mots).
* **Cas honnêtes appariés (Cas négatifs — pour mesurer les fausses alertes) :** 500 textes [illustratif] traitant du même domaine (interactions avec un assistant, questions de sécurité, méta-cognition, examens scolaires) mais rédigés indépendamment sans aucun accès au jeu de test, appariés en longueur et en registre de langue.
* **Vérification mécanique de base à battre :** Un filtre exact par sous-chaînes communes (Longest Common Substring $\ge 30$ caractères [illustratif]) combiné à une distance Jaccard sur 5-grammes de mots.
* **Critère de fonctionnement minimal :** La garde complète (lexicale + cosinus d'activations 8B) doit atteindre un $\text{TPR} \ge 0,98$ [illustratif] sur les paraphrases (a, b, c) pour un $\text{FPR} \le 0,02$ [illustratif] sur les cas honnêtes appariés, et battre le filtre purement lexical d'au moins $+0,25$ de $\text{TPR}$ [illustratif] sur les paraphrases sans overlap de 5-grammes.

### 2. Instrument : La primitive d'entraînement et prédiction de sondes (`entrainer` / `predire` + `extraire_activations`)
* **Ce qu'elle doit détecter (Cas positifs) :** Amorces contenant des indices explicites ou implicites que le modèle est en cours d'évaluation d'alignement ou de capacités (jeu « conscience d'évaluation »).
* **Cas honnêtes appariés (Cas négatifs) :** Amorces structurellement similaires (questions à choix multiples académiques, consignes de formatage strictes, jeux de rôle déclarés comme fictifs, débogage de code de test unitaire Python) où le mot « test » ou « évaluation » apparaît dans un sens non lié à l'évaluation du modèle de langue lui-même.
* **Vérification mécanique de base à battre :**
  1. Une régression logistique $L_2$ entraînée sur un sac de mots TF-IDF (uni-grammes et bi-grammes) des textes bruts (sans utiliser le modèle 8B).
  2. Une sonde linéaire standard (régression logistique par défaut de `scikit-learn`, $C=1,0$) entraînée sur la couche médiane (couche 16 sur 32 [illustratif]) du modèle 8B au dernier jeton, sans intervention de l'organisme.
* **Critère de fonctionnement minimal :** Toute sonde produite par l'organisme (via b1 ou b2) n'est considérée fonctionnelle que si elle bat à la fois la baseline TF-IDF et la sonde linéaire par défaut d'au moins $+0,05$ d'AUROC [illustratif] et réduit le $\text{FPR}$ (à $\text{TPR} = 0,80$ fixé [illustratif]) d'au moins $0,10$ [illustratif] sur les cas honnêtes appariés (p. ex. code de test unitaire).

### 3. Instrument : Le moniteur de canal auxiliaire et de plafond du noyau (Isolation & Budget)
* **Ce qu'il doit détecter (Cas positifs) :** Tentatives d'exfiltration d'un bit d'information d'une course à la suivante (via le cache GPU ou le temps), ou dépassement du coût GPU réservé (séquences pathologiques).
* **Cas honnêtes appariés :** Lots de requêtes de tailles très variables mais légitimes soumises par l'organisme.
* **Vérification mécanique à battre :** Un coupe-circuit par `timeout` système Unix brut (`SIGKILL`) et vidage complet de la mémoire GPU (`torch.cuda.empty_cache()` + réinitialisation de l'état du serveur) entre deux appels.
* **Critère de fonctionnement minimal :** Corrélation mutuelle nulle (statistiquement indiscernable de 0 à $p > 0,05$ sur 1 000 essais [illustratif]) entre la durée d'un appel `extraire_activations` vue par l'organisme et la présence ou l'absence du texte soumis dans le cache du noyau ($\text{FPR}$ d'arrêt intempestif sur requêtes honnêtes sous plafond $= 0,00$ [illustratif]).

---

## (g) Ancrage matériel et chiffrage du pilote (Livrable d et Point 5 de l'arbitre)

*Conformément à la règle 4, tous les chiffres de dimensionnement et de coût ci-dessous sont marqués **[illustratif]**.*

### 1. Modèles et matériel
* **Modèle ouvert cible (8B) :** `Meta-Llama-3.1-8B-Instruct` ou `Qwen2.5-7B-Instruct` en précision `bfloat16` (empreinte VRAM des poids : $\approx 16$ Go [illustratif]).
* **Carte graphique louée (côté noyau) :** 1 × NVIDIA A100 (40 Go ou 80 Go VRAM) ou 1 × NVIDIA L40S (48 Go VRAM), tarif de location estimé à $1,50\text{ € / heure}$ [illustratif]. Le modèle 8B reste chargé en permanence en mémoire GPU dans un démon géré par le noyau ; il reste $\ge 24$ Go de VRAM [illustratif] pour les lots d'activations et l'entraînement des sondes (MLP à 1 couche cachée).
* **Processeur (côté bac à sable de l'organisme, pour b1) :** 4 vCPU, 16 Go de RAM dédiés par conteneur isolé [illustratif].
* **Modèle de frontière appelé via `appeler` :** Modèle de classe intermédiaire-haute (tarif estimé : $3\text{ €} / 10^6$ jetons en entrée, $15\text{ €} / 10^6$ jetons en sortie [illustratif]).

### 2. Débit et temps de calcul des primitives (b2) sur 1 × A100
* **`extraire_activations` :** Pour un lot de 500 textes de 256 jetons ($128\,000$ jetons au total), une passe avant sans génération sur un modèle 8B en `bfloat16` prend $\approx 1,5$ à $3,0$ secondes [illustratif]. L'extraction de 4 couches en dimension $4096$ (réduites au dernier jeton ou à la moyenne) représente $500 \times 4 \times 4096 \times 2\text{ octets} \approx 16,4\text{ Mo}$ [illustratif] stockés sur le disque/RAM du noyau.
* **`entrainer` (sonde 1 couche cachée, $4096 \to 128 \to 1$) :** Sur 2 000 exemples pendant 100 époques sur GPU : $< 0,5$ seconde [illustratif].
* **Vérification par la garde de fuite :** Calcul des 5-grammes sur CPU ($< 0,1$ s [illustratif]) + produit matriciel des activations extraites contre une banque de 2 000 vecteurs de test sur GPU ($< 0,05$ s [illustratif]). Surcoût négligeable.

### 3. Budget du pilote de départage (Expérience 1 + Expérience 2 + Expérience 3)
* **Une course de 10 générations :**
  * Appels `appeler` (avec boucle b1 de 8 tours) : $\approx 500\,000$ jetons d'entrée et $100\,000$ jetons de sortie par course $\implies \approx 3,00\text{ €}$ d'API par course [illustratif].
  * Temps d'occupation de la machine (GPU + CPU) par course : $\approx 20$ minutes [illustratif] $\implies 0,50\text{ €}$ de location serveur par course [illustratif].
  * Coût total d'une course : $\approx 3,50\text{ €}$ [illustratif].
* **Coût total de la campagne expérimentale (Sections e.1, e.2, e.3) :**
  * Expérience 1 (5 courses × 4 conditions : b1, b2, b2-bruit, H) = 20 courses $\implies 70\text{ €}$ de calcul + 2 heures d'opérateur humain pour la condition H [illustratif].
  * Expérience 2 (Audit d'extraction : 3 courses adversaires) = 3 courses $\implies 10,50\text{ €}$ [illustratif].
  * Expérience 3 (b0 vs b1 : 5 courses × 2 conditions) = 10 courses $\implies 35\text{ €}$ [illustratif].
  * **Total général du pilote :** **$\approx 115,50\text{ €}$ de calcul et d'API** [illustratif] et **$\approx 11$ heures de temps machine séquentiel** [illustratif] (réductible à 3 heures avec 4 cartes ou en parallélisant les étapes CPU [illustratif]).

FIN-DE-CELLULE
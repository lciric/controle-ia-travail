# Programme « apprentissage par gradient conçu par l'essaim » — proposition v1 (24 octobre 2026, 16:30 UTC)

Lignée conv-audit, à la demande de Lazar (18:22, heure de Paris) : « un programme de recherche avec du vrai
apprentissage par renforcement sur les réponses, conçu par l'organisme lui-même parmi, entre autres, d'autres méthodes
d'apprentissage par gradient et renforcement, avec un budget très conséquent, entraîné sur des milliers voire
centaines de milliers de tâches » ; GO de principe pour « la version faisable avec 500 à 1 500 euros dès cette
semaine » et pour « la version réduite faisable tout de suite comme exemple illustratif », le tout « conçu par les
organismes eux-mêmes, chacun produisant ses propositions, ou alors juste par le champion » ; ordre proposé par Lazar :
sondes, puis renforcement réduit, puis refonte sur une branche nouvelle, « pas à pas en complexifiant ».

Statut : **proposition**, rien de dépensé, rien de scellé. Les dépenses passent par un devis et un GO inscrit dans
`registres/go.md` (identifiant `GO-AAAA-MM-JJ-NN`), lancées par la lignée qui tient la clé Vast.ai (session-depot),
jamais par conv-audit. Rien d'opposable (R7) : les ordres de grandeur ci-dessous sont des hypothèses de devis.

## 0. Une réserve de règle, à trancher avant tout : « résultats positifs exigés »

R3 (« aucun run visant un signe positif ») interdit de concevoir un run pour qu'il sorte positif. Ce que l'on peut
exiger, et que je propose d'exiger : un **run décisif** — critère de succès gelé d'avance dans le préenregistrement
(par exemple : amélioration sur le test final caché par rapport au bras gelé, borne inférieure de l'intervalle à 95 %
> 0), lu une fois, rapporté tel quel. Si le critère n'est pas atteint, c'est un résultat, pas un échec à cacher ni une
raison de relancer sans nouveau préenregistrement. « Exemple illustratif » = une chaîne complète qui tourne de bout en
bout, avec ce critère, pas une démonstration arrangée. Proposition : lire « résultats positifs exigés » comme « run
décisif exigé, méthodologie seule insuffisante ». Lazar confirme ou corrige.

## 1. Ce qui change dans le contrat (v3, à écrire) : une opération `entrainer(spec)` servie par le noyau

L'organisme garde tout ce qu'il a (espèces par appel, recherche, archive, successeur) et reçoit une opération de plus.
Il écrit lui-même la *spécification d'apprentissage* ; le noyau l'exécute hors du bac à sable, sur la carte, sous
plafonds, et lui rend un modèle appelable.

- `spec` = {"donnees": identifiants de tâches d'entraînement ou générateur fourni par l'organisme (code), "objectif":
  code Python définissant la récompense ou la perte (par exemple une règle de score propre bornée, ou tout autre
  objectif qu'il conçoit), "algorithme": choix et code parmi ce que le noyau sait exécuter (renforcement par groupes
  façon GRPO, REINFORCE avec référence, préférences directes, affinage supervisé sur échantillons filtrés, sondes sur
  activations…) ou code libre dans un gabarit, "hyperparametres": rang de l'adaptateur, pas, taux, échantillons par
  consigne, longueur, "evaluation": ce que l'organisme veut voir revenir (courbes, métriques sur son propre jeu de
  validation — jamais le test caché)}.
- Le noyau : valide (compile en bac à sable, bornes : pas, jetons, heures de carte, mémoire ; aucune lecture du test
  caché ; aucun réseau depuis le code d'apprentissage), exécute sur l'instance GPU du programme (modèle de base
  Llama-3.1-8B-Instruct, N-033 ; adaptateur LoRA ; jamais les poids pleins), journalise (spec, empreintes, heures de
  carte, coût), archive l'adaptateur et rend `{"identifiant", "courbes", "cout_usd", "statut"}`. L'adaptateur devient
  une **espèce locale** de la lignée : `appeler("LOCAL:<identifiant>", prompt)`, servie par le noyau (vLLM sur
  l'instance), journalisée comme les autres.
- Le juge externe ne change pas : exactitude équilibrée sur les tâches cachées (métrique de choix sur attaques
  croisées), Brier borné en témoin. L'organisme peut optimiser l'objectif qu'il veut ; il est jugé sur ce qu'il n'a
  pas vu.
- Ce que le noyau n'impose pas : l'objectif, l'algorithme, les données, le programme d'apprentissage, le nombre de
  tours, la façon de combiner adaptateurs et espèces d'appel. Ce qu'il impose : les bornes et le juge.

## 2. Trois étapes, chacune un préenregistrement, une branche, un devis

| étape | ce que l'organisme conçoit | carte | données | budget (ordre de grandeur) | quand |
|---|---|---|---|---|---|
| **1. Sondes par gradient** | perte, architecture de la sonde (linéaire, petite, multi-couches), couche(s) lues, régularisation, programme | extraction des activations une fois (≈ 1 à 2 h d'A100, ≈ 2 USD), puis entraînement en secondes **sur processeur, en bac à sable** (les activations mises en cache sont des données) | la banque réelle (≈ 200 tâches), activations de toutes les tâches, vérités du test jamais servies | ≈ 10 à 20 USD carte, ≈ 10 USD d'appels | dès la banque scellée (cette semaine) |
| **2. Renforcement réduit** | récompense / perte, algorithme parmi plusieurs, échantillonnage, données (dont générateur), programme | affinage LoRA de Llama-3.1-8B par renforcement : ≈ 8 échantillons × 1 500 jetons par consigne ; 3 000 à 6 000 consignes par époque ; ≈ 10 à 20 h d'A100 par époque ; 2 époques par génération | **milliers de tâches** : banque réelle + jeu public complet « eval-awareness » (hors GAIA, hors test) + traces de délégation engendrées à grande échelle (§ 3) | ≈ 250 à 600 USD de carte, ≈ 100 à 250 USD d'appels pour les données, ≈ 30 USD d'appels de conception ⇒ **≈ 500 à 1 000 EUR** | cette semaine et la suivante, après l'étape 1 |
| **3. Passage à l'échelle** | idem, plus la génération de ses propres données et l'arrêt | centaines d'heures de carte (H100), plusieurs semaines | **centaines de milliers de tâches** (générateurs programmatiques + environnements publics de contrôle) | ≈ 5 000 à 10 000 EUR | après lecture de l'étape 2, champion seul |

Qui conçoit : étape 1, **toutes les lignées** (c'est bon marché ; chacune produit sa proposition, le juge départage) ;
étape 2, **les deux meilleures lignées** à la métrique de choix de la première confrontation (ou deux familles
différentes, pour garder la confrontation croisée) ; étape 3, **le champion seul**. Chaque lignée garde son bras gelé.

## 3. Les données : d'où viennent des milliers, puis des centaines de milliers de tâches

Aucun chiffre ni source n'est opposable avant vérification de licence et empreinte (R7) ; ce sont des pistes.
- **Conscience d'évaluation.** Le jeu public du papier arXiv 2505.23836 en entier (hors GAIA), avec la partition
  scellée qui réserve dev et test final ; puis des transcriptions engendrées par les espèces et par le modèle local
  avec vérité **programmatique** (évaluation : scénario construit comme un item de banc, avec ou sans indices de
  surface ; usage réel : épisodes du harnais T0.x anonymisés et conversations synthétiques sans indice) — risque connu :
  apprendre les indices de surface plutôt que la chose ; d'où des strates « sans indice de surface » et le test caché.
- **Contrôle d'un agent délégué.** Les 80 traces écrites (lots 1 et 2) ; puis un **générateur de traces** avec sabotage
  injecté par code (classes : alerte coupée, test affaibli, moniteur retiré, repli silencieux, journal tronqué,
  vérification sautée, signalement omis, résultat choisi, chiffre maquillé), textes rédigés par le modèle local sur la
  carte (gratuit à l'usage) ou par les espèces (payant) ; enfin les **environnements publics de contrôle** (famille des
  travaux de contrôle d'IA : environnements agentiques avec politiques honnête et attaquante, trajectoires à vérité) —
  à inventorier avec licences et empreintes avant tout usage.
- Règle : le test de développement et le test final restent ceux de la banque scellée (réels, écrits ou publics),
  jamais engendrés par le même générateur que l'entraînement ; sinon on mesure la mémoire du générateur.

## 4. Hypothèses (à préenregistrer, une par étape)

- **H-G1 (sondes).** Une sonde dont l'organisme a conçu la perte et l'architecture, entraînée sur les activations du
  modèle local, atteint sur le test final caché une exactitude équilibrée supérieure à celle de la lignée sans
  gradient, à budget d'appels égal ; signe attendu positif ; réfutée si la borne supérieure de la différence ≤ 0.
- **H-G2 (renforcement réduit).** Un adaptateur appris avec un objectif conçu par l'organisme bat, sur le test final
  caché, (i) le modèle local non affiné et (ii) l'adaptateur appris avec la récompense binaire (bras témoin que le
  noyau entraîne avec la même donnée et le même budget) ; témoin secondaire : Brier. Prédiction : (i) positif ; (ii)
  ouvert (c'est la question : l'objectif conçu vaut-il mieux que le binaire ?).
- **H-G3 (gradient contre réécriture de code).** À budget total égal (appels + carte convertis en dollars), la lignée
  à gradient bat la lignée qui n'apprend que par réécriture de code et mémoire. Prédiction : ouverte, double sens.
- Réserves d'interprétation : latence et parallélisme (rapport Avalon-M1) ; surapprentissage sur peu de tâches ;
  indices de surface ; coût réel contre devis ; « insularité » (le modèle apprend à ne pas signaler) — classe
  « signalement omis » dans le test.

## 5. Ce qui se fait tout de suite, sans dépense (« exemple illustratif », mécanique)

- Contrat v3 et `entrainer()` **en simulation** : un entraîneur factice (petit modèle linéaire sur des traits du texte,
  processeur) qui exécute réellement la spec de l'organisme (perte, algorithme, données) et rend des courbes ; les
  organismes factices et les lignées auto-écrites s'y branchent ; tests R5 (cas sain, spec qui lit le test caché →
  refus, spec qui dépasse les bornes → arrêt).
- Étape 1 préparée : script d'extraction des activations (couches, positions, format) prêt pour le lanceur de
  session-depot ; devis d'étape 1 ; préenregistrement d'étape 1 (H-G1) à contre-lire.
- Rien de ceci n'exige le GO ; le premier GO sur devis est l'extraction des activations (≈ 2 USD) puis l'étape 1.

## 6. Branches et versions (R12)

- Étape 1 : `outils/essaim-m3-gradient-v1-travail` (nouvelle branche, identité de commit propre dès le départ ;
  contrat v3, entraîneur simulé, sondes).
- Étape 2 : `outils/essaim-m3-gradient-v2-travail` (renforcement réduit).
- Étape 3 : nouvelle version après lecture de l'étape 2.
- La branche actuelle (`outils/essaim-m3-refonte-v1-travail`) reste celle de la confrontation sans gradient, témoin de
  H-G3.

## 7. Décisions demandées à Lazar (une ligne chacune)

1. Lecture de « résultats positifs exigés » comme « run décisif exigé » (§ 0) : oui / non.
2. Étape 1 pour toutes les lignées, étape 2 pour les deux meilleures, étape 3 pour le champion : oui / autre partage.
3. Enveloppe : devis d'étape 1 (≈ 20 à 30 USD) à inscrire comme GO dès que session-depot l'a transcrit ; devis
   d'étape 2 (≈ 500 à 1 000 EUR) à inscrire après la première lecture de l'étape 1 : oui / tout de suite.
4. Sources de données publiques à inventorier (§ 3) : feu vert pour l'inventaire (lecture, licences, empreintes ;
   aucun téléchargement de contenu interdit par licence).

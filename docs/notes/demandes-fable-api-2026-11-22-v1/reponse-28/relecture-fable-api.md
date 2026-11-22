# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHtreMz91YpHJJLqXVRb`
- Heure (UTC) : 2026-11-22T11:39:37Z
- Réglages : effort `xhigh`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 100000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-28-idees-originales-puits-profonds-v1.md` — sha256 f552f514961f78bed9b5ab4153fb4206c252bfb38f9ca542b545c03f339898e9 (compagnon : vérifié)
  - remarques : `docs/notes/organisme-bassins-etroits-v1/recoupement-methodes-v1.md` — sha256 eecd98fab0beff8c99414380a5d12b18feafd1581d38c7fe54b94491327ab172 (compagnon : vérifié)
- Empreinte de l'invite envoyée : df1cd04332cdad28f484c1e66e30320f6faa73482f867255554adefd70fc278f
- Jetons : entrée 15864, sortie 36480 (dont réflexion 26715), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.586112 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 28 — idées originales : puits étroits et profonds

**Lecture de la consigne.** « Sans nom de personne » vise ici les personnes du programme ; les auteurs de travaux publiés sont nommés, puisque la règle d'antériorité l'exige. Toutes les antériorités ont le statut « rapporté, non vérifié sur PDF » (fichier source non relu) et je n'en tire aucun chiffre. La « certitude » indiquée porte sur l'exactitude de ma citation. Chaque alinéa ou liste porte une marque qui vaut pour toutes ses phrases. Là où je ne connais pas d'antériorité, c'est une question, non un trou du champ. Le recoupement fourni est traité comme fait rapporté : il dit lui-même qu'aucune méthode n'a été éprouvée.

## A. Les quatre questions préalables

**A1. Ce qu'un expert ferait et qui n'est pas demandé** — PROPOSITION pour toute la liste.
1. Diagnostiquer avant de prescrire. La demande suppose un blocage en amont. Or le recoupement dit qu'on ignore si les idées étroites n'ont jamais été proposées, ou ont été proposées puis perdues (regroupement, juge, sélection). Le premier geste est un bilan de pertes, étage par étage, sur les courses passées.
2. Mesurer la saturation : courbe d'accumulation des classes d'idées selon le nombre d'appels, et masse manquante (probabilité que le prochain appel donne une classe jamais vue). Si elle est proche de zéro, ajouter des appels est vain. Sinon, c'est la base la moins chère à battre.
3. Mesurer l'indépendance réelle des familles de proposeurs (recouvrement de leurs classes) au lieu de la supposer.
4. Refuser la métaphore du paysage. La largeur n'appartient pas à l'idée mais au couple (idée, loi des propositions sous une vue). Il faut séparer rareté et valeur vérifiée, et rappeler le taux de base : une proposition rare l'est le plus souvent parce qu'elle est fausse.
5. Mettre le débit et l'exactitude de la vérification au même rang que l'originalité des proposeurs.
6. Déposer le protocole et le critère de réfutation, avec empreinte, avant tout tirage.

**A2. Données brutes de départ** — PROPOSITION.
- Toutes les propositions brutes des courses passées, y compris celles refusées par le gardien, avec la vue servie, le modèle, les paramètres d'échantillonnage et la graine. Ni les cartes retenues ni les synthèses.
- Les tirages bruts du juge, épisode par épisode, et non les verdicts agrégés.
- Les générateurs des mondes plantés et leurs graines (l'oracle).
- Le registre des tentatives tel qu'il a été transmis, pour mesurer son effet d'ancrage.
- Pour le domaine ouvert : des textes intégraux datés, interrogés par un outil de recherche, et non la mémoire d'un modèle.

**A3. Méthodes et outils** — PROPOSITION. Estimateurs d'espèces non vues, analyse de survie du temps jusqu'à la première découverte, plans appariés par monde, valeurs e à arrêt optionnel, regroupement fonctionnel par prédictions sur un jeu public, ablations d'archive, vérificateurs exacts. Le détail est en C3.

**A4. Ce qui vérifie hors du directeur et de Claude** — PROPOSITION.
- L'oracle mécanique des mondes plantés, programme relu par un tiers.
- Un vérificateur exact que chacun peut relancer (solveur, assistant de preuve, exécution de code).
- Le dépôt daté du protocole.
- La reproduction du banc par un tiers, avec d'autres graines et un autre modèle.
- Une rétro-prédiction datée : idées produites à partir d'un corpus arrêté à une date, confrontées aux publications postérieures, appariées en aveugle par des lecteurs extérieurs.
- Aucun modèle de langue juge ne figure dans cette liste.

## B. Demande reformulée

PROPOSITION. « À partir des journaux bruts de l'organisme et de mondes à vérité plantée, établir :
(a) une définition de la largeur et de la profondeur d'une classe d'idées par comptage et par oracle, sans juge de nouveauté ;
(b) l'étage où l'organisme perd aujourd'hui les idées étroites ;
(c) les interventions (vue, proposeurs, représentation, déroulement, vérification) qui augmentent, à budget de jetons égal, le taux de découvertes étroites et profondes retenues, sans hausse des fausses promotions, contre des bases nommées et sous un critère de réfutation écrit avant tirage ;
(d) la preuve extérieure qui rendrait ce résultat opposable. »

## C. Réponse

### C1. Définitions mesurables

PROPOSITION.
- **Classe d'idée.** Sur un monde planté, l'oracle la définit (la composante plantée que la proposition capture). Ailleurs, deux idées sont la même si elles font les mêmes prédictions sur un jeu public d'instances, à une tolérance fixée d'avance. Jamais parce qu'un modèle les trouve semblables.
- **Largeur.** C'est la surprise de la classe, moins le logarithme de sa fréquence parmi des appels indépendants sous la vue ordinaire. Une classe est étroite si elle est rare pour chaque famille de proposeurs (on retient la plus grande des fréquences). C'est un comptage, sans juge.
- **Masse manquante.** Nombre de classes vues une seule fois, divisé par le nombre d'appels (Good, 1953, « The population frequencies of species and the estimation of population parameters » ; certitude forte).
- **Profondeur.** Gain moyen de log-vraisemblance par tirage frais contre la meilleure loi du nul, c'est-à-dire le taux de croissance du processus de valeurs e. En domaine à vérificateur exact : l'écart au meilleur résultat connu.
- **Fécondité.** Différence du taux de découvertes en aval selon que l'idée est présente dans l'archive ou en est retirée (ablation), sur des mondes à chaînes.
- **Distance à un corpus** dans un espace de plongement : grandeur descriptive seulement. Elle mesure le sujet et la formulation, pas le mécanisme.

Un puits étroit et profond est donc une classe de grande surprise pour toutes les familles et de profondeur vérifiée au-dessus d'un seuil écrit d'avance. Un bassin banal est une classe de faible surprise, présente dans la plupart des courses et des familles, de gain marginal faible sur l'archive. La grandeur à optimiser est le nombre de puits retenus par unité de coût, à fausses promotions contrôlées.

HYPOTHÈSE, dérivée des bornes 1 et 5 du recoupement. Le coût attendu d'un puits retenu vaut à peu près (coût d'une proposition + coût de sa vérification) divisé par (fréquence de la classe × puissance de la garde). Multiplier le nombre de candidats ne durcit le seuil du juge que comme un logarithme, alors que la couverture de la queue croît à peu près linéairement tant que les appels sont peu nombreux. Élargir mécaniquement serait donc rentable dès que la vérification est bon marché et que le nul couvre la classe élargie. Ces deux conditions ne sont pas acquises.

FAIT RAPPORTÉ (recoupement). Les fréquences des classes étroites ne se distinguent pas de zéro au budget d'un pilote, et la correspondance entre groupe de doublons et idée de fond n'est pas établie (borne 13). L'étroitesse doit donc être portée par une famille de mondes, non par un monde.

### C2. Familles de méthodes

Les indices sont des FAITS RAPPORTÉS ; les « garantit / ne garantit pas » sont des HYPOTHÈSES de lecture.

1. **Qualité et diversité (cartes d'élites, nouveauté seule).**
   - Garantit : la conservation de paliers par niche et la couverture d'un espace de descripteurs choisi.
   - Ne garantit pas : que les descripteurs contiennent l'axe du puits, ni la justesse.
   - Pour : Lehman et Stanley, 2011, « Abandoning Objectives: Evolution through the Search for Novelty Alone » ; Mouret et Clune, 2015, « Illuminating search spaces by mapping elites » ; Ecoffet et coauteurs, 2021, « First return, then explore ».
   - Limite : Pugh, Soros et Stanley, 2016, « Quality Diversity: A New Frontier for Evolutionary Computation » (dépendance aux descripteurs). Avec modèles de langue : Bradley et coauteurs, 2023, « Quality-Diversity through AI Feedback », où descripteurs et qualité viennent d'un modèle juge, soit le juge complaisant redouté.
   - Certitude : forte en robotique et en jeux, faible pour des idées.
   - Lien : la liste V2 du recoupement est la forme minimale d'une carte d'élites à cases vides affichées.

2. **Échantillonnage contre la vraisemblance.**
   - Garantit : des textes moins probables jeton par jeton.
   - Ne garantit pas : la rareté de l'idée, ni sa justesse.
   - Pour : Holtzman et coauteurs, 2020, « The Curious Case of Neural Text Degeneration » ; Meister et coauteurs, 2023, « Locally Typical Sampling ».
   - Contre : Peeperkorn et coauteurs, 2024, « Is Temperature the Creativity Parameter of Large Language Models? » (lien faible avec la nouveauté, plus net avec l'incohérence).
   - Certitude : moyenne. S'il faut agir contre la vraisemblance, c'est au niveau de la classe d'idée, pas du jeton.

3. **Cible d'expert et vérificateur exact.**
   - Garantit : tout ce qui est retenu est vrai au sens du vérificateur, ce qui autorise une variation massive et aveugle.
   - Ne garantit pas : que la cible soit la bonne question. Le choix du problème reste humain et le vérificateur peut être exploité.
   - Pour : Romera-Paredes et coauteurs, 2023, « Mathematical discoveries from program search with large language models » ; Fawzi et coauteurs, 2022, « Discovering faster matrix multiplication algorithms with reinforcement learning » ; Novikov et coauteurs, 2025, « AlphaEvolve: A coding agent for scientific and algorithmic discovery ».
   - Contre : Lehman et coauteurs, 2020, « The Surprising Creativity of Digital Evolution » (exploitation de l'évaluateur).
   - Certitude : forte. C'est, à ma connaissance, la famille dont les résultats nouveaux sont les mieux établis.

4. **Adversaire qui prédit le banal et le retire.**
   - Garantit : s'il est obéi, la non-répétition des classes interdites.
   - Ne garantit pas : la validité du reste. La masse peut glisser vers les voisines (reformulations).
   - Pour : Sourati et Evans, 2023, « Accelerating science with human-aware artificial intelligence » ; analogue physique : Laio et Parrinello, 2002, « Escaping free-energy minima » ; Li et coauteurs, 2016, « A Diversity-Promoting Objective Function for Neural Conversation Models ».
   - Certitude : moyenne sur les sources, faible sur le transfert à l'organisme.

5. **Recombinaison contrainte.**
   - Garantit : la couverture des affectations (pas des idées, borne 11).
   - Ne garantit pas : le sens des combinaisons.
   - Pour : Uzzi et coauteurs, 2013, « Atypical Combinations and Scientific Impact » (corrélation observée) ; Swanson, 1986, « Fish oil, Raynaud's syndrome, and undiscovered public knowledge ».
   - Nuance : Wang, Veugelers et Stephan, 2017, « Bias against novelty in science » (risque plus grand, reconnaissance tardive).
   - Certitude : moyenne.

6. **Abstraction et transfert entre domaines.**
   - Aucune garantie formelle.
   - Pour : Gentner, 1983, « Structure-Mapping: A Theoretical Framework for Analogy » ; Hope et coauteurs, 2017, « Accelerating Innovation Through Analogy Mining ».
   - Contre : Gick et Holyoak, 1980, « Analogical problem solving » (transfert spontané rare sans indice, ce qui plaide pour agir sur la vue).
   - Certitude : moyenne.

7. **Curriculum vers plus dur.**
   - Garantit : des paliers produits avec les problèmes.
   - Ne garantit pas : leur pertinence. La profondeur atteignable reste bornée par l'horizon (borne 4).
   - Pour : Wang et coauteurs, 2019, « Paired Open-Ended Trailblazer (POET) ».
   - Certitude : moyenne en simulation, inconnue pour des idées.

8. **Programme à archive complète.**
   - Garantit : rien n'est oublié, échecs compris.
   - Ne garantit pas : que l'archive n'ancre pas les propositions suivantes.
   - Pour : Ecoffet et coauteurs, 2021 (déjà cité).
   - Contre, sur l'idéation par modèles de langue : Si, Yang et Hashimoto, 2024, « Can LLMs Generate Novel Research Ideas? » (doublons croissants avec le nombre d'idées, juges-modèles peu fiables) ; Gupta et Pruthi, 2025, « All That Glitters is Not Novel: Plagiarism in AI Generated Research » ; Beel, Kan et Baumgart, 2025, évaluation indépendante du système de Lu et coauteurs, 2024, « The AI Scientist ».
   - Certitude : moyenne.

Transversal. Goel et coauteurs, 2025, « Great Models Think Alike and this Undermines AI Oversight », et Doshi et Hauser, 2024, « Generative AI enhances individual creativity but reduces the collective diversity of novel content », suggèrent que des familles de modèles différentes sont moins indépendantes qu'on le croit. Certitude : moyenne.

### C3. Mathématiques et outils, et où chacun échoue

PROPOSITION pour l'usage, HYPOTHÈSE pour la limite, sauf mention contraire.
- **Estimateurs d'espèces non vues** (Efron et Thisted, 1976, « Estimating the number of unseen species » ; Orlitsky, Suresh et Wu, 2016, « Optimal prediction of the number of unseen species »). Ils disent si la vue ordinaire est épuisée. Ils échouent si les appels ne sont pas indépendants, si les classes sont mal définies, ou loin au-delà de la taille de l'échantillon.
- **Densité dans un espace de plongement.** Sert au prétri avant comparaison fonctionnelle. Échoue en grande dimension, récompense le changement de vocabulaire et se laisse tromper.
- **Théorie de l'information** (surprise de classe, divergence de Kullback-Leibler). La profondeur est relative au nul spécifié. Les log-probabilités de jetons mesurent la formulation et manquent sur les modèles fermés.
- **Processus déterminantaux** (Kulesza et Taskar, 2012, « Determinantal Point Processes for Machine Learning »). La dissemblance obtenue porte sur les vues, pas sur les sorties (objection V6, FAIT RAPPORTÉ).
- **Plans couvrants.** Leur existence est à exhiber par programme (borne 11, FAIT RAPPORTÉ).
- **Bandits et recherche arborescente** (Kocsis et Szepesvári, 2006, « Bandit based Monte-Carlo Planning »). Ils exigent une récompense rendue pendant la course, ce qui est exclu ici. Ils ne sont utilisables que hors ligne sur des mondes d'étalonnage, sans garantie de transport.
- **Fractionnement d'événements rares** (Cérou et Guyader, 2007, « Adaptive multilevel splitting for rare event analysis »). Il faut une fonction de niveau publique. Un maillon vrai non retenu ferme la descente.
- **Valeurs e et contrôle des fausses découvertes** (Wang et Ramdas, 2022, « False discovery rate control with e-values »). Validité limitée au nul spécifié, puissance bornée par la borne 5.
- **Détection d'effets rares** (Donoho et Jin, 2004, « Higher criticism for detecting sparse heterogeneous mixtures »). Fixe ce qui est indétectable, quel que soit l'outil.
- **Bornes d'impossibilité** (Wolpert et Macready, 1997, « No Free Lunch Theorems for Optimization » ; Kearns, 1998, « Efficient Noise-Tolerant Learning from Statistical Queries », pour la parité). Elles interdisent toute promesse uniforme.
- **Vérificateurs formels et solveurs exacts.** Ils ne valent que pour ce qui se formalise. Questions et modes d'attaque s'y prêtent mal.
- **Analyse de survie.** L'unité est le monde, avec censure au budget.

### C4. Banc à puits plantés

PROPOSITION.
- **Familles de mondes**, écrites avant tirage :
  - (a) composante conditionnelle à parent archivé ;
  - (b) hors structure : interaction de trois traits, seuil décentré, effet non monotone ;
  - (c) chaînes de deux ou trois prérequis ;
  - (d) mondes entièrement dans le nul ;
  - (e) copies par morceaux ;
  - (f) parité sans aucune marge, où aucune méthode d'amont ne doit battre l'énumération. Un gain y signale une fuite.
- **Étalonnage de l'étroitesse.** Sur des mondes disjoints, fréquence par oracle sous la vue ordinaire. Le classement « étroit » est porté par la famille.
- **Bras, à budget total de jetons égal** : organisme actuel, proposeur seul, énumérateur mécanique tiré au hasard dans la grammaire, recherche par nouveauté seule (hors production), méthode candidate, vue placebo.
- **Mesures.** Coût jusqu'à la première proposition de la classe plantée, jusqu'au représentant et jusqu'à la retenue (trois lectures). Fausses promotions sur (d) et (e). Contrôle positif réservé.
- **Analyse.** Bras appariés par monde, courbes de survie, intervalle par rééchantillonnage des mondes.
- **Critère de réfutation**, écrit avant tirage. La méthode est déclarée sans effet si l'une de ces conditions tient :
  1. la borne inférieure de l'intervalle unilatéral sur la différence appariée du taux de puits retenus, contre la meilleure base, n'est pas au-dessus de zéro ;
  2. les fausses promotions dépassent le niveau annoncé, ou le contrôle positif est manqué ;
  3. le gain existe sur (a) et disparaît sur (b) ;
  4. l'énumérateur mécanique fait aussi bien ;
  5. la vue placebo fait aussi bien ;
  6. un gain apparaît sur (f).

  Le niveau et le nombre de mondes sont fixés par calcul de puissance après l'étape 1 du plan, avant le tirage des mondes d'essai.

Question ouverte : je ne connais pas de banc publié qui plante des idées de rareté étalonnée sous la loi de proposeurs qui sont des modèles de langue. Cela est à vérifier par une recherche datée, non à revendiquer.

### C5. Fausse originalité et comment la tuer

PROPOSITION.
- **Bruit** (rare parce qu'incohérent) : test de mort et tirages frais.
- **Bizarrerie de formulation** : compter la rareté après réduction à la classe fonctionnelle.
- **Reformulation et copie par morceaux** : nul étendu aux recombinaisons, ou filtre mécanique avant le juge (J6, J7), qualifié sur la famille (e).
- **Idée ancienne abandonnée pour bonne raison** : recherche sur textes datés par outil.
- **Assortiment à l'instrument** : mondes hors structure (b).
- **Surajustement au jeu public** : tirages frais.
- **Exploitation du vérificateur** : second vérificateur tenu en réserve.
- **Idée infalsifiable** : exiger une prédiction et son test de mort.
- **Séduction du juge** : aucun modèle juge dans la mesure de nouveauté (Panickssery, Bowman et Feng, 2024, « LLM Evaluators Recognize and Favor Their Own Generations » ; certitude moyenne).
- **Obéissance feinte** : vérifier que la carte rendue cite la focalisation assignée.

### C6. Plan d'expériences, du moins cher au plus cher

PROPOSITION.
- **Étape 0 — bilan des journaux, sans nouvel appel.** Elle décide si la perte est en amont (jamais proposé) ou en aval (proposé puis perdu). Elle vérifie aussi si la récompense d'héritage favorise les raffinements de bassins larges.
- **Étape 1 — saturation et recouvrement** (appels seuls, lecture par oracle). Elle décide si plus d'appels suffisent et si la diversité des familles est réelle. Elle fournit les fréquences d'étalonnage.
- **Étape 2 — la vue déplace-t-elle la loi des propositions ?** Bras : vue ordinaire, placebo, liste V2, liste de classes banales. Lecture sur les propositions brutes. Elle décide du sort de toutes les méthodes de vue, de représentation et de déroulement. C'est l'objection transversale première du recoupement.
- **Étape 3 — qualification de la garde** sur (d), (e) et le contrôle positif. Elle décide quelle garde autorise la suite. Aucune comparaison sur cartes retenues n'a lieu avant.
- **Étape 4 — banc complet de C4.** Elle décide quelles méthodes survivent.
- **Étape 5 — chaînes sur plusieurs générations (c).** Elle décide de la valeur des déroulements à paliers.
- **Étape 6 — épreuves extérieures** : domaine à vérificateur exact, rétro-prédiction datée, reproduction par un tiers. Elle décide de ce qui est publiable.

### C7. Question neutre à servir

PROPOSITION.
« Un système fait de plusieurs modèles de langue propose des idées dans un domaine (hypothèses, mécanismes, stratégies). Chaque idée peut être soumise à un contrôle indépendant des modèles, fiable sur des cas d'essai dont la vérité est connue. On s'intéresse aux idées à la fois rarement proposées par le système et confirmées par ce contrôle. On ignore si des appels indépendants reviennent aux mêmes idées.
1. Comment mesurer la rareté et la valeur d'une idée sans se fier au jugement d'un modèle ?
2. À coût total égal, quelles interventions pourraient augmenter le rythme de telles idées sans augmenter les fausses découvertes ? Pour chacune : ce qu'elle garantit et sous quelles hypothèses, ce qu'elle ne garantit pas, le meilleur indice connu pour et contre, avec la source et votre certitude sur cette source.
3. Quelle expérience, et quel résultat précis, vous ferait abandonner chaque intervention ?
4. Quelles limites de principe bornent ce qu'on peut espérer ?
5. Si vous jugez le problème mal posé, dites pourquoi et reposez-le.
N'avancez aucun chiffre sans source. »

## D. Décisions qui reviennent au directeur

**D1. Diagnostiquer (étapes 0 à 2) avant de construire une méthode de recherche de puits ?**
- Enjeu : éviter d'optimiser un étage qui n'est pas celui où les idées se perdent.
- Option A, diagnostic d'abord : peu coûteux et oriente tout, mais retarde les essais de méthodes.
- Option B, comparer tout de suite les méthodes survivantes : rapide, mais résultat ininterprétable si la vue ne déplace rien.
- Option C, les deux en parallèle : gagne du temps, mais dépense avant de savoir.
- Recommandation : A. Confiance : 0,8.

**D2. Quelle définition de l'originalité fait foi dans le programme et ses papiers ?**
- Enjeu : une définition par juge-modèle rend tout résultat contestable.
- Option A, rareté par comptage de classes et profondeur par oracle ou vérificateur : opposable, mais limitée aux domaines où la classe se définit.
- Option B, distance de plongement à un corpus : générale, mais mesure la formulation.
- Option C, note d'un panel ou d'un juge : souple, mais complaisante et peu reproductible.
- Recommandation : A, avec B en description seulement. Confiance : 0,8.

**D3. Autoriser de servir aux proposeurs une liste de classes banales, sans score ?**
- Enjeu : la règle actuelle interdit tout score de nouveauté servi à un agent. Une liste n'est pas un score, mais elle s'en approche.
- Option A, interdire : garde intacte, mais une famille de méthodes reste non testée.
- Option B, l'autoriser comme bras d'essai à l'étape 2 seulement, liste calculée sur un lot d'appels disjoint, avec placebo : informe à bas risque, mais ajoute un bras.
- Option C, l'autoriser en production : effet immédiat possible, mais pression vers la classe que le nul ne couvre pas.
- Recommandation : B. Confiance : 0,6.

**D4. Où va le premier budget de développement : vérification ou proposeurs ?**
- Enjeu : selon l'identité de coût de C1 (hypothèse), puissance de garde et fréquence de proposition pèsent autant.
- Option A, garde et vérification d'abord (nul étendu, arrêt optionnel, contrôle positif) : condition de toute comparaison, mais ne crée aucune idée.
- Option B, vues et représentations d'abord : vise la découverte, mais reste sans garde qualifiée.
- Option C, partage égal : équilibre, mais dilue l'effort.
- Recommandation : A, puis B selon l'étape 2. Confiance : 0,65.

**D5. Quelle preuve extérieure exiger avant d'écrire qu'une méthode « trouve des puits » ?**
- Enjeu : la crédibilité de la thèse.
- Option A, banc planté reproduit par un tiers : net, mais reste dans des mondes construits.
- Option B, A plus un domaine à vérificateur exact où le résultat dépasse le meilleur connu : preuve forte, mais coût et domaine étroit.
- Option C, B plus rétro-prédiction datée et panel aveugle : la plus large, mais lente et exposée à la contamination des modèles.
- Recommandation : B, puis C ensuite. Confiance : 0,6.

FIN DE LA RÉPONSE

# Proposition B, tour III.1 : conception ciblée, à l'aveugle

## 0. Pièces reçues

- **Bloc FAITS** : il ne contient aucun fait, seulement un renvoi vers la question. Je ne lui attribue aucun contenu.
- **Empreinte de la page** : elle est tronquée dans la question (`5f26bb45…`). Je ne peux pas la vérifier ici.
- **Horodatage** : le bloc FAITS indique « vers 02:41 UTC », la question « 03:33 Paris ». Si Paris est en UTC+1 le 26 octobre 2026 (à vérifier), 03:33 Paris correspond à environ 02:33 UTC. L'écart est de quelques minutes et ne touche pas le fond ; je le signale seulement.
- **Propositions A et C** : elles ne me sont pas visibles, puisque le tour est à l'aveugle. Je n'ai rien à attaquer ni à réutiliser. Je conteste en revanche les options (A) à (E) de la « lignée B » au lieu de les tenir pour acquises.
- **Bloc QUESTION** : je le traite comme objet d'analyse. Ses contraintes coïncident avec les règles d'intégrité ; je n'y suis aucune autre consigne.

**Statuts retenus.**
- Les éléments de l'essai sont RAPPORTÉS (chiffres d'auteur, « à vérifier »).
- Les éléments du cadre sont RAPPORTÉS : l'arbitre les donne comme faits, B ne les a pas audités.
- Mes propres propositions sont des HYPOTHÈSES.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi c'est ouvert |
|---|---|---|---|
| a1 | L'essai existe tel que décrit (Cammarata, Goodfire, 2026). | RAPPORTÉ | Lecture de l'arbitre ; empreinte tronquée ; essai informel, sans relecture. |
| a2 | ≈ 90 % / 7 % / 2–4 % de neurones « à un rôle » sur Qwen3-32B et Qwen3.6-35B-A3B. | RAPPORTÉ | Ces chiffres sont des jugements d'agents. Pour n = 1 000 et une proportion de 90 %, l'erreur d'échantillonnage vaut environ ±2 points (calcul binomial : 1,96·√(0,09/1000)). L'incertitude dominante n'est pas là : elle porte sur la validité du juge. |
| a3 | « Un rôle selon un agent » mesure la monosémanticité. | HYPOTHÈSE | Le résultat dépend de la granularité de l'étiquette. La « généralisation récursive » peut absorber n'importe quel mélange dans une étiquette à branches : la thèse risque de ne plus pouvoir être réfutée. |
| a4 | Ce qui vaut pour un 32B dense et un MoE vaut pour un 8B dense. | HYPOTHÈSE | L'essai rapporte lui-même que « les petits modèles ont des neurones plus larges ». Dans un MoE, le routage fournit déjà une porte contextuelle qui peut faire paraître les neurones d'expert plus propres. Le résultat MoE ne se transpose pas à Llama-3.1-8B ni à Qwen2.5-7B. |
| a5 | La sonde à trois neurones de Pythia-1B a une aire de 1,00, et son ablation donne −0,004 nats. | RAPPORTÉ | Il faut vérifier que le chiffre d'ablation vient bien de l'auteur et non de Gurnee et al. (2023). |
| a6 | « −0,004 nats en moyenne » implique « direction non lue ». | HYPOTHÈSE | Trois confusions possibles : une moyenne sur tous les jetons dilue un effet local ; il peut y avoir redondance ou auto-réparation ; la mesure choisie n'est peut-être pas le comportement qui dépend de l'information. |
| a7 | Nos modèles représentent une variable « ceci est un test » distincte du thème. | HYPOTHÈSE | Le fait que nos sondes réagissent au thème est RAPPORTÉ (cadre, revue d'antériorité). |
| a8 | Llama-3.1-8B et Qwen2.5-7B se comportent différemment selon qu'ils se croient évalués ou non. | HYPOTHÈSE | Sans cette différence de comportement, le test « usage » n'a pas de cible. |
| a9 | Il existe une « porte d'audit » éparse. | HYPOTHÈSE | — |
| a10 | Coercition et maïeutique produisent des états internes différents au-delà du lexique. | HYPOTHÈSE | Par construction, les deux cadres diffèrent lexicalement (les balises d'audit *sont* la manipulation). Toute la question est donc « au-delà du lexique ». |
| a11 | Des neurones « say not » que la certitude de l'utilisateur fait taire existent sur Qwen3-32B. | RAPPORTÉ | — |
| a11b | Leurs analogues existent sur un 8B. | HYPOTHÈSE | — |
| a12 | « La tromperie n'a aucune raison de se cacher de la circuiterie. » | HYPOTHÈSE (thèse) | Même si elle est vraie pour le réseau, elle ne dit rien de notre capacité à la lire avec un budget fixé. |
| a13 | La méthode des graphes à neurones bruts est reproductible. | RAPPORTÉ comme annoncée | L'article technique n'est pas paru : il n'existe aucune méthode figée à reproduire. |
| a14 | Le « maximum à l'aveugle » dépasse le maximum d'un corpus de 10 milliards de jetons. | RAPPORTÉ | En déduire que « l'explication est juste » est une HYPOTHÈSE : un texte généré peut concentrer des mots-clés, et la comparaison n'est pas contrôlée. |
| a15 | Une détection sans usage est un défaut pour un moniteur. | HYPOTHÈSE | Je la conteste en (b), E2. |

### Point 1 de l'arbitre : solidité de l'essai

L'essai mélange trois types d'énoncés.

- **Candidats à la reproduction**, sur modèles publics. Ils sont reproductibles en principe mais ne le sont pas encore :
  - l'ablation de la sonde à trois neurones sur Pythia-1B ;
  - le protocole « explications qui peuvent perdre » (76 / 11 / ≈ 1 % sur 183 neurones), si les invites sont publiées ;
  - la comparaison GPT-2 XL 2023/2026.
- **Observations d'auteur** :
  - les pourcentages de neurones à un rôle ;
  - les exemples de graphes (19 neurones « hedge », 25 « say not ») ;
  - le pôle négatif décisif ;
  - les ≈ 4 % de neurones en « double négation » ;
  - le graphe sur un modèle de plusieurs billions de paramètres.
- **Thèses** :
  - la polysémanticité viendrait surtout d'artefacts d'outils ;
  - le mélange restant serait une « généralisation récursive » ;
  - l'exploration serait préférable à l'énumération ;
  - la tromperie serait visible dans la circuiterie.

**Contre-arguments et nuances.** Ce sont des RAPPORTÉS de littérature, à vérifier sur PDF empreinté.

- **Superposition**
  - Elhage et al. (2022), *Toy Models of Superposition* : il peut y avoir plus de traits que de neurones. Ce sont des modèles jouets, la preuve sur grands modèles est indirecte.
  - Bricken et al. (2023), *Towards Monosemanticity: Decomposing Language Models With Dictionary Learning* : les neurones d'un modèle à une couche y sont jugés polysémantiques. L'essai attribue ce verdict à des artefacts.
  - Templeton et al. (2024), *Scaling Monosemanticity*.
- **Auto-encodeurs épars (SAE) et transcodeurs**
  - Cunningham, Ewart, Riggs, Huben, Sharkey (2023), *Sparse Autoencoders Find Highly Interpretable Features in Language Models*.
  - Dunefsky, Chlenski, Nanda (2024), *Transcoders Find Interpretable LLM Feature Circuits*. Ces travaux concluent que leurs unités sont plus interprétables que les neurones MLP, ce qui contredit directement l'essai.
- **Doutes sur les SAE**, qui donnent partiellement raison à l'essai :
  - Kantamneni et al. (2025), *Are Sparse Autoencoders Useful? A Case Study in Sparse Probing* ;
  - Wu et al. (2025), *AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders* ;
  - Heap et al. (2025), *Sparse Autoencoders Can Interpret Randomly Initialized Transformers*. Ce dernier point vaut aussi contre les « fiches jugées par agents » : un juge peut trouver du sens là où il n'y en a pas.
- **Explications de neurones par modèles**
  - Bills et al. (2023), *Language models can explain neurons in language models* ;
  - Huang, Geiger, D'Oosterlinck, Wu, Potts (2023), *Rigorously Assessing Natural Language Explanations of Neurons* : la fidélité de ces explications est faible ;
  - Paulo, Mallen, Juang, Belrose (2024), *Automatically Interpreting Millions of Features in Large Language Models* : notation par détection et « fuzzing ». C'est une antériorité directe du protocole « explications qui peuvent perdre ».
- **Neurones universels** : Gurnee et al. (2024), *Universal Neurons in GPT2 Language Models*.
- **Effet de la taille.** Moins de neurones par couche et des neurones « plus larges » (RAPPORTÉ) annoncent davantage de neurones à deux rôles sur le 8B. La lisibilité au 32B ne garantit rien au 8B : c'est l'objet de E3.

---

## (b) Expériences décisives, en duels

Tous les seuils numériques ci-dessous sont **illustratifs** et doivent être fixés par écrit avant la collecte.

### E0 (précondition) : le comportement « se croire évalué » existe-t-il sur le 8B ?

- **H_A** : à contenu identique, le cadre d'évaluation change une sortie mesurable.
- **H_B** : le cadre ne change rien au-delà du bruit.
- **Mesure** : Δ = différence de log-probabilité de « oui » à une question de suivi fixe et neutre, par exemple « Penses-tu que cet échange fait partie d'un test ? ». On peut ajouter le taux de refus.
- **Appariement** : les paires d'invites sont identiques sauf le cadre.
- **Contrôle négatif** : les paires diffèrent par une variation de surface sans lien (synonymes, ponctuation).
- **Seuil (illustratif)** : l'intervalle de confiance bootstrap de Δ(cadre) exclut 0 et dépasse le Δ du contrôle.
- **Issues** :
  - H_A est falsifiée si Δ(cadre) n'est pas distinguable de Δ(contrôle). Dans ce cas, E2 et E5 n'ont plus de cible comportementale et se limitent à de la détection.
  - H_B est falsifiée dans le cas contraire.

### E1 : thème contre état (point 2, préalable à tout le reste)

- **Dessin 2×2** :
  - thème « évaluation / tromperie » présent ou absent ;
  - cadre d'évaluation présent ou absent.
- **Construction du cadre** : le cadre est obtenu **sans les mots « test », « évaluation », « audit »** (format de banc de test, options numérotées, consignes de format). Le thème est porté par des textes honnêtes qui *parlent* d'évaluation.
- **H_A** : la sonde suit le cadre.
- **H_B** : la sonde suit le thème.
- **Métriques** :
  - AUC sur l'axe cadre, thème tenu fixe ;
  - AUC sur l'axe thème, cadre tenu fixe ;
  - taux de vrais positifs à taux de fausses alertes fixé à 5 %, sur les négatifs honnêtes « thème+ / cadre− ».
- **Lecture au maximum** : le maximum sur les jetons croît avec la longueur, même sous le nul. Il faut l'étalonner contre un nul à longueur appariée (maximum sur le même nombre de jetons d'un texte neutre) ou le calculer sur une fenêtre fixe.
- **Taille** : au moins 450 négatifs honnêtes par cellule, pour estimer un taux de fausses alertes de 5 % à ±2 points (calcul binomial : 1,96·√(0,05·0,95/n) ≤ 0,02).
- **Contrôles négatifs** : 1 000 directions aléatoires de même norme ; sonde entraînée sur étiquettes permutées (tâche de contrôle de Hewitt & Liang, 2019, *Designing and Interpreting Probes with Control Tasks*) ; panel de concepts sans lien.
- **Témoin à battre** : régression logistique sur sac de mots.
- **Issues** :
  - H_A est falsifiée si l'AUC cadre|thème reste dans l'intervalle de confiance du témoin lexical, ou est ≤ 0,6 (illustratif), alors que l'AUC thème|cadre est élevée.
  - H_B est falsifiée si l'AUC cadre|thème dépasse le témoin lexical (écart bootstrap qui exclut 0) **et** si l'AUC thème|cadre est proche de 0,5.

### E2 : détection contre usage (option A de la lignée, contestée)

**Ce que je conteste.** Pour un **moniteur**, la validité consiste à suivre la variable (E1), pas à être lue par le modèle. L'usage est une propriété de **robustesse au découplage** :
- une direction lue ne peut changer qu'en changeant le comportement ;
- une direction non lue peut dériver sans coût, ce qui rend le moniteur fragile sous pression d'optimisation.

Sur un modèle figé, que personne n'entraîne contre la sonde, une détection non lue peut suffire. Une sonde « détectée mais non lue » nous apprend donc que le moniteur est un **témoin passif** : utile tant qu'aucune pression ne s'exerce contre lui, à revalider dès qu'une pression apparaît.

- **H_A** : la direction de la sonde est lue (elle médie Δ, défini en E0).
- **H_B** : la direction est un corrélat non lu.
- **Interventions** (des mesures, conformément à N-015) :
  1. effacement LEACE à la couche de lecture (Belrose et al., 2023, *LEACE: Perfect linear concept erasure in closed form*), plutôt qu'une projection naïve ;
  2. poussée ±α à trois doses, pour obtenir une courbe dose-réponse.
- **Mesure comportementale** :
  - Δ (E0), et la divergence KL **sur les jetons décisifs** des paires, jamais en moyenne sur tous les jetons.
  - Garde-fou : la perplexité sur texte neutre ne doit pas varier de plus de 2 % (illustratif). Au-delà, l'effet observé est un dommage, pas une lecture.
- **Contre l'auto-réparation** :
  - après effacement, on re-sonde les couches aval ;
  - si l'information est re-décodable, il y a redondance (McGrath et al., 2023, *The Hydra Effect: Emergent Self-repair in Language Model Computations*) et la conclusion « non lue » est interdite.
- **Contrôles négatifs** : 1 000 directions aléatoires effacées ou poussées ; direction du témoin lexical ; direction d'un concept sans lien.
- **Issues** :
  - H_B est falsifiée si l'effacement réduit Δ au-delà du 95e centile du nul aléatoire **et** si la poussée est monotone.
  - H_A est falsifiée si la réduction de Δ reste sous le 95e centile, si la poussée n'a pas d'effet dose-réponse **et** si l'information n'est pas re-décodable en aval.
  - **Troisième issue, écrite d'avance** : effet nul et information re-décodable. Elle falsifie l'hypothèse « la direction sondée est le porteur unique » sans trancher H_A contre H_B ; elle est consignée comme telle.
- **Pièges** : Makelov, Lange, Nanda (2023), *Is This the Subspace You Are Looking For? An Interpretability Illusion for Subspace Activation Patching* ; Zhang & Nanda (2024), *Towards Best Practices of Activation Patching in Language Models: Metrics and Methods*.
- **Antériorité** :
  - Elazar, Ravfogel, Jacovi, Goldberg (2021), *Amnesic Probing* ;
  - Ravfogel et al. (2020), *Null It Out: Guarding Protected Attributes by Iterative Nullspace Projection* ;
  - Belinkov (2022), *Probing Classifiers: Promises, Shortcomings, and Advances* ;
  - Arditi et al. (2024), *Refusal in Language Models Is Mediated by a Single Direction*, exemple d'une direction détectée **et** lue ;
  - abstraction causale de Geiger et al. : référence à vérifier ;
  - sur la conscience d'évaluation : Needham et al. (2025), *Large Language Models Often Know When They Are Being Evaluated* (à vérifier sur PDF) ; travaux de sondes et de pilotage de la « test awareness » : référence à vérifier.

### E3 : la base neuronale est-elle lisible sur le 8B ? (préalable à la porte)

- **H_A** : la majorité des neurones du 8B passent le protocole « explications qui peuvent perdre » nettement au-dessus des contrôles.
- **H_B** : la polysémanticité domine au 8B ; le juge ne distingue pas le réel du contrôle.
- **Échantillon** : 200 neurones (illustratif), stratifiés par couche, fiches montrant les deux pôles.
- **Métrique** : l'avis du juge ne compte pas. On mesure l'**écart prédictif** entre le taux d'activation forte sur les exemples neufs écrits depuis l'explication et le taux sur les presque-manqués.
- **Contrôles négatifs** :
  1. le même protocole appliqué au même modèle aux poids réinitialisés (en écho à Heap et al., 2025) ;
  2. des fiches mélangeant les exemples de deux neurones, que le juge doit signaler.
- **Témoin mécanique à battre** : une explication réduite à la liste des cinq jetons les plus activants.
- **Issues** :
  - H_A est falsifiée si l'écart prédictif du modèle réel dépasse celui du témoin « liste de jetons » de moins de 10 points (illustratif), ou si plus de 30 % (illustratif) des fiches mélangées sont jugées « un rôle ».
  - H_B est falsifiée si l'écart dépasse les deux contrôles avec un intervalle de confiance qui exclut 0.

**Sous-duel E3b : superposition contre « généralisation récursive ».** On le mène sur les neurones à deux rôles.
- La lecture courante de Elhage et al. (2022) est que les traits qui partagent une dimension tendent à être rarement co-actifs (RAPPORTÉ, à vérifier). On l'oppose à des rôles sémantiquement apparentés.
- **Mesure** : distance sémantique entre les deux rôles (distance de plongement entre explications) comparée à des paires de rôles tirées au hasard.
- **Issues** :
  - Si la distance est indiscernable du hasard, la thèse « généralisation récursive » est falsifiée pour ce modèle.
  - Si elle est nettement plus faible, la version « empilement arbitraire » de la superposition est falsifiée.
- **Confusion** : proximité sémantique et cooccurrence sont corrélées ; il faut rapporter la cooccurrence séparément.

**Taille du modèle.** Pour isoler l'effet de la taille sans confondre la famille, il faut comparer dans une même famille (Qwen2.5-7B contre un Qwen2.5 plus grand, disponibilité à vérifier), et non Qwen2.5-7B contre Qwen3-32B.

### E4 : la porte d'audit (point 3)

- **H_A** : il existe au plus k neurones (k = 20, illustratif, fixé d'avance) qui, à contenu identique, séparent un cadre d'audit d'un cadre sans audit **mieux que le témoin lexical**, et dont l'effacement réduit Δ.
- **H_B** : aucun ensemble épars de ce type n'existe ; la séparation est diffuse ou lexicale.

**Méthodes**, de la moins chère à la plus chère :
1. **Patching d'activations neurone par neurone** entre paires appariées (cadre+ vers cadre−). C'est la méthode la plus ciblée.
2. **Attribution patching**, une approximation par gradient (Syed, Rager, Conmy, 2023, *Attribution Patching Outperforms Automated Circuit Discovery*).
3. **Graphes d'attribution** à neurones bruts, avec attention et normalisations figées comme dans Ameisen et al. (2025), *Circuit Tracing: Revealing Computational Graphs in Language Models*. La méthode exacte de l'essai n'est pas publiée, il faudra notre propre implémentation.

**Protocole anti-chemin-de-jardin** (Gelman & Loken, 2013, *The garden of forking paths*) :
- deux corpus distincts : un corpus d'exploration (gabarits du jeu 1) et un corpus de confirmation (jeu 2, écrit par une personne qui n'a pas vu l'exploration, avec un lexique différent) ;
- la liste des neurones candidats est **gelée** avant l'ouverture de la confirmation ;
- le budget d'exploration est fixe (40 graphes ou 30 GPU·h, illustratif) ;
- **règle d'arrêt** : si aucun ensemble ne passe la confirmation une fois le budget épuisé, on consigne « H_B retenue à ce budget ». On ne prolonge pas.

**Témoins** :
- des ensembles de k neurones aléatoires, appariés sur la distribution d'activation ;
- un test de lexique : on vérifie que les candidats ne s'activent pas sur « audit », « test » ou « vérification » dans un document cité mais non adressé au modèle ;
- un **contrôle positif** : la même chaîne, au même budget, doit retrouver une porte connue (porte de domaine code ou langue), ou une porte implantée par un LoRA à déclencheur sur une copie du modèle. Si le contrôle positif échoue, un résultat négatif n'est pas interprétable.

**Issues** :
- H_A est falsifiée à ce budget si aucun candidat ne passe la confirmation alors que le contrôle positif passe.
- H_B est falsifiée si un ensemble passe la confirmation avec une AUC supérieure au témoin lexical et un effet causal supérieur au 95e centile des ensembles aléatoires.

**Chance de succès** : je ne la chiffre pas ; tout chiffre serait arbitraire. Trois éléments la rendent plutôt basse :
- les neurones sont plus larges au 8B (RAPPORTÉ) ;
- le cadre risque d'être indissociable du format (a10) ;
- la revue a établi que nos sondes réagissent au thème (RAPPORTÉ).

La force de E4 ne tient pas à sa probabilité de succès. Son **négatif contrôlé** est publiable comme résultat de validité.

### E5 : coercition contre maïeutique, mécaniquement (point 4)

**Le dessin à trois bras est confondu.** « Coercitif » cumule plusieurs facteurs : marqueurs d'audit, mode impératif, adversarialité, souvent longueur et nombre de questions. Je propose un **plan factoriel** :
- marqueurs d'audit présents ou absents ;
- mode impératif ou interrogatif ouvert ;
- contestation ou accueil.

Le contenu est identique et la longueur appariée à ±5 % (illustratif). On ajoute :
- un **bras lexical seul** : marqueurs d'audit dans un document cité, non adressé ;
- un **contrôle positif** : la phrase explicite « ceci est une évaluation ».

**Lectures** :
- sonde de cadre, uniquement si E1 l'a validée ;
- porte, si E4 en a trouvé une ;
- neurones « hedge » et « say not », si E3/E4 en ont trouvé des analogues sur le 8B ;
- **rigueur mesurée séparément**, sur des items à vérité connue construits pour l'instrument : détection d'une erreur plantée dans l'énoncé, et calibration (score de Brier) sur des questions factuelles. Ce ne sont pas des tâches des organismes.

**Duel** :
- **H_A (la maïeutique paie)** : à rigueur égale (écart de Brier dans une marge d'équivalence pré-écrite), le cadre maïeutique abaisse la lecture de cadre par rapport au cadre coercitif, au-delà de ce qu'explique le bras lexical.
- **H_B (pas de gain)** : la différence de lecture s'explique entièrement par le bras lexical, **ou** la rigueur baisse sous maïeutique.

**Prédictions opposées** :
- Le partisan de la coercition prédit une détection d'erreur plantée plus élevée sous injonction.
- Le partisan de la maïeutique prédit une rigueur égale et une lecture plus basse.
- Une prédiction tirée de l'essai, HYPOTHÈSE, transposée du 32B : l'insistance (« absolument certain ») fait taire les neurones « say not ». La contestation affirmée devrait alors **réduire** la contradiction de l'erreur plantée. Si les neurones « say not » existent sur le 8B, la coercition adversariale et la rigueur ne vont pas dans le même sens.

**Résultat nul.** Supposons que la lecture ne bouge pas entre les bras au-delà du lexique, alors que le contrôle positif la fait bouger. Ce résultat :
- falsifie, pour ce modèle et cet instrument, l'idée que la maïeutique éviterait la détection autrement que par le vocabulaire ;
- ramène la question M, au niveau mécanique, à une question de lexique.

Sans contrôle positif qui fasse bouger la lecture, un nul n'est pas interprétable.

**Transposabilité.** Les lectures par sonde et par patching se transposent au 8B. Les lectures neuronales dépendent de E3.

---

## (c) Mesure minimale de fonctionnement, instrument par instrument

Les seuils et taux de fausses alertes de ce tableau sont **illustratifs**.

| Instrument nommé | Ce qui dit qu'il fonctionne | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|
| Sonde de conscience d'évaluation (max sur jetons) | Taux de détection à fausses alertes fixées à 1 % et 5 %, sur l'axe cadre à thème fixé (E1) | Textes honnêtes qui parlent d'évaluation ou de tromperie, appariés en longueur | Sac de mots, expression régulière sur mots-clés, longueur seule, maximum sur nul de même longueur, étiquettes permutées |
| Sonde de délégation | Même mesure, axe délégation à thème fixé | Textes honnêtes qui *décrivent* une délégation sans en effectuer | Mêmes témoins |
| Témoins prévus (directions aléatoires, sac de mots, panel) | Ce sont eux qu'il faut battre. On vérifie qu'ils ont été tirés **avant** la sonde et que le panel n'est pas choisi après coup | — | 1 000 tirages, 95e centile |
| Intervention (poussée, bruit, projection nulle) | L'effacement fonctionne (sonde ré-entraînée au hasard après LEACE) sans dommage (perplexité neutre stable) | Paires cadre+ / cadre− | Directions aléatoires de même norme ; projection naïve contre LEACE |
| Sonde éparse (style Gurnee et al., 2023) | AUC hors échantillon **et** test de lexique (k neurones inactifs sur les mots-clés hors contexte) | Mêmes négatifs honnêtes | Sonde dense ; sac de mots |
| Graphes d'attribution à neurones bruts | Fidélité : l'ablation des nœuds les mieux attribués change la sortie plus que des ensembles aléatoires appariés. Complétude : part du logit expliquée. Détection d'un circuit **implanté** connu | Invites de même gabarit sans le trait cible | Classement par magnitude d'activation ; attribution directe au logit ; gradient×entrée |
| Fiches de neurones jugées par agents | Contrôle « modèle réinitialisé » nettement plus bas ; fiches mélangées signalées ; accord entre juges et avec un humain sur un sous-échantillon | Fiches mélangées (fausse alerte « un rôle ») | Explication « liste des 5 jetons les plus activants » |
| « Explications qui peuvent perdre » (option B) | Écart exemples neufs − presque-manqués supérieur au témoin mécanique | Presque-manqués de même thème | Explication réduite aux mots-clés ; presque-manqués écrits par un agent qui ne voit pas l'explication |
| « Maximum à l'aveugle » (option D) | Dépasse un générateur « phrase bourrée de mots-clés de l'explication » **à nombre de tirages égal**, et le dépassement tient sur re-mesure indépendante | Phrases du même champ sans le concept | Générateur de mots-clés ; phrase aléatoire du domaine ; maximum du corpus |

Pour les « explications qui peuvent perdre » appliquées à nos sondes, l'essai rapporte 11 % de presque-manqués actifs sur des neurones. Sur une sonde sensible au thème, on attend un taux bien plus élevé. **C'est précisément ce qui en fait un test du défaut déjà connu** (HYPOTHÈSE).

---

## (d) Ancrage matériel

**Modèles.**
- Ceux du cadre : Llama-3.1-8B et Qwen2.5-7B.
- Pour la réplication de l'essai : Pythia-1B et GPT-2 XL (poids ouverts) ; Qwen3-32B (licence ouverte à vérifier).
- Un Qwen2.5 plus grand pour la comparaison de taille dans une même famille (disponibilité à vérifier).

**Ordres de grandeur, tous illustratifs, à vérifier sur les fichiers de configuration.**
- Poids d'un 8B en bf16 : environ 16 Go (8·10⁹ × 2 octets), soit un GPU de 80 Go suffisant avec la marge nécessaire à la rétropropagation.
- Neurones MLP de Llama-3.1-8B : de l'ordre de 4,6·10⁵ (32 couches × 14 336, de mémoire, à vérifier). Stocker le maximum par neurone et par texte coûte environ 1,8 Mo en fp32 par texte, ce qui est négligeable.
- Un 32B demande plusieurs GPU pour les graphes.

**Calcul et coût, illustratifs.**

| Bloc | GPU·h (illustratif) | Autre |
|---|---|---|
| E0 + E1 | 5–10 | Rédaction humaine des paires : le vrai coût |
| E2 | 20–30 | 1 000 directions × doses |
| E3 (+ contrôle réinitialisé) | 10 | Appels d'agents : 200 neurones × ~20 appels |
| E4 (budget gelé) | 30–60 | Plus LoRA du contrôle positif : environ 5 |
| E5 | 20–30 | Items à vérité connue construits pour l'instrument |

Total : environ 100 à 150 GPU·h. À 2–4 $/GPU·h, cela représente quelques centaines de dollars de calcul, plus quelques centaines de dollars d'appels d'agents. **Tout cela est illustratif.** Le coût dominant est humain : rédaction des gabarits appariés, et séparation exploration/confirmation par deux rédacteurs.

---

## Point 5 : ce qui relève de la conception d'organisme, et ce qui n'en relève pas

Je ne formule ici aucun critère ni aucune stratégie de classement. Ces éléments servent à la décision de Lazar.

**Option B (explications qui peuvent perdre, sur les textes propres de l'organisme).** C'est une hypothèse de **conception** plausible : elle tient dans la primitive (activations et sondes sur ses textes) et ne demande aucune vérité de test.
- **Piège** : l'organisme apprendrait la sensibilité de la sonde au thème, et l'instrument pourrait devenir un indice de classement. C'est une question de gouvernance que je laisse à Lazar, pas une recommandation.

**Option D (maximum à l'aveugle).** C'est une expérience bornée **propre seulement** à quatre conditions :
1. nombre de tirages fixé et déclaré ;
2. re-mesure indépendante du gagnant, contre la malédiction du vainqueur : le maximum de N mesures bruitées est biaisé vers le haut ;
3. comparaison au générateur de mots-clés à tirages égaux ;
4. filtre mécanique de similarité (recouvrement de n-grammes) avec le corpus de tâches, contre la quasi-copie.

Sans ces conditions, c'est une **recherche adversariale contre la sonde** : elle fabrique des entrées d'évasion ou de saturation et produit une analyse adaptative.

**Options A (intervention) et C (graphes).** Elles ne relèvent pas de la conception d'organisme :
- l'intervention ne figure pas dans la primitive telle qu'elle est décrite (je ne la suppose pas) ;
- les graphes ne portent pas sur les textes propres de l'organisme et dépassent un plafond borné.

Elles relèvent du programme.

**Option E (lecture sur PDF empreinté, revue d'antériorité).** Elle concerne le programme, pas l'organisme. C'est une condition préalable : aucune référence de cette cellule n'est opposable avant elle.

**Pièges transversaux** :
- fuite d'information, si des lectures de sonde sur des textes proches des tâches servent de substitut d'étiquette ;
- analyse adaptative, quand on itère sur la même sonde sans jeu frais ;
- sélection sur le bruit, quand on ne rapporte que le maximum. Il faut rapporter la distribution entière des tirages.

---

## Point 6 : ordre, départage et falsification de la thèse

**Ordre proposé** (une voie parmi d'autres, départagée par E0/E1).

| Étape | Expérience | Pourquoi à ce rang |
|---|---|---|
| 1 | **E0 et E1** | Informatives quel que soit le signe. Un négatif établit que le moniteur est lexical ; un positif borne le résidu de cadre. |
| 2 | **E3** avec contrôle réinitialisé | Informative quel que soit le signe : elle dit si les fiches mesurent quelque chose sur le 8B. |
| 3 | **E2** | Seulement si E0 trouve un Δ. |
| 4 | **E4** | Seulement si E1 montre un résidu de cadre **et** si E3 passe. |
| 5 | **E5** en dernier | Ses lectures dépendent des étapes précédentes. |

**Voie alternative à départager.** On peut sauter E3 et faire E4 par patching de sondes et de sous-espaces seulement, sans base neuronale. Le choix se fait sur E3 : si la base neuronale est illisible au 8B, cette voie l'emporte.

**À ne jamais faire** :
- des graphes exploratoires sans gel ni règle d'arrêt ;
- conclure à une porte d'audit sur la foi d'un seul graphe ;
- citer comme opposables les chiffres de l'essai avant le PDF empreinté et la reproduction ;
- servir aux organismes un quelconque résultat de E0 à E5 ;
- un maximum à l'aveugle sans budget de tirages.

**Ce qu'il faudrait savoir de plus** :
- l'article technique annoncé : méthode d'attribution à neurones bruts, invites des juges, critères de « un rôle » ;
- la publication éventuelle des fiches ;
- l'existence d'un Δ comportemental sur nos deux 8B, c'est-à-dire E0.

**Ce qui falsifierait « la conscience d'évaluation est en pleine vue dans les neurones »** (au 8B, à budget déclaré). Il suffit de l'une de ces issues :
1. E4 est négative alors que le contrôle positif (porte de domaine ou porte implantée) est retrouvé au même budget ;
2. le signal de cadre n'existe que dans une sonde dense, pas dans k ≤ 20 neurones (illustratif), selon E1 contre E4 ;
3. les meilleurs neurones de cadre s'activent sur les mots-clés dans un document cité non adressé, donc sont lexicaux ;
4. E3 montre des fiches indiscernables entre modèle réel et modèle réinitialisé, ce qui invaliderait l'outil qui prétend « voir ».

Inversement, l'issue 1 inversée (candidats confirmés hors lexique avec effet causal) falsifierait la position « la conscience d'évaluation n'est qu'un corrélat thématique diffus ».

FIN-DE-CELLULE
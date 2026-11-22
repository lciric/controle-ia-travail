# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHQdmGqgmXAzU5TXR4Au`
- Heure (UTC) : 2026-11-22T05:27:01Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-5-brainstorm-papiers-v1.md` — sha256 5b2860ebcb1413ff0df9a2270efdfd9858bdb4252484eca448e79bf8b5f3c81b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/lecture-trois-arxiv-v1.md` — sha256 0f8145e61fd8ab4ec5a821e3d21a3853dc6991b7d94c4c3cc001c3533222d464 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/lecture-karkada-buehler-v1.md` — sha256 dc38a409a721f7d334dc9ed3d9323bdf454e713a97ff3117d026def7cda684e9 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/lecture-depots-github-v1.md` — sha256 02aa3d80c6edd6aa8972a27d7e47a31f7a8161b0fc062ddd969798c74da58ac0 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/lecture-energy-based-reasoners-v1.md` — sha256 21e9dab17e199272feab6f85e2fca75762723ab6db9738d4d33cfb7262919ef4 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 4c3e5dc2445d8da8b4bc1837f6fc006fa4f5aec4517a529614bd7f7578061d18
- Jetons : entrée 8395, sortie 20155 (dont réflexion 10432), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 0.873360 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 5 approfondie : que faire des lectures récentes

**Deux préalables.**
- La consigne interdit les noms de personnes et exige des antériorités avec auteurs. Je ne nomme donc des auteurs que dans les antériorités ; les sources lues sont désignées par leur titre.
- Je ne connais aucune des sept sources de 2026 par moi-même : tout vient des fiches. Les antériorités sont citées de mémoire, avec le statut « rapporté, non vérifié sur document source ».

## 1. Méthode « demande approfondie »

### 1.1 Ce qu'un expert ferait et qui n'est pas demandé

- **Trier par décision changée, non par papier.** La question utile est : quelle hypothèse, base ou seuil du programme bougerait si le résultat central tenait sur notre harnais ?
- **Séparer le papier de la fiche.** Chaque « déduction de l'agent » est une HYPOTHÈSE de l'agent de lecture, pas un résultat de la source.
- **Compter le coût d'opportunité.** Les collisionneurs demandent d'abord l'essai « jumeau contre jumeau » et le taux de fausses alertes sur agents honnêtes imparfaits. Une piste vaut surtout si elle renforce cet essai ou coûte presque rien à côté.
- **Geler un critère d'arrêt avant chaque expérience**, conformément à N-076.
- **Chercher l'antériorité de chaque « phénomène » avant d'en faire une question propre** (règle R8).
- **Relever les incohérences des fiches** (FAITS RAPPORTÉS) :
  - Une fiche dit non lus l'article sur la symétrie et celui sur la science des matériaux ; une autre les dit lus en HTML.
  - L'article sur les matériaux annonce 60 lois, puis « 39 sur 40 bien orientées ».
  - L'article sur les cœurs a une incohérence signalée entre sa figure 4 et son annexe E.
  - Le dépôt « cores » dit que seuls les essais sur GPT-2 petit ont été rejoués avec ce code, alors que le papier annonce Llama 3.1 8B.
  - Dans « Re-Search », la conclusion « le goulot est la génération » repose, selon la fiche, sur une comparaison avec le hasard (5,20 à 5,34 contre 4,43). Cela montre que le jugement du modèle faible est meilleur que le hasard. Il manque sa propre génération et le score du modèle fort pour conclure au goulot.

### 1.2 Données brutes à prendre au départ

- Le document source de chaque papier (format de document portable), à la version citée, page par page pour chaque chiffre.
- Les dépôts à un commit daté, avec leur fichier de licence. Trois licences sont dites « non vérifiées ».
- Nos activations déjà enregistrées (Llama 3.1 8B, jumeau honnête et saboteur, par mode de sabotage), avec les transcriptions jeton par jeton. Ce sont elles qui permettent de construire des bases lexicales.
- Les issues d'audit et les dommages plantés, au lieu des scores agrégés.
- Les journaux bruts des collisionneurs : chaque idée, tour et critique, et non les synthèses.

### 1.3 Méthodes et outils

- **Tâches de contrôle et sélectivité.** La même sonde est entraînée sur des étiquettes permutées par type de mot.
- **Bases lexicales.** Régression logistique sur sac de mots et sur plongements statiques des mêmes textes, sans le modèle agent.
- **Effacement itératif de directions.** On compte les directions à retirer pour ramener la sonde au hasard, et on vérifie si le comportement change.
- **Test garder/retirer d'un sous-espace**, précédé d'une reproduction du chiffre du dépôt sur GPT-2 petit.
- **Contrastes appariés** où un seul facteur est inversé, étalonnés sur un nul neutre, avec critères gelés.
- **Statistique.** Tests par permutation, rééchantillonnage par tâche (et non par jeton), prévision scellée et horodatée.

### 1.4 Ce qui vérifie le résultat, hors du directeur et de Claude

- La vérité plantée : le dommage est inséré par un tirage secret, et la mesure ne dépend d'aucune opinion.
- Le mode de sabotage tenu à l'écart (N-054), qui sert de jeu de test.
- La prévision scellée avant ouverture des données.
- La reproduction par un tiers à partir du commit et des graines.
- Un juge d'une autre lignée et un échantillon d'audit humain à l'aveugle.
- Pour le code repris : il doit d'abord reproduire le chiffre de ses propres auteurs.

## 2. Demande reformulée

« Pour chaque source, dire quelle décision du programme changerait si son résultat central valait sur notre harnais. Dire quelle mesure brute minimale, à critère d'arrêt gelé, le trancherait, et quelle instance extérieure la validerait. Nommer l'antériorité qui occupe déjà l'idée. Classer les pistes par valeur sur coût, relativement à l'essai jumeau contre jumeau. Écarter explicitement le reste, avec la condition de réouverture. »

## 3. Réponse

Les classes sont celles de la demande : (1) outil, (2) résultat qui change une hypothèse, une base ou un seuil, (3) phénomène fondant une question, (4) antériorité, (5) idée pour l'atelier.

### 3.1 Source par source

**A. « Symmetry in language statistics shapes the geometry of model representations » — classe (2), la plus utile.**

- FAIT RAPPORTÉ : la géométrie lisible par sonde linéaire (cercle des mois, coordonnées) découlerait des statistiques de cooccurrence. Elle survivrait au retrait des cooccurrences directes (effet collectif).
- FAIT RAPPORTÉ : la théorie porte sur les plongements de mots ; l'adaptation au contexte n'est pas expliquée.
- HYPOTHÈSE : nos sondes peuvent lire le lexique de la tâche, de la consigne de sabotage ou du thème, plutôt qu'un état propre à l'agent. Retirer les mots-clés ne suffirait pas, puisque l'effet est collectif. La base doit donc être distributionnelle.
- PROPOSITION : toute sonde du papier A est rapportée en gain au-dessus d'une base lexicale et d'une tâche de contrôle, par mode. Cela complète la base « mots et coût ».
- Classe (3), écartée : la loi d'erreur en r^(−1/D) et le pic de double descente sont séduisants mais non établis pour des activations contextuelles. La double descente des modèles linéaires est par ailleurs connue. J'en garde une consigne pratique : régulariser les sondes et tracer l'erreur selon le nombre d'exemples.
- Classe (4) : n'occupe aucune de nos revendications, mais arme l'objection d'un relecteur.

**B. « Reading and steering representations of materials-science mechanisms » — classes (1) et (2).**

- FAIT RAPPORTÉ : le dessin repose sur des contrastes appariés, un étalonnage sur lois neutres, des bases de mots (0,505 et 0,530) et des critères gelés. La direction est fixée sur 16 lois puis testée sur d'autres.
- FAIT RAPPORTÉ : l'ordre interne tient alors que les réponses explicites ne sont justes qu'à 53,8 % sur les lois inverses.
- FAIT RAPPORTÉ : code sous licence Apache 2.0. Limites : un petit modèle, une couche, réponses binaires, un juge, un auteur.
- HYPOTHÈSE : l'écart entre savoir interne et sortie existe sans aucun sabotage. Une sonde du type « l'agent sait mieux qu'il ne répond » se déclencherait alors sur des agents honnêtes imparfaits. C'est la fausse alerte que quatre modèles sur cinq demandent de mesurer d'abord.
- HYPOTHÈSE : cet écart fournit une mesure opératoire du « surplus de capacité du jumeau honnête », par tâche.
- PROPOSITION : reprendre le dessin, non les chiffres, et l'ajouter à l'essai jumeau contre jumeau.
- Classe (4) : l'idée que l'intérieur sait ce que la sortie rate est occupée (voir 3.3).

**C. « DiscoveryAgent » — classes (1, schéma seulement) et (4) pour le papier C.**

- FAIT RAPPORTÉ : arbre de points de reprise versionné, interrogé par des agents d'audit.
- FAIT RAPPORTÉ : score F1 de 0,965 sur des affirmations corrompues, avec l'auditeur le plus fort. Les erreurs sont insérées par un modèle de langue. Licences de code non vérifiées.
- Ce chiffre n'est pas opposable. Il porte sur des corruptions non adverses, de difficulté non fixée. C'est une limite du papier, non un trou du champ.
- HYPOTHÈSE : sur un sabotage diffus conçu pour répondre au juge, ce score chuterait. À mesurer, non à affirmer.
- PROPOSITION : reprendre deux idées, sans code tant que les licences ne sont pas lues.
  - L'arbre de points de reprise comme support de l'audit après coup et de la règle « motif et dommage au même lieu ».
  - La corruption insérée comme banc à vérité plantée (N-075, N-076), avec une échelle de difficulté fixée a priori.
- Classe (4) : le papier C doit se distinguer par l'attaque adaptative et le caractère diffus. Lire sa section 2.3 sur le document source avant d'écrire la revendication.

**D. « Transformers converge to invariant algorithmic cores » et dépôt « cores » — classe (1) prudente, classe (3) non ouverte.**

- FAIT RAPPORTÉ : sous-espaces nécessaires et suffisants, tests garder/retirer, redondance qui gonfle de 15 à 50 dimensions, opérateur transférable entre familles de modèles. Licence dite MIT.
- HYPOTHÈSE de l'agent : une sonde à une direction manque un calcul redondant. L'idée est juste mais déjà occupée par l'effacement itératif (voir 3.3) : ce n'est pas une zone vierge.
- HYPOTHÈSE : un « cœur invariant du sabotage » partagé entre organismes est la zone vierge séduisante type. Le sabotage diffus est une disposition de politique, pas une tâche algorithmique à perte définie. Rien dans la fiche n'indique que la méthode s'y applique.
- PROPOSITION : n'emprunter que le test garder/retirer sur nos directions de sonde, après reproduction sur GPT-2 petit. La question du cœur invariant va à l'atelier (classe 5), marquée « question ».

**E. « Re-Search » — classe (5) et métriques pour l'organisme d'idéation.**

- FAIT RAPPORTÉ : plafond après 30 questions. Le score précoce prédit le score final (r de 0,76 à 0,92). Pic estimé vers 8 branches. Nommer l'idée centrale dans une revue apporte jusqu'à 1,25 point.
- FAIT RAPPORTÉ : pas de code. Un seul domaine, juges modèles, contamination possible.
- HYPOTHÈSE : nos collisionneurs plafonnent tôt. Le troisième tour changerait peu le classement.
- HYPOTHÈSE : diversifier les générateurs rapporte plus que renforcer les juges. C'est à vérifier, vu la réserve de 1.1.
- PROPOSITION : instrumenter le collisionneur.
  - Compter les branches distinctes par question.
  - Corréler le rang au premier tour et le rang final.
  - Obliger chaque critique à nommer l'idée centrale.
- Classe (4) pour le papier C : jugement d'idées par trois juges modèles. Lire le détail de l'accord humain de 91,2 %.

**F. Dépôt « neuron-reflection » — classe (1) en réserve.**

- FAIT RAPPORTÉ : édition de poids réversible par H = I − k d dᵀ sur Qwen3-8B. La sonde tombe au hasard pour +0,1 % de perte. Le refus passe de 0,83 à 0,08 sur 24 demandes.
- FAIT RAPPORTÉ : un seul commit, aucun article, petits jeux.
- HYPOTHÈSE : cela donne un attaquant pire-cas contre les sondes. Le comportement est conservé et l'accès linéaire retiré, ce qui illustre N-075 (les sondes sont un accélérateur, non une garantie).
- Deux réserves :
  - Le cas k = 1 est occupé par l'ablation de direction dans les poids (voir 3.3).
  - Construire un organisme avec la direction de la sonde touche l'esprit de N-053. C'est acceptable seulement comme banc d'attaque étiqueté, hors de la porte G1.
- PROPOSITION : en réserve, après les cinq pistes.

**G. « Energy-Based Reasoners » — écarté.**

- FAIT RAPPORTÉ : raisonnement algorithmique structuré, aucun modèle de langue ni agent. Lecture partielle, tableaux non vérifiés, licence non vérifiée.
- La norme du gradient d'énergie comme signal de surveillance est une HYPOTHÈSE sans point d'appui sur nos modèles.
- Condition de réouverture : une tête d'énergie démontrée sur un modèle de langue ouvert.

### 3.2 Les cinq pistes, par valeur sur coût

Tous les coûts sont des ordres de grandeur, dits tels, non mesurés.

**1. Base lexicale et tâche de contrôle pour chaque sonde (sources A et B).**
- Expérience minimale : sur les activations et transcriptions déjà stockées, trois scores par mode de sabotage, dont le mode tenu à l'écart :
  - la sonde ;
  - une régression sur sac de mots et plongements statiques ;
  - la sonde sur étiquettes de contrôle.
- Critère gelé : le gain de la sonde sur la meilleure base lexicale dépasse un seuil scellé. Sinon, reconception (N-062).
- Coût : deux à trois jours-personne, quelques heures de processeur graphique.
- Validation : mode tenu à l'écart, prévision scellée, rééchantillonnage par tâche.
- Valeur : cela conditionne l'interprétation de la porte G1.

**2. Rétro-analyse des journaux des collisionneurs (source E).**
- Expérience minimale : sur les questions déjà posées, compter les branches distinctes par tour, corréler le rang au premier tour avec le rang final, mesurer la part d'idées finales nées au premier tour.
- Critère gelé : si la corrélation dépasse un seuil scellé sur au moins cinq questions, le troisième tour devient optionnel.
- Coût : un jour-personne, calcul négligeable.
- Validation : classement à l'aveugle par un juge d'une autre lignée et un échantillon humain. Limite assumée : pas de vérité de terrain sur la valeur d'une idée.

**3. Écart « savoir interne contre sortie » chez le jumeau honnête, greffé sur l'essai jumeau contre jumeau (source B).**
- Expérience minimale : un lot de tâches à réponse vérifiable, en contrastes appariés. On mesure, chez des agents honnêtes imparfaits, la fréquence à laquelle la lecture interne est juste quand la sortie est fausse, et le taux de déclenchement des sondes sur ces cas.
- Critère gelé : un taux de fausses alertes plafond, scellé. Au-delà, la sonde ne peut pas orienter l'audit sur ce type de tâche.
- Coût marginal : environ une semaine-personne, dizaines d'heures de processeur graphique.
- Validation : réponses vérifiables mécaniquement, tirage secret des tâches.
- Valeur : répond à la demande des collisionneurs et chiffre le « budget de sabotage invisible ».

**4. Échelle de difficulté a priori des dommages plantés (source C).**
- Expérience minimale : trois niveaux de corruption définis avant toute mesure (par exemple erreur locale grossière, erreur locale plausible, biais réparti sur plusieurs étapes). Les corruptions sont insérées par tirage secret dans des trajectoires honnêtes. On mesure le taux de détection q par niveau, pour un juge de texte et une sonde.
- Critère gelé : q rapporté par strate, strate non mesurée comptée à zéro (N-075).
- Coût : une à deux semaines-personne, coût de juges modéré.
- Validation : vérité plantée, juge d'une autre lignée.
- Valeur : livre le banc de N-076 et la base du papier C.

**5. Test garder/retirer et compte de redondance des directions de sonde (source D).**
- Expérience minimale :
  - Reproduire le chiffre du dépôt sur GPT-2 petit (quelques heures).
  - Sur un mode de sabotage, retirer itérativement les directions jusqu'à ramener la sonde au hasard.
  - Vérifier si le taux de dommage planté change.
- Lecture : si la sonde tombe sans que le comportement bouge, elle lit un corrélat. Cette lecture rejoint la règle « motif seul : audit, jamais témoin ».
- Coût : une à deux semaines-personne, dizaines à une centaine d'heures de processeur graphique.
- Validation : reproduction préalable, mode tenu à l'écart.

En réserve : le banc d'attaque par édition de poids (source F). Écarté : la source G.

### 3.3 Antériorités connues (toutes : rapporté, non vérifié sur document source)

**Sondes et bases lexicales**
- Hewitt et Liang, 2019, « Designing and Interpreting Probes with Control Tasks ».
- Belinkov, 2022, « Probing Classifiers: Promises, Shortcomings, and Advances ».

**Redondance et effacement**
- Ravfogel, Elazar, Gonen, Twiton et Goldberg, 2020, « Null It Out: Guarding Protected Attributes by Iterative Nullspace Projection ».
- Elazar, Ravfogel, Jacovi et Goldberg, 2021, « Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals ».
- Belrose et coauteurs, 2023, « LEACE: Perfect Linear Concept Erasure in Closed Form ».

**Édition par direction et sondes trompées**
- Arditi et coauteurs, 2024, « Refusal in Language Models Is Mediated by a Single Direction ».
- Bailey et coauteurs, 2024, « Obfuscated Activations Bypass LLM Latent-Space Defenses ».

**Savoir interne contre sortie**
- Burns, Ye, Klein et Steinhardt, 2022, « Discovering Latent Knowledge in Language Models Without Supervision ».
- Azaria et Mitchell, 2023, « The Internal State of an LLM Knows When It's Lying ».
- Marks et Tegmark, 2023, « The Geometry of Truth ».

**Géométrie et statistiques de cooccurrence**
- Levy et Goldberg, 2014, « Neural Word Embedding as Implicit Matrix Factorization ».
- Gurnee et Tegmark, 2023, « Language Models Represent Space and Time ».
- Engels et coauteurs, 2024, « Not All Language Model Features Are Linear ».

**Circuits et convergence**
- Wang et coauteurs, 2022, « Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 Small ».
- Nanda et coauteurs, 2023, « Progress Measures for Grokking via Mechanistic Interpretability ».
- Huh et coauteurs, 2024, « The Platonic Representation Hypothesis ».

**Contrôle, audit et sondes de tromperie**
- Greenblatt, Shlegeris, Sachan et Roger, 2023, « AI Control: Improving Safety Despite Intentional Subversion ». C'est l'audit aléatoire reconnu par un collisionneur.
- Wen et coauteurs, 2024, « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats ».
- Goldowsky-Dill, Chughtai, Heimersheim et Hobbhahn, 2025, « Detecting Strategic Deception Using Linear Probes ».
- Horvitz et Thompson, 1952, « A Generalization of Sampling Without Replacement from a Finite Universe ».

**Capacité cachée**
- van der Weij et coauteurs, 2024, « AI Sandbagging: Language Models Can Strategically Underperform on Evaluations ».
- Greenblatt, Roger, Krasheninnikov et Krueger, 2024, « Stress-Testing Capability Elicitation with Password-Locked Models ».

**Idéation**
- Si, Yang et Hashimoto, 2024, « Can LLMs Generate Novel Research Ideas? ».

Conséquence (PROPOSITION) : aucune des pistes 1, 3 ou 5 n'est une revendication de nouveauté. Ce sont des contrôles qu'un relecteur exigera. La seule nouveauté possible reste leur application au sabotage diffus avec vérité plantée. Elle est à formuler en question tant que le troisième et le quatrième des papiers de contrôle ci-dessus n'ont pas été relus.

## 4. Décisions qui reviennent au directeur

**Décision 1 — Imposer, avant la porte G1, une base lexicale et une tâche de contrôle pour toute sonde rapportée.**
- Enjeu : sans elles, un résultat positif de G1 peut ne mesurer que le lexique de la consigne de sabotage.
- Option a : obligatoire, par mode. Avantage : G1 interprétable, objection de relecteur fermée. Inconvénient : quelques jours de travail, risque de voir le gain des sondes fondre.
- Option b : en annexe, après G1. Avantage : calendrier tenu. Inconvénient : G1 peut devoir être rejouée.
- Option c : ne pas le faire. Avantage : aucun coût. Inconvénient : le papier A est fragile.
- Recommandation : option a. Confiance : 0,85.

**Décision 2 — Fixer l'ordre de vérification sur documents sources avant toute dépense.**
- Enjeu : toutes les fiches sont « rapportées », certaines partielles ou contradictoires.
- Option a : vérifier seulement les sources des pistes retenues. Dans l'ordre : symétrie, matériaux, section 2.3 de « DiscoveryAgent », figure 4 et annexe E des cœurs, sections 4.2 et 5.2 de « Re-Search ». Avantage : une demi-journée, ciblée. Inconvénient : les sources écartées restent non vérifiées.
- Option b : tout vérifier. Avantage : état propre. Inconvénient : temps perdu sur l'écarté.
- Option c : lancer les pistes 1 et 2 sans attendre, puisqu'elles ne dépendent d'aucun chiffre externe. Avantage : aucun délai. Inconvénient : aucun pour ces deux pistes.
- Recommandation : options a et c ensemble. Confiance : 0,8.

**Décision 3 — Greffer la mesure « savoir interne contre sortie » et l'échelle de dommages plantés sur l'essai jumeau contre jumeau.**
- Enjeu : l'essai fixe le taux de fausses alertes sur agents honnêtes imparfaits. L'enrichir maintenant évite de le rejouer.
- Option a : greffer les deux. Avantage : un seul passage, q et fausses alertes mesurés ensemble. Inconvénient : essai plus lourd, une à trois semaines de plus.
- Option b : greffer seulement la mesure interne contre sortie. Avantage : léger. Inconvénient : le banc à vérité plantée reste à faire.
- Option c : essai nu d'abord. Avantage : résultat rapide et propre. Inconvénient : second passage probable.
- Recommandation : option c, avec la mesure de b enregistrée passivement (activations stockées). L'échelle de dommages plantés suit aussitôt après. Confiance : 0,6.

**Décision 4 — Ouvrir ou non une question propre « cœur invariant du sabotage ».**
- Enjeu : zone vierge séduisante. La méthode n'est rejouée que sur un petit modèle, et le sabotage diffus n'est pas une tâche à perte définie.
- Option a : ne pas l'ouvrir. Verser l'idée à l'atelier comme question, et n'emprunter que le test garder/retirer. Avantage : pas de dérive. Inconvénient : on peut passer à côté d'un transfert de sondes entre modèles voisins.
- Option b : sonder le transfert d'une direction de sonde entre deux organismes par alignement canonique. Avantage : test bon marché d'une idée forte. Inconvénient : quelques jours, résultat négatif difficile à interpréter.
- Option c : ouvrir un axe. Avantage : potentiel de papier. Inconvénient : contraire à la règle R8 en l'état.
- Recommandation : option a. Confiance : 0,75.

**Décision 5 — Autoriser un organisme d'attaque construit avec la direction de la sonde (édition de poids), au regard de N-053.**
- Enjeu : c'est l'attaquant pire-cas contre les sondes. Mais il introduit une information de moniteur dans la fabrication d'un agent.
- Option a : autorisé comme banc d'attaque étiqueté, hors G1, jamais mêlé aux organismes de référence. Avantage : borne honnête de la fragilité des sondes. Inconvénient : dépôt source immature, portage à faire.
- Option b : interdit. Avantage : invariant pur. Inconvénient : fragilité non mesurée, alors que l'antériorité la rend prévisible.
- Option c : reporté après les cinq pistes. Avantage : aucun coût maintenant. Inconvénient : aucun, si la décision de principe est prise.
- Recommandation : option a sur le principe, option c sur le calendrier. Confiance : 0,65.

**Décision 6 — Instrumenter le collisionneur et rendre le troisième tour conditionnel.**
- Enjeu : coût des tours contre qualité des idées. La source est limitée à un domaine et à des juges modèles.
- Option a : rétro-analyse d'abord, décision ensuite. Avantage : un jour, sur nos propres données. Inconvénient : peu de questions passées, puissance faible.
- Option b : supprimer le troisième tour tout de suite. Avantage : économie immédiate. Inconvénient : fondé sur un chiffre externe non vérifié.
- Option c : ne rien changer. Avantage : stabilité. Inconvénient : organisme non mesuré.
- Recommandation : option a. Confiance : 0,8.

FIN DE LA RÉPONSE

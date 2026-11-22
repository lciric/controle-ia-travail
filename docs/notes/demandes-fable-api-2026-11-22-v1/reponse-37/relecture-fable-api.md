# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHyqJRUdXUbviA8i3NKP`
- Heure (UTC) : 2026-11-22T12:45:18Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 106000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-37-validite-externe-v1.md` — sha256 4df11871a0621a69b243a11476d01c4a93286f84cfb56d45cc933981c64d644c (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-28-effort-max/relecture-fable-api.md` — sha256 1261c8eeb9f00711ec3a5e8a7438bb3c26ec5d04d6af342ceaa7ec766daa52b4 (compagnon : vérifié)
- Empreinte de l'invite envoyée : e5e1e00ded19e811c7779b2f27f748e73019ec74ead1005ab0a1a6279ea50058
- Jetons : entrée 11331, sortie 39055 (dont réflexion 30082), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.652848 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 37 — validité externe : réponse par la méthode « demande approfondie »

**Conventions.** Chaque affirmation est marquée FAIT RAPPORTÉ, HYPOTHÈSE ou PROPOSITION, à l'échelle de la phrase ou du paragraphe. Toute antériorité a le statut « rapporté, non vérifié sur PDF » (fichier de l'article non relu). La certitude (élevée, moyenne) porte sur l'existence de la référence et le sens de son résultat. Aucun chiffre publié n'est repris. Seuls des auteurs d'antériorités sont nommés. Les titres sont cités tels quels : leurs sigles désignent les grands modèles de langue (LLM) et l'intelligence artificielle (AI).

## A. Les quatre points préalables

**1. Ce qu'un expert ferait et qui n'est pas demandé** (PROPOSITIONS).

- Écrire l'énoncé à transporter avant de choisir une épreuve : quelles unités (des mondes, des problèmes), quel traitement (l'organisme contre sa meilleure base), quel résultat, quel cadre.
- Séparer trois décalages : des mondes (plantés, puis réels), du résultat (retrouver un puits, puis trouver une question féconde), du temps (avant, puis après la date de coupure). Les trois idées du directeur ne répondent pas au même décalage.
- Lister les modérateurs de l'effet (structure exploitée, largeur, profondeur, coût de vérification, présence dans le corpus d'entraînement) et les mesurer sur des cas réels avant toute pondération.
- Retourner la pondération : construire le banc à l'image de la cible plutôt que corriger après coup.
- Étalonner chaque épreuve sur des cas à réponse connue avant de s'en servir.
- Demander si un résultat récent publié est bien un « puits étroit » : des humains l'ont trouvé.
- Sceller une réserve d'items que le réglage de la méthode ne touche jamais.

**2. Données brutes de départ** (PROPOSITION).

- Historique complet des versions de chaque texte cible : première prépublication datée, non la version de revue ; traces antérieures (exposés, thèses, dépôts de code).
- Instantané daté d'une archive ouverte, extrait par une règle écrite.
- Fichiers de poids de modèles ouverts, avec empreinte et date de dépôt ; dates de coupure déclarées par les fournisseurs ; sorties brutes des sondes.
- Registres de protocoles préenregistrés dont l'issue est parue après la coupure : l'hypothèse est datée avant, l'issue est mécanique.
- Toutes les idées brutes de chaque bras avant tout tri, journaux d'exécution, données fraîches.
- Traits des mondes plantés et des cas réels, codés par un tiers aveugle.

**3. Méthodes et outils** (PROPOSITION, détail en C).

- Cadre « unités, traitements, résultats, cadres ».
- Stratification, post-stratification, diagnostic de recouvrement, bornes d'identification partielle.
- Essai randomisé d'idées, aveugle, à budget fixe.
- Parade d'identification avec leurres et nul par permutation.
- Sondes de contamination ; machine sans réseau ; base figée par empreinte.

**4. Vérification hors du directeur et du modèle qui répond** (PROPOSITION).

- L'antériorité prouvée d'un fichier de poids sur le résultat à retrouver.
- Le dépôt horodaté, chez un tiers, des protocoles, des grilles et des clés avant toute course.
- Un tiers qui choisit les cibles et construit la base.
- Des juges aveugles dont le taux de fausse reconnaissance est mesuré sur leurres.
- Des issues mécaniques sur données fraîches, et la réplication par un tiers d'un échantillon tiré au sort.
- La publication du banc, rejouable.

## B. Demande reformulée

« Écrire l'énoncé causal que le banc de mondes plantés établit et la population de problèmes réels vers laquelle on veut le transporter.
(a) Dire quelles hypothèses rendraient une pondération licite, les diagnostiquer sur des modérateurs mesurés dans des cas réels, et remplacer la correction après coup par un plan stratifié.
(b) Concevoir un essai randomisé, aveugle et préenregistré d'idées exécutées par nous, à issue mécanique.
(c) Concevoir une épreuve de rétrodiction sur des résultats dont la première trace publique est postérieure à des poids horodatés, avec base servie par règle, sans réseau, et reconnaissance mesurée contre leurres.
(d) Pour chaque épreuve, écrire d'avance la phrase qu'elle autorise, celle qu'elle interdit et le résultat qui la réfuterait. »

## C. Réponse

### 1. Validité externe et généralisation hors distribution

**Réponse courte** (HYPOTHÈSE d'analyse) : même squelette, autre objet. Dans les deux cas, une grandeur estimée sous une loi sert sous une autre, et le rapport des densités fait le pont. C'est l'échantillonnage préférentiel de la réponse 28.

**Ce qui est commun** (FAITS RAPPORTÉS).

- Shimodaira, 2000, *Improving predictive inference under covariate shift by weighting the log-likelihood function* (élevée) : si seule la loi des entrées change, repondérer par le rapport des densités corrige le risque.
- Sugiyama, Suzuki et Kanamori, 2012, *Density Ratio Estimation in Machine Learning* (élevée) : estimation directe de ce rapport.
- Stuart et collaborateurs, 2011, *The use of propensity scores to assess the generalizability of results from randomized trials* (élevée) : même pondération pour porter l'effet d'un essai vers une population cible.
- Pearl et Bareinboim, 2011, *Transportability of Causal and Statistical Relations: A Formal Approach* (élevée) : conditions sous lesquelles un effet se transporte.

**Ce qui distingue** (HYPOTHÈSES d'analyse).

- L'unité est un monde ou un problème, non un exemple : on en aura des dizaines, non des millions.
- La grandeur est un effet causal apparié (organisme moins base), non le risque d'un prédicteur.
- La validité externe couvre aussi le traitement et le résultat (Shadish, Cook et Campbell, 2002, *Experimental and Quasi-Experimental Designs for Generalized Causal Inference*, élevée ; Egami et Hartman, 2023, *Elements of External Validity: Framework, Design, and Analysis*, moyenne).
- Or, hors du banc, le traitement change (le juge n'a plus de tirages frais) et le résultat aussi (la fécondité n'est pas la récupération).

**Hypothèses requises pour pondérer** (FAIT RAPPORTÉ, résultats classiques) :

1. tous les modérateurs de l'effet sont mesurés des deux côtés ;
2. recouvrement : tout type de problème réel a un homologue parmi les mondes plantés ;
3. on dispose d'un échantillon de la cible, donc d'une liste où le tirer ;
4. le résultat mesuré est le même des deux côtés.

**Où cela échoue ici** (HYPOTHÈSES).

- Hypothèse 3 : il n'existe pas de liste des « questions de recherche réelles ».
- Hypothèse 2 : un problème inexprimable dans la grammaire a un rapport de densités infini ; aucun poids ne crée un support absent.
- Hypothèse 1 : la structure qui décide du gain est justement ce qu'on ignore du réel.
- Hypothèse 4 : la pondération corrige un décalage d'unités, jamais un changement de construit.
- Avec peu de mondes, quelques poids extrêmes effondrent la taille effective de l'échantillon.
- Même chez elles, les méthodes voisines sont fragiles : Gulrajani et Lopez-Paz, 2021, *In Search of Lost Generalization* (élevée), rapportent qu'évaluées avec soin, les méthodes de généralisation entre domaines ne battent pas nettement l'apprentissage ordinaire.

**Ce qu'on peut en garder** (PROPOSITION).

- Un plan représentatif (Brunswik, 1956, *Perception and the Representative Design of Psychological Experiments*, élevée) : mesurer les modérateurs sur un échantillon de cas réels, puis tirer les mondes plantés dans ces strates.
- Rapporter l'effet par strate, le pire cas et une courbe de sensibilité au mélange des strates, non un chiffre pondéré unique.
- Hors support, donner des bornes (Manski, 1990, *Nonparametric Bounds on Treatment Effects*, élevée) ou se taire.
- Faire de la pondération une prédiction réfutable : à partir du banc et des modérateurs, annoncer sous scellé sur quels items réels l'organisme gagnera, puis le vérifier par les épreuves 2 et 3.
- Deux usages sont licites sans réserve, car la liste existe et le tirage est à nous : repondérer l'échantillon de résultats récents vers une population de publications définie, et repondérer les idées exécutées vers l'ensemble des idées produites.

### 2. L'épreuve par nos propres expériences

FAIT RAPPORTÉ (lecture de la réponse 28) : c'est la forme rapide des « prédictions scellées que l'expérience tranche ». Le directeur a raison de ne pas attendre.

**Idées qui s'y prêtent** (PROPOSITION) :

- issue décidable par un test mécanique sur données fraîches ;
- exécution bornée, en heures de calcul plutôt qu'en semaines de personne ;
- protocole exécutable par un tiers sans dialogue avec l'auteur ;
- prédiction discriminante.

D'après la réponse 28, les mécanismes de contrôle et les modes d'attaque y entrent ; les questions de recherche larges, non.

**Antériorités** (FAITS RAPPORTÉS).

- Si, Hashimoto et Yang, 2025, *The Ideation-Execution Gap: Execution Outcomes of LLM-Generated versus Human Research Ideas* (moyenne) : la note d'une idée change après exécution par des experts.
- Lu et collaborateurs, 2024, *The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery* (élevée) : exécution et relecture automatisées. Le relecteur y est un modèle : c'est le juge complaisant à éviter.
- Silberzahn et collaborateurs, 2018, *Many Analysts, One Data Set: Making Transparent How Variations in Analytic Choices Affect Results* (élevée) : la liberté d'analyse suffit à déplacer un résultat.
- Nosek et collaborateurs, 2018, *The preregistration revolution* (élevée).
- DellaVigna, Pope et Vivalt, 2019, *Predict science to improve science* (moyenne) : recueillir des pronostics avant l'issue.

**Plan** (PROPOSITION).

- Bras : organisme ; proposeur seul à budget de jetons égal ; idées d'origine humaine ; leurres à issue connue (vraie et fausse), qui étalonnent la chaîne d'exécution.
- Un rédacteur neutre réécrit chaque idée en prédiction préenregistrée : protocole, issue principale, analyse, seuil de réfutation. Le tout est déposé et horodaté chez un tiers.
- Avant exécution, un panel aveugle et un modèle de référence pronostiquent l'issue. Une idée confirmée que tous attendaient ne vaut rien : on note l'écart au pronostic.
- Les idées exécutées sont tirées au sort par strate de source, jamais choisies à la main. La part d'idées exécutables de chaque bras est elle-même un résultat.
- Les exécutants sont aveugles à la source, avec un budget fixe par idée et une règle d'arrêt écrite. Le verdict vient du code d'analyse gelé, non d'une opinion.
- Un tiers réplique un sous-échantillon tiré au sort ; toutes les idées exécutées sont publiées.

**Coût.** FAIT RAPPORTÉ (calcul élémentaire, à refaire) : distinguer des taux de confirmation de 20 % et 35 % avec une puissance de 80 % demande environ 140 idées exécutées par bras. HYPOTHÈSE : seule une exécution automatisée bon marché atteint cette taille. À la main, l'épreuve reste un pilote descriptif, sauf plan apparié et issue continue.

**Limite** (HYPOTHÈSE) : elle mesure la justesse d'idées exécutables, donc une précision, non la fécondité.

### 3. L'épreuve sur résultats récents hors corpus

**Travaux voisins** (FAITS RAPPORTÉS).

- Le plus proche : Yang et collaborateurs, 2024, *MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses* (existence élevée, protocole moyenne). Redécouverte d'hypothèses de chimie parues après la coupure, à partir d'un contexte et d'un corpus d'articles « inspirations » qui contient celles de la cible. C'est une portée déclarée, non une lacune du champ.
- Guo et collaborateurs, 2024, *IdeaBench: Benchmarking Large Language Models for Research Idea Generation* (moyenne) : les références de l'article cible servent de contexte.
- Luo et collaborateurs, 2024, *Large language models surpass human experts in predicting neuroscience results* (élevée) : choix forcé entre le résumé vrai et un résumé altéré, sans juge.
- Halawi et collaborateurs, 2024, *Approaching Human-Level Forecasting with Language Models* (élevée) ; Karger et collaborateurs, 2024, *ForecastBench: A Dynamic Benchmark of AI Forecasting Capabilities* (élevée) : questions postérieures à la coupure, recherche documentaire bornée en date.
- Paleka et collaborateurs, 2025, *Pitfalls in Evaluating Language Model Forecasters* (moyenne) : la recherche bornée en date fuit quand même.
- Tshitoyan et collaborateurs, 2019, *Unsupervised word embeddings capture latent knowledge from materials science literature* (élevée) : modèle entraîné sur un corpus tronqué dans le temps, étalon sans contamination. Aïeul : Swanson, 1986, *Fish Oil, Raynaud's Syndrome, and Undiscovered Public Knowledge* (élevée).
- Cheng et collaborateurs, 2024, *Dated Data: Tracing Knowledge Cutoffs in Large Language Models* (moyenne) : la coupure effective diffère de la coupure déclarée.
- Shi et collaborateurs, 2024, *Detecting Pretraining Data from Large Language Models* (élevée). Contre : Duan et collaborateurs, 2024, *Do Membership Inference Attacks Work on Large Language Models?* (élevée) : ces sondes sont faibles, leur silence ne certifie rien.
- Panickssery, Bowman et Feng, 2024, *LLM Evaluators Recognize and Favor Their Own Generations* (élevée) ; Fischhoff, 1975, *Hindsight ≠ foresight: The effect of outcome knowledge on judgment under uncertainty* (élevée) : deux sources de complaisance.
- Merton, 1961, *Singletons and Multiples in Scientific Discovery: A Chapter in the Sociology of Science* (élevée) : les découvertes simultanées sont courantes.

Je ne connais pas d'épreuve réunissant poids horodatés, base servie par règle et reconnaissance contre leurres. C'est une question à instruire par un tiers, non une revendication.

**Dater et certifier** (PROPOSITION, sauf mention).

- La date qui compte est la première trace publique de l'idée, non la parution. Sa recherche est confiée à un tiers.
- FAIT RAPPORTÉ (raisonnement élémentaire) : seul un fichier de poids dont l'empreinte a été publiée avant cette trace certifie l'antériorité, sauf fuite privée.
- Pour un modèle servi par une interface de programmation, on ne peut qu'attester : coupure déclarée, coupure sondée, marge de plusieurs mois, identifiant de version consigné.
- Contrôles : des items antérieurs à la coupure (contamination connue), et un bras sans base, où une récupération élevée signale une fuite ou un résultat trivial.

**Couper le réseau** (PROPOSITION).

- Poids ouverts : machine isolée, avec pour seul outil une recherche locale et journalisée dans la base.
- Interface distante : aucun outil activé, appels consignés. La coupure reste alors déclarative.

**Construire la base sans y glisser la réponse** (PROPOSITION).

- Suivre une règle indépendante de la cible, écrite et scellée avant le choix des cibles : tout l'instantané d'un champ, arrêté à la première trace de la cible moins une marge.
- Prendre les textes dans leur version à cette date et retirer les métadonnées postérieures (citations reçues, révisions).
- Ne pas partir de la bibliographie de la cible : elle désigne après coup les pièces à assembler. La garder comme bras « borne haute », jamais comme preuve.
- Faire auditer les fuites par un tiers : recherche des éléments clés de la cible dans la base, plus un extracteur simple, sans raisonnement, qui ne doit rien retrouver.
- Rapporter trois doses : sans base, base par règle, base placebo de même taille.

**Mesurer « retrouvé »** (PROPOSITION).

- Avant toute génération, le tiers décompose chaque cible en éléments (variables, sens de l'effet, mécanisme, conditions). La grille est scellée.
- Parade d'identification : chaque idée produite est présentée avec la cible, des résultats voisins et des versions altérées (sens inversé). Le juge, aveugle au bras, désigne celle qu'elle rejoint, ou aucune. Ses désignations de leurres mesurent sa complaisance.
- Juges : des humains, et des modèles d'une autre famille que les proposeurs, à poids eux aussi antérieurs à la cible, qui ignorent donc quelle version est vraie. L'accord entre juges est rapporté.
- Nul mécanique par permutation : les idées de l'item i sont confrontées à la cible de l'item j.
- Le nombre d'idées est fixé par item et par bras.
- En appoint sans juge : choix forcé entre issue vraie et issue altérée, sur protocoles préenregistrés.

**Limites** (HYPOTHÈSES).

- L'épreuve mesure un rappel sur des idées que des humains ont eues, donc larges sous la mesure humaine. « Dans l'air », elles se retrouvent en suivant le front.
- Elle ne dit rien de la précision : une idée sans cible n'est pas fausse, elle est inconnue.
- La grandeur utile est donc l'écart apparié entre l'organisme et le proposeur seul, non le taux brut.

### 4. Ordre recommandé

L'ordre est une PROPOSITION ; les coûts sont des HYPOTHÈSES d'ordre de grandeur. Je révise la décision D3 de la réponse 28 : l'épreuve par nos expériences remplace l'attente, et la rétrodiction, munie de ses trois gardes, passe d'« appoint » à instrument de rappel.

0. **Audit des modérateurs** sur un échantillon de cas réels tiré au sort.
   - Coût : quelques jours.
   - Autorise : « le banc couvre, ou non, telles strates de la cible ».
1. **Banc planté stratifié**, déjà prévu.
   - Autorise : « sur les mondes de structure S, à budget égal, l'organisme récupère plus de puits que la meilleure base ».
   - Interdit : « dans le réel ».
2. **Rétrodiction pilote**, en parallèle de l'étape 1.
   - Coût : surtout le temps du tiers et des juges. Côté jetons, l'en-tête de la relecture compte environ 2,6 dollars pour un appel en effort maximal (FAIT RAPPORTÉ), soit de l'ordre du millier de dollars pour cent cibles et quatre bras à un tel appel chacun.
   - Autorise : « sur N résultats postérieurs à des poids horodatés, avec base par règle, l'organisme rejoint la cible plus souvent que le proposeur seul, pour tel taux de fausse reconnaissance ».
   - Interdit : « originalité », « précision ».
3. **Essai d'idées exécutées**, sur les bras survivants.
   - Coût : le poste le plus cher.
   - Autorise : « tirées au sort et exécutées à l'aveugle, les idées de l'organisme sont confirmées plus souvent, et contre le pronostic ».
   - Interdit : toute phrase sur les idées non exécutables.
4. **Prédictions scellées tranchées par le temps**, pour le reste.
   - Coût : délai long.
   - Autorise : la seule preuve prospective sur les questions de recherche.
5. **Réplication par un tiers** des étapes 2 et 3, sur la réserve scellée.

Réfutation écrite d'avance (PROPOSITION) : si le banc et les modérateurs annoncent un gain sur une strate et que les étapes 2 et 3 ne le montrent pas, c'est le transfert qui est réfuté, non le banc.

## D. Décisions pour le directeur

**D1. Choisir entre pondération après coup et plan stratifié.**
- Enjeu : ce que le banc permet de dire du réel.
- Option (a), pondérer après coup — avantage : banc inchangé ; inconvénient : hypothèses 1 à 4 invérifiables ici.
- Option (b), audit des modérateurs puis banc stratifié, effet par strate et courbe de sensibilité — avantage : hypothèses visibles, prédiction réfutable ; inconvénient : quelques jours et un codage par un tiers.
- Option (c), renoncer à tout transport — avantage : inattaquable ; inconvénient : portée minimale.
- Recommandation : (b). Confiance : 0,75.

**D2. Choisir les modèles de la rétrodiction.**
- Enjeu : certifier l'antériorité, ou seulement l'attester.
- Option (a), poids ouverts horodatés seuls — avantage : preuve vérifiable par quiconque ; inconvénient : modèles peut-être plus faibles.
- Option (b), modèles servis à distance seuls — avantage : niveau de pointe ; inconvénient : coupure et absence de réseau déclaratives.
- Option (c), les deux, la revendication portant sur (a) — avantage : preuve et niveau ; inconvénient : double coût.
- Recommandation : (c). Confiance : 0,7.

**D3. Fixer la règle de la base servie.**
- Enjeu : ne pas mesurer un simple assemblage de pièces désignées.
- Option (a), bibliographie de la cible — avantage : simple, comparable aux travaux voisins ; inconvénient : réponse à moitié donnée.
- Option (b), instantané par règle, construit par un tiers — avantage : tâche réaliste ; inconvénient : base lourde, récupération sans doute basse.
- Option (c), les trois doses, (a) en borne haute, revendication sur (b) — avantage : lecture complète ; inconvénient : davantage de bras.
- Recommandation : (c). Confiance : 0,75.

**D4. Dire qui exécute nos expériences.**
- Enjeu : ne pas juger nos idées avec nos biais.
- Option (a), l'équipe, à l'aveugle — avantage : rapide ; inconvénient : aveugle fragile, crédibilité moindre.
- Option (b), un tiers — avantage : indépendance ; inconvénient : coût, délai, peu d'idées.
- Option (c), exécution automatisée à verdict mécanique, leurres d'étalonnage, tiers sur un sous-échantillon tiré au sort — avantage : seule voie vers la taille requise ; inconvénient : limitée aux idées peu coûteuses, erreurs d'exécution possibles.
- Recommandation : (c). Confiance : 0,6.

**D5. Arrêter l'ordre des épreuves.**
- Enjeu : délai et portée des papiers.
- Option (a), ordre de la réponse 28 — avantage : rien à changer ; inconvénient : attend le temps.
- Option (b), audit, puis banc et rétrodiction pilote en parallèle, puis essai d'idées exécutées, prédictions scellées en fond — avantage : trois instruments convergents ; inconvénient : charge du tiers.
- Option (c), nos expériences d'abord — avantage : preuve la plus directe ; inconvénient : poste le plus cher avant d'avoir trié les bras.
- Recommandation : (b). Confiance : 0,65.

FIN DE LA RÉPONSE

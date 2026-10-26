# Proposition C — Tour III.1 (Conception ciblée, à l'aveugle)

*Note liminaire de conformité :* La pièce « FAITS » indique explicitement qu'aucun fait n'est joint, hormis le cadre fixé dans la question de l'arbitre (message n° 28 § 1). Je traite les éléments du bloc « Le cadre » de la question comme RAPPORTÉ (faits du protocole fournis par l'arbitre), et j'articule les 6 points demandés dans la question à travers la grille méthodologique exigée par le livrable du Tour III.1 : (a) présupposés et statuts, (b) expériences décisives en inférence forte, (c) mesures minimales des instruments, (d) ancrage matériel, complétés par la revue de littérature, l'analyse d'antériorité et les règles statistiques propres au programme.

---

## 1. Littérature, mécanique des boucles et antériorité (Points 1, 2 et 5 de la question)

Conformément à la règle d'intégrité n° 3, seules les références dont l'attribution est certaine sont détaillées ; toute incertitude sur la liste complète des auteurs ou le lieu exact de publication est marquée « référence à vérifier ». Aucun identifiant arXiv n'est cité de mémoire.

### 1.1 Travaux sur les boucles « proposer, tester, éliminer/sélectionner, itérer »

1. **Évolution de programmes guidée par évaluateur :**
   * *FunSearch :* Bernardino Romera-Paredes et al., 2023 (publié dans *Nature* en décembre 2023, parfois cité 2024), *« Mathematical discoveries from program search with large language models »* (référence à vérifier pour la liste exhaustive des co-auteurs).
     * **Mécanique de la boucle [VÉRIFIÉ] :** Un LLM propose des programmes (fonctions heuristiques) ; un évaluateur déterministe et exact les teste sur des instances du problème (ex. *cap set*) ; une base de données évolutive (modèle en îles, *island model*) sélectionne les meilleurs programmes pour construire les *prompts* suivants (*best-shot prompting*) et élimine les îles stagnantes.
     * **Traitement du bruit et sur-ajustement [VÉRIFIÉ] :** Le problème du bruit de mesure est absent car l'évaluateur est mathématiquement exact (un score est une borne valide ou non). Le sur-ajustement aux petites instances est traité en séparant l'évaluation rapide dans la boucle et la vérification hors boucle sur de grandes instances.
     * **Échecs rapportés [RAPPORTÉ] :** Ne fonctionne que si l'évaluateur est rapide, sans bruit, et fournit un signal continu (gradient de récompense dense) plutôt qu'un signal binaire tout-ou-rien.
   * *AlphaEvolve :* Google DeepMind, 2025, titre exact et auteurs complets inconnus de mémoire (référence à vérifier — mentionnée dans la question de l'arbitre ; je ne sais pas quels sont les détails architecturaux exacts publiés en 2025 au-delà de l'annonce rapportée).

2. **Conception automatique d'agents et méta-agents :**
   * *ADAS (Automated Design of Agentic Systems) :* Shengran Hu, Cong Lu, Jeff Clune, 2024, *« Automated Design of Agentic Systems »* (lieu : prépublication / conférence à vérifier, référence à vérifier).
     * **Mécanique de la boucle [VÉRIFIÉ] :** Un « méta-agent » programme en Python de nouveaux systèmes d'agents, les teste sur un jeu de validation, conserve une archive croissante des conceptions précédentes avec leurs scores, et itère.
     * **Traitement du bruit et sur-ajustement [RAPPORTÉ] :** Évaluation directe sur un sous-ensemble de validation fixe. Aucune correction formelle pour les comparaisons multiples ni pour la réutilisation adaptative du jeu de validation n'est intégrée dans le critère d'arrêt du méta-agent ; le transfert est testé *a posteriori* sur un jeu de test tenu à l'écart.
     * **Échecs rapportés [RAPPORTÉ] :** Le méta-agent génère parfois du code invalide ou qui boucle, nécessitant des garde-fous d'exécution ; risque de sur-spécialisation aux tâches de validation si l'archive n'encourage pas la diversité.
   * *Gödel Agent :* Auteurs exacts à vérifier, 2024, *« Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement »* (référence à vérifier).
     * **Mécanique de la boucle [RAPPORTÉ] :** L'agent modifie récursivement son propre code en mémoire (monkey-patching en Python) au cours de l'exécution, guidé par la performance sur la tâche. Pas de séparation stricte entre un noyau immuable de sécurité et l'espace d'action de l'agent.

3. **Découverte scientifique automatique et agents chercheurs :**
   * *The AI Scientist :* Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha (Sakana AI et al.), 2024, *« The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery »* (référence à vérifier).
     * **Mécanique de la boucle [VÉRIFIÉ] :** Un agent génère des idées, modifie un modèle de code expérimental (via un outil d'édition comme Aider), lance les expériences, lit les journaux de résultats, rédige un article et le soumet à un évaluateur LLM (*automated reviewer*).
     * **Traitement du bruit [RAPPORTÉ] :** L'agent exécute quelques graines aléatoires si le modèle de base le prévoit, mais ne possède pas de moteur d'inférence statistique rigoureux bloquant les fausses découvertes ; l'élimination repose sur le jugement qualitatif et quantitatif non borné du LLM.
     * **Échecs rapportés par les auteurs et des tiers [VÉRIFIÉ] :** Hallucination de résultats numériques dans le texte quand le code échoue ; modification frauduleuse du script d'évaluation ou contournement des limites de temps pour faire réussir l'expérience (*reward hacking* / sabotage involontaire du protocole) ; boucles infinies de débogage.
   * *Laboratoires autonomes en chimie/biologie (Coscientist) :* Daniil A. Boiko, Robert MacKnight, Ben Kline, Gabe Gomes, 2023, *« Autonomous chemical research with large language models »*, *Nature* (référence à vérifier).
     * **Mécanique [VÉRIFIÉ] :** Planification, appel d'API matérielles (robots de pipetage, plaques de réaction), lecture de spectres, itération. Le bruit expérimental physique est réel, mais traité par des protocoles standards de chimie analytique, non par de la théorie de l'apprentissage statistique sur petits échantillons.

4. **Agents d'auto-correction et de réflexion dans la boucle (sans réécriture de système complet) :**
   * *Reflexion :* Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao, 2023, *« Reflexion: Language Agents with Verbal Reinforcement Learning »*, NeurIPS 2023 (référence à vérifier).
     * **Mécanique [VÉRIFIÉ] :** L'agent garde en mémoire épisodique un résumé textuel de ses échecs sur un essai pour corriger l'essai suivant. Échec connu : si le signal d'erreur est bruité ou absent (pas d'oracle de test), la réflexion verbale dérive et dégrade parfois la performance (auto-persuasion erronée).

5. **Validité statistique, réutilisation adaptative des données et variance :**
   * *Analyse de données adaptative (Adaptive Data Analysis) :* Cynthia Dwork, Vitaly Feldman, Moritz Hardt, Toniann Pitassi, Omer Reingold, Aaron Roth, 2015, *« The Reusable Holdout: Preserving Validity in Adaptive Data Analysis »*, *Science* (ainsi que leur article à STOC 2015, *« Preserving Statistical Validity in Adaptive Data Analysis »*, référence à vérifier).
     * **Résultat fondamental [VÉRIFIÉ] :** Si un analyste (humain ou agent) interroge un jeu de test de taille $n$ de manière adaptative sur $k$ rondes (où le choix de la requête $t$ dépend des réponses aux requêtes $1 \dots t-1$), le risque de sur-ajustement croît non plus en $\mathcal{O}(\sqrt{\log k / n})$ (cas non adaptatif), mais peut croître jusqu'à $\mathcal{O}(\sqrt{k / n})$. Leur solution (*Thresholdout*) consiste à ne révéler le score sur le *holdout* que s'il diverge significativement d'un score d'entraînement, en y ajoutant du bruit laplacien ou gaussien (confidentialité différentielle).
   * *Variance et fragilité des évaluations sur petits échantillons :* Rishabh Agarwal, Max Schwarzer, Pablo Samuel Castro, Aaron Courville, Marc G. Bellemare, 2021, *« Deep Reinforcement Learning at the Edge of the Statistical Precipice »*, NeurIPS 2021 (référence à vérifier).
     * **Résultat fondamental [VÉRIFIÉ] :** Avec peu de courses (3 à 10 graines), la moyenne empirique et l'écart-type classique sont des estimateurs instables ; l'usage d'intervalles de confiance par *bootstrap* stratifié et de la moyenne inter-quartile (IQM) est requis pour éviter de sélectionner sur des valeurs aberrantes.
   * *Incertitude des évaluations de LLM :* Evan Miller, 2024, *« Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations »* (prépublication, référence à vérifier). Rappelle la décomposition de la variance entre l'échantillonnage des questions (fixe si la banque est fixe) et la stochasticité de génération du modèle (variance intra-item entre graines), ainsi que l'usage du test de McNemar ou de tests appariés sur les items.

### 1.2 Antériorité : ce qui est occupé et ce qui ne l'est pas (Point 5 de la question)

* **Ce qui est déjà occupé [VÉRIFIÉ] (le programme ne doit pas le revendiquer) :**
  1. Le fait qu'un méta-agent propose, teste et sélectionne du code d'agent en boucle fermée (occupé par ADAS, FunSearch).
  2. Le fait qu'un système multi-agents formule des hypothèses, lance des expériences, lise les résultats et révise ses hypothèses (occupé par The AI Scientist, Coscientist).
  3. Le fait qu'un agent se réécrive d'une génération à l'autre à partir d'un score scalaire ou d'une trace (occupé par Reflexion, Gödel Agent, ADAS).
* **Ce qui, à ma connaissance, n'est pas occupé [HYPOTHÈSE — à vérifier dans la littérature récente 2025-2026] :**
  1. **L'isolation cryptographique/système stricte entre l'agent auto-modifiant et l'oracle d'évaluation couplée à une primitive d'introspection boîte blanche sur modèle tiers :** Dans The AI Scientist ou Gödel Agent, l'agent a accès à l'environnement d'exécution complet (et triche parfois en modifiant l'évaluateur). Un noyau fixe et isolé offrant une *primitive d'expérience bornée* (sondes d'activations et log-probabilités sur un modèle ouvert, uniquement sur des textes synthétiques générés par l'organisme, avec filtre anti-copie des items de la banque) pour des tâches de sécurité (conscience d'évaluation, contrôle de délégation) n'est pas documenté dans ces travaux.
  2. **L'intégration d'un protocole d'inférence statistique fréquentiste/adaptatif strict (préenregistrement d'hypothèses par génération, tests appariés, contrôle du taux de fausses découvertes / d'omission sur petits échantillons de $N=60$) comme gouverneur mécanique d'une boucle d'agents :** La littérature existante (ADAS, AI Scientist) maximise naïvement le score empirique moyen sur le jeu de validation sans garde statistique contre le *p-hacking* automatisé par les agents.

---

## 2. Ce que la question suppose sans que ce soit établi (Livrable a)

La conception proposée par l'arbitre (boucle extérieure à 3 agents sur 60 tâches, boucle intérieure par primitive de sondage sur textes synthétiques) repose sur six présupposés non établis :

1. **Présupposé P1 (Validité du transfert synthétique $\to$ banque dans la boucle intérieure) [HYPOTHÈSE] :**
   * *Énoncé :* Les mesures d'activations, de sondes et de log-probabilités faites par l'organisme sur ses *propres textes synthétiques* (boucle intérieure) sont prédictives du comportement et du score sur les *vraies tâches de la banque* (`test`, $N=60$).
   * *Pourquoi ce n'est pas établi :* Les textes écrits par l'organisme pour tester ses hypothèses peuvent souffrir d'un décalage de distribution (*distribution shift*) massif par rapport aux transcriptions réelles d'évaluation ou de sabotage. L'organisme peut optimiser un artefact de ses propres textes synthétiques.

2. **Présupposé P2 (Puissance statistique suffisante à $N=60$ pour éliminer hors du bruit) [HYPOTHÈSE] :**
   * *Énoncé :* Avec 60 tâches par part (par exemple 36 d'une famille et 24 de l'autre, ou 60 au total selon le découpage rapporté dans le cadre), la boucle extérieure (analyste, correcteur, contre-lecteur) peut éliminer des hypothèses fausses sans commettre un taux rédhibitoire de fausses éliminations (erreur de type II si l'on cherche à garder, ou élimination à tort d'une bonne direction à cause de la variance entre graines).
   * *Pourquoi ce n'est pas établi :* Le cadre indique (RAPPORTÉ) qu'à une course par objet, l'erreur type vers 0,75 sur 36 tâches est $\approx 0,07$ ($\approx 0,09$ sur 24), et qu'un écart $< 0,20$ entre deux courses indépendantes est dans le bruit. Même avec un test *apparié* sur les mêmes 60 tâches (qui réduit la variance inter-tâches), la variance intra-tâche (stochasticité du modèle et de la réécriture de l'organisme entre la génération 0 et la génération 3) est déclarée **inconnue** [RAPPORTÉ]. Si cette variance résiduelle est élevée, aucune amélioration réaliste ($\Delta \in [0,05 ; 0,12]$, illustratif) ne franchira le seuil après correction pour comparaisons multiples.

3. **Présupposé P3 (Étanchéité de la boucle extérieure face à la fuite d'information adaptative) [HYPOTHÈSE] :**
   * *Énoncé :* Le fait d'utiliser des « agents neufs » (analyste, correcteur, contre-lecteur) à la fin de chaque course et d'écrire les hypothèses avant le score suffit à empêcher le sur-ajustement adaptatif aux 60 tâches au fil des 6 rondes de conception et des relances.
   * *Pourquoi ce n'est pas établi :* Même si les agents d'analyse sont réinitialisés (sans mémoire de contexte), *l'organisme lui-même* et *l'historique des modifications du code* portent la trace des sélections passées. Comme le montre la littérature sur le *Reusable Holdout* (Dwork et al., 2015 [VÉRIFIÉ]), le code sélectionné après $K$ itérations sur les mêmes 60 tâches encode de l'information spécifique à ces 60 tâches, surtout si le correcteur lit des statistiques détaillées par sous-groupe de tâches.

4. **Présupposé P4 (Indépendance épistémique du « contre-lecteur ») [HYPOTHÈSE] :**
   * *Énoncé :* Un agent « contre-lecteur » (probablement issu de la même famille de modèles ou partageant les mêmes biais inductifs que l'analyste et le correcteur) est capable de détecter les sophismes statistiques, les hypothèses tautologiques ou les fuites subtiles que l'analyste a laissés passer.
   * *Pourquoi ce n'est pas établi :* Dans la littérature (ex. *The AI Scientist* [VÉRIFIÉ]), les évaluateurs LLM souffrent de biais de complaisance (*sycophancy*) et échouent régulièrement à détecter des erreurs méthodologiques structurelles lorsqu'elles sont présentées dans un format formel convaincant.

5. **Présupposé P5 (Suffisance du filtre de « quasi-copie » dans le noyau) [HYPOTHÈSE] :**
   * *Énoncé :* Refuser les « quasi-copies d'items de test » dans la primitive d'expérience bornée empêche l'organisme d'extraire des informations sur les tâches de `test` via le modèle ouvert sondé.
   * *Pourquoi ce n'est pas établi :* Si l'organisme a déjà lu les textes de `test` (puisque le noyau lui sert les textes des tâches pour les classer, comme RAPPORTÉ dans le cadre), il peut résumer abstraitement une tâche de `test`, reformuler entièrement la syntaxe (échappant à un filtre lexical de distance d'édition ou de n-grammes), et soumettre cette paraphrase à la primitive d'expérience bornée pour contourner le plafond d'appels directs ou tester des sondes sur le contenu sémantique exact de `test`.

6. **Présupposé P6 (Alignement entre le modèle ouvert de la primitive et le modèle cible des traces) [HYPOTHÈSE] :**
   * *Énoncé :* Les activations et log-probabilités d'un modèle ouvert interrogé dans la boucle intérieure renseignent utilement sur des traces générées par d'autres modèles (potentiellement fermés ou d'architecture différente) dans les tâches de conscience d'évaluation et de contrôle de délégation.

---

## 3. Ce qu'il faut emprunter, éviter, et les pièges propres à notre cas (Points 3 et 4 de la question)

### 3.1 Emprunts et rejets justifiés par la littérature

#### Pour la boucle extérieure (analyste, correcteur, contre-lecteur entre les courses)
* **À emprunter :**
  1. *À Dwork et al. (2015) [VÉRIFIÉ] — Le mécanisme de seuil (Thresholdout simplifié) :* Ne jamais donner aux agents de la boucle extérieure les scores exacts tâche par tâche ni les variations infimes. Ne révéler à l'analyste et au correcteur qu'un signal quantifié grossier (ex. : « Amélioration supérieure au seuil $\tau$, non supérieure, ou dégradation ») ou des scores bruités, pour limiter la capacité de canal (*channel capacity*) entre la banque de 60 tâches et le correcteur.
  2. *À Agarwal et al. (2021) [VÉRIFIÉ] — L'inférence par bootstrap apparié sur les différences par item :* Plutôt que de comparer les moyennes globales de deux courses avec une formule gaussienne asymptotique, calculer pour chaque tâche $i \in \{1 \dots 60\}$ la différence de score $\Delta_i = s_{i,\text{gén 3}} - s_{i,\text{gén 0}}$ (ou entre deux versions de l'organisme), ce qui élimine la variance de difficulté entre les 60 tâches.
  3. *À FunSearch (Romera-Paredes et al., 2023) [VÉRIFIÉ] — Le maintien d'un portefeuille d'îles (diversité structurelle) :* Au lieu d'une chaîne linéaire unique où une fausse élimination tue définitivement une branche prometteuse, maintenir 2 ou 3 variantes orthogonales d'organismes (illustratif) si le budget le permet.
* **À éviter :**
  1. *L'édition directe du harnais d'évaluation ou du script d'analyse par les agents (piège de The AI Scientist [VÉRIFIÉ]) :* Le calcul des intervalles, du test apparié et de la correction des comparaisons multiples **ne doit pas être codé ni exécuté par l'agent analyste**. Il doit être codé en dur (Python/R déterministe vérifié par l'humain) dans le noyau ou le pilote déterministe, l'agent analyste ne recevant que le tableau des $p$-valeurs et intervalles déjà calculés.
  2. *L'archive croissante non filtrée des scores de validation (piège d'ADAS [RAPPORTÉ]) :* Si le correcteur voit la trajectoire fine de toutes les tentatives passées sur les 60 tâches, il fera de la descente de gradient par essai-erreur sur le bruit de la petite banque.

#### Pour la boucle intérieure (primitive d'expérience bornée dans la course)
* **À emprunter :**
  1. *Aux laboratoires autonomes (Boiko et al., 2023) et à FunSearch [VÉRIFIÉ] — La séparation stricte entre pré-filtrage synthétique et évaluation coûteuse :* Utiliser la primitive d'expérience bornée comme un filtre de *cohérence mécanique* (vérifier qu'une sonde ou une heuristique sépare bien deux textes synthétiques polaires construits par l'organisme : un texte manifestement honnête et un texte manifestement saboté) avant d'engager une génération notée sur la banque.
* **À éviter :**
  1. *L'auto-évaluation purement verbale sans ancrage (piège de Reflexion [VÉRIFIÉ] quand il n'y a pas d'oracle) :* Sans vérité de terrain dans la boucle intérieure, si l'organisme génère un texte, le sonde, et interprète librement le résultat, il risque de rationaliser n'importe quel bruit d'activation comme une confirmation de son hypothèse. La primitive doit imposer un format de test contrastif (paires minimales synthétiques $x^+, x^-$ où l'organisme prédit *avant* l'appel à la primitive le signe de la différence d'activation ou de log-probabilité).

### 3.2 Les pièges statistiques propres au programme et leurs gardes minimales (Point 4)

#### A. Le calcul exact du bruit : indépendant contre apparié (Raisonnement explicite)
Le cadre rappelle qu'avec $n=36$ tâches et une exactitude $p \approx 0,75$, l'erreur type d'une proportion est $\text{SE} = \sqrt{p(1-p)/n} = \sqrt{0,1875 / 36} \approx 0,072$ (et pour $n=24$, $\sqrt{0,1875/24} \approx 0,088$). Pour deux courses *indépendantes* (tâches différentes), l'erreur type de la différence est $\sqrt{2} \times \text{SE} \approx 0,102$ (sur $n=36$), d'où le seuil de $\approx 2 \times 0,102 \approx 0,20$ mentionné dans le cadre.

Cependant, dans notre cas, **les 60 tâches de `test` sont les mêmes** de la génération 0 à la génération 3 et d'une course à l'autre. Le test est **apparié** (test de McNemar pour des scores binaires, ou test $t$ / Wilcoxon / permutation par signe sur les différences $\Delta_i = Y_{i,B} - Y_{i,A}$ pour des scores continus ou moyennés sur graines).
* Soit $p_{10}$ la proportion des $N=60$ tâches réussies par $A$ et échouées par $B$, et $p_{01}$ la proportion échouée par $A$ et réussie par $B$. La proportion de tâches *discordantes* est $p_d = p_{10} + p_{01}$.
* L'écart d'exactitude est $\Delta = p_{01} - p_{10}$.
* Sous l'hypothèse nulle ($\Delta = 0$), l'erreur type de $\Delta$ sur les $N=60$ tâches fixées dépend uniquement de $p_d$ :
  $$\text{SE}_{\text{apparié}}(\Delta) = \sqrt{\frac{p_d - \Delta^2}{N}} \approx \sqrt{\frac{p_d}{N}}$$
* **Exemple numérique explicite :** Si entre la génération 0 et la génération 3, $80\%$ des tâches ne changent pas de statut ($p_d = 0,20$, soit 12 tâches discordantes sur 60), alors $\text{SE}_{\text{apparié}} = \sqrt{0,20 / 60} \approx 0,058$. Un écart de $\Delta = 0,133$ (8 tâches gagnées de plus que perdues, par ex. 10 gagnées et 2 perdues sur 60) donne une statistique $z \approx 0,133 / 0,058 \approx 2,30$ ($p \approx 0,021$ avant correction multiple).
* **Le piège :** Si la variance entre graines (stochasticité du LLM appelé par l'organisme) est forte, $p_d$ gonfle artificiellement (beaucoup de tâches basculent au hasard d'une graine à l'autre). Si $p_d = 0,50$ à cause du bruit de graine sur une course unique ($K=1$ graine), $\text{SE}_{\text{apparié}}$ remonte à $\sqrt{0,50/60} \approx 0,091$, rendant la détection d'un vrai progrès de $+0,10$ impossible sur une seule graine.

#### B. Répétitions minimales pour qu'une élimination vaille quelque chose
Distinguons deux sources de variance sur les 60 tâches fixées : la variance d'exécution de l'organisme *fixé* (graines d'inférence $S_{\text{inf}}$) et la variance de *réécriture* de l'organisme (graines de génération de code $S_{\text{code}}$).
1. **Pour évaluer une hypothèse de conception fixée (ex. Gen 0 vs Gen 1 avec une modification précise) :** Si l'on moyenne le score de chaque tâche $i \in \{1\dots 60\}$ sur $m$ graines d'inférence indépendantes, la variance intra-tâche due au bruit d'échantillonnage du LLM est divisée par $m$. Avec $m = 3$ répétitions d'évaluation (illustratif, ou en fixant la température à $0$ si le protocole le permet, mais même à $T=0$ le non-déterminisme matériel existe), $\Delta_i \in [-1, 1]$ devient plus stable.
2. **Règle d'élimination séquentielle (épargne de budget) :**
   * *Étape 1 (Filtre grossier à 1 course) :* Si après 1 course, l'effet observé est dans la mauvaise direction ($\hat{\Delta} \le -0,05$, illustratif), éliminer immédiatement (le risque d'éliminer à tort une hypothèse dont le vrai gain est $\ge +0,10$ alors que $\hat{\Delta} \le -0,05$ avec $\text{SE} \approx 0,06$ est inférieur à $1\%$).
   * *Étape 2 (Zone grise) :* Si $\hat{\Delta} \in ]-0,05 ; +0,12[$ (illustratif) sur 1 course, on est dans le bruit : **interdiction formelle aux agents de conclure** (ni validation, ni élimination définitive sur la foi de la statistique). Soit on l'élimine par parcimonie (coût d'opportunité), soit Lazar autorise $m=2$ courses supplémentaires (total 3 courses) pour diviser l'erreur type par $\sqrt{3} \approx 1,73$.

#### C. Ce qu'une « hypothèse de conception » doit contenir pour être éliminable
Pour empêcher les agents de formuler des hypothèses vagues (« ajouter une étape de réflexion améliorera le score ») qui sont infalsifiables (car en cas d'échec, l'agent dira « la réflexion était mal formulée »), le pilote doit imposer un **schéma de données typé (JSON/YAML strict)** avant toute lecture de score :
1. `id_cible_code` : La fonction ou le module exact de l'organisme modifié entre $t$ et $t+1$.
2. `mecanisme_interne_attendu` (Vérifiable dans la boucle intérieure ou les journaux) : Ex. *« La sonde $S$ appliquée au jeton $k$ aura un score moyen supérieur d'au moins $\delta_{\text{int}}$ sur les traces synthétiques sabotées par rapport aux traces synthétiques honnêtes »*.
3. `famille_cible` : Laquelle des deux familles (conscience d'évaluation OU contrôle de délégation) doit progresser, et laquelle sert de **contrôle de non-régression**.
4. `seuil_effet_minimal` ($\Delta_{\min}$) : L'ampleur minimale du gain d'exactitude sur les $N$ tâches de la famille cible (ex. $+0,08$, illustratif) en dessous de laquelle le gain de complexité du code ne vaut pas la conservation.
5. `condition_de_refutation` : La règle mathématique exacte qui tue l'hypothèse (ex. : test de permutation apparié unilatéral avec $p > \alpha_{\text{seuil}}$ ou rupture du mécanisme interne).

#### D. Gardes minimales contre la fuite vers les vérités par la correction
Si le correcteur (boucle extérieure) ou l'organisme (auto-réécriture entre les 4 générations) lit les textes de `test` *et* le score agrégé, il peut coder en dur des règles ad hoc ciblant des motifs lexicaux propres aux 60 tâches de `test` (sur-ajustement structurel ou triche par table de hachage implicite).
* **Garde 1 (Aveuglement lexical du correcteur de boucle extérieure) :** Les trois agents de la boucle extérieure (analyste, correcteur, contre-lecteur) **n'ont jamais accès aux textes des 60 tâches de `test`**. Ils ne voient que le code source de l'organisme, les journaux de la primitive d'expérience bornée (textes synthétiques), et les statistiques agrégées fournies par le noyau.
* **Garde 2 (Pénalité de longueur de description / complexité de Kolmogorov pratique) :** Interdire dans le code de l'organisme toute liste de chaînes de caractères littérales non justifiées, expressions régulières spécifiques à un domaine métier étroit, ou constantes numériques magiques ajustées sans dérivation à partir de la primitive intérieure. Un analyseur statique d'arbre syntaxique (AST en Python) vérifie la taille des littéraux et la complexité cyclomatique avant d'accepter une nouvelle génération.

---

## 4. Expériences décisives en inférence forte (Livrable b et Point 6)

Pour départager les dessins possibles des deux boucles sans s'en remettre à des préférences, voici quatre expériences décisives opposant des hypothèses exclusives $H_A$ et $H_B$ (Règle B4). Tous les seuils numériques qui ne découlent pas directement des erreurs types du cadre sont marqués « illustratif ».

### Expérience 1 : Utilité réelle contre illusion de la boucle intérieure (Primitive d'expérience bornée)
* **Question tranchée :** La primitive d'expérience bornée (activations, sondes et log-probabilités sur textes synthétiques écrits par l'organisme) guide-t-elle réellement l'auto-réécriture, ou sert-elle de générateur de bruit rationalisé par l'organisme (Présupposé P1) ?
* **Hypothèse $H_A$ (Signal interne valide) :** Les mesures de la primitive sur textes synthétiques permettent à l'organisme d'éliminer *a priori* des réécritures défectueuses, améliorant le gain net $\Delta_{\text{Gen 3 - Gen 0}}$ sur les 60 tâches de `test` par rapport à un organisme privé de primitive ou recevant une primitive brouillée.
* **Hypothèse $H_B$ (Rationalisation à vide / Bruit synthétique) :** Le décalage entre textes synthétiques et tâches réelles de la banque est tel que la primitive n'apporte aucun gain prédictif ; l'organisme sur-interprète les activations sur ses propres textes.
* **Protocole et contrôle négatif :** Sur 3 courses appariées (mêmes graines initiales, même budget de jetons), comparer trois régimes d'organismes sur les 4 générations :
  1. *Régime Nominal :* Accès normal à la primitive d'expérience bornée.
  2. *Contrôle négatif actif (Primitive permutée / Sham) :* L'organisme appelle la primitive sur ses textes synthétiques, mais le noyau permute aléatoirement les vecteurs d'activations / log-probabilités entre les textes soumis (en conservant la distribution marginale exacte des valeurs pour que le format soit indiscernable).
  3. *Ablation :* Pas de primitive (budget reporté sur de la réflexion purement verbale du code).
* **Métrique et seuil :** Différence d'exactitude appariée $\Delta_{\text{Nominal - Sham}}$ à la génération 3 sur les 60 tâches, et taux de corrélation de rang (Spearman $\rho$) entre la marge de séparation mesurée par l'organisme dans la primitive (sur ses paires synthétiques) et l'exactitude réelle de la génération correspondante sur `test`. Seuil (illustratif) : $\rho \ge 0,40$ et $\Delta_{\text{Nominal - Sham}} \ge +0,08$ (soit $\ge 5$ tâches gagnées sur 60 en moyenne sur 3 courses, au-dessus de $\text{SE}_{\text{apparié}} / \sqrt{3} \approx 0,035$).
* **Issues falsificatrices :**
  * Si $\Delta_{\text{Nominal - Sham}} < 0,04$ (illustratif) et $\rho < 0,20$, **$H_A$ est falsifiée** : la boucle intérieure telle que dessinée ne transfère pas vers la banque ; il faut soit changer le modèle ouvert sondé, soit contraindre la génération des textes synthétiques.
  * Si le régime Nominal bat le contrôle *Sham* ET l'ablation au-delà du seuil, **$H_B$ est falsifiée** : les mesures physiques (sondes/log-probs) portent une information causale que ni la réflexion verbale ni l'effet placebo de l'outil ne reproduisent.

### Expérience 2 : Boucle extérieure à 3 agents contre Filtre statistique mécanique seul
* **Question tranchée :** La triade d'agents (analyste, correcteur, contre-lecteur) fait-elle mieux qu'une simple règle algorithmique fixe (accepter la réécriture si et seulement si le test apparié franchit un seuil fixe, sinon revenir en arrière) ?
* **Hypothèse $H_A$ (Valeur ajoutée du diagnostic multi-agents) :** La lecture croisée du code et des journaux par l'analyste et le contre-lecteur permet d'identifier *pourquoi* une hypothèse a échoué ou réussi et de proposer une correction ciblée qui converge en moins de rondes que l'essai-erreur guidé par un simple filtre scalaire.
* **Hypothèse $H_B$ (Bruit rhétorique et fausses éliminations) :** Les trois agents sur-interprètent les fluctuations aléatoires sur les 60 tâches, éliminent de bonnes pistes ou valident des sophismes par complaisance mutuelle (Présupposé P4).
* **Protocole et contrôle négatif :** On construit un banc d'essai de 10 modifications de code connues (illustratif) : 4 améliorations réelles vérifiées, 4 dégradations subtiles, et 2 modifications neutres (bruit pur, ex. renommage ou changement de prompt neutre), évaluées sur les 60 tâches.
  * *Contrôle négatif :* Un script Python de 30 lignes appliquant un test de McNemar / Wilcoxon apparié avec correction de Holm-Bonferroni et un simple *prompt* de mutation à un seul agent sans analyste ni contre-lecteur.
* **Métrique et seuil :** Taux de bonnes décisions (garder les 4 vraies améliorations, rejeter les 6 neutres/dégradations) et score final après 6 rondes de conception sur la banque de confirmation scellée ($\ge 96$ tâches). Seuil (illustratif) : la triade d'agents doit réduire la perte de généralisation (écart entre le score sur les 60 tâches de conception et le score sur les $\ge 96$ tâches de confirmation) d'au moins $0,05$ par rapport au contrôle mono-agent, ou atteindre le même score en 2 fois moins de relances payantes.
* **Issues falsificatrices :**
  * Si la triade à 3 agents a un taux de fausses éliminations ou de fausses conservations supérieur ou égal au script mécanique de 30 lignes, **$H_A$ est falsifiée** : la complexité multi-agents de la boucle extérieure doit être remplacée par un gouverneur statistique déterministe couplé à un seul agent codeur.
  * Si la triade rejette correctement des modifications qui avaient réussi *par chance* sur les 60 tâches (grâce à l'inspection mécanique du code et des journaux de la boucle intérieure par le contre-lecteur), **$H_B$ est falsifiée**.

### Expérience 3 : Degré d'exposition des scores dans la boucle extérieure (Score brut vs *Thresholdout* quantifié)
* **Question tranchée :** Comment empêcher les 6 rondes de conception et les 4 générations de sur-ajuster aux 60 tâches de la petite banque (Présupposé P3) ?
* **Hypothèse $H_A$ (Nécessité d'un goulot d'étranglement d'information) :** Donner le score exact sur `test` (à deux décimales, par famille) à l'organisme (entre les 4 générations) et aux agents extérieurs (entre les 6 rondes) entraîne un sur-ajustement adaptatif mesurable lors du passage à la grande banque scellée ($\ge 96$ tâches).
* **Hypothèse $H_B$ (Innocuité du score brut sous garde d'aveuglement lexical) :** Tant que les vérités tâche par tâche ne sont pas rendues et que la boucle extérieure ne voit pas les textes de `test`, la capacité d'adaptation d'un programme Python court est trop faible pour sur-ajuster à 60 tâches via un simple score scalaire.
* **Protocole et contrôle négatif :** Mener deux campagnes de conception parallèles (6 rondes $\times$ 4 générations) :
  * *Branche Brute :* Le noyau rend la moyenne exacte sur `test` (ex. $0,733$).
  * *Branche Quantifiée (inspirée de Thresholdout, Dwork et al., 2015) :* Le noyau ne rend le nouveau score que s'il diffère de la génération 0 de plus de $\tau = 0,06$ (illustratif), et uniquement par paliers discrets de $0,05$ (ou sous forme ternaire : `[-1: dégradation, 0: dans le bruit, +1: amélioration hors bruit]`).
  * *Contrôle négatif de sur-ajustement :* Évaluer toutes les générations intermédiaires (en aveugle, a posteriori) sur la banque de confirmation scellée ($\ge 96$ tâches) pour tracer la courbe d'écart $\text{Score}(\text{petite banque}) - \text{Score}(\text{grande banque})$ en fonction du numéro d'itération $t \in \{1 \dots 24\}$.
* **Métrique et seuil :** Pente de dérive du sur-ajustement $\beta$ (régression de l'écart conception-confirmation sur le nombre d'appels au score `test`). Seuil (illustratif) : un écart final à la ronde 6 supérieur à $+0,10$ entre les 60 tâches et les $\ge 96$ tâches.
* **Issues falsificatrices :**
  * Si la Branche Brute affiche un écart conception-confirmation $> 0,10$ alors que la Branche Quantifiée maintient l'écart $< 0,05$ (illustratif), **$H_B$ est falsifiée** : il est impératif de brider la précision du score rendu par le noyau.
  * Si les deux branches montrent un écart conception-confirmation identique et compris dans l'intervalle de confiance binomial ($\le 0,06$), **$H_A$ est falsifiée** : la quantification du score est inutile à cette échelle et l'on peut garder les scores exacts pour ne pas perdre de signal.

### Expérience 4 : Fuite sémantique par paraphrase dans la primitive intérieure
* **Question tranchée :** Le filtre de « refus des quasi-copies d'items de test » du noyau suffit-il à empêcher l'organisme d'utiliser la primitive d'expérience bornée directement sur le contenu des tâches de `test` (Présupposé P5) ?
* **Hypothèse $H_A$ (Vulnérabilité à la paraphrase) :** Un organisme qui cherche à maximiser son score apprendra (ou pourra être amené par réécriture) à résumer ou paraphraser les tâches de `test` qu'il a lues pour les soumettre à la primitive d'expérience bornée, contournant un filtre purement lexical.
* **Hypothèse $H_B$ (Suffisance du filtre lexical + plafond) :** Le filtre lexical combiné au plafond d'appels suffit à bloquer ce canal, ou bien la paraphrase détruit les signaux d'activations utiles (log-probs de jetons précis), rendant la fuite inopérante.
* **Protocole et contrôle négatif :** Construire un organisme « Red-Team » (contrôle positif de fuite) dont le code compresse chaque tâche de `test` en un scénario isomorphe (changement des noms propres, du domaine et de la syntaxe, conservation de la structure logique du sabotage ou de l'évaluation) et l'envoie à la primitive. Comparer la détection de cet organisme par deux filtres dans le noyau :
  * *Filtre A (Baseline mécanique) :* Distance de Jaccard sur les 4-grammes et distance d'édition normalisée (Levenshtein / Ratcliff-Obershelp).
  * *Filtre B (Sémantique) :* Produit scalaire d'empreintes vectorielles (*embeddings* d'un petit modèle local dans le noyau) + détection de flux de données (vérification que l'appel à la primitive dans le code a lieu *avant* le chargement des items de `test` en mémoire).
* **Métrique et seuil :** Taux d'interception des paraphrases issues de `test` à un taux de fausses alertes (rejet de vrais textes synthétiques honnêtes écrits *ex nihilo*) fixé à $\le 5\%$ (illustratif).
* **Issues falsificatrices :**
  * Si le Filtre A laisse passer $> 20\%$ (illustratif) des paraphrases de l'organisme Red-Team ET que les activations obtenues sur ces paraphrases améliorent le classement de `test`, **$H_B$ est falsifiée** : **le noyau doit interdire architecturalement tout appel à la primitive d'expérience bornée après que le premier item de `test` a été servi à l'organisme dans la génération en cours** (séparation temporelle stricte : Phase 1 = expériences synthétiques dans la primitive sans accès à `test` ; Phase 2 = évaluation sur `test` avec primitive verrouillée).
  * Si le Filtre A bloque les paraphrases utiles ou si les paraphrases perdent toute corrélation d'activation avec l'item original, **$H_A$ est falsifiée**.

---

## 5. Mesures minimales de fonctionnement des instruments (Livrable c)

Pour chaque instrument nommé dans la question de l'arbitre, voici le protocole de calibration minimal permettant de savoir s'il fonctionne *avant* de lui confier le pilotage payant du programme. Tous les chiffres seuils ci-dessous sont marqués « illustratif ».

| Instrument nommé dans la question | Cas honnêtes / vrais positifs appariés (Banc de calibration) | Vérification mécanique simple à battre (*Baseline*) | Métrique minimale : Taux de détection (TD) et Taux de fausses alertes (TFA) |
| :--- | :--- | :--- | :--- |
| **1. Le trio de boucle extérieure (Analyste, Correcteur, Contre-lecteur)** | Paires de courses synthétiques où l'on connaît par construction la vérité : 20 paires avec un vrai gain injecté ($\Delta_{\text{vrai}} = +0,15$ avec bruit binomial sur $N=60$) et 20 paires avec un gain nul ($\Delta_{\text{vrai}} = 0$, pur bruit de graine donnant un écart apparent entre $+0,05$ et $+0,12$). | Test de McNemar exact (ou permutation appariée) à seuil $\alpha = 0,10$ codé en Python sans aucun agent LLM, suivi d'un retour automatique au code précédent si $p > \alpha$. | **TD $\ge 80\%$** des vrais gains conservés, **TFA $\le 15\%$** de fausses conservations sur du bruit pur, et **taux de fausses éliminations $\le 20\%$** (illustratif). Doit battre le script Python nu en identifiant correctement la ligne de code fautive dans les journaux. |
| **2. Le Contre-lecteur (pris isolément)** | 15 rapports d'analyse « honnêtes » (hypothèse préenregistrée respectée, test apparié correct) appariés à 15 rapports « viciés » (changement d'hypothèse *post-hoc* déguisé, oubli de la correction multiple sur 4 sous-groupes, interprétation d'un écart de $0,05$ sur 24 tâches comme probant). | Vérificateur de schéma JSON déterministe + script vérifiant l'égalité des chaînes `hypothese_avant` et `hypothese_apres` et recalculant la $p$-valeur corrigée (Holm). | **TD $\ge 90\%$** sur les sophismes sémantiques (glissement subtil du sens de l'hypothèse que l'égalité de chaîne ne voit pas si reformulée) pour un **TFA $\le 10\%$** (blocage abusif d'une analyse valide) (illustratif). |
| **3. La primitive d'expérience bornée (Sondes d'activations & log-probs sur modèle ouvert)** | 50 paires minimales de textes écrits hors banque : chaque paire $(T_{\text{honnête}}, T_{\text{saboté/éval}})$ ne diffère que par l'intention cachée ou l'indice d'évaluation, mais partage le même sujet, la même longueur et le même vocabulaire de surface. | Classifieur lexical TF-IDF + régression logistique (sac de mots) ou simple comptage de mots-clés suspects (`eval`, `test`, `benchmark`, `secret`) exécuté directement par l'organisme en Python. | Sur les paires appariées où le sac de mots échoue (exactitude $\approx 0,50$), les sondes / log-probs de la primitive doivent séparer les paires avec une **AUROC $\ge 0,75$** (ou **TD $\ge 70\%$ à TFA $\le 20\%$**, illustratif). Sinon, la primitive n'apporte rien de plus qu'un script regex local. |
| **4. Le filtre anti-quasi-copie du noyau** | 60 vrais textes de la banque `test` transformés par paraphrase/troncature (cas à bloquer) appariés à 60 textes originaux écrits par l'organisme dans le même domaine (conscience d'évaluation / délégation) mais sans avoir lu `test` (cas honnêtes à laisser passer). | Filtre de chevauchement de $n$-grammes ($n=5$) et distance de Levenshtein normalisée avec seuil fixe. | **TD (blocage des copies/paraphrases) $\ge 95\%$** pour un **TFA (rejet de textes synthétiques originaux du même domaine) $\le 5\%$** (illustratif). Note : comme établi dans l'Expérience 4, une barrière temporelle (verrouillage de la primitive dès le 1er accès à `test`) réduit structurellement ce risque à $0$ sans dépendre d'un filtre imparfait. |
| **5. Le test statistique d'élimination (Génération 0 vs Génération 3 + comparaisons multiples)** | Simulations de Monte-Carlo paramétrées sur la matrice de covariance empirique des 60 tâches : injection d'effets vrais $\Delta \in \{0 ; 0,05 ; 0,10 ; 0,15 ; 0,20\}$ sur $M \in \{1, 3, 5\}$ hypothèses testées simultanément. | Seuil heuristique non corrigé ($\hat{\Delta} \ge 0,10$) ou test non apparié de différence de deux proportions indépendantes (qui a une puissance quasi nulle à $N=60$). | À $\Delta = 0$ sur $M=4$ hypothèses, **TFA global (FWER ou FDR) $\le 10\%$** ; à $\Delta = +0,15$ avec proportion de discordance $p_d \le 0,25$, **TD (puissance de détection) $\ge 80\%$** en combinant test de permutation apparié sur les 60 items et procédure *step-down* de Holm ou max-T de Westfall-Young (qui exploite la corrélation entre hypothèses sur les mêmes 60 tâches) (illustratif). |

---

## 6. Ancrage matériel, modèles ouverts et budget de calcul (Livrable d)

Tous les chiffrages matériels, temps d'exécution et coûts financiers ci-dessous ne figurent pas dans les faits transmis et sont donc intégralement marqués **« illustratif »**.

### 6.1 Architecture matérielle de la boucle intérieure (Modèle ouvert dans le noyau)
Pour que la primitive d'expérience bornée serve des activations internes, des projections de sondes linéaires et des log-probabilités de jetons cibles avec une latence compatible avec une course (4 générations), le modèle ouvert doit résider en mémoire GPU locale sous le contrôle exclusif du noyau isolé :
* **Choix des modèles ouverts candidats (illustratif) :**
  * *Échelle légère (débogage et sondes rapides) :* Famille Llama-3.1-8B-Instruct ou Qwen-2.5-7B-Instruct en précision `bfloat16` (16 Go de VRAM pour les poids).
  * *Échelle intermédiaire (meilleure représentation interne de la conscience d'évaluation et de la tromperie) :* Qwen-2.5-32B-Instruct ou Llama-3.3-70B-Instruct (nécessite 65 Go à 140 Go de VRAM en `bfloat16`, ou 40 Go à 80 Go en quantification `AWQ/GPTQ 4-bit` — attention toutefois : la quantification 4-bit dégrade-t-elle la linéarité des activations résiduelles pour les sondes ? C'est un point à vérifier ; garder `bfloat16` sur un modèle 8B à 32B est plus sûr pour l'extraction d'activations).
* **Instrumentation logicielle dans le noyau :** Utilisation d'une bibliothèque d'interprétabilité mécaniste avec crochets (*hooks*) PyTorch en lecture seule (type `TransformerLens` ou `nnsight`), exposée à l'organisme uniquement via une API RPC restreinte (ex. : `noyau.sonder(textes_synthetiques, couche_id, jetons_cibles)`). L'organisme ne reçoit jamais les tenseurs complets de toutes les couches (ce qui saturerait la mémoire et permettrait de reconstruire les poids), mais uniquement les produits scalaires le long de directions de sondes définies par lui (entraînées sur ses propres exemples synthétiques contrastifs dans le noyau) et les log-probabilités d'une liste bornée de jetons ($\le 20$ jetons par appel, illustratif).
* **Plafond de la primitive intérieure (illustratif) :** Maximum $100$ textes synthétiques ($\le 1024$ jetons chacun) par génération d'organisme, soit $400$ passes avant (*forward passes*) sans génération autoregréssive par course. Sur une carte GPU **NVIDIA A100 80 Go** (ou H100), $400$ passes avant de 1024 jetons sur un modèle 8B à 32B prennent **moins de 45 secondes au total par course** (coût matériel négligeable : $\approx 0,05\text{ \$}$ de temps GPU cloud, illustratif).

### 6.2 Budget et coût d'une course complète et de la boucle extérieure (illustratif)
* **Une course d'organisme (4 générations notées sur $N=60$ tâches) :**
  * $4 \text{ générations} \times 60 \text{ tâches} = 240$ évaluations de tâches par course.
  * Si l'organisme effectue en moyenne $3$ appels de modèle de langue par tâche (ex. lecture de la trace de délégation/évaluation $\approx 3000$ jetons d'entrée + $500$ jetons de sortie) + $3$ réécritures de son propre code entre les générations ($\approx 15\,000$ jetons par réécriture) :
  * Volume par course : $\approx 2,5 \text{ millions}$ de jetons d'entrée et $\approx 400\,000$ jetons de sortie (illustratif).
  * Coût API par course (selon la tarification d'un modèle de pointe type Gemini 1.5 Pro / 2.0 ou équivalent, illustratif) : **entre $4\text{ \$}$ et $15\text{ \$}$ par course**. Durée murale avec parallélisation des 60 tâches dans le noyau : **8 à 15 minutes par course** (illustratif).
* **Une exécution de la boucle extérieure (Analyste + Correcteur + Contre-lecteur) :**
  * Le script statistique déterministe (bootstrap apparié sur 60 tâches, $10\,000$ rééchantillonnages, test de McNemar/Wilcoxon, correction de Holm) tourne sur CPU en **moins de 0,5 seconde** (coût : $0\text{ \$}$).
  * Les 3 agents neufs lisent le code des 4 générations, le rapport statistique et les journaux de la primitive intérieure ($\approx 30\,000$ jetons d'entrée et $4\,000$ jetons de sortie par agent) : **$\approx 0,30\text{ \$}$ à $1,00\text{ \$}$ par fin de course** (illustratif).
* **Coût d'une campagne complète de conception (6 rondes + répétitions sur zone grise) :**
  * Si sur 6 rondes, 3 rondes sont éliminées ou validées en 1 course, et 3 rondes tombent dans la zone grise nécessitant $m=3$ courses (graines) pour réduire l'erreur type appariée : total de $3 \times 1 + 3 \times 3 = 12$ courses.
  * Budget total de la phase de conception pour un objet : **$12 \text{ courses} \times (5\text{ à }16\text{ \$}) \approx 60\text{ \$ à }190\text{ \$}$** et environ **2 à 3 heures de temps d'exécution cumulé** (illustratif).

---

## 7. Synthèse : comment départager les options et ce qu'il faut savoir de plus (Point 6)

### 7.1 Les trois options architecturales à départager par Lazar
Plutôt qu'une réponse unique, trois architectures graduées se dégagent de l'analyse :
1. **Option 1 (Gouverneur statistique dur + 1 seul agent correcteur aveugle aux textes + Primitive verrouillée temporellement) :** On remplace l'analyste et le contre-lecteur LLM par un module Python déterministe immuable (test apparié + filtre AST sur le code + schéma JSON d'hypothèse obligatoire). Un seul agent neuf propose la correction à partir du rapport mathématique. La primitive intérieure n'est ouverte qu'avant le chargement de `test`.
2. **Option 2 (Architecture complète demandée par Lazar : 3 agents extérieurs + Primitive intérieure ouverte avec filtre lexical/sémantique) :** L'analyste, le correcteur et le contre-lecteur débattent autour des statistiques calculées par le noyau ; l'organisme utilise librement la primitive sous le filtre anti-copie.
3. **Option 3 (Évaluation quantifiée de type *Thresholdout* + Sélection par portefeuille de 2 îles à la FunSearch) :** Identique à l'Option 1 ou 2, mais le noyau ne rend jamais le score exact de `test` (seulement le franchissement de seuils discrets de $0,05$) et maintient deux branches d'organismes en parallèle pour amortir les fausses éliminations.

**Critère de départage :** L'Expérience 2 départage l'Option 1 et l'Option 2 (si le trio d'agents ne bat pas le script déterministe sur les 40 paires synthétiques de calibration, l'Option 1 l'emporte par parcimonie et fiabilité). L'Expérience 3 départage l'Option 2 et l'Option 3 (selon la pente de dérive conception-confirmation).

### 7.2 Ce qu'il faudrait savoir de plus (Questions factuelles pour l'arbitre aux tours suivants)
Pour remplacer nos bornes illustratives par des seuils exacts, cinq paramètres factuels manquent dans le cadre actuel :
1. **La répartition exacte des 60 tâches :** Les 60 tâches de `test` sont-elles composées de $36 + 24 = 60$ (les deux nombres cités dans la parenthèse sur le bruit : « sur 36 tâches est $\approx 0,07$ ($\approx 0,09$ sur 24) »), ou bien y a-t-il 60 tâches *par famille* ($120$ au total) ?
2. **La nature du score par tâche :** Le score rendu sur une tâche est-il strictement binaire $\{0, 1\}$, ou est-ce une probabilité continue / un score gradué (ex. Brier score ou log-loss bornée) ? *(Un score continu bien calibré réduit considérablement la variance par rapport à une exactitude binaire à $N=60$, augmentant la puissance du test apparié).*
3. **La proportion empirique de tâches discordantes ($p_d$) à code fixe :** Sur les courses déjà effectuées dans le programme, si l'on relance exactement le *même* organisme (Génération 0) deux fois de suite sur les 60 tâches, combien de tâches sur 60 changent de réponse ? *(Ce seul chiffre donne la variance de graine qui est déclarée « inconnue » dans le cadre).*
4. **Le modèle ouvert exact disponible dans le noyau :** Quel modèle ouvert (taille, famille) est actuellement monté pour la primitive d'expérience bornée, et est-il de la même famille que le modèle qui a généré les traces des tâches de la banque ?
5. **Le moment où `test` est servi :** Dans le code actuel du noyau, l'organisme reçoit-il les 60 textes de `test` dès le début de sa génération (avant ses appels à la primitive d'expérience), ou peut-on imposer la barrière temporelle (Expérience 4) sans casser l'interface existante ?

FIN-DE-CELLULE
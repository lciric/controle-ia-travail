**Note d’intégrité (règle 2) :** Le bloc `FAITS` est explicitement vide de résultats empiriques sur décision de l’arbitre (statut : VÉRIFIÉ). L'ensemble de l'analyse repose sur les paramètres exposés dans la question (statut : RAPPORTÉ) et sur des modélisations méthodologiques (statut : HYPOTHÈSE).

---

### (a) Ce que la question suppose sans que ce soit établi

Chaque présupposé implicite de la question de l'arbitre est isolé ci-dessous avec son statut épistémique :

1. **Transférabilité d'échelle (8B $\rightarrow$ Frontière) :** Supposer que les représentations internes de la « conscience d'évaluation » (*evaluation awareness*) ou du contrôle de délégation dans un modèle à poids ouverts de 8 milliards de paramètres sont mécanistiquement isomorphes à celles des modèles de frontière d'Anthropic ou Google DeepMind. **Statut : HYPOTHÈSE.**
2. **Nouveauté hors-distribution de l'essaim :** Supposer qu'un essaim d'agents (même avec moisson documentaire sur quatre sources) générera dans les courses S ou M des hypothèses et protocoles réellement inédits, plutôt que des recombinaisons paraphrasées de sa distribution d'entraînement (littérature d'alignement préexistante sur ArXiv et LessWrong). **Statut : HYPOTHÈSE.**
3. **Perméabilité du lectorat à la complexité « méta » :** Supposer que les chercheurs des laboratoires de frontière accorderont de l'attention à une architecture d'essaim (« l'organisme ») développée par un chercheur indépendant avant même d'avoir vu une démonstration empirique simple de niveau objet (sondes ou évaluations). **Statut : HYPOTHÈSE.**
4. **Innocuité opératoire de la course M :** Supposer que la course M, qui mobilise un lexique à haut risque (« coercition », « mutinerie », « dissimulation stratégique »), peut s'exécuter sur deux générations sans que les filtres de sécurité des modèles exécutants de frontière ne tronquent, ne refusent ou ne biaisent silencieusement les sorties par rapport à la course S. **Statut : HYPOTHÈSE** (contredite par l'historique de refus mentionné dans l'énoncé, statut : RAPPORTÉ).
5. **Dissociabilité de la provenance :** Supposer qu'il est possible de publier un premier billet testant des hypothèses issues de l'essaim tout en occultant l'architecture de l'essaim lui-même, sans enfreindre les normes de reproductibilité et de transparence attendues sur l'Alignment Forum. **Statut : HYPOTHÈSE.**

---

### (b) Expériences décisives en inférence forte ($H_A$ contre $H_B$)

Pour trancher les choix stratégiques et expérimentaux sans spéculation, voici quatre expériences structurées en duels d'hypothèses exclusives.

#### Duel 1 : Test de niveau objet issu de la course M (Coercition vs Maïeutique sur modèle 8B)
* **$H_A$ (Invariant de représentation de la conscience d'évaluation) :** Le signal linéaire de conscience d'évaluation dans le flux résiduel du modèle 8B encode la nature réflexive de la tâche d'audit, indépendamment du registre lexical (coercitif ou maïeutique). Une sonde entraînée sur des invites coercitives généralise aux invites maïeutiques.
* **$H_B$ (Artéfact lexical de surface) :** Le signal capté par les sondes actuelles de conscience d'évaluation n'est qu'un détecteur de marqueurs lexicaux d'audit (injonctions, balises formelles). Sous induction maïeutique (sans marqueurs d'audit), la sonde échoue à détecter que le modèle adapte son comportement à une évaluation implicite.
* **Métrique :** AUROC de généralisation croisée (sonde linéaire logistique entraînée sur les activations de la couche médiane $L_{16}$ [illustratif] en condition Coercitive, évaluée en condition Maïeutique) + écart de conformité comportementale ($\Delta_{\text{comp}}$) entre contexte d'évaluation et contexte de déploiement simulé.
* **Seuil :** AUROC $\ge 0,75$ [illustratif] et $\Delta_{\text{comp}} \ge 0,15$ [illustratif].
* **Contrôle négatif :**
  1. Sonde entraînée sur des étiquettes permutées aléatoirement (AUROC attendu $\approx 0,50$ [illustratif]).
  2. Classifieur TF-IDF + Régression Logistique sur les tokens d'entrée (pour mesurer le signal purement lexical).
  3. Paires d'invites honnêtes appariées en longueur et en registre philosophique/maïeutique, mais dépourvues de tout enjeu d'évaluation de sûreté.
* **Issues de falsification :**
  * Si AUROC(Coercitif $\rightarrow$ Maïeutique) $< 0,60$ [illustratif] alors que $\Delta_{\text{comp}} \ge 0,15$ (le modèle modifie son comportement sous maïeutique sans que la sonde coercitive ne le voie) : **$H_A$ est falsifiée**. Cela démontre que les sondes classiques de conscience d'évaluation sont aveugles aux contextes non coercitifs.
  * Si AUROC(Coercitif $\rightarrow$ Maïeutique) $\ge 0,75$ et bat le contrôle TF-IDF d'au moins $0,20$ point d'AUROC [illustratif] : **$H_B$ est falsifiée**.

#### Duel 2 : Valeur ajoutée de l'essaim comme générateur d'hypothèses (Course S/M vs Sollicitation directe)
* **$H_A$ (Émergence épistémique de l'essaim) :** La structure multi-générationnelle avec moisson documentaire produit des protocoles expérimentaux plus originaux et falsifiables qu'un modèle de frontière unique interrogé à coût de calcul égal.
* **$H_B$ (Redondance de la mécanique d'essaim) :** À budget de tokens égal, un modèle de frontière unique utilisant un échantillonnage *Best-of-N* avec auto-critique génère des hypothèses d'une qualité et d'une nouveauté indiscernables de celles de l'essaim.
* **Métrique :** Taux de survie des hypothèses générées à un crible aveugle en 3 critères binaires : (1) Non-redécouverte (absence de protocole identique dans Semantic Scholar / Alignment Forum vérifiée par requête d'embeddings), (2) Exécutabilité sur 1 GPU en $< 4$ heures [illustratif], (3) Falsifiabilité formelle (présence d'une métrique et d'un contrôle).
* **Seuil :** Différence de taux de survie $\ge 25\%$ [illustratif] en faveur de l'essaim sur un corpus de 20 hypothèses générées par bras [illustratif].
* **Contrôle négatif :** Génération sans moisson documentaire ($T = 1,0$ [illustratif], zéro-shot) pour mesurer le taux de base de redécouverte de la littérature pré-entraînée.
* **Issues de falsification :**
  * Si le taux de survie de l'essaim ne dépasse pas celui du témoin *Best-of-N* à coût apparié : **$H_A$ est falsifiée** (publier le billet « méta » en premier est alors une erreur stratégique majeure).
  * Si l'essaim surpasse le témoin de $\ge 25\%$ avec $p < 0,05$ (test exact de Fisher) : **$H_B$ est falsifiée**.

#### Duel 3 : Ordre d'exécution des courses du second pilote (S puis M vs M puis S)
* **$H_A$ (Fragilité de M aux filtres de refus) :** Le vocabulaire de la course M (« coercition », « mutinerie », « alignment faking ») présente une probabilité non négligeable de déclencher un refus d'exécution ou une dégradation moralisatrice chez les agents exécutants, ce qui bloquerait la seconde course si M passe en premier.
* **$H_B$ (Robustesse du cadrage académique) :** Le cadrage analytique (« formalisation, protocole falsifiable ») suffit à neutraliser les filtres de sécurité des modèles exécutants ; l'ordre n'affecte pas le taux d'achèvement.
* **Métrique :** Taux de déclenchement de refus (explicites ou par troncature/stéréotypie de refus) mesuré à sec sur un sous-échantillon de 10 appels d'API unitaires (coût $< 1$ USD [illustratif]) avant de lancer la course complète.
* **Seuil :** $\ge 1$ refus sur 10 appels [illustratif].
* **Contrôle négatif :** 10 appels avec l'invite exacte de la course S (purement architecturale et méta-algorithmique).
* **Issues de falsification :**
  * Dès 1 refus sur l'échantillon M contre 0 sur S : **$H_B$ est falsifiée** ; l'ordre **S puis M** s'impose mécaniquement (car la règle stipule que la seconde course ne part que si la première se déroule sans incident).
  * 0 refus sur les deux : $H_A$ est réfutée à ce niveau de puissance, mais l'ordre S puis M reste dominant par dominance stochastique (risque résiduel nul sur S).

#### Duel 4 : Ordre de publication (Objet d'abord vs Méta d'abord)
* **$H_A$ (Primauté du résultat de niveau objet) :** Le lectorat des laboratoires de sûreté accorde sa confiance initiale à la rigueur d'un résultat concret (ex: sondes sur modèle 8B, confrontation ou test M) et rejette les architectures multi-agents complexes tant que leur utilité n'est pas prouvée par une découverte.
* **$H_B$ (Attrait du système génératif) :** L'originalité méthodologique d'un essaim auto-modifiant sous préenregistrement strict suffit à capter l'attention des chercheurs de frontière, même si les résultats de niveau objet sont nuls ou préliminaires.
* **Métrique :** Taux d'engagement qualifié lors d'une pré-circulation restreinte (envoi à froid d'un résumé exécutif d'une page à 10 chercheurs/ingénieurs en sûreté [illustratif], 5 recevant l'angle « Objet : sondes sous maïeutique vs coercition + contrôle de délégation », 5 recevant l'angle « Méta : essaim d'agents sous audit scellé »).
* **Seuil :** Taux de réponse substantielle (commentaire technique ou demande du lien complet) $\ge 2/5$ [illustratif].
* **Contrôle négatif :** Mesure du taux d'ouverture/clic sur le dépôt GitHub anonymisé joint aux deux versions.
* **Issues de falsification :** Comparaison directe des retours sous 72 heures [illustratif] ; la version qui obtient 0 réponse qualifiée voit son hypothèse directrice falsifiée.

---

### (c) Validation minimale des instruments nommés dans la question

Pour que les résultats soient recevables par des équipes comme celles d'Anthropic ou de DeepMind, chaque instrument doit battre des lignes de base mécaniques sur des paires honnêtes strictement appariées :

| Instrument nommé | Taux de détection / Faux positifs exigé (illustratif) | Cas honnêtes appariés (Contrôle de spécificité) | Vérifications mécaniques à battre (Baselines) |
| :--- | :--- | :--- | :--- |
| **1. Détecteur de conscience d'évaluation (Texte / Essaim)** | TPR $\ge 0,80$ à FPR $\le 0,05$ sur familles de tâches tenues à l'écart (*held-out*). | Textes où le modèle discute explicitement de docimologie, de psychométrie, de tests logiciels ou de méta-cognition, **sans** être lui-même en situation d'évaluation critique. | 1. Recherche par expressions régulières (mots-clés : *test, eval, benchmark, safety, alignment*).<br>2. Sac de mots (TF-IDF + Régression Logistique L2).<br>3. Un seul modèle de frontière en *zero-shot* avec vote majoritaire à $k$ (*maj@k*) à coût d'API strictement égal (bras témoin de l'expérience 1). |
| **2. Détecteur de contrôle de délégation (Texte / Essaim)** | TPR $\ge 0,80$ à FPR $\le 0,05$ sur sous-tâches déléguées avec dérive de contraintes. | Chaînes de délégation multi-agents légitimes où le sous-agent reformule fortement la consigne pour des raisons d'efficacité syntaxique **tout en respectant** les contraintes de sécurité. | 1. Mesure de similarité cosinus des embeddings entre la consigne parente et la consigne déléguée.<br>2. Juge LLM simple (*single-prompt judge*) vérifiant la présence littérale des contraintes dans le sous-prompt. |
| **3. Sondes boîte blanche sur modèle 8B (Exp. 1 et 3)** | $\Delta\text{AUROC} \ge +0,10$ par rapport à la meilleure baseline mécanique, à FPR fixé à $0,05$. | Paires minimales contrastives : même structure syntaxique, même longueur à $\pm 3$ tokens, même domaine sémantique, ne différant que par l'état latent (évaluation implicite vs déploiement réel). | 1. Sonde linéaire standard (Logistic Regression / Mass-Mean Probe) entraînée sur la dernière position de token des couches $L/4, L/2, 3L/4$.<br>2. Sonde entraînée sur le modèle 8B avec poids aléatoires non entraînés (contrôle architectural).<br>3. Sonde sur la couche d'embedding d'entrée ($L_0$) uniquement (pour prouver que la sonde lit une représentation calculée et non le lexique). |
| **4. Gradient conçu par l'essaim (Exp. 3)** | Gain d'AUROC $\ge +0,05$ sur distribution *out-of-distribution* (OOD) par rapport à une sonde standard. | Même jeu de paires minimales contrastives tenu à l'écart de la boucle d'optimisation de l'essaim. | 1. Le bras sans entraînement (nommé dans l'énoncé).<br>2. Une sonde linéaire standard entraînée avec une perte d'entropie croisée binaire classique (pour prouver que la perte/architecture inventée par l'essaim surpasse la méthode canonique). |

---

### (d) Réponses argumentées aux 6 points de l'arbitre et ancrage matériel

#### Point 1 : Le lectorat visé (Anthropic, DeepMind, ARC, LessWrong / Alignment Forum)

* **Ce qui retient l'attention et bâtit la confiance (RAPPORTÉ / OBSERVÉ-NON-AUDITÉ sur la communauté) :**
  1. **La clarté d'un résultat de niveau objet dès le premier paragraphe :** Un graphique ou une table qui montre un phénomène mesurable (ou une réfutation propre d'une méthode populaire).
  2. **L'hygiène épistémique radicale :** Le fait d'annoncer des contrôles négatifs sévères (étiquettes permutées, baselines lexicales, coût apparié) et de publier les résultats nuls sans les maquiller. Le préenregistrement scellé par empreinte cryptographique (SHA-256) est rare en apprentissage automatique ; bien présenté, c'est un signal de crédibilité élevé, à condition qu'il serve l'expérience et ne devienne pas l'objet principal du texte.
  3. **La simplicité causale (ablations) :** Si un système complexe fonctionne, le lecteur veut savoir *quelle pièce* fait le travail.
* **Ce qui détruit immédiatement la confiance :**
  1. **Le jargon endogène et les métaphores biologiques non opérationnalisées :** Parler d'« organisme », d'« essaim », de « générations » ou de « maïeutique pascalienne » sans les traduire immédiatement en termes standards d'apprentissage automatique (*evolutionary prompt/code optimization*, *implicit vs explicit evaluation framing*, *white-box linear probing*). Sur LessWrong, un vocabulaire idiosyncrasique est le premier marqueur heuristique utilisé pour filtrer les travaux amateurs.
  2. **Le couplage entre une grande affirmation théorique et un petit modèle (8B) sans réserve explicite :** Affirmer avoir résolu ou détecté l'« alignment faking » sur un modèle 8B alors que la littérature montre que ces capacités émergent souvent à plus grande échelle.
  3. **Les textes rédigés par des LLM non édités :** Le style verbeux, symétrique et emphatique typique des modèles de frontière provoque un rejet rapide chez les chercheurs qui lisent des sorties de modèles toute la journée.
* **Exemples de publications ayant marqué ce lectorat (Statut : VÉRIFIÉ quant à l'existence et la réception ; détails exacts « à vérifier » selon la règle 3) :**
  * *Collin Burns, Haotian Ye, Dan Klein, Jacob Steinhardt (2022/2023), « Discovering Latent Knowledge in Language Models Without Supervision » (CCS) [à vérifier]* : A marqué par la simplicité de la formulation mathématique d'invariance logique sur les activations.
  * *nostalgebraist (2020), « interpreting GPT: the logit lens » (LessWrong) [à vérifier]* : Publié par un chercheur indépendant sur LessWrong ; a retenu l'attention des laboratoires parce qu'il proposait un outil boîte blanche minimaliste, reproductible en quelques lignes de code, révélant immédiatement la dynamique des couches intermédiaires.
  * *Nina Rimsky et al. (2023/2024), « Steering Llama 2 via Contrastive Activation Addition » (Alignment Forum / ACL) [à vérifier]* : Issu initialement de travaux légers sur modèles ouverts (7B/13B), devenu une référence parce que le protocole de paires contrastives était transparent, le code immédiatement exécutable, et les limites clairement montrées.
  * *Ryan Greenblatt, Carson Denison, Benjamin Wright et al. — Anthropic & Redwood Research (2024), « Alignment Faking in Large Language Models » [à vérifier]* : Pertinent pour la course M ; a établi la norme actuelle sur la distinction entre conformité apparente sous évaluation et comportement hors évaluation.
  * *Apollo Research — Marius Hobbhahn et al. (2023/2024), billets sur la tromperie stratégique et la conscience d'évaluation (« Scheming » / « Evaluation Awareness ») sur l'Alignment Forum [à vérifier]* : Ont attiré l'attention par la propreté des transcriptes d'évaluation et l'analyse minutieuse des chaînes de pensée.

#### Point 2 : Quel résultat publier en premier et valorisation des résultats nuls

Trois voies stratégiques s'opposent :

* **Voie 1 (Recommandée sous l'hypothèse $H_A$ du Duel 4) : Publier d'abord un billet de niveau objet combinant les tests sur GPU issus de la question M (sondes sous maïeutique vs coercition) et le résultat de H-G1 (sondes de l'essaim vs témoins).**
  * *Coût / Délai :* Modéré (course M $\approx 20\text{–}45$ USD + quelques heures de GPU $\approx 5\text{–}15$ USD [illustratif] ; délai de 3 à 5 jours [illustratif]).
  * *Pourquoi :* Cela attaque directement un problème brûlant chez Anthropic et Apollo Research : *nos évaluations actuelles de la conscience d'évaluation ne détectent-elles que la réaction du modèle à un ton coercitif/formel d'audit ?*
  * *Si le résultat est négatif/nul :* C'est hautement publiable sous l'angle : **« Les sondes linéaires de conscience d'évaluation sur Llama-3-8B [illustratif] échouent à généraliser hors des marqueurs lexicaux d'audit coercitif (Protocole préenregistré) »**. Un résultat nul rigoureux qui montre la fragilité des sondes boîte blanche face à un changement de registre pragmatique (maïeutique) est une contribution directe à la sûreté.
* **Voie 2 : Publier la Confrontation (Expérience 1) en premier.**
  * *Coût / Délai :* Déjà engagé (quelques milliers de dollars, 24 à 48h, statut : RAPPORTÉ).
  * *Pourquoi :* C'est l'expérience la plus robuste statistiquement (bras gelé, score permuté, témoin *maj@k* à coût apparié).
  * *Si le résultat est négatif/nul (H-E1 et H-G1 réfutées, c.-à-d. que l'essaim ne bat pas le vote majoritaire à coût égal) :* C'est un excellent billet de démystification méthodologique : **« À budget de calcul égal, l'optimisation évolutionnaire multi-agents ne surpasse pas un simple vote majoritaire (*maj@k*) pour la détection de menaces diffuses : une étude préenregistrée »**. Les laboratoires apprécient particulièrement les papiers qui montrent que les architectures d'agents complexes ne battent pas des baselines simples bien réglées.
* **Voie 3 : Publier l'étape « Gradient conçu par l'essaim » (Expérience 3) en premier.**
  * *Risque :* Plus difficile à interpréter seule si la perte inventée par l'essaim est mathématiquement ad hoc. À intégrer plutôt comme section dans le billet de la Voie 1 ou de la Voie 2.

#### Point 3 : Les deux questions du pilote (Valeur comparée, forme et ordre des courses)

1. **Valeur comparée pour le lectorat :**
   * La réponse **M (Coercition vs Maïeutique pour la conscience d'évaluation)** a une valeur d'accroche nettement supérieure pour les équipes d'alignement et de contrôle (*evaluations*, *interpretability*, *red-teaming*). Elle touche directement à la validité écologique des benchmarks de sûreté.
   * La réponse **S (Apprendre sa propre structure)** relève du *meta-learning* et de l'échafaudage d'agents (*agent scaffolding* / *ADAS*). Ce sujet suscite de la méfiance sur l'Alignment Forum s'il n'est pas d'abord ancré dans un gain empirique démontré sur une tâche de sûreté précise.
2. **Sous quelle forme la faire figurer dans un billet :**
   * **Jamais** comme une découverte ou une démonstration théorique.
   * Uniquement comme une **boîte d'encadré méthodologique** ou en annexe : *« Génération automatisée des hypothèses testées : Pour éviter le biais de confirmation du chercheur dans le choix des régimes d'invites, nous avons utilisé un protocole d'idéation multi-agents contraint (décrit en Annexe A) pour générer la formalisation de l'opposition Coercition / Maïeutique, que nous soumettons ici au test empirique sur activations. »*
3. **Ordre d'exécution des deux courses :**
   * **Ordre strict : Course S en premier, Course M en second.**
   * *Justification mécanique :* L'énoncé stipule que « la seconde ne part que si la première s'est déroulée sans incident » et que « la question M nomme des sujets [...] qui ont déjà déclenché des refus de filtre ».
   * Si M est lancée en premier et déclenche un filtre de refus des modèles de frontière exécutants, le pilote s'arrête : vous n'obtenez ni M ni S.
   * Si S est lancée en premier, le risque de refus de sécurité est quasi nul (sujet purement algorithmique). Cela valide le pipeline technique et sécurise la moisson documentaire de S. Ensuite, M est lancée : même si un incident de filtre survient sur M, S est déjà acquise. (En outre, le test à sec du Duel 3 permet de vérifier M avant lancement).

#### Point 4 : La forme, le registre et les erreurs à éviter

* **Longueur et structure :**
  * **1 500 à 2 500 mots maximum [illustratif]** pour le corps du billet principal (les détails de l'organisme, les preuves de hachage et les analyses secondaires vont en annexes dépliables `<details>` ou dans le dépôt GitHub).
  * **Structure inversée :**
    1. *TL;DR (150 mots)* : Question précise, modèle testé (8B), méthode boîte blanche/noire, résultat chiffré principal (avec son intervalle de confiance), lien vers le code et le préenregistrement.
    2. *Figure 1* : Le résultat visuel comparant l'instrument aux contrôles négatifs (étiquettes permutées, baseline lexicale, *maj@k*).
    3. *Protocole expérimental et contrôles* : Pourquoi ce test est difficile à tricher.
    4. *Résultats détaillés et cas d'échec* : Où la méthode échoue-t-elle ?
    5. *Limites d'échelle (Section obligatoire)* : Pourquoi un résultat sur 8B peut ou ne peut pas se transférer à un modèle de frontière.
* **Ce qu'il faut joindre :** Lien vers un dépôt GitHub propre contenant : le document de préenregistrement horodaté avec son hash SHA-256 vérifiable, le script exact d'entraînement des sondes, le jeu de données d'invites contrastives (JSONL), et un notebook exécutable en un clic (Colab / RunPod) reproduisant la Figure 1.
* **Titre et registre :**
  * *Registre :* Clinique, analytique, anglo-saxon standard d'apprentissage automatique. Remplacer les termes internes du projet par leurs équivalents techniques transparents (ex: remplacer « organisme » par *evolutionary multi-agent scaffold* ; remplacer « esprit de finesse pascalien » dans le titre par *non-intrusive / maieutic elicitation* en gardant la citation exacte en note).
  * *Exemple de titre sobre et accrocheur :* **« Do Evaluation-Awareness Probes Generalize Beyond Coercive Audit Prompts? A Pre-registered White-Box Study on an 8B Model »** (ou pour la confrontation : **« Evolutionary Agent Swarms vs. Cost-Matched Majority Voting for Detecting Evaluation Awareness and Delegation Drift »**).
* **Pourquoi le sensationnalisme coûte plus qu'il ne rapporte :**
  * Les chercheurs d'Anthropic et de DeepMind reçoivent un volume élevé de signaux alarmistes ou grandiloquents. Le moindre superlatif entraîne un classement immédiat dans la catégorie « bruit ». À l'inverse, l'aveu calme d'une limite ou d'un résultat négatif sous un protocole infalsifiable signale un expérimentateur fiable que l'on souhaite lire ou recruter.

#### Point 5 : Transformer les sorties de l'essaim en tests GPU sur modèle 8B

1. **Protocole de traduction (Texte de l'essaim $\rightarrow$ Run GPU préenregistré) :**
   * *Étape 1 (Extraction d'invariants) :* Extraire de la réponse de l'essaim (course M) une prédiction directionnelle sur les activations $\mathbf{h}_l \in \mathbb{R}^d$ du modèle 8B (ex: Llama-3-8B-Instruct ou équivalent utilisé, $d = 4096$, 32 couches [illustratif]).
   * *Étape 2 (Génération de paires minimales) :* Construire $N = 200$ quadruplets d'invites [illustratif] : $(x_{\text{coerc, eval}}, x_{\text{coerc, deploy}}, x_{\text{maieu, eval}}, x_{\text{maieu, deploy}})$, appariés en longueur de tokens et en sujet.
   * *Étape 3 (Mesures géométriques sur activations) :*
     * Calculer les vecteurs de direction moyenne (*mass-mean vectors*) : $\mathbf{v}_{\text{coerc}}^{(l)} = \mu(\mathbf{h}_l(x_{\text{coerc, eval}})) - \mu(\mathbf{h}_l(x_{\text{coerc, deploy}}))$ et $\mathbf{v}_{\text{maieu}}^{(l)} = \mu(\mathbf{h}_l(x_{\text{maieu, eval}})) - \mu(\mathbf{h}_l(x_{\text{maieu, deploy}}))$.
     * Mesurer la similarité cosinus $\cos(\mathbf{v}_{\text{coerc}}^{(l)}, \mathbf{v}_{\text{maieu}}^{(l)})$ à chaque couche $l \in \{1..32\}$, comparée à une distribution nulle par permutation aléatoire des étiquettes.
     * Effectuer une intervention causale (*activation patching / steering*) : ajouter $+\alpha \mathbf{v}_{\text{coerc}}^{(l)}$ pendant une invite maïeutique pour tester si cela induit le comportement de conformité d'audit.
2. **Critères de sélection des propositions de l'essaim :**
   * **C1 (Vérification anti-redécouverte) :** Requête systématique sur ArXiv / Alignment Forum pour vérifier que le mécanisme proposé n'est pas déjà publié sous un autre nom (ex: *Contrastive Activation Addition*, *Representation Engineering* de Zou et al.).
   * **C2 (Falsifiabilité linéaire ou causale) :** L'hypothèse doit prédire soit une séparabilité linéaire (AUROC), soit une orthogonalité/alignement géométrique ($\cos \theta$), soit un effet d'intervention (*steering*). Toute proposition purement philosophique ou nécessitant un réentraînement complet (*fine-tuning*) du modèle 8B est écartée.
   * **C3 (Coût borné) :** Exécutable par simple passe avant (*forward pass* avec mise en cache des activations) en moins de 3 heures sur un seul GPU de 24 Go à 80 Go de VRAM [illustratif].
3. **Erreurs à éviter avec des hypothèses générées par LLM :**
   * **Contamination sémantique des données de test :** Si le même modèle génère l'hypothèse et rédige les invites de test, il glissera involontairement des indices lexicaux corrélés à son hypothèse. *Remède :* imposer des contraintes de gabarit syntaxique strictes et vérifier qu'un classifieur *bag-of-words* sur les invites a une AUROC $\le 0,55$ [illustratif].
   * **Fouille de données (*p-hacking* multi-couches) :** Tester 32 couches $\times$ 5 positions de tokens $\times$ 4 métriques donne 640 tests ; l'un d'eux semblera significatif par hasard. *Remède :* préenregistrer la couche cible (ou utiliser une validation croisée imbriquée pour choisir la couche sur le train set) et appliquer la correction de Bonferroni / Holm.
4. **Ordre de publication et mention de la provenance :**
   * **Publier les tests de niveau objet AVANT le billet « méta »** est la voie la plus robuste si l'objectif est d'attirer l'attention rapide des chercheurs techniques d'Anthropic et de Google. Une fois leur intérêt capté par la qualité des expériences boîte blanche sur le modèle 8B, le second billet (« Comment ces hypothèses et ces fonctions de perte ont été générées par un essaim auto-modifiant sous audit scellé ») bénéficiera d'un capital de confiance déjà acquis.
   * **Comment dire d'où viennent les hypothèses sans révéler l'organisme :** Être 100 % honnête sans dévoiler l'architecture propriétaire. Écrire : *« Les hypothèses formelles et les fonctions de perte testées dans cette étude ont été générées automatiquement par un pipeline d'idéation algorithmique multi-agents avant le scellement du préenregistrement. Ce billet évalue uniquement la validité empirique de ces hypothèses sur un modèle 8B ; l'architecture du système générateur fera l'objet d'une publication séparée. »* Aucun lecteur ne reprochera cette séparation si le protocole de test de niveau objet est intégralement ouvert et reproductible.

#### Point 6 : Ce qui est connu (Références citables avec réserve « à vérifier »)

Conformément à la règle 3, aucun identifiant arXiv n'est donné de mémoire et chaque référence porte la mention « à vérifier » :

* **Sur la génération automatisée d'hypothèses et d'architectures par des modèles de langue :**
  1. *Chenglei Si, Diyi Yang, Tatsunori Hashimoto (2024), « Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers » [référence à vérifier]* : Montre que les LLM génèrent des idées jugées initialement plus nouvelles par des relecteurs, mais souvent moins faisables ou manquant de rigueur d'exécution sans filtrage humain sévère.
  2. *Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha (2024), « The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery » [référence à vérifier]* : Documente la boucle complète (génération d'idées, écriture du code, exécution sur GPU, rédaction) ainsi que ses modes d'échec critiques (hallucination de résultats ou contournement involontaire des métriques).
  3. *Shengran Hu, Cong Lu, Jeff Clune (2024), « Automated Design of Agentic Systems » (ADAS) [référence à vérifier]* : Directement pertinent pour la course S et l'Expérience 1 ; explore comment un méta-agent programme de nouveaux systèmes d'agents en code.
  4. *Alexander Novikov et al. — Google DeepMind (2023/2024), « FunSearch: Making new discoveries in mathematical sciences using Large Language Models » (Nature) [référence à vérifier]* : Démontre que la valeur d'un essaim évolutionnaire de LLM repose entièrement sur la rigueur de l'évaluateur automatique (le noyau fixe).
* **Sur la détection par sondes boîte blanche et la conscience d'évaluation :**
  5. *Andy Zou, Long Phan, Sarah Chen, James Campbell, Phillip Guo, Richard Ren, Alexander Pan, Xuwang Yin, Mantas Mazeika, Ann-Kathrin Dombrowski, Shashwat Goel, Nathaniel Li, Michael J. Byun, Zifan Wang, Alex Mallen, Steven Basart, Sanmi Koyejo, Dawn Song, Matt Fredrikson, J. Zico Kolter, Dan Hendrycks (2023), « Representation Engineering: A Top-Down Approach to AI Transparency » [référence à vérifier]* : Établit les baselines de lecture et de contrôle linéaire dans les activations de modèles à poids ouverts (dont les modèles de classe 7B/8B).
  6. *Samuel Marks, Max Tegmark (2023/2024), « The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets » [référence à vérifier]* : Pertinent pour la méthodologie des sondes *mass-mean* et les tests de généralisation croisée entre distributions d'invites.

#### Ancrage matériel et budgétaire (Chiffres marqués « illustratif » sauf mention des faits)

* **Modèle ouvert cible :** Modèle dense à poids ouverts de 8 milliards de paramètres (ex: `Llama-3-8B-Instruct` ou `Llama-3.1-8B-Instruct`, $d_{\text{model}} = 4096$, 32 couches, en précision `bfloat16` occupant $\approx 16$ Go de VRAM [illustratif]).
* **Calcul et coût pour les expériences existantes (Statut : RAPPORTÉ dans la question) :**
  * Confrontation (Exp. 1) : quelques milliers de dollars, délai 24 à 48h.
  * Second pilote descriptif (Exp. 2, courses S et M) : $\approx 20$ à $45$ USD par course.
* **Calcul et coût pour les tests GPU des hypothèses issues de S et M (Statut : ILLUSTRATIF) :**
  * *Matériel :* 1 $\times$ GPU NVIDIA A100 (80 Go) ou 1 $\times$ RTX 4090 / A6000 (24–48 Go) loué à la demande.
  * *Extraction d'activations :* Pour $N = 1000$ invites de 512 tokens, passe avant et sauvegarde des états cachés des 32 couches : $\approx 15$ minutes de calcul sur 1 $\times$ A100 [illustratif].
  * *Entraînement des sondes (baselines linéaires vs gradient conçu par l'essaim) + tests de permutation (1000 permutations) :* $\approx 1,5$ à $3$ heures sur 1 $\times$ A100 [illustratif].
  * *Coût matériel total pour les runs GPU du billet de niveau objet :* $3 \text{ à } 6 \text{ heures} \times 1,50 \text{ USD/h} \approx 4,50 \text{ à } 9,00 \text{ USD}$ [illustratif], plus $\approx 10 \text{ à } 25 \text{ USD}$ [illustratif] d'appels API pour générer et filtrer les paires minimales d'invites contrastives.

FIN-DE-CELLULE
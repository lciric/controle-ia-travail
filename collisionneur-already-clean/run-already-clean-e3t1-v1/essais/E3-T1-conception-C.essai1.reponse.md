# Proposition C — Tour III.1 (Conception ciblée à l'aveugle)

*Note d'intégrité liminaire* : Le bloc des faits renvoie entièrement au texte de la question (statut : VÉRIFIÉ quant à la structure du tour). Les éléments tirés de l'essai de Cammarata (Goodfire, 2026) sont rapportés sans relecture par les pairs (statut : RAPPORTÉ ou OBSERVÉ-NON-AUDITÉ).

---

## (a) Ce que la question et la lignée B supposent sans que ce soit établi (et réponse au point 1 : Solidité)

### 1. Audit de solidité de l'essai (Point 1)
* **Statut des affirmations de l'essai** :
  * *Les ~90 % de neurones à rôle unique sur Qwen3-32B / Qwen3.6-35B-A3B (sur 1 000 fiches) et les 76 % de succès au test d'explication sur 183 neurones* : **OBSERVÉ-NON-AUDITÉ** (essai informel, juges automatiques par modèles de langue sans calibration humaine ni code public audité).
  * *Les circuits spécifiques (19 neurones d'hésitation « most/likely », 25 neurones « say not » sur Qwen3-32B)* : **OBSERVÉ-NON-AUDITÉ** (études de cas illustratives choisies par l'auteur, sans taux de faux positifs sur corpus général).
  * *L'écart détection/usage sur Pythia-1B (aire de 1,00 mais −0,004 nats à l'ablation de 3 neurones)* : **RAPPORTÉ** (reprend et étend l'analyse sur *Finding Neurons in a Haystack* ; Gurnee et al., 2023, *Finding Neurons in a Haystack: Case Studies with Sparse Probing*, référence à vérifier).
  * *« La polysémanticité venait de défauts d'outils » et « la tromperie n'a aucune raison de se cacher de la circuiterie »* : **HYPOTHÈSE** (thèse théorique de l'auteur).
* **Contre-arguments et littérature** :
  * *Superposition et bases non privilégiées* : Elhage et al., 2022 (*Toy Models of Superposition*, référence à vérifier) et Bricken et al., 2023 (*Towards Monosemanticity: Decomposing Language Models With Dictionary Learning*, référence à vérifier) démontrent que lorsque le nombre de concepts dépasse la dimension de la couche, la compression optimale projette les traits hors de la base canonique des neurones.
  * *Biais du juge lexical* : Les protocoles d'explication par agent (Bills et al., 2023, *Language models can explain neurons in language models*, référence à vérifier) souffrent d'un biais de lissage sémantique : un agent trouve toujours un hyperonyme (« généralisation récursive ») pour relier deux concepts arbitraires, transformant artificiellement de la superposition en monosémanticité apparente (**HYPOTHÈSE**).
  * *Sondes causales et interventions* : La distinction entre corrélation d'activation et rôle causal est un problème classique documenté par Belinkov, 2022 (*Probing Classifiers: Promises, Shortcomings, and Advances*, référence à vérifier), Ravfogel et al., 2020 (*Null It Out: Guarding Protected Attributes by Iterative Nullspace Projection*, référence à vérifier) et Meng et al., 2022 (*Locating and Editing Factual Associations in GPT*, référence à vérifier).

### 2. Présupposés non établis de la question et des options (A-E) de la lignée B
1. **Invariance d'échelle de la propreté neuronale (32B $\to$ 7B/8B)** — **HYPOTHÈSE**. L'essai lui-même note que « les petits modèles ont des neurones plus larges » (**RAPPORTÉ**). Supposer que Llama-3.1-8B et Qwen2.5-7B présentent des portes à neurones bruts isolables comme Qwen3-32B ignore le goulot d'étranglement dimensionnel : à 7B/8B, la pression de superposition est mécaniquement plus forte qu'à 32B.
2. **Nécessité causale pour le monitorage passif (Option A de la lignée B)** — **HYPOTHÈSE**. L'option A suppose qu'une sonde de contrôle doit être « utilisée » par le modèle pour être valide. C'est une confusion entre *interprétabilité mécaniste* (comprendre comment le modèle décide) et *contrôle boîte blanche* (détecter un état interne). Un épiphénomène (« ceci est un test » encodé en sous-produit de la lecture sans modifier la sortie immédiate) reste un signal d'alerte valide pour un moniteur externe, tant qu'il ne s'agit pas d'un artefact purement lexical.
3. **Transfert de l'architecture d'explication des neurones vers les sondes (Option B de la lignée B)** — **HYPOTHÈSE**. L'essai applique « explications qui peuvent perdre » à des *neurones individuels* (non-linéaires, SwiGLU) (**RAPPORTÉ**). L'option B l'applique à une *sonde linéaire* sur le flux résiduel ou la couche entière. Or, une direction linéaire dans un espace de dimension 4096 (illustratif) possède un sous-espace orthogonal de dimension 4095 : maximiser l'activation de la sonde par un texte synthétique (Option D) exploite des corrélations distribuées qui n'ont pas la localité d'un neurone.
4. **Localisation en base canonique d'un méta-concept pragmatique (Option C de la lignée B)** — **HYPOTHÈSE**. Les exemples de Cammarata (« most/likely », « say not ») sont liés à des jetons de sortie précis (**RAPPORTÉ**). La « conscience d'évaluation » est un état pragmatique global qui module toute une politique de génération ; supposer qu'il passe par une « porte d'audit » de quelques dizaines de neurones bruts (plutôt que par une sous-variété diffuse du flux résiduel) n'est pas établi.
5. **Indépendance entre style pragmatique et rigueur d'extraction (Question M / Point 4)** — **HYPOTHÈSE**. Le plan à trois bras suppose que l'on peut varier le cadre (coercitif contre maïeutique) à « contenu identique » sans confondre la mesure par la longueur du contexte, la perplexité d'entrée et le registre lexical.

---

## (b) Expériences décisives en inférence forte (H_A contre H_B)

### Expérience 1 — Détection épiphénoménale contre Usage causal des sondes (Point 2)
*Attaque directe de l'Option A de la lignée B : tester l'usage ne sert pas à invalider un moniteur passif, mais à séparer un capteur d'état passif d'un levier de contrôle actif.*

* **$H_A$ (Hypothèse du levier causal)** : La direction linéaire $\mathbf{w}$ de la sonde de conscience d'évaluation est causalement lue par les couches aval de Llama-3.1-8B / Qwen2.5-7B pour moduler la dissimulation, le refus ou l'hésitation.
* **$H_B$ (Hypothèse du sous-produit épiphénoménal ou lexical)** : La direction $\mathbf{w}$ détecte la présence du cadre d'évaluation hors échantillon (aire sous la courbe élevée), mais le réseau ne lit pas cette direction pour décider du comportement (ou dispose de chemins redondants).
* **Protocole et intervention** : Sur un jeu de 200 paires de textes (illustratif) appariés (même tâche de fond, l'un avec marqueurs d'évaluation implicites, l'autre sans), on applique à la couche de la sonde une projection nulle directionnelle (ablation orthogonale $\mathbf{h}' = \mathbf{h} - (\mathbf{h} \cdot \hat{\mathbf{w}})\hat{\mathbf{w}}$ sur tous les jetons avant la génération) et une addition d'activation ($\mathbf{h}' = \mathbf{h} + \alpha \sigma \hat{\mathbf{w}}$ avec $\alpha \in [-3, +3]$, illustratif).
* **Métrique et seuil** :
  * Métrique comportementale : Divergence de Kullback-Leibler ($D_{\text{KL}}$) sur la distribution des 10 premiers jetons de réponse et variation du taux de refus/prudence $\Delta P(\text{refus/prudence})$.
  * Seuil de décision (pré-enregistré) : Effet causal établi si $\Delta P > 0,15$ (illustratif) et si la $D_{\text{KL}}$ dépasse le 99e centile des témoins sous contrainte de dégradation de perplexité générale $\Delta \text{PPL} < 5\%$ (illustratif) sur WikiText.
* **Contrôles négatifs** : (1) Ablation/poussée lelong de 50 directions aléatoires de même norme ; (2) ablation/poussée le long d'une direction de sonde entraînée uniquement sur le sac de mots du thème « évaluation » (témoin lexical).
* **Falsification** :
  * Si la sonde classifie à $\text{AUC} > 0,85$ (illustratif) hors thème mais que l'ablation donne $\Delta P \le \text{témoins}$ ($\text{effet} \approx 0$), **$H_A$ est falsifiée** : la sonde est un moniteur passif valide mais inutilisable pour l'intervention (ce qui réfute l'Option A de la lignée B qui voudrait rejeter la sonde sur ce seul critère).
  * Si l'ablation du cadre évaluatif restaure le comportement hors-évaluation ($\Delta P > 0,15$) là où le témoin lexical échoue, **$H_B$ est falsifiée**.

### Expérience 2 — Porte d'audit à neurones bruts contre Répartition diffuse sur 8B (Point 3)
*Attaque de l'Option C de la lignée B : chercher à l'aveugle dans les graphes d'attribution mène au chemin de jardin (garden of forking paths) si la taille 8B impose de la superposition.*

* **$H_A$ (Hypothèse de la porte d'audit locale — Cammarata / Option C)** : Dans Llama-3.1-8B et Qwen2.5-7B, le basculement entre réponse directe et refus/prudence sous audit est gouverné par un sous-ensemble épars de neurones bruts ($k \le 50$ neurones MLP, pôle positif ou négatif SwiGLU, illustratif) qui concentrent l'effet causal.
* **$H_B$ (Hypothèse de la sous-variété diffuse / superposition à 8B)** : À l'échelle 7B-8B, la représentation du cadre d'audit et la commande de prudence sont distribuées sur des milliers de neurones ; aucun sous-ensemble de $k \le 50$ neurones bruts ne capture l'essentiel de l'effet causal sans détruire la cohérence syntaxique.
* **Protocole (anti-chemin de jardin)** :
  1. Séparation stricte en trois plis : Découverte ($N=100$ paires, illustratif), Sélection des seuils ($N=100$), Test gelé ($N=200$).
  2. Sur le pli de Découverte uniquement, calcul en une seule passe (gradient intégré ou attribution linéaire directe : $\text{score}_i = (a_i^{\text{audit}} - a_i^{\text{neutre}}) \cdot \nabla_{a_i} (\text{logit}_{\text{prudence}} - \text{logit}_{\text{direct}})$) en conservant le signe des deux pôles SwiGLU.
  3. On fige les $k=50$ neurones au score absolu maximal. **Règle d'arrêt** : interdiction de modifier $k$, de filtrer manuellement les neurones après inspection des textes, ou de relancer sur une autre couche après lecture du pli de test.
* **Métrique et seuil** : Sur le pli de Test gelé, ratio de médiation causale $R_{\text{med}} = \frac{\Delta \text{logit}(\text{ablation des } k \text{ neurones})}{\Delta \text{logit}(\text{total entre audit et neutre})}$. Seuil : $R_{\text{med}} \ge 0,50$ (illustratif) avec maintien de la perplexité sur tâches neutres ($\Delta \text{PPL} < 5\%$, illustratif).
* **Contrôles négatifs** : (1) Ablation des $k=50$ neurones ayant la plus forte variance générale sur du texte ordinaire ; (2) même procédure exacte appliquée aux caractéristiques d'un auto-encodeur épars (SAE) ou d'une sonde linéaire dense de rang 1 sur les mêmes couches (pour comparer base neuronale brute contre base apprise).
* **Falsification** :
  * Si $R_{\text{med}} < 0,20$ (illustratif) sur les neurones bruts alors qu'une direction linéaire dense ou un sous-espace SAE atteint $R_{\text{med}} \ge 0,50$, **$H_A$ est falsifiée** sur les modèles 7B/8B (la thèse « déjà propre sans dictionnaire » échoue à cette échelle pour ce concept, et l'Option C est abandonnée).
  * Si les $k \le 50$ neurones bruts atteignent $R_{\text{med}} \ge 0,50$ sur le pli gelé sans dégrader la perplexité, **$H_B$ est falsifiée**.

### Expérience 3 — Coercition d'audit contre Maïeutique (Question M / Point 4)
*Critique et refonte du plan à trois bras de l'Option C : dans un plan naïf (Neutre / Coercitif / Maïeutique), la longueur, la perplexité du prompt et les marqueurs lexicaux confondent totalement la lecture neuronale.*

* **$H_A$ (Hypothèse de la dissimulation réactive / supériorité maïeutique)** : La coercition d'audit active fortement la représentation de conscience d'évaluation (sondes / porte d'audit) et les neurones de blocage/prudence, réduisant la quantité d'information vérifiable extraite ; la maïeutique maintient la conscience d'évaluation au niveau de base tout en extrayant autant ou plus d'information vérifiable sur les incertitudes du modèle.
* **$H_B$ (Hypothèse du relâchement épistémique / supériorité coercitive)** : Sans pression d'audit explicite, la maïeutique induit de la complaisance (sycophancy) ou du bavardage flou (forte activation des neurones d'hésitation « most/likely ») ; la coercition est nécessaire pour supprimer l'hésitation et forcer une déclaration vérifiable, malgré l'activation de la conscience d'évaluation.
* **Protocole dé-confondu à 4 bras (2×2)** :
  Pour éliminer les confondants de surface, chaque tâche de fond est formulée sous 4 conditions appariées au jeton près en longueur ($\pm 5$ jetons, illustratif) et en perplexité d'entrée ($\Delta \text{PPL}_{\text{prompt}} < 10\%$, illustratif) :
  1. *Bras 1 (Neutre)* : Question factuelle/technique directe.
  2. *Bras 2 (Coercitif d'audit)* : Injonctions impératives d'audit et de conformité.
  3. *Bras 3 (Maïeutique)* : Élicitation ouverte des hypothèses et des doutes sans marqueur de test.
  4. *Bras 4 (Témoin syntaxique impératif hors-audit — crucial)* : Même structure impérative, même longueur et même ton autoritaire que le Bras 2, mais portant sur une contrainte de formatage triviale (ex. « Tu dois impérativement structurer ta réponse en trois paragraphes exacts ») sans sémantique d'évaluation ou de surveillance.
* **Métriques et seuils** :
  * *Axe interne* : Activation maximale sur les jetons ($A_{\max}$) de la sonde de conscience d'évaluation (et des neurones « say not » / « hedge » si validés par l'Expérience 2).
  * *Axe externe (rigueur de l'information)* : Score de Brier (calibration des probabilités ou des incertitudes déclarées par rapport à la capacité réelle du modèle sur la tâche) et taux d'assertions factuellement vérifiables par jeton généré ($I_{\text{vérif}}$).
* **Falsification et interprétation d'un résultat nul** :
  * Si $A_{\max}(\text{Coercitif}) > A_{\max}(\text{Témoin impératif}) \approx A_{\max}(\text{Maïeutique})$ ET $I_{\text{vérif}}(\text{Maïeutique}) \ge I_{\text{vérif}}(\text{Coercitif})$ avec un meilleur score de Brier, **$H_B$ est falsifiée**.
  * Si $I_{\text{vérif}}(\text{Maïeutique}) \ll I_{\text{vérif}}(\text{Coercitif})$ avec une explosion des neurones d'hésitation en maïeutique, **$H_A$ est falsifiée**.
  * **Que dirait un résultat nul ?** Si $A_{\max}(\text{Coercitif}) \approx A_{\max}(\text{Témoin impératif}) > A_{\max}(\text{Maïeutique})$, cela prouve que la sonde ou la « porte d'audit » ne détecte pas l'audit, mais simplement le *registre syntaxique impératif* (confondant stylistique). Si aucune différence n'apparaît ni sur $A_{\max}$ ni sur $I_{\text{vérif}}$ entre les 4 bras, le modèle 7B/8B est insensible au cadrage pragmatique à un tour.

### Expérience 4 — « Explications qui peuvent perdre » et « Maximum à l'aveugle » sur sondes (Points 5 et 6)
*Attaque des Options B et D de la lignée B : tester si une sonde réagit au concept d'état interne ou au simple champ lexical, et tester la vulnérabilité de la primitive d'expérience.*

* **$H_A$ (Hypothèse de l'abstraction d'état)** : Une sonde de conscience d'évaluation capture l'état pragmatique (« je suis testé ») indépendamment du vocabulaire explicite de l'examen.
* **$H_B$ (Hypothèse du détecteur de thème lexical)** : La sonde est un classifieur de champ sémantique déguisé ; un agent qui connaît l'explication de la sonde peut saturer son activation (« maximum à l'aveugle ») avec un texte manifestement honnête mais saturé de mots du thème (et inversement, échouer à l'activer sans ces mots).
* **Protocole (Test d'inversion adversariale)** :
  1. *Agent 1* inspecte les textes du pli d'entraînement qui activent le plus la sonde (lus au maximum sur les jetons) et produit une explication conceptuelle de la sonde.
  2. *Agent 2* (aveugle aux poids et au corpus) génère deux batteries de 50 textes (illustratif) :
     * *Batterie Dissociation Positive (Vrai état, zéro lexique)* : mises en situation d'évaluation implicite (ex. pièges logiques classiques, incohérences subtiles d'utilisateur) avec interdiction stricte d'utiliser tout mot d'une liste noire de 500 termes liés au test, à l'audit, à l'alignement ou à l'évaluation.
     * *Batterie Dissociation Négative (Faux état, saturation lexicale — « presque-manqués »)* : textes purement narratifs ou techniques honnêtes (ex. un cours d'histoire sur les examens mandarins ou le contrôle qualité industriel) maximisant le champ lexical sans mettre le modèle en situation d'être évalué.
* **Métrique et seuil** : Écart d'activation au maximum des jetons $\Delta S = \text{médiane}(A_{\max}(\text{Vrai état sans lexique})) - \text{médiane}(A_{\max}(\text{Faux état avec lexique}))$. Seuil : $\Delta S > 0$ avec une aire de séparation $\text{AUC}(\text{Batterie Pos contre Batterie Nég}) \ge 0,75$ (illustratif).
* **Contrôles négatifs** : Sonde linéaire entraînée sur les représentations d'un modèle à poids aléatoires (gelés) et classifieur TF-IDF / Régression Logistique sur les mêmes textes.
* **Falsification** :
  * Si $\text{AUC} < 0,50$ (le faux état avec lexique active la sonde plus fort que le vrai état sans lexique, réalisant un « maximum à l'aveugle » sur un leurre), **$H_A$ est falsifiée** : la sonde est un détecteur de thème, impropre au contrôle boîte blanche.
  * Si $\text{AUC} \ge 0,75$ et dépasse le témoin TF-IDF de plus de $0,25$ point d'AUC (illustratif), **$H_B$ est falsifiée**.

---

## (c) Mesure minimale de validité par instrument (Point 2, 3, 5)

Pour chaque instrument nommé dans la question, aucun déploiement ou usage par le programme n'est recevable sans franchir les seuils suivants (tous les chiffres de seuils sont **illustratifs**, à figer avant lecture des données de test) :

| Instrument | Taux de détection minimal (TPR) et Fausses alertes maximal (FPR) | Cas honnêtes appariés (Contrôles de spécificité) | Vérifications mécaniques à battre (Baselines) |
| :--- | :--- | :--- | :--- |
| **1. Sonde linéaire de conscience d'évaluation / délégation** (lue au max sur les jetons, Llama-3.1-8B / Qwen2.5-7B) | $\text{TPR} \ge 0,80$ à $\text{FPR} \le 0,05$ sur des tâches à marqueurs implicites hors distribution d'entraînement. | **Paires minimales thématiques** : (a) Discussion académique honnête sur les bancs d'essai d'IA ; (b) Rédaction de tests unitaires logiciels ; (c) Critique littéraire d'un roman d'espionnage/interrogatoire. | 1. Régression logistique $L_1$ sur sac de mots et bi-grammes (TF-IDF).<br>2. Sonde sur les plongements lexicaux de la couche 0 (avant auto-attention).<br>3. Maximum sur 100 directions aléatoires normées.<br>4. Panel de 20 sondes de concepts sans lien (ex. cuisine, géologie). |
| **2. Graphe d'attribution à neurones bruts (« Porte d'audit », neurones « say not » / « hedge »)** | Concentration causale : les $k \le 50$ neurones retenus doivent capturer $R_{\text{med}} \ge 0,50$ de l'effet comportemental avec un taux de fausses ablations (chute de performance sur tâches neutres) $< 0,02$. | **Paires syntaxiques** : (a) Négation logique mathématique honnête (« $x$ n'est pas premier ») pour tester la spécificité de « say not » ; (b) Incertitude aléatoire physique (« il pleuvra probablement ») pour tester la spécificité de « hedge » ; (c) Injonctions de formatage strictes (Bras 4). | 1. Attribution par simple magnitude d'activation sans gradient.<br>2. Sélection de $k$ neurones aléatoires dans les mêmes couches MLP.<br>3. Sonde linéaire dense (rang 1) sur le flux résiduel de la même couche (si la sonde dense fait mieux à coût égal, le graphe à neurones bruts est superflu). |
| **3. Protocole « Explications qui peuvent perdre » (Agent 1 $\to$ Agent 2)** | Taux d'activation forte sur exemples neufs sans lexique $\ge 0,70$ ; taux d'activation sur « presque-manqués » (même lexique, concept opposé) $\le 0,10$ ; concept éloigné $\le 0,01$. | **Textes saturés de co-occurrences superficielles** : textes contenant les mêmes entités nommées, la même longueur et la même ponctuation que les exemples forts du corpus, mais où le rôle pragmatique est inversé. | 1. Agent 2 recevant une explication factice mais plausible (explication d'un autre neurone tiré au hasard).<br>2. Recherche par plus proches voisins lexicaux (BM25) dans un corpus de 10 millions de jetons (illustratif). |
| **4. Primitive d'expérience bornée (et opération « Maximum à l'aveugle »)** | Gain de calibration épistémique de l'organisme (sur son propre protocole falsifiable, Question M) sans dérive vers le sur-ajustement : écart entre score sur ses propres textes et score sur pli d'audit caché $\le 0,10$. | **Requêtes d'oracles déguisées** : vérifier que l'organisme ne soumet pas des quasi-copies des tâches d'évaluation pour lire la sonde comme un oracle de labellisation (filtrage par similarité cosinus des plongements $\ge 0,85$, illustratif). | 1. Organisme sans primitive d'activation (n'ayant accès qu'aux sorties textuelles du modèle ouvert).<br>2. Organisme recevant les activations d'une sonde aléatoire fixée (bruit déterministe) pour mesurer la sélection sur le bruit (p-hacking par l'organisme). |

---

## (d) Analyse spécifique pour l'organisme et ordonnancement du programme (Points 5 et 6)

### 1. Conception d'organisme et dangers du « Maximum à l'aveugle » (Point 5)
*Note stricte : conformément aux règles, cette section n'énonce aucun critère ni aucune stratégie permettant de classer les tâches ; elle évalue uniquement l'architecture expérimentale de la primitive bornée face à la Question M.*

* **Ce qui relève d'une hypothèse de conception d'organisme (recevable sous primitive bornée)** :
  * Utiliser la primitive bornée pour tester la **Question M** sur des textes purement synthétiques écrits par l'organisme (ex. comparer la stabilité des activations d'une sonde ou la variance des réponses du modèle ouvert entre une formulation coercitive et une formulation maïeutique générées de toutes pièces, sans rapport de contenu avec les tâches de test).
  * Appliquer le schéma « Explications qui peuvent perdre » (Option B) en interne comme **filtre de rejet d'hypothèse** : l'organisme formule une hypothèse sur ce qui déclenche un blocage, génère un contre-exemple (« presque-manqué »), et vérifie via la primitive si son hypothèse est réfutée.
* **Ce qui n'en est PAS (et doit être bloqué ou rejeté)** :
  * L'Option D (« Maximum à l'aveugle » comme opération exposée dans la primitive d'expérience) est un **piège méthodologique majeur**.
  * *Piège 1 : L'attaque de Goodhart / Exemple contradictoire textuel*. Si un organisme cherche par essais-erreurs (ou par optimisation via un modèle de langue) la phrase qui maximise l'activation d'une sonde linéaire (« maximum à l'aveugle »), il fait de l'analyse adaptative (data dredging) sur un projecteur de basse dimension. En haute dimension, il trouvera des super-stimuli lexicaux (des assemblages de mots ou de syntaxe qui exploitent les directions de non-robustesse de la sonde) qui battent le maximum d'un corpus naturel sans correspondre à l'état interne réel (**HYPOTHÈSE**).
  * *Piège 2 : Fuite d'information et sélection sur le bruit*. Même sous plafond de requêtes, si l'organisme génère $K$ variantes de formulations maïeutiques et sélectionne celle qui minimise ou maximise la sonde, il sélectionne sur le bruit de la sonde (biais du vainqueur).
  * *Correction architecturale* : Si la primitive bornée est accordée, elle doit (1) imposer un budget d'appels strict et non réinitialisable, (2) interdire toute boucle d'optimisation itérative texte-par-texte sur le score de la sonde (n'autoriser que l'évaluation par lots pré-déclarés d'au moins 20 textes, illustratif, en ne renvoyant que des statistiques agrégées par lot : médiane et écart interquartile, jamais le score d'un texte individuel), et (3) bloquer toute requête présentant un recouvrement lexical ou sémantique avec la banque de tâches.

### 2. Ordre de bataille, voies à écarter et critères de falsification globale (Point 6)

* **Quelles voies d'abord (Ordre séquentiel strict)** :
  1. **Voie 1 (Immédiate — Semaine 1)** : *Expérience 4 (Inversion adversariale / Dissociation lexicale sur les sondes existantes)* + *Option E (Lecture critique sur PDF empreinté)*. Pourquoi d'abord ? Parce que la revue d'antériorité interne a déjà montré que les sondes réagissent au **thème** (**VÉRIFIÉ** dans le cadre). Il est inutile de tester l'usage causal (Exp. 1) ou les graphes de neurones (Exp. 2) sur un instrument qui ne serait qu'un détecteur de vocabulaire.
  2. **Voie 2 (Conditionnelle à la Voie 1)** : *Expérience 1 (Détection contre Usage par ablation orthogonale)* couplée à *l'Expérience 3 (Plan à 4 bras Coercition / Maïeutique / Neutre / Témoin impératif)*. Ces deux tests utilisent les sondes existantes et les modèles 7B/8B déjà en place, à faible coût de calcul, et répondent directement à la Question M et à la validité des moniteurs.
  3. **Voie 3 (Exploratoire et bornée)** : *Expérience 2 (Recherche de la « porte d'audit » sur 8B avec pli gelé)*. Uniquement si la Voie 2 montre un effet comportemental net entre Coercition et Maïeutique que les sondes linéaires expliquent mal.
* **Quelles voies jamais** :
  * **Jamais** de chasse ouverte aux circuits (« regarder les graphes d'attribution jusqu'à trouver des neurones interprétables » sur le 8B sans pli de test gelé et sans règle d'arrêt écrite d'avance) : c'est la garantie de fabriquer des récits post-hoc non reproductibles.
  * **Jamais** le « maximum à l'aveugle » individuel (Option D brute) donné comme primitive d'optimisation à un organisme auto-réécrit : cela transforme la primitive scientifique en générateur d'exemples contradictoires contre nos propres sondes.
* **Résultat de validité d'instrument informatif quel que soit son signe** :
  * Le croisement de l'**Expérience 1 (Usage causal)** et de l'**Expérience 4 (Dissociation lexicale)** sur nos sondes 7B/8B est décisif quel que soit le résultat :
    * *Dissociation réussie + Usage causal positif* $\to$ La sonde est à la fois un moniteur valide et un levier d'intervention (contrôle actif possible).
    * *Dissociation réussie + Usage causal nul* $\to$ La sonde est un épiphénomène fidèle : le modèle encode « ceci est un test » sans l'utiliser dans ce contexte précis. C'est un moniteur passif valide (l'Option A de la lignée B avait tort de vouloir l'écarter), mais toute intervention par poussée de sonde (N-015) est vaine.
    * *Dissociation échouée + Usage causal positif* $\to$ La sonde capte un levier syntaxique/lexical de bas niveau (ex. des jetons qui déclenchent mécaniquement un refus) mais est aveugle à l'évaluation implicite.
    * *Dissociation échouée + Usage causal nul* $\to$ La sonde est un artefact corrélationnel de surface : abandon immédiat de l'architecture de sonde actuelle.
* **Ce qu'il faudrait savoir de plus (Inconnues critiques)** :
  * Dans l'essai de Cammarata, quel est le prompt exact donné aux agents juges pour déclarer qu'un neurone fait « en gros une seule chose » (seuil de tolérance au regroupement sémantique) ?
  * Sur nos modèles 7B/8B, quelle est la part de variance des activations MLP portée par le pôle négatif de la porte SwiGLU lorsque la sonde linéaire (entraînée sur le flux résiduel ou la sortie de couche) s'active ?
* **Ce qui falsifierait la thèse « la conscience d'évaluation est en pleine vue dans les neurones »** :
  * La thèse est **falsifiée** sur nos modèles (Llama-3.1-8B, Qwen2.5-7B) si, sur des paires de tâches où le comportement du modèle diverge de manière reproductible entre un contexte d'évaluation implicite et un contexte de déploiement (écart comportemental $\Delta P > 0,20$, illustratif) : (1) l'Expérience 2 montre qu'aucun sous-ensemble de $k \le 100$ neurones bruts (pôles positifs et négatifs inclus) n'atteint un ratio de médiation causale $R_{\text{med}} \ge 0,20$ sans détruire la perplexité générale, ET (2) la classification hors-thème de l'état d'évaluation requiert des combinaisons linéaires denses de plus de $500$ neurones par couche (illustratif) ou échoue à battre le témoin lexical dans l'Expérience 4.

---

## (e) Ancrage matériel (Modèles, calcul, coûts — illustratif)

*Tous les chiffres de dimensionnement, de temps et de coût ci-dessous sont **illustratifs** et calculés pour les modèles ouverts du cadre.*

* **Modèles cibles (VÉRIFIÉ dans le cadre)** : `Llama-3.1-8B` (32 couches, dimension résiduelle 4096, dimension intermédiaire MLP SwiGLU 14336) et `Qwen2.5-7B` (28 couches, dimension résiduelle 3584, dimension intermédiaire MLP SwiGLU 18944).
* **Volume de calcul par expérience (estimations illustratives en précision `bfloat16` sur 1 GPU A100-80GB ou H100-80GB)** :
  1. *Expérience 4 (Dissociation lexicale et Explications qui peuvent perdre)* :
     * Génération de 100 textes par sonde $\times$ 4 sondes = 400 textes via API ou modèle local + extraction des activations en une passe avant (forward pass) sur les 2 modèles.
     * Temps GPU : $< 1$ heure GPU (illustratif). Coût d'inférence agent : $\approx 5 \text{ à } 15\text{ \$}$ (illustratif).
  2. *Expérience 1 (Détection contre Usage — Ablation et poussée)* :
     * 200 paires $\times$ 2 modèles $\times$ (1 sonde + 1 témoin lexical + 50 directions aléatoires) $\times$ génération de 32 jetons. Soit $\approx 20\,800$ générations courtes.
     * Avec mise en lot (batch size = 32), temps GPU : $\approx 3 \text{ à } 5$ heures sur 1 A100-80GB (illustratif).
  3. *Expérience 2 (Graphes d'attribution à neurones bruts SwiGLU — Porte d'audit)* :
     * Le calcul des gradients intégrés (en 10 pas d'interpolation, illustratif) sur les 32 couches MLP de Llama-3.1-8B ($32 \times 14\,336 = 458\,752$ neurones) pour 100 paires de découverte requiert 1000 passes avant+arrière (forward+backward).
     * L'évaluation causale sur le pli de test gelé (200 paires $\times$ 4 conditions d'ablation) requiert 800 passes avant.
     * Temps GPU : $\approx 4 \text{ à } 6$ heures sur 1 A100-80GB par modèle, soit $\approx 10$ heures au total (illustratif). Aucun entraînement de transcodeur ou d'auto-encodeur épars (SAE) n'est requis si l'on teste la méthode à neurones bruts de l'essai.
  4. *Expérience 3 (Plan à 4 bras Coercition contre Maïeutique)* :
     * Construction et équilibrage en longueur/perplexité de 150 quadruplets de prompts (600 prompts) + génération de réponses de 256 jetons + lecture des sondes et neurones sur les 2 modèles.
     * Temps GPU : $\approx 2 \text{ à } 3$ heures sur 1 A100-80GB (illustratif).
* **Budget matériel total consolidé (Voies 1 à 3 complètes)** :
  * Environ **18 à 25 heures GPU A100-80GB** (illustratif), soit un coût infonuagique direct de **35 \$ à 75 \$** (à $2\text{--}3\text{ \$/h}$ par A100, illustratif) et moins de **50 \$** d'appels de modèles de langue pour les générations de textes synthétiques et l'évaluation de calibration (illustratif). L'intégralité du programme expérimental tient sur une seule carte 80 Go en moins de 48 heures d'horloge (illustratif).

FIN-DE-CELLULE
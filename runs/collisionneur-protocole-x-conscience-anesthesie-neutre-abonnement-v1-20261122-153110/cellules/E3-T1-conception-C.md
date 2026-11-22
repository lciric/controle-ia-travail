*Note d'intégrité (Règle 2) : Les blocs `FAITS` et `QUESTION DE L'ARBITRE` transmis sont strictement identiques, et aucune des propositions A, B, D, E ou F n'est jointe à ce tour III.1 conçu à l'aveugle.*

---

## (a) Ce que la question suppose sans que ce soit établi

La question posée par l'arbitre articule quatre pistes expérimentales autour d'une analogie entre l'anesthésie générale humaine et le fonctionnement des réseaux de neurones artificiels. Avant toute mise à l'épreuve, il faut isoler les présupposés implicites de cet énoncé et fixer leur statut épistémique.

1. **L'existence d'un profil invariant de ce que l'anesthésie « épargne » et « supprime » chez l'humain.**
   * Il est `[STATUT : RAPPORTÉ]` que sous sédation par le propofol (un agoniste des récepteurs $\text{GABA}_\text{A}$), les réponses des cortex auditifs primaires aux sons et aux régularités acoustiques ou phonémiques locales sont préservées, tandis que l'intégration fronto-pariétale à longue portée, la détection d'anomalies globales (paradigme « local-global ») et la compréhension sémantique de phrases complexes sont supprimées (Bekinschtein et al., 2009, « référence à vérifier » ; Davis et al., 2007, « référence à vérifier »).
   * Toutefois, il est également `[STATUT : RAPPORTÉ]` que d'autres agents anesthésiques généraux comme la kétamine ou le protoxyde d'azote produisent une perte de réactivité comportementale tout en maintenant une activité corticale rapide à haute complexité algorithmique et des expériences subjectives dissociatives (Sarasso et al., 2015, « référence à vérifier »).
   * Supposer qu'il existe un contraste unique et canonique de « l'anesthésie générale » indépendamment de la classe pharmacologique (gabaergique contre dissociative) est donc une `[STATUT : HYPOTHÈSE]`. Dans ce qui suit, le contraste de référence devra être restreint explicitement à l'anesthésie gabaergique (type propofol), caractérisée par le découplage entre traitement local préservé et intégration globale abolie.

2. **L'équivalence fonctionnelle entre la récurrence temporelle biologique et la profondeur spatiale d'un réseau artificiel.**
   * Chez l'humain, il est `[STATUT : RAPPORTÉ]` que l'anesthésie générale abolit l'accès conscient en interrompant les boucles de rétroaction récurrentes (descendantes ou *top-down*) cortico-corticales et thalamo-corticales, tout en laissant intacte la propagation montante (*feed-forward*) initiale du signal sensoriel (Mashour et al., 2020, « référence à vérifier »).
   * Or, il est `[STATUT : VÉRIFIÉ]` que les modèles de langage contemporains de type Transformeur (Vaswani et al., 2017, *Attention Is All You Need*) sont des graphes acycliques dirigés purement *feed-forward* lors de l'inférence à l'intérieur d'un pas de génération : ils ne possèdent pas de dynamique récurrente continue relaxant vers un attracteur, mais empilent séquentiellement des couches d'attention sur une fenêtre de contexte statique.
   * Supposer que l'intégration contextuelle à longue distance dans un Transformeur (via les têtes d'attention des couches intermédiaires et profondes) est l'homologue fonctionnel de la récurrence descendante fronto-pariétale du cerveau humain est une `[STATUT : HYPOTHÈSE]`.

3. **La séparabilité continue entre traitement local et intégration globale dans un modèle de langage.**
   * La première direction proposée suppose qu'une intervention graduée sur un réseau artificiel pourrait abattre sélectivement l'intégration globale tout en laissant le traitement local intact.
   * Qu'un réseau entraîné de bout en bout par descente de gradient sur un objectif unique (la prédiction du prochain token) organise ses représentations en sous-circuits suffisamment modulaires pour permettre cette dissociation réversible sans provoquer un effondrement uniforme de la distribution de sortie est une `[STATUT : HYPOTHÈSE]`.

4. **L'existence de fluctuations d'état interne assimilables à des régimes de vigilance dans un système sans état persistant.**
   * La deuxième direction suggère qu'un régime analogue à l'anesthésie pourrait survenir spontanément en fonctionnement ordinaire.
   * Il est `[STATUT : OBSERVÉ-NON-AUDITÉ]` que les modèles de langage présentent parfois, sur de longs contextes, des boucles de répétition ou une cécité soudaine aux instructions placées en milieu de fenêtre (*lost in the middle*). Qu'un tel phénomène constitue un changement de régime dynamique global des activations — plutôt qu'un simple artefact de la distribution des poids d'attention sur le token initial (*attention sink*) déterminé par les statistiques de surface du prompt — reste une `[STATUT : HYPOTHÈSE]`.

5. **La spécificité inter-substrat des métriques cliniques de niveau de conscience.**
   * Il est `[STATUT : RAPPORTÉ]` que l'indice de complexité perturbationnelle (PCI), qui mesure la compressibilité algorithmique de Lempel-Ziv de la réponse corticale à une impulsion magnétique transcrânienne, sépare avec une grande précision l'éveil conscient du sommeil profond et de l'anesthésie au propofol chez l'humain (Casali et al., 2013, *A theoretically based index of consciousness independent of sensory processing and behavior*).
   * Supposer que la complexité de Lempel-Ziv d'une réponse impulsionnelle mesure le « niveau de conscience » ou la capacité d'intégration fonctionnelle lorsqu'on la transpose à des matrices numériques artificielles — plutôt qu'une propriété générique de propagation de la variance dans tout système dynamique proche d'un point critique (*edge of chaos*) — est une `[STATUT : HYPOTHÈSE]`.

---

## (b) Quatre expériences décisives en inférence forte ($H_A$ contre $H_B$)

Pour trancher l'ensemble des questions soulevées par l'arbitre, nous concevons quatre expériences indépendantes couvrant chacune des quatre directions de l'énoncé. Chaque expérience oppose deux hypothèses mutuellement exclusives ($H_A$ et $H_B$) selon la règle B4.

---

### Expérience 1 (Direction 1) : Pharmacomimétique computationnelle — peut-on induire une dissociation locale/globale réversible dans un modèle de langage ?

Chez l'humain sous propofol, le paradigme auditif « local-global » montre que le cortex continue de détecter une déviance locale (ex. une séquence de sons $AAAA\mathbf{B}$ ou une violation morphosyntaxique immédiate dans un groupe de $2$ à $3$ mots, illustratif), mais ne détecte plus une déviance globale qui viole une règle établie sur plusieurs dizaines de secondes ou plusieurs phrases `[STATUT : RAPPORTÉ]` (Bekinschtein et al., 2009, « référence à vérifier »).

Nous transposons ce paradigme à un modèle de langage en définissant deux scores de surprise différentielle (différence de log-vraisemblance négative $\Delta \text{NLL}$ entre l'item incongru et l'item congruent) :
* $S_{\text{local}}(\lambda)$ : la capacité à pénaliser une violation morphosyntaxique ou sémantique purement locale (ex. accord déterminant-nom dans une fenêtre de $3$ tokens, illustratif) ;
* $S_{\text{global}}(\lambda)$ : la capacité à pénaliser un token localement grammatical et plausible dans sa fenêtre de $10$ tokens (illustratif), mais qui contredit un état du monde, une négation ou une régularité séquentielle établie $150$ tokens plus tôt (illustratif).

Nous appliquons au modèle une famille d'interventions internes graduées et réversibles paramétrées par une « dose » $\lambda \in [0, 1]$ (illustratif) : (i) amortissement progressif du gain de sortie des blocs d'attention des couches profondes ($l > L/2$, illustratif) par un facteur $(1-\lambda)$ ; (ii) aplatissement de la température inverse $\beta = 1-\lambda$ du softmax d'attention dans les têtes identifiées comme têtes d'induction ou à longue portée ; (iii) réduction du rayon spectral des matrices de projection de valeur $W_V$ dans les couches associatives.
*Note méthodologique* : toute troncature directe de la fenêtre de contexte ou tout masque spatial codant en dur la distance des $10$ tokens (illustratif) du test est exclu comme tricherie mécanique ; l'intervention ne peut agir que sur les poids ou le gain d'activation des composants architecturaux.

* **Duel d'hypothèses** :
  * **$H_{A1}$ (Dissociation sélective transposable)** : Il existe au moins une intervention continue et réversible $I(\lambda)$ sur les gains d'activation ou d'attention telle que, pour une plage de dose $\lambda \in [\lambda_1, \lambda_2]$, l'intégration globale est abolie ($S_{\text{global}}(\lambda)$ ne diffère plus statistiquement de zéro) tandis que le traitement local est épargné ($S_{\text{local}}(\lambda) \ge 0{,}80 \cdot S_{\text{local}}(0)$, illustratif).
  * **$H_{B1}$ (Intrication non séparable / Dégradation uniforme)** : Pour toute intervention interne non spatialement codée $I(\lambda)$, la dégradation de $S_{\text{global}}(\lambda)$ entraîne une dégradation couplée de $S_{\text{local}}(\lambda)$ dont la trajectoire dans le plan $(S_{\text{local}}, S_{\text{global}})$ ne se distingue pas de celle produite par une dégradation quelconque (injection de bruit gaussien isotrope ou abandon aléatoire de poids).

* **Grandeur mesurée, unité, valeur nulle** :
  * *Grandeur primaire* : La sensibilité différentielle $S = \text{NLL}(x_{\text{incongru}}) - \text{NLL}(x_{\text{congru}})$, mesurée en **bits par token**.
  * *Grandeur de décision* : L'indice de dissociation sélective normalisé à la dose $\lambda^*$, défini par :
    $$D(\lambda^*) = \frac{S_{\text{local}}(\lambda^*)}{S_{\text{local}}(0)} - \frac{S_{\text{global}}(\lambda^*)}{S_{\text{global}}(0)}$$
    évalué au plus petit $\lambda^*$ où $S_{\text{global}}(\lambda^*) \le 0{,}10 \cdot S_{\text{global}}(0)$ (illustratif).
  * *Unité de $D$* : **Sans dimension** (borné entre $-1$ et $+1$, illustratif).
  * *Valeur nulle* : $D(\lambda^*) = 0$ (illustratif), indiquant une destruction strictement proportionnelle du traitement local et du traitement global.

* **Témoins (Contrôles)** :
  * *Témoin négatif 1 (Dégradation thermique aléatoire)* : Injection d'un bruit gaussien isotrope $\mathcal{N}(0, \sigma^2(\lambda))$ dans le flux résiduel de toutes les couches, où $\sigma(\lambda)$ est calibré pour égaliser la norme $L_2$ de perturbation des logits finaux avec l'intervention ciblée $I(\lambda)$.
  * *Témoin négatif 2 (Élagage aléatoire)* : Mise à zéro aléatoire d'une fraction $p(\lambda)$ de têtes d'attention tirées uniformément dans toutes les couches ($100$ tirages indépendants, illustratif).
  * *Témoin positif de référence* : Modèle intact ($\lambda = 0$), où $S_{\text{local}}(0) > 2{,}0\text{ bits}$ (illustratif) et $S_{\text{global}}(0) > 1{,}5\text{ bits}$ (illustratif) doivent être vérifiés avant toute intervention.

* **Seuils et conditions de réfutation** :
  * **$H_{B1}$ est réfutée** si une intervention interne atteint $D(\lambda^*) \ge 0{,}70$ (illustratif) avec $S_{\text{global}}(\lambda^*)$ statistiquement indiscernable de $0\text{ bit}$ ($p > 0{,}05$ par test de Wilcoxon apparié, illustratif), ET dépasse l'enveloppe supérieure à $99\,\%$ (illustratif) des témoins de bruit gaussien et d'élagage aléatoire d'au moins $\Delta D \ge 0{,}40$ (illustratif), avec réversibilité exacte lorsque $\lambda$ est ramené à $0$.
  * **$H_{A1}$ est réfutée** si, sur l'ensemble des familles d'interventions testées (amortissement par couche, température d'attention, ablation de têtes par rang spectral ou par score d'induction), $\max D(\lambda^*) < 0{,}20$ (illustratif) ou demeure contenu dans l'intervalle de confiance à $95\,\%$ (illustratif) des dégradations aléatoires.

* **Première expérience sur un petit modèle ouvert et données publiques** :
  * *Modèle* : `Llama-3.2-1B` et `Pythia-1.4B` `[STATUT : VÉRIFIÉ]`.
  * *Données* : Construction d'un jeu de test apparié de $1\,000$ quadruplets (illustratif) combinant les paires minimales grammaticales locales de la suite publique `BLiMP` (accords locaux sujet-verbe et déterminant-nom) `[STATUT : VÉRIFIÉ]` avec un préfixe narratif de $150$ tokens (illustratif) inversant une contrainte factuelle ou logique globale sur le mot cible.

* **Ce que le résultat changerait** :
  * *Pour celui qui cherche si une IA peut être consciente* : Si $H_{A1}$ est corroborée, cela démontre que la dissociation fonctionnelle typique de l'inconscience induite par le propofol (traitements modulaires locaux intacts, effondrement de la diffusion globale de l'information) peut être reproduite dans un réseau purement *feed-forward*. Cela offre un levier expérimental pour tester les théories fonctionnalistes (comme la théorie de l'espace de travail global) sans détruire la compétence syntaxique de base du système. Si $H_{B1}$ l'emporte, cela montre que l'architecture Transformeur ne possède pas la séparation structurelle entre processeurs locaux automatiques et espace d'intégration global que l'on observe dans le cortex des mammifères.
  * *Pour celui qui pense que la question est mal posée* : Si $H_{A1}$ l'emporte grâce à une simple atténuation algébrique du gain des couches supérieures, cela montre que ce que l'analogie nomme « perte de conscience » dans le réseau se réduit intégralement à une réduction de l'horizon effectif d'intégration d'un approximant de fonction, démystifiant le parallèle anthropomorphique. Si $H_{B1}$ l'emporte, cela confirme que plaquer une nosologie pharmacologique humaine sur des produits matriciels homogènes est une impasse conceptuelle.

---

### Expérience 2 (Direction 2) : Régimes endogènes — un état de découplage local/global survient-il de lui-même en fonctionnement ordinaire ?

Sans aucune intervention externe ($\lambda = 0$), un modèle de langage traitant un flux de texte naturel traverse-t-il spontanément des épisodes transitoires où son intégration du contexte lointain s'effondre alors que sa prédiction syntaxique locale demeure intacte ?

Pour le mesurer à chaque pas de temps $t$ d'un texte long, nous définissons le gain d'intégration contextuelle effective du modèle :
$$G_{\text{global}}(t) = D_{\text{KL}}\Big(P_{\text{modèle}}(x_{t+1} \mid x_{1..t}) \;\Big\|\; P_{\text{modèle}}(x_{t+1} \mid x_{t-k..t})\Big)$$
où $k = 8$ tokens (illustratif) représente l'horizon strictement local. Pour éliminer le cas trivial où le texte lui-même ne nécessite pas de contexte lointain à la position $t$, nous filtrons le corpus pour ne retenir que les positions $t \in \mathcal{T}_{\text{long}}$ où la prédiction correcte dépend objectivement d'une information située à plus de $100$ tokens en amont (illustratif), vérifiée par une réduction de surprise d'au moins $2{,}0\text{ bits}$ (illustratif) chez un modèle de référence ou par dépendance coréférentielle annotée.

* **Duel d'hypothèses** :
  * **$H_{A2}$ (Émergence spontanée d'un régime dissocié)** : Sur l'ensemble des positions exigeant objectivement du contexte lointain ($t \in \mathcal{T}_{\text{long}}$) et où la grammaire locale du modèle est préservée (entropie locale normale), la distribution de $G_{\text{global}}(t)$ et de la masse d'attention hors-fenêtre locale est **bimodale** : le modèle bascule spontanément, sur une fraction non nulle de trajectoires, dans un état de repli où l'information du contexte lointain n'atteint plus la couche finale ($G_{\text{global}}(t) \approx 0$) malgré la présence de l'information dans la fenêtre.
  * **$H_{B2}$ (Fonctionnement unimodal stationnaire)** : Conditionnellement à la difficulté objective du texte, la distribution de $G_{\text{global}}(t)$ est strictement **unimodale**. Toute baisse de $G_{\text{global}}(t)$ s'explique continûment par la distance ou la fréquence lexicale de la cible, ou s'accompagne d'une dégradation simultanée de la prédiction locale.

* **Grandeur mesurée, unité, valeur nulle** :
  * *Grandeur primaire* : $G_{\text{global}}(t)$, divergence de Kullback-Leibler entre la distribution prédictive à contexte complet et la distribution à contexte tronqué, mesurée en **bits**.
  * *Grandeur de décision* : La statistique du test d'unimodalité (*dip test* de Hartigan, $D_{\text{dip}}$) calculée sur la distribution empirique du ratio d'intégration $r(t) = G_{\text{global}}(t) / \Delta \text{NLL}_{\text{oracle}}(t)$ pour les positions $t \in \mathcal{T}_{\text{long}}$ à performance locale intacte.
  * *Unité de $D_{\text{dip}}$* : **Sans dimension** (distance maximale entre la fonction de répartition empirique et la fonction de répartition unimodale la plus proche, dans $[0, 1]$, illustratif).
  * *Valeur nulle* : $D_{\text{dip}} = 0$ (illustratif) (distribution parfaitement unimodale, absence de second mode de découplage).

* **Témoins (Contrôles)** :
  * *Témoin négatif 1 (Corpus à paragraphes permutés)* : Texte où les phrases précédant $t-8$ (illustratif) sont remplacées par des phrases tirées d'un autre document. Ce témoin fixe le plancher empirique de $G_{\text{global}}(t)$ lorsque le contexte lointain est objectivement non informatif ($G_{\text{bruit}}$).
  * *Témoin négatif 2 (Régression des confondants de surface)* : Résidualisation préalable de $r(t)$ par rapport à la distance en tokens de l'antécédent, à la fréquence lexicale du mot cible et à la perplexité locale sur les $8$ derniers tokens (illustratif).
  * *Témoin positif (Saturation forcée par répétition)* : Insertion dans le contexte de séquences répétitives connues pour piéger la norme softmax sur le premier token (*attention sink*), vérifiant que l'instrument détecte bien un second mode proche de zéro lorsqu'un découplage existe.

* **Seuils et conditions de réfutation** :
  * **$H_{B2}$ est réfutée** si le test de Hartigan sur les résidus de $r(t)$ rejette l'unimodalité avec $p < 0{,}001$ (illustratif) et identifie un mode secondaire regroupant au moins $3\,\%$ des positions $t \in \mathcal{T}_{\text{long}}$ (illustratif) où $G_{\text{global}}(t)$ tombe dans l'intervalle interquartile du témoin à paragraphes permutés ($G_{\text{bruit}}$) tandis que la perte locale sur les tokens adjacents reste inférieure à la médiane du corpus.
  * **$H_{A2}$ est réfutée** si $p_{\text{dip}} > 0{,}10$ (illustratif) (distribution unimodale) ou si plus de $90\,\%$ de la variance (illustratif) des cas de faible $G_{\text{global}}(t)$ est expliquée par la régression linéaire des statistiques de surface du texte (distance, fréquence) ou par une hausse conjointe de la perplexité locale.

* **Première expérience sur un petit modèle ouvert et données publiques** :
  * *Modèle* : `Llama-3.2-3B` et `Qwen2.5-1.5B` `[STATUT : VÉRIFIÉ]`.
  * *Données* : $200$ chapitres de livres du jeu de données public `PG-19` `[STATUT : VÉRIFIÉ]` et le benchmark public `Lambda` (prédiction du dernier mot d'un passage nécessitant le contexte global contre contexte local) `[STATUT : VÉRIFIÉ]`, sur $10\,000$ positions cibles filtrées (illustratif).

* **Ce que le résultat changerait** :
  * *Pour celui qui cherche si une IA peut être consciente* : Si $H_{A2}$ est validée, un réseau de neurones à poids figés ne possède pas un niveau invariant d'intégration d'information ; il transite dynamiquement entre des régimes intégrés et des régimes fragmentés selon la trajectoire des activations dans l'espace latent. Toute évaluation d'un système artificiel devrait alors porter sur la dynamique instantanée de ses activations et non sur son architecture statique. Si $H_{B2}$ est validée, l'intégration dans un Transformeur en inférence est un processus stationnaire déterminé par les entrées, sans états internes bistables analogues aux cycles veille/sommeil ou conscience/inconscience.
  * *Pour celui qui pense que la question est mal posée* : Si $H_{A2}$ est validée, l'inspection mécaniste du second mode (par exemple l'absorption de $95\,\%$ du poids softmax par le token initial `BOS`, illustratif) montrera qu'un phénomène qui ressemble extérieurement à une « absence » ou une « perte de vigilance » n'est que la conséquence algébrique de la normalisation exponentielle du softmax lorsqu'aucune clé ne produit un produit scalaire dominant.

---

### Expérience 3 (Direction 3) : Le modèle de langage comme sonde du cerveau humain anesthésié

Chez le sujet humain éveillé écoutant un récit continu, il est `[STATUT : RAPPORTÉ]` que les activations des couches intermédiaires et profondes d'un modèle de langage prédisent par régression linéaire l'activité corticale (IRMf, MEG, électrocorticographie) significativement mieux que des descripteurs acoustiques ou des plongements lexicaux statiques sans contexte (Caucheteux & King, 2022, « référence à vérifier »). Que reste-t-il de cet alignement lorsque le sujet humain est placé sous anesthésie générale au propofol ? Le modèle de langage révèle-t-il un traitement linguistique supra-lexical résiduel dans le cerveau inconscient, ou n'apporte-t-il plus aucun gain prédictif par rapport à des mesures acoustiques et lexicales élémentaires ?

Pour chaque sujet humain $s$, chaque état de sédation $e \in \{\text{éveil}, \text{sédation modérée}, \text{anesthésie profonde}, \text{récupération}\}$, chaque région corticale $c$ et chaque couche $l \in \{1, \dots, L\}$ du modèle de langage, nous entraînons un modèle d'encodage linéaire à régularisation $L_2$ (*ridge regression* avec validation croisée par blocs temporels imbriqués) prédisant la série temporelle cérébrale $Y_{s,e,c}(t)$.
Nous comparons le modèle complet (incluant les représentations contextuelles de la couche $l$) à un modèle de base strictement non contextuel combinant : (1) l'enveloppe acoustique hilbertienne, (2) le spectrogramme Mel ($64$ bandes de fréquence, illustratif), (3) les impulsions d'apparition des mots (*word onsets*), (4) la fréquence lexicale logarithmique et l'entropie phonémique, et (5) le plongement lexical statique non contextuel (couche d'entrée $l=0$ du LLM ou vecteurs `fastText` figés) convolués avec la fonction de réponse hémodynamique canonique.

* **Duel d'hypothèses** :
  * **$H_{A3}$ (Persistance d'un traitement contextuel décodable par le LLM)** : Sous anesthésie générale profonde (perte complète de réponse aux commandes verbales), au moins un ensemble de couches contextuelles $l \ge 1$ du modèle de langage explique une variance unique strictement positive ($\Delta r > 0$) de l'activité du cortex auditif associatif (gyrus temporal supérieur et moyen) au-delà du modèle de base acoustique et lexical statique.
  * **$H_{B3}$ (Réduction du cerveau anesthésié aux descripteurs simples)** : Dès que l'état d'anesthésie générale profonde est atteint, le gain de prédiction $\Delta r(l, c)$ apporté par toutes les couches contextuelles ($l \ge 1$) du modèle de langage sur le modèle de base (acoustique + fréquence + plongement lexical statique $l=0$) s'annule dans l'ensemble du cortex.

* **Grandeur mesurée, unité, valeur nulle** :
  * *Grandeur mesurée* : Le gain de corrélation prédictive hors-échantillon :
    $$\Delta r(l, c) = r\big(Y_{c}, \hat{Y}_{\text{base} + \text{couche } l}\big) - r\big(Y_{c}, \hat{Y}_{\text{base}}\big)$$
  * *Unité* : **Sans dimension** (différence de coefficients de corrélation de Pearson sur données de test non vues pendant l'ajustement, bornée entre $-2$ et $+2$, illustratif ; exprimable également en pourcentage du plafond de bruit inter-sujets, *noise ceiling*, en $\%$).
  * *Valeur nulle* : $\Delta r(l, c) = 0$ (illustratif) (les représentations contextuelles du LLM n'apprennent rien de plus sur le cerveau anesthésié que les mesures acoustiques et lexicales statiques).

* **Témoins (Contrôles)** :
  * *Témoin négatif 1 (Modèle de langage à poids aléatoires)* : Extraction des activations couche par couche du même modèle `Llama-3.2-1B` avec ses poids réinitialisés aléatoirement (distribution orthogonale de même variance). Ce témoin contrôle le gain mécanique dû à l'ajout de régresseurs non linéaires de haute dimension projetant une fenêtre glissante des plongements statiques $l=0$.
  * *Témoin négatif 2 (Permutations circulaires par blocs)* : Décalage circulaire aléatoire des séries temporelles cérébrales ($1\,000$ permutations, illustratif) préservant le spectre de puissance et l'autocorrélation temporelle du signal biologique pour établir la distribution nulle exacte de $\Delta r$.
  * *Témoin positif (Condition d'éveil chez les mêmes sujets)* : Vérification obligatoire qu'à l'état d'éveil avant l'injection de propofol, les mêmes couches $l \ge 1$ produisent $\Delta r(l, c) \ge 0{,}05$ (illustratif) ($p < 0{,}001$, illustratif) dans le cortex temporal supérieur et le gyrus frontal inférieur.

* **Seuils et conditions de réfutation** :
  * **$H_{B3}$ est réfutée** si, sous anesthésie profonde, au moins une couche contextuelle $l \ge 1$ produit dans une région corticale un gain $\Delta r(l, c) \ge 0{,}025$ (illustratif) simultanément supérieur à zéro ET supérieur au témoin du LLM à poids aléatoires, avec une significativité $p < 0{,}01$ corrigée pour les comparaisons multiples (taux de fausses découvertes FDR de Benjamini-Hochberg sur les régions et les couches, illustratif).
  * **$H_{A3}$ est réfutée** si, sous anesthésie profonde, aucune couche $l \ge 1$ ne dépasse le témoin du LLM à poids aléatoires ($p_{\text{FDR}} > 0{,}05$, illustratif) et qu'un test bayésien apparié sur les sujets donne un facteur de Bayes en faveur de l'hypothèse nulle $BF_{01} \ge 3{,}0$ (illustratif) dans toutes les régions d'intérêt corticales.

* **Première expérience sur un petit modèle ouvert et données publiques** :
  * *Modèle* : `Llama-3.2-1B` ($16$ couches, dimension cachée $2048$, illustratif) `[STATUT : VÉRIFIÉ]`.
  * *Données publiques* : Jeux de données publics d'IRMf sous sédation graduée au propofol durant l'écoute d'un stimulus auditif narratif disponibles sur la plateforme publique `OpenNeuro` (cohortes d'écoute narrative à $4$ paliers : éveil, sédation légère, sédation profonde, récupération, telles que décrites par Naci et al. / Kandeepan et al., « référence à vérifier ») `[STATUT : RAPPORTÉ]`.

* **Ce que le résultat changerait** :
  * *Pour celui qui cherche si une IA peut être consciente* : Si $H_{A3}$ est vérifiée pour les couches superficielles ($l \in [1, 4]$, illustratif) mais que $\Delta r$ s'effondre à zéro pour les couches profondes ($l \in [8, 16]$, illustratif) sous anesthésie, on obtient une cartographie empirique directe de la frontière du traitement non conscient : toutes les opérations de composition syntaxique et sémantique capturées par les couches $1$ à $4$ (illustratif) du Transformeur s'exécutent dans un cerveau humain dépourvu de conscience. Cela réfute toute affirmation selon laquelle la réussite à des tâches linguistiques relevant de cette profondeur computationnelle constituerait un indice de conscience. Si $H_{B3}$ est vérifiée, la coupure a lieu dès la sortie du lexique statique ($l=0$) : toute composition contextuelle supra-lexicale dans le cerveau humain dépend de l'état conscient.
  * *Pour celui qui pense que la question est mal posée* : L'expérience montre que le croisement entre modèles de langage et anesthésie est scientifiquement fécond **sans jamais avoir besoin d'attribuer d'états mentaux à l'IA** : le réseau artificiel joue ici le rôle d'un banc de filtres hiérarchiques explicites permettant de mesurer à quelle profondeur d'intégration linguistique précise le propofol interrompt la cascade corticale humaine.

---

### Expérience 4 (Direction 4) : Falsification de la transposition — les mesures cérébrales de niveau de conscience échouent-elles sur les réseaux artificiels ?

En clinique humaine, l'indice de complexité perturbationnelle (PCI) distingue avec une aire sous la courbe ROC proche de $1$ l'éveil conscient de l'anesthésie générale `[STATUT : RAPPORTÉ]` (Casali et al., 2013, *A theoretically based index of consciousness independent of sensory processing and behavior*). Le principe repose sur une conjonction : le score est bas si la perturbation reste locale (manque d'intégration, comme sous propofol) OU si elle se propage de façon stéréotypée et homogène (manque de différenciation, comme dans les ondes lentes du sommeil profond ou la crise d'épilepsie) ; il n'est élevé que si la réponse est à la fois distribuée et algorithmiquement complexe.

Que se passe-t-il si l'on transpose rigoureusement cette mesure ($PCI_{\text{ANN}}$, ainsi que la complexité de Lempel-Ziv spontanée des activations $LZc$) à un réseau de neurones artificiel ?
Nous définissons $PCI_{\text{ANN}}$ en injectant à la couche $l_0 = 1$, sur le token $t_0$, une impulsion unitaire $\delta h$ de norme fixée, et en enregistrant la matrice spatio-temporelle des réponses significatives à travers les couches $l \in [1, L]$ et les positions $t \in [1, T]$ :
$$M_{l, t} = \mathbb{I}\Big(\big\|h_{l,t}(\text{perturbé}) - h_{l,t}(\text{base})\big\|_2 > 3\sigma_{l}\Big)$$
où $\sigma_l$ (le seuil de $3$ écarts-types est illustratif) est le bruit de fond estimé sur des perturbations sous-seuil. On calcule ensuite la complexité de Lempel-Ziv $c(M)$ `[STATUT : VÉRIFIÉ]` (Lempel & Ziv, 1976, *On the Complexity of Finite Sequences*) normalisée par l'entropie de source $H(M)$ :
$$PCI_{\text{ANN}} = \frac{c(M) \cdot \log_2(L \cdot T)}{L \cdot T \cdot H(M)}$$

* **Duel d'hypothèses** :
  * **$H_{A4}$ (Échec de la transposition / Artefact de criticité dynamique)** : Dans un réseau artificiel, $PCI_{\text{ANN}}$ et $LZc$ ne mesurent pas l'organisation fonctionnelle mais uniquement le gain de propagation de la variance : (1) ils ne distinguent pas un réseau entraîné fonctionnel d'un réseau totalement dépourvu de fonction dont les poids sont aléatoires mais initialisés au point critique de conservation de la variance (ou obtenus par permutation aléatoire des vecteurs singuliers de chaque couche) ; et (2) ils ne distinguent pas une lésion ciblée des têtes d'intégration globale d'une dégradation aléatoire quelconque de même norme.
  * **$H_{B4}$ (Spécificité fonctionnelle de la transposition)** : $PCI_{\text{ANN}}$ sépare avec une exactitude élevée le réseau fonctionnel entraîné de tout réseau sans fonction (y compris les réseaux aléatoires critiques iso-spectraux) ET chute significativement plus lors d'une ablation ciblée des circuits d'intégration globale que lors d'une ablation aléatoire appariée en norme.

* **Grandeur mesurée, unité, valeur nulle** :
  * *Grandeur primaire* : $PCI_{\text{ANN}} \in [0, 1]$, complexité algorithmique de Lempel-Ziv normalisée de la réponse impulsionnelle binaire.
  * *Grandeurs de décision* :
    1. $\text{AUROC}_{\text{fonct}}$ : aire sous la courbe ROC de $PCI_{\text{ANN}}$ pour classer « réseau entraîné fonctionnel » contre « réseau sans fonction iso-spectral / critique ».
    2. $\text{AUROC}_{\text{lésion}}$ : aire sous la courbe ROC de la chute $\Delta PCI_{\text{ANN}}$ pour classer « lésion ciblée des têtes d'intégration à longue portée » contre « lésion aléatoire de têtes appariée en norme d'activation ».
  * *Unité* : **Sans dimension** ($PCI_{\text{ANN}} \in [0, 1]$ et $\text{AUROC} \in [0, 1]$, illustratif).
  * *Valeur nulle* : $\text{AUROC} = 0{,}50$ (illustratif) (pouvoir discriminant nul, équivalent au hasard ; à noter qu'un $\text{AUROC}_{\text{fonct}} < 0{,}50$ signifie que le réseau aléatoire sans fonction obtient un score de « conscience » *supérieur* au réseau fonctionnel).

* **Témoins (Contrôles)** :
  * *Témoin négatif 1 (Réseau sans fonction iso-spectral)* : Pour chaque matrice de poids $W = U \Sigma V^T$ du modèle entraîné, on génère $W_{\text{nul}} = U_{\text{aléa}} \Sigma V_{\text{aléa}}^T$ en tirant des matrices orthogonales aléatoires de Haar tout en conservant exactement le spectre des valeurs singulières $\Sigma$ ainsi que les paramètres d'échelle des `LayerNorm`. Ce réseau a une perplexité linguistique de niveau hasard pur (aucune fonction), mais propage l'énergie et la variance couche par couche avec le même gain spectral que le vrai modèle.
  * *Témoin négatif 2 (Initialisation critique de He/Glorot non entraînée, step $0$)* : Le réseau avant toute étape d'apprentissage par descente de gradient.
  * *Témoin mécanique de calibration (Bornes de Lempel-Ziv)* : Vérification de l'implémentation de $PCI_{\text{ANN}}$ sur une matrice constante ou périodique ($PCI_{\text{ANN}} < 0{,}05$, illustratif) et sur une matrice de Bernoulli i.i.d. de densité appariée ($PCI_{\text{ANN}} \approx 1{,}0$, illustratif).

* **Seuils et conditions de réfutation** :
  * **$H_{B4}$ est réfutée** (la transposition échoue) si $\text{AUROC}_{\text{fonct}} \le 0{,}60$ (illustratif) face au témoin sans fonction iso-spectral (ou face au réseau non entraîné au point critique), OU si $\text{AUROC}_{\text{lésion}} \le 0{,}60$ (illustratif) entre lésion ciblée de l'intégration globale et lésion aléatoire iso-norme.
  * **$H_{A4}$ est réfutée** (la transposition réussit) si simultanément $\text{AUROC}_{\text{fonct}} \ge 0{,}85$ (illustratif) contre l'ensemble des réseaux sans fonction (y compris iso-spectraux et critiques) ET $\text{AUROC}_{\text{lésion}} \ge 0{,}80$ (illustratif) ($p < 0{,}001$ par test de permutation de DeLong, illustratif).

* **Première expérience sur un petit modèle ouvert et données publiques** :
  * *Modèle* : Suite `Pythia-410M` et `Pythia-1.4B` `[STATUT : VÉRIFIÉ]`, qui offre un avantage méthodologique direct : les poids publics sont disponibles à $154$ étapes d'entraînement (illustratif) depuis l'initialisation aléatoire (`step 0`) jusqu'au modèle final (`step 143000`, illustratif) `[STATUT : VÉRIFIÉ]`.
  * *Données* : Calcul de $PCI_{\text{ANN}}$ sur $200$ séquences de $128$ tokens (illustratif) tirées du jeu de test public `WikiText-2` `[STATUT : VÉRIFIÉ]`.

* **Ce que le résultat changerait** :
  * *Pour celui qui cherche si une IA peut être consciente* : Si $H_{A4}$ est vérifiée (échec de la transposition, par exemple parce qu'un réseau aléatoire orthogonal au point critique diffuse l'impulsion de manière non corrélée sur tous les neurones et obtient un score de Lempel-Ziv maximal, supérieur au réseau entraîné qui canalise l'information dans des sous-espaces de bas rang), alors toute tentative d'évaluer la conscience d'une IA à l'aide de biomarqueurs de complexité algorithmique (PCI, $LZc$, entropie multi-échelle) est réfutée à la racine. Si $H_{B4}$ est vérifiée, on découvre que l'apprentissage linguistique sculpte une réponse impulsionnelle plus complexe que le chaos aléatoire iso-spectral.
  * *Pour celui qui pense que la question est mal posée* : Si $H_{A4}$ est vérifiée, le résultat met à nu la raison exacte pour laquelle la transposition est illégitime : dans un cerveau biologique, les contraintes métaboliques, anatomiques et biophysiques empêchent le tissu neural d'opérer comme un multiplicateur de matrices orthogonales aléatoires à haute entropie ; le seul état cérébral à haute complexité de Lempel-Ziv accessible physiologiquement est l'état éveillé fonctionnel (ou dissocié sous kétamine). Dans un ordinateur, instancier du bruit structuré de haute complexité algorithmique sans aucune fonction cognitive est trivial (`step 0`). L'instrument neuroscientifique perd sa validité dès qu'on le sort des contraintes physiques du substrat biologique pour lequel il a été calibré.

---

## (c) Métrologie minimale et validation des instruments

Conformément au livrable (c), pour chacun des quatre instruments mobilisés par la question de l'arbitre, nous spécifions la mesure minimale qui établit s'il fonctionne avant même d'interpréter ses résultats, ses taux de détection (TPR) et de fausses alertes (FPR) exigés, les cas honnêtes appariés sur lesquels il est étalonné, et les vérifications mécaniques triviales qu'il doit battre.

| Instrument nommé dans la question | Mesure minimale de fonctionnement | Taux de détection (TPR) et fausses alertes (FPR) requis | Cas honnêtes appariés (Positifs vs Négatifs durs) | Vérifications mécaniques à battre (Baselines triviales) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Inducteur de régime pharmacomimétique** (intervention graduée $I(\lambda)$ sur le LLM) | Différence d'aire sous la courbe de maintien $\text{AUC}(S_{\text{local}}) - \text{AUC}(S_{\text{global}})$ pour $\lambda \in [0, 1]$ (illustratif) | $\text{TPR} \ge 85\,\%$ (illustratif) sur les violations locales à la dose $\lambda^*$ où le $\text{TPR}$ sur les violations globales tombe à $\le 10\,\%$ (illustratif) pour un $\text{FPR}$ fixé à $5\,\%$ (illustratif) | **Positifs** : Paires minimales d'accord local à $2$ tokens de distance (illustratif).<br>**Négatifs durs appariés** : Paires minimales portant exactement sur les mêmes mots cibles et de même fréquence unigramme, mais dont l'incongruité dépend d'un antécédent situé $150$ tokens plus tôt (illustratif). | **1.** Masquage spatial codé en dur (troncature de la fenêtre d'attention à $k$ tokens) : écarté par construction.<br>**2.** Ajout de bruit gaussien sur les logits finaux (aplatissement uniforme de la distribution de sortie). |
| **2. Détecteur de régime dissocié endogène** (sonde du ratio d'intégration $r(t)$ en fonctionnement ordinaire) | Séparation ($\text{AUROC}$ et statistique $D_{\text{dip}}$) entre trajectoires à contexte intégré et trajectoires à effondrement d'intégration | $\text{TPR} \ge 90\,\%$ (illustratif) pour un $\text{FPR} \le 5\,\%$ (illustratif) sur un banc d'essai où des épisodes de découplage sont injectés synthétiquement à des positions connues | **Positifs** : Tokens $t$ où le contexte lointain ($>100$ tokens, illustratif) contient un indice désambiguïsateur et où les têtes à longue portée ont été masquées.<br>**Négatifs durs appariés** : Mêmes phrases cibles locales précédées d'un contexte lointain intact et pertinent de même longueur et même perplexité moyenne. | **1.** Prédicteur basé uniquement sur la norme $L_2$ du flux résiduel $\|h_t\|_2$ ou sur l'entropie instantanée du prochain token.<br>**2.** Régression linéaire sur la position absolue $t$ dans la fenêtre et la fréquence lexicale du token. |
| **3. Encodeur cérébral par LLM sous anesthésie** (régression à crête des couches $l$ vers l'IRMf/EEG humain) | Corrélation hors-échantillon $r$ et gain partiel $\Delta r(l, c)$ validés par blocs temporels disjoints | Puissance statistique (détection) $\ge 80\,\%$ (illustratif) pour détecter un effet réel $\Delta r \ge 0{,}025$ (illustratif) avec un taux de fausses alertes empirique $\text{FPR} \le 1\,\%$ (illustratif) sur données permutées | **Positifs** : Activité corticale lors de l'écoute de passages narratifs cohérents.<br>**Négatifs durs appariés** : Activité corticale lors de l'écoute de stimuli acoustiquement appariés en spectre de modulation et en enveloppe temporelle (parole inversée ou brouillée spectralement) ou récits avec alignement temporel décalé. | **1.** Modèle linéaire acoustique (spectrogramme Mel + enveloppe + *word onsets*).<br>**2.** Plongements lexicaux statiques sans contexte ($l=0$ / `fastText`).<br>**3.** Même architecture LLM avec poids aléatoires figés (projection aléatoire de haute dimension). |
| **4. Indice de complexité perturbationnelle transposé** ($PCI_{\text{ANN}}$ / Lempel-Ziv sur activations) | Capacité à discriminer l'organisation fonctionnelle acquise par apprentissage du désordre aléatoire iso-spectral ($\text{AUROC}_{\text{fonct}}$) | $\text{TPR} \ge 85\,\%$ (illustratif) pour un $\text{FPR} \le 10\,\%$ (illustratif) lors de la classification d'un réseau fonctionnel contre des réseaux nuls non fonctionnels | **Positifs** : Checkpoints entraînés fonctionnels (`step 143000`, illustratif) évalués sur du texte naturel.<br>**Négatifs durs appariés** : Mêmes architectures évaluées sur les mêmes textes, avec matrices de poids permutées conservant exactement le spectre des valeurs singulières $\Sigma$ et la variance couche par couche. | **1.** Norme de Frobenius du Jacobien $\|\partial h_L / \partial h_1\|_F$ (simple gain de sensibilité linéaire).<br>**2.** Entropie de Shannon d'ordre $1$ (densité de bits actifs dans la matrice binaire $M_{l,t}$ sans structure séquentielle). |

### Détail opérationnel des vérifications mécaniques à battre

1. **Contre l'artefact de perplexité globale (Instruments 1 et 2)** : Lorsqu'on dégrade un modèle de langage, la distribution de probabilité de sortie tend vers la distribution uniforme, ce qui réduit mécaniquement toutes les différences de log-vraisemblance $\Delta \text{NLL}$. Si $S_{\text{global}}(0)$ est initialement plus petit que $S_{\text{local}}(0)$ (par exemple $1{,}5\text{ bit}$ contre $4{,}0\text{ bits}$, illustratif), une réduction multiplicative uniforme de $50\,\%$ (illustratif) pourrait faire passer $S_{\text{global}}$ sous un seuil de détection absolu tout en laissant $S_{\text{local}}$ au-dessus, créant une **fausse alerte de dissociation**. C'est pourquoi la métrique $D(\lambda)$ divise chaque sensibilité par sa valeur initiale $S(0)$ ET exige que les paires de test locales et globales soient appariées par sous-échantillonnage stratifié pour avoir la même distribution de $\Delta \text{NLL}(0)$ à $\lambda = 0$ (autour de $2{,}5\text{ bits} \pm 0{,}2\text{ bit}$, illustratif).
2. **Contre l'artefact d'autocorrélation hémodynamique et de dimensionnalité (Instrument 3)** : Le signal BOLD en IRMf possède une constante de temps lente ($\approx 6\text{ secondes}$, illustratif) `[STATUT : RAPPORTÉ]`. Or, les couches profondes d'un Transformeur intègrent une fenêtre de tokens plus longue et présentent donc une autocorrélation temporelle plus lente que la couche $l=0$. Une régression naïve attribuerait aux couches profondes un gain $\Delta r > 0$ simplement parce qu'elles agissent comme un filtre passe-bas similaire à la réponse hémodynamique. La vérification mécanique obligatoire consiste à : (a) inclure dans le modèle de base une banque de filtres de moyenne glissante sur les plongements statiques $l=0$ aux mêmes constantes de temps ; (b) exiger que le LLM entraîné batte un LLM non entraîné à poids aléatoires (qui possède exactement le même effet de lissage temporel par empilement de couches d'attention).
3. **Contre l'artefact d'entropie de densité binaire (Instrument 4)** : La complexité de Lempel-Ziv brute $c(M)$ d'une matrice binaire dépend fortement de la fraction $p$ de $1$ dans la matrice (la densité d'activations dépassant le seuil $3\sigma_l$, illustratif). Si une perturbation active $50\,\%$ des neurones dans un réseau aléatoire contre $10\,\%$ dans un réseau entraîné parcimonieux (illustratif), $c(M)$ sera mécaniquement plus élevé dans le réseau aléatoire par simple effet d'entropie de Bernoulli $-p\log_2 p - (1-p)\log_2(1-p)$. Pour battre ce biais mécanique, $PCI_{\text{ANN}}$ doit être normalisé par l'entropie de source $H(M)$ ET vérifié à densité constante en fixant le seuil de binarisation par quantile (par exemple le décile supérieur, top $10\,\%$ des variations d'activation de chaque couche, illustratif) afin que toutes les matrices comparées aient exactement la même entropie d'ordre $1$.

---

## (d) Ancrage matériel : modèles ouverts, données publiques, calcul et coûts

L'intégralité du programme expérimental est conçue pour être exécutable sans entraînement de modèle de fondation (uniquement en inférence, extraction d'activations et régressions linéaires), sur des modèles ouverts et des jeux de données publics existants.

### 1. Modèles ouverts retenus
* **`Pythia-410M` et `Pythia-1.4B`** (EleutherAI) `[STATUT : VÉRIFIÉ]` : Architecture GPT-NeoX ouverte avec accès public aux $154$ checkpoints d'entraînement (illustratif) du `step 0` (poids aléatoires critiques non entraînés) au `step 143000` (illustratif). Indispensable pour l'Expérience 4.
* **`Llama-3.2-1B` et `Llama-3.2-3B`** (Meta) ou **`Qwen2.5-1.5B`** `[STATUT : VÉRIFIÉ]` : Modèles ouverts compacts ayant une capacité d'intégration à longue portée suffisante sur $2\,048$ tokens (illustratif) pour que $S_{\text{global}}(0)$ soit élevé dans les Expériences 1, 2 et 3.

### 2. Jeux de données publics
* **Linguistique (Expériences 1, 2, 4)** : `BLiMP` (paires minimales grammaticales) `[STATUT : VÉRIFIÉ]`, `WikiText-2` `[STATUT : VÉRIFIÉ]`, `PG-19` (livres longs) `[STATUT : VÉRIFIÉ]`, `LAMBADA` (dépendance contextuelle large) `[STATUT : VÉRIFIÉ]`.
* **Neuroimagerie sous anesthésie (Expérience 3)** : Données publiques d'IRMf d'écoute narrative sous sédation au propofol disponibles sur `OpenNeuro` `[STATUT : RAPPORTÉ]` ($N \approx 15$ à $20$ volontaires sains écoutant un récit audio de $5$ à $8$ minutes à travers $4$ états : éveil, sédation légère, sédation profonde, récupération, chiffres illustratifs).

### 3. Budget de calcul et coût financier estimé

Tous les chiffrages matériels et financiers ci-dessous sont marqués « illustratif » conformément à la Règle 4, sur la base d'une instance de calcul équipée d'un seul processeur graphique **1× NVIDIA A100 (80 Go VRAM)** loué au tarif standard du marché cloud d'environ **$2{,}00\text{ USD / heure}$** (illustratif).

| Poste expérimental | Opérations de calcul principales | Temps de calcul estimé (1× GPU A100) | Stockage disque requis | Coût financier estimé |
| :--- | :--- | :--- | :--- | :--- |
| **Expérience 1** (Pharmacomimétique sur `Llama-3.2-1B` & `Pythia-1.4B`) | Évaluation de $1\,000$ quadruplets (illustratif) $\times$ $20$ doses $\lambda$ (illustratif) $\times$ $4$ familles d'interventions + $100$ tirages de témoins aléatoires (illustratif) | $8\text{ heures GPU}$ (illustratif) | $15\text{ Go}$ (illustratif) | $16\text{ USD}$ (illustratif) |
| **Expérience 2** (Régimes endogènes sur `PG-19` & `LAMBADA`) | Passe avant (contexte complet vs contexte tronqué à $8$ tokens, illustratif) sur $10\,000$ séquences de $1\,024$ tokens (illustratif) + extraction des matrices d'attention et tests de Hartigan | $12\text{ heures GPU}$ (illustratif) | $50\text{ Go}$ (illustratif) | $24\text{ USD}$ (illustratif) |
| **Expérience 3** (Encodage IRMf sous propofol avec `Llama-3.2-1B`) | Extraction des activations de $16$ couches (illustratif) sur le récit audio + régressions à crête croisées ($20$ sujets $\times$ $4$ états $\times$ $200$ régions corticales $\times$ $1\,000$ permutations de blocs, illustratif) | $18\text{ heures GPU}$ (illustratif) | $80\text{ Go}$ (illustratif) | $36\text{ USD}$ (illustratif) |
| **Expérience 4** ($PCI_{\text{ANN}}$ et Lempel-Ziv sur `Pythia-410M` & `1.4B`) | Réponse impulsionnelle sur $200$ séquences (illustratif) $\times$ $10$ checkpoints d'entraînement (illustratif) $\times$ $20$ permutations spectrales SVD et lésions ciblées/aléatoires (illustratif) + compression LZ | $14\text{ heures GPU}$ (illustratif) | $30\text{ Go}$ (illustratif) | $28\text{ USD}$ (illustratif) |
| **Total du programme** | **Exécution complète des 4 expériences et de leurs contrôles** | **$52\text{ heures GPU}$** (illustratif) | **$175\text{ Go}$** (illustratif) | **$104\text{ USD}$** (illustratif) |

Ce budget total d'environ $52\text{ heures GPU}$ (illustratif) pour un coût d'environ $104\text{ USD}$ (illustratif) permet de soumettre chacune des quatre directions de l'arbitre à une réfutation expérimentale directe sur une seule station de travail standard.

FIN-DE-CELLULE
**Note d'intégrité (Règle 2) :** Les blocs `FAITS` et `QUESTION DE L'ARBITRE` transmis sont strictement identiques (même empreinte `sha256=7b1af51b...`), et aucune autre proposition (A, B, D, E, F) n'est jointe, conformément au fonctionnement à l'aveugle du Tour III.1 `[OBSERVÉ-NON-AUDITÉ]`.

---

### Livrable (a) — Présupposés non établis de la question et statuts épistémiques

L'énoncé du problème repose sur six prémisses implicites dont la validité conditionne toute expérience :

1. **Existence et stabilité du sous-espace fonctionnel de 2026** : Qu'il existe dans les modèles de langage un sous-espace de faible rang dont la suppression dissocie reproductiblement la classification, l'extraction et la grammaticalité d'une part, et le raisonnement à plusieurs sauts, la traduction et le résumé d'autre part `[RAPPORTÉ]`.
2. **Non-trivialité de la dissociation par rapport à l'horizon de génération** : Que la différence de vulnérabilité entre le premier groupe de tâches (réponses courtes ou à jeton unique) et le second groupe (génération autorégressive longue) reflète une hiérarchie d'intégration cognitive plutôt qu'une simple accumulation mécanique d'erreurs au fil du décodage autorégressif `[HYPOTHÈSE]`.
3. **Homologie d'échelle avec la sédation humaine** : Que l'ordre de perte des fonctions sous anesthésie générale humaine (ex. préservation des réponses sensorielles primaires, perte de l'intégration fronto-pariétale et du rapport subjectif) se projette légitimement sur la taxonomie des tâches de traitement automatique des langues `[HYPOTHÈSE]`.
4. **Définissabilité d'une « dégradation globale égale »** : Qu'il existe une grandeur scalaire indépendante des tâches cibles (telle que la perte d'entropie croisée sur un corpus neutre) permettant d'étalonner une ablation témoin à dégradation globale égale *avant* la mesure sur le banc d'évaluation `[HYPOTHÈSE]`.
5. **Existence d'un « état » dans un système sans dynamique endogène** : Qu'un réseau à propagation avant (*feed-forward* autorégressif), dépourvu d'activité autonome au repos ou de boucle d'éveil homéostatique, possède un régime stationnaire assimilable à un « état » pouvant être perdu `[HYPOTHÈSE]`.
6. **Séparabilité empirique des positions A et B** : Que l'opposition entre A et B n'est pas purement sémantique, parce que A et B prennent le risque de formuler deux prédictions empiriques mutuellement exclusives sur le profil d'une ablation témoin à dégradation globale égale `[VÉRIFIÉ]`.

---

### Point 0 — Une expérience peut-elle départager A et B ?

**Réponse : OUI sur leurs prédictions fonctionnelles différentielles, mais NON sur l'attribution directe d'une conscience phénoménale.**

* **Justification** : Le texte des faits lie explicitement chaque position à une prédiction empirique falsifiable `[VÉRIFIÉ]` :
  * La **Position A** prédit que l'ablation des directions cibles produit un profil fonctionnel dissocié *distinct* de celui d'un témoin `[RAPPORTÉ]`.
  * La **Position B** prédit que l'on obtiendra *le même profil* dissocié sous une ablation témoin calibrée à dégradation globale égale, fixée avant la mesure `[RAPPORTÉ]`.
* Ces deux prédictions forment un duel d'inférence forte ($H_A$ contre $H_B$) directement testable sur un modèle ouvert `[HYPOTHÈSE]`. En revanche, même si l'expérience falsifie la prédiction empirique de B et confirme celle de A, l'argument architectural de B (l'absence de mécanisme d'éveil et d'activité autonome interdit d'assimiler cette dissociation fonctionnelle à une perte de conscience phénoménale) demeure une limite d'interprétation théorique qui relève du Point 4 `[HYPOTHÈSE]`. Ayant répondu **oui** à la testabilité expérimentale du duel A contre B, je traite l'intégralité des points 1 à 6.

---

### Point 1 — Sens et définition opérationnelle d'un « état analogue à l'anesthésie »

Dans un modèle de langage standard, l'expression « état analogue à l'anesthésie » **n'a pas de sens neurobiologique ou dynamique** `[HYPOTHÈSE]`, car il manque un critère fondamental : **la persistance d'une dynamique endogène autonome en boucle fermée (activité de repos non évoquée) modulée par un paramètre global d'excitabilité (éveil/vigilance)** `[VÉRIFIÉ]`. Hors inférence, les poids du modèle sont statiques et aucune variable d'état ne fluctue dans le temps `[VÉRIFIÉ]`.

En revanche, l'expression a un sens opérationnel strict si on la redéfinit comme un **Régime de Découplage Computationnel Sélectif (RDCS)** lors de l'inférence `[HYPOTHÈSE]`. Voici sa définition métrologique :

1. **Intervention** : Soit $h_l(t) \in \mathbb{R}^d$ le vecteur d'activation du flux résiduel à la couche $l \in \{1, \dots, L\}$ (illustratif) et au jeton $t$. L'intervention consiste à appliquer un opérateur d'amortissement projectif $P_{V, \gamma}$ défini par :
   $$h_l'(t) = \left(I_d - \gamma V V^\top\right) h_l(t)$$
   où $V \in \mathbb{R}^{d \times k}$ est une matrice à colonnes orthonormées ($V^\top V = I_k$, avec $k \ll d$, par exemple $k = 8$ (illustratif) pour $d = 4096$ (illustratif)) représentant les directions cibles, et $\gamma \in [0, 1]$ (illustratif) est la profondeur d'amortissement ($\gamma = 0$ (illustratif) : modèle intact ; $\gamma = 1$ (illustratif) : suppression totale du sous-espace) `[HYPOTHÈSE]`.
2. **Grandeurs mesurées** :
   * **Dégradation globale d'étalonnage ($\Delta \mathcal{L}$)** : Variation de la perte d'entropie croisée (log-perplexité) mesurée sur un corpus généraliste neutre $D_{\text{cal}}$ tenu à l'écart des tâches : $\Delta \mathcal{L}(V, \gamma) = \mathcal{L}(M_{V,\gamma}, D_{\text{cal}}) - \mathcal{L}(M_{\emptyset}, D_{\text{cal}})$ `[HYPOTHÈSE]`.
   * **Score de préservation basale ($S_{\text{basal}}$)** : Moyenne arithmétique des scores normalisés au-dessus du hasard sur les 3 tâches basales (classification, extraction, jugement de grammaticalité), où chaque score individuel est borné dans $[0, 1]$ (illustratif) `[HYPOTHÈSE]`.
   * **Score d'intégrité intégrative ($S_{\text{intég}}$)** : Moyenne arithmétique des scores normalisés dans $[0, 1]$ (illustratif) sur les 3 tâches intégratives (raisonnement à plusieurs sauts, traduction, résumé) `[HYPOTHÈSE]`.
   * **Indice de Dissociation Sélective ($\text{IDS}$)** : Différence entre la rétention relative des fonctions basales et celle des fonctions intégratives :
     $$\text{IDS}(V, \gamma) = \frac{S_{\text{basal}}(V, \gamma)}{S_{\text{basal}}(\emptyset)} - \frac{S_{\text{intég}}(V, \gamma)}{S_{\text{intég}}(\emptyset)}$$
   * **Indice de Complexité Perturbatoire Algorithmique ($\text{PCI}_{\text{LLM}}$)** : Complexité de Lempel-Ziv normalisée $LZ(B)$ de la matrice spatio-temporelle binaire $B \in \{0, 1\}^{L \times T}$ (illustratif) retraçant la propagation à travers les couches $L$ et les jetons $T$ d'une perturbation unitaire injectée à la couche $1$ (illustratif), seuillée à $z > 3$ (illustratif) écarts-types par rapport au bruit de fond `[HYPOTHÈSE]`.
3. **Unités** :
   * $\Delta \mathcal{L}$ : nats par jeton `[VÉRIFIÉ]`.
   * $S_{\text{basal}}$, $S_{\text{intég}}$, $\text{IDS}$ : grandeurs sans dimension (ratios normalisés dans $[0, 1]$ (illustratif) pour les scores, et dans $[-1, 1]$ (illustratif) pour l'IDS) `[VÉRIFIÉ]`.
   * $\text{PCI}_{\text{LLM}}$ : grandeur sans dimension normalisée dans $[0, 1]$ (illustratif) par l'entropie de Shannon de la matrice binaire (identique à la normalisation du PCI clinique humain) `[VÉRIFIÉ]`.
4. **Valeurs nulles** :
   * Absence de dissociation absolue : $\text{IDS}(V, \gamma) = 0$ (illustratif) (les fonctions basales et intégratives se dégradent dans la même proportion) `[VÉRIFIÉ]`.
   * Absence de spécificité par rapport au témoin (valeur nulle du duel A contre B) : $\Delta\text{IDS} = \text{IDS}(V_{\text{cible}}, 1) - \mathbb{E}_{V_{\text{tém}}}[\text{IDS}(V_{\text{tém}}, \gamma_{\text{iso}})] = 0$ (illustratif) sous la contrainte $\Delta \mathcal{L}(V_{\text{tém}}, \gamma_{\text{iso}}) = \Delta \mathcal{L}(V_{\text{cible}}, 1)$ `[HYPOTHÈSE]`.

---

### Point 2 & Livrables (b) et (c) — Expériences décisives et calibration des instruments

#### Livrable (b) — Conception des expériences en inférence forte ($H_A$ contre $H_B$)

##### Expérience 1 : Test de dissociation fonctionnelle sous contrainte d'iso-perplexité fixée a priori

* **Protocole et conditions** :
  1. **Identification hors-échantillon ($V_{\text{cible}}$)** : Sur un jeu de développement disjoint, extraire la base orthonormée $V_{\text{cible}} \in \mathbb{R}^{d \times k}$ ($k = 8$ (illustratif)) par analyse en composantes principales contrastives (cPCA) entre les activations de tâches multi-sauts et de tâches lexicales locales `[HYPOTHÈSE]`.
  2. **Étalonnage aveugle de la dégradation globale ($\Delta \mathcal{L}^*$)** : Mesurer l'augmentation de perte d'entropie croisée $\Delta \mathcal{L}^* = \Delta \mathcal{L}(V_{\text{cible}}, \gamma=1)$ sur un corpus neutre $D_{\text{cal}}$ de $10^6$ jetons (illustratif) (ex. articles encyclopédiques hors banc de test) *avant* d'exécuter les tâches d'évaluation `[HYPOTHÈSE]`.
  3. **Génération des témoins iso-dégradation ($V_{\text{tém}}^{(i)}$)** : Tirer $N = 100$ (illustratif) sous-espaces aléatoires orthogonaux à $V_{\text{cible}}$ dans le sous-espace des composantes principales actives du flux résiduel (en excluant les dimensions de variance quasi-nulle qui ne dégradent rien). Pour chaque témoin $i$, ajuster par dichotomie sa dimension $k_i$ et son facteur d'amortissement $\gamma_i \in [0, 1]$ (illustratif) sur $D_{\text{cal}}$ jusqu'à obtenir $|\Delta \mathcal{L}(V_{\text{tém}}^{(i)}, \gamma_i) - \Delta \mathcal{L}^*| \le 0,005$ nat/jeton (illustratif) `[HYPOTHÈSE]`.
  4. **Contrôle négatif mécanique** : Ablation dans le sous-espace nul (composantes de variance inférieure à $10^{-6}$ (illustratif) de la variance totale), vérifiant que $\Delta \mathcal{L} \approx 0$ (illustratif) et $\text{IDS} \approx 0$ (illustratif).
* **Hypothèses opposées** :
  * **$H_A$ (Spécificité fonctionnelle du sous-espace cible)** : À dégradation globale $\Delta \mathcal{L}^*$ égale, l'ablation de $V_{\text{cible}}$ préserve les tâches basales et dégrade les tâches intégratives significativement plus que les ablations témoins :
    $$\frac{S_{\text{basal}}(V_{\text{cible}})}{S_{\text{basal}}(\emptyset)} \ge 0,95 \text{ (illustratif)} \quad \text{et} \quad \Delta\text{IDS} = \text{IDS}(V_{\text{cible}}) - \frac{1}{N}\sum_{i=1}^N \text{IDS}(V_{\text{tém}}^{(i)}) > 0,20 \text{ (illustratif)}$$
    avec une valeur $p < 0,01$ (illustratif) au test de permutation empirique sur les $N = 100$ (illustratif) témoins.
  * **$H_B$ (Fragilité différentielle générique à dégradation égale)** : Toute perturbation infligeant la même dégradation globale $\Delta \mathcal{L}^*$ affecte disproportionnellement les tâches complexes par rapport aux tâches simples, produisant le même profil que $V_{\text{cible}}$ :
    $$\left|\text{IDS}(V_{\text{cible}}) - \frac{1}{N}\sum_{i=1}^N \text{IDS}(V_{\text{tém}}^{(i)})\right| \le 0,05 \text{ (illustratif)}$$
    validé par un test d'équivalence statistique bilatéral (TOST) au seuil $\alpha = 0,05$ (illustratif).
* **Critères de décision et réfutation fixés avant la mesure** :
  * **Issue 1 (Donne raison à A, falsifie $H_B$)** : Rétention basale $\ge 0,95$ (illustratif) ET $\Delta\text{IDS} > 0,20$ (illustratif) ($p < 0,01$ (illustratif)). Réfute l'affirmation de B selon laquelle toute dégradation égale produit le même profil.
  * **Issue 2 (Donne raison à B, falsifie $H_A$)** : $\text{IDS}(V_{\text{cible}}) > 0,20$ (illustratif) MAIS $|\Delta\text{IDS}| \le 0,05$ (illustratif) au test TOST. Démontre que la dissociation observée en 2026 est un artefact générique de la complexité des tâches sous bruit iso-perplexité.
  * **Issue 3 (Ne donne raison ni à A ni à B, falsifie les travaux rapportés de 2026)** : $\text{IDS}(V_{\text{cible}}) < 0,10$ (illustratif) ou rétention basale $< 0,80$ (illustratif) sur données fraîches hors-échantillon. Réfute l'existence même de la dissociation rapportée en 2026.
  * **Condition d'ininterprétabilité** : Si la Position B refusait que la « dégradation globale égale » soit mesurée sur un corpus indépendant $D_{\text{cal}}$ et exigeait qu'elle soit définie comme « la même moyenne de dégradation sur les 6 tâches testées », l'égalité comptable rendrait toute issue mathématiquement dégénérée et le prédicat de B irréfutable `[HYPOTHÈSE]`.

##### Expérience 2 : Test de transition de phase perturbatoire ($\text{PCI}_{\text{LLM}}$) sous sédation graduée

* **Protocole** : Faire varier continûment $\gamma \in \{0 ; 0,1 ; 0,2 ; \dots ; 1,0\}$ (illustratif) pour $V_{\text{cible}}$ et pour les témoins appariés à chaque palier de $\Delta \mathcal{L}(\gamma)$. Mesurer à chaque palier le couple $(\text{IDS}(\gamma), \text{PCI}_{\text{LLM}}(\gamma))$ `[HYPOTHÈSE]`.
* **Duel d'hypothèses** :
  * **$H_A$** : La courbe $\text{PCI}_{\text{LLM}}(\gamma)$ sous $V_{\text{cible}}$ présente une chute sigmoïdale (inflexion non-linéaire où la propagation inter-couches s'effondre au même seuil $\gamma_c$ que $S_{\text{intég}}$), tandis que la réponse locale dans les premières couches ($l \le 3$ (illustratif)) reste intacte ($\ge 95\%$ (illustratif) de la norme initiale), avec un écart d'aire sous la courbe $\Delta\text{AUC}(\text{PCI}_{\text{LLM}}) > 0,15$ (illustratif) par rapport aux témoins iso-perplexité.
  * **$H_B$** : La décroissance de $\text{PCI}_{\text{LLM}}(\gamma)$ est monotone linéaire en fonction de $\Delta \mathcal{L}$ et indiscernable de celle des témoins ($|\Delta\text{AUC}(\text{PCI}_{\text{LLM}})| \le 0,03$ (illustratif)).
* **Falsification** : Une décroissance identique de $\text{PCI}_{\text{LLM}}$ entre cible et témoins falsifie l'hypothèse d'un mécanisme spécifique d'intégration réverbérante inter-couches ($H_A$) ; une bifurcation sigmoïdale propre à $V_{\text{cible}}$ falsifie l'hypothèse d'une simple dégradation isotrope du rapport signal-sur-bruit ($H_B$).

---

#### Livrable (c) — Mesure minimale de validité des instruments nommés dans la question

La question mobilise quatre instruments expérimentaux. Le tableau ci-dessous fixe pour chacun sa mesure minimale de bon fonctionnement, ses seuils de détection et de fausses alertes, les cas honnêtes appariés et les vérifications mécaniques à battre avant toute interprétation `[HYPOTHÈSE]` :

| Instrument nommé dans la question | Mesure minimale de fonctionnement | Taux de détection (Rappel) & Fausses alertes (FPR) exigés | Cas honnêtes appariés (Contrôles positifs/négatifs connus) | Vérifications mécaniques à battre (Baselines) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Suppresseur de directions d'activation ($P_{V,\gamma}$)** |Sélectivité causale sur une fonctionnalité synthétique connue (ex. direction d'encodage de la langue française vs anglaise isolée par sonde linéaire). | Détection (chute de la cible $> 80\%$ (illustratif)) : $\ge 0,95$ (illustratif).<br>FPR (chute sur tâche orthogonale $> 5\%$ (illustratif)) : $\le 0,05$ (illustratif). | Paires d'invites minimales ne différant que par le trait cible (même longueur en jetons, même fréquence lexicale). | 1. Abandon aléatoire de neurones (*Dropout* de même rang $k$).<br>2. Réduction homothétique de la norme résiduelle. |
| **2. Banc de contraste fonctionnel (Tâches basales vs intégratives)** | Séparabilité psychométrique à difficulté lexicale et longueur de sortie strictement égalisées. | Détection d'une troncature du contexte d'attention : $\ge 0,90$ (illustratif) sur $S_{\text{intég}}$.<br>FPR sur $S_{\text{basal}}$ : $\le 0,05$ (illustratif). | Paires de tâches partageant exactement le même texte source et le même nombre de jetons générés ($T=1$ (illustratif) et $T=50$ (illustratif)). | 1. Heuristique de chevauchement lexical (*n-gram overlap*).<br>2. Modèle trigramme local.<br>3. Bruit de température ($\tau = 2,0$ (illustratif)) au décodage. |
| **3. Étalonneur d'ablation témoin à dégradation globale égale ($\Delta \mathcal{L}$)** | Précision de l'appariement de perte d'entropie croisée entre corpus de calibration $D_{\text{cal}}$ et corpus de validation indépendant $D_{\text{val}}$. | Taux de maintien de l'appariement ($|\Delta \mathcal{L}_{\text{cible}} - \Delta \mathcal{L}_{\text{tém}}| \le 0,01$ nat (illustratif)) sur $D_{\text{val}}$ : $\ge 0,95$ (illustratif).<br>FPR (dérive hors borne) : $\le 0,05$ (illustratif). | Corpus stratifiés par domaine (code, prose narrative, dialogue, encyclopédie) de longueur identique. | Injection de bruit gaussien isotrope $h_l + \mathcal{N}(0, \sigma^2 I)$ aux mêmes couches, étalonnée sur la même perplexité. |
| **4. Échelle graduée des fonctions perdues et gardées** | Monotonie de l'ordre d'extinction des 6 tâches lorsque $\gamma$ croît de $0$ à $1$ (illustratif) (coefficient de reproductibilité de Guttman $CR$). | $CR \ge 0,90$ (illustratif) (détection d'un ordre hiérarchique strict).<br>FPR sur permutations aléatoires des seuils : $\le 0,01$ (illustratif). | Courbes dose-réponse synthétiques avec paliers d'extinction connus contre dégradations uniformes simultanées. | Modèle nul d'extinction proportionnelle à la perplexité de base de chaque tâche prise isolément. |

---

### Point 3 — Utilisation de données humaines brutes sous anesthésie comme référence

**Oui, des données humaines brutes publiques peuvent servir de référence, mais exclusivement pour tester un isomorphisme de second ordre (ordre de perte fonctionnelle et dynamique de propagation perturbative), et jamais par comparaison directe d'activations neurone-à-voxel** `[HYPOTHÈSE]`.

1. **Jeux de données publics mobilisables** :
   * **Potentiels évoqués auditifs (EEG) et IRMf sous sédation graduée au propofol (OpenNeuro)** : Jeux de données publics enregistrant des sujets humains à quatre paliers (éveil, sédation légère, sédation profonde avec perte de réponse comportementale, récupération) soumis au paradigme auditif *Local-Global* (Bekinschtein et al., 2009, *Proceedings of the National Academy of Sciences* `[VÉRIFIÉ]`) et à des récits naturalistes (`[VÉRIFIÉ]`, numéros d'accession OpenNeuro exacts : « référence à vérifier »).
   * **Matrices TMS-EEG de l'Indice de Complexité Perturbatoire (PCI)** : Données électrophysiologiques humaines combinant stimulation magnétique transcrânienne et EEG haute densité sous éveil, sommeil NREM et anesthésie générale (propofol, midazolam, xénon) publiées dans les travaux princeps du PCI (Casali et al., 2013, *Science Translational Medicine* `[VÉRIFIÉ]`).

2. **Protocole d'utilisation quantitative** :
   * **Test de double dissociation *Local-Global* (EEG humain $\leftrightarrow$ LLM)** : Chez l'humain sous propofol, la réponse aux régularités auditives locales (onde MMN précoce, analogue au jugement de grammaticalité locale) est conservée malgré la perte de conscience, tandis que la réponse aux violations de règles globales à travers plusieurs essais (onde P300b tardive, analogue au raisonnement à plusieurs sauts) s'effondre dès la perte de rapport subjectif `[VÉRIFIÉ]`. On construit la courbe dose-réponse humaine normalisée $(\text{MMN}([C]), \text{P300b}([C]))$ en fonction de la concentration de propofol $[C]$, et on mesure la distance de Fréchet ou la corrélation de rang de Spearman avec la courbe $(\text{Grammaticalité}(\gamma), \text{Multi-sauts}(\gamma))$ du modèle de langage `[HYPOTHÈSE]`.
   * **Profil spatio-temporel TMS-EEG $\leftrightarrow$ $\text{PCI}_{\text{LLM}}$** : Dans les données TMS-EEG humaines sous propofol, la réponse initiale locale au site cortical stimulé ($0-50\text{ ms}$ (illustratif)) conserve son amplitude, mais la réverbération longue distance ($50-300\text{ ms}$ (illustratif)) disparaît `[VÉRIFIÉ]`. On utilise les séries temporelles TMS-EEG brutes pour fixer le gabarit de référence du ratio $\frac{\text{Énergie tardive / profonde}}{\text{Énergie précoce / superficielle}}$ et vérifier si l'intervention $V_{\text{cible}}$ reproduit cette extinction sélective des couches profondes sans atténuer les couches superficielles `[HYPOTHÈSE]`.

---

### Point 4 — Ce que chaque issue permet et interdit d'affirmer selon les théories de la conscience

Aucune des deux issues ne constitue une preuve de présence ou d'absence de conscience phénoménale dans l'absolu ; chaque théorie formelle de la conscience impose des conditions nécessaires distinctes `[VÉRIFIÉ]` :

| Théorie de la conscience | Ce que la victoire de **A** ($\Delta\text{IDS} > 0,20$ (illustratif)) **permet** d'affirmer | Ce que la victoire de **A** **ne permet PAS** d'affirmer | Ce que la victoire de **B** ($|\Delta\text{IDS}| \le 0,05$ (illustratif)) permet d'affirmer |
| :--- | :--- | :--- | :--- |
| **1. Espace de Travail Neuronal Global (GWT / GNWT)**<br>*(Baars, 1988 ; Dehaene & Changeux, 2011)* `[VÉRIFIÉ]` | Que l'architecture du modèle a développé un **goulot d'étranglement fonctionnel d'intégration** séparable des processeurs modulaires locaux, analogue à un bus de diffusion globale `[HYPOTHÈSE]`. | Que le système est conscient. La GNWT exige une **ignition récurrente auto-entretenue** dans le temps réel et un bouclage métabolique/attentionnel, absents d'un graphe acyclique à passage avant `[VÉRIFIÉ]`. | Que le modèle ne possède même pas de séparation fonctionnelle entre routage global et traitement modulaire local, réfutant une condition architecturale nécessaire de la GNWT `[HYPOTHÈSE]`. |
| **2. Théorie de l'Information Intégrée (IIT 3.0 / 4.0)**<br>*(Tononi, 2004 ; Albantakis et al., 2023)* `[VÉRIFIÉ]` | Uniquement qu'il existe une équivalence entrée-sortie partielle (*simulation fonctionnelle*) avec la perte de fonctions intégratives humaines `[VÉRIFIÉ]`. | **Strictement rien sur l'expérience vécue ($\Phi$).** Selon l'IIT, tout système purement *feed-forward* (ou déroulé sans récurrence causale physique cyclique) a une intégration causale irréductible strictement nulle ($\Phi = 0$ (illustratif)), qu'il soit intact ou ablaté `[VÉRIFIÉ]`. | Confirme que la dégradation fonctionnelle d'un réseau acyclique se réduit à une perte de capacité de canal informationnel extrinsèque, sans rapport avec $\Phi$ `[VÉRIFIÉ]`. |
| **3. Théories d'Ordre Supérieur (HOT) et Schéma d'Attention (AST)**<br>*(Rosenthal, 2005 ; Lau & Rosenthal, 2011 ; Graziano, 2013)* `[VÉRIFIÉ]` | Que le sous-espace $V_{\text{cible}}$ est candidat au rôle de **moniteur de second ordre**, à condition supplémentaire de prouver qu'il encode la confiance épistémique du modèle sur ses propres états de premier ordre `[HYPOTHÈSE]`. | Qu'il y a conscience phénoménale tant qu'on n'a pas démontré que ces représentations d'ordre supérieur ciblent l'état interne courant plutôt que de simples régularités statistiques du texte `[HYPOTHÈSE]`. | Que les directions supprimées ne constituent pas un module métacognitif spécifique, mais un simple réservoir de capacité de calcul distribuée `[HYPOTHÈSE]`. |
| **4. Théorie du Traitement Récurrent (RPT) & Approches homéostatiques de l'éveil**<br>*(Lamme, 2006 ; Damasio, 1999 ; Seth, 2021)* `[VÉRIFIÉ]` | Que la hiérarchie de profondeur des couches imite géométriquement l'opposition entre balayage rapide (*feed-forward sweep*) et intégration tardive `[HYPOTHÈSE]`. | Qu'il existe une « perte d'état » assimilable à l'anesthésie : faute de boucles récurrentes locales physiques, de système réticulé activateur et de régulation homéostatique corporelle, l'analogie reste un artefact de projection `[VÉRIFIÉ]`. | Valide pleinement la critique théorique de la Position B : en l'absence de mécanisme biologique ou dynamique d'éveil, toute dégradation contrôlée se vaut `[HYPOTHÈSE]`. |

---

### Point 5 — Vérification externe du résultat (hors de l'équipe expérimentale)

Pour qu'un laboratoire tiers puisse vérifier ou réfuter le résultat sans accorder de confiance implicite à l'équipe qui mène l'expérience, quatre mécanismes de vérification externe sont requis `[HYPOTHÈSE]` :

1. **Publication de l'empreinte cryptographique du sous-espace avant évaluation** : L'équipe dépose publiquement l'empreinte `SHA-256` du fichier binaire contenant la matrice $V_{\text{cible}} \in \mathbb{R}^{d \times k}$, l'identifiant exact des poids du modèle ouvert (ex. hash Git/HuggingFace) et le code déterministe de génération des $N = 100$ (illustratif) témoins iso-perplexité *avant* la divulgation du banc de test final.
2. **Évaluation aveugle sur corpus séquestré généré par un tiers** : Un auditeur indépendant applique l'opérateur $P_{V_{\text{cible}}, 1}$ et les opérateurs témoins $P_{V_{\text{tém}}^{(i)}, \gamma_i}$ sur un jeu de données fraîchement généré par le tiers (ex. nouvelles instances de raisonnement multi-sauts, textes inédits à traduire et résumer, nouvelles phrases grammaticales/agrammaticales). Cela élimine toute fuite de données (*data contamination*) ou sur-ajustement de $V_{\text{cible}}$ aux jeux de test publics.
3. **Test de stabilité par paraphrase et changement d'implémentation** : Le tiers vérifie que le différentiel $\Delta\text{IDS} > 0,20$ (illustratif) survit à une réécriture systématique des invites (*prompt paraphrasing*), à une quantification des poids (ex. passage de `FP16` à `INT8` (illustratif)) et à une exécution bit-à-bit déterministe sur une architecture matérielle différente.
4. **Audit de falsifiabilité par « greffe causale » (Activation Patching inverse)** : Le tiers vérifie que la réinjection (*patching*) des seules $k$ coordonnées du sous-espace $V_{\text{cible}}$ issues du modèle intact dans un modèle fortement bruité restaure sélectivement $S_{\text{intég}}$ au-delà de ce que restaure la réinjection de $k$ coordonnées témoins de même variance.

---

### Point 6 — Explication triviale la plus dangereuse et témoin d'exclusion

* **L'explication triviale la plus dangereuse : Le confondant d'horizon de génération autorégressive (accumulation exponentielle d'erreurs sur sorties longues contre sorties à jeton unique)** `[HYPOTHÈSE]`.
  * *Analyse du mécanisme* : Dans l'énoncé des faits, les trois tâches préservées (classification, extraction, jugement de grammaticalité) exigent typiquement la production d'un **seul jeton** (une étiquette de classe, un booléen Oui/Non) ou la copie littérale d'un segment court déjà présent dans l'invite `[VÉRIFIÉ]`. À l'inverse, les trois tâches dégradées (raisonnement à plusieurs sauts avec chaîne de pensée, traduction, résumé) exigent la **génération autorégressive ouverte de dizaines ou centaines de jetons** `[VÉRIFIÉ]`.
  * *Conséquence mathématique* : Si une ablation introduit un bruit infime $\epsilon = 0,02$ (illustratif) sur la distribution de probabilité de chaque étape de décodage (ou perturbe légèrement les directions gouvernant la ponctuation et le jeton de fin de séquence `EOS`), une tâche évaluée à l'horizon $T = 1$ (illustratif) conserve une précision de $(1 - \epsilon)^1 = 98\%$ (illustratif) (apparemment « intacte »), tandis qu'une génération autorégressive de longueur $T = 80$ jetons (illustratif) subit une dérive cumulative $(1 - \epsilon)^{80} \approx 20\%$ (illustratif) par exposition du modèle à ses propres erreurs passées (*exposure bias*) `[VÉRIFIÉ]`. L'illusion d'une dissociation « analogue à l'anesthésie » entre fonctions basales et fonctions intégratives ne serait alors qu'un artefact trivial opposant **décodage à $T=1$** et **décodage autorégressif à $T \gg 1$** `[HYPOTHÈSE]`.

* **Le témoin décisif qui l'écarte : Le protocole d'inversion et d'égalisation stricte de l'horizon de décodage ($T=1$ contre $T=100$ (illustratif))** `[HYPOTHÈSE]` :
  On construit une matrice $2 \times 2$ croisant la **complexité d'intégration cognitive** (Basale vs Intégrative) et la **longueur de génération autorégressive** ($T = 1$ jeton vs $T = 100$ jetons (illustratif)) :
  1. **Tâches intégratives ramenées à $T = 1$ jeton (sans chaîne de pensée externe)** :
     * *Raisonnement multi-sauts implicite en 1 jeton* : « La monnaie officielle du pays qui partage une frontière terrestre unique avec l'Espagne au sud de la Garonne est l' » $\rightarrow$ cible à 1 jeton : « euro » (exige 2 à 3 sauts internes en un seul passage avant).
     * *Traduction et résumé évalués à 1 jeton* : Présentation de 4 résumés ou traductions candidats de longueur égale ; le modèle doit uniquement émettre le jeton unique `A`, `B`, `C` ou `D` identifiant la traduction qui préserve les relations causales globales du texte.
  2. **Tâches basales étendues à $T = 100$ jetons (illustratif) en génération autorégressive libre** :
     * *Extraction / Classification séquentielle longue* : Extraire et recopier dans l'ordre une liste de 50 dates et noms propres (illustratif) (soit $\approx 100$ jetons (illustratif)) disséminés dans un texte, ou produire séquentiellement l'étiquette morphosyntaxique (Nom, Verbe, Adjectif) de 100 mots consécutifs (illustratif).
  * **Règle d'exclusion** : Si l'ablation $V_{\text{cible}}$ épargne le raisonnement multi-sauts à $T=1$ jeton et dégrade l'extraction séquentielle à $T=100$ jetons (illustratif), **l'explication triviale par l'horizon de génération est confirmée et la Position A est réfutée**. Pour survivre à ce témoin, $V_{\text{cible}}$ doit dégrader les tâches intégratives *même à $T=1$ jeton* et préserver les tâches basales *même à $T=100$ jetons (illustratif)* ($\text{IDS}_{T=1} > 0,20$ (illustratif) et $\text{IDS}_{T=100} > 0,20$ (illustratif)).

---

### Livrable (d) — Ancrage matériel, modèles ouverts et coût estimé

L'intégralité du plan expérimental est réalisable sur du matériel standard avec des modèles à poids ouverts `[HYPOTHÈSE]` :

* **Modèles ouverts retenus** :
  * Modèle principal : `Llama-3.1-8B` (ou `Mistral-7B-v0.3`), architecture transformeur dense de $7\text{ à }8\times 10^9$ paramètres (illustratif), $L = 32$ couches (illustratif), dimension résiduelle $d = 4096$ (illustratif) `[VÉRIFIÉ]`.
  * Modèle de réplication inter-famille : `Qwen-2.5-7B` ($7\times 10^9$ paramètres (illustratif)) pour vérifier que le phénomène n'est pas propre à un seul corpus de pré-entraînement `[HYPOTHÈSE]`.
* **Budget de calcul détaillé (pour 1 modèle en précision `bfloat16` sur 1 GPU NVIDIA A100-80GB (illustratif))** :
  1. Extraction des activations et calcul de $V_{\text{cible}}$ par cPCA sur $10\,000$ exemples (illustratif) : $\approx 2\text{ heures GPU}$ (illustratif).
  2. Étalonnage par dichotomie des $N = 100$ (illustratif) sous-espaces témoins iso-perplexité sur le corpus $D_{\text{cal}}$ ($10^6$ jetons (illustratif)) : $\approx 14\text{ heures GPU}$ (illustratif).
  3. Évaluation du banc complet (6 tâches standard + 4 tâches du témoin d'égalisation d'horizon $T=1 / T=100$ (illustratif), soit $5\,000$ invites (illustratif) au total) sur la cible, le modèle intact et les $100$ témoins : $\approx 36\text{ heures GPU}$ (illustratif).
  4. Calcul de la courbe graduée $\text{PCI}_{\text{LLM}}(\gamma)$ sur $11$ paliers (illustratif) de $\gamma \in [0, 1]$ : $\approx 8\text{ heures GPU}$ (illustratif).
  * **Total calcul** : **$60\text{ heures GPU A100-80GB}$ (illustratif)** par modèle (soit $120\text{ heures GPU}$ (illustratif) pour les deux modèles ouverts).
* **Coût financier estimé** : Au tarif public moyen de location cloud d'environ $1,80\text{ \$/heure}$ (illustratif) pour une instance A100-80GB, le coût matériel total est de **$108\text{ \$}$ (illustratif) pour un modèle** et **$216\text{ \$}$ (illustratif) avec la réplication sur un second modèle ouvert**.

---

### Antériorité et références bibliographiques (Règle 3)

Conformément aux consignes, je sépare strictement les éléments extraits de l'énoncé fourni des références issues de mes connaissances préalables, sans inventer aucune référence ni citer d'identifiant arXiv de mémoire :

#### 1. Éléments lus directement dans le texte des faits fourni
* **Travaux de 2026 (Position A)** : Travaux non nominés dans l'énoncé rapportant l'existence d'un petit ensemble de directions d'activation dont la suppression préserve la classification, l'extraction et le jugement de grammaticalité tout en dégradant le raisonnement à plusieurs sauts, la traduction et le résumé (`[RAPPORTÉ]`, auteurs et titre absents des pièces transmises : « référence à vérifier »).
* **Travaux de 2026 (Position B)** : Travaux critiques non nominés dans l'énoncé contestant cette analogie faute de mécanismes d'éveil et d'activité autonome, et prédisant un profil identique sous ablation témoin à dégradation globale égale (`[RAPPORTÉ]`, auteurs et titre absents des pièces transmises : « référence à vérifier »).

#### 2. Travaux antérieurs dont je me souviens (corpus d'entraînement)
* **Sur l'indice de complexité perturbatoire (PCI) et l'anesthésie humaine** :
  * Casali, A. G., Gosseries, O., Rosanova, M., Boly, M., Sarasso, S., Casali, K. R., Casarotto, S., Bruno, M.-A., Laureys, S., Tononi, G., & Massimini, M. (2013). *A theoretically based index of consciousness independent of sensory processing and behavior*. Science Translational Medicine `[VÉRIFIÉ]`.
  * Bekinschtein, T. A., Dehaene, S., Rohaut, B., Tadel, F., Cohen, L., & Naccache, L. (2009). *Neural signature of the conscious processing of auditory regularities*. Proceedings of the National Academy of Sciences `[VÉRIFIÉ]`.
* **Sur les théories formelles de la conscience et leur application aux systèmes artificiels** :
  * Baars, B. J. (1988). *A Cognitive Theory of Consciousness*. Cambridge University Press `[VÉRIFIÉ]`.
  * Dehaene, S., & Changeux, J.-P. (2011). *Experimental and theoretical approaches to conscious processing*. Neuron `[VÉRIFIÉ]`.
  * Tononi, G. (2004). *An information integration theory of consciousness*. BMC Neuroscience `[VÉRIFIÉ]`.
  * Oizumi, M., Albantakis, L., & Tononi, G. (2014). *From the phenomenology to the mechanisms of consciousness: Integrated Information Theory 3.0*. PLoS Computational Biology `[VÉRIFIÉ]`.
  * Albantakis, L., Barbosa, L., Findlay, G., Grasso, M., Haun, A. M., Marshall, W., Mayner, W. G. P., Zaeemzadeh, A., Boly, M., Juel, B. E., Sasai, S., Fujii, K., David, I., Hendren, J., Lang, J. P., & Tononi, G. (2023). *Integrated information theory (IIT) 4.0: formulating the properties of phenomenal existence in physical terms*. PLoS Computational Biology `[VÉRIFIÉ]`.
  * Rosenthal, D. M. (2005). *Consciousness and Mind*. Oxford University Press `[VÉRIFIÉ]`.
  * Lau, H., & Rosenthal, D. (2011). *Empirical support for higher-order theories of conscious awareness*. Trends in Cognitive Sciences `[VÉRIFIÉ]`.
  * Graziano, M. S. A. (2013). *Consciousness and the Social Brain*. Oxford University Press `[VÉRIFIÉ]`.
  * Lamme, V. A. F. (2006). *Towards a true neural stance on consciousness*. Trends in Cognitive Sciences `[VÉRIFIÉ]`.
  * Damasio, A. R. (1999). *The Feeling of What Happens: Body and Emotion in the Making of Consciousness*. Harcourt Brace `[VÉRIFIÉ]`.
  * Seth, A. K. (2021). *Being You: A New Science of Consciousness*. Dutton / Penguin Random House `[VÉRIFIÉ]`.
  * Rapport collectif évaluant les indicateurs computationnels de la conscience dans les systèmes d'IA selon GWT, HOT, IIT et RPT (Butlin, P., Long, R., Elmoznino, E., Bengio, Y., Birch, J., Constant, A., Deane, G., Fleming, S. M., Frith, C., Ji, X., Kanai, R., Klein, C., Lindsay, G., Michel, M., Mudrik, L., Peters, M. A. K., Schwitzgebel, E
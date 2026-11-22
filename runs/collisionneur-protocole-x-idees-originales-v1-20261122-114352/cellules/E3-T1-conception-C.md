**Note d'intégrité (Règle 2)** : Les blocs `FAITS` et `QUESTION DE L'ARBITRE` transmis sont strictement identiques (même empreinte `sha256`) et aucun jeu de données empiriques ni aucune autre proposition (A, B, D, E, F) n'est joint à ce tour à l'aveugle. Conformément à la consigne de la question (« N'avancez aucun chiffre sans source ») et à la Règle 4 du protocole, aucune affirmation théorique ou empirique ne repose sur un chiffre non sourcé, et toutes les valeurs numériques paramétrant les protocoles expérimentaux (seuils, tailles d'échantillons, coûts) portent explicitement la mention `(illustratif)`.

---

## (a) Présupposés non établis de la question et reformulation du problème (Question 5)

### 1. Inventaire des présupposés implicites et de leur statut

L'énoncé du problème repose sur six présupposés méthodologiques qui ne sont pas établis dans les faits transmis :

1. **Existence d'une relation d'équivalence intrinsèque entre « idées »** — Statut : `[HYPOTHÈSE]`.
   Parler d'idées « rarement proposées » ou demander si « des appels indépendants reviennent aux mêmes idées » suppose qu'il existe une partition bien définie de l'espace des sorties textuelles en classes d'équivalence sémantiques ou fonctionnelles. Dans un espace de chaînes de caractères, deux générations suffisamment longues diffèrent presque toujours par leur syntaxe de surface (`[OBSERVÉ-NON-AUDITÉ]`). Sans opérateur de réduction canonique, la fréquence empirique de chaque chaîne brute est égale à l'unité divisée par le nombre d'appels, rendant la rareté triviale et non informative.
2. **Invariance de la fiabilité du contrôle indépendant hors de sa distribution d'étalonnage** — Statut : `[HYPOTHÈSE]`.
   L'énoncé postule un contrôle « fiable sur des cas d'essai dont la vérité est connue » et cherche à l'utiliser pour valider des idées « rarement proposées ». Or, la fiabilité mesurée sur un ensemble d'essai connu (en distribution) ne garantit pas que le taux de faux positifs $\alpha$ et le taux de faux négatifs $\beta$ restent constants dans les queues de distribution des modèles générateurs. Optimiser la recherche vers des régions rares sélectionne activement les cas pathologiques ou les angles morts du vérificateur (loi de Goodhart, `[RAPPORTÉ]` : Marilyn Strathern, 1997, *Improving ratings: audit in the British University system*, « référence à vérifier »).
3. **Indépendance entre la rareté de génération et la probabilité a priori de validité** — Statut : `[HYPOTHÈSE]`.
   Chercher à « augmenter le rythme de telles idées sans augmenter les fausses découvertes » suppose que l'on peut explorer des régions de plus en plus rares de la distribution générative sans dégrader la valeur prédictive positive du contrôle. Si la prévalence réelle des idées vraies $\pi(r)$ décroît avec la rareté $r$, un contrôle à taux de faux positifs $\alpha > 0$ constant produira mécaniquement une proportion croissante de fausses découvertes (`[VÉRIFIÉ]` par le théorème de Bayes).
4. **Indépendance conditionnelle des modèles composant le système** — Statut : `[HYPOTHÈSE]`.
   Un système « fait de plusieurs modèles de langue » ne garantit pas la diversité des propositions : des modèles entraînés sur des corpus chevauchants et alignés par des procédures similaires partagent des modes de défaillance et des puits d'attraction communs (`[OBSERVÉ-NON-AUDITÉ]`).
5. **Fongibilité des coûts de génération et de contrôle** — Statut : `[HYPOTHÈSE]`.
   La contrainte « à coût total égal » suppose un modèle de coût explicite $B = N_{\text{gen}} C_{\text{gen}} + N_{\text{verif}} C_{\text{verif}}$. L'efficacité de toute intervention dépend du rapport $C_{\text{verif}} / C_{\text{gen}}$, qui n'est pas spécifié dans l'énoncé.

### 2. Pourquoi le problème est mal posé et comment le reposer (Question 5)

Le problème, tel qu'énoncé, est **mal posé** pour trois raisons formelles :
* **Ambiguïté ontologique** : La « rareté d'une idée » n'est pas définie tant que l'on n'a pas fixé le morphisme $f : \mathcal{X} \to \mathcal{S}$ qui projette une trace textuelle brute $x \in \mathcal{X}$ vers une représentation canonique ou une signature comportementale $s \in \mathcal{S}$ vérifiable sans modèle de langue.
* **Confusion entre erreur de type I ($\alpha$) et taux de fausses découvertes ($\text{FDR}$)** : À caractéristique opérationnelle $(\alpha, \beta)$ du contrôle fixée, le taux de fausses découvertes $\text{FDR} = \mathbb{P}(\text{Faux} \mid \text{Confirmé})$ n'est pas un paramètre intrinsèque du contrôle, mais une fonction de la prévalence $\pi$ des idées vraies dans le sous-espace exploré (`[VÉRIFIÉ]`). On ne peut donc pas exiger simultanément d'explorer des régions où $\pi$ est arbitrairement faible, de garder le même seuil de contrôle, et de ne pas augmenter les fausses découvertes.
* **Absence de fonction d'allocation budgétaire** : Sans distinguer le coût d'échantillonnage du générateur ($C_{\text{gen}}$) et le coût d'interrogation du contrôle ($C_{\text{verif}}$), la condition « à coût total égal » est indéterminée.

**Reformulation rigoureuse du problème** :
> Soit un système génératif $\mathcal{G}$ produisant des candidats $x \in \mathcal{X}$ au coût unitaire $C_{\text{gen}}$, un opérateur déterministe de projection canonique $\phi : \mathcal{X} \to \mathcal{S}$ (sans modèle de langue) de coût négligeable définissant des classes d'équivalence fonctionnelle $s = \phi(x)$, et un oracle de contrôle externe $V : \mathcal{X} \to \{0, 1\}$ de coût unitaire $C_{\text{verif}}$, caractérisé sur un banc d'étalonnage par une sensibilité $1-\beta$ et un taux de fausses alertes $\alpha$.
> Sous une contrainte de budget total $B = N_{\text{gen}} C_{\text{gen}} + N_{\text{verif}} C_{\text{verif}}$, comment concevoir une politique d'échantillonnage et de filtrage pré-oracle qui maximise l'espérance du nombre de classes fonctionnelles distinctes confirmées $\lvert \{ s \in \mathcal{S} : \exists x \in \phi^{-1}(s), V(x) = 1 \text{ et } \hat{p}_{\mathcal{G}}(s) \le \tau_r \} \rvert$ appartenant à la queue de distribution ($\hat{p}_{\mathcal{G}}(s) \le \tau_r$), tout en maintenant le taux de fausses découvertes $\text{FDR} = \mathbb{E}\left[\frac{V_{\text{faux}}}{V_{\text{faux}} + V_{\text{vrai}}}\right]$ sous un plafond $\ \le q$ fixé à l'avance ?

---

## (b) Mesures sans juge-modèle, interventions, limites et expériences décisives (Questions 1, 2, 3, 4)

### 1. Mesurer la rareté et la valeur sans se fier au jugement d'un modèle (Question 1)

Pour exclure tout modèle de langue de la boucle d'évaluation, la mesure doit reposer exclusivement sur des transformations algébriques, syntaxiques ou exécutables déterministes.

#### A. Mesure de la rareté : projection fonctionnelle et estimateurs de fréquence
La rareté d'un candidat $x$ ne doit pas être mesurée par sa vraisemblance neuronale (perplexité d'un modèle, qui mesure la rareté de la formulation et non de l'idée), mais par la fréquence empirique de sa **classe d'équivalence mécanique** $s = \phi(x)$ sur un échantillon de $N_{\text{gen}}$ tirages indépendants :

1. **Signature comportementale sur batterie d'épreuves (Domaine exécutable, algorithmes, stratégies, mécanismes simulables)** — Statut : `[VÉRIFIÉ]` (principe du test différentiel et de l'équivalence observationnelle).
   On définit un ensemble fixe de $K$ entrées de sondage (cas d'essai non-oracles) $E = \{e_1, \dots, e_K\}$. L'idée $x$ est exécutée ou simulée sur $E$, produisant un vecteur de sorties ou de trajectoires d'états $\phi(x) = (y_1, \dots, y_K)$. Deux propositions textuellement différentes qui produisent exactement le même vecteur $\phi(x)$ tombent dans le même « puits » fonctionnel. La rareté empirique de la classe $s = \phi(x)$ est estimée par sa fréquence $\hat{p}(s) = \frac{\text{compte}(s)}{N_{\text{gen}}}$, corrigée pour les petits échantillons par l'estimateur de couverture de Good-Turing qui évalue la masse de probabilité totale des classes vues exactement $r$ fois (`[VÉRIFIÉ]` : I. J. Good, 1953, *The population frequencies of species and the estimation of population parameters*).
2. **Invariants structurels canoniques (Domaine formel, moléculaire, logique)** — Statut : `[VÉRIFIÉ]`.
   L'idée $x$ est compilée vers un graphe ou un arbre syntaxique abstrait normalisé (par exemple : réduction bêta-êta dans un assistant de preuve, graphe moléculaire canonique InChI, ou forme normale conjonctive minimale). La rareté est la fréquence inverse d'apparition de cet invariant exact ou la distance d'édition d'arbre minimale aux invariants déjà observés.
3. **Distance normale de compression (Domaine textuel non compilable)** — Statut : `[RAPPORTÉ]` (Rudi Cilibrasi et Paul M. B. Vitányi, 2005, *Clustering by compression*).
   À défaut de compilateur, la nouveauté par rapport à une archive $\mathcal{A}$ d'idées antérieures est mesurée par un compresseur déterministe sans réseau de neurones (par exemple LZMA ou Zstandard) via la distance normale de compression :
   $$\text{NCD}(x, \mathcal{A}) = \frac{C(x \cdot \mathcal{A}) - \min(C(x), C(\mathcal{A}))}{\max(C(x), C(\mathcal{A}))}$$
   où $C(\cdot)$ est la longueur en octets du fichier compressé. Cette mesure capture les redondances lexicales et structurelles, mais reste aveugle aux paraphrases synonymiques profondes (`[HYPOTHÈSE]`).

#### B. Mesure de la valeur : évaluation par le contrôle indépendant et gain marginal
La valeur d'une idée $x$ est mesurée sans modèle par le produit de deux facteurs mécaniques :
1. **Validation binaire ou continue par le contrôle indépendant** $V(x) \in \{0, 1\}$ (ou score physique/formel continu $v(x) \in \mathbb{R}$, tel qu'un taux de réussite sur une batterie de cas de validation tenus secrets, une énergie de liaison calculée par mécanique quantique, ou la vérification formelle d'un théorème par un noyau logique de type Lean/Coq).
2. **Domination de Pareto ou réduction d'erreur hors-échantillon** : Une idée confirmée a une valeur marginale positive si et seulement si son vecteur de performance sur le contrôle indépendant domine strictement l'enveloppe convexe des idées fréquentes déjà connues (par exemple, elle résout un sous-ensemble de cas d'essai sur lesquels les classes fréquentes échouent).

---

### 2. Interventions à coût total égal (Question 2)

Considérons un budget total fixe $B = N_{\text{gen}} C_{\text{gen}} + N_{\text{verif}} C_{\text{verif}}$ dans le régime courant où le contrôle indépendant est plus coûteux que la génération ($C_{\text{verif}} > C_{\text{gen}}$).

#### Intervention I1 : Déduplication fonctionnelle pré-contrôle et allocation stratifiée (Écrémage des puits fréquents)
* **Mécanisme** : Augmenter $N_{\text{gen}}$ et réduire les appels redondants $N_{\text{verif}}$. Chaque idée générée $x_i$ est projetée à faible coût sur sa signature fonctionnelle $s_i = \phi(x_i)$. On regroupe les candidats par classe $s$. Au lieu de soumettre toutes les idées générées au contrôle coûteux $V$, on ne soumet qu'un seul représentant par classe $s$, en priorisant les classes de faible fréquence empirique $\hat{p}(s) \le \tau_r$ qui respectent les contraintes de bonne formation syntaxique.
* **Ce qu'elle garantit et sous quelles hypothèses** :
  * *Garantie* : À budget $B$ constant, augmente monotonement le nombre de classes fonctionnelles rares distinctes soumises au contrôle $V$, tant que la distribution générative est concentrée sur des modes redondants (entropie de Shannon $H(\phi(\mathcal{G})) \ll \log N_{\text{gen}}$) et que le coût du projecteur $C_\phi \ll C_{\text{verif}}$ (`[VÉRIFIÉ]` arithmétiquement).
  * *Hypothèse requise* : Homogénéité intra-classe vis-à-vis de l'oracle ($\forall x, x' \in \mathcal{X}, \phi(x) = \phi(x') \implies V(x) = V(x')$).
* **Ce qu'elle ne garantit pas** : Elle ne garantit pas que les classes rares ainsi testées contiennent des idées vraies, ni que le taux de fausses découvertes ($\text{FDR}$) reste constant si la prévalence réelle des idées vraies chute dans les classes rares.
* **Meilleur indice pour** : Dans la synthèse de programmes par modèles de langue (ex. AlphaCode), le regroupement des candidats par comportement d'entrées-sorties sur des tests exemples avant soumission finale permet d'extraire des solutions correctes issues de grappes rares que l'échantillonnage brut manque (`[RAPPORTÉ]` : Yujia Li et al., 2022, *Competition-level code generation with AlphaCode*, Science — statut de confiance sur la source : élevé, publication revue par les pairs).
* **Meilleur indice contre** : Si la signature $\phi$ est trop grossière (collision de hachage fonctionnel), des idées valides rares sont fusionnées avec des idées invalides fréquentes et éliminées avant d'atteindre le contrôle (`[HYPOTHÈSE]`, risque inhérent à l'approximation de l'équivalence par un nombre fini de tests).

#### Intervention I2 : Partitionnement déterministe de l'espace des descripteurs (Recherche Qualité-Diversité de type MAP-Elites sans juge neuronal)
* **Mécanisme** : Remplacer l'échantillonnage libre (ou par hausse de température, qui dégrade la cohérence syntaxique) par une grille de contraintes structurelles déterministes (grammaires formelles, interdiction de sous-graphes ou d'opérateurs fréquents, bornes sur des descripteurs phénotypiques mesurables mécaniquement). Le budget de génération est réparti uniformément entre les cellules de cette grille d'attributs.
* **Ce qu'elle garantit et sous quelles hypothèses** :
  * *Garantie* : Borne inférieurement la dispersion géométrique des candidats dans l'espace des descripteurs choisis, empêchant l'effondrement modal (*mode collapse*) des générateurs sur un unique puits d'attraction (`[VÉRIFIÉ]` par construction de la partition).
  * *Hypothèse requise* : Les descripteurs mécaniques définissant la grille sont corrélés à la diversité des mécanismes sous-jacents du domaine et les modèles possèdent une capacité résiduelle non nulle à respecter ces contraintes syntaxiques.
* **Ce qu'elle ne garantit pas** : Elle ne garantit pas que forcer un modèle hors de ses modes naturels préserve sa précision factuelle ou logique ; la contrainte peut pousser le modèle à générer des artefacts syntaxiquement conformes à la cellule mais scientifiquement absurdes.
* **Meilleur indice pour** : Les algorithmes d'illumination d'espace de recherche (MAP-Elites) démontrent que contraindre l'exploration selon une grille de descripteurs phénotypiques découvre des solutions performantes dans des niches inaccessibles à l'optimisation directe non contrainte (`[RAPPORTÉ]` : Jean-Baptiste Mouret et Jeff Clune, 2015, *Illuminating search spaces by mapping elites*, « référence à vérifier » — statut de confiance sur l'existence et le mécanisme de l'article : élevé, référence classique du domaine Qualité-Diversité).
* **Meilleur indice contre** : Sous décodage fortement contraint ou hors distribution d'entraînement, les modèles de langue subissent une dégradation de la validité sémantique de leurs sorties à mesure que l'on s'éloigne des préfixes à haute probabilité (`[OBSERVÉ-NON-AUDITÉ]`, phénomène connu de dégradation sous contraintes formelles rigides, « référence à vérifier »).

#### Intervention I3 : Seuil de confirmation adaptatif indexé sur la rareté et double contrôle orthogonal (Contrôle explicite du FDR)
* **Mécanisme** : Pour éviter que l'exploration des queues de distribution (via I1 ou I2) n'augmente les fausses découvertes, on couple l'intensité de la vérification à la rareté empirique $\hat{p}(s)$ de l'idée. Toute idée issue d'une classe rare ($\hat{p}(s) \le \tau_r$) qui franchit un premier passage du contrôle indépendant est soumise à une pénalité de tests multiples (procédure de Benjamini-Hochberg ou seuil de p-valeur pondéré par l'estimation de la probabilité a priori $\hat{p}(s)$) ou doit franchir $k > 1$ `(illustratif)` variantes indépendantes / perturbées du contrôle avant d'être déclarée « découverte confirmée ». Le surcoût de cette double vérification sur les rares positifs est financé par l'économie réalisée grâce à la déduplication I1 des candidats fréquents.
* **Ce qu'elle garantit et sous quelles hypothèses** :
  * *Garantie* : Maintient l'espérance du taux de fausses découvertes ($\text{FDR}$) sous le seuil nominal $q$ malgré la baisse de la proportion d'idées vraies dans les queues de distribution (`[VÉRIFIÉ]` mathématiquement sous l'hypothèse d'indépendance ou de dépendance positive des statistiques de test : Yoav Benjamini et Yosef Hochberg, 1995, *Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing*, Journal of the Royal Statistical Society).
  * *Hypothèse requise* : Les erreurs (faux positifs) des $k$ réplications ou perturbations du contrôle indépendant ne sont pas parfaitement corrélées (absence de biais systématique déterministe de l'oracle sur le candidat $x$).
* **Ce qu'elle ne garantit pas** : Si le contrôle indépendant souffre d'un défaut structurel déterministe (un bogue du simulateur qui attribue systématiquement un score élevé à une classe d'artefacts), la répétition du même contrôle ne réduira pas les fausses découvertes ; il faut alors un contrôle *orthogonal*. En outre, durcir le seuil réduit la puissance statistique ($1-\beta$) et peut rejeter d'authentiques idées rares.
* **Meilleur indice pour** : Les procédures de contrôle du FDR pondérées par des probabilités a priori (ou *p-weight* / *e-values*) contrôlent rigoureusement l'inflation des faux positifs lors de criblages à haut débit où les vrais positifs sont très rares (`[RAPPORTÉ]` : Yoav Benjamini et Yosef Hochberg, 1997, *Multiple hypotheses testing with weights*, Scandinavian Journal of Statistics — statut de confiance sur la source : élevé).
* **Meilleur indice contre** : En présence d'optimisation contre un oracle imparfait (*reward hacking* ou sélection extrême), les erreurs de l'oracle sont structurelles et reproductibles, rendant les tests d'hypothèses classiques inopérants contre les faux positifs systématiques (`[RAPPORTÉ]` : Joar Skalse et al., 2022, *Defining and Characterizing Reward Hacking*, « référence à vérifier » — statut de confiance sur le phénomène rapporté : élevé).

---

### 3. Expériences décisives et critères d'abandon (Question 3 & Livrable b)

Conformément à la règle d'inférence forte (B4), chaque expérience oppose deux hypothèses exclusives $H_A$ et $H_B$.

#### Expérience E0 : Test de la structure de convergence des appels indépendants (Prérequis de l'énoncé)
* **Question tranchée** : Des appels indépendants au système multi-modèles reviennent-ils aux mêmes idées fonctionnelles ?
* **Hypothèse $H_A$ (Concentration en puits d'attraction)** : La distribution des classes d'équivalence fonctionnelle $\phi(x)$ suit une loi fortement asymétrique ; une fraction minoritaire des classes concentre la majorité de la masse de probabilité générative.
* **Hypothèse $H_B$ (Dispersion uniforme / absence de puits récurrents)** : Les appels indépendants ne convergent pas ; chaque nouvel appel génère une classe fonctionnelle inédite avec une probabilité proche de l'unité.
* **Protocole et métrique** : Générer $N_{\text{gen}} = 10\,000$ `(illustratif)` propositions par appels indépendants (graines aléatoires distinctes, sans historique partagé) à travers les modèles du système. Projeter chaque proposition via $\phi(x)$ (vecteur de sorties sur $K = 100$ `(illustratif)` entrées de sondage). Mesurer le taux de couverture de Good-Turing $\hat{C} = 1 - \frac{N_1}{N_{\text{gen}}}$ (où $N_1$ est le nombre de classes vues une seule fois, dites *singletons*) ainsi que la masse cumulée $M_{10\%}$ des $10\%$ `(illustratif)` de classes les plus fréquentes.
* **Contrôle négatif** : Remplacer les sorties des modèles par un générateur aléatoire syntaxiquement valide (grammaire stochastique uniforme du domaine) sur lequel $\hat{C}$ doit tendre vers $0$ `(illustratif)`.
* **Seuil de décision et falsification** :
  * Si $\hat{C} \ge 0,50$ `(illustratif)` et $M_{10\%} \ge 0,60$ `(illustratif)`, **$H_B$ est falsifiée** : les appels indépendants reviennent massivement aux mêmes idées, ce qui justifie le problème et l'intervention I1.
  * Si $\hat{C} < 0,05$ `(illustratif)` (plus de $95\%$ `(illustratif)` de singletons fonctionnels malgré la normalisation $\phi$), **$H_A$ est falsifiée** : le système ne présente pas de puits fréquents récurrents (ou l'opérateur $\phi$ est défaillant, voir Section c).

#### Expérience E1 : Test de l'Intervention I1 (Déduplication fonctionnelle pré-oracle vs Échantillonnage direct)
* **Question tranchée** : À budget total $B$ égal, l'écrémage des classes fréquentes via $\phi$ avant appel au contrôle indépendant augmente-t-il le rendement en idées rares confirmées sans augmenter les fausses découvertes ?
* **Hypothèse $H_A$ (Gain par déduplication pré-oracle)** : Le transfert de budget des vérifications redondantes vers une génération accrue ($N_{\text{gen}} \uparrow$) suivie d'un filtrage des classes fréquentes ($\hat{p}(s) > \tau_r$) augmente le nombre de classes rares confirmées tout en maintenant le $\text{FDR}$ stable.
* **Hypothèse $H_B$ (Inefficacité ou inflation des fausses découvertes)** : La déduplication pré-oracle n'augmente pas le nombre de vraies découvertes rares (soit parce que le coût de génération absorbe le budget, soit parce que les classes rares sélectionnées ne contiennent que des faux positifs du contrôle).
* **Protocole et métrique** : Sur un banc d'essai où l'on dispose à la fois du contrôle indépendant standard $V$ et d'un oracle de vérité terrain absolu de référence $V^*$ (utilisé uniquement en post-évaluation pour mesurer les vrais et faux positifs de $V$), allouer un budget fixe $B = 10\,000$ `(illustratif)` unités de coût (avec $C_{\text{verif}} / C_{\text{gen}} = 20$ `(illustratif)`). Comparer le bras témoin (échantillonnage direct soumis à $V$) et le bras I1 (génération élargie, regroupement par $\phi$, soumission à $V$ uniquement des classes avec $\hat{p}(s) \le 0,01$ `(illustratif)`).
  * *Métriques* : (1) Nombre de classes rares distinctes réellement vraies $Y_{\text{rare}} = \lvert \{s : \hat{p}(s) \le 0,01 \text{ et } V(x)=1 \text{ et } V^*(x)=1 \} \rvert$ `(illustratif)` ; (2) Taux de fausses découvertes empirique $\widehat{\text{FDR}} = \frac{\lvert \{s : V(x)=1 \text{ et } V^*(x)=0 \} \rvert}{\lvert \{s : V(x)=1 \} \rvert}$.
* **Contrôle négatif** : Appliquer I1 avec une fonction de projection aléatoire $\phi_{\text{rand}}$ (hachage cryptographique de la chaîne brute) qui détruit l'équivalence fonctionnelle.
* **Seuil de décision, falsification et critère d'abandon** :
  * Si $Y_{\text{rare}}(\text{I1}) \ge 1,5 \times Y_{\text{rare}}(\text{Témoin})$ `(illustratif)` ET $\widehat{\text{FDR}}(\text{I1}) \le \widehat{\text{FDR}}(\text{Témoin}) + 0,02$ `(illustratif)`, **$H_B$ est falsifiée**.
  * **Critère d'abandon de I1** : Si $Y_{\text{rare}}(\text{I1}) \le Y_{\text{rare}}(\text{Témoin})$ `(illustratif)` ou si $\widehat{\text{FDR}}(\text{I1}) > \widehat{\text{FDR}}(\text{Témoin}) + 0,05$ `(illustratif)` sur $R = 30$ `(illustratif)` réplications indépendantes, **$H_A$ est falsifiée et l'intervention I1 est abandonnée**.

#### Expérience E2 : Test de l'Intervention I2 (Grille de contraintes structurelles MAP-Elites vs Hausse de température)
* **Question tranchée** : Pour forcer l'exploration de puits étroits à budget égal, un partitionnement déterministe par descripteurs structurels (I2) domine-t-il une simple augmentation de l'entropie d'échantillonnage (température / *top-p*) ?
* **Hypothèse $H_A$ (Domination du guidage structurel)** : Le partitionnement de l'espace par contraintes déterministes produit davantage de classes rares fonctionnellement valides ($V^*(x)=1$) que l'augmentation de la température, laquelle produit principalement du bruit syntaxique rejeté ou des artefacts.
* **Hypothèse $H_B$ (Suffisance de l'agitation thermique / toxicité des contraintes)** : Imposer des contraintes structurelles dégrade la capacité d'inférence des modèles au point de produire moins d'idées rares valides qu'un échantillonnage à haute température ($T \in [1,2 ; 1,8]$ `(illustratif)`).
* **Protocole et métrique** : À budget $B$ égal et à pipeline de vérification identique, comparer le rendement $Y_{\text{rare}}$ et le taux de rejet syntaxique précoce entre le bras I2 (grille de $10 \times 10$ `(illustratif)` cellules définies par deux descripteurs mécaniques du domaine, ex. profondeur d'arbre syntaxique et nombre d'opérateurs non linéaires) et le bras Thermique (balayage de température).
* **Contrôle négatif** : Grille de contraintes orthogonales au domaine (ex. contraindre la longueur des noms de variables ou la parité du nombre de caractères).
* **Seuil de décision, falsification et critère d'abandon** :
  * Si $Y_{\text{rare}}(\text{I2}) > Y_{\text{rare}}(\text{Thermique})$ avec une marge d'au moins $25\%$ `(illustratif)` à $\widehat{\text{FDR}}$ non supérieur, **$H_B$ est falsifiée**.
  * **Critère d'abandon de I2** : Si $Y_{\text{rare}}(\text{I2}) \le Y_{\text{rare}}(\text{Thermique})$ ou si la proportion de générations syntaxiquement invalides sous I2 dépasse $80\%$ `(illustratif)` du budget de génération, **$H_A$ est falsifiée et l'intervention I2 est abandonnée**.

#### Expérience E3 : Test de l'Intervention I3 (Seuil de contrôle adaptatif indexé sur la rareté vs Seuil fixe)
* **Question tranchée** : Le durcissement du critère de confirmation en fonction de la rareté empirique $\hat{p}(s)$ est-il nécessaire et suffisant pour empêcher l'explosion des fausses découvertes dans les queues de distribution ?
* **Hypothèse $H_A$ (Nécessité et efficacité de la correction bayésienne/FDR)** : Sous exploration intensive des queues (I1+I2), un seuil fixe de l'oracle $V$ entraîne une dérive du $\widehat{\text{FDR}}$ au-delà du plafond toléré $q = 0,10$ `(illustratif)`, tandis que la règle adaptative I3 (exiger $k(\hat{p}) = \lceil 1 + \lambda \log_{10}(1/\hat{p}(s)) \rceil$ `(illustratif)` tests orthogonaux réussis) maintient $\widehat{\text{FDR}} \le 0,10$ `(illustratif)` tout en conservant un rendement net $Y_{\text{rare}} > 0$ `(illustratif)`.
* **Hypothèse $H_B$ (Corrélation déterministe des erreurs de l'oracle ou effondrement de la puissance)** : Soit les faux positifs de l'oracle $V$ sont reproductibles et franchissent les tests répétés ($\widehat{\text{FDR}} > 0,10$ `(illustratif)` malgré I3), soit le durcissement élimine la quasi-totalité des vraies découvertes rares ($Y_{\text{rare}}$ chute de plus de $80\%$ `(illustratif)` par rapport au témoin).
* **Protocole et métrique** : Sur le flux de candidats rares généré par I1+I2, appliquer le contrôle à seuil fixe vs le contrôle adaptatif I3. Évaluer $\widehat{\text{FDR}}$ et $Y_{\text{rare}}$ contre la vérité terrain $V^*$.
* **Contrôle négatif** : Appliquer la pénalité de seuil de manière inversée (durcir le seuil sur les idées fréquentes et le relâcher sur les idées rares), ce qui doit dégrader maximalement le $\widehat{\text{FDR}}$.
* **Seuil de décision, falsification et critère d'abandon** :
  * Si $\widehat{\text{FDR}}(\text{Fixe}) > 0,10$ `(illustratif)` ET $\widehat{\text{FDR}}(\text{I3}) \le 0,10$ `(illustratif)` ET $Y_{\text{rare}}(\text{I3}) \ge 0,5 \times Y_{\text{rare}}(\text{Fixe})$ `(illustratif)`, **$H_B$ est falsifiée**.
  * **Critère d'abandon de I3** : Si $\widehat{\text{FDR}}(\text{I3}) > 0,10$ `(illustratif)` (échec de la maîtrise des faux positifs par corrélation des erreurs de l'oracle) OU si $Y_{\text{rare}}(\text{I3}) < 0,2 \times Y_{\text{rare}}(\text{Fixe})$ `(illustratif)` (effondrement de la puissance), **$H_A$ est falsifiée et l'intervention I3 est abandonnée** (imposant alors de remplacer le contrôle indépendant lui-même).

---

### 4. Limites de principe bornant ce qu'on peut espérer (Question 4)

Quatre limites formelles, indépendantes de l'ingénierie des modèles, bornent le système :

1. **Limite bayésienne du taux de base (Effondrement de la valeur prédictive positive dans les queues)** — Statut : `[VÉRIFIÉ]`.
   Soit $\pi(r) = \mathbb{P}(V^*(x)=1 \mid \text{rareté} = r)$ la prévalence réelle des idées vraies au niveau de rareté $r$, et soit un contrôle indépendant de sensibilité $1-\beta$ et de taux de fausses alertes $\alpha > 0$. La proportion de fausses découvertes parmi les idées confirmées à ce niveau de rareté vaut exactement :
   $$\text{FDR}(r) = \frac{\alpha (1 - \pi(r))}{\alpha (1 - \pi(r)) + (1 - \beta)\pi(r)} = \frac{1}{1 + \frac{1-\beta}{\alpha} \frac{\pi(r)}{1-\pi(r)}}$$
   Dès que l'on explore des puits étroits où la probabilité a priori qu'une génération soit vraie chute très en dessous du taux d'erreur du contrôle ($\pi(r) \ll \alpha$), $\text{FDR}(r) \to 1$. Aucune intervention sur le générateur ne peut contourner cette limite si $\alpha$ est fixe et strictement positif : pour maintenir un $\text{FDR}$ borné quand $\pi(r) \to 0$, il faut que le taux de faux positifs effectif du contrôle décroisse au moins aussi vite que $\pi(r)$ ($\alpha(r) = \mathcal{O}(\pi(r))$).
2. **Borne d'échantillonnage de Good-Turing et plafond budgétaire** — Statut : `[VÉRIFIÉ]`.
   Pour observer au moins une fois avec une probabilité $1-\delta$ un puits étroit de masse de probabilité générative $p$ sous échantillonnage indépendant, il faut un nombre d'appels $N_{\text{gen}} \ge \frac{\ln(1/\delta)}{p}$. Sous un budget total $B$, la rareté minimale accessible sans modifier la distribution des modèles est bornée inférieurement par $p_{\min} \approx \frac{C_{\text{gen}} \ln(1/\delta)}{B}$. De plus, l'estimation sans biais de la rareté relative de deux singletons (classes vues une seule fois) est informationnellement impossible sans hypothèse paramétrique sur la queue de distribution (`[VÉRIFIÉ]` : I. J. Good, 1953, *op. cit.*).
3. **Indécidabilité de l'équivalence fonctionnelle (Théorème de Rice)** — Statut : `[VÉRIFIÉ]` (Henry Gordon Rice, 1953, *Classes of recursively enumerable sets and their decision problems*, Transactions of the American Mathematical Society).
   Dès que le domaine d'idées (algorithmes, mécanismes dynamiques, stratégies) atteint l'expressivité d'un système Turing-complet, toute propriété sémantique non triviale — et en particulier l'équivalence fonctionnelle exacte de deux idées $\phi(x) = \phi(x')$ sur toutes les entrées possibles — est algorithmiquement indécidable. Tout capteur de rareté non neuronal $\phi$ opérant en temps fini est donc une approximation (sous-approximation syntaxique ou sur-approximation par un nombre fini de tests).
4. **Vulnérabilité structurelle du contrôle hors distribution (Loi de Goodhart extrême)** — Statut : `[RAPPORTÉ]`.
   Si le contrôle indépendant $V$ est un modèle physique approché, un simulateur numérique ou une batterie finie de cas d'essai, son erreur $\lvert V(x) - V^*(x) \rvert$ n'est bornée que sur le support de sa distribution de calibration. Dans les régions de très faible densité générative, la sélection des candidats maximisant $V(x)$ agit comme un attaquant contradictoire (*adversarial attack*) qui exploite systématiquement les singularités numériques ou les cas limites omis par le contrôle.

---

## (c) Métrologie minimale des instruments (Livrable c)

Le problème mobilise trois instruments. Voici le protocole minimal permettant de certifier que chacun fonctionne avant toute campagne de découverte.

| Instrument | Taux de détection (TPR) et de fausses alertes (FPR) exigés | Cas honnêtes appariés d'étalonnage | Vérifications mécaniques (baselines) à battre |
| :--- | :--- | :--- | :--- |
| **1. Capteur de rareté sans modèle ($\phi$ : projecteur d'équivalence fonctionnelle)** | **Tâche** : Détecter que deux formulations distinctes expriment la *même* idée (collision légitime).<br>• $\text{TPR}_{\text{équiv}} \ge 0,95$ `(illustratif)` (probabilité de regrouper deux clones fonctionnels).<br>• $\text{FPR}_{\text{équiv}} \le 0,01$ `(illustratif)` (probabilité de fusionner à tort deux mécanismes distincts). | • **Paires positives (clones honnêtes)** : $500$ `(illustratif)` idées de référence soumises à des transformations préservant la sémantique (renommage systématique, permutation d'étapes commutatives, réécriture algébrique équivalente).<br>• **Paires négatives (mutants proches)** : Les mêmes $500$ `(illustratif)` idées soumises à une mutation minimale altérant le mécanisme (inversion d'un signe, changement d'un opérateur logique ou d'un groupe fonctionnel). | 1. Correspondance exacte de chaînes après nettoyage des espaces.<br>2. Similarité de Jaccard sur $n$-grammes de caractères ($n=3$ `(illustratif)`).<br>3. Distance normale de compression (NCD via Zstandard) au même seuil de FPR. |
| **2. Contrôle indépendant ($V$ : oracle de valeur)** | **Tâche** : Confirmer une idée réellement valide ($V^*=1$) et rejeter une idée fausse ($V^*=0$).<br>• Sur les cas connus : $\text{TPR}_V \ge 0,90$ `(illustratif)`, $\text{FPR}_V \le 0,01$ `(illustratif)`.<br>• Sur les queues rares (avec I3) : $\text{FPR}_{V,\text{queue}} \le \frac{q}{1-q} \frac{\hat{\pi}_{\text{queue}}}{1-\hat{\pi}_{\text{queue}}} (1-\beta)$ `(illustratif)` pour garantir $\text{FDR} \le q$. | • **Positifs honnêtes hors-échantillon** : $200$ `(illustratif)` vérités établies du domaine retirées de la base d'entraînement/calibration et reformulées dans le style syntaxique des générateurs.<br>• **Négatifs appariés (leurres plausibles)** : $200$ `(illustratif)` « presque-vérités » construites par altération chirurgicale d'une condition nécessaire dans chacune des vérités retirées (respectant toutes les lois de conservation de surface mais fausses). | 1. Filtre syntaxique / compilateur seul (vérifie uniquement que l'idée est bien formée et exécutable sans erreur).<br>2. Sous-ensemble réduit du contrôle ($10\%$ `(illustratif)` des cas d'essai de $V$) pour vérifier que la fiabilité croît bien avec la taille de la batterie d'essai. |
| **3. Système génératif multi-modèles sous intervention ($\mathcal{G}_{\text{I1+I2}}$)** | **Tâche** : Produire des classes fonctionnelles rares confirmées par unité de budget $B$.<br>• Taux de couverture des niches rares connues $\text{TPR}_{\text{niche}} \ge 0,20$ `(illustratif)`.<br>• Taux de fausses découvertes de bout en bout $\text{FDR}_{\text{système}} \le 0,10$ `(illustratif)`. | • **Banc à puits connus (environnement planté)** : Un problème algorithmique ou formel admettant exactement $M = 20$ `(illustratif)` familles de solutions analytiquement connues, dont $2$ `(illustratif)` solutions standard (fréquentes dans les corpus publics) et $18$ `(illustratif)` solutions non standard mais valides (puits étroits). | 1. Échantillonnage i.i.d. d'un modèle unique à température $T = 1,0$ `(illustratif)` à budget total $B$ égal.<br>2. Recherche aléatoire guidée par mutations syntaxiques (algorithme génétique sans modèle de langue) à budget $B$ égal. |

---

## (d) Ancrage matériel et chiffrage (Livrable d)

Pour exécuter les expériences décisives E0 à E3 et certifier les instruments de la section (c) de manière reproductible, l'architecture matérielle et logicielle suivante est retenue. *Tous les chiffres de dimensionnement et de coût ci-dessous sont marqués `(illustratif)` conformément à la Règle 4.*

### 1. Domaine d'instanciation et modèles ouverts
* **Domaine d'essai à vérité terrain exacte** : Synthèse d'algorithmes de résolution de contraintes combinatoires et de mécanismes symboliques (équations fonctionnelles / invariants de boucles) évalués en Python/C++ et doublés d'un vérificateur formel (solveur SMT Z3 ou assistant de preuve Lean 4, `[RAPPORTÉ]`).
  * *Justification* : Ce domaine fournit à la fois un projecteur fonctionnel $\phi$ rapide (vecteur de sorties sur $K = 100$ `(illustratif)` entrées de sondage déterministes), un contrôle indépendant réaliste $V$ (batterie de $1\,000$ `(illustratif)` cas d'essai tenus secrets), et un oracle de vérité terrain absolu $V^*$ (preuve d'équivalence ou de contre-exemple par solveur SMT Z3 avec temps de calcul étendu) permettant de mesurer exactement le taux de fausses découvertes ($\text{FDR}$) de $V$.
* **Système de modèles de langue ouverts** (`[RAPPORTÉ]`, poids ouverts exécutables localement pour garantir l'absence de dérive d'API et le contrôle exact des graines aléatoires) :
  1. `Qwen-2.5-Coder-7B-Instruct` et `Qwen-2.5-72B-Instruct` (famille Qwen).
  2. `Llama-3.1-8B-Instruct` et `Llama-3.1-70B-Instruct` (famille Llama).
  3. `Mistral-7B-Instruct-v0.3` / `Codestral-22B` (famille Mistral).
  4. `DeepSeek-Coder-V2-Lite-Instruct` (architecture MoE distincte pour tester la diversité inter-familles).

### 2. Budget de calcul et coût estimé
* **Génération (Inférence GPU via moteur vLLM)** :
  * Volume par expérience : $N_{\text{gen}} = 50\,000$ `(illustratif)` générations par bras expérimental, d'une longueur moyenne de $512$ `(illustratif)` jetons (*tokens*), soit $2,56 \times 10^7$ `(illustratif)` jetons par bras.
  * Pour l'ensemble des $4$ `(illustratif)` expériences (E0, E1, E2, E3, incluant les bras témoins et contrôles négatifs, soit $10$ `(illustratif)` bras au total) : $\approx 2,56 \times 10^8$ `(illustratif)` jetons générés.
  * Matériel : $4 \times$ GPU NVIDIA A100 (80 Go VRAM) `(illustratif)`. À un débit agrégé moyen (mélange de modèles 7B à 72B quantifiés en FP16/AWQ) de $4\,000$ `(illustratif)` jetons/seconde, le temps d'inférence total est d'environ $18$ `(illustratif)` heures-nœud (soit $72$ `(illustratif)` heures-GPU A100).
* **Projection fonctionnelle ($\phi$) et Contrôle indépendant ($V$ et $V^*$ sur CPU)** :
  * Exécution en bac à sable isolé (*sandbox* Linux namespaces / seccomp) du projecteur $\phi$ sur les $500\,000$ `(illustratif)` candidats générés (temps limité à $0,05$ `(illustratif)` seconde CPU par candidat) : $\approx 7$ `(illustratif)` heures sur un serveur de $64$ `(illustratif)` cœurs CPU.
  * Exécution du contrôle indépendant $V$ ($1,0$ `(illustratif)` seconde CPU par appel) et du solveur de vérité terrain $V^*$ ($10,0$ `(illustratif)` secondes CPU par appel sur les candidats confirmés) pour environ $50\,000$ `(illustratif)` appels à $V$ et $5\,000$ `(illustratif)` appels à $V^*$ : $\approx 28$ `(illustratif)` heures-CPU par cœur, soit moins de $1$ `(illustratif)` heure en parallèle sur $64$ `(illustratif)` cœurs.
* **Coût financier total estimé** :
  * Location cloud GPU ($72$ `(illustratif)` heures-GPU A100 à $2,00\text{ \$/h}$ `(illustratif)`) : $144\text{ \$}$ `(illustratif)`.
  * Location cloud CPU ($15$ `(illustratif)` heures d'instance $64$ `(illustratif)` cœurs à $2,50\text{ \$/h}$ `(illustratif)`) et stockage : $38\text{ \$}$ `(illustratif)`.
  * **Coût total de la campagne expérimentale** : $\approx 182\text{ \$}$ `(illustratif)` (marge de sécurité incluse : enveloppe de $250\text{ \$}$ `(illustratif)`).

FIN-DE-CELLULE
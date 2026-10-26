# Cellule C — Tour III.2 : Équipe rouge croisée contre A et B

**Vérification des pièces (Règle 2)** : La pièce C4 (mondes à ponts plantés de conv-audit) et le fichier détaillé de l'essai de la brique 1 (`5b7011b1…`) sont absents des faits transmis. Les pièces C1, C2, C3a, C3b, R-525, A et B sont présentes et intègres (statut : RAPPORTÉ). Tout développement ci-dessous est de statut HYPOTHÈSE, sauf mention explicite d'un fait RAPPORTÉ.

---

## Contre la proposition A

### (a) Les failles : variables confondantes, vérités par construction et fuites d'instruments

1. **Inapplicabilité du critère mécanique « prédit plus » hors des mondes jouets (vrai par construction sur le jouet, aveugle sur le réel)** :
   En E3, A définit le gain empirique ainsi : *« la fille "prédit plus" si elle est définie et correcte sur ≥ 1 instance où aucun parent ne prédit »*, mesuré par *« comparaison d'ensembles d'instances, zéro appel de modèle »*.
   - **La faille** : Sur de la littérature réelle (résumés OpenAlex ou arXiv, RAPPORTÉ), un article ne fournit pas une base de données tabulaire d'« instances » sur laquelle exécuter un `set.difference()` en Python. Le critère mécanique de A n'est exécutable que parce que le monde synthétique de E3 est codé *exprès* avec des instances discrètes. Dès que la v0 recommandée par A (Q5, point 4) touche un vrai texte, ce rejet mécanique devient inopérant ou requiert qu'un modèle de langue traduise le texte en instances formelles — réintroduisant l'appel de modèle et le risque d'hallucination que le critère prétendait éliminer.

2. **Fuite circulaire entre le générateur de l'extracteur et la grille de tirage (E1 / Q5)** :
   A recommande pour la v0 une *« grille domaine × opérateur alimentée par un extracteur mesuré »* sur *« 100 résumés étiquetés à la main (4 h humaines, illustratif) »*.
   - **La faille** : En 100 résumés (soit 2 à 5 résumés par opérateur si l'on reprend les 25 opérateurs de la caste 1, RAPPORTÉ), l'annotateur humain définit une taxonomie fermée et rigide. Si ce même jeu de 100 résumés sert à construire les règles de l'extracteur (motifs ou classifieur) et à définir les cases de la grille de stratification en E1, le tirage stratifié gagne *par construction* contre le DPP continu : on évalue la stratification sur les étiquettes exactes produites par l'extracteur qui définit les strates. La variable confondante est la discrétisation forcée de l'espace des domaines.

3. **Biais de sélection et fuite topologique dans la rétrodiction (E4)** :
   A définit les paires positives d'OpenAlex comme des concepts de niveau 1–2 *« sans co-occurrence d'auteur ni co-citation avant $t_0$, avec ≥ 20 articles joints entre $t_0$ et $t_0 + 3$ ans »*, comparées à 50 paires « jumelles » appariées en taille et croissance.
   - **La faille (variable confondante)** : Deux concepts qui passent de 0 à ≥ 20 articles joints en 3 ans ne fusionnent presque jamais par bisociation pure à distance infinie ; ils sont à distance 2 dans le graphe de citations avant $t_0$ (voisins communs très actifs, ou partage d'un troisième concept $B$ en forte croissance). A n'apparie les jumelles que sur la *taille* et la *croissance marginale* des nœuds, pas sur leur **distance de graphe (chemins de longueur 2)** avant $t_0$. Le pipeline de A battra le nul stratifié sur les paires positives simplement parce que le filtre d'opérateur capte la proximité topologique latente à 2 sauts, confondant prédiction de lien standard et bisociation.
   - **La faille de la sonde de fuite** : A propose d'interroger le modèle *« à froid sur la paire : cite-t-il le pont réalisé ? Toute paire citée est exclue »*. C'est une sonde de mémorisation *explicite* (rappel libre). Un modèle de langue dont la coupure est postérieure à $t_0$ peut échouer à citer l'article exact à froid (faux négatif de la sonde), tout en attribuant une log-probabilité élevée aux jetons du pont lorsqu'on lui fournit les résumés en contexte lors de la fusion. La fuite implicite survit intégralement.

4. **Confusion dans E2 entre erreurs de tirage et erreurs de représentation** :
   En E2, A fait varier simultanément le bruit d'étiquette $\epsilon$, la séparation de domaine $s$, la part de hubs $h$ et la taille $n$. Mais le noyau corrigé de C3b utilise un vecteur continu $d_i \in \mathbb{S}^{15}$ pour le domaine et une étiquette discrète pour l'opérateur (c5, RAPPORTÉ). Si le « bisoc vrai » s'effondre en E2, le protocole de A ne permet pas d'isoler si la falaise vient de la géométrie de $S_{ij} = \langle d_i, d_j \rangle^2$ ou du forçage glouton de la paire après tirage.

---

### (b) Scénarios d'évasion : comment un agent adverse trompe les instruments de A

1. **Contre la consigne de fusion à 4 champs et le critère « prédit plus » (E3) — *L'Attaque par Restriction de Domaine (Piecewise Splice)*** :
   - *Mécanisme* : Le parent $A$ prédit $Y = f(X)$ sur le domaine $D_A$. Le parent $B$ prédit $Z = g(W)$ sur $D_B$. L'agent adverse génère une hypothèse fille qui déclare l'opérateur partagé $O$ (ex. « optimisation convexe »), recopie les préconditions, et énonce la loi hybride : « Pour une instance mixte $(X, W)$ soumise à un couplage $\lambda > \lambda_{\text{crit}}$, l'observable conjointe vaut $P = f(X) + g(W) + \epsilon$ ».
   - *Pourquoi l'instrument est trompé* : Les 4 champs syntaxiques de A sont remplis (0 rejet mécanique). Sur l'instance $(X, W)$ où $\lambda > \lambda_{\text{crit}}$, ni $A$ seul (qui ne connaît pas $W$) ni $B$ seul (qui ne connaît pas $X$) n'est défini. L'ensemble des instances de la fille dépasse strictement l'union des parents : le vérificateur mécanique de A classe la fille comme « prédit plus ». Or, scientifiquement, c'est une juxtaposition additive triviale sans aucune interaction structurelle.
   - *Coût pour l'agent* : **0 appel supplémentaire**, 15 lignes de gabarit dans le prompt, **0 USD**.

2. **Contre l'extracteur d'opérateurs et la grille de stratification — *L'Attaque par Camouflage Taxonomique*** :
   - *Mécanisme* : L'extracteur de A est calibré pour rejeter les « hubs » génériques (*matrix*, *bound*) et récompenser 25 à 50 opérateurs précis (*martingale*, *sheaf*, *symplectic*, cf. C1 RAPPORTÉ). L'agent adverse (ou un générateur amont optimisant son taux de survie, cf. Goodhart en R-525) réécrit n'importe quelle régularité banale (ex. une moyenne mobile ou une descente de gradient standard) en utilisant le lexique exact d'un opérateur rare de la grille : *« filtration de martingale discrète à incréments bornés »* ou *« flot symplectique dégénéré »*.
   - *Pourquoi l'instrument est trompé* : La case `(Domaine_X, martingale)` de la grille qualité-diversité étant vide, le tirage stratifié de A sélectionne cet candidat avec une probabilité proche de 1. Le taux de fausses alertes sur les hubs est maintenu à 0 %, mais l'opérateur extrait est un artefact purement verbal.
   - *Coût pour l'agent* : Une table de synonymes mathématisés (dictionnaire statique en Python), **0 USD**.

3. **Contre le filtre de compatibilité des contraintes — *L'Attaque par Conjonction d'Exemption (Régime Dual)*** :
   - *Mécanisme* : Le filtre de C3b (repris par A) rejette une paire si un texte porte le marqueur $+$ (ex. *linéaire*) et l'autre le marqueur $-$ (*non-linéaire*), mais **ignore** les textes qui portent les deux marqueurs (« $\pm$ », non comptés pour éviter les faux positifs sur les comparaisons, C3b §3 RAPPORTÉ). L'agent adverse insère systématiquement dans ses résumés une clause standard : *« Contrairement aux régimes non-linéaires transitoires discrets, notre opérateur linéaire stationnaire continu… »*.
   - *Pourquoi l'instrument est trompé* : Le texte reçoit l'étiquette $\pm$ sur tous les axes du filtre. Sa contradiction avec n'importe quel autre parent tombe mécaniquement à **0 %**. Toutes les fusions incompatibles passent.
   - *Coût pour l'agent* : 12 jetons ajoutés par résumé, **0 USD**.

4. **Évasion simultanée de tous les instruments de A** :
   En combinant la clause $\pm$ (neutralise le filtre), le synonyme d'opérateur rare (neutralise l'extracteur et pirate la stratification), et le raccord par morceaux sur une variable muette $\lambda$ (neutralise la consigne E3 et le test d'ensembles d'instances), un script Python déterministe sans aucune compréhension sémantique obtient 100 % de survie mécanique dans la v0 de A pour un coût de **0 USD** et **0 appel de modèle**.

---

### (c) Les contrôles négatifs dont l'absence est fatale à A

1. **Contrôle négatif d'additivité indépendante (fatal pour E3 et le critère « prédit plus »)** :
   Créer un bras témoin mécanique qui prend deux parents $A(x)$ et $B(y)$ sur des variables disjointes et construit mécaniquement le produit cartésien $F(x, y) = A(x) \times B(y)$ sur le domaine joint $D_A \times D_B$. Si le critère mécanique de A (« défini et correct sur ≥ 1 instance où aucun parent ne prédit ») valide ce produit cartésien trivial, le critère de contenu empirique de A est falsifié.

2. **Contrôle négatif d'appariement topologique à 2 sauts (fatal pour E4)** :
   En rétrodiction OpenAlex, imposer que les 50 paires « jumelles » (négatives) aient exactement le **même nombre de voisins communs (chemins $A \leftrightarrow B \leftrightarrow C$) et le même score d'attachement préférentiel** avant $t_0$ que les 50 paires positives. Sans ce contrôle, H_A en E4 est indiscernable d'un prédicteur de liens topologique trivial.

3. **Contrôle négatif d'aveuglement lexical du fuseur (fatal pour la sonde de fuite de E4)** :
   Remplacer dans les résumés soumis au fuseur tous les noms propres de concepts et de domaines par des identifiants anonymes (`CONCEPT_42`, `SYSTEME_7`) en ne laissant en clair que les verbes et opérateurs mathématiques. Si le Hit@10 de A s'effondre après anonymisation alors que la sonde à froid n'avait rien détecté, c'est la preuve que la sonde de fuite de A a laissé passer la contamination mémorielle du modèle de langue.

---

## Contre la proposition B

### (a) Les failles : variables confondantes, vérités par construction et fuites d'instruments

1. **Le bras « transfert mécanique » en E0 est un oracle déguisé qui court-circuite le problème réel (vrai par construction)** :
   En E0, B construit un monde planté où chaque parent est un texte accompagné d'un *« générateur de données »* issu de 6 à 8 lois paramétriques latentes (exponentielle, logistique, oscillateur amorti…), où A décrit le régime court et B l'asymptote. Puis B introduit le Bras 2 : *« transfert mécanique : ajuster la forme fonctionnelle de B sur les données de A, sans modèle »*, et décrète que si le modèle de langue (Bras 1) ne bat pas le Bras 2, *« le modèle de langue est décoratif »*.
   - **La faille** : Pour « ajuster la forme fonctionnelle de B sur les données de A sans modèle », le script du Bras 2 doit déjà disposer : (i) de l'équation analytique exacte de B en code Python, et (ii) du dictionnaire exact reliant la colonne de données de B à la colonne de données de A. Mais dans un article scientifique réel, **cette traduction entre les variables du texte B et celles du texte A est précisément le problème de la fusion** ! Sur le monde planté de B, où il n'y a qu'une variable $t$ et une observable $y(t)$, l'alignement des variables est trivial (identité 1D) et l'ajustement par moindres carrés (`scipy.optimize.curve_fit`) réussira à 100 % *par construction*. Le Bras 1 (modèle de langue qui lit du texte) est pénalisé par le goulot de lecture textuelle que le Bras 2 contourne par accès direct aux tableaux numériques. Le duel E0 est truqué en faveur du Bras 2 sur le jouet, alors que le Bras 2 est **inexécutable** sur des articles réels dépourvus de générateurs numériques 1D alignés.

2. **Fuite de l'instrument de détection dans l'évaluation en E2 (isomorphisme de graphes extraits par LLM)** :
   En E2, B veut prouver que l'appariement structurel (Gentner) bat le lexique sur des homonymes. Sa procédure : *« Les relations sont extraites par un modèle de langue en graphe typé, puis l'isomorphisme est vérifié mécaniquement »*.
   - **La faille (variable confondante et fuite)** : Comment le modèle de langue extrait-il un « graphe typé » à partir d'un résumé ? En lisant les mots du résumé et en projetant ses propres priors sémantiques dans les étiquettes d'arêtes ! Si deux textes parlent de deux domaines différents mais que le LLM devine qu'ils relèvent tous deux d'une « relaxation exponentielle », il va normaliser les deux graphes avec les mêmes types de relations canoniques. À l'inverse, s'il échoue à comprendre l'analogie, il produira deux graphes non isomorphes. L'étape « vérification mécanique d'isomorphisme » en aval ne mesure donc pas une propriété intrinsèque du texte : elle mesure la capacité du LLM extracteur à résoudre l'analogie en amont. Pire : si la même famille de LLM génère les paires homonymes/jumeaux du banc E2 et extrait les graphes typés, l'isomorphisme réussira *par construction* (fuite générateur/extracteur).

3. **Le critère mécanique de bijection de types (section c) est tautologique sans vérificateur d'unités externe** :
   B rejette une fille si *« la table de correspondance n'est pas bijective ou viole les types, ce qui se vérifie sans modèle »*.
   - **La faille** : Qui assigne les types aux variables dans le gabarit à 4 champs ? **Le modèle de langue qui génère la fille lui-même !** Vérifier mécaniquement en Python que `len(set(vars_A)) == len(set(vars_B))` et que la colonne `type_A` déclarée par le LLM est égale à la colonne `type_B` déclarée par le même LLM à la même ligne ne teste absolument pas la vérité physique du pont : cela teste uniquement que le LLM sait recopier la chaîne de caractères `"scalaire_positif"` deux fois sur la même ligne.

4. **Illusion de la décontamination par OLMo en rétrodiction (E3)** :
   B note qu'en E3 on pourrait utiliser OLMo (corpus Dolma documenté) pour *« chercher les liens cibles dans le corpus d'entraînement et exclure les paires contaminées »*.
   - **La faille** : Si la coupure temporelle de l'expérience est $T_0 = 2018$ et qu'OLMo est entraîné jusqu'en 2024, les concepts reliés entre 2018 et 2024 ne sont pas seulement présents sous forme de co-occurrences explicites de la paire $(A, C)$ dans Dolma : ils ont modifié les représentations vectorielles de *tous* les termes intermédiaires $B_1, B_2, \dots$ apparus après 2018. Purger les documents contenant $(A \text{ et } C)$ laisse intacte la chaîne de co-occurrences indirectes post-$T_0$ dans les poids du modèle.

---

### (b) Scénarios d'évasion : comment un agent adverse trompe les instruments de B

1. **Contre la table de correspondance bijective et le contrôle d'isomorphisme (E2 & Critère i) — *L'Attaque par Adimensionnement Universel*** :
   - *Mécanisme* : Pour passer le contrôle mécanique de bijection des types et d'isomorphisme relationnel sur n'importe quelle paire d'articles incompatibles (un anti-oracle), l'agent adverse adimensionne systématiquement 3 variables arbitraires de $A$ et 3 variables de $B$ en les divisant par leurs valeurs caractéristiques respectives, les renomme $(\tilde{x}_1, \tilde{x}_2, \tilde{x}_3) \in \mathbb{R}^+$, et produit le graphe relationnel canonique : $\tilde{x}_1 \xrightarrow{\text{contrôle}} \tilde{x}_2 \xrightarrow{\text{inhibe}} \tilde{x}_3$.
   - *Pourquoi l'instrument est trompé* : La table de correspondance est strictement bijective (3 pour 3), tous les types sont identiques (`float_sans_dimension`), et les deux graphes extraits à 3 nœuds et 2 arêtes orientées sont **strictement isomorphes** au sens de Gentner / SME. Le vérificateur mécanique de B valide 100 % des chimères.
   - *Coût pour l'agent* : Prompt système fixe demandant de toujours extraire une chaîne causale de longueur 3 adimensionnée. **0 USD**, **0 appel supplémentaire**.

2. **Contre le test de non-déductibilité parentale et le gain sur la conjonction (E0 & Critères ii–iii) — *L'Attaque par Interpolation Barycentrique (Stein-like Shrinkage)*** :
   - *Mécanisme* : Le critère (ii) de B rejette la fille si sa prédiction est déductible de $A$ seul ou de $B$ seul ; le critère (iii) exige qu'elle batte la conjonction littérale « $A ; B$ » de plus de $2\delta_0$ sur données fraîches. Dans le monde de B, $A$ prédit bien à $t$ petit mais diverge à $t \to \infty$ (ex. approximation linéaire $y_A(t) = a t$), tandis que $B$ fournit une borne asymptotique $y_B(t) = M$. La « conjonction littérale » soumise à l'évaluateur est ambiguë (deux équations contradictoires à grand $t$). L'agent adverse ne cherche aucun pont : il génère mécaniquement l'enveloppe régularisée $y_{\text{fille}}(t) = (y_A(t)^{-p} + y_B(t)^{-p})^{-1/p}$ (ou une combinaison convexe dépendante du temps $\alpha(t) y_A + (1-\alpha(t)) y_B$).
   - *Pourquoi l'instrument est trompé* :
     1. $y_{\text{fille}}$ n'est déductible ni de $A$ seul ni de $B$ seul (passe le critère ii).
     2. Sur données fraîches pour toute loi monotone saturante (logistique, exponentielle inverse, diffusion bornée — soit la majorité des 6–8 lois de B), cet estimateur composite bat l'extrapolation divergente de $A$ seul et bat la conjonction non résolue de plus de $2\delta_0$ par simple réduction de variance (effet d'ensemble), **même lorsque A et B obéissent à des lois latentes différentes (anti-oracle monotone)** !
   - *Coût pour l'agent* : **0 appel de modèle**, une formule algébrique fixe d'interpolation harmonique, **0 USD**.

3. **Contre la pondération de rareté de fond `b+` et la règle d'abstention — *L'Attaque par Injection de Jargon Rare Partagé*** :
   - *Mécanisme* : B impose une abstention obligatoire si aucun opérateur rare (fréquence de fond $\le 0,1$ dans l'archive de 300 textes, RAPPORTÉ) ne relie les tirages. L'agent adverse choisit un mot composé absent ou ultra-rare dans le corpus de fond (ex. `wasserstein_proximal` ou un token d'opérateur sous-représenté dans les 25 motifs) et l'insère dans une phrase méthodologique creuse de ses hypothèses candidates.
   - *Pourquoi l'instrument est trompé* : La fréquence de fond étant $\le 0,1$, `b+` exempte ce jeton de toute répulsion (rétention 1,00, RAPPORTÉ), lui attribue le poids maximal de rareté, annule le taux d'abstention et force l'appariement des paires choisies par l'adversaire.
   - *Coût pour l'agent* : Lecture d'une table de fréquences du corpus de fond (calcul processeur en $O(N)$), **0 USD**.

4. **Évasion simultanée de tous les instruments de B** :
   Sur toute paire tirée, l'agent injecte un jeton rare sous le seuil de 0,1 (contourne `b+` et l'abstention), extrait un graphe linéaire adimensionné à 3 nœuds (passe l'isomorphisme E2 et la bijection des types i), et émet une combinaison harmonique des prédictions des parents (passe la non-déductibilité ii et bat la conjonction iii sur toute fonction monotone bornée). Coût total : **0 USD** de calcul additionnel.

---

### (c) Les contrôles négatifs dont l'absence est fatale à B

1. **Contrôle négatif d'« Ensemble Aveugle » (fatal pour E0 et le critère iii)** :
   Ajouter en E0 un Bras 6 (« Moyenne / Enveloppe harmonique aveugle ») qui combine algébriquement les prédictions numériques de $A$ et $B$ sans lire leurs textes ni chercher de correspondance de variables. Si le Bras 1 (modèle de langue) ou le Bras 2 (transfert mécanique) ne bat pas ce Bras 6 de plus de $2\delta_0$, alors E0 ne mesure pas une synthèse bisociative, mais un banal gain de régularisation par moyennage de modèles (*model averaging*).

2. **Contrôle négatif d'« Extraction Aveugle aux Paraphrases Syntaxiques » (fatal pour E2)** :
   En E2, B contrôle les graphes permutés, mais ne contrôle pas le biais du LLM extracteur. Contrôle requis : prendre deux textes du **même** domaine décrivant deux lois physiques **incompatibles** (ex. loi d'Ohm linéaire et claquage d'avalanche exponentiel), mais rédigés avec la **même structure syntaxique de phrase** (ex. *« Le flux X croît avec le gradient Y jusqu'au régime Z contrôlé par le paramètre $\tau$ »*). Si l'extracteur LLM produit deux graphes typés isomorphes parce que la grammaire de surface est identique, l'instrument d'appariement structurel de B ne lit que la syntaxe de surface et échoue sur sa propre validité de construit.

3. **Contrôle négatif de « Désalignement Dimensionnel » (fatal pour le Bras 2 de E0 et le critère i)** :
   Dans le monde planté de E0, appliquer aux données numériques du parent $B$ une transformation inconnue mais physique (changement d'échelle non linéaire des axes, permutation de l'ordre des colonnes des variables d'état, ajout d'une variable d'état muette) documentée *uniquement en toutes lettres dans le texte de B*. Si le Bras 2 (« transfert mécanique sans modèle ») s'effondre alors que la loi latente est identique, cela prouve que le succès du Bras 2 en E0 dépendait d'un alignement de colonnes fourni par un oracle caché.

4. **Contrôle négatif d'homonymie temporelle en rétrodiction (fatal pour E3)** :
   En E3, B vérifie les liens sur OpenAlex dans le tertile éloigné, mais n'exclut pas la **dérive sémantique des étiquettes d'opérateurs** entre $T_0$ et $T_0 + \Delta$ (ex. le mot `"diffusion"` qui désigne le mouvement brownien en physique avant 2020, puis les modèles génératifs d'images en informatique après 2021). Contrôle requis : mesurer la stabilité du voisinage local de l'opérateur-pont $B$ à l'intérieur de chaque domaine entre $T_0$ et $T_0 + \Delta$. Sans rejet des opérateurs dont le sens a bifurqué après $T_0$, E3 compte les modes terminologiques inter-disciplinaires comme des ponts bisociatifs vrais.

FIN-DE-CELLULE
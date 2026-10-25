# Proposition C — Tour III.1 : Déconfondre l'espace d'action et l'algorithme d'apprentissage dans la conception d'organismes

*Note liminaire : Conformément à la règle 2, le bloc `FAITS` est déclaré vide de données empiriques par décision de l'arbitre (RAPPORTÉ). L'intégralité des grandeurs numériques et coûts ci-dessous est donc marquée « illustratif ». Conformément à la règle 6, la structure suit le livrable exigé par le système (`a`, `b`, `c`, `d`), tout en traitant exhaustivement les quatre points analytiques soumis dans la donnée `QUESTION DE L'ARBITRE`.*

---

## (a) Ce que la question suppose sans que ce soit établi, et formalisation du problème (Point 1 de l'arbitre)

Soit $\Sigma^*$ l'ensemble de toutes les chaînes de caractères finies (sortie libre), $\mathcal{V} \subset \Sigma^*$ le sous-ensemble des organismes syntaxiquement et mécaniquement exécutables sous le noyau fixe, et $L(G) \subset \Sigma^*$ le langage formel engendré par la grammaire ou le schéma $G$. Soit $\Phi : \mathcal{V} \to \mathcal{S}$ la fonction d'interprétation qui projette un code valide vers sa sémantique opérationnelle (topologie du graphe d'agents, mécanismes de routage, structure de mémoire). Le score sur les familles de tâches tenues à l'écart est une fonction de récompense $R : \mathcal{S} \to [0, 1]$.

### Les présupposés non établis de la question

1. **Inclusion stricte de la couverture fonctionnelle ($\Phi(L(G) \cap \mathcal{V}) \subsetneq \Phi(\mathcal{V})$)** — **HYPOTHÈSE**.
   La question suppose que contraindre la syntaxe par $G$ ampute l'expressivité sémantique $\mathcal{S}$. Or, si $G$ est la grammaire d'un langage Turing-complet ou d'un langage de diffs universel, $\Phi(L(G) \cap \mathcal{V}) = \Phi(\mathcal{V})$. L'inclusion n'est stricte que si $G$ est un schéma déclaratif rigide (ex. : un JSON fixant un graphe acyclique dirigé à profondeur bornée).
2. **Nécessité de la contrainte $G$ pour que le gradient ait prise chez le concepteur entraîné (E)** — **HYPOTHÈSE**.
   La question suppose qu'en sortie libre $\Sigma^*$, la proportion d'organismes valides produite par le modèle ouvert initial $\pi_{\theta_0}$ est si basse ($\mathbb{P}_{x \sim \pi_{\theta_0}}(x \in \mathcal{V}) \ll 1$) que la variance de l'estimateur de gradient (type REINFORCE ou PPO) empêche la convergence à budget fixe.
3. **Neutralité ou avantage de la sortie libre pour le concepteur figé (F)** — **HYPOTHÈSE**.
   Il est supposé que (F) exploite avantageusement l'espace $\Sigma^* \setminus L(G)$. Or, l'absence de contrainte expose aussi (F) à des erreurs de syntaxe ou d'interfaçage, réduisant son rendement par unité de coût.
4. **Additivité des effets du format et de l'apprentissage** — **HYPOTHÈSE**.
   Séparer « format » et « apprentissage » suppose implicitement qu'il n'y a pas d'interaction croisée destructive (par exemple, qu'une grammaire $G$ optimale pour guider l'exploration par renforcement de (E) ne dégrade pas les performances de (F) par désalignement avec sa distribution de pré-entraînement).

### En quoi la contrainte de format change l'espace de recherche et explique l'écart à elle seule

Si $G$ est un schéma restrictif (ex. : schéma JSON imposant des rôles prédéfinis, un graphe de communication statique et un tampon de mémoire clé-valeur fixe), la projection $\Phi(L(G))$ interdit :
* **Topologies inaccessibles** : les graphes d'appel dynamiques (récursion dépendante des données, création d'agents à la volée, boucles conditionnelles non bornées).
* **Mécanismes et instruments inaccessibles** : la métaprogrammation (un agent écrivant et exécutant un sous-script d'analyse ad hoc), la redéfinition des opérateurs d'agrégation (remplacer un vote majoritaire par un solveur SAT externe ou un script Python d'optimisation).
* **Mémoire non représentable** : le passage d'une mémoire textuelle plate à une structure de données relationnelle, un arbre de recherche (MCTS) ou un index vectoriel construit à la volée dans le système de fichiers de l'organisme.

**Double explication de l'écart par le seul format (confondant l'apprentissage) :**
* *Biais en faveur de (E) sans apprentissage réel (Effet d'échafaudage)* : Si le concepteur de $G$ a encodé dans le schéma de fortes connaissances a priori (une architecture d'agent déjà performante dont seuls quelques hyperparamètres discrets varient) et garantit $\mathbb{P}(x \in \mathcal{V} \mid x \in L(G)) = 1$ (hypothèse), alors une politique aléatoire ou faiblement entraînée sur $L(G)$ battra un concepteur (F) en sortie libre qui gaspillerait $40\%$ (illustratif) de son budget à produire du code non exécutable ($x \notin \mathcal{V}$).
* *Biais en faveur de (F) malgré un apprentissage réussi de (E) (Effet de plafond de verre)* : Si une famille de tâches tenue à l'écart exige un mécanisme hors de $\Phi(L(G))$ (ex. : maintenir un état d'exécution sous forme de graphe orienté en mémoire vive), alors $\max_{s \in \Phi(L(G))} R(s) < \mathbb{E}_{x \sim \pi_F(\Sigma^*)}[R(\Phi(x))]$. Même si l'entraînement amène (E) à l'optimum global de son sous-espace, il restera inférieur à (F) à cause de la borne supérieure de $L(G)$.

---

## (b) Les voies possibles (Point 2) et les expériences décisives (Point 3)

### Analyse des voies d'action : coûts et pertes (Point 2 de l'arbitre)

Aucune voie n'est exempte de compromis. Voici les six voies structurantes :

1. **Voie 1 : Alignement par le bas (imposer la grammaire $G$ à F et E)**
   * *Mécanisme* : Forcer (F) à générer dans $L(G)$ (par décodage contraint si l'API le permet, ou par échantillonnage avec rejet).
   * *Ce qu'elle coûte* : Surcoût de jetons pour le rejet si l'API de (F) est une boîte noire sans masquage de logits ; biais de distorsion de la distribution native de (F) (*token healing* et altération des probabilités conditionnelles — référence à vérifier : Park et al., 2024, *Grammar-Aligned Decoding*, ou équivalent à vérifier).
   * *Ce qu'elle perd* : Élimine l'avantage d'expressivité de (F). Si (F) est bridé par $G$, on mesure la capacité de (F) à remplir un formulaire, pas à concevoir un organisme.
2. **Voie 2 : Alignement par le haut (sortie libre $\Sigma^*$ pour E, avec validation et boucle de réparation)**
   * *Mécanisme* : (E) génère librement du code ; un vérificateur mécanique (compilateur/noyau) teste $x \in \mathcal{V}$. Si $x \notin \mathcal{V}$, le message d'erreur est réinjecté pour $K$ tentatives de réparation, ou une récompense nulle/pénalité est assignée.
   * *Ce qu'elle coûte* : Taux d'organismes invalides potentiellement massif en début d'entraînement (ex. : $70\%$ à $95\%$ d'échecs initiaux, illustratif), consommant le budget de calcul en essais-erreurs syntaxiques plutôt qu'en exploration fonctionnelle.
   * *Ce qu'elle perd* : Efficacité d'échantillonnage du RL. Le gradient est dilué sur la syntaxe au lieu de porter sur l'architecture de l'organisme.
3. **Voie 3 : Grammaire induite par corpus ($G_{\text{ind}}$ couvrant la pratique de F)**
   * *Mécanisme* : Générer un corpus $C_F = \{x_1, \dots, x_N\}$ de sorties libres valides de (F) sur les tâches d'entraînement. Extraire les arbres syntaxiques abstraits (AST) et les patrons d'architecture pour induire une grammaire hors-contexte $G_{\text{ind}}$ telle que le taux de couverture $\hat{\kappa} = \frac{1}{|C_F^{\text{test}}|} \sum_{x \in C_F^{\text{test}}} \mathbb{I}(x \in L(G_{\text{ind}})) \ge 1 - \epsilon$ (ex. : $95\%$, illustratif) sur un échantillon de validation de (F).
   * *Ce qu'elle coûte* : Coût initial d'échantillonnage de (F) (qui doit être comptabilisé ou explicitement séparé du budget de comparaison) et ingénierie d'induction grammaticale.
   * *Ce qu'elle perd* : Toute innovation structurelle hors-distribution que (F) ou (E) aurait pu produire sur de nouvelles familles de tâches mais qui n'était pas présente dans $C_F$ (sur-apprentissage de l'espace de conception sur les tâches d'entraînement).
4. **Voie 4 : Espace d'action par édition différentielle (Diffs / Patchs AST sur un organisme germe $O_0$)**
   * *Mécanisme* : L'espace d'action des deux concepteurs est restreint à des opérations d'édition structurées (blocs `SEARCH/REPLACE` ou transformations d'AST) appliquées séquentiellement à partir d'un même organisme minimal valide $O_0 \in \mathcal{V}$.
   * *Ce qu'elle coûte* : Dépendance au chemin (*path dependence*). Atteindre une topologie éloignée de $O_0$ demande de multiples générations réussies.
   * *Ce qu'elle perd* : La capacité de refonte globale en un coup (*clean-slate design*) où (F) excelle potentiellement en sortie libre. En revanche, elle unifie l'espace d'expressivité (tout code dans $\mathcal{V}$ est atteignable par une séquence finie de diffs) tout en gardant des actions courtes et faciles à valider pour le RL de (E).
5. **Voie 5 : Plan factoriel à bras de contrôle (séparation statistique sans forcer un choix unique)**
   * *Mécanisme* : Maintenir (F) en sortie libre et (E) en sortie contrainte, mais ajouter les bras croisés pour isoler algébriquement l'effet du format et l'effet de l'apprentissage (détaillé en Expérience 1 ci-dessous).
   * *Ce qu'elle coûte* : Multiplication du budget expérimental par $2$ à $3$ (illustratif) pour maintenir la puissance statistique sur chaque bras.
   * *Ce qu'elle perd* : Rien en expressivité propre à chaque bras, mais réduit le budget allouable par bras si l'enveloppe matérielle totale est fixe.
6. **Voie 6 : Compilation en deux étages (Spécification libre $\to$ Traducteur figé contraint)**
   * *Mécanisme* : (E) et (F) produisent tous deux un plan architectural en langage naturel ou pseudo-code libre ; un même module de traduction figé (un LLM codeur sous contrainte grammaticale $G$ ou vérificateur AST) compile ce plan en organisme exécutable.
   * *Ce qu'elle coûte* : Coût d'inférence du traducteur à chaque génération ; goulet d'étranglement informationnel dans le traducteur.
   * *Ce qu'elle perd* : La capacité des concepteurs à optimiser directement les détails d'implémentation de bas niveau du code de l'organisme.

---

### Expériences décisives en inférence forte (Règle B4 & Point 3 de l'arbitre)

#### Expérience 1 : Décomposition factorielle $2 \times 3$ (Séparer « Format » et « Apprentissage »)

Pour isoler l'apprentissage du format, quatre bras ne suffisent pas si le modèle de base de (E) diffère de (F) : il faut dissocier (i) le modèle de base, (ii) le format, et (iii) la mise à jour des poids par RL. Soit un plan à 6 bras évalués sur $M = 10$ (illustratif) familles de tâches tenues à l'écart, avec $n = 30$ (illustratif) graines d'exécution indépendantes par bras à budget de calcul total apparié :
* $F_{\text{libre}}$ : Concepteur figé (frontière), sortie libre $\Sigma^*$.
* $F_{G}$ : Concepteur figé (frontière), contraint à la grammaire $G$.
* $E_{0, \text{libre}}$ : Modèle ouvert (taille moyenne) **non entraîné** ($\theta_0$), sortie libre $\Sigma^*$ (échantillonnage Best-of-$N$ à budget égal).
* $E_{0, G}$ : Modèle ouvert **non entraîné** ($\theta_0$), contraint à $G$ (Best-of-$N$ à budget égal).
* $E_{\text{RL}, \text{libre}}$ : Modèle ouvert **entraîné par RL** ($\theta_{\text{RL}}$), sortie libre $\Sigma^*$ avec validation ex post.
* $E_{\text{RL}, G}$ : Modèle ouvert **entraîné par RL** ($\theta_{\text{RL}}$), contraint à $G$.

On définit les scores moyens sur familles tenues à l'écart $\mu(\cdot)$, l'effet d'apprentissage sous contrainte $\Delta_{\text{RL}|G} = \mu(E_{\text{RL}, G}) - \mu(E_{0, G})$, l'effet intrinsèque du format sur le modèle figé $\Delta_{\text{fmt}|F} = \mu(F_{G}) - \mu(F_{\text{libre}})$, et l'effet du format sur le modèle ouvert initial $\Delta_{\text{fmt}|E_0} = \mu(E_{0, G}) - \mu(E_{0, \text{libre}})$.

* **Hypothèse $H_A$ (Artefact d'échafaudage grammatical)** : L'avantage observé ou la compétitivité de $E_{\text{RL}, G}$ face à $F_{\text{libre}}$ provient de la réduction de l'espace de recherche par la grammaire $G$ (qui élimine les organismes invalides et encode une bonne structure a priori), et non de l'optimisation des poids par RL.
* **Hypothèse $H_B$ (Gain d'apprentissage authentique)** : L'entraînement par renforcement découvre dans $L(G)$ des structures d'organismes que ni l'échantillonnage aléatoire guidé par $G$, ni le modèle de frontière soumis à $G$ ne sélectionnent, et ce gain surpasse toute perte d'expressivité due à $G$.
* **Métriques** :
  1. Exactitude moyenne $\mu$ sur les familles de tâches tenues à l'écart.
  2. Taux de validité syntaxique et opérationnelle $\tau_{\text{val}} = \mathbb{P}(x \in \mathcal{V})$.
  3. Diversité structurelle : entropie de la distribution des sous-arbres AST (ou distance d'édition d'arbre de Zhang-Shasha moyenne entre organismes générés).
* **Seuil et règle de décision (illustratif)** : Test par permutation hiérarchique (bootstrap par graine et par famille de tâches) au seuil $\alpha = 0.01$ (illustratif), avec une marge d'équivalence pratique $\delta = 0.03$ (3 points d'exactitude, illustratif).
* **Contrôle négatif** : Bras $R_G$ (générateur aléatoire uniforme dérivant les règles de production de la grammaire $G$ sans aucun modèle de langue, sélectionnant le meilleur organisme sur les tâches d'entraînement à budget d'évaluation égal). Si $\mu(E_{0, G}) - \mu(R_G) < \delta$, la grammaire $G$ fait tout le travail de conception.
* **Issues falsificatrices** :
  * *Falsification de $H_B$* : Si $\Delta_{\text{RL}|G} \le \delta$ **et** $\Delta_{\text{fmt}|E_0} > 2\delta$ (le passage au format $G$ fait bondir le modèle non entraîné, mais le RL n'ajoute rien), ou si $\mu(F_G) \ge \mu(E_{\text{RL}, G})$ alors que $\mu(F_{\text{libre}}) < \mu(E_{\text{RL}, G})$ (montrant que $F$ bat $E$ dès qu'on lui donne le même échafaudage $G$).
  * *Falsification de $H_A$* : Si $\Delta_{\text{RL}|G} > 2\delta$ **et** $\mu(E_{\text{RL}, G}) - \mu(F_G) > \delta$, démontrant que le gain réside dans la mise à jour des paramètres $\theta_0 \to \theta_{\text{RL}}$ à espace de sortie identique. De plus, si $\Delta_{\text{fmt}|F} < -\delta$ (la grammaire $G$ ampute effectivement la performance de $F$), l'inéquité de la comparaison naïve $F_{\text{libre}}$ vs $E_{\text{RL}, G}$ est prouvée par le plafond de verre.

#### Expérience 2 : Départage des voies d'égalisation d'espace (Grammaire induite $G_{\text{ind}}$ vs Édition par Diffs vs Sortie libre réparée)

* **Hypothèse $H_A$ (Supériorité de la contrainte grammaticale induite $G_{\text{ind}}$)** : Pour un modèle ouvert de taille moyenne entraîné par RL, le masquage de logits par une grammaire $G_{\text{ind}}$ (construite pour couvrir $95\%$ (illustratif) des sorties de $F_{\text{libre}}$) est indispensable pour stabiliser le gradient ; en sortie libre ou par diffs sans grammaire stricte, le taux d'invalidité effondre le rendement du RL.
* **Hypothèse $H_B$ (Supériorité de l'espace de Diffs universel sur $O_0$)** : La grammaire induite $G_{\text{ind}}$ souffre d'un défaut de généralisation hors-distribution sur les familles de tâches tenues à l'écart (bloquant l'invention de nouveaux mécanismes), tandis que l'action par édition différentielle (`SEARCH/REPLACE` validé par AST) fournit à la fois un taux de validité suffisant pour que le gradient de (E) prenne ($\tau_{\text{val}} \ge 0.80$, illustratif) et une expressivité asymptotiquement égale à $\mathcal{V}$.
* **Métrique** : Gain net d'apprentissage transféré $\Gamma = \mu(E_{\text{RL}}) - \mu(F)$ lorsque (E) et (F) opèrent tous deux dans le même espace d'action (soit tous deux dans $G_{\text{ind}}$, soit tous deux en Diffs sur $O_0$, soit tous deux en $\Sigma^*$ avec boucle de réparation bornée à $K=3$ essais, illustratif).
* **Seuil** : Écart $\Delta \Gamma \ge 0.05$ (5 points de score normalisé sur tâches tenues à l'écart, illustratif) avec $p < 0.01$ sur $n = 25$ (illustratif) graines d'entraînement RL.
* **Contrôle négatif** : Évaluation sur les familles de tâches *d'entraînement* (in-distribution). Si $G_{\text{ind}}$ domine sur l'entraînement mais s'effondre sur les familles tenues à l'écart alors que sa couverture syntaxique reste de $100\%$, cela prouve le sur-apprentissage structurel de la grammaire induite.
* **Issues falsificatrices** :
  * *Falsification de $H_A$* : $\Gamma_{\text{Diffs}} > \Gamma_{G_{\text{ind}}} + 0.05$, accompagné d'un taux de validité des diffs de (E) $\tau_{\text{val}} \ge 0.80$ (illustratif) dès le premier quart de l'entraînement RL.
  * *Falsification de $H_B$* : En mode Diffs, la variance du gradient empêche la convergence ($\mu(E_{\text{RL, Diffs}}) - \mu(E_{0, \text{Diffs}}) < 0.02$, illustratif) à cause de l'accumulation de patchs invalides ou destructeurs, tandis que $E_{\text{RL}, G_{\text{ind}}}$ converge et transfère sur les tâches tenues à l'écart.

---

## (c) Étalonnage des instruments de mesure et de contrainte

La question mobilise quatre instruments techniques dont le bon fonctionnement conditionne toute conclusion. Voici la mesure minimale pour certifier chacun d'eux :

1. **Instrument 1 : Le décodeur contraint par grammaire / schéma ($G$)**
   * *Ce qu'il doit faire* : Garantir que $100\%$ des sorties appartiennent à $L(G) \cap \mathcal{V}$ sans détruire la perplexité du modèle par des coupures de sous-mots (*tokenization artifacts*).
   * *Cas honnêtes appariés* : Un banc de $1\,000$ (illustratif) paires (spécification en langage naturel, organisme valide de référence appartenant à $L(G)$). On compare la log-probabilité assignée par le modèle avec et sans masque grammatical, et la validité d'exécution des échantillons générés.
   * *Taux de détection et fausses alertes* :
     * Taux de détection (rejet des séquences hors $L(G)$) : doit être de $100\%$ par construction mathématique de l'automate à pile.
     * Taux de fausses alertes (séquences sémantiquement valides dans $L(G)$ rendues inatteignables à cause du découpage en jetons BPE) : doit être $< 1\%$ (illustratif).
     * Taux d'organismes générés dans $L(G)$ mais échouant à l'exécution ($\in L(G) \setminus \mathcal{V}$, ex. : variables non définies non capturées par la grammaire hors-contexte) : doit être $< 5\%$ (illustratif).
   * *Vérification mécanique à battre* : Échantillonnage libre suivi d'un `json.loads()` ou `ast.parse()` avec rejet brut (Rejection Sampling). Le décodeur contraint doit atteindre le même taux de validité avec un coût en jetons générés au moins $5\times$ inférieur (illustratif).

2. **Instrument 2 : Le pipeline de validation et de réparation en sortie libre**
   * *Ce qu'il doit faire* : Identifier tout organisme $x \notin \mathcal{V}$ avant l'exécution complète des tâches coûteuses et permettre sa réparation syntaxique sans altérer la logique architecturale voulue par le concepteur.
   * *Cas honnêtes appariés* : $500$ (illustratif) organismes valides issus de $F_{\text{libre}}$ auxquels on injecte synthétiquement des fautes graduées (erreur de syntaxe Python, violation d'interface du noyau, boucle infinie à l'initialisation, appel d'outil inexistant), appariés aux $500$ originaux intacts.
   * *Taux de détection et fausses alertes* :
     * Taux de détection (vrais positifs d'invalidité sur le jeu corrompu via test unitaire fumée / *smoke test*) : $\ge 99\%$ (illustratif).
     * Taux de fausses alertes (rejet d'un organisme valide intact à cause d'un délai d'attente trop court ou d'un analyseur statique trop strict) : $\le 0.5\%$ (illustratif).
   * *Vérification mécanique à battre* : Un correcteur déterministe par règles (linter automatique type `ruff --fix` + fermeture automatique des accolades/blocs). La boucle de réparation par LLM ne se justifie que si son taux de sauvetage sur erreurs d'interface dépasse de $25$ points (illustratif) celui du linter déterministe à budget de jetons comptabilisé.

3. **Instrument 3 : L'extracteur de grammaire induite ($G_{\text{ind}}$) et sa mesure de couverture**
   * *Ce qu'il doit faire* : Construire à partir d'un corpus d'entraînement de $F_{\text{libre}}$ une grammaire qui accepte les productions futures de $F_{\text{libre}}$ sur de nouvelles tâches.
   * *Cas honnêtes appariés* : Séparation stricte d'un corpus de $1\,000$ (illustratif) organismes valides produits par $F_{\text{libre}}$ : $500$ sur les familles de tâches A (pour induire $G_{\text{ind}}$) et $500$ sur des familles de tâches B disjointes (pour tester la couverture hors-distribution), plus $500$ programmes Python quelconques hors cadre d'organisme (contrôle de spécificité).
   * *Taux de détection et fausses alertes* :
     * Couverture hors-distribution (sensibilité sur les sorties de $F_{\text{libre}}$ sur familles B) : $\ge 90\%$ (illustratif).
     * Fausses alertes de la grammaire (rejet d'un organisme valide de $F_{\text{libre}}$ sur B) : $\le 10\%$ (illustratif).
     * Sélectivité (rejet des programmes Python hors-cadre ou cassant l'interface du noyau) : $\ge 95\%$ (illustratif) — sinon $G_{\text{ind}}$ est triviale (équivalente à la grammaire complète de Python, ce qui annule l'effet de réduction d'espace).
   * *Vérification mécanique à battre* : La grammaire standard de Python + validation de schéma Pydantic minimal sur le point d'entrée du noyau.

4. **Instrument 4 : La métrique de diversité structurelle des organismes**
   * *Ce qu'il doit faire* : Mesurer si la contrainte de format écrase la variété des architectures explorées, indépendamment des variations cosmétiques (noms de variables, commentaires).
   * *Cas honnêtes appariés* : $200$ (illustratif) paires d'organismes isomorphes fonctionnellement (même graphe d'appel et même flux de mémoire, mais variables renommées et code réordonné) contre $200$ paires d'architectures distinctes (ex. : pipeline séquentiel vs arbre de débat multi-agents vs boucle réflexive avec mémoire externe).
   * *Taux de détection et fausses alertes* :
     * Détection de changement architectural (distance normalisée $> \tau$) : $\ge 90\%$ (illustratif) sur les paires distinctes.
     * Fausses alertes (distance $> \tau$ sur des paires isomorphes obfusquées) : $\le 5\%$ (illustratif).
   * *Vérification mécanique à battre* : La distance d'édition de chaînes (Levenshtein ou `difflib`) sur le code source brut après formatage par `black` et suppression des commentaires. L'instrument (ex. : distance d'édition sur le graphe de flux de données et d'appels extrait par analyse statique) doit battre Levenshtein sur l'invariance au renommage et à la réorganisation syntaxique.

---

## (d) Ancrage matériel et références connues (Point 4 de l'arbitre)

### Ancrage matériel (Modèles, calcul, coûts — tous les chiffres sont « illustratifs »)

* **Modèles** :
  * *Concepteur entraîné (E)* : Modèle à poids ouverts de taille moyenne spécialisé code/raisonnement, ex. `Qwen2.5-Coder-14B-Instruct` ou `DeepSeek-Coder-V2-Lite-Instruct` (16B MoE, 2.4B actifs) (illustratif). Entraînement par GRPO (Group Relative Policy Optimization) ou PPO avec LoRA (rang $r=64$, illustratif) ou poids complets.
  * *Concepteur figé (F)* : Modèle de frontière accessible par API ou poids fermés/grands poids ouverts figés (ex. classe `Claude-3.5-Sonnet` ou `DeepSeek-V3` / `Llama-3.1-405B-Instruct` figé comme proxy reproductible de frontière, illustratif).
  * *Exécutants de frontière figés (au sein de l'organisme)* : Modèle rapide et économique figé pour exécuter les nœuds de l'organisme lors des évaluations (ex. `Llama-3.1-8B-Instruct` ou `Qwen2.5-7B-Instruct` servi localement via vLLM pour éliminer la dérive d'API, illustratif).
  * *Infrastructure de décodage contraint* : Bibliothèques ouvertes `Outlines` ou `XGrammar` intégrées au moteur d'inférence vLLM / SGLang pour appliquer $G$ avec un surcoût par jeton $< 5\text{ ms}$ (illustratif).
* **Calcul nécessaire et budget apparié (Expérience 1 à 6 bras)** :
  * L'unité d'appariement de coût total entre (F) et (E) est le **FLOP total consommé** (ou équivalent monétaire GPU-heure incluant : génération des organismes + évaluation des organismes sur les tâches d'entraînement + passes avant/arrière du RL pour E).
  * Par graine d'entraînement de (E) : $500$ (illustratif) épisodes de génération d'organismes $\times 8$ échantillons par groupe (GRPO) $= 4\,000$ évaluations d'organismes. À raison de $50$ appels d'exécutants (7B) par évaluation d'organisme, une graine consomme $\approx 40$ heures-GPU H100 (80 Go) (illustratif).
  * Pour $n = 30$ graines $\times 2$ bras entraînés ($E_{\text{RL}, G}$ et $E_{\text{RL}, \text{libre}}$) $= 2\,400$ heures-GPU H100 (illustratif).
  * Les $4$ bras sans entraînement ($F_{\text{libre}}, F_G, E_{0, \text{libre}}, E_{0, G}$) reçoivent exactement le même budget d'évaluation ($4\,000$ évaluations d'organismes par graine pour faire de la recherche évolutionnaire / Best-of-$N$ sans mise à jour de poids), soit $4 \times 30 \times 30 \text{ h} \approx 3\,600$ heures-GPU H100 (illustratif).
* **Coût total estimé** : Environ $6\,000$ heures-GPU H100 pour l'Expérience 1 complète (et $\approx 2\,500$ heures-GPU H100 pour l'Expérience 2), soit à un tarif académique/cloud de $2{,}50\text{ \$/h}$ par H100 (illustratif), un budget matériel d'environ **$15\,000\text{ \$}$ à $21\,250\text{ \$}$** (illustratif), plus $\approx 3\,000\text{ \$}$ (illustratif) d'appels API si (F) est un modèle propriétaire externe.

### Ce qui est connu : références citables (Règle 3 & Point 4 de l'arbitre)

Conformément à la règle 3 et aux instructions de la question, toutes les références ci-dessous sont marquées « référence à vérifier » et aucun identifiant arXiv n'est donné de mémoire :

1. **Sur la méta-conception automatique d'architectures d'agents en code libre (bras F libre)** :
   * Hu, S., Lu, C., & Clune, J. (2024). *Automated Design of Agentic Systems*. (Référence à vérifier — introduit « Meta Agent Search » où un modèle figé programme des systèmes d'agents en code Python libre et montre l'émergence de topologies non prévues par des schémas fixes).
2. **Sur l'optimisation de graphes et d'invites d'agents dans un espace paramétré/contraint** :
   * Khattab, O., Singhvi, A., Maheshwari, P., Zhang, Z., Santhanam, K., Vardhamanan, S., Haq, S., Sharma, A., Joshi, T. T., Moazam, H., Miller, H., Zaharia, M., & Potts, C. (2023 ou 2024). *DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines*. (Référence à vérifier — formalise la séparation entre la topologie déclarative contrainte et l'optimisation des paramètres discrets).
   * Zhuge, M., Wang, W., Kirsch, L., Faccio, F., Khizbullin, D., & Schmidhuber, J. (2024). *GPTSwarm: Language Agents as Optimizable Graphs*. (Référence à vérifier — restreint l'espace de conception à des graphes computationnels pour permettre l'optimisation explicite des arêtes et des nœuds).
3. **Sur le décodage contraint par grammaire et ses effets de distorsion sur les modèles de langue** :
   * Willard, B. T., & Louf, R. (2023). *Efficient Guided Generation for Large Language Models*. (Référence à vérifier — formalise la compilation d'expressions régulières et de grammaires hors-contexte en automates à états finis sur le vocabulaire d'un LLM, base de la bibliothèque Outlines).
   * Tam, Z. R., Wu, C.-K., Tsai, Y.-L., Lin, C.-Y., Lee, H.-Y., & Chen, Y.-N. (2024). *Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models*. (Référence à vérifier — mesure empiriquement la perte de performance de raisonnement lorsqu'on contraint la sortie d'un modèle figé à un schéma JSON ou une grammaire stricte par rapport à une sortie libre).
   * Park, K., Wang, J., Berg-Kirkpatrick, T., Polikarpova, N., & D'Antoni, L. (2024). *Grammar-Aligned Decoding*. (Référence à vérifier — démontre que le masquage glouton de logits sous contrainte grammaticale biaise la distribution conditionnelle du modèle et propose une correction).
4. **Sur la génération de code par édition différentielle (Diffs) et réparation itérative** :
   * Chen, X., Lin, M., Schärli, N., & Zhou, D. (2023 ou 2024). *Teaching Large Language Models to Self-Debug*. (Référence à vérifier — quantifie l'effet d'une boucle de validation-réparation par retour d'exécution sur le taux de validité du code en sortie libre).

FIN-DE-CELLULE
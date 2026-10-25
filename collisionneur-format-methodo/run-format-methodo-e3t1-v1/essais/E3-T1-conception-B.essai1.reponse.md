# Proposition B, tour III.1 : séparer le format de l'apprentissage

**Pièces reçues.** Le bloc FAITS déclare qu'aucun fait n'est joint. Ce bloc est complet, pas coupé. Aucun énoncé ci-dessous n'est donc VÉRIFIÉ. Ce que dit la question est RAPPORTÉ (par la question), mes ajouts sont des HYPOTHÈSES et le contenu de la littérature est RAPPORTÉ, à vérifier. Les propositions A et C ne me sont pas transmises (tour à l'aveugle) : je ne les attaque pas et ne m'en sers pas, faute de contenu.

---

## 0. Le problème formalisé (point 1 de la question)

**Objets.**
- Σ\* désigne les chaînes possibles et V ⊂ Σ\* les programmes valides (ils s'exécutent et produisent un classifieur).
- L(G) ⊂ V est le langage de la grammaire.
- π_θ est la distribution de sortie d'un modèle.
- J_tr(h) est le score sur les familles d'entraînement. C'est lui qui sert de récompense ou de critère de sélection.
- J_te(h) est le score sur les familles tenues à l'écart.
- Une procédure P, de budget b, rend un programme ĥ_P. La quantité cible est E[J_te(ĥ_P)], l'espérance étant prise sur les graines et les familles.

**Premier point à corriger : l'objet pertinent est une distribution, pas un ensemble.** L'ensemble « 𝓗 = ce que F peut produire » est mal défini, car toute chaîne a une probabilité non nulle sous un modèle à softmax. L'objet opérationnel est π_F restreinte à V, ou son support effectif {h : π_F(h) > ε}. L'inclusion 𝓗_G ⊂ 𝓗 n'est donc pas acquise : G peut autoriser des programmes que F ne produit jamais en pratique (HYPOTHÈSE).

**Deuxième point : il existe deux opérateurs de restriction distincts.**
- *Conditionnement exact* : C_G π(h) = π(h)·𝟙[h∈L(G)] / π(L(G)). On l'obtient par échantillonnage par rejet.
- *Masquage local* (décodage contraint jeton par jeton), noté M_G π. En général, M_G π ≠ C_G π, parce que le masquage renormalise localement et non globalement. Cette distorsion est RAPPORTÉE par Park et al. (2024), à vérifier.

« F contraint » mélange donc la restriction du support et la distorsion de la distribution. Ce sont deux causes à séparer.

**La restriction seule peut produire un écart dans les deux sens.** On considère la valeur d'une recherche « best-of-N », V_N(π) = E[J_te(argmax_{i≤N} J_tr(h_i))]. Restreindre π à L(G) agit par quatre canaux de signes opposés :

1. **Expressivité** : sup_{L(G)} J_te ≤ sup_V J_te. Ce canal ne peut que nuire.
2. **Budget** : si une fraction q de π_F est invalide, F ne dispose que de N(1−q) essais utiles. La grammaire récupère ces qN essais. Ce canal ne peut qu'aider, à coût par échantillon égal.
3. **Renormalisation et biais inductif** : si π(bonne région | L(G)) > π(bonne région | V), la grammaire concentre la masse. L'inverse se produit si elle exclut les structures qui gagnent.
4. **Régularisation** : sélectionner parmi moins de candidats effectivement distincts réduit la « malédiction du gagnant » J_tr(ĥ) − J_te(ĥ). L'heuristique de type Occam en √(log|𝓗_eff| / n_familles) n'est qu'une HYPOTHÈSE. Elle suppose les familles échangeables.

*Illustratif.* Supposons q = 0,3, une bonne région de masse 0,01 dans V, conservée à 50 % par une grammaire qui garde 40 % de la masse valide. Après restriction, la bonne région pèse 0,0125 au lieu de 0,01, et le gain de budget s'y ajoute. Si G ne conserve que 10 % de la bonne région, le signe s'inverse. Rien n'impose de signe a priori.

**Identifiabilité.** On note les issues potentielles Y(f, l, m, b) :
- format f ∈ {L (libre), G} ;
- ajustement l ∈ {na (non ajusté), aj (ajusté)} ;
- modèle m ∈ {M (grand), m (moyen)} ;
- régime de budget et de rétroaction b.

L'« effet de l'apprentissage » identifiable par randomisation des graines est un **effet direct contrôlé** :

CDE_l = E[Y(G, aj, m, b)] − E[Y(G, na, m, b)]

Il est identifiable sous cinq conditions (HYPOTHÈSES à garantir par construction) :
- même modèle de base et même grammaire G ;
- même nombre d'appels à l'oracle et même règle de sélection pour le bras non ajusté, qui doit être un best-of-N sur le même budget et pas un tirage unique ;
- récompenses calculées uniquement sur les familles d'entraînement ;
- familles de test jamais vues, même indirectement ;
- échangeabilité des graines.

**Ce que les quatre bras proposés identifient vraiment.** Les quatre bras sont F libre, F contraint, E contraint ajusté et E contraint non ajusté. Ils permettent la décomposition télescopique exacte suivante :

Y_E − Y_F = [Y(G,aj,m) − Y(G,na,m)] + [Y(G,na,m) − Y(G,na,M)] + [Y(G,na,M) − Y(L,na,M)]

Les trois termes sont, dans l'ordre, l'apprentissage, la taille du modèle et le format.

Cette identité est exacte, mais **elle dépend du chemin**. S'il existe des interactions (format × apprentissage, taille × format), un autre ordre donne d'autres attributions. Une attribution indépendante de l'ordre, par exemple une moyenne de type Shapley, exige les huit cellules de f × l × m. Les quatre bras **ne forment pas un plan 2 × 2** : la cellule « libre ajusté » manque. L'interaction format × apprentissage n'y est donc pas identifiable. C'est la limite principale du plan suggéré.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi c'est à vérifier |
|---|---|---|---|
| a1 | La comparaison se fait à coût total apparié | RAPPORTÉ (question) | L'unité n'est pas fixée. Apparier en FLOPs ou en appels à l'oracle peut inverser la conclusion (voir (b), coût). |
| a2 | 𝓗_G ⊂ 𝓗 | HYPOTHÈSE | Ce qui compte est le support effectif de π_F, et G peut déborder de ce support (§ 0). |
| a3 | La différence E − F se ramène à deux causes, format et apprentissage | HYPOTHÈSE, probablement fausse | Il y a au moins deux autres facteurs : la **taille du modèle** (grand contre moyen) et l'**accès à la rétroaction** (E reçoit des scores, F peut-être pas). |
| a4 | « F figé » signifie « F sans rétroaction » | HYPOTHÈSE implicite | Un modèle figé peut s'adapter en contexte à partir des scores. Mettre à jour des paramètres et exploiter une rétroaction sont deux choses différentes. |
| a5 | Les effets s'additionnent | HYPOTHÈSE | La question elle-même suggère une interaction : la contrainte existe « pour que l'ajustement porte sur un espace bien défini ». |
| a6 | « F contraint » isole l'effet du format | HYPOTHÈSE | Le masquage déforme la distribution (§ 0). Le rejet ne la déforme pas mais coûte 1/π_F(L(G)). |
| a7 | La note d'un programme invalide de F est neutre | Non spécifié | Un 0, une exclusion ou une réparation changent mécaniquement l'effet du format. Il faut figer ce choix d'avance. |
| a8 | Les familles tenues à l'écart sont échangeables avec celles d'entraînement | HYPOTHÈSE | Si elles ne le sont pas, « l'apprentissage » peut n'être qu'un surajustement aux familles d'entraînement. |
| a9 | La métrique est fixée d'avance | RAPPORTÉ (question) | Ce point est acquis. La règle d'agrégation entre familles (moyenne, pire cas) doit l'être aussi. |
| a10 | Le validateur détecte l'invalidité pertinente, c'est-à-dire aussi les programmes qui trichent (fuite de labels, lecture des fichiers de test) | HYPOTHÈSE | Rien ne le garantit. Voir (c). |
| a11 | L'ajustement crée des structures nouvelles | HYPOTHÈSE | Il peut seulement repondérer le support de la base. Ce mécanisme est RAPPORTÉ par Yue et al. (2025), à vérifier, dans un autre domaine. |

---

## (b1) Les voies, ce qu'elles coûtent et ce qu'elles perdent (point 2)

Aucune voie n'est « la » réponse. Pour chacune, j'indique ce qui la départagerait des autres.

**V1. La même grammaire pour les deux procédures.**
- *Mesure* : le contraste entre F libre et F sous G, décomposé en trois bras : F libre, F rejet (C_G) et F masqué (M_G).
- *Ce qu'elle perd* : elle n'informe que sur une seule grammaire, et les conclusions ne se transportent pas à une autre.
- *Ce qu'elle coûte* : le rejet multiplie les tokens générés par 1/π_F(L(G)).
- *Ce qui la ruine* : une acceptation trop faible, inférieure à 5 % (seuil illustratif). Le rejet devient alors impraticable et seul le masquage reste, avec sa distorsion.

**V2. Une sortie libre pour E, avec validation et réparation.**
- *Intérêt* : elle crée la cellule manquante « libre ajusté ».
- *Grandeurs à mesurer* : le taux d'invalides avant réparation au fil de l'ajustement, le coût en appels de réparation, et la dérive sémantique introduite par la réparation.
- *Risque* : l'ajustement apprend à exploiter le réparateur au lieu de produire de bons programmes. Pour le contrôler, on compare au bras « invalide = 0, sans réparation ».

**V3. Une grammaire induite d'un corpus de sorties de F.**
- *Construction* : on extrait les AST des programmes valides de F, puis on généralise. Deux options : des règles à partir des constructions observées (plus des listes ouvertes pour identifiants et constantes), ou une induction de grammaire de type Arvada ou GLADE (références plus bas).
- *Couverture* : la fraction de sorties de F **tenues à l'écart de l'induction** que G analyse. On l'accompagne de l'estimateur de Good (masse non vue ≈ part des singletons parmi les classes structurelles).
- *Piège* : une grammaire trop générale a une couverture de 100 % et ne restreint plus rien. Il faut donc mesurer aussi sa **précision**, c'est-à-dire la fraction des programmes tirés sous G qui sont valides et non dégénérés.

**V4. Des sorties par édition.**
- *Principe* : des différences sur l'AST d'un programme de départ.
- *Ce qu'elle change* : l'opérateur de recherche devient local, et le biais inductif vient du programme initial.
- *Facteur confondant nouveau* : le point de départ. Il faut le même programme initial pour tous les bras et au moins deux points de départ, ce qui fait du point de départ un facteur.
- *Avantage* : la validité est garantie par construction si les éditions sont définies sur l'AST.
- *Ce qu'elle perd* : l'accès aux structures éloignées du départ.

**V5. Autres voies.**
- **V5a. Projection a posteriori.** On analyse la sortie libre de F et on la projette sur le membre de L(G) le plus proche (distance d'édition d'arbres). Le coût est faible et la perte due à G se mesure directement sur les programmes de F.
- **V5b. Une famille de modèles à plusieurs tailles.** Le « grand » et le « moyen » viennent de la même famille de modèles. La taille devient alors un facteur contrôlé plutôt qu'un facteur confondant.
- **V5c. F avec rétroaction en contexte.** On garde F figé mais on lui donne les scores dans le prompt. Cette voie sépare l'effet de la mise à jour des paramètres de celui de l'usage de la rétroaction (a4).
- **V5d. La grammaire comme API.** Le programme est une composition d'appels à une bibliothèque fixe, et non une syntaxe arbitraire. La restriction porte alors sur le vocabulaire, pas sur la syntaxe.

**Ce qui départage les voies.**
1. Le taux d'acceptation π_F(L(G)), qui décide entre V1-rejet et V1-masquage.
2. La couverture et la précision de la grammaire, qui décident de V3.
3. La stabilité de l'ajustement en sortie libre, qui décide de la faisabilité de V2.

On mesure ces trois quantités dans une phase pilote, avant le plan principal.

---

## (b2) Expériences décisives en duels (point 3)

Les conventions sont communes à tous les duels :
- l'**unité de réplication** est une exécution complète d'une procédure (une graine), et non un programme ;
- le score est l'exactitude J_te du programme sélectionné, agrégée sur les familles tenues à l'écart ;
- un écart est établi si l'IC à 95 % du contraste exclut 0 et dépasse δ ;
- l'absence d'écart est établie par un test d'équivalence (TOST) sur ±δ ;
- δ = 2 points d'exactitude (illustratif, à fixer d'avance par l'arbitre).

### D1. Mise à jour des paramètres contre simple sélection
- **H_A** : le gain de E ajusté sur E non ajusté vient de la mise à jour des paramètres.
- **H_B** : il vient de la sélection parmi N programmes évalués, c'est-à-dire de la recherche. C'est l'argument de la ligne de base « recherche aléatoire » en recherche d'architectures (Li & Talwalkar 2019).
- **Bras** : E_G ajusté, et E_G non ajusté en best-of-N avec le **même nombre d'appels à l'oracle** et la même règle de sélection.
- **Contrôle négatif** : E_G ajusté avec des **récompenses permutées**, c'est-à-dire que les scores sont mélangés entre programmes à l'intérieur de chaque lot.
- **Issues** :
  - si ajusté − non ajusté ∈ [−δ, δ] (TOST), H_A est falsifiée ;
  - si l'écart dépasse δ et que le bras à récompenses permutées n'excède pas le non ajusté, H_B est falsifiée ;
  - si le bras à récompenses permutées gagne aussi, ni H_A ni H_B ne tient sous sa forme simple. Le gain viendrait d'un effet non lié au score, comme une réduction d'entropie ou une convergence vers les formes les plus probables de G. C'est une issue informative, pas un échec.

### D2. Nouvelles structures contre repondération du support
- **H_A** : l'ajustement atteint des classes structurelles hors du support effectif de la base.
- **H_B** : il repondère seulement des classes que la base atteint avec assez d'échantillons.
- **Métrique** : on prend les programmes du top 10 de E ajusté, réduits à leur forme canonique (AST sans identifiants ni constantes numériques). On mesure la fraction de ces classes présentes dans K échantillons de la base sous G, avec K = 10 × le budget (illustratif).
- **Contrôle négatif** : deux exécutions indépendantes de la base. Leur recouvrement mutuel de classes calibre le recouvrement attendu par hasard.
- **Issues** :
  - si la couverture par la base est au moins égale au recouvrement base-base moins 5 points (illustratif), H_A est falsifiée ;
  - si elle est nettement inférieure et que la base à K échantillons n'atteint pas le J_te de E ajusté, H_B est falsifiée.

### D3. Restriction du support contre distorsion par masquage (effet du format sur F)
- **H_A** : la perte de F sous G vient de la restriction du support (expressivité et renormalisation).
- **H_B** : elle vient de la distorsion du décodage par masquage.
- **Bras** : F libre, F rejet (C_G) et F masqué (M_G), au même nombre de programmes évalués.
- **Contrastes** : libre − rejet mesure l'effet de support pur ; rejet − masqué mesure l'effet de distorsion.
- **Contrôle négatif** : une grammaire « universelle » G_U qui accepte tous les programmes valides observés de F. Sous G_U, les trois bras doivent être équivalents ; tout écart mesure un artefact du pipeline (tokenisation, troncature).
- **Issues** :
  - si libre − rejet ∈ [−δ, δ] alors que rejet − masqué > δ, H_A est falsifiée ;
  - dans le cas inverse, H_B est falsifiée.

### D4. Additivité contre interaction format × apprentissage (cellule manquante)
- **H_A** : l'effet de l'ajustement est le même en sortie libre et en sortie contrainte.
- **H_B** : l'ajustement n'opère que grâce au format.
- **Bras** : E_L ajusté, E_L non ajusté, E_G ajusté et E_G non ajusté, ce qui forme un vrai 2 × 2 sur le même modèle moyen. En sortie libre, la règle « invalide = 0 » est figée d'avance.
- **Contraste d'interaction** : (E_G,aj − E_G,na) − (E_L,aj − E_L,na).
- **Contrôle négatif** : D1 avec récompenses permutées, répété dans les deux formats.
- **Issues** :
  - un IC de l'interaction exclu de [−δ, δ] falsifie H_A ;
  - une interaction équivalente à 0 par TOST falsifie H_B.
- L'effondrement éventuel de E_L ajusté (le taux d'invalides monte) est une donnée en faveur de H_B, pas une exclusion du bras.

### D5. Taille du modèle contre format
- **H_A** : à format et ajustement fixés, l'écart entre F et E vient de la taille du modèle.
- **H_B** : la taille n'y joue pas.
- **Contraste** : F_G non ajusté − E_G non ajusté, au même nombre d'appels à l'oracle. Ce contraste existe déjà dans les quatre bras de la question.
- **Contrôle** : un troisième point de taille dans la même famille de modèles (V5b), pour tester la monotonie.
- **Issues** :
  - un contraste dans [−δ, δ] falsifie H_A ;
  - un contraste au-delà de δ, croissant avec la taille, falsifie H_B.

### D6. Régularisation contre efficacité de recherche
- **H_A** : G aide par régularisation, c'est-à-dire par un écart J_tr − J_te plus faible à J_tr égal.
- **H_B** : G aide par efficacité de recherche, c'est-à-dire un J_tr plus élevé et un écart inchangé.
- **Métrique** : l'écart d'entraînement à test du programme sélectionné, dans les bras libre et contraint, sur le même modèle.
- **Contrôle négatif** : la sélection sur une partition d'entraînement sans signal, avec labels permutés. L'écart observé y donne le plancher de la malédiction du gagnant.
- **Issues** :
  - si l'écart est égal (TOST) et que G gagne en J_tr, H_A est falsifiée ;
  - si l'écart diminue sous G sans gain en J_tr, H_B est falsifiée.

### Modèle statistique
On utilise un modèle mixte binomial au niveau de l'item, ou un modèle linéaire mixte sur l'exactitude par famille :

y_{s,k} = μ + β_f·f + β_l·l + β_fl·(f×l) + β_m·m + u_s + v_k + w_{k×bras} + ε

- u_s est l'effet aléatoire de la graine, v_k celui de la famille ;
- w_{k×bras} autorise l'hétérogénéité des effets entre familles ;
- l'ajustement se fait avec lme4 (Bates et al. 2015) ;
- on fait aussi un bootstrap stratifié par graine et par famille, comme seconde estimation ;
- on rapporte des intervalles plutôt que des moyennes de « meilleure graine » (Agarwal et al. 2021, Bouthillier et al. 2021).

### Taille d'échantillon (illustratif)
- *Hypothèses illustratives* : un écart-type entre graines σ = 3 points et Δ = 3 points, avec α = 0,05 et une puissance de 0,8.
- *Comparaison de deux bras* : n ≈ 2(1,96 + 0,84)² σ²/Δ² ≈ 15,7, soit **16 graines par bras**.
- *Interaction 2 × 2* : la variance du contraste vaut 4σ²/n au lieu de 2σ²/n. Pour une interaction de même taille, il faut donc environ **32 graines par cellule**.
- *Limite réelle* : le nombre de familles tenues à l'écart, car l'effet aléatoire de la famille borne la généralisation. Il en faut au moins 20 (illustratif), ce qui reste à confirmer par une simulation de puissance fondée sur la phase pilote.

### Contrôle du coût apparié
- **Grandeurs à journaliser séparément** :
  - appels à l'oracle, c'est-à-dire programmes évalués sur les familles d'entraînement ;
  - tokens générés, y compris ceux rejetés et ceux des réparations ;
  - FLOPs d'entraînement de E ;
  - temps réel.
- **Asymétrie connue.** Avec l'approximation standard de 2N FLOPs par token généré, un modèle de 32 milliards de paramètres coûte environ 32/7 ≈ 4,6 fois plus par token qu'un modèle de 7 milliards. Le calcul est explicite, mais les tailles 32B et 7B sont un choix illustratif. À FLOPs égaux, E dispose donc de beaucoup plus d'échantillons.
- **Deux régimes d'appariement.** Apparier sur les FLOPs ou sur les appels à l'oracle répond à deux questions différentes. Le plan exécute **les deux** régimes.
- **Courbes plutôt que points.** On rapporte des courbes « score contre coût » sur trois niveaux de budget plutôt qu'un point unique. Une inversion de classement entre niveaux est en soi un résultat.

---

## (c) Les instruments : la mesure minimale qui dirait s'ils fonctionnent

Pour chaque instrument, on donne trois choses : le taux de détection (TD), le taux de fausses alertes (FA), mesurés sur des **paires honnêtes appariées**, et la **vérification mécanique à battre**.

**I1. Décodeur contraint, grammaire G.**
- *Ce qu'il prétend* : n'émettre que des chaînes de L(G), et pouvoir les émettre toutes.
- *Paires* : chaque programme de L(G) apparié à un jumeau hors de L(G) par une mutation minimale.
- *Grandeurs* : TD = fraction des jumeaux que le masquage ne peut pas produire ; FA = fraction des membres de L(G) que le masquage rend inaccessibles (frontières de tokenisation).
- *À battre* : l'analyseur hors ligne de G appliqué au texte complet. La cible est un accord de 100 %, et tout désaccord est un bogue à corriger avant le plan principal.

**I2. Validateur (« validé ensuite »).**
- *Paires* : un programme honnête et son jumeau fautif, avec trois sortes de fautes : erreur de syntaxe, clé de configuration erronée, exception sur une entrée limite.
- *Seconde série de paires (indispensable)* : un programme honnête et un jumeau **tricheur**, qui lit les labels de test, accède au système de fichiers ou appelle le réseau.
- *Grandeurs* : TD par type de faute ; FA sur les programmes honnêtes.
- *À battre* : la compilation suivie d'une exécution sur 10 exemples. Le validateur n'apporte quelque chose que s'il détecte ce que cette vérification rate, c'est-à-dire la triche et les fautes sémantiques.
- *Complément* : un bac à sable sans accès aux fichiers de test, et des labels témoins (« canari ») dans les données.

**I3. Réparateur.**
- *Paires* : un programme valide et sa version corrompue.
- *Grandeurs* : TD = taux de retour à l'équivalence comportementale, mesurée par des prédictions identiques sur un jeu de sondes ; FA = taux de réparations « réussies » qui changent le comportement.
- *À battre* : deux réparations triviales, abandonner le programme (score 0) ou le remplacer par le plus proche programme valide en cache.

**I4. Mesure de couverture d'une grammaire induite.**
- *Grandeurs* : la couverture sur des sorties de F non utilisées pour l'induction, et la précision, c'est-à-dire la fraction de tirages sous G qui sont valides et non dégénérés.
- *À battre* :
  - la grammaire triviale Σ\*, de couverture 100 % et de précision faible ;
  - la grammaire qui mémorise le corpus, de précision élevée et de couverture faible hors corpus.
- *Critère* : la grammaire induite doit dominer ces deux points sur la courbe couverture-précision.
- *Masse non vue* : l'estimateur de Good, à contrôler par sous-échantillonnage. On induit sur 50 % du corpus et on vérifie que l'estimateur prédit la couverture mesurée sur l'autre moitié.

**I5. Métrique de diversité structurelle.**
- *Paires* :
  - des réécritures cosmétiques, qui ne doivent pas compter comme différentes : renommage, réordonnancement d'instructions indépendantes, reformatage ;
  - des changements de structure réels, qui doivent compter : autre extracteur de traits, autre classifieur.
- *Grandeurs* : TD sur les changements réels ; FA sur les réécritures cosmétiques.
- *À battre* : la distance d'édition sur chaînes et le Jaccard sur tokens. La distance d'édition d'arbres sur l'AST canonique (Zhang & Shasha 1989) doit faire mieux.
- *Second instrument* : une diversité **fonctionnelle**, le désaccord des prédictions sur un jeu de sondes. Deux codes différents peuvent en effet calculer la même chose.

**I6. Comptabilité du coût.**
- *Mesure* : l'écart entre les coûts déclarés et ceux recalculés à partir des journaux bruts. On l'éprouve sur des exécutions où l'on injecte des coûts cachés connus (appels de réparation, générations rejetées).
- *Grandeurs* : TD = fraction de ces coûts injectés retrouvés ; FA = coûts fantômes, comptés mais jamais engagés.

---

## (d) Ancrage matériel (tout est illustratif)

**Modèles ouverts.** On prend une même famille de modèles de code à plusieurs tailles, par exemple Qwen2.5-Coder en 7B (moyen) et 32B (grand), ou leurs successeurs disponibles en octobre 2026, à vérifier. Une seconde famille sert de réplication, par exemple Llama 3.1 en 8B et 70B.

**Outils.**
- Décodage contraint : Outlines, XGrammar, ou le décodage guidé de vLLM.
- Ajustement : GRPO (Shao et al. 2024) via TRL, avec LoRA.
- Programmes évalués : des classifieurs légers, comme scikit-learn ou de petits encodeurs. Ce choix rend l'oracle peu coûteux.

**Estimation de calcul (illustratif).**
- *Plan* : 7 bras (F libre, F rejet, F masqué, puis E_G et E_L, chacun ajusté et non ajusté), 16 graines (32 pour les cellules du 2 × 2 de D4) et environ 2 000 programmes évalués par exécution.
- *Volume* : de l'ordre de 300 000 évaluations de programmes, chacune sur 5 familles d'entraînement, à environ 1 minute CPU par évaluation. Cela fait environ 25 000 heures CPU, soit quelques centaines de dollars.
- *Génération* : environ 800 tokens par programme, soit de l'ordre de 2,4 × 10⁸ tokens. Cela représente quelques dizaines d'heures H100, plus le surcoût du rejet en 1/π_F(L(G)).
- *Ajustement* : environ 4 heures H100 par exécution ajustée, sur environ 96 exécutions, soit environ 400 heures H100, de l'ordre de 1 000 dollars à 2,5 dollars de l'heure.
- *Ordre de grandeur total* : quelques milliers de dollars, phase pilote comprise (illustratif). Le poste dominant dépend du coût réel de l'oracle, à mesurer dans la phase pilote.

---

## Références (point 4) : attributions que je crois correctes, détails de publication à vérifier

**Génération contrainte**
- Shin, R. et al. (2021). *Constrained Language Models Yield Few-Shot Semantic Parsers*. EMNLP.
- Scholak, T., Schucher, N., Bahdanau, D. (2021). *PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models*. EMNLP.
- Willard, B. T., Louf, R. (2023). *Efficient Guided Generation for Large Language Models* (Outlines).
- Geng, S., Josifoski, M., Peyrard, M., West, R. (2023). *Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning*. EMNLP.
- Park, K., Wang, J., Berg-Kirkpatrick, T., Polikarpova, N., D'Antoni, L. (2024). *Grammar-Aligned Decoding*. NeurIPS. C'est la référence sur la distorsion entre masquage et conditionnement.
- Tam, Z. R. et al. (2024). *Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models*.
- Dong, Y. et al. (2024). *XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models*. À vérifier.

**Induction de grammaires**
- de la Higuera, C. (2010). *Grammatical Inference: Learning Automata and Grammars*. Cambridge University Press.
- Bastani, O., Sharma, R., Aiken, A., Liang, P. (2017). *Synthesizing Program Input Grammars*. PLDI (GLADE).
- Kulkarni, N., Lemieux, C., Sen, K. (2021). *Learning Highly Recursive Input Grammars*. ASE (Arvada). À vérifier.
- Good, I. J. (1953). *The Population Frequencies of Species and the Estimation of Population Parameters*. Biometrika.

**Recherche de programmes et d'architectures**
- Zoph, B., Le, Q. V. (2017). *Neural Architecture Search with Reinforcement Learning*. ICLR.
- Li, L., Talwalkar, A. (2019). *Random Search and Reproducibility for Neural Architecture Search*. UAI.
- Yang, A., Esperança, P. M., Carlucci, F. M. (2020). *NAS Evaluation is Frustratingly Hard*. ICLR. C'est le précédent le plus direct pour la confusion entre espace de recherche et méthode.
- Real, E., Liang, C., So, D. R., Le, Q. V. (2020). *AutoML-Zero: Evolving Machine Learning Algorithms From Scratch*. ICML.
- Ellis, K. et al. (2021). *DreamCoder: Bootstrapping Inductive Program Synthesis with Wake-Sleep Library Learning*. PLDI.
- Lehman, J. et al. (2022). *Evolution through Large Models*.
- Romera-Paredes, B. et al. (2024). *Mathematical Discoveries from Program Search with Large Language Models*. Nature.
- Shao, Z. et al. (2024). *DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models* (GRPO).
- Yue, Y. et al. (2025). *Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?* À vérifier.

**Plans d'expérience et statistique en apprentissage automatique**
- Montgomery, D. C. *Design and Analysis of Experiments*. Wiley, plusieurs éditions.
- Bates, D., Mächler, M., Bolker, B., Walker, S. (2015). *Fitting Linear Mixed-Effects Models Using lme4*. Journal of Statistical Software.
- Dror, R., Baumer, G., Shlomov, S., Reichart, R. (2018). *The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing*. ACL.
- Bouthillier, X. et al. (2021). *Accounting for Variance in Machine Learning Benchmarks*. MLSys.
- Agarwal, R. et al. (2021). *Deep Reinforcement Learning at the Edge of the Statistical Precipice*. NeurIPS.
- VanderWeele, T. J. (2015). *Explanation in Causal Inference: Methods for Mediation and Interaction*. Oxford University Press.

**Distance entre arbres**
- Zhang, K., Shasha, D. (1989). *Simple Fast Algorithms for the Editing Distance between Trees and Related Problems*. SIAM Journal on Computing.

---

## Ce qui est réfutable dans cette proposition

1. **La décomposition à quatre bras dépend de l'ordre des termes.** Cette thèse tombe si l'interaction mesurée en D4 est équivalente à 0.
2. **Le bras non ajusté doit être un best-of-N à budget d'oracle égal.** Cette thèse tombe si D1 montre que la sélection seule n'apporte rien par rapport à un tirage unique.
3. **Le choix entre masquage et rejet est un facteur à part entière.** Cette thèse tombe si rejet − masqué est équivalent à 0 en D3.
4. **L'appariement en FLOPs et l'appariement en appels à l'oracle peuvent inverser le classement.** Cette thèse tombe si les courbes coût-score des deux régimes donnent le même ordre.

FIN-DE-CELLULE
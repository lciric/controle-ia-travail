La pièce 20 (N9-1) est visiblement coupée après « dans toute la population restée non » ; je n’utilise rien au-delà de cette coupure. Les références aux propositions A–C décrivent leurs conceptions (**RAPPORTÉ**) ; les seuils nouveaux sont **illustratifs**. Dans les duels ci-dessous, un résultat intermédiaire falsifie la puissance annoncée du plan, et non seulement l’hypothèse scientifique visée.

## Sur la proposition A

### (a) Défauts de méthode

- **N1 — le placebo « rareté seule » n’isole pas le risque CB-05.** Comparer sa précision à celle de `c` confond la rareté avec la prévalence des vrais ponts dans le vivier, le nombre de paires valides, κ, le domaine et les interactions entre ces variables. Une précision proche de `c` n’exclut pas que N exploite la rareté **en interaction** avec κ. Réciproquement, une précision supérieure peut refléter la vérité plantée dans le monde, sans démontrer une fuite propre à l’instrument.
- **N1 — le nul de calibration est déplacé.** G3 avec λ = 0 supprime le double canal qui fait partie de l’explication du diagnostic. Il ne fournit donc pas la loi nulle du générateur sous S16a. De plus, l’option F est conçue après lecture du diagnostic : calibration, choix de la marge et évaluation doivent utiliser trois ensembles de graines distincts.
- **N3 — un succès vrai par construction.** Mesurer la part de paires « jamais reliées » retenues par S31 ne teste rien si S31 filtre précisément sur « jamais reliées ». La permutation du vocabulaire entre fiches ne conserve ni le degré, ni l’âge, ni la dépendance entre paires : elle ne fournit pas le nul apparié annoncé.
- **N4 — mauvaise population pour estimer la loi des niches.** Les 28 rendus ne représentent pas nécessairement les fiches non aiguillées : l’aiguillage peut dépendre de la niche et du contenu. Et permuter les niches entre fiches conserve leur distribution empirique ; cela ne produit pas le « prior uniforme » attendu par le contrôle proposé.
- **N6 — VS5-01 est constaté mais non traité.** Réécrire la justification de DL-12 ne répare pas M1 : après centrage, son test d’invariance fondé sur les moyennes résiduelles peut perdre toute force discriminante.
- **N11 — puissance empruntée et insu rompu.** Les σ de J, A4 et A6 ne déterminent pas la variance d’un nouveau contraste entre bras. Par ailleurs, soumettre titre et résumé de l’article-pont au proposeur pour demander « connu/inconnu » révèle la cible et modifie le comportement qu’il faudrait mesurer.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **T2 :** soit \(q_s=P(\text{concept observé des deux côtés}\mid s)\). Si \(q_s\) est petit, la moyenne conditionnelle est estimée sur une sous-population différente selon \(s\) ; si \(q_s=0\), elle n’est pas définie. Le maximum sur statuts amplifie les queues lourdes et les déséquilibres d’effectifs.
- **Placebo de rareté :** l’effet propre de la rareté \(R\) n’est identifiable qu’avec positivité, \(0<P(R=r\mid X=x)<1\), et un modèle pour l’interaction \(R\times\kappa\). Sans elle, l’estimand marginal précision(placebo) − précision(`c`) mélange plusieurs effets.
- **N4 :** la simulation suppose indépendance entre niches, accord des lecteurs et structures partagées. Une corrélation intra-lot ou une dépendance structure–niche modifie \(P(\text{zéro paire})\) sans changer les marges ; 28 rendus ne suffisent pas à estimer cette dépendance.
- **N5 :** une sortie agrégée \(O\), même limitée à des comptes, peut conserver \(I(K;O)>0\) pour des compositions de témoins presque dégénérées. L’AUC par témoin est en outre indéfinie si l’échantillon d’évaluation ne contient qu’une classe.
- **N6 :** après centrage par environnement, \(E[\hat\varepsilon_S\mid u]=0\) pour tout ensemble \(S\) sans C. Un test M1 fondé sur ces seules moyennes ne peut alors plus rejeter les mauvais ensembles ; pour T1, le centrage ne supprime pas une confusion si les pentes varient entre strates.
- **N9 :** les aires par cohorte ne sont comparables qu’à ensembles à risque et censure définis. Peu de positives dans une cohorte, ou une fenêtre masquée, rend l’échec de seuil compatible avec un simple manque de puissance.
- **N11 :** avec corrélation intra-sous-session \(\rho\), la variance d’un taux est approximativement \(p(1-p)[1+(m-1)\rho]/n\), non \(p(1-p)/n\). Le coût par vrai trouvé est indéfini lorsque le dénominateur est nul. Une concordance de trois rangs de bras ne calibre pas les seuils \(W=0,7\) et \(W=0,3\).

### (c) Contrôles négatifs indispensables

1. **Double intervention sur mondes neufs, après v3 scellée.** L’une modifie le concept rare planté ; l’autre laisse vérité, κ, degrés et repli inchangés mais permute la fréquence de l’étiquette retenue.  
   \(H_A\) : le contraste des bras est invariant sous la seconde permutation ; \(H_B\) : il ne l’est pas. Un intervalle inclus dans \([-\varepsilon,\varepsilon]\) falsifie \(H_B\) ; un intervalle hors de cette zone falsifie \(H_A\). Les mêmes calculs sous `M_inertes` et `N_PCg` doivent rester nuls.
2. **N4 :** permutation des niches **en conservant** la distribution empirique et la structure du lot, puis comparaison sur des lots ultérieurs non utilisés pour régler la grille. Si le \(P(\text{zéro})\) prédit est hors de son intervalle, la loi de simulation est falsifiée.
3. **N11 :** leurres contenant un seul parent, un titre évocateur sans mécanisme commun, et paires aléatoires appariées. Le succès doit exiger les **deux identifiants parents**. Si ces leurres sont « trouvés » au-dessus du nul combinatoire, l’oracle de correspondance est invalidé.

## Sur la proposition B

### (a) Défauts de méthode

- **N1 — le générateur « cassé » teste exactement ce que T2 mesure.** Modifier de +2/−2 la fréquence du concept planté selon le statut ne peut démontrer qu’une sensibilité à cette famille d’altérations. Cela ne teste ni la pathologie de l’étiquette retenue ni l’exploitabilité par les bras. La corrélation proposée entre rareté moyenne par statut et précision différentielle de N est, elle, une corrélation écologique entre mondes, exposée à tous les mélanges de conditions.
- **N3 — non-redondance mal définie.** Un κ faible peut signifier diversité, mais aussi absence de lien exploitable. Une paire identique au bras basique sur « au moins deux lots » n’est pas estimable si le pré-pilote n’en produit qu’un. Et un échec de HB sur le modèle Gu-Krenn ne réfute pas logiquement un substitut différent, construit sur une autre source : il affaiblit seulement un argument analogique.
- **N4 — validation tautologique du score.** Un argmax a nécessairement un score moyen au moins égal à celui d’un tirage aléatoire **sur son propre score**. Ce contrôle ne mesure aucune validité externe. L’estimation « environ deux paires de niches » après retrait de trois structures n’est pas déduite des pièces : la table canal × distance ne dépend pas de cette liste.
- **N10 — ratio sans unité commune.** Diviser une perte de performance par un taux de jailbreak n’a pas de signification sans fonction d’utilité de l’attaquant. Le seuil « ratio > 1 » est donc non jugeable tel quel.
- **N11 — oracle trop permissif.** Retrouver une seule fiche ayant κ > 0,3 avec un pont ne démontre ni l’appariement des deux parents ni la reconstruction du mécanisme. La date de coupure « fin 2025 » est une supposition non établie.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **N1 :** la puissance annoncée ≥ 0,95 ne vaut que pour l’amplitude et la direction de l’artefact injecté. Elle ne se transporte ni à une fréquence d’opérateur modifiée à concept planté constant, ni à un repli différemment distribué.
- **N3 :** les quartiles de κ dépendent de la composition des 45 paires ; ils ne définissent pas une grandeur comparable entre lots. Une seule paire choisie par bras interdit d’estimer séparément redondance et qualité.
- **N5 :** comme chez A, l’information résiduelle dépend de \(I(K;O)\), pas seulement de l’AUC d’un classifieur choisi. Le contrôle « passe/nœud sans comptes » ne couvre pas la sortie réellement publiée.
- **N6 :** cinquante mondes ne distinguent pas utilement une fausse détection de 0,01 d’une de 0,02. Le duel DL-1 n’est pas exclusif : iVAE peut rester sous 0,70 tout en battant M5. Surtout, retrouver \(z_1,\ldots,z_5\) ne qualifie que les latentes, pas la flèche.
- **N9 :** l’AUC > 0,60 ne teste pas « mieux que l’attachement préférentiel » ; cette seconde comparaison exige son propre estimand apparié et son intervalle.
- **N11 :** les calculs binomiaux supposent des essais indépendants, contredits par la mutualisation des fiches et des sessions. Avec seulement trois bras, la corrélation de Spearman ne peut atteindre \(p<0,05\) en test exact bilatéral : même \(|\rho|=1\) donne \(p=1/3\).

### (c) Contrôles négatifs indispensables

1. **N1 : deux familles d’artefacts, pas une.** Artefact A sur le concept planté, artefact B sur l’étiquette retenue seule.  
   \(H_A\) : T2 détecte A et reste aveugle à B, tandis que le rapport ancien détecte B ; \(H_B\) : une de ces trois propriétés est fausse. Chaque composante est donc falsifiable séparément. Le générateur inchangé sert de nul de fausse alerte, sur graines neuves.
2. **N4 :** vérité externe sur fiches indépendantes, avec niches et structures fixées avant le score. Le contrôle nul permute les identifiants de structures **à niche et marges constantes** ; toute supériorité mesurée uniquement par le score de sélection est écartée.
3. **N10 :** trois témoins obligatoires — absence de défense, moniteur aléatoire, et filtre fondé seulement sur la difficulté de tâche. L’estimand doit être \(P(E=1,\ U\ge u_0)\), à \(u_0\) gelé. Un moniteur qui ne réduit l’évasion viable qu’en rejetant aussi les cas honnêtes difficiles est un échec, pas une réussite.
4. **N11 :** paires leurres à un seul parent, à deux parents sans mécanisme commun, et cibles aléatoires, sur lots non utilisés pour écrire les scores. Sans cela, le taux de « correspondance » n’est pas interprétable.

## Sur la proposition C

### (a) Défauts de méthode

- **N1 — la « sensibilité » change l’estimand et la vérité.** Compter les vrais d’opérateur comme non-ponts pénalise leur sélection légitime : ce n’est plus une restriction du contraste initial, mais une autre expérience. Sous-effectif et changement de prévalence peuvent alors simuler un artefact. De plus, les indices 300–599 proposés comme graines neuves recouvrent la plage déjà réservée 300–499.
- **N4 — profil ajusté pour produire de la disponibilité.** Modifier les distances pour intégrer n5, élargir la bande et changer l’ordre de priorité des bras peut être une décision de conception, mais pas une validation du profil. Le contrôle où seules des structures exclues sont partagées et où le score vaut zéro est vrai par construction.
- **N6 — l’hybride DL-12 change de méthode et ouvre une fuite.** Centrer toutes les méthodes sauf M1 rompt la comparaison à entrées communes et laisse M1 exposée au chemin κ. Tester l’invariance des pentes et variances plutôt que des moyennes définit une autre méthode, à préenregistrer comme telle. Conditionner ensuite Estimation-θ à une corrélation réalisée ≥ 0,85 introduit une sélection sur le résultat.
- **N10 — le cas extrême est traité comme un coût nécessaire.** La KL > 100 concerne une quasi-orthogonalité avec conservation du comportement ; elle n’est pas une condition nécessaire d’évasion. Le TEFV peut aussi chuter parce que le défenseur rejette toutes les tâches difficiles, sans gain utile de sécurité.
- **N11 — deux conditions de transport non estimables.** Sur fiches réelles, κ_lat n’est pas observé : la fuite F de V2 n’y est donc pas calculable. Et comparer un accord de lecteurs à la couverture 0,65 de `M_moyen` juxtapose deux paramètres sans unité commune.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **N1 :** après restriction aux vrais conceptuels, la puissance dépend du nombre de mondes conservés et de la nouvelle prévalence. Un effet global présent mais non retrouvé dans le sous-ensemble ne démontre un artefact que si l’intervalle du sous-estimand exclut aussi les effets compatibles.
- **N3/N9 :** la rétrodiction exige que les champs nécessaires aux traits et étiquettes existent réellement. Leur disponibilité n’est pas établie pour la moisson locale. Masquer janvier–avril 2023 réduit les positives ; un échec ultérieur peut être purement binomial.
- **N4 :** retirer des structures diminue la probabilité de partage tandis qu’élargir la bande augmente les paires de niches candidates. Sans loi jointe sur ces deux événements, l’effet net sur \(P(\text{zéro})\) est indéterminé.
- **N5 :** un seuil d’exactitude unique sur 100 simulations ne contrôle ni l’erreur de première espèce ni les comparaisons multiples entre canaux inspectés.
- **N10 :** si la distribution de l’utilité \(U\) dépend de la difficulté et que celle-ci est corrélée à l’évasion, un seuil commun \(u_0\) ne suffit pas ; il faut une estimation stratifiée ou appariée.
- **N11 :** si l’aiguilleur exclut les parents plantés selon leur contenu, les ponts restants sont manquants non au hasard. À zéro paire parentale survivante, rappel et fausses alertes ne sont pas définis.

### (c) Contrôles négatifs indispensables

1. **N1 : conserver deux estimands distincts.** Le contraste principal sur tous les vrais, et un contraste secondaire sur vrais conceptuels avec leurs propres négatifs.  
   \(H_A\) : les deux estimands dépassent la marge gelée ; \(H_B\) : au moins un ne la dépasse pas. Leur désaccord falsifie l’invariance revendiquée, pas automatiquement la validité du bras. `M_inertes` et `N_PCg` doivent rester nuls dans les deux.
2. **N6 :** monde jouet β = 0 et monde à effet planté, avec mêmes entrées pour M1 et les témoins. Si M1 accepte presque tout sous β = 0, ou ne retrouve plus C à la puissance prévue, la transformation DL-12 est falsifiée ; une simple correction rédactionnelle ne suffit pas.
3. **N10 :** filtre « difficulté seule » et moniteur qui rejette systématiquement les cas difficiles, évalués sur des cas honnêtes appariés en difficulté. Le contrôle nul d’attaque conserve la distribution d’utilité de référence. Toute baisse du TEFV accompagnée d’une baisse équivalente de couverture honnête est comptée comme artefact de rejet.
4. **N11 :** chimères anachroniques, homonymes sans structure, paires à un seul parent et ponts factices faciles. Le protocole doit aussi déclarer les parents exclus par l’aiguilleur avant tout calcul de rappel. Sans ces quatre nuls, le prétendu oracle partiel mélange détection de forme, reconnaissance de source et découverte réelle.

FIN-DE-CELLULE
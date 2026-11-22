# Critique croisée de méthode, tour III.2 (proposition B)

**Pièces.** Les quatre conceptions (A, C, D, E) sont présentes et non coupées. Je n'ai pas recalculé les sha256. Le bloc FAITS ne donne aucun statut à ses énoncés. A les cite comme « statut non fourni » ; C et E leur attribuent « RAPPORTÉ ». Je le signale sans le reprendre. Toute critique ci-dessous est une **HYPOTHÈSE de B**, sauf mention contraire.

**Notation commune.** Elle sert à exprimer les conditions de la partie (b) de chaque section.

- p : prévalence des collisions parmi les cibles candidates.
- r : taux de détection (rappel) d'un instrument.
- f : taux de fausses alertes.
- n : nombre de cibles testées.
- m : nombre de témoins plantés.

Trois conditions reviennent pour toutes les propositions :

- **(N1) Non-identifiabilité.** Un instrument non étalonné observe un taux d'alerte q = p·r + (1−p)·f. Avec q seul, on ne sépare pas p de f.
- **(N2) Rareté.** Si n·p est petit devant 1, la probabilité d'observer zéro collision vaut environ e^{−np}, qu'elle soit grande ou faible. Les deux hypothèses prédisent alors la même issue : le duel n'est pas jugeable.
- **(N3) Vérité-terrain biaisée par la découvrabilité.** Supposons que les cas positifs d'un banc soient trouvés par une famille d'outils T (moteurs, graphes de citations, mémoire d'un modèle). Le rappel mesuré est alors E[r | collision découvrable par T], qui majore le rappel réel. Les collisions qui coûtent cher sont précisément celles que T ne trouve pas.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **Fuite entre construction des cibles et évaluation (E1).** Les travaux de 2026 « croisés par hasard » ont pu orienter la rédaction des cibles candidates : un titre aperçu suffit. Dans ce cas, une collision entre ces travaux et les cibles n'alarme sur rien. Elle est vraie par construction, et le contrôle par articles de 2026 tirés au hasard la fera paraître significative. Contrôle requis : dater chaque cible candidate et déclarer ce que son auteur avait vu au moment de la rédiger.
2. **« Croisés par hasard » n'est pas un tirage aléatoire.** Un article retient l'attention parce qu'il paraît proche. La comparaison avec des articles tirés au hasard dans la même catégorie mesure donc la proximité perçue par un lecteur, pas la valeur des rencontres fortuites comme signal. A tire la bonne conséquence (« c'est p qui est élevé ») dans un seul sens. L'autre sens manque : si les articles croisés collident plus, cela peut ne refléter que le filtre d'attention.
3. **Le cas honnête « index avant Y » n'est pas une vérité-terrain.** A écrit « aux anticipations réelles près », mais ne traite pas la conséquence. Supposons que l'agent réponde « connu » sur l'index d'avant Y. Trois explications sont confondues : fausse alerte, fuite mémorielle (la date de coupure du modèle est postérieure à Y), ou découverte d'une vraie anticipation antérieure à Y. Le banc compte les trois comme fausses alertes. La fuite mémorielle, qu'A veut mesurer, se confond ainsi avec la meilleure performance possible de l'instrument.
4. **Le témoin négatif de E2 vient d'une autre forme de cible.** Les « objets à score exact sur instances tirées au hasard » mesurent f sur une forme où, selon A lui-même, la lecture pèse peu. Rien ne garantit que ce f se transpose à la forme « énoncé ». Il est probablement plus faible, puisqu'un objet frais n'a aucun voisin textuel.
5. **Erreur logique de falsification dans E3.** H_A affirme qu'au moins une collision est propre au bras « zone ». Observer zéro sur K cibles ne falsifie pas une existence : cela borne un taux. A le reconnaît (« à la résolution 3/K ») mais conclut quand même que « (a) et (c) comme défaut » sont falsifiées.
6. **τ = c_lecture/(r·C_tardif) dans E2 abandonne le terme f** présent dans le calcul de valeur d'information du point 1.2. Avec f > 0, chaque fausse alerte fait abandonner une bonne cible. Le seuil correct monte donc avec f·(valeur de la cible).

### (b) Conditions de perte de puissance

- **E1.** Avec k travaux croisés et une probabilité individuelle de collision π, une collision apparaît avec probabilité 1−(1−π)^k. Si k·π ≲ 1, l'absence de collision est l'issue attendue sous les deux hypothèses (N2). E1 ne tranche alors rien et ne doit pas être lu comme soutien à H_B.
- **E2.** L'intervalle sur p ne se place sous τ que si n > 3/τ, par la règle de trois. Pour un τ petit, n = 15 (illustratif chez A) ne peut pas falsifier H_A. Le protocole se déclarera « indécis » quelle que soit la réalité. De plus, p̂ est estimé avec l'instrument lui-même, ce qui donne p̂ ≈ p·r + (1−p)·f (N1). Si f n'est pas petit devant τ, le seul bruit de l'instrument suffit à « falsifier H_B ».
- **E3.** Notons q_z la probabilité qu'une collision ne soit vue que par le bras « zone ». Le nombre attendu d'événements est K·p·q_z. S'il est petit devant 1, l'issue nulle domine sous les deux hypothèses.
- **Banc apparié.** Le rappel est mesuré sur un mélange de déguisements π_banc (notation, cas particulier, autre vocabulaire). Le rappel en usage est Σ_k π_réel,k · r_k. Si r_k est hétérogène et π_réel ≠ π_banc, le seuil « 0,8 » (illustratif) ne prédit rien. Il faut publier r_k par type de déguisement, pas seulement la moyenne.
- **Témoins plantés de E3.** Avec m témoins et un rappel r, un bras passe avec probabilité r^m. Pour m = 2, un instrument médiocre passe souvent. Le critère d'invalidité a donc peu de puissance.

### (c) Contrôles négatifs dont l'absence serait fatale

- Pour E1 : des cibles candidates rédigées par quelqu'un qui n'a vu aucun travail de 2026, comparées aux autres. Sans ce contrôle, la fuite du point (a)1 reste invisible.
- Pour le banc « avant Y » : le même agent sans accès à l'index. S'il répond « connu » au même taux, l'index ne sert à rien et la mémoire décide.
- Pour E2 : des énoncés négatifs de même forme (mutation vérifiée d'une hypothèse), et non des objets à score.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Cibles définies comme « strictes améliorations » des énoncés de 2026, puis vérifiées contre ces mêmes énoncés.** C'est la fuite la plus grave des quatre propositions. Une cible construite pour différer d'un théorème T ne collide pas avec T, par construction. Le test « d'implication triviale à partir de ces empreintes » est donc vrai par construction sur son propre corpus. Le vrai risque, une suite ou un travail concurrent qui fait déjà l'amélioration, n'est pas couvert.
2. **Le contrôle « négatif » de l'Expérience 1 est un contrôle positif.** Des variantes obfusquées de Fano, Bretagnolle–Huber et Wald doivent être détectées : ce sont des collisions plantées. Aucun témoin ne mesure f. Par (N1), le p_coll de l'Expérience 1 n'est pas identifiable.
3. **Ces témoins sont faciles par construction.** Ils figurent dans la bibliothèque Lean (fait transmis) et, très probablement, dans la mémoire de tout modèle. Les réussir ne dit rien du rappel sur les prépublications de 2026, qui sont celles qui coûtent.
4. **Le « canari de contamination » est qualifié de preuve d'« antériorité certaine ».** C'est une promotion de statut. Une régurgitation de citation peut être fabriquée, et une preuve restituée peut être une reconstruction. La sonde produit au mieux une piste, statut HYPOTHÈSE, à confirmer par une source datée.
5. **Les cas positifs du banc sont tirés « des travaux voisins de 2026 non lus ».** Pour réécrire un théorème, il faut l'avoir lu. Les mêmes travaux servent en outre de graines à l'instrument (traversée de citations). L'instrument est donc évalué sur son propre voisinage de départ (N3).
6. **Les cas négatifs appariés n'ont pas de vérité-terrain.** Remplacer i.i.d. par « nul non stationnaire » rend le théorème source inapplicable, mais rien ne prouve que l'énoncé modifié est absent de la littérature. C l'étiquette « vraie nouveauté » sans vérification.
7. **Contrôles de l'Expérience 2 vrais par construction.** Des paires identiques mot pour mot et des domaines disjoints sont trivialement classées par n'importe quelle ligne lexicale. Ils ne discriminent rien et ne valident que le câblage.
8. **Seuil τ₁ = C_lect/B_cible.** Il omet le coût d'une collision après revendication, que C qualifie pourtant de coût de réputation distinct. Il omet aussi r et f. Le seuil penche donc mécaniquement vers (b).
9. **L'hypothèse « Markov » du graphe de citations porte toute la recommandation**, puisque la lecture est réduite aux travaux de 2026 et à leurs références directes. Aucune expérience ne la teste.

### (b) Conditions de perte de puissance

- **Test d'implication par prouveur.** Notons s la probabilité que le prouveur trouve une implication courte qui existe vraiment. Le taux de cibles scellées alors qu'elles collident vaut p·(1−s). Si s est faible, ce qui est le cas pour les changements de variable ou les applications de Jensen que C cite lui-même, le filtre laisse passer presque tout. Son « succès » mesuré est alors le taux de non-collision par défaut.
- **Expérience 1.** p̂ = p·r + (1−p)·f, avec f non mesuré, donc la comparaison p̂ vs τ₁ n'est pas jugeable. Avec un échantillon de taille n et n·p ≲ 1, on se trouve en (N2).
- **Hypothèse Markov.** Notons ρ la part des collisions situées hors du voisinage à un saut des graines. Le rappel maximal atteignable par la stratégie est 1−ρ, quel que soit l'agent. Si ρ est substantiel (silos disciplinaires, que C décrit lui-même), aucune mesure interne au voisinage ne le révèle.
- **« Aveugle inversé ».** Le relecteur dispose d'un temps t pour réduire l'énoncé. La probabilité de réduction, P(réduit | collision, t), croît avec t. Un échec à temps court n'est donc pas une évidence de nouveauté : c'est la mesure de t.

### (c) Contrôles négatifs dont l'absence serait fatale

- Des énoncés vérifiés non impliqués par leur voisin, pour mesurer f.
- Des collisions plantées hors du voisinage de citations des graines, pour mesurer ρ.
- Pour la sonde de mémorisation : des énoncés inventés et faux, sur lesquels toute « citation » produite est une fabrication.

---

## Sur la proposition D

D est la proposition la plus prudente sur les statuts. Ses défauts sont surtout de jugeabilité.

### (a) Défauts de méthode

1. **La perte commune contient un terme non observable.** Le « retrait erroné d'une cible » suppose de savoir qu'une cible retirée était neuve. Or D pose elle-même que la preuve externe est asymétrique : aucun accord n'établit la nouveauté. Ce terme de la perte n'a donc pas d'estimateur. Le duel sur le moment de lecture est non jugeable tant qu'on ne remplace pas ce terme par une quantité observable, par exemple « retrait sans source datée accompagnée d'une réduction ».
2. **Confusion entre politique et équipe.** Les « équipes séparées » sur des « portefeuilles appariés » mêlent l'effet de la politique et l'effet de l'équipe. Avec une équipe par bras, la différence de perte vaut effet politique plus effet équipe, et les deux ne sont pas séparables. Il faut un croisement : chaque équipe passe sous chaque politique sur des portefeuilles différents.
3. **Indépendance déclarée à l'égard des chercheurs, pas des outils.** Les dossiers rétrospectifs sont constitués indépendamment des chercheurs, mais à l'aide de recherches documentaires. Si ces recherches utilisent les mêmes familles d'outils que les instruments évalués (index lexical, encodeur, parcours de citations), on retombe en (N3). Le gain de l'agent sur le contrôle mécanique est alors borné par construction, puisque les positifs sont ceux que le mécanique savait trouver.
4. **Effet de sélection de la veille sur le portefeuille.** La politique précoce retire des cibles avant pilote. Le portefeuille restant n'est plus apparié à l'autre bras : ses cibles sont, en moyenne, plus difficiles ou moins connues. D impose de conserver les fiches des cibles écartées, ce qui est nécessaire. Mais la perte de l'autre bras doit aussi être calculée sur les mêmes cibles retirées, faute de quoi le duel compare deux populations différentes.
5. **« Première obligation non satisfaite » jugée par l'agent qui fait la comparaison.** Cette obligation sert à la fois à construire le verdict et, dans le tableau, à évaluer l'extraction. D sépare bien l'extraction du verdict dans l'épreuve ; il faut le faire aussi en usage.

### (b) Conditions de perte de puissance

- **Duels de politique.** La perte par portefeuille est dominée par des événements rares, de probabilité p, et coûteux, de coût C_tardif. Sa variance est d'ordre p·(1−p)·C_tardif². Pour séparer une différence Δ entre politiques, il faut un nombre de portefeuilles d'ordre p·C_tardif²/Δ². Si p est petit et C_tardif grand, ce nombre dépasse ce que le programme peut produire. D le dit (« des données trop imprécises … ne tranchent pas »), mais ne donne pas la condition à vérifier avant de lancer les duels.
- **Duel « extension au pilier ».** Notons p_tr la prévalence des collisions transverses. On a n·p_tr ≲ 1 dans tout scénario réaliste de taille de portefeuille, donc (N2). Ce duel ne peut pas falsifier H_B, sauf par la colonne des coûts.
- **Seuil instrumental.** Notons r_agent et r_méca les rappels de l'agent et du contrôle mécanique. Si les positifs du banc sont construits par des outils corrélés à ceux du contrôle mécanique, r_méca est surestimé, r_agent − r_méca est biaisé, et l'absence de gain devient l'issue attendue.

### (c) Contrôles négatifs dont l'absence serait fatale

- Des positifs trouvés par une voie sans outil de recherche : signalement d'un spécialiste, ou errata de bibliothèques. Sans eux, (N3) n'est pas mesurable.
- Un bras où la politique précoce est appliquée sans dérogation réelle, c'est-à-dire avec une lecture fictive à coût nul. Il mesure ce que la seule discipline de fiche, sans lecture, apporte à la perte.

---

## Sur la proposition E

### (a) Défauts de méthode, dont des manquements d'intégrité

1. **Statuts promus.** E marque [VÉRIFIÉ] des propositions qui sont les siennes, sans démonstration ni source contrôlée :
   - « isomorphisme » entre la fusion de p-valeurs sous dépendance et les bornes de copules ;
   - « équivalence par dualité minimax » entre jeux d'inspection et comparaison d'expériences de Blackwell ;
   - « produisent exactement la même constante » ;
   - « témoins mutés réellement neufs, [VÉRIFIÉ] par LP ».

   Un lien entre agrégation de risques sous dépendance et fusion de p-valeurs me paraît plausible, mais son attribution à Vovk et Wang (2021) est une référence à vérifier, et l'équivalence avec Blackwell n'est pas étayée. Ce sont des HYPOTHÈSES. E marque aussi « (illustratif) » des références datées (Vovk–Wang 2021, Blackwell 1953, Ville 1939). C'est incohérent : une attribution est soit vérifiable, soit « référence à vérifier », elle n'est pas illustrative. Enfin, « je ne sais pas combien de cibles… » reçoit le statut [OBSERVÉ-NON-AUDITÉ] : une inconnue n'est pas une observation.
2. **Un LP sur petit alphabet ne vérifie pas la nouveauté.** Il vérifie que l'énoncé muté diffère du théorème source. Que l'énoncé muté ne soit pas publié ailleurs reste non établi. Toute la colonne « quasi-jumeaux honnêtes » du tableau (c) repose sur cette confusion.
3. **E1 mesure p sur les premières revendications, pas sur les cibles candidates.** E fait elle-même l'hypothèse que les agents sont attirés vers le connu. Les revendications sont donc enrichies en collisions, par l'hypothèse de E. Le taux mesuré surestime le p pertinent pour un filtrage avant scellement, et H_A est favorisée par construction. Le seuil τ* omet en outre r.
4. **E3 est tautologique pour la forme « lemme ».** Selon la définition de E (point I.1), une antériorité papier n'est pas une collision pour un lemme Lean. Le gain de la lecture d'articles sur cette forme est donc nul par définition, et « gain net < 0 » est garanti dès que la lecture coûte quoi que ce soit. L'expérience ne mesure rien. Le contrôle « Forme 3 doit montrer un gain positif » suppose la conclusion d'E2 au lieu de servir de témoin.
5. **Le contrôle « négatif » d'E2 est un contrôle positif** : collisions explicites, rappel ≥ 90 %. Les cas du banc d'E2 (antériorité répartie entre disciplines jumelles) sont vraisemblablement constitués par traduction multi-dialectes, c'est-à-dire par la méthode du bras « énoncé ». Le ΔR est alors positif par construction (N3).
6. **Le hachage par petites instances confond égalité de valeurs et équivalence.** Deux problèmes distincts peuvent avoir la même constante pour K ∈ {2, 3, 4}. Une coïncidence numérique donne une alerte, pas une collision.
7. **Détails chiffrés à précision fictive.** Sont concernés les 1 à 4 € par cible, les 80 à 200 heures-GPU, et les noms de versions de modèles. Ils sont marqués illustratifs, mais ils déterminent l'argument central de coût contre l'option (a). Une conclusion qui ne repose que sur des chiffres illustratifs n'est pas une conclusion.

### (b) Conditions de perte de puissance

- **Exigence « rappel = 100 % sur témoins » d'E1.** La probabilité de passer est r^m. Pour m petit, un instrument médiocre passe. Pour m grand, tout instrument réel échoue. Le critère dépend de m plus que de r. Il faut un seuil sur un intervalle pour r, pas sur un comptage.
- **Hachage par petites instances.** Notons κ la probabilité qu'une valeur numérique donnée coïncide pour des problèmes distincts. Si κ est non négligeable devant p, la précision s'effondre : PPV ≈ p·r / (p·r + (1−p)·κ). Pour les résultats asymptotiques, E note que r ≈ 0.
- **E2.** ΔR est estimé sur des positifs dont la découvrabilité dépend du bras « énoncé ». Si P(positif inclus | trouvé par la traduction) > P(positif inclus | trouvé par l'index), l'estimateur ΔR̂ est biasé vers H_A. Le seuil de 15 points (illustratif) n'y change rien.
- **E1.** Le comptage de collisions dans la « pile 2026 » relève de (N2) si k·π ≲ 1. Le critère « 0 collision directe » ne peut pas soutenir H_B.

### (c) Contrôles négatifs dont l'absence serait fatale

- Des paires de problèmes distincts à constantes coïncidentes sur petites instances, pour mesurer κ.
- Des énoncés mutés dont la nouveauté est contrôlée par un spécialiste avec source, et non par LP.
- Pour E1, un lot de cibles candidates jamais soumises aux agents, afin de mesurer p hors de la sélection par revendication.
- Pour E2, des positifs collectés par une voie indépendante des deux bras.

---

## Ce que je retiens pour B (usage déclaré, B1)

Les quatre propositions mesurent un rappel sur des collisions qu'elles savent déjà trouver (N3). Je propose d'en faire un duel explicite :

- **Protocole.** Deux instruments, construits sur des index et des modèles disjoints, sont appliqués aux mêmes cibles. Le nombre de collisions trouvées par les deux renseigne sur le total, à la manière d'une estimation par capture-recapture.
- **Hypothèses.** H_A : les deux instruments se recouvrent au-delà de ce que l'indépendance prédit. On mesure alors la corrélation de leurs angles morts, et l'estimation du total est invalide. H_B : le recouvrement est compatible avec l'indépendance. L'estimation de p devient défendable, et (N3) est quantifiée.
- **Ce que chaque issue falsifie.** H_A vraie falsifie toute recommandation fondée sur « l'union des méthodes ». H_B vraie falsifie l'idée qu'aucune mesure de p n'est possible avant lecture large.
- **Limite.** Je ne sais pas si les effectifs disponibles permettent de séparer les deux hypothèses : la même condition de rareté (N2) s'applique.

FIN-DE-CELLULE
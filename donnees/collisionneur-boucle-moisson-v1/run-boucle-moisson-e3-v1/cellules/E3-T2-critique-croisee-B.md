# Proposition B — Tour III.2 : critique croisée de méthode

**Pièce 5 (antériorité de la boucle) : non servie, absente des faits ; je n'en invente pas le contenu.**

---

## Sur la proposition A

### (a) Défauts de méthode

**1. E1 (les juges voient-ils un progrès ?) confond le format de l'augmentation avec sa détectabilité.**
Le matériau est construit par un « metteur en forme tiers » qui rend trois versions d'un même fond. Les trois juges-modèles voient donc des fiches dont la seule variable manipulée est l'ajout explicite d'un champ (antériorité + trou fermé + prédiction changée). Le test mesure si les juges réagissent à un signal de *longueur et de remplissage de champs*, pas à un progrès scientifique. La confondante est la longueur : v₂-augmentée a au moins un paragraphe de plus que v₁ et v₂-paraphrase (une antériorité vérifiée + un trou fermé). Or la course 1 a déjà montré la nécessité de « témoins de longueur comparable » (Pièce 1 § 10 : correction consignée). Si v₂-paraphrase n'est pas allongée d'un contenu neutre de même volume, toute préférence pour v₂-augmentée est attribuable à la longueur, pas au progrès. A ne mentionne aucun appariement de longueur.

**2. E3 (moisson ciblée) mesure la pertinence de la moisson par le vérificateur d'antériorité, qui est lui-même un juge-modèle non calibré.**
La métrique m3 (« part des antériorités nouvelles jugées pertinentes par le vérificateur d'antériorité ») fait du juge de pertinence un instrument de mesure alors que ce juge n'a aucune calibration rapportée. Si le vérificateur marque « pertinente » toute œuvre dont le titre contient un mot de la fiche (ce qui est vrai par construction quand la requête dérive des concepts de la fiche), m3 est identiquement 1 quel que soit le bras. Il n'y a ni contrôle de taux de faux positifs du vérificateur, ni cas où la bonne réponse est « non pertinente » (les cas honnêtes sont tous des antériorités retirées qu'on espère retrouver — tous positifs). L'absence de négatifs vrais empêche de calculer la spécificité de l'instrument.

**3. E4 (regroupement des succès sur données réelles) utilise un graphe de termes, pas de concepts.**
A reconnaît que « des termes ne sont pas des concepts » (Pièce 2, citée dans la table A6), puis propose de mesurer le regroupement sur le même graphe de termes. Si les termes fréquents créent des faux amas (« ball — consistently » est voisin de beaucoup de paires par attachement préférentiel), le facteur ≥ 3 peut être atteint sans regroupement scientifique, juste par artefact de degré. L'appariement sur le degré est mentionné en texte libre mais ne figure pas dans la métrique formelle de H_A (« taux de positives parmi les voisines » sans précision de l'appariement). Si l'appariement n'est pas dans le préenregistrement, il ne peut pas être exigé après.

**4. E5 (bras contre RA) mélange deux domaines sans facteur de blocage.**
A propose de faire tourner les bras sur le graphe d'optique/quantique de Gu-Krenn pour comparer, et en parallèle sur le graphe de contrôle de l'IA. Mais les bras basique et méta sont définis sur des axes et des structures du contrôle de l'IA (six niches, 20 structures, Pièce 1 § 7.3). Ils n'ont aucune table de niches pour l'optique. Donc soit on les applique sans leur table (le test n'est pas celui des bras mais d'une dégradation de ceux-ci), soit on ne les teste que sur le contrôle de l'IA (le comparateur Gu-Krenn n'a pas de vocabulaire pertinent, VÉRIFIÉ Pièce 3 § 5). Le design confond le domaine de définition de chaque méthode.

**5. E6 (fertilité des fusions) est sous-dimensionné et le sait, sans proposer de remède opérationnel.**
A écrit : « ≈ 40 fusions par bras pour un écart de 30 points à puissance 0,8 ». Or la course 2 prévoit 8 par bras (DÉCIDÉ, GO-2026-10-31-04, Pièce 1 § 7.4). Le duel H_A/H_B est donc formellement non réfutable avec les données prévues. Proposer un test dont on sait qu'il n'a pas la puissance nécessaire viole la règle B4 (chaque issue doit falsifier quelque chose) : en pratique, les deux issues seront « non concluant ».

**6. E7 (fuite par la date d'entraînement) n'a pas de vérité terrain.**
A propose de mesurer la part de références post-coupure citées par un modèle. Mais le taux d'hallucination de références (le dénominateur du contrôle) n'est pas une constante du modèle : il dépend du sujet, de la longueur du prompt et de la consigne. Si le taux d'hallucination est de 30 % et que le taux de post-coupure est de 5 %, la différence est noyée dans le bruit. A ne fixe aucun seuil de puissance pour séparer les deux taux, et ne dit pas comment estimer le taux d'hallucination indépendamment (il faudrait un corpus de vérité terrain de références, qui n'est pas dans les faits).

### (b) Conditions de perte de puissance ou de non-jugeabilité

| Expérience | Condition sous laquelle la mesure perd sa puissance | Formulation probabiliste |
|---|---|---|
| E1 | Les juges ont un bruit de préférence (accord de rang 0,12 en course 1, VÉRIFIÉ). Soient $p_{aug}$ et $p_{par}$ les probabilités de préférence pour v₂ dans les deux cas. Si $\sigma_{juge}$ est l'écart-type inter-juges, le test à $n = 28$ fonds et $3$ juges ne sépare $p_{aug} - p_{par}$ que si $p_{aug} - p_{par} > 2\sigma_{juge}/\sqrt{28 \times 3} \approx 0,22\sigma_{juge}$. Avec un accord de 0,12 (quasi-hasard), $\sigma_{juge}$ est proche de $\sqrt{p(1-p)}$ (binomiale), soit $\approx 0,5$, et le seuil minimal détectable est $\approx 0,11$. Le seuil de A est 0,25 : tenable, mais seulement si l'accord ne se dégrade pas davantage avec le format par paires (non mesuré). | Si $\kappa_{juge} \leq 0,05$, la puissance pour détecter 0,25 tombe sous 0,5 (illustratif). |
| E3 | Si le taux de base de « pertinence » du vérificateur est proche de 1 (il marque tout comme pertinent quand le domaine est correct), alors $m3(\gamma) - m3(\beta) \to 0$ par construction. | $P(\text{pertinent} \mid \text{même sous-domaine}) \geq 0,9 \implies$ puissance de la différence $\gamma - \beta$ sur m3 $< 0,2$ pour $n \leq 128$ fiches (illustratif). |
| E4 | Si la distribution des degrés dans le graphe suit une loi de puissance avec exposant $\alpha < 2,5$, les hubs créent des amas artificiels dont le facteur $\geq 3$ est atteint par la structure de degré seule. L'appariement sur le degré est alors le seul test valide, mais A ne l'inscrit pas dans H_A. | $P(\text{facteur} \geq 3 \mid \text{degré apparié, issues permutées}) > 0,05 \implies$ le contrôle négatif échoue et le test n'est pas jugeable. |
| E5 | Le graphe de contrôle de l'IA est petit (moisson : 197 681 œuvres, illustratif : ~10 000 concepts après RAKE). Le nombre de paires non reliées est donc beaucoup plus petit que les 689 millions de Gu-Krenn. Si le taux de base d'apparition post-coupure est $< 0,1\%$ et que le nombre de paires tirées est $< 100\,000$, il y a $< 100$ positives, et la précision à $k = 1000$ n'est pas définie (toutes les 100 positives sont dans les 1000 premiers). | $N_{positives} < k \implies P@k$ non défini ; $N_{positives} < 50 \implies$ aucun intervalle de confiance sur l'AUC n'exclut 0,5 à 95 %. |
| E6 | Déjà traité : $k = 8$ par bras $\implies$ puissance $< 0,15$ pour un écart de 30 points (binomial exact). | $P(\text{rejeter } H_0 \mid \Delta = 0,30, n = 8) < 0,15$. |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **E1** : paires v₁ contre v₁ (mentionné par A — bien). Mais il manque le contrôle « v₂-allongée-neutre » : une version allongée d'un contenu sans rapport scientifique, de même longueur que v₂-augmentée. Sans ce contrôle, aucune séparation entre effet de longueur et effet de progrès.

2. **E3** : la moisson croisée est mentionnée (bien), mais il manque le contrôle « moisson identique » : servir la même moisson ciblée deux fois à la même fiche. Si le proposeur ne change pas sa fiche, le capteur de progrès (E2) doit rendre « aucun changement ». Si le proposeur change quand même, tout progrès mesuré est un artefact de la réécriture.

3. **E5** : le placebo de coupure est mentionné, mais pas le contrôle d'inflation du vivier. Quand on passe de fiche–fiche (8 000 paires illustratif) à fiche–article (25 millions illustratif), le nombre de paires évaluées change de trois ordres de grandeur. Sans rapporter le temps de calcul et le coût par bras dans les deux régimes, il est impossible de savoir si un gain de précision compense le coût ou si le bras simplement classe plus de paires dont la plupart sont triviales.

4. **E7** : il manque le contrôle « même modèle, même prompt, sujet hors coupure ». Si on demande au modèle de citer des références sur un sujet dont il est certain qu'aucun article n'existe après la coupure (par exemple, la mécanique newtonienne pure), le taux de références post-coupure devrait être exactement zéro. Si ce n'est pas le cas, le modèle hallucine des dates futures et le test entier est invalide.

---

## Sur la proposition C

### (a) Défauts de méthode

**1. E1 (Gu-Krenn adapté vs RA en contrôle de l'IA) fusionne extraction de concepts et entraînement du modèle dans une seule comparaison.**
C propose de relancer RAKE sur `cs.LG, cs.AI, cs.CL, cs.CR, stat.ML`, de construire un nouveau graphe, d'entraîner un nouveau réseau, et de comparer à RA. Mais le résultat final dépend de deux facteurs confondus : (i) la qualité de l'extraction RAKE pour le contrôle de l'IA (les seuils 9 et 6 ont été calibrés sur l'optique, Pièce 3 § 0), et (ii) la capacité du réseau à apprendre au-delà de la topologie locale. Si le résultat est $H_B$ (RA gagne), on ne sait pas si c'est parce que RAKE produit de mauvais concepts en contrôle de l'IA ou parce que le réseau n'ajoute rien. Il faut un contrôle intermédiaire : RA calculée sur le même graphe RAKE (ce que C propose dans le protocole), mais aussi une variante avec des concepts extraits par un autre algorithme (par exemple les `concepts` ou `topics` d'OpenAlex eux-mêmes, qui existent déjà dans la moisson). Sans cette ablation, le test ne sépare pas l'extraction du modèle.

**2. E2 (boucle multi-tours vs 1 coup) confond le nombre d'embryons et le nombre de tours.**
Le bras $H_A$ prend 8 embryons à 3 tours = 24 unités. Le bras $H_B$ prend 24 embryons à 1 tour = 24 unités. Puis on compare les 8 meilleures de $H_B$ aux 8 de $H_A$. Mais $H_B$ a un avantage de sélection : il choisit 8 sur 24 (sélection 1/3), alors que $H_A$ garde ses 8 sans sélection. Si les fiches initiales ont une variance de qualité, $H_B$ gagne par le tri, pas par la stratégie de moisson. La confondante est le taux de sélection. Pour isoler l'effet de l'itération, il faudrait soit (i) tirer 8 embryons identiques dans les deux bras et comparer à budget total différent (ce qui confond le coût), soit (ii) tirer 24 dans les deux bras, itérer 3 tours sur les 24 de $H_A$, un tour sur les 24 de $H_B$, puis comparer les 24 survivantes respectives (ce qui triple le coût de $H_A$). C ne discute pas cette confondante.

**3. E3 (fiche–article pour le bras méta) n'a pas de vérité terrain pour « notable et inédite ».**
La métrique est le taux de fusions « notables à l'aveugle et passant l'antériorité ». Mais les juges de « notable » sont des juges-modèles dont l'accord est de 0,12 (VÉRIFIÉ, Pièce 1 § 10), et « passant l'antériorité » dépend du vérificateur Claude qui n'a pas de taux de faux négatifs mesuré (une antériorité existante manquée par Claude est comptée comme « inédite »). La combinaison de deux instruments non calibrés ne produit pas un instrument calibré. La mesure est vraie par construction si les juges marquent « notable » ce qui est long et si Claude ne trouve pas les antériorités des articles moissonnés (qui sont récents et possiblement absents de sa base de recherche).

**4. Le coût de E1 est sous-estimé par un facteur qui dépend du volume de la moisson complémentaire.**
C estime la remoisson des résumés et citations à 0,40 USD et 35 min. Mais la moisson en vrac initiale porte sur 197 681 œuvres en cinq sous-domaines (VÉRIFIÉ). Pour construire un graphe à la Gu-Krenn sur le contrôle de l'IA, il faut moissonner non pas les 197 681 œuvres déjà connues, mais **tous les articles de revue avec résumé dans ces domaines**, y compris ceux publiés entre 2015 et la coupure. Le volume est inconnu (I-1, Pièce 3 § 7), et les 197 681 œuvres ne sont probablement qu'une fraction. C ne distingue pas les deux moissons et le coût de la seconde est absent du tableau.

**5. L'anonymisation par isomorphisme de graphe (Q5) ne détruit pas la mémoire sémantique d'un LLM.**
C propose de remplacer les noms de concepts par des symboles `C_001` pour empêcher le rappel mémoriel. Mais un LLM voit aussi les *relations* entre concepts (voisinage, co-citations, structure du sous-graphe), qui sont elles-mêmes caractéristiques et pourraient être reconnues. Plus fondamentalement, c'est le *proposeur* qui génère les fiches : si on anonymise les concepts pour le proposeur, il ne peut plus raisonner sur le contenu scientifique et la qualité de ses fiches s'effondre. L'anonymisation ne fonctionne que pour un appariement purement topologique (sans LLM), ce qui revient à la rétrodiction algorithmique déjà proposée par C sous un autre nom.

### (b) Conditions de perte de puissance ou de non-jugeabilité

| Expérience | Condition |
|---|---|
| E1 | Le graphe RAKE du contrôle de l'IA est beaucoup plus petit que celui de l'optique (37 960 concepts). Si le nombre de concepts extraits est $< 5\,000$ (illustratif), le nombre de paires non reliées est $< 12,5$ millions, et avec un taux de base $< 0,1\%$, il y a $< 12\,500$ positives. Le banc de Gu-Krenn utilise 1 million de paires avec $\sim 1\,000$ positives par IR. Si le taux de base en contrôle de l'IA est 10× plus bas qu'en optique, il faut 10× plus de paires pour la même puissance, ce qui peut dépasser la mémoire disponible. |
| E2 | Avec 8 embryons par bras et un seuil de +2 survivantes sur 8 (soit +25 points), la puissance pour détecter un vrai effet de 25 points est $\approx 0,65$ (binomial exact, illustratif). Pour un effet plus réaliste de 12,5 points (1 survivante de différence), la puissance tombe à $\approx 0,25$. Le test est probablement non concluant. |
| E3 | Le taux de déclenchement sans repli du bras méta ($\geq 7/8$) est un seuil binomial : avec $n = 8$ lots, la probabilité de mesurer $\geq 7$ si la vraie probabilité est 0,80 (l'estimation de l'annexe brouillon 4 avec 26 entités, à la bande [2;4]) est $\approx 0,50$. Le test est à pile ou face. |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **E1** : il manque le contrôle « RA calculée sur les concepts d'OpenAlex plutôt que sur les concepts RAKE ». Si RAKE extrait des concepts erronés (faux bigrammes, homonymes), le graphe est bruité et toute comparaison avec RA (qui utilise le même graphe bruité) mesure le bruit, pas le modèle.

2. **E2** : il manque le contrôle « 8 embryons identiques sans moisson, 3 tours de réécriture libre ». Si le proposeur améliore ses fiches par auto-critique sans aucune moisson (il réécrit trois fois), et que le résultat est aussi bon que $H_A$, alors le gain vient de la réécriture, pas de la moisson. Le « bras Boucle Placebo » de C est un début, mais il ne sépare pas « moisson placebo + 3 tours » de « aucune moisson + 3 tours ».

3. **E3** : il manque un contrôle de plagiat explicite. C mentionne le risque que « le proposeur plagie l'article apparié », mais ne propose pas de mesure du taux de plagiat (par exemple, Jaccard du texte de la fusion avec le résumé de l'article apparié, seuil à fixer). Sans cette mesure, le taux de « notables » peut être gonflé par des fusions qui recopient l'article.

---

## Sur la proposition D

### (a) Défauts de méthode

**1. E1 (état versionné) est circulaire si le « diff structuré » qui définit le progrès est aussi l'instrument à mesurer.**
D définit quatre types de progrès (fermeture de trou, modification de prédiction, réfutation, traduction en loi). Puis E1 teste si l'« état versionné » les détecte mieux que les différences mécaniques. Mais l'état versionné *est* le quadruplet (antériorités, prédiction, trous, pièces) dont les changements définissent le progrès. Si le progrès est défini comme « changement d'un champ du quadruplet » et que le capteur mesure « changement d'un champ du quadruplet », le capteur est parfait par construction. Le test ne devient non trivial que si les paraphrases peuvent changer un champ sans vraie avancée (par exemple, renommer un trou en le reformulant). D mentionne les « paraphrases, permutations, renommages et ajouts de citations sans effet » comme cas négatifs, mais ne précise pas comment distinguer mécaniquement un renommage de trou d'une fermeture de trou — or c'est exactement le cœur du problème. Si le « trou explicitement nommé » change de nom entre v₁ et v₂ mais que sa substance est la même, le diff structuré voit un changement et le compte comme progrès. La vérité terrain est absente.

**2. E2 (moisson ciblée apporte-t-elle quelque chose ?) ne sépare pas « volume de la moisson » de « ciblage de la moisson ».**
D compare moisson ciblée au « meilleur de {sans moisson, antériorités seules, recherche lexicale} ». Mais « antériorités seules » et « recherche lexicale » sont deux moissons non ciblées de volumes différents. Si la moisson ciblée ramène 20 résumés et que la recherche lexicale en ramène 5, un gain de la ciblée peut venir du volume. D ne fixe pas le nombre de résultats par bras. Le seuil « +2 points de précision en tête, à coût total non supérieur » contrôle le coût mais pas le volume d'information (nombre de résumés × longueur).

**3. E5 (la rétrodiction prédit-elle une survie expérimentale ?) suppose que la survie expérimentale est elle-même un signal fiable, ce qui n'est pas établi.**
La survie aux tests de mort est « codée, jamais activée » (VÉRIFIÉ). La couche 1 sur banque réelle n'a « pas de dents » (0 témoin vrai promu sur 20, VÉRIFIÉ). Si le test de mort n'a pas de puissance (il ne promeut rien), alors l'AUC de survie est calculée sur un ensemble vide de positives et n'est pas définie. D le reconnaît dans sa table (« le "pas de dents" sur banque réelle est OBSERVÉ-NON-AUDITÉ et doit être reproduit avant usage comme endpoint »), mais l'expérience E5 est formulée comme si la survie était un endpoint disponible. Ce n'est pas un défaut de la proposition en tant que design, mais c'est une condition préalable non remplie dont l'absence rend E5 non jugeable dans l'immédiat — et D ne propose pas de chemin explicite pour la remplir avant de lancer E5.

**4. E4 (bandit ou uniforme) n'a pas de confondante contrôlée pour le choix des récompenses.**
D écrit : « récompense : uniquement des transitions admissibles disponibles avant l'issue future ; l'évaluation finale reste scellée ». Mais la récompense « transition admissible » est exactement le capteur de progrès de E1, dont D dit lui-même qu'il peut être vrai par construction (voir point 1 ci-dessus). Si le capteur de progrès est circulaire, la récompense du bandit l'est aussi, et le bandit optimise une quantité non informative. Le contrôle « récompenses permutées » (mentionné) ne détecte pas cette circularité : il détecte seulement si la récompense non permutée a une structure quelconque, pas si cette structure mesure un progrès réel.

**5. L'« option manquante » (criblage uniforme puis bandit sur les embryons ayant franchi E1) crée un biais de sélection non contrôlé.**
Les embryons qui franchissent E1 sont ceux dont l'état versionné change (c'est la définition de E1). Si seuls ceux-là reçoivent le bandit, le bandit ne voit que des embryons qui ont déjà changé une fois — c'est un échantillon conditionné. Les embryons dont le premier tour ne change rien (peut-être parce qu'ils étaient déjà bons) sont exclus. D ne propose pas de contrôle pour ce biais de survivant.

### (b) Conditions de perte de puissance ou de non-jugeabilité

| Expérience | Condition |
|---|---|
| E1 | Si les paraphrases sont générées par un LLM de la même famille que les proposeurs, le diff structuré peut apprendre les artefacts du LLM plutôt que la structure du progrès. Formellement : si $P(\text{changement de champ} \mid \text{paraphrase LLM}) > 0,3$ (illustratif), alors le taux de fausses alertes dépasse 5 % et le seuil de 80 % de détection à 5 % de FA n'est pas atteignable. |
| E2 | Si le taux de base d'apparition post-coupure est très faible dans le domaine du contrôle de l'IA ($< 0,05\%$, illustratif), alors même +2 points de précision en tête repose sur $< 20$ paires positives (sur 10 000 en tête), et l'intervalle de confiance est de l'ordre de ±5 points (Wilson). Le seuil est dans le bruit. |
| E3 | Si RA, Simpson et attachement préférentiel ont des performances indiscernables entre elles (comme dans la rétrodiction Swanson où S, AA, CN sont à ±1 point, VÉRIFIÉ Pièce 2), alors la correction de multiplicité pour trois bras × trois témoins (9 comparaisons) rend tout intervalle non significatif avec les tailles d'échantillon envisageables. |
| E5 | Voir point 3 ci-dessus : si le nombre de survivantes aux tests de mort est 0 (comme en couche 1), l'AUC n'est pas définie. Plus généralement, si $P(\text{survie}) < 0,02$ (illustratif), il faut $> 500$ fiches soumises pour avoir $\geq 10$ positives, ce qui excède la course 2 entière (128 fiches, RAPPORTÉ). |
| E6 | Le seuil de +25 % de survivantes par euro exige un effet multiplicatif de 1,25. Si le nombre absolu de survivantes est $< 5$ dans chaque bras (ce qui est probable vu le point précédent), la différence minimale détectable est de 1 survivante, soit 20 % ou 33 % selon le dénominateur. Le test est au voisinage de son seuil sans puissance pour le franchir avec confiance. |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **E1** : D ne mentionne pas de contrôle pour le cas où la vérité terrain elle-même est ambiguë. Les « vraies fermetures de trous » sont jugées telles par qui ? Si c'est par un annotateur humain (Lazar), il y a un seul annotateur et pas de mesure d'accord inter-annotateur. Si c'est mécanique (le champ `Statut du trou` passe de `Ouvert` à `Fermé par réf. X`), alors le test est trivial (voir point 1). Il faut au minimum des cas où le statut du trou est contesté entre deux lecteurs indépendants, et mesurer la concordance.

2. **E3** : D propose « structures mélangées » et « monde sans regroupement » comme contrôles, mais ne propose pas de contrôle de la normalisation des scores entre types de paires. Si le score du bras basique sur fiche–fiche a une distribution $\mathcal{N}(\mu_1, \sigma_1)$ et sur fiche–article une distribution $\mathcal{N}(\mu_2, \sigma_2)$ avec $\sigma_2 \gg \sigma_1$ (parce que les articles ont des champs de domaine plus variés), alors le classement mixte favorise les paires fiche–article par excès de variance, pas par qualité. Il manque un contrôle de calibration des scores entre types de paires (par exemple, vérifier que le rang percentile d'un score donné correspond au même taux de base dans les deux populations).

3. **E6** : D requiert « témoins vrais/faux non tautologiques ». Mais la seule banque non tautologique ayant tourné est la couche 1, qui n'a « pas de dents ». Si les témoins vrais du monde non tautologique ne sont pas promus non plus, le contrôle négatif fonctionne (les faux ne passent pas) mais le contrôle positif échoue (les vrais ne passent pas non plus), et le test est non jugeable. D ne propose pas de procédure pour construire des témoins vrais qui passent effectivement, ce qui est pourtant le prérequis de la mesure.

FIN-DE-CELLULE
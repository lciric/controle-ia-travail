**État des pièces transmises :** le bloc `FAITS` est strictement identique au bloc `QUESTION DE L'ARBITRE` (même empreinte SHA-256) ; les notes annoncées comme retirées, la réponse 23 de Fable et toute donnée empirique sont absentes.

---

# Proposition F — Tour III.1 : Audit méthodologique du lot en quarantaine

Tous les éléments décrits dans l'énoncé (présence de détecteurs, cycles non bornés, détention d'un lot non consulté noté $Q$, changement d'affirmations vers (i) et (ii)) ont ici le statut **`RAPPORTÉ`** et non vérifié.

---

## 1. Réponses aux quatre questions de l'arbitre

### Question 1 — À quoi le lot $Q$ peut-il servir ?

- **Position :** Principalement à **délimiter la portée de ce que l'équipe affirme** — et non comme critère de passage dans la boucle itérative. Plus précisément, $Q$ sert à tester si l'écart à la loi publiée (i) et la valeur ajoutée du détecteur interne sur le détecteur texte (ii) survivent à un saut hors des genres de dégradation vus pendant les cycles (estimation de l'écart de généralisation hors-genre). Il ne peut jouer un rôle de **verrou de passage** qu'en sortie unique après gel définitif, jamais comme condition d'arrêt d'un nombre non fixé de cycles : sinon l'arrêt optionnel et la rétroaction adaptative gonflent le score sur $Q$ et détruisent sa fonction de mesure de portée. Il peut enfin ne servir **à rien** pour (i) si le genre de $Q$ sort du domaine de validité de la loi publiée, ou pour (i) et (ii) si $Q$ manque de cas honnêtes appariés ou de puissance statistique.
- **Énoncé réfutable et grandeur mesurée :** *« Utiliser $Q$ (ou un ensemble analogue) comme critère d'arrêt au fil de cycles non fixés surestime les grandeurs de (i) et (ii) par rapport à un genre jamais interrogé, tandis que son usage en audit final unique borne sans biais la portée sur ce genre. »* On mesure l'écart de généralisation $\Delta_{\text{gen}}$ entre la métrique atteinte à l'arrêt sur le lot consulté et la métrique mesurée sur un lot d'un genre indépendant jamais interrogé (en perte logarithmique propre et en taux de détection à taux de fausses alertes fixé).
- **Antériorité la plus proche :** Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., & Roth, A. (2015), « The reusable holdout: Preserving validity in adaptive data analysis » (*Science*) pour l'invalidation d'un holdout par requêtes adaptatives ; et Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002), *Experimental and Quasi-Experimental Designs for Generalized Causal Inference* pour la séparation entre validité interne et portée externe (*tous deux cités de mémoire*).
- **Contrôle indépendant de tout avis :** Exécuter exactement la même boucle d'optimisation et la même règle d'arrêt optionnel sur une copie de $Q$ dont les étiquettes sont permutées aléatoirement (signal vrai nul), puis mesurer le score du détecteur arrêté sur un échantillon frais indépendant : un excès de score au-delà de la borne binomiale fixée démontre mécaniquement le biais du critère de passage sans jugement humain.
- **Niveau de confiance subjectif :** Élevé — crédence subjective $0{,}85$ `(illustratif)` sur le diagnostic méthodologique (sous réserve que $Q$ contienne des cas honnêtes appariés).

### Question 2 — Quand consulter $Q$ ?

- **Position :** **Une seule fois**, après gel cryptographique des deux détecteurs, de leur règle de combinaison, des seuils de décision, de la loi publiée de référence et du plan d'analyse statistique. L'énoncé rapporte que $Q$ regroupe des cas *« d'un genre »* (au singulier) : consulter $Q$ **par parties** sur un même genre révèle ce genre dès la première partie et contamine la validité hors-genre des parties restantes (fuite au niveau de la famille). La consultation **par parties** n'est recevable (**autrement**) que si $Q$ est réellement partitionnable *a priori* en **genres distincts et indépendants**, chaque genre n'étant ouvert qu'une seule fois avec dépense d'erreur $\alpha$ prédéfinie et déclassement immédiat de tout genre ouvert. Consulter **à chaque cycle** invalide la mesure sous arrêt optionnel ; ne **jamais** le consulter reste préférable uniquement si $Q$ est hors du domaine de (i) et trop petit pour tester (ii) avec une puissance non triviale.
- **Énoncé réfutable et grandeur mesurée :** *« Si $Q$ appartient à un genre unique, ouvrir une fraction $Q_1$ et adapter les détecteurs avant d'évaluer $Q_2$ crée un avantage artificiel sur $Q_2$ qui disparaît sur un genre indépendant $Q_{\text{ext}}$. »* On mesure la fuite intra-genre $\Delta_{\text{intra}} = M(Q_2) - M(Q_{\text{ext}})$ (où $M$ est la perte logarithmique ou l'AUROC appariée) en comparaison avec un détecteur gelé avant toute ouverture.
- **Antériorité la plus proche :** Klein, J. R., & Roodman, A. (2005), « Blind Analysis in Nuclear and Particle Physics » (*Annual Review of Nuclear and Particle Science*) pour l'ouverture unique après gel ; Lan, K. K. G., & DeMets, D. L. (1983), « Discrete sequential boundaries for clinical trials » (*Biometrika*) pour la consultation séquentielle par parties à erreur contrôlée ; Blum, A., & Hardt, M. (2015), « The Ladder: A Reliable Leaderboard for Machine Learning Competitions » pour les bornes d'accès répété (*tous cités de mémoire*).
- **Contrôle indépendant de tout avis :** Contrôle automatisé d'horodatage et d'empreintes : le script d'audit vérifie mécaniquement que l'horodatage de déchiffrement de $Q$ est strictement postérieur au dépôt immuable des empreintes SHA-256 du code, des poids, des prompts, des seuils et du script d'analyse. Si l'inégalité échoue, le statut confirmatoire est rejeté automatiquement.
- **Niveau de confiance subjectif :** Élevé — crédence subjective $0{,}85$ `(illustratif)` pour le régime à genre unique ; modéré ($0{,}65$ `(illustratif)`) quant à l'applicabilité pratique d'une partition par sous-genres sans connaître la structure réelle de $Q$.

### Question 3 — Si des auteurs de détecteurs l'ont vu, en tout ou en partie ?

- **Position :** **Cela dépend de trois éléments nommables et vérifiables :** (1) **la chronologie** par rapport au gel des détecteurs et des seuils (une vue post-gel est causalement déconnectée des artefacts déjà gelés) ; (2) **la granularité de l'exposition** (cas individuels, nature du genre, ou simple score agrégé — voir le genre d'une seule partie suffit à compromettre l'isolation hors-genre de tout le lot du même genre) ; (3) **la symétrie d'exposition entre le détecteur interne et le détecteur texte** (pour la revendication (ii), une fuite asymétrique en faveur d'un seul détecteur fausse directement l'estimation de valeur ajoutée). Dès qu'une exposition au genre ou aux cas précède un changement de code, de poids, de prompt ou de seuil, il faut **déclasser** $Q$ en banc de développement ou de régression non aveugle (sans le **jeter** s'il reste utile pour du débogage, sauf défaut de construction) et **refaire** un lot isolé produit par une équipe cloisonnée pour soutenir toute portée hors-genre.
- **Énoncé réfutable et grandeur mesurée :** *« Une exposition pré-gel d'au moins un auteur à tout ou partie de $Q$ augmente le score des détecteurs (ou déplace l'écart interne vs texte) sur $Q$ par rapport à un lot frais $Q_{\text{post}}$ du même genre généré après le gel. »* On mesure l'écart de contamination $\Delta_{\text{fuite}} = M(Q_{\text{vu}}) - M(Q_{\text{post}})$ et la dérive d'asymétrie $\Delta_{\text{asym}} = \Delta\text{NLL}(Q_{\text{vu}}) - \Delta\text{NLL}(Q_{\text{post}})$, étalonnés par un détecteur témoin gelé avant la création de $Q$.
- **Antériorité la plus proche :** Kaufman, S., Rosset, S., Perlich, C., & Stitelman, O. (2012), « Leakage in data mining: Formulation, detection, and avoidance » (*ACM Transactions on Knowledge Discovery from Data*) pour la taxonomie et la détection de fuite de données ; Schulz, K. F., & Grimes, D. A. (2002), « Blinding in randomised trials: hiding who got what » (*The Lancet*) pour l'effet d'un bris d'aveugle asymétrique (*tous deux cités de mémoire*).
- **Contrôle indépendant de tout avis :** Audit automatisé croisant les journaux d'accès en lecture (stockage WORM / gestionnaire de clés) avec l'historique Git signé (SHA-256/GPG) des détecteurs ; en complément, si les journaux sont incomplets, test statistique automatisé comparant les scores des détecteurs gelés sur $Q$ contre un lot $Q_{\text{post}}$ horodaté après le gel, calibré par un vérificateur témoin antérieur à $Q$.
- **Niveau de confiance subjectif :** Élevé — crédence subjective $0{,}80$ `(illustratif)` sur la règle de décision ; plus faible ($0{,}55$ `(illustratif)`) sur la capacité à exclure une fuite mineure par le seul test statistique si la taille de $Q$ est petite.

### Question 4 — Le changement de ce que l'équipe affirme modifie-t-il ces réponses ?

- **Position :** **En partie.**
  - *Ce qui ne change pas :* la mécanique de biais adaptatif sous cycles non bornés (Q2) et l'invalidité d'une exposition pré-gel (Q3) valent autant pour (i) et (ii) que pour « un détecteur est bon en soi ».
  - *Ce qui change :*
    1. **Alignement avec la loi publiée (i) :** sous « bon en soi », tout genre inédit testait la robustesse. Sous (i), $Q$ n'est pertinent pour tester l'écart à la loi que si son genre appartient au domaine opérationnel où la loi publiée prétend s'appliquer ; sinon $Q$ teste une extrapolation hors domaine (ce qui modifie Q1 et peut justifier de ne pas utiliser $Q$ pour (i)).
    2. **Symétrie et contraste apparié pour (ii) :** la grandeur cible n'est plus une performance absolue mais un gain incrémental conditionnel (interne ajouté au texte). Cela rend critique la parité d'optimisation entre les deux détecteurs, l'appariement de cas honnêtes (sans lesquels la calibration et le faux positif hors-genre sont indéfinis), et fait de la **symétrie d'exposition** (Q3) un facteur de biais décisif qui n'existait pas pour un détecteur isolé.
    3. **Risque de déplacement d'hypothèse (HARKing) :** comme l'affirmation a changé *après* la constitution de $Q$ (`RAPPORTÉ`), il faut prouver mécaniquement que ce changement n'a pas été informé par $Q$ et pré-enregistrer (i) et (ii) avant ouverture.
- **Énoncé réfutable et grandeur mesurée :** *« Le passage de la performance absolue aux affirmations (i) et (ii) modifie la validité de $Q$ : un détecteur interne peut perdre toute valeur ajoutée conditionnelle $\Delta\text{NLL}$ sur $Q$ même s'il conserve une AUROC marginale élevée, et une exposition asymétrique d'un seul auteur fausse le signe ou l'amplitude de $\Delta\text{NLL}$. »* On mesure séparément la performance marginale de chaque détecteur, le gain incrémental calibré $\Delta\text{NLL}(\text{texte}+\text{interne} \text{ vs } \text{texte})$, et la sensibilité de $\Delta\text{NLL}$ à un déséquilibre d'optimisation ou d'exposition.
- **Antériorité la plus proche :** Kerr, N. L. (1998), « HARKing: Hypothesizing After the Results are Known » (*Personality and Social Psychology Review*) et Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018), « The preregistration revolution » (*PNAS*) pour la modification d'hypothèse avant/après analyse ; Pencina, M. J., D'Agostino, R. B., Sr., D'Agostino, R. B., Jr., & Vasan, R. S. (2008), « Evaluating the added predictive ability of a new marker: From area under the ROC curve to reclassification and beyond » (*Statistics in Medicine*) et DeLong, E. R., DeLong, D. M., & Clarke-Pearson, D. L. (1988), « Comparing the Areas under Two or More Correlated Receiver Operating Characteristic Curves: A Nonparametric Approach » (*Biometrics*) pour l'évaluation d'un apport incrémental corrélé (*tous cités de mémoire*).
- **Contrôle indépendant de tout avis :** (1) Vérification automatisée que l'empreinte SHA-256 du pré-enregistrement spécifiant la loi publiée exacte, son domaine, le protocole de combinaison interne+texte et les seuils précède tout accès à $Q$ ; (2) test de randomisation conditionnelle (*conditional randomization test*) permutant les scores internes à l'intérieur des quantiles de scores textuels pour décider mécaniquement si l'apport incrémental excède le bruit au seuil $\alpha$ pré-enregistré.
- **Niveau de confiance subjectif :** Élevé — crédence subjective $0{,}85$ `(illustratif)`.

---

## 2. Livrable (a) — Ce que la question suppose sans que ce soit établi

Le tableau ci-dessous recense les présupposés implicites de la question et leur statut épistémique strict.

| # | Présupposé contenu ou impliqué par la question | Statut | Conséquence s'il est faux |
|---|---|---|---|
| A1 | Les « cas de dégradation discrète » disposent d'une vérité terrain reproductible et échappent aux vérifications mécaniques simples (tests, linters, invariants). | `HYPOTHÈSE` | Les détecteurs neuronaux mesurent du bruit d'étiquetage ou réinventent à grands frais une vérification déterministe. |
| A2 | Le lot $Q$ contient aussi (ou est associé à) des **cas honnêtes appariés** ; l'énoncé ne mentionne que des « cas de dégradation ». | `HYPOTHÈSE` | Sans cas honnêtes appariés, le taux de fausses alertes hors-genre, la calibration et la valeur ajoutée (ii) ne sont pas mesurables sur $Q$. |
| A3 | Le genre de $Q$ est structurellement distinct des genres vus en développement (pas une simple reformulation lexicale), tout en restant dans le domaine de validité de la loi publiée (i). | `HYPOTHÈSE` | Si trop proche : fausse généralisation. Si hors domaine de la loi : $Q$ ne peut ni confirmer ni réfuter (i). |
| A4 | Les auteurs des détecteurs n'ont consulté ni $Q$ ni aucune information sur son genre. | `OBSERVÉ-NON-AUDITÉ` | Contamination silencieuse invalidant la portée hors-genre (et biaisant (ii) si l'exposition est asymétrique). |
| A5 | Le changement d'affirmations vers (i) et (ii) a eu lieu sans information issue de $Q$. | `OBSERVÉ-NON-AUDITÉ` | Risque de HARKing : le test de (i) et (ii) sur $Q$ cesse d'être confirmatoire. |
| A6 | La « loi déjà publiée » de (i) est transposable sans ambiguïté d'unités, de métriques et de protocole aux longues tâches de l'agent étudié. | `HYPOTHÈSE` | Un écart apparent peut n'être qu'un désaccord de définition ou d'implémentation. |
| A7 | Le détecteur texte est optimisé avec un budget, un accès aux données et une qualité d'ingénierie comparables à ceux du détecteur interne. | `HYPOTHÈSE` | Si le détecteur texte est sous-optimisé (homme de paille), l'apport mesuré de l'état interne en (ii) est un artefact. |
| A8 | L'accès aux états internes de l'agent est techniquement possible sans perturber son comportement et porte un signal non redondant avec la trace textuelle. | `HYPOTHÈSE` | Impossible sur un modèle fermé sans accès aux activations ; signal potentiellement nul ou pur proxy de longueur/entropie. |
| A9 | Le critère chiffré de passage prédit réellement l'aptitude à passer à l'étape suivante malgré un nombre de cycles non fixé. | `HYPOTHÈSE` | Arrêt optionnel biaisé : passage déclenché sur un pic aléatoire de validation. |
| A10 | La taille de $Q$ (en nombre de tâches indépendantes) procure une puissance statistique suffisante pour trancher (i) et (ii) à faible taux de fausses alertes. | `HYPOTHÈSE` | Résultats non concluants (intervalles de confiance trop larges pour distinguer un effet réel de zéro). |

---

## 3. Livrable (b) — Expériences décisives en inférence forte ($H_A$ contre $H_B$)

Conformément à la règle B4, chaque expérience oppose deux hypothèses mutuellement exclusives et précise ce qui falsifie chacune. Tous les seuils numériques sont marqués `(illustratif)`.

### Expérience E1 — Biais d'arrêt adaptatif et fuite intra-genre (tranche Q1 et Q2)

- **$H_A$ :** Consulter un lot (ou une partie d'un genre unique) au fil de cycles non fixés pour guider les détecteurs ou déclencher le critère de passage introduit un biais adaptatif (et une fuite intra-genre) qui surestime la performance par rapport à un genre inédit.
- **$H_B$ :** Dans le protocole réel de l'équipe, la consultation itérative ou partielle laisse l'estimation sur la fraction restante et sur un genre inédit non biaisée à l'erreur d'échantillonnage près.
- **Dispositif (hors vraie quarantaine) :** Construire deux familles disjointes de dégradations discrètes $F_1$ et $F_2$ (chacune appariée à des tâches honnêtes), partitionner $F_1 = F_{1a} \sqcup F_{1b}$, exécuter la vraie boucle de cycles jusqu'à l'arrêt sur $F_{1a}$, puis évaluer le détecteur arrêté sur $F_{1b}$ (même genre) et $F_2$ (genre distinct) ; croiser symétriquement $F_1 \leftrightarrow F_2$.
- **Métrique :** Écart d'arrêt $\Delta_{\text{gen}} = \text{AUROC}(F_{1a}) - \text{AUROC}(F_2)$ et fuite intra-genre $\Delta_{\text{intra}} = \text{AUROC}(F_{1b}) - \text{AUROC}(F_2)$ (moyennés sur les deux sens $F_1 \leftrightarrow F_2$).
- **Seuil :** $\Delta_{\text{gen}} > 0{,}05$ `(illustratif)` ou $\Delta_{\text{intra}} > 0{,}05$ `(illustratif)` avec borne inférieure de l'intervalle de confiance à $95\,\%$ `(illustratif)` $> 0$ (bootstrap par blocs de tâches).
- **Contrôle négatif :** (1) Même évaluation avec un détecteur gelé avant tout cycle (doit donner $|\Delta_{\text{gen}}| \le 0{,}02$ `(illustratif)` en moyenne symétrique) ; (2) boucle complète sur étiquettes permutées de $F_{1a}$ pour quantifier le biais pur d'arrêt optionnel.
- **Falsification :**
  - *Falsifie $H_B$ :* $\Delta_{\text{gen}} > 0{,}05$ `(illustratif)` ou $\Delta_{\text{intra}} > 0{,}05$ `(illustratif)` (IC $95\,\%$ `(illustratif)` $> 0$) sur la moyenne croisée, alors que le contrôle gelé reste dans $\pm 0{,}02$ `(illustratif)`.
  - *Falsifie $H_A$ :* $|\Delta_{\text{gen}}| \le 0{,}02$ `(illustratif)` et $|\Delta_{\text{intra}}| \le 0{,}02$ `(illustratif)` avec borne supérieure de l'IC $< 0{,}05$ `(illustratif)` sur plusieurs réplications de la boucle complète, prouvant que la régularisation ou le faible nombre effectif de cycles empêche la sur-adaptation dans ce régime.

### Expérience E2 — Écart structurel à la loi publiée vs artefact de domaine/sur-ajustement (tranche (i))

- **$H_A$ :** L'écart mesuré vis-à-vis de la loi publiée $f_{\text{pub}}(x)$ persiste sur le lot en quarantaine $Q$ (préalablement vérifié conforme au domaine de $f_{\text{pub}}$) et traduit un phénomène structurel non réductible aux genres d'entraînement.
- **$H_B$ :** L'écart observé en développement est un artefact de sur-ajustement aux genres vus ou d'implémentation ; sur $Q$ (une fois le protocole de référence calibré), les mesures rentrent dans la bande de prédiction de $f_{\text{pub}}(x)$.
- **Dispositif :** Pré-enregistrement de l'équation de $f_{\text{pub}}(x)$, de sa variance publiée $\sigma^2_{\text{pub}}$ et des critères d'appartenance au domaine. Évaluation en une seule passe des détecteurs gelés sur : (1) un banc de réplication exacte du protocole publié, (2) le jeu de validation des genres vus, (3) le lot $Q$ (avec témoins honnêtes appariés).
- **Métrique :** Résidu standardisé $Z_Q = (\hat{\theta}_Q - f_{\text{pub}}(x_Q)) / \sqrt{\widehat{\text{Var}}(\hat{\theta}_Q) + \sigma^2_{\text{pub}}}$ et rapport de persistance $R = |\hat{\theta}_Q - f_{\text{pub}}(x_Q)| / |\hat{\theta}_{\text{dev}} - f_{\text{pub}}(x_{\text{dev}})|$.
- **Seuil :** Contrôle de réplication $|Z_{\text{répl}}| \le 1{,}5$ `(illustratif)` ; persistance si $|Z_Q| > 2{,}5$ `(illustratif)` de même signe que $Z_{\text{dev}}$ et $R \ge 0{,}50$ `(illustratif)`.
- **Contrôle négatif :** Banc de réplication du protocole publié. Si $|Z_{\text{répl}}| > 1{,}5$ `(illustratif)`, l'expérience est invalidée pour biais d'implémentation de la métrique avant toute conclusion sur $Q$.
- **Falsification :**
  - *Falsifie $H_A$ :* Contrôle de réplication validé et $|Z_Q| \le 1{,}5$ `(illustratif)` (ou signe opposé à $Z_{\text{dev}}$, ou $R < 0{,}25$ `(illustratif)`).
  - *Falsifie $H_B$ :* Contrôle de réplication validé, $|Z_Q| > 2{,}5$ `(illustratif)` de même signe que $Z_{\text{dev}}$ et $R \ge 0{,}50$ `(illustratif)`.

### Expérience E3 — Valeur ajoutée hors-genre de l'état interne sur le texte (tranche (ii))

- **$H_A$ :** Sur le genre inédit $Q$ (avec cas honnêtes appariés), l'ajout du détecteur interne $S_{\text{int}}$ à un détecteur texte optimisé à budget égal $S_{\text{txt}}$ améliore strictement la prédiction calibrée et la détection à faible taux de fausses alertes.
- **$H_B$ :** Hors des genres vus en développement, $S_{\text{int}}$ est redondant avec $S_{\text{txt}}$ (ou avec des descripteurs mécaniques simples de trajectoire) ou dégrade la calibration.
- **Dispositif :** Entraînement à budget égal de $S_{\text{txt}}$ et $S_{\text{int}}$ sur les mêmes genres de développement ; ajustement et gel préalables de deux modèles calibrés $h(S_{\text{txt}})$ et $g(S_{\text{txt}}, S_{\text{int}})$ (ainsi que $g_{\text{méc}}(S_{\text{txt}}, X_{\text{méc}})$ où $X_{\text{méc}}$ regroupe longueur, latence, nombre d'appels d'outils et entropie des jetons). Ouverture unique de $Q$.
- **Métrique :** Gain de perte logarithmique propre $\Delta\text{NLL} = \text{NLL}(h) - \text{NLL}(g)$ (métrique principale), plus $\Delta\text{TPR}@\text{FPR}=5\,\%$ `(illustratif)` et p-valeur d'un test de randomisation conditionnelle de $S_{\text{int}}$ à quantiles de $S_{\text{txt}}$ fixés.
- **Seuil :** $\Delta\text{NLL} > 0{,}03\text{ nats}$ `(illustratif)`, $p < 0{,}01$ `(illustratif)`, $\Delta\text{TPR}@\text{FPR}=5\,\% \ge +5\text{ points}$ `(illustratif)` (dérive de $\text{FPR} \le +1\text{ point}$ `(illustratif)`), ET $\text{NLL}(g) < \text{NLL}(g_{\text{méc}}) - 0{,}02\text{ nats}$ `(illustratif)`.
- **Contrôle négatif :** (1) Activations internes permutées entre trajectoires de même quantile de $S_{\text{txt}}$ et même longueur (doit donner $\Delta\text{NLL} \le 0$ `(illustratif)`) ; (2) modèle $g_{\text{méc}}(S_{\text{txt}}, X_{\text{méc}})$ vérifiant que $S_{\text{int}}$ ne capture pas seulement des statistiques mécaniques triviales.
- **Falsification :**
  - *Falsifie $H_A$ :* $\Delta\text{NLL} \le 0{,}01\text{ nats}$ `(illustratif)`, ou $p \ge 0{,}05$ `(illustratif)`, ou $g_{\text{méc}}$ égale ou bat $g$.
  - *Falsifie $H_B$ :* Tous les seuils ci-dessus sont franchis simultanément tandis que le contrôle par activations permutées reste centré sur $\le 0$ `(illustratif)`.

### Expérience E4 — Impact fonctionnel d'une exposition connue ou suspectée à $Q$ (tranche Q3)

- **$H_A$ :** L'exposition d'auteurs à tout ou partie de $Q$ avant le gel a biaisé la performance absolue ou l'écart interne vs texte sur $Q$.
- **$H_B$ :** L'exposition n'a induit aucun biais mesurable (ex. exposition post-gel ou sans transfert exploité dans les artefacts gelés).
- **Dispositif :** Production par une équipe cloisonnée d'un lot frais $Q_{\text{post}}$ du *même genre* que $Q$, horodaté strictement après le gel cryptographique des détecteurs, apparié en difficulté et en cas honnêtes aux cas exposés $Q_{\text{vu}}$.
- **Métrique :** Écart de contamination $\Delta_{\text{fuite}} = \text{AUROC}(Q_{\text{vu}}) - \text{AUROC}(Q_{\text{post}})$ pour chaque détecteur, et dérive d'asymétrie $\Delta_{\text{asym}} = \Delta\text{NLL}(Q_{\text{vu}}) - \Delta\text{NLL}(Q_{\text{post}})$.
- **Seuil :** $|\Delta_{\text{fuite}}| > 0{,}05$ `(illustratif)` ou $|\Delta_{\text{asym}}| > 0{,}03\text{ nats}$ `(illustratif)` (IC $95\,\%$ `(illustratif)` excluant $0$).
- **Contrôle négatif :** Un détecteur témoin gelé *avant* la création de $Q$ (ou une suite de vérifications mécaniques figée) évalué sur $Q_{\text{vu}}$ et $Q_{\text{post}}$ pour vérifier l'équivalence de difficulté ($|\Delta_{\text{témoin}}| \le 0{,}02$ `(illustratif)`).
- **Falsification :**
  - *Falsifie $H_B$ :* Parité de difficulté confirmée par le témoin et franchissement d'un des seuils de contamination ou d'asymétrie ($Q$ doit être déclassé et remplacé).
  - *Falsifie $H_A$ :* Parité confirmée et $|\Delta_{\text{fuite}}| \le 0{,}02$ `(illustratif)` et $|\Delta_{\text{asym}}| \le 0{,}01\text{ nats}$ `(illustratif)` avec une puissance statistique $\ge 80\,\%$ `(illustratif)` pour détecter les seuils critiques (innocence fonctionnelle pour cette version gelée uniquement).

---

## 4. Livrable (c) — Mesure minimale de fonctionnement pour chaque instrument nommé

Tous les chiffres de seuils ci-dessous sont marqués `(illustratif)`.

| Instrument nommé dans la question | Mesure minimale : détection (TPR) et fausses alertes (FPR) | Cas honnêtes appariés requis | Vérifications mécaniques à battre |
|---|---|---|---|
| **1. Détecteur lisant l'état interne** | Sur cas hors-genre passant les tests mécaniques : $\text{TPR} \ge 40\,\%$ `(illustratif)` à $\text{FPR} \le 5\,\%$ `(illustratif)` (ou $\text{TPR} \ge 25\,\%$ `(illustratif)` à $\text{FPR} \le 1\,\%$ `(illustratif)`), calibration ECE $\le 0{,}05$ `(illustratif)`. | Tâches réussies sans dégradation sur les **mêmes dépôts/domaines**, appariées en longueur de trajectoire ($\pm 10\,\%$ `(illustratif)`), nombre d'appels d'outils, présence d'erreurs intermédiaires légitimes (compilation ratée puis corrigée) et durée d'exécution. | (i) Tests unitaires, tests de propriété (*property-based*) et fuzzing ; (ii) analyse statique, vérificateurs de types, linters et invariants de sortie ; (iii) classifieur linéaire sur variables mécaniques de trace (longueur, latence, nombre d'échecs d'outils, entropie des logits de sortie, taille du diff). |
| **2. Second détecteur lisant le texte** | Mêmes seuils minimaux hors-genre : $\text{TPR} \ge 40\,\%$ `(illustratif)` à $\text{FPR} \le 5\,\%$ `(illustratif)` (et $\ge 25\,\%$ `(illustratif)` à $\text{FPR} \le 1\,\%$ `(illustratif)`), sur les cas résiduels non capturés par les contrôles mécaniques. | Mêmes cas honnêtes appariés que pour le détecteur interne, incluant des traces textuelles contenant des hésitations, corrections ou commentaires ambigus mais menant à un résultat honnête. | Mêmes suites de tests/linters/invariants + règles déterministes sur texte (expressions régulières d'erreurs ou de contournement, détection de suppression de tests, analyse syntaxique AST du diff de code). |
| **3. Instrument combiné interne + texte (pour (ii))** | Gain minimal $\Delta\text{TPR} \ge +5\text{ pts}$ `(illustratif)` à $\text{FPR} \le 5\,\%$ `(illustratif)` (sans hausse de $\text{FPR} > +1\text{ pt}$ `(illustratif)`) ET $\Delta\text{NLL} > 0{,}03\text{ nats}$ `(illustratif)` par rapport au texte seul. | Paires strictement identiques de trajectoires honnêtes/dégradées évaluées par les deux détecteurs (appariement exact pour réduire la variance du contraste). | Détecteur texte optimisé seul $h(S_{\text{txt}})$ ET détecteur texte augmenté des seules variables mécaniques de trajectoire $g_{\text{méc}}(S_{\text{txt}}, X_{\text{méc}})$. |
| **4. Critère chiffré de passage (règle d'arrêt)** | Taux de détection d'un vrai franchissement hors-échantillon $\ge 80\,\%$ `(illustratif)` ; taux de fausses alertes (arrêt prématuré sur un détecteur en réalité sous le seuil) $\le 5\,\%$ `(illustratif)` sur toute la séquence de cycles. | Trajectoires de cycles réels et simulés où la performance vraie hors-échantillon se situe juste sous le seuil visé (ainsi que des cycles sous étiquettes permutées). | Budget fixe prédéfini ($K$ cycles fixés *a priori* avec sélection sur validation dédiée) et règle séquentielle analytique classique (correction de multiplicité / *alpha-spending*). |
| **5. Lot en quarantaine $Q$ (instrument d'audit)** | Puissance $\ge 80\,\%$ `(illustratif)` pour détecter une chute de généralisation de $0{,}05$ AUROC `(illustratif)` ou un gain $\Delta\text{NLL}$ de $0{,}03\text{ nats}$ `(illustratif)` ; taux de fausse alerte $\le 5\,\%$ `(illustratif)` (ne pas signaler de chute quand un témoin invariant obtient le même score). | Tâches honnêtes générées par la **même équipe cloisonnée** que les cas dégradés de $Q$, avec distribution identique de complexité, de longueur et de taux d'échecs transitoires. | Holdout aléatoire i.i.d. issu des genres de développement + contrôles mécaniques de non-recouvrement (similarité n-grammes, hachage MinHash, distance d'AST) prouvant que $Q$ ne duplique pas le jeu de développement. |
| **6. Instrument de mesure d'écart à la loi publiée (i)** | Puissance $\ge 80\,\%$ `(illustratif)` pour détecter un écart réel de $2{,}5\,\sigma$ `(illustratif)` à la loi ; taux de fausse alerte $\le 5\,\%$ `(illustratif)` sur le banc où la loi publiée est vérifiée. | Banc de réplication respectant exactement les hypothèses de la loi publiée (même distribution de longueurs, même métrique, même structure de dépendance). | Régression paramétrique simple avec intervalles de confiance bootstrap par blocs de tâches (vérifiant que l'écart ne vient pas d'une sous-estimation naïve de la variance due à l'autocorrélation au sein des longues tâches). |

**Point critique sur l'appariement :** sur de longues tâches d'agent logiciel, une dégradation discrète modifie souvent indirectement le nombre d'étapes, la longueur du raisonnement ou le nombre d'appels d'outils. Si les cas honnêtes ne sont pas appariés sur ces variables de surface, un détecteur interne ou textuel peut obtenir un score élevé en ne détectant qu'une différence de longueur ; l'appariement strict + le contrôle $g_{\text{méc}}$ bloquent ce raccourci.

---

## 5. Livrable (d) — Ancrage matériel

Tous les chiffres de dimensionnement, de temps de calcul et de coûts ci-dessous sont marqués `(illustratif)`.

### Modèles ouverts (exigence d'accès aux états internes)
La revendication (ii) impose un accès direct aux états internes (activations résiduelles, têtes d'attention, logits avant échantillonnage), ce qui exclut les modèles propriétaires en boîte noire pour l'agent surveillé :
- **Agent logiciel surveillé :** modèle ouvert à fenêtre longue capable d'appels d'outils multi-étapes — par exemple `Qwen2.5-Coder-32B-Instruct` ou `Llama-3.1-70B-Instruct` pour l'expérience cible, et `Qwen2.5-Coder-7B-Instruct` ou `Llama-3.1-8B-Instruct` pour le prototypage rapide et les boucles de contrôle E1.
- **Détecteur texte de référence :** modèle ouvert de capacité suffisante pour éviter un homme de paille, par exemple `Qwen2.5-14B-Instruct` ou `Llama-3.1-8B-Instruct` (avec réglage de prompt ou fine-tuning LoRA sur les genres de développement).
- **Détecteur interne :** sondes légères (régression logistique régularisée, MLP à une couche cachée ou agrégateur par attention sur séquences d'états) entraînées sur un sous-ensemble de couches sélectionnées.

### Goulot d'étranglement matériel spécifique aux longues tâches
Sur une tâche longue de $32\,000$ jetons `(illustratif)`, sauvegarder en `bfloat16` toutes les couches d'un modèle de $64$ couches et dimension cachée $8\,192$ `(illustratif)` représente environ $33\text{ Go}$ `(illustratif)` par trajectoire unique — soit $\approx 33\text{ To}$ `(illustratif)` pour $1\,000$ trajectoires `(illustratif)`. Une implémentation viable impose une **extraction en flux (*streaming*)** limitée à $4\text{ à }8$ couches `(illustratif)` et agrégée par points de décision (fin d'appel d'outil ou blocs de $256$ jetons `(illustratif)`), ramenant l'empreinte disque à $\approx 25\text{–}100\text{ Mo}$ `(illustratif)` par trajectoire ($\approx 30\text{–}140\text{ Go}$ `(illustratif)` au total).

### Dimensionnement, calcul et coût estimés

- **Volume minimal de trajectoires (pour calibrer un $\text{FPR} \le 5\,\%$ `(illustratif)` avec une granularité non triviale) :**
  - Développement + validation interne ($3$ genres `(illustratif)`) : $600$ trajectoires `(illustratif)` ($300$ dégradées, $300$ honnêtes appariées).
  - Lot en quarantaine $Q$ : $200\text{ à }400$ trajectoires `(illustratif)` ($100\text{–}200$ dégradées d'un genre non consulté + $100\text{–}200$ honnêtes appariées).
  - Lots de contrôle (réplication de la loi E2 + lot frais post-gel $Q_{\text{post}}$ pour E4) : $300\text{ à }400$ trajectoires `(illustratif)`.
  - Total : $1\,100\text{ à }1\,400$ trajectoires longues `(illustratif)`.
- **Calcul GPU nécessaire (équivalent H100 $80\text{ Go}$ `(illustratif)`, agent $32\text{B}\text{–}70\text{B}$ `(illustratif)`) :**
  - Exécution des trajectoires agentiques et extraction en flux des activations : $150\text{ à }400\text{ heures-GPU}$ `(illustratif)`.
  - Cycles d'amélioration du détecteur texte ($10\text{ à }20$ cycles `(illustratif)` sur le développement) : $100\text{ à }250\text{ heures-GPU}$ `(illustratif)`.
  - Entraînement et balayage des sondes internes sur activations pré-agrégées : $20\text{ à }50\text{ heures-GPU}$ `(illustratif)`.
  - Expériences de contrôle (E1 boucle miroir, permutations, réplication E2, E4) : $100\text{ à }200\text{ heures-GPU}$ `(illustratif)`.
  - **Total calcul GPU :** $370\text{ à }900\text{ heures-GPU H100}$ `(illustratif)` (ou $120\text{ à }300\text{ heures-GPU}$ `(illustratif)` en version prototypage $7\text{B}\text{–}8\text{B}$ `(illustratif)`).
- **Coût estimé :**
  - Calcul GPU cloud (base $2{,}5\text{ à }3{,}5\text{ USD / heure-H100}$ `(illustratif)`) : $925\text{ à }3\,150\text{ USD}$ `(illustratif)`.
  - Environnement CPU sandboxé (exécution de code, tests unitaires, linters) + stockage chiffré WORM avec journal d'accès immuable ($\approx 200\text{ Go}$ `(illustratif)`) : $150\text{ à }400\text{ USD}$ `(illustratif)`.
  - **Poste dominant (ingénierie cloisonnée) :** concevoir, vérifier mécaniquement et apparier $200\text{ à }400$ tâches longues `(illustratif)` d'un genre inédit de dégradation discrète mobilise environ $40\text{ à }120\text{ heures-ingénieur}$ `(illustratif)`, soit $4\,000\text{ à }15\,000\text{ USD}$ `(illustratif)` en coût complet. C'est ce coût humain de création cloisonnée — bien plus que le calcul GPU — qui rend le gaspillage ou la contamination du lot $Q$ matériellement critique.

FIN-DE-CELLULE
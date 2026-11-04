# Proposition B : tour III.3, réponse aux critiques

**Pièces.** Les critiques de A, D et E sont présentes et lisibles. La critique C est absente (« jamais lancée ») : je n'en infère rien.

**Statuts.** Je reprends la convention de ma conception (tour III.1) :
- RAPPORTÉ : billet, pièce « nos résultats » ;
- OBSERVÉ-NON-AUDITÉ : journaux lus par le sous-agent (pièce 3) ;
- HYPOTHÈSE : tout ce que je propose ;
- VÉRIFIÉ : aucun fait.

Je traite les objections reçues comme des analyses méthodologiques de leurs auteurs (HYPOTHÈSES), pas comme des résultats. Je recalcule les chiffres que je reprends ; chacun est marqué « calcul ». Je ne réponds qu'aux sections « Sur la proposition B » et aux défauts transversaux T1 à T3 de A, qui me nomment.

---

## (a) Décision pour chaque critique

### Transversal

| Réf. | Critique | Décision |
|---|---|---|
| A-T1 | « 0 alerte sur 60 » ne certifie un taux de fausses alertes (TFA) ≤ 5 % que par un événement improbable. Si le TFA réel vaut 5 %, P(0/60) = 0,95⁶⁰ ≈ 0,046 ; s'il vaut 2 %, ≈ 0,30 (recalculé : calcul). | **Acceptée.** Ma phrase de E2 (« taille minimale pour certifier le seuil ») était fausse dans son usage. Je ne prétends plus certifier 5 %. Remplacement : protocole de calibration P0 ci-dessous. |
| A-T2 | Un seuil calibré sur m = 60 nuls donne un TFA réalisé d'écart-type ≈ 0,028. | **Acceptée.** Je recalcule : sous calibration par rang, le TFA réalisé suit une loi Bêta(3, 58), d'écart-type ≈ 0,0275 (calcul). Transformée en exigence de taille : P0. |
| A-T3 | Le modèle de départ est sycophante à 100 % (pièce 3 §3.1, OBSERVÉ-NON-AUDITÉ). | Déjà au cœur de E1. **Approfondie** : la proximité à l'ancêtre public devient une lecture concurrente à exclure (voir A-E1a). |
| D, E4 | 0 promotion sur 19 faux témoins ne borne le taux par témoin qu'à ≈ 14,6 %. | **Acceptée.** Je retrouve 1 − 0,05^(1/19) ≈ 0,146 (calcul). La remarque vaut aussi pour notre propre « 0 sur 19 » (pièce 2 §5, RAPPORTÉ). Pour borner à 5 %, il faut 0 sur 59 (calcul). |

**Correction de mon propre tour (d).** J'avais classé « E1 avec l'outil d'attention » parmi les expériences les moins chères. J'avais oublié que l'outil est piloté par un modèle de langue. Dans l'expérience 7, cela coûte 0,78 à 1,67 million de jetons d'entrée cumulés par paire (pièce 3 §3.3, OBSERVÉ-NON-AUDITÉ). Le cœur peu coûteux de E1' sera donc un outil d'attention **mécanisé**, c'est-à-dire figé. La version pilotée par un modèle de langue devient exploratoire.

### E1 (signe renversé)

| Réf. | Critique | Décision |
|---|---|---|
| A-E1a | P₁ descend de P₀. Le jumeau rendu sycophante depuis P₁ revient vers l'ancêtre public. La lecture « ressemble au Gemma public » n'est pas exclue. | **Acceptée, transformée en test.** Tant que l'ancêtre public est sycophante, « proche de l'ancêtre » et « sycophante » coïncident dans toutes les branches. Seule une famille dont l'ancêtre public est honnête les sépare. D'où l'étape 0 de E1' : mesurer l'ancêtre. Si aucun modèle candidat ne convient, la séparation est déclarée impossible au lieu d'être supposée. |
| A-E1b | La norme du delta est un confondant ; H_A et H_B ne sont pas exhaustives. | **Acceptée.** Normes appariées par construction, plus des cellules à norme inversée. Le duel porte désormais sur l'exactitude dans les cellules où chaque base mécanique se trompe. |
| A-E1c | « n doublé une fois » est un arrêt adaptatif. | **Acceptée.** n est fixé. Seule l'extension *avant toute lecture* est permise, pour atteindre un nombre minimal de cellules discordantes. |
| D-E1a | Les branches diffèrent par leur historique, leur force comportementale et leur parent. Il manque les lectures « parent », « norme » et « format ». | **Acceptée.** Jumeau « simulé » de même profondeur, plusieurs parents, force comportementale mesurée et rapportée. Les lectures « norme » et « format » sont traitées par appariement et par le témoin bénin. |
| D-E1b | Une base qui reçoit le parent n'a pas le même accès que le lecteur. | **Acceptée.** Deux niveaux d'accès, chacun avec ses propres bases. |
| D-E1c | La variance entre parents n'est pas estimable avec un seul P₁. | **Acceptée.** Quatre parents par type (illustratif) ; analyse en grappes par parent. |
| E-E1a | Il faut dire ce que voit le lecteur. | **Acceptée** : niveaux d'accès 1 et 2 de E1'. |
| E-E1b | Exiger ≈ 0,5 sur une paire de deux sycophantes est incorrect. | **Acceptée.** Ma consigne posait une question dont la prémisse (« exactement un des deux ») est fausse sur une paire nulle. On sépare désormais l'**orientation**, posée seulement sur les paires discordantes, et la **présence d'une différence**, posée sur toutes les paires et seule utilisée pour le TFA. |
| E-E1c | Le score de Brier doit porter sur l'événement noté. | **Acceptée.** Brier calculé sur « A est le sycophante, sachant qu'exactement un l'est », dans les paires discordantes seulement. |
| E-E1d | L'intervalle à n = 20 ne sépare pas assez. | **Acceptée.** Les tailles sont revues ; le critère porte sur les cellules discordantes, avec un minimum fixé d'avance. |

### E2 (deltas face aux sondes et à la boîte noire)

| Réf. | Critique | Décision |
|---|---|---|
| A-E2a | Le budget de la boîte noire était égalisé sur l'outil d'attention, pas sur le lecteur, qui ne fait aucune passe. | **Acceptée.** Deux régimes : (i) zéro requête, lecteur contre bases de poids ; (ii) apport incrémental, boîte noire à N figé, comparée à boîte noire + score de poids (voir E-E2c). |
| A-E2b | L'étiquette peut fuir vers la boîte noire. | **Acceptée.** La vérité comportementale est mesurée sur un lot scellé de faits, disjoint des requêtes de la boîte noire. |
| A-E2c | L'agrégation des trois répétitions n'est pas gelée. | **Acceptée** : moyenne des probabilités déclarées, gelée. |
| A-E2d | La boîte noire est au plafond, donc H_A est infalsifiable. | **Acceptée en partie.** Les positifs sont stratifiés par expression comportementale mesurée. Le contraste principal est restreint d'avance aux strates où la sensibilité de la boîte noire sur développement est ≤ 0,8 (illustratif). S'il n'y en a pas, l'issue « non jugeable » est déclarée. |
| D-E2a | Dose de données ≠ dose de comportement. | **Acceptée.** La dose n'est qu'une variable de construction ; la positivité est comportementale. Les adaptateurs exposés aux données du trait mais nuls en comportement sont *classés*, pas fabriqués : ils apparaissent d'eux-mêmes aux doses basses. Un lecteur qui les signale lit la recette. |
| D-E2b | Le maximum sur plusieurs concurrents est biaisé. | **Acceptée.** Ordre des concurrents fixé sur développement ; intervalles simultanés de Bonferroni sur 4 comparaisons. |
| D-E2c | Les mêmes nuls calibrent et rapportent. | **Acceptée** : P0. |
| E-E2a | Calibrer sur des paires ne vaut pas pour des verdicts par adaptateur. | **Acceptée.** Les nuls sont des adaptateurs individuels honnêtes : même unité que le verdict. |
| E-E2b | Les zones laissées entre les marges ne sont pas jugées. | **Acceptée.** Duel complémentaire à la manière de E : H_A : G ≥ ε ; H_B : G < ε. Un intervalle qui traverse ε donne « indécis », pas une réfutation. |
| E-E2c / D | Il manque le contrôle « métadonnées seules » et les descriptions désappariées. | **Acceptée** ; les deux sont ajoutés. |

### E3 (validité de construit d'un retrait)

| Réf. | Critique | Décision |
|---|---|---|
| A, D, E – E3a | Conditionner sur la terminaison dans les deux modèles revient à sélectionner sur une variable qui suit l'intervention (collisionneur). | **Acceptée.** Je reprends, en le disant, le conditionnement avant traitement que A attribue à D. La strate « la base termine » est définie sur des générations de sélection indépendantes. |
| A-E3a | Environ 35 problèmes MATH-500 terminés par la base (7 % de 500 : calcul ; pièce 3 §4.2, OBSERVÉ-NON-AUDITÉ) ; une marge de 2 points est inatteignable. | **Acceptée.** Réserve élargie à des problèmes hors bancs, 8 échantillons par problème, marge portée à 3 points (illustratif) et justifiée par une erreur type cible. |
| A-E3a | Ajouter un témoin de troncature forcée. | **Acceptée.** |
| D-E3a | Une seule direction aléatoire est un témoin faible. | **Acceptée.** 10 directions aléatoires appariées en norme, plus 5 directions candidates tirées du même espace (directions écrites par les mêmes perceptrons). |
| A-E3b | k et l'échelle des notes ne sont pas séparables sans ancrage. | **Acceptée** : items d'ancrage sans pression, notés avant et après l'intervention. |
| E-E3b | Changer k est déjà un effet causal ; opposer pente et point fixe n'est pas valide. | **Acceptée.** Le duel porte sur Δk seul ; le point fixe est rapporté séparément, sans valeur de verdict. |
| E-E3b | Utiliser la direction lisible comme témoin négatif est circulaire. | **Acceptée.** Elle devient un **second bras de traitement**. Seules les directions aléatoires sont des témoins. |
| D-E3b | Plages intermédiaires ; une seule intervention. | **Acceptée.** Duel complémentaire, et trois éditions estimées sur des partitions disjointes. |

### E4, E5, E6

| Réf. | Critique | Décision |
|---|---|---|
| A-E4 | « Propriété aléatoire » est mal défini ; les proposeurs ne doivent pas jouer l'oracle. | **Acceptée.** Faux témoins : étiquette rendue indépendante des poids au moment de l'évaluation. L'oracle est interdit aux proposeurs. Une loi doit être une statistique des poids, évaluée sur des tirages frais. |
| A (contre D, applicable à B) | Les propriétés lisibles en première ou dernière couche (L84, RAPPORTÉ) rendent le nul augmenté autodestructeur. | **Acceptée, je m'en sers.** Les propriétés sont plantées dans les couches du milieu, sur le modèle de l'expérience 3 (pièce 3 §2). |
| D, E – E4 | Un nul se définit par une famille de lois, pas par une liste ; l'absence de promotion ne prouve pas une réduction. | **Acceptée.** Le nul devient « la propriété est prédite par un prédicteur mécanique M, gelé et ajusté sur des réseaux de calibration ». H_B porte sur un test explicite contre M, plus sur l'absence de promotion. |
| A-E5 | La bascule test-retest (q) se confond avec la bascule induite. | **Acceptée** : transformée identité répétée. |
| A-E5 | Pour la tangente hyperbolique, seules permutations et changements de signe compensés préservent la fonction. | **Acceptée.** Ensemble admissible préenregistré par architecture. |
| D, E – E5 | J'attribuais à tort une invariance aux sondes, aux têtes et aux normes. | **Acceptée.** L'invariance de chaque référence est vérifiée et non supposée. La norme de Frobenius par couche est invariante sous permutation et changement de signe (calcul), pas sous changement d'échelle compensé. |
| D (contre A, applicable à B) | Un lecteur constant est invariant. | **Acceptée** : exigence de détection, plus des transformées qui changent la fonction, d'amplitude appariée. |
| E-E5 | Une moyenne ne borne pas le pire cas. | **Acceptée.** Aucune revendication sur le pire cas ; on rapporte le maximum sur les transformées tirées. |
| A, D, E – E6 | Les récompenses permutées ne forment pas un nul. | **Acceptée.** Nuls : réseaux à 0 pas d'entraînement, et réseaux entraînés sur des observations tirées entre jeux. |
| D-E6 | Le choix fermé change le construit ; les répétitions sur les mêmes réseaux ne sont pas indépendantes. | **Acceptée.** Question ouverte en primaire, choix fermé en secondaire ; réseaux frais par répétition. |
| E-E6 | 1 − (1 − p)ⁿ suppose l'indépendance. | **Acceptée.** Formule donnée comme référence sous indépendance seulement ; l'observé est rapporté tel quel. |

**Aucune critique n'est rejetée.** Une est seulement nuancée : A-E2d (plafond de la boîte noire). Le plafond n'est pas une fatalité du montage, il dépend de la strate. Je la traite par stratification préenregistrée plutôt qu'en abandonnant E2.

---

## (b) Expériences corrigées

Toutes les prédictions sont des HYPOTHÈSES ; toutes les tailles sont illustratives sauf mention « calcul ».

### P0 : protocole de calibration commun (réponse à T1 et T2)

1. **Unité d'indépendance** : le parent et la recette, pas la graine d'adaptateur seule (D). Calibration, test et développement sont disjoints par parent.
2. **Seuil** : rang conforme sur m_cal nuls échangeables. Seuil = statistique d'ordre ⌈(m_cal + 1)(1 − α)⌉, avec α = 0,05.
   - Garantie *en moyenne sur la calibration* : E[TFA] ≤ α sous échangeabilité. C'est une propriété classique des rangs (référence à vérifier).
   - Écart-type du TFA réalisé : ≈ 0,028 à m_cal = 60 ; ≈ 0,015 à m_cal = 200 (calcul).
3. **TFA rapporté** sur m_test nuls disjoints, avec une borne de Clopper-Pearson.
   - Avec m_test = 150 et un TFA observé de 5 %, la borne supérieure unilatérale vaut ≈ 0,08 à 0,09 (calcul, approximation).
   - Critère « plafond respecté » : borne supérieure ≤ 0,10. Je ne revendique plus 5 %.
4. **Comparaisons entre instruments** : chacun est calibré sur les **mêmes** unités nulles. Différence de détection appariée par unité positive. La ROC partielle sur un TFA de 0 à 0,10 est donnée en secondaire.
5. **Budget** :
   - Instruments mécaniques et outil d'attention mécanisé : m_cal = 200, m_test = 150.
   - Lecteurs modèles de langue : une seule famille, tirée au sort d'avance, au m complet. Les deux autres à m = 60/60, déclarées exploratoires (TFA flou de ±0,03, calcul).

### E1' : le verdict lit-il le trait, le déplacement, l'ancêtre ou la norme ?

**Étape 0** (environ un jour sur une carte, illustratif).
- Mesurer le taux de suivi des mauvaises suggestions sur le jeu de faits publié par les auteurs (pièce 3 §1, promesse (e), RAPPORTÉ) pour trois ancêtres publics :
  - Gemma 3 270M ajusté aux instructions (attendu : 100 %, pièce 3 §3.1, OBSERVÉ-NON-AUDITÉ) ;
  - Qwen3.5-0.8B ;
  - Llama-3.1-8B-Instruct.
- Un ancêtre est dit « honnête » s'il suit ≤ 0,3 des mauvaises suggestions (illustratif, figé avant la mesure).
- S'il n'y en a aucun, la lecture « ancêtre » est déclarée **non séparable** du trait et E1' ne départage que trait, déplacement et norme.

**Montage.**
- Pour chaque ancêtre retenu : 4 parents P_syc et 4 parents P_hon. Ce sont des affinages indépendants, à graines et sous-ensembles de faits différents.
- Depuis chaque parent, des paires (*mobile*, *simulé*) :
  - le *mobile* est affiné pour inverser le trait ;
  - le *simulé* est affiné au même format, avec le même nombre de pas, sur des données qui conservent le trait ;
  - le taux d'apprentissage du simulé est réglé sur la calibration pour apparier la norme du delta à ±10 % ;
  - un quart des paires a une norme volontairement inversée (simulé > mobile).
- Force comportementale de chaque jumeau mesurée sur un lot scellé ; une paire n'est retenue que si l'inversion voulue est réalisée.
- Paires nulles : deux simulés du même parent.

**Niveaux d'accès.**
- (1) Les deux points finaux seulement, comme dans le billet. Base mécanique : distance à l'ancêtre public.
- (2) Points finaux et parent. Bases : norme du delta, distance au parent.

Chaque base ne reçoit que l'accès de son niveau.

**Instruments.**
- Outil d'attention mécanisé : textes figés et statistique figée sur développement. Il s'agit de la masse d'attention de la position de réponse vers la suggestion, contre les nombres de la question, comme pour la tête 10.2 (pièce 3 §3.4, OBSERVÉ-NON-AUDITÉ), avec une règle d'agrégation sur les têtes gelée.
- Bases mécaniques.
- En exploratoire, sur 12 paires : outil d'attention piloté par un modèle de langue.

**Questions posées.**
- Orientation : seulement sur les paires discordantes.
- Présence d'une différence : sur toutes les paires ; elle seule sert au TFA, selon P0.

**Statistique décisive.** acc_disc : exactitude d'orientation sur les paires où **chaque** base mécanique de même niveau d'accès donne une prédiction fausse. Les prédictions des bases sont calculées avant toute lecture. On exige n_disc ≥ 24 paires (illustratif) ; s'il en manque, on produit d'autres paires **avant** de lire.

**Duel.**
- H_A, lecture du trait : acc_disc ≥ 0,75.
- H_B, réductible à une base : acc_disc ≤ 0,5.
- Entre les deux : non concluant, sans extension.
- Exclusives, et chaque issue concluante falsifie l'autre.
- Analyse en grappes par parent. Rapport séparé par niveau d'accès et par type de parent.

**Ce que ça change.**
- Si H_B est vraie, la statistique de la tête 10.2 ne peut entrer dans le programme de contrôle que comme mesure d'écart au parent, pas comme moniteur de sycophancie.
- Si H_A est vraie, on dispose d'un moniteur d'état interne candidat pour E2, avec son témoin obligatoire.

**Abandon.**
- Inversion voulue non réalisée dans plus de 25 % des paires (illustratif).
- Ou TFA de présence dont la borne supérieure dépasse 0,20 pour tous les instruments.

### E2' : deltas d'adaptateurs, à TFA calibré

**Montage.**
- Adaptateurs de rang 1, limités aux couches 8 à 14 de Gemma 3 270M, puis Llama-3.1-8B-Instruct.
- Verdict par adaptateur.
- Positivité définie sur un lot scellé, disjoint des requêtes de la boîte noire.
- La dose n'est qu'une variable de construction.

**Taille en texte.** 7 × (640 + 1 024 + 640 + 256) = 17 920 paramètres, soit ≈ 37 000 jetons (calcul). La dimension de tête de 256 est **supposée** ; le ratio d'environ 2,07 jetons par poids vient de la pièce 3 §6.1.

**Coût.** 350 unités × 37 000 jetons ≈ 13 millions de jetons pour une famille (calcul). À 1 à 3 $ par million (illustratif), cela fait 13 à 39 $. C'est pourquoi une seule famille passe au m complet.

**Régime (i), zéro requête.**
- Lecteur modèle de langue, contre la norme du delta et contre un cosinus avec une direction supervisée calibrée sur des parents disjoints.
- G = détection appariée du lecteur moins celle du meilleur concurrent, l'ordre des concurrents étant fixé sur développement.
- Duel : H_A : borne inférieure de G > 0,15 ; H_B : borne supérieure de G < 0,15 (illustratif). Intervalles de Bonferroni ; indécis sinon.

**Régime (ii), apport incrémental.**
- Boîte noire à N = 32 requêtes (illustratif, figé).
- Comparée à : boîte noire + score du lecteur ; boîte noire + score mécanique ; boîte noire + score du lecteur permuté entre unités.
- Règle de fusion : régression logistique gelée sur développement.
- Contraste principal restreint aux strates où la sensibilité de la boîte noire sur développement est ≤ 0,8 (illustratif).

**Témoins.**
- Adaptateurs bénins, appariés en norme.
- Adaptateurs exposés aux données du trait mais nuls en comportement.
- Lecteur privé des poids, avec métadonnées seules.
- Deltas présentés avec une description désappariée.

**Abandon.** Détection ≤ 0,2 à TFA calibré pour le meilleur lecteur, dans la strate la plus expressive.

### E3a' : retrait de la boucle de Qwen, capacité ou terminaison ?

**Objet.** Le diff livré, sur 50 passes (pièce 3 §6.6 f, OBSERVÉ-NON-AUDITÉ).

**Strate.**
- Problèmes de réserve hors bancs d'essai, au départ ≈ 2 000 (illustratif).
- Sélection : la base termine au moins 3 générations de sélection sur 4, générations indépendantes de l'estimation.
- Estimation : 8 nouveaux échantillons par problème, dans chaque bras.
- Viser une erreur type ≤ 1 point demande ≈ 1 800 observations appariées par bras si p ≈ 0,9 et sans tenir compte de la corrélation intra-problème (calcul, optimiste). Soit environ 225 problèmes retenus.

**Duel.**
- H_A, terminaison seule : |Δ| ≤ 3 points.
- H_B, raisonnement changé : |Δ| > 3 points.
- Décision sur l'intervalle ; indécis sinon.

**Témoins.**
- Troncature forcée de la base au budget de jetons de l'édité.
- 10 directions aléatoires appariées en norme.
- 5 directions candidates écrites par les mêmes perceptrons.

**Dégâts.** Mesurés à budget de jetons fixe : perplexité sur un texte tenu à l'écart, MMLU-Pro, IFEval.

**Abandon.** Si la médiane des directions candidates reproduit plus de la moitié du gain de terminaison, la notion de « direction » n'est pas spécifique.

### E3b' : loi d'attraction comme mesure de validité de construit

**Montage.**
- Llama-3.1-8B-Instruct.
- Au moins 5 doses, dont 0.
- Items d'ancrage sans pression, notés avant et après l'intervention, pour fixer l'échelle.
- Suggestions vraies, assertions neutres et pression sans contenu, pour détecter un esprit de contradiction générique.
- Non-réponses comptées selon un critère préenregistré, pas retirées du dénominateur.

**Bras.**
- Retrait de la direction selon 2511.05408 (cité par la question, non lu ici). Trois éditions, estimées sur des partitions disjointes de faits et de cadres.
- Second bras de traitement : la direction de notre sonde (pièce 2 §7, RAPPORTÉ).
- Témoins : 10 directions aléatoires appariées en norme.

**Duel.**
- H_A : Δk/k ≤ −0,2.
- H_B : Δk/k > −0,2 (illustratif).
- Le point fixe est rapporté sans valeur de verdict.

**Abandon.** Si k varie de plus de ±10 % entre graines sur le modèle non édité, la loi ne peut pas arbitrer.

### E4' : famille « couches du milieu à propriété plantée »

**Réseaux.** Transformeurs au gabarit de l'expérience 3, en plus petit. Propriété plantée par la tâche, mesurable par un oracle exécutable.

**Nul.**
- Prédicteur mécanique M gelé : statistiques de première et dernière couche, et normes.
- Le juge teste si la loi prédit mieux que M sur des tirages frais.

**Faux témoins et contrôles.**
- 59 faux témoins, à étiquette indépendante des poids. Zéro promotion borne le taux par témoin à ≈ 4,9 % (calcul).
- Injecteur scripté de recombinaisons de lois acceptées (classe W2, pièce 2 §3).
- Proposeur sans accès aux poids, à budget égal.

**Duel.**
- H_A : au moins une loi non plantée est promue contre M, et la puissance mesurée sur des lois plantées de force réglée est ≥ 2/3.
- H_B : aucune loi ne bat M, alors que la puissance sur les lois plantées est ≥ 2/3.
- Si la puissance est < 2/3 : non jugeable (A), plutôt qu'une réfutation de H_A.

### E5' : invariance du verdict sous reparamétrisation (côté défenseur)

**Transformées.**
- Ensemble admissible préenregistré par architecture : permutations ; changements de signe pour la tangente hyperbolique ; échelles positives compensées pour l'unité linéaire rectifiée.
- Fidélité fonctionnelle vérifiée par exécution.

**Bascule observée.**
- q, la bascule de la transformée identité répétée, est mesurée.
- La bascule induite est estimée par t = (b − q)/(1 − q), où b est la bascule observée (calcul).

**Contrôles.**
- Transformées qui changent la fonction, d'amplitude appariée.
- Exigence de détection, pour exclure un lecteur constant.

**Duel.**
- H_A : t ≤ 0,05.
- H_B : t ≥ 0,2.
- Le maximum sur les transformées tirées est rapporté ; aucune revendication sur le pire cas.
- Si la défense est une forme canonique, l'invariance est acquise par construction ; on mesure alors seulement son coût.

### E6' : lecteurs multiples, toutes tentatives publiées

**Montage.**
- Réseaux frais à chaque répétition. L'entraînement est plus court que dans le billet, ce qui est déclaré comme un écart.
- Question ouverte en primaire, choix parmi 8 en secondaire.
- Nuls : réseaux à 0 pas d'entraînement, et réseaux entraînés sur des observations tirées entre jeux.

**Duel.**
- H_A : exactitude par réseau frais ≥ 0,8, chez au moins deux familles.
- H_B : ≤ 0,5.

---

## (c) Réponse à la question de l'arbitre

**Ce qui est établi, au niveau qu'autorisent nos pièces (rien n'est VÉRIFIÉ ici).**
- RAPPORTÉ par le billet : lectures réussies sur de petits réseaux (17 253 à 7,16 millions de poids), une réparation de politique, des réseaux de jeu écrits sans gradient, un retrait de boucle sur Qwen3.5-0.8B.
- OBSERVÉ-NON-AUDITÉ par les journaux, pour l'expérience 7 :
  - échec sur les poids seuls : P = 0,5 avec départage forcé dans les tentatives 1 à 3 ; tentative 4 arrêtée ;
  - réussite seulement avec l'outil d'attention, qui est une passe avant : 3 sur 3 en choix forcé, confiance de 0,55 sur la paire 3, aucune paire témoin ;
  - greffe des composants nommés : écart fermé de 0,00 ;
  - modèle de départ déjà sycophante à 100 %.
- OBSERVÉ-NON-AUDITÉ pour l'expérience 8 : le gain porte sur les réponses coupées (93,9 → 93,9 % sur les réponses déjà terminées, problèmes d'entraînement).
- Un seul lecteur ; des runs non montrés.

**Ce qui n'est pas établi.**
- La lecture d'un trait d'alignement dans les **poids seuls** d'un modèle de langue.
- Que la réussite de l'expérience 7 lise le trait plutôt que l'écart au parent ou la proximité à l'ancêtre public.
- Un taux de fausses alertes, quel qu'il soit.
- Le transfert à d'autres lecteurs.
- La validité causale des composants nommés.
- Qu'un retrait de direction change une capacité plutôt que la terminaison.
- Une quelconque robustesse face à un adversaire qui écrit des poids.

Un point vaut aussi pour nous. Notre « 0 sur 19 faux témoins » (pièce 2 §5, RAPPORTÉ) ne borne le taux par témoin qu'à ≈ 14,6 % (calcul, sous indépendance) ; il en faut 59 pour borner à 5 %.

**Intégration proposée (HYPOTHÈSES).**
- **Organisme d'idéation.** Famille E4' : des lois sur les poids jugées contre un prédicteur mécanique gelé, avec 59 faux témoins et un injecteur W2.
- **Programme de contrôle.** Le lecteur de poids ou de deltas reste **hors** des moniteurs tant que E1' et E2' n'ont pas donné une détection à TFA calibré (P0). Si l'outil d'attention réussit, il est classé moniteur d'état interne, pas lecteur de poids. La boîte noire est la référence, et l'apport se mesure en incrément.
- **Travaux sur la sycophancie.** La loi d'attraction devient l'instrument de validité de construit (Δk ancré) pour toute intervention, y compris celles que proposerait un lecteur (E3b'). Le refus de traiter « lisible » comme témoin négatif évite de présumer notre propre conclusion.

**L'expérience à faire en premier : E1', étape 0 puis cœur mécanisé.**
1. Une journée sur une carte pour mesurer le suivi des mauvaises suggestions par les ancêtres publics. C'est ce qui décide si la lecture « ancêtre » est séparable du trait.
2. Ensuite, les paires mobile/simulé à normes appariées, l'outil d'attention figé et les bases mécaniques, sans aucun appel au lecteur modèle de langue.

Le coût est faible (illustratif) et le verdict, binaire : acc_disc ≥ 0,75 ou ≤ 0,5. Il conditionne l'interprétation de E2' et de la seule expérience du billet qui touche un trait d'alignement.

**Seuil d'abandon.** Inversion comportementale non réalisée dans plus de 25 % des paires, ou TFA de présence dont la borne supérieure dépasse 0,20 pour tous les instruments.

**En parallèle, à coût de carte seul.** E3a', sur le diff publié.

FIN-DE-CELLULE
# Proposition B · Tour III.2 : critique croisée de méthode

**Pièces.** J'ai reçu A, C, D et E. Elles paraissent complètes : chacune se termine par sa ligne de clôture. FAITS et QUESTION sont également reçus. Je n'ai pas recalculé les empreintes sha256.

**Forme.** La QUESTION fixe l'ordre 1 à 6 pour les conceptions, et ce tour fixe un livrable par proposition. Je suis le livrable du tour. J'applique la QUESTION comme critère : chercher la profondeur plutôt que la longueur, n'inventer aucun chiffre ni aucune référence, séparer ce qui est établi de ce qui est proposé. Les nombres repris des pièces sont les leurs, déjà illustratifs. Mes calculs sont de l'arithmétique, et leurs paramètres d'entrée sont marqués « illustratif ». Je ne modifie aucun statut ; quand une pièce en surélève un, je le signale sans le reprendre.

**Grille (HYPOTHÈSE de méthode).** La règle B4 est nécessaire mais ne suffit pas. Un duel dont chaque issue « falsifie » quelque chose, mais avec des erreurs proches de 1/2, ne falsifie rien. Pour chaque critère, je cherche donc trois choses : (i) ce qui est vrai par construction ; (ii) la loi sous laquelle le critère perd sa puissance ; (iii) le témoin négatif sans lequel une issue positive est ininterprétable.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **D1 : fuite par la formulation.** Les modèles reçoivent « les définitions et la question » d'un résultat postérieur à T. Or celui qui rédige ces définitions connaît le résultat. Le choix des objets, la normalisation et la forme de la question en encodent une part. Le contrôle sur les cibles antérieures à T mesure la mémorisation, pas cette fuite-là. De plus, les dates de coupure des modèles sont RAPPORTÉES par leurs fournisseurs, et les prépublications précèdent la publication : « postérieur à T » n'est pas une propriété vérifiée.
2. **D1 : choix de la « meilleure lignée seule ».** Si elle est choisie sur les mêmes cibles, elle bénéficie d'une sélection sur l'échantillon d'évaluation (malédiction du gagnant). Le duel est alors biaisé vers H_B. Elle doit être choisie sur un lot de développement disjoint.
3. **D1 : diversité et volume confondus.** L'écart entre l'organisme et une lignée seule mêle trois causes : la diversité des lignées, le nombre d'échantillons et la sélection par les juges. Tel qu'il est écrit, H_A attribue tout gain à l'architecture (S6).
4. **P2/D4 : vrai par construction.** La borne de P2 est un corollaire de l'inégalité de traitement des données. Si ses hypothèses tiennent, aucune sonde ne peut la dépasser. L'issue « borne respectée » ne réfute donc pas « la théorie est décorative » : elle confirme une implication logique. Seules les issues « borne vide » et « dépassement » informent. Encore un dépassement signale-t-il d'abord une erreur d'estimation ou une hypothèse violée, pas une fausseté.
5. **P1 : partition à l'intérieur de la grille.** Conjecturer sur une partie de la grille (k, α, β) et tester sur le reste revient à tester une interpolation. Si l'optimum vrai est défini par morceaux, avec des cassures hors de la grille, une forme close lisse survit par construction.
6. **D2 : la population de mutants décide du résultat.** Des mutants « à témoin connu » sont, par construction, ceux qu'une recherche finie sait tuer. La suite bon marché gagne donc sur cette population. L'avantage éventuel de Lean porte sur des hypothèses (mesurabilité, intégrabilité) dont le témoin n'est pas fini. Sans stratification par type de témoin, D2 mesure la façon dont les mutants ont été tirés.
7. **§4.2, recherche de preuve.** Les « lemmes de manuel absents de Mathlib » figurent dans les corpus d'entraînement. Le taux de clôture mesure donc aussi ce que le modèle a mémorisé.

### (b) Conditions de perte de puissance

- **D1.** Le test ne porte que sur les d cibles discordantes, avec b victoires de l'organisme et c de la lignée seule. Sous H_0 (discordances symétriques), avec d = 4 (illustratif), la probabilité P(b − c ≥ 2) vaut P(b ≥ 3) = 5/16. Le seuil de A déclarerait donc un gain près d'une fois sur trois sans effet réel. Si la probabilité de succès par cible est proche de 0, ce que l'on attend sur des cibles postérieures à T, d est petit et le duel n'est pas jugeable. Il en va de même si la variance du compte entre graines dépasse l'écart visé : une seule course par bras ne suffit pas.
- **D4.** La variation totale entre lois de transcriptions ou d'activations en grande dimension n'a pas d'estimateur consistant sans hypothèse de structure. L'estimateur par mesures empiriques vaut 1 presque sûrement pour des lois continues, puisque les supports empiriques sont disjoints. Si n est très inférieur à la taille effective du support, le critère « plafond < 1 » n'est pas jugeable. Il faut le remplacer par une borne inférieure de la variation totale, obtenue par une famille de tests fixée d'avance et assortie d'un intervalle de confiance. Cela change l'énoncé même de D4.
- **D3.** Si la distance au corpus des énoncés postérieurs à T recouvre celle des énoncés connus paraphrasés (cas des résultats incrémentaux), toute AUC tend vers 1/2. La nouveauté des énoncés postérieurs à T est graduée, pas binaire.

### (c) Contrôles négatifs fatals s'ils manquent

- **Cinq tirages d'une même lignée, à budget égal.** Duel : H_A, « la diversité des lignées atteint des cibles que le volume n'atteint pas » ; H_B, « l'organisme équivaut au meilleur de N tirages d'une seule lignée ». Si l'organisme bat les tirages homogènes, H_B tombe. Sinon, le gain observé dans D1 est réfuté en tant qu'effet d'architecture.
- **Sonde de fuite postérieure à T.** On donne aux modèles le seul titre du résultat, sans la question. S'ils en retrouvent la conclusion, la cible sort du lot.
- **Honnête contre honnête (deux graines du jumeau), pour D4.** La variation totale estimée doit être compatible avec 0. Sinon, l'estimateur est cassé. Les étiquettes permutées de A ne testent pas ce point.

---

## Sur la proposition C

### (a) Défauts de méthode

0. **Statuts.** C étiquette « VÉRIFIÉ dans les faits » des éléments que FAITS donne sans statut, et « VÉRIFIÉ » des références citées de mémoire. Je ne reprends pas ces statuts. Quant au « 70 % du succès », ce n'est pas une quantité mesurable, même à titre illustratif.
1. **Méthode 1 : vrai par construction.** Le Bras B « observe » la solution numérique du Bras A et propose U ; le critère de gel est |U − L| < 10⁻⁴ sur les mêmes mondes. Un ajustement sur L passe ce critère par construction. U n'est pas une borne supérieure : c'est une interpolation de bornes inférieures. Une borne supérieure exige un certificat dual, indépendant du primal.
2. **Méthode 1 et Expérience 2 : les mêmes mondes construisent et évaluent.** L'écart δ à V* est mesuré sur les douze mondes qui ont servi à ajuster U.
3. **Expérience 1 : vrai par construction, et confusion.** Si la fausseté d'un sous-lemme est décidée par le filtre lui-même, le bras filtré consacre par définition 0 % de son temps à des sous-lemmes faux. Il faut une vérité indépendante : des lemmes plantés dont le statut est connu. Par ailleurs, les sous-lemmes traduisibles en Python sont plus concrets, donc plus faciles. Le gain mesuré mêle ainsi l'effet du filtrage et une sélection par la difficulté. Enfin, les théorèmes « de niveau licence ou master » sont présents dans les corpus d'entraînement.
4. **Instrument 3 : « trivial » n'est pas « connu ».** La règle « prouvé par `exact?` ou `aesop` en 5 s, donc pas nouveau » confond facilité et antériorité. Elle tue les résultats neufs et faciles, classe que C désigne lui-même comme produit probable. Elle laisse en revanche passer les résultats connus mais difficiles à prouver.
5. **Instrument 2.** Des énoncés faux obtenus en violant une constante de 10 % sont loin de la frontière. Le taux de rejet mesure alors le choix de cet écart, pas l'instrument.
6. **Méthode 3.** Un terme correctif Δ(ρ) choisi pour rendre l'inégalité « vraie sur tous les mondes plantés » est vrai sur ces mondes par construction.

### (b) Conditions de perte de puissance

- **Méthode 1.** Si le problème de l'adversaire est non convexe, comme pour une covariance opposée à une sonde linéaire (exemple de C), l'optimiseur rend un optimum local. On a alors L < V* avec une probabilité non négligeable, et U, ajusté sur L, est faux. Un écart |U − L| petit ne détecte rien, puisque les deux erreurs vont dans le même sens. Le critère ne garde sa puissance que si le primal est un programme linéaire exact (alphabets finis, couplages), cas où L = V*.
- **Expérience 2.** L'écart δ = |U − V*|/|V*| n'est pas défini quand V* tend vers 0. Or c'est le cas dans les mondes où la détection est impossible, c'est-à-dire précisément ceux du lemme d'impossibilité.
- **Expérience 3.** Un juge quasi déterministe produit un seul point, pas une courbe ROC. L'AUC n'existe que si le juge rend un score continu.

### (c) Contrôles négatifs fatals s'ils manquent

- **Monde piège non convexe**, à optimum global connu et optimum local saillant. Si la Méthode 1 gèle l'optimum local, le critère de gel est réfuté.
- **Bornes L permutées entre mondes.** On donne au Bras B la borne L d'un autre monde. S'il obtient encore |U − L| sous le seuil, l'ajustement est trop souple pour prouver quoi que ce soit.
- **Lemmes vrais tangents** (égalité atteinte, arrondi critique), pour mesurer les faux rejets du filtre de l'Expérience 1. Les vingt squelettes faux de C ne mesurent que la détection.
- **Énoncés neufs et faciles plantés**, pour éprouver l'Instrument 3.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **La taille des instances décide du vainqueur.** À temps égal, l'énumération canonique gagne dès que l'espace est épuisable dans le temps alloué ; la recherche guidée ne peut gagner qu'au-delà. D-valeur mesure donc la loi des tailles de la famille réservée, pas la méthode. L'issue doit être rapportée en fonction de la taille.
2. **Équivalence non fixée.** « Séparations non équivalentes » doit être défini avant la course, de façon identique pour les deux bras (symétries du jeu, renommage des états). Sinon, le compte dépend de la canonisation.
3. **D-frontière : le domaine est choisi par le système.** Si le proposeur annonce son propre domaine, il peut le rétrécir jusqu'à ce que la suffisance devienne triviale. Le domaine doit être gelé en même temps que la famille.
4. **H_B fusionne des cas distincts.** La négation de « davantage de séparations sans fausse supplémentaire » couvre trois situations : « plus de séparations mais plus de fausses », « moins », « autant ». Elles n'ont pas les mêmes conséquences, et D les fusionne.
5. **Utilité mesurée « avant puis après divulgation » par la même équipe.** L'ordre crée un effet d'apprentissage sur le cas réservé. Il faut contrebalancer l'ordre ou faire appel à deux équipes.
6. **Statut.** D emploie OBSERVÉ-NON-AUDITÉ pour l'absence de pièces, ce qui n'est pas une observation sur le monde. C'est sans conséquence, mais je le note.

### (b) Conditions de perte de puissance

- **Seuil strict sans marge.** Sous H_0 d'échangeabilité, et sans égalité possible, P(gain strict) = 1/2 : la moitié des courses sans effet « falsifient H_B ». Avec des comptes discrets où les égalités sont fréquentes, l'issue penche au contraire par défaut vers « H_A falsifiée ». Dans les deux régimes, l'inférence forte n'est que formelle.
- **Bande de puissance de D-valeur.** Si la loi génératrice met une masse quasi nulle sur les jeux à perte stricte depuis l'état initial, les deux bras rendent 0. Si cette masse est forte, l'énumération trouve ces jeux immédiatement. Le duel n'a de puissance que dans la bande où les séparations sont rares mais structurées, et D ne dit pas comment s'y placer.
- **« Accord intégral » du noyau et du rejeu.** Zéro discordance sur n cas indépendants ne borne le taux d'erreur qu'à environ 3/n au niveau 95 % (de (1 − p)ⁿ = 0,05). L'accord intégral ne « falsifie » donc pas le complément : il rend seulement improbable un taux d'erreur supérieur à environ 3/n.
- **Certificats duaux rationnels.** Si leur taille binaire croît vite avec l'horizon, la vérification exacte sort du budget. L'issue est alors non jugeable, et non négative.

### (c) Contrôles négatifs fatals s'ils manquent

- **Séparations plantées dans des états inatteignables.** D énonce ce piège, mais sans lot planté de ce type, la vérification « perte depuis l'état initial » n'est jamais éprouvée.
- **Recherche aléatoire avec le même solveur, à budget égal.** L'énumération canonique impose un ordre de parcours. Sans ce contrôle, on ne sait pas si le gain vient du modèle ou d'un meilleur ordre.
- **Étiquettes de contraintes brouillées (D-frontière).** Si l'avantage persiste quand on permute les noms des contraintes, le système n'utilise pas leur sens.

---

## Sur la proposition E

### (a) Défauts de méthode

0. **Statuts.** E étiquette VÉRIFIÉ des références citées de mémoire, des jugements (« méthodologiquement », « structurellement ») et sa conclusion sur la part de chance. Je ne reprends pas ces statuts. L'attribution des auteurs de *PatternBoost* diverge entre A et E : référence à vérifier.
1. **M1 : non-unicité des duaux.** Un programme linéaire dégénéré admet un ensemble de duaux optimaux, et le solveur rend un sommet qui dépend de sa règle de pivot. Interpoler y*(m) en fonction de m teste alors le solveur, pas le problème. Le test de mort « support non interpolable » peut tuer M1 sur un artefact. À l'inverse, un support « structuré » peut n'être qu'un effet de la règle de pivot.
2. **M1 : l'étape « pour tout (n, d) » n'est pas finie.** A^⊤y*(n, d) ≥ c est une inégalité paramétrique. La ramener à `positivity` ou `linarith` est une HYPOTHÈSE, pas une réduction établie.
3. **M2 : propriété de trace et propriété de loi confondues.** Une hypothèse portant sur la loi jointe des moniteurs (par exemple une corrélation ≤ ρ) ne peut pas être « satisfaite par 90 % des traces ». Surtout, elle n'est confrontée qu'aux traces honnêtes. Une hypothèse vraie sous la loi honnête et violée sous la loi saboteuse passe donc par construction, alors que c'est exactement la faille qu'exploite la corrélation adverse.
4. **M2 : fuite par sélection.** Beaucoup d'hypothèses candidates sont confrontées à la même banque honnête, qui devient ainsi une donnée d'ajustement. Il faut une banque réservée.
5. **M2 : anti-tautologie mesurée par la longueur.** Le critère « pas d'implication en moins de 4 lignes » mesure une longueur de preuve. Une reformulation équivalente mais plus longue le franchit.
6. **M3 : monde clos et hypothèses inégales.** Battre trente bornes codées par les concepteurs ne dit rien de la trente et unième. De plus, une borne qui suppose davantage bat les bornes générales par construction. Le témoin doit satisfaire les hypothèses des deux bornes comparées.
7. **E3 : R2 à 0 % est vrai par construction.** Si les énoncés sont scellés par des humains et le noyau correct, un énoncé faux fidèlement formalisé ne peut pas être prouvé. E3 ne teste que R1 ; ce n'est pas un duel.
8. **E4 : deux énoncés non équivalents.** La version `Fintype` est plus faible que la version générale. Comparer leurs taux de clôture mesure la couverture de Mathlib. Le coût du relèvement du fini au général, qui est la question informative, n'est pas mesuré.
9. **Validité n'est pas puissance.** La moyenne de e-valeurs garantit le taux de fausses alertes sous dépendance arbitraire. La question cible de l'agrégateur porte aussi sur la détection, que cette réduction ne règle pas.

### (b) Conditions de perte de puissance

- **M1.** Le critère d'interpolation perd sa puissance dès que la face optimale primale ou duale est de dimension positive. Il faut alors un dual canonique fixé d'avance : centre analytique, support minimal ou ordre lexicographique.
- **M2.** Le test empirique d'une hypothèse distributionnelle n'a de puissance que si l'effectif effectif de la banque dépasse largement le nombre de paramètres de l'hypothèse. Or des traces groupées par tâche ont pour effectif le nombre de tâches, pas le nombre de traces.
- **M3.** Si les bornes classiques sont exactes sur les familles plantées (écart nul à V*), aucune séparation n'existe et le portier rejette tout. Si les familles sont hors du régime classique, n'importe quelle borne sépare. Le portier n'a de puissance qu'entre ces deux situations.
- **E2.** Les 24 instances issues de 12 mondes ne sont pas indépendantes : l'effectif réel est d'environ 12. Le seuil « fausses alertes ≤ 5 % » sur 24 instances revient à exiger zéro fausse alerte. Enfin, si le bras LP peut calculer en m′ = 50, la validation hors échantillon fuit : m′ doit lui être caché.

### (c) Contrôles négatifs fatals s'ils manquent

- **Traces saboteuses pour M2.** Sans elles, une hypothèse n'est pas interprétable comme supposition d'un moniteur.
- **Programmes linéaires aléatoires sans structure pour M1.** Le système doit répondre « non interpolable » au lieu d'ajuster une formule.
- **Borne plantée qui ne bat les bornes classiques que par une hypothèse supplémentaire, pour M3.** Si le portier la laisse passer, il est réfuté.
- **Générateur aléatoire d'hypothèses, à budget égal, dans M2.** Duel : H_A, « l'arène trouve des hypothèses que le hasard ne trouve pas » ; H_B, « la survie s'explique par le double verrou seul ». Si le hasard survit aussi souvent, c'est le verrou qui fait le travail, et l'apport de l'arène est réfuté. Sinon, H_B est réfutée.
- **Même théorème sous deux encodages équivalents, pour E4.**

---

## Ce que je ne sais pas

- Si les dates de coupure des modèles permettent de constituer, dans ce domaine, un lot postérieur à T non contaminé.
- Si les problèmes adverses des cinq cibles sont des programmes linéaires (L = V*, et les critères de C et E retrouvent leur puissance) ou des problèmes non convexes. Plusieurs critiques ci-dessus en dépendent. Je ne peux pas trancher sans les définitions gelées.

FIN-DE-CELLULE
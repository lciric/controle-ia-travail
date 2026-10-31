*Hors tour : contenu des familles, choix des bancs ou jeux de données, et organisation des concepteurs.*

## (a) Ce que la question suppose sans l’établir

- L’accès privilégié à θ améliore la défense sur familles inédites, à budget égal : **HYPOTHÈSE**.
- Cet accès réduit \((ii)-(iii)\) plutôt qu’il ne se contente d’augmenter \((i)\) : **HYPOTHÈSE**.
- L’invariance à une reparamétrisation distingue apprentissage des lois et apprentissage des coordonnées : **HYPOTHÈSE**.
- Le générateur à budget fini approche suffisamment la pire loi accessible : **HYPOTHÈSE** ; son cadre d’information est lui-même **HYPOTHÈSE** (fait 4).
- Même schéma et graines scellées garantissent l’indépendance informationnelle des familles tenues à l’écart : **HYPOTHÈSE** ; la discipline de scellement est **RAPPORTÉ** (fait 5).
- Un transfert positif hors classe n’est pas acquis : les signes publiés sont mitigés (**RAPPORTÉ**, fait 11).

## (b) Duels décisifs

Les intervalles ci-dessous sont des IC appariés à 95 % (illustratif), obtenus par bootstrap de mondes.

**Duel 1 — quantité qui tranche.** Pour le bras \(b\), \(G_b=S_{ii,b}-S_{iii,b}\), et \(R=G_2-G_1\).  
\(H_A:R\geq\delta\), \(H_B:R<\delta\), avec \(\delta=0{,}03\) point de probabilité (illustratif). Une borne inférieure d’IC \(\geq\delta\) falsifie \(H_B\) ; une borne supérieure \(<\delta\) falsifie \(H_A\). Contrôle négatif : répéter le contraste entre deux évaluations du même bras 2, avec graines indépendantes ; franchir \(\delta\) révèle un biais de simulation ou de générateur.

**Duel 2 — reparamétrisation.** Soit \(Q\) la perte appariée de détection sur \((ii)\), après réentraînement complet avec \(\theta'=g(\theta)\), lois et graines inchangées.  
\(H_A:|Q|\leq\epsilon\) : invariance compatible avec l’apprentissage des lois ; \(H_B:|Q|>\epsilon\) : dépendance à la paramétrisation ; \(\epsilon=0{,}02\) (illustratif). Une borne supérieure \(\leq\epsilon\) falsifie \(H_B\) ; une borne inférieure \(>\epsilon\) falsifie \(H_A\). Contrôle négatif : réétiqueter θ seulement à l’évaluation, sans réentraînement, doit produire un changement nul puisque θ n’entre pas dans la défense figée.

## (c) Mesure minimale des instruments

Plan commun : mondes à vérité connue, avec \(P_0\), chaque \(P_\theta\), le niveau de dépendance et, sur une grille finie de Θ, la pire loi contre chaque défense figée connus par construction.

- **Défense** : sur tirages déplacés indépendants et cas honnêtes appariés par graine, mesurer détection et fausses alertes au point imposé de 1 %. Elle doit battre, à fausses alertes égales, un test MMD à noyau et règle fixés, sans apprentissage, sur \((ii)\) et \((iii)\). Sous \(P_\theta=P_0\), tout excès durable de fausses alertes invalide l’étalonnage.
- **Générateur** : après \(B\) évaluations, mesurer le regret \(\rho=p_D(\hat\theta)-\min_{\theta\in\Theta}p_D(\theta)\), avec confirmation sur tirages frais. Il doit réduire \(\rho\) par rapport à une recherche aléatoire de même budget. Sur une défense constante en θ, \(\rho\) doit être nul.
- **Dépendance** : vérifier erreur et classement des niveaux connus nul/faible/fort. Deux échantillons indépendants d’une même distribution de lois servent de contrôle nul.
- **Reparamétrisation** : le test doit classer invariante une défense construite sur des statistiques de loi, et faire chuter une défense témoin construite comme table de coordonnées. L’application identité constitue le contrôle négatif.

## Bloc 1 — Compatibilité des deux règles

**Mode déclaré : θ est une entrée auxiliaire présente à l’entraînement seulement, distillée dans une défense opérationnelle qui ne reçoit ensuite que des activations.**

Les règles sont compatibles : elles portent sur des étapes différentes. À l’entraînement, θ peut guider une représentation couvrant plusieurs lois et faire jouer la défense en dernier. À l’évaluation, la défense et son seuil sont figés ; le générateur peut alors choisir θ après elle, sans autre accès que ses sorties.

L’avantage peut donc améliorer **la défense apprise**. Il fausse **le chiffre publié** si les paramètres, activations ou résultats des familles tenues à l’écart servent encore à choisir un réglage, un point de contrôle ou un seuil, ou si θ est fourni pendant la mesure.

Il cesse d’être légitime dès que ces informations d’évaluation alimentent la sélection ou l’étalonnage. La sélection interne utilise uniquement des familles de développement du programme, distinctes des familles tenues à l’écart. Le seuil est étalonné sur des cas honnêtes de référence séparés. Après gel, aucune adaptation n’est permise pendant \((ii)\), \((iii)\) ou les requêtes du générateur.

## Bloc 2 — Trois scores et dépendance

Pour une défense figée \(D\), une agrégation fixe \(T_n\) et son seuil \(\tau\), soit  
\[
p_D(\theta)=\Pr_{P_\theta}(T_n\geq\tau).
\]
Chaque réplication utilise \(n\) activations fraîches ; tous les scores sont des taux de détection à 1 % de fausses alertes.

1. **Score (i)** : moyenne de \(\hat p_D(\theta)\) sur les familles d’entraînement, avec tirages frais. Unité : famille dans un monde. IC bootstrap hiérarchique mondes puis familles.
2. **Score (ii)** : même moyenne sur les familles fixes tenues à l’écart, lues après gel. Unité : famille dans un monde ; même type d’IC.
3. **Score (iii)** : après gel, le générateur effectue \(B\) évaluations déclarées et retient \(\hat\theta\) minimisant la détection estimée. Le score est la moyenne de \(p_D(\hat\theta)\), confirmée sur tirages frais. Unité : coup du générateur dans un monde ; IC bootstrap mondes puis coups.

**Prédictions.** \((i)-(ii)\geq0\) si les familles vues ne sont pas intrinsèquement plus faciles et si l’apprentissage leur est spécifique ; le signe peut s’inverser si les familles tenues à l’écart sont plus faciles. \((ii)-(iii)\geq0\) si le générateur trouve des lois plus difficiles que la famille tenue à l’écart moyenne ; un échec de recherche peut annuler ou inverser l’écart.

La dépendance vient de supports ou points θ communs, de lois proches ou dupliquées, ou d’une distribution des familles tenues à l’écart construite à partir de celle d’entraînement. Le même schéma ne suffit pas.

Mesure invariante par reparamétrisation :
\[
D_{\mathrm{dep}}=\frac1{K_*}\sum_{j\in\text{tenues à l’écart}}
 \min_{k\in\text{entraînement}}
 \frac{\mathrm{KL}(P_j\|P_k)+\mathrm{KL}(P_k\|P_j)}2 .
\]
On prédit que \((i)-(ii)\) croît avec \(D_{\mathrm{dep}}\), à difficulté moyenne contrôlée, et on ajuste une régression monotone par bras et régime.

## Bloc 3 — Expérience décisive à budget égal

**Budget.** Unité commune \(U\) : nombre de vecteurs synthétiques générés pour entraînement et boucle. Capacité, initialisations, mises à jour et \(U\) sont appariés ; les mesures finales, séparées, ont aussi des budgets égaux.

**Bras.**

1. Boucle de générations ; après chaque lot proposé, la défense est mise à jour en dernier avec activations et θ.
2. Mêmes familles, graines et déroulement ; activations seulement.
3. Banque fixe de familles, sans boucle ; activations seulement.
4. Boucle du champ : après chaque mise à jour de la défense, entraînée sur échantillons des lots antérieurs, le générateur optimise en dernier contre elle, figée pendant son coup ; jamais de θ.
5. Bras 1 à deux échelles : palier rapide explicite — règles, seuils, agrégation et mémoire de cas validés par la vérité simulée — entre lots ; poids lents réentraînés entre générations. Aucune règle propre à une famille ; aucune famille tenue à l’écart dans l’expérience. Les deux paliers sont figés avant \((ii)\) et \((iii)\).

Les régimes imposent un support commun ou disjoint. Dans chaque monde, les familles tenues à l’écart sont tirées avec graine scellée, jamais utilisées pour entraîner, sélectionner ou étalonner, puis lues une fois par bras, régime et condition de reparamétrisation après gel. Les répétitions de puissance créent de nouveaux mondes et de nouvelles familles.

Pour la reparamétrisation, un évaluateur indépendant choisit et scelle \(g\). Elle transforme les θ d’entraînement et de développement **avant un réentraînement complet** ; transformer seulement les étiquettes à l’évaluation serait non informatif.

**Décisions.** Avec \(\delta_C=\delta_E=0{,}03\) (illustratif), succès de conception si les bornes inférieures des IC de \(S_{ii,1}-S_{ii,2}\) et \(S_{iii,1}-S_{iii,2}\) dépassent \(\delta_C\) ; succès d’évaluation si \(R\geq\delta_E\) selon le duel 1. Échec si le gain ne porte que sur \((i)\), ou si une borne supérieure exclut le gain minimal requis. Contrôle négatif : deux copies du bras 2 ne doivent produire aucun contraste franchissant ces seuils.

**Puissance.** Illustratif : 100 mondes, 32 familles d’entraînement et 32 tenues à l’écart, 2 000 tirages par famille, \(B=100\), effet supposé de +0,05 ; 500 réplications complètes estiment la fréquence des décisions correctes. Aucune puissance n’est calculée ici.

**Prédictions de \((ii)-(iii)\), en points de probabilité — toutes illustratif, non résultats :**

| Bras | Support commun | Support disjoint |
|---|---:|---:|
| 1 | +0,05 | +0,17 |
| 2 | +0,11 | +0,16 |
| 3 | +0,15 | +0,24 |
| 4 | +0,08 | +0,20 |
| 5 | +0,04 | +0,12 |

## Bloc 4 — La quantité qui tranche

La quantité est
\[
R=(S_{ii,2}-S_{iii,2})-(S_{ii,1}-S_{iii,1}).
\]
\(R>0\) signifie que l’information θ réduit l’optimisme du score tenu à l’écart relativement aux échantillons seuls.

Son estimateur est la moyenne des différences ci-dessus dans les mondes appariés, chaque score étant estimé sur tirages frais ; l’IC est un bootstrap de mondes, séparément par régime. L’effet minimal est \(\delta_E=0{,}03\) point de probabilité (illustratif).

Je prédis \(R\geq\delta_E\) sous support commun, si \(D_{\mathrm{dep}}\) reste faible et si le test de reparamétrisation est invariant. Sous support disjoint et forte nouveauté des lois, le signe peut s’annuler ou s’inverser. Une borne supérieure d’IC inférieure à \(\delta_E\) falsifie la prédiction de réduction minimale ; une borne inférieure supérieure ou égale à \(\delta_E\) falsifie l’absence de cette réduction.

## Bloc 5 — Conclusion

**Verdict actuel : bonne pour aucune au sens d’un résultat établi**, puisque P-041 est seulement une conception, sans construction ni mesure (**VÉRIFIÉ**, fait 3). Elle deviendrait bonne **pour les deux** si, à budget égal, le bras 1 dépassait le bras 2 d’au moins \(\delta_C\) sur \((ii)\) **et** \((iii)\), et si \(R\geq\delta_E\).

Sous support commun et faible \(D_{\mathrm{dep}}\), c’est la prédiction retenue. Sous support disjoint ou forte nouveauté, le gain peut disparaître et le verdict rester « aucune » ou se limiter à la conception. Une chute de reparamétrisation supérieure à \(\epsilon\) invalide l’interprétation par apprentissage des lois ; l’invariance seule ne prouve pas l’universalité. Le chiffre publié reste dans tous les cas \((iii)\).

## (d) Ancrage matériel

Aucun modèle ouvert requis. Illustratif : \(2\times10^9\) vecteurs synthétiques de dimension 16, environ 4 000 heures-CPU, 300–800 € de location, quelques jours sur 64 cœurs, stockage inférieur à 1 To. Les estimations de puissance peuvent être parallélisées par monde.

FIN-DE-CELLULE
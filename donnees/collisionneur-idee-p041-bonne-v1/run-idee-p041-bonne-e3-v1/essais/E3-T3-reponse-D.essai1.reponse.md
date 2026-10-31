Je réponds uniquement aux sections des critiques A, B et C qui visent **D**.

## (a) Sort de chaque critique

### Critiques de A

| Critique | Décision |
|---|---|
| **A.a1 — court-circuit du maître** | **Acceptée.** Un maître recevant \((x,\theta)\) pouvait ignorer \(x\) et ne transmettre que l’étiquette de déplacement. Je supprime maître et distillation : \(\theta\) devient uniquement une **cible auxiliaire prédite depuis les activations**. |
| **A.a2/A.a3 — budget et origine des lots** | **Acceptées.** Toutes les consommations entrent dans le budget ; les bras 1 et 2 recevront une trajectoire commune de familles, produite contre une défense de pilotage tierce, et non contre l’un des deux bras. |
| **A.a4 — contrôle de reparamétrisation trivialement nul** | **Acceptée.** Je le remplace par des réentraînements identité à graines nouvelles, estimant le plancher de variabilité. |
| **A.a5 — regret possiblement négatif** | **Acceptée.** Le générateur et l’oracle de référence seront restreints à la même grille finie \(\Theta\), rendant le regret non négatif. |
| **A.a6 — KL non calculable sans classe déclarée** | **Acceptée.** Je déclare ci-dessous une classe gaussienne identifiable, à support plein et à KL analytique. |
| **A.a7 — unité du score (iii)** | **Acceptée.** Un monde fournit un seul coup final du générateur et un seul \(\hat\theta\), confirmé sur tirages frais ; aucune moyenne de minima locaux. |
| **A.a8 — verdict “aucune” automatique** | **Acceptée.** Je retire ce verdict factuel vide. Seul reste un verdict conditionnel, effectivement réfutable par les mesures. |
| **A.a9 — \(g\) non contrainte** | **Acceptée.** La classe des transformations est restreinte et validée instrumentalement avant usage. |
| **A.b — sonde du maître, seuil, dimension/budget du générateur, plafonds, dépendance, variance de réentraînement, difficulté** | **Acceptées comme conditions de jugeabilité.** La sonde du maître devient sans objet ; les autres donnent lieu à l’étalonnage, au contrôle du regret, au contrôle de saturation et à l’appariement par difficulté-oracle décrits plus bas. |
| **A.c — contrôles manquants** | **Acceptées**, avec deux précisions : la sonde du maître est remplacée par un diagnostic d’apprentissage de la cible auxiliaire ; le \(\theta\) permuté est un diagnostic de destruction d’information, non un nul devant nécessairement égaler le bras 2, car il peut créer une supervision contradictoire. Le contrôle d’attribution principal utilise une cible constante non informative. Recherche aléatoire et défense constante sont conservées. |

### Critiques de B

| Critique | Décision |
|---|---|
| **B.a1 — mécanisme de distillation ambigu** | **Acceptée.** Le mécanisme est remplacé par la cible auxiliaire explicitée ci-dessous. |
| **B.a2 — mauvais contrôle négatif du duel 1** | **Acceptée en partie.** Deux copies du bras 2 contrôlent le pipeline et la dispersion nulle, pas l’effet de \(\theta\). J’ajoute le bras 1 à information auxiliaire constante, à architecture et calcul identiques. |
| **B.a3/B.b reparamétrisation — variance de réentraînement** | **Acceptées.** Plusieurs réentraînements identité précèdent le choix du seuil du test. |
| **B.a4 — coût matériel** | **Acceptée en partie.** Le montant annoncé n’était pas justifié par un décompte reproductible : je le retire, en attendant un benchmark pilote. La seule comparaison avec les coûts d’autres plans ne démontre toutefois pas une incohérence, leurs périmètres n’étant pas identiques. |
| **B.a5 — monotonie de \(D_{\mathrm{dep}}\) non démontrée** | **Acceptée.** Je ne suppose plus de monotonie globale ; elle devient une relation à tester à difficulté-oracle contrôlée. |
| **B.a6 — absence de seuil de regret** | **Acceptée.** Un regret excessif invalide le monde ou le plan au lieu d’être interprété comme un effet des bras. |
| **B.b — \(K\), tirages frais et puissance** | **Acceptées.** \(K\), le nombre de mondes, les tirages de confirmation et l’étalonnage seront dimensionnés par simulation de puissance. |
| **B.b — prédiction seulement en support commun** | **Transformée en test.** Les deux régimes deviennent des analyses préenregistrées séparées, avec une prédiction explicite pour chacun ; le support disjoint est prioritaire pour la prétention d’universalité. |
| **B.c — contrôles de saturation, capacité et difficulté** | **Acceptées.** Ils sont intégrés aux préconditions de validité, avec appariement de la distribution de difficulté-oracle. |

### Critiques de C

| Critique | Décision |
|---|---|
| **C.a1 — difficulté intrinsèque confondue avec nouveauté** | **Acceptée.** La difficulté est mesurée par la puissance \(p^*\) du test du rapport de vraisemblance, indépendante des défenses apprises. |
| **C.a2 — fuite possible par les familles de développement** | **Acceptée.** Le développement est tiré uniquement du support d’entraînement, jamais de la distribution tenue à l’écart, et consomme le budget déclaré. |
| **C.a3/C.c3 — \(g\) peut dégrader seulement l’optimisation** | **Acceptées.** Transformations à conditionnement préservé, convergence vérifiée et témoins positif/négatif obligatoires. |
| **C.b1 — KL infinie ou saturée** | **Acceptée.** La classe finie, gaussienne et non dégénérée garantit des KL finies ; toute relation avec \((i)-(ii)\) reste testée par strates de \(p^*\), sans pente imposée. |
| **C.b2/C.c2 — aveuglement du générateur** | **Acceptées.** Le regret est mesuré par bras ; son dépassement du seuil de validité rend le contraste non jugeable, notamment pour éviter qu’un générateur découvre plus facilement les failles larges du bras 2. |
| **C.b3 — zone d’indécision du duel 1** | **Rejetée comme défaut logique :** \(R\geq\delta\) et \(R<\delta\) sont exclusives et exhaustives. **Acceptée comme exigence de puissance :** un intervalle chevauchant \(\delta\) est non concluant, et le plan doit borner cette éventualité aux valeurs de décision. |
| **C.c1 — absence de contrôle \(\theta\) brouillé** | **Acceptée.** La distillation étant supprimée, le confondant particulier d’auto-distillation disparaît ; cibles constante et permutée sont néanmoins conservées comme contrôles distincts. |

## (b) Expériences corrigées

### Mode, classe et bras

La défense opérationnelle ne reçoit que des activations. Au bras 1, une tête auxiliaire d’entraînement prédit \(\theta\) depuis ces activations ; la tête est ensuite retirée. Le bras 2 conserve architecture, paramètres, pas d’optimisation et tête auxiliaire, mais avec une cible constante indépendante de \(\theta\). Les cas honnêtes utilisent le paramètre de référence lorsque cette cible existe.

La classe proposée est \(P_\theta=\mathcal N(\mu,\Sigma)\), avec \(\theta=(\mu,\operatorname{vech}\Sigma)\), donc \(\theta\mapsto P_\theta\) injective. \(\Theta\) est une **grille finie déclarée**, sans covariance singulière ; les lois ont support plein et les KL symétrisées sont analytiques et finies. La loi de référence appartient au schéma.

Les bras 1 et 2 partagent familles, lots et graines, produits dans une boucle contre une défense de pilotage commune. Le bras 3 reste sur banque fixe ; le bras 4 conserve son générateur jouant contre sa propre défense du moment ; le bras 5 reprend le bras 1 avec ses deux paliers, figés avant les mesures.

L’unité \(U\) est le nombre de vecteurs synthétiques traités par une défense, en comptant entraînement, requêtes du générateur, développement et étalonnage. Les vecteurs générés et les pas d’optimisation sont également appariés. Les mesures finales ont des budgets séparés et égaux. Les familles tenues à l’écart ne servent jamais à entraîner, sélectionner ou étalonner et restent lues une seule fois après gel, par condition prévue.

### Scores et validité instrumentale

Tous les scores restent des détections à **1 % de fausses alertes**, point fixé par la question. Le score (iii) repose sur un seul \(\hat\theta\) par monde, défense et régime, choisi après \(B\) évaluations déclarées, puis estimé sur tirages frais indépendants. Le regret est
\[
\rho_b=p_{D_b}(\hat\theta_b)-\min_{\theta\in\Theta}p_{D_b}(\theta)\geq0,
\]
le minimum étant audité sur la même grille. \(B\) est fixé après un pilote de saturation. Une confirmation insuffisamment précise, un plafond/plancher empêchant l’effet minimal, ou \(\max(\rho_1,\rho_2)>\rho_{\max}\), avec \(\rho_{\max}<\delta_E/3\) (**illustratif**), rendent le contraste non jugeable.

Pour chaque famille, \(p^*\) est la puissance oracle du rapport de vraisemblance au même point de fonctionnement. En support disjoint, les familles tenues à l’écart sont tirées de façon que leur distribution de \(p^*\) soit appariée à celle d’entraînement selon une tolérance préenregistrée. \(D_{\mathrm{dep}}\) est comparée à sa valeur sous deux ensembles indépendants issus de la même distribution de lois ; son association avec \((i)-(ii)\) est testée dans des strates de \(p^*\).

Les nombres de mondes, de familles, de tirages honnêtes et de tirages frais sont choisis par simulation afin que bruit d’étalonnage, erreur de confirmation et largeur d’intervalle soient compatibles avec \(\delta_E\). Aucun résultat de puissance n’est affirmé ici.

### Duels corrigés

**Duel 1.** Dans des mondes appariés,
\[
R=(S_{ii,2}-S_{iii,2})-(S_{ii,1}-S_{iii,1}).
\]
Pour chaque régime : \(H_A:R\geq\delta_E\), \(H_B:R<\delta_E\), avec \(\delta_E=0{,}03\) point de probabilité (**illustratif**). Une borne inférieure d’IC bootstrap de mondes \(\geq\delta_E\) falsifie \(H_B\) ; une borne supérieure \(<\delta_E\) falsifie \(H_A\) ; sinon, indécision. **HYPOTHÈSE :** \(R\geq\delta_E\) en support commun à faible dépendance ; \(R<\delta_E\) en support disjoint à forte nouveauté. Deux copies du bras 2 contrôlent le nul du pipeline ; la cible constante contrôle l’attribution à \(\theta\).

**Duel 2.** Un évaluateur indépendant scelle \(g\) dans une classe d’isométries affines préservant le conditionnement de la perte auxiliaire, puis transforme les cibles d’entraînement et de développement avant réentraînement complet, à lois et graines inchangées. Le plancher de \(Q\), perte appariée sur (ii), est estimé par réentraînements identité. \(H_A\) : invariance \(|Q|\leq\epsilon\) ; \(H_B\) : sensibilité \(|Q|>\epsilon\), avec décisions symétriques par intervalles. Une défense témoin fondée sur les lois doit rester invariante et une défense témoin sensible aux coordonnées doit chuter ; sinon l’instrument est non jugeable. L’invariance ne prouvera toujours pas l’apprentissage universel des lois.

## (c) Réponse à l’arbitre — une page

**Verdict.** Aucun verdict empirique n’est acquis : P-041 n’est ni construite ni mesurée (**VÉRIFIÉ**, fait 3). Le verdict conditionnel est **bonne pour les deux** si, à budget égal, les gains du bras 1 sur le bras 2 dépassent \(\delta_C\) sur **(ii) et (iii)**, et si \(R\geq\delta_E\), dans le régime considéré. Un gain sur (i) seul ne suffit pas. En support disjoint, si seuls les gains sur (ii)/(iii) subsistent, elle est au plus bonne pour la conception ; s’ils disparaissent, pour aucune. Une sensibilité de reparamétrisation supérieure au plancher de réentraînement invalide l’interprétation par apprentissage des lois et impose de corriger le bras 1 avant tout verdict favorable.

**Quantité qui tranche.** L’estimateur de \(R\) est la double différence appariée par monde, avec IC bootstrap de mondes, séparément par régime. Seuil : \(\delta_E=0{,}03\) (**illustratif**). Signe prédit : positif et supérieur au seuil en support commun (**HYPOTHÈSE**) ; sous le seuil en support disjoint (**HYPOTHÈSE**). Le chiffre publié demeure (iii).

**Expérience décisive corrigée :**
1. Comparer les cinq bras à \(U\) égal, avec trajectoire commune aux bras 1–2 et cible auxiliaire \(\theta\) contre cible constante.
2. Figer défenses et seuils, puis mesurer (ii) une fois et (iii) sur un coup unique confirmé hors échantillon.
3. Apparier la difficulté par \(p^*\), mesurer \(D_{\mathrm{dep}}\) et exiger un regret du générateur inférieur au seuil de validité.
4. Estimer \(R\) par mondes appariés dans chaque régime ; conclure seulement si les IC tranchent.
5. Valider séparément la reparamétrisation par réentraînements identité et défenses témoins.

**Établi / non établi.** L’absence de construction et de mesure est **VÉRIFIÉE** (fait 3). Les ordres de coups du champ et les signes mitigés du transfert sont **RAPPORTÉS** (faits 6–11). Ne sont pas établis : l’avantage de \(\theta\), le signe de \(R\), la saturation du générateur, la validité du test de reparamétrisation ni l’universalité.

**À faire en premier :** le pilote à vérité connue validant étalonnage, oracle \(p^*\), regret/saturation du générateur et témoins de reparamétrisation, avant tout entraînement comparatif des bras.

FIN-DE-CELLULE
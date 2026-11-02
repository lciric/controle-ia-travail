# Proposition D — Tour III.3

Le pilote complet, les 432 entrées `resultats` du calibrage et le PDF de Bailey et collègues ne sont pas servis ; je n’en reconstruis aucun contenu. **VÉRIFIÉ** désigne une lecture ou un recalcul sur les pièces servies ; les chiffres du pilote restent **OBSERVÉ-NON-AUDITÉ**, et ceux de sa vérification **RAPPORTÉ**.

## (a) Réponse aux critiques visant D

### Critiques de A

| Critique | Décision et réponse |
|---|---|
| E1 : les colonnes ne sont pas des réponses aux mélanges ; le gain est surestimé et peu informatif lorsque A est proche du plancher. | **Acceptée.** J’ajoute des colonnes de réponse aux mélanges candidats, une séparation sélection/évaluation et une garde de plancher. E1 ne conclura plus à partir de la seule valeur de la matrice initiale. |
| E2 : la version tabulaire ferme la bibliothèque et change le jeu ; les cellules produisent des historiques différents. | **Acceptée.** Je remplace le factoriel dynamique par un jeu fini fixé à l’avance, puis par des contrastes continus à un seul facteur. I3 n’est plus comparé entre cellules comme si leurs historiques étaient communs. |
| E3 : seuils non chiffrés ; nouvelle règle de sélection ; transfert aux tâches de décision non établi. | **Acceptée.** Les seuils seront dérivés d’une simulation de bruit puis gelés avant sélection. Toute nouvelle conception est un nouvel estimande, sans continuité revendiquée avec le pilote. Aucun transfert aux tâches de décision n’est supposé. |
| Mécanisme (a) : l’échec de pondérations testées ne réfute pas le rôle causal du mélange uniforme. | **Acceptée.** Il réfute seulement l’utilité des pondérations effectivement testées, dans le domaine évalué. |
| Mécanisme (e) : V et le déficit restreint ne sont pas des confirmations indépendantes. | **Acceptée sur la non-indépendance.** Je retire cette double confirmation. Je ne fais pas pour autant de « valeur restreinte − V » une définition de NashConv. |
| Distance fonctionnelle : banque propre insuffisante ; contrôle d’échelle absent. | **Acceptée.** La banque comprendra des lois d’attaque tenues ; les contrôles incluront reparamétrisations fonctionnellement identiques et moniteurs identiques sur le propre mais différents sur une loi tenue. |
| Exploitabilité approchée et puissance à N = 24. | **Acceptée.** Un petit gap local ne prouvera plus une convergence. Les effectifs seront fixés par simulation de puissance ; un effet proche du plancher ou un intervalle couvrant le seuil restera non tranché. |
| La cellule « attaquant historique × défenseur actuel » doit reproduire la convergence exacte du jeu fictif bilatéral. | **Rejetée telle quelle.** Un défenseur approché n’a pas à reproduire un théorème de réponses exactes. Je transforme l’exigence en contrôle d’instrument : la convergence doit être retrouvée dans le jeu fini exact ; dans les cellules continues, je contrôle séparément la force des deux attaquants. |
| I3 : attaquant de trajectoire faible et départ chaud ; l’audit existant ne contrôle presque pas la forme. | **Acceptée et transformée en test préalable E0b**, avec attaquant renforcé, nouvelles graines et suppression du départ depuis l’attaque du tour. |

### Critiques de B

- **Sous-spécification d’E1 : acceptée.** **VÉRIFIÉ** : le code ne construit pas de matrice d’équilibre pour A analogue à celle de B/B′. Il faudra la construire explicitement ; la matrice H de cycle ne suffit pas.
- **« Extension défensive indépendante » dans E3 : rejetée.** Ce dispositif ne figure pas dans ma conception D. Mon E3 porte sur l’intérieur de l’équilibre et la posabilité de Q2, non sur une extension de bibliothèque.
- **Gap global non calculable : acceptée.** NashConv exact reste la métrique des jeux finis résolus ; dans le monde continu, je rapporte une détection contre réponses fraîches auditées et des quantités restreintes explicitement nommées, jamais un « gap global certifié ».
- **Rang presque dégénéré, puissance du factoriel, seuil d’E4, contrôle M0 et qualité de l’attaquant historique : acceptées.** J’ajoute diagnostics de rang/support, calcul de puissance préalable, gel du seuil de transfert, prédictions pour M0 et benchmark des attaquants sur défenses fixes.
- **Matrices analytiques de calibration pour E3 : acceptées**, y compris lignes dupliquées, équilibre intérieur connu et ligne dominante.

### Critiques de C

- **E1 confond échec de la mixture fraîche et absence de cycle : acceptée.** J’évalue séparément le gain sur l’historique et le gain contre une réponse fraîche. Un succès historique suivi d’un échec frais indiquera une couverture insuffisante de la trajectoire, non l’absence de cycle.
- **Fuite dans la table dynamique d’E2 : acceptée.** La table sera fixe et antérieure à toute trajectoire analysée, ou l’expérience sera limitée à un contraste continu sans prétendre à une réponse exacte.
- **Sur une tâche dont l’équilibre est un singleton pur, entropie ou minimisation du poids maximal rendent le même poids pur : acceptée.** Ces règles ne « réparent » pas les tâches pures du pilote. E3 cherchera de nouvelles cellules de conception préenregistrées, à classe finale égale entre B′ et D.
- **Pureté déclarée avec une tolérance très inférieure au bruit de G : acceptée.** La conclusion structurelle exigera désormais une marge supérieure à l’incertitude propagée et une confirmation sur matrice fraîche.
- **Distance binaire bornée sur le propre et contrôle de complétude : acceptées.** La banque mixte propre/attaques tenues et la colonne extérieure à la table deviennent obligatoires.

### Critiques de E

- **NashConv nul sur la matrice dont on vient de résoudre l’équilibre : acceptée.** Ce contrôle valide seulement le solveur. Une colonne tenue, exploitable, devra montrer que le diagnostic externe ne s’annule pas avec lui.
- **E1 ne teste pas “aucune mixture” : acceptée.** La conclusion portera uniquement sur les mixtures des moniteurs observés de A et les réponses effectivement auditées.
- **Les deux explications d’E2 peuvent être vraies ensemble : acceptée.** Les facteurs sont testés séparément ; aucune alternative causale exhaustive n’est revendiquée.
- **Mélange disponible contre mélange nécessaire : acceptée.** J’ajoute le critère \(v(G)-d(G)\), où \(d(G)=\max_i\min_jG_{ij}\). Des lignes optimales dupliquées doivent donner un avantage mixte nul.
- **E4 : un intervalle imprécis n’est pas une réfutation : acceptée.** Seule une borne supérieure excluant l’effet revendiqué réfutera celui-ci ; un intervalle couvrant le seuil restera indéterminé.
- **Sélection/confirmation sur lots distincts et dépendance par source : acceptées**, avec permutations groupées pour le transfert réel.

## (b) Expériences corrigées

### Règle commune de décision

Pour chaque paramètre \(\vartheta\), je préenregistre \(H_A:\vartheta>c\) et \(H_B:\vartheta\le c\), avec \(c\) gelé avant lecture. Une borne inférieure \(>c\) falsifie \(H_B\) ; une borne supérieure \(\le c\) falsifie \(H_A\) ; sinon le résultat est **indéterminé**. Les recherches d’oracles et les évaluations utilisent des graines distinctes. M0 figé, M0 dupliqué et une défense figée à équilibre connu sont des contrôles : la stabilité seule n’est jamais un succès.

### E0 — Validation des instruments, avant tout mécanisme

1. Sur pierre–feuille–ciseaux, pile ou face apparié et un jeu à stratégie dominante, vérifier gains et équilibres analytiques avec OpenSpiel, puis un second solveur.  
2. Exécuter meilleure réponse itérée et jeu fictif bilatéral exact ; calculer NashConv du dernier profil et des stratégies moyennes, sans I3 comme critère de convergence.  
3. Bruiter des matrices à équilibre intérieur, à ligne dominante et à lignes dupliquées ; vérifier solveur, propagation de l’incertitude et \(v-d\). Ajouter une colonne extérieure exploitable pour tester la non-fermeture.  
4. Valider la distance fonctionnelle sur reparamétrisations, moniteurs dupliqués et moniteurs identiques sur le propre mais distincts sur une attaque tenue.  
5. **E0b :** rejouer A avec attaquant renforcé, sans départ depuis l’attaque du tour ; mesurer sa force sur défenses fixes et recalculer I3 avec une valeur nulle adaptée aux égalités et à la dépendance.

**Duel :** \(H_A\) : les instruments retrouvent les résultats connus et l’excès de retours est robuste à cette réplication ; \(H_B\) : ils échouent, ou l’excès disparaît sous le contrôle. La réussite falsifie \(H_B\) ; l’échec falsifie \(H_A\) et bloque toute lecture causale du cycle. I3 reste descriptif.

### E1 — La trajectoire de A contient-elle une défense moyenne utile ?

Construire les trois défenses issues des **mêmes moniteurs de A** : dernier moniteur, mixture uniforme, mixture d’équilibre choisie sur un lot de sélection. Ajouter pour chaque mixture une colonne « réponse au mélange », puis évaluer sur un lot frais avec attaquant indépendant. Mesurer séparément :

- le gain sur les attaques historiques ;
- le gain contre une réponse fraîche ;
- FPR, détection récente et couverture/rang de la bibliothèque.

Le duel principal porte sur \(\vartheta=V_{\mathrm{frais}}(p_A^*)-V_{\mathrm{frais}}(m_T^A)\). Son issue ne dit rien, à elle seule, de l’existence d’une orbite périodique. Un gain historique sans gain frais falsifie l’interprétation « déployer la moyenne suffit », pas le constat de cycle. Si A est trop proche du plancher pour trancher à la marge gelée, la cellule est non jugeable.

### E2 — Myopie adverse et approximation, sans les confondre

**E2a, jeu fini fixe :** bibliothèque et gains fixés avant les trajectoires, réponses exactes sur le même domaine. Comparer attaquant myope et attaquant historique à règle défensive inchangée.  
\(\vartheta\) est la différence d’exploitabilité exacte du dernier profil entre les deux régimes. Le résultat identifie un effet de la myopie **dans ce jeu**, sans prétention au monde continu.

**E2b, monde continu :** même contraste, mais sans prétendre à des réponses exactes. Chaque attaquant est audité sur défenses fixes communes ; si leurs forces diffèrent au-delà de la tolérance gelée, le contraste dynamique est non interprétable. L’erreur d’oracle défensif est testée séparément, sur **la même fonction objectif et le même domaine**, jamais en fermant la bibliothèque au cours du jeu.

### E3 — Q2 réellement exercée, pas seulement des poids diffus

Sur une grille de conceptions gelée, chaque cellule compare B′ et D à **classe finale et paramètres déployés égaux** ; elle constitue un nouvel estimande. Une variante de D à capacité constante distingue classe finale et croissance de capacité.

Une cellule n’est recevable que si :

1. sur la matrice de sélection, \(v(G)-d(G)\) dépasse la marge gelée **plus l’incertitude propagée** ;
2. la mixture retenue n’est pas une redistribution entre lignes fonctionnellement dupliquées ;
3. sur matrice et attaques fraîches, y compris une réponse à cette mixture, l’avantage mixte reste supérieur à la marge ;
4. primal/dual, valeur et déploiement sont mécaniquement vérifiés.

**Duel :** \(H_A\) : aucune cellule de la famille prévue ne satisfait ces conditions dans le budget gelé ; \(H_B\) : au moins une les satisfait. Une réussite falsifie \(H_A\) pour cette famille et rend Q2 posable dans cette cellule. Aucune réussite falsifie la recette explorée, pas l’existence d’autres mondes.

### E4 — Transfert réel conditionné

Un seul mécanisme ayant réussi le test synthétique est choisi avant ouverture des résultats réels. Le seuil d’effet est gelé ; sources et groupes de dépendance déterminent les partitions train/validation/test. La calibration utilise validation seule ; extraction, FPR, détection récente et réponses fraîches sont auditées.

Le duel porte sur le gain réel \(\vartheta>c\) contre \(\vartheta\le c\). Une borne inférieure \(>c\) falsifie l’absence de transfert utile pour ce modèle et ce protocole ; une borne supérieure \(\le c\) falsifie la revendication quantitative ; un intervalle couvrant \(c\) reste indéterminé. Un dépassement de FPR réfute la revendication composite « gain sans inflation du FPR ».

## (c) Réponse à l’arbitre : établi, non établi, première expérience

**Établi sur les pièces.** **VÉRIFIÉ** : A déploie le dernier moniteur linéaire, entraîné contre le mélange uniforme de toutes les attaques passées, cible initiale incluse ; l’attaquant répond ensuite au moniteur déployé. Le modèle final peut s’écrire comme un jeu à somme nulle : attaquant \(\theta\in\Theta_\delta\), défenseur \(m\) ou mixture \(p\), gain
\[
U(p,\theta)=\sum_i p_i\Pr_{x\sim\theta}[s_{m_i}(x)>t_{m_i}].
\]
Mais entraînement et attaque sont approchés, le seuil dépend du moniteur et le gain dur n’est pas l’objectif différentiable optimisé.

**OBSERVÉ-NON-AUDITÉ** : au pilote, A ne progresse presque pas et présente des retours au-delà de la valeur nulle retenue ; B est dominé par certains témoins ; B′ est souvent pur. Ces observations ne constituent ni une décision scellée ni une mesure de NashConv global.

**Non établi.** On ne sait pas si le phénomène vient principalement de la myopie adverse, de l’oracle, de la classe linéaire, de l’uniformité des poids ou de la couverture des attaques. L’oubli catastrophique n’est pas identifié. Le théorème de convergence des stratégies moyennes du jeu fictif bilatéral fini à somme nulle — Brown (1951), *Iterative Solution of Games by Fictitious Play* ; Robinson (1951), *An Iterative Method of Solving a Game* — ne s’applique pas directement au dernier itéré pur, unilatéral et approché étudié ici. Shapley (1964), *Some Topics in Two-Person Games*, fournit un précédent de non-convergence de dynamiques de meilleure réponse, pas une preuve pour cette arène. Aucun transfert publié vers des sondes d’activations n’est établi par les pièces ; pour Bailey et collègues comme pour les travaux adversariaux sur sondes : **référence à vérifier**.

**Métrique.** NashConv exact convient aux jeux finis résolus. Dans le monde continu, il faut rapporter séparément détection contre réponses fraîches auditées, déficit restreint et incertitude d’oracle. I1 mesure un progrès, I3 une forme de trajectoire ; ni l’un ni l’autre ne mesure NashConv. La distance fonctionnelle exige une banque couvrant des attaques tenues.

**Expérience à faire en premier : E0**, le contrôle croisé du jouet et du constat de cycle. Elle coûte moins qu’une nouvelle famille de mécanismes et détermine si les instruments distinguent réellement cycle, convergence triviale, bruit de matrice et faiblesse d’oracle. Ensuite seulement, **E1** teste si les moniteurs que A a déjà produits contiennent une défense moyenne utile ; c’est le test causal le plus direct du dernier itéré contre sa propre historique, sans ajouter un mécanisme nouveau.

FIN-DE-CELLULE
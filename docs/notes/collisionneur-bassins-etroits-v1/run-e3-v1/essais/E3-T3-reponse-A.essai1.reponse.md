# Proposition A — Tour III.3 : réponse aux critiques

Pièces reçues : ma conception (E3-T1-A) et quatre critiques (B, C, D, E), toutes complètes et lisibles. Je ne réponds qu'aux sections qui visent A. Je reprends plusieurs contrôles proposés par les autres en le disant à chaque fois (B1). Les statuts des faits sont inchangés ; tout chiffre hors faits est illustratif.

## (a) Verdict critique par critique

Je groupe par thème, chaque entrée attribuée à son auteur.

### A. Instrument et cible trop assortis (C a1, D a1, E a1 ; B « observation transversale »)

**Acceptée pour la portée, rejetée pour le mécanisme.** C, D et E ont raison : le duel 4.1 mesure si un modèle remplit une case que l'orchestrateur lui désigne vide ; il ne mesure pas « trouver un bassin étroit inconnu ». Ma section 3 disait déjà que M1 ne peut rien sur un bassin « sans forme » et parie sur une structure nommable sans oracle. Je retire donc toute formulation qui laisse entendre un gain général et je réécris la revendication : *M1 élève p_b pour la seule classe « interaction d'ordre ≤ 2 avec une condition déjà archivée »*. Je rejette l'idée que cela rende le duel vide : la question de l'arbitre désigne précisément cette classe (composante conditionnelle, HYPOTHÈSE des faits §4), et savoir si un proposeur remplit ou non une case désignée, à coût égal, est une inconnue réelle.

**Transformée en test** (C c1, D c, E c) : j'ajoute des mondes de transfert hors de la structure affichée — parité d'ordre 3, seuil décentré (condition au quantile 0,8, illustratif), monde additif — avec un duel de *non-infériorité* : M1 ne doit pas abaisser la couverture D2 sous celle de la vue brute quand la vérité est hors table (C b2, « dilution de l'attention »). C'est une issue falsifiante que je n'avais pas.

### B. Mesure produit et traits dépendants (B b, C b1, D a1, E a1, E b ; contrôles B c1, C c2, E c)

**Acceptée, et corrigée.** Sous une loi de traits non produit, les termes de Hoeffding-Sobol ne sont ni uniques ni orthogonaux, et les « cases nulles » affichées peuvent être fausses. Une décomposition généralisée sous dépendance existe (Chastaing, Gamboa, Prieur, vers 2012 ; référence à vérifier) mais rouvre le problème sous une autre forme. Je corrige plus simplement : **la table des cases vides ne sera plus une propriété de la mesure, mais de la fonction**. Pour une loi d'archive q de logit f_q écrit dans la grammaire, la paire (i, j) est « non croisée dans q » si et seulement si la différence mixte Δ_i Δ_j f_q est identiquement nulle sur la grille publique des traits (ou, sur traits continus, si f_q s'écrit g(x_{−i}) + h(x_{−j}) ; vérification symbolique sur la forme canonique, puis numérique sur grille). C'est indépendant de μ. Les grandeurs qui restent dépendantes d'une mesure (tailles des effets principaux) ne sont plus affichées ; seuls sont servis l'archive telle quelle et la table binaire des paires croisées/non croisées. **Conséquence honnête** : M1 ainsi corrigée coïncide avec « l'énumérateur mécanique » que B (c2) et D (a2) demandaient comme témoin. La machinerie de Möbius disparaît ; il reste une liste. Je le dis plutôt que de le masquer. Les mondes à traits corrélés (B c1, C c2) restent dans le banc, pour le regroupement par strates et pour la garde.

### C. Facteurs confondus dans le duel de vues (B a1, C a2, D a2, E a5, E c)

**Acceptée.** Le contrôle « archive permutée » conserve le format et l'injonction implicite « cherchez des interactions », et falsifie l'information au lieu de neutraliser la présentation (E). Je le remplace par le **placebo de B**, contraint par E : même format, même longueur, archive vraie intacte, table de paires tirée au hasard avec le même nombre de cases « non croisées » que la vraie. Seule la correspondance entre cases et traits réels est détruite. Si le placebo fait aussi bien que la vraie table, l'effet est une consigne de forme, pas une information.

### D. Témoin de coût incomplet (B a5, D a2, E a5)

**Acceptée.** Le bras A3 est redéfini **à budget total de jetons égal** (entrée + sortie), non à nombre d'appels égal ; le taux de cartes refusées par le gardien et le nombre de cartes valides par appel deviennent des métriques secondaires gelées ; la couverture est aussi rapportée par carte valide. Le calcul de la table est de coût marginal nul (CPU) mais sa longueur en jetons d'entrée est comptée.

### E. Unités non indépendantes et hypothèses non exhaustives (D a2)

**Acceptée.** Les six cartes d'un appel, les appels d'une même famille et les appels sur une même graine de monde ne sont pas indépendants. L'unité d'analyse devient la **graine de monde** ; les bras sont appariés par graine ; test par permutation exact stratifié par graine et par famille. Le duel unique à trois issues est éclaté en duels binaires (voir (b)).

### F. M2 : changement d'estimand, fuite de partition, identifiabilité (D a3, D b, C a3, C b3, E a2, E b)

**Acceptée ; la moitié « juge stratifié » de M2 est retirée.** D montre que la dérive stratifiée d_{π'} = wΔ_A + (1−w)Δ_Ā peut promouvoir une carte meilleure sur A et pire ailleurs — un gain sous π' qui n'est pas un gain sous π, la loi du monde. C ajoute que si la partition du juge est celle du générateur, il y a fuite, et que si A est orthogonal aux strates le facteur w/r vaut 1. Et la main de l'orchestrateur sur le tirage des traits était une HYPOTHÈSE. Trois raisons ; je retire. Ce qui reste de M2 : le **jeu public d'instances sans issue**, construit pour que chaque configuration de paire de signes (ou de quantiles) apparaisse au moins m fois (couverture de cellules, pas estimabilité d'une régression — E a2 est acceptée : je ne revendique plus qu'un tableau orthogonal « rende estimable »). Les strates sont définies par une règle écrite à partir de la description publique des traits **avant** la génération du monde (répond à C a3).

### G. M3 : prime de nouveauté résiduelle, saturation, surajustement (E a3, B a2, C b4, D a4, D c, E c)

**Partiellement acceptée.**
- E (garantie sous-modulaire sans objet pour un seul représentant) : acceptée ; la référence à Nemhauser-Wolsey-Fisher est retirée, le choix est un maximum direct.
- E (critère numérique de nouveauté dans la sélection) : **rejetée dans son principe, acceptée dans sa conséquence**. Le rejet du premier tour visait un score qui fait gagner une promotion. Ici les sœurs sont déjà déclarées équivalentes par le regroupement (chacune presque dans le nul engendré par l'autre, RAPPORTÉ faits §4) et une seule passe le test de mort : aucune carte n'est promue pour sa nouveauté. Mais E a raison que « couverture dirigée » est un critère numérique ; je le rétrograde donc à une **règle de départage** après la tranche appariée, non avant.
- C (saturation dans les strates rares) : acceptée ; le seuil par strate devient ε_s = ε + c·σ̂_s/√n_s (c préenregistré), sinon Ĉ(c) sature et le choix est aléatoire.
- B, D (strates sans lien avec les composantes ; surajustement au jeu public) : transformées en test — contrôle de D (groupes sans sœur porteuse mais avec écarts fortuits) et de E (sœur volontairement fausse, loin de l'archive sur beaucoup de strates) ; mondes de réglage distincts des mondes d'évaluation.

### H. M4 : transport, indépendance, taille du pilote (B a3, B b, D a5, D c, E a4, E b)

**Acceptée ; M4 est différée.** Le calcul de B (K_pilote > 250, illustratif, pour distinguer p̂ ≈ 0,02 de zéro) montre que le portefeuille n'est pas jugeable au budget d'un pilote ; D et E montrent que la factorisation des échecs et la stabilité des p̂ entre structures ne sont pas établies. Règle préenregistrée : M4 n'est appliquée que si, sur des mondes de **structure** différente (pas seulement de graine) et après permutation des étiquettes de familles, les intervalles de p̂_{jb}/c_j se séparent ; sinon, composition par le seul coût (N-045).

### I. M5 : règle d'allocation, bras isolé, validité composite, queues (B a4, B b, C a4, D a6, E a4, E b)

**Acceptée sur tous les points, M5 maintenue.**
- Bras M5-seul (B) : ajouté ; le duel aval ne mélange plus stratification et arrêt (la stratification du juge étant de toute façon retirée).
- Règle d'allocation (D, C) : écrite. Chaque carte reçoit n₀ tirages ; son e-processus continue par blocs tant que e ≥ θ₁ (θ₁ préenregistré, e.g. 1, illustratif) et jusqu'à N ou jusqu'à 1/α ; le budget total est un réservoir fixé ; si le réservoir s'épuise, l'ordre de continuation est l'ordre d'index scellé, jamais l'ordre des valeurs e. Comparaison au témoin à **espérance de tirages totale égale**, pas à n fixé par carte (répond à C a4).
- Validité conditionnelle sous nul composite (E) : le dénominateur est un **mélange à poids fixés d'avance** des lois du nul (archive, lois aveugles, recombinaisons sur grille) ; il n'est jamais recalibré sur les issues fraîches ; alors chaque facteur vérifie E_P[E_t | F_{t−1}] ≤ E_{t−1} pour tout P du nul. C'est à démontrer dans le préenregistrement, pas à affirmer.
- Puissance nulle si r·δ·N < ln(1/α) (B) : exacte ; c'est la borne budgétaire que j'avais écrite autrement. N est inscrit au devis.
- Queues (E) : le banc rapporte P_{H₀}(sup_n E_n ≥ 1/α) sur simulations, pas seulement la moyenne des e.

### J. Contrôles négatifs : nul complet contre copies hors classe (D c, E c, C c3)

**Acceptée.** Deux bancs distincts : (i) mondes entièrement dans la classe du nul — mesure des fausses promotions sous H₀ ; (ii) mondes qui sont des recombinaisons par morceaux des lois d'archive, hors classe — audité comme **défaillance de la garde contre les copies**, pas étiqueté H₀. Je les avais mis dans la même liste ; c'était une confusion.

### K. Métrique de garde (E a5) et métrique oracle (D b)

**Acceptées.** Une hausse de `si_sinon` sous monde nul n'est pas une dégradation de garde ; la métrique de garde est le taux de promotion e-BH sous monde nul et sous copies hors classe ; `si_sinon` devient descriptif. Pour que « additionnel à l'archive » ait le même sens entre bras, le duel décisif reste à **une génération, archive initiale identique et gelée** ; D2 est lue à l'étage « propositions brutes » relativement à cette archive.

### L. Chaîne et goulot (B a4 sur M5 « indépendant de la question »)

**Acceptée.** M5 est une amélioration de la survie, pas de l'exploration ; je la classe désormais ainsi.

## (b) Expériences corrigées

Ordre de dépense (N-045) : E0, E1, E3, E2. Toutes sous préenregistrement scellé (R1), lecteur neuf à critères gelés (R13), audit égal devant un résultat trop propre (R4).

### E0 — Banc hors ligne (zéro appel de proposeur)

- **Table de paires** : sur 50 lois synthétiques de forme connue (illustratif), zéro paire déclarée non croisée à tort, zéro croisée à tort (base : 0 erreur). Résidus R_{S,i} de E non pertinents après correction (plus de décomposition orthogonale) ; je les note comme mesure si la décomposition revenait.
- **Juge et M5** : sous mondes H₀ (nul complet), P(fausse promotion) ≤ niveau nominal et P_{H₀}(sup E ≥ 1/α) ≤ α sur 10 000 courses simulées (illustratif), avec le mélange fixe au dénominateur et la règle d'allocation écrite. Séparément, sous recombinaisons par morceaux : taux de promotion de copies hors classe, juge actuel contre juge avec arrêt. Ce nombre décide si toute poussée vers `si_sinon` est prématurée.
- **Regroupement par strates** : fusion à tort sur paires « égales sauf strate rare », non-fusion sur paires « égales », jeu public couvrant les cellules contre jeu i.i.d., à taille égale ; traits indépendants et corrélés (ρ = 0,8, illustratif).
- **Départage M3** : taux de choix de la sœur porteuse (base 1/|G|) et, sur groupes sans porteuse avec écarts fortuits (D) et avec sœur fausse-éloignée (E), taux de choix de la fausse ; seuils ε_s corrigés de la variance. Mondes de réglage ≠ mondes d'évaluation.

### E1 — Garde et levier sur monde sans interaction (le test le moins cher avec proposeurs ; repris de B, en le disant)

**Mondes.** Additif pur, traits indépendants ; jumeau additif à traits corrélés. Condition archivée identique dans les deux.
**Vues.** V0 brute ; V_L (brute + table binaire des paires non croisées) ; V_P (placebo : même format et longueur, table aléatoire).
**Deux duels binaires, unité = graine.**
- E1-garde. H_A : le taux de promotion e-BH sous V_L et V_P ne dépasse pas celui sous V0 au-delà d'une marge de non-infériorité préenregistrée (illustratif : +2 points). H_B : il le dépasse. Si H_B : arrêt, renforcement du nul avant toute poussée ; H_A tombe au titre de la garde.
- E1-levier. H_A : la loi des cartes change sous V_L par rapport à V0 (distance entre distributions des paires de traits conditionnantes citées dans les cartes, test de permutation par graine, seuil préenregistré). H_B : elle ne change pas. Si H_B : M1 n'a pas de levier, E2 est annulée et le budget va en appels (c'est la conclusion de B, que je fais mienne).
**Métriques secondaires descriptives** : `si_sinon`, refus du gardien, jetons.

### E2 — Duel décisif sur la composante conditionnelle (n'a lieu que si E1-garde donne H_A et E1-levier donne H_A)

**Mondes.** Programme à graine scellée, une génération, condition archivée dans l'archive initiale gelée ; facteurs : masse r ∈ {0,05 ; 0,25} et divergence δ par branche (deux niveaux) — illustratifs. Mondes de transfert : parité d'ordre 3 ; seuil décentré (quantile 0,8) ; additif (depuis E1).
**Bras.** V0 ; V_L ; V_P ; A3 = V0 à **budget total de jetons égal** à V_L (plus d'appels).
**Métrique.** Fraction des graines où au moins une carte valide couvre la composante (D2, étage brut, oracle lu une fois après) ; aussi par carte valide.
- **E2.1 (information).** H_A : V_L > V_P sur r = 0,05, test de permutation apparié par graine, α = 0,05 unilatéral (illustratif). H_B : V_L ≈ V_P. Si H_B, l'effet éventuel sur V0 est une consigne de forme.
- **E2.2 (valeur à coût égal).** H_A : V_L ≥ A3. H_B : A3 > V_L. Si H_B : on achète des appels, pas des tables.
- **E2.3 (non-nuisance hors structure).** Sur parité d'ordre 3 et seuil décentré : H_A : V_L n'est pas inférieure à V0 au-delà d'une marge préenregistrée. H_B : elle l'est — M1 aveugle, et serait rejetée même si E2.1 et E2.2 sont gagnées.
**Dimensionnement** : à calculer à rebours à partir d'une puissance cible sur la fraction par graine ; le chiffre « 10 graines par cellule » de ma v1 est illustratif et probablement insuffisant (point de B et C contre d'autres propositions, que je retourne contre la mienne).

### E3 — Survie, rejeu à zéro appel

Cartes scellées de E1/E2 rejouées sous : juge à n fixé ; juge avec arrêt optionnel M5-seul ; à espérance de tirages égale ; mondes avec composante et mondes nuls.
H_A : plus de promotions vraies (oracle, lu après) à fausses promotions égales. H_B : égal, ou fausses promotions en hausse.

### M4 — différée (règle écrite en (a)-H).

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi (déductions sur RAPPORTÉ, aucune mesure).**
1. Il n'y a pas de moteur de recherche à pousser : la probabilité qu'un bassin b reçoive au moins une proposition en k appels vaut 1 − (1 − p_b(v))^k, et rien en aval des proposeurs ne l'augmente. « Pousser » se réduit à changer la vue, changer les proposeurs, ou ne pas perdre ce qui a été proposé. Les critiques n'ont pas contesté cette borne.
2. Sans oracle, il n'existe pas de vue uniformément meilleure : élever p_b pour une classe de bassins l'abaisse pour les autres. Un gain exige une structure nommable sans oracle. La classe « interaction d'ordre ≤ 2 avec condition archivée » en est une ; la parité d'ordre 3 et le seuil décentré sont des exemples où la même vue ne peut rien et peut nuire.
3. Après correction, la méthode qui agit sur p_b n'est pas « sophistiquée » : c'est la liste des paires de traits que l'archive ne croise pas, propriété de la fonction et non d'une mesure. Les objets plus riches (décomposition orthogonale, plans pour le juge, portefeuille sous-modulaire) ont cédé à la critique soit pour défaut de validité sous traits dépendants, soit pour changement d'estimand, soit pour non-jugeabilité au budget.
4. L'arrêt optionnel (M5) est valide sous toute règle d'arrêt écrite d'avance avec un dénominateur fixé ; il améliore la survie d'un effet confiné, pas l'exploration ; il ne peut rien si r·δ·N < ln(1/α).

**Ce qui n'est pas établi.**
- Que la loi de proposition d'un modèle de langue bouge quand on lui montre une table de paires non croisées (E1-levier). Aucun fait ne le dit ; B, C, D et E ont tous relevé que les propositions convergentes le supposent sans preuve.
- Que ce déplacement, s'il existe, vienne de l'information et non du format (E2.1 contre placebo).
- Qu'il vaille plus que le même budget de jetons en appels (E2.2).
- Que la garde tienne quand on pousse vers `si_sinon` : la limite du juge hors classe est RAPPORTÉE, son taux de défaillance sur recombinaisons par morceaux n'est pas mesuré (E0).
- Que de vrais proposeurs trouvent la composante conditionnelle une fois sa condition archivée : c'est l'HYPOTHÈSE des faits §4, et E2 est le pilote qui la mesure.
- Que les familles de proposeurs diffèrent assez pour qu'un portefeuille ait un sens (M4, non jugeable au budget d'un pilote).

**L'expérience à faire en premier.** E0 puis E1, dans cet ordre, parce qu'elles sont les moins chères et qu'elles peuvent clore la question sans dépenser E2. E0 ne coûte que du CPU et dit si le juge cède déjà sur les copies hors classe — auquel cas toute poussée vers les bassins étroits est prématurée et le premier chantier est le nul, pas la vue. E1 coûte quelques centaines d'appels sur des familles ouvertes (devis sous GO) et oppose deux issues exclusives : soit la vue enrichie laisse la garde intacte **et** déplace la loi de proposition — alors E2 a un objet ; soit elle dégrade la garde, ou ne déplace rien — alors la réponse au directeur est : à coût égal, acheter des appels et travailler le nul, aucune méthode mathématique de la vue ne changera p_b. Ce verdict est lisible sur un monde sans aucune composante étroite, donc sans oracle à protéger, par un lecteur neuf sur critères gelés.

**Ce qui me ferait changer d'avis** reste ce que j'avais écrit, augmenté d'un point : si E1-levier montre que la table déplace la loi de proposition sur un monde additif mais que E2.3 montre qu'elle abaisse la couverture quand la vérité est hors table, je recommanderais de ne jamais servir cette table en course, même si E2.1 et E2.2 sont gagnées — parce que l'organisme ne sait pas, par construction, dans quel type de monde il est.

FIN-DE-CELLULE
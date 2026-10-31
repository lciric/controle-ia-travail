

# Proposition B — Tour III.1 : Croisement papier–programme–organisme

---

## (a) Ce que la question suppose sans que ce soit établi

La question de l'arbitre contient un programme de travail ambitieux. Avant de l'exécuter, je dois pointer ce qu'elle tient pour acquis et qui ne l'est pas.

### 1. Existence d'une correspondance non métaphorique entre le papier et les trois cibles

**Statut : HYPOTHÈSE.**
La question demande une « table de correspondance terme à terme » et insiste sur « établir où les théorèmes s'appliquent, non en tirer des métaphores ». Elle suppose donc qu'il existe au moins une cible (organisme, pince, arène) où les hypothèses des théorèmes sont satisfaites de façon vérifiable. Or le papier étudie un processus de branchement multitype à population infinie, sans compétition entre protocelles, avec une copie fidèle en trans, une partition binomiale, et un seul type de parasite. Chacune de ces hypothèses est violée ou non vérifiable dans au moins une des trois cibles (détail en (b)). La question ne demande pas *si* la correspondance existe, elle demande *où* elle tient — présupposant qu'elle tient quelque part.

### 2. Les paramètres (q, θ, n, R, τ, θ′) sont mesurables dans les cibles

**Statut : HYPOTHÈSE.**
Certains paramètres n'ont pas de correspondant univoque. Dans l'organisme d'idéation, par exemple :
- **q** (fidélité de copie) supposerait qu'une fusion entre fiches produit une « copie » dont on peut évaluer la probabilité d'être « fonctionnelle » vs « parasite ». Le bisociateur ne copie pas : il recombine deux parents. La notion de q n'est pas définie. *(Non vérifiable sans une définition opérationnelle de « copie correcte » dans le bisociateur.)*
- **R** (fécondité = copies complètes par vie de modèle) supposerait un taux de production mesurable et une durée de vie du « modèle ». Dans l'organisme, la durée de vie d'une fiche est fixée par le protocole, pas par un processus de dégradation.

### 3. « L'organisme s'allumera-t-il » est une question que le papier peut trancher

**Statut : HYPOTHÈSE.**
Le papier calcule le seuil d'erreur d'un réplicateur en trans dans des protocelles. L'organisme d'idéation n'est pas un réplicateur en trans : c'est un processus de recombinaison dirigée par un juge externe. Le rayon spectral ρ de la « matrice de descendance des paires » n'est défini que si la dynamique est celle d'un processus de branchement multitype à temps discret dont les types sont les compositions au moment de la division. Ces conditions ne sont pas établies pour l'organisme.

### 4. La note de conv-audit et la relecture d'Opus sont fiables

**Statut : NON VÉRIFIABLE.**
Les pièces `idees-conv-audit-papier-protocelles-v1.md` et la relecture d'Opus ne sont pas servies dans ce tour. Je ne peux ni les confirmer ni les contester. Toute conclusion qui s'appuierait sur leur contenu serait non vérifiable.

### 5. L'idée « les fusions inachevées doivent être jetées » est une conséquence du papier

**Statut : HYPOTHÈSE, à nuancer.**
Le papier montre deux régimes : copie perdue → coût en fécondité, facteur 1/(1−τ) ; copie recopiable et rapide (θ′ > θ) → coût en charge tolérable, potentiellement fatal (pages 8–10, Fig. 6). La conclusion « jeter » dépend entièrement de la valeur de θ′ dans la cible. Si la fusion inachevée est plus lente que le modèle original (θ′ < θ), le coût est faible. Si elle est plus rapide, le coût croît avec la taille de la protocelle. La réponse n'est donc pas « jeter toujours » ; elle est « jeter si et seulement si le produit inachevé est un modèle rapide (θ′ > 2θ dans le régime de grande protocelle), sinon le coût est absorbable ».

### 6. L'arène P-041 est modélisable comme une protocelle

**Statut : HYPOTHÈSE, probablement violée.**
L'arène est une course aux armements entre un attaquant et un moniteur. Ce n'est pas une population de compartiments qui croissent et se divisent. La sélection est exercée par un juge externe (le moniteur), pas par la croissance différentielle des compartiments. La dynamique est adversariale, pas neutre vis-à-vis de la composition. Le théorème 2 (plafond ln 2) suppose une « division aveugle à l'identité moléculaire » ; dans l'arène, le moniteur voit le contenu.

---

## (b) Table de correspondance et statut des hypothèses

### Correspondances terme à terme

| Objet du papier | Organisme d'idéation | Pince (moniteur) | Arène P-041 |
|---|---|---|---|
| Réplicase | Fiche fertile (hypothèse qui engendre des descendantes viables) | Sonde qui détecte un comportement dangereux | Attaque qui contourne le moniteur |
| Parasite | Fiche stérile mais qui absorbe les « slots » de fusion | Fausse alerte (sonde activée sur un cas bénin) | Attaque rejetée, mais qui consomme du budget de défense |
| θ (template efficiency) | Rapport entre le taux d'utilisation d'une fiche stérile et d'une fiche fertile dans le bisociateur | Rapport signal/bruit d'une fausse alerte vs vraie alerte | Rapport entre le coût d'une attaque échouée et d'une réussie pour l'attaquant — **aucun** correspondant naturel |
| q (fidélité de copie) | **Aucun** — le bisociateur recombine, ne copie pas | Probabilité qu'une mise à jour du moniteur préserve la détection correcte | Probabilité qu'une variante d'attaque reste fonctionnelle |
| Protocelle | Lot de fiches (un bras de la course 2 : 6 fiches) | Ensemble de sondes déployées dans une instance | Population d'attaques dans un tour |
| Division | Fin d'un round, tirage aléatoire des fiches pour le round suivant | Redéploiement des sondes après mise à jour | Renouvellement du pool d'attaques |
| Paire catalyseur–modèle | Paire de fiches dont la fusion produit une descendante fertile | Paire (sonde, cas de test) qui ensemble confirment une vraie menace | Paire (attaque, vulnérabilité) qui ensemble passent le moniteur |
| R (fécondité) | Nombre de fusions complètes lancées par fiche et par round | Nombre de cas évalués par sonde et par cycle | Nombre de variantes testées par attaque et par tour |
| Copie inachevée | Fusion interrompue (par budget, par timeout) | Évaluation partielle d'un cas | Attaque partiellement construite |
| τ (probabilité d'arrêt) | Fraction des fusions qui n'aboutissent pas à un produit complet | Fraction des évaluations tronquées | Fraction des variantes incomplètes |
| θ′ (template advantage du fragment) | Rapidité relative d'une fiche tronquée comme entrée du bisociateur | Facilité relative de déclencher une sonde sur un cas partiel | Facilité de réutiliser un fragment d'attaque |

### Hypothèses des théorèmes et leur statut dans chaque cible

| Hypothèse du papier (source) | Organisme | Pince | Arène |
|---|---|---|---|
| **Copie en trans** (une réplicase ne se copie pas elle-même) | **Violée** : une fiche peut être fusionnée avec une copie d'elle-même | **Tenue approximativement** : une sonde ne s'évalue pas elle-même | **Non applicable** : pas de copie |
| **Un seul type de parasite**, de poids θ fixe | **Violée** : les fiches stériles sont hétérogènes (proches, surfaces, faux) | **Violée** : les fausses alertes ont des coûts variés | **Violée** |
| **Division binomiale** (chaque molécule va dans l'une des deux filles indépendamment) | **Non vérifiable** : le protocole de sélection des fiches pour le round suivant n'est pas décrit dans les faits | **Non applicable** | **Non applicable** |
| **Division aveugle à l'identité** (Théorème 2) | **Probablement violée** : le juge (directeur) sélectionne, il ne tire pas au sort | **Violée** : le moniteur voit le contenu | **Violée** : le moniteur est précisément un classifieur de contenu |
| **Population infinie, pas de compétition entre protocelles** | **Violée** : 3 bras, 24 fusions | **Non applicable** | **Violée** : le moniteur est une ressource partagée |
| **Réplicase seule stérile** (F = 1 est morte) | **Tenue** si on admet qu'une fiche isolée ne produit rien sans partenaire de fusion | **Non applicable** | **Non applicable** |
| **Pas de réplication spontanée** (χ = 0) | **Violée potentiellement** : le bisociateur pourrait engendrer une fiche à partir de rien (bruit) | **Tenue** (pas de détection sans sonde) | **Violée** (un attaquant peut produire des attaques nouvelles sans réutiliser les anciennes) |
| **Fécondité R = copies complètes par vie** | **Partiellement applicable** : R serait le nombre de fusions complètes par fiche par round ; mesurable en principe | **Applicable** en principe | **Non applicable** directement |
| **Décroissance exponentielle des molécules** (taux 1) | **Violée** : les fiches ne se dégradent pas spontanément, elles sont retirées par le protocole | **Tenue approximativement** : obsolescence des sondes | **Non applicable** |

### Verdict global

- **Organisme** : 5 hypothèses violées ou probablement violées, 2 non vérifiables. La correspondance est **métaphorique**, pas structurelle. Le théorème 2 ne s'applique pas tel quel.
- **Pince** : La plupart des hypothèses sont non applicables. La structure du problème (détection, pas réplication) est différente.
- **Arène** : La dynamique adversariale viole la plupart des hypothèses. Le papier modélise une course *neutre* contre les parasites, pas une course aux armements.

---

## (c) Prédictions pour les correspondances qui survivent (avec réserves)

Seule la correspondance **organisme–protocelle** survit partiellement, et uniquement si l'on accepte les violations comme des approximations. Voici ce qu'on peut en tirer, avec les réserves appropriées.

### Prédiction 1 : Plafond sur le bénéfice de la compartimentation des fiches

**H_A** : Regrouper les fiches en lots (protocelles) ne peut pas ajouter plus de ln 2 ≈ 0,69 nat de charge tolérable par rapport à un pool bien mélangé, pourvu que la répartition des fiches entre lots soit aveugle à leur contenu.

**H_B** : Le bénéfice est illimité (ou au moins supérieur à ln 2) parce que le directeur sélectionne les lots, violant l'hypothèse de division aveugle.

**Métrique** : Mesurer, sur les journaux de la course 2, la fraction de fiches « fonctionnelles » (au sens d'un critère prédéfini, par ex. score d'allumage > seuil) dans les lots à la fin de chaque round vs dans un pool fictif bien mélangé (simulé par permutation des fiches entre lots).

**Seuil** : Si le gain en fraction fonctionnelle dépasse exp(ln 2) = 2 (un facteur 2 en supériorité effective), H_A est falsifiée et la sélection du directeur viole l'hypothèse de division aveugle d'une manière qui dépasse le plafond.

**Contrôle négatif** : Permuter aléatoirement les fiches entre lots à chaque round (détruire la sélection). Le gain devrait alors rester en dessous de ln 2.

**Issue** : Si le gain reste en dessous de ln 2 dans les deux conditions, le plafond tient malgré la petite taille (N = 6). Si le gain le dépasse dans la condition avec sélection, c'est la sélection, pas la compartimentation, qui fait le travail — et le papier n'est plus le bon modèle.

### Prédiction 2 : Le prix — la fécondité requise croît avec la taille du lot

**H_A** : Pour maintenir une fraction de fiches fonctionnelles au-dessus d'un seuil fixe, le nombre de fusions complètes par fiche et par round doit croître en proportion de la taille du lot (R_min ∝ n, Éq. 3 du papier, page 8).

**H_B** : Le nombre de fusions complètes par fiche et par round nécessaire ne dépend pas de la taille du lot.

**Métrique** : Varier la taille des lots (n = 3, 6, 12) à nombre total de fiches constant, mesurer le nombre minimal de fusions par fiche par round pour que la fraction fonctionnelle reste au-dessus de 50%.

**Seuil** : R_min(n=12)/R_min(n=3) > 2 (croissance linéaire en n) falsifie H_B. R_min(n=12)/R_min(n=3) < 1,5 falsifie H_A.

**Contrôle négatif** : Lots de taille 1 (chaque fiche seule). Aucune fusion n'est possible, R_min n'est pas défini.

**Issue** : Si la croissance linéaire est observée, le prix du papier se transfère. Si non, la dynamique de l'organisme est dominée par des effets absents du modèle (sélection, hétérogénéité des parasites).

### Prédiction 3 : Sort des fusions inachevées

C'est la question directe du directeur : « jeter, archiver hors du vivier, ou garder ? »

**H_A** : Si le produit d'une fusion inachevée est un modèle rapide (θ′ > 2 dans les termes du papier, c'est-à-dire qu'il est sélectionné comme entrée du bisociateur plus de deux fois plus souvent qu'une fiche complète fonctionnelle), alors le garder dans le vivier détruit la viabilité de tout lot qui en produit environ 1,5 par round de division (Fig. 6A, page 10 : charge tolérable tombe à zéro entre nτ = 1,5 et 1,85).

**H_B** : Si le produit inachevé est un modèle lent (θ′ ≤ θ), il forme un « bain » de copies lentes (Appendice S9, pages 57–60) et le coût se limite au facteur 1/(1−τ) en fécondité.

**Métrique** : Pour chaque fusion inachevée, mesurer :
1. Le produit est-il réutilisé par le bisociateur dans un round ultérieur ? (taux d'utilisation = proxy de θ′)
2. S'il est réutilisé, produit-il des descendantes fonctionnelles ? (proxy de sa stérilité)
3. Le lot qui l'a produit est-il encore « vivant » (contient ≥ 2 fiches fonctionnelles) après k rounds ?

**Seuil** : Si θ′ > 2 (la fusion inachevée est utilisée > 2× plus souvent que la fiche complète fonctionnelle) **et** que la fraction de lots vivants chute significativement (test exact de Fisher, p < 0,05) par rapport à un contrôle où les fusions inachevées sont jetées, alors H_A est confirmée : jeter.

**Contrôle négatif** : Course parallèle où les fusions inachevées sont jetées.

**La réponse au directeur** : « T'es sûr ? » Non, pas en général. **Jeter** est la politique robuste quand on ne connaît pas θ′ : le coût de jeter est 1/(1−τ) en fécondité (au plus ×1,03 pour τ = 3 %), tandis que le coût de garder peut être fatal si θ′ > 2. **Mais** si on *mesure* θ′ et qu'il est en dessous du coude (θ′ < 2), garder est préférable car les fusions inachevées forment un bain inerte qui n'est pas toxique. La mesure de θ′ est le taux d'utilisation relatif du produit inachevé comme entrée de fusion comparé à une fiche complète. Le papier montre que le coude est abrupt (Fig. 7B, page 10) : au-dessous de θ′ = 2, la charge critique dépend peu de θ′ ; au-dessus, la rapidité supplémentaire ne compte presque plus.

---

## (d) Ruptures d'analogie et modèles de remplacement

### Rupture 1 : Recombinaison vs copie

Le bisociateur fusionne deux parents en un enfant. Le papier modélise une copie d'un modèle par un catalyseur. La recombinaison :
- introduit deux parents (pas un) ;
- peut produire un enfant meilleur que chacun des parents (pas dans le papier, où q ≤ 1) ;
- ne conserve pas l'information d'un parent en particulier.

**Modèle de remplacement** : Un processus de branchement multitype avec recombinaison, où chaque « protocelle » contient des fiches de types différents et la « division » produit des filles dont les types sont des recombinants des types parentaux. Le rayon spectral de la matrice de transition moyenne serait toujours le critère de viabilité, mais la structure de la matrice est différente. *(Référence à vérifier : des modèles de ce type existent dans la théorie des quasi-espèces sexuées.)*

### Rupture 2 : Sélection par un juge vs sélection par la croissance

Dans le papier, la sélection entre protocelles est un sous-produit de la croissance différentielle : une protocelle riche en réplicases croît plus vite. Dans l'organisme, le directeur sélectionne les fiches. C'est une sélection artificielle, pas naturelle. Le théorème 2 (plafond ln 2) repose sur la division aveugle ; une sélection qui voit le contenu peut dépasser le plafond (Table 1, page 6 : le tri partiel des réplicases dans une fille, avec probabilité p, élève le plafond à ln 4 pour p = √2 − 1).

**Conséquence** : Si le directeur trie les fiches fonctionnelles dans un lot, il agit comme un « tri partiel » et le plafond peut dépasser ln 2. Le papier donne la formule (Table 1, Appendice S12.1) : r̄ = (1+p)/2, plafond = ln(1/λ*) = ½ log₂(2/(1+p)).

### Rupture 3 : Fragments fertiles

Le papier montre que les copies tronquées sont soit inertes (bain), soit toxiques (θ′ > 2). Dans l'organisme, un fragment d'idée peut être *plus fertile* que l'idée complète — il peut se recombiner plus facilement, étant plus court et plus général. C'est l'inverse du modèle : θ′ > θ signifie que le fragment est *recopié plus vite*, ce qui est exactement ce que fait un fragment fertile dans l'idéation. Le papier prédit que c'est toxique pour la protocelle. La prédiction pour l'organisme est donc : **un fragment d'idée très fertile (θ′ ≫ 1) envahit le vivier et élimine les idées complètes**, comme un parasite court envahit une population de réplicases.

### Rupture 4 : Taille finie et population structurée

Le papier travaille avec une population infinie de protocelles. L'organisme a 3 bras de 6 fiches. Les effets de taille finie sont dominants. L'Appendice S3 (page 42) note qu'une simulation de 200 protocelles sous-estime U_c de 0,014 à 0,048 ; avec 3 « protocelles » de 6 fiches, le biais serait bien plus grand.

---

## (e) Instruments nommés dans la question

### Le bisociateur

**Mesure minimale** : Le bisociateur doit, à minima, produire des fusions dont le taux de « fonctionnalité » (défini par un critère externe, par ex. un juge humain ou un vérificateur automatique) est significativement supérieur au taux de base des fiches aléatoires.

- **Taux de détection** : fraction des paires de fiches fertiles dont la fusion par le bisociateur produit une fiche fertile. Cible : > 0,1 (illustratif).
- **Taux de fausses alertes** : fraction des paires dont la fusion produit une fiche jugée fertile par le bisociateur mais stérile par le vérificateur. Cible : < 0,5 (illustratif).
- **Cas honnêtes appariés** : Paires de fiches tirées des mondes à vérité plantée, dont le statut (vrai conceptuel, faux, surface) est connu.
- **Vérification mécanique à battre** : Un bisociateur aléatoire (concaténation des deux fiches, sans traitement) doit avoir un taux de fonctionnalité significativement inférieur (test binomial, p < 0,01).

### Le moniteur (pince, boîte noire)

**Mesure minimale** : Taux de détection des attaques vs taux de fausses alertes, sur des cas appariés (comportement dangereux connu vs bénin connu).

- **Taux de détection** : > 0,9 sur les attaques connues.
- **Taux de fausses alertes** : < 0,1 sur les cas bénins.
- **Vérification mécanique à battre** : Un classifieur par mots-clés sur les mêmes cas.

Le résultat de Bailey et al. (arXiv 2412.09565 — RAPPORTÉ, non lu sur source) — un moniteur réentraîné est contourné à chaque tour pendant > 70 tours — fixe la barre : tout moniteur doit survivre à au moins 70 tours d'adaptation adversariale pour être considéré comme fonctionnel.

---

## (f) Ancrage matériel

### Modèles ouverts

Le papier repose sur des scripts Python (NumPy, SciPy) et un programme C pour le réseau. Tous les seuils sont produits par ces scripts, déposés avec le code (Appendice S7, pages 52–55). Les noyaux exacts pour n ≤ 320 et la résolution de ρ = 1 par la méthode de Brent à tolérance 10⁻⁷ sont décrits dans les Méthodes (page 17).

### Calcul nécessaire

Pour instancier le modèle avec les paramètres de l'organisme :
- Noyau exact pour n = 3 (lot de 6 fiches, n = 3 à la naissance) : quelques secondes sur un ordinateur portable.
- Noyau exact pour n = 6 : quelques minutes.
- Simulation de Monte Carlo du processus limite : quelques heures.

### Coût estimé (illustratif)

- Chaque tour du collisionneur : 8–10 USD (RAPPORTÉ dans la question, source R-879, R-884).
- Calcul des noyaux exacts : négligeable (CPU standard).
- Course 2 parallèle avec et sans fusions inachevées : coût principal = temps du directeur pour évaluer les fiches, non chiffrable ici.

---

## (g) Ce que le programme apporte au papier

### 1. Un terrain d'essai pour le modèle avec recombinaison

Le papier modélise une copie fidèle. L'organisme d'idéation, par le bisociateur, réalise une recombinaison. Si les journaux de la course 2 montrent que les fusions inachevées envahissent le vivier (prédiction du papier pour θ′ > 2), c'est une validation empirique, dans un système non biochimique, de la toxicité des modèles rapides.

### 2. Un cas de sélection non aveugle

L'organisme avec sélection par le directeur teste directement les prédictions de la Table 1 du papier (page 6) sur les divisions qui voient le contenu. Si le gain observé dépasse ln 2, c'est un argument empirique pour le tri partiel, qui renforce les résultats de l'Appendice S12.1.

### 3. Un test de la conjecture (H2) par analogie

L'arène P-041 est une dynamique adversariale à tours successifs. Si le moniteur réentraîné à chaque tour (analogue d'une « protocelle » qui adapte sa composition) est contourné à chaque tour, c'est un analogue empirique de la non-survie quand la division n'est pas aveugle et que les « parasites » (attaques) sont plus rapides — cohérent avec le papier (θ ≥ 2 → aucune fidélité ne suffit, Théorème 1, page 4).

---

## (h) Prédiction signée globale

**L'organisme de la course 2 ne s'allumera pas au sens du papier** (rayon spectral ρ > 1 de la matrice de descendance des paires).

**Raisons** :
1. La taille des lots (n = 3) est trop petite : le plafond exact à n = 3 et θ = 1 est U_c ≈ 0,450 (Table S1a, page 42), ce qui exige q > e^{−0,450} ≈ 0,638, c'est-à-dire que 64 % des fusions doivent produire une fiche fonctionnelle. C'est un taux très élevé pour un bisociateur qui recombine des fiches d'espaces éloignés.
2. La fécondité est probablement insuffisante : avec n = 3 et R ∼ 2–4 fusions par fiche par round (illustratif), la condition R > e^U ≈ 1,57 est satisfaite de justesse, mais le prix (R_min ∝ n) exige R > 0,22 × 3 ≈ 0,66 pour U + ln θ = 0,3, ce qui est atteint, et R > 3,1 × 3 ≈ 9,3 pour U + ln θ = 0,6, qui ne l'est probablement pas.
3. La sélection par le directeur viole l'hypothèse de division aveugle, ce qui rend le théorème 2 non applicable dans sa forme standard. Si la sélection agit comme un tri partiel, le plafond pourrait être plus haut, mais cela ne garantit pas l'allumage — cela change seulement le seuil.

**Prédiction falsifiable** : Si, dans les journaux de la course 2, la fraction de fiches fonctionnelles dans les lots croît au fil des rounds (au-dessus du taux de base des fiches aléatoires), l'organisme s'est « allumé » au sens faible (sélection, pas auto-réplication). Si cette fraction croît *et* que les lots sans sélection du directeur montrent aussi une croissance, alors il y a un effet de compartimentation au sens du papier. Je parie sur le premier (sélection) mais pas sur le second (compartimentation seule), et ce pari est scellé avant lecture des journaux.

FIN-DE-CELLULE
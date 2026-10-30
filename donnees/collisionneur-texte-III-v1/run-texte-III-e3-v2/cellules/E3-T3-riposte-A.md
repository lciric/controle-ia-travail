# Proposition A — Tour III.3 (réponse aux critiques)

Pièces reçues : FAITS v2 (16 faits), QUESTION DE L'ARBITRE, ma conception E3-T1-A, les trois critiques E3-T2 (B, C, D). Toutes complètes. Je ne réponds qu'aux sections qui visent A ; je ne reprends rien des critiques adressées à B, C ou D sauf là où elles proposent un remède que j'adopte, ce que je signale. Périmètre : aucune famille, aucun comportement, aucun moyen.

## (a) Verdict sur chaque critique

Notation reprise de ma conception : s(f) statistique par famille, τ seuil, ε part d'échec, T sources, S_obs familles observées, Q₁/Q₂ familles vues une/deux fois, c_f nombre de sources captant f.

### Critiques de B

**B-a1 (unité d'analyse : la fusion masque un échec sur une sous-famille).** Rejetée pour moitié, acceptée pour l'autre. Rejet : la fusion que je proposais ne sert qu'à l'estimation de N, où elle évite la corrélation parfaite créée par la scission ; elle n'oblige pas à mesurer s(f) au même grain. Acceptation : je n'avais pas dit que les deux instruments travaillent à deux grains, ce qui est bien une variable confondante. Correction : s(f) est mesurée au grain le plus fin disponible (unités de la source qui scinde), N est estimé au grain grossier, et, comme B et D le proposent, les deux conventions sont rapportées en analyse de sensibilité de l'intervalle sur N.

**B-a2 (duel 3 : prédicteur quasi binaire, pas de calcul de puissance).** Acceptée, et dépassée par C-a2 et D-a2 : le duel 3 est retiré sous sa forme initiale (voir (b)).

**B-a3 (loi nulle du duel 2 contaminée par la calibration des seuils).** Acceptée. La scission aléatoire estime une loi nulle interne à l'ensemble vu, qui est post-sélection si les seuils ont été calibrés dessus. Correction : lot de calibration des seuils scellé et disjoint du lot d'évaluation vu ; contrôle D-c2 (deux lots scellés tirés de la même loi, défense figée) remplace la scission.

**B-a4 (option 4 : une prédiction dégénérée est « calibrée »).** Acceptée. Correction : la statistique est un score strictement propre (Brier ou logarithmique) sur la prédiction probabiliste de s(f), comparé au score d'une prédiction de référence (moyenne des familles vues) ; on rapporte la largeur des intervalles prédictifs. Une prédiction constante à zéro obtient un score propre dégradé si la réalité en diffère ; elle n'est donc plus gagnante par construction.

**B-b1 (duel 1 : sous forte dépendance positive, LP et Chao convergent vers le même biais).** Acceptée. Chao2 est une borne inférieure sous hétérogénéité, pas sous dépendance positive, et l'écart LP/Chao ne distingue pas les deux causes. Correction : les deux causes sont séparées par le plan, non par ce duel ; voir duel 1 révisé.

**B-b2 (duel 2 : moins de 10 familles tenues à l'écart, puissance négligeable).** Prémisse rejetée, demande acceptée. La prémisse « moins de 10 » est une HYPOTHÈSE de B ; le fait 5 (VÉRIFIÉ) montre 25 à 28 familles par source, et cinq instances donneront un S_obs probablement du même ordre que les 34–35 actuels. La demande d'un calcul de puissance préenregistré pour δ est acceptée : si la puissance pour δ est inférieure à 0,80 (illustratif), on rapporte un intervalle, pas un verdict.

**B-b3 (ρ > 0,3, grappes ≥ 5 : 29 familles deviennent ~50 effectives ; ε = 0,10 non testable).** Acceptée : c'est précisément ce que la simulation devait mesurer, mais je n'en avais pas tiré la conséquence. Avec N̂ ≈ 37–39 (fait 8), ε = 0,05 (59 familles iid, fait 9) n'est pas atteignable même en observant la population entière, et ε = 0,10 (29) l'est à peine sans dépendance. Transformée en test de faisabilité arithmétique (ci-dessous), remède que C propose pour D et que je reprends en le disant.

**B-b4 (pas de test de fermeture).** Acceptée. Ajout : courbe d'accumulation par source datée, intervalle prédictif du nombre de nouvelles familles à la source suivante, test de tendance ; si l'intervalle prédictif exclut zéro de façon stable, on passe au cadre ouvert et N devient N(t).

**B-c1 (contrôle négatif de l'appariement lui-même).** Acceptée. Étalon à vérité connue : items dont la relation (identité, distinction, recouvrement un-vers-deux) est connue par construction de l'opérateur, insérés à l'aveugle dans les listes soumises au panel ; je n'en décris aucun contenu. Sortie : matrice de confusion des lecteurs (faux positifs, faux négatifs, erreurs de grain).

**B-c2 (règle d'arrêt validée sur données réelles hors programme).** Acceptée avec réserve. Il n'existe pas de « données réelles à vérité connue » sur le phénomène étudié ; un jeu statistique public d'un autre domaine, à dépendance connue, valide l'implémentation et le niveau nominal, pas le transport au mécanisme M. Je l'ajoute à ce titre.

### Critiques de C

**C-a1 (couverture inversée : je mesure la puissance et l'appelle couverture).** Acceptée sans réserve ; c'est le défaut le plus grave de ma conception. La garantie à protéger est P(accepter l'énoncé | π ≥ ε) ≤ α. Ma « couverture » (proportion où l'énoncé est accepté et π < ε) est satisfaite par le test qui accepte toujours. Correction dans (b).

**C-a2 (Horvitz-Thompson : c_f tronqué à c_f ≥ 1, poids bornés par T, double usage des degrés de liberté).** Acceptée, comme D-a2 qui dit la même chose. La pondération par l'inverse de c_f/T est retirée : elle ne corrige rien sur la masse à capture faible et donne une apparence de représentativité à un échantillon toujours sélectionné. Remplacement par une enveloppe explicite (b).

**C-a3 (Good-Turing : formule d'abondance appliquée à un plan d'incidence).** Acceptée. Le chiffre 0,69 est retiré. La couverture d'incidence se calcule avec la correction en (T−1)/T sur les doublets (Chao et al., 2014, référence à vérifier pour le titre exact et la formule) ; à T = 2 elle est peu informative, ce que je dis plutôt que de la chiffrer.

**C-a4 (imputation multiple de Rubin sur un panel déterministe).** Acceptée pour l'essentiel : les N par lecteur mesurent un désaccord taxinomique systématique, pas un tirage postérieur. Correction : propager la matrice de confusion mesurée sur l'étalon (B-c1) dans la vraisemblance de capture (modèle de mesure avec erreur de classification), et rapporter les N par lecteur comme analyse de sensibilité. C'est la « condition de sauvetage » du tableau de C ; je l'adopte.

**C-b1 (dégénérescence de HT sous loi de capture à queue lourde).** Acceptée, même correction que C-a2.

**C-b2 (table 2⁵ creuse à N ≈ 38 : séparation des MLE, χ² asymptotique invalide).** Acceptée. Correction : modèles log-linéaires parcimonieux (un ou deux termes d'interaction par groupe de lignée déclaré d'avance), inférence par bootstrap paramétrique ou test exact conditionnel plutôt que χ², puissance et existence des estimateurs vérifiées par simulation à N = 38.

**C-b3 (e-valeurs : la propriété de surmartingale casse si l'ordre d'arrivée est autocorrélé).** Acceptée. La règle séquentielle devient conditionnelle au contrôle C-c3 ; si le taux de rejet à la frontière π = ε sous arrivée groupée dépasse α, elle est remplacée par un plan à effectif fixe sur des unités déclarées d'avance. La randomisation de l'ordre d'évaluation parmi les familles déjà scellées supprime l'autocorrélation d'arrivée mais pas la dépendance marginale ; je le dis.

**C-c1 à C-c3.** Les trois contrôles (monde bimodal à capture 0,8/0,01, séparation sur table 2⁵ à N = 38 avec OR = 5 entre deux sources de même lignée, arrivée groupée à ρ = 0,4, tous illustratifs) sont intégrés tels quels.

### Critiques de D

**D-a1 (duel 2 : adaptation et déplacement de loi confondus ; scission interne ne valide pas le transport ; minima de tailles différentes).** Acceptée. Le duel 2 ne peut pas, sans covariable de difficulté indépendante de la défense (HYPOTHÈSE qu'elle existe), attribuer un écart à un surajustement. Il est reformulé comme duel de transportabilité d'une prédiction scellée. Minima remplacés par un quantile à tailles égalisées par sous-échantillonnage.

**D-a2 (c_f n'est pas une probabilité d'inclusion).** Acceptée (voir C-a2).

**D-a3 (loi nulle du duel 1 : les LP par paires partagent sources et appariements).** Acceptée. La comparaison « dispersion inter-paires contre écart-type théorique » est retirée ; la loi nulle de la dispersion est obtenue par bootstrap paramétrique sous le modèle d'indépendance ajusté.

**D-a4 (paliers d'information non ordinaux ; si un palier modifie la loi évaluée, l'écart confond information et déplacement).** Acceptée pour moitié. J'abandonne l'interprétation ordinale : les paliers sont des catégories. Je maintiens que l'écart est identifiable comme effet du régime si, et seulement si, les familles évaluées (mêmes scellés), k et s restent fixes entre paliers ; c'est une condition de plan que j'ajoute, avec le contrôle D-c4 (double exécution à information identique, écart attendu nul en loi).

**D-a5 (Good-Turing et gain de la cinquième source : non jugeable si la source n'est pas échangeable).** Acceptée. La prédiction scellée de Q1 est déclarée conditionnelle à l'échangeabilité (même consigne, même format, bloc 4) ; pour ne pas désigner d'avance la source « cinquième », l'ordre est tiré au sort après scellement de toutes les sorties et avant leur lecture. Un échec de la prédiction est alors imputable à l'estimateur ou à la non-échangeabilité résiduelle ; je le rapporte comme ambigu.

**D-b (cinq conditions) et D-c (quatre contrôles).** Acceptés ; D-c1 (population à vérité connue, appariement non bijectif, erreurs de fusion/scission, captures dépendantes) devient l'expérience à faire en premier.

## (b) Expériences corrigées

### Test de faisabilité arithmétique (préalable, calcul pur)

Avant tout préenregistrement : pour chaque (ε, α, ρ, g) de la grille de sensibilité, calculer n_min(ε, α, ρ, g) = ln α / ln(1 − ε) × (1 + (g − 1)ρ) (dérivé de ma formule de taille effective) et la probabilité que S_obs atteigne n_min quand N = 38 (fait 8, ordre de grandeur). Si cette probabilité est nulle ou négligeable, l'énoncé (ε, α) est déclaré non certifiable et retiré du préenregistrement. Avec les faits : ε = 0,05 est hors d'atteinte (59 > N̂) ; ε = 0,10 ne tient que si ρ ≈ 0 (dérivé). Conséquence sur la définition retenue, voir (c).

### Duel 1 révisé — estimateurs du nombre de familles

H_A : capture homogène, sources indépendantes ; Chapman à T = 2 et Chao2 à T = 5 coïncident à l'erreur d'échantillonnage près et Chapman couvre N au niveau nominal. H_B : hétérogénéité ou dépendance positive ; Chapman sous-estime N, Chao2 reste sous N, et l'écart Chao2 − Chapman croît avec le coefficient de variation des probabilités de capture (hétérogénéité) **mais pas** avec la dépendance (B-b1). Les deux causes sont donc traitées par deux instruments distincts : l'hétérogénéité par l'écart Chao2/Chapman et par les classes latentes, la dépendance par le terme d'interaction d'un modèle log-linéaire parcimonieux (groupes de lignée déclarés d'avance, un ou deux paramètres) et par l'étalonnage externe du bloc 4.

Métrique : sur mondes simulés à N ∈ {30, 38, 60, 100} (illustratif ; 38 obligatoire), T = 2 puis 5 : biais relatif, RMSE, couverture des intervalles à 95 %, et proportion de mondes où les MLE log-linéaires n'existent pas (C-b2). Sur les données réelles : dispersion des Chapman par paire, comparée à sa loi nulle par bootstrap paramétrique sous indépendance ajustée (D-a3).

Seuils (illustratifs) : couverture < 0,90 ou biais relatif > 10 % falsifie H_A dans le monde considéré ; sur les données réelles, dispersion inter-paires au-delà du quantile 0,95 de sa loi nulle bootstrap falsifie H_A ; terme d'interaction non retenu avec puissance ≥ 0,80 vérifiée par simulation à N = 38 et OR = 5 (contrôle C-c2) falsifie H_B à cette magnitude.

Contrôles négatifs : mondes homogènes et indépendants où les estimateurs doivent coïncider (code) ; mondes avec erreur d'appariement injectée aux taux mesurés sur l'étalon (B-c1), où l'on vérifie que Chao2 ne dépasse pas N (une inflation de Q₁ par faux négatifs d'appariement détruit la propriété de borne inférieure, point soulevé par C contre B et que je reprends pour moi) ; monde D-c1 où une interaction de capture et une fusion abusive produisent les mêmes comptes, pour mesurer explicitement où le duel est non jugeable.

### Duel 2 révisé — transportabilité d'une prédiction scellée

H_A : la loi de s(f) sur le lot tenu à l'écart est celle prédite, avant ouverture, à partir du lot vu (prédiction probabiliste par famille, scellée) ; le score propre de la prédiction n'est pas pire que celui de la prédiction de référence de plus de η. H_B : score dégradé au-delà de η : le lot vu ne prédit pas le lot tenu à l'écart. L'attribution à un surajustement ou à un déplacement de loi n'est pas tranchée par ce duel (D-a1) ; elle exigerait une covariable de difficulté indépendante de la défense, HYPOTHÈSE.

Métrique : score de Brier ou logarithmique de la prédiction scellée contre la référence (moyenne des familles vues) ; quantile 0,10 de s(f) à tailles égalisées par sous-échantillonnage, avec intervalle bootstrap au niveau famille. η = 0,02 en Brier (illustratif). Puissance préenregistrée pour δ et η (B-b2) ; si elle est inférieure à 0,80, intervalle sans verdict.

Contrôles négatifs : deux lots scellés tirés indépendamment de la même loi, tailles égales, défense figée, seuils calibrés sur un troisième lot disjoint (B-a3, D-c2) : l'écart doit suivre la loi nulle ; prédiction dégénérée constante, qui doit perdre contre la référence (B-a4).

### Duel 3 révisé — enveloppe sur la masse manquante (remplace la pondération HT)

L'énoncé (ε, α) porte sur la population capturable. Soit π_obs la part d'échec sur S_obs et N̂ un estimateur de N. H_A : la masse manquante réussit au taux de la masse observée ; la part d'échec capturable vaut π_obs. H_B : toute la masse manquante échoue ; elle vaut (π_obs S_obs + N̂ − S_obs)/N̂. Aucune donnée ne sépare H_A de H_B : l'enveloppe [π_obs S_obs/N̂, (π_obs S_obs + N̂ − S_obs)/N̂] est rapportée telle quelle, avec N̂ pris à la borne inférieure (Chao2) pour la borne haute. Avec S_obs = 34 et N̂ ∈ [37, 39] (fait 8), la borne haute à zéro échec observé vaut déjà 0,08 à 0,13 (dérivé) : l'énoncé ε = 0,05 est inaccessible sans hypothèse sur la masse manquante, et le rapport doit le dire. Contrôle négatif C-c1 (monde bimodal 0,8/0,01) : la procédure doit refuser l'énoncé global et ne rapporter que l'enveloppe ; si elle certifie, elle est réfutée. Les familles à capture nulle sur toutes les sources (refus commun) restent hors de N̂ et hors de l'enveloppe ; c'est écrit dans l'énoncé.

### Mesure minimale corrigée de l'énoncé d'universalité (C-a1)

Mondes simulés à deux niveaux (π connue, ρ, g, k). Trois quantités, séparées : **fausse certification** = proportion des mondes à π ≥ ε où l'énoncé est accepté, à borner par α ; **puissance** = proportion des mondes à π ≤ ε/2 où l'énoncé est accepté ; **largeur** de la borne supérieure obtenue sur ε quand l'énoncé est refusé. Base à battre : proportion brute d'échec sans intervalle, dont la fausse certification est mesurée dans les mêmes mondes. Cas appariés : π = ε (frontière) et π = ε/2 avec mêmes statistiques observées. Un test qui accepte toujours obtient désormais une fausse certification de 1 et échoue.

### Règle d'arrêt séquentielle (Q4)

Maintenue à titre d'HYPOTHÈSE, conditionnée à trois contrôles : arrivée groupée à ρ = 0,4 avec π = ε (C-c3, taux de rejet ≤ α exigé) ; ordre d'évaluation tiré au sort parmi les familles déjà scellées ; application à un jeu public à dépendance connue (B-c2, valide l'implémentation seulement). Échec du premier contrôle : plan à effectif fixe sur unités déclarées d'avance.

### Paliers d'information (Q5)

Catégories, non échelle. Condition de plan : mêmes familles scellées, même k, même s entre paliers ; sinon l'écart n'est pas interprété. Contrôle D-c4 : double exécution à information identique, écart nul en loi.

### Étalon d'appariement et propagation

Panel de trois lecteurs de lignées distinctes des cinq sources, items d'étalonnage à relation connue insérés à l'aveugle (aucun contenu décrit ici). Sortie : matrice de confusion par lecteur et par type d'erreur (fusion, scission, grain). Propagation : erreur de classification dans la vraisemblance de capture ; N par lecteur en sensibilité ; plus de règles de Rubin (C-a4).

### Test de fermeture

Courbe d'accumulation par source dans l'ordre tiré au sort, intervalle prédictif du gain à la source suivante (Good-Turing en version incidence, formule à vérifier) ; prédiction scellée avant ouverture de la dernière source (D-a5). Gain observé hors de l'intervalle à deux reprises consécutives : passage au cadre ouvert, N(t) et garantie datée.

## (c) Réponse à la question de l'arbitre

**Définition retenue.** Énoncé principal : pire cas sur la classe observée scellée (option 1), ∀ f ∈ C_obs, s(f) ≥ τ, au grain le plus fin, vérifiable par rejeu des scellés. Énoncé complémentaire, séparé et non fusionné : enveloppe sur la part d'échec de la population capturable, bornée par la masse manquante estimée (duel 3 révisé). L'énoncé (ε, α) sous la loi du mécanisme M n'est préenregistré que s'il passe le test de faisabilité arithmétique ; avec les faits, ε = 0,05 ne le passe pas. « Robuste à l'inconnu » n'est défini que relativement à M et à sa masse capturable ; la zone à capture nulle est hors de toute garantie, par écrit. L'option 4 (prédiction scellée notée par score propre) est l'engagement réfutable du programme.

**Estimateur retenu.** Chao2 à T = 5 en borne inférieure, avec vérification que l'erreur d'appariement mesurée sur l'étalon ne la fait pas dépasser N en simulation ; modèle log-linéaire parcimonieux (termes de lignée déclarés d'avance) pour l'estimation centrale, inférence par bootstrap paramétrique, existence des MLE vérifiée à N = 38 ; Chapman par paire à titre de comparaison, deux conventions de grain en sensibilité. Rapporté avec le test de fermeture.

**Questions candidates révisées (cinq).**
1. Estimer le nombre de familles capturables avec cinq sources, l'ordre tiré au sort, et prédire scellé le gain de la dernière source ; validation : l'intervalle prédictif scellé contre le gain observé.
2. Borner la part d'échec de la population capturable par une enveloppe explicite sur la masse manquante ; validation : les cinq lots extérieurs scellés ; chiffre déjà connu : la borne haute à zéro échec dépasse 0,08 (dérivé).
3. Mesurer la transportabilité d'une prédiction scellée des familles vues vers les familles tenues à l'écart, par score propre contre une référence, sans attribuer la cause de l'écart.
4. Valider par simulation la règle d'arrêt séquentielle sous arrivée groupée, ou la remplacer par un plan à effectif fixe si la fausse certification dépasse α.
5. Mesurer l'écart de s(f) entre régimes aveugle et informé à familles, k et s fixés, avec double exécution à information identique comme loi nulle.

**Organisation en cinq lignes.** Consigne unique scellée par empreinte, variation de format seulement. Engagement-révélation : chaque sortie hachée avant lecture d'une autre, journal horodaté, cinq canaux isolés. Panel de trois lecteurs de lignées étrangères aux cinq sources, étalon à vérité connue inséré à l'aveugle, matrice de confusion propagée. Indépendance : termes de lignée du modèle log-linéaire plus étalonnage sur une population de référence hors programme, les deux rapportés comme proxy (HYPOTHÈSE) de la corrélation d'entraînement. Refus : enregistré tel quel (fait 14), substitut prédéclaré d'une autre lignée, refus partiel traité comme censure par source, jamais comme capture vide.

**Ce qui est établi (VÉRIFIÉ ou calcul refaisable).** Les quatre valeurs LP/Chapman du contexte ; leur mélange d'unités ; le besoin de 29, 59, 149 familles iid pour ε = 0,10, 0,05, 0,02 ; qu'avec N̂ ≈ 37–39 et S_obs = 34–35, la population entière ne suffit pas à ε = 0,05 et suffit à peine à ε = 0,10 sans dépendance ; qu'à T = 2 l'indépendance des sources n'est pas testable (cellule manquante) ; que l'appariement actuel repose sur un lecteur unique de la lignée d'une source.

**Ce qui ne l'est pas (HYPOTHÈSE).** Que les cinq instances sont échangeables et indépendantes ; que la population est fermée ; que la dépendance mesurée sur une population de référence se transporte ; qu'une covariable de difficulté indépendante de la défense existe (sans elle, Q3 ne tranche pas la cause d'un écart) ; que la martingale de test survit à la dépendance réelle ; que les bancs publics ont un format, une licence et un recouvrement mesurables (fait 11).

**Expérience à faire en premier.** Le monde simulé à vérité connue de D-c1 : N = 38, T = 5, appariement non bijectif, erreurs de fusion et de scission injectées aux taux mesurés sur l'étalon de lecteurs, captures dépendantes par lignée. Elle mesure en une fois la fausse certification corrigée (C-a1), l'existence des MLE sur table creuse, la tenue de la borne de Chao2 sous erreur d'appariement et la largeur de l'enveloppe du duel 3 ; tout le reste du plan en dépend, et elle ne coûte que du calcul sur processeur ordinaire (illustratif).

FIN-DE-CELLULE
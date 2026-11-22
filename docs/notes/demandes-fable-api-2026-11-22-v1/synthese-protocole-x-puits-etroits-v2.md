# Méthodes mathématiques pour forcer l'exploration des puits étroits : synthèse du protocole X (Fable, Argon, Carbon, Neon) — v2

Classe C, 22 novembre 2026, 14:40Z. Session fille, sous GO-2026-11-22-67.

La v2 remplace la v1 (`synthese-protocole-x-puits-etroits-v1.md`, 497d1b47…, gardée telle quelle). Elle porte trois apports :
- la contre-lecture par un Opus 5.5 neuf : `contre-lecture-synthese-puits-etroits-opus55-v1.md`, 413ccd42…, 2 défauts forts, 6 moyens, 9 faibles ;
- la relecture par Neon : `relecture-synthese-40-neon/relecture-synthese-40-neon-v1.md`, 0,68 USD ;
- la vérification sur PDF de huit citations : `verification-pdf-citations-puits-etroits-v1.md`, PDF dans `docs/sources/pdf-puits-etroits-v1/`.

Elle inscrit aussi les décisions prises par le directeur.

Pièces sources, inchangées, dans `docs/notes/demandes-fable-api-2026-11-22-v1/` :
- la demande 40 (8fcdb2f4…) ;
- la réponse de Fable 5.2 : `reponse-40/relecture-fable-api.md` (7e6e539c…) ;
- la question servie v3 (6665fddb…) ;
- Argon `reponse-40-google/reponse-40-argon-v1.md` ; Carbon `…/reponse-40-carbon-v2.md` ; Neon `…/reponse-40-neon-v1.md`.

Dépense : Fable 1,40 USD ; Google 1,99 USD pour les réponses, plus 0,68 USD pour la relecture par Neon.

Rien de ces réponses n'est servi au collisionneur ni à l'organisme.

## 1. Verdict

**On ne force que la proposition, et seulement au prix de la force brute sur la grammaire publique, que l'on fabrique soi-même.** C'est la formule du contre-lecteur, reprise telle quelle.

- **Sans minorant connu de la fréquence p des bonnes idées, rien ne garantit de les trouver dans un budget fixé.** C'est ce que disent Argon, Carbon et Neon. Ils ne laissent que deux garanties sans minorant :
  - la garantie disjonctive : « trouvé, ou bien certifié que p est sous un seuil » ;
  - l'énumération, si la tranche explorée tient dans le budget.
- **On peut fabriquer soi-même un minorant.** On réserve une part ε du budget à un tirage mécanique, ou à une énumération, sur la grammaire publique. Chaque classe c reçoit alors une probabilité au moins ε·u(c), quel que soit le modèle de langue.
  - Fable nomme cette construction « mélange défensif » (en citant Hesterberg) et en fait sa réponse.
  - Neon propose la même idée sous le nom de « portefeuille hybride » : une part λ du budget au générateur, le reste à la grammaire.
  - Carbon conseille de « basculer sur l'énumération » de la grammaire.
- **Ce minorant coûte cher.** Avec une loi uniforme sur les M classes, il vaut ε/M, et M croît de façon exponentielle avec la longueur des idées. C'est donc la force brute, diluée par ε.
  - Il force la proposition, pas la reconnaissance : les fausses alertes du juge et la puissance du test restent entières.
  - La borne de l'aiguille, k/M, reste vraie.
- **Selon Fable (c'est une hypothèse, pas un fait établi),** les méthodes savantes ne gagnent que sous une structure, et un puits étroit sans parent manque justement de structure. Ces méthodes sont le recuit, le fractionnement, les bandits et les arbres de recherche.

## 2. La question, et ce qu'elle a induit

- **Le mot du directeur :** « il n'y a pas de méthodes mathématiques qui permettraient de forcer à explorer des puits profonds étroits ? »
- **La question neutre.** Fable l'a écrite, puis trois tests de devinette par des agents neufs l'ont affinée.
  - La version servie, la v3, reste « orientée de justesse » : 0,55 avec le contexte du dépôt, 0,45 sans (`devinette-question-neutre-40-v1.md`). L'en-tête de la v3 donne 0,40 pour le retest de la v2 ; la devinette donne 0,45 pour la v3.
  - La mère a choisi la v3 telle quelle (message à la session fille, 22 novembre, vers 13:50Z).
- **Biais induit, à garder en tête.** La v3 ne parle ni de modèle de langue ni d'idéation. Elle dit aussi « dont on ne peut qu'obtenir des tirages », ce qui pousse vers « on ne peut rien changer au générateur ». Une part de l'accord entre Argon, Carbon et Neon vient donc de la question elle-même (contre-lecture, défaut moyen 8).

## 3. Les méthodes, une par une

Les lettres disent qui avance chaque méthode : F Fable, A Argon, C Carbon, N Neon.

Statut des références : « vérifié PDF » renvoie à la section 6. Les autres sont rapportées par les modèles, non vérifiées (R7).

| Méthode | Ce qu'elle garantit | Ce qu'elle ne garantit pas | Qui |
|---|---|---|---|
| Tirer et vérifier au hasard, tirages indépendants | Succès avec probabilité 1 − (1 − p)^n ; au moins 1 − δ dès que n ≥ ln(1/δ)/p_min | Rien si p n'a pas de minorant | A, C, N ; F le suppose |
| Garantie disjonctive (borne de Clopper et Pearson à zéro succès) | Pour tout p, même nul : « trouvé, ou p < 1 − δ^(1/n) », avec probabilité au moins 1 − δ | Elle certifie une fréquence faible sous le générateur, pas l'absence de puits | A, C, N (pas F) |
| Dédoublonnage avant vérification | Domine le tirage direct à budget égal, sans hypothèse sur la loi, si le vérificateur est déterministe | Rien sur la génération elle-même | A, C, N ; F aussi |
| Tirage sans remise | Domine les tirages indépendants (Joag-Dev et Proschan, 1983, chez C ; loi hypergéométrique chez N) | La loi du générateur reste la même | C, N ; F (Kool et collaborateurs) |
| Énumération de la grammaire | Certitude si la tranche explorée est finie et tient dans le budget, même si le générateur ne la produit jamais | Impraticable au-delà : M explose avec la longueur | F, A, C, N |
| Part mécanique du budget : mélange défensif (F), portefeuille hybride (N), bascule sur l'énumération (C) | q(c) ≥ ε·u(c) pour toute classe, si l'organisme tire lui-même dans u et si u(c) > 0. Sur la part ε, l'énumération sans remise domine le tirage avec remise (N) | Rien hors de la grammaire ; un coût en ε/M ; et la perte d'au plus ε du budget suppose des coûts unitaires égaux sous u et sous p (Neon) | F (nommé), N, C |
| Recherche universelle de Levin | Optimale à une constante multiplicative près (vérifié PDF, Levin 1973) ; la forme « en 2^L essais » vient de travaux postérieurs, selon Trakhtenbrot | Coût exponentiel en L | F |
| Rejet exact par programme | Loi conditionnelle exacte ; gain borné par 1/(1 − p(S)) | Pas plus que ce gain. Une exclusion par l'invite n'est pas un conditionnement | F ; élagage par une sous-grammaire nécessaire chez C, N |
| Filtre syntaxique exact compilé | Pas de faux négatifs, si la propriété se décompose sur l'arbre de dérivation (Courcelle, 1990 ; Knuth, 1968) | Impossible en général si la grammaire écrit des programmes quelconques (Rice, 1953) | A ; N pour la sous-grammaire |
| Valeurs e pondérées par la longueur, contrôle en ligne des fausses découvertes | Erreur au plus α si les poids 2^(−L) forment un code préfixe, si les valeurs e sont valides sous le nul, sans adaptation. En ligne, il faut un niveau α_t qui décroît | La puissance. La validité sous le nul composite de l'organisme n'est pas prouvée | F |
| Stratification, histogramme plat, qualité-diversité | Quota par cellule ; le puits devient large à l'intérieur de sa cellule | Rien si le puits est étroit dans toutes les cellules. Aucune borne de temps d'atteinte connue pour la recherche de nouveauté (question de F) | F ; A sur les quotas par strate |
| Processus répulsifs, ensembles à faible dispersion | Dépendance négative ; toute boule de la métrique est touchée | Rien si le puits n'est pas une boule ; coût exponentiel en la dimension | F, N |
| Fractionnement multiniveau | Estimateur sans biais | Efficace seulement avec une fonction de progression. Si cette fonction est le juge statistique, la validité du juge s'use | F |
| Entropie croisée | Convergence dans une famille de lois | Se referme sur le premier bassin trouvé, donc le plus large | F |
| Recuit, tempering, chaînes de Markov | Convergence à refroidissement logarithmique, en temps exponentiel | Mélange lent quand des pics étroits côtoient des pics larges de masse comparable (vérifié PDF, Woodard et collaborateurs, 2009). A et N : inapplicables à un générateur passif. C : sans gradient, puisque le vérificateur ne rend qu'un bit | F, A, C, N |
| Bandits et recherche arborescente | Regret borné sous régularité ou queue paramétrique ; choix du meilleur de plusieurs générateurs (N) | Aucun regret garanti sans hypothèse de queue ; plus lent que l'uniforme sur un arbre trompeur | F, N, A |
| Filtre bon marché calibré (prédiction conforme, contrôle du risque) | Rappel au moins 1 − α sur les vrais positifs, sans hypothèse sur la loi, si les tirages sont échangeables et si la calibration contient des positifs | Calibration d'au moins l'ordre de 1/p vérifications ; rappel nul si mal calibré | C, N ; A n'a qu'un filtre appris, qu'il dit sans garantie |
| Règle d'arrêt et tests séquentiels (Wald, 1945 ; Dagum et collaborateurs, 2000) | Estimer p à erreur relative près en un nombre d'appels optimal à une constante près. Répéter le vérificateur s'il est bruité (N) | Elles ne lèvent pas l'impossibilité à budget fixe | A, C, N ; constante 4(e − 2) chez A et C |
| Redémarrages universels (Luby, Sinclair et Zuckerman, 1993) | Coût optimal à un facteur logarithmique près | Exige un générateur réinitialisable | C, N |
| Tests groupés (Dorfman, 1943) | Si le vérificateur accepte un lot, environ 2√p tests par candidat. C'est une dérivation, pas un énoncé de Dorfman (vérifié PDF : 20 % des tests, groupes de 11, taux de 1 %) | Exige un vérificateur « au moins un dans le lot » | C |
| Vote majoritaire, tri par modèle de score | Rien en régime rare : le vote converge vers l'erreur fréquente | — | C, N |
| Température, pénalité de vraisemblance, surprise | Rien sur les classes. Elles agissent sur les jetons ; la surprise est maximale sur le bruit | — | F |
| Méthodes de Stein, transport optimal | Rien ici : il faut le gradient d'une cible connue | Peuvent mesurer l'écart entre deux lots | F |

Calculs vérifiés à la main, puis par les deux contre-lecteurs. Ce sont des identités, non des chiffres publiés.
- **Rentabilité d'un filtre** (N). Le filtre abaisse le coût espéré par succès si et seulement si r_rec > (1 + q·ρ)/(1 + ρ). Ici q est la part des tirages qui passe le filtre, r_rec son rappel et ρ = c_v/c_g le rapport des coûts (noté r chez Neon, renommé ici). Hypothèses : tirages indépendants, sans dédoublonnage, vérificateur exact, coûts de filtrage et de calibration nuls.
- **Plafond du gain** (N). Le gain est au plus (1 + ρ)/(1 + p·ρ), donc au plus 1 + ρ, contre la vérification directe, sous les mêmes hypothèses.
- **Couverture** (F). N ≥ (1/τ)·ln(1/(τ·δ)) tirages indépendants suffisent pour voir toutes les classes de largeur au moins τ avec probabilité 1 − δ. Hypothèse : classes disjointes.
- **Borne disjonctive** (C, N). 1 − δ^(1/n), sous n tirages indépendants et un vérificateur exact.

Neon relève deux erreurs dans sa propre réponse, que la v1 n'avait pas vues. Pour au moins k ≥ 2 objets distincts, sa borne de Chernoff et son coût exact k/p(c_g + c_v) sont faux, car la loi binomiale compte les répétitions.

## 4. Le seuil de reconnaissance de Fable : ce qu'il dit, et ce qu'il ne dit pas

Fable écrit qu'un puits est retenu quand n·r·Δ dépasse environ L·ln 2 + ln(1/α). Les grandeurs viennent de sa réponse 28 (`reponse-28-effort-max/relecture-fable-api.md`) :
- n : le nombre de tirages frais du juge ;
- r : la masse de la région des données où l'effet vit (sans rapport avec le rapport des coûts) ;
- Δ : le gain de log-vraisemblance par tirage dans cette région ;
- L : la longueur de description de l'idée.

Ce que les contre-lecteurs ont établi :
- le contrôle d'erreur est juste si les poids 2^(−L) forment un code préfixe et si les valeurs e sont valides sous le nul, sans adaptation ;
- la condition de rétention n'est vraie qu'en espérance : la puissance est voisine d'une chance sur deux à la frontière, et il faut une marge ;
- c'est un ordre de grandeur, pas un critère suffisant. La validité sous le nul composite de l'organisme reste non prouvée.

## 5. Les impossibilités énoncées

- **Aiguille** (F, A, N ; Wolpert et Macready, 1997, non vérifié). Avec M candidats indiscernables et un vérificateur qui répond oui ou non, la réussite est d'au plus k/M en k vérifications. Neon en donne la forme minimax (Le Cam).
  - Carbon l'attribuait à Nisan et Szegedy (1994) : **attribution infirmée sur PDF**. L'article traite du degré des fonctions booléennes, en déterministe.
- **Pas de garantie uniforme sans minorant** (A, C, N). C'est le calcul binomial : (1 − p)^N tend vers 1.
  - Argon l'attribue à Halmos (1946). L'article n'a pas pu être lu (Project Euclid refuse le téléchargement automatique). Selon des sources secondaires non opposables, il dit seulement qu'il n'y a pas d'estimateur sans biais de 1/p à taille fixe : attribution à ne pas reprendre.
  - Carbon cite Bahadur et Savage (1956). Neon objecte que l'article vise des lois non bornées, pas des variables à deux valeurs : à vérifier avant tout usage.
- **Parité** (F ; Kearns, 1998). Une interaction d'ordre élevé sans effet marginal demande un nombre exponentiel de requêtes statistiques.
- **Maximum** (F ; Nishihara, Lopez-Paz et Bottou, 2016). Sans hypothèse de queue, aucun regret n'est garanti sur le maximum.
- **Adaptativité** (F ; Dwork et collaborateurs, 2015, non vérifié). Guider la recherche par le juge statistique use sa validité.
- **Indécidabilité** (A, N ; Rice, 1953). Si la grammaire écrit des programmes quelconques, aucun filtre exact ne remplace le vérificateur.
  - Carbon donne une autre borne : la NP-complétude du problème « existe-t-il une solution de longueur bornée ? » (Cook, 1971).
- **Apprentissage actif** (N ; Dasgupta, 2005 ; Hanneke, 2014). Sans hypothèse de structure, pas mieux que de l'ordre de 1/p.
- **Faux positifs du vérificateur** (N). Si le taux de fausses alertes dépasse nettement p, presque toutes les reconnaissances sont fausses.
  - La synthèse du tour précédent du collisionneur nomme la même limite pour cinq modèles sur six (`docs/notes/collisionneur-v9/syntheses-protocole-x-v1/note-synthese-idees-originales-v1.md`, sections 1 et 6).
- **Corrélation entre tirages** (A, C, N). Une corrélation positive dégrade toutes les bornes. Un mélange qui charge p = 0 avec une probabilité supérieure à δ rend tout budget vain (C, par le théorème de de Finetti).
- **Profondeur** (A ; Booth et Thompson, 1973). Sous une grammaire probabiliste, la fréquence des objets décroît de façon exponentielle avec la profondeur de dérivation. C'est la forme mathématique du « profond ».

## 6. Ce qui est vérifié sur PDF

Rapport : `verification-pdf-citations-puits-etroits-v1.md`. Les PDF sont dans `docs/sources/pdf-puits-etroits-v1/`, chacun avec son empreinte.

| Citation | Verdict | Ce qui change dans la synthèse |
|---|---|---|
| Hesterberg 1995, mélanges défensifs (p. 189) | Confirmée en partie. La composante défensive est la loi cible. C'est u/q ≤ 1/ε qui est borné, et p/q ≤ 1/(1 − ε) seulement. La borne porte sur la variance asymptotique. « Perdre au plus ε du budget » n'y est pas | Hesterberg nomme la construction. La garantie q(c) ≥ ε·u(c) est une identité d'une ligne, qui ne lui doit rien |
| Levin 1973, recherche universelle (p. 400 ; Trakhtenbrot 1984, p. 397) | Confirmée en partie. « Optimal à une constante multiplicative près ». Le facteur 2^L vient de travaux postérieurs (1980) | Citer « optimal à une constante près », et chercher la source du facteur 2^L |
| Woodard, Schmidler et Huber 2009 (p. 780, 799) | Confirmée. Pics étroits et pics larges de masse comparable : mélange lent. Revue : Electronic Journal of Probability | Corrigé. La v1 disait le contre-résultat « décisif » ; c'est le cas d'école du puits étroit voisin d'un bassin large |
| Dorfman 1943 (p. 437-438) | Confirmée en partie. Aucune formule en √p ; 20 % des tests, groupes de 11, taux de 1 % | Retirée des attributions douteuses : l'ordre 2√p est une dérivation correcte |
| Nisan et Szegedy 1994 (p. 301-310) | Infirmée pour l'usage qu'en fait Carbon | Ne pas reprendre |
| Gillman 1998 | Prénom David (fiche de thèse du MIT, pas le PDF). L'énoncé n'est pas vérifiable (SIAM, payant) | Carbon se trompe de prénom |
| Halmos 1946 | Non vérifiable (téléchargement refusé, non contourné) | Ne pas reprendre l'attribution d'Argon |
| Blumer et collaborateurs 1987 | Non vérifiable (payant). Le fichier téléchargé était une page d'erreur : versé sous son vrai nom, `blumer-1987-telechargement-echoue-page-erreur-404-v1.html` | Neon objecte que l'article porte sur l'apprentissage supervisé, pas sur des valeurs e pondérées : il ne fonde pas le seuil de la section 4 |

Réserve de provenance : trois PDF viennent de pages de cours d'universités, licence non vérifiée (Dorfman, Nisan et Szegedy, Trakhtenbrot). Le dépôt est privé ; la décision de les garder revient à la mère.

Reste à vérifier sur PDF avant tout usage dans une pièce décisive :
- Dwork et collaborateurs, 2015, *The reusable holdout*, qui fonde la décision sur le juge (section 9) ;
- Wang et Ramdas, 2022 ;
- Nishihara et collaborateurs, 2016 ; Carpentier et Valko, 2014 ;
- Weitzman, 1979 ; Coquelin et Munos, 2007 ;
- Bahadur et Savage, 1956 ;
- Dagum et collaborateurs, 2000 ;
- Luby, Sinclair et Zuckerman, 1993 ;
- Bates et collaborateurs, 2021 ;
- McAllester et Schapire, 2000 ; McAllester et Ortiz, 2003.

Neon relève aussi que Carbon cite Wald et Wolfowitz (1940), un test à deux échantillons, là où il faudrait le test d'aléa d'une suite (1943). À vérifier.

## 7. Accords et désaccords

**Accords :**
- Garantir veut dire énoncer des quantificateurs et des hypothèses. Argon, Carbon et Neon donnent cinq ou six énoncés, presque les mêmes ; Fable en donne huit.
- Sans structure, rien ne bat l'énumération ou le tirage dédoublonné (F, A, C, N).
- Composer soi-même une part des tirages sur la grammaire est la seule voie vers un minorant (F, N, C). La v1 voyait là un désaccord avec Fable ; il n'y en a pas.
- Commencer par compter la grammaire : c'est l'étape 0 de Fable, et Carbon et Neon le proposent aussi (leurs sections 5).

**Désaccords et écarts :**
- **Le juge peut-il guider la recherche ?** Ce n'est pas le même objet selon les modèles.
  - Pour A, C et N, le vérificateur est exact et ne s'use pas. Argon propose même un bandit guidé par le vérificateur pendant la course, sur le reste du budget après un pilote ; Carbon propose aussi un pilote.
  - Pour Fable, le juge est un test statistique sur des tirages partagés, que l'adaptation use.
  - Les deux sont compatibles une fois l'objet nommé. La décision prise (section 9) vise le juge statistique de l'organisme.
- **Par quoi commencer ?** Fable commence par le calcul sans modèle et le bras sans modèle. Les modèles de Google commencent par des diagnostics sur le générateur réel et par l'audit formel de la grammaire.
  - Les diagnostics sans appel au juge : taux de collisions et autocorrélation (A, C, N).
  - Les diagnostics qui coûtent des appels au juge : l'audit du déterminisme et des erreurs du juge (N), la masse non vue (N, et F).
  - L'audit formel : sous-grammaire nécessaire, décomposabilité, difficulté (A, C).
- **La recherche de nouveauté a-t-elle une borne de temps d'atteinte ?** Fable n'en connaît pas, et le dit comme une question. Ouvert.

## 8. Ce qu'il faut retenir

1. **Forcer, c'est fabriquer soi-même un minorant par force brute sur la grammaire.**
   - Réserve : rien hors de la grammaire ; un coût en ε/M, exponentiel en la longueur ; et la proposition seulement.
2. **Proposer n'est pas reconnaître.** Le seuil de Fable (section 4) n'est qu'un ordre de grandeur en espérance, sous des hypothèses non prouvées pour l'organisme.
3. **Les méthodes savantes sont des paris sur une structure.**
   - Le tempering échoue sur des pics étroits voisins de pics larges (vérifié PDF).
   - L'entropie croisée se referme sur le bassin large (F, non vérifié).
4. **Le juge est probablement le goulot.** Quand vérifier coûte bien plus que générer, les seuls gains garantis sont le dédoublonnage, le tirage sans remise et le filtrage calibré. Le gain du filtre est plafonné à 1 + ρ.
5. **Jugement du rédacteur.**
   - Les deux contre-lecteurs, Opus et Neon, ont corrigé surtout des attributions et des nuances ; aucun n'a contesté le noyau.
   - Mais les quatre modèles partagent la même culture statistique, et la question a orienté une part de l'accord : ce n'est pas une validation extérieure.
   - Seuls les PDF ont apporté un contrôle extérieur, sur cinq citations.

## 9. Décisions

**Prises par le directeur le 22 novembre 2026** (mot relayé par la mère vers 14:29Z : « Cinq décisions … go », sur les recommandations de la v1) :
- **D1.** « Forcer » veut dire, dans toute revendication, une garantie de pire cas dans la grammaire publique, à prix affiché. Le gain moyen sous un a priori n'est qu'une mesure.
- **D2.** Un bras sans modèle de langue (énumérateur ordonné par longueur, valeurs e pondérées par la longueur) est le premier essai et la base obligatoire de toute méthode.
  - Réserve de Neon, gardée : ce bras n'est une « garantie complète » qu'une fois prouvée la validité sous le nul composite de l'organisme.
- **D3.** Les diagnostics bon marché entrent au premier étage du plan, avec le calcul sans modèle de Fable :
  - sans appel au juge : collisions, autocorrélation, audit formel de la grammaire ;
  - sur un budget pilote compté : audit du juge, masse non vue.
- **D4. Le juge statistique ne guide jamais la recherche en course. Au banc, il ne la guide que sur des tirages d'exploration à part, comptés au budget.**
  - Décision prise le 22 novembre 2026 : « go » du directeur, relayé par la mère vers 14:33Z, sur la décision D3 de la réponse 40 de Fable (section D).
  - Elle vise le juge statistique de l'organisme, non un vérificateur exact.
  - Son appui, Dwork et collaborateurs (2015), reste à vérifier sur PDF.
- **D5.** Vérification sur PDF avant tout usage dans une pièce décisive.
  - Faite pour huit citations le 22 novembre (section 6).
  - Reste la liste de la section 6, Dwork et collaborateurs en tête.

Aucune décision neuve n'est proposée dans cette v2.

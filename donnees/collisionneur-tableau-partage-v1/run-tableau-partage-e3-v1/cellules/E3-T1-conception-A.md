# Proposition A — Tour III.1

Périmètre tenu : rien sur le contenu des fiches ; aucune formulation d'instruction glissée ; la chaîne inerte est décrite, jamais écrite. Tous les chiffres hors faits sont illustratifs.

## Bloc 1 — Le tableau complet face aux trois écueils

### Écueil 1 : influence croisée

**Mécanisme (flux).** Entre la passe 1 et la passe 2, le proposeur P_i écrit une entrée libre dans le tableau de sa case (texte × bras). Le noyau sert le tableau à P_j dans la consigne de passe 2. Trois chemins : (i) tableau → consigne de P_j → fiche de P_j → juge, par recopie ou paraphrase ; (ii) tableau → fiches de plusieurs proposeurs qui s'alignent sur les mêmes entrées (convergence) ; (iii) le proposeur qui écrit le plus d'entrées occupe la plus grande part de ce que lisent les autres (poids du plus prolifique). Le témoin, écrit par un tiers et absent du tableau, devient reconnaissable par un quatrième chemin, indirect : si les fiches de passe 2 partagent un vocabulaire venu du tableau, la fiche qui ne le partage pas se distingue.

**Protocole.** Entrées à gabarit fixe validé par le noyau (fait 2), bornées : 400 caractères par entrée, 6 entrées par proposeur et par passe, 60 au total par case (illustratif) ; auteur remplacé par une étiquette propre à chaque lecteur (permutation par lecteur, reprise de l'anonymisation par juge, fait 2) ; caviardage de chaque entrée avant service (fait 2) ; service comme donnée entre balises, jamais comme consigne (spécification v53, fait 5) ; quota de lecture égal par auteur (le noyau sert au plus k entrées par auteur, tirées au sort) ; aucun chemin de code du tableau vers l'archive servie au juge ; témoins exclus du tableau (fait 7).

**Mesures (pré-pilote : au moins 2 cases × 2 conditions, avec et sans tableau, ≥ 3 proposeurs, ≥ 6 fiches par proposeur et par condition, mêmes juges figés ; illustratif).**
- *Convergence* : idées distinctes par fiche (fait 4) et distance moyenne entre fiches d'une case (1 − recouvrement de trigrammes de caractères), avec tableau contre la même case sans tableau (contrôle négatif). Non évité si la diversité baisse de plus de 15 % (illustratif). Plantés : doublons de calibration (paires à recouvrement connu) pour vérifier le détecteur.
- *Poids du plus prolifique* : part des entrées du tableau et part des idées distinctes attribuées à un même proposeur. Non évité si une part dépasse 1/n + 0,15 avec tableau alors qu'elle ne le dépasse pas sans (illustratif).
- *Atteinte au juge* : recherche exacte de la chaîne inerte (plantée par un tiers dans une entrée du tableau) dans tout ce qui est servi aux juges, seuil zéro ; recouvrement de 8-grammes de caractères entre tableau et fiches servies, seuil 2 % (illustratif) ; taux de reconnaissance des mêmes témoins par les mêmes juges figés, avec et sans tableau, écart admis ≤ 10 points (illustratif), le sans-tableau servant de contrôle négatif.

**Conclusion : évité sous condition** (les trois seuils tenus au pré-pilote).

### Écueil 2 : instructions glissées

**Mécanisme.** P_i écrit une entrée ; le noyau la sert à P_j à la passe 2 ; l'entrée agit sur P_j. Chemin unique : tableau → contexte de P_j. Chemin dérivé : tableau → fiche de P_j → juge, déjà ouvert aujourd'hui par toute fiche (le juge lit du texte d'agent), donc non propre au tableau.

**Protocole.** Service comme donnée (fait 5) ; gabarit et bornes de taille de l'écueil 1 ; garde lexicale existante étendue aux entrées, comme elle l'est déjà aux fiches de passe 1 (fait 2, ligne 26) ; garde de forme (entrée refusée si elle sort du gabarit) ; traceur : chaîne inerte, unique par entrée plantée, dont la présence hors de son entrée se détecte mécaniquement.

**Mesure.** Prise = fréquence de la chaîne inerte hors de sa place (fiches de passe 2 des autres proposeurs, autres entrées), avec et sans garde. Plantés : 6 entrées écrites par un tiers hors du tour, appariées à 6 entrées honnêtes portant chacune une chaîne inerte propre (contrôle négatif : recopie spontanée d'une chaîne sans instruction). Seuil : prise des plantées non supérieure à celle des honnêtes, et nulle dans ce qui atteint le juge (illustratif). Effectif minimal : 12 entrées, 3 proposeurs lecteurs, 2 cases.

**Conclusion : évité sous condition** (prise nulle ou égale au contrôle).

### Écueil 3 : surcroît de code

**Mécanisme (liste).** Flux « écriture d'entrée » : (1) chemin d'écriture agent → noyau ; (2) gabarit d'entrée ; (3) bornes et quotas. Flux « stockage » : (4) tableau par case. Flux « lecture » : (5) service comme donnée ; (6) anonymisation par lecteur ; (7) quota de lecture par auteur ; (8) itération si lecture-écriture répétées. Flux « contrôle » : (9) caviardage des entrées ; (10) garde lexicale sur entrées ; (11) traceur chaîne inerte et sa recherche ; (12) exclusion des témoins.

**Repris tel quel.** (2) validation de gabarit, (6) permutation par lecteur, (9) caviardage, (10) garde lexicale : fait 2 ; (12) : fait 7 ; (3) : analogue de la coupe à 1 500 caractères, fait 7, à adapter.

**Mesure.** Par rapport au noyau (fait 2) : 8 éléments nouveaux (1, 3, 4, 5, 7, 8, 11, plus l'adaptation de 6). Par rapport au tableau minimal, qui a déjà (4), (5), (6), (9), (12) : 6 éléments nouveaux (1, 2, 3, 7, 8, 11 ; (10) est une extension, comptée dans 2). Liste close.

**Conclusion : évité sous condition**, condition = 6 éléments à contre-lire et sceller.

## Bloc 2 — Trois conceptions sur un même estimand

**Estimand opérationnel.** *Même idée* : deux lecteurs à part (sessions neuves, sans outil, ni proposeurs ni juges), lisant titre, résumé et corps de chaque paire candidate préfiltrée par recouvrement de trigrammes (seuil bas, pour ne rater presque rien), répondent oui/non ; doublon si les deux disent oui ; accord exigé κ ≥ 0,6 (illustratif), sinon la mesure est déclarée non jugeable ; des paires d'étalonnage plantées (réécritures d'une même fiche ; paires honnêtes) vérifient les lecteurs. *Paires → idées* : composantes connexes du graphe (fait 4), ce qui absorbe les cycles. *Diversité* : nombre de composantes, distance moyenne entre composantes (1 − recouvrement de trigrammes), entropie de la répartition des composantes entre proposeurs. *Dépense* : jetons lus et écrits, séparément, et dollars au tarif du jour ; les deux rapportés. *Qualité jugée égale* : moyenne des notes des juges par fiche, marge d'équivalence ±5 % de l'échelle (illustratif), vérifiée d'abord sur les témoins (leurs notes doivent rester dans la même marge d'une conception à l'autre, sinon le juge n'est pas étalonné et la comparaison tombe). Ces notes sont un verdict de juge. Le choix servi est celui de la conception (A, B ou C). Qu'il échappe au fait 13 est HYPOTHÈSE ; si elle ne tient pas, la qualité jugée est rapportée comme information et la comparaison repose sur idées distinctes, diversité et dépense seuls.

**(A) Tableau minimal.** Lecture : titres et résumés de la case, anonymisés, comme donnée. Écriture : aucune. Permet l'évitement des redites ; ni échange, ni idées ensemble, ni rôles. Coût : ~30 entrées × 40 jetons ≈ 1 200 jetons lus par proposeur (illustratif) ; 0 écrit ; code : liste, service, anonymisation. Pièges : le proposeur reformule un titre pour échapper à sa propre liste ; deux résumés d'une ligne cachent une redite que seul le corps montre ; le détecteur n'est pas éprouvé si le taux de doublons chute à zéro par construction.

**(B) Tableau complet.** Lecture et écriture libres sous gabarit et bornes du bloc 1. Permet échange, idées ensemble, rôles pris sur le tableau. Coût : 60 entrées × 100 jetons ≈ 6 000 jetons lus par lecture et par proposeur, multipliés par le nombre de tours ; 600 à 2 000 jetons écrits par proposeur (illustratif) ; 6 éléments de code. Pièges : les trois écueils ; chaque tour supplémentaire multiplie lectures et chemins.

**(C) Tableau intermédiaire.** Lecture : fiches entières de passe 1 de la case, anonymisées, caviardées, servies comme donnée. Écriture : pistes typées, type pris dans une liste fermée (complément, contraste, question, rôle pris), forme imposée (type, étiquette de la fiche visée, ≤ 200 caractères), ≤ 4 par proposeur. Permet un échange borné et des rôles déclarés ; pas de discussion libre. Coût : 30 fiches × 1 500 jetons ≈ 45 000 jetons lus par proposeur (illustratif), plus cher en lecture que B ; ~800 jetons écrits ; code : 3 éléments de plus que A (gabarit de piste, chemin d'écriture, traceur). Pièges : la lecture des corps entiers favorise la convergence et la recopie dans la passe 2 ; le type « rôle pris » est un rôle choisi sur le tableau (bloc 3).

## Bloc 3 — Les rôles

Pas de rôles dans la course avant mesure ; au pré-pilote, rôles assignés par l'orchestrateur et tirés au sort, non choisis sur le tableau (le choix ajouterait un chemin d'écriture et confondrait rôle et prolixité). Chemin de fuite : consigne de rôle → forme de la fiche (structure, longueur, part de critique) → juge → notes. Prévention : gabarit fixe de fiche et normalisation typographique (fait 2) ; la consigne de rôle hors des champs rendus ; vérification : un lecteur figé à part, servi des fiches anonymisées, tente de retrouver le rôle ; exactitude admise ≤ hasard + 10 points (illustratif), sinon le rôle fuit et la condition est écartée. Comparaison : sans rôle ; rôles au sort ; contrôle négatif : étiquette de rôle servie sans consigne de conduite. Mesure : idées distinctes et diversité (fait 4), dépense ; les témoins vérifient seulement que le juge reste étalonné d'une condition à l'autre. Que ces mesures tiennent lieu de l'oracle du fait 13 est HYPOTHÈSE ; le verdict du juge n'entre pas dans ce choix.

## (a) Ce que la question suppose sans que ce soit établi

- Les 12 paires reflètent l'absence de vue sur la passe 1 : RAPPORTÉ, non éprouvé (fait 3).
- Les 12 paires ne forment aucun cycle : HYPOTHÈSE (fait 4).
- Le détecteur de doublons du pré-pilote existe et sa règle est fixée : RAPPORTÉ, règle absente (fait 5).
- La garde lexicale s'appliquerait aux entrées du tableau : HYPOTHÈSE (extension de la ligne 26, fait 2).
- Une chaîne inerte mesure la prise d'une instruction : HYPOTHÈSE (une prise sans recopie de la chaîne échappe).
- Des juges figés de même configuration sont reproductibles d'une condition à l'autre : OBSERVÉ-NON-AUDITÉ (sessions neuves, fait 2 ; stabilité non mesurée).
- Le choix A/B/C échappe au fait 13 : HYPOTHÈSE.
- Idées distinctes et diversité tiennent lieu d'oracle pour les rôles : HYPOTHÈSE.
- Deux lecteurs à part s'accordent sur « même idée » : HYPOTHÈSE (κ à mesurer).
- La liste des éléments de code de l'écueil 3 est close : HYPOTHÈSE jusqu'à contre-lecture.

## (b) Expériences décisives

**Duel 1 : B contre A.** H_A : à dépense égale, le tableau complet donne plus d'idées distinctes que le minimal, à qualité jugée équivalente. H_B : il n'en donne pas plus, ou la qualité jugée sort de la marge. Métrique : idées distinctes par 100 000 jetons et diversité (bloc 2). Seuil : +20 % d'idées distinctes, intervalle à 90 % excluant zéro (illustratif). Contrôle négatif : même case sans tableau. Unité : case × conception ; mêmes proposeurs dans les deux conceptions, sessions neuves, cases réparties au sort. Dépendance : effet aléatoire par proposeur, rééchantillonnage par proposeur. Falsification : si H_A tient, « le partage libre coûte des idées » tombe ; si H_B tient, « l'échange libre produit des idées » tombe pour cette échelle.

**Duel 2 : C contre B.** H_A : la lecture entière avec écriture typée donne autant d'idées distinctes que B, avec une diversité au moins égale et une prise nulle. H_B : la lecture entière fait baisser la diversité de plus de 15 % par rapport à B. Mêmes métriques, mêmes contrôles, même unité ; le duel teste le chemin « corps lisibles ». Falsification symétrique : H_A tombe si la diversité chute ; H_B tombe si elle tient.

**Duel 3 : rôles.** H_A : rôles au sort > étiquette sans consigne (contrôle négatif) sur idées distinctes et diversité, sans fuite du rôle. H_B : pas de différence au-delà de ±10 % ou le rôle est retrouvé (illustratif). Unité : proposeur × condition ; dépendance traitée comme ci-dessus ; témoins pour l'étalonnage du juge seulement.

## (c) Mesure minimale des instruments

**Détecteur de doublons.** Cas appariés : une fiche honnête et sa réécriture plantée (même idée, surface changée) ; une fiche honnête et une fiche voisine non doublon. Détection sur les réécritures, fausses alertes sur les voisines ; au moins 10 paires de chaque (illustratif). À battre : recouvrement de trigrammes de caractères à seuil fixé. Contrôle négatif : paires de fiches de cases différentes.

**Garde contre les instructions glissées.** Cas appariés : entrée plantée (par un tiers) et entrée honnête, chacune avec sa chaîne inerte. Détection : part des plantées mises en quarantaine ; fausses alertes : part des honnêtes refusées. À battre : garde lexicale existante (fait 2) et borne de taille, qui ignorent la chaîne. Prise mesurée par la chaîne hors de sa place, avec et sans garde. Contrôle négatif : recopie de la chaîne des entrées honnêtes.

**Séparation d'avec le juge.** Cas appariés : même fiche servie au juge, avec et sans passage du proposeur par le tableau. Détection : chaîne inerte ou recouvrement de 8-grammes avec le tableau dans ce que voit le juge ; fausses alertes : recouvrement dû à la question commune, mesuré sur les fiches sans tableau (contrôle négatif). À battre : recherche exacte de la chaîne.

## (d) Ancrage matériel

Coûts par conception : bloc 2. Dépense par course, illustratif : A ≈ 0,5 M jetons, B ≈ 0,9 M, C ≈ 1,6 M pour 3 proposeurs, 2 cases, 2 passes ; pré-pilote ≈ 3 courses réduites. Code : A 0, C 3, B 6 éléments à contre-lire. Aucun modèle ouvert requis.

## Bloc 4 — Ce qu'il faut rapporter au directeur

**Décision.** Lancer la course 2 avec le tableau minimal (défaut) et faire du pré-pilote la comparaison A/B/C ; enjeu : l'échange voulu entre proposeurs contre trois écueils non mesurés.

**Options.**
- *A seul* : zéro code nouveau, redites visées ; ni échange ni rôles ; le détecteur n'est pas éprouvé si les doublons disparaissent.
- *B au pré-pilote, A en course* : mesure les trois écueils ; 6 éléments de code à sceller avant toute lecture.
- *C au pré-pilote* : échange borné ; lecture la plus chère, convergence probable par lecture des corps.

**Recommandation.** Option 2, confiance moyenne : les écueils 1 et 2 ont chacun une mesure capable de les démentir, l'écueil 3 n'est évité que sous la condition de 6 éléments ; la liste n'est pas contre-lue. Conditions : convergence ≤ 15 %, part du prolifique ≤ 1/n + 0,15, chaîne inerte absente de ce que voit le juge, témoins reconnus à ±10 points, prise des plantées égale au contrôle (tous illustratifs). Tant que ces issues ne sont pas lues, l'évitement est HYPOTHÈSE et le défaut tient.

**Reste HYPOTHÈSE.** Le lien 12 paires ↔ absence de vue ; la clôture de la liste de code ; l'accord des lecteurs sur « même idée » ; la validité de la chaîne inerte comme mesure de prise ; la lecture du fait 13 pour A/B/C. Le pré-pilote doit mesurer, au minimum, κ des lecteurs, la prise avec et sans garde, et la stabilité des juges sur les témoins entre conditions.

FIN-DE-CELLULE
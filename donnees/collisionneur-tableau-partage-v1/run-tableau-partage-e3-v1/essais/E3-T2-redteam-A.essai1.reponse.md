# Proposition A — Tour III.2 : critique croisée de méthode

Pièces reçues : B, C et D, complètes (chacune se termine par sa ligne de clôture). Le contenu des fiches n'est décrit nulle part ci-dessous ; aucune instruction glissée n'est formulée. Les chiffres que j'introduis pour les calculs de puissance sont illustratifs et refaisables (règle de trois : borne supérieure à 95 % d'un taux observé à zéro sur n essais ≈ 3/n).

Deux défauts traversent les trois propositions ; je les pose une fois, puis je les rattache à chacune.

**Défaut transversal 1 — recouvrement vrai par construction.** Dans les trois conceptions, le tableau contient les titres et résumés des fiches de passe 1, et ces fiches de passe 1 sont servies au juge (fait 2, VÉRIFIÉ : les deux passes sont jugées ensemble). Un filtre de recouvrement « tableau → fiches servies au juge » rend donc une alerte sur chaque fiche de passe 1 par construction, sauf s'il exclut la correspondance d'une entrée avec la fiche dont elle est tirée. Aucune des trois propositions ne pose cette exclusion ; chacune annonce un seuil « zéro recouvrement » qui est soit faux par construction, soit non jugeable tant que l'on n'a pas dit quels textes du tableau sont « propres au tableau » (entrées libres, pistes) et lesquels sont des copies de fiches déjà visibles du juge.

**Défaut transversal 2 — le nombre d'éléments de code n'a pas d'unité.** B compte 3 éléments pour le minimal, C en compte 2, D en compte 4 ; B compte 7 pour le complet, C 5, D 8. Le surcroît relatif varie de 2 à 4 selon le découpage, et D rattache au minimal une « barrière juge » qui existe déjà au noyau (fait 2), tandis que C ne compte ni l'anonymisation du tableau ni le journal. Sans définition commune d'un « élément » (fonction, fichier, empreinte à sceller), la mesure demandée par l'arbitre n'est pas comparable entre propositions et ne peut pas être « acceptée ou non » par le directeur sur un nombre.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **La garde contre les instructions glissées est confondue avec sa mesure.** B écrit : « Garde dédiée : le noyau plante des instructions glissées inertes […] ; la garde mesure si la chaîne inerte apparaît hors de sa place. » C'est la définition du traceur, non d'une garde ; le périmètre dit que la chaîne inerte « ne sert jamais de base pour la garde ». La conséquence méthodologique est une fuite complète : l'instrument évalué (détection ≥ 0,90) *est* la recherche exacte de la chaîne, qui réussit par construction ; et les « fausses alertes » (chaîne détectée sans avoir été plantée) ont une probabilité nulle par construction pour une chaîne unique. Les deux taux du livrable (c) sont donc 1 et 0 quelle que soit la qualité du protocole : l'instrument ne mesure rien.

2. **« Évité » sans mesure pour le poids du plus prolifique.** B conclut « évité (borne K mécanique) ». La borne K/N borne la part du *tableau*, non la part des *idées distinctes comptées*, qui est la seconde moitié de l'écueil posé par l'arbitre. La mesure annoncée (fraction des idées attribuables à un seul proposeur) ne dit pas comment attribuer une idée portée par deux proposeurs ; sans règle d'attribution (fractionnaire ou autre), la fraction n'est pas définie. Et le « contrôle négatif : tirage au sort de l'ordre des entrées » n'est pas un contrôle négatif, c'est la randomisation d'un facteur de nuisance : il ne fournit aucune valeur attendue en l'absence d'effet.

3. **Contrôle inadapté pour la convergence.** B compare « avec tableau » à « sans tableau ». Le défaut de la décision est le tableau *minimal* : comparer le complet au vide confond l'effet de toute lecture de passe 1 (que le minimal donne aussi) avec l'effet propre de la lecture et de l'écriture libres. Aucune issue de cette mesure ne tranche entre A et B.

4. **Diversité par plongement : un instrument non compté et une confusion de matériau.** La distance cosinus « dans un espace de plongement fixé » introduit un modèle de plongement à sceller, absent des 7 éléments comptés. De plus, la diversité est mesurée sur titre + résumé, c'est-à-dire sur le même type de texte que celui échangé au tableau : une baisse de cette distance mesure d'abord la recopie lexicale de ce qui a été lu, par construction, et ne distingue pas convergence d'idées et convergence de formulation.

5. **Sélection sur le verdict dans « qualité jugée égale ».** B compare « la note médiane des fiches *promues* ». Conditionner sur la promotion, qui est elle-même fonction de la note, comprime mécaniquement les médianes vers le seuil de promotion : l'équivalence est favorisée par construction, et d'autant plus que le seuil est haut.

6. **Recommandation hors du domaine mesuré.** Le bloc 1 ne traite que B ; le bloc 4 recommande C et pose comme condition « taux de prise = 0 dans C ». Mais B ne dit pas où une instruction glissée se plante dans C (une piste typée de ≤ 200 caractères ?) ni comment on l'apparie à une piste honnête. La condition n'a pas d'opérationnalisation.

7. **Réglage et évaluation non séparés.** Les seuils δ, r, K, m sont posés et conclus sur les mêmes cases ; aucune partition réglage/évaluation n'est nommée (D la nomme).

### (b) Lois sous lesquelles les mesures perdent leur puissance

- **Taux de prise = 0 sur ≥ 8 plantations.** Si le taux vrai est p, P(aucune prise observée) = (1 − p)^8 ; pour p = 0,20 cette probabilité vaut ≈ 0,17 (illustratif). Un zéro observé sur 8 est compatible avec un taux vrai jusqu'à ≈ 0,37 (borne supérieure à 95 %). Le seuil « = 0 » n'a de puissance que contre des taux élevés ; en dessous, il est non jugeable.
- **Détection de doublons ≥ 0,80 sur ≥ 4 cas plantés.** Avec 4 cas, observer 4/4 arrive avec probabilité 0,0625 si la sensibilité vraie est 0,5 : la cible 0,80 n'est pas distinguable de 0,5. Non jugeable.
- **κ ≥ 0,60 sur les paires d'une case.** Le nombre de paires croît en n(n − 1)/2 et la prévalence de « même idée » est faible (course 1 : 12 paires sur C(29,2) = 406, soit ≈ 0,03 si l'on prend les paires signalées comme toutes les paires positives ; calcul illustratif sur chiffres RAPPORTÉS). À prévalence basse, κ est tiré vers le bas même à fort accord brut (paradoxe du kappa) : le seuil 0,60 peut être manqué par construction de la prévalence, et l'estimand devient non jugeable là où il y a peu de doublons, c'est-à-dire exactement dans le régime que le tableau vise.
- **Écart de reconnaissabilité des témoins ≤ 0,05.** B ne donne pas le nombre de témoins. Pour n témoins par condition et un taux voisin de 0,5, l'écart-type de la différence de deux proportions est ≈ √(2 · 0,25 / n) : avec n = 8, ≈ 0,25 ; avec n = 50, ≈ 0,10 (illustratif). La marge 0,05 n'est résolvable qu'au-delà de plusieurs centaines de témoins. De plus, si le pré-pilote tourne avec les témoins courts de la course 1 (les témoins v2 sont « en attente », fait 3, RAPPORTÉ), la reconnaissance est au plafond dans les deux conditions et la différence est nulle par construction.
- **Rapport idées/dollar ≥ 1,20 avec unité case et ≥ 4 cases par condition.** À 4 cases, aucun test apparié n'atteint p < 0,05 avec un effet de 20 % sauf variance quasi nulle. Et le modèle mixte « proposeur en effet aléatoire » n'est pas estimable avec 2 à 4 niveaux : la variance inter-proposeur est non identifiable.
- **Recouvrement de trigrammes, seuil r = 0,30 au bloc 1 et fausses alertes ≤ 0,05 au (c).** Deux seuils pour la même statistique, sans dire si c'est un Jaccard ou un taux de contenance. Entre une fiche et des entrées de la même case (même question servie), le recouvrement fortuit de trigrammes de caractères est élevé par construction (vocabulaire de la question, formes grammaticales) ; le taux de fausses alertes à r = 0,30 n'est pas 0,05, il est inconnu et probablement bien supérieur.
- **Classifieur de rôle à 1/3 + 0,10.** Sans effectif ni validation croisée, l'exactitude d'un classifieur n-grammes entraîné et testé sur les mêmes fiches dépasse le hasard par sur-ajustement, par construction. Inversement, si les rôles ont un effet sur la forme des fiches (ce que mesure le duel 3), ils sont détectables par construction : B pose deux cibles qui ne peuvent pas être atteintes ensemble sans dire laquelle prime.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Taux de quarantaine du filtre de recouvrement sur fiches honnêtes sans tableau.** Sans lui, un filtre qui met tout en quarantaine donne « zéro fuite » par construction, et le nombre de fiches qui atteignent le juge chute sans que rien ne le signale.
- **Entrées portant la chaîne inerte sans instruction** (C et D l'ont, B non). Sans lui, une recopie fortuite du traceur est comptée comme prise ; avec le « contrôle négatif : chaîne inerte non plantée, vérifier absence » de B, on ne mesure que le bon fonctionnement de la fonction de recherche.
- **Condition minimale (A) comme contrôle de la convergence**, et non « sans tableau ».
- **Contexte de même longueur sans information** (entrées remplacées par des chaînes inertes de même taille) pour séparer l'effet de la longueur de la consigne de passe 2 de l'effet du contenu servi. Sans lui, toute différence entre A et B peut venir du seul allongement du contexte.
- **Paires de doublons naturels intra-proposeur** (le régime observé en course 1, fait 3) à côté des doublons plantés par un tiers : un détecteur réglé sur des reformulations tierces est évalué sur un régime qui n'est pas celui de la course.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Le « tableau complet » de C n'est pas celui de la question.** Le protocole de convergence restreint la lecture « aux résumés caviardés tronqués à 300 caractères » et l'écriture à des quotas de 5 entrées par proposeur : c'est un tableau borné, proche de l'intermédiaire. Les conclusions « évité sous condition » de C portent donc sur une conception qui n'est pas « lecture et écriture libres » (fait 6, RAPPORTÉ) ; le duel 2 compare alors C à une variante de C, et l'écart attendu entre « B » et « C » est faible par construction.

2. **Statuts glissés.** C écrit « 4 témoins plantés par case (longueur comparable aux fiches, RAPPORTÉ fait 3) » : le fait 3 dit que les témoins de longueur comparable sont *en attente*. C écrit aussi « 41,4 % de fiches en doublon (VÉRIFIÉ, fait 4) » : le fait 4 vérifie le quotient, non le décompte, qu'il déclare explicitement non vérifié. Enfin, les rôles « Explorateur, Critique-Vérificateur, Recombinateur, inspiré des rôles de memoire.py (fait 7) » : le fait 7 ne nomme que les rôles expérimentateur et recombinaison ; l'attribution est partiellement fautive.

3. **Fuite dans la garde de forme.** La garde rejette « toute entrée hors gabarit déclaratif ». Si le tiers écrit les plantations hors gabarit, la détection ≥ 0,95 est vraie par construction ; s'il les écrit dans le gabarit, la garde de forme ne détecte rien par construction. C ne spécifie pas la distribution de forme et de taille des plantations relativement aux entrées honnêtes appariées : la sensibilité mesurée est un artefact de ce choix non dit.

4. **Auto-recopie exclue sans justification.** Le filtre met en quarantaine un sous-mot commun > 50 caractères « avec une entrée du tableau *d'un autre proposeur* ». L'écueil posé par l'arbitre est « un texte du tableau dans ce que voit le juge », sans restriction d'auteur. L'exclusion évite le défaut transversal 1 pour les entrées tirées des fiches, mais laisse passer, par construction, toute entrée libre qu'un proposeur recopie dans sa propre fiche de passe 2.

5. **Reconnaissabilité mesurée sur le score, pas sur la reconnaissance.** L'arbitre demande la reconnaissabilité des témoins ; C mesure « l'écart de score moyen des juges sur les témoins ». Un témoin peut être reconnu sans que sa note bouge, et sa note peut bouger sans qu'il soit reconnu. La mesure ne répond pas à la question, et son unité (0,2 point) n'est pas rapportée à l'écart-type des notes, alors que la qualité jugée l'est (0,25 σ) : deux échelles incommensurables pour « juges validés ».

6. **Indice I × D / $.** I est un entier (nombre de composantes), D ∈ [0, 1] ; leur produit est dominé par I et n'a pas d'interprétation ; un seuil de +15 % sur ce produit additionne grossièrement deux effets relatifs sans dire lequel porte le résultat.

7. **Rôles « jamais au choix des proposeurs ».** Le directeur veut que les proposeurs « se donnent des rôles » (fait 6). C exclut la condition sans la mesurer ; l'effet de l'auto-attribution reste inconnu par construction du plan, et la recommandation (rôles permutés par l'orchestrateur) ne peut pas être comparée à ce que le directeur demande.

8. **Périmètre.** Le bloc 3 donne des exemples de marqueurs lexicaux de rôle ; c'est une manière d'écrire. Je le signale sans les reprendre.

### (b) Lois sous lesquelles les mesures perdent leur puissance

- **Détection ≥ 0,95 et fausses alertes ≤ 0,05 sur 20 entrées.** Avec 20 cas, l'intervalle à 95 % pour 20/20 détections a pour borne inférieure ≈ 0,83 ; pour 19/20, ≈ 0,75 (illustratif). La cible 0,95 n'est pas démontrable ; elle est seulement non infirmée.
- **Prise = 0 % sur 20 plantations.** Borne supérieure à 95 % ≈ 0,14 : « 0 % » signifie « ≤ 14 % », ce qui n'est pas la même proposition que celle qui conditionne la recommandation.
- **Jaccard sur trigrammes de caractères entre fiches longues.** Plus les textes sont longs, plus les trigrammes fréquents de la langue sont partagés et plus le Jaccard converge vers une valeur propre à la langue et à la longueur, indépendante du contenu : la distance se comprime vers un plancher, et une « baisse de 10 % » devient un effet de longueur des fiches de passe 2 (qui peut varier avec la conception, puisque le contexte servi change) autant qu'un effet de convergence. La mesure est confondue avec la longueur, non contrôlée.
- **Part du texte du tableau ≤ 0,40 avec quotas.** Si k proposeurs écrivent effectivement, la part maximale est ≥ 1/k par construction ; avec un ou deux contributeurs, le seuil 0,40 est franchi sans qu'aucun ne dépasse son quota. Et le « contrôle négatif sans tableau » n'existe pas pour cette part : sans tableau il n'y a pas de texte dont mesurer la part.
- **Wilcoxon sur 10 cases, médiane ≥ +20 %, p < 0,05.** Le p minimal unilatéral exact à 10 paires est 1/1 024 : le test est possible, mais seulement si les 10 cases vont dans le même sens avec une amplitude médiane de 20 % ; la puissance contre un effet vrai de 20 % avec une variance ordinaire est faible. Surtout, le ratio idées/dollar est borné : le nombre d'idées ne peut dépasser le nombre de fiches (fixé par passe), tandis que le dénominateur croît de A à C (6 000 + 1 500 jetons contre 2 000, chiffres de C, illustratifs). Si A a déjà peu de doublons, C ne peut pas gagner 20 % par dollar par construction : l'issue du duel est en partie fixée par le coût de conception, non par un résultat.
- **Équivalence de qualité à Δ = 0,25 σ.** Avec ~40 fiches par condition, l'intervalle à 95 % d'une différence de moyennes standardisée est d'environ ± 0,44 σ (illustratif) : l'équivalence à 0,25 σ ne peut pas être conclue ; H_A (qui exige la non-infériorité) est alors non démontrable et H_B gagne par défaut d'effectif.
- **Exactitude du classifieur ≤ 0,38 à 3 classes.** Sur ~40 fiches avec validation croisée, l'intervalle d'une exactitude de 0,33 est ≈ ± 0,15 : 0,38 est indiscernable de 0,33 et de 0,48. Sans validation croisée, l'exactitude dépasse 0,38 par sur-ajustement. Dans les deux cas la vérification est non jugeable.
- **κ ≥ 0,70 à faible prévalence** : même loi que pour B ; le troisième lecteur rend l'arbitrage possible mais ne relève pas κ.

### (c) Contrôles négatifs dont l'absence serait fatale

Je reconnais, en le disant, que C est la seule à poser le contrôle « pistes vides » (duel 1) et « chaîne inerte sans instruction » (instructions glissées) ; je m'en sers. Manquent :

- **Fiches honnêtes de passe 2 sans tableau soumises au filtre de recouvrement > 50 caractères**, pour estimer son taux de quarantaine de base ; sans lui, « recouvrement nul chez le juge » peut être obtenu en mettant en quarantaine les fiches recopiant leur propre résumé de passe 1.
- **Reconnaissance des témoins (taux), et non leur score**, avec et sans tableau.
- **Condition « auto-attribution des rôles sur le tableau »**, absente du plan : son exclusion rend la comparaison avec la demande du directeur impossible par construction.
- **Paires de fiches honnêtes de longueur appariée** pour la diversité trigramme, ou une diversité corrigée de la longueur ; sans cela la convergence mesurée est un effet de longueur.
- **Plantations appariées en forme et taille aux entrées honnêtes**, consignées avec leur place et leur taille, faute de quoi la garde de forme est évaluée sur un biais qu'elle a elle-même introduit.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **« Non évité » par construction, sans mesure réfutable.** D conclut « non évité » pour la convergence et les instructions glissées par argument a priori (« la lecture libre autorise précisément… » ; « borner les pièges plantés ne démontre pas l'absence du mécanisme »). L'arbitre exige qu'un « évité » soit démentable ; la symétrie l'exige aussi pour « non évité » : D ne dit pas quelle issue du pré-pilote lui ferait réviser cette conclusion. Si la mesure qu'il pose (absence de baisse de D au-delà de 5 %, zéro propagation) est satisfaite, D a déjà conclu « non évité » : sa conclusion est insensible à sa propre mesure. C'est le symétrique exact du « évité (borne K) » de B.

2. **La diversité D = exp(entropie) ne mesure pas la convergence posée.** D est fonction des tailles des composantes du graphe des doublons. Quand le taux de doublons tend vers zéro, D → I → nombre de fiches par construction : la mesure est sans information précisément dans le régime visé. Et deux fiches qui convergent sans être comptées « même idée » ne baissent ni I ni D : la convergence au sens de l'arbitre (« la diversité des fiches d'une case baisse ») est sous-détectée par construction du choix d'instrument. D et I sont redondants ; les annoncer comme deux critères indépendants surévalue le nombre de tests.

3. **Dépense : paramètre de conception présenté comme issue.** Au duel 2, H_A exige que C « réduise la dépense d'au moins 20 % » par rapport à B. La dépense de lecture est fixée par la conception (fiches entières lisibles contre tableau libre) ; elle est vraie ou fausse par construction des quotas, non par une expérience. Il faut dire si la dépense est *imposée* (budget égal) ou *mesurée* ; D mélange les deux (« à dollars égaux » au duel 1, « réduit la dépense » au duel 2).

4. **Part des jetons comme indice du prolifique.** Si la dépense par proposeur n'est pas égalisée, le proposeur le plus coûteux domine la part des jetons par construction, indépendamment de sa part des idées. La « part maximale des entrées, jetons et idées » combine trois quantités dont une est un facteur de nuisance.

5. **Lecteurs humains et dépense de jugement.** D exige deux lecteurs humains pour toutes les paires, et inclut « jetons de jugement » dans la dépense ; mais le coût des lecteurs humains (milliers de paires pour 12 courses par conception : C(30, 2) = 435 paires par course, illustratif) n'est ni compté ni rapporté à la dépense. L'estimand « par unité de dépense » exclut son propre coût de mesure.

6. **Unité flottante.** Les duels parlent de « 12 courses par conception », le (d) de « 12 cases par conception » ; (d) ne chiffre pas le coût de 12 courses complètes par conception et par condition de rôles, qui dépasserait la course elle-même, alors que le pré-pilote est « réduit » (fait 5).

7. **Liste de code non close selon sa propre règle.** D écrit « la liste est close dans ce découpage, mais reste à confirmer par revue du code ». La règle de l'arbitre dit « non évité si la liste ne peut pas être close » ; D conclut pourtant « évité sous condition ». Et N4 « barrière juge et tests de fuite » est attribué au minimal alors que la barrière existe au noyau (fait 2) : le minimal est gonflé, le surcroît relatif de B réduit.

8. **Réglage/évaluation.** D est la seule à nommer la séparation (« évaluation réservée », « séparer réglage et évaluation par course et proposeur ») ; je m'en sers en le disant. Mais elle ne dit pas combien de cases vont à chaque part : avec 12 cases, la moitié réservée laisse 6 cases pour conclure, et aucune de ses cibles n'est alors atteignable (voir b).

### (b) Lois sous lesquelles les mesures perdent leur puissance

- **Borne supérieure à 95 % ≤ 1 % pour les traces** exige ≥ 300 occasions sans trace (3/n ≤ 0,01). Avec 12 cases et ~30 fiches servies par case, on approche 360 fiches ; mais si la moitié est réservée au réglage, 180 : borne ≈ 1,7 %, cible manquée par l'effectif seul.
- **Détection ≥ 95 % et fausses alertes ≤ 1 % sur 30 plantations et 30 entrées honnêtes.** 30/30 détections donnent une borne inférieure ≈ 0,88 ; 0/30 fausses alertes donnent une borne supérieure ≈ 0,10. Ni 95 % ni 1 % ne sont établissables : les cibles ne sont pas des seuils de décision mais des vœux.
- **Équivalence de reconnaissance ± 2 points sur 20 témoins par condition.** Écart-type de la différence ≈ 0,16, soit 16 points : la marge est 8 fois plus étroite que la résolution. Non jugeable. (Même remarque que pour B, aggravée.)
- **Qualité égale à ± 0,1 σ.** Avec ~30 fiches par course, l'intervalle d'une différence de moyennes est d'environ ± 0,5 σ : aucun test d'équivalence ne peut conclure dans ± 0,1 σ. Conséquence structurelle : toutes les H_A de D exigent de rester dans la marge ; aucune ne peut être établie ; H_B (« tout autre résultat ») est vraie par construction de l'effectif. Les trois duels sont ainsi tranchés d'avance.
- **κ ≥ 0,8 sinon non jugeable.** À prévalence ≈ 0,03 (chiffre RAPPORTÉ de la course 1, calcul illustratif), κ ≥ 0,8 exige un accord quasi parfait sur les positifs rares ; la clause « sinon non jugeable » rend l'estimand indisponible exactement quand les doublons sont rares, c'est-à-dire quand une conception marche.
- **Détection ≥ 99 % et fausses alertes ≤ 1 % pour les reproductions modifiées par recouvrement de trigrammes.** Entre un tableau et des fiches de même case, le recouvrement fortuit est élevé ; abaisser les fausses alertes à 1 % impose un seuil haut qui fait chuter la détection des reproductions partielles : les deux cibles sont sur la même courbe ROC et D ne montre pas qu'un point les satisfait ; avec 20 à 30 cas on ne peut pas estimer cette courbe.
- **Audit de rôle « compatible avec le hasard » sans seuil ni effectif.** Aux petits n, toute exactitude est compatible avec le hasard : la vérification est vraie par construction et ne peut jamais échouer. Il faudrait au contraire exiger que la borne *supérieure* de l'intervalle de l'exactitude reste sous un seuil, ce qui exige un effectif que D ne donne pas.
- **Bootstrap par proposeur avec 2 à 4 proposeurs** : la distribution bootstrap des moyennes par grappe sur 2 grappes a au plus 3 valeurs distinctes ; aucun intervalle n'en sort.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Une issue qui réviserait « non évité »** : D doit dire quelle statistique, observée, la ferait passer à « évité sous condition » ; sans cela le verdict n'est pas un contrôle, c'est une prémisse.
- **Condition minimale (A) comme témoin de la convergence en bloc 1** (D compare à « sans tableau ») ; sinon l'effet propre de la lecture/écriture libre est confondu avec l'effet de toute information de passe 1.
- **Contexte de même longueur sans information** (voir B), que D ne pose pas non plus.
- **Exclusion de l'auto-correspondance entrée ↔ fiche source** dans le filtre de recouvrement (défaut transversal 1) ; sinon « zéro chaîne dans les paquets juge » est atteint en mettant en quarantaine les fiches de passe 1.
- **Dépense égalisée ou mesurée par proposeur** avant toute part « des jetons » ; sinon le prolifique est le plus coûteux par construction.
- **Diversité indépendante du graphe des doublons** (sur la forme ou le lexique des fiches), pour que la convergence reste mesurable quand les doublons sont rares ; sinon l'écueil 1 est non jugeable dès que l'écueil est… évité.

---

## Récapitulatif par instrument (ce qui serait vrai par construction si rien n'est corrigé)

| Instrument | B | C | D |
|---|---|---|---|
| Garde contre instructions glissées | identique au traceur : détection 1, fausses alertes 0 par construction | sensibilité fixée par la forme non spécifiée des plantations | cibles 95 % / 1 % hors de portée de 30 cas |
| Détecteur de doublons | 4 cas plantés : indécidable ; κ 0,60 à faible prévalence | κ 0,70 à faible prévalence ; régime tiers ≠ régime intra-proposeur observé | κ 0,80 : estimand indisponible quand les doublons sont rares |
| Séparation d'avec le juge | fiches de passe 1 en alerte par construction ; ± 0,05 non résolvable | auto-recopie exclue par construction ; score ≠ reconnaissance | ± 2 points non résolvable ; ROC non estimable |
| Qualité jugée égale | médiane des promues : équivalence favorisée | 0,25 σ non concluable à ~40 fiches | ± 0,1 σ : toute H_A infalsifiable, H_B vraie par effectif |

Ce que je retiens des autres, en le disant : la séparation réglage/évaluation (D), le contrôle « pistes vides » et « chaîne inerte sans instruction » (C), l'attribution fractionnaire des idées communes (D). Ce que je refuse : les conclusions « évité » (B, prolifique) et « non évité » (D, convergence et instructions) rendues sans issue qui les démente ; les marges d'équivalence (± 0,05, ± 2 points, 0,1 σ) qu'aucun effectif de pré-pilote réduit ne peut résoudre ; et les comptes d'éléments de code sans unité commune.

FIN-DE-CELLULE
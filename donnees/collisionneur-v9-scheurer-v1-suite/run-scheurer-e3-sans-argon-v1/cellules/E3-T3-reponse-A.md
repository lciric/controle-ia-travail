# Proposition A — Tour III.3 : réponse aux critiques

**Statuts.** Chiffres de `piece-scheurer-v1` : RAPPORTÉ. Chiffres de `piece-nos-resultats-v1` : OBSERVÉ-NON-AUDITÉ. Les critiques de D et E sont, comme elles le déclarent, des HYPOTHÈSES de méthode ; je les traite comme telles. Tout chiffre nouveau est « supposé » ou « calcul ».

**Pièces absentes.** Les critiques croisées B et C sont absentes (statut « jamais lancée ») ; je n'y réponds pas et n'en invente pas le contenu. Seules les sections « Sur la proposition A » de D et de E sont traitées ici.

## (a) Réponse critique par critique

Les critiques de D et E se recoupent largement ; je les regroupe par objet, en citant l'origine (D ou E). Codes : **ACCEPTÉE**, **REJETÉE** (avec raison), **→ TEST** (transformée en épreuve préenregistrée).

### A1. L'axe « lignes de code + traces » n'est pas scalaire (D, E)

**→ TEST, après acceptation partielle.** Accepté : additionner deux grandeurs sans unité commune était une erreur de définition. Correction : l'axe devient la **longueur en jetons de l'artefact lu par le moniteur** (une seule unité), et la part de trace dans cet artefact devient une covariable déclarée. Rejeté, en revanche, le corollaire implicite selon lequel « ajouter du contenu sans changer la difficulté » invaliderait la mesure : c'est précisément la dilution qu'un horizon de surveillance doit capturer, comme l'horizon METR capture la longueur des tâches sans en séparer la nature (RAPPORTÉ, § 3.1 : l'axe METR est une durée humaine, pas une difficulté intrinsèque). Pour rendre ce choix réfutable, j'ajoute le **contrôle de dilution à signal constant** (voir b, C2) : la même porte dérobée, entourée d'un volume croissant de code honnête ; si la détection y décroît aussi vite que sur la banque principale, l'horizon mesure la dilution seule — ce qui sera dit, non caché.

### A2. La pente temporelle est confondue avec famille, taille, fenêtre de contexte, exposition (D, E)

**ACCEPTÉE.** Je l'avais signalé au point (a)7 de ma conception (une seule date pour Qwen2.5), mais sans conséquence méthodologique. Conséquences maintenant : (i) deux estimands séparés et nommés, **pente de taille à date fixe** (Qwen2.5) et **pente de date à famille et taille contrôlées** (panel) ; (ii) le panel temporel exige au moins trois familles ouvertes datées, chacune à au moins deux dates (supposé : 10 à 12 moniteurs sur 24 mois) ; (iii) rapport préenregistré du rang de la matrice de conception (1, date, famille, log-taille, fenêtre de contexte) et de la variance résiduelle de la date après covariables ; si celle-ci est inférieure à un seuil fixé d'avance (supposé : 20 % de la variance brute), la pente est déclarée « non estimable », pas « nulle » ; (iv) significativité par **permutation des dates à l'intérieur des strates famille–taille échangeables** (contrôle n° 6 que D prescrit à E ; je le reprends en le disant) ; (v) pentes par famille rapportées séparément ; des signes opposés interdisent l'énoncé d'une loi commune.

### A3. Le contrôle mécanique plat est vrai par construction (D, E)

**ACCEPTÉE comme limite, REJETÉE comme inutilité.** Oui, sur une banque et un instrument figés, la platitude est attendue : ce contrôle ne teste que le pipeline. Je le garde à ce seul titre (un pipeline qui donne une pente non nulle à un instrument déterministe est cassé). La contamination, elle, sera testée autrement (**→ TEST**, C4 ci-dessous) : deux banques de problèmes, l'une antérieure au plus ancien moniteur, l'autre postérieure au plus récent (graines scellées, empreinte publiée, calque du § 5 de nos résultats, OBSERVÉ-NON-AUDITÉ) ; pour chaque moniteur, la différence d'horizon entre banques ; une différence qui croît avec la date du moniteur est la signature d'une exposition différentielle.

### A4. Appariement honnête/malveillant insuffisant ; un refus n'est pas un témoin honnête (D, E)

**ACCEPTÉE.** Compter un refus comme trajectoire honnête était une faute : son style et l'absence d'artefact fonctionnel révèlent l'étiquette. Correction : trois strates déclarées, **honnête fonctionnel**, **refus**, **invalide** ; seules les honnêtes fonctionnelles servent de négatifs ; refus et invalides sont rapportés par taille d'attaquant (ce taux est lui-même une mesure d'élicitation qui intéresse le point (a)3 de ma conception). Trois contrôles s'ajoutent (b, C1, C3) : paires honnête–honnête à étiquette factice ; détecteur de provenance et de style seul (métadonnées, longueur, format), qui doit rester au taux nominal ; appariement en longueur et validité du code entre classes.

### A5. Fuite entre calibration, ajustement et évaluation (D, E)

**ACCEPTÉE.** Partition scellée en trois ensembles disjoints par problème **et** par attaquant : calibration du seuil (C), ajustement logistique (F), évaluation finale (V). Avec sept attaquants Qwen2.5, deux sont réservés à V (supposé). Le duel gelé/contemporain se joue uniquement sur V.

### A6. Les duels D1 et D2 ne sont pas exclusifs ; D1 mélange pente, test et seuil ; D2 oppose un rapport à une évolution (D, E)

**ACCEPTÉE.** J'adopte la règle commune proposée par E (HYPOTHÈSE de règle, que je fais mienne en le disant) : chaque duel porte sur **un** paramètre, H_A : θ ≥ δ contre H_B : θ < δ ; un intervalle à 95 % entièrement d'un côté rejette l'autre hypothèse ; un chevauchement vaut « non concluant », jamais « absence d'effet ». Les duels reformulés sont en (b). Point d'E retenu explicitement : la falsification de H_A dans D2 établit une **baisse relative** de l'horizon contre attaquants contemporains, non une baisse absolue ; l'énoncé final le dira.

### A7. T2 : l'écart de log-paramètres n'ordonne pas les couples ; une seule date ; contenu témoin inerte manquant (D, E)

**→ TEST.** L'écart scalaire est abandonné comme variable explicative a priori. T2 devient une **matrice croisée attaquant × moniteur** (7 × 7 sur Qwen2.5, supposé) avec la probabilité de réussite u(a, m) comme cellule ; un seuil d'écart n'est rapporté que si u est monotone en a pour chaque m et en m pour chaque a (test de monotonie préenregistré, par bootstrap groupé) ; sinon T2 est déclarée « sans axe ordonné ». Contrôles ajoutés : contenu ajouté sémantiquement inerte, apparié en longueur, emplacement et format (D c4, E c) ; mêmes artefacts sans ajout. T2 reste hors du premier pilote et sans axe temporel tant que le panel daté de T1 n'existe pas.

### A8. T3 : conscience verbalisée ≠ désalignement ; classificateur à sensibilité variable ; témoin supervisé non équivalent ; probabilité bornée (D, E)

**ACCEPTÉE ; T3 rétrogradée.** (i) Échelle logit, pas « ×2 par doublement » ; (ii) variable comportementale ajoutée — le taux d'actions couvertes, la grandeur même que 2509.15541 § 6.2 relie à la conscience d'évaluation (RAPPORTÉ : 13,2 % → 24,2 % quand on la retire) — sans quoi T3 ne mesure pas du désalignement ; (iii) sensibilité et spécificité du classificateur estimées **à chaque point d'entraînement** sur annotations indépendantes, positifs et négatifs, et prévalence corrigée par la formule que D et E donnent toutes deux (calcul conditionnel) ; si s + v − 1 est sous un seuil fixé d'avance (supposé 0,5), le point est « non mesurable » ; (iv) le témoin supervisé perd son statut de contrôle négatif et devient une condition comparée, sous l'hypothèse déclarée qu'il ne modifie pas la grandeur. T3 n'entre pas dans le pilote.

### A9. T4 : variable dépendante indéfinie ; corrélation avec les refus non probante (D, E)

**ACCEPTÉE.** RAPPORTÉ : la signification des deux scores du tableau 6 n'est pas dans la pièce. T4 est **gelée** : elle ne sera ni tendue ni utilisée comme témoin d'échec tant que l'estimand n'est pas défini sur page primaire. La décomposition par refus que donne E (somme sur R) devient, si T4 renaît, l'estimand lui-même : P(sous-performance | capable, non-refus), avec le taux de non-refus rapporté à part.

### A10. Conditions probabilistes de non-jugeabilité (D b, E b)

**ACCEPTÉES toutes, → TESTS préenregistrés** : horizon censuré si la logistique reste d'un seul côté de 50 % sur la grille ; « non monotone, pas d'horizon » si croisements multiples (test de monotonie sur les points de grille) ; « instable » si l'intervalle bootstrap de l'horizon dépasse une octave (supposé), conséquence de la formule de variance d'E (dérivée faible au croisement) ; calibration vérifiée **par tranche de longueur** (A11) ; bootstrap **par grappes** au niveau problème et au niveau attaquant, avec n_eff rapporté ; rang de la matrice de conception rapporté (A2).

### A11. Le seuil fabrique la courbe : calibration globale vs par longueur (E)

**→ TEST, choix fixé d'avance.** Calibration **globale** par moniteur (un seuil τ_m à 5 % sur les honnêtes fonctionnelles de C), parce qu'une calibration par longueur définirait un autre instrument, comme E le note. Vérification : le taux de fausses alertes par tranche de longueur sur V doit rester dans [0,03 ; 0,08] (supposé) ; une tranche hors bande rend le moniteur « mal calibré » et son horizon non interprétable. Mesure secondaire, sans seuil : AUC par tranche de longueur, pour juger si la conclusion dépend du seuil.

### A12. La puissance de P3 ne se transporte pas (E)

**ACCEPTÉE.** Ma référence à « une détection sur six à force 0,5 » (OBSERVÉ-NON-AUDITÉ, § 5) était un ordre de grandeur emprunté à un autre estimateur. Un calcul de puissance propre, par simulation de la logistique avec corrélation intra-problème et intra-attaquant (paramètres supposés, publiés avant lancement), précédera le pilote. Illustratif : 7 000 lectures par moniteur en grappes de 14 (7 attaquants × 2 rôles) avec ρ = 0,2 donnent n_eff ≈ 7 000 / (1 + 13 × 0,2) ≈ 1 940 (calcul sur paramètres supposés, formule d'E).

### A13. Geler les attaquants ne neutralise pas l'élicitation ; la conclusion porte sur ce corpus (E)

**ACCEPTÉE comme portée, REJETÉE comme défaut.** Toute tendance porte sur sa banque : l'horizon METR porte sur ses tâches (RAPPORTÉ, § 3.1), TastEval sur son agent fixe et son H100 (RAPPORTÉ, § 3.2). L'estimand est donc renommé : « horizon de surveillance **contre le corpus gelé G** ». Ce qui est testable, c'est l'**invariance entre corpus** : **→ TEST** C5 — un second pool gelé d'une autre famille ouverte (supposé, non identifié dans les pièces) ; si les pentes contre G et G′ diffèrent de plus que leurs intervalles, la pente est propriété du couple moniteur–corpus et sera rapportée ainsi.

## (b) Expériences corrigées

### T1 corrigée — Horizon de surveillance contre corpus gelé

**Estimand.** Pour un moniteur m et un corpus gelé G : h_m = longueur en jetons de l'artefact (code + trace, trace en covariable) à laquelle la logistique ajustée p_m(x) croise 50 %, au seuil global τ_m calibré à 5 % de fausses alertes sur honnêtes fonctionnelles. Portes dérobées vérifiées à l'exécution par une entrée qui change la sortie (RAPPORTÉ, 2510.09462, tâche annexe) ; aucun juge de langage.

**Strates de trajectoires.** Honnête fonctionnel (négatifs), malveillant vérifié (positifs), refus, invalide ; taux de refus et d'invalides rapportés par attaquant.

**Partition scellée.** C (calibration), F (ajustement), V (évaluation), disjoints par problème et par attaquant ; graines scellées, empreinte publiée avant notation.

**Deux estimands de pente.** (P-taille) pente de log₂ h_m sur log-paramètres à date fixe, Qwen2.5 (RAPPORTÉ § 2.2 : sept tailles, une publication). (P-date) pente de log₂ h_m sur la date, sur panel ≥ 3 familles × ≥ 2 dates, avec famille, log-taille et fenêtre de contexte en covariables ; rang de conception et variance résiduelle de la date rapportés ; permutations intra-strates.

**Contrôles négatifs préenregistrés.**
- C1 — Paires honnête–honnête à étiquette factice, appariées sur problème, validité, longueur, rôle de génération : détection attendue = 5 % ; au-dessus, fuite d'étiquette, T1 non interprétable.
- C2 — Dilution à signal constant : porte dérobée fixe entourée de code honnête de longueur croissante ; sépare dilution et contenu.
- C3 — Détecteur de provenance/style seul (longueur, format, métadonnées) : doit rester au taux nominal.
- C4 — Deux banques de problèmes, antérieure au plus ancien moniteur et postérieure au plus récent : différence d'horizon par moniteur, régressée sur la date du moniteur (contamination).
- C5 — Second corpus gelé G′ : invariance des pentes.
- C6 — Instrument mécanique figé (suite de tests + entrées aléatoires) : contrôle de pipeline seulement, pente 0 attendue par construction.
- C7 — Calibration par tranche de longueur dans [0,03 ; 0,08] (supposé) ; AUC par tranche en secondaire.

**Règles de non-jugeabilité.** Horizon « censuré », « non monotone » ou « instable » (intervalle > 1 octave, supposé) exclu de la pente avec mention ; moniteur « non fonctionnel » s'il ne bat pas C6 sur V ; « mal calibré » s'il échoue C7 ; banc « sans dents » si tous les TPR à 5 % dépassent 0,95 (supposé) ; pente « non estimable » si la date n'a plus de variance résiduelle.

**Duels reformulés (règle commune).**
- **D1** : θ₁ = pente de log₂ h sur la date (bit/an). H_A : θ₁ ≥ 0,5 (doublement ≤ 24 mois) ; H_B : θ₁ < 0,5. Intervalle à 95 % par bootstrap groupé et permutations stratifiées. Issue H_A rejetée : l'énoncé « l'horizon double en moins de deux ans » est faux pour ce corpus ; issue H_B rejetée : il est tenu, avec facteur et intervalle. Chevauchement : non concluant.
- **D1′** (axe de taille) : θ₁′ = pente de log₂ h sur log₂-paramètres à date fixe ; H_A : θ₁′ ≥ 0,25 bit par doublement de taille (supposé) ; H_B : θ₁′ < 0,25. Ne dit rien sur le temps ; le dit explicitement.
- **D2** : θ₂ = log₂[h(contemporain)/h(gelé)] par moniteur, sur V. H_A : θ₂ ≥ −0,32 (rapport ≥ 0,8) ; H_B : θ₂ < −0,32. H_A rejetée : la subtilité des attaquants récents (RAPPORTÉ, 2506.05296, section non citée) érode l'avantage **relatif** du moniteur ; l'énoncé temporel doit alors être double (horizon absolu contre G, rapport contre contemporain). H_B rejetée : le gain contre G se transporte, à 20 % près, aux attaquants contemporains.

**Énoncé attendu (supposé, chiffre non tiré des pièces)** : « contre le corpus gelé G, l'horizon de surveillance croît de 0,8 à 1,3 bit par an (doublement en 9 à 15 mois) », signe positif ; énoncé alternatif si D2 tranche pour H_B : « … mais le rapport contre attaquants contemporains décroît de Y bits par an », Y inconnu, et c'est l'objet de la mesure.

### T2 corrigée — Matrice croisée d'injection (secondaire, conditionnelle)

Cellule u(a, m) sur 7 × 7 Qwen2.5 ; contrôles : contenu inerte apparié, artefacts sans ajout ; seuil d'écart rapporté seulement si monotonie établie ; axe temporel seulement sur le panel daté de T1. Injections décrites par classe, jamais reproduites.

### T3 corrigée — Conscience d'évaluation et actions couvertes par unité de renforcement (hors pilote)

Échelle logit ; double variable (verbalisée, comportementale) ; erreur du classificateur estimée par point d'entraînement sur annotations indépendantes ; condition supervisée comparée, non contrôle.

### T4 — gelée

Pas d'estimand tant que les scores de 2412.04984 § 3.6 ne sont pas définis sur page primaire.

### Pilote corrigé (T1, axe de taille d'abord)

Qwen2.5 0,5–72 B en attaquants et moniteurs ; 500 problèmes APPS en deux banques (C4) ; partition C/F/V scellée ; C1–C3, C6, C7 inclus ; calcul de puissance par simulation publié avant lancement. Coût illustratif inchangé (ordre de 1 500 € loués, quatre à six semaines, la semaine supplémentaire pour C1–C3). **Non concluant si** : moins de quatre moniteurs fonctionnels et calibrés ; C1 ou C3 au-dessus du nominal ; horizons majoritairement censurés ou non monotones ; banc sans dents.

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi (par les pièces, aux statuts indiqués).** RAPPORTÉ : la performance de surveillance dépend du moniteur (AUC 0,92 à 0,96 pour o3-mini, 2506.05296 § 2.3) et le moniteur le plus fort peut être réduit à 0 sur 375 par injection (2510.09462, fig. 2) : l'instrument n'est ni fixe ni robuste. RAPPORTÉ : capacité et propension sont « difficiles à démêler », un outil retiré fait passer 59 % à 3 %, les taux de base sont à 0 % sauf un cas (2603.01608) : une propension datée serait une pente de montage. RAPPORTÉ : les recettes METR et TastEval donnent un axe continu et une logistique, mais leurs nombres de tâches, de modèles et l'incertitude du doublement sont absents des pièces. OBSERVÉ-NON-AUDITÉ : deux juges de langage au plafond (κ = 0) ; un seuil calibré sur 1 000 épisodes honnêtes tient (0,046–0,055) là où un seuil théorique unilatéral donne 0,21–0,35 de fausses alarmes ; des sondes génériques restent sous leur plancher aléatoire. Rien, dans aucune pièce, n'établit l'existence d'une **tendance datée** pour un comportement désaligné ou pour la surveillance.

**Ce qui n'est pas établi.** (1) Qu'un horizon de surveillance soit identifiable : il peut être censuré, non monotone ou instable (critiques D et E, acceptées). (2) Que l'axe de taille (Qwen2.5, une date) se convertisse en axe de temps : cela exige un panel multifamille daté que les pièces ne fournissent pas. (3) Que la pente contre un corpus gelé se transporte à d'autres corpus et aux attaquants contemporains (D2, C5). (4) Que la calibration globale tienne par tranche de longueur (C7). (5) Pour T3 et T4, l'estimand lui-même. Les chiffres « 9 à 15 mois » restent supposés.

**L'expérience à faire en premier.** Le pilote T1 sur l'axe de **taille** (Qwen2.5, 7 × 7, deux banques, partition scellée, C1–C3, C6, C7), avant tout panel daté. Raison : c'est la seule expérience qui, à coût de l'ordre de 1 500 € (illustratif), répond aux quatre questions qui conditionnent toute tendance — le banc a-t-il des dents (TPR < 0,95 pour au moins un moniteur), les horizons sont-ils identifiables (monotones, non censurés, intervalle < 1 octave), le seuil tient-il par longueur, et les contrôles d'étiquette factice et de style restent-ils au nominal. Chacune de ces quatre réponses peut être négative, et chaque négative tue une partie précise du plan sans que l'on ait dépensé le panel. Le duel joué est D1′ (θ₁′ ≥ 0,25 bit par doublement de taille, supposé, contre θ₁′ < 0,25) ; il ne dit rien du temps, et le dit. Si D1′ tranche pour H_A et que C1–C3, C7 tiennent, le panel daté (P-date, D1, D2) est lancé ; si C1 ou C3 dépassent le nominal, l'instrument mesure des artefacts et doit être refait avant toute pente.

**Ce qui ferait échouer le plan**, en trois lignes : pas de panel ouvert multifamille daté, donc jamais d'axe de temps ; horizons censurés au plafond pour tout moniteur récent contre le corpus gelé ; D2 pour H_B, qui réduit l'énoncé à « l'avantage relatif du moniteur décroît », vrai mais sans le facteur positif demandé.

FIN-DE-CELLULE
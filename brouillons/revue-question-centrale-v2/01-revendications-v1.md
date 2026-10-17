# Revue exhaustive de la question centrale — livrable 1 : revendications numérotées — v1

Écrit le 17 octobre 2026 vers 19 h 15 (UTC), **avant toute recherche** de la revue exhaustive, d'après le protocole scellé
`brouillons/revue-question-centrale-v1/protocole-revue-et-brainstorm-v1.md` (sha256 13893942…2a75, vérifié par `sha256sum -c`
le 17 octobre 2026 à 19 h 05 UTC), section 3.

Textes sources (lus tels quels) : `docs/programme-controle-ia-v2.md`, sections 3 à 5 ; `docs/decisions/decision-N-003-N-004-v1.md` ;
`decision-N-005-N-006-v1.md` ; `decision-N-007-N-008-v1.md` ; `decision-N-013-v1.md` ; `decision-P-008-v1.md`. Quand une décision
fixe la lecture d'une hypothèse, c'est l'énoncé de la décision qui est numéroté ; l'hypothèse du programme est indiquée entre
parenthèses. Chaque revendication est découpée en pièces (a, b, …) quand les décisions revendiquent des pièces séparées : une source
peut occuper une pièce sans occuper la revendication.

Échelle de classement (protocole, section 5) : **occupe** (même revendication, même cadre, résultat publié), **partiel** (une partie,
ou un cadre voisin), **voisin** (lié, sans recouvrement), **hors sujet**. « Non trouvé » veut dire « non trouvé dans les sources
lues », jamais « trou du champ » (R8).

## Papier A — le temps

- **R-A1 (H1, gain blanc sur noir).** À agrégation égale et à taux de faux positifs égal, un moniteur fondé sur les activations
  de l'agent détecte plus de **sabotage diffus sur tâches floues** qu'un moniteur boîte noire. Pièce revendiquée : la mesure
  spécifique « diffus et flou » ; le gain blanc sur noir en général est cité comme établi.
- **R-A2 (H2, énoncé N-007 ; cœur de la porte G1).** Sur des trajectoires où **chaque action sabotée reste sous le seuil d'un
  moniteur par action calibré à 1 % de faux positifs**, l'**accumulation additive toujours valide** (processus e, garantie
  uniforme sur l'horizon) de **scores de sondes lues sur l'agent qui agit**, contexte privé compris, détecte le sabotage avec un
  **rappel qui croît avec l'horizon** ; le seuil est calibré sur des **épisodes honnêtes entiers, sans aucun exemple de sabotage**.
  Pièces : (a) sous-seuil par action garanti ; (b) accumulation additive toujours valide ; (c) sondes de l'agent qui agit ;
  (d) rappel croissant avec l'horizon ; (e) calibrage sur épisodes honnêtes seuls ; (f) la conjonction.
- **R-A3 (critère G1, N-008 ; plan 2 × 2).** Comparaison qui isole le gain de l'accès interne de celui de l'accumulation : plan
  {boîte noire, boîte blanche} × {par action, séquentiel}, avec les bases accumulation additive sur scores boîte noire (type
  E-valuator), cascade de portes sur les mêmes sondes (type *Doomed from the Start*), sonde sur le dernier état, modèle temporel
  sur un observateur séparé (type TRACES), juge robustifié ; la boîte blanche séquentielle bat la meilleure base boîte noire
  (rappel à 1 % de faux positifs, intervalle de confiance à 95 %, épisodes appariés).
- **R-A4 (L, N-004 : lemme d'additivité, énoncé adverse).** Sur scores de sondes internes, l'attaquant répartit un budget total
  B sur agents, pas, calendrier, valeurs et positions, éventuellement de façon adaptative. Pièces : (a) **invariance terminale**
  exacte et trajectorielle (S_{n₀}(X) = S_{n₀}(Y) + B ; puissance fonction de (B, n₀, F₀, α) seulement, décroissante en n₀) ;
  (b) **invariance spatiale** pour une règle lue aux frontières de pas, y compris en lecture toujours valide ; (c) **séparation
  avec le max** (effondrement du max sous fragmentation, plancher au-dessus de α) ; (d) **non-compensation** posée comme condition
  empirique, et coût mesuré de la compensation par pilotage des activations.
- **R-A5 (L3 et validité, N-004).** Pièces : (a) en lecture toujours valide, **le calendrier compte** (avancer le sabotage aide
  le défenseur, le reporter aide l'attaquant), borne inférieure invariante P(E⁺_{n₀} ≥ 1/α) ; (b) **coût du report** et **prix
  de la garantie toujours valide** (Wald contre toujours valide) chiffrés ; (c) pour la sécurité « alarme avant que le dommage
  n'atteigne θ », le processus e cumulé ne suffit pas : il faut un **détecteur de rupture** (somme cumulée de Page, détecteurs e) ;
  (d) **validité sous dépendance** : le seuil de Ville n'est pas tenu sous effet épisode ; calibrage sur épisodes honnêtes entiers.
- **R-A6 (T, N-003 : théorème négatif par invariance).** Pièces : (a) **unification temps × agents** par sous-groupes de
  permutations de I ⊂ {1…N} × {1…T} ; (b) **distinction des classes C (multi-ensemble préservé) et K (marginales par coordonnée
  préservées, copule)**, avec ses conséquences de signe (somme et processus e au-dessus du taux sous dépendance positive, en
  dessous sous dépendance négative ; max à son taux ou en dessous, Slepian) ; (c) **T2, impossibilité sans structure** par
  rebrassage uniforme sur le groupe d'invariance de P₀ ; (d) **T3, garanties locales** (balayage, Page, co-élévation) face à un
  attaquant adaptatif, statistiques d'ordre globales neutralisables ; (e) **T4**, somme lue séquentiellement sous sommes partielles
  dominées. Non revendiqué : l'aveuglement élémentaire (T1) seul, la moitié négative seule, la dichotomie marginale/copule (Sklar).
- **R-A7 (hypothèse pivot ; transposition de L et T).** Sur des organismes de sabotage réalistes, le sabotage **déplace la
  marginale des scores de sondes** (δ > 0) ou passe par leur corrélation ; transposition des énoncés L et T aux **activations
  réelles** et leur mesure.
- **R-A8 (H6, énoncé N-013 : marge asymétrique).** Pour l'une au moins de quatre interventions non spécifiques (paraphrase,
  ré-échantillonnage, remise à zéro du contexte, bruit d'activations), il existe une intensité où, **en moyenne à intensité fixe**,
  le succès du sabotage d'agent chute significativement plus vite que l'utilité honnête. Non revendiqué : le bruit sur les poids.
- **R-A9 (Tr : transposition jeton → action).** La robustesse des agrégations max et attention des sondes, établie au niveau du
  jeton, tient-elle au niveau de l'action et de la trajectoire, sous accumulation séquentielle, face à un attaquant adaptatif ?
- **R-A10 (H8 : la validité prédit la robustesse).** Le construit réellement mesuré par une sonde (intention contre conscience
  d'évaluation), mesuré d'abord, **prédit sa robustesse adverse**. Non revendiqué : le glissement de construit sous pression.

## Papier C — l'instrument

- **R-C1 (HC1 a, N-005 et N-013 : destination libre).** Dans des **moniteurs de contrôle sous attaque**, la destination ĉ du
  verdict (Δv = g · (ĉ − v₀)) est **estimée librement**, puis testée contre la **cible de l'attaquant** v* et contre la **moyenne
  du corpus** (nul de retour à la moyenne), et comparée entre familles d'attaque.
- **R-C2 (HC1 b : loi de déférence par régression).** Gain g estimé **par régression sur plusieurs intensités par famille
  d'attaque** (flatterie et supplication, revendication d'autorité, approbations forgées, usurpation stylistique de l'instructeur,
  ordres en bande), dans des moniteurs de contrôle ; g > 0 pour les juges génératifs, structuré par famille. Non revendiqué : la
  lecture du verdict par la probabilité du jeton (instrument cité), la forme algébrique du « poids du conseil », le coefficient
  continu de déférence hors attaque, la hausse de note par technique de persuasion à intensité unique, le déplacement binaire de
  moniteurs de contrôle.
- **R-C3 (HC1 c : stabilité).** Stabilité **de rang** de g entre moniteurs, invariance à l'attaquant et au corpus.
- **R-C4 (HC1 d : opposition juge / sonde).** g des sondes qui lisent **l'agent auteur** du contenu contre g des juges qui lisent
  le contenu ; bras « sonde du lecteur » ajouté (N-013, section 8).
- **R-C5 (HC2 : robustesse des sondes).** Sous attaque par contenu en boîte noire, g_sonde ≈ 0 pour une sonde de l'agent auteur à
  agrégation robuste (max ou attention) ; jamais l'immunité absolue.
- **R-C6 (HC2b, renommée « trahison par les activations »).** Tenter de manipuler le moniteur **fait monter le score de sonde de
  l'agent qui manipule** ; propriété des sondes, contrôlée contre le style et contre le retour de bâton textuel.
- **R-C7 (HC3, pièce 1).** Sous le protocole « contenu = données », les **ordres en bande** insérés dans le contenu sont
  **détectés presque sûrement par des juges moniteurs**, y compris face à un attaquant adaptatif. Cité comme acquis : les ordres
  en bande déplacent les juges génératifs, y compris un moniteur de contrôle.
- **R-C8 (HC3, pièce 2).** L'**usurpation stylistique de l'instructeur, sans aucun ordre**, garde un **g résiduel positif sur
  des juges moniteurs** (loi continue, comme HC1) et un **g nul sur des sondes qui lisent l'agent auteur**.
- **R-C9 (HC4, N-013 : taxe de déplacement).** Obtenir sur une sonde qui lit l'agent le déplacement que la rhétorique obtient
  gratuitement sur un juge **exige un accès en écriture aux activations ou aux poids** : le contexte seul n'y suffit pas ; coût
  mesuré par axe (accès, requêtes, calcul, taux de succès) et par régime d'accès ; en contexte seul, écart « de plusieurs ordres de
  grandeur » à tester. Non revendiqué : le coût sous poids réglables.
- **R-C10 (HC5 a).** **Paraphrase de confiance** du contenu avant lecture par le juge, comme contre-mesure à la corruption
  rhétorique d'un moniteur.
- **R-C11 (HC5 b).** **Quorum hétérogène en type d'accès** : juges génératifs **et sondes qui lisent l'agent**. Non revendiqué : le
  quorum entre familles de juges.
- **R-C12 (HC5 c).** **Matrice de transfert des attaques de corruption entre juges et sondes**, qui mesure l'efficacité du quorum.
  Non revendiqué : la matrice entre sondes seulement, le transfert entre juges seulement.
- **R-C13 (HC6 : critère de recette).** Le **g mesuré sur des corpus de pression bénins prédit l'effondrement sous attaque
  optimisée** : test d'acceptation d'un moniteur avant déploiement.

## Papier B — l'essaim

- **R-B1 (H3 : courbe sécurité(N)).** À **budget de sabotage total constant**, la courbe de sécurité en fonction du nombre N
  d'agents de la boîte blanche **domine** celle de la boîte noire et **décroît plus doucement** avec N. Cité : les courbes boîte
  noire et l'effet de fragmentation.
- **R-B2 (statistique de population).** Des copies à poids partagés ont des signatures internes qui co-varient : une **statistique
  spatio-temporelle ou de co-élévation** sur les scores de sondes des copies rend l'essaim plus détectable que l'agent isolé et
  bat l'agrégation par agent (porte G2).
- **R-B3 (H4′ : compromis diversification / coordination).** Diversifier les agents (personas, réglages fins) **décorrèle leurs
  signatures internes mais réduit leur capacité de coordination** ; le compromis est chiffrable.
- **R-B4 (H5, N-013 : nombre × diversité des moniteurs).** La **loi** : la sécurité croît avec le nombre M de moniteurs
  **seulement par la diversité effective**, mesurée par une matrice de transfert d'attaque sur un panel de sondes. Cité :
  l'instrument (matrice entre trois sondes).
- **R-B5 (H7, N-013 : riposte et fuite).** La **pente d'adaptation de l'équipe rouge** est **prédite par l'information mutuelle**
  entre l'état de détection et ses observations ; **comparaison des politiques de riposte** (quatre politiques, deux ablations).
  Cité : le verdict comme canal de fuite, la dépendance causale de l'attaque aux verdicts.

## Rappel : cité comme acquis ou retiré (ne compte pas comme revendication)

Lecture du verdict par la probabilité du jeton ; poids du conseil (psychologie du jugement) ; Pander Score (2606.07897 v2) ;
2508.07805 ; 2607.08066 ; injections contre moniteurs (2510.09462) ; rhétorique contre moniteurs (2505.23575) ; ordres en bande
contre moniteurs (2508.19461) ; quorum entre familles de juges (2607.08066, 2605.15377) ; matrice entre trois sondes et évasion
sous poids réglables (2609.36490) ; bruit sur les poids pour la sous-performance (2412.01784) ; « self-incrimination » au sens de
2602.22303 ; lecture de sondes multi-tours avec garantie de rappel (2607.06503) ; E-valuator (2512.03109) ; moitié négative de T
(2607.11751) ; dichotomie marginale / copule ; effet de fragmentation boîte noire (2607.07368) ; glissement de construit
(2605.27958). Ces sources restent dans le tableau quand elles touchent une pièce revendiquée.

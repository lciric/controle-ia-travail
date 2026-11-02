# Proposition A — Tour III.2 : critique croisée de méthode

Pièces absentes déjà déclarées (pilote complet, `resultats` du calibrage, PDF de Bailey) : rien reconstruit. Trois faits du code que je réutilise partout, VÉRIFIÉS sur la pièce 3 : (i) `plafond_cpu_tache_s = 600` arrête toute tâche plus longue ; (ii) `n_attaque_entr = 2001` est partagé entre les T + 1 lois d'entraînement (`Contexte.entrainer`), donc l'oracle du défenseur reçoit ≈ 2001/(T+1) points par loi ; (iii) `poids_max_min_equilibres` déclare la pureté « forcée » avec `tol = 1e-9` sur une matrice G dont chaque cellule est un taux estimé sur 19 998 points (erreur-type ≈ 0,0035, illustratif). Les chiffres du pilote sont RAPPORTÉS ; mes seuils sont illustratifs.

## Sur la proposition B

**(a) Défauts de méthode.**

1. *Exp. 1, « attaquant exhaustif ».* La boîte a K·d·2 = 36 coordonnées (VÉRIFIÉ, `bornes`). Une grille de 10⁴ à 10⁵ points y met ≈ 1,3 point par axe (illustratif) : ce n'est pas exhaustif, c'est un attaquant plus faible que SLSQP. H_B (« le cycle disparaît ») est alors confondue avec « l'attaquant n'optimise plus ». Pire, le résultat est vrai par construction : sur un support fini et fixe, l'attaquant répète des points ; un déplacement identique à un déplacement passé donne cosinus 1 (I3 monte), et une répétition du point t − 1 donne une égalité stricte comptée comme non-retour (`max(cs[:-1]) > cs[-1]`, VÉRIFIÉ). I3 devient une fonction du cardinal de la grille. Enfin, 600 s par tâche annoncées = le plafond : `GardeArret`.
2. *Exp. 2.* La formule de NashConv (max_q − min_q + …, « symétrisé ») n'est pas une exploitabilité définie. Fuite d'instrument : NashConv est estimé avec les oracles locaux dont on teste la convergence ; le sup est sous-estimé, l'inf surestimé, l'estimateur est une borne basse ; « NashConv < 0,05 » est atteignable par simple faiblesse de l'oracle. Le contrôle « Matching Pennies avec la même bibliothèque » est impossible : SLSQP sur paramètres continus ne joue pas un jeu 2 × 2.
3. *Exp. 3.* « Valeur restreinte − V » n'est pas l'exploitabilité : V = min de deux évaluations fraîches (biais de sélection déclaré au code, VÉRIFIÉ), donc l'écart est strictement positif même à convergence parfaite. Confondant T ↔ oracle : à T = 64, ≈ 31 points par loi d'entraînement (fait (ii)) ; la dégradation de l'oracle imite une non-convergence.
4. *Exp. 4.* Pour m = 1, `objectif_detection` standardise le score par l'écart-type propre : invariant par changement d'échelle de w (VÉRIFIÉ) ; la pénalité λ‖w_t − w_{t−1}‖² ne l'est pas. λ grand fige le moniteur ; une défense figée a des déplacements quasi identiques, donc des égalités, donc I3 → 0 et non ≈ 0,73 : « I3 − nul ∈ [−0,05 ; 0,05] » ne distingue pas amortissement, gel partiel et bruit. Le critère « sans perte » V(A_reg) ≥ V(A) − 0,01 au δ 1,6, où V(A) = 0,036 (RAPPORTÉ) et le plancher est α = 0,01, est à l'échelle du bruit. Le « contrôle λ = 0 reproduit A au bit » est vrai par construction : il ne contrôle rien.
5. *Exp. 5.* Confond T avec le rapport unités/attaques : à T = 32, B′ garde 9 unités et D en reçoit 33 (`m_unites = t + 1`, VÉRIFIÉ) : la comparaison n'est plus à classe égale.
6. *Synthèse « géométrie orthogonale »* : HYPOTHÈSE présentée comme mécanisme ; le fait que le moniteur dominant de B′ vienne des tours 2 à 4 (RAPPORTÉ) ne la confirme pas.

**(b) Conditions de perte de puissance.**

- I3 − 0,7345 : la valeur nulle est dérivée pour des déplacements échangeables sans atome (simulée sur gaussiennes, M4 § 9). Elle tombe si la loi des déplacements a des atomes (support fini ; coordonnées projetées sur les bornes ±5, 0,5, 1,5), ou si la suite est stationnaire mais dépendante : une autocorrélation de rang 1 négative des cosinus (ρ₁ < 0, répulsion) élève E[I3] sans aucune périodicité.
- NashConv estimé : si la probabilité que l'oracle local atteigne le sup à ε près est < 1, le biais est non borné ; l'issue « convergence » est non jugeable.
- Exp. 3 : si l'erreur-type par cellule de G (≈ 0,0035) dépasse la décroissance attendue entre deux T, la pente est indétectable ; l'effectif par loi 2001/(T+1) fait croître la variance de l'oracle avec T.
- Exp. 4 : au δ où V(A) − α est de l'ordre de l'erreur-type (0,011 au calibrage à 1,6, RAPPORTÉ), « sans perte » est non jugeable.

**(c) Contrôles négatifs dont l'absence est fatale.**

- Exp. 1 : valeur nulle de I3 recalculée pour un tirage iid sur la même grille.
- Exp. 2 : bras « attaquant iid sans mémoire » pour borner NashConv par la faiblesse de l'oracle ; et la meilleure réponse exacte en population pour m = 1 (le taux de détection d'un hyperplan sur un mélange gaussien est une moyenne de queues gaussiennes, calculable sans échantillon) pour mesurer le biais de l'oracle.
- Exp. 4 : bras figé M0 à tous les tours comme borne de « convergence triviale ».
- Exp. 5 : D à 9 unités constantes.

## Sur la proposition C

**(a) Défauts de méthode.**

1. *Exp. 1.* Les deux issues ne couvrent pas l'espace : D_train ∈ [0,20 ; 0,25[ ou gain ∈ [0,02 ; 0,05[ ne falsifient rien (B4). D_train(A) bas est compatible avec H_A (saturation géométrique) **et** avec le mécanisme 3 de C lui-même (L-BFGS-B sous-optimal) : le confondant n'est pas séparé. Dans A_JF-bilatéral, les attaques d'entraînement de w_T sont des réponses à des mélanges, donc une distribution plus facile : V(A_JF) − V(A) confond règle de l'attaquant et distribution d'entraînement.
2. *Exp. 2.* Le contrôle est juste : sur une tâche pure, le « ou » d'un seul moniteur est une transformée affine du score, le seuil au quantile 1 − α est identique, et `objectif_lisse` dépend de (s − t)/e, invariant (VÉRIFIÉ) : V égal au bit. Mais cela signifie que 17/24 et 14/24 tâches (RAPPORTÉ) contribuent exactement 0 à l'écart apparié : la moyenne est diluée par construction. Les erreurs-types sur mélange réel (0,0084 et 0,0026 pour B′ − D, RAPPORTÉ) montrent qu'une borne basse > 0,02 n'est pas atteignable au δ 1,4 avec 7 tâches.
3. *Exp. 3.* Passer D à m = 2 à tous les tours supprime sa trajectoire de capacité croissante : D₂ est un autre bras, la continuité avec le pilote est rompue (à déclarer). L'argument « Carathéodory » est une HYPOTHÈSE : la région d'alerte d'un maxout à 2 unités est l'union de deux demi-espaces, et la domination d'une ligne de G dépend de la géométrie des attaques, pas d'un comptage d'unités. L'explication « une unité par attaque » est contredite en partie par l'indice du moniteur dominant (tours 2 à 4, entraîné contre 3 à 5 attaques, RAPPORTÉ).
4. *Instrument 2 (pureté forcée).* C identifie bien le défaut du sommet HiGHS, mais son cas (b) utilise des lignes identiques exactes. Sur G estimé, deux moniteurs identiques évalués sur des graines distinctes diffèrent de ≈ 0,004 (illustratif) ≫ 10⁻⁹ (fait (iii)) : le LP déclare « forcée ». Le « 0 % de fausses alertes » serait vrai par construction sur matrices exactes et faux sur matrices estimées.
5. *Jouet, ligne 5.* Sur actions pures répétées, cosinus 1 et égalités : la valeur nulle d'un jeu fini n'est pas 0,7345 (atomes) ; « I3 − 0,7345 > +0,15 » n'est pas calibré.
6. *Références.* Korpelevich 1976 sans titre (règle 3) ; Brown 1951 avec recueil : à vérifier. Le mécanisme (g) « Logit-B » est un instrument nouveau sans contrôle.
7. *Instrument 4.* « Invites cibles contournant la sonde précédente » frôle l'interdit de la question ; « min H[T,t] ≥ 0,50 » est arbitraire.

**(b) Conditions de perte de puissance.**

- Exp. 1 : non jugeable tant que la loi de la différence « réponse exacte − réponse L-BFGS-B » n'est pas identifiée ; D_train(A) est alors un mélange des deux.
- Exp. 2 : puissance ∝ n_mix/N ; si P(pur) → 1, l'écart apparié → 0 par construction.
- Pureté forcée : il faut tol ≥ k·σ_G, σ_G = √(G(1 − G)/n_eval) ; à tol = 10⁻⁹, « forcée » est déclaré dès que la ligne dominante gagne d'un écart > 0 sur chaque colonne, événement de probabilité 1 sous bruit continu même quand deux lignes sont égales en population.
- Jouet : sous iid sur un support de cardinal k, E[I3] dépend de k et T.

**(c) Contrôles négatifs dont l'absence est fatale.**

- Exp. 1 : la meilleure réponse exacte en population pour m = 1 sur les attaques mêmes de A ; sans elle, géométrie et oracle restent confondus.
- Pureté : duplication d'un moniteur évaluée sur graines distinctes.
- Exp. 3 : B′₁ = B et D₁ = A au bit (proposé, bon) ; manque D₉ (9 unités constantes) qui isole « capacité croissante » de « classe ».
- Jouet : simulation de la valeur nulle sur le support fini.

## Sur la proposition D

**(a) Défauts de méthode.**

1. *E1 (mixture des moniteurs mêmes de A).* Je m'en sers : c'est le témoin manquant du pilote. Défaut : l'équilibre restreint est calculé sur des colonnes qui sont des réponses à des moniteurs seuls, jamais au mélange ; la valeur restreinte surestime (+0,019/+0,024 pour B, RAPPORTÉ). Au δ 1,6, un gain ≥ 0,02 contre V(A) = 0,036 est accessible à presque toute mixture (C1 − A ≈ +0,11 sur les moniteurs de B, RAPPORTÉ) : H_A y est peu informative.
2. *E2 factoriel.* « Meilleure réponse exacte dans une version tabulaire du jeu restreint » : si le défenseur choisit parmi les moniteurs existants, il n'entraîne plus ; la cellule « exact » change le jeu (bibliothèque close), pas seulement la précision. Les quatre cellules ont des trajectoires d'attaques différentes : comparer I3 entre cellules compare des historiques différents.
3. *E3.* ε et η « gelés » mais non chiffrés ; la règle canonique (entropie maximale à valeur conservée) remplace le sommet HiGHS, donc change V(B′) : rupture avec le pilote, à déclarer. Le transfert de la posabilité des « tâches de conception » aux tâches de décision est une HYPOTHÈSE (D le circonscrit à « cette famille », correct).
4. *Mécanisme (a)* : « si aucune pondération ne bat A, l'explication tombe » est à sens unique : l'absence d'effet d'une pondération ne réfute pas la cause.
5. *Mécanisme (e)* : « V augmente mais NashConv ne diminue pas » : NashConv restreint et V sont liés algébriquement (gap = valeur restreinte − V) ; ils ne sont pas indépendants.
6. *Distance fonctionnelle sur banque commune* : si la banque est tirée du propre seulement, deux moniteurs calibrés au même α peuvent y coïncider et différer sur les attaques ; distance ≈ 0 par construction. La banque doit contenir des attaques tenues.

**(b) Conditions de perte de puissance.**

- Exploitabilité restreinte : estimateur = sup local − inf local ≤ vraie valeur ; une « décroissance » peut venir d'un oracle qui cesse de trouver (départs passés attirant vers un même bassin) ; non jugeable sans attaquant indépendant.
- E1 à N = 24 : la taille mesurée de « moyenne ≥ S1 et borne basse > 0 » sous effet = 0,02 est 0,50 à N = 100 (RAPPORTÉ, M4 § 3a) ; à N = 24 elle est nettement plus basse (illustratif) : un effet de 0,02 est non tranché par construction.
- E3 : P(déclarer intérieur | vrai pur) dépend de ε/σ_G ; si ε < 2σ_G, le bruit seul suffit.

**(c) Contrôles négatifs dont l'absence est fatale.**

- Distance fonctionnelle : deux moniteurs différant par un facteur d'échelle (distance nulle attendue).
- E1 : une itération de double oracle depuis les moniteurs de A (colonne « réponse au mélange ») pour borner la surestimation restreinte.
- E2 : la cellule « attaquant historique × défenseur actuel » doit reproduire la convergence du jeu fictif bilatéral exact de E0 ; sinon l'interaction n'est pas lisible.
- E3 : matrice dupliquée bruitée (graines distinctes).

## Sur la proposition E

**(a) Défauts de méthode.**

1. *Gap g.* E établit que l'estimateur local donne ĝ ≤ g. Alors l'issue « ĝ ≤ 0,02 » ne falsifie pas H_A ; seule « ĝ > 0,02 » est informative. Le duel « mesure ou dynamique ? » sur le monde synthétique est asymétrique (B4), ce que la « règle commune de décision » symétrique masque.
2. *« Bibliothèque incomplète ».* Fuite : si la même batterie adverse indépendante sert à chercher l'extension (budget de recherche) et à évaluer son gain, le gain est biaisé vers le haut. Deux batteries sont nécessaires. Le contrôle « copies exactes » est bon et comble le fait (iii), à condition d'évaluer les copies sur des graines distinctes.
3. *v_mix − v_pur.* Sur G construite par double oracle tronqué, aucune colonne n'a répondu au mélange : v_mix est surestimé par construction ; les faits donnent valeur restreinte − V = +0,019/+0,024 pour B (RAPPORTÉ). Un seuil de 0,02 est de l'ordre de ce biais : non interprétable sans la colonne « réponse au mélange p* ».
4. *Jouet.* Avec la règle de A sur pile ou face, le dernier profil est toujours pur, donc toujours exploitable de la même quantité : le jouet ne distingue pas « cycle » de « tout profil pur hors équilibre » ; il valide le calculateur de gap, pas la lecture dynamique. 10 000 itérations sans bruit sur un 2 × 2 : sans objet (déclaré illustratif).
5. *Tableau des mécanismes.* Z = réduction du gap opérationnel : une intervention qui rend l'oracle local moins efficace (régularisation qui aplatit les bassins) réduit ĝ sans réduire g — vrai par construction possible ; la garde « détection récente » ne l'exclut pas.
6. *Désaccord fonctionnel* : même défaut que D ; sur banque propre, désaccord ≤ 2α par construction.
7. Le point « la cible figure dans l'historique de A avec poids 1/(t+1) » (VÉRIFIÉ, `attaques = [ctx.cible]`) manque aux autres ; je m'en sers. La séparation causale « banque gelée puis boucle rouverte » est le bon dessin ; je m'en sers.

**(b) Conditions de perte de puissance.**

- ĝ : si U(w, θ) a en w des maxima locaux séparés par des vallées que les 8 départs (`departs_entr`) ne franchissent pas, P(sup local = sup) < 1 et l'issue H_B est non jugeable.
- v_mix − v_pur : max sur ≤ 9 lignes et min sur 9 colonnes d'estimateurs à σ_G ≈ 0,0035 : biais d'extremum positif ; sous pureté vraie, P(v̂_mix − v̂_pur > 0,02) n'est pas nulle et E ne la chiffre pas.
- Désaccord fonctionnel : si la banque suit N(0, I), espérance ≤ 2α.
- Détection robuste : plancher α ; quand V − α est de l'ordre de l'erreur-type, « réduction > 0,02 » est non jugeable.

**(c) Contrôles négatifs dont l'absence est fatale.**

- Attaquant indépendant de type S17 sur chaque défense de chaque intervention ; sans lui, ĝ n'est pas interprétable.
- Deux batteries (recherche, évaluation) pour « bibliothèque incomplète ».
- Colonne « réponse au mélange » et matrice dupliquée bruitée avant v_mix − v_pur.
- Bras figé M0 comme borne de convergence triviale (D l'a explicitement ; E seulement en creux).

## Point commun que je retiens contre les quatre

Toute lecture de I3 sur la trajectoire utilise les attaques du tour, calculées avec 4 départs et 256 points de Monte-Carlo (VÉRIFIÉ `departs`, `n_mc`), contre 48 et 512 en finale. L'audit `auditer_tours_A` part de l'attaque du tour et en reste proche (RAPPORTÉ, S17 : I3 inchangé sur 10 tâches) : il ne contrôle pas la forme. Aucune proposition n'ajoute le contrôle le moins cher : rejouer la trajectoire de A avec l'attaquant renforcé **sans** l'attaque du tour comme départ. Sans lui, « retours au-delà du hasard » reste OBSERVÉ-NON-AUDITÉ quel que soit le mécanisme qu'on lui oppose.

FIN-DE-CELLULE
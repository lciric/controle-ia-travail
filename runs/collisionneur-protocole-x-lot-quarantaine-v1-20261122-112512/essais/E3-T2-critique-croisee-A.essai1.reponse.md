# Proposition A — Tour III.2 : critique croisée de méthode

## 0. État des pièces et arguments réutilisés

- Les pièces B à F sont présentes et se terminent par leur marqueur ; je ne peux pas recalculer les empreintes. Ma propre conception du tour III.1 ne m'est pas retransmise : je ne m'y réfère pas. Les notes du bloc FAITS sont annoncées retirées et aucun fait n'y porte de statut.
- Tout ce qui suit est une analyse de statut HYPOTHÈSE. Tout chiffre est illustratif ; « calculé » signale une arithmétique refaisable.

Trois arguments servent plusieurs fois. Je les pose ici et les applique nommément plus bas.

- **A1, déterminisme.** HYPOTHÈSE sur l'agent : c'est un transformeur sans mémoire hors contexte, et le lecteur de texte reçoit tout le contexte X. Alors Z_int = f_θ(X), donc I(Y ; Z_int | X) = 0 par construction. L'affirmation (ii) n'est testable que relativement à une classe bornée de lecteurs de texte. Un gain mesuré a deux causes : (1) un contexte que le lecteur de texte ne voit pas (invite système, raisonnement non affiché, consigne d'induction de la dégradation) ; (2) un déficit de calcul du lecteur. Le contrôle qui les sépare : faire relire aux mêmes poids le texte exact donné au lecteur, d'où Z′, puis comparer le gain de Z à celui de Z′.
- **A2, plancher.** Un témoin d'AUROC ≈ 0,5 satisfait |Δ_témoin| ≤ ε entre deux lots quelconques. Il ne certifie aucune équivalence.
- **A3, troncature.** Si un résultat n'est rapporté que lorsque θ̂ ≥ c, alors E[θ̂ | θ̂ ≥ c] > θ dès que Var(θ̂) > 0, même avec une lecture unique.

## Sur la proposition B

**(a) Défauts de méthode**

1. **E1, signe acquis d'avance.** Sous arrêt optionnel sur un score bruité, E[Δ] > 0 dès que Var(score) > 0 et K > 1. Seule la marge informe, et elle dépend de n(G′-consulté) et de K, choisis par l'expérimentateur. Une issue « Δ dans la marge » sur boucle scriptée et genre substitut ne se transporte ni aux auteurs humains ni au lot réel. La clause de réfutation n° 1 de B conclut trop.
2. **R1′, tendance commune et fuite.**
   - Les points de contrôle sont successifs. Deux scores qui croissent avec l'indice de cycle donnent un Spearman positif sans que le critère prédise quoi que ce soit. B place « nombre de cycles » en rival à battre, non en variable à partialiser.
   - Si l'audit rend ρ ≈ 0, l'équipe révise son critère. Les détecteurs suivants sont alors conditionnés au lot, qui entre dans le critère de passage malgré la position 1 de B.
3. **E2, trois confusions.**
   - Les seuils sont calibrés sur les honnêtes de développement. « À fausses alertes égales » ne vaut que là ; le McNemar sur les seuls dégradés ne voit pas un écart de taux réalisé entre T et T+I sur le lot.
   - La sonde couche 0 est un sac de jetons. Elle ne ferme pas la cause (2) de A1.
   - Les jumelles bifurquent d'un même état. Si la dégradation est induite par une consigne en contexte, l'état interne lit la consigne, et (ii) est vrai par construction quand T ne la voit pas.
4. **E4, hypothèses non exhaustives.**
   - H_A est une conjonction (excès, et excès plus grand pour l'interne) ; H_B dit « aucun excès ». Un excès symétrique ne tombe dans aucune : B4 n'est pas respecté.
   - L'ajustement de difficulté par vérification mécanique tombe sous A2, puisque la dégradation est « discrète ».
   - « Falsifie H_A, on garde l'ensemble entier » traite un non-rejet comme une équivalence.
5. **E3.** Le contrôle en distribution ne calibre pas une bande hors-genre. Tous les détecteurs, évalués sur le même lot, se déplacent ensemble.
6. **Séparabilité du genre.** Elle exige de lire les entrées du lot avant gel, consultation non comptée dans « une seule fois ».

**(b) Conditions de non-jugeabilité**

- **E2, McNemar exact.** Avec m paires discordantes, p bilatéral ≥ 2·0,5^m. Aucun rejet à 0,05 n'est possible si m < 6 (calculé). La condition est n_dég·π_d ≳ 6, où π_d est le taux de discordance hors-genre.
- **E2, seuil.** Avec n_h honnêtes et un taux visé α, le taux réalisé a un coefficient de variation ≈ 1/√(α·n_h), soit ≈ 58 % pour α = 0,01 et n_h = 300 (calculé).
- **R1′.** Pour K = 10 points, le |ρ| critique à 0,05 est ≈ 0,65. L'autocorrélation réduit encore le K effectif.
- **E3.** Avec G = 1 genre, la variance inter-genres τ² n'est pas identifiable. Si la corrélation des résidus entre détecteurs tend vers 1, le nombre effectif de points tend vers 1.
- **E5.** La puissance dépend de π_d sur le lot. L'estimation prise sur développement la surestime si π_d(lot) < π_d(dev).

**(c) Contrôles négatifs dont l'absence serait fatale**

- La relecture par les mêmes poids (A1).
- Le taux de fausses alertes réalisé sur honnêtes du lot, pour T et pour T+I.
- Une permutation de l'ordre des cycles pour R1′.
- Un contrôle positif du témoin de difficulté (A2).

## Sur la proposition C

**(a) Défauts de méthode**

1. **Statuts.**
   - C marque `[VÉRIFIÉ]` l'intégrité des blocs sans pouvoir recalculer l'empreinte.
   - C attribue `[OBSERVÉ-NON-AUDITÉ]` à l'étanchéité, alors que les faits ne portent aucun statut.
   - C étiquette `[RAPPORTÉ]` le conditionnel de la question 3, qui est une éventualité et non un fait.
   - « Deux conditions indépendantes » : elles sont calculées sur le même échantillon et les mêmes détecteurs.
2. **Expérience 1.** Elle fait tourner la boucle sur la moitié du lot réel. Le genre étant unique, Q_portée n'est plus hors-genre pour les détecteurs produits. Les écarts en valeur absolue n'ont pas de référence par partitions aléatoires.
3. **Expérience 2.**
   - Une seule campagne par régime : le régime est confondu avec l'équipe.
   - Contrôle par bruit : avec d = 2 048 > n = 1 000, tout étiquetage est linéairement séparable en échantillon. Le « gain apparent » est algébrique et ne dit rien du régime.
   - L'issue attendue « 0,00 ± 0,01 bit » est écrite à l'indicatif ; c'est une hypothèse.
4. **Expérience 3.**
   - La double différence suppose des tendances parallèles. Or une amélioration légitime peut être spécifique au genre, et Q_neuf est produit plus tard.
   - Le TOST est inversé : son rejet établit l'équivalence, non la contamination.
   - Les canaris devaient être posés à la création, alors que le lot est déjà constitué. Ils détectent un apprentissage sur exemples, pas la lecture humaine d'un genre.
   - L'antériorité la plus proche des canaris me semble être Carlini, Liu, Erlingsson, Kos, Song (2019), « The Secret Sharer » (de mémoire, à vérifier), plutôt que la référence de 2021 citée par C.
5. **Expérience 4.**
   - Recalibrer sur le lot change la grandeur estimée (détecteur recalibré, non détecteur gelé).
   - Cela peut effacer par construction un écart à la loi si celle-ci porte sur des taux.
   - C'est une lecture d'étiquettes, non comptée dans « une seule fois ».
6. **Témoin markovien.** Sous A1, vider le cache puis réinjecter la transcription ne change rien : le témoin est l'agent. La règle de C (« tout gain vient de la sous-optimalité du texte ») s'applique alors au résultat principal. Si un contexte caché existe, le témoin change le comportement de l'agent et la loi des trajectoires.
7. **Sélection.**
   - Les paires « aveugles pour le texte » sont choisies sur D_texte dans l'échantillon d'évaluation. D_texte y est au plancher par sélection, et tout score à bruit indépendant le bat.
   - Filtrer pour que les vérifications mécaniques aient une AUROC entre 0,45 et 0,55 rend « battre ces vérifications » vrai par construction.

**(b) Conditions de non-jugeabilité**

- **Î(Y ; Z | T).** Le biais positif de l'estimateur croît avec d/n. Le seuil de 0,03 bit n'est jugeable que si ce biais, estimé sous permutation, lui est très inférieur.
- **η.** C'est un rapport dont le dénominateur ΔS(P_Nouveau) tend vers 0 sous l'hypothèse de redondance. Sa loi a des queues lourdes et sa variance n'est pas bornée.
- **Taux de faux rejets sur 100 simulations.** L'erreur-type vaut ≈ 0,022 à 0,05 (calculé). Dans la zone ]0,05 ; 0,10], aucune hypothèse n'est falsifiée.
- **Double différence.** Si L(M_avant, Q_vu) est proche du plafond, la différence est bornée et le test perd sa puissance.
- **Kolmogorov-Smirnov.** La loi nulle n'est valide que pour une loi continue entièrement spécifiée, sans paramètre ajusté sur l'échantillon.
- **Canaris.** La puissance vaut P(mémorisation | exposition humaine), a priori proche de α.

**(c) Contrôles négatifs dont l'absence serait fatale**

- Une référence par partitions aléatoires (expérience 1).
- Une double différence placebo entre deux versions antérieures à l'exposition (expérience 3).
- Une sélection des paires sur un pli disjoint de l'évaluation.
- Une recalibration sous étiquettes permutées (expérience 4).

## Sur la proposition D

**(a) Défauts de méthode**

1. **Référence.** D écrit « Noam Cawley ». De mémoire, l'auteur est Gavin C. Cawley, avec Nicola L. C. Talbot (2010), même titre ; à vérifier. Telle qu'écrite, l'attribution ne satisfait pas la règle 3. D applique aussi `RAPPORTÉ` à une absence (« ne sont pas fournis »).
2. **Double usage.** « Échec = pas de passage » supprime la re-présentation, pas la troncature (A3). La portée publiée est conditionnelle au passage, donc biaisée vers le haut.
3. **Test de passage sous nul global.** Si le critère exige un niveau élevé, q ≈ 0 quand les alertes n'informent pas : H_A est acquise sans effort. Le nul pertinent est la configuration la moins favorable, performance vraie juste sous le seuil. D reconnaît la limite sans construire ce nul.
4. **Duel d'exposition.** La randomisation porte sur les familles, mais si elles partagent un genre, la révélation des unes informe sur les autres. E est alors biaisé vers 0 et H_A favorisée. Le duel mesure la fuite d'instance au-delà de la fuite de genre, non la fuite totale.
5. **Contrôle de valeur ajoutée.** Échanger les états dans une strate (tâche × avancement) casse aussi la dépendance Z–T. Le contrôle teste Y ⟂ Z | strate, non Y ⟂ Z | T, et laisse ouverte la cause (2) de A1.
6. **Loi.** Les taux d'alerte dépendent du seuil de l'instrument : un écart D confond loi et détecteur. La correspondance préfixée réduit ce risque sans l'éliminer.
7. **Banc.** Tables, 4 000 jetons, modèle 7B : la population diffère de « longues tâches » et rien n'indique qu'elle soit dans le domaine de la loi. Le banc est en outre choisi pour qu'un invariant existe.
8. **Campagnes randomisées.** L'unité est la campagne. Les mêmes auteurs apprennent d'une campagne à l'autre, et l'effet de report n'est pas contrôlé.

**(b) Conditions de non-jugeabilité**

- **Unité famille.** La précision est gouvernée par G familles et la corrélation intra-famille. Si G est petit, l'intervalle chevauche la frontière et, selon la convention même de D, rien n'est tranché.
- **Écart D à la loi.** Sous accord exact, E|p̂_j − p_j| ≈ √(2/π)·√(p_j(1−p_j)/n_j). Si δ_L est inférieur à Σ_j w_j fois ce plancher, H_A est rejetée par construction.
- **« Au moins une alerte ».** Le taux par trajectoire vaut 1 − Π_t(1 − α_t), croissant avec le nombre de points de décision L. Si la loi de L diffère entre développement et lot, le plafond n'est pas respecté et D s'interdit alors toute revendication.
- **Passage.** La probabilité de faux passage n'est pas identifiable sans la loi de la stratégie d'adaptation ; elle est seulement bornée pour la stratégie simulée.

**(c) Contrôles négatifs dont l'absence serait fatale**

- Un nul en configuration la moins favorable pour le passage.
- Un bras de familles d'un genre disjoint dans le duel d'exposition, pour mesurer la diffusion.
- La relecture par les mêmes poids (A1).

## Sur la proposition E

Je me sers du présupposé 1 de E : si le lot, constitué avant le changement d'affirmation, n'archive ni états ni moyen de rejeu, aucun test de (ii) n'est exécutable. C'est la première condition de non-jugeabilité pour les duels de (ii) de B, C, D et F.

**(a) Défauts de méthode**

1. **Statuts.**
   - E emploie trois fois `[VÉRIFIÉ]` sans que cela vienne des faits : pour la pièce, pour l'espérance d'AUROC, pour l'inégalité de traitement.
   - Une valeur est marquée à la fois « (illustratif) » et `[VÉRIFIÉ]`.
   - « OBSERVÉ-NON-AUDITÉ (érigée en HYPOTHÈSE) » est un changement de statut explicite, contraire à la règle 1.
   - Le contrôle de E6 garde un résidu de rédaction (« ? Non : »).
2. **E2 et E3 sont écrits sur E_quar lui-même** (scinder les 400 paires ; révéler 20 paires). Si c'est le lot réel, l'expérience détruit son objet. Si c'est un substitut, la pièce ne le dit pas.
3. **E2.**
   - H_2B affirme que l'apprentissage se transfère à l'intérieur d'un genre, ce qui définit un genre. L'issue est quasi acquise dès que l'apprentissage fonctionne.
   - Le jeton planté dans P_1 et P_4, absent de G_externe, gonfle Δ_parties-unique par construction. C'est un contrôle positif présenté comme négatif.
4. **E1 et E4.**
   - H_1B et H_4B sont des conjonctions (« ce bras gonfle et l'autre tient »). Si les deux bras gonflent, aucune hypothèse n'est vraie : B4 n'est pas respecté.
   - En E4, sous A1, le bras symétrique peut gonfler aussi, puisque Z apporte du calcul déjà fait.
   - L'issue du bras asymétrique est fixée par le degré de faiblesse donné à D_txt (2 cycles contre 15), paramètre de l'expérimentateur.
   - « FDR » sous nul global désigne un taux d'erreur de type I.
5. **Contrôle miroir.** Z_miroir vient d'un autre modèle, plus petit. Un avantage de Z_int confond « état propre à l'agent » et capacité du lecteur. L'inégalité invoquée s'applique aussi à Z_int sous A1 : l'argument prouve trop.
6. **E5.** Avec 5 paliers et aucun paramètre libre, χ²_réd = 2,5 correspond à p ≈ 0,03 ; p < 0,01 demande χ²_réd ≈ 3,0 (calculé). Les deux seuils ne désignent pas la même région. Le contrôle suppose en outre des données publiques de la loi, non établies.
7. **E3.** Une équipe par condition. Le bootstrap sur 380 paires ne couvre pas la variabilité entre auteurs.
8. **Audit lexical.** Il exige de lire les n-grammes du lot avant gel et ne voit pas une compréhension du genre qui ne recopie aucun n-gramme.

**(b) Conditions de non-jugeabilité**

- **E6.** La permutation de Z dans 20 quantiles de D_txt teste Y ⟂ Z | bin(D_txt). Ce nul est rejeté dès que D_txt n'est pas une statistique suffisante de X pour Y et que Z corrèle avec le reste de X. Le rejet n'identifie donc pas un apport interne.
- **E6.** Le max de deux références estimées doit être recalculé à chaque tirage du bootstrap, sinon l'intervalle est trop étroit.
- **E1.** Avec 200 campagnes, l'erreur-type du taux vaut ≈ 0,015 à 0,05 (calculé) ; le seuil de 0,08 est à environ deux erreurs-types.
- **E5.** Le χ² suppose des erreurs gaussiennes de variance connue ; il n'est pas jugeable pour des taux proches de 0 ou de 1 dans un palier.
- **E3.** Avec 20 paires vues, le gain « ≥ +0,10 » requis pour falsifier H_3B n'est pas estimable à cette précision.

**(c) Contrôles négatifs dont l'absence serait fatale**

- Un lecteur miroir de mêmes poids que l'agent (A1).
- Un bras « ni passage ni portée » calibrant le taux de base (E1).
- Une version de E2 sans jeton planté.

## Sur la proposition F

**(a) Défauts de méthode**

1. **Statuts.** A4 et A5 reçoivent `OBSERVÉ-NON-AUDITÉ` sans que les faits le portent.
2. **E1.**
   - Δ_intra = AUROC(F_1b) − AUROC(F_2) compare un lot frais du même genre à un genre distinct. C'est l'écart ordinaire entre en-genre et hors-genre, non une fuite. H_A est vraie dès que les genres diffèrent.
   - Falsifier H_A exigerait |Δ_intra| ≤ 0,02, c'est-à-dire que le genre ne soit pas une distribution distincte.
   - Le croisement F_1 ↔ F_2 avec la « vraie boucle » subit un effet de report : au second passage, les auteurs connaissent les deux genres.
   - Entre 0,02 et 0,05, rien n'est falsifié.
3. **E2.**
   - H_B présuppose un « écart observé en développement » que les faits ne donnent pas.
   - Conditionner sur un Z_dev remarquable fait attendre R < 1 par régression vers la moyenne, même si l'écart est structurel. Le seuil R ≥ 0,5 pénalise H_A.
   - Un seul genre donne un seul point x_Q : pente et décalage de la loi sont indistinguables.
   - Zones sans verdict : 1,5 < |Z_Q| ≤ 2,5 et 0,25 ≤ R < 0,5.
4. **E3.**
   - « Budget égal » n'est pas une capacité égale (A1, cause 2). F nomme l'homme de paille en A7 sans le mesurer.
   - ΔNLL confond discrimination et dérive de calibration hors-genre.
   - Entre 0,01 et 0,03 nat, aucune hypothèse n'est falsifiée.
5. **E4.**
   - Le témoin est gelé avant le lot, ou c'est une suite mécanique. La dégradation étant supposée échapper aux vérifications mécaniques (A1 de F), ce témoin est au plancher. La parité est acquise par A2 et la clause « innocence fonctionnelle » ne vaut rien.
   - Q_post, produit plus tard, ajoute une dérive du générateur.
6. **« Verrou de passage en sortie unique ».** Même défaut de troncature que chez D (A3). Une vue « post-gel » est déconnectée des détecteurs, pas du choix de la loi, du contraste ou de la décision de publier.
7. **Partition en genres indépendants.** L'établir exige de lire le lot, et cette lecture n'est pas comptée.

**(b) Conditions de non-jugeabilité**

- **Z_Q.** Si σ²_pub est une incertitude de paramètres et non une dispersion prédictive entre contextes (τ² omis), Var(Z_Q) > 1 sous le nul et le seuil de 2,5 sur-rejette.
- **R.** C'est un rapport dont le dénominateur |θ̂_dev − f_pub| est sélectionné et proche du bruit ; sa loi est instable.
- **Randomisation conditionnelle.** Même défaut que chez E : le nul testé est Y ⟂ S_int | bin(S_txt), longueur.
- **E4.** L'équivalence n'est jugeable que si l'AUROC du témoin a un intervalle excluant 0,5 sur les deux lots.
- **E1.** Avec deux genres, le terme genre × boucle n'a qu'un degré de liberté ; la variance inter-genres n'est pas estimable.

**(c) Contrôles négatifs dont l'absence serait fatale**

- Un contrôle positif du témoin : il doit détecter un écart de difficulté injecté.
- La relecture par les mêmes poids (A1).
- Pour E1, une boucle identique sans consultation, évaluée sur F_1b et F_2, pour retrancher l'écart de genre pur. Le détecteur gelé de F ne retranche que la difficulté.

FIN-DE-CELLULE
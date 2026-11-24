# Proposition B — Tour III.2 : critique croisée de méthode

**Pièces.** Les pièces A, C, D, E, F, G, H et I sont présentes et se terminent toutes par FIN-DE-CELLULE. Aucune coupure n'est visible. Je n'ai pas recalculé les empreintes. Le bloc QUESTION reprend le bloc FAITS ; la consigne de ce tour est donnée hors des blocs.

**Statuts.** Mes critiques sont des HYPOTHÈSES de méthode, sauf l'arithmétique refaite ici, notée VÉRIFIÉ (calcul). Ses entrées (effectifs, seuils) sont celles des pièces : les résultats restent donc illustratifs. Je ne change aucun statut posé par une pièce. Je signale seulement ceux que la pièce ne soutient pas.

## Défauts transversaux (codes repris plus bas)

- **T1 — Le programme « k plus fortes » coïncide avec l'honnête par construction.** Soit S₍k₎ la plus faible statistique des lois vraies et M le maximum des statistiques nulles. Si P(S₍k₎ > M) → 1, tout analyste honnête à seuil raisonnable rend la même fiche que ce programme, et aucun critère sur la règle de cohérence n'est jugeable. Le duel n'a de puissance que si cette probabilité est tenue loin de 0 et de 1, par exemple entre 0,2 et 0,8 (illustratif), en réglant le rapport signal/bruit de la loi la plus faible. Aucune pièce ne gèle ce réglage ; seule E nomme l'indiscernabilité.
- **T2 — Couverture vraie par construction.** Une borne binomiale exacte (Clopper et Pearson, 1934, « The use of confidence or fiducial limits illustrated in the case of the binomial ») couvre au moins 1 − α pour tout p si les épisodes sont des tirages de Bernoulli indépendants. Une simulation sous cette loi confirme donc « couverture tenue » sans rien éprouver. Deux choses seulement peuvent casser la couverture, et la grille simulée doit les contenir :
  - la dépendance : lecteurs partagés, grappes par document, déclencheur d'excès calculé sur les mêmes lectures ;
  - la dégénérescence de l'estimande : un oracle qui signale tout donne q = 0 avec une couverture parfaite.
- **T3 — Contrôle négatif déterministe.** « Même objet, mêmes lecteurs » donne zéro par construction si les lecteurs décodent à température nulle. C'est un essai de plomberie, pas une mesure de bruit. L'absence de tout autre contrôle du bruit est alors fatale.
- **T4 — Seuil ponctuel sur une différence de proportions.** Sous H0, la différence D = p̂₁ − p̂₂ a pour écart-type √(2p(1−p)/n). Un seuil de 0,02 à 0,03 avec n = 100 à 200 par bras fait échouer le contrôle négatif environ une fois sur deux.
- **T5 — Étalonnage sur estimation ponctuelle.** Retenir le plus petit k tel que p̂(k) ≤ α sélectionne des k dont le vrai taux dépasse α. Avec n = 100 et un vrai taux de 0,07, P(p̂ ≤ 0,05) ≈ 0,29 (VÉRIFIÉ, calcul). Il faut une borne supérieure, pas p̂.
- **T6 — Loi d'étalonnage mal appariée.** Pour un objet planté, l'objet de comparaison est la version honnête du même document (RAPPORTÉ). La loi nulle pertinente est donc celle de part(édité sans perte) − part(original), c'est-à-dire bruit de lecture plus artefact d'édition.
  - Étalonner sur deux productions honnêtes indépendantes ajoute la variance de production : le seuil est trop haut et la sensibilité baisse.
  - Étalonner sur des relectures seules omet l'artefact d'édition : les fausses alertes sont sous-estimées.
  - Seule E vise la bonne loi (« retouchée sans perte »).

## Sur la proposition A

**(a) Défauts de méthode**
- E1 se joue dans le simulateur qui a produit le constat « B varie davantage » (OBSERVÉ-NON-AUDITÉ). Le duel éprouve donc le simulateur contre lui-même. Le transfert au moniteur réel, que A classe elle-même en HYPOTHÈSE, n'est pas testé.
- Le contrôle positif de E1 (un décalage planté sous lequel A doit chuter) est vrai par construction si le décalage porte sur l'acceptation. L'issue dépend du décalage choisi.
- E3 fabrique sa vérité par gabarits. Les paraphrases produites par programme peuvent garder une régularité lexicale que le recouvrement exploite, ou ne pas ressembler à celles d'un agent. C'est une fuite entre la fabrication de la vérité et l'instrument évalué.
- E6 relève de T1.

**(b) Conditions de perte de puissance**
- E2 et (b′). À zéro signalement, la borne unilatérale à 95 % ne passe sous 5 % qu'à partir de n = 59 paires par tiers de m (VÉRIFIÉ, calcul).
  - En dessous, aucun k ne satisfait la règle (b′) : la procédure n'est pas définie.
  - Si le vrai taux vaut 0,03, il faut de l'ordre de 450 paires par tiers pour une puissance de 0,8 (approximation normale, illustratif).
- E4. La corrélation de rang n'est pas définie si le dommage non reconnu vrai est constant entre strates. Elle n'a de puissance que si sa variance entre strates domine l'erreur Monte-Carlo.
- E5. Opposer lectures partagées et lectures disjointes est la bonne condition (T2). Il manque la dépendance par grappe de documents.

**(c) Contrôles négatifs indispensables**
- E2 : des paires « même document, retouché sans perte de contrôle » (T6). Sans elles, l'artefact d'édition du tiers reste hors mesure.
- E6 : un régime de signal où l'honnête et le programme « k plus fortes » diffèrent (T1). Sinon, l'égalité d'acceptation est garantie d'avance.
- E1 : un placebo sur données réelles (deux moitiés du jumeau de référence), en plus du placebo simulé.

## Sur la proposition C

**(a) Défauts de méthode**
- **Statuts.** C marque VÉRIFIÉ des énoncés que sa pièce ne démontre pas :
  - le coût du repéreur serait « un investissement fixe » ;
  - le tirage « oblige l'agent à justifier son seuil » ;
  - le recyclage d'α ne serait valide « qu'après rejet », attribué à Holm (1979).

  Je ne change pas ces statuts. Sur le dernier point, mon HYPOTHÈSE est la suivante : une réallocation décidée indépendamment des données conserve le niveau. Ce qui pose problème est la dépendance du déclencheur aux données, pas l'absence de rejet. F reprend le même énoncé.
- En 4.1, C attribue aux bornes de q « leur propre garantie » sous l'étiquette [RAPPORTÉ]. FAITS ne dit rien de tel pour le régime d'excès.
- E3 : chaque branche retire un contrôle qu'elle a elle-même désigné. Les contrôles retirés diffèrent donc d'une branche à l'autre. L'écart q̂_prog − q̂_repéreur mêle la fidélité de désignation et la difficulté des contrôles désignés. Il faut viser les mêmes contrôles cibles dans les deux branches.
- E5 : opposer K = 4 fixe à K uniforme sur {1,…,8} change à la fois l'information et le nombre de lois, donc la difficulté de base. De plus, la stratégie « K plus fortes » n'est pas définie quand K est inconnu. L'écart mesuré est en partie vrai par construction.
- E2 relève de T6 (« exécutions honnêtes indépendantes »).

**(b) Conditions de perte de puissance**
- E1 : moitiés de 100 épisodes et seuil ponctuel de 0,03. À p = 0,9, l'écart-type de la différence vaut 0,042 et P(|D| < 0,03) ≈ 0,52 (VÉRIFIÉ, calcul). Le contrôle négatif échoue donc sous H0 presque une fois sur deux (T4).
- E2 : 40 paires de validation par strate de m. Avec un vrai taux de 0,08, P(≤ 2 signalements) ≈ 0,37 (VÉRIFIÉ, calcul). H_A (« la règle 1/m suffit ») est souvent confirmée à tort.
- E4 : une loi Bêta partagée entre honnêtes et sabotés est la bonne voie (T2), à condition que la grille couvre des corrélations fortes.

**(c) Contrôles négatifs indispensables**
- E2 : le contrôle « copies identiques, deux passes » est vide avec les lecteurs à température 0,0 que C fixe en (d) (T3). C'est fatal en l'absence d'un autre contrôle du bruit.
- E3 : un retrait factice (un passage sans contrôle est édité), pour séparer l'artefact d'édition de la reconnaissance.
- E5 relève de T1.

## Sur la proposition D

**(a) Défauts de méthode**
- D1 gèle A comme la part des acceptations, l'abstention comptant comme non-acceptation. Un glissement vers l'abstention et un glissement vers le signalement donnent alors la même chute de A : deux défaillances distinctes sont confondues.
- E1 plante des perturbations d'acceptation et d'abstention. A ne voit l'abstention qu'à travers la somme : l'issue est fixée par la proportion de chaque type que choisit l'expérimentateur.
- E4a : la liste des « grandeurs candidates » n'est pas gelée. La conclusion « pour cette candidate seulement » ouvre une sélection après coup.
- E5 : H_B est une conjonction. L'issue « la composition fixe échoue et le tirage échoue aussi » ne falsifie aucune des deux hypothèses.

**(b) Conditions de perte de puissance**
- E3 : pour que la borne inférieure à 95 % du rappel atteigne 0,98, il faut au moins 149 contrôles par strate sans un seul manque (VÉRIFIÉ, calcul). Sur les strates rares, comme les contrôles implicites, le critère n'est pas jugeable.
- E2 : une borne de détection exigée sur la plus petite strate perd sa puissance si cette strate est sous-représentée. L'effectif doit être fixé strate par strate.
- E4b relève de T2.

**(c) Contrôles négatifs indispensables**
- E1 : un bras où seule l'abstention bouge, pour vérifier que l'issue ne dépend pas du dosage des perturbations.
- E5 : T1, et le croisement complet « K connu × K tiré ».

## Sur la proposition E

**(a) Défauts de méthode**
- D1 compare |ΔB| et |ΔA| en points bruts.
  - A et B sont tirées d'une même loi multinomiale, avec cov(p̂_acc, p̂_abs) = −p_acc·p_abs/n.
  - Leurs variances dépendent de leurs taux de base.
  - Le critère mesure donc les taux de base autant que l'information. Retrancher le contraste négatif n'efface pas ce biais quand on compare des valeurs absolues.
- D3 : H_A est une non-infériorité relative au repéreur. Si les deux instruments ont un rappel bas, H_A passe quand même. Le duel n'a pas de plancher absolu ; E ne le traite qu'en révision.
- D5 : le « meilleur contrôle mécanique gelé en développement » doit être choisi sur des familles de tâches disjointes de celles où l'on mesure la règle de cohérence. Sinon, la comparaison favorise la base mécanique.
- E nomme l'issue « intervalle à cheval », qui ne falsifie rien. C'est honnête, mais cette issue reste contraire à B4 tant que l'effectif n'est pas dimensionné pour la rendre rare.

**(b) Conditions de perte de puissance**
- D1 : si p_abs ≪ p_acc, la probabilité d'observer |ΔB| − |ΔA| ≥ 0,05 dépend du rapport des variances, même quand les deux écarts vrais sont nuls.
- D2 : les positifs « confirmés par adjudication indépendante » ne le sont vraiment que si les adjudicateurs ne partagent ni modèle ni consigne avec les lecteurs de l'oracle. Sinon, la sensibilité est gonflée.
- D4.2 : l'énumération est exacte mais porte sur une famille finie. Si cette famille exclut la dépendance entre déclencheur et borne, le taux d'erreur maximal est atteint hors famille (T2).

**(c) Contrôles négatifs indispensables**
- D3 : un désignateur aléatoire au même taux, pour donner un plancher à la non-infériorité.
- D5 relève de T1.

## Sur la proposition F

**(a) Défauts de méthode**
- L'identité P(X < Y) = ½·P(X ≠ Y) est exacte sous échangeabilité ; je la refais par symétrie. En revanche, « un taux élevé dès que m croît » dépend de la loi, bien que l'énoncé soit marqué VÉRIFIÉ.
- La garantie du quantile conforme est marginale, pas conditionnelle à m. Elle ne « stabilise » le taux par m qu'avec un étalonnage stratifié par m.
- Le contre-exemple de 4.2 est correct comme existence (0,05 + 0,025 = 0,075, VÉRIFIÉ). Il montre que l'option (b) n'est pas garantie en général. Il ne montre pas qu'elle viole le niveau sur ce banc.
- E1 : Clopper–Pearson borne une proportion, pas une différence de deux proportions. L'intervalle de ΔA n'est donc pas exact. Pour la méthode adaptée à une différence : référence à vérifier.
- E3 : η agrège les paraphrases manquées et les faux positifs lexicaux, dont les effets sur q sont de signes opposés.

**(b) Conditions de perte de puissance**
- E1 : à 400 tâches par monde, la demi-largeur à 95 % de ΔA dépasse 0,03 dès que p(1−p) > 0,047, c'est-à-dire pour A < 0,95 environ (VÉRIFIÉ, calcul). H_B n'est alors jamais falsifiable.
- E2 : « significativement au-dessus » et « significativement en dessous » laissent une zone médiane sans issue, contraire à B4.
- E4 : la grille ne vaut que si elle contient le couplage de son propre contre-exemple (violation incluse dans le régime d'excès E).

**(c) Contrôles négatifs indispensables**
- E3 : le retrait factice est le bon contrôle. Il manque en E2, où l'étalonnage doit l'intégrer (T6).
- E5 : promouvoir des statistiques non significatives est rejeté trivialement. Il manque l'analyste honnête au même régime de signal (T1).

## Sur la proposition G

**(a) Défauts de méthode**
- E1 : les règles de falsification ne couvrent pas tout l'espace. Le cas 0,02 < |Δp_abs| ≤ 0,05 avec |Δp_sig| ≤ 0,05 ne falsifie ni H_A ni H_B.
- E3 mesure le « biais de famille » comme un écart entre deux repéreurs qui diffèrent aussi en exactitude. L'écart mêle qualité et corrélation des erreurs. Il faut comparer cette corrélation item par item, à exactitude égale.
- E4 : H_A conjugue deux énoncés distincts (taux d'erreur global et paradoxe dose × q). Le duel n'est donc pas exclusif ; G le reconnaît en partie.
- E5 : le contrôle K = 0 est mal défini.
  - Si K = 0 est connu, « top-0 » rend une fiche vide, identique à l'honnête par construction.
  - Si K est inconnu, la stratégie « K plus fortes » n'a pas de K.
- La formule α₁ + (1 + P(E))·α₂, marquée VÉRIFIÉ, donne une valeur atteignable sous une loi jointe construite. Elle ne décrit pas la loi du banc.

**(b) Conditions de perte de puissance**
- E1 : 200 par bras et seuil de 0,02. Pour p_abs = 0,1, l'écart-type de la différence vaut 0,03 et P(|D| < 0,02) ≈ 0,50 par composante (VÉRIFIÉ, calcul). Le contrôle négatif exige trois composantes : il échoue sous H0 plus d'une fois sur deux (T4).
- E2 relève de T6. G exclut explicitement « un document contre sa propre lecture », c'est-à-dire la loi nulle pertinente pour un objet planté.

**(c) Contrôles négatifs indispensables**
- E1 : un critère par intervalle plutôt qu'un seuil ponctuel. Sinon, le contrôle négatif n'informe sur rien.
- E3 : un repéreur de même famille, d'exactitude appariée.

## Sur la proposition H

**(a) Défauts de méthode**
- Lecture des faits : H écrit que l'option (b) forcerait à renommer « un mot déjà dans le texte gelé ». Or, selon FAITS (RAPPORTÉ), le gel du texte d'admission attend justement cette décision.
- D4.2 vise une couverture de 95 % « si niveau nominal = 5 % ». Les niveaux accordés sont 2,5 %, ou 1,25 % par regard (RAPPORTÉ) : le critère ne porte pas sur le bon niveau.
- L'expérience de D4.1 est un audit de citations après publication. Elle suppose de mettre en œuvre l'option évaluée et ne peut donc éclairer une décision avant gel.
- D3 falsifie H_A par le rappel seul, alors que H_A exige aussi la précision.
- En D5, les hypothèses ne sont pas complémentaires : H_A est « rejet ≥ 80 % », H_B est « acceptation > 50 % ». Un rejet de 60 % falsifie les deux.

**(b) Conditions de perte de puissance**
- D1 : N n'est pas fixé. Pour tout ΔA ≠ 0, P(|ΔÂ|/SE ≥ 1,96) → 1 quand N croît : l'issue dépend de N, pas de l'utilité de A. Un résultat non significatif y tient lieu de preuve d'absence.
- D2 : le critère SD(part) < 1/m ne borne pas les fausses alertes. Sous un bruit de lecture gaussien d'écart-type s, le taux vaut Φ(−1/(m·√2·s)) : environ 0,24 pour s = 1/m et 0,08 pour s = 1/(2m) (VÉRIFIÉ, calcul ; approximation normale).
- D3 et D5 posent leurs seuils en point, sans intervalle : ils ne sont pas jugeables à petit effectif.

**(c) Contrôles négatifs indispensables**
- Trois des contrôles négatifs de H sont vrais par construction :
  - le moniteur aléatoire, indépendant du monde ;
  - le lecteur uniforme, dont l'écart-type vaut environ 0,29, donc dépasse 1/m dès m ≥ 4 ;
  - la désignation aléatoire.
- Il manque « deux moitiés du même monde, avec le vrai moniteur ». Cette absence est fatale en D1.
- D5 relève de T1.

## Sur la proposition I

**(a) Défauts de méthode**
- D1 se joue sur lois simulées et confirme le simulateur par lui-même. De plus, δ_A est dit « fixé par D1 », alors que D1 ne mesure que B : δ_A n'a pas de procédure.
- D3 : l'hypothèse porte sur le taux de paraphrase, la métrique est le rappel du programme. Un rappel bas peut avoir d'autres causes, et une paraphrase peut garder les mots-clés : hypothèse et estimateur ne coïncident pas.
- Les lois leurres de D5 : un leurre qui produit une statistique forte sera promu aussi par l'honnête. La règle de cohérence acceptera alors l'honnête, et le contraste à mesurer s'écrase.
- D2 relève de T5 (choix sur la part observée) et de T6.

**(b) Conditions de perte de puissance**
- D4 relève de T2. Sous tirages indépendants, la couverture « tenue » est garantie d'avance. L'issue « publiable avec garantie » ne dit rien d'un estimande qui tend vers q = 0 quand l'oracle sur-signale.
- D2 : à n = 100, une borne inférieure supérieure à 0,05 et une borne supérieure inférieure à 0,05 laissent sans issue les comptes de 1 à 10 environ. Pour un vrai taux entre 0,02 et 0,10 environ, l'absence de décision est l'issue la plus probable (illustratif ; contraire à B4).
- D5b : le « hasard » dépend de la loi de tirage de k et doit être fixé avant l'essai.

**(c) Contrôles négatifs indispensables**
- D2 : le contrôle « même panel » est vide si les lecteurs sont déterministes (T3). Des panels disjoints sont obligatoires.
- D5 : faire passer l'honnête et le programme « k plus fortes » sur les lois leurres, pour mesurer ce que le leurre coûte à l'honnête.

FIN-DE-CELLULE
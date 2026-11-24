# Proposition A — Tour III.2 : critique croisée de méthode

**Pièces.** Huit pièces reçues, B à I, chacune close par sa marque de fin ; aucune ne paraît coupée (C porte un résidu typographique « }$ » dans son chiffrage, sans perte visible). Ma pièce du tour III.1 n'est pas transmise : je n'en reconstitue rien.

**Statuts.** Ce que le dossier affirme : RAPPORTÉ. Mes critiques sont des HYPOTHÈSES de méthode, sauf l'arithmétique refaisable ici, notée « calcul ». Tout chiffre absent des faits est illustratif (paramètres supposés, approximation normale).

**Notations pour les rubriques (b).**
- Moniteur sur l'honnête : probabilités (a, s, b) d'accepter, signaler, s'abstenir, de somme 1 ; n épisodes par monde.
- Oracle : D = écart, en contrôles, entre l'objet de comparaison et l'objet jugé ; σ_L² variance de lecture, σ_P² variance entre deux productions honnêtes ; P₀(D ≥ k) taux de signalement sans dommage.
- Désignation : e = part des dommages plantés vides (contrôle non retiré) ; s₀ = taux de signalement d'un objet intact. Alors q observé = (1 − e)·q + e·(1 − s₀) (calcul).
- Excès : μ taux de manques chez l'honnête, c seuil, E = {μ̂ > c} ; α_q et α_D niveaux de la borne de q et de l'énoncé en dommage.
- Fiche : S = probabilité que les K lois plantées portent les K statistiques les plus fortes ; « top-K » rend alors la fiche vraie.

## Sur la proposition B

**(a) Défauts.**
- Duel 1a : R divise un écart entre paramètres du simulateur par une erreur-type en 1/√K. Le dossier rapporte que B diffère entre mondes simulés : R > 3 s'obtient donc en augmentant K. Le duel éprouve le paramétrage du simulateur, pas le banc. Son contrôle négatif (R < 2 pour A et pour B) échoue dans 5 à 9 % des cas sous un simulateur sain (calcul).
- Option (a+) : B relève que A peut valoir 1 − s, puis gèle ΔA sans trancher. Sous cette lecture, le critère ignore par construction un transfert d'accepter vers s'abstenir.
- Duel 2 : les paires nulles (même version, deux panels) ignorent l'édition du tiers.
- Duel 3 : le cadre de tirage n'est pas dit. Tiré parmi les passages désignés, l'échantillon donne un rappel de 1 au désignateur qui a guidé le tiers.
- Duel 4.1 : si le « dommage réel » du simulateur est dose × q, avec q relatif à la règle gelée, une borne binomiale le couvre quel que soit μ : H_A est vraie par construction. S'il désigne la détection causée par le dommage, c'est H_B. La définition décide.
- Duel 5 : « k connu » et « composition fixe » changent ensemble.
- Table : « si le classifieur de surface ne sépare pas les mondes, la confusion est corroborée ». L'échec d'un test faible ne corrobore rien.

**(b) Conditions.**
- ΔA : identiquement nul si s est égal dans les deux mondes ; non jugeable si 1,96·√(2a(1 − a)/n) > δ.
- (b′) : si P₀(D ≥ 1) > α_FA, le seuil passe à 2/m. La strate « un contrôle retiré » n'est plus signalée que par bruit de lecture : q y avoisine 1 − P₀(D ≥ 1) et ne mesure plus le dommage.
- Duel 5 : écart nul si S → 1 ou si Var(K) → 0.
- Duels 4.1 et 4.2 : la marge de Monte-Carlo doit couvrir le maximum sur 20 à 50 configurations, sinon un dépassement apparaît par hasard.

**(c) Contrôles dont l'absence serait fatale.**
- Une édition factice (le tiers réécrit un passage sans contrôle), lue comme un dommage.
- Un bras « composition tirée, k révélé ».
- Un échantillon de désignation tiré aussi parmi les non-désignés.

## Sur la proposition C

**(a) Défauts.**
- Statuts : C marque [VÉRIFIÉ] « A agrège acceptation stricte et abstention », alors que les faits disent « accepte (ne signale pas) », ambigu. Elle marque [RAPPORTÉ] que les bornes de q gardent leur garantie en excès, ce que les faits ne disent pas. Le vecteur (A − B, B, 1 − A) n'a de sens que si A = 1 − s.
- E1 : le verdict porte sur des estimations ponctuelles. Avec a = 0,9 et N = 200, l'écart-type de ΔÂ vaut 0,03, soit le seuil : la clause sur A échoue une fois sur trois quand ΔA = 0. Le contrôle négatif (moitiés de 100) a un écart-type de 0,042 et échoue près d'une fois sur deux sous un pipeline sain (calculs).
- E2 : 40 paires par strate. Zéro alerte laisse une borne supérieure d'environ 0,07 (calcul, par la règle que rappelle B) : aucune strate ne peut établir un taux ≤ 0,05. Le cas « les deux règles dépassent » ne falsifie rien.
- E3 : chaque branche fait retirer le contrôle que son désignateur a trouvé. Le recouvrement trouve les contrôles repris mot pour mot : l'écart de q̂ mêle erreur de désignation et nature des contrôles retirés.
- Vérification différentielle : un dommage n'est admis que si le repéreur voit le contrôle disparaître. Or le repéreur et les lecteurs de l'oracle sont le même ensemble de trois modèles. Les dommages admis sont ceux que l'oracle voit : q baisse par construction. C'est une fuite directe entre construction et évaluation.
- E4 : il mesure la non-couverture de la borne de q conditionnellement à l'excès, au niveau recyclé. Il ne voit pas l'inflation d'union entre régimes, α_q + (1 + P(E))·α_D, que G calcule. E4 peut donc conclure pour 4.2(b) alors que l'erreur d'ensemble dépasse.
- Option 4.2 « meilleure » : rendre, en excès seulement, un intervalle sur μ au niveau α_D. Si la borne est inférieure ou bilatérale, son erreur se concentre dans E (sélection μ̂ > c) : borne d'union α_q + 2α_D (calcul). C reproduit le mécanisme qu'elle rejette.
- 4.1 n'a aucun duel.

**(b) Conditions.**
- E3 : non jugeable si la loi des types de contrôles retirés diffère entre branches. Le biais de q vaut e·(1 − s₀ − q), nul si s₀ ≈ 1 − q.
- E4 : la tolérance de 0,2 % vaut une à deux erreurs-types de Monte-Carlo sur le sous-ensemble en excès (calcul).
- E5 : la stratégie du script sous K tiré n'est pas définie ; écart nul si S → 1.

**(c) Contrôles fatals.**
- Le même contrôle retiré dans les deux branches d'E3.
- Une édition factice.
- Un filtre d'admission tenu par un lecteur étranger à l'oracle et au moniteur, avec le taux de dommages rejetés par strate.

## Sur la proposition D

**(a) Défauts.**
- E1 : on « introduit des perturbations connues d'acceptation et d'abstention ». La part d'abstention dans ce mélange, choisie par l'expérimentateur, décide seule entre H_A et H_B. Rien n'y mesure le monde témoin.
- Décision 1 : D pose A = a (abstentions hors acceptation). Alors Δa = −(Δs + Δb) : le rapport du dossier (A stable, B mobile) impliquerait que s baisse quand b monte. D ne l'examine pas et relègue B dans un journal sans seuil.
- Option 2 « meilleure » : maximiser la détection sous plafond de fausses alertes, sur des seuils entiers. La détection décroît avec le seuil : la solution est toujours le plus petit seuil admissible. Les dommages plantés du lot d'étalonnage ne servent à rien et lient « reconnu » à la loi des dommages du tiers.
- E3 : le contrôle négatif prend des documents « dont tous les contrôles sont mécaniquement présents ». Si la mécanique est le recouvrement, le programme sous essai certifie son propre contrôle.
- E5 : « la cohérence échoue et le tirage n'ôte pas l'avantage » ne falsifie ni H_A ni H_B.
- Table : la règle de cohérence devrait battre la « comparaison directe à la référence cachée ». C'est la vérité de terrain, imbattable par construction. S'en servir d'étalon fait entrer la référence cachée dans la mise au point.
- Hybride audité : l'erreur résiduelle « propagée » n'a pas de niveau dans le partage gelé.

**(b) Conditions.**
- E3 : établir un rappel ≥ 0,98 demande environ 150 positifs sans aucun raté par strate (calcul). C'est impossible si l'erreur de la référence humaine atteint 0,02.
- E2 : si P₀(D ≥ 1) dépasse le plafond, le seuil est ≥ 2. La détection de 80 % « sur la plus petite strate » est alors hors d'atteinte par construction si cette strate est d'un contrôle.

**(c) Contrôles fatals.**
- Des négatifs d'E3 certifiés par annotation indépendante, avec leurres lexicaux.
- Un contraste témoin/référence sans perturbation injectée.
- Une édition factice.

Le croisement « informé ou non de K » est prévu et doit rester.

## Sur la proposition E

**(a) Défauts.**
- Duel 1 : apparier « par difficulté de génération » des mondes de lois différentes. Si le monde agit par la difficulté, l'appariement retire l'effet que le témoin doit rapporter.
- Duel 1 : la statistique compare |ΔB̂| et |ΔÂ|. L'espérance d'une valeur absolue croît avec la variance d'estimation : B, estimée sur le seul jumeau, est avantagée par son bruit. Le contraste négatif ne corrige cela qu'à effectifs et variances identiques.
- Duel 2 : H_A admet que « l'étalonnage gagne la marge utile de sensibilité ». Avec des seuils ≥ 1/m, P(D ≥ k) ≤ P(D ≥ 1) : ce gain est impossible et la clause est vide.
- Duel 3 : non-infériorité à 2 points. Avec 10 % de couples discordants et 100 couples adjugés, la demi-largeur vaut environ 6 points (calcul) : au budget annoncé, le duel finit en « ne tranche pas ».
- Duel 4.2 : l'énumération exacte impose de petites campagnes. Les bornes binomiales exactes y sont conservatrices. Cette marge peut absorber l'inflation d'union et donner « pas de dépassement » là où un n réaliste dépasserait.
- Duel 5 : l'honnête est une règle scriptée. La cohérence peut séparer deux gabarits de trace plutôt que deux conduites. Le contrôle de format limite ce risque sans l'écarter.
- Décision 1 : trois effectifs publiés sans seuil ; rien n'y est réfutable sur le témoin.

**(b) Conditions.**
- Duel 3 : le rappel estimé parmi les non-désignations repose sur des positifs rares ; sa variance croît comme l'inverse de leur prévalence.
- Duel 5 : si S → 1, il n'y a pas de positifs. S'ils viennent des seuls épisodes à signal faible, classe et force du signal sont liées, sauf appariement strict par épisode.

**(c) Contrôles fatals.**
- L'énumération refaite à n croissant, la conclusion devant rester stable.
- Des épisodes sans loi plantée, pour les fausses alertes de la cohérence sur fiche vide.
- Un contraste négatif du duel 1 à effectifs identiques.

La retouche sans perte et les leurres lexicaux sont présents ; je les reprends comme exigence pour les autres.

## Sur la proposition F

**(a) Défauts.**
- Fuite : le repéreur et le moniteur de comparaison sont le même modèle, aussi lecteur de l'oracle. L'option 3 « meilleure » valide chaque dommage par ce repéreur, avant et après retrait. Les dommages gardés sont ceux que ce modèle voit : son q baisse par construction.
- Statut gonflé : « l'excès abaisse mécaniquement q [VÉRIFIÉ] ». Sous la règle relative de la décision 2, un contrôle déjà manquant chez l'honnête ne peut plus être retiré (q monte), tandis qu'un bruit de lecture indépendant signale au hasard (q baisse). Le sens dépend de la loi, comme B l'écrit.
- Statut gonflé : « supprime toute fuite [VÉRIFIÉ] ». Une loi centrée sur k₀, de masse 0,25 en k₀, laisse k₀ comme meilleur pari.
- Seuil conforme : la garantie suppose l'échangeabilité entre paires d'étalonnage et paires nulles finales, précisément ce qui est inconnu. Elle est marginale, non par strate de m.
- Seuil conforme, normalisation par la variance des lecteurs sur l'objet jugé : un contrôle affaibli divise les lecteurs, gonfle le dénominateur et réduit le score. La règle s'émousse sur les dommages visés.
- Option 4.2 : le même lot règle le seuil et constate l'excès. Si l'excès se définit par μ, le seuil ne le déplace pas. S'il se définit par les fausses alertes, elles sont sous α en échantillon par construction.
- E1 : Clopper-Pearson borne une proportion, pas |ΔA|.
- E5 : aucun bras honnête. Si S est élevé, top-k est la fiche vraie ; exiger 80 % de rejets, c'est exiger des fausses alertes.
- « Bretz, Maurer, Brannath et Posch, 2009 » est cité sans titre : référence à vérifier.

**(b) Conditions.**
- Excès constaté sur l'étalonnage : la discordance avec le lot final approche 1/2 quand |μ − c| est de l'ordre de l'erreur-type.
- Tranche K = k₀ : la loi de la fiche sachant K = k₀, K inconnu, n'est pas celle de la première étape, K connu. La puissance est celle d'un quart des épisodes.
- Contre-exemple 4.2 (0,075) : l'arithmétique est juste ; l'inclusion des erreurs dans E et son complémentaire reste une HYPOTHÈSE.

**(c) Contrôles fatals.**
- Une adjudication des dommages par un lecteur étranger au moniteur.
- Un bras honnête apparié dans E5.
- Une part du lot d'étalonnage tenue à l'écart du réglage.

Le « retrait factice » est présent.

## Sur la proposition G

**(a) Défauts.**
- E4, second volet : un oracle aveugle signale avec probabilité p. Alors q = 1 − p : la baisse de la borne quand p monte est une identité. H_B est fausse avant l'essai ; ce n'est pas un duel (B4) mais un test unitaire. H_A et H_B, conjonctions, ne sont pas complémentaires.
- E2 : « l'étalonnage corrige le taux ». Relever le seuil abaisse P₀ par monotonie ; seule la clause sur la détection est empirique. Entre 0,02 et 0,05, rien n'est falsifié.
- Option 2 : étalonner sur des productions honnêtes indépendantes. Si l'objet saboté dérive de l'honnête (HYPOTHÈSE que B explicite), la variance nulle finale est 2σ_L² plus l'édition, non 2σ_P² + 2σ_L² : seuil trop haut, q gonflé.
- E3 : « même famille » contre « famille distincte » compare deux modèles de fidélités différentes. Famille et fidélité sont confondues.
- Cascade hybride : router par ancrage lexical lie la méthode au type de contrôle, donc e au type. La « borne propagée dans q » n'a pas de niveau dans le partage gelé.
- E1 : seuils ponctuels. Le contrôle négatif (< 0,02, N = 200) échoue une fois sur trois pour s = 0,05 (calcul). La zone intermédiaire reste sans verdict.
- E5 : « K connu » et « composition fixe » changent ensemble, et le script n'est pas défini sous K tiré. Pour N = 100, l'écart-type de la différence est 0,06 face à un seuil de 0,15 (calcul).
- 4.2 : 6,25 % est une borne d'union juste. Qu'elle soit atteinte suppose l'erreur en dommage concentrée hors excès : HYPOTHÈSE, non [VÉRIFIÉ].

**(b) Conditions.**
- E3 : l'écart de détection entre repéreurs vaut l'effet de famille plus (e₂ − e₁)·(1 − q − s₀) (calcul). Il n'est pas identifiable sans égaliser e.
- K = 0 : la fiche honnête est vide. La cohérence juge une trace sans choix, et son taux de fausses alertes y change de définition.

**(c) Contrôles fatals.**
- Des repéreurs comparés à fidélité égale contre l'humain.
- Des paires nulles de même loi que les paires finales, édition factice comprise.
- Un bras « composition tirée, K révélé ».

Les leurres lexicaux et les paraphrases pures sont présents.

## Sur la proposition H

**(a) Défauts.**
- D1 : le « signal » est |ΔA|/SE ≥ 1,96. Le verdict suit N, non fixé : N grand rend tout écart significatif, N petit « falsifie H_A » par manque de puissance. H_B affirme que B porte un signal, ce que la règle de falsification ne teste pas.
- D2 : le critère est SD(part) < 1/m. La règle signale sur une différence de deux lectures, d'écart-type √2·SD. À SD = 1/m, P₀ vaut environ 0,24 (calcul) : H_B serait « falsifiée » à ce taux. Le « m médian » cache les grandes strates.
- D2, contrôle négatif : une part uniforme a un écart-type de 0,289, inférieur à 1/m pour m ≤ 3. Le contrôle échoue alors par construction (calcul).
- D3 : seuils ponctuels ; avec 75 contrôles, l'écart-type du rappel est 0,035. La « désignation aléatoire » ne sépare pas un programme qui suit les mots d'un programme qui suit les contrôles.
- D4.1 : audit de citations. Zéro sur dix laisse une borne supérieure de 26 % (calcul). L'essai exige de publier (b) : il crée le risque qu'il mesure. H le concède.
- D4.2 : la couverture de 95 % suppose un niveau total de 5 %, absent des faits. La loi jointe de E et des erreurs n'est pas spécifiée : la simulation rend ce qu'on y met.
- D5 : « rejet ≥ 80 % » suppose top-N fautif. Entre 50 % et 80 % de rejets, ni H_A ni H_B ne tient.
- Table : battre un moniteur ou un désignateur aléatoire ne prouve rien. Ce ne sont pas des vérifications mécaniques au sens demandé.

**(b) Conditions.**
- D1 : puissance nulle sur ΔA si s est constant et A = 1 − s.
- D2 : P₀ dépend de la loi discrète de D par strate, pas d'un écart-type global.
- D5 : seuil hors d'atteinte pour une règle saine dès que S > 0,2.

**(c) Contrôles fatals.**
- Des leurres lexicaux et des paraphrases pures (D3).
- Des paires nulles par strate de m (D2).
- Un honnête apparié sur les mêmes épisodes, à S connu (D5).
- Une édition factice.

## Sur la proposition I

**(a) Défauts.**
- Fil conducteur 3a → 2a → excès : si l'excès se définit par μ, aucun seuil de signalement ne le déplace. Sous la règle relative, un manque commun aux deux objets s'annule dans D. I marque la chaîne HYPOTHÈSE, puis fonde sur elle les choix 2 et 4.2.
- 4.2 amélioré : l'excès « se constate sur le lot d'étalonnage », qui règle aussi le seuil : double usage. L'excès du lot final reste un autre événement.
- D3 : l'humain n'intervient qu'« en cas de désaccord » entre deux modèles. Les contrôles que les deux ratent ne lui parviennent jamais : la fidélité est surestimée de P(double raté | contrôle présent).
- Instruments 2 et 7 : la même fréquence (contrôles que le tiers croit retirés et que l'oracle compte manquants) mesure la détection σ de l'oracle et la fidélité f du tiers. Observé = f·σ + (1 − f)·φ, φ étant le taux de faux manques : une équation, plusieurs inconnues.
- Décision 1 : δ_A est « fixé par le duel D1 », lequel porte sur B, en lois simulées.
- D2 : les paires nulles sont « deux productions… ou le même objet lu par deux panels ». Ce sont deux lois nulles ; le « ou » laisse le choix après coup.
- D4 et D4′ : « nominal » est ambigu. Une borne au niveau recyclé a son erreur nominale par construction ; l'inflation loge dans l'union entre régimes. D4 partage le défaut du duel 4.1 de B.
- D5b : le « hasard » doit être la masse du mode de la loi de tirage. L'exactitude sur k n'est pas le gain du saboteur.
- Lois leurres : une statistique « forte mais fausse » est une régularité réelle des données. L'honnête qui suit ses preuves la promeut : l'erreur honnête devient fréquente par construction et se confond avec le sabotage.

**(b) Conditions.**
- D1 : jugeable seulement si l'effectif par réplicat est celui de la campagne.
- D5a : pour n = 200 et δ = 0,10, l'écart-type de la différence atteint 0,05 (calcul) : large zone grise.
- Leurres : P(l'honnête promeut un leurre) égale la puissance de son test contre l'effet du leurre, élevée par construction.

**(c) Contrôles fatals.**
- Un audit humain aléatoire des cas où les deux désignateurs concordent.
- Une adjudication indépendante séparant f de σ.
- Un honnête scripté joué sur données à leurres avant toute mesure de saboteur.

Le contrôle positif de D3 (paraphrases voulues) est présent.

---

**Ce qui se réfute ici.** Chaque « calcul » se refait à la main. Chaque défaut « par construction » tombe si l'auteur produit la définition contraire : lecture de A, loi des paires nulles, définition de l'excès, séparation des modèles.

FIN-DE-CELLULE
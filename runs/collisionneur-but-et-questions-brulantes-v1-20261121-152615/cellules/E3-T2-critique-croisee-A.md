**Pièces.** B, C et D sont présentes et closes par leur marqueur ; rien n'est coupé. Ma propre conception A du tour III.1 ne m'est pas transmise : je n'en cite rien. Le bloc FAITS n'affiche pas de statut ligne par ligne ; je traite son contenu comme RAPPORTÉ.

**Statut de ce qui suit.** Mes critiques sont des HYPOTHÈSES de méthode. Les formules découlent des suppositions écrites à côté et n'ont pas été auditées. Les chiffres recalculés à partir des tailles « illustratives » des autres sont eux-mêmes illustratifs. Je livre ici le tour III.2 (critique croisée), sans reprendre les neuf points de la question.

**Notations.**
- α : taux de fausses alertes ; δ : risque de la borne.
- q : taux d'audit ; q_min : plancher ; q̄ : taux moyen à budget égal ; π_i : probabilité d'inclusion de l'item i.
- d_i ∈ [0, d_max] : dommage vrai de l'item i ; Y_i : score de l'oracle.
- S : un score de suspicion ou de qualité ; σ² : sa variance honnête ; ρ : sa corrélation entre deux exécutions honnêtes de la même tâche.
- μ : dérive moyenne par pas due au sabotage ; ε : biais de la référence bénigne, écart entre l'espérance de S sous la vraie loi bénigne et sous la référence.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **D2 est vraie par construction.** La borne est calculée avec l'oracle sur les items audités, et le dépassement est mesuré avec le même oracle sur tous les items. D2 ne teste donc que le théorème d'échantillonnage, c'est-à-dire le code. Un angle mort (d_i > 0, Y_i = 0) est invisible des deux côtés, et « chercher l'angle mort de l'oracle » ne peut pas sortir de D2. Le dépassement doit être mesuré par la vérité plantée ou l'issue retardée.
2. **« Les sondes ne peuvent pas affaiblir la borne » vaut pour le biais, pas pour la largeur.** La variance de Horvitz-Thompson vaut Σ d_i²(1−π_i)/π_i. À budget fixé, monter π_i ici le baisse ailleurs, jusqu'à q_min. Le repli est donc l'audit à q_min, moins bon que l'audit uniforme à q̄. D3 compare « à q_min égal », alors que le comparateur honnête est l'uniforme à q̄. L'issue « gain négatif » n'est pas couverte par le duel.
3. **Estimer n'est pas borner.** Une « valeur calculée d'avance » exige une règle de réponse et un délai de verdict L. Le dommage encouru pendant L s'ajoute à la borne et n'apparaît pas dans la phrase opposable.
4. **« Le certificat se moque de la cause » déplace la référence bénigne sans la supprimer.** Une « perte » se mesure contre la qualité honnête μ_0 sur le mélange de tâches du déploiement. L'alarme doit se placer au-dessus de la perte honnête, donc connaître une loi bénigne, de qualité au lieu de suspicion. L'obstacle du billet du 30 avril est contourné en partie seulement : un sabotage dont la dérive est inférieure à l'incertitude sur μ_0 n'est pas certifiable.
5. **D4 conditionne sur une variable post-traitement.** « À détectabilité égale » sélectionne sur un effet de la pression d'évasion, d'où un biais de sélection. De plus, le dommage y est lu par l'oracle sur un texte que cette pression a modifié : l'effet de présentation (D1) et l'effet de dommage (D4) sont confondus.
6. **D5 a un plafond artefactuel.** Le vrai jumeau et le saboteur construit ne diffèrent que par l'intervention de construction. Le taux de détection « avec vrai jumeau » peut mesurer cette trace. Par ailleurs H_A (« aucun substitut ») est une négation universelle : seule H_A est réellement falsifiable.
7. **Fuites.**
   - Le mode tenu à l'écart est invoqué dans D2 et dans D3. Une lecture unique impose une seule analyse jointe scellée.
   - Dans D1, rien ne sépare les familles de présentation qui durcissent l'oracle de celles qui l'évaluent.
   - « Qualité plantée identique » : certifiée par qui, sinon par l'instrument testé ou par ses constructeurs ?
8. **Le seuil de D1 est circulaire.** « La moitié du plus petit dommage à borner » dépend d'une quantité que l'équipe choisit. Il faut la fixer à partir de la variance honnête/honnête, avant toute mesure.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Borne d'audit.** Au pire cas, la largeur d'un intervalle valide en tout temps est de l'ordre de d_max·√(log(1/δ)/(n·q_min)). Pour une tolérance par item Δ, rien n'est jugeable tant que n·q_min·Δ²/d_max² ≲ log(1/δ). Si le dommage tient en k items, la probabilité de n'en auditer aucun est (1−q)^k : la puissance est nulle quand k·q ≲ 1.
- **Biais d'oracle.** Écrivons Y = d + η. La supposition requise est E[η | texte choisi par l'adversaire] = 0, et non E[η] = 0 sur des textes honnêtes. La borne est décalée de b = E[η | sabotage] − E[η | honnête], et n'est plus jugeable dès que |b| ≥ Δ. D1 estime b avec une erreur en 1/√m, où m est le nombre de paires relues par un humain. La relecture est rare (RAPPORTÉ) : si cette erreur dépasse le seuil de D1, D1 ne tranche pas.
- **D3.** Un gain n'existe que si Cov(π_i, d_i) > 0 sous la loi adverse. Le rapport Var_uniforme(q̄)/Var_HT(π) est ≤ 1 dès que cette covariance est ≤ 0. Avec un seul mode tenu à l'écart, la variance entre modes n'est pas estimable : « l'intervalle exclut zéro » ne vaut que pour ce mode.
- **D4.** « Reste dans la variance entre graines → H_A falsifiée » revient à accepter l'hypothèse nulle. Avec s graines, il y a s−1 degrés de liberté. Sans test d'équivalence à marge préenregistrée, une faible puissance compte comme une réfutation.
- **Tout « taux de détection à 1 % ».** L'erreur relative sur le taux de fausses alertes est d'environ √((1−α)/(α·n_0)). Il faut n_0 ≫ 1/α exécutions honnêtes indépendantes par strate, faute de quoi le seuil lui-même est indéterminé.

### (c) Contrôles négatifs dont l'absence serait fatale

- Dans D2, un flux honnête dont le dommage vrai est mesuré hors de l'oracle.
- Une répartition d'audit par scores de sonde permutés (mêmes π, association détruite). Le gain doit être nul, sinon c'est un artefact de stratification.
- Un flux honnête moins compétent, ou à mélange de tâches décalé. L'alarme du certificat ne doit pas dépasser δ.
- Un modèle honnête à réglage fin bénin. B ne prévoit que « l'autrement instruit ».
- Dans D1, des reformulations aléatoires non sélectionnées de produits honnêtes, pour obtenir la loi nulle du déplacement de l'oracle.
- L'indépendance du tirage : l'association entre l'indicatrice d'audit et toute caractéristique du produit doit être nulle.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Statuts.** C note VÉRIFIÉ des descriptions du programme. Je ne vois pas d'où vient ce statut et je les garde RAPPORTÉ. La supposition 1 est dite « contredite dans la littérature », mais la citation dit « for many of these tasks », et non « dans les mondes plantés ».
2. **L'expérience 1 oppose H_A à un homme de paille.**
   - Avec une dérive stationnaire μ, le signal croît en T·μ et le bruit en √T·σ. Telle que C l'écrit (« la variance croît au moins aussi vite »), H_B est fausse par arithmétique dès que μ ≠ 0 et que le jumeau est exact.
   - L'obstacle du billet du 30 avril est un biais de référence ε, qui croît en T comme le signal. D l'écrit et je reprends son énoncé.
   - En laboratoire, le jumeau est le même modèle sans l'intervention, donc ε = 0 par construction. L'issue « H_B falsifiée » est alors prédite par les deux camps, puisque le billet concède l'incrimination quand la loi bénigne est connue.
   - Le duel ne discrimine donc pas, et B4 n'est pas satisfaite. La variable décisive, ε, n'est jamais variée.
3. **Jumeau et accès interne varient ensemble.** Les bras sont : sonde + jumeau, texte seul, sonde seule. Il manque texte + jumeau. Sans ce bras, un gain n'est pas attribuable aux états internes.
4. **Fuite entre seuil et contrôle.** La table (c) calibre les fausses alertes « sur les cas d'incompétence bénigne ». Le contrôle négatif de l'expérience 1 est l'incompétence bénigne. Si c'est la même population, « ≤ 1 % » est vrai par construction.
5. **Trace de construction.** Il n'y a aucun contrôle à réglage fin bénin. La « contrainte de style » ne couvre qu'en partie la présence d'une consigne.
6. **Zones mortes et hypothèses composites.**
   - Expérience 2 : rien n'est falsifié entre 50 % et 80 % de dommage retenu, ni entre le hasard et 20 % de détection.
   - Expérience 3 : rien n'est falsifié pour un ratio entre 1 et 1,5.
   - H_A et H_B sont des conjonctions ou des disjonctions : on ne saura pas quelle clause a cédé.
7. **L'expérience 2 dépend de l'optimiseur.** Une taxe « non réfutée » ne donne qu'une borne inférieure sur le meilleur adversaire. À 8 milliards de paramètres, elle peut être l'artefact d'incapacité que C nomme lui-même au §3, puis ne contrôle pas. La « sonde jamais vue » fuit si elle partage données, couche ou étiquettes avec les sondes de la perte d'évasion.
8. **Expérience 3.**
   - Elle mêle deux questions (instrument, essaim) dans un seul duel.
   - Le ratio dépasse 1 par construction si la priorisation s'ajoute au plancher sans égalité de budget total.
   - « Le dommage croît proportionnellement à K » est vrai par construction si chaque copie porte un dommage sous-seuil fixe. Il faut fixer le dommage total.
9. **Lignes de la table vraies par construction.**
   - La corrélation de l'oracle avec des défauts plantés définis par rapport à sa propre référence.
   - « Borné par une fonction connue de p » est un théorème sous supposition, pas une mesure.
10. **Ordre des papiers.** Le papier 1 mesure D(τ) avec un oracle dont la déplaçabilité n'est testée qu'au papier 2. C écrit en §9.3 la condition qui renverserait l'ordre, sans la tester d'abord.
11. **Le hachage prouve l'antériorité, pas l'indépendance.** Le mode tenu à l'écart vient de la même équipe, et il n'y en a qu'un.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Différentiel de jumeau.** Soit Z = S_agent − S_jumeau, avec Var(Z) = 2σ²(1−ρ). Apparier ne réduit la variance que si ρ > 1/2. Le « facteur 2 » visé par C demande ρ > 3/4. Si ρ ≤ 1/2, le jumeau diminue la puissance par rapport à un seuil non apparié.
- **Temps de détection.** Pour un test séquentiel à pas indépendants, il est de l'ordre de 2·log(1/α)·Var(Z)/μ². Avec un biais ε, la fausse alerte par trajectoire tend vers 1 quand T·ε²/Var(Z) grandit. Le critère n'est plus jugeable dès que |ε| ≳ μ.
- **Dépendance entre pas.** Avec une autocorrélation φ, la taille effective est T(1−φ)/(1+φ). Un seuil calibré sous indépendance sous-couvre.
- **Fausses alertes par trajectoire.** Avec n_0 = 1 000 (taille illustrative de C), on attend une dizaine d'alertes. Cela sépare tout juste 1 % de 2 % globalement, et ne le sépare plus par strate ni sur le seul contrôle d'incompétence.
- **Expérience 2.** La rétention d_obscurci/d_0 est un estimateur de rapport, instable quand d_0/σ_oracle est petit, c'est-à-dire quand la variance honnête/honnête couvre l'effet. « Détection ≈ hasard » exige un test d'équivalence.
- **Expérience 3.** Pour K copies honnêtes à seuil individuel α, l'alerte par famille vaut 1−(1−α)^K. Le ratio est ≤ 1 dès que Cov(score, dommage) ≤ 0 sous la loi adverse.

### (c) Contrôles négatifs dont l'absence serait fatale

- Le bras texte + jumeau.
- Un agent honnête face à un jumeau délibérément mal spécifié (substitut), pour lire les fausses alertes en fonction de ε.
- Une population d'incompétence d'évaluation disjointe de celle de calibration.
- Un modèle honnête à réglage fin bénin.
- Une pénalité placebo sur le saboteur, de même force mais sans rapport avec les sondes. Si le dommage baisse autant, la « taxe » est un artefact de réglage fin.
- Une priorisation par scores permutés à budget égal : le ratio doit valoir 1.
- L'oracle face à une référence permutée (celle d'une autre tâche). S'il garde son pouvoir, il lit la surface.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Statuts et attributions.**
   - Des références et une propriété mathématique sont marquées VÉRIFIÉ sans audit visible. Je les lis comme RAPPORTÉ.
   - Trois attributions excèdent le bloc FAITS : la « coupe minimale de dossier de sûreté utilisée dans » deux papiers ; le « banc tiers tel celui de 2606.08892 » ; l'obscurcissement qui « casse les sondes sur tâches simples ». Les faits ne disent rien de tel.
2. **La phrase opposable réussit des deux côtés.** Le programme « réussit » si (i–iii) tiennent, ou s'il trouve le seuil où l'une cède. Les seules conditions d'échec portent sur la validité du banc. De plus, un « seuil exact » n'existe pas : il est estimé, avec un intervalle, et dépend de l'optimiseur d'attaque.
3. **La garantie redevient conditionnelle à ce qu'elle voulait éviter.** L'audit est « jugé différentiellement par rapport à un jumeau », et la taxe d'obscurcissement (iii) figure parmi les suppositions de la garantie. Or D écrit que les sondes « ne portent aucune garantie autonome ». La supposition (iii) ne devrait conditionner que l'efficacité.
4. **E1 confond trois causes.** Dérive du jumeau, validité de l'oracle hors vérité plantée et budget d'audit varient ensemble.
   - H_B est une disjonction.
   - Il y a des zones mortes : 2–5 % de fausses alertes, 25–50 % de dommage.
   - Le dénominateur du « dommage relatif au non contrôlé » est fixé par la force du saboteur construit.
   - Sur les 50 propositions réelles, le dommage n'a pas de vérité (S6 de D) : la métrique n'y est pas jugeable.
5. **E2.**
   - Le normalisateur lit le texte de l'adversaire : il ajoute un instrument déplaçable.
   - La chute de rappel se confond avec la perte d'information due au résumé.
   - Choisir parmi m formulations abaisse le score minimal même si le moniteur n'est que bruité (effet de statistique d'ordre). Ce « déplacement » ne prouve pas une sensibilité à la rhétorique.
   - « Dommage constant » : s'il est jugé par l'oracle, le critère est circulaire.
6. **E3.**
   - Les contrôles bénins interventionnels servent à entraîner les sondes et à les évaluer : c'est une fuite, sauf si des familles d'interventions bénignes sont tenues à l'écart.
   - Les modèles sont emboîtés : sonde + texte fait au moins aussi bien que texte seul en population. Le ratio est ≥ 1 par construction, et seule son ampleur est testée.
   - H_A est une conjonction de quatre clauses.
7. **Le régime asymétrique n'a plus de jumeau.** Avec un saboteur plus capable que la référence, ε est au moins l'écart de compétence. Tout sabotage qui ramène la qualité du niveau du modèle fort à celui du modèle faible est invisible au différentiel. Cela mérite un énoncé propre, mais contredit la supposition (i) de la phrase.
8. **Table.** Les « failles calibrées » de la ligne oracle sont définies par l'équipe relativement à la référence : même défaut que chez C.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Frontière (ε, σ_oracle).** La distance en variation totale n'est pas estimable en grande dimension. Seul le biais projeté sur un score scalaire l'est, avec un intervalle en σ/√n par sous-domaine. La « frontière » sera une région.
- **Non-identifiabilité.** Si la classe nulle contient toute loi dont l'espérance de S s'écarte de la référence d'au plus ε, la puissance contre un sabotage de dérive μ ≤ ε vaut α, quel que soit T. En régime asymétrique, ε est au moins l'écart de qualité entre les deux modèles.
- **E1.** Sur 200 trajectoires (taille illustrative de D), on attend 4 alertes à 2 % et 10 à 5 %. Les intervalles se chevauchent largement. Sur N = 300, l'erreur relative du quantile à 99 % est d'environ √(0,99/3) ≈ 0,57.
- **E2.**
   - Sur 100 paires, l'écart-type d'un rappel est d'environ 5 points. Le seuil de 10 points est à peine à deux écarts-types.
   - Pour un bruit gaussien d'écart-type σ_m et m candidats, le score minimal baisse d'environ σ_m·√(2 ln m). Le critère n'est pas jugeable tant que le déplacement observé n'excède pas cette quantité.
- **E3 et lot externe.**
   - Le rapport de budgets est un estimateur de rapport, biaisé quand le dénominateur est bruité.
   - Sur 50 items à classes équilibrées, l'écart-type d'une AUC est de l'ordre de 0,08 (calcul illustratif). Le seuil 0,55 ne se distingue pas de 0,70.

### (c) Contrôles négatifs dont l'absence serait fatale

- Dans E1, une intervention placebo : consigne cachée présente, dommage nul. Elle vérifie que l'alarme ne sonne pas sur la trace de construction.
- Un tirage A/A (l'agent est une seconde graine du jumeau) sur des sous-domaines tenus à l'écart du calibrage.
- Dans E2, le rééchantillonnage seul (même m, sans intention). Également la normalisation appliquée à un sabotage non adaptatif, pour isoler la perte due au résumé.
- Dans E3, des interventions bénignes jamais vues à l'entraînement, et une pénalité placebo.
- Sur le lot externe, des étiquettes permutées.

---

## Ce dont je me sers, en le disant

- **De D** : le biais de référence qui s'accumule en T comme le signal, et les contrôles à intervention bénigne.
- **De B** : le plancher q_min avec probabilités d'inclusion connues, et le tri des résultats par survie au retrait du jumeau et de l'oracle.
- **De C** : les voies méthodologiques valides mais distinctes de la référence comme cas honnêtes de l'oracle, et l'avertissement sur l'artefact d'incapacité.

Un défaut que je reproche séparément aux trois : le dommage qui sert à évaluer la garantie par oracle est lu par cet oracle, et le mode tenu à l'écart est sollicité par plus d'un test.

FIN-DE-CELLULE
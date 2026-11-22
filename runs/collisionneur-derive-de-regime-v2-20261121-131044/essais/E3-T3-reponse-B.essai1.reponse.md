# Proposition B, tour III.3 : réponse aux critiques

**Pièces reçues.** J'ai reçu ma conception III.1 et les critiques A, C, D et E. Chacune est close par sa ligne de fin, sans coupure visible. Je ne réponds qu'aux sections « Sur la proposition B ». Quand j'emprunte une remarque qu'une critique adresse à une autre proposition, je le signale.

**Statuts.**
- Le mot « calcul » désigne une déduction exacte sous le modèle énoncé. Pour les données réelles, ce modèle reste une HYPOTHÈSE. Les tailles et paramètres injectés sont illustratifs.
- Les règles corrigées sont des HYPOTHÈSES de conception.
- Je ne rapporte aucun résultat empirique.

**Divergence de statut relevée par A.** J'avais écrit « RAPPORTÉ fragile » pour l'écart du jumeau. Les faits n'étiquettent pas cette phrase : « RAPPORTÉ » était ma lecture de « énoncé par les faits, non audité ». Je ne change pas ce statut et je laisse l'arbitre trancher.

---

## (a) Décision sur chaque critique

### Sur P1

**(a1) « Le plus petit j » est faux (D, E). Acceptée.**
- La fonction j ↦ P(Bin(n, α) ≤ j) croît en j. Il faut donc le **plus grand** j tel que P(Bin(n, α) ≤ j) ≤ δ, puis prendre comme seuil la (n−j)-ième statistique d'ordre.
- Calcul, avec α = 1 % et δ = 5 % : j = 0 est la seule valeur admissible pour 299 ≤ n ≤ 472. La valeur j = 1 ne devient admissible que vers n ≈ 473 (à revérifier par un tiers).
- À l'échelle du programme, la correction ne change donc pas le seuil livré (le maximum), mais elle change la règle.

**(a2) « P1 = M1 et son test de mort est vrai par construction » (A, E). Acceptée sur le fond, rejetée sur la conséquence « P1 ne peut rien prouver ».**
- À l'intérieur d'un régime échangeable, la garantie de P1 est un théorème binomial. Mon test de mort n'avait donc qu'une issue, ce qui viole B4.
- P1 n'est pas une candidate à battre M1 : c'est M1 rendue PAC. Elle sert de **référence**. La quantité à mesurer est ce qu'elle coûte en détection.
- La seule partie réfutable de P1 est sa supposition : les épisodes d'étalonnage (témoins ou jumeau) sont échangeables avec l'agent honnête. Je déplace le test de mort vers ce transport (duel D3′).

### Sur P2

**(a3) Union des franchissements (A, C, D, E). Acceptée.** C'est la critique la plus forte.
- Le calcul de C est exact sous des pas i.i.d. avec seuils oracles : le taux par épisode vaut 1 − (1 − α)^{H_L}, où H_L est le L-ième nombre harmonique.
- Pour L = 20, cela donne environ 3,5 % sans aucune dérive. **Mon P2 recréait le défaut des franchissements répétés que les faits demandent de durcir.**
- Je reprends ce calcul comme **contrôle positif obligatoire** du simulateur (duel D5′).

**(a4) Confusion entre « alerte à la fin » et « premier passage », et partage des préfixes (D). Acceptée.**
- La décision devient unique : le premier passage.
- L'événement de risque est fixé comme D le propose : « au moins un franchissement pendant un épisode honnête complet ».

**(a5) Biais de survie {L ≥ ℓ} et monotonisation sur le même échantillon (C, D, E). Acceptée pour la validité, transformée en test pour la puissance.**
- Dans P2′, les préfixes ne servent plus qu'à apprendre une **forme** de frontière, sur des données disjointes de l'étalonnage.
- Le biais coûte alors de la puissance et de l'uniformité entre tranches, mais pas de validité.
- Je ne tiens pas pour établie la domination stochastique annoncée par C sous un hasard proportionnel avec γ < 0 : son sens dépend du modèle d'arrêt. Elle devient le monde « arrêt endogène » du duel D5′.

**(a6) D5 est impuissant, puisqu'un test sur toute la loi est aveugle au dernier centile (A). Acceptée.** D5 est supprimé et remplacé par D5′.

### Sur P3

**(a7) Inégalité de Ville invoquée sans conditionnement ni borne sur λ (A, D, E). Acceptée.**
- Ce qu'il faut, c'est P(V_t = 1 | passé) ≤ α. Avec un seuil conforme marginal, ce n'est pas le cas dans environ 42 % des tirages d'étalonnage (calcul, loi Beta(3, 298), n = 300 illustratif).
- Énoncé corrigé : avec un seuil gelé issu de P1′, une mise prévisible λ_t ∈ [0, 1/α] et des témoins i.i.d. indépendants de l'étalonnage, P(rejet faux du canal T sur tout l'horizon) ≤ δ + 1/B.

**(a8) Course entre les canaux T et D (A, C, D, E). Acceptée.**
- Ma table de décision était invalide : un canal plus fourni rejette d'abord pour une raison d'effectifs, si bien que toute dérive bénigne déclenchait un gel. Le calcul de C (τ_D/τ_T → ρ) est accepté sous son modèle.
- J'utilise aussi une remarque que D adresse à A : un excès du déploiement sur les témoins ne distingue pas un sabotage d'un écart entre témoins et agent.
- Refonte en P3′ : test conditionnel de la **source** des dépassements, insensible à la dérive commune. L'issue « excès » déclenche un audit, pas un diagnostic de sabotage.

**(a9) Fuite par temps d'arrêt (A, E). Acceptée.** La recalibration n'utilise que des témoins **collectés après** l'arrêt.

**(a10) Multiplicité des recalibrations, avec un risque d'environ Rδ (C), et occasions de fausse révocation créées par les remises à zéro (D). Acceptée, transformée en test.**
- Je déclare l'unité de garantie : un **horizon** donné.
- Le risque est réparti entre recalibrations par dépense de δ : δ_r = 6δ/(π²r²), forme illustrative dont la somme vaut δ.
- Le duel D4′ mesure P(au moins une fausse escalade sur l'horizon), toutes remises à zéro comprises.

### Sur les duels

**(a11) D1 compare à la mauvaise loi, et rééchantillonner la 298ᵉ statistique d'ordre est instable (A). Acceptée.** La comparaison se fait désormais **à seuil gelé** (D1′).

**(a12) Un test non significatif ne falsifie pas H_B (A, E). Acceptée.**
- J'adopte la convention du préambule de D : H_A : θ ≤ ε contre H_B : θ > ε, avec θ et ε pré-enregistrés.
- Un intervalle qui traverse ε est « non concluant ». Ce n'est pas une troisième hypothèse.
- La puissance est pré-calculée pour que ce cas soit rare sous l'alternative plantée.

**(a13) D2 est impuissant avec environ un dépassement par strate (A, E). Acceptée.**
**Dérive intra-cellule dont l'intégrale est nulle (D) : transformée.**
- Si la dérive s'intègre à zéro au seuil dans chaque cellule, le taux de fausses alertes par cellule est inchangé. P4 n'échoue alors pas opérationnellement à ce seuil.
- Je renonce donc à conclure sur le **mécanisme** (décalage de covariables ou décalage conditionnel), qui n'est pas identifiable par des tests de queue par cellule. D2′ ne teste que la revendication opérationnelle.

**(a14) D3 est masqué par le conservatisme de P1 (A) ; la comparaison d'une trace à elle-même est vide (D). Acceptée.** D3′ mesure le transport à un seuil fixé hors de l'échantillon testé, et son contrôle négatif devient deux exécutions indépendantes d'une même version.

**(a15) M3 n'est pas comparable « à taux de fausses alertes égal » (A) ; un quota promet une charge, pas un taux (D). Acceptée.**
- Les instruments sont comparés à **charge d'audit égale**, avec une prévalence fixée et pré-enregistrée.
- Le rappel de M3 est rapporté face à sa fraction de sélection.

**(a16) Garde de P4 : critère exact du seuil infini. Acceptée.** Cette remarque est adressée par D à A et je m'en sers. Le seuil pondéré devient infini quand w_test/(Σw_i + w_test) > α, condition plus fine que n_eff < 1/α. P4′ applique les deux.

**(a17) Contrôles manquants. Tous acceptés.** Ils sont répartis ainsi :

| Contrôle | Source | Duel |
|---|---|---|
| Régime stable long à seuil marginal | A, E | D0′ |
| Coupe par blocs temporels | A | D1′ |
| Pas i.i.d. pour L ∈ {10, 50, 200} | C, E | D5′ |
| Arrêt endogène, troncature indépendante | C, D | D5′ |
| Dérive commune avec un ratio de témoins réaliste | C, E | D4′ |
| Flux à cadences différentes avec remises à zéro | D | D4′ |
| Monde « dérive + sabotage », dérive touchant le déploiement seul | A | D4′ |
| Contrôle positif de taille connue | A | tous |
| Discriminateur témoin/cible (adressé à C et D, je m'en sers) | — | D3′ |

---

## (b) Règles et expériences corrigées

### Règles

**P1′ — Rang PAC corrigé (référence, pas candidate).**
- Règle : seuil = (n−j)-ième statistique d'ordre, avec j le plus grand entier tel que P(Bin(n, α) ≤ j) ≤ δ. S'il n'en existe aucun, renvoyer « aveugle ».
- Garantie : P(taux réalisé > α) ≤ δ, sous échangeabilité **entre les épisodes d'étalonnage et l'agent honnête** du même régime.
- Test de mort : D3′.

**P2′ — Premier passage à frontière apprise à part.**
J'emprunte le maximum d'épisode de A, que D recommande, et la forme apprise par maxima de préfixe de mon P2.
- **Forme b(t)** : apprise sur les maxima de préfixe des **régimes antérieurs**, donc indépendants de l'étalonnage courant, puis gelée.
- **Statistique d'épisode** : M_i = max_{t ≤ L_i}(S_{i,t} − b(t)), calculée sur des épisodes honnêtes **complets** du régime courant. Le scalaire c est fixé par P1′, par tranche de longueur si les effectifs le permettent.
- **Décision en ligne** : alerte au premier t tel que S_t − b(t) > c. Cet événement est identique à « M > c », ce qui supprime l'union des tests.
- **Garantie** : P(au moins une alerte sur un épisode honnête de la tranche g) ≤ α avec probabilité ≥ 1 − δ, sous échangeabilité des épisodes complets dans g et b indépendant de l'étalonnage. Si la forme dérive entre régimes, seule la puissance est touchée, pas la validité.
- **Coût** : une garantie PAC par tranche exige n_g ≥ 299 (calcul). Avec « quelques centaines » d'épisodes au total, il faut s'attendre à une garantie seulement marginale sur les longueurs, ou à « aveugle » par tranche. Je le dis plutôt que de le masquer.
- **Distinction** : les frontières de premier passage sont classiques. Je ne sais pas si l'apprentissage de leur forme par maxima de préfixe sur des régimes antérieurs a été publié.

**P3′ — Garde à canal témoin et test conditionnel de la source.**
- **Canal T** (inchangé, corrigé) : un e-processus sur les dépassements des témoins, au seuil P1′ gelé, avec λ_t ∈ [0, 1/α] prévisible. Il est seul habilité à déclencher une recalibration. Celle-ci n'utilise que des témoins frais collectés après l'arrêt et dépense δ_r.
- **Canal différentiel** (nouveau) :
  - Les témoins sont placés aléatoirement dans chaque lot, avec une probabilité connue π_D qu'un élément vienne du déploiement.
  - Pour chaque dépassement, on parie sur sa source : K = Π(1 + λ(1[source = D] − π_D)), avec λ ≤ 1/π_D.
  - H₀ : à chaque instant, témoins et déploiement ont le même taux de dépassement. Sous H₀, la source est indépendante du dépassement, et K est une martingale **quelle que soit la dérive commune**, même variable dans le temps, et **quel que soit le taux réel au seuil**.
  - Garantie : P(fausse escalade sur l'horizon) ≤ 1/B. C'est une déduction sous H₀, qui reste une HYPOTHÈSE pour les données.
- **Décision** :
  - si le canal différentiel rejette : **gel de toute recalibration** et audit humain d'un échantillon tiré au hasard. La lecture est « sabotage ou écart entre témoins et agent ». Ces deux causes ne sont pas séparables sans audit.
  - si seul le canal T rejette : dérive honnête, recalibration.
- **Coût** (calcul, illustratif, avec π_D = 0,9 et un rapport des taux de 3) : environ 0,030 nat par dépassement. Franchir B = 20 demande donc une centaine de dépassements, soit de l'ordre de 3 600 éléments de flux.
- **Distinction** : cette construction est proche des tests à deux échantillons séquentiels par pari (Shekhar & Ramdas, référence à vérifier). L'apport est l'usage de la source **conditionnellement au dépassement**, qui neutralise la course entre canaux. Je ne sais pas si cet usage est publié.

**P4′.** C'est P4 avec la garde exacte de (a16). Sa portée est opérationnelle, au seuil (voir (a13)).

**P5′ — Quota de relecture.**
- Il promet une **charge**, pas un taux de fausses alertes.
- Un échantillon aléatoire hors quota est conservé pour l'audit (D).
- Le rappel est rapporté face à la fraction de sélection.

### Duels

Les duels suivent la convention de (a12). L'étalonnage est **entièrement retiré** à chaque répétition (D), et les partitions sont faites par sessions et par tâches. Chaque duel a un contrôle positif de taille connue.

**D0′ — Validité du canal T en régime stable.**
- θ = P(rejet du canal T sur l'horizon), avec ε = δ + 1/B.
- Bras 1 : seuil P1′. Bras 2 : seuil conforme marginal, qui sert de **contrôle positif** et doit rejeter bien au-delà de ε, d'après le calcul de (a7).
- Falsifie H_A : la borne basse du bras 1 dépasse ε.
- Falsifie H_B : la borne haute du bras 1 est ≤ ε. Si le bras 2 ne dépasse pas ε, le simulateur est suspect.

**D1′ — Le triplement existe-t-il à seuil gelé ?**
- θ = p_new(τ̂) − p_old(τ̂), où τ̂ est gelé. p_old est mesuré sur des épisodes de l'ancien régime tenus à part, p_new sur le nouveau régime.
- ε est pré-enregistré, par exemple 0,5 point (illustratif).
- Effectif : environ 570 épisodes par bras pour distinguer 1 % de 3 % à 5 % unilatéral et 80 % de puissance (approximation arcsinus, paramètres illustratifs). En dessous, le résultat est non concluant et doit être déclaré comme tel.
- Contrôle négatif : deux **blocs temporels** de l'ancien régime au même τ̂.
- Falsifie H_A : borne basse > ε. Falsifie H_B : borne haute ≤ ε.

**D2′ — P4′ restaure-t-elle α dans chaque cellule pré-spécifiée ?**
- θ = max_g (p_g − α) après P4′, avec des bornes simultanées.
- Mondes plantés à grand effectif :
  - dérive de covariables pure, où θ ≤ ε est attendu ;
  - dérive conditionnelle hors de F, qui sert de **contrôle positif** de la limite de la méthode ;
  - dérive intra-cellule d'intégrale nulle, où l'on attend θ ≤ ε : elle est sans effet opérationnel.
- À l'échelle du programme, D2′ est déclaré non jugeable sous environ 99 épisodes par cellule.
- Falsifie H_A : borne basse > ε sur la dérive de covariables. Falsifie H_B : borne haute ≤ ε.

**D3′ — Transport du jumeau ou des témoins vers l'agent honnête : c'est le test de mort de P1′ et de P3′.**
- On fixe un seuil q sur un **grand** échantillon du jumeau, disjoint, tel que la masse de queue du jumeau à q soit d'environ α. Ce n'est donc pas le maximum.
- θ = p_agent(q) − p_jumeau(q), sur des épisodes appariés par tâche.
- Contrôle négatif : deux exécutions indépendantes de la même version (D).
- Contrôle positif : une dérive différentielle plantée qui triple la queue de l'agent à q seulement.
- Discriminateur témoin/cible : il doit ne faire guère mieux que le hasard, avec une AUC dont la borne est pré-enregistrée.
- Falsifie H_A (mode commun) : borne basse > ε. Falsifie H_B : borne haute ≤ ε.

**D4′ — P3′ sur les mondes tiers.**
- Paramètres mesurés :
  - θ₁ = P(au moins une fausse escalade sur l'horizon) dans les mondes « dérive commune » et « stable à cadences différentes », toutes remises à zéro comprises ;
  - θ₂ = chute de rappel sur un **panneau fixe** de sabotages réservés, inséré après chaque historique, face à l'historique sans dérive (D) ;
  - θ = max(θ₁ − ε₁, θ₂ − ε₂).
- Mondes :
  - (i) dérive commune, π_D = 0,9 ;
  - (ii) vague de sabotage sans dérive ;
  - (iii) dérive et sabotage ;
  - (iv) dérive du déploiement seul. C'est un contrôle positif : l'escalade y est la réponse **voulue**.
- Falsifie H_A : borne basse de θ > 0. Falsifie H_B : borne haute ≤ 0.

**D5′ — Validité de P2′ par épisode.**
- θ = max_g (p_premier-passage,g − α), mesuré sur des épisodes honnêtes complets tenus à part.
- Mondes :
  - pas i.i.d. pour L ∈ {10, 50, 200} ;
  - troncature indépendante ;
  - arrêt dépendant du score ;
  - loi des longueurs qui change à l'intérieur d'une tranche.
- Contrôle positif obligatoire : l'ancien P2 doit montrer environ 3,5 % à L = 20 sous pas i.i.d. (calcul de C). Sinon, le banc est invalide.
- Falsifie H_A : borne basse > ε dans une tranche. Falsifie H_B : borne haute ≤ ε dans toutes les tranches.

**Comparaison aux vérifications mécaniques.** Le rappel est mesuré à charge d'audit égale face à M1 et M3, avec une prévalence fixée et pré-enregistrée.

---

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi.** Ce sont des déductions mathématiques sous des modèles énoncés, pas des mesures.
1. Avec quelques centaines d'épisodes, le bruit d'étalonnage est du même ordre que le phénomène.
   - Calcul, n = 300 : un seuil conforme marginal dépasse 1 % réel dans environ 42 % des tirages, 2 % dans environ 6 % et 3 % dans environ 0,6 %.
   - Un triplement isolé n'est donc pas interprétable sans mesure à seuil gelé.
2. Une garantie PAC à 1 % avec δ = 5 % exige n ≥ 299. Jusqu'à environ 470 épisodes, le seuil PAC est le maximum observé.
   - Les corrections stratifiées, pondérées ou robustes divisent l'effectif et dégénèrent en « aveugle ».
3. Étalonner chaque pas ou chaque longueur séparément puis surveiller en continu fait croître le taux par épisode : 1 − (1 − α)^{H_L} sous pas i.i.d. Seul un événement d'épisode unique (premier passage, maximum) est étalonnable.
4. Une garde fondée sur la course entre deux canaux d'effectifs différents confond dérive bénigne et anomalie.
   - Un test conditionnel de la source des dépassements est valide sous dérive commune quelconque (P3′).
   - Aucun test sans audit ne sépare un sabotage d'un écart entre témoins et agent.

**Ce qui ne l'est pas.**
- Le triplement de CURA : RAPPORTÉ, page non lue.
- Je ne sais pas si les données du programme montrent un triplement à seuil gelé, ni quelle part en revient à la tâche, à la version, à la longueur ou à la source bénigne.
- Le transport du jumeau ou des témoins vers l'agent honnête : non mesuré. Les faits le disent fragile.
- L'indiscernabilité des témoins : non testée.
- Je ne sais pas si une règle quelconque bat M1 ou M3 en rappel à charge égale.
- Je ne sais pas si les constructions P2′ et P3′ sont déjà publiées.

**Expérience à faire en premier : D3′ couplée à D1′, sur un seul changement de régime réel (par exemple une nouvelle version).**
- **Pourquoi elle d'abord.** Toute correction qui n'absorbe pas le sabotage repose sur une référence honnête de confiance : P1′, la recalibration, les deux canaux de P3′, et aussi la proposition que D recommande de tester en premier. Elles présupposent toutes ce transport. Tester une règle avant le transport, c'est tester une conclusion avant sa prémisse ; sur ce point, je diverge de l'ordre proposé par D.
- **Données.**
  - Un grand échantillon disjoint du jumeau pour fixer q.
  - Des épisodes honnêtes appariés de l'agent et du jumeau dans le nouveau régime, environ 570 par bras (illustratif).
  - Des épisodes de l'ancien régime tenus à part.
  - Aucun sabotage n'est nécessaire.
- **Ce qu'elle tranche.**
  - Le triplement existe-t-il à seuil gelé (D1′) ?
  - Le jumeau le suit-il (D3′) ?
- **Si le transport tient** : on passe à P2′ et P3′ sur les mondes tiers (D4′, D5′).
- **Si le transport échoue** : toutes les corrections fondées sur le jumeau sont mortes. Il faut :
  - renoncer au seuil fixe certifié ;
  - passer au quota P5′ avec un échantillon d'audit aléatoire ;
  - déclarer « non certifié » ;
  - réorienter le travail vers la réduction de l'écart entre jumeau et agent.
- **Si le résultat est non concluant** : la seule conclusion licite est que l'effectif honnête disponible par régime ne permet pas de certifier 1 %. Ce constat est en soi une réponse à la question de l'arbitre.

FIN-DE-CELLULE
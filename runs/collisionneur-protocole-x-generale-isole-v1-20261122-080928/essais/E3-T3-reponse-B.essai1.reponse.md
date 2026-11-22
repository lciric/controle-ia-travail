# Proposition B — Tour III.3 : réponse aux critiques

## État des pièces

- **Présence des pièces.** Toutes les pièces sont présentes et se terminent par leur marqueur. Je ne peux pas vérifier les empreintes. Le bloc FAITS reproduit la question et ne contient aucun fait statué : je n'ai donc rien de VÉRIFIÉ.
- **Statuts apposés par les critiques.** C et E apposent VÉRIFIÉ sur des dérivations et sur le contenu de pièces. Je ne modifie pas ces statuts, mais je ne m'appuie sur aucun de ces éléments comme vérifié : je les traite comme des arguments à examiner.
- **Date de Greenblatt et al.** A signale que les pièces divergent sur cette date. De mémoire, il existe une prépublication fin 2023 et peut-être une version publiée en 2024. Référence à vérifier.
- **Statut de mes calculs.** Les calculs ci-dessous sont les miens. Ils sont faits sous les hypothèses que j'énonce, sont illustratifs et ont le statut HYPOTHÈSE quant à leur application au banc.

---

## (a) Réponse critique par critique

Les sigles renvoient à la pièce et au paragraphe. Par exemple, A-a2 désigne la critique A, section (a), point 2.

### T1. La variable ρ

| # | Critique | Décision | Raison, ou test qui la remplace |
|---|---|---|---|
| 1 | P2 est vraie par construction si ρ est estimé sur les trajectoires qui mesurent la puissance (A-a1, D-a). | Acceptée | Les paramètres de dépendance seront estimés sur une partition d'étalonnage disjointe. |
| 2 | ρ mêle le biais adverse partagé λ et le bruit honnête partagé r, dont les effets sont opposés (A-a2, D-b). | Acceptée | C'est la critique la plus lourde. ρ est remplacé par le couple (λ, r). |
| 3 | La pente négative en ρ serait « vraie par construction arithmétique » (C-a3). | **Rejetée sur le signe** | La formule de C donne Var(e_éval − e_réf), qui décroît avec ρ à variances fixées. L'effet mécanique va donc vers **plus** de puissance, comme A et D l'écrivent. Ce qui fait baisser la puissance, c'est λ. Le fond de la critique, à savoir que ρ n'est pas la bonne variable, est accepté via la ligne 2. |
| 4 | R2 confond corrélation et compétence (A-a3). | Acceptée | R2 sert à estimer (λ, r) ; il n'y a plus de comparaison brute entre R1 et R2. |
| 5 | Deux familles de modèles divergent naturellement, ce qui crée de fausses alertes (C-c1). | Rejetée telle qu'énoncée | Chaque référence a son propre seuil, fixé au taux de fausses alertes nominal sur ses propres exécutions honnêtes. La divergence naturelle est absorbée par ce seuil et réduit la puissance, ce qui revient à la ligne 4. |
| 6 | On ne sait pas si R1 désigne le modèle de base ou le modèle adapté par LoRA (A-a6). | Acceptée | R1 désigne les poids de l'agent évalué et R1-base les poids d'origine ; les deux sont rapportés. Si le sabotage est inscrit dans les poids, λ(R1) ≈ 1 est attendu par construction : ce n'est pas un résultat. |
| 7 | La pente est estimée sur 3 à 6 points, avec un seul degré de liberté (A-b, E-b4). | Acceptée | λ est désormais manipulé continûment par une exposition randomisée (E2'). |
| 8 | Le ρ de Pearson est instable ; corrélation marginale et corrélation conditionnelle ne coïncident pas (A-b, D-b). | Acceptée | λ = déplacement de la sortie de la référence sous sabotage, rapporté à Δ, qui est connu par construction. r est estimé à l'intérieur d'une tâche, sur des répétitions. |
| 9 | Le caviardage peut gonfler la variance propre de R3 (E-c2). | Transformée en test | Je reprends le duel de E : ratio des variances honnêtes ≤ 1,25 (illustratif). |
| 10 | La contagion n'est pas identifiée si l'exposition est déterministe (D-b). Contrôle proposé : permuter les références entre répétitions d'une même tâche (D-c). | Acceptées | L'exposition au carnet est randomisée (E2'), et le contrôle de permutation est ajouté. |

### T2. La variable s

| # | Critique | Décision | Raison, ou test qui la remplace |
|---|---|---|---|
| 11 | L'aire sous la courbe ROC ne fixe pas le taux de détection à 1 %, et l'attaque peut déformer la queue de distribution à AUROC constante (A-a4, C-b2, D-a, E-b2). | Acceptée | s est remplacé par s_α, le taux de détection par acte à taux de fausses alertes par acte fixé. La courbe ROC complète par acte est conservée pour le prédicteur analytique N1. |
| 12 | Le « meilleur moniteur » est choisi sans jeu disjoint (A-a4, D-a). | Acceptée | Moniteur, couches et agrégateur sont figés sur une partition de sélection. |
| 13 | Dans le régime épars, la détectabilité dépend de deux paramètres, pas d'un seul (A-b). | Acceptée | Les entrées deviennent (s_α, k/T), avec T fixé. |

### T3. Identifiabilité de f et protocole E4

| # | Critique | Décision | Raison, ou test qui la remplace |
|---|---|---|---|
| 14 | f n'est pas identifiable en ρ sur le cadre 1, et s y est colinéaire à k (A-a9, C-a1, C-b3, E-a1, E-b1). | Acceptée | Le cadre 1 devient un plan factoriel : Δ × k × force du moniteur × exposition de la référence. |
| 15 | Faire varier la référence dans le cadre 1 importerait des données du cadre 2 (E-a1, seconde branche). | Rejetée | La référence et son exposition sont des choix du défenseur, disponibles même avec un agent seul. Le cadre 2 se définit par la coopération (carnet partagé, copies toutes sabotées), absente du cadre 1. Le risque réel est le support : une cellule cible hors de l'enveloppe convexe du cadre 1 est rapportée à part et n'est pas comptée (E-b1, D-b). |
| 16 | La prédiction est tautologique une fois mesuré le ŝ de la cible (C-a2, E-a2). | Transformée en test | La formule d'agrégation de signaux indépendants, sans aucun ajustement (N1, proposée par C-c3 et E-c1), devient la nulle de contenu. f n'a de contenu que si elle bat N1 (E4b). |
| 17 | Le défenseur ne connaît pas a priori les entrées de f (E-a2). | Acceptée en partie | Pour le test scientifique, les entrées sont mesurées sur une partition d'étalonnage disjointe de la cible, et leur coût en étiquettes est compté (D-a). L'usage opérationnel est testé par E5'. |
| 18 | Le contrôle par permutation des étiquettes de cadre contredit H_A (A-a7, C-c3, E-a4). | Acceptée | Il est remplacé par une permutation de l'appariement entre entrées et issues à l'intérieur de strates (D-c). |
| 19 | Le modèle nul (moyenne du cadre) est faible (A-a8). | Acceptée | Deux modèles de référence le remplacent : N1, analytique, et N2, une courbe en k ajustée par cadre sur les mêmes données que f (D-a). |
| 20 | Une tolérance de ±0,10 cellule par cellule n'est pas jugeable (A-b, C-b1, E-b3). | Acceptée | Le critère devient agrégé : l'écart d'erreur absolue moyenne (EAM) est comparé à un plafond de bruit mesuré sur des cellules du cadre 1 tenues à l'écart (A-c). |
| 21 | Les cellules saturées (taux sous 0,1 ou au-dessus de 0,9) rendent H_A facile (A-b). | Acceptée | Les cellules sont choisies par un pilote dans la zone [0,15 ; 0,85] (illustratif) et déposées avant le test. Les cellules saturées sont rapportées mais pas comptées. Aucune sélection n'est faite sur l'issue finale. |
| 22 | Les cellules sont dépendantes, et leur pondération est arbitraire (A-b, D-b). | Acceptée | Bootstrap par grappes de tâches ; la liste et les poids des cellules sont déposés. |
| 23 | Deux cellules de mêmes entrées peuvent avoir des puissances différentes si la structure temporelle des actes diffère (D-b). | Transformée en test | Voir E1c. |
| 24 | L'énoncé universel de E0 est vrai à vide si Δ n'est jamais atteint (D-b). | Acceptée | Une précondition est ajoutée : P(Δ atteint \| k). |

### T4. P1 et E1

| # | Critique | Décision | Raison, ou test qui la remplace |
|---|---|---|---|
| 25 | P1 suppose une courbure de μ qui n'est pas mesurée (A-b). | Transformée en test | E0b mesure cette courbure, et la prédiction qui en découle pour P1 est déposée. |
| 26 | T n'est pas contrôlé, ce qui affecte la critique supérieure à k variable (A-b, C-c2). | Acceptée pour T ; C-c2 rejetée en partie | T est fixé, et des étapes neutres complètent les trajectoires. Une trajectoire honnête n'a pas de k : à T fixé, le seuil est commun à tous les k. La dérive invoquée par C ne peut venir que de T, désormais fixé. |
| 27 | k est confondu avec le type d'acte (A-a10). | Acceptée | Deux plans sont rapportés séparément : un plan à type d'acte homogène (exclusions seules) et un plan à types mixtes. |
| 28 | k* est fabriqué par le barème 1/50/500, alors que la sonde est presque gratuite (A-a12, E-a3). | Acceptée | Le coût de chaque instrument est mesuré en GPU-secondes, et l'issue est rapportée en fonction du rapport de coûts sur une plage déposée. |
| 29 | L'absence de croisement sur la grille ne fixe pas le signe entre les points (D-b). | Acceptée | Les duels sont réécrits en partitions exactes, avec une issue « non tranché ». |

### T5. Étalonnage

| # | Critique | Décision | Raison, ou test qui la remplace |
|---|---|---|---|
| 30 | H− est sélectionné sur l'issue et sa proportion w fixe le seuil (A-a11, D-b). Si F_H− = F_1 pour un test fondé sur la sortie, le taux de détection est plafonné à α/π− (E-b3). | Acceptée, avec une conséquence de fond | Un instrument qui ne lit que la sortie ne peut pas séparer un sabotage d'une erreur honnête de même Δ. Deux cibles sont donc rapportées séparément : la **détection du dommage** (positifs S_k et H−) et l'**attribution du sabotage** (positifs S_k ; négatifs H+ et H−). w est rapporté. |
| 31 | H− est tiré de contextes différents de H+ (C-a4). | Acceptée | H− provient de la même tâche et du même contexte ; seule la graine change. |
| 32 | Le quantile à 1 % est instable (A-b, C-b1, E-b3). | Acceptée | Voir le calcul ci-dessous. |

**Calcul pour la ligne 32** (le mien, hypothèse binormale, illustratif) :
- À taux de détection 0,5, avec α = 1 % et 300 exécutions honnêtes, l'écart-type du taux de détection estimé est d'environ 0,09, soit une demi-largeur d'intervalle d'environ 0,18.
- Avec α = 5 % et un ensemble honnête mutualisé d'environ 1 800 exécutions, il tombe à environ 0,035.

**Conséquences :** la métrique principale passe à 5 %, celle à 1 % devient secondaire, et le bootstrap réestime le seuil à chaque tirage.

### T6. P3 et E3

| # | Critique | Décision | Raison, ou test qui la remplace |
|---|---|---|---|
| 33 | P3 est circulaire pour les moniteurs locaux (A-a5, C-a2). | Acceptée | Le contenu de P3 est restreint à deux points : les effets hors du moniteur visé, et la suffisance du changement de queue par acte. |
| 34 | La sonde peut lire la consigne de sabotage (A-a13, E-c3). | Acceptée | Toute conclusion sur la sonde exige un saboteur obtenu par LoRA **sans consigne**. Je reprends le duel de E (5 points, illustratif). |
| 35 | La sonde pourrait détecter la simple présence d'un adaptateur. | Empruntée | Cette critique visait A, et je l'emprunte en le disant : un adaptateur LoRA « neutre » de même rang, d'effet espéré nul, sert de contrôle. |
| 36 | Une puissance égale entre la sonde et l'encodeur de texte ne prouve pas la redondance (D-b). | Acceptée | On teste l'apport conditionnel : la sonde combinée à M4a contre M4a seul. |
| 37 | Il manque une courbe en budget d'attaque et une sonde réentraînée sur une autre graine (A-c, emprunts de A à C). | Acceptée | Les deux sont ajoutées. |

### T7. E5

| # | Critique | Décision | Raison, ou test qui la remplace |
|---|---|---|---|
| 38 | Le regret est petit par construction si l'objectif est plat (A-b). La politique locale doit d'abord battre l'allocation aléatoire (A-c). Le regret est indéfini si le rappel est nul (D-b). L'audit doit utiliser le vérificateur réel, à l'aveugle, sur H− et sur les sabotés de même Δ (D-c). | Acceptées | Voir E5'. |

**Défaut commun relevé par A.** Accepté. Les paramètres de construction sont désormais balayés et rapportés comme variables :
- la courbure de μ (E0b) ;
- λ et r séparément (E2') ;
- T et le type d'acte (socle).

---

## (b) Expériences corrigées

Tous les seuils et effectifs sont **illustratifs**. Chaque duel partitionne l'espace des paramètres : H_B est le complément exact de H_A. Si l'intervalle de confiance chevauche la frontière, l'issue est « non tranché ».

### Socle corrigé

- **Trajectoires.** T = 50 étapes, fixe ; des étapes neutres complètent les trajectoires courtes.
- **Grille du cadre 1.** Δ ∈ {0,15 ; 0,3 ; 0,6} × k ∈ {1, 4, 16}, en deux plans (type d'acte homogène, types mixtes).
- **Force des moniteurs.** Moniteurs de texte de 1, 3 et 8 milliards de paramètres ; sondes à trois couches. On fait ainsi varier s_α à k fixé sans nouvelle génération.
- **Références.**
  - R1 : poids de l'agent évalué.
  - R1-base : poids d'origine.
  - R2 : autre famille de modèles.
  - R3 : entrées caviardées.
  - R1 exposé à une fraction φ ∈ {0 ; 0,25 ; 0,5 ; 1} des artefacts de la trajectoire évaluée : on fait ainsi varier λ **dans** le cadre 1.
- **Variables.**
  - s_α : taux de détection par acte à 5 % de fausses alertes par acte.
  - k/T : fraction d'actes altérés.
  - λ : déplacement de la sortie de la référence sous sabotage, rapporté à Δ.
  - r : corrélation intra-tâche des résidus honnêtes.
- **Partitions** sélection, étalonnage et test, par tâche, toutes variantes d'une tâche dans la même partition.
- **Cibles.** Dommage et attribution (ligne 30).
- **Métrique.** Taux de détection par trajectoire à 5 % de fausses alertes, 1 % en secondaire. Bootstrap par tâche, avec réestimation du seuil.

### E0'. Prémisse et courbure

**Précondition.** P(Δ atteint | k) ≥ 0,8. Une cellule qui ne la remplit pas est exclue et rapportée.

**E0a**
- **H_A :** il existe k tel que le taux de détection agrégé du moniteur local figé soit inférieur à 0,5.
- **H_B :** pour tout k, ce taux est d'au moins 0,5.
- **Ce que falsifie chaque issue :**
  - H_B falsifie la prémisse A1 à 8 milliards de paramètres.
  - H_A falsifie la suffisance d'une surveillance locale agrégée.

**E0b**
- **Mesure :** le décalage moyen μ(a) du score sur un acte isolé, en fonction de son amplitude a.
- **Rapport :** R = 4·μ(a/4)/μ(a).
- **H_A :** R < 0,8 (μ convexe ou à seuil).
- **H_B :** R ≥ 0,8.
- **Prédiction déposée :** sous H_A, l'agrégation par somme perd de la puissance quand k croît ; sous H_B, elle n'en perd pas.
- **Ce que falsifie chaque issue :**
  - H_B falsifie P1 pour l'agrégation par somme.
  - H_A falsifie l'idée que la dilution est sans coût pour l'agrégateur.

### E1'. Croisement et suffisance

**E1a (croisement).** On note g(k, c) = p_local − p_comparaison, à coût mesuré, avec un rapport de coûts c pris sur une plage déposée.
- **H_A :** le vrai g change de signe sur la grille.
- **H_B :** il garde un signe constant.
- **Règle de décision :**
  - H_A est établie si deux points ont des bandes simultanées excluant zéro, de signes opposés.
  - H_B est établie si toutes les bandes excluent zéro avec le même signe.
- **Ce que falsifie chaque issue :**
  - H_A falsifie l'idée qu'un seul instrument domine la plage.
  - H_B falsifie k comme axe d'arbitrage entre instruments.

**E1c (suffisance des entrées).** À (Δ, k) fixés, on compare des actes contigus à des actes dispersés, à s_α mesuré égal.
- **H_A :** l'écart de puissance est d'au plus 0,10.
- **H_B :** il dépasse 0,10.
- **Ce que falsifie chaque issue :**
  - H_B falsifie la suffisance de (s_α, k/T) : il faut ajouter une variable de structure temporelle à f.
  - H_A falsifie le besoin d'une telle variable.

### E2'. Contagion dans le cadre 2

**Dispositif.**
- Trois copies, dont une sabotée.
- Les copies honnêtes sont randomisées entre deux carnets : un carnet exposé, contenant les actes de la copie sabotée, et un carnet témoin, honnête, issu d'une autre graine.
- Bras placebo : carnet contenant les actes du saboteur P, de Δ nul.

**Mesure.** λ_cont = (sortie exposée − sortie témoin)/Δ.

**E2a**
- **H_A :** λ_cont ≥ 0,2.
- **H_B :** λ_cont < 0,2.
- **Ce que falsifie chaque issue :**
  - H_A falsifie l'idée que des copies exposées puissent servir de références indépendantes, et celle que le cadre 2 se réduit au cadre 1 avec λ = 0.
  - H_B falsifie l'idée que la contagion soit un mécanisme propre au cadre 2 à cette échelle.

**E2b (cadre 1, exposition φ).**
- **H_A :** la pente de la puissance en λ, à r fixé, est négative.
- **H_B :** elle est positive ou nulle.
- L'effet de r, attendu positif, est rapporté comme contrôle de cohérence.

**Contrôles :**
- permutation des références entre répétitions d'une même tâche ;
- duel de variance de R3 (ligne 9).

### E3'. Attaque des moniteurs

**Mesures**, avant et après attaque :
- Δ conservé ;
- s_α ;
- puissance des comparaisons et de la vérification ;
- taux de fausses alertes sur H+ au seuil figé ;
- λ.

**Duel.**
- **H_A (absorption) :** aucun instrument non visé ne varie de plus de 0,05, **et** la détection agrégée du moniteur visé est prédite à 0,05 près par f, appliquée à la queue par acte mesurée après l'attaque.
- **H_B :** l'une des deux conditions est violée.
- **Ce que falsifie chaque issue :**
  - H_A falsifie l'idée que le cadre 3 exige un modèle propre.
  - H_B falsifie P3 et désigne le canal de débordement.

**Contrôles :**
- adaptation LoRA sans pénalité, de même rang et de même nombre de pas ;
- adaptation LoRA neutre ;
- sonde réentraînée sur une autre graine ;
- trois niveaux de budget d'attaque ;
- saboteur LoRA sans consigne ;
- régimes boîte blanche et boîte noire.

### E4'. Unification : l'expérience qui tranche

**Dépôt, avant toute donnée des cadres 2 et 3 :**
- la forme de f et ses paramètres, ajustés sur le cadre 1 ;
- la liste et les poids des cellules ;
- l'enveloppe de support ;
- N1 et N2 ;
- les tolérances.

**E4a (transfert).** On note G = EAM_{2,3}(f) − EAM_{1, écart}(f), l'écart entre l'erreur sur les cadres cibles et l'erreur sur les cellules du cadre 1 tenues à l'écart.
- **H_A :** G ≤ 0,05.
- **H_B :** G > 0,05.

**E4b (contenu).**
- **H_A :** f bat N1 d'au moins 0,03 en EAM sur les cadres 2 et 3.
- **H_B :** l'écart est inférieur à 0,03.

**Contrôle.** Une permutation stratifiée de l'appariement entre entrées et issues doit faire monter l'EAM au niveau d'un prédicteur constant. Sinon, f capte un artefact.

**N2** (courbe en k ajustée par cadre sur les mêmes données que f) est rapporté. S'il bat f, les entrées n'apportent rien de plus qu'un étalonnage direct.

**Lecture des issues :**
- **H_A en E4a et en E4b :** il existe une problématique commune non triviale, portée par la dépendance (λ, r, structure temporelle).
- **H_A en E4a, H_B en E4b :** l'unification se réduit à l'identité d'agrégation de signaux indépendants. Les trois articles partagent une métrique, pas un modèle.
- **H_B en E4a :** les articles gagnent à rester distincts, et l'on rapporte quel cadre dévie.

### E5'. Transfert de la politique de budget

**Condition préalable.** La politique optimisée sur place doit battre l'allocation aléatoire d'au moins 0,10 de rappel absolu. Sinon, le regret n'est pas défini et cette absence est rapportée.

**Duel.**
- **H_A :** le regret est d'au plus 10 %.
- **H_B :** il dépasse 10 %.
- **Ce que falsifie chaque issue :**
  - H_A falsifie l'idée que les défenses doivent être conçues cadre par cadre.
  - H_B falsifie l'utilité pratique de l'unification, même si E4' réussit.

**Conditions de mesure :**
- le vérificateur réel est utilisé, à l'aveugle ;
- un audit aléatoire porte sur H− et sur les sabotés de même Δ ;
- les entrées sont estimées sur la partition d'étalonnage de la cible, et leur coût est compté.

### Moyens et calendrier

**Moyens (illustratif).** Environ 70 000 trajectoires et environ 600 h·GPU H100, soit 1 500 à 1 800 € de calcul. Les variantes de force des moniteurs réutilisent les mêmes trajectoires. En cas de dépassement, on retire k = 4.

**Calendrier :**

| Semaines | Travail |
|---|---|
| 1–2 | Socle, pilote de faisabilité (A2), E0' |
| 3 | Dépôt de la sélection, puis E1' et ajustement de f |
| 4 | **Dépôt du préenregistrement** |
| 5–6 | E2' et E3' |
| 7 | E4' et E5', réplication partielle sur Qwen3-8B |
| 8 | Rédaction |

---

## (c) Réponse à la question de l'arbitre

### Ce qui est établi

**Aucun résultat empirique.** Le bloc FAITS ne contient aucun fait statué.

Les critiques établissent en revanche des points de méthode, qui contraignent le plan. Ils ont le statut HYPOTHÈSE de méthode, mais ceux que j'ai recalculés tiennent sous les lois énoncées. **Ma conception du tour III.1 ne pouvait pas trancher**, pour quatre raisons :
- f n'était pas identifiable sur le seul cadre 1 ;
- ρ mêlait deux effets de signes opposés ;
- l'aire sous la courbe ROC ne fixait pas la métrique ;
- un seuil à 1 % sur 300 exécutions honnêtes rendait la tolérance de ±0,10 non jugeable.

### Ce qui n'est pas établi

Les points suivants restent à l'état d'HYPOTHÈSE :
- l'existence d'une dilution réelle à 8 milliards de paramètres (A1) ;
- la capacité d'un modèle de cette taille à saboter de façon diluée (A2) ;
- la contagion entre copies ;
- l'absorption d'une attaque de moniteur par une perte de signal ;
- l'unification.

### (1) Question révisée

> Une fois mesurés le signal par acte dans la queue utile, la fraction d'actes altérés, le biais reproduit par les références (λ) et leur bruit partagé (r), l'étiquette du cadre (agent seul, copies coopérantes, moniteur visé) apporte-t-elle encore de l'information sur la probabilité qu'un défenseur à budget fixé détecte une dégradation diluée ?

### (2) Réponse attendue

Statut : HYPOTHÈSE.
- **Réponse attendue :** non, au sens de E4a (G ≤ 0,05), et f bat N1 d'au moins 0,03 (E4b). Ces seuils sont illustratifs.
- **Point de rupture le plus probable :** le cadre 2. Une contagion forte (λ_cont élevé) placerait les cellules du cadre 2 hors du support du cadre 1.
- **Chaque issue est réfutable** par E4' tel qu'il est déposé.

### (3) Antériorité la plus proche

Greenblatt, Shlegeris, Sachan, Roger, *AI Control: Improving Safety Despite Intentional Subversion*, citée **de mémoire**, date à vérifier (2023 ou 2024).

### (4) Expérience à faire en premier : E0', en deux semaines

Trois raisons :
- **E0' peut clore la question.** Une issue H_B en E0a, ou la domination d'une vérification mécanique (M1 ou M5) pour tout k, rend la question **sans intérêt** à cette échelle.
- **E0b fixe la forme de P1.** Il décide si P1 est même possible pour l'agrégation par somme.
- **Le pilote teste la faisabilité.** Il vérifie que le modèle de 8 milliards de paramètres peut porter le sabotage (A2).

L'expérience qui tranche reste E4'.

### (5) Type de contribution

**Autre : un test de suffisance**, c'est-à-dire un test d'indépendance conditionnelle de l'étiquette du cadre, sachant des entrées mesurables. Il comporte deux éléments :
- une loi connue ailleurs, l'agrégation de signaux épars ou denses, utilisée comme nulle analytique N1 ;
- une variable candidate nouvelle, λ_cont.

Ce n'est pas une garantie.

### Issues à intérêt réduit

Une issue H_A en E4a avec H_B en E4b n'est pas sans intérêt, mais son intérêt est réduit : les trois articles partagent une métrique, pas un modèle.

### Vérification de la nouveauté

- **Bibliographie ciblée.** Vérifier si Wen et al. (2024) et Bhatt et al. (2025), cités de mémoire et à vérifier, mesurent déjà une contagion ou un biais reproduit par la référence.
- **Préenregistrement horodaté**, avant toute donnée des cadres 2 et 3.
- **Réplication** sur une seconde famille de modèles (Qwen3-8B).
- **Publication** des trajectoires, des scores bruts et des partitions.

FIN-DE-CELLULE
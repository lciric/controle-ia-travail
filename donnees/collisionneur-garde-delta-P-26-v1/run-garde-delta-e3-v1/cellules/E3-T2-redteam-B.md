# Cellule B — Tour III.2 : équipe rouge croisée contre A et C (P-26)

**Pièces reçues.** Les conceptions A et C sont complètes : chacune se termine par sa ligne de fin. La pièce F n'est pas servie (déclaré).

**Périmètre des « scénarios d'évasion ».** La garde de sûreté (R-519, R-339, R-597) interdit de concevoir ou de détailler une attaque. L'« agent adverse » est donc limité ici à deux acteurs :
- **le sujet A et ceux qui le règlent** : leurs degrés de liberté avant scellement ;
- **l'opérateur de la lecture** : ses degrés de liberté après lecture.

On ne trouvera ici aucune recette de sabotage ni aucune manière de tromper un moniteur, seulement des chemins qui permettent de faire dire à la procédure ce qu'elle ne mesure pas.

**Statuts.**
- **VÉRIFIÉ** : lisible dans la pièce A ou dans un texte de décision.
- **RAPPORTÉ** : chiffre des pièces B, C ou D.
- **HYPOTHÈSE** : ce que j'avance. Mes dérivations sur le code sont marquées « dérivation, falsifiable par… ».

---

## Contre la proposition A

### (a) Failles

**A-1 — Le « biais structurel » Δ_j est vrai par construction. C'est la faille la plus grave de A.**

A fixe le biais tenu pour honnête par Δ_j = |taux_calibrage_A − taux_calibrage_Bj|, avec une règle « calibrage insuffisant si max Δ_j > δ/4 » et une puissance calculée à biais ∈ {0 ; max Δ_j}.

Ce que fait le code (VÉRIFIÉ, `seuil`) :
- les scores honnêtes du calibrage sont triés par ordre décroissant ;
- s = scores[j − 1] ;
- `taux_calibrage` = part des x > s.

La conséquence (dérivation, falsifiable par une exécution de `seuil` sur toute banque) :
- au plus j − 1 scores dépassent strictement s. Sans ex æquo, taux_calibrage = (j − 1)/n pour **toute** cellule de la même strate ;
- Δ_j ne mesure donc que la masse d'ex æquo au seuil ;
- avec le bris d'égalité P-15 « scellé d'office » (pièce D), Δ_j = 0 identiquement.

La règle de A se réduit alors à « biais ∈ {0 ; 0} » et à un contrôle qui ne peut pas échouer. C'est la circularité de GD-04 (pièce C v1) déplacée de la garde vers son étalonnage : l'instrument qui doit révéler un biais hors échantillon est calculé sur l'échantillon qui fixe les seuils. Résultat : la sensibilité au biais que les pièces montrent est effacée du dimensionnement (0,89 → 0,03 à E[g] = 0,0125, τ = 0,10, pièce C v1 GD-03, RAPPORTÉ).

**A-2 — A6 présente un résultat conditionnel comme établi.**

A écrit « E[g_j] = 0 pour toute paire » sous le statut VÉRIFIÉ, puis conclut : « un biais n'est pas une propriété tolérable du sujet ». La docstring de `monde_banque_scores` pose pourtant la condition « pour des scores échangeables » (VÉRIFIÉ). Deux sources de biais restent ouvertes :

1. **Le conditionnement.** La garde teste E[g] à seuils fixés. Or le taux d'alerte d'une cellule, conditionnellement au calibrage tiré, est aléatoire autour de j/(n + 1). La moyenne nulle n'est que marginale.
2. **Le décalage de loi entre parties.** Les tâches d'épreuve sont disjointes de celles du calibrage. Si le décalage agit différemment sur la cellule A et sur la cellule B_j (A lit l'intérieur, B_j le texte), alors E[g] ≠ 0 sans aucune faute de calibrage. C'est exactement l'« artefact de source » que la garde devait voir.

A6 est donc une **HYPOTHÈSE d'échangeabilité**, pas un fait. Toute la chaîne du point 4 de A (« le biais attendu d'un sujet honnête est 0 ») en hérite.

**A-3 — E1 mesure la puissance sur une paire dont la variance est nulle par construction.**

La paire nulle de E1 compare la même cellule, calibrée sur la moitié 1 puis sur la moitié 2, et lue sur les **mêmes épisodes**. Dérivation : g(t) ≠ 0 seulement pour les épisodes dont le score tombe entre deux seuils voisins, calibrés chacun sur environ 4 800 épisodes (ordre de grandeur illustratif). g est donc presque toujours nul. La garde atteint alors le plancher à écarts nuls (93 ou 144 unités, pièce E) de façon quasi déterministe.

Conséquences :
- H_A (« ≥ 0,8 à n_h disponible ») est vraie dès que n_h dépasse le plancher, quelle que soit la loi réelle de g entre A et un vrai comparateur ;
- E1 ne peut falsifier H_A que si n_h < plancher, ce qu'on sait déjà sans données ;
- la puissance pertinente est celle de A contre B_j : scores différents, variance de g d'environ 0,045 à K = 10, τ = 0,01 (pièce C v1 Q3, RAPPORTÉ).

A ne mentionne ce cas que dans la table (c), pas dans l'expérience décisive.

**A-4 — m_c n'est pas un levier de puissance.**

A présente m_c comme « le levier le moins cher ». Ce que dit le code (VÉRIFIÉ) :
- le seuil d'une fiche est m_c/α_c ;
- `Course.entrer` refuse toute somme des α_c supérieure à α.

Dérivation, falsifiable par un appel à `entrer` : découper huit critères en huit familles de taille 1 impose α_c ≤ α/8 à chacune. Le seuil vaut alors 1/(α/8) = 160, comme une famille m_c = 8 au niveau α.

m_c ne baisse donc le seuil que si G1 porte **moins d'affirmations**. Or N-056 fixe le gain « dans chacun des autres modes, mode tenu à l'écart compris », intersection-union sur les comparateurs (VÉRIFIÉ). Réduire m_c revient soit à retirer des critères, ce qui casse N-056, soit à donner à G1 tout α au détriment des autres familles de la génération. Dans ce second cas, si α_c < α, le seuil monte au-dessus de 160 (GD2-03, RAPPORTÉ). Le « levier » est un choix de correction de multiplicité déguisé en paramètre de puissance.

**A-5 — La garantie de F3 est mal énoncée.**

A écrit « union des deux erreurs α_c + α_g ». Une règle « promue si les deux rejettent » est une intersection-union. Sous le nul de la garde, P(promotion) ≤ α_g : l'erreur est bornée par le maximum des deux niveaux, pas par leur somme (dérivation).

Le vrai défaut de F3 est ailleurs : pour que l'e-BH de la famille tienne, α_g doit valoir au plus α_c/m_c. On revient alors au seuil 160, et le gain de puissance « 93 au lieu de 144 » n'existe qu'en renonçant au contrôle au niveau de la fiche. C vise juste sur ce point (son option 1C). A écarte F3 pour de bonnes raisons de texte (D-S4), mais sur une garantie fausse.

**A-6 — Le critère de vacuité « δ < effet du contraste » repose sur une hypothèse non marquée.**

A affirme qu'« un sujet qui alerte +δ sur les honnêtes alerte aussi +δ (environ) sur les sabotés ». C'est un modèle d'artefact additif, sans source et sans statut. La conclusion « δ = 0,10 est vide » en dépend, ainsi que de E[v] = 0,10. A marque bien cette valeur SUPPOSÉ, mais il en tire tout de même une recommandation.

**A-7 — Les unités honnêtes seules introduisent un biais de sélection.**

A place dans l'épreuve des unités sans épisode saboté. La pièce C v4 (Q7, RAPPORTÉ) signale que les unités à sabotés peuvent avoir un autre taux d'alerte honnête que les autres. Si les consignes « honnêtes seules » sont tirées autrement que les consignes mixtes, la garde mesure la différence entre deux populations de consignes, pas le sujet. A exige « même fabrique, même journal », mais pas un **tirage aléatoire scellé** qui décide quelle consigne devient honnête seule et laquelle devient mixte.

### (b) Scénarios d'évasion (procédure seulement)

- **Avant scellement.** Celui qui règle A choisit, parmi des variantes gelées, celle dont le taux d'alerte sur les tâches de développement est le plus proche de τ. La garde en développement passe, alors qu'aucune échangeabilité avec l'épreuve n'est démontrée. A ne l'empêche pas (A-2), et son contrôle Δ_j ne peut pas l'attraper (A-1). Coût pour l'adversaire : nul. Il suffit d'une sélection parmi des variantes déjà construites.
- **Par le paramétrage.** Plaider « famille propre, m_c petit » au nom de la puissance (A-4) baisse le seuil de chaque processus, donc l'exigence sur les contrastes autant que sur la garde. Coût : un argument de texte.
- **Par la composition des unités.** Choisir quelles consignes deviennent honnêtes seules (A-7). Coût : faible.
- **Tous les instruments à la fois.** Une variante calibrée près de τ en développement, plus m_c réduit, plus des unités honnêtes seules choisies : le contrôle Δ_j (nul), E1 (au plancher) et la garde passent ensemble. Aucun instrument de A n'est indépendant de l'échangeabilité calibrage–épreuve qu'il présuppose.

### (c) Contrôles négatifs dont l'absence serait fatale

**CN-A1 — Biais hors échantillon par permutation de partie.**
- Protocole : sur le développement, recalibrer les seuils sur un sous-ensemble de **tâches** tiré par graine, puis mesurer g sur les tâches restantes.
- H_A (échangeabilité entre tâches) : |ḡ| reste dans ±2 erreurs types.
- H_B (décalage spécifique à la cellule) : |ḡ| dépasse ce seuil.
- Lecture : si H_A tombe, A6 tombe et le biais doit entrer dans la puissance. Si H_B tombe, A6 est tenue empiriquement.
- Ce contrôle remplace Δ_j, qui ne peut pas échouer.

**CN-A2 — Puissance sur une paire à variance réelle.**
- Protocole : remplacer la paire jumeau de E1 par A contre B_j recentré, rééchantillonné par unité entière.
- H_A : la puissance à n_h est au moins 0,8. H_B : elle est inférieure.
- Contrôle interne : la paire jumeau doit sortir au-dessus de A contre B_j. Sinon, l'implémentation est fausse.

**CN-A3 — Sous-échantillonnage du fichier réel.** Voir CN-C2 ; ce contrôle manque aux deux propositions.

---

## Contre la proposition C

### (a) Failles

**C-1 — La règle 2C règle δ sur le biais observé du sujet. Faille fatale.**

La formule est δ = clip(μ̂_g,max + (144/N_h) × 0,05 ; 0,05 ; 0,10), où μ̂_g,max est une borne haute du biais de **A** contre ses comparateurs, mesurée sur les jumeaux honnêtes du pilote. Le point 4 ajoute E[g]_tol = min(0,0125 ; max(0, max_j ḡ_j)).

Les hyperparamètres de A sont gelés avant la lecture des honnêtes (P-9). Son biais en pilote prédit donc son biais à l'épreuve. Plus A lève de faux positifs en pilote, plus δ est lâche, jusqu'à 0,10. La garde est ainsi rendue incapable, par construction, de bloquer le biais qu'elle a vu : c'est la définition d'une garde vide. Il y a là une fuite directe de l'objet évalué vers le paramètre de l'instrument. A dit l'inverse (« aucun biais observé du sujet A sur le pilote n'entre dans une règle ») et, sur ce point, A a raison contre C.

**C-2 — La formule 2C contredit la prose qui l'accompagne.**

Calcul sur la formule :
- N_h = 160, μ̂ = 0 : 144/160 × 0,05 = 0,045, que le clip porte à **0,05**. La prose dit pourtant « 160 ≤ N_h < 250 → δ = 0,10 » ;
- N_h = 160, μ̂ = 0,0125 : δ = 0,0575. La formule produit une valeur continue, pas l'ensemble {0,05 ; 0,10} annoncé.

La constante 144 est en outre le plancher à δ = 0,05 et au seuil 160 (pièce E). Un plancher calculé pour un δ donné sert ici à fixer δ : la formule est circulaire. Une règle de préenregistrement qui admet deux lectures est une porte de sortie, puisque l'interprète choisira après coup.

**C-3 — Des contenus sont inventés et les statuts sont gonflés.**
- **Les lots C et J.** La pièce D dit seulement que le fichier réel viendra « du pilote (lots C et J), un par comparateur ». C en fait « C = calibrage du pilote, J = jumeaux honnêtes » et construit dessus son étape t = 2 ainsi que ses expériences 1 et 2. Ce contenu n'est dans aucune pièce.
- **Les numéros de ligne.** C cite « VÉRIFIÉ » de nombreux numéros (l. 19, l. 111, l. 153-171, l. 225-232, l. 262, l. 398) que les pièces ne donnent pas. Seules les contre-lectures citent l. 103-118, 136, 167-178 et 210-222.
- **Les statuts des chiffres.** Des chiffres de simulation (pièces B et C) passent en VÉRIFIÉ alors qu'ils sont RAPPORTÉS : le script v4 n'est pas servi. Le critère P-20 (« 16/16, 0 sur 48 ») est une **recommandation** non tranchée (pièce D), présentée comme VÉRIFIÉE.
- **« Llama 8B / 3B ».** C l'écrit sous le statut VÉRIFIÉ ; la pièce D dit « 8B, 3B ».
- **Le registre.** « Compatible à 100 % » et une confiance de 0,98 relèvent du superlatif interdit par la règle 5.

**C-4 — Les seuils du pilote ne sont pas ceux de G1. C'est une variable confondante.**

À son étape t = 2, C recalibre les seuils sur « le lot C » du pilote. La spécification de la pièce C v2 (point 5) exige des seuils calibrés sur les honnêtes du **calibrage de la banque**, au τ et dans la strate de G1. Des seuils tirés de 16 tâches sont plus bruités que ceux d'une banque de plusieurs milliers d'épisodes (taille relevée par l'auteur, pièce B v1). Le ḡ et la dispersion mesurés intègrent donc un bruit de calibrage absent de G1 : n₈₀ est surestimé, et μ̂ se trouve gonflé ou dégonflé selon le tirage. Combiné à C-1, ce bruit de calibrage se transforme directement en δ.

**C-5 — Le tableau du point 3 contredit ses propres sources.**
- **Cellule « δ = 0,05, K = 10, τ = 0,01, biais 0 : n₈₀ 156–160 ».** La même case cite 0,78 à 160 unités pour k = 3, et 0,78 est inférieur à 0,8. Le 156 est le n₈₀ d'une **garde seule** au seuil 160 (pièce B v1, RAPPORTÉ), pas d'un minimum à trois gardes.
- **La plage 160–530.** C la répartit sur des cases précises (« 400–530 ») sans la marquer comme interpolation. La pièce C v3 § 7 ne la donne que globalement, toutes lois confondues.
- **Le « 0,96 à 250 unités » de l'erratum.** Il sert de base à la recommandation N_h = 250 au niveau de la fiche à k gardes, alors que l'erratum ne dit ni k ni K. En faire la garantie « tient un biais de 0,0125 avec puissance 0,96 » pour la fiche est une extrapolation.

**C-6 — La règle d'arrêt rouvre la porte après lecture.**

C scelle : « si min(log_richesse_finale_par_comparateur) ≥ seuil mais garde < seuil → arrêt et nœud pour Lazar ». Deux défauts :

1. La fiche est **arrêtée** au premier franchissement du minimum (VÉRIFIÉ, `evaluer`). Les richesses finales des contrastes, lues isolément, forment un autre test que la garantie de Ville ne couvre pas. Les rapporter comme « contrastes passés » revient à rendre une lecture sans garde.
2. Un nœud ouvert **après** l'épreuve sur ce motif invite à racheter des unités ou à changer δ, c'est-à-dire à faire exactement ce que la question demande d'empêcher. A place le nœud avant scellement seulement. C le place après.

**C-7 — Les expériences 1 et 2 ne peuvent pas trancher à la taille du pilote.**

- **Expérience 1.** H_A et H_B ne sont pas exclusives : une zone 0,005 < |ḡ| < 0,0125 ne falsifie rien, ce qui viole la règle B4. Le critère « puissance ≥ 0,80 à 160 unités, k = 3, seuil 160, δ = 0,05 » est déjà manqué à biais nul en synthétique (0,78, RAPPORTÉ). H_A est donc presque falsifiée d'avance. Enfin, l'erreur type de ḡ vaut environ 0,045/√N (illustratif). Pour quelques dizaines d'unités de pilote, elle est du même ordre que l'écart à distinguer.
- **Expérience 2.** À τ = 0,01, φ̂ = Var(f_A)/[f̄(1 − f̄)/K] repose sur une poignée d'alertes. Avec 1 % d'alertes sur quelques centaines d'épisodes honnêtes, on compte quelques alertes (illustratif). Distinguer ρ ≈ 0,015 de ρ ≥ 0,056 est hors de portée. Les deux issues sont ininterprétables.

**C-8 — La lecture du calibrage dans les contrôles.**

La table (c), point 2, de C propose la fiche jumeau « sur les 9 600 épisodes honnêtes du calibrage » comme cas honnête apparié du juge. Au sens du critère gelé de la question, c'est une lecture du calibrage dans l'évaluation, que la synthèse doit marquer « circulaire ». Le chiffre 0,024–0,027 qui l'accompagne vient en outre de P-17 (coupe par graine sous dérive), mélangé à P-15 (bris d'égalité) : deux sources sont confondues (pièce D, RAPPORTÉ).

### (b) Scénarios d'évasion (procédure seulement)

- **Acheter un δ lâche (C-1).** Parmi des variantes gelées de A, retenir celle dont le biais en pilote est le plus élevé sans dépasser l'arrêt de 0,025. La règle 2C relâche alors δ vers 0,10, et la garde certifie un sujet à environ +0,10 de faux positifs. Coût : nul, une sélection suffit. Je ne vois aucun instrument de C qui l'attrape, puisque le paramètre est fait du symptôme.
- **Jouer l'ambiguïté de 2C (C-2).** Après le passage sur le fichier réel, choisir entre la lecture « formule » et la lecture « prose » selon celle qui donne le δ voulu. Coût : nul.
- **Jouer le calibrage du pilote (C-4).** Le tirage de « lot C » fixe les seuils, donc ḡ, donc δ et N_h.
- **Après lecture (C-6).** Contrastes franchis et garde bloquante : le nœud permet de plaider des unités supplémentaires ou un autre δ.
- **Tous les instruments à la fois.** Variante choisie, seuils de pilote bruités et nœud après lecture : la garde, la règle de dimensionnement et la règle d'arrêt cèdent ensemble, parce qu'elles prennent toutes leurs entrées dans les mesures du sujet.

### (c) Contrôles négatifs dont l'absence serait fatale

**CN-C1 — Indépendance de δ vis-à-vis du sujet.**
- Protocole : appliquer la règle de fixation de δ à un sujet de **biais injecté connu** (seuil de A déplacé au quantile τ + δ/2, lu sur le développement).
- H_A (règle indépendante du sujet) : δ ne bouge pas.
- H_B : δ augmente avec le biais injecté.
- Lecture : si H_A tombe, la règle 2C est vide par construction et doit être rejetée. Si H_B tombe, C-1 est réfuté.

**CN-C2 — Stabilité de n₈₀ au sous-échantillonnage. Il manque aussi à A.**
- Protocole : refaire le calcul de n₈₀ sur des moitiés de **tâches** du fichier réel tirées par graine, au moins vingt fois (nombre illustratif).
- H_A : n₈₀ reste dans un facteur 1,25 (illustratif) de sa valeur sur tout le fichier.
- H_B : il en sort.
- Lecture : si H_A tombe, un rééchantillonnage tiré de 16 tâches ne peut pas dimensionner N_h, et le scellement doit prendre la borne haute. Si H_B tombe, le fichier réel suffit.

**CN-C3 — Seuils de G1 contre seuils du pilote.**
- Protocole : calculer ḡ et n₈₀ une fois avec les seuils du calibrage de la banque, une fois avec ceux de « lot C ».
- H_A (indifférence) : écart ≤ 2 erreurs types. H_B : écart supérieur.
- Lecture : si H_A tombe, seule la spécification de la pièce C v2 (point 5) est recevable.

**CN-C4 — Sujet identique à son comparateur.** Il manque aussi à A.
- Protocole : prendre A = B_j.
- H_A : la garde certifie (g ≡ 0) **et** le contraste n'est pas promu (E[v] = 0, promotion ≤ α_c/m_c).
- H_B : la fiche est promue au-delà de la borne de Ville.
- Lecture : si H_A tombe, l'implémentation ou l'alignement par rang est fautif. Ce contrôle rappelle aussi que la garde certifie trivialement un sujet sans signal : sa non-vacuité ne se lit pas sur elle seule.

---

## Ce qui frappe les deux propositions (attaqué séparément, sans fusion)

- **La garde est aveugle aux artefacts propres aux épisodes sabotés.** Elle ne lit que des honnêtes (VÉRIFIÉ, `ecarts_faux_positifs`). Une différence de fabrique corrélée à l'étiquette « saboté » n'augmente pas les faux positifs et passe la garde. A (« sans artefact de source ») et C (« garantie sans artefact de source ») lui prêtent davantage qu'elle ne certifie. La phrase scellable doit se limiter au taux de faux positifs relatif.
- **Il faut un contrôle placebo sur le contraste (HYPOTHÈSE).**
  - Protocole : permuter les étiquettes honnête et saboté à l'intérieur de chaque unité du développement.
  - H_A : aucune promotion au-delà de 1/seuil.
  - H_B : promotions au-delà de ce niveau.
  - Lecture : si H_A tombe, il existe une fuite entre l'étiquette et le score, que la garde ne peut pas voir.
  - Aucune des deux propositions ne prévoit ce contrôle. C'est la seule parade, au niveau de la procédure, contre le premier point.
- **Les unités honnêtes seules** (A-7 et l'option 2 de C) demandent toutes deux un tirage scellé qui décide quelle consigne devient honnête seule et laquelle devient mixte. Ni A ni C ne l'écrit.

## Non vérifié par moi

- Le contenu des lots C et J.
- Les valeurs de k, K_h, m_c et α_c de G1.
- L'effectif d'unités du pilote.
- Le script v4 (non servi).

Mes erreurs types et mes ordres de grandeur sont illustratifs. Les dérivations A-1 et A-4 se falsifient par une exécution de `seuil` et de `Course.entrer`.

FIN-DE-CELLULE
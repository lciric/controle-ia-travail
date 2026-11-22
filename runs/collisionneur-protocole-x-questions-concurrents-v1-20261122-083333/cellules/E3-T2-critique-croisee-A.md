# Proposition A : Tour III.2, critique croisée de méthode

## 0. Pièces et conventions

- **Liste de publications : absente.** Je n'en invente rien.
- **Ma propre conception (A, tour III.1) ne m'est pas retransmise.** Je ne m'y réfère pas.
- Les pièces B, C, D, E et F sont reçues et se terminent chacune par leur marqueur, sans coupure visible. Je n'ai pas recalculé les empreintes.
- **Statuts.** « La pièce X écrit Y » est VÉRIFIÉ, au sens où je l'ai lu dans la pièce. Tout défaut ou toute perte de puissance que j'avance est une HYPOTHÈSE, réfutable par les mesures indiquées.
- **Chiffres.** Tous mes chiffres sont des calculs faits sur les valeurs illustratives des pièces ; ils sont donc **illustratifs**.
- **Notations.** π est la prévalence de la classe positive, n l'effectif, ET l'erreur type.

---

## Sur la proposition B

**(a) Défauts de méthode**

1. **E1 : κ gonflé par la classe « aucune ».** L'unité inclut des phrases tirées au hasard hors des sections de limites, plus 15 % de témoins descriptifs. Le κ à quatre classes est alors dominé par la distinction manque/aucune, qui est facile. La frontière « annoncé »/« ouvert », objet de P4, pèse peu. H_B peut donc être falsifiée sans que la séparabilité ait été testée.
2. **Fuite E1 → I1.** Le consensus des deux experts sert de vérité terrain à I1. Rien ne sépare les articles qui servent à écrire la grille, à mesurer κ et à évaluer l'extracteur. La référence par expressions régulières reprend en outre les marqueurs de la grille, si bien que l'écart I1 − regex mesure la conformité à la grille.
3. **E2 : vérité terrain non indépendante.** La « lecture intégrale de la littérature » ne sera pas faite ainsi. Les experts chercheront par citations et mots-clés, c'est-à-dire avec l'instrument évalué. Les « comblements connus » sont par ailleurs connus parce qu'ils étaient trouvables, ce qui biaise le rappel vers le haut.
4. **E2 : duel non exhaustif.** H_A exige rappel ≥ θ₂ et fausses alertes ≤ φ₂, alors que H_B dit seulement rappel < θ₂. Avec un rappel conforme et des fausses alertes excessives, les deux sont fausses. Le codage de « partiellement comblé » n'est pas fixé.
5. **E3 : l'issue dépend des critères par construction.** La « contribution d'une petite équipe » dépend mécaniquement du critère 4 (faisable sur modèles ouverts). « Non comblé par l'équipe d'origine » dépend du critère 2 dès que H_A d'E4 est vraie. L'issue mesure donc l'affluence, pas la qualité du choix.
6. **E3 : erreur de mesure différentielle.** L'issue est relevée par I2, dont le rappel croît avec le critère 5 (portée spécifiée).
7. **E3 : le test de fuite ne vise pas la fuite réelle.** Celle-ci est le codage rétrospectif des critères « à t₀ » par des lecteurs qui connaissent t₁. Recalculer avec les informations de t₁ ne la détecte pas.
8. **Règle soustraite à l'épreuve.** « Un choix qui échoue aux critères 1, 2 et 7 est mauvais quelle que soit l'issue » est vrai par définition et échappe à E3.
9. **E4 : confusion.** Les équipes qui écrivent « nous ferons » diffèrent par leurs moyens et par le type de manque. Le témoin d'un autre domaine donne un taux de base mais n'ôte pas cette confusion.
10. **E6 : deux biais.** Une dégradation obtenue par consigne peut laisser la trace de la consigne dans la trajectoire, que le moniteur détecterait à la place de la dégradation. La « meilleure vérification mécanique » est choisie sur le lot d'évaluation.

**(b) Conditions de perte de puissance**

- **E1.** Le κ restreint à la frontière annoncé/ouvert n'est pas jugeable si π(annoncé) ≈ 0,05. Sur 400 énoncés, cela fait environ 20 items et une demi-largeur d'IC d'environ 0,25. Le bootstrap par article ramène l'effectif utile au nombre d'articles si les énoncés sont concentrés.
- **E2, rappel.** Le dénominateur vaut 100·π_c. Pour π_c ≤ 0,2, la loi est une Binomiale(≤ 20 ; 0,7), de demi-largeur ≈ 0,20. L'intervalle chevauche θ₂ pour tout rappel vrai entre 0,5 et 0,9.
- **E2, fausses alertes.** Avec 30 manques fabriqués, 0/30 donne une borne supérieure à 95 % d'environ 0,10. Une seule fausse alerte rend « ≤ φ₂ » indémontrable.
- **E3.** ET(AUC) ≈ 0,11 à 0,13 pour 15 positifs, donc δ₃ = 0,1 est inférieur à une ET. Avec une corrélation intra-article ρ et m manques par article, l'effectif utile est n/(1+(m−1)ρ).
- **E4.** Si la médiane de la loi des délais d'exécution dépasse Δ, les deux proportions tendent vers 0. Δp tend alors vers 0 quelle que soit la vérité : c'est une censure à droite.
- **E5.** Si le τ entre deux lecteurs « texte seul » est inférieur à θ₅, H_A est inatteignable, quelle que soit la valeur du texte.
- **E6.** À 1 % de fausses alertes par trajectoire, avec 300 trajectoires honnêtes dont 100 tâches indépendantes, le seuil repose sur 3 observations au plus. La variance du taux de détection est dominée par celle du seuil.

**(c) Contrôles négatifs dont l'absence serait fatale**

- **E1 :** κ calculé sur les seuls énoncés que les deux lecteurs classent comme manques, et articles de mise au point disjoints des articles d'évaluation.
- **E2 :** quasi-comblements réels, c'est-à-dire des articles citants de même vocabulaire qui redisent le manque ouvert. Je reprends ici C et F. Les manques fabriqués hors distribution sous-estiment les fausses alertes.
- **E2 :** double recherche indépendante pour estimer le dénominateur inconnu (capture-recapture).
- **E3 :** codage sur versions figées par des lecteurs à qui l'issue est masquée, et critère placebo (longueur de la phrase du manque) devant donner une AUC ≈ 0,5.
- **E6 :** trajectoires honnêtes où la consigne de dégradation est présente mais non suivie, ou consigne retirée de ce que voit le moniteur.

---

## Sur la proposition C

**(a) Défauts de méthode**

1. **Statuts.** Deux affirmations générales portent `OBSERVÉ-NON-AUDITÉ` (omission présentée comme piste ouverte ; coût des essais infructueux rarement publié). La pièce ne décrit aucune observation : ni qui, ni sur quel corpus. Elle ne fournit rien qui soutienne ce statut.
2. **E1 : frontière décrétée.** La règle de résolution code « we leave X » en classes 1 + 3, jamais en classe 2. κ mesure alors l'obéissance à une règle lexicale. H_B porte sur le cas « hors marqueurs triviaux », mais le protocole ne stratifie pas selon la présence de marqueurs. Deux issues ne falsifient rien : κ_global < 0,75 avec κ₂ᵥ₃ ≥ 0,65, et F₁ < 0,80 seul.
3. **E2 : ΔRappel positif par construction.** Les 20 manques synthétiques « reformulés dans le lexique de la sécurité logicielle » entrent dans le jeu d'essai. Ils sont visibles pour la passe 2 et invisibles pour la passe 1 par fabrication.
4. **E2 : référence non chiffrée.** La « revue systématique exhaustive multi-domaines » est absente du budget, qui prévoit 40 heures humaines au total. Elle sera vraisemblablement menée avec des requêtes fonctionnelles, donc avec la passe 2.
5. **Passe 3 : comblé confondu avec auditable.** Les conditions (ii) et (iii) exigent un taux de fausses alertes explicite et du code. Un manque théorique ou non lié à un moniteur ne peut jamais être déclaré comblé.
6. **O1 : auditeur non aveugle.** Il connaît le point d'injection. Le seuil ≥ 90 % est atteint par construction, et le cas « < 60 % » est incohérent avec cette connaissance.
7. **O3 : action hors politique.** La substitution franche en rejeu mesure la détectabilité de l'injection. Sa loi n'est pas celle des dégradations produites par l'agent.
8. **E3 : H_A vraie par construction.** « Concluant » signifie puissance ≥ 0,80 contre la ligne de base mécanique. Or la puissance est une fonction déterministe de la taille d'effet (O3), du bruit (O2) et de la marge sur le mécanique (O1). Le bras bibliométrique est défini par l'échec à l'un des trois. Les bras ne sont pas randomisés, et la puissance est une propriété du plan, pas une issue observée.
9. **E4 : information inégale.** Le moniteur A reçoit un graphe d'état extrait. Le « budget de jetons égal » n'égalise pas l'information reçue.
10. **E4 : verdict fixé par le mélange.** Le résultat dépend du mélange 100/100 choisi par l'expérimentateur. La zone |Δ| < 0,15 ne falsifie rien, et le seuil de fausses alertes est calibré sur les trajectoires honnêtes d'évaluation.

**(b) Conditions de perte de puissance**

- **E3, seuil.** L'issue seuil 5/6 contre 2/6 a une probabilité hypergéométrique unilatérale de (90+6)/792 ≈ 0,12. Le seuil préenregistré ne rejette pas l'égalité à 5 %.
- **E3, puissance.** Même avec p₁ = 0,8 et p₂ = 0,3, la probabilité d'obtenir l'issue qui falsifie H_B est d'environ 0,655 × 0,744 ≈ 0,49.
- **E3, contrôle négatif.** Avec 3 tâches et une probabilité de rejet q par tâche, la probabilité de réussir le contrôle est q³, soit 0,34 pour q = 0,7. Ce contrôle n'informe pas.
- **O3.** ET(d) ≈ √(2/n + d²/(4n)) ≈ 0,33 pour n = 20. Les seuils 0,5 et 0,8 sont séparés de moins d'une ET.
- **O1.** Une Binomiale(20, p) a une demi-largeur de 0,15 à 0,20. Les bornes du corridor (30 %, 80 %, 90 %) ne se distinguent pas de leurs voisines.
- **E2.** Sur les manques réels, le nombre de comblés vaut 40·π. Pour π = 0,25, un ΔRappel de 0,20 correspond à 2 items.
- **E4.** TPR_A − TPR_B = w·Δ_local + (1−w)·Δ_distribué. Le signe peut s'inverser selon w, et l'expérience n'estime que le point w = 0,5. À 1 % de fausses alertes, le seuil repose sur 2 trajectoires sur 200.
- **E1.** κ₂ᵥ₃ est instable quand π(classe 2) tend vers 0.

**(c) Contrôles négatifs dont l'absence serait fatale**

- **E1 :** κ sur la strate des énoncés sans marqueur de la grille.
- **E2 :** ΔRappel rapporté sur les seuls manques réels, avec une référence établie par des personnes sans accès aux requêtes de la passe 2.
- **O1 :** auditeur aveugle, avec traces honnêtes mêlées.
- **O3 :** substitution placebo (une action légitime remplacée par une autre action légitime) pour mesurer le d dû à la seule substitution.
- **E3 :** issue jugée par un tiers aveugle aux scores O, et bras « tirage aléatoire ».
- **E4 :** moniteur B recevant le même graphe d'état, résultats par strate, et lot de calibration disjoint (F en prévoit un, je le reprends).

---

## Sur la proposition D

**(a) Défauts de méthode**

1. **Le test d'attribution est une recherche.** Ce n'est pas un duel entre hypothèses rivales. Le verdict négatif (« lecture intégrale sans citation recevable falsifie H_A ») suppose un rappel du lecteur égal à 1. La « relecture contradictoire » n'a aucun taux d'erreur mesuré, et aucun accord inter-lecteurs n'est prévu.
2. **Contrat conjonctif.** « Comblé » exige un témoin pour chacune des six conditions. La probabilité d'un témoin complet décroît avec la finesse du contrat, qui reste un paramètre libre. Fixé avant la recherche, il n'est pas pour autant justifié. On peut atteindre « non comblé » par simple spécification.
3. **Absence sans taux d'erreur.** Borner le verdict « dans ce corpus seulement » est correct, et je reprends cette borne. Mais sans estimateur de la couverture du corpus, « aucun témoin » n'a pas de taux d'erreur.
4. **Choix prospectif non réfutable.** La liste des éléments « à consigner » est une règle de journal. Hors le cas du validateur simple, elle ne donne ni seuil, ni sens de variation, ni test de valeur prédictive. Rien n'y est réfutable. « Privilégier celui où une décision changerait » n'a pas d'estimateur.
5. **Duel de priorité.** Le signe du gain net dépend du rapport v/c entre valeur du dommage évité et coût de revue. Ce rapport est fixé par l'équipe ; le préenregistrer n'en fait pas une donnée. Construire deux candidats à enveloppe égale avantage en outre le plus mûr (code existant).
6. **Budget.** Une trace de 2 000 jetons générés n'est pas une tâche longue. Le pilote ne dit rien de l'horizon, qui est pourtant l'objet de la question.

**(b) Conditions de perte de puissance**

- **Attribution.** Si le lecteur manque un énoncé avec une probabilité m > 0, le verdict « non attesté » a un taux d'erreur m. Sans énoncés plantés, m n'est pas identifiable.
- **Comblement.** P(aucun témoin | comblement existant) = 1 − c·s, où c est la couverture du corpus et s la sensibilité de l'audit. Aucun des deux n'est estimé.
- **Verdicts suspendus.** Si chaque condition est décidable avec une probabilité q, la probabilité d'un verdict non suspendu est q⁶, soit 0,26 pour q = 0,8. La majorité des verdicts sont alors suspendus.
- **Respect du plafond (c).** Avec 100 traces honnêtes réservées et un plafond de 5 %, un moniteur dont le taux vrai est 8 % passe avec une probabilité d'environ 0,18. « Précision suffisante » n'est pas défini.
- **Duel.** Le nombre de dégradations détectées par le surveillant et manquées par le contrôle mécanique vaut n·(1 − TPR_méc)·TPR. En dessous d'une dizaine, l'intervalle apparié couvre 0 presque sûrement, et l'issue est « ne départage pas ».

**(c) Contrôles négatifs dont l'absence serait fatale**

- **Attribution :** énoncés plantés (positifs connus) et passages leurres en nombre fixé, pour estimer m et le taux de fausse attribution. Le témoin négatif cité (invitation prise pour un engagement) est nommé mais non dénombré.
- **Comblement :** comblements semés dans le corpus et double recherche indépendante.
- **Duel :** la permutation d'alertes est bien prévue. Il manque un surveillant nul (scores aléatoires, même volume d'alertes) pour fixer le plancher du gain, et une analyse de sensibilité sur v/c.

---

## Sur la proposition E

**(a) Défauts de méthode**

1. **E1 : le rapport ρ = TPR_local/TPR_global est mal conditionné.** Deux moniteurs au plancher (TPR ≈ FPR) donnent ρ ≈ 1 et « réfutent » H_B alors qu'aucun ne voit rien.
2. **E1 : confusion d'information.** Le moniteur global reçoit en plus le « différentiel d'état cumulé ». La comparaison confond fenêtre et information.
3. **E1 : mélange et contrôle.** ρ dépend de la proportion de dégradations couplées et atomiques choisie par l'expérimentateur. Le « contrôle négatif » (dégradations atomiques, ρ ≥ 0,95) est un contrôle positif.
4. **E2 : conjonction de deux propriétés sans rapport** (accord et fidélité à l'audit). Un échec n'est pas interprétable. B les sépare, et je préfère cette séparation.
5. **E2 : R_audit non identifié.** Son dénominateur, les limites trouvées par l'audit, croît avec l'effort d'audit. Des auditeurs qui ont lu l'article introduisent une fuite, et les publications à code exécutable sont un échantillon sélectionné.
6. **E2 : contrôles vides.** Les textes synthétiques sans ambiguïté donnent κ ≥ 0,9 par construction. La permutation donnant κ ≈ 0 teste le code, pas l'instrument.
7. **E3 : dénominateur tronqué.** Les « comblements totaux vérifiés » sont ceux qu'a trouvés l'union des méthodes. Ceux que toutes ont manqués en sont exclus.
8. **E3 : voisinage trop large.** Le voisinage à deux sauts d'un article cité peut couvrir une grande part du champ. H_A deviendrait vraie par construction, sans valeur pratique, et ni la taille ni la précision du voisinage ne sont rapportées.
9. **Dominance : ordre partiel.** Le test porte sur quatre dimensions. La « furtivité » n'a pas d'échelle commune entre publications, donc la plupart des paires sont incomparables et « non comblé » l'emporte par défaut.
10. **E4 : co-échelonnement.** L'agent change en même temps que le moniteur, donc la loi des trajectoires dégradées change aussi. Δ_FN confond les deux effets. Il n'y a que deux points, de générations différentes. Le classement « protocolaire » est fait a priori par l'équipe qui teste. Le contrôle sur tâche courte est un contrôle positif.
11. **E5 : prédicteurs dans l'issue.** « Fécond […] non annulé par l'échelle » reprend O₃. Le gain sur le mécanique reprend O₁ et O₂.
12. **E5 : rétrospection.** Restreindre les modèles à ceux d'avant t₀ n'ôte pas la connaissance rétrospective de l'expérimentateur qui conçoit les injections.
13. **I2 : double lecture par modèles.** L'accord entre deux modèles de langue n'est pas un accord entre lecteurs indépendants (HYPOTHÈSE : erreurs corrélées par les corpus d'entraînement partagés).

**(b) Conditions de perte de puissance**

- **E1.** Var(ρ̂) ≈ ρ²[(1−T_l)/(n·T_l) + (1−T_g)/(n·T_g) − terme de covariance]. Le rapport n'est pas jugeable pour T_g ≤ 0,2 à n = 200 dégradées, et il est sans contenu si T_g ≈ FPR.
- **E3.** Le nombre de comblés vaut 50·π. Pour π = 0,2, une observation de 8/10 a un IC95 d'environ [0,44 ; 0,97], qui chevauche 0,80.
- **E4.** Avec 100 dégradées et FNR_8B = 0,4, une réduction relative de 25 % vaut 0,10 en absolu, pour une ET appariée de 0,05 à 0,07. Pour FNR_8B ≤ 0,15, la mesure n'est pas jugeable.
- **E5.** Si chaque critère est satisfait avec une probabilité 0,5 et indépendamment, la conjonction O₁∧O₂∧O₃∧O₄ retient 24/16 ≈ 1,5 manque. P(succès | O₁..₄) est alors estimée sur un ou deux items.
- **O₃.** Avec environ 15 trajectoires dégradées, l'ET de l'écart de TPR entre deux moniteurs est d'environ 0,18. La « pente » n'est pas estimable.

**(c) Contrôles négatifs dont l'absence serait fatale**

- **E1 :** moniteur nul et condition de plancher (TPR_global significativement supérieur au FPR), puis moniteurs à information égale.
- **E3 :** capture-recapture, et proportion d'articles tirés au hasard qui tombent à deux sauts au plus.
- **E4 :** agent fixe sur traces figées, seul le moniteur changeant d'échelle. L'archivage figé prévu par E le permet ; je m'en sers.
- **E5 :** issue jugée à l'aveugle des scores O, et critère placebo.

---

## Sur la proposition F

**(a) Défauts de méthode**

1. **E1 : deux propriétés couplées.** H_A joint l'accord α_K et la valeur prédictive Δp. Même objection que pour E2 de E ; B les sépare (E1 et E4).
2. **E1 : Δp confondu et non aveugle.** Δp est confondu par les moyens de l'équipe. Rien ne dit que le juge du « suivi » ignore la catégorie de l'énoncé, alors que le masquage des auteurs à l'annotation est bien prévu.
3. **E2 : ρ mesure un désaccord, pas une erreur.** Le pipeline 2 contient le pipeline 1 plus une recherche élargie et un audit plus strict. ρ_FN ≥ 0 et ρ_FP ≥ 0 par construction, et ils croissent avec la sévérité des cinq champs. Il n'y a pas de vérité indépendante.
4. **E2 : test sur artefacts.** Il fait dépendre ρ_FP du taux de disponibilité des artefacts, paramètre étranger à l'hypothèse.
5. **E2 : témoins extrêmes.** Les manques « notoirement comblés » et « construits non comblés » sont des cas faciles. Les quasi-comblements figurent dans I3 mais pas dans E2.
6. **E3 : issue prédite par construction.** L'issue « décisive » inclut le résultat positif et la réfutation. Elle revient à « terminé avec une puissance adéquate sous budget », ce que O2 (coût sous plafond) et O3 (ligne de base reproductible) prédisent par construction.
7. **E3 : pondération non fixée.** La pondération de O1 à O5 n'est pas arrêtée avant les données. Je retiens en revanche le sous-ensemble témoin de pistes défavorables menées à terme : il traite la censure, que l'E3 de C ignore.
8. **E4 : le nul n'est pas 0.** ΔTPR d'une union est ≥ 0 par construction. Un moniteur aléatoire qui consomme le budget α de fausses alertes ajoute environ α·(1 − TPR_méc). Le « FPR apparié » d'une union n'est pas défini tant que le FPR mécanique n'est pas mesuré.
9. **E5 : FPR non comparables.** Les fenêtres locales sont centrées sur l'étape fautive, ce qui suppose une position donnée par un oracle, et leur FPR se compte par fenêtre. Le FPR de la trajectoire complète se compte par trajectoire. Un moniteur local déployé doit balayer L/k fenêtres. La formule 1 − (1−α)^L, que F écrit en (a.1), n'est pas appliquée ici. δ_L est donc gonflé en faveur de H_A.
10. **E5 : cas exclus et troisième issue.** Les dégradations distribuées n'ont pas d'« étape fautive ». Elles sont exclues par construction, alors que c'est le cas que vise H_B dans l'E1 de E. L'issue TPR_local ≥ 70 % avec δ_L < 25 points ne falsifie rien.

**(b) Conditions de perte de puissance**

- **E2.** Avec M = 25, le seuil de 25 % correspond à environ 6 verdicts. L'IC95 de 6/25 est d'environ [0,09 ; 0,45] et chevauche les deux seuils.
- **E3.** Avec K = 20, ET(AUC) ≈ 0,11 à 0,12. ΔAUC = 0,15 vaut environ une ET, et le seuil 0,75 n'est pas séparé de 0,5 avec certitude.
- **E4, calibration.** Sur 50 trajectoires honnêtes, le FPR réalisé d'un seuil placé au quantile empirique 95 % suit approximativement une loi Bêta d'écart type ≈ 0,03. Il peut tomber entre 0,01 et 0,12. Le point à 1 % est hors d'atteinte, puisque le plus petit pas est 1/51.
- **I1, dérive.** Détecter +2 points de FPR entre L = 20 et L = 60 autour de 5 % demande de l'ordre de 1 900 trajectoires honnêtes par longueur (α = 0,05, puissance 0,8). Avec 50 par longueur, l'ET de la différence est d'environ 0,044.
- **E1.** Avec 30 articles, le nombre d'énoncés « futur annoncé » est petit. L'IC de Δp inclut 0 sauf effet massif, et les énoncés d'un même article ne sont pas indépendants.

**(c) Contrôles négatifs dont l'absence serait fatale**

- **E2 :** vérité indépendante sur un sous-échantillon, et quasi-comblements réels dans E2.
- **E4 :** moniteur aléatoire au même volume d'alertes, qui donne le nul de l'union.
- **E5 :** balayage local exhaustif sans position donnée par un oracle, avec FPR compté par trajectoire.
- **E1 :** suivi jugé à l'aveugle de la catégorie, et stratification par taille d'équipe.

---

## Ce que je reprends, en le disant (B1)

- **De B :** la séparation entre fiabilité de l'extraction et valeur prédictive de l'annonce, et le FPR fixé par trajectoire.
- **De F :** le lot de calibration disjoint et le bras témoin de pistes défavorables.
- **De D :** la borne « dans ce corpus seulement ».
- **De C et F :** les quasi-comblements comme négatifs.

Je ne fusionne pas ces éléments en une proposition commune.

## Ce qui réfuterait mes critiques

- Les prévalences (π(annoncé), π_c) et les effectifs de manques datés, une fois mesurés, peuvent dépasser les valeurs que j'ai supposées. Mes verdicts « non jugeable » tombent alors.
- La liste étant absente, aucune de ces grandeurs n'est connue à ce jour.

FIN-DE-CELLULE
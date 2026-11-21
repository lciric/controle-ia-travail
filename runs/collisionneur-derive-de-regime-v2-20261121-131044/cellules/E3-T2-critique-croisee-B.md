# Tour III.2 : critique croisée de méthode (proposition B)

Pièces A, C, D et E : présentes et non coupées ; je n'ai pas contrôlé les empreintes. Les FAITS n'étiquettent aucun statut. Quand une pièce attribue un statut à un élément des FAITS, je signale cette attribution sans la modifier. Tous mes chiffres sont des **calculs illustratifs**. Mes diagnostics sont des HYPOTHÈSES de méthode, pas des résultats.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **D0 (bruit contre dérive) : bande trop étroite par construction.** La bande vient de ré-étalonnages A/A intra-régime tirés épisode par épisode.
   - Les épisodes d'une même tâche ou d'une même session sont probablement corrélés (HYPOTHÈSE). Une coupe aléatoire par épisode produit alors une bande Beta trop étroite.
   - Conséquence : un « hors bande » peut falsifier H_A à tort. Le confondant est la corrélation intra-tâche.
   - Correction : couper par blocs de tâches, et non par épisodes.
2. **D1 (composition contre concept) : non identifiable si la version et le mélange de tâches changent ensemble.** C'est le cas typique d'un déploiement. La post-stratification sur X n'attribue alors rien. Il faut un plan croisé : ancienne version sur nouvelles tâches, nouvelle version sur anciennes tâches. Sans ce plan, les deux issues de D1 ne falsifient rien.
3. **D4 est vrai par construction pour P1 et pour M4.**
   - P1 a un seuil aveugle au flux : son succès sur D4 est garanti et ne teste que l'implémentation.
   - L'échec de l'adaptatif appliqué au flux est lui aussi déterminé par construction.
   - D4 n'est informatif que pour le second volet de P4.
4. **P3 : fuite.** Si la forme de frontière b(t) est choisie, même informellement, sur les témoins qui fixent ensuite le quantile, la garantie « comme en P1 » tombe. Avec une partition séparée, n repasse sous 299, et la garantie (1 %, 95 %) devient impossible avec le dispositif annoncé.
5. **P4, second volet : un confondant est pris pour un signal.** « Dérive du flux sans dérive des témoins » se produit aussi quand une source bénigne présente dans le trafic manque dans la banque de témoins. A traite cela comme un signal de sabotage au niveau population. Le mode d'échec que C (3.6) et D (D-ancre) nomment devient chez A une fausse alarme de sabotage.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Critères « l'intervalle contient 1 % et exclut 3 % ».** Pour x = 3 alertes sur n = 300, la borne supérieure de Clopper–Pearson vaut environ 2,9 % (approximation de Poisson). C'est la limite de jugeabilité.
   - Sur une tranche de 60 épisodes, aucune issue n'est jugeable. Les lignes « strates » du tableau sont donc non jugeables par construction, ce que la règle « essai invalide » de A reconnaît.
   - Si les épisodes sont corrélés par tâche, avec une corrélation intra-classe ρ_c et m épisodes par tâche, le n effectif vaut n/(1+(m−1)ρ_c). Les seuils 299 et 900 de A deviennent alors des minorants.
- **D3 : le test d'uniformité est aveugle là où le risque se loge.** Supposons que la loi du jumeau G et celle de l'agent honnête F diffèrent seulement au-delà de leur quantile 0,98.
   - On a alors sup|F−G| ≤ 0,02. Un test KS à 5 % demande √n_eff · 0,02 ≳ 1,36, soit n de l'ordre de 4 600.
   - Avec quelques centaines de paires, D3 accepte H_A alors que le taux à 1 % peut doubler.
   - Il faut remplacer KS par un test binomial sur le franchissement du seuil.
- **P1 avec le jumeau comme témoin.** Si G est stochastiquement plus petite que F dans la queue seulement, le seuil est trop bas et le taux dépasse α, alors que D3 ne le voit pas.
- **P4, martingale sur témoins.** La croissance attendue est bornée par la divergence de KL par témoin. Pour une dérive de queue de masse ε ≤ 0,02 qui laisse le corps intact, elle est minuscule. Le délai dépasse le volume de témoins d'un régime.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Témoins contre honnêtes cachés du même lot, sans dérive.** A ne le pose que pour le jumeau (D3), pas pour les témoins injectés.
- **Pour P4.** Monde planté « nouvelle source bénigne dans le flux seulement, zéro sabotage ». Le signal « sabotage population » ne doit pas monter.
- **Discriminabilité des témoins.** Un classifieur à deux échantillons, témoins contre production honnête, doit rester à AUC ≈ 0,5. Sinon l'agent peut traiter les témoins à part, et P1 perd sa supposition S5.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Statuts instables dans la pièce.** Je ne les change pas ; je les relève.
   - « quelques centaines » et « relecture rare » sont étiquetés VÉRIFIÉ.
   - Les références bibliographiques sont étiquetées VÉRIFIÉ.
   - Le 3 % reçoit successivement RAPPORTÉ, VÉRIFIÉ et « RAPPORTÉ / VÉRIFIÉ ».
   - L'interdiction de moyenne sur les jetons reçoit à la fois OBSERVÉ-NON-AUDITÉ et VÉRIFIÉ.
   - Conséquence de méthode : plusieurs critères de succès (« ramener un FPR de 3 % [RAPPORTÉ] ») sont indexés sur le chiffre CURA, page non lue, au lieu de la famille plantée. Le critère dépend d'une donnée non auditée.
2. **P1 : fuite entre construction et évaluation.** m(L) et σ(L) sont ajustés sur les épisodes mêmes dont on conformise ensuite les résidus.
   - La « validité conforme exacte » n'est pas acquise sans partition.
   - La « validité conditionnelle à O(N^{-1/2}) » est une affirmation non démontrée dans la pièce : HYPOTHÈSE au mieux.
3. **Expérience 1 : verdict fixé par le générateur.**
   - Sur monde planté, le verdict dépend de la manière dont la dérive a été plantée. Si c'est par le mélange de longueurs, H_A gagne par construction.
   - Sur données réelles, l'expérience est non jugeable (voir b).
   - Les seuils à 1,3 % et 1,5 % laissent une bande où aucune hypothèse n'est falsifiée.
   - « ≥ 70 % de l'excès » n'est mesuré par aucune des métriques déclarées.
4. **TARR : l'ancre est elle-même un régime.**
   - Un bac à sable ou un masque syntaxique modifie le contexte, donc les activations (HYPOTHÈSE). On recalibre alors sur la dérive de l'ancre, pas sur celle du trafic.
   - La variante « premiers pas où les préfixes coïncident » sélectionne des préfixes courts. Elle est confondue avec la longueur, que P1 prétend justement corriger.
   - « Immunité totale » est un superlatif non étayé.
   - « FPR ≤ α + O(K^{-1}) » a le mauvais ordre : l'erreur sur la médiane et la MAD est en K^{-1/2}.
5. **Expérience 2 : l'adversaire est un homme de paille.** L'ACI non étiqueté est déclaré empoisonné par C elle-même. La falsification de H_B dans sa branche « ACI meilleur » est vraie par construction.
6. **SCEM.**
   - λ n'agit pas sur E[e_t | F_{t−1}] : la phrase « λ ajustée pour que E[e_t|F] ≤ 1 » confond la mise et la validité.
   - Δ est estimé sur l'étalonnage, puis l'étalonnage sert de référence aux p-valeurs : c'est une fuite.
   - Des p-valeurs qui partagent un même étalonnage ne sont pas des e-facteurs conditionnellement valides. D le note en général.
   - Comparer un score de pas à la loi des maxima de bloc rend les p-valeurs super-uniformes, mais au prix de la puissance.
7. **Quota top-1 sur 100.** « 1,0 % garanti » est un taux d'alertes, vrai par construction. Ce n'est pas un taux de fausses alertes.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **TARR, bruit d'ancrage du même ordre que l'effet.**
   - Sous loi gaussienne, l'erreur-type de la médiane sur K = 15 vaut 1,253σ/√15 ≈ 0,32σ.
   - Le décalage qui triple le taux vaut environ 0,445σ.
   - Le taux réalisé par lot est donc dispersé de part et d'autre de 1 %. Gonfler c_α pour couvrir ce bruit coûte la puissance que la proposition promet de garder.
- **Les trois expériences (seuils 1,3 % contre 1,5 %).** Séparer ces deux taux à environ 2 erreurs-types demande √(0,014/n) ≈ 0,0005, soit n de l'ordre de 55 000 épisodes honnêtes. Ce n'est jugeable qu'en simulation, où le générateur décide.
- **P1.** P1 perd sa validité par tranche si l'indice de queue ξ ou l'indice extrémal θ varie avec L. Extrapoler des quantiles 0,5 et 0,9 vers 0,99 suppose ξ constant ; l'erreur croît avec |Δξ|.
- **SCEM, sabotage concentré.** Avec κ = 0,5 et n = 300, le plus grand e-facteur possible vaut 0,5 × √301 ≈ 8,7.
   - Il faut donc au moins trois pas extrêmes, même avec λ = 1, pour atteindre 100.
   - Un sabotage sur un ou deux pas est indétectable par construction.
   - Avec λ < 1, il en faut davantage.
- **SCEM, mémoire longue.** Si l'autocorrélation des p_t a une portée supérieure à Δ, la super-uniformité conditionnelle tombe. C le reconnaît.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Ancres de bac à sable exécutées dans l'ancien régime** et comparées à l'étalonnage. Si elles diffèrent, TARR mesure l'effet du bac à sable.
- **Discriminabilité ancres contre trafic honnête** (AUC ≈ 0,5).
- **P1 sans partition contre P1 avec partition, sans dérive**, sur de nombreux tirages d'étalonnage : mesurer le taux marginal réel.
- **Le contrôle par permutation de l'Expérience 1** (« 1,0 % ± 0,2 % ») n'est pas jugeable sur les effectifs réels. Il est donc absent en pratique.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Le critère « ≤ 1 % » n'est pas établissable pour une règle bien calibrée.** Si le taux vrai vaut exactement α, une borne supérieure de niveau 1−δ ne passe sous α qu'avec une probabilité ≤ δ.
   - D-ancre, réglée sur α, ne peut donc presque jamais établir H_A.
   - Seule une règle sur-conservatrice gagne le duel.
   - Le critère récompense la perte de puissance que D veut pourtant chiffrer. Il faut une marge pré-enregistrée, ou un test contre 3 %.
2. **H_A est une conjonction de critères.** Elle est exclusive de H_B par définition, mais :
   - sous H_A vraie, la probabilité d'un faux « au moins une violation » croît avec le nombre de critères ;
   - établir chaque inégalité multiplie les exigences de puissance.
   D mentionne des bornes simultanées, mais ne dit pas qu'elles rendent l'issue « H_A établie » quasi inaccessible avec quelques centaines d'épisodes.
3. **« Meilleur contrôle mécanique admissible ».** Si ce contrôle est choisi après observation, la comparaison est biaisée. Il doit être fixé à l'enregistrement.
4. **Recomposition du §1.** Les taux conditionnels par tâche à 1 % sont estimés sur quelques épisodes par tâche. L'« écart résiduel » est dominé par la variance des cellules et n'est pas interprétable.
5. **Statuts.** D marque VÉRIFIÉ la garantie de transport par addition. Ce statut porte sur l'implication : son antécédent, une enveloppe vraie, reste une HYPOTHÈSE. Aucune expérience du §4 ne peut confirmer l'implication sur données réelles, seulement sur une famille plantée.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **D-enveloppe avec ε uniforme sur tous les seuils.** C'est une distance de Kolmogorov.
   - Pour la famille gaussienne qui triple (décalage 0,445σ), elle vaut 2Φ(0,2225) − 1 ≈ 0,18.
   - U + ε ≤ 0,01 est alors impossible : le certificat est vide sur la famille de test.
- **D-enveloppe restreinte aux seuils hauts.**
   - Au seuil t ≈ 2,77σ, la queue décalée vaut 1 %, la queue de référence ≈ 0,28 % et ε ≈ 0,72 %.
   - Il faut U ≤ 0,28 %. Même sans dépassement observé, cela demande n ≳ ln(20)/0,0028 ≈ 1 070 épisodes honnêtes par strate.
   - Avec quelques centaines, le certificat n'est jamais délivré.
- **D-ancre.** Il faut au moins 99 témoins par cellule.
   - Les alertes d'un même lot partagent les témoins. Le taux réalisé par lot suit approximativement une Beta(1, m).
   - Pour m = 99, P(taux > 3 %) ≈ 0,97^99 ≈ 5 % par lot.
   - Un audit par lot est donc bruité, même sous validité.
- **Jumeau.** La variante D du jumeau perd en puissance si la corrélation agent–jumeau est inférieure à 0,5, car Var(D) > Var(S) (formule de A, variances égales supposées).

### (c) Contrôles négatifs dont l'absence serait fatale

- **Discriminabilité des témoins injectés.** D nomme le risque « témoin reconnaissable » sans le mesurer.
- **Pipeline d'injection en régime stationnaire**, témoins injectés contre étalonnage. L'injection elle-même ne doit pas déplacer la loi.
- **Règle calibrée exactement à α sur lots stationnaires** : elle doit faire apparaître la non-établissabilité du point 1. Sinon, le banc récompense le conservatisme sans qu'on le voie.
- Le contrôle négatif « lots stationnaires, revue rejouée » est présent. C'est un point fort.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Proposition 3 : la récurrence n'est pas une surmartingale.** E écrit M_s = (1−λ) + λ·(½ p^{-1/2})·M_{s−1}.
   - Sous le nul, E[M_s | F] = 1−λ + λM_{s−1}, qui est supérieur à M_{s−1} dès que M_{s−1} < 1.
   - Le processus revient vers 1 et franchit 1/α une infinité de fois sur un horizon infini (HYPOTHÈSE de stationnarité ergodique).
   - Ville ne s'applique pas. « Quelle que soit T_e » est faux, et le taux de fausses alertes croît avec la longueur, soit exactement le défaut à corriger.
   - La forme multiplicative de C, M_{t−1}(1−λ+λe_t), n'a pas ce défaut.
2. **Canary-eMix : le nul n'est pas conditionnel à l'étalonnage.**
   - Sachant D_cal, P(V=1) est le taux réalisé de q_init. Avec n = 300 et k = 3, il dépasse 2 % avec une probabilité d'environ 6 % (calcul Beta de A).
   - Dans ces cas, E[e_j | D_cal] > 1 et la martingale révoque sans dérive. La borne β ne tient plus, faute de dérive à détecter.
   - De plus, « accélère d'un ordre de grandeur » n'est ni marqué illustratif ni étayé.
3. **PF-Gumbel : le jumeau en préfixe forcé lit les jetons du sabotage.** Si la sonde capte en partie le contenu, la soustraction retire aussi le signal (HYPOTHÈSE).
   - Le confondant est le contenu contre l'intention.
   - Π⊥ est estimé sur l'étalonnage qui sert ensuite au quantile conforme : c'est une fuite.
   - Le contrôle « auto-jumeau = 0 » est vrai par construction et ne teste que la tuyauterie.
4. **D1 : la falsification est mal dirigée.** Une borne supérieure ≤ 1,5 % ne falsifie pas H_B (« la queue conditionnelle dérive ») : un excès relatif de 50 % reste compatible. L'issue ne fait que borner H_B.
   - D2 a une troisième issue : le taux baisse mais le rappel chute.
   - D3 sur monde planté dépend du générateur, qui décide si les sabotages bougent avec les honnêtes.
5. **Cascade.** La borne B_humain/M est vraie par construction. C'est un taux d'alertes : « ne peut jamais tripler » ne dit rien des fausses alertes.
6. **Statuts.** E étiquette la fragilité du jumeau OBSERVÉ-NON-AUDITÉ, quand C étiquette la même phrase VÉRIFIÉ. Je ne tranche pas. Les critères de D2 héritent d'un statut que les FAITS ne fixent pas.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Canary-eMix, terme binaire.** Le gain logarithmique par ancre est au plus de l'ordre de KL(Bern(0,03) ‖ Bern(0,01)) ≈ 0,013 nat (calcul de E), et il est divisé par le mélange à ½.
   - Atteindre ln(20) ≈ 3 demande plus de 230 ancres, soit plus de 2 300 épisodes de production à η = 10 % (borne inférieure approximative).
   - Le taux reste triplé pendant tout ce délai.
- **Canary-eMix, terme p^{-1/2}.** Si la dérive porte sur la queue seule (masse ε ≤ 0,02), la loi des p_j est quasi inchangée dans le corps, et E[½ p^{-1/2}] reste proche de 1.
- **PF-Gumbel.** PF-Gumbel perd sa validité par tranche si θ ou ξ dépend de la version ou de la tâche, ou si K_e est corrélé à θ.
- **Cascade.** La cascade est aveuglée dès que la proportion d'honnêtes à score élevé d'un sous-régime atteint B_humain/M. C'est le test de mort de E, et il est bien posé.
- **D1 et D2 (seuil 1,5 %).** Ils sont non jugeables sur données réelles pour les mêmes raisons d'effectif que chez C.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Épisodes honnêtes stationnaires longs.** Mesurer la fraction d'alarmes de la Proposition 3 en fonction de T_e. Ce contrôle aurait révélé le point (a)1.
- **Sabotages plantés évalués en préfixe forcé.** Comparer le rappel du résidu à celui de l'agent seul.
- **Révocations sans dérive sur de nombreux tirages indépendants de D_cal**, et pas sur un seul étalonnage.
- **Discriminabilité ancres contre production.** E pose « indiscernables » comme hypothèse sans la mesurer.

---

Contrôle qu'aucune pièce ne rend obligatoire et que je retiens pour B : une famille de dérive plantée cachée à tous les proposants. Les quatre conceptions sont réglées, explicitement ou non, contre la famille qui triple décrite dans les FAITS. Un succès sur cette seule famille est donc en partie vrai par construction.

FIN-DE-CELLULE
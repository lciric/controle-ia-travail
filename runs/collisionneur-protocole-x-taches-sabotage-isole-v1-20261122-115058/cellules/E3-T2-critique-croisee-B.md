# Proposition B, tour III.2 : critique croisée de méthode

## 0. État des pièces et statut de cette critique

- Les quatre pièces A, C, D et E sont présentes et se terminent toutes par leur marqueur de fin. Je n'y vois aucune coupure.
- Dans le tableau (c) de C, la formule de I₄ contient un délimiteur cassé (`\}`). C'est une coquille, pas une troncature.
- Les blocs FAITS et QUESTION ont la même empreinte. Ils ne contiennent aucun fait muni d'un statut.
- Toutes mes critiques sont des **HYPOTHÈSES** méthodologiques.
- Les calculs de puissance ci-dessous partent des effectifs et seuils des pièces, qui sont eux-mêmes illustratifs. Leurs résultats sont donc **illustratifs**.
- Je ne modifie aucun statut attribué par une autre proposition. Quand un statut me paraît sans appui dans la pièce, je le signale et l'arbitre tranche.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **Le levier n'est pas indépendant de la difficulté, contrairement à ce que pose A.** Le biais induit par un mauvais choix (le levier) et la lisibilité du diagnostic qui révèle le bon choix sortent souvent du même paramètre du générateur. Exemple : des valeurs extrêmes plus grandes biaisent davantage et se voient aussi davantage. Si c'est le cas, Cov_hon(erreur, levier) ≠ 0 mécaniquement, et la statistique L mesure la lisibilité, pas le ciblage. A vérifie l'indépendance pour le régime (taux marginaux égaux entre ADD et INT), mais pas pour le levier.

2. **L'excès de conjonction X mélange deux bras.** X est défini comme le taux de conjonction du bras sabotage moins le produit des taux marginaux du bras honnête. Un saboteur qui dévie plus souvent, sans aucune coordination, obtient donc X > 0. L'indépendance doit être testée à l'intérieur de chaque bras :
   - P_sab(conj) − ∏ P_sab(dévier_j) ;
   - puis la même grandeur pour le bras honnête ;
   - et seulement alors la différence des deux.

3. **Le contrôle « X nul sur le bras honnête » suppose l'indépendance des erreurs honnêtes.** Un modèle qui confond confondant et collisionneur se trompe sur plusieurs décisions liées à la fois. Son X est positif sans intention. Le contrôle échouerait pour une raison étrangère au sabotage, et A ne prévoit pas de lecture de ce cas.

4. **En E3, la chute par construction ne vaut que pour une partie des mesures.** « En INT, toute mesure par action a un signal nul » est vrai pour une mesure fondée sur le dommage marginal. Ce n'est pas vrai pour la *surprise maximale sous la politique honnête*, qui détecte la déviation et non le dommage. H_B mêle ces deux sens de « par action ». Un résultat H_A obtenu par la surprise ne contredirait pas l'énoncé de A sur le dommage.

5. **Le saboteur informé de la conjonction (E3) transmet la structure plantée à l'agent évalué.** X mesure alors l'obéissance à une consigne qui contient la réponse. Il faut le présenter comme une borne, jamais comme une performance de détection. A le fait en partie (« borne haute »).

6. **Le repli par ajustement (saboteur verrouillé par mot de passe) crée une fuite.** Les données d'ajustement seraient produites par le même générateur que les instances de test. Le saboteur apprendrait la signature du générateur. Il faut séparer les familles de générateurs entre ajustement et évaluation.

7. **E2 conditionne sur l'issue.** Les trajectoires retenues sont celles où D dépasse le 95ᵉ centile honnête. Ce sous-ensemble est enrichi en sabotages grossiers. La « zone niable » est donc estimée sur la partie la moins niable, ce qui biaise vers H_B.

8. **En E4, l'appariement au chemin le plus proche est mal défini quand plusieurs chemins donnent des β̂ voisins.** Si les 256 valeurs de β̂ sont denses, le critère « couverture ≥ 80 % » est rempli presque par construction. Et c_hon en version libre est déduit de cet appariement, donc la comparaison est circulaire.

### (b) Lois sous lesquelles les critères perdent leur puissance

- **G**, appariement par instance, écart-type σ_d des différences D_sab − D_plac. La puissance de 90 % à α = 0,05 bilatéral exige G ≥ 3,24 σ_d/√n, soit G ≥ 0,23 σ_d pour n = 200. Avec un taux de refus r sous consigne de sabotage, l'effet observé devient (1 − r)·G_exéc + r·(E[D | refus] − E[D_plac]). G n'est plus jugeable quand r → 1, ou quand E[D | refus] dépend du traitement des sorties invalides.
- **c < 0,5.** Si le saboteur cible une fraction f des décisions, c_sab = (1 − f)·c_hon. On a c_sab < 0,5 seulement si f > 1 − 0,5/c_hon. Avec c_hon = 0,8 (illustratif), il faut f > 0,375. Un saboteur défendable reste sous ce seuil, donc le critère est sans puissance contre la cible même du scénario.
- **L.** Si le levier ne prend que deux valeurs, avec P(fort) = π, on a Var(ℓ) = π(1 − π)(ℓ_fort − ℓ_faible)². Var(ℓ) tend vers 0 quand π tend vers 0 ou 1. L n'est plus jugeable si P_hon(e = 1 | ℓ) varie avec ℓ (point a1), sauf à comparer L_sab − L_hon.
- **X.** La ligne de base honnête est q = P_hon(conj). Si q ≈ p^m = 10⁻³ (exemple de C, illustratif) et n = 200, la probabilité de n'observer aucun événement vaut (1 − q)^n ≈ 0,82. La ligne de base est alors non estimable et X n'est pas jugeable.
- **Détecteurs E2.** Trois détecteurs réglés chacun à 5 % donnent un taux de fausses alertes de la famille compris entre 5 % et 14,3 % (1 − 0,95³ sous indépendance). Il faut calibrer l'union. De plus, si N_hi trajectoires dépassent le 95ᵉ centile, l'intervalle sur une proportion de 0,2 a une demi-largeur d'environ 1,96·√(0,16/N_hi), soit ≈ 0,14 pour N_hi = 30 : le seuil de 20 % n'est pas tranchable. Enfin, la surprise perd sa puissance quand la divergence pas à pas KL(π_sab(·|h) ‖ π_hon(·|h)) est faible sur la plupart des pas.
- **E3.** Avec environ 200 cas par classe, l'erreur type d'une AUC vers 0,8 est de l'ordre de 0,03 (approximation de Hanley–McNeil). Celle d'une différence d'AUC est d'environ 0,04. La marge de 0,05 n'est donc pas jugeable.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Levier permuté.** Recalculer L et X avec le levier ou la conjonction tirés d'une *autre* instance. Le signal du saboteur doit disparaître. Sans ce contrôle, on ne sait pas si L capte la structure plantée ou une propriété générique.
- **Honnête à méprise systématique**, à basse température, sur un type de décision. C'est le seul cas honnête qui produit à la fois X > 0 et une erreur directionnelle. Il est absent de A.
- **Prédictibilité du levier depuis la surface.** Un classifieur sur les traits observables de l'instance doit prédire le levier au niveau du hasard. Sinon, le point a1 n'est pas exclu.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Statuts sans appui dans la pièce.** Je les signale sans les modifier :
   - « aucun banc publié […] [VÉRIFIÉ] » : une absence n'est pas établie par la pièce ;
   - « le levier ne nécessite pas de ré-exécuter le modèle [VÉRIFIÉ] » ;
   - la licence de Qwen2.5 [VÉRIFIÉ].

2. **Le levier ℓ_t se calcule par rejeu du pipeline, sans l'agent.** ℓ_t mesure ce que ferait le *calcul* si a_t était remplacé. Il ignore ce que l'agent aurait fait ensuite après d'autres observations. ALD et ρ̂ portent donc sur un contrefactuel de pipeline, pas sur un contrefactuel d'agent. Cela n'est pas dit.

3. **La température est confondue avec l'intention.** Les erreurs honnêtes à fort Δ viennent d'un échantillonnage à T_emp ∈ [0,7 ; 1,2]. Des erreurs à haute température sont diffuses. Un sabotage est concentré. Un détecteur de concentration séparera les deux par construction : l'AUC mesurera la température, pas l'intention.

4. **Fuite entre calibration et évaluation.** d_t (de type IRT) est estimé sur des trajectoires honnêtes. Rien ne dit qu'elles sont disjointes de celles qui servent à estimer les fausses alertes d'ALD. Si elles se recoupent, les fausses alertes sont sous-estimées.

5. **CUSUM-P est vrai par construction pour tout biais de signe constant.** Si la consigne fixe le sens de la dégradation, la cohérence sous permutation est imposée par la consigne. Un biais conceptuel honnête (toujours une jointure interne, par exemple) donne aussi un indice égal à 1. Les permutations de surface ne cassent que les biais de position.

6. **E3 est circulaire.** ρ_vrai est défini par rejeu avec remplacement, et ρ̂ par le même rejeu sur les pas signalés. Si le détecteur retrouve les pas substitués, ρ̂ = ρ par identité. De plus :
   - les « points de décision critiques » où l'on substitue sont choisis avec la vérité terrain ;
   - ALD utilise le levier calculé avec cette même vérité ;
   - l'épissage d'actions de sabotage dans une trace honnête rompt le lien entre actions et observations, ce qui crée un artefact d'incohérence détectable.

   Enfin, C pose lui-même la non-additivité (présupposé 3). ρ est alors mal défini, et ρ̂ peut sortir de [0, 1].

7. **Le contrôle négatif de E1 (honnête A contre honnête B, tirés au hasard) donne une AUC de 0,5 par construction**, quel que soit le détecteur. Il n'éprouve aucune confusion. Il ne règle que la variance de l'estimateur.

8. **Le contrôle de E2 compare un agent aléatoire uniforme à « p³ + 0,02 »**, où p est le taux d'erreur honnête. La référence doit être le p de l'agent aléatoire lui-même, élevé à la puissance m.

9. **Le critère τ_furtif repose sur un vérificateur de schéma et de bornes.** Passer ce vérificateur ne teste pas la défendabilité au sens du scénario. τ_furtif ≥ 0,25 est donc presque acquis d'avance.

### (b) Lois sous lesquelles les critères perdent leur puissance

- **ALD.** Si d_t est estimé sur n_h passages honnêtes et que le vrai d_t est proche de 0, on obtient d̂_t = 0 avec probabilité (1 − d_t)^{n_h}. Le ratio vaut alors ℓ_t/ε, et la statistique dépend du choix de ε. ALD n'a plus de puissance quand Cov_hon,t(e_t, ℓ_t/d_t) = Cov_sab,t(e_t, ℓ_t/d_t), notamment si P_hon(e_t) croît avec ℓ_t.
- **CUSUM-P à K = 4, magnitudes égales.** L'indice ne prend que les valeurs {0 ; 0,5 ; 1}. Si les signes honnêtes sont indépendants et équiprobables, P_hon(I = 1) = 2^{1−K} = 0,125. Le plafond de fausses alertes de 0,10 visé par C est inatteignable, sauf aux magnitudes inégales. Si P_hon(signe constant) = 1 (biais conceptuel), la puissance est nulle.
- **ISE.** Les négatifs requis (R_comb, au moins 3 erreurs honnêtes, même perte finale) ont une probabilité de l'ordre de p³. Avec n_neg négatifs sans alerte, la borne haute à 95 % vaut environ 3/n_neg (règle de trois). Il faut n_neg ≥ 30 pour garantir des fausses alertes ≤ 0,10. Sinon, le critère n'est pas jugeable.
- **r(ρ, ρ̂) avec α à 5 niveaux.** On a r² ≈ Var_entre/(Var_entre + Var_erreur). La variance entre niveaux gonfle r même quand l'erreur intra-niveau est grande. La MAE doit être rapportée par niveau, face au prédicteur constant.
- **Appariement à ± 5 % de Δ.** Si P_hon(Δ ∈ support de Δ_sab) est petite, la positivité échoue. L'échantillon apparié se réduit à la queue honnête, et l'estimande change.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Honnête à basse température avec méprise conceptuelle**, apparié en Δ. Il est fatal pour ALD et CUSUM-P. C n'a qu'un honnête à haute température et un biais de position.
- **Épissage honnête-sur-honnête.** Il faut greffer des actions tirées d'une *autre* trajectoire honnête, mêmes points, même fraction α. On doit obtenir ρ̂ ≈ 0. C'est fatal pour E3.
- **Saboteur à direction tirée au hasard par instance**, pour lever la confusion du point a5.
- **Calibration de d_t sur des instances tenues à l'écart.**

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Le duel « composition » est vrai par construction.** Ses deux issues portent sur des données de test (fixtures) que le concepteur écrit lui-même. Refuter H_A revient à trouver un défaut de spécification. Aucune des deux issues ne renseigne sur l'agent. D le reconnaît en partie (« interaction du calcul »). C'est un test unitaire, pas un duel au sens de B4.

2. **Contamination du duel « transfert ».** Les dossiers viennent de « rapports publics à résultats recalculables ». Un modèle peut en avoir vu les résultats à l'entraînement. Le score honnête en version libre peut alors venir de la mémoire et non de l'exploration. Cela confond le format avec le rappel.

3. **La cible de dommage est grossière.** S est une fraction de conclusions exactes. Un sabotage qui déplace une magnitude sans changer la conclusion est invisible. Le dommage maximal mesurable est borné par la granularité 1/m, où m est le nombre de conclusions par dossier.

4. **Le filtre de fuite de consigne n'est pas défini.** D écrit qu'« un détecteur fondé sur une fuite de consigne ne compte pas », sans critère mécanique. Un petit modèle verbalise souvent l'objectif (HYPOTHÈSE) : le détecteur lirait alors une déclaration, pas un comportement.

5. **Rien ne vérifie que l'objectif privé a été suivi**, en dehors du contrôle de paraphrase. Avec un modèle de 3 milliards de paramètres, Δ > 0 peut venir de la confusion. D en convient, mais aucune mesure ne sépare les deux cas.

### (b) Lois sous lesquelles les critères perdent leur puissance

- **Δ apparié, n = 24 dossiers.** La demi-largeur de l'intervalle vaut t₀,₉₇₅;₂₃·σ/√24 ≈ 0,42σ. Avec σ = 0,25 (illustratif), elle vaut ≈ 0,11. Il faut Δ̂ > 0,21 pour réfuter H_B, et Δ̂ < −0,01 pour réfuter H_A. Entre les deux, aucune conclusion n'est possible.
- **Plafond de fausses alertes de 5 %.** Avec zéro alerte sur n_h sessions honnêtes, la borne de Clopper–Pearson unilatérale à 95 % vaut 1 − 0,05^{1/n_h} : ≈ 0,117 pour n_h = 24, ≈ 0,061 pour n_h = 48. Le respect du plafond n'est pas jugeable au pilote, ce que D annonce. Le gain de sensibilité de 0,10 ne l'est pas non plus, car l'erreur type d'une proportion sur 24 sessions est d'environ 0,10.
- **Transfert.** Une différence de deux différences a une variance d'environ 2·Var(Δ̂). Avec la marge de 0,10, il faut un effectif environ quatre fois supérieur au pilote pour trancher.
- **S discret.** Si m est petit, P(S_H = S_D) est élevée. La loi de S_H − S_D a une masse en 0 qui réduit la puissance de tout test fondé sur un intervalle normal.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Version contrefactuelle des rapports**, aux chiffres modifiés. Si l'agent honnête rend les valeurs publiées d'origine, le score mesure la mémoire. C'est fatal pour le duel « transfert ».
- **Détecteur restreint aux traces dont toute mention de l'objectif a été retirée mécaniquement**, par recouvrement de n-grammes avec la consigne privée. C'est fatal pour le duel « détecteur ».
- **Honnête à méprise systématique dans la zone appariée en perte.** D mentionne « type d'erreur comparable » sans prévoir de quoi le produire.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Statuts sans appui dans la pièce.** Je les signale sans les modifier :
   - « VÉRIFIÉ, par analogie » avec Oaxaca–Blinder : une analogie ne vérifie pas ;
   - identification cardinale de ρ « VÉRIFIÉ algébriquement sous restriction d'exclusion », sans dérivation dans la pièce ;
   - croissance en √T du rapport signal sur bruit « VÉRIFIÉ », qui suppose l'indépendance des pas.

2. **Contradiction interne.** Le présupposé 2 de E pose Δ_inter ≠ 0. Or E1 et E4 notent MAE(ρ̂) comme si ρ = Δ_int/L_tot était bien défini. Sous interaction, ρ dépend de l'ordre d'attribution. Pour un épisode de saboteur pur (E4), ρ est indéfini, puisque l'épisode contient aussi des erreurs honnêtes.

3. **La température est confondue avec l'intention**, comme chez C : contrôle honnête à 0,9.

4. **Le cadrage honnête orienté n'est un contrôle difficile que s'il est aligné sur la direction du sabotage.** E n'impose pas cet alignement. S'il est indépendant de la polarité S_i, I1 le rejette trivialement.

5. **I1 ne voit que le sabotage directionnel.** Un saboteur uniforme correspond au cas d'impossibilité 2 de E lui-même. Il donne une différence nulle entre S = +1 et S = −1, donc ρ̂ ≈ 0 et une MAE élevée. Le critère confond ainsi « estimateur défaillant » et « saboteur hors classe ».

6. **Fuite possible en E2.** Les coupes minimales doivent être extraites de la *trace* de l'agent. Si elles viennent de la topologie conçue par l'expérimentateur, l'instrument connaît l'emplacement des pièges.

7. **E3 confond l'effet d'observateur avec la charge.** Ajouter 8 tables (16 → 24) change la longueur du contexte et la quantité de matière. Le C2ST détectera la charge. De plus, le « corpus réel » expose au même risque de contamination que D.

8. **M3 vaut 0,5 par construction, puisque l'appariement se fait sur |Y − Y*|.** C'est une vérification de l'appariement, pas une référence à battre. La référence informative manque : une régression de l'erreur sur les traits de surface.

9. **La sonde I4 apparie un modèle de 7B et un modèle de 3B.** La sensibilité au bruit sur les poids dépend de la taille. La confusion entre taille et rétention de capacité est entière.

### (b) Lois sous lesquelles les critères perdent leur puissance

- **I1 par trajectoire.** La différence de moyennes porte sur environ 12 items par polarité, d'où une variance d'environ σ²/6. I1 n'a plus de puissance quand P_hon(err | S = +1) − P_hon(err | S = −1) égale la même quantité sous sabotage. C'est le cas d'un biais honnête corrélé à la polarité, ou d'un sabotage uniforme.
- **MAE(ρ̂) avec ρ ~ U[0, 1].** Le prédicteur constant ρ̂ = 0,5 a une MAE de 0,25. Le seuil de 0,12 n'est interprétable que face à cette référence, que E ne déclare pas.
- **C2ST.** Avec N cas de test par classe, l'écart-type de l'exactitude au hasard vaut 0,5/√(2N), soit ≈ 0,05 pour N = 50. Le seuil de 0,58 est alors à 1,6 écart-type : fausses alertes d'environ 5 %, et puissance faible contre une distorsion réelle de taille modérée.
- **d de Cohen ≥ 0,6.** Si la variance honnête est presque nulle (décodage presque déterministe), d grandit sans borne et le critère est rempli trivialement.
- **I3 à fausses alertes de 0,05.** Comme chez C, les négatifs honnêtes qui activent un tuple de taille k sont de probabilité ~p^k. Le taux de fausses alertes *conditionnel à l'activation* n'est pas estimable avec 100 épisodes honnêtes.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Contrôle de charge pour E3** : ajouter 8 tables naturelles, non conçues pour l'audit. C'est fatal pour l'interprétation en effet d'observateur.
- **Honnête à cadrage aligné sur la direction du sabotage**, à basse température. C'est fatal pour I1.
- **Instrument I3 aveugle à la conception** : les étiquettes de pièges sont permutées, et le rappel doit tomber au niveau du hasard.
- **Contamination** : versions du corpus réel aux chiffres altérés, comme pour D.

FIN-DE-CELLULE
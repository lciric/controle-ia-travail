# Tour III.2 — Critique croisée de méthode (proposition A)

**État des pièces.** Les pièces B, C, D et E sont présentes et se terminent chacune par leur marqueur. Je ne peux pas vérifier les empreintes. Le bloc FAITS ne contient aucun fait muni d'un statut. Ma propre conception du tour III.1 ne figure pas dans ce qui m'est transmis ; je n'en invoque donc aucun contenu.

**Statut de ce qui suit.** Toute critique est une HYPOTHÈSE de méthode. Les calculs sont dérivés des chiffres illustratifs des pièces, sous les hypothèses que j'indique ; ils sont eux-mêmes illustratifs.

**Référence.** La date de Greenblatt et al., *AI Control*, diffère selon les pièces : 2023 pour B et D, 2024 pour C, 2024 avec prépublication 2023 pour E. Référence à vérifier.

**Statuts.** C et E apposent VÉRIFIÉ sur des éléments que le bloc FAITS ne statue pas : l'énoncé lui-même, des références « citées de mémoire », des propriétés d'un générateur non encore construit. Je ne modifie aucun statut. Je ne m'appuie sur aucun de ces éléments comme vérifié.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **P2 est en partie vraie par construction.** La comparaison détecte par l'écart D = e_chaîne − e_réf, et ρ est la corrélation de ces mêmes erreurs. Si ρ est estimé sur les trajectoires qui servent à mesurer la puissance, la pente négative est arithmétique.
2. **ρ confond deux paramètres d'effets opposés.** Posons e_chaîne = b + u et e_réf = λb + v, avec Corr(u,v) = r et variance commune σ². Alors le rapport signal sur bruit de D vaut (1−λ)·b / (σ·√(2(1−r))). La puissance décroît avec λ (biais adverse partagé) et croît avec r (bruit honnête partagé, effet d'appariement). Un ρ unique mélange les deux, et le signe de la « pente en ρ » n'est pas identifié.
3. **R2 confond corrélation et compétence.** Une autre famille de modèles change aussi le taux d'erreur marginal.
4. **s ne détermine pas la métrique.** s est une aire sous la courbe ROC, la métrique est un taux de détection à 1 % de fausses alertes. La première ne fixe pas la seconde hors d'une famille à un paramètre. Le « meilleur moniteur local » est de plus choisi sans jeu disjoint annoncé : c'est une fuite de sélection.
5. **P3 est circulaire pour les moniteurs locaux.** Si la détection agrégée est une fonction des scores par acte et que s est remesuré après l'attaque, « retomber sur la courbe » est attendu. Le seul contenu non trivial est l'absence d'effet sur les autres instruments.
6. **L'adaptation LoRA de l'attaque déplace la référence.** B ne dit pas si R1 est le modèle de base ou le modèle adapté. Selon le choix, ρ change par construction.
7. **Le contrôle négatif de E4 contredit H_A.** Si l'unification est vraie, les étiquettes de cadre sont échangeables. La fonction f réajustée après permutation doit alors réussir. Le contrôle « échoue » précisément quand H_A est vraie.
8. **Le modèle nul de E4 est faible en forme.** La moyenne du cadre ignore k ; toute fonction monotone de k la bat.
9. **La dépendance de f en ρ n'est pas identifiée.** f est ajustée sur le seul cadre 1, où rien n'indique que ρ varie. La prédiction dans le cadre 2 est une extrapolation de forme fonctionnelle.
10. **k est confondu avec le type d'acte.** À Δ fixé, k = 1 exige une exclusion massive et k = 32 des arrondis.
11. **H− est sélectionné sur l'issue.** Les trajectoires honnêtes « de même Δ » sont atypiques. La proportion de H− dans le mélange de calibration fixe le seuil à 1 %, donc le taux de détection.
12. **Le croisement k* dépend des taux de change.** Les coûts 1/50/500 sont arbitraires. L'existence de k* dans [1, 32] peut être fabriquée par l'unité de coût.
13. **La sonde peut lire la consigne.** Le sabotage est implanté par consigne, sans contrôle de fuite. J'emprunte ici, en le disant, le contrôle « adversaire LoRA sans consigne » de C.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Agrégation par somme.** Soit k actes sabotés parmi T, de décalage moyen μ(Δ/k) et d'écart-type honnête σ. Le rapport signal sur bruit de la somme vaut k·μ(Δ/k)/(σ√T).
  - Si μ est linéaire en l'amplitude, il est constant en k : pas de décroissance, donc pas de croisement.
  - Si μ est concave, il croît avec k.
  - Si μ est convexe ou à seuil, il décroît.
  - P1 est donc une hypothèse sur la courbure de μ, non mesurée.
  - T varie de 30 à 80 et n'est pas contrôlé.
- **Parcimonie.** En régime épars, la détectabilité dépend de deux paramètres (fraction et amplitude). C'est la leçon du cadre que B cite de Donoho et Jin (référence de B, à vérifier). Un s scalaire ne suffit pas.
- **Seuil à 1 %.** Avec environ 600 trajectoires honnêtes par condition, le quantile 0,99 repose sur environ 6 dépassements. Sa variance domine. Le bootstrap doit rééchantillonner le seuil.
- **ρ de Pearson.** Il est instable si Var(e_chaîne honnête) ≈ 0, et borné par les marges si les erreurs sont rares et binaires.
- **Pente de E2.** Six points au plus (3 références × 2 régimes). Si les ρ sont groupés, la demi-largeur de 0,1 est inatteignable et H_B n'est pas établissable.
- **Tolérance de E4.** Les conditions saturées (taux de détection sous 0,1 ou au-dessus de 0,9) sont prédites à ± 0,10 par n'importe quelle f saturante. Si elles dépassent 80 % des conditions, H_A est acquise sans contenu.
- **Dépendance des conditions.** Elles partagent tâches et moniteurs. L'effectif réel derrière « 80 % des conditions » est bien inférieur à leur nombre.
- **Regret de E5.** Si l'objectif est plat près de l'optimum, le regret est petit par construction.

### (c) Contrôles négatifs dont l'absence serait fatale

- ρ, ou mieux λ et r séparément, estimés sur des tâches honnêtes disjointes de celles qui mesurent la puissance.
- Un modèle nul fort pour E4 : courbe en k ajustée par cadre, et f avec ρ permuté entre conditions.
- Un plafond de bruit : erreur de f sur des conditions du cadre 1 tenues à l'écart.
- Un adversaire sans consigne en contexte (emprunt à C).
- Une stratification par type d'acte et par T.
- Une analyse de sensibilité aux unités de coût.
- Dans E5, la preuve préalable que la politique optimisée sur place bat l'allocation aléatoire.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Fuite entre construction de l'adversaire et évaluation.** L'adversaire est obtenu par rejet sous le « 95e centile de suspicion d'une étape honnête ». Si ce score est M_texte ou M_act, le détecteur max_t S_t est tronqué par construction et le décalage moyen subsiste. Le gain du CUSUM sur le maximum mesure alors la forme de la contrainte imposée, pas une propriété du sabotage. Un adversaire contraint sur la somme cumulée inverserait le résultat.
2. **L'argument √T contre T suppose E[erreur honnête] = 0.** Un agent honnête ancré dérive aussi linéairement. Le contrôle « température 1,0 et distracteurs non orientés » gonfle la variance sans créer de biais directionnel : c'est le contrôle facile. Le contrôle difficile est le « biais d'ordre honnête » de E, que je reprends ici en le disant.
3. **Réglages du CUSUM.** Les « scores blanchis », la valeur de référence et le seuil ne sont pas assignés à un jeu disjoint. Un réglage sur le Δ connu est un réglage oracle.
4. **H_A de l'expérience 2 est une disjonction** (variance trop haute ou rigidité avec M_act élevé), avec λ libre. Le composite peut réussir par M_act seul ; la comparaison serait alors créditée d'un effet de sonde.
5. **L'expérience 3 teste une impossibilité avec un attaquant fini.** Un échec d'optimisation compte comme « taxe d'évasion ». Le contrôle monocouche est un bon contrôle positif, mais la difficulté croît avec le nombre de contraintes : il manque une courbe en budget d'attaque. La pièce ne dit pas si la sonde d'évaluation est celle contre laquelle l'attaquant a optimisé.
6. **L'expérience 4 confond mémoire et couplage.** La politique « découplée » décrite déclenche les comparaisons sur des pics instantanés de M_texte seul. Elle perd à la fois la mémoire temporelle et le passage d'information entre instruments. Le gain attribué au couplage peut être celui de la seule intégration.
7. **Zone 15–35 % de l'expérience 4.** « Arbitrage éditorial » est une issue qui ne falsifie rien : c'est une entorse à B4.
8. **V_coût dispose de la vérité terrain complète et de l'arbre de dérivation.** Tout pointage sur une trajectoire sabotée intercepte. La localisation (t*, sous-arbre) devient inerte, et la métrique R se réduit à un classement des trajectoires.
9. **FPR_étape ≈ 0,2 % pour FPR_traj = 5 % sur 25 étapes** suppose des scores indépendants entre étapes.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **CUSUM contre maximum.** Avec une fraction π d'étapes sabotées, un décalage μ et une autocorrélation φ des scores honnêtes, le gain existe si π est grand et μ/σ petit. Il s'annule si π·T ≈ 1 à 2. Sous un modèle autorégressif d'ordre 1, l'horizon effectif vaut T(1−φ)/(1+φ), soit environ 6 étapes pour T = 25 et φ = 0,6 (illustratif).
- **Biais honnête.** Si le biais directionnel honnête b_h est du même ordre que Δ_min/T, la séparation dépend de (b_a − b_h)·√T/σ et peut être nulle.
- **Variance inter-copies à K = 3.** Sous une mesure scalaire gaussienne (hypothèse de calcul), la variance empirique suit σ²·Exp(1).
  - Branche « explosion » : il faut un rapport de variances d'environ 7 pour atteindre 65 % de détection à 5 % de fausses alertes.
  - Branche « rigidité » : |Var − μ_hon|/σ_hon est borné par 1 du côté bas, alors que le seuil à 5 % est proche de 2. Cette branche est indétectable par le terme de variance. Toute détection y vient de λ·M_act.
- **Ratio ρ = Δ_adaptatif/Δ_initial.** L'estimateur de rapport est instable si Δ_initial est dispersé. La condition « taux de détection ≤ 10 % à 5 % de fausses alertes » est à 5 points du hasard. Avec 200 trajectoires, la borne supérieure d'un taux observé de 7 % dépasse 10 % : la condition n'est pas établissable.
- **Malédiction du vainqueur.** Sélectionner sur le jeu d'évaluation les points de contrôle qui satisfont la contrainte biaise ρ.
- **R et B_vérif = 1 par trajectoire.** La pièce ne donne pas la loi de P(interception | étape pointée). Sans elle, R n'est pas calculable.

### (c) Contrôles négatifs dont l'absence serait fatale

- Un adversaire construit avec un score de suspicion disjoint des moniteurs évalués.
- Un agent honnête à biais directionnel (emprunt à E).
- Un CUSUM sur étapes permutées dans le temps : si le gain est inchangé, « séquentiel » n'ajoute rien à « somme ».
- Les ablations λ = 0 et M_act seul dans l'expérience 2.
- Un plan 2 × 2 mémoire × couplage dans l'expérience 4.
- Une cascade dont le signal déclencheur est permuté entre trajectoires, à même nombre et même loi temporelle de déclenchements.
- Une sonde fraîche, entraînée sur une autre graine d'adversaire.
- Une courbe en budget d'attaque.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Le duel « mécanisme » est vrai par construction.** Le générateur place la dépendance dans la filiation des pièces. À fiabilité marginale égale, n appuis dérivés portent moins d'information que n appuis indépendants. La règle de regroupement est le calcul a posteriori correct pour ce générateur. Le duel vérifie qu'une règle est bien implémentée, pas un fait sur les agents.
2. **La dépendance testée n'est pas celle de la question.** Dans le cadre posé, la cause commune d'une reprise, d'un accord entre copies et d'un feu vert de moniteur est le partage de poids ou de contexte. Elle ne figure dans aucune « pièce observable ». Deux copies peuvent se tromper ensemble sur des pièces indépendantes. Le banc ne contient pas ce cas.
3. **L'adversaire n'est pas opérationnalisé.** Aucune procédure de sabotage n'est décrite pour les régimes 1 et 2. Rien ne mesure que les actes sont non suspects isolément. L mélange erreurs de compétence et dégradation.
4. **Le régime 3 n'est pas réellement tenu à l'écart.** Il reprend « des dossiers et sorties identiques » : une règle choisie sur les régimes 1 et 2 a vu ces sorties. La mise à l'écart de familles ne suffit pas si le blocage n'est pas croisé régime × famille.
5. **Un paramètre libre décide du résultat dans le régime 3.** La proportion q d'avis erronés partageant une ascendance avec l'erreur de l'agent fixe le gain : il est d'ordre q.
6. **Le moniteur d'activations n'est pas mis à l'épreuve.** Le régime 3 perturbe des avis, pas le modèle. D le reconnaît pour l'adaptativité, mais la conséquence est que le troisième article n'est pas couvert par le test de transfert.
7. **La révision après audit est faite par l'agent**, qui peut être l'adversaire. L après révision confond la qualité du ciblage et l'honnêteté de la révision.
8. **Positifs incluant les erreurs spontanées.** C'est cohérent avec L, mais les instruments ne sont alors jamais évalués sur la distinction entre sabotage et erreur.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Plafond du gain.** Soit g la fraction de conclusions dont tous les appuis sont dans un même groupe, e le taux d'erreur marginal d'une pièce, c la probabilité qu'un audit corrige. Le gain du regroupement sur la politique sans provenance est borné par g·e·c. Avec g = 0,3 et e = 0,1 (illustratif), le plafond est de 3 points, sous la marge de 5. H_A est alors inatteignable quel que soit l'agent. Avec g et e grands, elle est acquise. L'issue dépend des paramètres du générateur.
- **Quota d'audit.** Le gain est nul quand le quota tend vers 0. Il est nul aussi quand le quota couvre toutes les conclusions à risque. Il n'est pas monotone entre les deux ; un seul quota ne juge rien.
- **Marge de non-infériorité de 2 points.** L'erreur type de la différence appariée est d'ordre s_F/√F, avec F le nombre de familles (non donné) et s_F l'écart-type entre familles. Pour F = 30 et s_F = 8 points (illustratif), la demi-largeur à 95 % est proche de 3 points : indécidable.
- **Conjonction.** Six inégalités simultanées sur trois régimes : la probabilité d'établir H_A quand elle est vraie est le produit des puissances. L'issue « indécis » est structurellement favorisée.
- **Interaction de 3 points.** Une différence de différences a une variance environ quatre fois plus grande qu'un contraste simple, à effectif égal.
- **Classement « importance × risque ».** Si la variance de l'importance entre conclusions est faible, il se réduit au risque. Le terme d'importance n'est pas testé.

### (c) Contrôles négatifs dont l'absence serait fatale

- Un bras où la cause commune est dans les poids et non dans les pièces : accord erroné de copies sur des appuis indépendants. Si la règle n'y gagne rien, l'unification proposée couvre la dépendance de l'environnement, pas celle des trois articles.
- Un bras à corrélation intra-groupe nulle : le gain doit être nul et la perte inférieure à la marge.
- Un balayage de q, avec seuil rapporté.
- Un blocage croisé régime × famille.
- Une mesure de détectabilité par acte isolé. Le pré-test G0 de E, corrigé comme indiqué plus bas, pourrait servir ; je le signale comme emprunt.
- Une révision effectuée par une procédure fixe non contrôlée par l'agent.

La permutation des filiations à tailles de groupes conservées est un bon contrôle. Il faut y ajouter la conservation de la fiabilité marginale par pièce.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **« Non suspect isolément » est confondu avec « probable sous la loi honnête ».** Chaque choix +ε a la probabilité 0,5 chez l'honnête, mais environ 0,83 chez l'adversaire à 20/24. Le rapport de vraisemblance par acte est d'environ 1,67 : l'acte est informatif. La mention « VÉRIFIÉ par construction » ne couvre que le support, pas l'indiscernabilité.
2. **G0 est décidé par l'arithmétique du générateur.** Hypothèses de calcul : signe lisible, agrégation additive. Atteindre Δ = 0,30 avec ε = 0,04 demande environ 15,75 choix positifs sur 24, soit une aire sous la courbe ROC par acte d'environ 0,578 pour un classifieur lisant le signe. Le seuil est 0,58. Tout Δ supérieur échoue. G0 mesure ε et D, pas le modèle.
3. **Le Δ ≈ 0,64 suppose une agrégation additive**, non précisée. Sous une moyenne, le biais serait d'environ 0,027, sous le seuil de 0,30.
4. **Le banc est bimodal.**
   - Si le signe de chaque choix est calculable par le défenseur, un test de comptage des signes suffit. P(Bin(24 ; 0,5) ≥ 17) ≈ 0,032 et la puissance contre 20/24 est proche de 1. L'issue « sans intérêt n° 2 » est alors quasi acquise.
   - Sinon, M_text ne peut pas le lire non plus.
   - Le contrôle mécanique de signe n'est listé que comme base de M_text, pas comme base de la cascade.
5. **La qualification micro de B_verif est inatteignable avec les chiffres de E.** Avec m = 8 et un taux de fausses alertes d'au plus 2 %, le test binomial bilatéral exige 8 concordances sur 8 (P honnête ≈ 0,008 ; à 7 sur 8, environ 0,07). Contre 20/24, P(8/8) = C(20,8)/C(24,8) ≈ 0,17, loin de 0,85.
6. **T est confondu avec le regroupement.** D = 24 choix quel que soit T ∈ {4, 12, 24}. La « dilution en T » ne change pas le nombre d'actes, seulement le nombre de documents par étape et la longueur de contexte. La loi en √T invoquée ne s'applique pas à ce plan.
7. **La comparaison à historique réinitialisé est décidée par la variante.**
   - Sous W, la copie fraîche porte le même biais : la détection est faible par construction.
   - Sous P, elle n'a pas la consigne : la comparaison détecte la consigne.
   - L'auteur du « résumé neutre » n'est pas précisé.
   - Le max(TPR_act, TPR_comp) de H_1A masque cela et ajoute un biais de sélection.
8. **Le test métamorphique E ↦ −E ne détecte qu'un biais de signe fixe.** L'objectif de la variante W, |θ̂ − θ*| ≥ 0,30, ne fixe pas la direction. Un adversaire « amplificateur » (fonction impaire des preuves) satisfait exactement θ̂(−E) = −θ̂(E). La puissance du test est alors nulle. L'issue de E2 est déterminée par un choix d'objectif non rapporté. E ne mentionne que le cas « variance pure ».
9. **H_3A est une disjonction que la faiblesse de l'attaquant satisfait.** Un apprentissage par renforcement mal réglé donne r_Δ ≤ 0,5, donc « unification féconde ». De plus, l'attaquant n'est pénalisé que sur M_text et M_act. B_comp^méta n'est jamais visé et porte le triage. Un GET élevé est attendu par construction de l'objectif d'attaque.
10. **M_text est entraîné contradictoirement avec l'adversaire**, puis évalué sur ce même adversaire.
11. **La prédiction hors échantillon annoncée en (5)** (paramètres des articles 1 et 2 prédisant l'article 3) n'a ni modèle déposé ni duel. Le protocole préenregistré E4 de B est l'instrument qui manque ici ; je le signale comme emprunt possible, avec les réserves faites plus haut.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **GET.** Avec N = 400, 10 % de tâches adverses et b_verif = 5 % :
  - 40 tâches adverses et 20 vérifications ;
  - le numérateur est au plus 20 ;
  - le tirage uniforme capture environ 2 tâches en espérance.
  
  C'est un rapport de comptages de cet ordre : son intervalle de confiance couvre largement 2,0. Si la base mécanique est le comptage de signes, le dénominateur sature et GET ≤ 1 par plafond.
- **δ_E1.** C'est une différence de différences de taux bornés. Elle dépend de l'échelle (linéaire ou probit) dès qu'un terme approche 0 ou 1. Le maximum de deux taux estimés est biaisé vers le haut, d'autant plus que leurs variances diffèrent entre horizons.
- **Antisymétrie.** La statistique |θ̂(E) + θ̂(−E)| a pour loi nulle celle du biais propre du modèle de base (acquiescement, polarité). Si son espérance honnête est du même ordre que le biais adverse, le seuil à 5 % absorbe le signal.
- **H_2A.** Conjonction de quatre inégalités, dont AUROC < 0,60 et taux de détection naïf < 0,20. Établir des bornes supérieures exige des intervalles étroits. À N = 400 avec des dossiers groupés, c'est non garanti.
- **G0.** N₀ = 100 dossiers et des étapes corrélées au sein d'un dossier. Une borne supérieure d'aire sous la courbe ROC sous 0,58 n'est pas établissable si l'estimateur est proche de 0,578.

### (c) Contrôles négatifs dont l'absence serait fatale

- Un adversaire à direction impaire (amplificateur ou atténuateur) dans E2.
- Le comptage de signes au niveau de la trajectoire comme base mécanique de toute la cascade.
- Un contrôle positif de l'attaque : contournement d'une sonde monocouche (emprunt à C).
- Un attaquant également pénalisé sur B_comp.
- Un plan où le nombre de choix varie avec T, contre un plan où il est constant.
- Une sonde entraînée sur un adaptateur adverse et testée sur un adaptateur d'une autre graine. Le LoRA honnête de même rang, présent, est un bon contrôle mais ne couvre pas l'empreinte propre d'un adaptateur.
- Un moniteur de texte figé avant l'entraînement de l'attaquant, ou évalué sur un attaquant frais.

---

## Défaut commun aux quatre

Je le rapproche sans harmoniser, car chaque pièce y est exposée différemment. Le résultat central de chacune est en partie fixé par un choix de construction non rapporté comme paramètre :
- chez B, la courbure de μ et le mélange λ/r ;
- chez C, la forme de la contrainte de furtivité ;
- chez D, les paramètres g, e et q du générateur ;
- chez E, l'objectif directionnel et ε.

Une issue n'est interprétable que si ce paramètre est balayé et l'issue rapportée comme fonction de lui.

FIN-DE-CELLULE
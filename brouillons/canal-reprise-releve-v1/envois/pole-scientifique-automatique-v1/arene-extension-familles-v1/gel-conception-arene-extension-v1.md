# Gel de conception — extension de l'arène : familles qu'aucun moniteur seul ne couvre (Q3) et prix imposé à l'adversaire synthétique (Q3b) — v1

**Écrit AVANT tout calcul** : aucune ligne de code de l'extension n'existe encore, aucune graine n'a été tirée, aucun script n'a tourné. Les ordres de grandeur ci-dessous viennent de formules fermées évaluées à la main (valeurs de Φ arrondies), pas d'une exécution.

- Auteur : sous-agent neuf Opus 5.5 (lignée conv-audit), rédacteur de l'extension ; n'a écrit aucune pièce de l'arène v1 à v3 (brouillons, codes, contre-lectures).
- Date : 2026-10-31, 12:51 UTC (relevé `date -u`).
- Décisions qui fondent la tâche : R-739, R-740 (extension proposée après le calcul décisif), R-741 et R-743 (« go », « relance-le » ; contenu au niveau méthode, cadrage défensif, aucune recette), R-747 (plage de racines 20265001–20265999 pour l'extension).
- Cadre : **modèle mathématique synthétique** seulement (lois gaussiennes paramétriques sur des vecteurs synthétiques, moniteurs simples à taux de fausses alertes fixé). Aucun modèle réel, aucun texte, rien d'applicable à un vrai réseau ; l'objet est de **certifier la couverture d'une défense** et de **mesurer le prix qu'elle impose à l'adversaire synthétique**. Aucun transfert aux vrais modèles n'est revendiqué (revendication restreinte de P-041 v3).

## 1. Racines (R9) — gelées ici, avant tout emploi

| Racine | Usage prévu | Statut au gel |
|---|---|---|
| 20265001 / 20265002 | essais du code (pytest) ; la seconde sert à vérifier qu'une autre racine change le résultat | jamais employées |
| 20265011 | pilote d'essai Q3 (toutes familles, tous bras) et audit d'essai par attaquant indépendant (même racine, rôle à part) | jamais employée |
| 20265021 | pilote d'essai Q3b (générateur de configurations du canal « comportement ») | jamais employée |
| 20265031 | mesures de temps (une ou deux tâches pleine taille ; temps et compteurs seulement) | jamais employée |
| 20265041 / 20265042 | réservées (second pilote éventuel, déclaré d'avance) ; non employées sauf consignation | jamais employées |
| **20265901** | **décision Q3** (jamais employée hors préenregistrement scellé, GO, et après le calcul décisif du pilote principal) | réservée |
| **20265902** | **décision Q3b** (mêmes conditions) | réservée |

**Racines refusées par garde** (relevées dans les brouillons 1 à 3, les LISEZMOI v1 à v3, les journaux, les trois contre-lectures et les essais de l'arène, et dans R-747) : 20261201 et 20261202 (décision de l'arène principale, RACINE et RACINE_TENUE) ; 20261291 à 20261298 ; 20262291 ; 20261301 ; 20261101 (racine factice des essais) ; 20261311 à 20261316 ; 20269501, 20269502 ; 20269731, 20269732 ; 20269741, 20269742 ; toute la plage 20264001–20264999 (pilote b4 en parallèle). De plus, hors décision, **toute racine hors de 20265001–20265999 est refusée**, et les deux racines de décision de l'extension sont refusées sans autorisation.

## 2. Constat de conception, avant code : fermeture par union

Pour des moniteurs dont la région « non détectée » est convexe (linéaire, maxout à maximum dur), l'union de deux moniteurs recalibrée au taux α est encore un maxout : l'union d'un maxout à k₁ unités et d'un maxout à k₂ unités est un maxout à k₁ + k₂ unités (avec le log-somme-exp, approximativement, l'écart tendant vers zéro avec l'échelle). **Conséquence** : si une union de deux moniteurs de la classe déployée par requête (maxout à 9 unités) couvre une famille, un maxout seul à 18 unités la couvre, donc a fortiori un maxout seul de 73 unités (même total de paramètres que B′). Le régime demandé — « aucun moniteur seul de la classe maxout à k unités, k au total de B′, ne couvre ; une union de deux couvre » — est **vide** pour des moniteurs à champ récepteur complet. Il n'existe que si la classe n'est pas fermée par l'union nécessaire :
- **classe linéaire** (une seule unité) : non fermée ; une famille à deux modes opposés n'est couvrable par aucun moniteur linéaire, et l'est par l'union de deux ;
- **classe « une vue »** (le moniteur, linéaire ou maxout de n'importe quelle taille, lit un seul bloc de coordonnées) : non fermée ; une famille dont les deux modes déplacent deux blocs différents n'est couvrable par **aucun** moniteur d'une vue, quelle que soit sa taille (73 unités comprises), et l'est par l'union de deux moniteurs, un par vue.

L'extension retient donc deux régimes, chacun avec un témoin couvrable de même taille.

## 3. Conception gelée

### 3.1 Monde

- Espace des activations synthétiques R⁶ ; loi propre N(0, I₆) ; α = 0,01 ; z = Φ⁻¹(1 − α) ≈ 2,326.
- Lois d'attaque : N(μ, I₆), moyenne seule (simplification déclarée par rapport à l'arène v3, où l'attaquant déplaçait aussi les écarts-types de trois composantes ; elle rend exacts les calculs de référence).
- **Famille** = réunion de J = 2 boules de comportement : le mode j a un centre c_j (une manière de réaliser le comportement visé) ; l'attaquant choisit μ avec ‖μ − c_j‖ ≤ δ (distance de Wasserstein d'ordre 2 entre N(μ, I) et N(c_j, I)), en ne modifiant que les coordonnées libres du mode (toutes en champ complet ; celles de la vue du mode en régime « vues »).
- Générateur de familles, par instance (graines `SeedSequence(entropy=racine, spawn_key=(…, instance, …))`) : rayons R₁, R₂ ~ U[4,25 ; 4,75] indépendants ; directions uniformes ; angle γ ~ U[20° ; 45°] pour les témoins couvrables. Les quatre familles d'une instance partagent R₁, R₂ (appariement).
  - **N2** (champ complet, non couvrable par un linéaire) : c₁ = R₁u, c₂ = −R₂u.
  - **C2** (champ complet, témoin couvrable) : c₁ = R₁u₁, c₂ = R₂u₂, angle γ entre u₁ et u₂.
  - **NV** (deux vues de 3 coordonnées, non couvrable par tout moniteur d'une vue) : c₁ = (R₁u₁, 0), c₂ = (0, R₂u₂) ; le mode j ne modifie que la vue j.
  - **CV** (vues, témoin couvrable) : les deux modes dans la vue 1, angle γ ; ils ne modifient que la vue 1.
- Budgets δ ∈ {1,0 ; 1,4} ; T = 8 tours ; seuil de couverture θ* = 0,5 (recommandé ; « la famille est couverte par un moniteur » si sa détection au pire cas sur la famille est ≥ θ*).

### 3.2 Couche exacte (référence, par famille et par δ ; formules fermées et recherches à une dimension, vérifiées)

Notations : r_j = R_j − δ ; a_j = Φ(r_j − z) ; b_j = Φ(−r_j − z).
- **N2, classe linéaire** : V_pur = Φ(−δ − z) (pour tout w unitaire, le minimum sur la famille de w·μ vaut au plus −δ, atteint pour w ⊥ u) ; V_mél = valeur du jeu 2 × 2 [[a₁, b₂], [b₁, a₂]] (défenseur sur ±u, meilleure réponse continue de l'attaquant au point le plus proche de l'origine), selle vérifiée par deux recherches à une dimension ; V_union = union de +u et −u au taux total α, partage du taux optimisé.
- **NV, toute classe « une vue »** : V_pur = α exactement (la loi marginale de la vue non déplacée est la loi propre) ; V_mél = (a₁a₂ − α²)/(a₁ + a₂ − 2α) (dans une vue, le meilleur détecteur de n'importe quelle capacité contre un seul mode est linéaire, lemme de Neyman–Pearson) ; V_union = union d'un moniteur par vue, vues indépendantes, partage optimisé.
- **C2 et CV, classe linéaire** : V_pur = Φ(ρ* − δ − z), ρ* = distance de l'origine au segment [c₁, c₂] ; selle pure vérifiée (stratégie mixte de l'attaquant aux poids du point projeté) ⇒ V_mél = V_pur, **valeur du tirage exactement nulle**.
- Garde de régime : les familles non couvrables doivent avoir V_pur < θ* et V_union ≥ θ* ; les témoins V_pur ≥ θ*.

### 3.3 Bras mesurés (machinerie de l'arène v3, recopiée et adaptée)

- Régime champ complet (N2, C2) : **A** (défense unique linéaire réentraînée sur le mélange uniforme des attaques passées) ; **B** (double oracle, oracle linéaire « détection ») ; **B′** (double oracle, oracle maxout à 9 unités) ; **D** (maxout unique à t + 1 unités réentraîné) ; témoins de finale **PUR_B**, **PUR_B′** (moniteur de poids maximal déployé seul) et **U_B**, **U_B′** (« ou » déterministe des moniteurs du support, recalibré à α).
- Régime vues (NV, CV), toutes classes « une vue » : **A_V** (linéaire d'une vue réentraîné), **B′_V** (double oracle, maxout à 9 unités d'une vue ; l'oracle entraîne un moniteur par vue et garde le meilleur), **D_V** (maxout d'une vue à t + 1 unités) ; témoins **PUR_B′V**, **U_B′V** (l'union lit deux vues si le support en couvre deux).
- Tour 0 : moniteur entraîné contre le mélange uniforme des deux lois de centre ; colonnes initiales du jeu restreint : les deux lois de centre.
- Finale : défense figée ; meilleure réponse standard et renforcée (plusieurs départs par mode, échantillons de Monte-Carlo fixés) ; V = la plus basse des deux détections, sur échantillons frais. Les témoins PUR et U emploient les graines de leur bras source (nombres aléatoires communs : si le mélange est pur, PUR = mélange au bit près).

### 3.4 Grandeurs mesurées

Valeur du tirage VT = V(mélange) − V(PUR) ; union contre mélange UM = V(U) − V(mélange) ; écarts d'étalonnage CAL = V mesuré − V exact (B contre V_mél linéaire ; B′_V contre V_mél vues ; U contre V_union) ; poids (part pure, support, poids maximal) ; pour A : I1 (progrès), I2 (baisse de détection des attaques passées, oubli ou saturation), **I3 (retours) avec sa valeur nulle 0,7345** (moyenne de (t − 2)/(t − 1) pour t = 3 … 8, cosinus entre moyennes d'attaque), **I4 (changements de mode) avec sa valeur nulle 0,5**, et V(A) − V_pur exact ; contrastes appariés « non couvrable − témoin ».

### 3.5 Q3b — canal « comportement » et nombre de vues surveillées (calcul analytique)

- Signature du comportement visé : décalage R_a u_v dans chacune des vues surveillées v = 1 … L (L = 1 … 8). L'adversaire déplace chaque vue de x_v le long de −u_v pour sortir de la région détectée.
- Canal « comportement » : b ~ N(0, 1) en régime honnête ; sous l'adversaire, b ~ N(β₀ + κ‖x‖, 1) (la loi du comportement se déplace avec le déplacement imposé aux activations).
- Dommage D(x) = exp(−‖x‖²/(2 s_D²)) (décroît avec le déplacement ; analogue synthétique du compromis observé par Bailey et collègues, arXiv 2412.09565v2, p. 3 et p. 23, lu par la session du 31 octobre (R-744) ; aucun chiffre repris).
- Gain de l'adversaire G = D × P(non-détection), maximisé sur x (log-concave, symétrique en v : un seul paramètre).
- Trois défenses au taux total α : activations seules (union des L moniteurs linéaires, seuils égaux) ; comportement seul (seuil à α) ; **lecture jointe** (union des deux canaux, partage du taux α choisi par le défenseur pour minimiser le gain maximal). Les deux défenses à un canal sont des cas particuliers du partage : G*_joint ≤ min(G*_act, G*_comp) par construction ; **la question est l'écart strict** (dilemme) et son évolution avec L.
- Générateur de configurations (racine 20265021 pour l'essai) : R_a ~ U[2,5 ; 3,5], s_D ~ U[2 ; 4], κ ~ U[0 ; 1,5], β₀ ~ U[0 ; 1].

## 4. Prédictions signées, écrites avant tout calcul

Seuils recommandés pour la lecture (à geler par Lazar) : marge m = 0,02 (deux fois α, principe de l'arène) ; tolérance d'étalonnage τ = 0,03 ; marge du dilemme m_b = 0,02. Valeurs « exactes » : moyennes attendues pour R ≈ 4,5.

### 4.1 Couche exacte (formules)

| Grandeur | δ = 1,0 | δ = 1,4 | Signe |
|---|---|---|---|
| N2 : V_pur linéaire | 0,0004 | 0,0001 | — |
| N2 : V_mél linéaire | ≈ 0,44 (0,41 à 0,46) | ≈ 0,39 (0,35 à 0,42) | — |
| N2 : V_union | ≈ 0,82 (0,75 à 0,88) | ≈ 0,70 (0,61 à 0,78) | — |
| N2 : VT exact | ≈ +0,44 | ≈ +0,39 | + |
| N2 : union − mélange exact | ≈ +0,38 | ≈ +0,31 | + |
| NV : V_pur (toute capacité) | 0,0100 | 0,0100 | — |
| NV : V_mél | ≈ 0,445 | ≈ 0,395 | — |
| NV : V_union | ≈ 0,82 | ≈ 0,70 | — |
| C2, CV : V_pur | ≈ 0,84 (0,73 à 0,91) | ≈ 0,72 (0,58 à 0,83) | — |
| C2, CV : VT exact | 0 (selle pure certifiée dans 100 % des instances) | 0 | = 0 |

### 4.2 Machinerie (pilote, puis décision) — branche prédite (confiance) ; branche opposée = audit

| # | Grandeur | Prédit | Confiance | Branche opposée et ce qu'elle voudrait dire |
|---|---|---|---|---|
| E1 | VT_B sur N2 | > m, entre +0,36 et +0,45, aux deux δ | 0,9 | VT ≤ m : la machinerie ne sait pas montrer un tirage utile là où il existe exactement ; la pureté de B′ en v3 deviendrait suspecte (artefact d'instrument) |
| E2 | VT_B′V sur NV | > m, entre +0,35 et +0,44 | 0,9 | idem pour le maxout d'une vue (la classe de B′) |
| E3 | Poids de B (N2) et de B′_V (NV) | part pure = 0, support ≥ 2 | 0,9 | part pure > 0 : l'instrument fabrique de la pureté |
| E4 | CAL_B (N2), CAL_B′V (NV) | moyenne dans [−0,03 ; +0,005] | 0,7 | hors bande : instrument biaisé (bas : oracle ou attaquant ; haut : attaquant trop faible) |
| E5 | UM_B (N2), UM_B′V (NV) | > 0, entre +0,20 et +0,38 | 0,85 | UM ≤ 0 : contredit la queue gaussienne (le coût de partage de α serait supérieur au gain) → erreur de seuil ou de code |
| E6 | CAL_U (N2, NV) | moyenne dans [−0,08 ; +0,005] | 0,6 | hors bande |
| E7 | VT_B (C2), VT_B′V (CV) | « ≈ 0 » : dans ]−m ; +m[ | 0,7 | VT > m : l'instrument fabrique du tirage là où il est exactement nul |
| E8 | Part pure de B (C2), B′_V (CV) | entre 0,3 et 0,9 (non ferme) | 0,5 | — (descriptif) |
| E9 | UM sur C2, CV | entre −0,03 et +0,01 | 0,6 | — |
| E10 | B′ sur N2 (maxout champ complet) | VT_B′ ≈ 0 (« ≈ »), part pure ≥ 0,5 ; V(B′) et V(D) entre V_union − 0,08 et V_union | 0,6 | VT_B′ > m : le maxout à 9 unités ne trouverait pas l'union à deux unités |
| E11 | A sur N2 et A_V sur NV | V(A) ≤ 0,012 ; I1 dans [−0,02 ; +0,02] ; I3 ≥ 0,85 ; I4 ≥ 0,8 (cycle) | 0,8 | V(A) au-dessus de V_pur exact + m : impossible par le certificat → erreur |
| E12 | A sur C2, CV | V(A) entre V_pur − 0,08 et V_pur ; **I3 ≥ 0,735 aussi** (alternance de modes couverte) ; I4 ≥ 0,6 | 0,6 | I3 sous la valeur nulle |
| E13 | D_V sur NV | V ≤ 0,012 (aucun moniteur d'une vue ne couvre, même riche) | 0,85 | V > 0,02 : contredit le certificat → erreur |
| E14 | Contraste VT(non couvrable) − VT(témoin), apparié | entre +0,35 et +0,45 aux deux δ, pour B (N2 − C2) et B′_V (NV − CV) | 0,85 | ≤ m |

Lecture anticipée (pas un résultat) : la valeur du tirage est grande exactement là où la classe déployée ne peut pas exprimer l'union que la famille exige, nulle ailleurs ; l'union, quand elle est permise, fait mieux que le tirage (queues gaussiennes) ; I3 au-dessus de sa valeur nulle ne distingue pas un cycle (N2, NV) d'une alternance couverte (C2, CV) — c'est le niveau de V(A) qui les distingue. Si la machinerie reproduit la couche exacte, la pureté de B′ en v3 s'explique par la couvrabilité des familles v3 par un maxout à 9 unités, pas par l'instrument ; sinon, audit de l'instrument v3.

### 4.3 Q3b — prédictions

| # | Grandeur | Prédit | Confiance | Branche opposée |
|---|---|---|---|---|
| P1 | G*_act(L) | strictement décroissant en L = 1 … 8 pour toutes les configurations ; rapport G*_act(8)/G*_act(1) de médiane entre 0,15 et 0,5 | 0,9 (décroissance) ; 0,6 (médiane) | une configuration non décroissante : à examiner (partage du taux entre vues plus coûteux que le déplacement) |
| P2 | G*_comp | = Φ(z − β₀), entre 0,91 et 0,99, indépendant de L | identité | — |
| P3 | G*_joint ≤ min(G*_act, G*_comp) | toujours | identité (vérifiée par essai) | violation : erreur de code |
| P4 | Part des configurations avec dilemme strict Δ(L) = min(G*_act, G*_comp) − G*_joint(L) > m_b, à L = 4 | entre 0,5 et 0,9 | 0,6 | < 0,5 : la lecture jointe n'ajoute presque rien dans ce modèle (le partage du taux coûte autant que le canal ajouté) |
| P5 | Cette part, de L = 1 à L = 8 | croissante | 0,6 | décroissante |
| P6 | Rapport G*_joint/G*_act pour κ ≥ 0,5 | décroissant en L | 0,7 | croissant |
| P7 | Configurations κ < 0,2 et β₀ < 0,2 | Δ < m_b | 0,7 | Δ ≥ m_b |

## 5. Ordre des opérations déclaré

1. Ce gel (aucun code). 2. Code `arene_extension_v1.py` (recopie et adaptation de `arene_melange_v3.py`, jamais modifié). 3. Essais (racines 20265001 / 20265002). 4. Mesure de temps (20265031). 5. Pilote d'essai Q3 (20265011) ; audit d'essai par attaquant indépendant (même racine, rôle à part). 6. Pilote d'essai Q3b (20265021). 7. Brouillon 1 du préenregistrement, LISEZMOI, journal. Toute correction de code après le début du pilote est consignée au journal avec sa raison ; aucune ne change la conception ni les prédictions ci-dessus.

# Proposition A · Tour III.2 · critique croisée de méthode

**Réception.** Les pièces B, C, D, E et F sont présentes, chacune close par sa ligne de fin, sans coupure visible. Je n'ai pas recalculé les empreintes. Le bloc FAITS ne contient que la question : aucun fait à statut n'est transmis. Ma conception du tour III.1 ne m'est pas retransmise ; je ne m'y réfère pas.

**Statut de ce qui suit.** HYPOTHÈSES de méthode et dérivations (signalées « dérivation »), aucun résultat empirique. Les chiffres repris des pièces restent « illustratifs ».

**Notations.** p_c est la masse d'une classe sous la loi de référence, N la taille d'un échantillon, π(r) la prévalence des idées vraies à rareté r, α et 1−β le taux de faux positifs et la sensibilité du contrôle.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Rareté sous G₀, production sous I.** Y compte les classes rares sous G₀. Pour I1 et I2, qui changent de modèle, les modes propres du nouveau générateur sont rares sous G₀ : une partie du gain est acquise par construction, sans accès à une queue. Ce gain dépend du budget, car les premiers appels récoltent les modes nouveaux puis la courbe sature. Un rapport Y_I/Y_B₀ à un seul budget ne tranche donc rien.
2. **Leurres de E1.** Le FPR est identifié sous la loi des leurres (perturbations minimales de vraies rares), pas sous la loi des fausses que le générateur émet réellement dans la strate. « Même strate » est une étiquette assignée : la classe du leurre n'a jamais été tirée, sa rareté n'est pas mesurée.
3. **Mondes plantés.** Placer des vérités « de faible probabilité sous G₀ » suppose d'avoir consulté G₀ pour construire le terrain. C'est une fuite entre l'instrument et son banc. La prévalence π y est choisie par le concepteur, donc FDR_I − FDR_B₀ est fonction de ce choix. Sur le terrain réel à contrôle exact, le FDR est nul par construction. La clause FDR de H_A n'est ainsi éprouvée que là où π est artificiel.
4. **I5.** Un taux de réplication plus bas sur O′ confond l'effet Goodhart avec une simple baisse de π dans le bras bouclé. Sur mondes plantés, la quantité propre est P(O=1 | faux) par bras, puis P(O′=1 | O=1, faux).
5. **Bootstrap sur f₁.** Une classe vue k fois dans l'échantillon réapparaît exactement une fois dans un rééchantillon avec probabilité ≈ k·e^(−k) (dérivation). L'espérance bootstrap de f₁ n'est donc pas f₁, et l'intervalle proposé pour Û est décentré.
6. **Canoniseur.** Les paires sont « tirées des sorties réelles de G₀ », mais l'étiqueteur n'est pas nommé. Si c'est C, la validation est circulaire. Si c'est une évaluation exhaustive, elle n'existe que sur domaine fini.

### (b) Conditions de perte de puissance

- **Û = f₁/N.** Soit q = P(C fusionne | non équivalentes) et u = P(C sépare | équivalentes), mesurés sous la loi des paires G₀×G₀. Û est biaisé vers H_A quand q > 0 et vers H_B quand u > 0. Le duel E0 n'est pas jugeable tant que le biais induit n'est pas borné sous ε.
- **Validité des p-valeurs pour I6.** Benjamini–Hochberg emploie des seuils jusqu'à α/m. Vérifier P(p ≤ t | faux, strate) ≤ t à t = α/m exige de l'ordre de 1/t tirages nuls dans la strate (dérivation). Les ~10³ leurres par strate (illustratif, valeur de B) ne suffisent plus dès que m est grand.
- **E2.** La demi-largeur sur le FDR varie comme √(FDR(1−FDR)/n_conf), où n_conf est le nombre de classes rares confirmées. Si E[n_conf] est petit, le critère δ n'est pas jugeable. Si E[Y_B₀] est proche de 0, l'intervalle du rapport est non borné.
- **Recouvrement Σ min(p_i, p_j) de I2.** L'estimateur par substitution est biaisé vers le bas par la masse non vue. Le rapport inter/intra n'est interprétable qu'à N égaux et à taux de sorties valides égaux entre familles.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Essai A/A.** B₀ contre B₀ à graines distinctes, sur toute la chaîne E2, pour obtenir la loi nulle du rapport et de l'écart de FDR. Le placebo d'invite ne le remplace pas.
- **Échange des rôles.** Compter aussi les classes rares sous I produites par G₀. Un gain symétrique signale une différence de modes, pas un accès à la queue.
- **Fausses naturelles.** Mesurer le FPR sur des fausses émises par le générateur dans la strate, étiquetées par la vérité plantée, à côté des leurres.
- **Générateur uniforme de E0.** Sous canonisation comportementale, des programmes aléatoires s'effondrent sur quelques comportements dégénérés (constantes, erreurs). Ce contrôle peut tomber en H_A sans défaut du canoniseur. Il faut le doubler d'un générateur à loi connue sur l'espace des classes, pas sur celui des syntaxes.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Statuts.** C appose [VÉRIFIÉ] sur des références citées de mémoire (Good, Rice) et [OBSERVÉ-NON-AUDITÉ] sur des constats que personne n'a transmis. Aucun fait du bloc FAITS ne porte ces statuts. Une identité mathématique est une dérivation et une citation reste RAPPORTÉE. L'impossibilité d'ordonner deux singletons est attribuée à Good (1953) : attribution à vérifier, je ne la reconnais pas comme résultat de cet article.
2. **Instrument de rareté différent selon le bras (E1).** p̂(s) ≤ 0,01 est calculé sur l'échantillon du bras. Avec les valeurs illustratives de C, le témoin tire environ B/(C_gen + C_verif) ≈ 476 candidats (dérivation), le bras I1 beaucoup plus. Le même seuil y sélectionne des comptes différents. Y_rare compare deux grandeurs définies par deux estimateurs, et il manque un échantillon de référence commun et disjoint.
3. **φ comme version réduite de V.** φ porte sur 100 sondes et V sur 1 000 cas (illustratifs). Si les deux viennent de la même loi d'instances, prioriser les signatures rares revient à prioriser les comportements inhabituels sur les sondes. L'hypothèse d'homogénéité (V constant dans la classe) n'est pas mesurée.
4. **Quantificateur ∃.** La définition de Y retient une classe dès qu'un de ses membres passe V. La probabilité de faux positif d'une classe croît alors avec le nombre de membres testés.
5. **Témoin faible.** L'échantillonnage direct sans déduplication est battu par toute déduplication. Le duel n'isole ni la déduplication seule, ni la priorité aux rares.
6. **Zones mortes.** Entre 1× et 1,5× (E1), entre 0,05 et 0,50 de couverture (E0), entre 0,2× et 0,5× (E3), aucune hypothèse n'est falsifiée. Dans E3, si le FDR à seuil fixe ne dérive pas, ni H_A ni H_B ne s'applique. La règle B4 n'est pas tenue.
7. **E2.** Le balayage de température n'a pas de règle de choix. Prendre la meilleure température a posteriori avantage le bras thermique, et moyenner le pénalise. La rareté sous générateur contraint n'est pas rattachée à une loi de référence.
8. **I3 sur ce banc.** Sur une batterie de cas secrets, « k tests orthogonaux » équivaut à une batterie plus longue. Les erreurs y sont d'échantillonnage, bien conditionnées. Rien n'est appris sur les erreurs structurelles, que C désigne pourtant comme le risque principal.
9. **Formule de la NCD.** Si la longueur compressée de l'archive domine celle de x, alors NCD(x, A) = (C(xA) − C(x))/C(A) tend vers 1 quel que soit x (dérivation). La mesure est constante par construction.

### (b) Conditions de perte de puissance

- **M₁₀%.** Cette masse dépend de N : sous une loi où toute classe est vue une fois, elle vaut 0,10 mécaniquement. Un seuil fixe n'est pas invariant en N.
- **Contrôle inversé de E3.** Il ne dégrade le FDR que si π(r) décroît avec la rareté. Si π(r) est plat ou croissant, il ne discrimine rien. Or π(r) n'est jamais estimé directement.
- **Cible FPR_queue.** Elle dépend de π̂_queue, qui n'est identifiable qu'avec V*. Hors banc, le critère est circulaire.
- **I1.** Le gain est nul si P(deux tirages indépendants tombent dans la même classe) est proche de 0, ou si le coût de φ approche celui de V.

### (c) Contrôles négatifs dont l'absence serait fatale

- Référence de rareté commune aux bras, et essai A/A.
- Bras « préfiltre par accord de φ avec les sorties connues, sans critère de rareté », pour séparer la prévérification de la recherche de rareté.
- Estimation de π(r) par strate avec V*, avant tout duel.
- Descripteurs de la grille gelés avant toute lecture des sorties.

Le contrôle φ_rand par hachage et la grille de descripteurs hors domaine sont de bons contrôles ; je les reprends.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Question évacuée par le terrain.** Avec un vecteur exhaustif sur instances finies et un évaluateur exhaustif, F est nul par construction, et D le dit. La clause « sans augmenter les fausses découvertes » devient vraie par définition. Rien ne se transfère à un contrôle imparfait, qui est le cas posé par la question.
2. **Certification différentielle.** Y exige que la rareté soit certifiée. La probabilité de certifier une classe de masse p avec n appels témoins est P(Bin(n, p) ≤ k*), soit (1−p)^n si k* = 0 (dérivation). ΔY mêle donc deux effets : trouver plus de classes rares utiles, et trouver des classes plus certifiables parce que plus rares encore. Le seuil effectif est de l'ordre de 1/n, pas τ.
3. **Interférence entre bras.** La couverture simultanée porte sur toutes les classes testées, tous bras confondus. Le Y d'un bras dépend alors du nombre de candidats des autres bras, et la règle d'imputation du coût du panel partagé n'est pas fixée.
4. **Non-infériorité à marge nulle.** H_A exige ΔF ≤ 0. Si ΔF = 0 exactement et que F n'est pas dégénéré, une région de confiance tombe entièrement dans H_A avec une probabilité au plus égale au risque nominal, quelle que soit la taille (dérivation). L'issue « à cheval » est alors l'issue générique.
5. **Étalonnage tautologique.** Tester la borne binomiale sur un échantillonneur à table connue vérifie un théorème. Les hypothèses fragiles (indépendance et stationnarité des appels réels) ne sont pas éprouvées, ce que D concède sans y remédier.
6. **Couverture.** Deux interventions seulement, toutes deux d'allocation. Aucune ne déplace la loi de proposition.

### (b) Conditions de perte de puissance

- **Rareté.** Le critère n'est pas jugeable si n < ln(M/δ)/τ, où M est le nombre de classes à certifier simultanément (dérivation, correction de Bonferroni). La condition d'arrêt de D ne tient pas compte de M.
- **Déduplication.** Elle est sans puissance si le coût du vecteur approche celui du contrôle (D le note) ou si la probabilité de collision est faible.
- **Réallocation.** La formule 1 − ∏(1 − p_mc)^(n_m) ne guide rien quand les p_mc utiles sont inférieurs à 1/n_pilote : le pilote ne les distingue pas de 0.
- **Dérive.** Le panel est tiré après le gel des candidats. Toute différence entre la loi témoin à cette date et celle des campagnes biaise p_c.

### (c) Contrôles négatifs dont l'absence serait fatale

- Test d'homogénéité entre deux moitiés du panel témoin, et entre panel et campagne témoin, sur les fréquences des classes dominantes.
- Campagnes A/A.
- Y recalculé avec une rareté certifiée par une moitié de panel indépendante par bras, pour mesurer l'interférence.
- Terrain apparié où le contrôle est volontairement tronqué et l'audit exhaustif, sans quoi F reste hors d'atteinte.

Le contrôle par alias du même modèle est le meilleur contrôle proposé pour la pluralité ; je le reprends.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Statuts.** « VÉRIFIÉ comme donnée de l'énoncé » et VÉRIFIÉ sur des théorèmes cités de mémoire : même remarque que pour C(a)1.
2. **Good–Turing comme rareté individuelle.** p_GT(c) ne dépend que du compte r. Tous les singletons reçoivent la même valeur, donc la « surprenance » n'ordonne rien dans la queue. Avec N = 10 000 et le seuil 0,01 (illustratifs), toute classe de compte inférieur à environ 100 est « rare ». Une classe produite par une intervention et absente de l'échantillon nominal est rare par construction.
3. **Jaccard sur classes rares.** Pour deux échantillons indépendants de la même loi, une classe de masse p avec Np ≪ 1 est vue dans les deux avec probabilité ≈ (Np)² et dans au moins un avec ≈ 2Np. Le rapport tend vers 0 (dérivation). Le critère « Jaccard < 0,30 » de M-C est satisfait par deux copies du même modèle.
4. **V* et V_orth partagent un principe de construction.** V mesure sur instances standards, V_orth sur distributions décalées, V* sur instances hors distribution. Une « fausse découverte » confond alors erreur du contrôle et échec de généralisation. Le bénéfice de V_orth peut venir de sa parenté de conception avec V*.
5. **Interventions composites.** M-A réunit déduplication et seuillage BH, M-B décodage tabou et second contrôle, M-C modèles de base, multi-familles, isolation et tests d'invariance. Aucun duel n'attribue l'effet à un composant.
6. **Décisions sans intervalle.** « Abandon si gain < +20 % » sur 5 graines : pour un gain vrai de 20 %, la décision est proche du tirage au sort. « FDR non accru » est accepté faute de rejet au test de Fisher. C'est une absence de preuve lue comme preuve d'absence.
7. **Contrôle négatif d'Exp-Diag.** P(V=1) sur générateur aléatoire vaut α(1−π_alé) + (1−β)π_alé. Il n'identifie α que si π_alé est connu. Le taux d'acceptation seul ne « démontre » rien.
8. **Calibration conforme.** L'échangeabilité entre leurres d'étalonnage et candidats de queue est précisément ce qui est en doute. Le contrôle proposé ne la teste pas.
9. **ΔMDL.** L(c) est la plus courte description observée dans la classe. L'espérance d'un minimum décroît avec le nombre de membres : les classes rares sont pénalisées mécaniquement, biais corrélé à la variable d'intérêt.

### (b) Conditions de perte de puissance

- **M̂₀ et taux de collision.** Ils sont liés (S₁ ≤ nombre de classes observées). Le triplet d'Exp-Diag n'a pas trois degrés de liberté.
- **Borne α_V·α_orth.** Elle exige P(V_orth=1 | V=1, faux) = α_orth sous la loi des fausses sélectionnées par la recherche taboue, pas sous celle des leurres chirurgicaux.
- **FDR_rare sur singletons.** Le nombre de singletons confirmés fixe la largeur de l'intervalle. En dessous, le seuil 0,10 n'est pas jugeable.
- **M-A.** Sans puissance si le taux de collision ρ est proche de 0, ou si le taux de fusion de vraies distinctes par φ à 64 sondes dépasse le gain. E prévoit ce critère (iv), mais il requiert V* sur des paires, à un coût non budgété.

### (c) Contrôles négatifs dont l'absence serait fatale

- Jaccard intra-modèle à graines distinctes et à N égal comme plancher. Le duel inter/intra de B est l'instrument correct ; je m'en sers ici.
- Plan factoriel ou ablation composant par composant.
- V* de même loi d'instances que V, pour séparer erreur de contrôle et décalage de distribution.
- Essai A/A donnant la variance entre graines avant tout seuil en pourcentage.

Le contrôle par hachage SHA-256 de M-A est pertinent.

---

## Sur la proposition F

### (a) Défauts de méthode

1. **FDR_audit vrai par construction.** Φ_audit est à la fois la porte d'acceptation (verrou e-values) et la référence de valeur (V_audit ≥ v₀ dans D_rare). Hors domaines plantés, la clause « FDR_audit ≤ 0,05 » de E1 à E4 restitue le niveau nominal de la procédure. Elle ne mesure pas une erreur. Seul l'instrument 4, avec ses instances nulles, fournit une vérité indépendante, et les duels ne l'utilisent pas explicitement.
2. **Test inatteignable.** Un test de permutation apparié sur 5 graines a 2⁵ = 32 configurations. Sa plus petite p-valeur unilatérale est 1/32 (dérivation), au-dessus du seuil 0,01 exigé. Tel qu'écrit, H_A1 ne peut jamais être établie, sauf mise en commun des domaines, non spécifiée.
3. **« Meilleur modèle unique ».** La règle de sélection de I₀ est absente. Choisi sur les mêmes domaines, I₀ bénéficie d'un biais de sélection ; choisi ailleurs, il peut être un faux « meilleur ».
4. **Rareté sous P₀ avec changement de modèles (I1).** Même gain par construction que pour B(a)1. Le contrôle par clones du meilleur modèle le corrige en partie.
5. **E0.** L'existence d'idées valides prouvée par oracle n'établit pas leur masse dans ]0, τ]. Rien ne distingue p = 0 (hors support) de p ≤ −ln δ/N₀. Zone morte entre 0,30 et 0,85.
6. **Contrôle composite de E4.** Remplacer à la fois les filtres et le bandit interdit l'attribution.
7. **Faux négatifs des filtres.** Le « jeu étalonné d'idées rares valides » n'a pas d'origine. S'il est tiré de ce qui a franchi la cascade, le taux de faux négatifs est nul par survie.
8. **Valeur.** La « longueur du programme minimal dans sa classe » a le même biais que chez E(a)9. Le gain de portefeuille dépend de l'ensemble des classes fréquentes trouvées par le bras : la valeur d'une même classe varie selon le bras et le budget.
9. **Références.** L'attribution est plausible, mais l'usage est à vérifier pour deux d'entre elles. Padmakumar et He (2024) porte, à ma connaissance (RAPPORTÉ, certitude moyenne), sur des textes coécrits par des humains, pas sur la diversité propre des modèles de base. Shumailov et al. (2024) traite d'entraînement récursif, pas de convergence entre familles : l'indice « contre » est analogique. La loi en √(k/m) de la limite 5 est donnée sans dérivation.

### (b) Conditions de perte de puissance

- **e-values.** La garantie tient si E[e | nulle] ≤ 1 sous la loi des instances d'audit. Elle porte sur l'hypothèse nulle « échoue sous cette loi », pas « faux dans le monde ». Si la loi d'audit s'écarte de la loi cible, le FDR contrôlé n'est pas celui demandé. La puissance s'effondre quand le nombre d'instances d'audit par candidat est faible devant l'écart à v₀.
- **Borne Clopper–Pearson à k = 0.** Avec les valeurs illustratives de F (N₀ = 10⁴, τ = 10⁻³), elle passe pour une classe isolée. Sous couverture simultanée de M classes, il faut N₀ ≥ ln(M/δ)/τ (dérivation), ce que F ne prévoit pas.
- **Bandit UCB.** Les récompenses « classe rare nouvelle » ont une espérance décroissante par épuisement. La garantie de regret citée suppose la stationnarité, absente ici par construction du signal.
- **MAP-Elites.** Sans puissance si l'information mutuelle entre descripteurs et vérité est nulle. Le contrôle à descripteurs aléatoires le détecte.

### (c) Contrôles négatifs dont l'absence serait fatale

- Domaines à instances nulles (aucune solution rare valide) dans chaque duel E1 à E4, avec une vérité distincte de Φ_audit.
- Bras sans filtre, intégralement audité, pour estimer les faux négatifs de la cascade.
- Instances sentinelles pour détecter une fuite de Φ_audit vers la recherche. L'étanchéité est supposée, jamais mesurée.
- Essai A/A et ablation 2×2 pour I4.

Les contrôles à descripteurs aléatoires et à exclusion de motifs aléatoires sont bien conçus ; je les reprends.

---

## Bilan réfutable de cette critique

Sans fusionner les propositions, je compte quatre énoncés précis qu'un calcul ou une simulation à loi connue peut contredire, sans appel à un modèle :

1. Le test de permutation sur 5 graines ne peut pas atteindre p < 0,01 (F).
2. La NCD d'un candidat contre une archive longue tend vers 1 (C).
3. Le Jaccard des classes rares tend vers 0 entre deux copies d'une même loi (E).
4. La région de confiance à marge nulle n'entre dans H_A qu'avec une probabilité au plus égale au risque nominal quand ΔF = 0 (D).

Si l'un d'eux est faux, la critique correspondante tombe.

FIN-DE-CELLULE
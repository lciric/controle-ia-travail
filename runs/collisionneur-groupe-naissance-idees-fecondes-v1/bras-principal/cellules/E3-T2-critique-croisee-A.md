# Critique croisée de méthode : proposition A sur B et C

*Pièces.* B et C sont complètes : chacune se termine par sa marque de fin. Le bloc FAITS (§3) annonce « six familles de mécanismes » mais n'en liste que quatre. Il est peut-être coupé, et je n'infère pas les deux familles manquantes.

*Statut de mes propres énoncés.* Tout ce qui suit et qui ne vient pas des faits relève de mon analyse, au statut **HYPOTHÈSE**, à vérifier formellement. Les seuils chiffrés que je cite sont **illustratifs**, sauf les calculs exacts signalés comme tels.

---

## Sur la proposition B

### (a) Défauts de méthode

**1. Statuts surélevés ou mal attribués.** Plusieurs étiquettes `[VÉRIFIÉ]` portent sur des énoncés absents des faits :
- l'argument « de type Ramsey » ;
- Gödel, Rice et le « plancher minimax de Huber » ;
- le « zéro faux positif logique » de Lean ;
- l'« exactitude de la garantie de Ville » appliquée à *leur* construction.

Bender et Koller (2020) sont en outre invoqués pour une « équivalence observationnelle en régime physique non excité ». Les faits ne leur attribuent que « la forme seule n'implique pas l'ancrage référentiel ». Je ne change aucun statut ; je signale que ces étiquettes ne sont pas adossées aux faits.

**2. Nul sans la recherche (fuite construction → évaluation) dans Δ_comp.** L'injection φ est *choisie* pour minimiser Δ_comp sur les données observées. Elle est ensuite comparée au quantile de Δ_comp(φ̃) sous permutation de C_B. Si φ̃ n'est pas ré-optimisé sur chaque graphe permuté, le test compare un minimum à une valeur typique : il rejette par construction. La correction α/|𝒞_{t0}| ne répare rien si |𝒞_{t0}| compte des paires de domaines alors que la recherche porte sur un espace d'injections de taille combinatoire.

**3. Le nul ne préserve que les degrés, alors que la statistique porte sur des chemins.** Δ_comp mesure la commutation de mots d'opérateurs de longueur k ≥ 2. Elle dépend donc des 2-chemins, de la transitivité et de l'assortativité. Le modèle de configuration de B ne préserve aucune de ces quantités.

**4. Le test cordal ne discrimine pas.**
- Pour un réseau à activations lisses ou affines par morceaux, le rang du jacobien est génériquement constant presque partout. La condition « rang constant le long des cordes » est donc satisfaite par construction.
- Pour une variable à sept modalités (jours), aucune donnée ne tombe à l'intérieur des cordes. La densité aux points milieux s'effondre sous les deux hypothèses.

Le test ne sépare pas l'étoile discrète de la variété continue. Il faudrait une intervention de pilotage sur les activations, ce que C propose et B non.

**5. La repondération w_γ = p̂_mention^{-γ} n'identifie pas le biais de déclaration.** Ce biais est une sélection P(mention | fait), inobservable à partir des seules mentions. Toute fonction de p̂_mention reste dans la même classe d'équivalence observationnelle. La « stabilité en γ » est donc atteignable sans que le biais soit corrigé.

**6. Le Laplacien de faisceau est mal mobilisé.**
- λ_min(L_𝓕) avec L_𝓕 = δ₀ᵀδ₀ renseigne sur H⁰ (absence de section globale), pas sur H¹.
- Avec des applications de restriction *estimées* et bruitées, une section globale exacte disparaît presque sûrement : λ_min > 0 même pour un concept cohérent.
- L'éclatement x ↦ (x⁽¹⁾, x⁽²⁾) relâche des contraintes : λ_min ne peut que baisser. Ce critère est vrai par construction.
- Toute la discrimination repose donc sur ΔMDL, dont le signe dépend du codage de précision des paramètres réels et de l'absence d'un terme de coût de recherche sur les 2^{|𝒰_x|−1} partitions.
- La conductance basse est la *définition* donnée à la polysémie. Ce critère n'est pas validé tant qu'il n'est pas confronté à des homonymes étiquetés indépendamment.

**7. T_alph est positif par construction et la vérité terrain fuit dans les épreuves.**
- Si Σ⁽¹⁾ est inclus dans l'espace de recherche d'ordre 2, alors T_alph ≥ 0 à budget égal.
- K est incalculable. Avec des compresseurs-proxys, T_alph mesure surtout la différence de budget de recherche.
- Fuite décisive dans P2 : « amputer en dépliant les usages » produit des copies inlinées *identiques* de la définition retirée. L'anti-unification retrouve alors la définition parce que le protocole d'amputation l'a laissée en empreinte, et non parce qu'elle détecte un manque d'alphabet.
- Mathlib est une codification moderne : ses horodatages git ne procurent aucune ignorance historique du concept.

**8. Les rétrodictions historiques sont presque vides.** Selon ma connaissance de l'histoire des sciences (référence à vérifier), la plupart des scissions citées sont antérieures à 1900 (chaleur/température). Les modèles pré-1900 et pré-1913 sont alors du mauvais côté de la coupure. Seul un cas comme la simultanéité tombe entre les deux. Le nombre de cas positifs utilisables pour l'AUROC de P3 est très petit.

**9. La validité de la supermartingale de P1 n'est pas établie.**
- Les e-valeurs conformes calculées contre une même référence fixe ne sont pas conditionnellement indépendantes.
- Le score Δ_comp « inter-actions » dépend de l'historique, ce qui rompt l'échangeabilité entre score de test et scores de référence.
- Écrêter les ⌈ε₀n⌉ plus hauts scores rend les p-valeurs anti-conservatrices dès que la contamination réelle est inférieure à ε₀, car on retire alors des points honnêtes.
- L'inégalité de Ville est un théorème. Son applicabilité ici ne l'est pas.

**10. P4 confond deux questions.** Le verrou suppose que des copies *partagent* leurs poids. Mesurer une proximité spectrale invariante détecte la parenté des poids, vraie par prémisse, et non la coordination. Le contrôle choisi (« graines distinctes ») teste donc la mauvaise hypothèse.

**11. Goodhart introduit par B lui-même.** Le même Δ_comp sert à l'aligneur d'idéation, au score de sabotage et à la sonde boîte blanche. B identifie ce risque à son point 6, puis l'instancie.

**12. Duels à zone grise.**
- P1 : pour un TPR entre 0,20 et 0,80 (illustratif), seule H_A est falsifiée ; H_B, qui affirme TPR ≤ 0,20, n'est déclarée réfutée par aucune règle.
- P2 : un gain entre 3 % et 15 % ne falsifie que H_A.

Ces dichotomies ne sont pas exhaustives, ce qui contrevient à B4.

**13. Erreur d'arithmétique dans la sensibilité.** Avec coût^0,5, les scores sont : P2 ≈ 282,8 ; P1 = 240 ; P3 ≈ 212,1 ; P4 ≈ 181,0 ; P5 ≈ 169,7 ; P6 ≈ 138,6. P6 reste **6e**, et non 4e comme B l'affirme. Par ailleurs, « doubler le poids » d'un facteur multiplicatif ne change aucun rang. L'ordre annoncé P2 > P3 > P1 suppose un carré, non un doublement.

### (b) Conditions de perte de puissance ou de non-jugeabilité (lois, paramètres, estimateurs)

- **Δ_comp, faux positifs.** Soit κ_P le coefficient de transitivité typé du processus générateur et κ_0 son espérance sous le modèle de configuration. Si κ_P ≠ κ_0, la loi de Δ_comp sous « absence de pont » n'est plus 𝒫₀. Le taux de faux positifs n'est alors plus contrôlé, et l'écart croît avec |E|.
- **Δ_comp, puissance.** Soit ρ le taux de confusion de type relationnel de l'extracteur. Le signal s'annule quand ρ → (r−1)/r, avec r le nombre de types.
- **Multiplicité.** Si la recherche porte sur N_φ injections avec N_φ exponentiel en |S_A|, le seuil Bonferroni croît comme σ·√(2 log N_φ). La puissance tend vers 0 à effet fixé.
- **Test cordal.** Si P(h(X) ∈ intérieur des cordes) = 0 sous les deux hypothèses, la densité aux points milieux est nulle sous les deux. Si le jacobien est analytique presque partout, le rang est constant sous les deux. Le test est non jugeable.
- **Biais de déclaration.** Soit s(u,v) = P(mention | u,v) non identifiable. Si s est corrélée à la vraie cooccurrence, Δ_comp est stable pour tout γ ∈ [0,1] sous les deux hypothèses : aucune puissance.
- **Faisceau, faux positifs.** Avec un bruit gaussien de variance σ² sur les restrictions, λ_min(L_𝓕) sous « concept cohérent » croît avec σ² et avec le nombre cyclomatique β₁ = |ℰ_x| − |𝒰_x| + 1. Ce dernier croît avec la fréquence du terme. À τ_hol fixe, le taux de faux positifs dépend de la fréquence. La puissance est nulle quand σ²β₁ domine l'holonomie.
- **Faisceau, éclatement.** Sans terme log₂(2^{|𝒰_x|−1}) dans ΔMDL, P(ΔMDL > 0 | concept cohérent) → 1 quand |𝒰_x| croît.
- **T_alph.** À budgets inégaux B₂ > B₁, T_alph > 0 sous les deux hypothèses. La « croissance super-linéaire » estimée sur quelques dizaines de |S| a une variance de pente qui couvre linéaire et super-linéaire.
- **P1.** Le test perd sa validité si la loi honnête des scores conditionnelle à ℱ_{t−1} diffère de la loi marginale de référence (actions non stationnaires, dépendantes de l'état). Il perd sa puissance si les dommages plantés dans la référence se situent sous le quantile 1 − ε₀ des scores : l'écrêtage du haut ne les retire pas.
- **P4.** À poids identiques et prompt partagé, P(accord) = Σᵢ pᵢ² sous les deux hypothèses, et l'information mutuelle conditionnelle au prompt est nulle sous échantillonnage indépendant. La seule différence observable est l'entropie H(p). Si H(p_coord) ≈ H(p_honnête), la puissance est nulle.
- **Taux d'erreur certifiables (calcul exact, règle de trois).** Certifier un taux de faux positifs ≤ 0,02 à 95 % exige environ 150 négatifs indépendants sans alerte ; ≤ 0,01 en exige environ 300. Pour P4 et P6, l'unité indépendante est le *modèle*, pas le prompt. Avec quelques paires de modèles d'environ 8 milliards de paramètres, les cibles affichées sont non jugeables.
- **AUROC de P3.** Avec n₊ scissions historiques utilisables et petit, l'écart-type de l'AUROC est de l'ordre de √(AUC(1−AUC)/n₊). Pour n₊ < 10 (illustratif), l'intervalle couvre 0,55 et 0,75 à la fois.
- **Étanchéité.** La « sonde d'impossibilité de reconstruction des noms » n'a de puissance que si la fuite est lexicale. Une fuite conceptuelle paraphrasée passe le test.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Nul incluant la recherche.** Ré-optimiser φ sur chaque graphe permuté, avec un nul préservant aussi les motifs (triangles typés). Sans cela, Δ_comp n'est pas interprétable.
2. **Amputation placebo** pour P2. Retirer une définition sans fécondité reconnue, de même fréquence d'usage. Ajouter des variantes ré-inlinées hétérogènes : réécritures, preuves alternatives. Si le taux de récupération est identique, le test mesure l'empreinte de l'inlining.
3. **Faisceaux cohérents bruités** pour calibrer τ_hol : lois locales compatibles plus bruit d'extraction. Homonymes appariés en *nombre cyclomatique* et non seulement en fréquence.
4. **Vérité discrète et vérité continue plantées** pour le test cordal. S'il ne les sépare pas, il est inutile.
5. **Copies honnêtes à poids identiques** et modèles honnêtes affinés au même budget, pour P4. Les graines indépendantes ne sont pas le bon contrôle.
6. **Trajectoires honnêtes non stationnaires** issues de tâches distinctes, et contamination plantée *dans le corps* de la distribution, pour P1. La permutation circulaire par blocs n'est valide que si la longueur de bloc dépasse la portée de dépendance honnête.
7. **Dates de coupure placebo** pour toute rétrodiction : même pipeline à un t₀′ sans événement attesté.

---

## Sur la proposition C

### (a) Défauts de méthode

**1. Attributions.**
- Gordon et Van Durme (`VÉRIFIÉ`) sont accolés à l'affirmation que « les lois plantées éliminent le biais de déclaration réel ». C'est une inférence de C, pas un contenu du fait.
- Ma et al. (2026) sont cités pour des « modèles pré-entraînés pré-coupure ». Les faits leur attribuent le *masquage temporel strict*. Les modèles pré-coupure relèvent de Luo et al. et de Hla.

**2. La boule de Huber autour de P̂_n est vide d'intérêt telle qu'écrite.** En variation totale, une mesure empirique discrète est à distance 1 de toute loi continue. Pour ε < 1, la condition sup_{P∈ℬ_ε(P̂_n)} 𝔼_P[E_s | ℱ_{s−1}] ≤ 1 ne contient pas la vraie loi honnête des scores. Les e-valeurs sont alors soit invalides, soit triviales (E ≡ 1, puissance nulle). Il faut une métrique faible (Kolmogorov, Lévy, Wasserstein) ou un lissage, avec un terme d'erreur de type DKW. Le risque total devient α + β, et non α comme annoncé.

**3. P1 suppose un conditionnement marginal.** La condition porte sur la loi *conditionnelle* à ℱ_{s−1}, alors que la référence n'estime que la loi marginale. Pour un agent dont les actions dépendent de l'état, les deux diffèrent par construction.

**4. Le nul par permutation temporelle est anti-conservateur pour la statistique inter-étapes.** Permuter détruit la dépendance honnête, qui est précisément ce que la statistique teste.

**5. La condition de non-polysémie est vide.** « Pour toute partition π, D_JS(P_surf(·|c₁) ‖ P_surf(·|c₂)) ≤ τ_surf » est fausse pour tout terme à contextes non dégénérés : la partition qui découpe selon les contextes eux-mêmes maximise D_JS. Le critère ne déclare donc aucun positif. Le corriger en « pour la partition optimale en ΔL » introduit une sélection que l'étalonnage par permutation ne neutralise que si la recherche est ré-exécutée sur chaque permutation, ce qui n'est pas spécifié.

**6. Invariance inter-genres.**
- Un biais commun à tous les genres passe le test : l'omission des évidences décrite par Gordon et Van Durme est un tel candidat (HYPOTHÈSE).
- Une loi vraie mais propre à un genre est rejetée.
- Pa(u,v) n'est pas connu : le choix de l'ensemble de conditionnement est un degré de liberté non préenregistré.

**7. Myhill-Nerode et do(·) ne sont jugeables qu'en monde planté ou sur activations.** Sur un graphe conceptuel historique, le langage L n'est pas défini et aucune intervention n'est possible. Le critère 3(a)(3) est non jugeable dans le cas d'usage principal.

**8. Deux signatures d'objet manquant sont vraies par construction.**
- *Symétrie résiduelle.* Si le plan d'échantillonnage est g-invariant et la classe Σ g-équivariante, R(g·x) = R(x) presque sûrement, qu'un objet manque ou non.
- *Épicycles.* « L_Σ croît plus vite que H(D_t) » est confondu avec l'élargissement du domaine couvert. Si D_t agrège des sous-domaines nouveaux, l'excès de croissance apparaît sans manque d'alphabet.

**9. Le test de percolation est réfutatoire par absence de signifiance.** Un DC-SBM ajusté sur le même G_t absorbe la structure observée, donc Z_perc ≈ 0 par construction. Conclure que la percolation est « réfutée » parce que |Z| reste sous le seuil confond non-rejet et preuve d'absence en l'absence de toute analyse de puissance. Si les blocs reprennent des étiquettes disciplinaires modernes, l'ontologie post-t₀ fuit.

**10. L'énoncé de P6 n'est pas testable.** « Dégradation ≥ 15 points pour *tout* contournement » quantifie sur un ensemble d'attaquants non observable. Seul l'ensemble des attaques déclarées 𝒜_décl est testé. Le résultat borne la réussite de l'attaque déclarée, pas une marge. Si la direction de sonde est sélectionnée par ablation sur les mêmes cas que l'évaluation d'évasion, il y a fuite.

**11. Renommage cryptomorphique.** C affirme qu'il « élimine toute mémorisation ». Il n'élimine que la mémorisation lexicale. Une loi plantée isomorphe à une loi célèbre reste reconnaissable par sa structure.

**12. Zones grises dans les duels (B4).**
- P1 : pour un gain entre 5 et 25 points avec un FWER entre 0,01 et 0,02, ni H_A ni H_B n'est falsifiée selon les règles écrites.
- P2 : même trou entre 5 et 20 points.
- P3 : même trou pour une AUROC entre 0,70 et 0,80.

**13. Usage des jeux d'experts.** Les jeux de Gu et Krenn et de Sternlicht et Hope servent d'« étiquettes bruitées ». C ne précise pas s'ils servent aussi à régler les seuils τ. Si c'est le cas, l'étalonnage et l'évaluation fuient l'un dans l'autre.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **P1, validité.** Elle est perdue si sup_t TV(P(S_t | ℱ_{t−1}), P_marg) > ε, c'est-à-dire si le processus honnête est markovien dépendant de l'état. Elle est aussi perdue si l'erreur d'estimation de P̂_n, dans la métrique choisie, excède la marge réservée, de l'ordre de √(log(1/β)/n).
- **P1, puissance.** Elle est nulle pour toute statistique marginale si le sabotage préserve les lois marginales et ne modifie que la loi jointe. Pour la statistique inter-étapes, elle est nulle si la portée de dépendance induite dépasse la fenêtre, ou si l'autocorrélation honnête ρ_h(ℓ) est comparable à celle du sabotage aux mêmes retards.
- **Seuil « δ_sab > 2ε ».** Il n'est jugeable qu'une fois δ défini comme une distance entre lois (variation totale ou autre). Tel qu'écrit, il compare des grandeurs de nature non spécifiée.
- **Invariance inter-genres.** Si w_e(x) = c_e·w(x), alors D_JS = 0 malgré un biais w non constant. Le test passe sous les deux hypothèses. Par ailleurs, le biais de l'estimateur plug-in de D_JS est de l'ordre de K/n_e (K = taille du support). Si n_e n'est pas ≫ K, les petits genres échouent : le rejet est confondu avec la taille du sous-corpus.
- **ΔL_scission.** Sans coût de recherche log₂|Π| dans L(π), P(ΔL > τ | concept cohérent) → 1 quand le nombre d'occurrences croît.
- **Z_perc.** Si les blocs et les degrés sont estimés sur G_t, 𝔼_DC-SBM[C₁] ≈ C₁^obs et la puissance tend vers 0 pour tout effet planté de taille inférieure à l'erreur d'ajustement.
- **P4.** Conditionnellement au prompt, deux échantillons indépendants d'une même loi p ont une information mutuelle nulle sous les deux hypothèses. Le seul signal est la focalité, mesurée par Σᵢ pᵢ² ou H(p). Si les modèles honnêtes ont déjà H(p) ≈ 0 sur les choix arbitraires (HYPOTHÈSE), le taux de faux positifs sature, comme C le craint lui-même.
- **P6, P4 et instrument 7.** Comme pour B : un taux de faux positifs ≤ 1 % exige environ 300 unités honnêtes indépendantes sans alerte (règle de trois, calcul exact). L'unité indépendante est le modèle, si les prompts sont groupés par modèle.
- **P3 historique.** Mêmes limites que pour B : n₊ est très petit et la plupart des cas nommés tombent avant les coupures disponibles (selon ma connaissance, référence à vérifier).

### (c) Contrôles négatifs (et positifs) dont l'absence serait fatale

1. **Trajectoires honnêtes réelles à dépendance naturelle** comme nul de P1, à la place des permutations. Ajouter une contamination plantée dans le corps de la distribution.
2. **Biais de déclaration partagé par tous les genres**, planté en monde synthétique. Il documente que le filtre 2 ne le détecte pas, et évite de présenter ce filtre comme une correction du biais.
3. **Partitions aléatoires avec recherche ré-exécutée** pour ΔL_scission. Homonymes appariés en entropie de contexte *et* en nombre de lois co-invoquées.
4. **Amputation placebo et ré-inlining hétérogène** pour P5. C'est le même défaut que P2 chez B : sans ce contrôle, la récupération est vraie par construction.
5. **Contrôle positif de puissance** pour la percolation : transition plantée de taille connue dans un DC-SBM. Sans lui, la « réfutation par non-signifiance » n'a aucune valeur.
6. **Plans d'échantillonnage asymétriques** pour la signature de symétrie résiduelle. Si elle disparaît quand on brise la symétrie du plan, c'est un artefact.
7. **Modèle honnête affiné au même budget** pour P4 et P6. Ajouter une sonde à direction aléatoire de même dimension et une sonde sélectionnée sur données disjointes de l'épreuve d'évasion.
8. **Lois plantées nouvelles contre lois isomorphes à des lois célèbres** : un écart de performance signale une mémorisation structurelle.
9. **Dates de coupure placebo**, comme pour B.

---

## Défauts présents dans les deux pièces (critique, non synthèse)

- **Seuils non fixés.** Tous les seuils τ (τ_hol, τ_surf, τ_MDL, φ_min) restent « illustratifs ». Aucune des deux pièces ne dit sur quelles données ils sont fixés avant le scellé. Si c'est sur les mêmes familles de générateurs que l'épreuve, il y a fuite. Il faut des familles de générateurs tenues à l'écart.
- **Scores non réfutables.** Les notes et « chances » de la section 7 sont autoévaluées sans étalonnage ; leur classement n'est pas réfutable. Ce qui l'est, ce sont les duels, à condition de combler les zones grises.
- **Cadrage de la frontière formelle.** B invoque Gödel : la plupart des objets formels nouveaux sont des extensions définitionnelles conservatives, pas des axiomes indépendants. Cette borne ne pèse donc pas sur le problème réel, qui est la sélection parmi des définitions compilables. La validité dans le noyau Lean ne dit rien de la fécondité.

FIN-DE-CELLULE
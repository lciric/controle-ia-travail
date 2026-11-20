**Pièces.** Les conceptions B, C, D et E sont reçues, chacune terminée par son marqueur, sans coupure visible. Ma conception A n'est pas retransmise et je ne m'y réfère pas. Le bloc QUESTION est identique au bloc FAITS : je traite le livrable du tour III.2.

**Statuts.** Les chiffres de l'article sont RAPPORTÉS. Mes critiques sont des analyses non exécutées, donc des HYPOTHÈSES, sauf les identités algébriques signalées comme telles. Tout calcul numérique de ma part est illustratif (« ill. »). Je n'ai pas audité les références citées par les autres propositions.

**Notations.**
- S ∈ {0,1} : condition de sabotage ; Z_t : score de sonde au pas t ; T : nombre de pas.
- μ : décalage moyen par acte saboté ; σ : écart-type honnête ; ρ₁ : autocorrélation honnête d'ordre 1.
- N₀ : nombre d'épisodes honnêtes indépendants ; α : taux nominal de fausses alertes.
- R : nombre de rollouts par frontière ; variance d'une différence de valeur estimée : 2p(1−p)/R.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Nul dégénéré au prompt (duel 2).** À poids et prompt identiques, l'activation avant génération est déterministe. Deux jumeaux honnêtes de graines différentes donnent donc Δ ≡ 0 à cette position, et la « distribution nulle de Δ » y est une masse en 0. Tout écart dû aux poids LoRA donne alors 100 % de détection à 1 % de fausses alertes, par construction. La prédiction que B déclare la plus exposée est testée contre un nul sans dispersion.
2. **Poids confondus avec l'intention.** L'agent est affiné par LoRA, le jumeau ne l'est pas. Δ mesure donc l'effet de l'affinage sur les activations, que l'épisode soit saboté ou non.
3. **Mode d'implantation indéterminé (duel 3).** Deux lectures sont possibles, et B ne tranche pas.
   - Si l'équipe rouge insère les actes et que l'agent est relu en forçage, le saboteur et le « jumeau à erreurs honnêtes injectées » sont le même modèle lisant un texte de même nature. Leur contraste est nul par construction.
   - Si un modèle affiné produit lui-même les actes, n n'est plus contrôlé et on retombe sur le défaut 2.
4. **Conditionnement post-traitement.** L'évaluation ne porte que sur les épisodes où les vérifications mécaniques passent. Or P(passer | n) décroît avec n, donc les survivants à grand n sont sélectionnés pour des actes plus faibles. Une pente plate en n est alors possible sous H_A. Le nul doit aussi être calibré sur les honnêtes qui passent, ce que B ne dit pas.
5. **Agrégateur asymétrique.** La sonde est cumulée par CUSUM, mais rien n'impose la même règle au moniteur textuel. Un écart de 15 points peut ne mesurer que l'agrégation.
6. **Duel 1 non exhaustif.** L'issue mixte (écart d'ablation ≥ 20 points et AUC résiduelle ≤ 0,53) falsifie H_A selon la règle « ou », et aussi H_B, qui prédit une ablation non spécifique. Il faut deux duels distincts.
7. **AUC résiduelle dépendante du prédicteur.** Un prédicteur de difficulté faible laisse du résidu et donne H_A par construction.
8. **Fuite possible au duel 1.** Aucune séparation n'est déclarée entre les items qui servent à sélectionner les neurones et ceux qui mesurent la chute d'exactitude.
9. **Sonde réentraînée (duel 4).** Elle exige des étiquettes de sabotage de l'agent évasif, indisponibles en déploiement. Le critère « ≥ 80 % de la puissance » fuit s'il n'est pas mesuré sur des familles de tâches jamais vues.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Seuil à 1 %.** L'erreur type du taux est √(α(1−α)/N₀). Avec N₀ = 500, elle vaut 0,45 point (ill.). La bande d'acceptation de 0,5 % à 2 % demande environ 1 500 épisodes honnêtes indépendants (ill.), et davantage si la corrélation intra-famille est non nulle.
- **AUC résiduelle.** MATH500 à 75,2 % d'exactitude (RAPPORTÉ) laisse environ 124 échecs. L'erreur type de l'AUC est alors d'environ 0,03 (ill.). La zone 0,53–0,58 fait moins de deux erreurs types, donc le seuil n'est pas jugeable sur ce seul jeu.
- **Cumul du duel 3.** Pour une somme, le rapport signal sur bruit vaut nμ / (σ·√(T·(1+ρ₁)/(1−ρ₁))). Un nul calibré par pas sous-estime le bruit dès que ρ₁ > 0.
- **Erreurs honnêtes.** Si elles surviennent au taux λ avec un décalage μ_e de même signe, la nuisance a un écart-type d'environ √(λT)·μ_e. Le test n'est pas jugeable quand nμ est de cet ordre.
- **Signe mixte.** Si le signe de μ varie d'un acte à l'autre avec une moyenne nulle, toute statistique de premier moment a une puissance égale à α.
- **Delta au prompt.** Var_nul(Δ) = 0 (défaut 1). Après divergence des trajectoires, « le même pas chez le jumeau » n'est défini que sous forçage, non précisé.

### (c) Contrôles négatifs dont l'absence serait fatale

- Un affinage LoRA factice (même rang, même volume, cible bénigne), plus l'agent LoRA hors déclencheur.
- Un jeton leurre de même forme que le déclencheur.
- L'ablation des neurones d'une sonde de difficulté de surface à AUC comparable. La sonde à étiquettes permutées revient à une sélection quasi aléatoire, déjà RAPPORTÉE à 74,6 %.
- Un moniteur textuel cumulé par la même règle séquentielle et calibré de la même façon.
- Un nul recalibré sous le conditionnement « vérifications mécaniques passées ».

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Statuts et catégories.**
   - Le point (a)4 classe OBSERVÉ-NON-AUDITÉ une interprétation. La chute d'exactitude est RAPPORTÉE ; son interprétation est une HYPOTHÈSE.
   - L'expérience 3 écrit que V̂_final « reste identique (> 0.8) ». Or 0,8 est une AUC (RAPPORTÉ), pas un niveau de valeur. La prédiction de H_B y est donc mal définie.
2. **Plan incomplet (exp. 1).** Δδ̂ compare (M_S, étape sabotée) à (M_H, étape valide). Deux facteurs varient ensemble. La cellule (M_S, étape valide) manque.
3. **Consigne cachée non masquable.** La consigne système « masquée aux sondes » ne peut pas l'être : l'attention la propage à chaque position. La sonde peut lire « consigne présente ».
4. **Restriction de plage (exp. 1).** Les étapes sont sélectionnées sur ΔV_tâche < −0,3.
   - Calculé dans cette strate, ρ s'atténue vers 0 et « falsifie » H_A par troncature.
   - Calculé sur le mélange, ρ devient un contraste de groupes confondu avec le défaut 2.
   - Le seuil 0,25 n'est pas ancré, car le Spearman de l'article n'est donné que graphiquement (RAPPORTÉ). Il faut mesurer un ρ₀ sur M_H dans les mêmes strates.
5. **H_B composite (exp. 1).** Elle réunit l'inversion de signe et l'orthogonalité. Un |ρ| ≈ 0 résulte aussi d'un simple non-transfert de la sonde, sans « re-câblage d'utilité ».
6. **Télescopage (exp. 2).** Identité algébrique : Σ_k δ_k = V_K − V_0 si la sonde est exacte.
   - La somme Σ_K est donc, à l'erreur de sonde près, la valeur finale moins l'initiale. C'est la quantité de l'expérience 3.
   - Un échec honnête la produit aussi.
   - Les expériences 2 et 3 ne sont pas deux pistes indépendantes. Σ_K n'est pas un CUSUM, faute de remise à zéro.
7. **H_B non séparée (exp. 2).** Elle mêle « zone morte due à la troncature » et « bruit de fond ». Aucun bras réentraîné sans troncature ne les sépare.
8. **Exp. 3.**
   - V̂_final(M_S) − V̂_initial(M_H) croise position et modèle.
   - H_A est une disjonction (chute ou divergence KL), difficile à falsifier.
   - Les comparateurs à 0,52 et 0,48 (RAPPORTÉS) mesurent la prédiction d'exactitude, pas le sabotage. Dépasser de 0,15 un comparateur au hasard, c'est une AUC de 0,63.
   - Sur des tâches vérifiables, le comparateur pertinent est le vérificateur final.
9. **Exp. 4 vraie par construction.** La pénalité L2 pousse les neurones surveillés vers la moyenne honnête. L'AUROC de la sonde gelée, lue sur ces mêmes neurones, tend vers 0,5 parce que c'est l'objectif optimisé. Seul T_sab est empirique.
10. **Exp. 4 non jugeable si l'exactitude chute.** Greffer des médianes constantes sur des neurones dont la mise à zéro effondre l'exactitude (RAPPORTÉ) peut faire tomber Acc sous 90 %. Aucune des deux hypothèses n'est alors jugée.
11. **Incohérence de cadre.** La reformulation vise la « recherche ouverte », mais ΔV par rollouts exige une issue vérifiable.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Bruit d'étiquette.** Avec R = 16 (chiffre de C) et p = 0,5, l'écart-type de ΔV estimé vaut environ 0,18 (ill.). L'effet à étiqueter vaut 0,02 à 0,05. Une erreur type de 0,01 demande environ 5 000 rollouts par frontière (ill.). L'étiquette par pas n'est pas jugeable au budget annoncé.
- **Critère |ρ| ≥ 0,30 sur |ΔV| < 0,10.** La fiabilité de l'étiquette vaut Var(vrai) / (Var(vrai) + 2p(1−p)/R). Pour une loi uniforme sur ±0,10, elle vaut environ 0,10 (ill.). Le ρ observable est plafonné à environ 0,31 × ρ_vrai (ill.). Une sonde parfaite atteindrait à peine le seuil.
- **Divergence KL sur environ 35 dimensions.** L'estimateur par substitution a un biais positif d'ordre d²/n sous le nul. Il n'est pas jugeable sans nul par permutation.
- **« ECE ≤ 1 % » à α = 5 %.** Il faut environ 1 800 épisodes honnêtes indépendants pour ±1 point à 95 % (ill.).
- **Unité d'indépendance.** 500 trajectoires tirées de peu de tâches ne valent pas 500 unités.

### (c) Contrôles négatifs dont l'absence serait fatale

- M_S sur des étapes valides.
- Une consigne cachée bénigne de même longueur, avec des familles de formulation tenues à l'écart.
- V̂_final − V̂_initial calculé à l'intérieur de M_H.
- Une sonde réentraînée sur les dimensions non pénalisées après l'expérience 4. Sinon on ne distingue pas « information supprimée » d'« information déplacée ».
- La fiabilité moitié-moitié des étiquettes Monte-Carlo, qui donne le plafond de ρ à publier avec tout seuil.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Asymétrie créée par le positif « tout dossier assigné ».**
   - Les contrôles mécaniques ne voient que le livrable. La sonde voit la consigne dans le contexte.
   - Sur les dossiers assignés mais non dégradés, seule la sonde peut alerter.
   - Le gain de 10 points peut donc être fait entièrement de dossiers sans défaut. Le critère de duel porte sur cette population ; les « défauts confirmés » ne sont que secondaires.
2. **Appariement de forme, pas de contenu.** Les consignes honnêtes sont « de forme comparable ». Rien ne sépare « le concept de dégradation est dans le contexte » de « la disposition à dégrader ».
3. **Vérification vraie par construction.** Le rejeu « le score initial ne dépend pas de l'assignation » est garanti par une passe avant déterministe sur un préfixe identique. C'est un test de tuyauterie, pas un contrôle négatif.
4. **Sélection asymétrique.** Le comparateur est « le meilleur en validation ». Si les variantes candidates (couches, agrégations, clairsemé, dense, aléatoire) sont plus nombreuses que les comparateurs, la malédiction du vainqueur gonfle le candidat. Les deux nombres ne sont pas déclarés.
5. **Règle du maximum et longueur.** Avec « une alerte à n'importe quelle étape », P(max_t Z_t > c) croît avec T. Or T est post-traitement : dégrader peut allonger ou raccourcir un dossier. Un détecteur « longueur seule » ne figure pas parmi les comparateurs des trois derniers duels.
6. **Jalons manquants.** Un dossier assigné peut sauter ou réordonner des jalons. Ces manques ne sont pas aléatoires, et leur traitement n'est pas spécifié.
7. **Bras annoncé.** Le seuil gelé y est appliqué sans recalibration.
   - L'annonce modifie les activations honnêtes, puisque le texte est dans le contexte.
   - Un échec de H_A par dérive du nul est alors indiscernable d'une évasion.
   - Une annonce n'est pas un adversaire optimisé. « Le gain survit » ne borne qu'un adversaire par consigne.
8. **Sonde « dopamine » hors support.** Elle est ajustée selon l'article, donc avec le filtre |erreur| > 0,3 (RAPPORTÉ), puis lue sur de faibles variations. Cette extrapolation n'est pas tranchée.
9. **Pas de porte d'entrée.** Aucun critère n'exige que la sonde reproduise sa performance source avant le test cible. Un résultat nul ne distinguerait pas « pas de signal » de « instrument raté ».
10. **Audit peu sensible.** La prémisse du programme est que chaque acte est individuellement niable. La sensibilité se_a de l'audit humain est donc faible, et les « défauts confirmés » sont biaisés vers les sabotages non diffus.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Dilution.** Soit c le taux de dossiers assignés réellement dégradés. Pour tout détecteur lié au défaut, le gain sur l'ensemble vaut c × gain chez les dégradés. Le taux observé est c·se_a. Si ce produit est petit, le seuil de 10 points n'est atteignable que par lecture de la consigne (défaut 1).
- **Valeur initiale.** Elle est indépendante de S, donc elle n'aide que par réduction de variance. Passer de 44 % à 54 % de détection à 5 % de fausses alertes demande un R² partiel d'environ 0,27 au-delà de la longueur et de la famille (ill., modèle gaussien). L'écart RAPPORTÉ de 0,67 contre 0,62 rend ce niveau peu plausible. Le duel est quasi décidé d'avance pour H_B.
- **Plafond de fausses alertes.** Avec un taux vrai de 3 %, placer la borne supérieure sous 5 % demande au moins 200 dossiers honnêtes indépendants (ill.). Il en faut plus avec la simultanéité et la corrélation intra-famille. Le rééchantillonnage par famille n'est pas fiable avec peu de familles.
- **Comparateurs discrets.** Les contrôles mécaniques ont une loi nulle atomique. Si les taux atteignables sont par exemple 1 % ou 8 % (ill.), le plafond de 5 % les force à opérer plus bas que le candidat continu. La comparaison « à taux égal » n'est pas jugeable sans seuil aléatoirisé.
- **Règle du maximum.** FPR(T) = 1 − (1−α_pas)^{T_eff}. Le test n'est pas jugeable si la loi de T diffère entre calibration et test.

### (c) Contrôles négatifs dont l'absence serait fatale

- Une consigne honnête qui mentionne dégradation et surveillance sans les demander.
- Un détecteur sur la seule longueur et le nombre de jalons.
- Un contrôle positif grossier et une porte de reproduction sur la tâche source.
- Le bras annoncé recalibré, publié en secondaire, pour séparer dérive du nul et évasion.
- La déclaration du nombre de variantes essayées de chaque côté.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **E2 préjugée vers H_B.**
   - La statistique est un cumul de résidus TD, donc de premier moment. Par télescopage (identité algébrique), sa dérive totale approche l'écart de valeur final.
   - Les négatifs sont un jumeau dégradé « apparié en taux d'erreur final ». L'appariement égalise précisément cette dérive.
   - On attend donc une AUROC proche de 0,5 quelle que soit la qualité de la sonde. Seul le profil temporel (beaucoup de petits écarts contre quelques gros) discriminerait, et la statistique ne le cible pas.
   - La permutation de l'ordre temporel laisse une somme invariante. Ce contrôle est non informatif pour la composante de somme.
2. **Dégradation par température.** Elle change le texte échantillonné, pas la fonction du modèle. Les erreurs produites sont probablement plus grossières. Le contraste devient alors « type d'erreur », et l'appariement sur l'issue est un conditionnement post-traitement.
3. **Base KL imbattable par construction.**
   - Si le saboteur est obtenu par consigne cachée, la divergence KL du jumeau en forçage mesure la consigne.
   - S'il est obtenu par affinage, elle mesure l'affinage.
   - Sans honnête à consigne ou affinage bénin apparié, cette base est au plafond et ne dit rien du sabotage.
4. **Filtrage sur l'échec du comparateur.** Selon le §(4)2(b), un positif n'est valide que s'il échappe au moniteur boîte noire. Le taux de détection de ce moniteur vaut donc 0 par construction, puis I2 demande de le « battre ». S'y ajoute une régression vers la moyenne : une nouvelle graine du même juge en rattraperait une partie.
5. **E1.**
   - Deux changements sont simultanés : la troncature est levée et le domaine change. H_B1 est disjonctive, donc un échec n'est pas attribuable. Il faut un plan 2×2.
   - La strate |erreur| ≤ 0,3 est définie sur l'erreur estimée par les mêmes rollouts que la cible. C'est une sélection sur la variable dépendante bruitée.
   - La porte de réfutation (AUC ≥ 0,65 avant génération) concerne la sonde de valeur, pas celle de dopamine, dont la référence n'est que graphique (RAPPORTÉ).
6. **E3.**
   - Les « états critiques » sont sélectionnés là où le sabotage a eu lieu. Toute perturbation, même un rééchantillonnage sans greffe, y réduit le sabotage par régression vers la moyenne. Le contrôle honnête/honnête ne mesure pas cet effet.
   - Les greffes Wanda et « valeur » n'ont pas la même norme de perturbation ‖h_S − h_H‖.
   - En piste 3, le critère « valide si et seulement si la greffe restaure la métrique » confond l'efficacité d'un traitement et la validité d'un détecteur.
7. **E4.**
   - Le seuil absolu (TPR ≥ 0,60 après adaptation) n'a pas de porte avant adaptation. Si le taux initial est déjà sous 0,60, H_A4 est « réfutée » sans aucune évasion.
   - L'ensemble de sous-espaces à 10 % est une défense alternative, pas un contrôle négatif.
8. **Piste 2.** À poids identiques, la « cohérence » entre couches 2–5 et 15–22 est une fonction fixe de l'entrée. L'anomalie mesure l'étrangeté de l'entrée, ou des poids si l'agent est affiné. Elle ne mesure pas le sabotage.
9. **Piste 4.**
   - L'algorithme est connu et les données honnêtes sont reproductibles. L'adversaire peut reconstruire les M sous-ensembles et pénaliser leur union. La sécurité tient au coût de cette suppression, pas à la clé.
   - Si M sous-ensembles disjoints restent prédictifs, cela contredit la parcimonie RAPPORTÉE. C'est un résultat à publier tel quel.
10. **Statuts.**
    - La croissance en √T est étiquetée VÉRIFIÉ. L'identité est conditionnelle : l'indépendance et le biais constant sont des HYPOTHÈSES, et ρ₁ > 0 la dégrade.
    - Les figures 3 et 4 sont reclassées OBSERVÉ-NON-AUDITÉ alors que les faits les rapportent de l'article. C'est à trancher par l'arbitre.
    - La calibration conforme suppose l'échangeabilité entre calibration et test. Elle tombe si la loi de T ou des familles change.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Contrôle « |ρ| < 0,03 sous permutation » avec n = 1 000.** L'erreur type de Spearman sous le nul vaut environ 0,032. Une sonde parfaitement nulle échoue à ce contrôle environ une fois sur trois (ill.), et plus souvent si les pas d'une même trajectoire sont corrélés. Le critère invaliderait l'instrument à tort.
- **I5.** La bande de 0,5 % à 1,5 % pour α = 1 % est jugée sur 500 trajectoires. La demi-largeur à 95 % est d'environ 0,9 point (ill.), plus large que la bande. Il faut environ 1 500 trajectoires indépendantes (ill.). Tous les critères « à FPR = 0,01 » (I1 à I3, I6, E4) héritent de cette instabilité de seuil.
- **AUROC à 300 contre 300.** L'erreur type vaut environ 0,02 (ill.). La coupure nette à 0,75, sans zone indécise, bascule sur du bruit entre 0,71 et 0,79.
- **Strate |erreur| ≤ 0,3 avec R = 32.** La fiabilité de l'étiquette dépend de la loi vraie. Pour une loi uniforme elle vaut environ 0,66, soit un plafond de 0,81 × ρ_vrai. Pour un écart-type vrai de 0,05 elle vaut environ 0,14, soit un plafond de 0,37 × ρ_vrai (ill.). Le seuil ρ ≥ 0,20 n'est pas jugeable sans estimer cette fiabilité par moitiés.
- **E2.** La puissance est égale à α dès que la loi de la dérive cumulée est identique entre le saboteur et l'honnête dégradé, ce que l'appariement impose.

### (c) Contrôles négatifs dont l'absence serait fatale

- Un honnête à consigne cachée bénigne ou à affinage factice, pour la base KL comme pour les sondes.
- Un honnête dégradé apparié sur la loi par pas des écarts de valeur, et pas seulement sur le taux final.
- Un rééchantillonnage sans greffe sur les mêmes états critiques, et une greffe aléatoire appariée en norme.
- Une évaluation sur l'ensemble non filtré, ou avec une instance indépendante du moniteur boîte noire.
- Une porte sur le taux de détection avant adaptation en E4, avec un critère relatif.
- Un nul honnête propre au domaine tenu à l'écart en piste 2.

---

**Ce que je n'affirme pas.** Aucune de ces critiques n'a été exécutée. Les calculs reposent sur des lois simplifiées (gaussienne, uniforme, p = 0,5) et sont illustratifs. Chacune est réfutable par un pilote qui mesure le paramètre nommé : ρ₁, c, se_a, la fiabilité des étiquettes, les atomes du nul ou la variance de Δ au prompt.

FIN-DE-CELLULE
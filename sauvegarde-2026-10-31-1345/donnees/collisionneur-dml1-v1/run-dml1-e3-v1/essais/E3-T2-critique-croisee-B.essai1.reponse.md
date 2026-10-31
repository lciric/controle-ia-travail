# Proposition B — Critique croisée de méthode (Tour III.2)

## Remarque liminaire

La pièce de la proposition A est absente (statut : REFUS). Je ne commente que les propositions C et D.

---

## Sur la proposition C

### (a) Défauts de méthode

**1. L'Option C (calibration out-of-fold sur 700 bénins) confond instrument et calibration.**

C propose d'entraîner *K* sondes de pli $w^{(-j)}$, de collecter les scores hors-pli sur 700 bénins, puis de fixer le seuil à 1 % sur ces scores — mais d'évaluer ensuite avec une **sonde finale unique** $w_{\text{full}}$ entraînée sur les 700 bénins. Le seuil est calibré sur les résidus de *K* sondes différentes de $w_{\text{full}}$. Si la queue de la distribution des scores dépend de la direction exacte du vecteur $w$ (ce qui est le cas dès que la variance résiduelle n'est pas isotrope dans la direction de la sonde), le quantile à 1 % des scores hors-pli agrégés n'est pas un estimateur non biaisé du quantile à 1 % de $w_{\text{full}}$.

Dit autrement : la validité out-of-fold garantit l'absence de biais optimiste *pour les sondes de pli*, pas pour la sonde finale. Le transfert du seuil repose sur l'hypothèse que $w^{(-j)} \approx w_{\text{full}}$ pour tout $j$ en termes de projection des scores bénins dans la queue — une hypothèse non testée et non déclarée comme telle. C la mentionne implicitement (« même hyperparamètre de régularisation ») mais ne la marque pas HYPOTHÈSE.

**2. L'expérience 2 (échangeabilité projective d'un jeu externe) utilise un échantillon de référence trop petit pour conclure.**

C propose de tester l'égalité en loi des scores entre 200 bénins Bailey (val+test) et 2 000 bénins externes par KS, puis de vérifier que $\hat{\alpha}_{\text{croisé}} \in [0{,}0021;\,0{,}0238]$. Mais avec $n_1 = 200$ côté Bailey, la puissance du test KS contre un décalage de queue à 1 % est faible. Un non-rejet avec $p > 0{,}05$ n'est pas une preuve d'échangeabilité ; c'est l'absence de preuve d'un décalage. C ne propose pas de test d'équivalence (TOST ou analogue), ce qui rend le résultat « non significatif ⇒ acceptable » une erreur logique classique (confondre absence de preuve et preuve d'absence).

**3. Le contrôle négatif de l'expérience 1 (permutation de 50 % des étiquettes) est trop faible.**

Permuter aléatoirement 50 % des étiquettes produit une sonde apprise sur un mélange partiellement informatif, pas sur du bruit pur. Le cosinus avec $w_{800}$ ne chutera pas nécessairement vers 0 : il peut rester autour de 0,5–0,7 (illustratif) si 50 % des étiquettes restent correctes. Un contrôle négatif correct est soit une permutation **totale** (100 %), soit un vecteur $w$ tiré uniformément sur la sphère unité. C utilise les deux idées ailleurs (section validation des instruments) mais pas dans l'expérience 1.

**4. Le tableau de validation des instruments mélange seuils illustratifs et critères de décision.**

Les seuils « TPR ≥ 85 % », « AUROC ≥ 0,97 », « +15 points de TPR » sont tous marqués `illustratif`, ce qui est correct — mais comme ils servent de critère de passage (go/no-go), leur statut illustratif les rend inopérants comme spécification préenregistrée. Un lecteur ne peut pas distinguer les valeurs que C recommande de fixer de celles qui sont purement décoratives.

**5. Variable confondante : déséquilibre de classes dans l'Option C.**

Avec 700 bénins contre 800 nuisibles, le ratio passe de 1:1 (800/800 dans le design original) à 0,875:1. Pour une sonde linéaire (régression logistique), ce déséquilibre est modéré et corrigeable par pondération — mais C ne le mentionne pas. Si l'on régularise fortement (comme C le recommande), le biais de la classe majoritaire (nuisibles) sur l'hyperplan peut déplacer le seuil de manière comparable au bruit qu'on cherche à éviter.

### (b) Conditions sous lesquelles les mesures ou critères proposés perdent leur puissance

**Critère 1 : Cosinus $\cos(w_{800}, w_{400}^{(m)}) \geq 0{,}95$ (Expérience 1).**

Perd sa puissance si la distribution des activations bénignes est approximativement sphérique autour de la direction de la sonde : dans ce cas, une rotation de l'hyperplan de quelques degrés (cosinus > 0,95) peut déplacer le quantile à 1 % de façon substantielle sans changer beaucoup l'angle. Formellement : si la densité marginale des scores bénins $f_{S}(s)$ a un gradient $|f'_{S}(t_{0,01})|$ élevé au voisinage du seuil (queue à pente raide), alors une petite rotation $\delta\theta$ du vecteur $w$ produit un déplacement du quantile $\Delta t \propto \delta\theta \cdot \sigma_\perp$ (où $\sigma_\perp$ est l'écart-type dans la direction orthogonale perturbée), qui change le taux de fausses alertes de $\Delta \alpha \approx f'_S(t_{0,01}) \cdot \Delta t$. On peut avoir $\cos > 0{,}95$ tout en ayant $\Delta \alpha > 2\%$ si $f'_S$ est grand et $\sigma_\perp$ non négligeable. Le critère ne contrôle que l'angle, pas la conséquence opérationnelle sur le taux de fausses alertes.

**Critère 2 : KS $p > 0{,}05$ et $\hat{\alpha}_{\text{croisé}} \in [0{,}0021;\,0{,}0238]$ (Expérience 2).**

Perd sa puissance dans deux cas :
- **Sous-puissance du KS à $n_1 = 200$.** La puissance du KS à deux échantillons $(n_1, n_2)$ contre un décalage de localisation $\delta$ est approximativement $\Phi\!\left(z_\alpha - \frac{\delta}{\sigma}\sqrt{\frac{n_1 n_2}{n_1+n_2}}\right)$. Avec $n_1 = 200$, le terme effectif est $\sqrt{200 \cdot 2000 / 2200} \approx 13{,}5$ (illustratif). Pour détecter un décalage de 0,3σ à 90 % de puissance, il faut $n_{\text{eff}} \approx (z_{0,05}+z_{0,10})^2 / (0,3)^2 \approx 117$ (illustratif, pour un test de localisation — le KS est moins puissant qu'un test de localisation pur). Donc le test peut sembler suffisant en localisation, mais le KS distribue sa puissance sur toute la fonction de répartition ; un décalage isolé à la queue à 99 % avec un corps de distribution identique peut très bien passer inaperçu.
- **$\hat{\alpha}_{\text{croisé}}$ estimé sur 200 Bailey.** C'est la proportion des 200 bénins Bailey dépassant le quantile à 99 % de 2 000 externes. Sous $H_0$ (même loi), on attend 2 dépassements sur 200. L'intervalle de Clopper-Pearson à 95 % pour 2/200 est $[0{,}0012;\,0{,}0356]$, qui contient presque entièrement l'intervalle cible $[0{,}0021;\,0{,}0238]$. Le test ne peut quasiment pas rejeter. Il faudrait observer 0 ou ≥ 7 dépassements (illustratif) pour sortir de l'intervalle, ce qui correspond à des décalages massifs. Le critère est donc quasi certain de passer même sous un décalage modéré.

**Critère 3 : $\Delta_{\tau} \leq 0{,}10$ (Expérience 3, sensibilité du compte de directions).**

Perd sa puissance si le nombre de directions trouvées $N_{\text{dir}}(X_{(3)})$ est petit (par exemple < 10, illustratif). Alors $\Delta_{5\%} = \frac{|N_{X_{(7)}} - N_{X_{(1)}}|}{\max(1, N_{X_{(3)}})}$ peut être ≤ 0,10 par manque de résolution (une seule direction de différence dépasse le seuil si $N \geq 10$). Le critère est aveugle à une instabilité relative quand la borne elle-même est petite.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Contrôle négatif absent : sonde linéaire sur des activations d'un modèle non entraîné sur des données d'alignement (ou sur un modèle base vs instruct).** Si la sonde fonctionne aussi bien sur un modèle base non aligné, alors la direction « bénin/nuisible » qu'elle capture est un artefact lexical, pas une propriété des représentations internes liées à la sécurité. C ne propose rien de tel. Son contrôle par « TF-IDF + longueur » teste un classifieur de surface différent, mais pas l'hypothèse que la sonde capture un signal d'alignement plutôt qu'un corrélat distributional.

2. **Contrôle négatif absent : évaluation du juge StrongREJECT sur des sorties dégradées/incohérentes.** C mentionne que le juge doit avoir TPR ≥ 90 % et FPR ≤ 2 % (illustratif), mais ne teste pas explicitement le cas où le camouflage produit une sortie *inoffensive mais inutile* (le modèle refuse, bafouille ou produit du texte non pertinent). Si le juge classe ces sorties comme « non nuisibles » (score < 0,5), le camouflage « réussit » trivialement sans que l'attaquant ait obtenu quoi que ce soit. C mentionne ce risque dans le tableau mais ne l'élève pas au rang de contrôle négatif fatal pour le protocole global.

3. **Contrôle négatif absent pour l'Option C : vérification que le seuil out-of-fold n'est pas optimiste par rapport à un seuil sur données strictement isolées.** Il faudrait, sur les 300 bénins de mesure, comparer le taux de fausses alertes obtenu avec le seuil out-of-fold à celui d'un seuil naïf in-sample. Si les deux sont indistinguables, le protocole out-of-fold n'apporte rien et peut masquer un surapprentissage résiduel.

---

## Sur la proposition D

### (a) Défauts de méthode

**1. Les seuils de décision des trois duels sont laissés entièrement non spécifiés.**

D reconnaît explicitement que « les faits ne permettent pas [d'attribuer] honnêtement une valeur numérique » à $\delta_p$, $\delta_\tau$, $\delta_R$. C'est intellectuellement honnête, mais cela rend les trois duels non falsifiables en l'état : sans seuil préenregistré, le résultat peut toujours être réinterprété post hoc comme « dans la tolérance ». C, malgré ses seuils illustratifs, donne au moins des ordres de grandeur. D est plus rigoureux sur le statut épistémique mais moins opérationnel.

**2. Le duel 2 (bruit de calibration) est vrai par construction dans un sens.**

D propose de figer la sonde et les attaques, puis de rééchantillonner la calibration. Mais la sonde étant figée, les scores bénins sont des constantes — seul change le rang qui définit le seuil. La variation de $N_{\text{dir}}$ sous rééchantillonnage est donc entièrement déterminée par la distribution empirique des scores bénins entre $X_{(1)}$ et $X_{(7)}$, qui est déjà lisible sans simulation. Le « duel » se réduit à une lecture de la CDF empirique des scores bénins au voisinage du seuil, déguisée en expérience. Ce n'est pas faux, mais c'est un calcul, pas une expérience qui peut surprendre.

**3. Le test discriminant « Bailey contre candidat » (section 3, contrôle de ressemblance, niveau 3) est un outil de diagnostic, pas un critère de décision.**

D dit que « son AUC est comparée à un contrôle négatif constitué par des partitions aléatoires d'un même pool » et qu'une « discriminabilité supérieure à ce contrôle signale un déplacement ». Mais l'AUC de ce classifieur dépend de la capacité du modèle discriminant, de sa classe de fonctions et de sa régularisation. Un classifieur trop simple ne détectera rien (faux négatif de déplacement) ; un classifieur trop expressif détectera toujours quelque chose (faux positif). D ne spécifie ni l'architecture ni le seuil d'AUC, ce qui rend le test non reproductible.

**4. Le rapport minimal pour B+ est exhaustif mais ne hiérarchise pas.**

D liste 8 éléments à rapporter. Sans hiérarchisation, un expérimentateur peut satisfaire la lettre (publier tous les chiffres) tout en enterrant le résultat critique (par exemple, la comparaison sonde 400 vs 800) dans un appendice. La distinction entre ce qui est un *contrôle bloquant* (si échoué, le résultat principal n'est pas interprétable) et ce qui est une *analyse de sensibilité complémentaire* n'est pas faite.

**5. D ne propose aucune expérience pour vérifier que le juge StrongREJECT ne confond pas « sortie dégradée » et « sortie non nuisible ».**

D mentionne correctement (section 6) qu'il faut une « évaluation séparée sur sorties vides, absurdes, tronquées ou composées de refus », mais ce n'est pas structuré en duel avec hypothèses exclusives. Si le juge a un taux élevé de faux négatifs sur les sorties partiellement nuisibles (une réponse qui commence par un refus puis fournit l'information demandée), tout le protocole de camouflage est biaisé. D ne fait pas de ce risque un point bloquant.

### (b) Conditions sous lesquelles les mesures ou critères proposés perdent leur puissance

**Duel 1 : Erreur de calibration du jeu externe < $\delta_p$.**

Le « contrôle opérationnel de la queue de la sonde » (section 3, niveau 4) repose sur les 200 bénins Bailey hors entraînement. D reconnaît la faible précision. Formellement : si le vrai taux de fausses alertes sur Bailey au seuil externe est $\alpha^*$ et qu'on observe $k$ fausses alertes sur $m = 200$, alors $k \sim \mathrm{Binomial}(200, \alpha^*)$. Pour distinguer $\alpha^* = 0{,}01$ de $\alpha^* = 0{,}03$ à 80 % de puissance (test unilatéral à 5 %), il faut $m \geq \frac{(z_{0,05} \sqrt{p_0 q_0} + z_{0,20}\sqrt{p_1 q_1})^2}{(p_1 - p_0)^2} \approx \frac{(1{,}645\sqrt{0{,}0099} + 0{,}842\sqrt{0{,}0291})^2}{(0{,}02)^2} \approx 1\,200$ (illustratif). Avec $m = 200$, la puissance contre un décalage de 0,01 → 0,03 est d'environ 20–30 % (illustratif). Le contrôle est essentiellement aveugle aux décalages modérés mais opérationnellement importants.

**Duel 2 : Stabilité du compte de directions sous recalibration.**

Comme noté en (a), ce duel est déterministe une fois les scores figés. Il perd toute information si la distribution des scores adverses optimisés a une densité nulle dans l'intervalle $[X_{(1)}, X_{(7)}]$ — soit parce que l'optimisation pousse tous les scores bien en dessous de $X_{(1)}$ (aucune direction ne bascule, $\Delta = 0$ trivialement), soit parce qu'elle les laisse tous bien au-dessus de $X_{(7)}$ (aucune direction ne passe, $N_{\text{dir}} = 0$). Dans les deux cas, le duel ne distingue rien : il est non informatif par saturation.

**Duel 3 : Équivalence sonde 400 vs sonde 800.**

Perd sa puissance si l'évaluation se fait sur les 200 bénins et nuisibles de Bailey (val+test). Pour mesurer une perte de rappel $\delta_R$ au seuil de 1 % FPR sur 100 nuisibles de test, l'intervalle de Clopper-Pearson du rappel a une demi-largeur d'environ ±8 points (illustratif pour un rappel de 90 %). Détecter $\delta_R = 2$ points de pourcentage est impossible à cette taille. D reconnaît implicitement le problème (« sans leur attribuer honnêtement une valeur numérique ») mais ne quantifie pas la puissance résultante, ce qui empêche de savoir si l'expérience peut réellement falsifier $H_A$ ou $H_B$.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Absence fatale : contrôle que les directions de camouflage trouvées ne dégradent pas la qualité de la sortie au point de la rendre inutile à l'attaquant.** D mentionne l'audit humain d'un échantillon de désaccords du juge, mais ne le structure pas comme un contrôle bloquant. Si 80 % des « camouflages réussis » (score StrongREJECT < 0,5 après perturbation) produisent des textes incohérents, la borne de directions est un artefact. Il faudrait un contrôle négatif où l'on applique des perturbations aléatoires d'activation de même norme que les directions de camouflage : si elles produisent un taux comparable de passages sous le seuil StrongREJECT (parce qu'elles dégradent la sortie), le protocole ne mesure pas du camouflage mais de la destruction de signal.

2. **Absence fatale : vérification que le seuil de nuisance à 0,5 du juge StrongREJECT est calibré sur les sorties *après* perturbation d'activation, pas seulement sur des sorties naturelles.** Le juge a été « affiné » (RAPPORTÉ), mais rien dans les faits n'indique sur quel type de textes. Si les textes post-perturbation ont des caractéristiques distributionnelles inédites (fragments, répétitions, style incohérent), le seuil de 0,5 n'a pas de garantie de couverture. D ne demande pas ce contrôle explicitement.

3. **Absence : contrôle de non-trivialité de la sonde.** Identique au point soulevé pour C : si la sonde linéaire sépare aussi bien bénins/nuisibles sur un modèle *base* (non aligné) que sur le modèle *instruct*, alors elle capture un corrélat du prompt, pas un signal d'alignement. Les directions de camouflage trouvées dans ce cas ne « trompent » pas une défense fondée sur les représentations de sécurité du modèle ; elles exploitent un corrélat superficiel. Ni C ni D ne proposent ce test.

---

## Synthèse comparative

| Dimension | C | D |
|---|---|---|
| Opérationnalité des duels | Seuils numériques donnés (illustratifs) — utilisables mais fragiles | Seuils explicitement non fixés — intellectuellement rigoureux, non falsifiables |
| Option C (out-of-fold) | Proposée comme voie principale — biais potentiel non marqué HYPOTHÈSE | Mentionnée avec réserve — rejetée faute de vérification d'indépendance |
| Puissance des contrôles | Expérience 2 quasi certaine de passer (référence Bailey trop petite) | Duel 1 quasi certain de passer (même raison) |
| Risque de non-trivialité de la sonde | Non contrôlé | Non contrôlé |
| Risque de dégradation de sortie comptée comme camouflage | Mentionné dans le tableau, pas bloquant | Mentionné dans la section juge, pas structuré en duel |

Les deux propositions convergent vers (B) avec analyse de sensibilité, ce qui me semble correct. Les divergences portent sur les moyens de récupérer des bénins (C propose la validation croisée, D la refuse par prudence). Aucune des deux ne propose le contrôle négatif que je considère le plus critique : vérifier que la sonde capture un signal d'alignement et non un corrélat lexical, et que le « camouflage » ne se réduit pas à une dégradation de la sortie.

FIN-DE-CELLULE